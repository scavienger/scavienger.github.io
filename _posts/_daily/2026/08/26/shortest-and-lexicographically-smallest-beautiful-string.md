---
layout: post
title: "Shortest and Lexicographically Smallest Beautiful String"
date: 2026-08-26 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Sliding Window"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    string shortestBeautifulSubstring(string\
        \ s, int k) {\n        int n = s.length();\n        string res = \"\";\n   \
        \     int minLen = n + 1;\n\n        for (int i = 0; i < n; ++i) {\n       \
        \     int ones = 0;\n            for (int j = i; j < n; ++j) {\n           \
        \     if (s[j] == '1') ones++;\n                if (ones == k) {\n         \
        \           int len = j - i + 1;\n                    string sub = s.substr(i,\
        \ len);\n                    if (len < minLen) {\n                        minLen\
        \ = len;\n                        res = sub;\n                    } else if\
        \ (len == minLen) {\n                        if (sub < res) res = sub;\n   \
        \                 }\n                    break;\n                }\n       \
        \     }\n        }\n        return res;\n    }\n};"
      java: "class Solution {\n    public String shortestBeautifulSubstring(String s,\
        \ int k) {\n        int n = s.length();\n        String res = \"\";\n      \
        \  int minLen = n + 1;\n\n        for (int i = 0; i < n; i++) {\n          \
        \  int ones = 0;\n            for (int j = i; j < n; j++) {\n              \
        \  if (s.charAt(j) == '1') {\n                    ones++;\n                }\n\
        \                if (ones == k) {\n                    int len = j - i + 1;\n\
        \                    String sub = s.substring(i, j + 1);\n                 \
        \   if (len < minLen) {\n                        minLen = len;\n           \
        \             res = sub;\n                    } else if (len == minLen) {\n\
        \                        if (sub.compareTo(res) < 0) {\n                   \
        \         res = sub;\n                        }\n                    }\n   \
        \                 break;\n                }\n            }\n        }\n    \
        \    return res;\n    }\n}"
      python: "class Solution(object):\n    def shortestBeautifulSubstring(self, s,\
        \ k):\n        \"\"\"\n        :type s: str\n        :type k: int\n        :rtype:\
        \ str\n        \"\"\"\n        n = len(s)\n        res = \"\"\n        minLen\
        \ = n + 1\n\n        for i in range(n):\n            ones = 0\n            for\
        \ j in range(i, n):\n                if s[j] == '1':\n                    ones\
        \ += 1\n                if ones == k:\n                    length = j - i +\
        \ 1\n                    sub = s[i:j+1]\n                    if length < minLen:\n\
        \                        minLen = length\n                        res = sub\n\
        \                    elif length == minLen:\n                        if res\
        \ == \"\" or sub < res:\n                            res = sub\n           \
        \         break\n        return res"
      python3: "class Solution:\n    def shortestBeautifulSubstring(self, s: str, k:\
        \ int) -> str:\n        n = len(s)\n        res = \"\"\n        minLen = n +\
        \ 1\n\n        for i in range(n):\n            ones = 0\n            for j in\
        \ range(i, n):\n                if s[j] == '1':\n                    ones +=\
        \ 1\n                if ones == k:\n                    length = j - i + 1\n\
        \                    sub = s[i:j+1]\n                    if length < minLen:\n\
        \                        minLen = length\n                        res = sub\n\
        \                    elif length == minLen:\n                        if not\
        \ res or sub < res:\n                            res = sub\n               \
        \     break\n        return res"
      c: "char* shortestBeautifulSubstring(char* s, int k) {\n    int n = strlen(s);\n\
        \    char* res = (char*)malloc((n + 1) * sizeof(char));\n    res[0] = '\\0';\n\
        \    int minLen = n + 1;\n\n    for (int i = 0; i < n; i++) {\n        int ones\
        \ = 0;\n        for (int j = i; j < n; j++) {\n            if (s[j] == '1')\
        \ {\n                ones++;\n            }\n            if (ones == k) {\n\
        \                int len = j - i + 1;\n                if (len < minLen) {\n\
        \                    minLen = len;\n                    strncpy(res, s + i,\
        \ len);\n                    res[len] = '\\0';\n                } else if (len\
        \ == minLen) {\n                    if (strncmp(s + i, res, len) < 0) {\n  \
        \                      strncpy(res, s + i, len);\n                        res[len]\
        \ = '\\0';\n                    }\n                }\n                break;\n\
        \            }\n        }\n    }\n    return res;\n}"
      csharp: "public class Solution {\n    public string ShortestBeautifulSubstring(string\
        \ s, int k) {\n        int n = s.Length;\n        string best = \"\";\n    \
        \    for (int i = 0; i < n; i++) {\n            int count = 0;\n           \
        \ for (int j = i; j < n; j++) {\n                if (s[j] == '1') {\n      \
        \              count++;\n                }\n                if (count == k)\
        \ {\n                    string current = s.Substring(i, j - i + 1);\n     \
        \               if (best == \"\" || current.Length < best.Length || (current.Length\
        \ == best.Length && string.CompareOrdinal(current, best) < 0)) {\n         \
        \               best = current;\n                    }\n                   \
        \ break;\n                }\n            }\n        }\n        return best;\n\
        \    }\n}"
      javascript: "/**\n * @param {string} s\n * @param {number} k\n * @return {string}\n\
        \ */\nvar shortestBeautifulSubstring = function(s, k) {\n    let n = s.length;\n\
        \    let best = \"\";\n    for (let i = 0; i < n; i++) {\n        let count\
        \ = 0;\n        for (let j = i; j < n; j++) {\n            if (s[j] === '1')\
        \ {\n                count++;\n            }\n            if (count === k) {\n\
        \                let current = s.substring(i, j + 1);\n                if (best\
        \ === \"\" || current.length < best.length || (current.length === best.length\
        \ && current < best)) {\n                    best = current;\n             \
        \   }\n                break;\n            }\n        }\n    }\n    return best;\n\
        };"
      typescript: "function shortestBeautifulSubstring(s: string, k: number): string\
        \ {\n    let n: number = s.length;\n    let best: string = \"\";\n    for (let\
        \ i: number = 0; i < n; i++) {\n        let count: number = 0;\n        for\
        \ (let j: number = i; j < n; j++) {\n            if (s[j] === '1') {\n     \
        \           count++;\n            }\n            if (count === k) {\n      \
        \          let current: string = s.substring(i, j + 1);\n                if\
        \ (best === \"\" || current.length < best.length || (current.length === best.length\
        \ && current < best)) {\n                    best = current;\n             \
        \   }\n                break;\n            }\n        }\n    }\n    return best;\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @param Integer\
        \ $k\n     * @return String\n     */\n    function shortestBeautifulSubstring($s,\
        \ $k) {\n        $n = strlen($s);\n        $best = \"\";\n        for ($i =\
        \ 0; $i < $n; $i++) {\n            $count = 0;\n            for ($j = $i; $j\
        \ < $n; $j++) {\n                if ($s[$j] == '1') {\n                    $count++;\n\
        \                }\n                if ($count == $k) {\n                  \
        \  $current = substr($s, $i, $j - $i + 1);\n                    if ($best ===\
        \ \"\" || strlen($current) < strlen($best) || (strlen($current) == strlen($best)\
        \ && strcmp($current, $best) < 0)) {\n                        $best = $current;\n\
        \                    }\n                    break;\n                }\n    \
        \        }\n        }\n        return $best;\n    }\n}"
      swift: "class Solution {\n    func shortestBeautifulSubstring(_ s: String, _ k:\
        \ Int) -> String {\n        let n = s.count\n        let sChars = Array(s)\n\
        \        var best = \"\"\n        for i in 0..<n {\n            var count =\
        \ 0\n            for j in i..<n {\n                if sChars[j] == \"1\" {\n\
        \                    count += 1\n                }\n                if count\
        \ == k {\n                    let current = String(sChars[i...j])\n        \
        \            if best == \"\" || current.count < best.count || (current.count\
        \ == best.count && current < best) {\n                        best = current\n\
        \                    }\n                    break\n                }\n     \
        \       }\n        }\n        return best\n    }\n}"
      kotlin: "class Solution {\n    fun shortestBeautifulSubstring(s: String, k: Int):\
        \ String {\n        var best = \"\"\n        val n = s.length\n        for (i\
        \ in 0 until n) {\n            var count = 0\n            for (j in i until\
        \ n) {\n                if (s[j] == '1') {\n                    count++\n  \
        \              }\n                if (count == k) {\n                    val\
        \ sub = s.substring(i, j + 1)\n                    if (best == \"\" || sub.length\
        \ < best.length || (sub.length == best.length && sub < best)) {\n          \
        \              best = sub\n                    }\n                    break\n\
        \                }\n            }\n        }\n        return best\n    }\n}"
      dart: "class Solution {\n  String shortestBeautifulSubstring(String s, int k)\
        \ {\n    String best = \"\";\n    int n = s.length;\n    for (int i = 0; i <\
        \ n; i++) {\n      int count = 0;\n      for (int j = i; j < n; j++) {\n   \
        \     if (s[j] == '1') {\n          count++;\n        }\n        if (count ==\
        \ k) {\n          String sub = s.substring(i, j + 1);\n          if (best ==\
        \ \"\" || sub.length < best.length || (sub.length == best.length && sub.compareTo(best)\
        \ < 0)) {\n            best = sub;\n          }\n          break;\n        }\n\
        \      }\n    }\n    return best;\n  }\n}"
      go: "func shortestBeautifulSubstring(s string, k int) string {\n    best := \"\
        \"\n    n := len(s)\n    for i := 0; i < n; i++ {\n        count := 0\n    \
        \    for j := i; j < n; j++ {\n            if s[j] == '1' {\n              \
        \  count++\n            }\n            if count == k {\n                sub\
        \ := s[i : j+1]\n                if best == \"\" || len(sub) < len(best) ||\
        \ (len(sub) == len(best) && sub < best) {\n                    best = sub\n\
        \                }\n                break\n            }\n        }\n    }\n\
        \    return best\n}"
      ruby: "# @param {String} s\n# @param {Integer} k\n# @return {String}\ndef shortest_beautiful_substring(s,\
        \ k)\n  best = \"\"\n  n = s.length\n  (0...n).each do |i|\n    count = 0\n\
        \    (i...n).each do |j|\n      count += 1 if s[j] == '1'\n      if count ==\
        \ k\n        sub = s[i..j]\n        if best == \"\" || sub.length < best.length\
        \ || (sub.length == best.length && sub < best)\n          best = sub\n     \
        \   end\n        break\n      end\n    end\n  end\n  best\nend"
      scala: "object Solution {\n    def shortestBeautifulSubstring(s: String, k: Int):\
        \ String = {\n        var best = \"\"\n        val n = s.length\n        for\
        \ (i <- 0 until n) {\n            var count = 0\n            var j = i\n   \
        \         var found = false\n            while (j < n && !found) {\n       \
        \         if (s(j) == '1') {\n                    count += 1\n             \
        \   }\n                if (count == k) {\n                    val sub = s.substring(i,\
        \ j + 1)\n                    if (best == \"\" || sub.length < best.length ||\
        \ (sub.length == best.length && sub.compareTo(best) < 0)) {\n              \
        \          best = sub\n                    }\n                    found = true\n\
        \                }\n                j += 1\n            }\n        }\n     \
        \   best\n    }\n}"
      rust: "impl Solution {\n    pub fn shortest_beautiful_substring(s: String, k:\
        \ i32) -> String {\n        let n = s.len();\n        let mut best = String::new();\n\
        \        let bytes = s.as_bytes();\n\n        for i in 0..n {\n            let\
        \ mut count = 0;\n            for j in i..n {\n                if bytes[j] ==\
        \ b'1' {\n                    count += 1;\n                }\n\n           \
        \     if count == k {\n                    let sub = &s[i..=j];\n          \
        \          if best.is_empty() || sub.len() < best.len() || (sub.len() == best.len()\
        \ && sub < &best) {\n                        best = sub.to_string();\n     \
        \               }\n                    break;\n                }\n         \
        \   }\n        }\n        best\n    }\n}"
      racket: "(define/contract (shortest-beautiful-substring s k)\n  (-> string? exact-integer?\
        \ string?)\n  (let* ([n (string-length s)]\n         [candidates\n         \
        \ (for*/list ([i (in-range n)]\n                      [j (in-range i n)]\n \
        \                     #:let [sub (substring s i (+ j 1))]\n                \
        \      #:let [c-ones (for/sum ([c (in-string sub)])\n                      \
        \                (if (char=? c #\\1) 1 0))]\n                      #:when (=\
        \ c-ones k))\n            sub)])\n    (if (null? candidates)\n        \"\"\n\
        \        (car (sort candidates\n                   (lambda (a b)\n         \
        \            (if (= (string-length a) (string-length b))\n                 \
        \        (string<? a b)\n                         (< (string-length a) (string-length\
        \ b)))))))))"
      erlang: "-spec shortest_beautiful_substring(S :: unicode:unicode_binary(), K ::\
        \ integer()) -> unicode:unicode_binary().\nshortest_beautiful_substring(S, K)\
        \ ->\n    List = binary_to_list(S),\n    N = length(List),\n    Beautiful =\
        \ [Sub || I <- lists:seq(1, N),\n                        J <- lists:seq(I, N),\n\
        \                        Sub <- [lists:sublist(List, I, J - I + 1)],\n     \
        \                   length([C || C <- Sub, C == $1]) == K],\n    case Beautiful\
        \ of\n        [] -> <<>>;\n        _ ->\n            Sorted = lists:sort(fun(A,\
        \ B) ->\n                LenA = length(A),\n                LenB = length(B),\n\
        \                if\n                    LenA < LenB -> true;\n            \
        \        LenA > LenB -> false;\n                    true -> A =< B\n       \
        \         end\n            end, Beautiful),\n            list_to_binary(hd(Sorted))\n\
        \    end."
      elixir: "defmodule Solution do\n  @spec shortest_beautiful_substring(s :: String.t,\
        \ k :: integer) :: String.t\n  def shortest_beautiful_substring(s, k) do\n \
        \   n = String.length(s)\n\n    beautiful = for i <- 0..(n-1), j <- i..(n-1)\
        \ do\n      String.slice(s, i..j)\n    end\n    |> Enum.filter(fn sub -> count_ones(sub)\
        \ == k end)\n\n    case beautiful do\n      [] -> \"\"\n      _ -> Enum.min_by(beautiful,\
        \ fn sub -> {String.length(sub), sub} end)\n    end\n  end\n\n  defp count_ones(s)\
        \ do\n    s \n    |> String.to_charlist() \n    |> Enum.count(fn c -> c == ?1\
        \ end)\n  end\nend"
    approach: 'The problem asks for the shortest beautiful substring containing exactly
      $k$ ones, and among those of the same shortest length, the lexicographically smallest
      one. Given the small constraint on the string length ($n \le 100$), we can efficiently
      solve this by iterating through all possible substrings $(i, j)$ of the string
      $s$. For each substring, we count the number of ''1'' characters it contains.
      If the count matches $k$, we have found a ''beautiful'' substring.


      To determine the best beautiful substring, we maintain a variable for the minimum
      length found so far and a string to store the current best result. When a substring
      of length $L$ with exactly $k$ ones is found, we compare $L$ to the current minimum
      length. If $L$ is smaller, we update both the minimum length and the result string.
      If $L$ is equal to the minimum length, we perform a lexicographical comparison
      and update the result string if the new substring is smaller. This brute-force
      approach works in $O(n^3)$ time, which is well within the limits for $n=100$.'
    time_complexity: O(n^3) where $n$ is the length of the input string $s$. There are
      $O(n^2)$ possible substrings, and for each substring, we perform a count of characters
      and a string comparison, both of which take $O(n)$ time.
    space_complexity: O(n) where $n$ is the length of the input string $s$. We need
      to store the current best beautiful substring and potentially temporary substrings
      for comparison, all of which are at most $n$ characters long.
    elapsed_time: 210.5187122821808
    model: gemini-3-flash-preview
    generated_at: '2026-08-26 00:54:31 '
---

## Problem #2904: Shortest and Lexicographically Smallest Beautiful String

**Difficulty:** Medium

**Topics:** String, Sliding Window

## Problem Description

<p>You are given a binary string <code>s</code> and a positive integer <code>k</code>.</p>

<p>A substring of <code>s</code> is <strong>beautiful</strong> if the number of <code>1</code>&#39;s in it is exactly <code>k</code>.</p>

<p>Let <code>len</code> be the length of the <strong>shortest</strong> beautiful substring.</p>

<p>Return <em>the lexicographically <strong>smallest</strong> beautiful substring of string </em><code>s</code><em> with length equal to </em><code>len</code>. If <code>s</code> doesn&#39;t contain a beautiful substring, return <em>an <strong>empty</strong> string</em>.</p>

<p>A string <code>a</code> is lexicographically <strong>larger</strong> than a string <code>b</code> (of the same length) if in the first position where <code>a</code> and <code>b</code> differ, <code>a</code> has a character strictly larger than the corresponding character in <code>b</code>.</p>

<ul>
	<li>For example, <code>&quot;abcd&quot;</code> is lexicographically larger than <code>&quot;abcc&quot;</code> because the first position they differ is at the fourth character, and <code>d</code> is greater than <code>c</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;100011001&quot;, k = 3
<strong>Output:</strong> &quot;11001&quot;
<strong>Explanation:</strong> There are 7 beautiful substrings in this example:
1. The substring &quot;<u>100011</u>001&quot;.
2. The substring &quot;<u>1000110</u>01&quot;.
3. The substring &quot;<u>10001100</u>1&quot;.
4. The substring &quot;1<u>00011001</u>&quot;.
5. The substring &quot;10<u>0011001</u>&quot;.
6. The substring &quot;100<u>011001</u>&quot;.
7. The substring &quot;1000<u>11001</u>&quot;.
The length of the shortest beautiful substring is 5.
The lexicographically smallest beautiful substring with length 5 is the substring &quot;11001&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;1011&quot;, k = 2
<strong>Output:</strong> &quot;11&quot;
<strong>Explanation:</strong> There are 3 beautiful substrings in this example:
1. The substring &quot;<u>101</u>1&quot;.
2. The substring &quot;1<u>011</u>&quot;.
3. The substring &quot;10<u>11</u>&quot;.
The length of the shortest beautiful substring is 2.
The lexicographically smallest beautiful substring with length 2 is the substring &quot;11&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;000&quot;, k = 1
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> There are no beautiful substrings in this example.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= s.length</code></li>
</ul>


## Hints

1. Notice that if we consider that index `i` is the leftmost index of a beautiful substring, it has only one candidate `j`, such that `s[i:j]` is beautiful and shortest too.

2. We can iterate over all possibilities of leftmost index `i` take `s[i:j]` and compare with the shortest and the lexicographically smallest beautiful string we could get before index `i`.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the shortest beautiful substring containing exactly $k$ ones, and among those of the same shortest length, the lexicographically smallest one. Given the small constraint on the string length ($n \le 100$), we can efficiently solve this by iterating through all possible substrings $(i, j)$ of the string $s$. For each substring, we count the number of '1' characters it contains. If the count matches $k$, we have found a 'beautiful' substring.

To determine the best beautiful substring, we maintain a variable for the minimum length found so far and a string to store the current best result. When a substring of length $L$ with exactly $k$ ones is found, we compare $L$ to the current minimum length. If $L$ is smaller, we update both the minimum length and the result string. If $L$ is equal to the minimum length, we perform a lexicographical comparison and update the result string if the new substring is smaller. This brute-force approach works in $O(n^3)$ time, which is well within the limits for $n=100$.

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
    string shortestBeautifulSubstring(string s, int k) {
        int n = s.length();
        string res = "";
        int minLen = n + 1;

        for (int i = 0; i < n; ++i) {
            int ones = 0;
            for (int j = i; j < n; ++j) {
                if (s[j] == '1') ones++;
                if (ones == k) {
                    int len = j - i + 1;
                    string sub = s.substr(i, len);
                    if (len < minLen) {
                        minLen = len;
                        res = sub;
                    } else if (len == minLen) {
                        if (sub < res) res = sub;
                    }
                    break;
                }
            }
        }
        return res;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public String shortestBeautifulSubstring(String s, int k) {
        int n = s.length();
        String res = "";
        int minLen = n + 1;

        for (int i = 0; i < n; i++) {
            int ones = 0;
            for (int j = i; j < n; j++) {
                if (s.charAt(j) == '1') {
                    ones++;
                }
                if (ones == k) {
                    int len = j - i + 1;
                    String sub = s.substring(i, j + 1);
                    if (len < minLen) {
                        minLen = len;
                        res = sub;
                    } else if (len == minLen) {
                        if (sub.compareTo(res) < 0) {
                            res = sub;
                        }
                    }
                    break;
                }
            }
        }
        return res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        res = ""
        minLen = n + 1

        for i in range(n):
            ones = 0
            for j in range(i, n):
                if s[j] == '1':
                    ones += 1
                if ones == k:
                    length = j - i + 1
                    sub = s[i:j+1]
                    if length < minLen:
                        minLen = length
                        res = sub
                    elif length == minLen:
                        if res == "" or sub < res:
                            res = sub
                    break
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        res = ""
        minLen = n + 1

        for i in range(n):
            ones = 0
            for j in range(i, n):
                if s[j] == '1':
                    ones += 1
                if ones == k:
                    length = j - i + 1
                    sub = s[i:j+1]
                    if length < minLen:
                        minLen = length
                        res = sub
                    elif length == minLen:
                        if not res or sub < res:
                            res = sub
                    break
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
char* shortestBeautifulSubstring(char* s, int k) {
    int n = strlen(s);
    char* res = (char*)malloc((n + 1) * sizeof(char));
    res[0] = '\0';
    int minLen = n + 1;

    for (int i = 0; i < n; i++) {
        int ones = 0;
        for (int j = i; j < n; j++) {
            if (s[j] == '1') {
                ones++;
            }
            if (ones == k) {
                int len = j - i + 1;
                if (len < minLen) {
                    minLen = len;
                    strncpy(res, s + i, len);
                    res[len] = '\0';
                } else if (len == minLen) {
                    if (strncmp(s + i, res, len) < 0) {
                        strncpy(res, s + i, len);
                        res[len] = '\0';
                    }
                }
                break;
            }
        }
    }
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public string ShortestBeautifulSubstring(string s, int k) {
        int n = s.Length;
        string best = "";
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = i; j < n; j++) {
                if (s[j] == '1') {
                    count++;
                }
                if (count == k) {
                    string current = s.Substring(i, j - i + 1);
                    if (best == "" || current.Length < best.Length || (current.Length == best.Length && string.CompareOrdinal(current, best) < 0)) {
                        best = current;
                    }
                    break;
                }
            }
        }
        return best;
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
 * @param {number} k
 * @return {string}
 */
var shortestBeautifulSubstring = function(s, k) {
    let n = s.length;
    let best = "";
    for (let i = 0; i < n; i++) {
        let count = 0;
        for (let j = i; j < n; j++) {
            if (s[j] === '1') {
                count++;
            }
            if (count === k) {
                let current = s.substring(i, j + 1);
                if (best === "" || current.length < best.length || (current.length === best.length && current < best)) {
                    best = current;
                }
                break;
            }
        }
    }
    return best;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function shortestBeautifulSubstring(s: string, k: number): string {
    let n: number = s.length;
    let best: string = "";
    for (let i: number = 0; i < n; i++) {
        let count: number = 0;
        for (let j: number = i; j < n; j++) {
            if (s[j] === '1') {
                count++;
            }
            if (count === k) {
                let current: string = s.substring(i, j + 1);
                if (best === "" || current.length < best.length || (current.length === best.length && current < best)) {
                    best = current;
                }
                break;
            }
        }
    }
    return best;
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
     * @param Integer $k
     * @return String
     */
    function shortestBeautifulSubstring($s, $k) {
        $n = strlen($s);
        $best = "";
        for ($i = 0; $i < $n; $i++) {
            $count = 0;
            for ($j = $i; $j < $n; $j++) {
                if ($s[$j] == '1') {
                    $count++;
                }
                if ($count == $k) {
                    $current = substr($s, $i, $j - $i + 1);
                    if ($best === "" || strlen($current) < strlen($best) || (strlen($current) == strlen($best) && strcmp($current, $best) < 0)) {
                        $best = $current;
                    }
                    break;
                }
            }
        }
        return $best;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func shortestBeautifulSubstring(_ s: String, _ k: Int) -> String {
        let n = s.count
        let sChars = Array(s)
        var best = ""
        for i in 0..<n {
            var count = 0
            for j in i..<n {
                if sChars[j] == "1" {
                    count += 1
                }
                if count == k {
                    let current = String(sChars[i...j])
                    if best == "" || current.count < best.count || (current.count == best.count && current < best) {
                        best = current
                    }
                    break
                }
            }
        }
        return best
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun shortestBeautifulSubstring(s: String, k: Int): String {
        var best = ""
        val n = s.length
        for (i in 0 until n) {
            var count = 0
            for (j in i until n) {
                if (s[j] == '1') {
                    count++
                }
                if (count == k) {
                    val sub = s.substring(i, j + 1)
                    if (best == "" || sub.length < best.length || (sub.length == best.length && sub < best)) {
                        best = sub
                    }
                    break
                }
            }
        }
        return best
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  String shortestBeautifulSubstring(String s, int k) {
    String best = "";
    int n = s.length;
    for (int i = 0; i < n; i++) {
      int count = 0;
      for (int j = i; j < n; j++) {
        if (s[j] == '1') {
          count++;
        }
        if (count == k) {
          String sub = s.substring(i, j + 1);
          if (best == "" || sub.length < best.length || (sub.length == best.length && sub.compareTo(best) < 0)) {
            best = sub;
          }
          break;
        }
      }
    }
    return best;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func shortestBeautifulSubstring(s string, k int) string {
    best := ""
    n := len(s)
    for i := 0; i < n; i++ {
        count := 0
        for j := i; j < n; j++ {
            if s[j] == '1' {
                count++
            }
            if count == k {
                sub := s[i : j+1]
                if best == "" || len(sub) < len(best) || (len(sub) == len(best) && sub < best) {
                    best = sub
                }
                break
            }
        }
    }
    return best
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @param {Integer} k
# @return {String}
def shortest_beautiful_substring(s, k)
  best = ""
  n = s.length
  (0...n).each do |i|
    count = 0
    (i...n).each do |j|
      count += 1 if s[j] == '1'
      if count == k
        sub = s[i..j]
        if best == "" || sub.length < best.length || (sub.length == best.length && sub < best)
          best = sub
        end
        break
      end
    end
  end
  best
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def shortestBeautifulSubstring(s: String, k: Int): String = {
        var best = ""
        val n = s.length
        for (i <- 0 until n) {
            var count = 0
            var j = i
            var found = false
            while (j < n && !found) {
                if (s(j) == '1') {
                    count += 1
                }
                if (count == k) {
                    val sub = s.substring(i, j + 1)
                    if (best == "" || sub.length < best.length || (sub.length == best.length && sub.compareTo(best) < 0)) {
                        best = sub
                    }
                    found = true
                }
                j += 1
            }
        }
        best
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn shortest_beautiful_substring(s: String, k: i32) -> String {
        let n = s.len();
        let mut best = String::new();
        let bytes = s.as_bytes();

        for i in 0..n {
            let mut count = 0;
            for j in i..n {
                if bytes[j] == b'1' {
                    count += 1;
                }

                if count == k {
                    let sub = &s[i..=j];
                    if best.is_empty() || sub.len() < best.len() || (sub.len() == best.len() && sub < &best) {
                        best = sub.to_string();
                    }
                    break;
                }
            }
        }
        best
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (shortest-beautiful-substring s k)
  (-> string? exact-integer? string?)
  (let* ([n (string-length s)]
         [candidates
          (for*/list ([i (in-range n)]
                      [j (in-range i n)]
                      #:let [sub (substring s i (+ j 1))]
                      #:let [c-ones (for/sum ([c (in-string sub)])
                                      (if (char=? c #\1) 1 0))]
                      #:when (= c-ones k))
            sub)])
    (if (null? candidates)
        ""
        (car (sort candidates
                   (lambda (a b)
                     (if (= (string-length a) (string-length b))
                         (string<? a b)
                         (< (string-length a) (string-length b)))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec shortest_beautiful_substring(S :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
shortest_beautiful_substring(S, K) ->
    List = binary_to_list(S),
    N = length(List),
    Beautiful = [Sub || I <- lists:seq(1, N),
                        J <- lists:seq(I, N),
                        Sub <- [lists:sublist(List, I, J - I + 1)],
                        length([C || C <- Sub, C == $1]) == K],
    case Beautiful of
        [] -> <<>>;
        _ ->
            Sorted = lists:sort(fun(A, B) ->
                LenA = length(A),
                LenB = length(B),
                if
                    LenA < LenB -> true;
                    LenA > LenB -> false;
                    true -> A =< B
                end
            end, Beautiful),
            list_to_binary(hd(Sorted))
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec shortest_beautiful_substring(s :: String.t, k :: integer) :: String.t
  def shortest_beautiful_substring(s, k) do
    n = String.length(s)

    beautiful = for i <- 0..(n-1), j <- i..(n-1) do
      String.slice(s, i..j)
    end
    |> Enum.filter(fn sub -> count_ones(sub) == k end)

    case beautiful do
      [] -> ""
      _ -> Enum.min_by(beautiful, fn sub -> {String.length(sub), sub} end)
    end
  end

  defp count_ones(s) do
    s 
    |> String.to_charlist() 
    |> Enum.count(fn c -> c == ?1 end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n^3) where $n$ is the length of the input string $s$. There are $O(n^2)$ possible substrings, and for each substring, we perform a count of characters and a string comparison, both of which take $O(n)$ time.
- **Space Complexity:** O(n) where $n$ is the length of the input string $s$. We need to store the current best beautiful substring and potentially temporary substrings for comparison, all of which are at most $n$ characters long.
