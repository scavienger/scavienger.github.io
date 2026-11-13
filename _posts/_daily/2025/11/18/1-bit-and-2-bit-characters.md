---
layout: post
title: "1-bit and 2-bit Characters"
date: 2025-11-18 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/1-bit-and-2-bit-characters/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool isOneBitCharacter(vector<int>& bits)\
        \ {\n        int i = 0;\n        while (i < static_cast<int>(bits.size()) -\
        \ 1) {\n            i += bits[i] == 1 ? 2 : 1;\n        }\n        return i\
        \ == static_cast<int>(bits.size()) - 1;\n    }\n};"
      java: "class Solution {\n    public boolean isOneBitCharacter(int[] bits) {\n\
        \        int i = 0;\n        while (i < bits.length - 1) {\n            i +=\
        \ bits[i] == 1 ? 2 : 1;\n        }\n        return i == bits.length - 1;\n \
        \   }\n}"
      python: "class Solution(object):\n    def isOneBitCharacter(self, bits):\n   \
        \     \"\"\"\n        :type bits: List[int]\n        :rtype: bool\n        \"\
        \"\"\n        i = 0\n        while i < len(bits) - 1:\n            i += 2 if\
        \ bits[i] == 1 else 1\n        return i == len(bits) - 1"
      python3: "class Solution:\n    def isOneBitCharacter(self, bits: list[int]) ->\
        \ bool:\n        i = 0\n        while i < len(bits) - 1:\n            i += 2\
        \ if bits[i] == 1 else 1\n        return i == len(bits) - 1"
      c: "bool isOneBitCharacter(int* bits, int bitsSize) {\n    int i = 0;\n    while\
        \ (i < bitsSize - 1) {\n        i += bits[i] == 1 ? 2 : 1;\n    }\n    return\
        \ i == bitsSize - 1;\n}"
      csharp: "public class Solution {\n    public bool IsOneBitCharacter(int[] bits)\
        \ {\n        int i = 0;\n        while (i < bits.Length - 1) {\n           \
        \ i += bits[i] == 1 ? 2 : 1;\n        }\n        return i == bits.Length - 1;\n\
        \    }\n}"
      javascript: "/**\n * @param {number[]} bits\n * @return {boolean}\n */\nvar isOneBitCharacter\
        \ = function(bits) {\n    let i = 0;\n    while (i < bits.length - 1) {\n  \
        \      i += bits[i] === 1 ? 2 : 1;\n    }\n    return i === bits.length - 1;\n\
        };"
      typescript: "function isOneBitCharacter(bits: number[]): boolean {\n    let i\
        \ = 0;\n    while (i < bits.length - 1) {\n        i += bits[i] === 1 ? 2 :\
        \ 1;\n    }\n    return i === bits.length - 1;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $bits\n     * @return\
        \ Boolean\n     */\n    function isOneBitCharacter($bits) {\n        $i = 0;\n\
        \        while ($i < count($bits) - 1) {\n            $i += $bits[$i] === 1\
        \ ? 2 : 1;\n        }\n        return $i === count($bits) - 1;\n    }\n}"
      swift: "class Solution {\n    func isOneBitCharacter(_ bits: [Int]) -> Bool {\n\
        \        var i = 0\n        while i < bits.count - 1 {\n            i += bits[i]\
        \ == 1 ? 2 : 1\n        }\n        return i == bits.count - 1\n    }\n}"
      kotlin: "class Solution {\n    fun isOneBitCharacter(bits: IntArray): Boolean\
        \ {\n        var i = 0\n        while (i < bits.size - 1) {\n            i +=\
        \ if (bits[i] == 1) 2 else 1\n        }\n        return i == bits.size - 1\n\
        \    }\n}"
      dart: "class Solution {\n  bool isOneBitCharacter(List<int> bits) {\n    var i\
        \ = 0;\n    while (i < bits.length - 1) {\n      i += bits[i] == 1 ? 2 : 1;\n\
        \    }\n    return i == bits.length - 1;\n  }\n}"
      go: "func isOneBitCharacter(bits []int) bool {\n    i := 0\n    for i < len(bits)-1\
        \ {\n        if bits[i] == 1 {\n            i += 2\n        } else {\n     \
        \       i++\n        }\n    }\n    return i == len(bits)-1\n}"
      ruby: "# @param {Integer[]} bits\n# @return {Boolean}\ndef is_one_bit_character(bits)\n\
        \  i = 0\n  while i < bits.length - 1\n    i += bits[i] == 1 ? 2 : 1\n  end\n\
        \  i == bits.length - 1\nend"
      scala: "object Solution {\n    def isOneBitCharacter(bits: Array[Int]): Boolean\
        \ = {\n        var i = 0\n        while (i < bits.length - 1) {\n          \
        \  i += (if (bits(i) == 1) 2 else 1)\n        }\n        i == bits.length -\
        \ 1\n    }\n}"
      rust: "impl Solution {\n    pub fn is_one_bit_character(bits: Vec<i32>) -> bool\
        \ {\n        let mut i = 0;\n        while i < bits.len() - 1 {\n          \
        \  i += if bits[i] == 1 { 2 } else { 1 };\n        }\n        i == bits.len()\
        \ - 1\n    }\n}"
      racket: "(define/contract (is-one-bit-character bits)\n  (-> (listof exact-integer?)\
        \ boolean?)\n  (let loop ([i 0])\n    (if (< i (- (length bits) 1))\n      \
        \  (loop (+ i (if (= (list-ref bits i) 1) 2 1)))\n        (= i (- (length bits)\
        \ 1)))))"
      erlang: "-spec is_one_bit_character(Bits :: [integer()]) -> boolean().\nis_one_bit_character(Bits)\
        \ ->\n  is_one_bit_character(Bits, 0, length(Bits) - 1).\n\nis_one_bit_character(Bits,\
        \ I, Last) when I < Last ->\n  Step = case lists:nth(I + 1, Bits) of\n    1\
        \ -> 2;\n    _ -> 1\n  end,\n  is_one_bit_character(Bits, I + Step, Last);\n\
        is_one_bit_character(_Bits, I, Last) ->\n  I =:= Last."
      elixir: "defmodule Solution do\n  @spec is_one_bit_character(bits :: [integer])\
        \ :: boolean\n  def is_one_bit_character(bits) do\n    scan(bits, 0, length(bits)\
        \ - 1)\n  end\n\n  defp scan(bits, i, last) when i < last do\n    step = if\
        \ Enum.at(bits, i) == 1, do: 2, else: 1\n    scan(bits, i + step, last)\n  end\n\
        \n  defp scan(_bits, i, last), do: i == last\nend"
    approach: 'Scan the array from left to right, advancing by two positions when the
      current bit is 1 because it begins a two-bit character, and by one position when
      it is 0 because it is a one-bit character.


      Stop when the scan reaches or passes the final bit. The last character is one-bit
      exactly when the scan lands on the final index.'
    time_complexity: O(n), where n is the length of bits, since each bit is examined
      at most once.
    space_complexity: O(1), since the scan uses only an index.
    elapsed_time: 40.672882080078125
    model: gpt-6-luna
    generated_at: '2026-11-13 00:05:02 '
---

## Problem #717: 1-bit and 2-bit Characters

**Difficulty:** Easy

**Topics:** Array

## Problem Description

<p>We have two special characters:</p>

<ul>
	<li>The first character can be represented by one bit <code>0</code>.</li>
	<li>The second character can be represented by two bits (<code>10</code> or <code>11</code>).</li>
</ul>

<p>Given a binary array <code>bits</code> that ends with <code>0</code>, return <code>true</code> if the last character must be a one-bit character.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> bits = [1,0,0]
<strong>Output:</strong> true
<strong>Explanation:</strong> The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> bits = [1,1,1,0]
<strong>Output:</strong> false
<strong>Explanation:</strong> The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= bits.length &lt;= 1000</code></li>
	<li><code>bits[i]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>


## Hints

1. Keep track of where the next character starts.  At the end, you want to know if you started on the last bit.

## 🤖 AI-Generated Solution (gpt-6-luna)

### Approach

Scan the array from left to right, advancing by two positions when the current bit is 1 because it begins a two-bit character, and by one position when it is 0 because it is a one-bit character.

Stop when the scan reaches or passes the final bit. The last character is one-bit exactly when the scan lands on the final index.

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
    bool isOneBitCharacter(vector<int>& bits) {
        int i = 0;
        while (i < static_cast<int>(bits.size()) - 1) {
            i += bits[i] == 1 ? 2 : 1;
        }
        return i == static_cast<int>(bits.size()) - 1;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        int i = 0;
        while (i < bits.length - 1) {
            i += bits[i] == 1 ? 2 : 1;
        }
        return i == bits.length - 1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(bits) - 1:
            i += 2 if bits[i] == 1 else 1
        return i == len(bits) - 1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        i = 0
        while i < len(bits) - 1:
            i += 2 if bits[i] == 1 else 1
        return i == len(bits) - 1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
bool isOneBitCharacter(int* bits, int bitsSize) {
    int i = 0;
    while (i < bitsSize - 1) {
        i += bits[i] == 1 ? 2 : 1;
    }
    return i == bitsSize - 1;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool IsOneBitCharacter(int[] bits) {
        int i = 0;
        while (i < bits.Length - 1) {
            i += bits[i] == 1 ? 2 : 1;
        }
        return i == bits.Length - 1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} bits
 * @return {boolean}
 */
var isOneBitCharacter = function(bits) {
    let i = 0;
    while (i < bits.length - 1) {
        i += bits[i] === 1 ? 2 : 1;
    }
    return i === bits.length - 1;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function isOneBitCharacter(bits: number[]): boolean {
    let i = 0;
    while (i < bits.length - 1) {
        i += bits[i] === 1 ? 2 : 1;
    }
    return i === bits.length - 1;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $bits
     * @return Boolean
     */
    function isOneBitCharacter($bits) {
        $i = 0;
        while ($i < count($bits) - 1) {
            $i += $bits[$i] === 1 ? 2 : 1;
        }
        return $i === count($bits) - 1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func isOneBitCharacter(_ bits: [Int]) -> Bool {
        var i = 0
        while i < bits.count - 1 {
            i += bits[i] == 1 ? 2 : 1
        }
        return i == bits.count - 1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun isOneBitCharacter(bits: IntArray): Boolean {
        var i = 0
        while (i < bits.size - 1) {
            i += if (bits[i] == 1) 2 else 1
        }
        return i == bits.size - 1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool isOneBitCharacter(List<int> bits) {
    var i = 0;
    while (i < bits.length - 1) {
      i += bits[i] == 1 ? 2 : 1;
    }
    return i == bits.length - 1;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func isOneBitCharacter(bits []int) bool {
    i := 0
    for i < len(bits)-1 {
        if bits[i] == 1 {
            i += 2
        } else {
            i++
        }
    }
    return i == len(bits)-1
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} bits
# @return {Boolean}
def is_one_bit_character(bits)
  i = 0
  while i < bits.length - 1
    i += bits[i] == 1 ? 2 : 1
  end
  i == bits.length - 1
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def isOneBitCharacter(bits: Array[Int]): Boolean = {
        var i = 0
        while (i < bits.length - 1) {
            i += (if (bits(i) == 1) 2 else 1)
        }
        i == bits.length - 1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn is_one_bit_character(bits: Vec<i32>) -> bool {
        let mut i = 0;
        while i < bits.len() - 1 {
            i += if bits[i] == 1 { 2 } else { 1 };
        }
        i == bits.len() - 1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (is-one-bit-character bits)
  (-> (listof exact-integer?) boolean?)
  (let loop ([i 0])
    (if (< i (- (length bits) 1))
        (loop (+ i (if (= (list-ref bits i) 1) 2 1)))
        (= i (- (length bits) 1)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec is_one_bit_character(Bits :: [integer()]) -> boolean().
is_one_bit_character(Bits) ->
  is_one_bit_character(Bits, 0, length(Bits) - 1).

is_one_bit_character(Bits, I, Last) when I < Last ->
  Step = case lists:nth(I + 1, Bits) of
    1 -> 2;
    _ -> 1
  end,
  is_one_bit_character(Bits, I + Step, Last);
is_one_bit_character(_Bits, I, Last) ->
  I =:= Last.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec is_one_bit_character(bits :: [integer]) :: boolean
  def is_one_bit_character(bits) do
    scan(bits, 0, length(bits) - 1)
  end

  defp scan(bits, i, last) when i < last do
    step = if Enum.at(bits, i) == 1, do: 2, else: 1
    scan(bits, i + step, last)
  end

  defp scan(_bits, i, last), do: i == last
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n), where n is the length of bits, since each bit is examined at most once.
- **Space Complexity:** O(1), since the scan uses only an index.
