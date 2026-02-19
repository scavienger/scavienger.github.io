---
layout: post
title: "Count Binary Substrings"
date: 2026-02-19 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Two Pointers", "String"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/count-binary-substrings/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int countBinarySubstrings(string s) {\n \
        \       int prev = 0, curr = 1, res = 0;\n        int n = s.length();\n    \
        \    for (int i = 1; i < n; i++) {\n            if (s[i] == s[i - 1]) {\n  \
        \              curr++;\n            } else {\n                res += min(prev,\
        \ curr);\n                prev = curr;\n                curr = 1;\n        \
        \    }\n        }\n        return res + min(prev, curr);\n    }\n};"
      java: "class Solution {\n    public int countBinarySubstrings(String s) {\n  \
        \      int prev = 0, curr = 1, res = 0;\n        int n = s.length();\n     \
        \   for (int i = 1; i < n; i++) {\n            if (s.charAt(i) == s.charAt(i\
        \ - 1)) {\n                curr++;\n            } else {\n                res\
        \ += Math.min(prev, curr);\n                prev = curr;\n                curr\
        \ = 1;\n            }\n        }\n        return res + Math.min(prev, curr);\n\
        \    }\n}"
      python: "class Solution(object):\n    def countBinarySubstrings(self, s):\n  \
        \      \"\"\"\n        :type s: str\n        :rtype: int\n        \"\"\"\n \
        \       prev, curr, res = 0, 1, 0\n        for i in range(1, len(s)):\n    \
        \        if s[i] == s[i-1]:\n                curr += 1\n            else:\n\
        \                res += min(prev, curr)\n                prev, curr = curr,\
        \ 1\n        return res + min(prev, curr)"
      python3: "class Solution:\n    def countBinarySubstrings(self, s: str) -> int:\n\
        \        prev, curr, res = 0, 1, 0\n        for i in range(1, len(s)):\n   \
        \         if s[i] == s[i-1]:\n                curr += 1\n            else:\n\
        \                res += min(prev, curr)\n                prev, curr = curr,\
        \ 1\n        return res + min(prev, curr)"
      c: "int countBinarySubstrings(char* s) {\n    int prev = 0, curr = 1, res = 0;\n\
        \    if (!s || s[0] == '\\0') return 0;\n    for (int i = 1; s[i] != '\\0';\
        \ i++) {\n        if (s[i] == s[i-1]) {\n            curr++;\n        } else\
        \ {\n            res += (prev < curr) ? prev : curr;\n            prev = curr;\n\
        \            curr = 1;\n        }\n    }\n    res += (prev < curr) ? prev :\
        \ curr;\n    return res;\n}"
      csharp: "public class Solution {\n    public int CountBinarySubstrings(string\
        \ s) {\n        int prev = 0, curr = 1, res = 0;\n        int n = s.Length;\n\
        \        for (int i = 1; i < n; i++) {\n            if (s[i] == s[i - 1]) {\n\
        \                curr++;\n            } else {\n                res += Math.Min(prev,\
        \ curr);\n                prev = curr;\n                curr = 1;\n        \
        \    }\n        }\n        return res + Math.Min(prev, curr);\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {number}\n */\nvar countBinarySubstrings\
        \ = function(s) {\n    let prev = 0, curr = 1, res = 0;\n    const n = s.length;\n\
        \    for (let i = 1; i < n; i++) {\n        if (s[i] === s[i - 1]) {\n     \
        \       curr++;\n        } else {\n            res += Math.min(prev, curr);\n\
        \            prev = curr;\n            curr = 1;\n        }\n    }\n    return\
        \ res + Math.min(prev, curr);\n};"
      typescript: "function countBinarySubstrings(s: string): number {\n    let prev\
        \ = 0;\n    let curr = 1;\n    let res = 0;\n    for (let i = 1; i < s.length;\
        \ i++) {\n        if (s[i] === s[i - 1]) {\n            curr++;\n        } else\
        \ {\n            res += Math.min(prev, curr);\n            prev = curr;\n  \
        \          curr = 1;\n        }\n    }\n    return res + Math.min(prev, curr);\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return Integer\n\
        \     */\n    function countBinarySubstrings($s) {\n        $prev = 0;\n   \
        \     $curr = 1;\n        $res = 0;\n        $len = strlen($s);\n        for\
        \ ($i = 1; $i < $len; $i++) {\n            if ($s[$i] == $s[$i - 1]) {\n   \
        \             $curr++;\n            } else {\n                $res += min($prev,\
        \ $curr);\n                $prev = $curr;\n                $curr = 1;\n    \
        \        }\n        }\n        return $res + min($prev, $curr);\n    }\n}"
      swift: "class Solution {\n    func countBinarySubstrings(_ s: String) -> Int {\n\
        \        let chars = Array(s)\n        if chars.count == 0 { return 0 }\n  \
        \      var prev = 0\n        var curr = 1\n        var res = 0\n        for\
        \ i in 1..<chars.count {\n            if chars[i] == chars[i-1] {\n        \
        \        curr += 1\n            } else {\n                res += min(prev, curr)\n\
        \                prev = curr\n                curr = 1\n            }\n    \
        \    }\n        return res + min(prev, curr)\n    }\n}"
      kotlin: "class Solution {\n    fun countBinarySubstrings(s: String): Int {\n \
        \       var prev = 0\n        var curr = 1\n        var res = 0\n        for\
        \ (i in 1 until s.length) {\n            if (s[i] == s[i - 1]) {\n         \
        \       curr++\n            } else {\n                res += Math.min(prev,\
        \ curr)\n                prev = curr\n                curr = 1\n           \
        \ }\n        }\n        return res + Math.min(prev, curr)\n    }\n}"
      dart: "class Solution {\n  int countBinarySubstrings(String s) {\n    int prev\
        \ = 0;\n    int curr = 1;\n    int res = 0;\n    for (int i = 1; i < s.length;\
        \ i++) {\n      if (s[i] == s[i - 1]) {\n        curr++;\n      } else {\n \
        \       res += (prev < curr ? prev : curr);\n        prev = curr;\n        curr\
        \ = 1;\n      }\n    }\n    return res + (prev < curr ? prev : curr);\n  }\n\
        }"
      go: "func countBinarySubstrings(s string) int {\n    prev := 0\n    curr := 1\n\
        \    res := 0\n    for i := 1; i < len(s); i++ {\n        if s[i] == s[i-1]\
        \ {\n            curr++\n        } else {\n            if prev < curr {\n  \
        \              res += prev\n            } else {\n                res += curr\n\
        \            }\n            prev = curr\n            curr = 1\n        }\n \
        \   }\n    if prev < curr {\n        res += prev\n    } else {\n        res\
        \ += curr\n    }\n    return res\n}"
      ruby: "def count_binary_substrings(s)\n  prev = 0\n  curr = 1\n  ans = 0\n  (1...s.length).each\
        \ do |i|\n    if s[i] == s[i - 1]\n      curr += 1\n    else\n      ans += [prev,\
        \ curr].min\n      prev = curr\n      curr = 1\n    end\n  end\n  ans + [prev,\
        \ curr].min\nend"
      scala: "object Solution {\n    def countBinarySubstrings(s: String): Int = {\n\
        \        var prev = 0\n        var curr = 1\n        var ans = 0\n        for\
        \ (i <- 1 until s.length) {\n            if (s(i) == s(i - 1)) {\n         \
        \       curr += 1\n            } else {\n                ans += Math.min(prev,\
        \ curr)\n                prev = curr\n                curr = 1\n           \
        \ }\n        }\n        ans + Math.min(prev, curr)\n    }\n}"
      rust: "impl Solution {\n    pub fn count_binary_substrings(s: String) -> i32 {\n\
        \        let bytes = s.as_bytes();\n        let mut prev = 0;\n        let mut\
        \ curr = 1;\n        let mut ans = 0;\n        for i in 1..bytes.len() {\n \
        \           if bytes[i] == bytes[i - 1] {\n                curr += 1;\n    \
        \        } else {\n                ans += prev.min(curr);\n                prev\
        \ = curr;\n                curr = 1;\n            }\n        }\n        ans\
        \ + prev.min(curr)\n    }\n}"
      racket: "(define/contract (count-binary-substrings s)\n  (-> string? exact-integer?)\n\
        \  (let* ([lst (string->list s)]\n         [get-counts (lambda (chars)\n   \
        \                    (let loop ([chars chars] [curr-char #f] [count 0] [acc\
        \ '()])\n                         (cond\n                           [(null?\
        \ chars) (if (zero? count) acc (reverse (cons count acc)))]\n              \
        \             [(not curr-char) (loop (cdr chars) (car chars) 1 acc)]\n     \
        \                      [(char=? (car chars) curr-char) (loop (cdr chars) curr-char\
        \ (+ count 1) acc)]\n                           [else (loop (cdr chars) (car\
        \ chars) 1 (cons count acc))])))]\n         [counts (get-counts lst)])\n   \
        \ (let sum-loop ([c counts] [ans 0])\n      (if (or (null? c) (null? (cdr c)))\n\
        \          ans\n          (sum-loop (cdr c) (+ ans (min (car c) (cadr c))))))))"
      erlang: "-spec count_binary_substrings(S :: unicode:unicode_binary()) -> integer().\n\
        count_binary_substrings(S) ->\n  L = unicode:characters_to_list(S),\n  Counts\
        \ = get_counts(L, undefined, 0, []),\n  calculate_ans(Counts, 0).\n\nget_counts([],\
        \ _Prev, Count, Acc) -> lists:reverse([Count | Acc]);\nget_counts([H|T], undefined,\
        \ 0, Acc) -> get_counts(T, H, 1, Acc);\nget_counts([H|T], H, Count, Acc) ->\
        \ get_counts(T, H, Count + 1, Acc);\nget_counts([H|T], _Prev, Count, Acc) ->\
        \ get_counts(T, H, 1, [Count | Acc]).\n\ncalculate_ans([C1, C2 | T], Ans) ->\
        \ calculate_ans([C2 | T], Ans + min_val(C1, C2));\ncalculate_ans(_, Ans) ->\
        \ Ans.\n\nmin_val(A, B) when A < B -> A;\nmin_val(_A, B) -> B."
      elixir: "defmodule Solution do\n  @spec count_binary_substrings(s :: String.t)\
        \ :: integer\n  def count_binary_substrings(s) do\n    counts = s\n      |>\
        \ String.to_charlist()\n      |> Enum.chunk_by(& &1)\n      |> Enum.map(&length/1)\n\
        \n    case counts do\n      [] -> 0\n      [_] -> 0\n      _ ->\n        counts\n\
        \        |> Enum.chunk_every(2, 1, :discard)\n        |> Enum.reduce(0, fn [a,\
        \ b], acc -> acc + min(a, b) end)\n    end\n  end\nend"
    approach: 'The problem asks for substrings where 0s and 1s are grouped consecutively
      and appear in equal numbers. The core intuition is that any such substring must
      be formed at the boundary of two blocks of different characters (e.g., a block
      of 0s followed by a block of 1s). For any two adjacent blocks of sizes ''a'' and
      ''b'', the number of valid substrings they can form is equal to the minimum of
      ''a'' and ''b''. For example, if we have ''000'' followed by ''11'', the possible
      valid substrings are ''01'' and ''0011'', which totals 2, or min(3, 2).


      To implement this efficiently, we traverse the string once and count the lengths
      of consecutive character groups. Instead of storing all group lengths in an array,
      we only keep track of the current group''s length and the previous group''s length.
      Every time the character changes, we add the minimum of the previous and current
      lengths to our result, update the previous length to the current length, and reset
      the current length to 1. We also perform a final addition after the loop finishes
      to account for the last pair of groups.'
    time_complexity: 'O(N) with one-paragraph explanation: The algorithm processes the
      string in a single pass of length N, where N is the length of the input string.
      All operations performed inside the loop, such as comparisons and additions, are
      O(1).'
    space_complexity: 'O(1) with one-paragraph explanation: We only use a few integer
      variables (prev, curr, res) to keep track of the counts and the result, regardless
      of the input size. No additional data structures that scale with the input size
      are required.'
    elapsed_time: 85.3885543346405
    model: gemini-3-flash-preview
    generated_at: '2026-02-19 01:27:33 '
---

## Problem #696: Count Binary Substrings

**Difficulty:** Easy

**Topics:** Two Pointers, String

## Problem Description

<p>Given a binary string <code>s</code>, return the number of non-empty substrings that have the same number of <code>0</code>&#39;s and <code>1</code>&#39;s, and all the <code>0</code>&#39;s and all the <code>1</code>&#39;s in these substrings are grouped consecutively.</p>

<p>Substrings that occur multiple times are counted the number of times they occur.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;00110011&quot;
<strong>Output:</strong> 6
<strong>Explanation:</strong> There are 6 substrings that have equal number of consecutive 1&#39;s and 0&#39;s: &quot;0011&quot;, &quot;01&quot;, &quot;1100&quot;, &quot;10&quot;, &quot;0011&quot;, and &quot;01&quot;.
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, &quot;00110011&quot; is not a valid substring because all the 0&#39;s (and 1&#39;s) are not grouped together.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;10101&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 4 substrings: &quot;10&quot;, &quot;01&quot;, &quot;10&quot;, &quot;01&quot; that have equal number of consecutive 1&#39;s and 0&#39;s.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
</ul>


## Hints

1. How many valid binary substrings exist in "000111", and how many in "11100"?  What about "00011100"?

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for substrings where 0s and 1s are grouped consecutively and appear in equal numbers. The core intuition is that any such substring must be formed at the boundary of two blocks of different characters (e.g., a block of 0s followed by a block of 1s). For any two adjacent blocks of sizes 'a' and 'b', the number of valid substrings they can form is equal to the minimum of 'a' and 'b'. For example, if we have '000' followed by '11', the possible valid substrings are '01' and '0011', which totals 2, or min(3, 2).

To implement this efficiently, we traverse the string once and count the lengths of consecutive character groups. Instead of storing all group lengths in an array, we only keep track of the current group's length and the previous group's length. Every time the character changes, we add the minimum of the previous and current lengths to our result, update the previous length to the current length, and reset the current length to 1. We also perform a final addition after the loop finishes to account for the last pair of groups.

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
    int countBinarySubstrings(string s) {
        int prev = 0, curr = 1, res = 0;
        int n = s.length();
        for (int i = 1; i < n; i++) {
            if (s[i] == s[i - 1]) {
                curr++;
            } else {
                res += min(prev, curr);
                prev = curr;
                curr = 1;
            }
        }
        return res + min(prev, curr);
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int countBinarySubstrings(String s) {
        int prev = 0, curr = 1, res = 0;
        int n = s.length();
        for (int i = 1; i < n; i++) {
            if (s.charAt(i) == s.charAt(i - 1)) {
                curr++;
            } else {
                res += Math.min(prev, curr);
                prev = curr;
                curr = 1;
            }
        }
        return res + Math.min(prev, curr);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev, curr, res = 0, 1, 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr += 1
            else:
                res += min(prev, curr)
                prev, curr = curr, 1
        return res + min(prev, curr)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev, curr, res = 0, 1, 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr += 1
            else:
                res += min(prev, curr)
                prev, curr = curr, 1
        return res + min(prev, curr)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int countBinarySubstrings(char* s) {
    int prev = 0, curr = 1, res = 0;
    if (!s || s[0] == '\0') return 0;
    for (int i = 1; s[i] != '\0'; i++) {
        if (s[i] == s[i-1]) {
            curr++;
        } else {
            res += (prev < curr) ? prev : curr;
            prev = curr;
            curr = 1;
        }
    }
    res += (prev < curr) ? prev : curr;
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int CountBinarySubstrings(string s) {
        int prev = 0, curr = 1, res = 0;
        int n = s.Length;
        for (int i = 1; i < n; i++) {
            if (s[i] == s[i - 1]) {
                curr++;
            } else {
                res += Math.Min(prev, curr);
                prev = curr;
                curr = 1;
            }
        }
        return res + Math.Min(prev, curr);
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
var countBinarySubstrings = function(s) {
    let prev = 0, curr = 1, res = 0;
    const n = s.length;
    for (let i = 1; i < n; i++) {
        if (s[i] === s[i - 1]) {
            curr++;
        } else {
            res += Math.min(prev, curr);
            prev = curr;
            curr = 1;
        }
    }
    return res + Math.min(prev, curr);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countBinarySubstrings(s: string): number {
    let prev = 0;
    let curr = 1;
    let res = 0;
    for (let i = 1; i < s.length; i++) {
        if (s[i] === s[i - 1]) {
            curr++;
        } else {
            res += Math.min(prev, curr);
            prev = curr;
            curr = 1;
        }
    }
    return res + Math.min(prev, curr);
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
    function countBinarySubstrings($s) {
        $prev = 0;
        $curr = 1;
        $res = 0;
        $len = strlen($s);
        for ($i = 1; $i < $len; $i++) {
            if ($s[$i] == $s[$i - 1]) {
                $curr++;
            } else {
                $res += min($prev, $curr);
                $prev = $curr;
                $curr = 1;
            }
        }
        return $res + min($prev, $curr);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func countBinarySubstrings(_ s: String) -> Int {
        let chars = Array(s)
        if chars.count == 0 { return 0 }
        var prev = 0
        var curr = 1
        var res = 0
        for i in 1..<chars.count {
            if chars[i] == chars[i-1] {
                curr += 1
            } else {
                res += min(prev, curr)
                prev = curr
                curr = 1
            }
        }
        return res + min(prev, curr)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun countBinarySubstrings(s: String): Int {
        var prev = 0
        var curr = 1
        var res = 0
        for (i in 1 until s.length) {
            if (s[i] == s[i - 1]) {
                curr++
            } else {
                res += Math.min(prev, curr)
                prev = curr
                curr = 1
            }
        }
        return res + Math.min(prev, curr)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int countBinarySubstrings(String s) {
    int prev = 0;
    int curr = 1;
    int res = 0;
    for (int i = 1; i < s.length; i++) {
      if (s[i] == s[i - 1]) {
        curr++;
      } else {
        res += (prev < curr ? prev : curr);
        prev = curr;
        curr = 1;
      }
    }
    return res + (prev < curr ? prev : curr);
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func countBinarySubstrings(s string) int {
    prev := 0
    curr := 1
    res := 0
    for i := 1; i < len(s); i++ {
        if s[i] == s[i-1] {
            curr++
        } else {
            if prev < curr {
                res += prev
            } else {
                res += curr
            }
            prev = curr
            curr = 1
        }
    }
    if prev < curr {
        res += prev
    } else {
        res += curr
    }
    return res
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def count_binary_substrings(s)
  prev = 0
  curr = 1
  ans = 0
  (1...s.length).each do |i|
    if s[i] == s[i - 1]
      curr += 1
    else
      ans += [prev, curr].min
      prev = curr
      curr = 1
    end
  end
  ans + [prev, curr].min
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def countBinarySubstrings(s: String): Int = {
        var prev = 0
        var curr = 1
        var ans = 0
        for (i <- 1 until s.length) {
            if (s(i) == s(i - 1)) {
                curr += 1
            } else {
                ans += Math.min(prev, curr)
                prev = curr
                curr = 1
            }
        }
        ans + Math.min(prev, curr)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn count_binary_substrings(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut prev = 0;
        let mut curr = 1;
        let mut ans = 0;
        for i in 1..bytes.len() {
            if bytes[i] == bytes[i - 1] {
                curr += 1;
            } else {
                ans += prev.min(curr);
                prev = curr;
                curr = 1;
            }
        }
        ans + prev.min(curr)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (count-binary-substrings s)
  (-> string? exact-integer?)
  (let* ([lst (string->list s)]
         [get-counts (lambda (chars)
                       (let loop ([chars chars] [curr-char #f] [count 0] [acc '()])
                         (cond
                           [(null? chars) (if (zero? count) acc (reverse (cons count acc)))]
                           [(not curr-char) (loop (cdr chars) (car chars) 1 acc)]
                           [(char=? (car chars) curr-char) (loop (cdr chars) curr-char (+ count 1) acc)]
                           [else (loop (cdr chars) (car chars) 1 (cons count acc))])))]
         [counts (get-counts lst)])
    (let sum-loop ([c counts] [ans 0])
      (if (or (null? c) (null? (cdr c)))
          ans
          (sum-loop (cdr c) (+ ans (min (car c) (cadr c))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec count_binary_substrings(S :: unicode:unicode_binary()) -> integer().
count_binary_substrings(S) ->
  L = unicode:characters_to_list(S),
  Counts = get_counts(L, undefined, 0, []),
  calculate_ans(Counts, 0).

get_counts([], _Prev, Count, Acc) -> lists:reverse([Count | Acc]);
get_counts([H|T], undefined, 0, Acc) -> get_counts(T, H, 1, Acc);
get_counts([H|T], H, Count, Acc) -> get_counts(T, H, Count + 1, Acc);
get_counts([H|T], _Prev, Count, Acc) -> get_counts(T, H, 1, [Count | Acc]).

calculate_ans([C1, C2 | T], Ans) -> calculate_ans([C2 | T], Ans + min_val(C1, C2));
calculate_ans(_, Ans) -> Ans.

min_val(A, B) when A < B -> A;
min_val(_A, B) -> B.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec count_binary_substrings(s :: String.t) :: integer
  def count_binary_substrings(s) do
    counts = s
      |> String.to_charlist()
      |> Enum.chunk_by(& &1)
      |> Enum.map(&length/1)

    case counts do
      [] -> 0
      [_] -> 0
      _ ->
        counts
        |> Enum.chunk_every(2, 1, :discard)
        |> Enum.reduce(0, fn [a, b], acc -> acc + min(a, b) end)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) with one-paragraph explanation: The algorithm processes the string in a single pass of length N, where N is the length of the input string. All operations performed inside the loop, such as comparisons and additions, are O(1).
- **Space Complexity:** O(1) with one-paragraph explanation: We only use a few integer variables (prev, curr, res) to keep track of the counts and the result, regardless of the input size. No additional data structures that scale with the input size are required.
