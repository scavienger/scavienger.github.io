---
layout: post
title: "Find Minimum Operations to Make All Elements Divisible by Three"
date: 2025-11-22 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Math"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minimumOperations(vector<int>& nums)\
        \ {\n        int operations = 0;\n        for (int num : nums) {\n         \
        \   int remainder = num % 3;\n            operations += min(remainder, 3 - remainder);\n\
        \        }\n        return operations;\n    }\n};"
      java: "class Solution {\n    public int minimumOperations(int[] nums) {\n    \
        \    int operations = 0;\n        for (int num : nums) {\n            int remainder\
        \ = num % 3;\n            operations += Math.min(remainder, 3 - remainder);\n\
        \        }\n        return operations;\n    }\n}"
      python: "class Solution(object):\n    def minimumOperations(self, nums):\n   \
        \     \"\"\"\n        :type nums: List[int]\n        :rtype: int\n        \"\
        \"\"\n        operations = 0\n        for num in nums:\n            remainder\
        \ = num % 3\n            operations += min(remainder, 3 - remainder)\n     \
        \   return operations"
      python3: "class Solution:\n    def minimumOperations(self, nums: List[int]) ->\
        \ int:\n        operations = 0\n        for num in nums:\n            remainder\
        \ = num % 3\n            operations += min(remainder, 3 - remainder)\n     \
        \   return operations"
      c: "int minimumOperations(int* nums, int numsSize) {\n    int operations = 0;\n\
        \    for (int i = 0; i < numsSize; i++) {\n        int remainder = nums[i] %\
        \ 3;\n        operations += remainder < 3 - remainder ? remainder : 3 - remainder;\n\
        \    }\n    return operations;\n}"
      csharp: "public class Solution {\n    public int MinimumOperations(int[] nums)\
        \ {\n        int operations = 0;\n        foreach (int num in nums) {\n    \
        \        int remainder = num % 3;\n            operations += Math.Min(remainder,\
        \ 3 - remainder);\n        }\n        return operations;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar minimumOperations\
        \ = function(nums) {\n    let operations = 0;\n    for (const num of nums) {\n\
        \        const remainder = num % 3;\n        operations += Math.min(remainder,\
        \ 3 - remainder);\n    }\n    return operations;\n};"
      typescript: "function minimumOperations(nums: number[]): number {\n    let operations\
        \ = 0;\n    for (const num of nums) {\n        const remainder = num % 3;\n\
        \        operations += Math.min(remainder, 3 - remainder);\n    }\n    return\
        \ operations;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function minimumOperations($nums) {\n        $operations\
        \ = 0;\n        foreach ($nums as $num) {\n            $remainder = $num % 3;\n\
        \            $operations += min($remainder, 3 - $remainder);\n        }\n  \
        \      return $operations;\n    }\n}"
      swift: "class Solution {\n    func minimumOperations(_ nums: [Int]) -> Int {\n\
        \        var operations = 0\n        for num in nums {\n            let remainder\
        \ = num % 3\n            operations += min(remainder, 3 - remainder)\n     \
        \   }\n        return operations\n    }\n}"
      kotlin: "class Solution {\n    fun minimumOperations(nums: IntArray): Int {\n\
        \        var operations = 0\n        for (num in nums) {\n            val remainder\
        \ = num % 3\n            operations += minOf(remainder, 3 - remainder)\n   \
        \     }\n        return operations\n    }\n}"
      dart: "class Solution {\n  int minimumOperations(List<int> nums) {\n    var operations\
        \ = 0;\n    for (final num in nums) {\n      final remainder = num % 3;\n  \
        \    operations += remainder < 3 - remainder ? remainder : 3 - remainder;\n\
        \    }\n    return operations;\n  }\n}"
      go: "func minimumOperations(nums []int) int {\n    operations := 0\n    for _,\
        \ num := range nums {\n        remainder := num % 3\n        if remainder <\
        \ 3-remainder {\n            operations += remainder\n        } else {\n   \
        \         operations += 3 - remainder\n        }\n    }\n    return operations\n\
        }"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef minimum_operations(nums)\n\
        \  operations = 0\n  nums.each do |num|\n    remainder = num % 3\n    operations\
        \ += [remainder, 3 - remainder].min\n  end\n  operations\nend"
      scala: "object Solution {\n    def minimumOperations(nums: Array[Int]): Int =\
        \ {\n        nums.map { num =>\n            val remainder = num % 3\n      \
        \      remainder.min(3 - remainder)\n        }.sum\n    }\n}"
      rust: "impl Solution {\n    pub fn minimum_operations(nums: Vec<i32>) -> i32 {\n\
        \        nums.iter()\n            .map(|&num| {\n                let remainder\
        \ = num % 3;\n                remainder.min(3 - remainder)\n            })\n\
        \            .sum()\n    }\n}"
      racket: "(define/contract (minimum-operations nums)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (for/sum ([num nums])\n    (let ([remainder (remainder\
        \ num 3)])\n      (min remainder (- 3 remainder)))))"
      erlang: "-spec minimum_operations(Nums :: [integer()]) -> integer().\nminimum_operations(Nums)\
        \ ->\n  lists:sum([begin\n               Remainder = Num rem 3,\n          \
        \     min(Remainder, 3 - Remainder)\n             end || Num <- Nums])."
      elixir: "defmodule Solution do\n  @spec minimum_operations(nums :: [integer])\
        \ :: integer\n  def minimum_operations(nums) do\n    Enum.reduce(nums, 0, fn\
        \ num, operations ->\n      remainder = rem(num, 3)\n      operations + min(remainder,\
        \ 3 - remainder)\n    end)\n  end\nend"
    approach: 'For each number, compute its remainder when divided by 3. If the remainder
      is 0, it already meets the requirement and needs no operations. Otherwise, it
      can be made divisible by 3 by changing it by 1 in the nearer direction.


      Add the smaller of the remainder and 3 minus the remainder to the total for each
      element. Return that total, which is minimal because each element can be adjusted
      independently.'
    time_complexity: O(n), where n is the number of elements, since the algorithm processes
      each element once.
    space_complexity: O(1), since only a running total and temporary values are used.
    elapsed_time: 37.704649209976196
    model: gpt-6-luna
    generated_at: '2026-11-13 00:09:49 '
---

## Problem #3190: Find Minimum Operations to Make All Elements Divisible by Three

**Difficulty:** Easy

**Topics:** Array, Math

## Problem Description

<p>You are given an integer array <code>nums</code>. In one operation, you can add or subtract 1 from <strong>any</strong> element of <code>nums</code>.</p>

<p>Return the <strong>minimum</strong> number of operations to make all elements of <code>nums</code> divisible by 3.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>All array elements can be made divisible by 3 using 3 operations:</p>

<ul>
	<li>Subtract 1 from 1.</li>
	<li>Add 1 to 2.</li>
	<li>Subtract 1 from 4.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,6,9]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 50</code></li>
</ul>


## Hints

1. If `x % 3 != 0` we can always increment or decrement `x` such that we only need 1 operation.

2. Add `min(nums[i] % 3, 3 - (nums[i] % 3))` to the count of operations.

## 🤖 AI-Generated Solution (gpt-6-luna)

### Approach

For each number, compute its remainder when divided by 3. If the remainder is 0, it already meets the requirement and needs no operations. Otherwise, it can be made divisible by 3 by changing it by 1 in the nearer direction.

Add the smaller of the remainder and 3 minus the remainder to the total for each element. Return that total, which is minimal because each element can be adjusted independently.

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
    int minimumOperations(vector<int>& nums) {
        int operations = 0;
        for (int num : nums) {
            int remainder = num % 3;
            operations += min(remainder, 3 - remainder);
        }
        return operations;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minimumOperations(int[] nums) {
        int operations = 0;
        for (int num : nums) {
            int remainder = num % 3;
            operations += Math.min(remainder, 3 - remainder);
        }
        return operations;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        operations = 0
        for num in nums:
            remainder = num % 3
            operations += min(remainder, 3 - remainder)
        return operations
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        for num in nums:
            remainder = num % 3
            operations += min(remainder, 3 - remainder)
        return operations
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int minimumOperations(int* nums, int numsSize) {
    int operations = 0;
    for (int i = 0; i < numsSize; i++) {
        int remainder = nums[i] % 3;
        operations += remainder < 3 - remainder ? remainder : 3 - remainder;
    }
    return operations;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinimumOperations(int[] nums) {
        int operations = 0;
        foreach (int num in nums) {
            int remainder = num % 3;
            operations += Math.Min(remainder, 3 - remainder);
        }
        return operations;
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
var minimumOperations = function(nums) {
    let operations = 0;
    for (const num of nums) {
        const remainder = num % 3;
        operations += Math.min(remainder, 3 - remainder);
    }
    return operations;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimumOperations(nums: number[]): number {
    let operations = 0;
    for (const num of nums) {
        const remainder = num % 3;
        operations += Math.min(remainder, 3 - remainder);
    }
    return operations;
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
    function minimumOperations($nums) {
        $operations = 0;
        foreach ($nums as $num) {
            $remainder = $num % 3;
            $operations += min($remainder, 3 - $remainder);
        }
        return $operations;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minimumOperations(_ nums: [Int]) -> Int {
        var operations = 0
        for num in nums {
            let remainder = num % 3
            operations += min(remainder, 3 - remainder)
        }
        return operations
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minimumOperations(nums: IntArray): Int {
        var operations = 0
        for (num in nums) {
            val remainder = num % 3
            operations += minOf(remainder, 3 - remainder)
        }
        return operations
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minimumOperations(List<int> nums) {
    var operations = 0;
    for (final num in nums) {
      final remainder = num % 3;
      operations += remainder < 3 - remainder ? remainder : 3 - remainder;
    }
    return operations;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minimumOperations(nums []int) int {
    operations := 0
    for _, num := range nums {
        remainder := num % 3
        if remainder < 3-remainder {
            operations += remainder
        } else {
            operations += 3 - remainder
        }
    }
    return operations
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def minimum_operations(nums)
  operations = 0
  nums.each do |num|
    remainder = num % 3
    operations += [remainder, 3 - remainder].min
  end
  operations
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minimumOperations(nums: Array[Int]): Int = {
        nums.map { num =>
            val remainder = num % 3
            remainder.min(3 - remainder)
        }.sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        nums.iter()
            .map(|&num| {
                let remainder = num % 3;
                remainder.min(3 - remainder)
            })
            .sum()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (minimum-operations nums)
  (-> (listof exact-integer?) exact-integer?)
  (for/sum ([num nums])
    (let ([remainder (remainder num 3)])
      (min remainder (- 3 remainder)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec minimum_operations(Nums :: [integer()]) -> integer().
minimum_operations(Nums) ->
  lists:sum([begin
               Remainder = Num rem 3,
               min(Remainder, 3 - Remainder)
             end || Num <- Nums]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_operations(nums :: [integer]) :: integer
  def minimum_operations(nums) do
    Enum.reduce(nums, 0, fn num, operations ->
      remainder = rem(num, 3)
      operations + min(remainder, 3 - remainder)
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n), where n is the number of elements, since the algorithm processes each element once.
- **Space Complexity:** O(1), since only a running total and temporary values are used.
