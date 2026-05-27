---
layout: post
title: "Count the Number of Special Characters II"
date: 2026-05-27 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Hash Table", "String"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/count-the-number-of-special-characters-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int numberOfSpecialChars(string word) {\n\
        \        int lastLower[26];\n        int firstUpper[26];\n        for (int i\
        \ = 0; i < 26; ++i) {\n            lastLower[i] = -1;\n            firstUpper[i]\
        \ = -1;\n        }\n        for (int i = 0; i < (int)word.size(); ++i) {\n \
        \           if (word[i] >= 'a' && word[i] <= 'z') {\n                lastLower[word[i]\
        \ - 'a'] = i;\n            } else if (word[i] >= 'A' && word[i] <= 'Z') {\n\
        \                int idx = word[i] - 'A';\n                if (firstUpper[idx]\
        \ == -1) {\n                    firstUpper[idx] = i;\n                }\n  \
        \          }\n        }\n        int count = 0;\n        for (int i = 0; i <\
        \ 26; ++i) {\n            if (lastLower[i] != -1 && firstUpper[i] != -1 && lastLower[i]\
        \ < firstUpper[i]) {\n                count++;\n            }\n        }\n \
        \       return count;\n    }\n};"
      java: "class Solution {\n    public int numberOfSpecialChars(String word) {\n\
        \        int[] lastLower = new int[26];\n        int[] firstUpper = new int[26];\n\
        \        java.util.Arrays.fill(lastLower, -1);\n        java.util.Arrays.fill(firstUpper,\
        \ -1);\n\n        for (int i = 0; i < word.length(); i++) {\n            char\
        \ c = word.charAt(i);\n            if (c >= 'a' && c <= 'z') {\n           \
        \     lastLower[c - 'a'] = i;\n            } else if (c >= 'A' && c <= 'Z')\
        \ {\n                int idx = c - 'A';\n                if (firstUpper[idx]\
        \ == -1) {\n                    firstUpper[idx] = i;\n                }\n  \
        \          }\n        }\n\n        int count = 0;\n        for (int i = 0; i\
        \ < 26; i++) {\n            if (lastLower[i] != -1 && firstUpper[i] != -1 &&\
        \ lastLower[i] < firstUpper[i]) {\n                count++;\n            }\n\
        \        }\n        return count;\n    }\n}"
      python: "class Solution(object):\n    def numberOfSpecialChars(self, word):\n\
        \        \"\"\"\n        :type word: str\n        :rtype: int\n        \"\"\"\
        \n        last_lower = [-1] * 26\n        first_upper = [-1] * 26\n\n      \
        \  for i, char in enumerate(word):\n            if 'a' <= char <= 'z':\n   \
        \             last_lower[ord(char) - ord('a')] = i\n            elif 'A' <=\
        \ char <= 'Z':\n                idx = ord(char) - ord('A')\n               \
        \ if first_upper[idx] == -1:\n                    first_upper[idx] = i\n\n \
        \       ans = 0\n        for i in range(26):\n            if last_lower[i] !=\
        \ -1 and first_upper[i] != -1 and last_lower[i] < first_upper[i]:\n        \
        \        ans += 1\n        return ans"
      python3: "class Solution:\n    def numberOfSpecialChars(self, word: str) -> int:\n\
        \        last_lower = [-1] * 26\n        first_upper = [-1] * 26\n\n       \
        \ for i, char in enumerate(word):\n            if 'a' <= char <= 'z':\n    \
        \            last_lower[ord(char) - ord('a')] = i\n            elif 'A' <= char\
        \ <= 'Z':\n                idx = ord(char) - ord('A')\n                if first_upper[idx]\
        \ == -1:\n                    first_upper[idx] = i\n\n        count = 0\n  \
        \      for i in range(26):\n            if last_lower[i] != -1 and first_upper[i]\
        \ != -1 and last_lower[i] < first_upper[i]:\n                count += 1\n  \
        \      return count"
      c: "int numberOfSpecialChars(char* word) {\n    int lastLower[26];\n    int firstUpper[26];\n\
        \    for (int i = 0; i < 26; i++) {\n        lastLower[i] = -1;\n        firstUpper[i]\
        \ = -1;\n    }\n\n    for (int i = 0; word[i] != '\\0'; i++) {\n        if (word[i]\
        \ >= 'a' && word[i] <= 'z') {\n            lastLower[word[i] - 'a'] = i;\n \
        \       } else if (word[i] >= 'A' && word[i] <= 'Z') {\n            int idx\
        \ = word[i] - 'A';\n            if (firstUpper[idx] == -1) {\n             \
        \   firstUpper[idx] = i;\n            }\n        }\n    }\n\n    int count =\
        \ 0;\n    for (int i = 0; i < 26; i++) {\n        if (lastLower[i] != -1 &&\
        \ firstUpper[i] != -1 && lastLower[i] < firstUpper[i]) {\n            count++;\n\
        \        }\n    }\n    return count;\n}"
      csharp: "public class Solution {\n    public int NumberOfSpecialChars(string word)\
        \ {\n        int[] lastLower = new int[26];\n        int[] firstUpper = new\
        \ int[26];\n        for (int i = 0; i < 26; i++) {\n            lastLower[i]\
        \ = -1;\n            firstUpper[i] = -1;\n        }\n\n        for (int i =\
        \ 0; i < word.Length; i++) {\n            char c = word[i];\n            if\
        \ (c >= 'a' && c <= 'z') {\n                lastLower[c - 'a'] = i;\n      \
        \      } else if (c >= 'A' && c <= 'Z') {\n                int idx = c - 'A';\n\
        \                if (firstUpper[idx] == -1) {\n                    firstUpper[idx]\
        \ = i;\n                }\n            }\n        }\n\n        int count = 0;\n\
        \        for (int i = 0; i < 26; i++) {\n            if (lastLower[i] != -1\
        \ && firstUpper[i] != -1 && lastLower[i] < firstUpper[i]) {\n              \
        \  count++;\n            }\n        }\n        return count;\n    }\n}"
      javascript: "/**\n * @param {string} word\n * @return {number}\n */\nvar numberOfSpecialChars\
        \ = function(word) {\n    const lastLower = new Array(26).fill(-1);\n    const\
        \ firstUpper = new Array(26).fill(-1);\n\n    for (let i = 0; i < word.length;\
        \ i++) {\n        const charCode = word.charCodeAt(i);\n        if (charCode\
        \ >= 97 && charCode <= 122) {\n            lastLower[charCode - 97] = i;\n \
        \       } else if (charCode >= 65 && charCode <= 90) {\n            const idx\
        \ = charCode - 65;\n            if (firstUpper[idx] === -1) {\n            \
        \    firstUpper[idx] = i;\n            }\n        }\n    }\n\n    let count\
        \ = 0;\n    for (let i = 0; i < 26; i++) {\n        if (lastLower[i] !== -1\
        \ && firstUpper[i] !== -1 && lastLower[i] < firstUpper[i]) {\n            count++;\n\
        \        }\n    }\n    return count;\n};"
      typescript: "function numberOfSpecialChars(word: string): number {\n    const\
        \ lastLower: number[] = new Array(26).fill(-1);\n    const firstUpper: number[]\
        \ = new Array(26).fill(-1);\n\n    for (let i = 0; i < word.length; i++) {\n\
        \        const charCode = word.charCodeAt(i);\n        if (charCode >= 97 &&\
        \ charCode <= 122) {\n            lastLower[charCode - 97] = i;\n        } else\
        \ if (charCode >= 65 && charCode <= 90) {\n            const idx = charCode\
        \ - 65;\n            if (firstUpper[idx] === -1) {\n                firstUpper[idx]\
        \ = i;\n            }\n        }\n    }\n\n    let count = 0;\n    for (let\
        \ i = 0; i < 26; i++) {\n        if (lastLower[i] !== -1 && firstUpper[i] !==\
        \ -1 && lastLower[i] < firstUpper[i]) {\n            count++;\n        }\n \
        \   }\n    return count;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $word\n     * @return\
        \ Integer\n     */\n    function numberOfSpecialChars($word) {\n        $lastLower\
        \ = array_fill(0, 26, -1);\n        $firstUpper = array_fill(0, 26, -1);\n \
        \       $n = strlen($word);\n\n        for ($i = 0; $i < $n; $i++) {\n     \
        \       $o = ord($word[$i]);\n            if ($o >= 97 && $o <= 122) {\n   \
        \             $lastLower[$o - 97] = $i;\n            } else if ($o >= 65 &&\
        \ $o <= 90) {\n                $idx = $o - 65;\n                if ($firstUpper[$idx]\
        \ === -1) {\n                    $firstUpper[$idx] = $i;\n                }\n\
        \            }\n        }\n\n        $count = 0;\n        for ($i = 0; $i <\
        \ 26; $i++) {\n            if ($lastLower[$i] !== -1 && $firstUpper[$i] !==\
        \ -1 && $lastLower[$i] < $firstUpper[$i]) {\n                $count++;\n   \
        \         }\n        }\n        return $count;\n    }\n}"
      swift: "class Solution {\n    func numberOfSpecialChars(_ word: String) -> Int\
        \ {\n        var lastLower = [Int](repeating: -1, count: 26)\n        var firstUpper\
        \ = [Int](repeating: -1, count: 26)\n        let lowerA = UInt8(97)\n      \
        \  let upperA = UInt8(65)\n\n        var i = 0\n        for char in word {\n\
        \            if let ascii = char.asciiValue {\n                if ascii >= lowerA\
        \ && ascii < lowerA + 26 {\n                    lastLower[Int(ascii - lowerA)]\
        \ = i\n                } else if ascii >= upperA && ascii < upperA + 26 {\n\
        \                    let idx = Int(ascii - upperA)\n                    if firstUpper[idx]\
        \ == -1 {\n                        firstUpper[idx] = i\n                   \
        \ }\n                }\n            }\n            i += 1\n        }\n\n   \
        \     var count = 0\n        for i in 0..<26 {\n            if lastLower[i]\
        \ != -1 && firstUpper[i] != -1 && lastLower[i] < firstUpper[i] {\n         \
        \       count += 1\n            }\n        }\n        return count\n    }\n}"
      kotlin: "class Solution {\n    fun numberOfSpecialChars(word: String): Int {\n\
        \        val lastLower = IntArray(26) { -1 }\n        val firstUpper = IntArray(26)\
        \ { -1 }\n        for (i in word.indices) {\n            val c = word[i]\n \
        \           if (c in 'a'..'z') {\n                lastLower[c - 'a'] = i\n \
        \           }\n            if (c in 'A'..'Z') {\n                val idx = c\
        \ - 'A'\n                if (firstUpper[idx] == -1) {\n                    firstUpper[idx]\
        \ = i\n                }\n            }\n        }\n        var count = 0\n\
        \        for (i in 0 until 26) {\n            if (lastLower[i] != -1 && firstUpper[i]\
        \ != -1 && lastLower[i] < firstUpper[i]) {\n                count++\n      \
        \      }\n        }\n        return count\n    }\n}"
      dart: "class Solution {\n  int numberOfSpecialChars(String word) {\n    List<int>\
        \ lastLower = List.filled(26, -1);\n    List<int> firstUpper = List.filled(26,\
        \ -1);\n    int aCode = 'a'.codeUnitAt(0);\n    int zCode = 'z'.codeUnitAt(0);\n\
        \    int ACode = 'A'.codeUnitAt(0);\n    int ZCode = 'Z'.codeUnitAt(0);\n\n\
        \    for (int i = 0; i < word.length; i++) {\n      int code = word.codeUnitAt(i);\n\
        \      if (code >= aCode && code <= zCode) {\n        lastLower[code - aCode]\
        \ = i;\n      } else if (code >= ACode && code <= ZCode) {\n        int idx\
        \ = code - ACode;\n        if (firstUpper[idx] == -1) {\n          firstUpper[idx]\
        \ = i;\n        }\n      }\n    }\n\n    int count = 0;\n    for (int i = 0;\
        \ i < 26; i++) {\n      if (lastLower[i] != -1 && firstUpper[i] != -1 && lastLower[i]\
        \ < firstUpper[i]) {\n        count++;\n      }\n    }\n    return count;\n\
        \  }\n}"
      go: "func numberOfSpecialChars(word string) int {\n    lastLower := make([]int,\
        \ 26)\n    firstUpper := make([]int, 26)\n    for i := 0; i < 26; i++ {\n  \
        \      lastLower[i] = -1\n        firstUpper[i] = -1\n    }\n\n    for i, char\
        \ := range word {\n        if char >= 'a' && char <= 'z' {\n            lastLower[int(char-'a')]\
        \ = i\n        } else if char >= 'A' && char <= 'Z' {\n            idx := int(char\
        \ - 'A')\n            if firstUpper[idx] == -1 {\n                firstUpper[idx]\
        \ = i\n            }\n        }\n    }\n\n    count := 0\n    for i := 0; i\
        \ < 26; i++ {\n        if lastLower[i] != -1 && firstUpper[i] != -1 && lastLower[i]\
        \ < firstUpper[i] {\n            count++\n        }\n    }\n    return count\n\
        }"
      ruby: "# @param {String} word\n# @return {Integer}\ndef number_of_special_chars(word)\n\
        \  last_lower = Array.new(26, -1)\n  first_upper = Array.new(26, -1)\n\n  word.each_char.with_index\
        \ do |char, i|\n    if char >= 'a' && char <= 'z'\n      last_lower[char.ord\
        \ - 'a'.ord] = i\n    elsif char >= 'A' && char <= 'Z'\n      idx = char.ord\
        \ - 'A'.ord\n      if first_upper[idx] == -1\n        first_upper[idx] = i\n\
        \      \tend\n    end\n  end\n\n  count = 0\n  26.times do |i|\n    if last_lower[i]\
        \ != -1 && first_upper[i] != -1 && last_lower[i] < first_upper[i]\n      count\
        \ += 1\n    end\n  end\n  count\nend"
      scala: "object Solution {\n    def numberOfSpecialChars(word: String): Int = {\n\
        \        val lastLower = Array.fill(26)(-1)\n        val firstUpper = Array.fill(26)(-1)\n\
        \n        for (i <- 0 until word.length) {\n            val c = word(i)\n  \
        \          if (c >= 'a' && c <= 'z') {\n                lastLower(c - 'a') =\
        \ i\n            } else if (c >= 'A' && c <= 'Z') {\n                val idx\
        \ = c - 'A'\n                if (firstUpper(idx) == -1) {\n                \
        \    firstUpper(idx) = i\n                }\n            }\n        }\n\n  \
        \      var count = 0\n        for (i <- 0 until 26) {\n            if (lastLower(i)\
        \ != -1 && firstUpper(i) != -1 && lastLower(i) < firstUpper(i)) {\n        \
        \        count += 1\n            }\n        }\n        count\n    }\n}"
      rust: "impl Solution {\n    pub fn number_of_special_chars(word: String) -> i32\
        \ {\n        let mut last_lower = [-1i32; 26];\n        let mut first_upper\
        \ = [-1i32; 26];\n        let bytes = word.as_bytes();\n        for i in 0..bytes.len()\
        \ {\n            let b = bytes[i];\n            if b >= b'a' && b <= b'z' {\n\
        \                last_lower[(b - b'a') as usize] = i as i32;\n            }\
        \ else if b >= b'A' && b <= b'Z' {\n                let idx = (b - b'A') as\
        \ usize;\n                if first_upper[idx] == -1 {\n                    first_upper[idx]\
        \ = i as i32;\n                }\n            }\n        }\n        let mut\
        \ count = 0;\n        for i in 0..26 {\n            if last_lower[i] != -1 &&\
        \ first_upper[i] != -1 && last_lower[i] < first_upper[i] {\n               \
        \ count += 1;\n            }\n        }\n        count\n    }\n}"
      racket: "(define/contract (number-of-special-chars word)\n  (-> string? exact-integer?)\n\
        \  (let ([last-lower (make-vector 26 -1)]\n        [first-upper (make-vector\
        \ 26 -1)])\n    (for ([c (in-string word)]\n          [i (in-naturals)])\n \
        \     (cond\n        [(and (char>=? c #\\a) (char<=? c #\\z))\n         (vector-set!\
        \ last-lower (- (char->integer c) (char->integer #\\a)) i)]\n        [(and (char>=?\
        \ c #\\A) (char<=? c #\\Z))\n         (let ([idx (- (char->integer c) (char->integer\
        \ #\\A))])\n           (when (= (vector-ref first-upper idx) -1)\n         \
        \    (vector-set! first-upper idx i)))]))\n    (for/fold ([count 0])\n     \
        \         ([i (in-range 26)])\n      (let ([ll (vector-ref last-lower i)]\n\
        \            [fu (vector-ref first-upper i)])\n        (if (and (not (= ll -1))\
        \ (not (= fu -1)) (< ll fu))\n            (+ count 1)\n            count)))))"
      erlang: "-spec number_of_special_chars(Word :: unicode:unicode_binary()) -> integer().\n\
        number_of_special_chars(Word) ->\n  List = binary_to_list(Word),\n  {LastLower,\
        \ FirstUpper} = process_chars(List, 0, #{}, #{}),\n  count_special(0, 0, LastLower,\
        \ FirstUpper).\n\nprocess_chars([], _, LastLower, FirstUpper) ->\n  {LastLower,\
        \ FirstUpper};\nprocess_chars([H | T], I, LastLower, FirstUpper) ->\n  if\n\
        \    H >= $a, H =< $z ->\n      process_chars(T, I + 1, maps:put(H - $a, I,\
        \ LastLower), FirstUpper);\n    H >= $A, H =< $Z ->\n      Idx = H - $A,\n \
        \     case maps:find(Idx, FirstUpper) of\n        error -> process_chars(T,\
        \ I + 1, LastLower, maps:put(Idx, I, FirstUpper));\n        _ -> process_chars(T,\
        \ I + 1, LastLower, FirstUpper)\n      end;\n    true ->\n      process_chars(T,\
        \ I + 1, LastLower, FirstUpper)\n  end.\n\ncount_special(26, Count, _, _) ->\
        \ Count;\ncount_special(I, Count, LastLower, FirstUpper) ->\n  LL = maps:get(I,\
        \ LastLower, -1),\n  FU = maps:get(I, FirstUpper, -1),\n  if\n    LL /= -1,\
        \ FU /= -1, LL < FU ->\n      count_special(I + 1, Count + 1, LastLower, FirstUpper);\n\
        \    true ->\n      count_special(I + 1, Count, LastLower, FirstUpper)\n  end."
      elixir: "defmodule Solution do\n  @spec number_of_special_chars(word :: String.t)\
        \ :: integer\n  def number_of_special_chars(word) do\n    {last_lower, first_upper}\
        \ = String.to_charlist(word)\n    |> Enum.with_index()\n    |> Enum.reduce({%{},\
        \ %{}}, fn {char, index}, {ll, fu} ->\n      cond do\n        char >= ?a and\
        \ char <= ?z ->\n          {Map.put(ll, char - ?a, index), fu}\n        char\
        \ >= ?A and char <= ?Z ->\n          idx = char - ?A\n          if Map.has_key?(fu,\
        \ idx) do\n            {ll, fu}\n          else\n            {ll, Map.put(fu,\
        \ idx, index)}\n          end\n        true ->\n          {ll, fu}\n      end\n\
        \    end)\n\n    0..25\n    |> Enum.count(fn i ->\n      ll_idx = Map.get(last_lower,\
        \ i, -1)\n      fu_idx = Map.get(first_upper, i, -1)\n      ll_idx != -1 and\
        \ fu_idx != -1 and ll_idx < fu_idx\n    end)\n  end\nend"
    approach: 'To determine if a letter is special, we must verify that all its lowercase
      instances occur before any of its uppercase instances. This is equivalent to checking
      if the index of the very last occurrence of the lowercase letter is strictly smaller
      than the index of the very first occurrence of the corresponding uppercase letter.
      We maintain two arrays of size 26 to store these specific indices while iterating
      through the string: one array records the last-seen index of each lowercase character,
      and the other records the first-seen index of each uppercase character.


      After a single pass through the string, we examine each letter of the English
      alphabet. A character is counted as special if and only if it appeared as both
      lowercase and uppercase, and its last lowercase index is strictly less than its
      first uppercase index. This condition guarantees that no lowercase occurrence
      exists at or after the point where the uppercase occurrences begin, fulfilling
      the problem''s requirement efficiently in linear time.'
    time_complexity: O(n), where n is the length of the string. The algorithm iterates
      through the input string once to record indices and then performs a constant-time
      iteration of 26 steps over the alphabet.
    space_complexity: O(1), as the extra space used consists of two fixed-size arrays
      of 26 integers each, which does not scale with the input size.
    elapsed_time: 183.48648238182068
    model: gemini-3-flash-preview
    generated_at: '2026-05-27 02:46:12 '
---

## Problem #3121: Count the Number of Special Characters II

**Difficulty:** Medium

**Topics:** Hash Table, String

## Problem Description

<p>You are given a string <code>word</code>. A letter&nbsp;<code>c</code> is called <strong>special</strong> if it appears <strong>both</strong> in lowercase and uppercase in <code>word</code>, and <strong>every</strong> lowercase occurrence of <code>c</code> appears before the <strong>first</strong> uppercase occurrence of <code>c</code>.</p>

<p>Return the number of<em> </em><strong>special</strong> letters<em> </em>in<em> </em><code>word</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = &quot;aaAbcBC&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>The special characters are <code>&#39;a&#39;</code>, <code>&#39;b&#39;</code>, and <code>&#39;c&#39;</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = &quot;abc&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>There are no special characters in <code>word</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = &quot;AbBCab&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>There are no special characters in <code>word</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>word</code> consists of only lowercase and uppercase English letters.</li>
</ul>


## Hints

1. For each character `c`, store the first occurrence of its uppercase and the last occurrence of its lowercase.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To determine if a letter is special, we must verify that all its lowercase instances occur before any of its uppercase instances. This is equivalent to checking if the index of the very last occurrence of the lowercase letter is strictly smaller than the index of the very first occurrence of the corresponding uppercase letter. We maintain two arrays of size 26 to store these specific indices while iterating through the string: one array records the last-seen index of each lowercase character, and the other records the first-seen index of each uppercase character.

After a single pass through the string, we examine each letter of the English alphabet. A character is counted as special if and only if it appeared as both lowercase and uppercase, and its last lowercase index is strictly less than its first uppercase index. This condition guarantees that no lowercase occurrence exists at or after the point where the uppercase occurrences begin, fulfilling the problem's requirement efficiently in linear time.

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
    int numberOfSpecialChars(string word) {
        int lastLower[26];
        int firstUpper[26];
        for (int i = 0; i < 26; ++i) {
            lastLower[i] = -1;
            firstUpper[i] = -1;
        }
        for (int i = 0; i < (int)word.size(); ++i) {
            if (word[i] >= 'a' && word[i] <= 'z') {
                lastLower[word[i] - 'a'] = i;
            } else if (word[i] >= 'A' && word[i] <= 'Z') {
                int idx = word[i] - 'A';
                if (firstUpper[idx] == -1) {
                    firstUpper[idx] = i;
                }
            }
        }
        int count = 0;
        for (int i = 0; i < 26; ++i) {
            if (lastLower[i] != -1 && firstUpper[i] != -1 && lastLower[i] < firstUpper[i]) {
                count++;
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
    public int numberOfSpecialChars(String word) {
        int[] lastLower = new int[26];
        int[] firstUpper = new int[26];
        java.util.Arrays.fill(lastLower, -1);
        java.util.Arrays.fill(firstUpper, -1);

        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (c >= 'a' && c <= 'z') {
                lastLower[c - 'a'] = i;
            } else if (c >= 'A' && c <= 'Z') {
                int idx = c - 'A';
                if (firstUpper[idx] == -1) {
                    firstUpper[idx] = i;
                }
            }
        }

        int count = 0;
        for (int i = 0; i < 26; i++) {
            if (lastLower[i] != -1 && firstUpper[i] != -1 && lastLower[i] < firstUpper[i]) {
                count++;
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
class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        last_lower = [-1] * 26
        first_upper = [-1] * 26

        for i, char in enumerate(word):
            if 'a' <= char <= 'z':
                last_lower[ord(char) - ord('a')] = i
            elif 'A' <= char <= 'Z':
                idx = ord(char) - ord('A')
                if first_upper[idx] == -1:
                    first_upper[idx] = i

        ans = 0
        for i in range(26):
            if last_lower[i] != -1 and first_upper[i] != -1 and last_lower[i] < first_upper[i]:
                ans += 1
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = [-1] * 26
        first_upper = [-1] * 26

        for i, char in enumerate(word):
            if 'a' <= char <= 'z':
                last_lower[ord(char) - ord('a')] = i
            elif 'A' <= char <= 'Z':
                idx = ord(char) - ord('A')
                if first_upper[idx] == -1:
                    first_upper[idx] = i

        count = 0
        for i in range(26):
            if last_lower[i] != -1 and first_upper[i] != -1 and last_lower[i] < first_upper[i]:
                count += 1
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int numberOfSpecialChars(char* word) {
    int lastLower[26];
    int firstUpper[26];
    for (int i = 0; i < 26; i++) {
        lastLower[i] = -1;
        firstUpper[i] = -1;
    }

    for (int i = 0; word[i] != '\0'; i++) {
        if (word[i] >= 'a' && word[i] <= 'z') {
            lastLower[word[i] - 'a'] = i;
        } else if (word[i] >= 'A' && word[i] <= 'Z') {
            int idx = word[i] - 'A';
            if (firstUpper[idx] == -1) {
                firstUpper[idx] = i;
            }
        }
    }

    int count = 0;
    for (int i = 0; i < 26; i++) {
        if (lastLower[i] != -1 && firstUpper[i] != -1 && lastLower[i] < firstUpper[i]) {
            count++;
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
    public int NumberOfSpecialChars(string word) {
        int[] lastLower = new int[26];
        int[] firstUpper = new int[26];
        for (int i = 0; i < 26; i++) {
            lastLower[i] = -1;
            firstUpper[i] = -1;
        }

        for (int i = 0; i < word.Length; i++) {
            char c = word[i];
            if (c >= 'a' && c <= 'z') {
                lastLower[c - 'a'] = i;
            } else if (c >= 'A' && c <= 'Z') {
                int idx = c - 'A';
                if (firstUpper[idx] == -1) {
                    firstUpper[idx] = i;
                }
            }
        }

        int count = 0;
        for (int i = 0; i < 26; i++) {
            if (lastLower[i] != -1 && firstUpper[i] != -1 && lastLower[i] < firstUpper[i]) {
                count++;
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
/**
 * @param {string} word
 * @return {number}
 */
var numberOfSpecialChars = function(word) {
    const lastLower = new Array(26).fill(-1);
    const firstUpper = new Array(26).fill(-1);

    for (let i = 0; i < word.length; i++) {
        const charCode = word.charCodeAt(i);
        if (charCode >= 97 && charCode <= 122) {
            lastLower[charCode - 97] = i;
        } else if (charCode >= 65 && charCode <= 90) {
            const idx = charCode - 65;
            if (firstUpper[idx] === -1) {
                firstUpper[idx] = i;
            }
        }
    }

    let count = 0;
    for (let i = 0; i < 26; i++) {
        if (lastLower[i] !== -1 && firstUpper[i] !== -1 && lastLower[i] < firstUpper[i]) {
            count++;
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
function numberOfSpecialChars(word: string): number {
    const lastLower: number[] = new Array(26).fill(-1);
    const firstUpper: number[] = new Array(26).fill(-1);

    for (let i = 0; i < word.length; i++) {
        const charCode = word.charCodeAt(i);
        if (charCode >= 97 && charCode <= 122) {
            lastLower[charCode - 97] = i;
        } else if (charCode >= 65 && charCode <= 90) {
            const idx = charCode - 65;
            if (firstUpper[idx] === -1) {
                firstUpper[idx] = i;
            }
        }
    }

    let count = 0;
    for (let i = 0; i < 26; i++) {
        if (lastLower[i] !== -1 && firstUpper[i] !== -1 && lastLower[i] < firstUpper[i]) {
            count++;
        }
    }
    return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String $word
     * @return Integer
     */
    function numberOfSpecialChars($word) {
        $lastLower = array_fill(0, 26, -1);
        $firstUpper = array_fill(0, 26, -1);
        $n = strlen($word);

        for ($i = 0; $i < $n; $i++) {
            $o = ord($word[$i]);
            if ($o >= 97 && $o <= 122) {
                $lastLower[$o - 97] = $i;
            } else if ($o >= 65 && $o <= 90) {
                $idx = $o - 65;
                if ($firstUpper[$idx] === -1) {
                    $firstUpper[$idx] = $i;
                }
            }
        }

        $count = 0;
        for ($i = 0; $i < 26; $i++) {
            if ($lastLower[$i] !== -1 && $firstUpper[$i] !== -1 && $lastLower[$i] < $firstUpper[$i]) {
                $count++;
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
    func numberOfSpecialChars(_ word: String) -> Int {
        var lastLower = [Int](repeating: -1, count: 26)
        var firstUpper = [Int](repeating: -1, count: 26)
        let lowerA = UInt8(97)
        let upperA = UInt8(65)

        var i = 0
        for char in word {
            if let ascii = char.asciiValue {
                if ascii >= lowerA && ascii < lowerA + 26 {
                    lastLower[Int(ascii - lowerA)] = i
                } else if ascii >= upperA && ascii < upperA + 26 {
                    let idx = Int(ascii - upperA)
                    if firstUpper[idx] == -1 {
                        firstUpper[idx] = i
                    }
                }
            }
            i += 1
        }

        var count = 0
        for i in 0..<26 {
            if lastLower[i] != -1 && firstUpper[i] != -1 && lastLower[i] < firstUpper[i] {
                count += 1
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
    fun numberOfSpecialChars(word: String): Int {
        val lastLower = IntArray(26) { -1 }
        val firstUpper = IntArray(26) { -1 }
        for (i in word.indices) {
            val c = word[i]
            if (c in 'a'..'z') {
                lastLower[c - 'a'] = i
            }
            if (c in 'A'..'Z') {
                val idx = c - 'A'
                if (firstUpper[idx] == -1) {
                    firstUpper[idx] = i
                }
            }
        }
        var count = 0
        for (i in 0 until 26) {
            if (lastLower[i] != -1 && firstUpper[i] != -1 && lastLower[i] < firstUpper[i]) {
                count++
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
  int numberOfSpecialChars(String word) {
    List<int> lastLower = List.filled(26, -1);
    List<int> firstUpper = List.filled(26, -1);
    int aCode = 'a'.codeUnitAt(0);
    int zCode = 'z'.codeUnitAt(0);
    int ACode = 'A'.codeUnitAt(0);
    int ZCode = 'Z'.codeUnitAt(0);

    for (int i = 0; i < word.length; i++) {
      int code = word.codeUnitAt(i);
      if (code >= aCode && code <= zCode) {
        lastLower[code - aCode] = i;
      } else if (code >= ACode && code <= ZCode) {
        int idx = code - ACode;
        if (firstUpper[idx] == -1) {
          firstUpper[idx] = i;
        }
      }
    }

    int count = 0;
    for (int i = 0; i < 26; i++) {
      if (lastLower[i] != -1 && firstUpper[i] != -1 && lastLower[i] < firstUpper[i]) {
        count++;
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
func numberOfSpecialChars(word string) int {
    lastLower := make([]int, 26)
    firstUpper := make([]int, 26)
    for i := 0; i < 26; i++ {
        lastLower[i] = -1
        firstUpper[i] = -1
    }

    for i, char := range word {
        if char >= 'a' && char <= 'z' {
            lastLower[int(char-'a')] = i
        } else if char >= 'A' && char <= 'Z' {
            idx := int(char - 'A')
            if firstUpper[idx] == -1 {
                firstUpper[idx] = i
            }
        }
    }

    count := 0
    for i := 0; i < 26; i++ {
        if lastLower[i] != -1 && firstUpper[i] != -1 && lastLower[i] < firstUpper[i] {
            count++
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
# @param {String} word
# @return {Integer}
def number_of_special_chars(word)
  last_lower = Array.new(26, -1)
  first_upper = Array.new(26, -1)

  word.each_char.with_index do |char, i|
    if char >= 'a' && char <= 'z'
      last_lower[char.ord - 'a'.ord] = i
    elsif char >= 'A' && char <= 'Z'
      idx = char.ord - 'A'.ord
      if first_upper[idx] == -1
        first_upper[idx] = i
      	end
    end
  end

  count = 0
  26.times do |i|
    if last_lower[i] != -1 && first_upper[i] != -1 && last_lower[i] < first_upper[i]
      count += 1
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
    def numberOfSpecialChars(word: String): Int = {
        val lastLower = Array.fill(26)(-1)
        val firstUpper = Array.fill(26)(-1)

        for (i <- 0 until word.length) {
            val c = word(i)
            if (c >= 'a' && c <= 'z') {
                lastLower(c - 'a') = i
            } else if (c >= 'A' && c <= 'Z') {
                val idx = c - 'A'
                if (firstUpper(idx) == -1) {
                    firstUpper(idx) = i
                }
            }
        }

        var count = 0
        for (i <- 0 until 26) {
            if (lastLower(i) != -1 && firstUpper(i) != -1 && lastLower(i) < firstUpper(i)) {
                count += 1
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
    pub fn number_of_special_chars(word: String) -> i32 {
        let mut last_lower = [-1i32; 26];
        let mut first_upper = [-1i32; 26];
        let bytes = word.as_bytes();
        for i in 0..bytes.len() {
            let b = bytes[i];
            if b >= b'a' && b <= b'z' {
                last_lower[(b - b'a') as usize] = i as i32;
            } else if b >= b'A' && b <= b'Z' {
                let idx = (b - b'A') as usize;
                if first_upper[idx] == -1 {
                    first_upper[idx] = i as i32;
                }
            }
        }
        let mut count = 0;
        for i in 0..26 {
            if last_lower[i] != -1 && first_upper[i] != -1 && last_lower[i] < first_upper[i] {
                count += 1;
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
(define/contract (number-of-special-chars word)
  (-> string? exact-integer?)
  (let ([last-lower (make-vector 26 -1)]
        [first-upper (make-vector 26 -1)])
    (for ([c (in-string word)]
          [i (in-naturals)])
      (cond
        [(and (char>=? c #\a) (char<=? c #\z))
         (vector-set! last-lower (- (char->integer c) (char->integer #\a)) i)]
        [(and (char>=? c #\A) (char<=? c #\Z))
         (let ([idx (- (char->integer c) (char->integer #\A))])
           (when (= (vector-ref first-upper idx) -1)
             (vector-set! first-upper idx i)))]))
    (for/fold ([count 0])
              ([i (in-range 26)])
      (let ([ll (vector-ref last-lower i)]
            [fu (vector-ref first-upper i)])
        (if (and (not (= ll -1)) (not (= fu -1)) (< ll fu))
            (+ count 1)
            count)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec number_of_special_chars(Word :: unicode:unicode_binary()) -> integer().
number_of_special_chars(Word) ->
  List = binary_to_list(Word),
  {LastLower, FirstUpper} = process_chars(List, 0, #{}, #{}),
  count_special(0, 0, LastLower, FirstUpper).

process_chars([], _, LastLower, FirstUpper) ->
  {LastLower, FirstUpper};
process_chars([H | T], I, LastLower, FirstUpper) ->
  if
    H >= $a, H =< $z ->
      process_chars(T, I + 1, maps:put(H - $a, I, LastLower), FirstUpper);
    H >= $A, H =< $Z ->
      Idx = H - $A,
      case maps:find(Idx, FirstUpper) of
        error -> process_chars(T, I + 1, LastLower, maps:put(Idx, I, FirstUpper));
        _ -> process_chars(T, I + 1, LastLower, FirstUpper)
      end;
    true ->
      process_chars(T, I + 1, LastLower, FirstUpper)
  end.

count_special(26, Count, _, _) -> Count;
count_special(I, Count, LastLower, FirstUpper) ->
  LL = maps:get(I, LastLower, -1),
  FU = maps:get(I, FirstUpper, -1),
  if
    LL /= -1, FU /= -1, LL < FU ->
      count_special(I + 1, Count + 1, LastLower, FirstUpper);
    true ->
      count_special(I + 1, Count, LastLower, FirstUpper)
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec number_of_special_chars(word :: String.t) :: integer
  def number_of_special_chars(word) do
    {last_lower, first_upper} = String.to_charlist(word)
    |> Enum.with_index()
    |> Enum.reduce({%{}, %{}}, fn {char, index}, {ll, fu} ->
      cond do
        char >= ?a and char <= ?z ->
          {Map.put(ll, char - ?a, index), fu}
        char >= ?A and char <= ?Z ->
          idx = char - ?A
          if Map.has_key?(fu, idx) do
            {ll, fu}
          else
            {ll, Map.put(fu, idx, index)}
          end
        true ->
          {ll, fu}
      end
    end)

    0..25
    |> Enum.count(fn i ->
      ll_idx = Map.get(last_lower, i, -1)
      fu_idx = Map.get(first_upper, i, -1)
      ll_idx != -1 and fu_idx != -1 and ll_idx < fu_idx
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n), where n is the length of the string. The algorithm iterates through the input string once to record indices and then performs a constant-time iteration of 26 steps over the alphabet.
- **Space Complexity:** O(1), as the extra space used consists of two fixed-size arrays of 26 integers each, which does not scale with the input size.
