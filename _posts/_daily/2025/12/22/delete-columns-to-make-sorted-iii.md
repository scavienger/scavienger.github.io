---
layout: post
title: "Delete Columns to Make Sorted III"
date: 2025-12-22 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "String", "Dynamic Programming"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/delete-columns-to-make-sorted-iii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minDeletionSize(std::vector<std::string>&\
        \ strs) {\n        int n = strs.size();\n        int L = strs[0].length();\n\
        \n        std::vector<int> dp(L, 1);\n\n        for (int i = 0; i < L; ++i)\
        \ {\n            for (int j = 0; j < i; ++j) {\n                bool is_valid_pair\
        \ = true;\n                for (int row = 0; row < n; ++row) {\n           \
        \         if (strs[row][j] > strs[row][i]) {\n                        is_valid_pair\
        \ = false;\n                        break;\n                    }\n        \
        \        }\n                if (is_valid_pair) {\n                    dp[i]\
        \ = std::max(dp[i], dp[j] + 1);\n                }\n            }\n        }\n\
        \n        int max_kept_columns = *std::max_element(dp.begin(), dp.end());\n\n\
        \        return L - max_kept_columns;\n    }\n};"
      java: "import java.util.Arrays;\n\nclass Solution {\n    public int minDeletionSize(String[]\
        \ strs) {\n        int n = strs.length;\n        int L = strs[0].length();\n\
        \n        int[] dp = new int[L];\n        Arrays.fill(dp, 1);\n\n        for\
        \ (int i = 0; i < L; ++i) {\n            for (int j = 0; j < i; ++j) {\n   \
        \             boolean isValidPair = true;\n                for (int row = 0;\
        \ row < n; ++row) {\n                    if (strs[row].charAt(j) > strs[row].charAt(i))\
        \ {\n                        isValidPair = false;\n                        break;\n\
        \                    }\n                }\n                if (isValidPair)\
        \ {\n                    dp[i] = Math.max(dp[i], dp[j] + 1);\n             \
        \   }\n            }\n        }\n\n        int maxKeptColumns = 0;\n       \
        \ for (int val : dp) {\n            maxKeptColumns = Math.max(maxKeptColumns,\
        \ val);\n        }\n\n        return L - maxKeptColumns;\n    }\n}"
      python: "class Solution:\n    def minDeletionSize(self, strs: List[str]) -> int:\n\
        \        n = len(strs)\n        L = len(strs[0])\n\n        dp = [1] * L\n\n\
        \        for i in range(L):\n            for j in range(i):\n              \
        \  is_valid_pair = True\n                for row in range(n):\n            \
        \        if strs[row][j] > strs[row][i]:\n                        is_valid_pair\
        \ = False\n                        break\n                if is_valid_pair:\n\
        \                    dp[i] = max(dp[i], dp[j] + 1)\n\n        max_kept_columns\
        \ = max(dp)\n\n        return L - max_kept_columns"
      python3: "class Solution:\n    def minDeletionSize(self, strs: List[str]) -> int:\n\
        \        n = len(strs)\n        L = len(strs[0])\n\n        dp = [1] * L\n\n\
        \        for i in range(L):\n            for j in range(i):\n              \
        \  is_valid_pair = True\n                for row in range(n):\n            \
        \        if strs[row][j] > strs[row][i]:\n                        is_valid_pair\
        \ = False\n                        break\n                if is_valid_pair:\n\
        \                    dp[i] = max(dp[i], dp[j] + 1)\n\n        max_kept_columns\
        \ = max(dp)\n\n        return L - max_kept_columns"
      c: "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <stdbool.h>\n\
        \nint findMax(int* arr, int size) {\n    int maxVal = arr[0];\n    for (int\
        \ i = 1; i < size; ++i) {\n        if (arr[i] > maxVal) {\n            maxVal\
        \ = arr[i];\n        }\n    }\n    return maxVal;\n}\n\nint minDeletionSize(char**\
        \ strs, int strsSize) {\n    int n = strsSize;\n    int L = strlen(strs[0]);\n\
        \n    int* dp = (int*)malloc(L * sizeof(int));\n    for (int k = 0; k < L; ++k)\
        \ {\n        dp[k] = 1;\n    }\n\n    for (int i = 0; i < L; ++i) {\n      \
        \  for (int j = 0; j < i; ++j) {\n            bool isValidPair = true;\n   \
        \         for (int row = 0; row < n; ++row) {\n                if (strs[row][j]\
        \ > strs[row][i]) {\n                    isValidPair = false;\n            \
        \        break;\n                }\n            }\n            if (isValidPair)\
        \ {\n                dp[i] = (dp[i] > dp[j] + 1) ? dp[i] : (dp[j] + 1);\n  \
        \          }\n        }\n    }\n\n    int maxKeptColumns = findMax(dp, L);\n\
        \n    free(dp);\n\n    return L - maxKeptColumns;\n}"
      csharp: "using System;\nusing System.Linq;\n\npublic class Solution {\n    public\
        \ int MinDeletionSize(string[] strs) {\n        int n = strs.Length;\n     \
        \   int L = strs[0].Length;\n\n        int[] dp = new int[L];\n        for (int\
        \ k = 0; k < L; k++) {\n            dp[k] = 1;\n        }\n\n        for (int\
        \ i = 0; i < L; ++i) {\n            for (int j = 0; j < i; ++j) {\n        \
        \        bool isValidPair = true;\n                for (int row = 0; row < n;\
        \ ++row) {\n                    if (strs[row][j] > strs[row][i]) {\n       \
        \                 isValidPair = false;\n                        break;\n   \
        \                 }\n                }\n                if (isValidPair) {\n\
        \                    dp[i] = Math.Max(dp[i], dp[j] + 1);\n                }\n\
        \            }\n        }\n\n        int maxKeptColumns = dp.Max();\n\n    \
        \    return L - maxKeptColumns;\n    }\n}"
      javascript: "/**\n * @param {string[]} strs\n * @return {number}\n */\nvar minDeletionSize\
        \ = function(strs) {\n    const n = strs.length;\n    const L = strs[0].length;\n\
        \n    const dp = new Array(L).fill(1);\n\n    for (let i = 0; i < L; ++i) {\n\
        \        for (let j = 0; j < i; ++j) {\n            let isValidPair = true;\n\
        \            for (let row = 0; row < n; ++row) {\n                if (strs[row][j]\
        \ > strs[row][i]) {\n                    isValidPair = false;\n            \
        \        break;\n                }\n            }\n            if (isValidPair)\
        \ {\n                dp[i] = Math.max(dp[i], dp[j] + 1);\n            }\n  \
        \      }\n    }\n\n    const maxKeptColumns = Math.max(...dp);\n\n    return\
        \ L - maxKeptColumns;\n};"
      typescript: "function minDeletionSize(strs: string[]): number {\n    const n =\
        \ strs.length;\n    const L = strs[0].length;\n\n    const dp: number[] = new\
        \ Array(L).fill(1);\n\n    for (let i = 0; i < L; ++i) {\n        for (let j\
        \ = 0; j < i; ++j) {\n            let isValidPair: boolean = true;\n       \
        \     for (let row = 0; row < n; ++row) {\n                if (strs[row][j]\
        \ > strs[row][i]) {\n                    isValidPair = false;\n            \
        \        break;\n                }\n            }\n            if (isValidPair)\
        \ {\n                dp[i] = Math.max(dp[i], dp[j] + 1);\n            }\n  \
        \      }\n\n    }\n\n    const maxKeptColumns: number = Math.max(...dp);\n\n\
        \    return L - maxKeptColumns;\n};"
      php: "<?php\nclass Solution {\n\n    /**\n     * @param String[] $strs\n     *\
        \ @return Integer\n     */\n    function minDeletionSize($strs) {\n        $n\
        \ = count($strs);\n        $L = strlen($strs[0]);\n\n        $dp = array_fill(0,\
        \ $L, 1);\n\n        for ($i = 0; $i < $L; ++$i) {\n            for ($j = 0;\
        \ $j < $i; ++$j) {\n                $isValidPair = true;\n                for\
        \ ($row = 0; $row < $n; ++$row) {\n                    if ($strs[$row][$j] >\
        \ $strs[$row][$i]) {\n                        $isValidPair = false;\n      \
        \                  break;\n                    }\n                }\n      \
        \          if ($isValidPair) {\n                    $dp[$i] = max($dp[$i], $dp[$j]\
        \ + 1);\n                }\n            }\n        }\n\n        $maxKeptColumns\
        \ = max($dp);\n\n        return $L - $maxKeptColumns;\n    }\n}\n?>"
      swift: "import Foundation\n\nclass Solution {\n    func minDeletionSize(_ strs:\
        \ [String]) -> Int {\n        let n = strs.count\n        let L = strs[0].count\n\
        \n        let charArrays: [[Character]] = strs.map { Array($0) }\n\n       \
        \ var dp = Array(repeating: 1, count: L)\n\n        for i in 0..<L {\n     \
        \       for j in 0..<i {\n                var isValidPair = true\n         \
        \       for row in 0..<n {\n                    if charArrays[row][j] > charArrays[row][i]\
        \ {\n                        isValidPair = false\n                        break\n\
        \                    }\n                }\n                if isValidPair {\n\
        \                    dp[i] = max(dp[i], dp[j] + 1)\n                }\n    \
        \        }\n        }\n\n        let maxKeptColumns = dp.max()!\n\n        return\
        \ L - maxKeptColumns\n    }\n}"
      kotlin: "import kotlin.math.max\n\nclass Solution {\n    fun minDeletionSize(strs:\
        \ Array<String>): Int {\n        val n = strs.size\n        val L = strs[0].length;\n\
        \n        val dp = IntArray(L) { 1 }\n\n        for (i in 0 until L) {\n   \
        \         for (j in 0 until i) {\n                var isValidPair = true\n \
        \               for (row in 0 until n) {\n                    if (strs[row][j]\
        \ > strs[row][i]) {\n                        isValidPair = false\n         \
        \               break\n                    }\n                }\n          \
        \      if (isValidPair) {\n                    dp[i] = max(dp[i], dp[j] + 1)\n\
        \                }\n            }\n        }\n\n        val maxKeptColumns =\
        \ dp.maxOrNull()!!\n\n        return L - maxKeptColumns\n    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int minDeletionSize(List<String>\
        \ strs) {\n    int n = strs.length;\n    int L = strs[0].length;\n\n    List<int>\
        \ dp = List<int>.filled(L, 1);\n\n    for (int i = 0; i < L; ++i) {\n      for\
        \ (int j = 0; j < i; ++j) {\n        bool isValidPair = true;\n        for (int\
        \ row = 0; row < n; ++row) {\n          if (strs[row].codeUnitAt(j) > strs[row].codeUnitAt(i))\
        \ {\n            isValidPair = false;\n            break;\n          }\n   \
        \     }\n        if (isValidPair) {\n          dp[i] = max(dp[i], dp[j] + 1);\n\
        \        }\n      }\n    }\n\n    int maxKeptColumns = dp.reduce(max);\n\n \
        \   return L - maxKeptColumns;\n  }\n}"
      go: "package main\n\nimport (\n\t\"math\"\n)\n\nfunc minDeletionSize(strs []string)\
        \ int {\n    n := len(strs)\n    L := len(strs[0])\n\n    dp := make([]int,\
        \ L)\n    for i := range dp {\n        dp[i] = 1\n    }\n\n    for i := 0; i\
        \ < L; i++ {\n        for j := 0; j < i; j++ {\n            isValidPair := true\n\
        \            for row := 0; row < n; row++ {\n                if strs[row][j]\
        \ > strs[row][i] {\n                    isValidPair = false\n              \
        \      break\n                }\n            }\n            if isValidPair {\n\
        \                dp[i] = int(math.Max(float64(dp[i]), float64(dp[j] + 1)))\n\
        \            }\n        }\n    }\n\n    maxKeptColumns := 0\n    for _, val\
        \ := range dp {\n        maxKeptColumns = int(math.Max(float64(maxKeptColumns),\
        \ float64(val)))\n    }\n\n    return L - maxKeptColumns\n}"
      ruby: "# @param {String[]} strs\n# @return {Integer}\ndef min_deletion_size(strs)\n\
        \    n = strs.length\n    L = strs[0].length\n\n    dp = Array.new(L, 1)\n\n\
        \    (0...L).each do |i|\n        (0...i).each do |j|\n            is_valid_pair\
        \ = true\n            (0...n).each do |row|\n                if strs[row][j]\
        \ > strs[row][i]\n                    is_valid_pair = false\n              \
        \      break\n                end\n            end\n            if is_valid_pair\n\
        \                dp[i] = [dp[i], dp[j] + 1].max\n            end\n        end\n\
        \    end\n\n    max_kept_columns = dp.max\n\n    L - max_kept_columns\nend"
      scala: "import scala.math.max\n\nobject Solution {\n    def minDeletionSize(strs:\
        \ Array[String]): Int = {\n        val n = strs.length\n        val L = strs(0).length\n\
        \n        val dp = Array.fill(L)(1)\n\n        for (i <- 0 until L) {\n    \
        \        for (j <- 0 until i) {\n                var isValidPair = true\n  \
        \              for (row <- 0 until n) {\n                    if (strs(row)(j)\
        \ > strs(row)(i)) {\n                        isValidPair = false\n         \
        \               break\n                    }\n                }\n          \
        \      if (isValidPair) {\n                    dp(i) = max(dp(i), dp(j) + 1)\n\
        \                }\n            }\n        }\n\n        val maxKeptColumns =\
        \ dp.max\n\n        L - maxKeptColumns\n    }\n}"
      rust: "use std::cmp::max;\n\nimpl Solution {\n    pub fn min_deletion_size(strs:\
        \ Vec<String>) -> i32 {\n        let n = strs.len();\n        let l = strs[0].len();\n\
        \n        let mut dp = vec![1; l];\n\n        for i in 0..l {\n            for\
        \ j in 0..i {\n                let mut is_valid_pair = true;\n             \
        \   for row in 0..n {\n                    let char_j = strs[row].as_bytes()[j];\n\
        \                    let char_i = strs[row].as_bytes()[i];\n               \
        \     if char_j > char_i {\n                        is_valid_pair = false;\n\
        \                        break;\n                    }\n                }\n\
        \                if is_valid_pair {\n                    dp[i] = max(dp[i],\
        \ dp[j] + 1);\n                }\n            }\n        }\n\n        let max_kept_columns\
        \ = *dp.iter().max().unwrap();\n\n        (l - max_kept_columns) as i32\n  \
        \  }\n}"
      racket: "#lang racket\n\n(define (min-deletion-size strs)\n  (define n (length\
        \ strs))\n  (define L (string-length (car strs)))\n\n  (define dp (make-vector\
        \ L 1))\n\n  (for ([i (in-range L)])\n    (for ([j (in-range i)])\n      (define\
        \ is-valid-pair? #t)\n      (for ([row (in-range n)])\n        (when (> (string-ref\
        \ (list-ref strs row) j)\n                 (string-ref (list-ref strs row) i))\n\
        \          (set! is-valid-pair? #f)\n          (break)))\n      (when is-valid-pair?\n\
        \        (vector-set! dp i (max (vector-ref dp i) (+ (vector-ref dp j) 1))))))\n\
        \n  (define max-kept-columns (vector-ref dp 0))\n  (for ([k (in-range 1 L)])\n\
        \    (set! max-kept-columns (max max-kept-columns (vector-ref dp k))))\n\n \
        \ (- L max-kept-columns))"
      erlang: "-module(solution).\n-export([min_deletion_size/1]).\n\n-include_lib(\"\
        stdlib/include/array.hrl\").\n\nmin_deletion_size(Strs) ->\n    N = length(Strs),\n\
        \    L = length(hd(Strs)),\n\n    StrsAsTupleArray = array:from_list([list_to_tuple(S)\
        \ || S <- Strs]),\n\n    DpArray = array:new([{size, L}, {fixed, true}, {default,\
        \ 1}]),\n\n    DpFinal = lists:foldl(\n        fun(I, CurrentDp) ->\n      \
        \      lists:foldl(\n                fun(J, InnerDp) ->\n                  \
        \  IsValidPair = lists:all(\n                        fun(RowIdx) ->\n      \
        \                      StringTuple = array:get(RowIdx, StrsAsTupleArray),\n\
        \                            CharJ = element(J + 1, StringTuple),\n        \
        \                    CharI = element(I + 1, StringTuple),\n                \
        \            CharJ =< CharI\n                        end,\n                \
        \        lists:seq(0, N - 1)\n                    ),\n                    if\
        \ IsValidPair ->\n                        array:set(I, max(array:get(I, InnerDp),\
        \ array:get(J, InnerDp) + 1), InnerDp);\n                    true ->\n     \
        \                   InnerDp\n                    end\n                end,\n\
        \                CurrentDp,\n                lists:seq(0, I - 1)\n         \
        \   )\n        end,\n        DpArray,\n        lists:seq(0, L - 1)\n    ),\n\
        \n    MaxKeptColumns = lists:foldl(fun(Val, Acc) -> max(Val, Acc) end, 0, array:to_list(DpFinal)),\n\
        \    L - MaxKeptColumns.\n\nmax(A, B) when A >= B -> A;\nmax(A, B) -> B."
      elixir: "defmodule Solution do\n  def min_deletion_size(strs) do\n    n = length(strs)\n\
        \    l = String.length(hd(strs))\n\n    strs_as_tuple_of_tuples =\n      strs\n\
        \      |> Enum.map(&String.to_charlist/1)\n      |> Enum.map(&List.to_tuple/1)\n\
        \      |> List.to_tuple\n\n    dp_initial = List.duplicate(1, l) |> List.to_tuple\n\
        \n    dp_final = Enum.reduce(0..(l - 1), dp_initial, fn i, current_dp ->\n \
        \     Enum.reduce(0..(i - 1), current_dp, fn j, inner_dp ->\n        is_valid_pair\
        \ = Enum.all?(0..(n - 1), fn row_idx ->\n          string_tuple = elem(strs_as_tuple_of_tuples,\
        \ row_idx)\n          char_j = elem(string_tuple, j)\n          char_i = elem(string_tuple,\
        \ i)\n          char_j <= char_i\n        end)\n\n        if is_valid_pair do\n\
        \          Tuple.replace_at(inner_dp, i, max(elem(inner_dp, i), elem(inner_dp,\
        \ j) + 1))\n        else\n          inner_dp\n        end\n      end)\n    end)\n\
        \n    max_kept_columns = Enum.max(Tuple.to_list(dp_final))\n    l - max_kept_columns\n\
        \  end\n\n  defp max(a, b) when a >= b, do: a\n  defp max(a, b), do: b\nend"
    approach: 'The problem asks us to find the minimum number of columns to delete such
      that the remaining characters in each row form a lexicographically sorted string.
      This is equivalent to finding the maximum number of columns we can *keep* such
      that they satisfy the sorting condition. Let `L` be the length of each string
      (number of columns) and `n` be the number of strings (rows). We are looking for
      a subsequence of column indices `c_1, c_2, ..., c_k` such that `0 <= c_1 < c_2
      < ... < c_k < L`, and for every string `s` in `strs`, `s[c_i] <= s[c_{i+1}]` for
      all `1 <= i < k`. The minimum deletions will then be `L - k_max`, where `k_max`
      is the length of the longest such subsequence.

      This problem can be solved using dynamic programming, similar to the Longest Increasing
      Subsequence (LIS) problem. We define `dp[i]` as the maximum length of a valid
      subsequence of columns ending at index `i`. To compute `dp[i]`, we iterate through
      all previous columns `j` (where `0 <= j < i`). If column `j` can precede column
      `i` in a valid subsequence (meaning `strs[row][j] <= strs[row][i]` for all rows
      `row`), then we can potentially extend the subsequence ending at `j` by including
      `i`. Thus, `dp[i]` is updated to `max(dp[i], dp[j] + 1)`. The base case is `dp[i]
      = 1` for all `i`, as any single column forms a valid subsequence. After filling
      the `dp` array, the maximum value in `dp` represents `k_max`, and the result is
      `L - k_max`.'
    time_complexity: 'The time complexity is O(L^2 * n), where `L` is the length of
      each string and `n` is the number of strings. This is derived from three nested
      loops: the outermost loop iterates `L` times (for `i`), the middle loop iterates
      up to `L` times (for `j`), and the innermost loop iterates `n` times (for `row`)
      to check the validity of a pair of columns. In some functional languages like
      Elixir, list/tuple updates or character access might incur an additional `O(L)`
      factor, leading to a worst-case complexity of O(L^2 * (n + L)). Given the constraints
      (L, n <= 100), this results in roughly 100^2 * 100 = 1,000,000 operations, which
      is efficient enough.'
    space_complexity: The space complexity is O(L) for storing the `dp` array. In languages
      like Swift, Erlang, or Elixir, converting strings to character arrays or tuples
      for efficient O(1) character access might require O(n * L) additional space for
      preprocessing the input strings. However, the core DP state itself only requires
      O(L) space.
    elapsed_time: 101.82619166374207
    model: gemini-2.5-flash
    generated_at: '2025-12-22 01:11:53 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int minDeletionSize(vector<string>& strs)\
        \ {\n        int count = 0;\n        int n = strs.size();\n        int m = strs[0].size();\n\
        \        for (int j = 0; j < m; j++) {\n            for (int i = 1; i < n; i++)\
        \ {\n                if (strs[i - 1][j] > strs[i][j]) {\n                  \
        \  count++;\n                    break;\n                }\n            }\n\
        \        }\n        return count;\n    }\n};"
      java: "class Solution {\n    public int minDeletionSize(String[] strs) {\n   \
        \     int count = 0;\n        int n = strs.length;\n        int m = strs[0].length();\n\
        \        for (int j = 0; j < m; j++) {\n            for (int i = 1; i < n; i++)\
        \ {\n                if (strs[i - 1].charAt(j) > strs[i].charAt(j)) {\n    \
        \                count++;\n                    break;\n                }\n \
        \           }\n        }\n        return count;\n    }\n}"
      python: "class Solution:\n    def minDeletionSize(self, strs: list[str]) -> int:\n\
        \        count = 0\n        n = len(strs)\n        m = len(strs[0])\n      \
        \  for j in range(m):\n            for i in range(1, n):\n                if\
        \ strs[i - 1][j] > strs[i][j]:\n                    count += 1\n           \
        \         break\n        return count"
      python3: "class Solution:\n    def minDeletionSize(self, strs: list[str]) -> int:\n\
        \        count = 0\n        n = len(strs)\n        m = len(strs[0])\n      \
        \  for j in range(m):\n            for i in range(1, n):\n                if\
        \ strs[i - 1][j] > strs[i][j]:\n                    count += 1\n           \
        \         break\n        return count"
      c: "int minDeletionSize(char ** strs, int strsSize) {\n    int count = 0;\n  \
        \  int m = strlen(strs[0]);\n    for (int j = 0; j < m; j++) {\n        for\
        \ (int i = 1; i < strsSize; i++) {\n            if (strs[i - 1][j] > strs[i][j])\
        \ {\n                count++;\n                break;\n            }\n     \
        \   }\n    }\n    return count;\n}"
      csharp: "public class Solution {\n    public int MinDeletionSize(string[] strs)\
        \ {\n        int count = 0;\n        int n = strs.Length;\n        int m = strs[0].Length;\n\
        \        for (int j = 0; j < m; j++) {\n            for (int i = 1; i < n; i++)\
        \ {\n                if (strs[i - 1][j] > strs[i][j]) {\n                  \
        \  count++;\n                    break;\n                }\n            }\n\
        \        }\n        return count;\n    }\n}"
      javascript: "var minDeletionSize = function(strs) {\n    let count = 0;\n    let\
        \ n = strs.length;\n    let m = strs[0].length;\n    for (let j = 0; j < m;\
        \ j++) {\n        for (let i = 1; i < n; i++) {\n            if (strs[i - 1][j]\
        \ > strs[i][j]) {\n                count++;\n                break;\n      \
        \      }\n        }\n    }\n    return count;\n};"
      typescript: "function minDeletionSize(strs: string[]): number {\n    let count:\
        \ number = 0;\n    let n: number = strs.length;\n    let m: number = strs[0].length;\n\
        \    for (let j: number = 0; j < m; j++) {\n        for (let i: number = 1;\
        \ i < n; i++) {\n            if (strs[i - 1][j] > strs[i][j]) {\n          \
        \      count++;\n                break;\n            }\n        }\n    }\n \
        \   return count;\n}"
      php: "class Solution {\n    function minDeletionSize($strs) {\n        $count\
        \ = 0;\n        $n = count($strs);\n        $m = strlen($strs[0]);\n       \
        \ for ($j = 0; $j < $m; $j++) {\n            for ($i = 1; $i < $n; $i++) {\n\
        \                if ($strs[$i - 1][$j] > $strs[$i][$j]) {\n                \
        \    $count++;\n                    break;\n                }\n            }\n\
        \        }\n        return $count;\n    }\n}"
      swift: "class Solution {\n    func minDeletionSize(_ strs: [String]) -> Int {\n\
        \        var count = 0\n        let n = strs.count\n        let m = strs[0].count\n\
        \        for j in 0..<m {\n            for i in 1..<n {\n                if\
        \ strs[i - 1][strs[i - 1].index(strs[i - 1].startIndex, offsetBy: j)] > strs[i][strs[i].index(strs[i].startIndex,\
        \ offsetBy: j)] {\n                    count += 1\n                    break\n\
        \                }\n            }\n        }\n        return count\n    }\n}"
      kotlin: "class Solution {\n    fun minDeletionSize(strs: Array<String>): Int {\n\
        \        var count = 0\n        val n = strs.size\n        val m = strs[0].length\n\
        \        for (j in 0 until m) {\n            for (i in 1 until n) {\n      \
        \          if (strs[i - 1][j] > strs[i][j]) {\n                    count++\n\
        \                    break\n                }\n            }\n        }\n  \
        \      return count\n    }\n}"
      dart: "class Solution {\n    int minDeletionSize(List<String> strs) {\n      \
        \  int count = 0;\n        int n = strs.length;\n        int m = strs[0].length;\n\
        \        for (int j = 0; j < m; j++) {\n            for (int i = 1; i < n; i++)\
        \ {\n                if (strs[i - 1][j] > strs[i][j]) {\n                  \
        \  count++;\n                    break;\n                }\n            }\n\
        \        }\n        return count;\n    }\n}"
      go: "func minDeletionSize(strs []string) int {\n    count := 0\n    n := len(strs)\n\
        \    m := len(strs[0])\n    for j := 0; j < m; j++ {\n        for i := 1; i\
        \ < n; i++ {\n            if strs[i-1][j] > strs[i][j] {\n                count++\n\
        \                break\n            }\n        }\n    }\n    return count\n}"
      ruby: "def min_deletion_size(strs)\n    count = 0\n    n = strs.size\n    m =\
        \ strs[0].size\n    (0...m).each do |j|\n        (1...n).each do |i|\n     \
        \       if strs[i - 1][j] > strs[i][j]\n                count += 1\n       \
        \         break\n            end\n        end\n    end\n    count\nend"
      scala: "object Solution {\n    def minDeletionSize(strs: Array[String]): Int =\
        \ {\n        var count = 0\n        val n = strs.length\n        val m = strs(0).length\n\
        \        for (j <- 0 until m) {\n            for (i <- 1 until n) {\n      \
        \          if (strs(i - 1)(j) > strs(i)(j)) {\n                    count +=\
        \ 1\n                    i\n                }\n            }\n        }\n  \
        \      count\n    }\n}"
      rust: "impl Solution {\n    pub fn min_deletion_size(strs: Vec<String>) -> i32\
        \ {\n        let mut count = 0;\n        let n = strs.len();\n        let m\
        \ = strs[0].len();\n        for j in 0..m {\n            for i in 1..n {\n \
        \               if strs[i - 1].as_bytes()[j] > strs[i].as_bytes()[j] {\n   \
        \                 count += 1;\n                    break;\n                }\n\
        \            }\n        }\n        count\n    }\n}"
      racket: "define (min-deletion-size strs)\n    (let ((count 0)\n          (n (length\
        \ strs))\n          (m (string-length (car strs))))\n      (do ((j 0 (+ j 1)))\n\
        \          ((= j m) count)\n        (do ((i 1 (+ i 1)))\n            ((= i n))\n\
        \          (if (> (string-ref (list-ref strs (- i 1)) j) (string-ref (list-ref\
        \ strs i) j))\n              (begin\n                (set! count (+ count 1))\n\
        \                (set! i n)))))))"
      erlang: "min_deletion_size(Strs) ->\n    Count =\n        lists:foldl(\n     \
        \     fun(J, {Count, N, M}) ->\n                  lists:foldl(\n           \
        \         fun(I, {Count, N, M}) ->\n                            if\n       \
        \                         string:slice(string:part(Strs, I - 1), J + 1, 1) >\
        \ string:slice(string:part(Strs, I), J + 1, 1) ->\n                        \
        \            {Count + 1, N, M};\n                                true ->\n \
        \                                   {Count, N, M}\n                        \
        \    end\n                    end,\n                    {Count, N, M},\n   \
        \                 lists:seq(1, N - 1))\n          end,\n          {0, length(Strs),\
        \ string:length(hd(Strs))},\n          lists:seq(0, string:length(hd(Strs))\
        \ - 1)),\n    Count."
      elixir: "def min_deletion_size(strs) do\n    count = 0\n    n = length(strs)\n\
        \    m = String.length(Enum.at(strs, 0))\n    for j <- 0..m-1 do\n        for\
        \ i <- 1..n-1 do\n            if String.at(Enum.at(strs, i-1), j) > String.at(Enum.at(strs,\
        \ i), j) do\n                count = count + 1\n                break\n    \
        \        end\n        end\n    end\n    count\nend"
    approach: The problem can be solved by iterating over each column in the given array
      of strings and checking if the characters in that column are in lexicographic
      order. If not, we need to delete that column. We can use a greedy approach to
      solve this problem. We start by assuming that we do not need to delete any columns.
      Then, we iterate over each column and check if the characters in that column are
      in lexicographic order. If we find a column where the characters are not in lexicographic
      order, we increment our count of columns to delete. The key intuition here is
      that we only need to check each column once, because if a column is not in lexicographic
      order, deleting it will not affect the lexicographic order of the other columns.
    time_complexity: The time complexity of this solution is O(n*m) where n is the number
      of strings and m is the length of each string. This is because we are iterating
      over each character in each string once.
    space_complexity: The space complexity of this solution is O(1) because we are not
      using any additional space that scales with the input size.
    elapsed_time: 5.277040243148804
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-22 01:11:58 '
---

## Problem #960: Delete Columns to Make Sorted III

**Difficulty:** Hard

**Topics:** Array, String, Dynamic Programming

## Problem Description

<p>You are given an array of <code>n</code> strings <code>strs</code>, all of the same length.</p>

<p>We may choose any deletion indices, and we delete all the characters in those indices for each string.</p>

<p>For example, if we have <code>strs = [&quot;abcdef&quot;,&quot;uvwxyz&quot;]</code> and deletion indices <code>{0, 2, 3}</code>, then the final array after deletions is <code>[&quot;bef&quot;, &quot;vyz&quot;]</code>.</p>

<p>Suppose we chose a set of deletion indices <code>answer</code> such that after deletions, the final array has <strong>every string (row) in lexicographic</strong> order. (i.e., <code>(strs[0][0] &lt;= strs[0][1] &lt;= ... &lt;= strs[0][strs[0].length - 1])</code>, and <code>(strs[1][0] &lt;= strs[1][1] &lt;= ... &lt;= strs[1][strs[1].length - 1])</code>, and so on). Return <em>the minimum possible value of</em> <code>answer.length</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;babca&quot;,&quot;bbazb&quot;]
<strong>Output:</strong> 3
<strong>Explanation:</strong> After deleting columns 0, 1, and 4, the final array is strs = [&quot;bc&quot;, &quot;az&quot;].
Both these rows are individually in lexicographic order (ie. strs[0][0] &lt;= strs[0][1] and strs[1][0] &lt;= strs[1][1]).
Note that strs[0] &gt; strs[1] - the array strs is not necessarily in lexicographic order.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;edcba&quot;]
<strong>Output:</strong> 4
<strong>Explanation:</strong> If we delete less than 4 columns, the only row will not be lexicographically sorted.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;ghi&quot;,&quot;def&quot;,&quot;abc&quot;]
<strong>Output:</strong> 0
<strong>Explanation:</strong> All rows are already lexicographically sorted.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == strs.length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= strs[i].length &lt;= 100</code></li>
	<li><code>strs[i]</code> consists of lowercase English letters.</li>
</ul>

<ul>
	<li>&nbsp;</li>
</ul>


## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-22 01:11:53 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to find the minimum number of columns to delete such that the remaining characters in each row form a lexicographically sorted string. This is equivalent to finding the maximum number of columns we can *keep* such that they satisfy the sorting condition. Let `L` be the length of each string (number of columns) and `n` be the number of strings (rows). We are looking for a subsequence of column indices `c_1, c_2, ..., c_k` such that `0 <= c_1 < c_2 < ... < c_k < L`, and for every string `s` in `strs`, `s[c_i] <= s[c_{i+1}]` for all `1 <= i < k`. The minimum deletions will then be `L - k_max`, where `k_max` is the length of the longest such subsequence.
This problem can be solved using dynamic programming, similar to the Longest Increasing Subsequence (LIS) problem. We define `dp[i]` as the maximum length of a valid subsequence of columns ending at index `i`. To compute `dp[i]`, we iterate through all previous columns `j` (where `0 <= j < i`). If column `j` can precede column `i` in a valid subsequence (meaning `strs[row][j] <= strs[row][i]` for all rows `row`), then we can potentially extend the subsequence ending at `j` by including `i`. Thus, `dp[i]` is updated to `max(dp[i], dp[j] + 1)`. The base case is `dp[i] = 1` for all `i`, as any single column forms a valid subsequence. After filling the `dp` array, the maximum value in `dp` represents `k_max`, and the result is `L - k_max`.

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
    int minDeletionSize(std::vector<std::string>& strs) {
        int n = strs.size();
        int L = strs[0].length();

        std::vector<int> dp(L, 1);

        for (int i = 0; i < L; ++i) {
            for (int j = 0; j < i; ++j) {
                bool is_valid_pair = true;
                for (int row = 0; row < n; ++row) {
                    if (strs[row][j] > strs[row][i]) {
                        is_valid_pair = false;
                        break;
                    }
                }
                if (is_valid_pair) {
                    dp[i] = std::max(dp[i], dp[j] + 1);
                }
            }
        }

        int max_kept_columns = *std::max_element(dp.begin(), dp.end());

        return L - max_kept_columns;
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
    public int minDeletionSize(String[] strs) {
        int n = strs.length;
        int L = strs[0].length();

        int[] dp = new int[L];
        Arrays.fill(dp, 1);

        for (int i = 0; i < L; ++i) {
            for (int j = 0; j < i; ++j) {
                boolean isValidPair = true;
                for (int row = 0; row < n; ++row) {
                    if (strs[row].charAt(j) > strs[row].charAt(i)) {
                        isValidPair = false;
                        break;
                    }
                }
                if (isValidPair) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }

        int maxKeptColumns = 0;
        for (int val : dp) {
            maxKeptColumns = Math.max(maxKeptColumns, val);
        }

        return L - maxKeptColumns;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        L = len(strs[0])

        dp = [1] * L

        for i in range(L):
            for j in range(i):
                is_valid_pair = True
                for row in range(n):
                    if strs[row][j] > strs[row][i]:
                        is_valid_pair = False
                        break
                if is_valid_pair:
                    dp[i] = max(dp[i], dp[j] + 1)

        max_kept_columns = max(dp)

        return L - max_kept_columns
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        L = len(strs[0])

        dp = [1] * L

        for i in range(L):
            for j in range(i):
                is_valid_pair = True
                for row in range(n):
                    if strs[row][j] > strs[row][i]:
                        is_valid_pair = False
                        break
                if is_valid_pair:
                    dp[i] = max(dp[i], dp[j] + 1)

        max_kept_columns = max(dp)

        return L - max_kept_columns
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int findMax(int* arr, int size) {
    int maxVal = arr[0];
    for (int i = 1; i < size; ++i) {
        if (arr[i] > maxVal) {
            maxVal = arr[i];
        }
    }
    return maxVal;
}

int minDeletionSize(char** strs, int strsSize) {
    int n = strsSize;
    int L = strlen(strs[0]);

    int* dp = (int*)malloc(L * sizeof(int));
    for (int k = 0; k < L; ++k) {
        dp[k] = 1;
    }

    for (int i = 0; i < L; ++i) {
        for (int j = 0; j < i; ++j) {
            bool isValidPair = true;
            for (int row = 0; row < n; ++row) {
                if (strs[row][j] > strs[row][i]) {
                    isValidPair = false;
                    break;
                }
            }
            if (isValidPair) {
                dp[i] = (dp[i] > dp[j] + 1) ? dp[i] : (dp[j] + 1);
            }
        }
    }

    int maxKeptColumns = findMax(dp, L);

    free(dp);

    return L - maxKeptColumns;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Linq;

public class Solution {
    public int MinDeletionSize(string[] strs) {
        int n = strs.Length;
        int L = strs[0].Length;

        int[] dp = new int[L];
        for (int k = 0; k < L; k++) {
            dp[k] = 1;
        }

        for (int i = 0; i < L; ++i) {
            for (int j = 0; j < i; ++j) {
                bool isValidPair = true;
                for (int row = 0; row < n; ++row) {
                    if (strs[row][j] > strs[row][i]) {
                        isValidPair = false;
                        break;
                    }
                }
                if (isValidPair) {
                    dp[i] = Math.Max(dp[i], dp[j] + 1);
                }
            }
        }

        int maxKeptColumns = dp.Max();

        return L - maxKeptColumns;
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
 * @return {number}
 */
var minDeletionSize = function(strs) {
    const n = strs.length;
    const L = strs[0].length;

    const dp = new Array(L).fill(1);

    for (let i = 0; i < L; ++i) {
        for (let j = 0; j < i; ++j) {
            let isValidPair = true;
            for (let row = 0; row < n; ++row) {
                if (strs[row][j] > strs[row][i]) {
                    isValidPair = false;
                    break;
                }
            }
            if (isValidPair) {
                dp[i] = Math.max(dp[i], dp[j] + 1);
            }
        }
    }

    const maxKeptColumns = Math.max(...dp);

    return L - maxKeptColumns;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minDeletionSize(strs: string[]): number {
    const n = strs.length;
    const L = strs[0].length;

    const dp: number[] = new Array(L).fill(1);

    for (let i = 0; i < L; ++i) {
        for (let j = 0; j < i; ++j) {
            let isValidPair: boolean = true;
            for (let row = 0; row < n; ++row) {
                if (strs[row][j] > strs[row][i]) {
                    isValidPair = false;
                    break;
                }
            }
            if (isValidPair) {
                dp[i] = Math.max(dp[i], dp[j] + 1);
            }
        }

    }

    const maxKeptColumns: number = Math.max(...dp);

    return L - maxKeptColumns;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php
class Solution {

    /**
     * @param String[] $strs
     * @return Integer
     */
    function minDeletionSize($strs) {
        $n = count($strs);
        $L = strlen($strs[0]);

        $dp = array_fill(0, $L, 1);

        for ($i = 0; $i < $L; ++$i) {
            for ($j = 0; $j < $i; ++$j) {
                $isValidPair = true;
                for ($row = 0; $row < $n; ++$row) {
                    if ($strs[$row][$j] > $strs[$row][$i]) {
                        $isValidPair = false;
                        break;
                    }
                }
                if ($isValidPair) {
                    $dp[$i] = max($dp[$i], $dp[$j] + 1);
                }
            }
        }

        $maxKeptColumns = max($dp);

        return $L - $maxKeptColumns;
    }
}
?>
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
import Foundation

class Solution {
    func minDeletionSize(_ strs: [String]) -> Int {
        let n = strs.count
        let L = strs[0].count

        let charArrays: [[Character]] = strs.map { Array($0) }

        var dp = Array(repeating: 1, count: L)

        for i in 0..<L {
            for j in 0..<i {
                var isValidPair = true
                for row in 0..<n {
                    if charArrays[row][j] > charArrays[row][i] {
                        isValidPair = false
                        break
                    }
                }
                if isValidPair {
                    dp[i] = max(dp[i], dp[j] + 1)
                }
            }
        }

        let maxKeptColumns = dp.max()!

        return L - maxKeptColumns
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import kotlin.math.max

class Solution {
    fun minDeletionSize(strs: Array<String>): Int {
        val n = strs.size
        val L = strs[0].length;

        val dp = IntArray(L) { 1 }

        for (i in 0 until L) {
            for (j in 0 until i) {
                var isValidPair = true
                for (row in 0 until n) {
                    if (strs[row][j] > strs[row][i]) {
                        isValidPair = false
                        break
                    }
                }
                if (isValidPair) {
                    dp[i] = max(dp[i], dp[j] + 1)
                }
            }
        }

        val maxKeptColumns = dp.maxOrNull()!!

        return L - maxKeptColumns
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
  int minDeletionSize(List<String> strs) {
    int n = strs.length;
    int L = strs[0].length;

    List<int> dp = List<int>.filled(L, 1);

    for (int i = 0; i < L; ++i) {
      for (int j = 0; j < i; ++j) {
        bool isValidPair = true;
        for (int row = 0; row < n; ++row) {
          if (strs[row].codeUnitAt(j) > strs[row].codeUnitAt(i)) {
            isValidPair = false;
            break;
          }
        }
        if (isValidPair) {
          dp[i] = max(dp[i], dp[j] + 1);
        }
      }
    }

    int maxKeptColumns = dp.reduce(max);

    return L - maxKeptColumns;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

import (
	"math"
)

func minDeletionSize(strs []string) int {
    n := len(strs)
    L := len(strs[0])

    dp := make([]int, L)
    for i := range dp {
        dp[i] = 1
    }

    for i := 0; i < L; i++ {
        for j := 0; j < i; j++ {
            isValidPair := true
            for row := 0; row < n; row++ {
                if strs[row][j] > strs[row][i] {
                    isValidPair = false
                    break
                }
            }
            if isValidPair {
                dp[i] = int(math.Max(float64(dp[i]), float64(dp[j] + 1)))
            }
        }
    }

    maxKeptColumns := 0
    for _, val := range dp {
        maxKeptColumns = int(math.Max(float64(maxKeptColumns), float64(val)))
    }

    return L - maxKeptColumns
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String[]} strs
# @return {Integer}
def min_deletion_size(strs)
    n = strs.length
    L = strs[0].length

    dp = Array.new(L, 1)

    (0...L).each do |i|
        (0...i).each do |j|
            is_valid_pair = true
            (0...n).each do |row|
                if strs[row][j] > strs[row][i]
                    is_valid_pair = false
                    break
                end
            end
            if is_valid_pair
                dp[i] = [dp[i], dp[j] + 1].max
            end
        end
    end

    max_kept_columns = dp.max

    L - max_kept_columns
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.math.max

object Solution {
    def minDeletionSize(strs: Array[String]): Int = {
        val n = strs.length
        val L = strs(0).length

        val dp = Array.fill(L)(1)

        for (i <- 0 until L) {
            for (j <- 0 until i) {
                var isValidPair = true
                for (row <- 0 until n) {
                    if (strs(row)(j) > strs(row)(i)) {
                        isValidPair = false
                        break
                    }
                }
                if (isValidPair) {
                    dp(i) = max(dp(i), dp(j) + 1)
                }
            }
        }

        val maxKeptColumns = dp.max

        L - maxKeptColumns
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::cmp::max;

impl Solution {
    pub fn min_deletion_size(strs: Vec<String>) -> i32 {
        let n = strs.len();
        let l = strs[0].len();

        let mut dp = vec![1; l];

        for i in 0..l {
            for j in 0..i {
                let mut is_valid_pair = true;
                for row in 0..n {
                    let char_j = strs[row].as_bytes()[j];
                    let char_i = strs[row].as_bytes()[i];
                    if char_j > char_i {
                        is_valid_pair = false;
                        break;
                    }
                }
                if is_valid_pair {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
        }

        let max_kept_columns = *dp.iter().max().unwrap();

        (l - max_kept_columns) as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (min-deletion-size strs)
  (define n (length strs))
  (define L (string-length (car strs)))

  (define dp (make-vector L 1))

  (for ([i (in-range L)])
    (for ([j (in-range i)])
      (define is-valid-pair? #t)
      (for ([row (in-range n)])
        (when (> (string-ref (list-ref strs row) j)
                 (string-ref (list-ref strs row) i))
          (set! is-valid-pair? #f)
          (break)))
      (when is-valid-pair?
        (vector-set! dp i (max (vector-ref dp i) (+ (vector-ref dp j) 1))))))

  (define max-kept-columns (vector-ref dp 0))
  (for ([k (in-range 1 L)])
    (set! max-kept-columns (max max-kept-columns (vector-ref dp k))))

  (- L max-kept-columns))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([min_deletion_size/1]).

-include_lib("stdlib/include/array.hrl").

min_deletion_size(Strs) ->
    N = length(Strs),
    L = length(hd(Strs)),

    StrsAsTupleArray = array:from_list([list_to_tuple(S) || S <- Strs]),

    DpArray = array:new([{size, L}, {fixed, true}, {default, 1}]),

    DpFinal = lists:foldl(
        fun(I, CurrentDp) ->
            lists:foldl(
                fun(J, InnerDp) ->
                    IsValidPair = lists:all(
                        fun(RowIdx) ->
                            StringTuple = array:get(RowIdx, StrsAsTupleArray),
                            CharJ = element(J + 1, StringTuple),
                            CharI = element(I + 1, StringTuple),
                            CharJ =< CharI
                        end,
                        lists:seq(0, N - 1)
                    ),
                    if IsValidPair ->
                        array:set(I, max(array:get(I, InnerDp), array:get(J, InnerDp) + 1), InnerDp);
                    true ->
                        InnerDp
                    end
                end,
                CurrentDp,
                lists:seq(0, I - 1)
            )
        end,
        DpArray,
        lists:seq(0, L - 1)
    ),

    MaxKeptColumns = lists:foldl(fun(Val, Acc) -> max(Val, Acc) end, 0, array:to_list(DpFinal)),
    L - MaxKeptColumns.

max(A, B) when A >= B -> A;
max(A, B) -> B.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  def min_deletion_size(strs) do
    n = length(strs)
    l = String.length(hd(strs))

    strs_as_tuple_of_tuples =
      strs
      |> Enum.map(&String.to_charlist/1)
      |> Enum.map(&List.to_tuple/1)
      |> List.to_tuple

    dp_initial = List.duplicate(1, l) |> List.to_tuple

    dp_final = Enum.reduce(0..(l - 1), dp_initial, fn i, current_dp ->
      Enum.reduce(0..(i - 1), current_dp, fn j, inner_dp ->
        is_valid_pair = Enum.all?(0..(n - 1), fn row_idx ->
          string_tuple = elem(strs_as_tuple_of_tuples, row_idx)
          char_j = elem(string_tuple, j)
          char_i = elem(string_tuple, i)
          char_j <= char_i
        end)

        if is_valid_pair do
          Tuple.replace_at(inner_dp, i, max(elem(inner_dp, i), elem(inner_dp, j) + 1))
        else
          inner_dp
        end
      end)
    end)

    max_kept_columns = Enum.max(Tuple.to_list(dp_final))
    l - max_kept_columns
  end

  defp max(a, b) when a >= b, do: a
  defp max(a, b), do: b
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(L^2 * n), where `L` is the length of each string and `n` is the number of strings. This is derived from three nested loops: the outermost loop iterates `L` times (for `i`), the middle loop iterates up to `L` times (for `j`), and the innermost loop iterates `n` times (for `row`) to check the validity of a pair of columns. In some functional languages like Elixir, list/tuple updates or character access might incur an additional `O(L)` factor, leading to a worst-case complexity of O(L^2 * (n + L)). Given the constraints (L, n <= 100), this results in roughly 100^2 * 100 = 1,000,000 operations, which is efficient enough.

- **Space Complexity:** The space complexity is O(L) for storing the `dp` array. In languages like Swift, Erlang, or Elixir, converting strings to character arrays or tuples for efficient O(1) character access might require O(n * L) additional space for preprocessing the input strings. However, the core DP state itself only requires O(L) space.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-22 01:11:58 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by iterating over each column in the given array of strings and checking if the characters in that column are in lexicographic order. If not, we need to delete that column. We can use a greedy approach to solve this problem. We start by assuming that we do not need to delete any columns. Then, we iterate over each column and check if the characters in that column are in lexicographic order. If we find a column where the characters are not in lexicographic order, we increment our count of columns to delete. The key intuition here is that we only need to check each column once, because if a column is not in lexicographic order, deleting it will not affect the lexicographic order of the other columns.

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
    int minDeletionSize(vector<string>& strs) {
        int count = 0;
        int n = strs.size();
        int m = strs[0].size();
        for (int j = 0; j < m; j++) {
            for (int i = 1; i < n; i++) {
                if (strs[i - 1][j] > strs[i][j]) {
                    count++;
                    break;
                }
            }
        }
        return count;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minDeletionSize(String[] strs) {
        int count = 0;
        int n = strs.length;
        int m = strs[0].length();
        for (int j = 0; j < m; j++) {
            for (int i = 1; i < n; i++) {
                if (strs[i - 1].charAt(j) > strs[i].charAt(j)) {
                    count++;
                    break;
                }
            }
        }
        return count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        count = 0
        n = len(strs)
        m = len(strs[0])
        for j in range(m):
            for i in range(1, n):
                if strs[i - 1][j] > strs[i][j]:
                    count += 1
                    break
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        count = 0
        n = len(strs)
        m = len(strs[0])
        for j in range(m):
            for i in range(1, n):
                if strs[i - 1][j] > strs[i][j]:
                    count += 1
                    break
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int minDeletionSize(char ** strs, int strsSize) {
    int count = 0;
    int m = strlen(strs[0]);
    for (int j = 0; j < m; j++) {
        for (int i = 1; i < strsSize; i++) {
            if (strs[i - 1][j] > strs[i][j]) {
                count++;
                break;
            }
        }
    }
    return count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinDeletionSize(string[] strs) {
        int count = 0;
        int n = strs.Length;
        int m = strs[0].Length;
        for (int j = 0; j < m; j++) {
            for (int i = 1; i < n; i++) {
                if (strs[i - 1][j] > strs[i][j]) {
                    count++;
                    break;
                }
            }
        }
        return count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var minDeletionSize = function(strs) {
    let count = 0;
    let n = strs.length;
    let m = strs[0].length;
    for (let j = 0; j < m; j++) {
        for (let i = 1; i < n; i++) {
            if (strs[i - 1][j] > strs[i][j]) {
                count++;
                break;
            }
        }
    }
    return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minDeletionSize(strs: string[]): number {
    let count: number = 0;
    let n: number = strs.length;
    let m: number = strs[0].length;
    for (let j: number = 0; j < m; j++) {
        for (let i: number = 1; i < n; i++) {
            if (strs[i - 1][j] > strs[i][j]) {
                count++;
                break;
            }
        }
    }
    return count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function minDeletionSize($strs) {
        $count = 0;
        $n = count($strs);
        $m = strlen($strs[0]);
        for ($j = 0; $j < $m; $j++) {
            for ($i = 1; $i < $n; $i++) {
                if ($strs[$i - 1][$j] > $strs[$i][$j]) {
                    $count++;
                    break;
                }
            }
        }
        return $count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minDeletionSize(_ strs: [String]) -> Int {
        var count = 0
        let n = strs.count
        let m = strs[0].count
        for j in 0..<m {
            for i in 1..<n {
                if strs[i - 1][strs[i - 1].index(strs[i - 1].startIndex, offsetBy: j)] > strs[i][strs[i].index(strs[i].startIndex, offsetBy: j)] {
                    count += 1
                    break
                }
            }
        }
        return count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minDeletionSize(strs: Array<String>): Int {
        var count = 0
        val n = strs.size
        val m = strs[0].length
        for (j in 0 until m) {
            for (i in 1 until n) {
                if (strs[i - 1][j] > strs[i][j]) {
                    count++
                    break
                }
            }
        }
        return count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int minDeletionSize(List<String> strs) {
        int count = 0;
        int n = strs.length;
        int m = strs[0].length;
        for (int j = 0; j < m; j++) {
            for (int i = 1; i < n; i++) {
                if (strs[i - 1][j] > strs[i][j]) {
                    count++;
                    break;
                }
            }
        }
        return count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minDeletionSize(strs []string) int {
    count := 0
    n := len(strs)
    m := len(strs[0])
    for j := 0; j < m; j++ {
        for i := 1; i < n; i++ {
            if strs[i-1][j] > strs[i][j] {
                count++
                break
            }
        }
    }
    return count
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def min_deletion_size(strs)
    count = 0
    n = strs.size
    m = strs[0].size
    (0...m).each do |j|
        (1...n).each do |i|
            if strs[i - 1][j] > strs[i][j]
                count += 1
                break
            end
        end
    end
    count
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minDeletionSize(strs: Array[String]): Int = {
        var count = 0
        val n = strs.length
        val m = strs(0).length
        for (j <- 0 until m) {
            for (i <- 1 until n) {
                if (strs(i - 1)(j) > strs(i)(j)) {
                    count += 1
                    i
                }
            }
        }
        count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_deletion_size(strs: Vec<String>) -> i32 {
        let mut count = 0;
        let n = strs.len();
        let m = strs[0].len();
        for j in 0..m {
            for i in 1..n {
                if strs[i - 1].as_bytes()[j] > strs[i].as_bytes()[j] {
                    count += 1;
                    break;
                }
            }
        }
        count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
define (min-deletion-size strs)
    (let ((count 0)
          (n (length strs))
          (m (string-length (car strs))))
      (do ((j 0 (+ j 1)))
          ((= j m) count)
        (do ((i 1 (+ i 1)))
            ((= i n))
          (if (> (string-ref (list-ref strs (- i 1)) j) (string-ref (list-ref strs i) j))
              (begin
                (set! count (+ count 1))
                (set! i n)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
min_deletion_size(Strs) ->
    Count =
        lists:foldl(
          fun(J, {Count, N, M}) ->
                  lists:foldl(
                    fun(I, {Count, N, M}) ->
                            if
                                string:slice(string:part(Strs, I - 1), J + 1, 1) > string:slice(string:part(Strs, I), J + 1, 1) ->
                                    {Count + 1, N, M};
                                true ->
                                    {Count, N, M}
                            end
                    end,
                    {Count, N, M},
                    lists:seq(1, N - 1))
          end,
          {0, length(Strs), string:length(hd(Strs))},
          lists:seq(0, string:length(hd(Strs)) - 1)),
    Count.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
def min_deletion_size(strs) do
    count = 0
    n = length(strs)
    m = String.length(Enum.at(strs, 0))
    for j <- 0..m-1 do
        for i <- 1..n-1 do
            if String.at(Enum.at(strs, i-1), j) > String.at(Enum.at(strs, i), j) do
                count = count + 1
                break
            end
        end
    end
    count
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this solution is O(n*m) where n is the number of strings and m is the length of each string. This is because we are iterating over each character in each string once.

- **Space Complexity:** The space complexity of this solution is O(1) because we are not using any additional space that scales with the input size.

</div>
</details>
