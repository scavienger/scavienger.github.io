---
layout: post
title: "Count the Number of Special Characters I"
date: 2026-05-26 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Hash Table", "String"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/count-the-number-of-special-characters-i/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int numberOfSpecialChars(string word) {\n\
        \        bool lower[26] = {false};\n        bool upper[26] = {false};\n    \
        \    for (char c : word) {\n            if (c >= 'a' && c <= 'z') {\n      \
        \          lower[c - 'a'] = true;\n            } else if (c >= 'A' && c <= 'Z')\
        \ {\n                upper[c - 'A'] = true;\n            }\n        }\n    \
        \    int count = 0;\n        for (int i = 0; i < 26; ++i) {\n            if\
        \ (lower[i] && upper[i]) {\n                count++;\n            }\n      \
        \  }\n        return count;\n    }\n};"
      java: "class Solution {\n    public int numberOfSpecialChars(String word) {\n\
        \        boolean[] lower = new boolean[26];\n        boolean[] upper = new boolean[26];\n\
        \        for (char c : word.toCharArray()) {\n            if (c >= 'a' && c\
        \ <= 'z') {\n                lower[c - 'a'] = true;\n            } else if (c\
        \ >= 'A' && c <= 'Z') {\n                upper[c - 'A'] = true;\n          \
        \  }\n        }\n        int count = 0;\n        for (int i = 0; i < 26; i++)\
        \ {\n            if (lower[i] && upper[i]) {\n                count++;\n   \
        \         }\n        }\n        return count;\n    }\n}"
      python: "class Solution(object):\n    def numberOfSpecialChars(self, word):\n\
        \        \"\"\"\n        :type word: str\n        :rtype: int\n        \"\"\"\
        \n        char_set = set(word)\n        count = 0\n        for i in range(26):\n\
        \            lower = chr(ord('a') + i)\n            upper = chr(ord('A') + i)\n\
        \            if lower in char_set and upper in char_set:\n                count\
        \ += 1\n        return count"
      python3: "class Solution:\n    def numberOfSpecialChars(self, word: str) -> int:\n\
        \        char_set = set(word)\n        count = 0\n        for i in range(26):\n\
        \            lower = chr(ord('a') + i)\n            upper = chr(ord('A') + i)\n\
        \            if lower in char_set and upper in char_set:\n                count\
        \ += 1\n        return count"
      c: "int numberOfSpecialChars(char* word) {\n    int lower[26] = {0};\n    int\
        \ upper[26] = {0};\n    for (int i = 0; word[i] != '\\0'; i++) {\n        if\
        \ (word[i] >= 'a' && word[i] <= 'z') {\n            lower[word[i] - 'a'] = 1;\n\
        \        } else if (word[i] >= 'A' && word[i] <= 'Z') {\n            upper[word[i]\
        \ - 'A'] = 1;\n        }\n    }\n    int count = 0;\n    for (int i = 0; i <\
        \ 26; i++) {\n        if (lower[i] && upper[i]) {\n            count++;\n  \
        \      }\n    }\n    return count;\n}"
      csharp: "public class Solution {\n    public int NumberOfSpecialChars(string word)\
        \ {\n        bool[] lower = new bool[26];\n        bool[] upper = new bool[26];\n\
        \        foreach (char c in word) {\n            if (c >= 'a' && c <= 'z') {\n\
        \                lower[c - 'a'] = true;\n            } else if (c >= 'A' &&\
        \ c <= 'Z') {\n                upper[c - 'A'] = true;\n            }\n     \
        \   }\n        int count = 0;\n        for (int i = 0; i < 26; i++) {\n    \
        \        if (lower[i] && upper[i]) {\n                count++;\n           \
        \ }\n        }\n        return count;\n    }\n}"
      javascript: "/**\n * @param {string} word\n * @return {number}\n */\nvar numberOfSpecialChars\
        \ = function(word) {\n    const charSet = new Set(word);\n    let count = 0;\n\
        \    const aCode = 'a'.charCodeAt(0);\n    const ACode = 'A'.charCodeAt(0);\n\
        \    for (let i = 0; i < 26; i++) {\n        const lower = String.fromCharCode(aCode\
        \ + i);\n        const upper = String.fromCharCode(ACode + i);\n        if (charSet.has(lower)\
        \ && charSet.has(upper)) {\n            count++;\n        }\n    }\n    return\
        \ count;\n};"
      typescript: "function numberOfSpecialChars(word: string): number {\n    const\
        \ lower = new Set<string>();\n    const upper = new Set<string>();\n\n    for\
        \ (let i = 0; i < word.length; i++) {\n        const char = word[i];\n     \
        \   if (char >= 'a' && char <= 'z') {\n            lower.add(char);\n      \
        \  } else if (char >= 'A' && char <= 'Z') {\n            upper.add(char.toLowerCase());\n\
        \        }\n    }\n\n    let count = 0;\n    lower.forEach((char) => {\n   \
        \     if (upper.has(char)) {\n            count++;\n        }\n    });\n\n \
        \   return count;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $word\n     * @return\
        \ Integer\n     */\n    function numberOfSpecialChars($word) {\n        $lower\
        \ = array_fill(0, 26, false);\n        $upper = array_fill(0, 26, false);\n\
        \        $len = strlen($word);\n\n        for ($i = 0; $i < $len; $i++) {\n\
        \            $ascii = ord($word[$i]);\n            if ($ascii >= 97 && $ascii\
        \ <= 122) {\n                $lower[$ascii - 97] = true;\n            } else\
        \ if ($ascii >= 65 && $ascii <= 90) {\n                $upper[$ascii - 65] =\
        \ true;\n            }\n        }\n\n        $count = 0;\n        for ($i =\
        \ 0; $i < 26; $i++) {\n            if ($lower[$i] && $upper[$i]) {\n       \
        \         $count++;\n            }\n        }\n\n        return $count;\n  \
        \  }\n}"
      swift: "class Solution {\n    func numberOfSpecialChars(_ word: String) -> Int\
        \ {\n        var lowerFound = Set<Character>()\n        var upperFound = Set<Character>()\n\
        \n        for char in word {\n            if char.isLowercase {\n          \
        \      lowerFound.insert(char)\n            } else if char.isUppercase {\n \
        \               upperFound.insert(Character(char.lowercased()))\n          \
        \  }\n        }\n\n        var specialCount = 0\n        for char in lowerFound\
        \ {\n            if upperFound.contains(char) {\n                specialCount\
        \ += 1\n            }\n        }\n\n        return specialCount\n    }\n}"
      kotlin: "class Solution {\n    fun numberOfSpecialChars(word: String): Int {\n\
        \        val lower = BooleanArray(26)\n        val upper = BooleanArray(26)\n\
        \n        for (char in word) {\n            if (char in 'a'..'z') {\n      \
        \          lower[char - 'a'] = true\n            } else if (char in 'A'..'Z')\
        \ {\n                upper[char - 'A'] = true\n            }\n        }\n\n\
        \        var count = 0\n        for (i in 0 until 26) {\n            if (lower[i]\
        \ && upper[i]) {\n                count++\n            }\n        }\n\n    \
        \    return count\n    }\n}"
      dart: "class Solution {\n  int numberOfSpecialChars(String word) {\n    Set<int>\
        \ lower = {};\n    Set<int> upper = {};\n    int codeA = 'a'.codeUnitAt(0);\n\
        \    int codeZ = 'z'.codeUnitAt(0);\n    int codeCapA = 'A'.codeUnitAt(0);\n\
        \    int codeCapZ = 'Z'.codeUnitAt(0);\n\n    for (int i = 0; i < word.length;\
        \ i++) {\n      int unit = word.codeUnitAt(i);\n      if (unit >= codeA && unit\
        \ <= codeZ) {\n        lower.add(unit);\n      } else if (unit >= codeCapA &&\
        \ unit <= codeCapZ) {\n        upper.add(unit - codeCapA + codeA);\n      }\n\
        \    }\n\n    int count = 0;\n    for (int unit in lower) {\n      if (upper.contains(unit))\
        \ {\n        count++;\n      }\n    }\n\n    return count;\n  }\n}"
      go: "func numberOfSpecialChars(word string) int {\n    var lower [26]bool\n  \
        \  var upper [26]bool\n\n    for _, char := range word {\n        if char >=\
        \ 'a' && char <= 'z' {\n            lower[char-'a'] = true\n        } else if\
        \ char >= 'A' && char <= 'Z' {\n            upper[char-'A'] = true\n       \
        \ }\n    }\n\n    count := 0\n    for i := 0; i < 26; i++ {\n        if lower[i]\
        \ && upper[i] {\n            count++\n        }\n    }\n\n    return count\n\
        }"
      ruby: "def number_of_special_chars(word)\n  ('a'..'z').count { |c| word.include?(c)\
        \ && word.include?(c.upcase) }\nend"
      scala: "object Solution {\n  def numberOfSpecialChars(word: String): Int = {\n\
        \    val charSet = word.toSet\n    ('a' to 'z').count(c => charSet.contains(c)\
        \ && charSet.contains(c.toUpper))\n  }\n}"
      rust: "use std::collections::HashSet;\n\nimpl Solution {\n    pub fn number_of_special_chars(word:\
        \ String) -> i32 {\n        let set: HashSet<char> = word.chars().collect();\n\
        \        ('a'..='z')\n            .filter(|&c| set.contains(&c) && set.contains(&c.to_ascii_uppercase()))\n\
        \            .count() as i32\n    }\n}"
      racket: "(define/contract (number-of-special-chars word)\n  (-> string? exact-integer?)\n\
        \  (let ([chars (string->list word)])\n    (for/sum ([i (in-range 97 123)])\n\
        \      (let ([l (integer->char i)]\n            [u (char-upcase (integer->char\
        \ i))])\n        (if (and (member l chars) (member u chars)) 1 0)))))"
      erlang: "number_of_special_chars(Word) ->\n  List = binary_to_list(Word),\n  SpecialChars\
        \ = [C || C <- lists:seq($a, $z), lists:member(C, List), lists:member(C - 32,\
        \ List)],\n  length(SpecialChars)."
      elixir: "defmodule Solution do\n  @spec number_of_special_chars(word :: String.t)\
        \ :: integer\n  def number_of_special_chars(word) do\n    char_list = String.to_charlist(word)\n\
        \    Enum.count(?a..?z, fn c ->\n      Enum.member?(char_list, c) and Enum.member?(char_list,\
        \ c - 32)\n    end)\n  end\nend"
    approach: 'To determine the number of special letters, we track the presence of
      every character in the string by categorizing them into lowercase and uppercase
      occurrences. Since only English letters are involved, we can efficiently record
      whether each letter from ''a'' through ''z'' and ''A'' through ''Z'' has appeared
      at least once by utilizing boolean arrays of size 26 or a hash set to store all
      unique characters from the input string.


      After processing the entire string, we iterate through the 26 possible letters
      of the English alphabet. For each index, we check if both the lowercase and uppercase
      variants of that letter were flagged as present. If both conditions are satisfied,
      we increment a counter. This approach ensures that each character is only counted
      once as special, regardless of its frequency or positions within the string.'
    time_complexity: O(N + A), where N is the length of the string and A is the size
      of the English alphabet (26). We iterate through the string once to populate our
      tracking data structure and then perform a fixed-count iteration over the alphabet
      to count matches. Since A is constant, the overall complexity simplifies to O(N).
    space_complexity: O(A), where A is the size of the English alphabet. We use fixed-size
      boolean arrays or a set to store character presence. Since the alphabet size is
      constant (26), the space required does not grow with the size of the input string,
      effectively making it O(1) in terms of auxiliary space.
    elapsed_time: 294.675822019577
    model: gemini-3-flash-preview
    generated_at: '2026-05-26 02:37:59 '
---

## Problem #3120: Count the Number of Special Characters I

**Difficulty:** Easy

**Topics:** Hash Table, String

## Problem Description

<p>You are given a string <code>word</code>. A letter is called <strong>special</strong> if it appears <strong>both</strong> in lowercase and uppercase in <code>word</code>.</p>

<p>Return the number of<em> </em><strong>special</strong> letters in<em> </em><code>word</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = &quot;aaAbcBC&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>The special characters in <code>word</code> are <code>&#39;a&#39;</code>, <code>&#39;b&#39;</code>, and <code>&#39;c&#39;</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = &quot;abc&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>No character in <code>word</code> appears in uppercase.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = &quot;abBCab&quot;</span></p>

<p><strong>Output:</strong> 1</p>

<p><strong>Explanation:</strong></p>

<p>The only special character in <code>word</code> is <code>&#39;b&#39;</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 50</code></li>
	<li><code>word</code> consists of only lowercase and uppercase English letters.</li>
</ul>


## Hints

1. The constraints are small. For all 52 characters, check if they are present in `word`.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To determine the number of special letters, we track the presence of every character in the string by categorizing them into lowercase and uppercase occurrences. Since only English letters are involved, we can efficiently record whether each letter from 'a' through 'z' and 'A' through 'Z' has appeared at least once by utilizing boolean arrays of size 26 or a hash set to store all unique characters from the input string.

After processing the entire string, we iterate through the 26 possible letters of the English alphabet. For each index, we check if both the lowercase and uppercase variants of that letter were flagged as present. If both conditions are satisfied, we increment a counter. This approach ensures that each character is only counted once as special, regardless of its frequency or positions within the string.

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
    int numberOfSpecialChars(string word) {
        bool lower[26] = {false};
        bool upper[26] = {false};
        for (char c : word) {
            if (c >= 'a' && c <= 'z') {
                lower[c - 'a'] = true;
            } else if (c >= 'A' && c <= 'Z') {
                upper[c - 'A'] = true;
            }
        }
        int count = 0;
        for (int i = 0; i < 26; ++i) {
            if (lower[i] && upper[i]) {
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
    public int numberOfSpecialChars(String word) {
        boolean[] lower = new boolean[26];
        boolean[] upper = new boolean[26];
        for (char c : word.toCharArray()) {
            if (c >= 'a' && c <= 'z') {
                lower[c - 'a'] = true;
            } else if (c >= 'A' && c <= 'Z') {
                upper[c - 'A'] = true;
            }
        }
        int count = 0;
        for (int i = 0; i < 26; i++) {
            if (lower[i] && upper[i]) {
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
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        char_set = set(word)
        count = 0
        for i in range(26):
            lower = chr(ord('a') + i)
            upper = chr(ord('A') + i)
            if lower in char_set and upper in char_set:
                count += 1
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        char_set = set(word)
        count = 0
        for i in range(26):
            lower = chr(ord('a') + i)
            upper = chr(ord('A') + i)
            if lower in char_set and upper in char_set:
                count += 1
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int numberOfSpecialChars(char* word) {
    int lower[26] = {0};
    int upper[26] = {0};
    for (int i = 0; word[i] != '\0'; i++) {
        if (word[i] >= 'a' && word[i] <= 'z') {
            lower[word[i] - 'a'] = 1;
        } else if (word[i] >= 'A' && word[i] <= 'Z') {
            upper[word[i] - 'A'] = 1;
        }
    }
    int count = 0;
    for (int i = 0; i < 26; i++) {
        if (lower[i] && upper[i]) {
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
    public int NumberOfSpecialChars(string word) {
        bool[] lower = new bool[26];
        bool[] upper = new bool[26];
        foreach (char c in word) {
            if (c >= 'a' && c <= 'z') {
                lower[c - 'a'] = true;
            } else if (c >= 'A' && c <= 'Z') {
                upper[c - 'A'] = true;
            }
        }
        int count = 0;
        for (int i = 0; i < 26; i++) {
            if (lower[i] && upper[i]) {
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
 * @param {string} word
 * @return {number}
 */
var numberOfSpecialChars = function(word) {
    const charSet = new Set(word);
    let count = 0;
    const aCode = 'a'.charCodeAt(0);
    const ACode = 'A'.charCodeAt(0);
    for (let i = 0; i < 26; i++) {
        const lower = String.fromCharCode(aCode + i);
        const upper = String.fromCharCode(ACode + i);
        if (charSet.has(lower) && charSet.has(upper)) {
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
function numberOfSpecialChars(word: string): number {
    const lower = new Set<string>();
    const upper = new Set<string>();

    for (let i = 0; i < word.length; i++) {
        const char = word[i];
        if (char >= 'a' && char <= 'z') {
            lower.add(char);
        } else if (char >= 'A' && char <= 'Z') {
            upper.add(char.toLowerCase());
        }
    }

    let count = 0;
    lower.forEach((char) => {
        if (upper.has(char)) {
            count++;
        }
    });

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
     * @param String $word
     * @return Integer
     */
    function numberOfSpecialChars($word) {
        $lower = array_fill(0, 26, false);
        $upper = array_fill(0, 26, false);
        $len = strlen($word);

        for ($i = 0; $i < $len; $i++) {
            $ascii = ord($word[$i]);
            if ($ascii >= 97 && $ascii <= 122) {
                $lower[$ascii - 97] = true;
            } else if ($ascii >= 65 && $ascii <= 90) {
                $upper[$ascii - 65] = true;
            }
        }

        $count = 0;
        for ($i = 0; $i < 26; $i++) {
            if ($lower[$i] && $upper[$i]) {
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
    func numberOfSpecialChars(_ word: String) -> Int {
        var lowerFound = Set<Character>()
        var upperFound = Set<Character>()

        for char in word {
            if char.isLowercase {
                lowerFound.insert(char)
            } else if char.isUppercase {
                upperFound.insert(Character(char.lowercased()))
            }
        }

        var specialCount = 0
        for char in lowerFound {
            if upperFound.contains(char) {
                specialCount += 1
            }
        }

        return specialCount
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun numberOfSpecialChars(word: String): Int {
        val lower = BooleanArray(26)
        val upper = BooleanArray(26)

        for (char in word) {
            if (char in 'a'..'z') {
                lower[char - 'a'] = true
            } else if (char in 'A'..'Z') {
                upper[char - 'A'] = true
            }
        }

        var count = 0
        for (i in 0 until 26) {
            if (lower[i] && upper[i]) {
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
  int numberOfSpecialChars(String word) {
    Set<int> lower = {};
    Set<int> upper = {};
    int codeA = 'a'.codeUnitAt(0);
    int codeZ = 'z'.codeUnitAt(0);
    int codeCapA = 'A'.codeUnitAt(0);
    int codeCapZ = 'Z'.codeUnitAt(0);

    for (int i = 0; i < word.length; i++) {
      int unit = word.codeUnitAt(i);
      if (unit >= codeA && unit <= codeZ) {
        lower.add(unit);
      } else if (unit >= codeCapA && unit <= codeCapZ) {
        upper.add(unit - codeCapA + codeA);
      }
    }

    int count = 0;
    for (int unit in lower) {
      if (upper.contains(unit)) {
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
func numberOfSpecialChars(word string) int {
    var lower [26]bool
    var upper [26]bool

    for _, char := range word {
        if char >= 'a' && char <= 'z' {
            lower[char-'a'] = true
        } else if char >= 'A' && char <= 'Z' {
            upper[char-'A'] = true
        }
    }

    count := 0
    for i := 0; i < 26; i++ {
        if lower[i] && upper[i] {
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
def number_of_special_chars(word)
  ('a'..'z').count { |c| word.include?(c) && word.include?(c.upcase) }
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def numberOfSpecialChars(word: String): Int = {
    val charSet = word.toSet
    ('a' to 'z').count(c => charSet.contains(c) && charSet.contains(c.toUpper))
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::HashSet;

impl Solution {
    pub fn number_of_special_chars(word: String) -> i32 {
        let set: HashSet<char> = word.chars().collect();
        ('a'..='z')
            .filter(|&c| set.contains(&c) && set.contains(&c.to_ascii_uppercase()))
            .count() as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (number-of-special-chars word)
  (-> string? exact-integer?)
  (let ([chars (string->list word)])
    (for/sum ([i (in-range 97 123)])
      (let ([l (integer->char i)]
            [u (char-upcase (integer->char i))])
        (if (and (member l chars) (member u chars)) 1 0)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
number_of_special_chars(Word) ->
  List = binary_to_list(Word),
  SpecialChars = [C || C <- lists:seq($a, $z), lists:member(C, List), lists:member(C - 32, List)],
  length(SpecialChars).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec number_of_special_chars(word :: String.t) :: integer
  def number_of_special_chars(word) do
    char_list = String.to_charlist(word)
    Enum.count(?a..?z, fn c ->
      Enum.member?(char_list, c) and Enum.member?(char_list, c - 32)
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N + A), where N is the length of the string and A is the size of the English alphabet (26). We iterate through the string once to populate our tracking data structure and then perform a fixed-count iteration over the alphabet to count matches. Since A is constant, the overall complexity simplifies to O(N).
- **Space Complexity:** O(A), where A is the size of the English alphabet. We use fixed-size boolean arrays or a set to store character presence. Since the alphabet size is constant (26), the space required does not grow with the size of the input string, effectively making it O(1) in terms of auxiliary space.
