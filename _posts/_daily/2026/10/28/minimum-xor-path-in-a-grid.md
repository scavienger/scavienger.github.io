---
layout: post
title: "Minimum XOR Path in a Grid"
date: 2026-10-28 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Dynamic Programming", "Bit Manipulation", "Matrix"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-xor-path-in-a-grid/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minCost(vector<vector<int>>& grid) {\n\
        \        int m = grid.size();\n        int n = grid[0].size();\n        vector<vector<char>>\
        \ dp(n, vector<char>(1024, 0));\n\n        for (int r = 0; r < m; ++r) {\n \
        \           for (int c = 0; c < n; ++c) {\n                vector<char> next_set(1024,\
        \ 0);\n                int val = grid[r][c];\n                if (r == 0 &&\
        \ c == 0) {\n                    next_set[val] = 1;\n                } else\
        \ {\n                    if (r > 0) {\n                        for (int k =\
        \ 0; k < 1024; ++k) {\n                            if (dp[c][k]) next_set[k\
        \ ^ val] = 1;\n                        }\n                    }\n          \
        \          if (c > 0) {\n                        for (int k = 0; k < 1024; ++k)\
        \ {\n                            if (dp[c - 1][k]) next_set[k ^ val] = 1;\n\
        \                        }\n                    }\n                }\n     \
        \           dp[c] = std::move(next_set);\n            }\n        }\n\n     \
        \   for (int k = 0; k < 1024; ++k) {\n            if (dp[n - 1][k]) return k;\n\
        \        }\n        return -1;\n    }\n};"
      java: "class Solution {\n    public int minCost(int[][] grid) {\n        int m\
        \ = grid.length;\n        int n = grid[0].length;\n        boolean[][] dp =\
        \ new boolean[n][1024];\n\n        for (int r = 0; r < m; r++) {\n         \
        \   for (int c = 0; c < n; c++) {\n                boolean[] nextSet = new boolean[1024];\n\
        \                int val = grid[r][c];\n                if (r == 0 && c == 0)\
        \ {\n                    nextSet[val] = true;\n                } else {\n  \
        \                  if (r > 0) {\n                        for (int k = 0; k <\
        \ 1024; k++) {\n                            if (dp[c][k]) nextSet[k ^ val] =\
        \ true;\n                        }\n                    }\n                \
        \    if (c > 0) {\n                        for (int k = 0; k < 1024; k++) {\n\
        \                            if (dp[c - 1][k]) nextSet[k ^ val] = true;\n  \
        \                      }\n                    }\n                }\n       \
        \         dp[c] = nextSet;\n            }\n        }\n\n        for (int k =\
        \ 0; k < 1024; k++) {\n            if (dp[n - 1][k]) return k;\n        }\n\
        \        return -1;\n    }\n}"
      python: "class Solution(object):\n    def minCost(self, grid):\n        \"\"\"\
        \n        :type grid: List[List[int]]\n        :rtype: int\n        \"\"\"\n\
        \        m = len(grid)\n        n = len(grid[0])\n        dp = [set() for _\
        \ in range(n)]\n\n        for r in range(m):\n            for c in range(n):\n\
        \                val = grid[r][c]\n                new_set = set()\n       \
        \         if r == 0 and c == 0:\n                    new_set.add(val)\n    \
        \            else:\n                    if r > 0:\n                        for\
        \ prev_xor in dp[c]:\n                            new_set.add(prev_xor ^ val)\n\
        \                    if c > 0:\n                        for prev_xor in dp[c-1]:\n\
        \                            new_set.add(prev_xor ^ val)\n                dp[c]\
        \ = new_set\n\n        return min(dp[n-1])"
      python3: "class Solution:\n    def minCost(self, grid: list[list[int]]) -> int:\n\
        \        m = len(grid)\n        n = len(grid[0])\n        dp = [set() for _\
        \ in range(n)]\n\n        for r in range(m):\n            for c in range(n):\n\
        \                val = grid[r][c]\n                new_set = set()\n       \
        \         if r == 0 and c == 0:\n                    new_set.add(val)\n    \
        \            else:\n                    if r > 0:\n                        for\
        \ prev_xor in dp[c]:\n                            new_set.add(prev_xor ^ val)\n\
        \                    if c > 0:\n                        for prev_xor in dp[c-1]:\n\
        \                            new_set.add(prev_xor ^ val)\n                dp[c]\
        \ = new_set\n\n        return min(dp[n-1])"
      c: "#include <stdlib.h>\n#include <string.h>\n\nint minCost(int** grid, int gridSize,\
        \ int* gridColSize) {\n    int m = gridSize;\n    int n = gridColSize[0];\n\
        \    unsigned char* dp = (unsigned char*)calloc(n * 1024, sizeof(unsigned char));\n\
        \n    for (int r = 0; r < m; r++) {\n        for (int c = 0; c < n; c++) {\n\
        \            unsigned char next_set[1024] = {0};\n            int val = grid[r][c];\n\
        \            if (r == 0 && c == 0) {\n                next_set[val] = 1;\n \
        \           } else {\n                if (r > 0) {\n                    for\
        \ (int k = 0; k < 1024; k++) {\n                        if (dp[c * 1024 + k])\
        \ next_set[k ^ val] = 1;\n                    }\n                }\n       \
        \         if (c > 0) {\n                    for (int k = 0; k < 1024; k++) {\n\
        \                        if (dp[(c - 1) * 1024 + k]) next_set[k ^ val] = 1;\n\
        \                    }\n                }\n            }\n            memcpy(&dp[c\
        \ * 1024], next_set, 1024);\n        }\n    }\n\n    int min_xor = 1023;\n \
        \   for (int k = 0; k < 1024; k++) {\n        if (dp[(n - 1) * 1024 + k]) {\n\
        \            min_xor = k;\n            break;\n        }\n    }\n\n    free(dp);\n\
        \    return min_xor;\n}"
      csharp: "public class Solution {\n    public int MinCost(int[][] grid) {\n   \
        \     int m = grid.Length;\n        int n = grid[0].Length;\n        int numCells\
        \ = m * n;\n        bool[] dp = new bool[numCells * 1024];\n\n        dp[grid[0][0]]\
        \ = true;\n\n        for (int i = 0; i < m; i++) {\n            for (int j =\
        \ 0; j < n; j++) {\n                if (i == 0 && j == 0) continue;\n      \
        \          int val = grid[i][j];\n                int currIdx = (i * n + j)\
        \ * 1024;\n\n                if (i > 0 && j > 0) {\n                    int\
        \ pR = (i - 1) * n * 1024;\n                    int pC = (i * n + (j - 1)) *\
        \ 1024;\n                    for (int x = 0; x < 1024; x++) {\n            \
        \            if (dp[pR + x] || dp[pC + x]) {\n                            dp[currIdx\
        \ + (x ^ val)] = true;\n                        }\n                    }\n \
        \               } else if (i > 0) {\n                    int pR = (i - 1) *\
        \ n * 1024;\n                    for (int x = 0; x < 1024; x++) {\n        \
        \                if (dp[pR + x]) {\n                            dp[currIdx +\
        \ (x ^ val)] = true;\n                        }\n                    }\n   \
        \             } else if (j > 0) {\n                    int pC = (i * n + (j\
        \ - 1)) * 1024;\n                    for (int x = 0; x < 1024; x++) {\n    \
        \                    if (dp[pC + x]) {\n                            dp[currIdx\
        \ + (x ^ val)] = true;\n                        }\n                    }\n \
        \               }\n            }\n        }\n\n        int lastCellIdx = (numCells\
        \ - 1) * 1024;\n        for (int x = 0; x < 1024; x++) {\n            if (dp[lastCellIdx\
        \ + x]) return x;\n        }\n\n        return -1;\n    }\n}"
      javascript: "/**\n * @param {number[][]} grid\n * @return {number}\n */\nvar minCost\
        \ = function(grid) {\n    const m = grid.length;\n    const n = grid[0].length;\n\
        \    const numCells = m * n;\n    const dp = new Uint8Array(numCells * 1024);\n\
        \n    dp[grid[0][0]] = 1;\n\n    for (let i = 0; i < m; i++) {\n        for\
        \ (let j = 0; j < n; j++) {\n            if (i === 0 && j === 0) continue;\n\
        \            const val = grid[i][j];\n            const currIdx = (i * n + j)\
        \ * 1024;\n\n            if (i > 0 && j > 0) {\n                const pR = (i\
        \ - 1) * n * 1024;\n                const pC = (i * n + j - 1) * 1024;\n   \
        \             for (let x = 0; x < 1024; x++) {\n                    if (dp[pR\
        \ + x] || dp[pC + x]) {\n                        dp[currIdx + (x ^ val)] = 1;\n\
        \                    }\n                }\n            } else if (i > 0) {\n\
        \                const pR = (i - 1) * n * 1024;\n                for (let x\
        \ = 0; x < 1024; x++) {\n                    if (dp[pR + x]) {\n           \
        \             dp[currIdx + (x ^ val)] = 1;\n                    }\n        \
        \        }\n            } else if (j > 0) {\n                const pC = (i *\
        \ n + j - 1) * 1024;\n                for (let x = 0; x < 1024; x++) {\n   \
        \                 if (dp[pC + x]) {\n                        dp[currIdx + (x\
        \ ^ val)] = 1;\n                    }\n                }\n            }\n  \
        \      }\n    }\n\n    const lastCellIdx = (numCells - 1) * 1024;\n    for (let\
        \ x = 0; x < 1024; x++) {\n        if (dp[lastCellIdx + x]) return x;\n    }\n\
        \n    return -1;\n};"
      typescript: "function minCost(grid: number[][]): number {\n    const m = grid.length;\n\
        \    const n = grid[0].length;\n    const numCells = m * n;\n    const dp =\
        \ new Uint8Array(numCells * 1024);\n\n    dp[grid[0][0]] = 1;\n\n    for (let\
        \ i = 0; i < m; i++) {\n        for (let j = 0; j < n; j++) {\n            if\
        \ (i === 0 && j === 0) continue;\n            const val = grid[i][j];\n    \
        \        const currIdx = (i * n + j) * 1024;\n\n            if (i > 0 && j >\
        \ 0) {\n                const pR = (i - 1) * n * 1024;\n                const\
        \ pC = (i * n + j - 1) * 1024;\n                for (let x = 0; x < 1024; x++)\
        \ {\n                    if (dp[pR + x] || dp[pC + x]) {\n                 \
        \       dp[currIdx + (x ^ val)] = 1;\n                    }\n              \
        \  }\n            } else if (i > 0) {\n                const pR = (i - 1) *\
        \ n * 1024;\n                for (let x = 0; x < 1024; x++) {\n            \
        \        if (dp[pR + x]) {\n                        dp[currIdx + (x ^ val)]\
        \ = 1;\n                    }\n                }\n            } else if (j >\
        \ 0) {\n                const pC = (i * n + j - 1) * 1024;\n               \
        \ for (let x = 0; x < 1024; x++) {\n                    if (dp[pC + x]) {\n\
        \                        dp[currIdx + (x ^ val)] = 1;\n                    }\n\
        \                }\n            }\n        }\n    }\n\n    const lastCellIdx\
        \ = (numCells - 1) * 1024;\n    for (let x = 0; x < 1024; x++) {\n        if\
        \ (dp[lastCellIdx + x]) return x;\n    }\n\n    return -1;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $grid\n     * @return\
        \ Integer\n     */\n    function minCost($grid) {\n        $m = count($grid);\n\
        \        $n = count($grid[0]);\n        $numCells = $m * $n;\n        $dp =\
        \ array_fill(0, $numCells * 1024, false);\n\n        $dp[$grid[0][0]] = true;\n\
        \n        for ($i = 0; $i < $m; $i++) {\n            for ($j = 0; $j < $n; $j++)\
        \ {\n                if ($i === 0 && $j === 0) continue;\n                $val\
        \ = $grid[$i][$j];\n                $currIdx = ($i * $n + $j) * 1024;\n\n  \
        \              if ($i > 0 && $j > 0) {\n                    $pR = ($i - 1) *\
        \ $n * 1024;\n                    $pC = ($i * $n + $j - 1) * 1024;\n       \
        \             for ($x = 0; $x < 1024; $x++) {\n                        if ($dp[$pR\
        \ + $x] || $dp[$pC + $x]) {\n                            $dp[$currIdx + ($x\
        \ ^ $val)] = true;\n                        }\n                    }\n     \
        \           } else if ($i > 0) {\n                    $pR = ($i - 1) * $n *\
        \ 1024;\n                    for ($x = 0; $x < 1024; $x++) {\n             \
        \           if ($dp[$pR + $x]) {\n                            $dp[$currIdx +\
        \ ($x ^ $val)] = true;\n                        }\n                    }\n \
        \               } else if ($j > 0) {\n                    $pC = ($i * $n + $j\
        \ - 1) * 1024;\n                    for ($x = 0; $x < 1024; $x++) {\n      \
        \                  if ($dp[$pC + $x]) {\n                            $dp[$currIdx\
        \ + ($x ^ $val)] = true;\n                        }\n                    }\n\
        \                }\n            }\n        }\n\n        $lastCellIdx = ($numCells\
        \ - 1) * 1024;\n        for ($x = 0; $x < 1024; $x++) {\n            if ($dp[$lastCellIdx\
        \ + $x]) return $x;\n        }\n\n        return -1;\n    }\n}"
      swift: "class Solution {\n    func minCost(_ grid: [[Int]]) -> Int {\n       \
        \ let m = grid.count\n        let n = grid[0].count\n        let numCells =\
        \ m * n\n        var dp = [Bool](repeating: false, count: numCells * 1024)\n\
        \n        dp[grid[0][0]] = true\n\n        for i in 0..<m {\n            for\
        \ j in 0..<n {\n                if i == 0 && j == 0 { continue }\n         \
        \       let val = grid[i][j]\n                let currIdx = (i * n + j) * 1024\n\
        \n                if i > 0 && j > 0 {\n                    let pR = (i - 1)\
        \ * n * 1024\n                    let pC = (i * n + j - 1) * 1024\n        \
        \            for x in 0..<1024 {\n                        if dp[pR + x] || dp[pC\
        \ + x] {\n                            dp[currIdx + (x ^ val)] = true\n     \
        \                   }\n                    }\n                } else if i >\
        \ 0 {\n                    let pR = (i - 1) * n * 1024\n                   \
        \ for x in 0..<1024 {\n                        if dp[pR + x] {\n           \
        \                 dp[currIdx + (x ^ val)] = true\n                        }\n\
        \                    }\n                } else if j > 0 {\n                \
        \    let pC = (i * n + j - 1) * 1024\n                    for x in 0..<1024\
        \ {\n                        if dp[pC + x] {\n                            dp[currIdx\
        \ + (x ^ val)] = true\n                        }\n                    }\n  \
        \              }\n            }\n        }\n\n        let lastCellIdx = (numCells\
        \ - 1) * 1024\n        for x in 0..<1024 {\n            if dp[lastCellIdx +\
        \ x] {\n                return x\n            }\n        }\n\n        return\
        \ -1\n    }\n}"
      kotlin: "import java.util.BitSet\n\nclass Solution {\n    fun minCost(grid: Array<IntArray>):\
        \ Int {\n        val m = grid.size\n        val n = grid[0].size\n        val\
        \ dp = Array(m) { Array(n) { BitSet(1024) } }\n\n        dp[0][0].set(grid[0][0])\n\
        \n        for (i in 0 until m) {\n            for (j in 0 until n) {\n     \
        \           if (i == 0 && j == 0) continue\n\n                val v = grid[i][j]\n\
        \                val current = dp[i][j]\n\n                if (i > 0) {\n  \
        \                  val prev = dp[i - 1][j]\n                    var k = prev.nextSetBit(0)\n\
        \                    while (k != -1) {\n                        current.set(k\
        \ xor v)\n                        k = prev.nextSetBit(k + 1)\n             \
        \       }\n                }\n\n                if (j > 0) {\n             \
        \       val prev = dp[i][j - 1]\n                    var k = prev.nextSetBit(0)\n\
        \                    while (k != -1) {\n                        current.set(k\
        \ xor v)\n                        k = prev.nextSetBit(k + 1)\n             \
        \       }\n                }\n            }\n        }\n\n        return dp[m\
        \ - 1][n - 1].nextSetBit(0)\n    }\n}"
      dart: "class Solution {\n  int minCost(List<List<int>> grid) {\n    int m = grid.length;\n\
        \    int n = grid[0].length;\n    List<List<Set<int>>> dp = List.generate(m,\
        \ (_) => List.generate(n, (_) => <int>{}));\n\n    dp[0][0].add(grid[0][0]);\n\
        \n    for (int i = 0; i < m; i++) {\n      for (int j = 0; j < n; j++) {\n \
        \       if (i == 0 && j == 0) continue;\n\n        int v = grid[i][j];\n   \
        \     Set<int> current = dp[i][j];\n\n        if (i > 0) {\n          for (int\
        \ k in dp[i - 1][j]) {\n            current.add(k ^ v);\n          }\n     \
        \   }\n\n        if (j > 0) {\n          for (int k in dp[i][j - 1]) {\n   \
        \         current.add(k ^ v);\n          }\n        }\n      }\n    }\n\n  \
        \  int minXor = 1024;\n    for (int k in dp[m - 1][n - 1]) {\n      if (k <\
        \ minXor) minXor = k;\n    }\n    return minXor;\n  }\n}"
      go: "func minCost(grid [][]int) int {\n    m := len(grid)\n    n := len(grid[0])\n\
        \n    dp := make([][]map[int]struct{}, m)\n    for i := range dp {\n       \
        \ dp[i] = make([]map[int]struct{}, n)\n        for j := range dp[i] {\n    \
        \        dp[i][j] = make(map[int]struct{})\n        }\n    }\n\n    dp[0][0][grid[0][0]]\
        \ = struct{}{}\n\n    for i := 0; i < m; i++ {\n        for j := 0; j < n; j++\
        \ {\n            if i == 0 && j == 0 {\n                continue\n         \
        \   }\n\n            v := grid[i][j]\n            current := dp[i][j]\n\n  \
        \          if i > 0 {\n                for k := range dp[i-1][j] {\n       \
        \             current[k^v] = struct{}{}\n                }\n            }\n\n\
        \            if j > 0 {\n                for k := range dp[i][j-1] {\n     \
        \               current[k^v] = struct{}{}\n                }\n            }\n\
        \        }\n    }\n\n    minXor := 1024\n    for k := range dp[m-1][n-1] {\n\
        \        if k < minXor {\n            minXor = k\n        }\n    }\n    return\
        \ minXor\n}"
      ruby: "require 'set'\n\n# @param {Integer[][]} grid\n# @return {Integer}\ndef\
        \ min_cost(grid)\n  m = grid.length\n  n = grid[0].length\n\n  dp = Array.new(m)\
        \ { Array.new(n) { Set.new } }\n  dp[0][0].add(grid[0][0])\n\n  m.times do |i|\n\
        \    n.times do |j|\n      next if i == 0 && j == 0\n\n      v = grid[i][j]\n\
        \      current = dp[i][j]\n\n      if i > 0\n        dp[i-1][j].each { |k| current.add(k\
        \ ^ v) }\n      end\n\n      if j > 0\n        dp[i][j-1].each { |k| current.add(k\
        \ ^ v) }\n      end\n    end\n  end\n\n  dp[m-1][n-1].min\nend"
      scala: "import java.util.BitSet\n\nobject Solution {\n    def minCost(grid: Array[Array[Int]]):\
        \ Int = {\n        val m = grid.length\n        val n = grid(0).length\n   \
        \     val dp = Array.tabulate(m, n)((_, _) => new BitSet(1024))\n\n        dp(0)(0).set(grid(0)(0))\n\
        \n        for (i <- 0 until m) {\n            for (j <- 0 until n) {\n     \
        \           if (i > 0 || j > 0) {\n                    val v = grid(i)(j)\n\
        \                    val current = dp(i)(j)\n\n                    if (i > 0)\
        \ {\n                        val prev = dp(i - 1)(j)\n                     \
        \   var k = prev.nextSetBit(0)\n                        while (k >= 0 && k <\
        \ 1024) {\n                            current.set(k ^ v)\n                \
        \            k = prev.nextSetBit(k + 1)\n                        }\n       \
        \             }\n\n                    if (j > 0) {\n                      \
        \  val prev = dp(i)(j - 1)\n                        var k = prev.nextSetBit(0)\n\
        \                        while (k >= 0 && k < 1024) {\n                    \
        \        current.set(k ^ v)\n                            k = prev.nextSetBit(k\
        \ + 1)\n                        }\n                    }\n                }\n\
        \            }\n        }\n\n        dp(m - 1)(n - 1).nextSetBit(0)\n    }\n\
        }"
      rust: "impl Solution {\n    pub fn min_cost(grid: Vec<Vec<i32>>) -> i32 {\n  \
        \      let m = grid.len();\n        let n = grid[0].len();\n        let mut\
        \ dp = vec![[false; 1024]; n];\n\n        for i in 0..m {\n            let mut\
        \ next_dp = vec![[false; 1024]; n];\n            for j in 0..n {\n         \
        \       let val = grid[i][j] as usize;\n                if i == 0 && j == 0\
        \ {\n                    next_dp[j][val] = true;\n                } else if\
        \ i == 0 {\n                    for k in 0..1024 {\n                       \
        \ if next_dp[j - 1][k] {\n                            next_dp[j][k ^ val] =\
        \ true;\n                        }\n                    }\n                }\
        \ else if j == 0 {\n                    for k in 0..1024 {\n               \
        \         if dp[j][k] {\n                            next_dp[j][k ^ val] = true;\n\
        \                        }\n                    }\n                } else {\n\
        \                    for k in 0..1024 {\n                        if dp[j][k]\
        \ || next_dp[j - 1][k] {\n                            next_dp[j][k ^ val] =\
        \ true;\n                        }\n                    }\n                }\n\
        \            }\n            dp = next_dp;\n        }\n\n        for k in 0..1024\
        \ {\n            if dp[n - 1][k] {\n                return k as i32;\n     \
        \       }\n        }\n        0\n    }\n}"
      racket: "(define/contract (min-cost grid)\n  (-> (listof (listof exact-integer?))\
        \ exact-integer?)\n  (letrec ([xor-mask (lambda (mask val)\n               \
        \        (let ([new-mask 0])\n                         (for ([k (in-range 1024)])\n\
        \                           (when (bitwise-bit-set? mask k)\n              \
        \               (set! new-mask (bitwise-ior new-mask (arithmetic-shift 1 (bitwise-xor\
        \ k val))))))\n                         new-mask))])\n    (let* ([m (length\
        \ grid)]\n           [n (length (car grid))]\n           [dp (make-vector n\
        \ 0)])\n      (for ([row grid] [i (in-naturals)])\n        (for ([val row] [j\
        \ (in-naturals)])\n          (let ([current-mask 0])\n            (cond\n  \
        \            [(and (= i 0) (= j 0))\n               (set! current-mask (arithmetic-shift\
        \ 1 val))]\n              [(= i 0)\n               (set! current-mask (xor-mask\
        \ (vector-ref dp (- j 1)) val))]\n              [(= j 0)\n               (set!\
        \ current-mask (xor-mask (vector-ref dp j) val))]\n              [else\n   \
        \            (set! current-mask (xor-mask (bitwise-ior (vector-ref dp j) (vector-ref\
        \ dp (- j 1))) val))])\n            (vector-set! dp j current-mask))))\n   \
        \   (let ([final-mask (vector-ref dp (- n 1))])\n        (let loop ([k 0])\n\
        \          (if (bitwise-bit-set? final-mask k)\n              k\n          \
        \    (loop (+ k 1))))))))"
      erlang: "-spec min_cost(Grid :: [[integer()]]) -> integer().\nmin_cost([FirstRow\
        \ | RestRows]) ->\n    FirstDP = build_first_row(FirstRow),\n    FinalDP = lists:foldl(fun(Row,\
        \ PrevDP) ->\n        process_row(Row, PrevDP)\n    end, FirstDP, RestRows),\n\
        \    find_min(lists:last(FinalDP), 0).\n\nbuild_first_row([Head | Tail]) ->\n\
        \    FirstMask = 1 bsl Head,\n    {_, RowDP_rev} = lists:foldl(fun(Val, {PrevMask,\
        \ Acc}) ->\n        NewMask = xor_mask(PrevMask, Val),\n        {NewMask, [NewMask\
        \ | Acc]}\n    end, {FirstMask, [FirstMask]}, Tail),\n    lists:reverse(RowDP_rev).\n\
        \nprocess_row(Row, PrevRowDP) ->\n    {_, NewRowDP_rev} = lists:foldl(fun({Val,\
        \ PrevRowMask}, {PrevColMask, Acc}) ->\n        CombinedMask = PrevRowMask bor\
        \ PrevColMask,\n        NewMask = xor_mask(CombinedMask, Val),\n        {NewMask,\
        \ [NewMask | Acc]}\n    end, {0, []}, lists:zip(Row, PrevRowDP)),\n    lists:reverse(NewRowDP_rev).\n\
        \nxor_mask(Mask, Val) ->\n    xor_mask_rec(Mask, Val, 0, 0).\n\nxor_mask_rec(0,\
        \ _Val, _K, Acc) -> Acc;\nxor_mask_rec(Mask, Val, K, Acc) ->\n    NewAcc = if\
        \ (Mask band 1) /= 0 -> Acc bor (1 bsl (K bxor Val));\n                true\
        \ -> Acc\n             end,\n    xor_mask_rec(Mask bsr 1, Val, K + 1, NewAcc).\n\
        \nfind_min(Mask, K) ->\n    case (Mask band (1 bsl K)) of\n        0 -> find_min(Mask,\
        \ K + 1);\n        _ -> K\n    end."
      elixir: "defmodule Solution do\n  import Bitwise\n\n  @spec min_cost(grid :: [[integer]])\
        \ :: integer\n  def min_cost([first_row | rest_rows]) do\n    first_dp = build_first_row(first_row)\n\
        \    final_dp = Enum.reduce(rest_rows, first_dp, fn row, prev_dp ->\n      process_row(row,\
        \ prev_dp)\n    end)\n    find_min(List.last(final_dp), 0)\n  end\n\n  defp\
        \ build_first_row([head | tail]) do\n    first_mask = 1 <<< head\n    {_, row_dp_rev}\
        \ = Enum.reduce(tail, {first_mask, [first_mask]}, fn val, {prev_mask, acc} ->\n\
        \      new_mask = xor_mask(prev_mask, val)\n      {new_mask, [new_mask | acc]}\n\
        \    end)\n    Enum.reverse(row_dp_rev)\n  end\n\n  defp process_row(row, prev_row_dp)\
        \ do\n    {_, new_row_dp_rev} = Enum.zip(row, prev_row_dp)\n    |> Enum.reduce({0,\
        \ []}, fn {val, prev_row_mask}, {prev_col_mask, acc} ->\n      combined_mask\
        \ = prev_row_mask ||| prev_col_mask\n      new_mask = xor_mask(combined_mask,\
        \ val)\n      {new_mask, [new_mask | acc]}\n    end)\n    Enum.reverse(new_row_dp_rev)\n\
        \  end\n\n  defp xor_mask(mask, val) do\n    xor_mask_rec(mask, val, 0, 0)\n\
        \  end\n\n  defp xor_mask_rec(0, _val, _k, acc), do: acc\n  defp xor_mask_rec(mask,\
        \ val, k, acc) do\n    new_acc = if (mask &&& 1) != 0, do: acc ||| (1 <<< bxor(k,\
        \ val)), else: acc\n    xor_mask_rec(mask >>> 1, val, k + 1, new_acc)\n  end\n\
        \n  defp find_min(mask, k) do\n    if (mask &&& (1 <<< k)) != 0 do\n      k\n\
        \    else\n      find_min(mask, k + 1)\n    end\n  end\nend"
    approach: 'To solve this problem efficiently, we use dynamic programming to keep
      track of all possible XOR values reachable at each cell in the grid. Given the
      constraints that the grid values are between 0 and 1023, the bitwise XOR sum of
      any path will also be within the range [0, 1023]. We define a DP state where $dp[i][j][x]$
      is a boolean indicating whether it is possible to reach cell $(i, j)$ with a path
      XOR sum equal to $x$. Since we can only move right or down, the possible XOR sums
      at cell $(i, j)$ are derived from the possible XOR sums at cell $(i-1, j)$ and
      cell $(i, j-1)$, each XORed with the current cell''s value $grid[i][j]$.


      To optimize space, we observe that the reachable XOR sums for the current row
      only depend on the results of the previous row and the cell immediately to the
      left. We can maintain a 2D DP table $dp[n][1024]$, where $dp[c]$ stores the set
      of reachable XOR values for column $c$. During the iteration over each row, we
      update the columns such that $dp[c]$ is computed using the previous row''s $dp[c]$
      (from above) and the current row''s $dp[c-1]$ (from the left). Finally, the minimum
      XOR value reachable at the bottom-right cell $(m-1, n-1)$ is the smallest index
      $k$ such that $dp[n-1][k]$ is true.'
    time_complexity: O(M * N * K) where M and N are the grid dimensions (with M * N
      ≤ 1000) and K is the maximum possible XOR value (1024). We iterate over each of
      the M * N cells exactly once and, for each cell, we potentially iterate through
      all K possible XOR values to update the reachability state.
    space_complexity: O(N * K) where N is the number of columns and K is 1024. By using
      a row-by-row DP update, we only need to store the possible XOR values for each
      column of the current and previous rows.
    elapsed_time: 239.04843544960022
    model: gemini-3-flash-preview
    generated_at: '2026-10-28 03:25:09 '
---

## Problem #3882: Minimum XOR Path in a Grid

**Difficulty:** Medium

**Topics:** Array, Dynamic Programming, Bit Manipulation, Matrix

## Problem Description

<p>You are given a 2D integer array <code>grid</code> of size <code>m * n</code>.</p>

<p>You start at the <strong>top-left</strong> cell <code>(0, 0)</code> and want to reach the <strong>bottom-right</strong> cell <code>(m - 1, n - 1)</code>.</p>

<p>At each step, you <strong>may</strong> move either <strong>right or down</strong>.</p>

<p>The <strong>cost</strong> of a path is defined as the <strong>bitwise XOR</strong> of all the values in the cells along that path, <strong>including</strong> the start and end cells.</p>

<p>Return the <strong>minimum</strong> possible XOR value among all valid paths from <code>(0, 0)</code> to <code>(m - 1, n - 1)</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,2],[3,4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<p>There are two valid paths:</p>

<ul>
	<li><code>(0, 0) &rarr; (0, 1) &rarr; (1, 1)</code> with XOR: <code>1 XOR 2 XOR 4 = 7</code></li>
	<li><code>(0, 0) &rarr; (1, 0) &rarr; (1, 1)</code> with XOR: <code>1 XOR 3 XOR 4 = 6</code></li>
</ul>

<p>The minimum XOR value among all valid paths is 6.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[6,7],[5,8]]</span></p>

<p><strong>Output:</strong> <span class="example-io">9</span></p>

<p><strong>Explanation:</strong></p>

<p>There are two valid paths:</p>

<ul>
	<li><code>(0, 0) &rarr; (0, 1) &rarr; (1, 1)</code> with XOR: <code>6 XOR 7 XOR 8 = 9</code></li>
	<li><code>(0, 0) &rarr; (1, 0) &rarr; (1, 1)</code> with XOR: <code>6 XOR 5 XOR 8 = 11</code></li>
</ul>

<p>The minimum XOR value among all valid paths is 9.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[2,7,5]]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>There is only one valid path:</p>

<ul>
	<li><code>(0, 0) &rarr; (0, 1) &rarr; (0, 2)</code> with XOR: <code>2 XOR 7 XOR 5 = 0</code></li>
</ul>

<p>The XOR value of this path is 0, which is the minimum possible.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m == grid.length &lt;= 1000</code></li>
	<li><code>1 &lt;= n == grid[i].length &lt;= 1000</code></li>
	<li><code>m * n &lt;= 1000</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 1023​</code></li>
</ul>


## Hints

1. Use dynamic programming with state `dp[i][j][x]`, where `x` is a possible XOR value.

2. `dp[i][j][x]` indicates whether it is possible to reach cell `(i, j)` with XOR equal to `x`.

3. Transition from the top left cell by updating `x ^ grid[i][j]`, and track all reachable XOR values to find the minimum at the end cell.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To solve this problem efficiently, we use dynamic programming to keep track of all possible XOR values reachable at each cell in the grid. Given the constraints that the grid values are between 0 and 1023, the bitwise XOR sum of any path will also be within the range [0, 1023]. We define a DP state where $dp[i][j][x]$ is a boolean indicating whether it is possible to reach cell $(i, j)$ with a path XOR sum equal to $x$. Since we can only move right or down, the possible XOR sums at cell $(i, j)$ are derived from the possible XOR sums at cell $(i-1, j)$ and cell $(i, j-1)$, each XORed with the current cell's value $grid[i][j]$.

To optimize space, we observe that the reachable XOR sums for the current row only depend on the results of the previous row and the cell immediately to the left. We can maintain a 2D DP table $dp[n][1024]$, where $dp[c]$ stores the set of reachable XOR values for column $c$. During the iteration over each row, we update the columns such that $dp[c]$ is computed using the previous row's $dp[c]$ (from above) and the current row's $dp[c-1]$ (from the left). Finally, the minimum XOR value reachable at the bottom-right cell $(m-1, n-1)$ is the smallest index $k$ such that $dp[n-1][k]$ is true.

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
    int minCost(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<char>> dp(n, vector<char>(1024, 0));

        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                vector<char> next_set(1024, 0);
                int val = grid[r][c];
                if (r == 0 && c == 0) {
                    next_set[val] = 1;
                } else {
                    if (r > 0) {
                        for (int k = 0; k < 1024; ++k) {
                            if (dp[c][k]) next_set[k ^ val] = 1;
                        }
                    }
                    if (c > 0) {
                        for (int k = 0; k < 1024; ++k) {
                            if (dp[c - 1][k]) next_set[k ^ val] = 1;
                        }
                    }
                }
                dp[c] = std::move(next_set);
            }
        }

        for (int k = 0; k < 1024; ++k) {
            if (dp[n - 1][k]) return k;
        }
        return -1;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minCost(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        boolean[][] dp = new boolean[n][1024];

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                boolean[] nextSet = new boolean[1024];
                int val = grid[r][c];
                if (r == 0 && c == 0) {
                    nextSet[val] = true;
                } else {
                    if (r > 0) {
                        for (int k = 0; k < 1024; k++) {
                            if (dp[c][k]) nextSet[k ^ val] = true;
                        }
                    }
                    if (c > 0) {
                        for (int k = 0; k < 1024; k++) {
                            if (dp[c - 1][k]) nextSet[k ^ val] = true;
                        }
                    }
                }
                dp[c] = nextSet;
            }
        }

        for (int k = 0; k < 1024; k++) {
            if (dp[n - 1][k]) return k;
        }
        return -1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [set() for _ in range(n)]

        for r in range(m):
            for c in range(n):
                val = grid[r][c]
                new_set = set()
                if r == 0 and c == 0:
                    new_set.add(val)
                else:
                    if r > 0:
                        for prev_xor in dp[c]:
                            new_set.add(prev_xor ^ val)
                    if c > 0:
                        for prev_xor in dp[c-1]:
                            new_set.add(prev_xor ^ val)
                dp[c] = new_set

        return min(dp[n-1])
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [set() for _ in range(n)]

        for r in range(m):
            for c in range(n):
                val = grid[r][c]
                new_set = set()
                if r == 0 and c == 0:
                    new_set.add(val)
                else:
                    if r > 0:
                        for prev_xor in dp[c]:
                            new_set.add(prev_xor ^ val)
                    if c > 0:
                        for prev_xor in dp[c-1]:
                            new_set.add(prev_xor ^ val)
                dp[c] = new_set

        return min(dp[n-1])
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

int minCost(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize;
    int n = gridColSize[0];
    unsigned char* dp = (unsigned char*)calloc(n * 1024, sizeof(unsigned char));

    for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
            unsigned char next_set[1024] = {0};
            int val = grid[r][c];
            if (r == 0 && c == 0) {
                next_set[val] = 1;
            } else {
                if (r > 0) {
                    for (int k = 0; k < 1024; k++) {
                        if (dp[c * 1024 + k]) next_set[k ^ val] = 1;
                    }
                }
                if (c > 0) {
                    for (int k = 0; k < 1024; k++) {
                        if (dp[(c - 1) * 1024 + k]) next_set[k ^ val] = 1;
                    }
                }
            }
            memcpy(&dp[c * 1024], next_set, 1024);
        }
    }

    int min_xor = 1023;
    for (int k = 0; k < 1024; k++) {
        if (dp[(n - 1) * 1024 + k]) {
            min_xor = k;
            break;
        }
    }

    free(dp);
    return min_xor;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinCost(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;
        int numCells = m * n;
        bool[] dp = new bool[numCells * 1024];

        dp[grid[0][0]] = true;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) continue;
                int val = grid[i][j];
                int currIdx = (i * n + j) * 1024;

                if (i > 0 && j > 0) {
                    int pR = (i - 1) * n * 1024;
                    int pC = (i * n + (j - 1)) * 1024;
                    for (int x = 0; x < 1024; x++) {
                        if (dp[pR + x] || dp[pC + x]) {
                            dp[currIdx + (x ^ val)] = true;
                        }
                    }
                } else if (i > 0) {
                    int pR = (i - 1) * n * 1024;
                    for (int x = 0; x < 1024; x++) {
                        if (dp[pR + x]) {
                            dp[currIdx + (x ^ val)] = true;
                        }
                    }
                } else if (j > 0) {
                    int pC = (i * n + (j - 1)) * 1024;
                    for (int x = 0; x < 1024; x++) {
                        if (dp[pC + x]) {
                            dp[currIdx + (x ^ val)] = true;
                        }
                    }
                }
            }
        }

        int lastCellIdx = (numCells - 1) * 1024;
        for (int x = 0; x < 1024; x++) {
            if (dp[lastCellIdx + x]) return x;
        }

        return -1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[][]} grid
 * @return {number}
 */
var minCost = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    const numCells = m * n;
    const dp = new Uint8Array(numCells * 1024);

    dp[grid[0][0]] = 1;

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (i === 0 && j === 0) continue;
            const val = grid[i][j];
            const currIdx = (i * n + j) * 1024;

            if (i > 0 && j > 0) {
                const pR = (i - 1) * n * 1024;
                const pC = (i * n + j - 1) * 1024;
                for (let x = 0; x < 1024; x++) {
                    if (dp[pR + x] || dp[pC + x]) {
                        dp[currIdx + (x ^ val)] = 1;
                    }
                }
            } else if (i > 0) {
                const pR = (i - 1) * n * 1024;
                for (let x = 0; x < 1024; x++) {
                    if (dp[pR + x]) {
                        dp[currIdx + (x ^ val)] = 1;
                    }
                }
            } else if (j > 0) {
                const pC = (i * n + j - 1) * 1024;
                for (let x = 0; x < 1024; x++) {
                    if (dp[pC + x]) {
                        dp[currIdx + (x ^ val)] = 1;
                    }
                }
            }
        }
    }

    const lastCellIdx = (numCells - 1) * 1024;
    for (let x = 0; x < 1024; x++) {
        if (dp[lastCellIdx + x]) return x;
    }

    return -1;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minCost(grid: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    const numCells = m * n;
    const dp = new Uint8Array(numCells * 1024);

    dp[grid[0][0]] = 1;

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (i === 0 && j === 0) continue;
            const val = grid[i][j];
            const currIdx = (i * n + j) * 1024;

            if (i > 0 && j > 0) {
                const pR = (i - 1) * n * 1024;
                const pC = (i * n + j - 1) * 1024;
                for (let x = 0; x < 1024; x++) {
                    if (dp[pR + x] || dp[pC + x]) {
                        dp[currIdx + (x ^ val)] = 1;
                    }
                }
            } else if (i > 0) {
                const pR = (i - 1) * n * 1024;
                for (let x = 0; x < 1024; x++) {
                    if (dp[pR + x]) {
                        dp[currIdx + (x ^ val)] = 1;
                    }
                }
            } else if (j > 0) {
                const pC = (i * n + j - 1) * 1024;
                for (let x = 0; x < 1024; x++) {
                    if (dp[pC + x]) {
                        dp[currIdx + (x ^ val)] = 1;
                    }
                }
            }
        }
    }

    const lastCellIdx = (numCells - 1) * 1024;
    for (let x = 0; x < 1024; x++) {
        if (dp[lastCellIdx + x]) return x;
    }

    return -1;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minCost($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $numCells = $m * $n;
        $dp = array_fill(0, $numCells * 1024, false);

        $dp[$grid[0][0]] = true;

        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($i === 0 && $j === 0) continue;
                $val = $grid[$i][$j];
                $currIdx = ($i * $n + $j) * 1024;

                if ($i > 0 && $j > 0) {
                    $pR = ($i - 1) * $n * 1024;
                    $pC = ($i * $n + $j - 1) * 1024;
                    for ($x = 0; $x < 1024; $x++) {
                        if ($dp[$pR + $x] || $dp[$pC + $x]) {
                            $dp[$currIdx + ($x ^ $val)] = true;
                        }
                    }
                } else if ($i > 0) {
                    $pR = ($i - 1) * $n * 1024;
                    for ($x = 0; $x < 1024; $x++) {
                        if ($dp[$pR + $x]) {
                            $dp[$currIdx + ($x ^ $val)] = true;
                        }
                    }
                } else if ($j > 0) {
                    $pC = ($i * $n + $j - 1) * 1024;
                    for ($x = 0; $x < 1024; $x++) {
                        if ($dp[$pC + $x]) {
                            $dp[$currIdx + ($x ^ $val)] = true;
                        }
                    }
                }
            }
        }

        $lastCellIdx = ($numCells - 1) * 1024;
        for ($x = 0; $x < 1024; $x++) {
            if ($dp[$lastCellIdx + $x]) return $x;
        }

        return -1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minCost(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        let numCells = m * n
        var dp = [Bool](repeating: false, count: numCells * 1024)

        dp[grid[0][0]] = true

        for i in 0..<m {
            for j in 0..<n {
                if i == 0 && j == 0 { continue }
                let val = grid[i][j]
                let currIdx = (i * n + j) * 1024

                if i > 0 && j > 0 {
                    let pR = (i - 1) * n * 1024
                    let pC = (i * n + j - 1) * 1024
                    for x in 0..<1024 {
                        if dp[pR + x] || dp[pC + x] {
                            dp[currIdx + (x ^ val)] = true
                        }
                    }
                } else if i > 0 {
                    let pR = (i - 1) * n * 1024
                    for x in 0..<1024 {
                        if dp[pR + x] {
                            dp[currIdx + (x ^ val)] = true
                        }
                    }
                } else if j > 0 {
                    let pC = (i * n + j - 1) * 1024
                    for x in 0..<1024 {
                        if dp[pC + x] {
                            dp[currIdx + (x ^ val)] = true
                        }
                    }
                }
            }
        }

        let lastCellIdx = (numCells - 1) * 1024
        for x in 0..<1024 {
            if dp[lastCellIdx + x] {
                return x
            }
        }

        return -1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import java.util.BitSet

class Solution {
    fun minCost(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        val dp = Array(m) { Array(n) { BitSet(1024) } }

        dp[0][0].set(grid[0][0])

        for (i in 0 until m) {
            for (j in 0 until n) {
                if (i == 0 && j == 0) continue

                val v = grid[i][j]
                val current = dp[i][j]

                if (i > 0) {
                    val prev = dp[i - 1][j]
                    var k = prev.nextSetBit(0)
                    while (k != -1) {
                        current.set(k xor v)
                        k = prev.nextSetBit(k + 1)
                    }
                }

                if (j > 0) {
                    val prev = dp[i][j - 1]
                    var k = prev.nextSetBit(0)
                    while (k != -1) {
                        current.set(k xor v)
                        k = prev.nextSetBit(k + 1)
                    }
                }
            }
        }

        return dp[m - 1][n - 1].nextSetBit(0)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minCost(List<List<int>> grid) {
    int m = grid.length;
    int n = grid[0].length;
    List<List<Set<int>>> dp = List.generate(m, (_) => List.generate(n, (_) => <int>{}));

    dp[0][0].add(grid[0][0]);

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (i == 0 && j == 0) continue;

        int v = grid[i][j];
        Set<int> current = dp[i][j];

        if (i > 0) {
          for (int k in dp[i - 1][j]) {
            current.add(k ^ v);
          }
        }

        if (j > 0) {
          for (int k in dp[i][j - 1]) {
            current.add(k ^ v);
          }
        }
      }
    }

    int minXor = 1024;
    for (int k in dp[m - 1][n - 1]) {
      if (k < minXor) minXor = k;
    }
    return minXor;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minCost(grid [][]int) int {
    m := len(grid)
    n := len(grid[0])

    dp := make([][]map[int]struct{}, m)
    for i := range dp {
        dp[i] = make([]map[int]struct{}, n)
        for j := range dp[i] {
            dp[i][j] = make(map[int]struct{})
        }
    }

    dp[0][0][grid[0][0]] = struct{}{}

    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if i == 0 && j == 0 {
                continue
            }

            v := grid[i][j]
            current := dp[i][j]

            if i > 0 {
                for k := range dp[i-1][j] {
                    current[k^v] = struct{}{}
                }
            }

            if j > 0 {
                for k := range dp[i][j-1] {
                    current[k^v] = struct{}{}
                }
            }
        }
    }

    minXor := 1024
    for k := range dp[m-1][n-1] {
        if k < minXor {
            minXor = k
        }
    }
    return minXor
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
require 'set'

# @param {Integer[][]} grid
# @return {Integer}
def min_cost(grid)
  m = grid.length
  n = grid[0].length

  dp = Array.new(m) { Array.new(n) { Set.new } }
  dp[0][0].add(grid[0][0])

  m.times do |i|
    n.times do |j|
      next if i == 0 && j == 0

      v = grid[i][j]
      current = dp[i][j]

      if i > 0
        dp[i-1][j].each { |k| current.add(k ^ v) }
      end

      if j > 0
        dp[i][j-1].each { |k| current.add(k ^ v) }
      end
    end
  end

  dp[m-1][n-1].min
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import java.util.BitSet

object Solution {
    def minCost(grid: Array[Array[Int]]): Int = {
        val m = grid.length
        val n = grid(0).length
        val dp = Array.tabulate(m, n)((_, _) => new BitSet(1024))

        dp(0)(0).set(grid(0)(0))

        for (i <- 0 until m) {
            for (j <- 0 until n) {
                if (i > 0 || j > 0) {
                    val v = grid(i)(j)
                    val current = dp(i)(j)

                    if (i > 0) {
                        val prev = dp(i - 1)(j)
                        var k = prev.nextSetBit(0)
                        while (k >= 0 && k < 1024) {
                            current.set(k ^ v)
                            k = prev.nextSetBit(k + 1)
                        }
                    }

                    if (j > 0) {
                        val prev = dp(i)(j - 1)
                        var k = prev.nextSetBit(0)
                        while (k >= 0 && k < 1024) {
                            current.set(k ^ v)
                            k = prev.nextSetBit(k + 1)
                        }
                    }
                }
            }
        }

        dp(m - 1)(n - 1).nextSetBit(0)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_cost(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut dp = vec![[false; 1024]; n];

        for i in 0..m {
            let mut next_dp = vec![[false; 1024]; n];
            for j in 0..n {
                let val = grid[i][j] as usize;
                if i == 0 && j == 0 {
                    next_dp[j][val] = true;
                } else if i == 0 {
                    for k in 0..1024 {
                        if next_dp[j - 1][k] {
                            next_dp[j][k ^ val] = true;
                        }
                    }
                } else if j == 0 {
                    for k in 0..1024 {
                        if dp[j][k] {
                            next_dp[j][k ^ val] = true;
                        }
                    }
                } else {
                    for k in 0..1024 {
                        if dp[j][k] || next_dp[j - 1][k] {
                            next_dp[j][k ^ val] = true;
                        }
                    }
                }
            }
            dp = next_dp;
        }

        for k in 0..1024 {
            if dp[n - 1][k] {
                return k as i32;
            }
        }
        0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-cost grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (letrec ([xor-mask (lambda (mask val)
                       (let ([new-mask 0])
                         (for ([k (in-range 1024)])
                           (when (bitwise-bit-set? mask k)
                             (set! new-mask (bitwise-ior new-mask (arithmetic-shift 1 (bitwise-xor k val))))))
                         new-mask))])
    (let* ([m (length grid)]
           [n (length (car grid))]
           [dp (make-vector n 0)])
      (for ([row grid] [i (in-naturals)])
        (for ([val row] [j (in-naturals)])
          (let ([current-mask 0])
            (cond
              [(and (= i 0) (= j 0))
               (set! current-mask (arithmetic-shift 1 val))]
              [(= i 0)
               (set! current-mask (xor-mask (vector-ref dp (- j 1)) val))]
              [(= j 0)
               (set! current-mask (xor-mask (vector-ref dp j) val))]
              [else
               (set! current-mask (xor-mask (bitwise-ior (vector-ref dp j) (vector-ref dp (- j 1))) val))])
            (vector-set! dp j current-mask))))
      (let ([final-mask (vector-ref dp (- n 1))])
        (let loop ([k 0])
          (if (bitwise-bit-set? final-mask k)
              k
              (loop (+ k 1))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_cost(Grid :: [[integer()]]) -> integer().
min_cost([FirstRow | RestRows]) ->
    FirstDP = build_first_row(FirstRow),
    FinalDP = lists:foldl(fun(Row, PrevDP) ->
        process_row(Row, PrevDP)
    end, FirstDP, RestRows),
    find_min(lists:last(FinalDP), 0).

build_first_row([Head | Tail]) ->
    FirstMask = 1 bsl Head,
    {_, RowDP_rev} = lists:foldl(fun(Val, {PrevMask, Acc}) ->
        NewMask = xor_mask(PrevMask, Val),
        {NewMask, [NewMask | Acc]}
    end, {FirstMask, [FirstMask]}, Tail),
    lists:reverse(RowDP_rev).

process_row(Row, PrevRowDP) ->
    {_, NewRowDP_rev} = lists:foldl(fun({Val, PrevRowMask}, {PrevColMask, Acc}) ->
        CombinedMask = PrevRowMask bor PrevColMask,
        NewMask = xor_mask(CombinedMask, Val),
        {NewMask, [NewMask | Acc]}
    end, {0, []}, lists:zip(Row, PrevRowDP)),
    lists:reverse(NewRowDP_rev).

xor_mask(Mask, Val) ->
    xor_mask_rec(Mask, Val, 0, 0).

xor_mask_rec(0, _Val, _K, Acc) -> Acc;
xor_mask_rec(Mask, Val, K, Acc) ->
    NewAcc = if (Mask band 1) /= 0 -> Acc bor (1 bsl (K bxor Val));
                true -> Acc
             end,
    xor_mask_rec(Mask bsr 1, Val, K + 1, NewAcc).

find_min(Mask, K) ->
    case (Mask band (1 bsl K)) of
        0 -> find_min(Mask, K + 1);
        _ -> K
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  import Bitwise

  @spec min_cost(grid :: [[integer]]) :: integer
  def min_cost([first_row | rest_rows]) do
    first_dp = build_first_row(first_row)
    final_dp = Enum.reduce(rest_rows, first_dp, fn row, prev_dp ->
      process_row(row, prev_dp)
    end)
    find_min(List.last(final_dp), 0)
  end

  defp build_first_row([head | tail]) do
    first_mask = 1 <<< head
    {_, row_dp_rev} = Enum.reduce(tail, {first_mask, [first_mask]}, fn val, {prev_mask, acc} ->
      new_mask = xor_mask(prev_mask, val)
      {new_mask, [new_mask | acc]}
    end)
    Enum.reverse(row_dp_rev)
  end

  defp process_row(row, prev_row_dp) do
    {_, new_row_dp_rev} = Enum.zip(row, prev_row_dp)
    |> Enum.reduce({0, []}, fn {val, prev_row_mask}, {prev_col_mask, acc} ->
      combined_mask = prev_row_mask ||| prev_col_mask
      new_mask = xor_mask(combined_mask, val)
      {new_mask, [new_mask | acc]}
    end)
    Enum.reverse(new_row_dp_rev)
  end

  defp xor_mask(mask, val) do
    xor_mask_rec(mask, val, 0, 0)
  end

  defp xor_mask_rec(0, _val, _k, acc), do: acc
  defp xor_mask_rec(mask, val, k, acc) do
    new_acc = if (mask &&& 1) != 0, do: acc ||| (1 <<< bxor(k, val)), else: acc
    xor_mask_rec(mask >>> 1, val, k + 1, new_acc)
  end

  defp find_min(mask, k) do
    if (mask &&& (1 <<< k)) != 0 do
      k
    else
      find_min(mask, k + 1)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(M * N * K) where M and N are the grid dimensions (with M * N ≤ 1000) and K is the maximum possible XOR value (1024). We iterate over each of the M * N cells exactly once and, for each cell, we potentially iterate through all K possible XOR values to update the reachability state.
- **Space Complexity:** O(N * K) where N is the number of columns and K is 1024. By using a row-by-row DP update, we only need to store the possible XOR values for each column of the current and previous rows.
