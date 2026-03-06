---
layout: post
title: "Check if Binary String Has at Most One Segment of Ones"
date: 2026-03-06 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["String"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool checkOnesSegment(string s) {\n     \
        \   return s.find(\"01\") == string::npos;\n    }\n};"
      java: "class Solution {\n    public boolean checkOnesSegment(String s) {\n   \
        \     return !s.contains(\"01\");\n    }\n}"
      python: "class Solution(object):\n    def checkOnesSegment(self, s):\n       \
        \ \"\"\"\n        :type s: str\n        :rtype: bool\n        \"\"\"\n     \
        \   return \"01\" not in s"
      python3: "class Solution:\n    def checkOnesSegment(self, s: str) -> bool:\n \
        \       return \"01\" not in s"
      c: "bool checkOnesSegment(char* s) {\n    for (int i = 0; s[i] != '\\0' && s[i+1]\
        \ != '\\0'; i++) {\n        if (s[i] == '0' && s[i+1] == '1') {\n          \
        \  return false;\n        }\n    }\n    return true;\n}"
      csharp: "public class Solution {\n    public bool CheckOnesSegment(string s) {\n\
        \        return !s.Contains(\"01\");\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {boolean}\n */\nvar checkOnesSegment\
        \ = function(s) {\n    return !s.includes(\"01\");\n};"
      typescript: "function checkOnesSegment(s: string): boolean {\n    return !s.includes(\"\
        01\");\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return Boolean\n\
        \     */\n    function checkOnesSegment($s) {\n        return strpos($s, \"\
        01\") === false;\n    }\n}"
      swift: "class Solution {\n    func checkOnesSegment(_ s: String) -> Bool {\n \
        \       return !s.contains(\"01\")\n    }\n}"
      kotlin: "class Solution {\n    fun checkOnesSegment(s: String): Boolean {\n  \
        \      return !s.contains(\"01\")\n    }\n}"
      dart: "class Solution {\n  bool checkOnesSegment(String s) {\n    return !s.contains(\"\
        01\");\n  }\n}"
      go: "func checkOnesSegment(s string) bool {\n    for i := 1; i < len(s); i++ {\n\
        \        if s[i-1] == '0' && s[i] == '1' {\n            return false\n     \
        \   }\n    }\n    return true\n}"
      ruby: "# @param {String} s\n# @return {Boolean}\ndef check_ones_segment(s)\n \
        \ !s.include?(\"01\")\nend"
      scala: "object Solution {\n    def checkOnesSegment(s: String): Boolean = {\n\
        \        !s.contains(\"01\")\n    }\n}"
      rust: "impl Solution {\n    pub fn check_ones_segment(s: String) -> bool {\n \
        \       !s.contains(\"01\")\n    }\n}"
      racket: "(define/contract (check-ones-segment s)\n  (-> string? boolean?)\n  (not\
        \ (regexp-match? \"01\" s))\n  )"
      erlang: "-spec check_ones_segment(S :: unicode:unicode_binary()) -> boolean().\n\
        check_ones_segment(S) ->\n  binary:match(S, <<\"01\">>) =:= nomatch."
      elixir: "defmodule Solution do\n  @spec check_ones_segment(s :: String.t) :: boolean\n\
        \  def check_ones_segment(s) do\n    !String.contains?(s, \"01\")\n  end\nend"
    approach: 'The problem asks to determine if a binary string s, which starts with
      ''1'', contains at most one contiguous segment of ones. Since the string is guaranteed
      to start with a segment of ones, any subsequent segment of ones must be preceded
      by at least one ''0''. Therefore, the condition for having more than one segment
      of ones is the presence of the substring ''01'' within the string.


      To implement this, we can simply iterate through the string or use built-in search
      functions to check if the pattern ''01'' exists. If ''01'' is found, it means
      a ''1'' has appeared after a ''0'', indicating a new segment has started, and
      we return false. If the loop finishes or the search fails without finding ''01'',
      it means all ones are grouped at the beginning, and we return true.'
    time_complexity: O(n), where n is the length of the string. We perform a single
      pass over the string to check for the occurrence of the substring '01'.
    space_complexity: O(1) because we do not allocate any additional data structures
      that scale with the input size; we only use a few constant-sized variables for
      iteration.
    elapsed_time: 332.12868094444275
    model: gemini-3-flash-preview
    generated_at: '2026-03-06 01:31:16 '
---

## Problem #1784: Check if Binary String Has at Most One Segment of Ones

**Difficulty:** Easy

**Topics:** String

## Problem Description

<p>Given a binary string <code>s</code> <strong>​​​​​without leading zeros</strong>, return <code>true</code>​​​ <em>if </em><code>s</code><em> contains <strong>at most one contiguous segment of ones</strong></em>. Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;1001&quot;
<strong>Output:</strong> false
<strong>Explanation: </strong>The ones do not form a contiguous segment.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;110&quot;
<strong>Output:</strong> true</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s[i]</code>​​​​ is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
	<li><code>s[0]</code> is&nbsp;<code>&#39;1&#39;</code>.</li>
</ul>


## Hints

1. It's guaranteed to have at least one segment

2. The string size is small so you can count all segments of ones with no that have no adjacent ones.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks to determine if a binary string s, which starts with '1', contains at most one contiguous segment of ones. Since the string is guaranteed to start with a segment of ones, any subsequent segment of ones must be preceded by at least one '0'. Therefore, the condition for having more than one segment of ones is the presence of the substring '01' within the string.

To implement this, we can simply iterate through the string or use built-in search functions to check if the pattern '01' exists. If '01' is found, it means a '1' has appeared after a '0', indicating a new segment has started, and we return false. If the loop finishes or the search fails without finding '01', it means all ones are grouped at the beginning, and we return true.

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
    bool checkOnesSegment(string s) {
        return s.find("01") == string::npos;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean checkOnesSegment(String s) {
        return !s.contains("01");
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return "01" not in s
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
bool checkOnesSegment(char* s) {
    for (int i = 0; s[i] != '\0' && s[i+1] != '\0'; i++) {
        if (s[i] == '0' && s[i+1] == '1') {
            return false;
        }
    }
    return true;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool CheckOnesSegment(string s) {
        return !s.Contains("01");
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
 * @return {boolean}
 */
var checkOnesSegment = function(s) {
    return !s.includes("01");
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function checkOnesSegment(s: string): boolean {
    return !s.includes("01");
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
     * @return Boolean
     */
    function checkOnesSegment($s) {
        return strpos($s, "01") === false;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func checkOnesSegment(_ s: String) -> Bool {
        return !s.contains("01")
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun checkOnesSegment(s: String): Boolean {
        return !s.contains("01")
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool checkOnesSegment(String s) {
    return !s.contains("01");
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func checkOnesSegment(s string) bool {
    for i := 1; i < len(s); i++ {
        if s[i-1] == '0' && s[i] == '1' {
            return false
        }
    }
    return true
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @return {Boolean}
def check_ones_segment(s)
  !s.include?("01")
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def checkOnesSegment(s: String): Boolean = {
        !s.contains("01")
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn check_ones_segment(s: String) -> bool {
        !s.contains("01")
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (check-ones-segment s)
  (-> string? boolean?)
  (not (regexp-match? "01" s))
  )
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec check_ones_segment(S :: unicode:unicode_binary()) -> boolean().
check_ones_segment(S) ->
  binary:match(S, <<"01">>) =:= nomatch.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec check_ones_segment(s :: String.t) :: boolean
  def check_ones_segment(s) do
    !String.contains?(s, "01")
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n), where n is the length of the string. We perform a single pass over the string to check for the occurrence of the substring '01'.
- **Space Complexity:** O(1) because we do not allocate any additional data structures that scale with the input size; we only use a few constant-sized variables for iteration.
