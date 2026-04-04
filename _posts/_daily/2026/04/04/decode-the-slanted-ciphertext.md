---
layout: post
title: "Decode the Slanted Ciphertext"
date: 2026-04-04 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Simulation"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/decode-the-slanted-ciphertext/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    string decodeCiphertext(string encodedText,\
        \ int rows) {\n        if (encodedText.empty()) return \"\";\n        int n\
        \ = encodedText.size();\n        int cols = n / rows;\n        string res =\
        \ \"\";\n        res.reserve(n);\n\n        for (int j = 0; j < cols; ++j) {\n\
        \            for (int i = 0; i < rows && j + i < cols; ++i) {\n            \
        \    res += encodedText[i * cols + (j + i)];\n            }\n        }\n\n \
        \       while (!res.empty() && res.back() == ' ') {\n            res.pop_back();\n\
        \        }\n        return res;\n    }\n};"
      java: "class Solution {\n    public String decodeCiphertext(String encodedText,\
        \ int rows) {\n        if (encodedText.isEmpty()) return \"\";\n        int\
        \ n = encodedText.length();\n        int cols = n / rows;\n        StringBuilder\
        \ res = new StringBuilder();\n\n        for (int j = 0; j < cols; j++) {\n \
        \           for (int i = 0; i < rows && j + i < cols; i++) {\n             \
        \   res.append(encodedText.charAt(i * cols + (j + i)));\n            }\n   \
        \     }\n\n        int len = res.length();\n        while (len > 0 && res.charAt(len\
        \ - 1) == ' ') {\n            len--;\n        }\n        return res.substring(0,\
        \ len);\n    }\n}"
      python: "class Solution(object):\n    def decodeCiphertext(self, encodedText,\
        \ rows):\n        \"\"\"\n        :type encodedText: str\n        :type rows:\
        \ int\n        :rtype: str\n        \"\"\"\n        if not encodedText:\n  \
        \          return \"\"\n        n = len(encodedText)\n        cols = n // rows\n\
        \        res = []\n        for j in xrange(cols):\n            for i in xrange(rows):\n\
        \                if j + i < cols:\n                    res.append(encodedText[i\
        \ * cols + (j + i)])\n                else:\n                    break\n   \
        \     return \"\".join(res).rstrip()"
      python3: "class Solution:\n    def decodeCiphertext(self, encodedText: str, rows:\
        \ int) -> str:\n        if not encodedText:\n            return \"\"\n     \
        \   n = len(encodedText)\n        cols = n // rows\n        res = []\n     \
        \   for j in range(cols):\n            for i in range(rows):\n             \
        \   if j + i < cols:\n                    res.append(encodedText[i * cols +\
        \ (j + i)])\n                else:\n                    break\n        return\
        \ \"\".join(res).rstrip()"
      c: "char* decodeCiphertext(char* encodedText, int rows) {\n    int n = strlen(encodedText);\n\
        \    if (n == 0) {\n        char* empty = (char*)malloc(1);\n        empty[0]\
        \ = '\\0';\n        return empty;\n    }\n    int cols = n / rows;\n    char*\
        \ res = (char*)malloc(n + 1);\n    int ptr = 0;\n    for (int j = 0; j < cols;\
        \ j++) {\n        for (int i = 0; i < rows && j + i < cols; i++) {\n       \
        \     res[ptr++] = encodedText[i * cols + (j + i)];\n        }\n    }\n    res[ptr]\
        \ = '\\0';\n    while (ptr > 0 && res[ptr - 1] == ' ') {\n        res[--ptr]\
        \ = '\\0';\n    }\n    return res;\n}"
      csharp: "using System.Text;\n\npublic class Solution {\n    public string DecodeCiphertext(string\
        \ encodedText, int rows) {\n        int n = encodedText.Length;\n        if\
        \ (n == 0) return \"\";\n        int cols = n / rows;\n        StringBuilder\
        \ sb = new StringBuilder(n);\n        for (int k = 0; k < cols; k++) {\n   \
        \         for (int r = 0; r < rows; r++) {\n                int c = k + r;\n\
        \                if (c < cols) {\n                    sb.Append(encodedText[r\
        \ * cols + c]);\n                } else {\n                    break;\n    \
        \            }\n            }\n        }\n        return sb.ToString().TrimEnd();\n\
        \    }\n}"
      javascript: "/**\n * @param {string} encodedText\n * @param {number} rows\n *\
        \ @return {string}\n */\nvar decodeCiphertext = function(encodedText, rows)\
        \ {\n    const n = encodedText.length;\n    if (n === 0) return \"\";\n    const\
        \ cols = n / rows;\n    let res = [];\n    for (let k = 0; k < cols; k++) {\n\
        \        for (let r = 0; r < rows; r++) {\n            const c = k + r;\n  \
        \          if (c < cols) {\n                res.push(encodedText[r * cols +\
        \ c]);\n            } else {\n                break;\n            }\n      \
        \  }\n    }\n    return res.join('').trimEnd();\n};"
      typescript: "function decodeCiphertext(encodedText: string, rows: number): string\
        \ {\n    const n = encodedText.length;\n    if (n === 0) return \"\";\n    const\
        \ cols = n / rows;\n    let res: string[] = [];\n    for (let k = 0; k < cols;\
        \ k++) {\n        for (let r = 0; r < rows; r++) {\n            const c = k\
        \ + r;\n            if (c < cols) {\n                res.push(encodedText[r\
        \ * cols + c]);\n            } else {\n                break;\n            }\n\
        \        }\n    }\n    return res.join('').trimEnd();\n};"
      php: "class Solution {\n\n    /**\n     * @param String $encodedText\n     * @param\
        \ Integer $rows\n     * @return String\n     */\n    function decodeCiphertext($encodedText,\
        \ $rows) {\n        $n = strlen($encodedText);\n        if ($n === 0) return\
        \ \"\";\n        $cols = (int)($n / $rows);\n        $res = [];\n        for\
        \ ($k = 0; $k < $cols; $k++) {\n            for ($r = 0; $r < $rows; $r++) {\n\
        \                $c = $k + $r;\n                if ($c < $cols) {\n        \
        \            $res[] = $encodedText[$r * $cols + $c];\n                } else\
        \ {\n                    break;\n                }\n            }\n        }\n\
        \        return rtrim(implode('', $res));\n    }\n}"
      swift: "class Solution {\n    func decodeCiphertext(_ encodedText: String, _ rows:\
        \ Int) -> String {\n        let n = encodedText.count\n        if n == 0 { return\
        \ \"\" }\n        let cols = n / rows\n        let s = Array(encodedText)\n\
        \        var res = \"\"\n        res.reserveCapacity(n)\n        for k in 0..<cols\
        \ {\n            for r in 0..<rows {\n                let c = k + r\n      \
        \          if c < cols {\n                    res.append(s[r * cols + c])\n\
        \                } else {\n                    break\n                }\n  \
        \          }\n        }\n        while let last = res.last, last == \" \" {\n\
        \            res.removeLast()\n        }\n        return res\n    }\n}"
      kotlin: "class Solution {\n    fun decodeCiphertext(encodedText: String, rows:\
        \ Int): String {\n        if (encodedText.isEmpty()) return \"\"\n        val\
        \ n = encodedText.length\n        val cols = n / rows\n        val sb = StringBuilder()\n\
        \        for (c0 in 0 until cols) {\n            var r = 0\n            while\
        \ (r < rows && c0 + r < cols) {\n                sb.append(encodedText[r * cols\
        \ + (c0 + r)])\n                r++\n            }\n        }\n        return\
        \ sb.toString().trimEnd()\n    }\n}"
      dart: "class Solution {\n  String decodeCiphertext(String encodedText, int rows)\
        \ {\n    if (encodedText.isEmpty) return \"\";\n    int n = encodedText.length;\n\
        \    int cols = n ~/ rows;\n    StringBuffer sb = StringBuffer();\n    for (int\
        \ c0 = 0; c0 < cols; c0++) {\n      for (int r = 0; r < rows && c0 + r < cols;\
        \ r++) {\n        sb.write(encodedText[r * cols + (c0 + r)]);\n      }\n   \
        \ }\n    return sb.toString().trimRight();\n  }\n}"
      go: "func decodeCiphertext(encodedText string, rows int) string {\n    if len(encodedText)\
        \ == 0 {\n        return \"\"\n    }\n    n := len(encodedText)\n    cols :=\
        \ n / rows\n    res := make([]byte, 0, n)\n    for c0 := 0; c0 < cols; c0++\
        \ {\n        for r := 0; r < rows && c0+r < cols; r++ {\n            res = append(res,\
        \ encodedText[r*cols+(c0+r)])\n        }\n    }\n    i := len(res) - 1\n   \
        \ for i >= 0 && res[i] == ' ' {\n        i--\n    }\n    return string(res[:i+1])\n\
        }"
      ruby: "# @param {String} encoded_text\n# @param {Integer} rows\n# @return {String}\n\
        def decode_ciphertext(encoded_text, rows)\n  return \"\" if encoded_text.empty?\n\
        \  n = encoded_text.length\n  cols = n / rows\n  res = \"\"\n  (0...cols).each\
        \ do |c0|\n    (0...rows).each do |r|\n      c = c0 + r\n      break if c >=\
        \ cols\n      res << encoded_text[r * cols + c]\n    end\n  end\n  res.rstrip\n\
        end"
      scala: "object Solution {\n    def decodeCiphertext(encodedText: String, rows:\
        \ Int): String = {\n        if (encodedText.isEmpty) return \"\"\n        val\
        \ n = encodedText.length\n        val cols = n / rows\n        val sb = new\
        \ StringBuilder()\n        for (c0 <- 0 until cols) {\n            var r = 0\n\
        \            while (r < rows && c0 + r < cols) {\n                sb.append(encodedText(r\
        \ * cols + (c0 + r)))\n                r += 1\n            }\n        }\n  \
        \      val res = sb.toString()\n        var i = res.length - 1\n        while\
        \ (i >= 0 && res(i) == ' ') {\n            i -= 1\n        }\n        res.substring(0,\
        \ i + 1)\n    }\n}"
      rust: "impl Solution {\n    pub fn decode_ciphertext(encoded_text: String, rows:\
        \ i32) -> String {\n        let n = encoded_text.len();\n        if n == 0 {\n\
        \            return \"\".to_string();\n        }\n        let rows = rows as\
        \ usize;\n        let cols = n / rows;\n        let bytes = encoded_text.as_bytes();\n\
        \        let mut res = Vec::with_capacity(n);\n\n        for c in 0..cols {\n\
        \            for r in 0..rows {\n                let col_idx = c + r;\n    \
        \            if col_idx < cols {\n                    res.push(bytes[r * cols\
        \ + col_idx]);\n                } else {\n                    break;\n     \
        \           }\n            }\n        }\n\n        let decoded = String::from_utf8(res).unwrap();\n\
        \        decoded.trim_end_matches(' ').to_string()\n    }\n}"
      racket: "(require racket/string)\n\n(define/contract (decode-ciphertext encodedText\
        \ rows)\n  (-> string? exact-integer? string?)\n  (let ([len (string-length\
        \ encodedText)])\n    (if (= len 0)\n        \"\"\n        (let* ([cols (quotient\
        \ len rows)]\n               [res (for*/list ([c (in-range cols)]\n        \
        \                        [r (in-range rows)]\n                             \
        \   #:when (< (+ c r) cols))\n                      (string-ref encodedText\
        \ (+ (* r cols) (+ c r))))])\n          (string-trim (list->string res) \" \"\
        \ #:left? #f)))))"
      erlang: "-spec decode_ciphertext(EncodedText :: unicode:unicode_binary(), Rows\
        \ :: integer()) -> unicode:unicode_binary().\ndecode_ciphertext(EncodedText,\
        \ Rows) ->\n    Len = byte_size(EncodedText),\n    if\n        Len == 0 -> <<>>;\n\
        \        true ->\n            Cols = Len div Rows,\n            Decoded = [binary:at(EncodedText,\
        \ R * Cols + (C + R)) ||\n                       C <- lists:seq(0, Cols - 1),\n\
        \                       R <- lists:seq(0, Rows - 1),\n                     \
        \  C + R < Cols],\n            unicode:characters_to_binary(string:trim(Decoded,\
        \ trailing, \" \"))\n    end."
      elixir: "defmodule Solution do\n  @spec decode_ciphertext(encoded_text :: String.t,\
        \ rows :: integer) :: String.t\n  def decode_ciphertext(encoded_text, rows)\
        \ do\n    len = byte_size(encoded_text)\n    if len == 0 do\n      \"\"\n  \
        \  else\n      cols = div(len, rows)\n      decoded = for c <- 0..(cols - 1),\n\
        \                    r <- 0..(rows - 1),\n                    c + r < cols,\n\
        \                    do: :binary.at(encoded_text, r * cols + (c + r))\n\n  \
        \    decoded\n      |> List.to_string()\n      |> String.trim_trailing(\" \"\
        )\n    end\n  end\nend"
    approach: The core of the problem lies in reversing a slanted transposition cipher.
      The encoded string is effectively a row-major representation of a matrix with
      a fixed number of rows. To reconstruct the original text, we first determine the
      number of columns by dividing the total length of the encoded string by the given
      number of rows. The original text was placed diagonally (slantwise), meaning characters
      were inserted in diagonals starting from each column of the first row and moving
      down-right. Thus, we can decode it by traversing these same diagonals.
    time_complexity: O(N) where N is the length of the encoded text. We iterate through
      the matrix diagonals, visiting each character at most once, and the final step
      of trimming trailing spaces also takes linear time relative to the length of the
      reconstructed string.
    space_complexity: O(N) to store the result. We allocate a buffer (or string builder)
      to hold the decoded characters, which in the worst case is proportional to the
      length of the input encoded text.
    elapsed_time: 698.8746273517609
    model: gemini-3-flash-preview
    generated_at: '2026-04-04 01:38:30 '
---

## Problem #2075: Decode the Slanted Ciphertext

**Difficulty:** Medium

**Topics:** String, Simulation

## Problem Description

<p>A string <code>originalText</code> is encoded using a <strong>slanted transposition cipher</strong> to a string <code>encodedText</code> with the help of a matrix having a <strong>fixed number of rows</strong> <code>rows</code>.</p>

<p><code>originalText</code> is placed first in a top-left to bottom-right manner.</p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/07/exa11.png" style="width: 300px; height: 185px;" />
<p>The blue cells are filled first, followed by the red cells, then the yellow cells, and so on, until we reach the end of <code>originalText</code>. The arrow indicates the order in which the cells are filled. All empty cells are filled with <code>&#39; &#39;</code>. The number of columns is chosen such that the rightmost column will <strong>not be empty</strong> after filling in <code>originalText</code>.</p>

<p><code>encodedText</code> is then formed by appending all characters of the matrix in a row-wise fashion.</p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/07/exa12.png" style="width: 300px; height: 200px;" />
<p>The characters in the blue cells are appended first to <code>encodedText</code>, then the red cells, and so on, and finally the yellow cells. The arrow indicates the order in which the cells are accessed.</p>

<p>For example, if <code>originalText = &quot;cipher&quot;</code> and <code>rows = 3</code>, then we encode it in the following manner:</p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/10/25/desc2.png" style="width: 281px; height: 211px;" />
<p>The blue arrows depict how <code>originalText</code> is placed in the matrix, and the red arrows denote the order in which <code>encodedText</code> is formed. In the above example, <code>encodedText = &quot;ch ie pr&quot;</code>.</p>

<p>Given the encoded string <code>encodedText</code> and number of rows <code>rows</code>, return <em>the original string</em> <code>originalText</code>.</p>

<p><strong>Note:</strong> <code>originalText</code> <strong>does not</strong> have any trailing spaces <code>&#39; &#39;</code>. The test cases are generated such that there is only one possible <code>originalText</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> encodedText = &quot;ch   ie   pr&quot;, rows = 3
<strong>Output:</strong> &quot;cipher&quot;
<strong>Explanation:</strong> This is the same example described in the problem description.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/10/26/exam1.png" style="width: 250px; height: 168px;" />
<pre>
<strong>Input:</strong> encodedText = &quot;iveo    eed   l te   olc&quot;, rows = 4
<strong>Output:</strong> &quot;i love leetcode&quot;
<strong>Explanation:</strong> The figure above denotes the matrix that was used to encode originalText. 
The blue arrows show how we can find originalText from encodedText.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/10/26/eg2.png" style="width: 300px; height: 51px;" />
<pre>
<strong>Input:</strong> encodedText = &quot;coding&quot;, rows = 1
<strong>Output:</strong> &quot;coding&quot;
<strong>Explanation:</strong> Since there is only 1 row, both originalText and encodedText are the same.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= encodedText.length &lt;= 10<sup>6</sup></code></li>
	<li><code>encodedText</code> consists of lowercase English letters and <code>&#39; &#39;</code> only.</li>
	<li><code>encodedText</code> is a valid encoding of some <code>originalText</code> that <strong>does not</strong> have trailing spaces.</li>
	<li><code>1 &lt;= rows &lt;= 1000</code></li>
	<li>The testcases are generated such that there is <strong>only one</strong> possible <code>originalText</code>.</li>
</ul>


## Hints

1. How can you use rows and encodedText to find the number of columns of the matrix?

2. Once you have the number of rows and columns, you can create the matrix and place encodedText in it. How should you place it in the matrix?

3. How should you traverse the matrix to "decode" originalText?

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The core of the problem lies in reversing a slanted transposition cipher. The encoded string is effectively a row-major representation of a matrix with a fixed number of rows. To reconstruct the original text, we first determine the number of columns by dividing the total length of the encoded string by the given number of rows. The original text was placed diagonally (slantwise), meaning characters were inserted in diagonals starting from each column of the first row and moving down-right. Thus, we can decode it by traversing these same diagonals.

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
    string decodeCiphertext(string encodedText, int rows) {
        if (encodedText.empty()) return "";
        int n = encodedText.size();
        int cols = n / rows;
        string res = "";
        res.reserve(n);

        for (int j = 0; j < cols; ++j) {
            for (int i = 0; i < rows && j + i < cols; ++i) {
                res += encodedText[i * cols + (j + i)];
            }
        }

        while (!res.empty() && res.back() == ' ') {
            res.pop_back();
        }
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
    public String decodeCiphertext(String encodedText, int rows) {
        if (encodedText.isEmpty()) return "";
        int n = encodedText.length();
        int cols = n / rows;
        StringBuilder res = new StringBuilder();

        for (int j = 0; j < cols; j++) {
            for (int i = 0; i < rows && j + i < cols; i++) {
                res.append(encodedText.charAt(i * cols + (j + i)));
            }
        }

        int len = res.length();
        while (len > 0 && res.charAt(len - 1) == ' ') {
            len--;
        }
        return res.substring(0, len);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        """
        :type encodedText: str
        :type rows: int
        :rtype: str
        """
        if not encodedText:
            return ""
        n = len(encodedText)
        cols = n // rows
        res = []
        for j in xrange(cols):
            for i in xrange(rows):
                if j + i < cols:
                    res.append(encodedText[i * cols + (j + i)])
                else:
                    break
        return "".join(res).rstrip()
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if not encodedText:
            return ""
        n = len(encodedText)
        cols = n // rows
        res = []
        for j in range(cols):
            for i in range(rows):
                if j + i < cols:
                    res.append(encodedText[i * cols + (j + i)])
                else:
                    break
        return "".join(res).rstrip()
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
char* decodeCiphertext(char* encodedText, int rows) {
    int n = strlen(encodedText);
    if (n == 0) {
        char* empty = (char*)malloc(1);
        empty[0] = '\0';
        return empty;
    }
    int cols = n / rows;
    char* res = (char*)malloc(n + 1);
    int ptr = 0;
    for (int j = 0; j < cols; j++) {
        for (int i = 0; i < rows && j + i < cols; i++) {
            res[ptr++] = encodedText[i * cols + (j + i)];
        }
    }
    res[ptr] = '\0';
    while (ptr > 0 && res[ptr - 1] == ' ') {
        res[--ptr] = '\0';
    }
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System.Text;

public class Solution {
    public string DecodeCiphertext(string encodedText, int rows) {
        int n = encodedText.Length;
        if (n == 0) return "";
        int cols = n / rows;
        StringBuilder sb = new StringBuilder(n);
        for (int k = 0; k < cols; k++) {
            for (int r = 0; r < rows; r++) {
                int c = k + r;
                if (c < cols) {
                    sb.Append(encodedText[r * cols + c]);
                } else {
                    break;
                }
            }
        }
        return sb.ToString().TrimEnd();
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} encodedText
 * @param {number} rows
 * @return {string}
 */
var decodeCiphertext = function(encodedText, rows) {
    const n = encodedText.length;
    if (n === 0) return "";
    const cols = n / rows;
    let res = [];
    for (let k = 0; k < cols; k++) {
        for (let r = 0; r < rows; r++) {
            const c = k + r;
            if (c < cols) {
                res.push(encodedText[r * cols + c]);
            } else {
                break;
            }
        }
    }
    return res.join('').trimEnd();
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function decodeCiphertext(encodedText: string, rows: number): string {
    const n = encodedText.length;
    if (n === 0) return "";
    const cols = n / rows;
    let res: string[] = [];
    for (let k = 0; k < cols; k++) {
        for (let r = 0; r < rows; r++) {
            const c = k + r;
            if (c < cols) {
                res.push(encodedText[r * cols + c]);
            } else {
                break;
            }
        }
    }
    return res.join('').trimEnd();
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String $encodedText
     * @param Integer $rows
     * @return String
     */
    function decodeCiphertext($encodedText, $rows) {
        $n = strlen($encodedText);
        if ($n === 0) return "";
        $cols = (int)($n / $rows);
        $res = [];
        for ($k = 0; $k < $cols; $k++) {
            for ($r = 0; $r < $rows; $r++) {
                $c = $k + $r;
                if ($c < $cols) {
                    $res[] = $encodedText[$r * $cols + $c];
                } else {
                    break;
                }
            }
        }
        return rtrim(implode('', $res));
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func decodeCiphertext(_ encodedText: String, _ rows: Int) -> String {
        let n = encodedText.count
        if n == 0 { return "" }
        let cols = n / rows
        let s = Array(encodedText)
        var res = ""
        res.reserveCapacity(n)
        for k in 0..<cols {
            for r in 0..<rows {
                let c = k + r
                if c < cols {
                    res.append(s[r * cols + c])
                } else {
                    break
                }
            }
        }
        while let last = res.last, last == " " {
            res.removeLast()
        }
        return res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun decodeCiphertext(encodedText: String, rows: Int): String {
        if (encodedText.isEmpty()) return ""
        val n = encodedText.length
        val cols = n / rows
        val sb = StringBuilder()
        for (c0 in 0 until cols) {
            var r = 0
            while (r < rows && c0 + r < cols) {
                sb.append(encodedText[r * cols + (c0 + r)])
                r++
            }
        }
        return sb.toString().trimEnd()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  String decodeCiphertext(String encodedText, int rows) {
    if (encodedText.isEmpty) return "";
    int n = encodedText.length;
    int cols = n ~/ rows;
    StringBuffer sb = StringBuffer();
    for (int c0 = 0; c0 < cols; c0++) {
      for (int r = 0; r < rows && c0 + r < cols; r++) {
        sb.write(encodedText[r * cols + (c0 + r)]);
      }
    }
    return sb.toString().trimRight();
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func decodeCiphertext(encodedText string, rows int) string {
    if len(encodedText) == 0 {
        return ""
    }
    n := len(encodedText)
    cols := n / rows
    res := make([]byte, 0, n)
    for c0 := 0; c0 < cols; c0++ {
        for r := 0; r < rows && c0+r < cols; r++ {
            res = append(res, encodedText[r*cols+(c0+r)])
        }
    }
    i := len(res) - 1
    for i >= 0 && res[i] == ' ' {
        i--
    }
    return string(res[:i+1])
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} encoded_text
# @param {Integer} rows
# @return {String}
def decode_ciphertext(encoded_text, rows)
  return "" if encoded_text.empty?
  n = encoded_text.length
  cols = n / rows
  res = ""
  (0...cols).each do |c0|
    (0...rows).each do |r|
      c = c0 + r
      break if c >= cols
      res << encoded_text[r * cols + c]
    end
  end
  res.rstrip
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def decodeCiphertext(encodedText: String, rows: Int): String = {
        if (encodedText.isEmpty) return ""
        val n = encodedText.length
        val cols = n / rows
        val sb = new StringBuilder()
        for (c0 <- 0 until cols) {
            var r = 0
            while (r < rows && c0 + r < cols) {
                sb.append(encodedText(r * cols + (c0 + r)))
                r += 1
            }
        }
        val res = sb.toString()
        var i = res.length - 1
        while (i >= 0 && res(i) == ' ') {
            i -= 1
        }
        res.substring(0, i + 1)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn decode_ciphertext(encoded_text: String, rows: i32) -> String {
        let n = encoded_text.len();
        if n == 0 {
            return "".to_string();
        }
        let rows = rows as usize;
        let cols = n / rows;
        let bytes = encoded_text.as_bytes();
        let mut res = Vec::with_capacity(n);

        for c in 0..cols {
            for r in 0..rows {
                let col_idx = c + r;
                if col_idx < cols {
                    res.push(bytes[r * cols + col_idx]);
                } else {
                    break;
                }
            }
        }

        let decoded = String::from_utf8(res).unwrap();
        decoded.trim_end_matches(' ').to_string()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(require racket/string)

(define/contract (decode-ciphertext encodedText rows)
  (-> string? exact-integer? string?)
  (let ([len (string-length encodedText)])
    (if (= len 0)
        ""
        (let* ([cols (quotient len rows)]
               [res (for*/list ([c (in-range cols)]
                                [r (in-range rows)]
                                #:when (< (+ c r) cols))
                      (string-ref encodedText (+ (* r cols) (+ c r))))])
          (string-trim (list->string res) " " #:left? #f)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec decode_ciphertext(EncodedText :: unicode:unicode_binary(), Rows :: integer()) -> unicode:unicode_binary().
decode_ciphertext(EncodedText, Rows) ->
    Len = byte_size(EncodedText),
    if
        Len == 0 -> <<>>;
        true ->
            Cols = Len div Rows,
            Decoded = [binary:at(EncodedText, R * Cols + (C + R)) ||
                       C <- lists:seq(0, Cols - 1),
                       R <- lists:seq(0, Rows - 1),
                       C + R < Cols],
            unicode:characters_to_binary(string:trim(Decoded, trailing, " "))
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec decode_ciphertext(encoded_text :: String.t, rows :: integer) :: String.t
  def decode_ciphertext(encoded_text, rows) do
    len = byte_size(encoded_text)
    if len == 0 do
      ""
    else
      cols = div(len, rows)
      decoded = for c <- 0..(cols - 1),
                    r <- 0..(rows - 1),
                    c + r < cols,
                    do: :binary.at(encoded_text, r * cols + (c + r))

      decoded
      |> List.to_string()
      |> String.trim_trailing(" ")
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) where N is the length of the encoded text. We iterate through the matrix diagonals, visiting each character at most once, and the final step of trimming trailing spaces also takes linear time relative to the length of the reconstructed string.
- **Space Complexity:** O(N) to store the result. We allocate a buffer (or string builder) to hold the decoded characters, which in the worst case is proportional to the length of the input encoded text.
