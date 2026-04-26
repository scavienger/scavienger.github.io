---
layout: post
title: "Detect Cycles in 2D Grid"
date: 2026-04-26 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Depth-First Search", "Breadth-First Search", "Union-Find", "Matrix"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/detect-cycles-in-2d-grid/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int find(vector<int>& parent, int i) {\n\
        \        int root = i;\n        while (parent[root] != root) root = parent[root];\n\
        \        while (parent[i] != root) {\n            int next = parent[i];\n  \
        \          parent[i] = root;\n            i = next;\n        }\n        return\
        \ root;\n    }\n\n    bool unite(vector<int>& parent, vector<int>& rank, int\
        \ i, int j) {\n        int root_i = find(parent, i);\n        int root_j = find(parent,\
        \ j);\n        if (root_i == root_j) return false;\n        if (rank[root_i]\
        \ < rank[root_j]) {\n            parent[root_i] = root_j;\n        } else if\
        \ (rank[root_i] > rank[root_j]) {\n            parent[root_j] = root_i;\n  \
        \      } else {\n            parent[root_i] = root_j;\n            rank[root_j]++;\n\
        \        }\n        return true;\n    }\n\n    bool containsCycle(vector<vector<char>>&\
        \ grid) {\n        int m = grid.size();\n        int n = grid[0].size();\n \
        \       vector<int> parent(m * n);\n        vector<int> rank(m * n, 0);\n  \
        \      for (int i = 0; i < m * n; i++) parent[i] = i;\n\n        for (int i\
        \ = 0; i < m; i++) {\n            for (int j = 0; j < n; j++) {\n          \
        \      if (j + 1 < n && grid[i][j] == grid[i][j + 1]) {\n                  \
        \  if (!unite(parent, rank, i * n + j, i * n + j + 1)) return true;\n      \
        \          }\n                if (i + 1 < m && grid[i][j] == grid[i + 1][j])\
        \ {\n                    if (!unite(parent, rank, i * n + j, (i + 1) * n + j))\
        \ return true;\n                }\n            }\n        }\n        return\
        \ false;\n    }\n};"
      java: "class Solution {\n    private int find(int[] parent, int i) {\n       \
        \ int root = i;\n        while (parent[root] != root) root = parent[root];\n\
        \        while (parent[i] != root) {\n            int next = parent[i];\n  \
        \          parent[i] = root;\n            i = next;\n        }\n        return\
        \ root;\n    }\n\n    private boolean unite(int[] parent, int[] rank, int i,\
        \ int j) {\n        int rootI = find(parent, i);\n        int rootJ = find(parent,\
        \ j);\n        if (rootI == rootJ) return false;\n        if (rank[rootI] <\
        \ rank[rootJ]) {\n            parent[rootI] = rootJ;\n        } else if (rank[rootI]\
        \ > rank[rootJ]) {\n            parent[rootJ] = rootI;\n        } else {\n \
        \           parent[rootI] = rootJ;\n            rank[rootJ]++;\n        }\n\
        \        return true;\n    }\n\n    public boolean containsCycle(char[][] grid)\
        \ {\n        int m = grid.length;\n        int n = grid[0].length;\n       \
        \ int[] parent = new int[m * n];\n        int[] rank = new int[m * n];\n   \
        \     for (int i = 0; i < m * n; i++) {\n            parent[i] = i;\n      \
        \      rank[i] = 0;\n        }\n\n        for (int i = 0; i < m; i++) {\n  \
        \          for (int j = 0; j < n; j++) {\n                if (j + 1 < n && grid[i][j]\
        \ == grid[i][j + 1]) {\n                    if (!unite(parent, rank, i * n +\
        \ j, i * n + j + 1)) return true;\n                }\n                if (i\
        \ + 1 < m && grid[i][j] == grid[i + 1][j]) {\n                    if (!unite(parent,\
        \ rank, i * n + j, (i + 1) * n + j)) return true;\n                }\n     \
        \       }\n        }\n        return false;\n    }\n}"
      python: "class Solution(object):\n    def containsCycle(self, grid):\n       \
        \ \"\"\"\n        :type grid: List[List[str]]\n        :rtype: bool\n      \
        \  \"\"\"\n        m = len(grid)\n        n = len(grid[0])\n        parent =\
        \ range(m * n)\n        rank = [0] * (m * n)\n\n        def find(i):\n     \
        \       root = i\n            while parent[root] != root:\n                root\
        \ = parent[root]\n            while parent[i] != root:\n                next_i\
        \ = parent[i]\n                parent[i] = root\n                i = next_i\n\
        \            return root\n\n        def unite(i, j):\n            root_i = find(i)\n\
        \            root_j = find(j)\n            if root_i == root_j: return False\n\
        \            if rank[root_i] < rank[root_j]:\n                parent[root_i]\
        \ = root_j\n            elif rank[root_i] > rank[root_j]:\n                parent[root_j]\
        \ = root_i\n            else:\n                parent[root_i] = root_j\n   \
        \             rank[root_j] += 1\n            return True\n\n        for i in\
        \ xrange(m):\n            for j in xrange(n):\n                if j + 1 < n\
        \ and grid[i][j] == grid[i][j + 1]:\n                    if not unite(i * n\
        \ + j, i * n + j + 1): return True\n                if i + 1 < m and grid[i][j]\
        \ == grid[i + 1][j]:\n                    if not unite(i * n + j, (i + 1) *\
        \ n + j): return True\n        return False"
      python3: "class Solution:\n    def containsCycle(self, grid: List[List[str]])\
        \ -> bool:\n        m, n = len(grid), len(grid[0])\n        parent = list(range(m\
        \ * n))\n        rank = [0] * (m * n)\n\n        def find(i):\n            root\
        \ = i\n            while parent[root] != root:\n                root = parent[root]\n\
        \            while parent[i] != root:\n                parent[i], i = root,\
        \ parent[i]\n            return root\n\n        def unite(i, j):\n         \
        \   root_i = find(i)\n            root_j = find(j)\n            if root_i ==\
        \ root_j:\n                return False\n            if rank[root_i] < rank[root_j]:\n\
        \                parent[root_i] = root_j\n            elif rank[root_i] > rank[root_j]:\n\
        \                parent[root_j] = root_i\n            else:\n              \
        \  parent[root_i] = root_j\n                rank[root_j] += 1\n            return\
        \ True\n\n        for i in range(m):\n            for j in range(n):\n     \
        \           if j + 1 < n and grid[i][j] == grid[i][j + 1]:\n               \
        \     if not unite(i * n + j, i * n + j + 1): return True\n                if\
        \ i + 1 < m and grid[i][j] == grid[i + 1][j]:\n                    if not unite(i\
        \ * n + j, (i + 1) * n + j): return True\n        return False"
      c: "#include <stdbool.h>\n#include <stdlib.h>\n\nint find(int* parent, int i)\
        \ {\n    int root = i;\n    while (parent[root] != root) root = parent[root];\n\
        \    while (parent[i] != root) {\n        int next = parent[i];\n        parent[i]\
        \ = root;\n        i = next;\n    }\n    return root;\n}\n\nbool unite(int*\
        \ parent, int* rank, int i, int j) {\n    int root_i = find(parent, i);\n  \
        \  int root_j = find(parent, j);\n    if (root_i == root_j) return false;\n\
        \    if (rank[root_i] < rank[root_j]) {\n        parent[root_i] = root_j;\n\
        \    } else if (rank[root_i] > rank[root_j]) {\n        parent[root_j] = root_i;\n\
        \    } else {\n        parent[root_i] = root_j;\n        rank[root_j]++;\n \
        \   }\n    return true;\n}\n\nbool containsCycle(char** grid, int gridSize,\
        \ int* gridColSize) {\n    int m = gridSize;\n    int n = gridColSize[0];\n\
        \    int total = m * n;\n    int* parent = (int*)malloc(total * sizeof(int));\n\
        \    int* rank = (int*)malloc(total * sizeof(int));\n    for (int i = 0; i <\
        \ total; i++) {\n        parent[i] = i;\n        rank[i] = 0;\n    }\n\n   \
        \ for (int i = 0; i < m; i++) {\n        for (int j = 0; j < n; j++) {\n   \
        \         if (j + 1 < n && grid[i][j] == grid[i][j + 1]) {\n               \
        \ if (!unite(parent, rank, i * n + j, i * n + (j + 1))) {\n                \
        \    free(parent); free(rank); return true;\n                }\n           \
        \ }\n            if (i + 1 < m && grid[i][j] == grid[i + 1][j]) {\n        \
        \        if (!unite(parent, rank, i * n + j, (i + 1) * n + j)) {\n         \
        \           free(parent); free(rank); return true;\n                }\n    \
        \        }\n        }\n    }\n\n    free(parent);\n    free(rank);\n    return\
        \ false;\n}"
      csharp: "public class Solution {\n    public bool ContainsCycle(char[][] grid)\
        \ {\n        int m = grid.Length;\n        int n = grid[0].Length;\n       \
        \ int[] parent = new int[m * n];\n        for (int i = 0; i < m * n; i++) parent[i]\
        \ = i;\n\n        int Find(int i) {\n            int root = i;\n           \
        \ while (parent[root] != root) root = parent[root];\n            while (parent[i]\
        \ != root) {\n                int next = parent[i];\n                parent[i]\
        \ = root;\n                i = next;\n            }\n            return root;\n\
        \        }\n\n        bool Union(int i, int j) {\n            int rootI = Find(i);\n\
        \            int rootJ = Find(j);\n            if (rootI != rootJ) {\n     \
        \           parent[rootI] = rootJ;\n                return true;\n         \
        \   }\n            return false;\n        }\n\n        for (int r = 0; r < m;\
        \ r++) {\n            for (int c = 0; c < n; c++) {\n                char ch\
        \ = grid[r][c];\n                int u = r * n + c;\n                if (c +\
        \ 1 < n && grid[r][c + 1] == ch) {\n                    int v = r * n + (c +\
        \ 1);\n                    if (!Union(u, v)) return true;\n                }\n\
        \                if (r + 1 < m && grid[r + 1][c] == ch) {\n                \
        \    int v = (r + 1) * n + c;\n                    if (!Union(u, v)) return\
        \ true;\n                }\n            }\n        }\n        return false;\n\
        \    }\n}"
      javascript: "/**\n * @param {character[][]} grid\n * @return {boolean}\n */\n\
        var containsCycle = function(grid) {\n    const m = grid.length;\n    const\
        \ n = grid[0].length;\n    const parent = new Int32Array(m * n);\n    for (let\
        \ i = 0; i < m * n; i++) parent[i] = i;\n\n    function find(i) {\n        let\
        \ root = i;\n        while (parent[root] !== root) root = parent[root];\n  \
        \      while (parent[i] !== root) {\n            let next = parent[i];\n   \
        \         parent[i] = root;\n            i = next;\n        }\n        return\
        \ root;\n    }\n\n    function union(i, j) {\n        let rootI = find(i);\n\
        \        let rootJ = find(j);\n        if (rootI !== rootJ) {\n            parent[rootI]\
        \ = rootJ;\n            return true;\n        }\n        return false;\n   \
        \ }\n\n    for (let r = 0; r < m; r++) {\n        for (let c = 0; c < n; c++)\
        \ {\n            const char = grid[r][c];\n            const u = r * n + c;\n\
        \            if (c + 1 < n && grid[r][c + 1] === char) {\n                if\
        \ (!union(u, r * n + c + 1)) return true;\n            }\n            if (r\
        \ + 1 < m && grid[r + 1][c] === char) {\n                if (!union(u, (r +\
        \ 1) * n + c)) return true;\n            }\n        }\n    }\n    return false;\n\
        };"
      typescript: "function containsCycle(grid: string[][]): boolean {\n    const m\
        \ = grid.length;\n    const n = grid[0].length;\n    const parent = new Int32Array(m\
        \ * n);\n    for (let i = 0; i < m * n; i++) parent[i] = i;\n\n    function\
        \ find(i: number): number {\n        let root = i;\n        while (parent[root]\
        \ !== root) root = parent[root];\n        while (parent[i] !== root) {\n   \
        \         let next = parent[i];\n            parent[i] = root;\n           \
        \ i = next;\n        }\n        return root;\n    }\n\n    function union(i:\
        \ number, j: number): boolean {\n        let rootI = find(i);\n        let rootJ\
        \ = find(j);\n        if (rootI !== rootJ) {\n            parent[rootI] = rootJ;\n\
        \            return true;\n        }\n        return false;\n    }\n\n    for\
        \ (let r = 0; r < m; r++) {\n        for (let c = 0; c < n; c++) {\n       \
        \     const char = grid[r][c];\n            const u = r * n + c;\n         \
        \   if (c + 1 < n && grid[r][c + 1] === char) {\n                if (!union(u,\
        \ r * n + c + 1)) return true;\n            }\n            if (r + 1 < m &&\
        \ grid[r + 1][c] === char) {\n                if (!union(u, (r + 1) * n + c))\
        \ return true;\n            }\n        }\n    }\n    return false;\n};"
      php: "class Solution {\n\n    /**\n     * @param String[][] $grid\n     * @return\
        \ Boolean\n     */\n    function containsCycle($grid) {\n        $m = count($grid);\n\
        \        if ($m === 0) return false;\n        $n = count($grid[0]);\n      \
        \  $parent = range(0, $m * $n - 1);\n\n        $find = function($i) use (&$parent)\
        \ {\n            $root = $i;\n            while ($parent[$root] != $root) {\n\
        \                $root = $parent[$root];\n            }\n            while ($parent[$i]\
        \ != $root) {\n                $next = $parent[$i];\n                $parent[$i]\
        \ = $root;\n                $i = $next;\n            }\n            return $root;\n\
        \        };\n\n        for ($r = 0; $r < $m; $r++) {\n            for ($c =\
        \ 0; $c < $n; $c++) {\n                $char = $grid[$r][$c];\n            \
        \    $u = $r * $n + $c;\n                if ($c + 1 < $n && $grid[$r][$c + 1]\
        \ === $char) {\n                    $v = $r * $n + $c + 1;\n               \
        \     $rootU = $find($u);\n                    $rootV = $find($v);\n       \
        \             if ($rootU === $rootV) return true;\n                    $parent[$rootU]\
        \ = $rootV;\n                }\n                if ($r + 1 < $m && $grid[$r\
        \ + 1][$c] === $char) {\n                    $v = ($r + 1) * $n + $c;\n    \
        \                $rootU = $find($u);\n                    $rootV = $find($v);\n\
        \                    if ($rootU === $rootV) return true;\n                 \
        \   $parent[$rootU] = $rootV;\n                }\n            }\n        }\n\
        \        return false;\n    }\n}"
      swift: "class Solution {\n    func containsCycle(_ grid: [[Character]]) -> Bool\
        \ {\n        let m = grid.count\n        if m == 0 { return false }\n      \
        \  let n = grid[0].count\n        var parent = Array(0..<(m * n))\n\n      \
        \  func find(_ i: Int) -> Int {\n            var root = i\n            while\
        \ parent[root] != root {\n                root = parent[root]\n            }\n\
        \            var curr = i\n            while parent[curr] != root {\n      \
        \          let next = parent[curr]\n                parent[curr] = root\n  \
        \              curr = next\n            }\n            return root\n       \
        \ }\n\n        func union(_ i: Int, _ j: Int) -> Bool {\n            let rootI\
        \ = find(i)\n            let rootJ = find(j)\n            if rootI != rootJ\
        \ {\n                parent[rootI] = rootJ\n                return true\n  \
        \          }\n            return false\n        }\n\n        for r in 0..<m\
        \ {\n            for c in 0..<n {\n                let char = grid[r][c]\n \
        \               let u = r * n + c\n                if c + 1 < n && grid[r][c\
        \ + 1] == char {\n                    let v = r * n + c + 1\n              \
        \      if !union(u, v) {\n                        return true\n            \
        \        }\n                }\n                if r + 1 < m && grid[r + 1][c]\
        \ == char {\n                    let v = (r + 1) * n + c\n                 \
        \   if !union(u, v) {\n                        return true\n               \
        \     }\n                }\n            }\n        }\n        return false\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun containsCycle(grid: Array<CharArray>): Boolean\
        \ {\n        val m = grid.size\n        val n = grid[0].size\n        val parent\
        \ = IntArray(m * n) { it }\n\n        fun find(idx: Int): Int {\n          \
        \  var root = idx\n            while (parent[root] != root) {\n            \
        \    root = parent[root]\n            }\n            var curr = idx\n      \
        \      while (parent[curr] != root) {\n                val next = parent[curr]\n\
        \                parent[curr] = root\n                curr = next\n        \
        \    }\n            return root\n        }\n\n        for (r in 0 until m) {\n\
        \            for (c in 0 until n) {\n                val char = grid[r][c]\n\
        \                if (c + 1 < n && grid[r][c + 1] == char) {\n              \
        \      val root1 = find(r * n + c)\n                    val root2 = find(r *\
        \ n + c + 1)\n                    if (root1 == root2) return true\n        \
        \            parent[root1] = root2\n                }\n                if (r\
        \ + 1 < m && grid[r + 1][c] == char) {\n                    val root1 = find(r\
        \ * n + c)\n                    val root2 = find((r + 1) * n + c)\n        \
        \            if (root1 == root2) return true\n                    parent[root1]\
        \ = root2\n                }\n            }\n        }\n        return false\n\
        \    }\n}"
      dart: "class Solution {\n  bool containsCycle(List<List<String>> grid) {\n   \
        \ int m = grid.length;\n    int n = grid[0].length;\n    List<int> parent =\
        \ List.generate(m * n, (i) => i);\n\n    int find(int idx) {\n      int root\
        \ = idx;\n      while (parent[root] != root) {\n        root = parent[root];\n\
        \      }\n      int curr = idx;\n      while (parent[curr] != root) {\n    \
        \    int next = parent[curr];\n        parent[curr] = root;\n        curr =\
        \ next;\n      }\n      return root;\n    }\n\n    for (int r = 0; r < m; r++)\
        \ {\n      for (int c = 0; c < n; c++) {\n        String char = grid[r][c];\n\
        \        if (c + 1 < n && grid[r][c + 1] == char) {\n          int root1 = find(r\
        \ * n + c);\n          int root2 = find(r * n + c + 1);\n          if (root1\
        \ == root2) return true;\n          parent[root1] = root2;\n        }\n    \
        \    if (r + 1 < m && grid[r + 1][c] == char) {\n          int root1 = find(r\
        \ * n + c);\n          int root2 = find((r + 1) * n + c);\n          if (root1\
        \ == root2) return true;\n          parent[root1] = root2;\n        }\n    \
        \  }\n    }\n    return false;\n  }\n}"
      go: "func containsCycle(grid [][]byte) bool {\n    m := len(grid)\n    n := len(grid[0])\n\
        \    parent := make([]int, m*n)\n    for i := range parent {\n        parent[i]\
        \ = i\n    }\n\n    find := func(idx int) int {\n        root := idx\n     \
        \   for parent[root] != root {\n            root = parent[root]\n        }\n\
        \        curr := idx\n        for parent[curr] != root {\n            next :=\
        \ parent[curr]\n            parent[curr] = root\n            curr = next\n \
        \       }\n        return root\n    }\n\n    for r := 0; r < m; r++ {\n    \
        \    for c := 0; c < n; c++ {\n            char := grid[r][c]\n            if\
        \ c+1 < n && grid[r][c+1] == char {\n                root1 := find(r*n + c)\n\
        \                root2 := find(r*n + c + 1)\n                if root1 == root2\
        \ {\n                    return true\n                }\n                parent[root1]\
        \ = root2\n            }\n            if r+1 < m && grid[r+1][c] == char {\n\
        \                root1 := find(r*n + c)\n                root2 := find((r+1)*n\
        \ + c)\n                if root1 == root2 {\n                    return true\n\
        \                }\n                parent[root1] = root2\n            }\n \
        \       }\n    }\n    return false\n}"
      ruby: "def contains_cycle(grid)\n  m = grid.length\n  n = grid[0].length\n  parent\
        \ = Array.new(m * n) { |i| i }\n\n  find = lambda do |idx|\n    root = idx\n\
        \    while parent[root] != root\n      root = parent[root]\n    end\n    curr\
        \ = idx\n    while parent[curr] != root\n      next_node = parent[curr]\n  \
        \    parent[curr] = root\n      curr = next_node\n    end\n    root\n  end\n\
        \n  (0...m).each do |r|\n    (0...n).each do |c|\n      char = grid[r][c]\n\
        \      if c + 1 < n && grid[r][c + 1] == char\n        root1 = find.call(r *\
        \ n + c)\n        root2 = find.call(r * n + c + 1)\n        return true if root1\
        \ == root2\n        parent[root1] = root2\n      end\n      if r + 1 < m &&\
        \ grid[r + 1][c] == char\n        root1 = find.call(r * n + c)\n        root2\
        \ = find.call((r + 1) * n + c)\n        return true if root1 == root2\n    \
        \    parent[root1] = root2\n      end\n    end\n  end\n  false\nend"
      scala: "object Solution {\n    def containsCycle(grid: Array[Array[Char]]): Boolean\
        \ = {\n        val m = grid.length\n        val n = grid(0).length\n       \
        \ val parent = Array.tabulate(m * n)(i => i)\n\n        def find(idx: Int):\
        \ Int = {\n            var root = idx\n            while (parent(root) != root)\
        \ {\n                root = parent(root)\n            }\n            var curr\
        \ = idx\n            while (parent(curr) != root) {\n                val next\
        \ = parent(curr)\n                parent(curr) = root\n                curr\
        \ = next\n            }\n            root\n        }\n\n        for (r <- 0\
        \ until m) {\n            for (c <- 0 until n) {\n                val char =\
        \ grid(r)(c)\n                if (c + 1 < n && grid(r)(c + 1) == char) {\n \
        \                   val root1 = find(r * n + c)\n                    val root2\
        \ = find(r * n + c + 1)\n                    if (root1 == root2) return true\n\
        \                    parent(root1) = root2\n                }\n            \
        \    if (r + 1 < m && grid(r + 1)(c) == char) {\n                    val root1\
        \ = find(r * n + c)\n                    val root2 = find((r + 1) * n + c)\n\
        \                    if (root1 == root2) return true\n                    parent(root1)\
        \ = root2\n                }\n            }\n        }\n        false\n    }\n\
        }"
      rust: "impl Solution {\n    pub fn contains_cycle(grid: Vec<Vec<char>>) -> bool\
        \ {\n        let m = grid.len();\n        let n = grid[0].len();\n        let\
        \ mut parent: Vec<usize> = (0..m * n).collect();\n        let mut rank: Vec<usize>\
        \ = vec![0; m * n];\n\n        for r in 0..m {\n            for c in 0..n {\n\
        \                let u = r * n + c;\n                let char_u = grid[r][c];\n\
        \n                if c + 1 < n && grid[r][c + 1] == char_u {\n             \
        \       let v = r * n + (c + 1);\n                    if !Self::unite(&mut parent,\
        \ &mut rank, u, v) {\n                        return true;\n               \
        \     }\n                }\n\n                if r + 1 < m && grid[r + 1][c]\
        \ == char_u {\n                    let v = (r + 1) * n + c;\n              \
        \      if !Self::unite(&mut parent, &mut rank, u, v) {\n                   \
        \     return true;\n                    }\n                }\n            }\n\
        \        }\n        false\n    }\n\n    fn find(parent: &mut Vec<usize>, mut\
        \ i: usize) -> usize {\n        let mut root = i;\n        while parent[root]\
        \ != root {\n            root = parent[root];\n        }\n        while parent[i]\
        \ != root {\n            let next = parent[i];\n            parent[i] = root;\n\
        \            i = next;\n        }\n        root\n    }\n\n    fn unite(parent:\
        \ &mut Vec<usize>, rank: &mut Vec<usize>, i: usize, j: usize) -> bool {\n  \
        \      let root_i = Self::find(parent, i);\n        let root_j = Self::find(parent,\
        \ j);\n        if root_i == root_j {\n            return false;\n        }\n\
        \        if rank[root_i] < rank[root_j] {\n            parent[root_i] = root_j;\n\
        \        } else if rank[root_i] > rank[root_j] {\n            parent[root_j]\
        \ = root_i;\n        } else {\n            parent[root_i] = root_j;\n      \
        \      rank[root_j] += 1;\n        }\n        true\n    }\n}"
      racket: "(define/contract (contains-cycle grid)\n  (-> (listof (listof char?))\
        \ boolean?)\n  (let* ([m (length grid)]\n         [n (length (first grid))]\n\
        \         [grid-vec (list->vector (map list->vector grid))]\n         [parent\
        \ (build-vector (* m n) (lambda (i) i))]\n         [rank (make-vector (* m n)\
        \ 0)])\n    (letrec ([find (lambda (i)\n                     (let ([val (vector-ref\
        \ parent i)])\n                       (if (= val i)\n                      \
        \     i\n                           (let ([root (find val)])\n             \
        \                (vector-set! parent i root)\n                             root))))]\n\
        \             [unite (lambda (root1 root2)\n                      (let ([r1\
        \ (vector-ref rank root1)]\n                            [r2 (vector-ref rank\
        \ root2)])\n                        (cond\n                          [(< r1\
        \ r2) (vector-set! parent root1 root2)]\n                          [(> r1 r2)\
        \ (vector-set! parent root2 root1)]\n                          [else\n     \
        \                      (vector-set! parent root1 root2)\n                  \
        \         (vector-set! rank root2 (+ r2 1))])))]\n             [loop-r (lambda\
        \ (r)\n                       (if (= r m)\n                           #f\n \
        \                          (let loop-c ([c 0])\n                           \
        \  (if (= c n)\n                                 (loop-r (+ r 1))\n        \
        \                         (let* ([char (vector-ref (vector-ref grid-vec r) c)]\n\
        \                                        [u (+ (* r n) c)])\n              \
        \                     (let ([res-r (if (and (< (+ c 1) n)\n                \
        \                                         (char=? char (vector-ref (vector-ref\
        \ grid-vec r) (+ c 1))))\n                                                 \
        \   (let* ([v (+ (* r n) (+ c 1))]\n                                       \
        \                    [root-u (find u)]\n                                   \
        \                        [root-v (find v)])\n                              \
        \                        (if (= root-u root-v)\n                           \
        \                               #t\n                                       \
        \                   (begin (unite root-u root-v) #f)))\n                   \
        \                                 #f)])\n                                  \
        \   (if res-r\n                                         #t\n               \
        \                          (let ([res-b (if (and (< (+ r 1) m)\n           \
        \                                                    (char=? char (vector-ref\
        \ (vector-ref grid-vec (+ r 1)) c)))\n                                     \
        \                     (let* ([v (+ (* (+ r 1) n) c)]\n                     \
        \                                            [root-u (find u)]\n           \
        \                                                      [root-v (find v)])\n\
        \                                                            (if (= root-u root-v)\n\
        \                                                                #t\n      \
        \                                                          (begin (unite root-u\
        \ root-v) #f)))\n                                                          #f)])\n\
        \                                           (if res-b\n                    \
        \                           #t\n                                           \
        \    (loop-c (+ c 1))))))))))])\n      (loop-r 0))))"
      erlang: "-spec contains_cycle(Grid :: [[char()]]) -> boolean().\ncontains_cycle(Grid)\
        \ ->\n    M = length(Grid),\n    N = length(hd(Grid)),\n    GridTuple = list_to_tuple([list_to_tuple(Row)\
        \ || Row <- Grid]),\n    Parent = array:from_list(lists:seq(0, M * N - 1)),\n\
        \    Rank = array:new(M * N, {default, 0}),\n    check_cells(0, 0, M, N, GridTuple,\
        \ Parent, Rank).\n\nfind(I, Parent) ->\n    Val = array:get(I, Parent),\n  \
        \  if Val == I -> {I, Parent};\n       true ->\n           {Root, P1} = find(Val,\
        \ Parent),\n           P2 = array:set(I, Root, P1),\n           {Root, P2}\n\
        \    end.\n\nunion_uf(Root1, Root2, Parent, Rank) ->\n    Rank1 = array:get(Root1,\
        \ Rank),\n    Rank2 = array:get(Root2, Rank),\n    if Rank1 < Rank2 -> {array:set(Root1,\
        \ Root2, Parent), Rank};\n       Rank1 > Rank2 -> {array:set(Root2, Root1, Parent),\
        \ Rank};\n       true ->\n           P1 = array:set(Root1, Root2, Parent),\n\
        \           R1 = array:set(Root2, Rank2 + 1, Rank),\n           {P1, R1}\n \
        \   end.\n\ncheck_cells(R, _C, M, _N, _GridTuple, _Parent, _Rank) when R ==\
        \ M -> false;\ncheck_cells(R, C, M, N, GridTuple, Parent, Rank) when C == N\
        \ -> \n    check_cells(R + 1, 0, M, N, GridTuple, Parent, Rank);\ncheck_cells(R,\
        \ C, M, N, GridTuple, Parent, Rank) ->\n    Char = element(C + 1, element(R\
        \ + 1, GridTuple)),\n    {CycleR, P1, R1} = \n        if C + 1 < N ->\n    \
        \        case element(C + 2, element(R + 1, GridTuple)) of\n               \
        \ Char ->\n                    U = R * N + C,\n                    V = R * N\
        \ + C + 1,\n                    {RootU, PA} = find(U, Parent),\n           \
        \         {RootV, PB} = find(V, PA),\n                    if RootU == RootV\
        \ -> {true, PB, Rank};\n                       true -> {NewP, NewR} = union_uf(RootU,\
        \ RootV, PB, Rank), {false, NewP, NewR}\n                    end;\n        \
        \        _ -> {false, Parent, Rank}\n            end;\n           true -> {false,\
        \ Parent, Rank}\n        end,\n    if CycleR -> true;\n       true ->\n    \
        \       {CycleB, P2, R2} = \n               if R + 1 < M ->\n              \
        \     case element(C + 1, element(R + 2, GridTuple)) of\n                  \
        \     Char ->\n                           U = R * N + C,\n                 \
        \          V = (R + 1) * N + C,\n                           {RootU, PA2} = find(U,\
        \ P1),\n                           {RootV, PB2} = find(V, PA2),\n          \
        \                 if RootU == RootV -> {true, PB2, R1};\n                  \
        \            true -> {NewP2, NewR2} = union_uf(RootU, RootV, PB2, R1), {false,\
        \ NewP2, NewR2}\n                           end;\n                       _ ->\
        \ {false, P1, R1}\n                   end;\n                  true -> {false,\
        \ P1, R1}\n               end,\n           if CycleB -> true;\n            \
        \  true -> check_cells(R, C + 1, M, N, GridTuple, P2, R2)\n           end\n\
        \    end."
      elixir: "defmodule Solution do\n  @spec contains_cycle(grid :: [[char]]) :: boolean\n\
        \  def contains_cycle(grid) do\n    m = length(grid)\n    n = length(hd(grid))\n\
        \    grid_tuple = grid |> Enum.map(&List.to_tuple/1) |> List.to_tuple()\n\n\
        \    Enum.reduce_while(0..m-1, {%{}, %{}}, fn r, {parent, rank} ->\n      case\
        \ Enum.reduce_while(0..n-1, {parent, rank}, fn c, {p, rk} ->\n        char =\
        \ elem(elem(grid_tuple, r), c)\n\n        {cycle_r, p1, rk1} = if c + 1 < n\
        \ and elem(elem(grid_tuple, r), c + 1) == char do\n          u = r * n + c\n\
        \          v = r * n + c + 1\n          {root_u, p_u} = find(u, p)\n       \
        \   {root_v, p_v} = find(v, p_u)\n          if root_u == root_v, do: {true,\
        \ p_v, rk}, else: (\n            {p_union, rk_union} = union_uf(root_u, root_v,\
        \ p_v, rk)\n            {false, p_union, rk_union}\n          )\n        else\n\
        \          {false, p, rk}\n        end\n\n        if cycle_r do\n          {:halt,\
        \ :cycle}\n        else\n          {cycle_b, p2, rk2} = if r + 1 < m and elem(elem(grid_tuple,\
        \ r + 1), c) == char do\n            u = r * n + c\n            v = (r + 1)\
        \ * n + c\n            {root_u, p_u_b} = find(u, p1)\n            {root_v, p_v_b}\
        \ = find(v, p_u_b)\n            if root_u == root_v, do: {true, p_v_b, rk1},\
        \ else: (\n              {p_union_b, rk_union_b} = union_uf(root_u, root_v,\
        \ p_v_b, rk1)\n              {false, p_union_b, rk_union_b}\n            )\n\
        \          else\n            {false, p1, rk1}\n          end\n\n          if\
        \ cycle_b, do: {:halt, :cycle}, else: {:cont, {p2, rk2}}\n        end\n    \
        \  end) do\n        :cycle -> {:halt, true}\n        {p_next, rk_next} -> {:cont,\
        \ {p_next, rk_next}}\n      end\n    end) == true\n  end\n\n  defp find(i, parent)\
        \ do\n    val = Map.get(parent, i, i)\n    if val == i do\n      {i, parent}\n\
        \    else\n      {root, p_new} = find(val, parent)\n      {root, Map.put(p_new,\
        \ i, root)}\n    end\n  end\n\n  defp union_uf(root1, root2, parent, rank) do\n\
        \    r1 = Map.get(rank, root1, 0)\n    r2 = Map.get(rank, root2, 0)\n    cond\
        \ do\n      r1 < r2 -> {Map.put(parent, root1, root2), rank}\n      r1 > r2\
        \ -> {Map.put(parent, root2, root1), rank}\n      true ->\n        p1 = Map.put(parent,\
        \ root1, root2)\n        rk1 = Map.put(rank, root2, r2 + 1)\n        {p1, rk1}\n\
        \    end\n  end\nend"
    approach: 'The problem can be modeled as finding a cycle in an undirected graph
      where each cell (r, c) represents a node. Edges exist between adjacent cells that
      share the same character value. According to the grid''s topology, the shortest
      possible cycle in such a graph (without immediately revisiting the parent cell)
      must have a length of at least 4. This observation allows us to simplify the cycle
      detection: if we treat each pair of identical adjacent cells as an undirected
      edge and find that an edge connects two nodes already belonging to the same connected
      component, a cycle of length at least 4 is guaranteed to exist.


      We implement this using the Disjoint Set Union (DSU) algorithm with path compression
      and union by rank for optimal performance. We iterate through every cell in the
      grid and process only its right and bottom neighbors to ensure each potential
      edge is considered exactly once. If a neighbor contains the same character as
      the current cell, we check if they already share the same root in the DSU. If
      they do, a cycle is detected and we return true. Otherwise, we unite their sets
      and continue. This efficiently handles the connectivity of identical characters
      across the 2D grid.'
    time_complexity: O(M * N * alpha(M * N)), where M and N are the grid dimensions
      and alpha is the inverse Ackermann function. This complexity arises because we
      iterate through each of the M * N cells once and perform a constant number of
      DSU operations per cell, which take nearly constant time.
    space_complexity: O(M * N) to store the parent and rank arrays for the Disjoint
      Set Union data structure, where each array has a size equal to the total number
      of cells in the grid.
    elapsed_time: 429.434787273407
    model: gemini-3-flash-preview
    generated_at: '2026-04-26 02:08:39 '
---

## Problem #1559: Detect Cycles in 2D Grid

**Difficulty:** Medium

**Topics:** Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix

## Problem Description

<p>Given a 2D array of characters <code>grid</code> of size <code>m x n</code>, you need to find if there exists any cycle consisting of the <strong>same value</strong> in <code>grid</code>.</p>

<p>A cycle is a path of <strong>length 4 or more</strong> in the grid that starts and ends at the same cell. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the <strong>same value</strong> of the current cell.</p>

<p>Also, you cannot move to the cell that you visited in your last move. For example, the cycle <code>(1, 1) -&gt; (1, 2) -&gt; (1, 1)</code> is invalid because from <code>(1, 2)</code> we visited <code>(1, 1)</code> which was the last visited cell.</p>

<p>Return <code>true</code> if any cycle of the same value exists in <code>grid</code>, otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2020/07/15/1.png" style="width: 231px; height: 152px;" /></strong></p>

<pre>
<strong>Input:</strong> grid = [[&quot;a&quot;,&quot;a&quot;,&quot;a&quot;,&quot;a&quot;],[&quot;a&quot;,&quot;b&quot;,&quot;b&quot;,&quot;a&quot;],[&quot;a&quot;,&quot;b&quot;,&quot;b&quot;,&quot;a&quot;],[&quot;a&quot;,&quot;a&quot;,&quot;a&quot;,&quot;a&quot;]]
<strong>Output:</strong> true
<strong>Explanation: </strong>There are two valid cycles shown in different colors in the image below:
<img alt="" src="https://assets.leetcode.com/uploads/2020/07/15/11.png" style="width: 225px; height: 163px;" />
</pre>

<p><strong class="example">Example 2:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2020/07/15/22.png" style="width: 236px; height: 154px;" /></strong></p>

<pre>
<strong>Input:</strong> grid = [[&quot;c&quot;,&quot;c&quot;,&quot;c&quot;,&quot;a&quot;],[&quot;c&quot;,&quot;d&quot;,&quot;c&quot;,&quot;c&quot;],[&quot;c&quot;,&quot;c&quot;,&quot;e&quot;,&quot;c&quot;],[&quot;f&quot;,&quot;c&quot;,&quot;c&quot;,&quot;c&quot;]]
<strong>Output:</strong> true
<strong>Explanation: </strong>There is only one valid cycle highlighted in the image below:
<img alt="" src="https://assets.leetcode.com/uploads/2020/07/15/2.png" style="width: 229px; height: 157px;" />
</pre>

<p><strong class="example">Example 3:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2020/07/15/3.png" style="width: 183px; height: 120px;" /></strong></p>

<pre>
<strong>Input:</strong> grid = [[&quot;a&quot;,&quot;b&quot;,&quot;b&quot;],[&quot;b&quot;,&quot;z&quot;,&quot;b&quot;],[&quot;b&quot;,&quot;b&quot;,&quot;a&quot;]]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 500</code></li>
	<li><code>grid</code> consists only of lowercase English letters.</li>
</ul>


## Hints

1. Keep track of the parent (previous position) to avoid considering an invalid path.

2. Use DFS or BFS and keep track of visited cells to see if there is a cycle.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be modeled as finding a cycle in an undirected graph where each cell (r, c) represents a node. Edges exist between adjacent cells that share the same character value. According to the grid's topology, the shortest possible cycle in such a graph (without immediately revisiting the parent cell) must have a length of at least 4. This observation allows us to simplify the cycle detection: if we treat each pair of identical adjacent cells as an undirected edge and find that an edge connects two nodes already belonging to the same connected component, a cycle of length at least 4 is guaranteed to exist.

We implement this using the Disjoint Set Union (DSU) algorithm with path compression and union by rank for optimal performance. We iterate through every cell in the grid and process only its right and bottom neighbors to ensure each potential edge is considered exactly once. If a neighbor contains the same character as the current cell, we check if they already share the same root in the DSU. If they do, a cycle is detected and we return true. Otherwise, we unite their sets and continue. This efficiently handles the connectivity of identical characters across the 2D grid.

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
    int find(vector<int>& parent, int i) {
        int root = i;
        while (parent[root] != root) root = parent[root];
        while (parent[i] != root) {
            int next = parent[i];
            parent[i] = root;
            i = next;
        }
        return root;
    }

    bool unite(vector<int>& parent, vector<int>& rank, int i, int j) {
        int root_i = find(parent, i);
        int root_j = find(parent, j);
        if (root_i == root_j) return false;
        if (rank[root_i] < rank[root_j]) {
            parent[root_i] = root_j;
        } else if (rank[root_i] > rank[root_j]) {
            parent[root_j] = root_i;
        } else {
            parent[root_i] = root_j;
            rank[root_j]++;
        }
        return true;
    }

    bool containsCycle(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<int> parent(m * n);
        vector<int> rank(m * n, 0);
        for (int i = 0; i < m * n; i++) parent[i] = i;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (j + 1 < n && grid[i][j] == grid[i][j + 1]) {
                    if (!unite(parent, rank, i * n + j, i * n + j + 1)) return true;
                }
                if (i + 1 < m && grid[i][j] == grid[i + 1][j]) {
                    if (!unite(parent, rank, i * n + j, (i + 1) * n + j)) return true;
                }
            }
        }
        return false;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    private int find(int[] parent, int i) {
        int root = i;
        while (parent[root] != root) root = parent[root];
        while (parent[i] != root) {
            int next = parent[i];
            parent[i] = root;
            i = next;
        }
        return root;
    }

    private boolean unite(int[] parent, int[] rank, int i, int j) {
        int rootI = find(parent, i);
        int rootJ = find(parent, j);
        if (rootI == rootJ) return false;
        if (rank[rootI] < rank[rootJ]) {
            parent[rootI] = rootJ;
        } else if (rank[rootI] > rank[rootJ]) {
            parent[rootJ] = rootI;
        } else {
            parent[rootI] = rootJ;
            rank[rootJ]++;
        }
        return true;
    }

    public boolean containsCycle(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[] parent = new int[m * n];
        int[] rank = new int[m * n];
        for (int i = 0; i < m * n; i++) {
            parent[i] = i;
            rank[i] = 0;
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (j + 1 < n && grid[i][j] == grid[i][j + 1]) {
                    if (!unite(parent, rank, i * n + j, i * n + j + 1)) return true;
                }
                if (i + 1 < m && grid[i][j] == grid[i + 1][j]) {
                    if (!unite(parent, rank, i * n + j, (i + 1) * n + j)) return true;
                }
            }
        }
        return false;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])
        parent = range(m * n)
        rank = [0] * (m * n)

        def find(i):
            root = i
            while parent[root] != root:
                root = parent[root]
            while parent[i] != root:
                next_i = parent[i]
                parent[i] = root
                i = next_i
            return root

        def unite(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i == root_j: return False
            if rank[root_i] < rank[root_j]:
                parent[root_i] = root_j
            elif rank[root_i] > rank[root_j]:
                parent[root_j] = root_i
            else:
                parent[root_i] = root_j
                rank[root_j] += 1
            return True

        for i in xrange(m):
            for j in xrange(n):
                if j + 1 < n and grid[i][j] == grid[i][j + 1]:
                    if not unite(i * n + j, i * n + j + 1): return True
                if i + 1 < m and grid[i][j] == grid[i + 1][j]:
                    if not unite(i * n + j, (i + 1) * n + j): return True
        return False
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        parent = list(range(m * n))
        rank = [0] * (m * n)

        def find(i):
            root = i
            while parent[root] != root:
                root = parent[root]
            while parent[i] != root:
                parent[i], i = root, parent[i]
            return root

        def unite(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i == root_j:
                return False
            if rank[root_i] < rank[root_j]:
                parent[root_i] = root_j
            elif rank[root_i] > rank[root_j]:
                parent[root_j] = root_i
            else:
                parent[root_i] = root_j
                rank[root_j] += 1
            return True

        for i in range(m):
            for j in range(n):
                if j + 1 < n and grid[i][j] == grid[i][j + 1]:
                    if not unite(i * n + j, i * n + j + 1): return True
                if i + 1 < m and grid[i][j] == grid[i + 1][j]:
                    if not unite(i * n + j, (i + 1) * n + j): return True
        return False
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdbool.h>
#include <stdlib.h>

int find(int* parent, int i) {
    int root = i;
    while (parent[root] != root) root = parent[root];
    while (parent[i] != root) {
        int next = parent[i];
        parent[i] = root;
        i = next;
    }
    return root;
}

bool unite(int* parent, int* rank, int i, int j) {
    int root_i = find(parent, i);
    int root_j = find(parent, j);
    if (root_i == root_j) return false;
    if (rank[root_i] < rank[root_j]) {
        parent[root_i] = root_j;
    } else if (rank[root_i] > rank[root_j]) {
        parent[root_j] = root_i;
    } else {
        parent[root_i] = root_j;
        rank[root_j]++;
    }
    return true;
}

bool containsCycle(char** grid, int gridSize, int* gridColSize) {
    int m = gridSize;
    int n = gridColSize[0];
    int total = m * n;
    int* parent = (int*)malloc(total * sizeof(int));
    int* rank = (int*)malloc(total * sizeof(int));
    for (int i = 0; i < total; i++) {
        parent[i] = i;
        rank[i] = 0;
    }

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (j + 1 < n && grid[i][j] == grid[i][j + 1]) {
                if (!unite(parent, rank, i * n + j, i * n + (j + 1))) {
                    free(parent); free(rank); return true;
                }
            }
            if (i + 1 < m && grid[i][j] == grid[i + 1][j]) {
                if (!unite(parent, rank, i * n + j, (i + 1) * n + j)) {
                    free(parent); free(rank); return true;
                }
            }
        }
    }

    free(parent);
    free(rank);
    return false;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool ContainsCycle(char[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        int[] parent = new int[m * n];
        for (int i = 0; i < m * n; i++) parent[i] = i;

        int Find(int i) {
            int root = i;
            while (parent[root] != root) root = parent[root];
            while (parent[i] != root) {
                int next = parent[i];
                parent[i] = root;
                i = next;
            }
            return root;
        }

        bool Union(int i, int j) {
            int rootI = Find(i);
            int rootJ = Find(j);
            if (rootI != rootJ) {
                parent[rootI] = rootJ;
                return true;
            }
            return false;
        }

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                char ch = grid[r][c];
                int u = r * n + c;
                if (c + 1 < n && grid[r][c + 1] == ch) {
                    int v = r * n + (c + 1);
                    if (!Union(u, v)) return true;
                }
                if (r + 1 < m && grid[r + 1][c] == ch) {
                    int v = (r + 1) * n + c;
                    if (!Union(u, v)) return true;
                }
            }
        }
        return false;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {character[][]} grid
 * @return {boolean}
 */
var containsCycle = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    const parent = new Int32Array(m * n);
    for (let i = 0; i < m * n; i++) parent[i] = i;

    function find(i) {
        let root = i;
        while (parent[root] !== root) root = parent[root];
        while (parent[i] !== root) {
            let next = parent[i];
            parent[i] = root;
            i = next;
        }
        return root;
    }

    function union(i, j) {
        let rootI = find(i);
        let rootJ = find(j);
        if (rootI !== rootJ) {
            parent[rootI] = rootJ;
            return true;
        }
        return false;
    }

    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            const char = grid[r][c];
            const u = r * n + c;
            if (c + 1 < n && grid[r][c + 1] === char) {
                if (!union(u, r * n + c + 1)) return true;
            }
            if (r + 1 < m && grid[r + 1][c] === char) {
                if (!union(u, (r + 1) * n + c)) return true;
            }
        }
    }
    return false;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function containsCycle(grid: string[][]): boolean {
    const m = grid.length;
    const n = grid[0].length;
    const parent = new Int32Array(m * n);
    for (let i = 0; i < m * n; i++) parent[i] = i;

    function find(i: number): number {
        let root = i;
        while (parent[root] !== root) root = parent[root];
        while (parent[i] !== root) {
            let next = parent[i];
            parent[i] = root;
            i = next;
        }
        return root;
    }

    function union(i: number, j: number): boolean {
        let rootI = find(i);
        let rootJ = find(j);
        if (rootI !== rootJ) {
            parent[rootI] = rootJ;
            return true;
        }
        return false;
    }

    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            const char = grid[r][c];
            const u = r * n + c;
            if (c + 1 < n && grid[r][c + 1] === char) {
                if (!union(u, r * n + c + 1)) return true;
            }
            if (r + 1 < m && grid[r + 1][c] === char) {
                if (!union(u, (r + 1) * n + c)) return true;
            }
        }
    }
    return false;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String[][] $grid
     * @return Boolean
     */
    function containsCycle($grid) {
        $m = count($grid);
        if ($m === 0) return false;
        $n = count($grid[0]);
        $parent = range(0, $m * $n - 1);

        $find = function($i) use (&$parent) {
            $root = $i;
            while ($parent[$root] != $root) {
                $root = $parent[$root];
            }
            while ($parent[$i] != $root) {
                $next = $parent[$i];
                $parent[$i] = $root;
                $i = $next;
            }
            return $root;
        };

        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                $char = $grid[$r][$c];
                $u = $r * $n + $c;
                if ($c + 1 < $n && $grid[$r][$c + 1] === $char) {
                    $v = $r * $n + $c + 1;
                    $rootU = $find($u);
                    $rootV = $find($v);
                    if ($rootU === $rootV) return true;
                    $parent[$rootU] = $rootV;
                }
                if ($r + 1 < $m && $grid[$r + 1][$c] === $char) {
                    $v = ($r + 1) * $n + $c;
                    $rootU = $find($u);
                    $rootV = $find($v);
                    if ($rootU === $rootV) return true;
                    $parent[$rootU] = $rootV;
                }
            }
        }
        return false;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func containsCycle(_ grid: [[Character]]) -> Bool {
        let m = grid.count
        if m == 0 { return false }
        let n = grid[0].count
        var parent = Array(0..<(m * n))

        func find(_ i: Int) -> Int {
            var root = i
            while parent[root] != root {
                root = parent[root]
            }
            var curr = i
            while parent[curr] != root {
                let next = parent[curr]
                parent[curr] = root
                curr = next
            }
            return root
        }

        func union(_ i: Int, _ j: Int) -> Bool {
            let rootI = find(i)
            let rootJ = find(j)
            if rootI != rootJ {
                parent[rootI] = rootJ
                return true
            }
            return false
        }

        for r in 0..<m {
            for c in 0..<n {
                let char = grid[r][c]
                let u = r * n + c
                if c + 1 < n && grid[r][c + 1] == char {
                    let v = r * n + c + 1
                    if !union(u, v) {
                        return true
                    }
                }
                if r + 1 < m && grid[r + 1][c] == char {
                    let v = (r + 1) * n + c
                    if !union(u, v) {
                        return true
                    }
                }
            }
        }
        return false
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun containsCycle(grid: Array<CharArray>): Boolean {
        val m = grid.size
        val n = grid[0].size
        val parent = IntArray(m * n) { it }

        fun find(idx: Int): Int {
            var root = idx
            while (parent[root] != root) {
                root = parent[root]
            }
            var curr = idx
            while (parent[curr] != root) {
                val next = parent[curr]
                parent[curr] = root
                curr = next
            }
            return root
        }

        for (r in 0 until m) {
            for (c in 0 until n) {
                val char = grid[r][c]
                if (c + 1 < n && grid[r][c + 1] == char) {
                    val root1 = find(r * n + c)
                    val root2 = find(r * n + c + 1)
                    if (root1 == root2) return true
                    parent[root1] = root2
                }
                if (r + 1 < m && grid[r + 1][c] == char) {
                    val root1 = find(r * n + c)
                    val root2 = find((r + 1) * n + c)
                    if (root1 == root2) return true
                    parent[root1] = root2
                }
            }
        }
        return false
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool containsCycle(List<List<String>> grid) {
    int m = grid.length;
    int n = grid[0].length;
    List<int> parent = List.generate(m * n, (i) => i);

    int find(int idx) {
      int root = idx;
      while (parent[root] != root) {
        root = parent[root];
      }
      int curr = idx;
      while (parent[curr] != root) {
        int next = parent[curr];
        parent[curr] = root;
        curr = next;
      }
      return root;
    }

    for (int r = 0; r < m; r++) {
      for (int c = 0; c < n; c++) {
        String char = grid[r][c];
        if (c + 1 < n && grid[r][c + 1] == char) {
          int root1 = find(r * n + c);
          int root2 = find(r * n + c + 1);
          if (root1 == root2) return true;
          parent[root1] = root2;
        }
        if (r + 1 < m && grid[r + 1][c] == char) {
          int root1 = find(r * n + c);
          int root2 = find((r + 1) * n + c);
          if (root1 == root2) return true;
          parent[root1] = root2;
        }
      }
    }
    return false;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func containsCycle(grid [][]byte) bool {
    m := len(grid)
    n := len(grid[0])
    parent := make([]int, m*n)
    for i := range parent {
        parent[i] = i
    }

    find := func(idx int) int {
        root := idx
        for parent[root] != root {
            root = parent[root]
        }
        curr := idx
        for parent[curr] != root {
            next := parent[curr]
            parent[curr] = root
            curr = next
        }
        return root
    }

    for r := 0; r < m; r++ {
        for c := 0; c < n; c++ {
            char := grid[r][c]
            if c+1 < n && grid[r][c+1] == char {
                root1 := find(r*n + c)
                root2 := find(r*n + c + 1)
                if root1 == root2 {
                    return true
                }
                parent[root1] = root2
            }
            if r+1 < m && grid[r+1][c] == char {
                root1 := find(r*n + c)
                root2 := find((r+1)*n + c)
                if root1 == root2 {
                    return true
                }
                parent[root1] = root2
            }
        }
    }
    return false
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def contains_cycle(grid)
  m = grid.length
  n = grid[0].length
  parent = Array.new(m * n) { |i| i }

  find = lambda do |idx|
    root = idx
    while parent[root] != root
      root = parent[root]
    end
    curr = idx
    while parent[curr] != root
      next_node = parent[curr]
      parent[curr] = root
      curr = next_node
    end
    root
  end

  (0...m).each do |r|
    (0...n).each do |c|
      char = grid[r][c]
      if c + 1 < n && grid[r][c + 1] == char
        root1 = find.call(r * n + c)
        root2 = find.call(r * n + c + 1)
        return true if root1 == root2
        parent[root1] = root2
      end
      if r + 1 < m && grid[r + 1][c] == char
        root1 = find.call(r * n + c)
        root2 = find.call((r + 1) * n + c)
        return true if root1 == root2
        parent[root1] = root2
      end
    end
  end
  false
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def containsCycle(grid: Array[Array[Char]]): Boolean = {
        val m = grid.length
        val n = grid(0).length
        val parent = Array.tabulate(m * n)(i => i)

        def find(idx: Int): Int = {
            var root = idx
            while (parent(root) != root) {
                root = parent(root)
            }
            var curr = idx
            while (parent(curr) != root) {
                val next = parent(curr)
                parent(curr) = root
                curr = next
            }
            root
        }

        for (r <- 0 until m) {
            for (c <- 0 until n) {
                val char = grid(r)(c)
                if (c + 1 < n && grid(r)(c + 1) == char) {
                    val root1 = find(r * n + c)
                    val root2 = find(r * n + c + 1)
                    if (root1 == root2) return true
                    parent(root1) = root2
                }
                if (r + 1 < m && grid(r + 1)(c) == char) {
                    val root1 = find(r * n + c)
                    val root2 = find((r + 1) * n + c)
                    if (root1 == root2) return true
                    parent(root1) = root2
                }
            }
        }
        false
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn contains_cycle(grid: Vec<Vec<char>>) -> bool {
        let m = grid.len();
        let n = grid[0].len();
        let mut parent: Vec<usize> = (0..m * n).collect();
        let mut rank: Vec<usize> = vec![0; m * n];

        for r in 0..m {
            for c in 0..n {
                let u = r * n + c;
                let char_u = grid[r][c];

                if c + 1 < n && grid[r][c + 1] == char_u {
                    let v = r * n + (c + 1);
                    if !Self::unite(&mut parent, &mut rank, u, v) {
                        return true;
                    }
                }

                if r + 1 < m && grid[r + 1][c] == char_u {
                    let v = (r + 1) * n + c;
                    if !Self::unite(&mut parent, &mut rank, u, v) {
                        return true;
                    }
                }
            }
        }
        false
    }

    fn find(parent: &mut Vec<usize>, mut i: usize) -> usize {
        let mut root = i;
        while parent[root] != root {
            root = parent[root];
        }
        while parent[i] != root {
            let next = parent[i];
            parent[i] = root;
            i = next;
        }
        root
    }

    fn unite(parent: &mut Vec<usize>, rank: &mut Vec<usize>, i: usize, j: usize) -> bool {
        let root_i = Self::find(parent, i);
        let root_j = Self::find(parent, j);
        if root_i == root_j {
            return false;
        }
        if rank[root_i] < rank[root_j] {
            parent[root_i] = root_j;
        } else if rank[root_i] > rank[root_j] {
            parent[root_j] = root_i;
        } else {
            parent[root_i] = root_j;
            rank[root_j] += 1;
        }
        true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (contains-cycle grid)
  (-> (listof (listof char?)) boolean?)
  (let* ([m (length grid)]
         [n (length (first grid))]
         [grid-vec (list->vector (map list->vector grid))]
         [parent (build-vector (* m n) (lambda (i) i))]
         [rank (make-vector (* m n) 0)])
    (letrec ([find (lambda (i)
                     (let ([val (vector-ref parent i)])
                       (if (= val i)
                           i
                           (let ([root (find val)])
                             (vector-set! parent i root)
                             root))))]
             [unite (lambda (root1 root2)
                      (let ([r1 (vector-ref rank root1)]
                            [r2 (vector-ref rank root2)])
                        (cond
                          [(< r1 r2) (vector-set! parent root1 root2)]
                          [(> r1 r2) (vector-set! parent root2 root1)]
                          [else
                           (vector-set! parent root1 root2)
                           (vector-set! rank root2 (+ r2 1))])))]
             [loop-r (lambda (r)
                       (if (= r m)
                           #f
                           (let loop-c ([c 0])
                             (if (= c n)
                                 (loop-r (+ r 1))
                                 (let* ([char (vector-ref (vector-ref grid-vec r) c)]
                                        [u (+ (* r n) c)])
                                   (let ([res-r (if (and (< (+ c 1) n)
                                                         (char=? char (vector-ref (vector-ref grid-vec r) (+ c 1))))
                                                    (let* ([v (+ (* r n) (+ c 1))]
                                                           [root-u (find u)]
                                                           [root-v (find v)])
                                                      (if (= root-u root-v)
                                                          #t
                                                          (begin (unite root-u root-v) #f)))
                                                    #f)])
                                     (if res-r
                                         #t
                                         (let ([res-b (if (and (< (+ r 1) m)
                                                               (char=? char (vector-ref (vector-ref grid-vec (+ r 1)) c)))
                                                          (let* ([v (+ (* (+ r 1) n) c)]
                                                                 [root-u (find u)]
                                                                 [root-v (find v)])
                                                            (if (= root-u root-v)
                                                                #t
                                                                (begin (unite root-u root-v) #f)))
                                                          #f)])
                                           (if res-b
                                               #t
                                               (loop-c (+ c 1))))))))))])
      (loop-r 0))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec contains_cycle(Grid :: [[char()]]) -> boolean().
contains_cycle(Grid) ->
    M = length(Grid),
    N = length(hd(Grid)),
    GridTuple = list_to_tuple([list_to_tuple(Row) || Row <- Grid]),
    Parent = array:from_list(lists:seq(0, M * N - 1)),
    Rank = array:new(M * N, {default, 0}),
    check_cells(0, 0, M, N, GridTuple, Parent, Rank).

find(I, Parent) ->
    Val = array:get(I, Parent),
    if Val == I -> {I, Parent};
       true ->
           {Root, P1} = find(Val, Parent),
           P2 = array:set(I, Root, P1),
           {Root, P2}
    end.

union_uf(Root1, Root2, Parent, Rank) ->
    Rank1 = array:get(Root1, Rank),
    Rank2 = array:get(Root2, Rank),
    if Rank1 < Rank2 -> {array:set(Root1, Root2, Parent), Rank};
       Rank1 > Rank2 -> {array:set(Root2, Root1, Parent), Rank};
       true ->
           P1 = array:set(Root1, Root2, Parent),
           R1 = array:set(Root2, Rank2 + 1, Rank),
           {P1, R1}
    end.

check_cells(R, _C, M, _N, _GridTuple, _Parent, _Rank) when R == M -> false;
check_cells(R, C, M, N, GridTuple, Parent, Rank) when C == N -> 
    check_cells(R + 1, 0, M, N, GridTuple, Parent, Rank);
check_cells(R, C, M, N, GridTuple, Parent, Rank) ->
    Char = element(C + 1, element(R + 1, GridTuple)),
    {CycleR, P1, R1} = 
        if C + 1 < N ->
            case element(C + 2, element(R + 1, GridTuple)) of
                Char ->
                    U = R * N + C,
                    V = R * N + C + 1,
                    {RootU, PA} = find(U, Parent),
                    {RootV, PB} = find(V, PA),
                    if RootU == RootV -> {true, PB, Rank};
                       true -> {NewP, NewR} = union_uf(RootU, RootV, PB, Rank), {false, NewP, NewR}
                    end;
                _ -> {false, Parent, Rank}
            end;
           true -> {false, Parent, Rank}
        end,
    if CycleR -> true;
       true ->
           {CycleB, P2, R2} = 
               if R + 1 < M ->
                   case element(C + 1, element(R + 2, GridTuple)) of
                       Char ->
                           U = R * N + C,
                           V = (R + 1) * N + C,
                           {RootU, PA2} = find(U, P1),
                           {RootV, PB2} = find(V, PA2),
                           if RootU == RootV -> {true, PB2, R1};
                              true -> {NewP2, NewR2} = union_uf(RootU, RootV, PB2, R1), {false, NewP2, NewR2}
                           end;
                       _ -> {false, P1, R1}
                   end;
                  true -> {false, P1, R1}
               end,
           if CycleB -> true;
              true -> check_cells(R, C + 1, M, N, GridTuple, P2, R2)
           end
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec contains_cycle(grid :: [[char]]) :: boolean
  def contains_cycle(grid) do
    m = length(grid)
    n = length(hd(grid))
    grid_tuple = grid |> Enum.map(&List.to_tuple/1) |> List.to_tuple()

    Enum.reduce_while(0..m-1, {%{}, %{}}, fn r, {parent, rank} ->
      case Enum.reduce_while(0..n-1, {parent, rank}, fn c, {p, rk} ->
        char = elem(elem(grid_tuple, r), c)

        {cycle_r, p1, rk1} = if c + 1 < n and elem(elem(grid_tuple, r), c + 1) == char do
          u = r * n + c
          v = r * n + c + 1
          {root_u, p_u} = find(u, p)
          {root_v, p_v} = find(v, p_u)
          if root_u == root_v, do: {true, p_v, rk}, else: (
            {p_union, rk_union} = union_uf(root_u, root_v, p_v, rk)
            {false, p_union, rk_union}
          )
        else
          {false, p, rk}
        end

        if cycle_r do
          {:halt, :cycle}
        else
          {cycle_b, p2, rk2} = if r + 1 < m and elem(elem(grid_tuple, r + 1), c) == char do
            u = r * n + c
            v = (r + 1) * n + c
            {root_u, p_u_b} = find(u, p1)
            {root_v, p_v_b} = find(v, p_u_b)
            if root_u == root_v, do: {true, p_v_b, rk1}, else: (
              {p_union_b, rk_union_b} = union_uf(root_u, root_v, p_v_b, rk1)
              {false, p_union_b, rk_union_b}
            )
          else
            {false, p1, rk1}
          end

          if cycle_b, do: {:halt, :cycle}, else: {:cont, {p2, rk2}}
        end
      end) do
        :cycle -> {:halt, true}
        {p_next, rk_next} -> {:cont, {p_next, rk_next}}
      end
    end) == true
  end

  defp find(i, parent) do
    val = Map.get(parent, i, i)
    if val == i do
      {i, parent}
    else
      {root, p_new} = find(val, parent)
      {root, Map.put(p_new, i, root)}
    end
  end

  defp union_uf(root1, root2, parent, rank) do
    r1 = Map.get(rank, root1, 0)
    r2 = Map.get(rank, root2, 0)
    cond do
      r1 < r2 -> {Map.put(parent, root1, root2), rank}
      r1 > r2 -> {Map.put(parent, root2, root1), rank}
      true ->
        p1 = Map.put(parent, root1, root2)
        rk1 = Map.put(rank, root2, r2 + 1)
        {p1, rk1}
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(M * N * alpha(M * N)), where M and N are the grid dimensions and alpha is the inverse Ackermann function. This complexity arises because we iterate through each of the M * N cells once and perform a constant number of DSU operations per cell, which take nearly constant time.
- **Space Complexity:** O(M * N) to store the parent and rank arrays for the Disjoint Set Union data structure, where each array has a size equal to the total number of cells in the grid.
