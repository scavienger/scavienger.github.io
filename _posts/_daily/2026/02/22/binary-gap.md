---
layout: post
title: "Binary Gap"
date: 2026-02-22 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Bit Manipulation"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/binary-gap/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int binaryGap(int n) {\n        int maxGap\
        \ = 0;\n        int lastPos = -1;\n        int currentPos = 0;\n        while\
        \ (n > 0) {\n            if (n & 1) {\n                if (lastPos != -1) {\n\
        \                    maxGap = std::max(maxGap, currentPos - lastPos);\n    \
        \            }\n                lastPos = currentPos;\n            }\n     \
        \       n >>= 1;\n            currentPos++;\n        }\n        return maxGap;\n\
        \    }\n};"
      java: "class Solution {\n    public int binaryGap(int n) {\n        int maxGap\
        \ = 0;\n        int lastPos = -1;\n        int currentPos = 0;\n        while\
        \ (n > 0) {\n            if ((n & 1) == 1) {\n                if (lastPos !=\
        \ -1) {\n                    maxGap = Math.max(maxGap, currentPos - lastPos);\n\
        \                }\n                lastPos = currentPos;\n            }\n \
        \           n >>= 1;\n            currentPos++;\n        }\n        return maxGap;\n\
        \    }\n}"
      python: "class Solution(object):\n    def binaryGap(self, n):\n        \"\"\"\n\
        \        :type n: int\n        :rtype: int\n        \"\"\"\n        max_gap\
        \ = 0\n        last_pos = -1\n        current_pos = 0\n        while n > 0:\n\
        \            if n & 1:\n                if last_pos != -1:\n               \
        \     max_gap = max(max_gap, current_pos - last_pos)\n                last_pos\
        \ = current_pos\n            n >>= 1\n            current_pos += 1\n       \
        \ return max_gap"
      python3: "class Solution:\n    def binaryGap(self, n: int) -> int:\n        max_gap\
        \ = 0\n        last_pos = -1\n        current_pos = 0\n        while n > 0:\n\
        \            if n & 1:\n                if last_pos != -1:\n               \
        \     max_gap = max(max_gap, current_pos - last_pos)\n                last_pos\
        \ = current_pos\n            n >>= 1\n            current_pos += 1\n       \
        \ return max_gap"
      c: "int binaryGap(int n) {\n    int maxGap = 0;\n    int lastPos = -1;\n    int\
        \ currentPos = 0;\n    while (n > 0) {\n        if (n & 1) {\n            if\
        \ (lastPos != -1) {\n                int gap = currentPos - lastPos;\n     \
        \           if (gap > maxGap) maxGap = gap;\n            }\n            lastPos\
        \ = currentPos;\n        }\n        n >>= 1;\n        currentPos++;\n    }\n\
        \    return maxGap;\n}"
      csharp: "public class Solution {\n    public int BinaryGap(int n) {\n        int\
        \ maxGap = 0;\n        int lastPos = -1;\n        int currentPos = 0;\n    \
        \    while (n > 0) {\n            if ((n & 1) == 1) {\n                if (lastPos\
        \ != -1) {\n                    maxGap = System.Math.Max(maxGap, currentPos\
        \ - lastPos);\n                }\n                lastPos = currentPos;\n  \
        \          }\n            n >>= 1;\n            currentPos++;\n        }\n \
        \       return maxGap;\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @return {number}\n */\nvar binaryGap\
        \ = function(n) {\n    let maxGap = 0;\n    let lastPos = -1;\n    let currentPos\
        \ = 0;\n    while (n > 0) {\n        if (n & 1) {\n            if (lastPos !==\
        \ -1) {\n                maxGap = Math.max(maxGap, currentPos - lastPos);\n\
        \            }\n            lastPos = currentPos;\n        }\n        n >>=\
        \ 1;\n        currentPos++;\n    }\n    return maxGap;\n};"
      typescript: "function binaryGap(n: number): number {\n    let maxGap = 0;\n  \
        \  let lastPos = -1;\n    let currentPos = 0;\n    while (n > 0) {\n       \
        \ if (n % 2 === 1) {\n            if (lastPos !== -1) {\n                if\
        \ (currentPos - lastPos > maxGap) {\n                    maxGap = currentPos\
        \ - lastPos;\n                }\n            }\n            lastPos = currentPos;\n\
        \        }\n        n = Math.floor(n / 2);\n        currentPos++;\n    }\n \
        \   return maxGap;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @return Integer\n\
        \     */\n    function binaryGap($n) {\n        $maxGap = 0;\n        $lastPos\
        \ = -1;\n        $currentPos = 0;\n        while ($n > 0) {\n            if\
        \ ($n % 2 == 1) {\n                if ($lastPos != -1) {\n                 \
        \   $dist = $currentPos - $lastPos;\n                    if ($dist > $maxGap)\
        \ {\n                        $maxGap = $dist;\n                    }\n     \
        \           }\n                $lastPos = $currentPos;\n            }\n    \
        \        $n = (int)($n / 2);\n            $currentPos++;\n        }\n      \
        \  return $maxGap;\n    }\n}"
      swift: "class Solution {\n    func binaryGap(_ n: Int) -> Int {\n        var maxGap\
        \ = 0\n        var lastPos = -1\n        var currentPos = 0\n        var n =\
        \ n\n        while n > 0 {\n            if n % 2 == 1 {\n                if\
        \ lastPos != -1 {\n                    maxGap = max(maxGap, currentPos - lastPos)\n\
        \                }\n                lastPos = currentPos\n            }\n  \
        \          n /= 2\n            currentPos += 1\n        }\n        return maxGap\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun binaryGap(n: Int): Int {\n        var maxGap\
        \ = 0\n        var lastPos = -1\n        var currentPos = 0\n        var tempN\
        \ = n\n        while (tempN > 0) {\n            if (tempN % 2 == 1) {\n    \
        \            if (lastPos != -1) {\n                    val dist = currentPos\
        \ - lastPos\n                    if (dist > maxGap) {\n                    \
        \    maxGap = dist\n                    }\n                }\n             \
        \   lastPos = currentPos\n            }\n            tempN /= 2\n          \
        \  currentPos++\n        }\n        return maxGap\n    }\n}"
      dart: "class Solution {\n  int binaryGap(int n) {\n    int maxGap = 0;\n    int\
        \ lastPos = -1;\n    int currentPos = 0;\n    while (n > 0) {\n      if (n %\
        \ 2 == 1) {\n        if (lastPos != -1) {\n          int gap = currentPos -\
        \ lastPos;\n          if (gap > maxGap) {\n            maxGap = gap;\n     \
        \     }\n        }\n        lastPos = currentPos;\n      }\n      n ~/= 2;\n\
        \      currentPos++;\n    }\n    return maxGap;\n  }\n}"
      go: "func binaryGap(n int) int {\n    maxGap := 0\n    lastPos := -1\n    currentPos\
        \ := 0\n    for n > 0 {\n        if n%2 == 1 {\n            if lastPos != -1\
        \ {\n                if currentPos-lastPos > maxGap {\n                    maxGap\
        \ = currentPos - lastPos\n                }\n            }\n            lastPos\
        \ = currentPos\n        }\n        n /= 2\n        currentPos++\n    }\n   \
        \ return maxGap\n}"
      ruby: "def binary_gap(n)\n  max_dist = 0\n  last_pos = -1\n  current_pos = 0\n\
        \  temp = n\n  while temp > 0\n    if temp % 2 == 1\n      if last_pos != -1\n\
        \        dist = current_pos - last_pos\n        max_dist = dist if dist > max_dist\n\
        \      end\n      last_pos = current_pos\n    end\n    temp /= 2\n    current_pos\
        \ += 1\n  end\n  max_dist\nend"
      scala: "object Solution {\n    def binaryGap(n: Int): Int = {\n        var maxDist\
        \ = 0\n        var lastPos = -1\n        var currentPos = 0\n        var temp\
        \ = n\n        while (temp > 0) {\n            if ((temp & 1) == 1) {\n    \
        \            if (lastPos != -1) {\n                    maxDist = Math.max(maxDist,\
        \ currentPos - lastPos)\n                }\n                lastPos = currentPos\n\
        \            }\n            temp >>= 1\n            currentPos += 1\n      \
        \  }\n        maxDist\n    }\n}"
      rust: "impl Solution {\n    pub fn binary_gap(n: i32) -> i32 {\n        let mut\
        \ max_dist = 0;\n        let mut last_pos: i32 = -1;\n        let mut current_pos\
        \ = 0;\n        let mut temp = n;\n        while temp > 0 {\n            if\
        \ (temp & 1) == 1 {\n                if last_pos != -1 {\n                 \
        \   max_dist = max_dist.max(current_pos - last_pos);\n                }\n  \
        \              last_pos = current_pos;\n            }\n            temp >>=\
        \ 1;\n            current_pos += 1;\n        }\n        max_dist\n    }\n}"
      racket: "(define/contract (binary-gap n)\n  (-> exact-integer? exact-integer?)\n\
        \  (let loop ([n n] [pos 0] [last -1] [max-dist 0])\n    (cond\n      [(= n\
        \ 0) max-dist]\n      [(= (remainder n 2) 1)\n       (loop (quotient n 2) (+\
        \ pos 1) pos (if (= last -1) max-dist (max max-dist (- pos last))))]\n     \
        \ [else\n       (loop (quotient n 2) (+ pos 1) last max-dist)])))"
      erlang: "-spec binary_gap(N :: integer()) -> integer().\nbinary_gap(N) ->\n  find_gap(N,\
        \ 0, -1, 0).\n\nfind_gap(0, _, _, MaxDist) -> MaxDist;\nfind_gap(N, Pos, Last,\
        \ MaxDist) ->\n  case N rem 2 of\n    1 ->\n      NewMax = if Last =:= -1 ->\
        \ MaxDist; true -> erlang:max(MaxDist, Pos - Last) end,\n      find_gap(N div\
        \ 2, Pos + 1, Pos, NewMax);\n    0 ->\n      find_gap(N div 2, Pos + 1, Last,\
        \ MaxDist)\n  end."
      elixir: "defmodule Solution do\n  @spec binary_gap(n :: integer) :: integer\n\
        \  def binary_gap(n) do\n    find_gap(n, 0, -1, 0)\n  end\n\n  defp find_gap(0,\
        \ _pos, _last, max_dist), do: max_dist\n  defp find_gap(n, pos, last, max_dist)\
        \ do\n    if rem(n, 2) == 1 do\n      new_max = if last == -1, do: max_dist,\
        \ else: max(max_dist, pos - last)\n      find_gap(div(n, 2), pos + 1, pos, new_max)\n\
        \    else\n      find_gap(div(n, 2), pos + 1, last, max_dist)\n    end\n  end\n\
        end"
    approach: 'The algorithm processes the binary representation of the integer n bit
      by bit from right to left using bitwise operations. We maintain a variable to
      track the position of the last seen ''1'' bit and a variable to store the maximum
      gap found. As we iterate through each bit position, we check if the current bit
      is 1. If it is and we have previously encountered a ''1'', we calculate the distance
      between the current bit position and the previous position and update our maximum
      gap accordingly.


      This approach effectively identifies all adjacent pairs of 1''s because we only
      update the ''last seen'' position when a new 1 is found, ensuring the distance
      calculated is always between the two closest set bits. The loop terminates once
      all bits in n have been shifted out. Since n is shifted right by one in each iteration,
      the complexity is directly proportional to the number of bits in n.'
    time_complexity: O(log n). The number of iterations in the loop corresponds to the
      number of bits required to represent n in binary, which is approximately log2(n).
    space_complexity: O(1). The solution uses a constant amount of extra space to store
      the current position, the last seen position, and the maximum gap found.
    elapsed_time: 124.81092047691345
    model: gemini-3-flash-preview
    generated_at: '2026-02-22 01:27:52 '
---

## Problem #868: Binary Gap

**Difficulty:** Easy

**Topics:** Bit Manipulation

## Problem Description

<p>Given a positive integer <code>n</code>, find and return <em>the <strong>longest distance</strong> between any two <strong>adjacent</strong> </em><code>1</code><em>&#39;s in the binary representation of </em><code>n</code><em>. If there are no two adjacent </em><code>1</code><em>&#39;s, return </em><code>0</code><em>.</em></p>

<p>Two <code>1</code>&#39;s are <strong>adjacent</strong> if there are only <code>0</code>&#39;s separating them (possibly no <code>0</code>&#39;s). The <b>distance</b> between two <code>1</code>&#39;s is the absolute difference between their bit positions. For example, the two <code>1</code>&#39;s in <code>&quot;1001&quot;</code> have a distance of 3.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 22
<strong>Output:</strong> 2
<strong>Explanation:</strong> 22 in binary is &quot;10110&quot;.
The first adjacent pair of 1&#39;s is &quot;<u>1</u>0<u>1</u>10&quot; with a distance of 2.
The second adjacent pair of 1&#39;s is &quot;10<u>11</u>0&quot; with a distance of 1.
The answer is the largest of these two distances, which is 2.
Note that &quot;<u>1</u>01<u>1</u>0&quot; is not a valid pair since there is a 1 separating the two 1&#39;s underlined.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 8
<strong>Output:</strong> 0
<strong>Explanation:</strong> 8 in binary is &quot;1000&quot;.
There are not any adjacent pairs of 1&#39;s in the binary representation of 8, so we return 0.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> 2
<strong>Explanation:</strong> 5 in binary is &quot;101&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm processes the binary representation of the integer n bit by bit from right to left using bitwise operations. We maintain a variable to track the position of the last seen '1' bit and a variable to store the maximum gap found. As we iterate through each bit position, we check if the current bit is 1. If it is and we have previously encountered a '1', we calculate the distance between the current bit position and the previous position and update our maximum gap accordingly.

This approach effectively identifies all adjacent pairs of 1's because we only update the 'last seen' position when a new 1 is found, ensuring the distance calculated is always between the two closest set bits. The loop terminates once all bits in n have been shifted out. Since n is shifted right by one in each iteration, the complexity is directly proportional to the number of bits in n.

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
    int binaryGap(int n) {
        int maxGap = 0;
        int lastPos = -1;
        int currentPos = 0;
        while (n > 0) {
            if (n & 1) {
                if (lastPos != -1) {
                    maxGap = std::max(maxGap, currentPos - lastPos);
                }
                lastPos = currentPos;
            }
            n >>= 1;
            currentPos++;
        }
        return maxGap;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int binaryGap(int n) {
        int maxGap = 0;
        int lastPos = -1;
        int currentPos = 0;
        while (n > 0) {
            if ((n & 1) == 1) {
                if (lastPos != -1) {
                    maxGap = Math.max(maxGap, currentPos - lastPos);
                }
                lastPos = currentPos;
            }
            n >>= 1;
            currentPos++;
        }
        return maxGap;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        max_gap = 0
        last_pos = -1
        current_pos = 0
        while n > 0:
            if n & 1:
                if last_pos != -1:
                    max_gap = max(max_gap, current_pos - last_pos)
                last_pos = current_pos
            n >>= 1
            current_pos += 1
        return max_gap
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def binaryGap(self, n: int) -> int:
        max_gap = 0
        last_pos = -1
        current_pos = 0
        while n > 0:
            if n & 1:
                if last_pos != -1:
                    max_gap = max(max_gap, current_pos - last_pos)
                last_pos = current_pos
            n >>= 1
            current_pos += 1
        return max_gap
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int binaryGap(int n) {
    int maxGap = 0;
    int lastPos = -1;
    int currentPos = 0;
    while (n > 0) {
        if (n & 1) {
            if (lastPos != -1) {
                int gap = currentPos - lastPos;
                if (gap > maxGap) maxGap = gap;
            }
            lastPos = currentPos;
        }
        n >>= 1;
        currentPos++;
    }
    return maxGap;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int BinaryGap(int n) {
        int maxGap = 0;
        int lastPos = -1;
        int currentPos = 0;
        while (n > 0) {
            if ((n & 1) == 1) {
                if (lastPos != -1) {
                    maxGap = System.Math.Max(maxGap, currentPos - lastPos);
                }
                lastPos = currentPos;
            }
            n >>= 1;
            currentPos++;
        }
        return maxGap;
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
 * @return {number}
 */
var binaryGap = function(n) {
    let maxGap = 0;
    let lastPos = -1;
    let currentPos = 0;
    while (n > 0) {
        if (n & 1) {
            if (lastPos !== -1) {
                maxGap = Math.max(maxGap, currentPos - lastPos);
            }
            lastPos = currentPos;
        }
        n >>= 1;
        currentPos++;
    }
    return maxGap;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function binaryGap(n: number): number {
    let maxGap = 0;
    let lastPos = -1;
    let currentPos = 0;
    while (n > 0) {
        if (n % 2 === 1) {
            if (lastPos !== -1) {
                if (currentPos - lastPos > maxGap) {
                    maxGap = currentPos - lastPos;
                }
            }
            lastPos = currentPos;
        }
        n = Math.floor(n / 2);
        currentPos++;
    }
    return maxGap;
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
     * @return Integer
     */
    function binaryGap($n) {
        $maxGap = 0;
        $lastPos = -1;
        $currentPos = 0;
        while ($n > 0) {
            if ($n % 2 == 1) {
                if ($lastPos != -1) {
                    $dist = $currentPos - $lastPos;
                    if ($dist > $maxGap) {
                        $maxGap = $dist;
                    }
                }
                $lastPos = $currentPos;
            }
            $n = (int)($n / 2);
            $currentPos++;
        }
        return $maxGap;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func binaryGap(_ n: Int) -> Int {
        var maxGap = 0
        var lastPos = -1
        var currentPos = 0
        var n = n
        while n > 0 {
            if n % 2 == 1 {
                if lastPos != -1 {
                    maxGap = max(maxGap, currentPos - lastPos)
                }
                lastPos = currentPos
            }
            n /= 2
            currentPos += 1
        }
        return maxGap
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun binaryGap(n: Int): Int {
        var maxGap = 0
        var lastPos = -1
        var currentPos = 0
        var tempN = n
        while (tempN > 0) {
            if (tempN % 2 == 1) {
                if (lastPos != -1) {
                    val dist = currentPos - lastPos
                    if (dist > maxGap) {
                        maxGap = dist
                    }
                }
                lastPos = currentPos
            }
            tempN /= 2
            currentPos++
        }
        return maxGap
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int binaryGap(int n) {
    int maxGap = 0;
    int lastPos = -1;
    int currentPos = 0;
    while (n > 0) {
      if (n % 2 == 1) {
        if (lastPos != -1) {
          int gap = currentPos - lastPos;
          if (gap > maxGap) {
            maxGap = gap;
          }
        }
        lastPos = currentPos;
      }
      n ~/= 2;
      currentPos++;
    }
    return maxGap;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func binaryGap(n int) int {
    maxGap := 0
    lastPos := -1
    currentPos := 0
    for n > 0 {
        if n%2 == 1 {
            if lastPos != -1 {
                if currentPos-lastPos > maxGap {
                    maxGap = currentPos - lastPos
                }
            }
            lastPos = currentPos
        }
        n /= 2
        currentPos++
    }
    return maxGap
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def binary_gap(n)
  max_dist = 0
  last_pos = -1
  current_pos = 0
  temp = n
  while temp > 0
    if temp % 2 == 1
      if last_pos != -1
        dist = current_pos - last_pos
        max_dist = dist if dist > max_dist
      end
      last_pos = current_pos
    end
    temp /= 2
    current_pos += 1
  end
  max_dist
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def binaryGap(n: Int): Int = {
        var maxDist = 0
        var lastPos = -1
        var currentPos = 0
        var temp = n
        while (temp > 0) {
            if ((temp & 1) == 1) {
                if (lastPos != -1) {
                    maxDist = Math.max(maxDist, currentPos - lastPos)
                }
                lastPos = currentPos
            }
            temp >>= 1
            currentPos += 1
        }
        maxDist
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn binary_gap(n: i32) -> i32 {
        let mut max_dist = 0;
        let mut last_pos: i32 = -1;
        let mut current_pos = 0;
        let mut temp = n;
        while temp > 0 {
            if (temp & 1) == 1 {
                if last_pos != -1 {
                    max_dist = max_dist.max(current_pos - last_pos);
                }
                last_pos = current_pos;
            }
            temp >>= 1;
            current_pos += 1;
        }
        max_dist
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (binary-gap n)
  (-> exact-integer? exact-integer?)
  (let loop ([n n] [pos 0] [last -1] [max-dist 0])
    (cond
      [(= n 0) max-dist]
      [(= (remainder n 2) 1)
       (loop (quotient n 2) (+ pos 1) pos (if (= last -1) max-dist (max max-dist (- pos last))))]
      [else
       (loop (quotient n 2) (+ pos 1) last max-dist)])))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec binary_gap(N :: integer()) -> integer().
binary_gap(N) ->
  find_gap(N, 0, -1, 0).

find_gap(0, _, _, MaxDist) -> MaxDist;
find_gap(N, Pos, Last, MaxDist) ->
  case N rem 2 of
    1 ->
      NewMax = if Last =:= -1 -> MaxDist; true -> erlang:max(MaxDist, Pos - Last) end,
      find_gap(N div 2, Pos + 1, Pos, NewMax);
    0 ->
      find_gap(N div 2, Pos + 1, Last, MaxDist)
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec binary_gap(n :: integer) :: integer
  def binary_gap(n) do
    find_gap(n, 0, -1, 0)
  end

  defp find_gap(0, _pos, _last, max_dist), do: max_dist
  defp find_gap(n, pos, last, max_dist) do
    if rem(n, 2) == 1 do
      new_max = if last == -1, do: max_dist, else: max(max_dist, pos - last)
      find_gap(div(n, 2), pos + 1, pos, new_max)
    else
      find_gap(div(n, 2), pos + 1, last, max_dist)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(log n). The number of iterations in the loop corresponds to the number of bits required to represent n in binary, which is approximately log2(n).
- **Space Complexity:** O(1). The solution uses a constant amount of extra space to store the current position, the last seen position, and the maximum gap found.
