---
layout: post
title: "Minimum Removals to Balance Array"
date: 2026-02-06 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Sliding Window", "Sorting"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-removals-to-balance-array/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minRemoval(vector<int>& nums, int k)\
        \ {\n        sort(nums.begin(), nums.end());\n        int n = nums.size();\n\
        \        int max_len = 0;\n        int j = 0;\n        for (int i = 0; i < n;\
        \ ++i) {\n            while (j < n && (long long)nums[j] <= (long long)nums[i]\
        \ * k) {\n                j++;\n            }\n            max_len = max(max_len,\
        \ j - i);\n        }\n        return n - max_len;\n    }\n};"
      java: "import java.util.Arrays;\n\nclass Solution {\n    public int minRemoval(int[]\
        \ nums, int k) {\n        Arrays.sort(nums);\n        int n = nums.length;\n\
        \        int maxLen = 0;\n        int j = 0;\n        for (int i = 0; i < n;\
        \ i++) {\n            while (j < n && (long)nums[j] <= (long)nums[i] * k) {\n\
        \                j++;\n            }\n            maxLen = Math.max(maxLen,\
        \ j - i);\n        }\n        return n - maxLen;\n    }\n}"
      python: "class Solution(object):\n    def minRemoval(self, nums, k):\n       \
        \ \"\"\"\n        :type nums: List[int]\n        :type k: int\n        :rtype:\
        \ int\n        \"\"\"\n        nums.sort()\n        n = len(nums)\n        max_len\
        \ = 0\n        j = 0\n        for i in range(n):\n            while j < n and\
        \ nums[j] <= nums[i] * k:\n                j += 1\n            if j - i > max_len:\n\
        \                max_len = j - i\n        return n - max_len"
      python3: "class Solution:\n    def minRemoval(self, nums: List[int], k: int) ->\
        \ int:\n        nums.sort()\n        n = len(nums)\n        max_len = 0\n  \
        \      j = 0\n        for i in range(n):\n            while j < n and nums[j]\
        \ <= nums[i] * k:\n                j += 1\n            if j - i > max_len:\n\
        \                max_len = j - i\n        return n - max_len"
      c: "#include <stdlib.h>\n\nint compare(const void* a, const void* b) {\n    int\
        \ arg1 = *(const int*)a;\n    int arg2 = *(const int*)b;\n    if (arg1 < arg2)\
        \ return -1;\n    if (arg1 > arg2) return 1;\n    return 0;\n}\n\nint minRemoval(int*\
        \ nums, int numsSize, int k) {\n    qsort(nums, numsSize, sizeof(int), compare);\n\
        \    int max_len = 0;\n    int j = 0;\n    for (int i = 0; i < numsSize; i++)\
        \ {\n        while (j < numsSize && (long long)nums[j] <= (long long)nums[i]\
        \ * k) {\n            j++;\n        }\n        if (j - i > max_len) {\n    \
        \        max_len = j - i;\n        }\n    }\n    return numsSize - max_len;\n\
        }"
      csharp: "using System;\n\npublic class Solution {\n    public int MinRemoval(int[]\
        \ nums, int k) {\n        Array.Sort(nums);\n        int n = nums.Length;\n\
        \        int maxLen = 0;\n        int j = 0;\n        for (int i = 0; i < n;\
        \ i++) {\n            while (j < n && (long)nums[j] <= (long)nums[i] * k) {\n\
        \                j++;\n            }\n            maxLen = Math.Max(maxLen,\
        \ j - i);\n        }\n        return n - maxLen;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} k\n * @return\
        \ {number}\n */\nvar minRemoval = function(nums, k) {\n    nums.sort((a, b)\
        \ => a - b);\n    let n = nums.length;\n    let maxLen = 0;\n    let j = 0;\n\
        \    for (let i = 0; i < n; i++) {\n        while (j < n && nums[j] <= k * nums[i])\
        \ {\n            j++;\n        }\n        maxLen = Math.max(maxLen, j - i);\n\
        \    }\n    return n - maxLen;\n};"
      typescript: "function minRemoval(nums: number[], k: number): number {\n    nums.sort((a,\
        \ b) => a - b);\n    const n = nums.length;\n    let maxLen = 0;\n    let i\
        \ = 0;\n    for (let j = 0; j < n; j++) {\n        while (nums[j] > nums[i]\
        \ * k) {\n            i++;\n        }\n        if (j - i + 1 > maxLen) {\n \
        \           maxLen = j - i + 1;\n        }\n    }\n    return n - maxLen;\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer $k\n     * @return Integer\n     */\n    function minRemoval($nums,\
        \ $k) {\n        sort($nums);\n        $n = count($nums);\n        $maxLen =\
        \ 0;\n        $i = 0;\n        for ($j = 0; $j < $n; $j++) {\n            while\
        \ ($nums[$j] > $nums[$i] * $k) {\n                $i++;\n            }\n   \
        \         $currentLen = $j - $i + 1;\n            if ($currentLen > $maxLen)\
        \ {\n                $maxLen = $currentLen;\n            }\n        }\n    \
        \    return $n - $maxLen;\n    }\n}"
      swift: "class Solution {\n    func minRemoval(_ nums: [Int], _ k: Int) -> Int\
        \ {\n        let sortedNums = nums.sorted()\n        let n = sortedNums.count\n\
        \        var maxLen = 0\n        var i = 0\n        for j in 0..<n {\n     \
        \       while sortedNums[j] > sortedNums[i] * k {\n                i += 1\n\
        \            }\n            let currentLen = j - i + 1\n            if currentLen\
        \ > maxLen {\n                maxLen = currentLen\n            }\n        }\n\
        \        return n - maxLen\n    }\n}"
      kotlin: "class Solution {\n    fun minRemoval(nums: IntArray, k: Int): Int {\n\
        \        nums.sort()\n        val n = nums.size\n        var maxLen = 0\n  \
        \      var i = 0\n        for (j in 0 until n) {\n            while (nums[j].toLong()\
        \ > nums[i].toLong() * k) {\n                i++\n            }\n          \
        \  val currentLen = j - i + 1\n            if (currentLen > maxLen) {\n    \
        \            maxLen = currentLen\n            }\n        }\n        return n\
        \ - maxLen\n    }\n}"
      dart: "class Solution {\n  int minRemoval(List<int> nums, int k) {\n    nums.sort();\n\
        \    int n = nums.length;\n    int maxLen = 0;\n    int i = 0;\n    for (int\
        \ j = 0; j < n; j++) {\n      while (nums[j] > nums[i] * k) {\n        i++;\n\
        \      }\n      int currentLen = j - i + 1;\n      if (currentLen > maxLen)\
        \ {\n        maxLen = currentLen;\n      }\n    }\n    return n - maxLen;\n\
        \  }\n}"
      go: "import \"sort\"\n\nfunc minRemoval(nums []int, k int) int {\n    sort.Ints(nums)\n\
        \    n := len(nums)\n    maxLen := 0\n    i := 0\n    for j := 0; j < n; j++\
        \ {\n        for int64(nums[j]) > int64(nums[i])*int64(k) {\n            i++\n\
        \        }\n        if j - i + 1 > maxLen {\n            maxLen = j - i + 1\n\
        \        }\n    }\n    return n - maxLen\n}"
      ruby: "def min_removal(nums, k)\n  nums.sort!\n  n = nums.length\n  max_len =\
        \ 0\n  i = 0\n  nums.each_with_index do |num, j|\n    while nums[i] * k < num\n\
        \      i += 1\n    end\n    current_len = j - i + 1\n    max_len = current_len\
        \ if current_len > max_len\n  end\n  n - max_len\nend"
      scala: "object Solution {\n    def minRemoval(nums: Array[Int], k: Int): Int =\
        \ {\n        val n = nums.length\n        java.util.Arrays.sort(nums)\n    \
        \    var maxLen = 0\n        var i = 0\n        for (j <- 0 until n) {\n   \
        \         while (nums(i).toLong * k < nums(j).toLong) {\n                i +=\
        \ 1\n            }\n            if (j - i + 1 > maxLen) {\n                maxLen\
        \ = j - i + 1\n            }\n        }\n        n - maxLen\n    }\n}"
      rust: "impl Solution {\n    pub fn min_removal(nums: Vec<i32>, k: i32) -> i32\
        \ {\n        let mut nums = nums;\n        nums.sort_unstable();\n        let\
        \ n = nums.len();\n        let mut max_len = 0;\n        let mut i = 0;\n  \
        \      for j in 0..n {\n            while (nums[i] as i64) * (k as i64) < (nums[j]\
        \ as i64) {\n                i += 1;\n            }\n            let current_len\
        \ = j - i + 1;\n            if current_len > max_len {\n                max_len\
        \ = current_len;\n            }\n        }\n        (n - max_len) as i32\n \
        \   }\n}"
      racket: "(define/contract (min-removal nums k)\n  (-> (listof exact-integer?)\
        \ exact-integer? exact-integer?)\n  (let* ([sorted-nums (sort nums <)]\n   \
        \      [arr (list->vector sorted-nums)]\n         [n (vector-length arr)])\n\
        \    (let loop ([i 0] [j 0] [max-len 0])\n      (if (= j n)\n          (- n\
        \ max-len)\n          (if (> (vector-ref arr j) (* (vector-ref arr i) k))\n\
        \              (loop (+ i 1) j max-len)\n              (let ([current-len (+\
        \ (- j i) 1)])\n                (loop i (+ j 1) (if (> current-len max-len)\
        \ current-len max-len))))))))"
      erlang: "min_removal(Nums, K) ->\n  Sorted = lists:sort(Nums),\n  Arr = list_to_tuple(Sorted),\n\
        \  N = tuple_size(Arr),\n  loop(1, 1, 0, N, Arr, K).\n\nloop(I, J, MaxLen, N,\
        \ Arr, K) when J > N ->\n  N - MaxLen;\nloop(I, J, MaxLen, N, Arr, K) ->\n \
        \ ValI = element(I, Arr),\n  ValJ = element(J, Arr),\n  if\n    ValJ > ValI\
        \ * K ->\n      loop(I + 1, J, MaxLen, N, Arr, K);\n    true ->\n      NewMaxLen\
        \ = erlang:max(MaxLen, J - I + 1),\n      loop(I, J + 1, NewMaxLen, N, Arr,\
        \ K)\n  end."
      elixir: "defmodule Solution do\n  @spec min_removal(nums :: [integer], k :: integer)\
        \ :: integer\n  def min_removal(nums, k) do\n    sorted = Enum.sort(nums)\n\
        \    arr = List.to_tuple(sorted)\n    n = tuple_size(arr)\n    loop(0, 0, 0,\
        \ n, arr, k)\n  end\n\n  defp loop(i, j, max_len, n, arr, k) when j < n do\n\
        \    val_i = elem(arr, i)\n    val_j = elem(arr, j)\n    if val_j > val_i *\
        \ k do\n      loop(i + 1, j, max_len, n, arr, k)\n    else\n      new_max_len\
        \ = max(max_len, j - i + 1)\n      loop(i, j + 1, new_max_len, n, arr, k)\n\
        \    end\n  end\n\n  defp loop(_i, _j, max_len, n, _arr, _k) do\n    n - max_len\n\
        \  end\nend"
    approach: 'The problem asks for the minimum number of removals to satisfy the condition
      that the maximum element is at most $k$ times the minimum element. Sorting the
      array is the most effective first step because it transforms the problem into
      finding the longest contiguous subarray $[i, j]$ where $nums[j] \le k \times nums[i]$.
      In a sorted array, for any fixed minimum element $nums[i]$, all elements between
      index $i$ and $j$ are naturally within the range $[nums[i], nums[j]]$. This allows
      us to use the two-pointer or sliding window technique to find the maximum possible
      length of such a balanced subarray.


      We initialize two pointers, $i$ and $j$, both starting at the beginning of the
      sorted array. As $i$ iterates through each element (treating it as the minimum),
      we advance $j$ as far as possible until the balance condition is violated. Because
      both $nums[i]$ and the threshold $k \times nums[i]$ increase monotonically as
      $i$ moves forward, $j$ never needs to backtrack. The maximum window size $j -
      i$ encountered during this traversal represents the largest balanced subset. Subtracting
      this value from the total array length yields the minimum number of elements to
      remove.'
    time_complexity: O(N \log N) where $N$ is the number of elements in the array. This
      complexity is dominated by the sorting step. The two-pointer sliding window traversal
      that follows sorting takes $O(N)$ time because each pointer $i$ and $j$ moves
      through the array at most once.
    space_complexity: O(N) in the worst case. While the sliding window itself uses only
      $O(1)$ extra space, the sorting algorithms in many languages (like Python's Timsort)
      utilize $O(N)$ auxiliary space, while others like C++'s std::sort typically use
      $O(\log N)$.
    elapsed_time: 196.82390189170837
    model: gemini-3-flash-preview
    generated_at: '2026-02-06 01:24:47 '
---

## Problem #3634: Minimum Removals to Balance Array

**Difficulty:** Medium

**Topics:** Array, Sliding Window, Sorting

## Problem Description

<p>You are given an integer array <code>nums</code> and an integer <code>k</code>.</p>

<p>An array is considered <strong>balanced</strong> if the value of its <strong>maximum</strong> element is <strong>at most</strong> <code>k</code> times the <strong>minimum</strong> element.</p>

<p>You may remove <strong>any</strong> number of elements from <code>nums</code>​​​​​​​ without making it <strong>empty</strong>.</p>

<p>Return the <strong>minimum</strong> number of elements to remove so that the remaining array is balanced.</p>

<p><strong>Note:</strong> An array of size 1 is considered balanced as its maximum and minimum are equal, and the condition always holds true.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,1,5], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Remove <code>nums[2] = 5</code> to get <code>nums = [2, 1]</code>.</li>
	<li>Now <code>max = 2</code>, <code>min = 1</code> and <code>max &lt;= min * k</code> as <code>2 &lt;= 1 * 2</code>. Thus, the answer is 1.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,6,2,9], k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Remove <code>nums[0] = 1</code> and <code>nums[3] = 9</code> to get <code>nums = [6, 2]</code>.</li>
	<li>Now <code>max = 6</code>, <code>min = 2</code> and <code>max &lt;= min * k</code> as <code>6 &lt;= 2 * 3</code>. Thus, the answer is 2.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,6], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Since <code>nums</code> is already balanced as <code>6 &lt;= 4 * 2</code>, no elements need to be removed.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. Sort `nums` and use two pointers `i` and `j` so that the window's minimum is `nums[i]` and maximum is `nums[j]`.

2. Expand `j` while `nums[j] <= k * nums[i]` to maximize the balanced window; answer = `n - (j - i + 1)`.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the minimum number of removals to satisfy the condition that the maximum element is at most $k$ times the minimum element. Sorting the array is the most effective first step because it transforms the problem into finding the longest contiguous subarray $[i, j]$ where $nums[j] \le k \times nums[i]$. In a sorted array, for any fixed minimum element $nums[i]$, all elements between index $i$ and $j$ are naturally within the range $[nums[i], nums[j]]$. This allows us to use the two-pointer or sliding window technique to find the maximum possible length of such a balanced subarray.

We initialize two pointers, $i$ and $j$, both starting at the beginning of the sorted array. As $i$ iterates through each element (treating it as the minimum), we advance $j$ as far as possible until the balance condition is violated. Because both $nums[i]$ and the threshold $k \times nums[i]$ increase monotonically as $i$ moves forward, $j$ never needs to backtrack. The maximum window size $j - i$ encountered during this traversal represents the largest balanced subset. Subtracting this value from the total array length yields the minimum number of elements to remove.

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
    int minRemoval(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int max_len = 0;
        int j = 0;
        for (int i = 0; i < n; ++i) {
            while (j < n && (long long)nums[j] <= (long long)nums[i] * k) {
                j++;
            }
            max_len = max(max_len, j - i);
        }
        return n - max_len;
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
    public int minRemoval(int[] nums, int k) {
        Arrays.sort(nums);
        int n = nums.length;
        int maxLen = 0;
        int j = 0;
        for (int i = 0; i < n; i++) {
            while (j < n && (long)nums[j] <= (long)nums[i] * k) {
                j++;
            }
            maxLen = Math.max(maxLen, j - i);
        }
        return n - maxLen;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minRemoval(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        max_len = 0
        j = 0
        for i in range(n):
            while j < n and nums[j] <= nums[i] * k:
                j += 1
            if j - i > max_len:
                max_len = j - i
        return n - max_len
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        max_len = 0
        j = 0
        for i in range(n):
            while j < n and nums[j] <= nums[i] * k:
                j += 1
            if j - i > max_len:
                max_len = j - i
        return n - max_len
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

int minRemoval(int* nums, int numsSize, int k) {
    qsort(nums, numsSize, sizeof(int), compare);
    int max_len = 0;
    int j = 0;
    for (int i = 0; i < numsSize; i++) {
        while (j < numsSize && (long long)nums[j] <= (long long)nums[i] * k) {
            j++;
        }
        if (j - i > max_len) {
            max_len = j - i;
        }
    }
    return numsSize - max_len;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public int MinRemoval(int[] nums, int k) {
        Array.Sort(nums);
        int n = nums.Length;
        int maxLen = 0;
        int j = 0;
        for (int i = 0; i < n; i++) {
            while (j < n && (long)nums[j] <= (long)nums[i] * k) {
                j++;
            }
            maxLen = Math.Max(maxLen, j - i);
        }
        return n - maxLen;
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
var minRemoval = function(nums, k) {
    nums.sort((a, b) => a - b);
    let n = nums.length;
    let maxLen = 0;
    let j = 0;
    for (let i = 0; i < n; i++) {
        while (j < n && nums[j] <= k * nums[i]) {
            j++;
        }
        maxLen = Math.max(maxLen, j - i);
    }
    return n - maxLen;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minRemoval(nums: number[], k: number): number {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    let maxLen = 0;
    let i = 0;
    for (let j = 0; j < n; j++) {
        while (nums[j] > nums[i] * k) {
            i++;
        }
        if (j - i + 1 > maxLen) {
            maxLen = j - i + 1;
        }
    }
    return n - maxLen;
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
    function minRemoval($nums, $k) {
        sort($nums);
        $n = count($nums);
        $maxLen = 0;
        $i = 0;
        for ($j = 0; $j < $n; $j++) {
            while ($nums[$j] > $nums[$i] * $k) {
                $i++;
            }
            $currentLen = $j - $i + 1;
            if ($currentLen > $maxLen) {
                $maxLen = $currentLen;
            }
        }
        return $n - $maxLen;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minRemoval(_ nums: [Int], _ k: Int) -> Int {
        let sortedNums = nums.sorted()
        let n = sortedNums.count
        var maxLen = 0
        var i = 0
        for j in 0..<n {
            while sortedNums[j] > sortedNums[i] * k {
                i += 1
            }
            let currentLen = j - i + 1
            if currentLen > maxLen {
                maxLen = currentLen
            }
        }
        return n - maxLen
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minRemoval(nums: IntArray, k: Int): Int {
        nums.sort()
        val n = nums.size
        var maxLen = 0
        var i = 0
        for (j in 0 until n) {
            while (nums[j].toLong() > nums[i].toLong() * k) {
                i++
            }
            val currentLen = j - i + 1
            if (currentLen > maxLen) {
                maxLen = currentLen
            }
        }
        return n - maxLen
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minRemoval(List<int> nums, int k) {
    nums.sort();
    int n = nums.length;
    int maxLen = 0;
    int i = 0;
    for (int j = 0; j < n; j++) {
      while (nums[j] > nums[i] * k) {
        i++;
      }
      int currentLen = j - i + 1;
      if (currentLen > maxLen) {
        maxLen = currentLen;
      }
    }
    return n - maxLen;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "sort"

func minRemoval(nums []int, k int) int {
    sort.Ints(nums)
    n := len(nums)
    maxLen := 0
    i := 0
    for j := 0; j < n; j++ {
        for int64(nums[j]) > int64(nums[i])*int64(k) {
            i++
        }
        if j - i + 1 > maxLen {
            maxLen = j - i + 1
        }
    }
    return n - maxLen
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def min_removal(nums, k)
  nums.sort!
  n = nums.length
  max_len = 0
  i = 0
  nums.each_with_index do |num, j|
    while nums[i] * k < num
      i += 1
    end
    current_len = j - i + 1
    max_len = current_len if current_len > max_len
  end
  n - max_len
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minRemoval(nums: Array[Int], k: Int): Int = {
        val n = nums.length
        java.util.Arrays.sort(nums)
        var maxLen = 0
        var i = 0
        for (j <- 0 until n) {
            while (nums(i).toLong * k < nums(j).toLong) {
                i += 1
            }
            if (j - i + 1 > maxLen) {
                maxLen = j - i + 1
            }
        }
        n - maxLen
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_removal(nums: Vec<i32>, k: i32) -> i32 {
        let mut nums = nums;
        nums.sort_unstable();
        let n = nums.len();
        let mut max_len = 0;
        let mut i = 0;
        for j in 0..n {
            while (nums[i] as i64) * (k as i64) < (nums[j] as i64) {
                i += 1;
            }
            let current_len = j - i + 1;
            if current_len > max_len {
                max_len = current_len;
            }
        }
        (n - max_len) as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-removal nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([sorted-nums (sort nums <)]
         [arr (list->vector sorted-nums)]
         [n (vector-length arr)])
    (let loop ([i 0] [j 0] [max-len 0])
      (if (= j n)
          (- n max-len)
          (if (> (vector-ref arr j) (* (vector-ref arr i) k))
              (loop (+ i 1) j max-len)
              (let ([current-len (+ (- j i) 1)])
                (loop i (+ j 1) (if (> current-len max-len) current-len max-len))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
min_removal(Nums, K) ->
  Sorted = lists:sort(Nums),
  Arr = list_to_tuple(Sorted),
  N = tuple_size(Arr),
  loop(1, 1, 0, N, Arr, K).

loop(I, J, MaxLen, N, Arr, K) when J > N ->
  N - MaxLen;
loop(I, J, MaxLen, N, Arr, K) ->
  ValI = element(I, Arr),
  ValJ = element(J, Arr),
  if
    ValJ > ValI * K ->
      loop(I + 1, J, MaxLen, N, Arr, K);
    true ->
      NewMaxLen = erlang:max(MaxLen, J - I + 1),
      loop(I, J + 1, NewMaxLen, N, Arr, K)
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_removal(nums :: [integer], k :: integer) :: integer
  def min_removal(nums, k) do
    sorted = Enum.sort(nums)
    arr = List.to_tuple(sorted)
    n = tuple_size(arr)
    loop(0, 0, 0, n, arr, k)
  end

  defp loop(i, j, max_len, n, arr, k) when j < n do
    val_i = elem(arr, i)
    val_j = elem(arr, j)
    if val_j > val_i * k do
      loop(i + 1, j, max_len, n, arr, k)
    else
      new_max_len = max(max_len, j - i + 1)
      loop(i, j + 1, new_max_len, n, arr, k)
    end
  end

  defp loop(_i, _j, max_len, n, _arr, _k) do
    n - max_len
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N \log N) where $N$ is the number of elements in the array. This complexity is dominated by the sorting step. The two-pointer sliding window traversal that follows sorting takes $O(N)$ time because each pointer $i$ and $j$ moves through the array at most once.
- **Space Complexity:** O(N) in the worst case. While the sliding window itself uses only $O(1)$ extra space, the sorting algorithms in many languages (like Python's Timsort) utilize $O(N)$ auxiliary space, while others like C++'s std::sort typically use $O(\log N)$.
