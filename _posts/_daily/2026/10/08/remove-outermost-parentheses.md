---
layout: post
title: "Remove Outermost Parentheses"
date: 2026-10-08 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["String", "Stack", "Bracket Sequences"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/remove-outermost-parentheses/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    string removeOuterParentheses(string s) {\n\
        \        string res = \"\";\n        int opened = 0;\n        for (char c :\
        \ s) {\n            if (c == '(') {\n                if (opened > 0) res +=\
        \ c;\n                opened++;\n            }\n            else {\n       \
        \         opened--;\n                if (opened > 0) res += c;\n           \
        \ }\n        }\n        return res;\n    }\n};"
      java: "class Solution {\n    public String removeOuterParentheses(String s) {\n\
        \        StringBuilder sb = new StringBuilder();\n        int opened = 0;\n\
        \        for (char c : s.toCharArray()) {\n            if (c == '(') {\n   \
        \             if (opened > 0) {\n                    sb.append(c);\n       \
        \         }\n                opened++;\n            } else {\n             \
        \   opened--;\n                if (opened > 0) {\n                    sb.append(c);\n\
        \                }\n            }\n        }\n        return sb.toString();\n\
        \    }\n}"
      python: "class Solution(object):\n    def removeOuterParentheses(self, s):\n \
        \       \"\"\"\n        :type s: str\n        :rtype: str\n        \"\"\"\n\
        \        res = []\n        opened = 0\n        for char in s:\n            if\
        \ char == '(':\n                if opened > 0:\n                    res.append(char)\n\
        \                opened += 1\n            else:\n                opened -= 1\n\
        \                if opened > 0:\n                    res.append(char)\n    \
        \    return \"\".join(res)"
      python3: "class Solution:\n    def removeOuterParentheses(self, s: str) -> str:\n\
        \        res = []\n        opened = 0\n        for char in s:\n            if\
        \ char == '(':\n                if opened > 0:\n                    res.append(char)\n\
        \                opened += 1\n            else:\n                opened -= 1\n\
        \                if opened > 0:\n                    res.append(char)\n    \
        \    return \"\".join(res)"
      c: "char* removeOuterParentheses(char* s) {\n    int n = strlen(s);\n    char*\
        \ res = (char*)malloc(sizeof(char) * (n + 1));\n    int opened = 0;\n    int\
        \ j = 0;\n    for (int i = 0; i < n; i++) {\n        if (s[i] == '(') {\n  \
        \          if (opened > 0) {\n                res[j++] = '(';\n            }\n\
        \            opened++;\n        } else {\n            opened--;\n          \
        \  if (opened > 0) {\n                res[j++] = ')';\n            }\n     \
        \   }\n    }\n    res[j] = '\\0';\n    return res;\n}"
      csharp: "using System.Text;\n\npublic class Solution {\n    public string RemoveOuterParentheses(string\
        \ s) {\n        StringBuilder sb = new StringBuilder();\n        int opened\
        \ = 0;\n        foreach (char c in s) {\n            if (c == '(') {\n     \
        \           if (opened > 0) {\n                    sb.Append(c);\n         \
        \       }\n                opened++;\n            } else {\n               \
        \ opened--;\n                if (opened > 0) {\n                    sb.Append(c);\n\
        \                }\n            }\n        }\n        return sb.ToString();\n\
        \    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {string}\n */\nvar removeOuterParentheses\
        \ = function(s) {\n    let res = [];\n    let opened = 0;\n    for (let i =\
        \ 0; i < s.length; i++) {\n        let c = s[i];\n        if (c === '(') {\n\
        \            if (opened > 0) {\n                res.push(c);\n            }\n\
        \            opened++;\n        } else {\n            opened--;\n          \
        \  if (opened > 0) {\n                res.push(c);\n            }\n        }\n\
        \    }\n    return res.join('');\n};"
      typescript: "function removeOuterParentheses(s: string): string {\n    let res\
        \ = '';\n    let opened = 0;\n    for (let i = 0; i < s.length; i++) {\n   \
        \     if (s[i] === '(') {\n            if (opened > 0) {\n                res\
        \ += '(';\n            }\n            opened++;\n        } else {\n        \
        \    opened--;\n            if (opened > 0) {\n                res += ')';\n\
        \            }\n        }\n    }\n    return res;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return String\n\
        \     */\n    function removeOuterParentheses($s) {\n        $res = '';\n  \
        \      $opened = 0;\n        $len = strlen($s);\n        for ($i = 0; $i < $len;\
        \ $i++) {\n            if ($s[$i] === '(') {\n                if ($opened >\
        \ 0) {\n                    $res .= '(';\n                }\n              \
        \  $opened++;\n            } else {\n                $opened--;\n          \
        \      if ($opened > 0) {\n                    $res .= ')';\n              \
        \  }\n            }\n        }\n        return $res;\n    }\n}"
      swift: "class Solution {\n    func removeOuterParentheses(_ s: String) -> String\
        \ {\n        var res = \"\"\n        var opened = 0\n        for char in s {\n\
        \            if char == \"(\" {\n                if opened > 0 {\n         \
        \           res.append(char)\n                }\n                opened += 1\n\
        \            } else {\n                opened -= 1\n                if opened\
        \ > 0 {\n                    res.append(char)\n                }\n         \
        \   }\n        }\n        return res\n    }\n}"
      kotlin: "class Solution {\n    fun removeOuterParentheses(s: String): String {\n\
        \        val res = StringBuilder()\n        var opened = 0\n        for (char\
        \ in s) {\n            if (char == '(') {\n                if (opened > 0) {\n\
        \                    res.append('(')\n                }\n                opened++\n\
        \            } else {\n                opened--\n                if (opened\
        \ > 0) {\n                    res.append(')')\n                }\n         \
        \   }\n        }\n        return res.toString()\n    }\n}"
      dart: "class Solution {\n  String removeOuterParentheses(String s) {\n    StringBuffer\
        \ res = StringBuffer();\n    int opened = 0;\n    for (int i = 0; i < s.length;\
        \ i++) {\n      if (s[i] == '(') {\n        if (opened > 0) {\n          res.write('(');\n\
        \        }\n        opened++;\n      } else {\n        opened--;\n        if\
        \ (opened > 0) {\n          res.write(')');\n        }\n      }\n    }\n   \
        \ return res.toString();\n  }\n}"
      go: "func removeOuterParentheses(s string) string {\n    res := make([]byte, 0,\
        \ len(s))\n    opened := 0\n    for i := 0; i < len(s); i++ {\n        if s[i]\
        \ == '(' {\n            if opened > 0 {\n                res = append(res, '(')\n\
        \            }\n            opened++\n        } else {\n            opened--\n\
        \            if opened > 0 {\n                res = append(res, ')')\n     \
        \       }\n        }\n    }\n    return string(res)\n}"
      ruby: "# @param {String} s\n# @return {String}\ndef remove_outer_parentheses(s)\n\
        \  res = \"\"\n  opened = 0\n  s.each_char do |c|\n    if c == '('\n      res\
        \ << c if opened > 0\n      opened += 1\n    else\n      opened -= 1\n     \
        \ res << c if opened > 0\n    end\n  end\n  res\nend"
      scala: "object Solution {\n    def removeOuterParentheses(s: String): String =\
        \ {\n        val sb = new StringBuilder()\n        var opened = 0\n        for\
        \ (c <- s) {\n            if (c == '(') {\n                if (opened > 0) {\n\
        \                    sb.append(c)\n                }\n                opened\
        \ += 1\n            } else {\n                opened -= 1\n                if\
        \ (opened > 0) {\n                    sb.append(c)\n                }\n    \
        \        }\n        }\n        sb.toString()\n    }\n}"
      rust: "impl Solution {\n    pub fn remove_outer_parentheses(s: String) -> String\
        \ {\n        let mut res = String::new();\n        let mut opened = 0;\n   \
        \     for c in s.chars() {\n            if c == '(' {\n                if opened\
        \ > 0 {\n                    res.push(c);\n                }\n             \
        \   opened += 1;\n            } else {\n                opened -= 1;\n     \
        \           if opened > 0 {\n                    res.push(c);\n            \
        \    }\n            }\n        }\n        res\n    }\n}"
      racket: "(define/contract (remove-outer-parentheses s)\n  (-> string? string?)\n\
        \  (let ([chars (string->list s)])\n    (let loop ([cs chars] [opened 0] [res\
        \ '()])\n      (if (null? cs)\n          (list->string (reverse res))\n    \
        \      (let ([c (car cs)])\n            (cond\n              [(char=? c #\\\
        ()\n               (if (> opened 0)\n                   (loop (cdr cs) (+ opened\
        \ 1) (cons c res))\n                   (loop (cdr cs) (+ opened 1) res))]\n\
        \              [(char=? c #\\))\n               (let ([new-opened (- opened\
        \ 1)])\n                 (if (> new-opened 0)\n                     (loop (cdr\
        \ cs) new-opened (cons c res))\n                     (loop (cdr cs) new-opened\
        \ res)))]))))))"
      erlang: "-spec remove_outer_parentheses(S :: unicode:unicode_binary()) -> unicode:unicode_binary().\n\
        remove_outer_parentheses(S) ->\n    L = binary_to_list(S),\n    Result = process(L,\
        \ 0, []),\n    list_to_binary(lists:reverse(Result)).\n\nprocess([], _Opened,\
        \ Acc) -> Acc;\nprocess([$( | T], Opened, Acc) ->\n    NewAcc = case Opened\
        \ > 0 of\n        true -> [$( | Acc];\n        false -> Acc\n    end,\n    process(T,\
        \ Opened + 1, NewAcc);\nprocess([$) | T], Opened, Acc) ->\n    NewOpened = Opened\
        \ - 1,\n    NewAcc = case NewOpened > 0 of\n        true -> [$) | Acc];\n  \
        \      false -> Acc\n    end,\n    process(T, NewOpened, NewAcc)."
      elixir: "defmodule Solution do\n  @spec remove_outer_parentheses(s :: String.t)\
        \ :: String.t\n  def remove_outer_parentheses(s) do\n    s\n    |> String.graphemes()\n\
        \    |> Enum.reduce({0, []}, fn char, {opened, acc} ->\n      case char do\n\
        \        \"(\" ->\n          new_acc = if opened > 0, do: [\"(\" | acc], else:\
        \ acc\n          {opened + 1, new_acc}\n        \")\" ->\n          new_opened\
        \ = opened - 1\n          new_acc = if new_opened > 0, do: [\")\" | acc], else:\
        \ acc\n          {new_opened, new_acc}\n      end\n    end)\n    |> elem(1)\n\
        \    |> Enum.reverse()\n    |> Enum.join(\"\")\n  end\nend"
    approach: 'The problem asks us to identify ''primitive'' components of a valid parentheses
      string and strip their outermost brackets. A valid parentheses string is primitive
      if it cannot be further split into smaller valid strings. We can identify these
      primitive components by maintaining a balance counter (nesting level). As we iterate
      through the input string, an opening parenthesis increases the nesting level,
      and a closing parenthesis decreases it. A primitive string begins when the balance
      starts at zero and ends when the balance returns to zero.


      To strip the outermost parentheses, we only include a character in our result
      if it lies ''inside'' a primitive component. For an opening bracket, this means
      the current nesting level must be at least 1 before we count the new bracket (or
      equivalently, the balance is greater than zero). For a closing bracket, this means
      the balance must still be at least 1 after decrementing the counter. By applying
      this logic during a single pass, we filter out the parentheses at the outermost
      level (depth 0) and concatenate the inner contents of all primitive parts.'
    time_complexity: O(N) where N is the length of the input string. We iterate through
      the string exactly once, performing constant-time increment/decrement operations
      and character appends at each step.
    space_complexity: O(N) to store the result. In the worst case, where the entire
      input is a single primitive string minus two characters, the resulting string
      will have a length proportional to the input size.
    elapsed_time: 325.3744752407074
    model: gemini-3-flash-preview
    generated_at: '2026-10-08 03:55:08 '
---

## Problem #1021: Remove Outermost Parentheses

**Difficulty:** Easy

**Topics:** String, Stack, Bracket Sequences

## Problem Description

<p>A valid parentheses string is either empty <code>&quot;&quot;</code>, <code>&quot;(&quot; + A + &quot;)&quot;</code>, or <code>A + B</code>, where <code>A</code> and <code>B</code> are valid parentheses strings, and <code>+</code> represents string concatenation.</p>

<ul>
	<li>For example, <code>&quot;&quot;</code>, <code>&quot;()&quot;</code>, <code>&quot;(())()&quot;</code>, and <code>&quot;(()(()))&quot;</code> are all valid parentheses strings.</li>
</ul>

<p>A valid parentheses string <code>s</code> is primitive if it is nonempty, and there does not exist a way to split it into <code>s = A + B</code>, with <code>A</code> and <code>B</code> nonempty valid parentheses strings.</p>

<p>Given a valid parentheses string <code>s</code>, consider its primitive decomposition: <code>s = P<sub>1</sub> + P<sub>2</sub> + ... + P<sub>k</sub></code>, where <code>P<sub>i</sub></code> are primitive valid parentheses strings.</p>

<p>Return <code>s</code> <em>after removing the outermost parentheses of every primitive string in the primitive decomposition of </em><code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(()())(())&quot;
<strong>Output:</strong> &quot;()()()&quot;
<strong>Explanation:</strong> 
The input string is &quot;(()())(())&quot;, with primitive decomposition &quot;(()())&quot; + &quot;(())&quot;.
After removing outer parentheses of each part, this is &quot;()()&quot; + &quot;()&quot; = &quot;()()()&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(()())(())(()(()))&quot;
<strong>Output:</strong> &quot;()()()()(())&quot;
<strong>Explanation:</strong> 
The input string is &quot;(()())(())(()(()))&quot;, with primitive decomposition &quot;(()())&quot; + &quot;(())&quot; + &quot;(()(()))&quot;.
After removing outer parentheses of each part, this is &quot;()()&quot; + &quot;()&quot; + &quot;()(())&quot; = &quot;()()()()(())&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;()()&quot;
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> 
The input string is &quot;()()&quot;, with primitive decomposition &quot;()&quot; + &quot;()&quot;.
After removing outer parentheses of each part, this is &quot;&quot; + &quot;&quot; = &quot;&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either <code>&#39;(&#39;</code> or <code>&#39;)&#39;</code>.</li>
	<li><code>s</code> is a valid parentheses string.</li>
</ul>


## Hints

1. Can you find the primitive decomposition?  The number of ( and ) characters must be equal.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks us to identify 'primitive' components of a valid parentheses string and strip their outermost brackets. A valid parentheses string is primitive if it cannot be further split into smaller valid strings. We can identify these primitive components by maintaining a balance counter (nesting level). As we iterate through the input string, an opening parenthesis increases the nesting level, and a closing parenthesis decreases it. A primitive string begins when the balance starts at zero and ends when the balance returns to zero.

To strip the outermost parentheses, we only include a character in our result if it lies 'inside' a primitive component. For an opening bracket, this means the current nesting level must be at least 1 before we count the new bracket (or equivalently, the balance is greater than zero). For a closing bracket, this means the balance must still be at least 1 after decrementing the counter. By applying this logic during a single pass, we filter out the parentheses at the outermost level (depth 0) and concatenate the inner contents of all primitive parts.

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
    string removeOuterParentheses(string s) {
        string res = "";
        int opened = 0;
        for (char c : s) {
            if (c == '(') {
                if (opened > 0) res += c;
                opened++;
            }
            else {
                opened--;
                if (opened > 0) res += c;
            }
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
    public String removeOuterParentheses(String s) {
        StringBuilder sb = new StringBuilder();
        int opened = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') {
                if (opened > 0) {
                    sb.append(c);
                }
                opened++;
            } else {
                opened--;
                if (opened > 0) {
                    sb.append(c);
                }
            }
        }
        return sb.toString();
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        opened = 0
        for char in s:
            if char == '(':
                if opened > 0:
                    res.append(char)
                opened += 1
            else:
                opened -= 1
                if opened > 0:
                    res.append(char)
        return "".join(res)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        opened = 0
        for char in s:
            if char == '(':
                if opened > 0:
                    res.append(char)
                opened += 1
            else:
                opened -= 1
                if opened > 0:
                    res.append(char)
        return "".join(res)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
char* removeOuterParentheses(char* s) {
    int n = strlen(s);
    char* res = (char*)malloc(sizeof(char) * (n + 1));
    int opened = 0;
    int j = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == '(') {
            if (opened > 0) {
                res[j++] = '(';
            }
            opened++;
        } else {
            opened--;
            if (opened > 0) {
                res[j++] = ')';
            }
        }
    }
    res[j] = '\0';
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System.Text;

public class Solution {
    public string RemoveOuterParentheses(string s) {
        StringBuilder sb = new StringBuilder();
        int opened = 0;
        foreach (char c in s) {
            if (c == '(') {
                if (opened > 0) {
                    sb.Append(c);
                }
                opened++;
            } else {
                opened--;
                if (opened > 0) {
                    sb.Append(c);
                }
            }
        }
        return sb.ToString();
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
 * @return {string}
 */
var removeOuterParentheses = function(s) {
    let res = [];
    let opened = 0;
    for (let i = 0; i < s.length; i++) {
        let c = s[i];
        if (c === '(') {
            if (opened > 0) {
                res.push(c);
            }
            opened++;
        } else {
            opened--;
            if (opened > 0) {
                res.push(c);
            }
        }
    }
    return res.join('');
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function removeOuterParentheses(s: string): string {
    let res = '';
    let opened = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '(') {
            if (opened > 0) {
                res += '(';
            }
            opened++;
        } else {
            opened--;
            if (opened > 0) {
                res += ')';
            }
        }
    }
    return res;
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
     * @return String
     */
    function removeOuterParentheses($s) {
        $res = '';
        $opened = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            if ($s[$i] === '(') {
                if ($opened > 0) {
                    $res .= '(';
                }
                $opened++;
            } else {
                $opened--;
                if ($opened > 0) {
                    $res .= ')';
                }
            }
        }
        return $res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func removeOuterParentheses(_ s: String) -> String {
        var res = ""
        var opened = 0
        for char in s {
            if char == "(" {
                if opened > 0 {
                    res.append(char)
                }
                opened += 1
            } else {
                opened -= 1
                if opened > 0 {
                    res.append(char)
                }
            }
        }
        return res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun removeOuterParentheses(s: String): String {
        val res = StringBuilder()
        var opened = 0
        for (char in s) {
            if (char == '(') {
                if (opened > 0) {
                    res.append('(')
                }
                opened++
            } else {
                opened--
                if (opened > 0) {
                    res.append(')')
                }
            }
        }
        return res.toString()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  String removeOuterParentheses(String s) {
    StringBuffer res = StringBuffer();
    int opened = 0;
    for (int i = 0; i < s.length; i++) {
      if (s[i] == '(') {
        if (opened > 0) {
          res.write('(');
        }
        opened++;
      } else {
        opened--;
        if (opened > 0) {
          res.write(')');
        }
      }
    }
    return res.toString();
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func removeOuterParentheses(s string) string {
    res := make([]byte, 0, len(s))
    opened := 0
    for i := 0; i < len(s); i++ {
        if s[i] == '(' {
            if opened > 0 {
                res = append(res, '(')
            }
            opened++
        } else {
            opened--
            if opened > 0 {
                res = append(res, ')')
            }
        }
    }
    return string(res)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @return {String}
def remove_outer_parentheses(s)
  res = ""
  opened = 0
  s.each_char do |c|
    if c == '('
      res << c if opened > 0
      opened += 1
    else
      opened -= 1
      res << c if opened > 0
    end
  end
  res
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def removeOuterParentheses(s: String): String = {
        val sb = new StringBuilder()
        var opened = 0
        for (c <- s) {
            if (c == '(') {
                if (opened > 0) {
                    sb.append(c)
                }
                opened += 1
            } else {
                opened -= 1
                if (opened > 0) {
                    sb.append(c)
                }
            }
        }
        sb.toString()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn remove_outer_parentheses(s: String) -> String {
        let mut res = String::new();
        let mut opened = 0;
        for c in s.chars() {
            if c == '(' {
                if opened > 0 {
                    res.push(c);
                }
                opened += 1;
            } else {
                opened -= 1;
                if opened > 0 {
                    res.push(c);
                }
            }
        }
        res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (remove-outer-parentheses s)
  (-> string? string?)
  (let ([chars (string->list s)])
    (let loop ([cs chars] [opened 0] [res '()])
      (if (null? cs)
          (list->string (reverse res))
          (let ([c (car cs)])
            (cond
              [(char=? c #\()
               (if (> opened 0)
                   (loop (cdr cs) (+ opened 1) (cons c res))
                   (loop (cdr cs) (+ opened 1) res))]
              [(char=? c #\))
               (let ([new-opened (- opened 1)])
                 (if (> new-opened 0)
                     (loop (cdr cs) new-opened (cons c res))
                     (loop (cdr cs) new-opened res)))]))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec remove_outer_parentheses(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
remove_outer_parentheses(S) ->
    L = binary_to_list(S),
    Result = process(L, 0, []),
    list_to_binary(lists:reverse(Result)).

process([], _Opened, Acc) -> Acc;
process([$( | T], Opened, Acc) ->
    NewAcc = case Opened > 0 of
        true -> [$( | Acc];
        false -> Acc
    end,
    process(T, Opened + 1, NewAcc);
process([$) | T], Opened, Acc) ->
    NewOpened = Opened - 1,
    NewAcc = case NewOpened > 0 of
        true -> [$) | Acc];
        false -> Acc
    end,
    process(T, NewOpened, NewAcc).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec remove_outer_parentheses(s :: String.t) :: String.t
  def remove_outer_parentheses(s) do
    s
    |> String.graphemes()
    |> Enum.reduce({0, []}, fn char, {opened, acc} ->
      case char do
        "(" ->
          new_acc = if opened > 0, do: ["(" | acc], else: acc
          {opened + 1, new_acc}
        ")" ->
          new_opened = opened - 1
          new_acc = if new_opened > 0, do: [")" | acc], else: acc
          {new_opened, new_acc}
      end
    end)
    |> elem(1)
    |> Enum.reverse()
    |> Enum.join("")
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) where N is the length of the input string. We iterate through the string exactly once, performing constant-time increment/decrement operations and character appends at each step.
- **Space Complexity:** O(N) to store the result. In the worst case, where the entire input is a single primitive string minus two characters, the resulting string will have a length proportional to the input size.
