---
layout: post
title: "Maximum Amount of Money Robot Can Earn"
date: 2026-04-02 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Dynamic Programming", "Matrix"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/
ai_solutions:
  - solutions:
      cpp: '// Generation failed for C++

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      java: '// Generation failed for Java

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      python: '// Generation failed for Python

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      python3: '// Generation failed for Python3

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      c: '// Generation failed for C

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      csharp: '// Generation failed for C#

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      javascript: '// Generation failed for JavaScript

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      typescript: "function maximumAmount(coins: number[][]): number {\n    const m\
        \ = coins.length;\n    const n = coins[0].length;\n    const INF = 1e15;\n \
        \   const dp: number[][][] = Array.from({ length: m }, () => \n        Array.from({\
        \ length: n }, () => [-INF, -INF, -INF])\n    );\n\n    for (let i = 0; i <\
        \ m; i++) {\n        for (let j = 0; j < n; j++) {\n            const val =\
        \ coins[i][j];\n            for (let k = 0; k < 3; k++) {\n                if\
        \ (i === 0 && j === 0) {\n                    dp[0][0][0] = val;\n         \
        \           dp[0][0][1] = val < 0 ? 0 : val;\n                    dp[0][0][2]\
        \ = val < 0 ? 0 : val;\n                    continue;\n                }\n\n\
        \                let res = -INF;\n                if (i > 0) res = Math.max(res,\
        \ dp[i - 1][j][k] + val);\n                if (j > 0) res = Math.max(res, dp[i][j\
        \ - 1][k] + val);\n\n                if (k > 0 && val < 0) {\n             \
        \       if (i > 0) res = Math.max(res, dp[i - 1][j][k - 1]);\n             \
        \       if (j > 0) res = Math.max(res, dp[i][j - 1][k - 1]);\n             \
        \   }\n                dp[i][j][k] = res;\n            }\n        }\n    }\n\
        \n    return dp[m - 1][n - 1][2];\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $coins\n     * @return\
        \ Integer\n     */\n    function maximumAmount($coins) {\n        $m = count($coins);\n\
        \        $n = count($coins[0]);\n        $inf = 1e15;\n        $dp = array_fill(0,\
        \ $m, array_fill(0, $n, [-$inf, -$inf, -$inf]));\n\n        for ($i = 0; $i\
        \ < $m; $i++) {\n            for ($j = 0; $j < $n; $j++) {\n               \
        \ $val = $coins[$i][$j];\n                for ($k = 0; $k < 3; $k++) {\n   \
        \                 if ($i == 0 && $j == 0) {\n                        $dp[0][0][0]\
        \ = $val;\n                        $dp[0][0][1] = $val < 0 ? 0 : $val;\n   \
        \                     $dp[0][0][2] = $val < 0 ? 0 : $val;\n                \
        \        continue;\n                    }\n\n                    $res = -$inf;\n\
        \                    if ($i > 0) $res = max($res, $dp[$i - 1][$j][$k] + $val);\n\
        \                    if ($j > 0) $res = max($res, $dp[$i][$j - 1][$k] + $val);\n\
        \n                    if ($k > 0 && $val < 0) {\n                        if\
        \ ($i > 0) $res = max($res, $dp[$i - 1][$j][$k - 1]);\n                    \
        \    if ($j > 0) $res = max($res, $dp[$i][$j - 1][$k - 1]);\n              \
        \      }\n                    $dp[$i][$j][$k] = $res;\n                }\n \
        \           }\n        }\n        return (int)$dp[$m - 1][$n - 1][2];\n    }\n\
        }"
      swift: "class Solution {\n    func maximumAmount(_ coins: [[Int]]) -> Int {\n\
        \        let m = coins.count\n        let n = coins[0].count\n        let inf\
        \ = 1_000_000_000_000_000\n        var dp = Array(repeating: Array(repeating:\
        \ Array(repeating: -inf, count: 3), count: n), count: m)\n\n        for i in\
        \ 0..<m {\n            for j in 0..<n {\n                let val = coins[i][j]\n\
        \                for k in 0..<3 {\n                    if i == 0 && j == 0 {\n\
        \                        dp[0][0][0] = val\n                        dp[0][0][1]\
        \ = val < 0 ? 0 : val\n                        dp[0][0][2] = val < 0 ? 0 : val\n\
        \                        continue\n                    }\n\n               \
        \     var res = -inf\n                    if i > 0 { res = max(res, dp[i - 1][j][k]\
        \ + val) }\n                    if j > 0 { res = max(res, dp[i][j - 1][k] +\
        \ val) }\n\n                    if k > 0 && val < 0 {\n                    \
        \    if i > 0 { res = max(res, dp[i - 1][j][k - 1]) }\n                    \
        \    if j > 0 { res = max(res, dp[i][j - 1][k - 1]) }\n                    }\n\
        \                    dp[i][j][k] = res\n                }\n            }\n \
        \       }\n\n        return dp[m - 1][n - 1][2]\n    }\n}"
      kotlin: "class Solution {\n    fun maximumAmount(coins: Array<IntArray>): Int\
        \ {\n        val m = coins.size\n        val n = coins[0].size\n        val\
        \ INF = 1_000_000_000_000_000L\n        val dp = Array(m) { Array(n) { LongArray(3)\
        \ { -INF } } }\n\n        for (i in 0 until m) {\n            for (j in 0 until\
        \ n) {\n                val value = coins[i][j].toLong()\n                for\
        \ (k in 0..2) {\n                    if (i == 0 && j == 0) {\n             \
        \           dp[0][0][0] = value\n                        dp[0][0][1] = if (value\
        \ < 0) 0L else value\n                        dp[0][0][2] = if (value < 0) 0L\
        \ else value\n                        continue\n                    }\n\n  \
        \                  var res = -INF\n                    if (i > 0) res = maxOf(res,\
        \ dp[i - 1][j][k] + value)\n                    if (j > 0) res = maxOf(res,\
        \ dp[i][j - 1][k] + value)\n\n                    if (k > 0 && value < 0) {\n\
        \                        if (i > 0) res = maxOf(res, dp[i - 1][j][k - 1])\n\
        \                        if (j > 0) res = maxOf(res, dp[i][j - 1][k - 1])\n\
        \                    }\n                    dp[i][j][k] = res\n            \
        \    }\n            }\n        }\n\n        return dp[m - 1][n - 1][2].toInt()\n\
        \    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int maximumAmount(List<List<int>>\
        \ coins) {\n    int m = coins.length;\n    int n = coins[0].length;\n    const\
        \ int inf = 1000000000000000;\n    List<List<List<int>>> dp = List.generate(\n\
        \      m,\n      (_) => List.generate(n, (_) => List.filled(3, -inf)),\n   \
        \ );\n\n    for (int i = 0; i < m; i++) {\n      for (int j = 0; j < n; j++)\
        \ {\n        int val = coins[i][j];\n        for (int k = 0; k < 3; k++) {\n\
        \          if (i == 0 && j == 0) {\n            dp[0][0][0] = val;\n       \
        \     dp[0][0][1] = val < 0 ? 0 : val;\n            dp[0][0][2] = val < 0 ?\
        \ 0 : val;\n            continue;\n          }\n\n          int res = -inf;\n\
        \          if (i > 0) res = max(res, dp[i - 1][j][k] + val);\n          if (j\
        \ > 0) res = max(res, dp[i][j - 1][k] + val);\n\n          if (k > 0 && val\
        \ < 0) {\n            if (i > 0) res = max(res, dp[i - 1][j][k - 1]);\n    \
        \        if (j > 0) res = max(res, dp[i][j - 1][k - 1]);\n          }\n    \
        \      dp[i][j][k] = res;\n        }\n      }\n    }\n\n    return dp[m - 1][n\
        \ - 1][2];\n  }\n}"
      go: "func maximumAmount(coins [][]int) int {\n\tm, n := len(coins), len(coins[0])\n\
        \tconst inf int64 = 1e15\n\tdp := make([][][3]int64, m)\n\tfor i := range dp\
        \ {\n\t\tdp[i] = make([][3]int64, n)\n\t\tfor j := range dp[i] {\n\t\t\tdp[i][j]\
        \ = [3]int64{-inf, -inf, -inf}\n\t\t}\n\t}\n\n\tfor i := 0; i < m; i++ {\n\t\
        \tfor j := 0; j < n; j++ {\n\t\t\tval := int64(coins[i][j])\n\t\t\tfor k :=\
        \ 0; k < 3; k++ {\n\t\t\t\tif i == 0 && j == 0 {\n\t\t\t\t\tdp[0][0][0] = val\n\
        \t\t\t\t\tif val < 0 {\n\t\t\t\t\t\tdp[0][0][1], dp[0][0][2] = 0, 0\n\t\t\t\t\
        \t} else {\n\t\t\t\t\t\tdp[0][0][1], dp[0][0][2] = val, val\n\t\t\t\t\t}\n\t\
        \t\t\t\tcontinue\n\t\t\t\t}\n\n\t\t\t\tvar res int64 = -inf\n\t\t\t\tif i >\
        \ 0 {\n\t\t\t\t\tif dp[i-1][j][k]+val > res { res = dp[i-1][j][k] + val }\n\t\
        \t\t\t}\n\t\t\t\tif j > 0 {\n\t\t\t\t\tif dp[i][j-1][k]+val > res { res = dp[i][j-1][k]\
        \ + val }\n\t\t\t\t}\n\n\t\t\t\tif k > 0 && val < 0 {\n\t\t\t\t\tif i > 0 {\n\
        \t\t\t\t\t\tif dp[i-1][j][k-1] > res { res = dp[i-1][j][k-1] }\n\t\t\t\t\t}\n\
        \t\t\t\t\tif j > 0 {\n\t\t\t\t\t\tif dp[i][j-1][k-1] > res { res = dp[i][j-1][k-1]\
        \ }\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t\tdp[i][j][k] = res\n\t\t\t}\n\t\t}\n\t}\n\
        \n\treturn int(dp[m-1][n-1][2])\n}"
      ruby: "# @param {Integer[][]} coins\n# @return {Integer}\ndef maximum_amount(coins)\n\
        \  m = coins.length\n  n = coins[0].length\n  inf = 10**15\n  dp = Array.new(n)\
        \ { [-inf, -inf, -inf] }\n\n  v00 = coins[0][0]\n  dp[0] = [v00, [v00, 0].max,\
        \ [v00, 0].max]\n\n  (1...n).each do |j|\n    v = coins[0][j]\n    p0, p1, p2\
        \ = dp[j - 1]\n    dp[j] = [p0 + v, [p1 + v, p0].max, [p2 + v, p1].max]\n  end\n\
        \n  (1...m).each do |i|\n    v0 = coins[i][0]\n    t0, t1, t2 = dp[0]\n    dp[0]\
        \ = [t0 + v0, [t1 + v0, t0].max, [t2 + v0, t1].max]\n    (1...n).each do |j|\n\
        \      v = coins[i][j]\n      t0, t1, t2 = dp[j]\n      l0, l1, l2 = dp[j -\
        \ 1]\n      dp[j] = [\n        [t0, l0].max + v,\n        [[t1 + v, t0].max,\
        \ [l1 + v, l0].max].max,\n        [[t2 + v, t1].max, [l2 + v, l1].max].max\n\
        \      ]\n    end\n  end\n\n  dp[n - 1][2]\nend"
      scala: "object Solution {\n    def maximumAmount(coins: Array[Array[Int]]): Int\
        \ = {\n        val m = coins.length\n        val n = coins(0).length\n     \
        \   val dp = Array.fill(m, n, 3)(-1000000000)\n\n        dp(0)(0)(0) = coins(0)(0)\n\
        \        dp(0)(0)(1) = Math.max(0, coins(0)(0))\n        dp(0)(0)(2) = Math.max(0,\
        \ coins(0)(0))\n\n        for (i <- 0 until m; j <- 0 until n) {\n         \
        \   if (!(i == 0 && j == 0)) {\n                val val_at = coins(i)(j)\n \
        \               for (k <- 0 until 3) {\n                    var max_val = -2000000000\n\
        \                    if (i > 0) {\n                        max_val = Math.max(max_val,\
        \ dp(i - 1)(j)(k) + val_at)\n                        if (k > 0) max_val = Math.max(max_val,\
        \ dp(i - 1)(j)(k - 1))\n                    }\n                    if (j > 0)\
        \ {\n                        max_val = Math.max(max_val, dp(i)(j - 1)(k) + val_at)\n\
        \                        if (k > 0) max_val = Math.max(max_val, dp(i)(j - 1)(k\
        \ - 1))\n                    }\n                    dp(i)(j)(k) = max_val\n\
        \                }\n            }\n        }\n        dp(m - 1)(n - 1)(2)\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn maximum_amount(coins: Vec<Vec<i32>>) -> i32\
        \ {\n        let m = coins.len();\n        let n = coins[0].len();\n       \
        \ let mut dp = vec![vec![-1_000_000_000; 3]; n];\n        let v00 = coins[0][0];\n\
        \        dp[0] = vec![v00, v00.max(0), v00.max(0)];\n        for j in 1..n {\n\
        \            let v = coins[0][j];\n            let (p0, p1, p2) = (dp[j - 1][0],\
        \ dp[j - 1][1], dp[j - 1][2]);\n            dp[j] = vec![p0 + v, (p1 + v).max(p0),\
        \ (p2 + v).max(p1)];\n        }\n        for i in 1..m {\n            let v0\
        \ = coins[i][0];\n            let (t0, t1, t2) = (dp[0][0], dp[0][1], dp[0][2]);\n\
        \            dp[0] = vec![t0 + v0, (t1 + v0).max(t0), (t2 + v0).max(t1)];\n\
        \            for j in 1..n {\n                let v = coins[i][j];\n       \
        \         let (t0, t1, t2) = (dp[j][0], dp[j][1], dp[j][2]);\n             \
        \   let (l0, l1, l2) = (dp[j - 1][0], dp[j - 1][1], dp[j - 1][2]);\n       \
        \         dp[j][0] = t0.max(l0) + v;\n                dp[j][1] = (t1 + v).max(t0).max((l1\
        \ + v).max(l0));\n                dp[j][2] = (t2 + v).max(t1).max((l2 + v).max(l1));\n\
        \            }\n        }\n        dp[n - 1][2]\n    }\n}"
      racket: "(define/contract (maximum-amount coins)\n  (-> (listof (listof exact-integer?))\
        \ exact-integer?)\n  (let* ([m (length coins)]\n         [n (length (car coins))]\n\
        \         [coins-vec (list->vector (map list->vector coins))]\n         [dp\
        \ (make-vector n)])\n    (let* ([v00 (vector-ref (vector-ref coins-vec 0) 0)]\n\
        \           [v0 v00]\n           [v1 (max 0 v00)])\n      (vector-set! dp 0\
        \ (vector v0 v1 v1)))\n    (for ([j (in-range 1 n)])\n      (let* ([v (vector-ref\
        \ (vector-ref coins-vec 0) j)]\n             [prev (vector-ref dp (- j 1))])\n\
        \        (vector-set! dp j (vector (+ (vector-ref prev 0) v)\n             \
        \                     (max (+ (vector-ref prev 1) v) (vector-ref prev 0))\n\
        \                                  (max (+ (vector-ref prev 2) v) (vector-ref\
        \ prev 1))))))\n    (for ([i (in-range 1 m)])\n      (let* ([v-col0 (vector-ref\
        \ (vector-ref coins-vec i) 0)]\n             [top0 (vector-ref dp 0)])\n   \
        \     (vector-set! dp 0 (vector (+ (vector-ref top0 0) v-col0)\n           \
        \                       (max (+ (vector-ref top0 1) v-col0) (vector-ref top0\
        \ 0))\n                                  (max (+ (vector-ref top0 2) v-col0)\
        \ (vector-ref top0 1)))))\n      (for ([j (in-range 1 n)])\n        (let* ([v\
        \ (vector-ref (vector-ref coins-vec i) j)]\n               [top (vector-ref\
        \ dp j)]\n               [left (vector-ref dp (- j 1))])\n          (vector-set!\
        \ dp j (vector (+ (max (vector-ref top 0) (vector-ref left 0)) v)\n        \
        \                            (max (max (+ (vector-ref top 1) v) (vector-ref\
        \ top 0))\n                                         (max (+ (vector-ref left\
        \ 1) v) (vector-ref left 0)))\n                                    (max (max\
        \ (+ (vector-ref top 2) v) (vector-ref top 1))\n                           \
        \              (max (+ (vector-ref left 2) v) (vector-ref left 1))))))))\n \
        \   (vector-ref (vector-ref dp (- n 1)) 2)))"
      erlang: "-spec maximum_amount(Coins :: [[integer()]]) -> integer().\nmaximum_amount(Coins)\
        \ ->\n    M = length(Coins),\n    N = length(hd(Coins)),\n    CoinsTuple = list_to_tuple([list_to_tuple(Row)\
        \ || Row <- Coins]),\n    FirstRowList = lists:foldl(fun(J, Acc) ->\n      \
        \  Val = element(J + 1, element(1, CoinsTuple)),\n        if J == 0 -> [{Val,\
        \ max(0, Val), max(0, Val)}];\n           true ->\n               {P0, P1, P2}\
        \ = hd(Acc),\n               [{P0 + Val, max(P1 + Val, P0), max(P2 + Val, P1)}\
        \ | Acc]\n        end\n    end, [], lists:seq(0, N - 1)),\n    FirstRow = list_to_tuple(lists:reverse(FirstRowList)),\n\
        \    FinalRow = lists:foldl(fun(I, PrevRow) ->\n        RowList = lists:foldl(fun(J,\
        \ Acc) ->\n            Val = element(J + 1, element(I + 1, CoinsTuple)),\n \
        \           {T0, T1, T2} = element(J + 1, PrevRow),\n            if J == 0 ->\
        \ [{T0 + Val, max(T1 + Val, T0), max(T2 + Val, T1)}];\n               true ->\n\
        \                   {L0, L1, L2} = hd(Acc),\n                   C0 = max(T0,\
        \ L0) + Val,\n                   C1 = lists:max([T1 + Val, T0, L1 + Val, L0]),\n\
        \                   C2 = lists:max([T2 + Val, T1, L2 + Val, L1]),\n        \
        \           [{C0, C1, C2} | Acc]\n            end\n        end, [], lists:seq(0,\
        \ N - 1)),\n        list_to_tuple(lists:reverse(RowList))\n    end, FirstRow,\
        \ if M > 1 -> lists:seq(1, M - 1); true -> [] end),\n    {_, _, FinalV} = element(N,\
        \ FinalRow),\n    FinalV."
      elixir: "defmodule Solution do\n  @spec maximum_amount(coins :: [[integer]]) ::\
        \ integer\n  def maximum_amount(coins) do\n    m = length(coins)\n    n = length(hd(coins))\n\
        \    coins_tuple = coins |> Enum.map(&List.to_tuple/1) |> List.to_tuple()\n\
        \    first_row = Enum.reduce(0..(n - 1), [], fn j, acc ->\n      val = elem(elem(coins_tuple,\
        \ 0), j)\n      if j == 0 do\n        [{val, max(0, val), max(0, val)}]\n  \
        \    else\n        {p0, p1, p2} = hd(acc)\n        [{p0 + val, max(p1 + val,\
        \ p0), max(p2 + val, p1)} | acc]\n      end\n    end) |> Enum.reverse() |> List.to_tuple()\n\
        \    final_row = if m > 1 do\n      Enum.reduce(1..(m - 1), first_row, fn i,\
        \ prev_row ->\n        Enum.reduce(0..(n - 1), [], fn j, acc ->\n          val\
        \ = elem(elem(coins_tuple, i), j)\n          {t0, t1, t2} = elem(prev_row, j)\n\
        \          if j == 0 do\n            [{t0 + val, max(t1 + val, t0), max(t2 +\
        \ val, t1)}]\n          else\n            {l0, l1, l2} = hd(acc)\n         \
        \   c0 = max(t0, l0) + val\n            c1 = Enum.max([t1 + val, t0, l1 + val,\
        \ l0])\n            c2 = Enum.max([t2 + val, t1, l2 + val, l1])\n          \
        \  [{c0, c1, c2} | acc]\n          end\n        end) |> Enum.reverse() |> List.to_tuple()\n\
        \      end)\n    else\n      first_row\n    end\n    {_, _, final_v} = elem(final_row,\
        \ n - 1)\n    final_v\n  end\nend"
    approach: 'This problem can be solved using dynamic programming by defining a state
      $dp[i][j][k]$, which represents the maximum amount of money the robot can have
      upon reaching cell $(i, j)$ with $k$ neutralizations remaining to be used (or
      $k$ neutralizations already used). Specifically, we use $dp[i][j][k]$ to store
      the maximum profit at row $i$ and column $j$ having used up to $k$ neutralizations
      ($0 \le k \le 2$). Since the robot can only move right or down, the state at $(i,
      j)$ is derived from the states at $(i-1, j)$ and $(i, j-1)$.


      For each cell $(i, j)$, if the value is non-negative, the robot simply adds the
      coins to its current total for all values of $k$. If the cell contains a robber
      (negative value), the robot has two choices: either accept the loss and subtract
      the absolute value from its total, or use one of its available neutralizations
      (if $k > 0$) to skip the loss, effectively treating the cell as having 0 coins.
      The final answer is the maximum profit found at the bottom-right corner $(m-1,
      n-1)$ with at most 2 neutralizations used.'
    time_complexity: O(m * n) where m is the number of rows and n is the number of columns.
      We iterate through each cell of the grid exactly once, and for each cell, we perform
      a constant number of operations (3 states for the number of neutralizations).
    space_complexity: O(m * n) to store the 3D DP table of size m x n x 3. This can
      be optimized to O(n) space since each row only depends on the previous row, but
      O(m * n) is well within the memory limits for m, n <= 500.
    elapsed_time: 176.86431694030762
    model: gemini-3-flash-preview
    generated_at: '2026-04-02 01:53:41 '
---

## Problem #3418: Maximum Amount of Money Robot Can Earn

**Difficulty:** Medium

**Topics:** Array, Dynamic Programming, Matrix

## Problem Description

<p>You are given an <code>m x n</code> grid. A robot starts at the top-left corner of the grid <code>(0, 0)</code> and wants to reach the bottom-right corner <code>(m - 1, n - 1)</code>. The robot can move either right or down at any point in time.</p>

<p>The grid contains a value <code>coins[i][j]</code> in each cell:</p>

<ul>
	<li>If <code>coins[i][j] &gt;= 0</code>, the robot gains that many coins.</li>
	<li>If <code>coins[i][j] &lt; 0</code>, the robot encounters a robber, and the robber steals the <strong>absolute</strong> value of <code>coins[i][j]</code> coins.</li>
</ul>

<p>The robot has a special ability to <strong>neutralize robbers</strong> in at most <strong>2 cells</strong> on its path, preventing them from stealing coins in those cells.</p>

<p><strong>Note:</strong> The robot&#39;s total coins can be negative.</p>

<p>Return the <strong>maximum</strong> profit the robot can gain on the route.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">coins = [[0,1,-1],[1,-2,3],[2,-3,4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">8</span></p>

<p><strong>Explanation:</strong></p>

<p>An optimal path for maximum coins is:</p>

<ol>
	<li>Start at <code>(0, 0)</code> with <code>0</code> coins (total coins = <code>0</code>).</li>
	<li>Move to <code>(0, 1)</code>, gaining <code>1</code> coin (total coins = <code>0 + 1 = 1</code>).</li>
	<li>Move to <code>(1, 1)</code>, where there&#39;s a robber stealing <code>2</code> coins. The robot uses one neutralization here, avoiding the robbery (total coins = <code>1</code>).</li>
	<li>Move to <code>(1, 2)</code>, gaining <code>3</code> coins (total coins = <code>1 + 3 = 4</code>).</li>
	<li>Move to <code>(2, 2)</code>, gaining <code>4</code> coins (total coins = <code>4 + 4 = 8</code>).</li>
</ol>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">coins = [[10,10,10],[10,10,10]]</span></p>

<p><strong>Output:</strong> <span class="example-io">40</span></p>

<p><strong>Explanation:</strong></p>

<p>An optimal path for maximum coins is:</p>

<ol>
	<li>Start at <code>(0, 0)</code> with <code>10</code> coins (total coins = <code>10</code>).</li>
	<li>Move to <code>(0, 1)</code>, gaining <code>10</code> coins (total coins = <code>10 + 10 = 20</code>).</li>
	<li>Move to <code>(0, 2)</code>, gaining another <code>10</code> coins (total coins = <code>20 + 10 = 30</code>).</li>
	<li>Move to <code>(1, 2)</code>, gaining the final <code>10</code> coins (total coins = <code>30 + 10 = 40</code>).</li>
</ol>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == coins.length</code></li>
	<li><code>n == coins[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 500</code></li>
	<li><code>-1000 &lt;= coins[i][j] &lt;= 1000</code></li>
</ul>


## Hints

1. Use Dynamic Programming.

2. Let `dp[i][j][k]` denote the maximum amount of money a robot can earn by starting at cell `(i,j)` and having neutralized `k` robbers.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

This problem can be solved using dynamic programming by defining a state $dp[i][j][k]$, which represents the maximum amount of money the robot can have upon reaching cell $(i, j)$ with $k$ neutralizations remaining to be used (or $k$ neutralizations already used). Specifically, we use $dp[i][j][k]$ to store the maximum profit at row $i$ and column $j$ having used up to $k$ neutralizations ($0 \le k \le 2$). Since the robot can only move right or down, the state at $(i, j)$ is derived from the states at $(i-1, j)$ and $(i, j-1)$.

For each cell $(i, j)$, if the value is non-negative, the robot simply adds the coins to its current total for all values of $k$. If the cell contains a robber (negative value), the robot has two choices: either accept the loss and subtract the absolute value from its total, or use one of its available neutralizations (if $k > 0$) to skip the loss, effectively treating the cell as having 0 coins. The final answer is the maximum profit found at the bottom-right corner $(m-1, n-1)$ with at most 2 neutralizations used.

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
// Generation failed for C++
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
// Generation failed for Java
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
// Generation failed for Python
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
// Generation failed for Python3
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
// Generation failed for C
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
// Generation failed for C#
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
// Generation failed for JavaScript
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maximumAmount(coins: number[][]): number {
    const m = coins.length;
    const n = coins[0].length;
    const INF = 1e15;
    const dp: number[][][] = Array.from({ length: m }, () => 
        Array.from({ length: n }, () => [-INF, -INF, -INF])
    );

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            const val = coins[i][j];
            for (let k = 0; k < 3; k++) {
                if (i === 0 && j === 0) {
                    dp[0][0][0] = val;
                    dp[0][0][1] = val < 0 ? 0 : val;
                    dp[0][0][2] = val < 0 ? 0 : val;
                    continue;
                }

                let res = -INF;
                if (i > 0) res = Math.max(res, dp[i - 1][j][k] + val);
                if (j > 0) res = Math.max(res, dp[i][j - 1][k] + val);

                if (k > 0 && val < 0) {
                    if (i > 0) res = Math.max(res, dp[i - 1][j][k - 1]);
                    if (j > 0) res = Math.max(res, dp[i][j - 1][k - 1]);
                }
                dp[i][j][k] = res;
            }
        }
    }

    return dp[m - 1][n - 1][2];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[][] $coins
     * @return Integer
     */
    function maximumAmount($coins) {
        $m = count($coins);
        $n = count($coins[0]);
        $inf = 1e15;
        $dp = array_fill(0, $m, array_fill(0, $n, [-$inf, -$inf, -$inf]));

        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                $val = $coins[$i][$j];
                for ($k = 0; $k < 3; $k++) {
                    if ($i == 0 && $j == 0) {
                        $dp[0][0][0] = $val;
                        $dp[0][0][1] = $val < 0 ? 0 : $val;
                        $dp[0][0][2] = $val < 0 ? 0 : $val;
                        continue;
                    }

                    $res = -$inf;
                    if ($i > 0) $res = max($res, $dp[$i - 1][$j][$k] + $val);
                    if ($j > 0) $res = max($res, $dp[$i][$j - 1][$k] + $val);

                    if ($k > 0 && $val < 0) {
                        if ($i > 0) $res = max($res, $dp[$i - 1][$j][$k - 1]);
                        if ($j > 0) $res = max($res, $dp[$i][$j - 1][$k - 1]);
                    }
                    $dp[$i][$j][$k] = $res;
                }
            }
        }
        return (int)$dp[$m - 1][$n - 1][2];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maximumAmount(_ coins: [[Int]]) -> Int {
        let m = coins.count
        let n = coins[0].count
        let inf = 1_000_000_000_000_000
        var dp = Array(repeating: Array(repeating: Array(repeating: -inf, count: 3), count: n), count: m)

        for i in 0..<m {
            for j in 0..<n {
                let val = coins[i][j]
                for k in 0..<3 {
                    if i == 0 && j == 0 {
                        dp[0][0][0] = val
                        dp[0][0][1] = val < 0 ? 0 : val
                        dp[0][0][2] = val < 0 ? 0 : val
                        continue
                    }

                    var res = -inf
                    if i > 0 { res = max(res, dp[i - 1][j][k] + val) }
                    if j > 0 { res = max(res, dp[i][j - 1][k] + val) }

                    if k > 0 && val < 0 {
                        if i > 0 { res = max(res, dp[i - 1][j][k - 1]) }
                        if j > 0 { res = max(res, dp[i][j - 1][k - 1]) }
                    }
                    dp[i][j][k] = res
                }
            }
        }

        return dp[m - 1][n - 1][2]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maximumAmount(coins: Array<IntArray>): Int {
        val m = coins.size
        val n = coins[0].size
        val INF = 1_000_000_000_000_000L
        val dp = Array(m) { Array(n) { LongArray(3) { -INF } } }

        for (i in 0 until m) {
            for (j in 0 until n) {
                val value = coins[i][j].toLong()
                for (k in 0..2) {
                    if (i == 0 && j == 0) {
                        dp[0][0][0] = value
                        dp[0][0][1] = if (value < 0) 0L else value
                        dp[0][0][2] = if (value < 0) 0L else value
                        continue
                    }

                    var res = -INF
                    if (i > 0) res = maxOf(res, dp[i - 1][j][k] + value)
                    if (j > 0) res = maxOf(res, dp[i][j - 1][k] + value)

                    if (k > 0 && value < 0) {
                        if (i > 0) res = maxOf(res, dp[i - 1][j][k - 1])
                        if (j > 0) res = maxOf(res, dp[i][j - 1][k - 1])
                    }
                    dp[i][j][k] = res
                }
            }
        }

        return dp[m - 1][n - 1][2].toInt()
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
  int maximumAmount(List<List<int>> coins) {
    int m = coins.length;
    int n = coins[0].length;
    const int inf = 1000000000000000;
    List<List<List<int>>> dp = List.generate(
      m,
      (_) => List.generate(n, (_) => List.filled(3, -inf)),
    );

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        int val = coins[i][j];
        for (int k = 0; k < 3; k++) {
          if (i == 0 && j == 0) {
            dp[0][0][0] = val;
            dp[0][0][1] = val < 0 ? 0 : val;
            dp[0][0][2] = val < 0 ? 0 : val;
            continue;
          }

          int res = -inf;
          if (i > 0) res = max(res, dp[i - 1][j][k] + val);
          if (j > 0) res = max(res, dp[i][j - 1][k] + val);

          if (k > 0 && val < 0) {
            if (i > 0) res = max(res, dp[i - 1][j][k - 1]);
            if (j > 0) res = max(res, dp[i][j - 1][k - 1]);
          }
          dp[i][j][k] = res;
        }
      }
    }

    return dp[m - 1][n - 1][2];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maximumAmount(coins [][]int) int {
	m, n := len(coins), len(coins[0])
	const inf int64 = 1e15
	dp := make([][][3]int64, m)
	for i := range dp {
		dp[i] = make([][3]int64, n)
		for j := range dp[i] {
			dp[i][j] = [3]int64{-inf, -inf, -inf}
		}
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			val := int64(coins[i][j])
			for k := 0; k < 3; k++ {
				if i == 0 && j == 0 {
					dp[0][0][0] = val
					if val < 0 {
						dp[0][0][1], dp[0][0][2] = 0, 0
					} else {
						dp[0][0][1], dp[0][0][2] = val, val
					}
					continue
				}

				var res int64 = -inf
				if i > 0 {
					if dp[i-1][j][k]+val > res { res = dp[i-1][j][k] + val }
				}
				if j > 0 {
					if dp[i][j-1][k]+val > res { res = dp[i][j-1][k] + val }
				}

				if k > 0 && val < 0 {
					if i > 0 {
						if dp[i-1][j][k-1] > res { res = dp[i-1][j][k-1] }
					}
					if j > 0 {
						if dp[i][j-1][k-1] > res { res = dp[i][j-1][k-1] }
					}
				}
				dp[i][j][k] = res
			}
		}
	}

	return int(dp[m-1][n-1][2])
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[][]} coins
# @return {Integer}
def maximum_amount(coins)
  m = coins.length
  n = coins[0].length
  inf = 10**15
  dp = Array.new(n) { [-inf, -inf, -inf] }

  v00 = coins[0][0]
  dp[0] = [v00, [v00, 0].max, [v00, 0].max]

  (1...n).each do |j|
    v = coins[0][j]
    p0, p1, p2 = dp[j - 1]
    dp[j] = [p0 + v, [p1 + v, p0].max, [p2 + v, p1].max]
  end

  (1...m).each do |i|
    v0 = coins[i][0]
    t0, t1, t2 = dp[0]
    dp[0] = [t0 + v0, [t1 + v0, t0].max, [t2 + v0, t1].max]
    (1...n).each do |j|
      v = coins[i][j]
      t0, t1, t2 = dp[j]
      l0, l1, l2 = dp[j - 1]
      dp[j] = [
        [t0, l0].max + v,
        [[t1 + v, t0].max, [l1 + v, l0].max].max,
        [[t2 + v, t1].max, [l2 + v, l1].max].max
      ]
    end
  end

  dp[n - 1][2]
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maximumAmount(coins: Array[Array[Int]]): Int = {
        val m = coins.length
        val n = coins(0).length
        val dp = Array.fill(m, n, 3)(-1000000000)

        dp(0)(0)(0) = coins(0)(0)
        dp(0)(0)(1) = Math.max(0, coins(0)(0))
        dp(0)(0)(2) = Math.max(0, coins(0)(0))

        for (i <- 0 until m; j <- 0 until n) {
            if (!(i == 0 && j == 0)) {
                val val_at = coins(i)(j)
                for (k <- 0 until 3) {
                    var max_val = -2000000000
                    if (i > 0) {
                        max_val = Math.max(max_val, dp(i - 1)(j)(k) + val_at)
                        if (k > 0) max_val = Math.max(max_val, dp(i - 1)(j)(k - 1))
                    }
                    if (j > 0) {
                        max_val = Math.max(max_val, dp(i)(j - 1)(k) + val_at)
                        if (k > 0) max_val = Math.max(max_val, dp(i)(j - 1)(k - 1))
                    }
                    dp(i)(j)(k) = max_val
                }
            }
        }
        dp(m - 1)(n - 1)(2)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn maximum_amount(coins: Vec<Vec<i32>>) -> i32 {
        let m = coins.len();
        let n = coins[0].len();
        let mut dp = vec![vec![-1_000_000_000; 3]; n];
        let v00 = coins[0][0];
        dp[0] = vec![v00, v00.max(0), v00.max(0)];
        for j in 1..n {
            let v = coins[0][j];
            let (p0, p1, p2) = (dp[j - 1][0], dp[j - 1][1], dp[j - 1][2]);
            dp[j] = vec![p0 + v, (p1 + v).max(p0), (p2 + v).max(p1)];
        }
        for i in 1..m {
            let v0 = coins[i][0];
            let (t0, t1, t2) = (dp[0][0], dp[0][1], dp[0][2]);
            dp[0] = vec![t0 + v0, (t1 + v0).max(t0), (t2 + v0).max(t1)];
            for j in 1..n {
                let v = coins[i][j];
                let (t0, t1, t2) = (dp[j][0], dp[j][1], dp[j][2]);
                let (l0, l1, l2) = (dp[j - 1][0], dp[j - 1][1], dp[j - 1][2]);
                dp[j][0] = t0.max(l0) + v;
                dp[j][1] = (t1 + v).max(t0).max((l1 + v).max(l0));
                dp[j][2] = (t2 + v).max(t1).max((l2 + v).max(l1));
            }
        }
        dp[n - 1][2]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (maximum-amount coins)
  (-> (listof (listof exact-integer?)) exact-integer?)
  (let* ([m (length coins)]
         [n (length (car coins))]
         [coins-vec (list->vector (map list->vector coins))]
         [dp (make-vector n)])
    (let* ([v00 (vector-ref (vector-ref coins-vec 0) 0)]
           [v0 v00]
           [v1 (max 0 v00)])
      (vector-set! dp 0 (vector v0 v1 v1)))
    (for ([j (in-range 1 n)])
      (let* ([v (vector-ref (vector-ref coins-vec 0) j)]
             [prev (vector-ref dp (- j 1))])
        (vector-set! dp j (vector (+ (vector-ref prev 0) v)
                                  (max (+ (vector-ref prev 1) v) (vector-ref prev 0))
                                  (max (+ (vector-ref prev 2) v) (vector-ref prev 1))))))
    (for ([i (in-range 1 m)])
      (let* ([v-col0 (vector-ref (vector-ref coins-vec i) 0)]
             [top0 (vector-ref dp 0)])
        (vector-set! dp 0 (vector (+ (vector-ref top0 0) v-col0)
                                  (max (+ (vector-ref top0 1) v-col0) (vector-ref top0 0))
                                  (max (+ (vector-ref top0 2) v-col0) (vector-ref top0 1)))))
      (for ([j (in-range 1 n)])
        (let* ([v (vector-ref (vector-ref coins-vec i) j)]
               [top (vector-ref dp j)]
               [left (vector-ref dp (- j 1))])
          (vector-set! dp j (vector (+ (max (vector-ref top 0) (vector-ref left 0)) v)
                                    (max (max (+ (vector-ref top 1) v) (vector-ref top 0))
                                         (max (+ (vector-ref left 1) v) (vector-ref left 0)))
                                    (max (max (+ (vector-ref top 2) v) (vector-ref top 1))
                                         (max (+ (vector-ref left 2) v) (vector-ref left 1))))))))
    (vector-ref (vector-ref dp (- n 1)) 2)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec maximum_amount(Coins :: [[integer()]]) -> integer().
maximum_amount(Coins) ->
    M = length(Coins),
    N = length(hd(Coins)),
    CoinsTuple = list_to_tuple([list_to_tuple(Row) || Row <- Coins]),
    FirstRowList = lists:foldl(fun(J, Acc) ->
        Val = element(J + 1, element(1, CoinsTuple)),
        if J == 0 -> [{Val, max(0, Val), max(0, Val)}];
           true ->
               {P0, P1, P2} = hd(Acc),
               [{P0 + Val, max(P1 + Val, P0), max(P2 + Val, P1)} | Acc]
        end
    end, [], lists:seq(0, N - 1)),
    FirstRow = list_to_tuple(lists:reverse(FirstRowList)),
    FinalRow = lists:foldl(fun(I, PrevRow) ->
        RowList = lists:foldl(fun(J, Acc) ->
            Val = element(J + 1, element(I + 1, CoinsTuple)),
            {T0, T1, T2} = element(J + 1, PrevRow),
            if J == 0 -> [{T0 + Val, max(T1 + Val, T0), max(T2 + Val, T1)}];
               true ->
                   {L0, L1, L2} = hd(Acc),
                   C0 = max(T0, L0) + Val,
                   C1 = lists:max([T1 + Val, T0, L1 + Val, L0]),
                   C2 = lists:max([T2 + Val, T1, L2 + Val, L1]),
                   [{C0, C1, C2} | Acc]
            end
        end, [], lists:seq(0, N - 1)),
        list_to_tuple(lists:reverse(RowList))
    end, FirstRow, if M > 1 -> lists:seq(1, M - 1); true -> [] end),
    {_, _, FinalV} = element(N, FinalRow),
    FinalV.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec maximum_amount(coins :: [[integer]]) :: integer
  def maximum_amount(coins) do
    m = length(coins)
    n = length(hd(coins))
    coins_tuple = coins |> Enum.map(&List.to_tuple/1) |> List.to_tuple()
    first_row = Enum.reduce(0..(n - 1), [], fn j, acc ->
      val = elem(elem(coins_tuple, 0), j)
      if j == 0 do
        [{val, max(0, val), max(0, val)}]
      else
        {p0, p1, p2} = hd(acc)
        [{p0 + val, max(p1 + val, p0), max(p2 + val, p1)} | acc]
      end
    end) |> Enum.reverse() |> List.to_tuple()
    final_row = if m > 1 do
      Enum.reduce(1..(m - 1), first_row, fn i, prev_row ->
        Enum.reduce(0..(n - 1), [], fn j, acc ->
          val = elem(elem(coins_tuple, i), j)
          {t0, t1, t2} = elem(prev_row, j)
          if j == 0 do
            [{t0 + val, max(t1 + val, t0), max(t2 + val, t1)}]
          else
            {l0, l1, l2} = hd(acc)
            c0 = max(t0, l0) + val
            c1 = Enum.max([t1 + val, t0, l1 + val, l0])
            c2 = Enum.max([t2 + val, t1, l2 + val, l1])
            [{c0, c1, c2} | acc]
          end
        end) |> Enum.reverse() |> List.to_tuple()
      end)
    else
      first_row
    end
    {_, _, final_v} = elem(final_row, n - 1)
    final_v
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(m * n) where m is the number of rows and n is the number of columns. We iterate through each cell of the grid exactly once, and for each cell, we perform a constant number of operations (3 states for the number of neutralizations).
- **Space Complexity:** O(m * n) to store the 3D DP table of size m x n x 3. This can be optimized to O(n) space since each row only depends on the previous row, but O(m * n) is well within the memory limits for m, n <= 500.
