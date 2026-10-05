---
layout: post
title: "Score of Parentheses"
date: 2026-10-05 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Stack", "Bracket Sequences"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/score-of-parentheses/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int scoreOfParentheses(string s) {\n    \
        \    int ans = 0;\n        int depth = 0;\n        for (int i = 0; i < s.length();\
        \ i++) {\n            if (s[i] == '(') {\n                depth++;\n       \
        \     } else {\n                depth--;\n                if (s[i - 1] == '(')\
        \ {\n                    ans += 1 << depth;\n                }\n           \
        \ }\n        }\n        return ans;\n    }\n};"
      java: "class Solution {\n    public int scoreOfParentheses(String s) {\n     \
        \   int ans = 0;\n        int depth = 0;\n        for (int i = 0; i < s.length();\
        \ i++) {\n            if (s.charAt(i) == '(') {\n                depth++;\n\
        \            } else {\n                depth--;\n                if (s.charAt(i\
        \ - 1) == '(') {\n                    ans += 1 << depth;\n                }\n\
        \            }\n        }\n        return ans;\n    }\n}"
      python: "class Solution(object):\n    def scoreOfParentheses(self, s):\n     \
        \   \"\"\"\n        :type s: str\n        :rtype: int\n        \"\"\"\n    \
        \    ans = 0\n        depth = 0\n        for i in range(len(s)):\n         \
        \   if s[i] == '(':\n                depth += 1\n            else:\n       \
        \         depth -= 1\n                if s[i-1] == '(':\n                  \
        \  ans += (1 << depth)\n        return ans"
      python3: "class Solution:\n    def scoreOfParentheses(self, s: str) -> int:\n\
        \        ans = 0\n        depth = 0\n        for i in range(len(s)):\n     \
        \       if s[i] == '(':\n                depth += 1\n            else:\n   \
        \             depth -= 1\n                if s[i-1] == '(':\n              \
        \      ans += (1 << depth)\n        return ans"
      c: "int scoreOfParentheses(char* s) {\n    int ans = 0;\n    int depth = 0;\n\
        \    for (int i = 0; s[i] != '\\0'; i++) {\n        if (s[i] == '(') {\n   \
        \         depth++;\n        } else {\n            depth--;\n            if (i\
        \ > 0 && s[i - 1] == '(') {\n                ans += 1 << depth;\n          \
        \  }\n        }\n    }\n    return ans;\n}"
      csharp: "public class Solution {\n    public int ScoreOfParentheses(string s)\
        \ {\n        int score = 0;\n        int depth = 0;\n        for (int i = 0;\
        \ i < s.Length; i++) {\n            if (s[i] == '(') {\n                depth++;\n\
        \            } else {\n                depth--;\n                if (i > 0 &&\
        \ s[i - 1] == '(') {\n                    score += (1 << depth);\n         \
        \       }\n            }\n        }\n        return score;\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {number}\n */\nvar scoreOfParentheses\
        \ = function(s) {\n    let score = 0;\n    let depth = 0;\n    for (let i =\
        \ 0; i < s.length; i++) {\n        if (s[i] === '(') {\n            depth++;\n\
        \        } else {\n            depth--;\n            if (i > 0 && s[i - 1] ===\
        \ '(') {\n                score += (1 << depth);\n            }\n        }\n\
        \    }\n    return score;\n};"
      typescript: "function scoreOfParentheses(s: string): number {\n    let score:\
        \ number = 0;\n    let depth: number = 0;\n    for (let i: number = 0; i < s.length;\
        \ i++) {\n        if (s[i] === '(') {\n            depth++;\n        } else\
        \ {\n            depth--;\n            if (i > 0 && s[i - 1] === '(') {\n  \
        \              score += (1 << depth);\n            }\n        }\n    }\n   \
        \ return score;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return Integer\n\
        \     */\n    function scoreOfParentheses($s) {\n        $score = 0;\n     \
        \   $depth = 0;\n        $len = strlen($s);\n        for ($i = 0; $i < $len;\
        \ $i++) {\n            if ($s[$i] == '(') {\n                $depth++;\n   \
        \         } else {\n                $depth--;\n                if ($i > 0 &&\
        \ $s[$i - 1] == '(') {\n                    $score += (1 << $depth);\n     \
        \           }\n            }\n        }\n        return $score;\n    }\n}"
      swift: "class Solution {\n    func scoreOfParentheses(_ s: String) -> Int {\n\
        \        var score = 0\n        var depth = 0\n        let chars = Array(s)\n\
        \        for i in 0..<chars.count {\n            if chars[i] == \"(\" {\n  \
        \              depth += 1\n            } else {\n                depth -= 1\n\
        \                if i > 0 && chars[i-1] == \"(\" {\n                    score\
        \ += (1 << depth)\n                }\n            }\n        }\n        return\
        \ score\n    }\n}"
      kotlin: "class Solution {\n    fun scoreOfParentheses(s: String): Int {\n    \
        \    var ans = 0\n        var depth = 0\n        for (i in s.indices) {\n  \
        \          if (s[i] == '(') {\n                depth++\n            } else {\n\
        \                depth--\n                if (i > 0 && s[i - 1] == '(') {\n\
        \                    ans += 1 shl depth\n                }\n            }\n\
        \        }\n        return ans\n    }\n}"
      dart: "class Solution {\n  int scoreOfParentheses(String s) {\n    int ans = 0;\n\
        \    int depth = 0;\n    for (int i = 0; i < s.length; i++) {\n      if (s[i]\
        \ == '(') {\n        depth++;\n      } else {\n        depth--;\n        if\
        \ (i > 0 && s[i - 1] == '(') {\n          ans += 1 << depth;\n        }\n  \
        \    }\n    }\n    return ans;\n  }\n}"
      go: "func scoreOfParentheses(s string) int {\n    ans := 0\n    depth := 0\n \
        \   for i := 0; i < len(s); i++ {\n        if s[i] == '(' {\n            depth++\n\
        \        } else {\n            depth--\n            if i > 0 && s[i-1] == '('\
        \ {\n                ans += 1 << depth\n            }\n        }\n    }\n  \
        \  return ans\n}"
      ruby: "# @param {String} s\n# @return {Integer}\ndef score_of_parentheses(s)\n\
        \    ans = 0\n    depth = 0\n    s.chars.each_with_index do |char, i|\n    \
        \    if char == '('\n            depth += 1\n        else\n            depth\
        \ -= 1\n            if i > 0 && s[i-1] == '('\n                ans += 1 << depth\n\
        \            end\n        end\n    end\n    ans\nend"
      scala: "object Solution {\n    def scoreOfParentheses(s: String): Int = {\n  \
        \      var ans = 0\n        var depth = 0\n        for (i <- 0 until s.length)\
        \ {\n            if (s(i) == '(') {\n                depth += 1\n          \
        \  } else {\n                depth -= 1\n                if (i > 0 && s(i -\
        \ 1) == '(') {\n                    ans += (1 << depth)\n                }\n\
        \            }\n        }\n        ans\n    }\n}"
      rust: "impl Solution {\n    pub fn score_of_parentheses(s: String) -> i32 {\n\
        \        let mut ans = 0;\n        let mut depth = 0;\n        let bytes = s.as_bytes();\n\
        \        for i in 0..bytes.len() {\n            if bytes[i] == b'(' {\n    \
        \            depth += 1;\n            } else {\n                depth -= 1;\n\
        \                if i > 0 && bytes[i - 1] == b'(' {\n                    ans\
        \ += 1 << depth;\n                }\n            }\n        }\n        ans\n\
        \    }\n}"
      racket: "(define/contract (score-of-parentheses s)\n  (-> string? exact-integer?)\n\
        \  (let ([chars (string->list s)])\n    (let loop ([lst chars] [depth 0] [prev\
        \ #f] [ans 0])\n      (if (null? lst)\n          ans\n          (let ([curr\
        \ (car lst)])\n            (if (char=? curr #\\()\n                (loop (cdr\
        \ lst) (+ depth 1) #\\( ans)\n                (let ([new-ans (if (and prev (char=?\
        \ prev #\\()))\n                                   (+ ans (expt 2 (- depth 1)))\n\
        \                                   ans)])\n                  (loop (cdr lst)\
        \ (- depth 1) #\\) new-ans))))))))"
      erlang: "-spec score_of_parentheses(S :: unicode:unicode_binary()) -> integer().\n\
        score_of_parentheses(S) ->\n  solve(binary_to_list(S), 0, undefined, 0).\n\n\
        solve([], _Depth, _Prev, Ans) ->\n  Ans;\nsolve([$( | Rest], Depth, _Prev, Ans)\
        \ ->\n  solve(Rest, Depth + 1, $(, Ans);\nsolve([$) | Rest], Depth, Prev, Ans)\
        \ ->\n  NewAns = if\n    Prev =:= $( -> Ans + (1 bsl (Depth - 1));\n    true\
        \ -> Ans\n  end,\n  solve(Rest, Depth - 1, $), NewAns)."
      elixir: "defmodule Solution do\n  @spec score_of_parentheses(s :: String.t) ::\
        \ integer\n  def score_of_parentheses(s) do\n    {ans, _, _} = Enum.reduce(String.to_charlist(s),\
        \ {0, 0, nil}, fn char, {ans, depth, prev} ->\n      case char do\n        ?(\
        \ -> {ans, depth + 1, ?(}\n        ?) ->\n          new_ans = if prev == ?(\
        \ do\n            ans + round(:math.pow(2, depth - 1))\n          else\n   \
        \         ans\n          end\n          {new_ans, depth - 1, ?)}\n      end\n\
        \    end)\n    ans\n  end\nend"
    approach: 'The core intuition is that every balanced parentheses string can be viewed
      as a collection of nested leaf nodes. Each leaf node, represented by the pair
      ''()'', contributes a value of 2 raised to the power of its nesting depth. For
      example, in the string ''(())'', the inner leaf ''()'' is at a nesting depth of
      1 (it is enclosed by one outer pair), effectively contributing $2^1 = 2$ to the
      final result. In ''()()'', there are two leaf nodes each at depth 0, contributing
      $2^0 + 2^0 = 1 + 1 = 2$.


      The algorithm iterates through the string while maintaining a depth counter that
      tracks the current nesting level. When an opening parenthesis is encountered,
      the depth increases; when a closing one is encountered, the depth decreases. If
      a closing parenthesis immediately follows an opening one (checked by comparing
      the current character with the previous one), it identifies a leaf node. We then
      add $1 \ll \text{depth}$ to the running total (where depth is the value after
      the current decrement). This approach is efficient as it avoids recursion or stack-based
      score accumulation by identifying the contribution of each pair at its base level.'
    time_complexity: O(n) where n is the length of the string. The algorithm performs
      a single linear scan of the input string, performing constant-time operations
      at each step.
    space_complexity: O(1) as we only maintain two integer variables, one for the current
      nesting depth and one for the cumulative score, regardless of the input size.
    elapsed_time: 317.03451204299927
    model: gemini-3-flash-preview
    generated_at: '2026-10-05 03:26:09 '
---

## Problem #856: Score of Parentheses

**Difficulty:** Medium

**Topics:** String, Stack, Bracket Sequences

## Problem Description

<p>Given a balanced parentheses string <code>s</code>, return <em>the <strong>score</strong> of the string</em>.</p>

<p>The <strong>score</strong> of a balanced parentheses string is based on the following rule:</p>

<ul>
	<li><code>&quot;()&quot;</code> has score <code>1</code>.</li>
	<li><code>AB</code> has score <code>A + B</code>, where <code>A</code> and <code>B</code> are balanced parentheses strings.</li>
	<li><code>(A)</code> has score <code>2 * A</code>, where <code>A</code> is a balanced parentheses string.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;()&quot;
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(())&quot;
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;()()&quot;
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 50</code></li>
	<li><code>s</code> consists of only <code>&#39;(&#39;</code> and <code>&#39;)&#39;</code>.</li>
	<li><code>s</code> is a balanced parentheses string.</li>
</ul>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The core intuition is that every balanced parentheses string can be viewed as a collection of nested leaf nodes. Each leaf node, represented by the pair '()', contributes a value of 2 raised to the power of its nesting depth. For example, in the string '(())', the inner leaf '()' is at a nesting depth of 1 (it is enclosed by one outer pair), effectively contributing $2^1 = 2$ to the final result. In '()()', there are two leaf nodes each at depth 0, contributing $2^0 + 2^0 = 1 + 1 = 2$.

The algorithm iterates through the string while maintaining a depth counter that tracks the current nesting level. When an opening parenthesis is encountered, the depth increases; when a closing one is encountered, the depth decreases. If a closing parenthesis immediately follows an opening one (checked by comparing the current character with the previous one), it identifies a leaf node. We then add $1 \ll \text{depth}$ to the running total (where depth is the value after the current decrement). This approach is efficient as it avoids recursion or stack-based score accumulation by identifying the contribution of each pair at its base level.

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
    int scoreOfParentheses(string s) {
        int ans = 0;
        int depth = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(') {
                depth++;
            } else {
                depth--;
                if (s[i - 1] == '(') {
                    ans += 1 << depth;
                }
            }
        }
        return ans;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int scoreOfParentheses(String s) {
        int ans = 0;
        int depth = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                depth++;
            } else {
                depth--;
                if (s.charAt(i - 1) == '(') {
                    ans += 1 << depth;
                }
            }
        }
        return ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        depth = 0
        for i in range(len(s)):
            if s[i] == '(':
                depth += 1
            else:
                depth -= 1
                if s[i-1] == '(':
                    ans += (1 << depth)
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = 0
        depth = 0
        for i in range(len(s)):
            if s[i] == '(':
                depth += 1
            else:
                depth -= 1
                if s[i-1] == '(':
                    ans += (1 << depth)
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int scoreOfParentheses(char* s) {
    int ans = 0;
    int depth = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '(') {
            depth++;
        } else {
            depth--;
            if (i > 0 && s[i - 1] == '(') {
                ans += 1 << depth;
            }
        }
    }
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int ScoreOfParentheses(string s) {
        int score = 0;
        int depth = 0;
        for (int i = 0; i < s.Length; i++) {
            if (s[i] == '(') {
                depth++;
            } else {
                depth--;
                if (i > 0 && s[i - 1] == '(') {
                    score += (1 << depth);
                }
            }
        }
        return score;
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
var scoreOfParentheses = function(s) {
    let score = 0;
    let depth = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '(') {
            depth++;
        } else {
            depth--;
            if (i > 0 && s[i - 1] === '(') {
                score += (1 << depth);
            }
        }
    }
    return score;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function scoreOfParentheses(s: string): number {
    let score: number = 0;
    let depth: number = 0;
    for (let i: number = 0; i < s.length; i++) {
        if (s[i] === '(') {
            depth++;
        } else {
            depth--;
            if (i > 0 && s[i - 1] === '(') {
                score += (1 << depth);
            }
        }
    }
    return score;
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
    function scoreOfParentheses($s) {
        $score = 0;
        $depth = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            if ($s[$i] == '(') {
                $depth++;
            } else {
                $depth--;
                if ($i > 0 && $s[$i - 1] == '(') {
                    $score += (1 << $depth);
                }
            }
        }
        return $score;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func scoreOfParentheses(_ s: String) -> Int {
        var score = 0
        var depth = 0
        let chars = Array(s)
        for i in 0..<chars.count {
            if chars[i] == "(" {
                depth += 1
            } else {
                depth -= 1
                if i > 0 && chars[i-1] == "(" {
                    score += (1 << depth)
                }
            }
        }
        return score
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun scoreOfParentheses(s: String): Int {
        var ans = 0
        var depth = 0
        for (i in s.indices) {
            if (s[i] == '(') {
                depth++
            } else {
                depth--
                if (i > 0 && s[i - 1] == '(') {
                    ans += 1 shl depth
                }
            }
        }
        return ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int scoreOfParentheses(String s) {
    int ans = 0;
    int depth = 0;
    for (int i = 0; i < s.length; i++) {
      if (s[i] == '(') {
        depth++;
      } else {
        depth--;
        if (i > 0 && s[i - 1] == '(') {
          ans += 1 << depth;
        }
      }
    }
    return ans;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func scoreOfParentheses(s string) int {
    ans := 0
    depth := 0
    for i := 0; i < len(s); i++ {
        if s[i] == '(' {
            depth++
        } else {
            depth--
            if i > 0 && s[i-1] == '(' {
                ans += 1 << depth
            }
        }
    }
    return ans
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @return {Integer}
def score_of_parentheses(s)
    ans = 0
    depth = 0
    s.chars.each_with_index do |char, i|
        if char == '('
            depth += 1
        else
            depth -= 1
            if i > 0 && s[i-1] == '('
                ans += 1 << depth
            end
        end
    end
    ans
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def scoreOfParentheses(s: String): Int = {
        var ans = 0
        var depth = 0
        for (i <- 0 until s.length) {
            if (s(i) == '(') {
                depth += 1
            } else {
                depth -= 1
                if (i > 0 && s(i - 1) == '(') {
                    ans += (1 << depth)
                }
            }
        }
        ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn score_of_parentheses(s: String) -> i32 {
        let mut ans = 0;
        let mut depth = 0;
        let bytes = s.as_bytes();
        for i in 0..bytes.len() {
            if bytes[i] == b'(' {
                depth += 1;
            } else {
                depth -= 1;
                if i > 0 && bytes[i - 1] == b'(' {
                    ans += 1 << depth;
                }
            }
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
(define/contract (score-of-parentheses s)
  (-> string? exact-integer?)
  (let ([chars (string->list s)])
    (let loop ([lst chars] [depth 0] [prev #f] [ans 0])
      (if (null? lst)
          ans
          (let ([curr (car lst)])
            (if (char=? curr #\()
                (loop (cdr lst) (+ depth 1) #\( ans)
                (let ([new-ans (if (and prev (char=? prev #\()))
                                   (+ ans (expt 2 (- depth 1)))
                                   ans)])
                  (loop (cdr lst) (- depth 1) #\) new-ans))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec score_of_parentheses(S :: unicode:unicode_binary()) -> integer().
score_of_parentheses(S) ->
  solve(binary_to_list(S), 0, undefined, 0).

solve([], _Depth, _Prev, Ans) ->
  Ans;
solve([$( | Rest], Depth, _Prev, Ans) ->
  solve(Rest, Depth + 1, $(, Ans);
solve([$) | Rest], Depth, Prev, Ans) ->
  NewAns = if
    Prev =:= $( -> Ans + (1 bsl (Depth - 1));
    true -> Ans
  end,
  solve(Rest, Depth - 1, $), NewAns).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec score_of_parentheses(s :: String.t) :: integer
  def score_of_parentheses(s) do
    {ans, _, _} = Enum.reduce(String.to_charlist(s), {0, 0, nil}, fn char, {ans, depth, prev} ->
      case char do
        ?( -> {ans, depth + 1, ?(}
        ?) ->
          new_ans = if prev == ?( do
            ans + round(:math.pow(2, depth - 1))
          else
            ans
          end
          {new_ans, depth - 1, ?)}
      end
    end)
    ans
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the string. The algorithm performs a single linear scan of the input string, performing constant-time operations at each step.
- **Space Complexity:** O(1) as we only maintain two integer variables, one for the current nesting depth and one for the cumulative score, regardless of the input size.
