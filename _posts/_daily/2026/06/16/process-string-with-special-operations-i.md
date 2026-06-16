---
layout: post
title: "Process String with Special Operations I"
date: 2026-06-16 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Simulation"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/process-string-with-special-operations-i/
ai_solutions:
  - solutions:
      cpp: "#include <string>\n#include <algorithm>\n\nusing namespace std;\n\nclass\
        \ Solution {\npublic:\n    string processStr(string s) {\n        string result\
        \ = \"\";\n        for (char c : s) {\n            if (c >= 'a' && c <= 'z')\
        \ {\n                result += c;\n            } else if (c == '*') {\n    \
        \            if (!result.empty()) {\n                    result.pop_back();\n\
        \                }\n            } else if (c == '#') {\n                result\
        \ += result;\n            } else if (c == '%') {\n                reverse(result.begin(),\
        \ result.end());\n            }\n        }\n        return result;\n    }\n\
        };"
      java: "class Solution {\n    public String processStr(String s) {\n        StringBuilder\
        \ result = new StringBuilder();\n        for (int i = 0; i < s.length(); i++)\
        \ {\n            char c = s.charAt(i);\n            if (c >= 'a' && c <= 'z')\
        \ {\n                result.append(c);\n            } else if (c == '*') {\n\
        \                if (result.length() > 0) {\n                    result.setLength(result.length()\
        \ - 1);\n                }\n            } else if (c == '#') {\n           \
        \     result.append(result.toString());\n            } else if (c == '%') {\n\
        \                result.reverse();\n            }\n        }\n        return\
        \ result.toString();\n    }\n}"
      python: "class Solution(object):\n    def processStr(self, s):\n        \"\"\"\
        \n        :type s: str\n        :rtype: str\n        \"\"\"\n        result\
        \ = \"\"\n        for char in s:\n            if 'a' <= char <= 'z':\n     \
        \           result += char\n            elif char == '*':\n                if\
        \ result:\n                    result = result[:-1]\n            elif char ==\
        \ '#':\n                result += result\n            elif char == '%':\n  \
        \              result = result[::-1]\n        return result"
      python3: "class Solution:\n    def processStr(self, s: str) -> str:\n        result\
        \ = \"\"\n        for char in s:\n            if 'a' <= char <= 'z':\n     \
        \           result += char\n            elif char == '*':\n                if\
        \ result:\n                    result = result[:-1]\n            elif char ==\
        \ '#':\n                result += result\n            elif char == '%':\n  \
        \              result = result[::-1]\n        return result"
      c: "#include <stdlib.h>\n#include <string.h>\n\nchar* processStr(char* s) {\n\
        \    int max_len = 1048576;\n    char* res = (char*)malloc(max_len * sizeof(char));\n\
        \    int len = 0;\n    for (int i = 0; s[i] != '\\0'; i++) {\n        if (s[i]\
        \ >= 'a' && s[i] <= 'z') {\n            res[len++] = s[i];\n        } else if\
        \ (s[i] == '*') {\n            if (len > 0) {\n                len--;\n    \
        \        }\n        } else if (s[i] == '#') {\n            if (len > 0 && len\
        \ * 2 < max_len) {\n                memcpy(res + len, res, len);\n         \
        \       len *= 2;\n            }\n        } else if (s[i] == '%') {\n      \
        \      for (int j = 0; j < len / 2; j++) {\n                char temp = res[j];\n\
        \                res[j] = res[len - 1 - j];\n                res[len - 1 - j]\
        \ = temp;\n            }\n        }\n    }\n    res[len] = '\\0';\n    return\
        \ res;\n}"
      csharp: "using System;\n\npublic class Solution {\n    public string ProcessStr(string\
        \ s) {\n        string result = \"\";\n        foreach (char c in s) {\n   \
        \         if (c == '*') {\n                if (result.Length > 0) {\n      \
        \              result = result.Substring(0, result.Length - 1);\n          \
        \      }\n            } else if (c == '#') {\n                result += result;\n\
        \            } else if (c == '%') {\n                char[] charArray = result.ToCharArray();\n\
        \                Array.Reverse(charArray);\n                result = new string(charArray);\n\
        \            } else {\n                result += c;\n            }\n       \
        \ }\n        return result;\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {string}\n */\nvar processStr\
        \ = function(s) {\n    let result = \"\";\n    for (let char of s) {\n     \
        \   if (char === '*') {\n            if (result.length > 0) {\n            \
        \    result = result.slice(0, -1);\n            }\n        } else if (char ===\
        \ '#') {\n            result += result;\n        } else if (char === '%') {\n\
        \            result = result.split('').reverse().join('');\n        } else {\n\
        \            result += char;\n        }\n    }\n    return result;\n};"
      typescript: "function processStr(s: string): string {\n    let result: string\
        \ = \"\";\n    for (let char of s) {\n        if (char === '*') {\n        \
        \    if (result.length > 0) {\n                result = result.slice(0, -1);\n\
        \            }\n        } else if (char === '#') {\n            result += result;\n\
        \        } else if (char === '%') {\n            result = result.split('').reverse().join('');\n\
        \        } else {\n            result += char;\n        }\n    }\n    return\
        \ result;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return String\n\
        \     */\n    function processStr($s) {\n        $result = \"\";\n        $len\
        \ = strlen($s);\n        for ($i = 0; $i < $len; $i++) {\n            $char\
        \ = $s[$i];\n            if ($char === '*') {\n                if (strlen($result)\
        \ > 0) {\n                    $result = substr($result, 0, -1);\n          \
        \      }\n            } else if ($char === '#') {\n                $result .=\
        \ $result;\n            } else if ($char === '%') {\n                $result\
        \ = strrev($result);\n            } else {\n                $result .= $char;\n\
        \            }\n        }\n        return $result;\n    }\n}"
      swift: "class Solution {\n    func processStr(_ s: String) -> String {\n     \
        \   var result = \"\"\n        for char in s {\n            switch char {\n\
        \            case \"*\":\n                if !result.isEmpty {\n           \
        \         result.removeLast()\n                }\n            case \"#\":\n\
        \                result += result\n            case \"%\":\n               \
        \ result = String(result.reversed())\n            default:\n               \
        \ result.append(char)\n            }\n        }\n        return result\n   \
        \ }\n}"
      kotlin: "class Solution {\n    fun processStr(s: String): String {\n        val\
        \ result = StringBuilder()\n        for (char in s) {\n            when (char)\
        \ {\n                '*' -> {\n                    if (result.isNotEmpty())\
        \ {\n                        result.deleteCharAt(result.length - 1)\n      \
        \              }\n                }\n                '#' -> {\n            \
        \        result.append(result.toString())\n                }\n             \
        \   '%' -> {\n                    result.reverse()\n                }\n    \
        \            else -> {\n                    result.append(char)\n          \
        \      }\n            }\n        }\n        return result.toString()\n    }\n\
        }"
      dart: "class Solution {\n  String processStr(String s) {\n    String result =\
        \ \"\";\n    for (int i = 0; i < s.length; i++) {\n      String char = s[i];\n\
        \      if (char == '*') {\n        if (result.isNotEmpty) {\n          result\
        \ = result.substring(0, result.length - 1);\n        }\n      } else if (char\
        \ == '#') {\n        result = result + result;\n      } else if (char == '%')\
        \ {\n        result = result.split('').reversed.join('');\n      } else {\n\
        \        result += char;\n      }\n    }\n    return result;\n  }\n}"
      go: "func processStr(s string) string {\n\tres := []rune{}\n\tfor _, char := range\
        \ s {\n\t\tswitch char {\n\t\tcase '*':\n\t\t\tif len(res) > 0 {\n\t\t\t\tres\
        \ = res[:len(res)-1]\n\t\t\t}\n\t\tcase '#':\n\t\t\tres = append(res, res...)\n\
        \t\tcase '%':\n\t\t\tfor i, j := 0, len(res)-1; i < j; i, j = i+1, j-1 {\n\t\
        \t\t\tres[i], res[j] = res[j], res[i]\n\t\t\t}\n\t\tdefault:\n\t\t\tres = append(res,\
        \ char)\n\t\t}\n\t}\n\treturn string(res)\n}"
      ruby: "def process_str(s)\n  result = \"\"\n  s.each_char do |char|\n    case\
        \ char\n    when '*'\n      result.chop! if result.length > 0\n    when '#'\n\
        \      result += result\n    when '%'\n      result.reverse!\n    else\n   \
        \   result << char\n    end\n  end\n  result\nend"
      scala: "object Solution {\n    def processStr(s: String): String = {\n       \
        \ var result = \"\"\n        for (char <- s) {\n            char match {\n \
        \               case '*' =>\n                    if (result.nonEmpty) {\n  \
        \                      result = result.substring(0, result.length - 1)\n   \
        \                 }\n                case '#' =>\n                    result\
        \ = result + result\n                case '%' =>\n                    result\
        \ = result.reverse\n                case _ =>\n                    result =\
        \ result + char\n            }\n        }\n        result\n    }\n}"
      rust: "impl Solution {\n    pub fn process_str(s: String) -> String {\n      \
        \  let mut result = String::new();\n        for c in s.chars() {\n         \
        \   match c {\n                '*' => {\n                    result.pop();\n\
        \                }\n                '#' => {\n                    let current\
        \ = result.clone();\n                    result.push_str(&current);\n      \
        \          }\n                '%' => {\n                    result = result.chars().rev().collect();\n\
        \                }\n                _ => {\n                    result.push(c);\n\
        \                }\n            }\n        }\n        result\n    }\n}"
      racket: "(define/contract (process-str s)\n  (-> string? string?)\n  (let loop\
        \ ([chars (string->list s)]\n             [res \"\"])\n    (if (null? chars)\n\
        \        res\n        (let ([c (car chars)]\n              [rest (cdr chars)])\n\
        \          (cond\n            [(char=? c #\\*)\n             (loop rest (if\
        \ (string=? res \"\") \"\" (substring res 0 (- (string-length res) 1))))]\n\
        \            [(char=? c #\\#)\n             (loop rest (string-append res res))]\n\
        \            [(char=? c #\\%)\n             (loop rest (list->string (reverse\
        \ (string->list res))))]\n            [else\n             (loop rest (string-append\
        \ res (string c)))])))))"
      erlang: "-spec process_str(S :: unicode:unicode_binary()) -> unicode:unicode_binary().\n\
        process_str(S) ->\n  StrList = binary_to_list(S),\n  Result = process_str_helper(StrList,\
        \ []),\n  list_to_binary(Result).\n\nprocess_str_helper([], Acc) -> Acc;\nprocess_str_helper([Char\
        \ | Rest], Acc) ->\n  case Char of\n    $* ->\n      NewAcc = case Acc of\n\
        \        [] -> [];\n        _ -> lists:sublist(Acc, 1, length(Acc) - 1)\n  \
        \    end,\n      process_str_helper(Rest, NewAcc);\n    $# ->\n      process_str_helper(Rest,\
        \ Acc ++ Acc);\n    $% ->\n      process_str_helper(Rest, lists:reverse(Acc));\n\
        \    _ ->\n      process_str_helper(Rest, Acc ++ [Char])\n  end."
      elixir: "defmodule Solution do\n  @spec process_str(s :: String.t) :: String.t\n\
        \  def process_str(s) do\n    s\n    |> String.graphemes()\n    |> Enum.reduce(\"\
        \", fn char, acc ->\n      case char do\n        \"*\" ->\n          if acc\
        \ == \"\", do: \"\", else: String.slice(acc, 0..-2)\n        \"#\" ->\n    \
        \      acc <> acc\n        \"%\" ->\n          String.reverse(acc)\n       \
        \ _ ->\n          acc <> char\n      end\n    end)\n  end\nend"
    approach: The algorithm processes the input string sequentially, character by character,
      and updates a result string based on the given rules. Letters are appended to
      the end, '*' removes the last character, '#' doubles the entire current string
      by appending it to itself, and '%' reverses the string. Because each operation
      depends only on the current state of the result string, a linear pass through
      the input string is sufficient for the simulation.
    time_complexity: O(2^N) where N is the length of the input string. Each '#' operation
      can double the current length of the result string. In the worst case, the total
      time spent on copying and reversing the result string grows as a geometric progression,
      leading to a complexity proportional to the final string length, which can be
      up to $2^{N-1}$. For $N=20$, this is approximately $10^6$ operations, which is
      efficient.
    space_complexity: O(2^N) to store the result string. In the worst-case scenario
      where the input consists mostly of duplication operations, the final string length
      can reach $2^{N-1}$. For $N=20$, the maximum space required is roughly 524,288
      characters, fitting within standard memory limits.
    elapsed_time: 503.56320333480835
    model: gemini-3-flash-preview
    generated_at: '2026-06-16 03:06:41 '
---

## Problem #3612: Process String with Special Operations I

**Difficulty:** Medium

**Topics:** String, Simulation

## Problem Description

<p>You are given a string <code>s</code> consisting of lowercase English letters and the special characters: <code>*</code>, <code>#</code>, and <code>%</code>.</p>

<p>Build a new string <code>result</code> by processing <code>s</code> according to the following rules from left to right:</p>

<ul>
	<li>If the letter is a <strong>lowercase</strong> English letter append it to <code>result</code>.</li>
	<li>A <code>&#39;*&#39;</code> <strong>removes</strong> the last character from <code>result</code>, if it exists.</li>
	<li>A <code>&#39;#&#39;</code> <strong>duplicates</strong> the current <code>result</code> and <strong>appends</strong> it to itself.</li>
	<li>A <code>&#39;%&#39;</code> <strong>reverses</strong> the current <code>result</code>.</li>
</ul>

<p>Return the final string <code>result</code> after processing all characters in <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;a#b%*&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;ba&quot;</span></p>

<p><strong>Explanation:</strong></p>

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;"><code>i</code></th>
			<th style="border: 1px solid black;"><code>s[i]</code></th>
			<th style="border: 1px solid black;">Operation</th>
			<th style="border: 1px solid black;">Current <code>result</code></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;"><code>&#39;a&#39;</code></td>
			<td style="border: 1px solid black;">Append <code>&#39;a&#39;</code></td>
			<td style="border: 1px solid black;"><code>&quot;a&quot;</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;"><code>&#39;#&#39;</code></td>
			<td style="border: 1px solid black;">Duplicate <code>result</code></td>
			<td style="border: 1px solid black;"><code>&quot;aa&quot;</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;"><code>&#39;b&#39;</code></td>
			<td style="border: 1px solid black;">Append <code>&#39;b&#39;</code></td>
			<td style="border: 1px solid black;"><code>&quot;aab&quot;</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;"><code>&#39;%&#39;</code></td>
			<td style="border: 1px solid black;">Reverse <code>result</code></td>
			<td style="border: 1px solid black;"><code>&quot;baa&quot;</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;"><code>&#39;*&#39;</code></td>
			<td style="border: 1px solid black;">Remove the last character</td>
			<td style="border: 1px solid black;"><code>&quot;ba&quot;</code></td>
		</tr>
	</tbody>
</table>

<p>Thus, the final <code>result</code> is <code>&quot;ba&quot;</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;z*#&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;&quot;</span></p>

<p><strong>Explanation:</strong></p>

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;"><code>i</code></th>
			<th style="border: 1px solid black;"><code>s[i]</code></th>
			<th style="border: 1px solid black;">Operation</th>
			<th style="border: 1px solid black;">Current <code>result</code></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;"><code>&#39;z&#39;</code></td>
			<td style="border: 1px solid black;">Append <code>&#39;z&#39;</code></td>
			<td style="border: 1px solid black;"><code>&quot;z&quot;</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;"><code>&#39;*&#39;</code></td>
			<td style="border: 1px solid black;">Remove the last character</td>
			<td style="border: 1px solid black;"><code>&quot;&quot;</code></td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;"><code>&#39;#&#39;</code></td>
			<td style="border: 1px solid black;">Duplicate the string</td>
			<td style="border: 1px solid black;"><code>&quot;&quot;</code></td>
		</tr>
	</tbody>
</table>

<p>Thus, the final <code>result</code> is <code>&quot;&quot;</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 20</code></li>
	<li><code>s</code> consists of only lowercase English letters and special characters <code>*</code>, <code>#</code>, and <code>%</code>.</li>
</ul>


## Hints

1. Simulate as described

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm processes the input string sequentially, character by character, and updates a result string based on the given rules. Letters are appended to the end, '*' removes the last character, '#' doubles the entire current string by appending it to itself, and '%' reverses the string. Because each operation depends only on the current state of the result string, a linear pass through the input string is sufficient for the simulation.

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

using namespace std;

class Solution {
public:
    string processStr(string s) {
        string result = "";
        for (char c : s) {
            if (c >= 'a' && c <= 'z') {
                result += c;
            } else if (c == '*') {
                if (!result.empty()) {
                    result.pop_back();
                }
            } else if (c == '#') {
                result += result;
            } else if (c == '%') {
                reverse(result.begin(), result.end());
            }
        }
        return result;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public String processStr(String s) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c >= 'a' && c <= 'z') {
                result.append(c);
            } else if (c == '*') {
                if (result.length() > 0) {
                    result.setLength(result.length() - 1);
                }
            } else if (c == '#') {
                result.append(result.toString());
            } else if (c == '%') {
                result.reverse();
            }
        }
        return result.toString();
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for char in s:
            if 'a' <= char <= 'z':
                result += char
            elif char == '*':
                if result:
                    result = result[:-1]
            elif char == '#':
                result += result
            elif char == '%':
                result = result[::-1]
        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def processStr(self, s: str) -> str:
        result = ""
        for char in s:
            if 'a' <= char <= 'z':
                result += char
            elif char == '*':
                if result:
                    result = result[:-1]
            elif char == '#':
                result += result
            elif char == '%':
                result = result[::-1]
        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

char* processStr(char* s) {
    int max_len = 1048576;
    char* res = (char*)malloc(max_len * sizeof(char));
    int len = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] >= 'a' && s[i] <= 'z') {
            res[len++] = s[i];
        } else if (s[i] == '*') {
            if (len > 0) {
                len--;
            }
        } else if (s[i] == '#') {
            if (len > 0 && len * 2 < max_len) {
                memcpy(res + len, res, len);
                len *= 2;
            }
        } else if (s[i] == '%') {
            for (int j = 0; j < len / 2; j++) {
                char temp = res[j];
                res[j] = res[len - 1 - j];
                res[len - 1 - j] = temp;
            }
        }
    }
    res[len] = '\0';
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public string ProcessStr(string s) {
        string result = "";
        foreach (char c in s) {
            if (c == '*') {
                if (result.Length > 0) {
                    result = result.Substring(0, result.Length - 1);
                }
            } else if (c == '#') {
                result += result;
            } else if (c == '%') {
                char[] charArray = result.ToCharArray();
                Array.Reverse(charArray);
                result = new string(charArray);
            } else {
                result += c;
            }
        }
        return result;
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
var processStr = function(s) {
    let result = "";
    for (let char of s) {
        if (char === '*') {
            if (result.length > 0) {
                result = result.slice(0, -1);
            }
        } else if (char === '#') {
            result += result;
        } else if (char === '%') {
            result = result.split('').reverse().join('');
        } else {
            result += char;
        }
    }
    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function processStr(s: string): string {
    let result: string = "";
    for (let char of s) {
        if (char === '*') {
            if (result.length > 0) {
                result = result.slice(0, -1);
            }
        } else if (char === '#') {
            result += result;
        } else if (char === '%') {
            result = result.split('').reverse().join('');
        } else {
            result += char;
        }
    }
    return result;
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
    function processStr($s) {
        $result = "";
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $char = $s[$i];
            if ($char === '*') {
                if (strlen($result) > 0) {
                    $result = substr($result, 0, -1);
                }
            } else if ($char === '#') {
                $result .= $result;
            } else if ($char === '%') {
                $result = strrev($result);
            } else {
                $result .= $char;
            }
        }
        return $result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func processStr(_ s: String) -> String {
        var result = ""
        for char in s {
            switch char {
            case "*":
                if !result.isEmpty {
                    result.removeLast()
                }
            case "#":
                result += result
            case "%":
                result = String(result.reversed())
            default:
                result.append(char)
            }
        }
        return result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun processStr(s: String): String {
        val result = StringBuilder()
        for (char in s) {
            when (char) {
                '*' -> {
                    if (result.isNotEmpty()) {
                        result.deleteCharAt(result.length - 1)
                    }
                }
                '#' -> {
                    result.append(result.toString())
                }
                '%' -> {
                    result.reverse()
                }
                else -> {
                    result.append(char)
                }
            }
        }
        return result.toString()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  String processStr(String s) {
    String result = "";
    for (int i = 0; i < s.length; i++) {
      String char = s[i];
      if (char == '*') {
        if (result.isNotEmpty) {
          result = result.substring(0, result.length - 1);
        }
      } else if (char == '#') {
        result = result + result;
      } else if (char == '%') {
        result = result.split('').reversed.join('');
      } else {
        result += char;
      }
    }
    return result;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func processStr(s string) string {
	res := []rune{}
	for _, char := range s {
		switch char {
		case '*':
			if len(res) > 0 {
				res = res[:len(res)-1]
			}
		case '#':
			res = append(res, res...)
		case '%':
			for i, j := 0, len(res)-1; i < j; i, j = i+1, j-1 {
				res[i], res[j] = res[j], res[i]
			}
		default:
			res = append(res, char)
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
def process_str(s)
  result = ""
  s.each_char do |char|
    case char
    when '*'
      result.chop! if result.length > 0
    when '#'
      result += result
    when '%'
      result.reverse!
    else
      result << char
    end
  end
  result
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def processStr(s: String): String = {
        var result = ""
        for (char <- s) {
            char match {
                case '*' =>
                    if (result.nonEmpty) {
                        result = result.substring(0, result.length - 1)
                    }
                case '#' =>
                    result = result + result
                case '%' =>
                    result = result.reverse
                case _ =>
                    result = result + char
            }
        }
        result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn process_str(s: String) -> String {
        let mut result = String::new();
        for c in s.chars() {
            match c {
                '*' => {
                    result.pop();
                }
                '#' => {
                    let current = result.clone();
                    result.push_str(&current);
                }
                '%' => {
                    result = result.chars().rev().collect();
                }
                _ => {
                    result.push(c);
                }
            }
        }
        result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (process-str s)
  (-> string? string?)
  (let loop ([chars (string->list s)]
             [res ""])
    (if (null? chars)
        res
        (let ([c (car chars)]
              [rest (cdr chars)])
          (cond
            [(char=? c #\*)
             (loop rest (if (string=? res "") "" (substring res 0 (- (string-length res) 1))))]
            [(char=? c #\#)
             (loop rest (string-append res res))]
            [(char=? c #\%)
             (loop rest (list->string (reverse (string->list res))))]
            [else
             (loop rest (string-append res (string c)))])))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec process_str(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
process_str(S) ->
  StrList = binary_to_list(S),
  Result = process_str_helper(StrList, []),
  list_to_binary(Result).

process_str_helper([], Acc) -> Acc;
process_str_helper([Char | Rest], Acc) ->
  case Char of
    $* ->
      NewAcc = case Acc of
        [] -> [];
        _ -> lists:sublist(Acc, 1, length(Acc) - 1)
      end,
      process_str_helper(Rest, NewAcc);
    $# ->
      process_str_helper(Rest, Acc ++ Acc);
    $% ->
      process_str_helper(Rest, lists:reverse(Acc));
    _ ->
      process_str_helper(Rest, Acc ++ [Char])
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec process_str(s :: String.t) :: String.t
  def process_str(s) do
    s
    |> String.graphemes()
    |> Enum.reduce("", fn char, acc ->
      case char do
        "*" ->
          if acc == "", do: "", else: String.slice(acc, 0..-2)
        "#" ->
          acc <> acc
        "%" ->
          String.reverse(acc)
        _ ->
          acc <> char
      end
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(2^N) where N is the length of the input string. Each '#' operation can double the current length of the result string. In the worst case, the total time spent on copying and reversing the result string grows as a geometric progression, leading to a complexity proportional to the final string length, which can be up to $2^{N-1}$. For $N=20$, this is approximately $10^6$ operations, which is efficient.
- **Space Complexity:** O(2^N) to store the result string. In the worst-case scenario where the input consists mostly of duplication operations, the final string length can reach $2^{N-1}$. For $N=20$, the maximum space required is roughly 524,288 characters, fitting within standard memory limits.
