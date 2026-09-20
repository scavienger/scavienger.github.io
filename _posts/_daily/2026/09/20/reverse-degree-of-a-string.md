---
layout: post
title: "Reverse Degree of a String"
date: 2026-09-20 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["String", "Simulation"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/reverse-degree-of-a-string/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int reverseDegree(string s) {\n        int\
        \ total = 0;\n        int n = s.length();\n        for (int i = 0; i < n; ++i)\
        \ {\n            int revVal = 26 - (s[i] - 'a');\n            total += revVal\
        \ * (i + 1);\n        }\n        return total;\n    }\n};"
      java: "class Solution {\n    public int reverseDegree(String s) {\n        int\
        \ total = 0;\n        int n = s.length();\n        for (int i = 0; i < n; ++i)\
        \ {\n            int revVal = 26 - (s.charAt(i) - 'a');\n            total +=\
        \ revVal * (i + 1);\n        }\n        return total;\n    }\n}"
      python: "class Solution(object):\n    def reverseDegree(self, s):\n        \"\"\
        \"\n        :type s: str\n        :rtype: int\n        \"\"\"\n        total\
        \ = 0\n        for i in range(len(s)):\n            revVal = 26 - (ord(s[i])\
        \ - ord('a'))\n            total += revVal * (i + 1)\n        return total"
      python3: "class Solution:\n    def reverseDegree(self, s: str) -> int:\n     \
        \   total = 0\n        for i, char in enumerate(s, 1):\n            revVal =\
        \ 26 - (ord(char) - ord('a'))\n            total += revVal * i\n        return\
        \ total"
      c: "int reverseDegree(char* s) {\n    int total = 0;\n    for (int i = 0; s[i]\
        \ != '\\0'; ++i) {\n        int revVal = 26 - (s[i] - 'a');\n        total +=\
        \ revVal * (i + 1);\n    }\n    return total;\n}"
      csharp: "public class Solution {\n    public int ReverseDegree(string s) {\n \
        \       int total = 0;\n        for (int i = 0; i < s.Length; ++i) {\n     \
        \       int revVal = 26 - (s[i] - 'a');\n            total += revVal * (i +\
        \ 1);\n        }\n        return total;\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {number}\n */\nvar reverseDegree\
        \ = function(s) {\n    let total = 0;\n    let charCodeA = 'a'.charCodeAt(0);\n\
        \    for (let i = 0; i < s.length; i++) {\n        let revVal = 26 - (s.charCodeAt(i)\
        \ - charCodeA);\n        total += revVal * (i + 1);\n    }\n    return total;\n\
        };"
      typescript: "function reverseDegree(s: string): number {\n    let total = 0;\n\
        \    for (let i = 0; i < s.length; i++) {\n        const reversedPos = 26 -\
        \ (s.charCodeAt(i) - 97);\n        total += reversedPos * (i + 1);\n    }\n\
        \    return total;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return Integer\n\
        \     */\n    function reverseDegree($s) {\n        $total = 0;\n        $len\
        \ = strlen($s);\n        for ($i = 0; $i < $len; $i++) {\n            $reversedPos\
        \ = 26 - (ord($s[$i]) - 97);\n            $total += $reversedPos * ($i + 1);\n\
        \        }\n        return $total;\n    }\n}"
      swift: "class Solution {\n    func reverseDegree(_ s: String) -> Int {\n     \
        \   var total = 0\n        var position = 1\n        for scalar in s.unicodeScalars\
        \ {\n            let val = Int(scalar.value)\n            let reversedPos =\
        \ 26 - (val - 97)\n            total += reversedPos * position\n           \
        \ position += 1\n        }\n        return total\n    }\n}"
      kotlin: "class Solution {\n    fun reverseDegree(s: String): Int {\n        var\
        \ total = 0\n        for (i in s.indices) {\n            val reversedPos = 26\
        \ - (s[i] - 'a')\n            total += reversedPos * (i + 1)\n        }\n  \
        \      return total\n    }\n}"
      dart: "class Solution {\n  int reverseDegree(String s) {\n    int total = 0;\n\
        \    for (int i = 0; i < s.length; i++) {\n      int reversedPos = 26 - (s.codeUnitAt(i)\
        \ - 97);\n      total += reversedPos * (i + 1);\n    }\n    return total;\n\
        \  }\n}"
      go: "func reverseDegree(s string) int {\n    total := 0\n    for i := 0; i < len(s);\
        \ i++ {\n        reversedPos := 26 - int(s[i] - 'a')\n        total += reversedPos\
        \ * (i + 1)\n    }\n    return total\n}"
      ruby: "# @param {String} s\n# @return {Integer}\ndef reverse_degree(s)\n  sum\
        \ = 0\n  s.each_char.with_index(1) do |char, i|\n    sum += (26 - (char.ord\
        \ - 'a'.ord)) * i\n  end\n  sum\nend"
      scala: "object Solution {\n    def reverseDegree(s: String): Int = {\n       \
        \ var sum = 0\n        for (i <- 0 until s.length) {\n            val valRev\
        \ = 26 - (s(i) - 'a')\n            sum += valRev * (i + 1)\n        }\n    \
        \    sum\n    }\n}"
      rust: "impl Solution {\n    pub fn reverse_degree(s: String) -> i32 {\n      \
        \  s.chars().enumerate().map(|(i, c)| {\n            (26 - (c as i32 - 'a' as\
        \ i32)) * (i as i32 + 1)\n        }).sum()\n    }\n}"
      racket: "(define/contract (reverse-degree s)\n  (-> string? exact-integer?)\n\
        \  (let ([chars (string->list s)])\n    (for/sum ([c chars]\n              [i\
        \ (in-range 1 (add1 (length chars)))])\n      (* (- 26 (- (char->integer c)\
        \ (char->integer #\\a))) i))))"
      erlang: "-spec reverse_degree(S :: unicode:unicode_binary()) -> integer().\nreverse_degree(S)\
        \ ->\n  {_, Result} = lists:foldl(fun(Char, {Idx, Acc}) ->\n               \
        \               {Idx + 1, Acc + (26 - (Char - $a)) * Idx}\n                \
        \            end, {1, 0}, binary_to_list(S)),\n  Result."
      elixir: "defmodule Solution do\n  @spec reverse_degree(s :: String.t) :: integer\n\
        \  def reverse_degree(s) do\n    s\n    |> String.to_charlist()\n    |> Enum.with_index(1)\n\
        \    |> Enum.reduce(0, fn {char, i}, acc ->\n      val = 26 - (char - ?a)\n\
        \      acc + (val * i)\n    end)\n  end\nend"
    approach: 'The algorithm calculates the reverse degree by iterating through the
      string once and identifying each character''s contribution to the total sum based
      on its position in the string and its rank in the alphabet. For every character
      at a 1-indexed position $i$, its reversed alphabet rank is computed by subtracting
      its index in the standard ''a-z'' sequence from 26 (mapping ''a'' to 26, ''b''
      to 25, ..., and ''z'' to 1). This value is then multiplied by the character''s
      string position $i$ to determine its individual product.


      To ensure efficiency, the process is implemented as a single linear scan of the
      input string. By accumulating these products in a running integer variable, the
      total reverse degree is calculated in a single pass. This approach is optimal
      given the constraints, as it processes the string once and uses minimal additional
      memory to store the cumulative result.'
    time_complexity: O(n), where n is the length of the string. The algorithm traverses
      the entire string once, and for each character, it performs a fixed number of
      constant-time arithmetic operations and lookups.
    space_complexity: O(1), as the algorithm only uses a small number of integer variables
      to maintain the running total and the iteration index, which does not scale with
      the size of the input.
    elapsed_time: 147.44228076934814
    model: gemini-3-flash-preview
    generated_at: '2026-09-20 02:43:55 '
---

## Problem #3498: Reverse Degree of a String

**Difficulty:** Easy

**Topics:** String, Simulation

## Problem Description

<p>Given a string <code>s</code>, calculate its <strong>reverse degree</strong>.</p>

<p>The <strong>reverse degree</strong> is calculated as follows:</p>

<ol>
	<li>For each character, multiply its position in the <em>reversed</em> alphabet (<code>&#39;a&#39;</code> = 26, <code>&#39;b&#39;</code> = 25, ..., <code>&#39;z&#39;</code> = 1) with its position in the string <strong>(1-indexed)</strong>.</li>
	<li>Sum these products for all characters in the string.</li>
</ol>

<p>Return the <strong>reverse degree</strong> of <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abc&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">148</span></p>

<p><strong>Explanation:</strong></p>

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Letter</th>
			<th style="border: 1px solid black;">Index in Reversed Alphabet</th>
			<th style="border: 1px solid black;">Index in String</th>
			<th style="border: 1px solid black;">Product</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>&#39;a&#39;</code></td>
			<td style="border: 1px solid black;">26</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">26</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>&#39;b&#39;</code></td>
			<td style="border: 1px solid black;">25</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">50</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>&#39;c&#39;</code></td>
			<td style="border: 1px solid black;">24</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">72</td>
		</tr>
	</tbody>
</table>

<p>The reversed degree is <code>26 + 50 + 72 = 148</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;zaza&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">160</span></p>

<p><strong>Explanation:</strong></p>

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Letter</th>
			<th style="border: 1px solid black;">Index in Reversed Alphabet</th>
			<th style="border: 1px solid black;">Index in String</th>
			<th style="border: 1px solid black;">Product</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>&#39;z&#39;</code></td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>&#39;a&#39;</code></td>
			<td style="border: 1px solid black;">26</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">52</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>&#39;z&#39;</code></td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><code>&#39;a&#39;</code></td>
			<td style="border: 1px solid black;">26</td>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">104</td>
		</tr>
	</tbody>
</table>

<p>The reverse degree is <code>1 + 52 + 3 + 104 = 160</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
</ul>


## Hints

1. Simulate the operations as described.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm calculates the reverse degree by iterating through the string once and identifying each character's contribution to the total sum based on its position in the string and its rank in the alphabet. For every character at a 1-indexed position $i$, its reversed alphabet rank is computed by subtracting its index in the standard 'a-z' sequence from 26 (mapping 'a' to 26, 'b' to 25, ..., and 'z' to 1). This value is then multiplied by the character's string position $i$ to determine its individual product.

To ensure efficiency, the process is implemented as a single linear scan of the input string. By accumulating these products in a running integer variable, the total reverse degree is calculated in a single pass. This approach is optimal given the constraints, as it processes the string once and uses minimal additional memory to store the cumulative result.

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
    int reverseDegree(string s) {
        int total = 0;
        int n = s.length();
        for (int i = 0; i < n; ++i) {
            int revVal = 26 - (s[i] - 'a');
            total += revVal * (i + 1);
        }
        return total;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int reverseDegree(String s) {
        int total = 0;
        int n = s.length();
        for (int i = 0; i < n; ++i) {
            int revVal = 26 - (s.charAt(i) - 'a');
            total += revVal * (i + 1);
        }
        return total;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for i in range(len(s)):
            revVal = 26 - (ord(s[i]) - ord('a'))
            total += revVal * (i + 1)
        return total
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, char in enumerate(s, 1):
            revVal = 26 - (ord(char) - ord('a'))
            total += revVal * i
        return total
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int reverseDegree(char* s) {
    int total = 0;
    for (int i = 0; s[i] != '\0'; ++i) {
        int revVal = 26 - (s[i] - 'a');
        total += revVal * (i + 1);
    }
    return total;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int ReverseDegree(string s) {
        int total = 0;
        for (int i = 0; i < s.Length; ++i) {
            int revVal = 26 - (s[i] - 'a');
            total += revVal * (i + 1);
        }
        return total;
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
var reverseDegree = function(s) {
    let total = 0;
    let charCodeA = 'a'.charCodeAt(0);
    for (let i = 0; i < s.length; i++) {
        let revVal = 26 - (s.charCodeAt(i) - charCodeA);
        total += revVal * (i + 1);
    }
    return total;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function reverseDegree(s: string): number {
    let total = 0;
    for (let i = 0; i < s.length; i++) {
        const reversedPos = 26 - (s.charCodeAt(i) - 97);
        total += reversedPos * (i + 1);
    }
    return total;
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
    function reverseDegree($s) {
        $total = 0;
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $reversedPos = 26 - (ord($s[$i]) - 97);
            $total += $reversedPos * ($i + 1);
        }
        return $total;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func reverseDegree(_ s: String) -> Int {
        var total = 0
        var position = 1
        for scalar in s.unicodeScalars {
            let val = Int(scalar.value)
            let reversedPos = 26 - (val - 97)
            total += reversedPos * position
            position += 1
        }
        return total
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun reverseDegree(s: String): Int {
        var total = 0
        for (i in s.indices) {
            val reversedPos = 26 - (s[i] - 'a')
            total += reversedPos * (i + 1)
        }
        return total
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int reverseDegree(String s) {
    int total = 0;
    for (int i = 0; i < s.length; i++) {
      int reversedPos = 26 - (s.codeUnitAt(i) - 97);
      total += reversedPos * (i + 1);
    }
    return total;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func reverseDegree(s string) int {
    total := 0
    for i := 0; i < len(s); i++ {
        reversedPos := 26 - int(s[i] - 'a')
        total += reversedPos * (i + 1)
    }
    return total
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @return {Integer}
def reverse_degree(s)
  sum = 0
  s.each_char.with_index(1) do |char, i|
    sum += (26 - (char.ord - 'a'.ord)) * i
  end
  sum
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def reverseDegree(s: String): Int = {
        var sum = 0
        for (i <- 0 until s.length) {
            val valRev = 26 - (s(i) - 'a')
            sum += valRev * (i + 1)
        }
        sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn reverse_degree(s: String) -> i32 {
        s.chars().enumerate().map(|(i, c)| {
            (26 - (c as i32 - 'a' as i32)) * (i as i32 + 1)
        }).sum()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (reverse-degree s)
  (-> string? exact-integer?)
  (let ([chars (string->list s)])
    (for/sum ([c chars]
              [i (in-range 1 (add1 (length chars)))])
      (* (- 26 (- (char->integer c) (char->integer #\a))) i))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec reverse_degree(S :: unicode:unicode_binary()) -> integer().
reverse_degree(S) ->
  {_, Result} = lists:foldl(fun(Char, {Idx, Acc}) ->
                              {Idx + 1, Acc + (26 - (Char - $a)) * Idx}
                            end, {1, 0}, binary_to_list(S)),
  Result.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec reverse_degree(s :: String.t) :: integer
  def reverse_degree(s) do
    s
    |> String.to_charlist()
    |> Enum.with_index(1)
    |> Enum.reduce(0, fn {char, i}, acc ->
      val = 26 - (char - ?a)
      acc + (val * i)
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n), where n is the length of the string. The algorithm traverses the entire string once, and for each character, it performs a fixed number of constant-time arithmetic operations and lookups.
- **Space Complexity:** O(1), as the algorithm only uses a small number of integer variables to maintain the running total and the iteration index, which does not scale with the size of the input.
