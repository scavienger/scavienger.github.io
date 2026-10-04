---
layout: post
title: "Valid Parenthesis String"
date: 2026-10-04 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Dynamic Programming", "Stack", "Greedy", "Bracket Sequences"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/valid-parenthesis-string/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool checkValidString(string s) {\n     \
        \   int low = 0, high = 0;\n        for (char c : s) {\n            if (c ==\
        \ '(') {\n                low++;\n                high++;\n            } else\
        \ if (c == ')') {\n                low--;\n                high--;\n       \
        \     } else {\n                low--;\n                high++;\n          \
        \  }\n            if (high < 0) return false;\n            if (low < 0) low\
        \ = 0;\n        }\n        return low == 0;\n    }\n};"
      java: "class Solution {\n    public boolean checkValidString(String s) {\n   \
        \     int low = 0, high = 0;\n        for (int i = 0; i < s.length(); i++) {\n\
        \            char c = s.charAt(i);\n            if (c == '(') {\n          \
        \      low++;\n                high++;\n            } else if (c == ')') {\n\
        \                low--;\n                high--;\n            } else {\n   \
        \             low--;\n                high++;\n            }\n            if\
        \ (high < 0) return false;\n            if (low < 0) low = 0;\n        }\n \
        \       return low == 0;\n    }\n}"
      python: "class Solution(object):\n    def checkValidString(self, s):\n       \
        \ \"\"\"\n        :type s: str\n        :rtype: bool\n        \"\"\"\n     \
        \   low = 0\n        high = 0\n        for char in s:\n            if char ==\
        \ '(':\n                low += 1\n                high += 1\n            elif\
        \ char == ')':\n                low -= 1\n                high -= 1\n      \
        \      else:\n                low -= 1\n                high += 1\n        \
        \    if high < 0:\n                return False\n            if low < 0:\n \
        \               low = 0\n        return low == 0"
      python3: "class Solution:\n    def checkValidString(self, s: str) -> bool:\n \
        \       low = 0\n        high = 0\n        for char in s:\n            if char\
        \ == '(':\n                low += 1\n                high += 1\n           \
        \ elif char == ')':\n                low -= 1\n                high -= 1\n \
        \           else:\n                low -= 1\n                high += 1\n   \
        \         if high < 0:\n                return False\n            if low < 0:\n\
        \                low = 0\n        return low == 0"
      c: "#include <stdbool.h>\n\nbool checkValidString(char* s) {\n    int low = 0,\
        \ high = 0;\n    for (int i = 0; s[i] != '\\0'; i++) {\n        if (s[i] ==\
        \ '(') {\n            low++;\n            high++;\n        } else if (s[i] ==\
        \ ')') {\n            low--;\n            high--;\n        } else {\n      \
        \      low--;\n            high++;\n        }\n        if (high < 0) return\
        \ false;\n        if (low < 0) low = 0;\n    }\n    return low == 0;\n}"
      csharp: "public class Solution {\n    public bool CheckValidString(string s) {\n\
        \        int low = 0;\n        int high = 0;\n        foreach (char c in s)\
        \ {\n            if (c == '(') {\n                low++;\n                high++;\n\
        \            } else if (c == ')') {\n                low--;\n              \
        \  high--;\n            } else {\n                low--;\n                high++;\n\
        \            }\n            if (high < 0) {\n                return false;\n\
        \            }\n            if (low < 0) {\n                low = 0;\n     \
        \       }\n        }\n        return low == 0;\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {boolean}\n */\nvar checkValidString\
        \ = function(s) {\n    let low = 0;\n    let high = 0;\n    for (let i = 0;\
        \ i < s.length; i++) {\n        let char = s[i];\n        if (char === '(')\
        \ {\n            low++;\n            high++;\n        } else if (char === ')')\
        \ {\n            low--;\n            high--;\n        } else {\n           \
        \ low--;\n            high++;\n        }\n        if (high < 0) {\n        \
        \    return false;\n        }\n        if (low < 0) {\n            low = 0;\n\
        \        }\n    }\n    return low === 0;\n};"
      typescript: "function checkValidString(s: string): boolean {\n    let low: number\
        \ = 0;\n    let high: number = 0;\n    for (let i: number = 0; i < s.length;\
        \ i++) {\n        let char: string = s[i];\n        if (char === '(') {\n  \
        \          low++;\n            high++;\n        } else if (char === ')') {\n\
        \            low--;\n            high--;\n        } else {\n            low--;\n\
        \            high++;\n        }\n        if (high < 0) {\n            return\
        \ false;\n        }\n        if (low < 0) {\n            low = 0;\n        }\n\
        \    }\n    return low === 0;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return Boolean\n\
        \     */\n    function checkValidString($s) {\n        $low = 0;\n        $high\
        \ = 0;\n        $n = strlen($s);\n        for ($i = 0; $i < $n; $i++) {\n  \
        \          $char = $s[$i];\n            if ($char === '(') {\n             \
        \   $low++;\n                $high++;\n            } else if ($char === ')')\
        \ {\n                $low--;\n                $high--;\n            } else {\n\
        \                $low--;\n                $high++;\n            }\n        \
        \    if ($high < 0) {\n                return false;\n            }\n      \
        \      if ($low < 0) {\n                $low = 0;\n            }\n        }\n\
        \        return $low === 0;\n    }\n}"
      swift: "class Solution {\n    func checkValidString(_ s: String) -> Bool {\n \
        \       var low = 0\n        var high = 0\n        for char in s {\n       \
        \     if char == \"(\" {\n                low += 1\n                high +=\
        \ 1\n            } else if char == \")\" {\n                low -= 1\n     \
        \           high -= 1\n            } else {\n                low -= 1\n    \
        \            high += 1\n            }\n            if high < 0 {\n         \
        \       return false\n            }\n            if low < 0 {\n            \
        \    low = 0\n            }\n        }\n        return low == 0\n    }\n}"
      kotlin: "class Solution {\n    fun checkValidString(s: String): Boolean {\n  \
        \      var low = 0\n        var high = 0\n        for (c in s) {\n         \
        \   if (c == '(') {\n                low++\n                high++\n       \
        \     } else if (c == ')') {\n                low--\n                high--\n\
        \            } else {\n                low--\n                high++\n     \
        \       }\n            if (high < 0) return false\n            if (low < 0)\
        \ low = 0\n        }\n        return low == 0\n    }\n}"
      dart: "class Solution {\n  bool checkValidString(String s) {\n    int low = 0;\n\
        \    int high = 0;\n    for (int i = 0; i < s.length; i++) {\n      String c\
        \ = s[i];\n      if (c == '(') {\n        low++;\n        high++;\n      } else\
        \ if (c == ')') {\n        low--;\n        high--;\n      } else {\n       \
        \ low--;\n        high++;\n      }\n      if (high < 0) return false;\n    \
        \  if (low < 0) low = 0;\n    }\n    return low == 0;\n  }\n}"
      go: "func checkValidString(s string) bool {\n    low := 0\n    high := 0\n   \
        \ for _, c := range s {\n        if c == '(' {\n            low++\n        \
        \    high++\n        } else if c == ')' {\n            low--\n            high--\n\
        \        } else {\n            low--\n            high++\n        }\n      \
        \  if high < 0 {\n            return false\n        }\n        if low < 0 {\n\
        \            low = 0\n        }\n    }\n    return low == 0\n}"
      ruby: "# @param {String} s\n# @return {Boolean}\ndef check_valid_string(s)\n \
        \ low = 0\n  high = 0\n  s.each_char do |c|\n    if c == '('\n      low += 1\n\
        \      high += 1\n    elsif c == ')'\n      low -= 1\n      high -= 1\n    else\n\
        \      low -= 1\n      high += 1\n    end\n    return false if high < 0\n  \
        \  low = 0 if low < 0\n  end\n  low == 0\nend"
      scala: "object Solution {\n    def checkValidString(s: String): Boolean = {\n\
        \        var low = 0\n        var high = 0\n        for (c <- s) {\n       \
        \     if (c == '(') {\n                low += 1\n                high += 1\n\
        \            } else if (c == ')') {\n                low -= 1\n            \
        \    high -= 1\n            } else {\n                low -= 1\n           \
        \     high += 1\n            }\n            if (high < 0) return false\n   \
        \         if (low < 0) low = 0\n        }\n        low == 0\n    }\n}"
      rust: "impl Solution {\n    pub fn check_valid_string(s: String) -> bool {\n \
        \       let mut low: i32 = 0;\n        let mut high: i32 = 0;\n        for c\
        \ in s.chars() {\n            match c {\n                '(' => {\n        \
        \            low += 1;\n                    high += 1;\n                }\n\
        \                ')' => {\n                    low -= 1;\n                 \
        \   high -= 1;\n                }\n                '*' => {\n              \
        \      low -= 1;\n                    high += 1;\n                }\n      \
        \          _ => {}\n            }\n            if high < 0 {\n             \
        \   return false;\n            }\n            if low < 0 {\n               \
        \ low = 0;\n            }\n        }\n        low == 0\n    }\n}"
      racket: "(define/contract (check-valid-string s)\n  (-> string? boolean?)\n  (let\
        \ loop ([chars (string->list s)]\n             [low 0]\n             [high 0])\n\
        \    (if (< high 0)\n        #f\n        (if (null? chars)\n            (= low\
        \ 0)\n            (let* ([c (car chars)]\n                   [rest (cdr chars)]\n\
        \                   [nl (cond\n                         [(char=? c #\\() (+\
        \ low 1)]\n                         [(char=? c #\\)) (- low 1)]\n          \
        \               [(char=? c #\\*) (- low 1)])]\n                   [nh (cond\n\
        \                         [(char=? c #\\() (+ high 1)]\n                   \
        \      [(char=? c #\\)) (- high 1)]\n                         [(char=? c #\\\
        *) (+ high 1)])])\n              (loop rest (max 0 nl) nh))))))"
      erlang: "-spec check_valid_string(S :: unicode:unicode_binary()) -> boolean().\n\
        check_valid_string(S) ->\n  check_helper(unicode:characters_to_list(S), 0, 0).\n\
        \ncheck_helper([], Low, High) ->\n  Low =:= 0;\ncheck_helper([C | Rest], Low,\
        \ High) ->\n  {NLow, NHigh} = case C of\n    $( -> {Low + 1, High + 1};\n  \
        \  $) -> {Low - 1, High - 1};\n    $* -> {Low - 1, High + 1}\n  end,\n  if\n\
        \    NHigh < 0 -> false;\n    true -> check_helper(Rest, erlang:max(0, NLow),\
        \ NHigh)\n  end."
      elixir: "defmodule Solution do\n  @spec check_valid_string(s :: String.t) :: boolean\n\
        \  def check_valid_string(s) do\n    result = s\n    |> String.to_charlist()\n\
        \    |> Enum.reduce_while({0, 0}, fn char, {low, high} ->\n      {nl, nh} =\
        \ case char do\n        ?( -> {low + 1, high + 1}\n        ?) -> {low - 1, high\
        \ - 1}\n        ?* -> {low - 1, high + 1}\n      end\n      if nh < 0 do\n \
        \       {:halt, :invalid}\n      else\n        {:cont, {max(0, nl), nh}}\n \
        \     end\n    end)\n\n    case result do\n      {low, _high} -> low == 0\n\
        \      :invalid -> false\n    end\n  end\nend"
    approach: 'The algorithm uses a greedy approach by maintaining a range of possible
      open parenthesis counts. We define low as the minimum number of open parentheses
      that must be matched and high as the maximum number of open parentheses that could
      be matched. This range accounts for the flexibility of the ''*'' character, which
      can represent a left parenthesis, a right parenthesis, or an empty string, effectively
      branching the possibilities at every occurrence of a wildcard.


      For every character in the string, we update the range: ''('' increases both limits,
      '')'' decreases both, and ''*'' expands the range by decreasing low and increasing
      high. If at any point high becomes negative, it indicates an impossible state
      with too many closing parentheses that cannot be balanced even by treating all
      wildcards as opening parentheses, so we return false. We also clamp low at zero
      because we cannot have a negative count of required open parentheses. Finally,
      the string is valid if low equals zero at the end, indicating that all required
      opening parentheses have been successfully matched.'
    time_complexity: O(n), where n is the length of the string, because we perform a
      single linear scan through the input string and execute a constant number of operations
      at each step.
    space_complexity: O(1), as we only maintain two integer counters (low and high)
      regardless of the length of the input string, requiring no additional data structures.
    elapsed_time: 93.46402955055237
    model: gemini-3-flash-preview
    generated_at: '2026-10-04 03:39:28 '
---

## Problem #678: Valid Parenthesis String

**Difficulty:** Medium

**Topics:** String, Dynamic Programming, Stack, Greedy, Bracket Sequences

## Problem Description

<p>Given a string <code>s</code> containing only three types of characters: <code>&#39;(&#39;</code>, <code>&#39;)&#39;</code> and <code>&#39;*&#39;</code>, return <code>true</code> <em>if</em> <code>s</code> <em>is <strong>valid</strong></em>.</p>

<p>The following rules define a <strong>valid</strong> string:</p>

<ul>
	<li>Any left parenthesis <code>&#39;(&#39;</code> must have a corresponding right parenthesis <code>&#39;)&#39;</code>.</li>
	<li>Any right parenthesis <code>&#39;)&#39;</code> must have a corresponding left parenthesis <code>&#39;(&#39;</code>.</li>
	<li>Left parenthesis <code>&#39;(&#39;</code> must go before the corresponding right parenthesis <code>&#39;)&#39;</code>.</li>
	<li><code>&#39;*&#39;</code> could be treated as a single right parenthesis <code>&#39;)&#39;</code> or a single left parenthesis <code>&#39;(&#39;</code> or an empty string <code>&quot;&quot;</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;()&quot;
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(*)&quot;
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(*))&quot;
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 4:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(&quot;
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s[i]</code> is <code>&#39;(&#39;</code>, <code>&#39;)&#39;</code> or <code>&#39;*&#39;</code>.</li>
</ul>


## Hints

1. Use backtracking to explore all possible combinations of treating '*' as either '(', ')', or an empty string. If any combination leads to a valid string, return true.

2. DP[i][j] represents whether the substring s[i:j] is valid.

3. Keep track of the count of open parentheses encountered so far. If you encounter a close parenthesis, it should balance with an open parenthesis. Utilize a stack to handle this effectively.

4. How about using 2 stacks instead of 1? Think about it.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm uses a greedy approach by maintaining a range of possible open parenthesis counts. We define low as the minimum number of open parentheses that must be matched and high as the maximum number of open parentheses that could be matched. This range accounts for the flexibility of the '*' character, which can represent a left parenthesis, a right parenthesis, or an empty string, effectively branching the possibilities at every occurrence of a wildcard.

For every character in the string, we update the range: '(' increases both limits, ')' decreases both, and '*' expands the range by decreasing low and increasing high. If at any point high becomes negative, it indicates an impossible state with too many closing parentheses that cannot be balanced even by treating all wildcards as opening parentheses, so we return false. We also clamp low at zero because we cannot have a negative count of required open parentheses. Finally, the string is valid if low equals zero at the end, indicating that all required opening parentheses have been successfully matched.

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
    bool checkValidString(string s) {
        int low = 0, high = 0;
        for (char c : s) {
            if (c == '(') {
                low++;
                high++;
            } else if (c == ')') {
                low--;
                high--;
            } else {
                low--;
                high++;
            }
            if (high < 0) return false;
            if (low < 0) low = 0;
        }
        return low == 0;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean checkValidString(String s) {
        int low = 0, high = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                low++;
                high++;
            } else if (c == ')') {
                low--;
                high--;
            } else {
                low--;
                high++;
            }
            if (high < 0) return false;
            if (low < 0) low = 0;
        }
        return low == 0;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        low = 0
        high = 0
        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
            else:
                low -= 1
                high += 1
            if high < 0:
                return False
            if low < 0:
                low = 0
        return low == 0
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0
        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
            else:
                low -= 1
                high += 1
            if high < 0:
                return False
            if low < 0:
                low = 0
        return low == 0
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdbool.h>

bool checkValidString(char* s) {
    int low = 0, high = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '(') {
            low++;
            high++;
        } else if (s[i] == ')') {
            low--;
            high--;
        } else {
            low--;
            high++;
        }
        if (high < 0) return false;
        if (low < 0) low = 0;
    }
    return low == 0;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool CheckValidString(string s) {
        int low = 0;
        int high = 0;
        foreach (char c in s) {
            if (c == '(') {
                low++;
                high++;
            } else if (c == ')') {
                low--;
                high--;
            } else {
                low--;
                high++;
            }
            if (high < 0) {
                return false;
            }
            if (low < 0) {
                low = 0;
            }
        }
        return low == 0;
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
 * @return {boolean}
 */
var checkValidString = function(s) {
    let low = 0;
    let high = 0;
    for (let i = 0; i < s.length; i++) {
        let char = s[i];
        if (char === '(') {
            low++;
            high++;
        } else if (char === ')') {
            low--;
            high--;
        } else {
            low--;
            high++;
        }
        if (high < 0) {
            return false;
        }
        if (low < 0) {
            low = 0;
        }
    }
    return low === 0;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function checkValidString(s: string): boolean {
    let low: number = 0;
    let high: number = 0;
    for (let i: number = 0; i < s.length; i++) {
        let char: string = s[i];
        if (char === '(') {
            low++;
            high++;
        } else if (char === ')') {
            low--;
            high--;
        } else {
            low--;
            high++;
        }
        if (high < 0) {
            return false;
        }
        if (low < 0) {
            low = 0;
        }
    }
    return low === 0;
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
     * @return Boolean
     */
    function checkValidString($s) {
        $low = 0;
        $high = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $char = $s[$i];
            if ($char === '(') {
                $low++;
                $high++;
            } else if ($char === ')') {
                $low--;
                $high--;
            } else {
                $low--;
                $high++;
            }
            if ($high < 0) {
                return false;
            }
            if ($low < 0) {
                $low = 0;
            }
        }
        return $low === 0;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func checkValidString(_ s: String) -> Bool {
        var low = 0
        var high = 0
        for char in s {
            if char == "(" {
                low += 1
                high += 1
            } else if char == ")" {
                low -= 1
                high -= 1
            } else {
                low -= 1
                high += 1
            }
            if high < 0 {
                return false
            }
            if low < 0 {
                low = 0
            }
        }
        return low == 0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun checkValidString(s: String): Boolean {
        var low = 0
        var high = 0
        for (c in s) {
            if (c == '(') {
                low++
                high++
            } else if (c == ')') {
                low--
                high--
            } else {
                low--
                high++
            }
            if (high < 0) return false
            if (low < 0) low = 0
        }
        return low == 0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool checkValidString(String s) {
    int low = 0;
    int high = 0;
    for (int i = 0; i < s.length; i++) {
      String c = s[i];
      if (c == '(') {
        low++;
        high++;
      } else if (c == ')') {
        low--;
        high--;
      } else {
        low--;
        high++;
      }
      if (high < 0) return false;
      if (low < 0) low = 0;
    }
    return low == 0;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func checkValidString(s string) bool {
    low := 0
    high := 0
    for _, c := range s {
        if c == '(' {
            low++
            high++
        } else if c == ')' {
            low--
            high--
        } else {
            low--
            high++
        }
        if high < 0 {
            return false
        }
        if low < 0 {
            low = 0
        }
    }
    return low == 0
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @return {Boolean}
def check_valid_string(s)
  low = 0
  high = 0
  s.each_char do |c|
    if c == '('
      low += 1
      high += 1
    elsif c == ')'
      low -= 1
      high -= 1
    else
      low -= 1
      high += 1
    end
    return false if high < 0
    low = 0 if low < 0
  end
  low == 0
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def checkValidString(s: String): Boolean = {
        var low = 0
        var high = 0
        for (c <- s) {
            if (c == '(') {
                low += 1
                high += 1
            } else if (c == ')') {
                low -= 1
                high -= 1
            } else {
                low -= 1
                high += 1
            }
            if (high < 0) return false
            if (low < 0) low = 0
        }
        low == 0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn check_valid_string(s: String) -> bool {
        let mut low: i32 = 0;
        let mut high: i32 = 0;
        for c in s.chars() {
            match c {
                '(' => {
                    low += 1;
                    high += 1;
                }
                ')' => {
                    low -= 1;
                    high -= 1;
                }
                '*' => {
                    low -= 1;
                    high += 1;
                }
                _ => {}
            }
            if high < 0 {
                return false;
            }
            if low < 0 {
                low = 0;
            }
        }
        low == 0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (check-valid-string s)
  (-> string? boolean?)
  (let loop ([chars (string->list s)]
             [low 0]
             [high 0])
    (if (< high 0)
        #f
        (if (null? chars)
            (= low 0)
            (let* ([c (car chars)]
                   [rest (cdr chars)]
                   [nl (cond
                         [(char=? c #\() (+ low 1)]
                         [(char=? c #\)) (- low 1)]
                         [(char=? c #\*) (- low 1)])]
                   [nh (cond
                         [(char=? c #\() (+ high 1)]
                         [(char=? c #\)) (- high 1)]
                         [(char=? c #\*) (+ high 1)])])
              (loop rest (max 0 nl) nh))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec check_valid_string(S :: unicode:unicode_binary()) -> boolean().
check_valid_string(S) ->
  check_helper(unicode:characters_to_list(S), 0, 0).

check_helper([], Low, High) ->
  Low =:= 0;
check_helper([C | Rest], Low, High) ->
  {NLow, NHigh} = case C of
    $( -> {Low + 1, High + 1};
    $) -> {Low - 1, High - 1};
    $* -> {Low - 1, High + 1}
  end,
  if
    NHigh < 0 -> false;
    true -> check_helper(Rest, erlang:max(0, NLow), NHigh)
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec check_valid_string(s :: String.t) :: boolean
  def check_valid_string(s) do
    result = s
    |> String.to_charlist()
    |> Enum.reduce_while({0, 0}, fn char, {low, high} ->
      {nl, nh} = case char do
        ?( -> {low + 1, high + 1}
        ?) -> {low - 1, high - 1}
        ?* -> {low - 1, high + 1}
      end
      if nh < 0 do
        {:halt, :invalid}
      else
        {:cont, {max(0, nl), nh}}
      end
    end)

    case result do
      {low, _high} -> low == 0
      :invalid -> false
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n), where n is the length of the string, because we perform a single linear scan through the input string and execute a constant number of operations at each step.
- **Space Complexity:** O(1), as we only maintain two integer counters (low and high) regardless of the length of the input string, requiring no additional data structures.
