---
layout: post
title: "Subarrays Distinct Element Sum of Squares I"
date: 2026-10-15 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Hash Table", "Binary Indexed Tree", "Segment Tree"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int sumCounts(vector<int>& nums) {\n    \
        \    int totalSum = 0;\n        int n = nums.size();\n        for (int i = 0;\
        \ i < n; ++i) {\n            std::unordered_set<int> distinct;\n           \
        \ for (int j = i; j < n; ++j) {\n                distinct.insert(nums[j]);\n\
        \                int count = distinct.size();\n                totalSum += count\
        \ * count;\n            }\n        }\n        return totalSum;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public int sumCounts(List<Integer>\
        \ nums) {\n        int totalSum = 0;\n        int n = nums.size();\n       \
        \ for (int i = 0; i < n; i++) {\n            Set<Integer> distinct = new HashSet<>();\n\
        \            for (int j = i; j < n; j++) {\n                distinct.add(nums.get(j));\n\
        \                int count = distinct.size();\n                totalSum += count\
        \ * count;\n            }\n        }\n        return totalSum;\n    }\n}"
      python: "class Solution(object):\n    def sumCounts(self, nums):\n        \"\"\
        \"\n        :type nums: List[int]\n        :rtype: int\n        \"\"\"\n   \
        \     total_sum = 0\n        n = len(nums)\n        for i in range(n):\n   \
        \         distinct = set()\n            for j in range(i, n):\n            \
        \    distinct.add(nums[j])\n                count = len(distinct)\n        \
        \        total_sum += count * count\n        return total_sum"
      python3: "class Solution:\n    def sumCounts(self, nums: List[int]) -> int:\n\
        \        total_sum = 0\n        n = len(nums)\n        for i in range(n):\n\
        \            distinct = set()\n            for j in range(i, n):\n         \
        \       distinct.add(nums[j])\n                count = len(distinct)\n     \
        \           total_sum += count * count\n        return total_sum"
      c: "int sumCounts(int* nums, int numsSize) {\n    int totalSum = 0;\n    for (int\
        \ i = 0; i < numsSize; i++) {\n        int seen[101] = {0};\n        int distinctCount\
        \ = 0;\n        for (int j = i; j < numsSize; j++) {\n            if (seen[nums[j]]\
        \ == 0) {\n                seen[nums[j]] = 1;\n                distinctCount++;\n\
        \            }\n            totalSum += (distinctCount * distinctCount);\n \
        \       }\n    }\n    return totalSum;\n}"
      csharp: "using System.Collections.Generic;\n\npublic class Solution {\n    public\
        \ int SumCounts(IList<int> nums) {\n        int totalSum = 0;\n        int n\
        \ = nums.Count;\n        for (int i = 0; i < n; i++) {\n            HashSet<int>\
        \ distinct = new HashSet<int>();\n            for (int j = i; j < n; j++) {\n\
        \                distinct.Add(nums[j]);\n                int count = distinct.Count;\n\
        \                totalSum += count * count;\n            }\n        }\n    \
        \    return totalSum;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar sumCounts\
        \ = function(nums) {\n    let totalSum = 0;\n    let n = nums.length;\n    for\
        \ (let i = 0; i < n; i++) {\n        let distinct = new Set();\n        for\
        \ (let j = i; j < n; j++) {\n            distinct.add(nums[j]);\n          \
        \  let count = distinct.size;\n            totalSum += count * count;\n    \
        \    }\n    }\n    return totalSum;\n};"
      typescript: "function sumCounts(nums: number[]): number {\n    let totalSum =\
        \ 0;\n    const n = nums.length;\n    for (let i = 0; i < n; i++) {\n      \
        \  const distinctSet = new Set<number>();\n        for (let j = i; j < n; j++)\
        \ {\n            distinctSet.add(nums[j]);\n            const count = distinctSet.size;\n\
        \            totalSum += count * count;\n        }\n    }\n    return totalSum;\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function sumCounts($nums) {\n        $totalSum = 0;\n\
        \        $n = count($nums);\n        for ($i = 0; $i < $n; $i++) {\n       \
        \     $distinct = [];\n            for ($j = $i; $j < $n; $j++) {\n        \
        \        $distinct[$nums[$j]] = true;\n                $count = count($distinct);\n\
        \                $totalSum += $count * $count;\n            }\n        }\n \
        \       return $totalSum;\n    }\n}"
      swift: "class Solution {\n    func sumCounts(_ nums: [Int]) -> Int {\n       \
        \ var totalSum = 0\n        let n = nums.count\n        for i in 0..<n {\n \
        \           var distinctSet = Set<Int>()\n            for j in i..<n {\n   \
        \             distinctSet.insert(nums[j])\n                let count = distinctSet.count\n\
        \                totalSum += count * count\n            }\n        }\n     \
        \   return totalSum\n    }\n}"
      kotlin: "class Solution {\n    fun sumCounts(nums: List<Int>): Int {\n       \
        \ var totalSum = 0\n        val n = nums.size\n        for (i in 0 until n)\
        \ {\n            val distinctSet = mutableSetOf<Int>()\n            for (j in\
        \ i until n) {\n                distinctSet.add(nums[j])\n                val\
        \ count = distinctSet.size\n                totalSum += count * count\n    \
        \        }\n        }\n        return totalSum\n    }\n}"
      dart: "class Solution {\n  int sumCounts(List<int> nums) {\n    int totalSum =\
        \ 0;\n    int n = nums.length;\n    for (int i = 0; i < n; i++) {\n      Set<int>\
        \ distinctSet = {};\n      for (int j = i; j < n; j++) {\n        distinctSet.add(nums[j]);\n\
        \        int count = distinctSet.length;\n        totalSum += count * count;\n\
        \      }\n    }\n    return totalSum;\n  }\n}"
      go: "func sumCounts(nums []int) int {\n    totalSum := 0\n    n := len(nums)\n\
        \    for i := 0; i < n; i++ {\n        distinctMap := make(map[int]bool)\n \
        \       for j := i; j < n; j++ {\n            distinctMap[nums[j]] = true\n\
        \            count := len(distinctMap)\n            totalSum += count * count\n\
        \        }\n    }\n    return totalSum\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef sum_counts(nums)\n\
        \  total_sum = 0\n  n = nums.length\n  (0...n).each do |i|\n    distinct_elements\
        \ = {}\n    (i...n).each do |j|\n      distinct_elements[nums[j]] = true\n \
        \     count = distinct_elements.size\n      total_sum += count * count\n   \
        \ end\n  end\n  total_sum\nend"
      scala: "object Solution {\n    def sumCounts(nums: List[Int]): Int = {\n     \
        \   val n = nums.length\n        val numsArr = nums.toArray\n        var totalSum\
        \ = 0\n        for (i <- 0 until n) {\n            var distinctSet = Set[Int]()\n\
        \            for (j <- i until n) {\n                distinctSet += numsArr(j)\n\
        \                val count = distinctSet.size\n                totalSum += count\
        \ * count\n            }\n        }\n        totalSum\n    }\n}"
      rust: "use std::collections::HashSet;\n\nimpl Solution {\n    pub fn sum_counts(nums:\
        \ Vec<i32>) -> i32 {\n        let n = nums.len();\n        let mut total_sum\
        \ = 0;\n        for i in 0..n {\n            let mut set = HashSet::new();\n\
        \            for j in i..n {\n                set.insert(nums[j]);\n       \
        \         let count = set.len() as i32;\n                total_sum += count\
        \ * count;\n            }\n        }\n        total_sum\n    }\n}"
      racket: "(define/contract (sum-counts nums)\n  (-> (listof exact-integer?) exact-integer?)\n\
        \  (let* ([n (length nums)]\n         [nums-vec (list->vector nums)])\n    (for/sum\
        \ ([i (in-range n)])\n      (let loop ([j i] [current-set (set)] [inner-sum\
        \ 0])\n        (if (= j n)\n            inner-sum\n            (let* ([new-set\
        \ (set-add current-set (vector-ref nums-vec j))]\n                   [count\
        \ (set-count new-set)])\n              (loop (+ j 1) new-set (+ inner-sum (*\
        \ count count)))))))))"
      erlang: "-spec sum_counts(Nums :: [integer()]) -> integer().\nsum_counts(Nums)\
        \ ->\n  N = length(Nums),\n  NumsVec = list_to_tuple(Nums),\n  lists:foldl(fun(I,\
        \ AccI) ->\n    {_, SumJ} = lists:foldl(fun(J, {Set, AccJ}) ->\n      Val =\
        \ element(J, NumsVec),\n      NewSet = sets:add_element(Val, Set),\n      Count\
        \ = sets:size(NewSet),\n      {NewSet, AccJ + (Count * Count)}\n    end, {sets:new(),\
        \ 0}, lists:seq(I, N)),\n    AccI + SumJ\n  end, 0, lists:seq(1, N))."
      elixir: "defmodule Solution do\n  @spec sum_counts(nums :: [integer]) :: integer\n\
        \  def sum_counts(nums) do\n    n = length(nums)\n    nums_vec = List.to_tuple(nums)\n\
        \    Enum.reduce(0..(n - 1), 0, fn i, total_sum ->\n      {_, inner_sum} = Enum.reduce(i..(n\
        \ - 1), {MapSet.new(), 0}, fn j, {set, current_inner_sum} ->\n        new_set\
        \ = MapSet.put(set, elem(nums_vec, j))\n        count = MapSet.size(new_set)\n\
        \        {new_set, current_inner_sum + count * count}\n      end)\n      total_sum\
        \ + inner_sum\n    end)\n  end\nend"
    approach: 'To solve this problem, we iterate through every possible starting index
      $i$ and ending index $j$ of a subarray. For each starting index $i$, we initialize
      a set or frequency tracker to keep track of the unique elements encountered as
      we extend the subarray by incrementing the end index $j$. This allows us to update
      the count of distinct elements in $O(1)$ time for each extension, ensuring we
      calculate the distinct count for every subarray efficiently.


      The squared value of the distinct count for each subarray is calculated and added
      to a cumulative sum. Since the problem constraints are small ($N \le 100$), a
      brute-force approach that checks all $O(N^2)$ subarrays is both simple and performance-adequate.
      We use standard data structures like hash sets or simple boolean arrays to track
      the distinct values within the inner loop.'
    time_complexity: O(N^2) where N is the length of the input array. We use two nested
      loops to iterate through all possible subarrays, and the work done inside the
      inner loop (updating the distinct count and calculating the square) takes constant
      time on average when using a hash set or frequency array.
    space_complexity: O(N) in the worst case. This is required for the hash set or frequency
      array to store the unique elements of the current subarray being processed, which
      can contain up to N distinct elements.
    elapsed_time: 66.17463994026184
    model: gemini-3-flash-preview
    generated_at: '2026-10-15 02:37:10 '
---

## Problem #2913: Subarrays Distinct Element Sum of Squares I

**Difficulty:** Easy

**Topics:** Array, Hash Table, Binary Indexed Tree, Segment Tree

## Problem Description

<p>You are given a <strong>0-indexed </strong>integer array <code>nums</code>.</p>

<p>The <strong>distinct count</strong> of a subarray of <code>nums</code> is defined as:</p>

<ul>
	<li>Let <code>nums[i..j]</code> be a subarray of <code>nums</code> consisting of all the indices from <code>i</code> to <code>j</code> such that <code>0 &lt;= i &lt;= j &lt; nums.length</code>. Then the number of distinct values in <code>nums[i..j]</code> is called the distinct count of <code>nums[i..j]</code>.</li>
</ul>

<p>Return <em>the sum of the <strong>squares</strong> of <strong>distinct counts</strong> of all subarrays of </em><code>nums</code>.</p>

<p>A subarray is a contiguous <strong>non-empty</strong> sequence of elements within an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,1]
<strong>Output:</strong> 15
<strong>Explanation:</strong> Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 1<sup>2</sup> + 1<sup>2</sup> + 1<sup>2</sup> + 2<sup>2</sup> + 2<sup>2</sup> + 2<sup>2</sup> = 15.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Three possible subarrays are:
[1]: 1 distinct value
[1]: 1 distinct value
[1,1]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 1<sup>2</sup> + 1<sup>2</sup> + 1<sup>2</sup> = 3.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## Hints

1. Use a set/heap to keep track of distinct element counts.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To solve this problem, we iterate through every possible starting index $i$ and ending index $j$ of a subarray. For each starting index $i$, we initialize a set or frequency tracker to keep track of the unique elements encountered as we extend the subarray by incrementing the end index $j$. This allows us to update the count of distinct elements in $O(1)$ time for each extension, ensuring we calculate the distinct count for every subarray efficiently.

The squared value of the distinct count for each subarray is calculated and added to a cumulative sum. Since the problem constraints are small ($N \le 100$), a brute-force approach that checks all $O(N^2)$ subarrays is both simple and performance-adequate. We use standard data structures like hash sets or simple boolean arrays to track the distinct values within the inner loop.

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
    int sumCounts(vector<int>& nums) {
        int totalSum = 0;
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            std::unordered_set<int> distinct;
            for (int j = i; j < n; ++j) {
                distinct.insert(nums[j]);
                int count = distinct.size();
                totalSum += count * count;
            }
        }
        return totalSum;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.*;

class Solution {
    public int sumCounts(List<Integer> nums) {
        int totalSum = 0;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            Set<Integer> distinct = new HashSet<>();
            for (int j = i; j < n; j++) {
                distinct.add(nums.get(j));
                int count = distinct.size();
                totalSum += count * count;
            }
        }
        return totalSum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = 0
        n = len(nums)
        for i in range(n):
            distinct = set()
            for j in range(i, n):
                distinct.add(nums[j])
                count = len(distinct)
                total_sum += count * count
        return total_sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total_sum = 0
        n = len(nums)
        for i in range(n):
            distinct = set()
            for j in range(i, n):
                distinct.add(nums[j])
                count = len(distinct)
                total_sum += count * count
        return total_sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int sumCounts(int* nums, int numsSize) {
    int totalSum = 0;
    for (int i = 0; i < numsSize; i++) {
        int seen[101] = {0};
        int distinctCount = 0;
        for (int j = i; j < numsSize; j++) {
            if (seen[nums[j]] == 0) {
                seen[nums[j]] = 1;
                distinctCount++;
            }
            totalSum += (distinctCount * distinctCount);
        }
    }
    return totalSum;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System.Collections.Generic;

public class Solution {
    public int SumCounts(IList<int> nums) {
        int totalSum = 0;
        int n = nums.Count;
        for (int i = 0; i < n; i++) {
            HashSet<int> distinct = new HashSet<int>();
            for (int j = i; j < n; j++) {
                distinct.Add(nums[j]);
                int count = distinct.Count;
                totalSum += count * count;
            }
        }
        return totalSum;
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
var sumCounts = function(nums) {
    let totalSum = 0;
    let n = nums.length;
    for (let i = 0; i < n; i++) {
        let distinct = new Set();
        for (let j = i; j < n; j++) {
            distinct.add(nums[j]);
            let count = distinct.size;
            totalSum += count * count;
        }
    }
    return totalSum;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function sumCounts(nums: number[]): number {
    let totalSum = 0;
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        const distinctSet = new Set<number>();
        for (let j = i; j < n; j++) {
            distinctSet.add(nums[j]);
            const count = distinctSet.size;
            totalSum += count * count;
        }
    }
    return totalSum;
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
    function sumCounts($nums) {
        $totalSum = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $distinct = [];
            for ($j = $i; $j < $n; $j++) {
                $distinct[$nums[$j]] = true;
                $count = count($distinct);
                $totalSum += $count * $count;
            }
        }
        return $totalSum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func sumCounts(_ nums: [Int]) -> Int {
        var totalSum = 0
        let n = nums.count
        for i in 0..<n {
            var distinctSet = Set<Int>()
            for j in i..<n {
                distinctSet.insert(nums[j])
                let count = distinctSet.count
                totalSum += count * count
            }
        }
        return totalSum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun sumCounts(nums: List<Int>): Int {
        var totalSum = 0
        val n = nums.size
        for (i in 0 until n) {
            val distinctSet = mutableSetOf<Int>()
            for (j in i until n) {
                distinctSet.add(nums[j])
                val count = distinctSet.size
                totalSum += count * count
            }
        }
        return totalSum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int sumCounts(List<int> nums) {
    int totalSum = 0;
    int n = nums.length;
    for (int i = 0; i < n; i++) {
      Set<int> distinctSet = {};
      for (int j = i; j < n; j++) {
        distinctSet.add(nums[j]);
        int count = distinctSet.length;
        totalSum += count * count;
      }
    }
    return totalSum;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func sumCounts(nums []int) int {
    totalSum := 0
    n := len(nums)
    for i := 0; i < n; i++ {
        distinctMap := make(map[int]bool)
        for j := i; j < n; j++ {
            distinctMap[nums[j]] = true
            count := len(distinctMap)
            totalSum += count * count
        }
    }
    return totalSum
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def sum_counts(nums)
  total_sum = 0
  n = nums.length
  (0...n).each do |i|
    distinct_elements = {}
    (i...n).each do |j|
      distinct_elements[nums[j]] = true
      count = distinct_elements.size
      total_sum += count * count
    end
  end
  total_sum
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def sumCounts(nums: List[Int]): Int = {
        val n = nums.length
        val numsArr = nums.toArray
        var totalSum = 0
        for (i <- 0 until n) {
            var distinctSet = Set[Int]()
            for (j <- i until n) {
                distinctSet += numsArr(j)
                val count = distinctSet.size
                totalSum += count * count
            }
        }
        totalSum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::HashSet;

impl Solution {
    pub fn sum_counts(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut total_sum = 0;
        for i in 0..n {
            let mut set = HashSet::new();
            for j in i..n {
                set.insert(nums[j]);
                let count = set.len() as i32;
                total_sum += count * count;
            }
        }
        total_sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (sum-counts nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([n (length nums)]
         [nums-vec (list->vector nums)])
    (for/sum ([i (in-range n)])
      (let loop ([j i] [current-set (set)] [inner-sum 0])
        (if (= j n)
            inner-sum
            (let* ([new-set (set-add current-set (vector-ref nums-vec j))]
                   [count (set-count new-set)])
              (loop (+ j 1) new-set (+ inner-sum (* count count)))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec sum_counts(Nums :: [integer()]) -> integer().
sum_counts(Nums) ->
  N = length(Nums),
  NumsVec = list_to_tuple(Nums),
  lists:foldl(fun(I, AccI) ->
    {_, SumJ} = lists:foldl(fun(J, {Set, AccJ}) ->
      Val = element(J, NumsVec),
      NewSet = sets:add_element(Val, Set),
      Count = sets:size(NewSet),
      {NewSet, AccJ + (Count * Count)}
    end, {sets:new(), 0}, lists:seq(I, N)),
    AccI + SumJ
  end, 0, lists:seq(1, N)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec sum_counts(nums :: [integer]) :: integer
  def sum_counts(nums) do
    n = length(nums)
    nums_vec = List.to_tuple(nums)
    Enum.reduce(0..(n - 1), 0, fn i, total_sum ->
      {_, inner_sum} = Enum.reduce(i..(n - 1), {MapSet.new(), 0}, fn j, {set, current_inner_sum} ->
        new_set = MapSet.put(set, elem(nums_vec, j))
        count = MapSet.size(new_set)
        {new_set, current_inner_sum + count * count}
      end)
      total_sum + inner_sum
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N^2) where N is the length of the input array. We use two nested loops to iterate through all possible subarrays, and the work done inside the inner loop (updating the distinct count and calculating the square) takes constant time on average when using a hash set or frequency array.
- **Space Complexity:** O(N) in the worst case. This is required for the hash set or frequency array to store the unique elements of the current subarray being processed, which can contain up to N distinct elements.
