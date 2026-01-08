---
layout: post
title: "Max Dot Product of Two Subsequences"
date: 2026-01-08 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Dynamic Programming"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/max-dot-product-of-two-subsequences/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxDotProduct(std::vector<int>& nums1,\
        \ std::vector<int>& nums2) {\n        int m = nums1.size();\n        int n =\
        \ nums2.size();\n\n        std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n\
        \ + 1, std::numeric_limits<int>::min()));\n\n        for (int i = 1; i <= m;\
        \ ++i) {\n            for (int j = 1; j <= n; ++j) {\n                int current_product\
        \ = nums1[i-1] * nums2[j-1];\n\n                int val_if_included = current_product\
        \ + std::max(0, dp[i-1][j-1]);\n\n                int val_if_skip_nums1_i =\
        \ dp[i-1][j];\n\n                int val_if_skip_nums2_j = dp[i][j-1];\n\n \
        \               dp[i][j] = std::max(val_if_included, std::max(val_if_skip_nums1_i,\
        \ val_if_skip_nums2_j));\n            }\n        }\n\n        return dp[m][n];\n\
        \    }\n};"
      java: "import java.util.Arrays;\n\nclass Solution {\n    public int maxDotProduct(int[]\
        \ nums1, int[] nums2) {\n        int m = nums1.length;\n        int n = nums2.length;\n\
        \n        int[][] dp = new int[m + 1][n + 1];\n        for (int i = 0; i <=\
        \ m; i++) {\n            Arrays.fill(dp[i], Integer.MIN_VALUE);\n        }\n\
        \n        for (int i = 1; i <= m; i++) {\n            for (int j = 1; j <= n;\
        \ j++) {\n                int current_product = nums1[i-1] * nums2[j-1];\n\n\
        \                int val_if_included = current_product + Math.max(0, dp[i-1][j-1]);\n\
        \n                int val_if_skip_nums1_i = dp[i-1][j];\n\n                int\
        \ val_if_skip_nums2_j = dp[i][j-1];\n\n                dp[i][j] = Math.max(val_if_included,\
        \ Math.max(val_if_skip_nums1_i, val_if_skip_nums2_j));\n            }\n    \
        \    }\n\n        return dp[m][n];\n    }\n}"
      python: "import math\n\nclass Solution(object):\n    def maxDotProduct(self, nums1,\
        \ nums2):\n        \"\"\"\n        :type nums1: List[int]\n        :type nums2:\
        \ List[int]\n        :rtype: int\n        \"\"\"\n        m, n = len(nums1),\
        \ len(nums2)\n\n        dp = [[-math.inf] * (n + 1) for _ in range(m + 1)]\n\
        \n        for i in range(1, m + 1):\n            for j in range(1, n + 1):\n\
        \                current_product = nums1[i-1] * nums2[j-1]\n\n             \
        \   val_if_included = current_product + max(0, dp[i-1][j-1])\n\n           \
        \     val_if_skip_nums1_i = dp[i-1][j]\n\n                val_if_skip_nums2_j\
        \ = dp[i][j-1]\n\n                dp[i][j] = max(val_if_included, val_if_skip_nums1_i,\
        \ val_if_skip_nums2_j)\n\n        return dp[m][n]"
      python3: "import math\n\nclass Solution:\n    def maxDotProduct(self, nums1: List[int],\
        \ nums2: List[int]) -> int:\n        m, n = len(nums1), len(nums2)\n\n     \
        \   dp = [[-math.inf] * (n + 1) for _ in range(m + 1)]\n\n        for i in range(1,\
        \ m + 1):\n            for j in range(1, n + 1):\n                current_product\
        \ = nums1[i-1] * nums2[j-1]\n\n                val_if_included = current_product\
        \ + max(0, dp[i-1][j-1])\n\n                val_if_skip_nums1_i = dp[i-1][j]\n\
        \n                val_if_skip_nums2_j = dp[i][j-1]\n\n                dp[i][j]\
        \ = max(val_if_included, val_if_skip_nums1_i, val_if_skip_nums2_j)\n\n     \
        \   return dp[m][n]"
      c: "#include <stdlib.h> // For malloc, free\n#include <limits.h> // For INT_MIN\n\
        \n// Helper function for max of two integers\nint max(int a, int b) {\n    return\
        \ a > b ? a : b;\n}\n\n// Helper function for max of three integers\nint max3(int\
        \ a, int b, int c) {\n    return max(a, max(b, c));\n}\n\nint maxDotProduct(int*\
        \ nums1, int nums1Size, int* nums2, int nums2Size) {\n    int m = nums1Size;\n\
        \    int n = nums2Size;\n\n    int** dp = (int**)malloc((m + 1) * sizeof(int*));\n\
        \    for (int i = 0; i <= m; i++) {\n        dp[i] = (int*)malloc((n + 1) *\
        \ sizeof(int));\n        for (int j = 0; j <= n; j++) {\n            dp[i][j]\
        \ = INT_MIN;\n        }\n    }\n\n    for (int i = 1; i <= m; i++) {\n     \
        \   for (int j = 1; j <= n; j++) {\n            int current_product = nums1[i-1]\
        \ * nums2[j-1];\n\n            int val_if_included = current_product + max(0,\
        \ dp[i-1][j-1]);\n\n            int val_if_skip_nums1_i = dp[i-1][j];\n\n  \
        \          int val_if_skip_nums2_j = dp[i][j-1];\n\n            dp[i][j] = max3(val_if_included,\
        \ val_if_skip_nums1_i, val_if_skip_nums2_j);\n        }\n    }\n\n    int result\
        \ = dp[m][n];\n\n    // Free allocated memory\n    for (int i = 0; i <= m; i++)\
        \ {\n        free(dp[i]);\n    }\n    free(dp);\n\n    return result;\n}"
      csharp: "public class Solution {\n    public int MaxDotProduct(int[] nums1, int[]\
        \ nums2) {\n        int m = nums1.Length;\n        int n = nums2.Length;\n\n\
        \        const int NEG_INF = int.MinValue;\n\n        int[,] dp = new int[m\
        \ + 1, n + 1];\n\n        for (int i = 0; i <= m; i++) {\n            for (int\
        \ j = 0; j <= n; j++) {\n                dp[i, j] = NEG_INF;\n            }\n\
        \        }\n\n        for (int i = 1; i <= m; i++) {\n            for (int j\
        \ = 1; j <= n; j++) {\n                int currentProduct = nums1[i-1] * nums2[j-1];\n\
        \n                int valMatch = currentProduct;\n                if (dp[i-1,\
        \ j-1] != NEG_INF) {\n                    valMatch = Math.Max(valMatch, currentProduct\
        \ + dp[i-1, j-1]);\n                }\n\n                int valExcludeI = dp[i-1,\
        \ j];\n\n                int valExcludeJ = dp[i, j-1];\n\n                dp[i,\
        \ j] = Math.Max(valMatch, Math.Max(valExcludeI, valExcludeJ));\n           \
        \ }\n        }\n\n        return dp[m, n];\n    }\n}"
      javascript: "/**\n * @param {number[]} nums1\n * @param {number[]} nums2\n * @return\
        \ {number}\n */\nvar maxDotProduct = function(nums1, nums2) {\n    const m =\
        \ nums1.length;\n    const n = nums2.length;\n\n    const NEG_INF = Number.MIN_SAFE_INTEGER;\n\
        \n    const dp = Array(m + 1).fill(0).map(() => Array(n + 1).fill(NEG_INF));\n\
        \n    for (let i = 1; i <= m; i++) {\n        for (let j = 1; j <= n; j++) {\n\
        \            const currentProduct = nums1[i-1] * nums2[j-1];\n\n           \
        \ let valMatch = currentProduct;\n            if (dp[i-1][j-1] !== NEG_INF)\
        \ {\n                valMatch = Math.max(valMatch, currentProduct + dp[i-1][j-1]);\n\
        \            }\n\n            const valExcludeI = dp[i-1][j];\n\n          \
        \  const valExcludeJ = dp[i][j-1];\n\n            dp[i][j] = Math.max(valMatch,\
        \ valExcludeI, valExcludeJ);\n        }\n    }\n\n    return dp[m][n];\n};"
      typescript: "function maxDotProduct(nums1: number[], nums2: number[]): number\
        \ {\n    const m = nums1.length;\n    const n = nums2.length;\n\n    const NEG_INF\
        \ = Number.MIN_SAFE_INTEGER;\n\n    const dp: number[][] = Array(m + 1).fill(0).map(()\
        \ => Array(n + 1).fill(NEG_INF));\n\n    for (let i = 1; i <= m; i++) {\n  \
        \      for (let j = 1; j <= n; j++) {\n            const currentProduct = nums1[i-1]\
        \ * nums2[j-1];\n\n            let valMatch = currentProduct;\n            if\
        \ (dp[i-1][j-1] !== NEG_INF) {\n                valMatch = Math.max(valMatch,\
        \ currentProduct + dp[i-1][j-1]);\n            }\n\n            const valExcludeI\
        \ = dp[i-1][j];\n\n            const valExcludeJ = dp[i][j-1];\n\n         \
        \   dp[i][j] = Math.max(valMatch, valExcludeI, valExcludeJ);\n        }\n  \
        \  }\n\n    return dp[m][n];\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums1\n     * @param\
        \ Integer[] $nums2\n     * @return Integer\n     */\n    function maxDotProduct($nums1,\
        \ $nums2) {\n        $m = count($nums1);\n        $n = count($nums2);\n\n  \
        \      $NEG_INF = PHP_INT_MIN;\n\n        $dp = array_fill(0, $m + 1, array_fill(0,\
        \ $n + 1, $NEG_INF));\n\n        for ($i = 1; $i <= $m; $i++) {\n          \
        \  for ($j = 1; $j <= $n; $j++) {\n                $currentProduct = $nums1[$i-1]\
        \ * $nums2[$j-1];\n\n                $valMatch = $currentProduct;\n        \
        \        if ($dp[$i-1][$j-1] !== $NEG_INF) {\n                    $valMatch\
        \ = max($valMatch, $currentProduct + $dp[$i-1][$j-1]);\n                }\n\n\
        \                $valExcludeI = $dp[$i-1][$j];\n\n                $valExcludeJ\
        \ = $dp[$i][$j-1];\n\n                $dp[$i][$j] = max($valMatch, $valExcludeI,\
        \ $valExcludeJ);\n            }\n        }\n\n        return $dp[$m][$n];\n\
        \    }\n}"
      swift: "class Solution {\n    func maxDotProduct(_ nums1: [Int], _ nums2: [Int])\
        \ -> Int {\n        let m = nums1.count\n        let n = nums2.count\n\n   \
        \     let NEG_INF = Int.min\n\n        var dp = Array(repeating: Array(repeating:\
        \ NEG_INF, count: n + 1), count: m + 1)\n\n        for i in 1...m {\n      \
        \      for j in 1...n {\n                let currentProduct = nums1[i-1] * nums2[j-1]\n\
        \n                var valMatch = currentProduct\n                if dp[i-1][j-1]\
        \ != NEG_INF {\n                    valMatch = max(valMatch, currentProduct\
        \ + dp[i-1][j-1])\n                }\n\n                let valExcludeI = dp[i-1][j]\n\
        \n                let valExcludeJ = dp[i][j-1]\n\n                dp[i][j] =\
        \ max(valMatch, valExcludeI, valExcludeJ)\n            }\n        }\n\n    \
        \    return dp[m][n]\n    }\n}"
      kotlin: "class Solution {\n    fun maxDotProduct(nums1: IntArray, nums2: IntArray):\
        \ Int {\n        val n = nums1.size\n        val m = nums2.size\n\n        val\
        \ dp = Array(n + 1) { IntArray(m + 1) { Int.MIN_VALUE } }\n\n        for (i\
        \ in 1..n) {\n            for (j in 1..m) {\n                val currentProduct\
        \ = nums1[i - 1] * nums2[j - 1]\n\n                val includeBoth: Int\n  \
        \              if (dp[i - 1][j - 1] == Int.MIN_VALUE) {\n                  \
        \  includeBoth = currentProduct\n                } else {\n                \
        \    includeBoth = Math.max(currentProduct, currentProduct + dp[i - 1][j - 1])\n\
        \                }\n\n                val excludeNum1 = dp[i - 1][j]\n     \
        \           val excludeNum2 = dp[i][j - 1]\n\n                dp[i][j] = Math.max(Math.max(includeBoth,\
        \ excludeNum1), excludeNum2)\n            }\n        }\n\n        return dp[n][m]\n\
        \    }\n}"
      dart: "import 'dart:math' as math;\n\nclass Solution {\n  int maxDotProduct(List<int>\
        \ nums1, List<int> nums2) {\n    final n = nums1.length;\n    final m = nums2.length;\n\
        \n    // A sufficiently small negative number to represent negative infinity\n\
        \    // Max possible dot product is 500 * 1000 * 1000 = 5 * 10^8\n    // Min\
        \ possible dot product is 500 * -1000 * 1000 = -5 * 10^8\n    // So -10^9 is\
        \ a safe \"negative infinity\" for int.\n    const int negInf = -1000000000;\n\
        \n    final dp = List.generate(n + 1, (_) => List.filled(m + 1, negInf));\n\n\
        \    for (int i = 1; i <= n; i++) {\n      for (int j = 1; j <= m; j++) {\n\
        \        final currentProduct = nums1[i - 1] * nums2[j - 1];\n\n        int\
        \ includeBoth;\n        if (dp[i - 1][j - 1] == negInf) {\n          includeBoth\
        \ = currentProduct;\n        } else {\n          includeBoth = math.max(currentProduct,\
        \ currentProduct + dp[i - 1][j - 1]);\n        }\n\n        final excludeNum1\
        \ = dp[i - 1][j];\n        final excludeNum2 = dp[i][j - 1];\n\n        dp[i][j]\
        \ = math.max(math.max(includeBoth, excludeNum1), excludeNum2);\n      }\n  \
        \  }\n\n    return dp[n][m];\n  }\n}"
      go: "package main\n\nimport \"math\"\n\nfunc maxDotProduct(nums1 []int, nums2\
        \ []int) int {\n    n := len(nums1)\n    m := len(nums2)\n\n    dp := make([][]int,\
        \ n+1)\n    for i := range dp {\n        dp[i] = make([]int, m+1)\n        for\
        \ j := range dp[i] {\n            dp[i][j] = math.MinInt32 // Initialize with\
        \ a very small number\n        }\n    }\n\n    for i := 1; i <= n; i++ {\n \
        \       for j := 1; j <= m; j++ {\n            currentProduct := nums1[i-1]\
        \ * nums2[j-1]\n\n            includeBoth := 0\n            if dp[i-1][j-1]\
        \ == math.MinInt32 {\n                includeBoth = currentProduct\n       \
        \     } else {\n                includeBoth = math.Max(currentProduct, currentProduct\
        \ + dp[i-1][j-1])\n            }\n\n            excludeNum1 := dp[i-1][j]\n\
        \            excludeNum2 := dp[i][j-1]\n\n            dp[i][j] = math.Max(math.Max(includeBoth,\
        \ excludeNum1), excludeNum2)\n        }\n    }\n\n    return dp[n][m]\n}"
      ruby: "# @param {Integer[]} nums1\n# @param {Integer[]} nums2\n# @return {Integer}\n\
        def max_dot_product(nums1, nums2)\n    n = nums1.length\n    m = nums2.length\n\
        \n    # Use a sufficiently small negative integer for \"negative infinity\"\n\
        \    # Max possible dot product is 500 * 1000 * 1000 = 5 * 10^8\n    # Min possible\
        \ dot product is 500 * -1000 * 1000 = -5 * 10^8\n    # So -10^9 is a safe \"\
        negative infinity\" for int.\n    neg_inf = -1_000_000_000 \n\n    dp = Array.new(n\
        \ + 1) { Array.new(m + 1, neg_inf) }\n\n    (1..n).each do |i|\n        (1..m).each\
        \ do |j|\n            current_product = nums1[i - 1] * nums2[j - 1]\n\n    \
        \        include_both = 0\n            if dp[i - 1][j - 1] == neg_inf\n    \
        \            include_both = current_product\n            else\n            \
        \    include_both = [current_product, current_product + dp[i - 1][j - 1]].max\n\
        \            end\n\n            exclude_num1 = dp[i - 1][j]\n            exclude_num2\
        \ = dp[i][j - 1]\n\n            dp[i][j] = [include_both, exclude_num1, exclude_num2].max\n\
        \        end\n    end\n\n    dp[n][m]\nend"
      scala: "object Solution {\n    def maxDotProduct(nums1: Array[Int], nums2: Array[Int]):\
        \ Int = {\n        val n = nums1.length\n        val m = nums2.length\n\n  \
        \      val dp = Array.ofDim[Int](n + 1, m + 1)\n        for (i <- 0 to n) {\n\
        \            for (j <- 0 to m) {\n                dp(i)(j) = Int.MinValue\n\
        \            }\n        }\n\n        for (i <- 1 to n) {\n            for (j\
        \ <- 1 to m) {\n                val currentProduct = nums1(i - 1) * nums2(j\
        \ - 1)\n\n                val includeBoth: Int = \n                    if (dp(i\
        \ - 1)(j - 1) == Int.MinValue) {\n                        currentProduct\n \
        \                   } else {\n                        math.max(currentProduct,\
        \ currentProduct + dp(i - 1)(j - 1))\n                    }\n\n            \
        \    val excludeNum1 = dp(i - 1)(j)\n                val excludeNum2 = dp(i)(j\
        \ - 1)\n\n                dp(i)(j) = math.max(math.max(includeBoth, excludeNum1),\
        \ excludeNum2)\n            }\n        }\n\n        dp(n)(m)\n    }\n}"
      rust: "impl Solution {\n    pub fn max_dot_product(nums1: Vec<i32>, nums2: Vec<i32>)\
        \ -> i32 {\n        let n = nums1.len();\n        let m = nums2.len();\n\n \
        \       let min_val = i32::MIN;\n\n        let mut prev_dp = vec![min_val; m\
        \ + 1];\n        let mut curr_dp = vec![min_val; m + 1];\n\n        for i in\
        \ 1..=n {\n            for j in 1..=m {\n                let current_product\
        \ = nums1[i - 1] * nums2[j - 1];\n\n                let mut val_from_diag_option\
        \ = current_product;\n\n                if prev_dp[j - 1] != min_val {\n   \
        \                 val_from_diag_option = val_from_diag_option.max(prev_dp[j\
        \ - 1] + current_product);\n                }\n\n                curr_dp[j]\
        \ = prev_dp[j]\n                    .max(curr_dp[j - 1])\n                 \
        \   .max(val_from_diag_option);\n            }\n            prev_dp.copy_from_slice(&curr_dp);\n\
        \        }\n\n        prev_dp[m]\n    }\n}"
      racket: "(define/contract (max-dot-product nums1 nums2)\n  (-> (listof exact-integer?)\
        \ (listof exact-integer?) exact-integer?)\n  (let* ([n (length nums1)]\n   \
        \      [m (length nums2)]\n         [min-val -1000000000]) ; A sufficiently\
        \ small number\n\n    (define (dp-row i prev-dp)\n      (if (> i n)\n      \
        \    (list-ref prev-dp m)\n          (let ([curr-dp (make-list (+ m 1) min-val)])\n\
        \            (for ([j (in-range 1 (+ m 1))])\n              (let* ([num1-val\
        \ (list-ref nums1 (- i 1))]\n                     [num2-val (list-ref nums2\
        \ (- j 1))]\n                     [current-product (* num1-val num2-val)]\n\
        \                     [val-from-diag-option current-product])\n            \
        \    (when (not (= (list-ref prev-dp (- j 1)) min-val))\n                  (set!\
        \ val-from-diag-option (max val-from-diag-option (+ (list-ref prev-dp (- j 1))\
        \ current-product))))\n                (list-set! curr-dp j\n              \
        \             (max (list-ref prev-dp j)\n                                (list-ref\
        \ curr-dp (- j 1))\n                                val-from-diag-option))))\n\
        \            (dp-row (+ i 1) curr-dp))))\n\n    (dp-row 1 (make-list (+ m 1)\
        \ min-val))))"
      erlang: "-spec max_dot_product(Nums1 :: [integer()], Nums2 :: [integer()]) ->\
        \ integer().\nmax_dot_product(Nums1, Nums2) ->\n    N = length(Nums1),\n   \
        \ M = length(Nums2),\n    MinVal = -1000000000, % A sufficiently small number\n\
        \n    % Convert lists to arrays for O(1) access\n    Nums1Arr = array:from_list(Nums1),\n\
        \    Nums2Arr = array:from_list(Nums2),\n\n    % Initialize prev_dp with MinVal\n\
        \    PrevDpArr = array:from_list(lists:duplicate(M + 1, MinVal)),\n\n    % Outer\
        \ loop for i from 0 to N-1 (array indices)\n    FinalPrevDpArr = lists:foldl(fun(I,\
        \ AccPrevDpArr) ->\n        % Initialize CurrDpArr for this row\n        CurrDpArr\
        \ = array:from_list(lists:duplicate(M + 1, MinVal)),\n\n        % Inner loop\
        \ for j from 0 to M-1 (array indices)\n        UpdatedCurrDpArr = lists:foldl(fun(J,\
        \ AccCurrDpArrInner) ->\n            Num1Val = array:get(I, Nums1Arr),\n   \
        \         Num2Val = array:get(J, Nums2Arr),\n            CurrentProduct = Num1Val\
        \ * Num2Val,\n\n            % prev_dp[j-1] is AccPrevDpArr[J]\n            ValFromDiagOption\
        \ =\n                case array:get(J, AccPrevDpArr) of\n                  \
        \  MinVal -> CurrentProduct;\n                    PrevDiagVal -> max(CurrentProduct,\
        \ PrevDiagVal + CurrentProduct)\n                end,\n\n            % prev_dp[j]\
        \ is AccPrevDpArr[J+1]\n            PrevDpJ = array:get(J + 1, AccPrevDpArr),\n\
        \            % curr_dp[j-1] is AccCurrDpArrInner[J]\n            CurrDpJMinus1\
        \ = array:get(J, AccCurrDpArrInner),\n\n            MaxVal = max(PrevDpJ, max(CurrDpJMinus1,\
        \ ValFromDiagOption)),\n\n            % Update AccCurrDpArrInner at index J+1\n\
        \            array:set(J + 1, MaxVal, AccCurrDpArrInner)\n        end, CurrDpArr,\
        \ lists:seq(0, M - 1)),\n\n        UpdatedCurrDpArr % Return CurrDpArr as the\
        \ new AccPrevDpArr for the next iteration\n    end, PrevDpArr, lists:seq(0,\
        \ N - 1)),\n\n    array:get(M, FinalPrevDpArr)."
      elixir: "defmodule Solution do\n  @spec max_dot_product(nums1 :: [integer], nums2\
        \ :: [integer]) :: integer\n  def max_dot_product(nums1, nums2) do\n    n =\
        \ length(nums1)\n    m = length(nums2)\n    min_val = -1_000_000_000 # A sufficiently\
        \ small number\n\n    # Convert lists to tuples for O(1) access\n    nums1_tuple\
        \ = List.to_tuple(nums1)\n    nums2_tuple = List.to_tuple(nums2)\n\n    # Initialize\
        \ prev_dp as a tuple with min_val\n    prev_dp_tuple = List.to_tuple(List.duplicate(min_val,\
        \ m + 1))\n\n    # Outer loop for i from 0 to n-1 (tuple indices)\n    final_prev_dp_tuple\
        \ = Enum.reduce(0..(n - 1), prev_dp_tuple, fn i, acc_prev_dp_tuple ->\n    \
        \  # Initialize curr_dp_tuple for this row\n      curr_dp_tuple = List.to_tuple(List.duplicate(min_val,\
        \ m + 1))\n\n      # Inner loop for j from 0 to m-1 (tuple indices)\n      Enum.reduce(0..(m\
        \ - 1), curr_dp_tuple, fn j, acc_curr_dp_tuple_inner ->\n        num1_val =\
        \ elem(nums1_tuple, i)\n        num2_val = elem(nums2_tuple, j)\n        current_product\
        \ = num1_val * num2_val\n\n        # prev_dp[j-1] is acc_prev_dp_tuple[j]\n\
        \        val_from_diag_option =\n          case elem(acc_prev_dp_tuple, j) do\n\
        \            ^min_val -> current_product\n            prev_diag_val -> max(current_product,\
        \ prev_diag_val + current_product)\n          end\n\n        # prev_dp[j] is\
        \ acc_prev_dp_tuple[j+1]\n        prev_dp_j = elem(acc_prev_dp_tuple, j + 1)\n\
        \        # curr_dp[j-1] is acc_curr_dp_tuple_inner[j]\n        curr_dp_j_minus_1\
        \ = elem(acc_curr_dp_tuple_inner, j)\n\n        max_val = max(prev_dp_j, max(curr_dp_j_minus_1,\
        \ val_from_diag_option))\n\n        # Update acc_curr_dp_tuple_inner at index\
        \ j+1\n        put_elem(acc_curr_dp_tuple_inner, j + 1, max_val)\n      end)\n\
        \    end)\n    |> elem(m) # Get the final result from the last row, last column\
        \ (index m)\n  end\n}"
    approach: 'The problem asks for the maximum dot product of two non-empty subsequences
      of equal length from two given arrays, nums1 and nums2. This can be solved using
      dynamic programming. We define `dp[i][j]` as the maximum dot product of two non-empty
      subsequences, one formed from the prefix `nums1[0...i-1]` and the other from `nums2[0...j-1]`.
      The DP table is initialized with a sufficiently small negative number (representing
      negative infinity) to signify that no valid subsequence has been formed yet.


      For each cell `dp[i][j]`, we consider three possibilities: 1. Match `nums1[i-1]`
      and `nums2[j-1]`: The product `nums1[i-1] * nums2[j-1]` is included. This can
      either start a new subsequence (just the product itself) or extend a previously
      found subsequence (product + `dp[i-1][j-1]`). We take the maximum of these two
      options, but only extend if `dp[i-1][j-1]` is not negative infinity (i.e., a valid
      subsequence exists). 2. Exclude `nums1[i-1]`: The maximum dot product is `dp[i-1][j]`.
      3. Exclude `nums2[j-1]`: The maximum dot product is `dp[i][j-1]`. `dp[i][j]` is
      then the maximum of these three possibilities. The final answer is `dp[m][n]`,
      where `m` and `n` are the lengths of `nums1` and `nums2` respectively.'
    time_complexity: The time complexity is O(M*N), where M is the length of nums1 and
      N is the length of nums2. This is because we iterate through each cell of the
      M x N DP table once, and each cell's computation involves a constant number of
      comparisons and arithmetic operations.
    space_complexity: The space complexity is O(M*N) for storing the 2D DP table. Each
      cell `dp[i][j]` stores an integer value. Given the constraints (M, N <= 500),
      an M x N table of integers is feasible.
    elapsed_time: 214.44763660430908
    model: gemini-2.5-flash
    generated_at: '2026-01-08 01:13:02 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxDotProduct(vector<int>& nums1, vector<int>&\
        \ nums2) {\n        int n = nums1.size(), m = nums2.size();\n        vector<vector<int>>\
        \ dp(n + 1, vector<int>(m + 1, INT_MIN));\n        for (int i = 1; i <= n; i++)\
        \ {\n            for (int j = 1; j <= m; j++) {\n                dp[i][j] =\
        \ max(dp[i][j], dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1]);\n         \
        \       dp[i][j] = max(dp[i][j], dp[i - 1][j]);\n                dp[i][j] =\
        \ max(dp[i][j], dp[i][j - 1]);\n                dp[i][j] = max(dp[i][j], nums1[i\
        \ - 1] * nums2[j - 1]);\n            }\n        }\n        return dp[n][m];\n\
        \    }\n};"
      java: "class Solution {\n    public int maxDotProduct(int[] nums1, int[] nums2)\
        \ {\n        int n = nums1.length, m = nums2.length;\n        int[][] dp = new\
        \ int[n + 1][m + 1];\n        for (int i = 0; i <= n; i++) {\n            for\
        \ (int j = 0; j <= m; j++) {\n                if (i == 0 || j == 0) continue;\n\
        \                dp[i][j] = Math.max(dp[i][j], dp[i - 1][j - 1] + nums1[i -\
        \ 1] * nums2[j - 1]);\n                dp[i][j] = Math.max(dp[i][j], dp[i -\
        \ 1][j]);\n                dp[i][j] = Math.max(dp[i][j], dp[i][j - 1]);\n  \
        \              dp[i][j] = Math.max(dp[i][j], nums1[i - 1] * nums2[j - 1]);\n\
        \            }\n        }\n        return dp[n][m];\n    }\n}"
      python: "class Solution(object):\n    def maxDotProduct(self, nums1, nums2):\n\
        \        n, m = len(nums1), len(nums2)\n        dp = [[float('-inf')] * (m +\
        \ 1) for _ in range(n + 1)]\n        for i in range(1, n + 1):\n           \
        \ for j in range(1, m + 1):\n                dp[i][j] = max(dp[i][j], dp[i -\
        \ 1][j - 1] + nums1[i - 1] * nums2[j - 1])\n                dp[i][j] = max(dp[i][j],\
        \ dp[i - 1][j])\n                dp[i][j] = max(dp[i][j], dp[i][j - 1])\n  \
        \              dp[i][j] = max(dp[i][j], nums1[i - 1] * nums2[j - 1])\n     \
        \   return dp[n][m]"
      python3: "class Solution:\n    def maxDotProduct(self, nums1: list[int], nums2:\
        \ list[int]) -> int:\n        n, m = len(nums1), len(nums2)\n        dp = [[float('-inf')]\
        \ * (m + 1) for _ in range(n + 1)]\n        for i in range(1, n + 1):\n    \
        \        for j in range(1, m + 1):\n                dp[i][j] = max(dp[i][j],\
        \ dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1])\n                dp[i][j]\
        \ = max(dp[i][j], dp[i - 1][j])\n                dp[i][j] = max(dp[i][j], dp[i][j\
        \ - 1])\n                dp[i][j] = max(dp[i][j], nums1[i - 1] * nums2[j - 1])\n\
        \        return dp[n][m]"
      c: "int maxDotProduct(int* nums1, int nums1Size, int* nums2, int nums2Size) {\n\
        \    int n = nums1Size, m = nums2Size;\n    int** dp = (int**)malloc((n + 1)\
        \ * sizeof(int*));\n    for (int i = 0; i <= n; i++) {\n        dp[i] = (int*)malloc((m\
        \ + 1) * sizeof(int));\n        for (int j = 0; j <= m; j++) {\n           \
        \ dp[i][j] = INT_MIN;\n        }\n    }\n    for (int i = 1; i <= n; i++) {\n\
        \        for (int j = 1; j <= m; j++) {\n            dp[i][j] = max(dp[i][j],\
        \ dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1]);\n            dp[i][j] = max(dp[i][j],\
        \ dp[i - 1][j]);\n            dp[i][j] = max(dp[i][j], dp[i][j - 1]);\n    \
        \        dp[i][j] = max(dp[i][j], nums1[i - 1] * nums2[j - 1]);\n        }\n\
        \    }\n    int result = dp[n][m];\n    for (int i = 0; i <= n; i++) {\n   \
        \     free(dp[i]);\n    }\n    free(dp);\n    return result;\n}"
      csharp: "public class Solution {\n    public int MaxDotProduct(int[] nums1, int[]\
        \ nums2) {\n        int m = nums1.Length;\n        int n = nums2.Length;\n \
        \       int[,] dp = new int[m + 1, n + 1];\n        for (int i = 1; i <= m;\
        \ i++) {\n            for (int j = 1; j <= n; j++) {\n                dp[i,\
        \ j] = Math.Max(dp[i - 1, j - 1] + nums1[i - 1] * nums2[j - 1], Math.Max(dp[i\
        \ - 1, j], dp[i, j - 1]));\n            }\n        }\n        return Math.Max(dp[m,\
        \ n], 0);\n    }\n}"
      javascript: "var maxDotProduct = function(nums1, nums2) {\n    let m = nums1.length;\n\
        \    let n = nums2.length;\n    let dp = Array(m + 1).fill(0).map(() => Array(n\
        \ + 1).fill(0));\n    for (let i = 1; i <= m; i++) {\n        for (let j = 1;\
        \ j <= n; j++) {\n            dp[i][j] = Math.max(dp[i - 1][j - 1] + nums1[i\
        \ - 1] * nums2[j - 1], Math.max(dp[i - 1][j], dp[i][j - 1]));\n        }\n \
        \   }\n    return Math.max(dp[m][n], 0);\n};"
      typescript: "function maxDotProduct(nums1: number[], nums2: number[]): number\
        \ {\n    let m: number = nums1.length;\n    let n: number = nums2.length;\n\
        \    let dp: number[][] = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));\n\
        \    for (let i: number = 1; i <= m; i++) {\n        for (let j: number = 1;\
        \ j <= n; j++) {\n            dp[i][j] = Math.max(dp[i - 1][j - 1] + nums1[i\
        \ - 1] * nums2[j - 1], Math.max(dp[i - 1][j], dp[i][j - 1]));\n        }\n \
        \   }\n    return Math.max(dp[m][n], 0);\n}"
      php: "class Solution {\n    function maxDotProduct($nums1, $nums2) {\n       \
        \ $m = count($nums1);\n        $n = count($nums2);\n        $dp = array_fill(0,\
        \ $m + 1, array_fill(0, $n + 1, 0));\n        for ($i = 1; $i <= $m; $i++) {\n\
        \            for ($j = 1; $j <= $n; $j++) {\n                $dp[$i][$j] = max($dp[$i\
        \ - 1][$j - 1] + $nums1[$i - 1] * $nums2[$j - 1], max($dp[$i - 1][$j], $dp[$i][$j\
        \ - 1]));\n            }\n        }\n        return max($dp[$m][$n], 0);\n \
        \   }\n}"
      swift: "class Solution {\n    func maxDotProduct(_ nums1: [Int], _ nums2: [Int])\
        \ -> Int {\n        let m = nums1.count\n        let n = nums2.count\n     \
        \   var dp = Array(repeating: Array(repeating: 0, count: n + 1), count: m +\
        \ 1)\n        for i in 1...m {\n            for j in 1...n {\n             \
        \   dp[i][j] = max(dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1], max(dp[i\
        \ - 1][j], dp[i][j - 1]))\n            }\n        }\n        return max(dp[m][n],\
        \ 0)\n    }\n}"
      kotlin: "class Solution {\n    fun maxDotProduct(nums1: IntArray, nums2: IntArray):\
        \ Int {\n        val m = nums1.size\n        val n = nums2.size\n        val\
        \ dp = Array(m + 1) { IntArray(n + 1) { Int.MIN_VALUE } }\n        for (i in\
        \ 1..m) {\n            for (j in 1..n) {\n                dp[i][j] = maxOf(dp[i][j],\
        \ dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1], nums1[i - 1] * nums2[j - 1])\n\
        \                if (i > 1) dp[i][j] = maxOf(dp[i][j], dp[i - 1][j])\n     \
        \           if (j > 1) dp[i][j] = maxOf(dp[i][j], dp[i][j - 1])\n          \
        \  }\n        }\n        return dp.maxOf { it.max() }\n    }\n}"
      dart: "class Solution {\n  int maxDotProduct(List<int> nums1, List<int> nums2)\
        \ {\n    int m = nums1.length;\n    int n = nums2.length;\n    List<List<int>>\
        \ dp = List.generate(m + 1, (i) => List.generate(n + 1, (j) => int.MinValue));\n\
        \    for (int i = 1; i <= m; i++) {\n      for (int j = 1; j <= n; j++) {\n\
        \        dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + nums1[i - 1] * nums2[j\
        \ - 1], nums1[i - 1] * nums2[j - 1]);\n        if (i > 1) dp[i][j] = max(dp[i][j],\
        \ dp[i - 1][j]);\n        if (j > 1) dp[i][j] = max(dp[i][j], dp[i][j - 1]);\n\
        \      }\n    }\n    int max = int.MinValue;\n    for (int i = 1; i <= m; i++)\
        \ {\n      for (int j = 1; j <= n; j++) {\n        max = max(max, dp[i][j]);\n\
        \      }\n    }\n    return max;\n  }\n  int max(int a, int b, int c) {\n  \
        \  return max(max(a, b), c);\n  }\n}"
      go: "func maxDotProduct(nums1 []int, nums2 []int) int {\n    m, n := len(nums1),\
        \ len(nums2)\n    dp := make([][]int, m + 1)\n    for i := range dp {\n    \
        \    dp[i] = make([]int, n + 1)\n        for j := range dp[i] {\n          \
        \  dp[i][j] = -1e9\n        }\n    }\n    for i := 1; i <= m; i++ {\n      \
        \  for j := 1; j <= n; j++ {\n            dp[i][j] = max(dp[i][j], dp[i - 1][j\
        \ - 1] + nums1[i - 1] * nums2[j - 1], nums1[i - 1] * nums2[j - 1])\n       \
        \     if i > 1 {\n                dp[i][j] = max(dp[i][j], dp[i - 1][j])\n \
        \           }\n            if j > 1 {\n                dp[i][j] = max(dp[i][j],\
        \ dp[i][j - 1])\n            }\n        }\n    }\n    maxVal := -1e9\n    for\
        \ i := 1; i <= m; i++ {\n        for j := 1; j <= n; j++ {\n            maxVal\
        \ = max(maxVal, dp[i][j])\n        }\n    }\n    return maxVal\n}\n\nfunc max(a,\
        \ b, c int) int {\n    if a > b {\n        if a > c {\n            return a\n\
        \        }\n        return c\n    }\n    if b > c {\n        return b\n    }\n\
        \    return c\n}"
      ruby: "def max_dot_product(nums1, nums2)\n    m, n = nums1.size, nums2.size\n\
        \    dp = Array.new(m + 1) { Array.new(n + 1, -1e9) }\n    for i in 1..m\n \
        \       for j in 1..n\n            dp[i][j] = [dp[i][j], dp[i - 1][j - 1] +\
        \ nums1[i - 1] * nums2[j - 1], nums1[i - 1] * nums2[j - 1]].max\n          \
        \  if i > 1\n                dp[i][j] = [dp[i][j], dp[i - 1][j]].max\n     \
        \       end\n            if j > 1\n                dp[i][j] = [dp[i][j], dp[i][j\
        \ - 1]].max\n            end\n        end\n    end\n    max_val = -1e9\n   \
        \ for i in 1..m\n        for j in 1..n\n            max_val = [max_val, dp[i][j]].max\n\
        \        end\n    end\n    max_val\nend"
      scala: "object Solution {\n    def maxDotProduct(nums1: Array[Int], nums2: Array[Int]):\
        \ Int = {\n        val m = nums1.length\n        val n = nums2.length\n    \
        \    val dp = Array.ofDim[Int](m + 1, n + 1)\n        for (i <- 1 to m) {\n\
        \            for (j <- 1 to n) {\n                dp(i)(j) = math.max(math.max(dp(i)(j),\
        \ dp(i - 1)(j - 1) + nums1(i - 1) * nums2(j - 1)), nums1(i - 1) * nums2(j -\
        \ 1))\n                if (i > 1) dp(i)(j) = math.max(dp(i)(j), dp(i - 1)(j))\n\
        \                if (j > 1) dp(i)(j) = math.max(dp(i)(j), dp(i)(j - 1))\n  \
        \          }\n        }\n        var maxVal = Int.MinValue\n        for (i <-\
        \ 1 to m) {\n            for (j <- 1 to n) {\n                maxVal = math.max(maxVal,\
        \ dp(i)(j))\n            }\n        }\n        maxVal\n    }\n}"
      rust: "impl Solution {\n    pub fn max_dot_product(nums1: Vec<i32>, nums2: Vec<i32>)\
        \ -> i32 {\n        let n = nums1.len();\n        let m = nums2.len();\n   \
        \     let mut dp = vec![vec![i32::MIN; m + 1]; n + 1];\n        for i in 1..=n\
        \ {\n            for j in 1..=m {\n                dp[i][j] = dp[i][j - 1].max(dp[i\
        \ - 1][j]).max(dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1]);\n          \
        \  }\n        }\n        let mut ans = i32::MIN;\n        for i in 1..=n {\n\
        \            for j in 1..=m {\n                if i == j {\n               \
        \     ans = ans.max(dp[i][j]);\n                }\n            }\n        }\n\
        \        ans\n    }\n}"
      racket: "(define/contract (max-dot-product nums1 nums2)\n  (-> (listof exact-integer?)\
        \ (listof exact-integer?) exact-integer?)\n  (let* (\n           [n (length\
        \ nums1)]\n           [m (length nums2)]\n           [dp (make-list (add1 n)\
        \ (lambda (x) (make-list (add1 m) -1000000000)))])\n    (for (\n         [i\
        \ (range 1 (add1 n))])\n      (for (\n           [j (range 1 (add1 m))])\n \
        \       (set! (list-ref (list-ref dp i) j)\n              (max (list-ref (list-ref\
        \ dp i) (sub1 j))\n                   (list-ref (list-ref dp (sub1 i)) j)\n\
        \                   (+ (list-ref (list-ref dp (sub1 i)) (sub1 j))\n        \
        \              (* (list-ref nums1 (sub1 i))\n                         (list-ref\
        \ nums2 (sub1 j))))))))\n    (let (\n          [ans -1000000000])\n      (for\
        \ (\n           [i (range 1 (add1 n))])\n        (for (\n             [j (range\
        \ 1 (add1 m))])\n          (when (= i j)\n            (set! ans (max ans (list-ref\
        \ (list-ref dp i) j))))))\n      ans)))"
      erlang: "max_dot_product(Nums1, Nums2) ->\n  N = length(Nums1),\n  M = length(Nums2),\n\
        \  DP = lists:duplicate(N + 1, lists:duplicate(M + 1, -1000000000)),\n  F =\
        \ fun(I, J) ->\n           case I > N orelse J > M of\n             true ->\
        \ ok;\n             false ->\n               NewDP =\n                 case\
        \ I > 1 orelse J > 1 of\n                   true ->\n                     max(lists:nth(J,\
        \ lists:nth(I, DP)),\n                         max(lists:nth(J, lists:nth(I\
        \ - 1, DP)),\n                            max(lists:nth(J - 1, lists:nth(I,\
        \ DP)),\n                               lists:nth(J - 1, lists:nth(I - 1, DP))\
        \ + lists:nth(I - 1, Nums1) * lists:nth(J - 1, Nums2))));\n                \
        \   false -> 0\n                 end,\n               lists:sublist(lists:nth(I,\
        \ DP), 1, J - 1) ++ [NewDP] ++ lists:sublist(lists:nth(I, DP), J + 1, length(lists:nth(I,\
        \ DP))),\n               F(I + 1, J),\n               F(I, J + 1)\n        \
        \   end\n         end,\n  F(1, 1),\n  Ans = -1000000000,\n  F2 = fun(I, J) ->\n\
        \           case I > N orelse J > M of\n             true -> Ans;\n        \
        \     false ->\n               case I == J of\n                 true ->\n  \
        \                 F2(I + 1, J + 1);\n                 false ->\n           \
        \        F2(I + 1, J)\n               end\n           end\n         end,\n \
        \ F2(1, 1)."
      elixir: "defmodule Solution do\n  @spec max_dot_product(nums1 :: [integer], nums2\
        \ :: [integer]) :: integer\n  def max_dot_product(nums1, nums2) do\n    n =\
        \ length(nums1)\n    m = length(nums2)\n    dp = for _ <- 1..n+1, do: for _\
        \ <- 1..m+1, do: -1000000000\n    dp = Enum.reduce(1..n, dp, fn i, dp ->\n \
        \     Enum.reduce(1..m, dp, fn j, dp ->\n        new_dp =\n          if i >\
        \ 1 or j > 1 do\n            max(Enum.at(Enum.at(dp, i), j - 1),\n         \
        \        max(Enum.at(Enum.at(dp, i - 1), j),\n                    max(Enum.at(Enum.at(dp,\
        \ i), j - 1),\n                       Enum.at(Enum.at(dp, i - 1), j - 1) + Enum.at(nums1,\
        \ i - 1) * Enum.at(nums2, j - 1))))\n          else\n            0\n       \
        \   end,\n        List.update_at(dp, i, fn x -> List.update_at(x, j, fn _ ->\
        \ new_dp end) end)\n      end)\n    end)\n    ans = -1000000000\n    Enum.reduce(1..n,\
        \ ans, fn i, ans ->\n      Enum.reduce(1..m, ans, fn j, ans ->\n        if i\
        \ == j do\n          max(ans, Enum.at(Enum.at(dp, i), j))\n        else\n  \
        \        ans\n        end\n      end)\n    end)\n  end\nend"
    approach: 'The problem can be solved using dynamic programming. We define DP[i][j]
      as the maximum dot product of two subsequences starting in the position i of nums1
      and position j of nums2. We can then fill up the DP table by considering two cases:
      either we include the current elements in the dot product or we don''t. If we
      include them, the dot product is the sum of the current elements plus the maximum
      dot product of the remaining subsequences. If we don''t include them, the maximum
      dot product is the maximum of the dot products of the subsequences starting at
      the next positions. The key intuition here is that we need to consider all possible
      subsequences and find the one that gives the maximum dot product.


      The algorithm works by iterating over all possible pairs of subsequences and calculating
      the maximum dot product for each pair. We use the DP table to store the maximum
      dot products for each pair of subsequences, which allows us to avoid recalculating
      the same dot products multiple times. This approach ensures that we consider all
      possible subsequences and find the one that gives the maximum dot product. The
      time complexity of this approach is O(n*m*min(n, m)), where n and m are the lengths
      of the input arrays, and the space complexity is O(n*m), where n and m are the
      lengths of the input arrays.'
    time_complexity: The time complexity of this approach is O(n*m*min(n, m)), where
      n and m are the lengths of the input arrays. This is because we need to iterate
      over all possible pairs of subsequences, and for each pair, we need to calculate
      the maximum dot product. The number of possible pairs of subsequences is proportional
      to the product of the lengths of the input arrays, and the time complexity of
      calculating the maximum dot product for each pair is proportional to the minimum
      of the lengths of the input arrays.
    space_complexity: The space complexity of this approach is O(n*m), where n and m
      are the lengths of the input arrays. This is because we need to store the maximum
      dot products for each pair of subsequences in the DP table, and the size of the
      DP table is proportional to the product of the lengths of the input arrays.
    elapsed_time: 14.174349546432495
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-08 01:13:31 '
---

## Problem #1458: Max Dot Product of Two Subsequences

**Difficulty:** Hard

**Topics:** Array, Dynamic Programming

## Problem Description

<p>Given two arrays <code>nums1</code>&nbsp;and <code><font face="monospace">nums2</font></code><font face="monospace">.</font></p>

<p>Return the maximum dot product&nbsp;between&nbsp;<strong>non-empty</strong> subsequences of nums1 and nums2 with the same length.</p>

<p>A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie,&nbsp;<code>[2,3,5]</code>&nbsp;is a subsequence of&nbsp;<code>[1,2,3,4,5]</code>&nbsp;while <code>[1,5,3]</code>&nbsp;is not).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [2,1,-2,5], nums2 = [3,0,-6]
<strong>Output:</strong> 18
<strong>Explanation:</strong> Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
Their dot product is (2*3 + (-2)*(-6)) = 18.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [3,-2], nums2 = [2,-6,7]
<strong>Output:</strong> 21
<strong>Explanation:</strong> Take subsequence [3] from nums1 and subsequence [7] from nums2.
Their dot product is (3*7) = 21.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [-1,-1], nums2 = [1,1]
<strong>Output:</strong> -1
<strong>Explanation: </strong>Take subsequence [-1] from nums1 and subsequence [1] from nums2.
Their dot product is -1.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 500</code></li>
	<li><code>-1000 &lt;= nums1[i], nums2[i] &lt;= 1000</code></li>
</ul>


## Hints

1. Use dynamic programming, define DP[i][j] as the maximum dot product of two subsequences starting in the position i of nums1 and position j of nums2.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2026-01-08 01:13:02 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks for the maximum dot product of two non-empty subsequences of equal length from two given arrays, nums1 and nums2. This can be solved using dynamic programming. We define `dp[i][j]` as the maximum dot product of two non-empty subsequences, one formed from the prefix `nums1[0...i-1]` and the other from `nums2[0...j-1]`. The DP table is initialized with a sufficiently small negative number (representing negative infinity) to signify that no valid subsequence has been formed yet.

For each cell `dp[i][j]`, we consider three possibilities: 1. Match `nums1[i-1]` and `nums2[j-1]`: The product `nums1[i-1] * nums2[j-1]` is included. This can either start a new subsequence (just the product itself) or extend a previously found subsequence (product + `dp[i-1][j-1]`). We take the maximum of these two options, but only extend if `dp[i-1][j-1]` is not negative infinity (i.e., a valid subsequence exists). 2. Exclude `nums1[i-1]`: The maximum dot product is `dp[i-1][j]`. 3. Exclude `nums2[j-1]`: The maximum dot product is `dp[i][j-1]`. `dp[i][j]` is then the maximum of these three possibilities. The final answer is `dp[m][n]`, where `m` and `n` are the lengths of `nums1` and `nums2` respectively.

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
    int maxDotProduct(std::vector<int>& nums1, std::vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();

        std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, std::numeric_limits<int>::min()));

        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                int current_product = nums1[i-1] * nums2[j-1];

                int val_if_included = current_product + std::max(0, dp[i-1][j-1]);

                int val_if_skip_nums1_i = dp[i-1][j];

                int val_if_skip_nums2_j = dp[i][j-1];

                dp[i][j] = std::max(val_if_included, std::max(val_if_skip_nums1_i, val_if_skip_nums2_j));
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
    public int maxDotProduct(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;

        int[][] dp = new int[m + 1][n + 1];
        for (int i = 0; i <= m; i++) {
            Arrays.fill(dp[i], Integer.MIN_VALUE);
        }

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                int current_product = nums1[i-1] * nums2[j-1];

                int val_if_included = current_product + Math.max(0, dp[i-1][j-1]);

                int val_if_skip_nums1_i = dp[i-1][j];

                int val_if_skip_nums2_j = dp[i][j-1];

                dp[i][j] = Math.max(val_if_included, Math.max(val_if_skip_nums1_i, val_if_skip_nums2_j));
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
import math

class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m, n = len(nums1), len(nums2)

        dp = [[-math.inf] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                current_product = nums1[i-1] * nums2[j-1]

                val_if_included = current_product + max(0, dp[i-1][j-1])

                val_if_skip_nums1_i = dp[i-1][j]

                val_if_skip_nums2_j = dp[i][j-1]

                dp[i][j] = max(val_if_included, val_if_skip_nums1_i, val_if_skip_nums2_j)

        return dp[m][n]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import math

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)

        dp = [[-math.inf] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                current_product = nums1[i-1] * nums2[j-1]

                val_if_included = current_product + max(0, dp[i-1][j-1])

                val_if_skip_nums1_i = dp[i-1][j]

                val_if_skip_nums2_j = dp[i][j-1]

                dp[i][j] = max(val_if_included, val_if_skip_nums1_i, val_if_skip_nums2_j)

        return dp[m][n]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h> // For malloc, free
#include <limits.h> // For INT_MIN

// Helper function for max of two integers
int max(int a, int b) {
    return a > b ? a : b;
}

// Helper function for max of three integers
int max3(int a, int b, int c) {
    return max(a, max(b, c));
}

int maxDotProduct(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int m = nums1Size;
    int n = nums2Size;

    int** dp = (int**)malloc((m + 1) * sizeof(int*));
    for (int i = 0; i <= m; i++) {
        dp[i] = (int*)malloc((n + 1) * sizeof(int));
        for (int j = 0; j <= n; j++) {
            dp[i][j] = INT_MIN;
        }
    }

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            int current_product = nums1[i-1] * nums2[j-1];

            int val_if_included = current_product + max(0, dp[i-1][j-1]);

            int val_if_skip_nums1_i = dp[i-1][j];

            int val_if_skip_nums2_j = dp[i][j-1];

            dp[i][j] = max3(val_if_included, val_if_skip_nums1_i, val_if_skip_nums2_j);
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
public class Solution {
    public int MaxDotProduct(int[] nums1, int[] nums2) {
        int m = nums1.Length;
        int n = nums2.Length;

        const int NEG_INF = int.MinValue;

        int[,] dp = new int[m + 1, n + 1];

        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                dp[i, j] = NEG_INF;
            }
        }

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                int currentProduct = nums1[i-1] * nums2[j-1];

                int valMatch = currentProduct;
                if (dp[i-1, j-1] != NEG_INF) {
                    valMatch = Math.Max(valMatch, currentProduct + dp[i-1, j-1]);
                }

                int valExcludeI = dp[i-1, j];

                int valExcludeJ = dp[i, j-1];

                dp[i, j] = Math.Max(valMatch, Math.Max(valExcludeI, valExcludeJ));
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
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var maxDotProduct = function(nums1, nums2) {
    const m = nums1.length;
    const n = nums2.length;

    const NEG_INF = Number.MIN_SAFE_INTEGER;

    const dp = Array(m + 1).fill(0).map(() => Array(n + 1).fill(NEG_INF));

    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            const currentProduct = nums1[i-1] * nums2[j-1];

            let valMatch = currentProduct;
            if (dp[i-1][j-1] !== NEG_INF) {
                valMatch = Math.max(valMatch, currentProduct + dp[i-1][j-1]);
            }

            const valExcludeI = dp[i-1][j];

            const valExcludeJ = dp[i][j-1];

            dp[i][j] = Math.max(valMatch, valExcludeI, valExcludeJ);
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
function maxDotProduct(nums1: number[], nums2: number[]): number {
    const m = nums1.length;
    const n = nums2.length;

    const NEG_INF = Number.MIN_SAFE_INTEGER;

    const dp: number[][] = Array(m + 1).fill(0).map(() => Array(n + 1).fill(NEG_INF));

    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            const currentProduct = nums1[i-1] * nums2[j-1];

            let valMatch = currentProduct;
            if (dp[i-1][j-1] !== NEG_INF) {
                valMatch = Math.max(valMatch, currentProduct + dp[i-1][j-1]);
            }

            const valExcludeI = dp[i-1][j];

            const valExcludeJ = dp[i][j-1];

            dp[i][j] = Math.max(valMatch, valExcludeI, valExcludeJ);
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

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function maxDotProduct($nums1, $nums2) {
        $m = count($nums1);
        $n = count($nums2);

        $NEG_INF = PHP_INT_MIN;

        $dp = array_fill(0, $m + 1, array_fill(0, $n + 1, $NEG_INF));

        for ($i = 1; $i <= $m; $i++) {
            for ($j = 1; $j <= $n; $j++) {
                $currentProduct = $nums1[$i-1] * $nums2[$j-1];

                $valMatch = $currentProduct;
                if ($dp[$i-1][$j-1] !== $NEG_INF) {
                    $valMatch = max($valMatch, $currentProduct + $dp[$i-1][$j-1]);
                }

                $valExcludeI = $dp[$i-1][$j];

                $valExcludeJ = $dp[$i][$j-1];

                $dp[$i][$j] = max($valMatch, $valExcludeI, $valExcludeJ);
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
    func maxDotProduct(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let m = nums1.count
        let n = nums2.count

        let NEG_INF = Int.min

        var dp = Array(repeating: Array(repeating: NEG_INF, count: n + 1), count: m + 1)

        for i in 1...m {
            for j in 1...n {
                let currentProduct = nums1[i-1] * nums2[j-1]

                var valMatch = currentProduct
                if dp[i-1][j-1] != NEG_INF {
                    valMatch = max(valMatch, currentProduct + dp[i-1][j-1])
                }

                let valExcludeI = dp[i-1][j]

                let valExcludeJ = dp[i][j-1]

                dp[i][j] = max(valMatch, valExcludeI, valExcludeJ)
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
    fun maxDotProduct(nums1: IntArray, nums2: IntArray): Int {
        val n = nums1.size
        val m = nums2.size

        val dp = Array(n + 1) { IntArray(m + 1) { Int.MIN_VALUE } }

        for (i in 1..n) {
            for (j in 1..m) {
                val currentProduct = nums1[i - 1] * nums2[j - 1]

                val includeBoth: Int
                if (dp[i - 1][j - 1] == Int.MIN_VALUE) {
                    includeBoth = currentProduct
                } else {
                    includeBoth = Math.max(currentProduct, currentProduct + dp[i - 1][j - 1])
                }

                val excludeNum1 = dp[i - 1][j]
                val excludeNum2 = dp[i][j - 1]

                dp[i][j] = Math.max(Math.max(includeBoth, excludeNum1), excludeNum2)
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
import 'dart:math' as math;

class Solution {
  int maxDotProduct(List<int> nums1, List<int> nums2) {
    final n = nums1.length;
    final m = nums2.length;

    // A sufficiently small negative number to represent negative infinity
    // Max possible dot product is 500 * 1000 * 1000 = 5 * 10^8
    // Min possible dot product is 500 * -1000 * 1000 = -5 * 10^8
    // So -10^9 is a safe "negative infinity" for int.
    const int negInf = -1000000000;

    final dp = List.generate(n + 1, (_) => List.filled(m + 1, negInf));

    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= m; j++) {
        final currentProduct = nums1[i - 1] * nums2[j - 1];

        int includeBoth;
        if (dp[i - 1][j - 1] == negInf) {
          includeBoth = currentProduct;
        } else {
          includeBoth = math.max(currentProduct, currentProduct + dp[i - 1][j - 1]);
        }

        final excludeNum1 = dp[i - 1][j];
        final excludeNum2 = dp[i][j - 1];

        dp[i][j] = math.max(math.max(includeBoth, excludeNum1), excludeNum2);
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
package main

import "math"

func maxDotProduct(nums1 []int, nums2 []int) int {
    n := len(nums1)
    m := len(nums2)

    dp := make([][]int, n+1)
    for i := range dp {
        dp[i] = make([]int, m+1)
        for j := range dp[i] {
            dp[i][j] = math.MinInt32 // Initialize with a very small number
        }
    }

    for i := 1; i <= n; i++ {
        for j := 1; j <= m; j++ {
            currentProduct := nums1[i-1] * nums2[j-1]

            includeBoth := 0
            if dp[i-1][j-1] == math.MinInt32 {
                includeBoth = currentProduct
            } else {
                includeBoth = math.Max(currentProduct, currentProduct + dp[i-1][j-1])
            }

            excludeNum1 := dp[i-1][j]
            excludeNum2 := dp[i][j-1]

            dp[i][j] = math.Max(math.Max(includeBoth, excludeNum1), excludeNum2)
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
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def max_dot_product(nums1, nums2)
    n = nums1.length
    m = nums2.length

    # Use a sufficiently small negative integer for "negative infinity"
    # Max possible dot product is 500 * 1000 * 1000 = 5 * 10^8
    # Min possible dot product is 500 * -1000 * 1000 = -5 * 10^8
    # So -10^9 is a safe "negative infinity" for int.
    neg_inf = -1_000_000_000 

    dp = Array.new(n + 1) { Array.new(m + 1, neg_inf) }

    (1..n).each do |i|
        (1..m).each do |j|
            current_product = nums1[i - 1] * nums2[j - 1]

            include_both = 0
            if dp[i - 1][j - 1] == neg_inf
                include_both = current_product
            else
                include_both = [current_product, current_product + dp[i - 1][j - 1]].max
            end

            exclude_num1 = dp[i - 1][j]
            exclude_num2 = dp[i][j - 1]

            dp[i][j] = [include_both, exclude_num1, exclude_num2].max
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
    def maxDotProduct(nums1: Array[Int], nums2: Array[Int]): Int = {
        val n = nums1.length
        val m = nums2.length

        val dp = Array.ofDim[Int](n + 1, m + 1)
        for (i <- 0 to n) {
            for (j <- 0 to m) {
                dp(i)(j) = Int.MinValue
            }
        }

        for (i <- 1 to n) {
            for (j <- 1 to m) {
                val currentProduct = nums1(i - 1) * nums2(j - 1)

                val includeBoth: Int = 
                    if (dp(i - 1)(j - 1) == Int.MinValue) {
                        currentProduct
                    } else {
                        math.max(currentProduct, currentProduct + dp(i - 1)(j - 1))
                    }

                val excludeNum1 = dp(i - 1)(j)
                val excludeNum2 = dp(i)(j - 1)

                dp(i)(j) = math.max(math.max(includeBoth, excludeNum1), excludeNum2)
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
    pub fn max_dot_product(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let n = nums1.len();
        let m = nums2.len();

        let min_val = i32::MIN;

        let mut prev_dp = vec![min_val; m + 1];
        let mut curr_dp = vec![min_val; m + 1];

        for i in 1..=n {
            for j in 1..=m {
                let current_product = nums1[i - 1] * nums2[j - 1];

                let mut val_from_diag_option = current_product;

                if prev_dp[j - 1] != min_val {
                    val_from_diag_option = val_from_diag_option.max(prev_dp[j - 1] + current_product);
                }

                curr_dp[j] = prev_dp[j]
                    .max(curr_dp[j - 1])
                    .max(val_from_diag_option);
            }
            prev_dp.copy_from_slice(&curr_dp);
        }

        prev_dp[m]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (max-dot-product nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ([n (length nums1)]
         [m (length nums2)]
         [min-val -1000000000]) ; A sufficiently small number

    (define (dp-row i prev-dp)
      (if (> i n)
          (list-ref prev-dp m)
          (let ([curr-dp (make-list (+ m 1) min-val)])
            (for ([j (in-range 1 (+ m 1))])
              (let* ([num1-val (list-ref nums1 (- i 1))]
                     [num2-val (list-ref nums2 (- j 1))]
                     [current-product (* num1-val num2-val)]
                     [val-from-diag-option current-product])
                (when (not (= (list-ref prev-dp (- j 1)) min-val))
                  (set! val-from-diag-option (max val-from-diag-option (+ (list-ref prev-dp (- j 1)) current-product))))
                (list-set! curr-dp j
                           (max (list-ref prev-dp j)
                                (list-ref curr-dp (- j 1))
                                val-from-diag-option))))
            (dp-row (+ i 1) curr-dp))))

    (dp-row 1 (make-list (+ m 1) min-val))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_dot_product(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
max_dot_product(Nums1, Nums2) ->
    N = length(Nums1),
    M = length(Nums2),
    MinVal = -1000000000, % A sufficiently small number

    % Convert lists to arrays for O(1) access
    Nums1Arr = array:from_list(Nums1),
    Nums2Arr = array:from_list(Nums2),

    % Initialize prev_dp with MinVal
    PrevDpArr = array:from_list(lists:duplicate(M + 1, MinVal)),

    % Outer loop for i from 0 to N-1 (array indices)
    FinalPrevDpArr = lists:foldl(fun(I, AccPrevDpArr) ->
        % Initialize CurrDpArr for this row
        CurrDpArr = array:from_list(lists:duplicate(M + 1, MinVal)),

        % Inner loop for j from 0 to M-1 (array indices)
        UpdatedCurrDpArr = lists:foldl(fun(J, AccCurrDpArrInner) ->
            Num1Val = array:get(I, Nums1Arr),
            Num2Val = array:get(J, Nums2Arr),
            CurrentProduct = Num1Val * Num2Val,

            % prev_dp[j-1] is AccPrevDpArr[J]
            ValFromDiagOption =
                case array:get(J, AccPrevDpArr) of
                    MinVal -> CurrentProduct;
                    PrevDiagVal -> max(CurrentProduct, PrevDiagVal + CurrentProduct)
                end,

            % prev_dp[j] is AccPrevDpArr[J+1]
            PrevDpJ = array:get(J + 1, AccPrevDpArr),
            % curr_dp[j-1] is AccCurrDpArrInner[J]
            CurrDpJMinus1 = array:get(J, AccCurrDpArrInner),

            MaxVal = max(PrevDpJ, max(CurrDpJMinus1, ValFromDiagOption)),

            % Update AccCurrDpArrInner at index J+1
            array:set(J + 1, MaxVal, AccCurrDpArrInner)
        end, CurrDpArr, lists:seq(0, M - 1)),

        UpdatedCurrDpArr % Return CurrDpArr as the new AccPrevDpArr for the next iteration
    end, PrevDpArr, lists:seq(0, N - 1)),

    array:get(M, FinalPrevDpArr).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_dot_product(nums1 :: [integer], nums2 :: [integer]) :: integer
  def max_dot_product(nums1, nums2) do
    n = length(nums1)
    m = length(nums2)
    min_val = -1_000_000_000 # A sufficiently small number

    # Convert lists to tuples for O(1) access
    nums1_tuple = List.to_tuple(nums1)
    nums2_tuple = List.to_tuple(nums2)

    # Initialize prev_dp as a tuple with min_val
    prev_dp_tuple = List.to_tuple(List.duplicate(min_val, m + 1))

    # Outer loop for i from 0 to n-1 (tuple indices)
    final_prev_dp_tuple = Enum.reduce(0..(n - 1), prev_dp_tuple, fn i, acc_prev_dp_tuple ->
      # Initialize curr_dp_tuple for this row
      curr_dp_tuple = List.to_tuple(List.duplicate(min_val, m + 1))

      # Inner loop for j from 0 to m-1 (tuple indices)
      Enum.reduce(0..(m - 1), curr_dp_tuple, fn j, acc_curr_dp_tuple_inner ->
        num1_val = elem(nums1_tuple, i)
        num2_val = elem(nums2_tuple, j)
        current_product = num1_val * num2_val

        # prev_dp[j-1] is acc_prev_dp_tuple[j]
        val_from_diag_option =
          case elem(acc_prev_dp_tuple, j) do
            ^min_val -> current_product
            prev_diag_val -> max(current_product, prev_diag_val + current_product)
          end

        # prev_dp[j] is acc_prev_dp_tuple[j+1]
        prev_dp_j = elem(acc_prev_dp_tuple, j + 1)
        # curr_dp[j-1] is acc_curr_dp_tuple_inner[j]
        curr_dp_j_minus_1 = elem(acc_curr_dp_tuple_inner, j)

        max_val = max(prev_dp_j, max(curr_dp_j_minus_1, val_from_diag_option))

        # Update acc_curr_dp_tuple_inner at index j+1
        put_elem(acc_curr_dp_tuple_inner, j + 1, max_val)
      end)
    end)
    |> elem(m) # Get the final result from the last row, last column (index m)
  end
}
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(M*N), where M is the length of nums1 and N is the length of nums2. This is because we iterate through each cell of the M x N DP table once, and each cell's computation involves a constant number of comparisons and arithmetic operations.

- **Space Complexity:** The space complexity is O(M*N) for storing the 2D DP table. Each cell `dp[i][j]` stores an integer value. Given the constraints (M, N <= 500), an M x N table of integers is feasible.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-08 01:13:31 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved using dynamic programming. We define DP[i][j] as the maximum dot product of two subsequences starting in the position i of nums1 and position j of nums2. We can then fill up the DP table by considering two cases: either we include the current elements in the dot product or we don't. If we include them, the dot product is the sum of the current elements plus the maximum dot product of the remaining subsequences. If we don't include them, the maximum dot product is the maximum of the dot products of the subsequences starting at the next positions. The key intuition here is that we need to consider all possible subsequences and find the one that gives the maximum dot product.

The algorithm works by iterating over all possible pairs of subsequences and calculating the maximum dot product for each pair. We use the DP table to store the maximum dot products for each pair of subsequences, which allows us to avoid recalculating the same dot products multiple times. This approach ensures that we consider all possible subsequences and find the one that gives the maximum dot product. The time complexity of this approach is O(n*m*min(n, m)), where n and m are the lengths of the input arrays, and the space complexity is O(n*m), where n and m are the lengths of the input arrays.

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
    int maxDotProduct(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size(), m = nums2.size();
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, INT_MIN));
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1]);
                dp[i][j] = max(dp[i][j], dp[i - 1][j]);
                dp[i][j] = max(dp[i][j], dp[i][j - 1]);
                dp[i][j] = max(dp[i][j], nums1[i - 1] * nums2[j - 1]);
            }
        }
        return dp[n][m];
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maxDotProduct(int[] nums1, int[] nums2) {
        int n = nums1.length, m = nums2.length;
        int[][] dp = new int[n + 1][m + 1];
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= m; j++) {
                if (i == 0 || j == 0) continue;
                dp[i][j] = Math.max(dp[i][j], dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1]);
                dp[i][j] = Math.max(dp[i][j], dp[i - 1][j]);
                dp[i][j] = Math.max(dp[i][j], dp[i][j - 1]);
                dp[i][j] = Math.max(dp[i][j], nums1[i - 1] * nums2[j - 1]);
            }
        }
        return dp[n][m];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        n, m = len(nums1), len(nums2)
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1])
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
                dp[i][j] = max(dp[i][j], dp[i][j - 1])
                dp[i][j] = max(dp[i][j], nums1[i - 1] * nums2[j - 1])
        return dp[n][m]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1])
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
                dp[i][j] = max(dp[i][j], dp[i][j - 1])
                dp[i][j] = max(dp[i][j], nums1[i - 1] * nums2[j - 1])
        return dp[n][m]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int maxDotProduct(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int n = nums1Size, m = nums2Size;
    int** dp = (int**)malloc((n + 1) * sizeof(int*));
    for (int i = 0; i <= n; i++) {
        dp[i] = (int*)malloc((m + 1) * sizeof(int));
        for (int j = 0; j <= m; j++) {
            dp[i][j] = INT_MIN;
        }
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1]);
            dp[i][j] = max(dp[i][j], dp[i - 1][j]);
            dp[i][j] = max(dp[i][j], dp[i][j - 1]);
            dp[i][j] = max(dp[i][j], nums1[i - 1] * nums2[j - 1]);
        }
    }
    int result = dp[n][m];
    for (int i = 0; i <= n; i++) {
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
    public int MaxDotProduct(int[] nums1, int[] nums2) {
        int m = nums1.Length;
        int n = nums2.Length;
        int[,] dp = new int[m + 1, n + 1];
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                dp[i, j] = Math.Max(dp[i - 1, j - 1] + nums1[i - 1] * nums2[j - 1], Math.Max(dp[i - 1, j], dp[i, j - 1]));
            }
        }
        return Math.Max(dp[m, n], 0);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var maxDotProduct = function(nums1, nums2) {
    let m = nums1.length;
    let n = nums2.length;
    let dp = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            dp[i][j] = Math.max(dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1], Math.max(dp[i - 1][j], dp[i][j - 1]));
        }
    }
    return Math.max(dp[m][n], 0);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxDotProduct(nums1: number[], nums2: number[]): number {
    let m: number = nums1.length;
    let n: number = nums2.length;
    let dp: number[][] = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));
    for (let i: number = 1; i <= m; i++) {
        for (let j: number = 1; j <= n; j++) {
            dp[i][j] = Math.max(dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1], Math.max(dp[i - 1][j], dp[i][j - 1]));
        }
    }
    return Math.max(dp[m][n], 0);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function maxDotProduct($nums1, $nums2) {
        $m = count($nums1);
        $n = count($nums2);
        $dp = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));
        for ($i = 1; $i <= $m; $i++) {
            for ($j = 1; $j <= $n; $j++) {
                $dp[$i][$j] = max($dp[$i - 1][$j - 1] + $nums1[$i - 1] * $nums2[$j - 1], max($dp[$i - 1][$j], $dp[$i][$j - 1]));
            }
        }
        return max($dp[$m][$n], 0);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxDotProduct(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let m = nums1.count
        let n = nums2.count
        var dp = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)
        for i in 1...m {
            for j in 1...n {
                dp[i][j] = max(dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1], max(dp[i - 1][j], dp[i][j - 1]))
            }
        }
        return max(dp[m][n], 0)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxDotProduct(nums1: IntArray, nums2: IntArray): Int {
        val m = nums1.size
        val n = nums2.size
        val dp = Array(m + 1) { IntArray(n + 1) { Int.MIN_VALUE } }
        for (i in 1..m) {
            for (j in 1..n) {
                dp[i][j] = maxOf(dp[i][j], dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1], nums1[i - 1] * nums2[j - 1])
                if (i > 1) dp[i][j] = maxOf(dp[i][j], dp[i - 1][j])
                if (j > 1) dp[i][j] = maxOf(dp[i][j], dp[i][j - 1])
            }
        }
        return dp.maxOf { it.max() }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maxDotProduct(List<int> nums1, List<int> nums2) {
    int m = nums1.length;
    int n = nums2.length;
    List<List<int>> dp = List.generate(m + 1, (i) => List.generate(n + 1, (j) => int.MinValue));
    for (int i = 1; i <= m; i++) {
      for (int j = 1; j <= n; j++) {
        dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1], nums1[i - 1] * nums2[j - 1]);
        if (i > 1) dp[i][j] = max(dp[i][j], dp[i - 1][j]);
        if (j > 1) dp[i][j] = max(dp[i][j], dp[i][j - 1]);
      }
    }
    int max = int.MinValue;
    for (int i = 1; i <= m; i++) {
      for (int j = 1; j <= n; j++) {
        max = max(max, dp[i][j]);
      }
    }
    return max;
  }
  int max(int a, int b, int c) {
    return max(max(a, b), c);
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxDotProduct(nums1 []int, nums2 []int) int {
    m, n := len(nums1), len(nums2)
    dp := make([][]int, m + 1)
    for i := range dp {
        dp[i] = make([]int, n + 1)
        for j := range dp[i] {
            dp[i][j] = -1e9
        }
    }
    for i := 1; i <= m; i++ {
        for j := 1; j <= n; j++ {
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1], nums1[i - 1] * nums2[j - 1])
            if i > 1 {
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
            }
            if j > 1 {
                dp[i][j] = max(dp[i][j], dp[i][j - 1])
            }
        }
    }
    maxVal := -1e9
    for i := 1; i <= m; i++ {
        for j := 1; j <= n; j++ {
            maxVal = max(maxVal, dp[i][j])
        }
    }
    return maxVal
}

func max(a, b, c int) int {
    if a > b {
        if a > c {
            return a
        }
        return c
    }
    if b > c {
        return b
    }
    return c
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def max_dot_product(nums1, nums2)
    m, n = nums1.size, nums2.size
    dp = Array.new(m + 1) { Array.new(n + 1, -1e9) }
    for i in 1..m
        for j in 1..n
            dp[i][j] = [dp[i][j], dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1], nums1[i - 1] * nums2[j - 1]].max
            if i > 1
                dp[i][j] = [dp[i][j], dp[i - 1][j]].max
            end
            if j > 1
                dp[i][j] = [dp[i][j], dp[i][j - 1]].max
            end
        end
    end
    max_val = -1e9
    for i in 1..m
        for j in 1..n
            max_val = [max_val, dp[i][j]].max
        end
    end
    max_val
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxDotProduct(nums1: Array[Int], nums2: Array[Int]): Int = {
        val m = nums1.length
        val n = nums2.length
        val dp = Array.ofDim[Int](m + 1, n + 1)
        for (i <- 1 to m) {
            for (j <- 1 to n) {
                dp(i)(j) = math.max(math.max(dp(i)(j), dp(i - 1)(j - 1) + nums1(i - 1) * nums2(j - 1)), nums1(i - 1) * nums2(j - 1))
                if (i > 1) dp(i)(j) = math.max(dp(i)(j), dp(i - 1)(j))
                if (j > 1) dp(i)(j) = math.max(dp(i)(j), dp(i)(j - 1))
            }
        }
        var maxVal = Int.MinValue
        for (i <- 1 to m) {
            for (j <- 1 to n) {
                maxVal = math.max(maxVal, dp(i)(j))
            }
        }
        maxVal
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_dot_product(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let n = nums1.len();
        let m = nums2.len();
        let mut dp = vec![vec![i32::MIN; m + 1]; n + 1];
        for i in 1..=n {
            for j in 1..=m {
                dp[i][j] = dp[i][j - 1].max(dp[i - 1][j]).max(dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1]);
            }
        }
        let mut ans = i32::MIN;
        for i in 1..=n {
            for j in 1..=m {
                if i == j {
                    ans = ans.max(dp[i][j]);
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
(define/contract (max-dot-product nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* (
           [n (length nums1)]
           [m (length nums2)]
           [dp (make-list (add1 n) (lambda (x) (make-list (add1 m) -1000000000)))])
    (for (
         [i (range 1 (add1 n))])
      (for (
           [j (range 1 (add1 m))])
        (set! (list-ref (list-ref dp i) j)
              (max (list-ref (list-ref dp i) (sub1 j))
                   (list-ref (list-ref dp (sub1 i)) j)
                   (+ (list-ref (list-ref dp (sub1 i)) (sub1 j))
                      (* (list-ref nums1 (sub1 i))
                         (list-ref nums2 (sub1 j))))))))
    (let (
          [ans -1000000000])
      (for (
           [i (range 1 (add1 n))])
        (for (
             [j (range 1 (add1 m))])
          (when (= i j)
            (set! ans (max ans (list-ref (list-ref dp i) j))))))
      ans)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
max_dot_product(Nums1, Nums2) ->
  N = length(Nums1),
  M = length(Nums2),
  DP = lists:duplicate(N + 1, lists:duplicate(M + 1, -1000000000)),
  F = fun(I, J) ->
           case I > N orelse J > M of
             true -> ok;
             false ->
               NewDP =
                 case I > 1 orelse J > 1 of
                   true ->
                     max(lists:nth(J, lists:nth(I, DP)),
                         max(lists:nth(J, lists:nth(I - 1, DP)),
                            max(lists:nth(J - 1, lists:nth(I, DP)),
                               lists:nth(J - 1, lists:nth(I - 1, DP)) + lists:nth(I - 1, Nums1) * lists:nth(J - 1, Nums2))));
                   false -> 0
                 end,
               lists:sublist(lists:nth(I, DP), 1, J - 1) ++ [NewDP] ++ lists:sublist(lists:nth(I, DP), J + 1, length(lists:nth(I, DP))),
               F(I + 1, J),
               F(I, J + 1)
           end
         end,
  F(1, 1),
  Ans = -1000000000,
  F2 = fun(I, J) ->
           case I > N orelse J > M of
             true -> Ans;
             false ->
               case I == J of
                 true ->
                   F2(I + 1, J + 1);
                 false ->
                   F2(I + 1, J)
               end
           end
         end,
  F2(1, 1).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_dot_product(nums1 :: [integer], nums2 :: [integer]) :: integer
  def max_dot_product(nums1, nums2) do
    n = length(nums1)
    m = length(nums2)
    dp = for _ <- 1..n+1, do: for _ <- 1..m+1, do: -1000000000
    dp = Enum.reduce(1..n, dp, fn i, dp ->
      Enum.reduce(1..m, dp, fn j, dp ->
        new_dp =
          if i > 1 or j > 1 do
            max(Enum.at(Enum.at(dp, i), j - 1),
                 max(Enum.at(Enum.at(dp, i - 1), j),
                    max(Enum.at(Enum.at(dp, i), j - 1),
                       Enum.at(Enum.at(dp, i - 1), j - 1) + Enum.at(nums1, i - 1) * Enum.at(nums2, j - 1))))
          else
            0
          end,
        List.update_at(dp, i, fn x -> List.update_at(x, j, fn _ -> new_dp end) end)
      end)
    end)
    ans = -1000000000
    Enum.reduce(1..n, ans, fn i, ans ->
      Enum.reduce(1..m, ans, fn j, ans ->
        if i == j do
          max(ans, Enum.at(Enum.at(dp, i), j))
        else
          ans
        end
      end)
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this approach is O(n*m*min(n, m)), where n and m are the lengths of the input arrays. This is because we need to iterate over all possible pairs of subsequences, and for each pair, we need to calculate the maximum dot product. The number of possible pairs of subsequences is proportional to the product of the lengths of the input arrays, and the time complexity of calculating the maximum dot product for each pair is proportional to the minimum of the lengths of the input arrays.

- **Space Complexity:** The space complexity of this approach is O(n*m), where n and m are the lengths of the input arrays. This is because we need to store the maximum dot products for each pair of subsequences in the DP table, and the size of the DP table is proportional to the product of the lengths of the input arrays.

</div>
</details>
