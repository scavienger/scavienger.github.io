---
layout: post
title: "Minimum Absolute Difference in Sliding Submatrix"
date: 2026-03-20 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Sorting", "Matrix"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nclass\
        \ Solution {\npublic:\n    vector<vector<int>> minAbsDiff(vector<vector<int>>&\
        \ grid, int k) {\n        int m = grid.size();\n        int n = grid[0].size();\n\
        \        int rows = m - k + 1;\n        int cols = n - k + 1;\n        vector<vector<int>>\
        \ res(rows, vector<int>(cols));\n\n        for (int i = 0; i < rows; ++i) {\n\
        \            for (int j = 0; j < cols; ++j) {\n                vector<int> sub;\n\
        \                sub.reserve(k * k);\n                for (int r = i; r < i\
        \ + k; ++r) {\n                    for (int c = j; c < j + k; ++c) {\n     \
        \                   sub.push_back(grid[r][c]);\n                    }\n    \
        \            }\n                sort(sub.begin(), sub.end());\n            \
        \    int min_diff = 200001;\n                bool found = false;\n         \
        \       for (int p = 0; p < (int)sub.size() - 1; ++p) {\n                  \
        \  if (sub[p] != sub[p+1]) {\n                        min_diff = min(min_diff,\
        \ sub[p+1] - sub[p]);\n                        found = true;\n             \
        \       }\n                }\n                res[i][j] = found ? min_diff :\
        \ 0;\n            }\n        }\n        return res;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public int[][] minAbsDiff(int[][]\
        \ grid, int k) {\n        int m = grid.length;\n        int n = grid[0].length;\n\
        \        int rows = m - k + 1;\n        int cols = n - k + 1;\n        int[][]\
        \ res = new int[rows][cols];\n\n        int[] sub = new int[k * k];\n      \
        \  for (int i = 0; i < rows; i++) {\n            for (int j = 0; j < cols; j++)\
        \ {\n                int idx = 0;\n                for (int r = i; r < i + k;\
        \ r++) {\n                    for (int c = j; c < j + k; c++) {\n          \
        \              sub[idx++] = grid[r][c];\n                    }\n           \
        \     }\n                Arrays.sort(sub);\n                int minDiff = 200001;\n\
        \                boolean found = false;\n                for (int p = 0; p <\
        \ sub.length - 1; p++) {\n                    if (sub[p] != sub[p + 1]) {\n\
        \                        minDiff = Math.min(minDiff, sub[p + 1] - sub[p]);\n\
        \                        found = true;\n                    }\n            \
        \    }\n                res[i][j] = found ? minDiff : 0;\n            }\n  \
        \      }\n        return res;\n    }\n}"
      python: "class Solution(object):\n    def minAbsDiff(self, grid, k):\n       \
        \ \"\"\"\n        :type grid: List[List[int]]\n        :type k: int\n      \
        \  :rtype: List[List[int]]\n        \"\"\"\n        m, n = len(grid), len(grid[0])\n\
        \        rows, cols = m - k + 1, n - k + 1\n        res = [[0] * cols for _\
        \ in range(rows)]\n\n        for i in range(rows):\n            for j in range(cols):\n\
        \                sub = []\n                for r in range(i, i + k):\n     \
        \               sub.extend(grid[r][j:j+k])\n                distinct = sorted(list(set(sub)))\n\
        \                if len(distinct) < 2:\n                    res[i][j] = 0\n\
        \                else:\n                    md = min(distinct[p+1] - distinct[p]\
        \ for p in range(len(distinct)-1))\n                    res[i][j] = md\n   \
        \     return res"
      python3: "class Solution:\n    def minAbsDiff(self, grid: List[List[int]], k:\
        \ int) -> List[List[int]]:\n        m, n = len(grid), len(grid[0])\n       \
        \ rows, cols = m - k + 1, n - k + 1\n        res = [[0] * cols for _ in range(rows)]\n\
        \n        for i in range(rows):\n            for j in range(cols):\n       \
        \         sub = []\n                for r in range(i, i + k):\n            \
        \        sub.extend(grid[r][j:j+k])\n                distinct = sorted(list(set(sub)))\n\
        \                if len(distinct) < 2:\n                    res[i][j] = 0\n\
        \                else:\n                    md = min(distinct[p+1] - distinct[p]\
        \ for p in range(len(distinct)-1))\n                    res[i][j] = md\n   \
        \     return res"
      c: "#include <stdlib.h>\n#include <string.h>\n\nint compare(const void* a, const\
        \ void* b) {\n    int ia = *(const int*)a;\n    int ib = *(const int*)b;\n \
        \   if (ia < ib) return -1;\n    if (ia > ib) return 1;\n    return 0;\n}\n\n\
        int** minAbsDiff(int** grid, int gridSize, int* gridColSize, int k, int* returnSize,\
        \ int** returnColumnSizes) {\n    int m = gridSize;\n    int n = gridColSize[0];\n\
        \    int rows = m - k + 1;\n    int cols = n - k + 1;\n    *returnSize = rows;\n\
        \    *returnColumnSizes = (int*)malloc(rows * sizeof(int));\n    int** ans =\
        \ (int**)malloc(rows * sizeof(int*));\n    int* sub = (int*)malloc(k * k * sizeof(int));\n\
        \n    for (int i = 0; i < rows; i++) {\n        (*returnColumnSizes)[i] = cols;\n\
        \        ans[i] = (int*)malloc(cols * sizeof(int));\n        for (int j = 0;\
        \ j < cols; j++) {\n            int count = 0;\n            for (int r = i;\
        \ r < i + k; r++) {\n                for (int c = j; c < j + k; c++) {\n   \
        \                 sub[count++] = grid[r][c];\n                }\n          \
        \  }\n            qsort(sub, count, sizeof(int), compare);\n            int\
        \ md = 200001, found = 0;\n            for (int p = 0; p < count - 1; p++) {\n\
        \                if (sub[p] != sub[p+1]) {\n                    int diff = sub[p+1]\
        \ - sub[p];\n                    if (diff < md) md = diff;\n               \
        \     found = 1;\n                }\n            }\n            ans[i][j] =\
        \ found ? md : 0;\n        }\n    }\n    free(sub);\n    return ans;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int[][] MinAbsDiff(int[][] grid, int k) {\n        int m = grid.Length;\n\
        \        int n = grid[0].Length;\n        int rows = m - k + 1;\n        int\
        \ cols = n - k + 1;\n        int[][] res = new int[rows][];\n\n        int[]\
        \ sub = new int[k * k];\n        for (int i = 0; i < rows; i++) {\n        \
        \    res[i] = new int[cols];\n            for (int j = 0; j < cols; j++) {\n\
        \                int idx = 0;\n                for (int r = i; r < i + k; r++)\
        \ {\n                    for (int c = j; c < j + k; c++) {\n               \
        \         sub[idx++] = grid[r][c];\n                    }\n                }\n\
        \                Array.Sort(sub);\n                int minDiff = 200001;\n \
        \               bool found = false;\n                for (int p = 0; p < k *\
        \ k - 1; p++) {\n                    if (sub[p] != sub[p + 1]) {\n         \
        \               int diff = sub[p + 1] - sub[p];\n                        if\
        \ (diff < minDiff) minDiff = diff;\n                        found = true;\n\
        \                    }\n                }\n                res[i][j] = found\
        \ ? minDiff : 0;\n            }\n        }\n        return res;\n    }\n}"
      javascript: "/**\n * @param {number[][]} grid\n * @param {number} k\n * @return\
        \ {number[][]}\n */\nvar minAbsDiff = function(grid, k) {\n    const m = grid.length;\n\
        \    const n = grid[0].length;\n    const rows = m - k + 1;\n    const cols\
        \ = n - k + 1;\n    const res = Array.from({ length: rows }, () => new Array(cols).fill(0));\n\
        \n    for (let i = 0; i < rows; i++) {\n        for (let j = 0; j < cols; j++)\
        \ {\n            const sub = [];\n            for (let r = i; r < i + k; r++)\
        \ {\n                for (let c = j; c < j + k; c++) {\n                   \
        \ sub.push(grid[r][c]);\n                }\n            }\n            sub.sort((a,\
        \ b) => a - b);\n            let minDiff = 200001;\n            let found =\
        \ false;\n            for (let p = 0; p < sub.length - 1; p++) {\n         \
        \       if (sub[p] !== sub[p + 1]) {\n                    const diff = sub[p\
        \ + 1] - sub[p];\n                    if (diff < minDiff) minDiff = diff;\n\
        \                    found = true;\n                }\n            }\n     \
        \       res[i][j] = found ? minDiff : 0;\n        }\n    }\n    return res;\n\
        };"
      typescript: "function minAbsDiff(grid: number[][], k: number): number[][] {\n\
        \    const m = grid.length;\n    const n = grid[0].length;\n    const ans: number[][]\
        \ = Array.from({ length: m - k + 1 }, () => Array(n - k + 1).fill(0));\n   \
        \ for (let i = 0; i <= m - k; i++) {\n        for (let j = 0; j <= n - k; j++)\
        \ {\n            let distinct = new Set<number>();\n            for (let r =\
        \ i; r < i + k; r++) {\n                for (let c = j; c < j + k; c++) {\n\
        \                    distinct.add(grid[r][c]);\n                }\n        \
        \    }\n            if (distinct.size < 2) {\n                ans[i][j] = 0;\n\
        \            } else {\n                let sorted = Array.from(distinct).sort((a,\
        \ b) => a - b);\n                let minDiff = Infinity;\n                for\
        \ (let l = 0; l < sorted.length - 1; l++) {\n                    minDiff = Math.min(minDiff,\
        \ sorted[l + 1] - sorted[l]);\n                }\n                ans[i][j]\
        \ = minDiff;\n            }\n        }\n    }\n    return ans;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $grid\n     * @param\
        \ Integer $k\n     * @return Integer[][]\n     */\n    function minAbsDiff($grid,\
        \ $k) {\n        $m = count($grid);\n        $n = count($grid[0]);\n       \
        \ $ans = [];\n        for ($i = 0; $i <= $m - $k; $i++) {\n            $row\
        \ = [];\n            for ($j = 0; $j <= $n - $k; $j++) {\n                $distinct\
        \ = [];\n                for ($r = $i; $r < $i + $k; $r++) {\n             \
        \       for ($c = $j; $c < $j + $k; $c++) {\n                        $distinct[$grid[$r][$c]]\
        \ = true;\n                    }\n                }\n                $vals =\
        \ array_keys($distinct);\n                if (count($vals) < 2) {\n        \
        \            $row[] = 0;\n                } else {\n                    sort($vals);\n\
        \                    $minDiff = 1000000000;\n                    for ($l = 0;\
        \ $l < count($vals) - 1; $l++) {\n                        $diff = $vals[$l +\
        \ 1] - $vals[$l];\n                        if ($diff < $minDiff) {\n       \
        \                     $minDiff = $diff;\n                        }\n       \
        \             }\n                    $row[] = $minDiff;\n                }\n\
        \            }\n            $ans[] = $row;\n        }\n        return $ans;\n\
        \    }\n}"
      swift: "class Solution {\n    func minAbsDiff(_ grid: [[Int]], _ k: Int) -> [[Int]]\
        \ {\n        let m = grid.count\n        let n = grid[0].count\n        var\
        \ ans = [[Int]](repeating: [Int](repeating: 0, count: n - k + 1), count: m -\
        \ k + 1)\n        for i in 0...(m - k) {\n            for j in 0...(n - k) {\n\
        \                var distinct = Set<Int>()\n                for r in i..<(i\
        \ + k) {\n                    for c in j..<(j + k) {\n                     \
        \   distinct.insert(grid[r][c])\n                    }\n                }\n\
        \                if distinct.count < 2 {\n                    ans[i][j] = 0\n\
        \                } else {\n                    let sortedVals = distinct.sorted()\n\
        \                    var minDiff = 1000000000\n                    for l in\
        \ 0..<(sortedVals.count - 1) {\n                        let diff = sortedVals[l\
        \ + 1] - sortedVals[l]\n                        if diff < minDiff {\n      \
        \                      minDiff = diff\n                        }\n         \
        \           }\n                    ans[i][j] = minDiff\n                }\n\
        \            }\n        }\n        return ans\n    }\n}"
      kotlin: "class Solution {\n    fun minAbsDiff(grid: Array<IntArray>, k: Int):\
        \ Array<IntArray> {\n        val m = grid.size\n        val n = grid[0].size\n\
        \        val ans = Array(m - k + 1) { IntArray(n - k + 1) }\n        for (i\
        \ in 0..m - k) {\n            for (j in 0..n - k) {\n                val distinct\
        \ = mutableSetOf<Int>()\n                for (r in i until i + k) {\n      \
        \              for (c in j until j + k) {\n                        distinct.add(grid[r][c])\n\
        \                    }\n                }\n                if (distinct.size\
        \ < 2) {\n                    ans[i][j] = 0\n                } else {\n    \
        \                val sortedVals = distinct.sorted()\n                    var\
        \ minDiff = 1000000000\n                    for (l in 0 until sortedVals.size\
        \ - 1) {\n                        val diff = sortedVals[l + 1] - sortedVals[l]\n\
        \                        if (diff < minDiff) {\n                           \
        \ minDiff = diff\n                        }\n                    }\n       \
        \             ans[i][j] = minDiff\n                }\n            }\n      \
        \  }\n        return ans\n    }\n}"
      dart: "class Solution {\n  List<List<int>> minAbsDiff(List<List<int>> grid, int\
        \ k) {\n    int m = grid.length;\n    int n = grid[0].length;\n    List<List<int>>\
        \ ans = List.generate(m - k + 1, (_) => List.filled(n - k + 1, 0));\n    for\
        \ (int i = 0; i <= m - k; i++) {\n      for (int j = 0; j <= n - k; j++) {\n\
        \        Set<int> distinct = {};\n        for (int r = i; r < i + k; r++) {\n\
        \          for (int c = j; c < j + k; c++) {\n            distinct.add(grid[r][c]);\n\
        \          }\n        }\n        if (distinct.length < 2) {\n          ans[i][j]\
        \ = 0;\n        } else {\n          List<int> sortedVals = distinct.toList()..sort();\n\
        \          int minDiff = 1000000000;\n          for (int l = 0; l < sortedVals.length\
        \ - 1; l++) {\n            int diff = sortedVals[l + 1] - sortedVals[l];\n \
        \           if (diff < minDiff) minDiff = diff;\n          }\n          ans[i][j]\
        \ = minDiff;\n        }\n      }\n    }\n    return ans;\n  }\n}"
      go: "import (\n    \"sort\"\n)\n\nfunc minAbsDiff(grid [][]int, k int) [][]int\
        \ {\n    m := len(grid)\n    n := len(grid[0])\n    ans := make([][]int, m-k+1)\n\
        \    for i := 0; i <= m-k; i++ {\n        ans[i] = make([]int, n-k+1)\n    \
        \    for j := 0; j <= n-k; j++ {\n            distinctMap := make(map[int]struct{})\n\
        \            for r := i; r < i+k; r++ {\n                for c := j; c < j+k;\
        \ c++ {\n                    distinctMap[grid[r][c]] = struct{}{}\n        \
        \        }\n            }\n            if len(distinctMap) < 2 {\n         \
        \       ans[i][j] = 0\n            } else {\n                vals := make([]int,\
        \ 0, len(distinctMap))\n                for v := range distinctMap {\n     \
        \               vals = append(vals, v)\n                }\n                sort.Ints(vals)\n\
        \                minDiff := 1000000000\n                for l := 0; l < len(vals)-1;\
        \ l++ {\n                    diff := vals[l+1] - vals[l]\n                 \
        \   if diff < minDiff {\n                        minDiff = diff\n          \
        \          }\n                }\n                ans[i][j] = minDiff\n     \
        \       }\n        }\n    }\n    return ans\n}"
      ruby: "def min_abs_diff(grid, k)\n  m, n = grid.length, grid[0].length\n  (0..m\
        \ - k).map do |i|\n    (0..n - k).map do |j|\n      vals = []\n      (i...i\
        \ + k).each { |r| (j...j + k).each { |c| vals << grid[r][c] } }\n      uv =\
        \ vals.uniq.sort\n      uv.size < 2 ? 0 : uv.each_cons(2).map { |a, b| b - a\
        \ }.min\n    end\n  end\nend"
      scala: "object Solution {\n  def minAbsDiff(grid: Array[Array[Int]], k: Int):\
        \ Array[Array[Int]] = {\n    val m = grid.length\n    val n = grid(0).length\n\
        \    Array.tabulate(m - k + 1, n - k + 1) { (i, j) =>\n      val vals = for\
        \ (r <- i until i + k; c <- j until j + k) yield grid(r)(c)\n      val uv =\
        \ vals.distinct.sorted\n      if (uv.length < 2) 0\n      else uv.sliding(2).map(pair\
        \ => pair(1) - pair(0)).min\n    }\n  }\n}"
      rust: "impl Solution {\n    pub fn min_abs_diff(grid: Vec<Vec<i32>>, k: i32) ->\
        \ Vec<Vec<i32>> {\n        let (m, n, k_idx) = (grid.len(), grid[0].len(), k\
        \ as usize);\n        (0..=(m - k_idx)).map(|i| {\n            (0..=(n - k_idx)).map(|j|\
        \ {\n                let mut uv: Vec<i32> = (i..i + k_idx).flat_map(|r| (j..j\
        \ + k_idx).map(move |c| grid[r][c])).collect();\n                uv.sort_unstable();\n\
        \                uv.dedup();\n                if uv.len() < 2 { 0 } else {\n\
        \                    uv.windows(2).map(|w| w[1] - w[0]).min().unwrap_or(0)\n\
        \                }\n            }).collect()\n        }).collect()\n    }\n}"
      racket: "(define/contract (min-abs-diff grid k)\n  (-> (listof (listof exact-integer?))\
        \ exact-integer? (listof (listof exact-integer?)))\n  (let* ([m (length grid)]\n\
        \         [n (length (car grid))]\n         [gv (list->vector (map list->vector\
        \ grid))])\n    (for/list ([i (in-range (+ (- m k) 1))])\n      (for/list ([j\
        \ (in-range (+ (- n k) 1))])\n        (let* ([vals (for*/list ([r (in-range\
        \ i (+ i k))] [c (in-range j (+ j k))]) (vector-ref (vector-ref gv r) c))]\n\
        \               [uv (sort (remove-duplicates vals) <)])\n          (if (< (length\
        \ uv) 2) 0\n              (let loop ([lst uv] [cur-min 200001])\n          \
        \      (if (null? (cdr lst))\n                    cur-min\n                \
        \    (loop (cdr lst) (min cur-min (- (cadr lst) (car lst))))))))))))"
      erlang: "-spec min_abs_diff(Grid :: [[integer()]], K :: integer()) -> [[integer()]].\n\
        min_abs_diff(Grid, K) ->\n    M = length(Grid), N = length(hd(Grid)),\n    GV\
        \ = list_to_tuple([list_to_tuple(R) || R <- Grid]),\n    [ [ solve(GV, I, J,\
        \ K) || J <- lists:seq(1, N - K + 1) ] || I <- lists:seq(1, M - K + 1) ].\n\n\
        solve(GV, I, J, K) ->\n    V = [ element(C, element(R, GV)) || R <- lists:seq(I,\
        \ I + K - 1), C <- lists:seq(J, J + K - 1) ],\n    UV = lists:usort(V),\n  \
        \  case UV of\n        [_] -> 0;\n        [] -> 0;\n        _ -> find_min_diff(UV,\
        \ 200001)\n    end.\n\nfind_min_diff([_], Min) -> Min;\nfind_min_diff([H1, H2\
        \ | T], Min) -> find_min_diff([H2 | T], erlang:min(Min, H2 - H1))."
      elixir: "defmodule Solution do\n  @spec min_abs_diff(grid :: [[integer]], k ::\
        \ integer) :: [[integer]]\n  def min_abs_diff(grid, k) do\n    m = length(grid)\n\
        \    n = length(hd(grid))\n    gv = grid |> Enum.map(&List.to_tuple/1) |> List.to_tuple()\n\
        \    for i <- 0..(m - k) do\n      for j <- 0..(n - k) do\n        vals = for\
        \ r <- i..(i + k - 1), c <- j..(j + k - 1) do\n          elem(elem(gv, r), c)\n\
        \        end\n        uv = Enum.uniq(vals) |> Enum.sort()\n        if length(uv)\
        \ < 2 do\n          0\n        else\n          uv |> Enum.chunk_every(2, 1,\
        \ :discard) |> Enum.map(fn [a, b] -> b - a end) |> Enum.min()\n        end\n\
        \      end\n    end\n  end\nend"
    approach: 'The algorithm uses a brute-force strategy by iterating through every
      possible top-left corner (i, j) of a k by k submatrix. Given that the matrix dimensions
      are small (up to 30 by 30), we can afford to explicitly process each submatrix.
      For every starting position, we collect all k*k elements into a temporary list
      or set to prepare for the calculation of the minimum absolute difference between
      distinct values.


      To find this minimum difference efficiently, we sort the elements of the submatrix.
      Once sorted, any minimum difference between distinct values must occur between
      adjacent elements in the sorted list. We iterate through the sorted array, skipping
      over identical adjacent values to satisfy the ''distinct'' requirement, and calculate
      the difference between non-equal neighbors. If the submatrix contains only one
      distinct value, the iteration will not produce any differences, and we return
      0 as per the problem''s note. The results are stored in a result matrix of size
      (m-k+1) by (n-k+1).'
    time_complexity: O((m - k + 1) * (n - k + 1) * k^2 * log(k^2)). There are (m - k
      + 1) * (n - k + 1) possible k by k submatrices. For each submatrix, we collect
      k^2 elements and sort them, taking O(k^2 log k^2) time. With m, n, k <= 30, the
      total number of operations is approximately 8 * 10^6, which fits comfortably within
      the time limit.
    space_complexity: O(m * n). This includes the storage for the output result matrix
      and the temporary memory (O(k^2)) used to store and sort the elements of each
      submatrix during processing.
    elapsed_time: 212.4430980682373
    model: gemini-3-flash-preview
    generated_at: '2026-03-20 01:27:10 '
---

## Problem #3567: Minimum Absolute Difference in Sliding Submatrix

**Difficulty:** Medium

**Topics:** Array, Sorting, Matrix

## Problem Description

<p>You are given an <code>m x n</code> integer matrix <code>grid</code> and an integer <code>k</code>.</p>

<p>For every contiguous <code>k x k</code> <strong>submatrix</strong> of <code>grid</code>, compute the <strong>minimum absolute</strong> difference between any two <strong>distinct</strong> values within that <strong>submatrix</strong>.</p>

<p>Return a 2D array <code>ans</code> of size <code>(m - k + 1) x (n - k + 1)</code>, where <code>ans[i][j]</code> is the minimum absolute difference in the submatrix whose top-left corner is <code>(i, j)</code> in <code>grid</code>.</p>

<p><strong>Note</strong>: If all elements in the submatrix have the same value, the answer will be 0.</p>
A submatrix <code>(x1, y1, x2, y2)</code> is a matrix that is formed by choosing all cells <code>matrix[x][y]</code> where <code>x1 &lt;= x &lt;= x2</code> and <code>y1 &lt;= y &lt;= y2</code>.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,8],[3,-2]], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">[[2]]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>There is only one possible <code>k x k</code> submatrix: <code><span class="example-io">[[1, 8], [3, -2]]</span></code><span class="example-io">.</span></li>
	<li>Distinct values in the submatrix are<span class="example-io"> <code>[1, 8, 3, -2]</code>.</span></li>
	<li>The minimum absolute difference in the submatrix is <code>|1 - 3| = 2</code>. Thus, the answer is <code>[[2]]</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[3,-1]], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">[[0,0]]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Both <code>k x k</code> submatrix has only one distinct element.</li>
	<li>Thus, the answer is <code>[[0, 0]]</code>.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,-2,3],[2,3,5]], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">[[1,2]]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>There are two possible <code>k &times; k</code> submatrix:

	<ul>
		<li>Starting at <code>(0, 0)</code>: <code>[[1, -2], [2, 3]]</code>.

		<ul>
			<li>Distinct values in the submatrix are <code>[1, -2, 2, 3]</code>.</li>
			<li>The minimum absolute difference in the submatrix is <code>|1 - 2| = 1</code>.</li>
		</ul>
		</li>
		<li>Starting at <code>(0, 1)</code>: <code>[[-2, 3], [3, 5]]</code>.
		<ul>
			<li>Distinct values in the submatrix are <code>[-2, 3, 5]</code>.</li>
			<li>The minimum absolute difference in the submatrix is <code>|3 - 5| = 2</code>.</li>
		</ul>
		</li>
	</ul>
	</li>
	<li>Thus, the answer is <code>[[1, 2]]</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m == grid.length &lt;= 30</code></li>
	<li><code>1 &lt;= n == grid[i].length &lt;= 30</code></li>
	<li><code>-10<sup>5</sup> &lt;= grid[i][j] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= min(m, n)</code></li>
</ul>


## Hints

1. Use bruteforce over the submatrices

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm uses a brute-force strategy by iterating through every possible top-left corner (i, j) of a k by k submatrix. Given that the matrix dimensions are small (up to 30 by 30), we can afford to explicitly process each submatrix. For every starting position, we collect all k*k elements into a temporary list or set to prepare for the calculation of the minimum absolute difference between distinct values.

To find this minimum difference efficiently, we sort the elements of the submatrix. Once sorted, any minimum difference between distinct values must occur between adjacent elements in the sorted list. We iterate through the sorted array, skipping over identical adjacent values to satisfy the 'distinct' requirement, and calculate the difference between non-equal neighbors. If the submatrix contains only one distinct value, the iteration will not produce any differences, and we return 0 as per the problem's note. The results are stored in a result matrix of size (m-k+1) by (n-k+1).

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
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> minAbsDiff(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();
        int rows = m - k + 1;
        int cols = n - k + 1;
        vector<vector<int>> res(rows, vector<int>(cols));

        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                vector<int> sub;
                sub.reserve(k * k);
                for (int r = i; r < i + k; ++r) {
                    for (int c = j; c < j + k; ++c) {
                        sub.push_back(grid[r][c]);
                    }
                }
                sort(sub.begin(), sub.end());
                int min_diff = 200001;
                bool found = false;
                for (int p = 0; p < (int)sub.size() - 1; ++p) {
                    if (sub[p] != sub[p+1]) {
                        min_diff = min(min_diff, sub[p+1] - sub[p]);
                        found = true;
                    }
                }
                res[i][j] = found ? min_diff : 0;
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
import java.util.*;

class Solution {
    public int[][] minAbsDiff(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        int rows = m - k + 1;
        int cols = n - k + 1;
        int[][] res = new int[rows][cols];

        int[] sub = new int[k * k];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                int idx = 0;
                for (int r = i; r < i + k; r++) {
                    for (int c = j; c < j + k; c++) {
                        sub[idx++] = grid[r][c];
                    }
                }
                Arrays.sort(sub);
                int minDiff = 200001;
                boolean found = false;
                for (int p = 0; p < sub.length - 1; p++) {
                    if (sub[p] != sub[p + 1]) {
                        minDiff = Math.min(minDiff, sub[p + 1] - sub[p]);
                        found = true;
                    }
                }
                res[i][j] = found ? minDiff : 0;
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
    def minAbsDiff(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        rows, cols = m - k + 1, n - k + 1
        res = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                sub = []
                for r in range(i, i + k):
                    sub.extend(grid[r][j:j+k])
                distinct = sorted(list(set(sub)))
                if len(distinct) < 2:
                    res[i][j] = 0
                else:
                    md = min(distinct[p+1] - distinct[p] for p in range(len(distinct)-1))
                    res[i][j] = md
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rows, cols = m - k + 1, n - k + 1
        res = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                sub = []
                for r in range(i, i + k):
                    sub.extend(grid[r][j:j+k])
                distinct = sorted(list(set(sub)))
                if len(distinct) < 2:
                    res[i][j] = 0
                else:
                    md = min(distinct[p+1] - distinct[p] for p in range(len(distinct)-1))
                    res[i][j] = md
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

int compare(const void* a, const void* b) {
    int ia = *(const int*)a;
    int ib = *(const int*)b;
    if (ia < ib) return -1;
    if (ia > ib) return 1;
    return 0;
}

int** minAbsDiff(int** grid, int gridSize, int* gridColSize, int k, int* returnSize, int** returnColumnSizes) {
    int m = gridSize;
    int n = gridColSize[0];
    int rows = m - k + 1;
    int cols = n - k + 1;
    *returnSize = rows;
    *returnColumnSizes = (int*)malloc(rows * sizeof(int));
    int** ans = (int**)malloc(rows * sizeof(int*));
    int* sub = (int*)malloc(k * k * sizeof(int));

    for (int i = 0; i < rows; i++) {
        (*returnColumnSizes)[i] = cols;
        ans[i] = (int*)malloc(cols * sizeof(int));
        for (int j = 0; j < cols; j++) {
            int count = 0;
            for (int r = i; r < i + k; r++) {
                for (int c = j; c < j + k; c++) {
                    sub[count++] = grid[r][c];
                }
            }
            qsort(sub, count, sizeof(int), compare);
            int md = 200001, found = 0;
            for (int p = 0; p < count - 1; p++) {
                if (sub[p] != sub[p+1]) {
                    int diff = sub[p+1] - sub[p];
                    if (diff < md) md = diff;
                    found = 1;
                }
            }
            ans[i][j] = found ? md : 0;
        }
    }
    free(sub);
    return ans;
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
    public int[][] MinAbsDiff(int[][] grid, int k) {
        int m = grid.Length;
        int n = grid[0].Length;
        int rows = m - k + 1;
        int cols = n - k + 1;
        int[][] res = new int[rows][];

        int[] sub = new int[k * k];
        for (int i = 0; i < rows; i++) {
            res[i] = new int[cols];
            for (int j = 0; j < cols; j++) {
                int idx = 0;
                for (int r = i; r < i + k; r++) {
                    for (int c = j; c < j + k; c++) {
                        sub[idx++] = grid[r][c];
                    }
                }
                Array.Sort(sub);
                int minDiff = 200001;
                bool found = false;
                for (int p = 0; p < k * k - 1; p++) {
                    if (sub[p] != sub[p + 1]) {
                        int diff = sub[p + 1] - sub[p];
                        if (diff < minDiff) minDiff = diff;
                        found = true;
                    }
                }
                res[i][j] = found ? minDiff : 0;
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
 * @param {number} k
 * @return {number[][]}
 */
var minAbsDiff = function(grid, k) {
    const m = grid.length;
    const n = grid[0].length;
    const rows = m - k + 1;
    const cols = n - k + 1;
    const res = Array.from({ length: rows }, () => new Array(cols).fill(0));

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            const sub = [];
            for (let r = i; r < i + k; r++) {
                for (let c = j; c < j + k; c++) {
                    sub.push(grid[r][c]);
                }
            }
            sub.sort((a, b) => a - b);
            let minDiff = 200001;
            let found = false;
            for (let p = 0; p < sub.length - 1; p++) {
                if (sub[p] !== sub[p + 1]) {
                    const diff = sub[p + 1] - sub[p];
                    if (diff < minDiff) minDiff = diff;
                    found = true;
                }
            }
            res[i][j] = found ? minDiff : 0;
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
function minAbsDiff(grid: number[][], k: number): number[][] {
    const m = grid.length;
    const n = grid[0].length;
    const ans: number[][] = Array.from({ length: m - k + 1 }, () => Array(n - k + 1).fill(0));
    for (let i = 0; i <= m - k; i++) {
        for (let j = 0; j <= n - k; j++) {
            let distinct = new Set<number>();
            for (let r = i; r < i + k; r++) {
                for (let c = j; c < j + k; c++) {
                    distinct.add(grid[r][c]);
                }
            }
            if (distinct.size < 2) {
                ans[i][j] = 0;
            } else {
                let sorted = Array.from(distinct).sort((a, b) => a - b);
                let minDiff = Infinity;
                for (let l = 0; l < sorted.length - 1; l++) {
                    minDiff = Math.min(minDiff, sorted[l + 1] - sorted[l]);
                }
                ans[i][j] = minDiff;
            }
        }
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
     * @param Integer[][] $grid
     * @param Integer $k
     * @return Integer[][]
     */
    function minAbsDiff($grid, $k) {
        $m = count($grid);
        $n = count($grid[0]);
        $ans = [];
        for ($i = 0; $i <= $m - $k; $i++) {
            $row = [];
            for ($j = 0; $j <= $n - $k; $j++) {
                $distinct = [];
                for ($r = $i; $r < $i + $k; $r++) {
                    for ($c = $j; $c < $j + $k; $c++) {
                        $distinct[$grid[$r][$c]] = true;
                    }
                }
                $vals = array_keys($distinct);
                if (count($vals) < 2) {
                    $row[] = 0;
                } else {
                    sort($vals);
                    $minDiff = 1000000000;
                    for ($l = 0; $l < count($vals) - 1; $l++) {
                        $diff = $vals[$l + 1] - $vals[$l];
                        if ($diff < $minDiff) {
                            $minDiff = $diff;
                        }
                    }
                    $row[] = $minDiff;
                }
            }
            $ans[] = $row;
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
    func minAbsDiff(_ grid: [[Int]], _ k: Int) -> [[Int]] {
        let m = grid.count
        let n = grid[0].count
        var ans = [[Int]](repeating: [Int](repeating: 0, count: n - k + 1), count: m - k + 1)
        for i in 0...(m - k) {
            for j in 0...(n - k) {
                var distinct = Set<Int>()
                for r in i..<(i + k) {
                    for c in j..<(j + k) {
                        distinct.insert(grid[r][c])
                    }
                }
                if distinct.count < 2 {
                    ans[i][j] = 0
                } else {
                    let sortedVals = distinct.sorted()
                    var minDiff = 1000000000
                    for l in 0..<(sortedVals.count - 1) {
                        let diff = sortedVals[l + 1] - sortedVals[l]
                        if diff < minDiff {
                            minDiff = diff
                        }
                    }
                    ans[i][j] = minDiff
                }
            }
        }
        return ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minAbsDiff(grid: Array<IntArray>, k: Int): Array<IntArray> {
        val m = grid.size
        val n = grid[0].size
        val ans = Array(m - k + 1) { IntArray(n - k + 1) }
        for (i in 0..m - k) {
            for (j in 0..n - k) {
                val distinct = mutableSetOf<Int>()
                for (r in i until i + k) {
                    for (c in j until j + k) {
                        distinct.add(grid[r][c])
                    }
                }
                if (distinct.size < 2) {
                    ans[i][j] = 0
                } else {
                    val sortedVals = distinct.sorted()
                    var minDiff = 1000000000
                    for (l in 0 until sortedVals.size - 1) {
                        val diff = sortedVals[l + 1] - sortedVals[l]
                        if (diff < minDiff) {
                            minDiff = diff
                        }
                    }
                    ans[i][j] = minDiff
                }
            }
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
class Solution {
  List<List<int>> minAbsDiff(List<List<int>> grid, int k) {
    int m = grid.length;
    int n = grid[0].length;
    List<List<int>> ans = List.generate(m - k + 1, (_) => List.filled(n - k + 1, 0));
    for (int i = 0; i <= m - k; i++) {
      for (int j = 0; j <= n - k; j++) {
        Set<int> distinct = {};
        for (int r = i; r < i + k; r++) {
          for (int c = j; c < j + k; c++) {
            distinct.add(grid[r][c]);
          }
        }
        if (distinct.length < 2) {
          ans[i][j] = 0;
        } else {
          List<int> sortedVals = distinct.toList()..sort();
          int minDiff = 1000000000;
          for (int l = 0; l < sortedVals.length - 1; l++) {
            int diff = sortedVals[l + 1] - sortedVals[l];
            if (diff < minDiff) minDiff = diff;
          }
          ans[i][j] = minDiff;
        }
      }
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
import (
    "sort"
)

func minAbsDiff(grid [][]int, k int) [][]int {
    m := len(grid)
    n := len(grid[0])
    ans := make([][]int, m-k+1)
    for i := 0; i <= m-k; i++ {
        ans[i] = make([]int, n-k+1)
        for j := 0; j <= n-k; j++ {
            distinctMap := make(map[int]struct{})
            for r := i; r < i+k; r++ {
                for c := j; c < j+k; c++ {
                    distinctMap[grid[r][c]] = struct{}{}
                }
            }
            if len(distinctMap) < 2 {
                ans[i][j] = 0
            } else {
                vals := make([]int, 0, len(distinctMap))
                for v := range distinctMap {
                    vals = append(vals, v)
                }
                sort.Ints(vals)
                minDiff := 1000000000
                for l := 0; l < len(vals)-1; l++ {
                    diff := vals[l+1] - vals[l]
                    if diff < minDiff {
                        minDiff = diff
                    }
                }
                ans[i][j] = minDiff
            }
        }
    }
    return ans
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def min_abs_diff(grid, k)
  m, n = grid.length, grid[0].length
  (0..m - k).map do |i|
    (0..n - k).map do |j|
      vals = []
      (i...i + k).each { |r| (j...j + k).each { |c| vals << grid[r][c] } }
      uv = vals.uniq.sort
      uv.size < 2 ? 0 : uv.each_cons(2).map { |a, b| b - a }.min
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
  def minAbsDiff(grid: Array[Array[Int]], k: Int): Array[Array[Int]] = {
    val m = grid.length
    val n = grid(0).length
    Array.tabulate(m - k + 1, n - k + 1) { (i, j) =>
      val vals = for (r <- i until i + k; c <- j until j + k) yield grid(r)(c)
      val uv = vals.distinct.sorted
      if (uv.length < 2) 0
      else uv.sliding(2).map(pair => pair(1) - pair(0)).min
    }
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_abs_diff(grid: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let (m, n, k_idx) = (grid.len(), grid[0].len(), k as usize);
        (0..=(m - k_idx)).map(|i| {
            (0..=(n - k_idx)).map(|j| {
                let mut uv: Vec<i32> = (i..i + k_idx).flat_map(|r| (j..j + k_idx).map(move |c| grid[r][c])).collect();
                uv.sort_unstable();
                uv.dedup();
                if uv.len() < 2 { 0 } else {
                    uv.windows(2).map(|w| w[1] - w[0]).min().unwrap_or(0)
                }
            }).collect()
        }).collect()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-abs-diff grid k)
  (-> (listof (listof exact-integer?)) exact-integer? (listof (listof exact-integer?)))
  (let* ([m (length grid)]
         [n (length (car grid))]
         [gv (list->vector (map list->vector grid))])
    (for/list ([i (in-range (+ (- m k) 1))])
      (for/list ([j (in-range (+ (- n k) 1))])
        (let* ([vals (for*/list ([r (in-range i (+ i k))] [c (in-range j (+ j k))]) (vector-ref (vector-ref gv r) c))]
               [uv (sort (remove-duplicates vals) <)])
          (if (< (length uv) 2) 0
              (let loop ([lst uv] [cur-min 200001])
                (if (null? (cdr lst))
                    cur-min
                    (loop (cdr lst) (min cur-min (- (cadr lst) (car lst))))))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_abs_diff(Grid :: [[integer()]], K :: integer()) -> [[integer()]].
min_abs_diff(Grid, K) ->
    M = length(Grid), N = length(hd(Grid)),
    GV = list_to_tuple([list_to_tuple(R) || R <- Grid]),
    [ [ solve(GV, I, J, K) || J <- lists:seq(1, N - K + 1) ] || I <- lists:seq(1, M - K + 1) ].

solve(GV, I, J, K) ->
    V = [ element(C, element(R, GV)) || R <- lists:seq(I, I + K - 1), C <- lists:seq(J, J + K - 1) ],
    UV = lists:usort(V),
    case UV of
        [_] -> 0;
        [] -> 0;
        _ -> find_min_diff(UV, 200001)
    end.

find_min_diff([_], Min) -> Min;
find_min_diff([H1, H2 | T], Min) -> find_min_diff([H2 | T], erlang:min(Min, H2 - H1)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_abs_diff(grid :: [[integer]], k :: integer) :: [[integer]]
  def min_abs_diff(grid, k) do
    m = length(grid)
    n = length(hd(grid))
    gv = grid |> Enum.map(&List.to_tuple/1) |> List.to_tuple()
    for i <- 0..(m - k) do
      for j <- 0..(n - k) do
        vals = for r <- i..(i + k - 1), c <- j..(j + k - 1) do
          elem(elem(gv, r), c)
        end
        uv = Enum.uniq(vals) |> Enum.sort()
        if length(uv) < 2 do
          0
        else
          uv |> Enum.chunk_every(2, 1, :discard) |> Enum.map(fn [a, b] -> b - a end) |> Enum.min()
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

- **Time Complexity:** O((m - k + 1) * (n - k + 1) * k^2 * log(k^2)). There are (m - k + 1) * (n - k + 1) possible k by k submatrices. For each submatrix, we collect k^2 elements and sort them, taking O(k^2 log k^2) time. With m, n, k <= 30, the total number of operations is approximately 8 * 10^6, which fits comfortably within the time limit.
- **Space Complexity:** O(m * n). This includes the storage for the output result matrix and the temporary memory (O(k^2)) used to store and sort the elements of each submatrix during processing.
