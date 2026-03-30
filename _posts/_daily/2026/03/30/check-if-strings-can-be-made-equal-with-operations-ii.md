---
layout: post
title: "Check if Strings Can be Made Equal With Operations II"
date: 2026-03-30 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Hash Table", "String", "Sorting"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool checkStrings(string s1, string s2) {\n\
        \        vector<int> countEven(26, 0), countOdd(26, 0);\n        int n = s1.length();\n\
        \        for (int i = 0; i < n; ++i) {\n            if (i % 2 == 0) {\n    \
        \            countEven[s1[i] - 'a']++;\n                countEven[s2[i] - 'a']--;\n\
        \            } else {\n                countOdd[s1[i] - 'a']++;\n          \
        \      countOdd[s2[i] - 'a']--;\n            }\n        }\n        for (int\
        \ i = 0; i < 26; ++i) {\n            if (countEven[i] != 0 || countOdd[i] !=\
        \ 0) return false;\n        }\n        return true;\n    }\n};"
      java: "class Solution {\n    public boolean checkStrings(String s1, String s2)\
        \ {\n        int[] countEven = new int[26];\n        int[] countOdd = new int[26];\n\
        \        int n = s1.length();\n        for (int i = 0; i < n; i++) {\n     \
        \       if (i % 2 == 0) {\n                countEven[s1.charAt(i) - 'a']++;\n\
        \                countEven[s2.charAt(i) - 'a']--;\n            } else {\n  \
        \              countOdd[s1.charAt(i) - 'a']++;\n                countOdd[s2.charAt(i)\
        \ - 'a']--;\n            }\n        }\n        for (int i = 0; i < 26; i++)\
        \ {\n            if (countEven[i] != 0 || countOdd[i] != 0) return false;\n\
        \        }\n        return true;\n    }\n}"
      python: "class Solution(object):\n    def checkStrings(self, s1, s2):\n      \
        \  \"\"\"\n        :type s1: str\n        :type s2: str\n        :rtype: bool\n\
        \        \"\"\"\n        return sorted(s1[0::2]) == sorted(s2[0::2]) and sorted(s1[1::2])\
        \ == sorted(s2[1::2])"
      python3: "class Solution:\n    def checkStrings(self, s1: str, s2: str) -> bool:\n\
        \        return sorted(s1[0::2]) == sorted(s2[0::2]) and sorted(s1[1::2]) ==\
        \ sorted(s2[1::2])"
      c: "#include <stdbool.h>\n#include <string.h>\n\nbool checkStrings(char* s1, char*\
        \ s2) {\n    int countEven[26] = {0}, countOdd[26] = {0};\n    int n = strlen(s1);\n\
        \    for (int i = 0; i < n; i++) {\n        if (i % 2 == 0) {\n            countEven[s1[i]\
        \ - 'a']++;\n            countEven[s2[i] - 'a']--;\n        } else {\n     \
        \       countOdd[s1[i] - 'a']++;\n            countOdd[s2[i] - 'a']--;\n   \
        \     }\n    }\n    for (int i = 0; i < 26; i++) {\n        if (countEven[i]\
        \ != 0 || countOdd[i] != 0) return false;\n    }\n    return true;\n}"
      csharp: "public class Solution {\n    public bool CheckStrings(string s1, string\
        \ s2) {\n        int[] countEven = new int[26];\n        int[] countOdd = new\
        \ int[26];\n        int n = s1.Length;\n        for (int i = 0; i < n; i++)\
        \ {\n            if (i % 2 == 0) {\n                countEven[s1[i] - 'a']++;\n\
        \                countEven[s2[i] - 'a']--;\n            } else {\n         \
        \       countOdd[s1[i] - 'a']++;\n                countOdd[s2[i] - 'a']--;\n\
        \            }\n        }\n        for (int i = 0; i < 26; i++) {\n        \
        \    if (countEven[i] != 0 || countOdd[i] != 0) return false;\n        }\n \
        \       return true;\n    }\n}"
      javascript: "/**\n * @param {string} s1\n * @param {string} s2\n * @return {boolean}\n\
        \ */\nvar checkStrings = function(s1, s2) {\n    let countEven = new Array(26).fill(0);\n\
        \    let countOdd = new Array(26).fill(0);\n    for (let i = 0; i < s1.length;\
        \ i++) {\n        if (i % 2 === 0) {\n            countEven[s1.charCodeAt(i)\
        \ - 97]++;\n            countEven[s2.charCodeAt(i) - 97]--;\n        } else\
        \ {\n            countOdd[s1.charCodeAt(i) - 97]++;\n            countOdd[s2.charCodeAt(i)\
        \ - 97]--;\n        }\n    }\n    return countEven.every(v => v === 0) && countOdd.every(v\
        \ => v === 0);\n};"
      typescript: "function checkStrings(s1: string, s2: string): boolean {\n    const\
        \ e1 = new Array(26).fill(0);\n    const o1 = new Array(26).fill(0);\n    const\
        \ e2 = new Array(26).fill(0);\n    const o2 = new Array(26).fill(0);\n    const\
        \ n = s1.length;\n    for (let i = 0; i < n; i++) {\n        const v1 = s1.charCodeAt(i)\
        \ - 97;\n        const v2 = s2.charCodeAt(i) - 97;\n        if (i % 2 === 0)\
        \ {\n            e1[v1]++;\n            e2[v2]++;\n        } else {\n      \
        \      o1[v1]++;\n            o2[v2]++;\n        }\n    }\n    for (let i =\
        \ 0; i < 26; i++) {\n        if (e1[i] !== e2[i] || o1[i] !== o2[i]) return\
        \ false;\n    }\n    return true;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s1\n     * @param String\
        \ $s2\n     * @return Boolean\n     */\n    function checkStrings($s1, $s2)\
        \ {\n        $e1 = array_fill(0, 26, 0);\n        $o1 = array_fill(0, 26, 0);\n\
        \        $e2 = array_fill(0, 26, 0);\n        $o2 = array_fill(0, 26, 0);\n\
        \        $n = strlen($s1);\n        $base = ord('a');\n        for ($i = 0;\
        \ $i < $n; $i++) {\n            $v1 = ord($s1[$i]) - $base;\n            $v2\
        \ = ord($s2[$i]) - $base;\n            if ($i % 2 === 0) {\n               \
        \ $e1[$v1]++;\n                $e2[$v2]++;\n            } else {\n         \
        \       $o1[$v1]++;\n                $o2[$v2]++;\n            }\n        }\n\
        \        return $e1 === $e2 && $o1 === $o2;\n    }\n}"
      swift: "class Solution {\n    func checkStrings(_ s1: String, _ s2: String) ->\
        \ Bool {\n        var e1 = Array(repeating: 0, count: 26)\n        var o1 =\
        \ Array(repeating: 0, count: 26)\n        var e2 = Array(repeating: 0, count:\
        \ 26)\n        var o2 = Array(repeating: 0, count: 26)\n        let s1Chars\
        \ = Array(s1.utf8)\n        let s2Chars = Array(s2.utf8)\n        let aVal =\
        \ UInt8(97)\n        for i in 0..<s1Chars.count {\n            let v1 = Int(s1Chars[i]\
        \ - aVal)\n            let v2 = Int(s2Chars[i] - aVal)\n            if i % 2\
        \ == 0 {\n                e1[v1] += 1\n                e2[v2] += 1\n       \
        \     } else {\n                o1[v1] += 1\n                o2[v2] += 1\n \
        \           }\n        }\n        return e1 == e2 && o1 == o2\n    }\n}"
      kotlin: "class Solution {\n    fun checkStrings(s1: String, s2: String): Boolean\
        \ {\n        val e1 = IntArray(26)\n        val o1 = IntArray(26)\n        val\
        \ e2 = IntArray(26)\n        val o2 = IntArray(26)\n        for (i in s1.indices)\
        \ {\n            val v1 = s1[i] - 'a'\n            val v2 = s2[i] - 'a'\n  \
        \          if (i % 2 == 0) {\n                e1[v1]++\n                e2[v2]++\n\
        \            } else {\n                o1[v1]++\n                o2[v2]++\n\
        \            }\n        }\n        return e1.contentEquals(e2) && o1.contentEquals(o2)\n\
        \    }\n}"
      dart: "class Solution {\n  bool checkStrings(String s1, String s2) {\n    List<int>\
        \ e1 = List.filled(26, 0);\n    List<int> o1 = List.filled(26, 0);\n    List<int>\
        \ e2 = List.filled(26, 0);\n    List<int> o2 = List.filled(26, 0);\n    int\
        \ base = 'a'.codeUnitAt(0);\n    for (int i = 0; i < s1.length; i++) {\n   \
        \   int v1 = s1.codeUnitAt(i) - base;\n      int v2 = s2.codeUnitAt(i) - base;\n\
        \      if (i % 2 == 0) {\n        e1[v1]++;\n        e2[v2]++;\n      } else\
        \ {\n        o1[v1]++;\n        o2[v2]++;\n      }\n    }\n    for (int i =\
        \ 0; i < 26; i++) {\n      if (e1[i] != e2[i] || o1[i] != o2[i]) return false;\n\
        \    }\n    return true;\n  }\n}"
      go: "func checkStrings(s1 string, s2 string) bool {\n    var e1, o1, e2, o2 [26]int\n\
        \    for i := 0; i < len(s1); i++ {\n        v1 := s1[i] - 'a'\n        v2 :=\
        \ s2[i] - 'a'\n        if i%2 == 0 {\n            e1[v1]++\n            e2[v2]++\n\
        \        } else {\n            o1[v1]++\n            o2[v2]++\n        }\n \
        \   }\n    return e1 == e2 && o1 == o2\n}"
      ruby: "def check_strings(s1, s2)\n  s1_even = s1.chars.each_with_index.select\
        \ { |_, i| i.even? }.map(&:first).sort\n  s1_odd = s1.chars.each_with_index.select\
        \ { |_, i| i.odd? }.map(&:first).sort\n  s2_even = s2.chars.each_with_index.select\
        \ { |_, i| i.even? }.map(&:first).sort\n  s2_odd = s2.chars.each_with_index.select\
        \ { |_, i| i.odd? }.map(&:first).sort\n  s1_even == s2_even && s1_odd == s2_odd\n\
        end"
      scala: "object Solution {\n  def checkStrings(s1: String, s2: String): Boolean\
        \ = {\n    def getSortedParity(s: String, p: Int): Seq[Char] = {\n      s.zipWithIndex.collect\
        \ { case (c, i) if i % 2 == p => c }.sorted\n    }\n    getSortedParity(s1,\
        \ 0) == getSortedParity(s2, 0) && getSortedParity(s1, 1) == getSortedParity(s2,\
        \ 1)\n  }\n}"
      rust: "impl Solution {\n    pub fn check_strings(s1: String, s2: String) -> bool\
        \ {\n        let mut s1_even: Vec<char> = s1.chars().step_by(2).collect();\n\
        \        let mut s1_odd: Vec<char> = s1.chars().skip(1).step_by(2).collect();\n\
        \        let mut s2_even: Vec<char> = s2.chars().step_by(2).collect();\n   \
        \     let mut s2_odd: Vec<char> = s2.chars().skip(1).step_by(2).collect();\n\
        \        s1_even.sort_unstable();\n        s1_odd.sort_unstable();\n       \
        \ s2_even.sort_unstable();\n        s2_odd.sort_unstable();\n        s1_even\
        \ == s2_even && s1_odd == s2_odd\n    }\n}"
      racket: "(define/contract (check-strings s1 s2)\n  (-> string? string? boolean?)\n\
        \  (let ([get-parity (lambda (s p)\n                      (sort (for/list ([c\
        \ (in-string s)]\n                                       [i (in-naturals)]\n\
        \                                       #:when (= (remainder i 2) p))\n    \
        \                          c)\n                            char<?))])\n    (and\
        \ (equal? (get-parity s1 0) (get-parity s2 0))\n         (equal? (get-parity\
        \ s1 1) (get-parity s2 1)))))"
      erlang: "check_strings(S1, S2) ->\n  L1 = binary_to_list(S1),\n  L2 = binary_to_list(S2),\n\
        \  {E1, O1} = split_parity(L1, 0, [], []),\n  {E2, O2} = split_parity(L2, 0,\
        \ [], []),\n  lists:sort(E1) =:= lists:sort(E2) andalso lists:sort(O1) =:= lists:sort(O2).\n\
        \nsplit_parity([], _, E, O) -> {E, O};\nsplit_parity([H|T], Idx, E, O) ->\n\
        \  case Idx rem 2 of\n    0 -> split_parity(T, Idx + 1, [H|E], O);\n    1 ->\
        \ split_parity(T, Idx + 1, E, [H|O])\n  end."
      elixir: "defmodule Solution do\n  @spec check_strings(s1 :: String.t, s2 :: String.t)\
        \ :: boolean\n  def check_strings(s1, s2) do\n    get_parity = fn s ->\n   \
        \   chars = String.to_charlist(s)\n      even = chars |> Enum.take_every(2)\
        \ |> Enum.sort()\n      odd = chars |> Enum.drop(1) |> Enum.take_every(2) |>\
        \ Enum.sort()\n      {even, odd}\n    end\n    get_parity.(s1) == get_parity.(s2)\n\
        \  end\nend"
    approach: 'The problem asks whether we can make two strings equal by swapping characters
      at indices $i$ and $j$ if $j - i$ is even. This condition implies that we can
      only swap characters located at even indices with other characters at even indices,
      and characters at odd indices with other characters at odd indices. Consequently,
      the string can be thought of as two independent sets of characters: one set occupying
      the even positions and another occupying the odd positions.


      To determine if $s1$ can be transformed into $s2$, we must verify that the multiset
      of characters at even indices in $s1$ is identical to the multiset of characters
      at even indices in $s2$, and similarly for the odd indices. We achieve this by
      counting the frequency of each character (a-z) in both the even-indexed and odd-indexed
      groups for both strings. If the frequency counts for both groups match between
      $s1$ and $s2$, the strings can be made equal through a series of swaps; otherwise,
      they cannot.'
    time_complexity: O(n + \Sigma) where $n$ is the length of the strings and $\Sigma$
      is the size of the alphabet (26). We iterate through both strings once to count
      character frequencies, and then perform a constant-time comparison of the frequency
      arrays.
    space_complexity: O(\Sigma) or O(1) in terms of $n$, as we only need storage for
      the frequency counts of the 26 lowercase English letters for the even and odd
      positions.
    elapsed_time: 251.73775362968445
    model: gemini-3-flash-preview
    generated_at: '2026-03-30 01:54:50 '
---

## Problem #2840: Check if Strings Can be Made Equal With Operations II

**Difficulty:** Medium

**Topics:** Hash Table, String, Sorting

## Problem Description

<p>You are given two strings <code>s1</code> and <code>s2</code>, both of length <code>n</code>, consisting of <strong>lowercase</strong> English letters.</p>

<p>You can apply the following operation on <strong>any</strong> of the two strings <strong>any</strong> number of times:</p>

<ul>
	<li>Choose any two indices <code>i</code> and <code>j</code> such that <code>i &lt; j</code> and the difference <code>j - i</code> is <strong>even</strong>, then <strong>swap</strong> the two characters at those indices in the string.</li>
</ul>

<p>Return <code>true</code><em> if you can make the strings </em><code>s1</code><em> and </em><code>s2</code><em> equal, and&nbsp;</em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;abcdba&quot;, s2 = &quot;cabdab&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> We can apply the following operations on s1:
- Choose the indices i = 0, j = 2. The resulting string is s1 = &quot;cbadba&quot;.
- Choose the indices i = 2, j = 4. The resulting string is s1 = &quot;cbbdaa&quot;.
- Choose the indices i = 1, j = 5. The resulting string is s1 = &quot;cabdab&quot; = s2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;abe&quot;, s2 = &quot;bea&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> It is not possible to make the two strings equal.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == s1.length == s2.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>s1</code> and <code>s2</code> consist only of lowercase English letters.</li>
</ul>


## Hints

1. Characters in two positions can be swapped if and only if the two positions have the same parity.

2. To be able to make the two strings equal, the characters at even and odd positions in the strings should be the same.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks whether we can make two strings equal by swapping characters at indices $i$ and $j$ if $j - i$ is even. This condition implies that we can only swap characters located at even indices with other characters at even indices, and characters at odd indices with other characters at odd indices. Consequently, the string can be thought of as two independent sets of characters: one set occupying the even positions and another occupying the odd positions.

To determine if $s1$ can be transformed into $s2$, we must verify that the multiset of characters at even indices in $s1$ is identical to the multiset of characters at even indices in $s2$, and similarly for the odd indices. We achieve this by counting the frequency of each character (a-z) in both the even-indexed and odd-indexed groups for both strings. If the frequency counts for both groups match between $s1$ and $s2$, the strings can be made equal through a series of swaps; otherwise, they cannot.

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
    bool checkStrings(string s1, string s2) {
        vector<int> countEven(26, 0), countOdd(26, 0);
        int n = s1.length();
        for (int i = 0; i < n; ++i) {
            if (i % 2 == 0) {
                countEven[s1[i] - 'a']++;
                countEven[s2[i] - 'a']--;
            } else {
                countOdd[s1[i] - 'a']++;
                countOdd[s2[i] - 'a']--;
            }
        }
        for (int i = 0; i < 26; ++i) {
            if (countEven[i] != 0 || countOdd[i] != 0) return false;
        }
        return true;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean checkStrings(String s1, String s2) {
        int[] countEven = new int[26];
        int[] countOdd = new int[26];
        int n = s1.length();
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                countEven[s1.charAt(i) - 'a']++;
                countEven[s2.charAt(i) - 'a']--;
            } else {
                countOdd[s1.charAt(i) - 'a']++;
                countOdd[s2.charAt(i) - 'a']--;
            }
        }
        for (int i = 0; i < 26; i++) {
            if (countEven[i] != 0 || countOdd[i] != 0) return false;
        }
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def checkStrings(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        return sorted(s1[0::2]) == sorted(s2[0::2]) and sorted(s1[1::2]) == sorted(s2[1::2])
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return sorted(s1[0::2]) == sorted(s2[0::2]) and sorted(s1[1::2]) == sorted(s2[1::2])
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdbool.h>
#include <string.h>

bool checkStrings(char* s1, char* s2) {
    int countEven[26] = {0}, countOdd[26] = {0};
    int n = strlen(s1);
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) {
            countEven[s1[i] - 'a']++;
            countEven[s2[i] - 'a']--;
        } else {
            countOdd[s1[i] - 'a']++;
            countOdd[s2[i] - 'a']--;
        }
    }
    for (int i = 0; i < 26; i++) {
        if (countEven[i] != 0 || countOdd[i] != 0) return false;
    }
    return true;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool CheckStrings(string s1, string s2) {
        int[] countEven = new int[26];
        int[] countOdd = new int[26];
        int n = s1.Length;
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                countEven[s1[i] - 'a']++;
                countEven[s2[i] - 'a']--;
            } else {
                countOdd[s1[i] - 'a']++;
                countOdd[s2[i] - 'a']--;
            }
        }
        for (int i = 0; i < 26; i++) {
            if (countEven[i] != 0 || countOdd[i] != 0) return false;
        }
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkStrings = function(s1, s2) {
    let countEven = new Array(26).fill(0);
    let countOdd = new Array(26).fill(0);
    for (let i = 0; i < s1.length; i++) {
        if (i % 2 === 0) {
            countEven[s1.charCodeAt(i) - 97]++;
            countEven[s2.charCodeAt(i) - 97]--;
        } else {
            countOdd[s1.charCodeAt(i) - 97]++;
            countOdd[s2.charCodeAt(i) - 97]--;
        }
    }
    return countEven.every(v => v === 0) && countOdd.every(v => v === 0);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function checkStrings(s1: string, s2: string): boolean {
    const e1 = new Array(26).fill(0);
    const o1 = new Array(26).fill(0);
    const e2 = new Array(26).fill(0);
    const o2 = new Array(26).fill(0);
    const n = s1.length;
    for (let i = 0; i < n; i++) {
        const v1 = s1.charCodeAt(i) - 97;
        const v2 = s2.charCodeAt(i) - 97;
        if (i % 2 === 0) {
            e1[v1]++;
            e2[v2]++;
        } else {
            o1[v1]++;
            o2[v2]++;
        }
    }
    for (let i = 0; i < 26; i++) {
        if (e1[i] !== e2[i] || o1[i] !== o2[i]) return false;
    }
    return true;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String $s1
     * @param String $s2
     * @return Boolean
     */
    function checkStrings($s1, $s2) {
        $e1 = array_fill(0, 26, 0);
        $o1 = array_fill(0, 26, 0);
        $e2 = array_fill(0, 26, 0);
        $o2 = array_fill(0, 26, 0);
        $n = strlen($s1);
        $base = ord('a');
        for ($i = 0; $i < $n; $i++) {
            $v1 = ord($s1[$i]) - $base;
            $v2 = ord($s2[$i]) - $base;
            if ($i % 2 === 0) {
                $e1[$v1]++;
                $e2[$v2]++;
            } else {
                $o1[$v1]++;
                $o2[$v2]++;
            }
        }
        return $e1 === $e2 && $o1 === $o2;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func checkStrings(_ s1: String, _ s2: String) -> Bool {
        var e1 = Array(repeating: 0, count: 26)
        var o1 = Array(repeating: 0, count: 26)
        var e2 = Array(repeating: 0, count: 26)
        var o2 = Array(repeating: 0, count: 26)
        let s1Chars = Array(s1.utf8)
        let s2Chars = Array(s2.utf8)
        let aVal = UInt8(97)
        for i in 0..<s1Chars.count {
            let v1 = Int(s1Chars[i] - aVal)
            let v2 = Int(s2Chars[i] - aVal)
            if i % 2 == 0 {
                e1[v1] += 1
                e2[v2] += 1
            } else {
                o1[v1] += 1
                o2[v2] += 1
            }
        }
        return e1 == e2 && o1 == o2
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun checkStrings(s1: String, s2: String): Boolean {
        val e1 = IntArray(26)
        val o1 = IntArray(26)
        val e2 = IntArray(26)
        val o2 = IntArray(26)
        for (i in s1.indices) {
            val v1 = s1[i] - 'a'
            val v2 = s2[i] - 'a'
            if (i % 2 == 0) {
                e1[v1]++
                e2[v2]++
            } else {
                o1[v1]++
                o2[v2]++
            }
        }
        return e1.contentEquals(e2) && o1.contentEquals(o2)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool checkStrings(String s1, String s2) {
    List<int> e1 = List.filled(26, 0);
    List<int> o1 = List.filled(26, 0);
    List<int> e2 = List.filled(26, 0);
    List<int> o2 = List.filled(26, 0);
    int base = 'a'.codeUnitAt(0);
    for (int i = 0; i < s1.length; i++) {
      int v1 = s1.codeUnitAt(i) - base;
      int v2 = s2.codeUnitAt(i) - base;
      if (i % 2 == 0) {
        e1[v1]++;
        e2[v2]++;
      } else {
        o1[v1]++;
        o2[v2]++;
      }
    }
    for (int i = 0; i < 26; i++) {
      if (e1[i] != e2[i] || o1[i] != o2[i]) return false;
    }
    return true;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func checkStrings(s1 string, s2 string) bool {
    var e1, o1, e2, o2 [26]int
    for i := 0; i < len(s1); i++ {
        v1 := s1[i] - 'a'
        v2 := s2[i] - 'a'
        if i%2 == 0 {
            e1[v1]++
            e2[v2]++
        } else {
            o1[v1]++
            o2[v2]++
        }
    }
    return e1 == e2 && o1 == o2
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def check_strings(s1, s2)
  s1_even = s1.chars.each_with_index.select { |_, i| i.even? }.map(&:first).sort
  s1_odd = s1.chars.each_with_index.select { |_, i| i.odd? }.map(&:first).sort
  s2_even = s2.chars.each_with_index.select { |_, i| i.even? }.map(&:first).sort
  s2_odd = s2.chars.each_with_index.select { |_, i| i.odd? }.map(&:first).sort
  s1_even == s2_even && s1_odd == s2_odd
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def checkStrings(s1: String, s2: String): Boolean = {
    def getSortedParity(s: String, p: Int): Seq[Char] = {
      s.zipWithIndex.collect { case (c, i) if i % 2 == p => c }.sorted
    }
    getSortedParity(s1, 0) == getSortedParity(s2, 0) && getSortedParity(s1, 1) == getSortedParity(s2, 1)
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn check_strings(s1: String, s2: String) -> bool {
        let mut s1_even: Vec<char> = s1.chars().step_by(2).collect();
        let mut s1_odd: Vec<char> = s1.chars().skip(1).step_by(2).collect();
        let mut s2_even: Vec<char> = s2.chars().step_by(2).collect();
        let mut s2_odd: Vec<char> = s2.chars().skip(1).step_by(2).collect();
        s1_even.sort_unstable();
        s1_odd.sort_unstable();
        s2_even.sort_unstable();
        s2_odd.sort_unstable();
        s1_even == s2_even && s1_odd == s2_odd
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (check-strings s1 s2)
  (-> string? string? boolean?)
  (let ([get-parity (lambda (s p)
                      (sort (for/list ([c (in-string s)]
                                       [i (in-naturals)]
                                       #:when (= (remainder i 2) p))
                              c)
                            char<?))])
    (and (equal? (get-parity s1 0) (get-parity s2 0))
         (equal? (get-parity s1 1) (get-parity s2 1)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
check_strings(S1, S2) ->
  L1 = binary_to_list(S1),
  L2 = binary_to_list(S2),
  {E1, O1} = split_parity(L1, 0, [], []),
  {E2, O2} = split_parity(L2, 0, [], []),
  lists:sort(E1) =:= lists:sort(E2) andalso lists:sort(O1) =:= lists:sort(O2).

split_parity([], _, E, O) -> {E, O};
split_parity([H|T], Idx, E, O) ->
  case Idx rem 2 of
    0 -> split_parity(T, Idx + 1, [H|E], O);
    1 -> split_parity(T, Idx + 1, E, [H|O])
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec check_strings(s1 :: String.t, s2 :: String.t) :: boolean
  def check_strings(s1, s2) do
    get_parity = fn s ->
      chars = String.to_charlist(s)
      even = chars |> Enum.take_every(2) |> Enum.sort()
      odd = chars |> Enum.drop(1) |> Enum.take_every(2) |> Enum.sort()
      {even, odd}
    end
    get_parity.(s1) == get_parity.(s2)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n + \Sigma) where $n$ is the length of the strings and $\Sigma$ is the size of the alphabet (26). We iterate through both strings once to count character frequencies, and then perform a constant-time comparison of the frequency arrays.
- **Space Complexity:** O(\Sigma) or O(1) in terms of $n$, as we only need storage for the frequency counts of the 26 lowercase English letters for the even and odd positions.
