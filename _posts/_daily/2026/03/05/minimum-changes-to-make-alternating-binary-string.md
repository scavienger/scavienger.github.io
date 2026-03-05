---
layout: post
title: "Minimum Changes To Make Alternating Binary String"
date: 2026-03-05 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["String"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minOperations(string s) {\n        int\
        \ n = s.length();\n        int count0 = 0;\n        for (int i = 0; i < n; ++i)\
        \ {\n            char expected = (i % 2 == 0) ? '0' : '1';\n            if (s[i]\
        \ != expected) {\n                count0++;\n            }\n        }\n    \
        \    return min(count0, n - count0);\n    }\n};"
      java: "class Solution {\n    public int minOperations(String s) {\n        int\
        \ n = s.length();\n        int count0 = 0;\n        for (int i = 0; i < n; i++)\
        \ {\n            char expected = (i % 2 == 0) ? '0' : '1';\n            if (s.charAt(i)\
        \ != expected) {\n                count0++;\n            }\n        }\n    \
        \    return Math.min(count0, n - count0);\n    }\n}"
      python: "class Solution(object):\n    def minOperations(self, s):\n        \"\"\
        \"\n        :type s: str\n        :rtype: int\n        \"\"\"\n        n = len(s)\n\
        \        count0 = 0\n        for i in range(n):\n            expected = str(i\
        \ % 2)\n            if s[i] != expected:\n                count0 += 1\n    \
        \    return min(count0, n - count0)"
      python3: "class Solution:\n    def minOperations(self, s: str) -> int:\n     \
        \   n = len(s)\n        count0 = 0\n        for i in range(n):\n           \
        \ expected = str(i % 2)\n            if s[i] != expected:\n                count0\
        \ += 1\n        return min(count0, n - count0)"
      c: "int minOperations(char* s) {\n    int n = 0;\n    while (s[n] != '\\0') n++;\n\
        \    int count0 = 0;\n    for (int i = 0; i < n; i++) {\n        char expected\
        \ = (i % 2 == 0) ? '0' : '1';\n        if (s[i] != expected) {\n           \
        \ count0++;\n        }\n    }\n    int count1 = n - count0;\n    return count0\
        \ < count1 ? count0 : count1;\n}"
      csharp: "public class Solution {\n    public int MinOperations(string s) {\n \
        \       int n = s.Length;\n        int count0 = 0;\n        for (int i = 0;\
        \ i < n; i++) {\n            char expected = (i % 2 == 0) ? '0' : '1';\n   \
        \         if (s[i] != expected) {\n                count0++;\n            }\n\
        \        }\n        return Math.Min(count0, n - count0);\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {number}\n */\nvar minOperations\
        \ = function(s) {\n    const n = s.length;\n    let count0 = 0;\n    for (let\
        \ i = 0; i < n; i++) {\n        const expected = (i % 2 === 0) ? '0' : '1';\n\
        \        if (s[i] !== expected) {\n            count0++;\n        }\n    }\n\
        \    return Math.min(count0, n - count0);\n};"
      typescript: "function minOperations(s: string): number {\n    const n = s.length;\n\
        \    let count0 = 0;\n    for (let i = 0; i < n; i++) {\n        if (s[i] !==\
        \ (i % 2 === 0 ? '0' : '1')) {\n            count0++;\n        }\n    }\n  \
        \  return Math.min(count0, n - count0);\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return Integer\n\
        \     */\n    function minOperations($s) {\n        $n = strlen($s);\n     \
        \   $count0 = 0;\n        for ($i = 0; $i < $n; $i++) {\n            if ($s[$i]\
        \ !== ($i % 2 === 0 ? '0' : '1')) {\n                $count0++;\n          \
        \  }\n        }\n        return min($count0, $n - $count0);\n    }\n}"
      swift: "class Solution {\n    func minOperations(_ s: String) -> Int {\n     \
        \   let sArray = Array(s)\n        let n = sArray.count\n        var count0\
        \ = 0\n        for i in 0..<n {\n            let expected: Character = (i %\
        \ 2 == 0 ? \"0\" : \"1\")\n            if sArray[i] != expected {\n        \
        \        count0 += 1\n            }\n        }\n        return min(count0, n\
        \ - count0)\n    }\n}"
      kotlin: "class Solution {\n    fun minOperations(s: String): Int {\n        val\
        \ n = s.length\n        var count0 = 0\n        for (i in 0 until n) {\n   \
        \         val expected = if (i % 2 == 0) '0' else '1'\n            if (s[i]\
        \ != expected) {\n                count0++\n            }\n        }\n     \
        \   return Math.min(count0, n - count0)\n    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int minOperations(String s)\
        \ {\n    int n = s.length;\n    int count0 = 0;\n    for (int i = 0; i < n;\
        \ i++) {\n      String expected = (i % 2 == 0 ? '0' : '1');\n      if (s[i]\
        \ != expected) {\n        count0++;\n      }\n    }\n    return min(count0,\
        \ n - count0);\n  }\n}"
      go: "func minOperations(s string) int {\n    n := len(s)\n    count0 := 0\n  \
        \  for i := 0; i < n; i++ {\n        var expected byte\n        if i % 2 ==\
        \ 0 {\n            expected = '0'\n        } else {\n            expected =\
        \ '1'\n        }\n        if s[i] != expected {\n            count0++\n    \
        \    }\n    }\n    if count0 < n - count0 {\n        return count0\n    }\n\
        \    return n - count0\n}"
      ruby: "def min_operations(s)\n  n = s.length\n  c1 = 0\n  s.each_char.with_index\
        \ do |char, i|\n    expected = (i.even? ? '0' : '1')\n    c1 += 1 if char !=\
        \ expected\n  end\n  [c1, n - c1].min\nend"
      scala: "object Solution {\n  def minOperations(s: String): Int = {\n    val n\
        \ = s.length\n    var c1 = 0\n    for (i <- 0 until n) {\n      val expected\
        \ = if (i % 2 == 0) '0' else '1'\n      if (s.charAt(i) != expected) c1 += 1\n\
        \    }\n    math.min(c1, n - c1)\n  }\n}"
      rust: "impl Solution {\n    pub fn min_operations(s: String) -> i32 {\n      \
        \  let n = s.len() as i32;\n        let mut c1 = 0;\n        for (i, c) in s.chars().enumerate()\
        \ {\n            let expected = if i % 2 == 0 { '0' } else { '1' };\n      \
        \      if c != expected {\n                c1 += 1;\n            }\n       \
        \ }\n        std::cmp::min(c1, n - c1)\n    }\n}"
      racket: "(define/contract (min-operations s)\n  (-> string? exact-integer?)\n\
        \  (let* ([n (string-length s)]\n         [c1 (for/sum ([i (in-range n)])\n\
        \               (if (char=? (string-ref s i) (if (even? i) #\\0 #\\1)) 0 1))])\n\
        \    (min c1 (- n c1))))"
      erlang: "min_operations(S) ->\n  L = binary_to_list(S),\n  N = length(L),\n  C1\
        \ = count_changes(L, 0, 0),\n  erlang:min(C1, N - C1).\n\ncount_changes([],\
        \ _I, Acc) ->\n  Acc;\ncount_changes([H | T], I, Acc) ->\n  Expected = case\
        \ I rem 2 of\n    0 -> $0;\n    1 -> $1\n  end,\n  NewAcc = if H =/= Expected\
        \ -> Acc + 1; true -> Acc end,\n  count_changes(T, I + 1, NewAcc)."
      elixir: "defmodule Solution do\n  @spec min_operations(s :: String.t) :: integer\n\
        \  def min_operations(s) do\n    chars = String.to_charlist(s)\n    n = length(chars)\n\
        \    c1 = chars\n         |> Enum.with_index()\n         |> Enum.count(fn {char,\
        \ i} ->\n              expected = if rem(i, 2) == 0, do: ?0, else: ?1\n    \
        \          char != expected\n            end)\n    min(c1, n - c1)\n  end\n\
        end"
    approach: 'An alternating binary string follows one of two distinct patterns: it
      either starts with ''0'' and alternates (0101...) or it starts with ''1'' and
      alternates (1010...). To find the minimum number of operations, we only need to
      calculate how many characters differ between the input string and one of these
      two ideal patterns. If we let $k$ be the number of positions where the string
      $s$ differs from the pattern starting with ''0'', then $k$ represents the cost
      to transform $s$ into the first pattern.


      Since the pattern starting with ''1'' is the exact inverse of the pattern starting
      with ''0'', every character that matches the first pattern will necessarily mismatch
      the second pattern. Consequently, the number of changes required to transform
      $s$ into the pattern starting with ''1'' is simply $n - k$, where $n$ is the length
      of the string. The final answer is the minimum of these two counts: $\min(k, n
      - k)$. This observation allows us to solve the problem by iterating through the
      string exactly once.'
    time_complexity: O(n), where n is the length of the string. The algorithm iterates
      through the input string a single time to count the mismatches against a target
      alternating pattern.
    space_complexity: O(1). We only use a constant amount of extra space for counters
      and loop variables, regardless of the size of the input string.
    elapsed_time: 96.47256922721863
    model: gemini-3-flash-preview
    generated_at: '2026-03-05 01:24:32 '
---

## Problem #1758: Minimum Changes To Make Alternating Binary String

**Difficulty:** Easy

**Topics:** String

## Problem Description

<p>You are given a string <code>s</code> consisting only of the characters <code>&#39;0&#39;</code> and <code>&#39;1&#39;</code>. In one operation, you can change any <code>&#39;0&#39;</code> to <code>&#39;1&#39;</code> or vice versa.</p>

<p>The string is called alternating if no two adjacent characters are equal. For example, the string <code>&quot;010&quot;</code> is alternating, while the string <code>&quot;0100&quot;</code> is not.</p>

<p>Return <em>the <strong>minimum</strong> number of operations needed to make</em> <code>s</code> <em>alternating</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;0100&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> If you change the last character to &#39;1&#39;, s will be &quot;0101&quot;, which is alternating.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;10&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> s is already alternating.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;1111&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> You need two operations to reach &quot;0101&quot; or &quot;1010&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
</ul>


## Hints

1. Think about how the final string will look like.

2. It will either start with a '0' and be like '010101010..' or with a '1' and be like '10101010..'

3. Try both ways, and check for each way, the number of changes needed to reach it from the given string. The answer is the minimum of both ways.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

An alternating binary string follows one of two distinct patterns: it either starts with '0' and alternates (0101...) or it starts with '1' and alternates (1010...). To find the minimum number of operations, we only need to calculate how many characters differ between the input string and one of these two ideal patterns. If we let $k$ be the number of positions where the string $s$ differs from the pattern starting with '0', then $k$ represents the cost to transform $s$ into the first pattern.

Since the pattern starting with '1' is the exact inverse of the pattern starting with '0', every character that matches the first pattern will necessarily mismatch the second pattern. Consequently, the number of changes required to transform $s$ into the pattern starting with '1' is simply $n - k$, where $n$ is the length of the string. The final answer is the minimum of these two counts: $\min(k, n - k)$. This observation allows us to solve the problem by iterating through the string exactly once.

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
    int minOperations(string s) {
        int n = s.length();
        int count0 = 0;
        for (int i = 0; i < n; ++i) {
            char expected = (i % 2 == 0) ? '0' : '1';
            if (s[i] != expected) {
                count0++;
            }
        }
        return min(count0, n - count0);
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minOperations(String s) {
        int n = s.length();
        int count0 = 0;
        for (int i = 0; i < n; i++) {
            char expected = (i % 2 == 0) ? '0' : '1';
            if (s.charAt(i) != expected) {
                count0++;
            }
        }
        return Math.min(count0, n - count0);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count0 = 0
        for i in range(n):
            expected = str(i % 2)
            if s[i] != expected:
                count0 += 1
        return min(count0, n - count0)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        count0 = 0
        for i in range(n):
            expected = str(i % 2)
            if s[i] != expected:
                count0 += 1
        return min(count0, n - count0)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int minOperations(char* s) {
    int n = 0;
    while (s[n] != '\0') n++;
    int count0 = 0;
    for (int i = 0; i < n; i++) {
        char expected = (i % 2 == 0) ? '0' : '1';
        if (s[i] != expected) {
            count0++;
        }
    }
    int count1 = n - count0;
    return count0 < count1 ? count0 : count1;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinOperations(string s) {
        int n = s.Length;
        int count0 = 0;
        for (int i = 0; i < n; i++) {
            char expected = (i % 2 == 0) ? '0' : '1';
            if (s[i] != expected) {
                count0++;
            }
        }
        return Math.Min(count0, n - count0);
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
var minOperations = function(s) {
    const n = s.length;
    let count0 = 0;
    for (let i = 0; i < n; i++) {
        const expected = (i % 2 === 0) ? '0' : '1';
        if (s[i] !== expected) {
            count0++;
        }
    }
    return Math.min(count0, n - count0);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minOperations(s: string): number {
    const n = s.length;
    let count0 = 0;
    for (let i = 0; i < n; i++) {
        if (s[i] !== (i % 2 === 0 ? '0' : '1')) {
            count0++;
        }
    }
    return Math.min(count0, n - count0);
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
    function minOperations($s) {
        $n = strlen($s);
        $count0 = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] !== ($i % 2 === 0 ? '0' : '1')) {
                $count0++;
            }
        }
        return min($count0, $n - $count0);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minOperations(_ s: String) -> Int {
        let sArray = Array(s)
        let n = sArray.count
        var count0 = 0
        for i in 0..<n {
            let expected: Character = (i % 2 == 0 ? "0" : "1")
            if sArray[i] != expected {
                count0 += 1
            }
        }
        return min(count0, n - count0)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minOperations(s: String): Int {
        val n = s.length
        var count0 = 0
        for (i in 0 until n) {
            val expected = if (i % 2 == 0) '0' else '1'
            if (s[i] != expected) {
                count0++
            }
        }
        return Math.min(count0, n - count0)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:math';

class Solution {
  int minOperations(String s) {
    int n = s.length;
    int count0 = 0;
    for (int i = 0; i < n; i++) {
      String expected = (i % 2 == 0 ? '0' : '1');
      if (s[i] != expected) {
        count0++;
      }
    }
    return min(count0, n - count0);
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minOperations(s string) int {
    n := len(s)
    count0 := 0
    for i := 0; i < n; i++ {
        var expected byte
        if i % 2 == 0 {
            expected = '0'
        } else {
            expected = '1'
        }
        if s[i] != expected {
            count0++
        }
    }
    if count0 < n - count0 {
        return count0
    }
    return n - count0
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def min_operations(s)
  n = s.length
  c1 = 0
  s.each_char.with_index do |char, i|
    expected = (i.even? ? '0' : '1')
    c1 += 1 if char != expected
  end
  [c1, n - c1].min
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def minOperations(s: String): Int = {
    val n = s.length
    var c1 = 0
    for (i <- 0 until n) {
      val expected = if (i % 2 == 0) '0' else '1'
      if (s.charAt(i) != expected) c1 += 1
    }
    math.min(c1, n - c1)
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_operations(s: String) -> i32 {
        let n = s.len() as i32;
        let mut c1 = 0;
        for (i, c) in s.chars().enumerate() {
            let expected = if i % 2 == 0 { '0' } else { '1' };
            if c != expected {
                c1 += 1;
            }
        }
        std::cmp::min(c1, n - c1)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-operations s)
  (-> string? exact-integer?)
  (let* ([n (string-length s)]
         [c1 (for/sum ([i (in-range n)])
               (if (char=? (string-ref s i) (if (even? i) #\0 #\1)) 0 1))])
    (min c1 (- n c1))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
min_operations(S) ->
  L = binary_to_list(S),
  N = length(L),
  C1 = count_changes(L, 0, 0),
  erlang:min(C1, N - C1).

count_changes([], _I, Acc) ->
  Acc;
count_changes([H | T], I, Acc) ->
  Expected = case I rem 2 of
    0 -> $0;
    1 -> $1
  end,
  NewAcc = if H =/= Expected -> Acc + 1; true -> Acc end,
  count_changes(T, I + 1, NewAcc).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_operations(s :: String.t) :: integer
  def min_operations(s) do
    chars = String.to_charlist(s)
    n = length(chars)
    c1 = chars
         |> Enum.with_index()
         |> Enum.count(fn {char, i} ->
              expected = if rem(i, 2) == 0, do: ?0, else: ?1
              char != expected
            end)
    min(c1, n - c1)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n), where n is the length of the string. The algorithm iterates through the input string a single time to count the mismatches against a target alternating pattern.
- **Space Complexity:** O(1). We only use a constant amount of extra space for counters and loop variables, regardless of the size of the input string.
