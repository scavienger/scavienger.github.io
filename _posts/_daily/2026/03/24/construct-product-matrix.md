---
layout: post
title: "Construct Product Matrix"
date: 2026-03-24 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Matrix", "Prefix Sum"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/construct-product-matrix/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<vector<int>> constructProductMatrix(vector<vector<int>>&\
        \ grid) {\n        int n = grid.size();\n        int m = grid[0].size();\n \
        \       vector<vector<int>> res(n, vector<int>(m));\n        int MOD = 12345;\n\
        \        long long running = 1;\n        for (int i = 0; i < n; ++i) {\n   \
        \         for (int j = 0; j < m; ++j) {\n                res[i][j] = (int)running;\n\
        \                running = (running * (grid[i][j] % MOD)) % MOD;\n         \
        \   }\n        }\n        running = 1;\n        for (int i = n - 1; i >= 0;\
        \ --i) {\n            for (int j = m - 1; j >= 0; --j) {\n                res[i][j]\
        \ = (int)((res[i][j] * running) % MOD);\n                running = (running\
        \ * (grid[i][j] % MOD)) % MOD;\n            }\n        }\n        return res;\n\
        \    }\n};"
      java: "class Solution {\n    public int[][] constructProductMatrix(int[][] grid)\
        \ {\n        int n = grid.length;\n        int m = grid[0].length;\n       \
        \ int[][] res = new int[n][m];\n        int MOD = 12345;\n        long running\
        \ = 1;\n        for (int i = 0; i < n; i++) {\n            for (int j = 0; j\
        \ < m; j++) {\n                res[i][j] = (int) running;\n                running\
        \ = (running * (grid[i][j] % MOD)) % MOD;\n            }\n        }\n      \
        \  running = 1;\n        for (int i = n - 1; i >= 0; i--) {\n            for\
        \ (int j = m - 1; j >= 0; j--) {\n                res[i][j] = (int) ((res[i][j]\
        \ * running) % MOD);\n                running = (running * (grid[i][j] % MOD))\
        \ % MOD;\n            }\n        }\n        return res;\n    }\n}"
      python: "class Solution(object):\n    def constructProductMatrix(self, grid):\n\
        \        \"\"\"\n        :type grid: List[List[int]]\n        :rtype: List[List[int]]\n\
        \        \"\"\"\n        n = len(grid)\n        m = len(grid[0])\n        res\
        \ = [[0] * m for _ in range(n)]\n        MOD = 12345\n        running = 1\n\
        \        for i in range(n):\n            for j in range(m):\n              \
        \  res[i][j] = running\n                running = (running * (grid[i][j] % MOD))\
        \ % MOD\n        running = 1\n        for i in range(n - 1, -1, -1):\n     \
        \       for j in range(m - 1, -1, -1):\n                res[i][j] = (res[i][j]\
        \ * running) % MOD\n                running = (running * (grid[i][j] % MOD))\
        \ % MOD\n        return res"
      python3: "class Solution:\n    def constructProductMatrix(self, grid: List[List[int]])\
        \ -> List[List[int]]:\n        n, m = len(grid), len(grid[0])\n        res =\
        \ [[0] * m for _ in range(n)]\n        MOD = 12345\n        running = 1\n  \
        \      for i in range(n):\n            for j in range(m):\n                res[i][j]\
        \ = running\n                running = (running * (grid[i][j] % MOD)) % MOD\n\
        \        running = 1\n        for i in range(n - 1, -1, -1):\n            for\
        \ j in range(m - 1, -1, -1):\n                res[i][j] = (res[i][j] * running)\
        \ % MOD\n                running = (running * (grid[i][j] % MOD)) % MOD\n  \
        \      return res"
      c: "/**\n * Return an array of arrays of size *returnSize.\n * The sizes of the\
        \ arrays are returned as *returnColumnSizes array.\n * Note: Both returned array\
        \ and *columnSizes array must be malloced, assume caller calls free().\n */\n\
        int** constructProductMatrix(int** grid, int gridSize, int* gridColSize, int*\
        \ returnSize, int** returnColumnSizes) {\n    *returnSize = gridSize;\n    *returnColumnSizes\
        \ = (int*)malloc(gridSize * sizeof(int));\n    int** res = (int**)malloc(gridSize\
        \ * sizeof(int*));\n    for (int i = 0; i < gridSize; i++) {\n        (*returnColumnSizes)[i]\
        \ = gridColSize[i];\n        res[i] = (int*)malloc(gridColSize[i] * sizeof(int));\n\
        \    }\n\n    int MOD = 12345;\n    long long running = 1;\n    for (int i =\
        \ 0; i < gridSize; i++) {\n        for (int j = 0; j < gridColSize[i]; j++)\
        \ {\n            res[i][j] = (int)running;\n            running = (running *\
        \ (grid[i][j] % MOD)) % MOD;\n        }\n    }\n\n    running = 1;\n    for\
        \ (int i = gridSize - 1; i >= 0; i--) {\n        for (int j = gridColSize[i]\
        \ - 1; j >= 0; j--) {\n            res[i][j] = (int)((res[i][j] * running) %\
        \ MOD);\n            running = (running * (grid[i][j] % MOD)) % MOD;\n     \
        \   }\n    }\n\n    return res;\n}"
      csharp: "public class Solution {\n    public int[][] ConstructProductMatrix(int[][]\
        \ grid) {\n        int n = grid.Length;\n        int m = grid[0].Length;\n \
        \       int[][] res = new int[n][];\n        for (int i = 0; i < n; i++) res[i]\
        \ = new int[m];\n\n        int MOD = 12345;\n        long running = 1;\n   \
        \     for (int i = 0; i < n; i++) {\n            for (int j = 0; j < m; j++)\
        \ {\n                res[i][j] = (int)running;\n                running = (running\
        \ * (grid[i][j] % MOD)) % MOD;\n            }\n        }\n\n        running\
        \ = 1;\n        for (int i = n - 1; i >= 0; i--) {\n            for (int j =\
        \ m - 1; j >= 0; j--) {\n                res[i][j] = (int)(( (long)res[i][j]\
        \ * running ) % MOD);\n                running = (running * (grid[i][j] % MOD))\
        \ % MOD;\n            }\n        }\n\n        return res;\n    }\n}"
      javascript: "/**\n * @param {number[][]} grid\n * @return {number[][]}\n */\n\
        var constructProductMatrix = function(grid) {\n    var n = grid.length;\n  \
        \  var m = grid[0].length;\n    var res = new Array(n);\n    for (var i = 0;\
        \ i < n; i++) {\n        res[i] = new Array(m);\n    }\n\n    var MOD = 12345;\n\
        \    var running = 1;\n    for (var i = 0; i < n; i++) {\n        for (var j\
        \ = 0; j < m; j++) {\n            res[i][j] = running;\n            running\
        \ = (running * (grid[i][j] % MOD)) % MOD;\n        }\n    }\n\n    running =\
        \ 1;\n    for (var i = n - 1; i >= 0; i--) {\n        for (var j = m - 1; j\
        \ >= 0; j--) {\n            res[i][j] = (res[i][j] * running) % MOD;\n     \
        \       running = (running * (grid[i][j] % MOD)) % MOD;\n        }\n    }\n\n\
        \    return res;\n};"
      typescript: "function constructProductMatrix(grid: number[][]): number[][] {\n\
        \    const n = grid.length;\n    const m = grid[0].length;\n    const MOD =\
        \ 12345;\n    const res: number[][] = Array.from({ length: n }, () => new Array(m).fill(0));\n\
        \n    let prefix = 1;\n    for (let i = 0; i < n; i++) {\n        for (let j\
        \ = 0; j < m; j++) {\n            res[i][j] = prefix;\n            prefix =\
        \ (prefix * (grid[i][j] % MOD)) % MOD;\n        }\n    }\n\n    let suffix =\
        \ 1;\n    for (let i = n - 1; i >= 0; i--) {\n        for (let j = m - 1; j\
        \ >= 0; j--) {\n            res[i][j] = (res[i][j] * suffix) % MOD;\n      \
        \      suffix = (suffix * (grid[i][j] % MOD)) % MOD;\n        }\n    }\n\n \
        \   return res;\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $grid\n     * @return\
        \ Integer[][]\n     */\n    function constructProductMatrix($grid) {\n     \
        \   $n = count($grid);\n        $m = count($grid[0]);\n        $MOD = 12345;\n\
        \        $res = [];\n        for ($i = 0; $i < $n; $i++) {\n            $res[$i]\
        \ = array_fill(0, $m, 0);\n        }\n\n        $prefix = 1;\n        for ($i\
        \ = 0; $i < $n; $i++) {\n            for ($j = 0; $j < $m; $j++) {\n       \
        \         $res[$i][$j] = $prefix;\n                $prefix = ($prefix * ($grid[$i][$j]\
        \ % $MOD)) % $MOD;\n            }\n        }\n\n        $suffix = 1;\n     \
        \   for ($i = $n - 1; $i >= 0; $i--) {\n            for ($j = $m - 1; $j >=\
        \ 0; $j--) {\n                $res[$i][$j] = ($res[$i][$j] * $suffix) % $MOD;\n\
        \                $suffix = ($suffix * ($grid[$i][$j] % $MOD)) % $MOD;\n    \
        \        }\n        }\n\n        return $res;\n    }\n}"
      swift: "class Solution {\n    func constructProductMatrix(_ grid: [[Int]]) ->\
        \ [[Int]] {\n        let n = grid.count\n        let m = grid[0].count\n   \
        \     let MOD = 12345\n        var res = Array(repeating: Array(repeating: 0,\
        \ count: m), count: n)\n\n        var prefix = 1\n        for i in 0..<n {\n\
        \            for j in 0..<m {\n                res[i][j] = prefix\n        \
        \        prefix = (prefix * (grid[i][j] % MOD)) % MOD\n            }\n     \
        \   }\n\n        var suffix = 1\n        for i in (0..<n).reversed() {\n   \
        \         for j in (0..<m).reversed() {\n                res[i][j] = (res[i][j]\
        \ * suffix) % MOD\n                suffix = (suffix * (grid[i][j] % MOD)) %\
        \ MOD\n            }\n        }\n\n        return res\n    }\n}"
      kotlin: "class Solution {\n    fun constructProductMatrix(grid: Array<IntArray>):\
        \ Array<IntArray> {\n        val n = grid.size\n        val m = grid[0].size\n\
        \        val MOD = 12345\n        val res = Array(n) { IntArray(m) }\n\n   \
        \     var prefix = 1\n        for (i in 0 until n) {\n            for (j in\
        \ 0 until m) {\n                res[i][j] = prefix\n                prefix =\
        \ (prefix * (grid[i][j] % MOD)) % MOD\n            }\n        }\n\n        var\
        \ suffix = 1\n        for (i in n - 1 downTo 0) {\n            for (j in m -\
        \ 1 downTo 0) {\n                res[i][j] = (res[i][j] * suffix) % MOD\n  \
        \              suffix = (suffix * (grid[i][j] % MOD)) % MOD\n            }\n\
        \        }\n\n        return res\n    }\n}"
      dart: "class Solution {\n  List<List<int>> constructProductMatrix(List<List<int>>\
        \ grid) {\n    int n = grid.length;\n    int m = grid[0].length;\n    int MOD\
        \ = 12345;\n    List<List<int>> res = List.generate(n, (_) => List.filled(m,\
        \ 0));\n\n    int prefix = 1;\n    for (int i = 0; i < n; i++) {\n      for\
        \ (int j = 0; j < m; j++) {\n        res[i][j] = prefix;\n        prefix = (prefix\
        \ * (grid[i][j] % MOD)) % MOD;\n      }\n    }\n\n    int suffix = 1;\n    for\
        \ (int i = n - 1; i >= 0; i--) {\n      for (int j = m - 1; j >= 0; j--) {\n\
        \        res[i][j] = (res[i][j] * suffix) % MOD;\n        suffix = (suffix *\
        \ (grid[i][j] % MOD)) % MOD;\n      }\n    }\n\n    return res;\n  }\n}"
      go: "func constructProductMatrix(grid [][]int) [][]int {\n\tn := len(grid)\n\t\
        m := len(grid[0])\n\tMOD := 12345\n\tres := make([][]int, n)\n\tfor i := range\
        \ res {\n\t\tres[i] = make([]int, m)\n\t}\n\n\tprefix := 1\n\tfor i := 0; i\
        \ < n; i++ {\n\t\tfor j := 0; j < m; j++ {\n\t\t\tres[i][j] = prefix\n\t\t\t\
        prefix = (prefix * (grid[i][j] % MOD)) % MOD\n\t\t}\n\t}\n\n\tsuffix := 1\n\t\
        for i := n - 1; i >= 0; i-- {\n\t\tfor j := m - 1; j >= 0; j-- {\n\t\t\tres[i][j]\
        \ = (res[i][j] * suffix) % MOD\n\t\t\tsuffix = (suffix * (grid[i][j] % MOD))\
        \ % MOD\n\t\t}\n\t}\n\n\treturn res\n}"
      ruby: "def construct_product_matrix(grid)\n  n = grid.length\n  m = grid[0].length\n\
        \  p = Array.new(n) { Array.new(m) }\n  mod = 12345\n  current_prod = 1\n  i\
        \ = 0\n  while i < n\n    j = 0\n    while j < m\n      p[i][j] = current_prod\n\
        \      current_prod = (current_prod * (grid[i][j] % mod)) % mod\n      j +=\
        \ 1\n    end\n    i += 1\n  end\n  current_prod = 1\n  i = n - 1\n  while i\
        \ >= 0\n    j = m - 1\n    while j >= 0\n      p[i][j] = (p[i][j] * current_prod)\
        \ % mod\n      current_prod = (current_prod * (grid[i][j] % mod)) % mod\n  \
        \    j -= 1\n    end\n    i -= 1\n  end\n  p\nend"
      scala: "object Solution {\n    def constructProductMatrix(grid: Array[Array[Int]]):\
        \ Array[Array[Int]] = {\n        val n = grid.length\n        val m = grid(0).length\n\
        \        val p = Array.ofDim[Int](n, m)\n        val mod = 12345\n\n       \
        \ var currentProd: Long = 1\n        var i = 0\n        while (i < n) {\n  \
        \          var j = 0\n            while (j < m) {\n                p(i)(j) =\
        \ currentProd.toInt\n                currentProd = (currentProd * (grid(i)(j)\
        \ % mod)) % mod\n                j += 1\n            }\n            i += 1\n\
        \        }\n\n        currentProd = 1\n        i = n - 1\n        while (i >=\
        \ 0) {\n            var j = m - 1\n            while (j >= 0) {\n          \
        \      p(i)(j) = ((p(i)(j).toLong * currentProd) % mod).toInt\n            \
        \    currentProd = (currentProd * (grid(i)(j) % mod)) % mod\n              \
        \  j -= 1\n            }\n            i -= 1\n        }\n        p\n    }\n}"
      rust: "impl Solution {\n    pub fn construct_product_matrix(grid: Vec<Vec<i32>>)\
        \ -> Vec<Vec<i32>> {\n        let n = grid.len();\n        let m = grid[0].len();\n\
        \        let mut p = vec![vec![0; m]; n];\n        let mut current_prod: i64\
        \ = 1;\n        let mod_val: i64 = 12345;\n\n        for i in 0..n {\n     \
        \       for j in 0..m {\n                p[i][j] = current_prod as i32;\n  \
        \              current_prod = (current_prod * (grid[i][j] as i64 % mod_val))\
        \ % mod_val;\n            }\n        }\n\n        current_prod = 1;\n      \
        \  for i in (0..n).rev() {\n            for j in (0..m).rev() {\n          \
        \      p[i][j] = ((p[i][j] as i64 * current_prod) % mod_val) as i32;\n     \
        \           current_prod = (current_prod * (grid[i][j] as i64 % mod_val)) %\
        \ mod_val;\n            }\n        }\n        p\n    }\n}"
      racket: "(require racket/list)\n(define/contract (construct-product-matrix grid)\n\
        \  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))\n\
        \  (let* ([n (length grid)]\n         [m (length (car grid))]\n         [flat\
        \ (append* grid)]\n         [len (* n m)]\n         [vec (list->vector flat)]\n\
        \         [res (make-vector len)]\n         [mod-val 12345])\n    (let loop\
        \ ([i 0] [prod 1])\n      (when (< i len)\n        (vector-set! res i prod)\n\
        \        (loop (+ i 1) (remainder (* prod (remainder (vector-ref vec i) mod-val))\
        \ mod-val))))\n    (let loop ([i (- len 1)] [prod 1])\n      (when (>= i 0)\n\
        \        (vector-set! res i (remainder (* (vector-ref res i) prod) mod-val))\n\
        \        (loop (- i 1) (remainder (* prod (remainder (vector-ref vec i) mod-val))\
        \ mod-val))))\n    (let ([res-list (vector->list res)])\n      (let chunk ([lst\
        \ res-list] [acc '()])\n        (if (null? lst)\n            (reverse acc)\n\
        \            (let loop ([i m] [l lst] [row '()])\n              (if (zero? i)\n\
        \                  (chunk l (cons (reverse row) acc))\n                  (loop\
        \ (- i 1) (cdr l) (cons (car l) row)))))))))"
      erlang: "-spec construct_product_matrix(Grid :: [[integer()]]) -> [[integer()]].\n\
        construct_product_matrix(Grid) ->\n  M = length(hd(Grid)),\n  Flat = lists:append(Grid),\n\
        \  {Prefixes, _} = lists:mapfoldl(fun(X, Prod) -> {Prod, (Prod * (X rem 12345))\
        \ rem 12345} end, 1, Flat),\n  {Suffixes, _} = lists:mapfoldr(fun(X, Prod) ->\
        \ {Prod, (Prod * (X rem 12345)) rem 12345} end, 1, Flat),\n  FlatRes = lists:zipwith(fun(P,\
        \ S) -> (P * S) rem 12345 end, Prefixes, Suffixes),\n  Chunk = fun(F, L, Acc)\
        \ ->\n            case L of\n              [] -> Acc;\n              _ -> {Row,\
        \ Rest} = lists:split(M, L), F(F, Rest, [Row | Acc])\n            end\n    \
        \      end,\n  lists:reverse(Chunk(Chunk, FlatRes, []))."
      elixir: "defmodule Solution do\n  @spec construct_product_matrix(grid :: [[integer]])\
        \ :: [[integer]]\n  def construct_product_matrix(grid) do\n    m = length(hd(grid))\n\
        \    flat = List.flatten(grid)\n    {prefixes, _} = Enum.map_reduce(flat, 1,\
        \ fn x, prod ->\n      {prod, rem(prod * rem(x, 12345), 12345)}\n    end)\n\
        \    {suffixes, _} = Enum.reverse(flat) |> Enum.map_reduce(1, fn x, prod ->\n\
        \      {prod, rem(prod * rem(x, 12345), 12345)}\n    end)\n    suffixes = Enum.reverse(suffixes)\n\
        \    flat_res = Enum.zip_with(prefixes, suffixes, fn p, s -> rem(p * s, 12345)\
        \ end)\n    Enum.chunk_every(flat_res, m)\n  end\nend"
    approach: 'The problem asks for the product of all elements in a 2D grid except
      for the element at the current position, all modulo 12345. Since the modulo is
      not prime, division is not reliable because the modular inverse might not exist.
      Instead, we use a prefix and suffix product strategy by treating the 2D grid as
      a flattened 1D array. We traverse the grid in row-major order, computing the product
      of all elements encountered so far to determine the prefix product for each position.


      The algorithm operates in two passes: a forward pass and a backward pass. In the
      forward pass, we store the running prefix product for each element $(i, j)$ in
      a result matrix and then update the running product by multiplying it with the
      current element. In the backward pass, we traverse the grid in reverse row-major
      order, maintain a running suffix product of all elements after $(i, j)$, and multiply
      the existing prefix product in the result matrix by this suffix. Both passes use
      the modulo 12345 to keep intermediate results small and prevent overflow.'
    time_complexity: O(n * m), where n is the number of rows and m is the number of
      columns. We iterate through the grid exactly twice—once forward and once backward—to
      compute prefix and suffix products.
    space_complexity: O(1) auxiliary space, excluding the space required for the result
      matrix. We only store a few constant-sized variables like the running product
      and loop indices.
    elapsed_time: 224.67789816856384
    model: gemini-3-flash-preview
    generated_at: '2026-03-24 01:26:00 '
---

## Problem #2906: Construct Product Matrix

**Difficulty:** Medium

**Topics:** Array, Matrix, Prefix Sum

## Problem Description

<p>Given a <strong>0-indexed</strong> 2D integer matrix <code><font face="monospace">grid</font></code><font face="monospace"> </font>of size <code>n * m</code>, we define a <strong>0-indexed</strong> 2D matrix <code>p</code> of size <code>n * m</code> as the <strong>product</strong> matrix of <code>grid</code> if the following condition is met:</p>

<ul>
	<li>Each element <code>p[i][j]</code> is calculated as the product of all elements in <code>grid</code> except for the element <code>grid[i][j]</code>. This product is then taken modulo <code><font face="monospace">12345</font></code>.</li>
</ul>

<p>Return <em>the product matrix of</em> <code><font face="monospace">grid</font></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> grid = [[1,2],[3,4]]
<strong>Output:</strong> [[24,12],[8,6]]
<strong>Explanation:</strong> p[0][0] = grid[0][1] * grid[1][0] * grid[1][1] = 2 * 3 * 4 = 24
p[0][1] = grid[0][0] * grid[1][0] * grid[1][1] = 1 * 3 * 4 = 12
p[1][0] = grid[0][0] * grid[0][1] * grid[1][1] = 1 * 2 * 4 = 8
p[1][1] = grid[0][0] * grid[0][1] * grid[1][0] = 1 * 2 * 3 = 6
So the answer is [[24,12],[8,6]].</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [[12345],[2],[1]]
<strong>Output:</strong> [[2],[0],[0]]
<strong>Explanation:</strong> p[0][0] = grid[0][1] * grid[0][2] = 2 * 1 = 2.
p[0][1] = grid[0][0] * grid[0][2] = 12345 * 1 = 12345. 12345 % 12345 = 0. So p[0][1] = 0.
p[0][2] = grid[0][0] * grid[0][1] = 12345 * 2 = 24690. 24690 % 12345 = 0. So p[0][2] = 0.
So the answer is [[2],[0],[0]].</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == grid.length&nbsp;&lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= m == grid[i].length&nbsp;&lt;= 10<sup>5</sup></code></li>
	<li><code>2 &lt;= n * m &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. Try to solve this without using the `'/'` (division operation).

2. Create two 2D arrays for suffix and prefix product, and use them to find the product for each position.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the product of all elements in a 2D grid except for the element at the current position, all modulo 12345. Since the modulo is not prime, division is not reliable because the modular inverse might not exist. Instead, we use a prefix and suffix product strategy by treating the 2D grid as a flattened 1D array. We traverse the grid in row-major order, computing the product of all elements encountered so far to determine the prefix product for each position.

The algorithm operates in two passes: a forward pass and a backward pass. In the forward pass, we store the running prefix product for each element $(i, j)$ in a result matrix and then update the running product by multiplying it with the current element. In the backward pass, we traverse the grid in reverse row-major order, maintain a running suffix product of all elements after $(i, j)$, and multiply the existing prefix product in the result matrix by this suffix. Both passes use the modulo 12345 to keep intermediate results small and prevent overflow.

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
    vector<vector<int>> constructProductMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        vector<vector<int>> res(n, vector<int>(m));
        int MOD = 12345;
        long long running = 1;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                res[i][j] = (int)running;
                running = (running * (grid[i][j] % MOD)) % MOD;
            }
        }
        running = 1;
        for (int i = n - 1; i >= 0; --i) {
            for (int j = m - 1; j >= 0; --j) {
                res[i][j] = (int)((res[i][j] * running) % MOD);
                running = (running * (grid[i][j] % MOD)) % MOD;
            }
        }
        return res;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int[][] constructProductMatrix(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        int[][] res = new int[n][m];
        int MOD = 12345;
        long running = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                res[i][j] = (int) running;
                running = (running * (grid[i][j] % MOD)) % MOD;
            }
        }
        running = 1;
        for (int i = n - 1; i >= 0; i--) {
            for (int j = m - 1; j >= 0; j--) {
                res[i][j] = (int) ((res[i][j] * running) % MOD);
                running = (running * (grid[i][j] % MOD)) % MOD;
            }
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
    def constructProductMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        m = len(grid[0])
        res = [[0] * m for _ in range(n)]
        MOD = 12345
        running = 1
        for i in range(n):
            for j in range(m):
                res[i][j] = running
                running = (running * (grid[i][j] % MOD)) % MOD
        running = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                res[i][j] = (res[i][j] * running) % MOD
                running = (running * (grid[i][j] % MOD)) % MOD
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        res = [[0] * m for _ in range(n)]
        MOD = 12345
        running = 1
        for i in range(n):
            for j in range(m):
                res[i][j] = running
                running = (running * (grid[i][j] % MOD)) % MOD
        running = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                res[i][j] = (res[i][j] * running) % MOD
                running = (running * (grid[i][j] % MOD)) % MOD
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** constructProductMatrix(int** grid, int gridSize, int* gridColSize, int* returnSize, int** returnColumnSizes) {
    *returnSize = gridSize;
    *returnColumnSizes = (int*)malloc(gridSize * sizeof(int));
    int** res = (int**)malloc(gridSize * sizeof(int*));
    for (int i = 0; i < gridSize; i++) {
        (*returnColumnSizes)[i] = gridColSize[i];
        res[i] = (int*)malloc(gridColSize[i] * sizeof(int));
    }

    int MOD = 12345;
    long long running = 1;
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < gridColSize[i]; j++) {
            res[i][j] = (int)running;
            running = (running * (grid[i][j] % MOD)) % MOD;
        }
    }

    running = 1;
    for (int i = gridSize - 1; i >= 0; i--) {
        for (int j = gridColSize[i] - 1; j >= 0; j--) {
            res[i][j] = (int)((res[i][j] * running) % MOD);
            running = (running * (grid[i][j] % MOD)) % MOD;
        }
    }

    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int[][] ConstructProductMatrix(int[][] grid) {
        int n = grid.Length;
        int m = grid[0].Length;
        int[][] res = new int[n][];
        for (int i = 0; i < n; i++) res[i] = new int[m];

        int MOD = 12345;
        long running = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                res[i][j] = (int)running;
                running = (running * (grid[i][j] % MOD)) % MOD;
            }
        }

        running = 1;
        for (int i = n - 1; i >= 0; i--) {
            for (int j = m - 1; j >= 0; j--) {
                res[i][j] = (int)(( (long)res[i][j] * running ) % MOD);
                running = (running * (grid[i][j] % MOD)) % MOD;
            }
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
 * @param {number[][]} grid
 * @return {number[][]}
 */
var constructProductMatrix = function(grid) {
    var n = grid.length;
    var m = grid[0].length;
    var res = new Array(n);
    for (var i = 0; i < n; i++) {
        res[i] = new Array(m);
    }

    var MOD = 12345;
    var running = 1;
    for (var i = 0; i < n; i++) {
        for (var j = 0; j < m; j++) {
            res[i][j] = running;
            running = (running * (grid[i][j] % MOD)) % MOD;
        }
    }

    running = 1;
    for (var i = n - 1; i >= 0; i--) {
        for (var j = m - 1; j >= 0; j--) {
            res[i][j] = (res[i][j] * running) % MOD;
            running = (running * (grid[i][j] % MOD)) % MOD;
        }
    }

    return res;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function constructProductMatrix(grid: number[][]): number[][] {
    const n = grid.length;
    const m = grid[0].length;
    const MOD = 12345;
    const res: number[][] = Array.from({ length: n }, () => new Array(m).fill(0));

    let prefix = 1;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            res[i][j] = prefix;
            prefix = (prefix * (grid[i][j] % MOD)) % MOD;
        }
    }

    let suffix = 1;
    for (let i = n - 1; i >= 0; i--) {
        for (let j = m - 1; j >= 0; j--) {
            res[i][j] = (res[i][j] * suffix) % MOD;
            suffix = (suffix * (grid[i][j] % MOD)) % MOD;
        }
    }

    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer[][]
     */
    function constructProductMatrix($grid) {
        $n = count($grid);
        $m = count($grid[0]);
        $MOD = 12345;
        $res = [];
        for ($i = 0; $i < $n; $i++) {
            $res[$i] = array_fill(0, $m, 0);
        }

        $prefix = 1;
        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $m; $j++) {
                $res[$i][$j] = $prefix;
                $prefix = ($prefix * ($grid[$i][$j] % $MOD)) % $MOD;
            }
        }

        $suffix = 1;
        for ($i = $n - 1; $i >= 0; $i--) {
            for ($j = $m - 1; $j >= 0; $j--) {
                $res[$i][$j] = ($res[$i][$j] * $suffix) % $MOD;
                $suffix = ($suffix * ($grid[$i][$j] % $MOD)) % $MOD;
            }
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
    func constructProductMatrix(_ grid: [[Int]]) -> [[Int]] {
        let n = grid.count
        let m = grid[0].count
        let MOD = 12345
        var res = Array(repeating: Array(repeating: 0, count: m), count: n)

        var prefix = 1
        for i in 0..<n {
            for j in 0..<m {
                res[i][j] = prefix
                prefix = (prefix * (grid[i][j] % MOD)) % MOD
            }
        }

        var suffix = 1
        for i in (0..<n).reversed() {
            for j in (0..<m).reversed() {
                res[i][j] = (res[i][j] * suffix) % MOD
                suffix = (suffix * (grid[i][j] % MOD)) % MOD
            }
        }

        return res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun constructProductMatrix(grid: Array<IntArray>): Array<IntArray> {
        val n = grid.size
        val m = grid[0].size
        val MOD = 12345
        val res = Array(n) { IntArray(m) }

        var prefix = 1
        for (i in 0 until n) {
            for (j in 0 until m) {
                res[i][j] = prefix
                prefix = (prefix * (grid[i][j] % MOD)) % MOD
            }
        }

        var suffix = 1
        for (i in n - 1 downTo 0) {
            for (j in m - 1 downTo 0) {
                res[i][j] = (res[i][j] * suffix) % MOD
                suffix = (suffix * (grid[i][j] % MOD)) % MOD
            }
        }

        return res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<List<int>> constructProductMatrix(List<List<int>> grid) {
    int n = grid.length;
    int m = grid[0].length;
    int MOD = 12345;
    List<List<int>> res = List.generate(n, (_) => List.filled(m, 0));

    int prefix = 1;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        res[i][j] = prefix;
        prefix = (prefix * (grid[i][j] % MOD)) % MOD;
      }
    }

    int suffix = 1;
    for (int i = n - 1; i >= 0; i--) {
      for (int j = m - 1; j >= 0; j--) {
        res[i][j] = (res[i][j] * suffix) % MOD;
        suffix = (suffix * (grid[i][j] % MOD)) % MOD;
      }
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
func constructProductMatrix(grid [][]int) [][]int {
	n := len(grid)
	m := len(grid[0])
	MOD := 12345
	res := make([][]int, n)
	for i := range res {
		res[i] = make([]int, m)
	}

	prefix := 1
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			res[i][j] = prefix
			prefix = (prefix * (grid[i][j] % MOD)) % MOD
		}
	}

	suffix := 1
	for i := n - 1; i >= 0; i-- {
		for j := m - 1; j >= 0; j-- {
			res[i][j] = (res[i][j] * suffix) % MOD
			suffix = (suffix * (grid[i][j] % MOD)) % MOD
		}
	}

	return res
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def construct_product_matrix(grid)
  n = grid.length
  m = grid[0].length
  p = Array.new(n) { Array.new(m) }
  mod = 12345
  current_prod = 1
  i = 0
  while i < n
    j = 0
    while j < m
      p[i][j] = current_prod
      current_prod = (current_prod * (grid[i][j] % mod)) % mod
      j += 1
    end
    i += 1
  end
  current_prod = 1
  i = n - 1
  while i >= 0
    j = m - 1
    while j >= 0
      p[i][j] = (p[i][j] * current_prod) % mod
      current_prod = (current_prod * (grid[i][j] % mod)) % mod
      j -= 1
    end
    i -= 1
  end
  p
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def constructProductMatrix(grid: Array[Array[Int]]): Array[Array[Int]] = {
        val n = grid.length
        val m = grid(0).length
        val p = Array.ofDim[Int](n, m)
        val mod = 12345

        var currentProd: Long = 1
        var i = 0
        while (i < n) {
            var j = 0
            while (j < m) {
                p(i)(j) = currentProd.toInt
                currentProd = (currentProd * (grid(i)(j) % mod)) % mod
                j += 1
            }
            i += 1
        }

        currentProd = 1
        i = n - 1
        while (i >= 0) {
            var j = m - 1
            while (j >= 0) {
                p(i)(j) = ((p(i)(j).toLong * currentProd) % mod).toInt
                currentProd = (currentProd * (grid(i)(j) % mod)) % mod
                j -= 1
            }
            i -= 1
        }
        p
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn construct_product_matrix(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = grid.len();
        let m = grid[0].len();
        let mut p = vec![vec![0; m]; n];
        let mut current_prod: i64 = 1;
        let mod_val: i64 = 12345;

        for i in 0..n {
            for j in 0..m {
                p[i][j] = current_prod as i32;
                current_prod = (current_prod * (grid[i][j] as i64 % mod_val)) % mod_val;
            }
        }

        current_prod = 1;
        for i in (0..n).rev() {
            for j in (0..m).rev() {
                p[i][j] = ((p[i][j] as i64 * current_prod) % mod_val) as i32;
                current_prod = (current_prod * (grid[i][j] as i64 % mod_val)) % mod_val;
            }
        }
        p
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(require racket/list)
(define/contract (construct-product-matrix grid)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  (let* ([n (length grid)]
         [m (length (car grid))]
         [flat (append* grid)]
         [len (* n m)]
         [vec (list->vector flat)]
         [res (make-vector len)]
         [mod-val 12345])
    (let loop ([i 0] [prod 1])
      (when (< i len)
        (vector-set! res i prod)
        (loop (+ i 1) (remainder (* prod (remainder (vector-ref vec i) mod-val)) mod-val))))
    (let loop ([i (- len 1)] [prod 1])
      (when (>= i 0)
        (vector-set! res i (remainder (* (vector-ref res i) prod) mod-val))
        (loop (- i 1) (remainder (* prod (remainder (vector-ref vec i) mod-val)) mod-val))))
    (let ([res-list (vector->list res)])
      (let chunk ([lst res-list] [acc '()])
        (if (null? lst)
            (reverse acc)
            (let loop ([i m] [l lst] [row '()])
              (if (zero? i)
                  (chunk l (cons (reverse row) acc))
                  (loop (- i 1) (cdr l) (cons (car l) row)))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec construct_product_matrix(Grid :: [[integer()]]) -> [[integer()]].
construct_product_matrix(Grid) ->
  M = length(hd(Grid)),
  Flat = lists:append(Grid),
  {Prefixes, _} = lists:mapfoldl(fun(X, Prod) -> {Prod, (Prod * (X rem 12345)) rem 12345} end, 1, Flat),
  {Suffixes, _} = lists:mapfoldr(fun(X, Prod) -> {Prod, (Prod * (X rem 12345)) rem 12345} end, 1, Flat),
  FlatRes = lists:zipwith(fun(P, S) -> (P * S) rem 12345 end, Prefixes, Suffixes),
  Chunk = fun(F, L, Acc) ->
            case L of
              [] -> Acc;
              _ -> {Row, Rest} = lists:split(M, L), F(F, Rest, [Row | Acc])
            end
          end,
  lists:reverse(Chunk(Chunk, FlatRes, [])).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec construct_product_matrix(grid :: [[integer]]) :: [[integer]]
  def construct_product_matrix(grid) do
    m = length(hd(grid))
    flat = List.flatten(grid)
    {prefixes, _} = Enum.map_reduce(flat, 1, fn x, prod ->
      {prod, rem(prod * rem(x, 12345), 12345)}
    end)
    {suffixes, _} = Enum.reverse(flat) |> Enum.map_reduce(1, fn x, prod ->
      {prod, rem(prod * rem(x, 12345), 12345)}
    end)
    suffixes = Enum.reverse(suffixes)
    flat_res = Enum.zip_with(prefixes, suffixes, fn p, s -> rem(p * s, 12345) end)
    Enum.chunk_every(flat_res, m)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n * m), where n is the number of rows and m is the number of columns. We iterate through the grid exactly twice—once forward and once backward—to compute prefix and suffix products.
- **Space Complexity:** O(1) auxiliary space, excluding the space required for the result matrix. We only store a few constant-sized variables like the running product and loop indices.
