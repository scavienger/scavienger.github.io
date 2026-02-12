---
layout: post
title: "Longest Balanced Substring I"
date: 2026-02-12 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Hash Table", "String", "Counting", "Enumeration"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/longest-balanced-substring-i/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int longestBalanced(string s) {\n       \
        \ int n = s.length();\n        int maxLen = 0;\n        for (int i = 0; i <\
        \ n; i++) {\n            int freq[26] = {0};\n            for (int j = i; j\
        \ < n; j++) {\n                freq[s[j] - 'a']++;\n                int target\
        \ = -1;\n                bool ok = true;\n                for (int k = 0; k\
        \ < 26; k++) {\n                    if (freq[k] > 0) {\n                   \
        \     if (target == -1) target = freq[k];\n                        else if (freq[k]\
        \ != target) {\n                            ok = false;\n                  \
        \          break;\n                        }\n                    }\n      \
        \          }\n                if (ok) {\n                    maxLen = std::max(maxLen,\
        \ j - i + 1);\n                }\n            }\n        }\n        return maxLen;\n\
        \    }\n};"
      java: "class Solution {\n    public int longestBalanced(String s) {\n        int\
        \ n = s.length();\n        int maxLen = 0;\n        for (int i = 0; i < n; i++)\
        \ {\n            int[] freq = new int[26];\n            for (int j = i; j <\
        \ n; j++) {\n                freq[s.charAt(j) - 'a']++;\n                int\
        \ target = -1;\n                boolean ok = true;\n                for (int\
        \ k = 0; k < 26; k++) {\n                    if (freq[k] > 0) {\n          \
        \              if (target == -1) target = freq[k];\n                       \
        \ else if (freq[k] != target) {\n                            ok = false;\n \
        \                           break;\n                        }\n            \
        \        }\n                }\n                if (ok) {\n                 \
        \   maxLen = Math.max(maxLen, j - i + 1);\n                }\n            }\n\
        \        }\n        return maxLen;\n    }\n}"
      python: "class Solution(object):\n    def longestBalanced(self, s):\n        \"\
        \"\"\n        :type s: str\n        :rtype: int\n        \"\"\"\n        n =\
        \ len(s)\n        max_len = 0\n        for i in range(n):\n            freq\
        \ = [0] * 26\n            for j in range(i, n):\n                freq[ord(s[j])\
        \ - 97] += 1\n                target = -1\n                ok = True\n     \
        \           for count in freq:\n                    if count > 0:\n        \
        \                if target == -1:\n                            target = count\n\
        \                        elif count != target:\n                           \
        \ ok = False\n                            break\n                if ok:\n  \
        \                  curr_len = j - i + 1\n                    if curr_len > max_len:\n\
        \                        max_len = curr_len\n        return max_len"
      python3: "class Solution:\n    def longestBalanced(self, s: str) -> int:\n   \
        \     n = len(s)\n        max_len = 0\n        for i in range(n):\n        \
        \    freq = [0] * 26\n            for j in range(i, n):\n                freq[ord(s[j])\
        \ - 97] += 1\n                target = -1\n                ok = True\n     \
        \           for count in freq:\n                    if count > 0:\n        \
        \                if target == -1:\n                            target = count\n\
        \                        elif count != target:\n                           \
        \ ok = False\n                            break\n                if ok:\n  \
        \                  max_len = max(max_len, j - i + 1)\n        return max_len"
      c: "#include <string.h>\n\nint longestBalanced(char* s) {\n    int n = strlen(s);\n\
        \    int maxLen = 0;\n    for (int i = 0; i < n; i++) {\n        int freq[26]\
        \ = {0};\n        for (int j = i; j < n; j++) {\n            freq[s[j] - 'a']++;\n\
        \            int target = -1;\n            int ok = 1;\n            for (int\
        \ k = 0; k < 26; k++) {\n                if (freq[k] > 0) {\n              \
        \      if (target == -1) target = freq[k];\n                    else if (freq[k]\
        \ != target) {\n                        ok = 0;\n                        break;\n\
        \                    }\n                }\n            }\n            if (ok)\
        \ {\n                int currLen = j - i + 1;\n                if (currLen >\
        \ maxLen) maxLen = currLen;\n            }\n        }\n    }\n    return maxLen;\n\
        }"
      csharp: "public class Solution {\n    public int LongestBalanced(string s) {\n\
        \        int n = s.Length;\n        int maxLen = 0;\n        for (int i = 0;\
        \ i < n; i++) {\n            int[] freq = new int[26];\n            for (int\
        \ j = i; j < n; j++) {\n                freq[s[j] - 'a']++;\n              \
        \  int target = -1;\n                bool ok = true;\n                for (int\
        \ k = 0; k < 26; k++) {\n                    if (freq[k] > 0) {\n          \
        \              if (target == -1) target = freq[k];\n                       \
        \ else if (freq[k] != target) {\n                            ok = false;\n \
        \                           break;\n                        }\n            \
        \        }\n                }\n                if (ok) {\n                 \
        \   int currLen = j - i + 1;\n                    if (currLen > maxLen) maxLen\
        \ = currLen;\n                }\n            }\n        }\n        return maxLen;\n\
        \    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {number}\n */\nvar longestBalanced\
        \ = function(s) {\n    let n = s.length;\n    let maxLen = 0;\n    for (let\
        \ i = 0; i < n; i++) {\n        let freq = new Array(26).fill(0);\n        for\
        \ (let j = i; j < n; j++) {\n            freq[s.charCodeAt(j) - 97]++;\n   \
        \         let target = -1;\n            let ok = true;\n            for (let\
        \ k = 0; k < 26; k++) {\n                if (freq[k] > 0) {\n              \
        \      if (target === -1) target = freq[k];\n                    else if (freq[k]\
        \ !== target) {\n                        ok = false;\n                     \
        \   break;\n                    }\n                }\n            }\n      \
        \      if (ok) {\n                if (j - i + 1 > maxLen) maxLen = j - i + 1;\n\
        \            }\n        }\n    }\n    return maxLen;\n};"
      typescript: "function longestBalanced(s: string): number {\n    let maxLen = 0;\n\
        \    const n = s.length;\n    for (let i = 0; i < n; i++) {\n        const counts\
        \ = new Int32Array(26);\n        for (let j = i; j < n; j++) {\n           \
        \ counts[s.charCodeAt(j) - 97]++;\n            let freq = -1;\n            let\
        \ isBalanced = true;\n            for (let k = 0; k < 26; k++) {\n         \
        \       if (counts[k] > 0) {\n                    if (freq === -1) {\n     \
        \                   freq = counts[k];\n                    } else if (counts[k]\
        \ !== freq) {\n                        isBalanced = false;\n               \
        \         break;\n                    }\n                }\n            }\n\
        \            if (isBalanced) {\n                if (j - i + 1 > maxLen) {\n\
        \                    maxLen = j - i + 1;\n                }\n            }\n\
        \        }\n    }\n    return maxLen;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return Integer\n\
        \     */\n    function longestBalanced($s) {\n        $maxLen = 0;\n       \
        \ $n = strlen($s);\n        $aOrd = ord('a');\n        for ($i = 0; $i < $n;\
        \ $i++) {\n            $counts = array_fill(0, 26, 0);\n            for ($j\
        \ = $i; $j < $n; $j++) {\n                $counts[ord($s[$j]) - $aOrd]++;\n\
        \                $freq = -1;\n                $isBalanced = true;\n        \
        \        for ($k = 0; $k < 26; $k++) {\n                    if ($counts[$k]\
        \ > 0) {\n                        if ($freq === -1) {\n                    \
        \        $freq = $counts[$k];\n                        } else if ($counts[$k]\
        \ !== $freq) {\n                            $isBalanced = false;\n         \
        \                   break;\n                        }\n                    }\n\
        \                }\n                if ($isBalanced) {\n                   \
        \ $maxLen = max($maxLen, $j - $i + 1);\n                }\n            }\n \
        \       }\n        return $maxLen;\n    }\n}"
      swift: "class Solution {\n    func longestBalanced(_ s: String) -> Int {\n   \
        \     let n = s.count\n        let chars = Array(s)\n        let aValue = Int(Character(\"\
        a\").asciiValue!)\n        var maxLen = 0\n        for i in 0..<n {\n      \
        \      var counts = [Int](repeating: 0, count: 26)\n            for j in i..<n\
        \ {\n                let idx = Int(chars[j].asciiValue!) - aValue\n        \
        \        counts[idx] += 1\n                var freq = -1\n                var\
        \ isBalanced = true\n                for k in 0..<26 {\n                   \
        \ if counts[k] > 0 {\n                        if freq == -1 {\n            \
        \                freq = counts[k]\n                        } else if counts[k]\
        \ != freq {\n                            isBalanced = false\n              \
        \              break\n                        }\n                    }\n   \
        \             }\n                if isBalanced {\n                    maxLen\
        \ = max(maxLen, j - i + 1)\n                }\n            }\n        }\n  \
        \      return maxLen\n    }\n}"
      kotlin: "class Solution {\n    fun longestBalanced(s: String): Int {\n       \
        \ var maxLen = 0\n        val n = s.length\n        for (i in 0 until n) {\n\
        \            val counts = IntArray(26)\n            for (j in i until n) {\n\
        \                counts[s[j] - 'a']++\n                var freq = -1\n     \
        \           var isBalanced = true\n                for (k in 0 until 26) {\n\
        \                    if (counts[k] > 0) {\n                        if (freq\
        \ == -1) {\n                            freq = counts[k]\n                 \
        \       } else if (counts[k] != freq) {\n                            isBalanced\
        \ = false\n                            break\n                        }\n  \
        \                  }\n                }\n                if (isBalanced) {\n\
        \                    maxLen = Math.max(maxLen, j - i + 1)\n                }\n\
        \            }\n        }\n        return maxLen\n    }\n}"
      dart: "class Solution {\n  int longestBalanced(String s) {\n    int maxLen = 0;\n\
        \    int n = s.length;\n    int aCode = 'a'.codeUnitAt(0);\n    for (int i =\
        \ 0; i < n; i++) {\n      List<int> counts = List.filled(26, 0);\n      for\
        \ (int j = i; j < n; j++) {\n        counts[s.codeUnitAt(j) - aCode]++;\n  \
        \      int freq = -1;\n        bool isBalanced = true;\n        for (int k =\
        \ 0; k < 26; k++) {\n          if (counts[k] > 0) {\n            if (freq ==\
        \ -1) {\n              freq = counts[k];\n            } else if (counts[k] !=\
        \ freq) {\n              isBalanced = false;\n              break;\n       \
        \     }\n          }\n        }\n        if (isBalanced) {\n          if (j\
        \ - i + 1 > maxLen) {\n            maxLen = j - i + 1;\n          }\n      \
        \  }\n      }\n    }\n    return maxLen;\n  }\n}"
      go: "func longestBalanced(s string) int {\n    maxLen := 0\n    n := len(s)\n\
        \    for i := 0; i < n; i++ {\n        counts := [26]int{}\n        for j :=\
        \ i; j < n; j++ {\n            counts[s[j]-'a']++\n            freq := -1\n\
        \            isBalanced := true\n            for k := 0; k < 26; k++ {\n   \
        \             if counts[k] > 0 {\n                    if freq == -1 {\n    \
        \                    freq = counts[k]\n                    } else if counts[k]\
        \ != freq {\n                        isBalanced = false\n                  \
        \      break\n                    }\n                }\n            }\n    \
        \        if isBalanced {\n                if j-i+1 > maxLen {\n            \
        \        maxLen = j - i + 1\n                }\n            }\n        }\n \
        \   }\n    return maxLen\n}"
      ruby: "def longest_balanced(s)\n  max_len = 0\n  n = s.length\n  chars = s.chars\n\
        \  (0...n).each do |i|\n    counts = Hash.new(0)\n    (i...n).each do |j|\n\
        \      char = chars[j]\n      counts[char] += 1\n      freqs = counts.values\n\
        \      first = freqs[0]\n      if freqs.all? { |f| f == first }\n        len\
        \ = j - i + 1\n        max_len = len if len > max_len\n      end\n    end\n\
        \  end\n  max_len\nend"
      scala: "object Solution {\n    def longestBalanced(s: String): Int = {\n     \
        \   var maxLen = 0\n        val n = s.length\n        for (i <- 0 until n) {\n\
        \            val counts = new Array[Int](26)\n            for (j <- i until\
        \ n) {\n                counts(s(j) - 'a') += 1\n                var freq =\
        \ -1\n                var balanced = true\n                var k = 0\n     \
        \           while (k < 26) {\n                    if (counts(k) > 0) {\n   \
        \                     if (freq == -1) {\n                            freq =\
        \ counts(k)\n                        } else if (counts(k) != freq) {\n     \
        \                       balanced = false\n                            k = 26\n\
        \                        }\n                    }\n                    k +=\
        \ 1\n                }\n                if (balanced) {\n                  \
        \  val len = j - i + 1\n                    if (len > maxLen) maxLen = len\n\
        \                }\n            }\n        }\n        maxLen\n    }\n}"
      rust: "impl Solution {\n    pub fn longest_balanced(s: String) -> i32 {\n    \
        \    let mut max_len = 0;\n        let n = s.len();\n        let bytes = s.as_bytes();\n\
        \        for i in 0..n {\n            let mut counts = [0; 26];\n          \
        \  for j in i..n {\n                counts[(bytes[j] - b'a') as usize] += 1;\n\
        \                let mut freq = -1;\n                let mut balanced = true;\n\
        \                for k in 0..26 {\n                    if counts[k] > 0 {\n\
        \                        if freq == -1 {\n                            freq =\
        \ counts[k];\n                        } else if counts[k] != freq {\n      \
        \                      balanced = false;\n                            break;\n\
        \                        }\n                    }\n                }\n     \
        \           if balanced {\n                    max_len = max_len.max((j - i\
        \ + 1) as i32);\n                }\n            }\n        }\n        max_len\n\
        \    }\n}"
      racket: "(define/contract (longest-balanced s)\n  (-> string? exact-integer?)\n\
        \  (let ([n (string-length s)])\n    (let loop-i ([i 0] [max-len 0])\n     \
        \ (if (= i n)\n          max-len\n          (let* ([counts (make-hash)]\n  \
        \               [res-max (let loop-j ([j i] [cur-max max-len])\n           \
        \                 (if (= j n)\n                                cur-max\n   \
        \                             (let* ([char (string-ref s j)]\n             \
        \                          [cnt (hash-ref counts char 0)])\n               \
        \                   (hash-set! counts char (+ cnt 1))\n                    \
        \              (let* ([freqs (hash-values counts)]\n                       \
        \                  [first (car freqs)]\n                                   \
        \      [balanced (andmap (lambda (f) (= f first)) freqs)]\n                \
        \                         [next-max (if balanced (max cur-max (+ (- j i) 1))\
        \ cur-max)])\n                                    (loop-j (+ j 1) next-max)))))])\n\
        \            (loop-i (+ i 1) res-max))))))"
      erlang: "-spec longest_balanced(S :: unicode:unicode_binary()) -> integer().\n\
        longest_balanced(S) ->\n  L = binary_to_list(S),\n  find_max(L, 0).\n\nfind_max([],\
        \ Max) -> Max;\nfind_max([_ | T] = List, Max) ->\n  NewMax = check_substrings(List,\
        \ Max, 1, #{}),\n  find_max(T, NewMax).\n\ncheck_substrings([], Max, _, _) ->\
        \ Max;\ncheck_substrings([H | T], Max, Len, Counts) ->\n  NewCounts = maps:update_with(H,\
        \ fun(V) -> V + 1 end, 1, Counts),\n  Freqs = maps:values(NewCounts),\n  [First\
        \ | Rest] = Freqs,\n  IsBalanced = lists:all(fun(F) -> F == First end, Rest),\n\
        \  NextMax = if IsBalanced -> erlang:max(Max, Len); true -> Max end,\n  check_substrings(T,\
        \ NextMax, Len + 1, NewCounts)."
      elixir: "defmodule Solution do\n  @spec longest_balanced(s :: String.t) :: integer\n\
        \  def longest_balanced(s) do\n    chars = String.to_charlist(s)\n    n = length(chars)\n\
        \    Enum.reduce(0..(n - 1), 0, fn i, max_so_far ->\n      sub_chars = Enum.drop(chars,\
        \ i)\n      {_, inner_max} = Enum.reduce(sub_chars, {%{}, max_so_far}, fn char,\
        \ {counts, current_max_inner} ->\n        new_counts = Map.update(counts, char,\
        \ 1, fn v -> v + 1 end)\n        freqs = Map.values(new_counts)\n        [first\
        \ | rest] = freqs\n        is_balanced = Enum.all?(rest, fn f -> f == first\
        \ end)\n        new_max = if is_balanced do\n          len = length(freqs) *\
        \ first\n          if len > current_max_inner, do: len, else: current_max_inner\n\
        \        else\n          current_max_inner\n        end\n        {new_counts,\
        \ new_max}\n      end)\n      inner_max\n    end)\n  end\nend"
    approach: The algorithm uses a brute-force approach to explore every possible substring
      of the input string $s$. We iterate through all potential starting indices $i$
      from 0 to $N-1$, and for each start, we expand the substring by moving the end
      index $j$ from $i$ to $N-1$. This allows us to inspect every contiguous sequence
      of characters within the string while maintaining a character frequency count
      incrementally.
    time_complexity: O(N^2 \cdot \Sigma) with one-paragraph explanation. The algorithm
      iterates through $O(N^2)$ substrings. For each substring, we update character
      frequencies and perform a check over the fixed-size alphabet $\Sigma = 26$. This
      results in a total complexity of roughly $26 \times 10^6$ operations for $N=1000$,
      which is well within the execution time limits.
    space_complexity: O(\Sigma) with one-paragraph explanation. The space used is independent
      of the input string length $N$. We only store a frequency array of size $\Sigma
      = 26$ to track character counts for the current substring, leading to constant
      extra space $O(1)$ relative to the input size.
    elapsed_time: 173.7861623764038
    model: gemini-3-flash-preview
    generated_at: '2026-02-12 01:29:32 '
---

## Problem #3713: Longest Balanced Substring I

**Difficulty:** Medium

**Topics:** Hash Table, String, Counting, Enumeration

## Problem Description

<p>You are given a string <code>s</code> consisting of lowercase English letters.</p>

<p>A <strong><span data-keyword="substring-nonempty">substring</span></strong> of <code>s</code> is called <strong>balanced</strong> if all <strong>distinct</strong> characters in the <strong>substring</strong> appear the <strong>same</strong> number of times.</p>

<p>Return the <strong>length</strong> of the <strong>longest balanced substring</strong> of <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abbac&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The longest balanced substring is <code>&quot;abba&quot;</code> because both distinct characters <code>&#39;a&#39;</code> and <code>&#39;b&#39;</code> each appear exactly 2 times.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;zzabccy&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The longest balanced substring is <code>&quot;zabc&quot;</code> because the distinct characters <code>&#39;z&#39;</code>, <code>&#39;a&#39;</code>, <code>&#39;b&#39;</code>, and <code>&#39;c&#39;</code> each appear exactly 1 time.​​​​​​​</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;aba&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p><strong>​​​​​​​</strong>One of the longest balanced substrings is <code>&quot;ab&quot;</code> because both distinct characters <code>&#39;a&#39;</code> and <code>&#39;b&#39;</code> each appear exactly 1 time. Another longest balanced substring is <code>&quot;ba&quot;</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>


## Hints

1. Use bruteforce over all substrings

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm uses a brute-force approach to explore every possible substring of the input string $s$. We iterate through all potential starting indices $i$ from 0 to $N-1$, and for each start, we expand the substring by moving the end index $j$ from $i$ to $N-1$. This allows us to inspect every contiguous sequence of characters within the string while maintaining a character frequency count incrementally.

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
    int longestBalanced(string s) {
        int n = s.length();
        int maxLen = 0;
        for (int i = 0; i < n; i++) {
            int freq[26] = {0};
            for (int j = i; j < n; j++) {
                freq[s[j] - 'a']++;
                int target = -1;
                bool ok = true;
                for (int k = 0; k < 26; k++) {
                    if (freq[k] > 0) {
                        if (target == -1) target = freq[k];
                        else if (freq[k] != target) {
                            ok = false;
                            break;
                        }
                    }
                }
                if (ok) {
                    maxLen = std::max(maxLen, j - i + 1);
                }
            }
        }
        return maxLen;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int longestBalanced(String s) {
        int n = s.length();
        int maxLen = 0;
        for (int i = 0; i < n; i++) {
            int[] freq = new int[26];
            for (int j = i; j < n; j++) {
                freq[s.charAt(j) - 'a']++;
                int target = -1;
                boolean ok = true;
                for (int k = 0; k < 26; k++) {
                    if (freq[k] > 0) {
                        if (target == -1) target = freq[k];
                        else if (freq[k] != target) {
                            ok = false;
                            break;
                        }
                    }
                }
                if (ok) {
                    maxLen = Math.max(maxLen, j - i + 1);
                }
            }
        }
        return maxLen;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        max_len = 0
        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                freq[ord(s[j]) - 97] += 1
                target = -1
                ok = True
                for count in freq:
                    if count > 0:
                        if target == -1:
                            target = count
                        elif count != target:
                            ok = False
                            break
                if ok:
                    curr_len = j - i + 1
                    if curr_len > max_len:
                        max_len = curr_len
        return max_len
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0
        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                freq[ord(s[j]) - 97] += 1
                target = -1
                ok = True
                for count in freq:
                    if count > 0:
                        if target == -1:
                            target = count
                        elif count != target:
                            ok = False
                            break
                if ok:
                    max_len = max(max_len, j - i + 1)
        return max_len
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <string.h>

int longestBalanced(char* s) {
    int n = strlen(s);
    int maxLen = 0;
    for (int i = 0; i < n; i++) {
        int freq[26] = {0};
        for (int j = i; j < n; j++) {
            freq[s[j] - 'a']++;
            int target = -1;
            int ok = 1;
            for (int k = 0; k < 26; k++) {
                if (freq[k] > 0) {
                    if (target == -1) target = freq[k];
                    else if (freq[k] != target) {
                        ok = 0;
                        break;
                    }
                }
            }
            if (ok) {
                int currLen = j - i + 1;
                if (currLen > maxLen) maxLen = currLen;
            }
        }
    }
    return maxLen;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int LongestBalanced(string s) {
        int n = s.Length;
        int maxLen = 0;
        for (int i = 0; i < n; i++) {
            int[] freq = new int[26];
            for (int j = i; j < n; j++) {
                freq[s[j] - 'a']++;
                int target = -1;
                bool ok = true;
                for (int k = 0; k < 26; k++) {
                    if (freq[k] > 0) {
                        if (target == -1) target = freq[k];
                        else if (freq[k] != target) {
                            ok = false;
                            break;
                        }
                    }
                }
                if (ok) {
                    int currLen = j - i + 1;
                    if (currLen > maxLen) maxLen = currLen;
                }
            }
        }
        return maxLen;
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
var longestBalanced = function(s) {
    let n = s.length;
    let maxLen = 0;
    for (let i = 0; i < n; i++) {
        let freq = new Array(26).fill(0);
        for (let j = i; j < n; j++) {
            freq[s.charCodeAt(j) - 97]++;
            let target = -1;
            let ok = true;
            for (let k = 0; k < 26; k++) {
                if (freq[k] > 0) {
                    if (target === -1) target = freq[k];
                    else if (freq[k] !== target) {
                        ok = false;
                        break;
                    }
                }
            }
            if (ok) {
                if (j - i + 1 > maxLen) maxLen = j - i + 1;
            }
        }
    }
    return maxLen;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function longestBalanced(s: string): number {
    let maxLen = 0;
    const n = s.length;
    for (let i = 0; i < n; i++) {
        const counts = new Int32Array(26);
        for (let j = i; j < n; j++) {
            counts[s.charCodeAt(j) - 97]++;
            let freq = -1;
            let isBalanced = true;
            for (let k = 0; k < 26; k++) {
                if (counts[k] > 0) {
                    if (freq === -1) {
                        freq = counts[k];
                    } else if (counts[k] !== freq) {
                        isBalanced = false;
                        break;
                    }
                }
            }
            if (isBalanced) {
                if (j - i + 1 > maxLen) {
                    maxLen = j - i + 1;
                }
            }
        }
    }
    return maxLen;
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
    function longestBalanced($s) {
        $maxLen = 0;
        $n = strlen($s);
        $aOrd = ord('a');
        for ($i = 0; $i < $n; $i++) {
            $counts = array_fill(0, 26, 0);
            for ($j = $i; $j < $n; $j++) {
                $counts[ord($s[$j]) - $aOrd]++;
                $freq = -1;
                $isBalanced = true;
                for ($k = 0; $k < 26; $k++) {
                    if ($counts[$k] > 0) {
                        if ($freq === -1) {
                            $freq = $counts[$k];
                        } else if ($counts[$k] !== $freq) {
                            $isBalanced = false;
                            break;
                        }
                    }
                }
                if ($isBalanced) {
                    $maxLen = max($maxLen, $j - $i + 1);
                }
            }
        }
        return $maxLen;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func longestBalanced(_ s: String) -> Int {
        let n = s.count
        let chars = Array(s)
        let aValue = Int(Character("a").asciiValue!)
        var maxLen = 0
        for i in 0..<n {
            var counts = [Int](repeating: 0, count: 26)
            for j in i..<n {
                let idx = Int(chars[j].asciiValue!) - aValue
                counts[idx] += 1
                var freq = -1
                var isBalanced = true
                for k in 0..<26 {
                    if counts[k] > 0 {
                        if freq == -1 {
                            freq = counts[k]
                        } else if counts[k] != freq {
                            isBalanced = false
                            break
                        }
                    }
                }
                if isBalanced {
                    maxLen = max(maxLen, j - i + 1)
                }
            }
        }
        return maxLen
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun longestBalanced(s: String): Int {
        var maxLen = 0
        val n = s.length
        for (i in 0 until n) {
            val counts = IntArray(26)
            for (j in i until n) {
                counts[s[j] - 'a']++
                var freq = -1
                var isBalanced = true
                for (k in 0 until 26) {
                    if (counts[k] > 0) {
                        if (freq == -1) {
                            freq = counts[k]
                        } else if (counts[k] != freq) {
                            isBalanced = false
                            break
                        }
                    }
                }
                if (isBalanced) {
                    maxLen = Math.max(maxLen, j - i + 1)
                }
            }
        }
        return maxLen
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int longestBalanced(String s) {
    int maxLen = 0;
    int n = s.length;
    int aCode = 'a'.codeUnitAt(0);
    for (int i = 0; i < n; i++) {
      List<int> counts = List.filled(26, 0);
      for (int j = i; j < n; j++) {
        counts[s.codeUnitAt(j) - aCode]++;
        int freq = -1;
        bool isBalanced = true;
        for (int k = 0; k < 26; k++) {
          if (counts[k] > 0) {
            if (freq == -1) {
              freq = counts[k];
            } else if (counts[k] != freq) {
              isBalanced = false;
              break;
            }
          }
        }
        if (isBalanced) {
          if (j - i + 1 > maxLen) {
            maxLen = j - i + 1;
          }
        }
      }
    }
    return maxLen;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func longestBalanced(s string) int {
    maxLen := 0
    n := len(s)
    for i := 0; i < n; i++ {
        counts := [26]int{}
        for j := i; j < n; j++ {
            counts[s[j]-'a']++
            freq := -1
            isBalanced := true
            for k := 0; k < 26; k++ {
                if counts[k] > 0 {
                    if freq == -1 {
                        freq = counts[k]
                    } else if counts[k] != freq {
                        isBalanced = false
                        break
                    }
                }
            }
            if isBalanced {
                if j-i+1 > maxLen {
                    maxLen = j - i + 1
                }
            }
        }
    }
    return maxLen
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def longest_balanced(s)
  max_len = 0
  n = s.length
  chars = s.chars
  (0...n).each do |i|
    counts = Hash.new(0)
    (i...n).each do |j|
      char = chars[j]
      counts[char] += 1
      freqs = counts.values
      first = freqs[0]
      if freqs.all? { |f| f == first }
        len = j - i + 1
        max_len = len if len > max_len
      end
    end
  end
  max_len
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def longestBalanced(s: String): Int = {
        var maxLen = 0
        val n = s.length
        for (i <- 0 until n) {
            val counts = new Array[Int](26)
            for (j <- i until n) {
                counts(s(j) - 'a') += 1
                var freq = -1
                var balanced = true
                var k = 0
                while (k < 26) {
                    if (counts(k) > 0) {
                        if (freq == -1) {
                            freq = counts(k)
                        } else if (counts(k) != freq) {
                            balanced = false
                            k = 26
                        }
                    }
                    k += 1
                }
                if (balanced) {
                    val len = j - i + 1
                    if (len > maxLen) maxLen = len
                }
            }
        }
        maxLen
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn longest_balanced(s: String) -> i32 {
        let mut max_len = 0;
        let n = s.len();
        let bytes = s.as_bytes();
        for i in 0..n {
            let mut counts = [0; 26];
            for j in i..n {
                counts[(bytes[j] - b'a') as usize] += 1;
                let mut freq = -1;
                let mut balanced = true;
                for k in 0..26 {
                    if counts[k] > 0 {
                        if freq == -1 {
                            freq = counts[k];
                        } else if counts[k] != freq {
                            balanced = false;
                            break;
                        }
                    }
                }
                if balanced {
                    max_len = max_len.max((j - i + 1) as i32);
                }
            }
        }
        max_len
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (longest-balanced s)
  (-> string? exact-integer?)
  (let ([n (string-length s)])
    (let loop-i ([i 0] [max-len 0])
      (if (= i n)
          max-len
          (let* ([counts (make-hash)]
                 [res-max (let loop-j ([j i] [cur-max max-len])
                            (if (= j n)
                                cur-max
                                (let* ([char (string-ref s j)]
                                       [cnt (hash-ref counts char 0)])
                                  (hash-set! counts char (+ cnt 1))
                                  (let* ([freqs (hash-values counts)]
                                         [first (car freqs)]
                                         [balanced (andmap (lambda (f) (= f first)) freqs)]
                                         [next-max (if balanced (max cur-max (+ (- j i) 1)) cur-max)])
                                    (loop-j (+ j 1) next-max)))))])
            (loop-i (+ i 1) res-max))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec longest_balanced(S :: unicode:unicode_binary()) -> integer().
longest_balanced(S) ->
  L = binary_to_list(S),
  find_max(L, 0).

find_max([], Max) -> Max;
find_max([_ | T] = List, Max) ->
  NewMax = check_substrings(List, Max, 1, #{}),
  find_max(T, NewMax).

check_substrings([], Max, _, _) -> Max;
check_substrings([H | T], Max, Len, Counts) ->
  NewCounts = maps:update_with(H, fun(V) -> V + 1 end, 1, Counts),
  Freqs = maps:values(NewCounts),
  [First | Rest] = Freqs,
  IsBalanced = lists:all(fun(F) -> F == First end, Rest),
  NextMax = if IsBalanced -> erlang:max(Max, Len); true -> Max end,
  check_substrings(T, NextMax, Len + 1, NewCounts).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec longest_balanced(s :: String.t) :: integer
  def longest_balanced(s) do
    chars = String.to_charlist(s)
    n = length(chars)
    Enum.reduce(0..(n - 1), 0, fn i, max_so_far ->
      sub_chars = Enum.drop(chars, i)
      {_, inner_max} = Enum.reduce(sub_chars, {%{}, max_so_far}, fn char, {counts, current_max_inner} ->
        new_counts = Map.update(counts, char, 1, fn v -> v + 1 end)
        freqs = Map.values(new_counts)
        [first | rest] = freqs
        is_balanced = Enum.all?(rest, fn f -> f == first end)
        new_max = if is_balanced do
          len = length(freqs) * first
          if len > current_max_inner, do: len, else: current_max_inner
        else
          current_max_inner
        end
        {new_counts, new_max}
      end)
      inner_max
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N^2 \cdot \Sigma) with one-paragraph explanation. The algorithm iterates through $O(N^2)$ substrings. For each substring, we update character frequencies and perform a check over the fixed-size alphabet $\Sigma = 26$. This results in a total complexity of roughly $26 \times 10^6$ operations for $N=1000$, which is well within the execution time limits.
- **Space Complexity:** O(\Sigma) with one-paragraph explanation. The space used is independent of the input string length $N$. We only store a frequency array of size $\Sigma = 26$ to track character counts for the current substring, leading to constant extra space $O(1)$ relative to the input size.
