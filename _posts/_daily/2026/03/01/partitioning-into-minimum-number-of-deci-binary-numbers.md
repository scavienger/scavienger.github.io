---
layout: post
title: "Partitioning Into Minimum Number Of Deci-Binary Numbers"
date: 2026-03-01 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Greedy"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minPartitions(string n) {\n        int\
        \ res = 0;\n        for (char c : n) {\n            res = max(res, c - '0');\n\
        \            if (res == 9) break;\n        }\n        return res;\n    }\n};"
      java: "class Solution {\n    public int minPartitions(String n) {\n        int\
        \ max = 0;\n        for (int i = 0; i < n.length(); i++) {\n            int\
        \ digit = n.charAt(i) - '0';\n            if (digit > max) max = digit;\n  \
        \          if (max == 9) break;\n        }\n        return max;\n    }\n}"
      python: "class Solution(object):\n    def minPartitions(self, n):\n        \"\"\
        \"\n        :type n: str\n        :rtype: int\n        \"\"\"\n        return\
        \ int(max(n))"
      python3: "class Solution:\n    def minPartitions(self, n: str) -> int:\n     \
        \   return int(max(n))"
      c: "int minPartitions(char* n) {\n    int max = 0;\n    for (int i = 0; n[i] !=\
        \ '\\0'; i++) {\n        int digit = n[i] - '0';\n        if (digit > max) max\
        \ = digit;\n        if (max == 9) break;\n    }\n    return max;\n}"
      csharp: "public class Solution {\n    public int MinPartitions(string n) {\n \
        \       int max = 0;\n        foreach (char c in n) {\n            int digit\
        \ = c - '0';\n            if (digit > max) max = digit;\n            if (max\
        \ == 9) break;\n        }\n        return max;\n    }\n}"
      javascript: "/**\n * @param {string} n\n * @return {number}\n */\nvar minPartitions\
        \ = function(n) {\n    let max = 0;\n    for (let i = 0; i < n.length; i++)\
        \ {\n        let digit = n.charCodeAt(i) - 48;\n        if (digit > max) max\
        \ = digit;\n        if (max === 9) break;\n    }\n    return max;\n};"
      typescript: "function minPartitions(n: string): number {\n    let maxDigit = 0;\n\
        \    for (let i = 0; i < n.length; i++) {\n        const digit = n.charCodeAt(i)\
        \ - 48;\n        if (digit > maxDigit) maxDigit = digit;\n        if (maxDigit\
        \ === 9) return 9;\n    }\n    return maxDigit;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $n\n     * @return Integer\n\
        \     */\n    function minPartitions($n) {\n        $maxDigit = 0;\n       \
        \ $len = strlen($n);\n        for ($i = 0; $i < $len; $i++) {\n            $digit\
        \ = ord($n[$i]) - 48;\n            if ($digit > $maxDigit) {\n             \
        \   $maxDigit = $digit;\n            }\n            if ($maxDigit === 9) return\
        \ 9;\n        }\n        return $maxDigit;\n    }\n}"
      swift: "class Solution {\n    func minPartitions(_ n: String) -> Int {\n     \
        \   var maxDigit = 0\n        for charCode in n.utf8 {\n            let digit\
        \ = Int(charCode - 48)\n            if digit > maxDigit {\n                maxDigit\
        \ = digit\n            }\n            if maxDigit == 9 { return 9 }\n      \
        \  }\n        return maxDigit\n    }\n}"
      kotlin: "class Solution {\n    fun minPartitions(n: String): Int {\n        var\
        \ maxDigit = 0\n        for (char in n) {\n            val digit = char - '0'\n\
        \            if (digit > maxDigit) {\n                maxDigit = digit\n   \
        \         }\n            if (maxDigit == 9) return 9\n        }\n        return\
        \ maxDigit\n    }\n}"
      dart: "class Solution {\n  int minPartitions(String n) {\n    int maxDigit = 0;\n\
        \    for (int i = 0; i < n.length; i++) {\n      int digit = n.codeUnitAt(i)\
        \ - 48;\n      if (digit > maxDigit) {\n        maxDigit = digit;\n      }\n\
        \      if (maxDigit == 9) return 9;\n    }\n    return maxDigit;\n  }\n}"
      go: "func minPartitions(n string) int {\n    maxDigit := 0\n    for i := 0; i\
        \ < len(n); i++ {\n        digit := int(n[i] - '0')\n        if digit > maxDigit\
        \ {\n            maxDigit = digit\n        }\n        if maxDigit == 9 {\n \
        \           return 9\n        }\n    }\n    return maxDigit\n}"
      ruby: "def min_partitions(n)\n  n.chars.max.to_i\nend"
      scala: "object Solution {\n    def minPartitions(n: String): Int = {\n       \
        \ n.map(_ - '0').max\n    }\n}"
      rust: "impl Solution {\n    pub fn min_partitions(n: String) -> i32 {\n      \
        \  (n.bytes().max().unwrap() - b'0') as i32\n    }\n}"
      racket: "(define/contract (min-partitions n)\n  (-> string? exact-integer?)\n\
        \  (apply max (map (lambda (c) (- (char->integer c) 48)) (string->list n))))"
      erlang: "-spec min_partitions(N :: unicode:unicode_binary()) -> integer().\nmin_partitions(N)\
        \ ->\n  lists:max(binary_to_list(N)) - $0."
      elixir: "defmodule Solution do\n  @spec min_partitions(n :: String.t) :: integer\n\
        \  def min_partitions(n) do\n    n |> String.to_charlist() |> Enum.max() |>\
        \ Kernel.-(?0)\n  end\nend"
    approach: 'To represent a decimal digit $d$ using only deci-binary numbers (where
      each digit is either 0 or 1), we need at least $d$ separate deci-binary numbers.
      This is because each deci-binary number can contribute at most a ''1'' to any
      specific digit position in the sum. If any position in the target string $n$ has
      a digit $k$, we must have at least $k$ deci-binary numbers that have a ''1'' at
      that specific position to reach that sum.


      Since this logic applies independently to every digit position in the string,
      the minimum number of deci-binary numbers required is determined by the maximum
      digit present in the string $n$. For any string $n$ with a maximum digit $k$,
      we can always construct $k$ deci-binary numbers by setting the digit at position
      $i$ to 1 in the first $n[i]$ deci-binary numbers and 0 in the remaining $k - n[i]$
      numbers. Thus, the solution is simply finding the maximum character value in the
      string.'
    time_complexity: O(L), where L is the length of the string $n$. We iterate through
      the string once to identify the maximum digit, performing a constant amount of
      work for each character.
    space_complexity: O(1). We only store a single variable to track the maximum digit
      encountered so far, which uses constant extra space regardless of the input size.
    elapsed_time: 42.10447597503662
    model: gemini-3-flash-preview
    generated_at: '2026-03-01 01:43:28 '
---

## Problem #1689: Partitioning Into Minimum Number Of Deci-Binary Numbers

**Difficulty:** Medium

**Topics:** String, Greedy

## Problem Description

<p>A decimal number is called <strong>deci-binary</strong> if each of its digits is either <code>0</code> or <code>1</code> without any leading zeros. For example, <code>101</code> and <code>1100</code> are <strong>deci-binary</strong>, while <code>112</code> and <code>3001</code> are not.</p>

<p>Given a string <code>n</code> that represents a positive decimal integer, return <em>the <strong>minimum</strong> number of positive <strong>deci-binary</strong> numbers needed so that they sum up to </em><code>n</code><em>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = &quot;32&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> 10 + 11 + 11 = 32
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = &quot;82734&quot;
<strong>Output:</strong> 8
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = &quot;27346209830709182346&quot;
<strong>Output:</strong> 9
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n.length &lt;= 10<sup>5</sup></code></li>
	<li><code>n</code> consists of only digits.</li>
	<li><code>n</code> does not contain any leading zeros and represents a positive integer.</li>
</ul>


## Hints

1. Think about if the input was only one digit. Then you need to add up as many ones as the value of this digit.

2. If the input has multiple digits, then you can solve for each digit independently, and merge the answers to form numbers that add up to that input.

3. Thus the answer is equal to the max digit.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To represent a decimal digit $d$ using only deci-binary numbers (where each digit is either 0 or 1), we need at least $d$ separate deci-binary numbers. This is because each deci-binary number can contribute at most a '1' to any specific digit position in the sum. If any position in the target string $n$ has a digit $k$, we must have at least $k$ deci-binary numbers that have a '1' at that specific position to reach that sum.

Since this logic applies independently to every digit position in the string, the minimum number of deci-binary numbers required is determined by the maximum digit present in the string $n$. For any string $n$ with a maximum digit $k$, we can always construct $k$ deci-binary numbers by setting the digit at position $i$ to 1 in the first $n[i]$ deci-binary numbers and 0 in the remaining $k - n[i]$ numbers. Thus, the solution is simply finding the maximum character value in the string.

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
    int minPartitions(string n) {
        int res = 0;
        for (char c : n) {
            res = max(res, c - '0');
            if (res == 9) break;
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
    public int minPartitions(String n) {
        int max = 0;
        for (int i = 0; i < n.length(); i++) {
            int digit = n.charAt(i) - '0';
            if (digit > max) max = digit;
            if (max == 9) break;
        }
        return max;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        return int(max(n))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int minPartitions(char* n) {
    int max = 0;
    for (int i = 0; n[i] != '\0'; i++) {
        int digit = n[i] - '0';
        if (digit > max) max = digit;
        if (max == 9) break;
    }
    return max;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinPartitions(string n) {
        int max = 0;
        foreach (char c in n) {
            int digit = c - '0';
            if (digit > max) max = digit;
            if (max == 9) break;
        }
        return max;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} n
 * @return {number}
 */
var minPartitions = function(n) {
    let max = 0;
    for (let i = 0; i < n.length; i++) {
        let digit = n.charCodeAt(i) - 48;
        if (digit > max) max = digit;
        if (max === 9) break;
    }
    return max;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minPartitions(n: string): number {
    let maxDigit = 0;
    for (let i = 0; i < n.length; i++) {
        const digit = n.charCodeAt(i) - 48;
        if (digit > maxDigit) maxDigit = digit;
        if (maxDigit === 9) return 9;
    }
    return maxDigit;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String $n
     * @return Integer
     */
    function minPartitions($n) {
        $maxDigit = 0;
        $len = strlen($n);
        for ($i = 0; $i < $len; $i++) {
            $digit = ord($n[$i]) - 48;
            if ($digit > $maxDigit) {
                $maxDigit = $digit;
            }
            if ($maxDigit === 9) return 9;
        }
        return $maxDigit;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minPartitions(_ n: String) -> Int {
        var maxDigit = 0
        for charCode in n.utf8 {
            let digit = Int(charCode - 48)
            if digit > maxDigit {
                maxDigit = digit
            }
            if maxDigit == 9 { return 9 }
        }
        return maxDigit
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minPartitions(n: String): Int {
        var maxDigit = 0
        for (char in n) {
            val digit = char - '0'
            if (digit > maxDigit) {
                maxDigit = digit
            }
            if (maxDigit == 9) return 9
        }
        return maxDigit
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minPartitions(String n) {
    int maxDigit = 0;
    for (int i = 0; i < n.length; i++) {
      int digit = n.codeUnitAt(i) - 48;
      if (digit > maxDigit) {
        maxDigit = digit;
      }
      if (maxDigit == 9) return 9;
    }
    return maxDigit;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minPartitions(n string) int {
    maxDigit := 0
    for i := 0; i < len(n); i++ {
        digit := int(n[i] - '0')
        if digit > maxDigit {
            maxDigit = digit
        }
        if maxDigit == 9 {
            return 9
        }
    }
    return maxDigit
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def min_partitions(n)
  n.chars.max.to_i
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minPartitions(n: String): Int = {
        n.map(_ - '0').max
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_partitions(n: String) -> i32 {
        (n.bytes().max().unwrap() - b'0') as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-partitions n)
  (-> string? exact-integer?)
  (apply max (map (lambda (c) (- (char->integer c) 48)) (string->list n))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_partitions(N :: unicode:unicode_binary()) -> integer().
min_partitions(N) ->
  lists:max(binary_to_list(N)) - $0.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_partitions(n :: String.t) :: integer
  def min_partitions(n) do
    n |> String.to_charlist() |> Enum.max() |> Kernel.-(?0)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(L), where L is the length of the string $n$. We iterate through the string once to identify the maximum digit, performing a constant amount of work for each character.
- **Space Complexity:** O(1). We only store a single variable to track the maximum digit encountered so far, which uses constant extra space regardless of the input size.
