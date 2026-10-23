---
layout: post
title: "Maximum K to Sort a Permutation"
date: 2026-10-23 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Bit Manipulation"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/maximum-k-to-sort-a-permutation/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int sortPermutation(vector<int>& nums) {\n\
        \        int res = -1;\n        int n = nums.size();\n        for (int i = 0;\
        \ i < n; i++) {\n            if (nums[i] != i) {\n                if (res ==\
        \ -1) {\n                    res = nums[i];\n                } else {\n    \
        \                res &= nums[i];\n                }\n            }\n       \
        \ }\n        return (res == -1) ? 0 : res;\n    }\n};"
      java: "class Solution {\n    public int sortPermutation(int[] nums) {\n      \
        \  int res = -1;\n        for (int i = 0; i < nums.length; i++) {\n        \
        \    if (nums[i] != i) {\n                if (res == -1) {\n               \
        \     res = nums[i];\n                } else {\n                    res &= nums[i];\n\
        \                }\n            }\n        }\n        return (res == -1) ? 0\
        \ : res;\n    }\n}"
      python: "class Solution(object):\n    def sortPermutation(self, nums):\n     \
        \   \"\"\"\n        :type nums: List[int]\n        :rtype: int\n        \"\"\
        \"\n        res = -1\n        for i in range(len(nums)):\n            if nums[i]\
        \ != i:\n                if res == -1:\n                    res = nums[i]\n\
        \                else:\n                    res &= nums[i]\n        return res\
        \ if res != -1 else 0"
      python3: "from typing import List\n\nclass Solution:\n    def sortPermutation(self,\
        \ nums: List[int]) -> int:\n        res = -1\n        for i in range(len(nums)):\n\
        \            if nums[i] != i:\n                if res == -1:\n             \
        \       res = nums[i]\n                else:\n                    res &= nums[i]\n\
        \        return res if res != -1 else 0"
      c: "int sortPermutation(int* nums, int numsSize) {\n    int res = -1;\n    for\
        \ (int i = 0; i < numsSize; i++) {\n        if (nums[i] != i) {\n          \
        \  if (res == -1) {\n                res = nums[i];\n            } else {\n\
        \                res &= nums[i];\n            }\n        }\n    }\n    return\
        \ (res == -1) ? 0 : res;\n}"
      csharp: "public class Solution {\n    public int SortPermutation(int[] nums) {\n\
        \        int res = -1;\n        for (int i = 0; i < nums.Length; i++) {\n  \
        \          if (nums[i] != i) {\n                if (res == -1) {\n         \
        \           res = nums[i];\n                } else {\n                    res\
        \ &= nums[i];\n                }\n            }\n        }\n        return res\
        \ == -1 ? 0 : res;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar sortPermutation\
        \ = function(nums) {\n    let res = -1;\n    for (let i = 0; i < nums.length;\
        \ i++) {\n        if (nums[i] !== i) {\n            if (res === -1) {\n    \
        \            res = nums[i];\n            } else {\n                res &= nums[i];\n\
        \            }\n        }\n    }\n    return res === -1 ? 0 : res;\n};"
      typescript: "function sortPermutation(nums: number[]): number {\n    let res:\
        \ number = -1;\n    for (let i = 0; i < nums.length; i++) {\n        if (nums[i]\
        \ !== i) {\n            if (res === -1) {\n                res = nums[i];\n\
        \            } else {\n                res &= nums[i];\n            }\n    \
        \    }\n    }\n    return res === -1 ? 0 : res;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function sortPermutation($nums) {\n        $res = -1;\n\
        \        $n = count($nums);\n        for ($i = 0; $i < $n; $i++) {\n       \
        \     if ($nums[$i] != $i) {\n                if ($res == -1) {\n          \
        \          $res = $nums[$i];\n                } else {\n                   \
        \ $res &= $nums[$i];\n                }\n            }\n        }\n        return\
        \ $res == -1 ? 0 : $res;\n    }\n}"
      swift: "class Solution {\n    func sortPermutation(_ nums: [Int]) -> Int {\n \
        \       var res = -1\n        let n = nums.count\n        for i in 0..<n {\n\
        \            if nums[i] != i {\n                if res == -1 {\n           \
        \         res = nums[i]\n                } else {\n                    res &=\
        \ nums[i]\n                }\n            }\n        }\n        return res ==\
        \ -1 ? 0 : res\n    }\n}"
      kotlin: "class Solution {\n    fun sortPermutation(nums: IntArray): Int {\n  \
        \      var ans = -1\n        for (i in nums.indices) {\n            if (nums[i]\
        \ != i) {\n                if (ans == -1) {\n                    ans = nums[i]\n\
        \                } else {\n                    ans = ans and nums[i]\n     \
        \           }\n            }\n        }\n        return if (ans == -1) 0 else\
        \ ans\n    }\n}"
      dart: "class Solution {\n  int sortPermutation(List<int> nums) {\n    int ans\
        \ = -1;\n    for (int i = 0; i < nums.length; i++) {\n      if (nums[i] != i)\
        \ {\n        if (ans == -1) {\n          ans = nums[i];\n        } else {\n\
        \          ans &= nums[i];\n        }\n      }\n    }\n    return ans == -1\
        \ ? 0 : ans;\n  }\n}"
      go: "func sortPermutation(nums []int) int {\n    ans := -1\n    for i, v := range\
        \ nums {\n        if v != i {\n            if ans == -1 {\n                ans\
        \ = v\n            } else {\n                ans &= v\n            }\n     \
        \   }\n    }\n    if ans == -1 {\n        return 0\n    }\n    return ans\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef sort_permutation(nums)\n\
        \  ans = -1\n  nums.each_with_index do |v, i|\n    if v != i\n      if ans ==\
        \ -1\n        ans = v\n      else\n        ans &= v\n      end\n    end\n  end\n\
        \  ans == -1 ? 0 : ans\nend"
      scala: "object Solution {\n    def sortPermutation(nums: Array[Int]): Int = {\n\
        \        var ans = -1\n        for (i <- nums.indices) {\n            if (nums(i)\
        \ != i) {\n                if (ans == -1) {\n                    ans = nums(i)\n\
        \                } else {\n                    ans &= nums(i)\n            \
        \    }\n            }\n        }\n        if (ans == -1) 0 else ans\n    }\n\
        }"
      rust: "impl Solution {\n    pub fn sort_permutation(nums: Vec<i32>) -> i32 {\n\
        \        let mut ans: Option<i32> = None;\n        for (i, &num) in nums.iter().enumerate()\
        \ {\n            if num != i as i32 {\n                ans = Some(match ans\
        \ {\n                    None => num,\n                    Some(current_and)\
        \ => current_and & num,\n                });\n            }\n        }\n   \
        \     ans.unwrap_or(0)\n    }\n}"
      racket: "(define/contract (sort-permutation nums)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let loop ([ns nums] [idx 0] [res #f])\n    (if (null?\
        \ ns)\n        (if (not res) 0 res)\n        (let ([num (car ns)])\n       \
        \   (if (not (= num idx))\n              (loop (cdr ns) (+ idx 1) (if (not res)\
        \ num (bitwise-and res num)))\n              (loop (cdr ns) (+ idx 1) res))))))"
      erlang: "-spec sort_permutation(Nums :: [integer()]) -> integer().\nsort_permutation(Nums)\
        \ ->\n    {_, Res} = lists:foldl(\n        fun(Num, {Idx, Acc}) ->\n       \
        \     if\n                Num =/= Idx ->\n                    NewAcc = if Acc\
        \ =:= undefined -> Num; true -> Acc band Num end,\n                    {Idx\
        \ + 1, NewAcc};\n                true ->\n                    {Idx + 1, Acc}\n\
        \            end\n        end,\n        {0, undefined},\n        Nums\n    ),\n\
        \    case Res of\n        undefined -> 0;\n        _ -> Res\n    end."
      elixir: "defmodule Solution do\n  import Bitwise\n  @spec sort_permutation(nums\
        \ :: [integer]) :: integer\n  def sort_permutation(nums) do\n    {_idx, res}\
        \ = Enum.reduce(nums, {0, nil}, fn num, {idx, acc} ->\n      if num != idx do\n\
        \        new_acc = if acc == nil, do: num, else: acc &&& num\n        {idx +\
        \ 1, new_acc}\n      else\n        {idx + 1, acc}\n      end\n    end)\n   \
        \ if res == nil, do: 0, else: res\n  end\nend"
    approach: 'The algorithm identifies the largest possible value of $k$ by finding
      the bitwise AND of all elements that are not in their correct positions. In a
      permutation of $0$ to $n - 1$, any element $v$ that is not at its correct index
      $i$ (i.e., $nums[i] \neq i$) must eventually be swapped. For any swap between
      $nums[i]$ and $nums[j]$ to occur, the condition $nums[i] \text{ AND } nums[j]
      = k$ must be satisfied, which implies that $k$ must be a bitwise submask of both
      $nums[i]$ and $nums[j]$. Consequently, $k$ must be a bitwise submask of every
      element that needs to be moved.


      The maximum such $k$ is exactly the bitwise AND of all misplaced elements. Because
      the input is a permutation, the set of misplaced values is identical to the set
      of misplaced indices, ensuring the value $k$ itself exists somewhere in the array
      (either as a misplaced value or a correctly placed one). This value $k$ can then
      act as a ''hub'' for swaps: for any misplaced value $v$, $v \text{ AND } k = k$,
      allowing $v$ to be swapped with the value $k$. This property guarantees that we
      can sort the misplaced elements into their correct positions using the value $k$
      as an intermediate. If the array is already sorted, the result is 0 per the problem
      requirements.'
    time_complexity: O(n) where n is the length of the input array. We traverse the
      array exactly once to identify misplaced elements and calculate their bitwise
      AND.
    space_complexity: O(1) as the algorithm only uses a few integer variables to store
      the bitwise AND result and the loop index, regardless of the input size.
    elapsed_time: 651.9914646148682
    model: gemini-3-flash-preview
    generated_at: '2026-10-23 02:58:03 '
---

## Problem #3644: Maximum K to Sort a Permutation

**Difficulty:** Medium

**Topics:** Array, Bit Manipulation

## Problem Description

<p>You are given an integer array <code>nums</code> of length <code>n</code>, where <code>nums</code> is a <strong><span data-keyword="permutation-array">permutation</span></strong> of the numbers in the range <code>[0..n - 1]</code>.</p>

<p>You may swap elements at indices <code>i</code> and <code>j</code> <strong>only if</strong> <code>nums[i] AND nums[j] == k</code>, where <code>AND</code> denotes the bitwise AND operation and <code>k</code> is a <strong>non-negative</strong> integer.</p>

<p>Return the <strong>maximum</strong> value of <code>k</code> such that the array can be sorted in <strong>non-decreasing</strong> order using any number of such swaps. If <code>nums</code> is already sorted, return 0.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [0,3,2,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>Choose <code>k = 1</code>. Swapping <code>nums[1] = 3</code> and <code>nums[3] = 1</code> is allowed since <code>nums[1] AND nums[3] == 1</code>, resulting in a sorted permutation: <code>[0, 1, 2, 3]</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [0,1,3,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>Choose <code>k = 2</code>. Swapping <code>nums[2] = 3</code> and <code>nums[3] = 2</code> is allowed since <code>nums[2] AND nums[3] == 2</code>, resulting in a sorted permutation: <code>[0, 1, 2, 3]</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,2,1,0]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>Only <code>k = 0</code> allows sorting since no greater <code>k</code> allows the required swaps where <code>nums[i] AND nums[j] == k</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= n - 1</code></li>
	<li><code>nums</code> is a permutation of integers from <code>0</code> to <code>n - 1</code>.</li>
</ul>


## Hints

1. Take the bitwise AND of all elements that are not in their correct position.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm identifies the largest possible value of $k$ by finding the bitwise AND of all elements that are not in their correct positions. In a permutation of $0$ to $n - 1$, any element $v$ that is not at its correct index $i$ (i.e., $nums[i] \neq i$) must eventually be swapped. For any swap between $nums[i]$ and $nums[j]$ to occur, the condition $nums[i] \text{ AND } nums[j] = k$ must be satisfied, which implies that $k$ must be a bitwise submask of both $nums[i]$ and $nums[j]$. Consequently, $k$ must be a bitwise submask of every element that needs to be moved.

The maximum such $k$ is exactly the bitwise AND of all misplaced elements. Because the input is a permutation, the set of misplaced values is identical to the set of misplaced indices, ensuring the value $k$ itself exists somewhere in the array (either as a misplaced value or a correctly placed one). This value $k$ can then act as a 'hub' for swaps: for any misplaced value $v$, $v \text{ AND } k = k$, allowing $v$ to be swapped with the value $k$. This property guarantees that we can sort the misplaced elements into their correct positions using the value $k$ as an intermediate. If the array is already sorted, the result is 0 per the problem requirements.

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
    int sortPermutation(vector<int>& nums) {
        int res = -1;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            if (nums[i] != i) {
                if (res == -1) {
                    res = nums[i];
                } else {
                    res &= nums[i];
                }
            }
        }
        return (res == -1) ? 0 : res;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int sortPermutation(int[] nums) {
        int res = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != i) {
                if (res == -1) {
                    res = nums[i];
                } else {
                    res &= nums[i];
                }
            }
        }
        return (res == -1) ? 0 : res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -1
        for i in range(len(nums)):
            if nums[i] != i:
                if res == -1:
                    res = nums[i]
                else:
                    res &= nums[i]
        return res if res != -1 else 0
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        res = -1
        for i in range(len(nums)):
            if nums[i] != i:
                if res == -1:
                    res = nums[i]
                else:
                    res &= nums[i]
        return res if res != -1 else 0
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int sortPermutation(int* nums, int numsSize) {
    int res = -1;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] != i) {
            if (res == -1) {
                res = nums[i];
            } else {
                res &= nums[i];
            }
        }
    }
    return (res == -1) ? 0 : res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int SortPermutation(int[] nums) {
        int res = -1;
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] != i) {
                if (res == -1) {
                    res = nums[i];
                } else {
                    res &= nums[i];
                }
            }
        }
        return res == -1 ? 0 : res;
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
var sortPermutation = function(nums) {
    let res = -1;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== i) {
            if (res === -1) {
                res = nums[i];
            } else {
                res &= nums[i];
            }
        }
    }
    return res === -1 ? 0 : res;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function sortPermutation(nums: number[]): number {
    let res: number = -1;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== i) {
            if (res === -1) {
                res = nums[i];
            } else {
                res &= nums[i];
            }
        }
    }
    return res === -1 ? 0 : res;
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
    function sortPermutation($nums) {
        $res = -1;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] != $i) {
                if ($res == -1) {
                    $res = $nums[$i];
                } else {
                    $res &= $nums[$i];
                }
            }
        }
        return $res == -1 ? 0 : $res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func sortPermutation(_ nums: [Int]) -> Int {
        var res = -1
        let n = nums.count
        for i in 0..<n {
            if nums[i] != i {
                if res == -1 {
                    res = nums[i]
                } else {
                    res &= nums[i]
                }
            }
        }
        return res == -1 ? 0 : res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun sortPermutation(nums: IntArray): Int {
        var ans = -1
        for (i in nums.indices) {
            if (nums[i] != i) {
                if (ans == -1) {
                    ans = nums[i]
                } else {
                    ans = ans and nums[i]
                }
            }
        }
        return if (ans == -1) 0 else ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int sortPermutation(List<int> nums) {
    int ans = -1;
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] != i) {
        if (ans == -1) {
          ans = nums[i];
        } else {
          ans &= nums[i];
        }
      }
    }
    return ans == -1 ? 0 : ans;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func sortPermutation(nums []int) int {
    ans := -1
    for i, v := range nums {
        if v != i {
            if ans == -1 {
                ans = v
            } else {
                ans &= v
            }
        }
    }
    if ans == -1 {
        return 0
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
def sort_permutation(nums)
  ans = -1
  nums.each_with_index do |v, i|
    if v != i
      if ans == -1
        ans = v
      else
        ans &= v
      end
    end
  end
  ans == -1 ? 0 : ans
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def sortPermutation(nums: Array[Int]): Int = {
        var ans = -1
        for (i <- nums.indices) {
            if (nums(i) != i) {
                if (ans == -1) {
                    ans = nums(i)
                } else {
                    ans &= nums(i)
                }
            }
        }
        if (ans == -1) 0 else ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn sort_permutation(nums: Vec<i32>) -> i32 {
        let mut ans: Option<i32> = None;
        for (i, &num) in nums.iter().enumerate() {
            if num != i as i32 {
                ans = Some(match ans {
                    None => num,
                    Some(current_and) => current_and & num,
                });
            }
        }
        ans.unwrap_or(0)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (sort-permutation nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ([ns nums] [idx 0] [res #f])
    (if (null? ns)
        (if (not res) 0 res)
        (let ([num (car ns)])
          (if (not (= num idx))
              (loop (cdr ns) (+ idx 1) (if (not res) num (bitwise-and res num)))
              (loop (cdr ns) (+ idx 1) res))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec sort_permutation(Nums :: [integer()]) -> integer().
sort_permutation(Nums) ->
    {_, Res} = lists:foldl(
        fun(Num, {Idx, Acc}) ->
            if
                Num =/= Idx ->
                    NewAcc = if Acc =:= undefined -> Num; true -> Acc band Num end,
                    {Idx + 1, NewAcc};
                true ->
                    {Idx + 1, Acc}
            end
        end,
        {0, undefined},
        Nums
    ),
    case Res of
        undefined -> 0;
        _ -> Res
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  import Bitwise
  @spec sort_permutation(nums :: [integer]) :: integer
  def sort_permutation(nums) do
    {_idx, res} = Enum.reduce(nums, {0, nil}, fn num, {idx, acc} ->
      if num != idx do
        new_acc = if acc == nil, do: num, else: acc &&& num
        {idx + 1, new_acc}
      else
        {idx + 1, acc}
      end
    end)
    if res == nil, do: 0, else: res
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the input array. We traverse the array exactly once to identify misplaced elements and calculate their bitwise AND.
- **Space Complexity:** O(1) as the algorithm only uses a few integer variables to store the bitwise AND result and the loop index, regardless of the input size.
