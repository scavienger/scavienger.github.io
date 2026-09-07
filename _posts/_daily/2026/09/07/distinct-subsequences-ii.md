---
layout: post
title: "Distinct Subsequences II"
date: 2026-09-07 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["String", "Dynamic Programming"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/distinct-subsequences-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int distinctSubseqII(string s) {\n      \
        \  long long total = 0;\n        long long MOD = 1e9 + 7;\n        long long\
        \ endsWith[26] = {0};\n\n        for (char c : s) {\n            int idx = c\
        \ - 'a';\n            long long prevCountEndingWithC = endsWith[idx];\n    \
        \        endsWith[idx] = (total + 1) % MOD;\n            total = (total + endsWith[idx]\
        \ - prevCountEndingWithC + MOD) % MOD;\n        }\n\n        return (int)total;\n\
        \    }\n};"
      java: "class Solution {\n    public int distinctSubseqII(String s) {\n       \
        \ long total = 0;\n        long MOD = 1_000_000_007;\n        long[] endsWith\
        \ = new long[26];\n\n        for (int i = 0; i < s.length(); i++) {\n      \
        \      int idx = s.charAt(i) - 'a';\n            long prevCountEndingWithC =\
        \ endsWith[idx];\n            endsWith[idx] = (total + 1) % MOD;\n         \
        \   total = (total + endsWith[idx] - prevCountEndingWithC + MOD) % MOD;\n  \
        \      }\n\n        return (int)total;\n    }\n}"
      python: "class Solution(object):\n    def distinctSubseqII(self, s):\n       \
        \ \"\"\"\n        :type s: str\n        :rtype: int\n        \"\"\"\n      \
        \  MOD = 10**9 + 7\n        total = 0\n        ends_with = [0] * 26\n\n    \
        \    for char in s:\n            idx = ord(char) - ord('a')\n            prev_count_ending_with_c\
        \ = ends_with[idx]\n            new_count_ending_with_c = (total + 1) % MOD\n\
        \            total = (total + new_count_ending_with_c - prev_count_ending_with_c\
        \ + MOD) % MOD\n            ends_with[idx] = new_count_ending_with_c\n\n   \
        \     return total"
      python3: "class Solution:\n    def distinctSubseqII(self, s: str) -> int:\n  \
        \      MOD = 1000000007\n        ends_with = [0] * 26\n        total = 0\n \
        \       for char in s:\n            idx = ord(char) - ord('a')\n           \
        \ new_ends_with_idx = (total + 1) % MOD\n            total = (total - ends_with[idx]\
        \ + new_ends_with_idx + MOD) % MOD\n            ends_with[idx] = new_ends_with_idx\n\
        \        return total"
      c: "int distinctSubseqII(char* s) {\n    long long ends_with[26] = {0};\n    long\
        \ long total = 0;\n    long long MOD = 1000000007;\n    for (int i = 0; s[i]\
        \ != '\\0'; i++) {\n        int idx = s[i] - 'a';\n        long long new_ends_with_idx\
        \ = (total + 1) % MOD;\n        total = (total - ends_with[idx] + new_ends_with_idx\
        \ + MOD) % MOD;\n        ends_with[idx] = new_ends_with_idx;\n    }\n    return\
        \ (int)total;\n}"
      csharp: "public class Solution {\n    public int DistinctSubseqII(string s) {\n\
        \        long[] endsWith = new long[26];\n        long total = 0;\n        long\
        \ mod = 1000000007;\n        foreach (char c in s) {\n            int idx =\
        \ c - 'a';\n            long newEndsWithIdx = (total + 1) % mod;\n         \
        \   total = (total - endsWith[idx] + newEndsWithIdx + mod) % mod;\n        \
        \    endsWith[idx] = newEndsWithIdx;\n        }\n        return (int)total;\n\
        \    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {number}\n */\nvar distinctSubseqII\
        \ = function(s) {\n    const MOD = 1000000007;\n    let endsWith = new Array(26).fill(0);\n\
        \    let total = 0;\n    for (let i = 0; i < s.length; i++) {\n        let idx\
        \ = s.charCodeAt(i) - 97;\n        let newEndsWithIdx = (total + 1) % MOD;\n\
        \        total = (total - endsWith[idx] + newEndsWithIdx + MOD) % MOD;\n   \
        \     endsWith[idx] = newEndsWithIdx;\n    }\n    return total;\n};"
      typescript: "function distinctSubseqII(s: string): number {\n    const MOD = 1000000007;\n\
        \    const ends = new Int32Array(26);\n    let total = 0;\n    for (let i =\
        \ 0; i < s.length; i++) {\n        const charIdx = s.charCodeAt(i) - 97;\n \
        \       const added = (total + 1) % MOD;\n        const nextTotal = (total +\
        \ added) % MOD;\n        total = (nextTotal - ends[charIdx] + MOD) % MOD;\n\
        \        ends[charIdx] = added;\n    }\n    return total;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return Integer\n\
        \     */\n    function distinctSubseqII($s) {\n        $MOD = 1000000007;\n\
        \        $ends = array_fill(0, 26, 0);\n        $total = 0;\n        $n = strlen($s);\n\
        \        for ($i = 0; $i < $n; $i++) {\n            $charIdx = ord($s[$i]) -\
        \ 97;\n            $added = ($total + 1) % $MOD;\n            $nextTotal = ($total\
        \ + $added) % $MOD;\n            $total = ($nextTotal - $ends[$charIdx] + $MOD)\
        \ % $MOD;\n            $ends[$charIdx] = $added;\n        }\n        return\
        \ $total;\n    }\n}"
      swift: "class Solution {\n    func distinctSubseqII(_ s: String) -> Int {\n  \
        \      let MOD = 1_000_000_007\n        var ends = [Int](repeating: 0, count:\
        \ 26)\n        var total = 0\n        for charByte in s.utf8 {\n           \
        \ let charIdx = Int(charByte) - 97\n            let added = (total + 1) % MOD\n\
        \            let nextTotal = (total + added) % MOD\n            total = (nextTotal\
        \ - ends[charIdx] + MOD) % MOD\n            ends[charIdx] = added\n        }\n\
        \        return total\n    }\n}"
      kotlin: "class Solution {\n    fun distinctSubseqII(s: String): Int {\n      \
        \  val MOD = 1000000007\n        val ends = IntArray(26)\n        var total\
        \ = 0\n        for (char in s) {\n            val charIdx = char - 'a'\n   \
        \         val added = (total + 1) % MOD\n            val nextTotal = (total\
        \ + added) % MOD\n            total = (nextTotal - ends[charIdx] + MOD) % MOD\n\
        \            ends[charIdx] = added\n        }\n        return total\n    }\n\
        }"
      dart: "class Solution {\n  int distinctSubseqII(String s) {\n    int mod = 1000000007;\n\
        \    List<int> added = List.filled(26, 0);\n    int totalSum = 0;\n    for (int\
        \ i = 0; i < s.length; i++) {\n      int charIdx = s.codeUnitAt(i) - 97;\n \
        \     int oldAdded = added[charIdx];\n      int newAdded = (totalSum + 1) %\
        \ mod;\n      added[charIdx] = newAdded;\n      totalSum = (totalSum - oldAdded\
        \ + newAdded + mod) % mod;\n    }\n    return totalSum;\n  }\n}"
      go: "func distinctSubseqII(s string) int {\n    const mod = 1000000007\n    added\
        \ := [26]int{}\n    totalSum := 0\n    for i := 0; i < len(s); i++ {\n     \
        \   charIdx := int(s[i] - 'a')\n        oldAdded := added[charIdx]\n       \
        \ newAdded := (totalSum + 1) % mod\n        added[charIdx] = newAdded\n    \
        \    totalSum = (totalSum - oldAdded + newAdded + mod) % mod\n    }\n    return\
        \ totalSum\n}"
      ruby: "# @param {String} s\n# @return {Integer}\ndef distinct_subseq_ii(s)\n \
        \ mod = 1_000_000_007\n  added = Array.new(26, 0)\n  total_sum = 0\n  s.each_char\
        \ do |char|\n    char_idx = char.ord - 97\n    old_added = added[char_idx]\n\
        \    new_added = (total_sum + 1) % mod\n    added[char_idx] = new_added\n  \
        \  total_sum = (total_sum - old_added + new_added + mod) % mod\n  end\n  total_sum\n\
        end"
      scala: "object Solution {\n    def distinctSubseqII(s: String): Int = {\n    \
        \    val mod = 1000000007\n        val added = Array.fill(26)(0L)\n        var\
        \ totalSum = 0L\n        for (c <- s) {\n            val charIdx = c - 'a'\n\
        \            val oldAdded = added(charIdx)\n            val newAdded = (totalSum\
        \ + 1) % mod\n            added(charIdx) = newAdded\n            totalSum =\
        \ (totalSum - oldAdded + newAdded + mod) % mod\n        }\n        totalSum.toInt\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn distinct_subseq_ii(s: String) -> i32 {\n  \
        \      let m: i64 = 1_000_000_007;\n        let mut last_added = [0i64; 26];\n\
        \        let mut total: i64 = 1;\n        for &b in s.as_bytes() {\n       \
        \     let idx = (b - b'a') as usize;\n            let prev_total = last_added[idx];\n\
        \            let added = (total - prev_total + m) % m;\n            last_added[idx]\
        \ = total;\n            total = (total + added) % m;\n        }\n        ((total\
        \ - 1 + m) % m) as i32\n    }\n}"
      racket: "(define/contract (distinct-subseq-ii s)\n  (-> string? exact-integer?)\n\
        \  (let ([mod 1000000007]\n        [dp (make-vector 26 0)])\n    (let ([final-total\n\
        \           (for/fold ([total 1])\n                     ([c (in-string s)])\n\
        \             (let* ([idx (- (char->integer c) (char->integer #\\a))]\n    \
        \                [prev-total (vector-ref dp idx)]\n                    [added\
        \ (modulo (- total prev-total) mod)]\n                    [new-total (modulo\
        \ (+ total added) mod)])\n               (vector-set! dp idx total)\n      \
        \         new-total))])\n      (modulo (- final-total 1) mod))))"
      erlang: "-spec distinct_subseq_ii(S :: unicode:unicode_binary()) -> integer().\n\
        distinct_subseq_ii(S) ->\n    Mod = 1000000007,\n    Chars = binary_to_list(S),\n\
        \    {FinalTotal, _} = lists:foldl(\n        fn(Char, {Total, LA}) ->\n    \
        \        PrevTotal = maps:get(Char, LA, 0),\n            Added = (Total - PrevTotal\
        \ + Mod) rem Mod,\n            NewTotal = (Total + Added) rem Mod,\n       \
        \     {NewTotal, maps:put(Char, Total, LA)}\n        end,\n        {1, #{}},\n\
        \        Chars\n    ),\n    (FinalTotal - 1 + Mod) rem Mod."
      elixir: "defmodule Solution do\n  @spec distinct_subseq_ii(s :: String.t) :: integer\n\
        \  def distinct_subseq_ii(s) do\n    mod = 1_000_000_007\n    {final_total,\
        \ _} = s\n      |> String.to_charlist()\n      |> Enum.reduce({1, %{}}, fn char,\
        \ {total, last_added} ->\n        prev_total = Map.get(last_added, char, 0)\n\
        \        added = Integer.mod(total - prev_total, mod)\n        new_total = Integer.mod(total\
        \ + added, mod)\n        {new_total, Map.put(last_added, char, total)}\n   \
        \   end)\n    Integer.mod(final_total - 1, mod)\n  end\nend"
    approach: 'The algorithm uses dynamic programming to efficiently count distinct
      non-empty subsequences by tracking the number of unique subsequences that end
      with each of the 26 lowercase English characters. As we iterate through the input
      string, any existing subsequence can be extended by the current character to form
      a new distinct subsequence. Additionally, the character itself forms a new single-letter
      subsequence. The total number of unique subsequences ending in the current character
      is therefore the sum of all previously counted distinct subsequences plus one.


      To maintain the global total of distinct subsequences without duplicates, we update
      a running total by adding the newly generated subsequences and subtracting the
      count of subsequences that previously ended with the same character. This subtraction
      step effectively removes duplicates that would have been counted multiple times.
      By applying modulo 10^9 + 7 at each arithmetic step, we ensure the numbers remain
      within bounds while calculating the final result in linear time and constant extra
      space.'
    time_complexity: O(N), where N is the length of the string s. The algorithm performs
      a single pass through the input string, and for each character, it executes a
      constant number of arithmetic operations and updates a fixed-size array.
    space_complexity: O(1) because we only store an array of size 26 to keep track of
      the counts for each lowercase English letter. The space used is independent of
      the input string length N.
    elapsed_time: 773.2870049476624
    model: gemini-3-flash-preview
    generated_at: '2026-09-07 02:22:57 '
---

## Problem #940: Distinct Subsequences II

**Difficulty:** Hard

**Topics:** String, Dynamic Programming

## Problem Description

<p>Given a string s, return <em>the number of <strong>distinct non-empty subsequences</strong> of</em> <code>s</code>. Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>
A <strong>subsequence</strong> of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., <code>&quot;ace&quot;</code> is a subsequence of <code>&quot;<u>a</u>b<u>c</u>d<u>e</u>&quot;</code> while <code>&quot;aec&quot;</code> is not.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abc&quot;
<strong>Output:</strong> 7
<strong>Explanation:</strong> The 7 distinct subsequences are &quot;a&quot;, &quot;b&quot;, &quot;c&quot;, &quot;ab&quot;, &quot;ac&quot;, &quot;bc&quot;, and &quot;abc&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aba&quot;
<strong>Output:</strong> 6
<strong>Explanation:</strong> The 6 distinct subsequences are &quot;a&quot;, &quot;b&quot;, &quot;ab&quot;, &quot;aa&quot;, &quot;ba&quot;, and &quot;aba&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aaa&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The 3 distinct subsequences are &quot;a&quot;, &quot;aa&quot; and &quot;aaa&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2000</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm uses dynamic programming to efficiently count distinct non-empty subsequences by tracking the number of unique subsequences that end with each of the 26 lowercase English characters. As we iterate through the input string, any existing subsequence can be extended by the current character to form a new distinct subsequence. Additionally, the character itself forms a new single-letter subsequence. The total number of unique subsequences ending in the current character is therefore the sum of all previously counted distinct subsequences plus one.

To maintain the global total of distinct subsequences without duplicates, we update a running total by adding the newly generated subsequences and subtracting the count of subsequences that previously ended with the same character. This subtraction step effectively removes duplicates that would have been counted multiple times. By applying modulo 10^9 + 7 at each arithmetic step, we ensure the numbers remain within bounds while calculating the final result in linear time and constant extra space.

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
    int distinctSubseqII(string s) {
        long long total = 0;
        long long MOD = 1e9 + 7;
        long long endsWith[26] = {0};

        for (char c : s) {
            int idx = c - 'a';
            long long prevCountEndingWithC = endsWith[idx];
            endsWith[idx] = (total + 1) % MOD;
            total = (total + endsWith[idx] - prevCountEndingWithC + MOD) % MOD;
        }

        return (int)total;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int distinctSubseqII(String s) {
        long total = 0;
        long MOD = 1_000_000_007;
        long[] endsWith = new long[26];

        for (int i = 0; i < s.length(); i++) {
            int idx = s.charAt(i) - 'a';
            long prevCountEndingWithC = endsWith[idx];
            endsWith[idx] = (total + 1) % MOD;
            total = (total + endsWith[idx] - prevCountEndingWithC + MOD) % MOD;
        }

        return (int)total;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        total = 0
        ends_with = [0] * 26

        for char in s:
            idx = ord(char) - ord('a')
            prev_count_ending_with_c = ends_with[idx]
            new_count_ending_with_c = (total + 1) % MOD
            total = (total + new_count_ending_with_c - prev_count_ending_with_c + MOD) % MOD
            ends_with[idx] = new_count_ending_with_c

        return total
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 1000000007
        ends_with = [0] * 26
        total = 0
        for char in s:
            idx = ord(char) - ord('a')
            new_ends_with_idx = (total + 1) % MOD
            total = (total - ends_with[idx] + new_ends_with_idx + MOD) % MOD
            ends_with[idx] = new_ends_with_idx
        return total
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int distinctSubseqII(char* s) {
    long long ends_with[26] = {0};
    long long total = 0;
    long long MOD = 1000000007;
    for (int i = 0; s[i] != '\0'; i++) {
        int idx = s[i] - 'a';
        long long new_ends_with_idx = (total + 1) % MOD;
        total = (total - ends_with[idx] + new_ends_with_idx + MOD) % MOD;
        ends_with[idx] = new_ends_with_idx;
    }
    return (int)total;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int DistinctSubseqII(string s) {
        long[] endsWith = new long[26];
        long total = 0;
        long mod = 1000000007;
        foreach (char c in s) {
            int idx = c - 'a';
            long newEndsWithIdx = (total + 1) % mod;
            total = (total - endsWith[idx] + newEndsWithIdx + mod) % mod;
            endsWith[idx] = newEndsWithIdx;
        }
        return (int)total;
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
var distinctSubseqII = function(s) {
    const MOD = 1000000007;
    let endsWith = new Array(26).fill(0);
    let total = 0;
    for (let i = 0; i < s.length; i++) {
        let idx = s.charCodeAt(i) - 97;
        let newEndsWithIdx = (total + 1) % MOD;
        total = (total - endsWith[idx] + newEndsWithIdx + MOD) % MOD;
        endsWith[idx] = newEndsWithIdx;
    }
    return total;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function distinctSubseqII(s: string): number {
    const MOD = 1000000007;
    const ends = new Int32Array(26);
    let total = 0;
    for (let i = 0; i < s.length; i++) {
        const charIdx = s.charCodeAt(i) - 97;
        const added = (total + 1) % MOD;
        const nextTotal = (total + added) % MOD;
        total = (nextTotal - ends[charIdx] + MOD) % MOD;
        ends[charIdx] = added;
    }
    return total;
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
    function distinctSubseqII($s) {
        $MOD = 1000000007;
        $ends = array_fill(0, 26, 0);
        $total = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $charIdx = ord($s[$i]) - 97;
            $added = ($total + 1) % $MOD;
            $nextTotal = ($total + $added) % $MOD;
            $total = ($nextTotal - $ends[$charIdx] + $MOD) % $MOD;
            $ends[$charIdx] = $added;
        }
        return $total;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func distinctSubseqII(_ s: String) -> Int {
        let MOD = 1_000_000_007
        var ends = [Int](repeating: 0, count: 26)
        var total = 0
        for charByte in s.utf8 {
            let charIdx = Int(charByte) - 97
            let added = (total + 1) % MOD
            let nextTotal = (total + added) % MOD
            total = (nextTotal - ends[charIdx] + MOD) % MOD
            ends[charIdx] = added
        }
        return total
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun distinctSubseqII(s: String): Int {
        val MOD = 1000000007
        val ends = IntArray(26)
        var total = 0
        for (char in s) {
            val charIdx = char - 'a'
            val added = (total + 1) % MOD
            val nextTotal = (total + added) % MOD
            total = (nextTotal - ends[charIdx] + MOD) % MOD
            ends[charIdx] = added
        }
        return total
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int distinctSubseqII(String s) {
    int mod = 1000000007;
    List<int> added = List.filled(26, 0);
    int totalSum = 0;
    for (int i = 0; i < s.length; i++) {
      int charIdx = s.codeUnitAt(i) - 97;
      int oldAdded = added[charIdx];
      int newAdded = (totalSum + 1) % mod;
      added[charIdx] = newAdded;
      totalSum = (totalSum - oldAdded + newAdded + mod) % mod;
    }
    return totalSum;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func distinctSubseqII(s string) int {
    const mod = 1000000007
    added := [26]int{}
    totalSum := 0
    for i := 0; i < len(s); i++ {
        charIdx := int(s[i] - 'a')
        oldAdded := added[charIdx]
        newAdded := (totalSum + 1) % mod
        added[charIdx] = newAdded
        totalSum = (totalSum - oldAdded + newAdded + mod) % mod
    }
    return totalSum
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @return {Integer}
def distinct_subseq_ii(s)
  mod = 1_000_000_007
  added = Array.new(26, 0)
  total_sum = 0
  s.each_char do |char|
    char_idx = char.ord - 97
    old_added = added[char_idx]
    new_added = (total_sum + 1) % mod
    added[char_idx] = new_added
    total_sum = (total_sum - old_added + new_added + mod) % mod
  end
  total_sum
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def distinctSubseqII(s: String): Int = {
        val mod = 1000000007
        val added = Array.fill(26)(0L)
        var totalSum = 0L
        for (c <- s) {
            val charIdx = c - 'a'
            val oldAdded = added(charIdx)
            val newAdded = (totalSum + 1) % mod
            added(charIdx) = newAdded
            totalSum = (totalSum - oldAdded + newAdded + mod) % mod
        }
        totalSum.toInt
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn distinct_subseq_ii(s: String) -> i32 {
        let m: i64 = 1_000_000_007;
        let mut last_added = [0i64; 26];
        let mut total: i64 = 1;
        for &b in s.as_bytes() {
            let idx = (b - b'a') as usize;
            let prev_total = last_added[idx];
            let added = (total - prev_total + m) % m;
            last_added[idx] = total;
            total = (total + added) % m;
        }
        ((total - 1 + m) % m) as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (distinct-subseq-ii s)
  (-> string? exact-integer?)
  (let ([mod 1000000007]
        [dp (make-vector 26 0)])
    (let ([final-total
           (for/fold ([total 1])
                     ([c (in-string s)])
             (let* ([idx (- (char->integer c) (char->integer #\a))]
                    [prev-total (vector-ref dp idx)]
                    [added (modulo (- total prev-total) mod)]
                    [new-total (modulo (+ total added) mod)])
               (vector-set! dp idx total)
               new-total))])
      (modulo (- final-total 1) mod))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec distinct_subseq_ii(S :: unicode:unicode_binary()) -> integer().
distinct_subseq_ii(S) ->
    Mod = 1000000007,
    Chars = binary_to_list(S),
    {FinalTotal, _} = lists:foldl(
        fn(Char, {Total, LA}) ->
            PrevTotal = maps:get(Char, LA, 0),
            Added = (Total - PrevTotal + Mod) rem Mod,
            NewTotal = (Total + Added) rem Mod,
            {NewTotal, maps:put(Char, Total, LA)}
        end,
        {1, #{}},
        Chars
    ),
    (FinalTotal - 1 + Mod) rem Mod.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec distinct_subseq_ii(s :: String.t) :: integer
  def distinct_subseq_ii(s) do
    mod = 1_000_000_007
    {final_total, _} = s
      |> String.to_charlist()
      |> Enum.reduce({1, %{}}, fn char, {total, last_added} ->
        prev_total = Map.get(last_added, char, 0)
        added = Integer.mod(total - prev_total, mod)
        new_total = Integer.mod(total + added, mod)
        {new_total, Map.put(last_added, char, total)}
      end)
    Integer.mod(final_total - 1, mod)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N), where N is the length of the string s. The algorithm performs a single pass through the input string, and for each character, it executes a constant number of arithmetic operations and updates a fixed-size array.
- **Space Complexity:** O(1) because we only store an array of size 26 to keep track of the counts for each lowercase English letter. The space used is independent of the input string length N.
