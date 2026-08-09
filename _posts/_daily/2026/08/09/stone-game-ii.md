---
layout: post
title: "Stone Game II"
date: 2026-08-09 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Math", "Dynamic Programming", "Minimax", "Prefix Sum", "Game Theory", "Zero-Sum Game"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/stone-game-ii/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <algorithm>\n\nclass Solution {\npublic:\n \
        \   int stoneGameII(std::vector<int>& piles) {\n        int n = piles.size();\n\
        \        std::vector<int> suffixSum(n + 1, 0);\n        for (int i = n - 1;\
        \ i >= 0; i--) {\n            suffixSum[i] = suffixSum[i + 1] + piles[i];\n\
        \        }\n        std::vector<std::vector<int>> memo(n, std::vector<int>(n\
        \ + 1, 0));\n        return solve(0, 1, n, suffixSum, memo);\n    }\n\nprivate:\n\
        \    int solve(int i, int m, int n, const std::vector<int>& suffixSum, std::vector<std::vector<int>>&\
        \ memo) {\n        if (i + 2 * m >= n) return suffixSum[i];\n        if (memo[i][m]\
        \ != 0) return memo[i][m];\n\n        int res = 0;\n        for (int x = 1;\
        \ x <= 2 * m; x++) {\n            int next_m = std::max(m, x);\n           \
        \ res = std::max(res, suffixSum[i] - solve(i + x, next_m, n, suffixSum, memo));\n\
        \        }\n        return memo[i][m] = res;\n    }\n};"
      java: "class Solution {\n    public int stoneGameII(int[] piles) {\n        int\
        \ n = piles.length;\n        int[][] memo = new int[n][n + 1];\n        int[]\
        \ suffixSum = new int[n + 1];\n        for (int i = n - 1; i >= 0; i--) {\n\
        \            suffixSum[i] = suffixSum[i + 1] + piles[i];\n        }\n      \
        \  return solve(0, 1, n, suffixSum, memo);\n    }\n\n    private int solve(int\
        \ i, int m, int n, int[] suffixSum, int[][] memo) {\n        if (i + 2 * m >=\
        \ n) return suffixSum[i];\n        if (memo[i][m] != 0) return memo[i][m];\n\
        \n        int res = 0;\n        for (int x = 1; x <= 2 * m; x++) {\n       \
        \     int next_m = Math.max(m, x);\n            res = Math.max(res, suffixSum[i]\
        \ - solve(i + x, next_m, n, suffixSum, memo));\n        }\n        memo[i][m]\
        \ = res;\n        return res;\n    }\n}"
      python: "class Solution(object):\n    def stoneGameII(self, piles):\n        \"\
        \"\"\n        :type piles: List[int]\n        :rtype: int\n        \"\"\"\n\
        \        n = len(piles)\n        suffix_sum = [0] * (n + 1)\n        for i in\
        \ range(n - 1, -1, -1):\n            suffix_sum[i] = suffix_sum[i + 1] + piles[i]\n\
        \n        memo = {}\n\n        def solve(i, m):\n            if i + 2 * m >=\
        \ n:\n                return suffix_sum[i]\n            if (i, m) in memo:\n\
        \                return memo[(i, m)]\n\n            res = 0\n            for\
        \ x in range(1, 2 * m + 1):\n                res = max(res, suffix_sum[i] -\
        \ solve(i + x, max(m, x)))\n            memo[(i, m)] = res\n            return\
        \ res\n\n        return solve(0, 1)"
      python3: "from functools import lru_cache\nfrom typing import List\n\nclass Solution:\n\
        \    def stoneGameII(self, piles: List[int]) -> int:\n        n = len(piles)\n\
        \        suffix_sum = [0] * (n + 1)\n        for i in range(n - 1, -1, -1):\n\
        \            suffix_sum[i] = suffix_sum[i + 1] + piles[i]\n\n        @lru_cache(None)\n\
        \        def solve(i, m):\n            if i + 2 * m >= n:\n                return\
        \ suffix_sum[i]\n\n            res = 0\n            for x in range(1, 2 * m\
        \ + 1):\n                res = max(res, suffix_sum[i] - solve(i + x, max(m,\
        \ x)))\n            return res\n\n        return solve(0, 1)"
      c: "#include <string.h>\n\nint solve(int i, int m, int n, int* suffixSum, int\
        \ memo[101][101]) {\n    if (i + 2 * m >= n) return suffixSum[i];\n    if (memo[i][m]\
        \ != 0) return memo[i][m];\n\n    int res = 0;\n    for (int x = 1; x <= 2 *\
        \ m; x++) {\n        int next_m = (m > x) ? m : x;\n        int current = suffixSum[i]\
        \ - solve(i + x, next_m, n, suffixSum, memo);\n        if (current > res) res\
        \ = current;\n    }\n    return memo[i][m] = res;\n}\n\nint stoneGameII(int*\
        \ piles, int pilesSize) {\n    int suffixSum[101];\n    int memo[101][101];\n\
        \    memset(memo, 0, sizeof(memo));\n\n    int currentSum = 0;\n    for (int\
        \ i = pilesSize - 1; i >= 0; i--) {\n        currentSum += piles[i];\n     \
        \   suffixSum[i] = currentSum;\n    }\n\n    return solve(0, 1, pilesSize, suffixSum,\
        \ memo);\n}"
      csharp: "public class Solution {\n    public int StoneGameII(int[] piles) {\n\
        \        int n = piles.Length;\n        int[] suffixSum = new int[n + 1];\n\
        \        for (int i = n - 1; i >= 0; i--) {\n            suffixSum[i] = suffixSum[i\
        \ + 1] + piles[i];\n        }\n        int[,] memo = new int[n, n + 1];\n  \
        \      return Solve(0, 1, n, suffixSum, memo);\n    }\n\n    private int Solve(int\
        \ i, int m, int n, int[] suffixSum, int[,] memo) {\n        if (i + 2 * m >=\
        \ n) {\n            return suffixSum[i];\n        }\n        if (memo[i, m]\
        \ != 0) {\n            return memo[i, m];\n        }\n        int res = 0;\n\
        \        for (int x = 1; x <= 2 * m; x++) {\n            res = Math.Max(res,\
        \ suffixSum[i] - Solve(i + x, Math.Max(m, x), n, suffixSum, memo));\n      \
        \  }\n        memo[i, m] = res;\n        return res;\n    }\n}"
      javascript: "/**\n * @param {number[]} piles\n * @return {number}\n */\nvar stoneGameII\
        \ = function(piles) {\n    const n = piles.length;\n    const suffixSum = new\
        \ Array(n + 1).fill(0);\n    for (let i = n - 1; i >= 0; i--) {\n        suffixSum[i]\
        \ = suffixSum[i + 1] + piles[i];\n    }\n    const memo = Array.from({ length:\
        \ n }, () => new Array(n + 1).fill(0));\n\n    const solve = function(i, m)\
        \ {\n        if (i + 2 * m >= n) return suffixSum[i];\n        if (memo[i][m]\
        \ !== 0) return memo[i][m];\n        let res = 0;\n        for (let x = 1; x\
        \ <= 2 * m; x++) {\n            res = Math.max(res, suffixSum[i] - solve(i +\
        \ x, Math.max(m, x)));\n        }\n        memo[i][m] = res;\n        return\
        \ res;\n    };\n\n    return solve(0, 1);\n};"
      typescript: "function stoneGameII(piles: number[]): number {\n    const n: number\
        \ = piles.length;\n    const suffixSum: number[] = new Array(n + 1).fill(0);\n\
        \    for (let i = n - 1; i >= 0; i--) {\n        suffixSum[i] = suffixSum[i\
        \ + 1] + piles[i];\n    }\n    const memo: number[][] = Array.from({ length:\
        \ n }, () => new Array(n + 1).fill(0));\n\n    const solve = (i: number, m:\
        \ number): number => {\n        if (i + 2 * m >= n) return suffixSum[i];\n \
        \       if (memo[i][m] !== 0) return memo[i][m];\n        let res: number =\
        \ 0;\n        for (let x = 1; x <= 2 * m; x++) {\n            res = Math.max(res,\
        \ suffixSum[i] - solve(i + x, Math.max(m, x)));\n        }\n        memo[i][m]\
        \ = res;\n        return res;\n    };\n\n    return solve(0, 1);\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $piles\n     * @return\
        \ Integer\n     */\n    function stoneGameII($piles) {\n        $n = count($piles);\n\
        \        $suffixSum = array_fill(0, $n + 1, 0);\n        for ($i = $n - 1; $i\
        \ >= 0; $i--) {\n            $suffixSum[$i] = $suffixSum[$i + 1] + $piles[$i];\n\
        \        }\n        $memo = array_fill(0, $n, array_fill(0, $n + 1, 0));\n \
        \       return $this->solve(0, 1, $n, $suffixSum, $memo);\n    }\n\n    private\
        \ function solve($i, $m, $n, $suffixSum, &$memo) {\n        if ($i + 2 * $m\
        \ >= $n) {\n            return $suffixSum[$i];\n        }\n        if ($memo[$i][$m]\
        \ != 0) {\n            return $memo[$i][$m];\n        }\n        $res = 0;\n\
        \        for ($x = 1; $x <= 2 * $m; $x++) {\n            $res = max($res, $suffixSum[$i]\
        \ - $this->solve($i + $x, max($m, $x), $n, $suffixSum, $memo));\n        }\n\
        \        $memo[$i][$m] = $res;\n        return $res;\n    }\n}"
      swift: "class Solution {\n    func stoneGameII(_ piles: [Int]) -> Int {\n    \
        \    let n = piles.count\n        var suffixSum = [Int](repeating: 0, count:\
        \ n + 1)\n        for i in stride(from: n - 1, through: 0, by: -1) {\n     \
        \       suffixSum[i] = suffixSum[i + 1] + piles[i]\n        }\n        var memo\
        \ = [[Int]](repeating: [Int](repeating: 0, count: n + 1), count: n)\n\n    \
        \    func solve(_ i: Int, _ m: Int) -> Int {\n            if i + 2 * m >= n\
        \ {\n                return suffixSum[i]\n            }\n            if memo[i][m]\
        \ != 0 {\n                return memo[i][m]\n            }\n            var\
        \ res = 0\n            for x in 1...(2 * m) {\n                let nextM = max(m,\
        \ x)\n                let currentScore = suffixSum[i] - solve(i + x, nextM)\n\
        \                if currentScore > res {\n                    res = currentScore\n\
        \                }\n            }\n            memo[i][m] = res\n          \
        \  return res\n        }\n\n        return solve(0, 1)\n    }\n}"
      kotlin: "import kotlin.math.max\n\nclass Solution {\n    fun stoneGameII(piles:\
        \ IntArray): Int {\n        val n = piles.size\n        val suffixSum = IntArray(n\
        \ + 1)\n        for (i in n - 1 downTo 0) {\n            suffixSum[i] = suffixSum[i\
        \ + 1] + piles[i]\n        }\n        val memo = Array(n + 1) { IntArray(n +\
        \ 1) }\n\n        fun solve(i: Int, m: Int): Int {\n            if (i + 2 *\
        \ m >= n) return suffixSum[i]\n            if (memo[i][m] != 0) return memo[i][m]\n\
        \n            var res = 0\n            for (x in 1..2 * m) {\n             \
        \   val cur = suffixSum[i] - solve(i + x, max(m, x))\n                if (cur\
        \ > res) res = cur\n            }\n            memo[i][m] = res\n          \
        \  return res\n        }\n\n        return solve(0, 1)\n    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int stoneGameII(List<int> piles)\
        \ {\n    int n = piles.length;\n    List<int> suffixSum = List.filled(n + 1,\
        \ 0);\n    for (int i = n - 1; i >= 0; i--) {\n      suffixSum[i] = suffixSum[i\
        \ + 1] + piles[i];\n    }\n    List<List<int>> memo = List.generate(n + 1, (_)\
        \ => List.filled(n + 1, 0));\n\n    int solve(int i, int m) {\n      if (i +\
        \ 2 * m >= n) return suffixSum[i];\n      if (memo[i][m] != 0) return memo[i][m];\n\
        \n      int res = 0;\n      for (int x = 1; x <= 2 * m; x++) {\n        int\
        \ cur = suffixSum[i] - solve(i + x, max(m, x));\n        if (cur > res) res\
        \ = cur;\n      }\n      memo[i][m] = res;\n      return res;\n    }\n\n   \
        \ return solve(0, 1);\n  }\n}"
      go: "func stoneGameII(piles []int) int {\n\tn := len(piles)\n\tsuffixSum := make([]int,\
        \ n+1)\n\tfor i := n - 1; i >= 0; i-- {\n\t\tsuffixSum[i] = suffixSum[i+1] +\
        \ piles[i]\n\t}\n\tmemo := make([][]int, n+1)\n\tfor i := range memo {\n\t\t\
        memo[i] = make([]int, n+1)\n\t}\n\n\tvar solve func(int, int) int\n\tsolve =\
        \ func(i, m int) int {\n\t\tif i+2*m >= n {\n\t\t\treturn suffixSum[i]\n\t\t\
        }\n\t\tif memo[i][m] != 0 {\n\t\t\treturn memo[i][m]\n\t\t}\n\n\t\tres := 0\n\
        \t\tfor x := 1; x <= 2*m; x++ {\n\t\t\tmNext := m\n\t\t\tif x > mNext {\n\t\t\
        \t\tmNext = x\n\t\t\t}\n\t\t\tcur := suffixSum[i] - solve(i+x, mNext)\n\t\t\t\
        if cur > res {\n\t\t\t\tres = cur\n\t\t\t}\n\t\t}\n\t\tmemo[i][m] = res\n\t\t\
        return res\n\t}\n\n\treturn solve(0, 1)\n}"
      ruby: "# @param {Integer[]} piles\n# @return {Integer}\ndef stone_game_ii(piles)\n\
        \  n = piles.length\n  suffix_sum = Array.new(n + 1, 0)\n  (n - 1).step(0, -1)\
        \ { |i| suffix_sum[i] = suffix_sum[i + 1] + piles[i] }\n  memo = Array.new(n\
        \ + 1) { Array.new(n + 1, 0) }\n\n  solve = lambda do |i, m|\n    return suffix_sum[i]\
        \ if i + 2 * m >= n\n    return memo[i][m] if memo[i][m] != 0\n\n    res = 0\n\
        \    (1..(2 * m)).each do |x|\n      m_next = m > x ? m : x\n      cur = suffix_sum[i]\
        \ - solve.call(i + x, m_next)\n      res = cur if cur > res\n    end\n    memo[i][m]\
        \ = res\n    res\n  end\n\n  solve.call(0, 1)\nend"
      scala: "import scala.math.max\n\nobject Solution {\n    def stoneGameII(piles:\
        \ Array[Int]): Int = {\n        val n = piles.length\n        val suffixSum\
        \ = new Array[Int](n + 1)\n        for (i <- n - 1 to 0 by -1) {\n         \
        \   suffixSum(i) = suffixSum(i + 1) + piles(i)\n        }\n        val memo\
        \ = Array.ofDim[Int](n + 1, n + 1)\n\n        def solve(i: Int, m: Int): Int\
        \ = {\n            if (i + 2 * m >= n) return suffixSum(i)\n            if (memo(i)(m)\
        \ != 0) return memo(i)(m)\n\n            var res = 0\n            for (x <-\
        \ 1 to 2 * m) {\n                val cur = suffixSum(i) - solve(i + x, max(m,\
        \ x))\n                if (cur > res) res = cur\n            }\n           \
        \ memo(i)(m) = res\n            res\n        }\n\n        solve(0, 1)\n    }\n\
        }"
      rust: "impl Solution {\n    pub fn stone_game_ii(piles: Vec<i32>) -> i32 {\n \
        \       let n = piles.len();\n        let mut suffix_sum = vec![0; n + 1];\n\
        \        for i in (0..n).rev() {\n            suffix_sum[i] = suffix_sum[i +\
        \ 1] + piles[i];\n        }\n\n        let mut dp = vec![vec![0; n + 1]; n +\
        \ 1];\n        for i in (0..=n).rev() {\n            for m in 1..=n {\n    \
        \            if i + 2 * m >= n {\n                    dp[i][m] = suffix_sum[i];\n\
        \                } else {\n                    let mut min_val = i32::MAX;\n\
        \                    for x in 1..=(2 * m) {\n                        let next_m\
        \ = std::cmp::min(n, std::cmp::max(m, x));\n                        if i + x\
        \ <= n {\n                            min_val = std::cmp::min(min_val, dp[i\
        \ + x][next_m]);\n                        }\n                    }\n       \
        \             dp[i][m] = suffix_sum[i] - min_val;\n                }\n     \
        \       }\n        }\n        dp[0][1]\n    }\n}"
      racket: "(define/contract (stone-game-ii piles)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let* ([n (length piles)]\n         [piles-vec (list->vector\
        \ piles)]\n         [suffix-sum (make-vector (+ n 1) 0)])\n    (for ([i (in-range\
        \ (- n 1) -1 -1)])\n      (vector-set! suffix-sum i (+ (vector-ref piles-vec\
        \ i) (vector-ref suffix-sum (+ i 1)))))\n    (let ([memo (make-hash)])\n   \
        \   (letrec ([solve (lambda (i m)\n                        (let ([m (min m n)])\n\
        \                          (cond\n                            [(>= i n) 0]\n\
        \                            [(>= (+ i (* 2 m)) n) (vector-ref suffix-sum i)]\n\
        \                            [(hash-has-key? memo (cons i m)) (hash-ref memo\
        \ (cons i m))]\n                            [else\n                        \
        \     (let* ([res (for/fold ([current-min 2000000000])\n                   \
        \                               ([x (in-range 1 (+ (* 2 m) 1))])\n         \
        \                                  (min current-min (solve (+ i x) (max m x))))])\n\
        \                               (let ([val (- (vector-ref suffix-sum i) res)])\n\
        \                                 (hash-set! memo (cons i m) val)\n        \
        \                         val))]))])\n        (solve 0 1)))))"
      erlang: "-spec stone_game_ii(Piles :: [integer()]) -> integer().\nstone_game_ii(Piles)\
        \ ->\n    N = length(Piles),\n    SuffixSums = calculate_suffix_sums(Piles),\n\
        \    Memo = ets:new(memo_table, [set, private]),\n    Result = solve(0, 1, N,\
        \ SuffixSums, Memo),\n    ets:delete(Memo),\n    Result.\n\ncalculate_suffix_sums(Piles)\
        \ ->\n    SuffixList = lists:foldl(fun(X, [H | _] = Acc) -> [X + H | Acc] end,\
        \ [0], lists:reverse(Piles)),\n    list_to_tuple(SuffixList).\n\nsolve(I, M,\
        \ N, SuffixSums, Memo) ->\n    MCapped = min(M, N),\n    case ets:lookup(Memo,\
        \ {I, MCapped}) of\n        [{_, Val}] -> Val;\n        [] ->\n            Res\
        \ = if\n                I >= N -> 0;\n                I + 2 * MCapped >= N ->\
        \ element(I + 1, SuffixSums);\n                true ->\n                   \
        \ MinOther = find_min(I, MCapped, 1, 2 * MCapped, N, SuffixSums, Memo, infinity),\n\
        \                    element(I + 1, SuffixSums) - MinOther\n            end,\n\
        \            ets:insert(Memo, {{I, MCapped}, Res}),\n            Res\n    end.\n\
        \nfind_min(_I, _M, X, MaxX, _N, _SuffixSums, _Memo, MinVal) when X > MaxX ->\
        \ MinVal;\nfind_min(I, M, X, MaxX, N, SuffixSums, Memo, MinVal) ->\n    Val\
        \ = solve(I + X, max(M, X), N, SuffixSums, Memo),\n    NewMinVal = min(MinVal,\
        \ Val),\n    find_min(I, M, X + 1, MaxX, N, SuffixSums, Memo, NewMinVal)."
      elixir: "defmodule Solution do\n  @spec stone_game_ii(piles :: [integer]) :: integer\n\
        \  def stone_game_ii(piles) do\n    n = length(piles)\n    suffix_sums = calculate_suffix_sums(piles)\n\
        \    {result, _} = solve(0, 1, n, suffix_sums, %{})\n    result\n  end\n\n \
        \ defp calculate_suffix_sums(piles) do\n    piles\n    |> Enum.reverse()\n \
        \   |> Enum.scan(0, fn x, acc -> x + acc end)\n    |> Enum.reverse()\n    |>\
        \ (fn sums -> sums ++ [0] end).()\n    |> Enum.with_index()\n    |> Map.new(fn\
        \ {s, i} -> {i, s} end)\n  end\n\n  defp solve(i, m, n, suffix_sums, memo) do\n\
        \    m_capped = min(m, n)\n    cond do\n      Map.has_key?(memo, {i, m_capped})\
        \ ->\n        {Map.get(memo, {i, m_capped}), memo}\n      i + 2 * m_capped >=\
        \ n ->\n        val = Map.get(suffix_sums, i, 0)\n        {val, Map.put(memo,\
        \ {i, m_capped}, val)}\n      true ->\n        {min_val, updated_memo} = Enum.reduce(1..(2\
        \ * m_capped), {nil, memo}, fn x, {curr_min, curr_memo} ->\n          {val,\
        \ new_memo} = solve(i + x, max(m_capped, x), n, suffix_sums, curr_memo)\n  \
        \        new_min = if is_nil(curr_min), do: val, else: min(curr_min, val)\n\
        \          {new_min, new_memo}\n        end)\n        res = Map.get(suffix_sums,\
        \ i) - min_val\n        {res, Map.put(updated_memo, {i, m_capped}, res)}\n \
        \   end\n  end\nend"
    approach: 'We use dynamic programming with memoization to determine the maximum
      stones Alice can obtain. The state of our DP is defined as (i, M), which represents
      the maximum number of stones the current player can collect starting from the
      i-th pile with the current value of M. Since Alice starts first, we want to find
      the result of the state (0, 1). To efficiently calculate the number of stones
      in any range [i, n-1], we precalculate suffix sums where suffixSum[i] is the total
      stones from the i-th pile to the end.


      For each turn, the player can take X piles where 1 <= X <= 2M. Each player''s
      goal is to maximize their stones, which is equivalent to taking the total remaining
      stones (suffixSum[i]) and subtracting the maximum stones the next player can get
      from the resulting state (solve(i + X, max(M, X))). The base case occurs when
      the current player can take all remaining piles (i + 2M >= n), at which point
      they take all available stones from suffixSum[i].'
    time_complexity: O(N^3). There are N possible values for the pile index i and approximately
      N possible values for M, resulting in O(N^2) states. For each state, we iterate
      up to 2M times (at most N) to explore all possible moves, giving an overall time
      complexity of O(N^3).
    space_complexity: O(N^2). We store the results of all (i, M) states in a memoization
      table of size approximately N x N, which consumes O(N^2) space.
    elapsed_time: 266.79233026504517
    model: gemini-3-flash-preview
    generated_at: '2026-08-09 01:10:44 '
---

## Problem #1140: Stone Game II

**Difficulty:** Medium

**Topics:** Array, Math, Dynamic Programming, Minimax, Prefix Sum, Game Theory, Zero-Sum Game

## Problem Description

<p>Alice and Bob continue their games with piles of stones. There are a number of piles <strong>arranged in a row</strong>, and each pile has a positive integer number of stones <code>piles[i]</code>. The objective of the game is to end with the most stones.</p>

<p>Alice and Bob take turns, with Alice starting first.</p>

<p>On each player&#39;s turn, that player can take <strong>all the stones</strong> in the <strong>first</strong> <code>X</code> remaining piles, where <code>1 &lt;= X &lt;= 2M</code>. Then, we set <code>M = max(M, X)</code>. Initially, M = 1.</p>

<p>The game continues until all the stones have been taken.</p>

<p>Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">piles = [2,7,9,4,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">10</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get <code>2 + 4 + 4 = 10</code> stones in total.</li>
	<li>If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get <code>2 + 7 = 9</code> stones in total.</li>
</ul>

<p>So we return 10 since it&#39;s larger.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">piles = [1,2,3,4,5,100]</span></p>

<p><strong>Output:</strong> <span class="example-io">104</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= piles.length &lt;= 100</code></li>
	<li><code>1 &lt;= piles[i]&nbsp;&lt;= 10<sup>4</sup></code></li>
</ul>


## Hints

1. Use dynamic programming: the states are (i, m) for the answer of piles[i:] and that given m.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

We use dynamic programming with memoization to determine the maximum stones Alice can obtain. The state of our DP is defined as (i, M), which represents the maximum number of stones the current player can collect starting from the i-th pile with the current value of M. Since Alice starts first, we want to find the result of the state (0, 1). To efficiently calculate the number of stones in any range [i, n-1], we precalculate suffix sums where suffixSum[i] is the total stones from the i-th pile to the end.

For each turn, the player can take X piles where 1 <= X <= 2M. Each player's goal is to maximize their stones, which is equivalent to taking the total remaining stones (suffixSum[i]) and subtracting the maximum stones the next player can get from the resulting state (solve(i + X, max(M, X))). The base case occurs when the current player can take all remaining piles (i + 2M >= n), at which point they take all available stones from suffixSum[i].

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

class Solution {
public:
    int stoneGameII(std::vector<int>& piles) {
        int n = piles.size();
        std::vector<int> suffixSum(n + 1, 0);
        for (int i = n - 1; i >= 0; i--) {
            suffixSum[i] = suffixSum[i + 1] + piles[i];
        }
        std::vector<std::vector<int>> memo(n, std::vector<int>(n + 1, 0));
        return solve(0, 1, n, suffixSum, memo);
    }

private:
    int solve(int i, int m, int n, const std::vector<int>& suffixSum, std::vector<std::vector<int>>& memo) {
        if (i + 2 * m >= n) return suffixSum[i];
        if (memo[i][m] != 0) return memo[i][m];

        int res = 0;
        for (int x = 1; x <= 2 * m; x++) {
            int next_m = std::max(m, x);
            res = std::max(res, suffixSum[i] - solve(i + x, next_m, n, suffixSum, memo));
        }
        return memo[i][m] = res;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int stoneGameII(int[] piles) {
        int n = piles.length;
        int[][] memo = new int[n][n + 1];
        int[] suffixSum = new int[n + 1];
        for (int i = n - 1; i >= 0; i--) {
            suffixSum[i] = suffixSum[i + 1] + piles[i];
        }
        return solve(0, 1, n, suffixSum, memo);
    }

    private int solve(int i, int m, int n, int[] suffixSum, int[][] memo) {
        if (i + 2 * m >= n) return suffixSum[i];
        if (memo[i][m] != 0) return memo[i][m];

        int res = 0;
        for (int x = 1; x <= 2 * m; x++) {
            int next_m = Math.max(m, x);
            res = Math.max(res, suffixSum[i] - solve(i + x, next_m, n, suffixSum, memo));
        }
        memo[i][m] = res;
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
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        memo = {}

        def solve(i, m):
            if i + 2 * m >= n:
                return suffix_sum[i]
            if (i, m) in memo:
                return memo[(i, m)]

            res = 0
            for x in range(1, 2 * m + 1):
                res = max(res, suffix_sum[i] - solve(i + x, max(m, x)))
            memo[(i, m)] = res
            return res

        return solve(0, 1)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from functools import lru_cache
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        @lru_cache(None)
        def solve(i, m):
            if i + 2 * m >= n:
                return suffix_sum[i]

            res = 0
            for x in range(1, 2 * m + 1):
                res = max(res, suffix_sum[i] - solve(i + x, max(m, x)))
            return res

        return solve(0, 1)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <string.h>

int solve(int i, int m, int n, int* suffixSum, int memo[101][101]) {
    if (i + 2 * m >= n) return suffixSum[i];
    if (memo[i][m] != 0) return memo[i][m];

    int res = 0;
    for (int x = 1; x <= 2 * m; x++) {
        int next_m = (m > x) ? m : x;
        int current = suffixSum[i] - solve(i + x, next_m, n, suffixSum, memo);
        if (current > res) res = current;
    }
    return memo[i][m] = res;
}

int stoneGameII(int* piles, int pilesSize) {
    int suffixSum[101];
    int memo[101][101];
    memset(memo, 0, sizeof(memo));

    int currentSum = 0;
    for (int i = pilesSize - 1; i >= 0; i--) {
        currentSum += piles[i];
        suffixSum[i] = currentSum;
    }

    return solve(0, 1, pilesSize, suffixSum, memo);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int StoneGameII(int[] piles) {
        int n = piles.Length;
        int[] suffixSum = new int[n + 1];
        for (int i = n - 1; i >= 0; i--) {
            suffixSum[i] = suffixSum[i + 1] + piles[i];
        }
        int[,] memo = new int[n, n + 1];
        return Solve(0, 1, n, suffixSum, memo);
    }

    private int Solve(int i, int m, int n, int[] suffixSum, int[,] memo) {
        if (i + 2 * m >= n) {
            return suffixSum[i];
        }
        if (memo[i, m] != 0) {
            return memo[i, m];
        }
        int res = 0;
        for (int x = 1; x <= 2 * m; x++) {
            res = Math.Max(res, suffixSum[i] - Solve(i + x, Math.Max(m, x), n, suffixSum, memo));
        }
        memo[i, m] = res;
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
 * @param {number[]} piles
 * @return {number}
 */
var stoneGameII = function(piles) {
    const n = piles.length;
    const suffixSum = new Array(n + 1).fill(0);
    for (let i = n - 1; i >= 0; i--) {
        suffixSum[i] = suffixSum[i + 1] + piles[i];
    }
    const memo = Array.from({ length: n }, () => new Array(n + 1).fill(0));

    const solve = function(i, m) {
        if (i + 2 * m >= n) return suffixSum[i];
        if (memo[i][m] !== 0) return memo[i][m];
        let res = 0;
        for (let x = 1; x <= 2 * m; x++) {
            res = Math.max(res, suffixSum[i] - solve(i + x, Math.max(m, x)));
        }
        memo[i][m] = res;
        return res;
    };

    return solve(0, 1);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function stoneGameII(piles: number[]): number {
    const n: number = piles.length;
    const suffixSum: number[] = new Array(n + 1).fill(0);
    for (let i = n - 1; i >= 0; i--) {
        suffixSum[i] = suffixSum[i + 1] + piles[i];
    }
    const memo: number[][] = Array.from({ length: n }, () => new Array(n + 1).fill(0));

    const solve = (i: number, m: number): number => {
        if (i + 2 * m >= n) return suffixSum[i];
        if (memo[i][m] !== 0) return memo[i][m];
        let res: number = 0;
        for (let x = 1; x <= 2 * m; x++) {
            res = Math.max(res, suffixSum[i] - solve(i + x, Math.max(m, x)));
        }
        memo[i][m] = res;
        return res;
    };

    return solve(0, 1);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $piles
     * @return Integer
     */
    function stoneGameII($piles) {
        $n = count($piles);
        $suffixSum = array_fill(0, $n + 1, 0);
        for ($i = $n - 1; $i >= 0; $i--) {
            $suffixSum[$i] = $suffixSum[$i + 1] + $piles[$i];
        }
        $memo = array_fill(0, $n, array_fill(0, $n + 1, 0));
        return $this->solve(0, 1, $n, $suffixSum, $memo);
    }

    private function solve($i, $m, $n, $suffixSum, &$memo) {
        if ($i + 2 * $m >= $n) {
            return $suffixSum[$i];
        }
        if ($memo[$i][$m] != 0) {
            return $memo[$i][$m];
        }
        $res = 0;
        for ($x = 1; $x <= 2 * $m; $x++) {
            $res = max($res, $suffixSum[$i] - $this->solve($i + $x, max($m, $x), $n, $suffixSum, $memo));
        }
        $memo[$i][$m] = $res;
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
    func stoneGameII(_ piles: [Int]) -> Int {
        let n = piles.count
        var suffixSum = [Int](repeating: 0, count: n + 1)
        for i in stride(from: n - 1, through: 0, by: -1) {
            suffixSum[i] = suffixSum[i + 1] + piles[i]
        }
        var memo = [[Int]](repeating: [Int](repeating: 0, count: n + 1), count: n)

        func solve(_ i: Int, _ m: Int) -> Int {
            if i + 2 * m >= n {
                return suffixSum[i]
            }
            if memo[i][m] != 0 {
                return memo[i][m]
            }
            var res = 0
            for x in 1...(2 * m) {
                let nextM = max(m, x)
                let currentScore = suffixSum[i] - solve(i + x, nextM)
                if currentScore > res {
                    res = currentScore
                }
            }
            memo[i][m] = res
            return res
        }

        return solve(0, 1)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import kotlin.math.max

class Solution {
    fun stoneGameII(piles: IntArray): Int {
        val n = piles.size
        val suffixSum = IntArray(n + 1)
        for (i in n - 1 downTo 0) {
            suffixSum[i] = suffixSum[i + 1] + piles[i]
        }
        val memo = Array(n + 1) { IntArray(n + 1) }

        fun solve(i: Int, m: Int): Int {
            if (i + 2 * m >= n) return suffixSum[i]
            if (memo[i][m] != 0) return memo[i][m]

            var res = 0
            for (x in 1..2 * m) {
                val cur = suffixSum[i] - solve(i + x, max(m, x))
                if (cur > res) res = cur
            }
            memo[i][m] = res
            return res
        }

        return solve(0, 1)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:math';

class Solution {
  int stoneGameII(List<int> piles) {
    int n = piles.length;
    List<int> suffixSum = List.filled(n + 1, 0);
    for (int i = n - 1; i >= 0; i--) {
      suffixSum[i] = suffixSum[i + 1] + piles[i];
    }
    List<List<int>> memo = List.generate(n + 1, (_) => List.filled(n + 1, 0));

    int solve(int i, int m) {
      if (i + 2 * m >= n) return suffixSum[i];
      if (memo[i][m] != 0) return memo[i][m];

      int res = 0;
      for (int x = 1; x <= 2 * m; x++) {
        int cur = suffixSum[i] - solve(i + x, max(m, x));
        if (cur > res) res = cur;
      }
      memo[i][m] = res;
      return res;
    }

    return solve(0, 1);
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func stoneGameII(piles []int) int {
	n := len(piles)
	suffixSum := make([]int, n+1)
	for i := n - 1; i >= 0; i-- {
		suffixSum[i] = suffixSum[i+1] + piles[i]
	}
	memo := make([][]int, n+1)
	for i := range memo {
		memo[i] = make([]int, n+1)
	}

	var solve func(int, int) int
	solve = func(i, m int) int {
		if i+2*m >= n {
			return suffixSum[i]
		}
		if memo[i][m] != 0 {
			return memo[i][m]
		}

		res := 0
		for x := 1; x <= 2*m; x++ {
			mNext := m
			if x > mNext {
				mNext = x
			}
			cur := suffixSum[i] - solve(i+x, mNext)
			if cur > res {
				res = cur
			}
		}
		memo[i][m] = res
		return res
	}

	return solve(0, 1)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} piles
# @return {Integer}
def stone_game_ii(piles)
  n = piles.length
  suffix_sum = Array.new(n + 1, 0)
  (n - 1).step(0, -1) { |i| suffix_sum[i] = suffix_sum[i + 1] + piles[i] }
  memo = Array.new(n + 1) { Array.new(n + 1, 0) }

  solve = lambda do |i, m|
    return suffix_sum[i] if i + 2 * m >= n
    return memo[i][m] if memo[i][m] != 0

    res = 0
    (1..(2 * m)).each do |x|
      m_next = m > x ? m : x
      cur = suffix_sum[i] - solve.call(i + x, m_next)
      res = cur if cur > res
    end
    memo[i][m] = res
    res
  end

  solve.call(0, 1)
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.math.max

object Solution {
    def stoneGameII(piles: Array[Int]): Int = {
        val n = piles.length
        val suffixSum = new Array[Int](n + 1)
        for (i <- n - 1 to 0 by -1) {
            suffixSum(i) = suffixSum(i + 1) + piles(i)
        }
        val memo = Array.ofDim[Int](n + 1, n + 1)

        def solve(i: Int, m: Int): Int = {
            if (i + 2 * m >= n) return suffixSum(i)
            if (memo(i)(m) != 0) return memo(i)(m)

            var res = 0
            for (x <- 1 to 2 * m) {
                val cur = suffixSum(i) - solve(i + x, max(m, x))
                if (cur > res) res = cur
            }
            memo(i)(m) = res
            res
        }

        solve(0, 1)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn stone_game_ii(piles: Vec<i32>) -> i32 {
        let n = piles.len();
        let mut suffix_sum = vec![0; n + 1];
        for i in (0..n).rev() {
            suffix_sum[i] = suffix_sum[i + 1] + piles[i];
        }

        let mut dp = vec![vec![0; n + 1]; n + 1];
        for i in (0..=n).rev() {
            for m in 1..=n {
                if i + 2 * m >= n {
                    dp[i][m] = suffix_sum[i];
                } else {
                    let mut min_val = i32::MAX;
                    for x in 1..=(2 * m) {
                        let next_m = std::cmp::min(n, std::cmp::max(m, x));
                        if i + x <= n {
                            min_val = std::cmp::min(min_val, dp[i + x][next_m]);
                        }
                    }
                    dp[i][m] = suffix_sum[i] - min_val;
                }
            }
        }
        dp[0][1]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (stone-game-ii piles)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([n (length piles)]
         [piles-vec (list->vector piles)]
         [suffix-sum (make-vector (+ n 1) 0)])
    (for ([i (in-range (- n 1) -1 -1)])
      (vector-set! suffix-sum i (+ (vector-ref piles-vec i) (vector-ref suffix-sum (+ i 1)))))
    (let ([memo (make-hash)])
      (letrec ([solve (lambda (i m)
                        (let ([m (min m n)])
                          (cond
                            [(>= i n) 0]
                            [(>= (+ i (* 2 m)) n) (vector-ref suffix-sum i)]
                            [(hash-has-key? memo (cons i m)) (hash-ref memo (cons i m))]
                            [else
                             (let* ([res (for/fold ([current-min 2000000000])
                                                  ([x (in-range 1 (+ (* 2 m) 1))])
                                           (min current-min (solve (+ i x) (max m x))))])
                               (let ([val (- (vector-ref suffix-sum i) res)])
                                 (hash-set! memo (cons i m) val)
                                 val))]))])
        (solve 0 1)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec stone_game_ii(Piles :: [integer()]) -> integer().
stone_game_ii(Piles) ->
    N = length(Piles),
    SuffixSums = calculate_suffix_sums(Piles),
    Memo = ets:new(memo_table, [set, private]),
    Result = solve(0, 1, N, SuffixSums, Memo),
    ets:delete(Memo),
    Result.

calculate_suffix_sums(Piles) ->
    SuffixList = lists:foldl(fun(X, [H | _] = Acc) -> [X + H | Acc] end, [0], lists:reverse(Piles)),
    list_to_tuple(SuffixList).

solve(I, M, N, SuffixSums, Memo) ->
    MCapped = min(M, N),
    case ets:lookup(Memo, {I, MCapped}) of
        [{_, Val}] -> Val;
        [] ->
            Res = if
                I >= N -> 0;
                I + 2 * MCapped >= N -> element(I + 1, SuffixSums);
                true ->
                    MinOther = find_min(I, MCapped, 1, 2 * MCapped, N, SuffixSums, Memo, infinity),
                    element(I + 1, SuffixSums) - MinOther
            end,
            ets:insert(Memo, {{I, MCapped}, Res}),
            Res
    end.

find_min(_I, _M, X, MaxX, _N, _SuffixSums, _Memo, MinVal) when X > MaxX -> MinVal;
find_min(I, M, X, MaxX, N, SuffixSums, Memo, MinVal) ->
    Val = solve(I + X, max(M, X), N, SuffixSums, Memo),
    NewMinVal = min(MinVal, Val),
    find_min(I, M, X + 1, MaxX, N, SuffixSums, Memo, NewMinVal).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec stone_game_ii(piles :: [integer]) :: integer
  def stone_game_ii(piles) do
    n = length(piles)
    suffix_sums = calculate_suffix_sums(piles)
    {result, _} = solve(0, 1, n, suffix_sums, %{})
    result
  end

  defp calculate_suffix_sums(piles) do
    piles
    |> Enum.reverse()
    |> Enum.scan(0, fn x, acc -> x + acc end)
    |> Enum.reverse()
    |> (fn sums -> sums ++ [0] end).()
    |> Enum.with_index()
    |> Map.new(fn {s, i} -> {i, s} end)
  end

  defp solve(i, m, n, suffix_sums, memo) do
    m_capped = min(m, n)
    cond do
      Map.has_key?(memo, {i, m_capped}) ->
        {Map.get(memo, {i, m_capped}), memo}
      i + 2 * m_capped >= n ->
        val = Map.get(suffix_sums, i, 0)
        {val, Map.put(memo, {i, m_capped}, val)}
      true ->
        {min_val, updated_memo} = Enum.reduce(1..(2 * m_capped), {nil, memo}, fn x, {curr_min, curr_memo} ->
          {val, new_memo} = solve(i + x, max(m_capped, x), n, suffix_sums, curr_memo)
          new_min = if is_nil(curr_min), do: val, else: min(curr_min, val)
          {new_min, new_memo}
        end)
        res = Map.get(suffix_sums, i) - min_val
        {res, Map.put(updated_memo, {i, m_capped}, res)}
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N^3). There are N possible values for the pile index i and approximately N possible values for M, resulting in O(N^2) states. For each state, we iterate up to 2M times (at most N) to explore all possible moves, giving an overall time complexity of O(N^3).
- **Space Complexity:** O(N^2). We store the results of all (i, M) states in a memoization table of size approximately N x N, which consumes O(N^2) space.
