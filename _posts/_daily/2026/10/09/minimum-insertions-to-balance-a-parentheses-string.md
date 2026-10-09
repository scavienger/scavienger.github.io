---
layout: post
title: "Minimum Insertions to Balance a Parentheses String"
date: 2026-10-09 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Stack", "Greedy", "Bracket Sequences"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minInsertions(string s) {\n        int\
        \ res = 0;\n        int rightNeeded = 0;\n        for (char c : s) {\n     \
        \       if (c == '(') {\n                rightNeeded += 2;\n               \
        \ if (rightNeeded % 2 != 0) {\n                    res++;\n                \
        \    rightNeeded--;\n                }\n            } else {\n             \
        \   rightNeeded--;\n                if (rightNeeded == -1) {\n             \
        \       res++;\n                    rightNeeded = 1;\n                }\n  \
        \          }\n        }\n        return res + rightNeeded;\n    }\n};"
      java: "class Solution {\n    public int minInsertions(String s) {\n        int\
        \ res = 0;\n        int rightNeeded = 0;\n        for (int i = 0; i < s.length();\
        \ i++) {\n            char c = s.charAt(i);\n            if (c == '(') {\n \
        \               rightNeeded += 2;\n                if (rightNeeded % 2 != 0)\
        \ {\n                    res++;\n                    rightNeeded--;\n      \
        \          }\n            } else {\n                rightNeeded--;\n       \
        \         if (rightNeeded == -1) {\n                    res++;\n           \
        \         rightNeeded = 1;\n                }\n            }\n        }\n  \
        \      return res + rightNeeded;\n    }\n}"
      python: "class Solution(object):\n    def minInsertions(self, s):\n        \"\"\
        \"\n        :type s: str\n        :rtype: int\n        \"\"\"\n        res =\
        \ 0\n        right_needed = 0\n        for char in s:\n            if char ==\
        \ '(':\n                right_needed += 2\n                if right_needed %\
        \ 2 != 0:\n                    res += 1\n                    right_needed -=\
        \ 1\n            else:\n                right_needed -= 1\n                if\
        \ right_needed == -1:\n                    res += 1\n                    right_needed\
        \ = 1\n        return res + right_needed"
      python3: "class Solution:\n    def minInsertions(self, s: str) -> int:\n     \
        \   res = 0\n        right_needed = 0\n        for char in s:\n            if\
        \ char == '(':\n                right_needed += 2\n                if right_needed\
        \ % 2 != 0:\n                    res += 1\n                    right_needed\
        \ -= 1\n            else:\n                right_needed -= 1\n             \
        \   if right_needed == -1:\n                    res += 1\n                 \
        \   right_needed = 1\n        return res + right_needed"
      c: "int minInsertions(char* s) {\n    int res = 0;\n    int rightNeeded = 0;\n\
        \    for (int i = 0; s[i] != '\\0'; i++) {\n        if (s[i] == '(') {\n   \
        \         rightNeeded += 2;\n            if (rightNeeded % 2 != 0) {\n     \
        \           res++;\n                rightNeeded--;\n            }\n        }\
        \ else {\n            rightNeeded--;\n            if (rightNeeded == -1) {\n\
        \                res++;\n                rightNeeded = 1;\n            }\n \
        \       }\n    }\n    return res + rightNeeded;\n}"
      csharp: "public class Solution {\n    public int MinInsertions(string s) {\n \
        \       int res = 0;\n        int rightNeeded = 0;\n        foreach (char c\
        \ in s) {\n            if (c == '(') {\n                if (rightNeeded % 2\
        \ != 0) {\n                    res++;\n                    rightNeeded--;\n\
        \                }\n                rightNeeded += 2;\n            } else {\n\
        \                rightNeeded--;\n                if (rightNeeded < 0) {\n  \
        \                  res++;\n                    rightNeeded += 2;\n         \
        \       }\n            }\n        }\n        return res + rightNeeded;\n   \
        \ }\n}"
      javascript: "/**\n * @param {string} s\n * @return {number}\n */\nvar minInsertions\
        \ = function(s) {\n    let res = 0;\n    let rightNeeded = 0;\n    for (let\
        \ i = 0; i < s.length; i++) {\n        const c = s[i];\n        if (c === '(')\
        \ {\n            if (rightNeeded % 2 !== 0) {\n                res++;\n    \
        \            rightNeeded--;\n            }\n            rightNeeded += 2;\n\
        \        } else {\n            rightNeeded--;\n            if (rightNeeded <\
        \ 0) {\n                res++;\n                rightNeeded += 2;\n        \
        \    }\n        }\n    }\n    return res + rightNeeded;\n};"
      typescript: "function minInsertions(s: string): number {\n    let res = 0;\n \
        \   let rightNeeded = 0;\n    for (let i = 0; i < s.length; i++) {\n       \
        \ const c = s[i];\n        if (c === '(') {\n            if (rightNeeded % 2\
        \ !== 0) {\n                res++;\n                rightNeeded--;\n       \
        \     }\n            rightNeeded += 2;\n        } else {\n            rightNeeded--;\n\
        \            if (rightNeeded < 0) {\n                res++;\n              \
        \  rightNeeded += 2;\n            }\n        }\n    }\n    return res + rightNeeded;\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return Integer\n\
        \     */\n    function minInsertions($s) {\n        $res = 0;\n        $rightNeeded\
        \ = 0;\n        $len = strlen($s);\n        for ($i = 0; $i < $len; $i++) {\n\
        \            $c = $s[$i];\n            if ($c == '(') {\n                if\
        \ ($rightNeeded % 2 != 0) {\n                    $res++;\n                 \
        \   $rightNeeded--;\n                }\n                $rightNeeded += 2;\n\
        \            } else {\n                $rightNeeded--;\n                if ($rightNeeded\
        \ < 0) {\n                    $res++;\n                    $rightNeeded += 2;\n\
        \                }\n            }\n        }\n        return $res + $rightNeeded;\n\
        \    }\n}"
      swift: "class Solution {\n    func minInsertions(_ s: String) -> Int {\n     \
        \   var res = 0\n        var rightNeeded = 0\n        for c in s {\n       \
        \     if c == \"(\" {\n                if rightNeeded % 2 != 0 {\n         \
        \           res += 1\n                    rightNeeded -= 1\n               \
        \ }\n                rightNeeded += 2\n            } else {\n              \
        \  rightNeeded -= 1\n                if rightNeeded < 0 {\n                \
        \    res += 1\n                    rightNeeded += 2\n                }\n   \
        \         }\n        }\n        return res + rightNeeded\n    }\n}"
      kotlin: "class Solution {\n    fun minInsertions(s: String): Int {\n        var\
        \ res = 0\n        var needed = 0\n        for (c in s) {\n            if (c\
        \ == '(') {\n                needed += 2\n                if (needed % 2 !=\
        \ 0) {\n                    res++\n                    needed--\n          \
        \      }\n            } else {\n                needed--\n                if\
        \ (needed == -1) {\n                    res++\n                    needed =\
        \ 1\n                }\n            }\n        }\n        return res + needed\n\
        \    }\n}"
      dart: "class Solution {\n  int minInsertions(String s) {\n    int res = 0;\n \
        \   int needed = 0;\n    for (int i = 0; i < s.length; i++) {\n      if (s[i]\
        \ == '(') {\n        needed += 2;\n        if (needed % 2 != 0) {\n        \
        \  res++;\n          needed--;\n        }\n      } else {\n        needed--;\n\
        \        if (needed == -1) {\n          res++;\n          needed = 1;\n    \
        \    }\n      }\n    }\n    return res + needed;\n  }\n}"
      go: "func minInsertions(s string) int {\n    res := 0\n    needed := 0\n    for\
        \ _, c := range s {\n        if c == '(' {\n            needed += 2\n      \
        \      if needed%2 != 0 {\n                res++\n                needed--\n\
        \            }\n        } else {\n            needed--\n            if needed\
        \ == -1 {\n                res++\n                needed = 1\n            }\n\
        \        }\n    }\n    return res + needed\n}"
      ruby: "# @param {String} s\n# @return {Integer}\ndef min_insertions(s)\n    res\
        \ = 0\n    needed = 0\n    s.each_char do |c|\n        if c == '('\n       \
        \     needed += 2\n            if needed % 2 != 0\n                res += 1\n\
        \                needed -= 1\n            end\n        else\n            needed\
        \ -= 1\n            if needed == -1\n                res += 1\n            \
        \    needed = 1\n            end\n        end\n    end\n    res + needed\nend"
      scala: "object Solution {\n    def minInsertions(s: String): Int = {\n       \
        \ var res = 0\n        var needed = 0\n        for (c <- s) {\n            if\
        \ (c == '(') {\n                needed += 2\n                if (needed % 2\
        \ != 0) {\n                    res += 1\n                    needed -= 1\n \
        \               }\n            } else {\n                needed -= 1\n     \
        \           if (needed == -1) {\n                    res += 1\n            \
        \        needed = 1\n                }\n            }\n        }\n        res\
        \ + needed\n    }\n}"
      rust: "impl Solution {\n    pub fn min_insertions(s: String) -> i32 {\n      \
        \  let s_bytes = s.as_bytes();\n        let mut i = 0;\n        let mut open_count:\
        \ i32 = 0;\n        let mut insertions: i32 = 0;\n\n        while i < s_bytes.len()\
        \ {\n            if s_bytes[i] == b'(' {\n                open_count += 1;\n\
        \            } else {\n                if i + 1 < s_bytes.len() && s_bytes[i\
        \ + 1] == b')' {\n                    if open_count > 0 {\n                \
        \        open_count -= 1;\n                    } else {\n                  \
        \      insertions += 1;\n                    }\n                    i += 1;\n\
        \                } else {\n                    if open_count > 0 {\n       \
        \                 open_count -= 1;\n                        insertions += 1;\n\
        \                    } else {\n                        insertions += 2;\n  \
        \                  }\n                }\n            }\n            i += 1;\n\
        \        }\n\n        insertions + (open_count * 2)\n    }\n}"
      racket: "(define/contract (min-insertions s)\n  (-> string? exact-integer?)\n\
        \  (let loop ([l (string->list s)] [open-count 0] [insertions 0])\n    (cond\n\
        \      [(null? l) (+ insertions (* open-count 2))]\n      [(char=? (car l) #\\\
        () (loop (cdr l) (+ open-count 1) insertions)]\n      [else\n       (if (and\
        \ (not (null? (cdr l))) (char=? (car (cdr l)) #\\)))\n           (if (> open-count\
        \ 0)\n               (loop (cdr (cdr l)) (- open-count 1) insertions)\n    \
        \           (loop (cdr (cdr l)) open-count (+ insertions 1)))\n           (if\
        \ (> open-count 0)\n               (loop (cdr l) (- open-count 1) (+ insertions\
        \ 1))\n               (loop (cdr l) open-count (+ insertions 2)))])))"
      erlang: "-spec min_insertions(S :: unicode:unicode_binary()) -> integer().\nmin_insertions(S)\
        \ ->\n  L = binary_to_list(S),\n  min_solve(L, 0, 0).\n\nmin_solve([], OpenCount,\
        \ Insertions) ->\n  Insertions + OpenCount * 2;\nmin_solve([$( | Rest], OpenCount,\
        \ Insertions) ->\n  min_solve(Rest, OpenCount + 1, Insertions);\nmin_solve([$),\
        \ $) | Rest], OpenCount, Insertions) ->\n  if\n    OpenCount > 0 -> min_solve(Rest,\
        \ OpenCount - 1, Insertions);\n    true -> min_solve(Rest, OpenCount, Insertions\
        \ + 1)\n  end;\nmin_solve([$) | Rest], OpenCount, Insertions) ->\n  if\n   \
        \ OpenCount > 0 -> min_solve(Rest, OpenCount - 1, Insertions + 1);\n    true\
        \ -> min_solve(Rest, OpenCount, Insertions + 2)\n  end."
      elixir: "defmodule Solution do\n  @spec min_insertions(s :: String.t) :: integer\n\
        \  def min_insertions(s) do\n    solve(String.to_charlist(s), 0, 0)\n  end\n\
        \n  defp solve([], open_count, insertions) do\n    insertions + open_count *\
        \ 2\n  end\n\n  defp solve([?( | rest], open_count, insertions) do\n    solve(rest,\
        \ open_count + 1, insertions)\n  end\n\n  defp solve([?), ?) | rest], open_count,\
        \ insertions) do\n    if open_count > 0 do\n      solve(rest, open_count - 1,\
        \ insertions)\n    else\n      solve(rest, 0, insertions + 1)\n    end\n  end\n\
        \n  defp solve([?) | rest], open_count, insertions) do\n    if open_count >\
        \ 0 do\n      solve(rest, open_count - 1, insertions + 1)\n    else\n      solve(rest,\
        \ 0, insertions + 2)\n    end\n  end\nend"
    approach: The algorithm uses a greedy approach to keep track of the number of required
      closing parentheses ')' needed to balance the opening parentheses '(' encountered
      so far. We maintain a counter `rightNeeded` to represent the deficit of ')' and
      a counter `res` for the total insertions performed. When an opening parenthesis
      '(' is found, we increment `rightNeeded` by 2, as each '(' requires a corresponding
      pair of '))'. If `rightNeeded` was odd before this increment (or becomes odd after),
      it indicates that a single ')' was previously pending; we must immediately insert
      one ')' to complete that unit (increment `res` and decrement `rightNeeded`) because
      the current '(' cannot satisfy the previous '(''s requirement.
    time_complexity: 'O(n) with one-paragraph explanation: The algorithm iterates through
      the string `s` exactly once, performing a constant number of arithmetic and comparison
      operations for each character. Thus, the time complexity scales linearly with
      the length of the input string.'
    space_complexity: 'O(1) with one-paragraph explanation: The solution only uses a
      fixed number of integer variables (`res` and `rightNeeded`) to track the state,
      regardless of the input size. No additional data structures like stacks or arrays
      are required.'
    elapsed_time: 481.81954741477966
    model: gemini-3-flash-preview
    generated_at: '2026-10-09 04:03:15 '
---

## Problem #1541: Minimum Insertions to Balance a Parentheses String

**Difficulty:** Medium

**Topics:** String, Stack, Greedy, Bracket Sequences

## Problem Description

<p>Given a parentheses string <code>s</code> containing only the characters <code>&#39;(&#39;</code> and <code>&#39;)&#39;</code>. A parentheses string is <strong>balanced</strong> if:</p>

<ul>
	<li>Any left parenthesis <code>&#39;(&#39;</code> must have a corresponding two consecutive right parenthesis <code>&#39;))&#39;</code>.</li>
	<li>Left parenthesis <code>&#39;(&#39;</code> must go before the corresponding two consecutive right parenthesis <code>&#39;))&#39;</code>.</li>
</ul>

<p>In other words, we treat <code>&#39;(&#39;</code> as an opening parenthesis and <code>&#39;))&#39;</code> as a closing parenthesis.</p>

<ul>
	<li>For example, <code>&quot;())&quot;</code>, <code>&quot;())(())))&quot;</code> and <code>&quot;(())())))&quot;</code> are balanced, <code>&quot;)()&quot;</code>, <code>&quot;()))&quot;</code> and <code>&quot;(()))&quot;</code> are not balanced.</li>
</ul>

<p>You can insert the characters <code>&#39;(&#39;</code> and <code>&#39;)&#39;</code> at any position of the string to balance it if needed.</p>

<p>Return <em>the minimum number of insertions</em> needed to make <code>s</code> balanced.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(()))&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> The second &#39;(&#39; has two matching &#39;))&#39;, but the first &#39;(&#39; has only &#39;)&#39; matching. We need to add one more &#39;)&#39; at the end of the string to be &quot;(())))&quot; which is balanced.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;())&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> The string is already balanced.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;))())(&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> Add &#39;(&#39; to match the first &#39;))&#39;, Add &#39;))&#39; to match the last &#39;(&#39;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of <code>&#39;(&#39;</code> and <code>&#39;)&#39;</code> only.</li>
</ul>


## Hints

1. Use a stack to keep opening brackets. If you face single closing ')' add 1 to the answer and consider it as '))'.

2. If you have '))' with empty stack, add 1 to the answer, If after finishing you have x opening remaining in the stack, add 2x to the answer.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm uses a greedy approach to keep track of the number of required closing parentheses ')' needed to balance the opening parentheses '(' encountered so far. We maintain a counter `rightNeeded` to represent the deficit of ')' and a counter `res` for the total insertions performed. When an opening parenthesis '(' is found, we increment `rightNeeded` by 2, as each '(' requires a corresponding pair of '))'. If `rightNeeded` was odd before this increment (or becomes odd after), it indicates that a single ')' was previously pending; we must immediately insert one ')' to complete that unit (increment `res` and decrement `rightNeeded`) because the current '(' cannot satisfy the previous '(''s requirement.

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
    int minInsertions(string s) {
        int res = 0;
        int rightNeeded = 0;
        for (char c : s) {
            if (c == '(') {
                rightNeeded += 2;
                if (rightNeeded % 2 != 0) {
                    res++;
                    rightNeeded--;
                }
            } else {
                rightNeeded--;
                if (rightNeeded == -1) {
                    res++;
                    rightNeeded = 1;
                }
            }
        }
        return res + rightNeeded;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minInsertions(String s) {
        int res = 0;
        int rightNeeded = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                rightNeeded += 2;
                if (rightNeeded % 2 != 0) {
                    res++;
                    rightNeeded--;
                }
            } else {
                rightNeeded--;
                if (rightNeeded == -1) {
                    res++;
                    rightNeeded = 1;
                }
            }
        }
        return res + rightNeeded;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        right_needed = 0
        for char in s:
            if char == '(':
                right_needed += 2
                if right_needed % 2 != 0:
                    res += 1
                    right_needed -= 1
            else:
                right_needed -= 1
                if right_needed == -1:
                    res += 1
                    right_needed = 1
        return res + right_needed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        right_needed = 0
        for char in s:
            if char == '(':
                right_needed += 2
                if right_needed % 2 != 0:
                    res += 1
                    right_needed -= 1
            else:
                right_needed -= 1
                if right_needed == -1:
                    res += 1
                    right_needed = 1
        return res + right_needed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int minInsertions(char* s) {
    int res = 0;
    int rightNeeded = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '(') {
            rightNeeded += 2;
            if (rightNeeded % 2 != 0) {
                res++;
                rightNeeded--;
            }
        } else {
            rightNeeded--;
            if (rightNeeded == -1) {
                res++;
                rightNeeded = 1;
            }
        }
    }
    return res + rightNeeded;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinInsertions(string s) {
        int res = 0;
        int rightNeeded = 0;
        foreach (char c in s) {
            if (c == '(') {
                if (rightNeeded % 2 != 0) {
                    res++;
                    rightNeeded--;
                }
                rightNeeded += 2;
            } else {
                rightNeeded--;
                if (rightNeeded < 0) {
                    res++;
                    rightNeeded += 2;
                }
            }
        }
        return res + rightNeeded;
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
var minInsertions = function(s) {
    let res = 0;
    let rightNeeded = 0;
    for (let i = 0; i < s.length; i++) {
        const c = s[i];
        if (c === '(') {
            if (rightNeeded % 2 !== 0) {
                res++;
                rightNeeded--;
            }
            rightNeeded += 2;
        } else {
            rightNeeded--;
            if (rightNeeded < 0) {
                res++;
                rightNeeded += 2;
            }
        }
    }
    return res + rightNeeded;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minInsertions(s: string): number {
    let res = 0;
    let rightNeeded = 0;
    for (let i = 0; i < s.length; i++) {
        const c = s[i];
        if (c === '(') {
            if (rightNeeded % 2 !== 0) {
                res++;
                rightNeeded--;
            }
            rightNeeded += 2;
        } else {
            rightNeeded--;
            if (rightNeeded < 0) {
                res++;
                rightNeeded += 2;
            }
        }
    }
    return res + rightNeeded;
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
    function minInsertions($s) {
        $res = 0;
        $rightNeeded = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            if ($c == '(') {
                if ($rightNeeded % 2 != 0) {
                    $res++;
                    $rightNeeded--;
                }
                $rightNeeded += 2;
            } else {
                $rightNeeded--;
                if ($rightNeeded < 0) {
                    $res++;
                    $rightNeeded += 2;
                }
            }
        }
        return $res + $rightNeeded;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minInsertions(_ s: String) -> Int {
        var res = 0
        var rightNeeded = 0
        for c in s {
            if c == "(" {
                if rightNeeded % 2 != 0 {
                    res += 1
                    rightNeeded -= 1
                }
                rightNeeded += 2
            } else {
                rightNeeded -= 1
                if rightNeeded < 0 {
                    res += 1
                    rightNeeded += 2
                }
            }
        }
        return res + rightNeeded
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minInsertions(s: String): Int {
        var res = 0
        var needed = 0
        for (c in s) {
            if (c == '(') {
                needed += 2
                if (needed % 2 != 0) {
                    res++
                    needed--
                }
            } else {
                needed--
                if (needed == -1) {
                    res++
                    needed = 1
                }
            }
        }
        return res + needed
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minInsertions(String s) {
    int res = 0;
    int needed = 0;
    for (int i = 0; i < s.length; i++) {
      if (s[i] == '(') {
        needed += 2;
        if (needed % 2 != 0) {
          res++;
          needed--;
        }
      } else {
        needed--;
        if (needed == -1) {
          res++;
          needed = 1;
        }
      }
    }
    return res + needed;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minInsertions(s string) int {
    res := 0
    needed := 0
    for _, c := range s {
        if c == '(' {
            needed += 2
            if needed%2 != 0 {
                res++
                needed--
            }
        } else {
            needed--
            if needed == -1 {
                res++
                needed = 1
            }
        }
    }
    return res + needed
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @return {Integer}
def min_insertions(s)
    res = 0
    needed = 0
    s.each_char do |c|
        if c == '('
            needed += 2
            if needed % 2 != 0
                res += 1
                needed -= 1
            end
        else
            needed -= 1
            if needed == -1
                res += 1
                needed = 1
            end
        end
    end
    res + needed
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minInsertions(s: String): Int = {
        var res = 0
        var needed = 0
        for (c <- s) {
            if (c == '(') {
                needed += 2
                if (needed % 2 != 0) {
                    res += 1
                    needed -= 1
                }
            } else {
                needed -= 1
                if (needed == -1) {
                    res += 1
                    needed = 1
                }
            }
        }
        res + needed
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_insertions(s: String) -> i32 {
        let s_bytes = s.as_bytes();
        let mut i = 0;
        let mut open_count: i32 = 0;
        let mut insertions: i32 = 0;

        while i < s_bytes.len() {
            if s_bytes[i] == b'(' {
                open_count += 1;
            } else {
                if i + 1 < s_bytes.len() && s_bytes[i + 1] == b')' {
                    if open_count > 0 {
                        open_count -= 1;
                    } else {
                        insertions += 1;
                    }
                    i += 1;
                } else {
                    if open_count > 0 {
                        open_count -= 1;
                        insertions += 1;
                    } else {
                        insertions += 2;
                    }
                }
            }
            i += 1;
        }

        insertions + (open_count * 2)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-insertions s)
  (-> string? exact-integer?)
  (let loop ([l (string->list s)] [open-count 0] [insertions 0])
    (cond
      [(null? l) (+ insertions (* open-count 2))]
      [(char=? (car l) #\() (loop (cdr l) (+ open-count 1) insertions)]
      [else
       (if (and (not (null? (cdr l))) (char=? (car (cdr l)) #\)))
           (if (> open-count 0)
               (loop (cdr (cdr l)) (- open-count 1) insertions)
               (loop (cdr (cdr l)) open-count (+ insertions 1)))
           (if (> open-count 0)
               (loop (cdr l) (- open-count 1) (+ insertions 1))
               (loop (cdr l) open-count (+ insertions 2)))])))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_insertions(S :: unicode:unicode_binary()) -> integer().
min_insertions(S) ->
  L = binary_to_list(S),
  min_solve(L, 0, 0).

min_solve([], OpenCount, Insertions) ->
  Insertions + OpenCount * 2;
min_solve([$( | Rest], OpenCount, Insertions) ->
  min_solve(Rest, OpenCount + 1, Insertions);
min_solve([$), $) | Rest], OpenCount, Insertions) ->
  if
    OpenCount > 0 -> min_solve(Rest, OpenCount - 1, Insertions);
    true -> min_solve(Rest, OpenCount, Insertions + 1)
  end;
min_solve([$) | Rest], OpenCount, Insertions) ->
  if
    OpenCount > 0 -> min_solve(Rest, OpenCount - 1, Insertions + 1);
    true -> min_solve(Rest, OpenCount, Insertions + 2)
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_insertions(s :: String.t) :: integer
  def min_insertions(s) do
    solve(String.to_charlist(s), 0, 0)
  end

  defp solve([], open_count, insertions) do
    insertions + open_count * 2
  end

  defp solve([?( | rest], open_count, insertions) do
    solve(rest, open_count + 1, insertions)
  end

  defp solve([?), ?) | rest], open_count, insertions) do
    if open_count > 0 do
      solve(rest, open_count - 1, insertions)
    else
      solve(rest, 0, insertions + 1)
    end
  end

  defp solve([?) | rest], open_count, insertions) do
    if open_count > 0 do
      solve(rest, open_count - 1, insertions + 1)
    else
      solve(rest, 0, insertions + 2)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) with one-paragraph explanation: The algorithm iterates through the string `s` exactly once, performing a constant number of arithmetic and comparison operations for each character. Thus, the time complexity scales linearly with the length of the input string.
- **Space Complexity:** O(1) with one-paragraph explanation: The solution only uses a fixed number of integer variables (`res` and `rightNeeded`) to track the state, regardless of the input size. No additional data structures like stacks or arrays are required.
