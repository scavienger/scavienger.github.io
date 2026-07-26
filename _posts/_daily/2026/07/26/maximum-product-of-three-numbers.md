---
layout: post
title: "Maximum Product of Three Numbers"
date: 2026-07-26 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Math", "Sorting"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/maximum-product-of-three-numbers/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nclass\
        \ Solution {\npublic:\n    int maximumProduct(vector<int>& nums) {\n       \
        \ sort(nums.begin(), nums.end());\n        int n = nums.size();\n        int\
        \ option1 = nums[n - 1] * nums[n - 2] * nums[n - 3];\n        int option2 =\
        \ nums[0] * nums[1] * nums[n - 1];\n        return max(option1, option2);\n\
        \    }\n};"
      java: "import java.util.Arrays;\n\nclass Solution {\n    public int maximumProduct(int[]\
        \ nums) {\n        Arrays.sort(nums);\n        int n = nums.length;\n      \
        \  int option1 = nums[n - 1] * nums[n - 2] * nums[n - 3];\n        int option2\
        \ = nums[0] * nums[1] * nums[n - 1];\n        return Math.max(option1, option2);\n\
        \    }\n}"
      python: "class Solution(object):\n    def maximumProduct(self, nums):\n      \
        \  \"\"\"\n        :type nums: List[int]\n        :rtype: int\n        \"\"\"\
        \n        nums.sort()\n        n = len(nums)\n        option1 = nums[n - 1]\
        \ * nums[n - 2] * nums[n - 3]\n        option2 = nums[0] * nums[1] * nums[n\
        \ - 1]\n        return max(option1, option2)"
      python3: "class Solution:\n    def maximumProduct(self, nums: List[int]) -> int:\n\
        \        nums.sort()\n        n = len(nums)\n        option1 = nums[n - 1] *\
        \ nums[n - 2] * nums[n - 3]\n        option2 = nums[0] * nums[1] * nums[n -\
        \ 1]\n        return max(option1, option2)"
      c: "#include <stdlib.h>\n\nint compare(const void* a, const void* b) {\n    int\
        \ arg1 = *(const int*)a;\n    int arg2 = *(const int*)b;\n    if (arg1 < arg2)\
        \ return -1;\n    if (arg1 > arg2) return 1;\n    return 0;\n}\n\nint maximumProduct(int*\
        \ nums, int numsSize) {\n    qsort(nums, numsSize, sizeof(int), compare);\n\
        \    int option1 = nums[numsSize - 1] * nums[numsSize - 2] * nums[numsSize -\
        \ 3];\n    int option2 = nums[0] * nums[1] * nums[numsSize - 1];\n    return\
        \ (option1 > option2) ? option1 : option2;\n}"
      csharp: "using System;\n\npublic class Solution {\n    public int MaximumProduct(int[]\
        \ nums) {\n        Array.Sort(nums);\n        int n = nums.Length;\n       \
        \ int option1 = nums[n - 1] * nums[n - 2] * nums[n - 3];\n        int option2\
        \ = nums[0] * nums[1] * nums[n - 1];\n        return Math.Max(option1, option2);\n\
        \    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar maximumProduct\
        \ = function(nums) {\n    nums.sort((a, b) => a - b);\n    let n = nums.length;\n\
        \    let option1 = nums[n - 1] * nums[n - 2] * nums[n - 3];\n    let option2\
        \ = nums[0] * nums[1] * nums[n - 1];\n    return Math.max(option1, option2);\n\
        };"
      typescript: "function maximumProduct(nums: number[]): number {\n    nums.sort((a,\
        \ b) => a - b);\n    const n = nums.length;\n    const p1 = nums[n - 1] * nums[n\
        \ - 2] * nums[n - 3];\n    const p2 = nums[0] * nums[1] * nums[n - 1];\n   \
        \ return Math.max(p1, p2);\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function maximumProduct($nums) {\n        sort($nums);\n\
        \        $n = count($nums);\n        $p1 = $nums[$n - 1] * $nums[$n - 2] * $nums[$n\
        \ - 3];\n        $p2 = $nums[0] * $nums[1] * $nums[$n - 1];\n        return\
        \ max($p1, $p2);\n    }\n}"
      swift: "class Solution {\n    func maximumProduct(_ nums: [Int]) -> Int {\n  \
        \      let sortedNums = nums.sorted()\n        let n = sortedNums.count\n  \
        \      let p1 = sortedNums[n - 1] * sortedNums[n - 2] * sortedNums[n - 3]\n\
        \        let p2 = sortedNums[0] * sortedNums[1] * sortedNums[n - 1]\n      \
        \  return max(p1, p2)\n    }\n}"
      kotlin: "class Solution {\n    fun maximumProduct(nums: IntArray): Int {\n   \
        \     nums.sort()\n        val n = nums.size\n        val p1 = nums[n - 1] *\
        \ nums[n - 2] * nums[n - 3]\n        val p2 = nums[0] * nums[1] * nums[n - 1]\n\
        \        return if (p1 > p2) p1 else p2\n    }\n}"
      dart: "class Solution {\n  int maximumProduct(List<int> nums) {\n    nums.sort();\n\
        \    int n = nums.length;\n    int p1 = nums[n - 1] * nums[n - 2] * nums[n -\
        \ 3];\n    int p2 = nums[0] * nums[1] * nums[n - 1];\n    return p1 > p2 ? p1\
        \ : p2;\n  }\n}"
      go: "import \"sort\"\n\nfunc maximumProduct(nums []int) int {\n    sort.Ints(nums)\n\
        \    n := len(nums)\n    p1 := nums[n-1] * nums[n-2] * nums[n-3]\n    p2 :=\
        \ nums[0] * nums[1] * nums[n-1]\n    if p1 > p2 {\n        return p1\n    }\n\
        \    return p2\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef maximum_product(nums)\n\
        \  s = nums.sort\n  p1 = s[-1] * s[-2] * s[-3]\n  p2 = s[0] * s[1] * s[-1]\n\
        \  p1 > p2 ? p1 : p2\nend"
      scala: "object Solution {\n    def maximumProduct(nums: Array[Int]): Int = {\n\
        \        val s = nums.sorted\n        val n = s.length\n        val p1 = s(n-1)\
        \ * s(n-2) * s(n-3)\n        val p2 = s(0) * s(1) * s(n-1)\n        if (p1 >\
        \ p2) p1 else p2\n    }\n}"
      rust: "impl Solution {\n    pub fn maximum_product(nums: Vec<i32>) -> i32 {\n\
        \        let mut nums = nums;\n        nums.sort();\n        let n = nums.len();\n\
        \        let p1 = nums[n-1] * nums[n-2] * nums[n-3];\n        let p2 = nums[0]\
        \ * nums[1] * nums[n-1];\n        if p1 > p2 { p1 } else { p2 }\n    }\n}"
      racket: "(define/contract (maximum-product nums)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let* ([sorted (sort nums <)]\n         [n (length sorted)]\n\
        \         [a (list-ref sorted (- n 1))]\n         [b (list-ref sorted (- n 2))]\n\
        \         [c (list-ref sorted (- n 3))]\n         [x (list-ref sorted 0)]\n\
        \         [y (list-ref sorted 1)])\n    (max (* a b c) (* x y a))))"
      erlang: "-spec maximum_product(Nums :: [integer()]) -> integer().\nmaximum_product(Nums)\
        \ ->\n  Sorted = lists:sort(Nums),\n  N = length(Sorted),\n  A = lists:nth(N,\
        \ Sorted),\n  B = lists:nth(N - 1, Sorted),\n  C = lists:nth(N - 2, Sorted),\n\
        \  X = lists:nth(1, Sorted),\n  Y = lists:nth(2, Sorted),\n  P1 = A * B * C,\n\
        \  P2 = X * Y * A,\n  if P1 > P2 -> P1; true -> P2 end."
      elixir: "defmodule Solution do\n  @spec maximum_product(nums :: [integer]) ::\
        \ integer\n  def maximum_product(nums) do\n    sorted = Enum.sort(nums)\n  \
        \  n = length(sorted)\n    a = Enum.at(sorted, n - 1)\n    b = Enum.at(sorted,\
        \ n - 2)\n    c = Enum.at(sorted, n - 3)\n    x = Enum.at(sorted, 0)\n    y\
        \ = Enum.at(sorted, 1)\n    p1 = a * b * c\n    p2 = x * y * a\n    max(p1,\
        \ p2)\n  end\nend"
    approach: 'To find the maximum product of three numbers, we consider two possible
      cases after sorting the array in ascending order. The first case is the product
      of the three largest numbers, which is the typical candidate for the maximum value
      when the numbers are primarily positive or all negative. The second case involves
      the product of the two smallest numbers and the largest number. This is crucial
      because if the two smallest numbers are large negative values, their product will
      be positive and, when multiplied by the largest positive number, could exceed
      the product of the three largest positive numbers.


      By sorting the array first, these candidate values—the three largest and the two
      smallest—are conveniently located at the ends of the array. We calculate the products
      for both identified scenarios and return the larger of the two values. This approach
      efficiently covers all possible sign combinations (negative, zero, and positive)
      and ensures the globally maximum product is found.'
    time_complexity: O(n log n) where n is the length of the input array. This time
      complexity is dictated by the sorting of the array, while the subsequent comparison
      and product calculations are performed in O(1) time.
    space_complexity: O(log n) or O(1) depending on the specific sorting algorithm used
      by the language's standard library. For example, some quicksort-based implementations
      use logarithmic auxiliary stack space for recursion.
    elapsed_time: 116.83978343009949
    model: gemini-3-flash-preview
    generated_at: '2026-07-26 02:04:21 '
---

## Problem #628: Maximum Product of Three Numbers

**Difficulty:** Easy

**Topics:** Array, Math, Sorting

## Problem Description

<p>Given an integer array <code>nums</code>, <em>find three numbers whose product is maximum and return the maximum product</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> 6
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> 24
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [-1,-2,-3]
<strong>Output:</strong> -6
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;=&nbsp;10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To find the maximum product of three numbers, we consider two possible cases after sorting the array in ascending order. The first case is the product of the three largest numbers, which is the typical candidate for the maximum value when the numbers are primarily positive or all negative. The second case involves the product of the two smallest numbers and the largest number. This is crucial because if the two smallest numbers are large negative values, their product will be positive and, when multiplied by the largest positive number, could exceed the product of the three largest positive numbers.

By sorting the array first, these candidate values—the three largest and the two smallest—are conveniently located at the ends of the array. We calculate the products for both identified scenarios and return the larger of the two values. This approach efficiently covers all possible sign combinations (negative, zero, and positive) and ensures the globally maximum product is found.

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

using namespace std;

class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int option1 = nums[n - 1] * nums[n - 2] * nums[n - 3];
        int option2 = nums[0] * nums[1] * nums[n - 1];
        return max(option1, option2);
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
    public int maximumProduct(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        int option1 = nums[n - 1] * nums[n - 2] * nums[n - 3];
        int option2 = nums[0] * nums[1] * nums[n - 1];
        return Math.max(option1, option2);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        option1 = nums[n - 1] * nums[n - 2] * nums[n - 3]
        option2 = nums[0] * nums[1] * nums[n - 1]
        return max(option1, option2)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        option1 = nums[n - 1] * nums[n - 2] * nums[n - 3]
        option2 = nums[0] * nums[1] * nums[n - 1]
        return max(option1, option2)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

int compare(const void* a, const void* b) {
    int arg1 = *(const int*)a;
    int arg2 = *(const int*)b;
    if (arg1 < arg2) return -1;
    if (arg1 > arg2) return 1;
    return 0;
}

int maximumProduct(int* nums, int numsSize) {
    qsort(nums, numsSize, sizeof(int), compare);
    int option1 = nums[numsSize - 1] * nums[numsSize - 2] * nums[numsSize - 3];
    int option2 = nums[0] * nums[1] * nums[numsSize - 1];
    return (option1 > option2) ? option1 : option2;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public int MaximumProduct(int[] nums) {
        Array.Sort(nums);
        int n = nums.Length;
        int option1 = nums[n - 1] * nums[n - 2] * nums[n - 3];
        int option2 = nums[0] * nums[1] * nums[n - 1];
        return Math.Max(option1, option2);
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
var maximumProduct = function(nums) {
    nums.sort((a, b) => a - b);
    let n = nums.length;
    let option1 = nums[n - 1] * nums[n - 2] * nums[n - 3];
    let option2 = nums[0] * nums[1] * nums[n - 1];
    return Math.max(option1, option2);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maximumProduct(nums: number[]): number {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const p1 = nums[n - 1] * nums[n - 2] * nums[n - 3];
    const p2 = nums[0] * nums[1] * nums[n - 1];
    return Math.max(p1, p2);
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
    function maximumProduct($nums) {
        sort($nums);
        $n = count($nums);
        $p1 = $nums[$n - 1] * $nums[$n - 2] * $nums[$n - 3];
        $p2 = $nums[0] * $nums[1] * $nums[$n - 1];
        return max($p1, $p2);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maximumProduct(_ nums: [Int]) -> Int {
        let sortedNums = nums.sorted()
        let n = sortedNums.count
        let p1 = sortedNums[n - 1] * sortedNums[n - 2] * sortedNums[n - 3]
        let p2 = sortedNums[0] * sortedNums[1] * sortedNums[n - 1]
        return max(p1, p2)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maximumProduct(nums: IntArray): Int {
        nums.sort()
        val n = nums.size
        val p1 = nums[n - 1] * nums[n - 2] * nums[n - 3]
        val p2 = nums[0] * nums[1] * nums[n - 1]
        return if (p1 > p2) p1 else p2
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maximumProduct(List<int> nums) {
    nums.sort();
    int n = nums.length;
    int p1 = nums[n - 1] * nums[n - 2] * nums[n - 3];
    int p2 = nums[0] * nums[1] * nums[n - 1];
    return p1 > p2 ? p1 : p2;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "sort"

func maximumProduct(nums []int) int {
    sort.Ints(nums)
    n := len(nums)
    p1 := nums[n-1] * nums[n-2] * nums[n-3]
    p2 := nums[0] * nums[1] * nums[n-1]
    if p1 > p2 {
        return p1
    }
    return p2
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def maximum_product(nums)
  s = nums.sort
  p1 = s[-1] * s[-2] * s[-3]
  p2 = s[0] * s[1] * s[-1]
  p1 > p2 ? p1 : p2
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maximumProduct(nums: Array[Int]): Int = {
        val s = nums.sorted
        val n = s.length
        val p1 = s(n-1) * s(n-2) * s(n-3)
        val p2 = s(0) * s(1) * s(n-1)
        if (p1 > p2) p1 else p2
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn maximum_product(nums: Vec<i32>) -> i32 {
        let mut nums = nums;
        nums.sort();
        let n = nums.len();
        let p1 = nums[n-1] * nums[n-2] * nums[n-3];
        let p2 = nums[0] * nums[1] * nums[n-1];
        if p1 > p2 { p1 } else { p2 }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (maximum-product nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([sorted (sort nums <)]
         [n (length sorted)]
         [a (list-ref sorted (- n 1))]
         [b (list-ref sorted (- n 2))]
         [c (list-ref sorted (- n 3))]
         [x (list-ref sorted 0)]
         [y (list-ref sorted 1)])
    (max (* a b c) (* x y a))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec maximum_product(Nums :: [integer()]) -> integer().
maximum_product(Nums) ->
  Sorted = lists:sort(Nums),
  N = length(Sorted),
  A = lists:nth(N, Sorted),
  B = lists:nth(N - 1, Sorted),
  C = lists:nth(N - 2, Sorted),
  X = lists:nth(1, Sorted),
  Y = lists:nth(2, Sorted),
  P1 = A * B * C,
  P2 = X * Y * A,
  if P1 > P2 -> P1; true -> P2 end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec maximum_product(nums :: [integer]) :: integer
  def maximum_product(nums) do
    sorted = Enum.sort(nums)
    n = length(sorted)
    a = Enum.at(sorted, n - 1)
    b = Enum.at(sorted, n - 2)
    c = Enum.at(sorted, n - 3)
    x = Enum.at(sorted, 0)
    y = Enum.at(sorted, 1)
    p1 = a * b * c
    p2 = x * y * a
    max(p1, p2)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n log n) where n is the length of the input array. This time complexity is dictated by the sorting of the array, while the subsequent comparison and product calculations are performed in O(1) time.
- **Space Complexity:** O(log n) or O(1) depending on the specific sorting algorithm used by the language's standard library. For example, some quicksort-based implementations use logarithmic auxiliary stack space for recursion.
