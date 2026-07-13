---
layout: post
title: "Sequential Digits"
date: 2026-07-13 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Enumeration"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/sequential-digits/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <algorithm>\n\nclass Solution {\npublic:\n \
        \   std::vector<int> sequentialDigits(int low, int high) {\n        std::vector<int>\
        \ result;\n        for (int length = 2; length <= 9; ++length) {\n         \
        \   for (int start = 1; start <= 10 - length; ++start) {\n                int\
        \ num = 0;\n                for (int i = 0; i < length; ++i) {\n           \
        \         num = num * 10 + (start + i);\n                }\n               \
        \ if (num >= low && num <= high) {\n                    result.push_back(num);\n\
        \                }\n            }\n        }\n        return result;\n    }\n\
        };"
      java: "import java.util.ArrayList;\nimport java.util.List;\nimport java.util.Collections;\n\
        \nclass Solution {\n    public List<Integer> sequentialDigits(int low, int high)\
        \ {\n        List<Integer> result = new ArrayList<>();\n        for (int length\
        \ = 2; length <= 9; length++) {\n            for (int start = 1; start <= 10\
        \ - length; start++) {\n                int num = 0;\n                for (int\
        \ i = 0; i < length; i++) {\n                    num = num * 10 + (start + i);\n\
        \                }\n                if (num >= low && num <= high) {\n     \
        \               result.add(num);\n                }\n            }\n       \
        \ }\n        return result;\n    }\n}"
      python: "class Solution(object):\n    def sequentialDigits(self, low, high):\n\
        \        \"\"\"\n        :type low: int\n        :type high: int\n        :rtype:\
        \ List[int]\n        \"\"\"\n        result = []\n        for length in range(2,\
        \ 10):\n            for start in range(1, 11 - length):\n                num\
        \ = 0\n                for i in range(length):\n                    num = num\
        \ * 10 + (start + i)\n                if low <= num <= high:\n             \
        \       result.append(num)\n        return result"
      python3: "from typing import List\n\nclass Solution:\n    def sequentialDigits(self,\
        \ low: int, high: int) -> List[int]:\n        result = []\n        for length\
        \ in range(2, 10):\n            for start in range(1, 11 - length):\n      \
        \          num = 0\n                for i in range(length):\n              \
        \      num = num * 10 + (start + i)\n                if low <= num <= high:\n\
        \                    result.append(num)\n        return result"
      c: "#include <stdlib.h>\n\n/**\n * Note: The returned array must be malloced,\
        \ assume caller calls free().\n */\nint* sequentialDigits(int low, int high,\
        \ int* returnSize) {\n    int* result = (int*)malloc(40 * sizeof(int));\n  \
        \  int count = 0;\n    for (int length = 2; length <= 9; length++) {\n     \
        \   for (int start = 1; start <= 10 - length; start++) {\n            int num\
        \ = 0;\n            for (int i = 0; i < length; i++) {\n                num\
        \ = num * 10 + (start + i);\n            }\n            if (num >= low && num\
        \ <= high) {\n                result[count++] = num;\n            }\n      \
        \  }\n    }\n    *returnSize = count;\n    return result;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public IList<int> SequentialDigits(int low, int high) {\n        List<int>\
        \ result = new List<int>();\n        string digits = \"123456789\";\n      \
        \  for (int len = 2; len <= 9; len++) {\n            for (int i = 0; i <= 9\
        \ - len; i++) {\n                int num = int.Parse(digits.Substring(i, len));\n\
        \                if (num >= low && num <= high) {\n                    result.Add(num);\n\
        \                }\n            }\n        }\n        return result;\n    }\n\
        }"
      javascript: "/**\n * @param {number} low\n * @param {number} high\n * @return\
        \ {number[]}\n */\nvar sequentialDigits = function(low, high) {\n    const result\
        \ = [];\n    const digits = \"123456789\";\n    for (let len = 2; len <= 9;\
        \ len++) {\n        for (let i = 0; i <= 9 - len; i++) {\n            const\
        \ num = parseInt(digits.substring(i, i + len));\n            if (num >= low\
        \ && num <= high) {\n                result.push(num);\n            }\n    \
        \    }\n    }\n    return result;\n};"
      typescript: "function sequentialDigits(low: number, high: number): number[] {\n\
        \    const result: number[] = [];\n    const digits = \"123456789\";\n    for\
        \ (let len = 2; len <= 9; len++) {\n        for (let i = 0; i <= 9 - len; i++)\
        \ {\n            const num = parseInt(digits.substring(i, i + len));\n     \
        \       if (num >= low && num <= high) {\n                result.push(num);\n\
        \            }\n        }\n    }\n    return result;\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer $low\n     * @param Integer\
        \ $high\n     * @return Integer[]\n     */\n    function sequentialDigits($low,\
        \ $high) {\n        $result = [];\n        $digits = \"123456789\";\n      \
        \  for ($len = 2; $len <= 9; $len++) {\n            for ($i = 0; $i <= 9 - $len;\
        \ $i++) {\n                $num = (int)substr($digits, $i, $len);\n        \
        \        if ($num >= $low && $num <= $high) {\n                    $result[]\
        \ = $num;\n                }\n            }\n        }\n        return $result;\n\
        \    }\n}"
      swift: "class Solution {\n    func sequentialDigits(_ low: Int, _ high: Int) ->\
        \ [Int] {\n        var result = [Int]()\n        let digits = \"123456789\"\n\
        \        let digitsArray = Array(digits)\n        for length in 2...9 {\n  \
        \          for i in 0...(9 - length) {\n                let subStr = String(digitsArray[i..<(i\
        \ + length)])\n                if let num = Int(subStr) {\n                \
        \    if num >= low && num <= high {\n                        result.append(num)\n\
        \                    }\n                }\n            }\n        }\n      \
        \  return result\n    }\n}"
      kotlin: "class Solution {\n    fun sequentialDigits(low: Int, high: Int): List<Int>\
        \ {\n        val result = mutableListOf<Int>()\n        for (len in 2..9) {\n\
        \            for (start in 1..10 - len) {\n                var num = 0\n   \
        \             for (i in 0 until len) {\n                    num = num * 10 +\
        \ (start + i)\n                }\n                if (num in low..high) {\n\
        \                    result.add(num)\n                }\n            }\n   \
        \     }\n        return result\n    }\n}"
      dart: "class Solution {\n  List<int> sequentialDigits(int low, int high) {\n \
        \   List<int> result = [];\n    for (int len = 2; len <= 9; len++) {\n     \
        \ for (int start = 1; start <= 10 - len; start++) {\n        int num = 0;\n\
        \        for (int i = 0; i < len; i++) {\n          num = num * 10 + (start\
        \ + i);\n        }\n        if (num >= low && num <= high) {\n          result.add(num);\n\
        \        }\n      }\n    }\n    return result;\n  }\n}"
      go: "func sequentialDigits(low int, high int) []int {\n    res := []int{}\n  \
        \  for length := 2; length <= 9; length++ {\n        for start := 1; start <=\
        \ 10-length; start++ {\n            num := 0\n            for i := 0; i < length;\
        \ i++ {\n                num = num*10 + (start + i)\n            }\n       \
        \     if num >= low && num <= high {\n                res = append(res, num)\n\
        \            }\n        }\n    }\n    return res\n}"
      ruby: "# @param {Integer} low\n# @param {Integer} high\n# @return {Integer[]}\n\
        def sequential_digits(low, high)\n  res = []\n  (2..9).each do |len|\n    (1..10\
        \ - len).each do |start|\n      num = 0\n      (0...len).each do |i|\n     \
        \   num = num * 10 + (start + i)\n      end\n      res << num if num >= low\
        \ && num <= high\n    end\n  end\n  res\nend"
      scala: "object Solution {\n    def sequentialDigits(low: Int, high: Int): List<Int>\
        \ = {\n        import scala.collection.mutable.ListBuffer\n        val res =\
        \ ListBuffer[Int]()\n        for (len <- 2 to 9) {\n            for (start <-\
        \ 1 to 10 - len) {\n                var num = 0\n                for (i <- 0\
        \ until len) {\n                    num = num * 10 + (start + i)\n         \
        \       }\n                if (num >= low && num <= high) {\n              \
        \      res += num\n                }\n            }\n        }\n        res.toList\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn sequential_digits(low: i32, high: i32) -> Vec<i32>\
        \ {\n        let s = \"123456789\";\n        let mut results = Vec::new();\n\
        \        for len in 2..10 {\n            for start in 0..=(9 - len) {\n    \
        \            if let Ok(num) = s[start..start + len].parse::<i32>() {\n     \
        \               if num >= low && num <= high {\n                        results.push(num);\n\
        \                    }\n                }\n            }\n        }\n      \
        \  results.sort();\n        results\n    }\n}"
      racket: "(define/contract (sequential-digits low high)\n  (-> exact-integer? exact-integer?\
        \ (listof exact-integer?))\n  (let* ([s \"123456789\"]\n         [nums (for*/list\
        \ ([len (in-range 2 10)]\n                           [start (in-range 0 (- 10\
        \ len))])\n                 (string->number (substring s start (+ start len))))])\n\
        \    (sort (filter (lambda (n) (and (>= n low) (<= n high))) nums) <)))"
      erlang: "-spec sequential_digits(Low :: integer(), High :: integer()) -> [integer()].\n\
        sequential_digits(Low, High) ->\n  S = \"123456789\",\n  Nums = [list_to_integer(lists:sublist(S,\
        \ Start, Len))\n          || Len <- lists:seq(2, 9),\n             Start <-\
        \ lists:seq(1, 10 - Len)],\n  Filtered = [N || N <- Nums, N >= Low, N =< High],\n\
        \  lists:sort(Filtered)."
      elixir: "defmodule Solution do\n  @spec sequential_digits(low :: integer, high\
        \ :: integer) :: [integer]\n  def sequential_digits(low, high) do\n    s = \"\
        123456789\"\n    for len <- 2..9,\n        start <- 0..(9 - len) do\n      String.slice(s,\
        \ start, len) |> String.to_integer()\n    end\n    |> Enum.filter(fn n -> n\
        \ >= low and n <= high end)\n    |> Enum.sort()\n  end\nend"
    approach: 'To identify all sequential digit integers within the range [low, high],
      we can systematically generate all such numbers and filter for those that satisfy
      the range condition. Since a sequential number is defined by each digit being
      exactly one greater than its predecessor, the maximum length of such a number
      is 9 (specifically, the integer 123,456,789). We can iterate through every possible
      length from 2 to 9 and every possible starting digit from 1 to $10 - length$ to
      construct these numbers in a nested loop.


      By generating numbers length by length and then by start digit, the resulting
      integers are naturally produced in increasing order. For each candidate number,
      we check if it falls within the inclusive range [low, high] and, if so, add it
      to our collection. This strategy is efficient and robust, as the total pool of
      sequential digit integers is extremely small, containing only 36 candidates in
      the range [10, 10^9].'
    time_complexity: O(1). Since the maximum possible number is $10^9$, there are only
      36 sequential digit numbers to consider (those of lengths 2 through 9). The algorithm
      iterates through these fixed number of possibilities, checking each against the
      range bounds, resulting in a constant time complexity regardless of the input
      values.
    space_complexity: O(1). The result list stores at most 36 integers, and no additional
      data structures that grow with input size are used. The memory used for generating
      and filtering the sequential digits remains constant.
    elapsed_time: 140.30934691429138
    model: gemini-3-flash-preview
    generated_at: '2026-07-13 02:04:00 '
---

## Problem #1291: Sequential Digits

**Difficulty:** Medium

**Topics:** Enumeration

## Problem Description

<p>An&nbsp;integer has <em>sequential digits</em> if and only if each digit in the number is one more than the previous digit.</p>

<p>Return a <strong>sorted</strong> list of all the integers&nbsp;in the range <code>[low, high]</code>&nbsp;inclusive that have sequential digits.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> low = 100, high = 300
<strong>Output:</strong> [123,234]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> low = 1000, high = 13000
<strong>Output:</strong> [1234,2345,3456,4567,5678,6789,12345]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>10 &lt;= low &lt;= high &lt;= 10^9</code></li>
</ul>


## Hints

1. Generate all numbers with sequential digits and check if they are in the given range.

2. Fix the starting digit then do a recursion that tries to append all valid digits.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To identify all sequential digit integers within the range [low, high], we can systematically generate all such numbers and filter for those that satisfy the range condition. Since a sequential number is defined by each digit being exactly one greater than its predecessor, the maximum length of such a number is 9 (specifically, the integer 123,456,789). We can iterate through every possible length from 2 to 9 and every possible starting digit from 1 to $10 - length$ to construct these numbers in a nested loop.

By generating numbers length by length and then by start digit, the resulting integers are naturally produced in increasing order. For each candidate number, we check if it falls within the inclusive range [low, high] and, if so, add it to our collection. This strategy is efficient and robust, as the total pool of sequential digit integers is extremely small, containing only 36 candidates in the range [10, 10^9].

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
#include <algorithm>

class Solution {
public:
    std::vector<int> sequentialDigits(int low, int high) {
        std::vector<int> result;
        for (int length = 2; length <= 9; ++length) {
            for (int start = 1; start <= 10 - length; ++start) {
                int num = 0;
                for (int i = 0; i < length; ++i) {
                    num = num * 10 + (start + i);
                }
                if (num >= low && num <= high) {
                    result.push_back(num);
                }
            }
        }
        return result;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.ArrayList;
import java.util.List;
import java.util.Collections;

class Solution {
    public List<Integer> sequentialDigits(int low, int high) {
        List<Integer> result = new ArrayList<>();
        for (int length = 2; length <= 9; length++) {
            for (int start = 1; start <= 10 - length; start++) {
                int num = 0;
                for (int i = 0; i < length; i++) {
                    num = num * 10 + (start + i);
                }
                if (num >= low && num <= high) {
                    result.add(num);
                }
            }
        }
        return result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        result = []
        for length in range(2, 10):
            for start in range(1, 11 - length):
                num = 0
                for i in range(length):
                    num = num * 10 + (start + i)
                if low <= num <= high:
                    result.append(num)
        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        for length in range(2, 10):
            for start in range(1, 11 - length):
                num = 0
                for i in range(length):
                    num = num * 10 + (start + i)
                if low <= num <= high:
                    result.append(num)
        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sequentialDigits(int low, int high, int* returnSize) {
    int* result = (int*)malloc(40 * sizeof(int));
    int count = 0;
    for (int length = 2; length <= 9; length++) {
        for (int start = 1; start <= 10 - length; start++) {
            int num = 0;
            for (int i = 0; i < length; i++) {
                num = num * 10 + (start + i);
            }
            if (num >= low && num <= high) {
                result[count++] = num;
            }
        }
    }
    *returnSize = count;
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Collections.Generic;

public class Solution {
    public IList<int> SequentialDigits(int low, int high) {
        List<int> result = new List<int>();
        string digits = "123456789";
        for (int len = 2; len <= 9; len++) {
            for (int i = 0; i <= 9 - len; i++) {
                int num = int.Parse(digits.Substring(i, len));
                if (num >= low && num <= high) {
                    result.Add(num);
                }
            }
        }
        return result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} low
 * @param {number} high
 * @return {number[]}
 */
var sequentialDigits = function(low, high) {
    const result = [];
    const digits = "123456789";
    for (let len = 2; len <= 9; len++) {
        for (let i = 0; i <= 9 - len; i++) {
            const num = parseInt(digits.substring(i, i + len));
            if (num >= low && num <= high) {
                result.push(num);
            }
        }
    }
    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function sequentialDigits(low: number, high: number): number[] {
    const result: number[] = [];
    const digits = "123456789";
    for (let len = 2; len <= 9; len++) {
        for (let i = 0; i <= 9 - len; i++) {
            const num = parseInt(digits.substring(i, i + len));
            if (num >= low && num <= high) {
                result.push(num);
            }
        }
    }
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $low
     * @param Integer $high
     * @return Integer[]
     */
    function sequentialDigits($low, $high) {
        $result = [];
        $digits = "123456789";
        for ($len = 2; $len <= 9; $len++) {
            for ($i = 0; $i <= 9 - $len; $i++) {
                $num = (int)substr($digits, $i, $len);
                if ($num >= $low && $num <= $high) {
                    $result[] = $num;
                }
            }
        }
        return $result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func sequentialDigits(_ low: Int, _ high: Int) -> [Int] {
        var result = [Int]()
        let digits = "123456789"
        let digitsArray = Array(digits)
        for length in 2...9 {
            for i in 0...(9 - length) {
                let subStr = String(digitsArray[i..<(i + length)])
                if let num = Int(subStr) {
                    if num >= low && num <= high {
                        result.append(num)
                    }
                }
            }
        }
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
    fun sequentialDigits(low: Int, high: Int): List<Int> {
        val result = mutableListOf<Int>()
        for (len in 2..9) {
            for (start in 1..10 - len) {
                var num = 0
                for (i in 0 until len) {
                    num = num * 10 + (start + i)
                }
                if (num in low..high) {
                    result.add(num)
                }
            }
        }
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
  List<int> sequentialDigits(int low, int high) {
    List<int> result = [];
    for (int len = 2; len <= 9; len++) {
      for (int start = 1; start <= 10 - len; start++) {
        int num = 0;
        for (int i = 0; i < len; i++) {
          num = num * 10 + (start + i);
        }
        if (num >= low && num <= high) {
          result.add(num);
        }
      }
    }
    return result;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func sequentialDigits(low int, high int) []int {
    res := []int{}
    for length := 2; length <= 9; length++ {
        for start := 1; start <= 10-length; start++ {
            num := 0
            for i := 0; i < length; i++ {
                num = num*10 + (start + i)
            }
            if num >= low && num <= high {
                res = append(res, num)
            }
        }
    }
    return res
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} low
# @param {Integer} high
# @return {Integer[]}
def sequential_digits(low, high)
  res = []
  (2..9).each do |len|
    (1..10 - len).each do |start|
      num = 0
      (0...len).each do |i|
        num = num * 10 + (start + i)
      end
      res << num if num >= low && num <= high
    end
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
    def sequentialDigits(low: Int, high: Int): List<Int> = {
        import scala.collection.mutable.ListBuffer
        val res = ListBuffer[Int]()
        for (len <- 2 to 9) {
            for (start <- 1 to 10 - len) {
                var num = 0
                for (i <- 0 until len) {
                    num = num * 10 + (start + i)
                }
                if (num >= low && num <= high) {
                    res += num
                }
            }
        }
        res.toList
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn sequential_digits(low: i32, high: i32) -> Vec<i32> {
        let s = "123456789";
        let mut results = Vec::new();
        for len in 2..10 {
            for start in 0..=(9 - len) {
                if let Ok(num) = s[start..start + len].parse::<i32>() {
                    if num >= low && num <= high {
                        results.push(num);
                    }
                }
            }
        }
        results.sort();
        results
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (sequential-digits low high)
  (-> exact-integer? exact-integer? (listof exact-integer?))
  (let* ([s "123456789"]
         [nums (for*/list ([len (in-range 2 10)]
                           [start (in-range 0 (- 10 len))])
                 (string->number (substring s start (+ start len))))])
    (sort (filter (lambda (n) (and (>= n low) (<= n high))) nums) <)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec sequential_digits(Low :: integer(), High :: integer()) -> [integer()].
sequential_digits(Low, High) ->
  S = "123456789",
  Nums = [list_to_integer(lists:sublist(S, Start, Len))
          || Len <- lists:seq(2, 9),
             Start <- lists:seq(1, 10 - Len)],
  Filtered = [N || N <- Nums, N >= Low, N =< High],
  lists:sort(Filtered).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec sequential_digits(low :: integer, high :: integer) :: [integer]
  def sequential_digits(low, high) do
    s = "123456789"
    for len <- 2..9,
        start <- 0..(9 - len) do
      String.slice(s, start, len) |> String.to_integer()
    end
    |> Enum.filter(fn n -> n >= low and n <= high end)
    |> Enum.sort()
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(1). Since the maximum possible number is $10^9$, there are only 36 sequential digit numbers to consider (those of lengths 2 through 9). The algorithm iterates through these fixed number of possibilities, checking each against the range bounds, resulting in a constant time complexity regardless of the input values.
- **Space Complexity:** O(1). The result list stores at most 36 integers, and no additional data structures that grow with input size are used. The memory used for generating and filtering the sequential digits remains constant.
