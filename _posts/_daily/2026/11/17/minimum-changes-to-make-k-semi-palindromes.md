---
layout: post
title: "Minimum Changes to Make K Semi-palindromes"
date: 2026-11-17 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Two Pointers", "String", "Dynamic Programming"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minimumChanges(string s, int k) {\n \
        \       int n = s.length();\n        vector<vector<int>> divisors(n + 1);\n\
        \        for (int i = 1; i <= n; ++i) {\n            for (int j = i * 2; j <=\
        \ n; j += i) {\n                divisors[j].push_back(i);\n            }\n \
        \       }\n\n        vector<vector<int>> cost(n, vector<int>(n, 0));\n     \
        \   for (int len = 2; len <= n; ++len) {\n            for (int i = 0; i + len\
        \ <= n; ++i) {\n                int j = i + len - 1;\n                int min_c\
        \ = 1e9;\n                for (int d : divisors[len]) {\n                  \
        \  int cur = 0;\n                    for (int rem = 0; rem < d; ++rem) {\n \
        \                       int left = rem;\n                        int right =\
        \ len - d + rem;\n                        while (left < right) {\n         \
        \                   if (s[i + left] != s[i + right]) {\n                   \
        \             cur++;\n                            }\n                      \
        \      left += d;\n                            right -= d;\n               \
        \         }\n                    }\n                    min_c = min(min_c, cur);\n\
        \                }\n                cost[i][j] = min_c;\n            }\n   \
        \     }\n\n        vector<vector<int>> dp(k + 1, vector<int>(n + 1, 1e9));\n\
        \        dp[0][0] = 0;\n\n        for (int c = 1; c <= k; ++c) {\n         \
        \   for (int i = 2 * c; i <= n; ++i) {\n                for (int p = 2 * (c\
        \ - 1); p <= i - 2; ++p) {\n                    dp[c][i] = min(dp[c][i], dp[c\
        \ - 1][p] + cost[p][i - 1]);\n                }\n            }\n        }\n\n\
        \        return dp[k][n];\n    }\n};"
      java: "class Solution {\n    public int minimumChanges(String s, int k) {\n  \
        \      int n = s.length();\n        java.util.List<Integer>[] divisors = new\
        \ java.util.ArrayList[n + 1];\n        for (int i = 1; i <= n; ++i) {\n    \
        \        divisors[i] = new java.util.ArrayList<>();\n        }\n        for\
        \ (int i = 1; i <= n; ++i) {\n            for (int j = i * 2; j <= n; j += i)\
        \ {\n                divisors[j].add(i);\n            }\n        }\n\n     \
        \   int[][] cost = new int[n][n];\n        for (int len = 2; len <= n; ++len)\
        \ {\n            for (int i = 0; i + len <= n; ++i) {\n                int j\
        \ = i + len - 1;\n                int minChanges = 1000000000;\n           \
        \     for (int d : divisors[len]) {\n                    int cur = 0;\n    \
        \                for (int rem = 0; rem < d; ++rem) {\n                     \
        \   int left = rem;\n                        int right = len - d + rem;\n  \
        \                      while (left < right) {\n                            if\
        \ (s.charAt(i + left) != s.charAt(i + right)) {\n                          \
        \      cur++;\n                            }\n                            left\
        \ += d;\n                            right -= d;\n                        }\n\
        \                    }\n                    minChanges = Math.min(minChanges,\
        \ cur);\n                }\n                cost[i][j] = minChanges;\n     \
        \       }\n        }\n\n        int[][] dp = new int[k + 1][n + 1];\n      \
        \  for (int i = 0; i <= k; ++i) {\n            java.util.Arrays.fill(dp[i],\
        \ 1000000000);\n        }\n        dp[0][0] = 0;\n\n        for (int c = 1;\
        \ c <= k; ++c) {\n            for (int i = 2 * c; i <= n; ++i) {\n         \
        \       for (int p = 2 * (c - 1); p <= i - 2; ++p) {\n                    dp[c][i]\
        \ = Math.min(dp[c][i], dp[c - 1][p] + cost[p][i - 1]);\n                }\n\
        \            }\n        }\n\n        return dp[k][n];\n    }\n}"
      python: "class Solution(object):\n    def minimumChanges(self, s, k):\n      \
        \  \"\"\"\n        :type s: str\n        :type k: int\n        :rtype: int\n\
        \        \"\"\"\n        n = len(s)\n        divisors = [[] for _ in range(n\
        \ + 1)]\n        for i in range(1, n + 1):\n            for j in range(i * 2,\
        \ n + 1, i):\n                divisors[j].append(i)\n\n        cost = [[0] *\
        \ n for _ in range(n)]\n        for length in range(2, n + 1):\n           \
        \ for i in range(n - length + 1):\n                j = i + length - 1\n    \
        \            min_c = float('inf')\n                for d in divisors[length]:\n\
        \                    cur = 0\n                    for rem in range(d):\n   \
        \                     left = rem\n                        right = length - d\
        \ + rem\n                        while left < right:\n                     \
        \       if s[i + left] != s[i + right]:\n                                cur\
        \ += 1\n                            left += d\n                            right\
        \ -= d\n                    if cur < min_c:\n                        min_c =\
        \ cur\n                cost[i][j] = min_c\n\n        INF = float('inf')\n  \
        \      dp = [[INF] * (n + 1) for _ in range(k + 1)]\n        dp[0][0] = 0\n\n\
        \        for c in range(1, k + 1):\n            for i in range(2 * c, n + 1):\n\
        \                dp[c][i] = min(dp[c - 1][p] + cost[p][i - 1] for p in range(2\
        \ * (c - 1), i - 1))\n\n        return dp[k][n]"
      python3: "class Solution:\n    def minimumChanges(self, s: str, k: int) -> int:\n\
        \        n = len(s)\n        divisors = [[] for _ in range(n + 1)]\n       \
        \ for i in range(1, n + 1):\n            for j in range(i * 2, n + 1, i):\n\
        \                divisors[j].append(i)\n\n        cost = [[0] * n for _ in range(n)]\n\
        \        for length in range(2, n + 1):\n            for i in range(n - length\
        \ + 1):\n                j = i + length - 1\n                min_c = float('inf')\n\
        \                for d in divisors[length]:\n                    cur = 0\n \
        \                   m = length // d\n                    for rem in range(d):\n\
        \                        left = rem\n                        right = (m - 1)\
        \ * d + rem\n                        while left < right:\n                 \
        \           if s[i + left] != s[i + right]:\n                              \
        \  cur += 1\n                            left += d\n                       \
        \     right -= d\n                    if cur < min_c:\n                    \
        \    min_c = cur\n                cost[i][j] = min_c\n\n        INF = float('inf')\n\
        \        dp = [[INF] * (n + 1) for _ in range(k + 1)]\n        dp[0][0] = 0\n\
        \n        for c in range(1, k + 1):\n            for i in range(2 * c, n + 1):\n\
        \                for p in range(2 * (c - 1), i - 1):\n                    if\
        \ dp[c - 1][p] + cost[p][i - 1] < dp[c][i]:\n                        dp[c][i]\
        \ = dp[c - 1][p] + cost[p][i - 1]\n\n        return int(dp[k][n])"
      c: "#include <stdio.h>\n#include <string.h>\n\n#define INF 1000000\n\nint minimumChanges(char*\
        \ s, int k) {\n    int n = strlen(s);\n    int div_counts[201] = {0};\n    int\
        \ divisors[201][40];\n    for (int d = 1; d <= 200; d++) {\n        for (int\
        \ j = d * 2; j <= 200; j += d) {\n            divisors[j][div_counts[j]++] =\
        \ d;\n        }\n    }\n\n    int cost[201][201];\n    for (int len = 2; len\
        \ <= n; len++) {\n        for (int i = 0; i <= n - len; i++) {\n           \
        \ int j = i + len - 1;\n            int min_c = INF;\n            for (int di\
        \ = 0; di < div_counts[len]; di++) {\n                int d = divisors[len][di];\n\
        \                int cur = 0;\n                int m = len / d;\n          \
        \      for (int r = 0; r < d; r++) {\n                    int left = r;\n  \
        \                  int right = (m - 1) * d + r;\n                    while (left\
        \ < right) {\n                        if (s[i + left] != s[i + right]) cur++;\n\
        \                        left += d;\n                        right -= d;\n \
        \                   }\n                }\n                if (cur < min_c) min_c\
        \ = cur;\n            }\n            cost[i][j] = min_c;\n        }\n    }\n\
        \n    int dp[101][201];\n    for (int i = 0; i <= k; i++) {\n        for (int\
        \ j = 0; j <= n; j++) {\n            dp[i][j] = INF;\n        }\n    }\n   \
        \ dp[0][0] = 0;\n\n    for (int c = 1; c <= k; c++) {\n        for (int i =\
        \ 2 * c; i <= n; i++) {\n            for (int p = 2 * (c - 1); p <= i - 2; p++)\
        \ {\n                if (dp[c - 1][p] != INF) {\n                    int current_cost\
        \ = dp[c - 1][p] + cost[p][i - 1];\n                    if (current_cost < dp[c][i])\
        \ {\n                        dp[c][i] = current_cost;\n                    }\n\
        \                }\n            }\n        }\n    }\n\n    return dp[k][n];\n\
        }"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int MinimumChanges(string s, int k) {\n        int n = s.Length;\n\
        \        List<int>[] divisors = new List<int>[n + 1];\n        for (int i =\
        \ 0; i <= n; i++) divisors[i] = new List<int>();\n        for (int d = 1; d\
        \ <= n; d++) {\n            for (int j = d * 2; j <= n; j += d) {\n        \
        \        divisors[j].Add(d);\n            }\n        }\n\n        int[,] cost\
        \ = new int[n, n];\n        for (int length = 2; length <= n; length++) {\n\
        \            for (int i = 0; i <= n - length; i++) {\n                int j\
        \ = i + length - 1;\n                int min_c = 1000000;\n                foreach\
        \ (int d in divisors[length]) {\n                    int cur = 0;\n        \
        \            int m = length / d;\n                    for (int r = 0; r < d;\
        \ r++) {\n                        int left = r;\n                        int\
        \ right = (m - 1) * d + r;\n                        while (left < right) {\n\
        \                            if (s[i + left] != s[i + right]) cur++;\n     \
        \                       left += d;\n                            right -= d;\n\
        \                        }\n                    }\n                    if (cur\
        \ < min_c) min_c = cur;\n                }\n                cost[i, j] = min_c;\n\
        \            }\n        }\n\n        int[,] dp = new int[k + 1, n + 1];\n  \
        \      for (int i = 0; i <= k; i++)\n            for (int j = 0; j <= n; j++)\n\
        \                dp[i, j] = 1000000;\n        dp[0, 0] = 0;\n\n        for (int\
        \ c = 1; c <= k; c++) {\n            for (int i = 2 * c; i <= n; i++) {\n  \
        \              for (int p = 2 * (c - 1); p <= i - 2; p++) {\n              \
        \      if (dp[c - 1, p] != 1000000) {\n                        int current_cost\
        \ = dp[c - 1, p] + cost[p, i - 1];\n                        if (current_cost\
        \ < dp[c, i]) {\n                            dp[c, i] = current_cost;\n    \
        \                    }\n                    }\n                }\n         \
        \   }\n        }\n\n        return dp[k, n];\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @param {number} k\n * @return {number}\n\
        \ */\nvar minimumChanges = function(s, k) {\n    const n = s.length;\n    const\
        \ divisors = Array.from({ length: n + 1 }, () => []);\n    for (let d = 1; d\
        \ <= n; d++) {\n        for (let j = d * 2; j <= n; j += d) {\n            divisors[j].push(d);\n\
        \        }\n    }\n\n    const cost = Array.from({ length: n }, () => Array(n).fill(0));\n\
        \    for (let len = 2; len <= n; len++) {\n        for (let i = 0; i <= n -\
        \ len; i++) {\n            let j = i + len - 1;\n            let min_c = 1000000;\n\
        \            for (const d of divisors[len]) {\n                let cur = 0;\n\
        \                let m = len / d;\n                for (let r = 0; r < d; r++)\
        \ {\n                    let left = r;\n                    let right = (m -\
        \ 1) * d + r;\n                    while (left < right) {\n                \
        \        if (s[i + left] !== s[i + right]) cur++;\n                        left\
        \ += d;\n                        right -= d;\n                    }\n      \
        \          }\n                if (cur < min_c) min_c = cur;\n            }\n\
        \            cost[i][j] = min_c;\n        }\n    }\n\n    const dp = Array.from({\
        \ length: k + 1 }, () => Array(n + 1).fill(1000000));\n    dp[0][0] = 0;\n\n\
        \    for (let c = 1; c <= k; c++) {\n        for (let i = 2 * c; i <= n; i++)\
        \ {\n            for (let p = 2 * (c - 1); p <= i - 2; p++) {\n            \
        \    if (dp[c - 1][p] !== 1000000) {\n                    let current_cost =\
        \ dp[c - 1][p] + cost[p][i - 1];\n                    if (current_cost < dp[c][i])\
        \ {\n                        dp[c][i] = current_cost;\n                    }\n\
        \                }\n            }\n        }\n    }\n\n    return dp[k][n];\n\
        };"
      typescript: "function minimumChanges(s: string, k: number): number {\n    const\
        \ n = s.length;\n    const divisors: number[][] = Array.from({ length: n + 1\
        \ }, () => []);\n    for (let i = 1; i <= n; i++) {\n        for (let j = i\
        \ * 2; j <= n; j += i) {\n            divisors[j].push(i);\n        }\n    }\n\
        \n    const cost: number[][] = Array.from({ length: n }, () => new Array(n).fill(0));\n\
        \    for (let len = 2; len <= n; len++) {\n        for (let i = 0; i <= n -\
        \ len; i++) {\n            let j = i + len - 1;\n            let minChanges\
        \ = Infinity;\n            for (const d of divisors[len]) {\n              \
        \  let currentChanges = 0;\n                const m = len / d;\n           \
        \     for (let rem = 0; rem < d; rem++) {\n                    let left = rem;\n\
        \                    let right = (m - 1) * d + rem;\n                    while\
        \ (left < right) {\n                        if (s[i + left] !== s[i + right])\
        \ {\n                            currentChanges++;\n                       \
        \ }\n                        left += d;\n                        right -= d;\n\
        \                    }\n                }\n                if (currentChanges\
        \ < minChanges) {\n                    minChanges = currentChanges;\n      \
        \          }\n            }\n            cost[i][j] = minChanges;\n        }\n\
        \    }\n\n    const INF = 1000000;\n    const dp: number[][] = Array.from({\
        \ length: k + 1 }, () => new Array(n + 1).fill(INF));\n    dp[0][0] = 0;\n\n\
        \    for (let c = 1; c <= k; c++) {\n        for (let i = 2 * c; i <= n; i++)\
        \ {\n            for (let p = 2 * (c - 1); p <= i - 2; p++) {\n            \
        \    if (dp[c - 1][p] !== INF) {\n                    dp[c][i] = Math.min(dp[c][i],\
        \ dp[c - 1][p] + cost[p][i - 1]);\n                }\n            }\n      \
        \  }\n    }\n\n    return dp[k][n];\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @param Integer\
        \ $k\n     * @return Integer\n     */\n    function minimumChanges($s, $k) {\n\
        \        $n = strlen($s);\n        $divisors = array_fill(0, $n + 1, []);\n\
        \        for ($i = 1; $i <= $n; $i++) {\n            for ($j = $i * 2; $j <=\
        \ $n; $j += $i) {\n                $divisors[$j][] = $i;\n            }\n  \
        \      }\n\n        $cost = array_fill(0, $n, array_fill(0, $n, 0));\n     \
        \   for ($len = 2; $len <= $n; $len++) {\n            for ($i = 0; $i <= $n\
        \ - $len; $i++) {\n                $j = $i + $len - 1;\n                $minChanges\
        \ = 1000000;\n                foreach ($divisors[$len] as $d) {\n          \
        \          $currentChanges = 0;\n                    $m = $len / $d;\n     \
        \               for ($rem = 0; $rem < $d; $rem++) {\n                      \
        \  $left = $rem;\n                        $right = ($m - 1) * $d + $rem;\n \
        \                       while ($left < $right) {\n                         \
        \   if ($s[$i + $left] !== $s[$i + $right]) {\n                            \
        \    $currentChanges++;\n                            }\n                   \
        \         $left += $d;\n                            $right -= $d;\n        \
        \                }\n                    }\n                    if ($currentChanges\
        \ < $minChanges) {\n                        $minChanges = $currentChanges;\n\
        \                    }\n                }\n                $cost[$i][$j] = $minChanges;\n\
        \            }\n        }\n\n        $INF = 1000000;\n        $dp = array_fill(0,\
        \ $k + 1, array_fill(0, $n + 1, $INF));\n        $dp[0][0] = 0;\n\n        for\
        \ ($c = 1; $c <= $k; $c++) {\n            for ($i = 2 * $c; $i <= $n; $i++)\
        \ {\n                for ($p = 2 * ($c - 1); $p <= $i - 2; $p++) {\n       \
        \             if ($dp[$c - 1][$p] != $INF) {\n                        $val =\
        \ $dp[$c - 1][$p] + $cost[$p][$i - 1];\n                        if ($val < $dp[$c][$i])\
        \ {\n                            $dp[$c][$i] = $val;\n                     \
        \   }\n                    }\n                }\n            }\n        }\n\n\
        \        return $dp[$k][$n];\n    }\n}"
      swift: "class Solution {\n    func minimumChanges(_ s: String, _ k: Int) -> Int\
        \ {\n        let sArray = Array(s)\n        let n = sArray.count\n\n       \
        \ var divisors = [[Int]](repeating: [], count: n + 1)\n        for i in 1...n\
        \ {\n            var j = i * 2\n            while j <= n {\n               \
        \ divisors[j].append(i)\n                j += i\n            }\n        }\n\n\
        \        var cost = [[Int]](repeating: [Int](repeating: 0, count: n), count:\
        \ n)\n        for length in 2...n {\n            for i in 0...(n - length) {\n\
        \                let j = i + length - 1\n                var minChanges = 1_000_000\n\
        \                for d in divisors[length] {\n                    var currentChanges\
        \ = 0\n                    let m = length / d\n                    for rem in\
        \ 0..<d {\n                        var left = rem\n                        var\
        \ right = (m - 1) * d + rem\n                        while left < right {\n\
        \                            if sArray[i + left] != sArray[i + right] {\n  \
        \                              currentChanges += 1\n                       \
        \     }\n                            left += d\n                           \
        \ right -= d\n                        }\n                    }\n           \
        \         minChanges = min(minChanges, currentChanges)\n                }\n\
        \                cost[i][j] = minChanges\n            }\n        }\n\n     \
        \   let INF = 1_000_000\n        var dp = [[Int]](repeating: [Int](repeating:\
        \ INF, count: n + 1), count: k + 1)\n        dp[0][0] = 0\n\n        for c in\
        \ 1...k {\n            for i in (2 * c)...n {\n                for p in (2 *\
        \ (c - 1))...(i - 2) {\n                    if dp[c - 1][p] != INF {\n     \
        \                   dp[c][i] = min(dp[c][i], dp[c - 1][p] + cost[p][i - 1])\n\
        \                    }\n                }\n            }\n        }\n\n    \
        \    return dp[k][n]\n    }\n}"
      kotlin: "class Solution {\n    fun minimumChanges(s: String, k: Int): Int {\n\
        \        val n = s.length\n        val divisors = Array(n + 1) { mutableListOf<Int>()\
        \ }\n        for (i in 1..n) {\n            for (j in i * 2..n step i) {\n \
        \               divisors[j].add(i)\n            }\n        }\n\n        val\
        \ cost = Array(n) { IntArray(n) }\n        for (length in 2..n) {\n        \
        \    for (i in 0..n - length) {\n                val j = i + length - 1\n  \
        \              var minChanges = 1000000\n                for (d in divisors[length])\
        \ {\n                    var currentChanges = 0\n                    val m =\
        \ length / d\n                    for (rem in 0 until d) {\n               \
        \         var left = rem\n                        var right = (m - 1) * d +\
        \ rem\n                        while (left < right) {\n                    \
        \        if (s[i + left] != s[i + right]) {\n                              \
        \  currentChanges++\n                            }\n                       \
        \     left += d\n                            right -= d\n                  \
        \      }\n                    }\n                    if (currentChanges < minChanges)\
        \ {\n                        minChanges = currentChanges\n                 \
        \   }\n                }\n                cost[i][j] = minChanges\n        \
        \    }\n        }\n\n        val INF = 1000000\n        val dp = Array(k + 1)\
        \ { IntArray(n + 1) { INF } }\n        dp[0][0] = 0\n\n        for (c in 1..k)\
        \ {\n            for (i in 2 * c..n) {\n                for (p in 2 * (c - 1)..i\
        \ - 2) {\n                    if (dp[c - 1][p] != INF) {\n                 \
        \       dp[c][i] = Math.min(dp[c][i], dp[c - 1][p] + cost[p][i - 1])\n     \
        \               }\n                }\n            }\n        }\n\n        return\
        \ dp[k][n]\n    }\n}"
      dart: "class Solution {\n  int minimumChanges(String s, int k) {\n    int n =\
        \ s.length;\n    List<List<int>> divisors = List.generate(n + 1, (_) => []);\n\
        \    for (int i = 1; i <= n; i++) {\n      for (int j = i * 2; j <= n; j +=\
        \ i) {\n        divisors[j].add(i);\n      }\n    }\n\n    List<List<int>> cost\
        \ = List.generate(n, (_) => List.filled(n, 0));\n    for (int length = 2; length\
        \ <= n; length++) {\n      for (int i = 0; i <= n - length; i++) {\n       \
        \ int j = i + length - 1;\n        int minC = 1000000000;\n        for (int\
        \ d in divisors[length]) {\n          int cur = 0;\n          int m = length\
        \ ~/ d;\n          for (int rem = 0; rem < d; rem++) {\n            int left\
        \ = rem;\n            int right = (m - 1) * d + rem;\n            while (left\
        \ < right) {\n              if (s[i + left] != s[i + right]) {\n           \
        \     cur++;\n              }\n              left += d;\n              right\
        \ -= d;\n            }\n          }\n          if (cur < minC) minC = cur;\n\
        \        }\n        cost[i][j] = minC;\n      }\n    }\n\n    List<List<int>>\
        \ dp = List.generate(k + 1, (_) => List.filled(n + 1, 1000000000));\n    dp[0][0]\
        \ = 0;\n\n    for (int c = 1; c <= k; c++) {\n      for (int i = 2 * c; i <=\
        \ n; i++) {\n        for (int p = 2 * (c - 1); p <= i - 2; p++) {\n        \
        \  if (dp[c - 1][p] + cost[p][i - 1] < dp[c][i]) {\n            dp[c][i] = dp[c\
        \ - 1][p] + cost[p][i - 1];\n          }\n        }\n      }\n    }\n\n    return\
        \ dp[k][n];\n  }\n}"
      go: "func minimumChanges(s string, k int) int {\n\tn := len(s)\n\tdivisors :=\
        \ make([][]int, n+1)\n\tfor i := 1; i <= n; i++ {\n\t\tfor j := i * 2; j <=\
        \ n; j += i {\n\t\t\tdivisors[j] = append(divisors[j], i)\n\t\t}\n\t}\n\n\t\
        cost := make([][]int, n)\n\tfor i := range cost {\n\t\tcost[i] = make([]int,\
        \ n)\n\t}\n\n\tfor length := 2; length <= n; length++ {\n\t\tfor i := 0; i <=\
        \ n-length; i++ {\n\t\t\tj := i + length - 1\n\t\t\tminC := 1000000000\n\t\t\
        \tfor _, d := range divisors[length] {\n\t\t\t\tcur := 0\n\t\t\t\tm := length\
        \ / d\n\t\t\t\tfor rem := 0; rem < d; rem++ {\n\t\t\t\t\tleft := rem\n\t\t\t\
        \t\tright := (m-1)*d + rem\n\t\t\t\t\tfor left < right {\n\t\t\t\t\t\tif s[i+left]\
        \ != s[i+right] {\n\t\t\t\t\t\t\tcur++\n\t\t\t\t\t\t}\n\t\t\t\t\t\tleft += d\n\
        \t\t\t\t\t\tright -= d\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t\tif cur < minC {\n\t\t\
        \t\t\tminC = cur\n\t\t\t\t}\n\t\t\t}\n\t\t\tcost[i][j] = minC\n\t\t}\n\t}\n\n\
        \tdp := make([][]int, k+1)\n\tfor i := range dp {\n\t\tdp[i] = make([]int, n+1)\n\
        \t\tfor j := range dp[i] {\n\t\t\tdp[i][j] = 1000000000\n\t\t}\n\t}\n\tdp[0][0]\
        \ = 0\n\n\tfor c := 1; c <= k; c++ {\n\t\tfor i := 2 * c; i <= n; i++ {\n\t\t\
        \tfor p := 2 * (c - 1); p <= i-2; p++ {\n\t\t\t\tif dp[c-1][p]+cost[p][i-1]\
        \ < dp[c][i] {\n\t\t\t\t\tdp[c][i] = dp[c-1][p] + cost[p][i-1]\n\t\t\t\t}\n\t\
        \t\t}\n\t\t}\n\t}\n\n\treturn dp[k][n]\n}"
      ruby: "# @param {String} s\n# @param {Integer} k\n# @return {Integer}\ndef minimum_changes(s,\
        \ k)\n  n = s.length\n  divisors = Array.new(n + 1) { [] }\n  (1..n).each do\
        \ |i|\n    (i * 2..n).step(i) do |j|\n      divisors[j] << i\n    end\n  end\n\
        \n  cost = Array.new(n) { Array.new(n, 0) }\n  (2..n).each do |length|\n   \
        \ (0..n - length).each do |i|\n      j = i + length - 1\n      min_c = 1_000_000_000\n\
        \      divisors[length].each do |d|\n        cur = 0\n        m = length / d\n\
        \        (0...d).each do |rem|\n          left = rem\n          right = (m -\
        \ 1) * d + rem\n          while left < right\n            cur += 1 if s[i +\
        \ left] != s[i + right]\n            left += d\n            right -= d\n   \
        \       end\n        end\n        min_c = cur if cur < min_c\n      end\n  \
        \    cost[i][j] = min_c\n    end\n  end\n\n  dp = Array.new(k + 1) { Array.new(n\
        \ + 1, 1_000_000_000) }\n  dp[0][0] = 0\n\n  (1..k).each do |c|\n    (2 * c..n).each\
        \ do |i|\n      (2 * (c - 1)..i - 2).each do |p|\n        if dp[c - 1][p] +\
        \ cost[p][i - 1] < dp[c][i]\n          dp[c][i] = dp[c - 1][p] + cost[p][i -\
        \ 1]\n        end\n      end\n    end\n  end\n\n  dp[k][n]\nend"
      scala: "object Solution {\n    def minimumChanges(s: String, k: Int): Int = {\n\
        \        val n = s.length\n        val divisors = Array.tabulate(n + 1)(_ =>\
        \ new scala.collection.mutable.ArrayBuffer[Int]())\n        for (i <- 1 to n)\
        \ {\n            for (j <- i * 2 to n by i) {\n                divisors(j) +=\
        \ i\n            }\n        }\n\n        val cost = Array.ofDim[Int](n, n)\n\
        \        for (length <- 2 to n) {\n            for (i <- 0 to n - length) {\n\
        \                val j = i + length - 1\n                var minC = 1000000000\n\
        \                for (d <- divisors(length)) {\n                    var cur\
        \ = 0\n                    val m = length / d\n                    for (rem\
        \ <- 0 until d) {\n                        var left = rem\n                \
        \        var right = (m - 1) * d + rem\n                        while (left\
        \ < right) {\n                            if (s.charAt(i + left) != s.charAt(i\
        \ + right)) {\n                                cur += 1\n                  \
        \          }\n                            left += d\n                      \
        \      right -= d\n                        }\n                    }\n      \
        \              if (cur < minC) minC = cur\n                }\n             \
        \   cost(i)(j) = minC\n            }\n        }\n\n        val dp = Array.fill(k\
        \ + 1, n + 1)(1000000000)\n        dp(0)(0) = 0\n\n        for (c <- 1 to k)\
        \ {\n            for (i <- 2 * c to n) {\n                for (p <- 2 * (c -\
        \ 1) to i - 2) {\n                    if (dp(c - 1)(p) + cost(p)(i - 1) < dp(c)(i))\
        \ {\n                        dp(c)(i) = dp(c - 1)(p) + cost(p)(i - 1)\n    \
        \                }\n                }\n            }\n        }\n\n        dp(k)(n)\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn minimum_changes(s: String, k: i32) -> i32 {\n\
        \        let n = s.len();\n        let k_size = k as usize;\n        let s_bytes\
        \ = s.as_bytes();\n        let mut divisors = vec![vec![]; n + 1];\n       \
        \ for i in 1..n {\n            for j in (i * 2..=n).step_by(i) {\n         \
        \       divisors[j].push(i);\n            }\n        }\n\n        let mut cost\
        \ = vec![vec![0; n]; n];\n        for length in 2..=n {\n            for i in\
        \ 0..=n - length {\n                let j = i + length - 1;\n              \
        \  let mut min_c = 1000000;\n                for &d in &divisors[length] {\n\
        \                    let mut cur = 0;\n                    let m = length /\
        \ d;\n                    for rem in 0..d {\n                        let mut\
        \ left = rem;\n                        let mut right = (m - 1) * d + rem;\n\
        \                        while left < right {\n                            if\
        \ s_bytes[i + left] != s_bytes[i + right] {\n                              \
        \  cur += 1;\n                            }\n                            left\
        \ += d;\n                            right -= d;\n                        }\n\
        \                    }\n                    if cur < min_c {\n             \
        \           min_c = cur;\n                    }\n                }\n       \
        \         cost[i][j] = min_c;\n            }\n        }\n\n        let mut dp\
        \ = vec![vec![1000000; n + 1]; k_size + 1];\n        dp[0][0] = 0;\n\n     \
        \   for c in 1..=k_size {\n            for i in (2 * c)..=n {\n            \
        \    for p in (2 * (c - 1))..=(i - 2) {\n                    let current_dp_val\
        \ = dp[c - 1][p] + cost[p][i - 1];\n                    if current_dp_val <\
        \ dp[c][i] {\n                        dp[c][i] = current_dp_val;\n         \
        \           }\n                }\n            }\n        }\n\n        dp[k_size][n]\
        \ as i32\n    }\n}"
      racket: "(define/contract (minimum-changes s k)\n  (-> string? exact-integer?\
        \ exact-integer?)\n  (let* ([n (string-length s)]\n         [s-vec (list->vector\
        \ (string->list s))]\n         [divs (make-vector (+ n 1) '())])\n    (for ([i\
        \ (in-range 1 n)])\n      (for ([j (in-range (* i 2) (+ n 1) i)])\n        (vector-set!\
        \ divs j (cons i (vector-ref divs j)))))\n\n    (define cost (make-vector n))\n\
        \    (for ([i (in-range n)])\n      (vector-set! cost i (make-vector n 0)))\n\
        \n    (for ([len (in-range 2 (+ n 1))])\n      (for ([i (in-range (+ (- n len)\
        \ 1))])\n        (let* ([j (+ i len -1)]\n               [min-c (for/fold ([m-min\
        \ 1000000])\n                                ([d (vector-ref divs len)])\n \
        \                       (let* ([m (quotient len d)]\n                      \
        \         [cur (for/sum ([rem (in-range d)])\n                             \
        \         (for/sum ([step (in-range (quotient m 2))])\n                    \
        \                    (if (char=? (vector-ref s-vec (+ i rem (* step d)))\n \
        \                                                   (vector-ref s-vec (+ i rem\
        \ (* (- m 1 step) d))))\n                                            0 1)))])\n\
        \                          (min m-min cur)))])\n          (vector-set! (vector-ref\
        \ cost i) j min-c))))\n\n    (define dp (make-vector (+ k 1)))\n    (for ([i\
        \ (in-range (+ k 1))])\n      (vector-set! dp i (make-vector (+ n 1) 1000000)))\n\
        \    (vector-set! (vector-ref dp 0) 0 0)\n\n    (for ([c (in-range 1 (+ k 1))])\n\
        \      (for ([i (in-range (* 2 c) (+ n 1))])\n        (let ([min-val (for/fold\
        \ ([m-min 1000000])\n                                 ([p (in-range (* 2 (-\
        \ c 1)) (- i 1))])\n                         (min m-min (+ (vector-ref (vector-ref\
        \ dp (- c 1)) p)\n                                       (vector-ref (vector-ref\
        \ cost p) (- i 1)))))])\n          (vector-set! (vector-ref dp c) i min-val))))\n\
        \    (vector-ref (vector-ref dp k) n)))"
      erlang: "-spec minimum_changes(S :: unicode:unicode_binary(), K :: integer())\
        \ -> integer().\nminimum_changes(S, K) ->\n    N = byte_size(S),\n    SList\
        \ = binary_to_list(S),\n    STuple = list_to_tuple(SList),\n    SafeSeq = fun(Start,\
        \ End, Step) ->\n        if Start > End -> []; true -> lists:seq(Start, End,\
        \ Step) end\n    end,\n    Divs = lists:foldl(fun(I, Acc) ->\n        lists:foldl(fun(J,\
        \ Acc2) ->\n            maps:put(J, [I | maps:get(J, Acc2, [])], Acc2)\n   \
        \     end, Acc, SafeSeq(I * 2, N, I))\n    end, #{}, lists:seq(1, N - 1)),\n\
        \    Costs = lists:foldl(fun(Len, AccI) ->\n        lists:foldl(fun(I, AccJ)\
        \ ->\n            J = I + Len - 1,\n            Divisors = maps:get(Len, Divs,\
        \ []),\n            MinC = lists:foldl(fun(D, MinAcc) ->\n                M\
        \ = Len div D,\n                Cur = lists:foldl(fun(Rem, RemAcc) ->\n    \
        \                RemAcc + count_changes_internal(STuple, I, Rem, D, M)\n   \
        \             end, 0, lists:seq(0, D - 1)),\n                min(MinAcc, Cur)\n\
        \            end, 1000000, Divisors),\n            maps:put({I, J}, MinC, AccJ)\n\
        \        end, AccI, lists:seq(0, N - Len))\n    end, #{}, lists:seq(2, N)),\n\
        \    DP0 = #{ {0, 0} => 0 },\n    DP = lists:foldl(fun(C, PrevDP) ->\n     \
        \   lists:foldl(fun(I, CurrDP) ->\n            MinVal = lists:foldl(fun(P, MinAcc)\
        \ ->\n                PrevVal = maps:get({C - 1, P}, PrevDP, 1000000),\n   \
        \             CostVal = maps:get({P, I - 1}, Costs, 1000000),\n            \
        \    min(MinAcc, PrevVal + CostVal)\n            end, 1000000, lists:seq(2 *\
        \ (C - 1), I - 2)),\n            maps:put({C, I}, MinVal, CurrDP)\n        end,\
        \ #{}, lists:seq(2 * C, N))\n    end, DP0, lists:seq(1, K)),\n    maps:get({K,\
        \ N}, DP).\n\ncount_changes_internal(STuple, I, Rem, D, M) ->\n    lists:foldl(fun(Step,\
        \ Acc) ->\n        Left = Rem + Step * D,\n        Right = Rem + (M - 1 - Step)\
        \ * D,\n        C1 = element(I + Left + 1, STuple),\n        C2 = element(I\
        \ + Right + 1, STuple),\n        if C1 /= C2 -> Acc + 1; true -> Acc end\n \
        \   end, 0, lists:seq(0, (M div 2) - 1))."
      elixir: "defmodule Solution do\n  @spec minimum_changes(s :: String.t, k :: integer)\
        \ :: integer\n  def minimum_changes(s, k) do\n    n = String.length(s)\n   \
        \ s_tuple = s |> String.to_charlist() |> List.to_tuple()\n\n    safe_seq = fn\
        \ start, stop, step ->\n      if start > stop, do: [], else: :lists.seq(start,\
        \ stop, step)\n    end\n\n    divs = for i <- 1..(n - 1), j <- safe_seq.(i *\
        \ 2, n, i), reduce: %{} do\n      acc -> Map.update(acc, j, [i], &[i | &1])\n\
        \    end\n\n    costs = for len <- 2..n, i <- 0..(n - len), reduce: %{} do\n\
        \      acc ->\n        j = i + len - 1\n        min_c = Enum.reduce(Map.get(divs,\
        \ len, []), 1000000, fn d, min_acc ->\n          m = div(len, d)\n         \
        \ cur = Enum.reduce(0..(d - 1), 0, fn rem, rem_acc ->\n            rem_acc +\
        \ count_changes_inner(s_tuple, i, rem, d, m)\n          end)\n          min(min_acc,\
        \ cur)\n        end)\n        Map.put(acc, {i, j}, min_c)\n    end\n\n    dp\
        \ = Enum.reduce(1..k, %{{0, 0} => 0}, fn c, prev_dp ->\n      for i <- (2 *\
        \ c)..n, reduce: %{} do\n        curr_dp ->\n          min_val = Enum.reduce((2\
        \ * (c - 1))..(i - 2), 1000000, fn p, m_min ->\n            val = Map.get(prev_dp,\
        \ {c - 1, p}, 1000000) + Map.get(costs, {p, i - 1}, 1000000)\n            min(m_min,\
        \ val)\n          end)\n          Map.put(curr_dp, {c, i}, min_val)\n      end\n\
        \    end)\n\n    Map.get(dp, {k, n})\n  end\n\n  defp count_changes_inner(s_tuple,\
        \ i, rem, d, m) do\n    Enum.reduce(0..(div(m, 2) - 1), 0, fn step, acc ->\n\
        \      left = rem + step * d\n      right = rem + (m - 1 - step) * d\n     \
        \ if elem(s_tuple, i + left) != elem(s_tuple, i + right), do: acc + 1, else:\
        \ acc\n    end)\n  end\nend"
    approach: 'To solve this problem, we first precalculate the minimum number of letter
      changes needed to turn every substring s[i..j] into a semi-palindrome. For a substring
      of length L = j - i + 1 (with L >= 2), we iterate through all proper divisors
      d of L (1 <= d < L). For each divisor d, the substring is split into d disjoint
      subsequences, where subsequence r consists of characters at indices r, r + d,
      r + 2d, ..., r + (L/d - 1)d. Each of these d subsequences must form a palindrome,
      which requires comparing characters from both ends of the subsequence towards
      the center and counting mismatches. The cost for a given d is the sum of changes
      across all d subsequences, and the cost for substring s[i..j] is the minimum cost
      among all proper divisors d of L.


      Once the substring modification costs are precomputed into a table, we use dynamic
      programming to find the optimal partition into k substrings. Let dp[c][i] denote
      the minimum changes needed to partition the prefix s[0..i-1] into c substrings.
      For each count c from 1 to k and each ending position i from 2*c to n, we transition
      from previous states dp[c - 1][p] by adding the precomputed cost of substring
      s[p..i-1], where p ranges from 2*(c - 1) up to i - 2 (since each semi-palindrome
      substring must have length at least 2). The final answer is stored in dp[k][n].'
    time_complexity: O(n^3 * d(n) + k * n^2), where n is the length of s and d(n) is
      the maximum number of divisors for any integer up to n (at most 12 for n <= 200).
      Precomputing the cost for all O(n^2) substrings takes O(n * d(L)) time per substring
      of length L, summing up to at most O(n^3 * d(n)). The DP transition takes O(k
      * n^2) operations. With n <= 200, this requires only a few million operations
      and executes well within the time limit.
    space_complexity: O(n^2 + k * n) auxiliary space to store the precomputed substring
      modification cost table of size n * n and the DP table of size (k + 1) * (n +
      1).
    elapsed_time: 531.7173130512238
    model: gemini-3-flash-preview
    generated_at: '2026-11-17 06:04:39 '
---

## Problem #2911: Minimum Changes to Make K Semi-palindromes

**Difficulty:** Hard

**Topics:** Two Pointers, String, Dynamic Programming

## Problem Description

<p>Given a string <code>s</code> and an integer <code>k</code>, partition <code>s</code> into <code>k</code> <strong><span data-keyword="substring-nonempty">substrings</span></strong> such that the letter changes needed to make each substring a <strong>semi-palindrome</strong>&nbsp;are minimized.</p>

<p>Return the <em><strong>minimum</strong> number of letter changes</em> required<em>.</em></p>

<p>A <strong>semi-palindrome</strong> is a special type of string that can be divided into <strong><span data-keyword="palindrome">palindromes</span></strong> based on a repeating pattern. To check if a string is a semi-palindrome:​</p>

<ol>
	<li>Choose a positive divisor <code>d</code> of the string&#39;s length. <code>d</code> can range from <code>1</code> up to, but not including, the string&#39;s length. For a string of length <code>1</code>, it does not have a valid divisor as per this definition, since the only divisor is its length, which is not allowed.</li>
	<li>For a given divisor <code>d</code>, divide the string into groups where each group contains characters from the string that follow a repeating pattern of length <code>d</code>. Specifically, the first group consists of characters at positions <code>1</code>, <code>1 + d</code>, <code>1 + 2d</code>, and so on; the second group includes characters at positions <code>2</code>, <code>2 + d</code>, <code>2 + 2d</code>, etc.</li>
	<li>The string is considered a semi-palindrome if each of these groups forms a palindrome.</li>
</ol>

<p>Consider the string <code>&quot;abcabc&quot;</code>:</p>

<ul>
	<li>The length of <code>&quot;abcabc&quot;</code> is <code>6</code>. Valid divisors are <code>1</code>, <code>2</code>, and <code>3</code>.</li>
	<li>For <code>d = 1</code>: The entire string <code>&quot;abcabc&quot;</code> forms one group. Not a palindrome.</li>
	<li>For <code>d = 2</code>:
	<ul>
		<li>Group 1 (positions <code>1, 3, 5</code>): <code>&quot;acb&quot;</code></li>
		<li>Group 2 (positions <code>2, 4, 6</code>): <code>&quot;bac&quot;</code></li>
		<li>Neither group forms a palindrome.</li>
	</ul>
	</li>
	<li>For <code>d = 3</code>:
	<ul>
		<li>Group 1 (positions <code>1, 4</code>): <code>&quot;aa&quot;</code></li>
		<li>Group 2 (positions <code>2, 5</code>): <code>&quot;bb&quot;</code></li>
		<li>Group 3 (positions <code>3, 6</code>): <code>&quot;cc&quot;</code></li>
		<li>All groups form palindromes. Therefore, <code>&quot;abcabc&quot;</code> is a semi-palindrome.</li>
	</ul>
	</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1: </strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>Input: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> s = &quot;abcac&quot;, k = 2 </span></p>

<p><strong>Output: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> 1 </span></p>

<p><strong>Explanation: </strong> Divide <code>s</code> into <code>&quot;ab&quot;</code> and <code>&quot;cac&quot;</code>. <code>&quot;cac&quot;</code> is already semi-palindrome. Change <code>&quot;ab&quot;</code> to <code>&quot;aa&quot;</code>, it becomes semi-palindrome with <code>d = 1</code>.</p>
</div>

<p><strong class="example">Example 2: </strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>Input: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> s = &quot;abcdef&quot;, k = 2 </span></p>

<p><strong>Output: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> 2 </span></p>

<p><strong>Explanation: </strong> Divide <code>s</code> into substrings <code>&quot;abc&quot;</code> and <code>&quot;def&quot;</code>. Each&nbsp;needs one change to become semi-palindrome.</p>
</div>

<p><strong class="example">Example 3: </strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>Input: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> s = &quot;aabbaa&quot;, k = 3 </span></p>

<p><strong>Output: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> 0 </span></p>

<p><strong>Explanation: </strong> Divide <code>s</code> into substrings <code>&quot;aa&quot;</code>, <code>&quot;bb&quot;</code> and <code>&quot;aa&quot;</code>.&nbsp;All are already semi-palindromes.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 200</code></li>
	<li><code>1 &lt;= k &lt;= s.length / 2</code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
</ul>


## Hints

1. Define `dp[i][j]` as the minimum count of letter changes needed to split the suffix of string `s` starting from `s[i]` into `j` valid parts.

2. We have `dp[i][j] = min(dp[x + 1][j - 1] + v[i][x])`. Here `v[i][x]` is the minimum number of letter changes to change substring `s[i..x]` into semi-palindrome.

3. `v[i][j]` can be calculated separately by brute-force. We can create a table of `v[i][j]` independently to improve the complexity. Also note that semi-palindrome’s length is at least `2`.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To solve this problem, we first precalculate the minimum number of letter changes needed to turn every substring s[i..j] into a semi-palindrome. For a substring of length L = j - i + 1 (with L >= 2), we iterate through all proper divisors d of L (1 <= d < L). For each divisor d, the substring is split into d disjoint subsequences, where subsequence r consists of characters at indices r, r + d, r + 2d, ..., r + (L/d - 1)d. Each of these d subsequences must form a palindrome, which requires comparing characters from both ends of the subsequence towards the center and counting mismatches. The cost for a given d is the sum of changes across all d subsequences, and the cost for substring s[i..j] is the minimum cost among all proper divisors d of L.

Once the substring modification costs are precomputed into a table, we use dynamic programming to find the optimal partition into k substrings. Let dp[c][i] denote the minimum changes needed to partition the prefix s[0..i-1] into c substrings. For each count c from 1 to k and each ending position i from 2*c to n, we transition from previous states dp[c - 1][p] by adding the precomputed cost of substring s[p..i-1], where p ranges from 2*(c - 1) up to i - 2 (since each semi-palindrome substring must have length at least 2). The final answer is stored in dp[k][n].

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
    int minimumChanges(string s, int k) {
        int n = s.length();
        vector<vector<int>> divisors(n + 1);
        for (int i = 1; i <= n; ++i) {
            for (int j = i * 2; j <= n; j += i) {
                divisors[j].push_back(i);
            }
        }

        vector<vector<int>> cost(n, vector<int>(n, 0));
        for (int len = 2; len <= n; ++len) {
            for (int i = 0; i + len <= n; ++i) {
                int j = i + len - 1;
                int min_c = 1e9;
                for (int d : divisors[len]) {
                    int cur = 0;
                    for (int rem = 0; rem < d; ++rem) {
                        int left = rem;
                        int right = len - d + rem;
                        while (left < right) {
                            if (s[i + left] != s[i + right]) {
                                cur++;
                            }
                            left += d;
                            right -= d;
                        }
                    }
                    min_c = min(min_c, cur);
                }
                cost[i][j] = min_c;
            }
        }

        vector<vector<int>> dp(k + 1, vector<int>(n + 1, 1e9));
        dp[0][0] = 0;

        for (int c = 1; c <= k; ++c) {
            for (int i = 2 * c; i <= n; ++i) {
                for (int p = 2 * (c - 1); p <= i - 2; ++p) {
                    dp[c][i] = min(dp[c][i], dp[c - 1][p] + cost[p][i - 1]);
                }
            }
        }

        return dp[k][n];
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minimumChanges(String s, int k) {
        int n = s.length();
        java.util.List<Integer>[] divisors = new java.util.ArrayList[n + 1];
        for (int i = 1; i <= n; ++i) {
            divisors[i] = new java.util.ArrayList<>();
        }
        for (int i = 1; i <= n; ++i) {
            for (int j = i * 2; j <= n; j += i) {
                divisors[j].add(i);
            }
        }

        int[][] cost = new int[n][n];
        for (int len = 2; len <= n; ++len) {
            for (int i = 0; i + len <= n; ++i) {
                int j = i + len - 1;
                int minChanges = 1000000000;
                for (int d : divisors[len]) {
                    int cur = 0;
                    for (int rem = 0; rem < d; ++rem) {
                        int left = rem;
                        int right = len - d + rem;
                        while (left < right) {
                            if (s.charAt(i + left) != s.charAt(i + right)) {
                                cur++;
                            }
                            left += d;
                            right -= d;
                        }
                    }
                    minChanges = Math.min(minChanges, cur);
                }
                cost[i][j] = minChanges;
            }
        }

        int[][] dp = new int[k + 1][n + 1];
        for (int i = 0; i <= k; ++i) {
            java.util.Arrays.fill(dp[i], 1000000000);
        }
        dp[0][0] = 0;

        for (int c = 1; c <= k; ++c) {
            for (int i = 2 * c; i <= n; ++i) {
                for (int p = 2 * (c - 1); p <= i - 2; ++p) {
                    dp[c][i] = Math.min(dp[c][i], dp[c - 1][p] + cost[p][i - 1]);
                }
            }
        }

        return dp[k][n];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minimumChanges(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        divisors = [[] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(i * 2, n + 1, i):
                divisors[j].append(i)

        cost = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                min_c = float('inf')
                for d in divisors[length]:
                    cur = 0
                    for rem in range(d):
                        left = rem
                        right = length - d + rem
                        while left < right:
                            if s[i + left] != s[i + right]:
                                cur += 1
                            left += d
                            right -= d
                    if cur < min_c:
                        min_c = cur
                cost[i][j] = min_c

        INF = float('inf')
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for c in range(1, k + 1):
            for i in range(2 * c, n + 1):
                dp[c][i] = min(dp[c - 1][p] + cost[p][i - 1] for p in range(2 * (c - 1), i - 1))

        return dp[k][n]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        divisors = [[] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(i * 2, n + 1, i):
                divisors[j].append(i)

        cost = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                min_c = float('inf')
                for d in divisors[length]:
                    cur = 0
                    m = length // d
                    for rem in range(d):
                        left = rem
                        right = (m - 1) * d + rem
                        while left < right:
                            if s[i + left] != s[i + right]:
                                cur += 1
                            left += d
                            right -= d
                    if cur < min_c:
                        min_c = cur
                cost[i][j] = min_c

        INF = float('inf')
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for c in range(1, k + 1):
            for i in range(2 * c, n + 1):
                for p in range(2 * (c - 1), i - 1):
                    if dp[c - 1][p] + cost[p][i - 1] < dp[c][i]:
                        dp[c][i] = dp[c - 1][p] + cost[p][i - 1]

        return int(dp[k][n])
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <string.h>

#define INF 1000000

int minimumChanges(char* s, int k) {
    int n = strlen(s);
    int div_counts[201] = {0};
    int divisors[201][40];
    for (int d = 1; d <= 200; d++) {
        for (int j = d * 2; j <= 200; j += d) {
            divisors[j][div_counts[j]++] = d;
        }
    }

    int cost[201][201];
    for (int len = 2; len <= n; len++) {
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            int min_c = INF;
            for (int di = 0; di < div_counts[len]; di++) {
                int d = divisors[len][di];
                int cur = 0;
                int m = len / d;
                for (int r = 0; r < d; r++) {
                    int left = r;
                    int right = (m - 1) * d + r;
                    while (left < right) {
                        if (s[i + left] != s[i + right]) cur++;
                        left += d;
                        right -= d;
                    }
                }
                if (cur < min_c) min_c = cur;
            }
            cost[i][j] = min_c;
        }
    }

    int dp[101][201];
    for (int i = 0; i <= k; i++) {
        for (int j = 0; j <= n; j++) {
            dp[i][j] = INF;
        }
    }
    dp[0][0] = 0;

    for (int c = 1; c <= k; c++) {
        for (int i = 2 * c; i <= n; i++) {
            for (int p = 2 * (c - 1); p <= i - 2; p++) {
                if (dp[c - 1][p] != INF) {
                    int current_cost = dp[c - 1][p] + cost[p][i - 1];
                    if (current_cost < dp[c][i]) {
                        dp[c][i] = current_cost;
                    }
                }
            }
        }
    }

    return dp[k][n];
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
    public int MinimumChanges(string s, int k) {
        int n = s.Length;
        List<int>[] divisors = new List<int>[n + 1];
        for (int i = 0; i <= n; i++) divisors[i] = new List<int>();
        for (int d = 1; d <= n; d++) {
            for (int j = d * 2; j <= n; j += d) {
                divisors[j].Add(d);
            }
        }

        int[,] cost = new int[n, n];
        for (int length = 2; length <= n; length++) {
            for (int i = 0; i <= n - length; i++) {
                int j = i + length - 1;
                int min_c = 1000000;
                foreach (int d in divisors[length]) {
                    int cur = 0;
                    int m = length / d;
                    for (int r = 0; r < d; r++) {
                        int left = r;
                        int right = (m - 1) * d + r;
                        while (left < right) {
                            if (s[i + left] != s[i + right]) cur++;
                            left += d;
                            right -= d;
                        }
                    }
                    if (cur < min_c) min_c = cur;
                }
                cost[i, j] = min_c;
            }
        }

        int[,] dp = new int[k + 1, n + 1];
        for (int i = 0; i <= k; i++)
            for (int j = 0; j <= n; j++)
                dp[i, j] = 1000000;
        dp[0, 0] = 0;

        for (int c = 1; c <= k; c++) {
            for (int i = 2 * c; i <= n; i++) {
                for (int p = 2 * (c - 1); p <= i - 2; p++) {
                    if (dp[c - 1, p] != 1000000) {
                        int current_cost = dp[c - 1, p] + cost[p, i - 1];
                        if (current_cost < dp[c, i]) {
                            dp[c, i] = current_cost;
                        }
                    }
                }
            }
        }

        return dp[k, n];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var minimumChanges = function(s, k) {
    const n = s.length;
    const divisors = Array.from({ length: n + 1 }, () => []);
    for (let d = 1; d <= n; d++) {
        for (let j = d * 2; j <= n; j += d) {
            divisors[j].push(d);
        }
    }

    const cost = Array.from({ length: n }, () => Array(n).fill(0));
    for (let len = 2; len <= n; len++) {
        for (let i = 0; i <= n - len; i++) {
            let j = i + len - 1;
            let min_c = 1000000;
            for (const d of divisors[len]) {
                let cur = 0;
                let m = len / d;
                for (let r = 0; r < d; r++) {
                    let left = r;
                    let right = (m - 1) * d + r;
                    while (left < right) {
                        if (s[i + left] !== s[i + right]) cur++;
                        left += d;
                        right -= d;
                    }
                }
                if (cur < min_c) min_c = cur;
            }
            cost[i][j] = min_c;
        }
    }

    const dp = Array.from({ length: k + 1 }, () => Array(n + 1).fill(1000000));
    dp[0][0] = 0;

    for (let c = 1; c <= k; c++) {
        for (let i = 2 * c; i <= n; i++) {
            for (let p = 2 * (c - 1); p <= i - 2; p++) {
                if (dp[c - 1][p] !== 1000000) {
                    let current_cost = dp[c - 1][p] + cost[p][i - 1];
                    if (current_cost < dp[c][i]) {
                        dp[c][i] = current_cost;
                    }
                }
            }
        }
    }

    return dp[k][n];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimumChanges(s: string, k: number): number {
    const n = s.length;
    const divisors: number[][] = Array.from({ length: n + 1 }, () => []);
    for (let i = 1; i <= n; i++) {
        for (let j = i * 2; j <= n; j += i) {
            divisors[j].push(i);
        }
    }

    const cost: number[][] = Array.from({ length: n }, () => new Array(n).fill(0));
    for (let len = 2; len <= n; len++) {
        for (let i = 0; i <= n - len; i++) {
            let j = i + len - 1;
            let minChanges = Infinity;
            for (const d of divisors[len]) {
                let currentChanges = 0;
                const m = len / d;
                for (let rem = 0; rem < d; rem++) {
                    let left = rem;
                    let right = (m - 1) * d + rem;
                    while (left < right) {
                        if (s[i + left] !== s[i + right]) {
                            currentChanges++;
                        }
                        left += d;
                        right -= d;
                    }
                }
                if (currentChanges < minChanges) {
                    minChanges = currentChanges;
                }
            }
            cost[i][j] = minChanges;
        }
    }

    const INF = 1000000;
    const dp: number[][] = Array.from({ length: k + 1 }, () => new Array(n + 1).fill(INF));
    dp[0][0] = 0;

    for (let c = 1; c <= k; c++) {
        for (let i = 2 * c; i <= n; i++) {
            for (let p = 2 * (c - 1); p <= i - 2; p++) {
                if (dp[c - 1][p] !== INF) {
                    dp[c][i] = Math.min(dp[c][i], dp[c - 1][p] + cost[p][i - 1]);
                }
            }
        }
    }

    return dp[k][n];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function minimumChanges($s, $k) {
        $n = strlen($s);
        $divisors = array_fill(0, $n + 1, []);
        for ($i = 1; $i <= $n; $i++) {
            for ($j = $i * 2; $j <= $n; $j += $i) {
                $divisors[$j][] = $i;
            }
        }

        $cost = array_fill(0, $n, array_fill(0, $n, 0));
        for ($len = 2; $len <= $n; $len++) {
            for ($i = 0; $i <= $n - $len; $i++) {
                $j = $i + $len - 1;
                $minChanges = 1000000;
                foreach ($divisors[$len] as $d) {
                    $currentChanges = 0;
                    $m = $len / $d;
                    for ($rem = 0; $rem < $d; $rem++) {
                        $left = $rem;
                        $right = ($m - 1) * $d + $rem;
                        while ($left < $right) {
                            if ($s[$i + $left] !== $s[$i + $right]) {
                                $currentChanges++;
                            }
                            $left += $d;
                            $right -= $d;
                        }
                    }
                    if ($currentChanges < $minChanges) {
                        $minChanges = $currentChanges;
                    }
                }
                $cost[$i][$j] = $minChanges;
            }
        }

        $INF = 1000000;
        $dp = array_fill(0, $k + 1, array_fill(0, $n + 1, $INF));
        $dp[0][0] = 0;

        for ($c = 1; $c <= $k; $c++) {
            for ($i = 2 * $c; $i <= $n; $i++) {
                for ($p = 2 * ($c - 1); $p <= $i - 2; $p++) {
                    if ($dp[$c - 1][$p] != $INF) {
                        $val = $dp[$c - 1][$p] + $cost[$p][$i - 1];
                        if ($val < $dp[$c][$i]) {
                            $dp[$c][$i] = $val;
                        }
                    }
                }
            }
        }

        return $dp[$k][$n];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minimumChanges(_ s: String, _ k: Int) -> Int {
        let sArray = Array(s)
        let n = sArray.count

        var divisors = [[Int]](repeating: [], count: n + 1)
        for i in 1...n {
            var j = i * 2
            while j <= n {
                divisors[j].append(i)
                j += i
            }
        }

        var cost = [[Int]](repeating: [Int](repeating: 0, count: n), count: n)
        for length in 2...n {
            for i in 0...(n - length) {
                let j = i + length - 1
                var minChanges = 1_000_000
                for d in divisors[length] {
                    var currentChanges = 0
                    let m = length / d
                    for rem in 0..<d {
                        var left = rem
                        var right = (m - 1) * d + rem
                        while left < right {
                            if sArray[i + left] != sArray[i + right] {
                                currentChanges += 1
                            }
                            left += d
                            right -= d
                        }
                    }
                    minChanges = min(minChanges, currentChanges)
                }
                cost[i][j] = minChanges
            }
        }

        let INF = 1_000_000
        var dp = [[Int]](repeating: [Int](repeating: INF, count: n + 1), count: k + 1)
        dp[0][0] = 0

        for c in 1...k {
            for i in (2 * c)...n {
                for p in (2 * (c - 1))...(i - 2) {
                    if dp[c - 1][p] != INF {
                        dp[c][i] = min(dp[c][i], dp[c - 1][p] + cost[p][i - 1])
                    }
                }
            }
        }

        return dp[k][n]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minimumChanges(s: String, k: Int): Int {
        val n = s.length
        val divisors = Array(n + 1) { mutableListOf<Int>() }
        for (i in 1..n) {
            for (j in i * 2..n step i) {
                divisors[j].add(i)
            }
        }

        val cost = Array(n) { IntArray(n) }
        for (length in 2..n) {
            for (i in 0..n - length) {
                val j = i + length - 1
                var minChanges = 1000000
                for (d in divisors[length]) {
                    var currentChanges = 0
                    val m = length / d
                    for (rem in 0 until d) {
                        var left = rem
                        var right = (m - 1) * d + rem
                        while (left < right) {
                            if (s[i + left] != s[i + right]) {
                                currentChanges++
                            }
                            left += d
                            right -= d
                        }
                    }
                    if (currentChanges < minChanges) {
                        minChanges = currentChanges
                    }
                }
                cost[i][j] = minChanges
            }
        }

        val INF = 1000000
        val dp = Array(k + 1) { IntArray(n + 1) { INF } }
        dp[0][0] = 0

        for (c in 1..k) {
            for (i in 2 * c..n) {
                for (p in 2 * (c - 1)..i - 2) {
                    if (dp[c - 1][p] != INF) {
                        dp[c][i] = Math.min(dp[c][i], dp[c - 1][p] + cost[p][i - 1])
                    }
                }
            }
        }

        return dp[k][n]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minimumChanges(String s, int k) {
    int n = s.length;
    List<List<int>> divisors = List.generate(n + 1, (_) => []);
    for (int i = 1; i <= n; i++) {
      for (int j = i * 2; j <= n; j += i) {
        divisors[j].add(i);
      }
    }

    List<List<int>> cost = List.generate(n, (_) => List.filled(n, 0));
    for (int length = 2; length <= n; length++) {
      for (int i = 0; i <= n - length; i++) {
        int j = i + length - 1;
        int minC = 1000000000;
        for (int d in divisors[length]) {
          int cur = 0;
          int m = length ~/ d;
          for (int rem = 0; rem < d; rem++) {
            int left = rem;
            int right = (m - 1) * d + rem;
            while (left < right) {
              if (s[i + left] != s[i + right]) {
                cur++;
              }
              left += d;
              right -= d;
            }
          }
          if (cur < minC) minC = cur;
        }
        cost[i][j] = minC;
      }
    }

    List<List<int>> dp = List.generate(k + 1, (_) => List.filled(n + 1, 1000000000));
    dp[0][0] = 0;

    for (int c = 1; c <= k; c++) {
      for (int i = 2 * c; i <= n; i++) {
        for (int p = 2 * (c - 1); p <= i - 2; p++) {
          if (dp[c - 1][p] + cost[p][i - 1] < dp[c][i]) {
            dp[c][i] = dp[c - 1][p] + cost[p][i - 1];
          }
        }
      }
    }

    return dp[k][n];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minimumChanges(s string, k int) int {
	n := len(s)
	divisors := make([][]int, n+1)
	for i := 1; i <= n; i++ {
		for j := i * 2; j <= n; j += i {
			divisors[j] = append(divisors[j], i)
		}
	}

	cost := make([][]int, n)
	for i := range cost {
		cost[i] = make([]int, n)
	}

	for length := 2; length <= n; length++ {
		for i := 0; i <= n-length; i++ {
			j := i + length - 1
			minC := 1000000000
			for _, d := range divisors[length] {
				cur := 0
				m := length / d
				for rem := 0; rem < d; rem++ {
					left := rem
					right := (m-1)*d + rem
					for left < right {
						if s[i+left] != s[i+right] {
							cur++
						}
						left += d
						right -= d
					}
				}
				if cur < minC {
					minC = cur
				}
			}
			cost[i][j] = minC
		}
	}

	dp := make([][]int, k+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
		for j := range dp[i] {
			dp[i][j] = 1000000000
		}
	}
	dp[0][0] = 0

	for c := 1; c <= k; c++ {
		for i := 2 * c; i <= n; i++ {
			for p := 2 * (c - 1); p <= i-2; p++ {
				if dp[c-1][p]+cost[p][i-1] < dp[c][i] {
					dp[c][i] = dp[c-1][p] + cost[p][i-1]
				}
			}
		}
	}

	return dp[k][n]
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @param {Integer} k
# @return {Integer}
def minimum_changes(s, k)
  n = s.length
  divisors = Array.new(n + 1) { [] }
  (1..n).each do |i|
    (i * 2..n).step(i) do |j|
      divisors[j] << i
    end
  end

  cost = Array.new(n) { Array.new(n, 0) }
  (2..n).each do |length|
    (0..n - length).each do |i|
      j = i + length - 1
      min_c = 1_000_000_000
      divisors[length].each do |d|
        cur = 0
        m = length / d
        (0...d).each do |rem|
          left = rem
          right = (m - 1) * d + rem
          while left < right
            cur += 1 if s[i + left] != s[i + right]
            left += d
            right -= d
          end
        end
        min_c = cur if cur < min_c
      end
      cost[i][j] = min_c
    end
  end

  dp = Array.new(k + 1) { Array.new(n + 1, 1_000_000_000) }
  dp[0][0] = 0

  (1..k).each do |c|
    (2 * c..n).each do |i|
      (2 * (c - 1)..i - 2).each do |p|
        if dp[c - 1][p] + cost[p][i - 1] < dp[c][i]
          dp[c][i] = dp[c - 1][p] + cost[p][i - 1]
        end
      end
    end
  end

  dp[k][n]
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minimumChanges(s: String, k: Int): Int = {
        val n = s.length
        val divisors = Array.tabulate(n + 1)(_ => new scala.collection.mutable.ArrayBuffer[Int]())
        for (i <- 1 to n) {
            for (j <- i * 2 to n by i) {
                divisors(j) += i
            }
        }

        val cost = Array.ofDim[Int](n, n)
        for (length <- 2 to n) {
            for (i <- 0 to n - length) {
                val j = i + length - 1
                var minC = 1000000000
                for (d <- divisors(length)) {
                    var cur = 0
                    val m = length / d
                    for (rem <- 0 until d) {
                        var left = rem
                        var right = (m - 1) * d + rem
                        while (left < right) {
                            if (s.charAt(i + left) != s.charAt(i + right)) {
                                cur += 1
                            }
                            left += d
                            right -= d
                        }
                    }
                    if (cur < minC) minC = cur
                }
                cost(i)(j) = minC
            }
        }

        val dp = Array.fill(k + 1, n + 1)(1000000000)
        dp(0)(0) = 0

        for (c <- 1 to k) {
            for (i <- 2 * c to n) {
                for (p <- 2 * (c - 1) to i - 2) {
                    if (dp(c - 1)(p) + cost(p)(i - 1) < dp(c)(i)) {
                        dp(c)(i) = dp(c - 1)(p) + cost(p)(i - 1)
                    }
                }
            }
        }

        dp(k)(n)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn minimum_changes(s: String, k: i32) -> i32 {
        let n = s.len();
        let k_size = k as usize;
        let s_bytes = s.as_bytes();
        let mut divisors = vec![vec![]; n + 1];
        for i in 1..n {
            for j in (i * 2..=n).step_by(i) {
                divisors[j].push(i);
            }
        }

        let mut cost = vec![vec![0; n]; n];
        for length in 2..=n {
            for i in 0..=n - length {
                let j = i + length - 1;
                let mut min_c = 1000000;
                for &d in &divisors[length] {
                    let mut cur = 0;
                    let m = length / d;
                    for rem in 0..d {
                        let mut left = rem;
                        let mut right = (m - 1) * d + rem;
                        while left < right {
                            if s_bytes[i + left] != s_bytes[i + right] {
                                cur += 1;
                            }
                            left += d;
                            right -= d;
                        }
                    }
                    if cur < min_c {
                        min_c = cur;
                    }
                }
                cost[i][j] = min_c;
            }
        }

        let mut dp = vec![vec![1000000; n + 1]; k_size + 1];
        dp[0][0] = 0;

        for c in 1..=k_size {
            for i in (2 * c)..=n {
                for p in (2 * (c - 1))..=(i - 2) {
                    let current_dp_val = dp[c - 1][p] + cost[p][i - 1];
                    if current_dp_val < dp[c][i] {
                        dp[c][i] = current_dp_val;
                    }
                }
            }
        }

        dp[k_size][n] as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (minimum-changes s k)
  (-> string? exact-integer? exact-integer?)
  (let* ([n (string-length s)]
         [s-vec (list->vector (string->list s))]
         [divs (make-vector (+ n 1) '())])
    (for ([i (in-range 1 n)])
      (for ([j (in-range (* i 2) (+ n 1) i)])
        (vector-set! divs j (cons i (vector-ref divs j)))))

    (define cost (make-vector n))
    (for ([i (in-range n)])
      (vector-set! cost i (make-vector n 0)))

    (for ([len (in-range 2 (+ n 1))])
      (for ([i (in-range (+ (- n len) 1))])
        (let* ([j (+ i len -1)]
               [min-c (for/fold ([m-min 1000000])
                                ([d (vector-ref divs len)])
                        (let* ([m (quotient len d)]
                               [cur (for/sum ([rem (in-range d)])
                                      (for/sum ([step (in-range (quotient m 2))])
                                        (if (char=? (vector-ref s-vec (+ i rem (* step d)))
                                                    (vector-ref s-vec (+ i rem (* (- m 1 step) d))))
                                            0 1)))])
                          (min m-min cur)))])
          (vector-set! (vector-ref cost i) j min-c))))

    (define dp (make-vector (+ k 1)))
    (for ([i (in-range (+ k 1))])
      (vector-set! dp i (make-vector (+ n 1) 1000000)))
    (vector-set! (vector-ref dp 0) 0 0)

    (for ([c (in-range 1 (+ k 1))])
      (for ([i (in-range (* 2 c) (+ n 1))])
        (let ([min-val (for/fold ([m-min 1000000])
                                 ([p (in-range (* 2 (- c 1)) (- i 1))])
                         (min m-min (+ (vector-ref (vector-ref dp (- c 1)) p)
                                       (vector-ref (vector-ref cost p) (- i 1)))))])
          (vector-set! (vector-ref dp c) i min-val))))
    (vector-ref (vector-ref dp k) n)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec minimum_changes(S :: unicode:unicode_binary(), K :: integer()) -> integer().
minimum_changes(S, K) ->
    N = byte_size(S),
    SList = binary_to_list(S),
    STuple = list_to_tuple(SList),
    SafeSeq = fun(Start, End, Step) ->
        if Start > End -> []; true -> lists:seq(Start, End, Step) end
    end,
    Divs = lists:foldl(fun(I, Acc) ->
        lists:foldl(fun(J, Acc2) ->
            maps:put(J, [I | maps:get(J, Acc2, [])], Acc2)
        end, Acc, SafeSeq(I * 2, N, I))
    end, #{}, lists:seq(1, N - 1)),
    Costs = lists:foldl(fun(Len, AccI) ->
        lists:foldl(fun(I, AccJ) ->
            J = I + Len - 1,
            Divisors = maps:get(Len, Divs, []),
            MinC = lists:foldl(fun(D, MinAcc) ->
                M = Len div D,
                Cur = lists:foldl(fun(Rem, RemAcc) ->
                    RemAcc + count_changes_internal(STuple, I, Rem, D, M)
                end, 0, lists:seq(0, D - 1)),
                min(MinAcc, Cur)
            end, 1000000, Divisors),
            maps:put({I, J}, MinC, AccJ)
        end, AccI, lists:seq(0, N - Len))
    end, #{}, lists:seq(2, N)),
    DP0 = #{ {0, 0} => 0 },
    DP = lists:foldl(fun(C, PrevDP) ->
        lists:foldl(fun(I, CurrDP) ->
            MinVal = lists:foldl(fun(P, MinAcc) ->
                PrevVal = maps:get({C - 1, P}, PrevDP, 1000000),
                CostVal = maps:get({P, I - 1}, Costs, 1000000),
                min(MinAcc, PrevVal + CostVal)
            end, 1000000, lists:seq(2 * (C - 1), I - 2)),
            maps:put({C, I}, MinVal, CurrDP)
        end, #{}, lists:seq(2 * C, N))
    end, DP0, lists:seq(1, K)),
    maps:get({K, N}, DP).

count_changes_internal(STuple, I, Rem, D, M) ->
    lists:foldl(fun(Step, Acc) ->
        Left = Rem + Step * D,
        Right = Rem + (M - 1 - Step) * D,
        C1 = element(I + Left + 1, STuple),
        C2 = element(I + Right + 1, STuple),
        if C1 /= C2 -> Acc + 1; true -> Acc end
    end, 0, lists:seq(0, (M div 2) - 1)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_changes(s :: String.t, k :: integer) :: integer
  def minimum_changes(s, k) do
    n = String.length(s)
    s_tuple = s |> String.to_charlist() |> List.to_tuple()

    safe_seq = fn start, stop, step ->
      if start > stop, do: [], else: :lists.seq(start, stop, step)
    end

    divs = for i <- 1..(n - 1), j <- safe_seq.(i * 2, n, i), reduce: %{} do
      acc -> Map.update(acc, j, [i], &[i | &1])
    end

    costs = for len <- 2..n, i <- 0..(n - len), reduce: %{} do
      acc ->
        j = i + len - 1
        min_c = Enum.reduce(Map.get(divs, len, []), 1000000, fn d, min_acc ->
          m = div(len, d)
          cur = Enum.reduce(0..(d - 1), 0, fn rem, rem_acc ->
            rem_acc + count_changes_inner(s_tuple, i, rem, d, m)
          end)
          min(min_acc, cur)
        end)
        Map.put(acc, {i, j}, min_c)
    end

    dp = Enum.reduce(1..k, %{{0, 0} => 0}, fn c, prev_dp ->
      for i <- (2 * c)..n, reduce: %{} do
        curr_dp ->
          min_val = Enum.reduce((2 * (c - 1))..(i - 2), 1000000, fn p, m_min ->
            val = Map.get(prev_dp, {c - 1, p}, 1000000) + Map.get(costs, {p, i - 1}, 1000000)
            min(m_min, val)
          end)
          Map.put(curr_dp, {c, i}, min_val)
      end
    end)

    Map.get(dp, {k, n})
  end

  defp count_changes_inner(s_tuple, i, rem, d, m) do
    Enum.reduce(0..(div(m, 2) - 1), 0, fn step, acc ->
      left = rem + step * d
      right = rem + (m - 1 - step) * d
      if elem(s_tuple, i + left) != elem(s_tuple, i + right), do: acc + 1, else: acc
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n^3 * d(n) + k * n^2), where n is the length of s and d(n) is the maximum number of divisors for any integer up to n (at most 12 for n <= 200). Precomputing the cost for all O(n^2) substrings takes O(n * d(L)) time per substring of length L, summing up to at most O(n^3 * d(n)). The DP transition takes O(k * n^2) operations. With n <= 200, this requires only a few million operations and executes well within the time limit.
- **Space Complexity:** O(n^2 + k * n) auxiliary space to store the precomputed substring modification cost table of size n * n and the DP table of size (k + 1) * (n + 1).
