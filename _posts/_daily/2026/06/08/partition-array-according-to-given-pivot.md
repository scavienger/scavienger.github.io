---
layout: post
title: "Partition Array According to Given Pivot"
date: 2026-06-08 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Two Pointers", "Simulation"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/partition-array-according-to-given-pivot/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> pivotArray(vector<int>& nums,\
        \ int pivot) {\n        int n = nums.size();\n        vector<int> res(n);\n\
        \        int left = 0, right = n - 1;\n\n        for (int i = 0; i < n; ++i)\
        \ {\n            if (nums[i] < pivot) {\n                res[left++] = nums[i];\n\
        \            }\n        }\n\n        for (int i = n - 1; i >= 0; --i) {\n  \
        \          if (nums[i] > pivot) {\n                res[right--] = nums[i];\n\
        \            }\n        }\n\n        while (left <= right) {\n            res[left++]\
        \ = pivot;\n        }\n\n        return res;\n    }\n};"
      java: "class Solution {\n    public int[] pivotArray(int[] nums, int pivot) {\n\
        \        int n = nums.length;\n        int[] res = new int[n];\n        int\
        \ left = 0, right = n - 1;\n\n        for (int i = 0; i < n; i++) {\n      \
        \      if (nums[i] < pivot) {\n                res[left++] = nums[i];\n    \
        \        }\n        }\n\n        for (int i = n - 1; i >= 0; i--) {\n      \
        \      if (nums[i] > pivot) {\n                res[right--] = nums[i];\n   \
        \         }\n        }\n\n        while (left <= right) {\n            res[left++]\
        \ = pivot;\n        }\n\n        return res;\n    }\n}"
      python: "class Solution(object):\n    def pivotArray(self, nums, pivot):\n   \
        \     \"\"\"\n        :type nums: List[int]\n        :type pivot: int\n    \
        \    :rtype: List[int]\n        \"\"\"\n        n = len(nums)\n        res =\
        \ [0] * n\n        l, r = 0, n - 1\n\n        for i in xrange(n):\n        \
        \    if nums[i] < pivot:\n                res[l] = nums[i]\n               \
        \ l += 1\n\n        for i in xrange(n - 1, -1, -1):\n            if nums[i]\
        \ > pivot:\n                res[r] = nums[i]\n                r -= 1\n\n   \
        \     while l <= r:\n            res[l] = pivot\n            l += 1\n\n    \
        \    return res"
      python3: "class Solution:\n    def pivotArray(self, nums: List[int], pivot: int)\
        \ -> List[int]:\n        n = len(nums)\n        res = [0] * n\n        l, r\
        \ = 0, n - 1\n\n        for i in range(n):\n            if nums[i] < pivot:\n\
        \                res[l] = nums[i]\n                l += 1\n\n        for i in\
        \ range(n - 1, -1, -1):\n            if nums[i] > pivot:\n                res[r]\
        \ = nums[i]\n                r -= 1\n\n        while l <= r:\n            res[l]\
        \ = pivot\n            l += 1\n\n        return res"
      c: "/**\n * Note: The returned array must be malloced, assume caller calls free().\n\
        \ */\nint* pivotArray(int* nums, int numsSize, int pivot, int* returnSize) {\n\
        \    int* res = (int*)malloc(sizeof(int) * numsSize);\n    *returnSize = numsSize;\n\
        \n    int left = 0, right = numsSize - 1;\n\n    for (int i = 0; i < numsSize;\
        \ i++) {\n        if (nums[i] < pivot) {\n            res[left++] = nums[i];\n\
        \        }\n    }\n\n    for (int i = numsSize - 1; i >= 0; i--) {\n       \
        \ if (nums[i] > pivot) {\n            res[right--] = nums[i];\n        }\n \
        \   }\n\n    while (left <= right) {\n        res[left++] = pivot;\n    }\n\n\
        \    return res;\n}"
      csharp: "public class Solution {\n    public int[] PivotArray(int[] nums, int\
        \ pivot) {\n        int n = nums.Length;\n        int lessCount = 0;\n     \
        \   int equalCount = 0;\n        foreach (int num in nums) {\n            if\
        \ (num < pivot) {\n                lessCount++;\n            } else if (num\
        \ == pivot) {\n                equalCount++;\n            }\n        }\n\n \
        \       int[] result = new int[n];\n        int lt = 0;\n        int eq = lessCount;\n\
        \        int gt = lessCount + equalCount;\n\n        foreach (int num in nums)\
        \ {\n            if (num < pivot) {\n                result[lt++] = num;\n \
        \           } else if (num == pivot) {\n                result[eq++] = num;\n\
        \            } else {\n                result[gt++] = num;\n            }\n\
        \        }\n        return result;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} pivot\n * @return\
        \ {number[]}\n */\nvar pivotArray = function(nums, pivot) {\n    const less\
        \ = [];\n    const equal = [];\n    const greater = [];\n\n    for (const num\
        \ of nums) {\n        if (num < pivot) {\n            less.push(num);\n    \
        \    } else if (num === pivot) {\n            equal.push(num);\n        } else\
        \ {\n            greater.push(num);\n        }\n    }\n\n    return less.concat(equal,\
        \ greater);\n};"
      typescript: "function pivotArray(nums: number[], pivot: number): number[] {\n\
        \    const less: number[] = [];\n    const equal: number[] = [];\n    const\
        \ greater: number[] = [];\n\n    for (const num of nums) {\n        if (num\
        \ < pivot) {\n            less.push(num);\n        } else if (num === pivot)\
        \ {\n            equal.push(num);\n        } else {\n            greater.push(num);\n\
        \        }\n    }\n\n    return less.concat(equal, greater);\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer $pivot\n     * @return Integer[]\n     */\n    function pivotArray($nums,\
        \ $pivot) {\n        $less = [];\n        $equal = [];\n        $greater = [];\n\
        \n        foreach ($nums as $num) {\n            if ($num < $pivot) {\n    \
        \            $less[] = $num;\n            } elseif ($num == $pivot) {\n    \
        \            $equal[] = $num;\n            } else {\n                $greater[]\
        \ = $num;\n            }\n        }\n\n        return array_merge($less, $equal,\
        \ $greater);\n    }\n}"
      swift: "class Solution {\n    func pivotArray(_ nums: [Int], _ pivot: Int) ->\
        \ [Int] {\n        var less = [Int]()\n        var equal = [Int]()\n       \
        \ var greater = [Int]()\n\n        for num in nums {\n            if num < pivot\
        \ {\n                less.append(num)\n            } else if num == pivot {\n\
        \                equal.append(num)\n            } else {\n                greater.append(num)\n\
        \            }\n        }\n\n        return less + equal + greater\n    }\n}"
      kotlin: "class Solution {\n    fun pivotArray(nums: IntArray, pivot: Int): IntArray\
        \ {\n        val n = nums.size\n        val res = IntArray(n)\n        var lessCount\
        \ = 0\n        var equalCount = 0\n        for (x in nums) {\n            if\
        \ (x < pivot) {\n                lessCount++\n            } else if (x == pivot)\
        \ {\n                equalCount++\n            }\n        }\n\n        var l\
        \ = 0\n        var e = lessCount\n        var g = lessCount + equalCount\n\n\
        \        for (x in nums) {\n            if (x < pivot) {\n                res[l++]\
        \ = x\n            } else if (x == pivot) {\n                res[e++] = x\n\
        \            } else {\n                res[g++] = x\n            }\n       \
        \ }\n        return res\n    }\n}"
      dart: "class Solution {\n  List<int> pivotArray(List<int> nums, int pivot) {\n\
        \    List<int> less = [];\n    List<int> equal = [];\n    List<int> greater\
        \ = [];\n    for (var n in nums) {\n      if (n < pivot) {\n        less.add(n);\n\
        \      } else if (n == pivot) {\n        equal.add(n);\n      } else {\n   \
        \     greater.add(n);\n      }\n    }\n    return [...less, ...equal, ...greater];\n\
        \  }\n}"
      go: "func pivotArray(nums []int, pivot int) []int {\n    n := len(nums)\n    res\
        \ := make([]int, n)\n    lessCount := 0\n    equalCount := 0\n    for _, x :=\
        \ range nums {\n        if x < pivot {\n            lessCount++\n        } else\
        \ if x == pivot {\n            equalCount++\n        }\n    }\n    l, e, g :=\
        \ 0, lessCount, lessCount+equalCount\n    for _, x := range nums {\n       \
        \ if x < pivot {\n            res[l] = x\n            l++\n        } else if\
        \ x == pivot {\n            res[e] = x\n            e++\n        } else {\n\
        \            res[g] = x\n            g++\n        }\n    }\n    return res\n\
        }"
      ruby: "# @param {Integer[]} nums\n# @param {Integer} pivot\n# @return {Integer[]}\n\
        def pivot_array(nums, pivot)\n    less = []\n    equal = []\n    greater = []\n\
        \    nums.each do |n|\n        if n < pivot\n            less << n\n       \
        \ elsif n == pivot\n            equal << n\n        else\n            greater\
        \ << n\n        end\n    end\n    less + equal + greater\nend"
      scala: "object Solution {\n    def pivotArray(nums: Array[Int], pivot: Int): Array[Int]\
        \ = {\n        val n = nums.length\n        val res = new Array[Int](n)\n  \
        \      var lessCount = 0\n        var equalCount = 0\n        for (x <- nums)\
        \ {\n            if (x < pivot) lessCount += 1\n            else if (x == pivot)\
        \ equalCount += 1\n        }\n        var l = 0\n        var e = lessCount\n\
        \        var g = lessCount + equalCount\n        for (x <- nums) {\n       \
        \     if (x < pivot) {\n                res(l) = x\n                l += 1\n\
        \            } else if (x == pivot) {\n                res(e) = x\n        \
        \        e += 1\n            } else {\n                res(g) = x\n        \
        \        g += 1\n            }\n        }\n        res\n    }\n}"
      rust: "impl Solution {\n    pub fn pivot_array(nums: Vec<i32>, pivot: i32) ->\
        \ Vec<i32> {\n        let mut less = Vec::with_capacity(nums.len());\n     \
        \   let mut equal = Vec::with_capacity(nums.len());\n        let mut greater\
        \ = Vec::with_capacity(nums.len());\n\n        for &num in nums.iter() {\n \
        \           if num < pivot {\n                less.push(num);\n            }\
        \ else if num == pivot {\n                equal.push(num);\n            } else\
        \ {\n                greater.push(num);\n            }\n        }\n\n      \
        \  less.extend(equal);\n        less.extend(greater);\n        less\n    }\n\
        }"
      racket: "(define/contract (pivot-array nums pivot)\n  (-> (listof exact-integer?)\
        \ exact-integer? (listof exact-integer?))\n  (let ([less (filter (lambda (x)\
        \ (< x pivot)) nums)]\n        [equal (filter (lambda (x) (= x pivot)) nums)]\n\
        \        [greater (filter (lambda (x) (> x pivot)) nums)])\n    (append less\
        \ equal greater)))"
      erlang: "-spec pivot_array(Nums :: [integer()], Pivot :: integer()) -> [integer()].\n\
        pivot_array(Nums, Pivot) ->\n    Less = [X || X <- Nums, X < Pivot],\n    Equal\
        \ = [X || X <- Nums, X == Pivot],\n    Greater = [X || X <- Nums, X > Pivot],\n\
        \    Less ++ Equal ++ Greater."
      elixir: "defmodule Solution do\n  @spec pivot_array(nums :: [integer], pivot ::\
        \ integer) :: [integer]\n  def pivot_array(nums, pivot) do\n    less = Enum.filter(nums,\
        \ fn x -> x < pivot end)\n    equal = Enum.filter(nums, fn x -> x == pivot end)\n\
        \    greater = Enum.filter(nums, fn x -> x > pivot end)\n    less ++ equal ++\
        \ greater\n  end\nend"
    approach: "The problem asks to partition an array into three groups based on a pivot\
      \ value—elements smaller than, equal to, and greater than the pivot—while maintaining\
      \ the original relative order within the 'less than' and 'greater than' groups.\
      \ This can be achieved efficiently using a two-pointer-like approach with a secondary\
      \ result array. By iterating forward through the input array, we can identify\
      \ and place all elements smaller than the pivot in their correct relative order\
      \ at the beginning of the result array. \n\nTo preserve the relative order of\
      \ elements greater than the pivot, we iterate through the input array in reverse.\
      \ Elements larger than the pivot are placed starting from the end of the result\
      \ array and moving backward; this backward placement ensures that the last element\
      \ greater than the pivot in the original array remains the last in the partitioned\
      \ result. Finally, any remaining slots in the middle of the result array, which\
      \ correspond to the gap between the 'less than' and 'greater than' sections, are\
      \ filled with the pivot value to complete the partitioning."
    time_complexity: O(n) where n is the number of elements in the input array. We traverse
      the array once forward to place elements smaller than the pivot, once backward
      to place elements larger than the pivot, and perform a final range fill for the
      equal elements, resulting in a linear total execution time.
    space_complexity: O(n) where n is the number of elements in the input array. We
      allocate a new array of size n to store and return the rearranged elements. No
      other auxiliary data structures that scale with the input size are used.
    elapsed_time: 159.23333263397217
    model: gemini-3-flash-preview
    generated_at: '2026-06-08 02:54:08 '
---

## Problem #2161: Partition Array According to Given Pivot

**Difficulty:** Medium

**Topics:** Array, Two Pointers, Simulation

## Problem Description

<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> and an integer <code>pivot</code>. Rearrange <code>nums</code> such that the following conditions are satisfied:</p>

<ul>
	<li>Every element less than <code>pivot</code> appears <strong>before</strong> every element greater than <code>pivot</code>.</li>
	<li>Every element equal to <code>pivot</code> appears <strong>in between</strong> the elements less than and greater than <code>pivot</code>.</li>
	<li>The <strong>relative order</strong> of the elements less than <code>pivot</code> and the elements greater than <code>pivot</code> is maintained.
	<ul>
		<li>More formally, consider every <code>p<sub>i</sub></code>, <code>p<sub>j</sub></code> where <code>p<sub>i</sub></code> is the new position of the <code>i<sup>th</sup></code> element and <code>p<sub>j</sub></code> is the new position of the <code>j<sup>th</sup></code> element. If <code>i &lt; j</code> and <strong>both</strong> elements are smaller (<em>or larger</em>) than <code>pivot</code>, then <code>p<sub>i</sub> &lt; p<sub>j</sub></code>.</li>
	</ul>
	</li>
</ul>

<p>Return <code>nums</code><em> after the rearrangement.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [9,12,5,10,14,3,10], pivot = 10
<strong>Output:</strong> [9,5,3,10,10,12,14]
<strong>Explanation:</strong> 
The elements 9, 5, and 3 are less than the pivot so they are on the left side of the array.
The elements 12 and 14 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [9, 5, 3] and [12, 14] are the respective orderings.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-3,4,3,2], pivot = 2
<strong>Output:</strong> [-3,2,4,3]
<strong>Explanation:</strong> 
The element -3 is less than the pivot so it is on the left side of the array.
The elements 4 and 3 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [-3] and [4, 3] are the respective orderings.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>6</sup> &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>pivot</code> equals to an element of <code>nums</code>.</li>
</ul>


## Hints

1. Could you put the elements smaller than the pivot and greater than the pivot in a separate list as in the sequence that they occur?

2. With the separate lists generated, could you then generate the result?

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks to partition an array into three groups based on a pivot value—elements smaller than, equal to, and greater than the pivot—while maintaining the original relative order within the 'less than' and 'greater than' groups. This can be achieved efficiently using a two-pointer-like approach with a secondary result array. By iterating forward through the input array, we can identify and place all elements smaller than the pivot in their correct relative order at the beginning of the result array. 

To preserve the relative order of elements greater than the pivot, we iterate through the input array in reverse. Elements larger than the pivot are placed starting from the end of the result array and moving backward; this backward placement ensures that the last element greater than the pivot in the original array remains the last in the partitioned result. Finally, any remaining slots in the middle of the result array, which correspond to the gap between the 'less than' and 'greater than' sections, are filled with the pivot value to complete the partitioning.

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
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        int n = nums.size();
        vector<int> res(n);
        int left = 0, right = n - 1;

        for (int i = 0; i < n; ++i) {
            if (nums[i] < pivot) {
                res[left++] = nums[i];
            }
        }

        for (int i = n - 1; i >= 0; --i) {
            if (nums[i] > pivot) {
                res[right--] = nums[i];
            }
        }

        while (left <= right) {
            res[left++] = pivot;
        }

        return res;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        int n = nums.length;
        int[] res = new int[n];
        int left = 0, right = n - 1;

        for (int i = 0; i < n; i++) {
            if (nums[i] < pivot) {
                res[left++] = nums[i];
            }
        }

        for (int i = n - 1; i >= 0; i--) {
            if (nums[i] > pivot) {
                res[right--] = nums[i];
            }
        }

        while (left <= right) {
            res[left++] = pivot;
        }

        return res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        n = len(nums)
        res = [0] * n
        l, r = 0, n - 1

        for i in xrange(n):
            if nums[i] < pivot:
                res[l] = nums[i]
                l += 1

        for i in xrange(n - 1, -1, -1):
            if nums[i] > pivot:
                res[r] = nums[i]
                r -= 1

        while l <= r:
            res[l] = pivot
            l += 1

        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        res = [0] * n
        l, r = 0, n - 1

        for i in range(n):
            if nums[i] < pivot:
                res[l] = nums[i]
                l += 1

        for i in range(n - 1, -1, -1):
            if nums[i] > pivot:
                res[r] = nums[i]
                r -= 1

        while l <= r:
            res[l] = pivot
            l += 1

        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* pivotArray(int* nums, int numsSize, int pivot, int* returnSize) {
    int* res = (int*)malloc(sizeof(int) * numsSize);
    *returnSize = numsSize;

    int left = 0, right = numsSize - 1;

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] < pivot) {
            res[left++] = nums[i];
        }
    }

    for (int i = numsSize - 1; i >= 0; i--) {
        if (nums[i] > pivot) {
            res[right--] = nums[i];
        }
    }

    while (left <= right) {
        res[left++] = pivot;
    }

    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int[] PivotArray(int[] nums, int pivot) {
        int n = nums.Length;
        int lessCount = 0;
        int equalCount = 0;
        foreach (int num in nums) {
            if (num < pivot) {
                lessCount++;
            } else if (num == pivot) {
                equalCount++;
            }
        }

        int[] result = new int[n];
        int lt = 0;
        int eq = lessCount;
        int gt = lessCount + equalCount;

        foreach (int num in nums) {
            if (num < pivot) {
                result[lt++] = num;
            } else if (num == pivot) {
                result[eq++] = num;
            } else {
                result[gt++] = num;
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
 * @param {number[]} nums
 * @param {number} pivot
 * @return {number[]}
 */
var pivotArray = function(nums, pivot) {
    const less = [];
    const equal = [];
    const greater = [];

    for (const num of nums) {
        if (num < pivot) {
            less.push(num);
        } else if (num === pivot) {
            equal.push(num);
        } else {
            greater.push(num);
        }
    }

    return less.concat(equal, greater);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function pivotArray(nums: number[], pivot: number): number[] {
    const less: number[] = [];
    const equal: number[] = [];
    const greater: number[] = [];

    for (const num of nums) {
        if (num < pivot) {
            less.push(num);
        } else if (num === pivot) {
            equal.push(num);
        } else {
            greater.push(num);
        }
    }

    return less.concat(equal, greater);
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
     * @param Integer $pivot
     * @return Integer[]
     */
    function pivotArray($nums, $pivot) {
        $less = [];
        $equal = [];
        $greater = [];

        foreach ($nums as $num) {
            if ($num < $pivot) {
                $less[] = $num;
            } elseif ($num == $pivot) {
                $equal[] = $num;
            } else {
                $greater[] = $num;
            }
        }

        return array_merge($less, $equal, $greater);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func pivotArray(_ nums: [Int], _ pivot: Int) -> [Int] {
        var less = [Int]()
        var equal = [Int]()
        var greater = [Int]()

        for num in nums {
            if num < pivot {
                less.append(num)
            } else if num == pivot {
                equal.append(num)
            } else {
                greater.append(num)
            }
        }

        return less + equal + greater
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun pivotArray(nums: IntArray, pivot: Int): IntArray {
        val n = nums.size
        val res = IntArray(n)
        var lessCount = 0
        var equalCount = 0
        for (x in nums) {
            if (x < pivot) {
                lessCount++
            } else if (x == pivot) {
                equalCount++
            }
        }

        var l = 0
        var e = lessCount
        var g = lessCount + equalCount

        for (x in nums) {
            if (x < pivot) {
                res[l++] = x
            } else if (x == pivot) {
                res[e++] = x
            } else {
                res[g++] = x
            }
        }
        return res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<int> pivotArray(List<int> nums, int pivot) {
    List<int> less = [];
    List<int> equal = [];
    List<int> greater = [];
    for (var n in nums) {
      if (n < pivot) {
        less.add(n);
      } else if (n == pivot) {
        equal.add(n);
      } else {
        greater.add(n);
      }
    }
    return [...less, ...equal, ...greater];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func pivotArray(nums []int, pivot int) []int {
    n := len(nums)
    res := make([]int, n)
    lessCount := 0
    equalCount := 0
    for _, x := range nums {
        if x < pivot {
            lessCount++
        } else if x == pivot {
            equalCount++
        }
    }
    l, e, g := 0, lessCount, lessCount+equalCount
    for _, x := range nums {
        if x < pivot {
            res[l] = x
            l++
        } else if x == pivot {
            res[e] = x
            e++
        } else {
            res[g] = x
            g++
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
# @param {Integer[]} nums
# @param {Integer} pivot
# @return {Integer[]}
def pivot_array(nums, pivot)
    less = []
    equal = []
    greater = []
    nums.each do |n|
        if n < pivot
            less << n
        elsif n == pivot
            equal << n
        else
            greater << n
        end
    end
    less + equal + greater
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def pivotArray(nums: Array[Int], pivot: Int): Array[Int] = {
        val n = nums.length
        val res = new Array[Int](n)
        var lessCount = 0
        var equalCount = 0
        for (x <- nums) {
            if (x < pivot) lessCount += 1
            else if (x == pivot) equalCount += 1
        }
        var l = 0
        var e = lessCount
        var g = lessCount + equalCount
        for (x <- nums) {
            if (x < pivot) {
                res(l) = x
                l += 1
            } else if (x == pivot) {
                res(e) = x
                e += 1
            } else {
                res(g) = x
                g += 1
            }
        }
        res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn pivot_array(nums: Vec<i32>, pivot: i32) -> Vec<i32> {
        let mut less = Vec::with_capacity(nums.len());
        let mut equal = Vec::with_capacity(nums.len());
        let mut greater = Vec::with_capacity(nums.len());

        for &num in nums.iter() {
            if num < pivot {
                less.push(num);
            } else if num == pivot {
                equal.push(num);
            } else {
                greater.push(num);
            }
        }

        less.extend(equal);
        less.extend(greater);
        less
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (pivot-array nums pivot)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let ([less (filter (lambda (x) (< x pivot)) nums)]
        [equal (filter (lambda (x) (= x pivot)) nums)]
        [greater (filter (lambda (x) (> x pivot)) nums)])
    (append less equal greater)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec pivot_array(Nums :: [integer()], Pivot :: integer()) -> [integer()].
pivot_array(Nums, Pivot) ->
    Less = [X || X <- Nums, X < Pivot],
    Equal = [X || X <- Nums, X == Pivot],
    Greater = [X || X <- Nums, X > Pivot],
    Less ++ Equal ++ Greater.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec pivot_array(nums :: [integer], pivot :: integer) :: [integer]
  def pivot_array(nums, pivot) do
    less = Enum.filter(nums, fn x -> x < pivot end)
    equal = Enum.filter(nums, fn x -> x == pivot end)
    greater = Enum.filter(nums, fn x -> x > pivot end)
    less ++ equal ++ greater
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the number of elements in the input array. We traverse the array once forward to place elements smaller than the pivot, once backward to place elements larger than the pivot, and perform a final range fill for the equal elements, resulting in a linear total execution time.
- **Space Complexity:** O(n) where n is the number of elements in the input array. We allocate a new array of size n to store and return the rearranged elements. No other auxiliary data structures that scale with the input size are used.
