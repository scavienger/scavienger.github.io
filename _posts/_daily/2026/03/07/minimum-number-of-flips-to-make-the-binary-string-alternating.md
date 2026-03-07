---
layout: post
title: "Minimum Number of Flips to Make the Binary String Alternating"
date: 2026-03-07 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Dynamic Programming", "Sliding Window"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minFlips(string s) {\n        int n =\
        \ s.length();\n        string s2 = s + s;\n        int diff1 = 0, diff2 = 0;\n\
        \        int ans = n;\n        for (int i = 0; i < 2 * n; i++) {\n         \
        \   if (s2[i] != (i % 2 == 0 ? '0' : '1')) diff1++;\n            if (s2[i] !=\
        \ (i % 2 == 0 ? '1' : '0')) diff2++;\n            if (i >= n) {\n          \
        \      if (s2[i - n] != ((i - n) % 2 == 0 ? '0' : '1')) diff1--;\n         \
        \       if (s2[i - n] != ((i - n) % 2 == 0 ? '1' : '0')) diff2--;\n        \
        \    }\n            if (i >= n - 1) {\n                if (diff1 < ans) ans\
        \ = diff1;\n                if (diff2 < ans) ans = diff2;\n            }\n \
        \       }\n        return ans;\n    }\n};"
      java: "class Solution {\n    public int minFlips(String s) {\n        int n =\
        \ s.length();\n        String s2 = s + s;\n        int diff1 = 0, diff2 = 0;\n\
        \        int ans = n;\n        for (int i = 0; i < 2 * n; i++) {\n         \
        \   if (s2.charAt(i) != (i % 2 == 0 ? '0' : '1')) diff1++;\n            if (s2.charAt(i)\
        \ != (i % 2 == 0 ? '1' : '0')) diff2++;\n            if (i >= n) {\n       \
        \         if (s2.charAt(i - n) != ((i - n) % 2 == 0 ? '0' : '1')) diff1--;\n\
        \                if (s2.charAt(i - n) != ((i - n) % 2 == 0 ? '1' : '0')) diff2--;\n\
        \            }\n            if (i >= n - 1) {\n                ans = Math.min(ans,\
        \ Math.min(diff1, diff2));\n            }\n        }\n        return ans;\n\
        \    }\n}"
      python: "class Solution(object):\n    def minFlips(self, s):\n        \"\"\"\n\
        \        :type s: str\n        :rtype: int\n        \"\"\"\n        n = len(s)\n\
        \        s2 = s + s\n        ans = n\n        diff1 = 0\n        diff2 = 0\n\
        \        for i in range(2 * n):\n            if s2[i] != ('0' if i % 2 == 0\
        \ else '1'):\n                diff1 += 1\n            if s2[i] != ('1' if i\
        \ % 2 == 0 else '0'):\n                diff2 += 1\n            if i >= n:\n\
        \                if s2[i - n] != ('0' if (i - n) % 2 == 0 else '1'):\n     \
        \               diff1 -= 1\n                if s2[i - n] != ('1' if (i - n)\
        \ % 2 == 0 else '0'):\n                    diff2 -= 1\n            if i >= n\
        \ - 1:\n                if diff1 < ans: ans = diff1\n                if diff2\
        \ < ans: ans = diff2\n        return ans"
      python3: "class Solution:\n    def minFlips(self, s: str) -> int:\n        n =\
        \ len(s)\n        s2 = s + s\n        ans = n\n        diff1 = 0\n        diff2\
        \ = 0\n        for i in range(2 * n):\n            if s2[i] != ('0' if i % 2\
        \ == 0 else '1'):\n                diff1 += 1\n            if s2[i] != ('1'\
        \ if i % 2 == 0 else '0'):\n                diff2 += 1\n            if i >=\
        \ n:\n                if s2[i - n] != ('0' if (i - n) % 2 == 0 else '1'):\n\
        \                    diff1 -= 1\n                if s2[i - n] != ('1' if (i\
        \ - n) % 2 == 0 else '0'):\n                    diff2 -= 1\n            if i\
        \ >= n - 1:\n                ans = min(ans, diff1, diff2)\n        return ans"
      c: "int minFlips(char* s) {\n    int n = 0;\n    while (s[n] != '\\0') n++;\n\
        \    int diff1 = 0, diff2 = 0;\n    int ans = n;\n    for (int i = 0; i < 2\
        \ * n; i++) {\n        if (s[i % n] != (i % 2 == 0 ? '0' : '1')) diff1++;\n\
        \        if (s[i % n] != (i % 2 == 0 ? '1' : '0')) diff2++;\n        if (i >=\
        \ n) {\n            if (s[(i - n) % n] != ((i - n) % 2 == 0 ? '0' : '1')) diff1--;\n\
        \            if (s[(i - n) % n] != ((i - n) % 2 == 0 ? '1' : '0')) diff2--;\n\
        \        }\n        if (i >= n - 1) {\n            if (diff1 < ans) ans = diff1;\n\
        \            if (diff2 < ans) ans = diff2;\n        }\n    }\n    return ans;\n\
        }"
      csharp: "public class Solution {\n    public int MinFlips(string s) {\n      \
        \  int n = s.Length;\n        string s2 = s + s;\n        int diff1 = 0, diff2\
        \ = 0;\n        int ans = n;\n        for (int i = 0; i < 2 * n; i++) {\n  \
        \          if (s2[i] != (i % 2 == 0 ? '0' : '1')) diff1++;\n            if (s2[i]\
        \ != (i % 2 == 0 ? '1' : '0')) diff2++;\n            if (i >= n) {\n       \
        \         if (s2[i - n] != ((i - n) % 2 == 0 ? '0' : '1')) diff1--;\n      \
        \          if (s2[i - n] != ((i - n) % 2 == 0 ? '1' : '0')) diff2--;\n     \
        \       }\n            if (i >= n - 1) {\n                ans = Math.Min(ans,\
        \ Math.Min(diff1, diff2));\n            }\n        }\n        return ans;\n\
        \    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {number}\n */\nvar minFlips\
        \ = function(s) {\n    let n = s.length;\n    let s2 = s + s;\n    let diff1\
        \ = 0, diff2 = 0;\n    let ans = n;\n    for (let i = 0; i < 2 * n; i++) {\n\
        \        if (s2[i] !== (i % 2 === 0 ? '0' : '1')) diff1++;\n        if (s2[i]\
        \ !== (i % 2 === 0 ? '1' : '0')) diff2++;\n        if (i >= n) {\n         \
        \   if (s2[i - n] !== ((i - n) % 2 === 0 ? '0' : '1')) diff1--;\n          \
        \  if (s2[i - n] !== ((i - n) % 2 === 0 ? '1' : '0')) diff2--;\n        }\n\
        \        if (i >= n - 1) {\n            ans = Math.min(ans, diff1, diff2);\n\
        \        }\n    }\n    return ans;\n};"
      typescript: "function minFlips(s: string): number {\n    const n = s.length;\n\
        \    const s2 = s + s;\n    let diff1 = 0, diff2 = 0;\n    let res = n;\n  \
        \  for (let i = 0; i < 2 * n; i++) {\n        if (s2[i] !== (i % 2 === 0 ? '0'\
        \ : '1')) diff1++;\n        if (s2[i] !== (i % 2 === 0 ? '1' : '0')) diff2++;\n\
        \        if (i >= n) {\n            if (s2[i - n] !== ((i - n) % 2 === 0 ? '0'\
        \ : '1')) diff1--;\n            if (s2[i - n] !== ((i - n) % 2 === 0 ? '1' :\
        \ '0')) diff2--;\n        }\n        if (i >= n - 1) {\n            res = Math.min(res,\
        \ diff1, diff2);\n        }\n    }\n    return res;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return Integer\n\
        \     */\n    function minFlips($s) {\n        $n = strlen($s);\n        $s2\
        \ = $s . $s;\n        $diff1 = 0;\n        $diff2 = 0;\n        $res = $n;\n\
        \        for ($i = 0; $i < 2 * $n; $i++) {\n            if ($s2[$i] !== ($i\
        \ % 2 === 0 ? '0' : '1')) $diff1++;\n            if ($s2[$i] !== ($i % 2 ===\
        \ 0 ? '1' : '0')) $diff2++;\n            if ($i >= $n) {\n                if\
        \ ($s2[$i - $n] !== (($i - $n) % 2 === 0 ? '0' : '1')) $diff1--;\n         \
        \       if ($s2[$i - $n] !== (($i - $n) % 2 === 0 ? '1' : '0')) $diff2--;\n\
        \            }\n            if ($i >= $n - 1) {\n                $res = min($res,\
        \ $diff1, $diff2);\n            }\n        }\n        return $res;\n    }\n}"
      swift: "class Solution {\n    func minFlips(_ s: String) -> Int {\n        let\
        \ n = s.count\n        let chars = Array(s + s)\n        var diff1 = 0\n   \
        \     var diff2 = 0\n        var res = n\n        for i in 0..<(2 * n) {\n \
        \           if chars[i] != (i % 2 == 0 ? \"0\" : \"1\") { diff1 += 1 }\n   \
        \         if chars[i] != (i % 2 == 0 ? \"1\" : \"0\") { diff2 += 1 }\n     \
        \       if i >= n {\n                if chars[i - n] != ((i - n) % 2 == 0 ?\
        \ \"0\" : \"1\") { diff1 -= 1 }\n                if chars[i - n] != ((i - n)\
        \ % 2 == 0 ? \"1\" : \"0\") { diff2 -= 1 }\n            }\n            if i\
        \ >= n - 1 {\n                res = min(res, min(diff1, diff2))\n          \
        \  }\n        }\n        return res\n    }\n}"
      kotlin: "class Solution {\n    fun minFlips(s: String): Int {\n        val n =\
        \ s.length\n        val s2 = s + s\n        var diff1 = 0\n        var diff2\
        \ = 0\n        var res = n\n        for (i in 0 until 2 * n) {\n           \
        \ if (s2[i] != (if (i % 2 == 0) '0' else '1')) diff1++\n            if (s2[i]\
        \ != (if (i % 2 == 0) '1' else '0')) diff2++\n            if (i >= n) {\n  \
        \              if (s2[i - n] != (if ((i - n) % 2 == 0) '0' else '1')) diff1--\n\
        \                if (s2[i - n] != (if ((i - n) % 2 == 0) '1' else '0')) diff2--\n\
        \            }\n            if (i >= n - 1) {\n                val currentMin\
        \ = if (diff1 < diff2) diff1 else diff2\n                if (currentMin < res)\
        \ res = currentMin\n            }\n        }\n        return res\n    }\n}"
      dart: "class Solution {\n  int minFlips(String s) {\n    int n = s.length;\n \
        \   String s2 = s + s;\n    int diff1 = 0;\n    int diff2 = 0;\n    int res\
        \ = n;\n    for (int i = 0; i < 2 * n; i++) {\n      if (s2[i] != (i % 2 ==\
        \ 0 ? '0' : '1')) diff1++;\n      if (s2[i] != (i % 2 == 0 ? '1' : '0')) diff2++;\n\
        \      if (i >= n) {\n        if (s2[i - n] != ((i - n) % 2 == 0 ? '0' : '1'))\
        \ diff1--;\n        if (s2[i - n] != ((i - n) % 2 == 0 ? '1' : '0')) diff2--;\n\
        \      }\n      if (i >= n - 1) {\n        int m = diff1 < diff2 ? diff1 : diff2;\n\
        \        if (m < res) res = m;\n      }\n    }\n    return res;\n  }\n}"
      go: "func minFlips(s string) int {\n\tn := len(s)\n\ts2 := s + s\n\tdiff1, diff2\
        \ := 0, 0\n\tres := n\n\tfor i := 0; i < 2*n; i++ {\n\t\tif s2[i] != \"01\"\
        [i%2] {\n\t\t\tdiff1++\n\t\t}\n\t\tif s2[i] != \"10\"[i%2] {\n\t\t\tdiff2++\n\
        \t\t}\n\t\tif i >= n {\n\t\t\tif s2[i-n] != \"01\"[(i-n)%2] {\n\t\t\t\tdiff1--\n\
        \t\t\t}\n\t\t\tif s2[i-n] != \"10\"[(i-n)%2] {\n\t\t\t\tdiff2--\n\t\t\t}\n\t\
        \t}\n\t\tif i >= n-1 {\n\t\t\tif diff1 < res {\n\t\t\t\tres = diff1\n\t\t\t\
        }\n\t\t\tif diff2 < res {\n\t\t\t\tres = diff2\n\t\t\t}\n\t\t}\n\t}\n\treturn\
        \ res\n}"
      ruby: "def min_flips(s)\n  n = s.length\n  ss = s + s\n  d1 = 0\n  d2 = 0\n  res\
        \ = n\n  (0...2 * n).each do |i|\n    d1 += 1 if ss[i] != (i.even? ? '0' : '1')\n\
        \    d2 += 1 if ss[i] != (i.even? ? '1' : '0')\n    if i >= n\n      d1 -= 1\
        \ if ss[i - n] != ((i - n).even? ? '0' : '1')\n      d2 -= 1 if ss[i - n] !=\
        \ ((i - n).even? ? '1' : '0')\n    end\n    if i >= n - 1\n      res = d1 if\
        \ d1 < res\n      res = d2 if d2 < res\n    end\n  end\n  res\nend"
      scala: "object Solution {\n  def minFlips(s: String): Int = {\n    val n = s.length\n\
        \    val ss = s + s\n    var d1 = 0\n    var d2 = 0\n    var res = n\n    for\
        \ (i <- 0 until 2 * n) {\n      if (ss(i) != (if (i % 2 == 0) '0' else '1'))\
        \ d1 += 1\n      if (ss(i) != (if (i % 2 == 0) '1' else '0')) d2 += 1\n    \
        \  if (i >= n) {\n        if (ss(i - n) != (if ((i - n) % 2 == 0) '0' else '1'))\
        \ d1 -= 1\n        if (ss(i - n) != (if ((i - n) % 2 == 0) '1' else '0')) d2\
        \ -= 1\n      }\n      if (i >= n - 1) {\n        res = Math.min(res, Math.min(d1,\
        \ d2))\n      }\n    }\n    res\n  }\n}"
      rust: "impl Solution {\n    pub fn min_flips(s: String) -> i32 {\n        let\
        \ n = s.len();\n        let ss = s.repeat(2);\n        let bytes = ss.as_bytes();\n\
        \        let mut d1 = 0;\n        let mut d2 = 0;\n        let mut res = n as\
        \ i32;\n        for i in 0..2 * n {\n            if bytes[i] != (if i % 2 ==\
        \ 0 { b'0' } else { b'1' }) { d1 += 1; }\n            if bytes[i] != (if i %\
        \ 2 == 0 { b'1' } else { b'0' }) { d2 += 1; }\n            if i >= n {\n   \
        \             if bytes[i - n] != (if (i - n) % 2 == 0 { b'0' } else { b'1' })\
        \ { d1 -= 1; }\n                if bytes[i - n] != (if (i - n) % 2 == 0 { b'1'\
        \ } else { b'0' }) { d2 -= 1; }\n            }\n            if i >= n - 1 {\n\
        \                res = res.min(d1).min(d2);\n            }\n        }\n    \
        \    res\n    }\n}"
      racket: "(define/contract (min-flips s)\n  (-> string? exact-integer?)\n  (let*\
        \ ([n (string-length s)]\n         [ss (string-append s s)])\n    (let-values\
        \ ([(_d1 _d2 final-min)\n                  (for/fold ([d1 0] [d2 0] [min-d n])\n\
        \                            ([i (in-range (* 2 n))])\n                    (let*\
        \ ([char (string-ref ss i)]\n                           [t1 (if (even? i) #\\\
        0 #\\1)]\n                           [t2 (if (even? i) #\\1 #\\0)]\n       \
        \                    [nd1 (+ d1 (if (char=? char t1) 0 1))]\n              \
        \             [nd2 (+ d2 (if (char=? char t2) 0 1))])\n                    \
        \  (let-values ([(fd1 fd2)\n                                    (if (>= i n)\n\
        \                                        (let* ([old-char (string-ref ss (-\
        \ i n))]\n                                               [old-t1 (if (even?\
        \ (- i n)) #\\0 #\\1)]\n                                               [old-t2\
        \ (if (even? (- i n)) #\\1 #\\0)])\n                                       \
        \   (values (- nd1 (if (char=? old-char old-t1) 0 1))\n                    \
        \                              (- nd2 (if (char=? old-char old-t2) 0 1))))\n\
        \                                        (values nd1 nd2))])\n             \
        \           (values fd1 fd2\n                                (if (>= i (- n\
        \ 1))\n                                    (min min-d fd1 fd2)\n           \
        \                         min-d)))))])\n      final-min)))"
      erlang: "-spec min_flips(S :: unicode:unicode_binary()) -> integer().\nmin_flips(S)\
        \ ->\n  N = byte_size(S),\n  SS = <<S/binary, S/binary>>,\n  Tuple = list_to_tuple(binary_to_list(SS)),\n\
        \  loop(Tuple, 0, N, 0, 0, N).\n\nloop(Tuple, I, N, D1, D2, MinD) when I < 2\
        \ * N ->\n  Char = element(I + 1, Tuple),\n  T1 = if I rem 2 =:= 0 -> $0; true\
        \ -> $1 end,\n  T2 = if I rem 2 =:= 0 -> $1; true -> $0 end,\n  ND1 = if Char\
        \ =/= T1 -> D1 + 1; true -> D1 end,\n  ND2 = if Char =/= T2 -> D2 + 1; true\
        \ -> D2 end,\n  {FD1, FD2} = if I >= N ->\n    CharOld = element(I - N + 1,\
        \ Tuple),\n    T1Old = if (I - N) rem 2 =:= 0 -> $0; true -> $1 end,\n    T2Old\
        \ = if (I - N) rem 2 =:= 0 -> $1; true -> $0 end,\n    {if CharOld =/= T1Old\
        \ -> ND1 - 1; true -> ND1 end,\n     if CharOld =/= T2Old -> ND2 - 1; true ->\
        \ ND2 end};\n    true -> {ND1, ND2}\n  end,\n  NMinD = if I >= N - 1 ->\n  \
        \  M = if FD1 < FD2 -> FD1; true -> FD2 end,\n    if M < MinD -> M; true ->\
        \ MinD end;\n    true -> MinD\n  end,\n  loop(Tuple, I + 1, N, FD1, FD2, NMinD);\n\
        loop(_, _, _, _, _, MinD) ->\n  MinD."
      elixir: "defmodule Solution do\n  @spec min_flips(s :: String.t) :: integer\n\
        \  def min_flips(s) do\n    n = String.length(s)\n    ss = s <> s\n    chars\
        \ = ss |> String.to_charlist() |> List.to_tuple()\n    reduce_flips(chars, 0,\
        \ n, 0, 0, n)\n  end\n\n  defp reduce_flips(_chars, i, n, _d1, _d2, min_d) when\
        \ i >= 2 * n, do: min_d\n  defp reduce_flips(chars, i, n, d1, d2, min_d) do\n\
        \    char = elem(chars, i)\n    t1 = if rem(i, 2) == 0, do: ?0, else: ?1\n \
        \   t2 = if rem(i, 2) == 0, do: ?1, else: ?0\n    nd1 = d1 + (if char != t1,\
        \ do: 1, else: 0)\n    nd2 = d2 + (if char != t2, do: 1, else: 0)\n    {fd1,\
        \ fd2} = if i >= n do\n      old_char = elem(chars, i - n)\n      old_t1 = if\
        \ rem(i - n, 2) == 0, do: ?0, else: ?1\n      old_t2 = if rem(i - n, 2) == 0,\
        \ do: ?1, else: ?0\n      {nd1 - (if old_char != old_t1, do: 1, else: 0), nd2\
        \ - (if old_char != old_t2, do: 1, else: 0)}\n    else\n      {nd1, nd2}\n \
        \   end\n    new_min_d = if i >= n - 1, do: min(min_d, min(fd1, fd2)), else:\
        \ min_d\n    reduce_flips(chars, i + 1, n, fd1, fd2, new_min_d)\n  end\nend"
    approach: "The problem is solved using a sliding window approach on a doubled version\
      \ of the input string. By concatenating the string with itself ($s + s$), all\
      \ possible cyclic shifts of length $n$ are represented as contiguous substrings\
      \ of length $n$. There are only two possible target alternating patterns for any\
      \ string: one starting with '0' (0101...) and one starting with '1' (1010...).\
      \ \n\nAs we slide a window of size $n$ across the doubled string, we maintain\
      \ counts of how many characters in the current window differ from the corresponding\
      \ characters in the two target patterns. For each position, we update the mismatch\
      \ counts by adding the contribution of the new character entering the window and\
      \ removing the contribution of the character leaving the window. The minimum mismatch\
      \ count observed across all windows and both patterns provides the minimum number\
      \ of type-2 operations required."
    time_complexity: O(n), where n is the length of the binary string. We iterate through
      a doubled version of the string (length 2n) exactly once, performing constant-time
      updates at each step of the sliding window.
    space_complexity: O(n), where n is the length of the binary string. This space is
      used to store the doubled string (s + s) in most languages. In the C solution,
      the space complexity is O(1) by using modulo indexing on the original string.
    elapsed_time: 313.71537160873413
    model: gemini-3-flash-preview
    generated_at: '2026-03-07 01:23:03 '
---

## Problem #1888: Minimum Number of Flips to Make the Binary String Alternating

**Difficulty:** Medium

**Topics:** String, Dynamic Programming, Sliding Window

## Problem Description

<p>You are given a binary string <code>s</code>. You are allowed to perform two types of operations on the string in any sequence:</p>

<ul>
	<li><strong>Type-1: Remove</strong> the character at the start of the string <code>s</code> and <strong>append</strong> it to the end of the string.</li>
	<li><strong>Type-2: Pick</strong> any character in <code>s</code> and <strong>flip</strong> its value, i.e., if its value is <code>&#39;0&#39;</code> it becomes <code>&#39;1&#39;</code> and vice-versa.</li>
</ul>

<p>Return <em>the <strong>minimum</strong> number of <strong>type-2</strong> operations you need to perform</em> <em>such that </em><code>s</code> <em>becomes <strong>alternating</strong>.</em></p>

<p>The string is called <strong>alternating</strong> if no two adjacent characters are equal.</p>

<ul>
	<li>For example, the strings <code>&quot;010&quot;</code> and <code>&quot;1010&quot;</code> are alternating, while the string <code>&quot;0100&quot;</code> is not.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;111000&quot;
<strong>Output:</strong> 2
<strong>Explanation</strong>: Use the first operation two times to make s = &quot;100011&quot;.
Then, use the second operation on the third and sixth elements to make s = &quot;10<u>1</u>01<u>0</u>&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;010&quot;
<strong>Output:</strong> 0
<strong>Explanation</strong>: The string is already alternating.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;1110&quot;
<strong>Output:</strong> 1
<strong>Explanation</strong>: Use the second operation on the second element to make s = &quot;1<u>0</u>10&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
</ul>


## Hints

1. Note what actually matters is how many 0s and 1s are in odd and even positions

2. For every cyclic shift we need to count how many 0s and 1s are at each parity and convert the minimum between them for each parity

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem is solved using a sliding window approach on a doubled version of the input string. By concatenating the string with itself ($s + s$), all possible cyclic shifts of length $n$ are represented as contiguous substrings of length $n$. There are only two possible target alternating patterns for any string: one starting with '0' (0101...) and one starting with '1' (1010...). 

As we slide a window of size $n$ across the doubled string, we maintain counts of how many characters in the current window differ from the corresponding characters in the two target patterns. For each position, we update the mismatch counts by adding the contribution of the new character entering the window and removing the contribution of the character leaving the window. The minimum mismatch count observed across all windows and both patterns provides the minimum number of type-2 operations required.

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
    int minFlips(string s) {
        int n = s.length();
        string s2 = s + s;
        int diff1 = 0, diff2 = 0;
        int ans = n;
        for (int i = 0; i < 2 * n; i++) {
            if (s2[i] != (i % 2 == 0 ? '0' : '1')) diff1++;
            if (s2[i] != (i % 2 == 0 ? '1' : '0')) diff2++;
            if (i >= n) {
                if (s2[i - n] != ((i - n) % 2 == 0 ? '0' : '1')) diff1--;
                if (s2[i - n] != ((i - n) % 2 == 0 ? '1' : '0')) diff2--;
            }
            if (i >= n - 1) {
                if (diff1 < ans) ans = diff1;
                if (diff2 < ans) ans = diff2;
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
    public int minFlips(String s) {
        int n = s.length();
        String s2 = s + s;
        int diff1 = 0, diff2 = 0;
        int ans = n;
        for (int i = 0; i < 2 * n; i++) {
            if (s2.charAt(i) != (i % 2 == 0 ? '0' : '1')) diff1++;
            if (s2.charAt(i) != (i % 2 == 0 ? '1' : '0')) diff2++;
            if (i >= n) {
                if (s2.charAt(i - n) != ((i - n) % 2 == 0 ? '0' : '1')) diff1--;
                if (s2.charAt(i - n) != ((i - n) % 2 == 0 ? '1' : '0')) diff2--;
            }
            if (i >= n - 1) {
                ans = Math.min(ans, Math.min(diff1, diff2));
            }
        }
        return ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        s2 = s + s
        ans = n
        diff1 = 0
        diff2 = 0
        for i in range(2 * n):
            if s2[i] != ('0' if i % 2 == 0 else '1'):
                diff1 += 1
            if s2[i] != ('1' if i % 2 == 0 else '0'):
                diff2 += 1
            if i >= n:
                if s2[i - n] != ('0' if (i - n) % 2 == 0 else '1'):
                    diff1 -= 1
                if s2[i - n] != ('1' if (i - n) % 2 == 0 else '0'):
                    diff2 -= 1
            if i >= n - 1:
                if diff1 < ans: ans = diff1
                if diff2 < ans: ans = diff2
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s2 = s + s
        ans = n
        diff1 = 0
        diff2 = 0
        for i in range(2 * n):
            if s2[i] != ('0' if i % 2 == 0 else '1'):
                diff1 += 1
            if s2[i] != ('1' if i % 2 == 0 else '0'):
                diff2 += 1
            if i >= n:
                if s2[i - n] != ('0' if (i - n) % 2 == 0 else '1'):
                    diff1 -= 1
                if s2[i - n] != ('1' if (i - n) % 2 == 0 else '0'):
                    diff2 -= 1
            if i >= n - 1:
                ans = min(ans, diff1, diff2)
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int minFlips(char* s) {
    int n = 0;
    while (s[n] != '\0') n++;
    int diff1 = 0, diff2 = 0;
    int ans = n;
    for (int i = 0; i < 2 * n; i++) {
        if (s[i % n] != (i % 2 == 0 ? '0' : '1')) diff1++;
        if (s[i % n] != (i % 2 == 0 ? '1' : '0')) diff2++;
        if (i >= n) {
            if (s[(i - n) % n] != ((i - n) % 2 == 0 ? '0' : '1')) diff1--;
            if (s[(i - n) % n] != ((i - n) % 2 == 0 ? '1' : '0')) diff2--;
        }
        if (i >= n - 1) {
            if (diff1 < ans) ans = diff1;
            if (diff2 < ans) ans = diff2;
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
    public int MinFlips(string s) {
        int n = s.Length;
        string s2 = s + s;
        int diff1 = 0, diff2 = 0;
        int ans = n;
        for (int i = 0; i < 2 * n; i++) {
            if (s2[i] != (i % 2 == 0 ? '0' : '1')) diff1++;
            if (s2[i] != (i % 2 == 0 ? '1' : '0')) diff2++;
            if (i >= n) {
                if (s2[i - n] != ((i - n) % 2 == 0 ? '0' : '1')) diff1--;
                if (s2[i - n] != ((i - n) % 2 == 0 ? '1' : '0')) diff2--;
            }
            if (i >= n - 1) {
                ans = Math.Min(ans, Math.Min(diff1, diff2));
            }
        }
        return ans;
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
var minFlips = function(s) {
    let n = s.length;
    let s2 = s + s;
    let diff1 = 0, diff2 = 0;
    let ans = n;
    for (let i = 0; i < 2 * n; i++) {
        if (s2[i] !== (i % 2 === 0 ? '0' : '1')) diff1++;
        if (s2[i] !== (i % 2 === 0 ? '1' : '0')) diff2++;
        if (i >= n) {
            if (s2[i - n] !== ((i - n) % 2 === 0 ? '0' : '1')) diff1--;
            if (s2[i - n] !== ((i - n) % 2 === 0 ? '1' : '0')) diff2--;
        }
        if (i >= n - 1) {
            ans = Math.min(ans, diff1, diff2);
        }
    }
    return ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minFlips(s: string): number {
    const n = s.length;
    const s2 = s + s;
    let diff1 = 0, diff2 = 0;
    let res = n;
    for (let i = 0; i < 2 * n; i++) {
        if (s2[i] !== (i % 2 === 0 ? '0' : '1')) diff1++;
        if (s2[i] !== (i % 2 === 0 ? '1' : '0')) diff2++;
        if (i >= n) {
            if (s2[i - n] !== ((i - n) % 2 === 0 ? '0' : '1')) diff1--;
            if (s2[i - n] !== ((i - n) % 2 === 0 ? '1' : '0')) diff2--;
        }
        if (i >= n - 1) {
            res = Math.min(res, diff1, diff2);
        }
    }
    return res;
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
    function minFlips($s) {
        $n = strlen($s);
        $s2 = $s . $s;
        $diff1 = 0;
        $diff2 = 0;
        $res = $n;
        for ($i = 0; $i < 2 * $n; $i++) {
            if ($s2[$i] !== ($i % 2 === 0 ? '0' : '1')) $diff1++;
            if ($s2[$i] !== ($i % 2 === 0 ? '1' : '0')) $diff2++;
            if ($i >= $n) {
                if ($s2[$i - $n] !== (($i - $n) % 2 === 0 ? '0' : '1')) $diff1--;
                if ($s2[$i - $n] !== (($i - $n) % 2 === 0 ? '1' : '0')) $diff2--;
            }
            if ($i >= $n - 1) {
                $res = min($res, $diff1, $diff2);
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
    func minFlips(_ s: String) -> Int {
        let n = s.count
        let chars = Array(s + s)
        var diff1 = 0
        var diff2 = 0
        var res = n
        for i in 0..<(2 * n) {
            if chars[i] != (i % 2 == 0 ? "0" : "1") { diff1 += 1 }
            if chars[i] != (i % 2 == 0 ? "1" : "0") { diff2 += 1 }
            if i >= n {
                if chars[i - n] != ((i - n) % 2 == 0 ? "0" : "1") { diff1 -= 1 }
                if chars[i - n] != ((i - n) % 2 == 0 ? "1" : "0") { diff2 -= 1 }
            }
            if i >= n - 1 {
                res = min(res, min(diff1, diff2))
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
    fun minFlips(s: String): Int {
        val n = s.length
        val s2 = s + s
        var diff1 = 0
        var diff2 = 0
        var res = n
        for (i in 0 until 2 * n) {
            if (s2[i] != (if (i % 2 == 0) '0' else '1')) diff1++
            if (s2[i] != (if (i % 2 == 0) '1' else '0')) diff2++
            if (i >= n) {
                if (s2[i - n] != (if ((i - n) % 2 == 0) '0' else '1')) diff1--
                if (s2[i - n] != (if ((i - n) % 2 == 0) '1' else '0')) diff2--
            }
            if (i >= n - 1) {
                val currentMin = if (diff1 < diff2) diff1 else diff2
                if (currentMin < res) res = currentMin
            }
        }
        return res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minFlips(String s) {
    int n = s.length;
    String s2 = s + s;
    int diff1 = 0;
    int diff2 = 0;
    int res = n;
    for (int i = 0; i < 2 * n; i++) {
      if (s2[i] != (i % 2 == 0 ? '0' : '1')) diff1++;
      if (s2[i] != (i % 2 == 0 ? '1' : '0')) diff2++;
      if (i >= n) {
        if (s2[i - n] != ((i - n) % 2 == 0 ? '0' : '1')) diff1--;
        if (s2[i - n] != ((i - n) % 2 == 0 ? '1' : '0')) diff2--;
      }
      if (i >= n - 1) {
        int m = diff1 < diff2 ? diff1 : diff2;
        if (m < res) res = m;
      }
    }
    return res;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minFlips(s string) int {
	n := len(s)
	s2 := s + s
	diff1, diff2 := 0, 0
	res := n
	for i := 0; i < 2*n; i++ {
		if s2[i] != "01"[i%2] {
			diff1++
		}
		if s2[i] != "10"[i%2] {
			diff2++
		}
		if i >= n {
			if s2[i-n] != "01"[(i-n)%2] {
				diff1--
			}
			if s2[i-n] != "10"[(i-n)%2] {
				diff2--
			}
		}
		if i >= n-1 {
			if diff1 < res {
				res = diff1
			}
			if diff2 < res {
				res = diff2
			}
		}
	}
	return res
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def min_flips(s)
  n = s.length
  ss = s + s
  d1 = 0
  d2 = 0
  res = n
  (0...2 * n).each do |i|
    d1 += 1 if ss[i] != (i.even? ? '0' : '1')
    d2 += 1 if ss[i] != (i.even? ? '1' : '0')
    if i >= n
      d1 -= 1 if ss[i - n] != ((i - n).even? ? '0' : '1')
      d2 -= 1 if ss[i - n] != ((i - n).even? ? '1' : '0')
    end
    if i >= n - 1
      res = d1 if d1 < res
      res = d2 if d2 < res
    end
  end
  res
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def minFlips(s: String): Int = {
    val n = s.length
    val ss = s + s
    var d1 = 0
    var d2 = 0
    var res = n
    for (i <- 0 until 2 * n) {
      if (ss(i) != (if (i % 2 == 0) '0' else '1')) d1 += 1
      if (ss(i) != (if (i % 2 == 0) '1' else '0')) d2 += 1
      if (i >= n) {
        if (ss(i - n) != (if ((i - n) % 2 == 0) '0' else '1')) d1 -= 1
        if (ss(i - n) != (if ((i - n) % 2 == 0) '1' else '0')) d2 -= 1
      }
      if (i >= n - 1) {
        res = Math.min(res, Math.min(d1, d2))
      }
    }
    res
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_flips(s: String) -> i32 {
        let n = s.len();
        let ss = s.repeat(2);
        let bytes = ss.as_bytes();
        let mut d1 = 0;
        let mut d2 = 0;
        let mut res = n as i32;
        for i in 0..2 * n {
            if bytes[i] != (if i % 2 == 0 { b'0' } else { b'1' }) { d1 += 1; }
            if bytes[i] != (if i % 2 == 0 { b'1' } else { b'0' }) { d2 += 1; }
            if i >= n {
                if bytes[i - n] != (if (i - n) % 2 == 0 { b'0' } else { b'1' }) { d1 -= 1; }
                if bytes[i - n] != (if (i - n) % 2 == 0 { b'1' } else { b'0' }) { d2 -= 1; }
            }
            if i >= n - 1 {
                res = res.min(d1).min(d2);
            }
        }
        res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-flips s)
  (-> string? exact-integer?)
  (let* ([n (string-length s)]
         [ss (string-append s s)])
    (let-values ([(_d1 _d2 final-min)
                  (for/fold ([d1 0] [d2 0] [min-d n])
                            ([i (in-range (* 2 n))])
                    (let* ([char (string-ref ss i)]
                           [t1 (if (even? i) #\0 #\1)]
                           [t2 (if (even? i) #\1 #\0)]
                           [nd1 (+ d1 (if (char=? char t1) 0 1))]
                           [nd2 (+ d2 (if (char=? char t2) 0 1))])
                      (let-values ([(fd1 fd2)
                                    (if (>= i n)
                                        (let* ([old-char (string-ref ss (- i n))]
                                               [old-t1 (if (even? (- i n)) #\0 #\1)]
                                               [old-t2 (if (even? (- i n)) #\1 #\0)])
                                          (values (- nd1 (if (char=? old-char old-t1) 0 1))
                                                  (- nd2 (if (char=? old-char old-t2) 0 1))))
                                        (values nd1 nd2))])
                        (values fd1 fd2
                                (if (>= i (- n 1))
                                    (min min-d fd1 fd2)
                                    min-d)))))])
      final-min)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_flips(S :: unicode:unicode_binary()) -> integer().
min_flips(S) ->
  N = byte_size(S),
  SS = <<S/binary, S/binary>>,
  Tuple = list_to_tuple(binary_to_list(SS)),
  loop(Tuple, 0, N, 0, 0, N).

loop(Tuple, I, N, D1, D2, MinD) when I < 2 * N ->
  Char = element(I + 1, Tuple),
  T1 = if I rem 2 =:= 0 -> $0; true -> $1 end,
  T2 = if I rem 2 =:= 0 -> $1; true -> $0 end,
  ND1 = if Char =/= T1 -> D1 + 1; true -> D1 end,
  ND2 = if Char =/= T2 -> D2 + 1; true -> D2 end,
  {FD1, FD2} = if I >= N ->
    CharOld = element(I - N + 1, Tuple),
    T1Old = if (I - N) rem 2 =:= 0 -> $0; true -> $1 end,
    T2Old = if (I - N) rem 2 =:= 0 -> $1; true -> $0 end,
    {if CharOld =/= T1Old -> ND1 - 1; true -> ND1 end,
     if CharOld =/= T2Old -> ND2 - 1; true -> ND2 end};
    true -> {ND1, ND2}
  end,
  NMinD = if I >= N - 1 ->
    M = if FD1 < FD2 -> FD1; true -> FD2 end,
    if M < MinD -> M; true -> MinD end;
    true -> MinD
  end,
  loop(Tuple, I + 1, N, FD1, FD2, NMinD);
loop(_, _, _, _, _, MinD) ->
  MinD.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_flips(s :: String.t) :: integer
  def min_flips(s) do
    n = String.length(s)
    ss = s <> s
    chars = ss |> String.to_charlist() |> List.to_tuple()
    reduce_flips(chars, 0, n, 0, 0, n)
  end

  defp reduce_flips(_chars, i, n, _d1, _d2, min_d) when i >= 2 * n, do: min_d
  defp reduce_flips(chars, i, n, d1, d2, min_d) do
    char = elem(chars, i)
    t1 = if rem(i, 2) == 0, do: ?0, else: ?1
    t2 = if rem(i, 2) == 0, do: ?1, else: ?0
    nd1 = d1 + (if char != t1, do: 1, else: 0)
    nd2 = d2 + (if char != t2, do: 1, else: 0)
    {fd1, fd2} = if i >= n do
      old_char = elem(chars, i - n)
      old_t1 = if rem(i - n, 2) == 0, do: ?0, else: ?1
      old_t2 = if rem(i - n, 2) == 0, do: ?1, else: ?0
      {nd1 - (if old_char != old_t1, do: 1, else: 0), nd2 - (if old_char != old_t2, do: 1, else: 0)}
    else
      {nd1, nd2}
    end
    new_min_d = if i >= n - 1, do: min(min_d, min(fd1, fd2)), else: min_d
    reduce_flips(chars, i + 1, n, fd1, fd2, new_min_d)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n), where n is the length of the binary string. We iterate through a doubled version of the string (length 2n) exactly once, performing constant-time updates at each step of the sliding window.
- **Space Complexity:** O(n), where n is the length of the binary string. This space is used to store the doubled string (s + s) in most languages. In the C solution, the space complexity is O(1) by using modulo indexing on the original string.
