---
layout: post
title: "Maximize Consecutive Elements in an Array After Modification"
date: 2026-11-20 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Dynamic Programming", "Sorting"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/
ai_solutions:
  - solutions:
      cpp: '// Generation failed for C++

        // Reason: Parsing failed'
      java: '// Generation failed for Java

        // Reason: Parsing failed'
      python: '// Generation failed for Python

        // Reason: Parsing failed'
      python3: "class Solution:\n    def maxSelectedElements(self, nums: List[int])\
        \ -> int:\n        nums.sort()\n        dp = {}\n        for x in nums:\n  \
        \          dp[x + 1] = dp.get(x, 0) + 1\n            dp[x] = dp.get(x - 1, 0)\
        \ + 1\n        return max(dp.values())"
      c: "static int compare(const void* a, const void* b) {\n    return (*(int*)a -\
        \ *(int*)b);\n}\n\nint maxSelectedElements(int* nums, int numsSize) {\n    qsort(nums,\
        \ numsSize, sizeof(int), compare);\n    int maxVal = nums[numsSize - 1];\n \
        \   int* dp = (int*)calloc(maxVal + 2, sizeof(int));\n    int ans = 0;\n\n \
        \   for (int i = 0; i < numsSize; i++) {\n        int x = nums[i];\n       \
        \ dp[x + 1] = dp[x] + 1;\n        dp[x] = dp[x - 1] + 1;\n        if (dp[x +\
        \ 1] > ans) ans = dp[x + 1];\n        if (dp[x] > ans) ans = dp[x];\n    }\n\
        \n    free(dp);\n    return ans;\n}"
      csharp: "public class Solution {\n    public int MaxSelectedElements(int[] nums)\
        \ {\n        Array.Sort(nums);\n        int maxVal = nums[nums.Length - 1];\n\
        \        int[] dp = new int[maxVal + 2];\n        int ans = 0;\n\n        foreach\
        \ (int x in nums) {\n            dp[x + 1] = dp[x] + 1;\n            dp[x] =\
        \ dp[x - 1] + 1;\n            if (dp[x + 1] > ans) ans = dp[x + 1];\n      \
        \      if (dp[x] > ans) ans = dp[x];\n        }\n\n        return ans;\n   \
        \ }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar maxSelectedElements\
        \ = function(nums) {\n    nums.sort((a, b) => a - b);\n    const dp = new Map();\n\
        \    let ans = 0;\n\n    for (const x of nums) {\n        const nextLen = (dp.get(x)\
        \ || 0) + 1;\n        const currLen = (dp.get(x - 1) || 0) + 1;\n        dp.set(x\
        \ + 1, nextLen);\n        dp.set(x, currLen);\n        if (nextLen > ans) ans\
        \ = nextLen;\n        if (currLen > ans) ans = currLen;\n    }\n\n    return\
        \ ans;\n};"
      typescript: "function maxSelectedElements(nums: number[]): number {\n    nums.sort((a,\
        \ b) => a - b);\n    const dp = new Map<number, number>();\n    let ans = 0;\n\
        \    for (const x of nums) {\n        const next = (dp.get(x) ?? 0) + 1;\n \
        \       const curr = (dp.get(x - 1) ?? 0) + 1;\n        dp.set(x + 1, next);\n\
        \        dp.set(x, curr);\n        if (next > ans) ans = next;\n        if (curr\
        \ > ans) ans = curr;\n    }\n    return ans;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function maxSelectedElements($nums) {\n        sort($nums);\n\
        \        $dp = [];\n        $ans = 0;\n        foreach ($nums as $x) {\n   \
        \         $next = ($dp[$x] ?? 0) + 1;\n            $curr = ($dp[$x - 1] ?? 0)\
        \ + 1;\n            $dp[$x + 1] = $next;\n            $dp[$x] = $curr;\n   \
        \         if ($next > $ans) $ans = $next;\n            if ($curr > $ans) $ans\
        \ = $curr;\n        }\n        return $ans;\n    }\n}"
      swift: "class Solution {\n    func maxSelectedElements(_ nums: [Int]) -> Int {\n\
        \        let sortedNums = nums.sorted()\n        var dp = [Int: Int](minimumCapacity:\
        \ nums.count * 2)\n        var ans = 0\n        for x in sortedNums {\n    \
        \        let next = (dp[x] ?? 0) + 1\n            let curr = (dp[x - 1] ?? 0)\
        \ + 1\n            dp[x + 1] = next\n            dp[x] = curr\n            if\
        \ next > ans { ans = next }\n            if curr > ans { ans = curr }\n    \
        \    }\n        return ans\n    }\n}"
      kotlin: "class Solution {\n    fun maxSelectedElements(nums: IntArray): Int {\n\
        \        nums.sort()\n        val dp = HashMap<Int, Int>(nums.size * 2)\n  \
        \      var ans = 0\n        for (x in nums) {\n            val next = (dp[x]\
        \ ?: 0) + 1\n            val curr = (dp[x - 1] ?: 0) + 1\n            dp[x +\
        \ 1] = next\n            dp[x] = curr\n            if (next > ans) ans = next\n\
        \            if (curr > ans) ans = curr\n        }\n        return ans\n   \
        \ }\n}"
      dart: "class Solution {\n  int maxSelectedElements(List<int> nums) {\n    nums.sort();\n\
        \    final dp = <int, int>{};\n    int ans = 0;\n    for (final x in nums) {\n\
        \      final v1 = (dp[x] ?? 0) + 1;\n      final v2 = (dp[x - 1] ?? 0) + 1;\n\
        \      dp[x + 1] = v1;\n      dp[x] = v2;\n      if (v1 > ans) ans = v1;\n \
        \     if (v2 > ans) ans = v2;\n    }\n    return ans;\n  }\n}"
      go: "func maxSelectedElements(nums []int) int {\n    sort.Ints(nums)\n    dp :=\
        \ make(map[int]int)\n    ans := 0\n    for _, x := range nums {\n        dp[x+1]\
        \ = dp[x] + 1\n        dp[x] = dp[x-1] + 1\n        if dp[x+1] > ans {\n   \
        \         ans = dp[x+1]\n        }\n        if dp[x] > ans {\n            ans\
        \ = dp[x]\n        }\n    }\n    return ans\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef max_selected_elements(nums)\n\
        \  nums.sort!\n  dp = Hash.new(0)\n  ans = 0\n  nums.each do |x|\n    v1 = dp[x]\
        \ + 1\n    v2 = dp[x - 1] + 1\n    dp[x + 1] = v1\n    dp[x] = v2\n    ans =\
        \ v1 if v1 > ans\n    ans = v2 if v2 > ans\n  end\n  ans\nend"
      scala: "object Solution {\n    def maxSelectedElements(nums: Array[Int]): Int\
        \ = {\n        scala.util.Sorting.quickSort(nums)\n        val dp = new scala.collection.mutable.HashMap[Int,\
        \ Int]()\n        var ans = 0\n        for (x <- nums) {\n            val v1\
        \ = dp.getOrElse(x, 0) + 1\n            val v2 = dp.getOrElse(x - 1, 0) + 1\n\
        \            dp(x + 1) = v1\n            dp(x) = v2\n            if (v1 > ans)\
        \ ans = v1\n            if (v2 > ans) ans = v2\n        }\n        ans\n   \
        \ }\n}"
      rust: '// Generation failed for Rust

        // Reason: Parsing failed'
      racket: '// Generation failed for Racket

        // Reason: Parsing failed'
      erlang: '// Generation failed for Erlang

        // Reason: Parsing failed'
      elixir: '// Generation failed for Elixir

        // Reason: Parsing failed'
    approach: 'To maximize the number of consecutive elements, we first sort the array
      in non-decreasing order. Each element $x$ can either be kept as $x$ or incremented
      to $x + 1$. By processing the sorted numbers sequentially, an element $x$ can
      extend a consecutive sequence ending at $x$ (by transforming into $x + 1$) or
      a consecutive sequence ending at $x - 1$ (by remaining $x$). We can define a dynamic
      programming state where $dp[v]$ represents the maximum length of a consecutive
      sequence ending with value $v$.


      When considering each number $x$ in sorted order, we update the DP states in the
      order of $dp[x + 1] = dp[x] + 1$ followed by $dp[x] = dp[x - 1] + 1$. Updating
      $dp[x + 1]$ first is crucial so that it uses the state $dp[x]$ computed from prior
      elements, preventing the current element from being counted twice (once as $x$
      and once as $x + 1$). The final answer is the maximum value achieved across all
      DP states.'
    time_complexity: O(n \log n) where $n$ is the length of the array, dominated by
      the sorting step. The subsequent dynamic programming traversal processes each
      element in $O(1)$ time.
    space_complexity: O(n) auxiliary space to store the dynamic programming states (or
      $O(\max(nums))$ when using a direct array), plus $O(n)$ space for sorting depending
      on the language runtime.
    elapsed_time: 165.4923083782196
    model: gemini-3.8-flash
    generated_at: '2026-11-20 05:09:07 '
---

## Problem #3041: Maximize Consecutive Elements in an Array After Modification

**Difficulty:** Hard

**Topics:** Array, Dynamic Programming, Sorting

## Problem Description

<p>You are given a <strong>0-indexed</strong> array <code>nums</code> consisting of <strong>positive</strong> integers.</p>

<p>Initially, you can increase the value of <strong>any</strong> element in the array by <strong>at most</strong> <code>1</code>.</p>

<p>After that, you need to select <strong>one or more</strong> elements from the final array such that those elements are <strong>consecutive</strong> when sorted in increasing order. For example, the elements <code>[3, 4, 5]</code> are consecutive while <code>[3, 4, 6]</code> and <code>[1, 1, 2, 3]</code> are not.<!-- notionvc: 312f8c5d-40d0-4cd1-96cc-9e96a846735b --></p>

<p>Return <em>the <strong>maximum</strong> number of elements that you can select</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,1,5,1,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can increase the elements at indices 0 and 3. The resulting array is nums = [3,1,5,2,1].
We select the elements [<u><strong>3</strong></u>,<u><strong>1</strong></u>,5,<u><strong>2</strong></u>,1] and we sort them to obtain [1,2,3], which are consecutive.
It can be shown that we cannot select more than 3 consecutive elements.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,4,7,10]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The maximum consecutive elements that we can select is 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## Hints

1. Sort the array and try using dynamic programming.

2. Let `dp[i]` be the length of the longest consecutive elements ending at element at index `i` in the sorted array.

## ✨ AI-Generated Solution (gemini-3.8-flash)

### Approach

To maximize the number of consecutive elements, we first sort the array in non-decreasing order. Each element $x$ can either be kept as $x$ or incremented to $x + 1$. By processing the sorted numbers sequentially, an element $x$ can extend a consecutive sequence ending at $x$ (by transforming into $x + 1$) or a consecutive sequence ending at $x - 1$ (by remaining $x$). We can define a dynamic programming state where $dp[v]$ represents the maximum length of a consecutive sequence ending with value $v$.

When considering each number $x$ in sorted order, we update the DP states in the order of $dp[x + 1] = dp[x] + 1$ followed by $dp[x] = dp[x - 1] + 1$. Updating $dp[x + 1]$ first is crucial so that it uses the state $dp[x]$ computed from prior elements, preventing the current element from being counted twice (once as $x$ and once as $x + 1$). The final answer is the maximum value achieved across all DP states.

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
// Generation failed for C++
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
// Generation failed for Java
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
// Generation failed for Python
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = {}
        for x in nums:
            dp[x + 1] = dp.get(x, 0) + 1
            dp[x] = dp.get(x - 1, 0) + 1
        return max(dp.values())
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
static int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int maxSelectedElements(int* nums, int numsSize) {
    qsort(nums, numsSize, sizeof(int), compare);
    int maxVal = nums[numsSize - 1];
    int* dp = (int*)calloc(maxVal + 2, sizeof(int));
    int ans = 0;

    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        dp[x + 1] = dp[x] + 1;
        dp[x] = dp[x - 1] + 1;
        if (dp[x + 1] > ans) ans = dp[x + 1];
        if (dp[x] > ans) ans = dp[x];
    }

    free(dp);
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaxSelectedElements(int[] nums) {
        Array.Sort(nums);
        int maxVal = nums[nums.Length - 1];
        int[] dp = new int[maxVal + 2];
        int ans = 0;

        foreach (int x in nums) {
            dp[x + 1] = dp[x] + 1;
            dp[x] = dp[x - 1] + 1;
            if (dp[x + 1] > ans) ans = dp[x + 1];
            if (dp[x] > ans) ans = dp[x];
        }

        return ans;
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
var maxSelectedElements = function(nums) {
    nums.sort((a, b) => a - b);
    const dp = new Map();
    let ans = 0;

    for (const x of nums) {
        const nextLen = (dp.get(x) || 0) + 1;
        const currLen = (dp.get(x - 1) || 0) + 1;
        dp.set(x + 1, nextLen);
        dp.set(x, currLen);
        if (nextLen > ans) ans = nextLen;
        if (currLen > ans) ans = currLen;
    }

    return ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxSelectedElements(nums: number[]): number {
    nums.sort((a, b) => a - b);
    const dp = new Map<number, number>();
    let ans = 0;
    for (const x of nums) {
        const next = (dp.get(x) ?? 0) + 1;
        const curr = (dp.get(x - 1) ?? 0) + 1;
        dp.set(x + 1, next);
        dp.set(x, curr);
        if (next > ans) ans = next;
        if (curr > ans) ans = curr;
    }
    return ans;
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
    function maxSelectedElements($nums) {
        sort($nums);
        $dp = [];
        $ans = 0;
        foreach ($nums as $x) {
            $next = ($dp[$x] ?? 0) + 1;
            $curr = ($dp[$x - 1] ?? 0) + 1;
            $dp[$x + 1] = $next;
            $dp[$x] = $curr;
            if ($next > $ans) $ans = $next;
            if ($curr > $ans) $ans = $curr;
        }
        return $ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxSelectedElements(_ nums: [Int]) -> Int {
        let sortedNums = nums.sorted()
        var dp = [Int: Int](minimumCapacity: nums.count * 2)
        var ans = 0
        for x in sortedNums {
            let next = (dp[x] ?? 0) + 1
            let curr = (dp[x - 1] ?? 0) + 1
            dp[x + 1] = next
            dp[x] = curr
            if next > ans { ans = next }
            if curr > ans { ans = curr }
        }
        return ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxSelectedElements(nums: IntArray): Int {
        nums.sort()
        val dp = HashMap<Int, Int>(nums.size * 2)
        var ans = 0
        for (x in nums) {
            val next = (dp[x] ?: 0) + 1
            val curr = (dp[x - 1] ?: 0) + 1
            dp[x + 1] = next
            dp[x] = curr
            if (next > ans) ans = next
            if (curr > ans) ans = curr
        }
        return ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maxSelectedElements(List<int> nums) {
    nums.sort();
    final dp = <int, int>{};
    int ans = 0;
    for (final x in nums) {
      final v1 = (dp[x] ?? 0) + 1;
      final v2 = (dp[x - 1] ?? 0) + 1;
      dp[x + 1] = v1;
      dp[x] = v2;
      if (v1 > ans) ans = v1;
      if (v2 > ans) ans = v2;
    }
    return ans;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxSelectedElements(nums []int) int {
    sort.Ints(nums)
    dp := make(map[int]int)
    ans := 0
    for _, x := range nums {
        dp[x+1] = dp[x] + 1
        dp[x] = dp[x-1] + 1
        if dp[x+1] > ans {
            ans = dp[x+1]
        }
        if dp[x] > ans {
            ans = dp[x]
        }
    }
    return ans
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def max_selected_elements(nums)
  nums.sort!
  dp = Hash.new(0)
  ans = 0
  nums.each do |x|
    v1 = dp[x] + 1
    v2 = dp[x - 1] + 1
    dp[x + 1] = v1
    dp[x] = v2
    ans = v1 if v1 > ans
    ans = v2 if v2 > ans
  end
  ans
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxSelectedElements(nums: Array[Int]): Int = {
        scala.util.Sorting.quickSort(nums)
        val dp = new scala.collection.mutable.HashMap[Int, Int]()
        var ans = 0
        for (x <- nums) {
            val v1 = dp.getOrElse(x, 0) + 1
            val v2 = dp.getOrElse(x - 1, 0) + 1
            dp(x + 1) = v1
            dp(x) = v2
            if (v1 > ans) ans = v1
            if (v2 > ans) ans = v2
        }
        ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
// Generation failed for Rust
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
// Generation failed for Racket
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
// Generation failed for Erlang
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
// Generation failed for Elixir
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n \log n) where $n$ is the length of the array, dominated by the sorting step. The subsequent dynamic programming traversal processes each element in $O(1)$ time.
- **Space Complexity:** O(n) auxiliary space to store the dynamic programming states (or $O(\max(nums))$ when using a direct array), plus $O(n)$ space for sorting depending on the language runtime.
