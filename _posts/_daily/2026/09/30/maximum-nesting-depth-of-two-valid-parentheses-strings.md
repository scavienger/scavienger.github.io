---
layout: post
title: "Maximum Nesting Depth of Two Valid Parentheses Strings"
date: 2026-09-30 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Stack", "Bracket Sequences"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <string>\n\nusing namespace std;\n\nclass Solution\
        \ {\npublic:\n    vector<int> maxDepthAfterSplit(string seq) {\n        int\
        \ n = seq.length();\n        vector<int> answer(n);\n        int depth = 0;\n\
        \        for (int i = 0; i < n; ++i) {\n            if (seq[i] == '(') {\n \
        \               answer[i] = depth % 2;\n                depth++;\n         \
        \   } else {\n                depth--;\n                answer[i] = depth %\
        \ 2;\n            }\n        }\n        return answer;\n    }\n};"
      java: "class Solution {\n    public int[] maxDepthAfterSplit(String seq) {\n \
        \       int n = seq.length();\n        int[] answer = new int[n];\n        int\
        \ depth = 0;\n        for (int i = 0; i < n; i++) {\n            if (seq.charAt(i)\
        \ == '(') {\n                answer[i] = depth % 2;\n                depth++;\n\
        \            } else {\n                depth--;\n                answer[i] =\
        \ depth % 2;\n            }\n        }\n        return answer;\n    }\n}"
      python: "class Solution(object):\n    def maxDepthAfterSplit(self, seq):\n   \
        \     \"\"\"\n        :type seq: str\n        :rtype: List[int]\n        \"\"\
        \"\n        n = len(seq)\n        answer = [0] * n\n        depth = 0\n    \
        \    for i in range(n):\n            if seq[i] == '(':\n                answer[i]\
        \ = depth % 2\n                depth += 1\n            else:\n             \
        \   depth -= 1\n                answer[i] = depth % 2\n        return answer"
      python3: "class Solution:\n    def maxDepthAfterSplit(self, seq: str) -> list[int]:\n\
        \        n = len(seq)\n        answer = [0] * n\n        depth = 0\n       \
        \ for i in range(n):\n            if seq[i] == '(':\n                answer[i]\
        \ = depth % 2\n                depth += 1\n            else:\n             \
        \   depth -= 1\n                answer[i] = depth % 2\n        return answer"
      c: "#include <stdlib.h>\n#include <string.h>\n\n/**\n * Note: The returned array\
        \ must be malloced, assume caller calls free().\n */\nint* maxDepthAfterSplit(char*\
        \ seq, int* returnSize) {\n    int n = (int)strlen(seq);\n    *returnSize =\
        \ n;\n    int* answer = (int*)malloc(n * sizeof(int));\n    int depth = 0;\n\
        \    for (int i = 0; i < n; i++) {\n        if (seq[i] == '(') {\n         \
        \   answer[i] = depth % 2;\n            depth++;\n        } else {\n       \
        \     depth--;\n            answer[i] = depth % 2;\n        }\n    }\n    return\
        \ answer;\n}"
      csharp: "public class Solution {\n    public int[] MaxDepthAfterSplit(string seq)\
        \ {\n        int n = seq.Length;\n        int[] result = new int[n];\n     \
        \   int depth = 0;\n        for (int i = 0; i < n; i++) {\n            if (seq[i]\
        \ == '(') {\n                result[i] = depth % 2;\n                depth++;\n\
        \            } else {\n                depth--;\n                result[i] =\
        \ depth % 2;\n            }\n        }\n        return result;\n    }\n}"
      javascript: "/**\n * @param {string} seq\n * @return {number[]}\n */\nvar maxDepthAfterSplit\
        \ = function(seq) {\n    const n = seq.length;\n    const result = new Array(n);\n\
        \    let depth = 0;\n    for (let i = 0; i < n; i++) {\n        if (seq[i] ===\
        \ '(') {\n            result[i] = depth % 2;\n            depth++;\n       \
        \ } else {\n            depth--;\n            result[i] = depth % 2;\n     \
        \   }\n    }\n    return result;\n};"
      typescript: "function maxDepthAfterSplit(seq: string): number[] {\n    const n\
        \ = seq.length;\n    const result: number[] = new Array(n);\n    let depth =\
        \ 0;\n    for (let i = 0; i < n; i++) {\n        if (seq[i] === '(') {\n   \
        \         result[i] = depth % 2;\n            depth++;\n        } else {\n \
        \           depth--;\n            result[i] = depth % 2;\n        }\n    }\n\
        \    return result;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $seq\n     * @return Integer[]\n\
        \     */\n    function maxDepthAfterSplit($seq) {\n        $n = strlen($seq);\n\
        \        $result = [];\n        $depth = 0;\n        for ($i = 0; $i < $n; $i++)\
        \ {\n            if ($seq[$i] === '(') {\n                $result[] = $depth\
        \ % 2;\n                $depth++;\n            } else {\n                $depth--;\n\
        \                $result[] = $depth % 2;\n            }\n        }\n       \
        \ return $result;\n    }\n}"
      swift: "class Solution {\n    func maxDepthAfterSplit(_ seq: String) -> [Int]\
        \ {\n        let n = seq.count\n        var result = [Int](repeating: 0, count:\
        \ n)\n        var depth = 0\n        let characters = Array(seq)\n\n       \
        \ for i in 0..<n {\n            if characters[i] == \"(\" {\n              \
        \  result[i] = depth % 2\n                depth += 1\n            } else {\n\
        \                depth -= 1\n                result[i] = depth % 2\n       \
        \     }\n        }\n\n        return result\n    }\n}"
      kotlin: "class Solution {\n    fun maxDepthAfterSplit(seq: String): IntArray {\n\
        \        val n = seq.length\n        val result = IntArray(n)\n        var depth\
        \ = 0\n        for (i in 0 until n) {\n            if (seq[i] == '(') {\n  \
        \              result[i] = depth % 2\n                depth++\n            }\
        \ else {\n                depth--\n                result[i] = depth % 2\n \
        \           }\n        }\n        return result\n    }\n}"
      dart: "class Solution {\n  List<int> maxDepthAfterSplit(String seq) {\n    int\
        \ n = seq.length;\n    List<int> result = List<int>.filled(n, 0);\n    int depth\
        \ = 0;\n    for (int i = 0; i < n; i++) {\n      if (seq[i] == '(') {\n    \
        \    result[i] = depth % 2;\n        depth++;\n      } else {\n        depth--;\n\
        \        result[i] = depth % 2;\n      }\n    }\n    return result;\n  }\n}"
      go: "func maxDepthAfterSplit(seq string) []int {\n    n := len(seq)\n    result\
        \ := make([]int, n)\n    depth := 0\n    for i := 0; i < n; i++ {\n        if\
        \ seq[i] == '(' {\n            result[i] = depth % 2\n            depth++\n\
        \        } else {\n            depth--\n            result[i] = depth % 2\n\
        \        }\n    }\n    return result\n}"
      ruby: "# @param {String} seq\n# @return {Integer[]}\ndef max_depth_after_split(seq)\n\
        \  depth = 0\n  result = Array.new(seq.length)\n  seq.each_char.with_index do\
        \ |char, i|\n    if char == '('\n      result[i] = depth % 2\n      depth +=\
        \ 1\n    else\n      depth -= 1\n      result[i] = depth % 2\n    end\n  end\n\
        \  result\nend"
      scala: "object Solution {\n    def maxDepthAfterSplit(seq: String): Array[Int]\
        \ = {\n        val n = seq.length\n        val result = new Array[Int](n)\n\
        \        var depth = 0\n        for (i <- 0 until n) {\n            if (seq(i)\
        \ == '(') {\n                result(i) = depth % 2\n                depth +=\
        \ 1\n            } else {\n                depth -= 1\n                result(i)\
        \ = depth % 2\n            }\n        }\n        result\n    }\n}"
      rust: "impl Solution {\n    pub fn max_depth_after_split(seq: String) -> Vec<i32>\
        \ {\n        let mut res = Vec::with_capacity(seq.len());\n        let mut depth\
        \ = 0;\n        for c in seq.chars() {\n            if c == '(' {\n        \
        \        res.push(depth % 2);\n                depth += 1;\n            } else\
        \ {\n                depth -= 1;\n                res.push(depth % 2);\n   \
        \         }\n        }\n        res\n    }\n}"
      racket: "(define/contract (max-depth-after-split seq)\n  (-> string? (listof exact-integer?))\n\
        \  (let ([chars (string->list seq)])\n    (let loop ([chars chars] [depth 0]\
        \ [acc '()])\n      (if (null? chars)\n          (reverse acc)\n          (let\
        \ ([c (car chars)])\n            (if (char=? c #\\()\n                (loop\
        \ (cdr chars) (+ depth 1) (cons (modulo depth 2) acc))\n                (let\
        \ ([new-depth (- depth 1)])\n                  (loop (cdr chars) new-depth (cons\
        \ (modulo new-depth 2) acc)))))))))"
      erlang: "-spec max_depth_after_split(Seq :: unicode:unicode_binary()) -> [integer()].\n\
        max_depth_after_split(Seq) ->\n    Chars = binary_to_list(Seq),\n    {_Depth,\
        \ Acc} = lists:foldl(fun(C, {D, A}) ->\n        case C of\n            $( ->\
        \ {D + 1, [D rem 2 | A]};\n            $) -> NewD = D - 1, {NewD, [NewD rem\
        \ 2 | A]}\n        end\n    end, {0, []}, Chars),\n    lists:reverse(Acc)."
      elixir: "defmodule Solution {\n  @spec max_depth_after_split(seq :: String.t)\
        \ :: [integer]\n  def max_depth_after_split(seq) do\n    {_final_depth, acc}\
        \ = seq\n    |> String.to_charlist()\n    |> Enum.reduce({0, []}, fn char, {depth,\
        \ acc} ->\n      if char == ?( do\n        {depth + 1, [rem(depth, 2) | acc]}\n\
        \      else\n        new_depth = depth - 1\n        {new_depth, [rem(new_depth,\
        \ 2) | acc]}\n      end\n    end)\n    Enum.reverse(acc)\n  end\n}"
    approach: The core idea is to distribute the nested parentheses as evenly as possible
      between two subsequences, A and B, to minimize their maximum nesting depth. Since
      the nesting depth of a valid parentheses string is determined by the number of
      open parentheses that have not yet been closed, we can track the current nesting
      depth at each character. By assigning parentheses at even depths to one subsequence
      and those at odd depths to the other, we effectively split the total depth in
      half, minimizing the overall maximum depth.
    time_complexity: O(N) where N is the length of the input string. The algorithm performs
      a single pass through the sequence, making a constant-time assignment for each
      character based on the current depth.
    space_complexity: O(N) to store and return the result array. Aside from the output
      array, only a constant amount of extra space is used for the depth counter, making
      the auxiliary space O(1).
    elapsed_time: 160.9020013809204
    model: gemini-3-flash-preview
    generated_at: '2026-09-30 03:20:47 '
---

## Problem #1111: Maximum Nesting Depth of Two Valid Parentheses Strings

**Difficulty:** Medium

**Topics:** String, Stack, Bracket Sequences

## Problem Description

<p>A string is a <em>valid parentheses string</em>&nbsp;(denoted VPS) if and only if it consists of <code>&quot;(&quot;</code> and <code>&quot;)&quot;</code> characters only, and:</p>

<ul>
	<li>It is the empty string, or</li>
	<li>It can be written as&nbsp;<code>AB</code>&nbsp;(<code>A</code>&nbsp;concatenated with&nbsp;<code>B</code>), where&nbsp;<code>A</code>&nbsp;and&nbsp;<code>B</code>&nbsp;are VPS&#39;s, or</li>
	<li>It can be written as&nbsp;<code>(A)</code>, where&nbsp;<code>A</code>&nbsp;is a VPS.</li>
</ul>

<p>We can&nbsp;similarly define the <em>nesting depth</em> <code>depth(S)</code> of any VPS <code>S</code> as follows:</p>

<ul>
	<li><code>depth(&quot;&quot;) = 0</code></li>
	<li><code>depth(A + B) = max(depth(A), depth(B))</code>, where <code>A</code> and <code>B</code> are VPS&#39;s</li>
	<li><code>depth(&quot;(&quot; + A + &quot;)&quot;) = 1 + depth(A)</code>, where <code>A</code> is a VPS.</li>
</ul>

<p>For example, <code>&quot;&quot;</code>,&nbsp;<code>&quot;()()&quot;</code>, and&nbsp;<code>&quot;()(()())&quot;</code>&nbsp;are VPS&#39;s (with nesting depths 0, 1, and 2), and <code>&quot;)(&quot;</code> and <code>&quot;(()&quot;</code> are not VPS&#39;s.</p>

<p>Given a VPS <font face="monospace">seq</font>, split it into two disjoint subsequences <code>A</code> and <code>B</code>, such that&nbsp;<code>A</code> and <code>B</code> are VPS&#39;s (and&nbsp;<code>A.length + B.length = seq.length</code>). The subsequences may not necessarily be contiguous.</p>

<p>For example, for the sequence <code>123456789</code>, one possible split is:</p>

<ul data-end="822" data-start="776">
	<li data-end="800" data-start="776">
	<p data-end="800" data-start="778"><code data-end="799" data-start="778">A = {1, 3, 5, 7, 9}</code>,</p>
	</li>
	<li data-end="822" data-start="801">
	<p data-end="822" data-start="803"><code data-end="821" data-start="803">B = {2, 4, 6, 8}</code>.</p>
	</li>
</ul>

<p data-end="855" data-start="824">This corresponds to the output <code>[0, 1, 0, 1, 0, 1, 0, 1, 0]</code> &nbsp;where 0 indicates membership in&nbsp;<code data-end="929" data-start="926">A</code>&nbsp;and 1 indicates membership in&nbsp;<code data-end="965" data-start="962">B</code>.</p>

<p>Now choose <strong>any</strong> such <code>A</code> and <code>B</code> such that&nbsp;<code>max(depth(A), depth(B))</code> is the minimum possible value.</p>

<p>Return an <code>answer</code> array (of length <code>seq.length</code>) that encodes such a&nbsp;choice of <code>A</code> and <code>B</code>:&nbsp; <code>answer[i] = 0</code> if <code>seq[i]</code> is part of <code>A</code>, else <code>answer[i] = 1</code>.&nbsp; Note that even though multiple answers may exist, you may return any of them.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> seq = &quot;(()())&quot;
<strong>Output:</strong> [0,1,1,1,1,0]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> seq = &quot;()(())()&quot;
<strong>Output:</strong> [0,0,0,1,1,0,1,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= seq.size &lt;= 10000</code></li>
</ul>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The core idea is to distribute the nested parentheses as evenly as possible between two subsequences, A and B, to minimize their maximum nesting depth. Since the nesting depth of a valid parentheses string is determined by the number of open parentheses that have not yet been closed, we can track the current nesting depth at each character. By assigning parentheses at even depths to one subsequence and those at odd depths to the other, we effectively split the total depth in half, minimizing the overall maximum depth.

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
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> maxDepthAfterSplit(string seq) {
        int n = seq.length();
        vector<int> answer(n);
        int depth = 0;
        for (int i = 0; i < n; ++i) {
            if (seq[i] == '(') {
                answer[i] = depth % 2;
                depth++;
            } else {
                depth--;
                answer[i] = depth % 2;
            }
        }
        return answer;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int[] maxDepthAfterSplit(String seq) {
        int n = seq.length();
        int[] answer = new int[n];
        int depth = 0;
        for (int i = 0; i < n; i++) {
            if (seq.charAt(i) == '(') {
                answer[i] = depth % 2;
                depth++;
            } else {
                depth--;
                answer[i] = depth % 2;
            }
        }
        return answer;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        n = len(seq)
        answer = [0] * n
        depth = 0
        for i in range(n):
            if seq[i] == '(':
                answer[i] = depth % 2
                depth += 1
            else:
                depth -= 1
                answer[i] = depth % 2
        return answer
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        n = len(seq)
        answer = [0] * n
        depth = 0
        for i in range(n):
            if seq[i] == '(':
                answer[i] = depth % 2
                depth += 1
            else:
                depth -= 1
                answer[i] = depth % 2
        return answer
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maxDepthAfterSplit(char* seq, int* returnSize) {
    int n = (int)strlen(seq);
    *returnSize = n;
    int* answer = (int*)malloc(n * sizeof(int));
    int depth = 0;
    for (int i = 0; i < n; i++) {
        if (seq[i] == '(') {
            answer[i] = depth % 2;
            depth++;
        } else {
            depth--;
            answer[i] = depth % 2;
        }
    }
    return answer;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int[] MaxDepthAfterSplit(string seq) {
        int n = seq.Length;
        int[] result = new int[n];
        int depth = 0;
        for (int i = 0; i < n; i++) {
            if (seq[i] == '(') {
                result[i] = depth % 2;
                depth++;
            } else {
                depth--;
                result[i] = depth % 2;
            }
        }
        return result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} seq
 * @return {number[]}
 */
var maxDepthAfterSplit = function(seq) {
    const n = seq.length;
    const result = new Array(n);
    let depth = 0;
    for (let i = 0; i < n; i++) {
        if (seq[i] === '(') {
            result[i] = depth % 2;
            depth++;
        } else {
            depth--;
            result[i] = depth % 2;
        }
    }
    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxDepthAfterSplit(seq: string): number[] {
    const n = seq.length;
    const result: number[] = new Array(n);
    let depth = 0;
    for (let i = 0; i < n; i++) {
        if (seq[i] === '(') {
            result[i] = depth % 2;
            depth++;
        } else {
            depth--;
            result[i] = depth % 2;
        }
    }
    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String $seq
     * @return Integer[]
     */
    function maxDepthAfterSplit($seq) {
        $n = strlen($seq);
        $result = [];
        $depth = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($seq[$i] === '(') {
                $result[] = $depth % 2;
                $depth++;
            } else {
                $depth--;
                $result[] = $depth % 2;
            }
        }
        return $result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxDepthAfterSplit(_ seq: String) -> [Int] {
        let n = seq.count
        var result = [Int](repeating: 0, count: n)
        var depth = 0
        let characters = Array(seq)

        for i in 0..<n {
            if characters[i] == "(" {
                result[i] = depth % 2
                depth += 1
            } else {
                depth -= 1
                result[i] = depth % 2
            }
        }

        return result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxDepthAfterSplit(seq: String): IntArray {
        val n = seq.length
        val result = IntArray(n)
        var depth = 0
        for (i in 0 until n) {
            if (seq[i] == '(') {
                result[i] = depth % 2
                depth++
            } else {
                depth--
                result[i] = depth % 2
            }
        }
        return result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<int> maxDepthAfterSplit(String seq) {
    int n = seq.length;
    List<int> result = List<int>.filled(n, 0);
    int depth = 0;
    for (int i = 0; i < n; i++) {
      if (seq[i] == '(') {
        result[i] = depth % 2;
        depth++;
      } else {
        depth--;
        result[i] = depth % 2;
      }
    }
    return result;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxDepthAfterSplit(seq string) []int {
    n := len(seq)
    result := make([]int, n)
    depth := 0
    for i := 0; i < n; i++ {
        if seq[i] == '(' {
            result[i] = depth % 2
            depth++
        } else {
            depth--
            result[i] = depth % 2
        }
    }
    return result
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} seq
# @return {Integer[]}
def max_depth_after_split(seq)
  depth = 0
  result = Array.new(seq.length)
  seq.each_char.with_index do |char, i|
    if char == '('
      result[i] = depth % 2
      depth += 1
    else
      depth -= 1
      result[i] = depth % 2
    end
  end
  result
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxDepthAfterSplit(seq: String): Array[Int] = {
        val n = seq.length
        val result = new Array[Int](n)
        var depth = 0
        for (i <- 0 until n) {
            if (seq(i) == '(') {
                result(i) = depth % 2
                depth += 1
            } else {
                depth -= 1
                result(i) = depth % 2
            }
        }
        result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_depth_after_split(seq: String) -> Vec<i32> {
        let mut res = Vec::with_capacity(seq.len());
        let mut depth = 0;
        for c in seq.chars() {
            if c == '(' {
                res.push(depth % 2);
                depth += 1;
            } else {
                depth -= 1;
                res.push(depth % 2);
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
(define/contract (max-depth-after-split seq)
  (-> string? (listof exact-integer?))
  (let ([chars (string->list seq)])
    (let loop ([chars chars] [depth 0] [acc '()])
      (if (null? chars)
          (reverse acc)
          (let ([c (car chars)])
            (if (char=? c #\()
                (loop (cdr chars) (+ depth 1) (cons (modulo depth 2) acc))
                (let ([new-depth (- depth 1)])
                  (loop (cdr chars) new-depth (cons (modulo new-depth 2) acc)))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_depth_after_split(Seq :: unicode:unicode_binary()) -> [integer()].
max_depth_after_split(Seq) ->
    Chars = binary_to_list(Seq),
    {_Depth, Acc} = lists:foldl(fun(C, {D, A}) ->
        case C of
            $( -> {D + 1, [D rem 2 | A]};
            $) -> NewD = D - 1, {NewD, [NewD rem 2 | A]}
        end
    end, {0, []}, Chars),
    lists:reverse(Acc).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution {
  @spec max_depth_after_split(seq :: String.t) :: [integer]
  def max_depth_after_split(seq) do
    {_final_depth, acc} = seq
    |> String.to_charlist()
    |> Enum.reduce({0, []}, fn char, {depth, acc} ->
      if char == ?( do
        {depth + 1, [rem(depth, 2) | acc]}
      else
        new_depth = depth - 1
        {new_depth, [rem(new_depth, 2) | acc]}
      end
    end)
    Enum.reverse(acc)
  end
}
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) where N is the length of the input string. The algorithm performs a single pass through the sequence, making a constant-time assignment for each character based on the current depth.
- **Space Complexity:** O(N) to store and return the result array. Aside from the output array, only a constant amount of extra space is used for the depth counter, making the auxiliary space O(1).
