---
layout: post
title: "Count Subarrays With Majority Element I"
date: 2026-06-25 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Divide and Conquer", "Segment Tree", "Merge Sort", "Counting", "Prefix Sum"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/count-subarrays-with-majority-element-i/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int countMajoritySubarrays(vector<int>& nums,\
        \ int target) {\n        int n = nums.size();\n        int result = 0;\n   \
        \     for (int i = 0; i < n; i++) {\n            int targetCount = 0;\n    \
        \        for (int j = i; j < n; j++) {\n                if (nums[j] == target)\
        \ {\n                    targetCount++;\n                }\n               \
        \ if (targetCount * 2 > (j - i + 1)) {\n                    result++;\n    \
        \            }\n            }\n        }\n        return result;\n    }\n};"
      java: "class Solution {\n    public int countMajoritySubarrays(int[] nums, int\
        \ target) {\n        int n = nums.length;\n        int result = 0;\n       \
        \ for (int i = 0; i < n; i++) {\n            int targetCount = 0;\n        \
        \    for (int j = i; j < n; j++) {\n                if (nums[j] == target) {\n\
        \                    targetCount++;\n                }\n                if (targetCount\
        \ * 2 > (j - i + 1)) {\n                    result++;\n                }\n \
        \           }\n        }\n        return result;\n    }\n}"
      python: "class Solution(object):\n    def countMajoritySubarrays(self, nums, target):\n\
        \        \"\"\"\n        :type nums: List[int]\n        :type target: int\n\
        \        :rtype: int\n        \"\"\"\n        n = len(nums)\n        result\
        \ = 0\n        for i in range(n):\n            target_count = 0\n          \
        \  for j in range(i, n):\n                if nums[j] == target:\n          \
        \          target_count += 1\n                if target_count * 2 > (j - i +\
        \ 1):\n                    result += 1\n        return result"
      python3: "class Solution:\n    def countMajoritySubarrays(self, nums: List[int],\
        \ target: int) -> int:\n        n = len(nums)\n        result = 0\n        for\
        \ i in range(n):\n            target_count = 0\n            for j in range(i,\
        \ n):\n                if nums[j] == target:\n                    target_count\
        \ += 1\n                if target_count * 2 > (j - i + 1):\n               \
        \     result += 1\n        return result"
      c: "int countMajoritySubarrays(int* nums, int numsSize, int target) {\n    int\
        \ result = 0;\n    for (int i = 0; i < numsSize; i++) {\n        int targetCount\
        \ = 0;\n        for (int j = i; j < numsSize; j++) {\n            if (nums[j]\
        \ == target) {\n                targetCount++;\n            }\n            if\
        \ (targetCount * 2 > (j - i + 1)) {\n                result++;\n           \
        \ }\n        }\n    }\n    return result;\n}"
      csharp: "public class Solution {\n    public int CountMajoritySubarrays(int[]\
        \ nums, int target) {\n        int n = nums.Length;\n        int totalCount\
        \ = 0;\n        for (int i = 0; i < n; i++) {\n            int balance = 0;\n\
        \            for (int j = i; j < n; j++) {\n                if (nums[j] == target)\
        \ {\n                    balance++;\n                } else {\n            \
        \        balance--;\n                }\n                if (balance > 0) {\n\
        \                    totalCount++;\n                }\n            }\n     \
        \   }\n        return totalCount;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} target\n * @return\
        \ {number}\n */\nvar countMajoritySubarrays = function(nums, target) {\n   \
        \ let n = nums.length;\n    let totalCount = 0;\n    for (let i = 0; i < n;\
        \ i++) {\n        let balance = 0;\n        for (let j = i; j < n; j++) {\n\
        \            if (nums[j] === target) {\n                balance++;\n       \
        \     } else {\n                balance--;\n            }\n            if (balance\
        \ > 0) {\n                totalCount++;\n            }\n        }\n    }\n \
        \   return totalCount;\n};"
      typescript: "function countMajoritySubarrays(nums: number[], target: number):\
        \ number {\n    let n = nums.length;\n    let totalCount = 0;\n    for (let\
        \ i = 0; i < n; i++) {\n        let balance = 0;\n        for (let j = i; j\
        \ < n; j++) {\n            if (nums[j] === target) {\n                balance++;\n\
        \            } else {\n                balance--;\n            }\n         \
        \   if (balance > 0) {\n                totalCount++;\n            }\n     \
        \   }\n    }\n    return totalCount;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer $target\n     * @return Integer\n     */\n    function countMajoritySubarrays($nums,\
        \ $target) {\n        $n = count($nums);\n        $totalCount = 0;\n       \
        \ for ($i = 0; $i < $n; $i++) {\n            $balance = 0;\n            for\
        \ ($j = $i; $j < $n; $j++) {\n                if ($nums[$j] == $target) {\n\
        \                    $balance++;\n                } else {\n               \
        \     $balance--;\n                }\n                if ($balance > 0) {\n\
        \                    $totalCount++;\n                }\n            }\n    \
        \    }\n        return $totalCount;\n    }\n}"
      swift: "class Solution {\n    func countMajoritySubarrays(_ nums: [Int], _ target:\
        \ Int) -> Int {\n        let n = nums.count\n        var totalCount = 0\n  \
        \      for i in 0..<n {\n            var balance = 0\n            for j in i..<n\
        \ {\n                if nums[j] == target {\n                    balance +=\
        \ 1\n                } else {\n                    balance -= 1\n          \
        \      }\n                if balance > 0 {\n                    totalCount +=\
        \ 1\n                }\n            }\n        }\n        return totalCount\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun countMajoritySubarrays(nums: IntArray, target:\
        \ Int): Int {\n        var totalCount = 0\n        val n = nums.size\n     \
        \   for (i in 0 until n) {\n            var targetFreq = 0\n            for\
        \ (j in i until n) {\n                if (nums[j] == target) {\n           \
        \         targetFreq++\n                }\n                val length = j -\
        \ i + 1\n                if (targetFreq * 2 > length) {\n                  \
        \  totalCount++\n                }\n            }\n        }\n        return\
        \ totalCount\n    }\n}"
      dart: "class Solution {\n  int countMajoritySubarrays(List<int> nums, int target)\
        \ {\n    int totalCount = 0;\n    int n = nums.length;\n    for (int i = 0;\
        \ i < n; i++) {\n      int targetFreq = 0;\n      for (int j = i; j < n; j++)\
        \ {\n        if (nums[j] == target) {\n          targetFreq++;\n        }\n\
        \        int length = j - i + 1;\n        if (targetFreq * 2 > length) {\n \
        \         totalCount++;\n        }\n      }\n    }\n    return totalCount;\n\
        \  }\n}"
      go: "func countMajoritySubarrays(nums []int, target int) int {\n    totalCount\
        \ := 0\n    n := len(nums)\n    for i := 0; i < n; i++ {\n        targetFreq\
        \ := 0\n        for j := i; j < n; j++ {\n            if nums[j] == target {\n\
        \                targetFreq++\n            }\n            length := j - i +\
        \ 1\n            if targetFreq * 2 > length {\n                totalCount++\n\
        \            }\n        }\n    }\n    return totalCount\n}"
      ruby: "# @param {Integer[]} nums\n# @param {Integer} target\n# @return {Integer}\n\
        def count_majority_subarrays(nums, target)\n  total_count = 0\n  n = nums.length\n\
        \  (0...n).each do |i|\n    target_freq = 0\n    (i...n).each do |j|\n     \
        \ target_freq += 1 if nums[j] == target\n      length = j - i + 1\n      total_count\
        \ += 1 if target_freq * 2 > length\n    end\n  end\n  total_count\nend"
      scala: "object Solution {\n    def countMajoritySubarrays(nums: Array[Int], target:\
        \ Int): Int = {\n        var totalCount = 0\n        val n = nums.length\n \
        \       for (i <- 0 until n) {\n            var targetFreq = 0\n           \
        \ for (j <- i until n) {\n                if (nums(j) == target) {\n       \
        \             targetFreq += 1\n                }\n                val length\
        \ = j - i + 1\n                if (targetFreq * 2 > length) {\n            \
        \        totalCount += 1\n                }\n            }\n        }\n    \
        \    totalCount\n    }\n}"
      rust: "impl Solution {\n    pub fn count_majority_subarrays(nums: Vec<i32>, target:\
        \ i32) -> i32 {\n        let n = nums.len();\n        let mut ans = 0;\n   \
        \     for i in 0..n {\n            let mut current_sum = 0;\n            for\
        \ j in i..n {\n                if nums[j] == target {\n                    current_sum\
        \ += 1;\n                } else {\n                    current_sum -= 1;\n \
        \               }\n                if current_sum > 0 {\n                  \
        \  ans += 1;\n                }\n            }\n        }\n        ans\n   \
        \ }\n}"
      racket: "(define/contract (count-majority-subarrays nums target)\n  (-> (listof\
        \ exact-integer?) exact-integer? exact-integer?)\n  (let loop-i ([lst nums]\
        \ [total-count 0])\n    (if (null? lst)\n        total-count\n        (let loop-j\
        \ ([inner-lst lst] [current-sum 0] [inner-count 0])\n          (if (null? inner-lst)\n\
        \              (loop-i (cdr lst) (+ total-count inner-count))\n            \
        \  (let* ([val (if (= (car inner-lst) target) 1 -1)]\n                     [new-sum\
        \ (+ current-sum val)])\n                (loop-j (cdr inner-lst) new-sum (+\
        \ inner-count (if (> new-sum 0) 1 0))))))))\n)"
      erlang: "-spec count_majority_subarrays(Nums :: [integer()], Target :: integer())\
        \ -> integer().\ncount_majority_subarrays(Nums, Target) ->\n    count_i(Nums,\
        \ Target, 0).\n\ncount_i([], _Target, TotalCount) ->\n    TotalCount;\ncount_i([_H\
        \ | T] = Lst, Target, TotalCount) ->\n    InnerCount = count_j(Lst, Target,\
        \ 0, 0),\n    count_i(T, Target, TotalCount + InnerCount).\n\ncount_j([], _Target,\
        \ _CurrentSum, InnerCount) ->\n    InnerCount;\ncount_j([H | T], Target, CurrentSum,\
        \ InnerCount) ->\n    Val = if H =:= Target -> 1; true -> -1 end,\n    NewSum\
        \ = CurrentSum + Val,\n    NewInnerCount = if NewSum > 0 -> InnerCount + 1;\
        \ true -> InnerCount end,\n    count_j(T, Target, NewSum, NewInnerCount)."
      elixir: "defmodule Solution do\n  @spec count_majority_subarrays(nums :: [integer],\
        \ target :: integer) :: integer\n  def count_majority_subarrays(nums, target)\
        \ do\n    count_i(nums, target, 0)\n  end\n\n  defp count_i([], _target, total_count)\
        \ do\n    total_count\n  end\n\n  defp count_i([_h | t] = lst, target, total_count)\
        \ do\n    inner_count = count_j(lst, target, 0, 0)\n    count_i(t, target, total_count\
        \ + inner_count)\n  end\n\n  defp count_j([], _target, _current_sum, inner_count)\
        \ do\n    inner_count\n  end\n\n  defp count_j([h | t], target, current_sum,\
        \ inner_count) do\n    val = if h == target, do: 1, else: -1\n    new_sum =\
        \ current_sum + val\n    new_inner_count = if new_sum > 0, do: inner_count +\
        \ 1, else: inner_count\n    count_j(t, target, new_sum, new_inner_count)\n \
        \ end\nend"
    approach: "To solve this problem, we iterate through all possible subarrays of the\
      \ given array and check the majority condition for each. For a subarray starting\
      \ at index 'i' and ending at index 'j', the target is considered the majority\
      \ element if its frequency 'C' is strictly greater than half the length of the\
      \ subarray, which is expressed by the condition $2 * C > (j - i + 1)$. \n\nWe\
      \ implement this using a nested loop where the outer loop fixes the starting point\
      \ and the inner loop expands the ending point. By maintaining a running count\
      \ of the target's occurrences as we expand the subarray in the inner loop, we\
      \ can evaluate the majority condition in constant time for each segment. This\
      \ brute-force approach effectively explores all $O(n^2)$ subarrays, making it\
      \ efficient for the given constraints where the array length is up to 1000."
    time_complexity: O(n^2) where n is the length of the input array. This is due to
      the two nested loops that iterate through every possible starting and ending index
      to identify all contiguous subarrays.
    space_complexity: O(1) because we only use a constant amount of extra space for
      variables such as the running counter and indices, independent of the input size.
    elapsed_time: 137.59534668922424
    model: gemini-3-flash-preview
    generated_at: '2026-06-25 02:38:35 '
---

## Problem #3737: Count Subarrays With Majority Element I

**Difficulty:** Medium

**Topics:** Array, Hash Table, Divide and Conquer, Segment Tree, Merge Sort, Counting, Prefix Sum

## Problem Description

<p>You are given an integer array <code>nums</code> and an integer <code>target</code>.</p>

<p>Return the number of <strong><span data-keyword="subarray-nonempty">subarrays</span></strong> of <code>nums</code> in which <code>target</code> is the <strong>majority element</strong>.</p>

<p>The <strong>majority element</strong> of a subarray is the element that appears <strong>strictly</strong> <strong>more than half</strong> of the times in that subarray.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,2,3], target = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p>Valid subarrays with <code>target = 2</code> as the majority element:</p>

<ul>
	<li><code>nums[1..1] = [2]</code></li>
	<li><code>nums[2..2] = [2]</code></li>
	<li><code>nums[1..2] = [2,2]</code></li>
	<li><code>nums[0..2] = [1,2,2]</code></li>
	<li><code>nums[1..3] = [2,2,3]</code></li>
</ul>

<p>So there are 5 such subarrays.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,1,1], target = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">10</span></p>

<p><strong>Explanation: </strong></p>

<p><strong>​​​​​​​</strong>All 10 subarrays have 1 as the majority element.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3], target = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p><code>target = 4</code> does not appear in <code>nums</code> at all. Therefore, there cannot be any subarray where 4 is the majority element. Hence the answer is 0.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>​​​​​​​9</sup></code></li>
	<li><code>1 &lt;= target &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. Use brute force

2. Count all subarrays where `2 * count(target) > length`

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To solve this problem, we iterate through all possible subarrays of the given array and check the majority condition for each. For a subarray starting at index 'i' and ending at index 'j', the target is considered the majority element if its frequency 'C' is strictly greater than half the length of the subarray, which is expressed by the condition $2 * C > (j - i + 1)$. 

We implement this using a nested loop where the outer loop fixes the starting point and the inner loop expands the ending point. By maintaining a running count of the target's occurrences as we expand the subarray in the inner loop, we can evaluate the majority condition in constant time for each segment. This brute-force approach effectively explores all $O(n^2)$ subarrays, making it efficient for the given constraints where the array length is up to 1000.

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
    int countMajoritySubarrays(vector<int>& nums, int target) {
        int n = nums.size();
        int result = 0;
        for (int i = 0; i < n; i++) {
            int targetCount = 0;
            for (int j = i; j < n; j++) {
                if (nums[j] == target) {
                    targetCount++;
                }
                if (targetCount * 2 > (j - i + 1)) {
                    result++;
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
class Solution {
    public int countMajoritySubarrays(int[] nums, int target) {
        int n = nums.length;
        int result = 0;
        for (int i = 0; i < n; i++) {
            int targetCount = 0;
            for (int j = i; j < n; j++) {
                if (nums[j] == target) {
                    targetCount++;
                }
                if (targetCount * 2 > (j - i + 1)) {
                    result++;
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
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        result = 0
        for i in range(n):
            target_count = 0
            for j in range(i, n):
                if nums[j] == target:
                    target_count += 1
                if target_count * 2 > (j - i + 1):
                    result += 1
        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        result = 0
        for i in range(n):
            target_count = 0
            for j in range(i, n):
                if nums[j] == target:
                    target_count += 1
                if target_count * 2 > (j - i + 1):
                    result += 1
        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int countMajoritySubarrays(int* nums, int numsSize, int target) {
    int result = 0;
    for (int i = 0; i < numsSize; i++) {
        int targetCount = 0;
        for (int j = i; j < numsSize; j++) {
            if (nums[j] == target) {
                targetCount++;
            }
            if (targetCount * 2 > (j - i + 1)) {
                result++;
            }
        }
    }
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int CountMajoritySubarrays(int[] nums, int target) {
        int n = nums.Length;
        int totalCount = 0;
        for (int i = 0; i < n; i++) {
            int balance = 0;
            for (int j = i; j < n; j++) {
                if (nums[j] == target) {
                    balance++;
                } else {
                    balance--;
                }
                if (balance > 0) {
                    totalCount++;
                }
            }
        }
        return totalCount;
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
 * @param {number} target
 * @return {number}
 */
var countMajoritySubarrays = function(nums, target) {
    let n = nums.length;
    let totalCount = 0;
    for (let i = 0; i < n; i++) {
        let balance = 0;
        for (let j = i; j < n; j++) {
            if (nums[j] === target) {
                balance++;
            } else {
                balance--;
            }
            if (balance > 0) {
                totalCount++;
            }
        }
    }
    return totalCount;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countMajoritySubarrays(nums: number[], target: number): number {
    let n = nums.length;
    let totalCount = 0;
    for (let i = 0; i < n; i++) {
        let balance = 0;
        for (let j = i; j < n; j++) {
            if (nums[j] === target) {
                balance++;
            } else {
                balance--;
            }
            if (balance > 0) {
                totalCount++;
            }
        }
    }
    return totalCount;
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
     * @param Integer $target
     * @return Integer
     */
    function countMajoritySubarrays($nums, $target) {
        $n = count($nums);
        $totalCount = 0;
        for ($i = 0; $i < $n; $i++) {
            $balance = 0;
            for ($j = $i; $j < $n; $j++) {
                if ($nums[$j] == $target) {
                    $balance++;
                } else {
                    $balance--;
                }
                if ($balance > 0) {
                    $totalCount++;
                }
            }
        }
        return $totalCount;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func countMajoritySubarrays(_ nums: [Int], _ target: Int) -> Int {
        let n = nums.count
        var totalCount = 0
        for i in 0..<n {
            var balance = 0
            for j in i..<n {
                if nums[j] == target {
                    balance += 1
                } else {
                    balance -= 1
                }
                if balance > 0 {
                    totalCount += 1
                }
            }
        }
        return totalCount
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun countMajoritySubarrays(nums: IntArray, target: Int): Int {
        var totalCount = 0
        val n = nums.size
        for (i in 0 until n) {
            var targetFreq = 0
            for (j in i until n) {
                if (nums[j] == target) {
                    targetFreq++
                }
                val length = j - i + 1
                if (targetFreq * 2 > length) {
                    totalCount++
                }
            }
        }
        return totalCount
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int countMajoritySubarrays(List<int> nums, int target) {
    int totalCount = 0;
    int n = nums.length;
    for (int i = 0; i < n; i++) {
      int targetFreq = 0;
      for (int j = i; j < n; j++) {
        if (nums[j] == target) {
          targetFreq++;
        }
        int length = j - i + 1;
        if (targetFreq * 2 > length) {
          totalCount++;
        }
      }
    }
    return totalCount;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func countMajoritySubarrays(nums []int, target int) int {
    totalCount := 0
    n := len(nums)
    for i := 0; i < n; i++ {
        targetFreq := 0
        for j := i; j < n; j++ {
            if nums[j] == target {
                targetFreq++
            }
            length := j - i + 1
            if targetFreq * 2 > length {
                totalCount++
            }
        }
    }
    return totalCount
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def count_majority_subarrays(nums, target)
  total_count = 0
  n = nums.length
  (0...n).each do |i|
    target_freq = 0
    (i...n).each do |j|
      target_freq += 1 if nums[j] == target
      length = j - i + 1
      total_count += 1 if target_freq * 2 > length
    end
  end
  total_count
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def countMajoritySubarrays(nums: Array[Int], target: Int): Int = {
        var totalCount = 0
        val n = nums.length
        for (i <- 0 until n) {
            var targetFreq = 0
            for (j <- i until n) {
                if (nums(j) == target) {
                    targetFreq += 1
                }
                val length = j - i + 1
                if (targetFreq * 2 > length) {
                    totalCount += 1
                }
            }
        }
        totalCount
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn count_majority_subarrays(nums: Vec<i32>, target: i32) -> i32 {
        let n = nums.len();
        let mut ans = 0;
        for i in 0..n {
            let mut current_sum = 0;
            for j in i..n {
                if nums[j] == target {
                    current_sum += 1;
                } else {
                    current_sum -= 1;
                }
                if current_sum > 0 {
                    ans += 1;
                }
            }
        }
        ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (count-majority-subarrays nums target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let loop-i ([lst nums] [total-count 0])
    (if (null? lst)
        total-count
        (let loop-j ([inner-lst lst] [current-sum 0] [inner-count 0])
          (if (null? inner-lst)
              (loop-i (cdr lst) (+ total-count inner-count))
              (let* ([val (if (= (car inner-lst) target) 1 -1)]
                     [new-sum (+ current-sum val)])
                (loop-j (cdr inner-lst) new-sum (+ inner-count (if (> new-sum 0) 1 0))))))))
)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec count_majority_subarrays(Nums :: [integer()], Target :: integer()) -> integer().
count_majority_subarrays(Nums, Target) ->
    count_i(Nums, Target, 0).

count_i([], _Target, TotalCount) ->
    TotalCount;
count_i([_H | T] = Lst, Target, TotalCount) ->
    InnerCount = count_j(Lst, Target, 0, 0),
    count_i(T, Target, TotalCount + InnerCount).

count_j([], _Target, _CurrentSum, InnerCount) ->
    InnerCount;
count_j([H | T], Target, CurrentSum, InnerCount) ->
    Val = if H =:= Target -> 1; true -> -1 end,
    NewSum = CurrentSum + Val,
    NewInnerCount = if NewSum > 0 -> InnerCount + 1; true -> InnerCount end,
    count_j(T, Target, NewSum, NewInnerCount).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec count_majority_subarrays(nums :: [integer], target :: integer) :: integer
  def count_majority_subarrays(nums, target) do
    count_i(nums, target, 0)
  end

  defp count_i([], _target, total_count) do
    total_count
  end

  defp count_i([_h | t] = lst, target, total_count) do
    inner_count = count_j(lst, target, 0, 0)
    count_i(t, target, total_count + inner_count)
  end

  defp count_j([], _target, _current_sum, inner_count) do
    inner_count
  end

  defp count_j([h | t], target, current_sum, inner_count) do
    val = if h == target, do: 1, else: -1
    new_sum = current_sum + val
    new_inner_count = if new_sum > 0, do: inner_count + 1, else: inner_count
    count_j(t, target, new_sum, new_inner_count)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n^2) where n is the length of the input array. This is due to the two nested loops that iterate through every possible starting and ending index to identify all contiguous subarrays.
- **Space Complexity:** O(1) because we only use a constant amount of extra space for variables such as the running counter and indices, independent of the input size.
