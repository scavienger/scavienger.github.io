---
layout: post
title: "Minimum Swaps to Arrange a Binary Grid"
date: 2026-03-02 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Greedy", "Matrix"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minSwaps(vector<vector<int>>& grid) {\n\
        \        int n = grid.size();\n        vector<int> t(n);\n        for (int i\
        \ = 0; i < n; i++) {\n            int count = 0;\n            for (int j = n\
        \ - 1; j >= 0; j--) {\n                if (grid[i][j] == 0) count++;\n     \
        \           else break;\n            }\n            t[i] = count;\n        }\n\
        \n        int swaps = 0;\n        for (int i = 0; i < n; i++) {\n          \
        \  int target = n - 1 - i;\n            int found = -1;\n            for (int\
        \ j = i; j < n; j++) {\n                if (t[j] >= target) {\n            \
        \        found = j;\n                    break;\n                }\n       \
        \     }\n            if (found == -1) return -1;\n            swaps += (found\
        \ - i);\n            int val = t[found];\n            for (int k = found; k\
        \ > i; k--) {\n                t[k] = t[k - 1];\n            }\n           \
        \ t[i] = val;\n        }\n        return swaps;\n    }\n};"
      java: "class Solution {\n    public int minSwaps(int[][] grid) {\n        int\
        \ n = grid.length;\n        int[] t = new int[n];\n        for (int i = 0; i\
        \ < n; i++) {\n            int count = 0;\n            for (int j = n - 1; j\
        \ >= 0; j--) {\n                if (grid[i][j] == 0) count++;\n            \
        \    else break;\n            }\n            t[i] = count;\n        }\n\n  \
        \      int swaps = 0;\n        for (int i = 0; i < n; i++) {\n            int\
        \ target = n - 1 - i;\n            int found = -1;\n            for (int j =\
        \ i; j < n; j++) {\n                if (t[j] >= target) {\n                \
        \    found = j;\n                    break;\n                }\n           \
        \ }\n            if (found == -1) return -1;\n            swaps += (found -\
        \ i);\n            int val = t[found];\n            for (int k = found; k >\
        \ i; k--) {\n                t[k] = t[k - 1];\n            }\n            t[i]\
        \ = val;\n        }\n        return swaps;\n    }\n}"
      python: "class Solution(object):\n    def minSwaps(self, grid):\n        \"\"\"\
        \n        :type grid: List[List[int]]\n        :rtype: int\n        \"\"\"\n\
        \        n = len(grid)\n        t = []\n        for i in range(n):\n       \
        \     count = 0\n            for j in range(n - 1, -1, -1):\n              \
        \  if grid[i][j] == 0:\n                    count += 1\n                else:\n\
        \                    break\n            t.append(count)\n\n        swaps = 0\n\
        \        for i in range(n):\n            target = n - 1 - i\n            found\
        \ = -1\n            for j in range(i, n):\n                if t[j] >= target:\n\
        \                    found = j\n                    break\n            if found\
        \ == -1:\n                return -1\n            swaps += (found - i)\n    \
        \        val = t.pop(found)\n            t.insert(i, val)\n        return swaps"
      python3: "class Solution:\n    def minSwaps(self, grid: List[List[int]]) -> int:\n\
        \        n = len(grid)\n        t = []\n        for row in grid:\n         \
        \   count = 0\n            for j in range(n - 1, -1, -1):\n                if\
        \ row[j] == 0:\n                    count += 1\n                else:\n    \
        \                break\n            t.append(count)\n\n        swaps = 0\n \
        \       for i in range(n):\n            target = n - 1 - i\n            found\
        \ = -1\n            for j in range(i, n):\n                if t[j] >= target:\n\
        \                    found = j\n                    break\n            if found\
        \ == -1:\n                return -1\n            swaps += (found - i)\n    \
        \        val = t.pop(found)\n            t.insert(i, val)\n        return swaps"
      c: "int minSwaps(int** grid, int gridSize, int* gridColSize) {\n    int n = gridSize;\n\
        \    int t[n];\n    for (int i = 0; i < n; i++) {\n        int count = 0;\n\
        \        for (int j = n - 1; j >= 0; j--) {\n            if (grid[i][j] == 0)\
        \ count++;\n            else break;\n        }\n        t[i] = count;\n    }\n\
        \n    int swaps = 0;\n    for (int i = 0; i < n; i++) {\n        int target\
        \ = n - 1 - i;\n        int found = -1;\n        for (int j = i; j < n; j++)\
        \ {\n            if (t[j] >= target) {\n                found = j;\n       \
        \         break;\n            }\n        }\n        if (found == -1) return\
        \ -1;\n        swaps += (found - i);\n        int val = t[found];\n        for\
        \ (int k = found; k > i; k--) {\n            t[k] = t[k - 1];\n        }\n \
        \       t[i] = val;\n    }\n    return swaps;\n}"
      csharp: "public class Solution {\n    public int MinSwaps(int[][] grid) {\n  \
        \      int n = grid.Length;\n        int[] t = new int[n];\n        for (int\
        \ i = 0; i < n; i++) {\n            int count = 0;\n            for (int j =\
        \ n - 1; j >= 0; j--) {\n                if (grid[i][j] == 0) count++;\n   \
        \             else break;\n            }\n            t[i] = count;\n      \
        \  }\n\n        int swaps = 0;\n        for (int i = 0; i < n; i++) {\n    \
        \        int target = n - 1 - i;\n            int found = -1;\n            for\
        \ (int j = i; j < n; j++) {\n                if (t[j] >= target) {\n       \
        \             found = j;\n                    break;\n                }\n  \
        \          }\n            if (found == -1) return -1;\n            swaps +=\
        \ (found - i);\n            int val = t[found];\n            for (int k = found;\
        \ k > i; k--) {\n                t[k] = t[k - 1];\n            }\n         \
        \   t[i] = val;\n        }\n        return swaps;\n    }\n}"
      javascript: "/**\n * @param {number[][]} grid\n * @return {number}\n */\nvar minSwaps\
        \ = function(grid) {\n    const n = grid.length;\n    const t = [];\n    for\
        \ (let i = 0; i < n; i++) {\n        let count = 0;\n        for (let j = n\
        \ - 1; j >= 0; j--) {\n            if (grid[i][j] === 0) count++;\n        \
        \    else break;\n        }\n        t.push(count);\n    }\n\n    let swaps\
        \ = 0;\n    for (let i = 0; i < n; i++) {\n        const target = n - 1 - i;\n\
        \        let found = -1;\n        for (let j = i; j < n; j++) {\n          \
        \  if (t[j] >= target) {\n                found = j;\n                break;\n\
        \            }\n        }\n        if (found === -1) return -1;\n        swaps\
        \ += (found - i);\n        const val = t.splice(found, 1)[0];\n        t.splice(i,\
        \ 0, val);\n    }\n    return swaps;\n};"
      typescript: "function minSwaps(grid: number[][]): number {\n    const n = grid.length;\n\
        \    const trailingZeros: number[] = new Array(n).fill(0);\n    for (let i =\
        \ 0; i < n; i++) {\n        let count = 0;\n        for (let j = n - 1; j >=\
        \ 0; j--) {\n            if (grid[i][j] === 0) {\n                count++;\n\
        \            } else {\n                break;\n            }\n        }\n  \
        \      trailingZeros[i] = count;\n    }\n\n    let totalSwaps = 0;\n    for\
        \ (let i = 0; i < n; i++) {\n        const needed = n - 1 - i;\n        let\
        \ foundIndex = -1;\n        for (let j = i; j < n; j++) {\n            if (trailingZeros[j]\
        \ >= needed) {\n                foundIndex = j;\n                break;\n  \
        \          }\n        }\n\n        if (foundIndex === -1) return -1;\n\n   \
        \     for (let k = foundIndex; k > i; k--) {\n            const temp = trailingZeros[k];\n\
        \            trailingZeros[k] = trailingZeros[k - 1];\n            trailingZeros[k\
        \ - 1] = temp;\n            totalSwaps++;\n        }\n    }\n    return totalSwaps;\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $grid\n     * @return\
        \ Integer\n     */\n    function minSwaps($grid) {\n        $n = count($grid);\n\
        \        $trailingZeros = [];\n        for ($i = 0; $i < $n; $i++) {\n     \
        \       $count = 0;\n            for ($j = $n - 1; $j >= 0; $j--) {\n      \
        \          if ($grid[$i][$j] == 0) {\n                    $count++;\n      \
        \          } else {\n                    break;\n                }\n       \
        \     }\n            $trailingZeros[$i] = $count;\n        }\n\n        $totalSwaps\
        \ = 0;\n        for ($i = 0; $i < $n; $i++) {\n            $needed = $n - 1\
        \ - $i;\n            $foundIndex = -1;\n            for ($j = $i; $j < $n; $j++)\
        \ {\n                if ($trailingZeros[$j] >= $needed) {\n                \
        \    $foundIndex = $j;\n                    break;\n                }\n    \
        \        }\n\n            if ($foundIndex == -1) return -1;\n\n            for\
        \ ($k = $foundIndex; $k > $i; $k--) {\n                $temp = $trailingZeros[$k];\n\
        \                $trailingZeros[$k] = $trailingZeros[$k - 1];\n            \
        \    $trailingZeros[$k - 1] = $temp;\n                $totalSwaps++;\n     \
        \       }\n        }\n        return $totalSwaps;\n    }\n}"
      swift: "class Solution {\n    func minSwaps(_ grid: [[Int]]) -> Int {\n      \
        \  let n = grid.count\n        var trailingZeros = [Int](repeating: 0, count:\
        \ n)\n        for i in 0..<n {\n            var count = 0\n            for j\
        \ in (0..<n).reversed() {\n                if grid[i][j] == 0 {\n          \
        \          count += 1\n                } else {\n                    break\n\
        \                }\n            }\n            trailingZeros[i] = count\n  \
        \      }\n\n        var totalSwaps = 0\n        for i in 0..<n {\n         \
        \   let needed = n - 1 - i\n            var foundIndex = -1\n            for\
        \ j in i..<n {\n                if trailingZeros[j] >= needed {\n          \
        \          foundIndex = j\n                    break\n                }\n  \
        \          }\n\n            if foundIndex == -1 {\n                return -1\n\
        \            }\n\n            for k in stride(from: foundIndex, to: i, by: -1)\
        \ {\n                trailingZeros.swapAt(k, k - 1)\n                totalSwaps\
        \ += 1\n            }\n        }\n        return totalSwaps\n    }\n}"
      kotlin: "class Solution {\n    fun minSwaps(grid: Array<IntArray>): Int {\n  \
        \      val n = grid.size\n        val trailingZeros = IntArray(n)\n        for\
        \ (i in 0 until n) {\n            var count = 0\n            for (j in n - 1\
        \ downTo 0) {\n                if (grid[i][j] == 0) {\n                    count++\n\
        \                } else {\n                    break\n                }\n  \
        \          }\n            trailingZeros[i] = count\n        }\n\n        var\
        \ totalSwaps = 0\n        for (i in 0 until n) {\n            val needed = n\
        \ - 1 - i\n            var foundIndex = -1\n            for (j in i until n)\
        \ {\n                if (trailingZeros[j] >= needed) {\n                   \
        \ foundIndex = j\n                    break\n                }\n           \
        \ }\n\n            if (foundIndex == -1) return -1\n\n            for (k in\
        \ foundIndex downTo i + 1) {\n                val temp = trailingZeros[k]\n\
        \                trailingZeros[k] = trailingZeros[k - 1]\n                trailingZeros[k\
        \ - 1] = temp\n                totalSwaps++\n            }\n        }\n    \
        \    return totalSwaps\n    }\n}"
      dart: "class Solution {\n  int minSwaps(List<List<int>> grid) {\n    int n = grid.length;\n\
        \    List<int> trailingZeros = List.filled(n, 0);\n    for (int i = 0; i < n;\
        \ i++) {\n      int count = 0;\n      for (int j = n - 1; j >= 0; j--) {\n \
        \       if (grid[i][j] == 0) {\n          count++;\n        } else {\n     \
        \     break;\n        }\n      }\n      trailingZeros[i] = count;\n    }\n\n\
        \    int totalSwaps = 0;\n    for (int i = 0; i < n; i++) {\n      int needed\
        \ = n - 1 - i;\n      int foundIndex = -1;\n      for (int j = i; j < n; j++)\
        \ {\n        if (trailingZeros[j] >= needed) {\n          foundIndex = j;\n\
        \          break;\n        }\n      }\n\n      if (foundIndex == -1) return\
        \ -1;\n\n      for (int k = foundIndex; k > i; k--) {\n        int temp = trailingZeros[k];\n\
        \        trailingZeros[k] = trailingZeros[k - 1];\n        trailingZeros[k -\
        \ 1] = temp;\n        totalSwaps++;\n      }\n    }\n    return totalSwaps;\n\
        \  }\n}"
      go: "func minSwaps(grid [][]int) int {\n    n := len(grid)\n    trailingZeros\
        \ := make([]int, n)\n    for i := 0; i < n; i++ {\n        count := 0\n    \
        \    for j := n - 1; j >= 0; j-- {\n            if grid[i][j] == 0 {\n     \
        \           count++\n            } else {\n                break\n         \
        \   }\n        }\n        trailingZeros[i] = count\n    }\n\n    totalSwaps\
        \ := 0\n    for i := 0; i < n; i++ {\n        needed := n - 1 - i\n        foundIndex\
        \ := -1\n        for j := i; j < n; j++ {\n            if trailingZeros[j] >=\
        \ needed {\n                foundIndex = j\n                break\n        \
        \    }\n        }\n\n        if foundIndex == -1 {\n            return -1\n\
        \        }\n\n        for k := foundIndex; k > i; k-- {\n            trailingZeros[k],\
        \ trailingZeros[k-1] = trailingZeros[k-1], trailingZeros[k]\n            totalSwaps++\n\
        \        }\n    }\n    return totalSwaps\n}"
      ruby: "def min_swaps(grid)\n  n = grid.length\n  trailing_zeros = grid.map do\
        \ |row|\n    count = 0\n    row.reverse_each do |val|\n      break if val !=\
        \ 0\n      count += 1\n    end\n    count\n  end\n  ans = 0\n  (0...n).each\
        \ do |i|\n    needed = n - 1 - i\n    found = -1\n    (i...n).each do |j|\n\
        \      if trailing_zeros[j] >= needed\n        found = j\n        break\n  \
        \    end\n    end\n    return -1 if found == -1\n    ans += (found - i)\n  \
        \  val = trailing_zeros.delete_at(found)\n    trailing_zeros.insert(i, val)\n\
        \  end\n  ans\nend"
      scala: "import scala.collection.mutable.ArrayBuffer\n\nobject Solution {\n  def\
        \ minSwaps(grid: Array[Array[Int]]): Int = {\n    val n = grid.length\n    val\
        \ trailingZeros = ArrayBuffer[Int]()\n    for (row <- grid) {\n      var count\
        \ = 0\n      var i = n - 1\n      while (i >= 0 && row(i) == 0) {\n        count\
        \ += 1\n        i -= 1\n      }\n      trailingZeros += count\n    }\n    var\
        \ ans = 0\n    for (i <- 0 until n) {\n      val needed = n - 1 - i\n      var\
        \ found = -1\n      var j = i\n      while (j < n && found == -1) {\n      \
        \  if (trailingZeros(j) >= needed) {\n          found = j\n        }\n     \
        \   j += 1\n      }\n      if (found == -1) return -1\n      ans += (found -\
        \ i)\n      val v = trailingZeros.remove(found)\n      trailingZeros.insert(i,\
        \ v)\n    }\n    ans\n  }\n}"
      rust: "impl Solution {\n    pub fn min_swaps(grid: Vec<Vec<i32>>) -> i32 {\n \
        \       let n = grid.len();\n        let mut trailing_zeros = Vec::with_capacity(n);\n\
        \        for row in grid {\n            let mut count = 0;\n            for\
        \ &val in row.iter().rev() {\n                if val == 0 { count += 1; }\n\
        \                else { break; }\n            }\n            trailing_zeros.push(count);\n\
        \        }\n        let mut ans = 0;\n        for i in 0..n {\n            let\
        \ needed = (n - 1 - i) as i32;\n            let mut found = -1;\n          \
        \  for j in i..n {\n                if trailing_zeros[j] >= needed {\n     \
        \               found = j as i32;\n                    break;\n            \
        \    }\n            }\n            if found == -1 { return -1; }\n         \
        \   ans += found - i as i32;\n            let val = trailing_zeros.remove(found\
        \ as usize);\n            trailing_zeros.insert(i, val);\n        }\n      \
        \  ans\n    }\n}"
      racket: "(define/contract (min-swaps grid)\n  (-> (listof (listof exact-integer?))\
        \ exact-integer?)\n  (let* ([n (length grid)]\n         [count-zeros (lambda\
        \ (row)\n                        (let loop ([lst (reverse row)] [c 0])\n   \
        \                       (cond [(empty? lst) c]\n                           \
        \     [(= (car lst) 0) (loop (cdr lst) (+ c 1))]\n                         \
        \       [else c])))]\n         [zeros (map count-zeros grid)])\n    (let loop\
        \ ([i 0] [current-zeros zeros] [total-swaps 0])\n      (if (= i n)\n       \
        \   total-swaps\n          (let* ([needed (- n 1 i)]\n                 [found-idx\
        \ (let find ([idx i] [lst (drop current-zeros i)])\n                       \
        \       (cond [(empty? lst) -1]\n                                    [(>= (car\
        \ lst) needed) idx]\n                                    [else (find (+ idx\
        \ 1) (cdr lst))]))])\n            (if (= found-idx -1)\n                -1\n\
        \                (let* ([val (list-ref current-zeros found-idx)]\n         \
        \              [without-val (append (take current-zeros found-idx) (drop current-zeros\
        \ (+ found-idx 1)))]\n                       [new-zeros (append (take without-val\
        \ i) (list val) (drop without-val i))])\n                  (loop (+ i 1) new-zeros\
        \ (+ total-swaps (- found-idx i))))))))))"
      erlang: "-spec min_swaps(Grid :: [[integer()]]) -> integer().\nmin_swaps(Grid)\
        \ ->\n    N = length(Grid),\n    TrailingZeros = [count_zeros(lists:reverse(Row))\
        \ || Row <- Grid],\n    solve(0, N, TrailingZeros, 0).\n\ncount_zeros([]) ->\
        \ 0;\ncount_zeros([0|T]) -> 1 + count_zeros(T);\ncount_zeros([1|_]) -> 0.\n\n\
        solve(I, N, _Zeros, Swaps) when I == N -> Swaps;\nsolve(I, N, Zeros, Swaps)\
        \ ->\n    Needed = N - 1 - I,\n    case find_index(I, Zeros, Needed) of\n  \
        \      -1 -> -1;\n        FoundIdx ->\n            {_Val, NewZeros} = extract_and_insert(FoundIdx,\
        \ I, Zeros),\n            solve(I + 1, N, NewZeros, Swaps + (FoundIdx - I))\n\
        \    end.\n\nfind_index(Idx, Zeros, Needed) ->\n    SubList = lists:nthtail(Idx,\
        \ Zeros),\n    find_index_recursive(Idx, SubList, Needed).\n\nfind_index_recursive(_,\
        \ [], _) -> -1;\nfind_index_recursive(Idx, [H|_], Needed) when H >= Needed ->\
        \ Idx;\nfind_index_recursive(Idx, [_|T], Needed) -> find_index_recursive(Idx\
        \ + 1, T, Needed).\n\nextract_and_insert(FoundIdx, I, Zeros) ->\n    {Left,\
        \ [Val|Right]} = lists:split(FoundIdx, Zeros),\n    WithoutVal = Left ++ Right,\n\
        \    {BeforeI, AfterI} = lists:split(I, WithoutVal),\n    {Val, BeforeI ++ [Val]\
        \ ++ AfterI}."
      elixir: "defmodule Solution do\n  @spec min_swaps(grid :: [[integer]]) :: integer\n\
        \  def min_swaps(grid) do\n    n = length(grid)\n    trailing_zeros = Enum.map(grid,\
        \ fn row ->\n      Enum.reverse(row) |> Enum.find_index(&(&1 != 0)) || n\n \
        \   end)\n    solve(0, n, trailing_zeros, 0)\n  end\n\n  defp solve(i, n, _zeros,\
        \ swaps) when i == n, do: swaps\n  defp solve(i, n, zeros, swaps) do\n    needed\
        \ = n - 1 - i\n    found_idx = Enum.find_index(Enum.slice(zeros, i..-1), &(&1\
        \ >= needed))\n\n    if found_idx == nil do\n      -1\n    else\n      abs_idx\
        \ = found_idx + i\n      val = Enum.at(zeros, abs_idx)\n      new_zeros = List.delete_at(zeros,\
        \ abs_idx) |> List.insert_at(i, val)\n      solve(i + 1, n, new_zeros, swaps\
        \ + (abs_idx - i))\n    end\n  end\nend"
    approach: 'To solve this problem, we first determine the number of trailing zeros
      in each row of the $n \times n$ grid. For a grid to be valid, row $i$ (where $0
      \le i < n$) must have at least $n - 1 - i$ trailing zeros. We preprocess the grid
      to store these zero counts in an array, where each element $t[i]$ represents the
      number of consecutive zeros at the end of the original $i$-th row. This transforms
      the problem into finding the minimum number of adjacent swaps to reorder the array
      such that $t[i] \ge n - 1 - i$ for all $i$.


      We use a greedy simulation strategy to find the minimum swaps. For each row position
      $i$ from $0$ to $n-1$, we look for the first row $j \ge i$ in the current array
      that satisfies the condition $t[j] \ge n - 1 - i$. If we find such a row at index
      $j$, the number of adjacent swaps required to move it to position $i$ is $j -
      i$. We add this to our total swap count and shift the intermediate rows down by
      one to maintain their relative order. If no such row is found for any position
      $i$, it''s impossible to satisfy the condition, so we return -1. This greedy choice
      is optimal because picking the closest row that satisfies the condition minimizes
      swaps and preserves the most options for future rows.'
    time_complexity: O(n^2) where n is the dimension of the grid. Calculating the trailing
      zeros for each of the n rows takes O(n^2) time. The greedy simulation involves
      an outer loop running n times and an inner search and shift, both of which take
      O(n) time, resulting in O(n^2) overall.
    space_complexity: O(n) because we store the trailing zero count for each of the
      n rows in a separate array or list.
    elapsed_time: 145.03434801101685
    model: gemini-3-flash-preview
    generated_at: '2026-03-02 01:25:05 '
---

## Problem #1536: Minimum Swaps to Arrange a Binary Grid

**Difficulty:** Medium

**Topics:** Array, Greedy, Matrix

## Problem Description

<p>Given an <code>n x n</code> binary <code>grid</code>, in one step you can choose two <strong>adjacent rows</strong> of the grid and swap them.</p>

<p>A grid is said to be <strong>valid</strong> if all the cells above the main diagonal are <strong>zeros</strong>.</p>

<p>Return <em>the minimum number of steps</em> needed to make the grid valid, or <strong>-1</strong> if the grid cannot be valid.</p>

<p>The main diagonal of a grid is the diagonal that starts at cell <code>(1, 1)</code> and ends at cell <code>(n, n)</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/07/28/fw.jpg" style="width: 750px; height: 141px;" />
<pre>
<strong>Input:</strong> grid = [[0,0,1],[1,1,0],[1,0,0]]
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/07/16/e2.jpg" style="width: 270px; height: 270px;" />
<pre>
<strong>Input:</strong> grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
<strong>Output:</strong> -1
<strong>Explanation:</strong> All rows are similar, swaps have no effect on the grid.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/07/16/e3.jpg" style="width: 200px; height: 200px;" />
<pre>
<strong>Input:</strong> grid = [[1,0,0],[1,1,0],[1,1,1]]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == grid.length</code> <code>== grid[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 200</code></li>
	<li><code>grid[i][j]</code> is either <code>0</code> or <code>1</code></li>
</ul>


## Hints

1. For each row of the grid calculate the most right 1 in the grid in the array maxRight.

2. To check if there exist answer, sort maxRight and check if maxRight[i] ≤ i for all possible i's.

3. If there exist an answer, simulate the swaps.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To solve this problem, we first determine the number of trailing zeros in each row of the $n \times n$ grid. For a grid to be valid, row $i$ (where $0 \le i < n$) must have at least $n - 1 - i$ trailing zeros. We preprocess the grid to store these zero counts in an array, where each element $t[i]$ represents the number of consecutive zeros at the end of the original $i$-th row. This transforms the problem into finding the minimum number of adjacent swaps to reorder the array such that $t[i] \ge n - 1 - i$ for all $i$.

We use a greedy simulation strategy to find the minimum swaps. For each row position $i$ from $0$ to $n-1$, we look for the first row $j \ge i$ in the current array that satisfies the condition $t[j] \ge n - 1 - i$. If we find such a row at index $j$, the number of adjacent swaps required to move it to position $i$ is $j - i$. We add this to our total swap count and shift the intermediate rows down by one to maintain their relative order. If no such row is found for any position $i$, it's impossible to satisfy the condition, so we return -1. This greedy choice is optimal because picking the closest row that satisfies the condition minimizes swaps and preserves the most options for future rows.

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
    int minSwaps(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<int> t(n);
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = n - 1; j >= 0; j--) {
                if (grid[i][j] == 0) count++;
                else break;
            }
            t[i] = count;
        }

        int swaps = 0;
        for (int i = 0; i < n; i++) {
            int target = n - 1 - i;
            int found = -1;
            for (int j = i; j < n; j++) {
                if (t[j] >= target) {
                    found = j;
                    break;
                }
            }
            if (found == -1) return -1;
            swaps += (found - i);
            int val = t[found];
            for (int k = found; k > i; k--) {
                t[k] = t[k - 1];
            }
            t[i] = val;
        }
        return swaps;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minSwaps(int[][] grid) {
        int n = grid.length;
        int[] t = new int[n];
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = n - 1; j >= 0; j--) {
                if (grid[i][j] == 0) count++;
                else break;
            }
            t[i] = count;
        }

        int swaps = 0;
        for (int i = 0; i < n; i++) {
            int target = n - 1 - i;
            int found = -1;
            for (int j = i; j < n; j++) {
                if (t[j] >= target) {
                    found = j;
                    break;
                }
            }
            if (found == -1) return -1;
            swaps += (found - i);
            int val = t[found];
            for (int k = found; k > i; k--) {
                t[k] = t[k - 1];
            }
            t[i] = val;
        }
        return swaps;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        t = []
        for i in range(n):
            count = 0
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    count += 1
                else:
                    break
            t.append(count)

        swaps = 0
        for i in range(n):
            target = n - 1 - i
            found = -1
            for j in range(i, n):
                if t[j] >= target:
                    found = j
                    break
            if found == -1:
                return -1
            swaps += (found - i)
            val = t.pop(found)
            t.insert(i, val)
        return swaps
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        t = []
        for row in grid:
            count = 0
            for j in range(n - 1, -1, -1):
                if row[j] == 0:
                    count += 1
                else:
                    break
            t.append(count)

        swaps = 0
        for i in range(n):
            target = n - 1 - i
            found = -1
            for j in range(i, n):
                if t[j] >= target:
                    found = j
                    break
            if found == -1:
                return -1
            swaps += (found - i)
            val = t.pop(found)
            t.insert(i, val)
        return swaps
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int minSwaps(int** grid, int gridSize, int* gridColSize) {
    int n = gridSize;
    int t[n];
    for (int i = 0; i < n; i++) {
        int count = 0;
        for (int j = n - 1; j >= 0; j--) {
            if (grid[i][j] == 0) count++;
            else break;
        }
        t[i] = count;
    }

    int swaps = 0;
    for (int i = 0; i < n; i++) {
        int target = n - 1 - i;
        int found = -1;
        for (int j = i; j < n; j++) {
            if (t[j] >= target) {
                found = j;
                break;
            }
        }
        if (found == -1) return -1;
        swaps += (found - i);
        int val = t[found];
        for (int k = found; k > i; k--) {
            t[k] = t[k - 1];
        }
        t[i] = val;
    }
    return swaps;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinSwaps(int[][] grid) {
        int n = grid.Length;
        int[] t = new int[n];
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = n - 1; j >= 0; j--) {
                if (grid[i][j] == 0) count++;
                else break;
            }
            t[i] = count;
        }

        int swaps = 0;
        for (int i = 0; i < n; i++) {
            int target = n - 1 - i;
            int found = -1;
            for (int j = i; j < n; j++) {
                if (t[j] >= target) {
                    found = j;
                    break;
                }
            }
            if (found == -1) return -1;
            swaps += (found - i);
            int val = t[found];
            for (int k = found; k > i; k--) {
                t[k] = t[k - 1];
            }
            t[i] = val;
        }
        return swaps;
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
var minSwaps = function(grid) {
    const n = grid.length;
    const t = [];
    for (let i = 0; i < n; i++) {
        let count = 0;
        for (let j = n - 1; j >= 0; j--) {
            if (grid[i][j] === 0) count++;
            else break;
        }
        t.push(count);
    }

    let swaps = 0;
    for (let i = 0; i < n; i++) {
        const target = n - 1 - i;
        let found = -1;
        for (let j = i; j < n; j++) {
            if (t[j] >= target) {
                found = j;
                break;
            }
        }
        if (found === -1) return -1;
        swaps += (found - i);
        const val = t.splice(found, 1)[0];
        t.splice(i, 0, val);
    }
    return swaps;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minSwaps(grid: number[][]): number {
    const n = grid.length;
    const trailingZeros: number[] = new Array(n).fill(0);
    for (let i = 0; i < n; i++) {
        let count = 0;
        for (let j = n - 1; j >= 0; j--) {
            if (grid[i][j] === 0) {
                count++;
            } else {
                break;
            }
        }
        trailingZeros[i] = count;
    }

    let totalSwaps = 0;
    for (let i = 0; i < n; i++) {
        const needed = n - 1 - i;
        let foundIndex = -1;
        for (let j = i; j < n; j++) {
            if (trailingZeros[j] >= needed) {
                foundIndex = j;
                break;
            }
        }

        if (foundIndex === -1) return -1;

        for (let k = foundIndex; k > i; k--) {
            const temp = trailingZeros[k];
            trailingZeros[k] = trailingZeros[k - 1];
            trailingZeros[k - 1] = temp;
            totalSwaps++;
        }
    }
    return totalSwaps;
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
    function minSwaps($grid) {
        $n = count($grid);
        $trailingZeros = [];
        for ($i = 0; $i < $n; $i++) {
            $count = 0;
            for ($j = $n - 1; $j >= 0; $j--) {
                if ($grid[$i][$j] == 0) {
                    $count++;
                } else {
                    break;
                }
            }
            $trailingZeros[$i] = $count;
        }

        $totalSwaps = 0;
        for ($i = 0; $i < $n; $i++) {
            $needed = $n - 1 - $i;
            $foundIndex = -1;
            for ($j = $i; $j < $n; $j++) {
                if ($trailingZeros[$j] >= $needed) {
                    $foundIndex = $j;
                    break;
                }
            }

            if ($foundIndex == -1) return -1;

            for ($k = $foundIndex; $k > $i; $k--) {
                $temp = $trailingZeros[$k];
                $trailingZeros[$k] = $trailingZeros[$k - 1];
                $trailingZeros[$k - 1] = $temp;
                $totalSwaps++;
            }
        }
        return $totalSwaps;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minSwaps(_ grid: [[Int]]) -> Int {
        let n = grid.count
        var trailingZeros = [Int](repeating: 0, count: n)
        for i in 0..<n {
            var count = 0
            for j in (0..<n).reversed() {
                if grid[i][j] == 0 {
                    count += 1
                } else {
                    break
                }
            }
            trailingZeros[i] = count
        }

        var totalSwaps = 0
        for i in 0..<n {
            let needed = n - 1 - i
            var foundIndex = -1
            for j in i..<n {
                if trailingZeros[j] >= needed {
                    foundIndex = j
                    break
                }
            }

            if foundIndex == -1 {
                return -1
            }

            for k in stride(from: foundIndex, to: i, by: -1) {
                trailingZeros.swapAt(k, k - 1)
                totalSwaps += 1
            }
        }
        return totalSwaps
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minSwaps(grid: Array<IntArray>): Int {
        val n = grid.size
        val trailingZeros = IntArray(n)
        for (i in 0 until n) {
            var count = 0
            for (j in n - 1 downTo 0) {
                if (grid[i][j] == 0) {
                    count++
                } else {
                    break
                }
            }
            trailingZeros[i] = count
        }

        var totalSwaps = 0
        for (i in 0 until n) {
            val needed = n - 1 - i
            var foundIndex = -1
            for (j in i until n) {
                if (trailingZeros[j] >= needed) {
                    foundIndex = j
                    break
                }
            }

            if (foundIndex == -1) return -1

            for (k in foundIndex downTo i + 1) {
                val temp = trailingZeros[k]
                trailingZeros[k] = trailingZeros[k - 1]
                trailingZeros[k - 1] = temp
                totalSwaps++
            }
        }
        return totalSwaps
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minSwaps(List<List<int>> grid) {
    int n = grid.length;
    List<int> trailingZeros = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      int count = 0;
      for (int j = n - 1; j >= 0; j--) {
        if (grid[i][j] == 0) {
          count++;
        } else {
          break;
        }
      }
      trailingZeros[i] = count;
    }

    int totalSwaps = 0;
    for (int i = 0; i < n; i++) {
      int needed = n - 1 - i;
      int foundIndex = -1;
      for (int j = i; j < n; j++) {
        if (trailingZeros[j] >= needed) {
          foundIndex = j;
          break;
        }
      }

      if (foundIndex == -1) return -1;

      for (int k = foundIndex; k > i; k--) {
        int temp = trailingZeros[k];
        trailingZeros[k] = trailingZeros[k - 1];
        trailingZeros[k - 1] = temp;
        totalSwaps++;
      }
    }
    return totalSwaps;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minSwaps(grid [][]int) int {
    n := len(grid)
    trailingZeros := make([]int, n)
    for i := 0; i < n; i++ {
        count := 0
        for j := n - 1; j >= 0; j-- {
            if grid[i][j] == 0 {
                count++
            } else {
                break
            }
        }
        trailingZeros[i] = count
    }

    totalSwaps := 0
    for i := 0; i < n; i++ {
        needed := n - 1 - i
        foundIndex := -1
        for j := i; j < n; j++ {
            if trailingZeros[j] >= needed {
                foundIndex = j
                break
            }
        }

        if foundIndex == -1 {
            return -1
        }

        for k := foundIndex; k > i; k-- {
            trailingZeros[k], trailingZeros[k-1] = trailingZeros[k-1], trailingZeros[k]
            totalSwaps++
        }
    }
    return totalSwaps
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def min_swaps(grid)
  n = grid.length
  trailing_zeros = grid.map do |row|
    count = 0
    row.reverse_each do |val|
      break if val != 0
      count += 1
    end
    count
  end
  ans = 0
  (0...n).each do |i|
    needed = n - 1 - i
    found = -1
    (i...n).each do |j|
      if trailing_zeros[j] >= needed
        found = j
        break
      end
    end
    return -1 if found == -1
    ans += (found - i)
    val = trailing_zeros.delete_at(found)
    trailing_zeros.insert(i, val)
  end
  ans
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable.ArrayBuffer

object Solution {
  def minSwaps(grid: Array[Array[Int]]): Int = {
    val n = grid.length
    val trailingZeros = ArrayBuffer[Int]()
    for (row <- grid) {
      var count = 0
      var i = n - 1
      while (i >= 0 && row(i) == 0) {
        count += 1
        i -= 1
      }
      trailingZeros += count
    }
    var ans = 0
    for (i <- 0 until n) {
      val needed = n - 1 - i
      var found = -1
      var j = i
      while (j < n && found == -1) {
        if (trailingZeros(j) >= needed) {
          found = j
        }
        j += 1
      }
      if (found == -1) return -1
      ans += (found - i)
      val v = trailingZeros.remove(found)
      trailingZeros.insert(i, v)
    }
    ans
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_swaps(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let mut trailing_zeros = Vec::with_capacity(n);
        for row in grid {
            let mut count = 0;
            for &val in row.iter().rev() {
                if val == 0 { count += 1; }
                else { break; }
            }
            trailing_zeros.push(count);
        }
        let mut ans = 0;
        for i in 0..n {
            let needed = (n - 1 - i) as i32;
            let mut found = -1;
            for j in i..n {
                if trailing_zeros[j] >= needed {
                    found = j as i32;
                    break;
                }
            }
            if found == -1 { return -1; }
            ans += found - i as i32;
            let val = trailing_zeros.remove(found as usize);
            trailing_zeros.insert(i, val);
        }
        ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-swaps grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ([n (length grid)]
         [count-zeros (lambda (row)
                        (let loop ([lst (reverse row)] [c 0])
                          (cond [(empty? lst) c]
                                [(= (car lst) 0) (loop (cdr lst) (+ c 1))]
                                [else c])))]
         [zeros (map count-zeros grid)])
    (let loop ([i 0] [current-zeros zeros] [total-swaps 0])
      (if (= i n)
          total-swaps
          (let* ([needed (- n 1 i)]
                 [found-idx (let find ([idx i] [lst (drop current-zeros i)])
                              (cond [(empty? lst) -1]
                                    [(>= (car lst) needed) idx]
                                    [else (find (+ idx 1) (cdr lst))]))])
            (if (= found-idx -1)
                -1
                (let* ([val (list-ref current-zeros found-idx)]
                       [without-val (append (take current-zeros found-idx) (drop current-zeros (+ found-idx 1)))]
                       [new-zeros (append (take without-val i) (list val) (drop without-val i))])
                  (loop (+ i 1) new-zeros (+ total-swaps (- found-idx i))))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_swaps(Grid :: [[integer()]]) -> integer().
min_swaps(Grid) ->
    N = length(Grid),
    TrailingZeros = [count_zeros(lists:reverse(Row)) || Row <- Grid],
    solve(0, N, TrailingZeros, 0).

count_zeros([]) -> 0;
count_zeros([0|T]) -> 1 + count_zeros(T);
count_zeros([1|_]) -> 0.

solve(I, N, _Zeros, Swaps) when I == N -> Swaps;
solve(I, N, Zeros, Swaps) ->
    Needed = N - 1 - I,
    case find_index(I, Zeros, Needed) of
        -1 -> -1;
        FoundIdx ->
            {_Val, NewZeros} = extract_and_insert(FoundIdx, I, Zeros),
            solve(I + 1, N, NewZeros, Swaps + (FoundIdx - I))
    end.

find_index(Idx, Zeros, Needed) ->
    SubList = lists:nthtail(Idx, Zeros),
    find_index_recursive(Idx, SubList, Needed).

find_index_recursive(_, [], _) -> -1;
find_index_recursive(Idx, [H|_], Needed) when H >= Needed -> Idx;
find_index_recursive(Idx, [_|T], Needed) -> find_index_recursive(Idx + 1, T, Needed).

extract_and_insert(FoundIdx, I, Zeros) ->
    {Left, [Val|Right]} = lists:split(FoundIdx, Zeros),
    WithoutVal = Left ++ Right,
    {BeforeI, AfterI} = lists:split(I, WithoutVal),
    {Val, BeforeI ++ [Val] ++ AfterI}.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_swaps(grid :: [[integer]]) :: integer
  def min_swaps(grid) do
    n = length(grid)
    trailing_zeros = Enum.map(grid, fn row ->
      Enum.reverse(row) |> Enum.find_index(&(&1 != 0)) || n
    end)
    solve(0, n, trailing_zeros, 0)
  end

  defp solve(i, n, _zeros, swaps) when i == n, do: swaps
  defp solve(i, n, zeros, swaps) do
    needed = n - 1 - i
    found_idx = Enum.find_index(Enum.slice(zeros, i..-1), &(&1 >= needed))

    if found_idx == nil do
      -1
    else
      abs_idx = found_idx + i
      val = Enum.at(zeros, abs_idx)
      new_zeros = List.delete_at(zeros, abs_idx) |> List.insert_at(i, val)
      solve(i + 1, n, new_zeros, swaps + (abs_idx - i))
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n^2) where n is the dimension of the grid. Calculating the trailing zeros for each of the n rows takes O(n^2) time. The greedy simulation involves an outer loop running n times and an inner search and shift, both of which take O(n) time, resulting in O(n^2) overall.
- **Space Complexity:** O(n) because we store the trailing zero count for each of the n rows in a separate array or list.
