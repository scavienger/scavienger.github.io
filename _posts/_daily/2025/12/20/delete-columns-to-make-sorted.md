---
layout: post
title: "Delete Columns to Make Sorted"
date: 2025-12-20 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "String"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/delete-columns-to-make-sorted/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minDeletionSize(std::vector<std::string>&\
        \ strs) {\n        if (strs.empty()) {\n            return 0;\n        }\n \
        \       int n = strs.size();\n        int m = strs[0].length();\n        int\
        \ deleted_columns = 0;\n\n        for (int j = 0; j < m; ++j) { // Iterate through\
        \ columns\n            for (int i = 0; i < n - 1; ++i) { // Iterate through\
        \ rows\n                if (strs[i][j] > strs[i+1][j]) {\n                 \
        \   deleted_columns++;\n                    break; // This column is not sorted,\
        \ move to the next column\n                }\n            }\n        }\n   \
        \     return deleted_columns;\n    }\n};"
      java: "class Solution {\n    public int minDeletionSize(String[] strs) {\n   \
        \     if (strs == null || strs.length == 0) {\n            return 0;\n     \
        \   }\n        int n = strs.length;\n        int m = strs[0].length();\n   \
        \     int deletedColumns = 0;\n\n        for (int j = 0; j < m; ++j) { // Iterate\
        \ through columns\n            for (int i = 0; i < n - 1; ++i) { // Iterate\
        \ through rows\n                if (strs[i].charAt(j) > strs[i+1].charAt(j))\
        \ {\n                    deletedColumns++;\n                    break; // This\
        \ column is not sorted, move to the next column\n                }\n       \
        \     }\n        }\n        return deletedColumns;\n    }\n}"
      python: "class Solution:\n    def minDeletionSize(self, strs: List[str]) -> int:\n\
        \        if not strs:\n            return 0\n\n        n = len(strs)\n     \
        \   m = len(strs[0])\n        deleted_columns = 0\n\n        for j in range(m):\
        \  # Iterate through columns\n            for i in range(n - 1):  # Iterate\
        \ through rows\n                if strs[i][j] > strs[i+1][j]:\n            \
        \        deleted_columns += 1\n                    break  # This column is not\
        \ sorted, move to the next column\n\n        return deleted_columns"
      python3: "class Solution:\n    def minDeletionSize(self, strs: List[str]) -> int:\n\
        \        if not strs:\n            return 0\n\n        n = len(strs)\n     \
        \   m = len(strs[0])\n        deleted_columns = 0\n\n        for j in range(m):\
        \  # Iterate through columns\n            for i in range(n - 1):  # Iterate\
        \ through rows\n                if strs[i][j] > strs[i+1][j]:\n            \
        \        deleted_columns += 1\n                    break  # This column is not\
        \ sorted, move to the next column\n\n        return deleted_columns"
      c: "#include <string.h>\n#include <stdlib.h>\n\nint minDeletionSize(char **strs,\
        \ int strsSize) {\n    if (strsSize == 0) {\n        return 0;\n    }\n    int\
        \ n = strsSize;\n    int m = strlen(strs[0]);\n    int deleted_columns = 0;\n\
        \n    for (int j = 0; j < m; ++j) { // Iterate through columns\n        for\
        \ (int i = 0; i < n - 1; ++i) { // Iterate through rows\n            if (strs[i][j]\
        \ > strs[i+1][j]) {\n                deleted_columns++;\n                break;\
        \ // This column is not sorted, move to the next column\n            }\n   \
        \     }\n    }\n    return deleted_columns;\n}"
      csharp: "public class Solution {\n    public int MinDeletionSize(string[] strs)\
        \ {\n        if (strs == null || strs.Length == 0) {\n            return 0;\n\
        \        }\n        int n = strs.Length;\n        int m = strs[0].Length;\n\
        \        int deletedColumns = 0;\n\n        for (int j = 0; j < m; ++j) { //\
        \ Iterate through columns\n            for (int i = 0; i < n - 1; ++i) { //\
        \ Iterate through rows\n                if (strs[i][j] > strs[i+1][j]) {\n \
        \                   deletedColumns++;\n                    break; // This column\
        \ is not sorted, move to the next column\n                }\n            }\n\
        \        }\n        return deletedColumns;\n    }\n}"
      javascript: "/**\n * @param {string[]} strs\n * @return {number}\n */\nvar minDeletionSize\
        \ = function(strs) {\n    if (!strs || strs.length === 0) {\n        return\
        \ 0;\n    }\n    let n = strs.length;\n    let m = strs[0].length;\n    let\
        \ deletedColumns = 0;\n\n    for (let j = 0; j < m; ++j) { // Iterate through\
        \ columns\n        for (let i = 0; i < n - 1; ++i) { // Iterate through rows\n\
        \            if (strs[i][j] > strs[i+1][j]) {\n                deletedColumns++;\n\
        \                break; // This column is not sorted, move to the next column\n\
        \            }\n        }\n    }\n    return deletedColumns;\n};"
      typescript: "function minDeletionSize(strs: string[]): number {\n    if (!strs\
        \ || strs.length === 0) {\n        return 0;\n    }\n    const n = strs.length;\n\
        \    const m = strs[0].length;\n    let deletedColumns = 0;\n\n    for (let\
        \ j = 0; j < m; ++j) { // Iterate through columns\n        for (let i = 0; i\
        \ < n - 1; ++i) { // Iterate through rows\n            if (strs[i][j] > strs[i+1][j])\
        \ {\n                deletedColumns++;\n                break; // This column\
        \ is not sorted, move to the next column\n            }\n        }\n    }\n\
        \    return deletedColumns;\n}"
      php: "class Solution {\n    /**\n     * @param String[] $strs\n     * @return\
        \ Integer\n     */\n    function minDeletionSize($strs) {\n        if (empty($strs))\
        \ {\n            return 0;\n        }\n        $n = count($strs);\n        $m\
        \ = strlen($strs[0]);\n        $deletedColumns = 0;\n\n        for ($j = 0;\
        \ $j < $m; ++$j) { // Iterate through columns\n            for ($i = 0; $i <\
        \ $n - 1; ++$i) { // Iterate through rows\n                if ($strs[$i][$j]\
        \ > $strs[$i+1][$j]) {\n                    $deletedColumns++;\n           \
        \         break; // This column is not sorted, move to the next column\n   \
        \             }\n            }\n        }\n        return $deletedColumns;\n\
        \    }\n}"
      swift: "class Solution {\n    func minDeletionSize(_ strs: [String]) -> Int {\n\
        \        guard !strs.isEmpty else {\n            return 0\n        }\n     \
        \   let n = strs.count\n        let m = strs[0].count\n        var deletedColumns\
        \ = 0\n\n        for j in 0..<m { // Iterate through columns\n            for\
        \ i in 0..<n-1 { // Iterate through rows\n                let char1 = strs[i][strs[i].index(strs[i].startIndex,\
        \ offsetBy: j)]\n                let char2 = strs[i+1][strs[i+1].index(strs[i+1].startIndex,\
        \ offsetBy: j)]\n                if char1 > char2 {\n                    deletedColumns\
        \ += 1\n                    break // This column is not sorted, move to the\
        \ next column\n                }\n            }\n        }\n        return deletedColumns\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun minDeletionSize(strs: Array<String>): Int {\n\
        \        if (strs.isEmpty()) {\n            return 0\n        }\n        val\
        \ n = strs.size\n        val m = strs[0].length\n        var deletedColumns\
        \ = 0\n\n        for (j in 0 until m) { // Iterate through columns\n       \
        \     for (i in 0 until n - 1) { // Iterate through rows\n                if\
        \ (strs[i][j] > strs[i+1][j]) {\n                    deletedColumns++\n    \
        \                break // This column is not sorted, move to the next column\n\
        \                }\n            }\n        }\n        return deletedColumns\n\
        \    }\n}"
      dart: "class Solution {\n  int minDeletionSize(List<String> strs) {\n    if (strs.isEmpty)\
        \ {\n      return 0;\n    }\n    int n = strs.length;\n    int m = strs[0].length;\n\
        \    int deletedColumns = 0;\n\n    for (int j = 0; j < m; ++j) { // Iterate\
        \ through columns\n      for (int i = 0; i < n - 1; ++i) { // Iterate through\
        \ rows\n        if (strs[i].codeUnitAt(j) > strs[i+1].codeUnitAt(j)) {\n   \
        \       deletedColumns++;\n          break; // This column is not sorted, move\
        \ to the next column\n        }\n      }\n    }\n    return deletedColumns;\n\
        \  }\n}"
      go: "func minDeletionSize(strs []string) int {\n    if len(strs) == 0 {\n    \
        \    return 0\n    }\n    n := len(strs)\n    m := len(strs[0])\n    deletedColumns\
        \ := 0\n\n    for j := 0; j < m; j++ { // Iterate through columns\n        for\
        \ i := 0; i < n - 1; i++ { // Iterate through rows\n            if strs[i][j]\
        \ > strs[i+1][j] {\n                deletedColumns++\n                break\
        \ // This column is not sorted, move to the next column\n            }\n   \
        \     }\n    }\n    return deletedColumns\n}"
      ruby: "def min_deletion_size(strs)\n    return 0 if strs.empty?\n\n    n = strs.length\n\
        \    m = strs[0].length\n    deleted_columns = 0\n\n    (0...m).each do |j|\
        \ # Iterate through columns\n        (0...n-1).each do |i| # Iterate through\
        \ rows\n            if strs[i][j] > strs[i+1][j]\n                deleted_columns\
        \ += 1\n                break # This column is not sorted, move to the next\
        \ column\n            end\n        end\n    end\n    deleted_columns\nend"
      scala: "object Solution {\n    def minDeletionSize(strs: Array[String]): Int =\
        \ {\n        if (strs.isEmpty) {\n            return 0\n        }\n        val\
        \ n = strs.length\n        val m = strs(0).length\n        var deletedColumns\
        \ = 0\n\n        for (j <- 0 until m) { // Iterate through columns\n       \
        \     for (i <- 0 until n - 1) { // Iterate through rows\n                if\
        \ (strs(i)(j) > strs(i+1)(j)) {\n                    deletedColumns += 1\n \
        \                   break // This column is not sorted, move to the next column\n\
        \                }\n            }\n        }\n        deletedColumns\n    }\n\
        }"
      rust: "impl Solution {\n    pub fn min_deletion_size(strs: Vec<String>) -> i32\
        \ {\n        if strs.is_empty() {\n            return 0;\n        }\n      \
        \  let n = strs.len();\n        let m = strs[0].len();\n        let mut deleted_columns\
        \ = 0;\n\n        for j in 0..m { // Iterate through columns\n            for\
        \ i in 0..n - 1 { // Iterate through rows\n                // Access characters\
        \ by byte index for ASCII strings\n                // strs[i].as_bytes()[j]\
        \ is safe because all strings have same length and are ASCII\n             \
        \   if strs[i].as_bytes()[j] > strs[i+1].as_bytes()[j] {\n                 \
        \   deleted_columns += 1;\n                    break; // This column is not\
        \ sorted, move to the next column\n                }\n            }\n      \
        \  }\n        deleted_columns\n    }\n}"
      racket: "#lang racket\n(define/contract (min-deletion-size strs)\n  (-> (listof\
        \ string?) integer?)\n  (if (empty? strs)\n      0\n      (let* ((n (length\
        \ strs))\n             (m (string-length (first strs)))\n             (deleted-columns\
        \ 0))\n        (for ([j (in-range m)])\n          (let loop ([i 0])\n      \
        \      (when (< i (- n 1))\n              (if (> (string-ref (list-ref strs\
        \ i) j)\n                     (string-ref (list-ref strs (+ i 1)) j))\n    \
        \              (set! deleted-columns (+ deleted-columns 1))\n              \
        \    (loop (+ i 1))))))\n        deleted-columns)))"
      erlang: "-spec min_deletion_size(Strs :: [string()]) -> integer().\nmin_deletion_size(Strs)\
        \ when is_list(Strs) ->\ncase Strs of\n[] -> 0;\n[H|_] ->\nN = length(Strs),\n\
        M = length(H),\nmin_deletion_size_loop(Strs, N, M, 0, 0)\nend.\n\nmin_deletion_size_loop(Strs,\
        \ N, M, J, DeletedColumns) when J < M ->\nIsColumnSorted = check_column_sorted(Strs,\
        \ N, J, 0),\nNewDeletedColumns = case IsColumnSorted of\n                true\
        \ -> DeletedColumns;\n                false -> DeletedColumns + 1\n        \
        \    end,\nmin_deletion_size_loop(Strs, N, M, J + 1, NewDeletedColumns);\nmin_deletion_size_loop(_Strs,\
        \ _N, _M, _J, DeletedColumns) ->\nDeletedColumns.\n\ncheck_column_sorted(Strs,\
        \ N, J, I) when I < N - 1 ->\nChar1 = element(J + 1, lists:nth(I + 1, Strs)),\
        \ %% Erlang strings are lists of chars, element access is 1-indexed\nChar2 =\
        \ element(J + 1, lists:nth(I + 2, Strs)),\nif\nChar1 > Char2 -> false;\ntrue\
        \ -> check_column_sorted(Strs, N, J, I + 1)\nend;\ncheck_column_sorted(_Strs,\
        \ _N, _J, _I) ->\ntrue."
      elixir: "defmodule Solution do\n  @spec min_deletion_size(strs :: [String.t])\
        \ :: integer()\n  def min_deletion_size(strs) do\n    if Enum.empty?(strs) do\n\
        \      0\n    else\n      n = Enum.count(strs)\n      m = String.length(hd(strs))\n\
        \      do_min_deletion_size(strs, n, m, 0, 0)\n    end\n  end\n\n  defp do_min_deletion_size(_strs,\
        \ _n, m, m, deleted_columns), do: deleted_columns\n  defp do_min_deletion_size(strs,\
        \ n, m, j, deleted_columns) do\n    is_column_sorted = check_column_sorted(strs,\
        \ n, j, 0)\n    new_deleted_columns = if is_column_sorted, do: deleted_columns,\
        \ else: deleted_columns + 1\n    do_min_deletion_size(strs, n, m, j + 1, new_deleted_columns)\n\
        \  end\n\n  defp check_column_sorted(_strs, n, _j, i) when i >= n - 1, do: true\n\
        \  defp check_column_sorted(strs, n, j, i) do\n    char1 = String.at(Enum.at(strs,\
        \ i), j)\n    char2 = String.at(Enum.at(strs, i + 1), j)\n    if char1 > char2\
        \ do\n      false\n    else\n      check_column_sorted(strs, n, j, i + 1)\n\
        \    end\n  end\nend"
    approach: The problem requires us to count the number of columns in a grid of strings
      that are not lexicographically sorted. We are given an array of `n` strings, all
      of the same length, say `m`. The core idea is to iterate through each column independently
      and check its sorted status. For each column, we examine the characters from top
      to bottom, comparing adjacent characters. If at any point a character is greater
      than the character immediately below it in the same column, then that column is
      considered unsorted.
    time_complexity: The time complexity is O(m * n), where `m` is the length of each
      string (number of columns) and `n` is the number of strings (number of rows).
      This is because we iterate through each of the `m` columns, and for each column,
      we iterate through `n-1` pairs of characters to check the sorted order. Each character
      comparison takes constant time.
    space_complexity: The space complexity is O(1). We only use a single integer variable
      to store the count of unsorted columns. No additional data structures are allocated
      that scale with the input size.
    elapsed_time: 37.56854248046875
    model: gemini-2.5-flash
    generated_at: '2025-12-20 01:03:55 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int minDeletionSize(vector<string>& strs)\
        \ {\n        int count = 0;\n        int n = strs.size();\n        int m = strs[0].size();\n\
        \        for (int j = 0; j < m; j++) {\n            for (int i = 1; i < n; i++)\
        \ {\n                if (strs[i][j] < strs[i-1][j]) {\n                    count++;\n\
        \                    break;\n                }\n            }\n        }\n \
        \       return count;\n    }\n};"
      java: "class Solution {\n    public int minDeletionSize(String[] strs) {\n   \
        \     int count = 0;\n        int n = strs.length;\n        int m = strs[0].length();\n\
        \        for (int j = 0; j < m; j++) {\n            for (int i = 1; i < n; i++)\
        \ {\n                if (strs[i].charAt(j) < strs[i-1].charAt(j)) {\n      \
        \              count++;\n                    break;\n                }\n   \
        \         }\n        }\n        return count;\n    }\n}"
      python: "class Solution:\n    def minDeletionSize(self, strs: list[str]) -> int:\n\
        \        count = 0\n        n = len(strs)\n        m = len(strs[0])\n      \
        \  for j in range(m):\n            for i in range(1, n):\n                if\
        \ strs[i][j] < strs[i-1][j]:\n                    count += 1\n             \
        \       break\n        return count"
      python3: "class Solution:\n    def minDeletionSize(self, strs: list[str]) -> int:\n\
        \        count = 0\n        n = len(strs)\n        m = len(strs[0])\n      \
        \  for j in range(m):\n            for i in range(1, n):\n                if\
        \ strs[i][j] < strs[i-1][j]:\n                    count += 1\n             \
        \       break\n        return count"
      c: "int minDeletionSize(char ** strs, int strsSize) {\n    int count = 0;\n  \
        \  int m = strlen(strs[0]);\n    for (int j = 0; j < m; j++) {\n        for\
        \ (int i = 1; i < strsSize; i++) {\n            if (strs[i][j] < strs[i-1][j])\
        \ {\n                count++;\n                break;\n            }\n     \
        \   }\n    }\n    return count;\n}"
      csharp: "public class Solution {\n    public int MinDeletionSize(string[] strs)\
        \ {\n        int count = 0;\n        int n = strs.Length;\n        int m = strs[0].Length;\n\
        \        for (int j = 0; j < m; j++) {\n            for (int i = 1; i < n; i++)\
        \ {\n                if (strs[i][j] < strs[i-1][j]) {\n                    count++;\n\
        \                    break;\n                }\n            }\n        }\n \
        \       return count;\n    }\n}"
      javascript: "var minDeletionSize = function(strs) {\n    let count = 0;\n    let\
        \ n = strs.length;\n    let m = strs[0].length;\n    for (let j = 0; j < m;\
        \ j++) {\n        for (let i = 1; i < n; i++) {\n            if (strs[i][j]\
        \ < strs[i-1][j]) {\n                count++;\n                break;\n    \
        \        }\n        }\n    }\n    return count;\n};"
      typescript: "function minDeletionSize(strs: string[]): number {\n    let count:\
        \ number = 0;\n    let n: number = strs.length;\n    let m: number = strs[0].length;\n\
        \    for (let j: number = 0; j < m; j++) {\n        for (let i: number = 1;\
        \ i < n; i++) {\n            if (strs[i][j] < strs[i-1][j]) {\n            \
        \    count++;\n                break;\n            }\n        }\n    }\n   \
        \ return count;\n}"
      php: "class Solution {\n    function minDeletionSize($strs) {\n        $count\
        \ = 0;\n        $n = count($strs);\n        $m = strlen($strs[0]);\n       \
        \ for ($j = 0; $j < $m; $j++) {\n            for ($i = 1; $i < $n; $i++) {\n\
        \                if ($strs[$i][$j] < $strs[$i-1][$j]) {\n                  \
        \  $count++;\n                    break;\n                }\n            }\n\
        \        }\n        return $count;\n    }\n}"
      swift: "class Solution {\n    func minDeletionSize(_ strs: [String]) -> Int {\n\
        \        var count = 0\n        let n = strs.count\n        let m = strs[0].count\n\
        \        for j in 0..<m {\n            for i in 1..<n {\n                if\
        \ strs[i][strs[i].index(strs[i].startIndex, offsetBy: j)] < strs[i-1][strs[i-1].index(strs[i-1].startIndex,\
        \ offsetBy: j)] {\n                    count += 1\n                    break\n\
        \                }\n            }\n        }\n        return count\n    }\n}"
      kotlin: "class Solution {\n    fun minDeletionSize(strs: Array<String>): Int {\n\
        \        var count = 0\n        val n = strs.size\n        val m = strs[0].length\n\
        \        for (j in 0 until m) {\n            for (i in 1 until n) {\n      \
        \          if (strs[i][j] < strs[i-1][j]) {\n                    count++\n \
        \                   break\n                }\n            }\n        }\n   \
        \     return count\n    }\n}"
      dart: "class Solution {\n    int minDeletionSize(List<String> strs) {\n      \
        \  int count = 0;\n        int n = strs.length;\n        int m = strs[0].length;\n\
        \        for (int j = 0; j < m; j++) {\n            for (int i = 1; i < n; i++)\
        \ {\n                if (strs[i][j] < strs[i-1][j]) {\n                    count++;\n\
        \                    break;\n                }\n            }\n        }\n \
        \       return count;\n    }\n}"
      go: "func minDeletionSize(strs []string) int {\n    count := 0\n    n := len(strs)\n\
        \    m := len(strs[0])\n    for j := 0; j < m; j++ {\n        for i := 1; i\
        \ < n; i++ {\n            if strs[i][j] < strs[i-1][j] {\n                count++\n\
        \                break\n            }\n        }\n    }\n    return count\n}"
      ruby: "def min_deletion_size(strs)\n    count = 0\n    n = strs.size\n    m =\
        \ strs[0].size\n    (0...m).each do |j|\n        (1...n).each do |i|\n     \
        \       if strs[i][j] < strs[i-1][j]\n                count += 1\n         \
        \       break\n            end\n        end\n    end\n    count\nend"
      scala: "object Solution {\n    def minDeletionSize(strs: Array[String]): Int =\
        \ {\n        var count = 0\n        val n = strs.length\n        val m = strs(0).length\n\
        \        for (j <- 0 until m) {\n            for (i <- 1 until n) {\n      \
        \          if (strs(i)(j) < strs(i-1)(j)) {\n                    count += 1\n\
        \                    i\n                }\n            }\n        }\n      \
        \  count\n    }\n}"
      rust: "impl Solution {\n    pub fn min_deletion_size(strs: Vec<String>) -> i32\
        \ {\n        let mut count = 0;\n        let n = strs.len();\n        let m\
        \ = strs[0].len();\n        for j in 0..m {\n            for i in 1..n {\n \
        \               if strs[i].as_bytes()[j] < strs[i-1].as_bytes()[j] {\n     \
        \               count += 1;\n                    break;\n                }\n\
        \            }\n        }\n        count\n    }\n}"
      racket: "define (min-deletion-size strs)\n    (let ((count 0)\n          (n (length\
        \ strs))\n          (m (string-length (car strs))))\n        (do ((j 0 (+ j\
        \ 1)))\n            ((= j m) count)\n            (do ((i 1 (+ i 1)))\n     \
        \           ((= i n))\n                (when (< (string-ref (list-ref strs i)\
        \ j) (string-ref (list-ref strs (- i 1)) j))\n                    (set! count\
        \ (+ count 1))\n                    (return))))))"
      erlang: "min_deletion_size(Strs) ->\n    length([J || J <- lists:seq(0, length(hd(Strs))\
        \ - 1),\n                 not lists:all(fun(I) ->\n                        \
        \            I == length(Strs) orelse\n                                    element(J\
        \ + 1, element(I, Strs)) >= element(J + 1, element(I - 1, Strs))\n         \
        \                   end,\n                            lists:seq(1, length(Strs)\
        \ - 1))])."
      elixir: "def min_deletion_size(strs) do\n    count = 0\n    n = length(strs)\n\
        \    m = String.length(hd(strs))\n    Enum.reduce(0..m-1, count, fn j, count\
        \ ->\n        if Enum.any?(1..n-1, fn i -> String.at(Enum.at(strs, i), j) <\
        \ String.at(Enum.at(strs, i-1), j) end) do\n            count + 1\n        else\n\
        \            count\n        end\n    end)\nend"
    approach: The algorithm works by iterating over each column in the grid of strings.
      For each column, it checks if the characters in that column are sorted lexicographically.
      If they are not, it increments a counter to keep track of the number of columns
      that need to be deleted. The key intuition here is that we can simply compare
      the characters in each column from top to bottom to determine if the column is
      sorted. This approach allows us to solve the problem in a straightforward and
      efficient manner. The algorithm iterates over each column and checks for sorted
      order, making it easy to implement and understand.
    time_complexity: The time complexity of this algorithm is O(n * m), where n is the
      number of strings and m is the length of each string. This is because we are iterating
      over each character in each string once, resulting in a linear time complexity
      with respect to the input size.
    space_complexity: The space complexity of this algorithm is O(1), as we are only
      using a constant amount of space to store the count of columns to be deleted.
      We do not need to store any additional data structures that scale with the input
      size, making the space complexity constant.
    elapsed_time: 5.290295600891113
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-20 01:04:00 '
---

## Problem #944: Delete Columns to Make Sorted

**Difficulty:** Easy

**Topics:** Array, String

## Problem Description

<p>You are given an array of <code>n</code> strings <code>strs</code>, all of the same length.</p>

<p>The strings can be arranged such that there is one on each line, making a grid.</p>

<ul>
	<li>For example, <code>strs = [&quot;abc&quot;, &quot;bce&quot;, &quot;cae&quot;]</code> can be arranged as follows:</li>
</ul>

<pre>
abc
bce
cae
</pre>

<p>You want to <strong>delete</strong> the columns that are <strong>not sorted lexicographically</strong>. In the above example (<strong>0-indexed</strong>), columns 0 (<code>&#39;a&#39;</code>, <code>&#39;b&#39;</code>, <code>&#39;c&#39;</code>) and 2 (<code>&#39;c&#39;</code>, <code>&#39;e&#39;</code>, <code>&#39;e&#39;</code>) are sorted, while column 1 (<code>&#39;b&#39;</code>, <code>&#39;c&#39;</code>, <code>&#39;a&#39;</code>) is not, so you would delete column 1.</p>

<p>Return <em>the number of columns that you will delete</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;cba&quot;,&quot;daf&quot;,&quot;ghi&quot;]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The grid looks as follows:
  cba
  daf
  ghi
Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;a&quot;,&quot;b&quot;]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The grid looks as follows:
  a
  b
Column 0 is the only column and is sorted, so you will not delete any columns.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;zyx&quot;,&quot;wvu&quot;,&quot;tsr&quot;]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The grid looks as follows:
  zyx
  wvu
  tsr
All 3 columns are not sorted, so you will delete all 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == strs.length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= strs[i].length &lt;= 1000</code></li>
	<li><code>strs[i]</code> consists of lowercase English letters.</li>
</ul>


## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-20 01:03:55 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem requires us to count the number of columns in a grid of strings that are not lexicographically sorted. We are given an array of `n` strings, all of the same length, say `m`. The core idea is to iterate through each column independently and check its sorted status. For each column, we examine the characters from top to bottom, comparing adjacent characters. If at any point a character is greater than the character immediately below it in the same column, then that column is considered unsorted.

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
        if (strs.empty()) {
            return 0;
        }
        int n = strs.size();
        int m = strs[0].length();
        int deleted_columns = 0;

        for (int j = 0; j < m; ++j) { // Iterate through columns
            for (int i = 0; i < n - 1; ++i) { // Iterate through rows
                if (strs[i][j] > strs[i+1][j]) {
                    deleted_columns++;
                    break; // This column is not sorted, move to the next column
                }
            }
        }
        return deleted_columns;
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
        if (strs == null || strs.length == 0) {
            return 0;
        }
        int n = strs.length;
        int m = strs[0].length();
        int deletedColumns = 0;

        for (int j = 0; j < m; ++j) { // Iterate through columns
            for (int i = 0; i < n - 1; ++i) { // Iterate through rows
                if (strs[i].charAt(j) > strs[i+1].charAt(j)) {
                    deletedColumns++;
                    break; // This column is not sorted, move to the next column
                }
            }
        }
        return deletedColumns;
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
        if not strs:
            return 0

        n = len(strs)
        m = len(strs[0])
        deleted_columns = 0

        for j in range(m):  # Iterate through columns
            for i in range(n - 1):  # Iterate through rows
                if strs[i][j] > strs[i+1][j]:
                    deleted_columns += 1
                    break  # This column is not sorted, move to the next column

        return deleted_columns
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if not strs:
            return 0

        n = len(strs)
        m = len(strs[0])
        deleted_columns = 0

        for j in range(m):  # Iterate through columns
            for i in range(n - 1):  # Iterate through rows
                if strs[i][j] > strs[i+1][j]:
                    deleted_columns += 1
                    break  # This column is not sorted, move to the next column

        return deleted_columns
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <string.h>
#include <stdlib.h>

int minDeletionSize(char **strs, int strsSize) {
    if (strsSize == 0) {
        return 0;
    }
    int n = strsSize;
    int m = strlen(strs[0]);
    int deleted_columns = 0;

    for (int j = 0; j < m; ++j) { // Iterate through columns
        for (int i = 0; i < n - 1; ++i) { // Iterate through rows
            if (strs[i][j] > strs[i+1][j]) {
                deleted_columns++;
                break; // This column is not sorted, move to the next column
            }
        }
    }
    return deleted_columns;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinDeletionSize(string[] strs) {
        if (strs == null || strs.Length == 0) {
            return 0;
        }
        int n = strs.Length;
        int m = strs[0].Length;
        int deletedColumns = 0;

        for (int j = 0; j < m; ++j) { // Iterate through columns
            for (int i = 0; i < n - 1; ++i) { // Iterate through rows
                if (strs[i][j] > strs[i+1][j]) {
                    deletedColumns++;
                    break; // This column is not sorted, move to the next column
                }
            }
        }
        return deletedColumns;
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
    if (!strs || strs.length === 0) {
        return 0;
    }
    let n = strs.length;
    let m = strs[0].length;
    let deletedColumns = 0;

    for (let j = 0; j < m; ++j) { // Iterate through columns
        for (let i = 0; i < n - 1; ++i) { // Iterate through rows
            if (strs[i][j] > strs[i+1][j]) {
                deletedColumns++;
                break; // This column is not sorted, move to the next column
            }
        }
    }
    return deletedColumns;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minDeletionSize(strs: string[]): number {
    if (!strs || strs.length === 0) {
        return 0;
    }
    const n = strs.length;
    const m = strs[0].length;
    let deletedColumns = 0;

    for (let j = 0; j < m; ++j) { // Iterate through columns
        for (let i = 0; i < n - 1; ++i) { // Iterate through rows
            if (strs[i][j] > strs[i+1][j]) {
                deletedColumns++;
                break; // This column is not sorted, move to the next column
            }
        }
    }
    return deletedColumns;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    /**
     * @param String[] $strs
     * @return Integer
     */
    function minDeletionSize($strs) {
        if (empty($strs)) {
            return 0;
        }
        $n = count($strs);
        $m = strlen($strs[0]);
        $deletedColumns = 0;

        for ($j = 0; $j < $m; ++$j) { // Iterate through columns
            for ($i = 0; $i < $n - 1; ++$i) { // Iterate through rows
                if ($strs[$i][$j] > $strs[$i+1][$j]) {
                    $deletedColumns++;
                    break; // This column is not sorted, move to the next column
                }
            }
        }
        return $deletedColumns;
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
        guard !strs.isEmpty else {
            return 0
        }
        let n = strs.count
        let m = strs[0].count
        var deletedColumns = 0

        for j in 0..<m { // Iterate through columns
            for i in 0..<n-1 { // Iterate through rows
                let char1 = strs[i][strs[i].index(strs[i].startIndex, offsetBy: j)]
                let char2 = strs[i+1][strs[i+1].index(strs[i+1].startIndex, offsetBy: j)]
                if char1 > char2 {
                    deletedColumns += 1
                    break // This column is not sorted, move to the next column
                }
            }
        }
        return deletedColumns
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
        if (strs.isEmpty()) {
            return 0
        }
        val n = strs.size
        val m = strs[0].length
        var deletedColumns = 0

        for (j in 0 until m) { // Iterate through columns
            for (i in 0 until n - 1) { // Iterate through rows
                if (strs[i][j] > strs[i+1][j]) {
                    deletedColumns++
                    break // This column is not sorted, move to the next column
                }
            }
        }
        return deletedColumns
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
    if (strs.isEmpty) {
      return 0;
    }
    int n = strs.length;
    int m = strs[0].length;
    int deletedColumns = 0;

    for (int j = 0; j < m; ++j) { // Iterate through columns
      for (int i = 0; i < n - 1; ++i) { // Iterate through rows
        if (strs[i].codeUnitAt(j) > strs[i+1].codeUnitAt(j)) {
          deletedColumns++;
          break; // This column is not sorted, move to the next column
        }
      }
    }
    return deletedColumns;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minDeletionSize(strs []string) int {
    if len(strs) == 0 {
        return 0
    }
    n := len(strs)
    m := len(strs[0])
    deletedColumns := 0

    for j := 0; j < m; j++ { // Iterate through columns
        for i := 0; i < n - 1; i++ { // Iterate through rows
            if strs[i][j] > strs[i+1][j] {
                deletedColumns++
                break // This column is not sorted, move to the next column
            }
        }
    }
    return deletedColumns
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def min_deletion_size(strs)
    return 0 if strs.empty?

    n = strs.length
    m = strs[0].length
    deleted_columns = 0

    (0...m).each do |j| # Iterate through columns
        (0...n-1).each do |i| # Iterate through rows
            if strs[i][j] > strs[i+1][j]
                deleted_columns += 1
                break # This column is not sorted, move to the next column
            end
        end
    end
    deleted_columns
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minDeletionSize(strs: Array[String]): Int = {
        if (strs.isEmpty) {
            return 0
        }
        val n = strs.length
        val m = strs(0).length
        var deletedColumns = 0

        for (j <- 0 until m) { // Iterate through columns
            for (i <- 0 until n - 1) { // Iterate through rows
                if (strs(i)(j) > strs(i+1)(j)) {
                    deletedColumns += 1
                    break // This column is not sorted, move to the next column
                }
            }
        }
        deletedColumns
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
        if strs.is_empty() {
            return 0;
        }
        let n = strs.len();
        let m = strs[0].len();
        let mut deleted_columns = 0;

        for j in 0..m { // Iterate through columns
            for i in 0..n - 1 { // Iterate through rows
                // Access characters by byte index for ASCII strings
                // strs[i].as_bytes()[j] is safe because all strings have same length and are ASCII
                if strs[i].as_bytes()[j] > strs[i+1].as_bytes()[j] {
                    deleted_columns += 1;
                    break; // This column is not sorted, move to the next column
                }
            }
        }
        deleted_columns
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket
(define/contract (min-deletion-size strs)
  (-> (listof string?) integer?)
  (if (empty? strs)
      0
      (let* ((n (length strs))
             (m (string-length (first strs)))
             (deleted-columns 0))
        (for ([j (in-range m)])
          (let loop ([i 0])
            (when (< i (- n 1))
              (if (> (string-ref (list-ref strs i) j)
                     (string-ref (list-ref strs (+ i 1)) j))
                  (set! deleted-columns (+ deleted-columns 1))
                  (loop (+ i 1))))))
        deleted-columns)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_deletion_size(Strs :: [string()]) -> integer().
min_deletion_size(Strs) when is_list(Strs) ->
case Strs of
[] -> 0;
[H|_] ->
N = length(Strs),
M = length(H),
min_deletion_size_loop(Strs, N, M, 0, 0)
end.

min_deletion_size_loop(Strs, N, M, J, DeletedColumns) when J < M ->
IsColumnSorted = check_column_sorted(Strs, N, J, 0),
NewDeletedColumns = case IsColumnSorted of
                true -> DeletedColumns;
                false -> DeletedColumns + 1
            end,
min_deletion_size_loop(Strs, N, M, J + 1, NewDeletedColumns);
min_deletion_size_loop(_Strs, _N, _M, _J, DeletedColumns) ->
DeletedColumns.

check_column_sorted(Strs, N, J, I) when I < N - 1 ->
Char1 = element(J + 1, lists:nth(I + 1, Strs)), %% Erlang strings are lists of chars, element access is 1-indexed
Char2 = element(J + 1, lists:nth(I + 2, Strs)),
if
Char1 > Char2 -> false;
true -> check_column_sorted(Strs, N, J, I + 1)
end;
check_column_sorted(_Strs, _N, _J, _I) ->
true.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_deletion_size(strs :: [String.t]) :: integer()
  def min_deletion_size(strs) do
    if Enum.empty?(strs) do
      0
    else
      n = Enum.count(strs)
      m = String.length(hd(strs))
      do_min_deletion_size(strs, n, m, 0, 0)
    end
  end

  defp do_min_deletion_size(_strs, _n, m, m, deleted_columns), do: deleted_columns
  defp do_min_deletion_size(strs, n, m, j, deleted_columns) do
    is_column_sorted = check_column_sorted(strs, n, j, 0)
    new_deleted_columns = if is_column_sorted, do: deleted_columns, else: deleted_columns + 1
    do_min_deletion_size(strs, n, m, j + 1, new_deleted_columns)
  end

  defp check_column_sorted(_strs, n, _j, i) when i >= n - 1, do: true
  defp check_column_sorted(strs, n, j, i) do
    char1 = String.at(Enum.at(strs, i), j)
    char2 = String.at(Enum.at(strs, i + 1), j)
    if char1 > char2 do
      false
    else
      check_column_sorted(strs, n, j, i + 1)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(m * n), where `m` is the length of each string (number of columns) and `n` is the number of strings (number of rows). This is because we iterate through each of the `m` columns, and for each column, we iterate through `n-1` pairs of characters to check the sorted order. Each character comparison takes constant time.

- **Space Complexity:** The space complexity is O(1). We only use a single integer variable to store the count of unsorted columns. No additional data structures are allocated that scale with the input size.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-20 01:04:00 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The algorithm works by iterating over each column in the grid of strings. For each column, it checks if the characters in that column are sorted lexicographically. If they are not, it increments a counter to keep track of the number of columns that need to be deleted. The key intuition here is that we can simply compare the characters in each column from top to bottom to determine if the column is sorted. This approach allows us to solve the problem in a straightforward and efficient manner. The algorithm iterates over each column and checks for sorted order, making it easy to implement and understand.

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
                if (strs[i][j] < strs[i-1][j]) {
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
                if (strs[i].charAt(j) < strs[i-1].charAt(j)) {
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
                if strs[i][j] < strs[i-1][j]:
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
                if strs[i][j] < strs[i-1][j]:
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
            if (strs[i][j] < strs[i-1][j]) {
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
                if (strs[i][j] < strs[i-1][j]) {
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
            if (strs[i][j] < strs[i-1][j]) {
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
            if (strs[i][j] < strs[i-1][j]) {
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
                if ($strs[$i][$j] < $strs[$i-1][$j]) {
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
                if strs[i][strs[i].index(strs[i].startIndex, offsetBy: j)] < strs[i-1][strs[i-1].index(strs[i-1].startIndex, offsetBy: j)] {
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
                if (strs[i][j] < strs[i-1][j]) {
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
                if (strs[i][j] < strs[i-1][j]) {
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
            if strs[i][j] < strs[i-1][j] {
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
            if strs[i][j] < strs[i-1][j]
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
                if (strs(i)(j) < strs(i-1)(j)) {
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
                if strs[i].as_bytes()[j] < strs[i-1].as_bytes()[j] {
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
                (when (< (string-ref (list-ref strs i) j) (string-ref (list-ref strs (- i 1)) j))
                    (set! count (+ count 1))
                    (return))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
min_deletion_size(Strs) ->
    length([J || J <- lists:seq(0, length(hd(Strs)) - 1),
                 not lists:all(fun(I) ->
                                    I == length(Strs) orelse
                                    element(J + 1, element(I, Strs)) >= element(J + 1, element(I - 1, Strs))
                            end,
                            lists:seq(1, length(Strs) - 1))]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
def min_deletion_size(strs) do
    count = 0
    n = length(strs)
    m = String.length(hd(strs))
    Enum.reduce(0..m-1, count, fn j, count ->
        if Enum.any?(1..n-1, fn i -> String.at(Enum.at(strs, i), j) < String.at(Enum.at(strs, i-1), j) end) do
            count + 1
        else
            count
        end
    end)
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this algorithm is O(n * m), where n is the number of strings and m is the length of each string. This is because we are iterating over each character in each string once, resulting in a linear time complexity with respect to the input size.

- **Space Complexity:** The space complexity of this algorithm is O(1), as we are only using a constant amount of space to store the count of columns to be deleted. We do not need to store any additional data structures that scale with the input size, making the space complexity constant.

</div>
</details>
