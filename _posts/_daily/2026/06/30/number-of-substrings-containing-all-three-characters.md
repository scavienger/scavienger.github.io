---
layout: post
title: "Number of Substrings Containing All Three Characters"
date: 2026-06-30 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Hash Table", "String", "Sliding Window"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int numberOfSubstrings(string s) {\n    \
        \    int last[3] = {-1, -1, -1};\n        int res = 0, n = s.length();\n   \
        \     for (int i = 0; i < n; ++i) {\n            last[s[i] - 'a'] = i;\n   \
        \         int min_idx = last[0];\n            if (last[1] < min_idx) min_idx\
        \ = last[1];\n            if (last[2] < min_idx) min_idx = last[2];\n      \
        \      res += (min_idx + 1);\n        }\n        return res;\n    }\n};"
      java: "class Solution {\n    public int numberOfSubstrings(String s) {\n     \
        \   int[] last = {-1, -1, -1};\n        int res = 0, n = s.length();\n     \
        \   for (int i = 0; i < n; i++) {\n            last[s.charAt(i) - 'a'] = i;\n\
        \            int minIdx = Math.min(last[0], Math.min(last[1], last[2]));\n \
        \           res += (minIdx + 1);\n        }\n        return res;\n    }\n}"
      python: "class Solution(object):\n    def numberOfSubstrings(self, s):\n     \
        \   \"\"\"\n        :type s: str\n        :rtype: int\n        \"\"\"\n    \
        \    last = [-1, -1, -1]\n        res = 0\n        for i in range(len(s)):\n\
        \            char = s[i]\n            last[ord(char) - ord('a')] = i\n     \
        \       res += min(last) + 1\n        return res"
      python3: "class Solution:\n    def numberOfSubstrings(self, s: str) -> int:\n\
        \        last = [-1, -1, -1]\n        res = 0\n        for i, char in enumerate(s):\n\
        \            last[ord(char) - ord('a')] = i\n            res += min(last) +\
        \ 1\n        return res"
      c: "int numberOfSubstrings(char* s) {\n    int last[3] = {-1, -1, -1};\n    int\
        \ res = 0;\n    for (int i = 0; s[i] != '\\0'; i++) {\n        last[s[i] - 'a']\
        \ = i;\n        int min_idx = last[0];\n        if (last[1] < min_idx) min_idx\
        \ = last[1];\n        if (last[2] < min_idx) min_idx = last[2];\n        res\
        \ += (min_idx + 1);\n    }\n    return res;\n}"
      csharp: "public class Solution {\n    public int NumberOfSubstrings(string s)\
        \ {\n        int n = s.Length;\n        int lastA = -1, lastB = -1, lastC =\
        \ -1;\n        int count = 0;\n        for (int i = 0; i < n; i++) {\n     \
        \       if (s[i] == 'a') lastA = i;\n            else if (s[i] == 'b') lastB\
        \ = i;\n            else if (s[i] == 'c') lastC = i;\n\n            if (lastA\
        \ != -1 && lastB != -1 && lastC != -1) {\n                count += Math.Min(Math.Min(lastA,\
        \ lastB), lastC) + 1;\n            }\n        }\n        return count;\n   \
        \ }\n}"
      javascript: "/**\n * @param {string} s\n * @return {number}\n */\nvar numberOfSubstrings\
        \ = function(s) {\n    let n = s.length;\n    let lastA = -1, lastB = -1, lastC\
        \ = -1;\n    let count = 0;\n    for (let i = 0; i < n; i++) {\n        if (s[i]\
        \ === 'a') lastA = i;\n        else if (s[i] === 'b') lastB = i;\n        else\
        \ if (s[i] === 'c') lastC = i;\n\n        if (lastA !== -1 && lastB !== -1 &&\
        \ lastC !== -1) {\n            count += Math.min(lastA, lastB, lastC) + 1;\n\
        \        }\n    }\n    return count;\n};"
      typescript: "function numberOfSubstrings(s: string): number {\n    let n = s.length;\n\
        \    let lastA = -1, lastB = -1, lastC = -1;\n    let count = 0;\n    for (let\
        \ i = 0; i < n; i++) {\n        if (s[i] === 'a') lastA = i;\n        else if\
        \ (s[i] === 'b') lastB = i;\n        else if (s[i] === 'c') lastC = i;\n\n \
        \       if (lastA !== -1 && lastB !== -1 && lastC !== -1) {\n            count\
        \ += Math.min(lastA, Math.min(lastB, lastC)) + 1;\n        }\n    }\n    return\
        \ count;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return Integer\n\
        \     */\n    function numberOfSubstrings($s) {\n        $n = strlen($s);\n\
        \        $lastA = -1;\n        $lastB = -1;\n        $lastC = -1;\n        $count\
        \ = 0;\n        for ($i = 0; $i < $n; $i++) {\n            if ($s[$i] === 'a')\
        \ $lastA = $i;\n            else if ($s[$i] === 'b') $lastB = $i;\n        \
        \    else if ($s[$i] === 'c') $lastC = $i;\n\n            if ($lastA !== -1\
        \ && $lastB !== -1 && $lastC !== -1) {\n                $count += min($lastA,\
        \ $lastB, $lastC) + 1;\n            }\n        }\n        return $count;\n \
        \   }\n}"
      swift: "class Solution {\n    func numberOfSubstrings(_ s: String) -> Int {\n\
        \        let sArray = Array(s)\n        let n = sArray.count\n        var lastA\
        \ = -1, lastB = -1, lastC = -1\n        var count = 0\n        for i in 0..<n\
        \ {\n            if sArray[i] == \"a\" { lastA = i }\n            else if sArray[i]\
        \ == \"b\" { lastB = i }\n            else if sArray[i] == \"c\" { lastC = i\
        \ }\n\n            if lastA != -1 && lastB != -1 && lastC != -1 {\n        \
        \        count += min(min(lastA, lastB), lastC) + 1\n            }\n       \
        \ }\n        return count\n    }\n}"
      kotlin: "class Solution {\n    fun numberOfSubstrings(s: String): Int {\n    \
        \    val count = IntArray(3)\n        var left = 0\n        var ans = 0\n  \
        \      for (right in 0 until s.length) {\n            count[s[right] - 'a']++\n\
        \            while (count[0] > 0 && count[1] > 0 && count[2] > 0) {\n      \
        \          count[s[left] - 'a']--\n                left++\n            }\n \
        \           ans += left\n        }\n        return ans\n    }\n}"
      dart: "class Solution {\n  int numberOfSubstrings(String s) {\n    List<int> count\
        \ = [0, 0, 0];\n    int left = 0;\n    int ans = 0;\n    int charA = 'a'.codeUnitAt(0);\n\
        \    for (int right = 0; right < s.length; right++) {\n      count[s.codeUnitAt(right)\
        \ - charA]++;\n      while (count[0] > 0 && count[1] > 0 && count[2] > 0) {\n\
        \        count[s.codeUnitAt(left) - charA]--;\n        left++;\n      }\n  \
        \    ans += left;\n    }\n    return ans;\n  }\n}"
      go: "func numberOfSubstrings(s string) int {\n    count := make([]int, 3)\n  \
        \  left := 0\n    ans := 0\n    for right := 0; right < len(s); right++ {\n\
        \        count[s[right]-'a']++\n        for count[0] > 0 && count[1] > 0 &&\
        \ count[2] > 0 {\n            count[s[left]-'a']--\n            left++\n   \
        \     }\n        ans += left\n    }\n    return ans\n}"
      ruby: "# @param {String} s\n# @return {Integer}\ndef number_of_substrings(s)\n\
        \    count = [0, 0, 0]\n    left = 0\n    ans = 0\n    char_a = 'a'.ord\n  \
        \  s.each_char.with_index do |char, right|\n        count[char.ord - char_a]\
        \ += 1\n        while count[0] > 0 && count[1] > 0 && count[2] > 0\n       \
        \     count[s[left].ord - char_a] -= 1\n            left += 1\n        end\n\
        \        ans += left\n    end\n    ans\nend"
      scala: "object Solution {\n    def numberOfSubstrings(s: String): Int = {\n  \
        \      val count = Array(0, 0, 0)\n        var left = 0\n        var ans = 0\n\
        \        for (right <- 0 until s.length) {\n            count(s(right) - 'a')\
        \ += 1\n            while (count(0) > 0 && count(1) > 0 && count(2) > 0) {\n\
        \                count(s(left) - 'a') -= 1\n                left += 1\n    \
        \        }\n            ans += left\n        }\n        ans\n    }\n}"
      rust: "impl Solution {\n    pub fn number_of_substrings(s: String) -> i32 {\n\
        \        let mut last = [-1i32; 3];\n        let mut count = 0i32;\n       \
        \ for (i, c) in s.bytes().enumerate() {\n            last[(c - b'a') as usize]\
        \ = i as i32;\n            if last[0] != -1 && last[1] != -1 && last[2] != -1\
        \ {\n                let min_pos = last[0].min(last[1]).min(last[2]);\n    \
        \            count += min_pos + 1;\n            }\n        }\n        count\n\
        \    }\n}"
      racket: "(define/contract (number-of-substrings s)\n  (-> string? exact-integer?)\n\
        \  (let ([n (string-length s)])\n    (let loop ([i 0] [a -1] [b -1] [c -1] [acc\
        \ 0])\n      (if (< i n)\n          (let* ([ch (string-ref s i)]\n         \
        \        [na (if (char=? ch #\\a) i a)]\n                 [nb (if (char=? ch\
        \ #\\b) i b)]\n                 [nc (if (char=? ch #\\c) i c)])\n          \
        \  (if (and (>= na 0) (>= nb 0) (>= nc 0))\n                (loop (+ i 1) na\
        \ nb nc (+ acc (min na nb nc) 1))\n                (loop (+ i 1) na nb nc acc)))\n\
        \          acc))))"
      erlang: "-spec number_of_substrings(S :: unicode:unicode_binary()) -> integer().\n\
        number_of_substrings(S) ->\n  number_of_substrings_helper(S, 0, -1, -1, -1,\
        \ 0).\n\nnumber_of_substrings_helper(<<>>, _Idx, _A, _B, _C, Acc) ->\n  Acc;\n\
        number_of_substrings_helper(<<Char, Rest/binary>>, Idx, A, B, C, Acc) ->\n \
        \ {NA, NB, NC} = case Char of\n    $a -> {Idx, B, C};\n    $b -> {A, Idx, C};\n\
        \    $c -> {A, B, Idx};\n    _ -> {A, B, C}\n  end,\n  NewAcc = if\n    NA >=\
        \ 0, NB >= 0, NC >= 0 ->\n      Acc + min(NA, min(NB, NC)) + 1;\n    true ->\n\
        \      Acc\n  end,\n  number_of_substrings_helper(Rest, Idx + 1, NA, NB, NC,\
        \ NewAcc)."
      elixir: "defmodule Solution do\n  @spec number_of_substrings(s :: String.t) ::\
        \ integer\n  def number_of_substrings(s) do\n    s\n    |> String.to_charlist()\n\
        \    |> Enum.reduce({0, -1, -1, -1, 0}, fn char, {idx, a, b, c, acc} ->\n  \
        \    {na, nb, nc} = case char do\n        ?a -> {idx, b, c}\n        ?b -> {a,\
        \ idx, c}\n        ?c -> {a, b, idx}\n        _ -> {a, b, idx}\n      end\n\
        \      new_acc = if na != -1 and nb != -1 and nc != -1 do\n        acc + min(na,\
        \ min(nb, nc)) + 1\n      else\n        acc\n      end\n      {idx + 1, na,\
        \ nb, nc, new_acc}\n    end)\n    |> elem(4)\n  end\nend"
    approach: 'The core intuition is to count the number of valid substrings ending
      at each position $i$. For a substring ending at index $i$ to be valid, it must
      contain at least one ''a'', one ''b'', and one ''c''. By keeping track of the
      last seen index for each character as we iterate through the string, the shortest
      valid substring ending at $i$ is determined by the minimum of these three indices.
      If any character has not been seen yet, this minimum index will be $-1$.


      Once all three characters have been encountered at least once, any substring that
      starts at an index $j$ in the range $[0, \min(\text{last}_a, \text{last}_b, \text{last}_c)]$
      and ends at $i$ will contain at least one occurrence of all three characters.
      Therefore, at each index $i$, we simply calculate this minimum index and add $\min(\text{last}_a,
      \text{last}_b, \text{last}_c) + 1$ to our total count. This ensures we count every
      valid substring exactly once, categorized by its ending position.'
    time_complexity: O(n) where n is the length of the string. We perform a single pass
      through the string, and at each character, we update a few variables and perform
      a constant number of comparisons to find the minimum index.
    space_complexity: O(1) because we only store the last seen indices of the three
      characters ('a', 'b', and 'c') in a fixed-size array or three variables, which
      does not depend on the input string length.
    elapsed_time: 249.54839944839478
    model: gemini-3-flash-preview
    generated_at: '2026-06-30 02:43:38 '
---

## Problem #1358: Number of Substrings Containing All Three Characters

**Difficulty:** Medium

**Topics:** Hash Table, String, Sliding Window

## Problem Description

<p>Given a string <code>s</code>&nbsp;consisting only of characters <em>a</em>, <em>b</em> and <em>c</em>.</p>

<p>Return the number of substrings containing <b>at least</b>&nbsp;one occurrence of all these characters <em>a</em>, <em>b</em> and <em>c</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcabc&quot;
<strong>Output:</strong> 10
<strong>Explanation:</strong> The substrings containing&nbsp;at least&nbsp;one occurrence of the characters&nbsp;<em>a</em>,&nbsp;<em>b</em>&nbsp;and&nbsp;<em>c are &quot;</em>abc<em>&quot;, &quot;</em>abca<em>&quot;, &quot;</em>abcab<em>&quot;, &quot;</em>abcabc<em>&quot;, &quot;</em>bca<em>&quot;, &quot;</em>bcab<em>&quot;, &quot;</em>bcabc<em>&quot;, &quot;</em>cab<em>&quot;, &quot;</em>cabc<em>&quot; </em>and<em> &quot;</em>abc<em>&quot; </em>(<strong>again</strong>)<em>. </em>
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aaacb&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The substrings containing&nbsp;at least&nbsp;one occurrence of the characters&nbsp;<em>a</em>,&nbsp;<em>b</em>&nbsp;and&nbsp;<em>c are &quot;</em>aaacb<em>&quot;, &quot;</em>aacb<em>&quot; </em>and<em> &quot;</em>acb<em>&quot;.</em><em> </em>
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abc&quot;
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= s.length &lt;= 5 x 10^4</code></li>
	<li><code>s</code>&nbsp;only consists of&nbsp;<em>a</em>, <em>b</em> or <em>c&nbsp;</em>characters.</li>
</ul>


## Hints

1. For each position we simply need to find the first occurrence of a/b/c on or after this position.

2. So we can pre-compute three link-list of indices of each a, b, and c.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The core intuition is to count the number of valid substrings ending at each position $i$. For a substring ending at index $i$ to be valid, it must contain at least one 'a', one 'b', and one 'c'. By keeping track of the last seen index for each character as we iterate through the string, the shortest valid substring ending at $i$ is determined by the minimum of these three indices. If any character has not been seen yet, this minimum index will be $-1$.

Once all three characters have been encountered at least once, any substring that starts at an index $j$ in the range $[0, \min(\text{last}_a, \text{last}_b, \text{last}_c)]$ and ends at $i$ will contain at least one occurrence of all three characters. Therefore, at each index $i$, we simply calculate this minimum index and add $\min(\text{last}_a, \text{last}_b, \text{last}_c) + 1$ to our total count. This ensures we count every valid substring exactly once, categorized by its ending position.

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
    int numberOfSubstrings(string s) {
        int last[3] = {-1, -1, -1};
        int res = 0, n = s.length();
        for (int i = 0; i < n; ++i) {
            last[s[i] - 'a'] = i;
            int min_idx = last[0];
            if (last[1] < min_idx) min_idx = last[1];
            if (last[2] < min_idx) min_idx = last[2];
            res += (min_idx + 1);
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
    public int numberOfSubstrings(String s) {
        int[] last = {-1, -1, -1};
        int res = 0, n = s.length();
        for (int i = 0; i < n; i++) {
            last[s.charAt(i) - 'a'] = i;
            int minIdx = Math.min(last[0], Math.min(last[1], last[2]));
            res += (minIdx + 1);
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
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = [-1, -1, -1]
        res = 0
        for i in range(len(s)):
            char = s[i]
            last[ord(char) - ord('a')] = i
            res += min(last) + 1
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last = [-1, -1, -1]
        res = 0
        for i, char in enumerate(s):
            last[ord(char) - ord('a')] = i
            res += min(last) + 1
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int numberOfSubstrings(char* s) {
    int last[3] = {-1, -1, -1};
    int res = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        last[s[i] - 'a'] = i;
        int min_idx = last[0];
        if (last[1] < min_idx) min_idx = last[1];
        if (last[2] < min_idx) min_idx = last[2];
        res += (min_idx + 1);
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
    public int NumberOfSubstrings(string s) {
        int n = s.Length;
        int lastA = -1, lastB = -1, lastC = -1;
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] == 'a') lastA = i;
            else if (s[i] == 'b') lastB = i;
            else if (s[i] == 'c') lastC = i;

            if (lastA != -1 && lastB != -1 && lastC != -1) {
                count += Math.Min(Math.Min(lastA, lastB), lastC) + 1;
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
 * @param {string} s
 * @return {number}
 */
var numberOfSubstrings = function(s) {
    let n = s.length;
    let lastA = -1, lastB = -1, lastC = -1;
    let count = 0;
    for (let i = 0; i < n; i++) {
        if (s[i] === 'a') lastA = i;
        else if (s[i] === 'b') lastB = i;
        else if (s[i] === 'c') lastC = i;

        if (lastA !== -1 && lastB !== -1 && lastC !== -1) {
            count += Math.min(lastA, lastB, lastC) + 1;
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
function numberOfSubstrings(s: string): number {
    let n = s.length;
    let lastA = -1, lastB = -1, lastC = -1;
    let count = 0;
    for (let i = 0; i < n; i++) {
        if (s[i] === 'a') lastA = i;
        else if (s[i] === 'b') lastB = i;
        else if (s[i] === 'c') lastC = i;

        if (lastA !== -1 && lastB !== -1 && lastC !== -1) {
            count += Math.min(lastA, Math.min(lastB, lastC)) + 1;
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
     * @param String $s
     * @return Integer
     */
    function numberOfSubstrings($s) {
        $n = strlen($s);
        $lastA = -1;
        $lastB = -1;
        $lastC = -1;
        $count = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === 'a') $lastA = $i;
            else if ($s[$i] === 'b') $lastB = $i;
            else if ($s[$i] === 'c') $lastC = $i;

            if ($lastA !== -1 && $lastB !== -1 && $lastC !== -1) {
                $count += min($lastA, $lastB, $lastC) + 1;
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
    func numberOfSubstrings(_ s: String) -> Int {
        let sArray = Array(s)
        let n = sArray.count
        var lastA = -1, lastB = -1, lastC = -1
        var count = 0
        for i in 0..<n {
            if sArray[i] == "a" { lastA = i }
            else if sArray[i] == "b" { lastB = i }
            else if sArray[i] == "c" { lastC = i }

            if lastA != -1 && lastB != -1 && lastC != -1 {
                count += min(min(lastA, lastB), lastC) + 1
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
    fun numberOfSubstrings(s: String): Int {
        val count = IntArray(3)
        var left = 0
        var ans = 0
        for (right in 0 until s.length) {
            count[s[right] - 'a']++
            while (count[0] > 0 && count[1] > 0 && count[2] > 0) {
                count[s[left] - 'a']--
                left++
            }
            ans += left
        }
        return ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int numberOfSubstrings(String s) {
    List<int> count = [0, 0, 0];
    int left = 0;
    int ans = 0;
    int charA = 'a'.codeUnitAt(0);
    for (int right = 0; right < s.length; right++) {
      count[s.codeUnitAt(right) - charA]++;
      while (count[0] > 0 && count[1] > 0 && count[2] > 0) {
        count[s.codeUnitAt(left) - charA]--;
        left++;
      }
      ans += left;
    }
    return ans;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func numberOfSubstrings(s string) int {
    count := make([]int, 3)
    left := 0
    ans := 0
    for right := 0; right < len(s); right++ {
        count[s[right]-'a']++
        for count[0] > 0 && count[1] > 0 && count[2] > 0 {
            count[s[left]-'a']--
            left++
        }
        ans += left
    }
    return ans
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @return {Integer}
def number_of_substrings(s)
    count = [0, 0, 0]
    left = 0
    ans = 0
    char_a = 'a'.ord
    s.each_char.with_index do |char, right|
        count[char.ord - char_a] += 1
        while count[0] > 0 && count[1] > 0 && count[2] > 0
            count[s[left].ord - char_a] -= 1
            left += 1
        end
        ans += left
    end
    ans
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def numberOfSubstrings(s: String): Int = {
        val count = Array(0, 0, 0)
        var left = 0
        var ans = 0
        for (right <- 0 until s.length) {
            count(s(right) - 'a') += 1
            while (count(0) > 0 && count(1) > 0 && count(2) > 0) {
                count(s(left) - 'a') -= 1
                left += 1
            }
            ans += left
        }
        ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn number_of_substrings(s: String) -> i32 {
        let mut last = [-1i32; 3];
        let mut count = 0i32;
        for (i, c) in s.bytes().enumerate() {
            last[(c - b'a') as usize] = i as i32;
            if last[0] != -1 && last[1] != -1 && last[2] != -1 {
                let min_pos = last[0].min(last[1]).min(last[2]);
                count += min_pos + 1;
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
(define/contract (number-of-substrings s)
  (-> string? exact-integer?)
  (let ([n (string-length s)])
    (let loop ([i 0] [a -1] [b -1] [c -1] [acc 0])
      (if (< i n)
          (let* ([ch (string-ref s i)]
                 [na (if (char=? ch #\a) i a)]
                 [nb (if (char=? ch #\b) i b)]
                 [nc (if (char=? ch #\c) i c)])
            (if (and (>= na 0) (>= nb 0) (>= nc 0))
                (loop (+ i 1) na nb nc (+ acc (min na nb nc) 1))
                (loop (+ i 1) na nb nc acc)))
          acc))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec number_of_substrings(S :: unicode:unicode_binary()) -> integer().
number_of_substrings(S) ->
  number_of_substrings_helper(S, 0, -1, -1, -1, 0).

number_of_substrings_helper(<<>>, _Idx, _A, _B, _C, Acc) ->
  Acc;
number_of_substrings_helper(<<Char, Rest/binary>>, Idx, A, B, C, Acc) ->
  {NA, NB, NC} = case Char of
    $a -> {Idx, B, C};
    $b -> {A, Idx, C};
    $c -> {A, B, Idx};
    _ -> {A, B, C}
  end,
  NewAcc = if
    NA >= 0, NB >= 0, NC >= 0 ->
      Acc + min(NA, min(NB, NC)) + 1;
    true ->
      Acc
  end,
  number_of_substrings_helper(Rest, Idx + 1, NA, NB, NC, NewAcc).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec number_of_substrings(s :: String.t) :: integer
  def number_of_substrings(s) do
    s
    |> String.to_charlist()
    |> Enum.reduce({0, -1, -1, -1, 0}, fn char, {idx, a, b, c, acc} ->
      {na, nb, nc} = case char do
        ?a -> {idx, b, c}
        ?b -> {a, idx, c}
        ?c -> {a, b, idx}
        _ -> {a, b, idx}
      end
      new_acc = if na != -1 and nb != -1 and nc != -1 do
        acc + min(na, min(nb, nc)) + 1
      else
        acc
      end
      {idx + 1, na, nb, nc, new_acc}
    end)
    |> elem(4)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the string. We perform a single pass through the string, and at each character, we update a few variables and perform a constant number of comparisons to find the minimum index.
- **Space Complexity:** O(1) because we only store the last seen indices of the three characters ('a', 'b', and 'c') in a fixed-size array or three variables, which does not depend on the input string length.
