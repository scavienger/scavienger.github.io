---
layout: post
title: "Add Binary"
date: 2026-02-15 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Math", "String", "Bit Manipulation", "Simulation"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/add-binary/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    string addBinary(string a, string b) {\n\
        \        string result = \"\";\n        int i = (int)a.length() - 1, j = (int)b.length()\
        \ - 1, carry = 0;\n        while (i >= 0 || j >= 0 || carry) {\n           \
        \ int sum = carry + (i >= 0 ? a[i--] - '0' : 0) + (j >= 0 ? b[j--] - '0' : 0);\n\
        \            result.push_back((sum % 2) + '0');\n            carry = sum / 2;\n\
        \        }\n        reverse(result.begin(), result.end());\n        return result;\n\
        \    }\n};"
      java: "class Solution {\n    public String addBinary(String a, String b) {\n \
        \       StringBuilder sb = new StringBuilder();\n        int i = a.length()\
        \ - 1, j = b.length() - 1, carry = 0;\n        while (i >= 0 || j >= 0 || carry\
        \ != 0) {\n            int sum = carry + (i >= 0 ? a.charAt(i--) - '0' : 0)\
        \ + (j >= 0 ? b.charAt(j--) - '0' : 0);\n            sb.append(sum % 2);\n \
        \           carry = sum / 2;\n        }\n        return sb.reverse().toString();\n\
        \    }\n}"
      python: "class Solution(object):\n    def addBinary(self, a, b):\n        \"\"\
        \"\n        :type a: str\n        :type b: str\n        :rtype: str\n      \
        \  \"\"\"\n        res = []\n        i, j, carry = len(a) - 1, len(b) - 1, 0\n\
        \        while i >= 0 or j >= 0 or carry:\n            total = carry\n     \
        \       if i >= 0:\n                total += ord(a[i]) - ord('0')\n        \
        \        i -= 1\n            if j >= 0:\n                total += ord(b[j])\
        \ - ord('0')\n                j -= 1\n            res.append(str(total % 2))\n\
        \            carry = total // 2\n        return \"\".join(res[::-1])"
      python3: "class Solution:\n    def addBinary(self, a: str, b: str) -> str:\n \
        \       res = []\n        i, j, carry = len(a) - 1, len(b) - 1, 0\n        while\
        \ i >= 0 or j >= 0 or carry:\n            total = carry\n            if i >=\
        \ 0:\n                total += ord(a[i]) - ord('0')\n                i -= 1\n\
        \            if j >= 0:\n                total += ord(b[j]) - ord('0')\n   \
        \             j -= 1\n            res.append(str(total % 2))\n            carry\
        \ = total // 2\n        return \"\".join(res[::-1])"
      c: "char* addBinary(char* a, char* b) {\n    int i = (int)strlen(a) - 1;\n   \
        \ int j = (int)strlen(b) - 1;\n    int max_len = (i > j ? i : j) + 1;\n    char*\
        \ res = (char*)malloc(max_len + 2);\n    res[max_len + 1] = '\\0';\n    int\
        \ carry = 0, k = max_len;\n    while (i >= 0 || j >= 0 || carry) {\n       \
        \ int sum = carry + (i >= 0 ? a[i--] - '0' : 0) + (j >= 0 ? b[j--] - '0' : 0);\n\
        \        res[k--] = (sum % 2) + '0';\n        carry = sum / 2;\n    }\n    if\
        \ (k >= 0) {\n        memmove(res, res + k + 1, max_len - k + 1);\n    }\n \
        \   return res;\n}"
      csharp: "public class Solution {\n    public string AddBinary(string a, string\
        \ b) {\n        StringBuilder sb = new StringBuilder();\n        int i = a.Length\
        \ - 1, j = b.Length - 1, carry = 0;\n        while (i >= 0 || j >= 0 || carry\
        \ > 0) {\n            int sum = carry + (i >= 0 ? a[i--] - '0' : 0) + (j >=\
        \ 0 ? b[j--] - '0' : 0);\n            sb.Append(sum % 2);\n            carry\
        \ = sum / 2;\n        }\n        char[] charArray = sb.ToString().ToCharArray();\n\
        \        Array.Reverse(charArray);\n        return new string(charArray);\n\
        \    }\n}"
      javascript: "/**\n * @param {string} a\n * @param {string} b\n * @return {string}\n\
        \ */\nvar addBinary = function(a, b) {\n    let i = a.length - 1, j = b.length\
        \ - 1, carry = 0, res = [];\n    while (i >= 0 || j >= 0 || carry) {\n     \
        \   let sum = carry + (i >= 0 ? a[i--] - '0' : 0) + (j >= 0 ? b[j--] - '0' :\
        \ 0);\n        res.push(sum % 2);\n        carry = Math.floor(sum / 2);\n  \
        \  }\n    return res.reverse().join('');\n};"
      typescript: "function addBinary(a: string, b: string): string {\n    let res:\
        \ number[] = [];\n    let i = a.length - 1, j = b.length - 1, carry = 0;\n \
        \   while (i >= 0 || j >= 0 || carry > 0) {\n        let sum = carry;\n    \
        \    if (i >= 0) sum += a[i--] === '1' ? 1 : 0;\n        if (j >= 0) sum +=\
        \ b[j--] === '1' ? 1 : 0;\n        res.push(sum % 2);\n        carry = Math.floor(sum\
        \ / 2);\n    }\n    return res.reverse().join(\"\");\n};"
      php: "class Solution {\n\n    /**\n     * @param String $a\n     * @param String\
        \ $b\n     * @return String\n     */\n    function addBinary($a, $b) {\n   \
        \     $res = \"\";\n        $i = strlen($a) - 1;\n        $j = strlen($b) -\
        \ 1;\n        $carry = 0;\n        while ($i >= 0 || $j >= 0 || $carry > 0)\
        \ {\n            $sum = $carry;\n            if ($i >= 0) $sum += ($a[$i--]\
        \ === '1' ? 1 : 0);\n            if ($j >= 0) $sum += ($b[$j--] === '1' ? 1\
        \ : 0);\n            $res .= ($sum % 2);\n            $carry = (int)($sum /\
        \ 2);\n        }\n        return strrev($res);\n    }\n}"
      swift: "class Solution {\n    func addBinary(_ a: String, _ b: String) -> String\
        \ {\n        var res = \"\"\n        let aArr = Array(a), bArr = Array(b)\n\
        \        var i = aArr.count - 1, j = bArr.count - 1, carry = 0\n        while\
        \ i >= 0 || j >= 0 || carry > 0 {\n            var sum = carry\n           \
        \ if i >= 0 {\n                sum += aArr[i] == \"1\" ? 1 : 0\n           \
        \     i -= 1\n            }\n            if j >= 0 {\n                sum +=\
        \ bArr[j] == \"1\" ? 1 : 0\n                j -= 1\n            }\n        \
        \    res += String(sum % 2)\n            carry = sum / 2\n        }\n      \
        \  return String(res.reversed())\n    }\n}"
      kotlin: "class Solution {\n    fun addBinary(a: String, b: String): String {\n\
        \        val res = StringBuilder()\n        var i = a.length - 1\n        var\
        \ j = b.length - 1\n        var carry = 0\n        while (i >= 0 || j >= 0 ||\
        \ carry > 0) {\n            var sum = carry\n            if (i >= 0) sum +=\
        \ if (a[i--] == '1') 1 else 0\n            if (j >= 0) sum += if (b[j--] ==\
        \ '1') 1 else 0\n            res.append(sum % 2)\n            carry = sum /\
        \ 2\n        }\n        return res.reverse().toString()\n    }\n}"
      dart: "class Solution {\n  String addBinary(String a, String b) {\n    StringBuffer\
        \ res = StringBuffer();\n    int i = a.length - 1;\n    int j = b.length - 1;\n\
        \    int carry = 0;\n    while (i >= 0 || j >= 0 || carry > 0) {\n      int\
        \ sum = carry;\n      if (i >= 0) sum += (a[i--] == '1' ? 1 : 0);\n      if\
        \ (j >= 0) sum += (b[j--] == '1' ? 1 : 0);\n      res.write(sum % 2);\n    \
        \  carry = sum ~/ 2;\n    }\n    return res.toString().split('').reversed.join('');\n\
        \  }\n}"
      go: "func addBinary(a string, b string) string {\n    i, j := len(a)-1, len(b)-1\n\
        \    carry := 0\n    var res []byte\n    for i >= 0 || j >= 0 || carry > 0 {\n\
        \        sum := carry\n        if i >= 0 {\n            sum += int(a[i] - '0')\n\
        \            i--\n        }\n        if j >= 0 {\n            sum += int(b[j]\
        \ - '0')\n            j--\n        }\n        res = append(res, byte(sum%2 +\
        \ '0'))\n        carry = sum / 2\n    }\n    for k, l := 0, len(res)-1; k <\
        \ l; k, l = k+1, l-1 {\n        res[k], res[l] = res[l], res[k]\n    }\n   \
        \ return string(res)\n}"
      ruby: "# @param {String} a\n# @param {String} b\n# @return {String}\ndef add_binary(a,\
        \ b)\n  (a.to_i(2) + b.to_i(2)).to_s(2)\nend"
      scala: "object Solution {\n    def addBinary(a: String, b: String): String = {\n\
        \        (BigInt(a, 2) + BigInt(b, 2)).toString(2)\n    }\n}"
      rust: "impl Solution {\n    pub fn add_binary(a: String, b: String) -> String\
        \ {\n        let mut res = String::new();\n        let mut i = a.len() as i32\
        \ - 1;\n        let mut j = b.len() as i32 - 1;\n        let mut carry = 0;\n\
        \        let a_bytes = a.as_bytes();\n        let b_bytes = b.as_bytes();\n\
        \        while i >= 0 || j >= 0 || carry != 0 {\n            let mut sum = carry;\n\
        \            if i >= 0 {\n                sum += (a_bytes[i as usize] - b'0')\
        \ as i32;\n                i -= 1;\n            }\n            if j >= 0 {\n\
        \                sum += (b_bytes[j as usize] - b'0') as i32;\n             \
        \   j -= 1;\n            }\n            res.push(((sum % 2) as u8 + b'0') as\
        \ char);\n            carry = sum / 2;\n        }\n        res.chars().rev().collect()\n\
        \    }\n}"
      racket: "(define/contract (add-binary a b)\n  (-> string? string? string?)\n \
        \ (number->string (+ (string->number a 2) (string->number b 2)) 2))"
      erlang: "-spec add_binary(A :: unicode:unicode_binary(), B :: unicode:unicode_binary())\
        \ -> unicode:unicode_binary().\nadd_binary(A, B) ->\n  integer_to_binary(binary_to_integer(A,\
        \ 2) + binary_to_integer(B, 2), 2)."
      elixir: "defmodule Solution do\n  @spec add_binary(a :: String.t, b :: String.t)\
        \ :: String.t\n  def add_binary(a, b) do\n    Integer.to_string(String.to_integer(a,\
        \ 2) + String.to_integer(b, 2), 2)\n  end\nend"
    approach: 'The algorithm uses a two-pointer approach starting from the end of both
      binary strings to simulate column-wise addition from the least significant bit
      to the most significant bit. A carry variable is maintained to handle sums that
      exceed the binary base of 2. In each iteration, we extract the numeric value of
      the current bits, add them along with any existing carry, and determine the resulting
      bit using the modulo operator. The carry is then updated for the next bit position
      using integer division.


      The resulting bits are collected in reverse order (from smallest to largest significance),
      so the final collection must be reversed to produce the correct binary string.
      This iterative simulation avoids potential overflow errors that would occur if
      the binary strings were converted to fixed-size integer types before performing
      the addition.'
    time_complexity: O(max(N, M)) where N and M are the lengths of the input strings.
      Each bit is processed exactly once in a single pass.
    space_complexity: O(max(N, M)) because the output string requires space proportional
      to the length of the larger input string plus at most one potential carry bit.
    elapsed_time: 261.075133562088
    model: gemini-3-flash-preview
    generated_at: '2026-02-15 01:33:22 '
---

## Problem #67: Add Binary

**Difficulty:** Easy

**Topics:** Math, String, Bit Manipulation, Simulation

## Problem Description

<p>Given two binary strings <code>a</code> and <code>b</code>, return <em>their sum as a binary string</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> a = "11", b = "1"
<strong>Output:</strong> "100"
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> a = "1010", b = "1011"
<strong>Output:</strong> "10101"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= a.length, b.length &lt;= 10<sup>4</sup></code></li>
	<li><code>a</code> and <code>b</code> consist&nbsp;only of <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code> characters.</li>
	<li>Each string does not contain leading zeros except for the zero itself.</li>
</ul>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm uses a two-pointer approach starting from the end of both binary strings to simulate column-wise addition from the least significant bit to the most significant bit. A carry variable is maintained to handle sums that exceed the binary base of 2. In each iteration, we extract the numeric value of the current bits, add them along with any existing carry, and determine the resulting bit using the modulo operator. The carry is then updated for the next bit position using integer division.

The resulting bits are collected in reverse order (from smallest to largest significance), so the final collection must be reversed to produce the correct binary string. This iterative simulation avoids potential overflow errors that would occur if the binary strings were converted to fixed-size integer types before performing the addition.

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
    string addBinary(string a, string b) {
        string result = "";
        int i = (int)a.length() - 1, j = (int)b.length() - 1, carry = 0;
        while (i >= 0 || j >= 0 || carry) {
            int sum = carry + (i >= 0 ? a[i--] - '0' : 0) + (j >= 0 ? b[j--] - '0' : 0);
            result.push_back((sum % 2) + '0');
            carry = sum / 2;
        }
        reverse(result.begin(), result.end());
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
    public String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();
        int i = a.length() - 1, j = b.length() - 1, carry = 0;
        while (i >= 0 || j >= 0 || carry != 0) {
            int sum = carry + (i >= 0 ? a.charAt(i--) - '0' : 0) + (j >= 0 ? b.charAt(j--) - '0' : 0);
            sb.append(sum % 2);
            carry = sum / 2;
        }
        return sb.reverse().toString();
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = []
        i, j, carry = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += ord(a[i]) - ord('0')
                i -= 1
            if j >= 0:
                total += ord(b[j]) - ord('0')
                j -= 1
            res.append(str(total % 2))
            carry = total // 2
        return "".join(res[::-1])
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i, j, carry = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += ord(a[i]) - ord('0')
                i -= 1
            if j >= 0:
                total += ord(b[j]) - ord('0')
                j -= 1
            res.append(str(total % 2))
            carry = total // 2
        return "".join(res[::-1])
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
char* addBinary(char* a, char* b) {
    int i = (int)strlen(a) - 1;
    int j = (int)strlen(b) - 1;
    int max_len = (i > j ? i : j) + 1;
    char* res = (char*)malloc(max_len + 2);
    res[max_len + 1] = '\0';
    int carry = 0, k = max_len;
    while (i >= 0 || j >= 0 || carry) {
        int sum = carry + (i >= 0 ? a[i--] - '0' : 0) + (j >= 0 ? b[j--] - '0' : 0);
        res[k--] = (sum % 2) + '0';
        carry = sum / 2;
    }
    if (k >= 0) {
        memmove(res, res + k + 1, max_len - k + 1);
    }
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public string AddBinary(string a, string b) {
        StringBuilder sb = new StringBuilder();
        int i = a.Length - 1, j = b.Length - 1, carry = 0;
        while (i >= 0 || j >= 0 || carry > 0) {
            int sum = carry + (i >= 0 ? a[i--] - '0' : 0) + (j >= 0 ? b[j--] - '0' : 0);
            sb.Append(sum % 2);
            carry = sum / 2;
        }
        char[] charArray = sb.ToString().ToCharArray();
        Array.Reverse(charArray);
        return new string(charArray);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    let i = a.length - 1, j = b.length - 1, carry = 0, res = [];
    while (i >= 0 || j >= 0 || carry) {
        let sum = carry + (i >= 0 ? a[i--] - '0' : 0) + (j >= 0 ? b[j--] - '0' : 0);
        res.push(sum % 2);
        carry = Math.floor(sum / 2);
    }
    return res.reverse().join('');
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function addBinary(a: string, b: string): string {
    let res: number[] = [];
    let i = a.length - 1, j = b.length - 1, carry = 0;
    while (i >= 0 || j >= 0 || carry > 0) {
        let sum = carry;
        if (i >= 0) sum += a[i--] === '1' ? 1 : 0;
        if (j >= 0) sum += b[j--] === '1' ? 1 : 0;
        res.push(sum % 2);
        carry = Math.floor(sum / 2);
    }
    return res.reverse().join("");
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String $a
     * @param String $b
     * @return String
     */
    function addBinary($a, $b) {
        $res = "";
        $i = strlen($a) - 1;
        $j = strlen($b) - 1;
        $carry = 0;
        while ($i >= 0 || $j >= 0 || $carry > 0) {
            $sum = $carry;
            if ($i >= 0) $sum += ($a[$i--] === '1' ? 1 : 0);
            if ($j >= 0) $sum += ($b[$j--] === '1' ? 1 : 0);
            $res .= ($sum % 2);
            $carry = (int)($sum / 2);
        }
        return strrev($res);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func addBinary(_ a: String, _ b: String) -> String {
        var res = ""
        let aArr = Array(a), bArr = Array(b)
        var i = aArr.count - 1, j = bArr.count - 1, carry = 0
        while i >= 0 || j >= 0 || carry > 0 {
            var sum = carry
            if i >= 0 {
                sum += aArr[i] == "1" ? 1 : 0
                i -= 1
            }
            if j >= 0 {
                sum += bArr[j] == "1" ? 1 : 0
                j -= 1
            }
            res += String(sum % 2)
            carry = sum / 2
        }
        return String(res.reversed())
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun addBinary(a: String, b: String): String {
        val res = StringBuilder()
        var i = a.length - 1
        var j = b.length - 1
        var carry = 0
        while (i >= 0 || j >= 0 || carry > 0) {
            var sum = carry
            if (i >= 0) sum += if (a[i--] == '1') 1 else 0
            if (j >= 0) sum += if (b[j--] == '1') 1 else 0
            res.append(sum % 2)
            carry = sum / 2
        }
        return res.reverse().toString()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  String addBinary(String a, String b) {
    StringBuffer res = StringBuffer();
    int i = a.length - 1;
    int j = b.length - 1;
    int carry = 0;
    while (i >= 0 || j >= 0 || carry > 0) {
      int sum = carry;
      if (i >= 0) sum += (a[i--] == '1' ? 1 : 0);
      if (j >= 0) sum += (b[j--] == '1' ? 1 : 0);
      res.write(sum % 2);
      carry = sum ~/ 2;
    }
    return res.toString().split('').reversed.join('');
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func addBinary(a string, b string) string {
    i, j := len(a)-1, len(b)-1
    carry := 0
    var res []byte
    for i >= 0 || j >= 0 || carry > 0 {
        sum := carry
        if i >= 0 {
            sum += int(a[i] - '0')
            i--
        }
        if j >= 0 {
            sum += int(b[j] - '0')
            j--
        }
        res = append(res, byte(sum%2 + '0'))
        carry = sum / 2
    }
    for k, l := 0, len(res)-1; k < l; k, l = k+1, l-1 {
        res[k], res[l] = res[l], res[k]
    }
    return string(res)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} a
# @param {String} b
# @return {String}
def add_binary(a, b)
  (a.to_i(2) + b.to_i(2)).to_s(2)
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def addBinary(a: String, b: String): String = {
        (BigInt(a, 2) + BigInt(b, 2)).toString(2)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn add_binary(a: String, b: String) -> String {
        let mut res = String::new();
        let mut i = a.len() as i32 - 1;
        let mut j = b.len() as i32 - 1;
        let mut carry = 0;
        let a_bytes = a.as_bytes();
        let b_bytes = b.as_bytes();
        while i >= 0 || j >= 0 || carry != 0 {
            let mut sum = carry;
            if i >= 0 {
                sum += (a_bytes[i as usize] - b'0') as i32;
                i -= 1;
            }
            if j >= 0 {
                sum += (b_bytes[j as usize] - b'0') as i32;
                j -= 1;
            }
            res.push(((sum % 2) as u8 + b'0') as char);
            carry = sum / 2;
        }
        res.chars().rev().collect()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (add-binary a b)
  (-> string? string? string?)
  (number->string (+ (string->number a 2) (string->number b 2)) 2))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec add_binary(A :: unicode:unicode_binary(), B :: unicode:unicode_binary()) -> unicode:unicode_binary().
add_binary(A, B) ->
  integer_to_binary(binary_to_integer(A, 2) + binary_to_integer(B, 2), 2).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec add_binary(a :: String.t, b :: String.t) :: String.t
  def add_binary(a, b) do
    Integer.to_string(String.to_integer(a, 2) + String.to_integer(b, 2), 2)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(max(N, M)) where N and M are the lengths of the input strings. Each bit is processed exactly once in a single pass.
- **Space Complexity:** O(max(N, M)) because the output string requires space proportional to the length of the larger input string plus at most one potential carry bit.
