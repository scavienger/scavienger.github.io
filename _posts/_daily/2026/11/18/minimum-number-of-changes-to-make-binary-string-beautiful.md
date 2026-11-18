---
layout: post
title: "Minimum Number of Changes to Make Binary String Beautiful"
date: 2026-11-18 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minChanges(string s) {\n        int changes\
        \ = 0;\n        for (int i = 0; i < s.length(); i += 2) {\n            if (s[i]\
        \ != s[i + 1]) {\n                changes++;\n            }\n        }\n   \
        \     return changes;\n    }\n};"
      java: "class Solution {\n    public int minChanges(String s) {\n        int changes\
        \ = 0;\n        int n = s.length();\n        for (int i = 0; i < n; i += 2)\
        \ {\n            if (s.charAt(i) != s.charAt(i + 1)) {\n                changes++;\n\
        \            }\n        }\n        return changes;\n    }\n}"
      python: "class Solution(object):\n    def minChanges(self, s):\n        \"\"\"\
        \n        :type s: str\n        :rtype: int\n        \"\"\"\n        changes\
        \ = 0\n        for i in range(0, len(s), 2):\n            if s[i] != s[i + 1]:\n\
        \                changes += 1\n        return changes"
      python3: "class Solution:\n    def minChanges(self, s: str) -> int:\n        changes\
        \ = 0\n        for i in range(0, len(s), 2):\n            if s[i] != s[i + 1]:\n\
        \                changes += 1\n        return changes"
      c: "int minChanges(char* s) {\n    int changes = 0;\n    for (int i = 0; s[i]\
        \ != '\\0'; i += 2) {\n        if (s[i] != s[i + 1]) {\n            changes++;\n\
        \        }\n    }\n    return changes;\n}"
      csharp: "public class Solution {\n    public int MinChanges(string s) {\n    \
        \    int changes = 0;\n        for (int i = 0; i < s.Length; i += 2) {\n   \
        \         if (s[i] != s[i + 1]) {\n                changes++;\n            }\n\
        \        }\n        return changes;\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {number}\n */\nvar minChanges\
        \ = function(s) {\n    let changes = 0;\n    for (let i = 0; i < s.length; i\
        \ += 2) {\n        if (s[i] !== s[i + 1]) {\n            changes++;\n      \
        \  }\n    }\n    return changes;\n};"
      typescript: "function minChanges(s: string): number {\n    let changes = 0;\n\
        \    for (let i = 0; i < s.length; i += 2) {\n        if (s[i] !== s[i + 1])\
        \ {\n            changes++;\n        }\n    }\n    return changes;\n}"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return Integer\n\
        \     */\n    function minChanges($s) {\n        $changes = 0;\n        $n =\
        \ strlen($s);\n        for ($i = 0; $i < $n; $i += 2) {\n            if ($s[$i]\
        \ !== $s[$i + 1]) {\n                $changes++;\n            }\n        }\n\
        \        return $changes;\n    }\n}"
      swift: "class Solution {\n    func minChanges(_ s: String) -> Int {\n        var\
        \ changes = 0\n        let characters = Array(s)\n        for i in stride(from:\
        \ 0, to: characters.count, by: 2) {\n            if characters[i] != characters[i\
        \ + 1] {\n                changes += 1\n            }\n        }\n        return\
        \ changes\n    }\n}"
      kotlin: "class Solution {\n    fun minChanges(s: String): Int {\n        var changes\
        \ = 0\n        for (i in 0 until s.length step 2) {\n            if (s[i] !=\
        \ s[i + 1]) {\n                changes++\n            }\n        }\n       \
        \ return changes\n    }\n}"
      dart: "class Solution {\n  int minChanges(String s) {\n    int changes = 0;\n\
        \    for (int i = 0; i < s.length; i += 2) {\n      if (s[i] != s[i + 1]) {\n\
        \        changes++;\n      }\n    }\n    return changes;\n  }\n}"
      go: "func minChanges(s string) int {\n    changes := 0\n    for i := 0; i < len(s);\
        \ i += 2 {\n        if s[i] != s[i+1] {\n            changes++\n        }\n\
        \    }\n    return changes\n}"
      ruby: "# @param {String} s\n# @return {Integer}\ndef min_changes(s)\n    changes\
        \ = 0\n    (0...s.length).step(2) do |i|\n        if s[i] != s[i + 1]\n    \
        \        changes += 1\n        end\n    end\n    changes\nend"
      scala: "object Solution {\n    def minChanges(s: String): Int = {\n        var\
        \ changes = 0\n        for (i <- 0 until s.length by 2) {\n            if (s(i)\
        \ != s(i + 1)) {\n                changes += 1\n            }\n        }\n \
        \       changes\n    }\n}"
      rust: "impl Solution {\n    pub fn min_changes(s: String) -> i32 {\n        let\
        \ bytes = s.as_bytes();\n        let mut changes = 0;\n        let n = bytes.len();\n\
        \        for i in (0..n).step_by(2) {\n            if bytes[i] != bytes[i +\
        \ 1] {\n                changes += 1;\n            }\n        }\n        changes\n\
        \    }\n}"
      racket: "(define/contract (min-changes s)\n  (-> string? exact-integer?)\n  (let\
        \ ([n (string-length s)])\n    (for/sum ([i (in-range 0 n 2)])\n      (if (char=?\
        \ (string-ref s i) (string-ref s (+ i 1)))\n          0\n          1))))"
      erlang: "-spec min_changes(S :: unicode:unicode_binary()) -> integer().\nmin_changes(S)\
        \ ->\n  min_changes_rec(S, 0).\n\nmin_changes_rec(<<>>, Acc) ->\n  Acc;\nmin_changes_rec(<<C1,\
        \ C2, Rest/binary>>, Acc) ->\n  NewAcc = if C1 =/= C2 -> Acc + 1;\n        \
        \      true -> Acc\n           end,\n  min_changes_rec(Rest, NewAcc)."
      elixir: "defmodule Solution do\n  @spec min_changes(s :: String.t) :: integer\n\
        \  def min_changes(s) do\n    count_changes(s, 0)\n  end\n\n  defp count_changes(<<>>,\
        \ acc), do: acc\n  defp count_changes(<<c1, c2, rest::binary>>, acc) do\n  \
        \  if c1 != c2 do\n      count_changes(rest, acc + 1)\n    else\n      count_changes(rest,\
        \ acc)\n    end\n  end\nend"
    approach: 'The core intuition is based on the requirement that a beautiful string
      can be partitioned into even-length substrings containing identical characters.
      Since any even length can be decomposed into disjoint blocks of size exactly 2,
      a beautiful string can always be viewed as a sequence of pairs $(s[0], s[1]),
      (s[2], s[3]), \dots, (s[n-2], s[n-1])$ where both characters in each specific
      pair are equal. Thus, the problem reduces to ensuring that every adjacent pair
      starting at an even index consists of the same character.


      To implement this, we iterate through the input string with a step size of 2,
      comparing character $s[i]$ with character $s[i+1]$. If the characters in a pair
      are different, we must change at least one of them to make the pair identical
      (either ''00'' or ''11''). We increment a counter for every mismatched pair found.
      This greedy approach works because each pair is independent; making a pair identical
      contributes to the overall beauty of the string with the minimum possible local
      effort, which aggregates to the global minimum.'
    time_complexity: O(n), where n is the length of the string. The algorithm performs
      a single linear scan through the string, examining each character once to process
      the pairs.
    space_complexity: O(1). The solution only uses a single integer counter to track
      the number of required changes, requiring no additional space that scales with
      the input size.
    elapsed_time: 28.251526355743408
    model: gemini-3-flash-preview
    generated_at: '2026-11-18 05:24:22 '
---

## Problem #2914: Minimum Number of Changes to Make Binary String Beautiful

**Difficulty:** Medium

**Topics:** String

## Problem Description

<p>You are given a <strong>0-indexed</strong> binary string <code>s</code> having an even length.</p>

<p>A string is <strong>beautiful</strong> if it&#39;s possible to partition it into one or more substrings such that:</p>

<ul>
	<li>Each substring has an <strong>even length</strong>.</li>
	<li>Each substring contains <strong>only</strong> <code>1</code>&#39;s or <strong>only</strong> <code>0</code>&#39;s.</li>
</ul>

<p>You can change any character in <code>s</code> to <code>0</code> or <code>1</code>.</p>

<p>Return <em>the <strong>minimum</strong> number of changes required to make the string </em><code>s</code> <em>beautiful</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;1001&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> We change s[1] to 1 and s[3] to 0 to get string &quot;1100&quot;.
It can be seen that the string &quot;1100&quot; is beautiful because we can partition it into &quot;11|00&quot;.
It can be proven that 2 is the minimum number of changes needed to make the string beautiful.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;10&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> We change s[1] to 1 to get string &quot;11&quot;.
It can be seen that the string &quot;11&quot; is beautiful because we can partition it into &quot;11&quot;.
It can be proven that 1 is the minimum number of changes needed to make the string beautiful.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;0000&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> We don&#39;t need to make any changes as the string &quot;0000&quot; is beautiful already.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> has an even length.</li>
	<li><code>s[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
</ul>


## Hints

1. For any valid partition, since each part consists of an even number of the same characters, we can further partition each part into lengths of exactly `2`.

2. After noticing the first hint, we can decompose the whole string into disjoint blocks of size `2` and find the minimum number of changes required to make those blocks beautiful.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The core intuition is based on the requirement that a beautiful string can be partitioned into even-length substrings containing identical characters. Since any even length can be decomposed into disjoint blocks of size exactly 2, a beautiful string can always be viewed as a sequence of pairs $(s[0], s[1]), (s[2], s[3]), \dots, (s[n-2], s[n-1])$ where both characters in each specific pair are equal. Thus, the problem reduces to ensuring that every adjacent pair starting at an even index consists of the same character.

To implement this, we iterate through the input string with a step size of 2, comparing character $s[i]$ with character $s[i+1]$. If the characters in a pair are different, we must change at least one of them to make the pair identical (either '00' or '11'). We increment a counter for every mismatched pair found. This greedy approach works because each pair is independent; making a pair identical contributes to the overall beauty of the string with the minimum possible local effort, which aggregates to the global minimum.

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
    int minChanges(string s) {
        int changes = 0;
        for (int i = 0; i < s.length(); i += 2) {
            if (s[i] != s[i + 1]) {
                changes++;
            }
        }
        return changes;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minChanges(String s) {
        int changes = 0;
        int n = s.length();
        for (int i = 0; i < n; i += 2) {
            if (s.charAt(i) != s.charAt(i + 1)) {
                changes++;
            }
        }
        return changes;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        changes = 0
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                changes += 1
        return changes
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minChanges(self, s: str) -> int:
        changes = 0
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                changes += 1
        return changes
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int minChanges(char* s) {
    int changes = 0;
    for (int i = 0; s[i] != '\0'; i += 2) {
        if (s[i] != s[i + 1]) {
            changes++;
        }
    }
    return changes;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinChanges(string s) {
        int changes = 0;
        for (int i = 0; i < s.Length; i += 2) {
            if (s[i] != s[i + 1]) {
                changes++;
            }
        }
        return changes;
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
var minChanges = function(s) {
    let changes = 0;
    for (let i = 0; i < s.length; i += 2) {
        if (s[i] !== s[i + 1]) {
            changes++;
        }
    }
    return changes;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minChanges(s: string): number {
    let changes = 0;
    for (let i = 0; i < s.length; i += 2) {
        if (s[i] !== s[i + 1]) {
            changes++;
        }
    }
    return changes;
}
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
    function minChanges($s) {
        $changes = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i += 2) {
            if ($s[$i] !== $s[$i + 1]) {
                $changes++;
            }
        }
        return $changes;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minChanges(_ s: String) -> Int {
        var changes = 0
        let characters = Array(s)
        for i in stride(from: 0, to: characters.count, by: 2) {
            if characters[i] != characters[i + 1] {
                changes += 1
            }
        }
        return changes
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minChanges(s: String): Int {
        var changes = 0
        for (i in 0 until s.length step 2) {
            if (s[i] != s[i + 1]) {
                changes++
            }
        }
        return changes
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minChanges(String s) {
    int changes = 0;
    for (int i = 0; i < s.length; i += 2) {
      if (s[i] != s[i + 1]) {
        changes++;
      }
    }
    return changes;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minChanges(s string) int {
    changes := 0
    for i := 0; i < len(s); i += 2 {
        if s[i] != s[i+1] {
            changes++
        }
    }
    return changes
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @return {Integer}
def min_changes(s)
    changes = 0
    (0...s.length).step(2) do |i|
        if s[i] != s[i + 1]
            changes += 1
        end
    end
    changes
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minChanges(s: String): Int = {
        var changes = 0
        for (i <- 0 until s.length by 2) {
            if (s(i) != s(i + 1)) {
                changes += 1
            }
        }
        changes
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_changes(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut changes = 0;
        let n = bytes.len();
        for i in (0..n).step_by(2) {
            if bytes[i] != bytes[i + 1] {
                changes += 1;
            }
        }
        changes
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-changes s)
  (-> string? exact-integer?)
  (let ([n (string-length s)])
    (for/sum ([i (in-range 0 n 2)])
      (if (char=? (string-ref s i) (string-ref s (+ i 1)))
          0
          1))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_changes(S :: unicode:unicode_binary()) -> integer().
min_changes(S) ->
  min_changes_rec(S, 0).

min_changes_rec(<<>>, Acc) ->
  Acc;
min_changes_rec(<<C1, C2, Rest/binary>>, Acc) ->
  NewAcc = if C1 =/= C2 -> Acc + 1;
              true -> Acc
           end,
  min_changes_rec(Rest, NewAcc).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_changes(s :: String.t) :: integer
  def min_changes(s) do
    count_changes(s, 0)
  end

  defp count_changes(<<>>, acc), do: acc
  defp count_changes(<<c1, c2, rest::binary>>, acc) do
    if c1 != c2 do
      count_changes(rest, acc + 1)
    else
      count_changes(rest, acc)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n), where n is the length of the string. The algorithm performs a single linear scan through the string, examining each character once to process the pairs.
- **Space Complexity:** O(1). The solution only uses a single integer counter to track the number of required changes, requiring no additional space that scales with the input size.
