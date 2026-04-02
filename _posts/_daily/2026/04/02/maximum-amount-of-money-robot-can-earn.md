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
      cpp: "class Solution {\npublic:\n    int maximumAmount(vector<vector<int>>& coins)\
        \ {\n        int m = coins.size();\n        int n = coins[0].size();\n     \
        \   vector<vector<vector<long long>>> dp(m, vector<vector<long long>>(n, vector<long\
        \ long>(3, -1e15)));\n\n        dp[0][0][0] = coins[0][0];\n        dp[0][0][1]\
        \ = (coins[0][0] < 0) ? 0 : coins[0][0];\n        dp[0][0][2] = (coins[0][0]\
        \ < 0) ? 0 : coins[0][0];\n\n        for (int i = 0; i < m; ++i) {\n       \
        \     for (int j = 0; j < n; ++j) {\n                if (i == 0 && j == 0) continue;\n\
        \                for (int k = 0; k < 3; ++k) {\n                    long long\
        \ from_up = (i > 0) ? dp[i - 1][j][k] : -1e15;\n                    long long\
        \ from_left = (j > 0) ? dp[i][j - 1][k] : -1e15;\n                    dp[i][j][k]\
        \ = max(from_up, from_left) + coins[i][j];\n\n                    if (k > 0\
        \ && coins[i][j] < 0) {\n                        long long from_up_k = (i >\
        \ 0) ? dp[i - 1][j][k - 1] : -1e15;\n                        long long from_left_k\
        \ = (j > 0) ? dp[i][j - 1][k - 1] : -1e15;\n                        dp[i][j][k]\
        \ = max(dp[i][j][k], max(from_up_k, from_left_k));\n                    }\n\
        \                }\n            }\n        }\n\n        return (int)max({dp[m\
        \ - 1][n - 1][0], dp[m - 1][n - 1][1], dp[m - 1][n - 1][2]});\n    }\n};"
      java: "class Solution {\n    public int maximumAmount(int[][] coins) {\n     \
        \   int m = coins.length;\n        int n = coins[0].length;\n        long[][][]\
        \ dp = new long[m][n][3];\n        for (int i = 0; i < m; i++) {\n         \
        \   for (int j = 0; j < n; j++) {\n                for (int k = 0; k < 3; k++)\
        \ {\n                    dp[i][j][k] = -1000000000000000L;\n               \
        \ }\n            }\n        }\n\n        dp[0][0][0] = coins[0][0];\n      \
        \  dp[0][0][1] = (coins[0][0] < 0) ? 0 : coins[0][0];\n        dp[0][0][2] =\
        \ (coins[0][0] < 0) ? 0 : coins[0][0];\n\n        for (int i = 0; i < m; i++)\
        \ {\n            for (int j = 0; j < n; j++) {\n                if (i == 0 &&\
        \ j == 0) continue;\n                for (int k = 0; k < 3; k++) {\n       \
        \             long fromUp = (i > 0) ? dp[i - 1][j][k] : -1000000000000000L;\n\
        \                    long fromLeft = (j > 0) ? dp[i][j - 1][k] : -1000000000000000L;\n\
        \                    dp[i][j][k] = Math.max(fromUp, fromLeft) + coins[i][j];\n\
        \n                    if (k > 0 && coins[i][j] < 0) {\n                    \
        \    long fromUpK = (i > 0) ? dp[i - 1][j][k - 1] : -1000000000000000L;\n  \
        \                      long fromLeftK = (j > 0) ? dp[i][j - 1][k - 1] : -1000000000000000L;\n\
        \                        dp[i][j][k] = Math.max(dp[i][j][k], Math.max(fromUpK,\
        \ fromLeftK));\n                    }\n                }\n            }\n  \
        \      }\n\n        return (int) Math.max(dp[m - 1][n - 1][0], Math.max(dp[m\
        \ - 1][n - 1][1], dp[m - 1][n - 1][2]));\n    }\n}"
      python: "class Solution(object):\n    def maximumAmount(self, coins):\n      \
        \  \"\"\"\n        :type coins: List[List[int]]\n        :rtype: int\n     \
        \   \"\"\"\n        m = len(coins)\n        n = len(coins[0])\n        dp =\
        \ [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]\n\n        dp[0][0][0]\
        \ = coins[0][0]\n        dp[0][0][1] = max(0, coins[0][0]) if coins[0][0] <\
        \ 0 else coins[0][0]\n        dp[0][0][2] = max(0, coins[0][0]) if coins[0][0]\
        \ < 0 else coins[0][0]\n\n        for i in range(m):\n            for j in range(n):\n\
        \                if i == 0 and j == 0: continue\n                for k in range(3):\n\
        \                    res = -float('inf')\n                    if i > 0: res\
        \ = max(res, dp[i - 1][j][k] + coins[i][j])\n                    if j > 0: res\
        \ = max(res, dp[i][j - 1][k] + coins[i][j])\n                    if k > 0 and\
        \ coins[i][j] < 0:\n                        if i > 0: res = max(res, dp[i -\
        \ 1][j][k - 1])\n                        if j > 0: res = max(res, dp[i][j -\
        \ 1][k - 1])\n                    dp[i][j][k] = res\n\n        return int(max(dp[m\
        \ - 1][n - 1]))"
      python3: "class Solution:\n    def maximumAmount(self, coins: List[List[int]])\
        \ -> int:\n        m = len(coins)\n        n = len(coins[0])\n        dp = [[[-float('inf')]\
        \ * 3 for _ in range(n)] for _ in range(m)]\n\n        dp[0][0][0] = coins[0][0]\n\
        \        dp[0][0][1] = max(0, coins[0][0]) if coins[0][0] < 0 else coins[0][0]\n\
        \        dp[0][0][2] = max(0, coins[0][0]) if coins[0][0] < 0 else coins[0][0]\n\
        \n        for i in range(m):\n            for j in range(n):\n             \
        \   if i == 0 and j == 0: continue\n                for k in range(3):\n   \
        \                 res = -float('inf')\n                    if i > 0: res = max(res,\
        \ dp[i-1][j][k] + coins[i][j])\n                    if j > 0: res = max(res,\
        \ dp[i][j-1][k] + coins[i][j])\n                    if k > 0 and coins[i][j]\
        \ < 0:\n                        if i > 0: res = max(res, dp[i-1][j][k-1])\n\
        \                        if j > 0: res = max(res, dp[i][j-1][k-1])\n       \
        \             dp[i][j][k] = res\n\n        return int(max(dp[m-1][n-1]))"
      c: "#include <stdlib.h>\n#include <limits.h>\n\n#define MAX(a, b) ((a) > (b) ?\
        \ (a) : (b))\n\nint maximumAmount(int** coins, int coinsSize, int* coinsColSize)\
        \ {\n    int m = coinsSize;\n    int n = coinsColSize[0];\n    long long* dp\
        \ = (long long*)malloc((long long)m * n * 3 * sizeof(long long));\n    for (int\
        \ i = 0; i < m * n * 3; i++) dp[i] = -1000000000000000LL;\n\n    dp[0] = (long\
        \ long)coins[0][0];\n    if (coins[0][0] < 0) {\n        dp[1] = 0LL;\n    \
        \    dp[2] = 0LL;\n    } else {\n        dp[1] = (long long)coins[0][0];\n \
        \       dp[2] = (long long)coins[0][0];\n    }\n\n    for (int i = 0; i < m;\
        \ i++) {\n        for (int j = 0; j < n; j++) {\n            if (i == 0 && j\
        \ == 0) continue;\n            for (int k = 0; k < 3; k++) {\n             \
        \   long long from_up = (i > 0) ? dp[((i - 1) * n + j) * 3 + k] : -1000000000000000LL;\n\
        \                long long from_left = (j > 0) ? dp[(i * n + (j - 1)) * 3 +\
        \ k] : -1000000000000000LL;\n                long long current = MAX(from_up,\
        \ from_left) + coins[i][j];\n\n                if (k > 0 && coins[i][j] < 0)\
        \ {\n                    long long neut_up = (i > 0) ? dp[((i - 1) * n + j)\
        \ * 3 + (k - 1)] : -1000000000000000LL;\n                    long long neut_left\
        \ = (j > 0) ? dp[(i * n + (j - 1)) * 3 + (k - 1)] : -1000000000000000LL;\n \
        \                   current = MAX(current, MAX(neut_up, neut_left));\n     \
        \           }\n                dp[(i * n + j) * 3 + k] = current;\n        \
        \    }\n        }\n    }\n\n    long long result = dp[((m - 1) * n + (n - 1))\
        \ * 3 + 0];\n    result = MAX(result, dp[((m - 1) * n + (n - 1)) * 3 + 1]);\n\
        \    result = MAX(result, dp[((m - 1) * n + (n - 1)) * 3 + 2]);\n\n    free(dp);\n\
        \    return (int)result;\n}"
      csharp: "public class Solution {\n    public int MaximumAmount(int[][] coins)\
        \ {\n        int m = coins.Length;\n        int n = coins[0].Length;\n     \
        \   long[,,] dp = new long[m, n, 3];\n\n        for (int i = 0; i < m; i++)\
        \ {\n            for (int j = 0; j < n; j++) {\n                for (int k =\
        \ 0; k < 3; k++) {\n                    dp[i, j, k] = -1000000000000000L;\n\
        \                }\n            }\n        }\n\n        dp[0, 0, 0] = coins[0][0];\n\
        \        dp[0, 0, 1] = (coins[0][0] < 0) ? 0 : coins[0][0];\n        dp[0, 0,\
        \ 2] = (coins[0][0] < 0) ? 0 : coins[0][0];\n\n        for (int i = 0; i < m;\
        \ i++) {\n            for (int j = 0; j < n; j++) {\n                if (i ==\
        \ 0 && j == 0) continue;\n                for (int k = 0; k < 3; k++) {\n  \
        \                  long fromUp = (i > 0) ? dp[i - 1, j, k] : -1000000000000000L;\n\
        \                    long fromLeft = (j > 0) ? dp[i, j - 1, k] : -1000000000000000L;\n\
        \                    dp[i, j, k] = Math.Max(fromUp, fromLeft) + coins[i][j];\n\
        \n                    if (k > 0 && coins[i][j] < 0) {\n                    \
        \    long fromUpK = (i > 0) ? dp[i - 1, j, k - 1] : -1000000000000000L;\n  \
        \                      long fromLeftK = (j > 0) ? dp[i, j - 1, k - 1] : -1000000000000000L;\n\
        \                        dp[i, j, k] = Math.Max(dp[i, j, k], Math.Max(fromUpK,\
        \ fromLeftK));\n                    }\n                }\n            }\n  \
        \      }\n\n        return (int)Math.Max(dp[m - 1, n - 1, 0], Math.Max(dp[m\
        \ - 1, n - 1, 1], dp[m - 1, n - 1, 2]));\n    }\n}"
      javascript: "/**\n * @param {number[][]} coins\n * @return {number}\n */\nvar\
        \ maximumAmount = function(coins) {\n    const m = coins.length;\n    const\
        \ n = coins[0].length;\n    const dp = Array.from({ length: m }, () =>\n   \
        \     Array.from({ length: n }, () => Array(3).fill(-1e15))\n    );\n\n    dp[0][0][0]\
        \ = coins[0][0];\n    dp[0][0][1] = (coins[0][0] < 0) ? 0 : coins[0][0];\n \
        \   dp[0][0][2] = (coins[0][0] < 0) ? 0 : coins[0][0];\n\n    for (let i = 0;\
        \ i < m; i++) {\n        for (let j = 0; j < n; j++) {\n            if (i ===\
        \ 0 && j === 0) continue;\n            for (let k = 0; k < 3; k++) {\n     \
        \           let fromUp = (i > 0) ? dp[i - 1][j][k] : -1e15;\n              \
        \  let fromLeft = (j > 0) ? dp[i][j - 1][k] : -1e15;\n                dp[i][j][k]\
        \ = Math.max(fromUp, fromLeft) + coins[i][j];\n\n                if (k > 0 &&\
        \ coins[i][j] < 0) {\n                    let fromUpK = (i > 0) ? dp[i - 1][j][k\
        \ - 1] : -1e15;\n                    let fromLeftK = (j > 0) ? dp[i][j - 1][k\
        \ - 1] : -1e15;\n                    dp[i][j][k] = Math.max(dp[i][j][k], Math.max(fromUpK,\
        \ fromLeftK));\n                }\n            }\n        }\n    }\n\n    return\
        \ Math.max(...dp[m - 1][n - 1]);\n};"
      typescript: "function maximumAmount(coins: number[][]): number {\n    const m\
        \ = coins.length;\n    const n = coins[0].length;\n    const inf = 100000000000000;\n\
        \    const dp: number[][][] = Array.from({ length: m }, () =>\n        Array.from({\
        \ length: n }, () => [-inf, -inf, -inf])\n    );\n\n    dp[0][0][0] = coins[0][0];\n\
        \    if (coins[0][0] < 0) {\n        dp[0][0][1] = 0;\n    }\n\n    for (let\
        \ i = 0; i < m; i++) {\n        for (let j = 0; j < n; j++) {\n            if\
        \ (i === 0 && j === 0) continue;\n            for (let k = 0; k < 3; k++) {\n\
        \                let prevMax = -inf;\n                if (i > 0) prevMax = Math.max(prevMax,\
        \ dp[i - 1][j][k]);\n                if (j > 0) prevMax = Math.max(prevMax,\
        \ dp[i][j - 1][k]);\n\n                if (prevMax > -inf) {\n             \
        \       dp[i][j][k] = Math.max(dp[i][j][k], prevMax + coins[i][j]);\n      \
        \          }\n\n                if (coins[i][j] < 0 && k > 0) {\n          \
        \          let prevMaxK = -inf;\n                    if (i > 0) prevMaxK = Math.max(prevMaxK,\
        \ dp[i - 1][j][k - 1]);\n                    if (j > 0) prevMaxK = Math.max(prevMaxK,\
        \ dp[i][j - 1][k - 1]);\n                    if (prevMaxK > -inf) {\n      \
        \                  dp[i][j][k] = Math.max(dp[i][j][k], prevMaxK);\n        \
        \            }\n                }\n            }\n        }\n    }\n    return\
        \ Math.max(dp[m - 1][n - 1][0], dp[m - 1][n - 1][1], dp[m - 1][n - 1][2]);\n\
        }"
      php: "class Solution {\n    /**\n     * @param Integer[][] $coins\n     * @return\
        \ Integer\n     */\n    function maximumAmount($coins) {\n        $m = count($coins);\n\
        \        $n = count($coins[0]);\n        $inf = 100000000000000;\n        $dp\
        \ = array_fill(0, $m, array_fill(0, $n, array_fill(0, 3, -$inf)));\n\n     \
        \   $dp[0][0][0] = $coins[0][0];\n        if ($coins[0][0] < 0) {\n        \
        \    $dp[0][0][1] = 0;\n        }\n\n        for ($i = 0; $i < $m; $i++) {\n\
        \            for ($j = 0; $j < $n; $j++) {\n                if ($i == 0 && $j\
        \ == 0) continue;\n                for ($k = 0; $k < 3; $k++) {\n          \
        \          $prevMax = -$inf;\n                    if ($i > 0) $prevMax = max($prevMax,\
        \ $dp[$i - 1][$j][$k]);\n                    if ($j > 0) $prevMax = max($prevMax,\
        \ $dp[$i][$j - 1][$k]);\n\n                    if ($prevMax > -$inf) {\n   \
        \                     $dp[$i][$j][$k] = max($dp[$i][$j][$k], $prevMax + $coins[$i][$j]);\n\
        \                    }\n\n                    if ($coins[$i][$j] < 0 && $k >\
        \ 0) {\n                        $prevMaxK = -$inf;\n                       \
        \ if ($i > 0) $prevMaxK = max($prevMaxK, $dp[$i - 1][$j][$k - 1]);\n       \
        \                 if ($j > 0) $prevMaxK = max($prevMaxK, $dp[$i][$j - 1][$k\
        \ - 1]);\n                        if ($prevMaxK > -$inf) {\n               \
        \             $dp[$i][$j][$k] = max($dp[$i][$j][$k], $prevMaxK);\n         \
        \               }\n                    }\n                }\n            }\n\
        \        }\n\n        return max($dp[$m - 1][$n - 1][0], $dp[$m - 1][$n - 1][1],\
        \ $dp[$m - 1][$n - 1][2]);\n    }\n}"
      swift: "class Solution {\n    func maximumAmount(_ coins: [[Int]]) -> Int {\n\
        \        let m = coins.count\n        let n = coins[0].count\n        let inf\
        \ = 100000000000000\n        var dp = Array(repeating: Array(repeating: Array(repeating:\
        \ -inf, count: 3), count: n), count: m)\n\n        dp[0][0][0] = coins[0][0]\n\
        \        if coins[0][0] < 0 {\n            dp[0][0][1] = 0\n        }\n\n  \
        \      for i in 0..<m {\n            for j in 0..<n {\n                if i\
        \ == 0 && j == 0 { continue }\n                for k in 0..<3 {\n          \
        \          var prevMax = -inf\n                    if i > 0 { prevMax = max(prevMax,\
        \ dp[i - 1][j][k]) }\n                    if j > 0 { prevMax = max(prevMax,\
        \ dp[i][j - 1][k]) }\n\n                    if prevMax > -inf {\n          \
        \              dp[i][j][k] = max(dp[i][j][k], prevMax + coins[i][j])\n     \
        \               }\n\n                    if coins[i][j] < 0 && k > 0 {\n   \
        \                     var prevMaxK = -inf\n                        if i > 0\
        \ { prevMaxK = max(prevMaxK, dp[i - 1][j][k - 1]) }\n                      \
        \  if j > 0 { prevMaxK = max(prevMaxK, dp[i][j - 1][k - 1]) }\n            \
        \            if prevMaxK > -inf {\n                            dp[i][j][k] =\
        \ max(dp[i][j][k], prevMaxK)\n                        }\n                  \
        \  }\n                }\n            }\n        }\n\n        return max(dp[m\
        \ - 1][n - 1][0], max(dp[m - 1][n - 1][1], dp[m - 1][n - 1][2]))\n    }\n}"
      kotlin: "class Solution {\n    fun maximumAmount(coins: Array<IntArray>): Int\
        \ {\n        val m = coins.size\n        val n = coins[0].size\n        val\
        \ inf = 100000000000000L\n        val dp = Array(m) { Array(n) { LongArray(3)\
        \ { -inf } } }\n\n        dp[0][0][0] = coins[0][0].toLong()\n        if (coins[0][0]\
        \ < 0) {\n            dp[0][0][1] = 0L\n        }\n\n        for (i in 0 until\
        \ m) {\n            for (j in 0 until n) {\n                if (i == 0 && j\
        \ == 0) continue\n                for (k in 0 until 3) {\n                 \
        \   var prevMax = -inf\n                    if (i > 0) prevMax = maxOf(prevMax,\
        \ dp[i - 1][j][k])\n                    if (j > 0) prevMax = maxOf(prevMax,\
        \ dp[i][j - 1][k])\n\n                    if (prevMax > -inf) {\n          \
        \              dp[i][j][k] = maxOf(dp[i][j][k], prevMax + coins[i][j])\n   \
        \                 }\n\n                    if (coins[i][j] < 0 && k > 0) {\n\
        \                        var prevMaxK = -inf\n                        if (i\
        \ > 0) prevMaxK = maxOf(prevMaxK, dp[i - 1][j][k - 1])\n                   \
        \     if (j > 0) prevMaxK = maxOf(prevMaxK, dp[i][j - 1][k - 1])\n         \
        \               if (prevMaxK > -inf) {\n                            dp[i][j][k]\
        \ = maxOf(dp[i][j][k], prevMaxK)\n                        }\n              \
        \      }\n                }\n            }\n        }\n\n        val res = maxOf(dp[m\
        \ - 1][n - 1][0], maxOf(dp[m - 1][n - 1][1], dp[m - 1][n - 1][2]))\n       \
        \ return res.toInt()\n    }\n}"
      dart: "class Solution {\n  int maximumAmount(List<List<int>> coins) {\n    int\
        \ m = coins.length;\n    int n = coins[0].length;\n    const int inf = 1000000000000000;\n\
        \    List<List<List<int>>> dp = List.generate(\n        m, (i) => List.generate(n,\
        \ (j) => List.filled(3, -inf)));\n\n    dp[0][0][0] = coins[0][0];\n    if (coins[0][0]\
        \ < 0) {\n      dp[0][0][1] = 0;\n    }\n\n    for (int i = 0; i < m; i++) {\n\
        \      for (int j = 0; j < n; j++) {\n        if (i == 0 && j == 0) continue;\n\
        \        for (int k = 0; k < 3; k++) {\n          int prevMax = -inf;\n    \
        \      if (i > 0) if (dp[i - 1][j][k] > prevMax) prevMax = dp[i - 1][j][k];\n\
        \          if (j > 0) if (dp[i][j - 1][k] > prevMax) prevMax = dp[i][j - 1][k];\n\
        \n          if (prevMax > -inf) {\n            int val = prevMax + coins[i][j];\n\
        \            if (val > dp[i][j][k]) dp[i][j][k] = val;\n          }\n\n    \
        \      if (coins[i][j] < 0 && k > 0) {\n            int prevMaxK = -inf;\n \
        \           if (i > 0) if (dp[i - 1][j][k - 1] > prevMaxK) prevMaxK = dp[i -\
        \ 1][j][k - 1];\n            if (j > 0) if (dp[i][j - 1][k - 1] > prevMaxK)\
        \ prevMaxK = dp[i][j - 1][k - 1];\n            if (prevMaxK > -inf) {\n    \
        \          if (prevMaxK > dp[i][j][k]) dp[i][j][k] = prevMaxK;\n           \
        \ }\n          }\n        }\n      }\n    }\n\n    int res = dp[m - 1][n - 1][0];\n\
        \    if (dp[m - 1][n - 1][1] > res) res = dp[m - 1][n - 1][1];\n    if (dp[m\
        \ - 1][n - 1][2] > res) res = dp[m - 1][n - 1][2];\n    return res;\n  }\n}"
      go: "func maximumAmount(coins [][]int) int {\n\tm := len(coins)\n\tn := len(coins[0])\n\
        \tconst inf = 1000000000000000\n\tdp := make([][][3]int, m)\n\tfor i := 0; i\
        \ < m; i++ {\n\t\tdp[i] = make([][3]int, n)\n\t\tfor j := 0; j < n; j++ {\n\t\
        \t\tdp[i][j] = [3]int{-inf, -inf, -inf}\n\t\t}\n\t}\n\n\tdp[0][0][0] = coins[0][0]\n\
        \tif coins[0][0] < 0 {\n\t\tdp[0][0][1] = 0\n\t}\n\n\tfor i := 0; i < m; i++\
        \ {\n\t\tfor j := 0; j < n; j++ {\n\t\t\tif i == 0 && j == 0 {\n\t\t\t\tcontinue\n\
        \t\t\t}\n\t\t\tfor k := 0; k < 3; k++ {\n\t\t\t\tprevMax := -inf\n\t\t\t\tif\
        \ i > 0 && dp[i-1][j][k] > prevMax {\n\t\t\t\t\tprevMax = dp[i-1][j][k]\n\t\t\
        \t\t}\n\t\t\t\tif j > 0 && dp[i][j-1][k] > prevMax {\n\t\t\t\t\tprevMax = dp[i][j-1][k]\n\
        \t\t\t\t}\n\n\t\t\t\tif prevMax > -inf {\n\t\t\t\t\tif prevMax+coins[i][j] >\
        \ dp[i][j][k] {\n\t\t\t\t\t\tdp[i][j][k] = prevMax + coins[i][j]\n\t\t\t\t\t\
        }\n\t\t\t\t}\n\n\t\t\t\tif coins[i][j] < 0 && k > 0 {\n\t\t\t\t\tprevMaxK :=\
        \ -inf\n\t\t\t\tif i > 0 && dp[i-1][j][k-1] > prevMaxK {\n\t\t\t\t\tprevMaxK\
        \ = dp[i-1][j][k-1]\n\t\t\t\t}\n\t\t\t\tif j > 0 && dp[i][j-1][k-1] > prevMaxK\
        \ {\n\t\t\t\t\tprevMaxK = dp[i][j-1][k-1]\n\t\t\t\t}\n\t\t\t\t\tif prevMaxK\
        \ > -inf {\n\t\t\t\t\t\tif prevMaxK > dp[i][j][k] {\n\t\t\t\t\t\t\tdp[i][j][k]\
        \ = prevMaxK\n\t\t\t\t\t\t}\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\t}\n\n\
        \tres := dp[m-1][n-1][0]\n\tif dp[m-1][n-1][1] > res {\n\t\tres = dp[m-1][n-1][1]\n\
        \t}\n\tif dp[m-1][n-1][2] > res {\n\t\tres = dp[m-1][n-1][2]\n\t}\n\treturn\
        \ res\n}"
      ruby: "def maximum_amount(coins)\n  m = coins.length\n  n = coins[0].length\n\
        \  inf = 1_000_000_000\n  dp = Array.new(n) { Array.new(3, -inf) }\n\n  v00\
        \ = coins[0][0]\n  dp[0][0] = v00\n  dp[0][1] = [v00, 0].max\n  dp[0][2] = [v00,\
        \ 0].max\n\n  (1...n).each do |j|\n    val = coins[0][j]\n    dp[j][0] = dp[j-1][0]\
        \ + val\n    dp[j][1] = [dp[j-1][1] + val, (val < 0 ? dp[j-1][0] : -inf)].max\n\
        \    dp[j][2] = [dp[j-1][2] + val, (val < 0 ? dp[j-1][1] : -inf)].max\n  end\n\
        \n  (1...m).each do |i|\n    val_first = coins[i][0]\n    dp[0][2] = [dp[0][2]\
        \ + val_first, (val_first < 0 ? dp[0][1] : -inf)].max\n    dp[0][1] = [dp[0][1]\
        \ + val_first, (val_first < 0 ? dp[0][0] : -inf)].max\n    dp[0][0] = dp[0][0]\
        \ + val_first\n\n    (1...n).each do |j|\n      val = coins[i][j]\n      prev0\
        \ = [dp[j][0], dp[j-1][0]].max\n      prev1 = [dp[j][1], dp[j-1][1]].max\n \
        \     prev2 = [dp[j][2], dp[j-1][2]].max\n\n      new0 = prev0 + val\n     \
        \ new1 = [prev1 + val, (val < 0 ? prev0 : -inf)].max\n      new2 = [prev2 +\
        \ val, (val < 0 ? prev1 : -inf)].max\n\n      dp[j][0], dp[j][1], dp[j][2] =\
        \ new0, new1, new2\n    end\n  end\n\n  dp[n-1].max\nend"
      scala: "object Solution {\n  def maximumAmount(coins: Array[Array[Int]]): Int\
        \ = {\n    val m = coins.length\n    val n = coins(0).length\n    val INF =\
        \ 1000000000\n    val dp = Array.fill(n)(Array.fill(3)(-INF))\n\n    val v00\
        \ = coins(0)(0)\n    dp(0)(0) = v00\n    dp(0)(1) = Math.max(v00, 0)\n    dp(0)(2)\
        \ = Math.max(v00, 0)\n\n    for (j <- 1 until n) {\n      val v = coins(0)(j)\n\
        \      dp(j)(0) = dp(j - 1)(0) + v\n      dp(j)(1) = Math.max(dp(j - 1)(1) +\
        \ v, if (v < 0) dp(j - 1)(0) else -INF)\n      dp(j)(2) = Math.max(dp(j - 1)(2)\
        \ + v, if (v < 0) dp(j - 1)(1) else -INF)\n    }\n\n    for (i <- 1 until m)\
        \ {\n      val v0 = coins(i)(0)\n      val old0 = dp(0)(0)\n      val old1 =\
        \ dp(0)(1)\n      val old2 = dp(0)(2)\n      dp(0)(2) = Math.max(old2 + v0,\
        \ if (v0 < 0) old1 else -INF)\n      dp(0)(1) = Math.max(old1 + v0, if (v0 <\
        \ 0) old0 else -INF)\n      dp(0)(0) = old0 + v0\n\n      for (j <- 1 until\
        \ n) {\n        val v = coins(i)(j)\n        val up0 = dp(j)(0)\n        val\
        \ up1 = dp(j)(1)\n        val up2 = dp(j)(2)\n        val left0 = dp(j - 1)(0)\n\
        \        val left1 = dp(j - 1)(1)\n        val left2 = dp(j - 1)(2)\n\n    \
        \    val p0 = Math.max(up0, left0)\n        val p1 = Math.max(up1, left1)\n\
        \        val p2 = Math.max(up2, left2)\n\n        dp(j)(0) = p0 + v\n      \
        \  dp(j)(1) = Math.max(p1 + v, if (v < 0) p0 else -INF)\n        dp(j)(2) =\
        \ Math.max(p2 + v, if (v < 0) p1 else -INF)\n      }\n    }\n    dp(n - 1).max\n\
        \  }\n}"
      rust: "impl Solution {\n    pub fn maximum_amount(coins: Vec<Vec<i32>>) -> i32\
        \ {\n        let m = coins.len();\n        let n = coins[0].len();\n       \
        \ let inf = 1_000_000_000;\n        let mut dp = vec![vec![-inf; 3]; n];\n\n\
        \        let v00 = coins[0][0];\n        dp[0][0] = v00;\n        dp[0][1] =\
        \ v00.max(0);\n        dp[0][2] = v00.max(0);\n\n        for j in 1..n {\n \
        \           let val = coins[0][j];\n            dp[j][0] = dp[j-1][0] + val;\n\
        \            dp[j][1] = (dp[j-1][1] + val).max(if val < 0 { dp[j-1][0] } else\
        \ { -inf });\n            dp[j][2] = (dp[j-1][2] + val).max(if val < 0 { dp[j-1][1]\
        \ } else { -inf });\n        }\n\n        for i in 1..m {\n            let v0\
        \ = coins[i][0];\n            let old0 = dp[0][0];\n            let old1 = dp[0][1];\n\
        \            let old2 = dp[0][2];\n            dp[0][2] = (old2 + v0).max(if\
        \ v0 < 0 { old1 } else { -inf });\n            dp[0][1] = (old1 + v0).max(if\
        \ v0 < 0 { old0 } else { -inf });\n            dp[0][0] = old0 + v0;\n\n   \
        \         for j in 1..n {\n                let val = coins[i][j];\n        \
        \        let p0 = dp[j][0].max(dp[j-1][0]);\n                let p1 = dp[j][1].max(dp[j-1][1]);\n\
        \                let p2 = dp[j][2].max(dp[j-1][2]);\n\n                dp[j][0]\
        \ = p0 + val;\n                dp[j][1] = (p1 + val).max(if val < 0 { p0 } else\
        \ { -inf });\n                dp[j][2] = (p2 + val).max(if val < 0 { p1 } else\
        \ { -inf });\n            }\n        }\n\n        *dp[n-1].iter().max().unwrap()\n\
        \    }\n}"
      racket: "(define/contract (maximum-amount coins)\n  (-> (listof (listof exact-integer?))\
        \ exact-integer?)\n  (let* ([m (length coins)]\n         [n (length (car coins))]\n\
        \         [coins-vec (list->vector (map list->vector coins))]\n         [INF\
        \ 1000000000]\n         [dp (make-vector n)])\n    (for ([j (in-range n)])\n\
        \      (vector-set! dp j (vector (- INF) (- INF) (- INF))))\n    (let ([v00\
        \ (vector-ref (vector-ref coins-vec 0) 0)])\n      (vector-set! dp 0 (vector\
        \ v00 (max v00 0) (max v00 0))))\n    (for ([j (in-range 1 n)])\n      (let*\
        \ ([v (vector-ref (vector-ref coins-vec 0) j)]\n             [prev (vector-ref\
        \ dp (- j 1))]\n             [d0 (+ (vector-ref prev 0) v)]\n             [d1\
        \ (max (+ (vector-ref prev 1) v) (if (< v 0) (vector-ref prev 0) (- INF)))]\n\
        \             [d2 (max (+ (vector-ref prev 2) v) (if (< v 0) (vector-ref prev\
        \ 1) (- INF)))])\n        (vector-set! dp j (vector d0 d1 d2))))\n    (for ([i\
        \ (in-range 1 m)])\n      (let* ([v0 (vector-ref (vector-ref coins-vec i) 0)]\n\
        \             [old (vector-ref dp 0)]\n             [n0 (+ (vector-ref old 0)\
        \ v0)]\n             [n1 (max (+ (vector-ref old 1) v0) (if (< v0 0) (vector-ref\
        \ old 0) (- INF)))]\n             [n2 (max (+ (vector-ref old 2) v0) (if (<\
        \ v0 0) (vector-ref old 1) (- INF)))])\n        (vector-set! dp 0 (vector n0\
        \ n1 n2))\n        (for ([j (in-range 1 n)])\n          (let* ([v (vector-ref\
        \ (vector-ref coins-vec i) j)]\n                 [up (vector-ref dp j)]\n  \
        \               [left (vector-ref dp (- j 1))]\n                 [p0 (max (vector-ref\
        \ up 0) (vector-ref left 0))]\n                 [p1 (max (vector-ref up 1) (vector-ref\
        \ left 1))]\n                 [p2 (max (vector-ref up 2) (vector-ref left 2))]\n\
        \                 [d0 (+ p0 v)]\n                 [d1 (max (+ p1 v) (if (< v\
        \ 0) p0 (- INF)))]\n                 [d2 (max (+ p2 v) (if (< v 0) p1 (- INF)))])\n\
        \            (vector-set! dp j (vector d0 d1 d2))))))\n    (let ([res (vector-ref\
        \ dp (- n 1))])\n      (max (vector-ref res 0) (vector-ref res 1) (vector-ref\
        \ res 2)))))"
      erlang: "-spec maximum_amount(Coins :: [[integer()]]) -> integer().\nmaximum_amount(Coins)\
        \ ->\n  M = length(Coins),\n  N = length(hd(Coins)),\n  CoinsVec = list_to_tuple([list_to_tuple(Row)\
        \ || Row <- Coins]),\n  INF = 1000000000,\n  V00 = element(1, element(1, CoinsVec)),\n\
        \  InitDP0 = {V00, max(V00, 0), max(V00, 0)},\n  FirstRowDP = lists:foldl(fun(J,\
        \ Acc) ->\n    V = element(J, element(1, CoinsVec)),\n    {P0, P1, P2} = hd(Acc),\n\
        \    D0 = P0 + V,\n    D1 = max(P1 + V, if V < 0 -> P0; true -> -INF end),\n\
        \    D2 = max(P2 + V, if V < 0 -> P1; true -> -INF end),\n    [{D0, D1, D2}\
        \ | Acc]\n  end, [InitDP0], lists:seq(2, N)),\n  RowDP = list_to_tuple(lists:reverse(FirstRowDP)),\n\
        \  FinalRowDP = if M > 1 ->\n    lists:foldl(fun(I, CurrentDP) ->\n      Row\
        \ = element(I, CoinsVec),\n      V0 = element(1, Row),\n      {P0_0, P0_1, P0_2}\
        \ = element(1, CurrentDP),\n      NewDP0_0 = P0_0 + V0,\n      NewDP0_1 = max(P0_1\
        \ + V0, if V0 < 0 -> P0_0; true -> -INF end),\n      NewDP0_2 = max(P0_2 + V0,\
        \ if V0 < 0 -> P0_1; true -> -INF end),\n      RowDPList = lists:foldl(fun(J,\
        \ Acc) ->\n        V = element(J, Row),\n        {Up0, Up1, Up2} = element(J,\
        \ CurrentDP),\n        {Left0, Left1, Left2} = hd(Acc),\n        P0 = max(Up0,\
        \ Left0),\n        P1 = max(Up1, Left1),\n        P2 = max(Up2, Left2),\n  \
        \      D0 = P0 + V,\n        D1 = max(P1 + V, if V < 0 -> P0; true -> -INF end),\n\
        \        D2 = max(P2 + V, if V < 0 -> P1; true -> -INF end),\n        [{D0,\
        \ D1, D2} | Acc]\n      end, [{NewDP0_0, NewDP0_1, NewDP0_2}], lists:seq(2,\
        \ N)),\n      list_to_tuple(lists:reverse(RowDPList))\n    end, RowDP, lists:seq(2,\
        \ M));\n  true -> RowDP\n  end,\n  {F0, F1, F2} = element(N, FinalRowDP),\n\
        \  max(F0, max(F1, F2))."
      elixir: "defmodule Solution do\n  @spec maximum_amount(coins :: [[integer]]) ::\
        \ integer\n  def maximum_amount(coins) do\n    m = length(coins)\n    n = length(hd(coins))\n\
        \    coins_tuple = coins |> Enum.map(&List.to_tuple/1) |> List.to_tuple()\n\
        \    inf = 1_000_000_000\n    v00 = elem(elem(coins_tuple, 0), 0)\n    init_dp0\
        \ = {v00, max(v00, 0), max(v00, 0)}\n    first_row_dp = Enum.reduce((if n >\
        \ 1, do: 1..(n - 1), else: []), [init_dp0], fn j, acc ->\n      v = elem(elem(coins_tuple,\
        \ 0), j)\n      {p0, p1, p2} = hd(acc)\n      d0 = p0 + v\n      d1 = max(p1\
        \ + v, if(v < 0, do: p0, else: -inf))\n      d2 = max(p2 + v, if(v < 0, do:\
        \ p1, else: -inf))\n      [{d0, d1, d2} | acc]\n    end) |> Enum.reverse() |>\
        \ List.to_tuple()\n    final_row_dp = Enum.reduce((if m > 1, do: 1..(m - 1),\
        \ else: []), first_row_dp, fn i, current_dp ->\n      row = elem(coins_tuple,\
        \ i)\n      v0 = elem(row, 0)\n      {p0_0, p0_1, p0_2} = elem(current_dp, 0)\n\
        \      new_dp0_0 = p0_0 + v0\n      new_dp0_1 = max(p0_1 + v0, if(v0 < 0, do:\
        \ p0_0, else: -inf))\n      new_dp0_2 = max(p0_2 + v0, if(v0 < 0, do: p0_1,\
        \ else: -inf))\n      Enum.reduce((if n > 1, do: 1..(n - 1), else: []), [{new_dp0_0,\
        \ new_dp0_1, new_dp0_2}], fn j, acc ->\n        v = elem(row, j)\n        {up0,\
        \ up1, up2} = elem(current_dp, j)\n        {left0, left1, left2} = hd(acc)\n\
        \        p0 = max(up0, left0)\n        p1 = max(up1, left1)\n        p2 = max(up2,\
        \ left2)\n        d0 = p0 + v\n        d1 = max(p1 + v, if(v < 0, do: p0, else:\
        \ -inf))\n        d2 = max(p2 + v, if(v < 0, do: p1, else: -inf))\n        [{d0,\
        \ d1, d2} | acc]\n      end) |> Enum.reverse() |> List.to_tuple()\n    end)\n\
        \    {f0, f1, f2} = elem(final_row_dp, n - 1)\n    max(f0, max(f1, f2))\n  end\n\
        end"
    approach: 'This problem is modeled using dynamic programming with a 3D table, where
      the state `dp[i][j][k]` represents the maximum amount of money the robot can collect
      upon reaching cell `(i, j)` having used up to `k` neutralizations ($0 \le k \le
      2$). The robot can reach cell `(i, j)` from either `(i-1, j)` (above) or `(i,
      j-1)` (left). For each possible move, the robot has two choices: either accept
      the current cell''s value or, if the cell contains a robber (a negative value)
      and the robot has at least one neutralization remaining, use a neutralization
      to treat the value as zero.


      The base case is the starting cell `(0, 0)`, where the robot either takes the
      coin value or neutralizes it if it''s negative. Transitions iterate through the
      grid, updating each state based on the maximum profit from neighboring cells.
      Specifically, `dp[i][j][k]` is updated by adding `coins[i][j]` to the previous
      state with the same `k`. Additionally, if `coins[i][j]` is negative and $k > 0$,
      the robot can also inherit the profit from previous states with $k-1$ neutralizations,
      effectively making the current cell''s value zero. The final answer is the maximum
      value found in the bottom-right corner among all neutralization counts.'
    time_complexity: O(m * n). We iterate through each cell of the $m \times n$ grid
      once, and for each cell, we perform a constant number of operations (checking
      3 neutralization states and 2 possible directions).
    space_complexity: O(m * n). A 3D DP table of size $m \times n \times 3$ is used
      to store the maximum coins for each state. This can be optimized to $O(n)$ by
      only storing the current and previous rows, but $O(m \times n)$ is well within
      memory constraints for $m, n \le 500$.
    elapsed_time: 635.3661439418793
    model: gemini-3-flash-preview
    generated_at: '2026-04-02 04:47:50 '
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

This problem is modeled using dynamic programming with a 3D table, where the state `dp[i][j][k]` represents the maximum amount of money the robot can collect upon reaching cell `(i, j)` having used up to `k` neutralizations ($0 \le k \le 2$). The robot can reach cell `(i, j)` from either `(i-1, j)` (above) or `(i, j-1)` (left). For each possible move, the robot has two choices: either accept the current cell's value or, if the cell contains a robber (a negative value) and the robot has at least one neutralization remaining, use a neutralization to treat the value as zero.

The base case is the starting cell `(0, 0)`, where the robot either takes the coin value or neutralizes it if it's negative. Transitions iterate through the grid, updating each state based on the maximum profit from neighboring cells. Specifically, `dp[i][j][k]` is updated by adding `coins[i][j]` to the previous state with the same `k`. Additionally, if `coins[i][j]` is negative and $k > 0$, the robot can also inherit the profit from previous states with $k-1$ neutralizations, effectively making the current cell's value zero. The final answer is the maximum value found in the bottom-right corner among all neutralization counts.

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
    int maximumAmount(vector<vector<int>>& coins) {
        int m = coins.size();
        int n = coins[0].size();
        vector<vector<vector<long long>>> dp(m, vector<vector<long long>>(n, vector<long long>(3, -1e15)));

        dp[0][0][0] = coins[0][0];
        dp[0][0][1] = (coins[0][0] < 0) ? 0 : coins[0][0];
        dp[0][0][2] = (coins[0][0] < 0) ? 0 : coins[0][0];

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i == 0 && j == 0) continue;
                for (int k = 0; k < 3; ++k) {
                    long long from_up = (i > 0) ? dp[i - 1][j][k] : -1e15;
                    long long from_left = (j > 0) ? dp[i][j - 1][k] : -1e15;
                    dp[i][j][k] = max(from_up, from_left) + coins[i][j];

                    if (k > 0 && coins[i][j] < 0) {
                        long long from_up_k = (i > 0) ? dp[i - 1][j][k - 1] : -1e15;
                        long long from_left_k = (j > 0) ? dp[i][j - 1][k - 1] : -1e15;
                        dp[i][j][k] = max(dp[i][j][k], max(from_up_k, from_left_k));
                    }
                }
            }
        }

        return (int)max({dp[m - 1][n - 1][0], dp[m - 1][n - 1][1], dp[m - 1][n - 1][2]});
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maximumAmount(int[][] coins) {
        int m = coins.length;
        int n = coins[0].length;
        long[][][] dp = new long[m][n][3];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < 3; k++) {
                    dp[i][j][k] = -1000000000000000L;
                }
            }
        }

        dp[0][0][0] = coins[0][0];
        dp[0][0][1] = (coins[0][0] < 0) ? 0 : coins[0][0];
        dp[0][0][2] = (coins[0][0] < 0) ? 0 : coins[0][0];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) continue;
                for (int k = 0; k < 3; k++) {
                    long fromUp = (i > 0) ? dp[i - 1][j][k] : -1000000000000000L;
                    long fromLeft = (j > 0) ? dp[i][j - 1][k] : -1000000000000000L;
                    dp[i][j][k] = Math.max(fromUp, fromLeft) + coins[i][j];

                    if (k > 0 && coins[i][j] < 0) {
                        long fromUpK = (i > 0) ? dp[i - 1][j][k - 1] : -1000000000000000L;
                        long fromLeftK = (j > 0) ? dp[i][j - 1][k - 1] : -1000000000000000L;
                        dp[i][j][k] = Math.max(dp[i][j][k], Math.max(fromUpK, fromLeftK));
                    }
                }
            }
        }

        return (int) Math.max(dp[m - 1][n - 1][0], Math.max(dp[m - 1][n - 1][1], dp[m - 1][n - 1][2]));
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maximumAmount(self, coins):
        """
        :type coins: List[List[int]]
        :rtype: int
        """
        m = len(coins)
        n = len(coins[0])
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]

        dp[0][0][0] = coins[0][0]
        dp[0][0][1] = max(0, coins[0][0]) if coins[0][0] < 0 else coins[0][0]
        dp[0][0][2] = max(0, coins[0][0]) if coins[0][0] < 0 else coins[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                for k in range(3):
                    res = -float('inf')
                    if i > 0: res = max(res, dp[i - 1][j][k] + coins[i][j])
                    if j > 0: res = max(res, dp[i][j - 1][k] + coins[i][j])
                    if k > 0 and coins[i][j] < 0:
                        if i > 0: res = max(res, dp[i - 1][j][k - 1])
                        if j > 0: res = max(res, dp[i][j - 1][k - 1])
                    dp[i][j][k] = res

        return int(max(dp[m - 1][n - 1]))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m = len(coins)
        n = len(coins[0])
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]

        dp[0][0][0] = coins[0][0]
        dp[0][0][1] = max(0, coins[0][0]) if coins[0][0] < 0 else coins[0][0]
        dp[0][0][2] = max(0, coins[0][0]) if coins[0][0] < 0 else coins[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                for k in range(3):
                    res = -float('inf')
                    if i > 0: res = max(res, dp[i-1][j][k] + coins[i][j])
                    if j > 0: res = max(res, dp[i][j-1][k] + coins[i][j])
                    if k > 0 and coins[i][j] < 0:
                        if i > 0: res = max(res, dp[i-1][j][k-1])
                        if j > 0: res = max(res, dp[i][j-1][k-1])
                    dp[i][j][k] = res

        return int(max(dp[m-1][n-1]))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <limits.h>

#define MAX(a, b) ((a) > (b) ? (a) : (b))

int maximumAmount(int** coins, int coinsSize, int* coinsColSize) {
    int m = coinsSize;
    int n = coinsColSize[0];
    long long* dp = (long long*)malloc((long long)m * n * 3 * sizeof(long long));
    for (int i = 0; i < m * n * 3; i++) dp[i] = -1000000000000000LL;

    dp[0] = (long long)coins[0][0];
    if (coins[0][0] < 0) {
        dp[1] = 0LL;
        dp[2] = 0LL;
    } else {
        dp[1] = (long long)coins[0][0];
        dp[2] = (long long)coins[0][0];
    }

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (i == 0 && j == 0) continue;
            for (int k = 0; k < 3; k++) {
                long long from_up = (i > 0) ? dp[((i - 1) * n + j) * 3 + k] : -1000000000000000LL;
                long long from_left = (j > 0) ? dp[(i * n + (j - 1)) * 3 + k] : -1000000000000000LL;
                long long current = MAX(from_up, from_left) + coins[i][j];

                if (k > 0 && coins[i][j] < 0) {
                    long long neut_up = (i > 0) ? dp[((i - 1) * n + j) * 3 + (k - 1)] : -1000000000000000LL;
                    long long neut_left = (j > 0) ? dp[(i * n + (j - 1)) * 3 + (k - 1)] : -1000000000000000LL;
                    current = MAX(current, MAX(neut_up, neut_left));
                }
                dp[(i * n + j) * 3 + k] = current;
            }
        }
    }

    long long result = dp[((m - 1) * n + (n - 1)) * 3 + 0];
    result = MAX(result, dp[((m - 1) * n + (n - 1)) * 3 + 1]);
    result = MAX(result, dp[((m - 1) * n + (n - 1)) * 3 + 2]);

    free(dp);
    return (int)result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaximumAmount(int[][] coins) {
        int m = coins.Length;
        int n = coins[0].Length;
        long[,,] dp = new long[m, n, 3];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < 3; k++) {
                    dp[i, j, k] = -1000000000000000L;
                }
            }
        }

        dp[0, 0, 0] = coins[0][0];
        dp[0, 0, 1] = (coins[0][0] < 0) ? 0 : coins[0][0];
        dp[0, 0, 2] = (coins[0][0] < 0) ? 0 : coins[0][0];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) continue;
                for (int k = 0; k < 3; k++) {
                    long fromUp = (i > 0) ? dp[i - 1, j, k] : -1000000000000000L;
                    long fromLeft = (j > 0) ? dp[i, j - 1, k] : -1000000000000000L;
                    dp[i, j, k] = Math.Max(fromUp, fromLeft) + coins[i][j];

                    if (k > 0 && coins[i][j] < 0) {
                        long fromUpK = (i > 0) ? dp[i - 1, j, k - 1] : -1000000000000000L;
                        long fromLeftK = (j > 0) ? dp[i, j - 1, k - 1] : -1000000000000000L;
                        dp[i, j, k] = Math.Max(dp[i, j, k], Math.Max(fromUpK, fromLeftK));
                    }
                }
            }
        }

        return (int)Math.Max(dp[m - 1, n - 1, 0], Math.Max(dp[m - 1, n - 1, 1], dp[m - 1, n - 1, 2]));
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[][]} coins
 * @return {number}
 */
var maximumAmount = function(coins) {
    const m = coins.length;
    const n = coins[0].length;
    const dp = Array.from({ length: m }, () =>
        Array.from({ length: n }, () => Array(3).fill(-1e15))
    );

    dp[0][0][0] = coins[0][0];
    dp[0][0][1] = (coins[0][0] < 0) ? 0 : coins[0][0];
    dp[0][0][2] = (coins[0][0] < 0) ? 0 : coins[0][0];

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (i === 0 && j === 0) continue;
            for (let k = 0; k < 3; k++) {
                let fromUp = (i > 0) ? dp[i - 1][j][k] : -1e15;
                let fromLeft = (j > 0) ? dp[i][j - 1][k] : -1e15;
                dp[i][j][k] = Math.max(fromUp, fromLeft) + coins[i][j];

                if (k > 0 && coins[i][j] < 0) {
                    let fromUpK = (i > 0) ? dp[i - 1][j][k - 1] : -1e15;
                    let fromLeftK = (j > 0) ? dp[i][j - 1][k - 1] : -1e15;
                    dp[i][j][k] = Math.max(dp[i][j][k], Math.max(fromUpK, fromLeftK));
                }
            }
        }
    }

    return Math.max(...dp[m - 1][n - 1]);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maximumAmount(coins: number[][]): number {
    const m = coins.length;
    const n = coins[0].length;
    const inf = 100000000000000;
    const dp: number[][][] = Array.from({ length: m }, () =>
        Array.from({ length: n }, () => [-inf, -inf, -inf])
    );

    dp[0][0][0] = coins[0][0];
    if (coins[0][0] < 0) {
        dp[0][0][1] = 0;
    }

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (i === 0 && j === 0) continue;
            for (let k = 0; k < 3; k++) {
                let prevMax = -inf;
                if (i > 0) prevMax = Math.max(prevMax, dp[i - 1][j][k]);
                if (j > 0) prevMax = Math.max(prevMax, dp[i][j - 1][k]);

                if (prevMax > -inf) {
                    dp[i][j][k] = Math.max(dp[i][j][k], prevMax + coins[i][j]);
                }

                if (coins[i][j] < 0 && k > 0) {
                    let prevMaxK = -inf;
                    if (i > 0) prevMaxK = Math.max(prevMaxK, dp[i - 1][j][k - 1]);
                    if (j > 0) prevMaxK = Math.max(prevMaxK, dp[i][j - 1][k - 1]);
                    if (prevMaxK > -inf) {
                        dp[i][j][k] = Math.max(dp[i][j][k], prevMaxK);
                    }
                }
            }
        }
    }
    return Math.max(dp[m - 1][n - 1][0], dp[m - 1][n - 1][1], dp[m - 1][n - 1][2]);
}
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
        $inf = 100000000000000;
        $dp = array_fill(0, $m, array_fill(0, $n, array_fill(0, 3, -$inf)));

        $dp[0][0][0] = $coins[0][0];
        if ($coins[0][0] < 0) {
            $dp[0][0][1] = 0;
        }

        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($i == 0 && $j == 0) continue;
                for ($k = 0; $k < 3; $k++) {
                    $prevMax = -$inf;
                    if ($i > 0) $prevMax = max($prevMax, $dp[$i - 1][$j][$k]);
                    if ($j > 0) $prevMax = max($prevMax, $dp[$i][$j - 1][$k]);

                    if ($prevMax > -$inf) {
                        $dp[$i][$j][$k] = max($dp[$i][$j][$k], $prevMax + $coins[$i][$j]);
                    }

                    if ($coins[$i][$j] < 0 && $k > 0) {
                        $prevMaxK = -$inf;
                        if ($i > 0) $prevMaxK = max($prevMaxK, $dp[$i - 1][$j][$k - 1]);
                        if ($j > 0) $prevMaxK = max($prevMaxK, $dp[$i][$j - 1][$k - 1]);
                        if ($prevMaxK > -$inf) {
                            $dp[$i][$j][$k] = max($dp[$i][$j][$k], $prevMaxK);
                        }
                    }
                }
            }
        }

        return max($dp[$m - 1][$n - 1][0], $dp[$m - 1][$n - 1][1], $dp[$m - 1][$n - 1][2]);
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
        let inf = 100000000000000
        var dp = Array(repeating: Array(repeating: Array(repeating: -inf, count: 3), count: n), count: m)

        dp[0][0][0] = coins[0][0]
        if coins[0][0] < 0 {
            dp[0][0][1] = 0
        }

        for i in 0..<m {
            for j in 0..<n {
                if i == 0 && j == 0 { continue }
                for k in 0..<3 {
                    var prevMax = -inf
                    if i > 0 { prevMax = max(prevMax, dp[i - 1][j][k]) }
                    if j > 0 { prevMax = max(prevMax, dp[i][j - 1][k]) }

                    if prevMax > -inf {
                        dp[i][j][k] = max(dp[i][j][k], prevMax + coins[i][j])
                    }

                    if coins[i][j] < 0 && k > 0 {
                        var prevMaxK = -inf
                        if i > 0 { prevMaxK = max(prevMaxK, dp[i - 1][j][k - 1]) }
                        if j > 0 { prevMaxK = max(prevMaxK, dp[i][j - 1][k - 1]) }
                        if prevMaxK > -inf {
                            dp[i][j][k] = max(dp[i][j][k], prevMaxK)
                        }
                    }
                }
            }
        }

        return max(dp[m - 1][n - 1][0], max(dp[m - 1][n - 1][1], dp[m - 1][n - 1][2]))
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
        val inf = 100000000000000L
        val dp = Array(m) { Array(n) { LongArray(3) { -inf } } }

        dp[0][0][0] = coins[0][0].toLong()
        if (coins[0][0] < 0) {
            dp[0][0][1] = 0L
        }

        for (i in 0 until m) {
            for (j in 0 until n) {
                if (i == 0 && j == 0) continue
                for (k in 0 until 3) {
                    var prevMax = -inf
                    if (i > 0) prevMax = maxOf(prevMax, dp[i - 1][j][k])
                    if (j > 0) prevMax = maxOf(prevMax, dp[i][j - 1][k])

                    if (prevMax > -inf) {
                        dp[i][j][k] = maxOf(dp[i][j][k], prevMax + coins[i][j])
                    }

                    if (coins[i][j] < 0 && k > 0) {
                        var prevMaxK = -inf
                        if (i > 0) prevMaxK = maxOf(prevMaxK, dp[i - 1][j][k - 1])
                        if (j > 0) prevMaxK = maxOf(prevMaxK, dp[i][j - 1][k - 1])
                        if (prevMaxK > -inf) {
                            dp[i][j][k] = maxOf(dp[i][j][k], prevMaxK)
                        }
                    }
                }
            }
        }

        val res = maxOf(dp[m - 1][n - 1][0], maxOf(dp[m - 1][n - 1][1], dp[m - 1][n - 1][2]))
        return res.toInt()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maximumAmount(List<List<int>> coins) {
    int m = coins.length;
    int n = coins[0].length;
    const int inf = 1000000000000000;
    List<List<List<int>>> dp = List.generate(
        m, (i) => List.generate(n, (j) => List.filled(3, -inf)));

    dp[0][0][0] = coins[0][0];
    if (coins[0][0] < 0) {
      dp[0][0][1] = 0;
    }

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (i == 0 && j == 0) continue;
        for (int k = 0; k < 3; k++) {
          int prevMax = -inf;
          if (i > 0) if (dp[i - 1][j][k] > prevMax) prevMax = dp[i - 1][j][k];
          if (j > 0) if (dp[i][j - 1][k] > prevMax) prevMax = dp[i][j - 1][k];

          if (prevMax > -inf) {
            int val = prevMax + coins[i][j];
            if (val > dp[i][j][k]) dp[i][j][k] = val;
          }

          if (coins[i][j] < 0 && k > 0) {
            int prevMaxK = -inf;
            if (i > 0) if (dp[i - 1][j][k - 1] > prevMaxK) prevMaxK = dp[i - 1][j][k - 1];
            if (j > 0) if (dp[i][j - 1][k - 1] > prevMaxK) prevMaxK = dp[i][j - 1][k - 1];
            if (prevMaxK > -inf) {
              if (prevMaxK > dp[i][j][k]) dp[i][j][k] = prevMaxK;
            }
          }
        }
      }
    }

    int res = dp[m - 1][n - 1][0];
    if (dp[m - 1][n - 1][1] > res) res = dp[m - 1][n - 1][1];
    if (dp[m - 1][n - 1][2] > res) res = dp[m - 1][n - 1][2];
    return res;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maximumAmount(coins [][]int) int {
	m := len(coins)
	n := len(coins[0])
	const inf = 1000000000000000
	dp := make([][][3]int, m)
	for i := 0; i < m; i++ {
		dp[i] = make([][3]int, n)
		for j := 0; j < n; j++ {
			dp[i][j] = [3]int{-inf, -inf, -inf}
		}
	}

	dp[0][0][0] = coins[0][0]
	if coins[0][0] < 0 {
		dp[0][0][1] = 0
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if i == 0 && j == 0 {
				continue
			}
			for k := 0; k < 3; k++ {
				prevMax := -inf
				if i > 0 && dp[i-1][j][k] > prevMax {
					prevMax = dp[i-1][j][k]
				}
				if j > 0 && dp[i][j-1][k] > prevMax {
					prevMax = dp[i][j-1][k]
				}

				if prevMax > -inf {
					if prevMax+coins[i][j] > dp[i][j][k] {
						dp[i][j][k] = prevMax + coins[i][j]
					}
				}

				if coins[i][j] < 0 && k > 0 {
					prevMaxK := -inf
				if i > 0 && dp[i-1][j][k-1] > prevMaxK {
					prevMaxK = dp[i-1][j][k-1]
				}
				if j > 0 && dp[i][j-1][k-1] > prevMaxK {
					prevMaxK = dp[i][j-1][k-1]
				}
					if prevMaxK > -inf {
						if prevMaxK > dp[i][j][k] {
							dp[i][j][k] = prevMaxK
						}
					}
				}
			}
		}
	}

	res := dp[m-1][n-1][0]
	if dp[m-1][n-1][1] > res {
		res = dp[m-1][n-1][1]
	}
	if dp[m-1][n-1][2] > res {
		res = dp[m-1][n-1][2]
	}
	return res
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def maximum_amount(coins)
  m = coins.length
  n = coins[0].length
  inf = 1_000_000_000
  dp = Array.new(n) { Array.new(3, -inf) }

  v00 = coins[0][0]
  dp[0][0] = v00
  dp[0][1] = [v00, 0].max
  dp[0][2] = [v00, 0].max

  (1...n).each do |j|
    val = coins[0][j]
    dp[j][0] = dp[j-1][0] + val
    dp[j][1] = [dp[j-1][1] + val, (val < 0 ? dp[j-1][0] : -inf)].max
    dp[j][2] = [dp[j-1][2] + val, (val < 0 ? dp[j-1][1] : -inf)].max
  end

  (1...m).each do |i|
    val_first = coins[i][0]
    dp[0][2] = [dp[0][2] + val_first, (val_first < 0 ? dp[0][1] : -inf)].max
    dp[0][1] = [dp[0][1] + val_first, (val_first < 0 ? dp[0][0] : -inf)].max
    dp[0][0] = dp[0][0] + val_first

    (1...n).each do |j|
      val = coins[i][j]
      prev0 = [dp[j][0], dp[j-1][0]].max
      prev1 = [dp[j][1], dp[j-1][1]].max
      prev2 = [dp[j][2], dp[j-1][2]].max

      new0 = prev0 + val
      new1 = [prev1 + val, (val < 0 ? prev0 : -inf)].max
      new2 = [prev2 + val, (val < 0 ? prev1 : -inf)].max

      dp[j][0], dp[j][1], dp[j][2] = new0, new1, new2
    end
  end

  dp[n-1].max
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
    val INF = 1000000000
    val dp = Array.fill(n)(Array.fill(3)(-INF))

    val v00 = coins(0)(0)
    dp(0)(0) = v00
    dp(0)(1) = Math.max(v00, 0)
    dp(0)(2) = Math.max(v00, 0)

    for (j <- 1 until n) {
      val v = coins(0)(j)
      dp(j)(0) = dp(j - 1)(0) + v
      dp(j)(1) = Math.max(dp(j - 1)(1) + v, if (v < 0) dp(j - 1)(0) else -INF)
      dp(j)(2) = Math.max(dp(j - 1)(2) + v, if (v < 0) dp(j - 1)(1) else -INF)
    }

    for (i <- 1 until m) {
      val v0 = coins(i)(0)
      val old0 = dp(0)(0)
      val old1 = dp(0)(1)
      val old2 = dp(0)(2)
      dp(0)(2) = Math.max(old2 + v0, if (v0 < 0) old1 else -INF)
      dp(0)(1) = Math.max(old1 + v0, if (v0 < 0) old0 else -INF)
      dp(0)(0) = old0 + v0

      for (j <- 1 until n) {
        val v = coins(i)(j)
        val up0 = dp(j)(0)
        val up1 = dp(j)(1)
        val up2 = dp(j)(2)
        val left0 = dp(j - 1)(0)
        val left1 = dp(j - 1)(1)
        val left2 = dp(j - 1)(2)

        val p0 = Math.max(up0, left0)
        val p1 = Math.max(up1, left1)
        val p2 = Math.max(up2, left2)

        dp(j)(0) = p0 + v
        dp(j)(1) = Math.max(p1 + v, if (v < 0) p0 else -INF)
        dp(j)(2) = Math.max(p2 + v, if (v < 0) p1 else -INF)
      }
    }
    dp(n - 1).max
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
        let inf = 1_000_000_000;
        let mut dp = vec![vec![-inf; 3]; n];

        let v00 = coins[0][0];
        dp[0][0] = v00;
        dp[0][1] = v00.max(0);
        dp[0][2] = v00.max(0);

        for j in 1..n {
            let val = coins[0][j];
            dp[j][0] = dp[j-1][0] + val;
            dp[j][1] = (dp[j-1][1] + val).max(if val < 0 { dp[j-1][0] } else { -inf });
            dp[j][2] = (dp[j-1][2] + val).max(if val < 0 { dp[j-1][1] } else { -inf });
        }

        for i in 1..m {
            let v0 = coins[i][0];
            let old0 = dp[0][0];
            let old1 = dp[0][1];
            let old2 = dp[0][2];
            dp[0][2] = (old2 + v0).max(if v0 < 0 { old1 } else { -inf });
            dp[0][1] = (old1 + v0).max(if v0 < 0 { old0 } else { -inf });
            dp[0][0] = old0 + v0;

            for j in 1..n {
                let val = coins[i][j];
                let p0 = dp[j][0].max(dp[j-1][0]);
                let p1 = dp[j][1].max(dp[j-1][1]);
                let p2 = dp[j][2].max(dp[j-1][2]);

                dp[j][0] = p0 + val;
                dp[j][1] = (p1 + val).max(if val < 0 { p0 } else { -inf });
                dp[j][2] = (p2 + val).max(if val < 0 { p1 } else { -inf });
            }
        }

        *dp[n-1].iter().max().unwrap()
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
         [INF 1000000000]
         [dp (make-vector n)])
    (for ([j (in-range n)])
      (vector-set! dp j (vector (- INF) (- INF) (- INF))))
    (let ([v00 (vector-ref (vector-ref coins-vec 0) 0)])
      (vector-set! dp 0 (vector v00 (max v00 0) (max v00 0))))
    (for ([j (in-range 1 n)])
      (let* ([v (vector-ref (vector-ref coins-vec 0) j)]
             [prev (vector-ref dp (- j 1))]
             [d0 (+ (vector-ref prev 0) v)]
             [d1 (max (+ (vector-ref prev 1) v) (if (< v 0) (vector-ref prev 0) (- INF)))]
             [d2 (max (+ (vector-ref prev 2) v) (if (< v 0) (vector-ref prev 1) (- INF)))])
        (vector-set! dp j (vector d0 d1 d2))))
    (for ([i (in-range 1 m)])
      (let* ([v0 (vector-ref (vector-ref coins-vec i) 0)]
             [old (vector-ref dp 0)]
             [n0 (+ (vector-ref old 0) v0)]
             [n1 (max (+ (vector-ref old 1) v0) (if (< v0 0) (vector-ref old 0) (- INF)))]
             [n2 (max (+ (vector-ref old 2) v0) (if (< v0 0) (vector-ref old 1) (- INF)))])
        (vector-set! dp 0 (vector n0 n1 n2))
        (for ([j (in-range 1 n)])
          (let* ([v (vector-ref (vector-ref coins-vec i) j)]
                 [up (vector-ref dp j)]
                 [left (vector-ref dp (- j 1))]
                 [p0 (max (vector-ref up 0) (vector-ref left 0))]
                 [p1 (max (vector-ref up 1) (vector-ref left 1))]
                 [p2 (max (vector-ref up 2) (vector-ref left 2))]
                 [d0 (+ p0 v)]
                 [d1 (max (+ p1 v) (if (< v 0) p0 (- INF)))]
                 [d2 (max (+ p2 v) (if (< v 0) p1 (- INF)))])
            (vector-set! dp j (vector d0 d1 d2))))))
    (let ([res (vector-ref dp (- n 1))])
      (max (vector-ref res 0) (vector-ref res 1) (vector-ref res 2)))))
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
  CoinsVec = list_to_tuple([list_to_tuple(Row) || Row <- Coins]),
  INF = 1000000000,
  V00 = element(1, element(1, CoinsVec)),
  InitDP0 = {V00, max(V00, 0), max(V00, 0)},
  FirstRowDP = lists:foldl(fun(J, Acc) ->
    V = element(J, element(1, CoinsVec)),
    {P0, P1, P2} = hd(Acc),
    D0 = P0 + V,
    D1 = max(P1 + V, if V < 0 -> P0; true -> -INF end),
    D2 = max(P2 + V, if V < 0 -> P1; true -> -INF end),
    [{D0, D1, D2} | Acc]
  end, [InitDP0], lists:seq(2, N)),
  RowDP = list_to_tuple(lists:reverse(FirstRowDP)),
  FinalRowDP = if M > 1 ->
    lists:foldl(fun(I, CurrentDP) ->
      Row = element(I, CoinsVec),
      V0 = element(1, Row),
      {P0_0, P0_1, P0_2} = element(1, CurrentDP),
      NewDP0_0 = P0_0 + V0,
      NewDP0_1 = max(P0_1 + V0, if V0 < 0 -> P0_0; true -> -INF end),
      NewDP0_2 = max(P0_2 + V0, if V0 < 0 -> P0_1; true -> -INF end),
      RowDPList = lists:foldl(fun(J, Acc) ->
        V = element(J, Row),
        {Up0, Up1, Up2} = element(J, CurrentDP),
        {Left0, Left1, Left2} = hd(Acc),
        P0 = max(Up0, Left0),
        P1 = max(Up1, Left1),
        P2 = max(Up2, Left2),
        D0 = P0 + V,
        D1 = max(P1 + V, if V < 0 -> P0; true -> -INF end),
        D2 = max(P2 + V, if V < 0 -> P1; true -> -INF end),
        [{D0, D1, D2} | Acc]
      end, [{NewDP0_0, NewDP0_1, NewDP0_2}], lists:seq(2, N)),
      list_to_tuple(lists:reverse(RowDPList))
    end, RowDP, lists:seq(2, M));
  true -> RowDP
  end,
  {F0, F1, F2} = element(N, FinalRowDP),
  max(F0, max(F1, F2)).
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
    inf = 1_000_000_000
    v00 = elem(elem(coins_tuple, 0), 0)
    init_dp0 = {v00, max(v00, 0), max(v00, 0)}
    first_row_dp = Enum.reduce((if n > 1, do: 1..(n - 1), else: []), [init_dp0], fn j, acc ->
      v = elem(elem(coins_tuple, 0), j)
      {p0, p1, p2} = hd(acc)
      d0 = p0 + v
      d1 = max(p1 + v, if(v < 0, do: p0, else: -inf))
      d2 = max(p2 + v, if(v < 0, do: p1, else: -inf))
      [{d0, d1, d2} | acc]
    end) |> Enum.reverse() |> List.to_tuple()
    final_row_dp = Enum.reduce((if m > 1, do: 1..(m - 1), else: []), first_row_dp, fn i, current_dp ->
      row = elem(coins_tuple, i)
      v0 = elem(row, 0)
      {p0_0, p0_1, p0_2} = elem(current_dp, 0)
      new_dp0_0 = p0_0 + v0
      new_dp0_1 = max(p0_1 + v0, if(v0 < 0, do: p0_0, else: -inf))
      new_dp0_2 = max(p0_2 + v0, if(v0 < 0, do: p0_1, else: -inf))
      Enum.reduce((if n > 1, do: 1..(n - 1), else: []), [{new_dp0_0, new_dp0_1, new_dp0_2}], fn j, acc ->
        v = elem(row, j)
        {up0, up1, up2} = elem(current_dp, j)
        {left0, left1, left2} = hd(acc)
        p0 = max(up0, left0)
        p1 = max(up1, left1)
        p2 = max(up2, left2)
        d0 = p0 + v
        d1 = max(p1 + v, if(v < 0, do: p0, else: -inf))
        d2 = max(p2 + v, if(v < 0, do: p1, else: -inf))
        [{d0, d1, d2} | acc]
      end) |> Enum.reverse() |> List.to_tuple()
    end)
    {f0, f1, f2} = elem(final_row_dp, n - 1)
    max(f0, max(f1, f2))
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(m * n). We iterate through each cell of the $m \times n$ grid once, and for each cell, we perform a constant number of operations (checking 3 neutralization states and 2 possible directions).
- **Space Complexity:** O(m * n). A 3D DP table of size $m \times n \times 3$ is used to store the maximum coins for each state. This can be optimized to $O(n)$ by only storing the current and previous rows, but $O(m \times n)$ is well within memory constraints for $m, n \le 500$.
