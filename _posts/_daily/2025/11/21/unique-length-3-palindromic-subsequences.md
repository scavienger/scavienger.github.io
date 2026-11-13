---
layout: post
title: "Unique Length-3 Palindromic Subsequences"
date: 2025-11-21 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Hash Table", "String", "Bit Manipulation", "Prefix Sum"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int countPalindromicSubsequence(string s)\
        \ {\n        int n = s.size();\n        int answer = 0;\n        for (char outer\
        \ = 'a'; outer <= 'z'; ++outer) {\n            int first = -1;\n           \
        \ int last = -1;\n            for (int i = 0; i < n; ++i) {\n              \
        \  if (s[i] == outer) {\n                    if (first == -1) first = i;\n \
        \                   last = i;\n                }\n            }\n          \
        \  if (last - first <= 1) continue;\n            bool seen[26] = {};\n     \
        \       for (int i = first + 1; i < last; ++i) {\n                seen[s[i]\
        \ - 'a'] = true;\n            }\n            for (bool present : seen) {\n \
        \               if (present) ++answer;\n            }\n        }\n        return\
        \ answer;\n    }\n};"
      java: "class Solution {\n    public int countPalindromicSubsequence(String s)\
        \ {\n        int n = s.length();\n        int answer = 0;\n        for (char\
        \ outer = 'a'; outer <= 'z'; outer++) {\n            int first = -1;\n     \
        \       int last = -1;\n            for (int i = 0; i < n; i++) {\n        \
        \        if (s.charAt(i) == outer) {\n                    if (first == -1) first\
        \ = i;\n                    last = i;\n                }\n            }\n  \
        \          if (last - first <= 1) continue;\n            boolean[] seen = new\
        \ boolean[26];\n            for (int i = first + 1; i < last; i++) {\n     \
        \           seen[s.charAt(i) - 'a'] = true;\n            }\n            for\
        \ (boolean present : seen) {\n                if (present) answer++;\n     \
        \       }\n        }\n        return answer;\n    }\n}"
      python: "class Solution(object):\n    def countPalindromicSubsequence(self, s):\n\
        \        \"\"\"\n        :type s: str\n        :rtype: int\n        \"\"\"\n\
        \        answer = 0\n        for outer in \"abcdefghijklmnopqrstuvwxyz\":\n\
        \            first = s.find(outer)\n            last = s.rfind(outer)\n    \
        \        if last - first <= 1:\n                continue\n            answer\
        \ += len(set(s[first + 1:last]))\n        return answer"
      python3: "class Solution:\n    def countPalindromicSubsequence(self, s: str) ->\
        \ int:\n        answer = 0\n        for outer in \"abcdefghijklmnopqrstuvwxyz\"\
        :\n            first = s.find(outer)\n            last = s.rfind(outer)\n  \
        \          if last - first <= 1:\n                continue\n            answer\
        \ += len(set(s[first + 1:last]))\n        return answer"
      c: "int countPalindromicSubsequence(char* s) {\n    int n = 0;\n    while (s[n]\
        \ != '\\0') {\n        n++;\n    }\n    int answer = 0;\n    for (char outer\
        \ = 'a'; outer <= 'z'; outer++) {\n        int first = -1;\n        int last\
        \ = -1;\n        for (int i = 0; i < n; i++) {\n            if (s[i] == outer)\
        \ {\n                if (first == -1) first = i;\n                last = i;\n\
        \            }\n        }\n        if (last - first <= 1) continue;\n      \
        \  int seen[26] = {0};\n        for (int i = first + 1; i < last; i++) {\n \
        \           seen[s[i] - 'a'] = 1;\n        }\n        for (int i = 0; i < 26;\
        \ i++) {\n            answer += seen[i];\n        }\n    }\n    return answer;\n\
        }"
      csharp: "public class Solution {\n    public int CountPalindromicSubsequence(string\
        \ s) {\n        int answer = 0;\n        for (char outer = 'a'; outer <= 'z';\
        \ outer++) {\n            int first = s.IndexOf(outer);\n            int last\
        \ = s.LastIndexOf(outer);\n            if (last - first <= 1) {\n          \
        \      continue;\n            }\n\n            var middleCharacters = new HashSet<char>();\n\
        \            for (int i = first + 1; i < last; i++) {\n                middleCharacters.Add(s[i]);\n\
        \            }\n            answer += middleCharacters.Count;\n        }\n \
        \       return answer;\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {number}\n */\nvar countPalindromicSubsequence\
        \ = function(s) {\n    let answer = 0;\n    for (let code = 97; code <= 122;\
        \ code++) {\n        const outer = String.fromCharCode(code);\n        const\
        \ first = s.indexOf(outer);\n        const last = s.lastIndexOf(outer);\n  \
        \      if (last - first <= 1) {\n            continue;\n        }\n\n      \
        \  const middleCharacters = new Set(s.slice(first + 1, last));\n        answer\
        \ += middleCharacters.size;\n    }\n    return answer;\n};"
      typescript: "function countPalindromicSubsequence(s: string): number {\n    let\
        \ answer = 0;\n    for (let code = 97; code <= 122; code++) {\n        const\
        \ outer = String.fromCharCode(code);\n        const first = s.indexOf(outer);\n\
        \        const last = s.lastIndexOf(outer);\n        if (last - first <= 1)\
        \ {\n            continue;\n        }\n\n        const middleCharacters = new\
        \ Set(s.slice(first + 1, last));\n        answer += middleCharacters.size;\n\
        \    }\n    return answer;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return Integer\n\
        \     */\n    function countPalindromicSubsequence($s) {\n        $answer =\
        \ 0;\n        for ($code = 97; $code <= 122; $code++) {\n            $outer\
        \ = chr($code);\n            $first = strpos($s, $outer);\n            $last\
        \ = strrpos($s, $outer);\n            if ($last - $first <= 1) {\n         \
        \       continue;\n            }\n\n            $middleCharacters = [];\n  \
        \          for ($i = $first + 1; $i < $last; $i++) {\n                $middleCharacters[$s[$i]]\
        \ = true;\n            }\n            $answer += count($middleCharacters);\n\
        \        }\n        return $answer;\n    }\n}"
      swift: "class Solution {\n    func countPalindromicSubsequence(_ s: String) ->\
        \ Int {\n        let characters = Array(s)\n        var answer = 0\n       \
        \ for code in 97...122 {\n            let outer = Character(UnicodeScalar(code)!)\n\
        \            guard let first = characters.firstIndex(of: outer),\n         \
        \         let last = characters.lastIndex(of: outer),\n                  last\
        \ - first > 1 else {\n                continue\n            }\n\n          \
        \  var middleCharacters = Set<Character>()\n            for index in (first\
        \ + 1)..<last {\n                middleCharacters.insert(characters[index])\n\
        \            }\n            answer += middleCharacters.count\n        }\n  \
        \      return answer\n    }\n}"
      kotlin: "class Solution {\n    fun countPalindromicSubsequence(s: String): Int\
        \ {\n        var answer = 0\n        for (outer in 'a'..'z') {\n           \
        \ val first = s.indexOf(outer)\n            val last = s.lastIndexOf(outer)\n\
        \            if (last - first <= 1) continue\n            val middleCharacters\
        \ = mutableSetOf<Char>()\n            for (i in first + 1 until last) {\n  \
        \              middleCharacters.add(s[i])\n            }\n            answer\
        \ += middleCharacters.size\n        }\n        return answer\n    }\n}"
      dart: "class Solution {\n  int countPalindromicSubsequence(String s) {\n    var\
        \ answer = 0;\n    for (var code = 'a'.codeUnitAt(0); code <= 'z'.codeUnitAt(0);\
        \ code++) {\n      final outer = String.fromCharCode(code);\n      final first\
        \ = s.indexOf(outer);\n      final last = s.lastIndexOf(outer);\n      if (last\
        \ - first <= 1) continue;\n      final middleCharacters = <String>{};\n    \
        \  for (var i = first + 1; i < last; i++) {\n        middleCharacters.add(s[i]);\n\
        \      }\n      answer += middleCharacters.length;\n    }\n    return answer;\n\
        \  }\n}"
      go: "func countPalindromicSubsequence(s string) int {\n\tanswer := 0\n\tfor outer\
        \ := byte('a'); outer <= byte('z'); outer++ {\n\t\tfirst := -1\n\t\tlast :=\
        \ -1\n\t\tfor i := 0; i < len(s); i++ {\n\t\t\tif s[i] == outer {\n\t\t\t\t\
        if first == -1 {\n\t\t\t\t\tfirst = i\n\t\t\t\t}\n\t\t\t\tlast = i\n\t\t\t}\n\
        \t\t}\n\t\tif last-first <= 1 {\n\t\t\tcontinue\n\t\t}\n\t\tvar seen [26]bool\n\
        \t\tcount := 0\n\t\tfor i := first + 1; i < last; i++ {\n\t\t\tindex := s[i]\
        \ - 'a'\n\t\t\tif !seen[index] {\n\t\t\t\tseen[index] = true\n\t\t\t\tcount++\n\
        \t\t\t}\n\t\t}\n\t\tanswer += count\n\t}\n\treturn answer\n}"
      ruby: "# @param {String} s\n# @return {Integer}\ndef count_palindromic_subsequence(s)\n\
        \  answer = 0\n  ('a'..'z').each do |outer|\n    first = s.index(outer)\n  \
        \  last = s.rindex(outer)\n    next if last - first <= 1\n\n    answer += s[(first\
        \ + 1)...last].chars.uniq.length\n  end\n  answer\nend"
      scala: "object Solution {\n    def countPalindromicSubsequence(s: String): Int\
        \ = {\n        var answer = 0\n        for (outer <- 'a' to 'z') {\n       \
        \     val first = s.indexOf(outer)\n            val last = s.lastIndexOf(outer)\n\
        \            if (last - first > 1) {\n                answer += s.substring(first\
        \ + 1, last).distinct.length\n            }\n        }\n        answer\n   \
        \ }\n}"
      rust: "impl Solution {\n    pub fn count_palindromic_subsequence(s: String) ->\
        \ i32 {\n        let bytes = s.as_bytes();\n        let mut answer = 0;\n\n\
        \        for outer in b'a'..=b'z' {\n            let first = bytes.iter().position(|&c|\
        \ c == outer);\n            let last = bytes.iter().rposition(|&c| c == outer);\n\
        \n            if let (Some(first), Some(last)) = (first, last) {\n         \
        \       if last > first + 1 {\n                    let mut seen = [false; 26];\n\
        \                    for &middle in &bytes[first + 1..last] {\n            \
        \            seen[(middle - b'a') as usize] = true;\n                    }\n\
        \                    answer += seen.iter().filter(|&&present| present).count()\
        \ as i32;\n                }\n            }\n        }\n\n        answer\n \
        \   }\n}"
      racket: "(define/contract (count-palindromic-subsequence s)\n  (-> string? exact-integer?)\n\
        \  (define chars (list->vector (string->list s)))\n  (define n (vector-length\
        \ chars))\n  (for/sum ([outer (in-range 26)])\n    (define letter (integer->char\
        \ (+ (char->integer #\\a) outer)))\n    (define first\n      (for/first ([i\
        \ (in-range n)]\n                  #:when (char=? (vector-ref chars i) letter))\n\
        \        i))\n    (define last\n      (for/first ([i (in-range (sub1 n) -1 -1)]\n\
        \                  #:when (char=? (vector-ref chars i) letter))\n        i))\n\
        \    (if (and first last (> (- last first) 1))\n        (let ([seen (make-vector\
        \ 26 #f)])\n          (for ([i (in-range (add1 first) last)])\n            (define\
        \ middle (vector-ref chars i))\n            (vector-set! seen (- (char->integer\
        \ middle) (char->integer #\\a)) #t))\n          (for/sum ([present (in-vector\
        \ seen)])\n            (if present 1 0)))\n        0)))"
      erlang: "-spec count_palindromic_subsequence(S :: unicode:unicode_binary()) ->\
        \ integer().\ncount_palindromic_subsequence(S) ->\n  Chars = unicode:characters_to_list(S),\n\
        \  lists:sum([\n    case find_bounds(Chars, $a + Offset) of\n      {First, Last}\
        \ when Last > First + 1 ->\n        length(lists:usort(lists:sublist(Chars,\
        \ First + 2, Last - First - 1)));\n      _ ->\n        0\n    end\n    || Offset\
        \ <- lists:seq(0, 25)\n  ]).\n\nfind_bounds(Chars, Letter) ->\n  find_bounds(Chars,\
        \ Letter, 1, none, none).\n\nfind_bounds([], _Letter, _Index, First, Last) ->\n\
        \  case {First, Last} of\n    {none, _} -> none;\n    {F, L} -> {F, L}\n  end;\n\
        find_bounds([Letter | Rest], Letter, Index, none, _Last) ->\n  find_bounds(Rest,\
        \ Letter, Index + 1, Index, Index);\nfind_bounds([Letter | Rest], Letter, Index,\
        \ First, _Last) ->\n  find_bounds(Rest, Letter, Index + 1, First, Index);\n\
        find_bounds([_ | Rest], Letter, Index, First, Last) ->\n  find_bounds(Rest,\
        \ Letter, Index + 1, First, Last)."
      elixir: "defmodule Solution do\n  @spec count_palindromic_subsequence(s :: String.t)\
        \ :: integer\n  def count_palindromic_subsequence(s) do\n    chars = String.to_charlist(s)\n\
        \n    Enum.reduce(?a..?z, 0, fn outer, answer ->\n      first = Enum.find_index(chars,\
        \ &(&1 == outer))\n      last = Enum.find_index(Enum.reverse(chars), &(&1 ==\
        \ outer))\n\n      case {first, last} do\n        {nil, _} ->\n          answer\n\
        \n        {_, nil} ->\n          answer\n\n        {first, reversed_last} ->\n\
        \          last = length(chars) - 1 - reversed_last\n\n          if last > first\
        \ + 1 do\n            middle_count =\n              chars\n              |>\
        \ Enum.slice((first + 1)..(last - 1))\n              |> Enum.uniq()\n      \
        \        |> length()\n\n            answer + middle_count\n          else\n\
        \            answer\n          end\n      end\n    end)\n  end\nend"
    approach: 'For each lowercase letter, find its first and last occurrence in the
      string. If there is at least one character between them, every distinct character
      in that interval can serve as the middle of a length-3 palindrome with that letter
      at both ends.


      Count the distinct middle characters for each possible outer letter and sum those
      counts. Each palindrome is counted once because its outer and middle characters
      uniquely identify it.'
    time_complexity: O(26n), which is O(n) for the fixed lowercase English alphabet,
      to scan the interval for each possible outer character.
    space_complexity: O(1), using a fixed-size array to track the 26 lowercase letters.
    elapsed_time: 79.58785080909729
    model: gpt-6-luna
    generated_at: '2026-11-13 00:09:07 '
---

## Problem #1930: Unique Length-3 Palindromic Subsequences

**Difficulty:** Medium

**Topics:** Hash Table, String, Bit Manipulation, Prefix Sum

## Problem Description

<p>Given a string <code>s</code>, return <em>the number of <strong>unique palindromes of length three</strong> that are a <strong>subsequence</strong> of </em><code>s</code>.</p>

<p>Note that even if there are multiple ways to obtain the same subsequence, it is still only counted <strong>once</strong>.</p>

<p>A <strong>palindrome</strong> is a string that reads the same forwards and backwards.</p>

<p>A <strong>subsequence</strong> of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.</p>

<ul>
	<li>For example, <code>&quot;ace&quot;</code> is a subsequence of <code>&quot;<u>a</u>b<u>c</u>d<u>e</u>&quot;</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aabca&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The 3 palindromic subsequences of length 3 are:
- &quot;aba&quot; (subsequence of &quot;<u>a</u>a<u>b</u>c<u>a</u>&quot;)
- &quot;aaa&quot; (subsequence of &quot;<u>aa</u>bc<u>a</u>&quot;)
- &quot;aca&quot; (subsequence of &quot;<u>a</u>ab<u>ca</u>&quot;)
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;adc&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> There are no palindromic subsequences of length 3 in &quot;adc&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bbcbaba&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong> The 4 palindromic subsequences of length 3 are:
- &quot;bbb&quot; (subsequence of &quot;<u>bb</u>c<u>b</u>aba&quot;)
- &quot;bcb&quot; (subsequence of &quot;<u>b</u>b<u>cb</u>aba&quot;)
- &quot;bab&quot; (subsequence of &quot;<u>b</u>bcb<u>ab</u>a&quot;)
- &quot;aba&quot; (subsequence of &quot;bbcb<u>aba</u>&quot;)
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
</ul>


## Hints

1. What is the maximum number of length-3 palindromic strings?

2. How can we keep track of the characters that appeared to the left of a given position?

## 🤖 AI-Generated Solution (gpt-6-luna)

### Approach

For each lowercase letter, find its first and last occurrence in the string. If there is at least one character between them, every distinct character in that interval can serve as the middle of a length-3 palindrome with that letter at both ends.

Count the distinct middle characters for each possible outer letter and sum those counts. Each palindrome is counted once because its outer and middle characters uniquely identify it.

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
    int countPalindromicSubsequence(string s) {
        int n = s.size();
        int answer = 0;
        for (char outer = 'a'; outer <= 'z'; ++outer) {
            int first = -1;
            int last = -1;
            for (int i = 0; i < n; ++i) {
                if (s[i] == outer) {
                    if (first == -1) first = i;
                    last = i;
                }
            }
            if (last - first <= 1) continue;
            bool seen[26] = {};
            for (int i = first + 1; i < last; ++i) {
                seen[s[i] - 'a'] = true;
            }
            for (bool present : seen) {
                if (present) ++answer;
            }
        }
        return answer;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int countPalindromicSubsequence(String s) {
        int n = s.length();
        int answer = 0;
        for (char outer = 'a'; outer <= 'z'; outer++) {
            int first = -1;
            int last = -1;
            for (int i = 0; i < n; i++) {
                if (s.charAt(i) == outer) {
                    if (first == -1) first = i;
                    last = i;
                }
            }
            if (last - first <= 1) continue;
            boolean[] seen = new boolean[26];
            for (int i = first + 1; i < last; i++) {
                seen[s.charAt(i) - 'a'] = true;
            }
            for (boolean present : seen) {
                if (present) answer++;
            }
        }
        return answer;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer = 0
        for outer in "abcdefghijklmnopqrstuvwxyz":
            first = s.find(outer)
            last = s.rfind(outer)
            if last - first <= 1:
                continue
            answer += len(set(s[first + 1:last]))
        return answer
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        answer = 0
        for outer in "abcdefghijklmnopqrstuvwxyz":
            first = s.find(outer)
            last = s.rfind(outer)
            if last - first <= 1:
                continue
            answer += len(set(s[first + 1:last]))
        return answer
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int countPalindromicSubsequence(char* s) {
    int n = 0;
    while (s[n] != '\0') {
        n++;
    }
    int answer = 0;
    for (char outer = 'a'; outer <= 'z'; outer++) {
        int first = -1;
        int last = -1;
        for (int i = 0; i < n; i++) {
            if (s[i] == outer) {
                if (first == -1) first = i;
                last = i;
            }
        }
        if (last - first <= 1) continue;
        int seen[26] = {0};
        for (int i = first + 1; i < last; i++) {
            seen[s[i] - 'a'] = 1;
        }
        for (int i = 0; i < 26; i++) {
            answer += seen[i];
        }
    }
    return answer;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int CountPalindromicSubsequence(string s) {
        int answer = 0;
        for (char outer = 'a'; outer <= 'z'; outer++) {
            int first = s.IndexOf(outer);
            int last = s.LastIndexOf(outer);
            if (last - first <= 1) {
                continue;
            }

            var middleCharacters = new HashSet<char>();
            for (int i = first + 1; i < last; i++) {
                middleCharacters.Add(s[i]);
            }
            answer += middleCharacters.Count;
        }
        return answer;
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
var countPalindromicSubsequence = function(s) {
    let answer = 0;
    for (let code = 97; code <= 122; code++) {
        const outer = String.fromCharCode(code);
        const first = s.indexOf(outer);
        const last = s.lastIndexOf(outer);
        if (last - first <= 1) {
            continue;
        }

        const middleCharacters = new Set(s.slice(first + 1, last));
        answer += middleCharacters.size;
    }
    return answer;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countPalindromicSubsequence(s: string): number {
    let answer = 0;
    for (let code = 97; code <= 122; code++) {
        const outer = String.fromCharCode(code);
        const first = s.indexOf(outer);
        const last = s.lastIndexOf(outer);
        if (last - first <= 1) {
            continue;
        }

        const middleCharacters = new Set(s.slice(first + 1, last));
        answer += middleCharacters.size;
    }
    return answer;
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
    function countPalindromicSubsequence($s) {
        $answer = 0;
        for ($code = 97; $code <= 122; $code++) {
            $outer = chr($code);
            $first = strpos($s, $outer);
            $last = strrpos($s, $outer);
            if ($last - $first <= 1) {
                continue;
            }

            $middleCharacters = [];
            for ($i = $first + 1; $i < $last; $i++) {
                $middleCharacters[$s[$i]] = true;
            }
            $answer += count($middleCharacters);
        }
        return $answer;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func countPalindromicSubsequence(_ s: String) -> Int {
        let characters = Array(s)
        var answer = 0
        for code in 97...122 {
            let outer = Character(UnicodeScalar(code)!)
            guard let first = characters.firstIndex(of: outer),
                  let last = characters.lastIndex(of: outer),
                  last - first > 1 else {
                continue
            }

            var middleCharacters = Set<Character>()
            for index in (first + 1)..<last {
                middleCharacters.insert(characters[index])
            }
            answer += middleCharacters.count
        }
        return answer
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun countPalindromicSubsequence(s: String): Int {
        var answer = 0
        for (outer in 'a'..'z') {
            val first = s.indexOf(outer)
            val last = s.lastIndexOf(outer)
            if (last - first <= 1) continue
            val middleCharacters = mutableSetOf<Char>()
            for (i in first + 1 until last) {
                middleCharacters.add(s[i])
            }
            answer += middleCharacters.size
        }
        return answer
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int countPalindromicSubsequence(String s) {
    var answer = 0;
    for (var code = 'a'.codeUnitAt(0); code <= 'z'.codeUnitAt(0); code++) {
      final outer = String.fromCharCode(code);
      final first = s.indexOf(outer);
      final last = s.lastIndexOf(outer);
      if (last - first <= 1) continue;
      final middleCharacters = <String>{};
      for (var i = first + 1; i < last; i++) {
        middleCharacters.add(s[i]);
      }
      answer += middleCharacters.length;
    }
    return answer;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func countPalindromicSubsequence(s string) int {
	answer := 0
	for outer := byte('a'); outer <= byte('z'); outer++ {
		first := -1
		last := -1
		for i := 0; i < len(s); i++ {
			if s[i] == outer {
				if first == -1 {
					first = i
				}
				last = i
			}
		}
		if last-first <= 1 {
			continue
		}
		var seen [26]bool
		count := 0
		for i := first + 1; i < last; i++ {
			index := s[i] - 'a'
			if !seen[index] {
				seen[index] = true
				count++
			}
		}
		answer += count
	}
	return answer
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @return {Integer}
def count_palindromic_subsequence(s)
  answer = 0
  ('a'..'z').each do |outer|
    first = s.index(outer)
    last = s.rindex(outer)
    next if last - first <= 1

    answer += s[(first + 1)...last].chars.uniq.length
  end
  answer
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def countPalindromicSubsequence(s: String): Int = {
        var answer = 0
        for (outer <- 'a' to 'z') {
            val first = s.indexOf(outer)
            val last = s.lastIndexOf(outer)
            if (last - first > 1) {
                answer += s.substring(first + 1, last).distinct.length
            }
        }
        answer
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn count_palindromic_subsequence(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut answer = 0;

        for outer in b'a'..=b'z' {
            let first = bytes.iter().position(|&c| c == outer);
            let last = bytes.iter().rposition(|&c| c == outer);

            if let (Some(first), Some(last)) = (first, last) {
                if last > first + 1 {
                    let mut seen = [false; 26];
                    for &middle in &bytes[first + 1..last] {
                        seen[(middle - b'a') as usize] = true;
                    }
                    answer += seen.iter().filter(|&&present| present).count() as i32;
                }
            }
        }

        answer
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (count-palindromic-subsequence s)
  (-> string? exact-integer?)
  (define chars (list->vector (string->list s)))
  (define n (vector-length chars))
  (for/sum ([outer (in-range 26)])
    (define letter (integer->char (+ (char->integer #\a) outer)))
    (define first
      (for/first ([i (in-range n)]
                  #:when (char=? (vector-ref chars i) letter))
        i))
    (define last
      (for/first ([i (in-range (sub1 n) -1 -1)]
                  #:when (char=? (vector-ref chars i) letter))
        i))
    (if (and first last (> (- last first) 1))
        (let ([seen (make-vector 26 #f)])
          (for ([i (in-range (add1 first) last)])
            (define middle (vector-ref chars i))
            (vector-set! seen (- (char->integer middle) (char->integer #\a)) #t))
          (for/sum ([present (in-vector seen)])
            (if present 1 0)))
        0)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec count_palindromic_subsequence(S :: unicode:unicode_binary()) -> integer().
count_palindromic_subsequence(S) ->
  Chars = unicode:characters_to_list(S),
  lists:sum([
    case find_bounds(Chars, $a + Offset) of
      {First, Last} when Last > First + 1 ->
        length(lists:usort(lists:sublist(Chars, First + 2, Last - First - 1)));
      _ ->
        0
    end
    || Offset <- lists:seq(0, 25)
  ]).

find_bounds(Chars, Letter) ->
  find_bounds(Chars, Letter, 1, none, none).

find_bounds([], _Letter, _Index, First, Last) ->
  case {First, Last} of
    {none, _} -> none;
    {F, L} -> {F, L}
  end;
find_bounds([Letter | Rest], Letter, Index, none, _Last) ->
  find_bounds(Rest, Letter, Index + 1, Index, Index);
find_bounds([Letter | Rest], Letter, Index, First, _Last) ->
  find_bounds(Rest, Letter, Index + 1, First, Index);
find_bounds([_ | Rest], Letter, Index, First, Last) ->
  find_bounds(Rest, Letter, Index + 1, First, Last).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec count_palindromic_subsequence(s :: String.t) :: integer
  def count_palindromic_subsequence(s) do
    chars = String.to_charlist(s)

    Enum.reduce(?a..?z, 0, fn outer, answer ->
      first = Enum.find_index(chars, &(&1 == outer))
      last = Enum.find_index(Enum.reverse(chars), &(&1 == outer))

      case {first, last} do
        {nil, _} ->
          answer

        {_, nil} ->
          answer

        {first, reversed_last} ->
          last = length(chars) - 1 - reversed_last

          if last > first + 1 do
            middle_count =
              chars
              |> Enum.slice((first + 1)..(last - 1))
              |> Enum.uniq()
              |> length()

            answer + middle_count
          else
            answer
          end
      end
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(26n), which is O(n) for the fixed lowercase English alphabet, to scan the interval for each possible outer character.
- **Space Complexity:** O(1), using a fixed-size array to track the 26 lowercase letters.
