---
layout: post
title: "Minimum Deletions to Make String Balanced"
date: 2026-02-07 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Dynamic Programming", "Stack"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minimumDeletions(string s) {\n      \
        \  int deletions = 0;\n        int count_b = 0;\n        for (char c : s) {\n\
        \            if (c == 'b') {\n                count_b++;\n            } else\
        \ {\n                deletions = min(deletions + 1, count_b);\n            }\n\
        \        }\n        return deletions;\n    }\n};"
      java: "class Solution {\n    public int minimumDeletions(String s) {\n       \
        \ int deletions = 0;\n        int countB = 0;\n        for (int i = 0; i < s.length();\
        \ i++) {\n            if (s.charAt(i) == 'b') {\n                countB++;\n\
        \            } else {\n                deletions = Math.min(deletions + 1, countB);\n\
        \            }\n        }\n        return deletions;\n    }\n}"
      python: "class Solution(object):\n    def minimumDeletions(self, s):\n       \
        \ \"\"\"\n        :type s: str\n        :rtype: int\n        \"\"\"\n      \
        \  deletions = 0\n        count_b = 0\n        for char in s:\n            if\
        \ char == 'b':\n                count_b += 1\n            else:\n          \
        \      deletions = min(deletions + 1, count_b)\n        return deletions"
      python3: "class Solution:\n    def minimumDeletions(self, s: str) -> int:\n  \
        \      deletions = 0\n        count_b = 0\n        for char in s:\n        \
        \    if char == 'b':\n                count_b += 1\n            else:\n    \
        \            deletions = min(deletions + 1, count_b)\n        return deletions"
      c: "int minimumDeletions(char* s) {\n    int deletions = 0;\n    int count_b =\
        \ 0;\n    for (int i = 0; s[i] != '\\0'; i++) {\n        if (s[i] == 'b') {\n\
        \            count_b++;\n        } else {\n            int option1 = deletions\
        \ + 1;\n            int option2 = count_b;\n            deletions = (option1\
        \ < option2) ? option1 : option2;\n        }\n    }\n    return deletions;\n\
        }"
      csharp: "public class Solution {\n    public int MinimumDeletions(string s) {\n\
        \        int deletions = 0;\n        int countB = 0;\n        foreach (char\
        \ c in s) {\n            if (c == 'b') {\n                countB++;\n      \
        \      } else {\n                deletions = Math.Min(deletions + 1, countB);\n\
        \            }\n        }\n        return deletions;\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {number}\n */\nvar minimumDeletions\
        \ = function(s) {\n    let deletions = 0;\n    let countB = 0;\n    for (let\
        \ i = 0; i < s.length; i++) {\n        if (s[i] === 'b') {\n            countB++;\n\
        \        } else {\n            deletions = Math.min(deletions + 1, countB);\n\
        \        }\n    }\n    return deletions;\n};"
      typescript: "function minimumDeletions(s: string): number {\n    let dp = 0;\n\
        \    let countB = 0;\n    for (let i = 0; i < s.length; i++) {\n        if (s[i]\
        \ === 'b') {\n            countB++;\n        } else {\n            dp = Math.min(dp\
        \ + 1, countB);\n        }\n    }\n    return dp;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return Integer\n\
        \     */\n    function minimumDeletions($s) {\n        $n = strlen($s);\n  \
        \      $dp = 0;\n        $countB = 0;\n        for ($i = 0; $i < $n; $i++) {\n\
        \            if ($s[$i] === 'b') {\n                $countB++;\n           \
        \ } else {\n                $dp = min($dp + 1, $countB);\n            }\n  \
        \      }\n        return $dp;\n    }\n}"
      swift: "class Solution {\n    func minimumDeletions(_ s: String) -> Int {\n  \
        \      var dp = 0\n        var countB = 0\n        for char in s {\n       \
        \     if char == \"b\" {\n                countB += 1\n            } else {\n\
        \                dp = min(dp + 1, countB)\n            }\n        }\n      \
        \  return dp\n    }\n}"
      kotlin: "class Solution {\n    fun minimumDeletions(s: String): Int {\n      \
        \  var dp = 0\n        var countB = 0\n        for (char in s) {\n         \
        \   if (char == 'b') {\n                countB++\n            } else {\n   \
        \             dp = if (dp + 1 < countB) dp + 1 else countB\n            }\n\
        \        }\n        return dp\n    }\n}"
      dart: "class Solution {\n  int minimumDeletions(String s) {\n    int dp = 0;\n\
        \    int countB = 0;\n    for (int i = 0; i < s.length; i++) {\n      if (s[i]\
        \ == 'b') {\n        countB++;\n      } else {\n        dp = (dp + 1 < countB)\
        \ ? dp + 1 : countB;\n      }\n    }\n    return dp;\n  }\n}"
      go: "func minimumDeletions(s string) int {\n\tdp := 0\n\tcountB := 0\n\tfor i\
        \ := 0; i < len(s); i++ {\n\t\tif s[i] == 'b' {\n\t\t\tcountB++\n\t\t} else\
        \ {\n\t\t\tif dp+1 < countB {\n\t\t\t\tdp++\n\t\t\t} else {\n\t\t\t\tdp = countB\n\
        \t\t\t}\n\t\t}\n\t}\n\treturn dp\n}"
      ruby: "def minimum_deletions(s)\n  res = 0\n  count_b = 0\n  s.each_char do |c|\n\
        \    if c == 'b'\n      count_b += 1\n    else\n      res = [res + 1, count_b].min\n\
        \    end\n  end\n  res\nend"
      scala: "object Solution {\n  def minimumDeletions(s: String): Int = {\n    var\
        \ res = 0\n    var countB = 0\n    for (c <- s) {\n      if (c == 'b') {\n \
        \       countB += 1\n      } else {\n        res = Math.min(res + 1, countB)\n\
        \      }\n    }\n    res\n  }\n}"
      rust: "impl Solution {\n    pub fn minimum_deletions(s: String) -> i32 {\n   \
        \     let mut res = 0;\n        let mut count_b = 0;\n        for c in s.chars()\
        \ {\n            if c == 'b' {\n                count_b += 1;\n            }\
        \ else {\n                res = std::cmp::min(res + 1, count_b);\n         \
        \   }\n        }\n        res\n    }\n}"
      racket: "(define/contract (minimum-deletions s)\n  (-> string? exact-integer?)\n\
        \  (let ([chars (string->list s)])\n    (let loop ([lst chars] [res 0] [count-b\
        \ 0])\n      (if (null? lst)\n          res\n          (let ([c (car lst)])\n\
        \            (if (char=? c #\\b)\n                (loop (cdr lst) res (+ count-b\
        \ 1))\n                (loop (cdr lst) (min (+ res 1) count-b) count-b)))))))"
      erlang: "minimum_deletions(S) ->\n  List = binary_to_list(S),\n  {Res, _} = lists:foldl(fun(C,\
        \ {R, B}) ->\n    if C =:= $b -> {R, B + 1};\n       true -> {erlang:min(R +\
        \ 1, B), B}\n    end\n  end, {0, 0}, List),\n  Res."
      elixir: "defmodule Solution do\n  @spec minimum_deletions(s :: String.t) :: integer\n\
        \  def minimum_deletions(s) do\n    {res, _} = s\n    |> String.to_charlist()\n\
        \    |> Enum.reduce({0, 0}, fn\n      ?b, {res, count_b} -> {res, count_b +\
        \ 1}\n      ?a, {res, count_b} -> {min(res + 1, count_b), count_b}\n    end)\n\
        \    res\n  end\nend"
    approach: The problem asks for the minimum deletions to make a string balanced,
      meaning no 'b' precedes an 'a'. We can solve this using dynamic programming by
      iterating through the string once and maintaining the minimum deletions required
      for the prefix processed so far. We keep track of the number of 'b' characters
      encountered as we move from left to right.
    time_complexity: O(n) where n is the length of the string s. We perform a single
      linear scan through the string, and each operation inside the loop takes constant
      time.
    space_complexity: O(1) because we only use two integer variables (one for the running
      count of 'b's and one for the minimum deletions) regardless of the input size.
    elapsed_time: 149.58917999267578
    model: gemini-3-flash-preview
    generated_at: '2026-02-07 01:21:48 '
---

## Problem #1653: Minimum Deletions to Make String Balanced

**Difficulty:** Medium

**Topics:** String, Dynamic Programming, Stack

## Problem Description

<p>You are given a string <code>s</code> consisting only of characters <code>&#39;a&#39;</code> and <code>&#39;b&#39;</code>​​​​.</p>

<p>You can delete any number of characters in <code>s</code> to make <code>s</code> <strong>balanced</strong>. <code>s</code> is <strong>balanced</strong> if there is no pair of indices <code>(i,j)</code> such that <code>i &lt; j</code> and <code>s[i] = &#39;b&#39;</code> and <code>s[j]= &#39;a&#39;</code>.</p>

<p>Return <em>the <strong>minimum</strong> number of deletions needed to make </em><code>s</code><em> <strong>balanced</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aababbab&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> You can either:
Delete the characters at 0-indexed positions 2 and 6 (&quot;aa<u>b</u>abb<u>a</u>b&quot; -&gt; &quot;aaabbb&quot;), or
Delete the characters at 0-indexed positions 3 and 6 (&quot;aab<u>a</u>bb<u>a</u>b&quot; -&gt; &quot;aabbbb&quot;).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bbaaaaabb&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> The only solution is to delete the first two characters.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is&nbsp;<code>&#39;a&#39;</code> or <code>&#39;b&#39;</code>​​.</li>
</ul>


## Hints

1. You need to find for every index the number of Bs before it and the number of A's after it

2. You can speed up the finding of A's and B's in suffix and prefix using preprocessing

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the minimum deletions to make a string balanced, meaning no 'b' precedes an 'a'. We can solve this using dynamic programming by iterating through the string once and maintaining the minimum deletions required for the prefix processed so far. We keep track of the number of 'b' characters encountered as we move from left to right.

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
    int minimumDeletions(string s) {
        int deletions = 0;
        int count_b = 0;
        for (char c : s) {
            if (c == 'b') {
                count_b++;
            } else {
                deletions = min(deletions + 1, count_b);
            }
        }
        return deletions;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minimumDeletions(String s) {
        int deletions = 0;
        int countB = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'b') {
                countB++;
            } else {
                deletions = Math.min(deletions + 1, countB);
            }
        }
        return deletions;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        deletions = 0
        count_b = 0
        for char in s:
            if char == 'b':
                count_b += 1
            else:
                deletions = min(deletions + 1, count_b)
        return deletions
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumDeletions(self, s: str) -> int:
        deletions = 0
        count_b = 0
        for char in s:
            if char == 'b':
                count_b += 1
            else:
                deletions = min(deletions + 1, count_b)
        return deletions
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int minimumDeletions(char* s) {
    int deletions = 0;
    int count_b = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == 'b') {
            count_b++;
        } else {
            int option1 = deletions + 1;
            int option2 = count_b;
            deletions = (option1 < option2) ? option1 : option2;
        }
    }
    return deletions;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinimumDeletions(string s) {
        int deletions = 0;
        int countB = 0;
        foreach (char c in s) {
            if (c == 'b') {
                countB++;
            } else {
                deletions = Math.Min(deletions + 1, countB);
            }
        }
        return deletions;
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
var minimumDeletions = function(s) {
    let deletions = 0;
    let countB = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === 'b') {
            countB++;
        } else {
            deletions = Math.min(deletions + 1, countB);
        }
    }
    return deletions;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimumDeletions(s: string): number {
    let dp = 0;
    let countB = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === 'b') {
            countB++;
        } else {
            dp = Math.min(dp + 1, countB);
        }
    }
    return dp;
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
    function minimumDeletions($s) {
        $n = strlen($s);
        $dp = 0;
        $countB = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === 'b') {
                $countB++;
            } else {
                $dp = min($dp + 1, $countB);
            }
        }
        return $dp;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minimumDeletions(_ s: String) -> Int {
        var dp = 0
        var countB = 0
        for char in s {
            if char == "b" {
                countB += 1
            } else {
                dp = min(dp + 1, countB)
            }
        }
        return dp
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minimumDeletions(s: String): Int {
        var dp = 0
        var countB = 0
        for (char in s) {
            if (char == 'b') {
                countB++
            } else {
                dp = if (dp + 1 < countB) dp + 1 else countB
            }
        }
        return dp
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minimumDeletions(String s) {
    int dp = 0;
    int countB = 0;
    for (int i = 0; i < s.length; i++) {
      if (s[i] == 'b') {
        countB++;
      } else {
        dp = (dp + 1 < countB) ? dp + 1 : countB;
      }
    }
    return dp;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minimumDeletions(s string) int {
	dp := 0
	countB := 0
	for i := 0; i < len(s); i++ {
		if s[i] == 'b' {
			countB++
		} else {
			if dp+1 < countB {
				dp++
			} else {
				dp = countB
			}
		}
	}
	return dp
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def minimum_deletions(s)
  res = 0
  count_b = 0
  s.each_char do |c|
    if c == 'b'
      count_b += 1
    else
      res = [res + 1, count_b].min
    end
  end
  res
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def minimumDeletions(s: String): Int = {
    var res = 0
    var countB = 0
    for (c <- s) {
      if (c == 'b') {
        countB += 1
      } else {
        res = Math.min(res + 1, countB)
      }
    }
    res
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn minimum_deletions(s: String) -> i32 {
        let mut res = 0;
        let mut count_b = 0;
        for c in s.chars() {
            if c == 'b' {
                count_b += 1;
            } else {
                res = std::cmp::min(res + 1, count_b);
            }
        }
        res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (minimum-deletions s)
  (-> string? exact-integer?)
  (let ([chars (string->list s)])
    (let loop ([lst chars] [res 0] [count-b 0])
      (if (null? lst)
          res
          (let ([c (car lst)])
            (if (char=? c #\b)
                (loop (cdr lst) res (+ count-b 1))
                (loop (cdr lst) (min (+ res 1) count-b) count-b)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
minimum_deletions(S) ->
  List = binary_to_list(S),
  {Res, _} = lists:foldl(fun(C, {R, B}) ->
    if C =:= $b -> {R, B + 1};
       true -> {erlang:min(R + 1, B), B}
    end
  end, {0, 0}, List),
  Res.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_deletions(s :: String.t) :: integer
  def minimum_deletions(s) do
    {res, _} = s
    |> String.to_charlist()
    |> Enum.reduce({0, 0}, fn
      ?b, {res, count_b} -> {res, count_b + 1}
      ?a, {res, count_b} -> {min(res + 1, count_b), count_b}
    end)
    res
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the string s. We perform a single linear scan through the string, and each operation inside the loop takes constant time.
- **Space Complexity:** O(1) because we only use two integer variables (one for the running count of 'b's and one for the minimum deletions) regardless of the input size.
