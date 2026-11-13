---
layout: post
title: "Number of Substrings With Only 1s"
date: 2025-11-16 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Math", "String"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/number-of-substrings-with-only-1s/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int numSub(string s) {\n        const int\
        \ MOD = 1000000007;\n        long long run = 0;\n        long long answer =\
        \ 0;\n        for (char c : s) {\n            if (c == '1') {\n            \
        \    ++run;\n                answer = (answer + run) % MOD;\n            } else\
        \ {\n                run = 0;\n            }\n        }\n        return static_cast<int>(answer);\n\
        \    }\n};"
      java: "class Solution {\n    public int numSub(String s) {\n        final int\
        \ MOD = 1000000007;\n        long run = 0;\n        long answer = 0;\n     \
        \   for (int i = 0; i < s.length(); i++) {\n            if (s.charAt(i) == '1')\
        \ {\n                run++;\n                answer = (answer + run) % MOD;\n\
        \            } else {\n                run = 0;\n            }\n        }\n\
        \        return (int) answer;\n    }\n}"
      python: "class Solution(object):\n    def numSub(self, s):\n        \"\"\"\n \
        \       :type s: str\n        :rtype: int\n        \"\"\"\n        mod = 10**9\
        \ + 7\n        run = 0\n        answer = 0\n        for char in s:\n       \
        \     if char == '1':\n                run += 1\n                answer = (answer\
        \ + run) % mod\n            else:\n                run = 0\n        return answer"
      python3: "class Solution:\n    def numSub(self, s: str) -> int:\n        mod =\
        \ 10**9 + 7\n        run = 0\n        answer = 0\n        for char in s:\n \
        \           if char == '1':\n                run += 1\n                answer\
        \ = (answer + run) % mod\n            else:\n                run = 0\n     \
        \   return answer"
      c: "int numSub(char* s) {\n    const int MOD = 1000000007;\n    long long run\
        \ = 0;\n    long long answer = 0;\n    for (int i = 0; s[i] != '\\0'; i++) {\n\
        \        if (s[i] == '1') {\n            run++;\n            answer = (answer\
        \ + run) % MOD;\n        } else {\n            run = 0;\n        }\n    }\n\
        \    return (int) answer;\n}"
      csharp: "public class Solution {\n    public int NumSub(string s) {\n        const\
        \ long mod = 1000000007;\n        long run = 0;\n        long answer = 0;\n\
        \        foreach (char c in s) {\n            if (c == '1') {\n            \
        \    run++;\n                answer = (answer + run) % mod;\n            } else\
        \ {\n                run = 0;\n            }\n        }\n        return (int)answer;\n\
        \    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {number}\n */\nvar numSub =\
        \ function(s) {\n    const mod = 1000000007;\n    let run = 0;\n    let answer\
        \ = 0;\n    for (const char of s) {\n        if (char === '1') {\n         \
        \   run++;\n            answer = (answer + run) % mod;\n        } else {\n \
        \           run = 0;\n        }\n    }\n    return answer;\n};"
      typescript: "function numSub(s: string): number {\n    const mod = 1000000007;\n\
        \    let run = 0;\n    let answer = 0;\n    for (const char of s) {\n      \
        \  if (char === '1') {\n            run++;\n            answer = (answer + run)\
        \ % mod;\n        } else {\n            run = 0;\n        }\n    }\n    return\
        \ answer;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return Integer\n\
        \     */\n    function numSub($s) {\n        $mod = 1000000007;\n        $run\
        \ = 0;\n        $answer = 0;\n        $length = strlen($s);\n        for ($i\
        \ = 0; $i < $length; $i++) {\n            if ($s[$i] === '1') {\n          \
        \      $run++;\n                $answer = ($answer + $run) % $mod;\n       \
        \     } else {\n                $run = 0;\n            }\n        }\n      \
        \  return $answer;\n    }\n}"
      swift: "class Solution {\n    func numSub(_ s: String) -> Int {\n        let mod\
        \ = 1_000_000_007\n        var run = 0\n        var answer = 0\n        for\
        \ char in s {\n            if char == \"1\" {\n                run += 1\n  \
        \              answer = (answer + run) % mod\n            } else {\n       \
        \         run = 0\n            }\n        }\n        return answer\n    }\n}"
      kotlin: "class Solution {\n    fun numSub(s: String): Int {\n        val mod =\
        \ 1_000_000_007L\n        var run = 0L\n        var answer = 0L\n        for\
        \ (char in s) {\n            if (char == '1') {\n                run += 1\n\
        \                answer = (answer + run) % mod\n            } else {\n     \
        \           run = 0\n            }\n        }\n        return answer.toInt()\n\
        \    }\n}"
      dart: "class Solution {\n  int numSub(String s) {\n    const mod = 1000000007;\n\
        \    var run = 0;\n    var answer = 0;\n    for (var i = 0; i < s.length; i++)\
        \ {\n      if (s[i] == '1') {\n        run++;\n        answer = (answer + run)\
        \ % mod;\n      } else {\n        run = 0;\n      }\n    }\n    return answer;\n\
        \  }\n}"
      go: "func numSub(s string) int {\n    const mod = 1000000007\n    run := 0\n \
        \   answer := 0\n    for _, char := range s {\n        if char == '1' {\n  \
        \          run++\n            answer = (answer + run) % mod\n        } else\
        \ {\n            run = 0\n        }\n    }\n    return answer\n}"
      ruby: "# @param {String} s\n# @return {Integer}\ndef num_sub(s)\n    mod = 1_000_000_007\n\
        \    run = 0\n    answer = 0\n    s.each_char do |char|\n        if char ==\
        \ '1'\n            run += 1\n            answer = (answer + run) % mod\n   \
        \     else\n            run = 0\n        end\n    end\n    answer\nend"
      scala: "object Solution {\n    def numSub(s: String): Int = {\n        val mod\
        \ = 1000000007L\n        var run = 0L\n        var answer = 0L\n        for\
        \ (char <- s) {\n            if (char == '1') {\n                run += 1\n\
        \                answer = (answer + run) % mod\n            } else {\n     \
        \           run = 0\n            }\n        }\n        answer.toInt\n    }\n\
        }"
      rust: "impl Solution {\n    pub fn num_sub(s: String) -> i32 {\n        let modulo:\
        \ i64 = 1_000_000_007;\n        let mut run: i64 = 0;\n        let mut answer:\
        \ i64 = 0;\n\n        for byte in s.bytes() {\n            if byte == b'1' {\n\
        \                run += 1;\n                answer = (answer + run) % modulo;\n\
        \            } else {\n                run = 0;\n            }\n        }\n\n\
        \        answer as i32\n    }\n}"
      racket: "(define/contract (num-sub s)\n  (-> string? exact-integer?)\n  (define\
        \ mod (+ 1000000000 7))\n  (let loop ([index 0] [run 0] [answer 0])\n    (if\
        \ (= index (string-length s))\n        answer\n        (if (char=? (string-ref\
        \ s index) #\\1)\n            (let ([next-run (+ run 1)])\n              (loop\
        \ (+ index 1) next-run (modulo (+ answer next-run) mod)))\n            (loop\
        \ (+ index 1) 0 answer)))))"
      erlang: "-spec num_sub(S :: unicode:unicode_binary()) -> integer().\nnum_sub(S)\
        \ ->\n  num_sub_loop(binary_to_list(S), 0, 0).\n\nnum_sub_loop([], _Run, Answer)\
        \ ->\n  Answer;\nnum_sub_loop([$1 | Rest], Run, Answer) ->\n  NextRun = Run\
        \ + 1,\n  num_sub_loop(Rest, NextRun, (Answer + NextRun) rem 1000000007);\n\
        num_sub_loop([_ | Rest], _Run, Answer) ->\n  num_sub_loop(Rest, 0, Answer)."
      elixir: "defmodule Solution do\n  @spec num_sub(s :: String.t) :: integer\n  def\
        \ num_sub(s) do\n    modulo = 1_000_000_007\n\n    s\n    |> :binary.bin_to_list()\n\
        \    |> Enum.reduce({0, 0}, fn\n      ?1, {run, answer} ->\n        next_run\
        \ = run + 1\n        {next_run, rem(answer + next_run, modulo)}\n\n      _,\
        \ {_run, answer} ->\n        {0, answer}\n    end)\n    |> elem(1)\n  end\n\
        end"
    approach: 'Scan the string once while counting the length of the current consecutive
      run of ''1''s. When a ''1'' is encountered, extend the run and add its length
      to the answer, since that many all-1 substrings end at this position.


      When a ''0'' is encountered, reset the run length to zero. Keep the answer modulo
      10^9 + 7 throughout; this yields the sum of n(n + 1) / 2 contributions for every
      consecutive run of n ones.'
    time_complexity: O(n), where n is the length of the string, because each character
      is processed once.
    space_complexity: O(1), using only a few counters in addition to the input string.
    elapsed_time: 55.63084292411804
    model: gpt-6-luna
    generated_at: '2026-11-13 00:03:24 '
---

## Problem #1513: Number of Substrings With Only 1s

**Difficulty:** Medium

**Topics:** Math, String

## Problem Description

<p>Given a binary string <code>s</code>, return <em>the number of substrings with all characters</em> <code>1</code><em>&#39;s</em>. Since the answer may be too large, return it modulo <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;0110111&quot;
<strong>Output:</strong> 9
<strong>Explanation:</strong> There are 9 substring in total with only 1&#39;s characters.
&quot;1&quot; -&gt; 5 times.
&quot;11&quot; -&gt; 3 times.
&quot;111&quot; -&gt; 1 time.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;101&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> Substring &quot;1&quot; is shown 2 times in s.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;111111&quot;
<strong>Output:</strong> 21
<strong>Explanation:</strong> Each substring contains only 1&#39;s characters.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
</ul>


## Hints

1. Count number of 1s in each consecutive-1 group. For a group with n consecutive 1s, the total contribution of it to the final answer is (n + 1) * n // 2.

## 🤖 AI-Generated Solution (gpt-6-luna)

### Approach

Scan the string once while counting the length of the current consecutive run of '1's. When a '1' is encountered, extend the run and add its length to the answer, since that many all-1 substrings end at this position.

When a '0' is encountered, reset the run length to zero. Keep the answer modulo 10^9 + 7 throughout; this yields the sum of n(n + 1) / 2 contributions for every consecutive run of n ones.

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
    int numSub(string s) {
        const int MOD = 1000000007;
        long long run = 0;
        long long answer = 0;
        for (char c : s) {
            if (c == '1') {
                ++run;
                answer = (answer + run) % MOD;
            } else {
                run = 0;
            }
        }
        return static_cast<int>(answer);
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int numSub(String s) {
        final int MOD = 1000000007;
        long run = 0;
        long answer = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') {
                run++;
                answer = (answer + run) % MOD;
            } else {
                run = 0;
            }
        }
        return (int) answer;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        mod = 10**9 + 7
        run = 0
        answer = 0
        for char in s:
            if char == '1':
                run += 1
                answer = (answer + run) % mod
            else:
                run = 0
        return answer
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def numSub(self, s: str) -> int:
        mod = 10**9 + 7
        run = 0
        answer = 0
        for char in s:
            if char == '1':
                run += 1
                answer = (answer + run) % mod
            else:
                run = 0
        return answer
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int numSub(char* s) {
    const int MOD = 1000000007;
    long long run = 0;
    long long answer = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '1') {
            run++;
            answer = (answer + run) % MOD;
        } else {
            run = 0;
        }
    }
    return (int) answer;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int NumSub(string s) {
        const long mod = 1000000007;
        long run = 0;
        long answer = 0;
        foreach (char c in s) {
            if (c == '1') {
                run++;
                answer = (answer + run) % mod;
            } else {
                run = 0;
            }
        }
        return (int)answer;
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
var numSub = function(s) {
    const mod = 1000000007;
    let run = 0;
    let answer = 0;
    for (const char of s) {
        if (char === '1') {
            run++;
            answer = (answer + run) % mod;
        } else {
            run = 0;
        }
    }
    return answer;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function numSub(s: string): number {
    const mod = 1000000007;
    let run = 0;
    let answer = 0;
    for (const char of s) {
        if (char === '1') {
            run++;
            answer = (answer + run) % mod;
        } else {
            run = 0;
        }
    }
    return answer;
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
    function numSub($s) {
        $mod = 1000000007;
        $run = 0;
        $answer = 0;
        $length = strlen($s);
        for ($i = 0; $i < $length; $i++) {
            if ($s[$i] === '1') {
                $run++;
                $answer = ($answer + $run) % $mod;
            } else {
                $run = 0;
            }
        }
        return $answer;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func numSub(_ s: String) -> Int {
        let mod = 1_000_000_007
        var run = 0
        var answer = 0
        for char in s {
            if char == "1" {
                run += 1
                answer = (answer + run) % mod
            } else {
                run = 0
            }
        }
        return answer
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun numSub(s: String): Int {
        val mod = 1_000_000_007L
        var run = 0L
        var answer = 0L
        for (char in s) {
            if (char == '1') {
                run += 1
                answer = (answer + run) % mod
            } else {
                run = 0
            }
        }
        return answer.toInt()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int numSub(String s) {
    const mod = 1000000007;
    var run = 0;
    var answer = 0;
    for (var i = 0; i < s.length; i++) {
      if (s[i] == '1') {
        run++;
        answer = (answer + run) % mod;
      } else {
        run = 0;
      }
    }
    return answer;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func numSub(s string) int {
    const mod = 1000000007
    run := 0
    answer := 0
    for _, char := range s {
        if char == '1' {
            run++
            answer = (answer + run) % mod
        } else {
            run = 0
        }
    }
    return answer
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @return {Integer}
def num_sub(s)
    mod = 1_000_000_007
    run = 0
    answer = 0
    s.each_char do |char|
        if char == '1'
            run += 1
            answer = (answer + run) % mod
        else
            run = 0
        end
    end
    answer
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def numSub(s: String): Int = {
        val mod = 1000000007L
        var run = 0L
        var answer = 0L
        for (char <- s) {
            if (char == '1') {
                run += 1
                answer = (answer + run) % mod
            } else {
                run = 0
            }
        }
        answer.toInt
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn num_sub(s: String) -> i32 {
        let modulo: i64 = 1_000_000_007;
        let mut run: i64 = 0;
        let mut answer: i64 = 0;

        for byte in s.bytes() {
            if byte == b'1' {
                run += 1;
                answer = (answer + run) % modulo;
            } else {
                run = 0;
            }
        }

        answer as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (num-sub s)
  (-> string? exact-integer?)
  (define mod (+ 1000000000 7))
  (let loop ([index 0] [run 0] [answer 0])
    (if (= index (string-length s))
        answer
        (if (char=? (string-ref s index) #\1)
            (let ([next-run (+ run 1)])
              (loop (+ index 1) next-run (modulo (+ answer next-run) mod)))
            (loop (+ index 1) 0 answer)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec num_sub(S :: unicode:unicode_binary()) -> integer().
num_sub(S) ->
  num_sub_loop(binary_to_list(S), 0, 0).

num_sub_loop([], _Run, Answer) ->
  Answer;
num_sub_loop([$1 | Rest], Run, Answer) ->
  NextRun = Run + 1,
  num_sub_loop(Rest, NextRun, (Answer + NextRun) rem 1000000007);
num_sub_loop([_ | Rest], _Run, Answer) ->
  num_sub_loop(Rest, 0, Answer).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec num_sub(s :: String.t) :: integer
  def num_sub(s) do
    modulo = 1_000_000_007

    s
    |> :binary.bin_to_list()
    |> Enum.reduce({0, 0}, fn
      ?1, {run, answer} ->
        next_run = run + 1
        {next_run, rem(answer + next_run, modulo)}

      _, {_run, answer} ->
        {0, answer}
    end)
    |> elem(1)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n), where n is the length of the string, because each character is processed once.
- **Space Complexity:** O(1), using only a few counters in addition to the input string.
