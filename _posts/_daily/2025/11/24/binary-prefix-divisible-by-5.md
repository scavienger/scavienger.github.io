---
layout: post
title: "Binary Prefix Divisible By 5"
date: 2025-11-24 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Bit Manipulation"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/binary-prefix-divisible-by-5/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<bool> prefixesDivBy5(vector<int>&\
        \ nums) {\n        vector<bool> answer;\n        int remainder = 0;\n      \
        \  for (int bit : nums) {\n            remainder = (remainder * 2 + bit) % 5;\n\
        \            answer.push_back(remainder == 0);\n        }\n        return answer;\n\
        \    }\n};"
      java: "class Solution {\n    public List<Boolean> prefixesDivBy5(int[] nums) {\n\
        \        List<Boolean> answer = new ArrayList<>();\n        int remainder =\
        \ 0;\n        for (int bit : nums) {\n            remainder = (remainder * 2\
        \ + bit) % 5;\n            answer.add(remainder == 0);\n        }\n        return\
        \ answer;\n    }\n}"
      python: "class Solution(object):\n    def prefixesDivBy5(self, nums):\n      \
        \  \"\"\"\n        :type nums: List[int]\n        :rtype: List[bool]\n     \
        \   \"\"\"\n        answer = []\n        remainder = 0\n        for bit in nums:\n\
        \            remainder = (remainder * 2 + bit) % 5\n            answer.append(remainder\
        \ == 0)\n        return answer"
      python3: "class Solution:\n    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:\n\
        \        answer = []\n        remainder = 0\n        for bit in nums:\n    \
        \        remainder = (remainder * 2 + bit) % 5\n            answer.append(remainder\
        \ == 0)\n        return answer"
      c: "bool* prefixesDivBy5(int* nums, int numsSize, int* returnSize) {\n    bool*\
        \ answer = malloc(numsSize * sizeof(bool));\n    int remainder = 0;\n    for\
        \ (int i = 0; i < numsSize; i++) {\n        remainder = (remainder * 2 + nums[i])\
        \ % 5;\n        answer[i] = (remainder == 0);\n    }\n    *returnSize = numsSize;\n\
        \    return answer;\n}"
      csharp: "public class Solution {\n    public IList<bool> PrefixesDivBy5(int[]\
        \ nums) {\n        IList<bool> answer = new List<bool>();\n        int remainder\
        \ = 0;\n        foreach (int bit in nums) {\n            remainder = (remainder\
        \ * 2 + bit) % 5;\n            answer.Add(remainder == 0);\n        }\n    \
        \    return answer;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {boolean[]}\n */\nvar\
        \ prefixesDivBy5 = function(nums) {\n    const answer = [];\n    let remainder\
        \ = 0;\n    for (const bit of nums) {\n        remainder = (remainder * 2 +\
        \ bit) % 5;\n        answer.push(remainder === 0);\n    }\n    return answer;\n\
        };"
      typescript: "function prefixesDivBy5(nums: number[]): boolean[] {\n    const answer:\
        \ boolean[] = [];\n    let remainder = 0;\n    for (const bit of nums) {\n \
        \       remainder = (remainder * 2 + bit) % 5;\n        answer.push(remainder\
        \ === 0);\n    }\n    return answer;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Boolean[]\n     */\n    function prefixesDivBy5($nums) {\n        $answer\
        \ = [];\n        $remainder = 0;\n        foreach ($nums as $bit) {\n      \
        \      $remainder = ($remainder * 2 + $bit) % 5;\n            $answer[] = $remainder\
        \ === 0;\n        }\n        return $answer;\n    }\n}"
      swift: "class Solution {\n    func prefixesDivBy5(_ nums: [Int]) -> [Bool] {\n\
        \        var answer: [Bool] = []\n        var remainder = 0\n        for bit\
        \ in nums {\n            remainder = (remainder * 2 + bit) % 5\n           \
        \ answer.append(remainder == 0)\n        }\n        return answer\n    }\n}"
      kotlin: "class Solution {\n    fun prefixesDivBy5(nums: IntArray): List<Boolean>\
        \ {\n        val answer = mutableListOf<Boolean>()\n        var remainder =\
        \ 0\n        for (bit in nums) {\n            remainder = (remainder * 2 + bit)\
        \ % 5\n            answer.add(remainder == 0)\n        }\n        return answer\n\
        \    }\n}"
      dart: "class Solution {\n  List<bool> prefixesDivBy5(List<int> nums) {\n    final\
        \ answer = <bool>[];\n    var remainder = 0;\n    for (final bit in nums) {\n\
        \      remainder = (remainder * 2 + bit) % 5;\n      answer.add(remainder ==\
        \ 0);\n    }\n    return answer;\n  }\n}"
      go: "func prefixesDivBy5(nums []int) []bool {\n    answer := make([]bool, 0, len(nums))\n\
        \    remainder := 0\n    for _, bit := range nums {\n        remainder = (remainder*2\
        \ + bit) % 5\n        answer = append(answer, remainder == 0)\n    }\n    return\
        \ answer\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Boolean[]}\ndef prefixes_div_by5(nums)\n\
        \    answer = []\n    remainder = 0\n    nums.each do |bit|\n        remainder\
        \ = (remainder * 2 + bit) % 5\n        answer << (remainder == 0)\n    end\n\
        \    answer\nend"
      scala: "object Solution {\n    def prefixesDivBy5(nums: Array[Int]): List[Boolean]\
        \ = {\n        var remainder = 0\n        nums.iterator.map { bit =>\n     \
        \       remainder = (remainder * 2 + bit) % 5\n            remainder == 0\n\
        \        }.toList\n    }\n}"
      rust: "impl Solution {\n    pub fn prefixes_div_by5(nums: Vec<i32>) -> Vec<bool>\
        \ {\n        let mut remainder = 0;\n        nums.into_iter()\n            .map(|bit|\
        \ {\n                remainder = (remainder * 2 + bit) % 5;\n              \
        \  remainder == 0\n            })\n            .collect()\n    }\n}"
      racket: "(define/contract (prefixes-div-by5 nums)\n  (-> (listof exact-integer?)\
        \ (listof boolean?))\n  (let loop ([remaining nums] [remainder 0] [answer '()])\n\
        \    (if (null? remaining)\n        (reverse answer)\n        (let ([next-remainder\
        \ (modulo (+ (* remainder 2) (car remaining)) 5)])\n          (loop (cdr remaining)\n\
        \                next-remainder\n                (cons (= next-remainder 0)\
        \ answer))))))"
      erlang: "-spec prefixes_div_by5(Nums :: [integer()]) -> [boolean()].\nprefixes_div_by5(Nums)\
        \ ->\n  prefixes_div_by5(Nums, 0, []).\n\nprefixes_div_by5([], _Remainder, Acc)\
        \ ->\n  lists:reverse(Acc);\nprefixes_div_by5([Bit | Rest], Remainder, Acc)\
        \ ->\n  NextRemainder = (Remainder * 2 + Bit) rem 5,\n  prefixes_div_by5(Rest,\
        \ NextRemainder, [NextRemainder =:= 0 | Acc])."
      elixir: "defmodule Solution do\n  @spec prefixes_div_by5(nums :: [integer]) ::\
        \ [boolean]\n  def prefixes_div_by5(nums) do\n    {answer, _remainder} =\n \
        \     Enum.map_reduce(nums, 0, fn bit, remainder ->\n        next_remainder\
        \ = rem(remainder * 2 + bit, 5)\n        {next_remainder == 0, next_remainder}\n\
        \      end)\n\n    answer\n  end\nend"
    approach: 'Process the bits from left to right while keeping only the current prefix''s
      remainder modulo 5. Appending a bit b to a binary number with remainder r gives
      a new remainder of (2r + b) modulo 5.


      After updating the remainder for each bit, append whether it equals zero to the
      answer. Tracking only the remainder avoids building potentially large prefix values.'
    time_complexity: O(n), where n is the length of nums, because each bit is processed
      once.
    space_complexity: O(n) for the output array; the remainder uses O(1) extra space.
    elapsed_time: 42.836931467056274
    model: gpt-6-luna
    generated_at: '2026-11-13 00:11:58 '
---

## Problem #1018: Binary Prefix Divisible By 5

**Difficulty:** Easy

**Topics:** Array, Bit Manipulation

## Problem Description

<p>You are given a binary array <code>nums</code> (<strong>0-indexed</strong>).</p>

<p>We define <code>x<sub>i</sub></code> as the number whose binary representation is the subarray <code>nums[0..i]</code> (from most-significant-bit to least-significant-bit).</p>

<ul>
	<li>For example, if <code>nums = [1,0,1]</code>, then <code>x<sub>0</sub> = 1</code>, <code>x<sub>1</sub> = 2</code>, and <code>x<sub>2</sub> = 5</code>.</li>
</ul>

<p>Return <em>an array of booleans </em><code>answer</code><em> where </em><code>answer[i]</code><em> is </em><code>true</code><em> if </em><code>x<sub>i</sub></code><em> is divisible by </em><code>5</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,1]
<strong>Output:</strong> [true,false,false]
<strong>Explanation:</strong> The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.
Only the first number is divisible by 5, so answer[0] is true.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1]
<strong>Output:</strong> [false,false,false]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>


## Hints

1. If X is the first i digits of the array as a binary number, then 2X + A[i] is the first i+1 digits.

## 🤖 AI-Generated Solution (gpt-6-luna)

### Approach

Process the bits from left to right while keeping only the current prefix's remainder modulo 5. Appending a bit b to a binary number with remainder r gives a new remainder of (2r + b) modulo 5.

After updating the remainder for each bit, append whether it equals zero to the answer. Tracking only the remainder avoids building potentially large prefix values.

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
    vector<bool> prefixesDivBy5(vector<int>& nums) {
        vector<bool> answer;
        int remainder = 0;
        for (int bit : nums) {
            remainder = (remainder * 2 + bit) % 5;
            answer.push_back(remainder == 0);
        }
        return answer;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public List<Boolean> prefixesDivBy5(int[] nums) {
        List<Boolean> answer = new ArrayList<>();
        int remainder = 0;
        for (int bit : nums) {
            remainder = (remainder * 2 + bit) % 5;
            answer.add(remainder == 0);
        }
        return answer;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        answer = []
        remainder = 0
        for bit in nums:
            remainder = (remainder * 2 + bit) % 5
            answer.append(remainder == 0)
        return answer
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        answer = []
        remainder = 0
        for bit in nums:
            remainder = (remainder * 2 + bit) % 5
            answer.append(remainder == 0)
        return answer
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
bool* prefixesDivBy5(int* nums, int numsSize, int* returnSize) {
    bool* answer = malloc(numsSize * sizeof(bool));
    int remainder = 0;
    for (int i = 0; i < numsSize; i++) {
        remainder = (remainder * 2 + nums[i]) % 5;
        answer[i] = (remainder == 0);
    }
    *returnSize = numsSize;
    return answer;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public IList<bool> PrefixesDivBy5(int[] nums) {
        IList<bool> answer = new List<bool>();
        int remainder = 0;
        foreach (int bit in nums) {
            remainder = (remainder * 2 + bit) % 5;
            answer.Add(remainder == 0);
        }
        return answer;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} nums
 * @return {boolean[]}
 */
var prefixesDivBy5 = function(nums) {
    const answer = [];
    let remainder = 0;
    for (const bit of nums) {
        remainder = (remainder * 2 + bit) % 5;
        answer.push(remainder === 0);
    }
    return answer;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function prefixesDivBy5(nums: number[]): boolean[] {
    const answer: boolean[] = [];
    let remainder = 0;
    for (const bit of nums) {
        remainder = (remainder * 2 + bit) % 5;
        answer.push(remainder === 0);
    }
    return answer;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean[]
     */
    function prefixesDivBy5($nums) {
        $answer = [];
        $remainder = 0;
        foreach ($nums as $bit) {
            $remainder = ($remainder * 2 + $bit) % 5;
            $answer[] = $remainder === 0;
        }
        return $answer;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func prefixesDivBy5(_ nums: [Int]) -> [Bool] {
        var answer: [Bool] = []
        var remainder = 0
        for bit in nums {
            remainder = (remainder * 2 + bit) % 5
            answer.append(remainder == 0)
        }
        return answer
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun prefixesDivBy5(nums: IntArray): List<Boolean> {
        val answer = mutableListOf<Boolean>()
        var remainder = 0
        for (bit in nums) {
            remainder = (remainder * 2 + bit) % 5
            answer.add(remainder == 0)
        }
        return answer
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<bool> prefixesDivBy5(List<int> nums) {
    final answer = <bool>[];
    var remainder = 0;
    for (final bit in nums) {
      remainder = (remainder * 2 + bit) % 5;
      answer.add(remainder == 0);
    }
    return answer;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func prefixesDivBy5(nums []int) []bool {
    answer := make([]bool, 0, len(nums))
    remainder := 0
    for _, bit := range nums {
        remainder = (remainder*2 + bit) % 5
        answer = append(answer, remainder == 0)
    }
    return answer
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Boolean[]}
def prefixes_div_by5(nums)
    answer = []
    remainder = 0
    nums.each do |bit|
        remainder = (remainder * 2 + bit) % 5
        answer << (remainder == 0)
    end
    answer
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def prefixesDivBy5(nums: Array[Int]): List[Boolean] = {
        var remainder = 0
        nums.iterator.map { bit =>
            remainder = (remainder * 2 + bit) % 5
            remainder == 0
        }.toList
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn prefixes_div_by5(nums: Vec<i32>) -> Vec<bool> {
        let mut remainder = 0;
        nums.into_iter()
            .map(|bit| {
                remainder = (remainder * 2 + bit) % 5;
                remainder == 0
            })
            .collect()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (prefixes-div-by5 nums)
  (-> (listof exact-integer?) (listof boolean?))
  (let loop ([remaining nums] [remainder 0] [answer '()])
    (if (null? remaining)
        (reverse answer)
        (let ([next-remainder (modulo (+ (* remainder 2) (car remaining)) 5)])
          (loop (cdr remaining)
                next-remainder
                (cons (= next-remainder 0) answer))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec prefixes_div_by5(Nums :: [integer()]) -> [boolean()].
prefixes_div_by5(Nums) ->
  prefixes_div_by5(Nums, 0, []).

prefixes_div_by5([], _Remainder, Acc) ->
  lists:reverse(Acc);
prefixes_div_by5([Bit | Rest], Remainder, Acc) ->
  NextRemainder = (Remainder * 2 + Bit) rem 5,
  prefixes_div_by5(Rest, NextRemainder, [NextRemainder =:= 0 | Acc]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec prefixes_div_by5(nums :: [integer]) :: [boolean]
  def prefixes_div_by5(nums) do
    {answer, _remainder} =
      Enum.map_reduce(nums, 0, fn bit, remainder ->
        next_remainder = rem(remainder * 2 + bit, 5)
        {next_remainder == 0, next_remainder}
      end)

    answer
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n), where n is the length of nums, because each bit is processed once.
- **Space Complexity:** O(n) for the output array; the remainder uses O(1) extra space.
