---
layout: post
title: "Longest Subsequence With Non-Zero Bitwise XOR"
date: 2026-08-15 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Bit Manipulation"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int longestSubsequence(vector<int>& nums)\
        \ {\n        int totalXor = 0;\n        bool hasNonZero = false;\n        int\
        \ n = nums.size();\n        for (int x : nums) {\n            totalXor ^= x;\n\
        \            if (x != 0) {\n                hasNonZero = true;\n           \
        \ }\n        }\n        if (totalXor != 0) {\n            return n;\n      \
        \  }\n        if (hasNonZero) {\n            return n - 1;\n        }\n    \
        \    return 0;\n    }\n};"
      java: "class Solution {\n    public int longestSubsequence(int[] nums) {\n   \
        \     int totalXor = 0;\n        boolean hasNonZero = false;\n        int n\
        \ = nums.length;\n        for (int x : nums) {\n            totalXor ^= x;\n\
        \            if (x != 0) {\n                hasNonZero = true;\n           \
        \ }\n        }\n        if (totalXor != 0) {\n            return n;\n      \
        \  }\n        if (hasNonZero) {\n            return n - 1;\n        }\n    \
        \    return 0;\n    }\n}"
      python: "class Solution(object):\n    def longestSubsequence(self, nums):\n  \
        \      \"\"\"\n        :type nums: List[int]\n        :rtype: int\n        \"\
        \"\"\n        total_xor = 0\n        has_non_zero = False\n        n = len(nums)\n\
        \        for x in nums:\n            total_xor ^= x\n            if x != 0:\n\
        \                has_non_zero = True\n        if total_xor != 0:\n         \
        \   return n\n        if has_non_zero:\n            return n - 1\n        return\
        \ 0"
      python3: "class Solution:\n    def longestSubsequence(self, nums: List[int]) ->\
        \ int:\n        total_xor = 0\n        has_non_zero = False\n        n = len(nums)\n\
        \        for x in nums:\n            total_xor ^= x\n            if x != 0:\n\
        \                has_non_zero = True\n        if total_xor != 0:\n         \
        \   return n\n        if has_non_zero:\n            return n - 1\n        return\
        \ 0"
      c: "int longestSubsequence(int* nums, int numsSize) {\n    int totalXor = 0;\n\
        \    int hasNonZero = 0;\n    for (int i = 0; i < numsSize; i++) {\n       \
        \ totalXor ^= nums[i];\n        if (nums[i] != 0) {\n            hasNonZero\
        \ = 1;\n        }\n    }\n    if (totalXor != 0) {\n        return numsSize;\n\
        \    }\n    if (hasNonZero) {\n        return numsSize - 1;\n    }\n    return\
        \ 0;\n}"
      csharp: "public class Solution {\n    public int LongestSubsequence(int[] nums)\
        \ {\n        int totalXor = 0;\n        bool hasNonZero = false;\n        for\
        \ (int i = 0; i < nums.Length; i++) {\n            totalXor ^= nums[i];\n  \
        \          if (nums[i] != 0) {\n                hasNonZero = true;\n       \
        \     }\n        }\n        if (totalXor != 0) {\n            return nums.Length;\n\
        \        }\n        if (hasNonZero) {\n            return nums.Length - 1;\n\
        \        }\n        return 0;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar longestSubsequence\
        \ = function(nums) {\n    var totalXor = 0;\n    var hasNonZero = false;\n \
        \   var n = nums.length;\n    for (var i = 0; i < n; i++) {\n        totalXor\
        \ ^= nums[i];\n        if (nums[i] !== 0) {\n            hasNonZero = true;\n\
        \        }\n    }\n    if (totalXor !== 0) {\n        return n;\n    }\n   \
        \ if (hasNonZero) {\n        return n - 1;\n    }\n    return 0;\n};"
      typescript: "function longestSubsequence(nums: number[]): number {\n    let totalXor:\
        \ number = 0;\n    let hasNonZero: boolean = false;\n    const n: number = nums.length;\n\
        \    for (let i = 0; i < n; i++) {\n        totalXor ^= nums[i];\n        if\
        \ (nums[i] !== 0) {\n            hasNonZero = true;\n        }\n    }\n    if\
        \ (totalXor !== 0) {\n        return n;\n    }\n    if (hasNonZero) {\n    \
        \    return n - 1;\n    }\n    return 0;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function longestSubsequence($nums) {\n        $totalXor\
        \ = 0;\n        $hasNonZero = false;\n        $n = count($nums);\n        foreach\
        \ ($nums as $num) {\n            $totalXor ^= $num;\n            if ($num !=\
        \ 0) {\n                $hasNonZero = true;\n            }\n        }\n    \
        \    if ($totalXor != 0) {\n            return $n;\n        }\n        if ($hasNonZero)\
        \ {\n            return $n - 1;\n        }\n        return 0;\n    }\n}"
      swift: "class Solution {\n    func longestSubsequence(_ nums: [Int]) -> Int {\n\
        \        var totalXor = 0\n        var hasNonZero = false\n        let n = nums.count\n\
        \        for num in nums {\n            totalXor ^= num\n            if num\
        \ != 0 {\n                hasNonZero = true\n            }\n        }\n    \
        \    if totalXor != 0 {\n            return n\n        }\n        if hasNonZero\
        \ {\n            return n - 1\n        }\n        return 0\n    }\n}"
      kotlin: "class Solution {\n    fun longestSubsequence(nums: IntArray): Int {\n\
        \        var xorSum = 0\n        var hasNonZero = false\n        for (n in nums)\
        \ {\n            xorSum = xorSum xor n\n            if (n != 0) {\n        \
        \        hasNonZero = true\n            }\n        }\n        if (xorSum !=\
        \ 0) {\n            return nums.size\n        }\n        if (hasNonZero) {\n\
        \            return nums.size - 1\n        }\n        return 0\n    }\n}"
      dart: "class Solution {\n  int longestSubsequence(List<int> nums) {\n    int xorSum\
        \ = 0;\n    bool hasNonZero = false;\n    for (int n in nums) {\n      xorSum\
        \ ^= n;\n      if (n != 0) {\n        hasNonZero = true;\n      }\n    }\n \
        \   if (xorSum != 0) {\n      return nums.length;\n    }\n    if (hasNonZero)\
        \ {\n      return nums.length - 1;\n    }\n    return 0;\n  }\n}"
      go: "func longestSubsequence(nums []int) int {\n    xorSum := 0\n    hasNonZero\
        \ := false\n    for _, n := range nums {\n        xorSum ^= n\n        if n\
        \ != 0 {\n            hasNonZero = true\n        }\n    }\n    if xorSum !=\
        \ 0 {\n        return len(nums)\n    }\n    if hasNonZero {\n        return\
        \ len(nums) - 1\n    }\n    return 0\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef longest_subsequence(nums)\n\
        \  xor_sum = 0\n  has_non_zero = false\n  nums.each do |n|\n    xor_sum ^= n\n\
        \    has_non_zero = true if n != 0\n  end\n  if xor_sum != 0\n    return nums.length\n\
        \  end\n  if has_non_zero\n    return nums.length - 1\n  end\n  0\nend"
      scala: "object Solution {\n    def longestSubsequence(nums: Array[Int]): Int =\
        \ {\n        var xorSum = 0\n        var hasNonZero = false\n        for (n\
        \ <- nums) {\n            xorSum ^= n\n            if (n != 0) {\n         \
        \       hasNonZero = true\n            }\n        }\n        if (xorSum != 0)\
        \ {\n            nums.length\n        } else if (hasNonZero) {\n           \
        \ nums.length - 1\n        } else {\n            0\n        }\n    }\n}"
      rust: "impl Solution {\n    pub fn longest_subsequence(nums: Vec<i32>) -> i32\
        \ {\n        let n = nums.len() as i32;\n        let mut total_xor = 0;\n  \
        \      let mut has_nonzero = false;\n        for &num in &nums {\n         \
        \   total_xor ^= num;\n            if num != 0 {\n                has_nonzero\
        \ = true;\n            }\n        }\n        if total_xor != 0 {\n         \
        \   n\n        } else if has_nonzero {\n            n - 1\n        } else {\n\
        \            0\n        }\n    }\n}"
      racket: "(define/contract (longest-subsequence nums)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let ([total-xor (foldl bitwise-xor 0 nums)]\n        [has-nonzero\
        \ (ormap (lambda (x) (not (zero? x))) nums)]\n        [len (length nums)])\n\
        \    (cond\n      [(not (zero? total-xor)) len]\n      [has-nonzero (- len 1)]\n\
        \      [else 0])))"
      erlang: "-spec longest_subsequence(Nums :: [integer()]) -> integer().\nlongest_subsequence(Nums)\
        \ ->\n    TotalXor = lists:foldl(fun(X, Acc) -> X bxor Acc end, 0, Nums),\n\
        \    HasNonZero = lists:any(fun(X) -> X /= 0 end, Nums),\n    Len = length(Nums),\n\
        \    if\n        TotalXor /= 0 -> Len;\n        HasNonZero -> Len - 1;\n   \
        \     true -> 0\n    end."
      elixir: "defmodule Solution do\n  require Bitwise\n  @spec longest_subsequence(nums\
        \ :: [integer]) :: integer\n  def longest_subsequence(nums) do\n    total_xor\
        \ = Enum.reduce(nums, 0, fn x, acc -> Bitwise.bxor(x, acc) end)\n    has_nonzero\
        \ = Enum.any?(nums, fn x -> x != 0 end)\n    len = length(nums)\n    cond do\n\
        \      total_xor != 0 -> len\n      has_nonzero -> len - 1\n      true -> 0\n\
        \    end\n  end\nend"
    approach: 'The core strategy is to evaluate the bitwise XOR sum of all elements
      in the entire array. If this total XOR sum is non-zero, the longest subsequence
      is the entire array itself, and we return its full length. Since the bitwise XOR
      operation is commutative and associative, adding a zero to a subsequence does
      not change its bitwise XOR value but does increase its length; thus, all zeros
      should be included in the subsequence if the total XOR is already non-zero.


      If the total XOR sum is zero, the original array cannot be the longest subsequence
      with a non-zero XOR. We must remove at least one element to obtain a non-zero
      XOR sum. Removing a non-zero element $x$ from the set results in a new XOR sum
      of $0 \text{ XOR } x = x$, which is non-zero, yielding a subsequence of length
      $n-1$. If the array consists entirely of zeros, any possible subsequence will
      also have an XOR sum of zero, so the longest such subsequence with a non-zero
      XOR does not exist, and we return 0.'
    time_complexity: O(n) where $n$ is the number of elements in the input array. We
      iterate through the array once to calculate the total bitwise XOR sum and to check
      for the existence of at least one non-zero element.
    space_complexity: O(1) because we only use a constant amount of extra space for
      the cumulative XOR variable and a boolean flag, regardless of the size of the
      input array.
    elapsed_time: 155.21358060836792
    model: gemini-3-flash-preview
    generated_at: '2026-08-15 00:49:44 '
---

## Problem #3702: Longest Subsequence With Non-Zero Bitwise XOR

**Difficulty:** Medium

**Topics:** Array, Bit Manipulation

## Problem Description

<p>You are given an integer array <code>nums</code>.</p>

<p>Return the length of the <strong>longest <span data-keyword="subsequence-array-nonempty">subsequence</span></strong> in <code>nums</code> whose bitwise <strong>XOR</strong> is <strong>non-zero</strong>. If no such <strong>subsequence</strong> exists, return 0.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>One longest subsequence is <code>[2, 3]</code>. The bitwise XOR is computed as <code>2 XOR 3 = 1</code>, which is non-zero.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>The longest subsequence is <code>[2, 3, 4]</code>. The bitwise XOR is computed as <code>2 XOR 3 XOR 4 = 5</code>, which is non-zero.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. What happens if you take the entire array?

2. If the XOR of the entire array is 0, can removing one element help?

3. What if all elements are 0?

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The core strategy is to evaluate the bitwise XOR sum of all elements in the entire array. If this total XOR sum is non-zero, the longest subsequence is the entire array itself, and we return its full length. Since the bitwise XOR operation is commutative and associative, adding a zero to a subsequence does not change its bitwise XOR value but does increase its length; thus, all zeros should be included in the subsequence if the total XOR is already non-zero.

If the total XOR sum is zero, the original array cannot be the longest subsequence with a non-zero XOR. We must remove at least one element to obtain a non-zero XOR sum. Removing a non-zero element $x$ from the set results in a new XOR sum of $0 \text{ XOR } x = x$, which is non-zero, yielding a subsequence of length $n-1$. If the array consists entirely of zeros, any possible subsequence will also have an XOR sum of zero, so the longest such subsequence with a non-zero XOR does not exist, and we return 0.

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
    int longestSubsequence(vector<int>& nums) {
        int totalXor = 0;
        bool hasNonZero = false;
        int n = nums.size();
        for (int x : nums) {
            totalXor ^= x;
            if (x != 0) {
                hasNonZero = true;
            }
        }
        if (totalXor != 0) {
            return n;
        }
        if (hasNonZero) {
            return n - 1;
        }
        return 0;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int longestSubsequence(int[] nums) {
        int totalXor = 0;
        boolean hasNonZero = false;
        int n = nums.length;
        for (int x : nums) {
            totalXor ^= x;
            if (x != 0) {
                hasNonZero = true;
            }
        }
        if (totalXor != 0) {
            return n;
        }
        if (hasNonZero) {
            return n - 1;
        }
        return 0;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_xor = 0
        has_non_zero = False
        n = len(nums)
        for x in nums:
            total_xor ^= x
            if x != 0:
                has_non_zero = True
        if total_xor != 0:
            return n
        if has_non_zero:
            return n - 1
        return 0
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = 0
        has_non_zero = False
        n = len(nums)
        for x in nums:
            total_xor ^= x
            if x != 0:
                has_non_zero = True
        if total_xor != 0:
            return n
        if has_non_zero:
            return n - 1
        return 0
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int longestSubsequence(int* nums, int numsSize) {
    int totalXor = 0;
    int hasNonZero = 0;
    for (int i = 0; i < numsSize; i++) {
        totalXor ^= nums[i];
        if (nums[i] != 0) {
            hasNonZero = 1;
        }
    }
    if (totalXor != 0) {
        return numsSize;
    }
    if (hasNonZero) {
        return numsSize - 1;
    }
    return 0;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int LongestSubsequence(int[] nums) {
        int totalXor = 0;
        bool hasNonZero = false;
        for (int i = 0; i < nums.Length; i++) {
            totalXor ^= nums[i];
            if (nums[i] != 0) {
                hasNonZero = true;
            }
        }
        if (totalXor != 0) {
            return nums.Length;
        }
        if (hasNonZero) {
            return nums.Length - 1;
        }
        return 0;
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
var longestSubsequence = function(nums) {
    var totalXor = 0;
    var hasNonZero = false;
    var n = nums.length;
    for (var i = 0; i < n; i++) {
        totalXor ^= nums[i];
        if (nums[i] !== 0) {
            hasNonZero = true;
        }
    }
    if (totalXor !== 0) {
        return n;
    }
    if (hasNonZero) {
        return n - 1;
    }
    return 0;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function longestSubsequence(nums: number[]): number {
    let totalXor: number = 0;
    let hasNonZero: boolean = false;
    const n: number = nums.length;
    for (let i = 0; i < n; i++) {
        totalXor ^= nums[i];
        if (nums[i] !== 0) {
            hasNonZero = true;
        }
    }
    if (totalXor !== 0) {
        return n;
    }
    if (hasNonZero) {
        return n - 1;
    }
    return 0;
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
    function longestSubsequence($nums) {
        $totalXor = 0;
        $hasNonZero = false;
        $n = count($nums);
        foreach ($nums as $num) {
            $totalXor ^= $num;
            if ($num != 0) {
                $hasNonZero = true;
            }
        }
        if ($totalXor != 0) {
            return $n;
        }
        if ($hasNonZero) {
            return $n - 1;
        }
        return 0;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func longestSubsequence(_ nums: [Int]) -> Int {
        var totalXor = 0
        var hasNonZero = false
        let n = nums.count
        for num in nums {
            totalXor ^= num
            if num != 0 {
                hasNonZero = true
            }
        }
        if totalXor != 0 {
            return n
        }
        if hasNonZero {
            return n - 1
        }
        return 0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun longestSubsequence(nums: IntArray): Int {
        var xorSum = 0
        var hasNonZero = false
        for (n in nums) {
            xorSum = xorSum xor n
            if (n != 0) {
                hasNonZero = true
            }
        }
        if (xorSum != 0) {
            return nums.size
        }
        if (hasNonZero) {
            return nums.size - 1
        }
        return 0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int longestSubsequence(List<int> nums) {
    int xorSum = 0;
    bool hasNonZero = false;
    for (int n in nums) {
      xorSum ^= n;
      if (n != 0) {
        hasNonZero = true;
      }
    }
    if (xorSum != 0) {
      return nums.length;
    }
    if (hasNonZero) {
      return nums.length - 1;
    }
    return 0;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func longestSubsequence(nums []int) int {
    xorSum := 0
    hasNonZero := false
    for _, n := range nums {
        xorSum ^= n
        if n != 0 {
            hasNonZero = true
        }
    }
    if xorSum != 0 {
        return len(nums)
    }
    if hasNonZero {
        return len(nums) - 1
    }
    return 0
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def longest_subsequence(nums)
  xor_sum = 0
  has_non_zero = false
  nums.each do |n|
    xor_sum ^= n
    has_non_zero = true if n != 0
  end
  if xor_sum != 0
    return nums.length
  end
  if has_non_zero
    return nums.length - 1
  end
  0
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def longestSubsequence(nums: Array[Int]): Int = {
        var xorSum = 0
        var hasNonZero = false
        for (n <- nums) {
            xorSum ^= n
            if (n != 0) {
                hasNonZero = true
            }
        }
        if (xorSum != 0) {
            nums.length
        } else if (hasNonZero) {
            nums.length - 1
        } else {
            0
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn longest_subsequence(nums: Vec<i32>) -> i32 {
        let n = nums.len() as i32;
        let mut total_xor = 0;
        let mut has_nonzero = false;
        for &num in &nums {
            total_xor ^= num;
            if num != 0 {
                has_nonzero = true;
            }
        }
        if total_xor != 0 {
            n
        } else if has_nonzero {
            n - 1
        } else {
            0
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (longest-subsequence nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ([total-xor (foldl bitwise-xor 0 nums)]
        [has-nonzero (ormap (lambda (x) (not (zero? x))) nums)]
        [len (length nums)])
    (cond
      [(not (zero? total-xor)) len]
      [has-nonzero (- len 1)]
      [else 0])))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec longest_subsequence(Nums :: [integer()]) -> integer().
longest_subsequence(Nums) ->
    TotalXor = lists:foldl(fun(X, Acc) -> X bxor Acc end, 0, Nums),
    HasNonZero = lists:any(fun(X) -> X /= 0 end, Nums),
    Len = length(Nums),
    if
        TotalXor /= 0 -> Len;
        HasNonZero -> Len - 1;
        true -> 0
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  require Bitwise
  @spec longest_subsequence(nums :: [integer]) :: integer
  def longest_subsequence(nums) do
    total_xor = Enum.reduce(nums, 0, fn x, acc -> Bitwise.bxor(x, acc) end)
    has_nonzero = Enum.any?(nums, fn x -> x != 0 end)
    len = length(nums)
    cond do
      total_xor != 0 -> len
      has_nonzero -> len - 1
      true -> 0
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where $n$ is the number of elements in the input array. We iterate through the array once to calculate the total bitwise XOR sum and to check for the existence of at least one non-zero element.
- **Space Complexity:** O(1) because we only use a constant amount of extra space for the cumulative XOR variable and a boolean flag, regardless of the size of the input array.
