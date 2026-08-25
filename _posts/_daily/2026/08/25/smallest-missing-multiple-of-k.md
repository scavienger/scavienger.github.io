---
layout: post
title: "Smallest Missing Multiple of K"
date: 2026-08-25 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Hash Table"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/smallest-missing-multiple-of-k/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int missingMultiple(vector<int>& nums, int\
        \ k) {\n        bool exists[101] = {false};\n        for (int num : nums) {\n\
        \            if (num <= 100) {\n                exists[num] = true;\n      \
        \      }\n        }\n        int current = k;\n        while (true) {\n    \
        \        if (current > 100 || !exists[current]) {\n                return current;\n\
        \            }\n            current += k;\n        }\n    }\n};"
      java: "import java.util.HashSet;\nimport java.util.Set;\n\nclass Solution {\n\
        \    public int missingMultiple(int[] nums, int k) {\n        Set<Integer> set\
        \ = new HashSet<>();\n        for (int num : nums) {\n            set.add(num);\n\
        \        }\n        int current = k;\n        while (true) {\n            if\
        \ (!set.contains(current)) {\n                return current;\n            }\n\
        \            current += k;\n        }\n    }\n}"
      python: "class Solution(object):\n    def missingMultiple(self, nums, k):\n  \
        \      \"\"\"\n        :type nums: List[int]\n        :type k: int\n       \
        \ :rtype: int\n        \"\"\"\n        num_set = set(nums)\n        current\
        \ = k\n        while True:\n            if current not in num_set:\n       \
        \         return current\n            current += k"
      python3: "class Solution:\n    def missingMultiple(self, nums: List[int], k: int)\
        \ -> int:\n        num_set = set(nums)\n        current = k\n        while True:\n\
        \            if current not in num_set:\n                return current\n  \
        \          current += k"
      c: "int missingMultiple(int* nums, int numsSize, int k) {\n    int exists[101]\
        \ = {0};\n    for (int i = 0; i < numsSize; i++) {\n        if (nums[i] <= 100)\
        \ {\n            exists[nums[i]] = 1;\n        }\n    }\n    int current = k;\n\
        \    while (1) {\n        if (current > 100 || !exists[current]) {\n       \
        \     return current;\n        }\n        current += k;\n    }\n}"
      csharp: "using System.Collections.Generic;\n\npublic class Solution {\n    public\
        \ int MissingMultiple(int[] nums, int k) {\n        HashSet<int> set = new HashSet<int>(nums);\n\
        \        int current = k;\n        while (true) {\n            if (!set.Contains(current))\
        \ {\n                return current;\n            }\n            current +=\
        \ k;\n        }\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} k\n * @return\
        \ {number}\n */\nvar missingMultiple = function(nums, k) {\n    const numSet\
        \ = new Set(nums);\n    let current = k;\n    while (true) {\n        if (!numSet.has(current))\
        \ {\n            return current;\n        }\n        current += k;\n    }\n\
        };"
      typescript: "function missingMultiple(nums: number[], k: number): number {\n \
        \   const numSet = new Set(nums);\n    let current = k;\n    while (numSet.has(current))\
        \ {\n        current += k;\n    }\n    return current;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer $k\n     * @return Integer\n     */\n    function missingMultiple($nums,\
        \ $k) {\n        $set = array_flip($nums);\n        $multiple = $k;\n      \
        \  while (isset($set[$multiple])) {\n            $multiple += $k;\n        }\n\
        \        return $multiple;\n    }\n}"
      swift: "class Solution {\n    func missingMultiple(_ nums: [Int], _ k: Int) ->\
        \ Int {\n        let numSet = Set(nums)\n        var multiple = k\n        while\
        \ numSet.contains(multiple) {\n            multiple += k\n        }\n      \
        \  return multiple\n    }\n}"
      kotlin: "class Solution {\n    fun missingMultiple(nums: IntArray, k: Int): Int\
        \ {\n        val numSet = nums.toSet()\n        var multiple = k\n        while\
        \ (numSet.contains(multiple)) {\n            multiple += k\n        }\n    \
        \    return multiple\n    }\n}"
      dart: "class Solution {\n  int missingMultiple(List<int> nums, int k) {\n    final\
        \ numSet = nums.toSet();\n    int multiple = k;\n    while (numSet.contains(multiple))\
        \ {\n      multiple += k;\n    }\n    return multiple;\n  }\n}"
      go: "func missingMultiple(nums []int, k int) int {\n    numSet := make(map[int]bool)\n\
        \    for _, num := range nums {\n        numSet[num] = true\n    }\n    multiple\
        \ := k\n    for numSet[multiple] {\n        multiple += k\n    }\n    return\
        \ multiple\n}"
      ruby: "# @param {Integer[]} nums\n# @param {Integer} k\n# @return {Integer}\n\
        def missing_multiple(nums, k)\n  multiple = k\n  while nums.include?(multiple)\n\
        \    multiple += k\n  end\n  multiple\nend"
      scala: "object Solution {\n    def missingMultiple(nums: Array[Int], k: Int):\
        \ Int = {\n        val numSet = nums.toSet\n        var multiple = k\n     \
        \   while (numSet.contains(multiple)) {\n            multiple += k\n       \
        \ }\n        multiple\n    }\n}"
      rust: "impl Solution {\n    pub fn missing_multiple(nums: Vec<i32>, k: i32) ->\
        \ i32 {\n        let mut multiple = k;\n        while nums.contains(&multiple)\
        \ {\n            multiple += k;\n        }\n        multiple\n    }\n}"
      racket: "(define/contract (missing-multiple nums k)\n  (-> (listof exact-integer?)\
        \ exact-integer? exact-integer?)\n  (let loop ([m k])\n    (if (member m nums)\n\
        \        (loop (+ m k))\n        m)))"
      erlang: "-spec missing_multiple(Nums :: [integer()], K :: integer()) -> integer().\n\
        missing_multiple(Nums, K) ->\n  missing_multiple(Nums, K, K).\n\nmissing_multiple(Nums,\
        \ Current, K) ->\n  case lists:member(Current, Nums) of\n    true -> missing_multiple(Nums,\
        \ Current + K, K);\n    false -> Current\n  end."
      elixir: "defmodule Solution do\n  @spec missing_multiple(nums :: [integer], k\
        \ :: integer) :: integer\n  def missing_multiple(nums, k) do\n    k\n    |>\
        \ Stream.iterate(&(&1 + k))\n    |> Enum.find(fn m -> m not in nums end)\n \
        \ end\nend"
    approach: 'To find the smallest missing multiple of k, we first insert all elements
      of the input array nums into a hash set (or a boolean frequency array) to enable
      efficient O(1) lookups. This preprocessing step ensures that we can determine
      whether a specific integer exists in the input array in constant time, avoiding
      repeated linear scans as we iterate through candidates.


      After building the lookup structure, we iterate through positive multiples of
      k starting from k itself (k * 1, k * 2, k * 3, ...). For each multiple, we check
      if it exists in the set. The first multiple that is not found in the set is the
      smallest missing multiple of k. Since the maximum value in nums is 100, the iteration
      will conclude very quickly, as any multiple greater than 100 is guaranteed to
      be missing.'
    time_complexity: O(N + M) where N is the length of the input array and M is the
      number of multiples checked. We iterate through the array once to populate the
      set, which takes O(N), and then check at most 101 multiples of k, resulting in
      a linear time complexity relative to the constraints.
    space_complexity: O(U) where U is the number of unique elements in nums stored in
      the hash set. Given the constraints that the values are between 1 and 100, the
      space used is at most O(100), which is effectively constant space.
    elapsed_time: 428.9976553916931
    model: gemini-3-flash-preview
    generated_at: '2026-08-25 00:56:03 '
---

## Problem #3718: Smallest Missing Multiple of K

**Difficulty:** Easy

**Topics:** Array, Hash Table

## Problem Description

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return the <strong>smallest positive multiple</strong> of <code>k</code> that is <strong>missing</strong> from <code>nums</code>.</p>

<p>A <strong>multiple</strong> of <code>k</code> is any positive integer divisible by <code>k</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [8,2,3,4,6], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">10</span></p>

<p><strong>Explanation:</strong></p>

<p>The multiples of <code>k = 2</code> are 2, 4, 6, 8, 10, 12... and the smallest multiple missing from <code>nums</code> is 10.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,4,7,10,15], k = 5</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p>The multiples of <code>k = 5</code> are 5, 10, 15, 20... and the smallest multiple missing from <code>nums</code> is 5.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= 100</code></li>
</ul>


## Hints

1. Add the values in `nums` to a hash set

2. Iterate through the positive multiples of `k` and return the first one not in the hash set

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To find the smallest missing multiple of k, we first insert all elements of the input array nums into a hash set (or a boolean frequency array) to enable efficient O(1) lookups. This preprocessing step ensures that we can determine whether a specific integer exists in the input array in constant time, avoiding repeated linear scans as we iterate through candidates.

After building the lookup structure, we iterate through positive multiples of k starting from k itself (k * 1, k * 2, k * 3, ...). For each multiple, we check if it exists in the set. The first multiple that is not found in the set is the smallest missing multiple of k. Since the maximum value in nums is 100, the iteration will conclude very quickly, as any multiple greater than 100 is guaranteed to be missing.

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
    int missingMultiple(vector<int>& nums, int k) {
        bool exists[101] = {false};
        for (int num : nums) {
            if (num <= 100) {
                exists[num] = true;
            }
        }
        int current = k;
        while (true) {
            if (current > 100 || !exists[current]) {
                return current;
            }
            current += k;
        }
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int missingMultiple(int[] nums, int k) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        int current = k;
        while (true) {
            if (!set.contains(current)) {
                return current;
            }
            current += k;
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        num_set = set(nums)
        current = k
        while True:
            if current not in num_set:
                return current
            current += k
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num_set = set(nums)
        current = k
        while True:
            if current not in num_set:
                return current
            current += k
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int missingMultiple(int* nums, int numsSize, int k) {
    int exists[101] = {0};
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] <= 100) {
            exists[nums[i]] = 1;
        }
    }
    int current = k;
    while (1) {
        if (current > 100 || !exists[current]) {
            return current;
        }
        current += k;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System.Collections.Generic;

public class Solution {
    public int MissingMultiple(int[] nums, int k) {
        HashSet<int> set = new HashSet<int>(nums);
        int current = k;
        while (true) {
            if (!set.Contains(current)) {
                return current;
            }
            current += k;
        }
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
var missingMultiple = function(nums, k) {
    const numSet = new Set(nums);
    let current = k;
    while (true) {
        if (!numSet.has(current)) {
            return current;
        }
        current += k;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function missingMultiple(nums: number[], k: number): number {
    const numSet = new Set(nums);
    let current = k;
    while (numSet.has(current)) {
        current += k;
    }
    return current;
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
    function missingMultiple($nums, $k) {
        $set = array_flip($nums);
        $multiple = $k;
        while (isset($set[$multiple])) {
            $multiple += $k;
        }
        return $multiple;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func missingMultiple(_ nums: [Int], _ k: Int) -> Int {
        let numSet = Set(nums)
        var multiple = k
        while numSet.contains(multiple) {
            multiple += k
        }
        return multiple
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun missingMultiple(nums: IntArray, k: Int): Int {
        val numSet = nums.toSet()
        var multiple = k
        while (numSet.contains(multiple)) {
            multiple += k
        }
        return multiple
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int missingMultiple(List<int> nums, int k) {
    final numSet = nums.toSet();
    int multiple = k;
    while (numSet.contains(multiple)) {
      multiple += k;
    }
    return multiple;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func missingMultiple(nums []int, k int) int {
    numSet := make(map[int]bool)
    for _, num := range nums {
        numSet[num] = true
    }
    multiple := k
    for numSet[multiple] {
        multiple += k
    }
    return multiple
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
def missing_multiple(nums, k)
  multiple = k
  while nums.include?(multiple)
    multiple += k
  end
  multiple
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def missingMultiple(nums: Array[Int], k: Int): Int = {
        val numSet = nums.toSet
        var multiple = k
        while (numSet.contains(multiple)) {
            multiple += k
        }
        multiple
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn missing_multiple(nums: Vec<i32>, k: i32) -> i32 {
        let mut multiple = k;
        while nums.contains(&multiple) {
            multiple += k;
        }
        multiple
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (missing-multiple nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let loop ([m k])
    (if (member m nums)
        (loop (+ m k))
        m)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec missing_multiple(Nums :: [integer()], K :: integer()) -> integer().
missing_multiple(Nums, K) ->
  missing_multiple(Nums, K, K).

missing_multiple(Nums, Current, K) ->
  case lists:member(Current, Nums) of
    true -> missing_multiple(Nums, Current + K, K);
    false -> Current
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec missing_multiple(nums :: [integer], k :: integer) :: integer
  def missing_multiple(nums, k) do
    k
    |> Stream.iterate(&(&1 + k))
    |> Enum.find(fn m -> m not in nums end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N + M) where N is the length of the input array and M is the number of multiples checked. We iterate through the array once to populate the set, which takes O(N), and then check at most 101 multiples of k, resulting in a linear time complexity relative to the constraints.
- **Space Complexity:** O(U) where U is the number of unique elements in nums stored in the hash set. Given the constraints that the values are between 1 and 100, the space used is at most O(100), which is effectively constant space.
