---
layout: post
title: "Minimum Number of Pushes to Type Word I"
date: 2026-07-30 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Math", "String", "Greedy"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minimumPushes(string word) {\n      \
        \  int n = word.length();\n        int totalPushes = 0;\n        for (int i\
        \ = 0; i < n; ++i) {\n            totalPushes += (i / 8) + 1;\n        }\n \
        \       return totalPushes;\n    }\n};"
      java: "class Solution {\n    public int minimumPushes(String word) {\n       \
        \ int n = word.length();\n        int totalPushes = 0;\n        for (int i =\
        \ 0; i < n; i++) {\n            totalPushes += (i / 8) + 1;\n        }\n   \
        \     return totalPushes;\n    }\n}"
      python: "class Solution(object):\n    def minimumPushes(self, word):\n       \
        \ \"\"\"\n        :type word: str\n        :rtype: int\n        \"\"\"\n   \
        \     n = len(word)\n        total_pushes = 0\n        for i in range(n):\n\
        \            total_pushes += (i // 8) + 1\n        return total_pushes"
      python3: "class Solution:\n    def minimumPushes(self, word: str) -> int:\n  \
        \      n = len(word)\n        total_pushes = 0\n        for i in range(n):\n\
        \            total_pushes += (i // 8) + 1\n        return total_pushes"
      c: "int minimumPushes(char* word) {\n    int n = 0;\n    while (word[n] != '\\\
        0') {\n        n++;\n    }\n    int totalPushes = 0;\n    for (int i = 0; i\
        \ < n; i++) {\n        totalPushes += (i / 8) + 1;\n    }\n    return totalPushes;\n\
        }"
      csharp: "public class Solution {\n    public int MinimumPushes(string word) {\n\
        \        int n = word.Length;\n        int totalPushes = 0;\n        for (int\
        \ i = 0; i < n; i++) {\n            totalPushes += (i / 8) + 1;\n        }\n\
        \        return totalPushes;\n    }\n}"
      javascript: "/**\n * @param {string} word\n * @return {number}\n */\nvar minimumPushes\
        \ = function(word) {\n    let n = word.length;\n    let totalPushes = 0;\n \
        \   for (let i = 0; i < n; i++) {\n        totalPushes += Math.floor(i / 8)\
        \ + 1;\n    }\n    return totalPushes;\n};"
      typescript: "function minimumPushes(word: string): number {\n    let n = word.length;\n\
        \    let pushes = 0;\n    for (let i = 0; i < n; i++) {\n        pushes += Math.floor(i\
        \ / 8) + 1;\n    }\n    return pushes;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $word\n     * @return\
        \ Integer\n     */\n    function minimumPushes($word) {\n        $n = strlen($word);\n\
        \        $pushes = 0;\n        for ($i = 0; $i < $n; $i++) {\n            $pushes\
        \ += (int)($i / 8) + 1;\n        }\n        return $pushes;\n    }\n}"
      swift: "class Solution {\n    func minimumPushes(_ word: String) -> Int {\n  \
        \      let n = word.count\n        var pushes = 0\n        for i in 0..<n {\n\
        \            pushes += (i / 8) + 1\n        }\n        return pushes\n    }\n\
        }"
      kotlin: "class Solution {\n    fun minimumPushes(word: String): Int {\n      \
        \  val n = word.length\n        var pushes = 0\n        for (i in 0 until n)\
        \ {\n            pushes += (i / 8) + 1\n        }\n        return pushes\n \
        \   }\n}"
      dart: "class Solution {\n  int minimumPushes(String word) {\n    int n = word.length;\n\
        \    int pushes = 0;\n    for (int i = 0; i < n; i++) {\n      pushes += (i\
        \ ~/ 8) + 1;\n    }\n    return pushes;\n  }\n}"
      go: "func minimumPushes(word string) int {\n    n := len(word)\n    pushes :=\
        \ 0\n    for i := 0; i < n; i++ {\n        pushes += (i / 8) + 1\n    }\n  \
        \  return pushes\n}"
      ruby: "# @param {String} word\n# @return {Integer}\ndef minimum_pushes(word)\n\
        \  n = word.length\n  (0...n).sum { |i| (i / 8) + 1 }\nend"
      scala: "object Solution {\n  def minimumPushes(word: String): Int = {\n    val\
        \ n = word.length\n    (0 until n).map(i => (i / 8) + 1).sum\n  }\n}"
      rust: "impl Solution {\n    pub fn minimum_pushes(word: String) -> i32 {\n   \
        \     let n = word.len() as i32;\n        (0..n).map(|i| (i / 8) + 1).sum()\n\
        \    }\n}"
      racket: "(define/contract (minimum-pushes word)\n  (-> string? exact-integer?)\n\
        \  (let ([n (string-length word)])\n    (for/sum ([i (in-range n)])\n      (+\
        \ (quotient i 8) 1))))"
      erlang: "-spec minimum_pushes(Word :: unicode:unicode_binary()) -> integer().\n\
        minimum_pushes(Word) ->\n  N = byte_size(Word),\n  lists:foldl(fun(I, Acc) ->\
        \ Acc + (I div 8) + 1 end, 0, lists:seq(0, N - 1))."
      elixir: "defmodule Solution do\n  @spec minimum_pushes(word :: String.t) :: integer\n\
        \  def minimum_pushes(word) do\n    n = String.length(word)\n    Enum.reduce(0..(n\
        \ - 1), 0, fn i, acc ->\n      acc + div(i, 8) + 1\n    end)\n  end\nend"
    approach: 'The goal is to minimize the total number of key presses by distributing
      distinct letters across the 8 available keys (numbered 2 to 9). Since every character
      in the input string is unique, the frequency of each character is 1. To minimize
      pushes, we should fill the first position of every available key before moving
      to the second position, then the third, and finally the fourth. This greedy approach
      ensures we use the minimum number of pushes for each character.


      Mathematically, for a string of length $n$, the first 8 characters will each require
      1 push, the next 8 characters will require 2 pushes each, the next 8 will require
      3 pushes each, and the remaining 2 characters will require 4 pushes each. We iterate
      through the indices of the string from 0 to $n-1$ and for each index $i$, the
      number of pushes required is calculated as $\lfloor i / 8 \rfloor + 1$. The sum
      of these values gives the final minimum pushes required to type the word.'
    time_complexity: O(n) where $n$ is the length of the input string. We iterate through
      the string once to calculate the total pushes. Given that $n \le 26$, this is
      effectively $O(1)$ in practice.
    space_complexity: O(1) because we only use a constant amount of extra space for
      the result variable and the loop index, regardless of the input size.
    elapsed_time: 58.401508808135986
    model: gemini-3-flash-preview
    generated_at: '2026-07-30 01:46:46 '
---

## Problem #3014: Minimum Number of Pushes to Type Word I

**Difficulty:** Easy

**Topics:** Math, String, Greedy

## Problem Description

<p>You are given a string <code>word</code> containing <strong>distinct</strong> lowercase English letters.</p>

<p>Telephone keypads have keys mapped with <strong>distinct</strong> collections of lowercase English letters, which can be used to form words by pushing them. For example, the key <code>2</code> is mapped with <code>[&quot;a&quot;,&quot;b&quot;,&quot;c&quot;]</code>, we need to push the key one time to type <code>&quot;a&quot;</code>, two times to type <code>&quot;b&quot;</code>, and three times to type <code>&quot;c&quot;</code> <em>.</em></p>

<p>It is allowed to remap the keys numbered <code>2</code> to <code>9</code> to <strong>distinct</strong> collections of letters. The keys can be remapped to <strong>any</strong> amount of letters, but each letter <strong>must</strong> be mapped to <strong>exactly</strong> one key. You need to find the <strong>minimum</strong> number of times the keys will be pushed to type the string <code>word</code>.</p>

<p>Return <em>the <strong>minimum</strong> number of pushes needed to type </em><code>word</code> <em>after remapping the keys</em>.</p>

<p>An example mapping of letters to keys on a telephone keypad is given below. Note that <code>1</code>, <code>*</code>, <code>#</code>, and <code>0</code> do <strong>not</strong> map to any letters.</p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/12/26/keypaddesc.png" style="width: 329px; height: 313px;" />
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/12/26/keypadv1e1.png" style="width: 329px; height: 313px;" />
<pre>
<strong>Input:</strong> word = &quot;abcde&quot;
<strong>Output:</strong> 5
<strong>Explanation:</strong> The remapped keypad given in the image provides the minimum cost.
&quot;a&quot; -&gt; one push on key 2
&quot;b&quot; -&gt; one push on key 3
&quot;c&quot; -&gt; one push on key 4
&quot;d&quot; -&gt; one push on key 5
&quot;e&quot; -&gt; one push on key 6
Total cost is 1 + 1 + 1 + 1 + 1 = 5.
It can be shown that no other mapping can provide a lower cost.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/12/26/keypadv1e2.png" style="width: 329px; height: 313px;" />
<pre>
<strong>Input:</strong> word = &quot;xycdefghij&quot;
<strong>Output:</strong> 12
<strong>Explanation:</strong> The remapped keypad given in the image provides the minimum cost.
&quot;x&quot; -&gt; one push on key 2
&quot;y&quot; -&gt; two pushes on key 2
&quot;c&quot; -&gt; one push on key 3
&quot;d&quot; -&gt; two pushes on key 3
&quot;e&quot; -&gt; one push on key 4
&quot;f&quot; -&gt; one push on key 5
&quot;g&quot; -&gt; one push on key 6
&quot;h&quot; -&gt; one push on key 7
&quot;i&quot; -&gt; one push on key 8
&quot;j&quot; -&gt; one push on key 9
Total cost is 1 + 2 + 1 + 2 + 1 + 1 + 1 + 1 + 1 + 1 = 12.
It can be shown that no other mapping can provide a lower cost.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 26</code></li>
	<li><code>word</code> consists of lowercase English letters.</li>
	<li>All letters in <code>word</code> are distinct.</li>
</ul>


## Hints

1. We have 8 keys in total. We can type 8 characters with one push each, 8 different characters with two pushes each, and so on.

2. The optimal way is to map letters to keys evenly.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The goal is to minimize the total number of key presses by distributing distinct letters across the 8 available keys (numbered 2 to 9). Since every character in the input string is unique, the frequency of each character is 1. To minimize pushes, we should fill the first position of every available key before moving to the second position, then the third, and finally the fourth. This greedy approach ensures we use the minimum number of pushes for each character.

Mathematically, for a string of length $n$, the first 8 characters will each require 1 push, the next 8 characters will require 2 pushes each, the next 8 will require 3 pushes each, and the remaining 2 characters will require 4 pushes each. We iterate through the indices of the string from 0 to $n-1$ and for each index $i$, the number of pushes required is calculated as $\lfloor i / 8 \rfloor + 1$. The sum of these values gives the final minimum pushes required to type the word.

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
    int minimumPushes(string word) {
        int n = word.length();
        int totalPushes = 0;
        for (int i = 0; i < n; ++i) {
            totalPushes += (i / 8) + 1;
        }
        return totalPushes;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minimumPushes(String word) {
        int n = word.length();
        int totalPushes = 0;
        for (int i = 0; i < n; i++) {
            totalPushes += (i / 8) + 1;
        }
        return totalPushes;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
        total_pushes = 0
        for i in range(n):
            total_pushes += (i // 8) + 1
        return total_pushes
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        total_pushes = 0
        for i in range(n):
            total_pushes += (i // 8) + 1
        return total_pushes
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int minimumPushes(char* word) {
    int n = 0;
    while (word[n] != '\0') {
        n++;
    }
    int totalPushes = 0;
    for (int i = 0; i < n; i++) {
        totalPushes += (i / 8) + 1;
    }
    return totalPushes;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinimumPushes(string word) {
        int n = word.Length;
        int totalPushes = 0;
        for (int i = 0; i < n; i++) {
            totalPushes += (i / 8) + 1;
        }
        return totalPushes;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} word
 * @return {number}
 */
var minimumPushes = function(word) {
    let n = word.length;
    let totalPushes = 0;
    for (let i = 0; i < n; i++) {
        totalPushes += Math.floor(i / 8) + 1;
    }
    return totalPushes;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimumPushes(word: string): number {
    let n = word.length;
    let pushes = 0;
    for (let i = 0; i < n; i++) {
        pushes += Math.floor(i / 8) + 1;
    }
    return pushes;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String $word
     * @return Integer
     */
    function minimumPushes($word) {
        $n = strlen($word);
        $pushes = 0;
        for ($i = 0; $i < $n; $i++) {
            $pushes += (int)($i / 8) + 1;
        }
        return $pushes;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minimumPushes(_ word: String) -> Int {
        let n = word.count
        var pushes = 0
        for i in 0..<n {
            pushes += (i / 8) + 1
        }
        return pushes
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minimumPushes(word: String): Int {
        val n = word.length
        var pushes = 0
        for (i in 0 until n) {
            pushes += (i / 8) + 1
        }
        return pushes
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minimumPushes(String word) {
    int n = word.length;
    int pushes = 0;
    for (int i = 0; i < n; i++) {
      pushes += (i ~/ 8) + 1;
    }
    return pushes;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minimumPushes(word string) int {
    n := len(word)
    pushes := 0
    for i := 0; i < n; i++ {
        pushes += (i / 8) + 1
    }
    return pushes
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} word
# @return {Integer}
def minimum_pushes(word)
  n = word.length
  (0...n).sum { |i| (i / 8) + 1 }
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def minimumPushes(word: String): Int = {
    val n = word.length
    (0 until n).map(i => (i / 8) + 1).sum
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn minimum_pushes(word: String) -> i32 {
        let n = word.len() as i32;
        (0..n).map(|i| (i / 8) + 1).sum()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (minimum-pushes word)
  (-> string? exact-integer?)
  (let ([n (string-length word)])
    (for/sum ([i (in-range n)])
      (+ (quotient i 8) 1))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec minimum_pushes(Word :: unicode:unicode_binary()) -> integer().
minimum_pushes(Word) ->
  N = byte_size(Word),
  lists:foldl(fun(I, Acc) -> Acc + (I div 8) + 1 end, 0, lists:seq(0, N - 1)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_pushes(word :: String.t) :: integer
  def minimum_pushes(word) do
    n = String.length(word)
    Enum.reduce(0..(n - 1), 0, fn i, acc ->
      acc + div(i, 8) + 1
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where $n$ is the length of the input string. We iterate through the string once to calculate the total pushes. Given that $n \le 26$, this is effectively $O(1)$ in practice.
- **Space Complexity:** O(1) because we only use a constant amount of extra space for the result variable and the loop index, regardless of the input size.
