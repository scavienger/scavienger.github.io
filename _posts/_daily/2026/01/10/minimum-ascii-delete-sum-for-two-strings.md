---
layout: post
title: "Minimum ASCII Delete Sum for Two Strings"
date: 2026-01-10 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Dynamic Programming"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minimumDeleteSum(string s1, string s2)\
        \ {\n        int m = s1.length();\n        int n = s2.length();\n\n        vector<vector<int>>\
        \ dp(m + 1, vector<int>(n + 1, 0));\n\n        // Base cases\n        // dp[i][0]:\
        \ delete all characters from s1[0...i-1] to match empty s2\n        for (int\
        \ i = 1; i <= m; ++i) {\n            dp[i][0] = dp[i-1][0] + (int)s1[i-1];\n\
        \        }\n        // dp[0][j]: delete all characters from s2[0...j-1] to match\
        \ empty s1\n        for (int j = 1; j <= n; ++j) {\n            dp[0][j] = dp[0][j-1]\
        \ + (int)s2[j-1];\n        }\n\n        // Fill the DP table\n        for (int\
        \ i = 1; i <= m; ++i) {\n            for (int j = 1; j <= n; ++j) {\n      \
        \          if (s1[i-1] == s2[j-1]) {\n                    dp[i][j] = dp[i-1][j-1];\n\
        \                } else {\n                    dp[i][j] = min(dp[i-1][j] + (int)s1[i-1],\
        \ // Delete s1[i-1]\n                                   dp[i][j-1] + (int)s2[j-1]);\
        \ // Delete s2[j-1]\n                }\n            }\n        }\n\n       \
        \ return dp[m][n];\n    }\n};"
      java: "class Solution {\n    public int minimumDeleteSum(String s1, String s2)\
        \ {\n        int m = s1.length();\n        int n = s2.length();\n\n        int[][]\
        \ dp = new int[m + 1][n + 1];\n\n        // Base cases\n        // dp[i][0]:\
        \ delete all characters from s1[0...i-1] to match empty s2\n        for (int\
        \ i = 1; i <= m; ++i) {\n            dp[i][0] = dp[i-1][0] + (int)s1.charAt(i-1);\n\
        \        }\n        // dp[0][j]: delete all characters from s2[0...j-1] to match\
        \ empty s1\n        for (int j = 1; j <= n; ++j) {\n            dp[0][j] = dp[0][j-1]\
        \ + (int)s2.charAt(j-1);\n        }\n\n        // Fill the DP table\n      \
        \  for (int i = 1; i <= m; ++i) {\n            for (int j = 1; j <= n; ++j)\
        \ {\n                if (s1.charAt(i-1) == s2.charAt(j-1)) {\n             \
        \       dp[i][j] = dp[i-1][j-1];\n                } else {\n               \
        \     dp[i][j] = Math.min(dp[i-1][j] + (int)s1.charAt(i-1), // Delete s1[i-1]\n\
        \                                        dp[i][j-1] + (int)s2.charAt(j-1));\
        \ // Delete s2[j-1]\n                }\n            }\n        }\n\n       \
        \ return dp[m][n];\n    }\n}"
      python: "class Solution(object):\n    def minimumDeleteSum(self, s1, s2):\n  \
        \      \"\"\"\n        :type s1: str\n        :type s2: str\n        :rtype:\
        \ int\n        \"\"\"\n        m = len(s1)\n        n = len(s2)\n\n        dp\
        \ = [[0] * (n + 1) for _ in range(m + 1)]\n\n        # Base cases\n        #\
        \ dp[i][0]: delete all characters from s1[0...i-1] to match empty s2\n     \
        \   for i in range(1, m + 1):\n            dp[i][0] = dp[i-1][0] + ord(s1[i-1])\n\
        \        # dp[0][j]: delete all characters from s2[0...j-1] to match empty s1\n\
        \        for j in range(1, n + 1):\n            dp[0][j] = dp[0][j-1] + ord(s2[j-1])\n\
        \n        # Fill the DP table\n        for i in range(1, m + 1):\n         \
        \   for j in range(1, n + 1):\n                if s1[i-1] == s2[j-1]:\n    \
        \                dp[i][j] = dp[i-1][j-1]\n                else:\n          \
        \          dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), # Delete s1[i-1]\n    \
        \                               dp[i][j-1] + ord(s2[j-1])) # Delete s2[j-1]\n\
        \n        return dp[m][n]"
      python3: "class Solution:\n    def minimumDeleteSum(self, s1: str, s2: str) ->\
        \ int:\n        m = len(s1)\n        n = len(s2)\n\n        dp = [[0] * (n +\
        \ 1) for _ in range(m + 1)]\n\n        # Base cases\n        # dp[i][0]: delete\
        \ all characters from s1[0...i-1] to match empty s2\n        for i in range(1,\
        \ m + 1):\n            dp[i][0] = dp[i-1][0] + ord(s1[i-1])\n        # dp[0][j]:\
        \ delete all characters from s2[0...j-1] to match empty s1\n        for j in\
        \ range(1, n + 1):\n            dp[0][j] = dp[0][j-1] + ord(s2[j-1])\n\n   \
        \     # Fill the DP table\n        for i in range(1, m + 1):\n            for\
        \ j in range(1, n + 1):\n                if s1[i-1] == s2[j-1]:\n          \
        \          dp[i][j] = dp[i-1][j-1]\n                else:\n                \
        \    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), # Delete s1[i-1]\n          \
        \                         dp[i][j-1] + ord(s2[j-1])) # Delete s2[j-1]\n\n  \
        \      return dp[m][n]"
      c: "#include <string.h>\n#include <stdlib.h>\n#include <stdio.h>\n\n// Helper\
        \ for min function\nint min(int a, int b) {\n    return a < b ? a : b;\n}\n\n\
        int minimumDeleteSum(char* s1, char* s2) {\n    int m = strlen(s1);\n    int\
        \ n = strlen(s2);\n\n    // Allocate DP table\n    int** dp = (int**)malloc((m\
        \ + 1) * sizeof(int*));\n    for (int i = 0; i <= m; ++i) {\n        dp[i] =\
        \ (int*)calloc((n + 1), sizeof(int)); // calloc initializes to 0\n    }\n\n\
        \    // Base cases\n    // dp[i][0]: delete all characters from s1[0...i-1]\
        \ to match empty s2\n    for (int i = 1; i <= m; ++i) {\n        dp[i][0] =\
        \ dp[i-1][0] + (int)s1[i-1];\n    }\n    // dp[0][j]: delete all characters\
        \ from s2[0...j-1] to match empty s1\n    for (int j = 1; j <= n; ++j) {\n \
        \       dp[0][j] = dp[0][j-1] + (int)s2[j-1];\n    }\n\n    // Fill the DP table\n\
        \    for (int i = 1; i <= m; ++i) {\n        for (int j = 1; j <= n; ++j) {\n\
        \            if (s1[i-1] == s2[j-1]) {\n                dp[i][j] = dp[i-1][j-1];\n\
        \            } else {\n                dp[i][j] = min(dp[i-1][j] + (int)s1[i-1],\
        \ // Delete s1[i-1]\n                               dp[i][j-1] + (int)s2[j-1]);\
        \ // Delete s2[j-1]\n            }\n        }\n    }\n\n    int result = dp[m][n];\n\
        \n    // Free allocated memory\n    for (int i = 0; i <= m; ++i) {\n       \
        \ free(dp[i]);\n    }\n    free(dp);\n\n    return result;\n}"
      csharp: "public class Solution {\n    public int MinimumDeleteSum(string s1, string\
        \ s2) {\n        int m = s1.Length;\n        int n = s2.Length;\n\n        int[,]\
        \ dp = new int[m + 1, n + 1];\n\n        // Initialize base cases\n        //\
        \ dp[i][0]: delete all characters from s1[0...i-1]\n        for (int i = 1;\
        \ i <= m; i++) {\n            dp[i, 0] = dp[i - 1, 0] + (int)s1[i - 1];\n  \
        \      }\n        // dp[0][j]: delete all characters from s2[0...j-1]\n    \
        \    for (int j = 1; j <= n; j++) {\n            dp[0, j] = dp[0, j - 1] + (int)s2[j\
        \ - 1];\n        }\n\n        // Fill the DP table\n        for (int i = 1;\
        \ i <= m; i++) {\n            for (int j = 1; j <= n; j++) {\n             \
        \   if (s1[i - 1] == s2[j - 1]) {\n                    dp[i, j] = dp[i - 1,\
        \ j - 1];\n                } else {\n                    dp[i, j] = Math.Min(dp[i\
        \ - 1, j] + (int)s1[i - 1], \n                                        dp[i,\
        \ j - 1] + (int)s2[j - 1]);\n                }\n            }\n        }\n\n\
        \        return dp[m, n];\n    }\n}"
      javascript: "/**\n * @param {string} s1\n * @param {string} s2\n * @return {number}\n\
        \ */\nvar minimumDeleteSum = function(s1, s2) {\n    const m = s1.length;\n\
        \    const n = s2.length;\n\n    const dp = Array(m + 1).fill(0).map(() => Array(n\
        \ + 1).fill(0));\n\n    // Initialize base cases\n    // dp[i][0]: delete all\
        \ characters from s1[0...i-1]\n    for (let i = 1; i <= m; i++) {\n        dp[i][0]\
        \ = dp[i - 1][0] + s1.charCodeAt(i - 1);\n    }\n    // dp[0][j]: delete all\
        \ characters from s2[0...j-1]\n    for (let j = 1; j <= n; j++) {\n        dp[0][j]\
        \ = dp[0][j - 1] + s2.charCodeAt(j - 1);\n    }\n\n    // Fill the DP table\n\
        \    for (let i = 1; i <= m; i++) {\n        for (let j = 1; j <= n; j++) {\n\
        \            if (s1[i - 1] === s2[j - 1]) {\n                dp[i][j] = dp[i\
        \ - 1][j - 1];\n            } else {\n                dp[i][j] = Math.min(dp[i\
        \ - 1][j] + s1.charCodeAt(i - 1), \n                                    dp[i][j\
        \ - 1] + s2.charCodeAt(j - 1));\n            }\n        }\n    }\n\n    return\
        \ dp[m][n];\n};"
      typescript: "function minimumDeleteSum(s1: string, s2: string): number {\n   \
        \ const m = s1.length;\n    const n = s2.length;\n\n    const dp: number[][]\
        \ = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));\n\n    // Initialize\
        \ base cases\n    // dp[i][0]: delete all characters from s1[0...i-1]\n    for\
        \ (let i = 1; i <= m; i++) {\n        dp[i][0] = dp[i - 1][0] + s1.charCodeAt(i\
        \ - 1);\n    }\n    // dp[0][j]: delete all characters from s2[0...j-1]\n  \
        \  for (let j = 1; j <= n; j++) {\n        dp[0][j] = dp[0][j - 1] + s2.charCodeAt(j\
        \ - 1);\n    }\n\n    // Fill the DP table\n    for (let i = 1; i <= m; i++)\
        \ {\n        for (let j = 1; j <= n; j++) {\n            if (s1[i - 1] === s2[j\
        \ - 1]) {\n                dp[i][j] = dp[i - 1][j - 1];\n            } else\
        \ {\n                dp[i][j] = Math.min(dp[i - 1][j] + s1.charCodeAt(i - 1),\
        \ \n                                    dp[i][j - 1] + s2.charCodeAt(j - 1));\n\
        \            }\n        }\n    }\n\n    return dp[m][n];\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s1\n     * @param String\
        \ $s2\n     * @return Integer\n     */\n    function minimumDeleteSum($s1, $s2)\
        \ {\n        $m = strlen($s1);\n        $n = strlen($s2);\n\n        $dp = array_fill(0,\
        \ $m + 1, array_fill(0, $n + 1, 0));\n\n        // Initialize base cases\n \
        \       // dp[i][0]: delete all characters from s1[0...i-1]\n        for ($i\
        \ = 1; $i <= $m; $i++) {\n            $dp[$i][0] = $dp[$i - 1][0] + ord($s1[$i\
        \ - 1]);\n        }\n        // dp[0][j]: delete all characters from s2[0...j-1]\n\
        \        for ($j = 1; $j <= $n; $j++) {\n            $dp[0][$j] = $dp[0][$j\
        \ - 1] + ord($s2[$j - 1]);\n        }\n\n        // Fill the DP table\n    \
        \    for ($i = 1; $i <= $m; $i++) {\n            for ($j = 1; $j <= $n; $j++)\
        \ {\n                if ($s1[$i - 1] === $s2[$j - 1]) {\n                  \
        \  $dp[$i][$j] = $dp[$i - 1][$j - 1];\n                } else {\n          \
        \          $dp[$i][$j] = min($dp[$i - 1][$j] + ord($s1[$i - 1]), \n        \
        \                              $dp[$i][$j - 1] + ord($s2[$j - 1]));\n      \
        \          }\n            }\n        }\n\n        return $dp[$m][$n];\n    }\n\
        }"
      swift: "class Solution {\n    func minimumDeleteSum(_ s1: String, _ s2: String)\
        \ -> Int {\n        let m = s1.count\n        let n = s2.count\n\n        var\
        \ dp = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)\n\n\
        \        let s1Chars = Array(s1)\n        let s2Chars = Array(s2)\n\n      \
        \  // Initialize base cases\n        // dp[i][0]: delete all characters from\
        \ s1[0...i-1]\n        for i in 1...m {\n            dp[i][0] = dp[i - 1][0]\
        \ + Int(s1Chars[i - 1].asciiValue!)\n        }\n        // dp[0][j]: delete\
        \ all characters from s2[0...j-1]\n        for j in 1...n {\n            dp[0][j]\
        \ = dp[0][j - 1] + Int(s2Chars[j - 1].asciiValue!)\n        }\n\n        //\
        \ Fill the DP table\n        for i in 1...m {\n            for j in 1...n {\n\
        \                if s1Chars[i - 1] == s2Chars[j - 1] {\n                   \
        \ dp[i][j] = dp[i - 1][j - 1]\n                } else {\n                  \
        \  dp[i][j] = min(dp[i - 1][j] + Int(s1Chars[i - 1].asciiValue!), \n       \
        \                            dp[i][j - 1] + Int(s2Chars[j - 1].asciiValue!))\n\
        \                }\n            }\n        }\n\n        return dp[m][n]\n  \
        \  }\n}"
      kotlin: "class Solution {\n    fun minimumDeleteSum(s1: String, s2: String): Int\
        \ {\n        val n = s1.length\n        val m = s2.length\n\n        val dp\
        \ = Array(n + 1) { IntArray(m + 1) }\n\n        for (j in 1..m) {\n        \
        \    dp[0][j] = dp[0][j - 1] + s2[j - 1].toInt()\n        }\n\n        for (i\
        \ in 1..n) {\n            dp[i][0] = dp[i - 1][0] + s1[i - 1].toInt()\n    \
        \    }\n\n        for (i in 1..n) {\n            for (j in 1..m) {\n       \
        \         if (s1[i - 1] == s2[j - 1]) {\n                    dp[i][j] = dp[i\
        \ - 1][j - 1]\n                } else {\n                    val cost1 = dp[i\
        \ - 1][j] + s1[i - 1].toInt()\n                    val cost2 = dp[i][j - 1]\
        \ + s2[j - 1].toInt()\n                    dp[i][j] = minOf(cost1, cost2)\n\
        \                }\n            }\n        }\n\n        return dp[n][m]\n  \
        \  }\n}"
      dart: "class Solution {\n  int minimumDeleteSum(String s1, String s2) {\n    final\
        \ n = s1.length;\n    final m = s2.length;\n\n    final dp = List.generate(n\
        \ + 1, (_) => List.filled(m + 1, 0));\n\n    for (int j = 1; j <= m; j++) {\n\
        \      dp[0][j] = dp[0][j - 1] + s2.codeUnitAt(j - 1);\n    }\n\n    for (int\
        \ i = 1; i <= n; i++) {\n      dp[i][0] = dp[i - 1][0] + s1.codeUnitAt(i - 1);\n\
        \    }\n\n    for (int i = 1; i <= n; i++) {\n      for (int j = 1; j <= m;\
        \ j++) {\n        if (s1[i - 1] == s2[j - 1]) {\n          dp[i][j] = dp[i -\
        \ 1][j - 1];\n        } else {\n          final cost1 = dp[i - 1][j] + s1.codeUnitAt(i\
        \ - 1);\n          final cost2 = dp[i][j - 1] + s2.codeUnitAt(j - 1);\n    \
        \      dp[i][j] = cost1 < cost2 ? cost1 : cost2;\n        }\n      }\n    }\n\
        \n    return dp[n][m];\n  }\n}"
      go: "func minimumDeleteSum(s1 string, s2 string) int {\n    n := len(s1)\n   \
        \ m := len(s2)\n\n    dp := make([][]int, n+1)\n    for i := range dp {\n  \
        \      dp[i] = make([]int, m+1)\n    }\n\n    for j := 1; j <= m; j++ {\n  \
        \      dp[0][j] = dp[0][j-1] + int(s2[j-1])\n    }\n\n    for i := 1; i <= n;\
        \ i++ {\n        dp[i][0] = dp[i-1][0] + int(s1[i-1])\n    }\n\n    for i :=\
        \ 1; i <= n; i++ {\n        for j := 1; j <= m; j++ {\n            if s1[i-1]\
        \ == s2[j-1] {\n                dp[i][j] = dp[i-1][j-1]\n            } else\
        \ {\n                cost1 := dp[i-1][j] + int(s1[i-1])\n                cost2\
        \ := dp[i][j-1] + int(s2[j-1])\n                if cost1 < cost2 {\n       \
        \             dp[i][j] = cost1\n                } else {\n                 \
        \   dp[i][j] = cost2\n                }\n            }\n        }\n    }\n\n\
        \    return dp[n][m]\n}"
      ruby: "# @param {String} s1\n# @param {String} s2\n# @return {Integer}\ndef minimum_delete_sum(s1,\
        \ s2)\n    n = s1.length\n    m = s2.length\n\n    dp = Array.new(n + 1) { Array.new(m\
        \ + 1, 0) }\n\n    (1..m).each do |j|\n        dp[0][j] = dp[0][j - 1] + s2[j\
        \ - 1].ord\n    end\n\n    (1..n).each do |i|\n        dp[i][0] = dp[i - 1][0]\
        \ + s1[i - 1].ord\n    end\n\n    (1..n).each do |i|\n        (1..m).each do\
        \ |j|\n            if s1[i - 1] == s2[j - 1]\n                dp[i][j] = dp[i\
        \ - 1][j - 1]\n            else\n                cost1 = dp[i - 1][j] + s1[i\
        \ - 1].ord\n                cost2 = dp[i][j - 1] + s2[j - 1].ord\n         \
        \       dp[i][j] = [cost1, cost2].min\n            end\n        end\n    end\n\
        \n    dp[n][m]\nend"
      scala: "object Solution {\n    def minimumDeleteSum(s1: String, s2: String): Int\
        \ = {\n        val n = s1.length\n        val m = s2.length\n\n        val dp\
        \ = Array.ofDim[Int](n + 1, m + 1)\n\n        for (j <- 1 to m) {\n        \
        \    dp(0)(j) = dp(0)(j - 1) + s2(j - 1).toInt\n        }\n\n        for (i\
        \ <- 1 to n) {\n            dp(i)(0) = dp(i - 1)(0) + s1(i - 1).toInt\n    \
        \    }\n\n        for (i <- 1 to n) {\n            for (j <- 1 to m) {\n   \
        \             if (s1(i - 1) == s2(j - 1)) {\n                    dp(i)(j) =\
        \ dp(i - 1)(j - 1)\n                } else {\n                    val cost1\
        \ = dp(i - 1)(j) + s1(i - 1).toInt\n                    val cost2 = dp(i)(j\
        \ - 1) + s2(j - 1).toInt\n                    dp(i)(j) = Math.min(cost1, cost2)\n\
        \                }\n            }\n        }\n\n        dp(n)(m)\n    }\n}"
      rust: "impl Solution {\n    pub fn minimum_delete_sum(s1: String, s2: String)\
        \ -> i32 {\n        let s1_bytes = s1.as_bytes();\n        let s2_bytes = s2.as_bytes();\n\
        \        let m = s1_bytes.len();\n        let n = s2_bytes.len();\n\n      \
        \  let mut dp = vec![vec![0; n + 1]; m + 1];\n\n        let mut total_ascii_sum\
        \ = 0;\n        for &c in s1_bytes {\n            total_ascii_sum += c as i32;\n\
        \        }\n        for &c in s2_bytes {\n            total_ascii_sum += c as\
        \ i32;\n        }\n\n        for i in 1..=m {\n            for j in 1..=n {\n\
        \                if s1_bytes[i - 1] == s2_bytes[j - 1] {\n                 \
        \   dp[i][j] = dp[i - 1][j - 1] + s1_bytes[i - 1] as i32;\n                }\
        \ else {\n                    dp[i][j] = dp[i - 1][j].max(dp[i][j - 1]);\n \
        \               }\n            }\n        }\n\n        total_ascii_sum - 2 *\
        \ dp[m][n]\n    }\n}"
      racket: "(define/contract (minimum-delete-sum s1 s2)\n  (-> string? string? exact-integer?)\n\
        \  (let* ([m (string-length s1)]\n         [n (string-length s2)]\n        \
        \ [dp (build-vector (+ m 1) (lambda (i) (build-vector (+ n 1) (lambda (j) 0))))]\n\
        \         [total-ascii-sum 0])\n\n    ;; Calculate total ASCII sum\n    (for\
        \ ([char (string->list s1)])\n      (set! total-ascii-sum (+ total-ascii-sum\
        \ (char->integer char))))\n    (for ([char (string->list s2)])\n      (set!\
        \ total-ascii-sum (+ total-ascii-sum (char->integer char))))\n\n    ;; Fill\
        \ DP table\n    (for ([i (in-range 1 (+ m 1))])\n      (for ([j (in-range 1\
        \ (+ n 1))])\n        (if (char=? (string-ref s1 (- i 1)) (string-ref s2 (-\
        \ j 1)))\n            (vector-set! (vector-ref dp i) j\n                   \
        \      (+ (vector-ref (vector-ref dp (- i 1)) (- j 1))\n                   \
        \         (char->integer (string-ref s1 (- i 1)))))\n            (vector-set!\
        \ (vector-ref dp i) j\n                         (max (vector-ref (vector-ref\
        \ dp (- i 1)) j)\n                              (vector-ref (vector-ref dp i)\
        \ (- j 1)))))))\n\n    (- total-ascii-sum (* 2 (vector-ref (vector-ref dp m)\
        \ n)))))"
      erlang: "-spec minimum_delete_sum(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary())\
        \ -> integer().\nminimum_delete_sum(S1, S2) ->\n    S1Chars = binary_to_list(S1),\
        \ % List of integers (ASCII values)\n    S2Chars = binary_to_list(S2),\n   \
        \ M = length(S1Chars),\n    N = length(S2Chars),\n\n    TotalAsciiSum = lists:sum(S1Chars)\
        \ + lists:sum(S2Chars),\n\n    % dp_prev_row represents dp[i-1][0...N]\n   \
        \ % Initialize dp_prev_row (for i=0)\n    DpPrevRow = lists:duplicate(N + 1,\
        \ 0),\n\n    LCS_Sum = calculate_lcs_sum_erlang(S1Chars, S2Chars, DpPrevRow),\n\
        \n    TotalAsciiSum - 2 * LCS_Sum.\n\n% S1Chars: remaining S1 characters to\
        \ process\n% S2Chars: full S2 list (for reference)\n% DpPrevRow: list representing\
        \ dp[i-1][0...N]\ncalculate_lcs_sum_erlang([], _S2Chars, DpPrevRow) ->\n   \
        \ % All S1Chars processed, DpPrevRow is now the last row (dp[M])\n    lists:last(DpPrevRow);\n\
        calculate_lcs_sum_erlang([S1Char | RestS1Chars], S2Chars, DpPrevRow) ->\n  \
        \  % Build DpCurrRow for current S1Char\n    % DpCurrRow starts with dp[i][0]\
        \ = 0\n    DpCurrRow = build_dp_current_row_erlang(S1Char, S2Chars, DpPrevRow,\
        \ 0, [0]),\n\n    calculate_lcs_sum_erlang(RestS1Chars, S2Chars, DpCurrRow).\n\
        \n% S1Char: current char from s1 (S1Chars[i])\n% S2Chars: remaining S2 characters\
        \ to process (S2Chars[j...N-1])\n% DpPrevRow: list representing dp[i-1][0...N]\n\
        % DpCurrRowPrevColVal: dp[i][j] (value from current row, previous column)\n\
        % AccCurrRow: accumulator for current row (built in reverse, starting with dp[i][0])\n\
        build_dp_current_row_erlang(_S1Char, [], _DpPrevRow, _DpCurrRowPrevColVal, AccCurrRow)\
        \ ->\n    % All S2Chars processed for current row\n    lists:reverse(AccCurrRow);\n\
        build_dp_current_row_erlang(S1Char, [S2Char | RestS2Chars], [PrevDiagVal | [PrevUpVal\
        \ | RestDpPrevRow]], DpCurrRowPrevColVal, AccCurrRow) ->\n    % PrevDiagVal\
        \ is dp[i-1][j-1]\n    % PrevUpVal is dp[i-1][j]\n    % DpCurrRowPrevColVal\
        \ is dp[i][j-1]\n\n    Val = if\n        S1Char =:= S2Char ->\n            PrevDiagVal\
        \ + S1Char;\n        true ->\n            max(PrevUpVal, DpCurrRowPrevColVal)\n\
        \    end,\n    build_dp_current_row_erlang(S1Char, RestS2Chars, [PrevUpVal |\
        \ RestDpPrevRow], Val, [Val | AccCurrRow])."
      elixir: "defmodule Solution do\n  @spec minimum_delete_sum(s1 :: String.t, s2\
        \ :: String.t) :: integer\n  def minimum_delete_sum(s1, s2) do\n    s1_chars\
        \ = String.to_charlist(s1)\n    s2_chars = String.to_charlist(s2)\n    m = length(s1_chars)\n\
        \    n = length(s2_chars)\n\n    total_ascii_sum = Enum.sum(s1_chars) + Enum.sum(s2_chars)\n\
        \n    # dp_prev_row represents dp[i-1][0...N]\n    # Initialize dp_prev_row\
        \ (for i=0)\n    dp_prev_row = List.duplicate(0, n + 1)\n\n    lcs_sum =\n \
        \     Enum.reduce(s1_chars, dp_prev_row, fn s1_char, acc_dp_prev_row ->\n  \
        \      # acc_dp_prev_row is dp[i-1][0...N]\n        # Build dp_curr_row for\
        \ current s1_char (dp[i][0...N])\n        build_dp_current_row_elixir(s1_char,\
        \ s2_chars, acc_dp_prev_row)\n      end)\n      |> List.last()\n\n    total_ascii_sum\
        \ - 2 * lcs_sum\n  end\n\n  # s1_char: current char from s1 (s1_chars[i])\n\
        \  # s2_chars: full s2 list (for reference)\n  # dp_prev_row: list representing\
        \ dp[i-1][0...N]\n  defp build_dp_current_row_elixir(s1_char, s2_chars, dp_prev_row)\
        \ do\n    # State for reduce: {current_dp_row_reversed, prev_col_val_in_curr_row,\
        \ dp_prev_row_tail}\n    # current_dp_row_reversed: [dp[i][j], dp[i][j-1], ...,\
        \ dp[i][0]]\n    # prev_col_val_in_curr_row: dp[i][j-1]\n    # dp_prev_row_tail:\
        \ [dp[i-1][j], dp[i-1][j+1], ...]\n\n    {final_dp_curr_row_reversed, _prev_col_val,\
        \ _dp_prev_row_tail} =\n      Enum.reduce(s2_chars, {[0], 0, dp_prev_row}, fn\
        \ s2_char, {acc_curr_row_rev, prev_col_val_in_curr_row, [prev_diag_val | [prev_up_val\
        \ | rest_dp_prev_row]]} ->\n        val = if s1_char == s2_char do\n       \
        \   prev_diag_val + s1_char\n        else\n          max(prev_up_val, prev_col_val_in_curr_row)\n\
        \        end\n        {[val | acc_curr_row_rev], val, [prev_up_val | rest_dp_prev_row]}\n\
        \      end)\n\n    Enum.reverse(final_dp_curr_row_reversed)\n  end\nend"
    approach: 'The problem asks for the minimum ASCII sum of deleted characters to make
      two strings, s1 and s2, equal. This is a classic dynamic programming problem,
      closely related to the Longest Common Subsequence (LCS) problem. We can define
      a 2D DP table, `dp[i][j]`, to represent the minimum ASCII sum of deletions required
      to make the prefix `s1[0...i-1]` equal to the prefix `s2[0...j-1]`. The dimensions
      of the DP table will be `(len(s1) + 1) x (len(s2) + 1)`.


      The base cases for the DP table are as follows: `dp[0][0]` is 0, as two empty
      strings are already equal with no deletions. For `dp[i][0]`, it means making `s1[0...i-1]`
      equal to an empty string, which requires deleting all characters in `s1[0...i-1]`.
      Thus, `dp[i][0] = dp[i-1][0] + ord(s1[i-1])`. Similarly, `dp[0][j] = dp[0][j-1]
      + ord(s2[j-1])` for making `s2[0...j-1]` equal to an empty string. For the general
      case `dp[i][j]` where `i > 0` and `j > 0`, we consider two scenarios: if `s1[i-1]`
      and `s2[j-1]` are equal, no deletion is needed for these characters, so `dp[i][j]
      = dp[i-1][j-1]`. If they are not equal, we must delete either `s1[i-1]` or `s2[j-1]`.
      We choose the option that results in the minimum deletion sum: `dp[i][j] = min(dp[i-1][j]
      + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))`. After filling the entire DP table,
      the final answer will be `dp[len(s1)][len(s2)]`.'
    time_complexity: The time complexity is O(m * n), where m is the length of string
      s1 and n is the length of string s2. This is because we iterate through each cell
      of the `(m+1) x (n+1)` DP table once, and each cell computation takes constant
      time.
    space_complexity: The space complexity is O(m * n), where m is the length of string
      s1 and n is the length of string s2. This is due to the storage required for the
      2D DP table. This can be optimized to O(min(m, n)) by only keeping track of the
      current and previous rows, but for clarity and given the constraints (lengths
      up to 1000), O(m*n) is acceptable.
    elapsed_time: 180.64159989356995
    model: gemini-2.5-flash
    generated_at: '2026-01-10 01:10:21 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int minimumDeleteSum(string s1, string s2)\
        \ {\n        int m = s1.size(), n = s2.size();\n        vector<vector<int>>\
        \ dp(m + 1, vector<int>(n + 1, 0));\n        for (int i = 1; i <= m; i++) dp[i][0]\
        \ = dp[i - 1][0] + s1[i - 1];\n        for (int j = 1; j <= n; j++) dp[0][j]\
        \ = dp[0][j - 1] + s2[j - 1];\n        for (int i = 1; i <= m; i++) {\n    \
        \        for (int j = 1; j <= n; j++) {\n                if (s1[i - 1] == s2[j\
        \ - 1]) dp[i][j] = dp[i - 1][j - 1];\n                else dp[i][j] = min(dp[i\
        \ - 1][j] + s1[i - 1], dp[i][j - 1] + s2[j - 1]);\n            }\n        }\n\
        \        return dp[m][n];\n    }\n};"
      java: "class Solution {\n    public int minimumDeleteSum(String s1, String s2)\
        \ {\n        int m = s1.length(), n = s2.length();\n        int[][] dp = new\
        \ int[m + 1][n + 1];\n        for (int i = 1; i <= m; i++) dp[i][0] = dp[i -\
        \ 1][0] + s1.charAt(i - 1);\n        for (int j = 1; j <= n; j++) dp[0][j] =\
        \ dp[0][j - 1] + s2.charAt(j - 1);\n        for (int i = 1; i <= m; i++) {\n\
        \            for (int j = 1; j <= n; j++) {\n                if (s1.charAt(i\
        \ - 1) == s2.charAt(j - 1)) dp[i][j] = dp[i - 1][j - 1];\n                else\
        \ dp[i][j] = Math.min(dp[i - 1][j] + s1.charAt(i - 1), dp[i][j - 1] + s2.charAt(j\
        \ - 1));\n            }\n        }\n        return dp[m][n];\n    }\n}"
      python: "class Solution(object):\n    def minimumDeleteSum(self, s1, s2):\n  \
        \      m, n = len(s1), len(s2)\n        dp = [[0] * (n + 1) for _ in range(m\
        \ + 1)]\n        for i in range(1, m + 1): dp[i][0] = dp[i - 1][0] + ord(s1[i\
        \ - 1])\n        for j in range(1, n + 1): dp[0][j] = dp[0][j - 1] + ord(s2[j\
        \ - 1])\n        for i in range(1, m + 1):\n            for j in range(1, n\
        \ + 1):\n                if s1[i - 1] == s2[j - 1]: dp[i][j] = dp[i - 1][j -\
        \ 1]\n                else: dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j\
        \ - 1] + ord(s2[j - 1]))\n        return dp[m][n]"
      python3: "class Solution:\n    def minimumDeleteSum(self, s1: str, s2: str) ->\
        \ int:\n        m, n = len(s1), len(s2)\n        dp = [[0] * (n + 1) for _ in\
        \ range(m + 1)]\n        for i in range(1, m + 1): dp[i][0] = dp[i - 1][0] +\
        \ ord(s1[i - 1])\n        for j in range(1, n + 1): dp[0][j] = dp[0][j - 1]\
        \ + ord(s2[j - 1])\n        for i in range(1, m + 1):\n            for j in\
        \ range(1, n + 1):\n                if s1[i - 1] == s2[j - 1]: dp[i][j] = dp[i\
        \ - 1][j - 1]\n                else: dp[i][j] = min(dp[i - 1][j] + ord(s1[i\
        \ - 1]), dp[i][j - 1] + ord(s2[j - 1]))\n        return dp[m][n]"
      c: "int minimumDeleteSum(char* s1, char* s2) {\n    int m = strlen(s1), n = strlen(s2);\n\
        \    int** dp = (int**)malloc((m + 1) * sizeof(int*));\n    for (int i = 0;\
        \ i <= m; i++) dp[i] = (int*)malloc((n + 1) * sizeof(int));\n    for (int i\
        \ = 1; i <= m; i++) dp[i][0] = dp[i - 1][0] + s1[i - 1];\n    for (int j = 1;\
        \ j <= n; j++) dp[0][j] = dp[0][j - 1] + s2[j - 1];\n    for (int i = 1; i <=\
        \ m; i++) {\n        for (int j = 1; j <= n; j++) {\n            if (s1[i -\
        \ 1] == s2[j - 1]) dp[i][j] = dp[i - 1][j - 1];\n            else dp[i][j] =\
        \ (dp[i - 1][j] + s1[i - 1] < dp[i][j - 1] + s2[j - 1]) ? dp[i - 1][j] + s1[i\
        \ - 1] : dp[i][j - 1] + s2[j - 1];\n        }\n    }\n    int result = dp[m][n];\n\
        \    for (int i = 0; i <= m; i++) free(dp[i]);\n    free(dp);\n    return result;\n\
        }"
      csharp: "public class Solution {\n    public int MinimumDeleteSum(string s1, string\
        \ s2) {\n        int m = s1.Length;\n        int n = s2.Length;\n        int[,]\
        \ dp = new int[m + 1, n + 1];\n        for (int i = 1; i <= m; i++) {\n    \
        \        dp[i, 0] = dp[i - 1, 0] + s1[i - 1];\n        }\n        for (int j\
        \ = 1; j <= n; j++) {\n            dp[0, j] = dp[0, j - 1] + s2[j - 1];\n  \
        \      }\n        for (int i = 1; i <= m; i++) {\n            for (int j = 1;\
        \ j <= n; j++) {\n                if (s1[i - 1] == s2[j - 1]) {\n          \
        \          dp[i, j] = dp[i - 1, j - 1];\n                } else {\n        \
        \            dp[i, j] = Math.Min(dp[i - 1, j] + s1[i - 1], dp[i, j - 1] + s2[j\
        \ - 1]);\n                }\n            }\n        }\n        return dp[m,\
        \ n];\n    }\n}"
      javascript: "var minimumDeleteSum = function(s1, s2) {\n    let m = s1.length;\n\
        \    let n = s2.length;\n    let dp = Array(m + 1).fill(0).map(() => Array(n\
        \ + 1).fill(0));\n    for (let i = 1; i <= m; i++) {\n        dp[i][0] = dp[i\
        \ - 1][0] + s1.charCodeAt(i - 1);\n    }\n    for (let j = 1; j <= n; j++) {\n\
        \        dp[0][j] = dp[0][j - 1] + s2.charCodeAt(j - 1);\n    }\n    for (let\
        \ i = 1; i <= m; i++) {\n        for (let j = 1; j <= n; j++) {\n          \
        \  if (s1[i - 1] === s2[j - 1]) {\n                dp[i][j] = dp[i - 1][j -\
        \ 1];\n            } else {\n                dp[i][j] = Math.min(dp[i - 1][j]\
        \ + s1.charCodeAt(i - 1), dp[i][j - 1] + s2.charCodeAt(j - 1));\n          \
        \  }\n        }\n    }\n    return dp[m][n];\n};"
      typescript: "function minimumDeleteSum(s1: string, s2: string): number {\n   \
        \ let m: number = s1.length;\n    let n: number = s2.length;\n    let dp: number[][]\
        \ = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));\n    for (let i =\
        \ 1; i <= m; i++) {\n        dp[i][0] = dp[i - 1][0] + s1.charCodeAt(i - 1);\n\
        \    }\n    for (let j = 1; j <= n; j++) {\n        dp[0][j] = dp[0][j - 1]\
        \ + s2.charCodeAt(j - 1);\n    }\n    for (let i = 1; i <= m; i++) {\n     \
        \   for (let j = 1; j <= n; j++) {\n            if (s1[i - 1] === s2[j - 1])\
        \ {\n                dp[i][j] = dp[i - 1][j - 1];\n            } else {\n  \
        \              dp[i][j] = Math.min(dp[i - 1][j] + s1.charCodeAt(i - 1), dp[i][j\
        \ - 1] + s2.charCodeAt(j - 1));\n            }\n        }\n    }\n    return\
        \ dp[m][n];\n}"
      php: "class Solution {\n    function minimumDeleteSum($s1, $s2) {\n        $m\
        \ = strlen($s1);\n        $n = strlen($s2);\n        $dp = array_fill(0, $m\
        \ + 1, array_fill(0, $n + 1, 0));\n        for ($i = 1; $i <= $m; $i++) {\n\
        \            $dp[$i][0] = $dp[$i - 1][0] + ord($s1[$i - 1]);\n        }\n  \
        \      for ($j = 1; $j <= $n; $j++) {\n            $dp[0][$j] = $dp[0][$j -\
        \ 1] + ord($s2[$j - 1]);\n        }\n        for ($i = 1; $i <= $m; $i++) {\n\
        \            for ($j = 1; $j <= $n; $j++) {\n                if ($s1[$i - 1]\
        \ === $s2[$j - 1]) {\n                    $dp[$i][$j] = $dp[$i - 1][$j - 1];\n\
        \                } else {\n                    $dp[$i][$j] = min($dp[$i - 1][$j]\
        \ + ord($s1[$i - 1]), $dp[$i][$j - 1] + ord($s2[$j - 1]));\n               \
        \ }\n            }\n        }\n        return $dp[$m][$n];\n    }\n}"
      swift: "class Solution {\n    func minimumDeleteSum(_ s1: String, _ s2: String)\
        \ -> Int {\n        let m = s1.count\n        let n = s2.count\n        var\
        \ dp = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)\n \
        \       for i in 1...m {\n            dp[i][0] = dp[i - 1][0] + Int(s1[s1.index(s1.startIndex,\
        \ offsetBy: i - 1)].asciiValue!)\n        }\n        for j in 1...n {\n    \
        \        dp[0][j] = dp[0][j - 1] + Int(s2[s2.index(s2.startIndex, offsetBy:\
        \ j - 1)].asciiValue!)\n        }\n        for i in 1...m {\n            for\
        \ j in 1...n {\n                if s1[s1.index(s1.startIndex, offsetBy: i -\
        \ 1)] == s2[s2.index(s2.startIndex, offsetBy: j - 1)] {\n                  \
        \  dp[i][j] = dp[i - 1][j - 1]\n                } else {\n                 \
        \   dp[i][j] = min(dp[i - 1][j] + Int(s1[s1.index(s1.startIndex, offsetBy: i\
        \ - 1)].asciiValue!), dp[i][j - 1] + Int(s2[s2.index(s2.startIndex, offsetBy:\
        \ j - 1)].asciiValue!))\n                }\n            }\n        }\n     \
        \   return dp[m][n]\n    }\n}"
      kotlin: "class Solution {\n    fun minimumDeleteSum(s1: String, s2: String): Int\
        \ {\n        val m = s1.length\n        val n = s2.length\n        val dp =\
        \ Array(m + 1) { IntArray(n + 1) }\n        for (i in m - 1 downTo 0) {\n  \
        \          dp[i][n] = dp[i + 1][n] + s1[i].toInt()\n        }\n        for (j\
        \ in n - 1 downTo 0) {\n            dp[m][j] = dp[m][j + 1] + s2[j].toInt()\n\
        \        }\n        for (i in m - 1 downTo 0) {\n            for (j in n - 1\
        \ downTo 0) {\n                if (s1[i] == s2[j]) {\n                    dp[i][j]\
        \ = dp[i + 1][j + 1]\n                } else {\n                    dp[i][j]\
        \ = Math.min(dp[i + 1][j] + s1[i].toInt(), dp[i][j + 1] + s2[j].toInt())\n \
        \               }\n            }\n        }\n        return dp[0][0]\n    }\n\
        }"
      dart: "class Solution {\n  int minimumDeleteSum(String s1, String s2) {\n    int\
        \ m = s1.length;\n    int n = s2.length;\n    List<List<int>> dp = List.generate(m\
        \ + 1, (i) => List.generate(n + 1, (j) => 0));\n    for (int i = m - 1; i >=\
        \ 0; i--) {\n      dp[i][n] = dp[i + 1][n] + s1.codeUnitAt(i);\n    }\n    for\
        \ (int j = n - 1; j >= 0; j--) {\n      dp[m][j] = dp[m][j + 1] + s2.codeUnitAt(j);\n\
        \    }\n    for (int i = m - 1; i >= 0; i--) {\n      for (int j = n - 1; j\
        \ >= 0; j--) {\n        if (s1[i] == s2[j]) {\n          dp[i][j] = dp[i + 1][j\
        \ + 1];\n        } else {\n          dp[i][j] = (dp[i + 1][j] + s1.codeUnitAt(i)).min(dp[i][j\
        \ + 1] + s2.codeUnitAt(j));\n        }\n      }\n    }\n    return dp[0][0];\n\
        \  }\n}"
      go: "func minimumDeleteSum(s1 string, s2 string) int {\n    m, n := len(s1), len(s2)\n\
        \    dp := make([][]int, m + 1)\n    for i := range dp {\n        dp[i] = make([]int,\
        \ n + 1)\n    }\n    for i := m - 1; i >= 0; i-- {\n        dp[i][n] = dp[i\
        \ + 1][n] + int(s1[i])\n    }\n    for j := n - 1; j >= 0; j-- {\n        dp[m][j]\
        \ = dp[m][j + 1] + int(s2[j])\n    }\n    for i := m - 1; i >= 0; i-- {\n  \
        \      for j := n - 1; j >= 0; j-- {\n            if s1[i] == s2[j] {\n    \
        \            dp[i][j] = dp[i + 1][j + 1]\n            } else {\n           \
        \     dp[i][j] = min(dp[i + 1][j] + int(s1[i]), dp[i][j + 1] + int(s2[j]))\n\
        \            }\n        }\n    }\n    return dp[0][0]\n}\n\nfunc min(a, b int)\
        \ int {\n    if a < b {\n        return a\n    }\n    return b\n}"
      ruby: "# @param {String} s1\n# @param {String} s2\n# @return {Integer}\ndef minimum_delete_sum(s1,\
        \ s2)\n    m, n = s1.length, s2.length\n    dp = Array.new(m + 1) { Array.new(n\
        \ + 1, 0) }\n    (m - 1).downto(0) do |i|\n        dp[i][n] = dp[i + 1][n] +\
        \ s1[i].ord\n    end\n    (n - 1).downto(0) do |j|\n        dp[m][j] = dp[m][j\
        \ + 1] + s2[j].ord\n    end\n    (m - 1).downto(0) do |i|\n        (n - 1).downto(0)\
        \ do |j|\n            if s1[i] == s2[j]\n                dp[i][j] = dp[i + 1][j\
        \ + 1]\n            else\n                dp[i][j] = [dp[i + 1][j] + s1[i].ord,\
        \ dp[i][j + 1] + s2[j].ord].min\n            end\n        end\n    end\n   \
        \ dp[0][0]\nend"
      scala: "object Solution {\n    def minimumDeleteSum(s1: String, s2: String): Int\
        \ = {\n        val m = s1.length\n        val n = s2.length\n        val dp\
        \ = Array.ofDim[Int](m + 1, n + 1)\n        for (i <- m - 1 to 0 by -1) {\n\
        \            dp(i)(n) = dp(i + 1)(n) + s1(i)\n        }\n        for (j <- n\
        \ - 1 to 0 by -1) {\n            dp(m)(j) = dp(m)(j + 1) + s2(j)\n        }\n\
        \        for (i <- m - 1 to 0 by -1) {\n            for (j <- n - 1 to 0 by\
        \ -1) {\n                if (s1(i) == s2(j)) {\n                    dp(i)(j)\
        \ = dp(i + 1)(j + 1)\n                } else {\n                    dp(i)(j)\
        \ = Math.min(dp(i + 1)(j) + s1(i), dp(i)(j + 1) + s2(j))\n                }\n\
        \            }\n        }\n        dp(0)(0)\n    }\n}"
      rust: "impl Solution {\n    pub fn minimum_delete_sum(s1: String, s2: String)\
        \ -> i32 {\n        let s1 = s1.as_bytes();\n        let s2 = s2.as_bytes();\n\
        \        let m = s1.len();\n        let n = s2.len();\n        let mut dp =\
        \ vec![vec![0; n + 1]; m + 1];\n        for i in (0..=m).rev() {\n         \
        \   for j in (0..=n).rev() {\n                if i == m && j == n {\n      \
        \              dp[i][j] = 0;\n                } else if i == m {\n         \
        \           dp[i][j] = dp[i][j + 1] + s2[j] as i32;\n                } else\
        \ if j == n {\n                    dp[i][j] = dp[i + 1][j] + s1[i] as i32;\n\
        \                } else if s1[i] == s2[j] {\n                    dp[i][j] =\
        \ dp[i + 1][j + 1];\n                } else {\n                    dp[i][j]\
        \ = std::cmp::min(dp[i + 1][j] + s1[i] as i32, dp[i][j + 1] + s2[j] as i32);\n\
        \                }\n            }\n        }\n        dp[0][0]\n    }\n}"
      racket: "define/contract (minimum-delete-sum s1 s2)\n  (-> string? string? exact-integer?)\n\
        \  (let* (\n    [s1-len (string-length s1)]\n    [s2-len (string-length s2)]\n\
        \    [dp (make-vector (add1 s1-len) (make-vector (add1 s2-len) 0))])\n    (do\
        \ (\n      [i (sub1 s1-len)])\n      [(< i 0)]\n      (do (\n        [j (sub1\
        \ s2-len)])\n        [(< j 0)]\n        (cond\n          [(and (= i s1-len)\
        \ (= j s2-len)) (vector-set! dp i (vector-ref dp (add1 i) j))]\n          [(=\
        \ i s1-len) (vector-set! dp i (vector-ref dp i (add1 j)) (vector-ref dp i (add1\
        \ j)) (+ (char->integer (string-ref s2 j)) (vector-ref (vector-ref dp i (add1\
        \ j)) j)))]\n          [(= j s2-len) (vector-set! dp i (vector-ref dp (add1\
        \ i) j) (+ (char->integer (string-ref s1 i)) (vector-ref (vector-ref dp (add1\
        \ i) j) j)))]\n          [(char=? (string-ref s1 i) (string-ref s2 j)) (vector-set!\
        \ dp i (vector-ref dp (add1 i) (add1 j)) (vector-ref (vector-ref dp (add1 i)\
        \ (add1 j)) j))]\n          [else (vector-set! dp i (vector-ref dp (add1 i)\
        \ j) (min (+ (char->integer (string-ref s1 i)) (vector-ref (vector-ref dp (add1\
        \ i) j) j)) (+ (char->integer (string-ref s2 j)) (vector-ref (vector-ref dp\
        \ i (add1 j)) j))))])\n        (set! j (sub1 j)))\n      (set! i (sub1 i)))\n\
        \    (vector-ref (vector-ref dp 0) 0))"
      erlang: "minimum_delete_sum(S1, S2) ->\n  M = length(S1),\n  N = length(S2),\n\
        \  Dp = array:new({M + 1, N + 1}, 0),\n  fill_dp(S1, S2, Dp, 0, 0),\n  array:get(0,\
        \ 0, Dp).\n\nfill_dp(S1, S2, Dp, M, N) ->\n  array:set(M, N, 0, Dp);\nfill_dp(S1,\
        \ S2, Dp, M, N) when N < length(S2) ->\n  array:set(M, N, array:get(M, N + 1,\
        \ Dp) + element(3, lists:nth(N + 1, S2)), Dp),\n  fill_dp(S1, S2, Dp, M, N +\
        \ 1);\nfill_dp(S1, S2, Dp, M, N) when M < length(S1) ->\n  array:set(M, N, array:get(M\
        \ + 1, N, Dp) + element(3, lists:nth(M + 1, S1)), Dp),\n  fill_dp(S1, S2, Dp,\
        \ M + 1, N);\nfill_dp(S1, S2, Dp, M, N) ->\n  case lists:nth(M + 1, S1) of\n\
        \    X when X == lists:nth(N + 1, S2) ->\n      array:set(M, N, array:get(M\
        \ + 1, N + 1, Dp), Dp),\n      fill_dp(S1, S2, Dp, M + 1, N + 1);\n    _ ->\n\
        \      Val1 = array:get(M + 1, N, Dp) + element(3, lists:nth(M + 1, S1)),\n\
        \      Val2 = array:get(M, N + 1, Dp) + element(3, lists:nth(N + 1, S2)),\n\
        \      array:set(M, N, min(Val1, Val2), Dp),\n      fill_dp(S1, S2, Dp, M +\
        \ 1, N + 1)\n  end."
      elixir: "defmodule Solution do\n  @spec minimum_delete_sum(s1 :: String.t, s2\
        \ :: String.t) :: integer\n  def minimum_delete_sum(s1, s2) do\n    m = String.length(s1)\n\
        \    n = String.length(s2)\n    dp = Array.new(m + 1, n + 1, 0)\n    fill_dp(s1,\
        \ s2, dp, 0, 0)\n    Enum.at(Enum.at(dp, 0), 0)\n  end\n\n  defp fill_dp(s1,\
        \ s2, dp, m, n) when m == String.length(s1) and n == String.length(s2) do\n\
        \    :ok\n  end\n\n  defp fill_dp(s1, s2, dp, m, n) when m == String.length(s1)\
        \ do\n    val = Enum.at(Enum.at(dp, m), n + 1) + String.to_charlist(Enum.at(String.to_charlist(s2),\
        \ n)) |> List.first()\n    dp = Array.update(dp, m, fn x -> List.update_at(x,\
        \ n, fn _ -> val end) end)\n    fill_dp(s1, s2, dp, m, n + 1)\n  end\n\n  defp\
        \ fill_dp(s1, s2, dp, m, n) when n == String.length(s2) do\n    val = Enum.at(Enum.at(dp,\
        \ m + 1), n) + String.to_charlist(Enum.at(String.to_charlist(s1), m)) |> List.first()\n\
        \    dp = Array.update(dp, m, fn x -> List.update_at(x, n, fn _ -> val end)\
        \ end)\n    fill_dp(s1, s2, dp, m + 1, n)\n  end\n\n  defp fill_dp(s1, s2, dp,\
        \ m, n) do\n    if String.at(s1, m) == String.at(s2, n) do\n      dp = Array.update(dp,\
        \ m, fn x -> List.update_at(x, n, fn _ -> Enum.at(Enum.at(dp, m + 1), n + 1)\
        \ end) end)\n      fill_dp(s1, s2, dp, m + 1, n + 1)\n    else\n      val1 =\
        \ Enum.at(Enum.at(dp, m + 1), n) + String.to_charlist(Enum.at(String.to_charlist(s1),\
        \ m)) |> List.first()\n      val2 = Enum.at(Enum.at(dp, m), n + 1) + String.to_charlist(Enum.at(String.to_charlist(s2),\
        \ n)) |> List.first()\n      dp = Array.update(dp, m, fn x -> List.update_at(x,\
        \ n, fn _ -> min(val1, val2) end) end)\n      fill_dp(s1, s2, dp, m + 1, n +\
        \ 1)\n    end\n  end\nend"
    approach: 'The problem can be solved using dynamic programming. We define a function
      dp(i, j) that represents the minimum ASCII sum of deleted characters to make s1[i:]
      and s2[j:] equal. We can calculate dp(i, j) by considering two cases: either the
      current characters in s1 and s2 are equal, or they are not. If they are equal,
      we can simply move to the next characters in both strings. If they are not equal,
      we need to delete one of the characters and add its ASCII value to the sum. We
      choose the character with the smaller ASCII value to delete. The base case is
      when one of the strings is empty, in which case we need to delete all the characters
      in the other string. The final answer is dp(0, 0), which represents the minimum
      ASCII sum of deleted characters to make the entire strings s1 and s2 equal. The
      key intuition is to use dynamic programming to avoid redundant calculations and
      to consider all possible cases of character equality and deletion.'
    time_complexity: The time complexity of the solution is O(m*n), where m and n are
      the lengths of the strings s1 and s2, respectively. This is because we need to
      fill in the dp table of size (m+1) x (n+1), and each cell in the table requires
      a constant amount of time to calculate. The dynamic programming approach allows
      us to avoid redundant calculations and reduce the time complexity from exponential
      to quadratic.
    space_complexity: The space complexity of the solution is O(m*n), where m and n
      are the lengths of the strings s1 and s2, respectively. This is because we need
      to store the dp table of size (m+1) x (n+1) to keep track of the minimum ASCII
      sum of deleted characters for each substring of s1 and s2. The space complexity
      is quadratic because we need to store all the intermediate results in the dp table.
    elapsed_time: 14.924665212631226
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-10 01:10:51 '
---

## Problem #712: Minimum ASCII Delete Sum for Two Strings

**Difficulty:** Medium

**Topics:** String, Dynamic Programming

## Problem Description

<p>Given two strings <code>s1</code> and&nbsp;<code>s2</code>, return <em>the lowest <strong>ASCII</strong> sum of deleted characters to make two strings equal</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;sea&quot;, s2 = &quot;eat&quot;
<strong>Output:</strong> 231
<strong>Explanation:</strong> Deleting &quot;s&quot; from &quot;sea&quot; adds the ASCII value of &quot;s&quot; (115) to the sum.
Deleting &quot;t&quot; from &quot;eat&quot; adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;delete&quot;, s2 = &quot;leet&quot;
<strong>Output:</strong> 403
<strong>Explanation:</strong> Deleting &quot;dee&quot; from &quot;delete&quot; to turn the string into &quot;let&quot;,
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting &quot;e&quot; from &quot;leet&quot; adds 101[e] to the sum.
At the end, both strings are equal to &quot;let&quot;, and the answer is 100+101+101+101 = 403.
If instead we turned both strings into &quot;lee&quot; or &quot;eet&quot;, we would get answers of 433 or 417, which are higher.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s1.length, s2.length &lt;= 1000</code></li>
	<li><code>s1</code> and <code>s2</code> consist of lowercase English letters.</li>
</ul>


## Hints

1. Let dp(i, j) be the answer for inputs s1[i:] and s2[j:].

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2026-01-10 01:10:21 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks for the minimum ASCII sum of deleted characters to make two strings, s1 and s2, equal. This is a classic dynamic programming problem, closely related to the Longest Common Subsequence (LCS) problem. We can define a 2D DP table, `dp[i][j]`, to represent the minimum ASCII sum of deletions required to make the prefix `s1[0...i-1]` equal to the prefix `s2[0...j-1]`. The dimensions of the DP table will be `(len(s1) + 1) x (len(s2) + 1)`.

The base cases for the DP table are as follows: `dp[0][0]` is 0, as two empty strings are already equal with no deletions. For `dp[i][0]`, it means making `s1[0...i-1]` equal to an empty string, which requires deleting all characters in `s1[0...i-1]`. Thus, `dp[i][0] = dp[i-1][0] + ord(s1[i-1])`. Similarly, `dp[0][j] = dp[0][j-1] + ord(s2[j-1])` for making `s2[0...j-1]` equal to an empty string. For the general case `dp[i][j]` where `i > 0` and `j > 0`, we consider two scenarios: if `s1[i-1]` and `s2[j-1]` are equal, no deletion is needed for these characters, so `dp[i][j] = dp[i-1][j-1]`. If they are not equal, we must delete either `s1[i-1]` or `s2[j-1]`. We choose the option that results in the minimum deletion sum: `dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))`. After filling the entire DP table, the final answer will be `dp[len(s1)][len(s2)]`.

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
    int minimumDeleteSum(string s1, string s2) {
        int m = s1.length();
        int n = s2.length();

        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

        // Base cases
        // dp[i][0]: delete all characters from s1[0...i-1] to match empty s2
        for (int i = 1; i <= m; ++i) {
            dp[i][0] = dp[i-1][0] + (int)s1[i-1];
        }
        // dp[0][j]: delete all characters from s2[0...j-1] to match empty s1
        for (int j = 1; j <= n; ++j) {
            dp[0][j] = dp[0][j-1] + (int)s2[j-1];
        }

        // Fill the DP table
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (s1[i-1] == s2[j-1]) {
                    dp[i][j] = dp[i-1][j-1];
                } else {
                    dp[i][j] = min(dp[i-1][j] + (int)s1[i-1], // Delete s1[i-1]
                                   dp[i][j-1] + (int)s2[j-1]); // Delete s2[j-1]
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
    public int minimumDeleteSum(String s1, String s2) {
        int m = s1.length();
        int n = s2.length();

        int[][] dp = new int[m + 1][n + 1];

        // Base cases
        // dp[i][0]: delete all characters from s1[0...i-1] to match empty s2
        for (int i = 1; i <= m; ++i) {
            dp[i][0] = dp[i-1][0] + (int)s1.charAt(i-1);
        }
        // dp[0][j]: delete all characters from s2[0...j-1] to match empty s1
        for (int j = 1; j <= n; ++j) {
            dp[0][j] = dp[0][j-1] + (int)s2.charAt(j-1);
        }

        // Fill the DP table
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (s1.charAt(i-1) == s2.charAt(j-1)) {
                    dp[i][j] = dp[i-1][j-1];
                } else {
                    dp[i][j] = Math.min(dp[i-1][j] + (int)s1.charAt(i-1), // Delete s1[i-1]
                                        dp[i][j-1] + (int)s2.charAt(j-1)); // Delete s2[j-1]
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
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m = len(s1)
        n = len(s2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base cases
        # dp[i][0]: delete all characters from s1[0...i-1] to match empty s2
        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        # dp[0][j]: delete all characters from s2[0...j-1] to match empty s1
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), # Delete s1[i-1]
                                   dp[i][j-1] + ord(s2[j-1])) # Delete s2[j-1]

        return dp[m][n]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base cases
        # dp[i][0]: delete all characters from s1[0...i-1] to match empty s2
        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        # dp[0][j]: delete all characters from s2[0...j-1] to match empty s1
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), # Delete s1[i-1]
                                   dp[i][j-1] + ord(s2[j-1])) # Delete s2[j-1]

        return dp[m][n]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

// Helper for min function
int min(int a, int b) {
    return a < b ? a : b;
}

int minimumDeleteSum(char* s1, char* s2) {
    int m = strlen(s1);
    int n = strlen(s2);

    // Allocate DP table
    int** dp = (int**)malloc((m + 1) * sizeof(int*));
    for (int i = 0; i <= m; ++i) {
        dp[i] = (int*)calloc((n + 1), sizeof(int)); // calloc initializes to 0
    }

    // Base cases
    // dp[i][0]: delete all characters from s1[0...i-1] to match empty s2
    for (int i = 1; i <= m; ++i) {
        dp[i][0] = dp[i-1][0] + (int)s1[i-1];
    }
    // dp[0][j]: delete all characters from s2[0...j-1] to match empty s1
    for (int j = 1; j <= n; ++j) {
        dp[0][j] = dp[0][j-1] + (int)s2[j-1];
    }

    // Fill the DP table
    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (s1[i-1] == s2[j-1]) {
                dp[i][j] = dp[i-1][j-1];
            } else {
                dp[i][j] = min(dp[i-1][j] + (int)s1[i-1], // Delete s1[i-1]
                               dp[i][j-1] + (int)s2[j-1]); // Delete s2[j-1]
            }
        }
    }

    int result = dp[m][n];

    // Free allocated memory
    for (int i = 0; i <= m; ++i) {
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
public class Solution {
    public int MinimumDeleteSum(string s1, string s2) {
        int m = s1.Length;
        int n = s2.Length;

        int[,] dp = new int[m + 1, n + 1];

        // Initialize base cases
        // dp[i][0]: delete all characters from s1[0...i-1]
        for (int i = 1; i <= m; i++) {
            dp[i, 0] = dp[i - 1, 0] + (int)s1[i - 1];
        }
        // dp[0][j]: delete all characters from s2[0...j-1]
        for (int j = 1; j <= n; j++) {
            dp[0, j] = dp[0, j - 1] + (int)s2[j - 1];
        }

        // Fill the DP table
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s1[i - 1] == s2[j - 1]) {
                    dp[i, j] = dp[i - 1, j - 1];
                } else {
                    dp[i, j] = Math.Min(dp[i - 1, j] + (int)s1[i - 1], 
                                        dp[i, j - 1] + (int)s2[j - 1]);
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
 * @param {string} s1
 * @param {string} s2
 * @return {number}
 */
var minimumDeleteSum = function(s1, s2) {
    const m = s1.length;
    const n = s2.length;

    const dp = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));

    // Initialize base cases
    // dp[i][0]: delete all characters from s1[0...i-1]
    for (let i = 1; i <= m; i++) {
        dp[i][0] = dp[i - 1][0] + s1.charCodeAt(i - 1);
    }
    // dp[0][j]: delete all characters from s2[0...j-1]
    for (let j = 1; j <= n; j++) {
        dp[0][j] = dp[0][j - 1] + s2.charCodeAt(j - 1);
    }

    // Fill the DP table
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (s1[i - 1] === s2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                dp[i][j] = Math.min(dp[i - 1][j] + s1.charCodeAt(i - 1), 
                                    dp[i][j - 1] + s2.charCodeAt(j - 1));
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
function minimumDeleteSum(s1: string, s2: string): number {
    const m = s1.length;
    const n = s2.length;

    const dp: number[][] = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));

    // Initialize base cases
    // dp[i][0]: delete all characters from s1[0...i-1]
    for (let i = 1; i <= m; i++) {
        dp[i][0] = dp[i - 1][0] + s1.charCodeAt(i - 1);
    }
    // dp[0][j]: delete all characters from s2[0...j-1]
    for (let j = 1; j <= n; j++) {
        dp[0][j] = dp[0][j - 1] + s2.charCodeAt(j - 1);
    }

    // Fill the DP table
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (s1[i - 1] === s2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                dp[i][j] = Math.min(dp[i - 1][j] + s1.charCodeAt(i - 1), 
                                    dp[i][j - 1] + s2.charCodeAt(j - 1));
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
     * @param String $s1
     * @param String $s2
     * @return Integer
     */
    function minimumDeleteSum($s1, $s2) {
        $m = strlen($s1);
        $n = strlen($s2);

        $dp = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));

        // Initialize base cases
        // dp[i][0]: delete all characters from s1[0...i-1]
        for ($i = 1; $i <= $m; $i++) {
            $dp[$i][0] = $dp[$i - 1][0] + ord($s1[$i - 1]);
        }
        // dp[0][j]: delete all characters from s2[0...j-1]
        for ($j = 1; $j <= $n; $j++) {
            $dp[0][$j] = $dp[0][$j - 1] + ord($s2[$j - 1]);
        }

        // Fill the DP table
        for ($i = 1; $i <= $m; $i++) {
            for ($j = 1; $j <= $n; $j++) {
                if ($s1[$i - 1] === $s2[$j - 1]) {
                    $dp[$i][$j] = $dp[$i - 1][$j - 1];
                } else {
                    $dp[$i][$j] = min($dp[$i - 1][$j] + ord($s1[$i - 1]), 
                                      $dp[$i][$j - 1] + ord($s2[$j - 1]));
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
    func minimumDeleteSum(_ s1: String, _ s2: String) -> Int {
        let m = s1.count
        let n = s2.count

        var dp = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)

        let s1Chars = Array(s1)
        let s2Chars = Array(s2)

        // Initialize base cases
        // dp[i][0]: delete all characters from s1[0...i-1]
        for i in 1...m {
            dp[i][0] = dp[i - 1][0] + Int(s1Chars[i - 1].asciiValue!)
        }
        // dp[0][j]: delete all characters from s2[0...j-1]
        for j in 1...n {
            dp[0][j] = dp[0][j - 1] + Int(s2Chars[j - 1].asciiValue!)
        }

        // Fill the DP table
        for i in 1...m {
            for j in 1...n {
                if s1Chars[i - 1] == s2Chars[j - 1] {
                    dp[i][j] = dp[i - 1][j - 1]
                } else {
                    dp[i][j] = min(dp[i - 1][j] + Int(s1Chars[i - 1].asciiValue!), 
                                   dp[i][j - 1] + Int(s2Chars[j - 1].asciiValue!))
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
    fun minimumDeleteSum(s1: String, s2: String): Int {
        val n = s1.length
        val m = s2.length

        val dp = Array(n + 1) { IntArray(m + 1) }

        for (j in 1..m) {
            dp[0][j] = dp[0][j - 1] + s2[j - 1].toInt()
        }

        for (i in 1..n) {
            dp[i][0] = dp[i - 1][0] + s1[i - 1].toInt()
        }

        for (i in 1..n) {
            for (j in 1..m) {
                if (s1[i - 1] == s2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1]
                } else {
                    val cost1 = dp[i - 1][j] + s1[i - 1].toInt()
                    val cost2 = dp[i][j - 1] + s2[j - 1].toInt()
                    dp[i][j] = minOf(cost1, cost2)
                }
            }
        }

        return dp[n][m]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minimumDeleteSum(String s1, String s2) {
    final n = s1.length;
    final m = s2.length;

    final dp = List.generate(n + 1, (_) => List.filled(m + 1, 0));

    for (int j = 1; j <= m; j++) {
      dp[0][j] = dp[0][j - 1] + s2.codeUnitAt(j - 1);
    }

    for (int i = 1; i <= n; i++) {
      dp[i][0] = dp[i - 1][0] + s1.codeUnitAt(i - 1);
    }

    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= m; j++) {
        if (s1[i - 1] == s2[j - 1]) {
          dp[i][j] = dp[i - 1][j - 1];
        } else {
          final cost1 = dp[i - 1][j] + s1.codeUnitAt(i - 1);
          final cost2 = dp[i][j - 1] + s2.codeUnitAt(j - 1);
          dp[i][j] = cost1 < cost2 ? cost1 : cost2;
        }
      }
    }

    return dp[n][m];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minimumDeleteSum(s1 string, s2 string) int {
    n := len(s1)
    m := len(s2)

    dp := make([][]int, n+1)
    for i := range dp {
        dp[i] = make([]int, m+1)
    }

    for j := 1; j <= m; j++ {
        dp[0][j] = dp[0][j-1] + int(s2[j-1])
    }

    for i := 1; i <= n; i++ {
        dp[i][0] = dp[i-1][0] + int(s1[i-1])
    }

    for i := 1; i <= n; i++ {
        for j := 1; j <= m; j++ {
            if s1[i-1] == s2[j-1] {
                dp[i][j] = dp[i-1][j-1]
            } else {
                cost1 := dp[i-1][j] + int(s1[i-1])
                cost2 := dp[i][j-1] + int(s2[j-1])
                if cost1 < cost2 {
                    dp[i][j] = cost1
                } else {
                    dp[i][j] = cost2
                }
            }
        }
    }

    return dp[n][m]
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s1
# @param {String} s2
# @return {Integer}
def minimum_delete_sum(s1, s2)
    n = s1.length
    m = s2.length

    dp = Array.new(n + 1) { Array.new(m + 1, 0) }

    (1..m).each do |j|
        dp[0][j] = dp[0][j - 1] + s2[j - 1].ord
    end

    (1..n).each do |i|
        dp[i][0] = dp[i - 1][0] + s1[i - 1].ord
    end

    (1..n).each do |i|
        (1..m).each do |j|
            if s1[i - 1] == s2[j - 1]
                dp[i][j] = dp[i - 1][j - 1]
            else
                cost1 = dp[i - 1][j] + s1[i - 1].ord
                cost2 = dp[i][j - 1] + s2[j - 1].ord
                dp[i][j] = [cost1, cost2].min
            end
        end
    end

    dp[n][m]
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minimumDeleteSum(s1: String, s2: String): Int = {
        val n = s1.length
        val m = s2.length

        val dp = Array.ofDim[Int](n + 1, m + 1)

        for (j <- 1 to m) {
            dp(0)(j) = dp(0)(j - 1) + s2(j - 1).toInt
        }

        for (i <- 1 to n) {
            dp(i)(0) = dp(i - 1)(0) + s1(i - 1).toInt
        }

        for (i <- 1 to n) {
            for (j <- 1 to m) {
                if (s1(i - 1) == s2(j - 1)) {
                    dp(i)(j) = dp(i - 1)(j - 1)
                } else {
                    val cost1 = dp(i - 1)(j) + s1(i - 1).toInt
                    val cost2 = dp(i)(j - 1) + s2(j - 1).toInt
                    dp(i)(j) = Math.min(cost1, cost2)
                }
            }
        }

        dp(n)(m)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn minimum_delete_sum(s1: String, s2: String) -> i32 {
        let s1_bytes = s1.as_bytes();
        let s2_bytes = s2.as_bytes();
        let m = s1_bytes.len();
        let n = s2_bytes.len();

        let mut dp = vec![vec![0; n + 1]; m + 1];

        let mut total_ascii_sum = 0;
        for &c in s1_bytes {
            total_ascii_sum += c as i32;
        }
        for &c in s2_bytes {
            total_ascii_sum += c as i32;
        }

        for i in 1..=m {
            for j in 1..=n {
                if s1_bytes[i - 1] == s2_bytes[j - 1] {
                    dp[i][j] = dp[i - 1][j - 1] + s1_bytes[i - 1] as i32;
                } else {
                    dp[i][j] = dp[i - 1][j].max(dp[i][j - 1]);
                }
            }
        }

        total_ascii_sum - 2 * dp[m][n]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (minimum-delete-sum s1 s2)
  (-> string? string? exact-integer?)
  (let* ([m (string-length s1)]
         [n (string-length s2)]
         [dp (build-vector (+ m 1) (lambda (i) (build-vector (+ n 1) (lambda (j) 0))))]
         [total-ascii-sum 0])

    ;; Calculate total ASCII sum
    (for ([char (string->list s1)])
      (set! total-ascii-sum (+ total-ascii-sum (char->integer char))))
    (for ([char (string->list s2)])
      (set! total-ascii-sum (+ total-ascii-sum (char->integer char))))

    ;; Fill DP table
    (for ([i (in-range 1 (+ m 1))])
      (for ([j (in-range 1 (+ n 1))])
        (if (char=? (string-ref s1 (- i 1)) (string-ref s2 (- j 1)))
            (vector-set! (vector-ref dp i) j
                         (+ (vector-ref (vector-ref dp (- i 1)) (- j 1))
                            (char->integer (string-ref s1 (- i 1)))))
            (vector-set! (vector-ref dp i) j
                         (max (vector-ref (vector-ref dp (- i 1)) j)
                              (vector-ref (vector-ref dp i) (- j 1)))))))

    (- total-ascii-sum (* 2 (vector-ref (vector-ref dp m) n)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec minimum_delete_sum(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary()) -> integer().
minimum_delete_sum(S1, S2) ->
    S1Chars = binary_to_list(S1), % List of integers (ASCII values)
    S2Chars = binary_to_list(S2),
    M = length(S1Chars),
    N = length(S2Chars),

    TotalAsciiSum = lists:sum(S1Chars) + lists:sum(S2Chars),

    % dp_prev_row represents dp[i-1][0...N]
    % Initialize dp_prev_row (for i=0)
    DpPrevRow = lists:duplicate(N + 1, 0),

    LCS_Sum = calculate_lcs_sum_erlang(S1Chars, S2Chars, DpPrevRow),

    TotalAsciiSum - 2 * LCS_Sum.

% S1Chars: remaining S1 characters to process
% S2Chars: full S2 list (for reference)
% DpPrevRow: list representing dp[i-1][0...N]
calculate_lcs_sum_erlang([], _S2Chars, DpPrevRow) ->
    % All S1Chars processed, DpPrevRow is now the last row (dp[M])
    lists:last(DpPrevRow);
calculate_lcs_sum_erlang([S1Char | RestS1Chars], S2Chars, DpPrevRow) ->
    % Build DpCurrRow for current S1Char
    % DpCurrRow starts with dp[i][0] = 0
    DpCurrRow = build_dp_current_row_erlang(S1Char, S2Chars, DpPrevRow, 0, [0]),

    calculate_lcs_sum_erlang(RestS1Chars, S2Chars, DpCurrRow).

% S1Char: current char from s1 (S1Chars[i])
% S2Chars: remaining S2 characters to process (S2Chars[j...N-1])
% DpPrevRow: list representing dp[i-1][0...N]
% DpCurrRowPrevColVal: dp[i][j] (value from current row, previous column)
% AccCurrRow: accumulator for current row (built in reverse, starting with dp[i][0])
build_dp_current_row_erlang(_S1Char, [], _DpPrevRow, _DpCurrRowPrevColVal, AccCurrRow) ->
    % All S2Chars processed for current row
    lists:reverse(AccCurrRow);
build_dp_current_row_erlang(S1Char, [S2Char | RestS2Chars], [PrevDiagVal | [PrevUpVal | RestDpPrevRow]], DpCurrRowPrevColVal, AccCurrRow) ->
    % PrevDiagVal is dp[i-1][j-1]
    % PrevUpVal is dp[i-1][j]
    % DpCurrRowPrevColVal is dp[i][j-1]

    Val = if
        S1Char =:= S2Char ->
            PrevDiagVal + S1Char;
        true ->
            max(PrevUpVal, DpCurrRowPrevColVal)
    end,
    build_dp_current_row_erlang(S1Char, RestS2Chars, [PrevUpVal | RestDpPrevRow], Val, [Val | AccCurrRow]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_delete_sum(s1 :: String.t, s2 :: String.t) :: integer
  def minimum_delete_sum(s1, s2) do
    s1_chars = String.to_charlist(s1)
    s2_chars = String.to_charlist(s2)
    m = length(s1_chars)
    n = length(s2_chars)

    total_ascii_sum = Enum.sum(s1_chars) + Enum.sum(s2_chars)

    # dp_prev_row represents dp[i-1][0...N]
    # Initialize dp_prev_row (for i=0)
    dp_prev_row = List.duplicate(0, n + 1)

    lcs_sum =
      Enum.reduce(s1_chars, dp_prev_row, fn s1_char, acc_dp_prev_row ->
        # acc_dp_prev_row is dp[i-1][0...N]
        # Build dp_curr_row for current s1_char (dp[i][0...N])
        build_dp_current_row_elixir(s1_char, s2_chars, acc_dp_prev_row)
      end)
      |> List.last()

    total_ascii_sum - 2 * lcs_sum
  end

  # s1_char: current char from s1 (s1_chars[i])
  # s2_chars: full s2 list (for reference)
  # dp_prev_row: list representing dp[i-1][0...N]
  defp build_dp_current_row_elixir(s1_char, s2_chars, dp_prev_row) do
    # State for reduce: {current_dp_row_reversed, prev_col_val_in_curr_row, dp_prev_row_tail}
    # current_dp_row_reversed: [dp[i][j], dp[i][j-1], ..., dp[i][0]]
    # prev_col_val_in_curr_row: dp[i][j-1]
    # dp_prev_row_tail: [dp[i-1][j], dp[i-1][j+1], ...]

    {final_dp_curr_row_reversed, _prev_col_val, _dp_prev_row_tail} =
      Enum.reduce(s2_chars, {[0], 0, dp_prev_row}, fn s2_char, {acc_curr_row_rev, prev_col_val_in_curr_row, [prev_diag_val | [prev_up_val | rest_dp_prev_row]]} ->
        val = if s1_char == s2_char do
          prev_diag_val + s1_char
        else
          max(prev_up_val, prev_col_val_in_curr_row)
        end
        {[val | acc_curr_row_rev], val, [prev_up_val | rest_dp_prev_row]}
      end)

    Enum.reverse(final_dp_curr_row_reversed)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(m * n), where m is the length of string s1 and n is the length of string s2. This is because we iterate through each cell of the `(m+1) x (n+1)` DP table once, and each cell computation takes constant time.

- **Space Complexity:** The space complexity is O(m * n), where m is the length of string s1 and n is the length of string s2. This is due to the storage required for the 2D DP table. This can be optimized to O(min(m, n)) by only keeping track of the current and previous rows, but for clarity and given the constraints (lengths up to 1000), O(m*n) is acceptable.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-10 01:10:51 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved using dynamic programming. We define a function dp(i, j) that represents the minimum ASCII sum of deleted characters to make s1[i:] and s2[j:] equal. We can calculate dp(i, j) by considering two cases: either the current characters in s1 and s2 are equal, or they are not. If they are equal, we can simply move to the next characters in both strings. If they are not equal, we need to delete one of the characters and add its ASCII value to the sum. We choose the character with the smaller ASCII value to delete. The base case is when one of the strings is empty, in which case we need to delete all the characters in the other string. The final answer is dp(0, 0), which represents the minimum ASCII sum of deleted characters to make the entire strings s1 and s2 equal. The key intuition is to use dynamic programming to avoid redundant calculations and to consider all possible cases of character equality and deletion.

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
    int minimumDeleteSum(string s1, string s2) {
        int m = s1.size(), n = s2.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        for (int i = 1; i <= m; i++) dp[i][0] = dp[i - 1][0] + s1[i - 1];
        for (int j = 1; j <= n; j++) dp[0][j] = dp[0][j - 1] + s2[j - 1];
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s1[i - 1] == s2[j - 1]) dp[i][j] = dp[i - 1][j - 1];
                else dp[i][j] = min(dp[i - 1][j] + s1[i - 1], dp[i][j - 1] + s2[j - 1]);
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
    public int minimumDeleteSum(String s1, String s2) {
        int m = s1.length(), n = s2.length();
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 1; i <= m; i++) dp[i][0] = dp[i - 1][0] + s1.charAt(i - 1);
        for (int j = 1; j <= n; j++) dp[0][j] = dp[0][j - 1] + s2.charAt(j - 1);
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) dp[i][j] = dp[i - 1][j - 1];
                else dp[i][j] = Math.min(dp[i - 1][j] + s1.charAt(i - 1), dp[i][j - 1] + s2.charAt(j - 1));
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
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1): dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
        for j in range(1, n + 1): dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]: dp[i][j] = dp[i - 1][j - 1]
                else: dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))
        return dp[m][n]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1): dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
        for j in range(1, n + 1): dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]: dp[i][j] = dp[i - 1][j - 1]
                else: dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))
        return dp[m][n]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int minimumDeleteSum(char* s1, char* s2) {
    int m = strlen(s1), n = strlen(s2);
    int** dp = (int**)malloc((m + 1) * sizeof(int*));
    for (int i = 0; i <= m; i++) dp[i] = (int*)malloc((n + 1) * sizeof(int));
    for (int i = 1; i <= m; i++) dp[i][0] = dp[i - 1][0] + s1[i - 1];
    for (int j = 1; j <= n; j++) dp[0][j] = dp[0][j - 1] + s2[j - 1];
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (s1[i - 1] == s2[j - 1]) dp[i][j] = dp[i - 1][j - 1];
            else dp[i][j] = (dp[i - 1][j] + s1[i - 1] < dp[i][j - 1] + s2[j - 1]) ? dp[i - 1][j] + s1[i - 1] : dp[i][j - 1] + s2[j - 1];
        }
    }
    int result = dp[m][n];
    for (int i = 0; i <= m; i++) free(dp[i]);
    free(dp);
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinimumDeleteSum(string s1, string s2) {
        int m = s1.Length;
        int n = s2.Length;
        int[,] dp = new int[m + 1, n + 1];
        for (int i = 1; i <= m; i++) {
            dp[i, 0] = dp[i - 1, 0] + s1[i - 1];
        }
        for (int j = 1; j <= n; j++) {
            dp[0, j] = dp[0, j - 1] + s2[j - 1];
        }
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s1[i - 1] == s2[j - 1]) {
                    dp[i, j] = dp[i - 1, j - 1];
                } else {
                    dp[i, j] = Math.Min(dp[i - 1, j] + s1[i - 1], dp[i, j - 1] + s2[j - 1]);
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
var minimumDeleteSum = function(s1, s2) {
    let m = s1.length;
    let n = s2.length;
    let dp = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));
    for (let i = 1; i <= m; i++) {
        dp[i][0] = dp[i - 1][0] + s1.charCodeAt(i - 1);
    }
    for (let j = 1; j <= n; j++) {
        dp[0][j] = dp[0][j - 1] + s2.charCodeAt(j - 1);
    }
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (s1[i - 1] === s2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                dp[i][j] = Math.min(dp[i - 1][j] + s1.charCodeAt(i - 1), dp[i][j - 1] + s2.charCodeAt(j - 1));
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
function minimumDeleteSum(s1: string, s2: string): number {
    let m: number = s1.length;
    let n: number = s2.length;
    let dp: number[][] = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));
    for (let i = 1; i <= m; i++) {
        dp[i][0] = dp[i - 1][0] + s1.charCodeAt(i - 1);
    }
    for (let j = 1; j <= n; j++) {
        dp[0][j] = dp[0][j - 1] + s2.charCodeAt(j - 1);
    }
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (s1[i - 1] === s2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                dp[i][j] = Math.min(dp[i - 1][j] + s1.charCodeAt(i - 1), dp[i][j - 1] + s2.charCodeAt(j - 1));
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
    function minimumDeleteSum($s1, $s2) {
        $m = strlen($s1);
        $n = strlen($s2);
        $dp = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));
        for ($i = 1; $i <= $m; $i++) {
            $dp[$i][0] = $dp[$i - 1][0] + ord($s1[$i - 1]);
        }
        for ($j = 1; $j <= $n; $j++) {
            $dp[0][$j] = $dp[0][$j - 1] + ord($s2[$j - 1]);
        }
        for ($i = 1; $i <= $m; $i++) {
            for ($j = 1; $j <= $n; $j++) {
                if ($s1[$i - 1] === $s2[$j - 1]) {
                    $dp[$i][$j] = $dp[$i - 1][$j - 1];
                } else {
                    $dp[$i][$j] = min($dp[$i - 1][$j] + ord($s1[$i - 1]), $dp[$i][$j - 1] + ord($s2[$j - 1]));
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
    func minimumDeleteSum(_ s1: String, _ s2: String) -> Int {
        let m = s1.count
        let n = s2.count
        var dp = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)
        for i in 1...m {
            dp[i][0] = dp[i - 1][0] + Int(s1[s1.index(s1.startIndex, offsetBy: i - 1)].asciiValue!)
        }
        for j in 1...n {
            dp[0][j] = dp[0][j - 1] + Int(s2[s2.index(s2.startIndex, offsetBy: j - 1)].asciiValue!)
        }
        for i in 1...m {
            for j in 1...n {
                if s1[s1.index(s1.startIndex, offsetBy: i - 1)] == s2[s2.index(s2.startIndex, offsetBy: j - 1)] {
                    dp[i][j] = dp[i - 1][j - 1]
                } else {
                    dp[i][j] = min(dp[i - 1][j] + Int(s1[s1.index(s1.startIndex, offsetBy: i - 1)].asciiValue!), dp[i][j - 1] + Int(s2[s2.index(s2.startIndex, offsetBy: j - 1)].asciiValue!))
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
    fun minimumDeleteSum(s1: String, s2: String): Int {
        val m = s1.length
        val n = s2.length
        val dp = Array(m + 1) { IntArray(n + 1) }
        for (i in m - 1 downTo 0) {
            dp[i][n] = dp[i + 1][n] + s1[i].toInt()
        }
        for (j in n - 1 downTo 0) {
            dp[m][j] = dp[m][j + 1] + s2[j].toInt()
        }
        for (i in m - 1 downTo 0) {
            for (j in n - 1 downTo 0) {
                if (s1[i] == s2[j]) {
                    dp[i][j] = dp[i + 1][j + 1]
                } else {
                    dp[i][j] = Math.min(dp[i + 1][j] + s1[i].toInt(), dp[i][j + 1] + s2[j].toInt())
                }
            }
        }
        return dp[0][0]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minimumDeleteSum(String s1, String s2) {
    int m = s1.length;
    int n = s2.length;
    List<List<int>> dp = List.generate(m + 1, (i) => List.generate(n + 1, (j) => 0));
    for (int i = m - 1; i >= 0; i--) {
      dp[i][n] = dp[i + 1][n] + s1.codeUnitAt(i);
    }
    for (int j = n - 1; j >= 0; j--) {
      dp[m][j] = dp[m][j + 1] + s2.codeUnitAt(j);
    }
    for (int i = m - 1; i >= 0; i--) {
      for (int j = n - 1; j >= 0; j--) {
        if (s1[i] == s2[j]) {
          dp[i][j] = dp[i + 1][j + 1];
        } else {
          dp[i][j] = (dp[i + 1][j] + s1.codeUnitAt(i)).min(dp[i][j + 1] + s2.codeUnitAt(j));
        }
      }
    }
    return dp[0][0];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minimumDeleteSum(s1 string, s2 string) int {
    m, n := len(s1), len(s2)
    dp := make([][]int, m + 1)
    for i := range dp {
        dp[i] = make([]int, n + 1)
    }
    for i := m - 1; i >= 0; i-- {
        dp[i][n] = dp[i + 1][n] + int(s1[i])
    }
    for j := n - 1; j >= 0; j-- {
        dp[m][j] = dp[m][j + 1] + int(s2[j])
    }
    for i := m - 1; i >= 0; i-- {
        for j := n - 1; j >= 0; j-- {
            if s1[i] == s2[j] {
                dp[i][j] = dp[i + 1][j + 1]
            } else {
                dp[i][j] = min(dp[i + 1][j] + int(s1[i]), dp[i][j + 1] + int(s2[j]))
            }
        }
    }
    return dp[0][0]
}

func min(a, b int) int {
    if a < b {
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
# @param {String} s1
# @param {String} s2
# @return {Integer}
def minimum_delete_sum(s1, s2)
    m, n = s1.length, s2.length
    dp = Array.new(m + 1) { Array.new(n + 1, 0) }
    (m - 1).downto(0) do |i|
        dp[i][n] = dp[i + 1][n] + s1[i].ord
    end
    (n - 1).downto(0) do |j|
        dp[m][j] = dp[m][j + 1] + s2[j].ord
    end
    (m - 1).downto(0) do |i|
        (n - 1).downto(0) do |j|
            if s1[i] == s2[j]
                dp[i][j] = dp[i + 1][j + 1]
            else
                dp[i][j] = [dp[i + 1][j] + s1[i].ord, dp[i][j + 1] + s2[j].ord].min
            end
        end
    end
    dp[0][0]
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minimumDeleteSum(s1: String, s2: String): Int = {
        val m = s1.length
        val n = s2.length
        val dp = Array.ofDim[Int](m + 1, n + 1)
        for (i <- m - 1 to 0 by -1) {
            dp(i)(n) = dp(i + 1)(n) + s1(i)
        }
        for (j <- n - 1 to 0 by -1) {
            dp(m)(j) = dp(m)(j + 1) + s2(j)
        }
        for (i <- m - 1 to 0 by -1) {
            for (j <- n - 1 to 0 by -1) {
                if (s1(i) == s2(j)) {
                    dp(i)(j) = dp(i + 1)(j + 1)
                } else {
                    dp(i)(j) = Math.min(dp(i + 1)(j) + s1(i), dp(i)(j + 1) + s2(j))
                }
            }
        }
        dp(0)(0)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn minimum_delete_sum(s1: String, s2: String) -> i32 {
        let s1 = s1.as_bytes();
        let s2 = s2.as_bytes();
        let m = s1.len();
        let n = s2.len();
        let mut dp = vec![vec![0; n + 1]; m + 1];
        for i in (0..=m).rev() {
            for j in (0..=n).rev() {
                if i == m && j == n {
                    dp[i][j] = 0;
                } else if i == m {
                    dp[i][j] = dp[i][j + 1] + s2[j] as i32;
                } else if j == n {
                    dp[i][j] = dp[i + 1][j] + s1[i] as i32;
                } else if s1[i] == s2[j] {
                    dp[i][j] = dp[i + 1][j + 1];
                } else {
                    dp[i][j] = std::cmp::min(dp[i + 1][j] + s1[i] as i32, dp[i][j + 1] + s2[j] as i32);
                }
            }
        }
        dp[0][0]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
define/contract (minimum-delete-sum s1 s2)
  (-> string? string? exact-integer?)
  (let* (
    [s1-len (string-length s1)]
    [s2-len (string-length s2)]
    [dp (make-vector (add1 s1-len) (make-vector (add1 s2-len) 0))])
    (do (
      [i (sub1 s1-len)])
      [(< i 0)]
      (do (
        [j (sub1 s2-len)])
        [(< j 0)]
        (cond
          [(and (= i s1-len) (= j s2-len)) (vector-set! dp i (vector-ref dp (add1 i) j))]
          [(= i s1-len) (vector-set! dp i (vector-ref dp i (add1 j)) (vector-ref dp i (add1 j)) (+ (char->integer (string-ref s2 j)) (vector-ref (vector-ref dp i (add1 j)) j)))]
          [(= j s2-len) (vector-set! dp i (vector-ref dp (add1 i) j) (+ (char->integer (string-ref s1 i)) (vector-ref (vector-ref dp (add1 i) j) j)))]
          [(char=? (string-ref s1 i) (string-ref s2 j)) (vector-set! dp i (vector-ref dp (add1 i) (add1 j)) (vector-ref (vector-ref dp (add1 i) (add1 j)) j))]
          [else (vector-set! dp i (vector-ref dp (add1 i) j) (min (+ (char->integer (string-ref s1 i)) (vector-ref (vector-ref dp (add1 i) j) j)) (+ (char->integer (string-ref s2 j)) (vector-ref (vector-ref dp i (add1 j)) j))))])
        (set! j (sub1 j)))
      (set! i (sub1 i)))
    (vector-ref (vector-ref dp 0) 0))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
minimum_delete_sum(S1, S2) ->
  M = length(S1),
  N = length(S2),
  Dp = array:new({M + 1, N + 1}, 0),
  fill_dp(S1, S2, Dp, 0, 0),
  array:get(0, 0, Dp).

fill_dp(S1, S2, Dp, M, N) ->
  array:set(M, N, 0, Dp);
fill_dp(S1, S2, Dp, M, N) when N < length(S2) ->
  array:set(M, N, array:get(M, N + 1, Dp) + element(3, lists:nth(N + 1, S2)), Dp),
  fill_dp(S1, S2, Dp, M, N + 1);
fill_dp(S1, S2, Dp, M, N) when M < length(S1) ->
  array:set(M, N, array:get(M + 1, N, Dp) + element(3, lists:nth(M + 1, S1)), Dp),
  fill_dp(S1, S2, Dp, M + 1, N);
fill_dp(S1, S2, Dp, M, N) ->
  case lists:nth(M + 1, S1) of
    X when X == lists:nth(N + 1, S2) ->
      array:set(M, N, array:get(M + 1, N + 1, Dp), Dp),
      fill_dp(S1, S2, Dp, M + 1, N + 1);
    _ ->
      Val1 = array:get(M + 1, N, Dp) + element(3, lists:nth(M + 1, S1)),
      Val2 = array:get(M, N + 1, Dp) + element(3, lists:nth(N + 1, S2)),
      array:set(M, N, min(Val1, Val2), Dp),
      fill_dp(S1, S2, Dp, M + 1, N + 1)
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_delete_sum(s1 :: String.t, s2 :: String.t) :: integer
  def minimum_delete_sum(s1, s2) do
    m = String.length(s1)
    n = String.length(s2)
    dp = Array.new(m + 1, n + 1, 0)
    fill_dp(s1, s2, dp, 0, 0)
    Enum.at(Enum.at(dp, 0), 0)
  end

  defp fill_dp(s1, s2, dp, m, n) when m == String.length(s1) and n == String.length(s2) do
    :ok
  end

  defp fill_dp(s1, s2, dp, m, n) when m == String.length(s1) do
    val = Enum.at(Enum.at(dp, m), n + 1) + String.to_charlist(Enum.at(String.to_charlist(s2), n)) |> List.first()
    dp = Array.update(dp, m, fn x -> List.update_at(x, n, fn _ -> val end) end)
    fill_dp(s1, s2, dp, m, n + 1)
  end

  defp fill_dp(s1, s2, dp, m, n) when n == String.length(s2) do
    val = Enum.at(Enum.at(dp, m + 1), n) + String.to_charlist(Enum.at(String.to_charlist(s1), m)) |> List.first()
    dp = Array.update(dp, m, fn x -> List.update_at(x, n, fn _ -> val end) end)
    fill_dp(s1, s2, dp, m + 1, n)
  end

  defp fill_dp(s1, s2, dp, m, n) do
    if String.at(s1, m) == String.at(s2, n) do
      dp = Array.update(dp, m, fn x -> List.update_at(x, n, fn _ -> Enum.at(Enum.at(dp, m + 1), n + 1) end) end)
      fill_dp(s1, s2, dp, m + 1, n + 1)
    else
      val1 = Enum.at(Enum.at(dp, m + 1), n) + String.to_charlist(Enum.at(String.to_charlist(s1), m)) |> List.first()
      val2 = Enum.at(Enum.at(dp, m), n + 1) + String.to_charlist(Enum.at(String.to_charlist(s2), n)) |> List.first()
      dp = Array.update(dp, m, fn x -> List.update_at(x, n, fn _ -> min(val1, val2) end) end)
      fill_dp(s1, s2, dp, m + 1, n + 1)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of the solution is O(m*n), where m and n are the lengths of the strings s1 and s2, respectively. This is because we need to fill in the dp table of size (m+1) x (n+1), and each cell in the table requires a constant amount of time to calculate. The dynamic programming approach allows us to avoid redundant calculations and reduce the time complexity from exponential to quadratic.

- **Space Complexity:** The space complexity of the solution is O(m*n), where m and n are the lengths of the strings s1 and s2, respectively. This is because we need to store the dp table of size (m+1) x (n+1) to keep track of the minimum ASCII sum of deleted characters for each substring of s1 and s2. The space complexity is quadratic because we need to store all the intermediate results in the dp table.

</div>
</details>
