---
layout: post
title: "Words Within Two Edits of Dictionary"
date: 2026-04-22 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "String", "Trie"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/words-within-two-edits-of-dictionary/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<string> twoEditWords(vector<string>&\
        \ queries, vector<string>& dictionary) {\n        vector<string> result;\n \
        \       for (const string& q : queries) {\n            for (const string& d\
        \ : dictionary) {\n                int diff = 0;\n                int n = q.length();\n\
        \                for (int i = 0; i < n; ++i) {\n                    if (q[i]\
        \ != d[i]) {\n                        diff++;\n                        if (diff\
        \ > 2) break;\n                    }\n                }\n                if\
        \ (diff <= 2) {\n                    result.push_back(q);\n                \
        \    break;\n                }\n            }\n        }\n        return result;\n\
        \    }\n};"
      java: "import java.util.ArrayList;\nimport java.util.List;\n\nclass Solution {\n\
        \    public List<String> twoEditWords(String[] queries, String[] dictionary)\
        \ {\n        List<String> result = new ArrayList<>();\n        for (String q\
        \ : queries) {\n            for (String d : dictionary) {\n                int\
        \ diff = 0;\n                int n = q.length();\n                for (int i\
        \ = 0; i < n; i++) {\n                    if (q.charAt(i) != d.charAt(i)) {\n\
        \                        diff++;\n                        if (diff > 2) break;\n\
        \                    }\n                }\n                if (diff <= 2) {\n\
        \                    result.add(q);\n                    break;\n          \
        \      }\n            }\n        }\n        return result;\n    }\n}"
      python: "class Solution(object):\n    def twoEditWords(self, queries, dictionary):\n\
        \        \"\"\"\n        :type queries: List[str]\n        :type dictionary:\
        \ List[str]\n        :rtype: List[str]\n        \"\"\"\n        result = []\n\
        \        for q in queries:\n            for d in dictionary:\n             \
        \   diff = 0\n                for i in range(len(q)):\n                    if\
        \ q[i] != d[i]:\n                        diff += 1\n                       \
        \ if diff > 2:\n                            break\n                if diff <=\
        \ 2:\n                    result.append(q)\n                    break\n    \
        \    return result"
      python3: "from typing import List\n\nclass Solution:\n    def twoEditWords(self,\
        \ queries: List[str], dictionary: List[str]) -> List[str]:\n        result =\
        \ []\n        for q in queries:\n            for d in dictionary:\n        \
        \        diff = 0\n                for char_q, char_d in zip(q, d):\n      \
        \              if char_q != char_d:\n                        diff += 1\n   \
        \                     if diff > 2:\n                            break\n    \
        \            if diff <= 2:\n                    result.append(q)\n         \
        \           break\n        return result"
      c: "#include <stdlib.h>\n#include <string.h>\n\n/**\n * Note: The returned array\
        \ must be malloced, assume caller calls free().\n */\nchar** twoEditWords(char**\
        \ queries, int queriesSize, char** dictionary, int dictionarySize, int* returnSize)\
        \ {\n    char** result = (char**)malloc(queriesSize * sizeof(char*));\n    int\
        \ count = 0;\n    int n = (int)strlen(queries[0]);\n    for (int i = 0; i <\
        \ queriesSize; i++) {\n        for (int j = 0; j < dictionarySize; j++) {\n\
        \            int diff = 0;\n            for (int k = 0; k < n; k++) {\n    \
        \            if (queries[i][k] != dictionary[j][k]) {\n                    diff++;\n\
        \                    if (diff > 2) break;\n                }\n            }\n\
        \            if (diff <= 2) {\n                result[count] = (char*)malloc((n\
        \ + 1) * sizeof(char));\n                strcpy(result[count], queries[i]);\n\
        \                count++;\n                break;\n            }\n        }\n\
        \    }\n    *returnSize = count;\n    return result;\n}"
      csharp: "public class Solution {\n    public IList<string> TwoEditWords(string[]\
        \ queries, string[] dictionary) {\n        IList<string> result = new List<string>();\n\
        \        foreach (string q in queries) {\n            foreach (string d in dictionary)\
        \ {\n                int diffCount = 0;\n                for (int i = 0; i <\
        \ q.Length; i++) {\n                    if (q[i] != d[i]) {\n              \
        \          diffCount++;\n                    }\n                    if (diffCount\
        \ > 2) break;\n                }\n                if (diffCount <= 2) {\n  \
        \                  result.Add(q);\n                    break;\n            \
        \    }\n            }\n        }\n        return result;\n    }\n}"
      javascript: "/**\n * @param {string[]} queries\n * @param {string[]} dictionary\n\
        \ * @return {string[]}\n */\nvar twoEditWords = function(queries, dictionary)\
        \ {\n    const result = [];\n    for (const q of queries) {\n        let foundMatch\
        \ = false;\n        for (const d of dictionary) {\n            let diffCount\
        \ = 0;\n            for (let i = 0; i < q.length; i++) {\n                if\
        \ (q[i] !== d[i]) {\n                    diffCount++;\n                }\n \
        \               if (diffCount > 2) break;\n            }\n            if (diffCount\
        \ <= 2) {\n                foundMatch = true;\n                break;\n    \
        \        }\n        }\n        if (foundMatch) {\n            result.push(q);\n\
        \        }\n    }\n    return result;\n};"
      typescript: "function twoEditWords(queries: string[], dictionary: string[]): string[]\
        \ {\n    const result: string[] = [];\n    for (const q of queries) {\n    \
        \    let foundMatch = false;\n        for (const d of dictionary) {\n      \
        \      let diffCount = 0;\n            for (let i = 0; i < q.length; i++) {\n\
        \                if (q[i] !== d[i]) {\n                    diffCount++;\n  \
        \              }\n                if (diffCount > 2) break;\n            }\n\
        \            if (diffCount <= 2) {\n                foundMatch = true;\n   \
        \             break;\n            }\n        }\n        if (foundMatch) {\n\
        \            result.push(q);\n        }\n    }\n    return result;\n}"
      php: "class Solution {\n\n    /**\n     * @param String[] $queries\n     * @param\
        \ String[] $dictionary\n     * @return String[]\n     */\n    function twoEditWords($queries,\
        \ $dictionary) {\n        $result = [];\n        foreach ($queries as $q) {\n\
        \            $matchFound = false;\n            foreach ($dictionary as $d) {\n\
        \                $diffCount = 0;\n                $len = strlen($q);\n     \
        \           for ($i = 0; $i < $len; $i++) {\n                    if ($q[$i]\
        \ !== $d[$i]) {\n                        $diffCount++;\n                   \
        \ }\n                    if ($diffCount > 2) break;\n                }\n   \
        \             if ($diffCount <= 2) {\n                    $matchFound = true;\n\
        \                    break;\n                }\n            }\n            if\
        \ ($matchFound) {\n                $result[] = $q;\n            }\n        }\n\
        \        return $result;\n    }\n}"
      swift: "class Solution {\n    func twoEditWords(_ queries: [String], _ dictionary:\
        \ [String]) -> [String] {\n        var result = [String]()\n        let dictArrays\
        \ = dictionary.map { Array($0) }\n\n        for q in queries {\n           \
        \ let qArray = Array(q)\n            var foundMatch = false\n            for\
        \ dArray in dictArrays {\n                var diffCount = 0\n              \
        \  for i in 0..<qArray.count {\n                    if qArray[i] != dArray[i]\
        \ {\n                        diffCount += 1\n                    }\n       \
        \             if diffCount > 2 {\n                        break\n          \
        \          }\n                }\n                if diffCount <= 2 {\n     \
        \               foundMatch = true\n                    break\n             \
        \   }\n            }\n            if foundMatch {\n                result.append(q)\n\
        \            }\n        }\n\n        return result\n    }\n}"
      kotlin: "class Solution {\n    fun twoEditWords(queries: Array<String>, dictionary:\
        \ Array<String>): List<String> {\n        val result = mutableListOf<String>()\n\
        \        for (query in queries) {\n            for (word in dictionary) {\n\
        \                var edits = 0\n                for (i in query.indices) {\n\
        \                    if (query[i] != word[i]) {\n                        edits++\n\
        \                    }\n                    if (edits > 2) break\n         \
        \       }\n                if (edits <= 2) {\n                    result.add(query)\n\
        \                    break\n                }\n            }\n        }\n  \
        \      return result\n    }\n}"
      dart: "class Solution {\n  List<String> twoEditWords(List<String> queries, List<String>\
        \ dictionary) {\n    List<String> result = [];\n    for (var query in queries)\
        \ {\n      for (var word in dictionary) {\n        int edits = 0;\n        for\
        \ (int i = 0; i < query.length; i++) {\n          if (query[i] != word[i]) {\n\
        \            edits++;\n          }\n          if (edits > 2) break;\n      \
        \  }\n        if (edits <= 2) {\n          result.add(query);\n          break;\n\
        \        }\n      }\n    }\n    return result;\n  }\n}"
      go: "func twoEditWords(queries []string, dictionary []string) []string {\n   \
        \ var result []string\n    for _, query := range queries {\n        found :=\
        \ false\n        for _, word := range dictionary {\n            edits := 0\n\
        \            for i := 0; i < len(query); i++ {\n                if query[i]\
        \ != word[i] {\n                    edits++\n                }\n           \
        \     if edits > 2 {\n                    break\n                }\n       \
        \     }\n            if edits <= 2 {\n                found = true\n       \
        \         break\n            }\n        }\n        if found {\n            result\
        \ = append(result, query)\n        }\n    }\n    return result\n}"
      ruby: "# @param {String[]} queries\n# @param {String[]} dictionary\n# @return\
        \ {String[]}\ndef two_edit_words(queries, dictionary)\n  queries.select do |query|\n\
        \    dictionary.any? do |word|\n      edits = 0\n      query.length.times do\
        \ |i|\n        edits += 1 if query[i] != word[i]\n        break if edits > 2\n\
        \      end\n      edits <= 2\n    end\n  end\nend"
      scala: "object Solution {\n    def twoEditWords(queries: Array[String], dictionary:\
        \ Array[String]): List[String] = {\n        queries.filter { query =>\n    \
        \        dictionary.exists { word =>\n                var edits = 0\n      \
        \          var i = 0\n                while (i < query.length && edits <= 2)\
        \ {\n                    if (query(i) != word(i)) {\n                      \
        \  edits += 1\n                    }\n                    i += 1\n         \
        \       }\n                edits <= 2\n            }\n        }.toList\n   \
        \ }\n}"
      rust: "impl Solution {\n    pub fn two_edit_words(queries: Vec<String>, dictionary:\
        \ Vec<String>) -> Vec<String> {\n        queries\n            .into_iter()\n\
        \            .filter(|q| {\n                let q_bytes = q.as_bytes();\n  \
        \              dictionary.iter().any(|d| {\n                    let d_bytes\
        \ = d.as_bytes();\n                    let mut diffs = 0;\n                \
        \    for i in 0..q_bytes.len() {\n                        if q_bytes[i] != d_bytes[i]\
        \ {\n                            diffs += 1;\n                            if\
        \ diffs > 2 {\n                                return false;\n             \
        \               }\n                        }\n                    }\n      \
        \              true\n                })\n            })\n            .collect()\n\
        \    }\n}"
      racket: "(define/contract (two-edit-words queries dictionary)\n  (-> (listof string?)\
        \ (listof string?) (listof string?))\n  (define (match? q d)\n    (let ([len\
        \ (string-length q)])\n      (let loop ([i 0] [diffs 0])\n        (cond\n  \
        \        [(> diffs 2) #f]\n          [(= i len) #t]\n          [(char=? (string-ref\
        \ q i) (string-ref d i)) (loop (+ i 1) diffs)]\n          [else (loop (+ i 1)\
        \ (+ diffs 1))]))))\n  (filter (lambda (q)\n            (ormap (lambda (d) (match?\
        \ q d)) dictionary))\n          queries))"
      erlang: "-spec two_edit_words(Queries :: [unicode:unicode_binary()], Dictionary\
        \ :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].\ntwo_edit_words(Queries,\
        \ Dictionary) ->\n  Check = fun Rec(<<H, T1/binary>>, <<H, T2/binary>>, D) ->\n\
        \                Rec(T1, T2, D);\n            Rec(<<_, T1/binary>>, <<_, T2/binary>>,\
        \ D) when D < 2 ->\n                Rec(T1, T2, D + 1);\n            Rec(<<>>,\
        \ <<>>, _) ->\n                true;\n            Rec(_, _, _) ->\n        \
        \        false\n          end,\n  [Q || Q <- Queries, lists:any(fun(D) -> Check(Q,\
        \ D, 0) end, Dictionary)]."
      elixir: "defmodule Solution do\n  @spec two_edit_words(queries :: [String.t],\
        \ dictionary :: [String.t]) :: [String.t]\n  def two_edit_words(queries, dictionary)\
        \ do\n    Enum.filter(queries, fn query ->\n      Enum.any?(dictionary, fn word\
        \ ->\n        within_two_edits?(query, word, 0)\n      end)\n    end)\n  end\n\
        \n  defp within_two_edits?(<<h, t1::binary>>, <<h, t2::binary>>, diffs) do\n\
        \    within_two_edits?(t1, t2, diffs)\n  end\n\n  defp within_two_edits?(<<_,\
        \ t1::binary>>, <<_, t2::binary>>, diffs) when diffs < 2 do\n    within_two_edits?(t1,\
        \ t2, diffs + 1)\n  end\n\n  defp within_two_edits?(<<>>, <<>>, _diffs) do\n\
        \    true\n  end\n\n  defp within_two_edits?(_, _, _) do\n    false\n  end\n\
        end"
    approach: The problem asks us to find all strings in a queries array that are at
      most two edits away from any string in a dictionary. Since all strings have the
      same length $n$, an edit is simply a character substitution at a specific index.
      The most direct approach is a brute-force search where we iterate through each
      word in the queries list and compare it character-by-character with every word
      in the dictionary.
    time_complexity: O(Q * D * n), where Q is the number of query strings, D is the
      number of dictionary strings, and n is the length of each string. In the worst
      case, we compare every query word with every dictionary word, checking up to n
      characters for each pair.
    space_complexity: O(Q * n) to store the result list, assuming each query word could
      potentially be a match. If the output storage is not counted as auxiliary space,
      the space complexity is O(1) beyond simple loop variables and mismatch counters.
    elapsed_time: 131.29588150978088
    model: gemini-3-flash-preview
    generated_at: '2026-04-22 01:56:24 '
---

## Problem #2452: Words Within Two Edits of Dictionary

**Difficulty:** Medium

**Topics:** Array, String, Trie

## Problem Description

<p>You are given two string arrays, <code>queries</code> and <code>dictionary</code>. All words in each array comprise of lowercase English letters and have the same length.</p>

<p>In one <strong>edit</strong> you can take a word from <code>queries</code>, and change any letter in it to any other letter. Find all words from <code>queries</code> that, after a <strong>maximum</strong> of two edits, equal some word from <code>dictionary</code>.</p>

<p>Return<em> a list of all words from </em><code>queries</code><em>, </em><em>that match with some word from </em><code>dictionary</code><em> after a maximum of <strong>two edits</strong></em>. Return the words in the <strong>same order</strong> they appear in <code>queries</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> queries = [&quot;word&quot;,&quot;note&quot;,&quot;ants&quot;,&quot;wood&quot;], dictionary = [&quot;wood&quot;,&quot;joke&quot;,&quot;moat&quot;]
<strong>Output:</strong> [&quot;word&quot;,&quot;note&quot;,&quot;wood&quot;]
<strong>Explanation:</strong>
- Changing the &#39;r&#39; in &quot;word&quot; to &#39;o&#39; allows it to equal the dictionary word &quot;wood&quot;.
- Changing the &#39;n&#39; to &#39;j&#39; and the &#39;t&#39; to &#39;k&#39; in &quot;note&quot; changes it to &quot;joke&quot;.
- It would take more than 2 edits for &quot;ants&quot; to equal a dictionary word.
- &quot;wood&quot; can remain unchanged (0 edits) and match the corresponding dictionary word.
Thus, we return [&quot;word&quot;,&quot;note&quot;,&quot;wood&quot;].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> queries = [&quot;yes&quot;], dictionary = [&quot;not&quot;]
<strong>Output:</strong> []
<strong>Explanation:</strong>
Applying any two edits to &quot;yes&quot; cannot make it equal to &quot;not&quot;. Thus, we return an empty array.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= queries.length, dictionary.length &lt;= 100</code></li>
	<li><code>n == queries[i].length == dictionary[j].length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li>All <code>queries[i]</code> and <code>dictionary[j]</code> are composed of lowercase English letters.</li>
</ul>


## Hints

1. Try brute-forcing the problem.

2. For each word in queries, try comparing to each word in dictionary.

3. If there is a maximum of two edit differences, the word should be present in answer.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks us to find all strings in a queries array that are at most two edits away from any string in a dictionary. Since all strings have the same length $n$, an edit is simply a character substitution at a specific index. The most direct approach is a brute-force search where we iterate through each word in the queries list and compare it character-by-character with every word in the dictionary.

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
    vector<string> twoEditWords(vector<string>& queries, vector<string>& dictionary) {
        vector<string> result;
        for (const string& q : queries) {
            for (const string& d : dictionary) {
                int diff = 0;
                int n = q.length();
                for (int i = 0; i < n; ++i) {
                    if (q[i] != d[i]) {
                        diff++;
                        if (diff > 2) break;
                    }
                }
                if (diff <= 2) {
                    result.push_back(q);
                    break;
                }
            }
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
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> twoEditWords(String[] queries, String[] dictionary) {
        List<String> result = new ArrayList<>();
        for (String q : queries) {
            for (String d : dictionary) {
                int diff = 0;
                int n = q.length();
                for (int i = 0; i < n; i++) {
                    if (q.charAt(i) != d.charAt(i)) {
                        diff++;
                        if (diff > 2) break;
                    }
                }
                if (diff <= 2) {
                    result.add(q);
                    break;
                }
            }
        }
        return result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
        result = []
        for q in queries:
            for d in dictionary:
                diff = 0
                for i in range(len(q)):
                    if q[i] != d[i]:
                        diff += 1
                        if diff > 2:
                            break
                if diff <= 2:
                    result.append(q)
                    break
        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result = []
        for q in queries:
            for d in dictionary:
                diff = 0
                for char_q, char_d in zip(q, d):
                    if char_q != char_d:
                        diff += 1
                        if diff > 2:
                            break
                if diff <= 2:
                    result.append(q)
                    break
        return result
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
char** twoEditWords(char** queries, int queriesSize, char** dictionary, int dictionarySize, int* returnSize) {
    char** result = (char**)malloc(queriesSize * sizeof(char*));
    int count = 0;
    int n = (int)strlen(queries[0]);
    for (int i = 0; i < queriesSize; i++) {
        for (int j = 0; j < dictionarySize; j++) {
            int diff = 0;
            for (int k = 0; k < n; k++) {
                if (queries[i][k] != dictionary[j][k]) {
                    diff++;
                    if (diff > 2) break;
                }
            }
            if (diff <= 2) {
                result[count] = (char*)malloc((n + 1) * sizeof(char));
                strcpy(result[count], queries[i]);
                count++;
                break;
            }
        }
    }
    *returnSize = count;
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public IList<string> TwoEditWords(string[] queries, string[] dictionary) {
        IList<string> result = new List<string>();
        foreach (string q in queries) {
            foreach (string d in dictionary) {
                int diffCount = 0;
                for (int i = 0; i < q.Length; i++) {
                    if (q[i] != d[i]) {
                        diffCount++;
                    }
                    if (diffCount > 2) break;
                }
                if (diffCount <= 2) {
                    result.Add(q);
                    break;
                }
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
 * @param {string[]} queries
 * @param {string[]} dictionary
 * @return {string[]}
 */
var twoEditWords = function(queries, dictionary) {
    const result = [];
    for (const q of queries) {
        let foundMatch = false;
        for (const d of dictionary) {
            let diffCount = 0;
            for (let i = 0; i < q.length; i++) {
                if (q[i] !== d[i]) {
                    diffCount++;
                }
                if (diffCount > 2) break;
            }
            if (diffCount <= 2) {
                foundMatch = true;
                break;
            }
        }
        if (foundMatch) {
            result.push(q);
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
function twoEditWords(queries: string[], dictionary: string[]): string[] {
    const result: string[] = [];
    for (const q of queries) {
        let foundMatch = false;
        for (const d of dictionary) {
            let diffCount = 0;
            for (let i = 0; i < q.length; i++) {
                if (q[i] !== d[i]) {
                    diffCount++;
                }
                if (diffCount > 2) break;
            }
            if (diffCount <= 2) {
                foundMatch = true;
                break;
            }
        }
        if (foundMatch) {
            result.push(q);
        }
    }
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String[] $queries
     * @param String[] $dictionary
     * @return String[]
     */
    function twoEditWords($queries, $dictionary) {
        $result = [];
        foreach ($queries as $q) {
            $matchFound = false;
            foreach ($dictionary as $d) {
                $diffCount = 0;
                $len = strlen($q);
                for ($i = 0; $i < $len; $i++) {
                    if ($q[$i] !== $d[$i]) {
                        $diffCount++;
                    }
                    if ($diffCount > 2) break;
                }
                if ($diffCount <= 2) {
                    $matchFound = true;
                    break;
                }
            }
            if ($matchFound) {
                $result[] = $q;
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
    func twoEditWords(_ queries: [String], _ dictionary: [String]) -> [String] {
        var result = [String]()
        let dictArrays = dictionary.map { Array($0) }

        for q in queries {
            let qArray = Array(q)
            var foundMatch = false
            for dArray in dictArrays {
                var diffCount = 0
                for i in 0..<qArray.count {
                    if qArray[i] != dArray[i] {
                        diffCount += 1
                    }
                    if diffCount > 2 {
                        break
                    }
                }
                if diffCount <= 2 {
                    foundMatch = true
                    break
                }
            }
            if foundMatch {
                result.append(q)
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
    fun twoEditWords(queries: Array<String>, dictionary: Array<String>): List<String> {
        val result = mutableListOf<String>()
        for (query in queries) {
            for (word in dictionary) {
                var edits = 0
                for (i in query.indices) {
                    if (query[i] != word[i]) {
                        edits++
                    }
                    if (edits > 2) break
                }
                if (edits <= 2) {
                    result.add(query)
                    break
                }
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
  List<String> twoEditWords(List<String> queries, List<String> dictionary) {
    List<String> result = [];
    for (var query in queries) {
      for (var word in dictionary) {
        int edits = 0;
        for (int i = 0; i < query.length; i++) {
          if (query[i] != word[i]) {
            edits++;
          }
          if (edits > 2) break;
        }
        if (edits <= 2) {
          result.add(query);
          break;
        }
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
func twoEditWords(queries []string, dictionary []string) []string {
    var result []string
    for _, query := range queries {
        found := false
        for _, word := range dictionary {
            edits := 0
            for i := 0; i < len(query); i++ {
                if query[i] != word[i] {
                    edits++
                }
                if edits > 2 {
                    break
                }
            }
            if edits <= 2 {
                found = true
                break
            }
        }
        if found {
            result = append(result, query)
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
# @param {String[]} queries
# @param {String[]} dictionary
# @return {String[]}
def two_edit_words(queries, dictionary)
  queries.select do |query|
    dictionary.any? do |word|
      edits = 0
      query.length.times do |i|
        edits += 1 if query[i] != word[i]
        break if edits > 2
      end
      edits <= 2
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def twoEditWords(queries: Array[String], dictionary: Array[String]): List[String] = {
        queries.filter { query =>
            dictionary.exists { word =>
                var edits = 0
                var i = 0
                while (i < query.length && edits <= 2) {
                    if (query(i) != word(i)) {
                        edits += 1
                    }
                    i += 1
                }
                edits <= 2
            }
        }.toList
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn two_edit_words(queries: Vec<String>, dictionary: Vec<String>) -> Vec<String> {
        queries
            .into_iter()
            .filter(|q| {
                let q_bytes = q.as_bytes();
                dictionary.iter().any(|d| {
                    let d_bytes = d.as_bytes();
                    let mut diffs = 0;
                    for i in 0..q_bytes.len() {
                        if q_bytes[i] != d_bytes[i] {
                            diffs += 1;
                            if diffs > 2 {
                                return false;
                            }
                        }
                    }
                    true
                })
            })
            .collect()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (two-edit-words queries dictionary)
  (-> (listof string?) (listof string?) (listof string?))
  (define (match? q d)
    (let ([len (string-length q)])
      (let loop ([i 0] [diffs 0])
        (cond
          [(> diffs 2) #f]
          [(= i len) #t]
          [(char=? (string-ref q i) (string-ref d i)) (loop (+ i 1) diffs)]
          [else (loop (+ i 1) (+ diffs 1))]))))
  (filter (lambda (q)
            (ormap (lambda (d) (match? q d)) dictionary))
          queries))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec two_edit_words(Queries :: [unicode:unicode_binary()], Dictionary :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
two_edit_words(Queries, Dictionary) ->
  Check = fun Rec(<<H, T1/binary>>, <<H, T2/binary>>, D) ->
                Rec(T1, T2, D);
            Rec(<<_, T1/binary>>, <<_, T2/binary>>, D) when D < 2 ->
                Rec(T1, T2, D + 1);
            Rec(<<>>, <<>>, _) ->
                true;
            Rec(_, _, _) ->
                false
          end,
  [Q || Q <- Queries, lists:any(fun(D) -> Check(Q, D, 0) end, Dictionary)].
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec two_edit_words(queries :: [String.t], dictionary :: [String.t]) :: [String.t]
  def two_edit_words(queries, dictionary) do
    Enum.filter(queries, fn query ->
      Enum.any?(dictionary, fn word ->
        within_two_edits?(query, word, 0)
      end)
    end)
  end

  defp within_two_edits?(<<h, t1::binary>>, <<h, t2::binary>>, diffs) do
    within_two_edits?(t1, t2, diffs)
  end

  defp within_two_edits?(<<_, t1::binary>>, <<_, t2::binary>>, diffs) when diffs < 2 do
    within_two_edits?(t1, t2, diffs + 1)
  end

  defp within_two_edits?(<<>>, <<>>, _diffs) do
    true
  end

  defp within_two_edits?(_, _, _) do
    false
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(Q * D * n), where Q is the number of query strings, D is the number of dictionary strings, and n is the length of each string. In the worst case, we compare every query word with every dictionary word, checking up to n characters for each pair.
- **Space Complexity:** O(Q * n) to store the result list, assuming each query word could potentially be a match. If the output storage is not counted as auxiliary space, the space complexity is O(1) beyond simple loop variables and mismatch counters.
