---
layout: post
title: "Number of Strings That Appear as Substrings in Word"
date: 2026-06-29 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "String"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int numOfStrings(vector<string>& patterns,\
        \ string word) {\n        int count = 0;\n        for (const string& p : patterns)\
        \ {\n            if (word.find(p) != string::npos) {\n                count++;\n\
        \            }\n        }\n        return count;\n    }\n};"
      java: "class Solution {\n    public int numOfStrings(String[] patterns, String\
        \ word) {\n        int count = 0;\n        for (String p : patterns) {\n   \
        \         if (word.contains(p)) {\n                count++;\n            }\n\
        \        }\n        return count;\n    }\n}"
      python: "class Solution(object):\n    def numOfStrings(self, patterns, word):\n\
        \        \"\"\"\n        :type patterns: List[str]\n        :type word: str\n\
        \        :rtype: int\n        \"\"\"\n        count = 0\n        for p in patterns:\n\
        \            if p in word:\n                count += 1\n        return count"
      python3: "class Solution:\n    def numOfStrings(self, patterns: List[str], word:\
        \ str) -> int:\n        count = 0\n        for p in patterns:\n            if\
        \ p in word:\n                count += 1\n        return count"
      c: "#include <string.h>\n\nint numOfStrings(char** patterns, int patternsSize,\
        \ char* word) {\n    int count = 0;\n    for (int i = 0; i < patternsSize; i++)\
        \ {\n        if (strstr(word, patterns[i]) != NULL) {\n            count++;\n\
        \        }\n    }\n    return count;\n}"
      csharp: "public class Solution {\n    public int NumOfStrings(string[] patterns,\
        \ string word) {\n        int count = 0;\n        foreach (string p in patterns)\
        \ {\n            if (word.Contains(p)) {\n                count++;\n       \
        \     }\n        }\n        return count;\n    }\n}"
      javascript: "/**\n * @param {string[]} patterns\n * @param {string} word\n * @return\
        \ {number}\n */\nvar numOfStrings = function(patterns, word) {\n    let count\
        \ = 0;\n    for (let i = 0; i < patterns.length; i++) {\n        if (word.includes(patterns[i]))\
        \ {\n            count++;\n        }\n    }\n    return count;\n};"
      typescript: "function numOfStrings(patterns: string[], word: string): number {\n\
        \    let count = 0;\n    for (const pattern of patterns) {\n        if (word.includes(pattern))\
        \ {\n            count++;\n        }\n    }\n    return count;\n};"
      php: "class Solution {\n\n    /**\n     * @param String[] $patterns\n     * @param\
        \ String $word\n     * @return Integer\n     */\n    function numOfStrings($patterns,\
        \ $word) {\n        $count = 0;\n        foreach ($patterns as $pattern) {\n\
        \            if (strpos($word, $pattern) !== false) {\n                $count++;\n\
        \            }\n        }\n        return $count;\n    }\n}"
      swift: "class Solution {\n    func numOfStrings(_ patterns: [String], _ word:\
        \ String) -> Int {\n        var count = 0\n        for pattern in patterns {\n\
        \            if word.contains(pattern) {\n                count += 1\n     \
        \       }\n        }\n        return count\n    }\n}"
      kotlin: "class Solution {\n    fun numOfStrings(patterns: Array<String>, word:\
        \ String): Int {\n        var count = 0\n        for (pattern in patterns) {\n\
        \            if (word.contains(pattern)) {\n                count++\n      \
        \      }\n        }\n        return count\n    }\n}"
      dart: "class Solution {\n  int numOfStrings(List<String> patterns, String word)\
        \ {\n    int count = 0;\n    for (final pattern in patterns) {\n      if (word.contains(pattern))\
        \ {\n        count++;\n      }\n    }\n    return count;\n  }\n}"
      go: "import \"strings\"\n\nfunc numOfStrings(patterns []string, word string) int\
        \ {\n    count := 0\n    for _, pattern := range patterns {\n        if strings.Contains(word,\
        \ pattern) {\n            count++\n        }\n    }\n    return count\n}"
      ruby: "# @param {String[]} patterns\n# @param {String} word\n# @return {Integer}\n\
        def num_of_strings(patterns, word)\n  patterns.count { |p| word.include?(p)\
        \ }\nend"
      scala: "object Solution {\n    def numOfStrings(patterns: Array[String], word:\
        \ String): Int = {\n        patterns.count(p => word.contains(p))\n    }\n}"
      rust: "impl Solution {\n    pub fn num_of_strings(patterns: Vec<String>, word:\
        \ String) -> i32 {\n        patterns.iter().filter(|p| word.contains(p.as_str())).count()\
        \ as i32\n    }\n}"
      racket: "(require racket/string)\n\n(define/contract (num-of-strings patterns\
        \ word)\n  (-> (listof string?) string? exact-integer?)\n  (length (filter (lambda\
        \ (p) (string-contains? word p)) patterns)))"
      erlang: "-spec num_of_strings(Patterns :: [unicode:unicode_binary()], Word ::\
        \ unicode:unicode_binary()) -> integer().\nnum_of_strings(Patterns, Word) ->\n\
        \  length([P || P <- Patterns, binary:match(Word, P) =/= nomatch])."
      elixir: "defmodule Solution do\n  @spec num_of_strings(patterns :: [String.t],\
        \ word :: String.t) :: integer\n  def num_of_strings(patterns, word) do\n  \
        \  Enum.count(patterns, fn p -> String.contains?(word, p) end)\n  end\nend"
    approach: 'The core approach involves iterating through each string in the provided
      patterns array and checking if it exists as a contiguous substring within the
      target word. We maintain a running counter to track how many patterns satisfy
      this condition. For each pattern, we utilize the language''s native string searching
      functionality to determine presence.


      Built-in functions such as ''contains'' in Java and C#, ''find'' in C++, ''strstr''
      in C, ''includes'' in JavaScript, and the ''in'' operator in Python provide an
      efficient and readable way to perform these checks. Since the constraints for
      both the number of patterns and the lengths of the strings are relatively small
      (maximum 100), this direct iteration approach is highly efficient and straightforward
      to implement.'
    time_complexity: O(N * M * K) where N is the number of patterns, M is the maximum
      length of a pattern, and K is the length of the target word. This assumes a naive
      substring search implementation; however, many built-in string search algorithms
      are optimized to perform closer to linear time relative to the search space.
    space_complexity: O(1) excluding the input storage. The algorithm only uses a constant
      amount of extra space for the loop index and the counter variable, making it space-efficient.
    elapsed_time: 253.6768922805786
    model: gemini-3-flash-preview
    generated_at: '2026-06-29 02:49:08 '
---

## Problem #1967: Number of Strings That Appear as Substrings in Word

**Difficulty:** Easy

**Topics:** Array, String

## Problem Description

<p>Given an array of strings <code>patterns</code> and a string <code>word</code>, return <em>the <strong>number</strong> of strings in </em><code>patterns</code><em> that exist as a <strong>substring</strong> in </em><code>word</code>.</p>

<p>A <strong>substring</strong> is a contiguous sequence of characters within a string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> patterns = [&quot;a&quot;,&quot;abc&quot;,&quot;bc&quot;,&quot;d&quot;], word = &quot;abc&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong>
- &quot;a&quot; appears as a substring in &quot;<u>a</u>bc&quot;.
- &quot;abc&quot; appears as a substring in &quot;<u>abc</u>&quot;.
- &quot;bc&quot; appears as a substring in &quot;a<u>bc</u>&quot;.
- &quot;d&quot; does not appear as a substring in &quot;abc&quot;.
3 of the strings in patterns appear as a substring in word.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> patterns = [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;], word = &quot;aaaaabbbbb&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong>
- &quot;a&quot; appears as a substring in &quot;a<u>a</u>aaabbbbb&quot;.
- &quot;b&quot; appears as a substring in &quot;aaaaabbbb<u>b</u>&quot;.
- &quot;c&quot; does not appear as a substring in &quot;aaaaabbbbb&quot;.
2 of the strings in patterns appear as a substring in word.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> patterns = [&quot;a&quot;,&quot;a&quot;,&quot;a&quot;], word = &quot;ab&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> Each of the patterns appears as a substring in word &quot;<u>a</u>b&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= patterns.length &lt;= 100</code></li>
	<li><code>1 &lt;= patterns[i].length &lt;= 100</code></li>
	<li><code>1 &lt;= word.length &lt;= 100</code></li>
	<li><code>patterns[i]</code> and <code>word</code> consist of lowercase English letters.</li>
</ul>


## Hints

1. Deal with each of the patterns individually.

2. Use the built-in function in the language you are using to find if the pattern exists as a substring in `word`.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The core approach involves iterating through each string in the provided patterns array and checking if it exists as a contiguous substring within the target word. We maintain a running counter to track how many patterns satisfy this condition. For each pattern, we utilize the language's native string searching functionality to determine presence.

Built-in functions such as 'contains' in Java and C#, 'find' in C++, 'strstr' in C, 'includes' in JavaScript, and the 'in' operator in Python provide an efficient and readable way to perform these checks. Since the constraints for both the number of patterns and the lengths of the strings are relatively small (maximum 100), this direct iteration approach is highly efficient and straightforward to implement.

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
    int numOfStrings(vector<string>& patterns, string word) {
        int count = 0;
        for (const string& p : patterns) {
            if (word.find(p) != string::npos) {
                count++;
            }
        }
        return count;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int numOfStrings(String[] patterns, String word) {
        int count = 0;
        for (String p : patterns) {
            if (word.contains(p)) {
                count++;
            }
        }
        return count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        count = 0
        for p in patterns:
            if p in word:
                count += 1
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for p in patterns:
            if p in word:
                count += 1
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <string.h>

int numOfStrings(char** patterns, int patternsSize, char* word) {
    int count = 0;
    for (int i = 0; i < patternsSize; i++) {
        if (strstr(word, patterns[i]) != NULL) {
            count++;
        }
    }
    return count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int NumOfStrings(string[] patterns, string word) {
        int count = 0;
        foreach (string p in patterns) {
            if (word.Contains(p)) {
                count++;
            }
        }
        return count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string[]} patterns
 * @param {string} word
 * @return {number}
 */
var numOfStrings = function(patterns, word) {
    let count = 0;
    for (let i = 0; i < patterns.length; i++) {
        if (word.includes(patterns[i])) {
            count++;
        }
    }
    return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function numOfStrings(patterns: string[], word: string): number {
    let count = 0;
    for (const pattern of patterns) {
        if (word.includes(pattern)) {
            count++;
        }
    }
    return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String[] $patterns
     * @param String $word
     * @return Integer
     */
    function numOfStrings($patterns, $word) {
        $count = 0;
        foreach ($patterns as $pattern) {
            if (strpos($word, $pattern) !== false) {
                $count++;
            }
        }
        return $count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func numOfStrings(_ patterns: [String], _ word: String) -> Int {
        var count = 0
        for pattern in patterns {
            if word.contains(pattern) {
                count += 1
            }
        }
        return count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun numOfStrings(patterns: Array<String>, word: String): Int {
        var count = 0
        for (pattern in patterns) {
            if (word.contains(pattern)) {
                count++
            }
        }
        return count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int numOfStrings(List<String> patterns, String word) {
    int count = 0;
    for (final pattern in patterns) {
      if (word.contains(pattern)) {
        count++;
      }
    }
    return count;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "strings"

func numOfStrings(patterns []string, word string) int {
    count := 0
    for _, pattern := range patterns {
        if strings.Contains(word, pattern) {
            count++
        }
    }
    return count
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String[]} patterns
# @param {String} word
# @return {Integer}
def num_of_strings(patterns, word)
  patterns.count { |p| word.include?(p) }
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def numOfStrings(patterns: Array[String], word: String): Int = {
        patterns.count(p => word.contains(p))
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn num_of_strings(patterns: Vec<String>, word: String) -> i32 {
        patterns.iter().filter(|p| word.contains(p.as_str())).count() as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(require racket/string)

(define/contract (num-of-strings patterns word)
  (-> (listof string?) string? exact-integer?)
  (length (filter (lambda (p) (string-contains? word p)) patterns)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec num_of_strings(Patterns :: [unicode:unicode_binary()], Word :: unicode:unicode_binary()) -> integer().
num_of_strings(Patterns, Word) ->
  length([P || P <- Patterns, binary:match(Word, P) =/= nomatch]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec num_of_strings(patterns :: [String.t], word :: String.t) :: integer
  def num_of_strings(patterns, word) do
    Enum.count(patterns, fn p -> String.contains?(word, p) end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N * M * K) where N is the number of patterns, M is the maximum length of a pattern, and K is the length of the target word. This assumes a naive substring search implementation; however, many built-in string search algorithms are optimized to perform closer to linear time relative to the search space.
- **Space Complexity:** O(1) excluding the input storage. The algorithm only uses a constant amount of extra space for the loop index and the counter variable, making it space-efficient.
