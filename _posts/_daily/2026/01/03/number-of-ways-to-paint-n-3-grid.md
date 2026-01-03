---
layout: post
title: "Number of Ways to Paint N × 3 Grid"
date: 2026-01-03 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Dynamic Programming"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int numOfWays(int n) {\n        long long\
        \ MOD = 1e9 + 7;\n\n        long long aba_count = 6; // Patterns like RGR\n\
        \        long long abc_count = 6; // Patterns like RYG\n\n        for (int i\
        \ = 2; i <= n; ++i) {\n            long long new_aba_count = (3 * aba_count\
        \ + 2 * abc_count) % MOD;\n            long long new_abc_count = (2 * aba_count\
        \ + 2 * abc_count) % MOD;\n\n            aba_count = new_aba_count;\n      \
        \      abc_count = new_abc_count;\n        }\n\n        return (aba_count +\
        \ abc_count) % MOD;\n    }\n};"
      java: "class Solution {\n    public int numOfWays(int n) {\n        long MOD =\
        \ 1_000_000_007;\n\n        long abaCount = 6; // Patterns like RGR\n      \
        \  long abcCount = 6; // Patterns like RYG\n\n        for (int i = 2; i <= n;\
        \ ++i) {\n            long newAbaCount = (3 * abaCount + 2 * abcCount) % MOD;\n\
        \            long newAbcCount = (2 * abaCount + 2 * abcCount) % MOD;\n\n   \
        \         abaCount = newAbaCount;\n            abcCount = newAbcCount;\n   \
        \     }\n\n        return (int)((abaCount + abcCount) % MOD);\n    }\n}"
      python: "class Solution:\n    def numOfWays(self, n: int) -> int:\n        MOD\
        \ = 10**9 + 7\n\n        # For n=1, there are 12 ways.\n        # 6 ways for\
        \ patterns like RGR (ABA type)\n        # 6 ways for patterns like RYG (ABC\
        \ type)\n\n        # dp_aba[i] = number of ways to paint i rows, with the i-th\
        \ row being an ABA pattern\n        # dp_abc[i] = number of ways to paint i\
        \ rows, with the i-th row being an ABC pattern\n\n        # Base case for n=1\n\
        \        aba_count = 6 \n        abc_count = 6 \n\n        for _ in range(2,\
        \ n + 1):\n            # If previous row was ABA (e.g., RGR):\n            #\
        \ Next row can be ABA in 3 ways\n            # Next row can be ABC in 2 ways\n\
        \n            # If previous row was ABC (e.g., RYG):\n            # Next row\
        \ can be ABA in 2 ways\n            # Next row can be ABC in 2 ways\n\n    \
        \        new_aba_count = (3 * aba_count + 2 * abc_count) % MOD\n           \
        \ new_abc_count = (2 * aba_count + 2 * abc_count) % MOD\n\n            aba_count\
        \ = new_aba_count\n            abc_count = new_abc_count\n\n        return (aba_count\
        \ + abc_count) % MOD"
      python3: "class Solution:\n    def numOfWays(self, n: int) -> int:\n        MOD\
        \ = 10**9 + 7\n\n        # For n=1, there are 12 ways.\n        # 6 ways for\
        \ patterns like RGR (ABA type)\n        # 6 ways for patterns like RYG (ABC\
        \ type)\n\n        # dp_aba[i] = number of ways to paint i rows, with the i-th\
        \ row being an ABA pattern\n        # dp_abc[i] = number of ways to paint i\
        \ rows, with the i-th row being an ABC pattern\n\n        # Base case for n=1\n\
        \        aba_count = 6 \n        abc_count = 6 \n\n        for _ in range(2,\
        \ n + 1):\n            # If previous row was ABA (e.g., RGR):\n            #\
        \ Next row can be ABA in 3 ways\n            # Next row can be ABC in 2 ways\n\
        \n            # If previous row was ABC (e.g., RYG):\n            # Next row\
        \ can be ABA in 2 ways\n            # Next row can be ABC in 2 ways\n\n    \
        \        new_aba_count = (3 * aba_count + 2 * abc_count) % MOD\n           \
        \ new_abc_count = (2 * aba_count + 2 * abc_count) % MOD\n\n            aba_count\
        \ = new_aba_count\n            abc_count = new_abc_count\n\n        return (aba_count\
        \ + abc_count) % MOD"
      c: "int numOfWays(int n) {\n    long long MOD = 1000000007;\n\n    long long aba_count\
        \ = 6; // Patterns like RGR\n    long long abc_count = 6; // Patterns like RYG\n\
        \n    for (int i = 2; i <= n; ++i) {\n        long long new_aba_count = (3 *\
        \ aba_count + 2 * abc_count) % MOD;\n        long long new_abc_count = (2 *\
        \ aba_count + 2 * abc_count) % MOD;\n\n        aba_count = new_aba_count;\n\
        \        abc_count = new_abc_count;\n    }\n\n    return (int)((aba_count +\
        \ abc_count) % MOD);\n}"
      csharp: "public class Solution {\n    public int NumOfWays(int n) {\n        long\
        \ MOD = 1_000_000_007;\n\n        long abaCount = 6; // Patterns like RGR\n\
        \        long abcCount = 6; // Patterns like RYG\n\n        for (int i = 2;\
        \ i <= n; ++i) {\n            long newAbaCount = (3 * abaCount + 2 * abcCount)\
        \ % MOD;\n            long newAbcCount = (2 * abaCount + 2 * abcCount) % MOD;\n\
        \n            abaCount = newAbaCount;\n            abcCount = newAbcCount;\n\
        \        }\n\n        return (int)((abaCount + abcCount) % MOD);\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @return {number}\n */\nvar numOfWays\
        \ = function(n) {\n    const MOD = 1_000_000_007;\n\n    let abaCount = 6; //\
        \ Patterns like RGR\n    let abcCount = 6; // Patterns like RYG\n\n    for (let\
        \ i = 2; i <= n; ++i) {\n        let newAbaCount = (3 * abaCount + 2 * abcCount)\
        \ % MOD;\n        let newAbcCount = (2 * abaCount + 2 * abcCount) % MOD;\n\n\
        \        abaCount = newAbaCount;\n        abcCount = newAbcCount;\n    }\n\n\
        \    return (abaCount + abcCount) % MOD;\n};"
      typescript: "function numOfWays(n: number): number {\n    const MOD = 1_000_000_007;\n\
        \n    let abaCount: number = 6; // Patterns like RGR\n    let abcCount: number\
        \ = 6; // Patterns like RYG\n\n    for (let i = 2; i <= n; ++i) {\n        let\
        \ newAbaCount: number = (3 * abaCount + 2 * abcCount) % MOD;\n        let newAbcCount:\
        \ number = (2 * abaCount + 2 * abcCount) % MOD;\n\n        abaCount = newAbaCount;\n\
        \        abcCount = newAbcCount;\n    }\n\n    return (abaCount + abcCount)\
        \ % MOD;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @return Integer\n\
        \     */\n    function numOfWays($n) {\n        $MOD = 1_000_000_007;\n\n  \
        \      $abaCount = 6; // Patterns like RGR\n        $abcCount = 6; // Patterns\
        \ like RYG\n\n        for ($i = 2; $i <= $n; ++$i) {\n            $newAbaCount\
        \ = (3 * $abaCount + 2 * $abcCount) % $MOD;\n            $newAbcCount = (2 *\
        \ $abaCount + 2 * $abcCount) % $MOD;\n\n            $abaCount = $newAbaCount;\n\
        \            $abcCount = $newAbcCount;\n        }\n\n        return ($abaCount\
        \ + $abcCount) % $MOD;\n    }\n}"
      swift: "class Solution {\n    func numOfWays(_ n: Int) -> Int {\n        let MOD\
        \ = 1_000_000_007\n\n        var abaCount: Int = 6 // Patterns like RGR\n  \
        \      var abcCount: Int = 6 // Patterns like RYG\n\n        for _ in 2...n\
        \ {\n            let newAbaCount = (3 * abaCount + 2 * abcCount) % MOD\n   \
        \         let newAbcCount = (2 * abaCount + 2 * abcCount) % MOD\n\n        \
        \    abaCount = newAbaCount\n            abcCount = newAbcCount\n        }\n\
        \n        return (abaCount + abcCount) % MOD\n    }\n}"
      kotlin: "class Solution {\n    fun numOfWays(n: Int): Int {\n        val MOD =\
        \ 1_000_000_007L // Use Long for MOD to ensure calculations are done in Long\n\
        \n        var abaCount: Long = 6 // Patterns like RGR\n        var abcCount:\
        \ Long = 6 // Patterns like RYG\n\n        for (i in 2..n) {\n            val\
        \ newAbaCount = (3 * abaCount + 2 * abcCount) % MOD\n            val newAbcCount\
        \ = (2 * abaCount + 2 * abcCount) % MOD\n\n            abaCount = newAbaCount;\n\
        \            abcCount = newAbcCount;\n        }\n\n        return ((abaCount\
        \ + abcCount) % MOD).toInt()\n    }\n}"
      dart: "class Solution {\n  int numOfWays(int n) {\n    final int MOD = 1_000_000_007;\n\
        \n    int abaCount = 6; // Patterns like RGR\n    int abcCount = 6; // Patterns\
        \ like RYG\n\n    for (int i = 2; i <= n; ++i) {\n      int newAbaCount = (3\
        \ * abaCount + 2 * abcCount) % MOD;\n      int newAbcCount = (2 * abaCount +\
        \ 2 * abcCount) % MOD;\n\n      abaCount = newAbaCount;\n      abcCount = newAbcCount;\n\
        \    }\n\n    return (abaCount + abcCount) % MOD;\n  }\n}"
      go: "func numOfWays(n int) int {\n    MOD := 1_000_000_007\n\n    var abaCount\
        \ int64 = 6 // Patterns like RGR\n    var abcCount int64 = 6 // Patterns like\
        \ RYG\n\n    for i := 2; i <= n; i++ {\n        newAbaCount := (3 * abaCount\
        \ + 2 * abcCount) % int64(MOD)\n        newAbcCount := (2 * abaCount + 2 * abcCount)\
        \ % int64(MOD)\n\n        abaCount = newAbaCount\n        abcCount = newAbcCount\n\
        \    }\n\n    return int((abaCount + abcCount) % int64(MOD))\n}"
      ruby: "# @param {Integer} n\n# @return {Integer}\ndef num_of_ways(n)\n    mod\
        \ = 1_000_000_007\n\n    aba_count = 6\n    abc_count = 6\n\n    (2..n).each\
        \ do |p_i|\n        new_aba_count = (3 * aba_count + 2 * abc_count) % mod\n\
        \        new_abc_count = (2 * aba_count + 2 * abc_count) % mod\n\n        aba_count\
        \ = new_aba_count\n        abc_count = new_abc_count\n    end\n\n    (aba_count\
        \ + abc_count) % mod\nend"
      scala: "object Solution {\n    def numOfWays(n: Int): Int = {\n        val MOD:\
        \ Long = 1_000_000_007L\n\n        var abaCount: Long = 6 // Patterns like RGR\n\
        \        var abcCount: Long = 6 // Patterns like RYG\n\n        for (i <- 2\
        \ to n) {\n            val newAbaCount = (3 * abaCount + 2 * abcCount) % MOD\n\
        \            val newAbcCount = (2 * abaCount + 2 * abcCount) % MOD\n\n     \
        \       abaCount = newAbaCount\n            abcCount = newAbcCount\n       \
        \ }\n\n        ((abaCount + abcCount) % MOD).toInt\n    }\n}"
      rust: "impl Solution {\n    pub fn num_of_ways(n: i32) -> i32 {\n        let modulus:\
        \ i64 = 1_000_000_007;\n\n        let mut aba_count: i64 = 6; // Patterns like\
        \ RGR\n        let mut abc_count: i64 = 6; // Patterns like RYG\n\n        for\
        \ _i in 2..=n {\n            let new_aba_count = (3 * aba_count + 2 * abc_count)\
        \ % modulus;\n            let new_abc_count = (2 * aba_count + 2 * abc_count)\
        \ % modulus;\n\n            aba_count = new_aba_count;\n            abc_count\
        \ = new_abc_count;\n        }\n\n        ((aba_count + abc_count) % modulus)\
        \ as i32\n    }\n}"
      racket: "(define/contract (num-of-ways n)\n  (-> exact-integer? exact-integer?)\n\
        \  (let ([MOD 1000000007])\n    (let loop ([i 1] [aba-count 6] [abc-count 6])\n\
        \      (if (= i n)\n          (modulo (+ aba-count abc-count) MOD)\n       \
        \   (let ([new-aba-count (modulo (+ (* 3 aba-count) (* 2 abc-count)) MOD)]\n\
        \                [new-abc-count (modulo (+ (* 2 aba-count) (* 2 abc-count))\
        \ MOD)])\n            (loop (+ i 1) new-aba-count new-abc-count))))))"
      erlang: "-spec num_of_ways(N :: integer()) -> integer().\nnum_of_ways(N) ->\n\
        \    MOD = 1000000007,\n    num_of_ways_loop(N, 1, 6, 6, MOD).\n\nnum_of_ways_loop(N,\
        \ N, AbaCount, AbcCount, MOD) ->\n    (AbaCount + AbcCount) rem MOD;\nnum_of_ways_loop(N,\
        \ I, AbaCount, AbcCount, MOD) ->\n    NewAbaCount = (3 * AbaCount + 2 * AbcCount)\
        \ rem MOD,\n    NewAbcCount = (2 * AbaCount + 2 * AbcCount) rem MOD,\n    num_of_ways_loop(N,\
        \ I + 1, NewAbaCount, NewAbcCount, MOD)."
      elixir: "defmodule Solution do\n  @spec num_of_ways(n :: integer) :: integer\n\
        \  def num_of_ways(n) do\n    mod = 1_000_000_007\n\n    # Base case for n=1\n\
        \    aba_count = 6\n    abc_count = 6\n\n    # Iterate from i=2 to n\n    Enum.reduce(2..n,\
        \ {aba_count, abc_count}, fn _, {current_aba, current_abc} ->\n      new_aba_count\
        \ = (3 * current_aba + 2 * current_abc) |> rem(mod)\n      new_abc_count = (2\
        \ * current_aba + 2 * current_abc) |> rem(mod)\n      {new_aba_count, new_abc_count}\n\
        \    end)\n    |> (fn {final_aba, final_abc} -> (final_aba + final_abc) |> rem(mod)\
        \ end).()\n  end\nend"
    approach: 'The problem asks for the number of ways to paint an n x 3 grid such that
      no two adjacent cells (horizontally or vertically) have the same color. This problem
      can be efficiently solved using dynamic programming due to the localized dependency
      of coloring. The key insight is that the valid colorings for any row i depend
      only on the coloring of the immediately preceding row i-1. We categorize the possible
      color patterns for a single row of three cells into two types: "ABA" patterns
      (e.g., Red-Yellow-Red, where the first and third colors are the same) and "ABC"
      patterns (e.g., Red-Yellow-Green, where all three colors are distinct). There
      are 6 unique "ABA" patterns and 6 unique "ABC" patterns, totaling 12 ways to color
      a single row.


      We define dp_aba[i] as the number of ways to paint i rows such that the i-th row
      ends with an "ABA" pattern, and dp_abc[i] as the number of ways to paint i rows
      such that the i-th row ends with an "ABC" pattern. For the base case n=1, dp_aba[1]
      = 6 and dp_abc[1] = 6. For subsequent rows, we derive recurrence relations by
      analyzing how many valid "ABA" and "ABC" patterns can follow a given "ABA" or
      "ABC" pattern in the previous row. A detailed analysis shows that an "ABA" pattern
      can be followed by 3 "ABA" patterns and 2 "ABC" patterns. Similarly, an "ABC"
      pattern can be followed by 2 "ABA" patterns and 2 "ABC" patterns. This leads to
      the transitions: dp_aba[i] = (3 * dp_aba[i-1] + 2 * dp_abc[i-1]) % MOD and dp_abc[i]
      = (2 * dp_aba[i-1] + 2 * dp_abc[i-1]) % MOD. The final answer is the sum of dp_aba[n]
      and dp_abc[n] modulo 10^9 + 7.'
    time_complexity: The algorithm iterates n-1 times to compute the counts for each
      row from 2 to n. In each iteration, a constant number of arithmetic operations
      (multiplications, additions, and modulo operations) are performed. Therefore,
      the time complexity is O(N).
    space_complexity: The algorithm only needs to store the counts for the previous
      row to compute the current row's counts. This means we only need a constant number
      of variables (two for ABA count and ABC count). Thus, the space complexity is
      O(1).
    elapsed_time: 56.000226736068726
    model: gemini-2.5-flash
    generated_at: '2026-01-03 01:05:42 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int numOfWays(int n) {\n        const int\
        \ MOD = 1e9 + 7;\n        long long dp[5001][3][3][3] = {0};\n        for (int\
        \ i = 0; i < 3; i++) {\n            for (int j = 0; j < 3; j++) {\n        \
        \        for (int k = 0; k < 3; k++) {\n                    if (i != j && j\
        \ != k && k != i) {\n                        dp[1][i][j][k] = 1;\n         \
        \           }\n                }\n            }\n        }\n        for (int\
        \ idx = 2; idx <= n; idx++) {\n            for (int i = 0; i < 3; i++) {\n \
        \               for (int j = 0; j < 3; j++) {\n                    for (int\
        \ k = 0; k < 3; k++) {\n                        if (dp[idx - 1][i][j][k] > 0)\
        \ {\n                            for (int x = 0; x < 3; x++) {\n           \
        \                     for (int y = 0; y < 3; y++) {\n                      \
        \              for (int z = 0; z < 3; z++) {\n                             \
        \           if (x != y && y != z && z != x && x != i && y != j && z != k) {\n\
        \                                            dp[idx][x][y][z] = (dp[idx][x][y][z]\
        \ + dp[idx - 1][i][j][k]) % MOD;\n                                        }\n\
        \                                    }\n                                }\n\
        \                            }\n                        }\n                \
        \    }\n                }\n            }\n        }\n        long long ans =\
        \ 0;\n        for (int i = 0; i < 3; i++) {\n            for (int j = 0; j <\
        \ 3; j++) {\n                for (int k = 0; k < 3; k++) {\n               \
        \     ans = (ans + dp[n][i][j][k]) % MOD;\n                }\n            }\n\
        \        }\n        return ans;\n    }\n};"
      java: "class Solution {\n    public int numOfWays(int n) {\n        final int\
        \ MOD = (int) 1e9 + 7;\n        long[][][][] dp = new long[5001][3][3][3];\n\
        \        for (int i = 0; i < 3; i++) {\n            for (int j = 0; j < 3; j++)\
        \ {\n                for (int k = 0; k < 3; k++) {\n                    if (i\
        \ != j && j != k && k != i) {\n                        dp[1][i][j][k] = 1;\n\
        \                    }\n                }\n            }\n        }\n      \
        \  for (int idx = 2; idx <= n; idx++) {\n            for (int i = 0; i < 3;\
        \ i++) {\n                for (int j = 0; j < 3; j++) {\n                  \
        \  for (int k = 0; k < 3; k++) {\n                        if (dp[idx - 1][i][j][k]\
        \ > 0) {\n                            for (int x = 0; x < 3; x++) {\n      \
        \                          for (int y = 0; y < 3; y++) {\n                 \
        \                   for (int z = 0; z < 3; z++) {\n                        \
        \                if (x != y && y != z && z != x && x != i && y != j && z !=\
        \ k) {\n                                            dp[idx][x][y][z] = (dp[idx][x][y][z]\
        \ + dp[idx - 1][i][j][k]) % MOD;\n                                        }\n\
        \                                    }\n                                }\n\
        \                            }\n                        }\n                \
        \    }\n                }\n            }\n        }\n        long ans = 0;\n\
        \        for (int i = 0; i < 3; i++) {\n            for (int j = 0; j < 3; j++)\
        \ {\n                for (int k = 0; k < 3; k++) {\n                    ans\
        \ = (ans + dp[n][i][j][k]) % MOD;\n                }\n            }\n      \
        \  }\n        return (int) ans;\n    }\n}"
      python: "class Solution:\n    def numOfWays(self, n: int) -> int:\n        MOD\
        \ = 10**9 + 7\n        dp = [[[0 for _ in range(3)] for _ in range(3)] for _\
        \ in range(3)]\n        for i in range(3):\n            for j in range(3):\n\
        \                for k in range(3):\n                    if i != j and j !=\
        \ k and k != i:\n                        dp[i][j][k] = 1\n        for idx in\
        \ range(2, n + 1):\n            new_dp = [[[0 for _ in range(3)] for _ in range(3)]\
        \ for _ in range(3)]\n            for i in range(3):\n                for j\
        \ in range(3):\n                    for k in range(3):\n                   \
        \     if dp[i][j][k] > 0:\n                            for x in range(3):\n\
        \                                for y in range(3):\n                      \
        \              for z in range(3):\n                                        if\
        \ x != y and y != z and z != x and x != i and y != j and z != k:\n         \
        \                                   new_dp[x][y][z] = (new_dp[x][y][z] + dp[i][j][k])\
        \ % MOD\n            dp = new_dp\n        ans = 0\n        for i in range(3):\n\
        \            for j in range(3):\n                for k in range(3):\n      \
        \              ans = (ans + dp[i][j][k]) % MOD\n        return ans"
      python3: "class Solution:\n    def numOfWays(self, n: int) -> int:\n        MOD\
        \ = 10**9 + 7\n        dp = [[[0 for _ in range(3)] for _ in range(3)] for _\
        \ in range(3)]\n        for i in range(3):\n            for j in range(3):\n\
        \                for k in range(3):\n                    if i != j and j !=\
        \ k and k != i:\n                        dp[i][j][k] = 1\n        for idx in\
        \ range(2, n + 1):\n            new_dp = [[[0 for _ in range(3)] for _ in range(3)]\
        \ for _ in range(3)]\n            for i in range(3):\n                for j\
        \ in range(3):\n                    for k in range(3):\n                   \
        \     if dp[i][j][k] > 0:\n                            for x in range(3):\n\
        \                                for y in range(3):\n                      \
        \              for z in range(3):\n                                        if\
        \ x != y and y != z and z != x and x != i and y != j and z != k:\n         \
        \                                   new_dp[x][y][z] = (new_dp[x][y][z] + dp[i][j][k])\
        \ % MOD\n            dp = new_dp\n        ans = 0\n        for i in range(3):\n\
        \            for j in range(3):\n                for k in range(3):\n      \
        \              ans = (ans + dp[i][j][k]) % MOD\n        return ans"
      c: Not implemented
      csharp: Not implemented
      javascript: Not implemented
      typescript: Not implemented
      php: Not implemented
      swift: Not implemented
      kotlin: Not implemented
      dart: Not implemented
      go: Not implemented
      ruby: Not implemented
      scala: Not implemented
      rust: Not implemented
      racket: Not implemented
      erlang: Not implemented
      elixir: Not implemented
    approach: The problem can be solved using dynamic programming. We define a 4D DP
      array dp[idx][prev1col][prev2col][prev3col] where dp[idx][prev1col][prev2col][prev3col]
      represents the number of ways to color the rows of the grid from idx to n-1, given
      that the previous row (idx - 1) has colors prev1col, prev2col, and prev3col. We
      iterate over all possible colors for the current row and update the DP array accordingly.
      The base case is when idx equals n, in which case there is only one way to color
      the grid (i.e., no more rows to color). The final answer is the sum of dp[1][i][j][k]
      for all possible i, j, and k, which represents the number of ways to color the
      entire grid.
    time_complexity: O(n * 3^4) because we have n rows and for each row, we have 3 choices
      for each of the 3 columns, resulting in 3^3 possibilities for the current row
      and 3 possibilities for the previous row.
    space_complexity: O(n * 3^3) because we need to store the DP array of size n * 3
      * 3 * 3.
    elapsed_time: 3.735126256942749
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-03 01:05:46 '
---

## Problem #1411: Number of Ways to Paint N × 3 Grid

**Difficulty:** Hard

**Topics:** Dynamic Programming

## Problem Description

<p>You have a <code>grid</code> of size <code>n x 3</code> and you want to paint each cell of the grid with exactly one of the three colors: <strong>Red</strong>, <strong>Yellow,</strong> or <strong>Green</strong> while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).</p>

<p>Given <code>n</code> the number of rows of the grid, return <em>the number of ways</em> you can paint this <code>grid</code>. As the answer may grow large, the answer <strong>must be</strong> computed modulo <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/03/26/e1.png" style="width: 400px; height: 257px;" />
<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 12
<strong>Explanation:</strong> There are 12 possible way to paint the grid as shown.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 5000
<strong>Output:</strong> 30228214
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == grid.length</code></li>
	<li><code>1 &lt;= n &lt;= 5000</code></li>
</ul>


## Hints

1. We will use Dynamic programming approach. we will try all possible configuration.

2. Let dp[idx][prev1col][prev2col][prev3col] be the number of ways to color the rows of the grid from idx to n-1 keeping in mind that the previous row (idx - 1) has colors prev1col, prev2col and prev3col. Build the dp array to get the answer.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2026-01-03 01:05:42 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks for the number of ways to paint an n x 3 grid such that no two adjacent cells (horizontally or vertically) have the same color. This problem can be efficiently solved using dynamic programming due to the localized dependency of coloring. The key insight is that the valid colorings for any row i depend only on the coloring of the immediately preceding row i-1. We categorize the possible color patterns for a single row of three cells into two types: "ABA" patterns (e.g., Red-Yellow-Red, where the first and third colors are the same) and "ABC" patterns (e.g., Red-Yellow-Green, where all three colors are distinct). There are 6 unique "ABA" patterns and 6 unique "ABC" patterns, totaling 12 ways to color a single row.

We define dp_aba[i] as the number of ways to paint i rows such that the i-th row ends with an "ABA" pattern, and dp_abc[i] as the number of ways to paint i rows such that the i-th row ends with an "ABC" pattern. For the base case n=1, dp_aba[1] = 6 and dp_abc[1] = 6. For subsequent rows, we derive recurrence relations by analyzing how many valid "ABA" and "ABC" patterns can follow a given "ABA" or "ABC" pattern in the previous row. A detailed analysis shows that an "ABA" pattern can be followed by 3 "ABA" patterns and 2 "ABC" patterns. Similarly, an "ABC" pattern can be followed by 2 "ABA" patterns and 2 "ABC" patterns. This leads to the transitions: dp_aba[i] = (3 * dp_aba[i-1] + 2 * dp_abc[i-1]) % MOD and dp_abc[i] = (2 * dp_aba[i-1] + 2 * dp_abc[i-1]) % MOD. The final answer is the sum of dp_aba[n] and dp_abc[n] modulo 10^9 + 7.

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-cpp-gemini-2-5-flash" checked>
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-java-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python3-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-c-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-csharp-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-javascript-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-typescript-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-php-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-swift-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-kotlin-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-dart-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-go-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-ruby-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-scala-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-rust-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-racket-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-erlang-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-elixir-gemini-2-5-flash">
  <div class="tab-labels">
    <label for="lang-cpp-gemini-2-5-flash">C++</label>
    <label for="lang-java-gemini-2-5-flash">Java</label>
    <label for="lang-python-gemini-2-5-flash">Python</label>
    <label for="lang-python3-gemini-2-5-flash">Python3</label>
    <label for="lang-c-gemini-2-5-flash">C</label>
    <label for="lang-csharp-gemini-2-5-flash">C#</label>
    <label for="lang-javascript-gemini-2-5-flash">JavaScript</label>
    <label for="lang-typescript-gemini-2-5-flash">TypeScript</label>
    <label for="lang-php-gemini-2-5-flash">PHP</label>
    <label for="lang-swift-gemini-2-5-flash">Swift</label>
    <label for="lang-kotlin-gemini-2-5-flash">Kotlin</label>
    <label for="lang-dart-gemini-2-5-flash">Dart</label>
    <label for="lang-go-gemini-2-5-flash">Go</label>
    <label for="lang-ruby-gemini-2-5-flash">Ruby</label>
    <label for="lang-scala-gemini-2-5-flash">Scala</label>
    <label for="lang-rust-gemini-2-5-flash">Rust</label>
    <label for="lang-racket-gemini-2-5-flash">Racket</label>
    <label for="lang-erlang-gemini-2-5-flash">Erlang</label>
    <label for="lang-elixir-gemini-2-5-flash">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
class Solution {
public:
    int numOfWays(int n) {
        long long MOD = 1e9 + 7;

        long long aba_count = 6; // Patterns like RGR
        long long abc_count = 6; // Patterns like RYG

        for (int i = 2; i <= n; ++i) {
            long long new_aba_count = (3 * aba_count + 2 * abc_count) % MOD;
            long long new_abc_count = (2 * aba_count + 2 * abc_count) % MOD;

            aba_count = new_aba_count;
            abc_count = new_abc_count;
        }

        return (aba_count + abc_count) % MOD;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int numOfWays(int n) {
        long MOD = 1_000_000_007;

        long abaCount = 6; // Patterns like RGR
        long abcCount = 6; // Patterns like RYG

        for (int i = 2; i <= n; ++i) {
            long newAbaCount = (3 * abaCount + 2 * abcCount) % MOD;
            long newAbcCount = (2 * abaCount + 2 * abcCount) % MOD;

            abaCount = newAbaCount;
            abcCount = newAbcCount;
        }

        return (int)((abaCount + abcCount) % MOD);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        # For n=1, there are 12 ways.
        # 6 ways for patterns like RGR (ABA type)
        # 6 ways for patterns like RYG (ABC type)

        # dp_aba[i] = number of ways to paint i rows, with the i-th row being an ABA pattern
        # dp_abc[i] = number of ways to paint i rows, with the i-th row being an ABC pattern

        # Base case for n=1
        aba_count = 6 
        abc_count = 6 

        for _ in range(2, n + 1):
            # If previous row was ABA (e.g., RGR):
            # Next row can be ABA in 3 ways
            # Next row can be ABC in 2 ways

            # If previous row was ABC (e.g., RYG):
            # Next row can be ABA in 2 ways
            # Next row can be ABC in 2 ways

            new_aba_count = (3 * aba_count + 2 * abc_count) % MOD
            new_abc_count = (2 * aba_count + 2 * abc_count) % MOD

            aba_count = new_aba_count
            abc_count = new_abc_count

        return (aba_count + abc_count) % MOD
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        # For n=1, there are 12 ways.
        # 6 ways for patterns like RGR (ABA type)
        # 6 ways for patterns like RYG (ABC type)

        # dp_aba[i] = number of ways to paint i rows, with the i-th row being an ABA pattern
        # dp_abc[i] = number of ways to paint i rows, with the i-th row being an ABC pattern

        # Base case for n=1
        aba_count = 6 
        abc_count = 6 

        for _ in range(2, n + 1):
            # If previous row was ABA (e.g., RGR):
            # Next row can be ABA in 3 ways
            # Next row can be ABC in 2 ways

            # If previous row was ABC (e.g., RYG):
            # Next row can be ABA in 2 ways
            # Next row can be ABC in 2 ways

            new_aba_count = (3 * aba_count + 2 * abc_count) % MOD
            new_abc_count = (2 * aba_count + 2 * abc_count) % MOD

            aba_count = new_aba_count
            abc_count = new_abc_count

        return (aba_count + abc_count) % MOD
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int numOfWays(int n) {
    long long MOD = 1000000007;

    long long aba_count = 6; // Patterns like RGR
    long long abc_count = 6; // Patterns like RYG

    for (int i = 2; i <= n; ++i) {
        long long new_aba_count = (3 * aba_count + 2 * abc_count) % MOD;
        long long new_abc_count = (2 * aba_count + 2 * abc_count) % MOD;

        aba_count = new_aba_count;
        abc_count = new_abc_count;
    }

    return (int)((aba_count + abc_count) % MOD);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int NumOfWays(int n) {
        long MOD = 1_000_000_007;

        long abaCount = 6; // Patterns like RGR
        long abcCount = 6; // Patterns like RYG

        for (int i = 2; i <= n; ++i) {
            long newAbaCount = (3 * abaCount + 2 * abcCount) % MOD;
            long newAbcCount = (2 * abaCount + 2 * abcCount) % MOD;

            abaCount = newAbaCount;
            abcCount = newAbcCount;
        }

        return (int)((abaCount + abcCount) % MOD);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} n
 * @return {number}
 */
var numOfWays = function(n) {
    const MOD = 1_000_000_007;

    let abaCount = 6; // Patterns like RGR
    let abcCount = 6; // Patterns like RYG

    for (let i = 2; i <= n; ++i) {
        let newAbaCount = (3 * abaCount + 2 * abcCount) % MOD;
        let newAbcCount = (2 * abaCount + 2 * abcCount) % MOD;

        abaCount = newAbaCount;
        abcCount = newAbcCount;
    }

    return (abaCount + abcCount) % MOD;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function numOfWays(n: number): number {
    const MOD = 1_000_000_007;

    let abaCount: number = 6; // Patterns like RGR
    let abcCount: number = 6; // Patterns like RYG

    for (let i = 2; i <= n; ++i) {
        let newAbaCount: number = (3 * abaCount + 2 * abcCount) % MOD;
        let newAbcCount: number = (2 * abaCount + 2 * abcCount) % MOD;

        abaCount = newAbaCount;
        abcCount = newAbcCount;
    }

    return (abaCount + abcCount) % MOD;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function numOfWays($n) {
        $MOD = 1_000_000_007;

        $abaCount = 6; // Patterns like RGR
        $abcCount = 6; // Patterns like RYG

        for ($i = 2; $i <= $n; ++$i) {
            $newAbaCount = (3 * $abaCount + 2 * $abcCount) % $MOD;
            $newAbcCount = (2 * $abaCount + 2 * $abcCount) % $MOD;

            $abaCount = $newAbaCount;
            $abcCount = $newAbcCount;
        }

        return ($abaCount + $abcCount) % $MOD;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func numOfWays(_ n: Int) -> Int {
        let MOD = 1_000_000_007

        var abaCount: Int = 6 // Patterns like RGR
        var abcCount: Int = 6 // Patterns like RYG

        for _ in 2...n {
            let newAbaCount = (3 * abaCount + 2 * abcCount) % MOD
            let newAbcCount = (2 * abaCount + 2 * abcCount) % MOD

            abaCount = newAbaCount
            abcCount = newAbcCount
        }

        return (abaCount + abcCount) % MOD
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun numOfWays(n: Int): Int {
        val MOD = 1_000_000_007L // Use Long for MOD to ensure calculations are done in Long

        var abaCount: Long = 6 // Patterns like RGR
        var abcCount: Long = 6 // Patterns like RYG

        for (i in 2..n) {
            val newAbaCount = (3 * abaCount + 2 * abcCount) % MOD
            val newAbcCount = (2 * abaCount + 2 * abcCount) % MOD

            abaCount = newAbaCount;
            abcCount = newAbcCount;
        }

        return ((abaCount + abcCount) % MOD).toInt()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int numOfWays(int n) {
    final int MOD = 1_000_000_007;

    int abaCount = 6; // Patterns like RGR
    int abcCount = 6; // Patterns like RYG

    for (int i = 2; i <= n; ++i) {
      int newAbaCount = (3 * abaCount + 2 * abcCount) % MOD;
      int newAbcCount = (2 * abaCount + 2 * abcCount) % MOD;

      abaCount = newAbaCount;
      abcCount = newAbcCount;
    }

    return (abaCount + abcCount) % MOD;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func numOfWays(n int) int {
    MOD := 1_000_000_007

    var abaCount int64 = 6 // Patterns like RGR
    var abcCount int64 = 6 // Patterns like RYG

    for i := 2; i <= n; i++ {
        newAbaCount := (3 * abaCount + 2 * abcCount) % int64(MOD)
        newAbcCount := (2 * abaCount + 2 * abcCount) % int64(MOD)

        abaCount = newAbaCount
        abcCount = newAbcCount
    }

    return int((abaCount + abcCount) % int64(MOD))
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} n
# @return {Integer}
def num_of_ways(n)
    mod = 1_000_000_007

    aba_count = 6
    abc_count = 6

    (2..n).each do |p_i|
        new_aba_count = (3 * aba_count + 2 * abc_count) % mod
        new_abc_count = (2 * aba_count + 2 * abc_count) % mod

        aba_count = new_aba_count
        abc_count = new_abc_count
    end

    (aba_count + abc_count) % mod
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def numOfWays(n: Int): Int = {
        val MOD: Long = 1_000_000_007L

        var abaCount: Long = 6 // Patterns like RGR
        var abcCount: Long = 6 // Patterns like RYG

        for (i <- 2 to n) {
            val newAbaCount = (3 * abaCount + 2 * abcCount) % MOD
            val newAbcCount = (2 * abaCount + 2 * abcCount) % MOD

            abaCount = newAbaCount
            abcCount = newAbcCount
        }

        ((abaCount + abcCount) % MOD).toInt
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn num_of_ways(n: i32) -> i32 {
        let modulus: i64 = 1_000_000_007;

        let mut aba_count: i64 = 6; // Patterns like RGR
        let mut abc_count: i64 = 6; // Patterns like RYG

        for _i in 2..=n {
            let new_aba_count = (3 * aba_count + 2 * abc_count) % modulus;
            let new_abc_count = (2 * aba_count + 2 * abc_count) % modulus;

            aba_count = new_aba_count;
            abc_count = new_abc_count;
        }

        ((aba_count + abc_count) % modulus) as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (num-of-ways n)
  (-> exact-integer? exact-integer?)
  (let ([MOD 1000000007])
    (let loop ([i 1] [aba-count 6] [abc-count 6])
      (if (= i n)
          (modulo (+ aba-count abc-count) MOD)
          (let ([new-aba-count (modulo (+ (* 3 aba-count) (* 2 abc-count)) MOD)]
                [new-abc-count (modulo (+ (* 2 aba-count) (* 2 abc-count)) MOD)])
            (loop (+ i 1) new-aba-count new-abc-count))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec num_of_ways(N :: integer()) -> integer().
num_of_ways(N) ->
    MOD = 1000000007,
    num_of_ways_loop(N, 1, 6, 6, MOD).

num_of_ways_loop(N, N, AbaCount, AbcCount, MOD) ->
    (AbaCount + AbcCount) rem MOD;
num_of_ways_loop(N, I, AbaCount, AbcCount, MOD) ->
    NewAbaCount = (3 * AbaCount + 2 * AbcCount) rem MOD,
    NewAbcCount = (2 * AbaCount + 2 * AbcCount) rem MOD,
    num_of_ways_loop(N, I + 1, NewAbaCount, NewAbcCount, MOD).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec num_of_ways(n :: integer) :: integer
  def num_of_ways(n) do
    mod = 1_000_000_007

    # Base case for n=1
    aba_count = 6
    abc_count = 6

    # Iterate from i=2 to n
    Enum.reduce(2..n, {aba_count, abc_count}, fn _, {current_aba, current_abc} ->
      new_aba_count = (3 * current_aba + 2 * current_abc) |> rem(mod)
      new_abc_count = (2 * current_aba + 2 * current_abc) |> rem(mod)
      {new_aba_count, new_abc_count}
    end)
    |> (fn {final_aba, final_abc} -> (final_aba + final_abc) |> rem(mod) end).()
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The algorithm iterates n-1 times to compute the counts for each row from 2 to n. In each iteration, a constant number of arithmetic operations (multiplications, additions, and modulo operations) are performed. Therefore, the time complexity is O(N).

- **Space Complexity:** The algorithm only needs to store the counts for the previous row to compute the current row's counts. This means we only need a constant number of variables (two for ABA count and ABC count). Thus, the space complexity is O(1).

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-03 01:05:46 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved using dynamic programming. We define a 4D DP array dp[idx][prev1col][prev2col][prev3col] where dp[idx][prev1col][prev2col][prev3col] represents the number of ways to color the rows of the grid from idx to n-1, given that the previous row (idx - 1) has colors prev1col, prev2col, and prev3col. We iterate over all possible colors for the current row and update the DP array accordingly. The base case is when idx equals n, in which case there is only one way to color the grid (i.e., no more rows to color). The final answer is the sum of dp[1][i][j][k] for all possible i, j, and k, which represents the number of ways to color the entire grid.

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-cpp-llama-3-3-70b-versatile" checked>
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-java-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-python-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-python3-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-c-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-csharp-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-javascript-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-typescript-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-php-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-swift-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-kotlin-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-dart-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-go-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-ruby-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-scala-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-rust-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-racket-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-erlang-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-elixir-llama-3-3-70b-versatile">
  <div class="tab-labels">
    <label for="lang-cpp-llama-3-3-70b-versatile">C++</label>
    <label for="lang-java-llama-3-3-70b-versatile">Java</label>
    <label for="lang-python-llama-3-3-70b-versatile">Python</label>
    <label for="lang-python3-llama-3-3-70b-versatile">Python3</label>
    <label for="lang-c-llama-3-3-70b-versatile">C</label>
    <label for="lang-csharp-llama-3-3-70b-versatile">C#</label>
    <label for="lang-javascript-llama-3-3-70b-versatile">JavaScript</label>
    <label for="lang-typescript-llama-3-3-70b-versatile">TypeScript</label>
    <label for="lang-php-llama-3-3-70b-versatile">PHP</label>
    <label for="lang-swift-llama-3-3-70b-versatile">Swift</label>
    <label for="lang-kotlin-llama-3-3-70b-versatile">Kotlin</label>
    <label for="lang-dart-llama-3-3-70b-versatile">Dart</label>
    <label for="lang-go-llama-3-3-70b-versatile">Go</label>
    <label for="lang-ruby-llama-3-3-70b-versatile">Ruby</label>
    <label for="lang-scala-llama-3-3-70b-versatile">Scala</label>
    <label for="lang-rust-llama-3-3-70b-versatile">Rust</label>
    <label for="lang-racket-llama-3-3-70b-versatile">Racket</label>
    <label for="lang-erlang-llama-3-3-70b-versatile">Erlang</label>
    <label for="lang-elixir-llama-3-3-70b-versatile">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
class Solution {
public:
    int numOfWays(int n) {
        const int MOD = 1e9 + 7;
        long long dp[5001][3][3][3] = {0};
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    if (i != j && j != k && k != i) {
                        dp[1][i][j][k] = 1;
                    }
                }
            }
        }
        for (int idx = 2; idx <= n; idx++) {
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    for (int k = 0; k < 3; k++) {
                        if (dp[idx - 1][i][j][k] > 0) {
                            for (int x = 0; x < 3; x++) {
                                for (int y = 0; y < 3; y++) {
                                    for (int z = 0; z < 3; z++) {
                                        if (x != y && y != z && z != x && x != i && y != j && z != k) {
                                            dp[idx][x][y][z] = (dp[idx][x][y][z] + dp[idx - 1][i][j][k]) % MOD;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        long long ans = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    ans = (ans + dp[n][i][j][k]) % MOD;
                }
            }
        }
        return ans;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int numOfWays(int n) {
        final int MOD = (int) 1e9 + 7;
        long[][][][] dp = new long[5001][3][3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    if (i != j && j != k && k != i) {
                        dp[1][i][j][k] = 1;
                    }
                }
            }
        }
        for (int idx = 2; idx <= n; idx++) {
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    for (int k = 0; k < 3; k++) {
                        if (dp[idx - 1][i][j][k] > 0) {
                            for (int x = 0; x < 3; x++) {
                                for (int y = 0; y < 3; y++) {
                                    for (int z = 0; z < 3; z++) {
                                        if (x != y && y != z && z != x && x != i && y != j && z != k) {
                                            dp[idx][x][y][z] = (dp[idx][x][y][z] + dp[idx - 1][i][j][k]) % MOD;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        long ans = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    ans = (ans + dp[n][i][j][k]) % MOD;
                }
            }
        }
        return (int) ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if i != j and j != k and k != i:
                        dp[i][j][k] = 1
        for idx in range(2, n + 1):
            new_dp = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(3)]
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        if dp[i][j][k] > 0:
                            for x in range(3):
                                for y in range(3):
                                    for z in range(3):
                                        if x != y and y != z and z != x and x != i and y != j and z != k:
                                            new_dp[x][y][z] = (new_dp[x][y][z] + dp[i][j][k]) % MOD
            dp = new_dp
        ans = 0
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    ans = (ans + dp[i][j][k]) % MOD
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if i != j and j != k and k != i:
                        dp[i][j][k] = 1
        for idx in range(2, n + 1):
            new_dp = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(3)]
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        if dp[i][j][k] > 0:
                            for x in range(3):
                                for y in range(3):
                                    for z in range(3):
                                        if x != y and y != z and z != x and x != i and y != j and z != k:
                                            new_dp[x][y][z] = (new_dp[x][y][z] + dp[i][j][k]) % MOD
            dp = new_dp
        ans = 0
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    ans = (ans + dp[i][j][k]) % MOD
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
Not implemented
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
Not implemented
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
Not implemented
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
Not implemented
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
Not implemented
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
Not implemented
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
Not implemented
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
Not implemented
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
Not implemented
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
Not implemented
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
Not implemented
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
Not implemented
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
Not implemented
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
Not implemented
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
Not implemented
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n * 3^4) because we have n rows and for each row, we have 3 choices for each of the 3 columns, resulting in 3^3 possibilities for the current row and 3 possibilities for the previous row.

- **Space Complexity:** O(n * 3^3) because we need to store the DP array of size n * 3 * 3 * 3.

</div>
</details>
