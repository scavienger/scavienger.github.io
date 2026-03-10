---
layout: post
title: "Find All Possible Stable Binary Arrays II"
date: 2026-03-10 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Dynamic Programming", "Prefix Sum"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int numberOfStableArrays(int zero, int one,\
        \ int limit) {\n        long long MOD = 1e9 + 7;\n        vector<vector<int>>\
        \ dp0(zero + 1, vector<int>(one + 1, 0));\n        vector<vector<int>> dp1(zero\
        \ + 1, vector<int>(one + 1, 0));\n\n        for (int i = 0; i <= min(zero, limit);\
        \ ++i) dp0[i][0] = 1;\n        for (int j = 0; j <= min(one, limit); ++j) dp1[0][j]\
        \ = 1;\n\n        for (int i = 1; i <= zero; ++i) {\n            for (int j\
        \ = 1; j <= one; ++j) {\n                dp0[i][j] = (dp0[i - 1][j] + dp1[i\
        \ - 1][j]) % MOD;\n                if (i > limit) {\n                    dp0[i][j]\
        \ = (dp0[i][j] - dp1[i - limit - 1][j] + MOD) % MOD;\n                }\n  \
        \              dp1[i][j] = (dp0[i][j - 1] + dp1[i][j - 1]) % MOD;\n        \
        \        if (j > limit) {\n                    dp1[i][j] = (dp1[i][j] - dp0[i][j\
        \ - limit - 1] + MOD) % MOD;\n                }\n            }\n        }\n\
        \        return (dp0[zero][one] + dp1[zero][one]) % MOD;\n    }\n};"
      java: "class Solution {\n    public int numberOfStableArrays(int zero, int one,\
        \ int limit) {\n        long MOD = 1_000_000_007;\n        int[][] dp0 = new\
        \ int[zero + 1][one + 1];\n        int[][] dp1 = new int[zero + 1][one + 1];\n\
        \n        for (int i = 0; i <= Math.min(zero, limit); i++) dp0[i][0] = 1;\n\
        \        for (int j = 0; j <= Math.min(one, limit); j++) dp1[0][j] = 1;\n\n\
        \        for (int i = 1; i <= zero; i++) {\n            for (int j = 1; j <=\
        \ one; j++) {\n                dp0[i][j] = (int) ((dp0[i - 1][j] + (long) dp1[i\
        \ - 1][j]) % MOD);\n                if (i > limit) {\n                    dp0[i][j]\
        \ = (int) ((dp0[i][j] - (long) dp1[i - limit - 1][j] + MOD) % MOD);\n      \
        \          }\n                dp1[i][j] = (int) ((dp0[i][j - 1] + (long) dp1[i][j\
        \ - 1]) % MOD);\n                if (j > limit) {\n                    dp1[i][j]\
        \ = (int) ((dp1[i][j] - (long) dp0[i][j - limit - 1] + MOD) % MOD);\n      \
        \          }\n            }\n        }\n        return (int) ((dp0[zero][one]\
        \ + (long) dp1[zero][one]) % MOD);\n    }\n}"
      python: "class Solution(object):\n    def numberOfStableArrays(self, zero, one,\
        \ limit):\n        \"\"\"\n        :type zero: int\n        :type one: int\n\
        \        :type limit: int\n        :rtype: int\n        \"\"\"\n        MOD\
        \ = 10**9 + 7\n        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]\n  \
        \      dp1 = [[0] * (one + 1) for _ in range(zero + 1)]\n\n        for i in\
        \ range(min(zero, limit) + 1):\n            dp0[i][0] = 1\n        for j in\
        \ range(min(one, limit) + 1):\n            dp1[0][j] = 1\n\n        for i in\
        \ range(1, zero + 1):\n            for j in range(1, one + 1):\n           \
        \     dp0[i][j] = (dp0[i - 1][j] + dp1[i - 1][j]) % MOD\n                if\
        \ i > limit:\n                    dp0[i][j] = (dp0[i][j] - dp1[i - limit - 1][j]\
        \ + MOD) % MOD\n\n                dp1[i][j] = (dp0[i][j - 1] + dp1[i][j - 1])\
        \ % MOD\n                if j > limit:\n                    dp1[i][j] = (dp1[i][j]\
        \ - dp0[i][j - limit - 1] + MOD) % MOD\n\n        return (dp0[zero][one] + dp1[zero][one])\
        \ % MOD"
      python3: "class Solution:\n    def numberOfStableArrays(self, zero: int, one:\
        \ int, limit: int) -> int:\n        MOD = 10**9 + 7\n        dp0 = [[0] * (one\
        \ + 1) for _ in range(zero + 1)]\n        dp1 = [[0] * (one + 1) for _ in range(zero\
        \ + 1)]\n\n        for i in range(min(zero, limit) + 1):\n            dp0[i][0]\
        \ = 1\n        for j in range(min(one, limit) + 1):\n            dp1[0][j] =\
        \ 1\n\n        for i in range(1, zero + 1):\n            for j in range(1, one\
        \ + 1):\n                dp0[i][j] = (dp0[i - 1][j] + dp1[i - 1][j]) % MOD\n\
        \                if i > limit:\n                    dp0[i][j] = (dp0[i][j] -\
        \ dp1[i - limit - 1][j] + MOD) % MOD\n\n                dp1[i][j] = (dp0[i][j\
        \ - 1] + dp1[i][j - 1]) % MOD\n                if j > limit:\n             \
        \       dp1[i][j] = (dp1[i][j] - dp0[i][j - limit - 1] + MOD) % MOD\n\n    \
        \    return (dp0[zero][one] + dp1[zero][one]) % MOD"
      c: "int numberOfStableArrays(int zero, int one, int limit) {\n    int MOD = 1000000007;\n\
        \    int (*dp0)[one + 1] = calloc(zero + 1, sizeof(*dp0));\n    int (*dp1)[one\
        \ + 1] = calloc(zero + 1, sizeof(*dp1));\n\n    for (int i = 0; i <= (zero <\
        \ limit ? zero : limit); i++) dp0[i][0] = 1;\n    for (int j = 0; j <= (one\
        \ < limit ? one : limit); j++) dp1[0][j] = 1;\n\n    for (int i = 1; i <= zero;\
        \ i++) {\n        for (int j = 1; j <= one; j++) {\n            dp0[i][j] =\
        \ (dp0[i - 1][j] + dp1[i - 1][j]) % MOD;\n            if (i > limit) {\n   \
        \             dp0[i][j] = (dp0[i][j] - dp1[i - limit - 1][j] + MOD) % MOD;\n\
        \            }\n            dp1[i][j] = (dp0[i][j - 1] + dp1[i][j - 1]) % MOD;\n\
        \            if (j > limit) {\n                dp1[i][j] = (dp1[i][j] - dp0[i][j\
        \ - limit - 1] + MOD) % MOD;\n            }\n        }\n    }\n\n    int result\
        \ = (dp0[zero][one] + dp1[zero][one]) % MOD;\n    free(dp0);\n    free(dp1);\n\
        \    return result;\n}"
      csharp: "public class Solution {\n    public int NumberOfStableArrays(int zero,\
        \ int one, int limit) {\n        long MOD = 1_000_000_007;\n        int[,] dp0\
        \ = new int[zero + 1, one + 1];\n        int[,] dp1 = new int[zero + 1, one\
        \ + 1];\n\n        for (int i = 0; i <= Math.Min(zero, limit); i++) dp0[i, 0]\
        \ = 1;\n        for (int j = 0; j <= Math.Min(one, limit); j++) dp1[0, j] =\
        \ 1;\n\n        for (int i = 1; i <= zero; i++) {\n            for (int j =\
        \ 1; j <= one; j++) {\n                dp0[i, j] = (int)((dp0[i - 1, j] + (long)dp1[i\
        \ - 1, j]) % MOD);\n                if (i > limit) {\n                    dp0[i,\
        \ j] = (int)((dp0[i, j] - (long)dp1[i - limit - 1, j] + MOD) % MOD);\n     \
        \           }\n                dp1[i, j] = (int)((dp0[i, j - 1] + (long)dp1[i,\
        \ j - 1]) % MOD);\n                if (j > limit) {\n                    dp1[i,\
        \ j] = (int)((dp1[i, j] - (long)dp0[i, j - limit - 1] + MOD) % MOD);\n     \
        \           }\n            }\n        }\n        return (int)((dp0[zero, one]\
        \ + (long)dp1[zero, one]) % MOD);\n    }\n}"
      javascript: "/**\n * @param {number} zero\n * @param {number} one\n * @param {number}\
        \ limit\n * @return {number}\n */\nvar numberOfStableArrays = function(zero,\
        \ one, limit) {\n    const MOD = 1000000007;\n    const dp0 = new Int32Array((zero\
        \ + 1) * (one + 1));\n    const dp1 = new Int32Array((zero + 1) * (one + 1));\n\
        \n    const getIdx = (i, j) => i * (one + 1) + j;\n\n    for (let i = 0; i <=\
        \ Math.min(zero, limit); i++) dp0[getIdx(i, 0)] = 1;\n    for (let j = 0; j\
        \ <= Math.min(one, limit); j++) dp1[getIdx(0, j)] = 1;\n\n    for (let i = 1;\
        \ i <= zero; i++) {\n        for (let j = 1; j <= one; j++) {\n            let\
        \ idx = getIdx(i, j);\n            dp0[idx] = (dp0[getIdx(i - 1, j)] + dp1[getIdx(i\
        \ - 1, j)]) % MOD;\n            if (i > limit) {\n                dp0[idx] =\
        \ (dp0[idx] - dp1[getIdx(i - limit - 1, j)] + MOD) % MOD;\n            }\n \
        \           dp1[idx] = (dp0[getIdx(i, j - 1)] + dp1[getIdx(i, j - 1)]) % MOD;\n\
        \            if (j > limit) {\n                dp1[idx] = (dp1[idx] - dp0[getIdx(i,\
        \ j - limit - 1)] + MOD) % MOD;\n            }\n        }\n    }\n    return\
        \ (dp0[getIdx(zero, one)] + dp1[getIdx(zero, one)]) % MOD;\n};"
      typescript: "function numberOfStableArrays(zero: number, one: number, limit: number):\
        \ number {\n    const MOD = 1000000007;\n    const dp0 = Array.from({ length:\
        \ zero + 1 }, () => new Int32Array(one + 1));\n    const dp1 = Array.from({\
        \ length: zero + 1 }, () => new Int32Array(one + 1));\n    for (let i = 1; i\
        \ <= zero && i <= limit; i++) dp0[i][0] = 1;\n    for (let j = 1; j <= one &&\
        \ j <= limit; j++) dp1[0][j] = 1;\n    for (let i = 1; i <= zero; i++) {\n \
        \       for (let j = 1; j <= one; j++) {\n            dp0[i][j] = (dp0[i - 1][j]\
        \ + dp1[i - 1][j]) % MOD;\n            if (i > limit) {\n                dp0[i][j]\
        \ = (dp0[i][j] - dp1[i - limit - 1][j] + MOD) % MOD;\n            }\n      \
        \      dp1[i][j] = (dp0[i][j - 1] + dp1[i][j - 1]) % MOD;\n            if (j\
        \ > limit) {\n                dp1[i][j] = (dp1[i][j] - dp0[i][j - limit - 1]\
        \ + MOD) % MOD;\n            }\n        }\n    }\n    return (dp0[zero][one]\
        \ + dp1[zero][one]) % MOD;\n}"
      php: "class Solution {\n    function numberOfStableArrays($zero, $one, $limit)\
        \ {\n        $MOD = 1000000007;\n        $dp0 = array_fill(0, $zero + 1, array_fill(0,\
        \ $one + 1, 0));\n        $dp1 = array_fill(0, $zero + 1, array_fill(0, $one\
        \ + 1, 0));\n        for ($i = 1; $i <= min($zero, $limit); $i++) {\n      \
        \      $dp0[$i][0] = 1;\n        }\n        for ($j = 1; $j <= min($one, $limit);\
        \ $j++) {\n            $dp1[0][$j] = 1;\n        }\n        for ($i = 1; $i\
        \ <= $zero; $i++) {\n            for ($j = 1; $j <= $one; $j++) {\n        \
        \        $dp0[$i][$j] = ($dp0[$i - 1][$j] + $dp1[$i - 1][$j]) % $MOD;\n    \
        \            if ($i > $limit) {\n                    $dp0[$i][$j] = ($dp0[$i][$j]\
        \ - $dp1[$i - $limit - 1][$j] + $MOD) % $MOD;\n                }\n         \
        \       $dp1[$i][$j] = ($dp0[$i][$j - 1] + $dp1[$i][$j - 1]) % $MOD;\n     \
        \           if ($j > $limit) {\n                    $dp1[$i][$j] = ($dp1[$i][$j]\
        \ - $dp0[$i][$j - $limit - 1] + $MOD) % $MOD;\n                }\n         \
        \   }\n        }\n        return ($dp0[$zero][$one] + $dp1[$zero][$one]) % $MOD;\n\
        \    }\n}"
      swift: "class Solution {\n    func numberOfStableArrays(_ zero: Int, _ one: Int,\
        \ _ limit: Int) -> Int {\n        let MOD = 1_000_000_007\n        let cols\
        \ = one + 1\n        var dp0 = [Int](repeating: 0, count: (zero + 1) * cols)\n\
        \        var dp1 = [Int](repeating: 0, count: (zero + 1) * cols)\n        for\
        \ i in 1...min(zero, limit) {\n            dp0[i * cols] = 1\n        }\n  \
        \      for j in 1...min(one, limit) {\n            dp1[j] = 1\n        }\n \
        \       for i in 1...zero {\n            for j in 1...one {\n              \
        \  let curr = i * cols + j\n                dp0[curr] = (dp0[(i - 1) * cols\
        \ + j] + dp1[(i - 1) * cols + j]) % MOD\n                if i > limit {\n  \
        \                  dp0[curr] = (dp0[curr] - dp1[(i - limit - 1) * cols + j]\
        \ + MOD) % MOD\n                }\n                dp1[curr] = (dp0[i * cols\
        \ + (j - 1)] + dp1[i * cols + (j - 1)]) % MOD\n                if j > limit\
        \ {\n                    dp1[curr] = (dp1[curr] - dp0[i * cols + (j - limit\
        \ - 1)] + MOD) % MOD\n                }\n            }\n        }\n        return\
        \ (dp0[zero * cols + one] + dp1[zero * cols + one]) % MOD\n    }\n}"
      kotlin: "class Solution {\n    fun numberOfStableArrays(zero: Int, one: Int, limit:\
        \ Int): Int {\n        val MOD = 1000000007\n        val dp0 = Array(zero +\
        \ 1) { IntArray(one + 1) }\n        val dp1 = Array(zero + 1) { IntArray(one\
        \ + 1) }\n        for (i in 1..if (zero < limit) zero else limit) {\n      \
        \      dp0[i][0] = 1\n        }\n        for (j in 1..if (one < limit) one else\
        \ limit) {\n            dp1[0][j] = 1\n        }\n        for (i in 1..zero)\
        \ {\n            for (j in 1..one) {\n                dp0[i][j] = (dp0[i - 1][j]\
        \ + dp1[i - 1][j]) % MOD\n                if (i > limit) {\n               \
        \     dp0[i][j] = (dp0[i][j] - dp1[i - limit - 1][j] + MOD) % MOD\n        \
        \        }\n                dp1[i][j] = (dp0[i][j - 1] + dp1[i][j - 1]) % MOD\n\
        \                if (j > limit) {\n                    dp1[i][j] = (dp1[i][j]\
        \ - dp0[i][j - limit - 1] + MOD) % MOD\n                }\n            }\n \
        \       }\n        return (dp0[zero][one] + dp1[zero][one]) % MOD\n    }\n}"
      dart: "class Solution {\n  int numberOfStableArrays(int zero, int one, int limit)\
        \ {\n    const int mod = 1000000007;\n    List<List<int>> dp0 = List.generate(zero\
        \ + 1, (_) => List.filled(one + 1, 0));\n    List<List<int>> dp1 = List.generate(zero\
        \ + 1, (_) => List.filled(one + 1, 0));\n    for (int i = 1; i <= (zero < limit\
        \ ? zero : limit); i++) {\n      dp0[i][0] = 1;\n    }\n    for (int j = 1;\
        \ j <= (one < limit ? one : limit); j++) {\n      dp1[0][j] = 1;\n    }\n  \
        \  for (int i = 1; i <= zero; i++) {\n      for (int j = 1; j <= one; j++) {\n\
        \        dp0[i][j] = (dp0[i - 1][j] + dp1[i - 1][j]) % mod;\n        if (i >\
        \ limit) {\n          dp0[i][j] = (dp0[i][j] - dp1[i - limit - 1][j] + mod)\
        \ % mod;\n        }\n        dp1[i][j] = (dp0[i][j - 1] + dp1[i][j - 1]) % mod;\n\
        \        if (j > limit) {\n          dp1[i][j] = (dp1[i][j] - dp0[i][j - limit\
        \ - 1] + mod) % mod;\n        }\n      }\n    }\n    return (dp0[zero][one]\
        \ + dp1[zero][one]) % mod;\n  }\n}"
      go: "func numberOfStableArrays(zero int, one int, limit int) int {\n    const\
        \ mod = 1000000007\n    dp0 := make([][]int, zero+1)\n    dp1 := make([][]int,\
        \ zero+1)\n    for i := range dp0 {\n        dp0[i] = make([]int, one+1)\n \
        \       dp1[i] = make([]int, one+1)\n    }\n    for i := 1; i <= zero && i <=\
        \ limit; i++ {\n        dp0[i][0] = 1\n    }\n    for j := 1; j <= one && j\
        \ <= limit; j++ {\n        dp1[0][j] = 1\n    }\n    for i := 1; i <= zero;\
        \ i++ {\n        for j := 1; j <= one; j++ {\n            dp0[i][j] = (dp0[i-1][j]\
        \ + dp1[i-1][j]) % mod\n            if i > limit {\n                dp0[i][j]\
        \ = (dp0[i][j] - dp1[i-limit-1][j] + mod) % mod\n            }\n           \
        \ dp1[i][j] = (dp0[i][j-1] + dp1[i][j-1]) % mod\n            if j > limit {\n\
        \                dp1[i][j] = (dp1[i][j] - dp0[i][j-limit-1] + mod) % mod\n \
        \           }\n        }\n    }\n    return (dp0[zero][one] + dp1[zero][one])\
        \ % mod\n}"
      ruby: "def number_of_stable_arrays(zero, one, limit)\n  mod = 1_000_000_007\n\
        \  dp0 = Array.new(zero + 1) { Array.new(one + 1, 0) }\n  dp1 = Array.new(zero\
        \ + 1) { Array.new(one + 1, 0) }\n\n  [zero, limit].min.times { |i| dp0[i +\
        \ 1][0] = 1 }\n  [one, limit].min.times { |j| dp1[0][j + 1] = 1 }\n\n  (1..zero).each\
        \ do |i|\n    (1..one).each do |j|\n      v0 = (dp0[i - 1][j] + dp1[i - 1][j])\
        \ % mod\n      v0 = (v0 - dp1[i - limit - 1][j] + mod) % mod if i > limit\n\
        \      dp0[i][j] = v0\n\n      v1 = (dp1[i][j - 1] + dp0[i][j - 1]) % mod\n\
        \      v1 = (v1 - dp0[i][j - limit - 1] + mod) % mod if j > limit\n      dp1[i][j]\
        \ = v1\n    end\n  end\n\n  (dp0[zero][one] + dp1[zero][one]) % mod\nend"
      scala: "object Solution {\n    def numberOfStableArrays(zero: Int, one: Int, limit:\
        \ Int): Int = {\n        val mod = 1000000007\n        val dp0 = Array.ofDim[Int](zero\
        \ + 1, one + 1)\n        val dp1 = Array.ofDim[Int](zero + 1, one + 1)\n\n \
        \       for (i <- 1 to math.min(zero, limit)) dp0(i)(0) = 1\n        for (j\
        \ <- 1 to math.min(one, limit)) dp1(0)(j) = 1\n\n        for (i <- 1 to zero)\
        \ {\n            for (j <- 1 to one) {\n                var v0 = (dp0(i - 1)(j).toLong\
        \ + dp1(i - 1)(j).toLong) % mod\n                if (i > limit) v0 = (v0 - dp1(i\
        \ - limit - 1)(j) + mod) % mod\n                dp0(i)(j) = v0.toInt\n\n   \
        \             var v1 = (dp1(i)(j - 1).toLong + dp0(i)(j - 1).toLong) % mod\n\
        \                if (j > limit) v1 = (v1 - dp0(i)(j - limit - 1) + mod) % mod\n\
        \                dp1(i)(j) = v1.toInt\n            }\n        }\n\n        ((dp0(zero)(one).toLong\
        \ + dp1(zero)(one).toLong) % mod).toInt\n    }\n}"
      rust: "impl Solution {\n    pub fn number_of_stable_arrays(zero: i32, one: i32,\
        \ limit: i32) -> i32 {\n        let zero = zero as usize;\n        let one =\
        \ one as usize;\n        let limit = limit as usize;\n        let m = 1_000_000_007i64;\n\
        \        let mut dp0 = vec![vec![0i64; one + 1]; zero + 1];\n        let mut\
        \ dp1 = vec![vec![0i64; one + 1]; zero + 1];\n\n        for i in 1..=std::cmp::min(zero,\
        \ limit) {\n            dp0[i][0] = 1;\n        }\n        for j in 1..=std::cmp::min(one,\
        \ limit) {\n            dp1[0][j] = 1;\n        }\n\n        for i in 1..=zero\
        \ {\n            for j in 1..=one {\n                let mut v0 = (dp0[i - 1][j]\
        \ + dp1[i - 1][j]) % m;\n                if i > limit {\n                  \
        \  v0 = (v0 - dp1[i - limit - 1][j] + m) % m;\n                }\n         \
        \       dp0[i][j] = v0;\n\n                let mut v1 = (dp1[i][j - 1] + dp0[i][j\
        \ - 1]) % m;\n                if j > limit {\n                    v1 = (v1 -\
        \ dp0[i][j - limit - 1] + m) % m;\n                }\n                dp1[i][j]\
        \ = v1;\n            }\n        }\n\n        ((dp0[zero][one] + dp1[zero][one])\
        \ % m) as i32\n    }\n}"
      racket: "(define/contract (number-of-stable-arrays zero one limit)\n  (-> exact-integer?\
        \ exact-integer? exact-integer? exact-integer?)\n  (let* ([mod 1000000007]\n\
        \         [dp0 (make-vector (+ zero 1))]\n         [dp1 (make-vector (+ zero\
        \ 1))])\n    (for ([i (in-range (+ zero 1))])\n      (vector-set! dp0 i (make-vector\
        \ (+ one 1) 0))\n      (vector-set! dp1 i (make-vector (+ one 1) 0)))\n    (for\
        \ ([i (in-range 1 (+ (min zero limit) 1))])\n      (vector-set! (vector-ref\
        \ dp0 i) 0 1))\n    (for ([j (in-range 1 (+ (min one limit) 1))])\n      (vector-set!\
        \ (vector-ref dp1 0) j 1))\n    (for ([i (in-range 1 (+ zero 1))])\n      (let\
        \ ([dp0-i (vector-ref dp0 i)]\n            [dp1-i (vector-ref dp1 i)]\n    \
        \        [dp0-i-1 (vector-ref dp0 (- i 1))]\n            [dp1-i-1 (vector-ref\
        \ dp1 (- i 1))])\n        (for ([j (in-range 1 (+ one 1))])\n          (let*\
        \ ([v0 (modulo (+ (vector-ref dp0-i-1 j) (vector-ref dp1-i-1 j)) mod)]\n   \
        \              [v0 (if (> i limit)\n                         (modulo (- v0 (vector-ref\
        \ (vector-ref dp1 (- i limit 1)) j)) mod)\n                         v0)]\n \
        \                [v1 (modulo (+ (vector-ref dp1-i (- j 1)) (vector-ref dp0-i\
        \ (- j 1))) mod)]\n                 [v1 (if (> j limit)\n                  \
        \       (modulo (- v1 (vector-ref dp0-i (- j limit 1))) mod)\n             \
        \            v1)])\n            (vector-set! dp0-i j v0)\n            (vector-set!\
        \ dp1-i j v1)))))\n    (modulo (+ (vector-ref (vector-ref dp0 zero) one)\n \
        \              (vector-ref (vector-ref dp1 zero) one))\n            mod)))"
      erlang: "-spec number_of_stable_arrays(Zero :: integer(), One :: integer(), Limit\
        \ :: integer()) -> integer().\nnumber_of_stable_arrays(Zero, One, Limit) ->\n\
        \  MOD = 1000000007,\n  DP0 = ets:new(dp0, [set, private]),\n  DP1 = ets:new(dp1,\
        \ [set, private]),\n  lists:foreach(fun(I) -> ets:insert(DP0, {{I, 0}, 1}) end,\
        \ lists:seq(1, min(Zero, Limit))),\n  lists:foreach(fun(J) -> ets:insert(DP1,\
        \ {{0, J}, 1}) end, lists:seq(1, min(One, Limit))),\n  lists:foreach(fun(I)\
        \ ->\n    lists:foreach(fun(J) ->\n      Val0 = (get_v(DP0, I - 1, J) + get_v(DP1,\
        \ I - 1, J)) rem MOD,\n      Val0Final = if I > Limit -> (Val0 - get_v(DP1,\
        \ I - Limit - 1, J) + MOD) rem MOD; true -> Val0 end,\n      ets:insert(DP0,\
        \ {{I, J}, Val0Final}),\n      Val1 = (get_v(DP1, I, J - 1) + get_v(DP0, I,\
        \ J - 1)) rem MOD,\n      Val1Final = if J > Limit -> (Val1 - get_v(DP0, I,\
        \ J - Limit - 1) + MOD) rem MOD; true -> Val1 end,\n      ets:insert(DP1, {{I,\
        \ J}, Val1Final})\n    end, lists:seq(1, One))\n  end, lists:seq(1, Zero)),\n\
        \  Result = (get_v(DP0, Zero, One) + get_v(DP1, Zero, One)) rem MOD,\n  ets:delete(DP0),\n\
        \  ets:delete(DP1),\n  Result.\n\nget_v(Table, I, J) ->\n  case ets:lookup(Table,\
        \ {I, J}) of\n    [{_, Val}] -> Val;\n    [] -> 0\n  end."
      elixir: "defmodule Solution do\n  @spec number_of_stable_arrays(zero :: integer,\
        \ one :: integer, limit :: integer) :: integer\n  def number_of_stable_arrays(zero,\
        \ one, limit) do\n    mod = 1_000_000_007\n    dp0 = :ets.new(:dp0, [:set, :private])\n\
        \    dp1 = :ets.new(:dp1, [:set, :private])\n\n    Enum.each(1..min(zero, limit),\
        \ fn i -> :ets.insert(dp0, {{i, 0}, 1}) end)\n    Enum.each(1..min(one, limit),\
        \ fn j -> :ets.insert(dp1, {{0, j}, 1}) end)\n\n    Enum.each(1..zero, fn i\
        \ ->\n      Enum.each(1..one, fn j ->\n        v0 = rem(get_v(dp0, i - 1, j)\
        \ + get_v(dp1, i - 1, j), mod)\n        v0 = if i > limit, do: rem(v0 - get_v(dp1,\
        \ i - limit - 1, j) + mod, mod), else: v0\n        :ets.insert(dp0, {{i, j},\
        \ v0})\n\n        v1 = rem(get_v(dp1, i, j - 1) + get_v(dp0, i, j - 1), mod)\n\
        \        v1 = if j > limit, do: rem(v1 - get_v(dp0, i, j - limit - 1) + mod,\
        \ mod), else: v1\n        :ets.insert(dp1, {{i, j}, v1})\n      end)\n    end)\n\
        \n    res = rem(get_v(dp0, zero, one) + get_v(dp1, zero, one), mod)\n    :ets.delete(dp0)\n\
        \    :ets.delete(dp1)\n    res\n  end\n\n  defp get_v(table, i, j) do\n    case\
        \ :ets.lookup(table, {i, j}) do\n      [{_, val}] -> val\n      [] -> 0\n  \
        \  end\n  end\nend"
    approach: 'The problem asks for the number of stable binary arrays with exactly
      `zero` zeros and `one` ones, such that no consecutive sequence of the same digit
      exceeds `limit`. We use dynamic programming where `dp0[i][j]` represents the number
      of stable arrays with `i` zeros and `j` ones ending in 0, and `dp1[i][j]` represents
      the number of stable arrays ending in 1. An array of `(i, j)` ending in 0 is formed
      by appending a 0 to any stable array of `(i-1, j)`. This append is valid unless
      the resulting array ends in `limit + 1` zeros, which occurs only if the `(i-1,
      j)` array ended in exactly `limit` zeros. The number of such invalid cases is
      exactly `dp1[i-limit-1][j]` because it represents a stable array ending in 1 followed
      by a block of `limit` zeros.


      The recurrence relations are `dp0[i][j] = (dp0[i-1][j] + dp1[i-1][j] - dp1[i-limit-1][j])
      % MOD` and `dp1[i][j] = (dp0[i][j-1] + dp1[i][j-1] - dp0[i][j-limit-1]) % MOD`.
      We handle base cases where `j=0` or `i=0` by initializing `dp0[i][0] = 1` for
      `1 <= i <= limit` and `dp1[0][j] = 1` for `1 <= j <= limit`. To make the recurrence
      work correctly for the first transitions, we also set `dp0[0][0] = 1` and `dp1[0][0]
      = 1`. This approach effectively uses a sliding window (or prefix sum) logic to
      maintain the constraints on consecutive digits efficiently.'
    time_complexity: O(zero * one) since we fill two 2D DP tables of size (zero + 1)
      by (one + 1), and each state is computed in constant time using the derived recurrence
      relations.
    space_complexity: O(zero * one) to store the DP tables. While it is possible to
      optimize this to O(one) or O(zero) by storing only necessary previous rows or
      columns, the given constraints allow for a full 2D representation.
    elapsed_time: 357.39085817337036
    model: gemini-3-flash-preview
    generated_at: '2026-03-10 01:24:35 '
---

## Problem #3130: Find All Possible Stable Binary Arrays II

**Difficulty:** Hard

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

<p>The two possible stable binary arrays are <code>[1,0]</code> and <code>[0,1]</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">zero = 1, one = 2, limit = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>The only possible stable binary array is <code>[1,0,1]</code>.</p>
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
	<li><code>1 &lt;= zero, one, limit &lt;= 1000</code></li>
</ul>


## Hints

1. Let `dp[x][y][z = 0/1]` be the number of stable arrays with exactly `x` zeros, `y` ones, and the last element is `z`. (0 or 1).
`dp[x][y][0] + dp[x][y][1]` is the answer for given `(x, y)`.

2. If we have already placed `x` 1 and `y` 0, if we place a group of `k` 0, the number of ways is `dp[x-k][y][1]`. We can place a group with size `i`, where `i` varies from 1 to `min(limit, zero - x)`.
Similarly, we can solve by placing a group of ones.

3. Speed up the calculation using prefix arrays to store the sum of `dp` states.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the number of stable binary arrays with exactly `zero` zeros and `one` ones, such that no consecutive sequence of the same digit exceeds `limit`. We use dynamic programming where `dp0[i][j]` represents the number of stable arrays with `i` zeros and `j` ones ending in 0, and `dp1[i][j]` represents the number of stable arrays ending in 1. An array of `(i, j)` ending in 0 is formed by appending a 0 to any stable array of `(i-1, j)`. This append is valid unless the resulting array ends in `limit + 1` zeros, which occurs only if the `(i-1, j)` array ended in exactly `limit` zeros. The number of such invalid cases is exactly `dp1[i-limit-1][j]` because it represents a stable array ending in 1 followed by a block of `limit` zeros.

The recurrence relations are `dp0[i][j] = (dp0[i-1][j] + dp1[i-1][j] - dp1[i-limit-1][j]) % MOD` and `dp1[i][j] = (dp0[i][j-1] + dp1[i][j-1] - dp0[i][j-limit-1]) % MOD`. We handle base cases where `j=0` or `i=0` by initializing `dp0[i][0] = 1` for `1 <= i <= limit` and `dp1[0][j] = 1` for `1 <= j <= limit`. To make the recurrence work correctly for the first transitions, we also set `dp0[0][0] = 1` and `dp1[0][0] = 1`. This approach effectively uses a sliding window (or prefix sum) logic to maintain the constraints on consecutive digits efficiently.

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
        vector<vector<int>> dp0(zero + 1, vector<int>(one + 1, 0));
        vector<vector<int>> dp1(zero + 1, vector<int>(one + 1, 0));

        for (int i = 0; i <= min(zero, limit); ++i) dp0[i][0] = 1;
        for (int j = 0; j <= min(one, limit); ++j) dp1[0][j] = 1;

        for (int i = 1; i <= zero; ++i) {
            for (int j = 1; j <= one; ++j) {
                dp0[i][j] = (dp0[i - 1][j] + dp1[i - 1][j]) % MOD;
                if (i > limit) {
                    dp0[i][j] = (dp0[i][j] - dp1[i - limit - 1][j] + MOD) % MOD;
                }
                dp1[i][j] = (dp0[i][j - 1] + dp1[i][j - 1]) % MOD;
                if (j > limit) {
                    dp1[i][j] = (dp1[i][j] - dp0[i][j - limit - 1] + MOD) % MOD;
                }
            }
        }
        return (dp0[zero][one] + dp1[zero][one]) % MOD;
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
        int[][] dp0 = new int[zero + 1][one + 1];
        int[][] dp1 = new int[zero + 1][one + 1];

        for (int i = 0; i <= Math.min(zero, limit); i++) dp0[i][0] = 1;
        for (int j = 0; j <= Math.min(one, limit); j++) dp1[0][j] = 1;

        for (int i = 1; i <= zero; i++) {
            for (int j = 1; j <= one; j++) {
                dp0[i][j] = (int) ((dp0[i - 1][j] + (long) dp1[i - 1][j]) % MOD);
                if (i > limit) {
                    dp0[i][j] = (int) ((dp0[i][j] - (long) dp1[i - limit - 1][j] + MOD) % MOD);
                }
                dp1[i][j] = (int) ((dp0[i][j - 1] + (long) dp1[i][j - 1]) % MOD);
                if (j > limit) {
                    dp1[i][j] = (int) ((dp1[i][j] - (long) dp0[i][j - limit - 1] + MOD) % MOD);
                }
            }
        }
        return (int) ((dp0[zero][one] + (long) dp1[zero][one]) % MOD);
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
        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]

        for i in range(min(zero, limit) + 1):
            dp0[i][0] = 1
        for j in range(min(one, limit) + 1):
            dp1[0][j] = 1

        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                dp0[i][j] = (dp0[i - 1][j] + dp1[i - 1][j]) % MOD
                if i > limit:
                    dp0[i][j] = (dp0[i][j] - dp1[i - limit - 1][j] + MOD) % MOD

                dp1[i][j] = (dp0[i][j - 1] + dp1[i][j - 1]) % MOD
                if j > limit:
                    dp1[i][j] = (dp1[i][j] - dp0[i][j - limit - 1] + MOD) % MOD

        return (dp0[zero][one] + dp1[zero][one]) % MOD
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]

        for i in range(min(zero, limit) + 1):
            dp0[i][0] = 1
        for j in range(min(one, limit) + 1):
            dp1[0][j] = 1

        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                dp0[i][j] = (dp0[i - 1][j] + dp1[i - 1][j]) % MOD
                if i > limit:
                    dp0[i][j] = (dp0[i][j] - dp1[i - limit - 1][j] + MOD) % MOD

                dp1[i][j] = (dp0[i][j - 1] + dp1[i][j - 1]) % MOD
                if j > limit:
                    dp1[i][j] = (dp1[i][j] - dp0[i][j - limit - 1] + MOD) % MOD

        return (dp0[zero][one] + dp1[zero][one]) % MOD
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int numberOfStableArrays(int zero, int one, int limit) {
    int MOD = 1000000007;
    int (*dp0)[one + 1] = calloc(zero + 1, sizeof(*dp0));
    int (*dp1)[one + 1] = calloc(zero + 1, sizeof(*dp1));

    for (int i = 0; i <= (zero < limit ? zero : limit); i++) dp0[i][0] = 1;
    for (int j = 0; j <= (one < limit ? one : limit); j++) dp1[0][j] = 1;

    for (int i = 1; i <= zero; i++) {
        for (int j = 1; j <= one; j++) {
            dp0[i][j] = (dp0[i - 1][j] + dp1[i - 1][j]) % MOD;
            if (i > limit) {
                dp0[i][j] = (dp0[i][j] - dp1[i - limit - 1][j] + MOD) % MOD;
            }
            dp1[i][j] = (dp0[i][j - 1] + dp1[i][j - 1]) % MOD;
            if (j > limit) {
                dp1[i][j] = (dp1[i][j] - dp0[i][j - limit - 1] + MOD) % MOD;
            }
        }
    }

    int result = (dp0[zero][one] + dp1[zero][one]) % MOD;
    free(dp0);
    free(dp1);
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int NumberOfStableArrays(int zero, int one, int limit) {
        long MOD = 1_000_000_007;
        int[,] dp0 = new int[zero + 1, one + 1];
        int[,] dp1 = new int[zero + 1, one + 1];

        for (int i = 0; i <= Math.Min(zero, limit); i++) dp0[i, 0] = 1;
        for (int j = 0; j <= Math.Min(one, limit); j++) dp1[0, j] = 1;

        for (int i = 1; i <= zero; i++) {
            for (int j = 1; j <= one; j++) {
                dp0[i, j] = (int)((dp0[i - 1, j] + (long)dp1[i - 1, j]) % MOD);
                if (i > limit) {
                    dp0[i, j] = (int)((dp0[i, j] - (long)dp1[i - limit - 1, j] + MOD) % MOD);
                }
                dp1[i, j] = (int)((dp0[i, j - 1] + (long)dp1[i, j - 1]) % MOD);
                if (j > limit) {
                    dp1[i, j] = (int)((dp1[i, j] - (long)dp0[i, j - limit - 1] + MOD) % MOD);
                }
            }
        }
        return (int)((dp0[zero, one] + (long)dp1[zero, one]) % MOD);
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
    const dp0 = new Int32Array((zero + 1) * (one + 1));
    const dp1 = new Int32Array((zero + 1) * (one + 1));

    const getIdx = (i, j) => i * (one + 1) + j;

    for (let i = 0; i <= Math.min(zero, limit); i++) dp0[getIdx(i, 0)] = 1;
    for (let j = 0; j <= Math.min(one, limit); j++) dp1[getIdx(0, j)] = 1;

    for (let i = 1; i <= zero; i++) {
        for (let j = 1; j <= one; j++) {
            let idx = getIdx(i, j);
            dp0[idx] = (dp0[getIdx(i - 1, j)] + dp1[getIdx(i - 1, j)]) % MOD;
            if (i > limit) {
                dp0[idx] = (dp0[idx] - dp1[getIdx(i - limit - 1, j)] + MOD) % MOD;
            }
            dp1[idx] = (dp0[getIdx(i, j - 1)] + dp1[getIdx(i, j - 1)]) % MOD;
            if (j > limit) {
                dp1[idx] = (dp1[idx] - dp0[getIdx(i, j - limit - 1)] + MOD) % MOD;
            }
        }
    }
    return (dp0[getIdx(zero, one)] + dp1[getIdx(zero, one)]) % MOD;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function numberOfStableArrays(zero: number, one: number, limit: number): number {
    const MOD = 1000000007;
    const dp0 = Array.from({ length: zero + 1 }, () => new Int32Array(one + 1));
    const dp1 = Array.from({ length: zero + 1 }, () => new Int32Array(one + 1));
    for (let i = 1; i <= zero && i <= limit; i++) dp0[i][0] = 1;
    for (let j = 1; j <= one && j <= limit; j++) dp1[0][j] = 1;
    for (let i = 1; i <= zero; i++) {
        for (let j = 1; j <= one; j++) {
            dp0[i][j] = (dp0[i - 1][j] + dp1[i - 1][j]) % MOD;
            if (i > limit) {
                dp0[i][j] = (dp0[i][j] - dp1[i - limit - 1][j] + MOD) % MOD;
            }
            dp1[i][j] = (dp0[i][j - 1] + dp1[i][j - 1]) % MOD;
            if (j > limit) {
                dp1[i][j] = (dp1[i][j] - dp0[i][j - limit - 1] + MOD) % MOD;
            }
        }
    }
    return (dp0[zero][one] + dp1[zero][one]) % MOD;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function numberOfStableArrays($zero, $one, $limit) {
        $MOD = 1000000007;
        $dp0 = array_fill(0, $zero + 1, array_fill(0, $one + 1, 0));
        $dp1 = array_fill(0, $zero + 1, array_fill(0, $one + 1, 0));
        for ($i = 1; $i <= min($zero, $limit); $i++) {
            $dp0[$i][0] = 1;
        }
        for ($j = 1; $j <= min($one, $limit); $j++) {
            $dp1[0][$j] = 1;
        }
        for ($i = 1; $i <= $zero; $i++) {
            for ($j = 1; $j <= $one; $j++) {
                $dp0[$i][$j] = ($dp0[$i - 1][$j] + $dp1[$i - 1][$j]) % $MOD;
                if ($i > $limit) {
                    $dp0[$i][$j] = ($dp0[$i][$j] - $dp1[$i - $limit - 1][$j] + $MOD) % $MOD;
                }
                $dp1[$i][$j] = ($dp0[$i][$j - 1] + $dp1[$i][$j - 1]) % $MOD;
                if ($j > $limit) {
                    $dp1[$i][$j] = ($dp1[$i][$j] - $dp0[$i][$j - $limit - 1] + $MOD) % $MOD;
                }
            }
        }
        return ($dp0[$zero][$one] + $dp1[$zero][$one]) % $MOD;
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
        let cols = one + 1
        var dp0 = [Int](repeating: 0, count: (zero + 1) * cols)
        var dp1 = [Int](repeating: 0, count: (zero + 1) * cols)
        for i in 1...min(zero, limit) {
            dp0[i * cols] = 1
        }
        for j in 1...min(one, limit) {
            dp1[j] = 1
        }
        for i in 1...zero {
            for j in 1...one {
                let curr = i * cols + j
                dp0[curr] = (dp0[(i - 1) * cols + j] + dp1[(i - 1) * cols + j]) % MOD
                if i > limit {
                    dp0[curr] = (dp0[curr] - dp1[(i - limit - 1) * cols + j] + MOD) % MOD
                }
                dp1[curr] = (dp0[i * cols + (j - 1)] + dp1[i * cols + (j - 1)]) % MOD
                if j > limit {
                    dp1[curr] = (dp1[curr] - dp0[i * cols + (j - limit - 1)] + MOD) % MOD
                }
            }
        }
        return (dp0[zero * cols + one] + dp1[zero * cols + one]) % MOD
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
        val dp0 = Array(zero + 1) { IntArray(one + 1) }
        val dp1 = Array(zero + 1) { IntArray(one + 1) }
        for (i in 1..if (zero < limit) zero else limit) {
            dp0[i][0] = 1
        }
        for (j in 1..if (one < limit) one else limit) {
            dp1[0][j] = 1
        }
        for (i in 1..zero) {
            for (j in 1..one) {
                dp0[i][j] = (dp0[i - 1][j] + dp1[i - 1][j]) % MOD
                if (i > limit) {
                    dp0[i][j] = (dp0[i][j] - dp1[i - limit - 1][j] + MOD) % MOD
                }
                dp1[i][j] = (dp0[i][j - 1] + dp1[i][j - 1]) % MOD
                if (j > limit) {
                    dp1[i][j] = (dp1[i][j] - dp0[i][j - limit - 1] + MOD) % MOD
                }
            }
        }
        return (dp0[zero][one] + dp1[zero][one]) % MOD
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
    const int mod = 1000000007;
    List<List<int>> dp0 = List.generate(zero + 1, (_) => List.filled(one + 1, 0));
    List<List<int>> dp1 = List.generate(zero + 1, (_) => List.filled(one + 1, 0));
    for (int i = 1; i <= (zero < limit ? zero : limit); i++) {
      dp0[i][0] = 1;
    }
    for (int j = 1; j <= (one < limit ? one : limit); j++) {
      dp1[0][j] = 1;
    }
    for (int i = 1; i <= zero; i++) {
      for (int j = 1; j <= one; j++) {
        dp0[i][j] = (dp0[i - 1][j] + dp1[i - 1][j]) % mod;
        if (i > limit) {
          dp0[i][j] = (dp0[i][j] - dp1[i - limit - 1][j] + mod) % mod;
        }
        dp1[i][j] = (dp0[i][j - 1] + dp1[i][j - 1]) % mod;
        if (j > limit) {
          dp1[i][j] = (dp1[i][j] - dp0[i][j - limit - 1] + mod) % mod;
        }
      }
    }
    return (dp0[zero][one] + dp1[zero][one]) % mod;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func numberOfStableArrays(zero int, one int, limit int) int {
    const mod = 1000000007
    dp0 := make([][]int, zero+1)
    dp1 := make([][]int, zero+1)
    for i := range dp0 {
        dp0[i] = make([]int, one+1)
        dp1[i] = make([]int, one+1)
    }
    for i := 1; i <= zero && i <= limit; i++ {
        dp0[i][0] = 1
    }
    for j := 1; j <= one && j <= limit; j++ {
        dp1[0][j] = 1
    }
    for i := 1; i <= zero; i++ {
        for j := 1; j <= one; j++ {
            dp0[i][j] = (dp0[i-1][j] + dp1[i-1][j]) % mod
            if i > limit {
                dp0[i][j] = (dp0[i][j] - dp1[i-limit-1][j] + mod) % mod
            }
            dp1[i][j] = (dp0[i][j-1] + dp1[i][j-1]) % mod
            if j > limit {
                dp1[i][j] = (dp1[i][j] - dp0[i][j-limit-1] + mod) % mod
            }
        }
    }
    return (dp0[zero][one] + dp1[zero][one]) % mod
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def number_of_stable_arrays(zero, one, limit)
  mod = 1_000_000_007
  dp0 = Array.new(zero + 1) { Array.new(one + 1, 0) }
  dp1 = Array.new(zero + 1) { Array.new(one + 1, 0) }

  [zero, limit].min.times { |i| dp0[i + 1][0] = 1 }
  [one, limit].min.times { |j| dp1[0][j + 1] = 1 }

  (1..zero).each do |i|
    (1..one).each do |j|
      v0 = (dp0[i - 1][j] + dp1[i - 1][j]) % mod
      v0 = (v0 - dp1[i - limit - 1][j] + mod) % mod if i > limit
      dp0[i][j] = v0

      v1 = (dp1[i][j - 1] + dp0[i][j - 1]) % mod
      v1 = (v1 - dp0[i][j - limit - 1] + mod) % mod if j > limit
      dp1[i][j] = v1
    end
  end

  (dp0[zero][one] + dp1[zero][one]) % mod
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def numberOfStableArrays(zero: Int, one: Int, limit: Int): Int = {
        val mod = 1000000007
        val dp0 = Array.ofDim[Int](zero + 1, one + 1)
        val dp1 = Array.ofDim[Int](zero + 1, one + 1)

        for (i <- 1 to math.min(zero, limit)) dp0(i)(0) = 1
        for (j <- 1 to math.min(one, limit)) dp1(0)(j) = 1

        for (i <- 1 to zero) {
            for (j <- 1 to one) {
                var v0 = (dp0(i - 1)(j).toLong + dp1(i - 1)(j).toLong) % mod
                if (i > limit) v0 = (v0 - dp1(i - limit - 1)(j) + mod) % mod
                dp0(i)(j) = v0.toInt

                var v1 = (dp1(i)(j - 1).toLong + dp0(i)(j - 1).toLong) % mod
                if (j > limit) v1 = (v1 - dp0(i)(j - limit - 1) + mod) % mod
                dp1(i)(j) = v1.toInt
            }
        }

        ((dp0(zero)(one).toLong + dp1(zero)(one).toLong) % mod).toInt
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
        let zero = zero as usize;
        let one = one as usize;
        let limit = limit as usize;
        let m = 1_000_000_007i64;
        let mut dp0 = vec![vec![0i64; one + 1]; zero + 1];
        let mut dp1 = vec![vec![0i64; one + 1]; zero + 1];

        for i in 1..=std::cmp::min(zero, limit) {
            dp0[i][0] = 1;
        }
        for j in 1..=std::cmp::min(one, limit) {
            dp1[0][j] = 1;
        }

        for i in 1..=zero {
            for j in 1..=one {
                let mut v0 = (dp0[i - 1][j] + dp1[i - 1][j]) % m;
                if i > limit {
                    v0 = (v0 - dp1[i - limit - 1][j] + m) % m;
                }
                dp0[i][j] = v0;

                let mut v1 = (dp1[i][j - 1] + dp0[i][j - 1]) % m;
                if j > limit {
                    v1 = (v1 - dp0[i][j - limit - 1] + m) % m;
                }
                dp1[i][j] = v1;
            }
        }

        ((dp0[zero][one] + dp1[zero][one]) % m) as i32
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
  (let* ([mod 1000000007]
         [dp0 (make-vector (+ zero 1))]
         [dp1 (make-vector (+ zero 1))])
    (for ([i (in-range (+ zero 1))])
      (vector-set! dp0 i (make-vector (+ one 1) 0))
      (vector-set! dp1 i (make-vector (+ one 1) 0)))
    (for ([i (in-range 1 (+ (min zero limit) 1))])
      (vector-set! (vector-ref dp0 i) 0 1))
    (for ([j (in-range 1 (+ (min one limit) 1))])
      (vector-set! (vector-ref dp1 0) j 1))
    (for ([i (in-range 1 (+ zero 1))])
      (let ([dp0-i (vector-ref dp0 i)]
            [dp1-i (vector-ref dp1 i)]
            [dp0-i-1 (vector-ref dp0 (- i 1))]
            [dp1-i-1 (vector-ref dp1 (- i 1))])
        (for ([j (in-range 1 (+ one 1))])
          (let* ([v0 (modulo (+ (vector-ref dp0-i-1 j) (vector-ref dp1-i-1 j)) mod)]
                 [v0 (if (> i limit)
                         (modulo (- v0 (vector-ref (vector-ref dp1 (- i limit 1)) j)) mod)
                         v0)]
                 [v1 (modulo (+ (vector-ref dp1-i (- j 1)) (vector-ref dp0-i (- j 1))) mod)]
                 [v1 (if (> j limit)
                         (modulo (- v1 (vector-ref dp0-i (- j limit 1))) mod)
                         v1)])
            (vector-set! dp0-i j v0)
            (vector-set! dp1-i j v1)))))
    (modulo (+ (vector-ref (vector-ref dp0 zero) one)
               (vector-ref (vector-ref dp1 zero) one))
            mod)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec number_of_stable_arrays(Zero :: integer(), One :: integer(), Limit :: integer()) -> integer().
number_of_stable_arrays(Zero, One, Limit) ->
  MOD = 1000000007,
  DP0 = ets:new(dp0, [set, private]),
  DP1 = ets:new(dp1, [set, private]),
  lists:foreach(fun(I) -> ets:insert(DP0, {{I, 0}, 1}) end, lists:seq(1, min(Zero, Limit))),
  lists:foreach(fun(J) -> ets:insert(DP1, {{0, J}, 1}) end, lists:seq(1, min(One, Limit))),
  lists:foreach(fun(I) ->
    lists:foreach(fun(J) ->
      Val0 = (get_v(DP0, I - 1, J) + get_v(DP1, I - 1, J)) rem MOD,
      Val0Final = if I > Limit -> (Val0 - get_v(DP1, I - Limit - 1, J) + MOD) rem MOD; true -> Val0 end,
      ets:insert(DP0, {{I, J}, Val0Final}),
      Val1 = (get_v(DP1, I, J - 1) + get_v(DP0, I, J - 1)) rem MOD,
      Val1Final = if J > Limit -> (Val1 - get_v(DP0, I, J - Limit - 1) + MOD) rem MOD; true -> Val1 end,
      ets:insert(DP1, {{I, J}, Val1Final})
    end, lists:seq(1, One))
  end, lists:seq(1, Zero)),
  Result = (get_v(DP0, Zero, One) + get_v(DP1, Zero, One)) rem MOD,
  ets:delete(DP0),
  ets:delete(DP1),
  Result.

get_v(Table, I, J) ->
  case ets:lookup(Table, {I, J}) of
    [{_, Val}] -> Val;
    [] -> 0
  end.
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
    dp0 = :ets.new(:dp0, [:set, :private])
    dp1 = :ets.new(:dp1, [:set, :private])

    Enum.each(1..min(zero, limit), fn i -> :ets.insert(dp0, {{i, 0}, 1}) end)
    Enum.each(1..min(one, limit), fn j -> :ets.insert(dp1, {{0, j}, 1}) end)

    Enum.each(1..zero, fn i ->
      Enum.each(1..one, fn j ->
        v0 = rem(get_v(dp0, i - 1, j) + get_v(dp1, i - 1, j), mod)
        v0 = if i > limit, do: rem(v0 - get_v(dp1, i - limit - 1, j) + mod, mod), else: v0
        :ets.insert(dp0, {{i, j}, v0})

        v1 = rem(get_v(dp1, i, j - 1) + get_v(dp0, i, j - 1), mod)
        v1 = if j > limit, do: rem(v1 - get_v(dp0, i, j - limit - 1) + mod, mod), else: v1
        :ets.insert(dp1, {{i, j}, v1})
      end)
    end)

    res = rem(get_v(dp0, zero, one) + get_v(dp1, zero, one), mod)
    :ets.delete(dp0)
    :ets.delete(dp1)
    res
  end

  defp get_v(table, i, j) do
    case :ets.lookup(table, {i, j}) do
      [{_, val}] -> val
      [] -> 0
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(zero * one) since we fill two 2D DP tables of size (zero + 1) by (one + 1), and each state is computed in constant time using the derived recurrence relations.
- **Space Complexity:** O(zero * one) to store the DP tables. While it is possible to optimize this to O(one) or O(zero) by storing only necessary previous rows or columns, the given constraints allow for a full 2D representation.
