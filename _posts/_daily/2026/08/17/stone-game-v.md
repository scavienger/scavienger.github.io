---
layout: post
title: "Stone Game V"
date: 2026-08-17 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Math", "Dynamic Programming", "Game Theory"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/stone-game-v/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int stoneGameV(vector<int>& stoneValue) {\n\
        \        int n = stoneValue.size();\n        if (n == 1) return 0;\n\n     \
        \   vector<int> prefixSum(n + 1, 0);\n        for (int i = 0; i < n; i++) {\n\
        \            prefixSum[i + 1] = prefixSum[i] + stoneValue[i];\n        }\n\n\
        \        vector<vector<int>> dp(n, vector<int>(n, 0));\n        vector<vector<int>>\
        \ L(n, vector<int>(n, 0));\n        vector<vector<int>> R(n, vector<int>(n,\
        \ 0));\n\n        for (int i = n - 1; i >= 0; i--) {\n            L[i][i] =\
        \ stoneValue[i];\n            R[i][i] = stoneValue[i];\n            int m =\
        \ i - 1;\n            for (int j = i + 1; j < n; j++) {\n                while\
        \ (m + 1 < j && (prefixSum[m + 2] - prefixSum[i]) <= (prefixSum[j + 1] - prefixSum[m\
        \ + 2])) {\n                    m++;\n                }\n\n                if\
        \ (m < i) {\n                    dp[i][j] = R[i + 1][j];\n                }\
        \ else if (m == j - 1) {\n                    if ((prefixSum[j] - prefixSum[i])\
        \ == (prefixSum[j + 1] - prefixSum[j])) {\n                        dp[i][j]\
        \ = max(L[i][j - 1], R[j][j]);\n                    } else {\n             \
        \           dp[i][j] = L[i][j - 1];\n                    }\n               \
        \ } else {\n                    if ((prefixSum[m + 1] - prefixSum[i]) == (prefixSum[j\
        \ + 1] - prefixSum[m + 1])) {\n                        dp[i][j] = max(L[i][m],\
        \ R[m + 1][j]);\n                    } else {\n                        dp[i][j]\
        \ = max(L[i][m], R[m + 2][j]);\n                    }\n                }\n\n\
        \                int curSum = prefixSum[j + 1] - prefixSum[i];\n           \
        \     L[i][j] = max(L[i][j - 1], curSum + dp[i][j]);\n                R[i][j]\
        \ = max(R[i + 1][j], curSum + dp[i][j]);\n            }\n        }\n       \
        \ return dp[0][n - 1];\n    }\n};"
      java: "class Solution {\n    public int stoneGameV(int[] stoneValue) {\n     \
        \   int n = stoneValue.length;\n        if (n == 1) return 0;\n\n        int[]\
        \ prefixSum = new int[n + 1];\n        for (int i = 0; i < n; i++) {\n     \
        \       prefixSum[i + 1] = prefixSum[i] + stoneValue[i];\n        }\n\n    \
        \    int[][] dp = new int[n][n];\n        int[][] L = new int[n][n];\n     \
        \   int[][] R = new int[n][n];\n\n        for (int i = n - 1; i >= 0; i--) {\n\
        \            L[i][i] = stoneValue[i];\n            R[i][i] = stoneValue[i];\n\
        \            int m = i - 1;\n            for (int j = i + 1; j < n; j++) {\n\
        \                while (m + 1 < j && (prefixSum[m + 2] - prefixSum[i]) <= (prefixSum[j\
        \ + 1] - prefixSum[m + 2])) {\n                    m++;\n                }\n\
        \n                if (m < i) {\n                    dp[i][j] = R[i + 1][j];\n\
        \                } else if (m == j - 1) {\n                    if ((prefixSum[j]\
        \ - prefixSum[i]) == (prefixSum[j + 1] - prefixSum[j])) {\n                \
        \        dp[i][j] = Math.max(L[i][j - 1], R[j][j]);\n                    } else\
        \ {\n                        dp[i][j] = L[i][j - 1];\n                    }\n\
        \                } else {\n                    if ((prefixSum[m + 1] - prefixSum[i])\
        \ == (prefixSum[j + 1] - prefixSum[m + 1])) {\n                        dp[i][j]\
        \ = Math.max(L[i][m], R[m + 1][j]);\n                    } else {\n        \
        \                dp[i][j] = Math.max(L[i][m], R[m + 2][j]);\n              \
        \      }\n                }\n\n                int curSum = prefixSum[j + 1]\
        \ - prefixSum[i];\n                L[i][j] = Math.max(L[i][j - 1], curSum +\
        \ dp[i][j]);\n                R[i][j] = Math.max(R[i + 1][j], curSum + dp[i][j]);\n\
        \            }\n        }\n\n        return dp[0][n - 1];\n    }\n}"
      python: "class Solution(object):\n    def stoneGameV(self, stoneValue):\n    \
        \    \"\"\"\n        :type stoneValue: List[int]\n        :rtype: int\n    \
        \    \"\"\"\n        n = len(stoneValue)\n        if n == 1: return 0\n\n  \
        \      prefix_sum = [0] * (n + 1)\n        for i in range(n):\n            prefix_sum[i\
        \ + 1] = prefix_sum[i] + stoneValue[i]\n\n        dp = [[0] * n for _ in range(n)]\n\
        \        L = [[0] * n for _ in range(n)]\n        R = [[0] * n for _ in range(n)]\n\
        \n        for i in range(n - 1, -1, -1):\n            L[i][i] = stoneValue[i]\n\
        \            R[i][i] = stoneValue[i]\n            m = i - 1\n            for\
        \ j in range(i + 1, n):\n                while m + 1 < j and (prefix_sum[m +\
        \ 2] - prefix_sum[i]) <= (prefix_sum[j + 1] - prefix_sum[m + 2]):\n        \
        \            m += 1\n\n                if m < i:\n                    dp[i][j]\
        \ = R[i + 1][j]\n                elif m == j - 1:\n                    if (prefix_sum[j]\
        \ - prefix_sum[i]) == (prefix_sum[j + 1] - prefix_sum[j]):\n               \
        \         dp[i][j] = max(L[i][j - 1], R[j][j])\n                    else:\n\
        \                        dp[i][j] = L[i][j - 1]\n                else:\n   \
        \                 if (prefix_sum[m + 1] - prefix_sum[i]) == (prefix_sum[j +\
        \ 1] - prefix_sum[m + 1]):\n                        dp[i][j] = max(L[i][m],\
        \ R[m + 1][j])\n                    else:\n                        score = L[i][m]\n\
        \                        if m + 2 <= j:\n                            score =\
        \ max(score, R[m + 2][j])\n                        dp[i][j] = score\n\n    \
        \            cur_sum = prefix_sum[j + 1] - prefix_sum[i]\n                L[i][j]\
        \ = max(L[i][j - 1], cur_sum + dp[i][j])\n                R[i][j] = max(R[i\
        \ + 1][j], cur_sum + dp[i][j])\n\n        return dp[0][n - 1]"
      python3: '// Generation failed for Python3

        // Reason: Parsing failed'
      c: '// Generation failed for C

        // Reason: Parsing failed'
      csharp: '// Generation failed for C#

        // Reason: Parsing failed'
      javascript: '// Generation failed for JavaScript

        // Reason: Parsing failed'
      typescript: '// Generation failed for TypeScript

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      php: '// Generation failed for PHP

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      swift: '// Generation failed for Swift

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      kotlin: '// Generation failed for Kotlin

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      dart: "import 'dart:math' as math;\n\nclass Solution {\n  int stoneGameV(List<int>\
        \ stoneValue) {\n    int n = stoneValue.length;\n    List<int> prefixSum = List.filled(n\
        \ + 1, 0);\n    for (int i = 0; i < n; i++) {\n      prefixSum[i + 1] = prefixSum[i]\
        \ + stoneValue[i];\n    }\n\n    List<List<int>> dp = List.generate(n, (_) =>\
        \ List.filled(n, 0));\n    List<List<int>> f = List.generate(n, (_) => List.filled(n,\
        \ 0));\n    List<List<int>> g = List.generate(n, (_) => List.filled(n, 0));\n\
        \n    for (int i = n - 1; i >= 0; i--) {\n      dp[i][i] = 0;\n      f[i][i]\
        \ = stoneValue[i];\n      g[i][i] = stoneValue[i];\n      int mid = i;\n   \
        \   for (int j = i + 1; j < n; j++) {\n        int totalSum = prefixSum[j +\
        \ 1] - prefixSum[i];\n        while (mid < j - 1 && (prefixSum[mid + 2] - prefixSum[i])\
        \ * 2 <= totalSum) {\n          mid++;\n        }\n\n        if ((prefixSum[mid\
        \ + 1] - prefixSum[i]) * 2 > totalSum) {\n          dp[i][j] = g[i + 1][j];\n\
        \        } else if ((prefixSum[mid + 1] - prefixSum[i]) * 2 == totalSum) {\n\
        \          dp[i][j] = math.max(f[i][mid], g[mid + 1][j]);\n        } else {\n\
        \          dp[i][j] = f[i][mid];\n          if (mid + 2 <= j) {\n          \
        \  dp[i][j] = math.max(dp[i][j], g[mid + 2][j]);\n          }\n        }\n\n\
        \        f[i][j] = math.max(f[i][j - 1], totalSum + dp[i][j]);\n        g[i][j]\
        \ = math.max(g[i + 1][j], totalSum + dp[i][j]);\n      }\n    }\n    return\
        \ dp[0][n - 1];\n  }\n}"
      go: "func stoneGameV(stoneValue []int) int {\n\tn := len(stoneValue)\n\tprefixSum\
        \ := make([]int, n+1)\n\tfor i := 0; i < n; i++ {\n\t\tprefixSum[i+1] = prefixSum[i]\
        \ + stoneValue[i]\n\t}\n\n\tdp := make([][]int, n)\n\tf := make([][]int, n)\n\
        \tg := make([][]int, n)\n\tfor i := range dp {\n\t\tdp[i] = make([]int, n)\n\
        \t\tf[i] = make([]int, n)\n\t\tg[i] = make([]int, n)\n\t}\n\n\tmax := func(a,\
        \ b int) int {\n\t\tif a > b {\n\t\t\treturn a\n\t\t}\n\t\treturn b\n\t}\n\n\
        \tfor i := n - 1; i >= 0; i-- {\n\t\tdp[i][i] = 0\n\t\tf[i][i] = stoneValue[i]\n\
        \t\tg[i][i] = stoneValue[i]\n\t\tmid := i\n\t\tfor j := i + 1; j < n; j++ {\n\
        \t\t\ttotalSum := prefixSum[j+1] - prefixSum[i]\n\t\t\tfor mid < j-1 && (prefixSum[mid+2]-prefixSum[i])*2\
        \ <= totalSum {\n\t\t\t\tmid++\n\t\t\t}\n\n\t\t\tif (prefixSum[mid+1]-prefixSum[i])*2\
        \ > totalSum {\n\t\t\t\tdp[i][j] = g[i+1][j]\n\t\t\t} else if (prefixSum[mid+1]-prefixSum[i])*2\
        \ == totalSum {\n\t\t\t\tdp[i][j] = max(f[i][mid], g[mid+1][j])\n\t\t\t} else\
        \ {\n\t\t\t\tdp[i][j] = f[i][mid]\n\t\t\t\tif mid+2 <= j {\n\t\t\t\t\tdp[i][j]\
        \ = max(dp[i][j], g[mid+2][j])\n\t\t\t\t}\n\t\t\t}\n\n\t\t\tf[i][j] = max(f[i][j-1],\
        \ totalSum+dp[i][j])\n\t\t\tg[i][j] = max(g[i+1][j], totalSum+dp[i][j])\n\t\t\
        }\n\t}\n\treturn dp[0][n-1]\n}"
      ruby: "def stone_game_v(stone_value)\n  n = stone_value.length\n  prefix_sum =\
        \ Array.new(n + 1, 0)\n  n.times { |i| prefix_sum[i + 1] = prefix_sum[i] + stone_value[i]\
        \ }\n\n  dp = Array.new(n) { Array.new(n, 0) }\n  f = Array.new(n) { Array.new(n,\
        \ 0) }\n  g = Array.new(n) { Array.new(n, 0) }\n\n  (n - 1).step(0, -1) do |i|\n\
        \    dp[i][i] = 0\n    f[i][i] = stone_value[i]\n    g[i][i] = stone_value[i]\n\
        \    mid = i\n    (i + 1).upto(n - 1) do |j|\n      total_sum = prefix_sum[j\
        \ + 1] - prefix_sum[i]\n      while mid < j - 1 && (prefix_sum[mid + 2] - prefix_sum[i])\
        \ * 2 <= total_sum\n        mid += 1\n      end\n\n      if (prefix_sum[mid\
        \ + 1] - prefix_sum[i]) * 2 > total_sum\n        dp[i][j] = g[i + 1][j]\n  \
        \    elsif (prefix_sum[mid + 1] - prefix_sum[i]) * 2 == total_sum\n        dp[i][j]\
        \ = [f[i][mid], g[mid + 1][j]].max\n      else\n        res = f[i][mid]\n  \
        \      res = [res, g[mid + 2][j]].max if mid + 2 <= j\n        dp[i][j] = res\n\
        \      end\n\n      f[i][j] = [f[i][j - 1], total_sum + dp[i][j]].max\n    \
        \  g[i][j] = [g[i + 1][j], total_sum + dp[i][j]].max\n    end\n  end\n  dp[0][n\
        \ - 1]\nend"
      scala: "object Solution {\n    def stoneGameV(stoneValue: Array[Int]): Int = {\n\
        \        val n = stoneValue.length\n        val prefixSum = new Array[Int](n\
        \ + 1)\n        for (i <- 0 until n) {\n            prefixSum(i + 1) = prefixSum(i)\
        \ + stoneValue(i)\n        }\n\n        val dp = Array.ofDim[Int](n, n)\n  \
        \      val f = Array.ofDim[Int](n, n)\n        val g = Array.ofDim[Int](n, n)\n\
        \n        for (i <- n - 1 to 0 by -1) {\n            dp(i)(i) = 0\n        \
        \    f(i)(i) = stoneValue(i)\n            g(i)(i) = stoneValue(i)\n        \
        \    var mid = i\n            for (j <- i + 1 until n) {\n                val\
        \ totalSum = prefixSum(j + 1) - prefixSum(i)\n                while (mid < j\
        \ - 1 && (prefixSum(mid + 2) - prefixSum(i)) * 2 <= totalSum) {\n          \
        \          mid += 1\n                }\n\n                if ((prefixSum(mid\
        \ + 1) - prefixSum(i)) * 2 > totalSum) {\n                    dp(i)(j) = g(i\
        \ + 1)(j)\n                } else if ((prefixSum(mid + 1) - prefixSum(i)) *\
        \ 2 == totalSum) {\n                    dp(i)(j) = math.max(f(i)(mid), g(mid\
        \ + 1)(j))\n                } else {\n                    var res = f(i)(mid)\n\
        \                    if (mid + 2 <= j) {\n                        res = math.max(res,\
        \ g(mid + 2)(j))\n                    }\n                    dp(i)(j) = res\n\
        \                }\n\n                f(i)(j) = math.max(f(i)(j - 1), totalSum\
        \ + dp(i)(j))\n                g(i)(j) = math.max(g(i + 1)(j), totalSum + dp(i)(j))\n\
        \            }\n        }\n        dp(0)(n - 1)\n    }\n}"
      rust: "impl Solution {\n    pub fn stone_game_v(stone_value: Vec<i32>) -> i32\
        \ {\n        let n = stone_value.len();\n        if n == 1 {\n            return\
        \ 0;\n        }\n        let mut pref = vec![0; n + 1];\n        for i in 0..n\
        \ {\n            pref[i + 1] = pref[i] + stone_value[i];\n        }\n\n    \
        \    let mut dp = vec![vec![0; n]; n];\n        let mut left = vec![vec![0;\
        \ n]; n];\n        let mut right = vec![vec![0; n]; n];\n\n        for i in\
        \ 0..n {\n            left[i][i] = stone_value[i];\n            right[i][i]\
        \ = stone_value[i];\n        }\n\n        for i in (0..n).rev() {\n        \
        \    let mut m = i;\n            for j in i + 1..n {\n                let total\
        \ = pref[j + 1] - pref[i];\n\n                while m + 1 < j && (pref[m + 2]\
        \ - pref[i]) * 2 <= total {\n                    m += 1;\n                }\n\
        \n                let sum_i_m = pref[m + 1] - pref[i];\n                if sum_i_m\
        \ * 2 > total {\n                    dp[i][j] = right[i + 1][j];\n         \
        \       } else if sum_i_m * 2 == total {\n                    dp[i][j] = std::cmp::max(left[i][m],\
        \ right[m + 1][j]);\n                } else {\n                    let mut res\
        \ = left[i][m];\n                    if m + 1 < j {\n                      \
        \  res = std::cmp::max(res, right[m + 2][j]);\n                    }\n     \
        \               dp[i][j] = res;\n                }\n\n                left[i][j]\
        \ = std::cmp::max(left[i][j - 1], dp[i][j] + total);\n                right[i][j]\
        \ = std::cmp::max(right[i + 1][j], dp[i][j] + total);\n            }\n     \
        \   }\n\n        dp[0][n - 1]\n    }\n}"
      racket: "(define/contract (stone-game-v stoneValue)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let* ([n (length stoneValue)]\n         [sv (list->vector\
        \ stoneValue)]\n         [pref (make-vector (+ n 1) 0)])\n    (for ([i (in-range\
        \ n)])\n      (vector-set! pref (+ i 1) (+ (vector-ref pref i) (vector-ref sv\
        \ i))))\n    (define (get-sum i j)\n      (- (vector-ref pref (+ j 1)) (vector-ref\
        \ pref i)))\n    (let ([dp (make-vector (* n n) 0)]\n          [left (make-vector\
        \ (* n n) 0)]\n          [right (make-vector (* n n) 0)])\n      (define (idx\
        \ i j) (+ (* i n) j))\n      (for ([i (in-range n)])\n        (vector-set! left\
        \ (idx i i) (vector-ref sv i))\n        (vector-set! right (idx i i) (vector-ref\
        \ sv i)))\n      (for ([i (in-range (- n 1) -1 -1)])\n        (let ([m i])\n\
        \          (for ([j (in-range (+ i 1) n)])\n            (let ([total (get-sum\
        \ i j)])\n              (let loop ()\n                (when (and (< (+ m 1)\
        \ j)\n                           (<= (* 2 (get-sum i (+ m 1))) total))\n   \
        \               (set! m (+ m 1))\n                  (loop)))\n             \
        \ (let ([sum-i-m (get-sum i m)])\n                (cond\n                  [(>\
        \ (* 2 sum-i-m) total)\n                   (vector-set! dp (idx i j) (vector-ref\
        \ right (idx (+ i 1) j)))]\n                  [(= (* 2 sum-i-m) total)\n   \
        \                (vector-set! dp (idx i j) (max (vector-ref left (idx i m))\n\
        \                                                 (vector-ref right (idx (+\
        \ m 1) j))))]\n                  [else\n                   (let ([res (vector-ref\
        \ left (idx i m))])\n                     (if (< (+ m 1) j)\n              \
        \           (vector-set! dp (idx i j) (max res (vector-ref right (idx (+ m 2)\
        \ j))))\n                         (vector-set! dp (idx i j) res)))]))\n    \
        \          (vector-set! left (idx i j) (max (vector-ref left (idx i (- j 1)))\n\
        \                                               (+ (vector-ref dp (idx i j))\
        \ total)))\n              (vector-set! right (idx i j) (max (vector-ref right\
        \ (idx (+ i 1) j))\n                                                (+ (vector-ref\
        \ dp (idx i j)) total)))))))\n      (vector-ref dp (idx 0 (- n 1))))))"
      erlang: "-spec stone_game_v(StoneValue :: [integer()]) -> integer().\nstone_game_v(StoneValue)\
        \ ->\n    N = length(StoneValue),\n    if N =:= 1 -> 0;\n       true ->\n  \
        \         SV = list_to_tuple(StoneValue),\n           Pref = list_to_tuple(lists:reverse(lists:foldl(fun(X,\
        \ [H|T]) -> [X+H, H|T] end, [0], StoneValue))),\n           ets:new(dp, [set,\
        \ public, named_table]),\n           ets:new(left, [set, public, named_table]),\n\
        \           ets:new(right, [set, public, named_table]),\n           lists:foreach(fun(I)\
        \ ->\n               Val = element(I+1, SV),\n               ets:insert(dp,\
        \ {{I, I}, 0}),\n               ets:insert(left, {{I, I}, Val}),\n         \
        \      ets:insert(right, {{I, I}, Val})\n           end, lists:seq(0, N-1)),\n\
        \           lists:foreach(fun(I) ->\n               lists:foldl(fun(J, M_In)\
        \ ->\n                   Total = element(J+2, Pref) - element(I+1, Pref),\n\
        \                   M = find_m(I, J, M_In, Total, Pref),\n                 \
        \  SumIM = element(M+2, Pref) - element(I+1, Pref),\n                   Res\
        \ = if\n                       SumIM * 2 > Total ->\n                      \
        \     [{_, RVal}] = ets:lookup(right, {I+1, J}),\n                         \
        \  RVal;\n                       SumIM * 2 =:= Total ->\n                  \
        \         [{_, LVal}] = ets:lookup(left, {I, M}),\n                        \
        \   [{_, RVal2}] = ets:lookup(right, {M+1, J}),\n                          \
        \ erlang:max(LVal, RVal2);\n                       true ->\n               \
        \            [{_, LVal3}] = ets:lookup(left, {I, M}),\n                    \
        \       if M + 1 < J ->\n                               [{_, RVal4}] = ets:lookup(right,\
        \ {M+2, J}),\n                               erlang:max(LVal3, RVal4);\n   \
        \                           true -> LVal3\n                           end\n\
        \                   end,\n                   ets:insert(dp, {{I, J}, Res}),\n\
        \                   [{_, LPrev}] = ets:lookup(left, {I, J-1}),\n           \
        \        ets:insert(left, {{I, J}, erlang:max(LPrev, Res + Total)}),\n     \
        \              [{_, RPrev}] = ets:lookup(right, {I+1, J}),\n               \
        \    ets:insert(right, {{I, J}, erlang:max(RPrev, Res + Total)}),\n        \
        \           M\n               end, I, lists:seq(I+1, N-1))\n           end,\
        \ lists:seq(N-1, 0, -1)),\n           [{_, Ans}] = ets:lookup(dp, {0, N-1}),\n\
        \           ets:delete(dp), ets:delete(left), ets:delete(right),\n         \
        \  Ans\n    end.\n\nfind_m(I, J, M, Total, Pref) ->\n    if\n        M + 1 <\
        \ J, (element(M+3, Pref) - element(I+1, Pref)) * 2 =< Total ->\n           \
        \ find_m(I, J, M+1, Total, Pref);\n        true -> M\n    end."
      elixir: "defmodule Solution do\n  @spec stone_game_v(stone_value :: [integer])\
        \ :: integer\n  def stone_game_v(stone_value) do\n    n = length(stone_value)\n\
        \    if n == 1 do\n      0\n    else\n      sv = List.to_tuple(stone_value)\n\
        \      pref = Enum.reduce(stone_value, [0], fn x, [h | t] -> [x + h, h | t]\
        \ end)\n             |> Enum.reverse()\n             |> List.to_tuple()\n\n\
        \      dp = :ets.new(:dp, [:set, :public])\n      left = :ets.new(:left, [:set,\
        \ :public])\n      right = :ets.new(:right, [:set, :public])\n\n      for i\
        \ <- 0..(n - 1) do\n        :ets.insert(dp, {{i, i}, 0})\n        val = elem(sv,\
        \ i)\n        :ets.insert(left, {{i, i}, val})\n        :ets.insert(right, {{i,\
        \ i}, val})\n      end\n\n      for i <- (n - 1)..0 do\n        Enum.reduce((i\
        \ + 1)..(n - 1), i, fn j, m_curr ->\n          total = elem(pref, j + 1) - elem(pref,\
        \ i)\n          new_m = find_m(i, j, m_curr, total, pref)\n          sum_i_m\
        \ = elem(pref, new_m + 1) - elem(pref, i)\n\n          res = cond do\n     \
        \       sum_i_m * 2 > total ->\n              [{_, val}] = :ets.lookup(right,\
        \ {i + 1, j})\n              val\n            sum_i_m * 2 == total ->\n    \
        \          [{_, l_val}] = :ets.lookup(left, {i, new_m})\n              [{_,\
        \ r_val}] = :ets.lookup(right, {new_m + 1, j})\n              max(l_val, r_val)\n\
        \            true ->\n              [{_, l_val}] = :ets.lookup(left, {i, new_m})\n\
        \              if new_m + 1 < j do\n                [{_, r_val}] = :ets.lookup(right,\
        \ {new_m + 2, j})\n                max(l_val, r_val)\n              else\n \
        \               l_val\n              end\n          end\n\n          :ets.insert(dp,\
        \ {{i, j}, res})\n          [{_, l_prev}] = :ets.lookup(left, {i, j - 1})\n\
        \          :ets.insert(left, {{i, j}, max(l_prev, res + total)})\n         \
        \ [{_, r_prev}] = :ets.lookup(right, {i + 1, j})\n          :ets.insert(right,\
        \ {{i, j}, max(r_prev, res + total)})\n          new_m\n        end)\n     \
        \ end\n\n      [{_, ans}] = :ets.lookup(dp, {0, n - 1})\n      :ets.delete(dp)\n\
        \      :ets.delete(left)\n      :ets.delete(right)\n      ans\n    end\n  end\n\
        \n  defp find_m(i, j, m, total, pref) do\n    if m + 1 < j and (elem(pref, m\
        \ + 2) - elem(pref, i)) * 2 <= total do\n      find_m(i, j, m + 1, total, pref)\n\
        \    else\n      m\n    end\n  end\nend"
    approach: The problem is solved using dynamic programming with an $O(N^2)$ optimization.
      The core idea is to find the maximum score for any subarray $[i, j]$. For each
      split point $k$, Alice keeps the row with the smaller sum. To avoid the $O(N^3)$
      complexity of checking every split point, we observe that for a fixed $i$, as
      $j$ increases, the split point $m$ where the left sum $S_L$ first becomes greater
      than or equal to the right sum $S_R$ moves monotonically. We pre-calculate two
      auxiliary matrices, $L[i][j]$ and $R[i][j]$, which store the maximum possible
      scores Alice can obtain from subarrays starting at $i$ or ending at $j$, respectively,
      considering all previous splits.
    time_complexity: O(N^2) where N is the number of stones. For each starting index
      $i$ (from $N-1$ down to $0$), we iterate through ending indices $j$ (from $i+1$
      up to $N-1$). The split point $m$ moves monotonically forward for each $i$, resulting
      in an amortized $O(1)$ update for each $(i, j)$ pair, leading to a total time
      complexity of $O(N^2)$.
    space_complexity: 'O(N^2) to store the prefix sums and the three matrices: $dp[i][j]$
      (maximum score for the range $[i, j]$), $L[i][j]$ (prefix maximums for splits
      starting at $i$), and $R[i][j]$ (suffix maximums for splits ending at $j$).'
    elapsed_time: 970.7304620742798
    model: gemini-3-flash-preview
    generated_at: '2026-08-17 01:24:01 '
---

## Problem #1563: Stone Game V

**Difficulty:** Hard

**Topics:** Array, Math, Dynamic Programming, Game Theory

## Problem Description

<p>There are several stones <strong>arranged in a row</strong>, and each stone has an associated value which is an integer given in the array <code>stoneValue</code>.</p>

<p>In each round of the game, Alice divides the row into <strong>two non-empty rows</strong> (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice&#39;s score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.</p>

<p>The game ends when there is only <strong>one stone remaining</strong>. Alice&#39;s score is initially <strong>zero</strong>.</p>

<p>Return <i>the maximum score that Alice can obtain</i>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> stoneValue = [6,2,3,4,5,5]
<strong>Output:</strong> 18
<strong>Explanation:</strong> In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has value 14. Bob throws away the right row and Alice&#39;s score is now 11.
In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice&#39;s score becomes 16 (11 + 5).
The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice&#39;s score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> stoneValue = [7,7,7,7,7,7,7]
<strong>Output:</strong> 28
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> stoneValue = [4]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= stoneValue.length &lt;= 500</code></li>
	<li><code>1 &lt;= stoneValue[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## Hints

1. We need to try all possible divisions for the current row to get the max score.

2. As calculating all possible divisions will lead us to calculate some sub-problems more than once, we need to think of dynamic programming.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem is solved using dynamic programming with an $O(N^2)$ optimization. The core idea is to find the maximum score for any subarray $[i, j]$. For each split point $k$, Alice keeps the row with the smaller sum. To avoid the $O(N^3)$ complexity of checking every split point, we observe that for a fixed $i$, as $j$ increases, the split point $m$ where the left sum $S_L$ first becomes greater than or equal to the right sum $S_R$ moves monotonically. We pre-calculate two auxiliary matrices, $L[i][j]$ and $R[i][j]$, which store the maximum possible scores Alice can obtain from subarrays starting at $i$ or ending at $j$, respectively, considering all previous splits.

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
    int stoneGameV(vector<int>& stoneValue) {
        int n = stoneValue.size();
        if (n == 1) return 0;

        vector<int> prefixSum(n + 1, 0);
        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + stoneValue[i];
        }

        vector<vector<int>> dp(n, vector<int>(n, 0));
        vector<vector<int>> L(n, vector<int>(n, 0));
        vector<vector<int>> R(n, vector<int>(n, 0));

        for (int i = n - 1; i >= 0; i--) {
            L[i][i] = stoneValue[i];
            R[i][i] = stoneValue[i];
            int m = i - 1;
            for (int j = i + 1; j < n; j++) {
                while (m + 1 < j && (prefixSum[m + 2] - prefixSum[i]) <= (prefixSum[j + 1] - prefixSum[m + 2])) {
                    m++;
                }

                if (m < i) {
                    dp[i][j] = R[i + 1][j];
                } else if (m == j - 1) {
                    if ((prefixSum[j] - prefixSum[i]) == (prefixSum[j + 1] - prefixSum[j])) {
                        dp[i][j] = max(L[i][j - 1], R[j][j]);
                    } else {
                        dp[i][j] = L[i][j - 1];
                    }
                } else {
                    if ((prefixSum[m + 1] - prefixSum[i]) == (prefixSum[j + 1] - prefixSum[m + 1])) {
                        dp[i][j] = max(L[i][m], R[m + 1][j]);
                    } else {
                        dp[i][j] = max(L[i][m], R[m + 2][j]);
                    }
                }

                int curSum = prefixSum[j + 1] - prefixSum[i];
                L[i][j] = max(L[i][j - 1], curSum + dp[i][j]);
                R[i][j] = max(R[i + 1][j], curSum + dp[i][j]);
            }
        }
        return dp[0][n - 1];
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int stoneGameV(int[] stoneValue) {
        int n = stoneValue.length;
        if (n == 1) return 0;

        int[] prefixSum = new int[n + 1];
        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + stoneValue[i];
        }

        int[][] dp = new int[n][n];
        int[][] L = new int[n][n];
        int[][] R = new int[n][n];

        for (int i = n - 1; i >= 0; i--) {
            L[i][i] = stoneValue[i];
            R[i][i] = stoneValue[i];
            int m = i - 1;
            for (int j = i + 1; j < n; j++) {
                while (m + 1 < j && (prefixSum[m + 2] - prefixSum[i]) <= (prefixSum[j + 1] - prefixSum[m + 2])) {
                    m++;
                }

                if (m < i) {
                    dp[i][j] = R[i + 1][j];
                } else if (m == j - 1) {
                    if ((prefixSum[j] - prefixSum[i]) == (prefixSum[j + 1] - prefixSum[j])) {
                        dp[i][j] = Math.max(L[i][j - 1], R[j][j]);
                    } else {
                        dp[i][j] = L[i][j - 1];
                    }
                } else {
                    if ((prefixSum[m + 1] - prefixSum[i]) == (prefixSum[j + 1] - prefixSum[m + 1])) {
                        dp[i][j] = Math.max(L[i][m], R[m + 1][j]);
                    } else {
                        dp[i][j] = Math.max(L[i][m], R[m + 2][j]);
                    }
                }

                int curSum = prefixSum[j + 1] - prefixSum[i];
                L[i][j] = Math.max(L[i][j - 1], curSum + dp[i][j]);
                R[i][j] = Math.max(R[i + 1][j], curSum + dp[i][j]);
            }
        }

        return dp[0][n - 1];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        n = len(stoneValue)
        if n == 1: return 0

        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]
        L = [[0] * n for _ in range(n)]
        R = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            L[i][i] = stoneValue[i]
            R[i][i] = stoneValue[i]
            m = i - 1
            for j in range(i + 1, n):
                while m + 1 < j and (prefix_sum[m + 2] - prefix_sum[i]) <= (prefix_sum[j + 1] - prefix_sum[m + 2]):
                    m += 1

                if m < i:
                    dp[i][j] = R[i + 1][j]
                elif m == j - 1:
                    if (prefix_sum[j] - prefix_sum[i]) == (prefix_sum[j + 1] - prefix_sum[j]):
                        dp[i][j] = max(L[i][j - 1], R[j][j])
                    else:
                        dp[i][j] = L[i][j - 1]
                else:
                    if (prefix_sum[m + 1] - prefix_sum[i]) == (prefix_sum[j + 1] - prefix_sum[m + 1]):
                        dp[i][j] = max(L[i][m], R[m + 1][j])
                    else:
                        score = L[i][m]
                        if m + 2 <= j:
                            score = max(score, R[m + 2][j])
                        dp[i][j] = score

                cur_sum = prefix_sum[j + 1] - prefix_sum[i]
                L[i][j] = max(L[i][j - 1], cur_sum + dp[i][j])
                R[i][j] = max(R[i + 1][j], cur_sum + dp[i][j])

        return dp[0][n - 1]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
// Generation failed for Python3
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
// Generation failed for C
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
// Generation failed for C#
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
// Generation failed for JavaScript
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
// Generation failed for TypeScript
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
// Generation failed for PHP
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
// Generation failed for Swift
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
// Generation failed for Kotlin
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:math' as math;

class Solution {
  int stoneGameV(List<int> stoneValue) {
    int n = stoneValue.length;
    List<int> prefixSum = List.filled(n + 1, 0);
    for (int i = 0; i < n; i++) {
      prefixSum[i + 1] = prefixSum[i] + stoneValue[i];
    }

    List<List<int>> dp = List.generate(n, (_) => List.filled(n, 0));
    List<List<int>> f = List.generate(n, (_) => List.filled(n, 0));
    List<List<int>> g = List.generate(n, (_) => List.filled(n, 0));

    for (int i = n - 1; i >= 0; i--) {
      dp[i][i] = 0;
      f[i][i] = stoneValue[i];
      g[i][i] = stoneValue[i];
      int mid = i;
      for (int j = i + 1; j < n; j++) {
        int totalSum = prefixSum[j + 1] - prefixSum[i];
        while (mid < j - 1 && (prefixSum[mid + 2] - prefixSum[i]) * 2 <= totalSum) {
          mid++;
        }

        if ((prefixSum[mid + 1] - prefixSum[i]) * 2 > totalSum) {
          dp[i][j] = g[i + 1][j];
        } else if ((prefixSum[mid + 1] - prefixSum[i]) * 2 == totalSum) {
          dp[i][j] = math.max(f[i][mid], g[mid + 1][j]);
        } else {
          dp[i][j] = f[i][mid];
          if (mid + 2 <= j) {
            dp[i][j] = math.max(dp[i][j], g[mid + 2][j]);
          }
        }

        f[i][j] = math.max(f[i][j - 1], totalSum + dp[i][j]);
        g[i][j] = math.max(g[i + 1][j], totalSum + dp[i][j]);
      }
    }
    return dp[0][n - 1];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func stoneGameV(stoneValue []int) int {
	n := len(stoneValue)
	prefixSum := make([]int, n+1)
	for i := 0; i < n; i++ {
		prefixSum[i+1] = prefixSum[i] + stoneValue[i]
	}

	dp := make([][]int, n)
	f := make([][]int, n)
	g := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, n)
		f[i] = make([]int, n)
		g[i] = make([]int, n)
	}

	max := func(a, b int) int {
		if a > b {
			return a
		}
		return b
	}

	for i := n - 1; i >= 0; i-- {
		dp[i][i] = 0
		f[i][i] = stoneValue[i]
		g[i][i] = stoneValue[i]
		mid := i
		for j := i + 1; j < n; j++ {
			totalSum := prefixSum[j+1] - prefixSum[i]
			for mid < j-1 && (prefixSum[mid+2]-prefixSum[i])*2 <= totalSum {
				mid++
			}

			if (prefixSum[mid+1]-prefixSum[i])*2 > totalSum {
				dp[i][j] = g[i+1][j]
			} else if (prefixSum[mid+1]-prefixSum[i])*2 == totalSum {
				dp[i][j] = max(f[i][mid], g[mid+1][j])
			} else {
				dp[i][j] = f[i][mid]
				if mid+2 <= j {
					dp[i][j] = max(dp[i][j], g[mid+2][j])
				}
			}

			f[i][j] = max(f[i][j-1], totalSum+dp[i][j])
			g[i][j] = max(g[i+1][j], totalSum+dp[i][j])
		}
	}
	return dp[0][n-1]
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def stone_game_v(stone_value)
  n = stone_value.length
  prefix_sum = Array.new(n + 1, 0)
  n.times { |i| prefix_sum[i + 1] = prefix_sum[i] + stone_value[i] }

  dp = Array.new(n) { Array.new(n, 0) }
  f = Array.new(n) { Array.new(n, 0) }
  g = Array.new(n) { Array.new(n, 0) }

  (n - 1).step(0, -1) do |i|
    dp[i][i] = 0
    f[i][i] = stone_value[i]
    g[i][i] = stone_value[i]
    mid = i
    (i + 1).upto(n - 1) do |j|
      total_sum = prefix_sum[j + 1] - prefix_sum[i]
      while mid < j - 1 && (prefix_sum[mid + 2] - prefix_sum[i]) * 2 <= total_sum
        mid += 1
      end

      if (prefix_sum[mid + 1] - prefix_sum[i]) * 2 > total_sum
        dp[i][j] = g[i + 1][j]
      elsif (prefix_sum[mid + 1] - prefix_sum[i]) * 2 == total_sum
        dp[i][j] = [f[i][mid], g[mid + 1][j]].max
      else
        res = f[i][mid]
        res = [res, g[mid + 2][j]].max if mid + 2 <= j
        dp[i][j] = res
      end

      f[i][j] = [f[i][j - 1], total_sum + dp[i][j]].max
      g[i][j] = [g[i + 1][j], total_sum + dp[i][j]].max
    end
  end
  dp[0][n - 1]
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def stoneGameV(stoneValue: Array[Int]): Int = {
        val n = stoneValue.length
        val prefixSum = new Array[Int](n + 1)
        for (i <- 0 until n) {
            prefixSum(i + 1) = prefixSum(i) + stoneValue(i)
        }

        val dp = Array.ofDim[Int](n, n)
        val f = Array.ofDim[Int](n, n)
        val g = Array.ofDim[Int](n, n)

        for (i <- n - 1 to 0 by -1) {
            dp(i)(i) = 0
            f(i)(i) = stoneValue(i)
            g(i)(i) = stoneValue(i)
            var mid = i
            for (j <- i + 1 until n) {
                val totalSum = prefixSum(j + 1) - prefixSum(i)
                while (mid < j - 1 && (prefixSum(mid + 2) - prefixSum(i)) * 2 <= totalSum) {
                    mid += 1
                }

                if ((prefixSum(mid + 1) - prefixSum(i)) * 2 > totalSum) {
                    dp(i)(j) = g(i + 1)(j)
                } else if ((prefixSum(mid + 1) - prefixSum(i)) * 2 == totalSum) {
                    dp(i)(j) = math.max(f(i)(mid), g(mid + 1)(j))
                } else {
                    var res = f(i)(mid)
                    if (mid + 2 <= j) {
                        res = math.max(res, g(mid + 2)(j))
                    }
                    dp(i)(j) = res
                }

                f(i)(j) = math.max(f(i)(j - 1), totalSum + dp(i)(j))
                g(i)(j) = math.max(g(i + 1)(j), totalSum + dp(i)(j))
            }
        }
        dp(0)(n - 1)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn stone_game_v(stone_value: Vec<i32>) -> i32 {
        let n = stone_value.len();
        if n == 1 {
            return 0;
        }
        let mut pref = vec![0; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + stone_value[i];
        }

        let mut dp = vec![vec![0; n]; n];
        let mut left = vec![vec![0; n]; n];
        let mut right = vec![vec![0; n]; n];

        for i in 0..n {
            left[i][i] = stone_value[i];
            right[i][i] = stone_value[i];
        }

        for i in (0..n).rev() {
            let mut m = i;
            for j in i + 1..n {
                let total = pref[j + 1] - pref[i];

                while m + 1 < j && (pref[m + 2] - pref[i]) * 2 <= total {
                    m += 1;
                }

                let sum_i_m = pref[m + 1] - pref[i];
                if sum_i_m * 2 > total {
                    dp[i][j] = right[i + 1][j];
                } else if sum_i_m * 2 == total {
                    dp[i][j] = std::cmp::max(left[i][m], right[m + 1][j]);
                } else {
                    let mut res = left[i][m];
                    if m + 1 < j {
                        res = std::cmp::max(res, right[m + 2][j]);
                    }
                    dp[i][j] = res;
                }

                left[i][j] = std::cmp::max(left[i][j - 1], dp[i][j] + total);
                right[i][j] = std::cmp::max(right[i + 1][j], dp[i][j] + total);
            }
        }

        dp[0][n - 1]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (stone-game-v stoneValue)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([n (length stoneValue)]
         [sv (list->vector stoneValue)]
         [pref (make-vector (+ n 1) 0)])
    (for ([i (in-range n)])
      (vector-set! pref (+ i 1) (+ (vector-ref pref i) (vector-ref sv i))))
    (define (get-sum i j)
      (- (vector-ref pref (+ j 1)) (vector-ref pref i)))
    (let ([dp (make-vector (* n n) 0)]
          [left (make-vector (* n n) 0)]
          [right (make-vector (* n n) 0)])
      (define (idx i j) (+ (* i n) j))
      (for ([i (in-range n)])
        (vector-set! left (idx i i) (vector-ref sv i))
        (vector-set! right (idx i i) (vector-ref sv i)))
      (for ([i (in-range (- n 1) -1 -1)])
        (let ([m i])
          (for ([j (in-range (+ i 1) n)])
            (let ([total (get-sum i j)])
              (let loop ()
                (when (and (< (+ m 1) j)
                           (<= (* 2 (get-sum i (+ m 1))) total))
                  (set! m (+ m 1))
                  (loop)))
              (let ([sum-i-m (get-sum i m)])
                (cond
                  [(> (* 2 sum-i-m) total)
                   (vector-set! dp (idx i j) (vector-ref right (idx (+ i 1) j)))]
                  [(= (* 2 sum-i-m) total)
                   (vector-set! dp (idx i j) (max (vector-ref left (idx i m))
                                                 (vector-ref right (idx (+ m 1) j))))]
                  [else
                   (let ([res (vector-ref left (idx i m))])
                     (if (< (+ m 1) j)
                         (vector-set! dp (idx i j) (max res (vector-ref right (idx (+ m 2) j))))
                         (vector-set! dp (idx i j) res)))]))
              (vector-set! left (idx i j) (max (vector-ref left (idx i (- j 1)))
                                               (+ (vector-ref dp (idx i j)) total)))
              (vector-set! right (idx i j) (max (vector-ref right (idx (+ i 1) j))
                                                (+ (vector-ref dp (idx i j)) total)))))))
      (vector-ref dp (idx 0 (- n 1))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec stone_game_v(StoneValue :: [integer()]) -> integer().
stone_game_v(StoneValue) ->
    N = length(StoneValue),
    if N =:= 1 -> 0;
       true ->
           SV = list_to_tuple(StoneValue),
           Pref = list_to_tuple(lists:reverse(lists:foldl(fun(X, [H|T]) -> [X+H, H|T] end, [0], StoneValue))),
           ets:new(dp, [set, public, named_table]),
           ets:new(left, [set, public, named_table]),
           ets:new(right, [set, public, named_table]),
           lists:foreach(fun(I) ->
               Val = element(I+1, SV),
               ets:insert(dp, {{I, I}, 0}),
               ets:insert(left, {{I, I}, Val}),
               ets:insert(right, {{I, I}, Val})
           end, lists:seq(0, N-1)),
           lists:foreach(fun(I) ->
               lists:foldl(fun(J, M_In) ->
                   Total = element(J+2, Pref) - element(I+1, Pref),
                   M = find_m(I, J, M_In, Total, Pref),
                   SumIM = element(M+2, Pref) - element(I+1, Pref),
                   Res = if
                       SumIM * 2 > Total ->
                           [{_, RVal}] = ets:lookup(right, {I+1, J}),
                           RVal;
                       SumIM * 2 =:= Total ->
                           [{_, LVal}] = ets:lookup(left, {I, M}),
                           [{_, RVal2}] = ets:lookup(right, {M+1, J}),
                           erlang:max(LVal, RVal2);
                       true ->
                           [{_, LVal3}] = ets:lookup(left, {I, M}),
                           if M + 1 < J ->
                               [{_, RVal4}] = ets:lookup(right, {M+2, J}),
                               erlang:max(LVal3, RVal4);
                              true -> LVal3
                           end
                   end,
                   ets:insert(dp, {{I, J}, Res}),
                   [{_, LPrev}] = ets:lookup(left, {I, J-1}),
                   ets:insert(left, {{I, J}, erlang:max(LPrev, Res + Total)}),
                   [{_, RPrev}] = ets:lookup(right, {I+1, J}),
                   ets:insert(right, {{I, J}, erlang:max(RPrev, Res + Total)}),
                   M
               end, I, lists:seq(I+1, N-1))
           end, lists:seq(N-1, 0, -1)),
           [{_, Ans}] = ets:lookup(dp, {0, N-1}),
           ets:delete(dp), ets:delete(left), ets:delete(right),
           Ans
    end.

find_m(I, J, M, Total, Pref) ->
    if
        M + 1 < J, (element(M+3, Pref) - element(I+1, Pref)) * 2 =< Total ->
            find_m(I, J, M+1, Total, Pref);
        true -> M
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec stone_game_v(stone_value :: [integer]) :: integer
  def stone_game_v(stone_value) do
    n = length(stone_value)
    if n == 1 do
      0
    else
      sv = List.to_tuple(stone_value)
      pref = Enum.reduce(stone_value, [0], fn x, [h | t] -> [x + h, h | t] end)
             |> Enum.reverse()
             |> List.to_tuple()

      dp = :ets.new(:dp, [:set, :public])
      left = :ets.new(:left, [:set, :public])
      right = :ets.new(:right, [:set, :public])

      for i <- 0..(n - 1) do
        :ets.insert(dp, {{i, i}, 0})
        val = elem(sv, i)
        :ets.insert(left, {{i, i}, val})
        :ets.insert(right, {{i, i}, val})
      end

      for i <- (n - 1)..0 do
        Enum.reduce((i + 1)..(n - 1), i, fn j, m_curr ->
          total = elem(pref, j + 1) - elem(pref, i)
          new_m = find_m(i, j, m_curr, total, pref)
          sum_i_m = elem(pref, new_m + 1) - elem(pref, i)

          res = cond do
            sum_i_m * 2 > total ->
              [{_, val}] = :ets.lookup(right, {i + 1, j})
              val
            sum_i_m * 2 == total ->
              [{_, l_val}] = :ets.lookup(left, {i, new_m})
              [{_, r_val}] = :ets.lookup(right, {new_m + 1, j})
              max(l_val, r_val)
            true ->
              [{_, l_val}] = :ets.lookup(left, {i, new_m})
              if new_m + 1 < j do
                [{_, r_val}] = :ets.lookup(right, {new_m + 2, j})
                max(l_val, r_val)
              else
                l_val
              end
          end

          :ets.insert(dp, {{i, j}, res})
          [{_, l_prev}] = :ets.lookup(left, {i, j - 1})
          :ets.insert(left, {{i, j}, max(l_prev, res + total)})
          [{_, r_prev}] = :ets.lookup(right, {i + 1, j})
          :ets.insert(right, {{i, j}, max(r_prev, res + total)})
          new_m
        end)
      end

      [{_, ans}] = :ets.lookup(dp, {0, n - 1})
      :ets.delete(dp)
      :ets.delete(left)
      :ets.delete(right)
      ans
    end
  end

  defp find_m(i, j, m, total, pref) do
    if m + 1 < j and (elem(pref, m + 2) - elem(pref, i)) * 2 <= total do
      find_m(i, j, m + 1, total, pref)
    else
      m
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N^2) where N is the number of stones. For each starting index $i$ (from $N-1$ down to $0$), we iterate through ending indices $j$ (from $i+1$ up to $N-1$). The split point $m$ moves monotonically forward for each $i$, resulting in an amortized $O(1)$ update for each $(i, j)$ pair, leading to a total time complexity of $O(N^2)$.
- **Space Complexity:** O(N^2) to store the prefix sums and the three matrices: $dp[i][j]$ (maximum score for the range $[i, j]$), $L[i][j]$ (prefix maximums for splits starting at $i$), and $R[i][j]$ (suffix maximums for splits ending at $j$).
