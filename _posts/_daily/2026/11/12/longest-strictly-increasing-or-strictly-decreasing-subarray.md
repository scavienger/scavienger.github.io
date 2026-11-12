---
layout: post
title: "Longest Strictly Increasing or Strictly Decreasing Subarray"
date: 2026-11-12 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int longestMonotonicSubarray(vector<int>&\
        \ nums) {\n        int n = nums.size();\n        if (n == 0) return 0;\n   \
        \     int maxLen = 1, inc = 1, dec = 1;\n        for (int i = 1; i < n; ++i)\
        \ {\n            if (nums[i] > nums[i - 1]) {\n                inc++;\n    \
        \            dec = 1;\n            } else if (nums[i] < nums[i - 1]) {\n   \
        \             dec++;\n                inc = 1;\n            } else {\n     \
        \           inc = 1;\n                dec = 1;\n            }\n            maxLen\
        \ = max({maxLen, inc, dec});\n        }\n        return maxLen;\n    }\n};"
      java: "class Solution {\n    public int longestMonotonicSubarray(int[] nums) {\n\
        \        int n = nums.length;\n        if (n == 0) return 0;\n        int maxLen\
        \ = 1, inc = 1, dec = 1;\n        for (int i = 1; i < n; i++) {\n          \
        \  if (nums[i] > nums[i - 1]) {\n                inc++;\n                dec\
        \ = 1;\n            } else if (nums[i] < nums[i - 1]) {\n                dec++;\n\
        \                inc = 1;\n            } else {\n                inc = 1;\n\
        \                dec = 1;\n            }\n            maxLen = Math.max(maxLen,\
        \ Math.max(inc, dec));\n        }\n        return maxLen;\n    }\n}"
      python: "class Solution(object):\n    def longestMonotonicSubarray(self, nums):\n\
        \        \"\"\"\n        :type nums: List[int]\n        :rtype: int\n      \
        \  \"\"\"\n        if not nums:\n            return 0\n        max_len = 1\n\
        \        inc = 1\n        dec = 1\n        for i in range(1, len(nums)):\n \
        \           if nums[i] > nums[i - 1]:\n                inc += 1\n          \
        \      dec = 1\n            elif nums[i] < nums[i - 1]:\n                dec\
        \ += 1\n                inc = 1\n            else:\n                inc = 1\n\
        \                dec = 1\n            max_len = max(max_len, inc, dec)\n   \
        \     return max_len"
      python3: "class Solution:\n    def longestMonotonicSubarray(self, nums: List[int])\
        \ -> int:\n        if not nums:\n            return 0\n        max_len = 1\n\
        \        inc = 1\n        dec = 1\n        for i in range(1, len(nums)):\n \
        \           if nums[i] > nums[i - 1]:\n                inc += 1\n          \
        \      dec = 1\n            elif nums[i] < nums[i - 1]:\n                dec\
        \ += 1\n                inc = 1\n            else:\n                inc = 1\n\
        \                dec = 1\n            max_len = max(max_len, inc, dec)\n   \
        \     return max_len"
      c: "int longestMonotonicSubarray(int* nums, int numsSize) {\n    if (numsSize\
        \ <= 0) return 0;\n    int maxLen = 1, inc = 1, dec = 1;\n    for (int i = 1;\
        \ i < numsSize; i++) {\n        if (nums[i] > nums[i - 1]) {\n            inc++;\n\
        \            dec = 1;\n        } else if (nums[i] < nums[i - 1]) {\n       \
        \     dec++;\n            inc = 1;\n        } else {\n            inc = 1;\n\
        \            dec = 1;\n        }\n        if (inc > maxLen) maxLen = inc;\n\
        \        if (dec > maxLen) maxLen = dec;\n    }\n    return maxLen;\n}"
      csharp: "public class Solution {\n    public int LongestMonotonicSubarray(int[]\
        \ nums) {\n        int n = nums.Length;\n        if (n == 0) return 0;\n   \
        \     int maxLen = 1, inc = 1, dec = 1;\n        for (int i = 1; i < n; i++)\
        \ {\n            if (nums[i] > nums[i - 1]) {\n                inc++;\n    \
        \            dec = 1;\n            } else if (nums[i] < nums[i - 1]) {\n   \
        \             dec++;\n                inc = 1;\n            } else {\n     \
        \           inc = 1;\n                dec = 1;\n            }\n            maxLen\
        \ = Math.Max(maxLen, Math.Max(inc, dec));\n        }\n        return maxLen;\n\
        \    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar longestMonotonicSubarray\
        \ = function(nums) {\n    if (nums.length === 0) return 0;\n    let maxLen =\
        \ 1, inc = 1, dec = 1;\n    for (let i = 1; i < nums.length; i++) {\n      \
        \  if (nums[i] > nums[i - 1]) {\n            inc++;\n            dec = 1;\n\
        \        } else if (nums[i] < nums[i - 1]) {\n            dec++;\n         \
        \   inc = 1;\n        } else {\n            inc = 1;\n            dec = 1;\n\
        \        }\n        maxLen = Math.max(maxLen, inc, dec);\n    }\n    return\
        \ maxLen;\n};"
      typescript: "function longestMonotonicSubarray(nums: number[]): number {\n   \
        \ if (nums.length === 0) return 0;\n    let maxLen = 1;\n    let inc = 1;\n\
        \    let dec = 1;\n    for (let i = 1; i < nums.length; i++) {\n        if (nums[i]\
        \ > nums[i - 1]) {\n            inc++;\n            dec = 1;\n        } else\
        \ if (nums[i] < nums[i - 1]) {\n            dec++;\n            inc = 1;\n \
        \       } else {\n            inc = 1;\n            dec = 1;\n        }\n  \
        \      maxLen = Math.max(maxLen, inc, dec);\n    }\n    return maxLen;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function longestMonotonicSubarray($nums) {\n       \
        \ $n = count($nums);\n        if ($n === 0) return 0;\n        $maxLen = 1;\n\
        \        $inc = 1;\n        $dec = 1;\n        for ($i = 1; $i < $n; $i++) {\n\
        \            if ($nums[$i] > $nums[$i - 1]) {\n                $inc++;\n   \
        \             $dec = 1;\n            } else if ($nums[$i] < $nums[$i - 1]) {\n\
        \                $dec++;\n                $inc = 1;\n            } else {\n\
        \                $inc = 1;\n                $dec = 1;\n            }\n     \
        \       $maxLen = max($maxLen, $inc, $dec);\n        }\n        return $maxLen;\n\
        \    }\n}"
      swift: "class Solution {\n    func longestMonotonicSubarray(_ nums: [Int]) ->\
        \ Int {\n        guard !nums.isEmpty else { return 0 }\n        var maxLen =\
        \ 1\n        var inc = 1\n        var dec = 1\n        for i in 1..<nums.count\
        \ {\n            if nums[i] > nums[i - 1] {\n                inc += 1\n    \
        \            dec = 1\n            } else if nums[i] < nums[i - 1] {\n      \
        \          dec += 1\n                inc = 1\n            } else {\n       \
        \         inc = 1\n                dec = 1\n            }\n            maxLen\
        \ = max(maxLen, inc, dec)\n        }\n        return maxLen\n    }\n}"
      kotlin: "class Solution {\n    fun longestMonotonicSubarray(nums: IntArray): Int\
        \ {\n        if (nums.isEmpty()) return 0\n        var maxLen = 1\n        var\
        \ inc = 1\n        var dec = 1\n        for (i in 1 until nums.size) {\n   \
        \         if (nums[i] > nums[i - 1]) {\n                inc++\n            \
        \    dec = 1\n            } else if (nums[i] < nums[i - 1]) {\n            \
        \    dec++\n                inc = 1\n            } else {\n                inc\
        \ = 1\n                dec = 1\n            }\n            maxLen = maxOf(maxLen,\
        \ inc, dec)\n        }\n        return maxLen\n    }\n}"
      dart: "class Solution {\n  int longestMonotonicSubarray(List<int> nums) {\n  \
        \  if (nums.isEmpty) return 0;\n    int maxLen = 1;\n    int inc = 1;\n    int\
        \ dec = 1;\n    for (int i = 1; i < nums.length; i++) {\n      if (nums[i] >\
        \ nums[i - 1]) {\n        inc++;\n        dec = 1;\n      } else if (nums[i]\
        \ < nums[i - 1]) {\n        dec++;\n        inc = 1;\n      } else {\n     \
        \   inc = 1;\n        dec = 1;\n      }\n      if (inc > maxLen) maxLen = inc;\n\
        \      if (dec > maxLen) maxLen = dec;\n    }\n    return maxLen;\n  }\n}"
      go: "func longestMonotonicSubarray(nums []int) int {\n    if len(nums) == 0 {\n\
        \        return 0\n    }\n    maxLen := 1\n    inc := 1\n    dec := 1\n    for\
        \ i := 1; i < len(nums); i++ {\n        if nums[i] > nums[i-1] {\n         \
        \   inc++\n            dec = 1\n        } else if nums[i] < nums[i-1] {\n  \
        \          dec++\n            inc = 1\n        } else {\n            inc = 1\n\
        \            dec = 1\n        }\n        if inc > maxLen {\n            maxLen\
        \ = inc\n        }\n        if dec > maxLen {\n            maxLen = dec\n  \
        \      }\n    }\n    return maxLen\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef longest_monotonic_subarray(nums)\n\
        \  return 0 if nums.empty?\n  max_len = 1\n  inc = 1\n  dec = 1\n  (1...nums.length).each\
        \ do |i|\n    if nums[i] > nums[i - 1]\n      inc += 1\n      dec = 1\n    elsif\
        \ nums[i] < nums[i - 1]\n      dec += 1\n      inc = 1\n    else\n      inc\
        \ = 1\n      dec = 1\n    end\n    max_len = [max_len, inc, dec].max\n  end\n\
        \  max_len\nend"
      scala: "object Solution {\n    def longestMonotonicSubarray(nums: Array[Int]):\
        \ Int = {\n        if (nums.isEmpty) return 0\n        var maxLen = 1\n    \
        \    var inc = 1\n        var dec = 1\n        for (i <- 1 until nums.length)\
        \ {\n            if (nums(i) > nums(i - 1)) {\n                inc += 1\n  \
        \              dec = 1\n            } else if (nums(i) < nums(i - 1)) {\n  \
        \              dec += 1\n                inc = 1\n            } else {\n   \
        \             inc = 1\n                dec = 1\n            }\n            maxLen\
        \ = maxLen.max(inc).max(dec)\n        }\n        maxLen\n    }\n}"
      rust: "impl Solution {\n    pub fn longest_monotonic_subarray(nums: Vec<i32>)\
        \ -> i32 {\n        if nums.is_empty() {\n            return 0;\n        }\n\
        \        let mut max_len = 1;\n        let mut inc = 1;\n        let mut dec\
        \ = 1;\n        for i in 1..nums.len() {\n            if nums[i] > nums[i -\
        \ 1] {\n                inc += 1;\n                dec = 1;\n            } else\
        \ if nums[i] < nums[i - 1] {\n                dec += 1;\n                inc\
        \ = 1;\n            } else {\n                inc = 1;\n                dec\
        \ = 1;\n            }\n            max_len = max_len.max(inc).max(dec);\n  \
        \      }\n        max_len\n    }\n}"
      racket: "(define/contract (longest-monotonic-subarray nums)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (if (null? nums)\n      0\n      (let loop ([lst (cdr nums)]\n\
        \                 [prev (car nums)]\n                 [inc 1]\n            \
        \     [dec 1]\n                 [max_len 1])\n        (if (null? lst)\n    \
        \        max_len\n            (let* ([curr (car lst)]\n                   [new_inc\
        \ (if (> curr prev) (+ inc 1) 1)]\n                   [new_dec (if (< curr prev)\
        \ (+ dec 1) 1)]\n                   [new_max (max max_len new_inc new_dec)])\n\
        \              (loop (cdr lst) curr new_inc new_dec new_max))))))"
      erlang: "-spec longest_monotonic_subarray(Nums :: [integer()]) -> integer().\n\
        longest_monotonic_subarray(Nums) ->\n  case Nums of\n    [] -> 0;\n    [H|T]\
        \ -> longest_monotonic_helper(T, H, 1, 1, 1)\n  end.\n\nlongest_monotonic_helper([],\
        \ _Prev, _Inc, _Dec, Max) -> Max;\nlongest_monotonic_helper([H|T], Prev, Inc,\
        \ Dec, Max) ->\n  {NewInc, NewDec} = if\n    H > Prev -> {Inc + 1, 1};\n   \
        \ H < Prev -> {1, Dec + 1};\n    true -> {1, 1}\n  end,\n  NewMax = erlang:max(Max,\
        \ erlang:max(NewInc, NewDec)),\n  longest_monotonic_helper(T, H, NewInc, NewDec,\
        \ NewMax)."
      elixir: "defmodule Solution do\n  @spec longest_monotonic_subarray(nums :: [integer])\
        \ :: integer\n  def longest_monotonic_subarray(nums) do\n    case nums do\n\
        \      [] -> 0\n      [h | t] ->\n        {_, _, _, max_len} = Enum.reduce(t,\
        \ {h, 1, 1, 1}, fn curr, {prev, inc, dec, max_l} ->\n          {ni, nd} = cond\
        \ do\n            curr > prev -> {inc + 1, 1}\n            curr < prev -> {1,\
        \ dec + 1}\n            true -> {1, 1}\n          end\n          {curr, ni,\
        \ nd, max(max_l, max(ni, nd))}\n        end)\n        max_len\n    end\n  end\n\
        end"
    approach: 'The algorithm employs a linear scan to efficiently track the lengths
      of the longest strictly increasing and strictly decreasing subarrays in a single
      pass. We maintain two running counters, one for the current increasing trend and
      another for the current decreasing trend, both starting at one. As we iterate
      through the array from the second element onward, we compare the current value
      to its predecessor to update these counters accordingly.


      If the current element is strictly greater, we increment the increasing counter
      and reset the decreasing counter to one. Conversely, if it is strictly smaller,
      we increment the decreasing counter and reset the increasing one to one. If the
      values are equal, both counters are reset to one as the strict monotonicity is
      broken. The overall maximum value observed across both counters during the iteration
      provides the final length of the longest monotonic subarray.'
    time_complexity: O(n) where n is the length of the input array. The algorithm performs
      a single traversal of the array, executing constant-time operations at each step.
    space_complexity: O(1) because the solution only uses a fixed number of integer
      variables to store the current and maximum lengths, independent of the input size.
    elapsed_time: 97.14847373962402
    model: gemini-3-flash-preview
    generated_at: '2026-11-12 05:11:17 '
---

## Problem #3105: Longest Strictly Increasing or Strictly Decreasing Subarray

**Difficulty:** Easy

**Topics:** Array

## Problem Description

<p>You are given an array of integers <code>nums</code>. Return <em>the length of the <strong>longest</strong> <span data-keyword="subarray-nonempty">subarray</span> of </em><code>nums</code><em> which is either <strong><span data-keyword="strictly-increasing-array">strictly increasing</span></strong> or <strong><span data-keyword="strictly-decreasing-array">strictly decreasing</span></strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,4,3,3,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The strictly increasing subarrays of <code>nums</code> are <code>[1]</code>, <code>[2]</code>, <code>[3]</code>, <code>[3]</code>, <code>[4]</code>, and <code>[1,4]</code>.</p>

<p>The strictly decreasing subarrays of <code>nums</code> are <code>[1]</code>, <code>[2]</code>, <code>[3]</code>, <code>[3]</code>, <code>[4]</code>, <code>[3,2]</code>, and <code>[4,3]</code>.</p>

<p>Hence, we return <code>2</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,3,3,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>The strictly increasing subarrays of <code>nums</code> are <code>[3]</code>, <code>[3]</code>, <code>[3]</code>, and <code>[3]</code>.</p>

<p>The strictly decreasing subarrays of <code>nums</code> are <code>[3]</code>, <code>[3]</code>, <code>[3]</code>, and <code>[3]</code>.</p>

<p>Hence, we return <code>1</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,2,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>The strictly increasing subarrays of <code>nums</code> are <code>[3]</code>, <code>[2]</code>, and <code>[1]</code>.</p>

<p>The strictly decreasing subarrays of <code>nums</code> are <code>[3]</code>, <code>[2]</code>, <code>[1]</code>, <code>[3,2]</code>, <code>[2,1]</code>, and <code>[3,2,1]</code>.</p>

<p>Hence, we return <code>3</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 50</code></li>
</ul>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm employs a linear scan to efficiently track the lengths of the longest strictly increasing and strictly decreasing subarrays in a single pass. We maintain two running counters, one for the current increasing trend and another for the current decreasing trend, both starting at one. As we iterate through the array from the second element onward, we compare the current value to its predecessor to update these counters accordingly.

If the current element is strictly greater, we increment the increasing counter and reset the decreasing counter to one. Conversely, if it is strictly smaller, we increment the decreasing counter and reset the increasing one to one. If the values are equal, both counters are reset to one as the strict monotonicity is broken. The overall maximum value observed across both counters during the iteration provides the final length of the longest monotonic subarray.

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
    int longestMonotonicSubarray(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        int maxLen = 1, inc = 1, dec = 1;
        for (int i = 1; i < n; ++i) {
            if (nums[i] > nums[i - 1]) {
                inc++;
                dec = 1;
            } else if (nums[i] < nums[i - 1]) {
                dec++;
                inc = 1;
            } else {
                inc = 1;
                dec = 1;
            }
            maxLen = max({maxLen, inc, dec});
        }
        return maxLen;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int longestMonotonicSubarray(int[] nums) {
        int n = nums.length;
        if (n == 0) return 0;
        int maxLen = 1, inc = 1, dec = 1;
        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[i - 1]) {
                inc++;
                dec = 1;
            } else if (nums[i] < nums[i - 1]) {
                dec++;
                inc = 1;
            } else {
                inc = 1;
                dec = 1;
            }
            maxLen = Math.max(maxLen, Math.max(inc, dec));
        }
        return maxLen;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_len = 1
        inc = 1
        dec = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc = 1
                dec = 1
            max_len = max(max_len, inc, dec)
        return max_len
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_len = 1
        inc = 1
        dec = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc = 1
                dec = 1
            max_len = max(max_len, inc, dec)
        return max_len
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int longestMonotonicSubarray(int* nums, int numsSize) {
    if (numsSize <= 0) return 0;
    int maxLen = 1, inc = 1, dec = 1;
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] > nums[i - 1]) {
            inc++;
            dec = 1;
        } else if (nums[i] < nums[i - 1]) {
            dec++;
            inc = 1;
        } else {
            inc = 1;
            dec = 1;
        }
        if (inc > maxLen) maxLen = inc;
        if (dec > maxLen) maxLen = dec;
    }
    return maxLen;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int LongestMonotonicSubarray(int[] nums) {
        int n = nums.Length;
        if (n == 0) return 0;
        int maxLen = 1, inc = 1, dec = 1;
        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[i - 1]) {
                inc++;
                dec = 1;
            } else if (nums[i] < nums[i - 1]) {
                dec++;
                inc = 1;
            } else {
                inc = 1;
                dec = 1;
            }
            maxLen = Math.Max(maxLen, Math.Max(inc, dec));
        }
        return maxLen;
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
 * @return {number}
 */
var longestMonotonicSubarray = function(nums) {
    if (nums.length === 0) return 0;
    let maxLen = 1, inc = 1, dec = 1;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > nums[i - 1]) {
            inc++;
            dec = 1;
        } else if (nums[i] < nums[i - 1]) {
            dec++;
            inc = 1;
        } else {
            inc = 1;
            dec = 1;
        }
        maxLen = Math.max(maxLen, inc, dec);
    }
    return maxLen;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function longestMonotonicSubarray(nums: number[]): number {
    if (nums.length === 0) return 0;
    let maxLen = 1;
    let inc = 1;
    let dec = 1;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > nums[i - 1]) {
            inc++;
            dec = 1;
        } else if (nums[i] < nums[i - 1]) {
            dec++;
            inc = 1;
        } else {
            inc = 1;
            dec = 1;
        }
        maxLen = Math.max(maxLen, inc, dec);
    }
    return maxLen;
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
     * @return Integer
     */
    function longestMonotonicSubarray($nums) {
        $n = count($nums);
        if ($n === 0) return 0;
        $maxLen = 1;
        $inc = 1;
        $dec = 1;
        for ($i = 1; $i < $n; $i++) {
            if ($nums[$i] > $nums[$i - 1]) {
                $inc++;
                $dec = 1;
            } else if ($nums[$i] < $nums[$i - 1]) {
                $dec++;
                $inc = 1;
            } else {
                $inc = 1;
                $dec = 1;
            }
            $maxLen = max($maxLen, $inc, $dec);
        }
        return $maxLen;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func longestMonotonicSubarray(_ nums: [Int]) -> Int {
        guard !nums.isEmpty else { return 0 }
        var maxLen = 1
        var inc = 1
        var dec = 1
        for i in 1..<nums.count {
            if nums[i] > nums[i - 1] {
                inc += 1
                dec = 1
            } else if nums[i] < nums[i - 1] {
                dec += 1
                inc = 1
            } else {
                inc = 1
                dec = 1
            }
            maxLen = max(maxLen, inc, dec)
        }
        return maxLen
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun longestMonotonicSubarray(nums: IntArray): Int {
        if (nums.isEmpty()) return 0
        var maxLen = 1
        var inc = 1
        var dec = 1
        for (i in 1 until nums.size) {
            if (nums[i] > nums[i - 1]) {
                inc++
                dec = 1
            } else if (nums[i] < nums[i - 1]) {
                dec++
                inc = 1
            } else {
                inc = 1
                dec = 1
            }
            maxLen = maxOf(maxLen, inc, dec)
        }
        return maxLen
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int longestMonotonicSubarray(List<int> nums) {
    if (nums.isEmpty) return 0;
    int maxLen = 1;
    int inc = 1;
    int dec = 1;
    for (int i = 1; i < nums.length; i++) {
      if (nums[i] > nums[i - 1]) {
        inc++;
        dec = 1;
      } else if (nums[i] < nums[i - 1]) {
        dec++;
        inc = 1;
      } else {
        inc = 1;
        dec = 1;
      }
      if (inc > maxLen) maxLen = inc;
      if (dec > maxLen) maxLen = dec;
    }
    return maxLen;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func longestMonotonicSubarray(nums []int) int {
    if len(nums) == 0 {
        return 0
    }
    maxLen := 1
    inc := 1
    dec := 1
    for i := 1; i < len(nums); i++ {
        if nums[i] > nums[i-1] {
            inc++
            dec = 1
        } else if nums[i] < nums[i-1] {
            dec++
            inc = 1
        } else {
            inc = 1
            dec = 1
        }
        if inc > maxLen {
            maxLen = inc
        }
        if dec > maxLen {
            maxLen = dec
        }
    }
    return maxLen
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def longest_monotonic_subarray(nums)
  return 0 if nums.empty?
  max_len = 1
  inc = 1
  dec = 1
  (1...nums.length).each do |i|
    if nums[i] > nums[i - 1]
      inc += 1
      dec = 1
    elsif nums[i] < nums[i - 1]
      dec += 1
      inc = 1
    else
      inc = 1
      dec = 1
    end
    max_len = [max_len, inc, dec].max
  end
  max_len
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def longestMonotonicSubarray(nums: Array[Int]): Int = {
        if (nums.isEmpty) return 0
        var maxLen = 1
        var inc = 1
        var dec = 1
        for (i <- 1 until nums.length) {
            if (nums(i) > nums(i - 1)) {
                inc += 1
                dec = 1
            } else if (nums(i) < nums(i - 1)) {
                dec += 1
                inc = 1
            } else {
                inc = 1
                dec = 1
            }
            maxLen = maxLen.max(inc).max(dec)
        }
        maxLen
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn longest_monotonic_subarray(nums: Vec<i32>) -> i32 {
        if nums.is_empty() {
            return 0;
        }
        let mut max_len = 1;
        let mut inc = 1;
        let mut dec = 1;
        for i in 1..nums.len() {
            if nums[i] > nums[i - 1] {
                inc += 1;
                dec = 1;
            } else if nums[i] < nums[i - 1] {
                dec += 1;
                inc = 1;
            } else {
                inc = 1;
                dec = 1;
            }
            max_len = max_len.max(inc).max(dec);
        }
        max_len
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (longest-monotonic-subarray nums)
  (-> (listof exact-integer?) exact-integer?)
  (if (null? nums)
      0
      (let loop ([lst (cdr nums)]
                 [prev (car nums)]
                 [inc 1]
                 [dec 1]
                 [max_len 1])
        (if (null? lst)
            max_len
            (let* ([curr (car lst)]
                   [new_inc (if (> curr prev) (+ inc 1) 1)]
                   [new_dec (if (< curr prev) (+ dec 1) 1)]
                   [new_max (max max_len new_inc new_dec)])
              (loop (cdr lst) curr new_inc new_dec new_max))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec longest_monotonic_subarray(Nums :: [integer()]) -> integer().
longest_monotonic_subarray(Nums) ->
  case Nums of
    [] -> 0;
    [H|T] -> longest_monotonic_helper(T, H, 1, 1, 1)
  end.

longest_monotonic_helper([], _Prev, _Inc, _Dec, Max) -> Max;
longest_monotonic_helper([H|T], Prev, Inc, Dec, Max) ->
  {NewInc, NewDec} = if
    H > Prev -> {Inc + 1, 1};
    H < Prev -> {1, Dec + 1};
    true -> {1, 1}
  end,
  NewMax = erlang:max(Max, erlang:max(NewInc, NewDec)),
  longest_monotonic_helper(T, H, NewInc, NewDec, NewMax).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec longest_monotonic_subarray(nums :: [integer]) :: integer
  def longest_monotonic_subarray(nums) do
    case nums do
      [] -> 0
      [h | t] ->
        {_, _, _, max_len} = Enum.reduce(t, {h, 1, 1, 1}, fn curr, {prev, inc, dec, max_l} ->
          {ni, nd} = cond do
            curr > prev -> {inc + 1, 1}
            curr < prev -> {1, dec + 1}
            true -> {1, 1}
          end
          {curr, ni, nd, max(max_l, max(ni, nd))}
        end)
        max_len
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the input array. The algorithm performs a single traversal of the array, executing constant-time operations at each step.
- **Space Complexity:** O(1) because the solution only uses a fixed number of integer variables to store the current and maximum lengths, independent of the input size.
