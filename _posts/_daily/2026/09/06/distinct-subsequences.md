---
layout: post
title: "Distinct Subsequences"
date: 2026-09-06 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["String", "Dynamic Programming"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/distinct-subsequences/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int numDistinct(string s, string t) {\n \
        \       int n = s.length();\n        int m = t.length();\n        if (n < m)\
        \ return 0;\n\n        vector<unsigned long long> dp(m + 1, 0);\n        dp[0]\
        \ = 1;\n\n        for (int i = 0; i < n; ++i) {\n            for (int j = m;\
        \ j >= 1; --j) {\n                if (s[i] == t[j - 1]) {\n                \
        \    dp[j] += dp[j - 1];\n                }\n            }\n        }\n\n  \
        \      return (int)dp[m];\n    }\n};"
      java: "class Solution {\n    public int numDistinct(String s, String t) {\n  \
        \      int n = s.length();\n        int m = t.length();\n        if (n < m)\
        \ return 0;\n\n        long[] dp = new long[m + 1];\n        dp[0] = 1;\n\n\
        \        for (int i = 0; i < n; i++) {\n            for (int j = m; j >= 1;\
        \ j--) {\n                if (s.charAt(i) == t.charAt(j - 1)) {\n          \
        \          dp[j] += dp[j - 1];\n                }\n            }\n        }\n\
        \n        return (int) dp[m];\n    }\n}"
      python: "class Solution(object):\n    def numDistinct(self, s, t):\n        \"\
        \"\"\n        :type s: str\n        :type t: str\n        :rtype: int\n    \
        \    \"\"\"\n        n = len(s)\n        m = len(t)\n        if n < m:\n   \
        \         return 0\n\n        dp = [0] * (m + 1)\n        dp[0] = 1\n\n    \
        \    for char in s:\n            for j in range(m, 0, -1):\n               \
        \ if char == t[j - 1]:\n                    dp[j] += dp[j - 1]\n\n        return\
        \ dp[m]"
      python3: "class Solution:\n    def numDistinct(self, s: str, t: str) -> int:\n\
        \        n, m = len(s), len(t)\n        if n < m:\n            return 0\n\n\
        \        dp = [0] * (m + 1)\n        dp[0] = 1\n\n        for char_s in s:\n\
        \            for j in range(m - 1, -1, -1):\n                if char_s == t[j]:\n\
        \                    dp[j + 1] += dp[j]\n\n        return dp[m]"
      c: "int numDistinct(char* s, char* t) {\n    int n = 0; while (s[n]) n++;\n  \
        \  int m = 0; while (t[m]) m++;\n\n    if (n < m) return 0;\n\n    unsigned\
        \ long long dp[1001];\n    for (int j = 0; j <= m; j++) {\n        dp[j] = 0;\n\
        \    }\n    dp[0] = 1;\n\n    for (int i = 0; i < n; i++) {\n        char current_s\
        \ = s[i];\n        for (int j = m - 1; j >= 0; j--) {\n            if (current_s\
        \ == t[j]) {\n                dp[j + 1] += dp[j];\n            }\n        }\n\
        \    }\n\n    return (int)dp[m];\n}"
      csharp: "public class Solution {\n    public int NumDistinct(string s, string\
        \ t) {\n        int n = s.Length;\n        int m = t.Length;\n        if (n\
        \ < m) return 0;\n\n        long[] dp = new long[m + 1];\n        dp[0] = 1;\n\
        \n        for (int i = 0; i < n; i++) {\n            char charS = s[i];\n  \
        \          for (int j = m - 1; j >= 0; j--) {\n                if (charS ==\
        \ t[j]) {\n                    dp[j + 1] += dp[j];\n                }\n    \
        \        }\n        }\n\n        return (int)dp[m];\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @param {string} t\n * @return {number}\n\
        \ */\nvar numDistinct = function(s, t) {\n    const n = s.length;\n    const\
        \ m = t.length;\n    if (n < m) return 0;\n\n    const dp = new Array(m + 1).fill(0);\n\
        \    dp[0] = 1;\n\n    for (let i = 0; i < n; i++) {\n        const charS =\
        \ s[i];\n        for (let j = m - 1; j >= 0; j--) {\n            if (charS ===\
        \ t[j]) {\n                dp[j + 1] += dp[j];\n            }\n        }\n \
        \   }\n\n    return dp[m];\n};"
      typescript: "function numDistinct(s: string, t: string): number {\n    const n\
        \ = s.length;\n    const m = t.length;\n    if (n < m) return 0;\n\n    const\
        \ dp = new Array(m + 1).fill(0);\n    dp[0] = 1;\n\n    for (let i = 0; i <\
        \ n; i++) {\n        for (let j = m; j >= 1; j--) {\n            if (s[i] ===\
        \ t[j - 1]) {\n                dp[j] += dp[j - 1];\n            }\n        }\n\
        \    }\n\n    return dp[m];\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @param String\
        \ $t\n     * @return Integer\n     */\n    function numDistinct($s, $t) {\n\
        \        $n = strlen($s);\n        $m = strlen($t);\n        if ($n < $m) return\
        \ 0;\n\n        $dp = array_fill(0, $m + 1, 0);\n        $dp[0] = 1;\n\n   \
        \     for ($i = 0; $i < $n; $i++) {\n            for ($j = $m; $j >= 1; $j--)\
        \ {\n                if ($s[$i] === $t[$j - 1]) {\n                    $dp[$j]\
        \ += $dp[$j - 1];\n                }\n            }\n        }\n\n        return\
        \ $dp[$m];\n    }\n}"
      swift: "class Solution {\n    func numDistinct(_ s: String, _ t: String) -> Int\
        \ {\n        let sChars = Array(s)\n        let tChars = Array(t)\n        let\
        \ n = sChars.count\n        let m = tChars.count\n        if n < m { return\
        \ 0 }\n\n        var dp = [Int](repeating: 0, count: m + 1)\n        dp[0] =\
        \ 1\n\n        for i in 0..<n {\n            for j in stride(from: m, through:\
        \ 1, by: -1) {\n                if sChars[i] == tChars[j - 1] {\n          \
        \          dp[j] += dp[j - 1]\n                }\n            }\n        }\n\
        \n        return dp[m]\n    }\n}"
      kotlin: "class Solution {\n    fun numDistinct(s: String, t: String): Int {\n\
        \        val n = s.length\n        val m = t.length\n        if (n < m) return\
        \ 0\n\n        val dp = LongArray(m + 1)\n        dp[0] = 1L\n\n        for\
        \ (i in 0 until n) {\n            for (j in m downTo 1) {\n                if\
        \ (s[i] == t[j - 1]) {\n                    dp[j] += dp[j - 1]\n           \
        \     }\n            }\n        }\n\n        return dp[m].toInt()\n    }\n}"
      dart: "class Solution {\n  int numDistinct(String s, String t) {\n    int n =\
        \ s.length;\n    int m = t.length;\n    if (n < m) return 0;\n    List<int>\
        \ dp = List<int>.filled(m + 1, 0);\n    dp[0] = 1;\n    for (int i = 0; i <\
        \ n; i++) {\n      int charS = s.codeUnitAt(i);\n      for (int j = m - 1; j\
        \ >= 0; j--) {\n        if (charS == t.codeUnitAt(j)) {\n          dp[j + 1]\
        \ += dp[j];\n        }\n      }\n    }\n    return dp[m];\n  }\n}"
      go: "func numDistinct(s string, t string) int {\n\tn, m := len(s), len(t)\n\t\
        if n < m {\n\t\treturn 0\n\t}\n\tdp := make([]int64, m+1)\n\tdp[0] = 1\n\tfor\
        \ i := 0; i < n; i++ {\n\t\tcharS := s[i]\n\t\tfor j := m - 1; j >= 0; j-- {\n\
        \t\t\tif charS == t[j] {\n\t\t\t\tdp[j+1] += dp[j]\n\t\t\t}\n\t\t}\n\t}\n\t\
        return int(dp[m])\n}"
      ruby: "# @param {String} s\n# @param {String} t\n# @return {Integer}\ndef num_distinct(s,\
        \ t)\n  n, m = s.length, t.length\n  return 0 if n < m\n  t_bytes = t.bytes\n\
        \  dp = Array.new(m + 1, 0)\n  dp[0] = 1\n  s.each_byte do |byte_s|\n    j =\
        \ m - 1\n    while j >= 0\n      if byte_s == t_bytes[j]\n        dp[j + 1]\
        \ += dp[j]\n      end\n      j -= 1\n    end\n  end\n  dp[m]\nend"
      scala: "object Solution {\n    def numDistinct(s: String, t: String): Int = {\n\
        \        val n = s.length\n        val m = t.length\n        if (n < m) return\
        \ 0\n        val dp = new Array[Long](m + 1)\n        dp(0) = 1L\n        var\
        \ i = 0\n        while (i < n) {\n            val charS = s.charAt(i)\n    \
        \        var j = m - 1\n            while (j >= 0) {\n                if (charS\
        \ == t.charAt(j)) {\n                    dp(j + 1) += dp(j)\n              \
        \  }\n                j -= 1\n            }\n            i += 1\n        }\n\
        \        dp(m).toInt\n    }\n}"
      rust: "impl Solution {\n    pub fn num_distinct(s: String, t: String) -> i32 {\n\
        \        let s_bytes = s.as_bytes();\n        let t_bytes = t.as_bytes();\n\
        \        let m = s_bytes.len();\n        let n = t_bytes.len();\n        if\
        \ m < n {\n            return 0;\n        }\n\n        let mut dp = vec![0u64;\
        \ n + 1];\n        dp[0] = 1;\n\n        for &sc in s_bytes {\n            for\
        \ j in (1..=n).rev() {\n                if sc == t_bytes[j - 1] {\n        \
        \            dp[j] = dp[j].wrapping_add(dp[j - 1]);\n                }\n   \
        \         }\n        }\n\n        dp[n] as i32\n    }\n}"
      racket: "(define/contract (num-distinct s t)\n  (-> string? string? exact-integer?)\n\
        \  (let* ([s-list (string->list s)]\n         [t-vec (list->vector (string->list\
        \ t))]\n         [n (vector-length t-vec)]\n         [dp (make-vector (+ n 1)\
        \ 0)])\n    (vector-set! dp 0 1)\n    (for ([char-s s-list])\n      (for ([j\
        \ (in-range n 0 -1)])\n        (when (char=? char-s (vector-ref t-vec (- j 1)))\n\
        \          (vector-set! dp j (+ (vector-ref dp j) (vector-ref dp (- j 1)))))))\n\
        \    (vector-ref dp n)))"
      erlang: "-spec num_distinct(S :: unicode:unicode_binary(), T :: unicode:unicode_binary())\
        \ -> integer().\nnum_distinct(S, T) ->\n    SList = binary_to_list(S),\n   \
        \ TList = binary_to_list(T),\n    InitialDP = [1 | lists:duplicate(length(TList),\
        \ 0)],\n    FinalDP = lists:foldl(fun(CharS, AccDP) ->\n        update_dp(CharS,\
        \ TList, AccDP)\n    end, InitialDP, SList),\n    lists:last(FinalDP).\n\nupdate_dp(CharS,\
        \ TList, [DPPrev | RestDP]) ->\n    [DPPrev | update_row(CharS, TList, DPPrev,\
        \ RestDP, [])].\n\nupdate_row(_CharS, [], _DPPrev, [], Acc) ->\n    lists:reverse(Acc);\n\
        update_row(CharS, [CharT | RestT], DPPrev, [DPCurr | RestDP], Acc) ->\n    NewVal\
        \ = if CharS =:= CharT -> DPCurr + DPPrev;\n                true -> DPCurr\n\
        \             end,\n    update_row(CharS, RestT, DPCurr, RestDP, [NewVal | Acc])."
      elixir: "defmodule Solution do\n  @spec num_distinct(s :: String.t, t :: String.t)\
        \ :: integer\n  def num_distinct(s, t) do\n    s_list = String.to_charlist(s)\n\
        \    t_list = String.to_charlist(t)\n    t_len = length(t_list)\n    initial_dp\
        \ = [1 | List.duplicate(0, t_len)]\n\n    final_dp = Enum.reduce(s_list, initial_dp,\
        \ fn char_s, acc_dp ->\n      update_dp(char_s, t_list, acc_dp)\n    end)\n\n\
        \    List.last(final_dp)\n  end\n\n  defp update_dp(char_s, t_list, [dp_prev\
        \ | rest_dp]) do\n    [dp_prev | update_row(char_s, t_list, dp_prev, rest_dp)]\n\
        \  end\n\n  defp update_row(char_s, t_list, dp_prev, rest_dp) do\n    do_update_row(char_s,\
        \ t_list, dp_prev, rest_dp, [])\n  end\n\n  defp do_update_row(_char_s, [],\
        \ _dp_prev, [], acc) do\n    Enum.reverse(acc)\n  end\n\n  defp do_update_row(char_s,\
        \ [char_t | rest_t], dp_prev, [dp_curr | rest_dp], acc) do\n    new_val = if\
        \ char_s == char_t, do: dp_curr + dp_prev, else: dp_curr\n    do_update_row(char_s,\
        \ rest_t, dp_curr, rest_dp, [new_val | acc])\n  end\nend"
    approach: 'The problem is solved using dynamic programming by defining $dp[j]$ as
      the number of distinct subsequences of the current prefix of $s$ that match the
      prefix of $t$ of length $j$. The base case is $dp[0] = 1$, because an empty string
      $t$ can be formed by a subsequence of any prefix of $s$ in exactly one way (by
      deleting all characters). For all other $j > 0$, $dp[j]$ is initially 0.


      We iterate through each character of $s$, and for each character, we update the
      $dp$ array. To optimize space, we use a 1D array and iterate through $t$ from
      right to left (from $j = m$ down to $1$). If the current character $s[i]$ matches
      $t[j-1]$, the new value of $dp[j]$ is the sum of its previous value (representing
      subsequences that do not use the current character $s[i]$) and $dp[j-1]$ (representing
      subsequences that use $s[i]$ to match $t[j-1]$). This backward iteration ensures
      that $dp[j-1]$ still reflects the count from the previous prefix of $s$, maintaining
      the integrity of the DP transition.'
    time_complexity: O(n * m) where n is the length of string s and m is the length
      of string t. We iterate through each character of s and, for each character, potentially
      update all m elements of the DP array.
    space_complexity: O(m) where m is the length of string t. This is achieved by using
      a 1D DP array to store the counts for prefixes of t, rather than a full 2D table.
    elapsed_time: 256.5944640636444
    model: gemini-3-flash-preview
    generated_at: '2026-09-06 02:17:08 '
---

## Problem #115: Distinct Subsequences

**Difficulty:** Hard

**Topics:** String, Dynamic Programming

## Problem Description

<p>Given two strings s and t, return <i>the number of distinct</i> <b><i>subsequences</i></b><i> of </i>s<i> which equals </i>t.</p>

<p>The test cases are generated so that the answer fits on a 32-bit signed integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;rabbbit&quot;, t = &quot;rabbit&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong>
As shown below, there are 3 ways you can generate &quot;rabbit&quot; from s.
<code><strong><u>rabb</u></strong>b<strong><u>it</u></strong></code>
<code><strong><u>ra</u></strong>b<strong><u>bbit</u></strong></code>
<code><strong><u>rab</u></strong>b<strong><u>bit</u></strong></code>
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;babgbag&quot;, t = &quot;bag&quot;
<strong>Output:</strong> 5
<strong>Explanation:</strong>
As shown below, there are 5 ways you can generate &quot;bag&quot; from s.
<code><strong><u>ba</u></strong>b<u><strong>g</strong></u>bag</code>
<code><strong><u>ba</u></strong>bgba<strong><u>g</u></strong></code>
<code><u><strong>b</strong></u>abgb<strong><u>ag</u></strong></code>
<code>ba<u><strong>b</strong></u>gb<u><strong>ag</strong></u></code>
<code>babg<strong><u>bag</u></strong></code></pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 1000</code></li>
	<li><code>s</code> and <code>t</code> consist of English letters.</li>
</ul>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem is solved using dynamic programming by defining $dp[j]$ as the number of distinct subsequences of the current prefix of $s$ that match the prefix of $t$ of length $j$. The base case is $dp[0] = 1$, because an empty string $t$ can be formed by a subsequence of any prefix of $s$ in exactly one way (by deleting all characters). For all other $j > 0$, $dp[j]$ is initially 0.

We iterate through each character of $s$, and for each character, we update the $dp$ array. To optimize space, we use a 1D array and iterate through $t$ from right to left (from $j = m$ down to $1$). If the current character $s[i]$ matches $t[j-1]$, the new value of $dp[j]$ is the sum of its previous value (representing subsequences that do not use the current character $s[i]$) and $dp[j-1]$ (representing subsequences that use $s[i]$ to match $t[j-1]$). This backward iteration ensures that $dp[j-1]$ still reflects the count from the previous prefix of $s$, maintaining the integrity of the DP transition.

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
    int numDistinct(string s, string t) {
        int n = s.length();
        int m = t.length();
        if (n < m) return 0;

        vector<unsigned long long> dp(m + 1, 0);
        dp[0] = 1;

        for (int i = 0; i < n; ++i) {
            for (int j = m; j >= 1; --j) {
                if (s[i] == t[j - 1]) {
                    dp[j] += dp[j - 1];
                }
            }
        }

        return (int)dp[m];
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int numDistinct(String s, String t) {
        int n = s.length();
        int m = t.length();
        if (n < m) return 0;

        long[] dp = new long[m + 1];
        dp[0] = 1;

        for (int i = 0; i < n; i++) {
            for (int j = m; j >= 1; j--) {
                if (s.charAt(i) == t.charAt(j - 1)) {
                    dp[j] += dp[j - 1];
                }
            }
        }

        return (int) dp[m];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n = len(s)
        m = len(t)
        if n < m:
            return 0

        dp = [0] * (m + 1)
        dp[0] = 1

        for char in s:
            for j in range(m, 0, -1):
                if char == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[m]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        if n < m:
            return 0

        dp = [0] * (m + 1)
        dp[0] = 1

        for char_s in s:
            for j in range(m - 1, -1, -1):
                if char_s == t[j]:
                    dp[j + 1] += dp[j]

        return dp[m]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int numDistinct(char* s, char* t) {
    int n = 0; while (s[n]) n++;
    int m = 0; while (t[m]) m++;

    if (n < m) return 0;

    unsigned long long dp[1001];
    for (int j = 0; j <= m; j++) {
        dp[j] = 0;
    }
    dp[0] = 1;

    for (int i = 0; i < n; i++) {
        char current_s = s[i];
        for (int j = m - 1; j >= 0; j--) {
            if (current_s == t[j]) {
                dp[j + 1] += dp[j];
            }
        }
    }

    return (int)dp[m];
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int NumDistinct(string s, string t) {
        int n = s.Length;
        int m = t.Length;
        if (n < m) return 0;

        long[] dp = new long[m + 1];
        dp[0] = 1;

        for (int i = 0; i < n; i++) {
            char charS = s[i];
            for (int j = m - 1; j >= 0; j--) {
                if (charS == t[j]) {
                    dp[j + 1] += dp[j];
                }
            }
        }

        return (int)dp[m];
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
 * @param {string} t
 * @return {number}
 */
var numDistinct = function(s, t) {
    const n = s.length;
    const m = t.length;
    if (n < m) return 0;

    const dp = new Array(m + 1).fill(0);
    dp[0] = 1;

    for (let i = 0; i < n; i++) {
        const charS = s[i];
        for (let j = m - 1; j >= 0; j--) {
            if (charS === t[j]) {
                dp[j + 1] += dp[j];
            }
        }
    }

    return dp[m];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function numDistinct(s: string, t: string): number {
    const n = s.length;
    const m = t.length;
    if (n < m) return 0;

    const dp = new Array(m + 1).fill(0);
    dp[0] = 1;

    for (let i = 0; i < n; i++) {
        for (let j = m; j >= 1; j--) {
            if (s[i] === t[j - 1]) {
                dp[j] += dp[j - 1];
            }
        }
    }

    return dp[m];
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
     * @param String $t
     * @return Integer
     */
    function numDistinct($s, $t) {
        $n = strlen($s);
        $m = strlen($t);
        if ($n < $m) return 0;

        $dp = array_fill(0, $m + 1, 0);
        $dp[0] = 1;

        for ($i = 0; $i < $n; $i++) {
            for ($j = $m; $j >= 1; $j--) {
                if ($s[$i] === $t[$j - 1]) {
                    $dp[$j] += $dp[$j - 1];
                }
            }
        }

        return $dp[$m];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func numDistinct(_ s: String, _ t: String) -> Int {
        let sChars = Array(s)
        let tChars = Array(t)
        let n = sChars.count
        let m = tChars.count
        if n < m { return 0 }

        var dp = [Int](repeating: 0, count: m + 1)
        dp[0] = 1

        for i in 0..<n {
            for j in stride(from: m, through: 1, by: -1) {
                if sChars[i] == tChars[j - 1] {
                    dp[j] += dp[j - 1]
                }
            }
        }

        return dp[m]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun numDistinct(s: String, t: String): Int {
        val n = s.length
        val m = t.length
        if (n < m) return 0

        val dp = LongArray(m + 1)
        dp[0] = 1L

        for (i in 0 until n) {
            for (j in m downTo 1) {
                if (s[i] == t[j - 1]) {
                    dp[j] += dp[j - 1]
                }
            }
        }

        return dp[m].toInt()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int numDistinct(String s, String t) {
    int n = s.length;
    int m = t.length;
    if (n < m) return 0;
    List<int> dp = List<int>.filled(m + 1, 0);
    dp[0] = 1;
    for (int i = 0; i < n; i++) {
      int charS = s.codeUnitAt(i);
      for (int j = m - 1; j >= 0; j--) {
        if (charS == t.codeUnitAt(j)) {
          dp[j + 1] += dp[j];
        }
      }
    }
    return dp[m];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func numDistinct(s string, t string) int {
	n, m := len(s), len(t)
	if n < m {
		return 0
	}
	dp := make([]int64, m+1)
	dp[0] = 1
	for i := 0; i < n; i++ {
		charS := s[i]
		for j := m - 1; j >= 0; j-- {
			if charS == t[j] {
				dp[j+1] += dp[j]
			}
		}
	}
	return int(dp[m])
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @param {String} t
# @return {Integer}
def num_distinct(s, t)
  n, m = s.length, t.length
  return 0 if n < m
  t_bytes = t.bytes
  dp = Array.new(m + 1, 0)
  dp[0] = 1
  s.each_byte do |byte_s|
    j = m - 1
    while j >= 0
      if byte_s == t_bytes[j]
        dp[j + 1] += dp[j]
      end
      j -= 1
    end
  end
  dp[m]
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def numDistinct(s: String, t: String): Int = {
        val n = s.length
        val m = t.length
        if (n < m) return 0
        val dp = new Array[Long](m + 1)
        dp(0) = 1L
        var i = 0
        while (i < n) {
            val charS = s.charAt(i)
            var j = m - 1
            while (j >= 0) {
                if (charS == t.charAt(j)) {
                    dp(j + 1) += dp(j)
                }
                j -= 1
            }
            i += 1
        }
        dp(m).toInt
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn num_distinct(s: String, t: String) -> i32 {
        let s_bytes = s.as_bytes();
        let t_bytes = t.as_bytes();
        let m = s_bytes.len();
        let n = t_bytes.len();
        if m < n {
            return 0;
        }

        let mut dp = vec![0u64; n + 1];
        dp[0] = 1;

        for &sc in s_bytes {
            for j in (1..=n).rev() {
                if sc == t_bytes[j - 1] {
                    dp[j] = dp[j].wrapping_add(dp[j - 1]);
                }
            }
        }

        dp[n] as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (num-distinct s t)
  (-> string? string? exact-integer?)
  (let* ([s-list (string->list s)]
         [t-vec (list->vector (string->list t))]
         [n (vector-length t-vec)]
         [dp (make-vector (+ n 1) 0)])
    (vector-set! dp 0 1)
    (for ([char-s s-list])
      (for ([j (in-range n 0 -1)])
        (when (char=? char-s (vector-ref t-vec (- j 1)))
          (vector-set! dp j (+ (vector-ref dp j) (vector-ref dp (- j 1)))))))
    (vector-ref dp n)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec num_distinct(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> integer().
num_distinct(S, T) ->
    SList = binary_to_list(S),
    TList = binary_to_list(T),
    InitialDP = [1 | lists:duplicate(length(TList), 0)],
    FinalDP = lists:foldl(fun(CharS, AccDP) ->
        update_dp(CharS, TList, AccDP)
    end, InitialDP, SList),
    lists:last(FinalDP).

update_dp(CharS, TList, [DPPrev | RestDP]) ->
    [DPPrev | update_row(CharS, TList, DPPrev, RestDP, [])].

update_row(_CharS, [], _DPPrev, [], Acc) ->
    lists:reverse(Acc);
update_row(CharS, [CharT | RestT], DPPrev, [DPCurr | RestDP], Acc) ->
    NewVal = if CharS =:= CharT -> DPCurr + DPPrev;
                true -> DPCurr
             end,
    update_row(CharS, RestT, DPCurr, RestDP, [NewVal | Acc]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec num_distinct(s :: String.t, t :: String.t) :: integer
  def num_distinct(s, t) do
    s_list = String.to_charlist(s)
    t_list = String.to_charlist(t)
    t_len = length(t_list)
    initial_dp = [1 | List.duplicate(0, t_len)]

    final_dp = Enum.reduce(s_list, initial_dp, fn char_s, acc_dp ->
      update_dp(char_s, t_list, acc_dp)
    end)

    List.last(final_dp)
  end

  defp update_dp(char_s, t_list, [dp_prev | rest_dp]) do
    [dp_prev | update_row(char_s, t_list, dp_prev, rest_dp)]
  end

  defp update_row(char_s, t_list, dp_prev, rest_dp) do
    do_update_row(char_s, t_list, dp_prev, rest_dp, [])
  end

  defp do_update_row(_char_s, [], _dp_prev, [], acc) do
    Enum.reverse(acc)
  end

  defp do_update_row(char_s, [char_t | rest_t], dp_prev, [dp_curr | rest_dp], acc) do
    new_val = if char_s == char_t, do: dp_curr + dp_prev, else: dp_curr
    do_update_row(char_s, rest_t, dp_curr, rest_dp, [new_val | acc])
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n * m) where n is the length of string s and m is the length of string t. We iterate through each character of s and, for each character, potentially update all m elements of the DP array.
- **Space Complexity:** O(m) where m is the length of string t. This is achieved by using a 1D DP array to store the counts for prefixes of t, rather than a full 2D table.
