---
layout: post
title: "Minimum Number of Pushes to Type Word II"
date: 2026-07-31 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Hash Table", "String", "Greedy", "Sorting", "Counting"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minimumPushes(string word) {\n      \
        \  vector<int> freq(26, 0);\n        for (char c : word) {\n            freq[c\
        \ - 'a']++;\n        }\n        sort(freq.rbegin(), freq.rend());\n\n      \
        \  int totalPushes = 0;\n        for (int i = 0; i < 26; i++) {\n          \
        \  if (freq[i] == 0) break;\n            int pushes = (i / 8) + 1;\n       \
        \     totalPushes += freq[i] * pushes;\n        }\n        return totalPushes;\n\
        \    }\n};"
      java: "import java.util.Arrays;\nimport java.util.Collections;\n\nclass Solution\
        \ {\n    public int minimumPushes(String word) {\n        int[] freq = new int[26];\n\
        \        for (char c : word.toCharArray()) {\n            freq[c - 'a']++;\n\
        \        }\n        Arrays.sort(freq);\n\n        int totalPushes = 0;\n   \
        \     int rank = 0;\n        for (int i = 25; i >= 0; i--) {\n            if\
        \ (freq[i] == 0) break;\n            int pushes = (rank / 8) + 1;\n        \
        \    totalPushes += freq[i] * pushes;\n            rank++;\n        }\n    \
        \    return totalPushes;\n    }\n}"
      python: "import collections\n\nclass Solution(object):\n    def minimumPushes(self,\
        \ word):\n        \"\"\"\n        :type word: str\n        :rtype: int\n   \
        \     \"\"\"\n        counts = collections.Counter(word)\n        freqs = sorted(counts.values(),\
        \ reverse=True)\n\n        total_pushes = 0\n        for i, count in enumerate(freqs):\n\
        \            pushes = (i // 8) + 1\n            total_pushes += count * pushes\n\
        \        return total_pushes"
      python3: "import collections\n\nclass Solution:\n    def minimumPushes(self, word:\
        \ str) -> int:\n        counts = collections.Counter(word)\n        freqs =\
        \ sorted(counts.values(), reverse=True)\n\n        total_pushes = 0\n      \
        \  for i, count in enumerate(freqs):\n            pushes = (i // 8) + 1\n  \
        \          total_pushes += count * pushes\n        return total_pushes"
      c: "#include <stdio.h>\n#include <string.h>\n#include <stdlib.h>\n\nint compare(const\
        \ void *a, const void *b) {\n    return (*(int *)b - *(int *)a);\n}\n\nint minimumPushes(char*\
        \ word) {\n    int freq[26] = {0};\n    int len = strlen(word);\n    for (int\
        \ i = 0; i < len; i++) {\n        freq[word[i] - 'a']++;\n    }\n\n    qsort(freq,\
        \ 26, sizeof(int), compare);\n\n    int totalPushes = 0;\n    for (int i = 0;\
        \ i < 26; i++) {\n        if (freq[i] == 0) break;\n        int multiplier =\
        \ (i / 8) + 1;\n        totalPushes += freq[i] * multiplier;\n    }\n\n    return\
        \ totalPushes;\n}"
      csharp: "public class Solution {\n    public int MinimumPushes(string word) {\n\
        \        int[] frequencies = new int[26];\n        foreach (char c in word)\
        \ {\n            frequencies[c - 'a']++;\n        }\n\n        System.Array.Sort(frequencies);\n\
        \        System.Array.Reverse(frequencies);\n\n        int totalPushes = 0;\n\
        \        for (int i = 0; i < 26; i++) {\n            if (frequencies[i] == 0)\
        \ break;\n            int pushCost = (i / 8) + 1;\n            totalPushes +=\
        \ frequencies[i] * pushCost;\n        }\n\n        return totalPushes;\n   \
        \ }\n}"
      javascript: "/**\n * @param {string} word\n * @return {number}\n */\nvar minimumPushes\
        \ = function(word) {\n    const freq = new Array(26).fill(0);\n    for (let\
        \ i = 0; i < word.length; i++) {\n        freq[word.charCodeAt(i) - 97]++;\n\
        \    }\n\n    freq.sort((a, b) => b - a);\n\n    let totalPushes = 0;\n    for\
        \ (let i = 0; i < 26; i++) {\n        if (freq[i] === 0) break;\n        totalPushes\
        \ += freq[i] * (Math.floor(i / 8) + 1);\n    }\n\n    return totalPushes;\n\
        };"
      typescript: "function minimumPushes(word: string): number {\n    const freq: number[]\
        \ = new Array(26).fill(0);\n    for (let i = 0; i < word.length; i++) {\n  \
        \      freq[word.charCodeAt(i) - 97]++;\n    }\n\n    freq.sort((a, b) => b\
        \ - a);\n\n    let totalPushes = 0;\n    for (let i = 0; i < 26; i++) {\n  \
        \      if (freq[i] === 0) break;\n        totalPushes += freq[i] * (Math.floor(i\
        \ / 8) + 1);\n    }\n\n    return totalPushes;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $word\n     * @return\
        \ Integer\n     */\n    function minimumPushes($word) {\n        $freq = array_fill(0,\
        \ 26, 0);\n        $n = strlen($word);\n        for ($i = 0; $i < $n; $i++)\
        \ {\n            $freq[ord($word[$i]) - ord('a')]++;\n        }\n\n        rsort($freq);\n\
        \n        $totalPushes = 0;\n        for ($i = 0; $i < 26; $i++) {\n       \
        \     if ($freq[$i] == 0) break;\n            $pushCost = intval($i / 8) + 1;\n\
        \            $totalPushes += $freq[$i] * $pushCost;\n        }\n\n        return\
        \ $totalPushes;\n    }\n}"
      swift: "class Solution {\n    func minimumPushes(_ word: String) -> Int {\n  \
        \      var freq = [Int](repeating: 0, count: 26)\n        let aAscii = Character(\"\
        a\").asciiValue!\n\n        for char in word {\n            let index = Int(char.asciiValue!\
        \ - aAscii)\n            freq[index] += 1\n        }\n\n        freq.sort(by:\
        \ >)\n\n        var totalPushes = 0\n        for i in 0..<26 {\n           \
        \ if freq[i] == 0 { break }\n            let pushCost = (i / 8) + 1\n      \
        \      totalPushes += freq[i] * pushCost\n        }\n\n        return totalPushes\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun minimumPushes(word: String): Int {\n      \
        \  val freq = IntArray(26)\n        for (char in word) {\n            freq[char\
        \ - 'a']++\n        }\n        freq.sortDescending()\n        var totalPushes\
        \ = 0\n        for (i in 0 until 26) {\n            if (freq[i] == 0) break\n\
        \            totalPushes += freq[i] * ((i / 8) + 1)\n        }\n        return\
        \ totalPushes\n    }\n}"
      dart: "class Solution {\n  int minimumPushes(String word) {\n    List<int> freq\
        \ = List.filled(26, 0);\n    for (int i = 0; i < word.length; i++) {\n     \
        \ freq[word.codeUnitAt(i) - 97]++;\n    }\n    freq.sort((a, b) => b.compareTo(a));\n\
        \    int totalPushes = 0;\n    for (int i = 0; i < 26; i++) {\n      if (freq[i]\
        \ == 0) break;\n      totalPushes += freq[i] * ((i ~/ 8) + 1);\n    }\n    return\
        \ totalPushes;\n  }\n}"
      go: "import \"sort\"\n\nfunc minimumPushes(word string) int {\n\tfreq := make([]int,\
        \ 26)\n\tfor _, char := range word {\n\t\tfreq[char-'a']++\n\t}\n\tsort.Slice(freq,\
        \ func(i, j int) bool {\n\t\treturn freq[i] > freq[j]\n\t})\n\ttotalPushes :=\
        \ 0\n\tfor i := 0; i < 26; i++ {\n\t\tif freq[i] == 0 {\n\t\t\tbreak\n\t\t}\n\
        \t\ttotalPushes += freq[i] * ((i / 8) + 1)\n\t}\n\treturn totalPushes\n}"
      ruby: "# @param {String} word\n# @return {Integer}\ndef minimum_pushes(word)\n\
        \  freq = Array.new(26, 0)\n  word.each_char { |char| freq[char.ord - 97] +=\
        \ 1 }\n  freq.sort!.reverse!\n  total_pushes = 0\n  freq.each_with_index do\
        \ |f, i|\n    break if f == 0\n    total_pushes += f * ((i / 8) + 1)\n  end\n\
        \  total_pushes\nend"
      scala: "object Solution {\n    def minimumPushes(word: String): Int = {\n    \
        \    val freq = new Array[Int](26)\n        word.foreach(c => freq(c - 'a')\
        \ += 1)\n        val sortedFreq = freq.sorted.reverse\n        var totalPushes\
        \ = 0\n        var i = 0\n        while (i < 26 && sortedFreq(i) > 0) {\n  \
        \          totalPushes += sortedFreq(i) * ((i / 8) + 1)\n            i += 1\n\
        \        }\n        totalPushes\n    }\n}"
      rust: "impl Solution {\n    pub fn minimum_pushes(word: String) -> i32 {\n   \
        \     let mut freq = [0; 26];\n        for &b in word.as_bytes() {\n       \
        \     freq[(b - b'a') as usize] += 1;\n        }\n        freq.sort_unstable_by(|a,\
        \ b| b.cmp(a));\n        let mut ans = 0;\n        for i in 0..26 {\n      \
        \      if freq[i] == 0 {\n                break;\n            }\n          \
        \  ans += freq[i] * (i as i32 / 8 + 1);\n        }\n        ans\n    }\n}"
      racket: "(define/contract (minimum-pushes word)\n  (-> string? exact-integer?)\n\
        \  (let* ([counts (make-vector 26 0)]\n         [chars (string->list word)])\n\
        \    (for ([c chars])\n      (let ([idx (- (char->integer c) (char->integer\
        \ #\\a))])\n        (vector-set! counts idx (+ (vector-ref counts idx) 1))))\n\
        \    (let ([sorted-counts (sort (vector->list counts) >)])\n      (for/sum ([f\
        \ sorted-counts]\n                [i (in-range 26)])\n        (* f (+ (quotient\
        \ i 8) 1))))))"
      erlang: "-spec minimum_pushes(Word :: unicode:unicode_binary()) -> integer().\n\
        minimum_pushes(Word) ->\n    Chars = binary_to_list(Word),\n    FreqMap = lists:foldl(fun(C,\
        \ Acc) ->\n        Count = maps:get(C, Acc, 0),\n        Acc#{C => Count + 1}\n\
        \    end, #{}, Chars),\n    Freqs = maps:values(FreqMap),\n    SortedFreqs =\
        \ lists:reverse(lists:sort(Freqs)),\n    {Total, _} = lists:foldl(fun(F, {AccSum,\
        \ Index}) ->\n        Pushes = (Index div 8) + 1,\n        {AccSum + (F * Pushes),\
        \ Index + 1}\n    end, {0, 0}, SortedFreqs),\n    Total."
      elixir: "defmodule Solution do\n  @spec minimum_pushes(word :: String.t) :: integer\n\
        \  def minimum_pushes(word) do\n    word\n    |> String.to_charlist()\n    |>\
        \ Enum.frequencies()\n    |> Map.values()\n    |> Enum.sort(:desc)\n    |> Enum.with_index()\n\
        \    |> Enum.reduce(0, fn {f, i}, acc ->\n      acc + f * (div(i, 8) + 1)\n\
        \    end)\n  end\nend"
    approach: 'The problem asks to minimize the total number of key pushes by remapping
      characters to 8 available keys (numbered 2-9). To achieve the minimum cost, a
      greedy strategy is applied: letters with the highest frequency in the input string
      should be assigned to positions that require the fewest pushes. Since there are
      8 keys, each of the 8 most frequent characters can be assigned as the first letter
      on a unique key, costing 1 push per occurrence. The next 8 most frequent characters
      are assigned as the second letter on each key, costing 2 pushes per occurrence,
      and so on.


      We start by calculating the frequency of each character in the string. These frequencies
      are then sorted in descending order to prioritize high-frequency characters for
      the 1st position on the keys. We iterate through the sorted list and for each
      character at index $i$, the number of pushes required is $(i // 8) + 1$. The total
      cost is the sum of (frequency * pushes) for all characters present in the string.
      This ensures that character placement is optimized to minimize the global sum
      of button presses.'
    time_complexity: O(N) where N is the length of the string 'word'. Frequency counting
      takes O(N) time. Sorting the fixed-size frequency array of 26 letters takes O(26
      log 26), which is effectively O(1). Thus, the overall time complexity is dominated
      by the linear scan of the input string.
    space_complexity: O(1) because we use an array of size 26 to store character frequencies,
      which is a constant space requirement regardless of the input size.
    elapsed_time: 69.8568205833435
    model: gemini-3-flash-preview
    generated_at: '2026-07-31 02:04:45 '
---

## Problem #3016: Minimum Number of Pushes to Type Word II

**Difficulty:** Medium

**Topics:** Hash Table, String, Greedy, Sorting, Counting

## Problem Description

<p>You are given a string <code>word</code> containing lowercase English letters.</p>

<p>Telephone keypads have keys mapped with <strong>distinct</strong> collections of lowercase English letters, which can be used to form words by pushing them. For example, the key <code>2</code> is mapped with <code>[&quot;a&quot;,&quot;b&quot;,&quot;c&quot;]</code>, we need to push the key one time to type <code>&quot;a&quot;</code>, two times to type <code>&quot;b&quot;</code>, and three times to type <code>&quot;c&quot;</code> <em>.</em></p>

<p>It is allowed to remap the keys numbered <code>2</code> to <code>9</code> to <strong>distinct</strong> collections of letters. The keys can be remapped to <strong>any</strong> amount of letters, but each letter <strong>must</strong> be mapped to <strong>exactly</strong> one key. You need to find the <strong>minimum</strong> number of times the keys will be pushed to type the string <code>word</code>.</p>

<p>Return <em>the <strong>minimum</strong> number of pushes needed to type </em><code>word</code> <em>after remapping the keys</em>.</p>

<p>An example mapping of letters to keys on a telephone keypad is given below. Note that <code>1</code>, <code>*</code>, <code>#</code>, and <code>0</code> do <strong>not</strong> map to any letters.</p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/12/26/keypaddesc.png" style="width: 329px; height: 313px;" />
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/12/26/keypadv1e1.png" style="width: 329px; height: 313px;" />
<pre>
<strong>Input:</strong> word = &quot;abcde&quot;
<strong>Output:</strong> 5
<strong>Explanation:</strong> The remapped keypad given in the image provides the minimum cost.
&quot;a&quot; -&gt; one push on key 2
&quot;b&quot; -&gt; one push on key 3
&quot;c&quot; -&gt; one push on key 4
&quot;d&quot; -&gt; one push on key 5
&quot;e&quot; -&gt; one push on key 6
Total cost is 1 + 1 + 1 + 1 + 1 = 5.
It can be shown that no other mapping can provide a lower cost.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/08/20/edited.png" style="width: 329px; height: 313px;" />
<pre>
<strong>Input:</strong> word = &quot;xyzxyzxyzxyz&quot;
<strong>Output:</strong> 12
<strong>Explanation:</strong> The remapped keypad given in the image provides the minimum cost.
&quot;x&quot; -&gt; one push on key 2
&quot;y&quot; -&gt; one push on key 3
&quot;z&quot; -&gt; one push on key 4
Total cost is 1 * 4 + 1 * 4 + 1 * 4 = 12
It can be shown that no other mapping can provide a lower cost.
Note that the key 9 is not mapped to any letter: it is not necessary to map letters to every key, but to map all the letters.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/12/27/keypadv2.png" style="width: 329px; height: 313px;" />
<pre>
<strong>Input:</strong> word = &quot;aabbccddeeffgghhiiiiii&quot;
<strong>Output:</strong> 24
<strong>Explanation:</strong> The remapped keypad given in the image provides the minimum cost.
&quot;a&quot; -&gt; one push on key 2
&quot;b&quot; -&gt; one push on key 3
&quot;c&quot; -&gt; one push on key 4
&quot;d&quot; -&gt; one push on key 5
&quot;e&quot; -&gt; one push on key 6
&quot;f&quot; -&gt; one push on key 7
&quot;g&quot; -&gt; one push on key 8
&quot;h&quot; -&gt; two pushes on key 9
&quot;i&quot; -&gt; one push on key 9
Total cost is 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 2 * 2 + 6 * 1 = 24.
It can be shown that no other mapping can provide a lower cost.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 10<sup>5</sup></code></li>
	<li><code>word</code> consists of lowercase English letters.</li>
</ul>


## Hints

1. We have 8 keys in total. We can type 8 characters with one push each, 8 different characters with two pushes each, and so on.

2. The optimal way is to map letters to keys evenly.

3. Sort the letters by frequencies in the word in non-increasing order.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks to minimize the total number of key pushes by remapping characters to 8 available keys (numbered 2-9). To achieve the minimum cost, a greedy strategy is applied: letters with the highest frequency in the input string should be assigned to positions that require the fewest pushes. Since there are 8 keys, each of the 8 most frequent characters can be assigned as the first letter on a unique key, costing 1 push per occurrence. The next 8 most frequent characters are assigned as the second letter on each key, costing 2 pushes per occurrence, and so on.

We start by calculating the frequency of each character in the string. These frequencies are then sorted in descending order to prioritize high-frequency characters for the 1st position on the keys. We iterate through the sorted list and for each character at index $i$, the number of pushes required is $(i // 8) + 1$. The total cost is the sum of (frequency * pushes) for all characters present in the string. This ensures that character placement is optimized to minimize the global sum of button presses.

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
    int minimumPushes(string word) {
        vector<int> freq(26, 0);
        for (char c : word) {
            freq[c - 'a']++;
        }
        sort(freq.rbegin(), freq.rend());

        int totalPushes = 0;
        for (int i = 0; i < 26; i++) {
            if (freq[i] == 0) break;
            int pushes = (i / 8) + 1;
            totalPushes += freq[i] * pushes;
        }
        return totalPushes;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.Arrays;
import java.util.Collections;

class Solution {
    public int minimumPushes(String word) {
        int[] freq = new int[26];
        for (char c : word.toCharArray()) {
            freq[c - 'a']++;
        }
        Arrays.sort(freq);

        int totalPushes = 0;
        int rank = 0;
        for (int i = 25; i >= 0; i--) {
            if (freq[i] == 0) break;
            int pushes = (rank / 8) + 1;
            totalPushes += freq[i] * pushes;
            rank++;
        }
        return totalPushes;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import collections

class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        counts = collections.Counter(word)
        freqs = sorted(counts.values(), reverse=True)

        total_pushes = 0
        for i, count in enumerate(freqs):
            pushes = (i // 8) + 1
            total_pushes += count * pushes
        return total_pushes
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import collections

class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = collections.Counter(word)
        freqs = sorted(counts.values(), reverse=True)

        total_pushes = 0
        for i, count in enumerate(freqs):
            pushes = (i // 8) + 1
            total_pushes += count * pushes
        return total_pushes
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return (*(int *)b - *(int *)a);
}

int minimumPushes(char* word) {
    int freq[26] = {0};
    int len = strlen(word);
    for (int i = 0; i < len; i++) {
        freq[word[i] - 'a']++;
    }

    qsort(freq, 26, sizeof(int), compare);

    int totalPushes = 0;
    for (int i = 0; i < 26; i++) {
        if (freq[i] == 0) break;
        int multiplier = (i / 8) + 1;
        totalPushes += freq[i] * multiplier;
    }

    return totalPushes;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinimumPushes(string word) {
        int[] frequencies = new int[26];
        foreach (char c in word) {
            frequencies[c - 'a']++;
        }

        System.Array.Sort(frequencies);
        System.Array.Reverse(frequencies);

        int totalPushes = 0;
        for (int i = 0; i < 26; i++) {
            if (frequencies[i] == 0) break;
            int pushCost = (i / 8) + 1;
            totalPushes += frequencies[i] * pushCost;
        }

        return totalPushes;
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
var minimumPushes = function(word) {
    const freq = new Array(26).fill(0);
    for (let i = 0; i < word.length; i++) {
        freq[word.charCodeAt(i) - 97]++;
    }

    freq.sort((a, b) => b - a);

    let totalPushes = 0;
    for (let i = 0; i < 26; i++) {
        if (freq[i] === 0) break;
        totalPushes += freq[i] * (Math.floor(i / 8) + 1);
    }

    return totalPushes;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimumPushes(word: string): number {
    const freq: number[] = new Array(26).fill(0);
    for (let i = 0; i < word.length; i++) {
        freq[word.charCodeAt(i) - 97]++;
    }

    freq.sort((a, b) => b - a);

    let totalPushes = 0;
    for (let i = 0; i < 26; i++) {
        if (freq[i] === 0) break;
        totalPushes += freq[i] * (Math.floor(i / 8) + 1);
    }

    return totalPushes;
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
    function minimumPushes($word) {
        $freq = array_fill(0, 26, 0);
        $n = strlen($word);
        for ($i = 0; $i < $n; $i++) {
            $freq[ord($word[$i]) - ord('a')]++;
        }

        rsort($freq);

        $totalPushes = 0;
        for ($i = 0; $i < 26; $i++) {
            if ($freq[$i] == 0) break;
            $pushCost = intval($i / 8) + 1;
            $totalPushes += $freq[$i] * $pushCost;
        }

        return $totalPushes;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minimumPushes(_ word: String) -> Int {
        var freq = [Int](repeating: 0, count: 26)
        let aAscii = Character("a").asciiValue!

        for char in word {
            let index = Int(char.asciiValue! - aAscii)
            freq[index] += 1
        }

        freq.sort(by: >)

        var totalPushes = 0
        for i in 0..<26 {
            if freq[i] == 0 { break }
            let pushCost = (i / 8) + 1
            totalPushes += freq[i] * pushCost
        }

        return totalPushes
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minimumPushes(word: String): Int {
        val freq = IntArray(26)
        for (char in word) {
            freq[char - 'a']++
        }
        freq.sortDescending()
        var totalPushes = 0
        for (i in 0 until 26) {
            if (freq[i] == 0) break
            totalPushes += freq[i] * ((i / 8) + 1)
        }
        return totalPushes
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minimumPushes(String word) {
    List<int> freq = List.filled(26, 0);
    for (int i = 0; i < word.length; i++) {
      freq[word.codeUnitAt(i) - 97]++;
    }
    freq.sort((a, b) => b.compareTo(a));
    int totalPushes = 0;
    for (int i = 0; i < 26; i++) {
      if (freq[i] == 0) break;
      totalPushes += freq[i] * ((i ~/ 8) + 1);
    }
    return totalPushes;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "sort"

func minimumPushes(word string) int {
	freq := make([]int, 26)
	for _, char := range word {
		freq[char-'a']++
	}
	sort.Slice(freq, func(i, j int) bool {
		return freq[i] > freq[j]
	})
	totalPushes := 0
	for i := 0; i < 26; i++ {
		if freq[i] == 0 {
			break
		}
		totalPushes += freq[i] * ((i / 8) + 1)
	}
	return totalPushes
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} word
# @return {Integer}
def minimum_pushes(word)
  freq = Array.new(26, 0)
  word.each_char { |char| freq[char.ord - 97] += 1 }
  freq.sort!.reverse!
  total_pushes = 0
  freq.each_with_index do |f, i|
    break if f == 0
    total_pushes += f * ((i / 8) + 1)
  end
  total_pushes
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minimumPushes(word: String): Int = {
        val freq = new Array[Int](26)
        word.foreach(c => freq(c - 'a') += 1)
        val sortedFreq = freq.sorted.reverse
        var totalPushes = 0
        var i = 0
        while (i < 26 && sortedFreq(i) > 0) {
            totalPushes += sortedFreq(i) * ((i / 8) + 1)
            i += 1
        }
        totalPushes
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn minimum_pushes(word: String) -> i32 {
        let mut freq = [0; 26];
        for &b in word.as_bytes() {
            freq[(b - b'a') as usize] += 1;
        }
        freq.sort_unstable_by(|a, b| b.cmp(a));
        let mut ans = 0;
        for i in 0..26 {
            if freq[i] == 0 {
                break;
            }
            ans += freq[i] * (i as i32 / 8 + 1);
        }
        ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (minimum-pushes word)
  (-> string? exact-integer?)
  (let* ([counts (make-vector 26 0)]
         [chars (string->list word)])
    (for ([c chars])
      (let ([idx (- (char->integer c) (char->integer #\a))])
        (vector-set! counts idx (+ (vector-ref counts idx) 1))))
    (let ([sorted-counts (sort (vector->list counts) >)])
      (for/sum ([f sorted-counts]
                [i (in-range 26)])
        (* f (+ (quotient i 8) 1))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec minimum_pushes(Word :: unicode:unicode_binary()) -> integer().
minimum_pushes(Word) ->
    Chars = binary_to_list(Word),
    FreqMap = lists:foldl(fun(C, Acc) ->
        Count = maps:get(C, Acc, 0),
        Acc#{C => Count + 1}
    end, #{}, Chars),
    Freqs = maps:values(FreqMap),
    SortedFreqs = lists:reverse(lists:sort(Freqs)),
    {Total, _} = lists:foldl(fun(F, {AccSum, Index}) ->
        Pushes = (Index div 8) + 1,
        {AccSum + (F * Pushes), Index + 1}
    end, {0, 0}, SortedFreqs),
    Total.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_pushes(word :: String.t) :: integer
  def minimum_pushes(word) do
    word
    |> String.to_charlist()
    |> Enum.frequencies()
    |> Map.values()
    |> Enum.sort(:desc)
    |> Enum.with_index()
    |> Enum.reduce(0, fn {f, i}, acc ->
      acc + f * (div(i, 8) + 1)
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) where N is the length of the string 'word'. Frequency counting takes O(N) time. Sorting the fixed-size frequency array of 26 letters takes O(26 log 26), which is effectively O(1). Thus, the overall time complexity is dominated by the linear scan of the input string.
- **Space Complexity:** O(1) because we use an array of size 26 to store character frequencies, which is a constant space requirement regardless of the input size.
