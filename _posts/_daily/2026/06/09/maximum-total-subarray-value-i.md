---
layout: post
title: "Maximum Total Subarray Value I"
date: 2026-06-09 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Greedy"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/maximum-total-subarray-value-i/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    long long maxTotalValue(vector<int>& nums,\
        \ int k) {\n        int min_val = nums[0];\n        int max_val = nums[0];\n\
        \        for (int x : nums) {\n            if (x < min_val) min_val = x;\n \
        \           if (x > max_val) max_val = x;\n        }\n        return (long long)k\
        \ * (max_val - min_val);\n    }\n};"
      java: "class Solution {\n    public long maxTotalValue(int[] nums, int k) {\n\
        \        int minVal = nums[0];\n        int maxVal = nums[0];\n        for (int\
        \ i = 1; i < nums.length; i++) {\n            if (nums[i] < minVal) {\n    \
        \            minVal = nums[i];\n            }\n            if (nums[i] > maxVal)\
        \ {\n                maxVal = nums[i];\n            }\n        }\n        return\
        \ (long)k * (maxVal - minVal);\n    }\n}"
      python: "class Solution(object):\n    def maxTotalValue(self, nums, k):\n    \
        \    \"\"\"\n        :type nums: List[int]\n        :type k: int\n        :rtype:\
        \ int\n        \"\"\"\n        return k * (max(nums) - min(nums))"
      python3: "class Solution:\n    def maxTotalValue(self, nums: List[int], k: int)\
        \ -> int:\n        return k * (max(nums) - min(nums))"
      c: "long long maxTotalValue(int* nums, int numsSize, int k) {\n    int min_val\
        \ = nums[0];\n    int max_val = nums[0];\n    for (int i = 1; i < numsSize;\
        \ i++) {\n        if (nums[i] < min_val) min_val = nums[i];\n        if (nums[i]\
        \ > max_val) max_val = nums[i];\n    }\n    return (long long)k * (max_val -\
        \ min_val);\n}"
      csharp: "public class Solution {\n    public long MaxTotalValue(int[] nums, int\
        \ k) {\n        int minVal = nums[0];\n        int maxVal = nums[0];\n     \
        \   foreach (int num in nums) {\n            if (num < minVal) minVal = num;\n\
        \            if (num > maxVal) maxVal = num;\n        }\n        return (long)k\
        \ * (maxVal - minVal);\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} k\n * @return\
        \ {number}\n */\nvar maxTotalValue = function(nums, k) {\n    let minVal = nums[0];\n\
        \    let maxVal = nums[0];\n    for (let i = 1; i < nums.length; i++) {\n  \
        \      if (nums[i] < minVal) minVal = nums[i];\n        if (nums[i] > maxVal)\
        \ maxVal = nums[i];\n    }\n    return k * (maxVal - minVal);\n};"
      typescript: "function maxTotalValue(nums: number[], k: number): number {\n   \
        \ let minVal: number = nums[0];\n    let maxVal: number = nums[0];\n    for\
        \ (let i = 1; i < nums.length; i++) {\n        if (nums[i] < minVal) minVal\
        \ = nums[i];\n        if (nums[i] > maxVal) maxVal = nums[i];\n    }\n    return\
        \ k * (maxVal - minVal);\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer $k\n     * @return Integer\n     */\n    function maxTotalValue($nums,\
        \ $k) {\n        $minVal = $nums[0];\n        $maxVal = $nums[0];\n        foreach\
        \ ($nums as $num) {\n            if ($num < $minVal) $minVal = $num;\n     \
        \       if ($num > $maxVal) $maxVal = $num;\n        }\n        return $k *\
        \ ($maxVal - $minVal);\n    }\n}"
      swift: "class Solution {\n    func maxTotalValue(_ nums: [Int], _ k: Int) -> Int\
        \ {\n        var minVal = nums[0]\n        var maxVal = nums[0]\n        for\
        \ num in nums {\n            if num < minVal { minVal = num }\n            if\
        \ num > maxVal { maxVal = num }\n        }\n        return k * (maxVal - minVal)\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun maxTotalValue(nums: IntArray, k: Int): Long\
        \ {\n        if (nums.isEmpty()) return 0L\n        var minVal = nums[0]\n \
        \       var maxVal = nums[0]\n        for (x in nums) {\n            if (x <\
        \ minVal) minVal = x\n            if (x > maxVal) maxVal = x\n        }\n  \
        \      return (maxVal.toLong() - minVal.toLong()) * k.toLong()\n    }\n}"
      dart: "class Solution {\n  int maxTotalValue(List<int> nums, int k) {\n    if\
        \ (nums.isEmpty()) return 0;\n    int minVal = nums[0];\n    int maxVal = nums[0];\n\
        \    for (int i = 1; i < nums.length; i++) {\n      if (nums[i] < minVal) minVal\
        \ = nums[i];\n      if (nums[i] > maxVal) maxVal = nums[i];\n    }\n    return\
        \ (maxVal - minVal) * k;\n  }\n}"
      go: "func maxTotalValue(nums []int, k int) int64 {\n\tif len(nums) == 0 {\n\t\t\
        return 0\n\t}\n\tminVal := nums[0]\n\tmaxVal := nums[0]\n\tfor _, x := range\
        \ nums {\n\t\tif x < minVal {\n\t\t\tminVal = x\n\t\t}\n\t\tif x > maxVal {\n\
        \t\t\tmaxVal = x\n\t\t}\n\t}\n\treturn int64(maxVal-minVal) * int64(k)\n}"
      ruby: "# @param {Integer[]} nums\n# @param {Integer} k\n# @return {Integer}\n\
        def max_total_value(nums, k)\n  return 0 if nums.empty?\n  min_val, max_val\
        \ = nums.minmax\n  (max_val - min_val) * k\nend"
      scala: "object Solution {\n    def maxTotalValue(nums: Array[Int], k: Int): Long\
        \ = {\n        if (nums.isEmpty) return 0L\n        val minVal = nums.min\n\
        \        val maxVal = nums.max\n        (maxVal.toLong - minVal.toLong) * k.toLong\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn max_total_value(nums: Vec<i32>, k: i32) ->\
        \ i64 {\n        let mut max_val = i32::MIN;\n        let mut min_val = i32::MAX;\n\
        \        for &x in &nums {\n            if x > max_val {\n                max_val\
        \ = x;\n            }\n            if x < min_val {\n                min_val\
        \ = x;\n            }\n        }\n        (max_val as i64 - min_val as i64)\
        \ * (k as i64)\n    }\n}"
      racket: "(define/contract (max-total-value nums k)\n  (-> (listof exact-integer?)\
        \ exact-integer? exact-integer?)\n  (let ([max-v (apply max nums)]\n       \
        \ [min-v (apply min nums)])\n    (* (- max-v min-v) k)))"
      erlang: "-spec max_total_value(Nums :: [integer()], K :: integer()) -> integer().\n\
        max_total_value(Nums, K) ->\n  Max = lists:max(Nums),\n  Min = lists:min(Nums),\n\
        \  (Max - Min) * K."
      elixir: "defmodule Solution do\n  @spec max_total_value(nums :: [integer], k ::\
        \ integer) :: integer\n  def max_total_value(nums, k) do\n    {min_val, max_val}\
        \ = Enum.min_max(nums)\n    (max_val - min_val) * k\n  end\nend"
    approach: 'The core intuition is that the maximum value any single subarray can
      have is the difference between the global maximum and the global minimum of the
      entire array. Since we are required to pick exactly $k$ subarrays and are allowed
      to pick overlapping or identical ones multiple times, the optimal strategy is
      to repeatedly choose a subarray that contains both the global maximum and the
      global minimum. Picked subarray values are always bounded by the range of the
      entire array.


      Specifically, picking the entire array $k$ times is a simple way to achieve this,
      as the full array always encompasses every element, including those representing
      the absolute minimum and maximum values. The total value is thus the product of
      $k$ and the range calculated as $\max(nums) - \min(nums)$. This approach ensures
      we reach the theoretical upper bound of the sum since no individual subarray can
      provide a value larger than this difference.'
    time_complexity: O(n) where n is the length of the array nums. This complexity arises
      because we need to perform a single linear scan of the array to find the global
      maximum and minimum values.
    space_complexity: O(1) because we only store a constant number of variables (the
      maximum, minimum, and the result) regardless of the input size.
    elapsed_time: 298.9026973247528
    model: gemini-3-flash-preview
    generated_at: '2026-06-09 02:34:05 '
---

## Problem #3689: Maximum Total Subarray Value I

**Difficulty:** Medium

**Topics:** Array, Greedy

## Problem Description

<p>You are given an integer array <code>nums</code> of length <code>n</code> and an integer <code>k</code>.</p>

<p>You need to choose <strong>exactly</strong> <code>k</code> non-empty <span data-keyword="subarray-nonempty">subarrays</span> <code>nums[l..r]</code> of <code>nums</code>. Subarrays may overlap, and the exact same subarray (same <code>l</code> and <code>r</code>) <strong>can</strong> be chosen more than once.</p>

<p>The <strong>value</strong> of a subarray <code>nums[l..r]</code> is defined as: <code>max(nums[l..r]) - min(nums[l..r])</code>.</p>

<p>The <strong>total value</strong> is the sum of the <strong>values</strong> of all chosen subarrays.</p>

<p>Return the <strong>maximum</strong> possible total value you can achieve.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,3,2], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>One optimal approach is:</p>

<ul>
	<li>Choose <code>nums[0..1] = [1, 3]</code>. The maximum is 3 and the minimum is 1, giving a value of <code>3 - 1 = 2</code>.</li>
	<li>Choose <code>nums[0..2] = [1, 3, 2]</code>. The maximum is still 3 and the minimum is still 1, so the value is also <code>3 - 1 = 2</code>.</li>
</ul>

<p>Adding these gives <code>2 + 2 = 4</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,2,5,1], k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">12</span></p>

<p><strong>Explanation:</strong></p>

<p>One optimal approach is:</p>

<ul>
	<li>Choose <code>nums[0..3] = [4, 2, 5, 1]</code>. The maximum is 5 and the minimum is 1, giving a value of <code>5 - 1 = 4</code>.</li>
	<li>Choose <code>nums[0..3] = [4, 2, 5, 1]</code>. The maximum is 5 and the minimum is 1, so the value is also <code>4</code>.</li>
	<li>Choose <code>nums[2..3] = [5, 1]</code>. The maximum is 5 and the minimum is 1, so the value is again <code>4</code>.</li>
</ul>

<p>Adding these gives <code>4 + 4 + 4 = 12</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 5 * 10<sup>​​​​​​​4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. Choose the whole subarray `k` times.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The core intuition is that the maximum value any single subarray can have is the difference between the global maximum and the global minimum of the entire array. Since we are required to pick exactly $k$ subarrays and are allowed to pick overlapping or identical ones multiple times, the optimal strategy is to repeatedly choose a subarray that contains both the global maximum and the global minimum. Picked subarray values are always bounded by the range of the entire array.

Specifically, picking the entire array $k$ times is a simple way to achieve this, as the full array always encompasses every element, including those representing the absolute minimum and maximum values. The total value is thus the product of $k$ and the range calculated as $\max(nums) - \min(nums)$. This approach ensures we reach the theoretical upper bound of the sum since no individual subarray can provide a value larger than this difference.

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
    long long maxTotalValue(vector<int>& nums, int k) {
        int min_val = nums[0];
        int max_val = nums[0];
        for (int x : nums) {
            if (x < min_val) min_val = x;
            if (x > max_val) max_val = x;
        }
        return (long long)k * (max_val - min_val);
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public long maxTotalValue(int[] nums, int k) {
        int minVal = nums[0];
        int maxVal = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] < minVal) {
                minVal = nums[i];
            }
            if (nums[i] > maxVal) {
                maxVal = nums[i];
            }
        }
        return (long)k * (maxVal - minVal);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return k * (max(nums) - min(nums))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return k * (max(nums) - min(nums))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
long long maxTotalValue(int* nums, int numsSize, int k) {
    int min_val = nums[0];
    int max_val = nums[0];
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] < min_val) min_val = nums[i];
        if (nums[i] > max_val) max_val = nums[i];
    }
    return (long long)k * (max_val - min_val);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public long MaxTotalValue(int[] nums, int k) {
        int minVal = nums[0];
        int maxVal = nums[0];
        foreach (int num in nums) {
            if (num < minVal) minVal = num;
            if (num > maxVal) maxVal = num;
        }
        return (long)k * (maxVal - minVal);
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
 * @param {number} k
 * @return {number}
 */
var maxTotalValue = function(nums, k) {
    let minVal = nums[0];
    let maxVal = nums[0];
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] < minVal) minVal = nums[i];
        if (nums[i] > maxVal) maxVal = nums[i];
    }
    return k * (maxVal - minVal);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxTotalValue(nums: number[], k: number): number {
    let minVal: number = nums[0];
    let maxVal: number = nums[0];
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] < minVal) minVal = nums[i];
        if (nums[i] > maxVal) maxVal = nums[i];
    }
    return k * (maxVal - minVal);
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
     * @param Integer $k
     * @return Integer
     */
    function maxTotalValue($nums, $k) {
        $minVal = $nums[0];
        $maxVal = $nums[0];
        foreach ($nums as $num) {
            if ($num < $minVal) $minVal = $num;
            if ($num > $maxVal) $maxVal = $num;
        }
        return $k * ($maxVal - $minVal);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxTotalValue(_ nums: [Int], _ k: Int) -> Int {
        var minVal = nums[0]
        var maxVal = nums[0]
        for num in nums {
            if num < minVal { minVal = num }
            if num > maxVal { maxVal = num }
        }
        return k * (maxVal - minVal)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxTotalValue(nums: IntArray, k: Int): Long {
        if (nums.isEmpty()) return 0L
        var minVal = nums[0]
        var maxVal = nums[0]
        for (x in nums) {
            if (x < minVal) minVal = x
            if (x > maxVal) maxVal = x
        }
        return (maxVal.toLong() - minVal.toLong()) * k.toLong()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maxTotalValue(List<int> nums, int k) {
    if (nums.isEmpty()) return 0;
    int minVal = nums[0];
    int maxVal = nums[0];
    for (int i = 1; i < nums.length; i++) {
      if (nums[i] < minVal) minVal = nums[i];
      if (nums[i] > maxVal) maxVal = nums[i];
    }
    return (maxVal - minVal) * k;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxTotalValue(nums []int, k int) int64 {
	if len(nums) == 0 {
		return 0
	}
	minVal := nums[0]
	maxVal := nums[0]
	for _, x := range nums {
		if x < minVal {
			minVal = x
		}
		if x > maxVal {
			maxVal = x
		}
	}
	return int64(maxVal-minVal) * int64(k)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_total_value(nums, k)
  return 0 if nums.empty?
  min_val, max_val = nums.minmax
  (max_val - min_val) * k
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxTotalValue(nums: Array[Int], k: Int): Long = {
        if (nums.isEmpty) return 0L
        val minVal = nums.min
        val maxVal = nums.max
        (maxVal.toLong - minVal.toLong) * k.toLong
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_total_value(nums: Vec<i32>, k: i32) -> i64 {
        let mut max_val = i32::MIN;
        let mut min_val = i32::MAX;
        for &x in &nums {
            if x > max_val {
                max_val = x;
            }
            if x < min_val {
                min_val = x;
            }
        }
        (max_val as i64 - min_val as i64) * (k as i64)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (max-total-value nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let ([max-v (apply max nums)]
        [min-v (apply min nums)])
    (* (- max-v min-v) k)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_total_value(Nums :: [integer()], K :: integer()) -> integer().
max_total_value(Nums, K) ->
  Max = lists:max(Nums),
  Min = lists:min(Nums),
  (Max - Min) * K.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_total_value(nums :: [integer], k :: integer) :: integer
  def max_total_value(nums, k) do
    {min_val, max_val} = Enum.min_max(nums)
    (max_val - min_val) * k
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the array nums. This complexity arises because we need to perform a single linear scan of the array to find the global maximum and minimum values.
- **Space Complexity:** O(1) because we only store a constant number of variables (the maximum, minimum, and the result) regardless of the input size.
