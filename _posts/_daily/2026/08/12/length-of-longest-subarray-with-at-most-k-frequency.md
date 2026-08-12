---
layout: post
title: "Length of Longest Subarray With at Most K Frequency"
date: 2026-08-12 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Sliding Window"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <unordered_map>\n#include <algorithm>\n\nusing\
        \ namespace std;\n\nclass Solution {\npublic:\n    int maxSubarrayLength(vector<int>&\
        \ nums, int k) {\n        unordered_map<int, int> counts;\n        int left\
        \ = 0;\n        int maxLen = 0;\n        int n = nums.size();\n\n        for\
        \ (int right = 0; right < n; ++right) {\n            int currentVal = nums[right];\n\
        \            counts[currentVal]++;\n\n            while (counts[currentVal]\
        \ > k) {\n                counts[nums[left]]--;\n                left++;\n \
        \           }\n\n            maxLen = max(maxLen, right - left + 1);\n     \
        \   }\n\n        return maxLen;\n    }\n};"
      java: "import java.util.HashMap;\nimport java.util.Map;\n\nclass Solution {\n\
        \    public int maxSubarrayLength(int[] nums, int k) {\n        Map<Integer,\
        \ Integer> counts = new HashMap<>();\n        int left = 0;\n        int maxLen\
        \ = 0;\n\n        for (int right = 0; right < nums.length; right++) {\n    \
        \        int num = nums[right];\n            counts.put(num, counts.getOrDefault(num,\
        \ 0) + 1);\n\n            while (counts.get(num) > k) {\n                counts.put(nums[left],\
        \ counts.get(nums[left]) - 1);\n                left++;\n            }\n\n \
        \           maxLen = Math.max(maxLen, right - left + 1);\n        }\n\n    \
        \    return maxLen;\n    }\n}"
      python: "class Solution(object):\n    def maxSubarrayLength(self, nums, k):\n\
        \        \"\"\"\n        :type nums: List[int]\n        :type k: int\n     \
        \   :rtype: int\n        \"\"\"\n        counts = {}\n        left = 0\n   \
        \     max_len = 0\n\n        for right in range(len(nums)):\n            val\
        \ = nums[right]\n            counts[val] = counts.get(val, 0) + 1\n\n      \
        \      while counts[val] > k:\n                counts[nums[left]] -= 1\n   \
        \             left += 1\n\n            current_len = right - left + 1\n    \
        \        if current_len > max_len:\n                max_len = current_len\n\n\
        \        return max_len"
      python3: "from typing import List\nfrom collections import defaultdict\n\nclass\
        \ Solution:\n    def maxSubarrayLength(self, nums: List[int], k: int) -> int:\n\
        \        counts = defaultdict(int)\n        left = 0\n        max_len = 0\n\n\
        \        for right in range(len(nums)):\n            val = nums[right]\n   \
        \         counts[val] += 1\n\n            while counts[val] > k:\n         \
        \       counts[nums[left]] -= 1\n                left += 1\n\n            max_len\
        \ = max(max_len, right - left + 1)\n\n        return max_len"
      c: "#include <stdlib.h>\n\ntypedef struct {\n    int key;\n    int count;\n} HashEntry;\n\
        \nint maxSubarrayLength(int* nums, int numsSize, int k) {\n    int mapSize =\
        \ numsSize * 2 + 1;\n    HashEntry* table = (HashEntry*)calloc(mapSize, sizeof(HashEntry));\n\
        \    int left = 0;\n    int maxLen = 0;\n\n    for (int right = 0; right < numsSize;\
        \ right++) {\n        int val = nums[right];\n        unsigned int h = (unsigned\
        \ int)val % mapSize;\n\n        while (table[h].key != 0 && table[h].key !=\
        \ val) {\n            h = (h + 1) % mapSize;\n        }\n\n        if (table[h].key\
        \ == 0) {\n            table[h].key = val;\n        }\n        table[h].count++;\n\
        \n        while (table[h].count > k) {\n            int leftVal = nums[left];\n\
        \            unsigned int hL = (unsigned int)leftVal % mapSize;\n          \
        \  while (table[hL].key != leftVal) {\n                hL = (hL + 1) % mapSize;\n\
        \            }\n            table[hL].count--;\n            left++;\n      \
        \  }\n\n        int currentLen = right - left + 1;\n        if (currentLen >\
        \ maxLen) {\n            maxLen = currentLen;\n        }\n    }\n\n    free(table);\n\
        \    return maxLen;\n}"
      csharp: "public class Solution {\n    public int MaxSubarrayLength(int[] nums,\
        \ int k) {\n        int n = nums.Length;\n        int left = 0;\n        int\
        \ maxLen = 0;\n        Dictionary<int, int> counts = new Dictionary<int, int>();\n\
        \        for (int right = 0; right < n; right++) {\n            int val = nums[right];\n\
        \            if (counts.ContainsKey(val)) {\n                counts[val]++;\n\
        \            } else {\n                counts[val] = 1;\n            }\n   \
        \         while (counts[val] > k) {\n                counts[nums[left]]--;\n\
        \                left++;\n            }\n            maxLen = Math.Max(maxLen,\
        \ right - left + 1);\n        }\n        return maxLen;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} k\n * @return\
        \ {number}\n */\nvar maxSubarrayLength = function(nums, k) {\n    let n = nums.length;\n\
        \    let left = 0;\n    let maxLen = 0;\n    const counts = new Map();\n   \
        \ for (let right = 0; right < n; right++) {\n        let val = nums[right];\n\
        \        counts.set(val, (counts.get(val) || 0) + 1);\n        while (counts.get(val)\
        \ > k) {\n            counts.set(nums[left], counts.get(nums[left]) - 1);\n\
        \            left++;\n        }\n        maxLen = Math.max(maxLen, right - left\
        \ + 1);\n    }\n    return maxLen;\n};"
      typescript: "function maxSubarrayLength(nums: number[], k: number): number {\n\
        \    let n = nums.length;\n    let left = 0;\n    let maxLen = 0;\n    const\
        \ counts = new Map<number, number>();\n    for (let right = 0; right < n; right++)\
        \ {\n        let val = nums[right];\n        counts.set(val, (counts.get(val)\
        \ || 0) + 1);\n        while (counts.get(val)! > k) {\n            counts.set(nums[left],\
        \ counts.get(nums[left])! - 1);\n            left++;\n        }\n        maxLen\
        \ = Math.max(maxLen, right - left + 1);\n    }\n    return maxLen;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer $k\n     * @return Integer\n     */\n    function maxSubarrayLength($nums,\
        \ $k) {\n        $n = count($nums);\n        $left = 0;\n        $maxLen = 0;\n\
        \        $counts = [];\n        for ($right = 0; $right < $n; $right++) {\n\
        \            $val = $nums[$right];\n            if (!isset($counts[$val])) {\n\
        \                $counts[$val] = 0;\n            }\n            $counts[$val]++;\n\
        \            while ($counts[$val] > $k) {\n                $counts[$nums[$left]]--;\n\
        \                $left++;\n            }\n            $maxLen = max($maxLen,\
        \ $right - $left + 1);\n        }\n        return $maxLen;\n    }\n}"
      swift: "class Solution {\n    func maxSubarrayLength(_ nums: [Int], _ k: Int)\
        \ -> Int {\n        let n = nums.count\n        var left = 0\n        var maxLen\
        \ = 0\n        var counts = [Int: Int]()\n        for right in 0..<n {\n   \
        \         let val = nums[right]\n            counts[val, default: 0] += 1\n\
        \            while counts[val]! > k {\n                counts[nums[left]]! -=\
        \ 1\n                left += 1\n            }\n            maxLen = max(maxLen,\
        \ right - left + 1)\n        }\n        return maxLen\n    }\n}"
      kotlin: "class Solution {\n    fun maxSubarrayLength(nums: IntArray, k: Int):\
        \ Int {\n        val counts = mutableMapOf<Int, Int>()\n        var left = 0\n\
        \        var maxLen = 0\n        for (right in nums.indices) {\n           \
        \ val num = nums[right]\n            counts[num] = (counts[num] ?: 0) + 1\n\
        \            while (counts[num]!! > k) {\n                val leftNum = nums[left]\n\
        \                counts[leftNum] = counts[leftNum]!! - 1\n                left++\n\
        \            }\n            val currentLen = right - left + 1\n            if\
        \ (currentLen > maxLen) {\n                maxLen = currentLen\n           \
        \ }\n        }\n        return maxLen\n    }\n}"
      dart: "class Solution {\n  int maxSubarrayLength(List<int> nums, int k) {\n  \
        \  Map<int, int> counts = {};\n    int left = 0;\n    int maxLen = 0;\n    for\
        \ (int right = 0; right < nums.length; right++) {\n      int num = nums[right];\n\
        \      counts[num] = (counts[num] ?? 0) + 1;\n      while (counts[num]! > k)\
        \ {\n        int leftNum = nums[left];\n        counts[leftNum] = counts[leftNum]!\
        \ - 1;\n        left++;\n      }\n      int currentLen = right - left + 1;\n\
        \      if (currentLen > maxLen) {\n        maxLen = currentLen;\n      }\n \
        \   }\n    return maxLen;\n  }\n}"
      go: "func maxSubarrayLength(nums []int, k int) int {\n    counts := make(map[int]int)\n\
        \    left := 0\n    maxLen := 0\n    for right, num := range nums {\n      \
        \  counts[num]++\n        for counts[num] > k {\n            counts[nums[left]]--\n\
        \            left++\n        }\n        currentLen := right - left + 1\n   \
        \     if currentLen > maxLen {\n            maxLen = currentLen\n        }\n\
        \    }\n    return maxLen\n}"
      ruby: "# @param {Integer[]} nums\n# @param {Integer} k\n# @return {Integer}\n\
        def max_subarray_length(nums, k)\n  counts = Hash.new(0)\n  left = 0\n  max_len\
        \ = 0\n  nums.each_with_index do |num, right|\n    counts[num] += 1\n    while\
        \ counts[num] > k\n      counts[nums[left]] -= 1\n      left += 1\n    end\n\
        \    current_len = right - left + 1\n    max_len = current_len if current_len\
        \ > max_len\n  end\n  max_len\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n    def maxSubarrayLength(nums:\
        \ Array[Int], k: Int): Int = {\n        val counts = mutable.Map[Int, Int]()\n\
        \        var left = 0\n        var maxLen = 0\n        for (right <- nums.indices)\
        \ {\n            val num = nums(right)\n            counts(num) = counts.getOrElse(num,\
        \ 0) + 1\n            while (counts(num) > k) {\n                val leftNum\
        \ = nums(left)\n                counts(leftNum) = counts(leftNum) - 1\n    \
        \            left += 1\n            }\n            val currentLen = right -\
        \ left + 1\n            if (currentLen > maxLen) {\n                maxLen =\
        \ currentLen\n            }\n        }\n        maxLen\n    }\n}"
      rust: "use std::collections::HashMap;\n\nimpl Solution {\n    pub fn max_subarray_length(nums:\
        \ Vec<i32>, k: i32) -> i32 {\n        let mut counts = HashMap::new();\n   \
        \     let mut max_len = 0;\n        let mut left = 0;\n        let n = nums.len();\n\
        \        for right in 0..n {\n            let val_right = nums[right];\n   \
        \         let count = counts.entry(val_right).or_insert(0);\n            *count\
        \ += 1;\n\n            while *counts.get(&val_right).unwrap() > k {\n      \
        \          let val_left = nums[left];\n                if let Some(c) = counts.get_mut(&val_left)\
        \ {\n                    *c -= 1;\n                }\n                left +=\
        \ 1;\n            }\n\n            let curr_len = right - left + 1;\n      \
        \      if curr_len > max_len {\n                max_len = curr_len;\n      \
        \      }\n        }\n        max_len as i32\n    }\n}"
      racket: "(define/contract (max-subarray-length nums k)\n  (-> (listof exact-integer?)\
        \ exact-integer? exact-integer?)\n  (let* ([nums-vec (list->vector nums)]\n\
        \         [n (vector-length nums-vec)]\n         [counts (make-hash)])\n   \
        \ (let loop ([left 0] [right 0] [max-len 0])\n      (if (< right n)\n      \
        \    (let* ([val-right (vector-ref nums-vec right)]\n                 [count-right\
        \ (+ (hash-ref counts val-right 0) 1)])\n            (hash-set! counts val-right\
        \ count-right)\n            (let shrink ([l left])\n              (if (> (hash-ref\
        \ counts val-right) k)\n                  (let* ([val-left (vector-ref nums-vec\
        \ l)])\n                    (hash-set! counts val-left (- (hash-ref counts val-left)\
        \ 1))\n                    (shrink (+ l 1)))\n                  (loop l (+ right\
        \ 1) (max max-len (+ (- right l) 1))))))\n          max-len))))"
      erlang: "-spec max_subarray_length(Nums :: [integer()], K :: integer()) -> integer().\n\
        max_subarray_length(Nums, K) ->\n  NumsTuple = list_to_tuple(Nums),\n  N = tuple_size(NumsTuple),\n\
        \  max_loop(1, 1, 0, #{}, N, NumsTuple, K).\n\nmax_loop(Right, Left, MaxLen,\
        \ Counts, N, NumsTuple, K) when Right =< N ->\n  ValRight = element(Right, NumsTuple),\n\
        \  NewCounts = maps:put(ValRight, maps:get(ValRight, Counts, 0) + 1, Counts),\n\
        \  {NewLeft, FinalCounts} = max_shrink(Left, ValRight, NewCounts, NumsTuple,\
        \ K),\n  CurrentLen = Right - NewLeft + 1,\n  NewMaxLen = if CurrentLen > MaxLen\
        \ -> CurrentLen; true -> MaxLen end,\n  max_loop(Right + 1, NewLeft, NewMaxLen,\
        \ FinalCounts, N, NumsTuple, K);\nmax_loop(_Right, _Left, MaxLen, _Counts, _N,\
        \ _NumsTuple, _K) ->\n  MaxLen.\n\nmax_shrink(Left, ValRight, Counts, NumsTuple,\
        \ K) ->\n  case maps:get(ValRight, Counts) > K of\n    true ->\n      ValLeft\
        \ = element(Left, NumsTuple),\n      UpdatedCounts = maps:put(ValLeft, maps:get(ValLeft,\
        \ Counts) - 1, Counts),\n      max_shrink(Left + 1, ValRight, UpdatedCounts,\
        \ NumsTuple, K);\n    false ->\n      {Left, Counts}\n  end."
      elixir: "defmodule Solution do\n  @spec max_subarray_length(nums :: [integer],\
        \ k :: integer) :: integer\n  def max_subarray_length(nums, k) do\n    nums_vec\
        \ = List.to_tuple(nums)\n    n = tuple_size(nums_vec)\n    solve(0, 0, 0, %{},\
        \ n, nums_vec, k)\n  end\n\n  defp solve(right, left, max_len, counts, n, nums_vec,\
        \ k) when right < n do\n    val_right = elem(nums_vec, right)\n    count_right\
        \ = Map.get(counts, val_right, 0) + 1\n    new_counts = Map.put(counts, val_right,\
        \ count_right)\n\n    {new_left, final_counts} = shrink(left, val_right, new_counts,\
        \ nums_vec, k)\n\n    new_max_len = max(max_len, right - new_left + 1)\n   \
        \ solve(right + 1, new_left, new_max_len, final_counts, n, nums_vec, k)\n  end\n\
        \n  defp solve(_right, _left, max_len, _counts, _n, _nums_vec, _k) do\n    max_len\n\
        \  end\n\n  defp shrink(left, val_right, counts, nums_vec, k) do\n    if Map.get(counts,\
        \ val_right, 0) > k do\n      val_left = elem(nums_vec, left)\n      new_counts\
        \ = Map.put(counts, val_left, Map.get(counts, val_left, 0) - 1)\n      shrink(left\
        \ + 1, val_right, new_counts, nums_vec, k)\n    else\n      {left, counts}\n\
        \    end\n  end\nend"
    approach: 'The algorithm employs a sliding window strategy with two pointers, `left`
      and `right`, to efficiently find the longest subarray where each element''s frequency
      is at most `k`. A hash-based frequency map is maintained to track the occurrences
      of each number within the current sliding window. As the `right` pointer iterates
      through the array, it includes the current element in the window and updates its
      frequency count in the map.


      If adding an element causes its frequency to exceed the limit `k`, the `left`
      pointer is incremented to shrink the window from the left side. This process involves
      decrementing the frequency of the elements being removed until the frequency of
      the element at the `right` pointer is restored to `k` or less. Throughout the
      iteration, the maximum window size ($right - left + 1$) is recorded, which represents
      the length of the longest ''good'' subarray found so far.'
    time_complexity: O(N), where N is the length of the input array. Each element is
      added to the window by the right pointer once and removed by the left pointer
      at most once. Hash map operations (insertion, lookup, and deletion) take O(1)
      time on average.
    space_complexity: O(N), as the hash map can store the frequencies of up to N unique
      elements in the worst-case scenario where every element in the array is distinct.
    elapsed_time: 155.0478618144989
    model: gemini-3-flash-preview
    generated_at: '2026-08-12 01:17:23 '
---

## Problem #2958: Length of Longest Subarray With at Most K Frequency

**Difficulty:** Medium

**Topics:** Array, Hash Table, Sliding Window

## Problem Description

<p>You are given an integer array <code>nums</code> and an integer <code>k</code>.</p>

<p>The <strong>frequency</strong> of an element <code>x</code> is the number of times it occurs in an array.</p>

<p>An array is called <strong>good</strong> if the frequency of each element in this array is <strong>less than or equal</strong> to <code>k</code>.</p>

<p>Return <em>the length of the <strong>longest</strong> <strong>good</strong> subarray of</em> <code>nums</code><em>.</em></p>

<p>A <strong>subarray</strong> is a contiguous non-empty sequence of elements within an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1,2,3,1,2], k = 2
<strong>Output:</strong> 6
<strong>Explanation:</strong> The longest possible good subarray is [1,2,3,1,2,3] since the values 1, 2, and 3 occur at most twice in this subarray. Note that the subarrays [2,3,1,2,3,1] and [3,1,2,3,1,2] are also good.
It can be shown that there are no good subarrays with length more than 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,1,2,1,2,1,2], k = 1
<strong>Output:</strong> 2
<strong>Explanation:</strong> The longest possible good subarray is [1,2] since the values 1 and 2 occur at most once in this subarray. Note that the subarray [2,1] is also good.
It can be shown that there are no good subarrays with length more than 2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,5,5,5,5,5,5], k = 4
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest possible good subarray is [5,5,5,5] since the value 5 occurs 4 times in this subarray.
It can be shown that there are no good subarrays with length more than 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= nums.length</code></li>
</ul>


## Hints

1. For each index `i`, find the rightmost index `j >= i` such that the frequency of each element in the subarray `[i, j]` is at most `k`.

2. We can use 2 pointers / sliding window to achieve it.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm employs a sliding window strategy with two pointers, `left` and `right`, to efficiently find the longest subarray where each element's frequency is at most `k`. A hash-based frequency map is maintained to track the occurrences of each number within the current sliding window. As the `right` pointer iterates through the array, it includes the current element in the window and updates its frequency count in the map.

If adding an element causes its frequency to exceed the limit `k`, the `left` pointer is incremented to shrink the window from the left side. This process involves decrementing the frequency of the elements being removed until the frequency of the element at the `right` pointer is restored to `k` or less. Throughout the iteration, the maximum window size ($right - left + 1$) is recorded, which represents the length of the longest 'good' subarray found so far.

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
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        unordered_map<int, int> counts;
        int left = 0;
        int maxLen = 0;
        int n = nums.size();

        for (int right = 0; right < n; ++right) {
            int currentVal = nums[right];
            counts[currentVal]++;

            while (counts[currentVal] > k) {
                counts[nums[left]]--;
                left++;
            }

            maxLen = max(maxLen, right - left + 1);
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
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int maxSubarrayLength(int[] nums, int k) {
        Map<Integer, Integer> counts = new HashMap<>();
        int left = 0;
        int maxLen = 0;

        for (int right = 0; right < nums.length; right++) {
            int num = nums[right];
            counts.put(num, counts.getOrDefault(num, 0) + 1);

            while (counts.get(num) > k) {
                counts.put(nums[left], counts.get(nums[left]) - 1);
                left++;
            }

            maxLen = Math.max(maxLen, right - left + 1);
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
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counts = {}
        left = 0
        max_len = 0

        for right in range(len(nums)):
            val = nums[right]
            counts[val] = counts.get(val, 0) + 1

            while counts[val] > k:
                counts[nums[left]] -= 1
                left += 1

            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len

        return max_len
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from typing import List
from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        left = 0
        max_len = 0

        for right in range(len(nums)):
            val = nums[right]
            counts[val] += 1

            while counts[val] > k:
                counts[nums[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

typedef struct {
    int key;
    int count;
} HashEntry;

int maxSubarrayLength(int* nums, int numsSize, int k) {
    int mapSize = numsSize * 2 + 1;
    HashEntry* table = (HashEntry*)calloc(mapSize, sizeof(HashEntry));
    int left = 0;
    int maxLen = 0;

    for (int right = 0; right < numsSize; right++) {
        int val = nums[right];
        unsigned int h = (unsigned int)val % mapSize;

        while (table[h].key != 0 && table[h].key != val) {
            h = (h + 1) % mapSize;
        }

        if (table[h].key == 0) {
            table[h].key = val;
        }
        table[h].count++;

        while (table[h].count > k) {
            int leftVal = nums[left];
            unsigned int hL = (unsigned int)leftVal % mapSize;
            while (table[hL].key != leftVal) {
                hL = (hL + 1) % mapSize;
            }
            table[hL].count--;
            left++;
        }

        int currentLen = right - left + 1;
        if (currentLen > maxLen) {
            maxLen = currentLen;
        }
    }

    free(table);
    return maxLen;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaxSubarrayLength(int[] nums, int k) {
        int n = nums.Length;
        int left = 0;
        int maxLen = 0;
        Dictionary<int, int> counts = new Dictionary<int, int>();
        for (int right = 0; right < n; right++) {
            int val = nums[right];
            if (counts.ContainsKey(val)) {
                counts[val]++;
            } else {
                counts[val] = 1;
            }
            while (counts[val] > k) {
                counts[nums[left]]--;
                left++;
            }
            maxLen = Math.Max(maxLen, right - left + 1);
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
 * @param {number} k
 * @return {number}
 */
var maxSubarrayLength = function(nums, k) {
    let n = nums.length;
    let left = 0;
    let maxLen = 0;
    const counts = new Map();
    for (let right = 0; right < n; right++) {
        let val = nums[right];
        counts.set(val, (counts.get(val) || 0) + 1);
        while (counts.get(val) > k) {
            counts.set(nums[left], counts.get(nums[left]) - 1);
            left++;
        }
        maxLen = Math.max(maxLen, right - left + 1);
    }
    return maxLen;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxSubarrayLength(nums: number[], k: number): number {
    let n = nums.length;
    let left = 0;
    let maxLen = 0;
    const counts = new Map<number, number>();
    for (let right = 0; right < n; right++) {
        let val = nums[right];
        counts.set(val, (counts.get(val) || 0) + 1);
        while (counts.get(val)! > k) {
            counts.set(nums[left], counts.get(nums[left])! - 1);
            left++;
        }
        maxLen = Math.max(maxLen, right - left + 1);
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
     * @param Integer $k
     * @return Integer
     */
    function maxSubarrayLength($nums, $k) {
        $n = count($nums);
        $left = 0;
        $maxLen = 0;
        $counts = [];
        for ($right = 0; $right < $n; $right++) {
            $val = $nums[$right];
            if (!isset($counts[$val])) {
                $counts[$val] = 0;
            }
            $counts[$val]++;
            while ($counts[$val] > $k) {
                $counts[$nums[$left]]--;
                $left++;
            }
            $maxLen = max($maxLen, $right - $left + 1);
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
    func maxSubarrayLength(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var left = 0
        var maxLen = 0
        var counts = [Int: Int]()
        for right in 0..<n {
            let val = nums[right]
            counts[val, default: 0] += 1
            while counts[val]! > k {
                counts[nums[left]]! -= 1
                left += 1
            }
            maxLen = max(maxLen, right - left + 1)
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
    fun maxSubarrayLength(nums: IntArray, k: Int): Int {
        val counts = mutableMapOf<Int, Int>()
        var left = 0
        var maxLen = 0
        for (right in nums.indices) {
            val num = nums[right]
            counts[num] = (counts[num] ?: 0) + 1
            while (counts[num]!! > k) {
                val leftNum = nums[left]
                counts[leftNum] = counts[leftNum]!! - 1
                left++
            }
            val currentLen = right - left + 1
            if (currentLen > maxLen) {
                maxLen = currentLen
            }
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
  int maxSubarrayLength(List<int> nums, int k) {
    Map<int, int> counts = {};
    int left = 0;
    int maxLen = 0;
    for (int right = 0; right < nums.length; right++) {
      int num = nums[right];
      counts[num] = (counts[num] ?? 0) + 1;
      while (counts[num]! > k) {
        int leftNum = nums[left];
        counts[leftNum] = counts[leftNum]! - 1;
        left++;
      }
      int currentLen = right - left + 1;
      if (currentLen > maxLen) {
        maxLen = currentLen;
      }
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
func maxSubarrayLength(nums []int, k int) int {
    counts := make(map[int]int)
    left := 0
    maxLen := 0
    for right, num := range nums {
        counts[num]++
        for counts[num] > k {
            counts[nums[left]]--
            left++
        }
        currentLen := right - left + 1
        if currentLen > maxLen {
            maxLen = currentLen
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
# @param {Integer} k
# @return {Integer}
def max_subarray_length(nums, k)
  counts = Hash.new(0)
  left = 0
  max_len = 0
  nums.each_with_index do |num, right|
    counts[num] += 1
    while counts[num] > k
      counts[nums[left]] -= 1
      left += 1
    end
    current_len = right - left + 1
    max_len = current_len if current_len > max_len
  end
  max_len
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

object Solution {
    def maxSubarrayLength(nums: Array[Int], k: Int): Int = {
        val counts = mutable.Map[Int, Int]()
        var left = 0
        var maxLen = 0
        for (right <- nums.indices) {
            val num = nums(right)
            counts(num) = counts.getOrElse(num, 0) + 1
            while (counts(num) > k) {
                val leftNum = nums(left)
                counts(leftNum) = counts(leftNum) - 1
                left += 1
            }
            val currentLen = right - left + 1
            if (currentLen > maxLen) {
                maxLen = currentLen
            }
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
use std::collections::HashMap;

impl Solution {
    pub fn max_subarray_length(nums: Vec<i32>, k: i32) -> i32 {
        let mut counts = HashMap::new();
        let mut max_len = 0;
        let mut left = 0;
        let n = nums.len();
        for right in 0..n {
            let val_right = nums[right];
            let count = counts.entry(val_right).or_insert(0);
            *count += 1;

            while *counts.get(&val_right).unwrap() > k {
                let val_left = nums[left];
                if let Some(c) = counts.get_mut(&val_left) {
                    *c -= 1;
                }
                left += 1;
            }

            let curr_len = right - left + 1;
            if curr_len > max_len {
                max_len = curr_len;
            }
        }
        max_len as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (max-subarray-length nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([nums-vec (list->vector nums)]
         [n (vector-length nums-vec)]
         [counts (make-hash)])
    (let loop ([left 0] [right 0] [max-len 0])
      (if (< right n)
          (let* ([val-right (vector-ref nums-vec right)]
                 [count-right (+ (hash-ref counts val-right 0) 1)])
            (hash-set! counts val-right count-right)
            (let shrink ([l left])
              (if (> (hash-ref counts val-right) k)
                  (let* ([val-left (vector-ref nums-vec l)])
                    (hash-set! counts val-left (- (hash-ref counts val-left) 1))
                    (shrink (+ l 1)))
                  (loop l (+ right 1) (max max-len (+ (- right l) 1))))))
          max-len))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_subarray_length(Nums :: [integer()], K :: integer()) -> integer().
max_subarray_length(Nums, K) ->
  NumsTuple = list_to_tuple(Nums),
  N = tuple_size(NumsTuple),
  max_loop(1, 1, 0, #{}, N, NumsTuple, K).

max_loop(Right, Left, MaxLen, Counts, N, NumsTuple, K) when Right =< N ->
  ValRight = element(Right, NumsTuple),
  NewCounts = maps:put(ValRight, maps:get(ValRight, Counts, 0) + 1, Counts),
  {NewLeft, FinalCounts} = max_shrink(Left, ValRight, NewCounts, NumsTuple, K),
  CurrentLen = Right - NewLeft + 1,
  NewMaxLen = if CurrentLen > MaxLen -> CurrentLen; true -> MaxLen end,
  max_loop(Right + 1, NewLeft, NewMaxLen, FinalCounts, N, NumsTuple, K);
max_loop(_Right, _Left, MaxLen, _Counts, _N, _NumsTuple, _K) ->
  MaxLen.

max_shrink(Left, ValRight, Counts, NumsTuple, K) ->
  case maps:get(ValRight, Counts) > K of
    true ->
      ValLeft = element(Left, NumsTuple),
      UpdatedCounts = maps:put(ValLeft, maps:get(ValLeft, Counts) - 1, Counts),
      max_shrink(Left + 1, ValRight, UpdatedCounts, NumsTuple, K);
    false ->
      {Left, Counts}
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_subarray_length(nums :: [integer], k :: integer) :: integer
  def max_subarray_length(nums, k) do
    nums_vec = List.to_tuple(nums)
    n = tuple_size(nums_vec)
    solve(0, 0, 0, %{}, n, nums_vec, k)
  end

  defp solve(right, left, max_len, counts, n, nums_vec, k) when right < n do
    val_right = elem(nums_vec, right)
    count_right = Map.get(counts, val_right, 0) + 1
    new_counts = Map.put(counts, val_right, count_right)

    {new_left, final_counts} = shrink(left, val_right, new_counts, nums_vec, k)

    new_max_len = max(max_len, right - new_left + 1)
    solve(right + 1, new_left, new_max_len, final_counts, n, nums_vec, k)
  end

  defp solve(_right, _left, max_len, _counts, _n, _nums_vec, _k) do
    max_len
  end

  defp shrink(left, val_right, counts, nums_vec, k) do
    if Map.get(counts, val_right, 0) > k do
      val_left = elem(nums_vec, left)
      new_counts = Map.put(counts, val_left, Map.get(counts, val_left, 0) - 1)
      shrink(left + 1, val_right, new_counts, nums_vec, k)
    else
      {left, counts}
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N), where N is the length of the input array. Each element is added to the window by the right pointer once and removed by the left pointer at most once. Hash map operations (insertion, lookup, and deletion) take O(1) time on average.
- **Space Complexity:** O(N), as the hash map can store the frequencies of up to N unique elements in the worst-case scenario where every element in the array is distinct.
