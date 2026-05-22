---
layout: post
title: "Search in Rotated Sorted Array"
date: 2026-05-22 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Binary Search"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/search-in-rotated-sorted-array/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int search(vector<int>& nums, int target)\
        \ {\n        int left = 0;\n        int right = nums.size() - 1;\n\n       \
        \ while (left <= right) {\n            int mid = left + (right - left) / 2;\n\
        \            if (nums[mid] == target) {\n                return mid;\n     \
        \       }\n\n            if (nums[left] <= nums[mid]) {\n                if\
        \ (nums[left] <= target && target < nums[mid]) {\n                    right\
        \ = mid - 1;\n                } else {\n                    left = mid + 1;\n\
        \                }\n            } else {\n                if (nums[mid] < target\
        \ && target <= nums[right]) {\n                    left = mid + 1;\n       \
        \         } else {\n                    right = mid - 1;\n                }\n\
        \            }\n        }\n\n        return -1;\n    }\n};"
      java: "class Solution {\n    public int search(int[] nums, int target) {\n   \
        \     int left = 0;\n        int right = nums.length - 1;\n\n        while (left\
        \ <= right) {\n            int mid = left + (right - left) / 2;\n          \
        \  if (nums[mid] == target) {\n                return mid;\n            }\n\n\
        \            if (nums[left] <= nums[mid]) {\n                if (nums[left]\
        \ <= target && target < nums[mid]) {\n                    right = mid - 1;\n\
        \                } else {\n                    left = mid + 1;\n           \
        \     }\n            } else {\n                if (nums[mid] < target && target\
        \ <= nums[right]) {\n                    left = mid + 1;\n                }\
        \ else {\n                    right = mid - 1;\n                }\n        \
        \    }\n        }\n\n        return -1;\n    }\n}"
      python: "class Solution(object):\n    def search(self, nums, target):\n      \
        \  \"\"\"\n        :type nums: List[int]\n        :type target: int\n      \
        \  :rtype: int\n        \"\"\"\n        left = 0\n        right = len(nums)\
        \ - 1\n\n        while left <= right:\n            mid = left + (right - left)\
        \ // 2\n            if nums[mid] == target:\n                return mid\n\n\
        \            if nums[left] <= nums[mid]:\n                if nums[left] <= target\
        \ < nums[mid]:\n                    right = mid - 1\n                else:\n\
        \                    left = mid + 1\n            else:\n                if nums[mid]\
        \ < target <= nums[right]:\n                    left = mid + 1\n           \
        \     else:\n                    right = mid - 1\n\n        return -1"
      python3: "class Solution:\n    def search(self, nums: List[int], target: int)\
        \ -> int:\n        left = 0\n        right = len(nums) - 1\n\n        while\
        \ left <= right:\n            mid = left + (right - left) // 2\n           \
        \ if nums[mid] == target:\n                return mid\n\n            if nums[left]\
        \ <= nums[mid]:\n                if nums[left] <= target < nums[mid]:\n    \
        \                right = mid - 1\n                else:\n                  \
        \  left = mid + 1\n            else:\n                if nums[mid] < target\
        \ <= nums[right]:\n                    left = mid + 1\n                else:\n\
        \                    right = mid - 1\n\n        return -1"
      c: "int search(int* nums, int numsSize, int target) {\n    int left = 0;\n   \
        \ int right = numsSize - 1;\n\n    while (left <= right) {\n        int mid\
        \ = left + (right - left) / 2;\n        if (nums[mid] == target) {\n       \
        \     return mid;\n        }\n\n        if (nums[left] <= nums[mid]) {\n   \
        \         if (nums[left] <= target && target < nums[mid]) {\n              \
        \  right = mid - 1;\n            } else {\n                left = mid + 1;\n\
        \            }\n        } else {\n            if (nums[mid] < target && target\
        \ <= nums[right]) {\n                left = mid + 1;\n            } else {\n\
        \                right = mid - 1;\n            }\n        }\n    }\n\n    return\
        \ -1;\n}"
      csharp: "public class Solution {\n    public int Search(int[] nums, int target)\
        \ {\n        int left = 0;\n        int right = nums.Length - 1;\n\n       \
        \ while (left <= right) {\n            int mid = left + (right - left) / 2;\n\
        \            if (nums[mid] == target) {\n                return mid;\n     \
        \       }\n\n            if (nums[left] <= nums[mid]) {\n                if\
        \ (target >= nums[left] && target < nums[mid]) {\n                    right\
        \ = mid - 1;\n                } else {\n                    left = mid + 1;\n\
        \                }\n            } else {\n                if (target > nums[mid]\
        \ && target <= nums[right]) {\n                    left = mid + 1;\n       \
        \         } else {\n                    right = mid - 1;\n                }\n\
        \            }\n        }\n\n        return -1;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} target\n * @return\
        \ {number}\n */\nvar search = function(nums, target) {\n    let left = 0;\n\
        \    let right = nums.length - 1;\n\n    while (left <= right) {\n        let\
        \ mid = Math.floor(left + (right - left) / 2);\n        if (nums[mid] === target)\
        \ {\n            return mid;\n        }\n\n        if (nums[left] <= nums[mid])\
        \ {\n            if (target >= nums[left] && target < nums[mid]) {\n       \
        \         right = mid - 1;\n            } else {\n                left = mid\
        \ + 1;\n            }\n        } else {\n            if (target > nums[mid]\
        \ && target <= nums[right]) {\n                left = mid + 1;\n           \
        \ } else {\n                right = mid - 1;\n            }\n        }\n   \
        \ }\n\n    return -1;\n};"
      typescript: "function search(nums: number[], target: number): number {\n    let\
        \ left: number = 0;\n    let right: number = nums.length - 1;\n\n    while (left\
        \ <= right) {\n        let mid: number = Math.floor(left + (right - left) /\
        \ 2);\n        if (nums[mid] === target) {\n            return mid;\n      \
        \  }\n\n        if (nums[left] <= nums[mid]) {\n            if (target >= nums[left]\
        \ && target < nums[mid]) {\n                right = mid - 1;\n            }\
        \ else {\n                left = mid + 1;\n            }\n        } else {\n\
        \            if (target > nums[mid] && target <= nums[right]) {\n          \
        \      left = mid + 1;\n            } else {\n                right = mid -\
        \ 1;\n            }\n        }\n    }\n\n    return -1;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer $target\n     * @return Integer\n     */\n    function search($nums,\
        \ $target) {\n        $left = 0;\n        $right = count($nums) - 1;\n\n   \
        \     while ($left <= $right) {\n            $mid = $left + floor(($right -\
        \ $left) / 2);\n            if ($nums[$mid] == $target) {\n                return\
        \ $mid;\n            }\n\n            if ($nums[$left] <= $nums[$mid]) {\n \
        \               if ($target >= $nums[$left] && $target < $nums[$mid]) {\n  \
        \                  $right = $mid - 1;\n                } else {\n          \
        \          $left = $mid + 1;\n                }\n            } else {\n    \
        \            if ($target > $nums[$mid] && $target <= $nums[$right]) {\n    \
        \                $left = $mid + 1;\n                } else {\n             \
        \       $right = $mid - 1;\n                }\n            }\n        }\n\n\
        \        return -1;\n    }\n}"
      swift: "class Solution {\n    func search(_ nums: [Int], _ target: Int) -> Int\
        \ {\n        var left = 0\n        var right = nums.count - 1\n\n        while\
        \ left <= right {\n            let mid = left + (right - left) / 2\n       \
        \     if nums[mid] == target {\n                return mid\n            }\n\n\
        \            if nums[left] <= nums[mid] {\n                if target >= nums[left]\
        \ && target < nums[mid] {\n                    right = mid - 1\n           \
        \     } else {\n                    left = mid + 1\n                }\n    \
        \        } else {\n                if target > nums[mid] && target <= nums[right]\
        \ {\n                    left = mid + 1\n                } else {\n        \
        \            right = mid - 1\n                }\n            }\n        }\n\n\
        \        return -1\n    }\n}"
      kotlin: "class Solution {\n    fun search(nums: IntArray, target: Int): Int {\n\
        \        var left = 0\n        var right = nums.size - 1\n\n        while (left\
        \ <= right) {\n            val mid = left + (right - left) / 2\n           \
        \ if (nums[mid] == target) return mid\n\n            if (nums[left] <= nums[mid])\
        \ {\n                if (target >= nums[left] && target < nums[mid]) {\n   \
        \                 right = mid - 1\n                } else {\n              \
        \      left = mid + 1\n                }\n            } else {\n           \
        \     if (target > nums[mid] && target <= nums[right]) {\n                 \
        \   left = mid + 1\n                } else {\n                    right = mid\
        \ - 1\n                }\n            }\n        }\n\n        return -1\n  \
        \  }\n}"
      dart: "class Solution {\n  int search(List<int> nums, int target) {\n    int left\
        \ = 0;\n    int right = nums.length - 1;\n\n    while (left <= right) {\n  \
        \    int mid = left + (right - left) ~/ 2;\n      if (nums[mid] == target) return\
        \ mid;\n\n      if (nums[left] <= nums[mid]) {\n        if (target >= nums[left]\
        \ && target < nums[mid]) {\n          right = mid - 1;\n        } else {\n \
        \         left = mid + 1;\n        }\n      } else {\n        if (target > nums[mid]\
        \ && target <= nums[right]) {\n          left = mid + 1;\n        } else {\n\
        \          right = mid - 1;\n        }\n      }\n    }\n\n    return -1;\n \
        \ }\n}"
      go: "func search(nums []int, target int) int {\n    left := 0\n    right := len(nums)\
        \ - 1\n\n    for left <= right {\n        mid := left + (right-left)/2\n   \
        \     if nums[mid] == target {\n            return mid\n        }\n\n      \
        \  if nums[left] <= nums[mid] {\n            if target >= nums[left] && target\
        \ < nums[mid] {\n                right = mid - 1\n            } else {\n   \
        \             left = mid + 1\n            }\n        } else {\n            if\
        \ target > nums[mid] && target <= nums[right] {\n                left = mid\
        \ + 1\n            } else {\n                right = mid - 1\n            }\n\
        \        }\n    }\n\n    return -1\n}"
      ruby: "# @param {Integer[]} nums\n# @param {Integer} target\n# @return {Integer}\n\
        def search(nums, target)\n    left = 0\n    right = nums.length - 1\n\n    while\
        \ left <= right\n        mid = left + (right - left) / 2\n        return mid\
        \ if nums[mid] == target\n\n        if nums[left] <= nums[mid]\n           \
        \ if target >= nums[left] && target < nums[mid]\n                right = mid\
        \ - 1\n            else\n                left = mid + 1\n            end\n \
        \       else\n            if target > nums[mid] && target <= nums[right]\n \
        \               left = mid + 1\n            else\n                right = mid\
        \ - 1\n            end\n        end\n    end\n\n    -1\nend"
      scala: "object Solution {\n    def search(nums: Array[Int], target: Int): Int\
        \ = {\n        var left = 0\n        var right = nums.length - 1\n\n       \
        \ while (left <= right) {\n            val mid = left + (right - left) / 2\n\
        \            if (nums(mid) == target) return mid\n\n            if (nums(left)\
        \ <= nums(mid)) {\n                if (target >= nums(left) && target < nums(mid))\
        \ {\n                    right = mid - 1\n                } else {\n       \
        \             left = mid + 1\n                }\n            } else {\n    \
        \            if (target > nums(mid) && target <= nums(right)) {\n          \
        \          left = mid + 1\n                } else {\n                    right\
        \ = mid - 1\n                }\n            }\n        }\n\n        -1\n   \
        \ }\n}"
      rust: "impl Solution {\n    pub fn search(nums: Vec<i32>, target: i32) -> i32\
        \ {\n        let mut low: i32 = 0;\n        let mut high: i32 = nums.len() as\
        \ i32 - 1;\n\n        while low <= high {\n            let mid = low + (high\
        \ - low) / 2;\n            let mid_val = nums[mid as usize];\n\n           \
        \ if mid_val == target {\n                return mid;\n            }\n\n   \
        \         let low_val = nums[low as usize];\n            let high_val = nums[high\
        \ as usize];\n\n            if low_val <= mid_val {\n                if target\
        \ >= low_val && target < mid_val {\n                    high = mid - 1;\n  \
        \              } else {\n                    low = mid + 1;\n              \
        \  }\n            } else {\n                if target > mid_val && target <=\
        \ high_val {\n                    low = mid + 1;\n                } else {\n\
        \                    high = mid - 1;\n                }\n            }\n   \
        \     }\n\n        -1\n    }\n}"
      racket: "(define/contract (search nums target)\n  (-> (listof exact-integer?)\
        \ exact-integer? exact-integer?)\n  (let ([vec (list->vector nums)])\n    (let\
        \ loop ([low 0]\n               [high (- (vector-length vec) 1)])\n      (if\
        \ (> low high)\n          -1\n          (let* ([mid (quotient (+ low high) 2)]\n\
        \                 [mid-val (vector-ref vec mid)]\n                 [low-val\
        \ (vector-ref vec low)]\n                 [high-val (vector-ref vec high)])\n\
        \            (cond\n              [(= mid-val target) mid]\n              [(<=\
        \ low-val mid-val)\n               (if (and (>= target low-val) (< target mid-val))\n\
        \                   (loop low (- mid 1))\n                   (loop (+ mid 1)\
        \ high))]\n              [else\n               (if (and (> target mid-val) (<=\
        \ target high-val))\n                   (loop (+ mid 1) high)\n            \
        \       (loop low (- mid 1)))]))))))"
      erlang: "-spec search(Nums :: [integer()], Target :: integer()) -> integer().\n\
        search(Nums, Target) ->\n  Arr = list_to_tuple(Nums),\n  binary_search(Arr,\
        \ Target, 1, tuple_size(Arr)).\n\nbinary_search(_Arr, _Target, Low, High) when\
        \ Low > High ->\n  -1;\nbinary_search(Arr, Target, Low, High) ->\n  Mid = (Low\
        \ + High) div 2,\n  MidVal = element(Mid, Arr),\n  LowVal = element(Low, Arr),\n\
        \  HighVal = element(High, Arr),\n  if\n    MidVal == Target ->\n      Mid -\
        \ 1;\n    LowVal =< MidVal ->\n      if\n        Target >= LowVal andalso Target\
        \ < MidVal ->\n          binary_search(Arr, Target, Low, Mid - 1);\n       \
        \ true ->\n          binary_search(Arr, Target, Mid + 1, High)\n      end;\n\
        \    true ->\n      if\n        Target > MidVal andalso Target =< HighVal ->\n\
        \          binary_search(Arr, Target, Mid + 1, High);\n        true ->\n   \
        \       binary_search(Arr, Target, Low, Mid - 1)\n      end\n  end."
      elixir: "defmodule Solution do\n  @spec search(nums :: [integer], target :: integer)\
        \ :: integer\n  def search(nums, target) do\n    nums_tuple = List.to_tuple(nums)\n\
        \    search_recursive(nums_tuple, target, 0, tuple_size(nums_tuple) - 1)\n \
        \ end\n\n  defp search_recursive(_nums_tuple, _target, low, high) when low >\
        \ high do\n    -1\n  end\n\n  defp search_recursive(nums_tuple, target, low,\
        \ high) do\n    mid = div(low + high, 2)\n    mid_val = elem(nums_tuple, mid)\n\
        \    low_val = elem(nums_tuple, low)\n    high_val = elem(nums_tuple, high)\n\
        \n    cond do\n      mid_val == target ->\n        mid\n      low_val <= mid_val\
        \ ->\n        if target >= low_val and target < mid_val do\n          search_recursive(nums_tuple,\
        \ target, low, mid - 1)\n        else\n          search_recursive(nums_tuple,\
        \ target, mid + 1, high)\n        end\n      true ->\n        if target > mid_val\
        \ and target <= high_val do\n          search_recursive(nums_tuple, target,\
        \ mid + 1, high)\n        else\n          search_recursive(nums_tuple, target,\
        \ low, mid - 1)\n        end\n    end\n  end\nend"
    approach: 'The algorithm employs a modified binary search to achieve logarithmic
      time complexity. In a rotated sorted array, for any middle index chosen, at least
      one half of the array (either from the start to the middle or from the middle
      to the end) will remain sorted. By comparing the value at the middle index with
      the value at the left boundary, we can determine which half is sorted and whether
      the target value potentially lies within that range.


      Once the sorted half is identified, we check if the target falls within its lower
      and upper bounds. If it does, we adjust our search pointers to narrow down on
      that side; otherwise, we shift to the opposite half. This process repeats, effectively
      halving the search space in each iteration until the target is found or the pointers
      cross, indicating the target is not present in the array.'
    time_complexity: O(log n) because the search space is reduced by half in each iteration
      of the binary search, resulting in a logarithmic number of steps relative to the
      size of the input array.
    space_complexity: O(1) as the algorithm only requires a constant amount of extra
      space for the left, right, and middle pointers, regardless of the input size.
    elapsed_time: 52.276548624038696
    model: gemini-3-flash-preview
    generated_at: '2026-05-22 02:40:42 '
---

## Problem #33: Search in Rotated Sorted Array

**Difficulty:** Medium

**Topics:** Array, Binary Search

## Problem Description

<p>There is an integer array <code>nums</code> sorted in ascending order (with <strong>distinct</strong> values).</p>

<p>Prior to being passed to your function, <code>nums</code> is <strong>possibly left rotated</strong> at an unknown index <code>k</code> (<code>1 &lt;= k &lt; nums.length</code>) such that the resulting array is <code>[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]</code> (<strong>0-indexed</strong>). For example, <code>[0,1,2,4,5,6,7]</code> might be left rotated by&nbsp;<code>3</code>&nbsp;indices and become <code>[4,5,6,7,0,1,2]</code>.</p>

<p>Given the array <code>nums</code> <strong>after</strong> the possible rotation and an integer <code>target</code>, return <em>the index of </em><code>target</code><em> if it is in </em><code>nums</code><em>, or </em><code>-1</code><em> if it is not in </em><code>nums</code>.</p>

<p>You must write an algorithm with <code>O(log n)</code> runtime complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [4,5,6,7,0,1,2], target = 0
<strong>Output:</strong> 4
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [4,5,6,7,0,1,2], target = 3
<strong>Output:</strong> -1
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1], target = 0
<strong>Output:</strong> -1
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5000</code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li>All values of <code>nums</code> are <strong>unique</strong>.</li>
	<li><code>nums</code> is an ascending array that is possibly rotated.</li>
	<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm employs a modified binary search to achieve logarithmic time complexity. In a rotated sorted array, for any middle index chosen, at least one half of the array (either from the start to the middle or from the middle to the end) will remain sorted. By comparing the value at the middle index with the value at the left boundary, we can determine which half is sorted and whether the target value potentially lies within that range.

Once the sorted half is identified, we check if the target falls within its lower and upper bounds. If it does, we adjust our search pointers to narrow down on that side; otherwise, we shift to the opposite half. This process repeats, effectively halving the search space in each iteration until the target is found or the pointers cross, indicating the target is not present in the array.

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
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            }

            if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        return -1;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            }

            if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        return -1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int search(int* nums, int numsSize, int target) {
    int left = 0;
    int right = numsSize - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            return mid;
        }

        if (nums[left] <= nums[mid]) {
            if (nums[left] <= target && target < nums[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        } else {
            if (nums[mid] < target && target <= nums[right]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    }

    return -1;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int Search(int[] nums, int target) {
        int left = 0;
        int right = nums.Length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            }

            if (nums[left] <= nums[mid]) {
                if (target >= nums[left] && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                if (target > nums[mid] && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        return -1;
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
var search = function(nums, target) {
    let left = 0;
    let right = nums.length - 1;

    while (left <= right) {
        let mid = Math.floor(left + (right - left) / 2);
        if (nums[mid] === target) {
            return mid;
        }

        if (nums[left] <= nums[mid]) {
            if (target >= nums[left] && target < nums[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        } else {
            if (target > nums[mid] && target <= nums[right]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    }

    return -1;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function search(nums: number[], target: number): number {
    let left: number = 0;
    let right: number = nums.length - 1;

    while (left <= right) {
        let mid: number = Math.floor(left + (right - left) / 2);
        if (nums[mid] === target) {
            return mid;
        }

        if (nums[left] <= nums[mid]) {
            if (target >= nums[left] && target < nums[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        } else {
            if (target > nums[mid] && target <= nums[right]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    }

    return -1;
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
    function search($nums, $target) {
        $left = 0;
        $right = count($nums) - 1;

        while ($left <= $right) {
            $mid = $left + floor(($right - $left) / 2);
            if ($nums[$mid] == $target) {
                return $mid;
            }

            if ($nums[$left] <= $nums[$mid]) {
                if ($target >= $nums[$left] && $target < $nums[$mid]) {
                    $right = $mid - 1;
                } else {
                    $left = $mid + 1;
                }
            } else {
                if ($target > $nums[$mid] && $target <= $nums[$right]) {
                    $left = $mid + 1;
                } else {
                    $right = $mid - 1;
                }
            }
        }

        return -1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func search(_ nums: [Int], _ target: Int) -> Int {
        var left = 0
        var right = nums.count - 1

        while left <= right {
            let mid = left + (right - left) / 2
            if nums[mid] == target {
                return mid
            }

            if nums[left] <= nums[mid] {
                if target >= nums[left] && target < nums[mid] {
                    right = mid - 1
                } else {
                    left = mid + 1
                }
            } else {
                if target > nums[mid] && target <= nums[right] {
                    left = mid + 1
                } else {
                    right = mid - 1
                }
            }
        }

        return -1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun search(nums: IntArray, target: Int): Int {
        var left = 0
        var right = nums.size - 1

        while (left <= right) {
            val mid = left + (right - left) / 2
            if (nums[mid] == target) return mid

            if (nums[left] <= nums[mid]) {
                if (target >= nums[left] && target < nums[mid]) {
                    right = mid - 1
                } else {
                    left = mid + 1
                }
            } else {
                if (target > nums[mid] && target <= nums[right]) {
                    left = mid + 1
                } else {
                    right = mid - 1
                }
            }
        }

        return -1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int search(List<int> nums, int target) {
    int left = 0;
    int right = nums.length - 1;

    while (left <= right) {
      int mid = left + (right - left) ~/ 2;
      if (nums[mid] == target) return mid;

      if (nums[left] <= nums[mid]) {
        if (target >= nums[left] && target < nums[mid]) {
          right = mid - 1;
        } else {
          left = mid + 1;
        }
      } else {
        if (target > nums[mid] && target <= nums[right]) {
          left = mid + 1;
        } else {
          right = mid - 1;
        }
      }
    }

    return -1;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func search(nums []int, target int) int {
    left := 0
    right := len(nums) - 1

    for left <= right {
        mid := left + (right-left)/2
        if nums[mid] == target {
            return mid
        }

        if nums[left] <= nums[mid] {
            if target >= nums[left] && target < nums[mid] {
                right = mid - 1
            } else {
                left = mid + 1
            }
        } else {
            if target > nums[mid] && target <= nums[right] {
                left = mid + 1
            } else {
                right = mid - 1
            }
        }
    }

    return -1
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
def search(nums, target)
    left = 0
    right = nums.length - 1

    while left <= right
        mid = left + (right - left) / 2
        return mid if nums[mid] == target

        if nums[left] <= nums[mid]
            if target >= nums[left] && target < nums[mid]
                right = mid - 1
            else
                left = mid + 1
            end
        else
            if target > nums[mid] && target <= nums[right]
                left = mid + 1
            else
                right = mid - 1
            end
        end
    end

    -1
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def search(nums: Array[Int], target: Int): Int = {
        var left = 0
        var right = nums.length - 1

        while (left <= right) {
            val mid = left + (right - left) / 2
            if (nums(mid) == target) return mid

            if (nums(left) <= nums(mid)) {
                if (target >= nums(left) && target < nums(mid)) {
                    right = mid - 1
                } else {
                    left = mid + 1
                }
            } else {
                if (target > nums(mid) && target <= nums(right)) {
                    left = mid + 1
                } else {
                    right = mid - 1
                }
            }
        }

        -1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut low: i32 = 0;
        let mut high: i32 = nums.len() as i32 - 1;

        while low <= high {
            let mid = low + (high - low) / 2;
            let mid_val = nums[mid as usize];

            if mid_val == target {
                return mid;
            }

            let low_val = nums[low as usize];
            let high_val = nums[high as usize];

            if low_val <= mid_val {
                if target >= low_val && target < mid_val {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            } else {
                if target > mid_val && target <= high_val {
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
        }

        -1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (search nums target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let ([vec (list->vector nums)])
    (let loop ([low 0]
               [high (- (vector-length vec) 1)])
      (if (> low high)
          -1
          (let* ([mid (quotient (+ low high) 2)]
                 [mid-val (vector-ref vec mid)]
                 [low-val (vector-ref vec low)]
                 [high-val (vector-ref vec high)])
            (cond
              [(= mid-val target) mid]
              [(<= low-val mid-val)
               (if (and (>= target low-val) (< target mid-val))
                   (loop low (- mid 1))
                   (loop (+ mid 1) high))]
              [else
               (if (and (> target mid-val) (<= target high-val))
                   (loop (+ mid 1) high)
                   (loop low (- mid 1)))]))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec search(Nums :: [integer()], Target :: integer()) -> integer().
search(Nums, Target) ->
  Arr = list_to_tuple(Nums),
  binary_search(Arr, Target, 1, tuple_size(Arr)).

binary_search(_Arr, _Target, Low, High) when Low > High ->
  -1;
binary_search(Arr, Target, Low, High) ->
  Mid = (Low + High) div 2,
  MidVal = element(Mid, Arr),
  LowVal = element(Low, Arr),
  HighVal = element(High, Arr),
  if
    MidVal == Target ->
      Mid - 1;
    LowVal =< MidVal ->
      if
        Target >= LowVal andalso Target < MidVal ->
          binary_search(Arr, Target, Low, Mid - 1);
        true ->
          binary_search(Arr, Target, Mid + 1, High)
      end;
    true ->
      if
        Target > MidVal andalso Target =< HighVal ->
          binary_search(Arr, Target, Mid + 1, High);
        true ->
          binary_search(Arr, Target, Low, Mid - 1)
      end
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec search(nums :: [integer], target :: integer) :: integer
  def search(nums, target) do
    nums_tuple = List.to_tuple(nums)
    search_recursive(nums_tuple, target, 0, tuple_size(nums_tuple) - 1)
  end

  defp search_recursive(_nums_tuple, _target, low, high) when low > high do
    -1
  end

  defp search_recursive(nums_tuple, target, low, high) do
    mid = div(low + high, 2)
    mid_val = elem(nums_tuple, mid)
    low_val = elem(nums_tuple, low)
    high_val = elem(nums_tuple, high)

    cond do
      mid_val == target ->
        mid
      low_val <= mid_val ->
        if target >= low_val and target < mid_val do
          search_recursive(nums_tuple, target, low, mid - 1)
        else
          search_recursive(nums_tuple, target, mid + 1, high)
        end
      true ->
        if target > mid_val and target <= high_val do
          search_recursive(nums_tuple, target, mid + 1, high)
        else
          search_recursive(nums_tuple, target, low, mid - 1)
        end
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(log n) because the search space is reduced by half in each iteration of the binary search, resulting in a logarithmic number of steps relative to the size of the input array.
- **Space Complexity:** O(1) as the algorithm only requires a constant amount of extra space for the left, right, and middle pointers, regardless of the input size.
