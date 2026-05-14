---
layout: post
title: "Check if Array is Good"
date: 2026-05-14 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Hash Table", "Sorting"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/check-if-array-is-good/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool isGood(vector<int>& nums) {\n      \
        \  int n = nums.size() - 1;\n        if (n < 1) return false;\n        sort(nums.begin(),\
        \ nums.end());\n        for (int i = 0; i < n; i++) {\n            if (nums[i]\
        \ != i + 1) return false;\n        }\n        return nums[n] == n;\n    }\n\
        };"
      java: "import java.util.Arrays;\n\nclass Solution {\n    public boolean isGood(int[]\
        \ nums) {\n        int n = nums.length - 1;\n        if (n < 1) return false;\n\
        \        Arrays.sort(nums);\n        for (int i = 0; i < n; i++) {\n       \
        \     if (nums[i] != i + 1) return false;\n        }\n        return nums[n]\
        \ == n;\n    }\n}"
      python: "class Solution(object):\n    def isGood(self, nums):\n        \"\"\"\n\
        \        :type nums: List[int]\n        :rtype: bool\n        \"\"\"\n     \
        \   n = len(nums) - 1\n        if n < 1:\n            return False\n       \
        \ nums.sort()\n        for i in range(n):\n            if nums[i] != i + 1:\n\
        \                return False\n        return nums[n] == n"
      python3: "class Solution:\n    def isGood(self, nums: List[int]) -> bool:\n  \
        \      n = len(nums) - 1\n        if n < 1:\n            return False\n    \
        \    nums.sort()\n        for i in range(n):\n            if nums[i] != i +\
        \ 1:\n                return False\n        return nums[n] == n"
      c: "#include <stdbool.h>\n#include <stdlib.h>\n\nint compare(const void* a, const\
        \ void* b) {\n    return (*(int*)a - *(int*)b);\n}\n\nbool isGood(int* nums,\
        \ int numsSize) {\n    int n = numsSize - 1;\n    if (n < 1) return false;\n\
        \    qsort(nums, numsSize, sizeof(int), compare);\n    for (int i = 0; i < n;\
        \ i++) {\n        if (nums[i] != i + 1) return false;\n    }\n    return nums[n]\
        \ == n;\n}"
      csharp: "using System;\n\npublic class Solution {\n    public bool IsGood(int[]\
        \ nums) {\n        int n = nums.Length - 1;\n        if (n < 1) return false;\n\
        \        Array.Sort(nums);\n        for (int i = 0; i < n; i++) {\n        \
        \    if (nums[i] != i + 1) return false;\n        }\n        return nums[n]\
        \ == n;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {boolean}\n */\nvar isGood\
        \ = function(nums) {\n    let n = nums.length - 1;\n    if (n < 1) return false;\n\
        \    nums.sort((a, b) => a - b);\n    for (let i = 0; i < n; i++) {\n      \
        \  if (nums[i] !== i + 1) return false;\n    }\n    return nums[n] === n;\n\
        };"
      typescript: "function isGood(nums: number[]): boolean {\n    const n = nums.length\
        \ - 1;\n    if (n < 1) return false;\n    nums.sort((a, b) => a - b);\n    for\
        \ (let i = 0; i < n - 1; i++) {\n        if (nums[i] !== i + 1) return false;\n\
        \    }\n    return nums[n - 1] === n && nums[n] === n;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Boolean\n     */\n    function isGood($nums) {\n        $n = count($nums)\
        \ - 1;\n        if ($n < 1) return false;\n        sort($nums);\n        for\
        \ ($i = 0; $i < $n - 1; $i++) {\n            if ($nums[$i] !== ($i + 1)) return\
        \ false;\n        }\n        return $nums[$n - 1] === $n && $nums[$n] === $n;\n\
        \    }\n}"
      swift: "class Solution {\n    func isGood(_ nums: [Int]) -> Bool {\n        let\
        \ n = nums.count - 1\n        if n < 1 {\n            return false\n       \
        \ }\n        let sortedNums = nums.sorted()\n        for i in 0..<(n - 1) {\n\
        \            if sortedNums[i] != i + 1 {\n                return false\n   \
        \         }\n        }\n        return sortedNums[n - 1] == n && sortedNums[n]\
        \ == n\n    }\n}"
      kotlin: "class Solution {\n    fun isGood(nums: IntArray): Boolean {\n       \
        \ val n = nums.size - 1\n        if (n < 1) return false\n        nums.sort()\n\
        \        for (i in 0 until n - 1) {\n            if (nums[i] != i + 1) return\
        \ false\n        }\n        return nums[n - 1] == n && nums[n] == n\n    }\n\
        }"
      dart: "class Solution {\n  bool isGood(List<int> nums) {\n    int n = nums.length\
        \ - 1;\n    if (n < 1) return false;\n    nums.sort();\n    for (int i = 0;\
        \ i < n - 1; i++) {\n      if (nums[i] != i + 1) return false;\n    }\n    return\
        \ nums[n - 1] == n && nums[n] == n;\n  }\n}"
      go: "func isGood(nums []int) bool {\n    n := len(nums) - 1\n    if n < 1 {\n\
        \        return false\n    }\n    counts := make([]int, n+1)\n    for _, num\
        \ := range nums {\n        if num > n {\n            return false\n        }\n\
        \        counts[num]++\n    }\n    for i := 1; i < n; i++ {\n        if counts[i]\
        \ != 1 {\n            return false\n        }\n    }\n    return counts[n] ==\
        \ 2\n}"
      ruby: "def is_good(nums)\n  n = nums.max\n  nums.sort == (1..n).to_a + [n]\nend"
      scala: "object Solution {\n  def isGood(nums: Array[Int]): Boolean = {\n    if\
        \ (nums.isEmpty) return false\n    val n = nums.max\n    val sorted = nums.sorted\n\
        \    val expected = (1 to n).toArray :+ n\n    sorted.sameElements(expected)\n\
        \  }\n}"
      rust: "impl Solution {\n    pub fn is_good(nums: Vec<i32>) -> bool {\n       \
        \ if nums.is_empty() {\n            return false;\n        }\n        let n\
        \ = *nums.iter().max().unwrap();\n        if nums.len() as i32 != n + 1 {\n\
        \            return false;\n        }\n        let mut sorted_nums = nums;\n\
        \        sorted_nums.sort();\n        let mut expected: Vec<i32> = (1..=n).collect();\n\
        \        expected.push(n);\n        sorted_nums == expected\n    }\n}"
      racket: "(define/contract (is-good nums)\n  (-> (listof exact-integer?) boolean?)\n\
        \  (let* ([n (apply max nums)]\n         [sorted-nums (sort nums <)]\n     \
        \    [expected (append (range 1 (+ n 1)) (list n))])\n    (equal? sorted-nums\
        \ expected)))"
      erlang: "is_good(Nums) ->\n  Max = lists:max(Nums),\n  lists:sort(Nums) =:= lists:seq(1,\
        \ Max) ++ [Max]."
      elixir: "defmodule Solution do\n  @spec is_good(nums :: [integer]) :: boolean\n\
        \  def is_good(nums) do\n    max_val = Enum.max(nums)\n    Enum.sort(nums) ==\
        \ Enum.to_list(1..max_val) ++ [max_val]\n  end\nend"
    approach: 'The algorithm verifies if the given array is a permutation of the sequence
      [1, 2, ..., n-1, n, n]. Since the length of base[n] is always n + 1, we first
      determine the target value n as the length of the input array minus one. If the
      array length is less than 2, it is impossible for the array to be good as the
      smallest valid base array (base[1]) has a length of 2. This ensures we have a
      valid candidate for n.


      After determining n, we sort the array to easily check for the permutation property.
      In a valid sorted Good Array of length n + 1, the elements from index 0 up to
      index n - 1 must strictly follow the sequence 1, 2, ..., n (where index i contains
      value i + 1). Finally, the last element at index n must also be equal to n. This
      logic ensures that every integer from 1 to n - 1 appears exactly once, and the
      integer n appears exactly twice.'
    time_complexity: O(N log N), where N is the length of the input array. This is primarily
      due to the sorting step. The subsequent linear scan of the array to verify the
      values takes O(N) time. Given the maximum constraint of N = 100, this approach
      is extremely efficient.
    space_complexity: O(1) or O(N) depending on the language's sorting implementation.
      Many standard sorting algorithms use O(log N) auxiliary space for the recursion
      stack. In practice, for an array of size 100, the space overhead is minimal.
    elapsed_time: 378.964359998703
    model: gemini-3-flash-preview
    generated_at: '2026-05-14 02:37:29 '
---

## Problem #2784: Check if Array is Good

**Difficulty:** Easy

**Topics:** Array, Hash Table, Sorting

## Problem Description

<p>You are given an integer array <code>nums</code>. We consider an array <strong>good </strong>if it is a permutation of an array <code>base[n]</code>.</p>

<p><code>base[n] = [1, 2, ..., n - 1, n, n] </code>(in other words, it is an array of length <code>n + 1</code> which contains <code>1</code> to <code>n - 1 </code>exactly once, plus two occurrences of <code>n</code>). For example, <code>base[1] = [1, 1]</code> and<code> base[3] = [1, 2, 3, 3]</code>.</p>

<p>Return <code>true</code> <em>if the given array is good, otherwise return</em><em> </em><code>false</code>.</p>

<p><strong>Note: </strong>A permutation of integers represents an arrangement of these numbers.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2, 1, 3]
<strong>Output:</strong> false
<strong>Explanation:</strong> Since the maximum element of the array is 3, the only candidate n for which this array could be a permutation of base[n], is n = 3. However, base[3] has four elements but array nums has three. Therefore, it can not be a permutation of base[3] = [1, 2, 3, 3]. So the answer is false.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1, 3, 3, 2]
<strong>Output:</strong> true
<strong>Explanation:</strong> Since the maximum element of the array is 3, the only candidate n for which this array could be a permutation of base[n], is n = 3. It can be seen that nums is a permutation of base[3] = [1, 2, 3, 3] (by swapping the second and fourth elements in nums, we reach base[3]). Therefore, the answer is true.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1, 1]
<strong>Output:</strong> true
<strong>Explanation:</strong> Since the maximum element of the array is 1, the only candidate n for which this array could be a permutation of base[n], is n = 1. It can be seen that nums is a permutation of base[1] = [1, 1]. Therefore, the answer is true.</pre>

<p><strong class="example">Example 4:</strong></p>

<pre>
<strong>Input:</strong> nums = [3, 4, 4, 1, 2, 1]
<strong>Output:</strong> false
<strong>Explanation:</strong> Since the maximum element of the array is 4, the only candidate n for which this array could be a permutation of base[n], is n = 4. However, base[4] has five elements but array nums has six. Therefore, it can not be a permutation of base[4] = [1, 2, 3, 4, 4]. So the answer is false.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= num[i] &lt;= 200</code></li>
</ul>


## Hints

1. Find the maximum element of the array.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm verifies if the given array is a permutation of the sequence [1, 2, ..., n-1, n, n]. Since the length of base[n] is always n + 1, we first determine the target value n as the length of the input array minus one. If the array length is less than 2, it is impossible for the array to be good as the smallest valid base array (base[1]) has a length of 2. This ensures we have a valid candidate for n.

After determining n, we sort the array to easily check for the permutation property. In a valid sorted Good Array of length n + 1, the elements from index 0 up to index n - 1 must strictly follow the sequence 1, 2, ..., n (where index i contains value i + 1). Finally, the last element at index n must also be equal to n. This logic ensures that every integer from 1 to n - 1 appears exactly once, and the integer n appears exactly twice.

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
    bool isGood(vector<int>& nums) {
        int n = nums.size() - 1;
        if (n < 1) return false;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < n; i++) {
            if (nums[i] != i + 1) return false;
        }
        return nums[n] == n;
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
    public boolean isGood(int[] nums) {
        int n = nums.length - 1;
        if (n < 1) return false;
        Arrays.sort(nums);
        for (int i = 0; i < n; i++) {
            if (nums[i] != i + 1) return false;
        }
        return nums[n] == n;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums) - 1
        if n < 1:
            return False
        nums.sort()
        for i in range(n):
            if nums[i] != i + 1:
                return False
        return nums[n] == n
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        if n < 1:
            return False
        nums.sort()
        for i in range(n):
            if nums[i] != i + 1:
                return False
        return nums[n] == n
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdbool.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

bool isGood(int* nums, int numsSize) {
    int n = numsSize - 1;
    if (n < 1) return false;
    qsort(nums, numsSize, sizeof(int), compare);
    for (int i = 0; i < n; i++) {
        if (nums[i] != i + 1) return false;
    }
    return nums[n] == n;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public bool IsGood(int[] nums) {
        int n = nums.Length - 1;
        if (n < 1) return false;
        Array.Sort(nums);
        for (int i = 0; i < n; i++) {
            if (nums[i] != i + 1) return false;
        }
        return nums[n] == n;
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
 * @return {boolean}
 */
var isGood = function(nums) {
    let n = nums.length - 1;
    if (n < 1) return false;
    nums.sort((a, b) => a - b);
    for (let i = 0; i < n; i++) {
        if (nums[i] !== i + 1) return false;
    }
    return nums[n] === n;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function isGood(nums: number[]): boolean {
    const n = nums.length - 1;
    if (n < 1) return false;
    nums.sort((a, b) => a - b);
    for (let i = 0; i < n - 1; i++) {
        if (nums[i] !== i + 1) return false;
    }
    return nums[n - 1] === n && nums[n] === n;
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
     * @return Boolean
     */
    function isGood($nums) {
        $n = count($nums) - 1;
        if ($n < 1) return false;
        sort($nums);
        for ($i = 0; $i < $n - 1; $i++) {
            if ($nums[$i] !== ($i + 1)) return false;
        }
        return $nums[$n - 1] === $n && $nums[$n] === $n;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func isGood(_ nums: [Int]) -> Bool {
        let n = nums.count - 1
        if n < 1 {
            return false
        }
        let sortedNums = nums.sorted()
        for i in 0..<(n - 1) {
            if sortedNums[i] != i + 1 {
                return false
            }
        }
        return sortedNums[n - 1] == n && sortedNums[n] == n
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun isGood(nums: IntArray): Boolean {
        val n = nums.size - 1
        if (n < 1) return false
        nums.sort()
        for (i in 0 until n - 1) {
            if (nums[i] != i + 1) return false
        }
        return nums[n - 1] == n && nums[n] == n
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool isGood(List<int> nums) {
    int n = nums.length - 1;
    if (n < 1) return false;
    nums.sort();
    for (int i = 0; i < n - 1; i++) {
      if (nums[i] != i + 1) return false;
    }
    return nums[n - 1] == n && nums[n] == n;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func isGood(nums []int) bool {
    n := len(nums) - 1
    if n < 1 {
        return false
    }
    counts := make([]int, n+1)
    for _, num := range nums {
        if num > n {
            return false
        }
        counts[num]++
    }
    for i := 1; i < n; i++ {
        if counts[i] != 1 {
            return false
        }
    }
    return counts[n] == 2
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def is_good(nums)
  n = nums.max
  nums.sort == (1..n).to_a + [n]
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def isGood(nums: Array[Int]): Boolean = {
    if (nums.isEmpty) return false
    val n = nums.max
    val sorted = nums.sorted
    val expected = (1 to n).toArray :+ n
    sorted.sameElements(expected)
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn is_good(nums: Vec<i32>) -> bool {
        if nums.is_empty() {
            return false;
        }
        let n = *nums.iter().max().unwrap();
        if nums.len() as i32 != n + 1 {
            return false;
        }
        let mut sorted_nums = nums;
        sorted_nums.sort();
        let mut expected: Vec<i32> = (1..=n).collect();
        expected.push(n);
        sorted_nums == expected
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (is-good nums)
  (-> (listof exact-integer?) boolean?)
  (let* ([n (apply max nums)]
         [sorted-nums (sort nums <)]
         [expected (append (range 1 (+ n 1)) (list n))])
    (equal? sorted-nums expected)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
is_good(Nums) ->
  Max = lists:max(Nums),
  lists:sort(Nums) =:= lists:seq(1, Max) ++ [Max].
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec is_good(nums :: [integer]) :: boolean
  def is_good(nums) do
    max_val = Enum.max(nums)
    Enum.sort(nums) == Enum.to_list(1..max_val) ++ [max_val]
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N log N), where N is the length of the input array. This is primarily due to the sorting step. The subsequent linear scan of the array to verify the values takes O(N) time. Given the maximum constraint of N = 100, this approach is extremely efficient.
- **Space Complexity:** O(1) or O(N) depending on the language's sorting implementation. Many standard sorting algorithms use O(log N) auxiliary space for the recursion stack. In practice, for an array of size 100, the space overhead is minimal.
