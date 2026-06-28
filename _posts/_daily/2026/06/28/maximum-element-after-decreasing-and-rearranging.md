---
layout: post
title: "Maximum Element After Decreasing and Rearranging"
date: 2026-06-28 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Greedy", "Sorting"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <algorithm>\n\nusing namespace std;\n\nclass\
        \ Solution {\npublic:\n    int maximumElementAfterDecrementingAndRearranging(vector<int>&\
        \ arr) {\n        sort(arr.begin(), arr.end());\n        arr[0] = 1;\n     \
        \   for (int i = 1; i < arr.size(); ++i) {\n            if (arr[i] > arr[i -\
        \ 1] + 1) {\n                arr[i] = arr[i - 1] + 1;\n            }\n     \
        \   }\n        return arr.back();\n    }\n};"
      java: "import java.util.Arrays;\n\nclass Solution {\n    public int maximumElementAfterDecrementingAndRearranging(int[]\
        \ arr) {\n        Arrays.sort(arr);\n        arr[0] = 1;\n        for (int i\
        \ = 1; i < arr.length; i++) {\n            if (arr[i] > arr[i - 1] + 1) {\n\
        \                arr[i] = arr[i - 1] + 1;\n            }\n        }\n      \
        \  return arr[arr.length - 1];\n    }\n}"
      python: "class Solution(object):\n    def maximumElementAfterDecrementingAndRearranging(self,\
        \ arr):\n        \"\"\"\n        :type arr: List[int]\n        :rtype: int\n\
        \        \"\"\"\n        arr.sort()\n        arr[0] = 1\n        for i in range(1,\
        \ len(arr)):\n            if arr[i] > arr[i - 1] + 1:\n                arr[i]\
        \ = arr[i - 1] + 1\n        return arr[-1]"
      python3: "class Solution:\n    def maximumElementAfterDecrementingAndRearranging(self,\
        \ arr: List[int]) -> int:\n        arr.sort()\n        arr[0] = 1\n        for\
        \ i in range(1, len(arr)):\n            if arr[i] > arr[i - 1] + 1:\n      \
        \          arr[i] = arr[i - 1] + 1\n        return arr[-1]"
      c: "#include <stdlib.h>\n\nint compare(const void* a, const void* b) {\n    int\
        \ val1 = *(const int*)a;\n    int val2 = *(const int*)b;\n    if (val1 < val2)\
        \ return -1;\n    if (val1 > val2) return 1;\n    return 0;\n}\n\nint maximumElementAfterDecrementingAndRearranging(int*\
        \ arr, int arrSize) {\n    qsort(arr, arrSize, sizeof(int), compare);\n    arr[0]\
        \ = 1;\n    for (int i = 1; i < arrSize; i++) {\n        if (arr[i] > arr[i\
        \ - 1] + 1) {\n            arr[i] = arr[i - 1] + 1;\n        }\n    }\n    return\
        \ arr[arrSize - 1];\n}"
      csharp: "public class Solution {\n    public int MaximumElementAfterDecrementingAndRearranging(int[]\
        \ arr) {\n        System.Array.Sort(arr);\n        arr[0] = 1;\n        for\
        \ (int i = 1; i < arr.Length; i++) {\n            if (arr[i] > arr[i - 1] +\
        \ 1) {\n                arr[i] = arr[i - 1] + 1;\n            }\n        }\n\
        \        return arr[arr.Length - 1];\n    }\n}"
      javascript: "/**\n * @param {number[]} arr\n * @return {number}\n */\nvar maximumElementAfterDecrementingAndRearranging\
        \ = function(arr) {\n    arr.sort((a, b) => a - b);\n    arr[0] = 1;\n    for\
        \ (let i = 1; i < arr.length; i++) {\n        arr[i] = Math.min(arr[i], arr[i\
        \ - 1] + 1);\n    }\n    return arr[arr.length - 1];\n};"
      typescript: "function maximumElementAfterDecrementingAndRearranging(arr: number[]):\
        \ number {\n    arr.sort((a, b) => a - b);\n    arr[0] = 1;\n    for (let i\
        \ = 1; i < arr.length; i++) {\n        arr[i] = Math.min(arr[i], arr[i - 1]\
        \ + 1);\n    }\n    return arr[arr.length - 1];\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $arr\n     * @return\
        \ Integer\n     */\n    function maximumElementAfterDecrementingAndRearranging($arr)\
        \ {\n        sort($arr);\n        $arr[0] = 1;\n        $n = count($arr);\n\
        \        for ($i = 1; $i < $n; $i++) {\n            $arr[$i] = min($arr[$i],\
        \ $arr[$i - 1] + 1);\n        }\n        return $arr[$n - 1];\n    }\n}"
      swift: "class Solution {\n    func maximumElementAfterDecrementingAndRearranging(_\
        \ arr: [Int]) -> Int {\n        var sortedArr = arr.sorted()\n        sortedArr[0]\
        \ = 1\n        for i in 1..<sortedArr.count {\n            sortedArr[i] = min(sortedArr[i],\
        \ sortedArr[i - 1] + 1)\n        }\n        return sortedArr[sortedArr.count\
        \ - 1]\n    }\n}"
      kotlin: "class Solution {\n    fun maximumElementAfterDecrementingAndRearranging(arr:\
        \ IntArray): Int {\n        arr.sort()\n        var res = 1\n        for (i\
        \ in 1 until arr.size) {\n            if (arr[i] > res) {\n                res++\n\
        \            }\n        }\n        return res\n    }\n}"
      dart: "class Solution {\n  int maximumElementAfterDecrementingAndRearranging(List<int>\
        \ arr) {\n    arr.sort();\n    int res = 1;\n    for (int i = 1; i < arr.length;\
        \ i++) {\n      if (arr[i] > res) {\n        res++;\n      }\n    }\n    return\
        \ res;\n  }\n}"
      go: "import \"sort\"\n\nfunc maximumElementAfterDecrementingAndRearranging(arr\
        \ []int) int {\n    sort.Ints(arr)\n    res := 1\n    for i := 1; i < len(arr);\
        \ i++ {\n        if arr[i] > res {\n            res++\n        }\n    }\n  \
        \  return res\n}"
      ruby: "# @param {Integer[]} arr\n# @return {Integer}\ndef maximum_element_after_decrementing_and_rearranging(arr)\n\
        \    arr.sort!\n    res = 1\n    (1...arr.length).each do |i|\n        if arr[i]\
        \ > res\n            res += 1\n        end\n    end\n    res\nend"
      scala: "object Solution {\n    def maximumElementAfterDecrementingAndRearranging(arr:\
        \ Array[Int]): Int = {\n        val s = arr.sorted\n        var res = 1\n  \
        \      for (i <- 1 until s.length) {\n            if (s(i) > res) {\n      \
        \          res += 1\n            }\n        }\n        res\n    }\n}"
      rust: "impl Solution {\n    pub fn maximum_element_after_decrementing_and_rearranging(arr:\
        \ Vec<i32>) -> i32 {\n        let mut arr = arr;\n        arr.sort_unstable();\n\
        \        let mut ans = 1;\n        for i in 1..arr.len() {\n            ans\
        \ = std::cmp::min(arr[i], ans + 1);\n        }\n        ans\n    }\n}"
      racket: "(define/contract (maximum-element-after-decrementing-and-rearranging\
        \ arr)\n  (-> (listof exact-integer?) exact-integer?)\n  (let ([sorted-arr (sort\
        \ arr <)])\n    (foldl (lambda (x acc) (min x (+ acc 1)))\n           1\n  \
        \         (if (null? sorted-arr) '() (cdr sorted-arr)))))"
      erlang: "-spec maximum_element_after_decrementing_and_rearranging(Arr :: [integer()])\
        \ -> integer().\nmaximum_element_after_decrementing_and_rearranging(Arr) ->\n\
        \  Sorted = lists:sort(Arr),\n  lists:foldl(fun(X, Acc) -> min(X, Acc + 1) end,\
        \ 1, tl(Sorted))."
      elixir: "defmodule Solution do\n  @spec maximum_element_after_decrementing_and_rearranging(arr\
        \ :: [integer]) :: integer\n  def maximum_element_after_decrementing_and_rearranging(arr)\
        \ do\n    arr\n    |> Enum.sort()\n    |> tl()\n    |> Enum.reduce(1, fn x,\
        \ acc -> min(x, acc + 1) end)\n  end\nend"
    approach: 'To satisfy the problem constraints while maximizing the final value,
      we first sort the array to place elements in non-decreasing order. This allows
      us to greedily build up values such that each subsequent element is as large as
      possible relative to its predecessor. We initialize the first element to 1, fulfilling
      the first condition, and then iterate through the remaining elements.


      During the iteration, we ensure that each element is at most one greater than
      the element before it. If an element in the sorted array exceeds its predecessor
      by more than one, we decrease it to exactly one more than the preceding value.
      Since we are allowed to rearrange elements and decrease them to any smaller positive
      integer, this greedy approach ensures that every step maintains the maximum possible
      growth, leading to the largest possible value at the end of the array.'
    time_complexity: O(n log n) where n is the number of elements in the input array.
      This complexity is dominated by the sorting operation, while the subsequent linear
      pass to adjust the values according to the adjacency constraints takes O(n) time.
    space_complexity: O(log n) space complexity is generally required for the sorting
      algorithm's recursion stack (e.g., in introsort or Timsort). The adjustment phase
      is done in place, requiring only constant extra memory beyond the space used by
      the sort.
    elapsed_time: 408.7751798629761
    model: gemini-3-flash-preview
    generated_at: '2026-06-28 02:51:13 '
---

## Problem #1846: Maximum Element After Decreasing and Rearranging

**Difficulty:** Medium

**Topics:** Array, Greedy, Sorting

## Problem Description

<p>You are given an array of positive integers <code>arr</code>. Perform some operations (possibly none) on <code>arr</code> so that it satisfies these conditions:</p>

<ul>
	<li>The value of the <strong>first</strong> element in <code>arr</code> must be <code>1</code>.</li>
	<li>The absolute difference between any 2 adjacent elements must be <strong>less than or equal to </strong><code>1</code>. In other words, <code>abs(arr[i] - arr[i - 1]) &lt;= 1</code> for each <code>i</code> where <code>1 &lt;= i &lt; arr.length</code> (<strong>0-indexed</strong>). <code>abs(x)</code> is the absolute value of <code>x</code>.</li>
</ul>

<p>There are 2 types of operations that you can perform any number of times:</p>

<ul>
	<li><strong>Decrease</strong> the value of any element of <code>arr</code> to a <strong>smaller positive integer</strong>.</li>
	<li><strong>Rearrange</strong> the elements of <code>arr</code> to be in any order.</li>
</ul>

<p>Return <em>the <strong>maximum</strong> possible value of an element in </em><code>arr</code><em> after performing the operations to satisfy the conditions</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [2,2,1,2,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
We can satisfy the conditions by rearranging <code>arr</code> so it becomes <code>[1,2,2,2,1]</code>.
The largest element in <code>arr</code> is 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [100,1,1000]
<strong>Output:</strong> 3
<strong>Explanation:</strong> 
One possible way to satisfy the conditions is by doing the following:
1. Rearrange <code>arr</code> so it becomes <code>[1,100,1000]</code>.
2. Decrease the value of the second element to 2.
3. Decrease the value of the third element to 3.
Now <code>arr = [1,2,3]</code>, which<code> </code>satisfies the conditions.
The largest element in <code>arr is 3.</code>
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2,3,4,5]
<strong>Output:</strong> 5
<strong>Explanation:</strong> The array already satisfies the conditions, and the largest element is 5.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= arr[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. Sort the Array.

2. Decrement each element to the largest integer that satisfies the conditions.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To satisfy the problem constraints while maximizing the final value, we first sort the array to place elements in non-decreasing order. This allows us to greedily build up values such that each subsequent element is as large as possible relative to its predecessor. We initialize the first element to 1, fulfilling the first condition, and then iterate through the remaining elements.

During the iteration, we ensure that each element is at most one greater than the element before it. If an element in the sorted array exceeds its predecessor by more than one, we decrease it to exactly one more than the preceding value. Since we are allowed to rearrange elements and decrease them to any smaller positive integer, this greedy approach ensures that every step maintains the maximum possible growth, leading to the largest possible value at the end of the array.

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
    int maximumElementAfterDecrementingAndRearranging(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        arr[0] = 1;
        for (int i = 1; i < arr.size(); ++i) {
            if (arr[i] > arr[i - 1] + 1) {
                arr[i] = arr[i - 1] + 1;
            }
        }
        return arr.back();
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
    public int maximumElementAfterDecrementingAndRearranging(int[] arr) {
        Arrays.sort(arr);
        arr[0] = 1;
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > arr[i - 1] + 1) {
                arr[i] = arr[i - 1] + 1;
            }
        }
        return arr[arr.length - 1];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1] + 1:
                arr[i] = arr[i - 1] + 1
        return arr[-1]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1] + 1:
                arr[i] = arr[i - 1] + 1
        return arr[-1]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

int compare(const void* a, const void* b) {
    int val1 = *(const int*)a;
    int val2 = *(const int*)b;
    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}

int maximumElementAfterDecrementingAndRearranging(int* arr, int arrSize) {
    qsort(arr, arrSize, sizeof(int), compare);
    arr[0] = 1;
    for (int i = 1; i < arrSize; i++) {
        if (arr[i] > arr[i - 1] + 1) {
            arr[i] = arr[i - 1] + 1;
        }
    }
    return arr[arrSize - 1];
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaximumElementAfterDecrementingAndRearranging(int[] arr) {
        System.Array.Sort(arr);
        arr[0] = 1;
        for (int i = 1; i < arr.Length; i++) {
            if (arr[i] > arr[i - 1] + 1) {
                arr[i] = arr[i - 1] + 1;
            }
        }
        return arr[arr.Length - 1];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} arr
 * @return {number}
 */
var maximumElementAfterDecrementingAndRearranging = function(arr) {
    arr.sort((a, b) => a - b);
    arr[0] = 1;
    for (let i = 1; i < arr.length; i++) {
        arr[i] = Math.min(arr[i], arr[i - 1] + 1);
    }
    return arr[arr.length - 1];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maximumElementAfterDecrementingAndRearranging(arr: number[]): number {
    arr.sort((a, b) => a - b);
    arr[0] = 1;
    for (let i = 1; i < arr.length; i++) {
        arr[i] = Math.min(arr[i], arr[i - 1] + 1);
    }
    return arr[arr.length - 1];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function maximumElementAfterDecrementingAndRearranging($arr) {
        sort($arr);
        $arr[0] = 1;
        $n = count($arr);
        for ($i = 1; $i < $n; $i++) {
            $arr[$i] = min($arr[$i], $arr[$i - 1] + 1);
        }
        return $arr[$n - 1];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maximumElementAfterDecrementingAndRearranging(_ arr: [Int]) -> Int {
        var sortedArr = arr.sorted()
        sortedArr[0] = 1
        for i in 1..<sortedArr.count {
            sortedArr[i] = min(sortedArr[i], sortedArr[i - 1] + 1)
        }
        return sortedArr[sortedArr.count - 1]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maximumElementAfterDecrementingAndRearranging(arr: IntArray): Int {
        arr.sort()
        var res = 1
        for (i in 1 until arr.size) {
            if (arr[i] > res) {
                res++
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
  int maximumElementAfterDecrementingAndRearranging(List<int> arr) {
    arr.sort();
    int res = 1;
    for (int i = 1; i < arr.length; i++) {
      if (arr[i] > res) {
        res++;
      }
    }
    return res;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "sort"

func maximumElementAfterDecrementingAndRearranging(arr []int) int {
    sort.Ints(arr)
    res := 1
    for i := 1; i < len(arr); i++ {
        if arr[i] > res {
            res++
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
# @param {Integer[]} arr
# @return {Integer}
def maximum_element_after_decrementing_and_rearranging(arr)
    arr.sort!
    res = 1
    (1...arr.length).each do |i|
        if arr[i] > res
            res += 1
        end
    end
    res
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maximumElementAfterDecrementingAndRearranging(arr: Array[Int]): Int = {
        val s = arr.sorted
        var res = 1
        for (i <- 1 until s.length) {
            if (s(i) > res) {
                res += 1
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
    pub fn maximum_element_after_decrementing_and_rearranging(arr: Vec<i32>) -> i32 {
        let mut arr = arr;
        arr.sort_unstable();
        let mut ans = 1;
        for i in 1..arr.len() {
            ans = std::cmp::min(arr[i], ans + 1);
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
(define/contract (maximum-element-after-decrementing-and-rearranging arr)
  (-> (listof exact-integer?) exact-integer?)
  (let ([sorted-arr (sort arr <)])
    (foldl (lambda (x acc) (min x (+ acc 1)))
           1
           (if (null? sorted-arr) '() (cdr sorted-arr)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec maximum_element_after_decrementing_and_rearranging(Arr :: [integer()]) -> integer().
maximum_element_after_decrementing_and_rearranging(Arr) ->
  Sorted = lists:sort(Arr),
  lists:foldl(fun(X, Acc) -> min(X, Acc + 1) end, 1, tl(Sorted)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec maximum_element_after_decrementing_and_rearranging(arr :: [integer]) :: integer
  def maximum_element_after_decrementing_and_rearranging(arr) do
    arr
    |> Enum.sort()
    |> tl()
    |> Enum.reduce(1, fn x, acc -> min(x, acc + 1) end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n log n) where n is the number of elements in the input array. This complexity is dominated by the sorting operation, while the subsequent linear pass to adjust the values according to the adjacency constraints takes O(n) time.
- **Space Complexity:** O(log n) space complexity is generally required for the sorting algorithm's recursion stack (e.g., in introsort or Timsort). The adjustment phase is done in place, requiring only constant extra memory beyond the space used by the sort.
