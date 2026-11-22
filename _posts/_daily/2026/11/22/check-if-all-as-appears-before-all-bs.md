---
layout: post
title: "Check if All A's Appears Before All B's"
date: 2026-11-22 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["String"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool checkString(string s) {\n        for\
        \ (int i = 0; i + 1 < (int)s.length(); i++) {\n            if (s[i] == 'b' &&\
        \ s[i + 1] == 'a') {\n                return false;\n            }\n       \
        \ }\n        return true;\n    }\n};"
      java: "class Solution {\n    public boolean checkString(String s) {\n        return\
        \ !s.contains(\"ba\");\n    }\n}"
      python: "class Solution(object):\n    def checkString(self, s):\n        \"\"\"\
        \n        :type s: str\n        :rtype: bool\n        \"\"\"\n        return\
        \ \"ba\" not in s"
      python3: "class Solution:\n    def checkString(self, s: str) -> bool:\n      \
        \  return \"ba\" not in s"
      c: "bool checkString(char* s) {\n    for (int i = 0; s[i] != '\\0' && s[i + 1]\
        \ != '\\0'; i++) {\n        if (s[i] == 'b' && s[i + 1] == 'a') {\n        \
        \    return false;\n        }\n    }\n    return true;\n}"
      csharp: "public class Solution {\n    public bool CheckString(string s) {\n  \
        \      return !s.Contains(\"ba\");\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {boolean}\n */\nvar checkString\
        \ = function(s) {\n    return !s.includes(\"ba\");\n};"
      typescript: "function checkString(s: string): boolean {\n    return !s.includes(\"\
        ba\");\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return Boolean\n\
        \     */\n    function checkString($s) {\n        return strpos($s, \"ba\")\
        \ === false;\n    }\n}"
      swift: "class Solution {\n    func checkString(_ s: String) -> Bool {\n      \
        \  return !s.contains(\"ba\")\n    }\n}"
      kotlin: "class Solution {\n    fun checkString(s: String): Boolean {\n       \
        \ return !s.contains(\"ba\")\n    }\n}"
      dart: "class Solution {\n  bool checkString(String s) {\n    return !s.contains(\"\
        ba\");\n  }\n}"
      go: "func checkString(s string) bool {\n    for i := 0; i < len(s) - 1; i++ {\n\
        \        if s[i] == 'b' && s[i+1] == 'a' {\n            return false\n     \
        \   }\n    }\n    return true\n}"
      ruby: "# @param {String} s\n# @return {Boolean}\ndef check_string(s)\n  !s.include?(\"\
        ba\")\nend"
      scala: "object Solution {\n    def checkString(s: String): Boolean = {\n     \
        \   !s.contains(\"ba\")\n    }\n}"
      rust: "impl Solution {\n    pub fn check_string(s: String) -> bool {\n       \
        \ !s.contains(\"ba\")\n    }\n}"
      racket: "(define/contract (check-string s)\n  (-> string? boolean?)\n  (not (string-contains?\
        \ s \"ba\"))\n  )"
      erlang: "-spec check_string(S :: unicode:unicode_binary()) -> boolean().\ncheck_string(S)\
        \ ->\n  binary:match(S, <<\"ba\">>) =:= nomatch."
      elixir: "defmodule Solution do\n  @spec check_string(s :: String.t) :: boolean\n\
        \  def check_string(s) do\n    not String.contains?(s, \"ba\")\n  end\nend"
    approach: 'The core intuition behind this problem is that the condition "every ''a''
      appears before every ''b''" is equivalent to saying that the string is sorted
      in non-decreasing order lexicographically. Since the string only contains the
      characters ''a'' and ''b'', and ''a'' comes before ''b'' in alphabetical order,
      any occurrence where an ''a'' appears after a ''b'' would violate the condition.
      This violation is effectively captured by the presence of the substring ''ba''.


      To implement this, we check if the substring ''ba'' exists in the given string.
      This can be achieved by a single linear scan through the string to see if any
      character ''b'' is immediately followed by ''a'', or by using built-in string
      search functions like ''contains'' or ''includes''. If no such occurrence is found,
      the string satisfies the condition and we return true. This approach correctly
      handles edge cases where the string consists of only one type of character or
      contains only a single character.'
    time_complexity: O(n), where n is the length of the string. The algorithm performs
      a single pass through the string to check for the presence of the substring 'ba',
      which takes linear time relative to the length of the input.
    space_complexity: O(1). Only a constant amount of extra space is used for loop variables
      or temporary flags, regardless of the size of the input string.
    elapsed_time: 151.40083122253418
    model: gemini-3-flash-preview
    generated_at: '2026-11-22 04:26:10 '
---

## Problem #2124: Check if All A's Appears Before All B's

**Difficulty:** Easy

**Topics:** String

## Problem Description

<p>Given a string <code>s</code> consisting of <strong>only</strong> the characters <code>&#39;a&#39;</code> and <code>&#39;b&#39;</code>, return <code>true</code> <em>if <strong>every</strong> </em><code>&#39;a&#39;</code> <em>appears before <strong>every</strong> </em><code>&#39;b&#39;</code><em> in the string</em>. Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aaabbb&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong>
The &#39;a&#39;s are at indices 0, 1, and 2, while the &#39;b&#39;s are at indices 3, 4, and 5.
Hence, every &#39;a&#39; appears before every &#39;b&#39; and we return true.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abab&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong>
There is an &#39;a&#39; at index 2 and a &#39;b&#39; at index 1.
Hence, not every &#39;a&#39; appears before every &#39;b&#39; and we return false.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bbb&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong>
There are no &#39;a&#39;s, hence, every &#39;a&#39; appears before every &#39;b&#39; and we return true.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s[i]</code> is either <code>&#39;a&#39;</code> or <code>&#39;b&#39;</code>.</li>
</ul>


## Hints

1. You can check the opposite: check if there is a ‘b’ before an ‘a’. Then, negate and return that answer.

2. s should not have any occurrences of “ba” as a substring.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The core intuition behind this problem is that the condition "every 'a' appears before every 'b'" is equivalent to saying that the string is sorted in non-decreasing order lexicographically. Since the string only contains the characters 'a' and 'b', and 'a' comes before 'b' in alphabetical order, any occurrence where an 'a' appears after a 'b' would violate the condition. This violation is effectively captured by the presence of the substring 'ba'.

To implement this, we check if the substring 'ba' exists in the given string. This can be achieved by a single linear scan through the string to see if any character 'b' is immediately followed by 'a', or by using built-in string search functions like 'contains' or 'includes'. If no such occurrence is found, the string satisfies the condition and we return true. This approach correctly handles edge cases where the string consists of only one type of character or contains only a single character.

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
    bool checkString(string s) {
        for (int i = 0; i + 1 < (int)s.length(); i++) {
            if (s[i] == 'b' && s[i + 1] == 'a') {
                return false;
            }
        }
        return true;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean checkString(String s) {
        return !s.contains("ba");
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return "ba" not in s
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def checkString(self, s: str) -> bool:
        return "ba" not in s
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
bool checkString(char* s) {
    for (int i = 0; s[i] != '\0' && s[i + 1] != '\0'; i++) {
        if (s[i] == 'b' && s[i + 1] == 'a') {
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
    public bool CheckString(string s) {
        return !s.Contains("ba");
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
var checkString = function(s) {
    return !s.includes("ba");
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function checkString(s: string): boolean {
    return !s.includes("ba");
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
    function checkString($s) {
        return strpos($s, "ba") === false;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func checkString(_ s: String) -> Bool {
        return !s.contains("ba")
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun checkString(s: String): Boolean {
        return !s.contains("ba")
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool checkString(String s) {
    return !s.contains("ba");
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func checkString(s string) bool {
    for i := 0; i < len(s) - 1; i++ {
        if s[i] == 'b' && s[i+1] == 'a' {
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
def check_string(s)
  !s.include?("ba")
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def checkString(s: String): Boolean = {
        !s.contains("ba")
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn check_string(s: String) -> bool {
        !s.contains("ba")
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (check-string s)
  (-> string? boolean?)
  (not (string-contains? s "ba"))
  )
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec check_string(S :: unicode:unicode_binary()) -> boolean().
check_string(S) ->
  binary:match(S, <<"ba">>) =:= nomatch.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec check_string(s :: String.t) :: boolean
  def check_string(s) do
    not String.contains?(s, "ba")
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n), where n is the length of the string. The algorithm performs a single pass through the string to check for the presence of the substring 'ba', which takes linear time relative to the length of the input.
- **Space Complexity:** O(1). Only a constant amount of extra space is used for loop variables or temporary flags, regardless of the size of the input string.
