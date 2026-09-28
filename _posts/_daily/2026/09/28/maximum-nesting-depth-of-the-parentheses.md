---
layout: post
title: "Maximum Nesting Depth of the Parentheses"
date: 2026-09-28 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["String", "Stack", "Bracket Sequences"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxDepth(string s) {\n        int max_depth\
        \ = 0;\n        int current_depth = 0;\n        for (char c : s) {\n       \
        \     if (c == '(') {\n                current_depth++;\n                if\
        \ (current_depth > max_depth) {\n                    max_depth = current_depth;\n\
        \                }\n            } else if (c == ')') {\n                current_depth--;\n\
        \            }\n        }\n        return max_depth;\n    }\n};"
      java: "class Solution {\n    public int maxDepth(String s) {\n        int maxDepth\
        \ = 0;\n        int currentDepth = 0;\n        for (int i = 0; i < s.length();\
        \ i++) {\n            char c = s.charAt(i);\n            if (c == '(') {\n \
        \               currentDepth++;\n                if (currentDepth > maxDepth)\
        \ {\n                    maxDepth = currentDepth;\n                }\n     \
        \       } else if (c == ')') {\n                currentDepth--;\n          \
        \  }\n        }\n        return maxDepth;\n    }\n}"
      python: "class Solution(object):\n    def maxDepth(self, s):\n        \"\"\"\n\
        \        :type s: str\n        :rtype: int\n        \"\"\"\n        max_depth\
        \ = 0\n        current_depth = 0\n        for char in s:\n            if char\
        \ == '(':\n                current_depth += 1\n                if current_depth\
        \ > max_depth:\n                    max_depth = current_depth\n            elif\
        \ char == ')':\n                current_depth -= 1\n        return max_depth"
      python3: "class Solution:\n    def maxDepth(self, s: str) -> int:\n        max_depth\
        \ = 0\n        current_depth = 0\n        for char in s:\n            if char\
        \ == '(':\n                current_depth += 1\n                if current_depth\
        \ > max_depth:\n                    max_depth = current_depth\n            elif\
        \ char == ')':\n                current_depth -= 1\n        return max_depth"
      c: "int maxDepth(char* s) {\n    int max_depth = 0;\n    int current_depth = 0;\n\
        \    for (int i = 0; s[i] != '\\0'; i++) {\n        if (s[i] == '(') {\n   \
        \         current_depth++;\n            if (current_depth > max_depth) {\n \
        \               max_depth = current_depth;\n            }\n        } else if\
        \ (s[i] == ')') {\n            current_depth--;\n        }\n    }\n    return\
        \ max_depth;\n}"
      csharp: "public class Solution {\n    public int MaxDepth(string s) {\n      \
        \  int maxDepth = 0;\n        int currentDepth = 0;\n        foreach (char c\
        \ in s) {\n            if (c == '(') {\n                currentDepth++;\n  \
        \              if (currentDepth > maxDepth) {\n                    maxDepth\
        \ = currentDepth;\n                }\n            } else if (c == ')') {\n \
        \               currentDepth--;\n            }\n        }\n        return maxDepth;\n\
        \    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {number}\n */\nvar maxDepth\
        \ = function(s) {\n    let maxDepth = 0;\n    let currentDepth = 0;\n    for\
        \ (let i = 0; i < s.length; i++) {\n        if (s[i] === '(') {\n          \
        \  currentDepth++;\n            if (currentDepth > maxDepth) {\n           \
        \     maxDepth = currentDepth;\n            }\n        } else if (s[i] === ')')\
        \ {\n            currentDepth--;\n        }\n    }\n    return maxDepth;\n};"
      typescript: "function maxDepth(s: string): number {\n    let maxDepthValue = 0;\n\
        \    let currentDepthValue = 0;\n    for (let i = 0; i < s.length; i++) {\n\
        \        if (s[i] === '(') {\n            currentDepthValue++;\n           \
        \ if (currentDepthValue > maxDepthValue) {\n                maxDepthValue =\
        \ currentDepthValue;\n            }\n        } else if (s[i] === ')') {\n  \
        \          currentDepthValue--;\n        }\n    }\n    return maxDepthValue;\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return Integer\n\
        \     */\n    function maxDepth($s) {\n        $maxDepth = 0;\n        $currentDepth\
        \ = 0;\n        $length = strlen($s);\n        for ($i = 0; $i < $length; $i++)\
        \ {\n            if ($s[$i] === '(') {\n                $currentDepth++;\n \
        \               if ($currentDepth > $maxDepth) {\n                    $maxDepth\
        \ = $currentDepth;\n                }\n            } else if ($s[$i] === ')')\
        \ {\n                $currentDepth--;\n            }\n        }\n        return\
        \ $maxDepth;\n    }\n}"
      swift: "class Solution {\n    func maxDepth(_ s: String) -> Int {\n        var\
        \ maxDepth = 0\n        var currentDepth = 0\n        for char in s {\n    \
        \        if char == \"(\" {\n                currentDepth += 1\n           \
        \     if currentDepth > maxDepth {\n                    maxDepth = currentDepth\n\
        \                }\n            } else if char == \")\" {\n                currentDepth\
        \ -= 1\n            }\n        }\n        return maxDepth\n    }\n}"
      kotlin: "class Solution {\n    fun maxDepth(s: String): Int {\n        var maxDepth\
        \ = 0\n        var currentDepth = 0\n        for (char in s) {\n           \
        \ if (char == '(') {\n                currentDepth++\n                if (currentDepth\
        \ > maxDepth) {\n                    maxDepth = currentDepth\n             \
        \   }\n            } else if (char == ')') {\n                currentDepth--\n\
        \            }\n        }\n        return maxDepth\n    }\n}"
      dart: "class Solution {\n  int maxDepth(String s) {\n    int maxDepthValue = 0;\n\
        \    int currentDepthValue = 0;\n    for (int i = 0; i < s.length; i++) {\n\
        \      if (s[i] == '(') {\n        currentDepthValue++;\n        if (currentDepthValue\
        \ > maxDepthValue) {\n          maxDepthValue = currentDepthValue;\n       \
        \ }\n      } else if (s[i] == ')') {\n        currentDepthValue--;\n      }\n\
        \    }\n    return maxDepthValue;\n  }\n}"
      go: "func maxDepth(s string) int {\n    maxDepthValue := 0\n    currentDepthValue\
        \ := 0\n    for i := 0; i < len(s); i++ {\n        if s[i] == '(' {\n      \
        \      currentDepthValue++\n            if currentDepthValue > maxDepthValue\
        \ {\n                maxDepthValue = currentDepthValue\n            }\n    \
        \    } else if s[i] == ')' {\n            currentDepthValue--\n        }\n \
        \   }\n    return maxDepthValue\n}"
      ruby: "# @param {String} s\n# @return {Integer}\ndef max_depth(s)\n  max_d = 0\n\
        \  curr_d = 0\n  s.each_char do |c|\n    if c == '(' \n      curr_d += 1\n \
        \     max_d = [max_d, curr_d].max\n    elsif c == ')'\n      curr_d -= 1\n \
        \   end\n  end\n  max_d\nend"
      scala: "object Solution {\n    def maxDepth(s: String): Int = {\n        var maxD\
        \ = 0\n        var currD = 0\n        for (c <- s) {\n            if (c == '(')\
        \ {\n                currD += 1\n                if (currD > maxD) maxD = currD\n\
        \            } else if (c == ')') {\n                currD -= 1\n          \
        \  }\n        }\n        maxD\n    }\n}"
      rust: "impl Solution {\n    pub fn max_depth(s: String) -> i32 {\n        let\
        \ mut max_d = 0;\n        let mut curr_d = 0;\n        for c in s.chars() {\n\
        \            if c == '(' {\n                curr_d += 1;\n                if\
        \ curr_d > max_d {\n                    max_d = curr_d;\n                }\n\
        \            } else if c == ')' {\n                curr_d -= 1;\n          \
        \  }\n        }\n        max_d\n    }\n}"
      racket: "(define/contract (max-depth s)\n  (-> string? exact-integer?)\n  (let\
        \ loop ([chars (string->list s)]\n             [curr-d 0]\n             [max-d\
        \ 0])\n    (if (null? chars)\n        max-d\n        (let ([c (car chars)])\n\
        \          (cond\n            [(char=? c #\\() (loop (cdr chars) (+ curr-d 1)\
        \ (max max-d (+ curr-d 1)))]\n            [(char=? c #\\)) (loop (cdr chars)\
        \ (- curr-d 1) max-d)]\n            [else (loop (cdr chars) curr-d max-d)])))))"
      erlang: "-spec max_depth(S :: unicode:unicode_binary()) -> integer().\nmax_depth(S)\
        \ ->\n  max_depth_list(unicode:characters_to_list(S), 0, 0).\n\nmax_depth_list([],\
        \ _CurrD, MaxD) ->\n  MaxD;\nmax_depth_list([$( | T], CurrD, MaxD) ->\n  NewCurrD\
        \ = CurrD + 1,\n  NewMaxD = if NewCurrD > MaxD -> NewCurrD; true -> MaxD end,\n\
        \  max_depth_list(T, NewCurrD, NewMaxD);\nmax_depth_list([$) | T], CurrD, MaxD)\
        \ ->\n  max_depth_list(T, CurrD - 1, MaxD);\nmax_depth_list([_ | T], CurrD,\
        \ MaxD) ->\n  max_depth_list(T, CurrD, MaxD)."
      elixir: "defmodule Solution do\n  @spec max_depth(s :: String.t) :: integer\n\
        \  def max_depth(s) do\n    s\n    |> String.graphemes()\n    |> Enum.reduce({0,\
        \ 0}, fn char, {curr_d, max_d} ->\n      case char do\n        \"(\" ->\n  \
        \        new_curr = curr_d + 1\n          {new_curr, max(max_d, new_curr)}\n\
        \        \")\" ->\n          {curr_d - 1, max_d}\n        _ ->\n          {curr_d,\
        \ max_d}\n      end\n    end)\n    |> elem(1)\n  end\nend"
    approach: The algorithm employs a single-pass traversal technique to calculate the
      maximum nesting depth of a given Valid Parentheses String (VPS). By maintaining
      a running counter that increments whenever an opening parenthesis '(' is encountered
      and decrements whenever a closing parenthesis ')' is encountered, we effectively
      track the current level of nesting at any specific point in the string.
    time_complexity: O(n), where n is the length of the string s. The algorithm performs
      a single linear scan through the input string, performing constant-time increment,
      decrement, and comparison operations for each character.
    space_complexity: O(1). Apart from the input string, the algorithm only requires
      a constant amount of extra space to store the current nesting depth and the maximum
      depth found during the traversal.
    elapsed_time: 1145.4512705802917
    model: gemini-3-flash-preview
    generated_at: '2026-09-28 03:11:21 '
---

## Problem #1614: Maximum Nesting Depth of the Parentheses

**Difficulty:** Easy

**Topics:** String, Stack, Bracket Sequences

## Problem Description

<p>Given a <strong>valid parentheses string</strong> <code>s</code>, return the <strong>nesting depth</strong> of<em> </em><code>s</code>. The nesting depth is the <strong>maximum</strong> number of nested parentheses.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;(1+(2*3)+((8)/4))+1&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>Digit 8 is inside of 3 nested parentheses in the string.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;(1)+((2))+(((3)))&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>Digit 3 is inside of 3 nested parentheses in the string.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;()(())((()()))&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> consists of digits <code>0-9</code> and characters <code>&#39;+&#39;</code>, <code>&#39;-&#39;</code>, <code>&#39;*&#39;</code>, <code>&#39;/&#39;</code>, <code>&#39;(&#39;</code>, and <code>&#39;)&#39;</code>.</li>
	<li>It is guaranteed that parentheses expression <code>s</code> is a VPS.</li>
</ul>


## Hints

1. The depth of any character in the VPS is the ( number of left brackets before it ) - ( number of right brackets before it )

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm employs a single-pass traversal technique to calculate the maximum nesting depth of a given Valid Parentheses String (VPS). By maintaining a running counter that increments whenever an opening parenthesis '(' is encountered and decrements whenever a closing parenthesis ')' is encountered, we effectively track the current level of nesting at any specific point in the string.

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
    int maxDepth(string s) {
        int max_depth = 0;
        int current_depth = 0;
        for (char c : s) {
            if (c == '(') {
                current_depth++;
                if (current_depth > max_depth) {
                    max_depth = current_depth;
                }
            } else if (c == ')') {
                current_depth--;
            }
        }
        return max_depth;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maxDepth(String s) {
        int maxDepth = 0;
        int currentDepth = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                currentDepth++;
                if (currentDepth > maxDepth) {
                    maxDepth = currentDepth;
                }
            } else if (c == ')') {
                currentDepth--;
            }
        }
        return maxDepth;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_depth = 0
        current_depth = 0
        for char in s:
            if char == '(':
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif char == ')':
                current_depth -= 1
        return max_depth
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        current_depth = 0
        for char in s:
            if char == '(':
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif char == ')':
                current_depth -= 1
        return max_depth
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int maxDepth(char* s) {
    int max_depth = 0;
    int current_depth = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '(') {
            current_depth++;
            if (current_depth > max_depth) {
                max_depth = current_depth;
            }
        } else if (s[i] == ')') {
            current_depth--;
        }
    }
    return max_depth;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaxDepth(string s) {
        int maxDepth = 0;
        int currentDepth = 0;
        foreach (char c in s) {
            if (c == '(') {
                currentDepth++;
                if (currentDepth > maxDepth) {
                    maxDepth = currentDepth;
                }
            } else if (c == ')') {
                currentDepth--;
            }
        }
        return maxDepth;
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
var maxDepth = function(s) {
    let maxDepth = 0;
    let currentDepth = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '(') {
            currentDepth++;
            if (currentDepth > maxDepth) {
                maxDepth = currentDepth;
            }
        } else if (s[i] === ')') {
            currentDepth--;
        }
    }
    return maxDepth;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxDepth(s: string): number {
    let maxDepthValue = 0;
    let currentDepthValue = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '(') {
            currentDepthValue++;
            if (currentDepthValue > maxDepthValue) {
                maxDepthValue = currentDepthValue;
            }
        } else if (s[i] === ')') {
            currentDepthValue--;
        }
    }
    return maxDepthValue;
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
    function maxDepth($s) {
        $maxDepth = 0;
        $currentDepth = 0;
        $length = strlen($s);
        for ($i = 0; $i < $length; $i++) {
            if ($s[$i] === '(') {
                $currentDepth++;
                if ($currentDepth > $maxDepth) {
                    $maxDepth = $currentDepth;
                }
            } else if ($s[$i] === ')') {
                $currentDepth--;
            }
        }
        return $maxDepth;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxDepth(_ s: String) -> Int {
        var maxDepth = 0
        var currentDepth = 0
        for char in s {
            if char == "(" {
                currentDepth += 1
                if currentDepth > maxDepth {
                    maxDepth = currentDepth
                }
            } else if char == ")" {
                currentDepth -= 1
            }
        }
        return maxDepth
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxDepth(s: String): Int {
        var maxDepth = 0
        var currentDepth = 0
        for (char in s) {
            if (char == '(') {
                currentDepth++
                if (currentDepth > maxDepth) {
                    maxDepth = currentDepth
                }
            } else if (char == ')') {
                currentDepth--
            }
        }
        return maxDepth
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maxDepth(String s) {
    int maxDepthValue = 0;
    int currentDepthValue = 0;
    for (int i = 0; i < s.length; i++) {
      if (s[i] == '(') {
        currentDepthValue++;
        if (currentDepthValue > maxDepthValue) {
          maxDepthValue = currentDepthValue;
        }
      } else if (s[i] == ')') {
        currentDepthValue--;
      }
    }
    return maxDepthValue;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxDepth(s string) int {
    maxDepthValue := 0
    currentDepthValue := 0
    for i := 0; i < len(s); i++ {
        if s[i] == '(' {
            currentDepthValue++
            if currentDepthValue > maxDepthValue {
                maxDepthValue = currentDepthValue
            }
        } else if s[i] == ')' {
            currentDepthValue--
        }
    }
    return maxDepthValue
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @return {Integer}
def max_depth(s)
  max_d = 0
  curr_d = 0
  s.each_char do |c|
    if c == '(' 
      curr_d += 1
      max_d = [max_d, curr_d].max
    elsif c == ')'
      curr_d -= 1
    end
  end
  max_d
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxDepth(s: String): Int = {
        var maxD = 0
        var currD = 0
        for (c <- s) {
            if (c == '(') {
                currD += 1
                if (currD > maxD) maxD = currD
            } else if (c == ')') {
                currD -= 1
            }
        }
        maxD
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_depth(s: String) -> i32 {
        let mut max_d = 0;
        let mut curr_d = 0;
        for c in s.chars() {
            if c == '(' {
                curr_d += 1;
                if curr_d > max_d {
                    max_d = curr_d;
                }
            } else if c == ')' {
                curr_d -= 1;
            }
        }
        max_d
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (max-depth s)
  (-> string? exact-integer?)
  (let loop ([chars (string->list s)]
             [curr-d 0]
             [max-d 0])
    (if (null? chars)
        max-d
        (let ([c (car chars)])
          (cond
            [(char=? c #\() (loop (cdr chars) (+ curr-d 1) (max max-d (+ curr-d 1)))]
            [(char=? c #\)) (loop (cdr chars) (- curr-d 1) max-d)]
            [else (loop (cdr chars) curr-d max-d)])))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_depth(S :: unicode:unicode_binary()) -> integer().
max_depth(S) ->
  max_depth_list(unicode:characters_to_list(S), 0, 0).

max_depth_list([], _CurrD, MaxD) ->
  MaxD;
max_depth_list([$( | T], CurrD, MaxD) ->
  NewCurrD = CurrD + 1,
  NewMaxD = if NewCurrD > MaxD -> NewCurrD; true -> MaxD end,
  max_depth_list(T, NewCurrD, NewMaxD);
max_depth_list([$) | T], CurrD, MaxD) ->
  max_depth_list(T, CurrD - 1, MaxD);
max_depth_list([_ | T], CurrD, MaxD) ->
  max_depth_list(T, CurrD, MaxD).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_depth(s :: String.t) :: integer
  def max_depth(s) do
    s
    |> String.graphemes()
    |> Enum.reduce({0, 0}, fn char, {curr_d, max_d} ->
      case char do
        "(" ->
          new_curr = curr_d + 1
          {new_curr, max(max_d, new_curr)}
        ")" ->
          {curr_d - 1, max_d}
        _ ->
          {curr_d, max_d}
      end
    end)
    |> elem(1)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n), where n is the length of the string s. The algorithm performs a single linear scan through the input string, performing constant-time increment, decrement, and comparison operations for each character.
- **Space Complexity:** O(1). Apart from the input string, the algorithm only requires a constant amount of extra space to store the current nesting depth and the maximum depth found during the traversal.
