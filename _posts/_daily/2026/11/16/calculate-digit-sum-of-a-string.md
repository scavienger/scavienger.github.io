---
layout: post
title: "Calculate Digit Sum of a String"
date: 2026-11-16 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["String", "Simulation"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/calculate-digit-sum-of-a-string/
ai_solutions:
  - solutions:
      cpp: '// Generation failed for C++

        // Reason: Parsing failed'
      java: '// Generation failed for Java

        // Reason: Parsing failed'
      python: '// Generation failed for Python

        // Reason: Parsing failed'
      python3: '// Generation failed for Python3

        // Reason: Parsing failed'
      c: '// Generation failed for C

        // Reason: Parsing failed'
      csharp: '// Generation failed for C#

        // Reason: Parsing failed'
      javascript: '// Generation failed for JavaScript

        // Reason: Parsing failed'
      typescript: "function digitSum(s: string, k: number): string {\n    while (s.length\
        \ > k) {\n        let nextStr = \"\";\n        for (let i = 0; i < s.length;\
        \ i += k) {\n            let sum = 0;\n            const end = Math.min(i +\
        \ k, s.length);\n            for (let j = i; j < end; j++) {\n             \
        \   sum += s.charCodeAt(j) - 48;\n            }\n            nextStr += sum.toString();\n\
        \        }\n        s = nextStr;\n    }\n    return s;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @param Integer\
        \ $k\n     * @return String\n     */\n    function digitSum($s, $k) {\n    \
        \    while (strlen($s) > $k) {\n            $nextStr = \"\";\n            $len\
        \ = strlen($s);\n            for ($i = 0; $i < $len; $i += $k) {\n         \
        \       $sum = 0;\n                $end = min($i + $k, $len);\n            \
        \    for ($j = $i; $j < $end; $j++) {\n                    $sum += ord($s[$j])\
        \ - ord('0');\n                }\n                $nextStr .= (string)$sum;\n\
        \            }\n            $s = $nextStr;\n        }\n        return $s;\n\
        \    }\n}"
      swift: "class Solution {\n    func digitSum(_ s: String, _ k: Int) -> String {\n\
        \        var current = Array(s)\n        while current.count > k {\n       \
        \     var nextChars: [Character] = []\n            var i = 0\n            while\
        \ i < current.count {\n                var sum = 0\n                let end\
        \ = min(i + k, current.count)\n                for j in i..<end {\n        \
        \            sum += Int(String(current[j]))!\n                }\n          \
        \      nextChars.append(contentsOf: String(sum))\n                i += k\n \
        \           }\n            current = nextChars\n        }\n        return String(current)\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun digitSum(s: String, k: Int): String {\n   \
        \     var current = s\n        while (current.length > k) {\n            val\
        \ sb = java.lang.StringBuilder()\n            var i = 0\n            while (i\
        \ < current.length) {\n                var sum = 0\n                val end\
        \ = kotlin.math.min(i + k, current.length)\n                for (j in i until\
        \ end) {\n                    sum += current[j] - '0'\n                }\n \
        \               sb.append(sum)\n                i += k\n            }\n    \
        \        current = sb.toString()\n        }\n        return current\n    }\n\
        }"
      dart: "class Solution {\n  String digitSum(String s, int k) {\n    while (s.length\
        \ > k) {\n      StringBuffer sb = StringBuffer();\n      for (int i = 0; i <\
        \ s.length; i += k) {\n        int sum = 0;\n        int end = (i + k < s.length)\
        \ ? i + k : s.length;\n        for (int j = i; j < end; j++) {\n          sum\
        \ += s.codeUnitAt(j) - 48;\n        }\n        sb.write(sum.toString());\n \
        \     }\n      s = sb.toString();\n    }\n    return s;\n  }\n}"
      go: "func digitSum(s string, k int) string {\n    for len(s) > k {\n        var\
        \ sb strings.Builder\n        for i := 0; i < len(s); i += k {\n           \
        \ sum := 0\n            end := i + k\n            if end > len(s) {\n      \
        \          end = len(s)\n            }\n            for j := i; j < end; j++\
        \ {\n                sum += int(s[j] - '0')\n            }\n            sb.WriteString(strconv.Itoa(sum))\n\
        \        }\n        s = sb.String()\n    }\n    return s\n}"
      ruby: "# @param {String} s\n# @param {Integer} k\n# @return {String}\ndef digit_sum(s,\
        \ k)\n  while s.length > k\n    s = s.chars.each_slice(k).map { |slice| slice.map(&:to_i).sum.to_s\
        \ }.join\n  end\n  s\nend"
      scala: "object Solution {\n    def digitSum(s: String, k: Int): String = {\n \
        \       var curr = s\n        while (curr.length > k) {\n            curr =\
        \ curr.grouped(k).map(g => g.map(_ - '0').sum.toString).mkString\n        }\n\
        \        curr\n    }\n}"
      rust: "impl Solution {\n    pub fn digit_sum(mut s: String, k: i32) -> String\
        \ {\n        let k = k as usize;\n        while s.len() > k {\n            let\
        \ mut next = String::new();\n            for chunk in s.as_bytes().chunks(k)\
        \ {\n                let sum: u32 = chunk.iter().map(|&b| (b - b'0') as u32).sum();\n\
        \                next.push_str(&sum.to_string());\n            }\n         \
        \   s = next;\n        }\n        s\n    }\n}"
      racket: "(define/contract (digit-sum s k)\n  (-> string? exact-integer? string?)\n\
        \  (if (<= (string-length s) k)\n      s\n      (let loop ([i 0] [acc '()])\n\
        \        (if (>= i (string-length s))\n            (digit-sum (apply string-append\
        \ (reverse acc)) k)\n            (let* ([end (min (+ i k) (string-length s))]\n\
        \                   [sub (substring s i end)]\n                   [sum (for/sum\
        \ ([c (in-string sub)]) (- (char->integer c) 48))])\n              (loop end\
        \ (cons (number->string sum) acc)))))))"
      erlang: "-spec digit_sum(S :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().\n\
        digit_sum(S, K) ->\n  case byte_size(S) =< K of\n    true -> S;\n    false ->\n\
        \      NewS = process_chunks(S, K, []),\n      digit_sum(NewS, K)\n  end.\n\n\
        process_chunks(<<>>, _K, Acc) ->\n  iolist_to_binary(lists:reverse(Acc));\n\
        process_chunks(S, K, Acc) ->\n  {Chunk, Rest} = case byte_size(S) =< K of\n\
        \    true -> {S, <<>>};\n    false -> split_binary(S, K)\n  end,\n  Sum = lists:sum([B\
        \ - $0 || <<B>> <= Chunk]),\n  process_chunks(Rest, K, [integer_to_binary(Sum)\
        \ | Acc])."
      elixir: "defmodule Solution do\n  @spec digit_sum(s :: String.t, k :: integer)\
        \ :: String.t\n  def digit_sum(s, k) do\n    if String.length(s) <= k do\n \
        \     s\n    else\n      s\n      |> String.to_charlist()\n      |> Enum.chunk_every(k)\n\
        \      |> Enum.map(fn chunk ->\n        chunk\n        |> Enum.map(&(&1 - ?0))\n\
        \        |> Enum.sum()\n        |> Integer.to_string()\n      end)\n      |>\
        \ Enum.join()\n      |> digit_sum(k)\n    end\n  end\nend"
    approach: 'The problem asks us to simulate a process that repeatedly transforms
      a string of digits until its length is less than or equal to an integer k. In
      each round of the simulation, we divide the string into consecutive blocks of
      size k, with the final block possibly being shorter. For each block, we sum the
      numeric values of its characters, convert the sum into its string representation,
      and concatenate these representations to form the new string.


      We repeat this grouping and summation procedure inside a loop that continues as
      long as the length of the string strictly exceeds k. Because each group of size
      k has a digit sum whose string representation has length at most ceil(log10(9k
      + 1)), which is strictly less than k for any k >= 2 and reasonable group sizes,
      the string''s length decreases strictly in each step after the initial reduction,
      ensuring quick convergence to a length of at most k.'
    time_complexity: O(N * log(k)) where N is the initial length of the string. In each
      round, we iterate through all characters of the current string, and the length
      shrinks roughly by a factor of k / log10(k), resulting in a logarithmic number
      of rounds and a total work bounded by a geometric series dominated by the first
      round.
    space_complexity: O(N) auxiliary space needed to store the intermediate strings
      and substrings generated during each round of the simulation.
    elapsed_time: 409.29365277290344
    model: gemini-3.8-flash
    generated_at: '2026-11-16 04:12:10 '
---

## Problem #2243: Calculate Digit Sum of a String

**Difficulty:** Easy

**Topics:** String, Simulation

## Problem Description

<p>You are given a string <code>s</code> consisting of digits and an integer <code>k</code>.</p>

<p>A <strong>round</strong> can be completed if the length of <code>s</code> is greater than <code>k</code>. In one round, do the following:</p>

<ol>
	<li><strong>Divide</strong> <code>s</code> into <strong>consecutive groups</strong> of size <code>k</code> such that the first <code>k</code> characters are in the first group, the next <code>k</code> characters are in the second group, and so on. <strong>Note</strong> that the size of the last group can be smaller than <code>k</code>.</li>
	<li><strong>Replace</strong> each group of <code>s</code> with a string representing the sum of all its digits. For example, <code>&quot;346&quot;</code> is replaced with <code>&quot;13&quot;</code> because <code>3 + 4 + 6 = 13</code>.</li>
	<li><strong>Merge</strong> consecutive groups together to form a new string. If the length of the string is greater than <code>k</code>, repeat from step <code>1</code>.</li>
</ol>

<p>Return <code>s</code> <em>after all rounds have been completed</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;11111222223&quot;, k = 3
<strong>Output:</strong> &quot;135&quot;
<strong>Explanation:</strong> 
- For the first round, we divide s into groups of size 3: &quot;111&quot;, &quot;112&quot;, &quot;222&quot;, and &quot;23&quot;.
  ​​​​​Then we calculate the digit sum of each group: 1 + 1 + 1 = 3, 1 + 1 + 2 = 4, 2 + 2 + 2 = 6, and 2 + 3 = 5. 
&nbsp; So, s becomes &quot;3&quot; + &quot;4&quot; + &quot;6&quot; + &quot;5&quot; = &quot;3465&quot; after the first round.
- For the second round, we divide s into &quot;346&quot; and &quot;5&quot;.
&nbsp; Then we calculate the digit sum of each group: 3 + 4 + 6 = 13, 5 = 5. 
&nbsp; So, s becomes &quot;13&quot; + &quot;5&quot; = &quot;135&quot; after second round. 
Now, s.length &lt;= k, so we return &quot;135&quot; as the answer.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;00000000&quot;, k = 3
<strong>Output:</strong> &quot;000&quot;
<strong>Explanation:</strong> 
We divide s into &quot;000&quot;, &quot;000&quot;, and &quot;00&quot;.
Then we calculate the digit sum of each group: 0 + 0 + 0 = 0, 0 + 0 + 0 = 0, and 0 + 0 = 0. 
s becomes &quot;0&quot; + &quot;0&quot; + &quot;0&quot; = &quot;000&quot;, whose length is equal to k, so we return &quot;000&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>2 &lt;= k &lt;= 100</code></li>
	<li><code>s</code> consists of digits only.</li>
</ul>


## Hints

1. Try simulating the entire process to find the final answer.

## ✨ AI-Generated Solution (gemini-3.8-flash)

### Approach

The problem asks us to simulate a process that repeatedly transforms a string of digits until its length is less than or equal to an integer k. In each round of the simulation, we divide the string into consecutive blocks of size k, with the final block possibly being shorter. For each block, we sum the numeric values of its characters, convert the sum into its string representation, and concatenate these representations to form the new string.

We repeat this grouping and summation procedure inside a loop that continues as long as the length of the string strictly exceeds k. Because each group of size k has a digit sum whose string representation has length at most ceil(log10(9k + 1)), which is strictly less than k for any k >= 2 and reasonable group sizes, the string's length decreases strictly in each step after the initial reduction, ensuring quick convergence to a length of at most k.

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
// Generation failed for C++
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
// Generation failed for Java
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
// Generation failed for Python
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
// Generation failed for Python3
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
// Generation failed for C
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
// Generation failed for C#
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
// Generation failed for JavaScript
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function digitSum(s: string, k: number): string {
    while (s.length > k) {
        let nextStr = "";
        for (let i = 0; i < s.length; i += k) {
            let sum = 0;
            const end = Math.min(i + k, s.length);
            for (let j = i; j < end; j++) {
                sum += s.charCodeAt(j) - 48;
            }
            nextStr += sum.toString();
        }
        s = nextStr;
    }
    return s;
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
     * @param Integer $k
     * @return String
     */
    function digitSum($s, $k) {
        while (strlen($s) > $k) {
            $nextStr = "";
            $len = strlen($s);
            for ($i = 0; $i < $len; $i += $k) {
                $sum = 0;
                $end = min($i + $k, $len);
                for ($j = $i; $j < $end; $j++) {
                    $sum += ord($s[$j]) - ord('0');
                }
                $nextStr .= (string)$sum;
            }
            $s = $nextStr;
        }
        return $s;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func digitSum(_ s: String, _ k: Int) -> String {
        var current = Array(s)
        while current.count > k {
            var nextChars: [Character] = []
            var i = 0
            while i < current.count {
                var sum = 0
                let end = min(i + k, current.count)
                for j in i..<end {
                    sum += Int(String(current[j]))!
                }
                nextChars.append(contentsOf: String(sum))
                i += k
            }
            current = nextChars
        }
        return String(current)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun digitSum(s: String, k: Int): String {
        var current = s
        while (current.length > k) {
            val sb = java.lang.StringBuilder()
            var i = 0
            while (i < current.length) {
                var sum = 0
                val end = kotlin.math.min(i + k, current.length)
                for (j in i until end) {
                    sum += current[j] - '0'
                }
                sb.append(sum)
                i += k
            }
            current = sb.toString()
        }
        return current
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  String digitSum(String s, int k) {
    while (s.length > k) {
      StringBuffer sb = StringBuffer();
      for (int i = 0; i < s.length; i += k) {
        int sum = 0;
        int end = (i + k < s.length) ? i + k : s.length;
        for (int j = i; j < end; j++) {
          sum += s.codeUnitAt(j) - 48;
        }
        sb.write(sum.toString());
      }
      s = sb.toString();
    }
    return s;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func digitSum(s string, k int) string {
    for len(s) > k {
        var sb strings.Builder
        for i := 0; i < len(s); i += k {
            sum := 0
            end := i + k
            if end > len(s) {
                end = len(s)
            }
            for j := i; j < end; j++ {
                sum += int(s[j] - '0')
            }
            sb.WriteString(strconv.Itoa(sum))
        }
        s = sb.String()
    }
    return s
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @param {Integer} k
# @return {String}
def digit_sum(s, k)
  while s.length > k
    s = s.chars.each_slice(k).map { |slice| slice.map(&:to_i).sum.to_s }.join
  end
  s
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def digitSum(s: String, k: Int): String = {
        var curr = s
        while (curr.length > k) {
            curr = curr.grouped(k).map(g => g.map(_ - '0').sum.toString).mkString
        }
        curr
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn digit_sum(mut s: String, k: i32) -> String {
        let k = k as usize;
        while s.len() > k {
            let mut next = String::new();
            for chunk in s.as_bytes().chunks(k) {
                let sum: u32 = chunk.iter().map(|&b| (b - b'0') as u32).sum();
                next.push_str(&sum.to_string());
            }
            s = next;
        }
        s
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (digit-sum s k)
  (-> string? exact-integer? string?)
  (if (<= (string-length s) k)
      s
      (let loop ([i 0] [acc '()])
        (if (>= i (string-length s))
            (digit-sum (apply string-append (reverse acc)) k)
            (let* ([end (min (+ i k) (string-length s))]
                   [sub (substring s i end)]
                   [sum (for/sum ([c (in-string sub)]) (- (char->integer c) 48))])
              (loop end (cons (number->string sum) acc)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec digit_sum(S :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
digit_sum(S, K) ->
  case byte_size(S) =< K of
    true -> S;
    false ->
      NewS = process_chunks(S, K, []),
      digit_sum(NewS, K)
  end.

process_chunks(<<>>, _K, Acc) ->
  iolist_to_binary(lists:reverse(Acc));
process_chunks(S, K, Acc) ->
  {Chunk, Rest} = case byte_size(S) =< K of
    true -> {S, <<>>};
    false -> split_binary(S, K)
  end,
  Sum = lists:sum([B - $0 || <<B>> <= Chunk]),
  process_chunks(Rest, K, [integer_to_binary(Sum) | Acc]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec digit_sum(s :: String.t, k :: integer) :: String.t
  def digit_sum(s, k) do
    if String.length(s) <= k do
      s
    else
      s
      |> String.to_charlist()
      |> Enum.chunk_every(k)
      |> Enum.map(fn chunk ->
        chunk
        |> Enum.map(&(&1 - ?0))
        |> Enum.sum()
        |> Integer.to_string()
      end)
      |> Enum.join()
      |> digit_sum(k)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N * log(k)) where N is the initial length of the string. In each round, we iterate through all characters of the current string, and the length shrinks roughly by a factor of k / log10(k), resulting in a logarithmic number of rounds and a total work bounded by a geometric series dominated by the first round.
- **Space Complexity:** O(N) auxiliary space needed to store the intermediate strings and substrings generated during each round of the simulation.
