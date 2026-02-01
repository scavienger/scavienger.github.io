---
layout: post
title: "Divide an Array Into Subarrays With Minimum Cost I"
date: 2026-02-01 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Sorting", "Enumeration"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <algorithm>\n\nclass Solution {\npublic:\n \
        \   int minimumCost(std::vector<int>& nums) {\n        std::sort(nums.begin()\
        \ + 1, nums.end());\n        return nums[0] + nums[1] + nums[2];\n    }\n};"
      java: "import java.util.Arrays;\n\nclass Solution {\n    public int minimumCost(int[]\
        \ nums) {\n        Arrays.sort(nums, 1, nums.length);\n        return nums[0]\
        \ + nums[1] + nums[2];\n    }\n}"
      python: "class Solution(object):\n    def minimumCost(self, nums):\n        \"\
        \"\"\n        :type nums: List[int]\n        :rtype: int\n        \"\"\"\n \
        \       suffix = sorted(nums[1:])\n        return nums[0] + suffix[0] + suffix[1]"
      python3: "class Solution:\n    def minimumCost(self, nums: List[int]) -> int:\n\
        \        suffix = sorted(nums[1:])\n        return nums[0] + suffix[0] + suffix[1]"
      c: "int minimumCost(int* nums, int numsSize) {\n    int min1 = 101;\n    int min2\
        \ = 101;\n    for (int i = 1; i < numsSize; i++) {\n        if (nums[i] < min1)\
        \ {\n            min2 = min1;\n            min1 = nums[i];\n        } else if\
        \ (nums[i] < min2) {\n            min2 = nums[i];\n        }\n    }\n    return\
        \ nums[0] + min1 + min2;\n}"
      csharp: "using System;\n\npublic class Solution {\n    public int MinimumCost(int[]\
        \ nums) {\n        Array.Sort(nums, 1, nums.Length - 1);\n        return nums[0]\
        \ + nums[1] + nums[2];\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar minimumCost\
        \ = function(nums) {\n    const suffix = nums.slice(1).sort((a, b) => a - b);\n\
        \    return nums[0] + suffix[0] + suffix[1];\n};"
      typescript: "function minimumCost(nums: number[]): number {\n    const rest =\
        \ nums.slice(1).sort((a, b) => a - b);\n    return nums[0] + rest[0] + rest[1];\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function minimumCost($nums) {\n        $rest = array_slice($nums,\
        \ 1);\n        sort($rest);\n        return $nums[0] + $rest[0] + $rest[1];\n\
        \    }\n}"
      swift: "class Solution {\n    func minimumCost(_ nums: [Int]) -> Int {\n     \
        \   let rest = nums[1...].sorted()\n        return nums[0] + rest[0] + rest[1]\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun minimumCost(nums: IntArray): Int {\n      \
        \  val rest = nums.sliceArray(1 until nums.size)\n        rest.sort()\n    \
        \    return nums[0] + rest[0] + rest[1]\n    }\n}"
      dart: "class Solution {\n  int minimumCost(List<int> nums) {\n    var rest = nums.sublist(1);\n\
        \    rest.sort();\n    return nums[0] + rest[0] + rest[1];\n  }\n}"
      go: "func minimumCost(nums []int) int {\n    m1, m2 := 51, 51\n    for i := 1;\
        \ i < len(nums); i++ {\n        if nums[i] < m1 {\n            m2 = m1\n   \
        \         m1 = nums[i]\n        } else if nums[i] < m2 {\n            m2 = nums[i]\n\
        \        }\n    }\n    return nums[0] + m1 + m2\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef minimum_cost(nums)\n\
        \  first = nums[0]\n  rest = nums[1..-1].sort\n  first + rest[0] + rest[1]\n\
        end"
      scala: "object Solution {\n    def minimumCost(nums: Array[Int]): Int = {\n  \
        \      val first = nums(0)\n        val rest = nums.tail.sorted\n        first\
        \ + rest(0) + rest(1)\n    }\n}"
      rust: "impl Solution {\n    pub fn minimum_cost(nums: Vec<i32>) -> i32 {\n   \
        \     let first = nums[0];\n        let mut rest = nums[1..].to_vec();\n   \
        \     rest.sort();\n        first + rest[0] + rest[1]\n    }\n}"
      racket: "(define/contract (minimum-cost nums)\n  (-> (listof exact-integer?) exact-integer?)\n\
        \  (let* ([first (car nums)]\n         [rest (sort (cdr nums) <)])\n    (+ first\
        \ (first rest) (second rest))))"
      erlang: "-spec minimum_cost(Nums :: [integer()]) -> integer().\nminimum_cost([First\
        \ | Rest]) ->\n  Sorted = lists:sort(Rest),\n  [S1, S2 | _] = Sorted,\n  First\
        \ + S1 + S2."
      elixir: "defmodule Solution do\n  @spec minimum_cost(nums :: [integer]) :: integer\n\
        \  def minimum_cost([head | tail]) do\n    [s1, s2 | _] = Enum.sort(tail)\n\
        \    head + s1 + s2\n  end\nend"
    approach: 'The problem asks to divide an array into three disjoint contiguous subarrays
      while minimizing the sum of their first elements. The first subarray must always
      start at the very first element of the array, `nums[0]`, so its cost is fixed.
      To achieve the minimum total cost, we must select two additional indices in the
      remaining part of the array (from index 1 to $n-1$) to serve as the start of the
      second and third subarrays.


      To minimize the total sum, we need to choose the two smallest values from the
      array excluding the first element. We can efficiently find these values by sorting
      the subarray that begins at index 1 and goes to the end of the array. After sorting,
      the two smallest elements will be at the first two positions of this sorted suffix.
      The final result is the sum of `nums[0]` and these two smallest values.'
    time_complexity: O(n \log n) where $n$ is the length of the input array. This is
      due to sorting the subarray of size $n-1$ to identify the two smallest elements.
      In languages like C, a simple $O(n)$ traversal can also be used to find the two
      minimums.
    space_complexity: O(n) where $n$ is the length of the array. This complexity arises
      from creating a copy of the subarray or from the auxiliary space required by the
      sorting algorithms used in most standard libraries.
    elapsed_time: 345.42557168006897
    model: gemini-3-flash-preview
    generated_at: '2026-02-01 01:49:49 '
---

## Problem #3010: Divide an Array Into Subarrays With Minimum Cost I

**Difficulty:** Easy

**Topics:** Array, Sorting, Enumeration

## Problem Description

<p>You are given an array of integers <code>nums</code> of length <code>n</code>.</p>

<p>The <strong>cost</strong> of an array is the value of its <strong>first</strong> element. For example, the cost of <code>[1,2,3]</code> is <code>1</code> while the cost of <code>[3,4,1]</code> is <code>3</code>.</p>

<p>You need to divide <code>nums</code> into <code>3</code> <strong>disjoint contiguous </strong><span data-keyword="subarray-nonempty">subarrays</span>.</p>

<p>Return <em>the <strong>minimum</strong> possible <strong>sum</strong> of the cost of these subarrays</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,12]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The best possible way to form 3 subarrays is: [1], [2], and [3,12] at a total cost of 1 + 2 + 3 = 6.
The other possible ways to form 3 subarrays are:
- [1], [2,3], and [12] at a total cost of 1 + 2 + 12 = 15.
- [1,2], [3], and [12] at a total cost of 1 + 3 + 12 = 16.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,4,3]
<strong>Output:</strong> 12
<strong>Explanation:</strong> The best possible way to form 3 subarrays is: [5], [4], and [3] at a total cost of 5 + 4 + 3 = 12.
It can be shown that 12 is the minimum cost achievable.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,3,1,1]
<strong>Output:</strong> 12
<strong>Explanation:</strong> The best possible way to form 3 subarrays is: [10,3], [1], and [1] at a total cost of 10 + 1 + 1 = 12.
It can be shown that 12 is the minimum cost achievable.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= n &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 50</code></li>
</ul>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks to divide an array into three disjoint contiguous subarrays while minimizing the sum of their first elements. The first subarray must always start at the very first element of the array, `nums[0]`, so its cost is fixed. To achieve the minimum total cost, we must select two additional indices in the remaining part of the array (from index 1 to $n-1$) to serve as the start of the second and third subarrays.

To minimize the total sum, we need to choose the two smallest values from the array excluding the first element. We can efficiently find these values by sorting the subarray that begins at index 1 and goes to the end of the array. After sorting, the two smallest elements will be at the first two positions of this sorted suffix. The final result is the sum of `nums[0]` and these two smallest values.

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
    int minimumCost(std::vector<int>& nums) {
        std::sort(nums.begin() + 1, nums.end());
        return nums[0] + nums[1] + nums[2];
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.Arrays;

class Solution {
    public int minimumCost(int[] nums) {
        Arrays.sort(nums, 1, nums.length);
        return nums[0] + nums[1] + nums[2];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        suffix = sorted(nums[1:])
        return nums[0] + suffix[0] + suffix[1]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        suffix = sorted(nums[1:])
        return nums[0] + suffix[0] + suffix[1]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int minimumCost(int* nums, int numsSize) {
    int min1 = 101;
    int min2 = 101;
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] < min1) {
            min2 = min1;
            min1 = nums[i];
        } else if (nums[i] < min2) {
            min2 = nums[i];
        }
    }
    return nums[0] + min1 + min2;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public int MinimumCost(int[] nums) {
        Array.Sort(nums, 1, nums.Length - 1);
        return nums[0] + nums[1] + nums[2];
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
var minimumCost = function(nums) {
    const suffix = nums.slice(1).sort((a, b) => a - b);
    return nums[0] + suffix[0] + suffix[1];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimumCost(nums: number[]): number {
    const rest = nums.slice(1).sort((a, b) => a - b);
    return nums[0] + rest[0] + rest[1];
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
    function minimumCost($nums) {
        $rest = array_slice($nums, 1);
        sort($rest);
        return $nums[0] + $rest[0] + $rest[1];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minimumCost(_ nums: [Int]) -> Int {
        let rest = nums[1...].sorted()
        return nums[0] + rest[0] + rest[1]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minimumCost(nums: IntArray): Int {
        val rest = nums.sliceArray(1 until nums.size)
        rest.sort()
        return nums[0] + rest[0] + rest[1]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minimumCost(List<int> nums) {
    var rest = nums.sublist(1);
    rest.sort();
    return nums[0] + rest[0] + rest[1];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minimumCost(nums []int) int {
    m1, m2 := 51, 51
    for i := 1; i < len(nums); i++ {
        if nums[i] < m1 {
            m2 = m1
            m1 = nums[i]
        } else if nums[i] < m2 {
            m2 = nums[i]
        }
    }
    return nums[0] + m1 + m2
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def minimum_cost(nums)
  first = nums[0]
  rest = nums[1..-1].sort
  first + rest[0] + rest[1]
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minimumCost(nums: Array[Int]): Int = {
        val first = nums(0)
        val rest = nums.tail.sorted
        first + rest(0) + rest(1)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn minimum_cost(nums: Vec<i32>) -> i32 {
        let first = nums[0];
        let mut rest = nums[1..].to_vec();
        rest.sort();
        first + rest[0] + rest[1]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (minimum-cost nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([first (car nums)]
         [rest (sort (cdr nums) <)])
    (+ first (first rest) (second rest))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec minimum_cost(Nums :: [integer()]) -> integer().
minimum_cost([First | Rest]) ->
  Sorted = lists:sort(Rest),
  [S1, S2 | _] = Sorted,
  First + S1 + S2.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_cost(nums :: [integer]) :: integer
  def minimum_cost([head | tail]) do
    [s1, s2 | _] = Enum.sort(tail)
    head + s1 + s2
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n \log n) where $n$ is the length of the input array. This is due to sorting the subarray of size $n-1$ to identify the two smallest elements. In languages like C, a simple $O(n)$ traversal can also be used to find the two minimums.
- **Space Complexity:** O(n) where $n$ is the length of the array. This complexity arises from creating a copy of the subarray or from the auxiliary space required by the sorting algorithms used in most standard libraries.
