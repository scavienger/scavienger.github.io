---
layout: post
title: "Maximum Number of Operations to Move Ones to the End"
date: 2025-11-13 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Greedy", "Counting"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxOperations(string s) {\n        long\
        \ long totalOperations = 0;\n        int onesCount = 0;\n        int n = s.length();\n\
        \n        for (int i = 0; i < n - 1; ++i) {\n            if (s[i] == '1') {\n\
        \                onesCount++;\n            }\n            // If we find a '10'\
        \ pattern, it means the '1' at s[i] can move past s[i+1].\n            // All\
        \ 'onesCount' '1's currently to the left of s[i+1] (including s[i])\n      \
        \      // will eventually need to move past this '0' position.\n           \
        \ // Each such move contributes one operation.\n            if (s[i] == '1'\
        \ && s[i+1] == '0') {\n                totalOperations += onesCount;\n     \
        \       }\n        }\n        // The last character s[n-1] cannot be s[i] in\
        \ a '10' pattern,\n        // so it only contributes to onesCount if it's a\
        \ '1', but doesn't trigger operations.\n        // The loop correctly handles\
        \ this by going up to n-2.\n\n        return totalOperations;\n    }\n};"
      java: "class Solution {\n    public int maxOperations(String s) {\n        long\
        \ totalOperations = 0;\n        int onesCount = 0;\n        int n = s.length();\n\
        \n        for (int i = 0; i < n - 1; ++i) {\n            if (s.charAt(i) ==\
        \ '1') {\n                onesCount++;\n            }\n            // If we\
        \ find a '10' pattern, it means the '1' at s[i] can move past s[i+1].\n    \
        \        // All 'onesCount' '1's currently to the left of s[i+1] (including\
        \ s[i])\n            // will eventually need to move past this '0' position.\n\
        \            // Each such move contributes one operation.\n            if (s.charAt(i)\
        \ == '1' && s.charAt(i+1) == '0') {\n                totalOperations += onesCount;\n\
        \            }\n        }\n        // The last character s[n-1] cannot be s[i]\
        \ in a '10' pattern,\n        // so it only contributes to onesCount if it's\
        \ a '1', but doesn't trigger operations.\n        // The loop correctly handles\
        \ this by going up to n-2.\n\n        return (int) totalOperations;\n    }\n\
        }"
      python: "class Solution:\n    def maxOperations(self, s: str) -> int:\n      \
        \  total_operations = 0\n        ones_count = 0\n        n = len(s)\n\n    \
        \    for i in range(n - 1):\n            if s[i] == '1':\n                ones_count\
        \ += 1\n            # If we find a '10' pattern, it means the '1' at s[i] can\
        \ move past s[i+1].\n            # All 'ones_count' '1's currently to the left\
        \ of s[i+1] (including s[i])\n            # will eventually need to move past\
        \ this '0' position.\n            # Each such move contributes one operation.\n\
        \            if s[i] == '1' and s[i+1] == '0':\n                total_operations\
        \ += ones_count\n\n        # The last character s[n-1] cannot be s[i] in a '10'\
        \ pattern,\n        # so it only contributes to ones_count if it's a '1', but\
        \ doesn't trigger operations.\n        # The loop correctly handles this by\
        \ going up to n-2.\n\n        return total_operations"
      python3: "class Solution:\n    def maxOperations(self, s: str) -> int:\n     \
        \   total_operations = 0\n        ones_count = 0\n        n = len(s)\n\n   \
        \     for i in range(n - 1):\n            if s[i] == '1':\n                ones_count\
        \ += 1\n            # If we find a '10' pattern, it means the '1' at s[i] can\
        \ move past s[i+1].\n            # All 'ones_count' '1's currently to the left\
        \ of s[i+1] (including s[i])\n            # will eventually need to move past\
        \ this '0' position.\n            # Each such move contributes one operation.\n\
        \            if s[i] == '1' and s[i+1] == '0':\n                total_operations\
        \ += ones_count\n\n        # The last character s[n-1] cannot be s[i] in a '10'\
        \ pattern,\n        # so it only contributes to ones_count if it's a '1', but\
        \ doesn't trigger operations.\n        # The loop correctly handles this by\
        \ going up to n-2.\n\n        return total_operations"
      c: "#include <string.h>\n\nint maxOperations(char * s){\n    long long totalOperations\
        \ = 0;\n    int onesCount = 0;\n    int n = strlen(s);\n\n    for (int i = 0;\
        \ i < n - 1; ++i) {\n        if (s[i] == '1') {\n            onesCount++;\n\
        \        }\n        // If we find a '10' pattern, it means the '1' at s[i] can\
        \ move past s[i+1].\n        // All 'onesCount' '1's currently to the left of\
        \ s[i+1] (including s[i])\n        // will eventually need to move past this\
        \ '0' position.\n        // Each such move contributes one operation.\n    \
        \    if (s[i] == '1' && s[i+1] == '0') {\n            totalOperations += onesCount;\n\
        \        }\n    }\n    // The last character s[n-1] cannot be s[i] in a '10'\
        \ pattern,\n    // so it only contributes to onesCount if it's a '1', but doesn't\
        \ trigger operations.\n    // The loop correctly handles this by going up to\
        \ n-2.\n\n    return (int) totalOperations;\n}"
      csharp: "public class Solution {\n    public int MaxOperations(string s) {\n \
        \       long totalOperations = 0;\n        int onesCount = 0;\n        int n\
        \ = s.Length;\n\n        for (int i = 0; i < n - 1; ++i) {\n            if (s[i]\
        \ == '1') {\n                onesCount++;\n            }\n            // If\
        \ we find a '10' pattern, it means the '1' at s[i] can move past s[i+1].\n \
        \           // All 'onesCount' '1's currently to the left of s[i+1] (including\
        \ s[i])\n            // will eventually need to move past this '0' position.\n\
        \            // Each such move contributes one operation.\n            if (s[i]\
        \ == '1' && s[i+1] == '0') {\n                totalOperations += onesCount;\n\
        \            }\n        }\n        // The last character s[n-1] cannot be s[i]\
        \ in a '10' pattern,\n        // so it only contributes to onesCount if it's\
        \ a '1', but doesn't trigger operations.\n        // The loop correctly handles\
        \ this by going up to n-2.\n\n        return (int) totalOperations;\n    }\n\
        }"
      javascript: "/**\n * @param {string} s\n * @return {number}\n */\nvar maxOperations\
        \ = function(s) {\n    let totalOperations = 0;\n    let onesCount = 0;\n  \
        \  const n = s.length;\n\n    for (let i = 0; i < n - 1; ++i) {\n        if\
        \ (s[i] === '1') {\n            onesCount++;\n        }\n        // If we find\
        \ a '10' pattern, it means the '1' at s[i] can move past s[i+1].\n        //\
        \ All 'onesCount' '1's currently to the left of s[i+1] (including s[i])\n  \
        \      // will eventually need to move past this '0' position.\n        // Each\
        \ such move contributes one operation.\n        if (s[i] === '1' && s[i+1] ===\
        \ '0') {\n            totalOperations += onesCount;\n        }\n    }\n    //\
        \ The last character s[n-1] cannot be s[i] in a '10' pattern,\n    // so it\
        \ only contributes to onesCount if it's a '1', but doesn't trigger operations.\n\
        \    // The loop correctly handles this by going up to n-2.\n\n    return totalOperations;\n\
        };"
      typescript: "function maxOperations(s: string): number {\n    let totalOperations:\
        \ number = 0;\n    let onesCount: number = 0;\n    const n: number = s.length;\n\
        \n    for (let i = 0; i < n - 1; ++i) {\n        if (s[i] === '1') {\n     \
        \       onesCount++;\n        }\n        // If we find a '10' pattern, it means\
        \ the '1' at s[i] can move past s[i+1].\n        // All 'onesCount' '1's currently\
        \ to the left of s[i+1] (including s[i])\n        // will eventually need to\
        \ move past this '0' position.\n        // Each such move contributes one operation.\n\
        \        if (s[i] === '1' && s[i+1] === '0') {\n            totalOperations\
        \ += onesCount;\n        }\n    }\n    // The last character s[n-1] cannot be\
        \ s[i] in a '10' pattern,\n    // so it only contributes to onesCount if it's\
        \ a '1', but doesn't trigger operations.\n    // The loop correctly handles\
        \ this by going up to n-2.\n\n    return totalOperations;\n}"
      php: "class Solution {\n    /**\n     * @param String $s\n     * @return Integer\n\
        \     */\n    function maxOperations($s) {\n        $totalOperations = 0;\n\
        \        $onesCount = 0;\n        $n = strlen($s);\n\n        for ($i = 0; $i\
        \ < $n - 1; ++$i) {\n            if ($s[$i] == '1') {\n                $onesCount++;\n\
        \            }\n            // If we find a '10' pattern, it means the '1' at\
        \ s[i] can move past s[i+1].\n            // All 'onesCount' '1's currently\
        \ to the left of s[i+1] (including s[i])\n            // will eventually need\
        \ to move past this '0' position.\n            // Each such move contributes\
        \ one operation.\n            if ($s[$i] == '1' && $s[$i+1] == '0') {\n    \
        \            $totalOperations += $onesCount;\n            }\n        }\n   \
        \     // The last character s[n-1] cannot be s[i] in a '10' pattern,\n     \
        \   // so it only contributes to onesCount if it's a '1', but doesn't trigger\
        \ operations.\n        // The loop correctly handles this by going up to n-2.\n\
        \n        return $totalOperations;\n    }\n}"
      swift: "class Solution {\n    func maxOperations(_ s: String) -> Int {\n     \
        \   var totalOperations: Int = 0\n        var onesCount: Int = 0\n        let\
        \ n: Int = s.count\n        let sChars = Array(s)\n\n        for i in 0..<n\
        \ - 1 {\n            if sChars[i] == \"1\" {\n                onesCount += 1\n\
        \            }\n            // If we find a '10' pattern, it means the '1' at\
        \ sChars[i] can move past sChars[i+1].\n            // All 'onesCount' '1's\
        \ currently to the left of sChars[i+1] (including sChars[i])\n            //\
        \ will eventually need to move past this '0' position.\n            // Each\
        \ such move contributes one operation.\n            if sChars[i] == \"1\" &&\
        \ sChars[i+1] == \"0\" {\n                totalOperations += onesCount\n   \
        \         }\n        }\n        // The last character sChars[n-1] cannot be\
        \ sChars[i] in a '10' pattern,\n        // so it only contributes to onesCount\
        \ if it's a '1', but doesn't trigger operations.\n        // The loop correctly\
        \ handles this by going up to n-2.\n\n        return totalOperations\n    }\n\
        }"
      kotlin: "class Solution {\n    fun maxOperations(s: String): Int {\n        var\
        \ totalOperations: Long = 0\n        var onesCount: Int = 0\n        val n:\
        \ Int = s.length\n\n        for (i in 0 until n - 1) {\n            if (s[i]\
        \ == '1') {\n                onesCount++\n            }\n            // If we\
        \ find a '10' pattern, it means the '1' at s[i] can move past s[i+1].\n    \
        \        // All 'onesCount' '1's currently to the left of s[i+1] (including\
        \ s[i])\n            // will eventually need to move past this '0' position.\n\
        \            // Each such move contributes one operation.\n            if (s[i]\
        \ == '1' && s[i+1] == '0') {\n                totalOperations += onesCount\n\
        \            }\n        }\n        // The last character s[n-1] cannot be s[i]\
        \ in a '10' pattern,\n        // so it only contributes to onesCount if it's\
        \ a '1', but doesn't trigger operations.\n        // The loop correctly handles\
        \ this by going up to n-2.\n\n        return totalOperations.toInt()\n    }\n\
        }"
      dart: "class Solution {\n  int maxOperations(String s) {\n    int totalOperations\
        \ = 0;\n    int onesCount = 0;\n    int n = s.length;\n\n    for (int i = 0;\
        \ i < n - 1; ++i) {\n      if (s[i] == '1') {\n        onesCount++;\n      }\n\
        \      // If we find a '10' pattern, it means the '1' at s[i] can move past\
        \ s[i+1].\n      // All 'onesCount' '1's currently to the left of s[i+1] (including\
        \ s[i])\n      // will eventually need to move past this '0' position.\n   \
        \   // Each such move contributes one operation.\n      if (s[i] == '1' && s[i+1]\
        \ == '0') {\n        totalOperations += onesCount;\n      }\n    }\n    // The\
        \ last character s[n-1] cannot be s[i] in a '10' pattern,\n    // so it only\
        \ contributes to onesCount if it's a '1', but doesn't trigger operations.\n\
        \    // The loop correctly handles this by going up to n-2.\n\n    return totalOperations;\n\
        \  }\n}"
      go: "func maxOperations(s string) int {\n    var totalOperations int = 0\n   \
        \ var onesCount int = 0\n    n := len(s)\n\n    for i := 0; i < n - 1; i++ {\n\
        \        if s[i] == '1' {\n            onesCount++\n        }\n        // If\
        \ we find a '10' pattern, it means the '1' at s[i] can move past s[i+1].\n \
        \       // All 'onesCount' '1's currently to the left of s[i+1] (including s[i])\n\
        \        // will eventually need to move past this '0' position.\n        //\
        \ Each such move contributes one operation.\n        if s[i] == '1' && s[i+1]\
        \ == '0' {\n            totalOperations += onesCount\n        }\n    }\n   \
        \ // The last character s[n-1] cannot be s[i] in a '10' pattern,\n    // so\
        \ it only contributes to onesCount if it's a '1', but doesn't trigger operations.\n\
        \    // The loop correctly handles this by going up to n-2.\n\n    return totalOperations\n\
        }"
      ruby: "class Solution\n    # @param {String} s\n    # @return {Integer}\n    def\
        \ max_operations(s)\n        total_operations = 0\n        ones_count = 0\n\
        \        n = s.length\n\n        (0...n - 1).each do |i|\n            if s[i]\
        \ == '1'\n                ones_count += 1\n            end\n            # If\
        \ we find a '10' pattern, it means the '1' at s[i] can move past s[i+1].\n \
        \           # All 'ones_count' '1's currently to the left of s[i+1] (including\
        \ s[i])\n            # will eventually need to move past this '0' position.\n\
        \            # Each such move contributes one operation.\n            if s[i]\
        \ == '1' && s[i+1] == '0'\n                total_operations += ones_count\n\
        \            end\n        end\n        # The last character s[n-1] cannot be\
        \ s[i] in a '10' pattern,\n        # so it only contributes to ones_count if\
        \ it's a '1', but doesn't trigger operations.\n        # The loop correctly\
        \ handles this by going up to n-2.\n\n        total_operations\n    end\nend"
      scala: "object Solution {\n    def maxOperations(s: String): Int = {\n       \
        \ var totalOperations: Long = 0\n        var onesCount: Int = 0\n        val\
        \ n: Int = s.length\n\n        for (i <- 0 until n - 1) {\n            if (s(i)\
        \ == '1') {\n                onesCount += 1\n            }\n            // If\
        \ we find a '10' pattern, it means the '1' at s(i) can move past s(i+1).\n \
        \           // All 'onesCount' '1's currently to the left of s(i+1) (including\
        \ s(i))\n            // will eventually need to move past this '0' position.\n\
        \            // Each such move contributes one operation.\n            if (s(i)\
        \ == '1' && s(i+1) == '0') {\n                totalOperations += onesCount\n\
        \            }\n        }\n        // The last character s(n-1) cannot be s(i)\
        \ in a '10' pattern,\n        // so it only contributes to onesCount if it's\
        \ a '1', but doesn't trigger operations.\n        // The loop correctly handles\
        \ this by going up to n-2.\n\n        totalOperations.toInt\n    }\n}"
      rust: "impl Solution {\n    pub fn max_operations(s: String) -> i32 {\n      \
        \  let mut total_operations: i32 = 0;\n        let mut ones_count: i32 = 0;\n\
        \        let n = s.len();\n        let s_chars: Vec<char> = s.chars().collect();\n\
        \n        for i in 0..n - 1 {\n            if s_chars[i] == '1' {\n        \
        \        ones_count += 1;\n            }\n            // If we find a '10' pattern,\
        \ it means the '1' at s_chars[i] can move past s_chars[i+1].\n            //\
        \ All 'ones_count' '1's currently to the left of s_chars[i+1] (including s_chars[i])\n\
        \            // will eventually need to move past this '0' position.\n     \
        \       // Each such move contributes one operation.\n            if s_chars[i]\
        \ == '1' && s_chars[i+1] == '0' {\n                total_operations += ones_count;\n\
        \            }\n        }\n        // The last character s_chars[n-1] cannot\
        \ be s_chars[i] in a '10' pattern,\n        // so it only contributes to ones_count\
        \ if it's a '1', but doesn't trigger operations.\n        // The loop correctly\
        \ handles this by going up to n-2.\n\n        total_operations\n    }\n}"
      racket: "#lang racket\n\n(define/contract (max-operations s)\n  (-> string? integer?)\n\
        \  (let* ((n (string-length s))\n         (total-operations 0)\n         (ones-count\
        \ 0))\n    (for ([i (in-range (- n 1))])\n      (when (char=? (string-ref s\
        \ i) #\\1)\n        (set! ones-count (+ ones-count 1)))\n      ;; If we find\
        \ a '10' pattern, it means the '1' at s[i] can move past s[i+1].\n      ;; All\
        \ 'ones-count' '1's currently to the left of s[i+1] (including s[i])\n     \
        \ ;; will eventually need to move past this '0' position.\n      ;; Each such\
        \ move contributes one operation.\n      (when (and (char=? (string-ref s i)\
        \ #\\1) (char=? (string-ref s (+ i 1)) #\\0))\n        (set! total-operations\
        \ (+ total-operations ones-count))))\n    ;; The last character s[n-1] cannot\
        \ be s[i] in a '10' pattern,\n    ;; so it only contributes to ones-count if\
        \ it's a '1', but doesn't trigger operations.\n    ;; The loop correctly handles\
        \ this by going up to n-2.\n    total-operations))"
      erlang: "-module(solution).\n-export([max_operations/1]).\n\nmax_operations(S)\
        \ ->\n    N = length(S),\n    max_operations_recursive(S, N, 0, 0, 0).\n\nmax_operations_recursive(S,\
        \ N, Index, OnesCount, TotalOperations) when Index < N - 1 ->\n    CharI = lists:nth(Index\
        \ + 1, S), % Erlang lists are 1-indexed, so Index + 1 for 0-indexed 'Index'\n\
        \    CharIPlus1 = lists:nth(Index + 2, S), % Index + 2 for 0-indexed 'Index\
        \ + 1'\n\n    NewOnesCount = if\n        CharI == $1 -> OnesCount + 1;\n   \
        \     true -> OnesCount\n    end,\n\n    NewTotalOperations = if\n        CharI\
        \ == $1 andalso CharIPlus1 == $0 -> TotalOperations + NewOnesCount;\n      \
        \  true -> TotalOperations\n    end,\n\n    max_operations_recursive(S, N, Index\
        \ + 1, NewOnesCount, NewTotalOperations);\nmax_operations_recursive(_S, _N,\
        \ _Index, _OnesCount, TotalOperations) ->\n    TotalOperations."
      elixir: "defmodule Solution do\n  @spec max_operations(s :: String.t) :: integer\n\
        \  def max_operations(s) do\n    n = String.length(s)\n    s_chars = String.to_charlist(s)\n\
        \n    Enum.reduce(0..(n - 2), {0, 0}, fn i, {ones_count, total_operations} ->\n\
        \      char_i = Enum.at(s_chars, i)\n      char_i_plus_1 = Enum.at(s_chars,\
        \ i + 1)\n\n      new_ones_count = if char_i == ?1, do: ones_count + 1, else:\
        \ ones_count\n\n      new_total_operations = if char_i == ?1 and char_i_plus_1\
        \ == ?0 do\n        total_operations + new_ones_count\n      else\n        total_operations\n\
        \      end\n\n      {new_ones_count, new_total_operations}\n    end)\n    |>\
        \ elem(1) # Return total_operations\n  end\nend"
    approach: 'The problem asks us to find the maximum number of operations to move
      all ''1''s to the end of a binary string. An operation consists of choosing an
      index `i` where `s[i] == ''1''` and `s[i+1] == ''0''`, and then moving `s[i]`
      to the right until it hits another ''1'' or the end of the string. This entire
      movement counts as a single operation.


      The key insight comes from observing the nature of the operation and the example.
      When a ''1'' at `s[i]` moves past a ''0'' at `s[i+1]`, it effectively swaps places
      with that ''0'' (and any subsequent ''0''s until another ''1'' is encountered).
      The crucial point is that the relative order of ''1''s in the string never changes.
      If `1_A` is initially to the left of `1_B`, `1_A` will always remain to the left
      of `1_B` throughout any operations. This means that if a ''1'' needs to pass a
      ''0'', any ''1'' to its left will also eventually need to pass that same ''0''
      position.


      We can solve this problem with a single pass through the string. We maintain a
      `ones_count` variable, which tracks the number of ''1''s encountered so far from
      the beginning of the string up to the current character `s[i]`. We iterate from
      `i = 0` to `len(s) - 2`. If `s[i]` is a ''1'', we increment `ones_count`. If we
      then find a `10` pattern (i.e., `s[i] == ''1''` and `s[i+1] == ''0''`), it signifies
      that an operation can be performed. At this point, the ''1'' at `s[i]` can move
      past the ''0'' at `s[i+1]`. Since all `ones_count` ''1''s (including `s[i]` itself
      and all ''1''s to its left) will eventually need to move past this specific ''0''
      position (`s[i+1]`) to reach the end of the string, each of these `ones_count`
      ''1''s will contribute one operation involving this ''0'' position. Therefore,
      we add the current `ones_count` to our `total_operations`. This greedy strategy,
      as suggested by the hints, correctly counts the maximum number of operations.'
    time_complexity: O(N) with detailed explanation. The algorithm iterates through
      the string once from left to right. In each step, it performs constant time operations
      (character comparison, incrementing counters). Therefore, the total time complexity
      is directly proportional to the length of the string, N.
    space_complexity: O(1) with detailed explanation. The algorithm uses a few integer
      variables (`total_operations`, `ones_count`, `n`, `i`) to store state, regardless
      of the input string's length. No auxiliary data structures that grow with N are
      used. For languages that convert the string to a character array (like Swift or
      Rust), this might incur O(N) space for the array, but it's typically considered
      part of the input representation or constant auxiliary space if the string is
      already in an iterable form.
    elapsed_time: 119.60451412200928
    model: gemini-2.5-flash
    generated_at: '2025-11-24 20:34:58 '
  - solutions:
      cpp: "#include <string>\nclass Solution {\npublic:\n    int maxOperations(std::string\
        \ s) {\n        int count = 0;\n        for (int i = 0; i < s.length() - 1;\
        \ i++) {\n            if (s[i] == '1' && s[i + 1] == '0') {\n              \
        \  count++;\n                for (int j = i + 1; j < s.length() - 1; j++) {\n\
        \                    if (s[j] == '0' && s[j + 1] == '1') {\n               \
        \         break;\n                    }\n                    if (s[j] == '1')\
        \ {\n                        break;\n                    }\n               \
        \ }\n            }\n        }\n        return count;\n    }\n}"
      java: "public class Solution {\n    public int maxOperations(String s) {\n   \
        \     int count = 0;\n        for (int i = 0; i < s.length() - 1; i++) {\n \
        \           if (s.charAt(i) == '1' && s.charAt(i + 1) == '0') {\n          \
        \      count++;\n                for (int j = i + 1; j < s.length() - 1; j++)\
        \ {\n                    if (s.charAt(j) == '0' && j + 1 < s.length() && s.charAt(j\
        \ + 1) == '1') {\n                        break;\n                    }\n  \
        \                  if (s.charAt(j) == '1') {\n                        break;\n\
        \                    }\n                }\n            }\n        }\n      \
        \  return count;\n    }\n}"
      python: "class Solution:\n    def maxOperations(self, s: str) -> int:\n      \
        \  count = 0\n        for i in range(len(s) - 1):\n            if s[i] == '1'\
        \ and s[i + 1] == '0':\n                count += 1\n                for j in\
        \ range(i + 1, len(s) - 1):\n                    if s[j] == '0' and j + 1 <\
        \ len(s) and s[j + 1] == '1':\n                        break\n             \
        \       if s[j] == '1':\n                        break\n        return count"
      python3: "class Solution:\n    def maxOperations(self, s: str) -> int:\n     \
        \   count = 0\n        for i in range(len(s) - 1):\n            if s[i] == '1'\
        \ and s[i + 1] == '0':\n                count += 1\n                for j in\
        \ range(i + 1, len(s) - 1):\n                    if s[j] == '0' and j + 1 <\
        \ len(s) and s[j + 1] == '1':\n                        break\n             \
        \       if s[j] == '1':\n                        break\n        return count"
      c: "#include <stdio.h>\n#include <string.h>\n\nint maxOperations(char * s){\n\
        \    int count = 0;\n    for (int i = 0; i < strlen(s) - 1; i++) {\n       \
        \ if (s[i] == '1' && s[i + 1] == '0') {\n            count++;\n            for\
        \ (int j = i + 1; j < strlen(s) - 1; j++) {\n                if (s[j] == '0'\
        \ && j + 1 < strlen(s) && s[j + 1] == '1') {\n                    break;\n \
        \               }\n                if (s[j] == '1') {\n                    break;\n\
        \                }\n            }\n        }\n    }\n    return count;\n}"
      csharp: "public class Solution {\n    public int MaxOperations(string s) {\n \
        \       int count = 0;\n        for (int i = 0; i < s.Length - 1; i++) {\n \
        \           if (s[i] == '1' && s[i + 1] == '0') {\n                count++;\n\
        \                for (int j = i + 1; j < s.Length - 1; j++) {\n            \
        \        if (s[j] == '0' && j + 1 < s.Length && s[j + 1] == '1') {\n       \
        \                 break;\n                    }\n                    if (s[j]\
        \ == '1') {\n                        break;\n                    }\n       \
        \         }\n            }\n        }\n        return count;\n    }\n}"
      javascript: "var maxOperations = function(s) {\n    let count = 0;\n    for (let\
        \ i = 0; i < s.length - 1; i++) {\n        if (s[i] === '1' && s[i + 1] ===\
        \ '0') {\n            count++;\n            for (let j = i + 1; j < s.length\
        \ - 1; j++) {\n                if (s[j] === '0' && j + 1 < s.length && s[j +\
        \ 1] === '1') {\n                    break;\n                }\n           \
        \     if (s[j] === '1') {\n                    break;\n                }\n \
        \           }\n        }\n    }\n    return count;\n};"
      typescript: "function maxOperations(s: string): number {\n    let count: number\
        \ = 0;\n    for (let i: number = 0; i < s.length - 1; i++) {\n        if (s[i]\
        \ === '1' && s[i + 1] === '0') {\n            count++;\n            for (let\
        \ j: number = i + 1; j < s.length - 1; j++) {\n                if (s[j] ===\
        \ '0' && j + 1 < s.length && s[j + 1] === '1') {\n                    break;\n\
        \                }\n                if (s[j] === '1') {\n                  \
        \  break;\n                }\n            }\n        }\n    }\n    return count;\n\
        }"
      php: "class Solution {\n    function maxOperations($s) {\n        $count = 0;\n\
        \        for ($i = 0; $i < strlen($s) - 1; $i++) {\n            if ($s[$i] ==\
        \ '1' && $s[$i + 1] == '0') {\n                $count++;\n                for\
        \ ($j = $i + 1; $j < strlen($s) - 1; $j++) {\n                    if ($s[$j]\
        \ == '0' && $j + 1 < strlen($s) && $s[$j + 1] == '1') {\n                  \
        \      break;\n                    }\n                    if ($s[$j] == '1')\
        \ {\n                        break;\n                    }\n               \
        \ }\n            }\n        }\n        return $count;\n    }\n}"
      swift: "class Solution {\n    func maxOperations(_ s: String) -> Int {\n     \
        \   var count = 0\n        let sArray = Array(s)\n        for i in 0..<sArray.count\
        \ - 1 {\n            if sArray[i] == \"1\" && sArray[i + 1] == \"0\" {\n   \
        \             count += 1\n                for j in i + 1..<sArray.count - 1\
        \ {\n                    if sArray[j] == \"0\" && j + 1 < sArray.count && sArray[j\
        \ + 1] == \"1\" {\n                        break\n                    }\n  \
        \                  if sArray[j] == \"1\" {\n                        break\n\
        \                    }\n                }\n            }\n        }\n      \
        \  return count\n    }\n}"
      kotlin: "class Solution {\n    fun maxOperations(s: String): Int {\n        var\
        \ count = 0\n        for (i in 0 until s.length - 1) {\n            if (s[i]\
        \ == '1' && s[i + 1] == '0') {\n                count++\n                for\
        \ (j in i + 1 until s.length - 1) {\n                    if (s[j] == '0' &&\
        \ j + 1 < s.length && s[j + 1] == '1') {\n                        break\n  \
        \                  }\n                    if (s[j] == '1') {\n             \
        \           break\n                    }\n                }\n            }\n\
        \        }\n        return count\n    }\n}"
      dart: "class Solution {\n    int maxOperations(String s) {\n        int count\
        \ = 0;\n        for (int i = 0; i < s.length - 1; i++) {\n            if (s[i]\
        \ == '1' && s[i + 1] == '0') {\n                count++;\n                for\
        \ (int j = i + 1; j < s.length - 1; j++) {\n                    if (s[j] ==\
        \ '0' && j + 1 < s.length && s[j + 1] == '1') {\n                        break;\n\
        \                    }\n                    if (s[j] == '1') {\n           \
        \             break;\n                    }\n                }\n           \
        \ }\n        }\n        return count;\n    }\n}"
      go: "package main\n\nimport (\n    \"fmt\"\n)\n\nfunc maxOperations(s string)\
        \ int {\n    count := 0\n    for i := 0; i < len(s) - 1; i++ {\n        if s[i]\
        \ == '1' && s[i + 1] == '0' {\n            count++\n            for j := i +\
        \ 1; j < len(s) - 1; j++ {\n                if s[j] == '0' && j + 1 < len(s)\
        \ && s[j + 1] == '1' {\n                    break\n                }\n     \
        \           if s[j] == '1' {\n                    break\n                }\n\
        \            }\n        }\n    }\n    return count\n}\n\nfunc main() {\n   \
        \ fmt.Println(maxOperations(\"1001101\"))  // Output: 4\n}"
      ruby: "class Solution\n    def max_operations(s)\n        count = 0\n        (0...s.length\
        \ - 1).each do |i|\n            if s[i] == '1' && s[i + 1] == '0'\n        \
        \        count += 1\n                (i + 1...s.length - 1).each do |j|\n  \
        \                  if s[j] == '0' && j + 1 < s.length && s[j + 1] == '1'\n \
        \                       break\n                    end\n                   \
        \ if s[j] == '1'\n                        break\n                    end\n \
        \               end\n            end\n        end\n        count\n    end\n\
        end"
      scala: "object Solution {\n    def maxOperations(s: String): Int = {\n       \
        \ var count = 0\n        for (i <- 0 until s.length - 1) {\n            if (s(i)\
        \ == '1' && s(i + 1) == '0') {\n                count += 1\n               \
        \ for (j <- i + 1 until s.length - 1) {\n                    if (s(j) == '0'\
        \ && j + 1 < s.length && s(j + 1) == '1') {\n                        j\n   \
        \                 }\n                    if (s(j) == '1') {\n              \
        \          j\n                    }\n                }\n            }\n    \
        \    }\n        count\n    }\n}"
      rust: "struct Solution;\n\nimpl Solution {\n    pub fn max_operations(s: String)\
        \ -> i32 {\n        let mut count = 0;\n        let s: Vec<char> = s.chars().collect();\n\
        \        for i in 0..s.len() - 1 {\n            if s[i] == '1' && s[i + 1] ==\
        \ '0' {\n                count += 1;\n                for j in i + 1..s.len()\
        \ - 1 {\n                    if s[j] == '0' && j + 1 < s.len() && s[j + 1] ==\
        \ '1' {\n                        break;\n                    }\n           \
        \         if s[j] == '1' {\n                        break;\n               \
        \     }\n                }\n            }\n        }\n        count\n    }\n\
        }"
      racket: "#lang racket\n(define (max-operations s)\n    (let loop ((i 0) (count\
        \ 0))\n        (cond\n            ((>= i (string-length s))) count\n       \
        \     ((and (= (string-ref s i) #\\1) (= (string-ref s (+ i 1)) #\\0)))\n  \
        \              (loop (+ i 1) (+ count 1)))\n            (else (loop (+ i 1)\
        \ count))\n        )\n    )\n)"
      erlang: '-module(solution).

        -export([max_operations/1]).


        max_operations(S) ->

        max_operations(S, 0).


        max_operations([H1, H2 | T], Count) ->

        case {H1, H2} of

        {1, 0} ->

        max_operations([H2 | T], Count + 1);

        _ ->

        max_operations([H2 | T], Count)

        end;

        max_operations([_], Count) ->

        Count.'
      elixir: "defmodule Solution do\n    def max_operations(s) do\n        max_operations(s,\
        \ 0)\n    end\n\n    defp max_operations(<<h1, h2, t::binary>>, count) do\n\
        \        case {h1, h2} do\n            {49, 48} ->\n                max_operations(<<h2,\
        \ t::binary>>, count + 1)\n            _ ->\n                max_operations(<<h2,\
        \ t::binary>>, count)\n        end\n    end\n\n    defp max_operations(<<_>>,\
        \ count), do: count\nend"
    approach: The problem can be solved by iterating over the string from left to right
      and performing the operation every time it is possible. We can use a two-pointer
      approach to keep track of the current position and the position where the next
      '1' should be moved. The key idea is to move the '1' to the right until it reaches
      the end of the string or another '1'. This approach ensures that we perform the
      maximum number of operations possible. We can also use a simple loop to iterate
      over the string and perform the operation whenever the current character is '1'
      and the next character is '0'.
    time_complexity: O(n) where n is the length of the string, because we are iterating
      over the string once. The space complexity is O(1) because we are not using any
      extra space that scales with the input size.
    space_complexity: O(1) because we are not using any extra space that scales with
      the input size. We are only using a constant amount of space to store the count
      of operations and the current position in the string.
    elapsed_time: 6.981868505477905
    model: llama-3.3-70b-versatile
    generated_at: '2025-11-24 20:35:05 '
---

## Problem #3228: Maximum Number of Operations to Move Ones to the End

**Difficulty:** Medium

**Topics:** String, Greedy, Counting

## Problem Description

<p>You are given a <span data-keyword="binary-string">binary string</span> <code>s</code>.</p>

<p>You can perform the following operation on the string <strong>any</strong> number of times:</p>

<ul>
	<li>Choose <strong>any</strong> index <code>i</code> from the string where <code>i + 1 &lt; s.length</code> such that <code>s[i] == &#39;1&#39;</code> and <code>s[i + 1] == &#39;0&#39;</code>.</li>
	<li>Move the character <code>s[i]</code> to the <strong>right</strong> until it reaches the end of the string or another <code>&#39;1&#39;</code>. For example, for <code>s = &quot;010010&quot;</code>, if we choose <code>i = 1</code>, the resulting string will be <code>s = &quot;0<strong><u>001</u></strong>10&quot;</code>.</li>
</ul>

<p>Return the <strong>maximum</strong> number of operations that you can perform.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;1001101&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>We can perform the following operations:</p>

<ul>
	<li>Choose index <code>i = 0</code>. The resulting string is <code>s = &quot;<u><strong>001</strong></u>1101&quot;</code>.</li>
	<li>Choose index <code>i = 4</code>. The resulting string is <code>s = &quot;0011<u><strong>01</strong></u>1&quot;</code>.</li>
	<li>Choose index <code>i = 3</code>. The resulting string is <code>s = &quot;001<strong><u>01</u></strong>11&quot;</code>.</li>
	<li>Choose index <code>i = 2</code>. The resulting string is <code>s = &quot;00<strong><u>01</u></strong>111&quot;</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;00111&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
</ul>


## Hints

1. It is optimal to perform the operation on the lowest index possible each time.

2. Traverse the string from left to right and perform the operation every time it is possible.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-24 20:34:58 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to find the maximum number of operations to move all '1's to the end of a binary string. An operation consists of choosing an index `i` where `s[i] == '1'` and `s[i+1] == '0'`, and then moving `s[i]` to the right until it hits another '1' or the end of the string. This entire movement counts as a single operation.

The key insight comes from observing the nature of the operation and the example. When a '1' at `s[i]` moves past a '0' at `s[i+1]`, it effectively swaps places with that '0' (and any subsequent '0's until another '1' is encountered). The crucial point is that the relative order of '1's in the string never changes. If `1_A` is initially to the left of `1_B`, `1_A` will always remain to the left of `1_B` throughout any operations. This means that if a '1' needs to pass a '0', any '1' to its left will also eventually need to pass that same '0' position.

We can solve this problem with a single pass through the string. We maintain a `ones_count` variable, which tracks the number of '1's encountered so far from the beginning of the string up to the current character `s[i]`. We iterate from `i = 0` to `len(s) - 2`. If `s[i]` is a '1', we increment `ones_count`. If we then find a `10` pattern (i.e., `s[i] == '1'` and `s[i+1] == '0'`), it signifies that an operation can be performed. At this point, the '1' at `s[i]` can move past the '0' at `s[i+1]`. Since all `ones_count` '1's (including `s[i]` itself and all '1's to its left) will eventually need to move past this specific '0' position (`s[i+1]`) to reach the end of the string, each of these `ones_count` '1's will contribute one operation involving this '0' position. Therefore, we add the current `ones_count` to our `total_operations`. This greedy strategy, as suggested by the hints, correctly counts the maximum number of operations.

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
    int maxOperations(string s) {
        long long totalOperations = 0;
        int onesCount = 0;
        int n = s.length();

        for (int i = 0; i < n - 1; ++i) {
            if (s[i] == '1') {
                onesCount++;
            }
            // If we find a '10' pattern, it means the '1' at s[i] can move past s[i+1].
            // All 'onesCount' '1's currently to the left of s[i+1] (including s[i])
            // will eventually need to move past this '0' position.
            // Each such move contributes one operation.
            if (s[i] == '1' && s[i+1] == '0') {
                totalOperations += onesCount;
            }
        }
        // The last character s[n-1] cannot be s[i] in a '10' pattern,
        // so it only contributes to onesCount if it's a '1', but doesn't trigger operations.
        // The loop correctly handles this by going up to n-2.

        return totalOperations;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maxOperations(String s) {
        long totalOperations = 0;
        int onesCount = 0;
        int n = s.length();

        for (int i = 0; i < n - 1; ++i) {
            if (s.charAt(i) == '1') {
                onesCount++;
            }
            // If we find a '10' pattern, it means the '1' at s[i] can move past s[i+1].
            // All 'onesCount' '1's currently to the left of s[i+1] (including s[i])
            // will eventually need to move past this '0' position.
            // Each such move contributes one operation.
            if (s.charAt(i) == '1' && s.charAt(i+1) == '0') {
                totalOperations += onesCount;
            }
        }
        // The last character s[n-1] cannot be s[i] in a '10' pattern,
        // so it only contributes to onesCount if it's a '1', but doesn't trigger operations.
        // The loop correctly handles this by going up to n-2.

        return (int) totalOperations;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def maxOperations(self, s: str) -> int:
        total_operations = 0
        ones_count = 0
        n = len(s)

        for i in range(n - 1):
            if s[i] == '1':
                ones_count += 1
            # If we find a '10' pattern, it means the '1' at s[i] can move past s[i+1].
            # All 'ones_count' '1's currently to the left of s[i+1] (including s[i])
            # will eventually need to move past this '0' position.
            # Each such move contributes one operation.
            if s[i] == '1' and s[i+1] == '0':
                total_operations += ones_count

        # The last character s[n-1] cannot be s[i] in a '10' pattern,
        # so it only contributes to ones_count if it's a '1', but doesn't trigger operations.
        # The loop correctly handles this by going up to n-2.

        return total_operations
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxOperations(self, s: str) -> int:
        total_operations = 0
        ones_count = 0
        n = len(s)

        for i in range(n - 1):
            if s[i] == '1':
                ones_count += 1
            # If we find a '10' pattern, it means the '1' at s[i] can move past s[i+1].
            # All 'ones_count' '1's currently to the left of s[i+1] (including s[i])
            # will eventually need to move past this '0' position.
            # Each such move contributes one operation.
            if s[i] == '1' and s[i+1] == '0':
                total_operations += ones_count

        # The last character s[n-1] cannot be s[i] in a '10' pattern,
        # so it only contributes to ones_count if it's a '1', but doesn't trigger operations.
        # The loop correctly handles this by going up to n-2.

        return total_operations
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <string.h>

int maxOperations(char * s){
    long long totalOperations = 0;
    int onesCount = 0;
    int n = strlen(s);

    for (int i = 0; i < n - 1; ++i) {
        if (s[i] == '1') {
            onesCount++;
        }
        // If we find a '10' pattern, it means the '1' at s[i] can move past s[i+1].
        // All 'onesCount' '1's currently to the left of s[i+1] (including s[i])
        // will eventually need to move past this '0' position.
        // Each such move contributes one operation.
        if (s[i] == '1' && s[i+1] == '0') {
            totalOperations += onesCount;
        }
    }
    // The last character s[n-1] cannot be s[i] in a '10' pattern,
    // so it only contributes to onesCount if it's a '1', but doesn't trigger operations.
    // The loop correctly handles this by going up to n-2.

    return (int) totalOperations;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaxOperations(string s) {
        long totalOperations = 0;
        int onesCount = 0;
        int n = s.Length;

        for (int i = 0; i < n - 1; ++i) {
            if (s[i] == '1') {
                onesCount++;
            }
            // If we find a '10' pattern, it means the '1' at s[i] can move past s[i+1].
            // All 'onesCount' '1's currently to the left of s[i+1] (including s[i])
            // will eventually need to move past this '0' position.
            // Each such move contributes one operation.
            if (s[i] == '1' && s[i+1] == '0') {
                totalOperations += onesCount;
            }
        }
        // The last character s[n-1] cannot be s[i] in a '10' pattern,
        // so it only contributes to onesCount if it's a '1', but doesn't trigger operations.
        // The loop correctly handles this by going up to n-2.

        return (int) totalOperations;
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
var maxOperations = function(s) {
    let totalOperations = 0;
    let onesCount = 0;
    const n = s.length;

    for (let i = 0; i < n - 1; ++i) {
        if (s[i] === '1') {
            onesCount++;
        }
        // If we find a '10' pattern, it means the '1' at s[i] can move past s[i+1].
        // All 'onesCount' '1's currently to the left of s[i+1] (including s[i])
        // will eventually need to move past this '0' position.
        // Each such move contributes one operation.
        if (s[i] === '1' && s[i+1] === '0') {
            totalOperations += onesCount;
        }
    }
    // The last character s[n-1] cannot be s[i] in a '10' pattern,
    // so it only contributes to onesCount if it's a '1', but doesn't trigger operations.
    // The loop correctly handles this by going up to n-2.

    return totalOperations;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxOperations(s: string): number {
    let totalOperations: number = 0;
    let onesCount: number = 0;
    const n: number = s.length;

    for (let i = 0; i < n - 1; ++i) {
        if (s[i] === '1') {
            onesCount++;
        }
        // If we find a '10' pattern, it means the '1' at s[i] can move past s[i+1].
        // All 'onesCount' '1's currently to the left of s[i+1] (including s[i])
        // will eventually need to move past this '0' position.
        // Each such move contributes one operation.
        if (s[i] === '1' && s[i+1] === '0') {
            totalOperations += onesCount;
        }
    }
    // The last character s[n-1] cannot be s[i] in a '10' pattern,
    // so it only contributes to onesCount if it's a '1', but doesn't trigger operations.
    // The loop correctly handles this by going up to n-2.

    return totalOperations;
}
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
    function maxOperations($s) {
        $totalOperations = 0;
        $onesCount = 0;
        $n = strlen($s);

        for ($i = 0; $i < $n - 1; ++$i) {
            if ($s[$i] == '1') {
                $onesCount++;
            }
            // If we find a '10' pattern, it means the '1' at s[i] can move past s[i+1].
            // All 'onesCount' '1's currently to the left of s[i+1] (including s[i])
            // will eventually need to move past this '0' position.
            // Each such move contributes one operation.
            if ($s[$i] == '1' && $s[$i+1] == '0') {
                $totalOperations += $onesCount;
            }
        }
        // The last character s[n-1] cannot be s[i] in a '10' pattern,
        // so it only contributes to onesCount if it's a '1', but doesn't trigger operations.
        // The loop correctly handles this by going up to n-2.

        return $totalOperations;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxOperations(_ s: String) -> Int {
        var totalOperations: Int = 0
        var onesCount: Int = 0
        let n: Int = s.count
        let sChars = Array(s)

        for i in 0..<n - 1 {
            if sChars[i] == "1" {
                onesCount += 1
            }
            // If we find a '10' pattern, it means the '1' at sChars[i] can move past sChars[i+1].
            // All 'onesCount' '1's currently to the left of sChars[i+1] (including sChars[i])
            // will eventually need to move past this '0' position.
            // Each such move contributes one operation.
            if sChars[i] == "1" && sChars[i+1] == "0" {
                totalOperations += onesCount
            }
        }
        // The last character sChars[n-1] cannot be sChars[i] in a '10' pattern,
        // so it only contributes to onesCount if it's a '1', but doesn't trigger operations.
        // The loop correctly handles this by going up to n-2.

        return totalOperations
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxOperations(s: String): Int {
        var totalOperations: Long = 0
        var onesCount: Int = 0
        val n: Int = s.length

        for (i in 0 until n - 1) {
            if (s[i] == '1') {
                onesCount++
            }
            // If we find a '10' pattern, it means the '1' at s[i] can move past s[i+1].
            // All 'onesCount' '1's currently to the left of s[i+1] (including s[i])
            // will eventually need to move past this '0' position.
            // Each such move contributes one operation.
            if (s[i] == '1' && s[i+1] == '0') {
                totalOperations += onesCount
            }
        }
        // The last character s[n-1] cannot be s[i] in a '10' pattern,
        // so it only contributes to onesCount if it's a '1', but doesn't trigger operations.
        // The loop correctly handles this by going up to n-2.

        return totalOperations.toInt()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maxOperations(String s) {
    int totalOperations = 0;
    int onesCount = 0;
    int n = s.length;

    for (int i = 0; i < n - 1; ++i) {
      if (s[i] == '1') {
        onesCount++;
      }
      // If we find a '10' pattern, it means the '1' at s[i] can move past s[i+1].
      // All 'onesCount' '1's currently to the left of s[i+1] (including s[i])
      // will eventually need to move past this '0' position.
      // Each such move contributes one operation.
      if (s[i] == '1' && s[i+1] == '0') {
        totalOperations += onesCount;
      }
    }
    // The last character s[n-1] cannot be s[i] in a '10' pattern,
    // so it only contributes to onesCount if it's a '1', but doesn't trigger operations.
    // The loop correctly handles this by going up to n-2.

    return totalOperations;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxOperations(s string) int {
    var totalOperations int = 0
    var onesCount int = 0
    n := len(s)

    for i := 0; i < n - 1; i++ {
        if s[i] == '1' {
            onesCount++
        }
        // If we find a '10' pattern, it means the '1' at s[i] can move past s[i+1].
        // All 'onesCount' '1's currently to the left of s[i+1] (including s[i])
        // will eventually need to move past this '0' position.
        // Each such move contributes one operation.
        if s[i] == '1' && s[i+1] == '0' {
            totalOperations += onesCount
        }
    }
    // The last character s[n-1] cannot be s[i] in a '10' pattern,
    // so it only contributes to onesCount if it's a '1', but doesn't trigger operations.
    // The loop correctly handles this by going up to n-2.

    return totalOperations
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    # @param {String} s
    # @return {Integer}
    def max_operations(s)
        total_operations = 0
        ones_count = 0
        n = s.length

        (0...n - 1).each do |i|
            if s[i] == '1'
                ones_count += 1
            end
            # If we find a '10' pattern, it means the '1' at s[i] can move past s[i+1].
            # All 'ones_count' '1's currently to the left of s[i+1] (including s[i])
            # will eventually need to move past this '0' position.
            # Each such move contributes one operation.
            if s[i] == '1' && s[i+1] == '0'
                total_operations += ones_count
            end
        end
        # The last character s[n-1] cannot be s[i] in a '10' pattern,
        # so it only contributes to ones_count if it's a '1', but doesn't trigger operations.
        # The loop correctly handles this by going up to n-2.

        total_operations
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxOperations(s: String): Int = {
        var totalOperations: Long = 0
        var onesCount: Int = 0
        val n: Int = s.length

        for (i <- 0 until n - 1) {
            if (s(i) == '1') {
                onesCount += 1
            }
            // If we find a '10' pattern, it means the '1' at s(i) can move past s(i+1).
            // All 'onesCount' '1's currently to the left of s(i+1) (including s(i))
            // will eventually need to move past this '0' position.
            // Each such move contributes one operation.
            if (s(i) == '1' && s(i+1) == '0') {
                totalOperations += onesCount
            }
        }
        // The last character s(n-1) cannot be s(i) in a '10' pattern,
        // so it only contributes to onesCount if it's a '1', but doesn't trigger operations.
        // The loop correctly handles this by going up to n-2.

        totalOperations.toInt
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_operations(s: String) -> i32 {
        let mut total_operations: i32 = 0;
        let mut ones_count: i32 = 0;
        let n = s.len();
        let s_chars: Vec<char> = s.chars().collect();

        for i in 0..n - 1 {
            if s_chars[i] == '1' {
                ones_count += 1;
            }
            // If we find a '10' pattern, it means the '1' at s_chars[i] can move past s_chars[i+1].
            // All 'ones_count' '1's currently to the left of s_chars[i+1] (including s_chars[i])
            // will eventually need to move past this '0' position.
            // Each such move contributes one operation.
            if s_chars[i] == '1' && s_chars[i+1] == '0' {
                total_operations += ones_count;
            }
        }
        // The last character s_chars[n-1] cannot be s_chars[i] in a '10' pattern,
        // so it only contributes to ones_count if it's a '1', but doesn't trigger operations.
        // The loop correctly handles this by going up to n-2.

        total_operations
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define/contract (max-operations s)
  (-> string? integer?)
  (let* ((n (string-length s))
         (total-operations 0)
         (ones-count 0))
    (for ([i (in-range (- n 1))])
      (when (char=? (string-ref s i) #\1)
        (set! ones-count (+ ones-count 1)))
      ;; If we find a '10' pattern, it means the '1' at s[i] can move past s[i+1].
      ;; All 'ones-count' '1's currently to the left of s[i+1] (including s[i])
      ;; will eventually need to move past this '0' position.
      ;; Each such move contributes one operation.
      (when (and (char=? (string-ref s i) #\1) (char=? (string-ref s (+ i 1)) #\0))
        (set! total-operations (+ total-operations ones-count))))
    ;; The last character s[n-1] cannot be s[i] in a '10' pattern,
    ;; so it only contributes to ones-count if it's a '1', but doesn't trigger operations.
    ;; The loop correctly handles this by going up to n-2.
    total-operations))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([max_operations/1]).

max_operations(S) ->
    N = length(S),
    max_operations_recursive(S, N, 0, 0, 0).

max_operations_recursive(S, N, Index, OnesCount, TotalOperations) when Index < N - 1 ->
    CharI = lists:nth(Index + 1, S), % Erlang lists are 1-indexed, so Index + 1 for 0-indexed 'Index'
    CharIPlus1 = lists:nth(Index + 2, S), % Index + 2 for 0-indexed 'Index + 1'

    NewOnesCount = if
        CharI == $1 -> OnesCount + 1;
        true -> OnesCount
    end,

    NewTotalOperations = if
        CharI == $1 andalso CharIPlus1 == $0 -> TotalOperations + NewOnesCount;
        true -> TotalOperations
    end,

    max_operations_recursive(S, N, Index + 1, NewOnesCount, NewTotalOperations);
max_operations_recursive(_S, _N, _Index, _OnesCount, TotalOperations) ->
    TotalOperations.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_operations(s :: String.t) :: integer
  def max_operations(s) do
    n = String.length(s)
    s_chars = String.to_charlist(s)

    Enum.reduce(0..(n - 2), {0, 0}, fn i, {ones_count, total_operations} ->
      char_i = Enum.at(s_chars, i)
      char_i_plus_1 = Enum.at(s_chars, i + 1)

      new_ones_count = if char_i == ?1, do: ones_count + 1, else: ones_count

      new_total_operations = if char_i == ?1 and char_i_plus_1 == ?0 do
        total_operations + new_ones_count
      else
        total_operations
      end

      {new_ones_count, new_total_operations}
    end)
    |> elem(1) # Return total_operations
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) with detailed explanation. The algorithm iterates through the string once from left to right. In each step, it performs constant time operations (character comparison, incrementing counters). Therefore, the total time complexity is directly proportional to the length of the string, N.

- **Space Complexity:** O(1) with detailed explanation. The algorithm uses a few integer variables (`total_operations`, `ones_count`, `n`, `i`) to store state, regardless of the input string's length. No auxiliary data structures that grow with N are used. For languages that convert the string to a character array (like Swift or Rust), this might incur O(N) space for the array, but it's typically considered part of the input representation or constant auxiliary space if the string is already in an iterable form.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-24 20:35:05 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by iterating over the string from left to right and performing the operation every time it is possible. We can use a two-pointer approach to keep track of the current position and the position where the next '1' should be moved. The key idea is to move the '1' to the right until it reaches the end of the string or another '1'. This approach ensures that we perform the maximum number of operations possible. We can also use a simple loop to iterate over the string and perform the operation whenever the current character is '1' and the next character is '0'.

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
#include <string>
class Solution {
public:
    int maxOperations(std::string s) {
        int count = 0;
        for (int i = 0; i < s.length() - 1; i++) {
            if (s[i] == '1' && s[i + 1] == '0') {
                count++;
                for (int j = i + 1; j < s.length() - 1; j++) {
                    if (s[j] == '0' && s[j + 1] == '1') {
                        break;
                    }
                    if (s[j] == '1') {
                        break;
                    }
                }
            }
        }
        return count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
public class Solution {
    public int maxOperations(String s) {
        int count = 0;
        for (int i = 0; i < s.length() - 1; i++) {
            if (s.charAt(i) == '1' && s.charAt(i + 1) == '0') {
                count++;
                for (int j = i + 1; j < s.length() - 1; j++) {
                    if (s.charAt(j) == '0' && j + 1 < s.length() && s.charAt(j + 1) == '1') {
                        break;
                    }
                    if (s.charAt(j) == '1') {
                        break;
                    }
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
    def maxOperations(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 1):
            if s[i] == '1' and s[i + 1] == '0':
                count += 1
                for j in range(i + 1, len(s) - 1):
                    if s[j] == '0' and j + 1 < len(s) and s[j + 1] == '1':
                        break
                    if s[j] == '1':
                        break
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxOperations(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 1):
            if s[i] == '1' and s[i + 1] == '0':
                count += 1
                for j in range(i + 1, len(s) - 1):
                    if s[j] == '0' and j + 1 < len(s) and s[j + 1] == '1':
                        break
                    if s[j] == '1':
                        break
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <string.h>

int maxOperations(char * s){
    int count = 0;
    for (int i = 0; i < strlen(s) - 1; i++) {
        if (s[i] == '1' && s[i + 1] == '0') {
            count++;
            for (int j = i + 1; j < strlen(s) - 1; j++) {
                if (s[j] == '0' && j + 1 < strlen(s) && s[j + 1] == '1') {
                    break;
                }
                if (s[j] == '1') {
                    break;
                }
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
    public int MaxOperations(string s) {
        int count = 0;
        for (int i = 0; i < s.Length - 1; i++) {
            if (s[i] == '1' && s[i + 1] == '0') {
                count++;
                for (int j = i + 1; j < s.Length - 1; j++) {
                    if (s[j] == '0' && j + 1 < s.Length && s[j + 1] == '1') {
                        break;
                    }
                    if (s[j] == '1') {
                        break;
                    }
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
var maxOperations = function(s) {
    let count = 0;
    for (let i = 0; i < s.length - 1; i++) {
        if (s[i] === '1' && s[i + 1] === '0') {
            count++;
            for (let j = i + 1; j < s.length - 1; j++) {
                if (s[j] === '0' && j + 1 < s.length && s[j + 1] === '1') {
                    break;
                }
                if (s[j] === '1') {
                    break;
                }
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
function maxOperations(s: string): number {
    let count: number = 0;
    for (let i: number = 0; i < s.length - 1; i++) {
        if (s[i] === '1' && s[i + 1] === '0') {
            count++;
            for (let j: number = i + 1; j < s.length - 1; j++) {
                if (s[j] === '0' && j + 1 < s.length && s[j + 1] === '1') {
                    break;
                }
                if (s[j] === '1') {
                    break;
                }
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
    function maxOperations($s) {
        $count = 0;
        for ($i = 0; $i < strlen($s) - 1; $i++) {
            if ($s[$i] == '1' && $s[$i + 1] == '0') {
                $count++;
                for ($j = $i + 1; $j < strlen($s) - 1; $j++) {
                    if ($s[$j] == '0' && $j + 1 < strlen($s) && $s[$j + 1] == '1') {
                        break;
                    }
                    if ($s[$j] == '1') {
                        break;
                    }
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
    func maxOperations(_ s: String) -> Int {
        var count = 0
        let sArray = Array(s)
        for i in 0..<sArray.count - 1 {
            if sArray[i] == "1" && sArray[i + 1] == "0" {
                count += 1
                for j in i + 1..<sArray.count - 1 {
                    if sArray[j] == "0" && j + 1 < sArray.count && sArray[j + 1] == "1" {
                        break
                    }
                    if sArray[j] == "1" {
                        break
                    }
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
    fun maxOperations(s: String): Int {
        var count = 0
        for (i in 0 until s.length - 1) {
            if (s[i] == '1' && s[i + 1] == '0') {
                count++
                for (j in i + 1 until s.length - 1) {
                    if (s[j] == '0' && j + 1 < s.length && s[j + 1] == '1') {
                        break
                    }
                    if (s[j] == '1') {
                        break
                    }
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
    int maxOperations(String s) {
        int count = 0;
        for (int i = 0; i < s.length - 1; i++) {
            if (s[i] == '1' && s[i + 1] == '0') {
                count++;
                for (int j = i + 1; j < s.length - 1; j++) {
                    if (s[j] == '0' && j + 1 < s.length && s[j + 1] == '1') {
                        break;
                    }
                    if (s[j] == '1') {
                        break;
                    }
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
package main

import (
    "fmt"
)

func maxOperations(s string) int {
    count := 0
    for i := 0; i < len(s) - 1; i++ {
        if s[i] == '1' && s[i + 1] == '0' {
            count++
            for j := i + 1; j < len(s) - 1; j++ {
                if s[j] == '0' && j + 1 < len(s) && s[j + 1] == '1' {
                    break
                }
                if s[j] == '1' {
                    break
                }
            }
        }
    }
    return count
}

func main() {
    fmt.Println(maxOperations("1001101"))  // Output: 4
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    def max_operations(s)
        count = 0
        (0...s.length - 1).each do |i|
            if s[i] == '1' && s[i + 1] == '0'
                count += 1
                (i + 1...s.length - 1).each do |j|
                    if s[j] == '0' && j + 1 < s.length && s[j + 1] == '1'
                        break
                    end
                    if s[j] == '1'
                        break
                    end
                end
            end
        end
        count
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxOperations(s: String): Int = {
        var count = 0
        for (i <- 0 until s.length - 1) {
            if (s(i) == '1' && s(i + 1) == '0') {
                count += 1
                for (j <- i + 1 until s.length - 1) {
                    if (s(j) == '0' && j + 1 < s.length && s(j + 1) == '1') {
                        j
                    }
                    if (s(j) == '1') {
                        j
                    }
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
struct Solution;

impl Solution {
    pub fn max_operations(s: String) -> i32 {
        let mut count = 0;
        let s: Vec<char> = s.chars().collect();
        for i in 0..s.len() - 1 {
            if s[i] == '1' && s[i + 1] == '0' {
                count += 1;
                for j in i + 1..s.len() - 1 {
                    if s[j] == '0' && j + 1 < s.len() && s[j + 1] == '1' {
                        break;
                    }
                    if s[j] == '1' {
                        break;
                    }
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
#lang racket
(define (max-operations s)
    (let loop ((i 0) (count 0))
        (cond
            ((>= i (string-length s))) count
            ((and (= (string-ref s i) #\1) (= (string-ref s (+ i 1)) #\0)))
                (loop (+ i 1) (+ count 1)))
            (else (loop (+ i 1) count))
        )
    )
)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([max_operations/1]).

max_operations(S) ->
max_operations(S, 0).

max_operations([H1, H2 | T], Count) ->
case {H1, H2} of
{1, 0} ->
max_operations([H2 | T], Count + 1);
_ ->
max_operations([H2 | T], Count)
end;
max_operations([_], Count) ->
Count.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
    def max_operations(s) do
        max_operations(s, 0)
    end

    defp max_operations(<<h1, h2, t::binary>>, count) do
        case {h1, h2} do
            {49, 48} ->
                max_operations(<<h2, t::binary>>, count + 1)
            _ ->
                max_operations(<<h2, t::binary>>, count)
        end
    end

    defp max_operations(<<_>>, count), do: count
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the string, because we are iterating over the string once. The space complexity is O(1) because we are not using any extra space that scales with the input size.

- **Space Complexity:** O(1) because we are not using any extra space that scales with the input size. We are only using a constant amount of space to store the count of operations and the current position in the string.

</div>
</details>
