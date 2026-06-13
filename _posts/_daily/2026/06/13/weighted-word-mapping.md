---
layout: post
title: "Weighted Word Mapping"
date: 2026-06-13 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "String", "Simulation"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/weighted-word-mapping/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    string mapWordWeights(vector<string>& words,\
        \ vector<int>& weights) {\n        string result = \"\";\n        for (const\
        \ string& word : words) {\n            int weightSum = 0;\n            for (char\
        \ c : word) {\n                weightSum += weights[c - 'a'];\n            }\n\
        \            int rem = weightSum % 26;\n            char mappedChar = (char)('z'\
        \ - rem);\n            result += mappedChar;\n        }\n        return result;\n\
        \    }\n};"
      java: "class Solution {\n    public String mapWordWeights(String[] words, int[]\
        \ weights) {\n        StringBuilder sb = new StringBuilder();\n        for (String\
        \ word : words) {\n            int weightSum = 0;\n            for (int i =\
        \ 0; i < word.length(); i++) {\n                weightSum += weights[word.charAt(i)\
        \ - 'a'];\n            }\n            int rem = weightSum % 26;\n          \
        \  sb.append((char) ('z' - rem));\n        }\n        return sb.toString();\n\
        \    }\n}"
      python: "class Solution(object):\n    def mapWordWeights(self, words, weights):\n\
        \        \"\"\"\n        :type words: List[str]\n        :type weights: List[int]\n\
        \        :rtype: str\n        \"\"\"\n        result = []\n        for word\
        \ in words:\n            weight_sum = 0\n            for char in word:\n   \
        \             weight_sum += weights[ord(char) - ord('a')]\n            rem =\
        \ weight_sum % 26\n            result.append(chr(ord('z') - rem))\n        return\
        \ \"\".join(result)"
      python3: "class Solution:\n    def mapWordWeights(self, words: List[str], weights:\
        \ List[int]) -> str:\n        result = []\n        for word in words:\n    \
        \        weight_sum = sum(weights[ord(c) - ord('a')] for c in word)\n      \
        \      rem = weight_sum % 26\n            result.append(chr(ord('z') - rem))\n\
        \        return \"\".join(result)"
      c: "#include <stdlib.h>\n#include <string.h>\n\nchar* mapWordWeights(char** words,\
        \ int wordsSize, int* weights, int weightsSize) {\n    char* result = (char*)malloc((wordsSize\
        \ + 1) * sizeof(char));\n    if (!result) return NULL;\n    for (int i = 0;\
        \ i < wordsSize; i++) {\n        int weightSum = 0;\n        char* currentWord\
        \ = words[i];\n        while (*currentWord) {\n            weightSum += weights[*currentWord\
        \ - 'a'];\n            currentWord++;\n        }\n        int rem = weightSum\
        \ % 26;\n        result[i] = (char)('z' - rem);\n    }\n    result[wordsSize]\
        \ = '\\0';\n    return result;\n}"
      csharp: "public class Solution {\n    public string MapWordWeights(string[] words,\
        \ int[] weights) {\n        char[] result = new char[words.Length];\n      \
        \  for (int i = 0; i < words.Length; i++) {\n            int weightSum = 0;\n\
        \            foreach (char c in words[i]) {\n                weightSum += weights[c\
        \ - 'a'];\n            }\n            int rem = weightSum % 26;\n          \
        \  result[i] = (char)('z' - rem);\n        }\n        return new string(result);\n\
        \    }\n}"
      javascript: "/**\n * @param {string[]} words\n * @param {number[]} weights\n *\
        \ @return {string}\n */\nvar mapWordWeights = function(words, weights) {\n \
        \   let result = \"\";\n    for (let word of words) {\n        let weightSum\
        \ = 0;\n        for (let i = 0; i < word.length; i++) {\n            weightSum\
        \ += weights[word.charCodeAt(i) - 97];\n        }\n        let rem = weightSum\
        \ % 26;\n        result += String.fromCharCode(122 - rem);\n    }\n    return\
        \ result;\n};"
      typescript: "function mapWordWeights(words: string[], weights: number[]): string\
        \ {\n    let result = \"\";\n    for (const word of words) {\n        let sum\
        \ = 0;\n        for (let i = 0; i < word.length; i++) {\n            sum +=\
        \ weights[word.charCodeAt(i) - 97];\n        }\n        const index = sum %\
        \ 26;\n        result += String.fromCharCode(122 - index);\n    }\n    return\
        \ result;\n};"
      php: "class Solution {\n\n    /**\n     * @param String[] $words\n     * @param\
        \ Integer[] $weights\n     * @return String\n     */\n    function mapWordWeights($words,\
        \ $weights) {\n        $result = \"\";\n        foreach ($words as $word) {\n\
        \            $sum = 0;\n            $len = strlen($word);\n            for ($i\
        \ = 0; $i < $len; $i++) {\n                $sum += $weights[ord($word[$i]) -\
        \ 97];\n            }\n            $result .= chr(122 - ($sum % 26));\n    \
        \    }\n        return $result;\n    }\n}"
      swift: "class Solution {\n    func mapWordWeights(_ words: [String], _ weights:\
        \ [Int]) -> String {\n        var result = \"\"\n        for word in words {\n\
        \            var sum = 0\n            for scalar in word.utf8 {\n          \
        \      sum += weights[Int(scalar) - 97]\n            }\n            let index\
        \ = sum % 26\n            if let unicodeScalar = UnicodeScalar(122 - index)\
        \ {\n                result.append(Character(unicodeScalar))\n            }\n\
        \        }\n        return result\n    }\n}"
      kotlin: "class Solution {\n    fun mapWordWeights(words: Array<String>, weights:\
        \ IntArray): String {\n        val result = StringBuilder()\n        for (word\
        \ in words) {\n            var sum = 0\n            for (char in word) {\n \
        \               sum += weights[char - 'a']\n            }\n            val index\
        \ = sum % 26\n            result.append(('z'.toInt() - index).toChar())\n  \
        \      }\n        return result.toString()\n    }\n}"
      dart: "class Solution {\n  String mapWordWeights(List<String> words, List<int>\
        \ weights) {\n    String result = \"\";\n    for (var word in words) {\n   \
        \   int sum = 0;\n      for (int i = 0; i < word.length; i++) {\n        sum\
        \ += weights[word.codeUnitAt(i) - 97];\n      }\n      int index = sum % 26;\n\
        \      result += String.fromCharCode(122 - index);\n    }\n    return result;\n\
        \  }\n}"
      go: "func mapWordWeights(words []string, weights []int) string {\n    res := make([]byte,\
        \ len(words))\n    for i, word := range words {\n        sum := 0\n        for\
        \ j := 0; j < len(word); j++ {\n            sum += weights[int(word[j]-'a')]\n\
        \        }\n        res[i] = 'z' - byte(sum%26)\n    }\n    return string(res)\n\
        }"
      ruby: "# @param {String[]} words\n# @param {Integer[]} weights\n# @return {String}\n\
        def map_word_weights(words, weights)\n  words.map do |word|\n    sum = word.bytes.reduce(0)\
        \ { |acc, b| acc + weights[b - 97] }\n    (122 - (sum % 26)).chr\n  end.join\n\
        end"
      scala: "object Solution {\n    def mapWordWeights(words: Array[String], weights:\
        \ Array[Int]): String = {\n        words.map { word =>\n            val weightSum\
        \ = word.map(c => weights(c - 'a')).sum\n            ('z'.toInt - (weightSum\
        \ % 26)).toChar\n        }.mkString\n    }\n}"
      rust: "impl Solution {\n    pub fn map_word_weights(words: Vec<String>, weights:\
        \ Vec<i32>) -> String {\n        words.iter().map(|word| {\n            let\
        \ weight_sum: i32 = word.chars().map(|c| weights[(c as usize) - ('a' as usize)]).sum();\n\
        \            let rem = weight_sum % 26;\n            ((b'z' - (rem as u8)) as\
        \ char)\n        }).collect()\n    }\n}"
      racket: "(define/contract (map-word-weights words weights)\n  (-> (listof string?)\
        \ (listof exact-integer?) string?)\n  (apply string\n         (map (lambda (word)\n\
        \                (let* ([chars (string->list word)]\n                      \
        \ [char-weights (map (lambda (c)\n                                         \
        \   (list-ref weights (- (char->integer c) (char->integer #\\a))))\n       \
        \                                   chars)]\n                       [total-weight\
        \ (apply + char-weights)]\n                       [rem (modulo total-weight\
        \ 26)])\n                  (integer->char (- (char->integer #\\z) rem))))\n\
        \              words)))"
      erlang: "-spec map_word_weights(Words :: [unicode:unicode_binary()], Weights ::\
        \ [integer()]) -> unicode:unicode_binary().\nmap_word_weights(Words, Weights)\
        \ ->\n  WeightsTuple = list_to_tuple(Weights),\n  Mapped = [begin\n        \
        \      WordList = unicode:characters_to_list(Word),\n              Sum = lists:foldl(fun(C,\
        \ Acc) -> Acc + element(C - $a + 1, WeightsTuple) end, 0, WordList),\n     \
        \         $z - (Sum rem 26)\n            end || Word <- Words],\n  unicode:characters_to_binary(Mapped)."
      elixir: "defmodule Solution do\n  @spec map_word_weights(words :: [String.t],\
        \ weights :: [integer]) :: String.t\n  def map_word_weights(words, weights)\
        \ do\n    weights_tuple = List.to_tuple(weights)\n    words\n    |> Enum.map(fn\
        \ word ->\n      sum = word\n      |> String.to_charlist()\n      |> Enum.reduce(0,\
        \ fn c, acc -> acc + elem(weights_tuple, c - ?a) end)\n      rem_val = rem(sum,\
        \ 26)\n      <<?z - rem_val>>\n    end)\n    |> Enum.join(\"\")\n  end\nend"
    approach: 'The core of the algorithm involves calculating a numerical weight for
      each word in the input array. For every word, we iterate through its characters,
      converting each lowercase English letter to its zero-based alphabetical index
      (where ''a'' is 0, ''b'' is 1, and so on) and then retrieving the corresponding
      value from the provided weights array. These values are summed to find the total
      weight of the word, which is then reduced modulo 26.


      To perform the mapping to a character in reverse alphabetical order, we subtract
      the result of the modulo operation from the character ''z''. In this mapping scheme,
      a result of 0 yields ''z'', 1 yields ''y'', and 25 yields ''a''. Each resulting
      character is collected and finally concatenated into a single string to form the
      final result.'
    time_complexity: O(N ⋅ L), where N is the number of words and L is the average length
      of each word. We process every character of every word exactly once to compute
      the weights. The constant time lookup for weights and the character mapping operations
      do not depend on the input size beyond the 26-element weights array.
    space_complexity: O(N), where N is the number of words. We store the resulting string
      which contains one character for every input word. Additional auxiliary space
      used for calculations is constant, O(1).
    elapsed_time: 68.30569410324097
    model: gemini-3-flash-preview
    generated_at: '2026-06-13 02:42:09 '
---

## Problem #3838: Weighted Word Mapping

**Difficulty:** Easy

**Topics:** Array, String, Simulation

## Problem Description

<p>You are given an array of strings <code>words</code>, where each string represents a word containing lowercase English letters.</p>

<p>You are also given an integer array <code>weights</code> of length 26, where <code>weights[i]</code> represents the weight of the <code>i<sup>th</sup></code> lowercase English letter.</p>

<p>The <strong>weight</strong> of a word is defined as the <strong>sum</strong> of the weights of its characters.</p>

<p>For each word, take its weight modulo 26 and map the result to a lowercase English letter using reverse alphabetical order (<code>0 -&gt; &#39;z&#39;, 1 -&gt; &#39;y&#39;, ..., 25 -&gt; &#39;a&#39;</code>).</p>

<p>Return a string formed by concatenating the mapped characters for all words in order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">words = [&quot;abcd&quot;,&quot;def&quot;,&quot;xyz&quot;], weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;rij&quot;</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The weight of <code>&quot;abcd&quot;</code> is <code>5 + 3 + 12 + 14 = 34</code>. The result modulo 26 is <code>34 % 26 = 8</code>, which maps to <code>&#39;r&#39;</code>.</li>
	<li>The weight of <code>&quot;def&quot;</code> is <code>14 + 1 + 2 = 17</code>. The result modulo 26 is <code>17 % 26 = 17</code>, which maps to <code>&#39;i&#39;</code>.</li>
	<li>The weight of <code>&quot;xyz&quot;</code> is <code>7 + 7 + 2 = 16</code>. The result modulo 26 is <code>16 % 26 = 16</code>, which maps to <code>&#39;j&#39;</code>.</li>
</ul>

<p>Thus, the string formed by concatenating the mapped characters is <code>&quot;rij&quot;</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">words = [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;], weights = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;yyy&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>Each word has weight 1. The result modulo 26 is <code>1 % 26 = 1</code>, which maps to <code>&#39;y&#39;</code>.</p>

<p>Thus, the string formed by concatenating the mapped characters is <code>&quot;yyy&quot;</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">words = [&quot;abcd&quot;], weights = [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;g&quot;</span></p>

<p><strong>Explanation:​​​​​​​</strong></p>

<p>The weight of <code>&quot;abcd&quot;</code> is <code>7 + 5 + 3 + 4 = 19</code>. The result modulo 26 is <code>19 % 26 = 19</code>, which maps to <code>&#39;g&#39;</code>.</p>

<p>Thus, the string formed by concatenating the mapped characters is <code>&quot;g&quot;</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 10</code></li>
	<li><code>weights.length == 26</code></li>
	<li><code>1 &lt;= weights[i] &lt;= 100</code></li>
	<li><code>words[i]</code> consists of lowercase English letters.</li>
</ul>


## Hints

1. For each word, sum character weights using `weights[c - 'a']`

2. Take the sum modulo `26`

3. Map the value to a character using reverse order: `char = 'z' - value`

4. Append all mapped characters in order to form the result string

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The core of the algorithm involves calculating a numerical weight for each word in the input array. For every word, we iterate through its characters, converting each lowercase English letter to its zero-based alphabetical index (where 'a' is 0, 'b' is 1, and so on) and then retrieving the corresponding value from the provided weights array. These values are summed to find the total weight of the word, which is then reduced modulo 26.

To perform the mapping to a character in reverse alphabetical order, we subtract the result of the modulo operation from the character 'z'. In this mapping scheme, a result of 0 yields 'z', 1 yields 'y', and 25 yields 'a'. Each resulting character is collected and finally concatenated into a single string to form the final result.

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
    string mapWordWeights(vector<string>& words, vector<int>& weights) {
        string result = "";
        for (const string& word : words) {
            int weightSum = 0;
            for (char c : word) {
                weightSum += weights[c - 'a'];
            }
            int rem = weightSum % 26;
            char mappedChar = (char)('z' - rem);
            result += mappedChar;
        }
        return result;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public String mapWordWeights(String[] words, int[] weights) {
        StringBuilder sb = new StringBuilder();
        for (String word : words) {
            int weightSum = 0;
            for (int i = 0; i < word.length(); i++) {
                weightSum += weights[word.charAt(i) - 'a'];
            }
            int rem = weightSum % 26;
            sb.append((char) ('z' - rem));
        }
        return sb.toString();
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        result = []
        for word in words:
            weight_sum = 0
            for char in word:
                weight_sum += weights[ord(char) - ord('a')]
            rem = weight_sum % 26
            result.append(chr(ord('z') - rem))
        return "".join(result)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []
        for word in words:
            weight_sum = sum(weights[ord(c) - ord('a')] for c in word)
            rem = weight_sum % 26
            result.append(chr(ord('z') - rem))
        return "".join(result)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

char* mapWordWeights(char** words, int wordsSize, int* weights, int weightsSize) {
    char* result = (char*)malloc((wordsSize + 1) * sizeof(char));
    if (!result) return NULL;
    for (int i = 0; i < wordsSize; i++) {
        int weightSum = 0;
        char* currentWord = words[i];
        while (*currentWord) {
            weightSum += weights[*currentWord - 'a'];
            currentWord++;
        }
        int rem = weightSum % 26;
        result[i] = (char)('z' - rem);
    }
    result[wordsSize] = '\0';
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public string MapWordWeights(string[] words, int[] weights) {
        char[] result = new char[words.Length];
        for (int i = 0; i < words.Length; i++) {
            int weightSum = 0;
            foreach (char c in words[i]) {
                weightSum += weights[c - 'a'];
            }
            int rem = weightSum % 26;
            result[i] = (char)('z' - rem);
        }
        return new string(result);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string[]} words
 * @param {number[]} weights
 * @return {string}
 */
var mapWordWeights = function(words, weights) {
    let result = "";
    for (let word of words) {
        let weightSum = 0;
        for (let i = 0; i < word.length; i++) {
            weightSum += weights[word.charCodeAt(i) - 97];
        }
        let rem = weightSum % 26;
        result += String.fromCharCode(122 - rem);
    }
    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function mapWordWeights(words: string[], weights: number[]): string {
    let result = "";
    for (const word of words) {
        let sum = 0;
        for (let i = 0; i < word.length; i++) {
            sum += weights[word.charCodeAt(i) - 97];
        }
        const index = sum % 26;
        result += String.fromCharCode(122 - index);
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
     * @param String[] $words
     * @param Integer[] $weights
     * @return String
     */
    function mapWordWeights($words, $weights) {
        $result = "";
        foreach ($words as $word) {
            $sum = 0;
            $len = strlen($word);
            for ($i = 0; $i < $len; $i++) {
                $sum += $weights[ord($word[$i]) - 97];
            }
            $result .= chr(122 - ($sum % 26));
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
    func mapWordWeights(_ words: [String], _ weights: [Int]) -> String {
        var result = ""
        for word in words {
            var sum = 0
            for scalar in word.utf8 {
                sum += weights[Int(scalar) - 97]
            }
            let index = sum % 26
            if let unicodeScalar = UnicodeScalar(122 - index) {
                result.append(Character(unicodeScalar))
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
    fun mapWordWeights(words: Array<String>, weights: IntArray): String {
        val result = StringBuilder()
        for (word in words) {
            var sum = 0
            for (char in word) {
                sum += weights[char - 'a']
            }
            val index = sum % 26
            result.append(('z'.toInt() - index).toChar())
        }
        return result.toString()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  String mapWordWeights(List<String> words, List<int> weights) {
    String result = "";
    for (var word in words) {
      int sum = 0;
      for (int i = 0; i < word.length; i++) {
        sum += weights[word.codeUnitAt(i) - 97];
      }
      int index = sum % 26;
      result += String.fromCharCode(122 - index);
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
func mapWordWeights(words []string, weights []int) string {
    res := make([]byte, len(words))
    for i, word := range words {
        sum := 0
        for j := 0; j < len(word); j++ {
            sum += weights[int(word[j]-'a')]
        }
        res[i] = 'z' - byte(sum%26)
    }
    return string(res)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String[]} words
# @param {Integer[]} weights
# @return {String}
def map_word_weights(words, weights)
  words.map do |word|
    sum = word.bytes.reduce(0) { |acc, b| acc + weights[b - 97] }
    (122 - (sum % 26)).chr
  end.join
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def mapWordWeights(words: Array[String], weights: Array[Int]): String = {
        words.map { word =>
            val weightSum = word.map(c => weights(c - 'a')).sum
            ('z'.toInt - (weightSum % 26)).toChar
        }.mkString
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn map_word_weights(words: Vec<String>, weights: Vec<i32>) -> String {
        words.iter().map(|word| {
            let weight_sum: i32 = word.chars().map(|c| weights[(c as usize) - ('a' as usize)]).sum();
            let rem = weight_sum % 26;
            ((b'z' - (rem as u8)) as char)
        }).collect()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (map-word-weights words weights)
  (-> (listof string?) (listof exact-integer?) string?)
  (apply string
         (map (lambda (word)
                (let* ([chars (string->list word)]
                       [char-weights (map (lambda (c)
                                            (list-ref weights (- (char->integer c) (char->integer #\a))))
                                          chars)]
                       [total-weight (apply + char-weights)]
                       [rem (modulo total-weight 26)])
                  (integer->char (- (char->integer #\z) rem))))
              words)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec map_word_weights(Words :: [unicode:unicode_binary()], Weights :: [integer()]) -> unicode:unicode_binary().
map_word_weights(Words, Weights) ->
  WeightsTuple = list_to_tuple(Weights),
  Mapped = [begin
              WordList = unicode:characters_to_list(Word),
              Sum = lists:foldl(fun(C, Acc) -> Acc + element(C - $a + 1, WeightsTuple) end, 0, WordList),
              $z - (Sum rem 26)
            end || Word <- Words],
  unicode:characters_to_binary(Mapped).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec map_word_weights(words :: [String.t], weights :: [integer]) :: String.t
  def map_word_weights(words, weights) do
    weights_tuple = List.to_tuple(weights)
    words
    |> Enum.map(fn word ->
      sum = word
      |> String.to_charlist()
      |> Enum.reduce(0, fn c, acc -> acc + elem(weights_tuple, c - ?a) end)
      rem_val = rem(sum, 26)
      <<?z - rem_val>>
    end)
    |> Enum.join("")
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N ⋅ L), where N is the number of words and L is the average length of each word. We process every character of every word exactly once to compute the weights. The constant time lookup for weights and the character mapping operations do not depend on the input size beyond the 26-element weights array.
- **Space Complexity:** O(N), where N is the number of words. We store the resulting string which contains one character for every input word. Additional auxiliary space used for calculations is constant, O(1).
