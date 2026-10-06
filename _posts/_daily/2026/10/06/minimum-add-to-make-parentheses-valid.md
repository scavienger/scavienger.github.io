---
layout: post
title: "Minimum Add to Make Parentheses Valid"
date: 2026-10-06 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Stack", "Greedy", "Bracket Sequences"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minAddToMakeValid(string s) {\n     \
        \   int additions = 0;\n        int balance = 0;\n        for (char c : s) {\n\
        \            if (c == '(') {\n                balance++;\n            } else\
        \ {\n                if (balance > 0) {\n                    balance--;\n  \
        \              } else {\n                    additions++;\n                }\n\
        \            }\n        }\n        return additions + balance;\n    }\n};"
      java: "class Solution {\n    public int minAddToMakeValid(String s) {\n      \
        \  int additions = 0;\n        int balance = 0;\n        for (int i = 0; i <\
        \ s.length(); i++) {\n            char c = s.charAt(i);\n            if (c ==\
        \ '(') {\n                balance++;\n            } else {\n               \
        \ if (balance > 0) {\n                    balance--;\n                } else\
        \ {\n                    additions++;\n                }\n            }\n  \
        \      }\n        return additions + balance;\n    }\n}"
      python: "class Solution(object):\n    def minAddToMakeValid(self, s):\n      \
        \  \"\"\"\n        :type s: str\n        :rtype: int\n        \"\"\"\n     \
        \   additions = 0\n        balance = 0\n        for char in s:\n           \
        \ if char == '(':\n                balance += 1\n            else:\n       \
        \         if balance > 0:\n                    balance -= 1\n              \
        \  else:\n                    additions += 1\n        return additions + balance"
      python3: "class Solution:\n    def minAddToMakeValid(self, s: str) -> int:\n \
        \       additions = 0\n        balance = 0\n        for char in s:\n       \
        \     if char == '(':\n                balance += 1\n            else:\n   \
        \             if balance > 0:\n                    balance -= 1\n          \
        \      else:\n                    additions += 1\n        return additions +\
        \ balance"
      c: "int minAddToMakeValid(char* s) {\n    int additions = 0;\n    int balance\
        \ = 0;\n    int i = 0;\n    while (s[i] != '\\0') {\n        if (s[i] == '(')\
        \ {\n            balance++;\n        } else {\n            if (balance > 0)\
        \ {\n                balance--;\n            } else {\n                additions++;\n\
        \            }\n        }\n        i++;\n    }\n    return additions + balance;\n\
        }"
      csharp: "public class Solution {\n    public int MinAddToMakeValid(string s) {\n\
        \        int openNeeded = 0;\n        int closeNeeded = 0;\n        foreach\
        \ (char c in s) {\n            if (c == '(') {\n                openNeeded++;\n\
        \            } else {\n                if (openNeeded > 0) {\n             \
        \       openNeeded--;\n                } else {\n                    closeNeeded++;\n\
        \                }\n            }\n        }\n        return openNeeded + closeNeeded;\n\
        \    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {number}\n */\nvar minAddToMakeValid\
        \ = function(s) {\n    let openNeeded = 0;\n    let closeNeeded = 0;\n    for\
        \ (let i = 0; i < s.length; i++) {\n        if (s[i] === '(') {\n          \
        \  openNeeded++;\n        } else {\n            if (openNeeded > 0) {\n    \
        \            openNeeded--;\n            } else {\n                closeNeeded++;\n\
        \            }\n        }\n    }\n    return openNeeded + closeNeeded;\n};"
      typescript: "function minAddToMakeValid(s: string): number {\n    let openNeeded\
        \ = 0;\n    let closeNeeded = 0;\n    for (let i = 0; i < s.length; i++) {\n\
        \        if (s[i] === '(') {\n            openNeeded++;\n        } else {\n\
        \            if (openNeeded > 0) {\n                openNeeded--;\n        \
        \    } else {\n                closeNeeded++;\n            }\n        }\n  \
        \  }\n    return openNeeded + closeNeeded;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return Integer\n\
        \     */\n    function minAddToMakeValid($s) {\n        $openNeeded = 0;\n \
        \       $closeNeeded = 0;\n        $len = strlen($s);\n        for ($i = 0;\
        \ $i < $len; $i++) {\n            if ($s[$i] === '(') {\n                $openNeeded++;\n\
        \            } else {\n                if ($openNeeded > 0) {\n            \
        \        $openNeeded--;\n                } else {\n                    $closeNeeded++;\n\
        \                }\n            }\n        }\n        return $openNeeded + $closeNeeded;\n\
        \    }\n}"
      swift: "class Solution {\n    func minAddToMakeValid(_ s: String) -> Int {\n \
        \       var openNeeded = 0\n        var closeNeeded = 0\n        for char in\
        \ s {\n            if char == \"(\" {\n                openNeeded += 1\n   \
        \         } else {\n                if openNeeded > 0 {\n                  \
        \  openNeeded -= 1\n                } else {\n                    closeNeeded\
        \ += 1\n                }\n            }\n        }\n        return openNeeded\
        \ + closeNeeded\n    }\n}"
      kotlin: "class Solution {\n    fun minAddToMakeValid(s: String): Int {\n     \
        \   var open = 0\n        var moves = 0\n        for (char in s) {\n       \
        \     if (char == '(') {\n                open++\n            } else {\n   \
        \             if (open > 0) {\n                    open--\n                }\
        \ else {\n                    moves++\n                }\n            }\n  \
        \      }\n        return open + moves\n    }\n}"
      dart: "class Solution {\n  int minAddToMakeValid(String s) {\n    int openCount\
        \ = 0;\n    int moves = 0;\n    for (int i = 0; i < s.length; i++) {\n     \
        \ if (s[i] == '(') {\n        openCount++;\n      } else {\n        if (openCount\
        \ > 0) {\n          openCount--;\n        } else {\n          moves++;\n   \
        \     }\n      }\n    }\n    return openCount + moves;\n  }\n}"
      go: "func minAddToMakeValid(s string) int {\n    open := 0\n    moves := 0\n \
        \   for _, char := range s {\n        if char == '(' {\n            open++\n\
        \        } else {\n            if open > 0 {\n                open--\n     \
        \       } else {\n                moves++\n            }\n        }\n    }\n\
        \    return open + moves\n}"
      ruby: "# @param {String} s\n# @param {Integer}\ndef min_add_to_make_valid(s)\n\
        \  open_count = 0\n  moves = 0\n  s.each_char do |char|\n    if char == '('\n\
        \      open_count += 1\n    else\n      if open_count > 0\n        open_count\
        \ -= 1\n      else\n        moves += 1\n      end\n    end\n  end\n  open_count\
        \ + moves\nend"
      scala: "object Solution {\n    def minAddToMakeValid(s: String): Int = {\n   \
        \     var open = 0\n        var moves = 0\n        for (char <- s) {\n     \
        \       if (char == '(') {\n                open += 1\n            } else {\n\
        \                if (open > 0) {\n                    open -= 1\n          \
        \      } else {\n                    moves += 1\n                }\n       \
        \     }\n        }\n        open + moves\n    }\n}"
      rust: "impl Solution {\n    pub fn min_add_to_make_valid(s: String) -> i32 {\n\
        \        let mut open_needed = 0;\n        let mut close_needed = 0;\n     \
        \   for c in s.chars() {\n            if c == '(' {\n                open_needed\
        \ += 1;\n            } else if c == ')' {\n                if open_needed >\
        \ 0 {\n                    open_needed -= 1;\n                } else {\n   \
        \                 close_needed += 1;\n                }\n            }\n   \
        \     }\n        open_needed + close_needed\n    }\n}"
      racket: "(define/contract (min-add-to-make-valid s)\n  (-> string? exact-integer?)\n\
        \  (let loop ([chars (string->list s)]\n             [open-needed 0]\n     \
        \        [close-needed 0])\n    (if (empty? chars)\n        (+ open-needed close-needed)\n\
        \        (let ([c (car chars)]\n              [rest (cdr chars)])\n        \
        \  (cond\n            [(char=? c #\\() (loop rest (+ open-needed 1) close-needed)]\n\
        \            [(char=? c #\\)) \n             (if (> open-needed 0)\n       \
        \          (loop rest (- open-needed 1) close-needed)\n                 (loop\
        \ rest open-needed (+ close-needed 1)))])))))"
      erlang: "-spec min_add_to_make_valid(S :: unicode:unicode_binary()) -> integer().\n\
        min_add_to_make_valid(S) ->\n  solve(binary_to_list(S), 0, 0).\n\nsolve([],\
        \ Open, Close) ->\n  Open + Close;\nsolve([$( | T], Open, Close) ->\n  solve(T,\
        \ Open + 1, Close);\nsolve([$) | T], Open, Close) ->\n  if\n    Open > 0 ->\
        \ solve(T, Open - 1, Close);\n    true -> solve(T, Open, Close + 1)\n  end."
      elixir: "defmodule Solution do\n  @spec min_add_to_make_valid(s :: String.t) ::\
        \ integer\n  def min_add_to_make_valid(s) do\n    s\n    |> String.graphemes()\n\
        \    |> Enum.reduce({0, 0}, fn char, {open_needed, close_needed} ->\n      case\
        \ char do\n        \"(\" ->\n          {open_needed + 1, close_needed}\n   \
        \     \")\" ->\n          if open_needed > 0 do\n            {open_needed -\
        \ 1, close_needed}\n          else\n            {open_needed, close_needed +\
        \ 1}\n          end\n      end\n    end)\n    |> (fn {o, c} -> o + c end).()\n\
        \  end\nend"
    approach: 'The algorithm processes the string linearly to track the balance of parentheses
      and the number of insertions needed for unmatched closing parentheses. We maintain
      two counters: one for the current ''balance'' of open parentheses that are waiting
      to be closed, and one for ''additions'' required for closing parentheses that
      do not have a preceding open parenthesis to pair with. As we iterate through the
      string, we increment the balance whenever we encounter ''(''. When we encounter
      '')'', we either decrement the balance if it is greater than zero (forming a valid
      pair) or increment the additions counter if the balance is zero (representing
      an unmatched closing bracket).


      After iterating through the entire string, the additions counter represents the
      number of open parentheses we must insert to satisfy unmatched closing parentheses.
      However, any remaining positive balance indicates open parentheses that were never
      closed; these also require an equal number of closing parentheses to be inserted
      at the end of the string. Therefore, the total minimum moves required is the sum
      of the additions counter and the remaining balance. This approach ensures we find
      the minimum number of insertions by greedily matching every possible pair as early
      as possible.'
    time_complexity: O(n) where n is the length of the string. We iterate through the
      characters of the string exactly once, performing constant-time arithmetic operations
      at each step.
    space_complexity: O(1) excluding the space used by the input string. We only maintain
      two integer variables (balance and additions) to keep track of the parentheses
      state, regardless of the input size.
    elapsed_time: 66.58001136779785
    model: gemini-3-flash-preview
    generated_at: '2026-10-06 04:08:54 '
---

## Problem #921: Minimum Add to Make Parentheses Valid

**Difficulty:** Medium

**Topics:** String, Stack, Greedy, Bracket Sequences

## Problem Description

<p>A parentheses string is valid if and only if:</p>

<ul>
	<li>It is the empty string,</li>
	<li>It can be written as <code>AB</code> (<code>A</code> concatenated with <code>B</code>), where <code>A</code> and <code>B</code> are valid strings, or</li>
	<li>It can be written as <code>(A)</code>, where <code>A</code> is a valid string.</li>
</ul>

<p>You are given a parentheses string <code>s</code>. In one move, you can insert a parenthesis at any position of the string.</p>

<ul>
	<li>For example, if <code>s = &quot;()))&quot;</code>, you can insert an opening parenthesis to be <code>&quot;(<strong>(</strong>)))&quot;</code> or a closing parenthesis to be <code>&quot;())<strong>)</strong>)&quot;</code>.</li>
</ul>

<p>Return <em>the minimum number of moves required to make </em><code>s</code><em> valid</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;())&quot;
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(((&quot;
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s[i]</code> is either <code>&#39;(&#39;</code> or <code>&#39;)&#39;</code>.</li>
</ul>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm processes the string linearly to track the balance of parentheses and the number of insertions needed for unmatched closing parentheses. We maintain two counters: one for the current 'balance' of open parentheses that are waiting to be closed, and one for 'additions' required for closing parentheses that do not have a preceding open parenthesis to pair with. As we iterate through the string, we increment the balance whenever we encounter '('. When we encounter ')', we either decrement the balance if it is greater than zero (forming a valid pair) or increment the additions counter if the balance is zero (representing an unmatched closing bracket).

After iterating through the entire string, the additions counter represents the number of open parentheses we must insert to satisfy unmatched closing parentheses. However, any remaining positive balance indicates open parentheses that were never closed; these also require an equal number of closing parentheses to be inserted at the end of the string. Therefore, the total minimum moves required is the sum of the additions counter and the remaining balance. This approach ensures we find the minimum number of insertions by greedily matching every possible pair as early as possible.

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
    int minAddToMakeValid(string s) {
        int additions = 0;
        int balance = 0;
        for (char c : s) {
            if (c == '(') {
                balance++;
            } else {
                if (balance > 0) {
                    balance--;
                } else {
                    additions++;
                }
            }
        }
        return additions + balance;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minAddToMakeValid(String s) {
        int additions = 0;
        int balance = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                balance++;
            } else {
                if (balance > 0) {
                    balance--;
                } else {
                    additions++;
                }
            }
        }
        return additions + balance;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        additions = 0
        balance = 0
        for char in s:
            if char == '(':
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    additions += 1
        return additions + balance
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        additions = 0
        balance = 0
        for char in s:
            if char == '(':
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    additions += 1
        return additions + balance
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int minAddToMakeValid(char* s) {
    int additions = 0;
    int balance = 0;
    int i = 0;
    while (s[i] != '\0') {
        if (s[i] == '(') {
            balance++;
        } else {
            if (balance > 0) {
                balance--;
            } else {
                additions++;
            }
        }
        i++;
    }
    return additions + balance;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinAddToMakeValid(string s) {
        int openNeeded = 0;
        int closeNeeded = 0;
        foreach (char c in s) {
            if (c == '(') {
                openNeeded++;
            } else {
                if (openNeeded > 0) {
                    openNeeded--;
                } else {
                    closeNeeded++;
                }
            }
        }
        return openNeeded + closeNeeded;
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
var minAddToMakeValid = function(s) {
    let openNeeded = 0;
    let closeNeeded = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '(') {
            openNeeded++;
        } else {
            if (openNeeded > 0) {
                openNeeded--;
            } else {
                closeNeeded++;
            }
        }
    }
    return openNeeded + closeNeeded;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minAddToMakeValid(s: string): number {
    let openNeeded = 0;
    let closeNeeded = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '(') {
            openNeeded++;
        } else {
            if (openNeeded > 0) {
                openNeeded--;
            } else {
                closeNeeded++;
            }
        }
    }
    return openNeeded + closeNeeded;
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
    function minAddToMakeValid($s) {
        $openNeeded = 0;
        $closeNeeded = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            if ($s[$i] === '(') {
                $openNeeded++;
            } else {
                if ($openNeeded > 0) {
                    $openNeeded--;
                } else {
                    $closeNeeded++;
                }
            }
        }
        return $openNeeded + $closeNeeded;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minAddToMakeValid(_ s: String) -> Int {
        var openNeeded = 0
        var closeNeeded = 0
        for char in s {
            if char == "(" {
                openNeeded += 1
            } else {
                if openNeeded > 0 {
                    openNeeded -= 1
                } else {
                    closeNeeded += 1
                }
            }
        }
        return openNeeded + closeNeeded
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minAddToMakeValid(s: String): Int {
        var open = 0
        var moves = 0
        for (char in s) {
            if (char == '(') {
                open++
            } else {
                if (open > 0) {
                    open--
                } else {
                    moves++
                }
            }
        }
        return open + moves
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minAddToMakeValid(String s) {
    int openCount = 0;
    int moves = 0;
    for (int i = 0; i < s.length; i++) {
      if (s[i] == '(') {
        openCount++;
      } else {
        if (openCount > 0) {
          openCount--;
        } else {
          moves++;
        }
      }
    }
    return openCount + moves;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minAddToMakeValid(s string) int {
    open := 0
    moves := 0
    for _, char := range s {
        if char == '(' {
            open++
        } else {
            if open > 0 {
                open--
            } else {
                moves++
            }
        }
    }
    return open + moves
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @param {Integer}
def min_add_to_make_valid(s)
  open_count = 0
  moves = 0
  s.each_char do |char|
    if char == '('
      open_count += 1
    else
      if open_count > 0
        open_count -= 1
      else
        moves += 1
      end
    end
  end
  open_count + moves
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minAddToMakeValid(s: String): Int = {
        var open = 0
        var moves = 0
        for (char <- s) {
            if (char == '(') {
                open += 1
            } else {
                if (open > 0) {
                    open -= 1
                } else {
                    moves += 1
                }
            }
        }
        open + moves
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_add_to_make_valid(s: String) -> i32 {
        let mut open_needed = 0;
        let mut close_needed = 0;
        for c in s.chars() {
            if c == '(' {
                open_needed += 1;
            } else if c == ')' {
                if open_needed > 0 {
                    open_needed -= 1;
                } else {
                    close_needed += 1;
                }
            }
        }
        open_needed + close_needed
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-add-to-make-valid s)
  (-> string? exact-integer?)
  (let loop ([chars (string->list s)]
             [open-needed 0]
             [close-needed 0])
    (if (empty? chars)
        (+ open-needed close-needed)
        (let ([c (car chars)]
              [rest (cdr chars)])
          (cond
            [(char=? c #\() (loop rest (+ open-needed 1) close-needed)]
            [(char=? c #\)) 
             (if (> open-needed 0)
                 (loop rest (- open-needed 1) close-needed)
                 (loop rest open-needed (+ close-needed 1)))])))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_add_to_make_valid(S :: unicode:unicode_binary()) -> integer().
min_add_to_make_valid(S) ->
  solve(binary_to_list(S), 0, 0).

solve([], Open, Close) ->
  Open + Close;
solve([$( | T], Open, Close) ->
  solve(T, Open + 1, Close);
solve([$) | T], Open, Close) ->
  if
    Open > 0 -> solve(T, Open - 1, Close);
    true -> solve(T, Open, Close + 1)
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_add_to_make_valid(s :: String.t) :: integer
  def min_add_to_make_valid(s) do
    s
    |> String.graphemes()
    |> Enum.reduce({0, 0}, fn char, {open_needed, close_needed} ->
      case char do
        "(" ->
          {open_needed + 1, close_needed}
        ")" ->
          if open_needed > 0 do
            {open_needed - 1, close_needed}
          else
            {open_needed, close_needed + 1}
          end
      end
    end)
    |> (fn {o, c} -> o + c end).()
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the string. We iterate through the characters of the string exactly once, performing constant-time arithmetic operations at each step.
- **Space Complexity:** O(1) excluding the space used by the input string. We only maintain two integer variables (balance and additions) to keep track of the parentheses state, regardless of the input size.
