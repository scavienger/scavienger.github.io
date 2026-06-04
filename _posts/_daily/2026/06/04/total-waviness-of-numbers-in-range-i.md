---
layout: post
title: "Total Waviness of Numbers in Range I"
date: 2026-06-04 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Math", "Dynamic Programming", "Enumeration"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/
ai_solutions:
  - solutions:
      cpp: "#include <string>\n\nclass Solution {\npublic:\n    int totalWaviness(int\
        \ num1, int num2) {\n        int total = 0;\n        for (int n = num1; n <=\
        \ num2; ++n) {\n            if (n < 100) continue;\n            std::string\
        \ s = std::to_string(n);\n            int len = (int)s.length();\n         \
        \   for (int i = 1; i < len - 1; ++i) {\n                if ((s[i] > s[i - 1]\
        \ && s[i] > s[i + 1]) || \n                    (s[i] < s[i - 1] && s[i] < s[i\
        \ + 1])) {\n                    total++;\n                }\n            }\n\
        \        }\n        return total;\n    }\n};"
      java: "class Solution {\n    public int totalWaviness(int num1, int num2) {\n\
        \        int total = 0;\n        for (int n = num1; n <= num2; n++) {\n    \
        \        if (n < 100) continue;\n            String s = Integer.toString(n);\n\
        \            int len = s.length();\n            for (int i = 1; i < len - 1;\
        \ i++) {\n                char curr = s.charAt(i);\n                char prev\
        \ = s.charAt(i - 1);\n                char next = s.charAt(i + 1);\n       \
        \         if ((curr > prev && curr > next) || (curr < prev && curr < next))\
        \ {\n                    total++;\n                }\n            }\n      \
        \  }\n        return total;\n    }\n}"
      python: "class Solution(object):\n    def totalWaviness(self, num1, num2):\n \
        \       \"\"\"\n        :type num1: int\n        :type num2: int\n        :rtype:\
        \ int\n        \"\"\"\n        total = 0\n        for n in range(num1, num2\
        \ + 1):\n            s = str(n)\n            if len(s) < 3:\n              \
        \  continue\n            for i in range(1, len(s) - 1):\n                if\
        \ (s[i] > s[i-1] and s[i] > s[i+1]) or (s[i] < s[i-1] and s[i] < s[i+1]):\n\
        \                    total += 1\n        return total"
      python3: "class Solution:\n    def totalWaviness(self, num1: int, num2: int) ->\
        \ int:\n        total = 0\n        for n in range(num1, num2 + 1):\n       \
        \     s = str(n)\n            if len(s) < 3:\n                continue\n   \
        \         for i in range(1, len(s) - 1):\n                if (s[i] > s[i-1]\
        \ and s[i] > s[i+1]) or (s[i] < s[i-1] and s[i] < s[i+1]):\n               \
        \     total += 1\n        return total"
      c: "int totalWaviness(int num1, int num2) {\n    int total = 0;\n    for (int\
        \ n = num1; n <= num2; n++) {\n        if (n < 100) continue;\n        int digits[10];\n\
        \        int len = 0;\n        int temp = n;\n        while (temp > 0) {\n \
        \           digits[len++] = temp % 10;\n            temp /= 10;\n        }\n\
        \        for (int i = 1; i < len - 1; i++) {\n            if ((digits[i] > digits[i\
        \ - 1] && digits[i] > digits[i + 1]) || \n                (digits[i] < digits[i\
        \ - 1] && digits[i] < digits[i + 1])) {\n                total++;\n        \
        \    }\n        }\n    }\n    return total;\n}"
      csharp: "public class Solution {\n    public int TotalWaviness(int num1, int num2)\
        \ {\n        int total = 0;\n        for (int i = num1; i <= num2; i++) {\n\
        \            string s = i.ToString();\n            if (s.Length < 3) continue;\n\
        \            for (int j = 1; j < s.Length - 1; j++) {\n                if ((s[j]\
        \ > s[j - 1] && s[j] > s[j + 1]) || (s[j] < s[j - 1] && s[j] < s[j + 1])) {\n\
        \                    total++;\n                }\n            }\n        }\n\
        \        return total;\n    }\n}"
      javascript: "/**\n * @param {number} num1\n * @param {number} num2\n * @return\
        \ {number}\n */\nvar totalWaviness = function(num1, num2) {\n    let total =\
        \ 0;\n    for (let i = num1; i <= num2; i++) {\n        let s = i.toString();\n\
        \        if (s.length < 3) continue;\n        for (let j = 1; j < s.length -\
        \ 1; j++) {\n            if ((s[j] > s[j - 1] && s[j] > s[j + 1]) || (s[j] <\
        \ s[j - 1] && s[j] < s[j + 1])) {\n                total++;\n            }\n\
        \        }\n    }\n    return total;\n};"
      typescript: "function totalWaviness(num1: number, num2: number): number {\n  \
        \  let total = 0;\n    for (let i = num1; i <= num2; i++) {\n        let s =\
        \ i.toString();\n        if (s.length < 3) continue;\n        for (let j = 1;\
        \ j < s.length - 1; j++) {\n            if ((s[j] > s[j - 1] && s[j] > s[j +\
        \ 1]) || (s[j] < s[j - 1] && s[j] < s[j + 1])) {\n                total++;\n\
        \            }\n        }\n    }\n    return total;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $num1\n     * @param\
        \ Integer $num2\n     * @return Integer\n     */\n    function totalWaviness($num1,\
        \ $num2) {\n        $total = 0;\n        for ($i = $num1; $i <= $num2; $i++)\
        \ {\n            $s = (string)$i;\n            $len = strlen($s);\n        \
        \    if ($len < 3) continue;\n            for ($j = 1; $j < $len - 1; $j++)\
        \ {\n                if (($s[$j] > $s[$j - 1] && $s[$j] > $s[$j + 1]) || ($s[$j]\
        \ < $s[$j - 1] && $s[$j] < $s[$j + 1])) {\n                    $total++;\n \
        \               }\n            }\n        }\n        return $total;\n    }\n\
        }"
      swift: "class Solution {\n    func totalWaviness(_ num1: Int, _ num2: Int) ->\
        \ Int {\n        var total = 0\n        for i in num1...num2 {\n           \
        \ let s = String(i)\n            let digits = Array(s)\n            if digits.count\
        \ < 3 {\n                continue\n            }\n            for j in 1..<(digits.count\
        \ - 1) {\n                if (digits[j] > digits[j - 1] && digits[j] > digits[j\
        \ + 1]) || (digits[j] < digits[j - 1] && digits[j] < digits[j + 1]) {\n    \
        \                total += 1\n                }\n            }\n        }\n \
        \       return total\n    }\n}"
      kotlin: "class Solution {\n    fun totalWaviness(num1: Int, num2: Int): Int {\n\
        \        var total = 0\n        for (i in num1..num2) {\n            val s =\
        \ i.toString()\n            if (s.length >= 3) {\n                for (j in\
        \ 1 until s.length - 1) {\n                    val prev = s[j - 1]\n       \
        \             val curr = s[j]\n                    val next = s[j + 1]\n   \
        \                 if ((curr > prev && curr > next) || (curr < prev && curr <\
        \ next)) {\n                        total++\n                    }\n       \
        \         }\n            }\n        }\n        return total\n    }\n}"
      dart: "class Solution {\n  int totalWaviness(int num1, int num2) {\n    int total\
        \ = 0;\n    for (int i = num1; i <= num2; i++) {\n      String s = i.toString();\n\
        \      if (s.length >= 3) {\n        for (int j = 1; j < s.length - 1; j++)\
        \ {\n          int prev = s.codeUnitAt(j - 1);\n          int curr = s.codeUnitAt(j);\n\
        \          int next = s.codeUnitAt(j + 1);\n          if ((curr > prev && curr\
        \ > next) || (curr < prev && curr < next)) {\n            total++;\n       \
        \   }\n        }\n      }\n    }\n    return total;\n  }\n}"
      go: "import \"strconv\"\n\nfunc totalWaviness(num1 int, num2 int) int {\n\ttotal\
        \ := 0\n\tfor i := num1; i <= num2; i++ {\n\t\ts := strconv.Itoa(i)\n\t\tif\
        \ len(s) >= 3 {\n\t\t\tfor j := 1; j < len(s)-1; j++ {\n\t\t\t\tif (s[j] > s[j-1]\
        \ && s[j] > s[j+1]) || (s[j] < s[j-1] && s[j] < s[j+1]) {\n\t\t\t\t\ttotal++\n\
        \t\t\t\t}\n\t\t\t}\n\t\t}\n\t}\n\treturn total\n}"
      ruby: "# @param {Integer} num1\n# @param {Integer} num2\n# @return {Integer}\n\
        def total_waviness(num1, num2)\n  total = 0\n  (num1..num2).each do |i|\n  \
        \  s = i.to_s\n    if s.length >= 3\n      (1...(s.length - 1)).each do |j|\n\
        \        prev = s[j - 1]\n        curr = s[j]\n        nxt = s[j + 1]\n    \
        \    if (curr > prev && curr > nxt) || (curr < prev && curr < nxt)\n       \
        \   total += 1\n        end\n      end\n    end\n  end\n  total\nend"
      scala: "object Solution {\n    def totalWaviness(num1: Int, num2: Int): Int =\
        \ {\n        var total = 0\n        for (i <- num1 to num2) {\n            val\
        \ s = i.toString\n            if (s.length >= 3) {\n                for (j <-\
        \ 1 until s.length - 1) {\n                    val prev = s(j - 1)\n       \
        \             val curr = s(j)\n                    val next = s(j + 1)\n   \
        \                 if ((curr > prev && curr > next) || (curr < prev && curr <\
        \ next)) {\n                        total += 1\n                    }\n    \
        \            }\n            }\n        }\n        total\n    }\n}"
      rust: "impl Solution {\n    pub fn total_waviness(num1: i32, num2: i32) -> i32\
        \ {\n        let mut total = 0;\n        for n in num1..=num2 {\n          \
        \  let s = n.to_string();\n            let digits = s.as_bytes();\n        \
        \    if digits.len() < 3 {\n                continue;\n            }\n     \
        \       for i in 1..digits.len() - 1 {\n                if (digits[i] > digits[i\
        \ - 1] && digits[i] > digits[i + 1]) ||\n                   (digits[i] < digits[i\
        \ - 1] && digits[i] < digits[i + 1]) {\n                    total += 1;\n  \
        \              }\n            }\n        }\n        total\n    }\n}"
      racket: "(define/contract (total-waviness num1 num2)\n  (-> exact-integer? exact-integer?\
        \ exact-integer?)\n  (define (get-waviness d count)\n    (match d\n      [(list\
        \ d1 d2 d3 rest ...)\n       (let ([nc (if (or (and (> d2 d1) (> d2 d3))\n \
        \                        (and (< d2 d1) (< d2 d3)))\n                     (+\
        \ count 1)\n                     count)])\n         (get-waviness (list* d2\
        \ d3 rest) nc))]\n      [_ count]))\n  (for/sum ([n (in-range num1 (add1 num2))])\n\
        \    (get-waviness (map char->integer (string->list (number->string n))) 0)))"
      erlang: "-spec total_waviness(Num1 :: integer(), Num2 :: integer()) -> integer().\n\
        total_waviness(Num1, Num2) ->\n    lists:foldl(fun(N, Acc) -> Acc + calculate_waviness(integer_to_list(N),\
        \ 0) end, 0, lists:seq(Num1, Num2)).\n\ncalculate_waviness([D1, D2, D3 | Rest],\
        \ Count) ->\n    NewCount = case (D2 > D1 andalso D2 > D3) orelse (D2 < D1 andalso\
        \ D2 < D3) of\n                   true -> Count + 1;\n                   false\
        \ -> Count\n               end,\n    calculate_waviness([D2, D3 | Rest], NewCount);\n\
        calculate_waviness(_, Count) ->\n    Count."
      elixir: "defmodule Solution do\n  @spec total_waviness(num1 :: integer, num2 ::\
        \ integer) :: integer\n  def total_waviness(num1, num2) do\n    Enum.reduce(num1..num2,\
        \ 0, fn n, acc ->\n      acc + get_waviness(Integer.to_charlist(n))\n    end)\n\
        \  end\n\n  defp get_waviness([d1, d2, d3 | rest]) do\n    count = if (d2 >\
        \ d1 and d2 > d3) or (d2 < d1 and d2 < d3), do: 1, else: 0\n    count + get_waviness([d2,\
        \ d3 | rest])\n  end\n\n  defp get_waviness(_), do: 0\nend"
    approach: 'The algorithm employs a brute-force approach to iterate through every
      integer in the inclusive range [num1, num2]. For each integer, it calculates the
      ''waviness'' by checking all digits except for the first and the last. Since the
      maximum value of num2 is $10^5$, each number has at most 6 digits, making it efficient
      to convert the number into a traversable format like a string or an array of digits
      to perform these localized comparisons.


      A digit at index $i$ is identified as a peak if $digit[i] > digit[i-1]$ and $digit[i]
      > digit[i+1]$. Similarly, it is a valley if $digit[i] < digit[i-1]$ and $digit[i]
      < digit[i+1]$. For every number, we sum the occurrences of peaks and valleys and
      add this to a global counter. Numbers with fewer than three digits are skipped
      as they cannot contain any internal digits to satisfy the peak or valley criteria.'
    time_complexity: O((num2 - num1) * log10(num2)) with one-paragraph explanation.
      The algorithm iterates through every integer in the range, which contains at most
      $10^5$ numbers. For each number, it performs a number of operations proportional
      to its digit count (at most 6), leading to a total execution time that is well
      within the limits.
    space_complexity: O(log10(num2)) with one-paragraph explanation. The space complexity
      is determined by the storage required for the digits of a single number (either
      as a string or an array) while it is being processed. Since the maximum number
      of digits is 6, this is effectively constant space O(1).
    elapsed_time: 207.88891124725342
    model: gemini-3-flash-preview
    generated_at: '2026-06-04 02:58:03 '
---

## Problem #3751: Total Waviness of Numbers in Range I

**Difficulty:** Medium

**Topics:** Math, Dynamic Programming, Enumeration

## Problem Description

<p>You are given two integers <code>num1</code> and <code>num2</code> representing an <strong>inclusive</strong> range <code>[num1, num2]</code>.</p>

<p>The <strong>waviness</strong> of a number is defined as the total count of its <strong>peaks</strong> and <strong>valleys</strong>:</p>

<ul>
	<li>A digit is a <strong>peak</strong> if it is <strong>strictly greater</strong> than both of its immediate neighbors.</li>
	<li>A digit is a <strong>valley</strong> if it is <strong>strictly less</strong> than both of its immediate neighbors.</li>
	<li>The first and last digits of a number <strong>cannot</strong> be peaks or valleys.</li>
	<li>Any number with fewer than 3 digits has a waviness of 0.</li>
</ul>
Return the total sum of waviness for all numbers in the range <code>[num1, num2]</code>.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">num1 = 120, num2 = 130</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>
In the range <code>[120, 130]</code>:

<ul>
	<li><code>120</code>: middle digit 2 is a peak, waviness = 1.</li>
	<li><code>121</code>: middle digit 2 is a peak, waviness = 1.</li>
	<li><code>130</code>: middle digit 3 is a peak, waviness = 1.</li>
	<li>All other numbers in the range have a waviness of 0.</li>
</ul>

<p>Thus, total waviness is <code>1 + 1 + 1 = 3</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">num1 = 198, num2 = 202</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>
In the range <code>[198, 202]</code>:

<ul>
	<li><code>198</code>: middle digit 9 is a peak, waviness = 1.</li>
	<li><code>201</code>: middle digit 0 is a valley, waviness = 1.</li>
	<li><code>202</code>: middle digit 0 is a valley, waviness = 1.</li>
	<li>All other numbers in the range have a waviness of 0.</li>
</ul>

<p>Thus, total waviness is <code>1 + 1 + 1 = 3</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">num1 = 4848, num2 = 4848</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>Number <code>4848</code>: the second digit 8 is a peak, and the third digit 4 is a valley, giving a waviness of 2.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num1 &lt;= num2 &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. Use bruteforce

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm employs a brute-force approach to iterate through every integer in the inclusive range [num1, num2]. For each integer, it calculates the 'waviness' by checking all digits except for the first and the last. Since the maximum value of num2 is $10^5$, each number has at most 6 digits, making it efficient to convert the number into a traversable format like a string or an array of digits to perform these localized comparisons.

A digit at index $i$ is identified as a peak if $digit[i] > digit[i-1]$ and $digit[i] > digit[i+1]$. Similarly, it is a valley if $digit[i] < digit[i-1]$ and $digit[i] < digit[i+1]$. For every number, we sum the occurrences of peaks and valleys and add this to a global counter. Numbers with fewer than three digits are skipped as they cannot contain any internal digits to satisfy the peak or valley criteria.

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
#include <string>

class Solution {
public:
    int totalWaviness(int num1, int num2) {
        int total = 0;
        for (int n = num1; n <= num2; ++n) {
            if (n < 100) continue;
            std::string s = std::to_string(n);
            int len = (int)s.length();
            for (int i = 1; i < len - 1; ++i) {
                if ((s[i] > s[i - 1] && s[i] > s[i + 1]) || 
                    (s[i] < s[i - 1] && s[i] < s[i + 1])) {
                    total++;
                }
            }
        }
        return total;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int totalWaviness(int num1, int num2) {
        int total = 0;
        for (int n = num1; n <= num2; n++) {
            if (n < 100) continue;
            String s = Integer.toString(n);
            int len = s.length();
            for (int i = 1; i < len - 1; i++) {
                char curr = s.charAt(i);
                char prev = s.charAt(i - 1);
                char next = s.charAt(i + 1);
                if ((curr > prev && curr > next) || (curr < prev && curr < next)) {
                    total++;
                }
            }
        }
        return total;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        total = 0
        for n in range(num1, num2 + 1):
            s = str(n)
            if len(s) < 3:
                continue
            for i in range(1, len(s) - 1):
                if (s[i] > s[i-1] and s[i] > s[i+1]) or (s[i] < s[i-1] and s[i] < s[i+1]):
                    total += 1
        return total
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total = 0
        for n in range(num1, num2 + 1):
            s = str(n)
            if len(s) < 3:
                continue
            for i in range(1, len(s) - 1):
                if (s[i] > s[i-1] and s[i] > s[i+1]) or (s[i] < s[i-1] and s[i] < s[i+1]):
                    total += 1
        return total
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int totalWaviness(int num1, int num2) {
    int total = 0;
    for (int n = num1; n <= num2; n++) {
        if (n < 100) continue;
        int digits[10];
        int len = 0;
        int temp = n;
        while (temp > 0) {
            digits[len++] = temp % 10;
            temp /= 10;
        }
        for (int i = 1; i < len - 1; i++) {
            if ((digits[i] > digits[i - 1] && digits[i] > digits[i + 1]) || 
                (digits[i] < digits[i - 1] && digits[i] < digits[i + 1])) {
                total++;
            }
        }
    }
    return total;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int TotalWaviness(int num1, int num2) {
        int total = 0;
        for (int i = num1; i <= num2; i++) {
            string s = i.ToString();
            if (s.Length < 3) continue;
            for (int j = 1; j < s.Length - 1; j++) {
                if ((s[j] > s[j - 1] && s[j] > s[j + 1]) || (s[j] < s[j - 1] && s[j] < s[j + 1])) {
                    total++;
                }
            }
        }
        return total;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} num1
 * @param {number} num2
 * @return {number}
 */
var totalWaviness = function(num1, num2) {
    let total = 0;
    for (let i = num1; i <= num2; i++) {
        let s = i.toString();
        if (s.length < 3) continue;
        for (let j = 1; j < s.length - 1; j++) {
            if ((s[j] > s[j - 1] && s[j] > s[j + 1]) || (s[j] < s[j - 1] && s[j] < s[j + 1])) {
                total++;
            }
        }
    }
    return total;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function totalWaviness(num1: number, num2: number): number {
    let total = 0;
    for (let i = num1; i <= num2; i++) {
        let s = i.toString();
        if (s.length < 3) continue;
        for (let j = 1; j < s.length - 1; j++) {
            if ((s[j] > s[j - 1] && s[j] > s[j + 1]) || (s[j] < s[j - 1] && s[j] < s[j + 1])) {
                total++;
            }
        }
    }
    return total;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $num1
     * @param Integer $num2
     * @return Integer
     */
    function totalWaviness($num1, $num2) {
        $total = 0;
        for ($i = $num1; $i <= $num2; $i++) {
            $s = (string)$i;
            $len = strlen($s);
            if ($len < 3) continue;
            for ($j = 1; $j < $len - 1; $j++) {
                if (($s[$j] > $s[$j - 1] && $s[$j] > $s[$j + 1]) || ($s[$j] < $s[$j - 1] && $s[$j] < $s[$j + 1])) {
                    $total++;
                }
            }
        }
        return $total;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func totalWaviness(_ num1: Int, _ num2: Int) -> Int {
        var total = 0
        for i in num1...num2 {
            let s = String(i)
            let digits = Array(s)
            if digits.count < 3 {
                continue
            }
            for j in 1..<(digits.count - 1) {
                if (digits[j] > digits[j - 1] && digits[j] > digits[j + 1]) || (digits[j] < digits[j - 1] && digits[j] < digits[j + 1]) {
                    total += 1
                }
            }
        }
        return total
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun totalWaviness(num1: Int, num2: Int): Int {
        var total = 0
        for (i in num1..num2) {
            val s = i.toString()
            if (s.length >= 3) {
                for (j in 1 until s.length - 1) {
                    val prev = s[j - 1]
                    val curr = s[j]
                    val next = s[j + 1]
                    if ((curr > prev && curr > next) || (curr < prev && curr < next)) {
                        total++
                    }
                }
            }
        }
        return total
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int totalWaviness(int num1, int num2) {
    int total = 0;
    for (int i = num1; i <= num2; i++) {
      String s = i.toString();
      if (s.length >= 3) {
        for (int j = 1; j < s.length - 1; j++) {
          int prev = s.codeUnitAt(j - 1);
          int curr = s.codeUnitAt(j);
          int next = s.codeUnitAt(j + 1);
          if ((curr > prev && curr > next) || (curr < prev && curr < next)) {
            total++;
          }
        }
      }
    }
    return total;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "strconv"

func totalWaviness(num1 int, num2 int) int {
	total := 0
	for i := num1; i <= num2; i++ {
		s := strconv.Itoa(i)
		if len(s) >= 3 {
			for j := 1; j < len(s)-1; j++ {
				if (s[j] > s[j-1] && s[j] > s[j+1]) || (s[j] < s[j-1] && s[j] < s[j+1]) {
					total++
				}
			}
		}
	}
	return total
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} num1
# @param {Integer} num2
# @return {Integer}
def total_waviness(num1, num2)
  total = 0
  (num1..num2).each do |i|
    s = i.to_s
    if s.length >= 3
      (1...(s.length - 1)).each do |j|
        prev = s[j - 1]
        curr = s[j]
        nxt = s[j + 1]
        if (curr > prev && curr > nxt) || (curr < prev && curr < nxt)
          total += 1
        end
      end
    end
  end
  total
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def totalWaviness(num1: Int, num2: Int): Int = {
        var total = 0
        for (i <- num1 to num2) {
            val s = i.toString
            if (s.length >= 3) {
                for (j <- 1 until s.length - 1) {
                    val prev = s(j - 1)
                    val curr = s(j)
                    val next = s(j + 1)
                    if ((curr > prev && curr > next) || (curr < prev && curr < next)) {
                        total += 1
                    }
                }
            }
        }
        total
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn total_waviness(num1: i32, num2: i32) -> i32 {
        let mut total = 0;
        for n in num1..=num2 {
            let s = n.to_string();
            let digits = s.as_bytes();
            if digits.len() < 3 {
                continue;
            }
            for i in 1..digits.len() - 1 {
                if (digits[i] > digits[i - 1] && digits[i] > digits[i + 1]) ||
                   (digits[i] < digits[i - 1] && digits[i] < digits[i + 1]) {
                    total += 1;
                }
            }
        }
        total
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (total-waviness num1 num2)
  (-> exact-integer? exact-integer? exact-integer?)
  (define (get-waviness d count)
    (match d
      [(list d1 d2 d3 rest ...)
       (let ([nc (if (or (and (> d2 d1) (> d2 d3))
                         (and (< d2 d1) (< d2 d3)))
                     (+ count 1)
                     count)])
         (get-waviness (list* d2 d3 rest) nc))]
      [_ count]))
  (for/sum ([n (in-range num1 (add1 num2))])
    (get-waviness (map char->integer (string->list (number->string n))) 0)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec total_waviness(Num1 :: integer(), Num2 :: integer()) -> integer().
total_waviness(Num1, Num2) ->
    lists:foldl(fun(N, Acc) -> Acc + calculate_waviness(integer_to_list(N), 0) end, 0, lists:seq(Num1, Num2)).

calculate_waviness([D1, D2, D3 | Rest], Count) ->
    NewCount = case (D2 > D1 andalso D2 > D3) orelse (D2 < D1 andalso D2 < D3) of
                   true -> Count + 1;
                   false -> Count
               end,
    calculate_waviness([D2, D3 | Rest], NewCount);
calculate_waviness(_, Count) ->
    Count.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec total_waviness(num1 :: integer, num2 :: integer) :: integer
  def total_waviness(num1, num2) do
    Enum.reduce(num1..num2, 0, fn n, acc ->
      acc + get_waviness(Integer.to_charlist(n))
    end)
  end

  defp get_waviness([d1, d2, d3 | rest]) do
    count = if (d2 > d1 and d2 > d3) or (d2 < d1 and d2 < d3), do: 1, else: 0
    count + get_waviness([d2, d3 | rest])
  end

  defp get_waviness(_), do: 0
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O((num2 - num1) * log10(num2)) with one-paragraph explanation. The algorithm iterates through every integer in the range, which contains at most $10^5$ numbers. For each number, it performs a number of operations proportional to its digit count (at most 6), leading to a total execution time that is well within the limits.
- **Space Complexity:** O(log10(num2)) with one-paragraph explanation. The space complexity is determined by the storage required for the digits of a single number (either as a string or an array) while it is being processed. Since the maximum number of digits is 6, this is effectively constant space O(1).
