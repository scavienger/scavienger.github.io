---
layout: post
title: "Check If All 1's Are at Least Length K Places Away"
date: 2025-11-17 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool kLengthApart(vector<int>& nums, int\
        \ k) {\n        int previous = -1;\n        for (int i = 0; i < nums.size();\
        \ ++i) {\n            if (nums[i] == 1) {\n                if (previous != -1\
        \ && i - previous <= k) {\n                    return false;\n             \
        \   }\n                previous = i;\n            }\n        }\n        return\
        \ true;\n    }\n};"
      java: "class Solution {\n    public boolean kLengthApart(int[] nums, int k) {\n\
        \        int previous = -1;\n        for (int i = 0; i < nums.length; i++) {\n\
        \            if (nums[i] == 1) {\n                if (previous != -1 && i -\
        \ previous <= k) {\n                    return false;\n                }\n \
        \               previous = i;\n            }\n        }\n        return true;\n\
        \    }\n}"
      python: "class Solution(object):\n    def kLengthApart(self, nums, k):\n     \
        \   \"\"\"\n        :type nums: List[int]\n        :type k: int\n        :rtype:\
        \ bool\n        \"\"\"\n        previous = -1\n        for i, value in enumerate(nums):\n\
        \            if value == 1:\n                if previous != -1 and i - previous\
        \ <= k:\n                    return False\n                previous = i\n  \
        \      return True"
      python3: "class Solution:\n    def kLengthApart(self, nums: list[int], k: int)\
        \ -> bool:\n        previous = -1\n        for i, value in enumerate(nums):\n\
        \            if value == 1:\n                if previous != -1 and i - previous\
        \ <= k:\n                    return False\n                previous = i\n  \
        \      return True"
      c: "bool kLengthApart(int* nums, int numsSize, int k) {\n    int previous = -1;\n\
        \    for (int i = 0; i < numsSize; ++i) {\n        if (nums[i] == 1) {\n   \
        \         if (previous != -1 && i - previous <= k) {\n                return\
        \ false;\n            }\n            previous = i;\n        }\n    }\n    return\
        \ true;\n}"
      csharp: "public class Solution {\n    public bool KLengthApart(int[] nums, int\
        \ k) {\n        int previous = -1;\n        for (int i = 0; i < nums.Length;\
        \ i++) {\n            if (nums[i] == 1) {\n                if (previous != -1\
        \ && i - previous <= k) {\n                    return false;\n             \
        \   }\n                previous = i;\n            }\n        }\n        return\
        \ true;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} k\n * @return\
        \ {boolean}\n */\nvar kLengthApart = function(nums, k) {\n    let previous =\
        \ -1;\n    for (let i = 0; i < nums.length; i++) {\n        if (nums[i] ===\
        \ 1) {\n            if (previous !== -1 && i - previous <= k) {\n          \
        \      return false;\n            }\n            previous = i;\n        }\n\
        \    }\n    return true;\n};"
      typescript: "function kLengthApart(nums: number[], k: number): boolean {\n   \
        \ let previous = -1;\n    for (let i = 0; i < nums.length; i++) {\n        if\
        \ (nums[i] === 1) {\n            if (previous !== -1 && i - previous <= k) {\n\
        \                return false;\n            }\n            previous = i;\n \
        \       }\n    }\n    return true;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer $k\n     * @return Boolean\n     */\n    function kLengthApart($nums,\
        \ $k) {\n        $previous = -1;\n        foreach ($nums as $i => $value) {\n\
        \            if ($value === 1) {\n                if ($previous !== -1 && $i\
        \ - $previous <= $k) {\n                    return false;\n                }\n\
        \                $previous = $i;\n            }\n        }\n        return true;\n\
        \    }\n}"
      swift: "class Solution {\n    func kLengthApart(_ nums: [Int], _ k: Int) -> Bool\
        \ {\n        var previous = -1\n        for (i, value) in nums.enumerated()\
        \ {\n            if value == 1 {\n                if previous != -1 && i - previous\
        \ <= k {\n                    return false\n                }\n            \
        \    previous = i\n            }\n        }\n        return true\n    }\n}"
      kotlin: "class Solution {\n    fun kLengthApart(nums: IntArray, k: Int): Boolean\
        \ {\n        var previous = -1\n        for (i in nums.indices) {\n        \
        \    if (nums[i] == 1) {\n                if (previous != -1 && i - previous\
        \ <= k) {\n                    return false\n                }\n           \
        \     previous = i\n            }\n        }\n        return true\n    }\n}"
      dart: "class Solution {\n  bool kLengthApart(List<int> nums, int k) {\n    var\
        \ previous = -1;\n    for (var i = 0; i < nums.length; i++) {\n      if (nums[i]\
        \ == 1) {\n        if (previous != -1 && i - previous <= k) {\n          return\
        \ false;\n        }\n        previous = i;\n      }\n    }\n    return true;\n\
        \  }\n}"
      go: "func kLengthApart(nums []int, k int) bool {\n\tprevious := -1\n\tfor i, value\
        \ := range nums {\n\t\tif value == 1 {\n\t\t\tif previous != -1 && i-previous\
        \ <= k {\n\t\t\t\treturn false\n\t\t\t}\n\t\t\tprevious = i\n\t\t}\n\t}\n\t\
        return true\n}"
      ruby: "# @param {Integer[]} nums\n# @param {Integer} k\n# @return {Boolean}\n\
        def k_length_apart(nums, k)\n  previous = -1\n  nums.each_with_index do |value,\
        \ i|\n    if value == 1\n      return false if previous != -1 && i - previous\
        \ <= k\n      previous = i\n    end\n  end\n  true\nend"
      scala: "object Solution {\n    def kLengthApart(nums: Array[Int], k: Int): Boolean\
        \ = {\n        var previous = -1\n        var i = 0\n        while (i < nums.length)\
        \ {\n            if (nums(i) == 1) {\n                if (previous != -1 &&\
        \ i - previous <= k) return false\n                previous = i\n          \
        \  }\n            i += 1\n        }\n        true\n    }\n}"
      rust: "impl Solution {\n    pub fn k_length_apart(nums: Vec<i32>, k: i32) -> bool\
        \ {\n        let mut previous: i32 = -1;\n        for (i, value) in nums.iter().enumerate()\
        \ {\n            if *value == 1 {\n                if previous != -1 && i as\
        \ i32 - previous <= k {\n                    return false;\n               \
        \ }\n                previous = i as i32;\n            }\n        }\n      \
        \  true\n    }\n}"
      racket: "(define/contract (k-length-apart nums k)\n  (-> (listof exact-integer?)\
        \ exact-integer? boolean?)\n  (let loop ([remaining nums] [i 0] [previous -1])\n\
        \    (cond\n      [(null? remaining) #t]\n      [(= (car remaining) 1)\n   \
        \    (if (and (not (= previous -1)) (<= (- i previous) k))\n           #f\n\
        \           (loop (cdr remaining) (add1 i) i))]\n      [else (loop (cdr remaining)\
        \ (add1 i) previous)])))"
      erlang: "-spec k_length_apart(Nums :: [integer()], K :: integer()) -> boolean().\n\
        k_length_apart(Nums, K) ->\n  k_length_apart(Nums, K, 0, -1).\n\nk_length_apart([],\
        \ _K, _Index, _Previous) -> true;\nk_length_apart([1 | Rest], K, Index, Previous)\
        \ when Previous =/= -1, Index - Previous =< K -> false;\nk_length_apart([1 |\
        \ Rest], K, Index, _Previous) ->\n  k_length_apart(Rest, K, Index + 1, Index);\n\
        k_length_apart([_ | Rest], K, Index, Previous) ->\n  k_length_apart(Rest, K,\
        \ Index + 1, Previous)."
      elixir: "defmodule Solution do\n  @spec k_length_apart(nums :: [integer], k ::\
        \ integer) :: boolean\n  def k_length_apart(nums, k) do\n    nums\n    |> Enum.with_index()\n\
        \    |> Enum.reduce_while(-1, fn {value, i}, previous ->\n      if value ==\
        \ 1 do\n        if previous != -1 and i - previous <= k do\n          {:halt,\
        \ false}\n        else\n          {:cont, i}\n        end\n      else\n    \
        \    {:cont, previous}\n      end\n    end)\n    |> then(&(&1 != false))\n \
        \ end\nend"
    approach: 'Scan the array from left to right and remember the index of the most
      recently seen 1. When another 1 is found, compare its index with the remembered
      index.


      If the difference between the indices is less than k + 1, the 1s are too close,
      so return false. Otherwise, update the remembered index. If the scan finishes
      without finding a pair that is too close, return true.'
    time_complexity: O(n), where n is the length of nums, because the array is scanned
      once.
    space_complexity: O(1), because only the index of the previous 1 is stored.
    elapsed_time: 48.47818613052368
    model: gpt-6-luna
    generated_at: '2026-11-13 00:04:17 '
---

## Problem #1437: Check If All 1's Are at Least Length K Places Away

**Difficulty:** Easy

**Topics:** Array

## Problem Description

<p>Given an binary array <code>nums</code> and an integer <code>k</code>, return <code>true</code><em> if all </em><code>1</code><em>&#39;s are at least </em><code>k</code><em> places away from each other, otherwise return </em><code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/04/15/sample_1_1791.png" style="width: 428px; height: 181px;" />
<pre>
<strong>Input:</strong> nums = [1,0,0,0,1,0,0,1], k = 2
<strong>Output:</strong> true
<strong>Explanation:</strong> Each of the 1s are at least 2 places away from each other.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/04/15/sample_2_1791.png" style="width: 320px; height: 173px;" />
<pre>
<strong>Input:</strong> nums = [1,0,0,1,0,1], k = 2
<strong>Output:</strong> false
<strong>Explanation:</strong> The second 1 and third 1 are only one apart from each other.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= k &lt;= nums.length</code></li>
	<li><code>nums[i]</code> is <code>0</code> or <code>1</code></li>
</ul>


## Hints

1. Each time you find a number 1, check whether or not it is K or more places away from the next one. If it's not, return false.

## 🤖 AI-Generated Solution (gpt-6-luna)

### Approach

Scan the array from left to right and remember the index of the most recently seen 1. When another 1 is found, compare its index with the remembered index.

If the difference between the indices is less than k + 1, the 1s are too close, so return false. Otherwise, update the remembered index. If the scan finishes without finding a pair that is too close, return true.

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
    bool kLengthApart(vector<int>& nums, int k) {
        int previous = -1;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == 1) {
                if (previous != -1 && i - previous <= k) {
                    return false;
                }
                previous = i;
            }
        }
        return true;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean kLengthApart(int[] nums, int k) {
        int previous = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                if (previous != -1 && i - previous <= k) {
                    return false;
                }
                previous = i;
            }
        }
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        previous = -1
        for i, value in enumerate(nums):
            if value == 1:
                if previous != -1 and i - previous <= k:
                    return False
                previous = i
        return True
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        previous = -1
        for i, value in enumerate(nums):
            if value == 1:
                if previous != -1 and i - previous <= k:
                    return False
                previous = i
        return True
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
bool kLengthApart(int* nums, int numsSize, int k) {
    int previous = -1;
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] == 1) {
            if (previous != -1 && i - previous <= k) {
                return false;
            }
            previous = i;
        }
    }
    return true;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool KLengthApart(int[] nums, int k) {
        int previous = -1;
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == 1) {
                if (previous != -1 && i - previous <= k) {
                    return false;
                }
                previous = i;
            }
        }
        return true;
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
 * @return {boolean}
 */
var kLengthApart = function(nums, k) {
    let previous = -1;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 1) {
            if (previous !== -1 && i - previous <= k) {
                return false;
            }
            previous = i;
        }
    }
    return true;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function kLengthApart(nums: number[], k: number): boolean {
    let previous = -1;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 1) {
            if (previous !== -1 && i - previous <= k) {
                return false;
            }
            previous = i;
        }
    }
    return true;
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
     * @return Boolean
     */
    function kLengthApart($nums, $k) {
        $previous = -1;
        foreach ($nums as $i => $value) {
            if ($value === 1) {
                if ($previous !== -1 && $i - $previous <= $k) {
                    return false;
                }
                $previous = $i;
            }
        }
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func kLengthApart(_ nums: [Int], _ k: Int) -> Bool {
        var previous = -1
        for (i, value) in nums.enumerated() {
            if value == 1 {
                if previous != -1 && i - previous <= k {
                    return false
                }
                previous = i
            }
        }
        return true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun kLengthApart(nums: IntArray, k: Int): Boolean {
        var previous = -1
        for (i in nums.indices) {
            if (nums[i] == 1) {
                if (previous != -1 && i - previous <= k) {
                    return false
                }
                previous = i
            }
        }
        return true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool kLengthApart(List<int> nums, int k) {
    var previous = -1;
    for (var i = 0; i < nums.length; i++) {
      if (nums[i] == 1) {
        if (previous != -1 && i - previous <= k) {
          return false;
        }
        previous = i;
      }
    }
    return true;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func kLengthApart(nums []int, k int) bool {
	previous := -1
	for i, value := range nums {
		if value == 1 {
			if previous != -1 && i-previous <= k {
				return false
			}
			previous = i
		}
	}
	return true
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def k_length_apart(nums, k)
  previous = -1
  nums.each_with_index do |value, i|
    if value == 1
      return false if previous != -1 && i - previous <= k
      previous = i
    end
  end
  true
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def kLengthApart(nums: Array[Int], k: Int): Boolean = {
        var previous = -1
        var i = 0
        while (i < nums.length) {
            if (nums(i) == 1) {
                if (previous != -1 && i - previous <= k) return false
                previous = i
            }
            i += 1
        }
        true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn k_length_apart(nums: Vec<i32>, k: i32) -> bool {
        let mut previous: i32 = -1;
        for (i, value) in nums.iter().enumerate() {
            if *value == 1 {
                if previous != -1 && i as i32 - previous <= k {
                    return false;
                }
                previous = i as i32;
            }
        }
        true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (k-length-apart nums k)
  (-> (listof exact-integer?) exact-integer? boolean?)
  (let loop ([remaining nums] [i 0] [previous -1])
    (cond
      [(null? remaining) #t]
      [(= (car remaining) 1)
       (if (and (not (= previous -1)) (<= (- i previous) k))
           #f
           (loop (cdr remaining) (add1 i) i))]
      [else (loop (cdr remaining) (add1 i) previous)])))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec k_length_apart(Nums :: [integer()], K :: integer()) -> boolean().
k_length_apart(Nums, K) ->
  k_length_apart(Nums, K, 0, -1).

k_length_apart([], _K, _Index, _Previous) -> true;
k_length_apart([1 | Rest], K, Index, Previous) when Previous =/= -1, Index - Previous =< K -> false;
k_length_apart([1 | Rest], K, Index, _Previous) ->
  k_length_apart(Rest, K, Index + 1, Index);
k_length_apart([_ | Rest], K, Index, Previous) ->
  k_length_apart(Rest, K, Index + 1, Previous).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec k_length_apart(nums :: [integer], k :: integer) :: boolean
  def k_length_apart(nums, k) do
    nums
    |> Enum.with_index()
    |> Enum.reduce_while(-1, fn {value, i}, previous ->
      if value == 1 do
        if previous != -1 and i - previous <= k do
          {:halt, false}
        else
          {:cont, i}
        end
      else
        {:cont, previous}
      end
    end)
    |> then(&(&1 != false))
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n), where n is the length of nums, because the array is scanned once.
- **Space Complexity:** O(1), because only the index of the previous 1 is stored.
