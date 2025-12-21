---
layout: post
title: "Delete Columns to Make Sorted II"
date: 2025-12-21 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "String", "Greedy"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/delete-columns-to-make-sorted-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minDeletionSize(std::vector<std::string>&\
        \ strs) {\n        int n = strs.size();\n        if (n <= 1) {\n           \
        \ return 0;\n        }\n        int L = strs[0].length();\n        int deleted_columns\
        \ = 0;\n        std::vector<bool> is_sorted(n - 1, false);\n\n        for (int\
        \ j = 0; j < L; ++j) { // Iterate through columns\n            bool should_delete_current_column\
        \ = false;\n            for (int i = 0; i < n - 1; ++i) { // Iterate through\
        \ adjacent string pairs\n                if (is_sorted[i]) {\n             \
        \       continue; // This pair is already strictly sorted\n                }\n\
        \                if (strs[i][j] > strs[i+1][j]) {\n                    should_delete_current_column\
        \ = true;\n                    deleted_columns++;\n                    break;\
        \ // Found a violation, must delete this column\n                }\n       \
        \     }\n\n            if (!should_delete_current_column) { // If we decided\
        \ to keep this column\n                for (int i = 0; i < n - 1; ++i) {\n \
        \                   if (!is_sorted[i] && strs[i][j] < strs[i+1][j]) {\n    \
        \                    is_sorted[i] = true; // This pair is now strictly sorted\n\
        \                    }\n                }\n            }\n        }\n\n    \
        \    return deleted_columns;\n    }\n};"
      java: "class Solution {\n    public int minDeletionSize(String[] strs) {\n   \
        \     int n = strs.length;\n        if (n <= 1) {\n            return 0;\n \
        \       }\n        int L = strs[0].length();\n        int deletedColumns = 0;\n\
        \        boolean[] isSorted = new boolean[n - 1];\n\n        for (int j = 0;\
        \ j < L; j++) { // Iterate through columns\n            boolean shouldDeleteCurrentColumn\
        \ = false;\n            for (int i = 0; i < n - 1; i++) { // Iterate through\
        \ adjacent string pairs\n                if (isSorted[i]) {\n              \
        \      continue; // This pair is already strictly sorted\n                }\n\
        \                if (strs[i].charAt(j) > strs[i+1].charAt(j)) {\n          \
        \          shouldDeleteCurrentColumn = true;\n                    deletedColumns++;\n\
        \                    break; // Found a violation, must delete this column\n\
        \                }\n            }\n\n            if (!shouldDeleteCurrentColumn)\
        \ { // If we decided to keep this column\n                for (int i = 0; i\
        \ < n - 1; i++) {\n                    if (!isSorted[i] && strs[i].charAt(j)\
        \ < strs[i+1].charAt(j)) {\n                        isSorted[i] = true; // This\
        \ pair is now strictly sorted\n                    }\n                }\n  \
        \          }\n        }\n\n        return deletedColumns;\n    }\n}"
      python: "class Solution:\n    def minDeletionSize(self, strs: List[str]) -> int:\n\
        \        n = len(strs)\n        if n <= 1:\n            return 0\n        L\
        \ = len(strs[0])\n        deleted_columns = 0\n        is_sorted = [False] *\
        \ (n - 1)\n\n        for j in range(L):  # Iterate through columns\n       \
        \     should_delete_current_column = False\n            for i in range(n - 1):\
        \  # Iterate through adjacent string pairs\n                if is_sorted[i]:\n\
        \                    continue  # This pair is already strictly sorted\n    \
        \            if strs[i][j] > strs[i+1][j]:\n                    should_delete_current_column\
        \ = True\n                    deleted_columns += 1\n                    break\
        \  # Found a violation, must delete this column\n\n            if not should_delete_current_column:\
        \  # If we decided to keep this column\n                for i in range(n - 1):\n\
        \                    if not is_sorted[i] and strs[i][j] < strs[i+1][j]:\n  \
        \                      is_sorted[i] = True  # This pair is now strictly sorted\n\
        \n        return deleted_columns"
      python3: "class Solution:\n    def minDeletionSize(self, strs: List[str]) -> int:\n\
        \        n = len(strs)\n        if n <= 1:\n            return 0\n        L\
        \ = len(strs[0])\n        deleted_columns = 0\n        is_sorted = [False] *\
        \ (n - 1)\n\n        for j in range(L):  # Iterate through columns\n       \
        \     should_delete_current_column = False\n            for i in range(n - 1):\
        \  # Iterate through adjacent string pairs\n                if is_sorted[i]:\n\
        \                    continue  # This pair is already strictly sorted\n    \
        \            if strs[i][j] > strs[i+1][j]:\n                    should_delete_current_column\
        \ = True\n                    deleted_columns += 1\n                    break\
        \  # Found a violation, must delete this column\n\n            if not should_delete_current_column:\
        \  # If we decided to keep this column\n                for i in range(n - 1):\n\
        \                    if not is_sorted[i] and strs[i][j] < strs[i+1][j]:\n  \
        \                      is_sorted[i] = True  # This pair is now strictly sorted\n\
        \n        return deleted_columns"
      c: "#include <stdlib.h>\n#include <stdbool.h>\n#include <string.h>\n\nint minDeletionSize(char\
        \ **strs, int strsSize) {\n    if (strsSize <= 1) {\n        return 0;\n   \
        \ }\n    int L = strlen(strs[0]);\n    int deleted_columns = 0;\n    bool *is_sorted\
        \ = (bool *)calloc(strsSize - 1, sizeof(bool));\n\n    for (int j = 0; j < L;\
        \ ++j) { // Iterate through columns\n        bool should_delete_current_column\
        \ = false;\n        for (int i = 0; i < strsSize - 1; ++i) { // Iterate through\
        \ adjacent string pairs\n            if (is_sorted[i]) {\n                continue;\
        \ // This pair is already strictly sorted\n            }\n            if (strs[i][j]\
        \ > strs[i+1][j]) {\n                should_delete_current_column = true;\n\
        \                deleted_columns++;\n                break; // Found a violation,\
        \ must delete this column\n            }\n        }\n\n        if (!should_delete_current_column)\
        \ { // If we decided to keep this column\n            for (int i = 0; i < strsSize\
        \ - 1; ++i) {\n                if (!is_sorted[i] && strs[i][j] < strs[i+1][j])\
        \ {\n                    is_sorted[i] = true; // This pair is now strictly sorted\n\
        \                }\n            }\n        }\n    }\n\n    free(is_sorted);\n\
        \    return deleted_columns;\n}"
      csharp: "public class Solution {\n    public int MinDeletionSize(string[] strs)\
        \ {\n        int n = strs.Length;\n        if (n <= 1) {\n            return\
        \ 0;\n        }\n        int L = strs[0].Length;\n        int deletedColumns\
        \ = 0;\n        bool[] isSorted = new bool[n - 1];\n\n        for (int j = 0;\
        \ j < L; j++) { // Iterate through columns\n            bool shouldDeleteCurrentColumn\
        \ = false;\n            for (int i = 0; i < n - 1; i++) { // Iterate through\
        \ adjacent string pairs\n                if (isSorted[i]) {\n              \
        \      continue; // This pair is already strictly sorted\n                }\n\
        \                if (strs[i][j] > strs[i+1][j]) {\n                    shouldDeleteCurrentColumn\
        \ = true;\n                    deletedColumns++;\n                    break;\
        \ // Found a violation, must delete this column\n                }\n       \
        \     }\n\n            if (!shouldDeleteCurrentColumn) { // If we decided to\
        \ keep this column\n                for (int i = 0; i < n - 1; i++) {\n    \
        \                if (!isSorted[i] && strs[i][j] < strs[i+1][j]) {\n        \
        \                isSorted[i] = true; // This pair is now strictly sorted\n \
        \                   }\n                }\n            }\n        }\n\n     \
        \   return deletedColumns;\n    }\n}"
      javascript: "/**\n * @param {string[]} strs\n * @return {number}\n */\nvar minDeletionSize\
        \ = function(strs) {\n    let n = strs.length;\n    if (n <= 1) {\n        return\
        \ 0;\n    }\n    let L = strs[0].length;\n    let deletedColumns = 0;\n    let\
        \ isSorted = new Array(n - 1).fill(false);\n\n    for (let j = 0; j < L; j++)\
        \ { // Iterate through columns\n        let shouldDeleteCurrentColumn = false;\n\
        \        for (let i = 0; i < n - 1; i++) { // Iterate through adjacent string\
        \ pairs\n            if (isSorted[i]) {\n                continue; // This pair\
        \ is already strictly sorted\n            }\n            if (strs[i][j] > strs[i+1][j])\
        \ {\n                shouldDeleteCurrentColumn = true;\n                deletedColumns++;\n\
        \                break; // Found a violation, must delete this column\n    \
        \        }\n        }\n\n        if (!shouldDeleteCurrentColumn) { // If we\
        \ decided to keep this column\n            for (let i = 0; i < n - 1; i++) {\n\
        \                if (!isSorted[i] && strs[i][j] < strs[i+1][j]) {\n        \
        \            isSorted[i] = true; // This pair is now strictly sorted\n     \
        \           }\n            }\n        }\n    }\n\n    return deletedColumns;\n\
        };"
      typescript: "function minDeletionSize(strs: string[]): number {\n    let n = strs.length;\n\
        \    if (n <= 1) {\n        return 0;\n    }\n    let L = strs[0].length;\n\
        \    let deletedColumns = 0;\n    let isSorted: boolean[] = new Array(n - 1).fill(false);\n\
        \n    for (let j = 0; j < L; j++) { // Iterate through columns\n        let\
        \ shouldDeleteCurrentColumn = false;\n        for (let i = 0; i < n - 1; i++)\
        \ { // Iterate through adjacent string pairs\n            if (isSorted[i]) {\n\
        \                continue; // This pair is already strictly sorted\n       \
        \     }\n            if (strs[i][j] > strs[i+1][j]) {\n                shouldDeleteCurrentColumn\
        \ = true;\n                deletedColumns++;\n                break; // Found\
        \ a violation, must delete this column\n            }\n        }\n\n       \
        \ if (!shouldDeleteCurrentColumn) { // If we decided to keep this column\n \
        \           for (let i = 0; i < n - 1; i++) {\n                if (!isSorted[i]\
        \ && strs[i][j] < strs[i+1][j]) {\n                    isSorted[i] = true; //\
        \ This pair is now strictly sorted\n                }\n            }\n     \
        \   }\n    }\n\n    return deletedColumns;\n};"
      php: "class Solution {\n    /**\n     * @param String[] $strs\n     * @return\
        \ Integer\n     */\n    function minDeletionSize($strs) {\n        $n = count($strs);\n\
        \        if ($n <= 1) {\n            return 0;\n        }\n        $L = strlen($strs[0]);\n\
        \        $deletedColumns = 0;\n        $isSorted = array_fill(0, $n - 1, false);\n\
        \n        for ($j = 0; $j < $L; $j++) { // Iterate through columns\n       \
        \     $shouldDeleteCurrentColumn = false;\n            for ($i = 0; $i < $n\
        \ - 1; $i++) { // Iterate through adjacent string pairs\n                if\
        \ ($isSorted[$i]) {\n                    continue; // This pair is already strictly\
        \ sorted\n                }\n                if ($strs[$i][$j] > $strs[$i+1][$j])\
        \ {\n                    $shouldDeleteCurrentColumn = true;\n              \
        \      $deletedColumns++;\n                    break; // Found a violation,\
        \ must delete this column\n                }\n            }\n\n            if\
        \ (!$shouldDeleteCurrentColumn) { // If we decided to keep this column\n   \
        \             for ($i = 0; $i < $n - 1; $i++) {\n                    if (!$isSorted[$i]\
        \ && $strs[$i][$j] < $strs[$i+1][$j]) {\n                        $isSorted[$i]\
        \ = true; // This pair is now strictly sorted\n                    }\n     \
        \           }\n            }\n        }\n\n        return $deletedColumns;\n\
        \    }\n}"
      swift: "class Solution {\n    func minDeletionSize(_ strs: [String]) -> Int {\n\
        \        let n = strs.count\n        if n <= 1 {\n            return 0\n   \
        \     }\n        let L = strs[0].count\n        var deletedColumns = 0\n   \
        \     var isSorted = Array(repeating: false, count: n - 1)\n\n        let strChars\
        \ = strs.map { Array($0) }\n\n        for j in 0..<L { // Iterate through columns\n\
        \            var shouldDeleteCurrentColumn = false\n            for i in 0..<n\
        \ - 1 { // Iterate through adjacent string pairs\n                if isSorted[i]\
        \ {\n                    continue // This pair is already strictly sorted\n\
        \                }\n                if strChars[i][j] > strChars[i+1][j] {\n\
        \                    shouldDeleteCurrentColumn = true\n                    deletedColumns\
        \ += 1\n                    break // Found a violation, must delete this column\n\
        \                }\n            }\n\n            if !shouldDeleteCurrentColumn\
        \ { // If we decided to keep this column\n                for i in 0..<n - 1\
        \ {\n                    if !isSorted[i] && strChars[i][j] < strChars[i+1][j]\
        \ {\n                        isSorted[i] = true // This pair is now strictly\
        \ sorted\n                    }\n                }\n            }\n        }\n\
        \n        return deletedColumns\n    }\n}"
      kotlin: "class Solution {\n    fun minDeletionSize(strs: Array<String>): Int {\n\
        \        val n = strs.size\n        if (n <= 1) {\n            return 0\n  \
        \      }\n        val L = strs[0].length\n        var deletedColumns = 0\n \
        \       val isSorted = BooleanArray(n - 1) { false }\n\n        for (j in 0\
        \ until L) { // Iterate through columns\n            var shouldDeleteCurrentColumn\
        \ = false\n            for (i in 0 until n - 1) { // Iterate through adjacent\
        \ string pairs\n                if (isSorted[i]) {\n                    continue\
        \ // This pair is already strictly sorted\n                }\n             \
        \   if (strs[i][j] > strs[i+1][j]) {\n                    shouldDeleteCurrentColumn\
        \ = true\n                    deletedColumns++\n                    break //\
        \ Found a violation, must delete this column\n                }\n          \
        \  }\n\n            if (!shouldDeleteCurrentColumn) { // If we decided to keep\
        \ this column\n                for (i in 0 until n - 1) {\n                \
        \    if (!isSorted[i] && strs[i][j] < strs[i+1][j]) {\n                    \
        \    isSorted[i] = true // This pair is now strictly sorted\n              \
        \      }\n                }\n            }\n        }\n\n        return deletedColumns\n\
        \    }\n}"
      dart: "class Solution {\n  int minDeletionSize(List<String> strs) {\n    int n\
        \ = strs.length;\n    if (n <= 1) {\n      return 0;\n    }\n    int L = strs[0].length;\n\
        \    int deletedColumns = 0;\n    List<bool> isSorted = List.filled(n - 1, false);\n\
        \n    for (int j = 0; j < L; j++) { // Iterate through columns\n      bool shouldDeleteCurrentColumn\
        \ = false;\n      for (int i = 0; i < n - 1; i++) { // Iterate through adjacent\
        \ string pairs\n        if (isSorted[i]) {\n          continue; // This pair\
        \ is already strictly sorted\n        }\n        if (strs[i].codeUnitAt(j) >\
        \ strs[i+1].codeUnitAt(j)) {\n          shouldDeleteCurrentColumn = true;\n\
        \          deletedColumns++;\n          break; // Found a violation, must delete\
        \ this column\n        }\n      }\n\n      if (!shouldDeleteCurrentColumn) {\
        \ // If we decided to keep this column\n        for (int i = 0; i < n - 1; i++)\
        \ {\n          if (!isSorted[i] && strs[i].codeUnitAt(j) < strs[i+1].codeUnitAt(j))\
        \ {\n            isSorted[i] = true; // This pair is now strictly sorted\n \
        \         }\n        }\n      }\n    }\n\n    return deletedColumns;\n  }\n}"
      go: "func minDeletionSize(strs []string) int {\n    n := len(strs)\n    if n <=\
        \ 1 {\n        return 0\n    }\n    L := len(strs[0])\n    deletedColumns :=\
        \ 0\n    isSorted := make([]bool, n-1)\n\n    for j := 0; j < L; j++ { // Iterate\
        \ through columns\n        shouldDeleteCurrentColumn := false\n        for i\
        \ := 0; i < n-1; i++ { // Iterate through adjacent string pairs\n          \
        \  if isSorted[i] {\n                continue // This pair is already strictly\
        \ sorted\n            }\n            if strs[i][j] > strs[i+1][j] {\n      \
        \          shouldDeleteCurrentColumn = true\n                deletedColumns++\n\
        \                break // Found a violation, must delete this column\n     \
        \       }\n        }\n\n        if !shouldDeleteCurrentColumn { // If we decided\
        \ to keep this column\n            for i := 0; i < n-1; i++ {\n            \
        \    if !isSorted[i] && strs[i][j] < strs[i+1][j] {\n                    isSorted[i]\
        \ = true // This pair is now strictly sorted\n                }\n          \
        \  }\n        }\n    }\n\n    return deletedColumns\n}"
      ruby: "def min_deletion_size(strs)\n    n = strs.length\n    return 0 if n <=\
        \ 1\n    L = strs[0].length\n    deleted_columns = 0\n    is_sorted = Array.new(n\
        \ - 1, false)\n\n    (0...L).each do |j| # Iterate through columns\n       \
        \ should_delete_current_column = false\n        (0...n - 1).each do |i| # Iterate\
        \ through adjacent string pairs\n            if is_sorted[i]\n             \
        \   next # This pair is already strictly sorted\n            end\n         \
        \   if strs[i][j] > strs[i+1][j]\n                should_delete_current_column\
        \ = true\n                deleted_columns += 1\n                break # Found\
        \ a violation, must delete this column\n            end\n        end\n\n   \
        \     unless should_delete_current_column # If we decided to keep this column\n\
        \            (0...n - 1).each do |i|\n                if !is_sorted[i] && strs[i][j]\
        \ < strs[i+1][j]\n                    is_sorted[i] = true # This pair is now\
        \ strictly sorted\n                end\n            end\n        end\n    end\n\
        \n    deleted_columns\nend"
      scala: "object Solution {\n    def minDeletionSize(strs: Array[String]): Int =\
        \ {\n        val n = strs.length\n        if (n <= 1) {\n            return\
        \ 0\n        }\n        val L = strs(0).length\n        var deletedColumns =\
        \ 0\n        val isSorted = Array.fill(n - 1)(false)\n\n        for (j <- 0\
        \ until L) { // Iterate through columns\n            var shouldDeleteCurrentColumn\
        \ = false\n            for (i <- 0 until n - 1) { // Iterate through adjacent\
        \ string pairs\n                if (isSorted(i)) {\n                    // This\
        \ pair is already strictly sorted\n                } else if (strs(i)(j) > strs(i+1)(j))\
        \ {\n                    shouldDeleteCurrentColumn = true\n                \
        \    deletedColumns += 1\n                    break // Found a violation, must\
        \ delete this column\n                }\n            }\n\n            if (!shouldDeleteCurrentColumn)\
        \ { // If we decided to keep this column\n                for (i <- 0 until\
        \ n - 1) {\n                    if (!isSorted(i) && strs(i)(j) < strs(i+1)(j))\
        \ {\n                        isSorted(i) = true // This pair is now strictly\
        \ sorted\n                    }\n                }\n            }\n        }\n\
        \n        deletedColumns\n    }\n}"
      rust: "impl Solution {\n    pub fn min_deletion_size(strs: Vec<String>) -> i32\
        \ {\n        let n = strs.len();\n        if n <= 1 {\n            return 0;\n\
        \        }\n        let L = strs[0].len();\n        let mut deleted_columns\
        \ = 0;\n        let mut is_sorted = vec![false; n - 1];\n\n        // Convert\
        \ strings to vectors of chars for easier indexing\n        let str_chars: Vec<Vec<char>>\
        \ = strs.iter().map(|s| s.chars().collect()).collect();\n\n        for j in\
        \ 0..L { // Iterate through columns\n            let mut should_delete_current_column\
        \ = false;\n            for i in 0..n - 1 { // Iterate through adjacent string\
        \ pairs\n                if is_sorted[i] {\n                    continue; //\
        \ This pair is already strictly sorted\n                }\n                if\
        \ str_chars[i][j] > str_chars[i+1][j] {\n                    should_delete_current_column\
        \ = true;\n                    deleted_columns += 1;\n                    break;\
        \ // Found a violation, must delete this column\n                }\n       \
        \     }\n\n            if !should_delete_current_column { // If we decided to\
        \ keep this column\n                for i in 0..n - 1 {\n                  \
        \  if !is_sorted[i] && str_chars[i][j] < str_chars[i+1][j] {\n             \
        \           is_sorted[i] = true; // This pair is now strictly sorted\n     \
        \               }\n                }\n            }\n        }\n\n        deleted_columns\n\
        \    }\n}"
      racket: "#lang racket\n(define/contract (min-deletion-size strs)\n  (-> (listof\
        \ string?) exact-integer?)\n  (let* ([n (length strs)])\n    (if (<= n 1)\n\
        \        0\n        (let* ([L (string-length (car strs))]\n               [deleted-columns\
        \ (make-box 0)]\n               [is-sorted (make-vector (- n 1) #f)])\n\n  \
        \        (for ([j (in-range L)]) ; Iterate through columns\n            (let\
        \ ([violation-found\n                   (for/or ([i (in-range (- n 1))])\n \
        \                    (and (not (vector-ref is-sorted i))\n                 \
        \         (> (char->integer (string-ref (list-ref strs i) j))\n            \
        \                 (char->integer (string-ref (list-ref strs (+ i 1)) j)))))]\n\
        \                  )\n              (if violation-found\n                  (set-box!\
        \ deleted-columns (+ (unbox deleted-columns) 1))\n                  ; If no\
        \ violation, keep this column and update is-sorted\n                  (for ([i\
        \ (in-range (- n 1))])\n                    (when (and (not (vector-ref is-sorted\
        \ i))\n                               (< (char->integer (string-ref (list-ref\
        \ strs i) j))\n                                  (char->integer (string-ref\
        \ (list-ref strs (+ i 1)) j))))\n                      (vector-set! is-sorted\
        \ i #t))))))\n          (unbox deleted-columns)))))"
      erlang: "-module(solution).\n-export([min_deletion_size/1]).\n\nmin_deletion_size(Strs)\
        \ ->\nN = length(Strs),\nif N =< 1 ->\n0;\ntrue ->\nL = length(hd(Strs)),\n\
        IsSorted = array:new([{size, N - 1}, {fixed, true}, {default, false}]),\n\n\
        min_deletion_size_loop(0, L, N, Strs, IsSorted, 0)\nend.\n\nmin_deletion_size_loop(J,\
        \ L, N, Strs, IsSorted, DeletedColumns) when J < L ->\n{ShouldDeleteCurrentColumn,\
        \ NewDeletedColumns} = check_column(J, N, Strs, IsSorted, DeletedColumns),\n\
        \nNewIsSorted = \nif ShouldDeleteCurrentColumn ->\n    IsSorted;\ntrue ->\n\
        \    update_is_sorted(J, N, Strs, IsSorted)\nend,\n\nmin_deletion_size_loop(J\
        \ + 1, L, N, Strs, NewIsSorted, NewDeletedColumns);\nmin_deletion_size_loop(_J,\
        \ _L, _N, _Strs, _IsSorted, DeletedColumns) ->\nDeletedColumns.\n\ncheck_column(J,\
        \ N, Strs, IsSorted, DeletedColumns) ->\ncheck_column_loop(0, N, J, Strs, IsSorted,\
        \ false, DeletedColumns).\n\ncheck_column_loop(I, N, J, Strs, IsSorted, ShouldDelete,\
        \ CurrentDeletedColumns) when I < N - 1 ->\ncase array:get(I, IsSorted) of\n\
        true ->\n    check_column_loop(I + 1, N, J, Strs, IsSorted, ShouldDelete, CurrentDeletedColumns);\n\
        false ->\n    StrI = lists:nth(I + 1, Strs),\n    StrIPlus1 = lists:nth(I +\
        \ 2, Strs),\n    CharI = lists:nth(J + 1, StrI),\n    CharIPlus1 = lists:nth(J\
        \ + 1, StrIPlus1),\n    if CharI > CharIPlus1 ->\n        {true, CurrentDeletedColumns\
        \ + 1};\n    true ->\n        check_column_loop(I + 1, N, J, Strs, IsSorted,\
        \ ShouldDelete, CurrentDeletedColumns)\n    end\nend;\ncheck_column_loop(_I,\
        \ _N, _J, _Strs, _IsSorted, ShouldDelete, CurrentDeletedColumns) ->\n{ShouldDelete,\
        \ CurrentDeletedColumns}.\n\nupdate_is_sorted(J, N, Strs, IsSorted) ->\nupdate_is_sorted_loop(0,\
        \ N, J, Strs, IsSorted).\n\nupdate_is_sorted_loop(I, N, J, Strs, CurrentIsSorted)\
        \ when I < N - 1 ->\nNewIsSorted = \ncase array:get(I, CurrentIsSorted) of\n\
        \    true ->\n        CurrentIsSorted;\n    false ->\n        StrI = lists:nth(I\
        \ + 1, Strs),\n        StrIPlus1 = lists:nth(I + 2, Strs),\n        CharI =\
        \ lists:nth(J + 1, StrI),\n        CharIPlus1 = lists:nth(J + 1, StrIPlus1),\n\
        \        if CharI < CharIPlus1 ->\n            array:set(I, true, CurrentIsSorted);\n\
        \        true ->\n            CurrentIsSorted\n        end\nend,\nupdate_is_sorted_loop(I\
        \ + 1, N, J, Strs, NewIsSorted);\nupdate_is_sorted_loop(_I, _N, _J, _Strs, IsSorted)\
        \ ->\nIsSorted."
      elixir: "defmodule Solution do\n  @spec min_deletion_size(strs :: [String.t])\
        \ :: integer\n  def min_deletion_size(strs) do\n    n = length(strs)\n    if\
        \ n <= 1 do\n      0\n    else\n      l = String.length(hd(strs))\n      is_sorted\
        \ = :array.new([{size: n - 1, fixed: true, default: false}])\n\n      do_min_deletion_size(0,\
        \ l, n, strs, is_sorted, 0)\n    end\n  end\n\n  defp do_min_deletion_size(j,\
        \ l, n, strs, is_sorted, deleted_columns) when j < l do\n    {should_delete_current_column,\
        \ new_deleted_columns} = check_column(j, n, strs, is_sorted, deleted_columns)\n\
        \n    new_is_sorted = \n      if should_delete_current_column do\n        is_sorted\n\
        \      else\n        update_is_sorted(j, n, strs, is_sorted)\n      end\n\n\
        \    do_min_deletion_size(j + 1, l, n, strs, new_is_sorted, new_deleted_columns)\n\
        \  end\n  defp do_min_deletion_size(_j, _l, _n, _strs, _is_sorted, deleted_columns)\
        \ do\n    deleted_columns\n  end\n\n  defp check_column(j, n, strs, is_sorted,\
        \ deleted_columns) do\n    check_column_loop(0, n, j, strs, is_sorted, false,\
        \ deleted_columns)\n  end\n\n  defp check_column_loop(i, n, j, strs, is_sorted,\
        \ should_delete, current_deleted_columns) when i < n - 1 do\n    case :array.get(i,\
        \ is_sorted) do\n      true ->\n        check_column_loop(i + 1, n, j, strs,\
        \ is_sorted, should_delete, current_deleted_columns)\n      false ->\n     \
        \   str_i = Enum.at(strs, i)\n        str_i_plus_1 = Enum.at(strs, i + 1)\n\
        \        char_i = String.at(str_i, j)\n        char_i_plus_1 = String.at(str_i_plus_1,\
        \ j)\n\n        if char_i > char_i_plus_1 do\n          {true, current_deleted_columns\
        \ + 1}\n        else\n          check_column_loop(i + 1, n, j, strs, is_sorted,\
        \ should_delete, current_deleted_columns)\n        end\n    end\n  end\n  defp\
        \ check_column_loop(_i, _n, _j, _strs, _is_sorted, should_delete, current_deleted_columns)\
        \ do\n    {should_delete, current_deleted_columns}\n  end\n\n  defp update_is_sorted(j,\
        \ n, strs, current_is_sorted) do\n    update_is_sorted_loop(0, n, j, strs, current_is_sorted)\n\
        \  end\n\n  defp update_is_sorted_loop(i, n, j, strs, current_is_sorted) when\
        \ i < n - 1 do\n    new_is_sorted = \n      case :array.get(i, current_is_sorted)\
        \ do\n        true ->\n          current_is_sorted\n        false ->\n     \
        \     str_i = Enum.at(strs, i)\n          str_i_plus_1 = Enum.at(strs, i + 1)\n\
        \          char_i = String.at(str_i, j)\n          char_i_plus_1 = String.at(str_i_plus_1,\
        \ j)\n\n          if char_i < char_i_plus_1 do\n            :array.set(i, true,\
        \ current_is_sorted)\n          else\n            current_is_sorted\n      \
        \    end\n      end\n    update_is_sorted_loop(i + 1, n, j, strs, new_is_sorted)\n\
        \  end\n  defp update_is_sorted_loop(_i, _n, _j, _strs, is_sorted) do\n    is_sorted\n\
        \  end\nend"
    approach: The problem asks for the minimum number of columns to delete such that
      the remaining strings are lexicographically sorted. We can solve this using a
      greedy approach. We iterate through the columns from left to right. For each column,
      we decide whether to keep it or delete it. A column must be deleted if keeping
      it would violate the lexicographical order for any adjacent pair of strings (i.e.,
      `strs[i]` would become greater than `strs[i+1]`) that are not yet strictly sorted
      by previously kept columns. If no such violation occurs, we keep the column.
    time_complexity: The time complexity is O(N * L), where N is the number of strings
      and L is the length of each string. We iterate through each of the L columns.
      For each column, we iterate through N-1 adjacent pairs of strings to check for
      violations and update their sorted status. Each character comparison takes constant
      time, leading to O(N) operations per column.
    space_complexity: The space complexity is O(N), where N is the number of strings.
      We use a boolean array of size N-1 to keep track of whether each adjacent pair
      of strings `(strs[i], strs[i+1])` has already been strictly sorted by previously
      kept columns. This array stores N-1 boolean values.
    elapsed_time: 88.40619468688965
    model: gemini-2.5-flash
    generated_at: '2025-12-21 01:13:09 '
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
      python: "class Solution:\n    def minDeletionSize(self, strs: List[str]) -> int:\n\
        \        count = 0\n        n = len(strs)\n        m = len(strs[0])\n      \
        \  for j in range(m):\n            for i in range(1, n):\n                if\
        \ strs[i - 1][j] > strs[i][j]:\n                    count += 1\n           \
        \         break\n        return count"
      python3: "class Solution:\n    def minDeletionSize(self, strs: List[str]) -> int:\n\
        \        count = 0\n        n = len(strs)\n        m = len(strs[0])\n      \
        \  for j in range(m):\n            for i in range(1, n):\n                if\
        \ strs[i - 1][j] > strs[i][j]:\n                    count += 1\n           \
        \         break\n        return count"
      c: "int minDeletionSize(char ** strs, int strsSize, int* strsColSize) {\n    int\
        \ count = 0;\n    int m = strsColSize[0];\n    for (int j = 0; j < m; j++) {\n\
        \        for (int i = 1; i < strsSize; i++) {\n            if (strs[i - 1][j]\
        \ > strs[i][j]) {\n                count++;\n                break;\n      \
        \      }\n        }\n    }\n    return count;\n}"
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
        \                (return)))))))"
      erlang: "min_deletion_size(Strs) ->\n    Count = lists:foldl(fun(J, Count0) ->\n\
        \        case lists:foldl(fun(I, Count1) ->\n            case string:slice(string:substr(lists:nth(I\
        \ - 1, Strs), J + 1, 1), 1, 1) > string:slice(string:substr(lists:nth(I, Strs),\
        \ J + 1, 1), 1, 1) of\n                true -> Count1 + 1;\n               \
        \ false -> Count1\n            end,\n            Count0,\n            lists:seq(1,\
        \ length(Strs) - 1))\n        of\n            Count1 when Count1 > Count0 ->\
        \ Count1;\n            _ -> Count0\n        end,\n        0,\n        lists:seq(0,\
        \ length(string:substr(hd(Strs), 1, 1)) - 1)),\n    Count."
      elixir: "def min_deletion_size(strs) do\n    count = 0\n    n = length(strs)\n\
        \    m = String.length(Enum.at(strs, 0))\n    Enum.reduce(0..m - 1, count, fn\
        \ j, count ->\n        Enum.reduce(1..n - 1, count, fn i, count ->\n       \
        \     if String.at(Enum.at(strs, i - 1), j) > String.at(Enum.at(strs, i), j)\
        \ do\n                count + 1\n            else\n                count\n \
        \           end\n        end)\n    end)\nend"
    approach: The problem can be solved by iterating over each column of the input strings
      and checking if the characters in that column are in lexicographic order. If they
      are not, we need to delete that column. We can use a greedy approach to solve
      this problem, where we always try to delete the minimum number of columns required
      to make the strings lexicographically sorted. The key intuition here is that if
      a column is not in lexicographic order, we can delete it and the remaining columns
      will still be in lexicographic order if the original strings were in lexicographic
      order after deleting that column.
    time_complexity: The time complexity of this solution is O(n*m), where n is the
      number of strings and m is the length of each string. This is because we are iterating
      over each column of the input strings, and for each column, we are comparing the
      characters at that position in each string.
    space_complexity: The space complexity of this solution is O(1), which means the
      space required does not change with the size of the input, making it very efficient
      in terms of space usage. We only need a constant amount of space to store the
      count of columns to be deleted and the current column being processed.
    elapsed_time: 5.892703533172607
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-21 01:13:15 '
---

## Problem #955: Delete Columns to Make Sorted II

**Difficulty:** Medium

**Topics:** Array, String, Greedy

## Problem Description

<p>You are given an array of <code>n</code> strings <code>strs</code>, all of the same length.</p>

<p>We may choose any deletion indices, and we delete all the characters in those indices for each string.</p>

<p>For example, if we have <code>strs = [&quot;abcdef&quot;,&quot;uvwxyz&quot;]</code> and deletion indices <code>{0, 2, 3}</code>, then the final array after deletions is <code>[&quot;bef&quot;, &quot;vyz&quot;]</code>.</p>

<p>Suppose we chose a set of deletion indices <code>answer</code> such that after deletions, the final array has its elements in <strong>lexicographic</strong> order (i.e., <code>strs[0] &lt;= strs[1] &lt;= strs[2] &lt;= ... &lt;= strs[n - 1]</code>). Return <em>the minimum possible value of</em> <code>answer.length</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;ca&quot;,&quot;bb&quot;,&quot;ac&quot;]
<strong>Output:</strong> 1
<strong>Explanation:</strong> 
After deleting the first column, strs = [&quot;a&quot;, &quot;b&quot;, &quot;c&quot;].
Now strs is in lexicographic order (ie. strs[0] &lt;= strs[1] &lt;= strs[2]).
We require at least 1 deletion since initially strs was not in lexicographic order, so the answer is 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;xc&quot;,&quot;yb&quot;,&quot;za&quot;]
<strong>Output:</strong> 0
<strong>Explanation:</strong> 
strs is already in lexicographic order, so we do not need to delete anything.
Note that the rows of strs are not necessarily in lexicographic order:
i.e., it is NOT necessarily true that (strs[0][0] &lt;= strs[0][1] &lt;= ...)
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> strs = [&quot;zyx&quot;,&quot;wvu&quot;,&quot;tsr&quot;]
<strong>Output:</strong> 3
<strong>Explanation:</strong> We have to delete every column.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == strs.length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= strs[i].length &lt;= 100</code></li>
	<li><code>strs[i]</code> consists of lowercase English letters.</li>
</ul>


## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-21 01:13:09 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks for the minimum number of columns to delete such that the remaining strings are lexicographically sorted. We can solve this using a greedy approach. We iterate through the columns from left to right. For each column, we decide whether to keep it or delete it. A column must be deleted if keeping it would violate the lexicographical order for any adjacent pair of strings (i.e., `strs[i]` would become greater than `strs[i+1]`) that are not yet strictly sorted by previously kept columns. If no such violation occurs, we keep the column.

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
        if (n <= 1) {
            return 0;
        }
        int L = strs[0].length();
        int deleted_columns = 0;
        std::vector<bool> is_sorted(n - 1, false);

        for (int j = 0; j < L; ++j) { // Iterate through columns
            bool should_delete_current_column = false;
            for (int i = 0; i < n - 1; ++i) { // Iterate through adjacent string pairs
                if (is_sorted[i]) {
                    continue; // This pair is already strictly sorted
                }
                if (strs[i][j] > strs[i+1][j]) {
                    should_delete_current_column = true;
                    deleted_columns++;
                    break; // Found a violation, must delete this column
                }
            }

            if (!should_delete_current_column) { // If we decided to keep this column
                for (int i = 0; i < n - 1; ++i) {
                    if (!is_sorted[i] && strs[i][j] < strs[i+1][j]) {
                        is_sorted[i] = true; // This pair is now strictly sorted
                    }
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
        int n = strs.length;
        if (n <= 1) {
            return 0;
        }
        int L = strs[0].length();
        int deletedColumns = 0;
        boolean[] isSorted = new boolean[n - 1];

        for (int j = 0; j < L; j++) { // Iterate through columns
            boolean shouldDeleteCurrentColumn = false;
            for (int i = 0; i < n - 1; i++) { // Iterate through adjacent string pairs
                if (isSorted[i]) {
                    continue; // This pair is already strictly sorted
                }
                if (strs[i].charAt(j) > strs[i+1].charAt(j)) {
                    shouldDeleteCurrentColumn = true;
                    deletedColumns++;
                    break; // Found a violation, must delete this column
                }
            }

            if (!shouldDeleteCurrentColumn) { // If we decided to keep this column
                for (int i = 0; i < n - 1; i++) {
                    if (!isSorted[i] && strs[i].charAt(j) < strs[i+1].charAt(j)) {
                        isSorted[i] = true; // This pair is now strictly sorted
                    }
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
        n = len(strs)
        if n <= 1:
            return 0
        L = len(strs[0])
        deleted_columns = 0
        is_sorted = [False] * (n - 1)

        for j in range(L):  # Iterate through columns
            should_delete_current_column = False
            for i in range(n - 1):  # Iterate through adjacent string pairs
                if is_sorted[i]:
                    continue  # This pair is already strictly sorted
                if strs[i][j] > strs[i+1][j]:
                    should_delete_current_column = True
                    deleted_columns += 1
                    break  # Found a violation, must delete this column

            if not should_delete_current_column:  # If we decided to keep this column
                for i in range(n - 1):
                    if not is_sorted[i] and strs[i][j] < strs[i+1][j]:
                        is_sorted[i] = True  # This pair is now strictly sorted

        return deleted_columns
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        if n <= 1:
            return 0
        L = len(strs[0])
        deleted_columns = 0
        is_sorted = [False] * (n - 1)

        for j in range(L):  # Iterate through columns
            should_delete_current_column = False
            for i in range(n - 1):  # Iterate through adjacent string pairs
                if is_sorted[i]:
                    continue  # This pair is already strictly sorted
                if strs[i][j] > strs[i+1][j]:
                    should_delete_current_column = True
                    deleted_columns += 1
                    break  # Found a violation, must delete this column

            if not should_delete_current_column:  # If we decided to keep this column
                for i in range(n - 1):
                    if not is_sorted[i] and strs[i][j] < strs[i+1][j]:
                        is_sorted[i] = True  # This pair is now strictly sorted

        return deleted_columns
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int minDeletionSize(char **strs, int strsSize) {
    if (strsSize <= 1) {
        return 0;
    }
    int L = strlen(strs[0]);
    int deleted_columns = 0;
    bool *is_sorted = (bool *)calloc(strsSize - 1, sizeof(bool));

    for (int j = 0; j < L; ++j) { // Iterate through columns
        bool should_delete_current_column = false;
        for (int i = 0; i < strsSize - 1; ++i) { // Iterate through adjacent string pairs
            if (is_sorted[i]) {
                continue; // This pair is already strictly sorted
            }
            if (strs[i][j] > strs[i+1][j]) {
                should_delete_current_column = true;
                deleted_columns++;
                break; // Found a violation, must delete this column
            }
        }

        if (!should_delete_current_column) { // If we decided to keep this column
            for (int i = 0; i < strsSize - 1; ++i) {
                if (!is_sorted[i] && strs[i][j] < strs[i+1][j]) {
                    is_sorted[i] = true; // This pair is now strictly sorted
                }
            }
        }
    }

    free(is_sorted);
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
        int n = strs.Length;
        if (n <= 1) {
            return 0;
        }
        int L = strs[0].Length;
        int deletedColumns = 0;
        bool[] isSorted = new bool[n - 1];

        for (int j = 0; j < L; j++) { // Iterate through columns
            bool shouldDeleteCurrentColumn = false;
            for (int i = 0; i < n - 1; i++) { // Iterate through adjacent string pairs
                if (isSorted[i]) {
                    continue; // This pair is already strictly sorted
                }
                if (strs[i][j] > strs[i+1][j]) {
                    shouldDeleteCurrentColumn = true;
                    deletedColumns++;
                    break; // Found a violation, must delete this column
                }
            }

            if (!shouldDeleteCurrentColumn) { // If we decided to keep this column
                for (int i = 0; i < n - 1; i++) {
                    if (!isSorted[i] && strs[i][j] < strs[i+1][j]) {
                        isSorted[i] = true; // This pair is now strictly sorted
                    }
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
    let n = strs.length;
    if (n <= 1) {
        return 0;
    }
    let L = strs[0].length;
    let deletedColumns = 0;
    let isSorted = new Array(n - 1).fill(false);

    for (let j = 0; j < L; j++) { // Iterate through columns
        let shouldDeleteCurrentColumn = false;
        for (let i = 0; i < n - 1; i++) { // Iterate through adjacent string pairs
            if (isSorted[i]) {
                continue; // This pair is already strictly sorted
            }
            if (strs[i][j] > strs[i+1][j]) {
                shouldDeleteCurrentColumn = true;
                deletedColumns++;
                break; // Found a violation, must delete this column
            }
        }

        if (!shouldDeleteCurrentColumn) { // If we decided to keep this column
            for (let i = 0; i < n - 1; i++) {
                if (!isSorted[i] && strs[i][j] < strs[i+1][j]) {
                    isSorted[i] = true; // This pair is now strictly sorted
                }
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
    let n = strs.length;
    if (n <= 1) {
        return 0;
    }
    let L = strs[0].length;
    let deletedColumns = 0;
    let isSorted: boolean[] = new Array(n - 1).fill(false);

    for (let j = 0; j < L; j++) { // Iterate through columns
        let shouldDeleteCurrentColumn = false;
        for (let i = 0; i < n - 1; i++) { // Iterate through adjacent string pairs
            if (isSorted[i]) {
                continue; // This pair is already strictly sorted
            }
            if (strs[i][j] > strs[i+1][j]) {
                shouldDeleteCurrentColumn = true;
                deletedColumns++;
                break; // Found a violation, must delete this column
            }
        }

        if (!shouldDeleteCurrentColumn) { // If we decided to keep this column
            for (let i = 0; i < n - 1; i++) {
                if (!isSorted[i] && strs[i][j] < strs[i+1][j]) {
                    isSorted[i] = true; // This pair is now strictly sorted
                }
            }
        }
    }

    return deletedColumns;
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
     * @return Integer
     */
    function minDeletionSize($strs) {
        $n = count($strs);
        if ($n <= 1) {
            return 0;
        }
        $L = strlen($strs[0]);
        $deletedColumns = 0;
        $isSorted = array_fill(0, $n - 1, false);

        for ($j = 0; $j < $L; $j++) { // Iterate through columns
            $shouldDeleteCurrentColumn = false;
            for ($i = 0; $i < $n - 1; $i++) { // Iterate through adjacent string pairs
                if ($isSorted[$i]) {
                    continue; // This pair is already strictly sorted
                }
                if ($strs[$i][$j] > $strs[$i+1][$j]) {
                    $shouldDeleteCurrentColumn = true;
                    $deletedColumns++;
                    break; // Found a violation, must delete this column
                }
            }

            if (!$shouldDeleteCurrentColumn) { // If we decided to keep this column
                for ($i = 0; $i < $n - 1; $i++) {
                    if (!$isSorted[$i] && $strs[$i][$j] < $strs[$i+1][$j]) {
                        $isSorted[$i] = true; // This pair is now strictly sorted
                    }
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
        let n = strs.count
        if n <= 1 {
            return 0
        }
        let L = strs[0].count
        var deletedColumns = 0
        var isSorted = Array(repeating: false, count: n - 1)

        let strChars = strs.map { Array($0) }

        for j in 0..<L { // Iterate through columns
            var shouldDeleteCurrentColumn = false
            for i in 0..<n - 1 { // Iterate through adjacent string pairs
                if isSorted[i] {
                    continue // This pair is already strictly sorted
                }
                if strChars[i][j] > strChars[i+1][j] {
                    shouldDeleteCurrentColumn = true
                    deletedColumns += 1
                    break // Found a violation, must delete this column
                }
            }

            if !shouldDeleteCurrentColumn { // If we decided to keep this column
                for i in 0..<n - 1 {
                    if !isSorted[i] && strChars[i][j] < strChars[i+1][j] {
                        isSorted[i] = true // This pair is now strictly sorted
                    }
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
        val n = strs.size
        if (n <= 1) {
            return 0
        }
        val L = strs[0].length
        var deletedColumns = 0
        val isSorted = BooleanArray(n - 1) { false }

        for (j in 0 until L) { // Iterate through columns
            var shouldDeleteCurrentColumn = false
            for (i in 0 until n - 1) { // Iterate through adjacent string pairs
                if (isSorted[i]) {
                    continue // This pair is already strictly sorted
                }
                if (strs[i][j] > strs[i+1][j]) {
                    shouldDeleteCurrentColumn = true
                    deletedColumns++
                    break // Found a violation, must delete this column
                }
            }

            if (!shouldDeleteCurrentColumn) { // If we decided to keep this column
                for (i in 0 until n - 1) {
                    if (!isSorted[i] && strs[i][j] < strs[i+1][j]) {
                        isSorted[i] = true // This pair is now strictly sorted
                    }
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
    int n = strs.length;
    if (n <= 1) {
      return 0;
    }
    int L = strs[0].length;
    int deletedColumns = 0;
    List<bool> isSorted = List.filled(n - 1, false);

    for (int j = 0; j < L; j++) { // Iterate through columns
      bool shouldDeleteCurrentColumn = false;
      for (int i = 0; i < n - 1; i++) { // Iterate through adjacent string pairs
        if (isSorted[i]) {
          continue; // This pair is already strictly sorted
        }
        if (strs[i].codeUnitAt(j) > strs[i+1].codeUnitAt(j)) {
          shouldDeleteCurrentColumn = true;
          deletedColumns++;
          break; // Found a violation, must delete this column
        }
      }

      if (!shouldDeleteCurrentColumn) { // If we decided to keep this column
        for (int i = 0; i < n - 1; i++) {
          if (!isSorted[i] && strs[i].codeUnitAt(j) < strs[i+1].codeUnitAt(j)) {
            isSorted[i] = true; // This pair is now strictly sorted
          }
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
    n := len(strs)
    if n <= 1 {
        return 0
    }
    L := len(strs[0])
    deletedColumns := 0
    isSorted := make([]bool, n-1)

    for j := 0; j < L; j++ { // Iterate through columns
        shouldDeleteCurrentColumn := false
        for i := 0; i < n-1; i++ { // Iterate through adjacent string pairs
            if isSorted[i] {
                continue // This pair is already strictly sorted
            }
            if strs[i][j] > strs[i+1][j] {
                shouldDeleteCurrentColumn = true
                deletedColumns++
                break // Found a violation, must delete this column
            }
        }

        if !shouldDeleteCurrentColumn { // If we decided to keep this column
            for i := 0; i < n-1; i++ {
                if !isSorted[i] && strs[i][j] < strs[i+1][j] {
                    isSorted[i] = true // This pair is now strictly sorted
                }
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
    n = strs.length
    return 0 if n <= 1
    L = strs[0].length
    deleted_columns = 0
    is_sorted = Array.new(n - 1, false)

    (0...L).each do |j| # Iterate through columns
        should_delete_current_column = false
        (0...n - 1).each do |i| # Iterate through adjacent string pairs
            if is_sorted[i]
                next # This pair is already strictly sorted
            end
            if strs[i][j] > strs[i+1][j]
                should_delete_current_column = true
                deleted_columns += 1
                break # Found a violation, must delete this column
            end
        end

        unless should_delete_current_column # If we decided to keep this column
            (0...n - 1).each do |i|
                if !is_sorted[i] && strs[i][j] < strs[i+1][j]
                    is_sorted[i] = true # This pair is now strictly sorted
                end
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
        val n = strs.length
        if (n <= 1) {
            return 0
        }
        val L = strs(0).length
        var deletedColumns = 0
        val isSorted = Array.fill(n - 1)(false)

        for (j <- 0 until L) { // Iterate through columns
            var shouldDeleteCurrentColumn = false
            for (i <- 0 until n - 1) { // Iterate through adjacent string pairs
                if (isSorted(i)) {
                    // This pair is already strictly sorted
                } else if (strs(i)(j) > strs(i+1)(j)) {
                    shouldDeleteCurrentColumn = true
                    deletedColumns += 1
                    break // Found a violation, must delete this column
                }
            }

            if (!shouldDeleteCurrentColumn) { // If we decided to keep this column
                for (i <- 0 until n - 1) {
                    if (!isSorted(i) && strs(i)(j) < strs(i+1)(j)) {
                        isSorted(i) = true // This pair is now strictly sorted
                    }
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
        let n = strs.len();
        if n <= 1 {
            return 0;
        }
        let L = strs[0].len();
        let mut deleted_columns = 0;
        let mut is_sorted = vec![false; n - 1];

        // Convert strings to vectors of chars for easier indexing
        let str_chars: Vec<Vec<char>> = strs.iter().map(|s| s.chars().collect()).collect();

        for j in 0..L { // Iterate through columns
            let mut should_delete_current_column = false;
            for i in 0..n - 1 { // Iterate through adjacent string pairs
                if is_sorted[i] {
                    continue; // This pair is already strictly sorted
                }
                if str_chars[i][j] > str_chars[i+1][j] {
                    should_delete_current_column = true;
                    deleted_columns += 1;
                    break; // Found a violation, must delete this column
                }
            }

            if !should_delete_current_column { // If we decided to keep this column
                for i in 0..n - 1 {
                    if !is_sorted[i] && str_chars[i][j] < str_chars[i+1][j] {
                        is_sorted[i] = true; // This pair is now strictly sorted
                    }
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
  (-> (listof string?) exact-integer?)
  (let* ([n (length strs)])
    (if (<= n 1)
        0
        (let* ([L (string-length (car strs))]
               [deleted-columns (make-box 0)]
               [is-sorted (make-vector (- n 1) #f)])

          (for ([j (in-range L)]) ; Iterate through columns
            (let ([violation-found
                   (for/or ([i (in-range (- n 1))])
                     (and (not (vector-ref is-sorted i))
                          (> (char->integer (string-ref (list-ref strs i) j))
                             (char->integer (string-ref (list-ref strs (+ i 1)) j)))))]
                  )
              (if violation-found
                  (set-box! deleted-columns (+ (unbox deleted-columns) 1))
                  ; If no violation, keep this column and update is-sorted
                  (for ([i (in-range (- n 1))])
                    (when (and (not (vector-ref is-sorted i))
                               (< (char->integer (string-ref (list-ref strs i) j))
                                  (char->integer (string-ref (list-ref strs (+ i 1)) j))))
                      (vector-set! is-sorted i #t))))))
          (unbox deleted-columns)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([min_deletion_size/1]).

min_deletion_size(Strs) ->
N = length(Strs),
if N =< 1 ->
0;
true ->
L = length(hd(Strs)),
IsSorted = array:new([{size, N - 1}, {fixed, true}, {default, false}]),

min_deletion_size_loop(0, L, N, Strs, IsSorted, 0)
end.

min_deletion_size_loop(J, L, N, Strs, IsSorted, DeletedColumns) when J < L ->
{ShouldDeleteCurrentColumn, NewDeletedColumns} = check_column(J, N, Strs, IsSorted, DeletedColumns),

NewIsSorted = 
if ShouldDeleteCurrentColumn ->
    IsSorted;
true ->
    update_is_sorted(J, N, Strs, IsSorted)
end,

min_deletion_size_loop(J + 1, L, N, Strs, NewIsSorted, NewDeletedColumns);
min_deletion_size_loop(_J, _L, _N, _Strs, _IsSorted, DeletedColumns) ->
DeletedColumns.

check_column(J, N, Strs, IsSorted, DeletedColumns) ->
check_column_loop(0, N, J, Strs, IsSorted, false, DeletedColumns).

check_column_loop(I, N, J, Strs, IsSorted, ShouldDelete, CurrentDeletedColumns) when I < N - 1 ->
case array:get(I, IsSorted) of
true ->
    check_column_loop(I + 1, N, J, Strs, IsSorted, ShouldDelete, CurrentDeletedColumns);
false ->
    StrI = lists:nth(I + 1, Strs),
    StrIPlus1 = lists:nth(I + 2, Strs),
    CharI = lists:nth(J + 1, StrI),
    CharIPlus1 = lists:nth(J + 1, StrIPlus1),
    if CharI > CharIPlus1 ->
        {true, CurrentDeletedColumns + 1};
    true ->
        check_column_loop(I + 1, N, J, Strs, IsSorted, ShouldDelete, CurrentDeletedColumns)
    end
end;
check_column_loop(_I, _N, _J, _Strs, _IsSorted, ShouldDelete, CurrentDeletedColumns) ->
{ShouldDelete, CurrentDeletedColumns}.

update_is_sorted(J, N, Strs, IsSorted) ->
update_is_sorted_loop(0, N, J, Strs, IsSorted).

update_is_sorted_loop(I, N, J, Strs, CurrentIsSorted) when I < N - 1 ->
NewIsSorted = 
case array:get(I, CurrentIsSorted) of
    true ->
        CurrentIsSorted;
    false ->
        StrI = lists:nth(I + 1, Strs),
        StrIPlus1 = lists:nth(I + 2, Strs),
        CharI = lists:nth(J + 1, StrI),
        CharIPlus1 = lists:nth(J + 1, StrIPlus1),
        if CharI < CharIPlus1 ->
            array:set(I, true, CurrentIsSorted);
        true ->
            CurrentIsSorted
        end
end,
update_is_sorted_loop(I + 1, N, J, Strs, NewIsSorted);
update_is_sorted_loop(_I, _N, _J, _Strs, IsSorted) ->
IsSorted.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_deletion_size(strs :: [String.t]) :: integer
  def min_deletion_size(strs) do
    n = length(strs)
    if n <= 1 do
      0
    else
      l = String.length(hd(strs))
      is_sorted = :array.new([{size: n - 1, fixed: true, default: false}])

      do_min_deletion_size(0, l, n, strs, is_sorted, 0)
    end
  end

  defp do_min_deletion_size(j, l, n, strs, is_sorted, deleted_columns) when j < l do
    {should_delete_current_column, new_deleted_columns} = check_column(j, n, strs, is_sorted, deleted_columns)

    new_is_sorted = 
      if should_delete_current_column do
        is_sorted
      else
        update_is_sorted(j, n, strs, is_sorted)
      end

    do_min_deletion_size(j + 1, l, n, strs, new_is_sorted, new_deleted_columns)
  end
  defp do_min_deletion_size(_j, _l, _n, _strs, _is_sorted, deleted_columns) do
    deleted_columns
  end

  defp check_column(j, n, strs, is_sorted, deleted_columns) do
    check_column_loop(0, n, j, strs, is_sorted, false, deleted_columns)
  end

  defp check_column_loop(i, n, j, strs, is_sorted, should_delete, current_deleted_columns) when i < n - 1 do
    case :array.get(i, is_sorted) do
      true ->
        check_column_loop(i + 1, n, j, strs, is_sorted, should_delete, current_deleted_columns)
      false ->
        str_i = Enum.at(strs, i)
        str_i_plus_1 = Enum.at(strs, i + 1)
        char_i = String.at(str_i, j)
        char_i_plus_1 = String.at(str_i_plus_1, j)

        if char_i > char_i_plus_1 do
          {true, current_deleted_columns + 1}
        else
          check_column_loop(i + 1, n, j, strs, is_sorted, should_delete, current_deleted_columns)
        end
    end
  end
  defp check_column_loop(_i, _n, _j, _strs, _is_sorted, should_delete, current_deleted_columns) do
    {should_delete, current_deleted_columns}
  end

  defp update_is_sorted(j, n, strs, current_is_sorted) do
    update_is_sorted_loop(0, n, j, strs, current_is_sorted)
  end

  defp update_is_sorted_loop(i, n, j, strs, current_is_sorted) when i < n - 1 do
    new_is_sorted = 
      case :array.get(i, current_is_sorted) do
        true ->
          current_is_sorted
        false ->
          str_i = Enum.at(strs, i)
          str_i_plus_1 = Enum.at(strs, i + 1)
          char_i = String.at(str_i, j)
          char_i_plus_1 = String.at(str_i_plus_1, j)

          if char_i < char_i_plus_1 do
            :array.set(i, true, current_is_sorted)
          else
            current_is_sorted
          end
      end
    update_is_sorted_loop(i + 1, n, j, strs, new_is_sorted)
  end
  defp update_is_sorted_loop(_i, _n, _j, _strs, is_sorted) do
    is_sorted
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N * L), where N is the number of strings and L is the length of each string. We iterate through each of the L columns. For each column, we iterate through N-1 adjacent pairs of strings to check for violations and update their sorted status. Each character comparison takes constant time, leading to O(N) operations per column.

- **Space Complexity:** The space complexity is O(N), where N is the number of strings. We use a boolean array of size N-1 to keep track of whether each adjacent pair of strings `(strs[i], strs[i+1])` has already been strictly sorted by previously kept columns. This array stores N-1 boolean values.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-21 01:13:15 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by iterating over each column of the input strings and checking if the characters in that column are in lexicographic order. If they are not, we need to delete that column. We can use a greedy approach to solve this problem, where we always try to delete the minimum number of columns required to make the strings lexicographically sorted. The key intuition here is that if a column is not in lexicographic order, we can delete it and the remaining columns will still be in lexicographic order if the original strings were in lexicographic order after deleting that column.

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
    def minDeletionSize(self, strs: List[str]) -> int:
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
    def minDeletionSize(self, strs: List[str]) -> int:
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
int minDeletionSize(char ** strs, int strsSize, int* strsColSize) {
    int count = 0;
    int m = strsColSize[0];
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
                (return)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
min_deletion_size(Strs) ->
    Count = lists:foldl(fun(J, Count0) ->
        case lists:foldl(fun(I, Count1) ->
            case string:slice(string:substr(lists:nth(I - 1, Strs), J + 1, 1), 1, 1) > string:slice(string:substr(lists:nth(I, Strs), J + 1, 1), 1, 1) of
                true -> Count1 + 1;
                false -> Count1
            end,
            Count0,
            lists:seq(1, length(Strs) - 1))
        of
            Count1 when Count1 > Count0 -> Count1;
            _ -> Count0
        end,
        0,
        lists:seq(0, length(string:substr(hd(Strs), 1, 1)) - 1)),
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
    Enum.reduce(0..m - 1, count, fn j, count ->
        Enum.reduce(1..n - 1, count, fn i, count ->
            if String.at(Enum.at(strs, i - 1), j) > String.at(Enum.at(strs, i), j) do
                count + 1
            else
                count
            end
        end)
    end)
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this solution is O(n*m), where n is the number of strings and m is the length of each string. This is because we are iterating over each column of the input strings, and for each column, we are comparing the characters at that position in each string.

- **Space Complexity:** The space complexity of this solution is O(1), which means the space required does not change with the size of the input, making it very efficient in terms of space usage. We only need a constant amount of space to store the count of columns to be deleted and the current column being processed.

</div>
</details>
