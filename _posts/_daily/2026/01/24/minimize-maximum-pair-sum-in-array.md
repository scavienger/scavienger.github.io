---
layout: post
title: "Minimize Maximum Pair Sum in Array"
date: 2026-01-24 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Two Pointers", "Greedy", "Sorting"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minPairSum(vector<int>& nums) {\n   \
        \     sort(nums.begin(), nums.end());\n        int n = nums.size();\n      \
        \  int maxPair = 0;\n        for (int i = 0; i < n / 2; ++i) {\n           \
        \ maxPair = max(maxPair, nums[i] + nums[n - 1 - i]);\n        }\n        return\
        \ maxPair;\n    }\n};"
      java: "class Solution {\n    public int minPairSum(int[] nums) {\n        java.util.Arrays.sort(nums);\n\
        \        int n = nums.length;\n        int maxPair = 0;\n        for (int i\
        \ = 0; i < n / 2; i++) {\n            maxPair = Math.max(maxPair, nums[i] +\
        \ nums[n - 1 - i]);\n        }\n        return maxPair;\n    }\n}"
      python: "class Solution(object):\n    def minPairSum(self, nums):\n        \"\"\
        \"\n        :type nums: List[int]\n        :rtype: int\n        \"\"\"\n   \
        \     nums.sort()\n        n = len(nums)\n        max_sum = 0\n        for i\
        \ in range(n // 2):\n            max_sum = max(max_sum, nums[i] + nums[n - 1\
        \ - i])\n        return max_sum"
      python3: "class Solution:\n    def minPairSum(self, nums: List[int]) -> int:\n\
        \        nums.sort()\n        n = len(nums)\n        max_sum = 0\n        for\
        \ i in range(n // 2):\n            current_sum = nums[i] + nums[n - 1 - i]\n\
        \            if current_sum > max_sum:\n                max_sum = current_sum\n\
        \        return max_sum"
      c: "int compare(const void *a, const void *b) {\n    return (*(int*)a - *(int*)b);\n\
        }\n\nint minPairSum(int* nums, int numsSize){\n    qsort(nums, numsSize, sizeof(int),\
        \ compare);\n    int maxPair = 0;\n    for (int i = 0; i < numsSize / 2; i++)\
        \ {\n        int currentSum = nums[i] + nums[numsSize - 1 - i];\n        if\
        \ (currentSum > maxPair) {\n            maxPair = currentSum;\n        }\n \
        \   }\n    return maxPair;\n}"
      csharp: "public class Solution {\n    public int MinPairSum(int[] nums) {\n  \
        \      Array.Sort(nums);\n        int n = nums.Length;\n        int maxPair\
        \ = 0;\n        for (int i = 0; i < n / 2; i++) {\n            int currentSum\
        \ = nums[i] + nums[n - 1 - i];\n            if (currentSum > maxPair) {\n  \
        \              maxPair = currentSum;\n            }\n        }\n        return\
        \ maxPair;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar minPairSum\
        \ = function(nums) {\n    nums.sort((a, b) => a - b);\n    let n = nums.length;\n\
        \    let maxPair = 0;\n    for (let i = 0; i < n / 2; i++) {\n        maxPair\
        \ = Math.max(maxPair, nums[i] + nums[n - 1 - i]);\n    }\n    return maxPair;\n\
        };"
      typescript: "function minPairSum(nums: number[]): number {\n    nums.sort((a,\
        \ b) => a - b);\n    let maxPairSum = 0;\n    const n = nums.length;\n    for\
        \ (let i = 0; i < n / 2; i++) {\n        const currentSum = nums[i] + nums[n\
        \ - 1 - i];\n        if (currentSum > maxPairSum) {\n            maxPairSum\
        \ = currentSum;\n        }\n    }\n    return maxPairSum;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function minPairSum($nums) {\n        sort($nums);\n\
        \        $maxSum = 0;\n        $n = count($nums);\n        for ($i = 0; $i <\
        \ $n / 2; $i++) {\n            $currentSum = $nums[$i] + $nums[$n - 1 - $i];\n\
        \            if ($currentSum > $maxSum) {\n                $maxSum = $currentSum;\n\
        \            }\n        }\n        return $maxSum;\n    }\n}"
      swift: "class Solution {\n    func minPairSum(_ nums: [Int]) -> Int {\n      \
        \  let sortedNums = nums.sorted()\n        var maxSum = 0\n        let n = sortedNums.count\n\
        \        for i in 0..<(n / 2) {\n            let currentSum = sortedNums[i]\
        \ + sortedNums[n - 1 - i]\n            if currentSum > maxSum {\n          \
        \      maxSum = currentSum\n            }\n        }\n        return maxSum\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun minPairSum(nums: IntArray): Int {\n       \
        \ nums.sort()\n        var maxSum = 0\n        val n = nums.size\n        for\
        \ (i in 0 until n / 2) {\n            val currentSum = nums[i] + nums[n - 1\
        \ - i]\n            if (currentSum > maxSum) {\n                maxSum = currentSum\n\
        \            }\n        }\n        return maxSum\n    }\n}"
      dart: "class Solution {\n  int minPairSum(List<int> nums) {\n    nums.sort();\n\
        \    int maxSum = 0;\n    int n = nums.length;\n    for (int i = 0; i < n ~/\
        \ 2; i++) {\n      int currentSum = nums[i] + nums[n - 1 - i];\n      if (currentSum\
        \ > maxSum) {\n        maxSum = currentSum;\n      }\n    }\n    return maxSum;\n\
        \  }\n}"
      go: "import \"sort\"\n\nfunc minPairSum(nums []int) int {\n    sort.Ints(nums)\n\
        \    maxSum := 0\n    n := len(nums)\n    for i := 0; i < n / 2; i++ {\n   \
        \     sum := nums[i] + nums[n - 1 - i]\n        if sum > maxSum {\n        \
        \    maxSum = sum\n        }\n    }\n    return maxSum\n}"
      ruby: '// Generation failed for Ruby

        // Reason: Generation failed: STOP'
      scala: '// Generation failed for Scala

        // Reason: Generation failed: STOP'
      rust: '// Generation failed for Rust

        // Reason: Generation failed: STOP'
      racket: '// Generation failed for Racket

        // Reason: Generation failed: STOP'
      erlang: '// Generation failed for Erlang

        // Reason: Generation failed: STOP'
      elixir: '// Generation failed for Elixir

        // Reason: Generation failed: STOP'
    approach: To minimize the maximum pair sum, the optimal strategy is to pair the
      smallest available element with the largest available element. By sorting the
      array in non-decreasing order, we can systematically pair elements from opposite
      ends of the sorted sequence. This greedy approach balances the pair sums, preventing
      any single pair from being unnecessarily large by offsetting the largest values
      with the smallest ones.
    time_complexity: O(n log n) where n is the length of the array. The dominant factor
      is sorting the input array. The subsequent linear scan to find the maximum sum
      among the pairs takes O(n) time.
    space_complexity: O(log n) or O(1) depending on the sorting implementation. In most
      modern languages, the sorting algorithm (like Quicksort or Timsort) uses O(log
      n) auxiliary space for the recursion stack or temporary storage.
    elapsed_time: 61.930036306381226
    model: gemini-3-pro-preview
    generated_at: '2026-01-24 06:59:45 '
---

## Problem #1877: Minimize Maximum Pair Sum in Array

**Difficulty:** Medium

**Topics:** Array, Two Pointers, Greedy, Sorting

## Problem Description

<p>The <strong>pair sum</strong> of a pair <code>(a,b)</code> is equal to <code>a + b</code>. The <strong>maximum pair sum</strong> is the largest <strong>pair sum</strong> in a list of pairs.</p>

<ul>
	<li>For example, if we have pairs <code>(1,5)</code>, <code>(2,3)</code>, and <code>(4,4)</code>, the <strong>maximum pair sum</strong> would be <code>max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8</code>.</li>
</ul>

<p>Given an array <code>nums</code> of <strong>even</strong> length <code>n</code>, pair up the elements of <code>nums</code> into <code>n / 2</code> pairs such that:</p>

<ul>
	<li>Each element of <code>nums</code> is in <strong>exactly one</strong> pair, and</li>
	<li>The <strong>maximum pair sum </strong>is <strong>minimized</strong>.</li>
</ul>

<p>Return <em>the minimized <strong>maximum pair sum</strong> after optimally pairing up the elements</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,5,2,3]
<strong>Output:</strong> 7
<strong>Explanation:</strong> The elements can be paired up into pairs (3,3) and (5,2).
The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,5,4,2,4,6]
<strong>Output:</strong> 8
<strong>Explanation:</strong> The elements can be paired up into pairs (3,5), (4,4), and (6,2).
The maximum pair sum is max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>n</code> is <strong>even</strong>.</li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

## Hints

1. Would sorting help find the optimal order?

2. Given a specific element, how would you minimize its specific pairwise sum?

## ✨ AI-Generated Solution (gemini-3-pro-preview)

### Approach

To minimize the maximum pair sum, the optimal strategy is to pair the smallest available element with the largest available element. By sorting the array in non-decreasing order, we can systematically pair elements from opposite ends of the sorted sequence. This greedy approach balances the pair sums, preventing any single pair from being unnecessarily large by offsetting the largest values with the smallest ones.

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
    int minPairSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int maxPair = 0;
        for (int i = 0; i < n / 2; ++i) {
            maxPair = max(maxPair, nums[i] + nums[n - 1 - i]);
        }
        return maxPair;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minPairSum(int[] nums) {
        java.util.Arrays.sort(nums);
        int n = nums.length;
        int maxPair = 0;
        for (int i = 0; i < n / 2; i++) {
            maxPair = Math.max(maxPair, nums[i] + nums[n - 1 - i]);
        }
        return maxPair;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        max_sum = 0
        for i in range(n // 2):
            max_sum = max(max_sum, nums[i] + nums[n - 1 - i])
        return max_sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        max_sum = 0
        for i in range(n // 2):
            current_sum = nums[i] + nums[n - 1 - i]
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int minPairSum(int* nums, int numsSize){
    qsort(nums, numsSize, sizeof(int), compare);
    int maxPair = 0;
    for (int i = 0; i < numsSize / 2; i++) {
        int currentSum = nums[i] + nums[numsSize - 1 - i];
        if (currentSum > maxPair) {
            maxPair = currentSum;
        }
    }
    return maxPair;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinPairSum(int[] nums) {
        Array.Sort(nums);
        int n = nums.Length;
        int maxPair = 0;
        for (int i = 0; i < n / 2; i++) {
            int currentSum = nums[i] + nums[n - 1 - i];
            if (currentSum > maxPair) {
                maxPair = currentSum;
            }
        }
        return maxPair;
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
var minPairSum = function(nums) {
    nums.sort((a, b) => a - b);
    let n = nums.length;
    let maxPair = 0;
    for (let i = 0; i < n / 2; i++) {
        maxPair = Math.max(maxPair, nums[i] + nums[n - 1 - i]);
    }
    return maxPair;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minPairSum(nums: number[]): number {
    nums.sort((a, b) => a - b);
    let maxPairSum = 0;
    const n = nums.length;
    for (let i = 0; i < n / 2; i++) {
        const currentSum = nums[i] + nums[n - 1 - i];
        if (currentSum > maxPairSum) {
            maxPairSum = currentSum;
        }
    }
    return maxPairSum;
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
    function minPairSum($nums) {
        sort($nums);
        $maxSum = 0;
        $n = count($nums);
        for ($i = 0; $i < $n / 2; $i++) {
            $currentSum = $nums[$i] + $nums[$n - 1 - $i];
            if ($currentSum > $maxSum) {
                $maxSum = $currentSum;
            }
        }
        return $maxSum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minPairSum(_ nums: [Int]) -> Int {
        let sortedNums = nums.sorted()
        var maxSum = 0
        let n = sortedNums.count
        for i in 0..<(n / 2) {
            let currentSum = sortedNums[i] + sortedNums[n - 1 - i]
            if currentSum > maxSum {
                maxSum = currentSum
            }
        }
        return maxSum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minPairSum(nums: IntArray): Int {
        nums.sort()
        var maxSum = 0
        val n = nums.size
        for (i in 0 until n / 2) {
            val currentSum = nums[i] + nums[n - 1 - i]
            if (currentSum > maxSum) {
                maxSum = currentSum
            }
        }
        return maxSum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minPairSum(List<int> nums) {
    nums.sort();
    int maxSum = 0;
    int n = nums.length;
    for (int i = 0; i < n ~/ 2; i++) {
      int currentSum = nums[i] + nums[n - 1 - i];
      if (currentSum > maxSum) {
        maxSum = currentSum;
      }
    }
    return maxSum;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "sort"

func minPairSum(nums []int) int {
    sort.Ints(nums)
    maxSum := 0
    n := len(nums)
    for i := 0; i < n / 2; i++ {
        sum := nums[i] + nums[n - 1 - i]
        if sum > maxSum {
            maxSum = sum
        }
    }
    return maxSum
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
// Generation failed for Ruby
// Reason: Generation failed: STOP
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
// Generation failed for Scala
// Reason: Generation failed: STOP
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
// Generation failed for Rust
// Reason: Generation failed: STOP
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
// Generation failed for Racket
// Reason: Generation failed: STOP
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
// Generation failed for Erlang
// Reason: Generation failed: STOP
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
// Generation failed for Elixir
// Reason: Generation failed: STOP
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n log n) where n is the length of the array. The dominant factor is sorting the input array. The subsequent linear scan to find the maximum sum among the pairs takes O(n) time.
- **Space Complexity:** O(log n) or O(1) depending on the sorting implementation. In most modern languages, the sorting algorithm (like Quicksort or Timsort) uses O(log n) auxiliary space for the recursion stack or temporary storage.
