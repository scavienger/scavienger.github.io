---
layout: post
title: "Number of Paths with Max Score"
date: 2026-07-05 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Dynamic Programming", "Matrix"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/number-of-paths-with-max-score/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <string>\n#include <utility>\n\nusing namespace\
        \ std;\n\nclass Solution {\npublic:\n    vector<int> pathsWithMaxScore(vector<string>&\
        \ board) {\n        int n = board.size();\n        int mod = 1000000007;\n \
        \       vector<vector<pair<int, int>>> dp(n, vector<pair<int, int>>(n, {0, 0}));\n\
        \        dp[n - 1][n - 1] = {0, 1};\n\n        for (int i = n - 1; i >= 0; --i)\
        \ {\n            for (int j = n - 1; j >= 0; --j) {\n                if ((i\
        \ == n - 1 && j == n - 1) || board[i][j] == 'X') continue;\n\n             \
        \   int maxS = -1;\n                long long count = 0;\n                int\
        \ dirs[3][2] = {{i + 1, j}, {i, j + 1}, {i + 1, j + 1}};\n\n               \
        \ for (int k = 0; k < 3; ++k) {\n                    int ni = dirs[k][0], nj\
        \ = dirs[k][1];\n                    if (ni < n && nj < n && dp[ni][nj].second\
        \ > 0) {\n                        if (dp[ni][nj].first > maxS) {\n         \
        \                   maxS = dp[ni][nj].first;\n                            count\
        \ = dp[ni][nj].second;\n                        } else if (dp[ni][nj].first\
        \ == maxS) {\n                            count = (count + dp[ni][nj].second)\
        \ % mod;\n                        }\n                    }\n               \
        \ }\n\n                if (maxS != -1) {\n                    int val = (board[i][j]\
        \ == 'E' ? 0 : board[i][j] - '0');\n                    dp[i][j] = {val + maxS,\
        \ (int)count};\n                }\n            }\n        }\n\n        return\
        \ {dp[0][0].first, dp[0][0].second};\n    }\n};"
      java: "import java.util.List;\n\nclass Solution {\n    public int[] pathsWithMaxScore(List<String>\
        \ board) {\n        int n = board.size();\n        int mod = 1000000007;\n \
        \       int[][] dpSum = new int[n][n];\n        int[][] dpCount = new int[n][n];\n\
        \        dpCount[n - 1][n - 1] = 1;\n\n        for (int i = n - 1; i >= 0; i--)\
        \ {\n            for (int j = n - 1; j >= 0; j--) {\n                if ((i\
        \ == n - 1 && j == n - 1) || board.get(i).charAt(j) == 'X') continue;\n\n  \
        \              int maxS = -1;\n                long count = 0;\n           \
        \     int[][] dirs = {{i + 1, j}, {i, j + 1}, {i + 1, j + 1}};\n\n         \
        \       for (int[] d : dirs) {\n                    int ni = d[0], nj = d[1];\n\
        \                    if (ni < n && nj < n && dpCount[ni][nj] > 0) {\n      \
        \                  if (dpSum[ni][nj] > maxS) {\n                           \
        \ maxS = dpSum[ni][nj];\n                            count = dpCount[ni][nj];\n\
        \                        } else if (dpSum[ni][nj] == maxS) {\n             \
        \               count = (count + dpCount[ni][nj]) % mod;\n                 \
        \       }\n                    }\n                }\n\n                if (maxS\
        \ != -1) {\n                    char c = board.get(i).charAt(j);\n         \
        \           int val = (c == 'E' ? 0 : c - '0');\n                    dpSum[i][j]\
        \ = val + maxS;\n                    dpCount[i][j] = (int) count;\n        \
        \        }\n            }\n        }\n\n        return new int[]{dpSum[0][0],\
        \ dpCount[0][0]};\n    }\n}"
      python: "class Solution(object):\n    def pathsWithMaxScore(self, board):\n  \
        \      \"\"\"\n        :type board: List[str]\n        :rtype: List[int]\n \
        \       \"\"\"\n        n = len(board)\n        MOD = 10**9 + 7\n        dp_sum\
        \ = [[0] * n for _ in range(n)]\n        dp_count = [[0] * n for _ in range(n)]\n\
        \        dp_count[n-1][n-1] = 1\n\n        for i in range(n - 1, -1, -1):\n\
        \            for j in range(n - 1, -1, -1):\n                if (i == n - 1\
        \ and j == n - 1) or board[i][j] == 'X':\n                    continue\n\n \
        \               max_s = -1\n                count = 0\n                for ni,\
        \ nj in [(i + 1, j), (i, j + 1), (i + 1, j + 1)]:\n                    if ni\
        \ < n and nj < n and dp_count[ni][nj] > 0:\n                        if dp_sum[ni][nj]\
        \ > max_s:\n                            max_s = dp_sum[ni][nj]\n           \
        \                 count = dp_count[ni][nj]\n                        elif dp_sum[ni][nj]\
        \ == max_s:\n                            count = (count + dp_count[ni][nj])\
        \ % MOD\n\n                if max_s != -1:\n                    char = board[i][j]\n\
        \                    val = int(char) if '1' <= char <= '9' else 0\n        \
        \            dp_sum[i][j] = val + max_s\n                    dp_count[i][j]\
        \ = count % MOD\n\n        return [dp_sum[0][0], dp_count[0][0]]"
      python3: "class Solution:\n    def pathsWithMaxScore(self, board: List[str]) ->\
        \ List[int]:\n        n = len(board)\n        MOD = 10**9 + 7\n        dp_sum\
        \ = [[0] * n for _ in range(n)]\n        dp_cnt = [[0] * n for _ in range(n)]\n\
        \n        dp_cnt[n-1][n-1] = 1\n\n        for i in range(n - 1, -1, -1):\n \
        \           for j in range(n - 1, -1, -1):\n                if i == n - 1 and\
        \ j == n - 1:\n                    continue\n                if board[i][j]\
        \ == 'X':\n                    continue\n\n                max_s = -1\n    \
        \            count = 0\n\n                for ni, nj in [(i + 1, j), (i, j +\
        \ 1), (i + 1, j + 1)]:\n                    if ni < n and nj < n and dp_cnt[ni][nj]\
        \ > 0:\n                        if dp_sum[ni][nj] > max_s:\n               \
        \             max_s = dp_sum[ni][nj]\n                            count = dp_cnt[ni][nj]\n\
        \                        elif dp_sum[ni][nj] == max_s:\n                   \
        \         count = (count + dp_cnt[ni][nj]) % MOD\n\n                if max_s\
        \ != -1:\n                    score = int(board[i][j]) if '1' <= board[i][j]\
        \ <= '9' else 0\n                    dp_sum[i][j] = max_s + score\n        \
        \            dp_cnt[i][j] = count\n\n        return [dp_sum[0][0], dp_cnt[0][0]]"
      c: "#include <stdlib.h>\n#include <string.h>\n\n/**\n * Note: The returned array\
        \ must be malloced, assume caller calls free().\n */\nint* pathsWithMaxScore(char\
        \ ** board, int boardSize, int* returnSize){\n    int n = boardSize;\n    int\
        \ MOD = 1000000007;\n\n    int dpSum[100][100];\n    int dpCnt[100][100];\n\
        \    for (int i = 0; i < n; i++) {\n        for (int j = 0; j < n; j++) {\n\
        \            dpSum[i][j] = 0;\n            dpCnt[i][j] = 0;\n        }\n   \
        \ }\n\n    dpCnt[n-1][n-1] = 1;\n\n    for (int i = n - 1; i >= 0; i--) {\n\
        \        for (int j = n - 1; j >= 0; j--) {\n            if (i == n - 1 && j\
        \ == n - 1) continue;\n            if (board[i][j] == 'X') continue;\n\n   \
        \         int maxS = -1;\n            long long count = 0;\n\n            int\
        \ ni_vals[3] = {i + 1, i, i + 1};\n            int nj_vals[3] = {j, j + 1, j\
        \ + 1};\n\n            for (int d = 0; d < 3; d++) {\n                int ni\
        \ = ni_vals[d];\n                int nj = nj_vals[d];\n                if (ni\
        \ < n && nj < n && dpCnt[ni][nj] > 0) {\n                    if (dpSum[ni][nj]\
        \ > maxS) {\n                        maxS = dpSum[ni][nj];\n               \
        \         count = dpCnt[ni][nj];\n                    } else if (dpSum[ni][nj]\
        \ == maxS) {\n                        count = (count + dpCnt[ni][nj]) % MOD;\n\
        \                    }\n                }\n            }\n\n            if (maxS\
        \ != -1) {\n                int score = (board[i][j] >= '1' && board[i][j] <=\
        \ '9') ? (board[i][j] - '0') : 0;\n                dpSum[i][j] = maxS + score;\n\
        \                dpCnt[i][j] = (int)count;\n            }\n        }\n    }\n\
        \n    int* result = (int*)malloc(2 * sizeof(int));\n    result[0] = dpSum[0][0];\n\
        \    result[1] = dpCnt[0][0];\n    *returnSize = 2;\n    return result;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int[] PathsWithMaxScore(IList<string> board) {\n        int\
        \ n = board.Count;\n        int MOD = 1000000007;\n\n        int[,] dpSum =\
        \ new int[n, n];\n        int[,] dpCnt = new int[n, n];\n\n        dpCnt[n -\
        \ 1, n - 1] = 1;\n\n        for (int i = n - 1; i >= 0; i--) {\n           \
        \ for (int j = n - 1; j >= 0; j--) {\n                if (i == n - 1 && j ==\
        \ n - 1) continue;\n                if (board[i][j] == 'X') continue;\n\n  \
        \              int maxS = -1;\n                long count = 0;\n\n         \
        \       int[] ni_vals = { i + 1, i, i + 1 };\n                int[] nj_vals\
        \ = { j, j + 1, j + 1 };\n\n                for (int d = 0; d < 3; d++) {\n\
        \                    int ni = ni_vals[d];\n                    int nj = nj_vals[d];\n\
        \                    if (ni < n && nj < n && dpCnt[ni, nj] > 0) {\n        \
        \                if (dpSum[ni, nj] > maxS) {\n                            maxS\
        \ = dpSum[ni, nj];\n                            count = dpCnt[ni, nj];\n   \
        \                     } else if (dpSum[ni, nj] == maxS) {\n                \
        \            count = (count + dpCnt[ni, nj]) % MOD;\n                      \
        \  }\n                    }\n                }\n\n                if (maxS !=\
        \ -1) {\n                    int score = (board[i][j] >= '1' && board[i][j]\
        \ <= '9') ? (board[i][j] - '0') : 0;\n                    dpSum[i, j] = maxS\
        \ + score;\n                    dpCnt[i, j] = (int)count;\n                }\n\
        \            }\n        }\n\n        return new int[] { dpSum[0, 0], dpCnt[0,\
        \ 0] };\n    }\n}"
      javascript: "/**\n * @param {string[]} board\n * @return {number[]}\n */\nvar\
        \ pathsWithMaxScore = function(board) {\n    const n = board.length;\n    const\
        \ MOD = 1000000007;\n    const dpSum = Array.from({ length: n }, () => new Int32Array(n).fill(0));\n\
        \    const dpCnt = Array.from({ length: n }, () => new Int32Array(n).fill(0));\n\
        \n    dpCnt[n - 1][n - 1] = 1;\n\n    for (let i = n - 1; i >= 0; i--) {\n \
        \       for (let j = n - 1; j >= 0; j--) {\n            if (i === n - 1 && j\
        \ === n - 1) continue;\n            if (board[i][j] === 'X') continue;\n\n \
        \           let maxS = -1;\n            let count = 0;\n\n            const\
        \ neighbors = [[i + 1, j], [i, j + 1], [i + 1, j + 1]];\n            for (const\
        \ [ni, nj] of neighbors) {\n                if (ni < n && nj < n && dpCnt[ni][nj]\
        \ > 0) {\n                    if (dpSum[ni][nj] > maxS) {\n                \
        \        maxS = dpSum[ni][nj];\n                        count = dpCnt[ni][nj];\n\
        \                    } else if (dpSum[ni][nj] === maxS) {\n                \
        \        count = (count + dpCnt[ni][nj]) % MOD;\n                    }\n   \
        \             }\n            }\n\n            if (maxS !== -1) {\n         \
        \       const score = (board[i][j] >= '1' && board[i][j] <= '9') ? (board[i][j]\
        \ - '0') : 0;\n                dpSum[i][j] = maxS + score;\n               \
        \ dpCnt[i][j] = count;\n            }\n        }\n    }\n\n    return [dpSum[0][0],\
        \ dpCnt[0][0]];\n};"
      typescript: "function pathsWithMaxScore(board: string[]): number[] {\n    const\
        \ n = board.length;\n    const MOD = 1000000007;\n    const dpSum = Array.from({\
        \ length: n }, () => new Int32Array(n).fill(-1));\n    const dpCnt = Array.from({\
        \ length: n }, () => new Int32Array(n).fill(0));\n\n    dpSum[n - 1][n - 1]\
        \ = 0;\n    dpCnt[n - 1][n - 1] = 1;\n\n    for (let r = n - 1; r >= 0; r--)\
        \ {\n        for (let c = n - 1; c >= 0; c--) {\n            if ((r === n -\
        \ 1 && c === n - 1) || board[r][c] === 'X') continue;\n\n            let maxS\
        \ = -1;\n            let count = 0;\n\n            if (r + 1 < n && dpSum[r\
        \ + 1][c] !== -1) {\n                if (dpSum[r + 1][c] > maxS) {\n       \
        \             maxS = dpSum[r + 1][c];\n                    count = dpCnt[r +\
        \ 1][c];\n                } else if (dpSum[r + 1][c] === maxS) {\n         \
        \           count = (count + dpCnt[r + 1][c]) % MOD;\n                }\n  \
        \          }\n            if (c + 1 < n && dpSum[r][c + 1] !== -1) {\n     \
        \           if (dpSum[r][c + 1] > maxS) {\n                    maxS = dpSum[r][c\
        \ + 1];\n                    count = dpCnt[r][c + 1];\n                } else\
        \ if (dpSum[r][c + 1] === maxS) {\n                    count = (count + dpCnt[r][c\
        \ + 1]) % MOD;\n                }\n            }\n            if (r + 1 < n\
        \ && c + 1 < n && dpSum[r + 1][c + 1] !== -1) {\n                if (dpSum[r\
        \ + 1][c + 1] > maxS) {\n                    maxS = dpSum[r + 1][c + 1];\n \
        \                   count = dpCnt[r + 1][c + 1];\n                } else if\
        \ (dpSum[r + 1][c + 1] === maxS) {\n                    count = (count + dpCnt[r\
        \ + 1][c + 1]) % MOD;\n                }\n            }\n\n            if (maxS\
        \ !== -1) {\n                const charVal = board[r][c];\n                const\
        \ val = charVal === 'E' ? 0 : (charVal.charCodeAt(0) - 48);\n              \
        \  dpSum[r][c] = maxS + val;\n                dpCnt[r][c] = count;\n       \
        \     }\n        }\n    }\n\n    if (dpSum[0][0] === -1) return [0, 0];\n  \
        \  return [dpSum[0][0], dpCnt[0][0]];\n}"
      php: "class Solution {\n\n    /**\n     * @param String[] $board\n     * @return\
        \ Integer[]\n     */\n    function pathsWithMaxScore($board) {\n        $n =\
        \ count($board);\n        $mod = 1000000007;\n        $dpSum = array_fill(0,\
        \ $n, array_fill(0, $n, -1));\n        $dpCnt = array_fill(0, $n, array_fill(0,\
        \ $n, 0));\n\n        $dpSum[$n - 1][$n - 1] = 0;\n        $dpCnt[$n - 1][$n\
        \ - 1] = 1;\n\n        for ($r = $n - 1; $r >= 0; $r--) {\n            for ($c\
        \ = $n - 1; $c >= 0; $c--) {\n                if (($r == $n - 1 && $c == $n\
        \ - 1) || $board[$r][$c] == 'X') continue;\n\n                $maxS = -1;\n\
        \                $count = 0;\n\n                if ($r + 1 < $n && $dpSum[$r\
        \ + 1][$c] != -1) {\n                    $s = $dpSum[$r + 1][$c];\n        \
        \            if ($s > $maxS) {\n                        $maxS = $s;\n      \
        \                  $count = $dpCnt[$r + 1][$c];\n                    } else\
        \ if ($s == $maxS) {\n                        $count = ($count + $dpCnt[$r +\
        \ 1][$c]) % $mod;\n                    }\n                }\n              \
        \  if ($c + 1 < $n && $dpSum[$r][$c + 1] != -1) {\n                    $s =\
        \ $dpSum[$r][$c + 1];\n                    if ($s > $maxS) {\n             \
        \           $maxS = $s;\n                        $count = $dpCnt[$r][$c + 1];\n\
        \                    } else if ($s == $maxS) {\n                        $count\
        \ = ($count + $dpCnt[$r][$c + 1]) % $mod;\n                    }\n         \
        \       }\n                if ($r + 1 < $n && $c + 1 < $n && $dpSum[$r + 1][$c\
        \ + 1] != -1) {\n                    $s = $dpSum[$r + 1][$c + 1];\n        \
        \            if ($s > $maxS) {\n                        $maxS = $s;\n      \
        \                  $count = $dpCnt[$r + 1][$c + 1];\n                    } else\
        \ if ($s == $maxS) {\n                        $count = ($count + $dpCnt[$r +\
        \ 1][$c + 1]) % $mod;\n                    }\n                }\n\n        \
        \        if ($maxS != -1) {\n                    $char = $board[$r][$c];\n \
        \                   $val = ($char == 'E') ? 0 : (ord($char) - 48);\n       \
        \             $dpSum[$r][$c] = $maxS + $val;\n                    $dpCnt[$r][$c]\
        \ = $count;\n                }\n            }\n        }\n\n        if ($dpSum[0][0]\
        \ == -1) return [0, 0];\n        return [$dpSum[0][0], $dpCnt[0][0]];\n    }\n\
        }"
      swift: "class Solution {\n    func pathsWithMaxScore(_ board: [String]) -> [Int]\
        \ {\n        let n = board.count\n        let mod = 1_000_000_007\n        let\
        \ grid = board.map { Array($0) }\n        var dpSum = Array(repeating: Array(repeating:\
        \ -1, count: n), count: n)\n        var dpCnt = Array(repeating: Array(repeating:\
        \ 0, count: n), count: n)\n\n        dpSum[n - 1][n - 1] = 0\n        dpCnt[n\
        \ - 1][n - 1] = 1\n\n        for r in stride(from: n - 1, through: 0, by: -1)\
        \ {\n            for c in stride(from: n - 1, through: 0, by: -1) {\n      \
        \          if (r == n - 1 && c == n - 1) || grid[r][c] == \"X\" { continue }\n\
        \n                var maxS = -1\n                var count = 0\n\n         \
        \       if r + 1 < n && dpSum[r + 1][c] != -1 {\n                    let s =\
        \ dpSum[r + 1][c]\n                    if s > maxS {\n                     \
        \   maxS = s\n                        count = dpCnt[r + 1][c]\n            \
        \        } else if s == maxS {\n                        count = (count + dpCnt[r\
        \ + 1][c]) % mod\n                    }\n                }\n               \
        \ if c + 1 < n && dpSum[r][c + 1] != -1 {\n                    let s = dpSum[r][c\
        \ + 1]\n                    if s > maxS {\n                        maxS = s\n\
        \                        count = dpCnt[r][c + 1]\n                    } else\
        \ if s == maxS {\n                        count = (count + dpCnt[r][c + 1])\
        \ % mod\n                    }\n                }\n                if r + 1\
        \ < n && c + 1 < n && dpSum[r + 1][c + 1] != -1 {\n                    let s\
        \ = dpSum[r + 1][c + 1]\n                    if s > maxS {\n               \
        \         maxS = s\n                        count = dpCnt[r + 1][c + 1]\n  \
        \                  } else if s == maxS {\n                        count = (count\
        \ + dpCnt[r + 1][c + 1]) % mod\n                    }\n                }\n\n\
        \                if maxS != -1 {\n                    let char = grid[r][c]\n\
        \                    let val = char == \"E\" ? 0 : Int(char.asciiValue! - 48)\n\
        \                    dpSum[r][c] = maxS + val\n                    dpCnt[r][c]\
        \ = count\n                }\n            }\n        }\n\n        if dpSum[0][0]\
        \ == -1 { return [0, 0] }\n        return [dpSum[0][0], dpCnt[0][0]]\n    }\n\
        }"
      kotlin: "class Solution {\n    fun pathsWithMaxScore(board: List<String>): IntArray\
        \ {\n        val n = board.size\n        val mod = 1_000_000_007\n        val\
        \ dpSum = Array(n) { IntArray(n) { -1 } }\n        val dpCnt = Array(n) { IntArray(n)\
        \ { 0 } }\n\n        dpSum[n - 1][n - 1] = 0\n        dpCnt[n - 1][n - 1] =\
        \ 1\n\n        for (r in n - 1 downTo 0) {\n            for (c in n - 1 downTo\
        \ 0) {\n                if ((r == n - 1 && c == n - 1) || board[r][c] == 'X')\
        \ continue\n\n                var maxS = -1\n                var count = 0\n\
        \n                if (r + 1 < n && dpSum[r + 1][c] != -1) {\n              \
        \      val s = dpSum[r + 1][c]\n                    if (s > maxS) {\n      \
        \                  maxS = s\n                        count = dpCnt[r + 1][c]\n\
        \                    } else if (s == maxS) {\n                        count\
        \ = (count + dpCnt[r + 1][c]) % mod\n                    }\n               \
        \ }\n                if (c + 1 < n && dpSum[r][c + 1] != -1) {\n           \
        \         val s = dpSum[r][c + 1]\n                    if (s > maxS) {\n   \
        \                     maxS = s\n                        count = dpCnt[r][c +\
        \ 1]\n                    } else if (s == maxS) {\n                        count\
        \ = (count + dpCnt[r][c + 1]) % mod\n                    }\n               \
        \ }\n                if (r + 1 < n && c + 1 < n && dpSum[r + 1][c + 1] != -1)\
        \ {\n                    val s = dpSum[r + 1][c + 1]\n                    if\
        \ (s > maxS) {\n                        maxS = s\n                        count\
        \ = dpCnt[r + 1][c + 1]\n                    } else if (s == maxS) {\n     \
        \                   count = (count + dpCnt[r + 1][c + 1]) % mod\n          \
        \          }\n                }\n\n                if (maxS != -1) {\n     \
        \               val v = if (board[r][c] == 'E') 0 else (board[r][c] - '0')\n\
        \                    dpSum[r][c] = maxS + v\n                    dpCnt[r][c]\
        \ = count\n                }\n            }\n        }\n\n        if (dpSum[0][0]\
        \ == -1) return intArrayOf(0, 0)\n        return intArrayOf(dpSum[0][0], dpCnt[0][0])\n\
        \    }\n}"
      dart: "class Solution {\n  List<int> pathsWithMaxScore(List<String> board) {\n\
        \    int n = board.length;\n    int mod = 1000000007;\n    List<List<int>> dpScore\
        \ = List.generate(n, (_) => List.filled(n, 0));\n    List<List<int>> dpCount\
        \ = List.generate(n, (_) => List.filled(n, 0));\n    dpCount[n - 1][n - 1] =\
        \ 1;\n    for (int i = n - 1; i >= 0; i--) {\n      for (int j = n - 1; j >=\
        \ 0; j--) {\n        if ((i == n - 1 && j == n - 1) || board[i][j] == 'X') continue;\n\
        \        int maxS = -1;\n        int paths = 0;\n        if (i + 1 < n && dpCount[i\
        \ + 1][j] > 0) {\n          if (dpScore[i + 1][j] > maxS) {\n            maxS\
        \ = dpScore[i + 1][j];\n            paths = dpCount[i + 1][j];\n          }\
        \ else if (dpScore[i + 1][j] == maxS) {\n            paths = (paths + dpCount[i\
        \ + 1][j]) % mod;\n          }\n        }\n        if (j + 1 < n && dpCount[i][j\
        \ + 1] > 0) {\n          if (dpScore[i][j + 1] > maxS) {\n            maxS =\
        \ dpScore[i][j + 1];\n            paths = dpCount[i][j + 1];\n          } else\
        \ if (dpScore[i][j + 1] == maxS) {\n            paths = (paths + dpCount[i][j\
        \ + 1]) % mod;\n          }\n        }\n        if (i + 1 < n && j + 1 < n &&\
        \ dpCount[i + 1][j + 1] > 0) {\n          if (dpScore[i + 1][j + 1] > maxS)\
        \ {\n            maxS = dpScore[i + 1][j + 1];\n            paths = dpCount[i\
        \ + 1][j + 1];\n          } else if (dpScore[i + 1][j + 1] == maxS) {\n    \
        \        paths = (paths + dpCount[i + 1][j + 1]) % mod;\n          }\n     \
        \   }\n        if (maxS != -1) {\n          int val = board[i][j] == 'E' ? 0\
        \ : int.parse(board[i][j]);\n          dpScore[i][j] = maxS + val;\n       \
        \   dpCount[i][j] = paths;\n        }\n      }\n    }\n    if (dpCount[0][0]\
        \ == 0) return [0, 0];\n    return [dpScore[0][0], dpCount[0][0]];\n  }\n}"
      go: "func pathsWithMaxScore(board []string) []int {\n\tn := len(board)\n\tmod\
        \ := 1000000007\n\tdpScore := make([][]int, n)\n\tdpCount := make([][]int, n)\n\
        \tfor i := range dpScore {\n\t\tdpScore[i] = make([]int, n)\n\t\tdpCount[i]\
        \ = make([]int, n)\n\t}\n\tdpCount[n-1][n-1] = 1\n\tfor i := n - 1; i >= 0;\
        \ i-- {\n\t\tfor j := n - 1; j >= 0; j-- {\n\t\t\tif (i == n-1 && j == n-1)\
        \ || board[i][j] == 'X' {\n\t\t\t\tcontinue\n\t\t\t}\n\t\t\tmaxS := -1\n\t\t\
        \tpaths := 0\n\t\t\tif i+1 < n && dpCount[i+1][j] > 0 {\n\t\t\t\tif dpScore[i+1][j]\
        \ > maxS {\n\t\t\t\t\tmaxS = dpScore[i+1][j]\n\t\t\t\t\tpaths = dpCount[i+1][j]\n\
        \t\t\t\t} else if dpScore[i+1][j] == maxS {\n\t\t\t\t\tpaths = (paths + dpCount[i+1][j])\
        \ % mod\n\t\t\t\t}\n\t\t\t}\n\t\t\tif j+1 < n && dpCount[i][j+1] > 0 {\n\t\t\
        \t\tif dpScore[i][j+1] > maxS {\n\t\t\t\t\tmaxS = dpScore[i][j+1]\n\t\t\t\t\t\
        paths = dpCount[i][j+1]\n\t\t\t\t} else if dpScore[i][j+1] == maxS {\n\t\t\t\
        \t\tpaths = (paths + dpCount[i][j+1]) % mod\n\t\t\t\t}\n\t\t\t}\n\t\t\tif i+1\
        \ < n && j+1 < n && dpCount[i+1][j+1] > 0 {\n\t\t\t\tif dpScore[i+1][j+1] >\
        \ maxS {\n\t\t\t\t\tmaxS = dpScore[i+1][j+1]\n\t\t\t\t\tpaths = dpCount[i+1][j+1]\n\
        \t\t\t\t} else if dpScore[i+1][j+1] == maxS {\n\t\t\t\t\tpaths = (paths + dpCount[i+1][j+1])\
        \ % mod\n\t\t\t\t}\n\t\t\t}\n\t\t\tif maxS != -1 {\n\t\t\t\tval := 0\n\t\t\t\
        \tif board[i][j] != 'E' {\n\t\t\t\t\tval = int(board[i][j] - '0')\n\t\t\t\t\
        }\n\t\t\t\tdpScore[i][j] = maxS + val\n\t\t\t\tdpCount[i][j] = paths\n\t\t\t\
        }\n\t\t}\n\t}\n\tif dpCount[0][0] == 0 {\n\t\treturn []int{0, 0}\n\t}\n\treturn\
        \ []int{dpScore[0][0], dpCount[0][0]}\n}"
      ruby: "def paths_with_max_score(board)\n  n = board.length\n  mod = 1_000_000_007\n\
        \  dp_score = Array.new(n) { Array.new(n, 0) }\n  dp_count = Array.new(n) {\
        \ Array.new(n, 0) }\n  dp_count[n-1][n-1] = 1\n  (n-1).step(0, -1) do |i|\n\
        \    (n-1).step(0, -1) do |j|\n      next if (i == n-1 && j == n-1) || board[i][j]\
        \ == 'X'\n      max_s = -1\n      paths = 0\n      [[i+1, j], [i, j+1], [i+1,\
        \ j+1]].each do |ni, nj|\n        if ni < n && nj < n && dp_count[ni][nj] >\
        \ 0\n          if dp_score[ni][nj] > max_s\n            max_s = dp_score[ni][nj]\n\
        \            paths = dp_count[ni][nj]\n          elsif dp_score[ni][nj] == max_s\n\
        \            paths = (paths + dp_count[ni][nj]) % mod\n          end\n     \
        \   end\n      end\n      if max_s != -1\n        val = board[i][j] == 'E' ?\
        \ 0 : board[i][j].to_i\n        dp_score[i][j] = max_s + val\n        dp_count[i][j]\
        \ = paths\n      end\n    end\n  end\n  dp_count[0][0] == 0 ? [0, 0] : [dp_score[0][0],\
        \ dp_count[0][0]]\nend"
      scala: "object Solution {\n    def pathsWithMaxScore(board: List[String]): Array[Int]\
        \ = {\n        val n = board.length\n        val mod = 1000000007\n        val\
        \ dpScore = Array.ofDim[Int](n, n)\n        val dpCount = Array.ofDim[Int](n,\
        \ n)\n        dpCount(n - 1)(n - 1) = 1\n        for (i <- n - 1 to 0 by -1)\
        \ {\n            for (j <- n - 1 to 0 by -1) {\n                if (!((i ==\
        \ n - 1 && j == n - 1) || board(i)(j) == 'X')) {\n                    var maxS\
        \ = -1\n                    var paths = 0\n                    if (i + 1 < n\
        \ && dpCount(i + 1)(j) > 0) {\n                        if (dpScore(i + 1)(j)\
        \ > maxS) {\n                            maxS = dpScore(i + 1)(j)\n        \
        \                    paths = dpCount(i + 1)(j)\n                        } else\
        \ if (dpScore(i + 1)(j) == maxS) {\n                            paths = (paths\
        \ + dpCount(i + 1)(j)) % mod\n                        }\n                  \
        \  }\n                    if (j + 1 < n && dpCount(i)(j + 1) > 0) {\n      \
        \                  if (dpScore(i)(j + 1) > maxS) {\n                       \
        \     maxS = dpScore(i)(j + 1)\n                            paths = dpCount(i)(j\
        \ + 1)\n                        } else if (dpScore(i)(j + 1) == maxS) {\n  \
        \                          paths = (paths + dpCount(i)(j + 1)) % mod\n     \
        \                   }\n                    }\n                    if (i + 1\
        \ < n && j + 1 < n && dpCount(i + 1)(j + 1) > 0) {\n                       \
        \ if (dpScore(i + 1)(j + 1) > maxS) {\n                            maxS = dpScore(i\
        \ + 1)(j + 1)\n                            paths = dpCount(i + 1)(j + 1)\n \
        \                       } else if (dpScore(i + 1)(j + 1) == maxS) {\n      \
        \                      paths = (paths + dpCount(i + 1)(j + 1)) % mod\n     \
        \                   }\n                    }\n                    if (maxS !=\
        \ -1) {\n                        val v = if (board(i)(j) == 'E') 0 else board(i)(j).asDigit\n\
        \                        dpScore(i)(j) = maxS + v\n                        dpCount(i)(j)\
        \ = paths\n                    }\n                }\n            }\n       \
        \ }\n        if (dpCount(0)(0) == 0) Array(0, 0)\n        else Array(dpScore(0)(0),\
        \ dpCount(0)(0))\n    }\n}"
      rust: "impl Solution {\n    pub fn paths_with_max_score(board: Vec<String>) ->\
        \ Vec<i32> {\n        let n = board.len();\n        let b: Vec<Vec<u8>> = board.into_iter().map(|s|\
        \ s.into_bytes()).collect();\n        let mut dp_sum = vec![vec![0; n]; n];\n\
        \        let mut dp_cnt = vec![vec![0; n]; n];\n        let mod_val = 1_000_000_007;\n\
        \n        dp_cnt[n - 1][n - 1] = 1;\n\n        for i in (0..n).rev() {\n   \
        \         for j in (0..n).rev() {\n                if (i == n - 1 && j == n\
        \ - 1) || b[i][j] == b'X' {\n                    continue;\n               \
        \ }\n\n                let mut max_s = -1;\n                let mut count =\
        \ 0;\n\n                let neighbors = [(i + 1, j), (i, j + 1), (i + 1, j +\
        \ 1)];\n                for (ni, nj) in neighbors {\n                    if\
        \ ni < n && nj < n && dp_cnt[ni][nj] > 0 {\n                        if dp_sum[ni][nj]\
        \ > max_s {\n                            max_s = dp_sum[ni][nj];\n         \
        \                   count = dp_cnt[ni][nj];\n                        } else\
        \ if dp_sum[ni][nj] == max_s {\n                            count = (count +\
        \ dp_cnt[ni][nj]) % mod_val;\n                        }\n                  \
        \  }\n                }\n\n                if max_s != -1 {\n              \
        \      let cur_val = if b[i][j] == b'E' { 0 } else { (b[i][j] - b'0') as i32\
        \ };\n                    dp_sum[i][j] = max_s + cur_val;\n                \
        \    dp_cnt[i][j] = count;\n                }\n            }\n        }\n\n\
        \        vec![dp_sum[0][0], dp_cnt[0][0]]\n    }\n}"
      racket: "(define/contract (paths-with-max-score board)\n  (-> (listof string?)\
        \ (listof integer?))\n  (let* ([n (length board)]\n         [grid (list->vector\
        \ (map (lambda (s) (list->vector (string->list s))) board))]\n         [dp-sum\
        \ (make-vector (* n n) 0)]\n         [dp-cnt (make-vector (* n n) 0)]\n    \
        \     [mod 1000000007])\n    (define (get-idx r c) (+ (* r n) c))\n    (vector-set!\
        \ dp-cnt (get-idx (- n 1) (- n 1)) 1)\n    (for ([r (in-range (- n 1) -1 -1)])\n\
        \      (for ([c (in-range (- n 1) -1 -1)])\n        (let ([char (vector-ref\
        \ (vector-ref grid r) c)])\n          (unless (or (and (= r (- n 1)) (= c (-\
        \ n 1))) (char=? char #\\X))\n            (let ([max-s -1]\n               \
        \   [count 0])\n              (for ([move (list (list (+ r 1) c) (list r (+\
        \ c 1)) (list (+ r 1) (+ c 1)))])\n                (let ([nr (car move)] [nc\
        \ (cadr move)])\n                  (when (and (< nr n) (< nc n) (> (vector-ref\
        \ dp-cnt (get-idx nr nc)) 0))\n                    (let ([s (vector-ref dp-sum\
        \ (get-idx nr nc))]\n                          [cnt (vector-ref dp-cnt (get-idx\
        \ nr nc))])\n                      (cond\n                        [(> s max-s)\
        \ (set! max-s s) (set! count cnt)]\n                        [(= s max-s) (set!\
        \ count (modulo (+ count cnt) mod))])))))\n              (when (not (= max-s\
        \ -1))\n                (let ([val (if (char=? char #\\E) 0 (- (char->integer\
        \ char) 48))])\n                  (vector-set! dp-sum (get-idx r c) (+ max-s\
        \ val))\n                  (vector-set! dp-cnt (get-idx r c) count))))))))\n\
        \    (list (vector-ref dp-sum 0) (vector-ref dp-cnt 0))))"
      erlang: "-spec paths_with_max_score(Board :: [unicode:unicode_binary()]) -> [integer()].\n\
        paths_with_max_score(Board) ->\n    N = length(Board),\n    Grid = list_to_tuple([list_to_tuple(binary_to_list(Row))\
        \ || Row <- Board]),\n    Mod = 1000000007,\n    DP = solve(N, Grid, Mod),\n\
        \    {S, C} = maps:get({0, 0}, DP, {0, 0}),\n    [S, C].\n\nsolve(N, Grid, Mod)\
        \ ->\n    lists:foldl(fun(R, AccR) ->\n        lists:foldl(fun(C, AccC) ->\n\
        \            Row = element(R + 1, Grid),\n            Char = element(C + 1,\
        \ Row),\n            if\n                R == N - 1, C == N - 1 ->\n       \
        \             maps:put({R, C}, {0, 1}, AccC);\n                Char == $X ->\n\
        \                    maps:put({R, C}, {0, 0}, AccC);\n                true ->\n\
        \                    Neighbors = [{R + 1, C}, {R, C + 1}, {R + 1, C + 1}],\n\
        \                    {MaxS, Count} = lists:foldl(fun({NR, NC}, {MS, MC}) ->\n\
        \                        case maps:get({NR, NC}, AccC, {0, 0}) of\n        \
        \                    {S, CV} when CV > 0 ->\n                              \
        \  if\n                                    S > MS -> {S, CV};\n            \
        \                        S == MS -> {MS, (MC + CV) rem Mod};\n             \
        \                       true -> {MS, MC}\n                                end;\n\
        \                            _ -> {MS, MC}\n                        end\n  \
        \                  end, {-1, 0}, Neighbors),\n                    if\n     \
        \                   MaxS == -1 ->\n                            maps:put({R,\
        \ C}, {0, 0}, AccC);\n                        true ->\n                    \
        \        Val = if Char == $E -> 0; true -> Char - $0 end,\n                \
        \            maps:put({R, C}, {MaxS + Val, Count}, AccC)\n                 \
        \   end\n            end\n        end, AccR, lists:seq(N - 1, 0, -1))\n    end,\
        \ #{}, lists:seq(N - 1, 0, -1))."
      elixir: "defmodule Solution do\n  @spec paths_with_max_score(board :: [String.t])\
        \ :: [integer]\n  def paths_with_max_score(board) do\n    n = length(board)\n\
        \    grid = board\n           |> Enum.map(fn row -> String.to_charlist(row)\
        \ |> List.to_tuple() end)\n           |> List.to_tuple()\n    mod = 1_000_000_007\n\
        \n    dp = Enum.reduce((n - 1)..0, %{}, fn r, acc_r ->\n      Enum.reduce((n\
        \ - 1)..0, acc_r, fn c, acc_c ->\n        char = elem(elem(grid, r), c)\n  \
        \      cond do\n          r == n - 1 and c == n - 1 ->\n            Map.put(acc_c,\
        \ {r, c}, {0, 1})\n          char == ?X ->\n            Map.put(acc_c, {r, c},\
        \ {0, 0})\n          true ->\n            moves = [{r + 1, c}, {r, c + 1}, {r\
        \ + 1, c + 1}]\n            {max_s, count} = Enum.reduce(moves, {-1, 0}, fn\
        \ {nr, nc}, {ms, mc} ->\n              case Map.get(acc_c, {nr, nc}) do\n  \
        \              {s, c_val} when c_val > 0 ->\n                  cond do\n   \
        \                 s > ms -> {s, c_val}\n                    s == ms -> {ms,\
        \ rem(mc + c_val, mod)}\n                    true -> {ms, mc}\n            \
        \      end\n                _ -> {ms, mc}\n              end\n            end)\n\
        \n            if max_s == -1 do\n              Map.put(acc_c, {r, c}, {0, 0})\n\
        \            else\n              val = if char == ?E, do: 0, else: char - ?0\n\
        \              Map.put(acc_c, {r, c}, {max_s + val, count})\n            end\n\
        \        end\n      end)\n    end)\n\n    {s, c} = Map.get(dp, {0, 0}, {0, 0})\n\
        \    [s, c]\n  end\nend"
    approach: 'The problem can be solved using dynamic programming by maintaining two
      grids (or a grid of pairs) to store the maximum score and the number of paths
      achieving that score for each cell. We iterate backward through the $N \times
      N$ grid, starting from the ''S'' square at the bottom-right corner and ending
      at the ''E'' square at the top-left corner. For each cell $(i, j)$, we evaluate
      incoming paths from three potential neighboring cells: $(i+1, j)$, $(i, j+1)$,
      and $(i+1, j+1)$, which represent moving up, left, or up-left respectively from
      the perspective of the starting point.


      For every non-obstacle cell, we determine the maximum score among its reachable
      neighbors and calculate the total number of paths that result in this maximum
      score. Path counts are summed and taken modulo $10^9 + 7$. If a cell is an obstacle
      ''X'' or has no reachable neighbors, its path count remains zero, signifying it
      cannot be part of a valid path to the destination. The values of ''E'' and ''S''
      are treated as zero, while numeric characters are added to the maximum score from
      the chosen neighbors. The final result for the ''E'' cell at $(0, 0)$ gives the
      maximum score and the total number of such paths.'
    time_complexity: O(N^2) where $N$ is the side length of the board. The algorithm
      iterates through each of the $N \times N$ cells exactly once, and for each cell,
      it performs a constant number of operations to check three adjacent neighbors.
    space_complexity: O(N^2) as the algorithm uses two $N \times N$ grids to store the
      maximum scores and the count of paths for every cell on the board. This can be
      optimized to $O(N)$ space using row-based DP, but $O(N^2)$ is well within limits
      for $N=100$.
    elapsed_time: 640.4297080039978
    model: gemini-3-flash-preview
    generated_at: '2026-07-05 02:35:10 '
---

## Problem #1301: Number of Paths with Max Score

**Difficulty:** Hard

**Topics:** Array, Dynamic Programming, Matrix

## Problem Description

<p>You are given a square <code>board</code>&nbsp;of characters. You can move on the board starting at the bottom right square marked with the character&nbsp;<code>&#39;S&#39;</code>.</p>

<p>You need&nbsp;to reach the top left square marked with the character <code>&#39;E&#39;</code>. The rest of the squares are labeled either with a numeric character&nbsp;<code>1, 2, ..., 9</code> or with an obstacle <code>&#39;X&#39;</code>. In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.</p>

<p>Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect, and the second is the number of such paths that you can take to get that maximum sum, <strong>taken modulo <code>10^9 + 7</code></strong>.</p>

<p>In case there is no path, return&nbsp;<code>[0, 0]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> board = ["E23","2X2","12S"]
<strong>Output:</strong> [7,1]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> board = ["E12","1X1","21S"]
<strong>Output:</strong> [4,2]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> board = ["E11","XXX","11S"]
<strong>Output:</strong> [0,0]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= board.length == board[i].length &lt;= 100</code></li>
</ul>

## Hints

1. Use dynamic programming to find the path with the max score.

2. Use another dynamic programming array to count the number of paths with max score.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be solved using dynamic programming by maintaining two grids (or a grid of pairs) to store the maximum score and the number of paths achieving that score for each cell. We iterate backward through the $N \times N$ grid, starting from the 'S' square at the bottom-right corner and ending at the 'E' square at the top-left corner. For each cell $(i, j)$, we evaluate incoming paths from three potential neighboring cells: $(i+1, j)$, $(i, j+1)$, and $(i+1, j+1)$, which represent moving up, left, or up-left respectively from the perspective of the starting point.

For every non-obstacle cell, we determine the maximum score among its reachable neighbors and calculate the total number of paths that result in this maximum score. Path counts are summed and taken modulo $10^9 + 7$. If a cell is an obstacle 'X' or has no reachable neighbors, its path count remains zero, signifying it cannot be part of a valid path to the destination. The values of 'E' and 'S' are treated as zero, while numeric characters are added to the maximum score from the chosen neighbors. The final result for the 'E' cell at $(0, 0)$ gives the maximum score and the total number of such paths.

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
#include <string>
#include <utility>

using namespace std;

class Solution {
public:
    vector<int> pathsWithMaxScore(vector<string>& board) {
        int n = board.size();
        int mod = 1000000007;
        vector<vector<pair<int, int>>> dp(n, vector<pair<int, int>>(n, {0, 0}));
        dp[n - 1][n - 1] = {0, 1};

        for (int i = n - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                if ((i == n - 1 && j == n - 1) || board[i][j] == 'X') continue;

                int maxS = -1;
                long long count = 0;
                int dirs[3][2] = {{i + 1, j}, {i, j + 1}, {i + 1, j + 1}};

                for (int k = 0; k < 3; ++k) {
                    int ni = dirs[k][0], nj = dirs[k][1];
                    if (ni < n && nj < n && dp[ni][nj].second > 0) {
                        if (dp[ni][nj].first > maxS) {
                            maxS = dp[ni][nj].first;
                            count = dp[ni][nj].second;
                        } else if (dp[ni][nj].first == maxS) {
                            count = (count + dp[ni][nj].second) % mod;
                        }
                    }
                }

                if (maxS != -1) {
                    int val = (board[i][j] == 'E' ? 0 : board[i][j] - '0');
                    dp[i][j] = {val + maxS, (int)count};
                }
            }
        }

        return {dp[0][0].first, dp[0][0].second};
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.List;

class Solution {
    public int[] pathsWithMaxScore(List<String> board) {
        int n = board.size();
        int mod = 1000000007;
        int[][] dpSum = new int[n][n];
        int[][] dpCount = new int[n][n];
        dpCount[n - 1][n - 1] = 1;

        for (int i = n - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if ((i == n - 1 && j == n - 1) || board.get(i).charAt(j) == 'X') continue;

                int maxS = -1;
                long count = 0;
                int[][] dirs = {{i + 1, j}, {i, j + 1}, {i + 1, j + 1}};

                for (int[] d : dirs) {
                    int ni = d[0], nj = d[1];
                    if (ni < n && nj < n && dpCount[ni][nj] > 0) {
                        if (dpSum[ni][nj] > maxS) {
                            maxS = dpSum[ni][nj];
                            count = dpCount[ni][nj];
                        } else if (dpSum[ni][nj] == maxS) {
                            count = (count + dpCount[ni][nj]) % mod;
                        }
                    }
                }

                if (maxS != -1) {
                    char c = board.get(i).charAt(j);
                    int val = (c == 'E' ? 0 : c - '0');
                    dpSum[i][j] = val + maxS;
                    dpCount[i][j] = (int) count;
                }
            }
        }

        return new int[]{dpSum[0][0], dpCount[0][0]};
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        n = len(board)
        MOD = 10**9 + 7
        dp_sum = [[0] * n for _ in range(n)]
        dp_count = [[0] * n for _ in range(n)]
        dp_count[n-1][n-1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if (i == n - 1 and j == n - 1) or board[i][j] == 'X':
                    continue

                max_s = -1
                count = 0
                for ni, nj in [(i + 1, j), (i, j + 1), (i + 1, j + 1)]:
                    if ni < n and nj < n and dp_count[ni][nj] > 0:
                        if dp_sum[ni][nj] > max_s:
                            max_s = dp_sum[ni][nj]
                            count = dp_count[ni][nj]
                        elif dp_sum[ni][nj] == max_s:
                            count = (count + dp_count[ni][nj]) % MOD

                if max_s != -1:
                    char = board[i][j]
                    val = int(char) if '1' <= char <= '9' else 0
                    dp_sum[i][j] = val + max_s
                    dp_count[i][j] = count % MOD

        return [dp_sum[0][0], dp_count[0][0]]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7
        dp_sum = [[0] * n for _ in range(n)]
        dp_cnt = [[0] * n for _ in range(n)]

        dp_cnt[n-1][n-1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == n - 1 and j == n - 1:
                    continue
                if board[i][j] == 'X':
                    continue

                max_s = -1
                count = 0

                for ni, nj in [(i + 1, j), (i, j + 1), (i + 1, j + 1)]:
                    if ni < n and nj < n and dp_cnt[ni][nj] > 0:
                        if dp_sum[ni][nj] > max_s:
                            max_s = dp_sum[ni][nj]
                            count = dp_cnt[ni][nj]
                        elif dp_sum[ni][nj] == max_s:
                            count = (count + dp_cnt[ni][nj]) % MOD

                if max_s != -1:
                    score = int(board[i][j]) if '1' <= board[i][j] <= '9' else 0
                    dp_sum[i][j] = max_s + score
                    dp_cnt[i][j] = count

        return [dp_sum[0][0], dp_cnt[0][0]]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* pathsWithMaxScore(char ** board, int boardSize, int* returnSize){
    int n = boardSize;
    int MOD = 1000000007;

    int dpSum[100][100];
    int dpCnt[100][100];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            dpSum[i][j] = 0;
            dpCnt[i][j] = 0;
        }
    }

    dpCnt[n-1][n-1] = 1;

    for (int i = n - 1; i >= 0; i--) {
        for (int j = n - 1; j >= 0; j--) {
            if (i == n - 1 && j == n - 1) continue;
            if (board[i][j] == 'X') continue;

            int maxS = -1;
            long long count = 0;

            int ni_vals[3] = {i + 1, i, i + 1};
            int nj_vals[3] = {j, j + 1, j + 1};

            for (int d = 0; d < 3; d++) {
                int ni = ni_vals[d];
                int nj = nj_vals[d];
                if (ni < n && nj < n && dpCnt[ni][nj] > 0) {
                    if (dpSum[ni][nj] > maxS) {
                        maxS = dpSum[ni][nj];
                        count = dpCnt[ni][nj];
                    } else if (dpSum[ni][nj] == maxS) {
                        count = (count + dpCnt[ni][nj]) % MOD;
                    }
                }
            }

            if (maxS != -1) {
                int score = (board[i][j] >= '1' && board[i][j] <= '9') ? (board[i][j] - '0') : 0;
                dpSum[i][j] = maxS + score;
                dpCnt[i][j] = (int)count;
            }
        }
    }

    int* result = (int*)malloc(2 * sizeof(int));
    result[0] = dpSum[0][0];
    result[1] = dpCnt[0][0];
    *returnSize = 2;
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

public class Solution {
    public int[] PathsWithMaxScore(IList<string> board) {
        int n = board.Count;
        int MOD = 1000000007;

        int[,] dpSum = new int[n, n];
        int[,] dpCnt = new int[n, n];

        dpCnt[n - 1, n - 1] = 1;

        for (int i = n - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (i == n - 1 && j == n - 1) continue;
                if (board[i][j] == 'X') continue;

                int maxS = -1;
                long count = 0;

                int[] ni_vals = { i + 1, i, i + 1 };
                int[] nj_vals = { j, j + 1, j + 1 };

                for (int d = 0; d < 3; d++) {
                    int ni = ni_vals[d];
                    int nj = nj_vals[d];
                    if (ni < n && nj < n && dpCnt[ni, nj] > 0) {
                        if (dpSum[ni, nj] > maxS) {
                            maxS = dpSum[ni, nj];
                            count = dpCnt[ni, nj];
                        } else if (dpSum[ni, nj] == maxS) {
                            count = (count + dpCnt[ni, nj]) % MOD;
                        }
                    }
                }

                if (maxS != -1) {
                    int score = (board[i][j] >= '1' && board[i][j] <= '9') ? (board[i][j] - '0') : 0;
                    dpSum[i, j] = maxS + score;
                    dpCnt[i, j] = (int)count;
                }
            }
        }

        return new int[] { dpSum[0, 0], dpCnt[0, 0] };
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string[]} board
 * @return {number[]}
 */
var pathsWithMaxScore = function(board) {
    const n = board.length;
    const MOD = 1000000007;
    const dpSum = Array.from({ length: n }, () => new Int32Array(n).fill(0));
    const dpCnt = Array.from({ length: n }, () => new Int32Array(n).fill(0));

    dpCnt[n - 1][n - 1] = 1;

    for (let i = n - 1; i >= 0; i--) {
        for (let j = n - 1; j >= 0; j--) {
            if (i === n - 1 && j === n - 1) continue;
            if (board[i][j] === 'X') continue;

            let maxS = -1;
            let count = 0;

            const neighbors = [[i + 1, j], [i, j + 1], [i + 1, j + 1]];
            for (const [ni, nj] of neighbors) {
                if (ni < n && nj < n && dpCnt[ni][nj] > 0) {
                    if (dpSum[ni][nj] > maxS) {
                        maxS = dpSum[ni][nj];
                        count = dpCnt[ni][nj];
                    } else if (dpSum[ni][nj] === maxS) {
                        count = (count + dpCnt[ni][nj]) % MOD;
                    }
                }
            }

            if (maxS !== -1) {
                const score = (board[i][j] >= '1' && board[i][j] <= '9') ? (board[i][j] - '0') : 0;
                dpSum[i][j] = maxS + score;
                dpCnt[i][j] = count;
            }
        }
    }

    return [dpSum[0][0], dpCnt[0][0]];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function pathsWithMaxScore(board: string[]): number[] {
    const n = board.length;
    const MOD = 1000000007;
    const dpSum = Array.from({ length: n }, () => new Int32Array(n).fill(-1));
    const dpCnt = Array.from({ length: n }, () => new Int32Array(n).fill(0));

    dpSum[n - 1][n - 1] = 0;
    dpCnt[n - 1][n - 1] = 1;

    for (let r = n - 1; r >= 0; r--) {
        for (let c = n - 1; c >= 0; c--) {
            if ((r === n - 1 && c === n - 1) || board[r][c] === 'X') continue;

            let maxS = -1;
            let count = 0;

            if (r + 1 < n && dpSum[r + 1][c] !== -1) {
                if (dpSum[r + 1][c] > maxS) {
                    maxS = dpSum[r + 1][c];
                    count = dpCnt[r + 1][c];
                } else if (dpSum[r + 1][c] === maxS) {
                    count = (count + dpCnt[r + 1][c]) % MOD;
                }
            }
            if (c + 1 < n && dpSum[r][c + 1] !== -1) {
                if (dpSum[r][c + 1] > maxS) {
                    maxS = dpSum[r][c + 1];
                    count = dpCnt[r][c + 1];
                } else if (dpSum[r][c + 1] === maxS) {
                    count = (count + dpCnt[r][c + 1]) % MOD;
                }
            }
            if (r + 1 < n && c + 1 < n && dpSum[r + 1][c + 1] !== -1) {
                if (dpSum[r + 1][c + 1] > maxS) {
                    maxS = dpSum[r + 1][c + 1];
                    count = dpCnt[r + 1][c + 1];
                } else if (dpSum[r + 1][c + 1] === maxS) {
                    count = (count + dpCnt[r + 1][c + 1]) % MOD;
                }
            }

            if (maxS !== -1) {
                const charVal = board[r][c];
                const val = charVal === 'E' ? 0 : (charVal.charCodeAt(0) - 48);
                dpSum[r][c] = maxS + val;
                dpCnt[r][c] = count;
            }
        }
    }

    if (dpSum[0][0] === -1) return [0, 0];
    return [dpSum[0][0], dpCnt[0][0]];
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String[] $board
     * @return Integer[]
     */
    function pathsWithMaxScore($board) {
        $n = count($board);
        $mod = 1000000007;
        $dpSum = array_fill(0, $n, array_fill(0, $n, -1));
        $dpCnt = array_fill(0, $n, array_fill(0, $n, 0));

        $dpSum[$n - 1][$n - 1] = 0;
        $dpCnt[$n - 1][$n - 1] = 1;

        for ($r = $n - 1; $r >= 0; $r--) {
            for ($c = $n - 1; $c >= 0; $c--) {
                if (($r == $n - 1 && $c == $n - 1) || $board[$r][$c] == 'X') continue;

                $maxS = -1;
                $count = 0;

                if ($r + 1 < $n && $dpSum[$r + 1][$c] != -1) {
                    $s = $dpSum[$r + 1][$c];
                    if ($s > $maxS) {
                        $maxS = $s;
                        $count = $dpCnt[$r + 1][$c];
                    } else if ($s == $maxS) {
                        $count = ($count + $dpCnt[$r + 1][$c]) % $mod;
                    }
                }
                if ($c + 1 < $n && $dpSum[$r][$c + 1] != -1) {
                    $s = $dpSum[$r][$c + 1];
                    if ($s > $maxS) {
                        $maxS = $s;
                        $count = $dpCnt[$r][$c + 1];
                    } else if ($s == $maxS) {
                        $count = ($count + $dpCnt[$r][$c + 1]) % $mod;
                    }
                }
                if ($r + 1 < $n && $c + 1 < $n && $dpSum[$r + 1][$c + 1] != -1) {
                    $s = $dpSum[$r + 1][$c + 1];
                    if ($s > $maxS) {
                        $maxS = $s;
                        $count = $dpCnt[$r + 1][$c + 1];
                    } else if ($s == $maxS) {
                        $count = ($count + $dpCnt[$r + 1][$c + 1]) % $mod;
                    }
                }

                if ($maxS != -1) {
                    $char = $board[$r][$c];
                    $val = ($char == 'E') ? 0 : (ord($char) - 48);
                    $dpSum[$r][$c] = $maxS + $val;
                    $dpCnt[$r][$c] = $count;
                }
            }
        }

        if ($dpSum[0][0] == -1) return [0, 0];
        return [$dpSum[0][0], $dpCnt[0][0]];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func pathsWithMaxScore(_ board: [String]) -> [Int] {
        let n = board.count
        let mod = 1_000_000_007
        let grid = board.map { Array($0) }
        var dpSum = Array(repeating: Array(repeating: -1, count: n), count: n)
        var dpCnt = Array(repeating: Array(repeating: 0, count: n), count: n)

        dpSum[n - 1][n - 1] = 0
        dpCnt[n - 1][n - 1] = 1

        for r in stride(from: n - 1, through: 0, by: -1) {
            for c in stride(from: n - 1, through: 0, by: -1) {
                if (r == n - 1 && c == n - 1) || grid[r][c] == "X" { continue }

                var maxS = -1
                var count = 0

                if r + 1 < n && dpSum[r + 1][c] != -1 {
                    let s = dpSum[r + 1][c]
                    if s > maxS {
                        maxS = s
                        count = dpCnt[r + 1][c]
                    } else if s == maxS {
                        count = (count + dpCnt[r + 1][c]) % mod
                    }
                }
                if c + 1 < n && dpSum[r][c + 1] != -1 {
                    let s = dpSum[r][c + 1]
                    if s > maxS {
                        maxS = s
                        count = dpCnt[r][c + 1]
                    } else if s == maxS {
                        count = (count + dpCnt[r][c + 1]) % mod
                    }
                }
                if r + 1 < n && c + 1 < n && dpSum[r + 1][c + 1] != -1 {
                    let s = dpSum[r + 1][c + 1]
                    if s > maxS {
                        maxS = s
                        count = dpCnt[r + 1][c + 1]
                    } else if s == maxS {
                        count = (count + dpCnt[r + 1][c + 1]) % mod
                    }
                }

                if maxS != -1 {
                    let char = grid[r][c]
                    let val = char == "E" ? 0 : Int(char.asciiValue! - 48)
                    dpSum[r][c] = maxS + val
                    dpCnt[r][c] = count
                }
            }
        }

        if dpSum[0][0] == -1 { return [0, 0] }
        return [dpSum[0][0], dpCnt[0][0]]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun pathsWithMaxScore(board: List<String>): IntArray {
        val n = board.size
        val mod = 1_000_000_007
        val dpSum = Array(n) { IntArray(n) { -1 } }
        val dpCnt = Array(n) { IntArray(n) { 0 } }

        dpSum[n - 1][n - 1] = 0
        dpCnt[n - 1][n - 1] = 1

        for (r in n - 1 downTo 0) {
            for (c in n - 1 downTo 0) {
                if ((r == n - 1 && c == n - 1) || board[r][c] == 'X') continue

                var maxS = -1
                var count = 0

                if (r + 1 < n && dpSum[r + 1][c] != -1) {
                    val s = dpSum[r + 1][c]
                    if (s > maxS) {
                        maxS = s
                        count = dpCnt[r + 1][c]
                    } else if (s == maxS) {
                        count = (count + dpCnt[r + 1][c]) % mod
                    }
                }
                if (c + 1 < n && dpSum[r][c + 1] != -1) {
                    val s = dpSum[r][c + 1]
                    if (s > maxS) {
                        maxS = s
                        count = dpCnt[r][c + 1]
                    } else if (s == maxS) {
                        count = (count + dpCnt[r][c + 1]) % mod
                    }
                }
                if (r + 1 < n && c + 1 < n && dpSum[r + 1][c + 1] != -1) {
                    val s = dpSum[r + 1][c + 1]
                    if (s > maxS) {
                        maxS = s
                        count = dpCnt[r + 1][c + 1]
                    } else if (s == maxS) {
                        count = (count + dpCnt[r + 1][c + 1]) % mod
                    }
                }

                if (maxS != -1) {
                    val v = if (board[r][c] == 'E') 0 else (board[r][c] - '0')
                    dpSum[r][c] = maxS + v
                    dpCnt[r][c] = count
                }
            }
        }

        if (dpSum[0][0] == -1) return intArrayOf(0, 0)
        return intArrayOf(dpSum[0][0], dpCnt[0][0])
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<int> pathsWithMaxScore(List<String> board) {
    int n = board.length;
    int mod = 1000000007;
    List<List<int>> dpScore = List.generate(n, (_) => List.filled(n, 0));
    List<List<int>> dpCount = List.generate(n, (_) => List.filled(n, 0));
    dpCount[n - 1][n - 1] = 1;
    for (int i = n - 1; i >= 0; i--) {
      for (int j = n - 1; j >= 0; j--) {
        if ((i == n - 1 && j == n - 1) || board[i][j] == 'X') continue;
        int maxS = -1;
        int paths = 0;
        if (i + 1 < n && dpCount[i + 1][j] > 0) {
          if (dpScore[i + 1][j] > maxS) {
            maxS = dpScore[i + 1][j];
            paths = dpCount[i + 1][j];
          } else if (dpScore[i + 1][j] == maxS) {
            paths = (paths + dpCount[i + 1][j]) % mod;
          }
        }
        if (j + 1 < n && dpCount[i][j + 1] > 0) {
          if (dpScore[i][j + 1] > maxS) {
            maxS = dpScore[i][j + 1];
            paths = dpCount[i][j + 1];
          } else if (dpScore[i][j + 1] == maxS) {
            paths = (paths + dpCount[i][j + 1]) % mod;
          }
        }
        if (i + 1 < n && j + 1 < n && dpCount[i + 1][j + 1] > 0) {
          if (dpScore[i + 1][j + 1] > maxS) {
            maxS = dpScore[i + 1][j + 1];
            paths = dpCount[i + 1][j + 1];
          } else if (dpScore[i + 1][j + 1] == maxS) {
            paths = (paths + dpCount[i + 1][j + 1]) % mod;
          }
        }
        if (maxS != -1) {
          int val = board[i][j] == 'E' ? 0 : int.parse(board[i][j]);
          dpScore[i][j] = maxS + val;
          dpCount[i][j] = paths;
        }
      }
    }
    if (dpCount[0][0] == 0) return [0, 0];
    return [dpScore[0][0], dpCount[0][0]];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func pathsWithMaxScore(board []string) []int {
	n := len(board)
	mod := 1000000007
	dpScore := make([][]int, n)
	dpCount := make([][]int, n)
	for i := range dpScore {
		dpScore[i] = make([]int, n)
		dpCount[i] = make([]int, n)
	}
	dpCount[n-1][n-1] = 1
	for i := n - 1; i >= 0; i-- {
		for j := n - 1; j >= 0; j-- {
			if (i == n-1 && j == n-1) || board[i][j] == 'X' {
				continue
			}
			maxS := -1
			paths := 0
			if i+1 < n && dpCount[i+1][j] > 0 {
				if dpScore[i+1][j] > maxS {
					maxS = dpScore[i+1][j]
					paths = dpCount[i+1][j]
				} else if dpScore[i+1][j] == maxS {
					paths = (paths + dpCount[i+1][j]) % mod
				}
			}
			if j+1 < n && dpCount[i][j+1] > 0 {
				if dpScore[i][j+1] > maxS {
					maxS = dpScore[i][j+1]
					paths = dpCount[i][j+1]
				} else if dpScore[i][j+1] == maxS {
					paths = (paths + dpCount[i][j+1]) % mod
				}
			}
			if i+1 < n && j+1 < n && dpCount[i+1][j+1] > 0 {
				if dpScore[i+1][j+1] > maxS {
					maxS = dpScore[i+1][j+1]
					paths = dpCount[i+1][j+1]
				} else if dpScore[i+1][j+1] == maxS {
					paths = (paths + dpCount[i+1][j+1]) % mod
				}
			}
			if maxS != -1 {
				val := 0
				if board[i][j] != 'E' {
					val = int(board[i][j] - '0')
				}
				dpScore[i][j] = maxS + val
				dpCount[i][j] = paths
			}
		}
	}
	if dpCount[0][0] == 0 {
		return []int{0, 0}
	}
	return []int{dpScore[0][0], dpCount[0][0]}
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def paths_with_max_score(board)
  n = board.length
  mod = 1_000_000_007
  dp_score = Array.new(n) { Array.new(n, 0) }
  dp_count = Array.new(n) { Array.new(n, 0) }
  dp_count[n-1][n-1] = 1
  (n-1).step(0, -1) do |i|
    (n-1).step(0, -1) do |j|
      next if (i == n-1 && j == n-1) || board[i][j] == 'X'
      max_s = -1
      paths = 0
      [[i+1, j], [i, j+1], [i+1, j+1]].each do |ni, nj|
        if ni < n && nj < n && dp_count[ni][nj] > 0
          if dp_score[ni][nj] > max_s
            max_s = dp_score[ni][nj]
            paths = dp_count[ni][nj]
          elsif dp_score[ni][nj] == max_s
            paths = (paths + dp_count[ni][nj]) % mod
          end
        end
      end
      if max_s != -1
        val = board[i][j] == 'E' ? 0 : board[i][j].to_i
        dp_score[i][j] = max_s + val
        dp_count[i][j] = paths
      end
    end
  end
  dp_count[0][0] == 0 ? [0, 0] : [dp_score[0][0], dp_count[0][0]]
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def pathsWithMaxScore(board: List[String]): Array[Int] = {
        val n = board.length
        val mod = 1000000007
        val dpScore = Array.ofDim[Int](n, n)
        val dpCount = Array.ofDim[Int](n, n)
        dpCount(n - 1)(n - 1) = 1
        for (i <- n - 1 to 0 by -1) {
            for (j <- n - 1 to 0 by -1) {
                if (!((i == n - 1 && j == n - 1) || board(i)(j) == 'X')) {
                    var maxS = -1
                    var paths = 0
                    if (i + 1 < n && dpCount(i + 1)(j) > 0) {
                        if (dpScore(i + 1)(j) > maxS) {
                            maxS = dpScore(i + 1)(j)
                            paths = dpCount(i + 1)(j)
                        } else if (dpScore(i + 1)(j) == maxS) {
                            paths = (paths + dpCount(i + 1)(j)) % mod
                        }
                    }
                    if (j + 1 < n && dpCount(i)(j + 1) > 0) {
                        if (dpScore(i)(j + 1) > maxS) {
                            maxS = dpScore(i)(j + 1)
                            paths = dpCount(i)(j + 1)
                        } else if (dpScore(i)(j + 1) == maxS) {
                            paths = (paths + dpCount(i)(j + 1)) % mod
                        }
                    }
                    if (i + 1 < n && j + 1 < n && dpCount(i + 1)(j + 1) > 0) {
                        if (dpScore(i + 1)(j + 1) > maxS) {
                            maxS = dpScore(i + 1)(j + 1)
                            paths = dpCount(i + 1)(j + 1)
                        } else if (dpScore(i + 1)(j + 1) == maxS) {
                            paths = (paths + dpCount(i + 1)(j + 1)) % mod
                        }
                    }
                    if (maxS != -1) {
                        val v = if (board(i)(j) == 'E') 0 else board(i)(j).asDigit
                        dpScore(i)(j) = maxS + v
                        dpCount(i)(j) = paths
                    }
                }
            }
        }
        if (dpCount(0)(0) == 0) Array(0, 0)
        else Array(dpScore(0)(0), dpCount(0)(0))
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn paths_with_max_score(board: Vec<String>) -> Vec<i32> {
        let n = board.len();
        let b: Vec<Vec<u8>> = board.into_iter().map(|s| s.into_bytes()).collect();
        let mut dp_sum = vec![vec![0; n]; n];
        let mut dp_cnt = vec![vec![0; n]; n];
        let mod_val = 1_000_000_007;

        dp_cnt[n - 1][n - 1] = 1;

        for i in (0..n).rev() {
            for j in (0..n).rev() {
                if (i == n - 1 && j == n - 1) || b[i][j] == b'X' {
                    continue;
                }

                let mut max_s = -1;
                let mut count = 0;

                let neighbors = [(i + 1, j), (i, j + 1), (i + 1, j + 1)];
                for (ni, nj) in neighbors {
                    if ni < n && nj < n && dp_cnt[ni][nj] > 0 {
                        if dp_sum[ni][nj] > max_s {
                            max_s = dp_sum[ni][nj];
                            count = dp_cnt[ni][nj];
                        } else if dp_sum[ni][nj] == max_s {
                            count = (count + dp_cnt[ni][nj]) % mod_val;
                        }
                    }
                }

                if max_s != -1 {
                    let cur_val = if b[i][j] == b'E' { 0 } else { (b[i][j] - b'0') as i32 };
                    dp_sum[i][j] = max_s + cur_val;
                    dp_cnt[i][j] = count;
                }
            }
        }

        vec![dp_sum[0][0], dp_cnt[0][0]]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (paths-with-max-score board)
  (-> (listof string?) (listof integer?))
  (let* ([n (length board)]
         [grid (list->vector (map (lambda (s) (list->vector (string->list s))) board))]
         [dp-sum (make-vector (* n n) 0)]
         [dp-cnt (make-vector (* n n) 0)]
         [mod 1000000007])
    (define (get-idx r c) (+ (* r n) c))
    (vector-set! dp-cnt (get-idx (- n 1) (- n 1)) 1)
    (for ([r (in-range (- n 1) -1 -1)])
      (for ([c (in-range (- n 1) -1 -1)])
        (let ([char (vector-ref (vector-ref grid r) c)])
          (unless (or (and (= r (- n 1)) (= c (- n 1))) (char=? char #\X))
            (let ([max-s -1]
                  [count 0])
              (for ([move (list (list (+ r 1) c) (list r (+ c 1)) (list (+ r 1) (+ c 1)))])
                (let ([nr (car move)] [nc (cadr move)])
                  (when (and (< nr n) (< nc n) (> (vector-ref dp-cnt (get-idx nr nc)) 0))
                    (let ([s (vector-ref dp-sum (get-idx nr nc))]
                          [cnt (vector-ref dp-cnt (get-idx nr nc))])
                      (cond
                        [(> s max-s) (set! max-s s) (set! count cnt)]
                        [(= s max-s) (set! count (modulo (+ count cnt) mod))])))))
              (when (not (= max-s -1))
                (let ([val (if (char=? char #\E) 0 (- (char->integer char) 48))])
                  (vector-set! dp-sum (get-idx r c) (+ max-s val))
                  (vector-set! dp-cnt (get-idx r c) count))))))))
    (list (vector-ref dp-sum 0) (vector-ref dp-cnt 0))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec paths_with_max_score(Board :: [unicode:unicode_binary()]) -> [integer()].
paths_with_max_score(Board) ->
    N = length(Board),
    Grid = list_to_tuple([list_to_tuple(binary_to_list(Row)) || Row <- Board]),
    Mod = 1000000007,
    DP = solve(N, Grid, Mod),
    {S, C} = maps:get({0, 0}, DP, {0, 0}),
    [S, C].

solve(N, Grid, Mod) ->
    lists:foldl(fun(R, AccR) ->
        lists:foldl(fun(C, AccC) ->
            Row = element(R + 1, Grid),
            Char = element(C + 1, Row),
            if
                R == N - 1, C == N - 1 ->
                    maps:put({R, C}, {0, 1}, AccC);
                Char == $X ->
                    maps:put({R, C}, {0, 0}, AccC);
                true ->
                    Neighbors = [{R + 1, C}, {R, C + 1}, {R + 1, C + 1}],
                    {MaxS, Count} = lists:foldl(fun({NR, NC}, {MS, MC}) ->
                        case maps:get({NR, NC}, AccC, {0, 0}) of
                            {S, CV} when CV > 0 ->
                                if
                                    S > MS -> {S, CV};
                                    S == MS -> {MS, (MC + CV) rem Mod};
                                    true -> {MS, MC}
                                end;
                            _ -> {MS, MC}
                        end
                    end, {-1, 0}, Neighbors),
                    if
                        MaxS == -1 ->
                            maps:put({R, C}, {0, 0}, AccC);
                        true ->
                            Val = if Char == $E -> 0; true -> Char - $0 end,
                            maps:put({R, C}, {MaxS + Val, Count}, AccC)
                    end
            end
        end, AccR, lists:seq(N - 1, 0, -1))
    end, #{}, lists:seq(N - 1, 0, -1)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec paths_with_max_score(board :: [String.t]) :: [integer]
  def paths_with_max_score(board) do
    n = length(board)
    grid = board
           |> Enum.map(fn row -> String.to_charlist(row) |> List.to_tuple() end)
           |> List.to_tuple()
    mod = 1_000_000_007

    dp = Enum.reduce((n - 1)..0, %{}, fn r, acc_r ->
      Enum.reduce((n - 1)..0, acc_r, fn c, acc_c ->
        char = elem(elem(grid, r), c)
        cond do
          r == n - 1 and c == n - 1 ->
            Map.put(acc_c, {r, c}, {0, 1})
          char == ?X ->
            Map.put(acc_c, {r, c}, {0, 0})
          true ->
            moves = [{r + 1, c}, {r, c + 1}, {r + 1, c + 1}]
            {max_s, count} = Enum.reduce(moves, {-1, 0}, fn {nr, nc}, {ms, mc} ->
              case Map.get(acc_c, {nr, nc}) do
                {s, c_val} when c_val > 0 ->
                  cond do
                    s > ms -> {s, c_val}
                    s == ms -> {ms, rem(mc + c_val, mod)}
                    true -> {ms, mc}
                  end
                _ -> {ms, mc}
              end
            end)

            if max_s == -1 do
              Map.put(acc_c, {r, c}, {0, 0})
            else
              val = if char == ?E, do: 0, else: char - ?0
              Map.put(acc_c, {r, c}, {max_s + val, count})
            end
        end
      end)
    end)

    {s, c} = Map.get(dp, {0, 0}, {0, 0})
    [s, c]
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N^2) where $N$ is the side length of the board. The algorithm iterates through each of the $N \times N$ cells exactly once, and for each cell, it performs a constant number of operations to check three adjacent neighbors.
- **Space Complexity:** O(N^2) as the algorithm uses two $N \times N$ grids to store the maximum scores and the count of paths for every cell on the board. This can be optimized to $O(N)$ space using row-based DP, but $O(N^2)$ is well within limits for $N=100$.
