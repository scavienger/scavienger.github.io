---
layout: post
title: "Find All Possible Stable Binary Arrays I"
date: 2026-03-09 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Dynamic Programming", "Prefix Sum"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int numberOfStableArrays(int zero, int one,\
        \ int limit) {\n        long long MOD = 1e9 + 7;\n        vector<vector<vector<long\
        \ long>>> dp(zero + 1, vector<vector<long long>>(one + 1, vector<long long>(2,\
        \ 0)));\n\n        for (int i = 1; i <= min(zero, limit); ++i) dp[i][0][0] =\
        \ 1;\n        for (int j = 1; j <= min(one, limit); ++j) dp[0][j][1] = 1;\n\n\
        \        for (int i = 1; i <= zero; ++i) {\n            for (int j = 1; j <=\
        \ one; ++j) {\n                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1])\
        \ % MOD;\n                if (i > limit) {\n                    dp[i][j][0]\
        \ = (dp[i][j][0] - dp[i - limit - 1][j][1] + MOD) % MOD;\n                }\n\
        \n                dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % MOD;\n\
        \                if (j > limit) {\n                    dp[i][j][1] = (dp[i][j][1]\
        \ - dp[i][j - limit - 1][0] + MOD) % MOD;\n                }\n            }\n\
        \        }\n\n        return (int)((dp[zero][one][0] + dp[zero][one][1]) % MOD);\n\
        \    }\n};"
      java: "class Solution {\n    public int numberOfStableArrays(int zero, int one,\
        \ int limit) {\n        long MOD = 1_000_000_007;\n        long[][][] dp = new\
        \ long[zero + 1][one + 1][2];\n\n        for (int i = 1; i <= Math.min(zero,\
        \ limit); i++) dp[i][0][0] = 1;\n        for (int j = 1; j <= Math.min(one,\
        \ limit); j++) dp[0][j][1] = 1;\n\n        for (int i = 1; i <= zero; i++) {\n\
        \            for (int j = 1; j <= one; j++) {\n                dp[i][j][0] =\
        \ (dp[i - 1][j][0] + dp[i - 1][j][1]) % MOD;\n                if (i > limit)\
        \ {\n                    dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1]\
        \ + MOD) % MOD;\n                }\n\n                dp[i][j][1] = (dp[i][j\
        \ - 1][0] + dp[i][j - 1][1]) % MOD;\n                if (j > limit) {\n    \
        \                dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0] + MOD)\
        \ % MOD;\n                }\n            }\n        }\n\n        return (int)\
        \ ((dp[zero][one][0] + dp[zero][one][1]) % MOD);\n    }\n}"
      python: "class Solution(object):\n    def numberOfStableArrays(self, zero, one,\
        \ limit):\n        \"\"\"\n        :type zero: int\n        :type one: int\n\
        \        :type limit: int\n        :rtype: int\n        \"\"\"\n        MOD\
        \ = 10**9 + 7\n        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero\
        \ + 1)]\n\n        for i in range(1, min(zero, limit) + 1):\n            dp[i][0][0]\
        \ = 1\n        for j in range(1, min(one, limit) + 1):\n            dp[0][j][1]\
        \ = 1\n\n        for i in range(1, zero + 1):\n            for j in range(1,\
        \ one + 1):\n                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1])\
        \ % MOD\n                if i > limit:\n                    dp[i][j][0] = (dp[i][j][0]\
        \ - dp[i - limit - 1][j][1] + MOD) % MOD\n\n                dp[i][j][1] = (dp[i][j\
        \ - 1][0] + dp[i][j - 1][1]) % MOD\n                if j > limit:\n        \
        \            dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0] + MOD) % MOD\n\
        \n        return (dp[zero][one][0] + dp[zero][one][1]) % MOD"
      python3: "class Solution:\n    def numberOfStableArrays(self, zero: int, one:\
        \ int, limit: int) -> int:\n        MOD = 10**9 + 7\n        dp = [[[0, 0] for\
        \ _ in range(one + 1)] for _ in range(zero + 1)]\n\n        for i in range(1,\
        \ min(zero, limit) + 1):\n            dp[i][0][0] = 1\n        for j in range(1,\
        \ min(one, limit) + 1):\n            dp[0][j][1] = 1\n\n        for i in range(1,\
        \ zero + 1):\n            for j in range(1, one + 1):\n                dp[i][j][0]\
        \ = (dp[i - 1][j][0] + dp[i - 1][j][1]) % MOD\n                if i > limit:\n\
        \                    dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1] +\
        \ MOD) % MOD\n\n                dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1])\
        \ % MOD\n                if j > limit:\n                    dp[i][j][1] = (dp[i][j][1]\
        \ - dp[i][j - limit - 1][0] + MOD) % MOD\n\n        return (dp[zero][one][0]\
        \ + dp[zero][one][1]) % MOD"
      c: "int numberOfStableArrays(int zero, int one, int limit) {\n    long long MOD\
        \ = 1e9 + 7;\n    static long long dp[201][201][2];\n\n    for (int i = 0; i\
        \ <= zero; i++) {\n        for (int j = 0; j <= one; j++) {\n            dp[i][j][0]\
        \ = dp[i][j][1] = 0;\n        }\n    }\n\n    for (int i = 1; i <= (zero < limit\
        \ ? zero : limit); i++) dp[i][0][0] = 1;\n    for (int j = 1; j <= (one < limit\
        \ ? one : limit); j++) dp[0][j][1] = 1;\n\n    for (int i = 1; i <= zero; i++)\
        \ {\n        for (int j = 1; j <= one; j++) {\n            dp[i][j][0] = (dp[i\
        \ - 1][j][0] + dp[i - 1][j][1]) % MOD;\n            if (i > limit)\n       \
        \         dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1] + MOD) % MOD;\n\
        \n            dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % MOD;\n   \
        \         if (j > limit)\n                dp[i][j][1] = (dp[i][j][1] - dp[i][j\
        \ - limit - 1][0] + MOD) % MOD;\n        }\n    }\n\n    return (int)((dp[zero][one][0]\
        \ + dp[zero][one][1]) % MOD);\n}"
      csharp: "public class Solution {\n    public int NumberOfStableArrays(int zero,\
        \ int one, int limit) {\n        long MOD = 1000000007;\n        long[,,] dp\
        \ = new long[zero + 1, one + 1, 2];\n\n        for (int i = 1; i <= Math.Min(zero,\
        \ limit); i++) dp[i, 0, 0] = 1;\n        for (int j = 1; j <= Math.Min(one,\
        \ limit); j++) dp[0, j, 1] = 1;\n\n        for (int i = 1; i <= zero; i++) {\n\
        \            for (int j = 1; j <= one; j++) {\n                dp[i, j, 0] =\
        \ (dp[i - 1, j, 0] + dp[i - 1, j, 1]) % MOD;\n                if (i > limit)\
        \ {\n                    dp[i, j, 0] = (dp[i, j, 0] - dp[i - limit - 1, j, 1]\
        \ + MOD) % MOD;\n                }\n\n                dp[i, j, 1] = (dp[i, j\
        \ - 1, 0] + dp[i, j - 1, 1]) % MOD;\n                if (j > limit) {\n    \
        \                dp[i, j, 1] = (dp[i, j, 1] - dp[i, j - limit - 1, 0] + MOD)\
        \ % MOD;\n                }\n            }\n        }\n\n        return (int)((dp[zero,\
        \ one, 0] + dp[zero, one, 1]) % MOD);\n    }\n}"
      javascript: "/**\n * @param {number} zero\n * @param {number} one\n * @param {number}\
        \ limit\n * @return {number}\n */\nvar numberOfStableArrays = function(zero,\
        \ one, limit) {\n    const MOD = 1000000007;\n    const dp = Array.from({ length:\
        \ zero + 1 }, () =>\n        Array.from({ length: one + 1 }, () => new BigInt64Array(2).fill(0n))\n\
        \    );\n\n    for (let i = 1; i <= Math.min(zero, limit); i++) dp[i][0][0]\
        \ = 1n;\n    for (let j = 1; j <= Math.min(one, limit); j++) dp[0][j][1] = 1n;\n\
        \n    for (let i = 1; i <= zero; i++) {\n        for (let j = 1; j <= one; j++)\
        \ {\n            dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % BigInt(MOD);\n\
        \            if (i > limit) {\n                dp[i][j][0] = (dp[i][j][0] -\
        \ dp[i - limit - 1][j][1] + BigInt(MOD)) % BigInt(MOD);\n            }\n\n \
        \           dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % BigInt(MOD);\n\
        \            if (j > limit) {\n                dp[i][j][1] = (dp[i][j][1] -\
        \ dp[i][j - limit - 1][0] + BigInt(MOD)) % BigInt(MOD);\n            }\n   \
        \     }\n    }\n\n    return Number((dp[zero][one][0] + dp[zero][one][1]) %\
        \ BigInt(MOD));\n};"
      typescript: "function numberOfStableArrays(zero: number, one: number, limit: number):\
        \ number {\n    const MOD = 1000000007;\n    const dp = Array.from({ length:\
        \ zero + 1 }, () => Array.from({ length: one + 1 }, () => [0, 0]));\n    for\
        \ (let i = 1; i <= Math.min(zero, limit); i++) dp[i][0][0] = 1;\n    for (let\
        \ j = 1; j <= Math.min(one, limit); j++) dp[0][j][1] = 1;\n    for (let i =\
        \ 1; i <= zero; i++) {\n        for (let j = 1; j <= one; j++) {\n         \
        \   dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % MOD;\n            if\
        \ (i > limit) {\n                dp[i][j][0] = (dp[i][j][0] - dp[i - limit -\
        \ 1][j][1] + MOD) % MOD;\n            }\n            dp[i][j][1] = (dp[i][j\
        \ - 1][0] + dp[i][j - 1][1]) % MOD;\n            if (j > limit) {\n        \
        \        dp[i][j][1] = (dp[i][j][1] - dp[i - limit - 1][0] || 0);\n        \
        \        dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % MOD;\n        \
        \        if (j > limit) {\n                    dp[i][j][1] = (dp[i][j][1] -\
        \ dp[i][j - limit - 1][0] + MOD) % MOD;\n                }\n            }\n\
        \        }\n    }\n    return (dp[zero][one][0] + dp[zero][one][1]) % MOD;\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param Integer $zero\n     * @param\
        \ Integer $one\n     * @param Integer $limit\n     * @return Integer\n     */\n\
        \    function numberOfStableArrays($zero, $one, $limit) {\n        $MOD = 1000000007;\n\
        \        $dp = array_fill(0, $zero + 1, array_fill(0, $one + 1, [0, 0]));\n\
        \        for ($i = 1; $i <= min($zero, $limit); $i++) {\n            $dp[$i][0][0]\
        \ = 1;\n        }\n        for ($j = 1; $j <= min($one, $limit); $j++) {\n \
        \           $dp[0][$j][1] = 1;\n        }\n        for ($i = 1; $i <= $zero;\
        \ $i++) {\n            for ($j = 1; $j <= $one; $j++) {\n                $dp[$i][$j][0]\
        \ = ($dp[$i - 1][$j][0] + $dp[$i - 1][$j][1]) % $MOD;\n                if ($i\
        \ > $limit) {\n                    $dp[$i][$j][0] = ($dp[$i][$j][0] - $dp[$i\
        \ - $limit - 1][$j][1] + $MOD) % $MOD;\n                }\n                $dp[$i][$j][1]\
        \ = ($dp[$i][$j - 1][0] + $dp[$i][$j - 1][1]) % $MOD;\n                if ($j\
        \ > $limit) {\n                    $dp[$i][$j][1] = ($dp[$i][$j][1] - $dp[$i][$j\
        \ - $limit - 1][0] + $MOD) % $MOD;\n                }\n            }\n     \
        \   }\n        return ($dp[$zero][$one][0] + $dp[$zero][$one][1]) % $MOD;\n\
        \    }\n}"
      swift: "class Solution {\n    func numberOfStableArrays(_ zero: Int, _ one: Int,\
        \ _ limit: Int) -> Int {\n        let MOD = 1_000_000_007\n        var dp =\
        \ Array(repeating: Array(repeating: [0, 0], count: one + 1), count: zero + 1)\n\
        \        for i in 1...min(zero, limit) {\n            dp[i][0][0] = 1\n    \
        \    }\n        for j in 1...min(one, limit) {\n            dp[0][j][1] = 1\n\
        \        }\n        if zero > 0 && one > 0 {\n            for i in 1...zero\
        \ {\n                for j in 1...one {\n                    dp[i][j][0] = (dp[i\
        \ - 1][j][0] + dp[i - 1][j][1]) % MOD\n                    if i > limit {\n\
        \                        dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1]\
        \ + MOD) % MOD\n                    }\n                    dp[i][j][1] = (dp[i][j\
        \ - 1][0] + dp[i][j - 1][1]) % MOD\n                    if j > limit {\n   \
        \                     dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0] +\
        \ MOD) % MOD\n                    }\n                }\n            }\n    \
        \    }\n        return (dp[zero][one][0] + dp[zero][one][1]) % MOD\n    }\n}"
      kotlin: "class Solution {\n    fun numberOfStableArrays(zero: Int, one: Int, limit:\
        \ Int): Int {\n        val MOD = 1000000007\n        val dp = Array(zero + 1)\
        \ { Array(one + 1) { IntArray(2) } }\n        for (i in 1..minOf(zero, limit))\
        \ {\n            dp[i][0][0] = 1\n        }\n        for (j in 1..minOf(one,\
        \ limit)) {\n            dp[0][j][1] = 1\n        }\n        for (i in 1..zero)\
        \ {\n            for (j in 1..one) {\n                dp[i][j][0] = (dp[i -\
        \ 1][j][0] + dp[i - 1][j][1]) % MOD\n                if (i > limit) {\n    \
        \                dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1] + MOD)\
        \ % MOD\n                }\n                dp[i][j][1] = (dp[i][j - 1][0] +\
        \ dp[i][j - 1][1]) % MOD\n                if (j > limit) {\n               \
        \     dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0] + MOD) % MOD\n  \
        \              }\n            }\n        }\n        return (dp[zero][one][0]\
        \ + dp[zero][one][1]) % MOD\n    }\n}"
      dart: "class Solution {\n  int numberOfStableArrays(int zero, int one, int limit)\
        \ {\n    final int mod = 1000000007;\n    var dp = List.generate(zero + 1, (_)\
        \ => List.generate(one + 1, (_) => List.filled(2, 0)));\n    for (int i = 1;\
        \ i <= zero && i <= limit; i++) {\n      dp[i][0][0] = 1;\n    }\n    for (int\
        \ j = 1; j <= one && j <= limit; j++) {\n      dp[0][j][1] = 1;\n    }\n   \
        \ for (int i = 1; i <= zero; i++) {\n      for (int j = 1; j <= one; j++) {\n\
        \        dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % mod;\n        if\
        \ (i > limit) {\n          dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1]\
        \ + mod) % mod;\n        }\n        dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j\
        \ - 1][1]) % mod;\n        if (j > limit) {\n          dp[i][j][1] = (dp[i][j][1]\
        \ - dp[i][j - limit - 1][0] + mod) % mod;\n        }\n      }\n    }\n    return\
        \ (dp[zero][one][0] + dp[zero][one][1]) % mod;\n  }\n}"
      go: "func numberOfStableArrays(zero int, one int, limit int) int {\n    const\
        \ MOD = 1000000007\n    dp := make([][][2]int, zero+1)\n    for i := range dp\
        \ {\n        dp[i] = make([][2]int, one+1)\n    }\n    for i := 1; i <= zero\
        \ && i <= limit; i++ {\n        dp[i][0][0] = 1\n    }\n    for j := 1; j <=\
        \ one && j <= limit; j++ {\n        dp[0][j][1] = 1\n    }\n    for i := 1;\
        \ i <= zero; i++ {\n        for j := 1; j <= one; j++ {\n            dp[i][j][0]\
        \ = (dp[i-1][j][0] + dp[i-1][j][1]) % MOD\n            if i > limit {\n    \
        \            dp[i][j][0] = (dp[i][j][0] - dp[i-limit-1][j][1] + MOD) % MOD\n\
        \            }\n            dp[i][j][1] = (dp[i][j-1][0] + dp[i][j-1][1]) %\
        \ MOD\n            if j > limit {\n                dp[i][j][1] = (dp[i][j][1]\
        \ - dp[i][j-limit-1][0] + MOD) % MOD\n            }\n        }\n    }\n    return\
        \ (dp[zero][one][0] + dp[zero][one][1]) % MOD\n}"
      ruby: "def number_of_stable_arrays(zero, one, limit)\n  mod = 1_000_000_007\n\
        \  dp = Array.new(zero + 1) { Array.new(one + 1) { [0, 0] } }\n  (1..[zero,\
        \ limit].min).each { |i| dp[i][0][0] = 1 }\n  (1..[one, limit].min).each { |j|\
        \ dp[0][j][1] = 1 }\n  (1..zero).each do |i|\n    (1..one).each do |j|\n   \
        \   dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % mod\n      if i > limit\n\
        \        dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1] + mod) % mod\n\
        \      end\n      dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % mod\n\
        \      if j > limit\n        dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit -\
        \ 1][0] + mod) % mod\n      end\n    end\n  end\n  (dp[zero][one][0] + dp[zero][one][1])\
        \ % mod\nend"
      scala: "object Solution {\n  def numberOfStableArrays(zero: Int, one: Int, limit:\
        \ Int): Int = {\n    val MOD = 1000000007\n    val dp = Array.ofDim[Int](zero\
        \ + 1, one + 1, 2)\n    for (i <- 1 to Math.min(zero, limit)) dp(i)(0)(0) =\
        \ 1\n    for (j <- 1 to Math.min(one, limit)) dp(0)(j)(1) = 1\n    for (i <-\
        \ 1 to zero) {\n      for (j <- 1 to one) {\n        dp(i)(j)(0) = ((dp(i -\
        \ 1)(j)(0).toLong + dp(i - 1)(j)(1)) % MOD).toInt\n        if (i > limit) {\n\
        \          dp(i)(j)(0) = ((dp(i)(j)(0).toLong - dp(i - limit - 1)(j)(1) + MOD)\
        \ % MOD).toInt\n        }\n        dp(i)(j)(1) = ((dp(i)(j - 1)(0).toLong +\
        \ dp(i)(j - 1)(1)) % MOD).toInt\n        if (j > limit) {\n          dp(i)(j)(1)\
        \ = ((dp(i)(j)(1).toLong - dp(i)(j - limit - 1)(0) + MOD) % MOD).toInt\n   \
        \     }\n      }\n    }\n    ((dp(zero)(one)(0).toLong + dp(zero)(one)(1)) %\
        \ MOD).toInt\n  }\n}"
      rust: "impl Solution {\n    pub fn number_of_stable_arrays(zero: i32, one: i32,\
        \ limit: i32) -> i32 {\n        let (z, o, l) = (zero as usize, one as usize,\
        \ limit as usize);\n        let mut dp = vec![vec![[0i32; 2]; o + 1]; z + 1];\n\
        \        let mod_val = 1_000_000_007;\n\n        for i in 1..=std::cmp::min(z,\
        \ l) {\n            dp[i][0][0] = 1;\n        }\n        for j in 1..=std::cmp::min(o,\
        \ l) {\n            dp[0][j][1] = 1;\n        }\n\n        for i in 1..=z {\n\
        \            for j in 1..=o {\n                dp[i][j][0] = (dp[i - 1][j][0]\
        \ + dp[i - 1][j][1]) % mod_val;\n                if i > l {\n              \
        \      dp[i][j][0] = (dp[i][j][0] - dp[i - l - 1][j][1] + mod_val) % mod_val;\n\
        \                }\n                dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j\
        \ - 1][1]) % mod_val;\n                if j > l {\n                    dp[i][j][1]\
        \ = (dp[i][j][1] - dp[i][j - l - 1][0] + mod_val) % mod_val;\n             \
        \   }\n            }\n        }\n        (dp[z][o][0] + dp[z][o][1]) % mod_val\n\
        \    }\n}"
      racket: "(define/contract (number-of-stable-arrays zero one limit)\n  (-> exact-integer?\
        \ exact-integer? exact-integer? exact-integer?)\n  (let* ([dp (make-vector (*\
        \ (+ zero 1) (+ one 1) 2) 0)]\n         [get-dp (lambda (i j k) (vector-ref\
        \ dp (+ (* i (+ one 1) 2) (* j 2) k)))]\n         [set-dp! (lambda (i j k val)\
        \ (vector-set! dp (+ (* i (+ one 1) 2) (* j 2) k) val))])\n    (for ([i (in-range\
        \ 1 (+ (min zero limit) 1))]) (set-dp! i 0 0 1))\n    (for ([j (in-range 1 (+\
        \ (min one limit) 1))]) (set-dp! 0 j 1 1))\n    (for* ([i (in-range 1 (+ zero\
        \ 1))]\n           [j (in-range 1 (+ one 1))])\n      (let* ([ways0 (modulo\
        \ (+ (get-dp (- i 1) j 0) (get-dp (- i 1) j 1)) 1000000007)]\n             [ways0-final\
        \ (if (> i limit)\n                              (modulo (- ways0 (get-dp (-\
        \ i limit 1) j 1)) 1000000007)\n                              ways0)])\n   \
        \     (set-dp! i j 0 ways0-final))\n      (let* ([ways1 (modulo (+ (get-dp i\
        \ (- j 1) 0) (get-dp i (- j 1) 1)) 1000000007)]\n             [ways1-final (if\
        \ (> j limit)\n                              (modulo (- ways1 (get-dp i (- j\
        \ limit 1) 0)) 1000000007)\n                              ways1)])\n       \
        \ (set-dp! i j 1 ways1-final)))\n    (modulo (+ (get-dp zero one 0) (get-dp\
        \ zero one 1)) 1000000007)))"
      erlang: "number_of_stable_arrays(Zero, One, Limit) ->\n  MOD = 1000000007,\n \
        \ DP0 = lists:foldl(fun(I, Acc) -> Acc#{ {I, 0, 0} => 1 } end, #{}, lists:seq(1,\
        \ erlang:min(Zero, Limit))),\n  DP1 = lists:foldl(fun(J, Acc) -> Acc#{ {0, J,\
        \ 1} => 1 } end, DP0, lists:seq(1, erlang:min(One, Limit))),\n  FinalDP = lists:foldl(fun(I,\
        \ AccI) ->\n    lists:foldl(fun(J, AccJ) ->\n      Ways0 = (maps:get({I - 1,\
        \ J, 0}, AccJ, 0) + maps:get({I - 1, J, 1}, AccJ, 0)) rem MOD,\n      Ways0F\
        \ = case I > Limit of\n        true -> (Ways0 - maps:get({I - Limit - 1, J,\
        \ 1}, AccJ, 0) + MOD) rem MOD;\n        false -> Ways0\n      end,\n      Ways1\
        \ = (maps:get({I, J - 1, 0}, AccJ, 0) + maps:get({I, J - 1, 1}, AccJ, 0)) rem\
        \ MOD,\n      Ways1F = case J > Limit of\n        true -> (Ways1 - maps:get({I,\
        \ J - Limit - 1, 0}, AccJ, 0) + MOD) rem MOD;\n        false -> Ways1\n    \
        \  end,\n      AccJ#{ {I, J, 0} => Ways0F, {I, J, 1} => Ways1F }\n    end, AccI,\
        \ lists:seq(1, One))\n  end, DP1, lists:seq(1, Zero)),\n  (maps:get({Zero, One,\
        \ 0}, FinalDP, 0) + maps:get({Zero, One, 1}, FinalDP, 0)) rem MOD."
      elixir: "defmodule Solution do\n  @spec number_of_stable_arrays(zero :: integer,\
        \ one :: integer, limit :: integer) :: integer\n  def number_of_stable_arrays(zero,\
        \ one, limit) do\n    mod = 1_000_000_007\n    dp = %{}\n    dp = Enum.reduce(1..min(zero,\
        \ limit), dp, fn i, acc -> Map.put(acc, {i, 0, 0}, 1) end)\n    dp = Enum.reduce(1..min(one,\
        \ limit), dp, fn j, acc -> Map.put(acc, {0, j, 1}, 1) end)\n\n    final_dp =\
        \ Enum.reduce(1..zero, dp, fn i, acc_i ->\n      Enum.reduce(1..one, acc_i,\
        \ fn j, acc_j ->\n        ways0 = rem(Map.get(acc_j, {i - 1, j, 0}, 0) + Map.get(acc_j,\
        \ {i - 1, j, 1}, 0), mod)\n        ways0 = if i > limit do rem(ways0 - Map.get(acc_j,\
        \ {i - limit - 1, j, 1}, 0) + mod, mod) else ways0 end\n\n        ways1 = rem(Map.get(acc_j,\
        \ {i, j - 1, 0}, 0) + Map.get(acc_j, {i, j - 1, 1}, 0), mod)\n        ways1\
        \ = if j > limit do rem(ways1 - Map.get(acc_j, {i, j - limit - 1, 0}, 0) + mod,\
        \ mod) else ways1 end\n\n        acc_j |> Map.put({i, j, 0}, ways0) |> Map.put({i,\
        \ j, 1}, ways1)\n      end)\n    end)\n\n    rem(Map.get(final_dp, {zero, one,\
        \ 0}, 0) + Map.get(final_dp, {zero, one, 1}, 0), mod)\n  end\nend"
    approach: 'The problem can be solved using dynamic programming by defining $dp[i][j][k]$
      as the number of stable binary arrays containing exactly $i$ zeros and $j$ ones,
      ending with the digit $k$ (where $k=0$ or $k=1$). A stable array is one where
      no block of consecutive identical digits exceeds the given $limit$. The total
      number of stable arrays is the sum of arrays ending in zero and those ending in
      one: $dp[zero][one][0] + dp[zero][one][1]$.


      To compute $dp[i][j][0]$, we consider appending a zero to any stable array with
      $i-1$ zeros and $j$ ones. This transition is represented by $dp[i-1][j][0] + dp[i-1][j][1]$.
      However, we must subtract cases where this creates a sequence of $limit + 1$ consecutive
      zeros. These invalid sequences are formed by appending $limit+1$ zeros to a stable
      sequence that ended in 1 (or was empty) and had $i-(limit+1)$ zeros. Thus, we
      subtract $dp[i-limit-1][j][1]$ from the total. A symmetric recurrence applies
      to $dp[i][j][1]$ by swapping the roles of zeros and ones.'
    time_complexity: "O(zero * one). We iterate through a 2D grid of size $(zero+1)\
      \ \times (one+1)$, and for each cell, we perform a constant number of operations\
      \ to update the two states (ending in 0 or 1)."
    space_complexity: "O(zero * one). We maintain a 3D dynamic programming table of\
      \ size $(zero+1) \times (one+1) \times 2$ to store the number of stable arrays\
      \ for each state."
    elapsed_time: 261.1716482639313
    model: gemini-3-flash-preview
    generated_at: '2026-03-09 01:28:21 '
---

## Problem #3129: Find All Possible Stable Binary Arrays I

**Difficulty:** Medium

**Topics:** Dynamic Programming, Prefix Sum

## Problem Description

<p>You are given 3 positive integers <code>zero</code>, <code>one</code>, and <code>limit</code>.</p>

<p>A <span data-keyword="binary-array">binary array</span> <code>arr</code> is called <strong>stable</strong> if:</p>

<ul>
	<li>The number of occurrences of 0 in <code>arr</code> is <strong>exactly </strong><code>zero</code>.</li>
	<li>The number of occurrences of 1 in <code>arr</code> is <strong>exactly</strong> <code>one</code>.</li>
	<li>Each <span data-keyword="subarray-nonempty">subarray</span> of <code>arr</code> with a size greater than <code>limit</code> must contain <strong>both </strong>0 and 1.</li>
</ul>

<p>Return the <em>total</em> number of <strong>stable</strong> binary arrays.</p>

<p>Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">zero = 1, one = 1, limit = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The two possible stable binary arrays are <code>[1,0]</code> and <code>[0,1]</code>, as both arrays have a single 0 and a single 1, and no subarray has a length greater than 2.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">zero = 1, one = 2, limit = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>The only possible stable binary array is <code>[1,0,1]</code>.</p>

<p>Note that the binary arrays <code>[1,1,0]</code> and <code>[0,1,1]</code> have subarrays of length 2 with identical elements, hence, they are not stable.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">zero = 3, one = 3, limit = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">14</span></p>

<p><strong>Explanation:</strong></p>

<p>All the possible stable binary arrays are <code>[0,0,1,0,1,1]</code>, <code>[0,0,1,1,0,1]</code>, <code>[0,1,0,0,1,1]</code>, <code>[0,1,0,1,0,1]</code>, <code>[0,1,0,1,1,0]</code>, <code>[0,1,1,0,0,1]</code>, <code>[0,1,1,0,1,0]</code>, <code>[1,0,0,1,0,1]</code>, <code>[1,0,0,1,1,0]</code>, <code>[1,0,1,0,0,1]</code>, <code>[1,0,1,0,1,0]</code>, <code>[1,0,1,1,0,0]</code>, <code>[1,1,0,0,1,0]</code>, and <code>[1,1,0,1,0,0]</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= zero, one, limit &lt;= 200</code></li>
</ul>


## Hints

1. Let `dp[a][b][c = 0/1][d]` be the number of stable arrays with exactly `a` 0s, `b` 1s and consecutive `d` value of `c`’s at the end.

2. Try each case by appending a 0/1 at last to get the inductions.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be solved using dynamic programming by defining $dp[i][j][k]$ as the number of stable binary arrays containing exactly $i$ zeros and $j$ ones, ending with the digit $k$ (where $k=0$ or $k=1$). A stable array is one where no block of consecutive identical digits exceeds the given $limit$. The total number of stable arrays is the sum of arrays ending in zero and those ending in one: $dp[zero][one][0] + dp[zero][one][1]$.

To compute $dp[i][j][0]$, we consider appending a zero to any stable array with $i-1$ zeros and $j$ ones. This transition is represented by $dp[i-1][j][0] + dp[i-1][j][1]$. However, we must subtract cases where this creates a sequence of $limit + 1$ consecutive zeros. These invalid sequences are formed by appending $limit+1$ zeros to a stable sequence that ended in 1 (or was empty) and had $i-(limit+1)$ zeros. Thus, we subtract $dp[i-limit-1][j][1]$ from the total. A symmetric recurrence applies to $dp[i][j][1]$ by swapping the roles of zeros and ones.

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
    int numberOfStableArrays(int zero, int one, int limit) {
        long long MOD = 1e9 + 7;
        vector<vector<vector<long long>>> dp(zero + 1, vector<vector<long long>>(one + 1, vector<long long>(2, 0)));

        for (int i = 1; i <= min(zero, limit); ++i) dp[i][0][0] = 1;
        for (int j = 1; j <= min(one, limit); ++j) dp[0][j][1] = 1;

        for (int i = 1; i <= zero; ++i) {
            for (int j = 1; j <= one; ++j) {
                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % MOD;
                if (i > limit) {
                    dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1] + MOD) % MOD;
                }

                dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % MOD;
                if (j > limit) {
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0] + MOD) % MOD;
                }
            }
        }

        return (int)((dp[zero][one][0] + dp[zero][one][1]) % MOD);
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int numberOfStableArrays(int zero, int one, int limit) {
        long MOD = 1_000_000_007;
        long[][][] dp = new long[zero + 1][one + 1][2];

        for (int i = 1; i <= Math.min(zero, limit); i++) dp[i][0][0] = 1;
        for (int j = 1; j <= Math.min(one, limit); j++) dp[0][j][1] = 1;

        for (int i = 1; i <= zero; i++) {
            for (int j = 1; j <= one; j++) {
                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % MOD;
                if (i > limit) {
                    dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1] + MOD) % MOD;
                }

                dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % MOD;
                if (j > limit) {
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0] + MOD) % MOD;
                }
            }
        }

        return (int) ((dp[zero][one][0] + dp[zero][one][1]) % MOD);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def numberOfStableArrays(self, zero, one, limit):
        """
        :type zero: int
        :type one: int
        :type limit: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]

        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1

        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % MOD
                if i > limit:
                    dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1] + MOD) % MOD

                dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % MOD
                if j > limit:
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0] + MOD) % MOD

        return (dp[zero][one][0] + dp[zero][one][1]) % MOD
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]

        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1

        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % MOD
                if i > limit:
                    dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1] + MOD) % MOD

                dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % MOD
                if j > limit:
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0] + MOD) % MOD

        return (dp[zero][one][0] + dp[zero][one][1]) % MOD
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int numberOfStableArrays(int zero, int one, int limit) {
    long long MOD = 1e9 + 7;
    static long long dp[201][201][2];

    for (int i = 0; i <= zero; i++) {
        for (int j = 0; j <= one; j++) {
            dp[i][j][0] = dp[i][j][1] = 0;
        }
    }

    for (int i = 1; i <= (zero < limit ? zero : limit); i++) dp[i][0][0] = 1;
    for (int j = 1; j <= (one < limit ? one : limit); j++) dp[0][j][1] = 1;

    for (int i = 1; i <= zero; i++) {
        for (int j = 1; j <= one; j++) {
            dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % MOD;
            if (i > limit)
                dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1] + MOD) % MOD;

            dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % MOD;
            if (j > limit)
                dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0] + MOD) % MOD;
        }
    }

    return (int)((dp[zero][one][0] + dp[zero][one][1]) % MOD);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int NumberOfStableArrays(int zero, int one, int limit) {
        long MOD = 1000000007;
        long[,,] dp = new long[zero + 1, one + 1, 2];

        for (int i = 1; i <= Math.Min(zero, limit); i++) dp[i, 0, 0] = 1;
        for (int j = 1; j <= Math.Min(one, limit); j++) dp[0, j, 1] = 1;

        for (int i = 1; i <= zero; i++) {
            for (int j = 1; j <= one; j++) {
                dp[i, j, 0] = (dp[i - 1, j, 0] + dp[i - 1, j, 1]) % MOD;
                if (i > limit) {
                    dp[i, j, 0] = (dp[i, j, 0] - dp[i - limit - 1, j, 1] + MOD) % MOD;
                }

                dp[i, j, 1] = (dp[i, j - 1, 0] + dp[i, j - 1, 1]) % MOD;
                if (j > limit) {
                    dp[i, j, 1] = (dp[i, j, 1] - dp[i, j - limit - 1, 0] + MOD) % MOD;
                }
            }
        }

        return (int)((dp[zero, one, 0] + dp[zero, one, 1]) % MOD);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} zero
 * @param {number} one
 * @param {number} limit
 * @return {number}
 */
var numberOfStableArrays = function(zero, one, limit) {
    const MOD = 1000000007;
    const dp = Array.from({ length: zero + 1 }, () =>
        Array.from({ length: one + 1 }, () => new BigInt64Array(2).fill(0n))
    );

    for (let i = 1; i <= Math.min(zero, limit); i++) dp[i][0][0] = 1n;
    for (let j = 1; j <= Math.min(one, limit); j++) dp[0][j][1] = 1n;

    for (let i = 1; i <= zero; i++) {
        for (let j = 1; j <= one; j++) {
            dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % BigInt(MOD);
            if (i > limit) {
                dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1] + BigInt(MOD)) % BigInt(MOD);
            }

            dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % BigInt(MOD);
            if (j > limit) {
                dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0] + BigInt(MOD)) % BigInt(MOD);
            }
        }
    }

    return Number((dp[zero][one][0] + dp[zero][one][1]) % BigInt(MOD));
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function numberOfStableArrays(zero: number, one: number, limit: number): number {
    const MOD = 1000000007;
    const dp = Array.from({ length: zero + 1 }, () => Array.from({ length: one + 1 }, () => [0, 0]));
    for (let i = 1; i <= Math.min(zero, limit); i++) dp[i][0][0] = 1;
    for (let j = 1; j <= Math.min(one, limit); j++) dp[0][j][1] = 1;
    for (let i = 1; i <= zero; i++) {
        for (let j = 1; j <= one; j++) {
            dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % MOD;
            if (i > limit) {
                dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1] + MOD) % MOD;
            }
            dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % MOD;
            if (j > limit) {
                dp[i][j][1] = (dp[i][j][1] - dp[i - limit - 1][0] || 0);
                dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % MOD;
                if (j > limit) {
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0] + MOD) % MOD;
                }
            }
        }
    }
    return (dp[zero][one][0] + dp[zero][one][1]) % MOD;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $zero
     * @param Integer $one
     * @param Integer $limit
     * @return Integer
     */
    function numberOfStableArrays($zero, $one, $limit) {
        $MOD = 1000000007;
        $dp = array_fill(0, $zero + 1, array_fill(0, $one + 1, [0, 0]));
        for ($i = 1; $i <= min($zero, $limit); $i++) {
            $dp[$i][0][0] = 1;
        }
        for ($j = 1; $j <= min($one, $limit); $j++) {
            $dp[0][$j][1] = 1;
        }
        for ($i = 1; $i <= $zero; $i++) {
            for ($j = 1; $j <= $one; $j++) {
                $dp[$i][$j][0] = ($dp[$i - 1][$j][0] + $dp[$i - 1][$j][1]) % $MOD;
                if ($i > $limit) {
                    $dp[$i][$j][0] = ($dp[$i][$j][0] - $dp[$i - $limit - 1][$j][1] + $MOD) % $MOD;
                }
                $dp[$i][$j][1] = ($dp[$i][$j - 1][0] + $dp[$i][$j - 1][1]) % $MOD;
                if ($j > $limit) {
                    $dp[$i][$j][1] = ($dp[$i][$j][1] - $dp[$i][$j - $limit - 1][0] + $MOD) % $MOD;
                }
            }
        }
        return ($dp[$zero][$one][0] + $dp[$zero][$one][1]) % $MOD;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func numberOfStableArrays(_ zero: Int, _ one: Int, _ limit: Int) -> Int {
        let MOD = 1_000_000_007
        var dp = Array(repeating: Array(repeating: [0, 0], count: one + 1), count: zero + 1)
        for i in 1...min(zero, limit) {
            dp[i][0][0] = 1
        }
        for j in 1...min(one, limit) {
            dp[0][j][1] = 1
        }
        if zero > 0 && one > 0 {
            for i in 1...zero {
                for j in 1...one {
                    dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % MOD
                    if i > limit {
                        dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1] + MOD) % MOD
                    }
                    dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % MOD
                    if j > limit {
                        dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0] + MOD) % MOD
                    }
                }
            }
        }
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun numberOfStableArrays(zero: Int, one: Int, limit: Int): Int {
        val MOD = 1000000007
        val dp = Array(zero + 1) { Array(one + 1) { IntArray(2) } }
        for (i in 1..minOf(zero, limit)) {
            dp[i][0][0] = 1
        }
        for (j in 1..minOf(one, limit)) {
            dp[0][j][1] = 1
        }
        for (i in 1..zero) {
            for (j in 1..one) {
                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % MOD
                if (i > limit) {
                    dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1] + MOD) % MOD
                }
                dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % MOD
                if (j > limit) {
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0] + MOD) % MOD
                }
            }
        }
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int numberOfStableArrays(int zero, int one, int limit) {
    final int mod = 1000000007;
    var dp = List.generate(zero + 1, (_) => List.generate(one + 1, (_) => List.filled(2, 0)));
    for (int i = 1; i <= zero && i <= limit; i++) {
      dp[i][0][0] = 1;
    }
    for (int j = 1; j <= one && j <= limit; j++) {
      dp[0][j][1] = 1;
    }
    for (int i = 1; i <= zero; i++) {
      for (int j = 1; j <= one; j++) {
        dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % mod;
        if (i > limit) {
          dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1] + mod) % mod;
        }
        dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % mod;
        if (j > limit) {
          dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0] + mod) % mod;
        }
      }
    }
    return (dp[zero][one][0] + dp[zero][one][1]) % mod;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func numberOfStableArrays(zero int, one int, limit int) int {
    const MOD = 1000000007
    dp := make([][][2]int, zero+1)
    for i := range dp {
        dp[i] = make([][2]int, one+1)
    }
    for i := 1; i <= zero && i <= limit; i++ {
        dp[i][0][0] = 1
    }
    for j := 1; j <= one && j <= limit; j++ {
        dp[0][j][1] = 1
    }
    for i := 1; i <= zero; i++ {
        for j := 1; j <= one; j++ {
            dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1]) % MOD
            if i > limit {
                dp[i][j][0] = (dp[i][j][0] - dp[i-limit-1][j][1] + MOD) % MOD
            }
            dp[i][j][1] = (dp[i][j-1][0] + dp[i][j-1][1]) % MOD
            if j > limit {
                dp[i][j][1] = (dp[i][j][1] - dp[i][j-limit-1][0] + MOD) % MOD
            }
        }
    }
    return (dp[zero][one][0] + dp[zero][one][1]) % MOD
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def number_of_stable_arrays(zero, one, limit)
  mod = 1_000_000_007
  dp = Array.new(zero + 1) { Array.new(one + 1) { [0, 0] } }
  (1..[zero, limit].min).each { |i| dp[i][0][0] = 1 }
  (1..[one, limit].min).each { |j| dp[0][j][1] = 1 }
  (1..zero).each do |i|
    (1..one).each do |j|
      dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % mod
      if i > limit
        dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1] + mod) % mod
      end
      dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % mod
      if j > limit
        dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0] + mod) % mod
      end
    end
  end
  (dp[zero][one][0] + dp[zero][one][1]) % mod
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def numberOfStableArrays(zero: Int, one: Int, limit: Int): Int = {
    val MOD = 1000000007
    val dp = Array.ofDim[Int](zero + 1, one + 1, 2)
    for (i <- 1 to Math.min(zero, limit)) dp(i)(0)(0) = 1
    for (j <- 1 to Math.min(one, limit)) dp(0)(j)(1) = 1
    for (i <- 1 to zero) {
      for (j <- 1 to one) {
        dp(i)(j)(0) = ((dp(i - 1)(j)(0).toLong + dp(i - 1)(j)(1)) % MOD).toInt
        if (i > limit) {
          dp(i)(j)(0) = ((dp(i)(j)(0).toLong - dp(i - limit - 1)(j)(1) + MOD) % MOD).toInt
        }
        dp(i)(j)(1) = ((dp(i)(j - 1)(0).toLong + dp(i)(j - 1)(1)) % MOD).toInt
        if (j > limit) {
          dp(i)(j)(1) = ((dp(i)(j)(1).toLong - dp(i)(j - limit - 1)(0) + MOD) % MOD).toInt
        }
      }
    }
    ((dp(zero)(one)(0).toLong + dp(zero)(one)(1)) % MOD).toInt
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn number_of_stable_arrays(zero: i32, one: i32, limit: i32) -> i32 {
        let (z, o, l) = (zero as usize, one as usize, limit as usize);
        let mut dp = vec![vec![[0i32; 2]; o + 1]; z + 1];
        let mod_val = 1_000_000_007;

        for i in 1..=std::cmp::min(z, l) {
            dp[i][0][0] = 1;
        }
        for j in 1..=std::cmp::min(o, l) {
            dp[0][j][1] = 1;
        }

        for i in 1..=z {
            for j in 1..=o {
                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % mod_val;
                if i > l {
                    dp[i][j][0] = (dp[i][j][0] - dp[i - l - 1][j][1] + mod_val) % mod_val;
                }
                dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % mod_val;
                if j > l {
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j - l - 1][0] + mod_val) % mod_val;
                }
            }
        }
        (dp[z][o][0] + dp[z][o][1]) % mod_val
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (number-of-stable-arrays zero one limit)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ([dp (make-vector (* (+ zero 1) (+ one 1) 2) 0)]
         [get-dp (lambda (i j k) (vector-ref dp (+ (* i (+ one 1) 2) (* j 2) k)))]
         [set-dp! (lambda (i j k val) (vector-set! dp (+ (* i (+ one 1) 2) (* j 2) k) val))])
    (for ([i (in-range 1 (+ (min zero limit) 1))]) (set-dp! i 0 0 1))
    (for ([j (in-range 1 (+ (min one limit) 1))]) (set-dp! 0 j 1 1))
    (for* ([i (in-range 1 (+ zero 1))]
           [j (in-range 1 (+ one 1))])
      (let* ([ways0 (modulo (+ (get-dp (- i 1) j 0) (get-dp (- i 1) j 1)) 1000000007)]
             [ways0-final (if (> i limit)
                              (modulo (- ways0 (get-dp (- i limit 1) j 1)) 1000000007)
                              ways0)])
        (set-dp! i j 0 ways0-final))
      (let* ([ways1 (modulo (+ (get-dp i (- j 1) 0) (get-dp i (- j 1) 1)) 1000000007)]
             [ways1-final (if (> j limit)
                              (modulo (- ways1 (get-dp i (- j limit 1) 0)) 1000000007)
                              ways1)])
        (set-dp! i j 1 ways1-final)))
    (modulo (+ (get-dp zero one 0) (get-dp zero one 1)) 1000000007)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
number_of_stable_arrays(Zero, One, Limit) ->
  MOD = 1000000007,
  DP0 = lists:foldl(fun(I, Acc) -> Acc#{ {I, 0, 0} => 1 } end, #{}, lists:seq(1, erlang:min(Zero, Limit))),
  DP1 = lists:foldl(fun(J, Acc) -> Acc#{ {0, J, 1} => 1 } end, DP0, lists:seq(1, erlang:min(One, Limit))),
  FinalDP = lists:foldl(fun(I, AccI) ->
    lists:foldl(fun(J, AccJ) ->
      Ways0 = (maps:get({I - 1, J, 0}, AccJ, 0) + maps:get({I - 1, J, 1}, AccJ, 0)) rem MOD,
      Ways0F = case I > Limit of
        true -> (Ways0 - maps:get({I - Limit - 1, J, 1}, AccJ, 0) + MOD) rem MOD;
        false -> Ways0
      end,
      Ways1 = (maps:get({I, J - 1, 0}, AccJ, 0) + maps:get({I, J - 1, 1}, AccJ, 0)) rem MOD,
      Ways1F = case J > Limit of
        true -> (Ways1 - maps:get({I, J - Limit - 1, 0}, AccJ, 0) + MOD) rem MOD;
        false -> Ways1
      end,
      AccJ#{ {I, J, 0} => Ways0F, {I, J, 1} => Ways1F }
    end, AccI, lists:seq(1, One))
  end, DP1, lists:seq(1, Zero)),
  (maps:get({Zero, One, 0}, FinalDP, 0) + maps:get({Zero, One, 1}, FinalDP, 0)) rem MOD.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec number_of_stable_arrays(zero :: integer, one :: integer, limit :: integer) :: integer
  def number_of_stable_arrays(zero, one, limit) do
    mod = 1_000_000_007
    dp = %{}
    dp = Enum.reduce(1..min(zero, limit), dp, fn i, acc -> Map.put(acc, {i, 0, 0}, 1) end)
    dp = Enum.reduce(1..min(one, limit), dp, fn j, acc -> Map.put(acc, {0, j, 1}, 1) end)

    final_dp = Enum.reduce(1..zero, dp, fn i, acc_i ->
      Enum.reduce(1..one, acc_i, fn j, acc_j ->
        ways0 = rem(Map.get(acc_j, {i - 1, j, 0}, 0) + Map.get(acc_j, {i - 1, j, 1}, 0), mod)
        ways0 = if i > limit do rem(ways0 - Map.get(acc_j, {i - limit - 1, j, 1}, 0) + mod, mod) else ways0 end

        ways1 = rem(Map.get(acc_j, {i, j - 1, 0}, 0) + Map.get(acc_j, {i, j - 1, 1}, 0), mod)
        ways1 = if j > limit do rem(ways1 - Map.get(acc_j, {i, j - limit - 1, 0}, 0) + mod, mod) else ways1 end

        acc_j |> Map.put({i, j, 0}, ways0) |> Map.put({i, j, 1}, ways1)
      end)
    end)

    rem(Map.get(final_dp, {zero, one, 0}, 0) + Map.get(final_dp, {zero, one, 1}, 0), mod)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(zero * one). We iterate through a 2D grid of size $(zero+1) 	imes (one+1)$, and for each cell, we perform a constant number of operations to update the two states (ending in 0 or 1).
- **Space Complexity:** O(zero * one). We maintain a 3D dynamic programming table of size $(zero+1) 	imes (one+1) 	imes 2$ to store the number of stable arrays for each state.
