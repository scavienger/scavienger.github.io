---
layout: post
title: "Special Binary String"
date: 2026-02-20 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["String", "Divide and Conquer", "Sorting"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/special-binary-string/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    string makeLargestSpecial(string s) {\n \
        \       if (s.empty()) return \"\";\n        vector<string> parts;\n       \
        \ int balance = 0, start = 0;\n        for (int i = 0; i < s.length(); ++i)\
        \ {\n            balance += (s[i] == '1' ? 1 : -1);\n            if (balance\
        \ == 0) {\n                string inner = s.substr(start + 1, i - start - 1);\n\
        \                parts.push_back(\"1\" + makeLargestSpecial(inner) + \"0\");\n\
        \                start = i + 1;\n            }\n        }\n        sort(parts.rbegin(),\
        \ parts.rend());\n        string res = \"\";\n        for (const string& p :\
        \ parts) res += p;\n        return res;\n    }\n};"
      java: "class Solution {\n    public String makeLargestSpecial(String s) {\n  \
        \      if (s.length() == 0) return \"\";\n        List<String> parts = new ArrayList<>();\n\
        \        int balance = 0, start = 0;\n        for (int i = 0; i < s.length();\
        \ i++) {\n            balance += (s.charAt(i) == '1' ? 1 : -1);\n          \
        \  if (balance == 0) {\n                parts.add(\"1\" + makeLargestSpecial(s.substring(start\
        \ + 1, i)) + \"0\");\n                start = i + 1;\n            }\n      \
        \  }\n        Collections.sort(parts, Collections.reverseOrder());\n       \
        \ return String.join(\"\", parts);\n    }\n}"
      python: "class Solution(object):\n    def makeLargestSpecial(self, s):\n     \
        \   \"\"\"\n        :type s: str\n        :rtype: str\n        \"\"\"\n    \
        \    if not s: return \"\"\n        res = []\n        balance = 0\n        start\
        \ = 0\n        for i, char in enumerate(s):\n            balance += 1 if char\
        \ == '1' else -1\n            if balance == 0:\n                res.append(\"\
        1\" + self.makeLargestSpecial(s[start + 1:i]) + \"0\")\n                start\
        \ = i + 1\n        res.sort(reverse=True)\n        return \"\".join(res)"
      python3: "class Solution:\n    def makeLargestSpecial(self, s: str) -> str:\n\
        \        if not s: return \"\"\n        parts = []\n        balance = 0\n  \
        \      start = 0\n        for i, char in enumerate(s):\n            balance\
        \ += 1 if char == '1' else -1\n            if balance == 0:\n              \
        \  parts.append(\"1\" + self.makeLargestSpecial(s[start + 1:i]) + \"0\")\n \
        \               start = i + 1\n        return \"\".join(sorted(parts, reverse=True))"
      c: "int compare(const void* a, const void* b) {\n    return strcmp(*(const char**)b,\
        \ *(const char**)a);\n}\n\nchar* makeLargestSpecial(char* s) {\n    int n =\
        \ strlen(s);\n    if (n == 0) return \"\";\n\n    char** parts = malloc(n *\
        \ sizeof(char*));\n    int partsCount = 0;\n    int balance = 0, start = 0;\n\
        \n    for (int i = 0; i < n; i++) {\n        balance += (s[i] == '1' ? 1 : -1);\n\
        \        if (balance == 0) {\n            int len = i - start - 1;\n       \
        \     char* sub = malloc(len + 1);\n            if (len > 0) strncpy(sub, s\
        \ + start + 1, len);\n            sub[len] = '\\0';\n\n            char* inner\
        \ = makeLargestSpecial(sub);\n            int innerLen = strlen(inner);\n  \
        \          parts[partsCount] = malloc(innerLen + 3);\n            parts[partsCount][0]\
        \ = '1';\n            strcpy(parts[partsCount] + 1, inner);\n            parts[partsCount][innerLen\
        \ + 1] = '0';\n            parts[partsCount][innerLen + 2] = '\\0';\n\n    \
        \        if (len > 0) free(sub);\n            partsCount++;\n            start\
        \ = i + 1;\n        }\n    }\n\n    qsort(parts, partsCount, sizeof(char*),\
        \ compare);\n\n    char* result = malloc(n + 1);\n    result[0] = '\\0';\n \
        \   for (int i = 0; i < partsCount; i++) {\n        strcat(result, parts[i]);\n\
        \        free(parts[i]);\n    }\n    free(parts);\n    return result;\n}"
      csharp: "public class Solution {\n    public string MakeLargestSpecial(string\
        \ s) {\n        if (string.IsNullOrEmpty(s)) return \"\";\n        List<string>\
        \ parts = new List<string>();\n        int balance = 0, start = 0;\n       \
        \ for (int i = 0; i < s.Length; i++) {\n            balance += (s[i] == '1'\
        \ ? 1 : -1);\n            if (balance == 0) {\n                parts.Add(\"\
        1\" + MakeLargestSpecial(s.Substring(start + 1, i - start - 1)) + \"0\");\n\
        \                start = i + 1;\n            }\n        }\n        parts.Sort((a,\
        \ b) => b.CompareTo(a));\n        return string.Concat(parts);\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {string}\n */\nvar makeLargestSpecial\
        \ = function(s) {\n    if (!s) return \"\";\n    let parts = [];\n    let balance\
        \ = 0;\n    let start = 0;\n    for (let i = 0; i < s.length; i++) {\n     \
        \   balance += (s[i] === '1' ? 1 : -1);\n        if (balance === 0) {\n    \
        \        parts.push(\"1\" + makeLargestSpecial(s.substring(start + 1, i)) +\
        \ \"0\");\n            start = i + 1;\n        }\n    }\n    parts.sort().reverse();\n\
        \    return parts.join(\"\");\n};"
      typescript: "function makeLargestSpecial(s: string): string {\n    if (s.length\
        \ === 0) return \"\";\n    let count = 0, i = 0;\n    const res: string[] =\
        \ [];\n    for (let j = 0; j < s.length; j++) {\n        count += (s[j] ===\
        \ '1' ? 1 : -1);\n        if (count === 0) {\n            res.push('1' + makeLargestSpecial(s.substring(i\
        \ + 1, j)) + '0');\n            i = j + 1;\n        }\n    }\n    return res.sort((a,\
        \ b) => (a < b ? 1 : -1)).join('');\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return String\n\
        \     */\n    function makeLargestSpecial($s) {\n        if ($s === \"\") return\
        \ \"\";\n        $count = 0;\n        $i = 0;\n        $res = [];\n        $len\
        \ = strlen($s);\n        for ($j = 0; $j < $len; $j++) {\n            $count\
        \ += ($s[$j] === '1' ? 1 : -1);\n            if ($count === 0) {\n         \
        \       $res[] = '1' . $this->makeLargestSpecial(substr($s, $i + 1, $j - $i\
        \ - 1)) . '0';\n                $i = $j + 1;\n            }\n        }\n   \
        \     rsort($res);\n        return implode(\"\", $res);\n    }\n}"
      swift: "class Solution {\n    func makeLargestSpecial(_ s: String) -> String {\n\
        \        if s.isEmpty { return \"\" }\n        var count = 0\n        var i\
        \ = 0\n        var res = [String]()\n        let chars = Array(s)\n        for\
        \ j in 0..<chars.count {\n            count += (chars[j] == \"1\" ? 1 : -1)\n\
        \            if count == 0 {\n                let startIdx = s.index(s.startIndex,\
        \ offsetBy: i + 1)\n                let endIdx = s.index(s.startIndex, offsetBy:\
        \ j)\n                let sub = String(s[startIdx..<endIdx])\n             \
        \   res.append(\"1\" + makeLargestSpecial(sub) + \"0\")\n                i =\
        \ j + 1\n            }\n        }\n        res.sort(by: >)\n        return res.joined()\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun makeLargestSpecial(s: String): String {\n \
        \       if (s.isEmpty()) return \"\"\n        var count = 0\n        var i =\
        \ 0\n        val res = mutableListOf<String>()\n        for (j in s.indices)\
        \ {\n            count += if (s[j] == '1') 1 else -1\n            if (count\
        \ == 0) {\n                res.add(\"1\" + makeLargestSpecial(s.substring(i\
        \ + 1, j)) + \"0\")\n                i = j + 1\n            }\n        }\n \
        \       res.sortDescending()\n        return res.joinToString(\"\")\n    }\n\
        }"
      dart: "class Solution {\n  String makeLargestSpecial(String s) {\n    if (s.isEmpty)\
        \ return \"\";\n    int count = 0;\n    int i = 0;\n    List<String> res = [];\n\
        \    for (int j = 0; j < s.length; j++) {\n      count += (s[j] == '1' ? 1 :\
        \ -1);\n      if (count == 0) {\n        res.add(\"1\" + makeLargestSpecial(s.substring(i\
        \ + 1, j)) + \"0\");\n        i = j + 1;\n      }\n    }\n    res.sort((a, b)\
        \ => b.compareTo(a));\n    return res.join(\"\");\n  }\n}"
      go: "import (\n    \"sort\"\n    \"strings\"\n)\n\nfunc makeLargestSpecial(s string)\
        \ string {\n    if len(s) == 0 {\n        return \"\"\n    }\n    count := 0\n\
        \    i := 0\n    var res []string\n    for j, char := range s {\n        if\
        \ char == '1' {\n            count++\n        } else {\n            count--\n\
        \        }\n        if count == 0 {\n            res = append(res, \"1\"+makeLargestSpecial(s[i+1:j])+\"\
        0\")\n            i = j + 1\n        }\n    }\n    sort.Slice(res, func(i, j\
        \ int) bool {\n        return res[i] > res[j]\n    })\n    return strings.Join(res,\
        \ \"\")\n}"
      ruby: "# @param {String} s\n# @return {String}\ndef make_largest_special(s)\n\
        \  return \"\" if s.empty?\n  res = []\n  count = 0\n  i = 0\n  s.chars.each_with_index\
        \ do |char, j|\n    count += (char == '1' ? 1 : -1)\n    if count == 0\n   \
        \   res << \"1#{make_largest_special(s[i + 1...j])}0\"\n      i = j + 1\n  \
        \  end\n  end\n  res.sort.reverse.join\nend"
      scala: "object Solution {\n    def makeLargestSpecial(s: String): String = {\n\
        \        if (s == \"\") return \"\"\n        val res = scala.collection.mutable.ListBuffer[String]()\n\
        \        var count = 0\n        var i = 0\n        for (j <- 0 until s.length)\
        \ {\n            if (s(j) == '1') count += 1 else count -= 1\n            if\
        \ (count == 0) {\n                res += \"1\" + makeLargestSpecial(s.substring(i\
        \ + 1, j)) + \"0\"\n                i = j + 1\n            }\n        }\n  \
        \      res.toList.sorted(Ordering.String.reverse).mkString\n    }\n}"
      rust: "impl Solution {\n    pub fn make_largest_special(s: String) -> String {\n\
        \        if s.is_empty() {\n            return \"\".to_string();\n        }\n\
        \        let mut res = Vec::new();\n        let mut count = 0;\n        let\
        \ mut i = 0;\n        let chars: Vec<char> = s.chars().collect();\n        for\
        \ (j, &c) in chars.iter().enumerate() {\n            if c == '1' {\n       \
        \         count += 1;\n            } else {\n                count -= 1;\n \
        \           }\n            if count == 0 {\n                let inner = chars[i\
        \ + 1..j].iter().collect::<String>();\n                res.push(format!(\"1{}0\"\
        , Self::make_largest_special(inner)));\n                i = j + 1;\n       \
        \     }\n        }\n        res.sort_unstable_by(|a, b| b.cmp(a));\n       \
        \ res.concat()\n    }\n}"
      racket: "(define/contract (make-largest-special s)\n  (-> string? string?)\n \
        \ (if (string=? s \"\")\n      \"\"\n      (let loop ([chars (string->list s)]\n\
        \                 [count 0]\n                 [start 0]\n                 [current-idx\
        \ 0]\n                 [acc '()])\n        (if (null? chars)\n            (apply\
        \ string-append (sort acc string>?))\n            (let* ([char (car chars)]\n\
        \                   [new-count (+ count (if (char=? char #\\1) 1 -1))])\n  \
        \            (if (= new-count 0)\n                  (let* ([inner (substring\
        \ s (+ start 1) current-idx)]\n                         [processed (string-append\
        \ \"1\" (make-largest-special inner) \"0\")])\n                    (loop (cdr\
        \ chars) 0 (+ current-idx 1) (+ current-idx 1) (cons processed acc)))\n    \
        \              (loop (cdr chars) new-count start (+ current-idx 1) acc)))))))"
      erlang: "-spec make_largest_special(S :: unicode:unicode_binary()) -> unicode:unicode_binary().\n\
        make_largest_special(S) ->\n  list_to_binary(do_solve(binary_to_list(S))).\n\
        \ndo_solve([]) -> [];\ndo_solve(S) ->\n  Substrings = find_sub(S, 0, [], []),\n\
        \  Processed = [ [$1 | do_solve(Sub)] ++ [$0] || Sub <- Substrings ],\n  Sorted\
        \ = lists:reverse(lists:sort(Processed)),\n  lists:flatten(Sorted).\n\nfind_sub([],\
        \ _, _, Acc) -> lists:reverse(Acc);\nfind_sub([H|T], Count, CurrentSub, Acc)\
        \ ->\n  NewCount = if H == $1 -> Count + 1; true -> Count - 1 end,\n  if\n \
        \   NewCount == 0 ->\n      FullSub = lists:reverse([H|CurrentSub]),\n     \
        \ [_First | Rest] = FullSub,\n      InnerPart = lists:sublist(Rest, length(Rest)\
        \ - 1),\n      find_sub(T, 0, [], [InnerPart | Acc]);\n    true ->\n      find_sub(T,\
        \ NewCount, [H|CurrentSub], Acc)\n  end."
      elixir: "defmodule Solution do\n  @spec make_largest_special(s :: String.t) ::\
        \ String.t\n  def make_largest_special(s) do\n    if s == \"\" do\n      \"\"\
        \n    else\n      {parts, _, _} = s\n        |> String.graphemes()\n       \
        \ |> Enum.reduce({[], 0, \"\"}, fn char, {acc, count, current} ->\n        \
        \  new_count = count + (if char == \"1\", do: 1, else: -1)\n          new_current\
        \ = current <> char\n          if new_count == 0 do\n            inner = String.slice(new_current,\
        \ 1, String.length(new_current) - 2)\n            {[\"1\" <> make_largest_special(inner)\
        \ <> \"0\" | acc], 0, \"\"}\n          else\n            {acc, new_count, new_current}\n\
        \          end\n        end)\n      parts\n      |> Enum.sort(:desc)\n     \
        \ |> Enum.join(\"\")\n    end\n  end\nend"
    approach: A special binary string can be decomposed into a sequence of top-level
      special components. Each component is a special string that starts with '1', ends
      with '0', and contains another special string in between. We can think of these
      components as balanced parentheses, where '1' is '(' and '0' is ')'. To maximize
      the string lexicographically, we must recursively maximize the inner part of each
      top-level component and then sort these components in descending order before
      concatenating them back together.
    time_complexity: O(N^2) where N is the length of the string. In the worst case,
      we scan the string once to find top-level components, and the sorting step takes
      $O(N^2 \log N)$ if we consider the string lengths. Given $N \le 50$, the recursive
      depth is at most $N/2$, leading to an efficient solution.
    space_complexity: O(N^2) to store the intermediate substrings created during the
      recursive process and the recursion stack depth.
    elapsed_time: 165.71119856834412
    model: gemini-3-flash-preview
    generated_at: '2026-02-20 01:24:51 '
---

## Problem #761: Special Binary String

**Difficulty:** Hard

**Topics:** String, Divide and Conquer, Sorting

## Problem Description

<p><strong>Special binary strings</strong> are binary strings with the following two properties:</p>

<ul>
	<li>The number of <code>0</code>&#39;s is equal to the number of <code>1</code>&#39;s.</li>
	<li>Every prefix of the binary string has at least as many <code>1</code>&#39;s as <code>0</code>&#39;s.</li>
</ul>

<p>You are given a <strong>special binary</strong> string <code>s</code>.</p>

<p>A move consists of choosing two consecutive, non-empty, special substrings of <code>s</code>, and swapping them. Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.</p>

<p>Return <em>the lexicographically largest resulting string possible after applying the mentioned operations on the string</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;11011000&quot;
<strong>Output:</strong> &quot;11100100&quot;
<strong>Explanation:</strong> The strings &quot;10&quot; [occuring at s[1]] and &quot;1100&quot; [at s[3]] are swapped.
This is the lexicographically largest string possible after some number of swaps.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;10&quot;
<strong>Output:</strong> &quot;10&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 50</code></li>
	<li><code>s[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
	<li><code>s</code> is a special binary string.</li>
</ul>


## Hints

1. Draw a line from (x, y) to (x+1, y+1) if we see a "1", else to (x+1, y-1).
A special substring is just a line that starts and ends at the same y-coordinate, and that is the lowest y-coordinate reached.
Call a mountain a special substring with no special prefixes - ie. only at the beginning and end is the lowest y-coordinate reached.
If F is the answer function, and S has mountain decomposition M1,M2,M3,...,Mk,  then the answer is:
reverse_sorted(F(M1), F(M2), ..., F(Mk)).
However, you'll also need to deal with the case that S is a mountain, such as 11011000 -> 11100100.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

A special binary string can be decomposed into a sequence of top-level special components. Each component is a special string that starts with '1', ends with '0', and contains another special string in between. We can think of these components as balanced parentheses, where '1' is '(' and '0' is ')'. To maximize the string lexicographically, we must recursively maximize the inner part of each top-level component and then sort these components in descending order before concatenating them back together.

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
    string makeLargestSpecial(string s) {
        if (s.empty()) return "";
        vector<string> parts;
        int balance = 0, start = 0;
        for (int i = 0; i < s.length(); ++i) {
            balance += (s[i] == '1' ? 1 : -1);
            if (balance == 0) {
                string inner = s.substr(start + 1, i - start - 1);
                parts.push_back("1" + makeLargestSpecial(inner) + "0");
                start = i + 1;
            }
        }
        sort(parts.rbegin(), parts.rend());
        string res = "";
        for (const string& p : parts) res += p;
        return res;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public String makeLargestSpecial(String s) {
        if (s.length() == 0) return "";
        List<String> parts = new ArrayList<>();
        int balance = 0, start = 0;
        for (int i = 0; i < s.length(); i++) {
            balance += (s.charAt(i) == '1' ? 1 : -1);
            if (balance == 0) {
                parts.add("1" + makeLargestSpecial(s.substring(start + 1, i)) + "0");
                start = i + 1;
            }
        }
        Collections.sort(parts, Collections.reverseOrder());
        return String.join("", parts);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def makeLargestSpecial(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ""
        res = []
        balance = 0
        start = 0
        for i, char in enumerate(s):
            balance += 1 if char == '1' else -1
            if balance == 0:
                res.append("1" + self.makeLargestSpecial(s[start + 1:i]) + "0")
                start = i + 1
        res.sort(reverse=True)
        return "".join(res)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if not s: return ""
        parts = []
        balance = 0
        start = 0
        for i, char in enumerate(s):
            balance += 1 if char == '1' else -1
            if balance == 0:
                parts.append("1" + self.makeLargestSpecial(s[start + 1:i]) + "0")
                start = i + 1
        return "".join(sorted(parts, reverse=True))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int compare(const void* a, const void* b) {
    return strcmp(*(const char**)b, *(const char**)a);
}

char* makeLargestSpecial(char* s) {
    int n = strlen(s);
    if (n == 0) return "";

    char** parts = malloc(n * sizeof(char*));
    int partsCount = 0;
    int balance = 0, start = 0;

    for (int i = 0; i < n; i++) {
        balance += (s[i] == '1' ? 1 : -1);
        if (balance == 0) {
            int len = i - start - 1;
            char* sub = malloc(len + 1);
            if (len > 0) strncpy(sub, s + start + 1, len);
            sub[len] = '\0';

            char* inner = makeLargestSpecial(sub);
            int innerLen = strlen(inner);
            parts[partsCount] = malloc(innerLen + 3);
            parts[partsCount][0] = '1';
            strcpy(parts[partsCount] + 1, inner);
            parts[partsCount][innerLen + 1] = '0';
            parts[partsCount][innerLen + 2] = '\0';

            if (len > 0) free(sub);
            partsCount++;
            start = i + 1;
        }
    }

    qsort(parts, partsCount, sizeof(char*), compare);

    char* result = malloc(n + 1);
    result[0] = '\0';
    for (int i = 0; i < partsCount; i++) {
        strcat(result, parts[i]);
        free(parts[i]);
    }
    free(parts);
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public string MakeLargestSpecial(string s) {
        if (string.IsNullOrEmpty(s)) return "";
        List<string> parts = new List<string>();
        int balance = 0, start = 0;
        for (int i = 0; i < s.Length; i++) {
            balance += (s[i] == '1' ? 1 : -1);
            if (balance == 0) {
                parts.Add("1" + MakeLargestSpecial(s.Substring(start + 1, i - start - 1)) + "0");
                start = i + 1;
            }
        }
        parts.Sort((a, b) => b.CompareTo(a));
        return string.Concat(parts);
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
 * @return {string}
 */
var makeLargestSpecial = function(s) {
    if (!s) return "";
    let parts = [];
    let balance = 0;
    let start = 0;
    for (let i = 0; i < s.length; i++) {
        balance += (s[i] === '1' ? 1 : -1);
        if (balance === 0) {
            parts.push("1" + makeLargestSpecial(s.substring(start + 1, i)) + "0");
            start = i + 1;
        }
    }
    parts.sort().reverse();
    return parts.join("");
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function makeLargestSpecial(s: string): string {
    if (s.length === 0) return "";
    let count = 0, i = 0;
    const res: string[] = [];
    for (let j = 0; j < s.length; j++) {
        count += (s[j] === '1' ? 1 : -1);
        if (count === 0) {
            res.push('1' + makeLargestSpecial(s.substring(i + 1, j)) + '0');
            i = j + 1;
        }
    }
    return res.sort((a, b) => (a < b ? 1 : -1)).join('');
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
     * @return String
     */
    function makeLargestSpecial($s) {
        if ($s === "") return "";
        $count = 0;
        $i = 0;
        $res = [];
        $len = strlen($s);
        for ($j = 0; $j < $len; $j++) {
            $count += ($s[$j] === '1' ? 1 : -1);
            if ($count === 0) {
                $res[] = '1' . $this->makeLargestSpecial(substr($s, $i + 1, $j - $i - 1)) . '0';
                $i = $j + 1;
            }
        }
        rsort($res);
        return implode("", $res);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func makeLargestSpecial(_ s: String) -> String {
        if s.isEmpty { return "" }
        var count = 0
        var i = 0
        var res = [String]()
        let chars = Array(s)
        for j in 0..<chars.count {
            count += (chars[j] == "1" ? 1 : -1)
            if count == 0 {
                let startIdx = s.index(s.startIndex, offsetBy: i + 1)
                let endIdx = s.index(s.startIndex, offsetBy: j)
                let sub = String(s[startIdx..<endIdx])
                res.append("1" + makeLargestSpecial(sub) + "0")
                i = j + 1
            }
        }
        res.sort(by: >)
        return res.joined()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun makeLargestSpecial(s: String): String {
        if (s.isEmpty()) return ""
        var count = 0
        var i = 0
        val res = mutableListOf<String>()
        for (j in s.indices) {
            count += if (s[j] == '1') 1 else -1
            if (count == 0) {
                res.add("1" + makeLargestSpecial(s.substring(i + 1, j)) + "0")
                i = j + 1
            }
        }
        res.sortDescending()
        return res.joinToString("")
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  String makeLargestSpecial(String s) {
    if (s.isEmpty) return "";
    int count = 0;
    int i = 0;
    List<String> res = [];
    for (int j = 0; j < s.length; j++) {
      count += (s[j] == '1' ? 1 : -1);
      if (count == 0) {
        res.add("1" + makeLargestSpecial(s.substring(i + 1, j)) + "0");
        i = j + 1;
      }
    }
    res.sort((a, b) => b.compareTo(a));
    return res.join("");
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import (
    "sort"
    "strings"
)

func makeLargestSpecial(s string) string {
    if len(s) == 0 {
        return ""
    }
    count := 0
    i := 0
    var res []string
    for j, char := range s {
        if char == '1' {
            count++
        } else {
            count--
        }
        if count == 0 {
            res = append(res, "1"+makeLargestSpecial(s[i+1:j])+"0")
            i = j + 1
        }
    }
    sort.Slice(res, func(i, j int) bool {
        return res[i] > res[j]
    })
    return strings.Join(res, "")
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @return {String}
def make_largest_special(s)
  return "" if s.empty?
  res = []
  count = 0
  i = 0
  s.chars.each_with_index do |char, j|
    count += (char == '1' ? 1 : -1)
    if count == 0
      res << "1#{make_largest_special(s[i + 1...j])}0"
      i = j + 1
    end
  end
  res.sort.reverse.join
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def makeLargestSpecial(s: String): String = {
        if (s == "") return ""
        val res = scala.collection.mutable.ListBuffer[String]()
        var count = 0
        var i = 0
        for (j <- 0 until s.length) {
            if (s(j) == '1') count += 1 else count -= 1
            if (count == 0) {
                res += "1" + makeLargestSpecial(s.substring(i + 1, j)) + "0"
                i = j + 1
            }
        }
        res.toList.sorted(Ordering.String.reverse).mkString
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn make_largest_special(s: String) -> String {
        if s.is_empty() {
            return "".to_string();
        }
        let mut res = Vec::new();
        let mut count = 0;
        let mut i = 0;
        let chars: Vec<char> = s.chars().collect();
        for (j, &c) in chars.iter().enumerate() {
            if c == '1' {
                count += 1;
            } else {
                count -= 1;
            }
            if count == 0 {
                let inner = chars[i + 1..j].iter().collect::<String>();
                res.push(format!("1{}0", Self::make_largest_special(inner)));
                i = j + 1;
            }
        }
        res.sort_unstable_by(|a, b| b.cmp(a));
        res.concat()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (make-largest-special s)
  (-> string? string?)
  (if (string=? s "")
      ""
      (let loop ([chars (string->list s)]
                 [count 0]
                 [start 0]
                 [current-idx 0]
                 [acc '()])
        (if (null? chars)
            (apply string-append (sort acc string>?))
            (let* ([char (car chars)]
                   [new-count (+ count (if (char=? char #\1) 1 -1))])
              (if (= new-count 0)
                  (let* ([inner (substring s (+ start 1) current-idx)]
                         [processed (string-append "1" (make-largest-special inner) "0")])
                    (loop (cdr chars) 0 (+ current-idx 1) (+ current-idx 1) (cons processed acc)))
                  (loop (cdr chars) new-count start (+ current-idx 1) acc)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec make_largest_special(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
make_largest_special(S) ->
  list_to_binary(do_solve(binary_to_list(S))).

do_solve([]) -> [];
do_solve(S) ->
  Substrings = find_sub(S, 0, [], []),
  Processed = [ [$1 | do_solve(Sub)] ++ [$0] || Sub <- Substrings ],
  Sorted = lists:reverse(lists:sort(Processed)),
  lists:flatten(Sorted).

find_sub([], _, _, Acc) -> lists:reverse(Acc);
find_sub([H|T], Count, CurrentSub, Acc) ->
  NewCount = if H == $1 -> Count + 1; true -> Count - 1 end,
  if
    NewCount == 0 ->
      FullSub = lists:reverse([H|CurrentSub]),
      [_First | Rest] = FullSub,
      InnerPart = lists:sublist(Rest, length(Rest) - 1),
      find_sub(T, 0, [], [InnerPart | Acc]);
    true ->
      find_sub(T, NewCount, [H|CurrentSub], Acc)
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec make_largest_special(s :: String.t) :: String.t
  def make_largest_special(s) do
    if s == "" do
      ""
    else
      {parts, _, _} = s
        |> String.graphemes()
        |> Enum.reduce({[], 0, ""}, fn char, {acc, count, current} ->
          new_count = count + (if char == "1", do: 1, else: -1)
          new_current = current <> char
          if new_count == 0 do
            inner = String.slice(new_current, 1, String.length(new_current) - 2)
            {["1" <> make_largest_special(inner) <> "0" | acc], 0, ""}
          else
            {acc, new_count, new_current}
          end
        end)
      parts
      |> Enum.sort(:desc)
      |> Enum.join("")
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N^2) where N is the length of the string. In the worst case, we scan the string once to find top-level components, and the sorting step takes $O(N^2 \log N)$ if we consider the string lengths. Given $N \le 50$, the recursive depth is at most $N/2$, leading to an efficient solution.
- **Space Complexity:** O(N^2) to store the intermediate substrings created during the recursive process and the recursion stack depth.
