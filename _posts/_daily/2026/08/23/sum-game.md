---
layout: post
title: "Sum Game"
date: 2026-08-23 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Math", "String", "Greedy", "Game Theory"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/sum-game/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool sumGame(string num) {\n        int n\
        \ = num.length();\n        int s1 = 0, s2 = 0, c1 = 0, c2 = 0;\n        for\
        \ (int i = 0; i < n / 2; ++i) {\n            if (num[i] == '?') c1++;\n    \
        \        else s1 += num[i] - '0';\n        }\n        for (int i = n / 2; i\
        \ < n; ++i) {\n            if (num[i] == '?') c2++;\n            else s2 +=\
        \ num[i] - '0';\n        }\n        return (2 * s1 + 9 * c1) != (2 * s2 + 9\
        \ * c2);\n    }\n};"
      java: "class Solution {\n    public boolean sumGame(String num) {\n        int\
        \ n = num.length();\n        int s1 = 0, s2 = 0, c1 = 0, c2 = 0;\n        for\
        \ (int i = 0; i < n / 2; i++) {\n            char ch = num.charAt(i);\n    \
        \        if (ch == '?') c1++;\n            else s1 += ch - '0';\n        }\n\
        \        for (int i = n / 2; i < n; i++) {\n            char ch = num.charAt(i);\n\
        \            if (ch == '?') c2++;\n            else s2 += ch - '0';\n      \
        \  }\n        return (2 * s1 + 9 * c1) != (2 * s2 + 9 * c2);\n    }\n}"
      python: "class Solution(object):\n    def sumGame(self, num):\n        \"\"\"\n\
        \        :type num: str\n        :rtype: bool\n        \"\"\"\n        n = len(num)\n\
        \        s1 = c1 = s2 = c2 = 0\n        for i in range(n / 2):\n           \
        \ if num[i] == '?':\n                c1 += 1\n            else:\n          \
        \      s1 += int(num[i])\n        for i in range(n / 2, n):\n            if\
        \ num[i] == '?':\n                c2 += 1\n            else:\n             \
        \   s2 += int(num[i])\n        return 2 * s1 + 9 * c1 != 2 * s2 + 9 * c2"
      python3: "class Solution:\n    def sumGame(self, num: str) -> bool:\n        n\
        \ = len(num)\n        s1 = s2 = c1 = c2 = 0\n        for i in range(n // 2):\n\
        \            if num[i] == '?':\n                c1 += 1\n            else:\n\
        \                s1 += int(num[i])\n        for i in range(n // 2, n):\n   \
        \         if num[i] == '?':\n                c2 += 1\n            else:\n  \
        \              s2 += int(num[i])\n        return 2 * s1 + 9 * c1 != 2 * s2 +\
        \ 9 * c2"
      c: "#include <stdbool.h>\n#include <string.h>\n\nbool sumGame(char* num) {\n \
        \   int n = (int)strlen(num);\n    int s1 = 0, s2 = 0, c1 = 0, c2 = 0;\n   \
        \ for (int i = 0; i < n / 2; i++) {\n        if (num[i] == '?') c1++;\n    \
        \    else s1 += num[i] - '0';\n    }\n    for (int i = n / 2; i < n; i++) {\n\
        \        if (num[i] == '?') c2++;\n        else s2 += num[i] - '0';\n    }\n\
        \    return (2 * s1 + 9 * c1) != (2 * s2 + 9 * c2);\n}"
      csharp: "public class Solution {\n    public bool SumGame(string num) {\n    \
        \    int n = num.Length;\n        int s1 = 0, c1 = 0, s2 = 0, c2 = 0;\n\n  \
        \      for (int i = 0; i < n; i++) {\n            if (i < n / 2) {\n       \
        \         if (num[i] == '?') {\n                    c1++;\n                }\
        \ else {\n                    s1 += num[i] - '0';\n                }\n     \
        \       } else {\n                if (num[i] == '?') {\n                   \
        \ c2++;\n                } else {\n                    s2 += num[i] - '0';\n\
        \                }\n            }\n        }\n\n        // Bob wins if 2 * (s1\
        \ - s2) == 9 * (c2 - c1).\n        // Otherwise, Alice wins (return true).\n\
        \        return 2 * (s1 - s2) != 9 * (c2 - c1);\n    }\n}"
      javascript: "/**\n * @param {string} num\n * @return {boolean}\n */\nvar sumGame\
        \ = function(num) {\n    const n = num.length;\n    let s1 = 0, c1 = 0, s2 =\
        \ 0, c2 = 0;\n\n    for (let i = 0; i < n; i++) {\n        if (i < n / 2) {\n\
        \            if (num[i] === '?') {\n                c1++;\n            } else\
        \ {\n                s1 += num[i] - '0';\n            }\n        } else {\n\
        \            if (num[i] === '?') {\n                c2++;\n            } else\
        \ {\n                s2 += num[i] - '0';\n            }\n        }\n    }\n\n\
        \    return 2 * (s1 - s2) !== 9 * (c2 - c1);\n};"
      typescript: "function sumGame(num: string): boolean {\n    const n = num.length;\n\
        \    let s1 = 0, c1 = 0, s2 = 0, c2 = 0;\n\n    for (let i = 0; i < n; i++)\
        \ {\n        if (i < n / 2) {\n            if (num[i] === '?') {\n         \
        \       c1++;\n            } else {\n                s1 += parseInt(num[i],\
        \ 10);\n            }\n        } else {\n            if (num[i] === '?') {\n\
        \                c2++;\n            }\n        } \n    }\n\n    // Recalculating\
        \ sum and count logic to ensure correct iteration\n    s1 = 0; c1 = 0; s2 =\
        \ 0; c2 = 0;\n    for (let i = 0; i < n; i++) {\n        if (i < n / 2) {\n\
        \            if (num[i] === '?') {\n                c1++;\n            } else\
        \ {\n                s1 += Number(num[i]);\n            }\n        } else {\n\
        \            if (num[i] === '?') {\n                c2++;\n            } else\
        \ {\n                s2 += Number(num[i]);\n            }\n        }\n    }\n\
        \n    return 2 * (s1 - s2) !== 9 * (c2 - c1);\n};"
      php: "class Solution {\n\n    /**\n     * @param String $num\n     * @return Boolean\n\
        \     */\n    function sumGame($num) {\n        $n = strlen($num);\n       \
        \ $s1 = 0; $c1 = 0; $s2 = 0; $c2 = 0;\n\n        for ($i = 0; $i < $n; $i++)\
        \ {\n            if ($i < $n / 2) {\n                if ($num[$i] === '?') {\n\
        \                    $c1++;\n                } else {\n                    $s1\
        \ += intval($num[$i]);\n                }\n            } else {\n          \
        \      if ($num[$i] === '?') {\n                    $c2++;\n               \
        \ } else {\n                    $s2 += intval($num[$i]);\n                }\n\
        \            }\n        }\n\n        return 2 * ($s1 - $s2) !== 9 * ($c2 - $c1);\n\
        \    }\n}"
      swift: "class Solution {\n    func sumGame(_ num: String) -> Bool {\n        let\
        \ n = num.count\n        var s1 = 0, c1 = 0, s2 = 0, c2 = 0\n        var i =\
        \ 0\n\n        for char in num {\n            if i < n / 2 {\n             \
        \   if char == \"?\" {\n                    c1 += 1\n                } else\
        \ if let digit = char.wholeNumberValue {\n                    s1 += digit\n\
        \                }\n            } else {\n                if char == \"?\" {\n\
        \                    c2 += 1\n                } else if let digit = char.wholeNumberValue\
        \ {\n                    s2 += digit\n                }\n            }\n   \
        \         i += 1\n        }\n\n        return 2 * (s1 - s2) != 9 * (c2 - c1)\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun sumGame(num: String): Boolean {\n        val\
        \ n = num.length\n        var diffS = 0\n        var diffQ = 0\n        for\
        \ (i in 0 until n / 2) {\n            if (num[i] == '?') {\n               \
        \ diffQ--\n            } else {\n                diffS += num[i] - '0'\n   \
        \         }\n        }\n        for (i in n / 2 until n) {\n            if (num[i]\
        \ == '?') {\n                diffQ++\n            } else {\n               \
        \ diffS -= num[i] - '0'\n            }\n        }\n        return 2 * diffS\
        \ != 9 * diffQ\n    }\n}"
      dart: "class Solution {\n  bool sumGame(String num) {\n    int n = num.length;\n\
        \    int diffS = 0;\n    int diffQ = 0;\n    for (int i = 0; i < n ~/ 2; i++)\
        \ {\n      if (num[i] == '?') {\n        diffQ--;\n      } else {\n        diffS\
        \ += int.parse(num[i]);\n      }\n    }\n    for (int i = n ~/ 2; i < n; i++)\
        \ {\n      if (num[i] == '?') {\n        diffQ++;\n      } else {\n        diffS\
        \ -= int.parse(num[i]);\n      }\n    }\n    return 2 * diffS != 9 * diffQ;\n\
        \  }\n}"
      go: "func sumGame(num string) bool {\n    n := len(num)\n    diffS := 0\n    diffQ\
        \ := 0\n    for i := 0; i < n/2; i++ {\n        if num[i] == '?' {\n       \
        \     diffQ--\n        } else {\n            diffS += int(num[i] - '0')\n  \
        \      }\n    }\n    for i := n/2; i < n; i++ {\n        if num[i] == '?' {\n\
        \            diffQ++\n        } else {\n            diffS -= int(num[i] - '0')\n\
        \        }\n    }\n    return 2*diffS != 9*diffQ\n}"
      ruby: "# @param {String} num\n# @return {Boolean}\ndef sum_game(num)\n    n =\
        \ num.length\n    diff_s = 0\n    diff_q = 0\n    (0...(n / 2)).each do |i|\n\
        \        if num[i] == '?'\n            diff_q -= 1\n        else\n         \
        \   diff_s += num[i].to_i\n        end\n    end\n    ((n / 2)...n).each do |i|\n\
        \        if num[i] == '?'\n            diff_q += 1\n        else\n         \
        \   diff_s -= num[i].to_i\n        end\n    end\n    2 * diff_s != 9 * diff_q\n\
        end"
      scala: "object Solution {\n    def sumGame(num: String): Boolean = {\n       \
        \ val n = num.length\n        var diffS = 0\n        var diffQ = 0\n       \
        \ for (i <- 0 until n / 2) {\n            if (num(i) == '?') {\n           \
        \     diffQ -= 1\n            } else {\n                diffS += num(i).asDigit\n\
        \            }\n        }\n        for (i <- n / 2 until n) {\n            if\
        \ (num(i) == '?') {\n                diffQ += 1\n            } else {\n    \
        \            diffS -= num(i).asDigit\n            }\n        }\n        2 *\
        \ diffS != 9 * diffQ\n    }\n}"
      rust: "impl Solution {\n    pub fn sum_game(num: String) -> bool {\n        let\
        \ n = num.len();\n        let bytes = num.as_bytes();\n        let mut l_sum\
        \ = 0i32;\n        let mut l_cnt = 0i32;\n        let mut r_sum = 0i32;\n  \
        \      let mut r_cnt = 0i32;\n\n        for i in 0..n / 2 {\n            if\
        \ bytes[i] == b'?' {\n                l_cnt += 1;\n            } else {\n  \
        \              l_sum += (bytes[i] - b'0') as i32;\n            }\n        }\n\
        \        for i in n / 2..n {\n            if bytes[i] == b'?' {\n          \
        \      r_cnt += 1;\n            } else {\n                r_sum += (bytes[i]\
        \ - b'0') as i32;\n            }\n        }\n\n        2 * (l_sum - r_sum) !=\
        \ 9 * (r_cnt - l_cnt)\n    }\n}"
      racket: "(define/contract (sum-game num)\n  (-> string? boolean?)\n  (let* ([n\
        \ (string-length num)]\n         [half (quotient n 2)])\n    (let-values ([(l-sum\
        \ l-cnt r-sum r-cnt)\n                  (for/fold ([ls 0] [lc 0] [rs 0] [rc\
        \ 0])\n                            ([i (in-range n)])\n                    (let\
        \ ([c (string-ref num i)])\n                      (if (< i half)\n         \
        \                 (if (char=? c #\\?)\n                              (values\
        \ ls (+ lc 1) rs rc)\n                              (values (+ ls (- (char->integer\
        \ c) (char->integer #\\0))) lc rs rc))\n                          (if (char=?\
        \ c #\\?)\n                              (values ls lc rs (+ rc 1))\n      \
        \                        (values ls lc (+ rs (- (char->integer c) (char->integer\
        \ #\\0))) rc)))))])\n      (not (= (* 2 (- l-sum r-sum)) (* 9 (- r-cnt l-cnt)))))))"
      erlang: "-spec sum_game(Num :: unicode:unicode_binary()) -> boolean().\nsum_game(Num)\
        \ ->\n    Len = byte_size(Num),\n    Half = Len div 2,\n    {LSum, LCnt} = sum_and_cnt(binary:part(Num,\
        \ 0, Half), 0, 0),\n    {RSum, RCnt} = sum_and_cnt(binary:part(Num, Half, Half),\
        \ 0, 0),\n    (2 * (LSum - RSum)) /= (9 * (RCnt - LCnt)).\n\nsum_and_cnt(<<>>,\
        \ Sum, Cnt) -> {Sum, Cnt};\nsum_and_cnt(<<Char, Rest/binary>>, Sum, Cnt) ->\n\
        \    if\n        Char =:= $? -> sum_and_cnt(Rest, Sum, Cnt + 1);\n        true\
        \ -> sum_and_cnt(Rest, Sum + (Char - $0), Cnt)\n    end."
      elixir: "defmodule Solution do\n  @spec sum_game(num :: String.t) :: boolean\n\
        \  def sum_game(num) do\n    len = String.length(num)\n    half_len = div(len,\
        \ 2)\n    {l_sum, l_cnt} = sum_and_cnt(String.slice(num, 0, half_len))\n   \
        \ {r_sum, r_cnt} = sum_and_cnt(String.slice(num, half_len, half_len))\n    2\
        \ * (l_sum - r_sum) != 9 * (r_cnt - l_cnt)\n  end\n\n  defp sum_and_cnt(s) do\n\
        \    s\n    |> String.to_charlist()\n    |> Enum.reduce({0, 0}, fn char, {sum,\
        \ cnt} ->\n      if char == ?? do\n        {sum, cnt + 1}\n      else\n    \
        \    {sum + (char - ?0), cnt}\n      end\n    end)\n  end\nend"
    approach: 'The problem can be modeled as a game theory problem where Alice and Bob
      take turns replacing ''?'' with digits. Bob wins if the final sums of the two
      halves are equal, and Alice wins otherwise. A crucial observation is that because
      they take turns and Alice starts first, Bob can win only if the total number of
      ''?'' is even. For every pair of ''?'' moves, Bob can employ a strategy to maintain
      balance: if Alice picks a digit $d$ on one side, Bob can either pick $d$ on the
      opposite side to keep the difference unchanged, or $9-d$ on the same side to make
      the pair sum to 9. This means that each pair of ''?'' effectively contributes
      an average of 4.5 to the sum of its side.'
    time_complexity: O(N) where N is the length of the string num. We iterate through
      the string exactly once to calculate the sums of digits and counts of '?' characters
      for both the first and second halves.
    space_complexity: O(1) because we only use a fixed number of integer variables to
      store the sums and counts, regardless of the size of the input string.
    elapsed_time: 259.92800188064575
    model: gemini-3-flash-preview
    generated_at: '2026-08-23 00:56:27 '
---

## Problem #1927: Sum Game

**Difficulty:** Medium

**Topics:** Math, String, Greedy, Game Theory

## Problem Description

<p>Alice and Bob take turns playing a game, with <strong>Alice</strong><strong>&nbsp;starting first</strong>.</p>

<p>You are given a string <code>num</code> of <strong>even length</strong> consisting of digits and <code>&#39;?&#39;</code> characters. On each turn, a player will do the following if there is still at least one <code>&#39;?&#39;</code> in <code>num</code>:</p>

<ol>
	<li>Choose an index <code>i</code> where <code>num[i] == &#39;?&#39;</code>.</li>
	<li>Replace <code>num[i]</code> with any digit between <code>&#39;0&#39;</code> and <code>&#39;9&#39;</code>.</li>
</ol>

<p>The game ends when there are no more <code>&#39;?&#39;</code> characters in <code>num</code>.</p>

<p>For Bob&nbsp;to win, the sum of the digits in the first half of <code>num</code> must be <strong>equal</strong> to the sum of the digits in the second half. For Alice&nbsp;to win, the sums must <strong>not be equal</strong>.</p>

<ul>
	<li>For example, if the game ended with <code>num = &quot;243801&quot;</code>, then Bob&nbsp;wins because <code>2+4+3 = 8+0+1</code>. If the game ended with <code>num = &quot;243803&quot;</code>, then Alice&nbsp;wins because <code>2+4+3 != 8+0+3</code>.</li>
</ul>

<p>Assuming Alice and Bob play <strong>optimally</strong>, return <code>true</code> <em>if Alice will win and </em><code>false</code> <em>if Bob will win</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = &quot;5023&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> There are no moves to be made.
The sum of the first half is equal to the sum of the second half: 5 + 0 = 2 + 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = &quot;25??&quot;
<strong>Output:</strong> true
<strong>Explanation: </strong>Alice can replace one of the &#39;?&#39;s with &#39;9&#39; and it will be impossible for Bob to make the sums equal.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> num = &quot;?3295???&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> It can be proven that Bob will always win. One possible outcome is:
- Alice replaces the first &#39;?&#39; with &#39;9&#39;. num = &quot;93295???&quot;.
- Bob replaces one of the &#39;?&#39; in the right half with &#39;9&#39;. num = &quot;932959??&quot;.
- Alice replaces one of the &#39;?&#39; in the right half with &#39;2&#39;. num = &quot;9329592?&quot;.
- Bob replaces the last &#39;?&#39; in the right half with &#39;7&#39;. num = &quot;93295927&quot;.
Bob wins because 9 + 3 + 2 + 9 = 5 + 9 + 2 + 7.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= num.length &lt;= 10<sup>5</sup></code></li>
	<li><code>num.length</code> is <strong>even</strong>.</li>
	<li><code>num</code> consists of only digits and <code>&#39;?&#39;</code>.</li>
</ul>


## Hints

1. Bob can always make the total sum of both sides equal in mod 9.

2. Why does the difference between the number of question marks on the left and right side matter?

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be modeled as a game theory problem where Alice and Bob take turns replacing '?' with digits. Bob wins if the final sums of the two halves are equal, and Alice wins otherwise. A crucial observation is that because they take turns and Alice starts first, Bob can win only if the total number of '?' is even. For every pair of '?' moves, Bob can employ a strategy to maintain balance: if Alice picks a digit $d$ on one side, Bob can either pick $d$ on the opposite side to keep the difference unchanged, or $9-d$ on the same side to make the pair sum to 9. This means that each pair of '?' effectively contributes an average of 4.5 to the sum of its side.

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
    bool sumGame(string num) {
        int n = num.length();
        int s1 = 0, s2 = 0, c1 = 0, c2 = 0;
        for (int i = 0; i < n / 2; ++i) {
            if (num[i] == '?') c1++;
            else s1 += num[i] - '0';
        }
        for (int i = n / 2; i < n; ++i) {
            if (num[i] == '?') c2++;
            else s2 += num[i] - '0';
        }
        return (2 * s1 + 9 * c1) != (2 * s2 + 9 * c2);
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean sumGame(String num) {
        int n = num.length();
        int s1 = 0, s2 = 0, c1 = 0, c2 = 0;
        for (int i = 0; i < n / 2; i++) {
            char ch = num.charAt(i);
            if (ch == '?') c1++;
            else s1 += ch - '0';
        }
        for (int i = n / 2; i < n; i++) {
            char ch = num.charAt(i);
            if (ch == '?') c2++;
            else s2 += ch - '0';
        }
        return (2 * s1 + 9 * c1) != (2 * s2 + 9 * c2);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        s1 = c1 = s2 = c2 = 0
        for i in range(n / 2):
            if num[i] == '?':
                c1 += 1
            else:
                s1 += int(num[i])
        for i in range(n / 2, n):
            if num[i] == '?':
                c2 += 1
            else:
                s2 += int(num[i])
        return 2 * s1 + 9 * c1 != 2 * s2 + 9 * c2
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        s1 = s2 = c1 = c2 = 0
        for i in range(n // 2):
            if num[i] == '?':
                c1 += 1
            else:
                s1 += int(num[i])
        for i in range(n // 2, n):
            if num[i] == '?':
                c2 += 1
            else:
                s2 += int(num[i])
        return 2 * s1 + 9 * c1 != 2 * s2 + 9 * c2
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdbool.h>
#include <string.h>

bool sumGame(char* num) {
    int n = (int)strlen(num);
    int s1 = 0, s2 = 0, c1 = 0, c2 = 0;
    for (int i = 0; i < n / 2; i++) {
        if (num[i] == '?') c1++;
        else s1 += num[i] - '0';
    }
    for (int i = n / 2; i < n; i++) {
        if (num[i] == '?') c2++;
        else s2 += num[i] - '0';
    }
    return (2 * s1 + 9 * c1) != (2 * s2 + 9 * c2);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool SumGame(string num) {
        int n = num.Length;
        int s1 = 0, c1 = 0, s2 = 0, c2 = 0;

        for (int i = 0; i < n; i++) {
            if (i < n / 2) {
                if (num[i] == '?') {
                    c1++;
                } else {
                    s1 += num[i] - '0';
                }
            } else {
                if (num[i] == '?') {
                    c2++;
                } else {
                    s2 += num[i] - '0';
                }
            }
        }

        // Bob wins if 2 * (s1 - s2) == 9 * (c2 - c1).
        // Otherwise, Alice wins (return true).
        return 2 * (s1 - s2) != 9 * (c2 - c1);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} num
 * @return {boolean}
 */
var sumGame = function(num) {
    const n = num.length;
    let s1 = 0, c1 = 0, s2 = 0, c2 = 0;

    for (let i = 0; i < n; i++) {
        if (i < n / 2) {
            if (num[i] === '?') {
                c1++;
            } else {
                s1 += num[i] - '0';
            }
        } else {
            if (num[i] === '?') {
                c2++;
            } else {
                s2 += num[i] - '0';
            }
        }
    }

    return 2 * (s1 - s2) !== 9 * (c2 - c1);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function sumGame(num: string): boolean {
    const n = num.length;
    let s1 = 0, c1 = 0, s2 = 0, c2 = 0;

    for (let i = 0; i < n; i++) {
        if (i < n / 2) {
            if (num[i] === '?') {
                c1++;
            } else {
                s1 += parseInt(num[i], 10);
            }
        } else {
            if (num[i] === '?') {
                c2++;
            }
        } 
    }

    // Recalculating sum and count logic to ensure correct iteration
    s1 = 0; c1 = 0; s2 = 0; c2 = 0;
    for (let i = 0; i < n; i++) {
        if (i < n / 2) {
            if (num[i] === '?') {
                c1++;
            } else {
                s1 += Number(num[i]);
            }
        } else {
            if (num[i] === '?') {
                c2++;
            } else {
                s2 += Number(num[i]);
            }
        }
    }

    return 2 * (s1 - s2) !== 9 * (c2 - c1);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String $num
     * @return Boolean
     */
    function sumGame($num) {
        $n = strlen($num);
        $s1 = 0; $c1 = 0; $s2 = 0; $c2 = 0;

        for ($i = 0; $i < $n; $i++) {
            if ($i < $n / 2) {
                if ($num[$i] === '?') {
                    $c1++;
                } else {
                    $s1 += intval($num[$i]);
                }
            } else {
                if ($num[$i] === '?') {
                    $c2++;
                } else {
                    $s2 += intval($num[$i]);
                }
            }
        }

        return 2 * ($s1 - $s2) !== 9 * ($c2 - $c1);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func sumGame(_ num: String) -> Bool {
        let n = num.count
        var s1 = 0, c1 = 0, s2 = 0, c2 = 0
        var i = 0

        for char in num {
            if i < n / 2 {
                if char == "?" {
                    c1 += 1
                } else if let digit = char.wholeNumberValue {
                    s1 += digit
                }
            } else {
                if char == "?" {
                    c2 += 1
                } else if let digit = char.wholeNumberValue {
                    s2 += digit
                }
            }
            i += 1
        }

        return 2 * (s1 - s2) != 9 * (c2 - c1)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun sumGame(num: String): Boolean {
        val n = num.length
        var diffS = 0
        var diffQ = 0
        for (i in 0 until n / 2) {
            if (num[i] == '?') {
                diffQ--
            } else {
                diffS += num[i] - '0'
            }
        }
        for (i in n / 2 until n) {
            if (num[i] == '?') {
                diffQ++
            } else {
                diffS -= num[i] - '0'
            }
        }
        return 2 * diffS != 9 * diffQ
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool sumGame(String num) {
    int n = num.length;
    int diffS = 0;
    int diffQ = 0;
    for (int i = 0; i < n ~/ 2; i++) {
      if (num[i] == '?') {
        diffQ--;
      } else {
        diffS += int.parse(num[i]);
      }
    }
    for (int i = n ~/ 2; i < n; i++) {
      if (num[i] == '?') {
        diffQ++;
      } else {
        diffS -= int.parse(num[i]);
      }
    }
    return 2 * diffS != 9 * diffQ;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func sumGame(num string) bool {
    n := len(num)
    diffS := 0
    diffQ := 0
    for i := 0; i < n/2; i++ {
        if num[i] == '?' {
            diffQ--
        } else {
            diffS += int(num[i] - '0')
        }
    }
    for i := n/2; i < n; i++ {
        if num[i] == '?' {
            diffQ++
        } else {
            diffS -= int(num[i] - '0')
        }
    }
    return 2*diffS != 9*diffQ
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} num
# @return {Boolean}
def sum_game(num)
    n = num.length
    diff_s = 0
    diff_q = 0
    (0...(n / 2)).each do |i|
        if num[i] == '?'
            diff_q -= 1
        else
            diff_s += num[i].to_i
        end
    end
    ((n / 2)...n).each do |i|
        if num[i] == '?'
            diff_q += 1
        else
            diff_s -= num[i].to_i
        end
    end
    2 * diff_s != 9 * diff_q
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def sumGame(num: String): Boolean = {
        val n = num.length
        var diffS = 0
        var diffQ = 0
        for (i <- 0 until n / 2) {
            if (num(i) == '?') {
                diffQ -= 1
            } else {
                diffS += num(i).asDigit
            }
        }
        for (i <- n / 2 until n) {
            if (num(i) == '?') {
                diffQ += 1
            } else {
                diffS -= num(i).asDigit
            }
        }
        2 * diffS != 9 * diffQ
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn sum_game(num: String) -> bool {
        let n = num.len();
        let bytes = num.as_bytes();
        let mut l_sum = 0i32;
        let mut l_cnt = 0i32;
        let mut r_sum = 0i32;
        let mut r_cnt = 0i32;

        for i in 0..n / 2 {
            if bytes[i] == b'?' {
                l_cnt += 1;
            } else {
                l_sum += (bytes[i] - b'0') as i32;
            }
        }
        for i in n / 2..n {
            if bytes[i] == b'?' {
                r_cnt += 1;
            } else {
                r_sum += (bytes[i] - b'0') as i32;
            }
        }

        2 * (l_sum - r_sum) != 9 * (r_cnt - l_cnt)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (sum-game num)
  (-> string? boolean?)
  (let* ([n (string-length num)]
         [half (quotient n 2)])
    (let-values ([(l-sum l-cnt r-sum r-cnt)
                  (for/fold ([ls 0] [lc 0] [rs 0] [rc 0])
                            ([i (in-range n)])
                    (let ([c (string-ref num i)])
                      (if (< i half)
                          (if (char=? c #\?)
                              (values ls (+ lc 1) rs rc)
                              (values (+ ls (- (char->integer c) (char->integer #\0))) lc rs rc))
                          (if (char=? c #\?)
                              (values ls lc rs (+ rc 1))
                              (values ls lc (+ rs (- (char->integer c) (char->integer #\0))) rc)))))])
      (not (= (* 2 (- l-sum r-sum)) (* 9 (- r-cnt l-cnt)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec sum_game(Num :: unicode:unicode_binary()) -> boolean().
sum_game(Num) ->
    Len = byte_size(Num),
    Half = Len div 2,
    {LSum, LCnt} = sum_and_cnt(binary:part(Num, 0, Half), 0, 0),
    {RSum, RCnt} = sum_and_cnt(binary:part(Num, Half, Half), 0, 0),
    (2 * (LSum - RSum)) /= (9 * (RCnt - LCnt)).

sum_and_cnt(<<>>, Sum, Cnt) -> {Sum, Cnt};
sum_and_cnt(<<Char, Rest/binary>>, Sum, Cnt) ->
    if
        Char =:= $? -> sum_and_cnt(Rest, Sum, Cnt + 1);
        true -> sum_and_cnt(Rest, Sum + (Char - $0), Cnt)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec sum_game(num :: String.t) :: boolean
  def sum_game(num) do
    len = String.length(num)
    half_len = div(len, 2)
    {l_sum, l_cnt} = sum_and_cnt(String.slice(num, 0, half_len))
    {r_sum, r_cnt} = sum_and_cnt(String.slice(num, half_len, half_len))
    2 * (l_sum - r_sum) != 9 * (r_cnt - l_cnt)
  end

  defp sum_and_cnt(s) do
    s
    |> String.to_charlist()
    |> Enum.reduce({0, 0}, fn char, {sum, cnt} ->
      if char == ?? do
        {sum, cnt + 1}
      else
        {sum + (char - ?0), cnt}
      end
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) where N is the length of the string num. We iterate through the string exactly once to calculate the sums of digits and counts of '?' characters for both the first and second halves.
- **Space Complexity:** O(1) because we only use a fixed number of integer variables to store the sums and counts, regardless of the size of the input string.
