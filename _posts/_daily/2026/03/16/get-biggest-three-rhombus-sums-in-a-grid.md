---
layout: post
title: "Get Biggest Three Rhombus Sums in a Grid"
date: 2026-03-16 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Math", "Sorting", "Heap (Priority Queue)", "Matrix", "Prefix Sum"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> getBiggestThree(vector<vector<int>>&\
        \ grid) {\n        int m = grid.size(), n = grid[0].size();\n        set<int>\
        \ distinctSums;\n        for (int r = 0; r < m; ++r) {\n            for (int\
        \ c = 0; c < n; ++c) {\n                distinctSums.insert(grid[r][c]);\n \
        \               for (int L = 1; ; ++L) {\n                    int r_top = r\
        \ - L, r_bottom = r + L;\n                    int c_left = c - L, c_right =\
        \ c + L;\n                    if (r_top < 0 || r_bottom >= m || c_left < 0 ||\
        \ c_right >= n) break;\n                    int currentSum = 0;\n          \
        \          for (int i = 0; i < L; ++i) {\n                        currentSum\
        \ += grid[r_top + i][c + i];\n                        currentSum += grid[r +\
        \ i][c_right - i];\n                        currentSum += grid[r_bottom - i][c\
        \ - i];\n                        currentSum += grid[r - i][c_left + i];\n  \
        \                  }\n                    distinctSums.insert(currentSum);\n\
        \                }\n            }\n        }\n        vector<int> result(distinctSums.rbegin(),\
        \ distinctSums.rend());\n        if (result.size() > 3) result.resize(3);\n\
        \        return result;\n    }\n};"
      java: "class Solution {\n    public int[] getBiggestThree(int[][] grid) {\n  \
        \      int m = grid.length, n = grid[0].length;\n        TreeSet<Integer> distinctSums\
        \ = new TreeSet<>();\n        for (int r = 0; r < m; r++) {\n            for\
        \ (int c = 0; c < n; c++) {\n                distinctSums.add(grid[r][c]);\n\
        \                for (int L = 1; ; L++) {\n                    int rt = r -\
        \ L, rb = r + L, cl = c - L, cr = c + L;\n                    if (rt < 0 ||\
        \ rb >= m || cl < 0 || cr >= n) break;\n                    int currentSum =\
        \ 0;\n                    for (int i = 0; i < L; i++) {\n                  \
        \      currentSum += grid[rt + i][c + i];\n                        currentSum\
        \ += grid[r + i][cr - i];\n                        currentSum += grid[rb - i][c\
        \ - i];\n                        currentSum += grid[r - i][cl + i];\n      \
        \              }\n                    distinctSums.add(currentSum);\n      \
        \          }\n            }\n        }\n        return distinctSums.descendingSet().stream().limit(3).mapToInt(i\
        \ -> i).toArray();\n    }\n}"
      python: "class Solution(object):\n    def getBiggestThree(self, grid):\n     \
        \   \"\"\"\n        :type grid: List[List[int]]\n        :rtype: List[int]\n\
        \        \"\"\"\n        m, n = len(grid), len(grid[0])\n        distinct_sums\
        \ = set()\n        for r in range(m):\n            for c in range(n):\n    \
        \            distinct_sums.add(grid[r][c])\n                for L in range(1,\
        \ 51):\n                    rt, rb, cl, cr = r - L, r + L, c - L, c + L\n  \
        \                  if rt < 0 or rb >= m or cl < 0 or cr >= n:\n            \
        \            break\n                    curr_sum = 0\n                    for\
        \ i in range(L):\n                        curr_sum += grid[rt + i][c + i]\n\
        \                        curr_sum += grid[r + i][cr - i]\n                 \
        \       curr_sum += grid[rb - i][c - i]\n                        curr_sum +=\
        \ grid[r - i][cl + i]\n                    distinct_sums.add(curr_sum)\n   \
        \     return sorted(list(distinct_sums), reverse=True)[:3]"
      python3: "class Solution:\n    def getBiggestThree(self, grid: List[List[int]])\
        \ -> List[int]:\n        m, n = len(grid), len(grid[0])\n        distinct_sums\
        \ = set()\n        for r in range(m):\n            for c in range(n):\n    \
        \            distinct_sums.add(grid[r][c])\n                for L in range(1,\
        \ 51):\n                    rt, rb, cl, cr = r - L, r + L, c - L, c + L\n  \
        \                  if rt < 0 or rb >= m or cl < 0 or cr >= n:\n            \
        \            break\n                    curr_sum = 0\n                    for\
        \ i in range(L):\n                        curr_sum += grid[rt + i][c + i]\n\
        \                        curr_sum += grid[r + i][cr - i]\n                 \
        \       curr_sum += grid[rb - i][c - i]\n                        curr_sum +=\
        \ grid[r - i][cl + i]\n                    distinct_sums.add(curr_sum)\n   \
        \     return sorted(list(distinct_sums), reverse=True)[:3]"
      c: "#include <stdlib.h>\n#include <string.h>\n\nint compare(const void *a, const\
        \ void *b) {\n    int arg1 = *(const int*)a;\n    int arg2 = *(const int*)b;\n\
        \    if (arg1 < arg2) return 1;\n    if (arg1 > arg2) return -1;\n    return\
        \ 0;\n}\n\nint* getBiggestThree(int** grid, int gridSize, int* gridColSize,\
        \ int* returnSize) {\n    int m = gridSize, n = gridColSize[0];\n    int* allSums\
        \ = (int*)malloc(62500 * sizeof(int));\n    int count = 0;\n    for (int r =\
        \ 0; r < m; r++) {\n        for (int c = 0; c < n; c++) {\n            allSums[count++]\
        \ = grid[r][c];\n            for (int L = 1; ; L++) {\n                int rt\
        \ = r - L, rb = r + L, cl = c - L, cr = c + L;\n                if (rt < 0 ||\
        \ rb >= m || cl < 0 || cr >= n) break;\n                int currentSum = 0;\n\
        \                for (int i = 0; i < L; i++) {\n                    currentSum\
        \ += grid[rt + i][c + i];\n                    currentSum += grid[r + i][cr\
        \ - i];\n                    currentSum += grid[rb - i][c - i];\n          \
        \          currentSum += grid[r - i][cl + i];\n                }\n         \
        \       allSums[count++] = currentSum;\n            }\n        }\n    }\n  \
        \  qsort(allSums, count, sizeof(int), compare);\n    int* result = (int*)malloc(3\
        \ * sizeof(int));\n    int uniqueCount = 0;\n    for (int i = 0; i < count &&\
        \ uniqueCount < 3; i++) {\n        if (i == 0 || allSums[i] != allSums[i - 1])\
        \ {\n            result[uniqueCount++] = allSums[i];\n        }\n    }\n   \
        \ free(allSums);\n    *returnSize = uniqueCount;\n    return result;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\nusing System.Linq;\n\
        \npublic class Solution {\n    public int[] GetBiggestThree(int[][] grid) {\n\
        \        int m = grid.Length, n = grid[0].Length;\n        HashSet<int> distinctSums\
        \ = new HashSet<int>();\n        for (int r = 0; r < m; r++) {\n           \
        \ for (int c = 0; c < n; c++) {\n                distinctSums.Add(grid[r][c]);\n\
        \                for (int L = 1; ; L++) {\n                    int rt = r -\
        \ L, rb = r + L, cl = c - L, cr = c + L;\n                    if (rt < 0 ||\
        \ rb >= m || cl < 0 || cr >= n) break;\n                    int currentSum =\
        \ 0;\n                    for (int i = 0; i < L; i++) {\n                  \
        \      currentSum += grid[rt + i][c + i];\n                        currentSum\
        \ += grid[r + i][cr - i];\n                        currentSum += grid[rb - i][c\
        \ - i];\n                        currentSum += grid[r - i][cl + i];\n      \
        \              }\n                    distinctSums.Add(currentSum);\n      \
        \          }\n            }\n        }\n        return distinctSums.OrderByDescending(x\
        \ => x).Take(3).ToArray();\n    }\n}"
      javascript: "/**\n * @param {number[][]} grid\n * @return {number[]}\n */\nvar\
        \ getBiggestThree = function(grid) {\n    const m = grid.length, n = grid[0].length;\n\
        \    const distinctSums = new Set();\n    for (let r = 0; r < m; r++) {\n  \
        \      for (let c = 0; c < n; c++) {\n            distinctSums.add(grid[r][c]);\n\
        \            for (let L = 1; ; L++) {\n                const rt = r - L, rb\
        \ = r + L, cl = c - L, cr = c + L;\n                if (rt < 0 || rb >= m ||\
        \ cl < 0 || cr >= n) break;\n                let currentSum = 0;\n         \
        \       for (let i = 0; i < L; i++) {\n                    currentSum += grid[rt\
        \ + i][c + i];\n                    currentSum += grid[r + i][cr - i];\n   \
        \                 currentSum += grid[rb - i][c - i];\n                    currentSum\
        \ += grid[r - i][cl + i];\n                }\n                distinctSums.add(currentSum);\n\
        \            }\n        }\n    }\n    return Array.from(distinctSums).sort((a,\
        \ b) => b - a).slice(0, 3);\n};"
      typescript: "function getBiggestThree(grid: number[][]): number[] {\n    const\
        \ m = grid.length;\n    const n = grid[0].length;\n    const sums = new Set<number>();\n\
        \n    for (let r = 0; r < m; r++) {\n        for (let c = 0; c < n; c++) {\n\
        \            sums.add(grid[r][c]);\n            for (let k = 1; r + 2 * k <\
        \ m && c - k >= 0 && c + k < n; k++) {\n                let sum = grid[r][c]\
        \ + grid[r + 2 * k][c] + grid[r + k][c - k] + grid[r + k][c + k];\n        \
        \        for (let i = 1; i < k; i++) {\n                    sum += grid[r +\
        \ i][c - i] + grid[r + i][c + i] + grid[r + 2 * k - i][c - i] + grid[r + 2 *\
        \ k - i][c + i];\n                }\n                sums.add(sum);\n      \
        \      }\n        }\n    }\n\n    return Array.from(sums).sort((a, b) => b -\
        \ a).slice(0, 3);\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $grid\n     * @return\
        \ Integer[]\n     */\n    function getBiggestThree($grid) {\n        $m = count($grid);\n\
        \        $n = count($grid[0]);\n        $sums = [];\n\n        for ($r = 0;\
        \ $r < $m; $r++) {\n            for ($c = 0; $c < $n; $c++) {\n            \
        \    $sums[$grid[$r][$c]] = true;\n                for ($k = 1; ; $k++) {\n\
        \                    if ($r + 2 * $k >= $m || $c - $k < 0 || $c + $k >= $n)\
        \ break;\n                    $sum = $grid[$r][$c] + $grid[$r + 2 * $k][$c]\
        \ + $grid[$r + $k][$c - $k] + $grid[$r + $k][$c + $k];\n                   \
        \ for ($i = 1; $i < $k; $i++) {\n                        $sum += $grid[$r +\
        \ $i][$c - $i] + $grid[$r + $i][$c + $i] + $grid[$r + 2 * $k - $i][$c - $i]\
        \ + $grid[$r + 2 * $k - $i][$c + $i];\n                    }\n             \
        \       $sums[$sum] = true;\n                }\n            }\n        }\n\n\
        \        $result = array_keys($sums);\n        rsort($result);\n        return\
        \ array_slice($result, 0, 3);\n    }\n}"
      swift: "class Solution {\n    func getBiggestThree(_ grid: [[Int]]) -> [Int] {\n\
        \        let m = grid.count\n        let n = grid[0].count\n        var sums\
        \ = Set<Int>()\n\n        for r in 0..<m {\n            for c in 0..<n {\n \
        \               sums.insert(grid[r][c])\n                var k = 1\n       \
        \         while r + 2 * k < m && c - k >= 0 && c + k < n {\n               \
        \     var sum = grid[r][c] + grid[r + 2 * k][c] + grid[r + k][c - k] + grid[r\
        \ + k][c + k]\n                    for i in 1..<k {\n                      \
        \  sum += grid[r + i][c - i] + grid[r + i][c + i] + grid[r + 2 * k - i][c -\
        \ i] + grid[r + 2 * k - i][c + i]\n                    }\n                 \
        \   sums.insert(sum)\n                    k += 1\n                }\n      \
        \      }\n        }\n\n        return Array(sums.sorted(by: >).prefix(3))\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun getBiggestThree(grid: Array<IntArray>): IntArray\
        \ {\n        val m = grid.size\n        val n = grid[0].size\n        val sums\
        \ = mutableSetOf<Int>()\n\n        for (r in 0 until m) {\n            for (c\
        \ in 0 until n) {\n                sums.add(grid[r][c])\n                var\
        \ k = 1\n                while (r + 2 * k < m && c - k >= 0 && c + k < n) {\n\
        \                    var sum = grid[r][c] + grid[r + 2 * k][c] + grid[r + k][c\
        \ - k] + grid[r + k][c + k]\n                    for (i in 1 until k) {\n  \
        \                      sum += grid[r + i][c - i] + grid[r + i][c + i] + grid[r\
        \ + 2 * k - i][c - i] + grid[r + 2 * k - i][c + i]\n                    }\n\
        \                    sums.add(sum)\n                    k++\n              \
        \  }\n            }\n        }\n\n        return sums.toList().sortedDescending().take(3).toIntArray()\n\
        \    }\n}"
      dart: "class Solution {\n  List<int> getBiggestThree(List<List<int>> grid) {\n\
        \    final m = grid.length;\n    final n = grid[0].length;\n    final sums =\
        \ <int>{};\n\n    for (var r = 0; r < m; r++) {\n      for (var c = 0; c < n;\
        \ c++) {\n        sums.add(grid[r][c]);\n        for (var k = 1; r + 2 * k <\
        \ m && c - k >= 0 && c + k < n; k++) {\n          var sum = grid[r][c] + grid[r\
        \ + 2 * k][c] + grid[r + k][c - k] + grid[r + k][c + k];\n          for (var\
        \ i = 1; i < k; i++) {\n            sum += grid[r + i][c - i] + grid[r + i][c\
        \ + i] + grid[r + 2 * k - i][c - i] + grid[r + 2 * k - i][c + i];\n        \
        \  }\n          sums.add(sum);\n        }\n      }\n    }\n\n    final result\
        \ = sums.toList()..sort((a, b) => b.compareTo(a));\n    return result.take(3).toList();\n\
        \  }\n}"
      go: "import (\n    \"sort\"\n)\n\nfunc getBiggestThree(grid [][]int) []int {\n\
        \    m := len(grid)\n    n := len(grid[0])\n    sumsMap := make(map[int]bool)\n\
        \n    for r := 0; r < m; r++ {\n        for c := 0; c < n; c++ {\n         \
        \   sumsMap[grid[r][c]] = true\n            for k := 1; r+2*k < m && c-k >=\
        \ 0 && c+k < n; k++ {\n                sum := grid[r][c] + grid[r+2*k][c] +\
        \ grid[r+k][c-k] + grid[r+k][c+k]\n                for i := 1; i < k; i++ {\n\
        \                    sum += grid[r+i][c-i] + grid[r+i][c+i] + grid[r+2*k-i][c-i]\
        \ + grid[r+2*k-i][c+i]\n                }\n                sumsMap[sum] = true\n\
        \            }\n        }\n    }\n\n    var res []int\n    for s := range sumsMap\
        \ {\n        res = append(res, s)\n    }\n    sort.Slice(res, func(i, j int)\
        \ bool {\n        return res[i] > res[j]\n    })\n\n    if len(res) > 3 {\n\
        \        return res[:3]\n    }\n    return res\n}"
      ruby: "require 'set'\n\ndef get_biggest_three(grid)\n  m = grid.length\n  n =\
        \ grid[0].length\n  sums = Set.new\n  (0...m).each do |r|\n    (0...n).each\
        \ do |c|\n      sums.add(grid[r][c])\n      (1...m).each do |s|\n        break\
        \ if r + 2 * s >= m || c - s < 0 || c + s >= n\n        val = grid[r][c] + grid[r\
        \ + 2 * s][c] + grid[r + s][c - s] + grid[r + s][c + s]\n        (1...s).each\
        \ do |i|\n          val += grid[r + i][c + i]\n          val += grid[r + s +\
        \ i][c + s - i]\n          val += grid[r + 2 * s - i][c - i]\n          val\
        \ += grid[r + s - i][c - s + i]\n        end\n        sums.add(val)\n      end\n\
        \    end\n  end\n  sums.to_a.sort.reverse.take(3)\nend"
      scala: "import scala.collection.mutable.Set\n\nobject Solution {\n    def getBiggestThree(grid:\
        \ Array[Array[Int]]): Array[Int] = {\n        val m = grid.length\n        val\
        \ n = grid(0).length\n        val sums = Set[Int]()\n        for (r <- 0 until\
        \ m; c <- 0 until n) {\n            sums += grid(r)(c)\n            var s =\
        \ 1\n            while (r + 2 * s < m && c - s >= 0 && c + s < n) {\n      \
        \          var currentSum = grid(r)(c) + grid(r + 2 * s)(c) + grid(r + s)(c\
        \ - s) + grid(r + s)(c + s)\n                for (i <- 1 until s) {\n      \
        \              currentSum += grid(r + i)(c + i)\n                    currentSum\
        \ += grid(r + s + i)(c + s - i)\n                    currentSum += grid(r +\
        \ 2 * s - i)(c - i)\n                    currentSum += grid(r + s - i)(c - s\
        \ + i)\n                }\n                sums += currentSum\n            \
        \    s += 1\n            }\n        }\n        sums.toArray.sorted(Ordering.Int.reverse).take(3)\n\
        \    }\n}"
      rust: "use std::collections::BTreeSet;\n\nimpl Solution {\n    pub fn get_biggest_three(grid:\
        \ Vec<Vec<i32>>) -> Vec<i32> {\n        let m = grid.len();\n        let n =\
        \ grid[0].len();\n        let mut sums = BTreeSet::new();\n        for r in\
        \ 0..m {\n            for c in 0..n {\n                sums.insert(grid[r][c]);\n\
        \                let mut s = 1;\n                while r + 2 * s < m && c >=\
        \ s && c + s < n {\n                    let mut current_sum = grid[r][c] + grid[r\
        \ + 2 * s][c] + grid[r + s][c - s] + grid[r + s][c + s];\n                 \
        \   for i in 1..s {\n                        current_sum += grid[r + i][c +\
        \ i];\n                        current_sum += grid[r + s + i][c + s - i];\n\
        \                        current_sum += grid[r + 2 * s - i][c - i];\n      \
        \                  current_sum += grid[r + s - i][c - s + i];\n            \
        \        }\n                    sums.insert(current_sum);\n                \
        \    s += 1;\n                }\n            }\n        }\n        sums.into_iter().rev().take(3).collect()\n\
        \    }\n}"
      racket: "(require racket/set)\n\n(define/contract (get-biggest-three grid)\n \
        \ (-> (listof (listof exact-integer?)) (listof exact-integer?))\n  (let* ([m\
        \ (length grid)]\n         [n (length (car grid))]\n         [g (list->vector\
        \ (map list->vector grid))]\n         [sums (mutable-set)])\n    (for ([r (in-range\
        \ m)])\n      (for ([c (in-range n)])\n        (set-add! sums (vector-ref (vector-ref\
        \ g r) c))\n        (for ([s (in-range 1 m)])\n          #:break (or (>= (+\
        \ r (* 2 s)) m) (< c s) (>= (+ c s) n))\n          (let* ([v1 (vector-ref (vector-ref\
        \ g r) c)]\n                 [v2 (vector-ref (vector-ref g (+ r (* 2 s))) c)]\n\
        \                 [v3 (vector-ref (vector-ref g (+ r s)) (- c s))]\n       \
        \          [v4 (vector-ref (vector-ref g (+ r s)) (+ c s))]\n              \
        \   [curr-sum (+ v1 v2 v3 v4)])\n            (set-add! sums\n              \
        \        (for/fold ([acc curr-sum])\n                                ([i (in-range\
        \ 1 s)])\n                        (+ acc\n                           (vector-ref\
        \ (vector-ref g (+ r i)) (+ c i))\n                           (vector-ref (vector-ref\
        \ g (+ r s i)) (+ c s (- i)))\n                           (vector-ref (vector-ref\
        \ g (+ r (* 2 s) (- i))) (- c i))\n                           (vector-ref (vector-ref\
        \ g (+ r s (- i))) (- c s i)))))))))\n    (let ([sorted (sort (set->list sums)\
        \ >)])\n      (take sorted (min (length sorted) 3)))))"
      erlang: "get_biggest_three(Grid) ->\n  M = length(Grid),\n  N = length(hd(Grid)),\n\
        \  GridMap = maps:from_list([{{R, C}, Val} || {R, Row} <- lists:zip(lists:seq(0,\
        \ M-1), Grid), {C, Val} <- lists:zip(lists:seq(0, N-1), Row)]),\n  AllSums =\
        \ lists:foldl(fn(R, AccR) ->\n    lists:foldl(fn(C, AccC) ->\n      Val0 = maps:get({R,\
        \ C}, GridMap),\n      CurrentSums = lists:foldl(fn(S, AccS) ->\n        case\
        \ (R + 2*S < M) andalso (C - S >= 0) andalso (C + S < N) of\n          true\
        \ ->\n            V1 = maps:get({R, C}, GridMap),\n            V2 = maps:get({R\
        \ + 2*S, C}, GridMap),\n            V3 = maps:get({R + S, C - S}, GridMap),\n\
        \            V4 = maps:get({R + S, C + S}, GridMap),\n            VerticesSum\
        \ = V1 + V2 + V3 + V4,\n            Sum = lists:foldl(fn(I, AccI) ->\n     \
        \         AccI + maps:get({R+I, C+I}, GridMap)\n                   + maps:get({R+S+I,\
        \ C+S-I}, GridMap)\n                   + maps:get({R+2*S-I, C-I}, GridMap)\n\
        \                   + maps:get({R+S-I, C-S+I}, GridMap)\n            end, VerticesSum,\
        \ if S > 1 -> lists:seq(1, S-1); true -> [] end),\n            [Sum | AccS];\n\
        \          false ->\n            AccS\n        end\n      end, [Val0], lists:seq(1,\
        \ (M-1) div 2)),\n      CurrentSums ++ AccC\n    end, AccR, lists:seq(0, N-1))\n\
        \  end, [], lists:seq(0, M-1)),\n  SortedUnique = lists:reverse(lists:usort(AllSums)),\n\
        \  lists:sublist(SortedUnique, 3)."
      elixir: "defmodule Solution do\n  @spec get_biggest_three(grid :: [[integer]])\
        \ :: [integer]\n  def get_biggest_three(grid) do\n    m = length(grid)\n   \
        \ n = length(hd(grid))\n    grid_map = for {row, r} <- Enum.with_index(grid),\
        \ {val, c} <- Enum.with_index(row), into: %{}, do: {{r, c}, val}\n    sums =\
        \ for r <- 0..(m-1), c <- 0..(n-1), reduce: MapSet.new() do\n      acc ->\n\
        \        acc = MapSet.put(acc, Map.get(grid_map, {r, c}))\n        max_s = min(div(m\
        \ - 1 - r, 2), min(c, n - 1 - c))\n        if max_s >= 1 do\n          Enum.reduce(1..max_s,\
        \ acc, fn s, acc_s ->\n            v1 = Map.get(grid_map, {r, c})\n        \
        \    v2 = Map.get(grid_map, {r + 2 * s, c})\n            v3 = Map.get(grid_map,\
        \ {r + s, c - s})\n            v4 = Map.get(grid_map, {r + s, c + s})\n    \
        \        vertices_sum = v1 + v2 + v3 + v4\n            sum = if s > 1 do\n \
        \             Enum.reduce(1..(s - 1), vertices_sum, fn i, acc_i ->\n       \
        \         acc_i + Map.get(grid_map, {r + i, c + i}) + Map.get(grid_map, {r +\
        \ s + i, c + s - i}) +\n                  Map.get(grid_map, {r + 2 * s - i,\
        \ c - i}) + Map.get(grid_map, {r + s - i, c - s + i})\n              end)\n\
        \            else\n              vertices_sum\n            end\n           \
        \ MapSet.put(acc_s, sum)\n          end)\n        else\n          acc\n    \
        \    end\n    end\n    sums |> MapSet.to_list() |> Enum.sort(:desc) |> Enum.take(3)\n\
        \  end\nend"
    approach: 'The algorithm iterates over every cell $(r, c)$ in the $m \times n$ grid
      to treat it as the center of a potential rhombus. For each center, we explore
      all possible side lengths $L \ge 0$ such that the four corners of the rhombus
      stay within the grid boundaries. For $L=0$, the rhombus sum is simply the value
      at $grid[r][c]$. For $L > 0$, the rhombus is defined by four corners: top $(r-L,
      c)$, bottom $(r+L, c)$, left $(r, c-L)$, and right $(r, c+L)$. The border sum
      is computed by summing the $4L$ cells along the segments connecting these corners.


      To ensure we return only the three largest distinct sums, we store every calculated
      rhombus sum in a set-like data structure. This handles the requirement for distinct
      values automatically. After checking all possible centers and side lengths, we
      sort the unique sums in descending order and return the top three (or all of them
      if fewer than three distinct sums exist). The small grid constraints ($m, n \le
      50$) allow this brute-force approach to run efficiently within the time limits.'
    time_complexity: O(m \cdot n \cdot \min(m, n)^2). For each of the $m \times n$ cells,
      we iterate over $O(\min(m, n))$ possible side lengths. For each side length $L
      > 0$, we perform a traversal of $4L$ cells to calculate the border sum, leading
      to a complexity of $O(m \cdot n \cdot \min(m, n)^2)$. Sorting the resulting distinct
      sums takes $O(K \log K)$ where $K$ is the number of valid rhombuses.
    space_complexity: O(m \cdot n \cdot \min(m, n)). In the worst case, we store a distinct
      sum for every possible rhombus in the grid. The total number of rhombuses is approximately
      $O(m \cdot n \cdot \min(m, n))$, which dictates the space required for the collection
      of sums.
    elapsed_time: 255.97199487686157
    model: gemini-3-flash-preview
    generated_at: '2026-03-16 01:51:29 '
---

## Problem #1878: Get Biggest Three Rhombus Sums in a Grid

**Difficulty:** Medium

**Topics:** Array, Math, Sorting, Heap (Priority Queue), Matrix, Prefix Sum

## Problem Description

<p>You are given an <code>m x n</code> integer matrix <code>grid</code>​​​.</p>

<p>A <strong>rhombus sum</strong> is the sum of the elements that form <strong>the</strong> <strong>border</strong> of a regular rhombus shape in <code>grid</code>​​​. The rhombus must have the shape of a square rotated 45 degrees with each of the corners centered in a grid cell. Below is an image of four valid rhombus shapes with the corresponding colored cells that should be included in each <strong>rhombus sum</strong>:</p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/23/pc73-q4-desc-2.png" style="width: 385px; height: 385px;" />
<p>Note that the rhombus can have an area of 0, which is depicted by the purple rhombus in the bottom right corner.</p>

<p>Return <em>the biggest three <strong>distinct rhombus sums</strong> in the </em><code>grid</code><em> in <strong>descending order</strong></em><em>. If there are less than three distinct values, return all of them</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/23/pc73-q4-ex1.png" style="width: 360px; height: 361px;" />
<pre>
<strong>Input:</strong> grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
<strong>Output:</strong> [228,216,211]
<strong>Explanation:</strong> The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 20 + 3 + 200 + 5 = 228
- Red: 200 + 2 + 10 + 4 = 216
- Green: 5 + 200 + 4 + 2 = 211
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/23/pc73-q4-ex2.png" style="width: 217px; height: 217px;" />
<pre>
<strong>Input:</strong> grid = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:</strong> [20,9,8]
<strong>Explanation:</strong> The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 4 + 2 + 6 + 8 = 20
- Red: 9 (area 0 rhombus in the bottom right corner)
- Green: 8 (area 0 rhombus in the bottom middle)
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> grid = [[7,7,7]]
<strong>Output:</strong> [7]
<strong>Explanation:</strong> All three possible rhombus sums are the same, so return [7].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. You need to maintain only the biggest 3 distinct sums

2. The limits are small enough for you to iterate over all rhombus sizes then iterate over all possible borders to get the sums

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm iterates over every cell $(r, c)$ in the $m \times n$ grid to treat it as the center of a potential rhombus. For each center, we explore all possible side lengths $L \ge 0$ such that the four corners of the rhombus stay within the grid boundaries. For $L=0$, the rhombus sum is simply the value at $grid[r][c]$. For $L > 0$, the rhombus is defined by four corners: top $(r-L, c)$, bottom $(r+L, c)$, left $(r, c-L)$, and right $(r, c+L)$. The border sum is computed by summing the $4L$ cells along the segments connecting these corners.

To ensure we return only the three largest distinct sums, we store every calculated rhombus sum in a set-like data structure. This handles the requirement for distinct values automatically. After checking all possible centers and side lengths, we sort the unique sums in descending order and return the top three (or all of them if fewer than three distinct sums exist). The small grid constraints ($m, n \le 50$) allow this brute-force approach to run efficiently within the time limits.

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
    vector<int> getBiggestThree(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        set<int> distinctSums;
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                distinctSums.insert(grid[r][c]);
                for (int L = 1; ; ++L) {
                    int r_top = r - L, r_bottom = r + L;
                    int c_left = c - L, c_right = c + L;
                    if (r_top < 0 || r_bottom >= m || c_left < 0 || c_right >= n) break;
                    int currentSum = 0;
                    for (int i = 0; i < L; ++i) {
                        currentSum += grid[r_top + i][c + i];
                        currentSum += grid[r + i][c_right - i];
                        currentSum += grid[r_bottom - i][c - i];
                        currentSum += grid[r - i][c_left + i];
                    }
                    distinctSums.insert(currentSum);
                }
            }
        }
        vector<int> result(distinctSums.rbegin(), distinctSums.rend());
        if (result.size() > 3) result.resize(3);
        return result;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int[] getBiggestThree(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        TreeSet<Integer> distinctSums = new TreeSet<>();
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                distinctSums.add(grid[r][c]);
                for (int L = 1; ; L++) {
                    int rt = r - L, rb = r + L, cl = c - L, cr = c + L;
                    if (rt < 0 || rb >= m || cl < 0 || cr >= n) break;
                    int currentSum = 0;
                    for (int i = 0; i < L; i++) {
                        currentSum += grid[rt + i][c + i];
                        currentSum += grid[r + i][cr - i];
                        currentSum += grid[rb - i][c - i];
                        currentSum += grid[r - i][cl + i];
                    }
                    distinctSums.add(currentSum);
                }
            }
        }
        return distinctSums.descendingSet().stream().limit(3).mapToInt(i -> i).toArray();
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        distinct_sums = set()
        for r in range(m):
            for c in range(n):
                distinct_sums.add(grid[r][c])
                for L in range(1, 51):
                    rt, rb, cl, cr = r - L, r + L, c - L, c + L
                    if rt < 0 or rb >= m or cl < 0 or cr >= n:
                        break
                    curr_sum = 0
                    for i in range(L):
                        curr_sum += grid[rt + i][c + i]
                        curr_sum += grid[r + i][cr - i]
                        curr_sum += grid[rb - i][c - i]
                        curr_sum += grid[r - i][cl + i]
                    distinct_sums.add(curr_sum)
        return sorted(list(distinct_sums), reverse=True)[:3]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        distinct_sums = set()
        for r in range(m):
            for c in range(n):
                distinct_sums.add(grid[r][c])
                for L in range(1, 51):
                    rt, rb, cl, cr = r - L, r + L, c - L, c + L
                    if rt < 0 or rb >= m or cl < 0 or cr >= n:
                        break
                    curr_sum = 0
                    for i in range(L):
                        curr_sum += grid[rt + i][c + i]
                        curr_sum += grid[r + i][cr - i]
                        curr_sum += grid[rb - i][c - i]
                        curr_sum += grid[r - i][cl + i]
                    distinct_sums.add(curr_sum)
        return sorted(list(distinct_sums), reverse=True)[:3]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

int compare(const void *a, const void *b) {
    int arg1 = *(const int*)a;
    int arg2 = *(const int*)b;
    if (arg1 < arg2) return 1;
    if (arg1 > arg2) return -1;
    return 0;
}

int* getBiggestThree(int** grid, int gridSize, int* gridColSize, int* returnSize) {
    int m = gridSize, n = gridColSize[0];
    int* allSums = (int*)malloc(62500 * sizeof(int));
    int count = 0;
    for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
            allSums[count++] = grid[r][c];
            for (int L = 1; ; L++) {
                int rt = r - L, rb = r + L, cl = c - L, cr = c + L;
                if (rt < 0 || rb >= m || cl < 0 || cr >= n) break;
                int currentSum = 0;
                for (int i = 0; i < L; i++) {
                    currentSum += grid[rt + i][c + i];
                    currentSum += grid[r + i][cr - i];
                    currentSum += grid[rb - i][c - i];
                    currentSum += grid[r - i][cl + i];
                }
                allSums[count++] = currentSum;
            }
        }
    }
    qsort(allSums, count, sizeof(int), compare);
    int* result = (int*)malloc(3 * sizeof(int));
    int uniqueCount = 0;
    for (int i = 0; i < count && uniqueCount < 3; i++) {
        if (i == 0 || allSums[i] != allSums[i - 1]) {
            result[uniqueCount++] = allSums[i];
        }
    }
    free(allSums);
    *returnSize = uniqueCount;
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] GetBiggestThree(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        HashSet<int> distinctSums = new HashSet<int>();
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                distinctSums.Add(grid[r][c]);
                for (int L = 1; ; L++) {
                    int rt = r - L, rb = r + L, cl = c - L, cr = c + L;
                    if (rt < 0 || rb >= m || cl < 0 || cr >= n) break;
                    int currentSum = 0;
                    for (int i = 0; i < L; i++) {
                        currentSum += grid[rt + i][c + i];
                        currentSum += grid[r + i][cr - i];
                        currentSum += grid[rb - i][c - i];
                        currentSum += grid[r - i][cl + i];
                    }
                    distinctSums.Add(currentSum);
                }
            }
        }
        return distinctSums.OrderByDescending(x => x).Take(3).ToArray();
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
 * @return {number[]}
 */
var getBiggestThree = function(grid) {
    const m = grid.length, n = grid[0].length;
    const distinctSums = new Set();
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            distinctSums.add(grid[r][c]);
            for (let L = 1; ; L++) {
                const rt = r - L, rb = r + L, cl = c - L, cr = c + L;
                if (rt < 0 || rb >= m || cl < 0 || cr >= n) break;
                let currentSum = 0;
                for (let i = 0; i < L; i++) {
                    currentSum += grid[rt + i][c + i];
                    currentSum += grid[r + i][cr - i];
                    currentSum += grid[rb - i][c - i];
                    currentSum += grid[r - i][cl + i];
                }
                distinctSums.add(currentSum);
            }
        }
    }
    return Array.from(distinctSums).sort((a, b) => b - a).slice(0, 3);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function getBiggestThree(grid: number[][]): number[] {
    const m = grid.length;
    const n = grid[0].length;
    const sums = new Set<number>();

    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            sums.add(grid[r][c]);
            for (let k = 1; r + 2 * k < m && c - k >= 0 && c + k < n; k++) {
                let sum = grid[r][c] + grid[r + 2 * k][c] + grid[r + k][c - k] + grid[r + k][c + k];
                for (let i = 1; i < k; i++) {
                    sum += grid[r + i][c - i] + grid[r + i][c + i] + grid[r + 2 * k - i][c - i] + grid[r + 2 * k - i][c + i];
                }
                sums.add(sum);
            }
        }
    }

    return Array.from(sums).sort((a, b) => b - a).slice(0, 3);
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
     * @return Integer[]
     */
    function getBiggestThree($grid) {
        $m = count($grid);
        $n = count($grid[0]);
        $sums = [];

        for ($r = 0; $r < $m; $r++) {
            for ($c = 0; $c < $n; $c++) {
                $sums[$grid[$r][$c]] = true;
                for ($k = 1; ; $k++) {
                    if ($r + 2 * $k >= $m || $c - $k < 0 || $c + $k >= $n) break;
                    $sum = $grid[$r][$c] + $grid[$r + 2 * $k][$c] + $grid[$r + $k][$c - $k] + $grid[$r + $k][$c + $k];
                    for ($i = 1; $i < $k; $i++) {
                        $sum += $grid[$r + $i][$c - $i] + $grid[$r + $i][$c + $i] + $grid[$r + 2 * $k - $i][$c - $i] + $grid[$r + 2 * $k - $i][$c + $i];
                    }
                    $sums[$sum] = true;
                }
            }
        }

        $result = array_keys($sums);
        rsort($result);
        return array_slice($result, 0, 3);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func getBiggestThree(_ grid: [[Int]]) -> [Int] {
        let m = grid.count
        let n = grid[0].count
        var sums = Set<Int>()

        for r in 0..<m {
            for c in 0..<n {
                sums.insert(grid[r][c])
                var k = 1
                while r + 2 * k < m && c - k >= 0 && c + k < n {
                    var sum = grid[r][c] + grid[r + 2 * k][c] + grid[r + k][c - k] + grid[r + k][c + k]
                    for i in 1..<k {
                        sum += grid[r + i][c - i] + grid[r + i][c + i] + grid[r + 2 * k - i][c - i] + grid[r + 2 * k - i][c + i]
                    }
                    sums.insert(sum)
                    k += 1
                }
            }
        }

        return Array(sums.sorted(by: >).prefix(3))
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun getBiggestThree(grid: Array<IntArray>): IntArray {
        val m = grid.size
        val n = grid[0].size
        val sums = mutableSetOf<Int>()

        for (r in 0 until m) {
            for (c in 0 until n) {
                sums.add(grid[r][c])
                var k = 1
                while (r + 2 * k < m && c - k >= 0 && c + k < n) {
                    var sum = grid[r][c] + grid[r + 2 * k][c] + grid[r + k][c - k] + grid[r + k][c + k]
                    for (i in 1 until k) {
                        sum += grid[r + i][c - i] + grid[r + i][c + i] + grid[r + 2 * k - i][c - i] + grid[r + 2 * k - i][c + i]
                    }
                    sums.add(sum)
                    k++
                }
            }
        }

        return sums.toList().sortedDescending().take(3).toIntArray()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<int> getBiggestThree(List<List<int>> grid) {
    final m = grid.length;
    final n = grid[0].length;
    final sums = <int>{};

    for (var r = 0; r < m; r++) {
      for (var c = 0; c < n; c++) {
        sums.add(grid[r][c]);
        for (var k = 1; r + 2 * k < m && c - k >= 0 && c + k < n; k++) {
          var sum = grid[r][c] + grid[r + 2 * k][c] + grid[r + k][c - k] + grid[r + k][c + k];
          for (var i = 1; i < k; i++) {
            sum += grid[r + i][c - i] + grid[r + i][c + i] + grid[r + 2 * k - i][c - i] + grid[r + 2 * k - i][c + i];
          }
          sums.add(sum);
        }
      }
    }

    final result = sums.toList()..sort((a, b) => b.compareTo(a));
    return result.take(3).toList();
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

func getBiggestThree(grid [][]int) []int {
    m := len(grid)
    n := len(grid[0])
    sumsMap := make(map[int]bool)

    for r := 0; r < m; r++ {
        for c := 0; c < n; c++ {
            sumsMap[grid[r][c]] = true
            for k := 1; r+2*k < m && c-k >= 0 && c+k < n; k++ {
                sum := grid[r][c] + grid[r+2*k][c] + grid[r+k][c-k] + grid[r+k][c+k]
                for i := 1; i < k; i++ {
                    sum += grid[r+i][c-i] + grid[r+i][c+i] + grid[r+2*k-i][c-i] + grid[r+2*k-i][c+i]
                }
                sumsMap[sum] = true
            }
        }
    }

    var res []int
    for s := range sumsMap {
        res = append(res, s)
    }
    sort.Slice(res, func(i, j int) bool {
        return res[i] > res[j]
    })

    if len(res) > 3 {
        return res[:3]
    }
    return res
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
require 'set'

def get_biggest_three(grid)
  m = grid.length
  n = grid[0].length
  sums = Set.new
  (0...m).each do |r|
    (0...n).each do |c|
      sums.add(grid[r][c])
      (1...m).each do |s|
        break if r + 2 * s >= m || c - s < 0 || c + s >= n
        val = grid[r][c] + grid[r + 2 * s][c] + grid[r + s][c - s] + grid[r + s][c + s]
        (1...s).each do |i|
          val += grid[r + i][c + i]
          val += grid[r + s + i][c + s - i]
          val += grid[r + 2 * s - i][c - i]
          val += grid[r + s - i][c - s + i]
        end
        sums.add(val)
      end
    end
  end
  sums.to_a.sort.reverse.take(3)
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable.Set

object Solution {
    def getBiggestThree(grid: Array[Array[Int]]): Array[Int] = {
        val m = grid.length
        val n = grid(0).length
        val sums = Set[Int]()
        for (r <- 0 until m; c <- 0 until n) {
            sums += grid(r)(c)
            var s = 1
            while (r + 2 * s < m && c - s >= 0 && c + s < n) {
                var currentSum = grid(r)(c) + grid(r + 2 * s)(c) + grid(r + s)(c - s) + grid(r + s)(c + s)
                for (i <- 1 until s) {
                    currentSum += grid(r + i)(c + i)
                    currentSum += grid(r + s + i)(c + s - i)
                    currentSum += grid(r + 2 * s - i)(c - i)
                    currentSum += grid(r + s - i)(c - s + i)
                }
                sums += currentSum
                s += 1
            }
        }
        sums.toArray.sorted(Ordering.Int.reverse).take(3)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::BTreeSet;

impl Solution {
    pub fn get_biggest_three(grid: Vec<Vec<i32>>) -> Vec<i32> {
        let m = grid.len();
        let n = grid[0].len();
        let mut sums = BTreeSet::new();
        for r in 0..m {
            for c in 0..n {
                sums.insert(grid[r][c]);
                let mut s = 1;
                while r + 2 * s < m && c >= s && c + s < n {
                    let mut current_sum = grid[r][c] + grid[r + 2 * s][c] + grid[r + s][c - s] + grid[r + s][c + s];
                    for i in 1..s {
                        current_sum += grid[r + i][c + i];
                        current_sum += grid[r + s + i][c + s - i];
                        current_sum += grid[r + 2 * s - i][c - i];
                        current_sum += grid[r + s - i][c - s + i];
                    }
                    sums.insert(current_sum);
                    s += 1;
                }
            }
        }
        sums.into_iter().rev().take(3).collect()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(require racket/set)

(define/contract (get-biggest-three grid)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ([m (length grid)]
         [n (length (car grid))]
         [g (list->vector (map list->vector grid))]
         [sums (mutable-set)])
    (for ([r (in-range m)])
      (for ([c (in-range n)])
        (set-add! sums (vector-ref (vector-ref g r) c))
        (for ([s (in-range 1 m)])
          #:break (or (>= (+ r (* 2 s)) m) (< c s) (>= (+ c s) n))
          (let* ([v1 (vector-ref (vector-ref g r) c)]
                 [v2 (vector-ref (vector-ref g (+ r (* 2 s))) c)]
                 [v3 (vector-ref (vector-ref g (+ r s)) (- c s))]
                 [v4 (vector-ref (vector-ref g (+ r s)) (+ c s))]
                 [curr-sum (+ v1 v2 v3 v4)])
            (set-add! sums
                      (for/fold ([acc curr-sum])
                                ([i (in-range 1 s)])
                        (+ acc
                           (vector-ref (vector-ref g (+ r i)) (+ c i))
                           (vector-ref (vector-ref g (+ r s i)) (+ c s (- i)))
                           (vector-ref (vector-ref g (+ r (* 2 s) (- i))) (- c i))
                           (vector-ref (vector-ref g (+ r s (- i))) (- c s i)))))))))
    (let ([sorted (sort (set->list sums) >)])
      (take sorted (min (length sorted) 3)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
get_biggest_three(Grid) ->
  M = length(Grid),
  N = length(hd(Grid)),
  GridMap = maps:from_list([{{R, C}, Val} || {R, Row} <- lists:zip(lists:seq(0, M-1), Grid), {C, Val} <- lists:zip(lists:seq(0, N-1), Row)]),
  AllSums = lists:foldl(fn(R, AccR) ->
    lists:foldl(fn(C, AccC) ->
      Val0 = maps:get({R, C}, GridMap),
      CurrentSums = lists:foldl(fn(S, AccS) ->
        case (R + 2*S < M) andalso (C - S >= 0) andalso (C + S < N) of
          true ->
            V1 = maps:get({R, C}, GridMap),
            V2 = maps:get({R + 2*S, C}, GridMap),
            V3 = maps:get({R + S, C - S}, GridMap),
            V4 = maps:get({R + S, C + S}, GridMap),
            VerticesSum = V1 + V2 + V3 + V4,
            Sum = lists:foldl(fn(I, AccI) ->
              AccI + maps:get({R+I, C+I}, GridMap)
                   + maps:get({R+S+I, C+S-I}, GridMap)
                   + maps:get({R+2*S-I, C-I}, GridMap)
                   + maps:get({R+S-I, C-S+I}, GridMap)
            end, VerticesSum, if S > 1 -> lists:seq(1, S-1); true -> [] end),
            [Sum | AccS];
          false ->
            AccS
        end
      end, [Val0], lists:seq(1, (M-1) div 2)),
      CurrentSums ++ AccC
    end, AccR, lists:seq(0, N-1))
  end, [], lists:seq(0, M-1)),
  SortedUnique = lists:reverse(lists:usort(AllSums)),
  lists:sublist(SortedUnique, 3).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec get_biggest_three(grid :: [[integer]]) :: [integer]
  def get_biggest_three(grid) do
    m = length(grid)
    n = length(hd(grid))
    grid_map = for {row, r} <- Enum.with_index(grid), {val, c} <- Enum.with_index(row), into: %{}, do: {{r, c}, val}
    sums = for r <- 0..(m-1), c <- 0..(n-1), reduce: MapSet.new() do
      acc ->
        acc = MapSet.put(acc, Map.get(grid_map, {r, c}))
        max_s = min(div(m - 1 - r, 2), min(c, n - 1 - c))
        if max_s >= 1 do
          Enum.reduce(1..max_s, acc, fn s, acc_s ->
            v1 = Map.get(grid_map, {r, c})
            v2 = Map.get(grid_map, {r + 2 * s, c})
            v3 = Map.get(grid_map, {r + s, c - s})
            v4 = Map.get(grid_map, {r + s, c + s})
            vertices_sum = v1 + v2 + v3 + v4
            sum = if s > 1 do
              Enum.reduce(1..(s - 1), vertices_sum, fn i, acc_i ->
                acc_i + Map.get(grid_map, {r + i, c + i}) + Map.get(grid_map, {r + s + i, c + s - i}) +
                  Map.get(grid_map, {r + 2 * s - i, c - i}) + Map.get(grid_map, {r + s - i, c - s + i})
              end)
            else
              vertices_sum
            end
            MapSet.put(acc_s, sum)
          end)
        else
          acc
        end
    end
    sums |> MapSet.to_list() |> Enum.sort(:desc) |> Enum.take(3)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(m \cdot n \cdot \min(m, n)^2). For each of the $m \times n$ cells, we iterate over $O(\min(m, n))$ possible side lengths. For each side length $L > 0$, we perform a traversal of $4L$ cells to calculate the border sum, leading to a complexity of $O(m \cdot n \cdot \min(m, n)^2)$. Sorting the resulting distinct sums takes $O(K \log K)$ where $K$ is the number of valid rhombuses.
- **Space Complexity:** O(m \cdot n \cdot \min(m, n)). In the worst case, we store a distinct sum for every possible rhombus in the grid. The total number of rhombuses is approximately $O(m \cdot n \cdot \min(m, n))$, which dictates the space required for the collection of sums.
