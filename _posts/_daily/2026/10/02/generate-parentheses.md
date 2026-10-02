---
layout: post
title: "Generate Parentheses"
date: 2026-10-02 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Dynamic Programming", "Backtracking", "Bracket Sequences"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/generate-parentheses/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <string>\n\nusing namespace std;\n\nclass Solution\
        \ {\npublic:\n    vector<string> generateParenthesis(int n) {\n        vector<string>\
        \ result;\n        string current = \"\";\n        backtrack(result, current,\
        \ 0, 0, n);\n        return result;\n    }\n\nprivate:\n    void backtrack(vector<string>&\
        \ result, string& current, int open, int close, int n) {\n        if (current.length()\
        \ == 2 * n) {\n            result.push_back(current);\n            return;\n\
        \        }\n        if (open < n) {\n            current.push_back('(');\n \
        \           backtrack(result, current, open + 1, close, n);\n            current.pop_back();\n\
        \        }\n        if (close < open) {\n            current.push_back(')');\n\
        \            backtrack(result, current, open, close + 1, n);\n            current.pop_back();\n\
        \        }\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public List<String> generateParenthesis(int\
        \ n) {\n        List<String> result = new ArrayList<>();\n        backtrack(result,\
        \ new StringBuilder(), 0, 0, n);\n        return result;\n    }\n\n    private\
        \ void backtrack(List<String> result, StringBuilder current, int open, int close,\
        \ int n) {\n        if (current.length() == 2 * n) {\n            result.add(current.toString());\n\
        \            return;\n        }\n        if (open < n) {\n            current.append('(');\n\
        \            backtrack(result, current, open + 1, close, n);\n            current.deleteCharAt(current.length()\
        \ - 1);\n        }\n        if (close < open) {\n            current.append(')');\n\
        \            backtrack(result, current, open, close + 1, n);\n            current.deleteCharAt(current.length()\
        \ - 1);\n        }\n    }\n}"
      python: "class Solution(object):\n    def generateParenthesis(self, n):\n    \
        \    \"\"\"\n        :type n: int\n        :rtype: List[str]\n        \"\"\"\
        \n        result = []\n        def backtrack(current, open_count, close_count):\n\
        \            if len(current) == 2 * n:\n                result.append(current)\n\
        \                return\n            if open_count < n:\n                backtrack(current\
        \ + \"(\", open_count + 1, close_count)\n            if close_count < open_count:\n\
        \                backtrack(current + \")\", open_count, close_count + 1)\n\n\
        \        backtrack(\"\", 0, 0)\n        return result"
      python3: "class Solution:\n    def generateParenthesis(self, n: int) -> list[str]:\n\
        \        result = []\n        def backtrack(current, open_count, close_count):\n\
        \            if len(current) == 2 * n:\n                result.append(current)\n\
        \                return\n            if open_count < n:\n                backtrack(current\
        \ + \"(\", open_count + 1, close_count)\n            if close_count < open_count:\n\
        \                backtrack(current + \")\", open_count, close_count + 1)\n\n\
        \        backtrack(\"\", 0, 0)\n        return result"
      c: "#include <stdlib.h>\n#include <string.h>\n\nvoid backtrack(int n, int open,\
        \ int close, char* current, int index, char** result, int* returnSize) {\n \
        \   if (index == 2 * n) {\n        current[index] = '\\0';\n        result[*returnSize]\
        \ = (char*)malloc((2 * n + 1) * sizeof(char));\n        strcpy(result[*returnSize],\
        \ current);\n        (*returnSize)++;\n        return;\n    }\n    if (open\
        \ < n) {\n        current[index] = '(';\n        backtrack(n, open + 1, close,\
        \ current, index + 1, result, returnSize);\n    }\n    if (close < open) {\n\
        \        current[index] = ')';\n        backtrack(n, open, close + 1, current,\
        \ index + 1, result, returnSize);\n    }\n}\n\n/**\n * Note: The returned array\
        \ must be malloced, assume caller calls free().\n */\nchar** generateParenthesis(int\
        \ n, int* returnSize) {\n    *returnSize = 0;\n    char** result = (char**)malloc(2000\
        \ * sizeof(char*));\n    char* current = (char*)malloc((2 * n + 1) * sizeof(char));\n\
        \    backtrack(n, 0, 0, current, 0, result, returnSize);\n    free(current);\n\
        \    return result;\n}"
      csharp: "public class Solution {\n    public IList<string> GenerateParenthesis(int\
        \ n) {\n        List<string> result = new List<string>();\n        Backtrack(result,\
        \ \"\", 0, 0, n);\n        return result;\n    }\n\n    private void Backtrack(List<string>\
        \ result, string current, int open, int close, int max) {\n        if (current.Length\
        \ == max * 2) {\n            result.Add(current);\n            return;\n   \
        \     }\n\n        if (open < max) {\n            Backtrack(result, current\
        \ + \"(\", open + 1, close, max);\n        }\n        if (close < open) {\n\
        \            Backtrack(result, current + \")\", open, close + 1, max);\n   \
        \     }\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @return {string[]}\n */\nvar generateParenthesis\
        \ = function(n) {\n    const result = [];\n\n    const backtrack = (current,\
        \ open, close) => {\n        if (current.length === n * 2) {\n            result.push(current);\n\
        \            return;\n        }\n\n        if (open < n) {\n            backtrack(current\
        \ + \"(\", open + 1, close);\n        }\n        if (close < open) {\n     \
        \       backtrack(current + \")\", open, close + 1);\n        }\n    };\n\n\
        \    backtrack(\"\", 0, 0);\n    return result;\n};"
      typescript: "function generateParenthesis(n: number): string[] {\n    const result:\
        \ string[] = [];\n\n    const backtrack = (current: string, open: number, close:\
        \ number): void => {\n        if (current.length === n * 2) {\n            result.push(current);\n\
        \            return;\n        }\n\n        if (open < n) {\n            backtrack(current\
        \ + \"(\", open + 1, close);\n        }\n        if (close < open) {\n     \
        \       backtrack(current + \")\", open, close + 1);\n        }\n    };\n\n\
        \    backtrack(\"\", 0, 0);\n    return result;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @return String[]\n\
        \     */\n    function generateParenthesis($n) {\n        $result = [];\n  \
        \      $this->backtrack($result, \"\", 0, 0, $n);\n        return $result;\n\
        \    }\n\n    private function backtrack(&$result, $current, $open, $close,\
        \ $n) {\n        if (strlen($current) === 2 * $n) {\n            $result[] =\
        \ $current;\n            return;\n        }\n\n        if ($open < $n) {\n \
        \           $this->backtrack($result, $current . \"(\", $open + 1, $close, $n);\n\
        \        }\n        if ($close < $open) {\n            $this->backtrack($result,\
        \ $current . \")\", $open, $close + 1, $n);\n        }\n    }\n}"
      swift: "class Solution {\n    func generateParenthesis(_ n: Int) -> [String] {\n\
        \        var result = [String]()\n        backtrack(&result, \"\", 0, 0, n)\n\
        \        return result\n    }\n\n    private func backtrack(_ result: inout\
        \ [String], _ current: String, _ open: Int, _ close: Int, _ n: Int) {\n    \
        \    if current.count == n * 2 {\n            result.append(current)\n     \
        \       return\n        }\n\n        if open < n {\n            backtrack(&result,\
        \ current + \"(\", open + 1, close, n)\n        }\n        if close < open {\n\
        \            backtrack(&result, current + \")\", open, close + 1, n)\n     \
        \   }\n    }\n}"
      kotlin: "class Solution {\n    fun generateParenthesis(n: Int): List<String> {\n\
        \        val result = mutableListOf<String>()\n        backtrack(result, StringBuilder(),\
        \ 0, 0, n)\n        return result\n    }\n\n    private fun backtrack(result:\
        \ MutableList<String>, current: StringBuilder, open: Int, close: Int, max: Int)\
        \ {\n        if (current.length == max * 2) {\n            result.add(current.toString())\n\
        \            return\n        }\n        if (open < max) {\n            current.append('(')\n\
        \            backtrack(result, current, open + 1, close, max)\n            current.deleteCharAt(current.length\
        \ - 1)\n        }\n        if (close < open) {\n            current.append(')')\n\
        \            backtrack(result, current, open, close + 1, max)\n            current.deleteCharAt(current.length\
        \ - 1)\n        }\n    }\n}"
      dart: "class Solution {\n  List<String> generateParenthesis(int n) {\n    List<String>\
        \ result = [];\n    _backtrack(result, \"\", 0, 0, n);\n    return result;\n\
        \  }\n\n  void _backtrack(List<String> result, String current, int open, int\
        \ close, int max) {\n    if (current.length == max * 2) {\n      result.add(current);\n\
        \      return;\n    }\n    if (open < max) {\n      _backtrack(result, current\
        \ + \"(\", open + 1, close, max);\n    }\n    if (close < open) {\n      _backtrack(result,\
        \ current + \")\", open, close + 1, max);\n    }\n  }\n}"
      go: "func generateParenthesis(n int) []string {\n    result := []string{}\n  \
        \  var backtrack func(current string, open int, close int)\n    backtrack =\
        \ func(current string, open int, close int) {\n        if len(current) == 2*n\
        \ {\n            result = append(result, current)\n            return\n    \
        \    }\n        if open < n {\n            backtrack(current+\"(\", open+1,\
        \ close)\n        }\n        if close < open {\n            backtrack(current+\"\
        )\", open, close+1)\n        }\n    }\n    backtrack(\"\", 0, 0)\n    return\
        \ result\n}"
      ruby: "def generate_parenthesis(n)\n    result = []\n    backtrack(result, \"\"\
        , 0, 0, n)\n    result\nend\n\ndef backtrack(result, current, open_count, close_count,\
        \ max)\n    if current.length == max * 2\n        result << current\n      \
        \  return\n    end\n    if open_count < max\n        backtrack(result, current\
        \ + \"(\", open_count + 1, close_count, max)\n    end\n    if close_count <\
        \ open_count\n        backtrack(result, current + \")\", open_count, close_count\
        \ + 1, max)\n    end\nend"
      scala: "object Solution {\n    def generateParenthesis(n: Int): List[String] =\
        \ {\n        val result = scala.collection.mutable.ListBuffer[String]()\n  \
        \      def backtrack(current: String, open: Int, close: Int): Unit = {\n   \
        \         if (current.length == 2 * n) {\n                result += current\n\
        \                return\n            }\n            if (open < n) {\n      \
        \          backtrack(current + \"(\", open + 1, close)\n            }\n    \
        \        if (close < open) {\n                backtrack(current + \")\", open,\
        \ close + 1)\n            }\n        }\n        backtrack(\"\", 0, 0)\n    \
        \    result.toList\n    }\n}"
      rust: "impl Solution {\n    pub fn generate_parenthesis(n: i32) -> Vec<String>\
        \ {\n        let mut result = Vec::new();\n        let mut current = String::new();\n\
        \        Self::backtrack(&mut result, &mut current, 0, 0, n);\n        result\n\
        \    }\n\n    fn backtrack(result: &mut Vec<String>, current: &mut String, open:\
        \ i32, close: i32, max: i32) {\n        if current.len() == (max * 2) as usize\
        \ {\n            result.push(current.clone());\n            return;\n      \
        \  }\n\n        if open < max {\n            current.push('(');\n          \
        \  Self::backtrack(result, current, open + 1, close, max);\n            current.pop();\n\
        \        }\n\n        if close < open {\n            current.push(')');\n  \
        \          Self::backtrack(result, current, open, close + 1, max);\n       \
        \     current.pop();\n        }\n    }\n}"
      racket: "(define/contract (generate-parenthesis n)\n  (-> exact-integer? (listof\
        \ string?))\n  (define (backtrack open close current)\n    (if (= (string-length\
        \ current) (* 2 n))\n        (list current)\n        (let ()\n          (define\
        \ left (if (< open n)\n                           (backtrack (+ open 1) close\
        \ (string-append current \"(\"))\n                           '()))\n       \
        \   (define right (if (< close open)\n                            (backtrack\
        \ open (+ close 1) (string-append current \")\"))\n                        \
        \    '()))\n          (append left right))))\n  (backtrack 0 0 \"\"))"
      erlang: "-spec generate_parenthesis(N :: integer()) -> [unicode:unicode_binary()].\n\
        generate_parenthesis(N) ->\n  backtrack(0, 0, N, <<>>).\n\nbacktrack(Open, Close,\
        \ N, Acc) when byte_size(Acc) =:= 2 * N ->\n  [Acc];\nbacktrack(Open, Close,\
        \ N, Acc) ->\n  Res1 = if\n    Open < N -> backtrack(Open + 1, Close, N, <<Acc/binary,\
        \ \"(\">>);\n    true -> []\n  end,\n  Res2 = if\n    Close < Open -> backtrack(Open,\
        \ Close + 1, N, <<Acc/binary, \")\">>);\n    true -> []\n  end,\n  Res1 ++ Res2."
      elixir: "defmodule Solution do\n  @spec generate_parenthesis(n :: integer) ::\
        \ [String.t]\n  def generate_parenthesis(n) do\n    backtrack(0, 0, n, \"\"\
        )\n  end\n\n  defp backtrack(open, close, n, acc) when byte_size(acc) == 2 *\
        \ n do\n    [acc]\n  end\n\n  defp backtrack(open, close, n, acc) do\n    res1\
        \ = if open < n do\n      backtrack(open + 1, close, n, acc <> \"(\")\n    else\n\
        \      []\n    end\n\n    res2 = if close < open do\n      backtrack(open, close\
        \ + 1, n, acc <> \")\")\n    else\n      []\n    end\n\n    res1 ++ res2\n \
        \ end\nend"
    approach: 'The problem is solved using a recursive backtracking approach to explore
      all valid combinations of parentheses. We incrementally build a string of length
      $2n$ by making choices at each step: we can either add an opening parenthesis
      ''('' or a closing parenthesis '')''. To ensure the combinations are well-formed,
      we maintain the counts of open and closed parentheses used so far, following two
      core constraints: the total number of open parentheses cannot exceed $n$, and
      a closing parenthesis can only be added if its count is strictly less than the
      count of open parentheses currently in the string.


      This strategy prunes invalid branches of the recursion tree early, as it never
      attempts to place a closing parenthesis that doesn''t have a matching opening
      one preceding it. When the length of the current string reaches $2n$, we know
      a complete and valid combination has been formed, so we add it to our result list.
      This process effectively explores the state space of all valid bracket sequences,
      ensuring each generated string is uniquely valid and that all possible combinations
      are found.'
    time_complexity: O(4^n / (n * sqrt(n))) which is the $n$-th Catalan number. Each
      valid sequence takes $O(n)$ time to construct or copy, making the total complexity
      $O(4^n / sqrt(n))$.
    space_complexity: O(n) representing the maximum depth of the recursion stack, which
      is $2n$. Storing the results themselves requires $O(n \cdot C_n)$ space, where
      $C_n$ is the $n$-th Catalan number.
    elapsed_time: 45.064658880233765
    model: gemini-3-flash-preview
    generated_at: '2026-10-02 03:26:06 '
---

## Problem #22: Generate Parentheses

**Difficulty:** Medium

**Topics:** String, Dynamic Programming, Backtracking, Bracket Sequences

## Problem Description

<p>Given <code>n</code> pairs of parentheses, write a function to <em>generate all combinations of well-formed parentheses</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> ["((()))","(()())","(())()","()(())","()()()"]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> ["()"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 8</code></li>
</ul>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem is solved using a recursive backtracking approach to explore all valid combinations of parentheses. We incrementally build a string of length $2n$ by making choices at each step: we can either add an opening parenthesis '(' or a closing parenthesis ')'. To ensure the combinations are well-formed, we maintain the counts of open and closed parentheses used so far, following two core constraints: the total number of open parentheses cannot exceed $n$, and a closing parenthesis can only be added if its count is strictly less than the count of open parentheses currently in the string.

This strategy prunes invalid branches of the recursion tree early, as it never attempts to place a closing parenthesis that doesn't have a matching opening one preceding it. When the length of the current string reaches $2n$, we know a complete and valid combination has been formed, so we add it to our result list. This process effectively explores the state space of all valid bracket sequences, ensuring each generated string is uniquely valid and that all possible combinations are found.

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
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        string current = "";
        backtrack(result, current, 0, 0, n);
        return result;
    }

private:
    void backtrack(vector<string>& result, string& current, int open, int close, int n) {
        if (current.length() == 2 * n) {
            result.push_back(current);
            return;
        }
        if (open < n) {
            current.push_back('(');
            backtrack(result, current, open + 1, close, n);
            current.pop_back();
        }
        if (close < open) {
            current.push_back(')');
            backtrack(result, current, open, close + 1, n);
            current.pop_back();
        }
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.*;

class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        backtrack(result, new StringBuilder(), 0, 0, n);
        return result;
    }

    private void backtrack(List<String> result, StringBuilder current, int open, int close, int n) {
        if (current.length() == 2 * n) {
            result.add(current.toString());
            return;
        }
        if (open < n) {
            current.append('(');
            backtrack(result, current, open + 1, close, n);
            current.deleteCharAt(current.length() - 1);
        }
        if (close < open) {
            current.append(')');
            backtrack(result, current, open, close + 1, n);
            current.deleteCharAt(current.length() - 1);
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def backtrack(current, open_count, close_count):
            if len(current) == 2 * n:
                result.append(current)
                return
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        def backtrack(current, open_count, close_count):
            if len(current) == 2 * n:
                result.append(current)
                return
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

void backtrack(int n, int open, int close, char* current, int index, char** result, int* returnSize) {
    if (index == 2 * n) {
        current[index] = '\0';
        result[*returnSize] = (char*)malloc((2 * n + 1) * sizeof(char));
        strcpy(result[*returnSize], current);
        (*returnSize)++;
        return;
    }
    if (open < n) {
        current[index] = '(';
        backtrack(n, open + 1, close, current, index + 1, result, returnSize);
    }
    if (close < open) {
        current[index] = ')';
        backtrack(n, open, close + 1, current, index + 1, result, returnSize);
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** generateParenthesis(int n, int* returnSize) {
    *returnSize = 0;
    char** result = (char**)malloc(2000 * sizeof(char*));
    char* current = (char*)malloc((2 * n + 1) * sizeof(char));
    backtrack(n, 0, 0, current, 0, result, returnSize);
    free(current);
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public IList<string> GenerateParenthesis(int n) {
        List<string> result = new List<string>();
        Backtrack(result, "", 0, 0, n);
        return result;
    }

    private void Backtrack(List<string> result, string current, int open, int close, int max) {
        if (current.Length == max * 2) {
            result.Add(current);
            return;
        }

        if (open < max) {
            Backtrack(result, current + "(", open + 1, close, max);
        }
        if (close < open) {
            Backtrack(result, current + ")", open, close + 1, max);
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    const result = [];

    const backtrack = (current, open, close) => {
        if (current.length === n * 2) {
            result.push(current);
            return;
        }

        if (open < n) {
            backtrack(current + "(", open + 1, close);
        }
        if (close < open) {
            backtrack(current + ")", open, close + 1);
        }
    };

    backtrack("", 0, 0);
    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function generateParenthesis(n: number): string[] {
    const result: string[] = [];

    const backtrack = (current: string, open: number, close: number): void => {
        if (current.length === n * 2) {
            result.push(current);
            return;
        }

        if (open < n) {
            backtrack(current + "(", open + 1, close);
        }
        if (close < open) {
            backtrack(current + ")", open, close + 1);
        }
    };

    backtrack("", 0, 0);
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
     * @param Integer $n
     * @return String[]
     */
    function generateParenthesis($n) {
        $result = [];
        $this->backtrack($result, "", 0, 0, $n);
        return $result;
    }

    private function backtrack(&$result, $current, $open, $close, $n) {
        if (strlen($current) === 2 * $n) {
            $result[] = $current;
            return;
        }

        if ($open < $n) {
            $this->backtrack($result, $current . "(", $open + 1, $close, $n);
        }
        if ($close < $open) {
            $this->backtrack($result, $current . ")", $open, $close + 1, $n);
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func generateParenthesis(_ n: Int) -> [String] {
        var result = [String]()
        backtrack(&result, "", 0, 0, n)
        return result
    }

    private func backtrack(_ result: inout [String], _ current: String, _ open: Int, _ close: Int, _ n: Int) {
        if current.count == n * 2 {
            result.append(current)
            return
        }

        if open < n {
            backtrack(&result, current + "(", open + 1, close, n)
        }
        if close < open {
            backtrack(&result, current + ")", open, close + 1, n)
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun generateParenthesis(n: Int): List<String> {
        val result = mutableListOf<String>()
        backtrack(result, StringBuilder(), 0, 0, n)
        return result
    }

    private fun backtrack(result: MutableList<String>, current: StringBuilder, open: Int, close: Int, max: Int) {
        if (current.length == max * 2) {
            result.add(current.toString())
            return
        }
        if (open < max) {
            current.append('(')
            backtrack(result, current, open + 1, close, max)
            current.deleteCharAt(current.length - 1)
        }
        if (close < open) {
            current.append(')')
            backtrack(result, current, open, close + 1, max)
            current.deleteCharAt(current.length - 1)
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<String> generateParenthesis(int n) {
    List<String> result = [];
    _backtrack(result, "", 0, 0, n);
    return result;
  }

  void _backtrack(List<String> result, String current, int open, int close, int max) {
    if (current.length == max * 2) {
      result.add(current);
      return;
    }
    if (open < max) {
      _backtrack(result, current + "(", open + 1, close, max);
    }
    if (close < open) {
      _backtrack(result, current + ")", open, close + 1, max);
    }
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func generateParenthesis(n int) []string {
    result := []string{}
    var backtrack func(current string, open int, close int)
    backtrack = func(current string, open int, close int) {
        if len(current) == 2*n {
            result = append(result, current)
            return
        }
        if open < n {
            backtrack(current+"(", open+1, close)
        }
        if close < open {
            backtrack(current+")", open, close+1)
        }
    }
    backtrack("", 0, 0)
    return result
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def generate_parenthesis(n)
    result = []
    backtrack(result, "", 0, 0, n)
    result
end

def backtrack(result, current, open_count, close_count, max)
    if current.length == max * 2
        result << current
        return
    end
    if open_count < max
        backtrack(result, current + "(", open_count + 1, close_count, max)
    end
    if close_count < open_count
        backtrack(result, current + ")", open_count, close_count + 1, max)
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def generateParenthesis(n: Int): List[String] = {
        val result = scala.collection.mutable.ListBuffer[String]()
        def backtrack(current: String, open: Int, close: Int): Unit = {
            if (current.length == 2 * n) {
                result += current
                return
            }
            if (open < n) {
                backtrack(current + "(", open + 1, close)
            }
            if (close < open) {
                backtrack(current + ")", open, close + 1)
            }
        }
        backtrack("", 0, 0)
        result.toList
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        let mut result = Vec::new();
        let mut current = String::new();
        Self::backtrack(&mut result, &mut current, 0, 0, n);
        result
    }

    fn backtrack(result: &mut Vec<String>, current: &mut String, open: i32, close: i32, max: i32) {
        if current.len() == (max * 2) as usize {
            result.push(current.clone());
            return;
        }

        if open < max {
            current.push('(');
            Self::backtrack(result, current, open + 1, close, max);
            current.pop();
        }

        if close < open {
            current.push(')');
            Self::backtrack(result, current, open, close + 1, max);
            current.pop();
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (generate-parenthesis n)
  (-> exact-integer? (listof string?))
  (define (backtrack open close current)
    (if (= (string-length current) (* 2 n))
        (list current)
        (let ()
          (define left (if (< open n)
                           (backtrack (+ open 1) close (string-append current "("))
                           '()))
          (define right (if (< close open)
                            (backtrack open (+ close 1) (string-append current ")"))
                            '()))
          (append left right))))
  (backtrack 0 0 ""))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec generate_parenthesis(N :: integer()) -> [unicode:unicode_binary()].
generate_parenthesis(N) ->
  backtrack(0, 0, N, <<>>).

backtrack(Open, Close, N, Acc) when byte_size(Acc) =:= 2 * N ->
  [Acc];
backtrack(Open, Close, N, Acc) ->
  Res1 = if
    Open < N -> backtrack(Open + 1, Close, N, <<Acc/binary, "(">>);
    true -> []
  end,
  Res2 = if
    Close < Open -> backtrack(Open, Close + 1, N, <<Acc/binary, ")">>);
    true -> []
  end,
  Res1 ++ Res2.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec generate_parenthesis(n :: integer) :: [String.t]
  def generate_parenthesis(n) do
    backtrack(0, 0, n, "")
  end

  defp backtrack(open, close, n, acc) when byte_size(acc) == 2 * n do
    [acc]
  end

  defp backtrack(open, close, n, acc) do
    res1 = if open < n do
      backtrack(open + 1, close, n, acc <> "(")
    else
      []
    end

    res2 = if close < open do
      backtrack(open, close + 1, n, acc <> ")")
    else
      []
    end

    res1 ++ res2
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(4^n / (n * sqrt(n))) which is the $n$-th Catalan number. Each valid sequence takes $O(n)$ time to construct or copy, making the total complexity $O(4^n / sqrt(n))$.
- **Space Complexity:** O(n) representing the maximum depth of the recursion stack, which is $2n$. Storing the results themselves requires $O(n \cdot C_n)$ space, where $C_n$ is the $n$-th Catalan number.
