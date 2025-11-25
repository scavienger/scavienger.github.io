---
layout: post
title: "Ones and Zeroes"
date: 2025-11-11 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "String", "Dynamic Programming"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/ones-and-zeroes/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int findMaxForm(std::vector<std::string>&\
        \ strs, int m, int n) {\n        std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n\
        \ + 1, 0));\n\n        for (const std::string& s : strs) {\n            int\
        \ zeros = 0;\n            int ones = 0;\n            for (char c : s) {\n  \
        \              if (c == '0') {\n                    zeros++;\n             \
        \   } else {\n                    ones++;\n                }\n            }\n\
        \n            for (int i = m; i >= zeros; --i) {\n                for (int j\
        \ = n; j >= ones; --j) {\n                    dp[i][j] = std::max(dp[i][j],\
        \ dp[i - zeros][j - ones] + 1);\n                }\n            }\n        }\n\
        \n        return dp[m][n];\n    }\n};"
      java: "import java.util.Arrays;\n\nclass Solution {\n    public int findMaxForm(String[]\
        \ strs, int m, int n) {\n        int[][] dp = new int[m + 1][n + 1];\n\n   \
        \     for (String s : strs) {\n            int zeros = 0;\n            int ones\
        \ = 0;\n            for (char c : s.toCharArray()) {\n                if (c\
        \ == '0') {\n                    zeros++;\n                } else {\n      \
        \              ones++;\n                }\n            }\n\n            for\
        \ (int i = m; i >= zeros; i--) {\n                for (int j = n; j >= ones;\
        \ j--) {\n                    dp[i][j] = Math.max(dp[i][j], dp[i - zeros][j\
        \ - ones] + 1);\n                }\n            }\n        }\n\n        return\
        \ dp[m][n];\n    }\n}"
      python: "class Solution:\n    def findMaxForm(self, strs: List[str], m: int, n:\
        \ int) -> int:\n        dp = [[0] * (n + 1) for _ in range(m + 1)]\n\n     \
        \   for s in strs:\n            zeros = s.count('0')\n            ones = s.count('1')\n\
        \n            for i in range(m, zeros - 1, -1):\n                for j in range(n,\
        \ ones - 1, -1):\n                    dp[i][j] = max(dp[i][j], dp[i - zeros][j\
        \ - ones] + 1)\n\n        return dp[m][n]"
      python3: "class Solution:\n    def findMaxForm(self, strs: List[str], m: int,\
        \ n: int) -> int:\n        dp = [[0] * (n + 1) for _ in range(m + 1)]\n\n  \
        \      for s in strs:\n            zeros = s.count('0')\n            ones =\
        \ s.count('1')\n\n            for i in range(m, zeros - 1, -1):\n          \
        \      for j in range(n, ones - 1, -1):\n                    dp[i][j] = max(dp[i][j],\
        \ dp[i - zeros][j - ones] + 1)\n\n        return dp[m][n]"
      c: "#include <stdlib.h>\n#include <string.h>\n\n// Helper function to count zeros\
        \ and ones\nvoid countZerosOnes(const char* s, int* zeros, int* ones) {\n  \
        \  *zeros = 0;\n    *ones = 0;\n    for (int k = 0; s[k] != '\\0'; k++) {\n\
        \        if (s[k] == '0') {\n            (*zeros)++;\n        } else {\n   \
        \         (*ones)++;\n        }\n    }\n}\n\nint findMaxForm(char ** strs, int\
        \ strsSize, int m, int n){\n    // dp[i][j] stores the maximum number of strings\
        \ that can be formed\n    // using at most i zeros and j ones.\n    int** dp\
        \ = (int**)malloc((m + 1) * sizeof(int*));\n    for (int i = 0; i <= m; i++)\
        \ {\n        dp[i] = (int*)malloc((n + 1) * sizeof(int));\n        for (int\
        \ j = 0; j <= n; j++) {\n            dp[i][j] = 0;\n        }\n    }\n\n   \
        \ for (int k = 0; k < strsSize; k++) {\n        int zeros, ones;\n        countZerosOnes(strs[k],\
        \ &zeros, &ones);\n\n        // Iterate backwards to ensure each string is used\
        \ at most once (0/1 knapsack)\n        for (int i = m; i >= zeros; i--) {\n\
        \            for (int j = n; j >= ones; j--) {\n                dp[i][j] = (dp[i][j]\
        \ > dp[i - zeros][j - ones] + 1) ? dp[i][j] : dp[i - zeros][j - ones] + 1;\n\
        \            }\n        }\n    }\n\n    int result = dp[m][n];\n\n    // Free\
        \ allocated memory\n    for (int i = 0; i <= m; i++) {\n        free(dp[i]);\n\
        \    }\n    free(dp);\n\n    return result;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int FindMaxForm(string[] strs, int m, int n) {\n        int[,]\
        \ dp = new int[m + 1, n + 1];\n\n        foreach (string s in strs) {\n    \
        \        int zeros = 0;\n            int ones = 0;\n            foreach (char\
        \ c in s) {\n                if (c == '0') {\n                    zeros++;\n\
        \                } else {\n                    ones++;\n                }\n\
        \            }\n\n            for (int i = m; i >= zeros; i--) {\n         \
        \       for (int j = n; j >= ones; j--) {\n                    dp[i, j] = Math.Max(dp[i,\
        \ j], dp[i - zeros, j - ones] + 1);\n                }\n            }\n    \
        \    }\n\n        return dp[m, n];\n    }\n}"
      javascript: "/**\n * @param {string[]} strs\n * @param {number} m\n * @param {number}\
        \ n\n * @return {number}\n */\nvar findMaxForm = function(strs, m, n) {\n  \
        \  let dp = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));\n\n    for\
        \ (let s of strs) {\n        let zeros = 0;\n        let ones = 0;\n       \
        \ for (let char of s) {\n            if (char === '0') {\n                zeros++;\n\
        \            } else {\n                ones++;\n            }\n        }\n\n\
        \        for (let i = m; i >= zeros; i--) {\n            for (let j = n; j >=\
        \ ones; j--) {\n                dp[i][j] = Math.max(dp[i][j], dp[i - zeros][j\
        \ - ones] + 1);\n            }\n        }\n    }\n\n    return dp[m][n];\n};"
      typescript: "function findMaxForm(strs: string[], m: number, n: number): number\
        \ {\n    let dp: number[][] = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));\n\
        \n    for (let s of strs) {\n        let zeros = 0;\n        let ones = 0;\n\
        \        for (let char of s) {\n            if (char === '0') {\n          \
        \      zeros++;\n            } else {\n                ones++;\n           \
        \ }\n        }\n\n        for (let i = m; i >= zeros; i--) {\n            for\
        \ (let j = n; j >= ones; j--) {\n                dp[i][j] = Math.max(dp[i][j],\
        \ dp[i - zeros][j - ones] + 1);\n            }\n        }\n    }\n\n    return\
        \ dp[m][n];\n};"
      php: "class Solution {\n\n    /**\n     * @param String[] $strs\n     * @param\
        \ Integer $m\n     * @param Integer $n\n     * @return Integer\n     */\n  \
        \  function findMaxForm($strs, $m, $n) {\n        $dp = array_fill(0, $m + 1,\
        \ array_fill(0, $n + 1, 0));\n\n        foreach ($strs as $s) {\n          \
        \  $zeros = 0;\n            $ones = 0;\n            for ($k = 0; $k < strlen($s);\
        \ $k++) {\n                if ($s[$k] == '0') {\n                    $zeros++;\n\
        \                } else {\n                    $ones++;\n                }\n\
        \            }\n\n            for ($i = $m; $i >= $zeros; $i--) {\n        \
        \        for ($j = $n; $j >= $ones; $j--) {\n                    $dp[$i][$j]\
        \ = max($dp[$i][$j], $dp[$i - $zeros][$j - $ones] + 1);\n                }\n\
        \            }\n        }\n\n        return $dp[$m][$n];\n    }\n}"
      swift: "class Solution {\n    func findMaxForm(_ strs: [String], _ m: Int, _ n:\
        \ Int) -> Int {\n        var dp = Array(repeating: Array(repeating: 0, count:\
        \ n + 1), count: m + 1)\n\n        for s in strs {\n            var zeros =\
        \ 0\n            var ones = 0\n            for char in s {\n               \
        \ if char == \"0\" {\n                    zeros += 1\n                } else\
        \ {\n                    ones += 1\n                }\n            }\n\n   \
        \         for i in (zeros...m).reversed() {\n                for j in (ones...n).reversed()\
        \ {\n                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] +\
        \ 1)\n                }\n            }\n        }\n\n        return dp[m][n]\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun findMaxForm(strs: Array<String>, m: Int, n:\
        \ Int): Int {\n        val dp = Array(m + 1) { IntArray(n + 1) { 0 } }\n\n \
        \       for (s in strs) {\n            var zeros = 0\n            var ones =\
        \ 0\n            for (char in s) {\n                if (char == '0') {\n   \
        \                 zeros++\n                } else {\n                    ones++\n\
        \                }\n            }\n\n            for (i in m downTo zeros) {\n\
        \                for (j in n downTo ones) {\n                    dp[i][j] =\
        \ Math.max(dp[i][j], dp[i - zeros][j - ones] + 1)\n                }\n     \
        \       }\n        }\n\n        return dp[m][n]\n    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int findMaxForm(List<String>\
        \ strs, int m, int n) {\n    List<List<int>> dp = List.generate(m + 1, (_) =>\
        \ List.filled(n + 1, 0));\n\n    for (String s in strs) {\n      int zeros =\
        \ 0;\n      int ones = 0;\n      for (int i = 0; i < s.length; i++) {\n    \
        \    if (s[i] == '0') {\n          zeros++;\n        } else {\n          ones++;\n\
        \        }\n      }\n\n      for (int i = m; i >= zeros; i--) {\n        for\
        \ (int j = n; j >= ones; j--) {\n          dp[i][j] = max(dp[i][j], dp[i - zeros][j\
        \ - ones] + 1);\n        }\n      }\n    }\n\n    return dp[m][n];\n  }\n}"
      go: "package main\n\nimport \"strings\"\nimport \"math\"\n\nfunc findMaxForm(strs\
        \ []string, m int, n int) int {\n    dp := make([][]int, m + 1)\n    for i :=\
        \ range dp {\n        dp[i] = make([]int, n + 1)\n    }\n\n    for _, s := range\
        \ strs {\n        zeros := strings.Count(s, \"0\")\n        ones := strings.Count(s,\
        \ \"1\")\n\n        for i := m; i >= zeros; i-- {\n            for j := n; j\
        \ >= ones; j-- {\n                dp[i][j] = int(math.Max(float64(dp[i][j]),\
        \ float64(dp[i - zeros][j - ones] + 1)))\n            }\n        }\n    }\n\n\
        \    return dp[m][n]\n}"
      ruby: "# @param {String[]} strs\n# @param {Integer} m\n# @param {Integer} n\n\
        # @return {Integer}\ndef find_max_form(strs, m, n)\n    dp = Array.new(m + 1)\
        \ { Array.new(n + 1, 0) }\n\n    strs.each do |s|\n        zeros = s.count('0')\n\
        \        ones = s.count('1')\n\n        m.downto(zeros) do |i|\n           \
        \ n.downto(ones) do |j|\n                dp[i][j] = [dp[i][j], dp[i - zeros][j\
        \ - ones] + 1].max\n            end\n        end\n    end\n\n    dp[m][n]\n\
        end"
      scala: "import scala.collection.mutable.ArrayBuffer\n\nobject Solution {\n   \
        \ def findMaxForm(strs: Array[String], m: Int, n: Int): Int = {\n        val\
        \ dp = Array.ofDim[Int](m + 1, n + 1)\n\n        for (s <- strs) {\n       \
        \     var zeros = 0\n            var ones = 0\n            for (char <- s) {\n\
        \                if (char == '0') {\n                    zeros += 1\n      \
        \          } else {\n                    ones += 1\n                }\n    \
        \        }\n\n            for (i <- m to zeros by -1) {\n                for\
        \ (j <- n to ones by -1) {\n                    dp(i)(j) = math.max(dp(i)(j),\
        \ dp(i - zeros)(j - ones) + 1)\n                }\n            }\n        }\n\
        \n        dp(m)(n)\n    }\n}"
      rust: "use std::cmp;\n\nimpl Solution {\n    pub fn find_max_form(strs: Vec<String>,\
        \ m: i32, n: i32) -> i32 {\n        let m_usize = m as usize;\n        let n_usize\
        \ = n as usize;\n        let mut dp = vec![vec![0; n_usize + 1]; m_usize + 1];\n\
        \n        for s in strs {\n            let mut zeros = 0;\n            let mut\
        \ ones = 0;\n            for c in s.chars() {\n                if c == '0' {\n\
        \                    zeros += 1;\n                } else {\n               \
        \     ones += 1;\n                }\n            }\n\n            for i in (zeros..=m_usize).rev()\
        \ {\n                for j in (ones..=n_usize).rev() {\n                   \
        \ dp[i][j] = cmp::max(dp[i][j], dp[i - zeros][j - ones] + 1);\n            \
        \    }\n            }\n        }\n\n        dp[m_usize][n_usize]\n    }\n}"
      racket: "#lang racket\n\n(define (find-max-form strs m n)\n  (let ([dp (build-vector\
        \ (+ m 1) (lambda (i) (build-vector (+ n 1) (lambda (j) 0))))])\n    (for-each\n\
        \     (lambda (s)\n       (let-values ([(zeros ones)\n                     (let\
        \ loop ([idx 0] [z 0] [o 0])\n                       (if (= idx (string-length\
        \ s))\n                           (values z o)\n                           (case\
        \ (string-ref s idx)\n                             [#\\0 (loop (+ idx 1) (+\
        \ z 1) o)]\n                             [#\\1 (loop (+ idx 1) z (+ o 1))])))]))\n\
        \         (for ([i (in-range m (- zeros 1) -1)])\n           (for ([j (in-range\
        \ n (- ones 1) -1)])\n             (vector-set! (vector-ref dp i) j\n      \
        \                    (max (vector-ref (vector-ref dp i) j)\n               \
        \                (+ (vector-ref (vector-ref dp (- i zeros)) (- j ones)) 1)))))))\n\
        \     strs)\n    (vector-ref (vector-ref dp m) n)))"
      erlang: "-module(solution).\n-export([find_max_form/3]).\n\n% Helper to count\
        \ zeros and ones in a string\ncount_zeros_ones(S) ->\n    lists:foldl(\n   \
        \     fun(Char, {Zeros, Ones}) ->\n            case Char of\n              \
        \  $0 -> {Zeros + 1, Ones};\n                $1 -> {Zeros, Ones + 1}\n     \
        \       end\n        end,\n        {0, 0},\n        S\n    ).\n\nfind_max_form(Strs,\
        \ M, N) ->\n    % Initialize DP table as an array of arrays\n    InitialRow\
        \ = array:new([{size, N + 1}, {fixed, true}, {default, 0}]),\n    DP = array:new([{size,\
        \ M + 1}, {fixed, true}, {default, InitialRow}]),\n\n    FinalDP = lists:foldl(\n\
        \        fun(S, CurrentDP) ->\n            {Zeros, Ones} = count_zeros_ones(S),\n\
        \n            % Iterate M down to Zeros\n            lists:foldl(\n        \
        \        fun(I, AccDP_I) ->\n                    % Get the current row for I\n\
        \                    CurrentRow_I = array:get(I, AccDP_I),\n\n             \
        \       % Iterate N down to Ones for this row\n                    NewRow_I\
        \ = lists:foldl(\n                        fun(J, AccRow_J) ->\n            \
        \                % dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)\n \
        \                           Val = array:get(J, AccRow_J),\n\n              \
        \              PrevRow = array:get(I - Zeros, AccDP_I),\n                  \
        \          PrevVal = array:get(J - Ones, PrevRow),\n\n                     \
        \       NewVal = max(Val, PrevVal + 1),\n                            array:set(J,\
        \ NewVal, AccRow_J)\n                        end,\n                        CurrentRow_I,\
        \ % Start with the current row\n                        lists:seq(N, Ones, -1)\n\
        \                    ),\n                    array:set(I, NewRow_I, AccDP_I)\n\
        \                end,\n                CurrentDP,\n                lists:seq(M,\
        \ Zeros, -1)\n            )\n        end,\n        DP,\n        Strs\n    ),\n\
        \n    % Result is at FinalDP[M][N]\n    array:get(N, array:get(M, FinalDP))."
      elixir: "defmodule Solution do\n  @spec find_max_form(strs :: [String.t()], m\
        \ :: integer, n :: integer) :: integer\n  def find_max_form(strs, m, n) do\n\
        \    dp = Map.new(for i <- 0..m, j <- 0..n, do: {{i, j}, 0})\n\n    Enum.reduce(strs,\
        \ dp, fn s, current_dp ->\n      {zeros, ones} = count_zeros_ones(s)\n\n   \
        \   Enum.reduce(m..zeros, current_dp, fn i, dp_with_i ->\n        Enum.reduce(n..ones,\
        \ dp_with_i, fn j, dp_with_j ->\n          current_val = Map.get(dp_with_j,\
        \ {i, j}, 0)\n          prev_val = Map.get(dp_with_j, {i - zeros, j - ones},\
        \ 0)\n          new_val = max(current_val, prev_val + 1)\n          Map.put(dp_with_j,\
        \ {i, j}, new_val)\n        end)\n      end)\n    end)\n    |> Map.get({m, n})\n\
        \  end\n\n  defp count_zeros_ones(s) do\n    Enum.reduce(String.graphemes(s),\
        \ {0, 0}, fn\n      \"0\", {zeros, ones} -> {zeros + 1, ones}\n      \"1\",\
        \ {zeros, ones} -> {zeros, ones + 1}\n      _, acc -> acc\n    end)\n  end\n\
        end"
    approach: 'This problem is a variation of the 0/1 Knapsack problem, but with two
      constraints instead of one: the maximum number of zeros (m) and ones (n) allowed
      in the subset. We want to maximize the number of strings selected. We use dynamic
      programming to solve this. We define a 2D DP array, `dp[i][j]`, which represents
      the maximum number of strings that can be formed using at most `i` zeros and `j`
      ones. The DP table is initialized with all zeros, as initially no strings can
      be formed.'
    time_complexity: The time complexity is O(L * m * n), where L is the number of strings
      in `strs`, `m` is the maximum number of zeros allowed, and `n` is the maximum
      number of ones allowed. For each of the L strings, we iterate through the `m *
      n` states of the DP table. Counting zeros and ones for each string takes O(length
      of string), but since `strs[i].length` is at most 100, and `L` is at most 600,
      the dominant factor is the DP table iteration.
    space_complexity: The space complexity is O(m * n) for the `dp` table. This table
      stores `(m+1) * (n+1)` integer values to keep track of the maximum number of strings
      for all possible combinations of zeros and ones up to `m` and `n` respectively.
    elapsed_time: 56.575297594070435
    model: gemini-2.5-flash
    generated_at: '2025-11-24 23:29:47 '
  - solutions:
      cpp: "class Solution {\n    public:\n        int findMaxForm(vector<string>& strs,\
        \ int m, int n) {\n            vector<vector<int>> dp(m + 1, vector<int>(n +\
        \ 1, 0));\n            for (string s : strs) {\n                int zeros =\
        \ count(s.begin(), s.end(), '0');\n                int ones = s.size() - zeros;\n\
        \                for (int i = m; i >= zeros; i--) {\n                    for\
        \ (int j = n; j >= ones; j--) {\n                        dp[i][j] = max(dp[i][j],\
        \ dp[i - zeros][j - ones] + 1);\n                    }\n                }\n\
        \            }\n            return dp[m][n];\n        }\n    };"
      java: "class Solution {\npublic int findMaxForm(String[] strs, int m, int n) {\n\
        \    int[][] dp = new int[m + 1][n + 1];\n    for (String s : strs) {\n    \
        \    int zeros = 0, ones = 0;\n        for (char c : s.toCharArray()) {\n  \
        \          if (c == '0') zeros++;\n            else ones++;\n        }\n   \
        \     for (int i = m; i >= zeros; i--) {\n            for (int j = n; j >= ones;\
        \ j--) {\n                dp[i][j] = Math.max(dp[i][j], dp[i - zeros][j - ones]\
        \ + 1);\n            }\n        }\n    }\n    return dp[m][n];\n}\n}"
      python: "class Solution:\ndef findMaxForm(self, strs: List[str], m: int, n: int)\
        \ -> int:\n    dp = [[0] * (n + 1) for _ in range(m + 1)]\n    for s in strs:\n\
        \        zeros = s.count('0')\n        ones = len(s) - zeros\n        for i\
        \ in range(m, zeros - 1, -1):\n            for j in range(n, ones - 1, -1):\n\
        \                dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)\n   \
        \ return dp[m][n]"
      python3: "class Solution:\ndef findMaxForm(self, strs: List[str], m: int, n: int)\
        \ -> int:\n    dp = [[0] * (n + 1) for _ in range(m + 1)]\n    for s in strs:\n\
        \        zeros = s.count('0')\n        ones = len(s) - zeros\n        for i\
        \ in range(m, zeros - 1, -1):\n            for j in range(n, ones - 1, -1):\n\
        \                dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)\n   \
        \ return dp[m][n]"
      c: "#include <stdio.h>\n    #include <string.h>\n\n    int findMaxForm(char **\
        \ strs, int strsSize, int m, int n){\n        int dp[m + 1][n + 1] = {{0}};\n\
        \        for (int i = 0; i < strsSize; i++) {\n            int zeros = 0, ones\
        \ = 0;\n            for (int j = 0; j < strlen(strs[i]); j++) {\n          \
        \      if (strs[i][j] == '0') zeros++;\n                else ones++;\n     \
        \       }\n            for (int x = m; x >= zeros; x--) {\n                for\
        \ (int y = n; y >= ones; y--) {\n                    dp[x][y] = (dp[x][y] >\
        \ dp[x - zeros][y - ones] + 1) ? dp[x][y] : dp[x - zeros][y - ones] + 1;\n \
        \               }\n            }\n        }\n        return dp[m][n];\n    }"
      csharp: "public class Solution {\npublic int FindMaxForm(string[] strs, int m,\
        \ int n) {\n    int[,] dp = new int[m + 1, n + 1];\n    foreach (string s in\
        \ strs) {\n        int zeros = 0, ones = 0;\n        foreach (char c in s) {\n\
        \            if (c == '0') zeros++;\n            else ones++;\n        }\n \
        \       for (int i = m; i >= zeros; i--) {\n            for (int j = n; j >=\
        \ ones; j--) {\n                dp[i, j] = Math.Max(dp[i, j], dp[i - zeros,\
        \ j - ones] + 1);\n            }\n        }\n    }\n    return dp[m, n];\n}\n\
        }"
      javascript: "var findMaxForm = function(strs, m, n) {\nlet dp = Array(m + 1).fill(0).map(()\
        \ => Array(n + 1).fill(0));\nfor (let s of strs) {\n    let zeros = 0, ones\
        \ = 0;\n    for (let c of s) {\n        if (c == '0') zeros++;\n        else\
        \ ones++;\n    }\n    for (let i = m; i >= zeros; i--) {\n        for (let j\
        \ = n; j >= ones; j--) {\n            dp[i][j] = Math.max(dp[i][j], dp[i - zeros][j\
        \ - ones] + 1);\n        }\n    }\n}\nreturn dp[m][n];\n};"
      typescript: "function findMaxForm(strs: string[], m: number, n: number): number\
        \ {\nlet dp: number[][] = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));\n\
        for (let s of strs) {\n    let zeros: number = 0, ones: number = 0;\n    for\
        \ (let c of s) {\n        if (c == '0') zeros++;\n        else ones++;\n   \
        \ }\n    for (let i: number = m; i >= zeros; i--) {\n        for (let j: number\
        \ = n; j >= ones; j--) {\n            dp[i][j] = Math.max(dp[i][j], dp[i - zeros][j\
        \ - ones] + 1);\n        }\n    }\n}\nreturn dp[m][n];\n}"
      php: "class Solution {\nfunction findMaxForm($strs, $m, $n) {\n    $dp = array_fill(0,\
        \ $m + 1, array_fill(0, $n + 1, 0));\n    foreach ($strs as $s) {\n        $zeros\
        \ = 0; $ones = 0;\n        for ($i = 0; $i < strlen($s); $i++) {\n         \
        \   if ($s[$i] == '0') $zeros++;\n            else $ones++;\n        }\n   \
        \     for ($i = $m; $i >= $zeros; $i--) {\n            for ($j = $n; $j >= $ones;\
        \ $j--) {\n                $dp[$i][$j] = max($dp[$i][$j], $dp[$i - $zeros][$j\
        \ - $ones] + 1);\n            }\n        }\n    }\n    return $dp[$m][$n];\n\
        }\n}"
      swift: "class Solution {\nfunc findMaxForm(_ strs: [String], _ m: Int, _ n: Int)\
        \ -> Int {\n    var dp = Array(repeating: Array(repeating: 0, count: n + 1),\
        \ count: m + 1)\n    for s in strs {\n        var zeros = 0, ones = 0\n    \
        \    for c in s {\n            if c == \"0\" {\n                zeros += 1\n\
        \            } else {\n                ones += 1\n            }\n        }\n\
        \        for i in stride(from: m, to: zeros - 1, by: -1) {\n            for\
        \ j in stride(from: n, to: ones - 1, by: -1) {\n                dp[i][j] = max(dp[i][j],\
        \ dp[i - zeros][j - ones] + 1)\n            }\n        }\n    }\n    return\
        \ dp[m][n]\n}\n}"
      kotlin: "class Solution {\nfun findMaxForm(strs: Array<String>, m: Int, n: Int):\
        \ Int {\n    val dp = Array(m + 1) { IntArray(n + 1) }\n    for (s in strs)\
        \ {\n        var zeros = 0\n        var ones = 0\n        for (c in s) {\n \
        \           if (c == '0') zeros++ else ones++\n        }\n        for (i in\
        \ m downTo zeros) {\n            for (j in n downTo ones) {\n              \
        \  dp[i][j] = maxOf(dp[i][j], dp[i - zeros][j - ones] + 1)\n            }\n\
        \        }\n    }\n    return dp[m][n]\n}\n}"
      dart: "class Solution {\nint findMaxForm(List<String> strs, int m, int n) {\n\
        \    List<List<int>> dp = List.generate(m + 1, (i) => List.generate(n + 1, (j)\
        \ => 0));\n    for (String s in strs) {\n        int zeros = 0, ones = 0;\n\
        \        for (String c in s.split('')) {\n            if (c == '0') zeros++;\n\
        \            else ones++;\n        }\n        for (int i = m; i >= zeros; i--)\
        \ {\n            for (int j = n; j >= ones; j--) {\n                dp[i][j]\
        \ = max(dp[i][j], dp[i - zeros][j - ones] + 1);\n            }\n        }\n\
        \    }\n    return dp[m][n];\n}\n}"
      go: "func findMaxForm(strs []string, m int, n int) int {\ndp := make([][]int,\
        \ m + 1)\nfor i := range dp {\n    dp[i] = make([]int, n + 1)\n}\nfor _, s :=\
        \ range strs {\n    zeros, ones := 0, 0\n    for _, c := range s {\n       \
        \ if c == '0' {\n            zeros++\n        } else {\n            ones++\n\
        \        }\n    }\n    for i := m; i >= zeros; i-- {\n        for j := n; j\
        \ >= ones; j-- {\n            dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones]\
        \ + 1)\n        }\n    }\n}\nreturn dp[m][n]\n}\n\nfunc max(a, b int) int {\n\
        if a > b {\n    return a\n}\nreturn b\n}"
      ruby: "# @param {String[]} strs\n    # @param {Integer} m\n    # @param {Integer}\
        \ n\n    # @return {Integer}\n    def find_max_form(strs, m, n)\n        dp\
        \ = Array.new(m + 1) { Array.new(n + 1, 0) }\n        strs.each do |s|\n   \
        \         zeros, ones = 0, 0\n            s.each_char do |c|\n             \
        \   if c == '0'\n                    zeros += 1\n                else\n    \
        \                ones += 1\n                end\n            end\n         \
        \   (m - zeros).downto(0) do |i|\n                (n - ones).downto(0) do |j|\n\
        \                    dp[i + zeros][j + ones] = [dp[i + zeros][j + ones], dp[i][j]\
        \ + 1].max\n                end\n            end\n        end\n        dp[m][n]\n\
        \    end"
      scala: "object Solution {\ndef findMaxForm(strs: Array[String], m: Int, n: Int):\
        \ Int = {\n    val dp = Array.ofDim[Int](m + 1, n + 1)\n    for (s <- strs)\
        \ {\n        var zeros = 0\n        var ones = 0\n        for (c <- s) {\n \
        \           if (c == '0') zeros += 1\n            else ones += 1\n        }\n\
        \        for (i <- m to zeros by -1) {\n            for (j <- n to ones by -1)\
        \ {\n                dp(i)(j) = math.max(dp(i)(j), dp(i - zeros)(j - ones) +\
        \ 1)\n            }\n        }\n    }\n    dp(m)(n)\n}\n}"
      rust: "impl Solution {\npub fn find_max_form(strs: Vec<String>, m: i32, n: i32)\
        \ -> i32 {\n    let m = m as usize;\n    let n = n as usize;\n    let mut dp\
        \ = vec![vec![0; n + 1]; m + 1];\n    for s in strs {\n        let mut zeros\
        \ = 0;\n        let mut ones = 0;\n        for c in s.chars() {\n          \
        \  if c == '0' {\n                zeros += 1;\n            } else {\n      \
        \          ones += 1;\n            }\n        }\n        for i in (zeros..=m).rev()\
        \ {\n            for j in (ones..=n).rev() {\n                dp[i][j] = dp[i][j].max(dp[i\
        \ - zeros][j - ones] + 1);\n            }\n        }\n    }\n    dp[m][n] as\
        \ i32\n}\n}"
      racket: "#lang racket\n    (define (find-max-form strs m n)\n        (let ((dp\
        \ (make-vector (add1 m) (make-vector (add1 n) 0))))\n            (for-each\n\
        \                (λ (s)\n                    (let ((zeros 0) (ones 0))\n   \
        \                     (for-each\n                            (λ (c)\n      \
        \                          (if (eq? c #\\0)\n                              \
        \      (set! zeros (add1 zeros))\n                                    (set!\
        \ ones (add1 ones))))\n                            (string->list s))\n     \
        \                   (for ((i (range (add1 m) zeros -1 -1)))\n              \
        \              (for ((j (range (add1 n) ones -1 -1)))\n                    \
        \            (vector-set! (vector-ref dp i) j\n                            \
        \        (max (vector-ref (vector-ref dp i) j)\n                           \
        \             (add1 (vector-ref (vector-ref dp (- i zeros)) (- j ones)))))))))\n\
        \                strs)\n            (vector-ref (vector-ref dp m) n)))"
      erlang: "-module(solution).\n    -export([find_max_form/3]).\n\n    find_max_form(Strs,\
        \ M, N) ->\n        DP = array:new([{size, M + 1}, {default, array:new([{size,\
        \ N + 1}, {default, 0}])}]),\n        lists:foldl(\n            fun(S, Dp) ->\n\
        \                {Zeros, Ones} = lists:foldl(\n                    fun(C, {Z,\
        \ O}) ->\n                        case C of\n                            $0\
        \ -> {Z + 1, O};\n                            $1 -> {Z, O + 1}\n           \
        \             end\n                    end, {0, 0}, S),\n                lists:foldl(\n\
        \                    fun(I, D) when I >= Zeros ->\n                        lists:foldl(\n\
        \                            fun(J, D1) when J >= Ones ->\n                \
        \                array:set(I, J, max(array:get(D1, I, J), array:get(D1, I -\
        \ Zeros, J - Ones) + 1), D1);\n                            (_, D1) -> D1\n \
        \                       end, D, lists:seq(0, N));\n                    (_, D)\
        \ -> D\n                end, Dp, lists:seq(0, M))\n            end, DP, Strs),\n\
        \        array:get(array:get(DP, M), N)."
      elixir: "defmodule Solution do\ndef find_max_form(strs, m, n) do\n    dp = Array.new(m\
        \ + 1, fn -> Array.new(n + 1, 0) end)\n    Enum.reduce(strs, dp, fn s, dp ->\n\
        \        zeros = Enum.count(String.graphemes(s), &(&1 == \"0\"))\n        ones\
        \ = String.length(s) - zeros\n        Enum.reduce(m..zeros, dp, fn i, dp ->\n\
        \            Enum.reduce(n..ones, dp, fn j, dp ->\n                array = dp\n\
        \                array = update_in(array, [i, j], fn x -> max(x, get_in(array,\
        \ [i - zeros, j - ones]) + 1) end)\n                array\n            end)\n\
        \        end)\n    end)\n    get_in(dp, [m, n])\nend\n\ndefp get_in(array, [i\
        \ | []]), do: array[i]\ndefp get_in(array, [i | rest]), do: get_in(array[i],\
        \ rest)\n\ndefp update_in(array, [i | []], fun), do: put_in(array, [i], fun.(array[i]))\n\
        defp update_in(array, [i | rest], fun), do: put_in(array, [i], update_in(array[i],\
        \ rest, fun))\n\ndefp put_in(array, [i | []], value), do: List.update_at(array,\
        \ i, fn _ -> value end)\ndefp put_in(array, [i | rest], value), do: List.update_at(array,\
        \ i, fn x -> put_in(x, rest, value) end)\nend"
    approach: 'The problem can be solved using dynamic programming. The idea is to create
      a 3D DP table where dp[i][m][n] represents the maximum number of strings that
      can be included in the subset using the first i strings and at most m 0''s and
      n 1''s. We iterate over each string and for each string, we calculate the number
      of 0''s and 1''s. Then we update the DP table by considering two cases: including
      the current string in the subset or not including it. The final answer will be
      stored in dp[strs.length][m][n]. The key intuition here is to use a bottom-up
      approach to build up the solution by considering all possible subsets of strings
      and their corresponding counts of 0''s and 1''s.


      The algorithm starts by initializing the DP table with zeros. Then it iterates
      over each string and updates the DP table accordingly. The time complexity of
      this approach is O(strs.length * m * n) and the space complexity is also O(strs.length
      * m * n). This approach ensures that we consider all possible subsets of strings
      and their corresponding counts of 0''s and 1''s, thus giving us the maximum number
      of strings that can be included in the subset with at most m 0''s and n 1''s.'
    time_complexity: 'The time complexity of this approach is O(strs.length * m * n)
      because we are using three nested loops to iterate over each string, each possible
      count of 0''s, and each possible count of 1''s. This ensures that we consider
      all possible subsets of strings and their corresponding counts of 0''s and 1''s,
      thus giving us the maximum number of strings that can be included in the subset
      with at most m 0''s and n 1''s.


      The space complexity of this approach is O(m * n) because we are using a 2D DP
      table to store the maximum number of strings that can be included in the subset
      for each possible count of 0''s and 1''s. However, in the given solutions, the
      space complexity is O(strs.length * m * n) due to the use of a 3D DP table in
      some languages. This is because some languages require a 3D DP table to store
      the maximum number of strings that can be included in the subset for each possible
      count of 0''s and 1''s and for each string.'
    space_complexity: The space complexity of this approach is O(m * n) because we are
      using a 2D DP table to store the maximum number of strings that can be included
      in the subset for each possible count of 0's and 1's. However, in the given solutions,
      the space complexity is O(strs.length * m * n) due to the use of a 3D DP table
      in some languages. This is because some languages require a 3D DP table to store
      the maximum number of strings that can be included in the subset for each possible
      count of 0's and 1's and for each string.
    elapsed_time: 11.909987211227417
    model: llama-3.3-70b-versatile
    generated_at: '2025-11-24 23:29:58 '
---

## Problem #474: Ones and Zeroes

**Difficulty:** Medium

**Topics:** Array, String, Dynamic Programming

## Problem Description

<p>You are given an array of binary strings <code>strs</code> and two integers <code>m</code> and <code>n</code>.</p>

<p>Return <em>the size of the largest subset of <code>strs</code> such that there are <strong>at most</strong> </em><code>m</code><em> </em><code>0</code><em>&#39;s and </em><code>n</code><em> </em><code>1</code><em>&#39;s in the subset</em>.</p>

<p>A set <code>x</code> is a <strong>subset</strong> of a set <code>y</code> if all elements of <code>x</code> are also elements of <code>y</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;10&quot;,&quot;0001&quot;,&quot;111001&quot;,&quot;1&quot;,&quot;0&quot;], m = 5, n = 3
<strong>Output:</strong> 4
<strong>Explanation:</strong> The largest subset with at most 5 0&#39;s and 3 1&#39;s is {&quot;10&quot;, &quot;0001&quot;, &quot;1&quot;, &quot;0&quot;}, so the answer is 4.
Other valid but smaller subsets include {&quot;0001&quot;, &quot;1&quot;} and {&quot;10&quot;, &quot;1&quot;, &quot;0&quot;}.
{&quot;111001&quot;} is an invalid subset because it contains 4 1&#39;s, greater than the maximum of 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;10&quot;,&quot;0&quot;,&quot;1&quot;], m = 1, n = 1
<strong>Output:</strong> 2
<b>Explanation:</b> The largest subset is {&quot;0&quot;, &quot;1&quot;}, so the answer is 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 600</code></li>
	<li><code>1 &lt;= strs[i].length &lt;= 100</code></li>
	<li><code>strs[i]</code> consists only of digits <code>&#39;0&#39;</code> and <code>&#39;1&#39;</code>.</li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
</ul>


## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-24 23:29:47 )</small>
</summary>

<div class="ai-solution-content">

### Approach

This problem is a variation of the 0/1 Knapsack problem, but with two constraints instead of one: the maximum number of zeros (m) and ones (n) allowed in the subset. We want to maximize the number of strings selected. We use dynamic programming to solve this. We define a 2D DP array, `dp[i][j]`, which represents the maximum number of strings that can be formed using at most `i` zeros and `j` ones. The DP table is initialized with all zeros, as initially no strings can be formed.

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
    int findMaxForm(std::vector<std::string>& strs, int m, int n) {
        std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, 0));

        for (const std::string& s : strs) {
            int zeros = 0;
            int ones = 0;
            for (char c : s) {
                if (c == '0') {
                    zeros++;
                } else {
                    ones++;
                }
            }

            for (int i = m; i >= zeros; --i) {
                for (int j = n; j >= ones; --j) {
                    dp[i][j] = std::max(dp[i][j], dp[i - zeros][j - ones] + 1);
                }
            }
        }

        return dp[m][n];
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.Arrays;

class Solution {
    public int findMaxForm(String[] strs, int m, int n) {
        int[][] dp = new int[m + 1][n + 1];

        for (String s : strs) {
            int zeros = 0;
            int ones = 0;
            for (char c : s.toCharArray()) {
                if (c == '0') {
                    zeros++;
                } else {
                    ones++;
                }
            }

            for (int i = m; i >= zeros; i--) {
                for (int j = n; j >= ones; j--) {
                    dp[i][j] = Math.max(dp[i][j], dp[i - zeros][j - ones] + 1);
                }
            }
        }

        return dp[m][n];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')

            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

        return dp[m][n]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')

            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

        return dp[m][n]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

// Helper function to count zeros and ones
void countZerosOnes(const char* s, int* zeros, int* ones) {
    *zeros = 0;
    *ones = 0;
    for (int k = 0; s[k] != '\0'; k++) {
        if (s[k] == '0') {
            (*zeros)++;
        } else {
            (*ones)++;
        }
    }
}

int findMaxForm(char ** strs, int strsSize, int m, int n){
    // dp[i][j] stores the maximum number of strings that can be formed
    // using at most i zeros and j ones.
    int** dp = (int**)malloc((m + 1) * sizeof(int*));
    for (int i = 0; i <= m; i++) {
        dp[i] = (int*)malloc((n + 1) * sizeof(int));
        for (int j = 0; j <= n; j++) {
            dp[i][j] = 0;
        }
    }

    for (int k = 0; k < strsSize; k++) {
        int zeros, ones;
        countZerosOnes(strs[k], &zeros, &ones);

        // Iterate backwards to ensure each string is used at most once (0/1 knapsack)
        for (int i = m; i >= zeros; i--) {
            for (int j = n; j >= ones; j--) {
                dp[i][j] = (dp[i][j] > dp[i - zeros][j - ones] + 1) ? dp[i][j] : dp[i - zeros][j - ones] + 1;
            }
        }
    }

    int result = dp[m][n];

    // Free allocated memory
    for (int i = 0; i <= m; i++) {
        free(dp[i]);
    }
    free(dp);

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
    public int FindMaxForm(string[] strs, int m, int n) {
        int[,] dp = new int[m + 1, n + 1];

        foreach (string s in strs) {
            int zeros = 0;
            int ones = 0;
            foreach (char c in s) {
                if (c == '0') {
                    zeros++;
                } else {
                    ones++;
                }
            }

            for (int i = m; i >= zeros; i--) {
                for (int j = n; j >= ones; j--) {
                    dp[i, j] = Math.Max(dp[i, j], dp[i - zeros, j - ones] + 1);
                }
            }
        }

        return dp[m, n];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string[]} strs
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var findMaxForm = function(strs, m, n) {
    let dp = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));

    for (let s of strs) {
        let zeros = 0;
        let ones = 0;
        for (let char of s) {
            if (char === '0') {
                zeros++;
            } else {
                ones++;
            }
        }

        for (let i = m; i >= zeros; i--) {
            for (let j = n; j >= ones; j--) {
                dp[i][j] = Math.max(dp[i][j], dp[i - zeros][j - ones] + 1);
            }
        }
    }

    return dp[m][n];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function findMaxForm(strs: string[], m: number, n: number): number {
    let dp: number[][] = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));

    for (let s of strs) {
        let zeros = 0;
        let ones = 0;
        for (let char of s) {
            if (char === '0') {
                zeros++;
            } else {
                ones++;
            }
        }

        for (let i = m; i >= zeros; i--) {
            for (let j = n; j >= ones; j--) {
                dp[i][j] = Math.max(dp[i][j], dp[i - zeros][j - ones] + 1);
            }
        }
    }

    return dp[m][n];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String[] $strs
     * @param Integer $m
     * @param Integer $n
     * @return Integer
     */
    function findMaxForm($strs, $m, $n) {
        $dp = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));

        foreach ($strs as $s) {
            $zeros = 0;
            $ones = 0;
            for ($k = 0; $k < strlen($s); $k++) {
                if ($s[$k] == '0') {
                    $zeros++;
                } else {
                    $ones++;
                }
            }

            for ($i = $m; $i >= $zeros; $i--) {
                for ($j = $n; $j >= $ones; $j--) {
                    $dp[$i][$j] = max($dp[$i][$j], $dp[$i - $zeros][$j - $ones] + 1);
                }
            }
        }

        return $dp[$m][$n];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func findMaxForm(_ strs: [String], _ m: Int, _ n: Int) -> Int {
        var dp = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)

        for s in strs {
            var zeros = 0
            var ones = 0
            for char in s {
                if char == "0" {
                    zeros += 1
                } else {
                    ones += 1
                }
            }

            for i in (zeros...m).reversed() {
                for j in (ones...n).reversed() {
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
                }
            }
        }

        return dp[m][n]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun findMaxForm(strs: Array<String>, m: Int, n: Int): Int {
        val dp = Array(m + 1) { IntArray(n + 1) { 0 } }

        for (s in strs) {
            var zeros = 0
            var ones = 0
            for (char in s) {
                if (char == '0') {
                    zeros++
                } else {
                    ones++
                }
            }

            for (i in m downTo zeros) {
                for (j in n downTo ones) {
                    dp[i][j] = Math.max(dp[i][j], dp[i - zeros][j - ones] + 1)
                }
            }
        }

        return dp[m][n]
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
  int findMaxForm(List<String> strs, int m, int n) {
    List<List<int>> dp = List.generate(m + 1, (_) => List.filled(n + 1, 0));

    for (String s in strs) {
      int zeros = 0;
      int ones = 0;
      for (int i = 0; i < s.length; i++) {
        if (s[i] == '0') {
          zeros++;
        } else {
          ones++;
        }
      }

      for (int i = m; i >= zeros; i--) {
        for (int j = n; j >= ones; j--) {
          dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1);
        }
      }
    }

    return dp[m][n];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

import "strings"
import "math"

func findMaxForm(strs []string, m int, n int) int {
    dp := make([][]int, m + 1)
    for i := range dp {
        dp[i] = make([]int, n + 1)
    }

    for _, s := range strs {
        zeros := strings.Count(s, "0")
        ones := strings.Count(s, "1")

        for i := m; i >= zeros; i-- {
            for j := n; j >= ones; j-- {
                dp[i][j] = int(math.Max(float64(dp[i][j]), float64(dp[i - zeros][j - ones] + 1)))
            }
        }
    }

    return dp[m][n]
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String[]} strs
# @param {Integer} m
# @param {Integer} n
# @return {Integer}
def find_max_form(strs, m, n)
    dp = Array.new(m + 1) { Array.new(n + 1, 0) }

    strs.each do |s|
        zeros = s.count('0')
        ones = s.count('1')

        m.downto(zeros) do |i|
            n.downto(ones) do |j|
                dp[i][j] = [dp[i][j], dp[i - zeros][j - ones] + 1].max
            end
        end
    end

    dp[m][n]
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable.ArrayBuffer

object Solution {
    def findMaxForm(strs: Array[String], m: Int, n: Int): Int = {
        val dp = Array.ofDim[Int](m + 1, n + 1)

        for (s <- strs) {
            var zeros = 0
            var ones = 0
            for (char <- s) {
                if (char == '0') {
                    zeros += 1
                } else {
                    ones += 1
                }
            }

            for (i <- m to zeros by -1) {
                for (j <- n to ones by -1) {
                    dp(i)(j) = math.max(dp(i)(j), dp(i - zeros)(j - ones) + 1)
                }
            }
        }

        dp(m)(n)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::cmp;

impl Solution {
    pub fn find_max_form(strs: Vec<String>, m: i32, n: i32) -> i32 {
        let m_usize = m as usize;
        let n_usize = n as usize;
        let mut dp = vec![vec![0; n_usize + 1]; m_usize + 1];

        for s in strs {
            let mut zeros = 0;
            let mut ones = 0;
            for c in s.chars() {
                if c == '0' {
                    zeros += 1;
                } else {
                    ones += 1;
                }
            }

            for i in (zeros..=m_usize).rev() {
                for j in (ones..=n_usize).rev() {
                    dp[i][j] = cmp::max(dp[i][j], dp[i - zeros][j - ones] + 1);
                }
            }
        }

        dp[m_usize][n_usize]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (find-max-form strs m n)
  (let ([dp (build-vector (+ m 1) (lambda (i) (build-vector (+ n 1) (lambda (j) 0))))])
    (for-each
     (lambda (s)
       (let-values ([(zeros ones)
                     (let loop ([idx 0] [z 0] [o 0])
                       (if (= idx (string-length s))
                           (values z o)
                           (case (string-ref s idx)
                             [#\0 (loop (+ idx 1) (+ z 1) o)]
                             [#\1 (loop (+ idx 1) z (+ o 1))])))]))
         (for ([i (in-range m (- zeros 1) -1)])
           (for ([j (in-range n (- ones 1) -1)])
             (vector-set! (vector-ref dp i) j
                          (max (vector-ref (vector-ref dp i) j)
                               (+ (vector-ref (vector-ref dp (- i zeros)) (- j ones)) 1)))))))
     strs)
    (vector-ref (vector-ref dp m) n)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([find_max_form/3]).

% Helper to count zeros and ones in a string
count_zeros_ones(S) ->
    lists:foldl(
        fun(Char, {Zeros, Ones}) ->
            case Char of
                $0 -> {Zeros + 1, Ones};
                $1 -> {Zeros, Ones + 1}
            end
        end,
        {0, 0},
        S
    ).

find_max_form(Strs, M, N) ->
    % Initialize DP table as an array of arrays
    InitialRow = array:new([{size, N + 1}, {fixed, true}, {default, 0}]),
    DP = array:new([{size, M + 1}, {fixed, true}, {default, InitialRow}]),

    FinalDP = lists:foldl(
        fun(S, CurrentDP) ->
            {Zeros, Ones} = count_zeros_ones(S),

            % Iterate M down to Zeros
            lists:foldl(
                fun(I, AccDP_I) ->
                    % Get the current row for I
                    CurrentRow_I = array:get(I, AccDP_I),

                    % Iterate N down to Ones for this row
                    NewRow_I = lists:foldl(
                        fun(J, AccRow_J) ->
                            % dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
                            Val = array:get(J, AccRow_J),

                            PrevRow = array:get(I - Zeros, AccDP_I),
                            PrevVal = array:get(J - Ones, PrevRow),

                            NewVal = max(Val, PrevVal + 1),
                            array:set(J, NewVal, AccRow_J)
                        end,
                        CurrentRow_I, % Start with the current row
                        lists:seq(N, Ones, -1)
                    ),
                    array:set(I, NewRow_I, AccDP_I)
                end,
                CurrentDP,
                lists:seq(M, Zeros, -1)
            )
        end,
        DP,
        Strs
    ),

    % Result is at FinalDP[M][N]
    array:get(N, array:get(M, FinalDP)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec find_max_form(strs :: [String.t()], m :: integer, n :: integer) :: integer
  def find_max_form(strs, m, n) do
    dp = Map.new(for i <- 0..m, j <- 0..n, do: {{i, j}, 0})

    Enum.reduce(strs, dp, fn s, current_dp ->
      {zeros, ones} = count_zeros_ones(s)

      Enum.reduce(m..zeros, current_dp, fn i, dp_with_i ->
        Enum.reduce(n..ones, dp_with_i, fn j, dp_with_j ->
          current_val = Map.get(dp_with_j, {i, j}, 0)
          prev_val = Map.get(dp_with_j, {i - zeros, j - ones}, 0)
          new_val = max(current_val, prev_val + 1)
          Map.put(dp_with_j, {i, j}, new_val)
        end)
      end)
    end)
    |> Map.get({m, n})
  end

  defp count_zeros_ones(s) do
    Enum.reduce(String.graphemes(s), {0, 0}, fn
      "0", {zeros, ones} -> {zeros + 1, ones}
      "1", {zeros, ones} -> {zeros, ones + 1}
      _, acc -> acc
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(L * m * n), where L is the number of strings in `strs`, `m` is the maximum number of zeros allowed, and `n` is the maximum number of ones allowed. For each of the L strings, we iterate through the `m * n` states of the DP table. Counting zeros and ones for each string takes O(length of string), but since `strs[i].length` is at most 100, and `L` is at most 600, the dominant factor is the DP table iteration.

- **Space Complexity:** The space complexity is O(m * n) for the `dp` table. This table stores `(m+1) * (n+1)` integer values to keep track of the maximum number of strings for all possible combinations of zeros and ones up to `m` and `n` respectively.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-24 23:29:58 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved using dynamic programming. The idea is to create a 3D DP table where dp[i][m][n] represents the maximum number of strings that can be included in the subset using the first i strings and at most m 0's and n 1's. We iterate over each string and for each string, we calculate the number of 0's and 1's. Then we update the DP table by considering two cases: including the current string in the subset or not including it. The final answer will be stored in dp[strs.length][m][n]. The key intuition here is to use a bottom-up approach to build up the solution by considering all possible subsets of strings and their corresponding counts of 0's and 1's.

The algorithm starts by initializing the DP table with zeros. Then it iterates over each string and updates the DP table accordingly. The time complexity of this approach is O(strs.length * m * n) and the space complexity is also O(strs.length * m * n). This approach ensures that we consider all possible subsets of strings and their corresponding counts of 0's and 1's, thus giving us the maximum number of strings that can be included in the subset with at most m 0's and n 1's.

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
        int findMaxForm(vector<string>& strs, int m, int n) {
            vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
            for (string s : strs) {
                int zeros = count(s.begin(), s.end(), '0');
                int ones = s.size() - zeros;
                for (int i = m; i >= zeros; i--) {
                    for (int j = n; j >= ones; j--) {
                        dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1);
                    }
                }
            }
            return dp[m][n];
        }
    };
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
public int findMaxForm(String[] strs, int m, int n) {
    int[][] dp = new int[m + 1][n + 1];
    for (String s : strs) {
        int zeros = 0, ones = 0;
        for (char c : s.toCharArray()) {
            if (c == '0') zeros++;
            else ones++;
        }
        for (int i = m; i >= zeros; i--) {
            for (int j = n; j >= ones; j--) {
                dp[i][j] = Math.max(dp[i][j], dp[i - zeros][j - ones] + 1);
            }
        }
    }
    return dp[m][n];
}
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for s in strs:
        zeros = s.count('0')
        ones = len(s) - zeros
        for i in range(m, zeros - 1, -1):
            for j in range(n, ones - 1, -1):
                dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
    return dp[m][n]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for s in strs:
        zeros = s.count('0')
        ones = len(s) - zeros
        for i in range(m, zeros - 1, -1):
            for j in range(n, ones - 1, -1):
                dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
    return dp[m][n]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
    #include <string.h>

    int findMaxForm(char ** strs, int strsSize, int m, int n){
        int dp[m + 1][n + 1] = {{0}};
        for (int i = 0; i < strsSize; i++) {
            int zeros = 0, ones = 0;
            for (int j = 0; j < strlen(strs[i]); j++) {
                if (strs[i][j] == '0') zeros++;
                else ones++;
            }
            for (int x = m; x >= zeros; x--) {
                for (int y = n; y >= ones; y--) {
                    dp[x][y] = (dp[x][y] > dp[x - zeros][y - ones] + 1) ? dp[x][y] : dp[x - zeros][y - ones] + 1;
                }
            }
        }
        return dp[m][n];
    }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
public int FindMaxForm(string[] strs, int m, int n) {
    int[,] dp = new int[m + 1, n + 1];
    foreach (string s in strs) {
        int zeros = 0, ones = 0;
        foreach (char c in s) {
            if (c == '0') zeros++;
            else ones++;
        }
        for (int i = m; i >= zeros; i--) {
            for (int j = n; j >= ones; j--) {
                dp[i, j] = Math.Max(dp[i, j], dp[i - zeros, j - ones] + 1);
            }
        }
    }
    return dp[m, n];
}
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var findMaxForm = function(strs, m, n) {
let dp = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));
for (let s of strs) {
    let zeros = 0, ones = 0;
    for (let c of s) {
        if (c == '0') zeros++;
        else ones++;
    }
    for (let i = m; i >= zeros; i--) {
        for (let j = n; j >= ones; j--) {
            dp[i][j] = Math.max(dp[i][j], dp[i - zeros][j - ones] + 1);
        }
    }
}
return dp[m][n];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function findMaxForm(strs: string[], m: number, n: number): number {
let dp: number[][] = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));
for (let s of strs) {
    let zeros: number = 0, ones: number = 0;
    for (let c of s) {
        if (c == '0') zeros++;
        else ones++;
    }
    for (let i: number = m; i >= zeros; i--) {
        for (let j: number = n; j >= ones; j--) {
            dp[i][j] = Math.max(dp[i][j], dp[i - zeros][j - ones] + 1);
        }
    }
}
return dp[m][n];
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
function findMaxForm($strs, $m, $n) {
    $dp = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));
    foreach ($strs as $s) {
        $zeros = 0; $ones = 0;
        for ($i = 0; $i < strlen($s); $i++) {
            if ($s[$i] == '0') $zeros++;
            else $ones++;
        }
        for ($i = $m; $i >= $zeros; $i--) {
            for ($j = $n; $j >= $ones; $j--) {
                $dp[$i][$j] = max($dp[$i][$j], $dp[$i - $zeros][$j - $ones] + 1);
            }
        }
    }
    return $dp[$m][$n];
}
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
func findMaxForm(_ strs: [String], _ m: Int, _ n: Int) -> Int {
    var dp = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)
    for s in strs {
        var zeros = 0, ones = 0
        for c in s {
            if c == "0" {
                zeros += 1
            } else {
                ones += 1
            }
        }
        for i in stride(from: m, to: zeros - 1, by: -1) {
            for j in stride(from: n, to: ones - 1, by: -1) {
                dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
            }
        }
    }
    return dp[m][n]
}
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
fun findMaxForm(strs: Array<String>, m: Int, n: Int): Int {
    val dp = Array(m + 1) { IntArray(n + 1) }
    for (s in strs) {
        var zeros = 0
        var ones = 0
        for (c in s) {
            if (c == '0') zeros++ else ones++
        }
        for (i in m downTo zeros) {
            for (j in n downTo ones) {
                dp[i][j] = maxOf(dp[i][j], dp[i - zeros][j - ones] + 1)
            }
        }
    }
    return dp[m][n]
}
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
int findMaxForm(List<String> strs, int m, int n) {
    List<List<int>> dp = List.generate(m + 1, (i) => List.generate(n + 1, (j) => 0));
    for (String s in strs) {
        int zeros = 0, ones = 0;
        for (String c in s.split('')) {
            if (c == '0') zeros++;
            else ones++;
        }
        for (int i = m; i >= zeros; i--) {
            for (int j = n; j >= ones; j--) {
                dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1);
            }
        }
    }
    return dp[m][n];
}
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func findMaxForm(strs []string, m int, n int) int {
dp := make([][]int, m + 1)
for i := range dp {
    dp[i] = make([]int, n + 1)
}
for _, s := range strs {
    zeros, ones := 0, 0
    for _, c := range s {
        if c == '0' {
            zeros++
        } else {
            ones++
        }
    }
    for i := m; i >= zeros; i-- {
        for j := n; j >= ones; j-- {
            dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        }
    }
}
return dp[m][n]
}

func max(a, b int) int {
if a > b {
    return a
}
return b
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String[]} strs
    # @param {Integer} m
    # @param {Integer} n
    # @return {Integer}
    def find_max_form(strs, m, n)
        dp = Array.new(m + 1) { Array.new(n + 1, 0) }
        strs.each do |s|
            zeros, ones = 0, 0
            s.each_char do |c|
                if c == '0'
                    zeros += 1
                else
                    ones += 1
                end
            end
            (m - zeros).downto(0) do |i|
                (n - ones).downto(0) do |j|
                    dp[i + zeros][j + ones] = [dp[i + zeros][j + ones], dp[i][j] + 1].max
                end
            end
        end
        dp[m][n]
    end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
def findMaxForm(strs: Array[String], m: Int, n: Int): Int = {
    val dp = Array.ofDim[Int](m + 1, n + 1)
    for (s <- strs) {
        var zeros = 0
        var ones = 0
        for (c <- s) {
            if (c == '0') zeros += 1
            else ones += 1
        }
        for (i <- m to zeros by -1) {
            for (j <- n to ones by -1) {
                dp(i)(j) = math.max(dp(i)(j), dp(i - zeros)(j - ones) + 1)
            }
        }
    }
    dp(m)(n)
}
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
pub fn find_max_form(strs: Vec<String>, m: i32, n: i32) -> i32 {
    let m = m as usize;
    let n = n as usize;
    let mut dp = vec![vec![0; n + 1]; m + 1];
    for s in strs {
        let mut zeros = 0;
        let mut ones = 0;
        for c in s.chars() {
            if c == '0' {
                zeros += 1;
            } else {
                ones += 1;
            }
        }
        for i in (zeros..=m).rev() {
            for j in (ones..=n).rev() {
                dp[i][j] = dp[i][j].max(dp[i - zeros][j - ones] + 1);
            }
        }
    }
    dp[m][n] as i32
}
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket
    (define (find-max-form strs m n)
        (let ((dp (make-vector (add1 m) (make-vector (add1 n) 0))))
            (for-each
                (λ (s)
                    (let ((zeros 0) (ones 0))
                        (for-each
                            (λ (c)
                                (if (eq? c #\0)
                                    (set! zeros (add1 zeros))
                                    (set! ones (add1 ones))))
                            (string->list s))
                        (for ((i (range (add1 m) zeros -1 -1)))
                            (for ((j (range (add1 n) ones -1 -1)))
                                (vector-set! (vector-ref dp i) j
                                    (max (vector-ref (vector-ref dp i) j)
                                        (add1 (vector-ref (vector-ref dp (- i zeros)) (- j ones)))))))))
                strs)
            (vector-ref (vector-ref dp m) n)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
    -export([find_max_form/3]).

    find_max_form(Strs, M, N) ->
        DP = array:new([{size, M + 1}, {default, array:new([{size, N + 1}, {default, 0}])}]),
        lists:foldl(
            fun(S, Dp) ->
                {Zeros, Ones} = lists:foldl(
                    fun(C, {Z, O}) ->
                        case C of
                            $0 -> {Z + 1, O};
                            $1 -> {Z, O + 1}
                        end
                    end, {0, 0}, S),
                lists:foldl(
                    fun(I, D) when I >= Zeros ->
                        lists:foldl(
                            fun(J, D1) when J >= Ones ->
                                array:set(I, J, max(array:get(D1, I, J), array:get(D1, I - Zeros, J - Ones) + 1), D1);
                            (_, D1) -> D1
                        end, D, lists:seq(0, N));
                    (_, D) -> D
                end, Dp, lists:seq(0, M))
            end, DP, Strs),
        array:get(array:get(DP, M), N).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
def find_max_form(strs, m, n) do
    dp = Array.new(m + 1, fn -> Array.new(n + 1, 0) end)
    Enum.reduce(strs, dp, fn s, dp ->
        zeros = Enum.count(String.graphemes(s), &(&1 == "0"))
        ones = String.length(s) - zeros
        Enum.reduce(m..zeros, dp, fn i, dp ->
            Enum.reduce(n..ones, dp, fn j, dp ->
                array = dp
                array = update_in(array, [i, j], fn x -> max(x, get_in(array, [i - zeros, j - ones]) + 1) end)
                array
            end)
        end)
    end)
    get_in(dp, [m, n])
end

defp get_in(array, [i | []]), do: array[i]
defp get_in(array, [i | rest]), do: get_in(array[i], rest)

defp update_in(array, [i | []], fun), do: put_in(array, [i], fun.(array[i]))
defp update_in(array, [i | rest], fun), do: put_in(array, [i], update_in(array[i], rest, fun))

defp put_in(array, [i | []], value), do: List.update_at(array, i, fn _ -> value end)
defp put_in(array, [i | rest], value), do: List.update_at(array, i, fn x -> put_in(x, rest, value) end)
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this approach is O(strs.length * m * n) because we are using three nested loops to iterate over each string, each possible count of 0's, and each possible count of 1's. This ensures that we consider all possible subsets of strings and their corresponding counts of 0's and 1's, thus giving us the maximum number of strings that can be included in the subset with at most m 0's and n 1's.

The space complexity of this approach is O(m * n) because we are using a 2D DP table to store the maximum number of strings that can be included in the subset for each possible count of 0's and 1's. However, in the given solutions, the space complexity is O(strs.length * m * n) due to the use of a 3D DP table in some languages. This is because some languages require a 3D DP table to store the maximum number of strings that can be included in the subset for each possible count of 0's and 1's and for each string.

- **Space Complexity:** The space complexity of this approach is O(m * n) because we are using a 2D DP table to store the maximum number of strings that can be included in the subset for each possible count of 0's and 1's. However, in the given solutions, the space complexity is O(strs.length * m * n) due to the use of a 3D DP table in some languages. This is because some languages require a 3D DP table to store the maximum number of strings that can be included in the subset for each possible count of 0's and 1's and for each string.

</div>
</details>
