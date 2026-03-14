---
layout: post
title: "The k-th Lexicographical String of All Happy Strings of Length n"
date: 2026-03-14 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Backtracking"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    string getHappyString(int n, int k) {\n \
        \       string result = \"\";\n        int count = 0;\n        string current\
        \ = \"\";\n        backtrack(n, k, count, current, result);\n        return\
        \ result;\n    }\n\nprivate:\n    void backtrack(int n, int k, int& count, string\
        \ current, string& result) {\n        if (!result.empty()) return;\n       \
        \ if (current.length() == n) {\n            count++;\n            if (count\
        \ == k) result = current;\n            return;\n        }\n        for (char\
        \ c : {'a', 'b', 'c'}) {\n            if (current.empty() || current.back()\
        \ != c) {\n                backtrack(n, k, count, current + c, result);\n  \
        \          }\n        }\n    }\n};"
      java: "class Solution {\n    private int count = 0;\n    private String result\
        \ = \"\";\n\n    public String getHappyString(int n, int k) {\n        count\
        \ = 0;\n        result = \"\";\n        backtrack(n, k, new StringBuilder());\n\
        \        return result;\n    }\n\n    private void backtrack(int n, int k, StringBuilder\
        \ current) {\n        if (!result.isEmpty()) return;\n        if (current.length()\
        \ == n) {\n            count++;\n            if (count == k) {\n           \
        \     result = current.toString();\n            }\n            return;\n   \
        \     }\n        for (char c = 'a'; c <= 'c'; c++) {\n            if (current.length()\
        \ == 0 || current.charAt(current.length() - 1) != c) {\n                current.append(c);\n\
        \                backtrack(n, k, current);\n                current.deleteCharAt(current.length()\
        \ - 1);\n            }\n        }\n    }\n}"
      python: "class Solution(object):\n    def getHappyString(self, n, k):\n      \
        \  self.count = 0\n        self.result = \"\"\n\n        def dfs(current):\n\
        \            if self.result != \"\":\n                return\n            if\
        \ len(current) == n:\n                self.count += 1\n                if self.count\
        \ == k:\n                    self.result = current\n                return\n\
        \            for char in ['a', 'b', 'c']:\n                if not current or\
        \ current[-1] != char:\n                    dfs(current + char)\n\n        dfs(\"\
        \")\n        return self.result"
      python3: "class Solution:\n    def getHappyString(self, n: int, k: int) -> str:\n\
        \        count = 0\n        result = \"\"\n\n        def dfs(current):\n   \
        \         nonlocal count, result\n            if result:\n                return\n\
        \            if len(current) == n:\n                count += 1\n           \
        \     if count == k:\n                    result = current\n               \
        \ return\n            for char in 'abc':\n                if not current or\
        \ current[-1] != char:\n                    dfs(current + char)\n\n        dfs(\"\
        \")\n        return result"
      c: "#include <stdlib.h>\n#include <string.h>\n\nvoid dfs(int n, int k, int depth,\
        \ char* current, int* count, char* result) {\n    if (result[0] != '\\0') return;\n\
        \    if (depth == n) {\n        (*count)++;\n        if (*count == k) {\n  \
        \          current[depth] = '\\0';\n            strcpy(result, current);\n \
        \       }\n        return;\n    }\n    for (char c = 'a'; c <= 'c'; c++) {\n\
        \        if (depth == 0 || current[depth - 1] != c) {\n            current[depth]\
        \ = c;\n            dfs(n, k, depth + 1, current, count, result);\n        }\n\
        \    }\n}\n\nchar* getHappyString(int n, int k) {\n    int total = 3 * (1 <<\
        \ (n - 1));\n    if (k > total) {\n        char* empty = (char*)malloc(1);\n\
        \        empty[0] = '\\0';\n        return empty;\n    }\n    char* result =\
        \ (char*)malloc(n + 1);\n    char* current = (char*)malloc(n + 1);\n    int\
        \ count = 0;\n    result[0] = '\\0';\n    dfs(n, k, 0, current, &count, result);\n\
        \    free(current);\n    return result;\n}"
      csharp: "public class Solution {\n    public string GetHappyString(int n, int\
        \ k) {\n        int count = 0;\n        string result = \"\";\n        Backtrack(n,\
        \ k, \"\", ref count, ref result);\n        return result;\n    }\n\n    private\
        \ void Backtrack(int n, int k, string current, ref int count, ref string result)\
        \ {\n        if (result != \"\") return;\n        if (current.Length == n) {\n\
        \            count++;\n            if (count == k) result = current;\n     \
        \       return;\n        }\n        foreach (char c in new char[] { 'a', 'b',\
        \ 'c' }) {\n            if (current.Length == 0 || current[current.Length -\
        \ 1] != c) {\n                Backtrack(n, k, current + c, ref count, ref result);\n\
        \            }\n        }\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @param {number} k\n * @return {string}\n\
        \ */\nvar getHappyString = function(n, k) {\n    let count = 0;\n    let result\
        \ = \"\";\n\n    const backtrack = (current) => {\n        if (result !== \"\
        \") return;\n        if (current.length === n) {\n            count++;\n   \
        \         if (count === k) {\n                result = current;\n          \
        \  }\n            return;\n        }\n        for (const char of ['a', 'b',\
        \ 'c']) {\n            if (current.length === 0 || current[current.length -\
        \ 1] !== char) {\n                backtrack(current + char);\n            }\n\
        \        }\n    };\n\n    backtrack(\"\");\n    return result;\n};"
      typescript: "function getHappyString(n: number, k: number): string {\n    let\
        \ count = 0;\n    let result = \"\";\n    const backtrack = (curr: string) =>\
        \ {\n        if (result !== \"\") return;\n        if (curr.length === n) {\n\
        \            count++;\n            if (count === k) {\n                result\
        \ = curr;\n            }\n            return;\n        }\n        for (const\
        \ char of [\"a\", \"b\", \"c\"]) {\n            if (curr.length === 0 || curr[curr.length\
        \ - 1] !== char) {\n                backtrack(curr + char);\n            }\n\
        \        }\n    };\n    backtrack(\"\");\n    return result;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @param Integer\
        \ $k\n     * @return String\n     */\n    private $count = 0;\n    private $result\
        \ = \"\";\n\n    function getHappyString($n, $k) {\n        $this->count = 0;\n\
        \        $this->result = \"\";\n        $this->backtrack($n, $k, \"\");\n  \
        \      return $this->result;\n    }\n\n    private function backtrack($n, $k,\
        \ $curr) {\n        if ($this->result !== \"\") return;\n        if (strlen($curr)\
        \ == $n) {\n            $this->count++;\n            if ($this->count == $k)\
        \ {\n                $this->result = $curr;\n            }\n            return;\n\
        \        }\n        foreach (['a', 'b', 'c'] as $char) {\n            if ($curr\
        \ === \"\" || $curr[strlen($curr) - 1] !== $char) {\n                $this->backtrack($n,\
        \ $k, $curr . $char);\n            }\n        }\n    }\n}"
      swift: "class Solution {\n    func getHappyString(_ n: Int, _ k: Int) -> String\
        \ {\n        var count = 0\n        var result = \"\"\n        func backtrack(_\
        \ curr: String) {\n            if !result.isEmpty { return }\n            if\
        \ curr.count == n {\n                count += 1\n                if count ==\
        \ k {\n                    result = curr\n                }\n              \
        \  return\n            }\n            for char in [\"a\", \"b\", \"c\"] {\n\
        \                if curr.isEmpty || String(curr.last!) != char {\n         \
        \           backtrack(curr + char)\n                }\n            }\n     \
        \   }\n        backtrack(\"\")\n        return result\n    }\n}"
      kotlin: "class Solution {\n    fun getHappyString(n: Int, k: Int): String {\n\
        \        var count = 0\n        var result = \"\"\n        fun backtrack(curr:\
        \ String) {\n            if (result != \"\") return\n            if (curr.length\
        \ == n) {\n                count++\n                if (count == k) result =\
        \ curr\n                return\n            }\n            for (char in charArrayOf('a',\
        \ 'b', 'c')) {\n                if (curr.isEmpty() || curr.last() != char) {\n\
        \                    backtrack(curr + char)\n                }\n           \
        \ }\n        }\n        backtrack(\"\")\n        return result\n    }\n}"
      dart: "class Solution {\n  String getHappyString(int n, int k) {\n    int count\
        \ = 0;\n    String result = \"\";\n    void backtrack(String curr) {\n     \
        \ if (result.isNotEmpty) return;\n      if (curr.length == n) {\n        count++;\n\
        \        if (count == k) {\n          result = curr;\n        }\n        return;\n\
        \      }\n      for (var char in ['a', 'b', 'c']) {\n        if (curr.isEmpty\
        \ || curr[curr.length - 1] != char) {\n          backtrack(curr + char);\n \
        \       }\n      }\n    }\n    backtrack(\"\");\n    return result;\n  }\n}"
      go: "func getHappyString(n int, k int) string {\n\tcount := 0\n\tresult := \"\"\
        \n\tvar backtrack func(string)\n\tbacktrack = func(curr string) {\n\t\tif result\
        \ != \"\" {\n\t\t\treturn\n\t\t}\n\t\tif len(curr) == n {\n\t\t\tcount++\n\t\
        \t\tif count == k {\n\t\t\t\tresult = curr\n\t\t\t}\n\t\t\treturn\n\t\t}\n\t\
        \tfor _, char := range []string{\"a\", \"b\", \"c\"} {\n\t\t\tif len(curr) ==\
        \ 0 || string(curr[len(curr)-1]) != char {\n\t\t\t\tbacktrack(curr + char)\n\
        \t\t\t}\n\t\t}\n\t}\n\tbacktrack(\"\")\n\treturn result\n}"
      ruby: "def get_happy_string(n, k)\n  total = 3 * (2**(n - 1))\n  return \"\" if\
        \ k > total\n\n  res = \"\"\n  chars = [\"a\", \"b\", \"c\"]\n\n  step = 2**(n\
        \ - 1)\n  idx = (k - 1) / step\n  res << chars[idx]\n  curr_k = (k - 1) % step\n\
        \n  (n - 1).times do |i|\n    last_char = res[-1]\n    options = chars.reject\
        \ { |c| c == last_char }\n    step /= 2\n    idx = curr_k / step\n    res <<\
        \ options[idx]\n    curr_k %= step\n  end\n  res\nend"
      scala: "object Solution {\n    def getHappyString(n: Int, k: Int): String = {\n\
        \        val total = 3 * Math.pow(2, n - 1).toInt\n        if (k > total) return\
        \ \"\"\n\n        var res = \"\"\n        val chars = List('a', 'b', 'c')\n\
        \        var currentK = k - 1\n        var step = Math.pow(2, n - 1).toInt\n\
        \n        val idx = currentK / step\n        res = res + chars(idx)\n      \
        \  currentK %= step\n\n        for (i <- 1 until n) {\n            step /= 2\n\
        \            val lastChar = res.last\n            val options = chars.filter(_\
        \ != lastChar)\n            val idxInner = currentK / step\n            res\
        \ = res + options(idxInner)\n            currentK %= step\n        }\n     \
        \   res\n    }\n}"
      rust: "impl Solution {\n    pub fn get_happy_string(n: i32, k: i32) -> String\
        \ {\n        let total = 3 * 2_i32.pow((n - 1) as u32);\n        if k > total\
        \ { return \"\".to_string(); }\n\n        let mut res = String::new();\n   \
        \     let chars = vec!['a', 'b', 'c'];\n        let mut current_k = k - 1;\n\
        \        let mut step = 2_i32.pow((n - 1) as u32);\n\n        let idx = (current_k\
        \ / step) as usize;\n        res.push(chars[idx]);\n        current_k %= step;\n\
        \n        for _ in 1..n {\n            step /= 2;\n            let last_char\
        \ = res.chars().last().unwrap();\n            let options: Vec<char> = chars.iter().cloned().filter(|&c|\
        \ c != last_char).collect();\n            let idx = (current_k / step) as usize;\n\
        \            res.push(options[idx]);\n            current_k %= step;\n     \
        \   }\n        res\n    }\n}"
      racket: "(define/contract (get-happy-string n k)\n  (-> exact-integer? exact-integer?\
        \ string?)\n  (let ([total (* 3 (expt 2 (- n 1)))])\n    (if (> k total)\n \
        \       \"\"\n        (let loop ([i 0] [curr-k (- k 1)] [res \"\"])\n      \
        \    (if (= i n)\n              res\n              (let* ([step (expt 2 (- n\
        \ 1 i))]\n                     [idx (quotient curr-k step)]\n              \
        \       [next-k (remainder curr-k step)]\n                     [chars '(#\\\
        a #\\b #\\c)]\n                     [last-char (if (= i 0) #f (string-ref res\
        \ (- i 1)))]\n                     [options (if last-char \n               \
        \                   (filter (lambda (c) (not (char=? c last-char))) chars)\n\
        \                                  chars)]\n                     [chosen (list-ref\
        \ options idx)])\n                (loop (+ i 1) next-k (string-append res (string\
        \ chosen)))))))))"
      erlang: "-spec get_happy_string(N :: integer(), K :: integer()) -> unicode:unicode_binary().\n\
        get_happy_string(N, K) ->\n  Total = 3 * trunc(math:pow(2, N - 1)),\n  if\n\
        \    K > Total -> <<>>;\n    true -> solve(N, K - 1, [$a, $b, $c], [])\n  end.\n\
        \nsolve(0, _, _, Acc) -> list_to_binary(lists:reverse(Acc));\nsolve(N, K, Chars,\
        \ Acc) ->\n  Step = trunc(math:pow(2, N - 1)),\n  Idx = K div Step,\n  NextK\
        \ = K rem Step,\n  Options = case Acc of\n    [] -> Chars;\n    [Last | _] ->\
        \ [C || C <- Chars, C /= Last]\n  end,\n  Chosen = lists:nth(Idx + 1, Options),\n\
        \  solve(N - 1, NextK, Chars, [Chosen | Acc])."
      elixir: "defmodule Solution do\n  @spec get_happy_string(n :: integer, k :: integer)\
        \ :: String.t\n  def get_happy_string(n, k) do\n    total = 3 * round(:math.pow(2,\
        \ n - 1))\n    if k > total do\n      \"\"\n    else\n      solve(n, k - 1,\
        \ [?a, ?b, ?c], [])\n    end\n  end\n\n  defp solve(0, _k, _chars, acc), do:\
        \ List.to_string(Enum.reverse(acc))\n  defp solve(n, k, chars, acc) do\n   \
        \ step = round(:math.pow(2, n - 1))\n    idx = div(k, step)\n    next_k = rem(k,\
        \ step)\n    options = case acc do\n      [] -> chars\n      [last | _] -> Enum.filter(chars,\
        \ &(&1 != last))\n    end\n    chosen = Enum.at(options, idx)\n    solve(n -\
        \ 1, next_k, chars, [chosen | acc])\n  end\nend"
    approach: 'To solve this problem, we can use a backtracking algorithm to generate
      all happy strings of length $n$ in lexicographical order. A happy string consists
      of the characters ''a'', ''b'', and ''c'' where no two adjacent characters are
      the same. By always trying to append characters in the order ''a'', ''b'', then
      ''c'', the recursive exploration naturally visits potential happy strings in their
      alphabetical order.


      To optimize the search, we maintain a counter to track how many happy strings
      have been formed. As soon as the counter reaches $k$, we capture the current string
      and terminate the recursion immediately. We also check the total number of possible
      happy strings, which is $3 \times 2^{n-1}$, to return an empty string early if
      $k$ is beyond the available count. This approach ensures we only visit the necessary
      portion of the search space.'
    time_complexity: O(k \cdot n) where $k$ is the target index and $n$ is the length
      of the string. In the worst case, we might need to explore all happy strings if
      $k$ is large, but the search stops as soon as the $k$-th string is found. Each
      happy string construction involves $n$ recursive steps.
    space_complexity: O(n) which is determined by the depth of the recursion stack and
      the memory required to store the current string during the backtracking process.
    elapsed_time: 179.33137941360474
    model: gemini-3-flash-preview
    generated_at: '2026-03-14 01:24:06 '
---

## Problem #1415: The k-th Lexicographical String of All Happy Strings of Length n

**Difficulty:** Medium

**Topics:** String, Backtracking

## Problem Description

<p>A <strong>happy string</strong> is a string that:</p>

<ul>
	<li>consists only of letters of the set <code>[&#39;a&#39;, &#39;b&#39;, &#39;c&#39;]</code>.</li>
	<li><code>s[i] != s[i + 1]</code> for all values of <code>i</code> from <code>1</code> to <code>s.length - 1</code> (string is 1-indexed).</li>
</ul>

<p>For example, strings <strong>&quot;abc&quot;, &quot;ac&quot;, &quot;b&quot;</strong> and <strong>&quot;abcbabcbcb&quot;</strong> are all happy strings and strings <strong>&quot;aa&quot;, &quot;baa&quot;</strong> and <strong>&quot;ababbc&quot;</strong> are not happy strings.</p>

<p>Given two integers <code>n</code> and <code>k</code>, consider a list of all happy strings of length <code>n</code> sorted in lexicographical order.</p>

<p>Return <em>the kth string</em> of this list or return an <strong>empty string</strong> if there are less than <code>k</code> happy strings of length <code>n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 1, k = 3
<strong>Output:</strong> &quot;c&quot;
<strong>Explanation:</strong> The list [&quot;a&quot;, &quot;b&quot;, &quot;c&quot;] contains all happy strings of length 1. The third string is &quot;c&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1, k = 4
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> There are only 3 happy strings of length 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 3, k = 9
<strong>Output:</strong> &quot;cab&quot;
<strong>Explanation:</strong> There are 12 different happy string of length 3 [&quot;aba&quot;, &quot;abc&quot;, &quot;aca&quot;, &quot;acb&quot;, &quot;bab&quot;, &quot;bac&quot;, &quot;bca&quot;, &quot;bcb&quot;, &quot;cab&quot;, &quot;cac&quot;, &quot;cba&quot;, &quot;cbc&quot;]. You will find the 9<sup>th</sup> string = &quot;cab&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10</code></li>
	<li><code>1 &lt;= k &lt;= 100</code></li>
</ul>


## Hints

1. Generate recursively all the happy strings of length n.

2. Sort them in lexicographical order and return the kth string if it exists.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To solve this problem, we can use a backtracking algorithm to generate all happy strings of length $n$ in lexicographical order. A happy string consists of the characters 'a', 'b', and 'c' where no two adjacent characters are the same. By always trying to append characters in the order 'a', 'b', then 'c', the recursive exploration naturally visits potential happy strings in their alphabetical order.

To optimize the search, we maintain a counter to track how many happy strings have been formed. As soon as the counter reaches $k$, we capture the current string and terminate the recursion immediately. We also check the total number of possible happy strings, which is $3 \times 2^{n-1}$, to return an empty string early if $k$ is beyond the available count. This approach ensures we only visit the necessary portion of the search space.

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
    string getHappyString(int n, int k) {
        string result = "";
        int count = 0;
        string current = "";
        backtrack(n, k, count, current, result);
        return result;
    }

private:
    void backtrack(int n, int k, int& count, string current, string& result) {
        if (!result.empty()) return;
        if (current.length() == n) {
            count++;
            if (count == k) result = current;
            return;
        }
        for (char c : {'a', 'b', 'c'}) {
            if (current.empty() || current.back() != c) {
                backtrack(n, k, count, current + c, result);
            }
        }
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    private int count = 0;
    private String result = "";

    public String getHappyString(int n, int k) {
        count = 0;
        result = "";
        backtrack(n, k, new StringBuilder());
        return result;
    }

    private void backtrack(int n, int k, StringBuilder current) {
        if (!result.isEmpty()) return;
        if (current.length() == n) {
            count++;
            if (count == k) {
                result = current.toString();
            }
            return;
        }
        for (char c = 'a'; c <= 'c'; c++) {
            if (current.length() == 0 || current.charAt(current.length() - 1) != c) {
                current.append(c);
                backtrack(n, k, current);
                current.deleteCharAt(current.length() - 1);
            }
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
    def getHappyString(self, n, k):
        self.count = 0
        self.result = ""

        def dfs(current):
            if self.result != "":
                return
            if len(current) == n:
                self.count += 1
                if self.count == k:
                    self.result = current
                return
            for char in ['a', 'b', 'c']:
                if not current or current[-1] != char:
                    dfs(current + char)

        dfs("")
        return self.result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        count = 0
        result = ""

        def dfs(current):
            nonlocal count, result
            if result:
                return
            if len(current) == n:
                count += 1
                if count == k:
                    result = current
                return
            for char in 'abc':
                if not current or current[-1] != char:
                    dfs(current + char)

        dfs("")
        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

void dfs(int n, int k, int depth, char* current, int* count, char* result) {
    if (result[0] != '\0') return;
    if (depth == n) {
        (*count)++;
        if (*count == k) {
            current[depth] = '\0';
            strcpy(result, current);
        }
        return;
    }
    for (char c = 'a'; c <= 'c'; c++) {
        if (depth == 0 || current[depth - 1] != c) {
            current[depth] = c;
            dfs(n, k, depth + 1, current, count, result);
        }
    }
}

char* getHappyString(int n, int k) {
    int total = 3 * (1 << (n - 1));
    if (k > total) {
        char* empty = (char*)malloc(1);
        empty[0] = '\0';
        return empty;
    }
    char* result = (char*)malloc(n + 1);
    char* current = (char*)malloc(n + 1);
    int count = 0;
    result[0] = '\0';
    dfs(n, k, 0, current, &count, result);
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
    public string GetHappyString(int n, int k) {
        int count = 0;
        string result = "";
        Backtrack(n, k, "", ref count, ref result);
        return result;
    }

    private void Backtrack(int n, int k, string current, ref int count, ref string result) {
        if (result != "") return;
        if (current.Length == n) {
            count++;
            if (count == k) result = current;
            return;
        }
        foreach (char c in new char[] { 'a', 'b', 'c' }) {
            if (current.Length == 0 || current[current.Length - 1] != c) {
                Backtrack(n, k, current + c, ref count, ref result);
            }
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
 * @param {number} k
 * @return {string}
 */
var getHappyString = function(n, k) {
    let count = 0;
    let result = "";

    const backtrack = (current) => {
        if (result !== "") return;
        if (current.length === n) {
            count++;
            if (count === k) {
                result = current;
            }
            return;
        }
        for (const char of ['a', 'b', 'c']) {
            if (current.length === 0 || current[current.length - 1] !== char) {
                backtrack(current + char);
            }
        }
    };

    backtrack("");
    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function getHappyString(n: number, k: number): string {
    let count = 0;
    let result = "";
    const backtrack = (curr: string) => {
        if (result !== "") return;
        if (curr.length === n) {
            count++;
            if (count === k) {
                result = curr;
            }
            return;
        }
        for (const char of ["a", "b", "c"]) {
            if (curr.length === 0 || curr[curr.length - 1] !== char) {
                backtrack(curr + char);
            }
        }
    };
    backtrack("");
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
     * @param Integer $k
     * @return String
     */
    private $count = 0;
    private $result = "";

    function getHappyString($n, $k) {
        $this->count = 0;
        $this->result = "";
        $this->backtrack($n, $k, "");
        return $this->result;
    }

    private function backtrack($n, $k, $curr) {
        if ($this->result !== "") return;
        if (strlen($curr) == $n) {
            $this->count++;
            if ($this->count == $k) {
                $this->result = $curr;
            }
            return;
        }
        foreach (['a', 'b', 'c'] as $char) {
            if ($curr === "" || $curr[strlen($curr) - 1] !== $char) {
                $this->backtrack($n, $k, $curr . $char);
            }
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
    func getHappyString(_ n: Int, _ k: Int) -> String {
        var count = 0
        var result = ""
        func backtrack(_ curr: String) {
            if !result.isEmpty { return }
            if curr.count == n {
                count += 1
                if count == k {
                    result = curr
                }
                return
            }
            for char in ["a", "b", "c"] {
                if curr.isEmpty || String(curr.last!) != char {
                    backtrack(curr + char)
                }
            }
        }
        backtrack("")
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
    fun getHappyString(n: Int, k: Int): String {
        var count = 0
        var result = ""
        fun backtrack(curr: String) {
            if (result != "") return
            if (curr.length == n) {
                count++
                if (count == k) result = curr
                return
            }
            for (char in charArrayOf('a', 'b', 'c')) {
                if (curr.isEmpty() || curr.last() != char) {
                    backtrack(curr + char)
                }
            }
        }
        backtrack("")
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
  String getHappyString(int n, int k) {
    int count = 0;
    String result = "";
    void backtrack(String curr) {
      if (result.isNotEmpty) return;
      if (curr.length == n) {
        count++;
        if (count == k) {
          result = curr;
        }
        return;
      }
      for (var char in ['a', 'b', 'c']) {
        if (curr.isEmpty || curr[curr.length - 1] != char) {
          backtrack(curr + char);
        }
      }
    }
    backtrack("");
    return result;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func getHappyString(n int, k int) string {
	count := 0
	result := ""
	var backtrack func(string)
	backtrack = func(curr string) {
		if result != "" {
			return
		}
		if len(curr) == n {
			count++
			if count == k {
				result = curr
			}
			return
		}
		for _, char := range []string{"a", "b", "c"} {
			if len(curr) == 0 || string(curr[len(curr)-1]) != char {
				backtrack(curr + char)
			}
		}
	}
	backtrack("")
	return result
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def get_happy_string(n, k)
  total = 3 * (2**(n - 1))
  return "" if k > total

  res = ""
  chars = ["a", "b", "c"]

  step = 2**(n - 1)
  idx = (k - 1) / step
  res << chars[idx]
  curr_k = (k - 1) % step

  (n - 1).times do |i|
    last_char = res[-1]
    options = chars.reject { |c| c == last_char }
    step /= 2
    idx = curr_k / step
    res << options[idx]
    curr_k %= step
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
    def getHappyString(n: Int, k: Int): String = {
        val total = 3 * Math.pow(2, n - 1).toInt
        if (k > total) return ""

        var res = ""
        val chars = List('a', 'b', 'c')
        var currentK = k - 1
        var step = Math.pow(2, n - 1).toInt

        val idx = currentK / step
        res = res + chars(idx)
        currentK %= step

        for (i <- 1 until n) {
            step /= 2
            val lastChar = res.last
            val options = chars.filter(_ != lastChar)
            val idxInner = currentK / step
            res = res + options(idxInner)
            currentK %= step
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
    pub fn get_happy_string(n: i32, k: i32) -> String {
        let total = 3 * 2_i32.pow((n - 1) as u32);
        if k > total { return "".to_string(); }

        let mut res = String::new();
        let chars = vec!['a', 'b', 'c'];
        let mut current_k = k - 1;
        let mut step = 2_i32.pow((n - 1) as u32);

        let idx = (current_k / step) as usize;
        res.push(chars[idx]);
        current_k %= step;

        for _ in 1..n {
            step /= 2;
            let last_char = res.chars().last().unwrap();
            let options: Vec<char> = chars.iter().cloned().filter(|&c| c != last_char).collect();
            let idx = (current_k / step) as usize;
            res.push(options[idx]);
            current_k %= step;
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
(define/contract (get-happy-string n k)
  (-> exact-integer? exact-integer? string?)
  (let ([total (* 3 (expt 2 (- n 1)))])
    (if (> k total)
        ""
        (let loop ([i 0] [curr-k (- k 1)] [res ""])
          (if (= i n)
              res
              (let* ([step (expt 2 (- n 1 i))]
                     [idx (quotient curr-k step)]
                     [next-k (remainder curr-k step)]
                     [chars '(#\a #\b #\c)]
                     [last-char (if (= i 0) #f (string-ref res (- i 1)))]
                     [options (if last-char 
                                  (filter (lambda (c) (not (char=? c last-char))) chars)
                                  chars)]
                     [chosen (list-ref options idx)])
                (loop (+ i 1) next-k (string-append res (string chosen)))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec get_happy_string(N :: integer(), K :: integer()) -> unicode:unicode_binary().
get_happy_string(N, K) ->
  Total = 3 * trunc(math:pow(2, N - 1)),
  if
    K > Total -> <<>>;
    true -> solve(N, K - 1, [$a, $b, $c], [])
  end.

solve(0, _, _, Acc) -> list_to_binary(lists:reverse(Acc));
solve(N, K, Chars, Acc) ->
  Step = trunc(math:pow(2, N - 1)),
  Idx = K div Step,
  NextK = K rem Step,
  Options = case Acc of
    [] -> Chars;
    [Last | _] -> [C || C <- Chars, C /= Last]
  end,
  Chosen = lists:nth(Idx + 1, Options),
  solve(N - 1, NextK, Chars, [Chosen | Acc]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec get_happy_string(n :: integer, k :: integer) :: String.t
  def get_happy_string(n, k) do
    total = 3 * round(:math.pow(2, n - 1))
    if k > total do
      ""
    else
      solve(n, k - 1, [?a, ?b, ?c], [])
    end
  end

  defp solve(0, _k, _chars, acc), do: List.to_string(Enum.reverse(acc))
  defp solve(n, k, chars, acc) do
    step = round(:math.pow(2, n - 1))
    idx = div(k, step)
    next_k = rem(k, step)
    options = case acc do
      [] -> chars
      [last | _] -> Enum.filter(chars, &(&1 != last))
    end
    chosen = Enum.at(options, idx)
    solve(n - 1, next_k, chars, [chosen | acc])
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(k \cdot n) where $k$ is the target index and $n$ is the length of the string. In the worst case, we might need to explore all happy strings if $k$ is large, but the search stops as soon as the $k$-th string is found. Each happy string construction involves $n$ recursive steps.
- **Space Complexity:** O(n) which is determined by the depth of the recursion stack and the memory required to store the current string during the backtracking process.
