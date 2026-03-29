---
layout: post
title: "Check if Strings Can be Made Equal With Operations I"
date: 2026-03-29 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["String"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool canBeEqual(string s1, string s2) {\n\
        \        bool evenMatch = (s1[0] == s2[0] && s1[2] == s2[2]) || (s1[0] == s2[2]\
        \ && s1[2] == s2[0]);\n        bool oddMatch = (s1[1] == s2[1] && s1[3] == s2[3])\
        \ || (s1[1] == s2[3] && s1[3] == s2[1]);\n        return evenMatch && oddMatch;\n\
        \    }\n};"
      java: "class Solution {\n    public boolean canBeEqual(String s1, String s2) {\n\
        \        boolean evenMatch = (s1.charAt(0) == s2.charAt(0) && s1.charAt(2) ==\
        \ s2.charAt(2)) ||\n                          (s1.charAt(0) == s2.charAt(2)\
        \ && s1.charAt(2) == s2.charAt(0));\n        boolean oddMatch = (s1.charAt(1)\
        \ == s2.charAt(1) && s1.charAt(3) == s2.charAt(3)) ||\n                    \
        \     (s1.charAt(1) == s2.charAt(3) && s1.charAt(3) == s2.charAt(1));\n    \
        \    return evenMatch && oddMatch;\n    }\n}"
      python: "class Solution(object):\n    def canBeEqual(self, s1, s2):\n        \"\
        \"\"\n        :type s1: str\n        :type s2: str\n        :rtype: bool\n \
        \       \"\"\"\n        even_match = (s1[0] == s2[0] and s1[2] == s2[2]) or\
        \ (s1[0] == s2[2] and s1[2] == s2[0])\n        odd_match = (s1[1] == s2[1] and\
        \ s1[3] == s2[3]) or (s1[1] == s2[3] and s1[3] == s2[1])\n        return even_match\
        \ and odd_match"
      python3: "class Solution:\n    def canBeEqual(self, s1: str, s2: str) -> bool:\n\
        \        even_match = (s1[0] == s2[0] and s1[2] == s2[2]) or (s1[0] == s2[2]\
        \ and s1[2] == s2[0])\n        odd_match = (s1[1] == s2[1] and s1[3] == s2[3])\
        \ or (s1[1] == s2[3] and s1[3] == s2[1])\n        return even_match and odd_match"
      c: "bool canBeEqual(char* s1, char* s2) {\n    bool evenMatch = (s1[0] == s2[0]\
        \ && s1[2] == s2[2]) || (s1[0] == s2[2] && s1[2] == s2[0]);\n    bool oddMatch\
        \ = (s1[1] == s2[1] && s1[3] == s2[3]) || (s1[1] == s2[3] && s1[3] == s2[1]);\n\
        \    return evenMatch && oddMatch;\n}"
      csharp: "public class Solution {\n    public bool CanBeEqual(string s1, string\
        \ s2) {\n        bool evenMatch = (s1[0] == s2[0] && s1[2] == s2[2]) || (s1[0]\
        \ == s2[2] && s1[2] == s2[0]);\n        bool oddMatch = (s1[1] == s2[1] && s1[3]\
        \ == s2[3]) || (s1[1] == s2[3] && s1[3] == s2[1]);\n        return evenMatch\
        \ && oddMatch;\n    }\n}"
      javascript: "/**\n * @param {string} s1\n * @param {string} s2\n * @return {boolean}\n\
        \ */\nvar canBeEqual = function(s1, s2) {\n    let evenMatch = (s1[0] === s2[0]\
        \ && s1[2] === s2[2]) || (s1[0] === s2[2] && s1[2] === s2[0]);\n    let oddMatch\
        \ = (s1[1] === s2[1] && s1[3] === s2[3]) || (s1[1] === s2[3] && s1[3] === s2[1]);\n\
        \    return evenMatch && oddMatch;\n};"
      typescript: "function canBeEqual(s1: string, s2: string): boolean {\n    return\
        \ ((s1[0] === s2[0] && s1[2] === s2[2]) || (s1[0] === s2[2] && s1[2] === s2[0]))\
        \ &&\n           ((s1[1] === s2[1] && s1[3] === s2[3]) || (s1[1] === s2[3] &&\
        \ s1[3] === s2[1]));\n};"
      php: "class Solution {\n    /**\n     * @param String $s1\n     * @param String\
        \ $s2\n     * @return Boolean\n     */\n    function canBeEqual($s1, $s2) {\n\
        \        return (($s1[0] == $s2[0] && $s1[2] == $s2[2]) || ($s1[0] == $s2[2]\
        \ && $s1[2] == $s2[0])) &&\n               (($s1[1] == $s2[1] && $s1[3] == $s2[3])\
        \ || ($s1[1] == $s2[3] && $s1[3] == $s2[1]));\n    }\n}"
      swift: "class Solution {\n    func canBeEqual(_ s1: String, _ s2: String) -> Bool\
        \ {\n        let a = Array(s1), b = Array(s2)\n        return ((a[0] == b[0]\
        \ && a[2] == b[2]) || (a[0] == b[2] && a[2] == b[0])) &&\n               ((a[1]\
        \ == b[1] && a[3] == b[3]) || (a[1] == b[3] && a[3] == b[1]))\n    }\n}"
      kotlin: "class Solution {\n    fun canBeEqual(s1: String, s2: String): Boolean\
        \ {\n        return ((s1[0] == s2[0] && s1[2] == s2[2]) || (s1[0] == s2[2] &&\
        \ s1[2] == s2[0])) &&\n               ((s1[1] == s2[1] && s1[3] == s2[3]) ||\
        \ (s1[1] == s2[3] && s1[3] == s2[1]))\n    }\n}"
      dart: "class Solution {\n  bool canBeEqual(String s1, String s2) {\n    return\
        \ ((s1[0] == s2[0] && s1[2] == s2[2]) || (s1[0] == s2[2] && s1[2] == s2[0]))\
        \ &&\n           ((s1[1] == s2[1] && s1[3] == s2[3]) || (s1[1] == s2[3] && s1[3]\
        \ == s2[1]));\n  }\n}"
      go: "func canBeEqual(s1 string, s2 string) bool {\n    return ((s1[0] == s2[0]\
        \ && s1[2] == s2[2]) || (s1[0] == s2[2] && s1[2] == s2[0])) &&\n           ((s1[1]\
        \ == s2[1] && s1[3] == s2[3]) || (s1[1] == s2[3] && s1[3] == s2[1]))\n}"
      ruby: "def can_be_equal(s1, s2)\n  cond1 = (s1[0] == s2[0] && s1[2] == s2[2])\
        \ || (s1[0] == s2[2] && s1[2] == s2[0])\n  cond2 = (s1[1] == s2[1] && s1[3]\
        \ == s2[3]) || (s1[1] == s2[3] && s1[3] == s2[1])\n  cond1 && cond2\nend"
      scala: "object Solution {\n    def canBeEqual(s1: String, s2: String): Boolean\
        \ = {\n        val cond1 = (s1(0) == s2(0) && s1(2) == s2(2)) || (s1(0) == s2(2)\
        \ && s1(2) == s2(0))\n        val cond2 = (s1(1) == s2(1) && s1(3) == s2(3))\
        \ || (s1(1) == s2(3) && s1(3) == s2(1))\n        cond1 && cond2\n    }\n}"
      rust: "impl Solution {\n    pub fn can_be_equal(s1: String, s2: String) -> bool\
        \ {\n        let b1 = s1.as_bytes();\n        let b2 = s2.as_bytes();\n    \
        \    let cond1 = (b1[0] == b2[0] && b1[2] == b2[2]) || (b1[0] == b2[2] && b1[2]\
        \ == b2[0]);\n        let cond2 = (b1[1] == b2[1] && b1[3] == b2[3]) || (b1[1]\
        \ == b2[3] && b1[3] == b2[1]);\n        cond1 && cond2\n    }\n}"
      racket: "(define/contract (can-be-equal s1 s2)\n  (-> string? string? boolean?)\n\
        \  (let ([c1_0 (string-ref s1 0)]\n        [c1_1 (string-ref s1 1)]\n      \
        \  [c1_2 (string-ref s1 2)]\n        [c1_3 (string-ref s1 3)]\n        [c2_0\
        \ (string-ref s2 0)]\n        [c2_1 (string-ref s2 1)]\n        [c2_2 (string-ref\
        \ s2 2)]\n        [c2_3 (string-ref s2 3)])\n    (and (or (and (char=? c1_0\
        \ c2_0) (char=? c1_2 c2_2))\n             (and (char=? c1_0 c2_2) (char=? c1_2\
        \ c2_0)))\n         (or (and (char=? c1_1 c2_1) (char=? c1_3 c2_3))\n      \
        \       (and (char=? c1_1 c2_3) (char=? c1_3 c2_1))))))"
      erlang: "-spec can_be_equal(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary())\
        \ -> boolean().\ncan_be_equal(S1, S2) ->\n    <<A, B, C, D>> = S1,\n    <<W,\
        \ X, Y, Z>> = S2,\n    Cond1 = ((A =:= W) and (C =:= Y)) or ((A =:= Y) and (C\
        \ =:= W)),\n    Cond2 = ((B =:= X) and (D =:= Z)) or ((B =:= Z) and (D =:= X)),\n\
        \    Cond1 and Cond2."
      elixir: "defmodule Solution do\n  @spec can_be_equal(s1 :: String.t, s2 :: String.t)\
        \ :: boolean\n  def can_be_equal(s1, s2) do\n    <<a, b, c, d>> = s1\n    <<w,\
        \ x, y, z>> = s2\n    cond1 = (a == w and c == y) or (a == y and c == w)\n \
        \   cond2 = (b == x and d == z) or (b == z and d == x)\n    cond1 and cond2\n\
        \  end\nend"
    approach: 'The problem asks whether two strings of length 4 can be made equal by
      swapping characters that are 2 indices apart. This specific constraint means that
      characters at even indices (0 and 2) can only be swapped with each other, and
      characters at odd indices (1 and 3) can only be swapped with each other. Essentially,
      the multiset of characters at indices {0, 2} in s1 must match the multiset of
      characters at indices {0, 2} in s2, and similarly for the odd indices {1, 3}.


      To implement this, we check two conditions. First, for the even indices, s1[0]
      and s1[2] must either be equal to s2[0] and s2[2] respectively, or they must be
      equal when one pair is swapped (s1[0] == s2[2] and s1[2] == s2[0]). Second, we
      perform the same check for the odd indices 1 and 3. If both pairs of positions
      satisfy their respective multiset equality, it is possible to transform s1 into
      s2, and we return true; otherwise, we return false.'
    time_complexity: O(1) because the problem specifically limits the string length
      to a constant value of 4. The algorithm performs a fixed number of character comparisons
      regardless of the contents of the strings.
    space_complexity: O(1) as the solution uses a constant amount of extra space for
      boolean flags and does not require any additional data structures or recursion
      that scales with input size.
    elapsed_time: 107.45527076721191
    model: gemini-3-flash-preview
    generated_at: '2026-03-29 01:49:55 '
---

## Problem #2839: Check if Strings Can be Made Equal With Operations I

**Difficulty:** Easy

**Topics:** String

## Problem Description

<p>You are given two strings <code>s1</code> and <code>s2</code>, both of length <code>4</code>, consisting of <strong>lowercase</strong> English letters.</p>

<p>You can apply the following operation on any of the two strings <strong>any</strong> number of times:</p>

<ul>
	<li>Choose any two indices <code>i</code> and <code>j</code> such that <code>j - i = 2</code>, then <strong>swap</strong> the two characters at those indices in the string.</li>
</ul>

<p>Return <code>true</code><em> if you can make the strings </em><code>s1</code><em> and </em><code>s2</code><em> equal, and </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;abcd&quot;, s2 = &quot;cdab&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> We can do the following operations on s1:
- Choose the indices i = 0, j = 2. The resulting string is s1 = &quot;cbad&quot;.
- Choose the indices i = 1, j = 3. The resulting string is s1 = &quot;cdab&quot; = s2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;abcd&quot;, s2 = &quot;dacb&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> It is not possible to make the two strings equal.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>s1.length == s2.length == 4</code></li>
	<li><code>s1</code> and <code>s2</code> consist only of lowercase English letters.</li>
</ul>


## Hints

1. Since the strings are very small you can try a brute-force approach.

2. There are only `2` different swaps that are possible in a string.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks whether two strings of length 4 can be made equal by swapping characters that are 2 indices apart. This specific constraint means that characters at even indices (0 and 2) can only be swapped with each other, and characters at odd indices (1 and 3) can only be swapped with each other. Essentially, the multiset of characters at indices {0, 2} in s1 must match the multiset of characters at indices {0, 2} in s2, and similarly for the odd indices {1, 3}.

To implement this, we check two conditions. First, for the even indices, s1[0] and s1[2] must either be equal to s2[0] and s2[2] respectively, or they must be equal when one pair is swapped (s1[0] == s2[2] and s1[2] == s2[0]). Second, we perform the same check for the odd indices 1 and 3. If both pairs of positions satisfy their respective multiset equality, it is possible to transform s1 into s2, and we return true; otherwise, we return false.

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
    bool canBeEqual(string s1, string s2) {
        bool evenMatch = (s1[0] == s2[0] && s1[2] == s2[2]) || (s1[0] == s2[2] && s1[2] == s2[0]);
        bool oddMatch = (s1[1] == s2[1] && s1[3] == s2[3]) || (s1[1] == s2[3] && s1[3] == s2[1]);
        return evenMatch && oddMatch;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean canBeEqual(String s1, String s2) {
        boolean evenMatch = (s1.charAt(0) == s2.charAt(0) && s1.charAt(2) == s2.charAt(2)) ||
                          (s1.charAt(0) == s2.charAt(2) && s1.charAt(2) == s2.charAt(0));
        boolean oddMatch = (s1.charAt(1) == s2.charAt(1) && s1.charAt(3) == s2.charAt(3)) ||
                         (s1.charAt(1) == s2.charAt(3) && s1.charAt(3) == s2.charAt(1));
        return evenMatch && oddMatch;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def canBeEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        even_match = (s1[0] == s2[0] and s1[2] == s2[2]) or (s1[0] == s2[2] and s1[2] == s2[0])
        odd_match = (s1[1] == s2[1] and s1[3] == s2[3]) or (s1[1] == s2[3] and s1[3] == s2[1])
        return even_match and odd_match
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        even_match = (s1[0] == s2[0] and s1[2] == s2[2]) or (s1[0] == s2[2] and s1[2] == s2[0])
        odd_match = (s1[1] == s2[1] and s1[3] == s2[3]) or (s1[1] == s2[3] and s1[3] == s2[1])
        return even_match and odd_match
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
bool canBeEqual(char* s1, char* s2) {
    bool evenMatch = (s1[0] == s2[0] && s1[2] == s2[2]) || (s1[0] == s2[2] && s1[2] == s2[0]);
    bool oddMatch = (s1[1] == s2[1] && s1[3] == s2[3]) || (s1[1] == s2[3] && s1[3] == s2[1]);
    return evenMatch && oddMatch;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool CanBeEqual(string s1, string s2) {
        bool evenMatch = (s1[0] == s2[0] && s1[2] == s2[2]) || (s1[0] == s2[2] && s1[2] == s2[0]);
        bool oddMatch = (s1[1] == s2[1] && s1[3] == s2[3]) || (s1[1] == s2[3] && s1[3] == s2[1]);
        return evenMatch && oddMatch;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var canBeEqual = function(s1, s2) {
    let evenMatch = (s1[0] === s2[0] && s1[2] === s2[2]) || (s1[0] === s2[2] && s1[2] === s2[0]);
    let oddMatch = (s1[1] === s2[1] && s1[3] === s2[3]) || (s1[1] === s2[3] && s1[3] === s2[1]);
    return evenMatch && oddMatch;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function canBeEqual(s1: string, s2: string): boolean {
    return ((s1[0] === s2[0] && s1[2] === s2[2]) || (s1[0] === s2[2] && s1[2] === s2[0])) &&
           ((s1[1] === s2[1] && s1[3] === s2[3]) || (s1[1] === s2[3] && s1[3] === s2[1]));
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    /**
     * @param String $s1
     * @param String $s2
     * @return Boolean
     */
    function canBeEqual($s1, $s2) {
        return (($s1[0] == $s2[0] && $s1[2] == $s2[2]) || ($s1[0] == $s2[2] && $s1[2] == $s2[0])) &&
               (($s1[1] == $s2[1] && $s1[3] == $s2[3]) || ($s1[1] == $s2[3] && $s1[3] == $s2[1]));
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func canBeEqual(_ s1: String, _ s2: String) -> Bool {
        let a = Array(s1), b = Array(s2)
        return ((a[0] == b[0] && a[2] == b[2]) || (a[0] == b[2] && a[2] == b[0])) &&
               ((a[1] == b[1] && a[3] == b[3]) || (a[1] == b[3] && a[3] == b[1]))
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun canBeEqual(s1: String, s2: String): Boolean {
        return ((s1[0] == s2[0] && s1[2] == s2[2]) || (s1[0] == s2[2] && s1[2] == s2[0])) &&
               ((s1[1] == s2[1] && s1[3] == s2[3]) || (s1[1] == s2[3] && s1[3] == s2[1]))
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool canBeEqual(String s1, String s2) {
    return ((s1[0] == s2[0] && s1[2] == s2[2]) || (s1[0] == s2[2] && s1[2] == s2[0])) &&
           ((s1[1] == s2[1] && s1[3] == s2[3]) || (s1[1] == s2[3] && s1[3] == s2[1]));
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func canBeEqual(s1 string, s2 string) bool {
    return ((s1[0] == s2[0] && s1[2] == s2[2]) || (s1[0] == s2[2] && s1[2] == s2[0])) &&
           ((s1[1] == s2[1] && s1[3] == s2[3]) || (s1[1] == s2[3] && s1[3] == s2[1]))
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def can_be_equal(s1, s2)
  cond1 = (s1[0] == s2[0] && s1[2] == s2[2]) || (s1[0] == s2[2] && s1[2] == s2[0])
  cond2 = (s1[1] == s2[1] && s1[3] == s2[3]) || (s1[1] == s2[3] && s1[3] == s2[1])
  cond1 && cond2
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def canBeEqual(s1: String, s2: String): Boolean = {
        val cond1 = (s1(0) == s2(0) && s1(2) == s2(2)) || (s1(0) == s2(2) && s1(2) == s2(0))
        val cond2 = (s1(1) == s2(1) && s1(3) == s2(3)) || (s1(1) == s2(3) && s1(3) == s2(1))
        cond1 && cond2
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn can_be_equal(s1: String, s2: String) -> bool {
        let b1 = s1.as_bytes();
        let b2 = s2.as_bytes();
        let cond1 = (b1[0] == b2[0] && b1[2] == b2[2]) || (b1[0] == b2[2] && b1[2] == b2[0]);
        let cond2 = (b1[1] == b2[1] && b1[3] == b2[3]) || (b1[1] == b2[3] && b1[3] == b2[1]);
        cond1 && cond2
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (can-be-equal s1 s2)
  (-> string? string? boolean?)
  (let ([c1_0 (string-ref s1 0)]
        [c1_1 (string-ref s1 1)]
        [c1_2 (string-ref s1 2)]
        [c1_3 (string-ref s1 3)]
        [c2_0 (string-ref s2 0)]
        [c2_1 (string-ref s2 1)]
        [c2_2 (string-ref s2 2)]
        [c2_3 (string-ref s2 3)])
    (and (or (and (char=? c1_0 c2_0) (char=? c1_2 c2_2))
             (and (char=? c1_0 c2_2) (char=? c1_2 c2_0)))
         (or (and (char=? c1_1 c2_1) (char=? c1_3 c2_3))
             (and (char=? c1_1 c2_3) (char=? c1_3 c2_1))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec can_be_equal(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary()) -> boolean().
can_be_equal(S1, S2) ->
    <<A, B, C, D>> = S1,
    <<W, X, Y, Z>> = S2,
    Cond1 = ((A =:= W) and (C =:= Y)) or ((A =:= Y) and (C =:= W)),
    Cond2 = ((B =:= X) and (D =:= Z)) or ((B =:= Z) and (D =:= X)),
    Cond1 and Cond2.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec can_be_equal(s1 :: String.t, s2 :: String.t) :: boolean
  def can_be_equal(s1, s2) do
    <<a, b, c, d>> = s1
    <<w, x, y, z>> = s2
    cond1 = (a == w and c == y) or (a == y and c == w)
    cond2 = (b == x and d == z) or (b == z and d == x)
    cond1 and cond2
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(1) because the problem specifically limits the string length to a constant value of 4. The algorithm performs a fixed number of character comparisons regardless of the contents of the strings.
- **Space Complexity:** O(1) as the solution uses a constant amount of extra space for boolean flags and does not require any additional data structures or recursion that scales with input size.
