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
        \ MOD = 1e9 + 7;\n\n        long long dp_2_colors = 6; // Patterns like RGR\n\
        \        long long dp_3_colors = 6; // Patterns like RYG\n\n        for (int\
        \ i = 2; i <= n; ++i) {\n            // If current row is ABA type (e.g., 010):\n\
        \            //   It can be preceded by 3 ABA patterns (e.g., 101, 121, 202\
        \ for 010)\n            //   It can be preceded by 2 ABC patterns (e.g., 102,\
        \ 201 for 010)\n            long long new_dp_2_colors = (3 * dp_2_colors + 2\
        \ * dp_3_colors) % MOD;\n\n            // If current row is ABC type (e.g.,\
        \ 012):\n            //   It can be preceded by 2 ABA patterns (e.g., 101, 121\
        \ for 012)\n            //   It can be preceded by 2 ABC patterns (e.g., 120,\
        \ 201 for 012)\n            long long new_dp_3_colors = (2 * dp_2_colors + 2\
        \ * dp_3_colors) % MOD;\n\n            dp_2_colors = new_dp_2_colors;\n    \
        \        dp_3_colors = new_dp_3_colors;\n        }\n\n        return (int)((dp_2_colors\
        \ + dp_3_colors) % MOD);\n    }\n};"
      java: "class Solution {\n    public int numOfWays(int n) {\n        long MOD =\
        \ 1_000_000_007;\n\n        long dp_2_colors = 6; // Patterns like RGR\n   \
        \     long dp_3_colors = 6; // Patterns like RYG\n\n        for (int i = 2;\
        \ i <= n; ++i) {\n            // If current row is ABA type (e.g., 010):\n \
        \           //   It can be preceded by 3 ABA patterns (e.g., 101, 121, 202 for\
        \ 010)\n            //   It can be preceded by 2 ABC patterns (e.g., 102, 201\
        \ for 010)\n            long new_dp_2_colors = (3 * dp_2_colors + 2 * dp_3_colors)\
        \ % MOD;\n\n            // If current row is ABC type (e.g., 012):\n       \
        \     //   It can be preceded by 2 ABA patterns (e.g., 101, 121 for 012)\n \
        \           //   It can be preceded by 2 ABC patterns (e.g., 120, 201 for 012)\n\
        \            long new_dp_3_colors = (2 * dp_2_colors + 2 * dp_3_colors) % MOD;\n\
        \n            dp_2_colors = new_dp_2_colors;\n            dp_3_colors = new_dp_3_colors;\n\
        \        }\n\n        return (int)((dp_2_colors + dp_3_colors) % MOD);\n   \
        \ }\n}"
      python: "class Solution(object):\n    def numOfWays(self, n):\n        \"\"\"\n\
        \        :type n: int\n        :rtype: int\n        \"\"\"\n        MOD = 10**9\
        \ + 7\n\n        # dp_2_colors: number of ways to paint a row with 2 distinct\
        \ colors (e.g., RGR)\n        # dp_3_colors: number of ways to paint a row with\
        \ 3 distinct colors (e.g., RYG)\n\n        # For n=1:\n        # There are 6\
        \ patterns of type ABA (e.g., RGR, RYR, GRG, GYG, YRY, YGY)\n        # There\
        \ are 6 patterns of type ABC (e.g., RYG, RGY, YRG, YGR, GRY, GYR)\n        dp_2_colors\
        \ = 6\n        dp_3_colors = 6\n\n        for _ in range(2, n + 1):\n      \
        \      # If current row is ABA type (e.g., 010):\n            #   It can be\
        \ preceded by 3 ABA patterns (e.g., 101, 121, 202 for 010)\n            #  \
        \ It can be preceded by 2 ABC patterns (e.g., 102, 201 for 010)\n          \
        \  new_dp_2_colors = (3 * dp_2_colors + 2 * dp_3_colors) % MOD\n\n         \
        \   # If current row is ABC type (e.g., 012):\n            #   It can be preceded\
        \ by 2 ABA patterns (e.g., 101, 121 for 012)\n            #   It can be preceded\
        \ by 2 ABC patterns (e.g., 120, 201 for 012)\n            new_dp_3_colors =\
        \ (2 * dp_2_colors + 2 * dp_3_colors) % MOD\n\n            dp_2_colors = new_dp_2_colors\n\
        \            dp_3_colors = new_dp_3_colors\n\n        return (dp_2_colors +\
        \ dp_3_colors) % MOD"
      python3: "class Solution:\n    def numOfWays(self, n: int) -> int:\n        MOD\
        \ = 10**9 + 7\n\n        # dp_2_colors: number of ways to paint a row with 2\
        \ distinct colors (e.g., RGR)\n        # dp_3_colors: number of ways to paint\
        \ a row with 3 distinct colors (e.g., RYG)\n\n        # For n=1:\n        #\
        \ There are 6 patterns of type ABA (e.g., RGR, RYR, GRG, GYG, YRY, YGY)\n  \
        \      # There are 6 patterns of type ABC (e.g., RYG, RGY, YRG, YGR, GRY, GYR)\n\
        \        dp_2_colors = 6\n        dp_3_colors = 6\n\n        for _ in range(2,\
        \ n + 1):\n            # If current row is ABA type (e.g., 010):\n         \
        \   #   It can be preceded by 3 ABA patterns (e.g., 101, 121, 202 for 010)\n\
        \            #   It can be preceded by 2 ABC patterns (e.g., 102, 201 for 010)\n\
        \            new_dp_2_colors = (3 * dp_2_colors + 2 * dp_3_colors) % MOD\n\n\
        \            # If current row is ABC type (e.g., 012):\n            #   It can\
        \ be preceded by 2 ABA patterns (e.g., 101, 121 for 012)\n            #   It\
        \ can be preceded by 2 ABC patterns (e.g., 120, 201 for 012)\n            new_dp_3_colors\
        \ = (2 * dp_2_colors + 2 * dp_3_colors) % MOD\n\n            dp_2_colors = new_dp_2_colors\n\
        \            dp_3_colors = new_dp_3_colors\n\n        return (dp_2_colors +\
        \ dp_3_colors) % MOD"
      c: "int numOfWays(int n) {\n    long long MOD = 1e9 + 7;\n\n    long long dp_2_colors\
        \ = 6; // Patterns like RGR\n    long long dp_3_colors = 6; // Patterns like\
        \ RYG\n\n    for (int i = 2; i <= n; ++i) {\n        // If current row is ABA\
        \ type (e.g., 010):\n        //   It can be preceded by 3 ABA patterns (e.g.,\
        \ 101, 121, 202 for 010)\n        //   It can be preceded by 2 ABC patterns\
        \ (e.g., 102, 201 for 010)\n        long long new_dp_2_colors = (3 * dp_2_colors\
        \ + 2 * dp_3_colors) % MOD;\n\n        // If current row is ABC type (e.g.,\
        \ 012):\n        //   It can be preceded by 2 ABA patterns (e.g., 101, 121 for\
        \ 012)\n        //   It can be preceded by 2 ABC patterns (e.g., 120, 201 for\
        \ 012)\n        long long new_dp_3_colors = (2 * dp_2_colors + 2 * dp_3_colors)\
        \ % MOD;\n\n        dp_2_colors = new_dp_2_colors;\n        dp_3_colors = new_dp_3_colors;\n\
        \    }\n\n    return (int)((dp_2_colors + dp_3_colors) % MOD);\n}"
      csharp: "public class Solution {\n    public int NumOfWays(int n) {\n        long\
        \ mod = 1_000_000_007;\n        long countAba = 6; // Ways to paint a row with\
        \ pattern like RGR (2 colors)\n        long countAbc = 6; // Ways to paint a\
        \ row with pattern like RYG (3 colors)\n\n        for (int i = 2; i <= n; i++)\
        \ {\n            long nextAba = (countAba * 3 + countAbc * 2) % mod;\n     \
        \       long nextAbc = (countAba * 2 + countAbc * 2) % mod;\n            countAba\
        \ = nextAba;\n            countAbc = nextAbc;\n        }\n\n        return (int)((countAba\
        \ + countAbc) % mod);\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @return {number}\n */\nvar numOfWays\
        \ = function(n) {\n    const mod = 1_000_000_007;\n    let countAba = 6; //\
        \ Ways to paint a row with pattern like RGR (2 colors)\n    let countAbc = 6;\
        \ // Ways to paint a row with pattern like RYG (3 colors)\n\n    for (let i\
        \ = 2; i <= n; i++) {\n        let nextAba = (countAba * 3 + countAbc * 2) %\
        \ mod;\n        let nextAbc = (countAba * 2 + countAbc * 2) % mod;\n       \
        \ countAba = nextAba;\n        countAbc = nextAbc;\n    }\n\n    return (countAba\
        \ + countAbc) % mod;\n};"
      typescript: "function numOfWays(n: number): number {\n    const mod = 1_000_000_007;\n\
        \    let countAba: number = 6; // Ways to paint a row with pattern like RGR\
        \ (2 colors)\n    let countAbc: number = 6; // Ways to paint a row with pattern\
        \ like RYG (3 colors)\n\n    for (let i = 2; i <= n; i++) {\n        let nextAba:\
        \ number = (countAba * 3 + countAbc * 2) % mod;\n        let nextAbc: number\
        \ = (countAba * 2 + countAbc * 2) % mod;\n        countAba = nextAba;\n    \
        \    countAbc = nextAbc;\n    }\n\n    return (countAba + countAbc) % mod;\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @return Integer\n\
        \     */\n    function numOfWays($n) {\n        $mod = 1000000007;\n       \
        \ $countAba = 6; // Ways to paint a row with pattern like RGR (2 colors)\n \
        \       $countAbc = 6; // Ways to paint a row with pattern like RYG (3 colors)\n\
        \n        for ($i = 2; $i <= $n; $i++) {\n            $nextAba = ($countAba\
        \ * 3 + $countAbc * 2) % $mod;\n            $nextAbc = ($countAba * 2 + $countAbc\
        \ * 2) % $mod;\n            $countAba = $nextAba;\n            $countAbc = $nextAbc;\n\
        \        }\n\n        return ($countAba + $countAbc) % $mod;\n    }\n}"
      swift: "class Solution {\n    func numOfWays(_ n: Int) -> Int {\n        let mod\
        \ = 1_000_000_007\n        var countAba: Int = 6 // Ways to paint a row with\
        \ pattern like RGR (2 colors)\n        var countAbc: Int = 6 // Ways to paint\
        \ a row with pattern like RYG (3 colors)\n\n        for _ in 2...n {\n     \
        \       let nextAba = (countAba * 3 + countAbc * 2) % mod\n            let nextAbc\
        \ = (countAba * 2 + countAbc * 2) % mod\n            countAba = nextAba\n  \
        \          countAbc = nextAbc\n        }\n\n        return (countAba + countAbc)\
        \ % mod\n    }\n}"
      kotlin: "class Solution {\n    fun numOfWays(n: Int): Int {\n        val MOD =\
        \ 1_000_000_000 + 7\n\n        var dp3Color: Long = 6L\n        var dp2Color:\
        \ Long = 6L\n\n        for (i in 2..n) {\n            val newDp3Color = (2 *\
        \ dp3Color + 2 * dp2Color) % MOD\n            val newDp2Color = (2 * dp3Color\
        \ + 3 * dp2Color) % MOD\n            dp3Color = newDp3Color\n            dp2Color\
        \ = newDp2Color\n        }\n\n        return ((dp3Color + dp2Color) % MOD).toInt()\n\
        \    }\n}"
      dart: "class Solution {\n  int numOfWays(int n) {\n    final int MOD = 1000000000\
        \ + 7;\n\n    int dp3Color = 6;\n    int dp2Color = 6;\n\n    for (int i = 2;\
        \ i <= n; i++) {\n      int newDp3Color = (2 * dp3Color + 2 * dp2Color) % MOD;\n\
        \      int newDp2Color = (2 * dp3Color + 3 * dp2Color) % MOD;\n      dp3Color\
        \ = newDp3Color;\n      dp2Color = newDp2Color;\n    }\n\n    return (dp3Color\
        \ + dp2Color) % MOD;\n  }\n}"
      go: "func numOfWays(n int) int {\n    MOD := 1_000_000_000 + 7\n\n    var dp3Color\
        \ int64 = 6\n    var dp2Color int64 = 6\n\n    for i := 2; i <= n; i++ {\n \
        \       newDp3Color := (2*dp3Color + 2*dp2Color) % MOD\n        newDp2Color\
        \ := (2*dp3Color + 3*dp2Color) % MOD\n        dp3Color = newDp3Color\n     \
        \   dp2Color = newDp2Color\n    }\n\n    return int((dp3Color + dp2Color) %\
        \ MOD)\n}"
      ruby: "# @param {Integer} n\n# @return {Integer}\ndef num_of_ways(n)\n    mod\
        \ = 10**9 + 7\n\n    dp_3_color = 6\n    dp_2_color = 6\n\n    (2..n).each do\
        \ |i|\n        new_dp_3_color = (2 * dp_3_color + 2 * dp_2_color) % mod\n  \
        \      new_dp_2_color = (2 * dp_3_color + 3 * dp_2_color) % mod\n        dp_3_color\
        \ = new_dp_3_color\n        dp_2_color = new_dp_2_color\n    end\n\n    (dp_3_color\
        \ + dp_2_color) % mod\nend"
      scala: "object Solution {\n    def numOfWays(n: Int): Int = {\n        val MOD\
        \ = 1_000_000_000 + 7\n\n        var dp3Color: Long = 6L\n        var dp2Color:\
        \ Long = 6L\n\n        for (i <- 2 to n) {\n            val newDp3Color = (2\
        \ * dp3Color + 2 * dp2Color) % MOD\n            val newDp2Color = (2 * dp3Color\
        \ + 3 * dp2Color) % MOD\n            dp3Color = newDp3Color\n            dp2Color\
        \ = newDp2Color\n        }\n\n        ((dp3Color + dp2Color) % MOD).toInt\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn num_of_ways(n: i33) -> i33 {\n        let modulo:\
        \ i64 = 1_000_000_007;\n\n        // a_prev: count of ways to paint previous\
        \ row with 3-color patterns (e.g., R-Y-G)\n        // b_prev: count of ways\
        \ to paint previous row with 2-color patterns (e.g., R-Y-R)\n        let mut\
        \ a_prev: i64 = 6; // For n=1, there are 6 such patterns\n        let mut b_prev:\
        \ i64 = 6; // For n=1, there are 6 such patterns\n\n        for _i in 2..=n\
        \ {\n            let a_curr = (a_prev * 2 + b_prev * 2) % modulo;\n        \
        \    let b_curr = (a_prev * 2 + b_prev * 3) % modulo;\n            a_prev =\
        \ a_curr;\n            b_prev = b_curr;\n        }\n\n        ((a_prev + b_prev)\
        \ % modulo) as i32\n    }\n}"
      racket: "(define/contract (num-of-ways n)\n  (-> exact-integer? exact-integer?)\n\
        \  (let* ([modulo 1000000007]\n         [a-prev 6] ; count of ways to paint\
        \ previous row with 3-color patterns (e.g., R-Y-G)\n         [b-prev 6] ; count\
        \ of ways to paint previous row with 2-color patterns (e.g., R-Y-R)\n      \
        \   [result (for/fold ([a a-prev] [b b-prev])\n                           ([i\
        \ (in-range 2 (+ n 1))])\n                   (let ([a-curr (modulo (+ (* a 2)\
        \ (* b 2)) modulo)]\n                         [b-curr (modulo (+ (* a 2) (*\
        \ b 3)) modulo)])\n                     (values a-curr b-curr)))])\n    (modulo\
        \ (+ (car result) (cdr result)) modulo)))"
      erlang: "-spec num_of_ways(N :: integer()) -> integer().\nnum_of_ways(N) ->\n\
        \    Modulo = 1000000007,\n    %% a_prev: count of ways to paint previous row\
        \ with 3-color patterns (e.g., R-Y-G)\n    %% b_prev: count of ways to paint\
        \ previous row with 2-color patterns (e.g., R-Y-R)\n    A_prev = 6, %% For N=1,\
        \ there are 6 such patterns\n    B_prev = 6, %% For N=1, there are 6 such patterns\n\
        \n    %% Use a fold-like approach for iteration\n    Result = lists:foldl(fun(_I,\
        \ {A_acc, B_acc}) ->\n                                 A_curr = (A_acc * 2 +\
        \ B_acc * 2) rem Modulo,\n                                 B_curr = (A_acc *\
        \ 2 + B_acc * 3) rem Modulo,\n                                 {A_curr, B_curr}\n\
        \                         end, {A_prev, B_prev}, lists:seq(2, N)),\n\n    {Final_A,\
        \ Final_B} = Result,\n    (Final_A + Final_B) rem Modulo."
      elixir: "defmodule Solution do\n  @spec num_of_ways(n :: integer) :: integer\n\
        \  def num_of_ways(n) do\n    modulo = 1_000_000_007\n\n    # a_prev: count\
        \ of ways to paint previous row with 3-color patterns (e.g., R-Y-G)\n    # b_prev:\
        \ count of ways to paint previous row with 2-color patterns (e.g., R-Y-R)\n\
        \    a_prev = 6 # For n=1, there are 6 such patterns\n    b_prev = 6 # For n=1,\
        \ there are 6 such patterns\n\n    {final_a, final_b} = \n      Enum.reduce(2..n,\
        \ {a_prev, b_prev}, fn _i, {a_acc, b_acc} ->\n        a_curr = rem(a_acc * 2\
        \ + b_acc * 2, modulo)\n        b_curr = rem(a_acc * 2 + b_acc * 3, modulo)\n\
        \        {a_curr, b_curr}\n      end)\n\n    rem(final_a + final_b, modulo)\n\
        \  end\nend"
    approach: 'The problem can be solved using dynamic programming by observing that
      the number of ways to paint the current row depends only on the color pattern
      of the previous row. We categorize valid single-row color patterns into two types:
      ''ABA'' patterns (e.g., Red-Yellow-Red, where the first and third colors are the
      same but different from the middle color) and ''ABC'' patterns (e.g., Red-Yellow-Green,
      where all three colors are distinct). There are 6 distinct ''ABA'' patterns and
      6 distinct ''ABC'' patterns for a single row, totaling 12 ways for n=1.


      We define two DP states: `dp_aba[i]` as the number of ways to paint `i` rows such
      that the `i`-th row ends with an ''ABA'' pattern, and `dp_abc[i]` as the number
      of ways to paint `i` rows such that the `i`-th row ends with an ''ABC'' pattern.
      By analyzing the compatibility between current and previous row patterns, we derive
      recurrence relations: an ''ABA'' pattern can be placed on top of 3 ''ABA'' patterns
      or 2 ''ABC'' patterns from the previous row. Similarly, an ''ABC'' pattern can
      be placed on top of 2 ''ABA'' patterns or 2 ''ABC'' patterns from the previous
      row. This leads to `dp_aba[i] = (dp_aba[i-1] * 3 + dp_abc[i-1] * 2) % MOD` and
      `dp_abc[i] = (dp_aba[i-1] * 2 + dp_abc[i-1] * 2) % MOD`. The base cases are `dp_aba[1]
      = 6` and `dp_abc[1] = 6`. Since the current state only depends on the previous
      state, we can optimize space to O(1) by iteratively updating the counts.'
    time_complexity: The time complexity is O(N). We iterate from `i = 2` to `n` (or
      `n-1` times in a 0-indexed loop), performing a constant number of arithmetic operations
      and modulo operations in each iteration. Therefore, the total time taken scales
      linearly with the number of rows `n`.
    space_complexity: The space complexity is O(1). We only need to store the counts
      for the two types of patterns from the previous row (`count_aba` and `count_abc`)
      to calculate the counts for the current row. This requires a constant amount of
      memory regardless of the input `n`.
    elapsed_time: 159.07864689826965
    model: gemini-2.5-flash
    generated_at: '2026-01-04 06:23:03 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int numOfWays(int n) {\n        const int\
        \ MOD = 1e9 + 7;\n        long long dp[3][3][3] = {0};\n        for (int i =\
        \ 0; i < 3; i++) {\n            for (int j = 0; j < 3; j++) {\n            \
        \    for (int k = 0; k < 3; k++) {\n                    if (i != j && j != k\
        \ && i != k) {\n                        dp[i][j][k] = 1;\n                 \
        \   }\n                }\n            }\n        }\n        for (int i = 2;\
        \ i <= n; i++) {\n            long long ndp[3][3][3] = {0};\n            for\
        \ (int a = 0; a < 3; a++) {\n                for (int b = 0; b < 3; b++) {\n\
        \                    for (int c = 0; c < 3; c++) {\n                       \
        \ if (dp[a][b][c] > 0) {\n                            for (int d = 0; d < 3;\
        \ d++) {\n                                for (int e = 0; e < 3; e++) {\n  \
        \                                  for (int f = 0; f < 3; f++) {\n         \
        \                               if (a != d && b != e && c != f && d != e &&\
        \ e != f && d != f) {\n                                            ndp[d][e][f]\
        \ = (ndp[d][e][f] + dp[a][b][c]) % MOD;\n                                  \
        \      }\n                                    }\n                          \
        \      }\n                            }\n                        }\n       \
        \             }\n                }\n            }\n            for (int a =\
        \ 0; a < 3; a++) {\n                for (int b = 0; b < 3; b++) {\n        \
        \            for (int c = 0; c < 3; c++) {\n                        dp[a][b][c]\
        \ = ndp[a][b][c];\n                    }\n                }\n            }\n\
        \        }\n        long long ans = 0;\n        for (int i = 0; i < 3; i++)\
        \ {\n            for (int j = 0; j < 3; j++) {\n                for (int k =\
        \ 0; k < 3; k++) {\n                    ans = (ans + dp[i][j][k]) % MOD;\n \
        \               }\n            }\n        }\n        return ans;\n    }\n};"
      java: "class Solution {\n    public int numOfWays(int n) {\n        final int\
        \ MOD = (int) 1e9 + 7;\n        long[][][] dp = new long[3][3][3];\n       \
        \ for (int i = 0; i < 3; i++) {\n            for (int j = 0; j < 3; j++) {\n\
        \                for (int k = 0; k < 3; k++) {\n                    if (i !=\
        \ j && j != k && i != k) {\n                        dp[i][j][k] = 1;\n     \
        \               }\n                }\n            }\n        }\n        for\
        \ (int i = 2; i <= n; i++) {\n            long[][][] ndp = new long[3][3][3];\n\
        \            for (int a = 0; a < 3; a++) {\n                for (int b = 0;\
        \ b < 3; b++) {\n                    for (int c = 0; c < 3; c++) {\n       \
        \                 if (dp[a][b][c] > 0) {\n                            for (int\
        \ d = 0; d < 3; d++) {\n                                for (int e = 0; e <\
        \ 3; e++) {\n                                    for (int f = 0; f < 3; f++)\
        \ {\n                                        if (a != d && b != e && c != f\
        \ && d != e && e != f && d != f) {\n                                       \
        \     ndp[d][e][f] = (ndp[d][e][f] + dp[a][b][c]) % MOD;\n                 \
        \                       }\n                                    }\n         \
        \                       }\n                            }\n                 \
        \       }\n                    }\n                }\n            }\n       \
        \     for (int a = 0; a < 3; a++) {\n                for (int b = 0; b < 3;\
        \ b++) {\n                    for (int c = 0; c < 3; c++) {\n              \
        \          dp[a][b][c] = ndp[a][b][c];\n                    }\n            \
        \    }\n            }\n        }\n        long ans = 0;\n        for (int i\
        \ = 0; i < 3; i++) {\n            for (int j = 0; j < 3; j++) {\n          \
        \      for (int k = 0; k < 3; k++) {\n                    ans = (ans + dp[i][j][k])\
        \ % MOD;\n                }\n            }\n        }\n        return (int)\
        \ ans;\n    }\n}"
      python: "class Solution(object):\n    def numOfWays(self, n):\n        MOD = 10**9\
        \ + 7\n        dp = [[[0]*3 for _ in range(3)] for _ in range(3)]\n        for\
        \ i in range(3):\n            for j in range(3):\n                for k in range(3):\n\
        \                    if i != j and j != k and i != k:\n                    \
        \    dp[i][j][k] = 1\n        for _ in range(2, n+1):\n            ndp = [[[0]*3\
        \ for _ in range(3)] for _ in range(3)]\n            for a in range(3):\n  \
        \              for b in range(3):\n                    for c in range(3):\n\
        \                        if dp[a][b][c] > 0:\n                            for\
        \ d in range(3):\n                                for e in range(3):\n     \
        \                               for f in range(3):\n                       \
        \                 if a != d and b != e and c != f and d != e and e != f and\
        \ d != f:\n                                            ndp[d][e][f] = (ndp[d][e][f]\
        \ + dp[a][b][c]) % MOD\n            dp = ndp\n        ans = 0\n        for i\
        \ in range(3):\n            for j in range(3):\n                for k in range(3):\n\
        \                    ans = (ans + dp[i][j][k]) % MOD\n        return ans"
      python3: "class Solution:\n    def numOfWays(self, n: int) -> int:\n        MOD\
        \ = 10**9 + 7\n        dp = [[[0]*3 for _ in range(3)] for _ in range(3)]\n\
        \        for i in range(3):\n            for j in range(3):\n              \
        \  for k in range(3):\n                    if i != j and j != k and i != k:\n\
        \                        dp[i][j][k] = 1\n        for _ in range(2, n+1):\n\
        \            ndp = [[[0]*3 for _ in range(3)] for _ in range(3)]\n         \
        \   for a in range(3):\n                for b in range(3):\n               \
        \     for c in range(3):\n                        if dp[a][b][c] > 0:\n    \
        \                        for d in range(3):\n                              \
        \  for e in range(3):\n                                    for f in range(3):\n\
        \                                        if a != d and b != e and c != f and\
        \ d != e and e != f and d != f:\n                                          \
        \  ndp[d][e][f] = (ndp[d][e][f] + dp[a][b][c]) % MOD\n            dp = ndp\n\
        \        ans = 0\n        for i in range(3):\n            for j in range(3):\n\
        \                for k in range(3):\n                    ans = (ans + dp[i][j][k])\
        \ % MOD\n        return ans"
      c: "int numOfWays(int n) {\n    const int MOD = 1e9 + 7;\n    long long dp[3][3][3]\
        \ = {0};\n    for (int i = 0; i < 3; i++) {\n        for (int j = 0; j < 3;\
        \ j++) {\n            for (int k = 0; k < 3; k++) {\n                if (i !=\
        \ j && j != k && i != k) {\n                    dp[i][j][k] = 1;\n         \
        \       }\n            }\n        }\n    }\n    for (int i = 2; i <= n; i++)\
        \ {\n        long long ndp[3][3][3] = {0};\n        for (int a = 0; a < 3; a++)\
        \ {\n            for (int b = 0; b < 3; b++) {\n                for (int c =\
        \ 0; c < 3; c++) {\n                    if (dp[a][b][c] > 0) {\n           \
        \             for (int d = 0; d < 3; d++) {\n                            for\
        \ (int e = 0; e < 3; e++) {\n                                for (int f = 0;\
        \ f < 3; f++) {\n                                    if (a != d && b != e &&\
        \ c != f && d != e && e != f && d != f) {\n                                \
        \        ndp[d][e][f] = (ndp[d][e][f] + dp[a][b][c]) % MOD;\n              \
        \                      }\n                                }\n              \
        \              }\n                        }\n                    }\n       \
        \         }\n            }\n        }\n        for (int a = 0; a < 3; a++) {\n\
        \            for (int b = 0; b < 3; b++) {\n                for (int c = 0;\
        \ c < 3; c++) {\n                    dp[a][b][c] = ndp[a][b][c];\n         \
        \       }\n            }\n        }\n    }\n    long long ans = 0;\n    for\
        \ (int i = 0; i < 3; i++) {\n        for (int j = 0; j < 3; j++) {\n       \
        \     for (int k = 0; k < 3; k++) {\n                ans = (ans + dp[i][j][k])\
        \ % MOD;\n            }\n        }\n    }\n    return ans;\n}"
      csharp: "public class Solution {\n    public int NumOfWays(int n) {\n        const\
        \ int MOD = 1000000007;\n        long[,,] dp = new long[n + 1, 3, 3, 3];\n \
        \       for (int i = 0; i < 3; i++) {\n            for (int j = 0; j < 3; j++)\
        \ {\n                for (int k = 0; k < 3; k++) {\n                    if (i\
        \ != j && j != k && k != i) {\n                        dp[1, i, j, k] = 1;\n\
        \                    }\n                }\n            }\n        }\n      \
        \  for (int idx = 2; idx <= n; idx++) {\n            for (int prev1col = 0;\
        \ prev1col < 3; prev1col++) {\n                for (int prev2col = 0; prev2col\
        \ < 3; prev2col++) {\n                    for (int prev3col = 0; prev3col <\
        \ 3; prev3col++) {\n                        if (dp[idx - 1, prev1col, prev2col,\
        \ prev3col] > 0) {\n                            for (int col1 = 0; col1 < 3;\
        \ col1++) {\n                                for (int col2 = 0; col2 < 3; col2++)\
        \ {\n                                    for (int col3 = 0; col3 < 3; col3++)\
        \ {\n                                        if (col1 != col2 && col2 != col3\
        \ && col3 != col1 && col1 != prev1col && col2 != prev2col && col3 != prev3col)\
        \ {\n                                            dp[idx, col1, col2, col3] =\
        \ (dp[idx, col1, col2, col3] + dp[idx - 1, prev1col, prev2col, prev3col]) %\
        \ MOD;\n                                        }\n                        \
        \            }\n                                }\n                        \
        \    }\n                        }\n                    }\n                }\n\
        \            }\n        }\n        long res = 0;\n        for (int i = 0; i\
        \ < 3; i++) {\n            for (int j = 0; j < 3; j++) {\n                for\
        \ (int k = 0; k < 3; k++) {\n                    res = (res + dp[n, i, j, k])\
        \ % MOD;\n                }\n            }\n        }\n        return (int)res;\n\
        \    }\n}"
      javascript: "var numOfWays = function(n) {\n    const MOD = 1000000007;\n    let\
        \ dp = Array(n + 1).fill(0).map(() => Array(3).fill(0).map(() => Array(3).fill(0).map(()\
        \ => Array(3).fill(0))));\n    for (let i = 0; i < 3; i++) {\n        for (let\
        \ j = 0; j < 3; j++) {\n            for (let k = 0; k < 3; k++) {\n        \
        \        if (i !== j && j !== k && k !== i) {\n                    dp[1][i][j][k]\
        \ = 1;\n                }\n            }\n        }\n    }\n    for (let idx\
        \ = 2; idx <= n; idx++) {\n        for (let prev1col = 0; prev1col < 3; prev1col++)\
        \ {\n            for (let prev2col = 0; prev2col < 3; prev2col++) {\n      \
        \          for (let prev3col = 0; prev3col < 3; prev3col++) {\n            \
        \        if (dp[idx - 1][prev1col][prev2col][prev3col] > 0) {\n            \
        \            for (let col1 = 0; col1 < 3; col1++) {\n                      \
        \      for (let col2 = 0; col2 < 3; col2++) {\n                            \
        \    for (let col3 = 0; col3 < 3; col3++) {\n                              \
        \      if (col1 !== col2 && col2 !== col3 && col3 !== col1 && col1 !== prev1col\
        \ && col2 !== prev2col && col3 !== prev3col) {\n                           \
        \             dp[idx][col1][col2][col3] = (dp[idx][col1][col2][col3] + dp[idx\
        \ - 1][prev1col][prev2col][prev3col]) % MOD;\n                             \
        \       }\n                                }\n                            }\n\
        \                        }\n                    }\n                }\n     \
        \       }\n        }\n    }\n    let res = 0;\n    for (let i = 0; i < 3; i++)\
        \ {\n        for (let j = 0; j < 3; j++) {\n            for (let k = 0; k <\
        \ 3; k++) {\n                res = (res + dp[n][i][j][k]) % MOD;\n         \
        \   }\n        }\n    }\n    return res;\n};"
      typescript: "function numOfWays(n: number): number {\n    const MOD: number =\
        \ 1000000007;\n    let dp: number[][][][] = Array(n + 1).fill(0).map(() => Array(3).fill(0).map(()\
        \ => Array(3).fill(0).map(() => Array(3).fill(0))));\n    for (let i = 0; i\
        \ < 3; i++) {\n        for (let j = 0; j < 3; j++) {\n            for (let k\
        \ = 0; k < 3; k++) {\n                if (i !== j && j !== k && k !== i) {\n\
        \                    dp[1][i][j][k] = 1;\n                }\n            }\n\
        \        }\n    }\n    for (let idx = 2; idx <= n; idx++) {\n        for (let\
        \ prev1col = 0; prev1col < 3; prev1col++) {\n            for (let prev2col =\
        \ 0; prev2col < 3; prev2col++) {\n                for (let prev3col = 0; prev3col\
        \ < 3; prev3col++) {\n                    if (dp[idx - 1][prev1col][prev2col][prev3col]\
        \ > 0) {\n                        for (let col1 = 0; col1 < 3; col1++) {\n \
        \                           for (let col2 = 0; col2 < 3; col2++) {\n       \
        \                         for (let col3 = 0; col3 < 3; col3++) {\n         \
        \                           if (col1 !== col2 && col2 !== col3 && col3 !== col1\
        \ && col1 !== prev1col && col2 !== prev2col && col3 !== prev3col) {\n      \
        \                                  dp[idx][col1][col2][col3] = (dp[idx][col1][col2][col3]\
        \ + dp[idx - 1][prev1col][prev2col][prev3col]) % MOD;\n                    \
        \                }\n                                }\n                    \
        \        }\n                        }\n                    }\n             \
        \   }\n            }\n        }\n    }\n    let res: number = 0;\n    for (let\
        \ i = 0; i < 3; i++) {\n        for (let j = 0; j < 3; j++) {\n            for\
        \ (let k = 0; k < 3; k++) {\n                res = (res + dp[n][i][j][k]) %\
        \ MOD;\n            }\n        }\n    }\n    return res;\n}"
      php: "class Solution {\n    function numOfWays($n) {\n        $MOD = 1000000007;\n\
        \        $dp = array_fill(0, $n + 1, array_fill(0, 3, array_fill(0, 3, array_fill(0,\
        \ 3, 0))));\n        for ($i = 0; $i < 3; $i++) {\n            for ($j = 0;\
        \ $j < 3; $j++) {\n                for ($k = 0; $k < 3; $k++) {\n          \
        \          if ($i !== $j && $j !== $k && $k !== $i) {\n                    \
        \    $dp[1][$i][$j][$k] = 1;\n                    }\n                }\n   \
        \         }\n        }\n        for ($idx = 2; $idx <= $n; $idx++) {\n     \
        \       for ($prev1col = 0; $prev1col < 3; $prev1col++) {\n                for\
        \ ($prev2col = 0; $prev2col < 3; $prev2col++) {\n                    for ($prev3col\
        \ = 0; $prev3col < 3; $prev3col++) {\n                        if ($dp[$idx -\
        \ 1][$prev1col][$prev2col][$prev3col] > 0) {\n                            for\
        \ ($col1 = 0; $col1 < 3; $col1++) {\n                                for ($col2\
        \ = 0; $col2 < 3; $col2++) {\n                                    for ($col3\
        \ = 0; $col3 < 3; $col3++) {\n                                        if ($col1\
        \ !== $col2 && $col2 !== $col3 && $col3 !== $col1 && $col1 !== $prev1col &&\
        \ $col2 !== $prev2col && $col3 !== $prev3col) {\n                          \
        \                  $dp[$idx][$col1][$col2][$col3] = ($dp[$idx][$col1][$col2][$col3]\
        \ + $dp[$idx - 1][$prev1col][$prev2col][$prev3col]) % $MOD;\n              \
        \                          }\n                                    }\n      \
        \                          }\n                            }\n              \
        \          }\n                    }\n                }\n            }\n    \
        \    }\n        $res = 0;\n        for ($i = 0; $i < 3; $i++) {\n          \
        \  for ($j = 0; $j < 3; $j++) {\n                for ($k = 0; $k < 3; $k++)\
        \ {\n                    $res = ($res + $dp[$n][$i][$j][$k]) % $MOD;\n     \
        \           }\n            }\n        }\n        return $res;\n    }\n}"
      swift: "class Solution {\n    func numOfWays(_ n: Int) -> Int {\n        let MOD:\
        \ Int = 1000000007\n        var dp: [[[Int]]] = Array(repeating: Array(repeating:\
        \ Array(repeating: 0, count: 3), count: 3), count: 3)\n        for i in 0..<3\
        \ {\n            for j in 0..<3 {\n                for k in 0..<3 {\n      \
        \              if i != j && j != k && k != i {\n                        dp[1][i][j][k]\
        \ = 1\n                    }\n                }\n            }\n        }\n\
        \        for idx in 2...n {\n            for prev1col in 0..<3 {\n         \
        \       for prev2col in 0..<3 {\n                    for prev3col in 0..<3 {\n\
        \                        if dp[idx - 1][prev1col][prev2col][prev3col] > 0 {\n\
        \                            for col1 in 0..<3 {\n                         \
        \       for col2 in 0..<3 {\n                                    for col3 in\
        \ 0..<3 {\n                                        if col1 != col2 && col2 !=\
        \ col3 && col3 != col1 && col1 != prev1col && col2 != prev2col && col3 != prev3col\
        \ {\n                                            dp[idx][col1][col2][col3] =\
        \ (dp[idx][col1][col2][col3] + dp[idx - 1][prev1col][prev2col][prev3col]) %\
        \ MOD\n                                        }\n                         \
        \           }\n                                }\n                         \
        \   }\n                        }\n                    }\n                }\n\
        \            }\n        }\n        var res: Int = 0\n        for i in 0..<3\
        \ {\n            for j in 0..<3 {\n                for k in 0..<3 {\n      \
        \              res = (res + dp[n][i][j][k]) % MOD\n                }\n     \
        \       }\n        }\n        return res\n    }\n}"
      kotlin: "class Solution {\n    fun numOfWays(n: Int): Int {\n        val MOD =\
        \ 1000000007\n        val memo = HashMap<String, Long>()\n        fun dp(row:\
        \ Int, prev1: Int, prev2: Int, prev3: Int): Long {\n            if (row == n)\
        \ return 1\n            val key = \"$row,$prev1,$prev2,$prev3\"\n          \
        \  if (memo.containsKey(key)) return memo[key]!!\n            var res = 0L\n\
        \            for (i in 0..2) {\n                for (j in 0..2) {\n        \
        \            for (k in 0..2) {\n                        if (i != prev1 && j\
        \ != prev2 && k != prev3 && i != j && j != k) {\n                          \
        \  res = (res + dp(row + 1, i, j, k)) % MOD\n                        }\n   \
        \                 }\n                }\n            }\n            memo[key]\
        \ = res\n            return res\n        }\n        return dp(0, -1, -1, -1).toInt()\n\
        \    }\n}"
      dart: "class Solution {\n  int numOfWays(int n) {\n    final int MOD = 1000000007;\n\
        \    final Map<String, int> memo = {};\n    int dp(int row, int prev1, int prev2,\
        \ int prev3) {\n      if (row == n) return 1;\n      final String key = \"$row,$prev1,$prev2,$prev3\"\
        ;\n      if (memo.containsKey(key)) return memo[key]!;\n      int res = 0;\n\
        \      for (int i = 0; i < 3; i++) {\n        for (int j = 0; j < 3; j++) {\n\
        \          for (int k = 0; k < 3; k++) {\n            if (i != prev1 && j !=\
        \ prev2 && k != prev3 && i != j && j != k) {\n              res = (res + dp(row\
        \ + 1, i, j, k)) % MOD;\n            }\n          }\n        }\n      }\n  \
        \    memo[key] = res;\n      return res;\n    }\n    return dp(0, -1, -1, -1);\n\
        \  }\n}"
      go: "func numOfWays(n int) int {\n    const MOD int = 1e9 + 7\n    memo := make(map[string]int)\n\
        \    var dp func(row, prev1, prev2, prev3 int) int\n    dp = func(row, prev1,\
        \ prev2, prev3 int) int {\n        if row == n {\n            return 1\n   \
        \     }\n        key := fmt.Sprintf(\"%d,%d,%d,%d\", row, prev1, prev2, prev3)\n\
        \        if val, ok := memo[key]; ok {\n            return val\n        }\n\
        \        res := 0\n        for i := 0; i < 3; i++ {\n            for j := 0;\
        \ j < 3; j++ {\n                for k := 0; k < 3; k++ {\n                 \
        \   if i != prev1 && j != prev2 && k != prev3 && i != j && j != k {\n      \
        \                  res = (res + dp(row+1, i, j, k)) % MOD\n                \
        \    }\n                }\n            }\n        }\n        memo[key] = res\n\
        \        return res\n    }\n    return dp(0, -1, -1, -1)\n}"
      ruby: "def num_of_ways(n)\n    MOD = 10**9 + 7\n    memo = {}\n    def dp(row,\
        \ prev1, prev2, prev3)\n        if row == n\n            return 1\n        end\n\
        \        key = [row, prev1, prev2, prev3].join(\",\")\n        if memo.key?(key)\n\
        \            return memo[key]\n        end\n        res = 0\n        (0..2).each\
        \ do |i|\n            (0..2).each do |j|\n                (0..2).each do |k|\n\
        \                    if i != prev1 && j != prev2 && k != prev3 && i != j &&\
        \ j != k\n                        res = (res + dp(row + 1, i, j, k)) % MOD\n\
        \                    end\n                end\n            end\n        end\n\
        \        memo[key] = res\n        res\n    end\n    dp(0, -1, -1, -1)\nend"
      scala: "object Solution {\n    def numOfWays(n: Int): Int = {\n        val MOD\
        \ = 1000000007\n        val memo = scala.collection.mutable.Map[String, Long]()\n\
        \        def dp(row: Int, prev1: Int, prev2: Int, prev3: Int): Long = {\n  \
        \          if (row == n) return 1\n            val key = s\"$row,$prev1,$prev2,$prev3\"\
        \n            if (memo.contains(key)) return memo(key)\n            var res\
        \ = 0L\n            for (i <- 0 to 2) {\n                for (j <- 0 to 2) {\n\
        \                    for (k <- 0 to 2) {\n                        if (i != prev1\
        \ && j != prev2 && k != prev3 && i != j && j != k) {\n                     \
        \       res = (res + dp(row + 1, i, j, k)) % MOD\n                        }\n\
        \                    }\n                }\n            }\n            memo(key)\
        \ = res\n            res\n        }\n        dp(0, -1, -1, -1).toInt\n    }\n\
        }"
      rust: "impl Solution {\n    pub fn num_of_ways(n: i32) -> i32 {\n        const\
        \ MOD: i32 = 1_000_000_007;\n        let mut dp: [[[i32; 3]; 3]; 3] = [[[0;\
        \ 3]; 3]; 3];\n        for i in 0..3 {\n            for j in 0..3 {\n      \
        \          for k in 0..3 {\n                    if i != j && j != k && k !=\
        \ i {\n                        dp[i][j][k] = 1;\n                    }\n   \
        \             }\n            }\n        }\n        for _ in 1..n {\n       \
        \     let mut new_dp: [[[i32; 3]; 3]; 3] = [[[0; 3]; 3]; 3];\n            for\
        \ i in 0..3 {\n                for j in 0..3 {\n                    for k in\
        \ 0..3 {\n                        for x in 0..3 {\n                        \
        \    for y in 0..3 {\n                                for z in 0..3 {\n    \
        \                                if i != x && j != y && k != z && x != y &&\
        \ y != z && z != x {\n                                        new_dp[x][y][z]\
        \ = (new_dp[x][y][z] + dp[i][j][k]) % MOD;\n                               \
        \     }\n                                }\n                            }\n\
        \                        }\n                    }\n                }\n     \
        \       }\n            dp = new_dp;\n        }\n        let mut ans = 0;\n \
        \       for i in 0..3 {\n            for j in 0..3 {\n                for k\
        \ in 0..3 {\n                    ans = (ans + dp[i][j][k]) % MOD;\n        \
        \        }\n            }\n        }\n        ans\n    }\n}"
      racket: "(define/contract (num-of-ways n)\n  (-> exact-integer? exact-integer?)\n\
        \  (define MOD 1000000007)\n  (define dp (make-vector 27 0))\n  (define (idx\
        \ i j k) (+ (* i 9) (* j 3) k))\n  (for ([i (in-range 3)] [j (in-range 3)] [k\
        \ (in-range 3)])\n    (when (and (not (= i j)) (not (= j k)) (not (= k i)))\n\
        \      (vector-set! dp (idx i j k) 1)))\n  (for ([_ (in-range (sub1 n))])\n\
        \    (define new-dp (make-vector 27 0))\n    (for ([i (in-range 3)] [j (in-range\
        \ 3)] [k (in-range 3)])\n      (for ([x (in-range 3)] [y (in-range 3)] [z (in-range\
        \ 3)])\n        (when (and (not (= i x)) (not (= j y)) (not (= k z)) (not (=\
        \ x y)) (not (= y z)) (not (= z x)))\n          (vector-set! new-dp (idx x y\
        \ z) (modulo (+ (vector-ref new-dp (idx x y z)) (vector-ref dp (idx i j k)))\
        \ MOD))))))\n    (set! dp new-dp))\n  (apply + (vector->list dp)))"
      erlang: "num_of_ways(N) ->\n  MOD = 1000000007,\n  DP = array:new([27, {default,\
        \ 0}]),\n  Fun = fun(I, J, K) ->\n           case {I, J, K} of\n           \
        \  {I, J, K} when I =:= J; J =:= K; K =:= I ->\n               ok;\n       \
        \      _ ->\n               array:set(I * 9 + J * 3 + K, 1, DP)\n          \
        \ end\n         end,\n  lists:foreach(fun(I) ->\n                     lists:foreach(fun(J)\
        \ ->\n                                   lists:foreach(fun(K) -> Fun(I, J, K)\
        \ end, lists:seq(0, 2))\n                                 end, lists:seq(0,\
        \ 2))\n                   end, lists:seq(0, 2)),\n  Fun2 = fun(_, DP1) ->\n\
        \           DP2 = array:new([27, {default, 0}]),\n           Fun3 = fun(I, J,\
        \ K) ->\n                    Fun4 = fun(X, Y, Z) ->\n                      \
        \        case {I, J, K, X, Y, Z} of\n                                {I, J,\
        \ K, X, Y, Z} when I =:= X; J =:= Y; K =:= Z; X =:= Y; Y =:= Z; Z =:= X ->\n\
        \                                  ok;\n                                _ ->\n\
        \                                  array:set(X * 9 + Y * 3 + Z, (array:get(X\
        \ * 9 + Y * 3 + Z, DP2) + array:get(I * 9 + J * 3 + K, DP1)) rem MOD, DP2)\n\
        \                              end\n                            end,\n     \
        \               lists:foreach(fun(X) ->\n                                  \
        \ lists:foreach(fun(Y) ->\n                                                \
        \ lists:foreach(fun(Z) -> Fun4(X, Y, Z) end, lists:seq(0, 2))\n            \
        \                                   end, lists:seq(0, 2))\n                \
        \                 end, lists:seq(0, 2))\n                  end,\n          \
        \ lists:foreach(fun(I) ->\n                         lists:foreach(fun(J) ->\n\
        \                                   lists:foreach(fun(K) -> Fun3(I, J, K) end,\
        \ lists:seq(0, 2))\n                                 end, lists:seq(0, 2))\n\
        \                       end, lists:seq(0, 2)),\n           DP2\n         end,\n\
        \  lists:foldl(Fun2, DP, lists:seq(1, N - 1)),\n  array:foldl(fun(I, Acc, _)\
        \ -> Acc + array:get(I, DP) end, 0, DP) rem MOD."
      elixir: "defmodule Solution do\n  @spec num_of_ways(n :: integer) :: integer\n\
        \  def num_of_ways(n) do\n    mod = 1_000_000_007\n    dp = for i <- 0..2, j\
        \ <- 0..2, k <- 0..2, into: %{} do\n      {{i, j, k}, if i != j and j != k and\
        \ k != i, do: 1, else: 0}\n    end\n    for _ <- 1..(n - 1) do\n      new_dp\
        \ = for x <- 0..2, y <- 0..2, z <- 0..2, into: %{} do\n        {{x, y, z},\n\
        \         Enum.reduce(0..2, 0, fn i, acc ->\n           Enum.reduce(0..2, acc,\
        \ fn j, acc ->\n             Enum.reduce(0..2, acc, fn k, acc ->\n         \
        \      if i != x and j != y and k != z and x != y and y != z and z != x do\n\
        \                 rem(acc + Map.get(dp, {i, j, k}, 0), mod)\n              \
        \ else\n                 acc\n               end\n             end)\n      \
        \     end)\n         end)}\n      end\n      dp = new_dp\n    end\n    Enum.reduce(dp,\
        \ 0, fn {_, v}, acc -> rem(acc + v, mod) end)\n  end\nend"
    approach: The problem can be solved using dynamic programming. We will create a
      4D DP array where dp[idx][prev1col][prev2col][prev3col] represents the number
      of ways to color the rows of the grid from idx to n-1, given that the previous
      row has colors prev1col, prev2col, and prev3col. We will iterate over all possible
      colors for the current row and update the DP array accordingly. The base case
      will be when we have colored all rows, in which case we return 1. The final answer
      will be the sum of all possible ways to color the first row, which will be stored
      in dp[1][prev1col][prev2col][prev3col] for all possible prev1col, prev2col, and
      prev3col. We will use a modulo operation to avoid overflow, as the answer can
      be very large.
    time_complexity: The time complexity of the solution is O(n * 3^4) because we are
      iterating over all possible colors for the current row and the previous row. The
      space complexity is also O(n * 3^4) because we need to store the DP array. However,
      we can optimize the space complexity to O(3^4) by only storing the previous row
      in the DP array.
    space_complexity: The space complexity of the solution is O(3^4) because we only
      need to store the previous row in the DP array. This is a significant improvement
      over the original O(n * 3^4) space complexity, and it allows us to solve the problem
      for large values of n.
    elapsed_time: 18.610949516296387
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-04 06:23:37 '
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
  <small class="solution-timestamp">(2026-01-04 06:23:03 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved using dynamic programming by observing that the number of ways to paint the current row depends only on the color pattern of the previous row. We categorize valid single-row color patterns into two types: 'ABA' patterns (e.g., Red-Yellow-Red, where the first and third colors are the same but different from the middle color) and 'ABC' patterns (e.g., Red-Yellow-Green, where all three colors are distinct). There are 6 distinct 'ABA' patterns and 6 distinct 'ABC' patterns for a single row, totaling 12 ways for n=1.

We define two DP states: `dp_aba[i]` as the number of ways to paint `i` rows such that the `i`-th row ends with an 'ABA' pattern, and `dp_abc[i]` as the number of ways to paint `i` rows such that the `i`-th row ends with an 'ABC' pattern. By analyzing the compatibility between current and previous row patterns, we derive recurrence relations: an 'ABA' pattern can be placed on top of 3 'ABA' patterns or 2 'ABC' patterns from the previous row. Similarly, an 'ABC' pattern can be placed on top of 2 'ABA' patterns or 2 'ABC' patterns from the previous row. This leads to `dp_aba[i] = (dp_aba[i-1] * 3 + dp_abc[i-1] * 2) % MOD` and `dp_abc[i] = (dp_aba[i-1] * 2 + dp_abc[i-1] * 2) % MOD`. The base cases are `dp_aba[1] = 6` and `dp_abc[1] = 6`. Since the current state only depends on the previous state, we can optimize space to O(1) by iteratively updating the counts.

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

        long long dp_2_colors = 6; // Patterns like RGR
        long long dp_3_colors = 6; // Patterns like RYG

        for (int i = 2; i <= n; ++i) {
            // If current row is ABA type (e.g., 010):
            //   It can be preceded by 3 ABA patterns (e.g., 101, 121, 202 for 010)
            //   It can be preceded by 2 ABC patterns (e.g., 102, 201 for 010)
            long long new_dp_2_colors = (3 * dp_2_colors + 2 * dp_3_colors) % MOD;

            // If current row is ABC type (e.g., 012):
            //   It can be preceded by 2 ABA patterns (e.g., 101, 121 for 012)
            //   It can be preceded by 2 ABC patterns (e.g., 120, 201 for 012)
            long long new_dp_3_colors = (2 * dp_2_colors + 2 * dp_3_colors) % MOD;

            dp_2_colors = new_dp_2_colors;
            dp_3_colors = new_dp_3_colors;
        }

        return (int)((dp_2_colors + dp_3_colors) % MOD);
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

        long dp_2_colors = 6; // Patterns like RGR
        long dp_3_colors = 6; // Patterns like RYG

        for (int i = 2; i <= n; ++i) {
            // If current row is ABA type (e.g., 010):
            //   It can be preceded by 3 ABA patterns (e.g., 101, 121, 202 for 010)
            //   It can be preceded by 2 ABC patterns (e.g., 102, 201 for 010)
            long new_dp_2_colors = (3 * dp_2_colors + 2 * dp_3_colors) % MOD;

            // If current row is ABC type (e.g., 012):
            //   It can be preceded by 2 ABA patterns (e.g., 101, 121 for 012)
            //   It can be preceded by 2 ABC patterns (e.g., 120, 201 for 012)
            long new_dp_3_colors = (2 * dp_2_colors + 2 * dp_3_colors) % MOD;

            dp_2_colors = new_dp_2_colors;
            dp_3_colors = new_dp_3_colors;
        }

        return (int)((dp_2_colors + dp_3_colors) % MOD);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7

        # dp_2_colors: number of ways to paint a row with 2 distinct colors (e.g., RGR)
        # dp_3_colors: number of ways to paint a row with 3 distinct colors (e.g., RYG)

        # For n=1:
        # There are 6 patterns of type ABA (e.g., RGR, RYR, GRG, GYG, YRY, YGY)
        # There are 6 patterns of type ABC (e.g., RYG, RGY, YRG, YGR, GRY, GYR)
        dp_2_colors = 6
        dp_3_colors = 6

        for _ in range(2, n + 1):
            # If current row is ABA type (e.g., 010):
            #   It can be preceded by 3 ABA patterns (e.g., 101, 121, 202 for 010)
            #   It can be preceded by 2 ABC patterns (e.g., 102, 201 for 010)
            new_dp_2_colors = (3 * dp_2_colors + 2 * dp_3_colors) % MOD

            # If current row is ABC type (e.g., 012):
            #   It can be preceded by 2 ABA patterns (e.g., 101, 121 for 012)
            #   It can be preceded by 2 ABC patterns (e.g., 120, 201 for 012)
            new_dp_3_colors = (2 * dp_2_colors + 2 * dp_3_colors) % MOD

            dp_2_colors = new_dp_2_colors
            dp_3_colors = new_dp_3_colors

        return (dp_2_colors + dp_3_colors) % MOD
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        # dp_2_colors: number of ways to paint a row with 2 distinct colors (e.g., RGR)
        # dp_3_colors: number of ways to paint a row with 3 distinct colors (e.g., RYG)

        # For n=1:
        # There are 6 patterns of type ABA (e.g., RGR, RYR, GRG, GYG, YRY, YGY)
        # There are 6 patterns of type ABC (e.g., RYG, RGY, YRG, YGR, GRY, GYR)
        dp_2_colors = 6
        dp_3_colors = 6

        for _ in range(2, n + 1):
            # If current row is ABA type (e.g., 010):
            #   It can be preceded by 3 ABA patterns (e.g., 101, 121, 202 for 010)
            #   It can be preceded by 2 ABC patterns (e.g., 102, 201 for 010)
            new_dp_2_colors = (3 * dp_2_colors + 2 * dp_3_colors) % MOD

            # If current row is ABC type (e.g., 012):
            #   It can be preceded by 2 ABA patterns (e.g., 101, 121 for 012)
            #   It can be preceded by 2 ABC patterns (e.g., 120, 201 for 012)
            new_dp_3_colors = (2 * dp_2_colors + 2 * dp_3_colors) % MOD

            dp_2_colors = new_dp_2_colors
            dp_3_colors = new_dp_3_colors

        return (dp_2_colors + dp_3_colors) % MOD
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int numOfWays(int n) {
    long long MOD = 1e9 + 7;

    long long dp_2_colors = 6; // Patterns like RGR
    long long dp_3_colors = 6; // Patterns like RYG

    for (int i = 2; i <= n; ++i) {
        // If current row is ABA type (e.g., 010):
        //   It can be preceded by 3 ABA patterns (e.g., 101, 121, 202 for 010)
        //   It can be preceded by 2 ABC patterns (e.g., 102, 201 for 010)
        long long new_dp_2_colors = (3 * dp_2_colors + 2 * dp_3_colors) % MOD;

        // If current row is ABC type (e.g., 012):
        //   It can be preceded by 2 ABA patterns (e.g., 101, 121 for 012)
        //   It can be preceded by 2 ABC patterns (e.g., 120, 201 for 012)
        long long new_dp_3_colors = (2 * dp_2_colors + 2 * dp_3_colors) % MOD;

        dp_2_colors = new_dp_2_colors;
        dp_3_colors = new_dp_3_colors;
    }

    return (int)((dp_2_colors + dp_3_colors) % MOD);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int NumOfWays(int n) {
        long mod = 1_000_000_007;
        long countAba = 6; // Ways to paint a row with pattern like RGR (2 colors)
        long countAbc = 6; // Ways to paint a row with pattern like RYG (3 colors)

        for (int i = 2; i <= n; i++) {
            long nextAba = (countAba * 3 + countAbc * 2) % mod;
            long nextAbc = (countAba * 2 + countAbc * 2) % mod;
            countAba = nextAba;
            countAbc = nextAbc;
        }

        return (int)((countAba + countAbc) % mod);
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
    const mod = 1_000_000_007;
    let countAba = 6; // Ways to paint a row with pattern like RGR (2 colors)
    let countAbc = 6; // Ways to paint a row with pattern like RYG (3 colors)

    for (let i = 2; i <= n; i++) {
        let nextAba = (countAba * 3 + countAbc * 2) % mod;
        let nextAbc = (countAba * 2 + countAbc * 2) % mod;
        countAba = nextAba;
        countAbc = nextAbc;
    }

    return (countAba + countAbc) % mod;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function numOfWays(n: number): number {
    const mod = 1_000_000_007;
    let countAba: number = 6; // Ways to paint a row with pattern like RGR (2 colors)
    let countAbc: number = 6; // Ways to paint a row with pattern like RYG (3 colors)

    for (let i = 2; i <= n; i++) {
        let nextAba: number = (countAba * 3 + countAbc * 2) % mod;
        let nextAbc: number = (countAba * 2 + countAbc * 2) % mod;
        countAba = nextAba;
        countAbc = nextAbc;
    }

    return (countAba + countAbc) % mod;
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
        $mod = 1000000007;
        $countAba = 6; // Ways to paint a row with pattern like RGR (2 colors)
        $countAbc = 6; // Ways to paint a row with pattern like RYG (3 colors)

        for ($i = 2; $i <= $n; $i++) {
            $nextAba = ($countAba * 3 + $countAbc * 2) % $mod;
            $nextAbc = ($countAba * 2 + $countAbc * 2) % $mod;
            $countAba = $nextAba;
            $countAbc = $nextAbc;
        }

        return ($countAba + $countAbc) % $mod;
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
        let mod = 1_000_000_007
        var countAba: Int = 6 // Ways to paint a row with pattern like RGR (2 colors)
        var countAbc: Int = 6 // Ways to paint a row with pattern like RYG (3 colors)

        for _ in 2...n {
            let nextAba = (countAba * 3 + countAbc * 2) % mod
            let nextAbc = (countAba * 2 + countAbc * 2) % mod
            countAba = nextAba
            countAbc = nextAbc
        }

        return (countAba + countAbc) % mod
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
        val MOD = 1_000_000_000 + 7

        var dp3Color: Long = 6L
        var dp2Color: Long = 6L

        for (i in 2..n) {
            val newDp3Color = (2 * dp3Color + 2 * dp2Color) % MOD
            val newDp2Color = (2 * dp3Color + 3 * dp2Color) % MOD
            dp3Color = newDp3Color
            dp2Color = newDp2Color
        }

        return ((dp3Color + dp2Color) % MOD).toInt()
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
    final int MOD = 1000000000 + 7;

    int dp3Color = 6;
    int dp2Color = 6;

    for (int i = 2; i <= n; i++) {
      int newDp3Color = (2 * dp3Color + 2 * dp2Color) % MOD;
      int newDp2Color = (2 * dp3Color + 3 * dp2Color) % MOD;
      dp3Color = newDp3Color;
      dp2Color = newDp2Color;
    }

    return (dp3Color + dp2Color) % MOD;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func numOfWays(n int) int {
    MOD := 1_000_000_000 + 7

    var dp3Color int64 = 6
    var dp2Color int64 = 6

    for i := 2; i <= n; i++ {
        newDp3Color := (2*dp3Color + 2*dp2Color) % MOD
        newDp2Color := (2*dp3Color + 3*dp2Color) % MOD
        dp3Color = newDp3Color
        dp2Color = newDp2Color
    }

    return int((dp3Color + dp2Color) % MOD)
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
    mod = 10**9 + 7

    dp_3_color = 6
    dp_2_color = 6

    (2..n).each do |i|
        new_dp_3_color = (2 * dp_3_color + 2 * dp_2_color) % mod
        new_dp_2_color = (2 * dp_3_color + 3 * dp_2_color) % mod
        dp_3_color = new_dp_3_color
        dp_2_color = new_dp_2_color
    end

    (dp_3_color + dp_2_color) % mod
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def numOfWays(n: Int): Int = {
        val MOD = 1_000_000_000 + 7

        var dp3Color: Long = 6L
        var dp2Color: Long = 6L

        for (i <- 2 to n) {
            val newDp3Color = (2 * dp3Color + 2 * dp2Color) % MOD
            val newDp2Color = (2 * dp3Color + 3 * dp2Color) % MOD
            dp3Color = newDp3Color
            dp2Color = newDp2Color
        }

        ((dp3Color + dp2Color) % MOD).toInt
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn num_of_ways(n: i33) -> i33 {
        let modulo: i64 = 1_000_000_007;

        // a_prev: count of ways to paint previous row with 3-color patterns (e.g., R-Y-G)
        // b_prev: count of ways to paint previous row with 2-color patterns (e.g., R-Y-R)
        let mut a_prev: i64 = 6; // For n=1, there are 6 such patterns
        let mut b_prev: i64 = 6; // For n=1, there are 6 such patterns

        for _i in 2..=n {
            let a_curr = (a_prev * 2 + b_prev * 2) % modulo;
            let b_curr = (a_prev * 2 + b_prev * 3) % modulo;
            a_prev = a_curr;
            b_prev = b_curr;
        }

        ((a_prev + b_prev) % modulo) as i32
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
  (let* ([modulo 1000000007]
         [a-prev 6] ; count of ways to paint previous row with 3-color patterns (e.g., R-Y-G)
         [b-prev 6] ; count of ways to paint previous row with 2-color patterns (e.g., R-Y-R)
         [result (for/fold ([a a-prev] [b b-prev])
                           ([i (in-range 2 (+ n 1))])
                   (let ([a-curr (modulo (+ (* a 2) (* b 2)) modulo)]
                         [b-curr (modulo (+ (* a 2) (* b 3)) modulo)])
                     (values a-curr b-curr)))])
    (modulo (+ (car result) (cdr result)) modulo)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec num_of_ways(N :: integer()) -> integer().
num_of_ways(N) ->
    Modulo = 1000000007,
    %% a_prev: count of ways to paint previous row with 3-color patterns (e.g., R-Y-G)
    %% b_prev: count of ways to paint previous row with 2-color patterns (e.g., R-Y-R)
    A_prev = 6, %% For N=1, there are 6 such patterns
    B_prev = 6, %% For N=1, there are 6 such patterns

    %% Use a fold-like approach for iteration
    Result = lists:foldl(fun(_I, {A_acc, B_acc}) ->
                                 A_curr = (A_acc * 2 + B_acc * 2) rem Modulo,
                                 B_curr = (A_acc * 2 + B_acc * 3) rem Modulo,
                                 {A_curr, B_curr}
                         end, {A_prev, B_prev}, lists:seq(2, N)),

    {Final_A, Final_B} = Result,
    (Final_A + Final_B) rem Modulo.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec num_of_ways(n :: integer) :: integer
  def num_of_ways(n) do
    modulo = 1_000_000_007

    # a_prev: count of ways to paint previous row with 3-color patterns (e.g., R-Y-G)
    # b_prev: count of ways to paint previous row with 2-color patterns (e.g., R-Y-R)
    a_prev = 6 # For n=1, there are 6 such patterns
    b_prev = 6 # For n=1, there are 6 such patterns

    {final_a, final_b} = 
      Enum.reduce(2..n, {a_prev, b_prev}, fn _i, {a_acc, b_acc} ->
        a_curr = rem(a_acc * 2 + b_acc * 2, modulo)
        b_curr = rem(a_acc * 2 + b_acc * 3, modulo)
        {a_curr, b_curr}
      end)

    rem(final_a + final_b, modulo)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N). We iterate from `i = 2` to `n` (or `n-1` times in a 0-indexed loop), performing a constant number of arithmetic operations and modulo operations in each iteration. Therefore, the total time taken scales linearly with the number of rows `n`.

- **Space Complexity:** The space complexity is O(1). We only need to store the counts for the two types of patterns from the previous row (`count_aba` and `count_abc`) to calculate the counts for the current row. This requires a constant amount of memory regardless of the input `n`.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-04 06:23:37 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved using dynamic programming. We will create a 4D DP array where dp[idx][prev1col][prev2col][prev3col] represents the number of ways to color the rows of the grid from idx to n-1, given that the previous row has colors prev1col, prev2col, and prev3col. We will iterate over all possible colors for the current row and update the DP array accordingly. The base case will be when we have colored all rows, in which case we return 1. The final answer will be the sum of all possible ways to color the first row, which will be stored in dp[1][prev1col][prev2col][prev3col] for all possible prev1col, prev2col, and prev3col. We will use a modulo operation to avoid overflow, as the answer can be very large.

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
        long long dp[3][3][3] = {0};
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    if (i != j && j != k && i != k) {
                        dp[i][j][k] = 1;
                    }
                }
            }
        }
        for (int i = 2; i <= n; i++) {
            long long ndp[3][3][3] = {0};
            for (int a = 0; a < 3; a++) {
                for (int b = 0; b < 3; b++) {
                    for (int c = 0; c < 3; c++) {
                        if (dp[a][b][c] > 0) {
                            for (int d = 0; d < 3; d++) {
                                for (int e = 0; e < 3; e++) {
                                    for (int f = 0; f < 3; f++) {
                                        if (a != d && b != e && c != f && d != e && e != f && d != f) {
                                            ndp[d][e][f] = (ndp[d][e][f] + dp[a][b][c]) % MOD;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
            for (int a = 0; a < 3; a++) {
                for (int b = 0; b < 3; b++) {
                    for (int c = 0; c < 3; c++) {
                        dp[a][b][c] = ndp[a][b][c];
                    }
                }
            }
        }
        long long ans = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    ans = (ans + dp[i][j][k]) % MOD;
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
        long[][][] dp = new long[3][3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    if (i != j && j != k && i != k) {
                        dp[i][j][k] = 1;
                    }
                }
            }
        }
        for (int i = 2; i <= n; i++) {
            long[][][] ndp = new long[3][3][3];
            for (int a = 0; a < 3; a++) {
                for (int b = 0; b < 3; b++) {
                    for (int c = 0; c < 3; c++) {
                        if (dp[a][b][c] > 0) {
                            for (int d = 0; d < 3; d++) {
                                for (int e = 0; e < 3; e++) {
                                    for (int f = 0; f < 3; f++) {
                                        if (a != d && b != e && c != f && d != e && e != f && d != f) {
                                            ndp[d][e][f] = (ndp[d][e][f] + dp[a][b][c]) % MOD;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
            for (int a = 0; a < 3; a++) {
                for (int b = 0; b < 3; b++) {
                    for (int c = 0; c < 3; c++) {
                        dp[a][b][c] = ndp[a][b][c];
                    }
                }
            }
        }
        long ans = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    ans = (ans + dp[i][j][k]) % MOD;
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
class Solution(object):
    def numOfWays(self, n):
        MOD = 10**9 + 7
        dp = [[[0]*3 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if i != j and j != k and i != k:
                        dp[i][j][k] = 1
        for _ in range(2, n+1):
            ndp = [[[0]*3 for _ in range(3)] for _ in range(3)]
            for a in range(3):
                for b in range(3):
                    for c in range(3):
                        if dp[a][b][c] > 0:
                            for d in range(3):
                                for e in range(3):
                                    for f in range(3):
                                        if a != d and b != e and c != f and d != e and e != f and d != f:
                                            ndp[d][e][f] = (ndp[d][e][f] + dp[a][b][c]) % MOD
            dp = ndp
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
        dp = [[[0]*3 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if i != j and j != k and i != k:
                        dp[i][j][k] = 1
        for _ in range(2, n+1):
            ndp = [[[0]*3 for _ in range(3)] for _ in range(3)]
            for a in range(3):
                for b in range(3):
                    for c in range(3):
                        if dp[a][b][c] > 0:
                            for d in range(3):
                                for e in range(3):
                                    for f in range(3):
                                        if a != d and b != e and c != f and d != e and e != f and d != f:
                                            ndp[d][e][f] = (ndp[d][e][f] + dp[a][b][c]) % MOD
            dp = ndp
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
int numOfWays(int n) {
    const int MOD = 1e9 + 7;
    long long dp[3][3][3] = {0};
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            for (int k = 0; k < 3; k++) {
                if (i != j && j != k && i != k) {
                    dp[i][j][k] = 1;
                }
            }
        }
    }
    for (int i = 2; i <= n; i++) {
        long long ndp[3][3][3] = {0};
        for (int a = 0; a < 3; a++) {
            for (int b = 0; b < 3; b++) {
                for (int c = 0; c < 3; c++) {
                    if (dp[a][b][c] > 0) {
                        for (int d = 0; d < 3; d++) {
                            for (int e = 0; e < 3; e++) {
                                for (int f = 0; f < 3; f++) {
                                    if (a != d && b != e && c != f && d != e && e != f && d != f) {
                                        ndp[d][e][f] = (ndp[d][e][f] + dp[a][b][c]) % MOD;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        for (int a = 0; a < 3; a++) {
            for (int b = 0; b < 3; b++) {
                for (int c = 0; c < 3; c++) {
                    dp[a][b][c] = ndp[a][b][c];
                }
            }
        }
    }
    long long ans = 0;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            for (int k = 0; k < 3; k++) {
                ans = (ans + dp[i][j][k]) % MOD;
            }
        }
    }
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int NumOfWays(int n) {
        const int MOD = 1000000007;
        long[,,] dp = new long[n + 1, 3, 3, 3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    if (i != j && j != k && k != i) {
                        dp[1, i, j, k] = 1;
                    }
                }
            }
        }
        for (int idx = 2; idx <= n; idx++) {
            for (int prev1col = 0; prev1col < 3; prev1col++) {
                for (int prev2col = 0; prev2col < 3; prev2col++) {
                    for (int prev3col = 0; prev3col < 3; prev3col++) {
                        if (dp[idx - 1, prev1col, prev2col, prev3col] > 0) {
                            for (int col1 = 0; col1 < 3; col1++) {
                                for (int col2 = 0; col2 < 3; col2++) {
                                    for (int col3 = 0; col3 < 3; col3++) {
                                        if (col1 != col2 && col2 != col3 && col3 != col1 && col1 != prev1col && col2 != prev2col && col3 != prev3col) {
                                            dp[idx, col1, col2, col3] = (dp[idx, col1, col2, col3] + dp[idx - 1, prev1col, prev2col, prev3col]) % MOD;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        long res = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    res = (res + dp[n, i, j, k]) % MOD;
                }
            }
        }
        return (int)res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var numOfWays = function(n) {
    const MOD = 1000000007;
    let dp = Array(n + 1).fill(0).map(() => Array(3).fill(0).map(() => Array(3).fill(0).map(() => Array(3).fill(0))));
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            for (let k = 0; k < 3; k++) {
                if (i !== j && j !== k && k !== i) {
                    dp[1][i][j][k] = 1;
                }
            }
        }
    }
    for (let idx = 2; idx <= n; idx++) {
        for (let prev1col = 0; prev1col < 3; prev1col++) {
            for (let prev2col = 0; prev2col < 3; prev2col++) {
                for (let prev3col = 0; prev3col < 3; prev3col++) {
                    if (dp[idx - 1][prev1col][prev2col][prev3col] > 0) {
                        for (let col1 = 0; col1 < 3; col1++) {
                            for (let col2 = 0; col2 < 3; col2++) {
                                for (let col3 = 0; col3 < 3; col3++) {
                                    if (col1 !== col2 && col2 !== col3 && col3 !== col1 && col1 !== prev1col && col2 !== prev2col && col3 !== prev3col) {
                                        dp[idx][col1][col2][col3] = (dp[idx][col1][col2][col3] + dp[idx - 1][prev1col][prev2col][prev3col]) % MOD;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    let res = 0;
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            for (let k = 0; k < 3; k++) {
                res = (res + dp[n][i][j][k]) % MOD;
            }
        }
    }
    return res;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function numOfWays(n: number): number {
    const MOD: number = 1000000007;
    let dp: number[][][][] = Array(n + 1).fill(0).map(() => Array(3).fill(0).map(() => Array(3).fill(0).map(() => Array(3).fill(0))));
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            for (let k = 0; k < 3; k++) {
                if (i !== j && j !== k && k !== i) {
                    dp[1][i][j][k] = 1;
                }
            }
        }
    }
    for (let idx = 2; idx <= n; idx++) {
        for (let prev1col = 0; prev1col < 3; prev1col++) {
            for (let prev2col = 0; prev2col < 3; prev2col++) {
                for (let prev3col = 0; prev3col < 3; prev3col++) {
                    if (dp[idx - 1][prev1col][prev2col][prev3col] > 0) {
                        for (let col1 = 0; col1 < 3; col1++) {
                            for (let col2 = 0; col2 < 3; col2++) {
                                for (let col3 = 0; col3 < 3; col3++) {
                                    if (col1 !== col2 && col2 !== col3 && col3 !== col1 && col1 !== prev1col && col2 !== prev2col && col3 !== prev3col) {
                                        dp[idx][col1][col2][col3] = (dp[idx][col1][col2][col3] + dp[idx - 1][prev1col][prev2col][prev3col]) % MOD;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    let res: number = 0;
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            for (let k = 0; k < 3; k++) {
                res = (res + dp[n][i][j][k]) % MOD;
            }
        }
    }
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function numOfWays($n) {
        $MOD = 1000000007;
        $dp = array_fill(0, $n + 1, array_fill(0, 3, array_fill(0, 3, array_fill(0, 3, 0))));
        for ($i = 0; $i < 3; $i++) {
            for ($j = 0; $j < 3; $j++) {
                for ($k = 0; $k < 3; $k++) {
                    if ($i !== $j && $j !== $k && $k !== $i) {
                        $dp[1][$i][$j][$k] = 1;
                    }
                }
            }
        }
        for ($idx = 2; $idx <= $n; $idx++) {
            for ($prev1col = 0; $prev1col < 3; $prev1col++) {
                for ($prev2col = 0; $prev2col < 3; $prev2col++) {
                    for ($prev3col = 0; $prev3col < 3; $prev3col++) {
                        if ($dp[$idx - 1][$prev1col][$prev2col][$prev3col] > 0) {
                            for ($col1 = 0; $col1 < 3; $col1++) {
                                for ($col2 = 0; $col2 < 3; $col2++) {
                                    for ($col3 = 0; $col3 < 3; $col3++) {
                                        if ($col1 !== $col2 && $col2 !== $col3 && $col3 !== $col1 && $col1 !== $prev1col && $col2 !== $prev2col && $col3 !== $prev3col) {
                                            $dp[$idx][$col1][$col2][$col3] = ($dp[$idx][$col1][$col2][$col3] + $dp[$idx - 1][$prev1col][$prev2col][$prev3col]) % $MOD;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        $res = 0;
        for ($i = 0; $i < 3; $i++) {
            for ($j = 0; $j < 3; $j++) {
                for ($k = 0; $k < 3; $k++) {
                    $res = ($res + $dp[$n][$i][$j][$k]) % $MOD;
                }
            }
        }
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
    func numOfWays(_ n: Int) -> Int {
        let MOD: Int = 1000000007
        var dp: [[[Int]]] = Array(repeating: Array(repeating: Array(repeating: 0, count: 3), count: 3), count: 3)
        for i in 0..<3 {
            for j in 0..<3 {
                for k in 0..<3 {
                    if i != j && j != k && k != i {
                        dp[1][i][j][k] = 1
                    }
                }
            }
        }
        for idx in 2...n {
            for prev1col in 0..<3 {
                for prev2col in 0..<3 {
                    for prev3col in 0..<3 {
                        if dp[idx - 1][prev1col][prev2col][prev3col] > 0 {
                            for col1 in 0..<3 {
                                for col2 in 0..<3 {
                                    for col3 in 0..<3 {
                                        if col1 != col2 && col2 != col3 && col3 != col1 && col1 != prev1col && col2 != prev2col && col3 != prev3col {
                                            dp[idx][col1][col2][col3] = (dp[idx][col1][col2][col3] + dp[idx - 1][prev1col][prev2col][prev3col]) % MOD
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        var res: Int = 0
        for i in 0..<3 {
            for j in 0..<3 {
                for k in 0..<3 {
                    res = (res + dp[n][i][j][k]) % MOD
                }
            }
        }
        return res
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
        val MOD = 1000000007
        val memo = HashMap<String, Long>()
        fun dp(row: Int, prev1: Int, prev2: Int, prev3: Int): Long {
            if (row == n) return 1
            val key = "$row,$prev1,$prev2,$prev3"
            if (memo.containsKey(key)) return memo[key]!!
            var res = 0L
            for (i in 0..2) {
                for (j in 0..2) {
                    for (k in 0..2) {
                        if (i != prev1 && j != prev2 && k != prev3 && i != j && j != k) {
                            res = (res + dp(row + 1, i, j, k)) % MOD
                        }
                    }
                }
            }
            memo[key] = res
            return res
        }
        return dp(0, -1, -1, -1).toInt()
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
    final int MOD = 1000000007;
    final Map<String, int> memo = {};
    int dp(int row, int prev1, int prev2, int prev3) {
      if (row == n) return 1;
      final String key = "$row,$prev1,$prev2,$prev3";
      if (memo.containsKey(key)) return memo[key]!;
      int res = 0;
      for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
          for (int k = 0; k < 3; k++) {
            if (i != prev1 && j != prev2 && k != prev3 && i != j && j != k) {
              res = (res + dp(row + 1, i, j, k)) % MOD;
            }
          }
        }
      }
      memo[key] = res;
      return res;
    }
    return dp(0, -1, -1, -1);
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func numOfWays(n int) int {
    const MOD int = 1e9 + 7
    memo := make(map[string]int)
    var dp func(row, prev1, prev2, prev3 int) int
    dp = func(row, prev1, prev2, prev3 int) int {
        if row == n {
            return 1
        }
        key := fmt.Sprintf("%d,%d,%d,%d", row, prev1, prev2, prev3)
        if val, ok := memo[key]; ok {
            return val
        }
        res := 0
        for i := 0; i < 3; i++ {
            for j := 0; j < 3; j++ {
                for k := 0; k < 3; k++ {
                    if i != prev1 && j != prev2 && k != prev3 && i != j && j != k {
                        res = (res + dp(row+1, i, j, k)) % MOD
                    }
                }
            }
        }
        memo[key] = res
        return res
    }
    return dp(0, -1, -1, -1)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def num_of_ways(n)
    MOD = 10**9 + 7
    memo = {}
    def dp(row, prev1, prev2, prev3)
        if row == n
            return 1
        end
        key = [row, prev1, prev2, prev3].join(",")
        if memo.key?(key)
            return memo[key]
        end
        res = 0
        (0..2).each do |i|
            (0..2).each do |j|
                (0..2).each do |k|
                    if i != prev1 && j != prev2 && k != prev3 && i != j && j != k
                        res = (res + dp(row + 1, i, j, k)) % MOD
                    end
                end
            end
        end
        memo[key] = res
        res
    end
    dp(0, -1, -1, -1)
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def numOfWays(n: Int): Int = {
        val MOD = 1000000007
        val memo = scala.collection.mutable.Map[String, Long]()
        def dp(row: Int, prev1: Int, prev2: Int, prev3: Int): Long = {
            if (row == n) return 1
            val key = s"$row,$prev1,$prev2,$prev3"
            if (memo.contains(key)) return memo(key)
            var res = 0L
            for (i <- 0 to 2) {
                for (j <- 0 to 2) {
                    for (k <- 0 to 2) {
                        if (i != prev1 && j != prev2 && k != prev3 && i != j && j != k) {
                            res = (res + dp(row + 1, i, j, k)) % MOD
                        }
                    }
                }
            }
            memo(key) = res
            res
        }
        dp(0, -1, -1, -1).toInt
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
        const MOD: i32 = 1_000_000_007;
        let mut dp: [[[i32; 3]; 3]; 3] = [[[0; 3]; 3]; 3];
        for i in 0..3 {
            for j in 0..3 {
                for k in 0..3 {
                    if i != j && j != k && k != i {
                        dp[i][j][k] = 1;
                    }
                }
            }
        }
        for _ in 1..n {
            let mut new_dp: [[[i32; 3]; 3]; 3] = [[[0; 3]; 3]; 3];
            for i in 0..3 {
                for j in 0..3 {
                    for k in 0..3 {
                        for x in 0..3 {
                            for y in 0..3 {
                                for z in 0..3 {
                                    if i != x && j != y && k != z && x != y && y != z && z != x {
                                        new_dp[x][y][z] = (new_dp[x][y][z] + dp[i][j][k]) % MOD;
                                    }
                                }
                            }
                        }
                    }
                }
            }
            dp = new_dp;
        }
        let mut ans = 0;
        for i in 0..3 {
            for j in 0..3 {
                for k in 0..3 {
                    ans = (ans + dp[i][j][k]) % MOD;
                }
            }
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
(define/contract (num-of-ways n)
  (-> exact-integer? exact-integer?)
  (define MOD 1000000007)
  (define dp (make-vector 27 0))
  (define (idx i j k) (+ (* i 9) (* j 3) k))
  (for ([i (in-range 3)] [j (in-range 3)] [k (in-range 3)])
    (when (and (not (= i j)) (not (= j k)) (not (= k i)))
      (vector-set! dp (idx i j k) 1)))
  (for ([_ (in-range (sub1 n))])
    (define new-dp (make-vector 27 0))
    (for ([i (in-range 3)] [j (in-range 3)] [k (in-range 3)])
      (for ([x (in-range 3)] [y (in-range 3)] [z (in-range 3)])
        (when (and (not (= i x)) (not (= j y)) (not (= k z)) (not (= x y)) (not (= y z)) (not (= z x)))
          (vector-set! new-dp (idx x y z) (modulo (+ (vector-ref new-dp (idx x y z)) (vector-ref dp (idx i j k))) MOD))))))
    (set! dp new-dp))
  (apply + (vector->list dp)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
num_of_ways(N) ->
  MOD = 1000000007,
  DP = array:new([27, {default, 0}]),
  Fun = fun(I, J, K) ->
           case {I, J, K} of
             {I, J, K} when I =:= J; J =:= K; K =:= I ->
               ok;
             _ ->
               array:set(I * 9 + J * 3 + K, 1, DP)
           end
         end,
  lists:foreach(fun(I) ->
                     lists:foreach(fun(J) ->
                                   lists:foreach(fun(K) -> Fun(I, J, K) end, lists:seq(0, 2))
                                 end, lists:seq(0, 2))
                   end, lists:seq(0, 2)),
  Fun2 = fun(_, DP1) ->
           DP2 = array:new([27, {default, 0}]),
           Fun3 = fun(I, J, K) ->
                    Fun4 = fun(X, Y, Z) ->
                              case {I, J, K, X, Y, Z} of
                                {I, J, K, X, Y, Z} when I =:= X; J =:= Y; K =:= Z; X =:= Y; Y =:= Z; Z =:= X ->
                                  ok;
                                _ ->
                                  array:set(X * 9 + Y * 3 + Z, (array:get(X * 9 + Y * 3 + Z, DP2) + array:get(I * 9 + J * 3 + K, DP1)) rem MOD, DP2)
                              end
                            end,
                    lists:foreach(fun(X) ->
                                   lists:foreach(fun(Y) ->
                                                 lists:foreach(fun(Z) -> Fun4(X, Y, Z) end, lists:seq(0, 2))
                                               end, lists:seq(0, 2))
                                 end, lists:seq(0, 2))
                  end,
           lists:foreach(fun(I) ->
                         lists:foreach(fun(J) ->
                                   lists:foreach(fun(K) -> Fun3(I, J, K) end, lists:seq(0, 2))
                                 end, lists:seq(0, 2))
                       end, lists:seq(0, 2)),
           DP2
         end,
  lists:foldl(Fun2, DP, lists:seq(1, N - 1)),
  array:foldl(fun(I, Acc, _) -> Acc + array:get(I, DP) end, 0, DP) rem MOD.
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
    dp = for i <- 0..2, j <- 0..2, k <- 0..2, into: %{} do
      {{i, j, k}, if i != j and j != k and k != i, do: 1, else: 0}
    end
    for _ <- 1..(n - 1) do
      new_dp = for x <- 0..2, y <- 0..2, z <- 0..2, into: %{} do
        {{x, y, z},
         Enum.reduce(0..2, 0, fn i, acc ->
           Enum.reduce(0..2, acc, fn j, acc ->
             Enum.reduce(0..2, acc, fn k, acc ->
               if i != x and j != y and k != z and x != y and y != z and z != x do
                 rem(acc + Map.get(dp, {i, j, k}, 0), mod)
               else
                 acc
               end
             end)
           end)
         end)}
      end
      dp = new_dp
    end
    Enum.reduce(dp, 0, fn {_, v}, acc -> rem(acc + v, mod) end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of the solution is O(n * 3^4) because we are iterating over all possible colors for the current row and the previous row. The space complexity is also O(n * 3^4) because we need to store the DP array. However, we can optimize the space complexity to O(3^4) by only storing the previous row in the DP array.

- **Space Complexity:** The space complexity of the solution is O(3^4) because we only need to store the previous row in the DP array. This is a significant improvement over the original O(n * 3^4) space complexity, and it allows us to solve the problem for large values of n.

</div>
</details>
