---
layout: post
title: "Number of Steps to Reduce a Number in Binary Representation to One"
date: 2026-02-26 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Bit Manipulation", "Simulation"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int numSteps(string s) {\n        int steps\
        \ = 0;\n        int carry = 0;\n        for (int i = s.size() - 1; i > 0; --i)\
        \ {\n            if ((s[i] - '0') + carry == 1) {\n                steps +=\
        \ 2;\n                carry = 1;\n            } else {\n                steps\
        \ += 1;\n            }\n        }\n        return steps + carry;\n    }\n};"
      java: "class Solution {\n    public int numSteps(String s) {\n        int steps\
        \ = 0;\n        int carry = 0;\n        for (int i = s.length() - 1; i > 0;\
        \ i--) {\n            if ((s.charAt(i) - '0') + carry == 1) {\n            \
        \    steps += 2;\n                carry = 1;\n            } else {\n       \
        \         steps += 1;\n            }\n        }\n        return steps + carry;\n\
        \    }\n}"
      python: "class Solution(object):\n    def numSteps(self, s):\n        \"\"\"\n\
        \        :type s: str\n        :rtype: int\n        \"\"\"\n        steps =\
        \ 0\n        carry = 0\n        for i in range(len(s) - 1, 0, -1):\n       \
        \     if int(s[i]) + carry == 1:\n                steps += 2\n             \
        \   carry = 1\n            else:\n                steps += 1\n        return\
        \ steps + carry"
      python3: "class Solution:\n    def numSteps(self, s: str) -> int:\n        steps\
        \ = 0\n        carry = 0\n        for i in range(len(s) - 1, 0, -1):\n     \
        \       if int(s[i]) + carry == 1:\n                steps += 2\n           \
        \     carry = 1\n            else:\n                steps += 1\n        return\
        \ steps + carry"
      c: "int numSteps(char* s) {\n    int steps = 0;\n    int carry = 0;\n    int n\
        \ = strlen(s);\n    for (int i = n - 1; i > 0; i--) {\n        if ((s[i] - '0')\
        \ + carry == 1) {\n            steps += 2;\n            carry = 1;\n       \
        \ } else {\n            steps += 1;\n        }\n    }\n    return steps + carry;\n\
        }"
      csharp: "public class Solution {\n    public int NumSteps(string s) {\n      \
        \  int steps = 0;\n        int carry = 0;\n        for (int i = s.Length - 1;\
        \ i > 0; i--) {\n            if ((s[i] - '0') + carry == 1) {\n            \
        \    steps += 2;\n                carry = 1;\n            } else {\n       \
        \         steps += 1;\n            }\n        }\n        return steps + carry;\n\
        \    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {number}\n */\nvar numSteps\
        \ = function(s) {\n    let steps = 0;\n    let carry = 0;\n    for (let i =\
        \ s.length - 1; i > 0; i--) {\n        if (parseInt(s[i]) + carry === 1) {\n\
        \            steps += 2;\n            carry = 1;\n        } else {\n       \
        \     steps += 1;\n        }\n    }\n    return steps + carry;\n};"
      typescript: "function numSteps(s: string): number {\n    let steps = 0;\n    let\
        \ carry = 0;\n    for (let i = s.length - 1; i > 0; i--) {\n        const digit\
        \ = s[i] === '1' ? 1 : 0;\n        if (digit + carry === 1) {\n            steps\
        \ += 2;\n            carry = 1;\n        } else {\n            steps += 1;\n\
        \        }\n    }\n    return steps + carry;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return Integer\n\
        \     */\n    function numSteps($s) {\n        $steps = 0;\n        $carry =\
        \ 0;\n        $n = strlen($s);\n        for ($i = $n - 1; $i > 0; $i--) {\n\
        \            $digit = $s[$i] === '1' ? 1 : 0;\n            if ($digit + $carry\
        \ == 1) {\n                $steps += 2;\n                $carry = 1;\n     \
        \       } else {\n                $steps += 1;\n            }\n        }\n \
        \       return $steps + $carry;\n    }\n}"
      swift: "class Solution {\n    func numSteps(_ s: String) -> Int {\n        var\
        \ steps = 0\n        var carry = 0\n        let chars = Array(s)\n        let\
        \ n = chars.count\n        for i in stride(from: n - 1, to: 0, by: -1) {\n \
        \           let digit = chars[i] == \"1\" ? 1 : 0\n            if digit + carry\
        \ == 1 {\n                steps += 2\n                carry = 1\n          \
        \  } else {\n                steps += 1\n            }\n        }\n        return\
        \ steps + carry\n    }\n}"
      kotlin: "class Solution {\n    fun numSteps(s: String): Int {\n        var steps\
        \ = 0\n        var carry = 0\n        for (i in s.length - 1 downTo 1) {\n \
        \           val digit = if (s[i] == '1') 1 else 0\n            if (digit + carry\
        \ == 1) {\n                steps += 2\n                carry = 1\n         \
        \   } else {\n                steps += 1\n            }\n        }\n       \
        \ return steps + carry\n    }\n}"
      dart: "class Solution {\n  int numSteps(String s) {\n    int steps = 0;\n    int\
        \ carry = 0;\n    for (int i = s.length - 1; i > 0; i--) {\n      int digit\
        \ = s[i] == '1' ? 1 : 0;\n      if (digit + carry == 1) {\n        steps +=\
        \ 2;\n        carry = 1;\n      } else {\n        steps += 1;\n      }\n   \
        \ }\n    return steps + carry;\n  }\n}"
      go: "func numSteps(s string) int {\n    steps := 0\n    carry := 0\n    for i\
        \ := len(s) - 1; i > 0; i-- {\n        digit := 0\n        if s[i] == '1' {\n\
        \            digit = 1\n        }\n        if digit + carry == 1 {\n       \
        \     steps += 2\n            carry = 1\n        } else {\n            steps\
        \ += 1\n        }\n    }\n    return steps + carry\n}"
      ruby: "# @param {String} s\n# @return {Integer}\ndef num_steps(s)\n  steps = 0\n\
        \  carry = 0\n  (s.length - 1).downto(1) do |i|\n    digit = s[i] == '1' ? 1\
        \ : 0\n    if digit + carry == 1\n      steps += 2\n      carry = 1\n    elsif\
        \ digit + carry == 2\n      steps += 1\n      carry = 1\n    else\n      steps\
        \ += 1\n      carry = 0\n    end\n  end\n  steps + carry\nend"
      scala: "object Solution {\n    def numSteps(s: String): Int = {\n        var steps\
        \ = 0\n        var carry = 0\n        for (i <- s.length - 1 until 0 by -1)\
        \ {\n            val digit = if (s(i) == '1') 1 else 0\n            val sum\
        \ = digit + carry\n            if (sum == 1) {\n                steps += 2\n\
        \                carry = 1\n            } else if (sum == 2) {\n           \
        \     steps += 1\n                carry = 1\n            } else {\n        \
        \        steps += 1\n                carry = 0\n            }\n        }\n \
        \       steps + carry\n    }\n}"
      rust: "impl Solution {\n    pub fn num_steps(s: String) -> i32 {\n        let\
        \ mut steps = 0;\n        let mut carry = 0;\n        let bytes = s.as_bytes();\n\
        \        for i in (1..bytes.len()).rev() {\n            let digit = (bytes[i]\
        \ - b'0') as i32;\n            match digit + carry {\n                1 => {\n\
        \                    steps += 2;\n                    carry = 1;\n         \
        \       }\n                2 => {\n                    steps += 1;\n       \
        \             carry = 1;\n                }\n                _ => {\n      \
        \              steps += 1;\n                    carry = 0;\n               \
        \ }\n            }\n        }\n        steps + carry\n    }\n}"
      racket: "(define/contract (num-steps s)\n  (-> string? exact-integer?)\n  (let\
        \ ([n (string-length s)])\n    (let loop ([i (- n 1)] [carry 0] [steps 0])\n\
        \      (if (<= i 0)\n          (+ steps carry)\n          (let* ([digit (if\
        \ (char=? (string-ref s i) #\\1) 1 0)]\n                 [val (+ digit carry)])\n\
        \            (cond\n              [(= val 1) (loop (- i 1) 1 (+ steps 2))]\n\
        \              [(= val 2) (loop (- i 1) 1 (+ steps 1))]\n              [else\
        \      (loop (- i 1) 0 (+ steps 1))]))))))"
      erlang: "-spec num_steps(S :: unicode:unicode_binary()) -> integer().\nnum_steps(S)\
        \ ->\n  L = binary_to_list(S),\n  case L of\n    [_] -> 0;\n    [_ | Rest] ->\n\
        \      ToProcess = lists:reverse(Rest),\n      num_steps_process(ToProcess,\
        \ 0, 0)\n  end.\n\nnum_steps_process([], Carry, Steps) ->\n  Steps + Carry;\n\
        num_steps_process([Char | Rest], Carry, Steps) ->\n  Digit = Char - $0,\n  case\
        \ Digit + Carry of\n    1 -> num_steps_process(Rest, 1, Steps + 2);\n    2 ->\
        \ num_steps_process(Rest, 1, Steps + 1);\n    0 -> num_steps_process(Rest, 0,\
        \ Steps + 1)\n  end."
      elixir: "defmodule Solution do\n  @spec num_steps(s :: String.t) :: integer\n\
        \  def num_steps(s) do\n    chars = String.to_charlist(s)\n    case chars do\n\
        \      [_] -> 0\n      [_first | rest] ->\n        {steps, carry} = Enum.reduce(Enum.reverse(rest),\
        \ {0, 0}, fn char, {steps, carry} ->\n          digit = char - ?0\n        \
        \  case digit + carry do\n            1 -> {steps + 2, 1}\n            2 ->\
        \ {steps + 1, 1}\n            0 -> {steps + 1, 0}\n          end\n        end)\n\
        \        steps + carry\n    end\n  end\nend"
    approach: 'To solve this problem efficiently, we process the binary string from
      right to left, simulating the operations while maintaining a carry. If the current
      bit plus the carry results in an odd number, we must add 1 to make it even, which
      requires two steps: one addition and one division by 2. If the current bit plus
      the carry is even, we only need a single step for division. This right-to-left
      approach avoids manual string manipulation or large number conversions.


      We iterate from the last character up to (but not including) the first character.
      During each iteration, if the current bit combined with the carry is 1 (representing
      an odd state), we increment the step count by 2 and set the carry to 1. If the
      combination is 0 or 2 (representing an even state), we increment the step count
      by 1 (the carry remains 1 if it was already 1 from a previous odd state, otherwise
      it stays 0). Finally, we add the carry to the total steps to account for the very
      first bit becoming a 2 (requiring one last division) or staying as a 1 (requiring
      no more steps).'
    time_complexity: O(N) where N is the length of the string s. We perform a single
      pass from the end of the string to the beginning, doing constant time operations
      at each step.
    space_complexity: O(1) as we only use a few integer variables (steps, carry, and
      index) to store the state, regardless of the input size.
    elapsed_time: 152.54748129844666
    model: gemini-3-flash-preview
    generated_at: '2026-02-26 01:25:28 '
---

## Problem #1404: Number of Steps to Reduce a Number in Binary Representation to One

**Difficulty:** Medium

**Topics:** String, Bit Manipulation, Simulation

## Problem Description

<p>Given the binary representation of an integer as a string <code>s</code>, return <em>the number of steps to reduce it to </em><code>1</code><em> under the following rules</em>:</p>

<ul>
	<li>
	<p>If the current number is even, you have to divide it by <code>2</code>.</p>
	</li>
	<li>
	<p>If the current number is odd, you have to add <code>1</code> to it.</p>
	</li>
</ul>

<p>It is guaranteed that you can always reach one for all test cases.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;1101&quot;
<strong>Output:</strong> 6
<strong>Explanation:</strong> &quot;1101&quot; corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14.&nbsp;
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.&nbsp; 
Step 5) 4 is even, divide by 2 and obtain 2.&nbsp;
Step 6) 2 is even, divide by 2 and obtain 1.&nbsp; 
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;10&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> &quot;10&quot; corresponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.&nbsp; 
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;1&quot;
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length&nbsp;&lt;= 500</code></li>
	<li><code>s</code> consists of characters &#39;0&#39; or &#39;1&#39;</li>
	<li><code>s[0] == &#39;1&#39;</code></li>
</ul>


## Hints

1. Read the string from right to left, if the string ends in '0' then the number is even otherwise it is odd.

2. Simulate the steps described in the binary string.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To solve this problem efficiently, we process the binary string from right to left, simulating the operations while maintaining a carry. If the current bit plus the carry results in an odd number, we must add 1 to make it even, which requires two steps: one addition and one division by 2. If the current bit plus the carry is even, we only need a single step for division. This right-to-left approach avoids manual string manipulation or large number conversions.

We iterate from the last character up to (but not including) the first character. During each iteration, if the current bit combined with the carry is 1 (representing an odd state), we increment the step count by 2 and set the carry to 1. If the combination is 0 or 2 (representing an even state), we increment the step count by 1 (the carry remains 1 if it was already 1 from a previous odd state, otherwise it stays 0). Finally, we add the carry to the total steps to account for the very first bit becoming a 2 (requiring one last division) or staying as a 1 (requiring no more steps).

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
    int numSteps(string s) {
        int steps = 0;
        int carry = 0;
        for (int i = s.size() - 1; i > 0; --i) {
            if ((s[i] - '0') + carry == 1) {
                steps += 2;
                carry = 1;
            } else {
                steps += 1;
            }
        }
        return steps + carry;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int numSteps(String s) {
        int steps = 0;
        int carry = 0;
        for (int i = s.length() - 1; i > 0; i--) {
            if ((s.charAt(i) - '0') + carry == 1) {
                steps += 2;
                carry = 1;
            } else {
                steps += 1;
            }
        }
        return steps + carry;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        steps = 0
        carry = 0
        for i in range(len(s) - 1, 0, -1):
            if int(s[i]) + carry == 1:
                steps += 2
                carry = 1
            else:
                steps += 1
        return steps + carry
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        for i in range(len(s) - 1, 0, -1):
            if int(s[i]) + carry == 1:
                steps += 2
                carry = 1
            else:
                steps += 1
        return steps + carry
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int numSteps(char* s) {
    int steps = 0;
    int carry = 0;
    int n = strlen(s);
    for (int i = n - 1; i > 0; i--) {
        if ((s[i] - '0') + carry == 1) {
            steps += 2;
            carry = 1;
        } else {
            steps += 1;
        }
    }
    return steps + carry;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int NumSteps(string s) {
        int steps = 0;
        int carry = 0;
        for (int i = s.Length - 1; i > 0; i--) {
            if ((s[i] - '0') + carry == 1) {
                steps += 2;
                carry = 1;
            } else {
                steps += 1;
            }
        }
        return steps + carry;
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
var numSteps = function(s) {
    let steps = 0;
    let carry = 0;
    for (let i = s.length - 1; i > 0; i--) {
        if (parseInt(s[i]) + carry === 1) {
            steps += 2;
            carry = 1;
        } else {
            steps += 1;
        }
    }
    return steps + carry;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function numSteps(s: string): number {
    let steps = 0;
    let carry = 0;
    for (let i = s.length - 1; i > 0; i--) {
        const digit = s[i] === '1' ? 1 : 0;
        if (digit + carry === 1) {
            steps += 2;
            carry = 1;
        } else {
            steps += 1;
        }
    }
    return steps + carry;
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
    function numSteps($s) {
        $steps = 0;
        $carry = 0;
        $n = strlen($s);
        for ($i = $n - 1; $i > 0; $i--) {
            $digit = $s[$i] === '1' ? 1 : 0;
            if ($digit + $carry == 1) {
                $steps += 2;
                $carry = 1;
            } else {
                $steps += 1;
            }
        }
        return $steps + $carry;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func numSteps(_ s: String) -> Int {
        var steps = 0
        var carry = 0
        let chars = Array(s)
        let n = chars.count
        for i in stride(from: n - 1, to: 0, by: -1) {
            let digit = chars[i] == "1" ? 1 : 0
            if digit + carry == 1 {
                steps += 2
                carry = 1
            } else {
                steps += 1
            }
        }
        return steps + carry
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun numSteps(s: String): Int {
        var steps = 0
        var carry = 0
        for (i in s.length - 1 downTo 1) {
            val digit = if (s[i] == '1') 1 else 0
            if (digit + carry == 1) {
                steps += 2
                carry = 1
            } else {
                steps += 1
            }
        }
        return steps + carry
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int numSteps(String s) {
    int steps = 0;
    int carry = 0;
    for (int i = s.length - 1; i > 0; i--) {
      int digit = s[i] == '1' ? 1 : 0;
      if (digit + carry == 1) {
        steps += 2;
        carry = 1;
      } else {
        steps += 1;
      }
    }
    return steps + carry;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func numSteps(s string) int {
    steps := 0
    carry := 0
    for i := len(s) - 1; i > 0; i-- {
        digit := 0
        if s[i] == '1' {
            digit = 1
        }
        if digit + carry == 1 {
            steps += 2
            carry = 1
        } else {
            steps += 1
        }
    }
    return steps + carry
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @return {Integer}
def num_steps(s)
  steps = 0
  carry = 0
  (s.length - 1).downto(1) do |i|
    digit = s[i] == '1' ? 1 : 0
    if digit + carry == 1
      steps += 2
      carry = 1
    elsif digit + carry == 2
      steps += 1
      carry = 1
    else
      steps += 1
      carry = 0
    end
  end
  steps + carry
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def numSteps(s: String): Int = {
        var steps = 0
        var carry = 0
        for (i <- s.length - 1 until 0 by -1) {
            val digit = if (s(i) == '1') 1 else 0
            val sum = digit + carry
            if (sum == 1) {
                steps += 2
                carry = 1
            } else if (sum == 2) {
                steps += 1
                carry = 1
            } else {
                steps += 1
                carry = 0
            }
        }
        steps + carry
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn num_steps(s: String) -> i32 {
        let mut steps = 0;
        let mut carry = 0;
        let bytes = s.as_bytes();
        for i in (1..bytes.len()).rev() {
            let digit = (bytes[i] - b'0') as i32;
            match digit + carry {
                1 => {
                    steps += 2;
                    carry = 1;
                }
                2 => {
                    steps += 1;
                    carry = 1;
                }
                _ => {
                    steps += 1;
                    carry = 0;
                }
            }
        }
        steps + carry
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (num-steps s)
  (-> string? exact-integer?)
  (let ([n (string-length s)])
    (let loop ([i (- n 1)] [carry 0] [steps 0])
      (if (<= i 0)
          (+ steps carry)
          (let* ([digit (if (char=? (string-ref s i) #\1) 1 0)]
                 [val (+ digit carry)])
            (cond
              [(= val 1) (loop (- i 1) 1 (+ steps 2))]
              [(= val 2) (loop (- i 1) 1 (+ steps 1))]
              [else      (loop (- i 1) 0 (+ steps 1))]))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec num_steps(S :: unicode:unicode_binary()) -> integer().
num_steps(S) ->
  L = binary_to_list(S),
  case L of
    [_] -> 0;
    [_ | Rest] ->
      ToProcess = lists:reverse(Rest),
      num_steps_process(ToProcess, 0, 0)
  end.

num_steps_process([], Carry, Steps) ->
  Steps + Carry;
num_steps_process([Char | Rest], Carry, Steps) ->
  Digit = Char - $0,
  case Digit + Carry of
    1 -> num_steps_process(Rest, 1, Steps + 2);
    2 -> num_steps_process(Rest, 1, Steps + 1);
    0 -> num_steps_process(Rest, 0, Steps + 1)
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec num_steps(s :: String.t) :: integer
  def num_steps(s) do
    chars = String.to_charlist(s)
    case chars do
      [_] -> 0
      [_first | rest] ->
        {steps, carry} = Enum.reduce(Enum.reverse(rest), {0, 0}, fn char, {steps, carry} ->
          digit = char - ?0
          case digit + carry do
            1 -> {steps + 2, 1}
            2 -> {steps + 1, 1}
            0 -> {steps + 1, 0}
          end
        end)
        steps + carry
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) where N is the length of the string s. We perform a single pass from the end of the string to the beginning, doing constant time operations at each step.
- **Space Complexity:** O(1) as we only use a few integer variables (steps, carry, and index) to store the state, regardless of the input size.
