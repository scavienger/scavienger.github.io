---
layout: post
title: "Maximize Active Section with Trade I"
date: 2026-07-21 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Enumeration"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/maximize-active-section-with-trade-i/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxActiveSectionsAfterTrade(string s)\
        \ {\n        int n = s.length();\n        int count1 = 0;\n        for (char\
        \ c : s) {\n            if (c == '1') count1++;\n        }\n\n        vector<int>\
        \ z_lengths;\n        for (int i = 0; i < n; ) {\n            if (s[i] == '0')\
        \ {\n                int start = i;\n                while (i < n && s[i] ==\
        \ '0') {\n                    i++;\n                }\n                z_lengths.push_back(i\
        \ - start);\n            } else {\n                i++;\n            }\n   \
        \     }\n\n        int max_delta = 0;\n        int m = z_lengths.size();\n \
        \       if (m >= 2) {\n            for (int i = 0; i < m - 1; i++) {\n     \
        \           if (z_lengths[i] + z_lengths[i + 1] > max_delta) {\n           \
        \         max_delta = z_lengths[i] + z_lengths[i + 1];\n                }\n\
        \            }\n        }\n\n        return count1 + max_delta;\n    }\n};"
      java: "class Solution {\n    public int maxActiveSectionsAfterTrade(String s)\
        \ {\n        int n = s.length();\n        int count1 = 0;\n        for (int\
        \ i = 0; i < n; i++) {\n            if (s.charAt(i) == '1') count1++;\n    \
        \    }\n\n        java.util.List<Integer> zLengths = new java.util.ArrayList<>();\n\
        \        for (int i = 0; i < n; ) {\n            if (s.charAt(i) == '0') {\n\
        \                int start = i;\n                while (i < n && s.charAt(i)\
        \ == '0') {\n                    i++;\n                }\n                zLengths.add(i\
        \ - start);\n            } else {\n                i++;\n            }\n   \
        \     }\n\n        int maxDelta = 0;\n        int m = zLengths.size();\n   \
        \     if (m >= 2) {\n            for (int i = 0; i < m - 1; i++) {\n       \
        \         int sum = zLengths.get(i) + zLengths.get(i + 1);\n               \
        \ if (sum > maxDelta) {\n                    maxDelta = sum;\n             \
        \   }\n            }\n        }\n\n        return count1 + maxDelta;\n    }\n\
        }"
      python: "class Solution(object):\n    def maxActiveSectionsAfterTrade(self, s):\n\
        \        \"\"\"\n        :type s: str\n        :rtype: int\n        \"\"\"\n\
        \        count1 = s.count('1')\n        z_lengths = [len(z) for z in s.split('1')\
        \ if z]\n\n        max_delta = 0\n        if len(z_lengths) >= 2:\n        \
        \    for i in range(len(z_lengths) - 1):\n                delta = z_lengths[i]\
        \ + z_lengths[i+1]\n                if delta > max_delta:\n                \
        \    max_delta = delta\n\n        return count1 + max_delta"
      python3: "class Solution:\n    def maxActiveSectionsAfterTrade(self, s: str) ->\
        \ int:\n        count1 = s.count('1')\n        z_lengths = [len(z) for z in\
        \ s.split('1') if z]\n\n        max_delta = 0\n        if len(z_lengths) >=\
        \ 2:\n            for i in range(len(z_lengths) - 1):\n                max_delta\
        \ = max(max_delta, z_lengths[i] + z_lengths[i+1])\n\n        return count1 +\
        \ max_delta"
      c: "#include <string.h>\n#include <stdlib.h>\n\nint maxActiveSectionsAfterTrade(char*\
        \ s) {\n    int n = strlen(s);\n    int count1 = 0;\n    for (int i = 0; i <\
        \ n; i++) {\n        if (s[i] == '1') count1++;\n    }\n\n    int* z_lengths\
        \ = (int*)malloc(n * sizeof(int));\n    int m = 0;\n    for (int i = 0; i <\
        \ n; ) {\n        if (s[i] == '0') {\n            int start = i;\n         \
        \   while (i < n && s[i] == '0') {\n                i++;\n            }\n  \
        \          z_lengths[m++] = i - start;\n        } else {\n            i++;\n\
        \        }\n    }\n\n    int max_delta = 0;\n    if (m >= 2) {\n        for\
        \ (int i = 0; i < m - 1; i++) {\n            int sum = z_lengths[i] + z_lengths[i+1];\n\
        \            if (sum > max_delta) {\n                max_delta = sum;\n    \
        \        }\n        }\n    }\n\n    free(z_lengths);\n    return count1 + max_delta;\n\
        }"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int MaxActiveSectionsAfterTrade(string s) {\n        int totalOnes\
        \ = 0;\n        foreach (char c in s) {\n            if (c == '1') totalOnes++;\n\
        \        }\n\n        string t = \"1\" + s + \"1\";\n        List<int> lengths\
        \ = new List<int>();\n        int currentLen = 1;\n        for (int j = 1; j\
        \ < t.Length; j++) {\n            if (t[j] == t[j - 1]) {\n                currentLen++;\n\
        \            } else {\n                lengths.Add(currentLen);\n          \
        \      currentLen = 1;\n            }\n        }\n        lengths.Add(currentLen);\n\
        \n        int maxDelta = 0;\n        int m = lengths.Count;\n        // i corresponds\
        \ to the block index in the alternating sequence (1s, 0s, 1s, 0s...)\n     \
        \   // We look for a '1' block surrounded by '0' blocks, which must also be\
        \ surrounded by '1' blocks.\n        // This means B_i is '1's (i is even),\
        \ and B_{i-1}, B_{i+1} are '0's (i is even and 0 < i < m-1).\n        // The\
        \ merged block (B_{i-1}, B_i, B_{i+1}) must be surrounded by '1's (B_{i-2} and\
        \ B_{i+2}).\n        // Thus, 2 <= i <= m - 3 and i must be even.\n        for\
        \ (int i = 2; i <= m - 3; i += 2) {\n            int delta = lengths[i - 1]\
        \ + lengths[i + 1];\n            if (delta > maxDelta) {\n                maxDelta\
        \ = delta;\n            }\n        }\n\n        return totalOnes + maxDelta;\n\
        \    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {number}\n */\nvar maxActiveSectionsAfterTrade\
        \ = function(s) {\n    let totalOnes = 0;\n    for (let i = 0; i < s.length;\
        \ i++) {\n        if (s[i] === '1') totalOnes++;\n    }\n\n    const t = \"\
        1\" + s + \"1\";\n    const lengths = [];\n    let currentLen = 1;\n    for\
        \ (let j = 1; j < t.length; j++) {\n        if (t[j] === t[j - 1]) {\n     \
        \       currentLen++;\n        } else {\n            lengths.push(currentLen);\n\
        \            currentLen = 1;\n        }\n    }\n    lengths.push(currentLen);\n\
        \n    let maxDelta = 0;\n    const m = lengths.length;\n    for (let i = 2;\
        \ i <= m - 3; i += 2) {\n        let delta = lengths[i - 1] + lengths[i + 1];\n\
        \        if (delta > maxDelta) {\n            maxDelta = delta;\n        }\n\
        \    }\n\n    return totalOnes + maxDelta;\n};"
      typescript: "function maxActiveSectionsAfterTrade(s: string): number {\n    let\
        \ totalOnes: number = 0;\n    for (let i = 0; i < s.length; i++) {\n       \
        \ if (s[i] === '1') totalOnes++;\n    }\n\n    const t: string = \"1\" + s +\
        \ \"1\";\n    const lengths: number[] = [];\n    let currentLen: number = 1;\n\
        \    for (let j = 1; j < t.length; j++) {\n        if (t[j] === t[j - 1]) {\n\
        \            currentLen++;\n        } else {\n            lengths.push(currentLen);\n\
        \            currentLen = 1;\n        }\n    }\n    lengths.push(currentLen);\n\
        \n    let maxDelta: number = 0;\n    const m: number = lengths.length;\n   \
        \ for (let i = 2; i <= m - 3; i += 2) {\n        let delta: number = lengths[i\
        \ - 1] + lengths[i + 1];\n        if (delta > maxDelta) {\n            maxDelta\
        \ = delta;\n        }\n    }\n\n    return totalOnes + maxDelta;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return Integer\n\
        \     */\n    function maxActiveSectionsAfterTrade($s) {\n        $totalOnes\
        \ = 0;\n        $n = strlen($s);\n        for ($i = 0; $i < $n; $i++) {\n  \
        \          if ($s[$i] === '1') {\n                $totalOnes++;\n          \
        \  }\n        }\n\n        $t = \"1\" . $s . \"1\";\n        $tLen = strlen($t);\n\
        \        $lengths = [];\n        $currentLen = 1;\n        for ($j = 1; $j <\
        \ $tLen; $j++) {\n            if ($t[$j] === $t[$j - 1]) {\n               \
        \ $currentLen++;\n            } else {\n                $lengths[] = $currentLen;\n\
        \                $currentLen = 1;\n            }\n        }\n        $lengths[]\
        \ = $currentLen;\n\n        $maxDelta = 0;\n        $m = count($lengths);\n\
        \        for ($i = 2; $i <= $m - 3; $i += 2) {\n            $delta = $lengths[$i\
        \ - 1] + $lengths[$i + 1];\n            if ($delta > $maxDelta) {\n        \
        \        $maxDelta = $delta;\n            }\n        }\n\n        return $totalOnes\
        \ + $maxDelta;\n    }\n}"
      swift: "class Solution {\n    func maxActiveSectionsAfterTrade(_ s: String) ->\
        \ Int {\n        var totalOnes = 0\n        for char in s {\n            if\
        \ char == \"1\" {\n                totalOnes += 1\n            }\n        }\n\
        \n        let t = \"1\" + s + \"1\"\n        let chars = Array(t)\n        var\
        \ lengths: [Int] = []\n        var currentLen = 1\n\n        if chars.count\
        \ > 1 {\n            for j in 1..<chars.count {\n                if chars[j]\
        \ == chars[j - 1] {\n                    currentLen += 1\n                }\
        \ else {\n                    lengths.append(currentLen)\n                 \
        \   currentLen = 1\n                }\n            }\n        }\n        lengths.append(currentLen)\n\
        \n        var maxDelta = 0\n        let m = lengths.count\n        if m >= 5\
        \ {\n            for i in stride(from: 2, through: m - 3, by: 2) {\n       \
        \         let delta = lengths[i - 1] + lengths[i + 1]\n                if delta\
        \ > maxDelta {\n                    maxDelta = delta\n                }\n  \
        \          }\n        }\n\n        return totalOnes + maxDelta\n    }\n}"
      kotlin: "class Solution {\n    fun maxActiveSectionsAfterTrade(s: String): Int\
        \ {\n        var initialOnes = 0\n        for (c in s) {\n            if (c\
        \ == '1') initialOnes++\n        }\n\n        val t = \"1\" + s + \"1\"\n  \
        \      val segments = mutableListOf<Int>()\n        var currentLen = 1\n   \
        \     for (i in 1 until t.length) {\n            if (t[i] == t[i - 1]) {\n \
        \               currentLen++\n            } else {\n                segments.add(currentLen)\n\
        \                currentLen = 1\n            }\n        }\n        segments.add(currentLen)\n\
        \n        val k = (segments.size - 1) / 2\n        var maxGain = 0\n       \
        \ for (i in 1 until k) {\n            val gain = segments[2 * i - 1] + segments[2\
        \ * i + 1]\n            if (gain > maxGain) {\n                maxGain = gain\n\
        \            }\n        }\n\n        return initialOnes + maxGain\n    }\n}"
      dart: "class Solution {\n  int maxActiveSectionsAfterTrade(String s) {\n    int\
        \ initialOnes = 0;\n    for (int i = 0; i < s.length; i++) {\n      if (s[i]\
        \ == '1') {\n        initialOnes++;\n      }\n    }\n\n    String t = \"1\"\
        \ + s + \"1\";\n    List<int> segments = [];\n    int currentLen = 1;\n    for\
        \ (int i = 1; i < t.length; i++) {\n      if (t[i] == t[i - 1]) {\n        currentLen++;\n\
        \      } else {\n        segments.add(currentLen);\n        currentLen = 1;\n\
        \      }\n    }\n    segments.add(currentLen);\n\n    int k = (segments.length\
        \ - 1) ~/ 2;\n    int maxGain = 0;\n    for (int i = 1; i < k; i++) {\n    \
        \  int gain = segments[2 * i - 1] + segments[2 * i + 1];\n      if (gain > maxGain)\
        \ {\n        maxGain = gain;\n      }\n    }\n\n    return initialOnes + maxGain;\n\
        \  }\n}"
      go: "func maxActiveSectionsAfterTrade(s string) int {\n\tinitialOnes := 0\n\t\
        for _, c := range s {\n\t\tif c == '1' {\n\t\t\tinitialOnes++\n\t\t}\n\t}\n\n\
        \tt := \"1\" + s + \"1\"\n\tsegments := []int{}\n\tcurrentLen := 1\n\tfor i\
        \ := 1; i < len(t); i++ {\n\t\tif t[i] == t[i-1] {\n\t\t\tcurrentLen++\n\t\t\
        } else {\n\t\t\tsegments = append(segments, currentLen)\n\t\t\tcurrentLen =\
        \ 1\n\t\t}\n\t}\n\tsegments = append(segments, currentLen)\n\n\tk := (len(segments)\
        \ - 1) / 2\n\tmaxGain := 0\n\tfor i := 1; i < k; i++ {\n\t\tgain := segments[2*i-1]\
        \ + segments[2*i+1]\n\t\tif gain > maxGain {\n\t\t\tmaxGain = gain\n\t\t}\n\t\
        }\n\n\treturn initialOnes + maxGain\n}"
      ruby: "def max_active_sections_after_trade(s)\n  initial_ones = s.count('1')\n\
        \  t = '1' + s + '1'\n  segments = []\n  current_len = 1\n  (1...t.length).each\
        \ do |i|\n    if t[i] == t[i - 1]\n      current_len += 1\n    else\n      segments\
        \ << current_len\n      current_len = 1\n    end\n  end\n  segments << current_len\n\
        \n  k = (segments.size - 1) / 2\n  max_gain = 0\n  (1...k).each do |i|\n   \
        \ gain = segments[2 * i - 1] + segments[2 * i + 1]\n    max_gain = gain if gain\
        \ > max_gain\n  end\n\n  initial_ones + max_gain\nend"
      scala: "import scala.collection.mutable.ArrayBuffer\n\nobject Solution {\n   \
        \ def maxActiveSectionsAfterTrade(s: String): Int = {\n        var initialOnes\
        \ = 0\n        var i = 0\n        while (i < s.length) {\n            if (s(i)\
        \ == '1') initialOnes += 1\n            i += 1\n        }\n\n        val t =\
        \ \"1\" + s + \"1\"\n        val segments = ArrayBuffer[Int]()\n        var\
        \ currentLen = 1\n        var j = 1\n        while (j < t.length) {\n      \
        \      if (t(j) == t(j - 1)) {\n                currentLen += 1\n          \
        \  } else {\n                segments += currentLen\n                currentLen\
        \ = 1\n            }\n            j += 1\n        }\n        segments += currentLen\n\
        \n        val k = (segments.size - 1) / 2\n        var maxGain = 0\n       \
        \ var m = 1\n        while (m < k) {\n            val gain = segments(2 * m\
        \ - 1) + segments(2 * m + 1)\n            if (gain > maxGain) maxGain = gain\n\
        \            m += 1\n        }\n\n        initialOnes + maxGain\n    }\n}"
      rust: "impl Solution {\n    pub fn max_active_sections_after_trade(s: String)\
        \ -> i32 {\n        let s_bytes = s.as_bytes();\n        let initial_ones =\
        \ s_bytes.iter().filter(|&&b| b == b'1').count() as i32;\n\n        let mut\
        \ t = Vec::with_capacity(s.len() + 2);\n        t.push(b'1');\n        t.extend_from_slice(s_bytes);\n\
        \        t.push(b'1');\n\n        let mut block_lens = Vec::new();\n       \
        \ if t.is_empty() { return initial_ones; }\n\n        let mut current_len =\
        \ 1;\n        for i in 1..t.len() {\n            if t[i] == t[i-1] {\n     \
        \           current_len += 1;\n            } else {\n                block_lens.push(current_len);\n\
        \                current_len = 1;\n            }\n        }\n        block_lens.push(current_len);\n\
        \n        let mut max_gain = 0;\n        let k = block_lens.len();\n       \
        \ let mut i = 2;\n        while i < k - 2 {\n            let gain = block_lens[i-1]\
        \ + block_lens[i+1];\n            if gain > max_gain {\n                max_gain\
        \ = gain;\n            }\n            i += 2;\n        }\n\n        initial_ones\
        \ + max_gain\n    }\n}"
      racket: "(define/contract (max-active-sections-after-trade s)\n  (-> string? exact-integer?)\n\
        \  (let* ([s-list (string->list s)]\n         [initial-ones (length (filter\
        \ (lambda (c) (char=? c #\\1)) s-list))]\n         [t (append '(#\\1) s-list\
        \ '(#\\1))]\n         [block-lens-list (if (null? t) '()\n                 \
        \             (let loop ([lst (cdr t)] [curr (car t)] [len 1] [acc '()])\n \
        \                               (cond [(null? lst) (reverse (cons len acc))]\n\
        \                                      [(char=? (car lst) curr) (loop (cdr lst)\
        \ curr (+ len 1) acc)]\n                                      [else (loop (cdr\
        \ lst) (car lst) 1 (cons len acc))])))]\n         [block-lens (list->vector\
        \ block-lens-list)]\n         [k (vector-length block-lens)])\n    (let loop\
        \ ([i 2] [max-gain 0])\n      (if (>= i (- k 2))\n          (+ initial-ones\
        \ max-gain)\n          (let ([gain (+ (vector-ref block-lens (- i 1)) (vector-ref\
        \ block-lens (+ i 1)))])\n            (loop (+ i 2) (max max-gain gain)))))))"
      erlang: "-spec max_active_sections_after_trade(S :: unicode:unicode_binary())\
        \ -> integer().\nmax_active_sections_after_trade(S) ->\n  SList = binary_to_list(S),\n\
        \  InitialOnes = length([C || C <- SList, C =:= $1]),\n  T = [$1 | SList] ++\
        \ [$1],\n  BlockLens = get_block_lens(T, undefined, 0, []),\n  BlockVec = list_to_tuple(BlockLens),\n\
        \  K = tuple_size(BlockVec),\n  MaxGain = find_max_gain(3, K, BlockVec, 0),\n\
        \  InitialOnes + MaxGain.\n\nget_block_lens([], _Curr, Len, Acc) ->\n  lists:reverse([Len\
        \ | Acc]);\nget_block_lens([H | T], undefined, 0, Acc) ->\n  get_block_lens(T,\
        \ H, 1, Acc);\nget_block_lens([H | T], H, Len, Acc) ->\n  get_block_lens(T,\
        \ H, Len + 1, Acc);\nget_block_lens([H | T], _Curr, Len, Acc) ->\n  get_block_lens(T,\
        \ H, 1, [Len | Acc]).\n\nfind_max_gain(I, K, Vec, MaxG) when I > K - 2 -> MaxG;\n\
        find_max_gain(I, K, Vec, MaxG) ->\n  Gain = element(I - 1, Vec) + element(I\
        \ + 1, Vec),\n  find_max_gain(I + 2, K, Vec, max(MaxG, Gain))."
      elixir: "defmodule Solution do\n  @spec max_active_sections_after_trade(s :: String.t)\
        \ :: integer\n  def max_active_sections_after_trade(s) do\n    s_chars = String.to_charlist(s)\n\
        \    initial_ones = Enum.count(s_chars, &(&1 == ?1))\n    t = [?1 | s_chars]\
        \ ++ [?1]\n\n    block_lens = \n      t \n      |> Enum.chunk_by(& &1)\n   \
        \   |> Enum.map(&length/1)\n\n    k = length(block_lens)\n    if k < 5 do\n\
        \      initial_ones\n    else\n      block_vec = List.to_tuple(block_lens)\n\
        \      max_gain = \n        2..(k-3)\n        |> Enum.filter(&(rem(&1, 2) ==\
        \ 0))\n        |> Enum.map(fn i -> elem(block_vec, i-1) + elem(block_vec, i+1)\
        \ end)\n        |> Enum.max(fn -> 0 end)\n      initial_ones + max_gain\n  \
        \  end\n  end\nend"
    approach: 'The problem asks us to maximize the count of ''1''s after at most one
      trade. By augmenting the string $s$ with ''1''s at both ends (forming $t = ''1''
      + s + ''1''$), we ensure that any trade must involve a block of ''1''s within
      the original string that is flanked by ''0''s. A trade consists of converting
      such a ''1'' block into ''0''s and then converting an resulting contiguous ''0''
      block into ''1''s. To maximize the result, we should pick a ''1'' block surrounded
      by two ''0'' blocks ($Z_{i-1}$ and $Z_i$) and then convert the newly merged ''0''
      block (formed by $Z_{i-1}$, the original ''1'' block, and $Z_i$) into ''1''s.
      The net gain in the number of active sections from this trade is exactly the sum
      of the lengths of the two ''0'' blocks flanking that ''1'' block.


      To implement this, we first count the initial number of ''1''s in the string $s$.
      Then, we identify the lengths of all contiguous blocks of ''0''s in $s$. If there
      are at least two such ''0'' blocks, they must be separated by at least one ''1''
      block that is surrounded by ''0''s. The maximum possible gain is the maximum sum
      of lengths of any two adjacent ''0'' blocks. If there are fewer than two ''0''
      blocks, no ''1'' block can be surrounded by ''0''s (even with augmentation), so
      no valid trade is possible. The final answer is the initial count of ''1''s plus
      the maximum gain discovered.'
    time_complexity: 'O(n) where n is the length of the string s. We iterate through
      the string a constant number of times: once to count the initial ''1''s, once
      to identify the lengths of ''0'' blocks, and once to find the maximum sum of adjacent
      ''0'' block lengths.'
    space_complexity: O(n) to store the lengths of the contiguous '0' blocks. In the
      worst case (e.g., "010101..."), there are approximately n/2 such blocks, requiring
      O(n) space. This can be optimized to O(1) by keeping track of only the current
      and previous '0' block lengths during a single pass.
    elapsed_time: 794.4218153953552
    model: gemini-3-flash-preview
    generated_at: '2026-07-21 02:09:34 '
---

## Problem #3499: Maximize Active Section with Trade I

**Difficulty:** Medium

**Topics:** String, Enumeration

## Problem Description

<p>You are given a binary string <code>s</code> of length <code>n</code>, where:</p>

<ul>
	<li><code>&#39;1&#39;</code> represents an <strong>active</strong> section.</li>
	<li><code>&#39;0&#39;</code> represents an <strong>inactive</strong> section.</li>
</ul>

<p>You can perform <strong>at most one trade</strong> to maximize the number of active sections in <code>s</code>. In a trade, you:</p>

<ul>
	<li>Convert a contiguous block of <code>&#39;1&#39;</code>s that is surrounded by <code>&#39;0&#39;</code>s to all <code>&#39;0&#39;</code>s.</li>
	<li>Afterward, convert a contiguous block of <code>&#39;0&#39;</code>s that is surrounded by <code>&#39;1&#39;</code>s to all <code>&#39;1&#39;</code>s.</li>
</ul>

<p>Return the <strong>maximum</strong> number of active sections in <code>s</code> after making the optimal trade.</p>

<p><strong>Note:</strong> Treat <code>s</code> as if it is <strong>augmented</strong> with a <code>&#39;1&#39;</code> at both ends, forming <code>t = &#39;1&#39; + s + &#39;1&#39;</code>. The augmented <code>&#39;1&#39;</code>s <strong>do not</strong> contribute to the final count.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;01&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>Because there is no block of <code>&#39;1&#39;</code>s surrounded by <code>&#39;0&#39;</code>s, no valid trade is possible. The maximum number of active sections is 1.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;0100&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>String <code>&quot;0100&quot;</code> &rarr; Augmented to <code>&quot;101001&quot;</code>.</li>
	<li>Choose <code>&quot;0100&quot;</code>, convert <code>&quot;10<u><strong>1</strong></u>001&quot;</code> &rarr; <code>&quot;1<u><strong>0000</strong></u>1&quot;</code> &rarr; <code>&quot;1<u><strong>1111</strong></u>1&quot;</code>.</li>
	<li>The final string without augmentation is <code>&quot;1111&quot;</code>. The maximum number of active sections is 4.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;1000100&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">7</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>String <code>&quot;1000100&quot;</code> &rarr; Augmented to <code>&quot;110001001&quot;</code>.</li>
	<li>Choose <code>&quot;000100&quot;</code>, convert <code>&quot;11000<u><strong>1</strong></u>001&quot;</code> &rarr; <code>&quot;11<u><strong>000000</strong></u>1&quot;</code> &rarr; <code>&quot;11<u><strong>111111</strong></u>1&quot;</code>.</li>
	<li>The final string without augmentation is <code>&quot;1111111&quot;</code>. The maximum number of active sections is 7.</li>
</ul>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;01010&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>String <code>&quot;01010&quot;</code> &rarr; Augmented to <code>&quot;1010101&quot;</code>.</li>
	<li>Choose <code>&quot;010&quot;</code>, convert <code>&quot;10<u><strong>1</strong></u>0101&quot;</code> &rarr; <code>&quot;1<u><strong>000</strong></u>101&quot;</code> &rarr; <code>&quot;1<u><strong>111</strong></u>101&quot;</code>.</li>
	<li>The final string without augmentation is <code>&quot;11110&quot;</code>. The maximum number of active sections is 4.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code></li>
</ul>


## Hints

1. Split the string into several zero-one segments.

2. For each one-segment, if it has two neighbors (i.e., it is surrounded by two zero-segments), the total sum of their lengths is one of the candidates for `delta`.

3. Find the maximum `delta` and add it to the total number of ones in the string.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks us to maximize the count of '1's after at most one trade. By augmenting the string $s$ with '1's at both ends (forming $t = '1' + s + '1'$), we ensure that any trade must involve a block of '1's within the original string that is flanked by '0's. A trade consists of converting such a '1' block into '0's and then converting an resulting contiguous '0' block into '1's. To maximize the result, we should pick a '1' block surrounded by two '0' blocks ($Z_{i-1}$ and $Z_i$) and then convert the newly merged '0' block (formed by $Z_{i-1}$, the original '1' block, and $Z_i$) into '1's. The net gain in the number of active sections from this trade is exactly the sum of the lengths of the two '0' blocks flanking that '1' block.

To implement this, we first count the initial number of '1's in the string $s$. Then, we identify the lengths of all contiguous blocks of '0's in $s$. If there are at least two such '0' blocks, they must be separated by at least one '1' block that is surrounded by '0's. The maximum possible gain is the maximum sum of lengths of any two adjacent '0' blocks. If there are fewer than two '0' blocks, no '1' block can be surrounded by '0's (even with augmentation), so no valid trade is possible. The final answer is the initial count of '1's plus the maximum gain discovered.

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
    int maxActiveSectionsAfterTrade(string s) {
        int n = s.length();
        int count1 = 0;
        for (char c : s) {
            if (c == '1') count1++;
        }

        vector<int> z_lengths;
        for (int i = 0; i < n; ) {
            if (s[i] == '0') {
                int start = i;
                while (i < n && s[i] == '0') {
                    i++;
                }
                z_lengths.push_back(i - start);
            } else {
                i++;
            }
        }

        int max_delta = 0;
        int m = z_lengths.size();
        if (m >= 2) {
            for (int i = 0; i < m - 1; i++) {
                if (z_lengths[i] + z_lengths[i + 1] > max_delta) {
                    max_delta = z_lengths[i] + z_lengths[i + 1];
                }
            }
        }

        return count1 + max_delta;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maxActiveSectionsAfterTrade(String s) {
        int n = s.length();
        int count1 = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '1') count1++;
        }

        java.util.List<Integer> zLengths = new java.util.ArrayList<>();
        for (int i = 0; i < n; ) {
            if (s.charAt(i) == '0') {
                int start = i;
                while (i < n && s.charAt(i) == '0') {
                    i++;
                }
                zLengths.add(i - start);
            } else {
                i++;
            }
        }

        int maxDelta = 0;
        int m = zLengths.size();
        if (m >= 2) {
            for (int i = 0; i < m - 1; i++) {
                int sum = zLengths.get(i) + zLengths.get(i + 1);
                if (sum > maxDelta) {
                    maxDelta = sum;
                }
            }
        }

        return count1 + maxDelta;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        count1 = s.count('1')
        z_lengths = [len(z) for z in s.split('1') if z]

        max_delta = 0
        if len(z_lengths) >= 2:
            for i in range(len(z_lengths) - 1):
                delta = z_lengths[i] + z_lengths[i+1]
                if delta > max_delta:
                    max_delta = delta

        return count1 + max_delta
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        count1 = s.count('1')
        z_lengths = [len(z) for z in s.split('1') if z]

        max_delta = 0
        if len(z_lengths) >= 2:
            for i in range(len(z_lengths) - 1):
                max_delta = max(max_delta, z_lengths[i] + z_lengths[i+1])

        return count1 + max_delta
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <string.h>
#include <stdlib.h>

int maxActiveSectionsAfterTrade(char* s) {
    int n = strlen(s);
    int count1 = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == '1') count1++;
    }

    int* z_lengths = (int*)malloc(n * sizeof(int));
    int m = 0;
    for (int i = 0; i < n; ) {
        if (s[i] == '0') {
            int start = i;
            while (i < n && s[i] == '0') {
                i++;
            }
            z_lengths[m++] = i - start;
        } else {
            i++;
        }
    }

    int max_delta = 0;
    if (m >= 2) {
        for (int i = 0; i < m - 1; i++) {
            int sum = z_lengths[i] + z_lengths[i+1];
            if (sum > max_delta) {
                max_delta = sum;
            }
        }
    }

    free(z_lengths);
    return count1 + max_delta;
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
    public int MaxActiveSectionsAfterTrade(string s) {
        int totalOnes = 0;
        foreach (char c in s) {
            if (c == '1') totalOnes++;
        }

        string t = "1" + s + "1";
        List<int> lengths = new List<int>();
        int currentLen = 1;
        for (int j = 1; j < t.Length; j++) {
            if (t[j] == t[j - 1]) {
                currentLen++;
            } else {
                lengths.Add(currentLen);
                currentLen = 1;
            }
        }
        lengths.Add(currentLen);

        int maxDelta = 0;
        int m = lengths.Count;
        // i corresponds to the block index in the alternating sequence (1s, 0s, 1s, 0s...)
        // We look for a '1' block surrounded by '0' blocks, which must also be surrounded by '1' blocks.
        // This means B_i is '1's (i is even), and B_{i-1}, B_{i+1} are '0's (i is even and 0 < i < m-1).
        // The merged block (B_{i-1}, B_i, B_{i+1}) must be surrounded by '1's (B_{i-2} and B_{i+2}).
        // Thus, 2 <= i <= m - 3 and i must be even.
        for (int i = 2; i <= m - 3; i += 2) {
            int delta = lengths[i - 1] + lengths[i + 1];
            if (delta > maxDelta) {
                maxDelta = delta;
            }
        }

        return totalOnes + maxDelta;
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
var maxActiveSectionsAfterTrade = function(s) {
    let totalOnes = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '1') totalOnes++;
    }

    const t = "1" + s + "1";
    const lengths = [];
    let currentLen = 1;
    for (let j = 1; j < t.length; j++) {
        if (t[j] === t[j - 1]) {
            currentLen++;
        } else {
            lengths.push(currentLen);
            currentLen = 1;
        }
    }
    lengths.push(currentLen);

    let maxDelta = 0;
    const m = lengths.length;
    for (let i = 2; i <= m - 3; i += 2) {
        let delta = lengths[i - 1] + lengths[i + 1];
        if (delta > maxDelta) {
            maxDelta = delta;
        }
    }

    return totalOnes + maxDelta;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxActiveSectionsAfterTrade(s: string): number {
    let totalOnes: number = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '1') totalOnes++;
    }

    const t: string = "1" + s + "1";
    const lengths: number[] = [];
    let currentLen: number = 1;
    for (let j = 1; j < t.length; j++) {
        if (t[j] === t[j - 1]) {
            currentLen++;
        } else {
            lengths.push(currentLen);
            currentLen = 1;
        }
    }
    lengths.push(currentLen);

    let maxDelta: number = 0;
    const m: number = lengths.length;
    for (let i = 2; i <= m - 3; i += 2) {
        let delta: number = lengths[i - 1] + lengths[i + 1];
        if (delta > maxDelta) {
            maxDelta = delta;
        }
    }

    return totalOnes + maxDelta;
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
    function maxActiveSectionsAfterTrade($s) {
        $totalOnes = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '1') {
                $totalOnes++;
            }
        }

        $t = "1" . $s . "1";
        $tLen = strlen($t);
        $lengths = [];
        $currentLen = 1;
        for ($j = 1; $j < $tLen; $j++) {
            if ($t[$j] === $t[$j - 1]) {
                $currentLen++;
            } else {
                $lengths[] = $currentLen;
                $currentLen = 1;
            }
        }
        $lengths[] = $currentLen;

        $maxDelta = 0;
        $m = count($lengths);
        for ($i = 2; $i <= $m - 3; $i += 2) {
            $delta = $lengths[$i - 1] + $lengths[$i + 1];
            if ($delta > $maxDelta) {
                $maxDelta = $delta;
            }
        }

        return $totalOnes + $maxDelta;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxActiveSectionsAfterTrade(_ s: String) -> Int {
        var totalOnes = 0
        for char in s {
            if char == "1" {
                totalOnes += 1
            }
        }

        let t = "1" + s + "1"
        let chars = Array(t)
        var lengths: [Int] = []
        var currentLen = 1

        if chars.count > 1 {
            for j in 1..<chars.count {
                if chars[j] == chars[j - 1] {
                    currentLen += 1
                } else {
                    lengths.append(currentLen)
                    currentLen = 1
                }
            }
        }
        lengths.append(currentLen)

        var maxDelta = 0
        let m = lengths.count
        if m >= 5 {
            for i in stride(from: 2, through: m - 3, by: 2) {
                let delta = lengths[i - 1] + lengths[i + 1]
                if delta > maxDelta {
                    maxDelta = delta
                }
            }
        }

        return totalOnes + maxDelta
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxActiveSectionsAfterTrade(s: String): Int {
        var initialOnes = 0
        for (c in s) {
            if (c == '1') initialOnes++
        }

        val t = "1" + s + "1"
        val segments = mutableListOf<Int>()
        var currentLen = 1
        for (i in 1 until t.length) {
            if (t[i] == t[i - 1]) {
                currentLen++
            } else {
                segments.add(currentLen)
                currentLen = 1
            }
        }
        segments.add(currentLen)

        val k = (segments.size - 1) / 2
        var maxGain = 0
        for (i in 1 until k) {
            val gain = segments[2 * i - 1] + segments[2 * i + 1]
            if (gain > maxGain) {
                maxGain = gain
            }
        }

        return initialOnes + maxGain
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maxActiveSectionsAfterTrade(String s) {
    int initialOnes = 0;
    for (int i = 0; i < s.length; i++) {
      if (s[i] == '1') {
        initialOnes++;
      }
    }

    String t = "1" + s + "1";
    List<int> segments = [];
    int currentLen = 1;
    for (int i = 1; i < t.length; i++) {
      if (t[i] == t[i - 1]) {
        currentLen++;
      } else {
        segments.add(currentLen);
        currentLen = 1;
      }
    }
    segments.add(currentLen);

    int k = (segments.length - 1) ~/ 2;
    int maxGain = 0;
    for (int i = 1; i < k; i++) {
      int gain = segments[2 * i - 1] + segments[2 * i + 1];
      if (gain > maxGain) {
        maxGain = gain;
      }
    }

    return initialOnes + maxGain;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxActiveSectionsAfterTrade(s string) int {
	initialOnes := 0
	for _, c := range s {
		if c == '1' {
			initialOnes++
		}
	}

	t := "1" + s + "1"
	segments := []int{}
	currentLen := 1
	for i := 1; i < len(t); i++ {
		if t[i] == t[i-1] {
			currentLen++
		} else {
			segments = append(segments, currentLen)
			currentLen = 1
		}
	}
	segments = append(segments, currentLen)

	k := (len(segments) - 1) / 2
	maxGain := 0
	for i := 1; i < k; i++ {
		gain := segments[2*i-1] + segments[2*i+1]
		if gain > maxGain {
			maxGain = gain
		}
	}

	return initialOnes + maxGain
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def max_active_sections_after_trade(s)
  initial_ones = s.count('1')
  t = '1' + s + '1'
  segments = []
  current_len = 1
  (1...t.length).each do |i|
    if t[i] == t[i - 1]
      current_len += 1
    else
      segments << current_len
      current_len = 1
    end
  end
  segments << current_len

  k = (segments.size - 1) / 2
  max_gain = 0
  (1...k).each do |i|
    gain = segments[2 * i - 1] + segments[2 * i + 1]
    max_gain = gain if gain > max_gain
  end

  initial_ones + max_gain
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable.ArrayBuffer

object Solution {
    def maxActiveSectionsAfterTrade(s: String): Int = {
        var initialOnes = 0
        var i = 0
        while (i < s.length) {
            if (s(i) == '1') initialOnes += 1
            i += 1
        }

        val t = "1" + s + "1"
        val segments = ArrayBuffer[Int]()
        var currentLen = 1
        var j = 1
        while (j < t.length) {
            if (t(j) == t(j - 1)) {
                currentLen += 1
            } else {
                segments += currentLen
                currentLen = 1
            }
            j += 1
        }
        segments += currentLen

        val k = (segments.size - 1) / 2
        var maxGain = 0
        var m = 1
        while (m < k) {
            val gain = segments(2 * m - 1) + segments(2 * m + 1)
            if (gain > maxGain) maxGain = gain
            m += 1
        }

        initialOnes + maxGain
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_active_sections_after_trade(s: String) -> i32 {
        let s_bytes = s.as_bytes();
        let initial_ones = s_bytes.iter().filter(|&&b| b == b'1').count() as i32;

        let mut t = Vec::with_capacity(s.len() + 2);
        t.push(b'1');
        t.extend_from_slice(s_bytes);
        t.push(b'1');

        let mut block_lens = Vec::new();
        if t.is_empty() { return initial_ones; }

        let mut current_len = 1;
        for i in 1..t.len() {
            if t[i] == t[i-1] {
                current_len += 1;
            } else {
                block_lens.push(current_len);
                current_len = 1;
            }
        }
        block_lens.push(current_len);

        let mut max_gain = 0;
        let k = block_lens.len();
        let mut i = 2;
        while i < k - 2 {
            let gain = block_lens[i-1] + block_lens[i+1];
            if gain > max_gain {
                max_gain = gain;
            }
            i += 2;
        }

        initial_ones + max_gain
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (max-active-sections-after-trade s)
  (-> string? exact-integer?)
  (let* ([s-list (string->list s)]
         [initial-ones (length (filter (lambda (c) (char=? c #\1)) s-list))]
         [t (append '(#\1) s-list '(#\1))]
         [block-lens-list (if (null? t) '()
                              (let loop ([lst (cdr t)] [curr (car t)] [len 1] [acc '()])
                                (cond [(null? lst) (reverse (cons len acc))]
                                      [(char=? (car lst) curr) (loop (cdr lst) curr (+ len 1) acc)]
                                      [else (loop (cdr lst) (car lst) 1 (cons len acc))])))]
         [block-lens (list->vector block-lens-list)]
         [k (vector-length block-lens)])
    (let loop ([i 2] [max-gain 0])
      (if (>= i (- k 2))
          (+ initial-ones max-gain)
          (let ([gain (+ (vector-ref block-lens (- i 1)) (vector-ref block-lens (+ i 1)))])
            (loop (+ i 2) (max max-gain gain)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_active_sections_after_trade(S :: unicode:unicode_binary()) -> integer().
max_active_sections_after_trade(S) ->
  SList = binary_to_list(S),
  InitialOnes = length([C || C <- SList, C =:= $1]),
  T = [$1 | SList] ++ [$1],
  BlockLens = get_block_lens(T, undefined, 0, []),
  BlockVec = list_to_tuple(BlockLens),
  K = tuple_size(BlockVec),
  MaxGain = find_max_gain(3, K, BlockVec, 0),
  InitialOnes + MaxGain.

get_block_lens([], _Curr, Len, Acc) ->
  lists:reverse([Len | Acc]);
get_block_lens([H | T], undefined, 0, Acc) ->
  get_block_lens(T, H, 1, Acc);
get_block_lens([H | T], H, Len, Acc) ->
  get_block_lens(T, H, Len + 1, Acc);
get_block_lens([H | T], _Curr, Len, Acc) ->
  get_block_lens(T, H, 1, [Len | Acc]).

find_max_gain(I, K, Vec, MaxG) when I > K - 2 -> MaxG;
find_max_gain(I, K, Vec, MaxG) ->
  Gain = element(I - 1, Vec) + element(I + 1, Vec),
  find_max_gain(I + 2, K, Vec, max(MaxG, Gain)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_active_sections_after_trade(s :: String.t) :: integer
  def max_active_sections_after_trade(s) do
    s_chars = String.to_charlist(s)
    initial_ones = Enum.count(s_chars, &(&1 == ?1))
    t = [?1 | s_chars] ++ [?1]

    block_lens = 
      t 
      |> Enum.chunk_by(& &1)
      |> Enum.map(&length/1)

    k = length(block_lens)
    if k < 5 do
      initial_ones
    else
      block_vec = List.to_tuple(block_lens)
      max_gain = 
        2..(k-3)
        |> Enum.filter(&(rem(&1, 2) == 0))
        |> Enum.map(fn i -> elem(block_vec, i-1) + elem(block_vec, i+1) end)
        |> Enum.max(fn -> 0 end)
      initial_ones + max_gain
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the string s. We iterate through the string a constant number of times: once to count the initial '1's, once to identify the lengths of '0' blocks, and once to find the maximum sum of adjacent '0' block lengths.
- **Space Complexity:** O(n) to store the lengths of the contiguous '0' blocks. In the worst case (e.g., "010101..."), there are approximately n/2 such blocks, requiring O(n) space. This can be optimized to O(1) by keeping track of only the current and previous '0' block lengths during a single pass.
