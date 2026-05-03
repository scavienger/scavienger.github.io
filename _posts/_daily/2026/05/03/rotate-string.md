---
layout: post
title: "Rotate String"
date: 2026-05-03 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["String", "String Matching"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/rotate-string/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool rotateString(string s, string goal)\
        \ {\n        if (s.length() != goal.length()) return false;\n        string\
        \ doubled = s + s;\n        return doubled.find(goal) != string::npos;\n   \
        \ }\n};"
      java: "class Solution {\n    public boolean rotateString(String s, String goal)\
        \ {\n        if (s.length() != goal.length()) return false;\n        String\
        \ doubled = s + s;\n        return doubled.contains(goal);\n    }\n}"
      python: "class Solution(object):\n    def rotateString(self, s, goal):\n     \
        \   \"\"\"\n        :type s: str\n        :type goal: str\n        :rtype: bool\n\
        \        \"\"\"\n        if len(s) != len(goal):\n            return False\n\
        \        return goal in (s + s)"
      python3: "class Solution:\n    def rotateString(self, s: str, goal: str) -> bool:\n\
        \        if len(s) != len(goal):\n            return False\n        return goal\
        \ in (s + s)"
      c: "#include <string.h>\n#include <stdbool.h>\n\nbool rotateString(char* s, char*\
        \ goal) {\n    size_t n = strlen(s);\n    size_t m = strlen(goal);\n    if (n\
        \ != m) return false;\n    if (n == 0) return true;\n    char doubled[201];\n\
        \    strcpy(doubled, s);\n    strcat(doubled, s);\n    return strstr(doubled,\
        \ goal) != NULL;\n}"
      csharp: "public class Solution {\n    public bool RotateString(string s, string\
        \ goal) {\n        if (s.Length != goal.Length) return false;\n        string\
        \ doubled = s + s;\n        return doubled.Contains(goal);\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @param {string} goal\n * @return {boolean}\n\
        \ */\nvar rotateString = function(s, goal) {\n    if (s.length !== goal.length)\
        \ return false;\n    let doubled = s + s;\n    return doubled.includes(goal);\n\
        };"
      typescript: "function rotateString(s: string, goal: string): boolean {\n    return\
        \ s.length === goal.length && (s + s).includes(goal);\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @param String\
        \ $goal\n     * @return Boolean\n     */\n    function rotateString($s, $goal)\
        \ {\n        return strlen($s) === strlen($goal) && strpos($s . $s, $goal) !==\
        \ false;\n    }\n}"
      swift: "class Solution {\n    func rotateString(_ s: String, _ goal: String) ->\
        \ Bool {\n        return s.count == goal.count && (s + s).contains(goal)\n \
        \   }\n}"
      kotlin: "class Solution {\n    fun rotateString(s: String, goal: String): Boolean\
        \ {\n        return s.length == goal.length && (s + s).contains(goal)\n    }\n\
        }"
      dart: "class Solution {\n  bool rotateString(String s, String goal) {\n    return\
        \ s.length == goal.length && (s + s).contains(goal);\n  }\n}"
      go: "import \"strings\"\n\nfunc rotateString(s string, goal string) bool {\n \
        \   return len(s) == len(goal) && strings.Contains(s + s, goal)\n}"
      ruby: "# @param {String} s\n# @param {String} goal\n# @return {Boolean}\ndef rotate_string(s,\
        \ goal)\n  s.length == goal.length && (s + s).include?(goal)\nend"
      scala: "object Solution {\n    def rotateString(s: String, goal: String): Boolean\
        \ = {\n        s.length == goal.length && (s + s).contains(goal)\n    }\n}"
      rust: "impl Solution {\n    pub fn rotate_string(s: String, goal: String) -> bool\
        \ {\n        s.len() == goal.len() && (s.clone() + &s).contains(&goal)\n   \
        \ }\n}"
      racket: "(define/contract (rotate-string s goal)\n  (-> string? string? boolean?)\n\
        \  (and (= (string-length s) (string-length goal))\n       (regexp-match? (regexp-quote\
        \ goal) (string-append s s))))"
      erlang: "-spec rotate_string(S :: unicode:unicode_binary(), Goal :: unicode:unicode_binary())\
        \ -> boolean().\nrotate_string(S, Goal) ->\n  (byte_size(S) =:= byte_size(Goal))\
        \ andalso (binary:match(<<S/binary, S/binary>>, Goal) =/= nomatch)."
      elixir: "defmodule Solution do\n  @spec rotate_string(s :: String.t, goal :: String.t)\
        \ :: boolean\n  def rotate_string(s, goal) do\n    String.length(s) == String.length(goal)\
        \ and String.contains?(s <> s, goal)\n  end\nend"
    approach: 'To determine if one string is a rotation of another, the fundamental
      intuition is that every cyclic shift of a string s of length N is always a substring
      of the doubled string (s + s). For instance, if s is "abcde", the concatenated
      string "abcdeabcde" contains all possible rotations such as "abcde", "bcdea",
      "cdeab", "deabc", and "eabcd" as contiguous substrings. Thus, the problem is simplified
      to checking if goal is a substring of the concatenated string s + s.


      The algorithm first checks if the lengths of s and goal are equal; if they match,
      it proceeds to search for goal within s + s using a standard substring search
      function. If the lengths are different, s can never be transformed into goal via
      shifts, and the function returns false. This approach is highly efficient given
      the constraints and elegantly covers all cyclic permutations in a single search
      pass.'
    time_complexity: O(N^2) where N is the length of the string s. The algorithm involves
      concatenating s with itself to form a string of length 2N, which takes O(N) time.
      The subsequent substring search (like contains, in, or strstr) has a worst-case
      time complexity of O(N * M) in many standard library implementations, where M
      is the length of the pattern (goal). Since both lengths are equal to N, the overall
      worst-case complexity is O(N^2).
    space_complexity: O(N) where N is the length of the string s. This is because a
      new temporary string of length 2N is created to store the result of the concatenation
      (s + s), which is necessary to perform the substring search.
    elapsed_time: 124.68039202690125
    model: gemini-3-flash-preview
    generated_at: '2026-05-03 02:10:24 '
---

## Problem #796: Rotate String

**Difficulty:** Easy

**Topics:** String, String Matching

## Problem Description

<p>Given two strings <code>s</code> and <code>goal</code>, return <code>true</code> <em>if and only if</em> <code>s</code> <em>can become</em> <code>goal</code> <em>after some number of <strong>shifts</strong> on</em> <code>s</code>.</p>

<p>A <strong>shift</strong> on <code>s</code> consists of moving the leftmost character of <code>s</code> to the rightmost position.</p>

<ul>
	<li>For example, if <code>s = &quot;abcde&quot;</code>, then it will be <code>&quot;bcdea&quot;</code> after one shift.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "abcde", goal = "cdeab"
<strong>Output:</strong> true
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "abcde", goal = "abced"
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, goal.length &lt;= 100</code></li>
	<li><code>s</code> and <code>goal</code> consist of lowercase English letters.</li>
</ul>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To determine if one string is a rotation of another, the fundamental intuition is that every cyclic shift of a string s of length N is always a substring of the doubled string (s + s). For instance, if s is "abcde", the concatenated string "abcdeabcde" contains all possible rotations such as "abcde", "bcdea", "cdeab", "deabc", and "eabcd" as contiguous substrings. Thus, the problem is simplified to checking if goal is a substring of the concatenated string s + s.

The algorithm first checks if the lengths of s and goal are equal; if they match, it proceeds to search for goal within s + s using a standard substring search function. If the lengths are different, s can never be transformed into goal via shifts, and the function returns false. This approach is highly efficient given the constraints and elegantly covers all cyclic permutations in a single search pass.

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
    bool rotateString(string s, string goal) {
        if (s.length() != goal.length()) return false;
        string doubled = s + s;
        return doubled.find(goal) != string::npos;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean rotateString(String s, String goal) {
        if (s.length() != goal.length()) return false;
        String doubled = s + s;
        return doubled.contains(goal);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False
        return goal in (s + s)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return goal in (s + s)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <string.h>
#include <stdbool.h>

bool rotateString(char* s, char* goal) {
    size_t n = strlen(s);
    size_t m = strlen(goal);
    if (n != m) return false;
    if (n == 0) return true;
    char doubled[201];
    strcpy(doubled, s);
    strcat(doubled, s);
    return strstr(doubled, goal) != NULL;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool RotateString(string s, string goal) {
        if (s.Length != goal.Length) return false;
        string doubled = s + s;
        return doubled.Contains(goal);
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
 * @param {string} goal
 * @return {boolean}
 */
var rotateString = function(s, goal) {
    if (s.length !== goal.length) return false;
    let doubled = s + s;
    return doubled.includes(goal);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function rotateString(s: string, goal: string): boolean {
    return s.length === goal.length && (s + s).includes(goal);
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
     * @param String $goal
     * @return Boolean
     */
    function rotateString($s, $goal) {
        return strlen($s) === strlen($goal) && strpos($s . $s, $goal) !== false;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func rotateString(_ s: String, _ goal: String) -> Bool {
        return s.count == goal.count && (s + s).contains(goal)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun rotateString(s: String, goal: String): Boolean {
        return s.length == goal.length && (s + s).contains(goal)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool rotateString(String s, String goal) {
    return s.length == goal.length && (s + s).contains(goal);
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "strings"

func rotateString(s string, goal string) bool {
    return len(s) == len(goal) && strings.Contains(s + s, goal)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @param {String} goal
# @return {Boolean}
def rotate_string(s, goal)
  s.length == goal.length && (s + s).include?(goal)
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def rotateString(s: String, goal: String): Boolean = {
        s.length == goal.length && (s + s).contains(goal)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn rotate_string(s: String, goal: String) -> bool {
        s.len() == goal.len() && (s.clone() + &s).contains(&goal)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (rotate-string s goal)
  (-> string? string? boolean?)
  (and (= (string-length s) (string-length goal))
       (regexp-match? (regexp-quote goal) (string-append s s))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec rotate_string(S :: unicode:unicode_binary(), Goal :: unicode:unicode_binary()) -> boolean().
rotate_string(S, Goal) ->
  (byte_size(S) =:= byte_size(Goal)) andalso (binary:match(<<S/binary, S/binary>>, Goal) =/= nomatch).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec rotate_string(s :: String.t, goal :: String.t) :: boolean
  def rotate_string(s, goal) do
    String.length(s) == String.length(goal) and String.contains?(s <> s, goal)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N^2) where N is the length of the string s. The algorithm involves concatenating s with itself to form a string of length 2N, which takes O(N) time. The subsequent substring search (like contains, in, or strstr) has a worst-case time complexity of O(N * M) in many standard library implementations, where M is the length of the pattern (goal). Since both lengths are equal to N, the overall worst-case complexity is O(N^2).
- **Space Complexity:** O(N) where N is the length of the string s. This is because a new temporary string of length 2N is created to store the result of the concatenation (s + s), which is necessary to perform the substring search.
