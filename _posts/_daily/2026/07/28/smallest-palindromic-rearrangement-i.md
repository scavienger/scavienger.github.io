---
layout: post
title: "Smallest Palindromic Rearrangement I"
date: 2026-07-28 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Sorting", "Counting Sort"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/smallest-palindromic-rearrangement-i/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    string smallestPalindrome(string s) {\n \
        \       int counts[26] = {0};\n        for (char c : s) {\n            counts[c\
        \ - 'a']++;\n        }\n\n        string firstHalf = \"\";\n        char middleChar\
        \ = 0;\n\n        for (int i = 0; i < 26; ++i) {\n            if (counts[i]\
        \ % 2 != 0) {\n                middleChar = (char)('a' + i);\n            }\n\
        \            for (int j = 0; j < counts[i] / 2; ++j) {\n                firstHalf\
        \ += (char)('a' + i);\n            }\n        }\n\n        string secondHalf\
        \ = firstHalf;\n        reverse(secondHalf.begin(), secondHalf.end());\n\n \
        \       if (middleChar != 0) {\n            return firstHalf + middleChar +\
        \ secondHalf;\n        }\n        return firstHalf + secondHalf;\n    }\n};"
      java: "class Solution {\n    public String smallestPalindrome(String s) {\n  \
        \      int[] counts = new int[26];\n        for (int i = 0; i < s.length();\
        \ i++) {\n            counts[s.charAt(i) - 'a']++;\n        }\n\n        StringBuilder\
        \ firstHalf = new StringBuilder();\n        Character middleChar = null;\n\n\
        \        for (int i = 0; i < 26; i++) {\n            if (counts[i] % 2 != 0)\
        \ {\n                middleChar = (char) ('a' + i);\n            }\n       \
        \     int half = counts[i] / 2;\n            for (int j = 0; j < half; j++)\
        \ {\n                firstHalf.append((char) ('a' + i));\n            }\n  \
        \      }\n\n        String prefix = firstHalf.toString();\n        String suffix\
        \ = firstHalf.reverse().toString();\n\n        if (middleChar != null) {\n \
        \           return prefix + middleChar + suffix;\n        } else {\n       \
        \     return prefix + suffix;\n        }\n    }\n}"
      python: "class Solution(object):\n    def smallestPalindrome(self, s):\n     \
        \   \"\"\"\n        :type s: str\n        :rtype: str\n        \"\"\"\n    \
        \    from collections import Counter\n        counts = Counter(s)\n\n      \
        \  first_half_list = []\n        middle_char = \"\"\n\n        for char_code\
        \ in range(ord('a'), ord('z') + 1):\n            char = chr(char_code)\n   \
        \         if char in counts:\n                if counts[char] % 2 != 0:\n  \
        \                  middle_char = char\n                first_half_list.append(char\
        \ * (counts[char] // 2))\n\n        first_half = \"\".join(first_half_list)\n\
        \        return first_half + middle_char + first_half[::-1]"
      python3: "class Solution:\n    def smallestPalindrome(self, s: str) -> str:\n\
        \        from collections import Counter\n        counts = Counter(s)\n\n  \
        \      first_half_chars = []\n        middle_char = \"\"\n\n        for i in\
        \ range(26):\n            char = chr(ord('a') + i)\n            if char in counts:\n\
        \                count = counts[char]\n                if count % 2 != 0:\n\
        \                    middle_char = char\n                first_half_chars.append(char\
        \ * (count // 2))\n\n        first_half = \"\".join(first_half_chars)\n    \
        \    return first_half + middle_char + first_half[::-1]"
      c: "#include <string.h>\n#include <stdlib.h>\n\nchar* smallestPalindrome(char*\
        \ s) {\n    int n = strlen(s);\n    int counts[26] = {0};\n    for (int i =\
        \ 0; i < n; i++) {\n        counts[s[i] - 'a']++;\n    }\n\n    char* result\
        \ = (char*)malloc((n + 1) * sizeof(char));\n    int left = 0;\n    int mid_idx\
        \ = -1;\n\n    for (int i = 0; i < 26; i++) {\n        if (counts[i] % 2 !=\
        \ 0) {\n            mid_idx = i;\n        }\n        int half = counts[i] /\
        \ 2;\n        for (int j = 0; j < half; j++) {\n            result[left++] =\
        \ (char)('a' + i);\n        }\n    }\n\n    int prefix_len = left;\n    if (mid_idx\
        \ != -1) {\n        result[left++] = (char)('a' + mid_idx);\n    }\n\n    for\
        \ (int i = prefix_len - 1; i >= 0; i--) {\n        result[left++] = result[i];\n\
        \    }\n\n    result[n] = '\\0';\n    return result;\n}"
      csharp: "using System.Text;\n\npublic class Solution {\n    public string SmallestPalindrome(string\
        \ s) {\n        int[] counts = new int[26];\n        foreach (char c in s) {\n\
        \            counts[c - 'a']++;\n        }\n\n        StringBuilder firstHalf\
        \ = new StringBuilder();\n        char middleChar = '\\0';\n        bool hasMiddle\
        \ = false;\n\n        for (int i = 0; i < 26; i++) {\n            int halfCount\
        \ = counts[i] / 2;\n            firstHalf.Append((char)('a' + i), halfCount);\n\
        \            if (counts[i] % 2 != 0) {\n                middleChar = (char)('a'\
        \ + i);\n                hasMiddle = true;\n            }\n        }\n\n   \
        \     string first = firstHalf.ToString();\n        char[] reversedArray = first.ToCharArray();\n\
        \        System.Array.Reverse(reversedArray);\n        string second = new string(reversedArray);\n\
        \n        if (hasMiddle) {\n            return first + middleChar + second;\n\
        \        } else {\n            return first + second;\n        }\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {string}\n */\nvar smallestPalindrome\
        \ = function(s) {\n    let counts = new Array(26).fill(0);\n    for (let char\
        \ of s) {\n        counts[char.charCodeAt(0) - 97]++;\n    }\n\n    let firstHalf\
        \ = \"\";\n    let middleChar = \"\";\n\n    for (let i = 0; i < 26; i++) {\n\
        \        let char = String.fromCharCode(97 + i);\n        let halfCount = Math.floor(counts[i]\
        \ / 2);\n        firstHalf += char.repeat(halfCount);\n        if (counts[i]\
        \ % 2 !== 0) {\n            middleChar = char;\n        }\n    }\n\n    let\
        \ secondHalf = firstHalf.split(\"\").reverse().join(\"\");\n    return firstHalf\
        \ + middleChar + secondHalf;\n};"
      typescript: "function smallestPalindrome(s: string): string {\n    let counts\
        \ = new Array(26).fill(0);\n    for (let i = 0; i < s.length; i++) {\n     \
        \   counts[s.charCodeAt(i) - 97]++;\n    }\n\n    let firstHalf: string[] =\
        \ [];\n    let middleChar: string = \"\";\n\n    for (let i = 0; i < 26; i++)\
        \ {\n        let char = String.fromCharCode(97 + i);\n        let halfCount\
        \ = Math.floor(counts[i] / 2);\n        for (let j = 0; j < halfCount; j++)\
        \ {\n            firstHalf.push(char);\n        }\n        if (counts[i] % 2\
        \ !== 0) {\n            middleChar = char;\n        }\n    }\n\n    let firstHalfStr\
        \ = firstHalf.join(\"\");\n    let secondHalfStr = firstHalf.reverse().join(\"\
        \");\n    return firstHalfStr + middleChar + secondHalfStr;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return String\n\
        \     */\n    function smallestPalindrome($s) {\n        $counts = array_fill(0,\
        \ 26, 0);\n        $n = strlen($s);\n        for ($i = 0; $i < $n; $i++) {\n\
        \            $counts[ord($s[$i]) - ord('a')]++;\n        }\n\n        $firstHalf\
        \ = \"\";\n        $middleChar = \"\";\n\n        for ($i = 0; $i < 26; $i++)\
        \ {\n            $char = chr(ord('a') + $i);\n            $count = $counts[$i];\n\
        \            $halfCount = intdiv($count, 2);\n            $firstHalf .= str_repeat($char,\
        \ $halfCount);\n            if ($count % 2 !== 0) {\n                $middleChar\
        \ = $char;\n            }\n        }\n\n        return $firstHalf . $middleChar\
        \ . strrev($firstHalf);\n    }\n}"
      swift: "class Solution {\n    func smallestPalindrome(_ s: String) -> String {\n\
        \        var counts = [Int](repeating: 0, count: 26)\n        let aValue = Int(UnicodeScalar(\"\
        a\").value)\n\n        for char in s.unicodeScalars {\n            counts[Int(char.value)\
        \ - aValue] += 1\n        }\n\n        var firstHalf = \"\"\n        var middleChar\
        \ = \"\"\n\n        for i in 0..<26 {\n            let char = Character(UnicodeScalar(aValue\
        \ + i)!)\n            let halfCount = counts[i] / 2\n            if halfCount\
        \ > 0 {\n                firstHalf.append(String(repeating: char, count: halfCount))\n\
        \            }\n            if counts[i] % 2 != 0 {\n                middleChar\
        \ = String(char)\n            }\n        }\n\n        let secondHalf = String(firstHalf.reversed())\n\
        \        return firstHalf + middleChar + secondHalf\n    }\n}"
      kotlin: "class Solution {\n    fun smallestPalindrome(s: String): String {\n \
        \       val counts = IntArray(26)\n        for (c in s) {\n            counts[c\
        \ - 'a']++\n        }\n        val firstHalf = StringBuilder()\n        var\
        \ middleChar = \"\"\n        for (i in 0 until 26) {\n            val char =\
        \ ('a' + i).toChar()\n            if (counts[i] % 2 != 0) {\n              \
        \  middleChar = char.toString()\n            }\n            repeat(counts[i]\
        \ / 2) {\n                firstHalf.append(char)\n            }\n        }\n\
        \        val first = firstHalf.toString()\n        return first + middleChar\
        \ + first.reversed()\n    }\n}"
      dart: "class Solution {\n  String smallestPalindrome(String s) {\n    List<int>\
        \ counts = List.filled(26, 0);\n    for (int i = 0; i < s.length; i++) {\n \
        \     counts[s.codeUnitAt(i) - 97]++;\n    }\n    StringBuffer firstHalf = StringBuffer();\n\
        \    String middleChar = \"\";\n    for (int i = 0; i < 26; i++) {\n      if\
        \ (counts[i] % 2 != 0) {\n        middleChar = String.fromCharCode(i + 97);\n\
        \      }\n      int halfCount = counts[i] ~/ 2;\n      if (halfCount > 0) {\n\
        \        firstHalf.write(String.fromCharCode(i + 97) * halfCount);\n      }\n\
        \    }\n    String first = firstHalf.toString();\n    return first + middleChar\
        \ + String.fromCharCodes(first.codeUnits.toList().reversed);\n  }\n}"
      go: "import (\n\t\"strings\"\n)\n\nfunc smallestPalindrome(s string) string {\n\
        \tcounts := make([]int, 26)\n\tfor i := 0; i < len(s); i++ {\n\t\tcounts[s[i]-'a']++\n\
        \t}\n\tvar firstHalf strings.Builder\n\tvar middleChar byte\n\tvar hasMiddle\
        \ bool\n\tfor i := 0; i < 26; i++ {\n\t\tchar := byte('a' + i)\n\t\tif counts[i]%2\
        \ != 0 {\n\t\t\tmiddleChar = char\n\t\t\thasMiddle = true\n\t\t}\n\t\tfor j\
        \ := 0; j < counts[i]/2; j++ {\n\t\t\tfirstHalf.WriteByte(char)\n\t\t}\n\t}\n\
        \tfirst := firstHalf.String()\n\tvar result strings.Builder\n\tresult.Grow(len(s))\n\
        \tresult.WriteString(first)\n\tif hasMiddle {\n\t\tresult.WriteByte(middleChar)\n\
        \t}\n\tfor i := len(first) - 1; i >= 0; i-- {\n\t\tresult.WriteByte(first[i])\n\
        \t}\n\treturn result.String()\n}"
      ruby: "# @param {String} s\n# @return {String}\ndef smallest_palindrome(s)\n \
        \ counts = Array.new(26, 0)\n  s.each_byte { |b| counts[b - 97] += 1 }\n  first_half\
        \ = \"\"\n  middle_char = \"\"\n  (0..25).each do |i|\n    char = (i + 97).chr\n\
        \    if counts[i] % 2 != 0\n      middle_char = char\n    end\n    first_half\
        \ << (char * (counts[i] / 2))\n  end\n  first_half + middle_char + first_half.reverse\n\
        end"
      scala: "object Solution {\n    def smallestPalindrome(s: String): String = {\n\
        \        val counts = new Array[Int](26)\n        for (c <- s) {\n         \
        \   counts(c - 'a') += 1\n        }\n        val firstHalf = new StringBuilder()\n\
        \        var middleChar = \"\"\n        for (i <- 0 until 26) {\n          \
        \  val char = (i + 'a'.toInt).toChar\n            if (counts(i) % 2 != 0) {\n\
        \                middleChar = char.toString\n            }\n            for\
        \ (_ <- 0 until (counts(i) / 2)) {\n                firstHalf.append(char)\n\
        \            }\n        }\n        val first = firstHalf.toString()\n      \
        \  first + middleChar + first.reverse\n    }\n}"
      rust: "impl Solution {\n    pub fn smallest_palindrome(s: String) -> String {\n\
        \        let mut counts = [0; 26];\n        for b in s.bytes() {\n         \
        \   counts[(b - b'a') as usize] += 1;\n        }\n        let mut first_half\
        \ = String::with_capacity(s.len() / 2);\n        let mut mid = String::new();\n\
        \        for i in 0..26 {\n            let char_code = (b'a' + i as u8) as char;\n\
        \            let count = counts[i];\n            if count % 2 == 1 {\n     \
        \           mid.push(char_code);\n            }\n            for _ in 0..(count\
        \ / 2) {\n                first_half.push(char_code);\n            }\n     \
        \   }\n        let mut result = first_half.clone();\n        result.push_str(&mid);\n\
        \        result.extend(first_half.chars().rev());\n        result\n    }\n}"
      racket: "(define/contract (smallest-palindrome s)\n  (-> string? string?)\n  (let\
        \ ([counts (make-vector 26 0)])\n    (for ([c (in-string s)])\n      (let ([idx\
        \ (- (char->integer c) (char->integer #\\a))])\n        (vector-set! counts\
        \ idx (add1 (vector-ref counts idx)))))\n    (let-values ([(half-parts-list\
        \ mid-str)\n                  (for/fold ([half-acc '()] [mid \"\"])\n      \
        \                      ([i (in-range 26)])\n                    (let* ([count\
        \ (vector-ref counts i)]\n                           [char (integer->char (+\
        \ (char->integer #\\a) i))])\n                      (values (cons (make-string\
        \ (quotient count 2) char) half-acc)\n                              (if (odd?\
        \ count) (string char) mid))))])\n      (let* ([first-half (apply string-append\
        \ (reverse half-parts-list))]\n             [second-half (list->string (reverse\
        \ (string->list first-half)))])\n        (string-append first-half mid-str second-half)))))"
      erlang: "-spec smallest_palindrome(S :: unicode:unicode_binary()) -> unicode:unicode_binary().\n\
        smallest_palindrome(S) ->\n  Counts = count_chars(S, #{}),\n  {HalfList, Mid}\
        \ = lists:foldl(fun(Char, {HAcc, MAcc}) ->\n    Count = maps:get(Char, Counts,\
        \ 0),\n    NewM = if Count rem 2 == 1 -> <<Char>>; true -> MAcc end,\n    NewH\
        \ = if Count div 2 > 0 -> [binary:copy(<<Char>>, Count div 2) | HAcc]; true\
        \ -> HAcc end,\n    {NewH, NewM}\n  end, {[], <<>>}, lists:seq($a, $z)),\n \
        \ FirstHalf = list_to_binary(lists:reverse(HalfList)),\n  SecondHalf = list_to_binary(lists:reverse(binary_to_list(FirstHalf))),\n\
        \  <<FirstHalf/binary, Mid/binary, SecondHalf/binary>>.\n\ncount_chars(<<C,\
        \ Rest/binary>>, Acc) ->\n  count_chars(Rest, Acc#{C => maps:get(C, Acc, 0)\
        \ + 1});\ncount_chars(<<>>, Acc) ->\n  Acc."
      elixir: "defmodule Solution do\n  @spec smallest_palindrome(s :: String.t) ::\
        \ String.t\n  def smallest_palindrome(s) do\n    counts = s\n             |>\
        \ String.to_charlist()\n             |> Enum.reduce(%{}, fn c, acc ->\n    \
        \           Map.update(acc, c, 1, &(&1 + 1))\n             end)\n\n    {half_parts,\
        \ mid_char} = Enum.reduce(?a..?z, {[], \"\"}, fn char, {half_acc, mid_acc} ->\n\
        \      count = Map.get(counts, char, 0)\n      new_mid = if rem(count, 2) ==\
        \ 1, do: <<char>>, else: mid_acc\n      half_part = String.duplicate(<<char>>,\
        \ div(count, 2))\n      {[half_part | half_acc], new_mid}\n    end)\n\n    first_half\
        \ = half_parts |> Enum.reverse() |> Enum.join()\n    first_half <> mid_char\
        \ <> String.reverse(first_half)\n  end\nend"
    approach: 'To find the lexicographically smallest palindromic permutation, we construct
      the first half of the string by collecting half of the total occurrences of each
      character present in the input string. Since the input is guaranteed to be a palindrome,
      at most one character can have an odd frequency, and this character must occupy
      the center position. To minimize the lexicographical value, the first half is
      built by appending characters in alphabetical order from ''a'' to ''z'' based
      on their required half-counts.


      The final palindromic string is formed by concatenating this sorted first half,
      the single middle character (if any character had an odd count), and the reverse
      of the first half. This structure ensures that the smallest possible characters
      are placed at the beginning of the string, which results in the lexicographically
      smallest possible palindrome while maintaining the symmetry required.'
    time_complexity: O(n) where n is the length of the string s. We perform one pass
      over the string to count character frequencies and another pass to construct the
      result string, both of which are linear in relation to the input size.
    space_complexity: O(n) for the output string. The auxiliary space used for storing
      character counts is O(1) because the size of the alphabet is constant (26 lowercase
      English letters).
    elapsed_time: 114.46423721313477
    model: gemini-3-flash-preview
    generated_at: '2026-07-28 01:52:06 '
---

## Problem #3517: Smallest Palindromic Rearrangement I

**Difficulty:** Medium

**Topics:** String, Sorting, Counting Sort

## Problem Description

<p>You are given a <strong><span data-keyword="palindrome-string">palindromic</span></strong> string <code>s</code>.</p>

<p>Return the <strong><span data-keyword="lexicographically-smaller-string">lexicographically smallest</span></strong> palindromic <span data-keyword="permutation-string">permutation</span> of <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;z&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;z&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>A string of only one character is already the lexicographically smallest palindrome.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;babab&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;abbba&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>Rearranging <code>&quot;babab&quot;</code> &rarr; <code>&quot;abbba&quot;</code> gives the smallest lexicographic palindrome.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;daccad&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;acddca&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>Rearranging <code>&quot;daccad&quot;</code> &rarr; <code>&quot;acddca&quot;</code> gives the smallest lexicographic palindrome.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
	<li><code>s</code> is guaranteed to be palindromic.</li>
</ul>


## Hints

1. Consider a palindrome as composed of two mirror-image halves.

2. Construct one half (using `s`), and then the other half is its reverse to obtain the lexicographically smallest permutation.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To find the lexicographically smallest palindromic permutation, we construct the first half of the string by collecting half of the total occurrences of each character present in the input string. Since the input is guaranteed to be a palindrome, at most one character can have an odd frequency, and this character must occupy the center position. To minimize the lexicographical value, the first half is built by appending characters in alphabetical order from 'a' to 'z' based on their required half-counts.

The final palindromic string is formed by concatenating this sorted first half, the single middle character (if any character had an odd count), and the reverse of the first half. This structure ensures that the smallest possible characters are placed at the beginning of the string, which results in the lexicographically smallest possible palindrome while maintaining the symmetry required.

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
    string smallestPalindrome(string s) {
        int counts[26] = {0};
        for (char c : s) {
            counts[c - 'a']++;
        }

        string firstHalf = "";
        char middleChar = 0;

        for (int i = 0; i < 26; ++i) {
            if (counts[i] % 2 != 0) {
                middleChar = (char)('a' + i);
            }
            for (int j = 0; j < counts[i] / 2; ++j) {
                firstHalf += (char)('a' + i);
            }
        }

        string secondHalf = firstHalf;
        reverse(secondHalf.begin(), secondHalf.end());

        if (middleChar != 0) {
            return firstHalf + middleChar + secondHalf;
        }
        return firstHalf + secondHalf;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public String smallestPalindrome(String s) {
        int[] counts = new int[26];
        for (int i = 0; i < s.length(); i++) {
            counts[s.charAt(i) - 'a']++;
        }

        StringBuilder firstHalf = new StringBuilder();
        Character middleChar = null;

        for (int i = 0; i < 26; i++) {
            if (counts[i] % 2 != 0) {
                middleChar = (char) ('a' + i);
            }
            int half = counts[i] / 2;
            for (int j = 0; j < half; j++) {
                firstHalf.append((char) ('a' + i));
            }
        }

        String prefix = firstHalf.toString();
        String suffix = firstHalf.reverse().toString();

        if (middleChar != null) {
            return prefix + middleChar + suffix;
        } else {
            return prefix + suffix;
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        counts = Counter(s)

        first_half_list = []
        middle_char = ""

        for char_code in range(ord('a'), ord('z') + 1):
            char = chr(char_code)
            if char in counts:
                if counts[char] % 2 != 0:
                    middle_char = char
                first_half_list.append(char * (counts[char] // 2))

        first_half = "".join(first_half_list)
        return first_half + middle_char + first_half[::-1]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import Counter
        counts = Counter(s)

        first_half_chars = []
        middle_char = ""

        for i in range(26):
            char = chr(ord('a') + i)
            if char in counts:
                count = counts[char]
                if count % 2 != 0:
                    middle_char = char
                first_half_chars.append(char * (count // 2))

        first_half = "".join(first_half_chars)
        return first_half + middle_char + first_half[::-1]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <string.h>
#include <stdlib.h>

char* smallestPalindrome(char* s) {
    int n = strlen(s);
    int counts[26] = {0};
    for (int i = 0; i < n; i++) {
        counts[s[i] - 'a']++;
    }

    char* result = (char*)malloc((n + 1) * sizeof(char));
    int left = 0;
    int mid_idx = -1;

    for (int i = 0; i < 26; i++) {
        if (counts[i] % 2 != 0) {
            mid_idx = i;
        }
        int half = counts[i] / 2;
        for (int j = 0; j < half; j++) {
            result[left++] = (char)('a' + i);
        }
    }

    int prefix_len = left;
    if (mid_idx != -1) {
        result[left++] = (char)('a' + mid_idx);
    }

    for (int i = prefix_len - 1; i >= 0; i--) {
        result[left++] = result[i];
    }

    result[n] = '\0';
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System.Text;

public class Solution {
    public string SmallestPalindrome(string s) {
        int[] counts = new int[26];
        foreach (char c in s) {
            counts[c - 'a']++;
        }

        StringBuilder firstHalf = new StringBuilder();
        char middleChar = '\0';
        bool hasMiddle = false;

        for (int i = 0; i < 26; i++) {
            int halfCount = counts[i] / 2;
            firstHalf.Append((char)('a' + i), halfCount);
            if (counts[i] % 2 != 0) {
                middleChar = (char)('a' + i);
                hasMiddle = true;
            }
        }

        string first = firstHalf.ToString();
        char[] reversedArray = first.ToCharArray();
        System.Array.Reverse(reversedArray);
        string second = new string(reversedArray);

        if (hasMiddle) {
            return first + middleChar + second;
        } else {
            return first + second;
        }
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
 * @return {string}
 */
var smallestPalindrome = function(s) {
    let counts = new Array(26).fill(0);
    for (let char of s) {
        counts[char.charCodeAt(0) - 97]++;
    }

    let firstHalf = "";
    let middleChar = "";

    for (let i = 0; i < 26; i++) {
        let char = String.fromCharCode(97 + i);
        let halfCount = Math.floor(counts[i] / 2);
        firstHalf += char.repeat(halfCount);
        if (counts[i] % 2 !== 0) {
            middleChar = char;
        }
    }

    let secondHalf = firstHalf.split("").reverse().join("");
    return firstHalf + middleChar + secondHalf;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function smallestPalindrome(s: string): string {
    let counts = new Array(26).fill(0);
    for (let i = 0; i < s.length; i++) {
        counts[s.charCodeAt(i) - 97]++;
    }

    let firstHalf: string[] = [];
    let middleChar: string = "";

    for (let i = 0; i < 26; i++) {
        let char = String.fromCharCode(97 + i);
        let halfCount = Math.floor(counts[i] / 2);
        for (let j = 0; j < halfCount; j++) {
            firstHalf.push(char);
        }
        if (counts[i] % 2 !== 0) {
            middleChar = char;
        }
    }

    let firstHalfStr = firstHalf.join("");
    let secondHalfStr = firstHalf.reverse().join("");
    return firstHalfStr + middleChar + secondHalfStr;
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
     * @return String
     */
    function smallestPalindrome($s) {
        $counts = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $counts[ord($s[$i]) - ord('a')]++;
        }

        $firstHalf = "";
        $middleChar = "";

        for ($i = 0; $i < 26; $i++) {
            $char = chr(ord('a') + $i);
            $count = $counts[$i];
            $halfCount = intdiv($count, 2);
            $firstHalf .= str_repeat($char, $halfCount);
            if ($count % 2 !== 0) {
                $middleChar = $char;
            }
        }

        return $firstHalf . $middleChar . strrev($firstHalf);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func smallestPalindrome(_ s: String) -> String {
        var counts = [Int](repeating: 0, count: 26)
        let aValue = Int(UnicodeScalar("a").value)

        for char in s.unicodeScalars {
            counts[Int(char.value) - aValue] += 1
        }

        var firstHalf = ""
        var middleChar = ""

        for i in 0..<26 {
            let char = Character(UnicodeScalar(aValue + i)!)
            let halfCount = counts[i] / 2
            if halfCount > 0 {
                firstHalf.append(String(repeating: char, count: halfCount))
            }
            if counts[i] % 2 != 0 {
                middleChar = String(char)
            }
        }

        let secondHalf = String(firstHalf.reversed())
        return firstHalf + middleChar + secondHalf
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun smallestPalindrome(s: String): String {
        val counts = IntArray(26)
        for (c in s) {
            counts[c - 'a']++
        }
        val firstHalf = StringBuilder()
        var middleChar = ""
        for (i in 0 until 26) {
            val char = ('a' + i).toChar()
            if (counts[i] % 2 != 0) {
                middleChar = char.toString()
            }
            repeat(counts[i] / 2) {
                firstHalf.append(char)
            }
        }
        val first = firstHalf.toString()
        return first + middleChar + first.reversed()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  String smallestPalindrome(String s) {
    List<int> counts = List.filled(26, 0);
    for (int i = 0; i < s.length; i++) {
      counts[s.codeUnitAt(i) - 97]++;
    }
    StringBuffer firstHalf = StringBuffer();
    String middleChar = "";
    for (int i = 0; i < 26; i++) {
      if (counts[i] % 2 != 0) {
        middleChar = String.fromCharCode(i + 97);
      }
      int halfCount = counts[i] ~/ 2;
      if (halfCount > 0) {
        firstHalf.write(String.fromCharCode(i + 97) * halfCount);
      }
    }
    String first = firstHalf.toString();
    return first + middleChar + String.fromCharCodes(first.codeUnits.toList().reversed);
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import (
	"strings"
)

func smallestPalindrome(s string) string {
	counts := make([]int, 26)
	for i := 0; i < len(s); i++ {
		counts[s[i]-'a']++
	}
	var firstHalf strings.Builder
	var middleChar byte
	var hasMiddle bool
	for i := 0; i < 26; i++ {
		char := byte('a' + i)
		if counts[i]%2 != 0 {
			middleChar = char
			hasMiddle = true
		}
		for j := 0; j < counts[i]/2; j++ {
			firstHalf.WriteByte(char)
		}
	}
	first := firstHalf.String()
	var result strings.Builder
	result.Grow(len(s))
	result.WriteString(first)
	if hasMiddle {
		result.WriteByte(middleChar)
	}
	for i := len(first) - 1; i >= 0; i-- {
		result.WriteByte(first[i])
	}
	return result.String()
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @return {String}
def smallest_palindrome(s)
  counts = Array.new(26, 0)
  s.each_byte { |b| counts[b - 97] += 1 }
  first_half = ""
  middle_char = ""
  (0..25).each do |i|
    char = (i + 97).chr
    if counts[i] % 2 != 0
      middle_char = char
    end
    first_half << (char * (counts[i] / 2))
  end
  first_half + middle_char + first_half.reverse
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def smallestPalindrome(s: String): String = {
        val counts = new Array[Int](26)
        for (c <- s) {
            counts(c - 'a') += 1
        }
        val firstHalf = new StringBuilder()
        var middleChar = ""
        for (i <- 0 until 26) {
            val char = (i + 'a'.toInt).toChar
            if (counts(i) % 2 != 0) {
                middleChar = char.toString
            }
            for (_ <- 0 until (counts(i) / 2)) {
                firstHalf.append(char)
            }
        }
        val first = firstHalf.toString()
        first + middleChar + first.reverse
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn smallest_palindrome(s: String) -> String {
        let mut counts = [0; 26];
        for b in s.bytes() {
            counts[(b - b'a') as usize] += 1;
        }
        let mut first_half = String::with_capacity(s.len() / 2);
        let mut mid = String::new();
        for i in 0..26 {
            let char_code = (b'a' + i as u8) as char;
            let count = counts[i];
            if count % 2 == 1 {
                mid.push(char_code);
            }
            for _ in 0..(count / 2) {
                first_half.push(char_code);
            }
        }
        let mut result = first_half.clone();
        result.push_str(&mid);
        result.extend(first_half.chars().rev());
        result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (smallest-palindrome s)
  (-> string? string?)
  (let ([counts (make-vector 26 0)])
    (for ([c (in-string s)])
      (let ([idx (- (char->integer c) (char->integer #\a))])
        (vector-set! counts idx (add1 (vector-ref counts idx)))))
    (let-values ([(half-parts-list mid-str)
                  (for/fold ([half-acc '()] [mid ""])
                            ([i (in-range 26)])
                    (let* ([count (vector-ref counts i)]
                           [char (integer->char (+ (char->integer #\a) i))])
                      (values (cons (make-string (quotient count 2) char) half-acc)
                              (if (odd? count) (string char) mid))))])
      (let* ([first-half (apply string-append (reverse half-parts-list))]
             [second-half (list->string (reverse (string->list first-half)))])
        (string-append first-half mid-str second-half)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec smallest_palindrome(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
smallest_palindrome(S) ->
  Counts = count_chars(S, #{}),
  {HalfList, Mid} = lists:foldl(fun(Char, {HAcc, MAcc}) ->
    Count = maps:get(Char, Counts, 0),
    NewM = if Count rem 2 == 1 -> <<Char>>; true -> MAcc end,
    NewH = if Count div 2 > 0 -> [binary:copy(<<Char>>, Count div 2) | HAcc]; true -> HAcc end,
    {NewH, NewM}
  end, {[], <<>>}, lists:seq($a, $z)),
  FirstHalf = list_to_binary(lists:reverse(HalfList)),
  SecondHalf = list_to_binary(lists:reverse(binary_to_list(FirstHalf))),
  <<FirstHalf/binary, Mid/binary, SecondHalf/binary>>.

count_chars(<<C, Rest/binary>>, Acc) ->
  count_chars(Rest, Acc#{C => maps:get(C, Acc, 0) + 1});
count_chars(<<>>, Acc) ->
  Acc.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec smallest_palindrome(s :: String.t) :: String.t
  def smallest_palindrome(s) do
    counts = s
             |> String.to_charlist()
             |> Enum.reduce(%{}, fn c, acc ->
               Map.update(acc, c, 1, &(&1 + 1))
             end)

    {half_parts, mid_char} = Enum.reduce(?a..?z, {[], ""}, fn char, {half_acc, mid_acc} ->
      count = Map.get(counts, char, 0)
      new_mid = if rem(count, 2) == 1, do: <<char>>, else: mid_acc
      half_part = String.duplicate(<<char>>, div(count, 2))
      {[half_part | half_acc], new_mid}
    end)

    first_half = half_parts |> Enum.reverse() |> Enum.join()
    first_half <> mid_char <> String.reverse(first_half)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the string s. We perform one pass over the string to count character frequencies and another pass to construct the result string, both of which are linear in relation to the input size.
- **Space Complexity:** O(n) for the output string. The auxiliary space used for storing character counts is O(1) because the size of the alphabet is constant (26 lowercase English letters).
