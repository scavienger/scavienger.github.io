---
layout: post
title: "Maximum Number of Balloons"
date: 2026-06-22 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Hash Table", "String", "Counting"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/maximum-number-of-balloons/
ai_solutions:
  - solutions:
      cpp: "#include <string>\n#include <algorithm>\n#include <vector>\n\nusing namespace\
        \ std;\n\nclass Solution {\npublic:\n    int maxNumberOfBalloons(string text)\
        \ {\n        int counts[26] = {0};\n        for (char c : text) {\n        \
        \    counts[c - 'a']++;\n        }\n        int b = counts['b' - 'a'];\n   \
        \     int a = counts['a' - 'a'];\n        int l = counts['l' - 'a'] / 2;\n \
        \       int o = counts['o' - 'a'] / 2;\n        int n = counts['n' - 'a'];\n\
        \        return min({b, a, l, o, n});\n    }\n};"
      java: "class Solution {\n    public int maxNumberOfBalloons(String text) {\n \
        \       int[] counts = new int[26];\n        for (int i = 0; i < text.length();\
        \ i++) {\n            counts[text.charAt(i) - 'a']++;\n        }\n        int\
        \ b = counts['b' - 'a'];\n        int a = counts['a' - 'a'];\n        int l\
        \ = counts['l' - 'a'] / 2;\n        int o = counts['o' - 'a'] / 2;\n       \
        \ int n = counts['n' - 'a'];\n\n        int min = b;\n        if (a < min) min\
        \ = a;\n        if (l < min) min = l;\n        if (o < min) min = o;\n     \
        \   if (n < min) min = n;\n\n        return min;\n    }\n}"
      python: "class Solution(object):\n    def maxNumberOfBalloons(self, text):\n \
        \       \"\"\"\n        :type text: str\n        :rtype: int\n        \"\"\"\
        \n        counts = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}\n        for char\
        \ in text:\n            if char in counts:\n                counts[char] +=\
        \ 1\n        return min(counts['b'], counts['a'], counts['l'] // 2, counts['o']\
        \ // 2, counts['n'])"
      python3: "class Solution:\n    def maxNumberOfBalloons(self, text: str) -> int:\n\
        \        b = a = l = o = n = 0\n        for char in text:\n            if char\
        \ == 'b': b += 1\n            elif char == 'a': a += 1\n            elif char\
        \ == 'l': l += 1\n            elif char == 'o': o += 1\n            elif char\
        \ == 'n': n += 1\n        return min(b, a, l // 2, o // 2, n)"
      c: "int maxNumberOfBalloons(char* text) {\n    int counts[26] = {0};\n    for\
        \ (int i = 0; text[i] != '\\0'; i++) {\n        counts[text[i] - 'a']++;\n \
        \   }\n    int b = counts['b' - 'a'];\n    int a = counts['a' - 'a'];\n    int\
        \ l = counts['l' - 'a'] / 2;\n    int o = counts['o' - 'a'] / 2;\n    int n\
        \ = counts['n' - 'a'];\n\n    int min = b;\n    if (a < min) min = a;\n    if\
        \ (l < min) min = l;\n    if (o < min) min = o;\n    if (n < min) min = n;\n\
        \n    return min;\n}"
      csharp: "using System;\n\npublic class Solution {\n    public int MaxNumberOfBalloons(string\
        \ text) {\n        int[] counts = new int[26];\n        foreach (char c in text)\
        \ {\n            counts[c - 'a']++;\n        }\n        int b = counts['b' -\
        \ 'a'];\n        int a = counts['a' - 'a'];\n        int l = counts['l' - 'a']\
        \ / 2;\n        int o = counts['o' - 'a'] / 2;\n        int n = counts['n' -\
        \ 'a'];\n\n        return Math.Min(b, Math.Min(a, Math.Min(l, Math.Min(o, n))));\n\
        \    }\n}"
      javascript: "/**\n * @param {string} text\n * @return {number}\n */\nvar maxNumberOfBalloons\
        \ = function(text) {\n    let b = 0, a = 0, l = 0, o = 0, n = 0;\n    for (let\
        \ i = 0; i < text.length; i++) {\n        const c = text[i];\n        if (c\
        \ === 'b') b++;\n        else if (c === 'a') a++;\n        else if (c === 'l')\
        \ l++;\n        else if (c === 'o') o++;\n        else if (c === 'n') n++;\n\
        \    }\n    return Math.min(b, a, Math.floor(l / 2), Math.floor(o / 2), n);\n\
        };"
      typescript: "function maxNumberOfBalloons(text: string): number {\n    const counts:\
        \ { [key: string]: number } = { b: 0, a: 0, l: 0, o: 0, n: 0 };\n    for (const\
        \ char of text) {\n        if (char in counts) {\n            counts[char]++;\n\
        \        }\n    }\n    return Math.min(\n        counts['b'],\n        counts['a'],\n\
        \        Math.floor(counts['l'] / 2),\n        Math.floor(counts['o'] / 2),\n\
        \        counts['n']\n    );\n};"
      php: "class Solution {\n\n    /**\n     * @param String $text\n     * @return\
        \ Integer\n     */\n    function maxNumberOfBalloons($text) {\n        $counts\
        \ = ['b' => 0, 'a' => 0, 'l' => 0, 'o' => 0, 'n' => 0];\n        $len = strlen($text);\n\
        \        for ($i = 0; $i < $len; $i++) {\n            $char = $text[$i];\n \
        \           if (isset($counts[$char])) {\n                $counts[$char]++;\n\
        \            }\n        }\n        return min(\n            $counts['b'],\n\
        \            $counts['a'],\n            (int)($counts['l'] / 2),\n         \
        \   (int)($counts['o'] / 2),\n            $counts['n']\n        );\n    }\n}"
      swift: "class Solution {\n    func maxNumberOfBalloons(_ text: String) -> Int\
        \ {\n        var counts = [\"b\": 0, \"a\": 0, \"l\": 0, \"o\": 0, \"n\": 0]\n\
        \        for char in text {\n            let s = String(char)\n            if\
        \ let current = counts[s] {\n                counts[s] = current + 1\n     \
        \       }\n        }\n        let b = counts[\"b\"]!\n        let a = counts[\"\
        a\"]!\n        let l = counts[\"l\"]! / 2\n        let o = counts[\"o\"]! /\
        \ 2\n        let n = counts[\"n\"]!\n\n        return min(min(min(b, a), min(l,\
        \ o)), n)\n    }\n}"
      kotlin: "import kotlin.math.min\n\nclass Solution {\n    fun maxNumberOfBalloons(text:\
        \ String): Int {\n        val counts = mutableMapOf('b' to 0, 'a' to 0, 'l'\
        \ to 0, 'o' to 0, 'n' to 0)\n        for (char in text) {\n            if (counts.containsKey(char))\
        \ {\n                counts[char] = counts[char]!! + 1\n            }\n    \
        \    }\n        val b = counts['b']!!\n        val a = counts['a']!!\n     \
        \   val l = counts['l']!! / 2\n        val o = counts['o']!! / 2\n        val\
        \ n = counts['n']!!\n\n        return minOf(b, a, l, o, n)\n    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int maxNumberOfBalloons(String\
        \ text) {\n    Map<String, int> counts = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n':\
        \ 0};\n    for (int i = 0; i < text.length; i++) {\n      String char = text[i];\n\
        \      if (counts.containsKey(char)) {\n        counts[char] = counts[char]!\
        \ + 1;\n      }\n    }\n    List<int> limits = [\n      counts['b']!,\n    \
        \  counts['a']!,\n      counts['l']! ~/ 2,\n      counts['o']! ~/ 2,\n     \
        \ counts['n']!\n    ];\n    return limits.reduce(min);\n  }\n}"
      go: "func maxNumberOfBalloons(text string) int {\n    counts := make(map[rune]int)\n\
        \    for _, char := range text {\n        counts[char]++\n    }\n\n    b :=\
        \ counts['b']\n    a := counts['a']\n    l := counts['l'] / 2\n    o := counts['o']\
        \ / 2\n    n := counts['n']\n\n    res := b\n    if a < res { res = a }\n  \
        \  if l < res { res = l }\n    if o < res { res = o }\n    if n < res { res\
        \ = n }\n\n    return res\n}"
      ruby: "# @param {String} text\n# @return {Integer}\ndef max_number_of_balloons(text)\n\
        \  counts = Hash.new(0)\n  text.each_char { |c| counts[c] += 1 }\n  [\n    counts['b'],\n\
        \    counts['a'],\n    counts['l'] / 2,\n    counts['o'] / 2,\n    counts['n']\n\
        \  ].min\nend"
      scala: "object Solution {\n    def maxNumberOfBalloons(text: String): Int = {\n\
        \        val counts = text.groupBy(identity).map { case (k, v) => k -> v.length\
        \ }\n        List(\n            counts.getOrElse('b', 0),\n            counts.getOrElse('a',\
        \ 0),\n            counts.getOrElse('l', 0) / 2,\n            counts.getOrElse('o',\
        \ 0) / 2,\n            counts.getOrElse('n', 0)\n        ).min\n    }\n}"
      rust: "impl Solution {\n    pub fn max_number_of_balloons(text: String) -> i32\
        \ {\n        let mut counts = [0; 26];\n        for c in text.chars() {\n  \
        \          counts[(c as usize) - ('a' as usize)] += 1;\n        }\n        let\
        \ b = counts[('b' as usize) - ('a' as usize)];\n        let a = counts[('a'\
        \ as usize) - ('a' as usize)];\n        let l = counts[('l' as usize) - ('a'\
        \ as usize)] / 2;\n        let o = counts[('o' as usize) - ('a' as usize)] /\
        \ 2;\n        let n = counts[('n' as usize) - ('a' as usize)];\n\n        *[b,\
        \ a, l, o, n].iter().min().unwrap()\n    }\n}"
      racket: "(define/contract (max-number-of-balloons text)\n  (-> string? exact-integer?)\n\
        \  (let ([counts (make-hash)])\n    (for ([char (in-string text)])\n      (hash-set!\
        \ counts char (add1 (hash-ref counts char 0))))\n    (min (hash-ref counts #\\\
        b 0)\n         (hash-ref counts #\\a 0)\n         (quotient (hash-ref counts\
        \ #\\l 0) 2)\n         (quotient (hash-ref counts #\\o 0) 2)\n         (hash-ref\
        \ counts #\\n 0))))"
      erlang: "-spec max_number_of_balloons(Text :: unicode:unicode_binary()) -> integer().\n\
        max_number_of_balloons(Text) ->\n  Counts = lists:foldl(fun(Char, Map) ->\n\
        \    maps:put(Char, maps:get(Char, Map, 0) + 1, Map)\n  end, #{}, binary_to_list(Text)),\n\
        \  B = maps:get($b, Counts, 0),\n  A = maps:get($a, Counts, 0),\n  L = maps:get($l,\
        \ Counts, 0) div 2,\n  O = maps:get($o, Counts, 0) div 2,\n  N = maps:get($n,\
        \ Counts, 0),\n  lists:min([B, A, L, O, N])."
      elixir: "defmodule Solution do\n  @spec max_number_of_balloons(text :: String.t)\
        \ :: integer\n  def max_number_of_balloons(text) do\n    counts = text\n   \
        \          |> String.graphemes()\n             |> Enum.frequencies()\n\n   \
        \ b = Map.get(counts, \"b\", 0)\n    a = Map.get(counts, \"a\", 0)\n    l =\
        \ div(Map.get(counts, \"l\", 0), 2)\n    o = div(Map.get(counts, \"o\", 0),\
        \ 2)\n    n = Map.get(counts, \"n\", 0)\n\n    Enum.min([b, a, l, o, n])\n \
        \ end\nend"
    approach: 'To solve this problem, we count the frequency of each character in the
      input string that is necessary to form the word "balloon". Specifically, we need
      the letters ''b'', ''a'', ''l'', ''o'', and ''n''. Since the word "balloon" requires
      one ''b'', one ''a'', two ''l''s, two ''o''s, and one ''n'', we store these counts
      in a frequency map or an array of size 26 for efficient access as we iterate through
      the input string once.


      The key intuition is that the maximum number of instances we can form is determined
      by the "bottleneck" character—the character that is least available relative to
      how many are needed for a single word. We take the counts of ''b'', ''a'', and
      ''n'' as they are, and we halve the counts of ''l'' and ''o'' since each word
      requires two of them. The final result is the minimum of these adjusted values,
      which gives the maximum number of complete words that can be constructed.'
    time_complexity: O(N) where N is the length of the string text. We perform a single
      pass over the string to count the character frequencies, and then perform a constant
      number of comparisons to find the minimum of five values.
    space_complexity: O(1) because we only use a fixed-size integer array or hash map
      to store the frequencies of 26 lowercase English letters, which does not depend
      on the size of the input string.
    elapsed_time: 135.3194501399994
    model: gemini-3-flash-preview
    generated_at: '2026-06-22 03:01:19 '
---

## Problem #1189: Maximum Number of Balloons

**Difficulty:** Easy

**Topics:** Hash Table, String, Counting

## Problem Description

<p>Given a string <code>text</code>, you want to use the characters of <code>text</code> to form as many instances of the word <strong>&quot;balloon&quot;</strong> as possible.</p>

<p>You can use each character in <code>text</code> <strong>at most once</strong>. Return the maximum number of instances that can be formed.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/09/05/1536_ex1_upd.JPG" style="width: 132px; height: 35px;" /></strong></p>

<pre>
<strong>Input:</strong> text = &quot;nlaebolko&quot;
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/09/05/1536_ex2_upd.JPG" style="width: 267px; height: 35px;" /></strong></p>

<pre>
<strong>Input:</strong> text = &quot;loonbalxballpoon&quot;
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> text = &quot;leetcode&quot;
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= text.length &lt;= 10<sup>4</sup></code></li>
	<li><code>text</code> consists of lower case English letters only.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as <a href="https://leetcode.com/problems/rearrange-characters-to-make-target-string/description/" target="_blank"> 2287: Rearrange Characters to Make Target String.</a></p>


## Hints

1. Count the frequency of letters in the given string.

2. Find the letter than can make the minimum number of instances of the word "balloon".

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To solve this problem, we count the frequency of each character in the input string that is necessary to form the word "balloon". Specifically, we need the letters 'b', 'a', 'l', 'o', and 'n'. Since the word "balloon" requires one 'b', one 'a', two 'l's, two 'o's, and one 'n', we store these counts in a frequency map or an array of size 26 for efficient access as we iterate through the input string once.

The key intuition is that the maximum number of instances we can form is determined by the "bottleneck" character—the character that is least available relative to how many are needed for a single word. We take the counts of 'b', 'a', and 'n' as they are, and we halve the counts of 'l' and 'o' since each word requires two of them. The final result is the minimum of these adjusted values, which gives the maximum number of complete words that can be constructed.

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
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int maxNumberOfBalloons(string text) {
        int counts[26] = {0};
        for (char c : text) {
            counts[c - 'a']++;
        }
        int b = counts['b' - 'a'];
        int a = counts['a' - 'a'];
        int l = counts['l' - 'a'] / 2;
        int o = counts['o' - 'a'] / 2;
        int n = counts['n' - 'a'];
        return min({b, a, l, o, n});
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maxNumberOfBalloons(String text) {
        int[] counts = new int[26];
        for (int i = 0; i < text.length(); i++) {
            counts[text.charAt(i) - 'a']++;
        }
        int b = counts['b' - 'a'];
        int a = counts['a' - 'a'];
        int l = counts['l' - 'a'] / 2;
        int o = counts['o' - 'a'] / 2;
        int n = counts['n' - 'a'];

        int min = b;
        if (a < min) min = a;
        if (l < min) min = l;
        if (o < min) min = o;
        if (n < min) min = n;

        return min;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        counts = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for char in text:
            if char in counts:
                counts[char] += 1
        return min(counts['b'], counts['a'], counts['l'] // 2, counts['o'] // 2, counts['n'])
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = a = l = o = n = 0
        for char in text:
            if char == 'b': b += 1
            elif char == 'a': a += 1
            elif char == 'l': l += 1
            elif char == 'o': o += 1
            elif char == 'n': n += 1
        return min(b, a, l // 2, o // 2, n)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int maxNumberOfBalloons(char* text) {
    int counts[26] = {0};
    for (int i = 0; text[i] != '\0'; i++) {
        counts[text[i] - 'a']++;
    }
    int b = counts['b' - 'a'];
    int a = counts['a' - 'a'];
    int l = counts['l' - 'a'] / 2;
    int o = counts['o' - 'a'] / 2;
    int n = counts['n' - 'a'];

    int min = b;
    if (a < min) min = a;
    if (l < min) min = l;
    if (o < min) min = o;
    if (n < min) min = n;

    return min;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public int MaxNumberOfBalloons(string text) {
        int[] counts = new int[26];
        foreach (char c in text) {
            counts[c - 'a']++;
        }
        int b = counts['b' - 'a'];
        int a = counts['a' - 'a'];
        int l = counts['l' - 'a'] / 2;
        int o = counts['o' - 'a'] / 2;
        int n = counts['n' - 'a'];

        return Math.Min(b, Math.Min(a, Math.Min(l, Math.Min(o, n))));
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} text
 * @return {number}
 */
var maxNumberOfBalloons = function(text) {
    let b = 0, a = 0, l = 0, o = 0, n = 0;
    for (let i = 0; i < text.length; i++) {
        const c = text[i];
        if (c === 'b') b++;
        else if (c === 'a') a++;
        else if (c === 'l') l++;
        else if (c === 'o') o++;
        else if (c === 'n') n++;
    }
    return Math.min(b, a, Math.floor(l / 2), Math.floor(o / 2), n);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxNumberOfBalloons(text: string): number {
    const counts: { [key: string]: number } = { b: 0, a: 0, l: 0, o: 0, n: 0 };
    for (const char of text) {
        if (char in counts) {
            counts[char]++;
        }
    }
    return Math.min(
        counts['b'],
        counts['a'],
        Math.floor(counts['l'] / 2),
        Math.floor(counts['o'] / 2),
        counts['n']
    );
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String $text
     * @return Integer
     */
    function maxNumberOfBalloons($text) {
        $counts = ['b' => 0, 'a' => 0, 'l' => 0, 'o' => 0, 'n' => 0];
        $len = strlen($text);
        for ($i = 0; $i < $len; $i++) {
            $char = $text[$i];
            if (isset($counts[$char])) {
                $counts[$char]++;
            }
        }
        return min(
            $counts['b'],
            $counts['a'],
            (int)($counts['l'] / 2),
            (int)($counts['o'] / 2),
            $counts['n']
        );
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxNumberOfBalloons(_ text: String) -> Int {
        var counts = ["b": 0, "a": 0, "l": 0, "o": 0, "n": 0]
        for char in text {
            let s = String(char)
            if let current = counts[s] {
                counts[s] = current + 1
            }
        }
        let b = counts["b"]!
        let a = counts["a"]!
        let l = counts["l"]! / 2
        let o = counts["o"]! / 2
        let n = counts["n"]!

        return min(min(min(b, a), min(l, o)), n)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import kotlin.math.min

class Solution {
    fun maxNumberOfBalloons(text: String): Int {
        val counts = mutableMapOf('b' to 0, 'a' to 0, 'l' to 0, 'o' to 0, 'n' to 0)
        for (char in text) {
            if (counts.containsKey(char)) {
                counts[char] = counts[char]!! + 1
            }
        }
        val b = counts['b']!!
        val a = counts['a']!!
        val l = counts['l']!! / 2
        val o = counts['o']!! / 2
        val n = counts['n']!!

        return minOf(b, a, l, o, n)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:math';

class Solution {
  int maxNumberOfBalloons(String text) {
    Map<String, int> counts = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0};
    for (int i = 0; i < text.length; i++) {
      String char = text[i];
      if (counts.containsKey(char)) {
        counts[char] = counts[char]! + 1;
      }
    }
    List<int> limits = [
      counts['b']!,
      counts['a']!,
      counts['l']! ~/ 2,
      counts['o']! ~/ 2,
      counts['n']!
    ];
    return limits.reduce(min);
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxNumberOfBalloons(text string) int {
    counts := make(map[rune]int)
    for _, char := range text {
        counts[char]++
    }

    b := counts['b']
    a := counts['a']
    l := counts['l'] / 2
    o := counts['o'] / 2
    n := counts['n']

    res := b
    if a < res { res = a }
    if l < res { res = l }
    if o < res { res = o }
    if n < res { res = n }

    return res
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} text
# @return {Integer}
def max_number_of_balloons(text)
  counts = Hash.new(0)
  text.each_char { |c| counts[c] += 1 }
  [
    counts['b'],
    counts['a'],
    counts['l'] / 2,
    counts['o'] / 2,
    counts['n']
  ].min
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxNumberOfBalloons(text: String): Int = {
        val counts = text.groupBy(identity).map { case (k, v) => k -> v.length }
        List(
            counts.getOrElse('b', 0),
            counts.getOrElse('a', 0),
            counts.getOrElse('l', 0) / 2,
            counts.getOrElse('o', 0) / 2,
            counts.getOrElse('n', 0)
        ).min
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_number_of_balloons(text: String) -> i32 {
        let mut counts = [0; 26];
        for c in text.chars() {
            counts[(c as usize) - ('a' as usize)] += 1;
        }
        let b = counts[('b' as usize) - ('a' as usize)];
        let a = counts[('a' as usize) - ('a' as usize)];
        let l = counts[('l' as usize) - ('a' as usize)] / 2;
        let o = counts[('o' as usize) - ('a' as usize)] / 2;
        let n = counts[('n' as usize) - ('a' as usize)];

        *[b, a, l, o, n].iter().min().unwrap()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (max-number-of-balloons text)
  (-> string? exact-integer?)
  (let ([counts (make-hash)])
    (for ([char (in-string text)])
      (hash-set! counts char (add1 (hash-ref counts char 0))))
    (min (hash-ref counts #\b 0)
         (hash-ref counts #\a 0)
         (quotient (hash-ref counts #\l 0) 2)
         (quotient (hash-ref counts #\o 0) 2)
         (hash-ref counts #\n 0))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_number_of_balloons(Text :: unicode:unicode_binary()) -> integer().
max_number_of_balloons(Text) ->
  Counts = lists:foldl(fun(Char, Map) ->
    maps:put(Char, maps:get(Char, Map, 0) + 1, Map)
  end, #{}, binary_to_list(Text)),
  B = maps:get($b, Counts, 0),
  A = maps:get($a, Counts, 0),
  L = maps:get($l, Counts, 0) div 2,
  O = maps:get($o, Counts, 0) div 2,
  N = maps:get($n, Counts, 0),
  lists:min([B, A, L, O, N]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_number_of_balloons(text :: String.t) :: integer
  def max_number_of_balloons(text) do
    counts = text
             |> String.graphemes()
             |> Enum.frequencies()

    b = Map.get(counts, "b", 0)
    a = Map.get(counts, "a", 0)
    l = div(Map.get(counts, "l", 0), 2)
    o = div(Map.get(counts, "o", 0), 2)
    n = Map.get(counts, "n", 0)

    Enum.min([b, a, l, o, n])
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) where N is the length of the string text. We perform a single pass over the string to count the character frequencies, and then perform a constant number of comparisons to find the minimum of five values.
- **Space Complexity:** O(1) because we only use a fixed-size integer array or hash map to store the frequencies of 26 lowercase English letters, which does not depend on the size of the input string.
