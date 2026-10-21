---
layout: post
title: "Minimum Operations to Sort a String"
date: 2026-10-21 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-operations-to-sort-a-string/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minOperations(string s) {\n        int\
        \ n = s.length();\n        if (n <= 1) return 0;\n\n        bool sorted = true;\n\
        \        for (int i = 0; i < n - 1; ++i) {\n            if (s[i] > s[i + 1])\
        \ {\n                sorted = false;\n                break;\n            }\n\
        \        }\n        if (sorted) return 0;\n        if (n == 2) return -1;\n\n\
        \        char mn = s[0], mx = s[0];\n        for (char c : s) {\n          \
        \  if (c < mn) mn = c;\n            if (c > mx) mx = c;\n        }\n\n     \
        \   if (s[0] == mn || s[n - 1] == mx) return 1;\n\n        bool mn_in_prefix\
        \ = false;\n        for (int i = 0; i < n - 1; ++i) {\n            if (s[i]\
        \ == mn) mn_in_prefix = true;\n        }\n        bool mx_in_suffix = false;\n\
        \        for (int i = 1; i < n; ++i) {\n            if (s[i] == mx) mx_in_suffix\
        \ = true;\n        }\n\n        if (mn_in_prefix || mx_in_suffix) return 2;\n\
        \n        return 3;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public int minOperations(String\
        \ s) {\n        int n = s.length();\n        if (n <= 1) return 0;\n\n     \
        \   boolean sorted = true;\n        for (int i = 0; i < n - 1; i++) {\n    \
        \        if (s.charAt(i) > s.charAt(i + 1)) {\n                sorted = false;\n\
        \                break;\n            }\n        }\n        if (sorted) return\
        \ 0;\n        if (n == 2) return -1;\n\n        char mn = s.charAt(0);\n   \
        \     char mx = s.charAt(0);\n        for (int i = 1; i < n; i++) {\n      \
        \      char c = s.charAt(i);\n            if (c < mn) mn = c;\n            if\
        \ (c > mx) mx = c;\n        }\n\n        if (s.charAt(0) == mn || s.charAt(n\
        \ - 1) == mx) return 1;\n\n        boolean mnInPrefix = false;\n        for\
        \ (int i = 0; i < n - 1; i++) {\n            if (s.charAt(i) == mn) {\n    \
        \            mnInPrefix = true;\n                break;\n            }\n   \
        \     }\n        boolean mxInSuffix = false;\n        for (int i = 1; i < n;\
        \ i++) {\n            if (s.charAt(i) == mx) {\n                mxInSuffix =\
        \ true;\n                break;\n            }\n        }\n\n        if (mnInPrefix\
        \ || mxInSuffix) return 2;\n\n        return 3;\n    }\n}"
      python: "class Solution(object):\n    def minOperations(self, s):\n        \"\"\
        \"\n        :type s: str\n        :rtype: int\n        \"\"\"\n        n = len(s)\n\
        \        if n <= 1:\n            return 0\n\n        is_sorted = True\n    \
        \    for i in range(n - 1):\n            if s[i] > s[i+1]:\n               \
        \ is_sorted = False\n                break\n        if is_sorted:\n        \
        \    return 0\n        if n == 2:\n            return -1\n\n        mn = min(s)\n\
        \        mx = max(s)\n\n        if s[0] == mn or s[n-1] == mx:\n           \
        \ return 1\n\n        mn_in_prefix = any(s[i] == mn for i in range(n - 1))\n\
        \        mx_in_suffix = any(s[i] == mx for i in range(1, n))\n\n        if mn_in_prefix\
        \ or mx_in_suffix:\n            return 2\n\n        return 3"
      python3: "class Solution:\n    def minOperations(self, s: str) -> int:\n     \
        \   n = len(s)\n        if n <= 1:\n            return 0\n\n        is_sorted\
        \ = True\n        for i in range(n - 1):\n            if s[i] > s[i+1]:\n  \
        \              is_sorted = False\n                break\n        if is_sorted:\n\
        \            return 0\n        if n == 2:\n            return -1\n\n       \
        \ mn = min(s)\n        mx = max(s)\n\n        if s[0] == mn or s[n-1] == mx:\n\
        \            return 1\n\n        mn_in_prefix = any(s[i] == mn for i in range(n\
        \ - 1))\n        mx_in_suffix = any(s[i] == mx for i in range(1, n))\n\n   \
        \     if mn_in_prefix or mx_in_suffix:\n            return 2\n\n        return\
        \ 3"
      c: "#include <string.h>\n#include <stdbool.h>\n\nint minOperations(char* s) {\n\
        \    int n = strlen(s);\n    if (n <= 1) return 0;\n\n    bool is_sorted = true;\n\
        \    for (int i = 0; i < n - 1; i++) {\n        if (s[i] > s[i + 1]) {\n   \
        \         is_sorted = false;\n            break;\n        }\n    }\n    if (is_sorted)\
        \ return 0;\n    if (n == 2) return -1;\n\n    char mn = s[0], mx = s[0];\n\
        \    for (int i = 1; i < n; i++) {\n        if (s[i] < mn) mn = s[i];\n    \
        \    if (s[i] > mx) mx = s[i];\n    }\n\n    if (s[0] == mn || s[n - 1] == mx)\
        \ return 1;\n\n    bool mn_in_prefix = false;\n    for (int i = 0; i < n - 1;\
        \ i++) {\n        if (s[i] == mn) {\n            mn_in_prefix = true;\n    \
        \        break;\n        }\n    }\n    bool mx_in_suffix = false;\n    for (int\
        \ i = 1; i < n; i++) {\n        if (s[i] == mx) {\n            mx_in_suffix\
        \ = true;\n            break;\n        }\n    }\n\n    if (mn_in_prefix || mx_in_suffix)\
        \ return 2;\n\n    return 3;\n}"
      csharp: "public class Solution {\n    public int MinOperations(string s) {\n \
        \       int n = s.Length;\n        if (n <= 1) return 0;\n\n        bool isSorted\
        \ = true;\n        char minChar = s[0];\n        char maxChar = s[0];\n\n  \
        \      for (int i = 1; i < n; i++) {\n            if (s[i] < s[i - 1]) {\n \
        \               isSorted = false;\n            }\n            if (s[i] < minChar)\
        \ {\n                minChar = s[i];\n            }\n            if (s[i] >\
        \ maxChar) {\n                maxChar = s[i];\n            }\n        }\n\n\
        \        if (isSorted) return 0;\n        if (n == 2) return -1;\n\n       \
        \ if (s[0] == minChar || s[n - 1] == maxChar) {\n            return 1;\n   \
        \     }\n\n        bool minInProperPrefix = false;\n        for (int i = 0;\
        \ i < n - 1; i++) {\n            if (s[i] == minChar) {\n                minInProperPrefix\
        \ = true;\n                break;\n            }\n        }\n\n        bool\
        \ maxInProperSuffix = false;\n        for (int i = 1; i < n; i++) {\n      \
        \      if (s[i] == maxChar) {\n                maxInProperSuffix = true;\n \
        \               break;\n            }\n        }\n\n        if (minInProperPrefix\
        \ || maxInProperSuffix) {\n            return 2;\n        }\n\n        return\
        \ 3;\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {number}\n */\nvar minOperations\
        \ = function(s) {\n    const n = s.length;\n    if (n <= 1) return 0;\n\n  \
        \  let isSorted = true;\n    let minChar = s[0];\n    let maxChar = s[0];\n\n\
        \    for (let i = 1; i < n; i++) {\n        if (s[i] < s[i - 1]) {\n       \
        \     isSorted = false;\n        }\n        if (s[i] < minChar) {\n        \
        \    minChar = s[i];\n        }\n        if (s[i] > maxChar) {\n           \
        \ maxChar = s[i];\n        }\n    }\n\n    if (isSorted) return 0;\n    if (n\
        \ === 2) return -1;\n\n    if (s[0] === minChar || s[n - 1] === maxChar) {\n\
        \        return 1;\n    }\n\n    let minInProperPrefix = false;\n    for (let\
        \ i = 0; i < n - 1; i++) {\n        if (s[i] === minChar) {\n            minInProperPrefix\
        \ = true;\n            break;\n        }\n    }\n\n    let maxInProperSuffix\
        \ = false;\n    for (let i = 1; i < n; i++) {\n        if (s[i] === maxChar)\
        \ {\n            maxInProperSuffix = true;\n            break;\n        }\n\
        \    }\n\n    if (minInProperPrefix || maxInProperSuffix) {\n        return\
        \ 2;\n    }\n\n    return 3;\n};"
      typescript: "function minOperations(s: string): number {\n    const n: number\
        \ = s.length;\n    if (n <= 1) return 0;\n\n    let isSorted: boolean = true;\n\
        \    let minChar: string = s[0];\n    let maxChar: string = s[0];\n\n    for\
        \ (let i = 1; i < n; i++) {\n        if (s[i] < s[i - 1]) {\n            isSorted\
        \ = false;\n        }\n        if (s[i] < minChar) {\n            minChar =\
        \ s[i];\n        }\n        if (s[i] > maxChar) {\n            maxChar = s[i];\n\
        \        }\n    }\n\n    if (isSorted) return 0;\n    if (n === 2) return -1;\n\
        \n    if (s[0] === minChar || s[n - 1] === maxChar) {\n        return 1;\n \
        \   }\n\n    let minInProperPrefix: boolean = false;\n    for (let i = 0; i\
        \ < n - 1; i++) {\n        if (s[i] === minChar) {\n            minInProperPrefix\
        \ = true;\n            break;\n        }\n    }\n\n    let maxInProperSuffix:\
        \ boolean = false;\n    for (let i = 1; i < n; i++) {\n        if (s[i] ===\
        \ maxChar) {\n            maxInProperSuffix = true;\n            break;\n  \
        \      }\n    }\n\n    if (minInProperPrefix || maxInProperSuffix) {\n     \
        \   return 2;\n    }\n\n    return 3;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return Integer\n\
        \     */\n    function minOperations($s) {\n        $n = strlen($s);\n     \
        \   if ($n <= 1) return 0;\n\n        $isSorted = true;\n        $minChar =\
        \ $s[0];\n        $maxChar = $s[0];\n\n        for ($i = 1; $i < $n; $i++) {\n\
        \            if ($s[$i] < $s[$i - 1]) {\n                $isSorted = false;\n\
        \            }\n            if ($s[$i] < $minChar) {\n                $minChar\
        \ = $s[$i];\n            }\n            if ($s[$i] > $maxChar) {\n         \
        \       $maxChar = $s[$i];\n            }\n        }\n\n        if ($isSorted)\
        \ return 0;\n        if ($n == 2) return -1;\n\n        if ($s[0] == $minChar\
        \ || $s[$n - 1] == $maxChar) {\n            return 1;\n        }\n\n       \
        \ $minInProperPrefix = false;\n        for ($i = 0; $i < $n - 1; $i++) {\n \
        \           if ($s[$i] == $minChar) {\n                $minInProperPrefix =\
        \ true;\n                break;\n            }\n        }\n\n        $maxInProperSuffix\
        \ = false;\n        for ($i = 1; $i < $n; $i++) {\n            if ($s[$i] ==\
        \ $maxChar) {\n                $maxInProperSuffix = true;\n                break;\n\
        \            }\n        }\n\n        if ($minInProperPrefix || $maxInProperSuffix)\
        \ {\n            return 2;\n        }\n\n        return 3;\n    }\n}"
      swift: "class Solution {\n    func minOperations(_ s: String) -> Int {\n     \
        \   let chars = Array(s)\n        let n = chars.count\n        if n <= 1 { return\
        \ 0 }\n\n        var isSorted = true\n        var minChar = chars[0]\n     \
        \   var maxChar = chars[0]\n\n        for i in 1..<n {\n            if chars[i]\
        \ < chars[i - 1] {\n                isSorted = false\n            }\n      \
        \      if chars[i] < minChar {\n                minChar = chars[i]\n       \
        \     }\n            if chars[i] > maxChar {\n                maxChar = chars[i]\n\
        \            }\n        }\n\n        if isSorted { return 0 }\n        if n\
        \ == 2 { return -1 }\n\n        if chars[0] == minChar || chars[n - 1] == maxChar\
        \ {\n            return 1\n        }\n\n        var minInProperPrefix = false\n\
        \        for i in 0..<(n - 1) {\n            if chars[i] == minChar {\n    \
        \            minInProperPrefix = true\n                break\n            }\n\
        \        }\n\n        var maxInProperSuffix = false\n        for i in 1..<n\
        \ {\n            if chars[i] == maxChar {\n                maxInProperSuffix\
        \ = true\n                break\n            }\n        }\n\n        if minInProperPrefix\
        \ || maxInProperSuffix {\n            return 2\n        }\n\n        return\
        \ 3\n    }\n}"
      kotlin: "class Solution {\n    fun minOperations(s: String): Int {\n        val\
        \ n = s.length\n        val charArray = s.toCharArray()\n        val sortedS\
        \ = charArray.sortedArray()\n\n        var first = -1\n        var last = -1\n\
        \        for (k in 0 until n) {\n            if (s[k] != sortedS[k]) {\n   \
        \             if (first == -1) first = k\n                last = k\n       \
        \     }\n        }\n\n        if (first == -1) return 0\n        if (n == 2)\
        \ return -1\n        if (first > 0 || last < n - 1) return 1\n\n        val\
        \ mn = sortedS[0]\n        val mx = sortedS[n - 1]\n\n        var mnInPrefix\
        \ = false\n        for (k in 0 until n - 1) {\n            if (s[k] == mn) {\n\
        \                mnInPrefix = true\n                break\n            }\n \
        \       }\n\n        var mxInSuffix = false\n        for (k in 1 until n) {\n\
        \            if (s[k] == mx) {\n                mxInSuffix = true\n        \
        \        break\n            }\n        }\n\n        return if (mnInPrefix ||\
        \ mxInSuffix) 2 else 3\n    }\n}"
      dart: "class Solution {\n  int minOperations(String s) {\n    int n = s.length;\n\
        \    List<String> chars = s.split('');\n    chars.sort();\n    String sortedS\
        \ = chars.join('');\n\n    int first = -1;\n    int last = -1;\n    for (int\
        \ k = 0; k < n; k++) {\n      if (s[k] != sortedS[k]) {\n        if (first ==\
        \ -1) first = k;\n        last = k;\n      }\n    }\n\n    if (first == -1)\
        \ return 0;\n    if (n == 2) return -1;\n    if (first > 0 || last < n - 1)\
        \ return 1;\n\n    String mn = sortedS[0];\n    String mx = sortedS[n - 1];\n\
        \n    bool mnInPrefix = false;\n    for (int k = 0; k < n - 1; k++) {\n    \
        \  if (s[k] == mn) {\n        mnInPrefix = true;\n        break;\n      }\n\
        \    }\n\n    bool mxInSuffix = false;\n    for (int k = 1; k < n; k++) {\n\
        \      if (s[k] == mx) {\n        mxInSuffix = true;\n        break;\n     \
        \ }\n    }\n\n    return (mnInPrefix || mxInSuffix) ? 2 : 3;\n  }\n}"
      go: "import (\n\t\"sort\"\n)\n\nfunc minOperations(s string) int {\n\tn := len(s)\n\
        \tb := []byte(s)\n\tsortedB := make([]byte, n)\n\tcopy(sortedB, b)\n\tsort.Slice(sortedB,\
        \ func(i, j int) bool {\n\t\treturn sortedB[i] < sortedB[j]\n\t})\n\n\tfirst\
        \ := -1\n\tlast := -1\n\tfor i := 0; i < n; i++ {\n\t\tif b[i] != sortedB[i]\
        \ {\n\t\t\tif first == -1 {\n\t\t\t\tfirst = i\n\t\t\t}\n\t\t\tlast = i\n\t\t\
        }\n\t}\n\n\tif first == -1 {\n\t\treturn 0\n\t}\n\tif n == 2 {\n\t\treturn -1\n\
        \t}\n\tif first > 0 || last < n-1 {\n\t\treturn 1\n\t}\n\n\tmn := sortedB[0]\n\
        \tmx := sortedB[n-1]\n\n\tmnInPrefix := false\n\tfor i := 0; i < n-1; i++ {\n\
        \t\tif b[i] == mn {\n\t\t\tmnInPrefix = true\n\t\t\tbreak\n\t\t}\n\t}\n\n\t\
        mxInSuffix := false\n\tfor i := 1; i < n; i++ {\n\t\tif b[i] == mx {\n\t\t\t\
        mxInSuffix = true\n\t\t\tbreak\n\t\t}\n\t}\n\n\tif mnInPrefix || mxInSuffix\
        \ {\n\t\treturn 2\n\t}\n\treturn 3\n}"
      ruby: "# @param {String} s\n# @return {Integer}\ndef min_operations(s)\n  n =\
        \ s.length\n  sorted_s = s.chars.sort.join\n\n  first = -1\n  last = -1\n  (0...n).each\
        \ do |k|\n    if s[k] != sorted_s[k]\n      first = k if first == -1\n     \
        \ last = k\n    end\n  end\n\n  return 0 if first == -1\n  return -1 if n ==\
        \ 2\n  return 1 if first > 0 || last < n - 1\n\n  mn = sorted_s[0]\n  mx = sorted_s[-1]\n\
        \n  mn_in_prefix = false\n  (0...n - 1).each do |k|\n    if s[k] == mn\n   \
        \   mn_in_prefix = true\n      break\n    end\n  end\n\n  mx_in_suffix = false\n\
        \  (1...n).each do |k|\n    if s[k] == mx\n      mx_in_suffix = true\n     \
        \ break\n    end\n  end\n\n  return 2 if mn_in_prefix || mx_in_suffix\n  3\n\
        end"
      scala: "object Solution {\n    def minOperations(s: String): Int = {\n       \
        \ val n = s.length\n        val sortedS = s.sorted\n\n        var first = -1\n\
        \        var last = -1\n        for (k <- 0 until n) {\n            if (s(k)\
        \ != sortedS(k)) {\n                if (first == -1) first = k\n           \
        \     last = k\n            }\n        }\n\n        if (first == -1) return\
        \ 0\n        if (n == 2) return -1\n        if (first > 0 || last < n - 1) return\
        \ 1\n\n        val mn = sortedS(0)\n        val mx = sortedS(n - 1)\n\n    \
        \    var mnInPrefix = false\n        var i = 0\n        while (i < n - 1) {\n\
        \            if (s(i) == mn) mnInPrefix = true\n            i += 1\n       \
        \ }\n\n        var mxInSuffix = false\n        var j = 1\n        while (j <\
        \ n) {\n            if (s(j) == mx) mxInSuffix = true\n            j += 1\n\
        \        }\n\n        if (mnInPrefix || mxInSuffix) 2 else 3\n    }\n}"
      rust: "impl Solution {\n    pub fn min_operations(s: String) -> i32 {\n      \
        \  let chars = s.as_bytes();\n        let n = chars.len();\n\n        let mut\
        \ is_sorted = true;\n        for i in 0..n.saturating_sub(1) {\n           \
        \ if chars[i] > chars[i+1] {\n                is_sorted = false;\n         \
        \       break;\n            }\n        }\n\n        if is_sorted {\n       \
        \     return 0;\n        }\n\n        if n == 2 {\n            return -1;\n\
        \        }\n\n        let min_char = *chars.iter().min().unwrap();\n       \
        \ let max_char = *chars.iter().max().unwrap();\n\n        if chars[0] == min_char\
        \ || chars[n - 1] == max_char {\n            return 1;\n        }\n\n      \
        \  let min_in_prefix = chars[..n - 1].iter().any(|&c| c == min_char);\n    \
        \    let max_in_suffix = chars[1..].iter().any(|&c| c == max_char);\n\n    \
        \    if !min_in_prefix && !max_in_suffix {\n            3\n        } else {\n\
        \            2\n        }\n    }\n}"
      racket: "(define/contract (min-operations s)\n  (-> string? exact-integer?)\n\
        \  (let* ([chars (string->list s)]\n         [n (length chars)])\n    (letrec\
        \ ([is-sorted? (lambda (lst)\n                           (or (null? lst)\n \
        \                              (null? (cdr lst))\n                         \
        \      (and (char<=? (car lst) (cadr lst))\n                               \
        \     (is-sorted? (cdr lst)))))])\n      (if (is-sorted? chars)\n          0\n\
        \          (if (= n 2)\n              -1\n              (let* ([sorted-chars\
        \ (sort chars char<?)]\n                     [min-char (car sorted-chars)]\n\
        \                     [max-char (list-ref sorted-chars (- n 1))]\n         \
        \            [first-char (car chars)]\n                     [last-char (list-ref\
        \ chars (- n 1))])\n                (if (or (char=? first-char min-char)\n \
        \                       (char=? last-char max-char))\n                    1\n\
        \                    (let* ([prefix (take chars (- n 1))]\n                \
        \           [suffix (drop chars 1)]\n                           [min-in-prefix\
        \ (member min-char prefix)]\n                           [max-in-suffix (member\
        \ max-char suffix)])\n                      (if (and (not min-in-prefix) (not\
        \ max-in-suffix))\n                          3\n                          2)))))))))"
      erlang: "-spec min_operations(S :: unicode:unicode_binary()) -> integer().\nmin_operations(S)\
        \ ->\n  Chars = unicode:characters_to_list(S),\n  N = length(Chars),\n  Sorted\
        \ = lists:sort(Chars),\n  if\n    Chars == Sorted -> 0;\n    N == 2 -> -1;\n\
        \    true ->\n      MinChar = lists:min(Chars),\n      MaxChar = lists:max(Chars),\n\
        \      First = hd(Chars),\n      Last = lists:last(Chars),\n      if\n     \
        \   First == MinChar orelse Last == MaxChar -> 1;\n        true ->\n       \
        \   Prefix = lists:sublist(Chars, 1, N - 1),\n          Suffix = lists:sublist(Chars,\
        \ 2, N - 1),\n          MinInPrefix = lists:member(MinChar, Prefix),\n     \
        \     MaxInSuffix = lists:member(MaxChar, Suffix),\n          if\n         \
        \   (not MinInPrefix) andalso (not MaxInSuffix) -> 3;\n            true -> 2\n\
        \          end\n      end\n  end."
      elixir: "defmodule Solution do\n  @spec min_operations(s :: String.t) :: integer\n\
        \  def min_operations(s) do\n    chars = String.to_charlist(s)\n    n = length(chars)\n\
        \    sorted_chars = Enum.sort(chars)\n\n    cond do\n      chars == sorted_chars\
        \ -> 0\n      n == 2 -> -1\n      true ->\n        min_char = Enum.min(chars)\n\
        \        max_char = Enum.max(chars)\n        first_char = hd(chars)\n      \
        \  last_char = List.last(chars)\n\n        if first_char == min_char or last_char\
        \ == max_char do\n          1\n        else\n          prefix = Enum.slice(chars,\
        \ 0, n - 1)\n          suffix = Enum.slice(chars, 1, n - 1)\n          min_in_prefix\
        \ = Enum.member?(prefix, min_char)\n          max_in_suffix = Enum.member?(suffix,\
        \ max_char)\n\n          if not min_in_prefix and not max_in_suffix do\n   \
        \         3\n          else\n            2\n          end\n        end\n   \
        \ end\n  end\nend"
    approach: 'To find the minimum number of operations to sort the string $s$, we first
      observe the constraints and properties of the sorting operation. If the string
      is already sorted, the answer is 0. If the string has a length of 2 and is not
      sorted, it is impossible to sort it because only proper substrings (length 1 in
      this case) can be sorted, which results in no change; thus, we return -1. For
      strings of length $n \ge 3$, it is always possible to sort the string in at most
      3 operations by strategically moving the minimum character ($mn$) to the front
      and the maximum character ($mx$) to the back using proper substrings.


      The number of operations depends on the placement of $mn$ and $mx$. If $s[0] =
      mn$ or $s[n-1] = mx$, we can sort the entire string in 1 operation by sorting
      the proper substring that includes the unsorted portion (either $s[1\dots n-1]$
      or $s[0\dots n-2]$). If neither is true, we can achieve the goal in 2 operations
      if $mn$ exists anywhere in the proper prefix $s[0\dots n-2]$ or $mx$ exists anywhere
      in the proper suffix $s[1\dots n-1]$, allowing us to move one of them to an endpoint
      in the first step. If $mn$ only exists at the very end ($s[n-1]$) and $mx$ only
      exists at the very beginning ($s[0]$), then 3 operations are required.'
    time_complexity: O(N) where N is the length of the string. We iterate through the
      string a constant number of times to check if it is sorted, find the minimum and
      maximum characters, and check their occurrences in the proper prefix and suffix.
    space_complexity: O(1) beyond the input string. We only store a few character variables
      and boolean flags, regardless of the size of the input string.
    elapsed_time: 361.6459786891937
    model: gemini-3-flash-preview
    generated_at: '2026-10-21 02:50:47 '
---

## Problem #3863: Minimum Operations to Sort a String

**Difficulty:** Medium

**Topics:** String

## Problem Description

<p data-end="244" data-start="156">You are given a string <code>s</code> consisting of lowercase English letters.</p>

<p>In one operation, you can select any <strong><span data-keyword="substring-nonempty">substring</span></strong> of <code>s</code> that is <strong>not</strong> the entire string and <strong>sort</strong> it in <strong>non-descending alphabetical</strong> order.</p>

<p>Return the <strong>minimum</strong> number of operations required to make <code>s</code> sorted in <strong>non-descending</strong> order. If it is not possible, return -1.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;dog&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong>​​​​​​​</p>

<ul>
	<li>Sort substring <code>&quot;og&quot;</code> to <code>&quot;go&quot;</code>.</li>
	<li>Now, <code>s = &quot;dgo&quot;</code>, which is sorted in ascending order. Thus, the answer is 1.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;card&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Sort substring <code>&quot;car&quot;</code> to <code>&quot;acr&quot;</code>, so <code>s = &quot;acrd&quot;</code>.</li>
	<li>Sort substring <code>&quot;rd&quot;</code> to <code>&quot;dr&quot;</code>, making <code>s = &quot;acdr&quot;</code>, which is sorted in ascending order. Thus, the answer is 2.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;gf&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>It is impossible to sort <code>s</code> under the given constraints. Thus, the answer is -1.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
</ul>


## Hints

1. If `s` is already sorted, answer is `0`.

2. Let `mn` be the minimum char and `mx` be the maximum char; if `mn` appears at the beginning (not whole string) or `mx` appears at the end (not whole string), answer is `1`.

3. If `s` cannot be transformed into a sorted string, return `-1`.

4. If no `mn` exists in any proper prefix and no `mx` exists in any proper suffix, answer is `3`; otherwise answer is `2`

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To find the minimum number of operations to sort the string $s$, we first observe the constraints and properties of the sorting operation. If the string is already sorted, the answer is 0. If the string has a length of 2 and is not sorted, it is impossible to sort it because only proper substrings (length 1 in this case) can be sorted, which results in no change; thus, we return -1. For strings of length $n \ge 3$, it is always possible to sort the string in at most 3 operations by strategically moving the minimum character ($mn$) to the front and the maximum character ($mx$) to the back using proper substrings.

The number of operations depends on the placement of $mn$ and $mx$. If $s[0] = mn$ or $s[n-1] = mx$, we can sort the entire string in 1 operation by sorting the proper substring that includes the unsorted portion (either $s[1\dots n-1]$ or $s[0\dots n-2]$). If neither is true, we can achieve the goal in 2 operations if $mn$ exists anywhere in the proper prefix $s[0\dots n-2]$ or $mx$ exists anywhere in the proper suffix $s[1\dots n-1]$, allowing us to move one of them to an endpoint in the first step. If $mn$ only exists at the very end ($s[n-1]$) and $mx$ only exists at the very beginning ($s[0]$), then 3 operations are required.

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
    int minOperations(string s) {
        int n = s.length();
        if (n <= 1) return 0;

        bool sorted = true;
        for (int i = 0; i < n - 1; ++i) {
            if (s[i] > s[i + 1]) {
                sorted = false;
                break;
            }
        }
        if (sorted) return 0;
        if (n == 2) return -1;

        char mn = s[0], mx = s[0];
        for (char c : s) {
            if (c < mn) mn = c;
            if (c > mx) mx = c;
        }

        if (s[0] == mn || s[n - 1] == mx) return 1;

        bool mn_in_prefix = false;
        for (int i = 0; i < n - 1; ++i) {
            if (s[i] == mn) mn_in_prefix = true;
        }
        bool mx_in_suffix = false;
        for (int i = 1; i < n; ++i) {
            if (s[i] == mx) mx_in_suffix = true;
        }

        if (mn_in_prefix || mx_in_suffix) return 2;

        return 3;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.*;

class Solution {
    public int minOperations(String s) {
        int n = s.length();
        if (n <= 1) return 0;

        boolean sorted = true;
        for (int i = 0; i < n - 1; i++) {
            if (s.charAt(i) > s.charAt(i + 1)) {
                sorted = false;
                break;
            }
        }
        if (sorted) return 0;
        if (n == 2) return -1;

        char mn = s.charAt(0);
        char mx = s.charAt(0);
        for (int i = 1; i < n; i++) {
            char c = s.charAt(i);
            if (c < mn) mn = c;
            if (c > mx) mx = c;
        }

        if (s.charAt(0) == mn || s.charAt(n - 1) == mx) return 1;

        boolean mnInPrefix = false;
        for (int i = 0; i < n - 1; i++) {
            if (s.charAt(i) == mn) {
                mnInPrefix = true;
                break;
            }
        }
        boolean mxInSuffix = false;
        for (int i = 1; i < n; i++) {
            if (s.charAt(i) == mx) {
                mxInSuffix = true;
                break;
            }
        }

        if (mnInPrefix || mxInSuffix) return 2;

        return 3;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n <= 1:
            return 0

        is_sorted = True
        for i in range(n - 1):
            if s[i] > s[i+1]:
                is_sorted = False
                break
        if is_sorted:
            return 0
        if n == 2:
            return -1

        mn = min(s)
        mx = max(s)

        if s[0] == mn or s[n-1] == mx:
            return 1

        mn_in_prefix = any(s[i] == mn for i in range(n - 1))
        mx_in_suffix = any(s[i] == mx for i in range(1, n))

        if mn_in_prefix or mx_in_suffix:
            return 2

        return 3
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0

        is_sorted = True
        for i in range(n - 1):
            if s[i] > s[i+1]:
                is_sorted = False
                break
        if is_sorted:
            return 0
        if n == 2:
            return -1

        mn = min(s)
        mx = max(s)

        if s[0] == mn or s[n-1] == mx:
            return 1

        mn_in_prefix = any(s[i] == mn for i in range(n - 1))
        mx_in_suffix = any(s[i] == mx for i in range(1, n))

        if mn_in_prefix or mx_in_suffix:
            return 2

        return 3
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <string.h>
#include <stdbool.h>

int minOperations(char* s) {
    int n = strlen(s);
    if (n <= 1) return 0;

    bool is_sorted = true;
    for (int i = 0; i < n - 1; i++) {
        if (s[i] > s[i + 1]) {
            is_sorted = false;
            break;
        }
    }
    if (is_sorted) return 0;
    if (n == 2) return -1;

    char mn = s[0], mx = s[0];
    for (int i = 1; i < n; i++) {
        if (s[i] < mn) mn = s[i];
        if (s[i] > mx) mx = s[i];
    }

    if (s[0] == mn || s[n - 1] == mx) return 1;

    bool mn_in_prefix = false;
    for (int i = 0; i < n - 1; i++) {
        if (s[i] == mn) {
            mn_in_prefix = true;
            break;
        }
    }
    bool mx_in_suffix = false;
    for (int i = 1; i < n; i++) {
        if (s[i] == mx) {
            mx_in_suffix = true;
            break;
        }
    }

    if (mn_in_prefix || mx_in_suffix) return 2;

    return 3;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinOperations(string s) {
        int n = s.Length;
        if (n <= 1) return 0;

        bool isSorted = true;
        char minChar = s[0];
        char maxChar = s[0];

        for (int i = 1; i < n; i++) {
            if (s[i] < s[i - 1]) {
                isSorted = false;
            }
            if (s[i] < minChar) {
                minChar = s[i];
            }
            if (s[i] > maxChar) {
                maxChar = s[i];
            }
        }

        if (isSorted) return 0;
        if (n == 2) return -1;

        if (s[0] == minChar || s[n - 1] == maxChar) {
            return 1;
        }

        bool minInProperPrefix = false;
        for (int i = 0; i < n - 1; i++) {
            if (s[i] == minChar) {
                minInProperPrefix = true;
                break;
            }
        }

        bool maxInProperSuffix = false;
        for (int i = 1; i < n; i++) {
            if (s[i] == maxChar) {
                maxInProperSuffix = true;
                break;
            }
        }

        if (minInProperPrefix || maxInProperSuffix) {
            return 2;
        }

        return 3;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} s
 * @return {number}
 */
var minOperations = function(s) {
    const n = s.length;
    if (n <= 1) return 0;

    let isSorted = true;
    let minChar = s[0];
    let maxChar = s[0];

    for (let i = 1; i < n; i++) {
        if (s[i] < s[i - 1]) {
            isSorted = false;
        }
        if (s[i] < minChar) {
            minChar = s[i];
        }
        if (s[i] > maxChar) {
            maxChar = s[i];
        }
    }

    if (isSorted) return 0;
    if (n === 2) return -1;

    if (s[0] === minChar || s[n - 1] === maxChar) {
        return 1;
    }

    let minInProperPrefix = false;
    for (let i = 0; i < n - 1; i++) {
        if (s[i] === minChar) {
            minInProperPrefix = true;
            break;
        }
    }

    let maxInProperSuffix = false;
    for (let i = 1; i < n; i++) {
        if (s[i] === maxChar) {
            maxInProperSuffix = true;
            break;
        }
    }

    if (minInProperPrefix || maxInProperSuffix) {
        return 2;
    }

    return 3;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minOperations(s: string): number {
    const n: number = s.length;
    if (n <= 1) return 0;

    let isSorted: boolean = true;
    let minChar: string = s[0];
    let maxChar: string = s[0];

    for (let i = 1; i < n; i++) {
        if (s[i] < s[i - 1]) {
            isSorted = false;
        }
        if (s[i] < minChar) {
            minChar = s[i];
        }
        if (s[i] > maxChar) {
            maxChar = s[i];
        }
    }

    if (isSorted) return 0;
    if (n === 2) return -1;

    if (s[0] === minChar || s[n - 1] === maxChar) {
        return 1;
    }

    let minInProperPrefix: boolean = false;
    for (let i = 0; i < n - 1; i++) {
        if (s[i] === minChar) {
            minInProperPrefix = true;
            break;
        }
    }

    let maxInProperSuffix: boolean = false;
    for (let i = 1; i < n; i++) {
        if (s[i] === maxChar) {
            maxInProperSuffix = true;
            break;
        }
    }

    if (minInProperPrefix || maxInProperSuffix) {
        return 2;
    }

    return 3;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minOperations($s) {
        $n = strlen($s);
        if ($n <= 1) return 0;

        $isSorted = true;
        $minChar = $s[0];
        $maxChar = $s[0];

        for ($i = 1; $i < $n; $i++) {
            if ($s[$i] < $s[$i - 1]) {
                $isSorted = false;
            }
            if ($s[$i] < $minChar) {
                $minChar = $s[$i];
            }
            if ($s[$i] > $maxChar) {
                $maxChar = $s[$i];
            }
        }

        if ($isSorted) return 0;
        if ($n == 2) return -1;

        if ($s[0] == $minChar || $s[$n - 1] == $maxChar) {
            return 1;
        }

        $minInProperPrefix = false;
        for ($i = 0; $i < $n - 1; $i++) {
            if ($s[$i] == $minChar) {
                $minInProperPrefix = true;
                break;
            }
        }

        $maxInProperSuffix = false;
        for ($i = 1; $i < $n; $i++) {
            if ($s[$i] == $maxChar) {
                $maxInProperSuffix = true;
                break;
            }
        }

        if ($minInProperPrefix || $maxInProperSuffix) {
            return 2;
        }

        return 3;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minOperations(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        if n <= 1 { return 0 }

        var isSorted = true
        var minChar = chars[0]
        var maxChar = chars[0]

        for i in 1..<n {
            if chars[i] < chars[i - 1] {
                isSorted = false
            }
            if chars[i] < minChar {
                minChar = chars[i]
            }
            if chars[i] > maxChar {
                maxChar = chars[i]
            }
        }

        if isSorted { return 0 }
        if n == 2 { return -1 }

        if chars[0] == minChar || chars[n - 1] == maxChar {
            return 1
        }

        var minInProperPrefix = false
        for i in 0..<(n - 1) {
            if chars[i] == minChar {
                minInProperPrefix = true
                break
            }
        }

        var maxInProperSuffix = false
        for i in 1..<n {
            if chars[i] == maxChar {
                maxInProperSuffix = true
                break
            }
        }

        if minInProperPrefix || maxInProperSuffix {
            return 2
        }

        return 3
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minOperations(s: String): Int {
        val n = s.length
        val charArray = s.toCharArray()
        val sortedS = charArray.sortedArray()

        var first = -1
        var last = -1
        for (k in 0 until n) {
            if (s[k] != sortedS[k]) {
                if (first == -1) first = k
                last = k
            }
        }

        if (first == -1) return 0
        if (n == 2) return -1
        if (first > 0 || last < n - 1) return 1

        val mn = sortedS[0]
        val mx = sortedS[n - 1]

        var mnInPrefix = false
        for (k in 0 until n - 1) {
            if (s[k] == mn) {
                mnInPrefix = true
                break
            }
        }

        var mxInSuffix = false
        for (k in 1 until n) {
            if (s[k] == mx) {
                mxInSuffix = true
                break
            }
        }

        return if (mnInPrefix || mxInSuffix) 2 else 3
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minOperations(String s) {
    int n = s.length;
    List<String> chars = s.split('');
    chars.sort();
    String sortedS = chars.join('');

    int first = -1;
    int last = -1;
    for (int k = 0; k < n; k++) {
      if (s[k] != sortedS[k]) {
        if (first == -1) first = k;
        last = k;
      }
    }

    if (first == -1) return 0;
    if (n == 2) return -1;
    if (first > 0 || last < n - 1) return 1;

    String mn = sortedS[0];
    String mx = sortedS[n - 1];

    bool mnInPrefix = false;
    for (int k = 0; k < n - 1; k++) {
      if (s[k] == mn) {
        mnInPrefix = true;
        break;
      }
    }

    bool mxInSuffix = false;
    for (int k = 1; k < n; k++) {
      if (s[k] == mx) {
        mxInSuffix = true;
        break;
      }
    }

    return (mnInPrefix || mxInSuffix) ? 2 : 3;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import (
	"sort"
)

func minOperations(s string) int {
	n := len(s)
	b := []byte(s)
	sortedB := make([]byte, n)
	copy(sortedB, b)
	sort.Slice(sortedB, func(i, j int) bool {
		return sortedB[i] < sortedB[j]
	})

	first := -1
	last := -1
	for i := 0; i < n; i++ {
		if b[i] != sortedB[i] {
			if first == -1 {
				first = i
			}
			last = i
		}
	}

	if first == -1 {
		return 0
	}
	if n == 2 {
		return -1
	}
	if first > 0 || last < n-1 {
		return 1
	}

	mn := sortedB[0]
	mx := sortedB[n-1]

	mnInPrefix := false
	for i := 0; i < n-1; i++ {
		if b[i] == mn {
			mnInPrefix = true
			break
		}
	}

	mxInSuffix := false
	for i := 1; i < n; i++ {
		if b[i] == mx {
			mxInSuffix = true
			break
		}
	}

	if mnInPrefix || mxInSuffix {
		return 2
	}
	return 3
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @return {Integer}
def min_operations(s)
  n = s.length
  sorted_s = s.chars.sort.join

  first = -1
  last = -1
  (0...n).each do |k|
    if s[k] != sorted_s[k]
      first = k if first == -1
      last = k
    end
  end

  return 0 if first == -1
  return -1 if n == 2
  return 1 if first > 0 || last < n - 1

  mn = sorted_s[0]
  mx = sorted_s[-1]

  mn_in_prefix = false
  (0...n - 1).each do |k|
    if s[k] == mn
      mn_in_prefix = true
      break
    end
  end

  mx_in_suffix = false
  (1...n).each do |k|
    if s[k] == mx
      mx_in_suffix = true
      break
    end
  end

  return 2 if mn_in_prefix || mx_in_suffix
  3
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minOperations(s: String): Int = {
        val n = s.length
        val sortedS = s.sorted

        var first = -1
        var last = -1
        for (k <- 0 until n) {
            if (s(k) != sortedS(k)) {
                if (first == -1) first = k
                last = k
            }
        }

        if (first == -1) return 0
        if (n == 2) return -1
        if (first > 0 || last < n - 1) return 1

        val mn = sortedS(0)
        val mx = sortedS(n - 1)

        var mnInPrefix = false
        var i = 0
        while (i < n - 1) {
            if (s(i) == mn) mnInPrefix = true
            i += 1
        }

        var mxInSuffix = false
        var j = 1
        while (j < n) {
            if (s(j) == mx) mxInSuffix = true
            j += 1
        }

        if (mnInPrefix || mxInSuffix) 2 else 3
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_operations(s: String) -> i32 {
        let chars = s.as_bytes();
        let n = chars.len();

        let mut is_sorted = true;
        for i in 0..n.saturating_sub(1) {
            if chars[i] > chars[i+1] {
                is_sorted = false;
                break;
            }
        }

        if is_sorted {
            return 0;
        }

        if n == 2 {
            return -1;
        }

        let min_char = *chars.iter().min().unwrap();
        let max_char = *chars.iter().max().unwrap();

        if chars[0] == min_char || chars[n - 1] == max_char {
            return 1;
        }

        let min_in_prefix = chars[..n - 1].iter().any(|&c| c == min_char);
        let max_in_suffix = chars[1..].iter().any(|&c| c == max_char);

        if !min_in_prefix && !max_in_suffix {
            3
        } else {
            2
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-operations s)
  (-> string? exact-integer?)
  (let* ([chars (string->list s)]
         [n (length chars)])
    (letrec ([is-sorted? (lambda (lst)
                           (or (null? lst)
                               (null? (cdr lst))
                               (and (char<=? (car lst) (cadr lst))
                                    (is-sorted? (cdr lst)))))])
      (if (is-sorted? chars)
          0
          (if (= n 2)
              -1
              (let* ([sorted-chars (sort chars char<?)]
                     [min-char (car sorted-chars)]
                     [max-char (list-ref sorted-chars (- n 1))]
                     [first-char (car chars)]
                     [last-char (list-ref chars (- n 1))])
                (if (or (char=? first-char min-char)
                        (char=? last-char max-char))
                    1
                    (let* ([prefix (take chars (- n 1))]
                           [suffix (drop chars 1)]
                           [min-in-prefix (member min-char prefix)]
                           [max-in-suffix (member max-char suffix)])
                      (if (and (not min-in-prefix) (not max-in-suffix))
                          3
                          2)))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_operations(S :: unicode:unicode_binary()) -> integer().
min_operations(S) ->
  Chars = unicode:characters_to_list(S),
  N = length(Chars),
  Sorted = lists:sort(Chars),
  if
    Chars == Sorted -> 0;
    N == 2 -> -1;
    true ->
      MinChar = lists:min(Chars),
      MaxChar = lists:max(Chars),
      First = hd(Chars),
      Last = lists:last(Chars),
      if
        First == MinChar orelse Last == MaxChar -> 1;
        true ->
          Prefix = lists:sublist(Chars, 1, N - 1),
          Suffix = lists:sublist(Chars, 2, N - 1),
          MinInPrefix = lists:member(MinChar, Prefix),
          MaxInSuffix = lists:member(MaxChar, Suffix),
          if
            (not MinInPrefix) andalso (not MaxInSuffix) -> 3;
            true -> 2
          end
      end
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_operations(s :: String.t) :: integer
  def min_operations(s) do
    chars = String.to_charlist(s)
    n = length(chars)
    sorted_chars = Enum.sort(chars)

    cond do
      chars == sorted_chars -> 0
      n == 2 -> -1
      true ->
        min_char = Enum.min(chars)
        max_char = Enum.max(chars)
        first_char = hd(chars)
        last_char = List.last(chars)

        if first_char == min_char or last_char == max_char do
          1
        else
          prefix = Enum.slice(chars, 0, n - 1)
          suffix = Enum.slice(chars, 1, n - 1)
          min_in_prefix = Enum.member?(prefix, min_char)
          max_in_suffix = Enum.member?(suffix, max_char)

          if not min_in_prefix and not max_in_suffix do
            3
          else
            2
          end
        end
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) where N is the length of the string. We iterate through the string a constant number of times to check if it is sorted, find the minimum and maximum characters, and check their occurrences in the proper prefix and suffix.
- **Space Complexity:** O(1) beyond the input string. We only store a few character variables and boolean flags, regardless of the size of the input string.
