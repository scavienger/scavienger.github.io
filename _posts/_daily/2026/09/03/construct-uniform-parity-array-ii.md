---
layout: post
title: "Construct Uniform Parity Array II"
date: 2026-09-03 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Math"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/construct-uniform-parity-array-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool uniformArray(vector<int>& nums1) {\n\
        \        int n = nums1.size();\n        int min_val = nums1[0];\n        bool\
        \ has_odd = false;\n        for (int i = 0; i < n; ++i) {\n            if (nums1[i]\
        \ < min_val) {\n                min_val = nums1[i];\n            }\n       \
        \     if (nums1[i] % 2 != 0) {\n                has_odd = true;\n          \
        \  }\n        }\n        return (min_val % 2 != 0) || (!has_odd);\n    }\n};"
      java: "class Solution {\n    public boolean uniformArray(int[] nums1) {\n    \
        \    int n = nums1.length;\n        int minVal = nums1[0];\n        boolean\
        \ hasOdd = false;\n        for (int i = 0; i < n; i++) {\n            if (nums1[i]\
        \ < minVal) {\n                minVal = nums1[i];\n            }\n         \
        \   if (nums1[i] % 2 != 0) {\n                hasOdd = true;\n            }\n\
        \        }\n        return (minVal % 2 != 0) || (!hasOdd);\n    }\n}"
      python: "class Solution(object):\n    def uniformArray(self, nums1):\n       \
        \ \"\"\"\n        :type nums1: List[int]\n        :rtype: bool\n        \"\"\
        \"\n        min_val = min(nums1)\n        has_odd = False\n        for x in\
        \ nums1:\n            if x % 2 != 0:\n                has_odd = True\n     \
        \           break\n        return (min_val % 2 != 0) or (not has_odd)"
      python3: "class Solution:\n    def uniformArray(self, nums1: list[int]) -> bool:\n\
        \        min_val = min(nums1)\n        has_odd = any(x % 2 != 0 for x in nums1)\n\
        \        return (min_val % 2 != 0) or (not has_odd)"
      c: "#include <stdbool.h>\n#include <limits.h>\n\nbool uniformArray(int* nums1,\
        \ int nums1Size) {\n    int min_val = nums1[0];\n    bool has_odd = false;\n\
        \    for (int i = 0; i < nums1Size; i++) {\n        if (nums1[i] < min_val)\
        \ {\n            min_val = nums1[i];\n        }\n        if (nums1[i] % 2 !=\
        \ 0) {\n            has_odd = true;\n        }\n    }\n    return (min_val %\
        \ 2 != 0) || (!has_odd);\n}"
      csharp: "public class Solution {\n    public bool UniformArray(int[] nums1) {\n\
        \        int n = nums1.Length;\n        if (n == 0) return true;\n\n       \
        \ int minVal = nums1[0];\n        bool allEven = true;\n\n        foreach (int\
        \ x in nums1) {\n            if (x < minVal) {\n                minVal = x;\n\
        \            }\n            if (x % 2 != 0) {\n                allEven = false;\n\
        \            }\n        }\n\n        return allEven || (minVal % 2 != 0);\n\
        \    }\n}"
      javascript: "/**\n * @param {number[]} nums1\n * @return {boolean}\n */\nvar uniformArray\
        \ = function(nums1) {\n    const n = nums1.length;\n    if (n === 0) return\
        \ true;\n\n    let minVal = nums1[0];\n    let allEven = true;\n\n    for (let\
        \ i = 0; i < n; i++) {\n        if (nums1[i] < minVal) {\n            minVal\
        \ = nums1[i];\n        }\n        if (nums1[i] % 2 !== 0) {\n            allEven\
        \ = false;\n        }\n    }\n\n    return allEven || (minVal % 2 !== 0);\n\
        };"
      typescript: "function uniformArray(nums1: number[]): boolean {\n    const n =\
        \ nums1.length;\n    if (n === 0) return true;\n\n    let minVal = nums1[0];\n\
        \    let allEven = true;\n\n    for (let i = 0; i < n; i++) {\n        if (nums1[i]\
        \ < minVal) {\n            minVal = nums1[i];\n        }\n        if (nums1[i]\
        \ % 2 !== 0) {\n            allEven = false;\n        }\n    }\n\n    return\
        \ allEven || (minVal % 2 !== 0);\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums1\n     * @return\
        \ Boolean\n     */\n    function uniformArray($nums1) {\n        $n = count($nums1);\n\
        \        if ($n === 0) return true;\n\n        $minVal = $nums1[0];\n      \
        \  $allEven = true;\n\n        foreach ($nums1 as $x) {\n            if ($x\
        \ < $minVal) {\n                $minVal = $x;\n            }\n            if\
        \ ($x % 2 !== 0) {\n                $allEven = false;\n            }\n     \
        \   }\n\n        return $allEven || ($minVal % 2 !== 0);\n    }\n}"
      swift: "class Solution {\n    func uniformArray(_ nums1: [Int]) -> Bool {\n  \
        \      guard !nums1.isEmpty else { return true }\n\n        var minVal = nums1[0]\n\
        \        var allEven = true\n\n        for x in nums1 {\n            if x <\
        \ minVal {\n                minVal = x\n            }\n            if x % 2\
        \ != 0 {\n                allEven = false\n            }\n        }\n\n    \
        \    return allEven || (minVal % 2 != 0)\n    }\n}"
      kotlin: "class Solution {\n    fun uniformArray(nums1: IntArray): Boolean {\n\
        \        var minOdd = Long.MAX_VALUE\n        var minEven = Long.MAX_VALUE\n\
        \        var hasOdd = false\n        var hasEven = false\n\n        for (num\
        \ in nums1) {\n            if (num % 2 != 0) {\n                if (num.toLong()\
        \ < minOdd) {\n                    minOdd = num.toLong()\n                }\n\
        \                hasOdd = true\n            } else {\n                if (num.toLong()\
        \ < minEven) {\n                    minEven = num.toLong()\n               \
        \ }\n                hasEven = true\n            }\n        }\n\n        if\
        \ (!hasOdd || !hasEven) {\n            return true\n        }\n        return\
        \ minOdd < minEven\n    }\n}"
      dart: "class Solution {\n  bool uniformArray(List<int> nums1) {\n    int minOdd\
        \ = 2000000001;\n    int minEven = 2000000001;\n    bool hasOdd = false;\n \
        \   bool hasEven = false;\n\n    for (int num in nums1) {\n      if (num % 2\
        \ != 0) {\n        if (num < minOdd) minOdd = num;\n        hasOdd = true;\n\
        \      } else {\n        if (num < minEven) minEven = num;\n        hasEven\
        \ = true;\n      }\n    }\n\n    if (!hasOdd || !hasEven) {\n      return true;\n\
        \    }\n    return minOdd < minEven;\n  }\n}"
      go: "func uniformArray(nums1 []int) bool {\n    var minOdd, minEven int\n    var\
        \ hasOdd, hasEven bool\n\n    for _, num := range nums1 {\n        if num%2\
        \ != 0 {\n            if !hasOdd || num < minOdd {\n                minOdd =\
        \ num\n                hasOdd = true\n            }\n        } else {\n    \
        \        if !hasEven || num < minEven {\n                minEven = num\n   \
        \             hasEven = true\n            }\n        }\n    }\n\n    if !hasOdd\
        \ || !hasEven {\n        return true\n    }\n    return minOdd < minEven\n}"
      ruby: "# @param {Integer[]} nums1\n# @return {Boolean}\ndef uniform_array(nums1)\n\
        \  min_odd = nil\n  min_even = nil\n\n  nums1.each do |num|\n    if num % 2\
        \ != 0\n      if min_odd.nil? || num < min_odd\n        min_odd = num\n    \
        \  end\n    else\n      if min_even.nil? || num < min_even\n        min_even\
        \ = num\n      end\n    end\n  end\n\n  return true if min_odd.nil? || min_even.nil?\n\
        \  min_odd < min_even\nend"
      scala: "object Solution {\n    def uniformArray(nums1: Array[Int]): Boolean =\
        \ {\n        var minOdd = Long.MaxValue\n        var minEven = Long.MaxValue\n\
        \        var hasOdd = false\n        var hasEven = false\n\n        for (num\
        \ <- nums1) {\n            if (num % 2 != 0) {\n                if (num.toLong\
        \ < minOdd) minOdd = num.toLong\n                hasOdd = true\n           \
        \ } else {\n                if (num.toLong < minEven) minEven = num.toLong\n\
        \                hasEven = true\n            }\n        }\n\n        if (!hasOdd\
        \ || !hasEven) {\n            true\n        } else {\n            minOdd < minEven\n\
        \        }\n    }\n}"
      rust: "impl Solution {\n    pub fn uniform_array(nums1: Vec<i32>) -> bool {\n\
        \        let min_val = *nums1.iter().min().unwrap();\n        if min_val % 2\
        \ != 0 {\n            true\n        } else {\n            nums1.iter().all(|&x|\
        \ x % 2 == 0)\n        }\n    }\n}"
      racket: "(define/contract (uniform-array nums1)\n  (-> (listof exact-integer?)\
        \ boolean?)\n  (let ([min-val (apply min nums1)])\n    (if (odd? min-val)\n\
        \        #t\n        (andmap even? nums1))))"
      erlang: "uniform_array(Nums1) ->\n  MinVal = lists:min(Nums1),\n  case MinVal\
        \ rem 2 of\n    1 -> true;\n    0 -> lists:all(fun(X) -> X rem 2 =:= 0 end,\
        \ Nums1)\n  end."
      elixir: "defmodule Solution do\n  @spec uniform_array(nums1 :: [integer]) :: boolean\n\
        \  def uniform_array(nums1) do\n    min_val = Enum.min(nums1)\n    if rem(min_val,\
        \ 2) != 0 do\n      true\n    else\n      Enum.all?(nums1, fn x -> rem(x, 2)\
        \ == 0 end)\n    end\n  end\nend"
    approach: 'The problem asks whether we can construct an array where all elements
      have the same parity (either all even or all odd). Every element in the constructed
      array, $nums2[i]$, is either the original element $nums1[i]$ or the result of
      $nums1[i] - nums1[j]$ where $nums1[j] < nums1[i]$. The key intuition is that the
      smallest element in the original array, $min\_val$, can never be changed because
      there is no $nums1[j]$ smaller than it. Consequently, the parity of the entire
      constructed array $nums2$ must match the parity of $min\_val$. If $min\_val$ is
      odd, we must attempt to make all elements odd; if $min\_val$ is even, we must
      attempt to make all elements even.


      If $min\_val$ is odd, we can successfully make all elements odd: any original
      odd number remains as it is, and any original even number $nums1[i]$ can be converted
      by subtracting $min\_val$ (even - odd = odd). Since $min\_val$ is the smallest
      element, $nums1[i] - min\_val$ will always be at least 1. If $min\_val$ is even,
      we can only succeed if all original elements are already even. This is because
      any odd number $nums1[i]$ would require subtracting a smaller odd number to become
      even, but if there are any odd numbers, the smallest one among them will not have
      a smaller odd number to subtract from it. Therefore, the construction is possible
      if either the smallest element is odd or every element in the array is even.'
    time_complexity: 'O(n) with one-paragraph explanation: The algorithm requires a
      single pass through the array to determine the minimum element and check if any
      element in the array is odd. Both operations are linear with respect to the number
      of elements in the input array.'
    space_complexity: 'O(1) with one-paragraph explanation: The solution only uses a
      few scalar variables to store the minimum value and a boolean flag, regardless
      of the size of the input array.'
    elapsed_time: 263.6705937385559
    model: gemini-3-flash-preview
    generated_at: '2026-09-03 02:25:46 '
---

## Problem #3876: Construct Uniform Parity Array II

**Difficulty:** Medium

**Topics:** Array, Math

## Problem Description

<p>You are given an array <code>nums1</code> of <code>n</code> <strong>distinct</strong> integers.</p>

<p>You want to construct another array <code>nums2</code> of length <code>n</code> such that the elements in <code>nums2</code> are either <strong>all odd or all even</strong>.</p>

<p>For each index <code>i</code>, you must choose <strong>exactly one</strong> of the following (in any order):</p>

<ul>
	<li><code>nums2[i] = nums1[i]</code>​​​​​​​</li>
	<li><code>nums2[i] = nums1[i] - nums1[j]</code>, for an index <code>j != i</code>, such that <code>nums1[i] - nums1[j] &gt;= 1</code></li>
</ul>

<p>Return <code>true</code> if it is possible to construct such an array, otherwise return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums1 = [1,4,7]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong>​​​​​​​​​​​​​​</p>

<ul>
	<li>Set <code>nums2[0] = nums1[0] = 1</code>.</li>
	<li>Set <code>nums2[1] = nums1[1] - nums1[0] = 4 - 1 = 3</code>.</li>
	<li>Set <code>nums2[2] = nums1[2] = 7</code>.</li>
	<li><code>nums2 = [1, 3, 7]</code>, and all elements are odd. Thus, the answer is <code>true</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums1 = [2,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p>It is not possible to construct <code>nums2</code> such that all elements have the same parity. Thus, the answer is <code>false</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums1 = [4,6]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Set <code>nums2[0] = nums1[0] = 4</code>.</li>
	<li>Set <code>nums2[1] = nums1[1] = 6</code>.</li>
	<li><code>nums2 = [4, 6]</code>, and all elements are even. Thus, the answer is <code>true</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums1.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums1[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>nums1</code> consists of distinct integers.</li>
</ul>


## Hints

1. Try fixing the parity to either all even or all odd.

2. Use the smallest odd/even element if a subtraction is needed to match the chosen parity.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks whether we can construct an array where all elements have the same parity (either all even or all odd). Every element in the constructed array, $nums2[i]$, is either the original element $nums1[i]$ or the result of $nums1[i] - nums1[j]$ where $nums1[j] < nums1[i]$. The key intuition is that the smallest element in the original array, $min\_val$, can never be changed because there is no $nums1[j]$ smaller than it. Consequently, the parity of the entire constructed array $nums2$ must match the parity of $min\_val$. If $min\_val$ is odd, we must attempt to make all elements odd; if $min\_val$ is even, we must attempt to make all elements even.

If $min\_val$ is odd, we can successfully make all elements odd: any original odd number remains as it is, and any original even number $nums1[i]$ can be converted by subtracting $min\_val$ (even - odd = odd). Since $min\_val$ is the smallest element, $nums1[i] - min\_val$ will always be at least 1. If $min\_val$ is even, we can only succeed if all original elements are already even. This is because any odd number $nums1[i]$ would require subtracting a smaller odd number to become even, but if there are any odd numbers, the smallest one among them will not have a smaller odd number to subtract from it. Therefore, the construction is possible if either the smallest element is odd or every element in the array is even.

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
    bool uniformArray(vector<int>& nums1) {
        int n = nums1.size();
        int min_val = nums1[0];
        bool has_odd = false;
        for (int i = 0; i < n; ++i) {
            if (nums1[i] < min_val) {
                min_val = nums1[i];
            }
            if (nums1[i] % 2 != 0) {
                has_odd = true;
            }
        }
        return (min_val % 2 != 0) || (!has_odd);
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean uniformArray(int[] nums1) {
        int n = nums1.length;
        int minVal = nums1[0];
        boolean hasOdd = false;
        for (int i = 0; i < n; i++) {
            if (nums1[i] < minVal) {
                minVal = nums1[i];
            }
            if (nums1[i] % 2 != 0) {
                hasOdd = true;
            }
        }
        return (minVal % 2 != 0) || (!hasOdd);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        min_val = min(nums1)
        has_odd = False
        for x in nums1:
            if x % 2 != 0:
                has_odd = True
                break
        return (min_val % 2 != 0) or (not has_odd)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_val = min(nums1)
        has_odd = any(x % 2 != 0 for x in nums1)
        return (min_val % 2 != 0) or (not has_odd)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdbool.h>
#include <limits.h>

bool uniformArray(int* nums1, int nums1Size) {
    int min_val = nums1[0];
    bool has_odd = false;
    for (int i = 0; i < nums1Size; i++) {
        if (nums1[i] < min_val) {
            min_val = nums1[i];
        }
        if (nums1[i] % 2 != 0) {
            has_odd = true;
        }
    }
    return (min_val % 2 != 0) || (!has_odd);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool UniformArray(int[] nums1) {
        int n = nums1.Length;
        if (n == 0) return true;

        int minVal = nums1[0];
        bool allEven = true;

        foreach (int x in nums1) {
            if (x < minVal) {
                minVal = x;
            }
            if (x % 2 != 0) {
                allEven = false;
            }
        }

        return allEven || (minVal % 2 != 0);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} nums1
 * @return {boolean}
 */
var uniformArray = function(nums1) {
    const n = nums1.length;
    if (n === 0) return true;

    let minVal = nums1[0];
    let allEven = true;

    for (let i = 0; i < n; i++) {
        if (nums1[i] < minVal) {
            minVal = nums1[i];
        }
        if (nums1[i] % 2 !== 0) {
            allEven = false;
        }
    }

    return allEven || (minVal % 2 !== 0);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function uniformArray(nums1: number[]): boolean {
    const n = nums1.length;
    if (n === 0) return true;

    let minVal = nums1[0];
    let allEven = true;

    for (let i = 0; i < n; i++) {
        if (nums1[i] < minVal) {
            minVal = nums1[i];
        }
        if (nums1[i] % 2 !== 0) {
            allEven = false;
        }
    }

    return allEven || (minVal % 2 !== 0);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $nums1
     * @return Boolean
     */
    function uniformArray($nums1) {
        $n = count($nums1);
        if ($n === 0) return true;

        $minVal = $nums1[0];
        $allEven = true;

        foreach ($nums1 as $x) {
            if ($x < $minVal) {
                $minVal = $x;
            }
            if ($x % 2 !== 0) {
                $allEven = false;
            }
        }

        return $allEven || ($minVal % 2 !== 0);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func uniformArray(_ nums1: [Int]) -> Bool {
        guard !nums1.isEmpty else { return true }

        var minVal = nums1[0]
        var allEven = true

        for x in nums1 {
            if x < minVal {
                minVal = x
            }
            if x % 2 != 0 {
                allEven = false
            }
        }

        return allEven || (minVal % 2 != 0)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun uniformArray(nums1: IntArray): Boolean {
        var minOdd = Long.MAX_VALUE
        var minEven = Long.MAX_VALUE
        var hasOdd = false
        var hasEven = false

        for (num in nums1) {
            if (num % 2 != 0) {
                if (num.toLong() < minOdd) {
                    minOdd = num.toLong()
                }
                hasOdd = true
            } else {
                if (num.toLong() < minEven) {
                    minEven = num.toLong()
                }
                hasEven = true
            }
        }

        if (!hasOdd || !hasEven) {
            return true
        }
        return minOdd < minEven
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool uniformArray(List<int> nums1) {
    int minOdd = 2000000001;
    int minEven = 2000000001;
    bool hasOdd = false;
    bool hasEven = false;

    for (int num in nums1) {
      if (num % 2 != 0) {
        if (num < minOdd) minOdd = num;
        hasOdd = true;
      } else {
        if (num < minEven) minEven = num;
        hasEven = true;
      }
    }

    if (!hasOdd || !hasEven) {
      return true;
    }
    return minOdd < minEven;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func uniformArray(nums1 []int) bool {
    var minOdd, minEven int
    var hasOdd, hasEven bool

    for _, num := range nums1 {
        if num%2 != 0 {
            if !hasOdd || num < minOdd {
                minOdd = num
                hasOdd = true
            }
        } else {
            if !hasEven || num < minEven {
                minEven = num
                hasEven = true
            }
        }
    }

    if !hasOdd || !hasEven {
        return true
    }
    return minOdd < minEven
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums1
# @return {Boolean}
def uniform_array(nums1)
  min_odd = nil
  min_even = nil

  nums1.each do |num|
    if num % 2 != 0
      if min_odd.nil? || num < min_odd
        min_odd = num
      end
    else
      if min_even.nil? || num < min_even
        min_even = num
      end
    end
  end

  return true if min_odd.nil? || min_even.nil?
  min_odd < min_even
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def uniformArray(nums1: Array[Int]): Boolean = {
        var minOdd = Long.MaxValue
        var minEven = Long.MaxValue
        var hasOdd = false
        var hasEven = false

        for (num <- nums1) {
            if (num % 2 != 0) {
                if (num.toLong < minOdd) minOdd = num.toLong
                hasOdd = true
            } else {
                if (num.toLong < minEven) minEven = num.toLong
                hasEven = true
            }
        }

        if (!hasOdd || !hasEven) {
            true
        } else {
            minOdd < minEven
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
    pub fn uniform_array(nums1: Vec<i32>) -> bool {
        let min_val = *nums1.iter().min().unwrap();
        if min_val % 2 != 0 {
            true
        } else {
            nums1.iter().all(|&x| x % 2 == 0)
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (uniform-array nums1)
  (-> (listof exact-integer?) boolean?)
  (let ([min-val (apply min nums1)])
    (if (odd? min-val)
        #t
        (andmap even? nums1))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
uniform_array(Nums1) ->
  MinVal = lists:min(Nums1),
  case MinVal rem 2 of
    1 -> true;
    0 -> lists:all(fun(X) -> X rem 2 =:= 0 end, Nums1)
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec uniform_array(nums1 :: [integer]) :: boolean
  def uniform_array(nums1) do
    min_val = Enum.min(nums1)
    if rem(min_val, 2) != 0 do
      true
    else
      Enum.all?(nums1, fn x -> rem(x, 2) == 0 end)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) with one-paragraph explanation: The algorithm requires a single pass through the array to determine the minimum element and check if any element in the array is odd. Both operations are linear with respect to the number of elements in the input array.
- **Space Complexity:** O(1) with one-paragraph explanation: The solution only uses a few scalar variables to store the minimum value and a boolean flag, regardless of the size of the input array.
