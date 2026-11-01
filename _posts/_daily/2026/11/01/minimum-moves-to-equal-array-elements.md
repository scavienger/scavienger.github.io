---
layout: post
title: "Minimum Moves to Equal Array Elements"
date: 2026-11-01 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Math"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minMoves(vector<int>& nums) {\n     \
        \   int minVal = nums[0];\n        for (int num : nums) {\n            if (num\
        \ < minVal) {\n                minVal = num;\n            }\n        }\n   \
        \     long long moves = 0;\n        for (int num : nums) {\n            moves\
        \ += (num - minVal);\n        }\n        return (int)moves;\n    }\n};"
      java: "class Solution {\n    public int minMoves(int[] nums) {\n        int minVal\
        \ = nums[0];\n        for (int num : nums) {\n            if (num < minVal)\
        \ {\n                minVal = num;\n            }\n        }\n        long moves\
        \ = 0;\n        for (int num : nums) {\n            moves += (long)num - minVal;\n\
        \        }\n        return (int)moves;\n    }\n}"
      python: "class Solution(object):\n    def minMoves(self, nums):\n        \"\"\"\
        \n        :type nums: List[int]\n        :rtype: int\n        \"\"\"\n     \
        \   min_val = min(nums)\n        moves = 0\n        for num in nums:\n     \
        \       moves += (num - min_val)\n        return moves"
      python3: "class Solution:\n    def minMoves(self, nums: list[int]) -> int:\n \
        \       min_val = min(nums)\n        moves = 0\n        for num in nums:\n \
        \           moves += num - min_val\n        return moves"
      c: "int minMoves(int* nums, int numsSize) {\n    int minVal = nums[0];\n    for\
        \ (int i = 1; i < numsSize; i++) {\n        if (nums[i] < minVal) {\n      \
        \      minVal = nums[i];\n        }\n    }\n    long long moves = 0;\n    for\
        \ (int i = 0; i < numsSize; i++) {\n        moves += (long long)nums[i] - minVal;\n\
        \    }\n    return (int)moves;\n}"
      csharp: "public class Solution {\n    public int MinMoves(int[] nums) {\n    \
        \    if (nums == null || nums.Length == 0) return 0;\n        int min = nums[0];\n\
        \        for (int i = 1; i < nums.Length; i++) {\n            if (nums[i] <\
        \ min) {\n                min = nums[i];\n            }\n        }\n       \
        \ int moves = 0;\n        for (int i = 0; i < nums.Length; i++) {\n        \
        \    moves += nums[i] - min;\n        }\n        return moves;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar minMoves\
        \ = function(nums) {\n    if (nums.length === 0) return 0;\n    let min = nums[0];\n\
        \    for (let i = 1; i < nums.length; i++) {\n        if (nums[i] < min) {\n\
        \            min = nums[i];\n        }\n    }\n    let moves = 0;\n    for (let\
        \ i = 0; i < nums.length; i++) {\n        moves += nums[i] - min;\n    }\n \
        \   return moves;\n};"
      typescript: "function minMoves(nums: number[]): number {\n    if (nums.length\
        \ === 0) return 0;\n    let min = nums[0];\n    for (let i = 1; i < nums.length;\
        \ i++) {\n        if (nums[i] < min) {\n            min = nums[i];\n       \
        \ }\n    }\n    let moves = 0;\n    for (let i = 0; i < nums.length; i++) {\n\
        \        moves += nums[i] - min;\n    }\n    return moves;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function minMoves($nums) {\n        if (empty($nums))\
        \ return 0;\n        $min = $nums[0];\n        foreach ($nums as $num) {\n \
        \           if ($num < $min) {\n                $min = $num;\n            }\n\
        \        }\n        $moves = 0;\n        foreach ($nums as $num) {\n       \
        \     $moves += ($num - $min);\n        }\n        return $moves;\n    }\n}"
      swift: "class Solution {\n    func minMoves(_ nums: [Int]) -> Int {\n        guard\
        \ !nums.isEmpty else { return 0 }\n        var minVal = nums[0]\n        for\
        \ num in nums {\n            if num < minVal {\n                minVal = num\n\
        \            }\n        }\n        var moves = 0\n        for num in nums {\n\
        \            moves += (num - minVal)\n        }\n        return moves\n    }\n\
        }"
      kotlin: "class Solution {\n    fun minMoves(nums: IntArray): Int {\n        var\
        \ minVal = nums[0]\n        for (num in nums) {\n            if (num < minVal)\
        \ {\n                minVal = num\n            }\n        }\n        var moves\
        \ = 0\n        for (num in nums) {\n            moves += num - minVal\n    \
        \    }\n        return moves\n    }\n}"
      dart: "class Solution {\n  int minMoves(List<int> nums) {\n    int minVal = nums[0];\n\
        \    for (int i = 1; i < nums.length; i++) {\n      if (nums[i] < minVal) {\n\
        \        minVal = nums[i];\n      }\n    }\n    int moves = 0;\n    for (int\
        \ num in nums) {\n      moves += num - minVal;\n    }\n    return moves;\n \
        \ }\n}"
      go: "func minMoves(nums []int) int {\n    minVal := nums[0]\n    for _, num :=\
        \ range nums {\n        if num < minVal {\n            minVal = num\n      \
        \  }\n    }\n    moves := 0\n    for _, num := range nums {\n        moves +=\
        \ num - minVal\n    }\n    return moves\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef min_moves(nums)\n \
        \ min_val = nums.min\n  moves = 0\n  nums.each do |num|\n    moves += num -\
        \ min_val\n  end\n  moves\nend"
      scala: "object Solution {\n    def minMoves(nums: Array[Int]): Int = {\n     \
        \   val minVal = nums.min\n        var moves = 0\n        for (num <- nums)\
        \ {\n            moves += (num - minVal)\n        }\n        moves\n    }\n}"
      rust: "impl Solution {\n    pub fn min_moves(nums: Vec<i32>) -> i32 {\n      \
        \  let min_val = *nums.iter().min().unwrap();\n        nums.iter().map(|&x|\
        \ x - min_val).sum()\n    }\n}"
      racket: "(define/contract (min-moves nums)\n  (-> (listof exact-integer?) exact-integer?)\n\
        \  (let ([min-val (foldl min (car nums) (cdr nums))])\n    (foldl (lambda (x\
        \ acc) (+ acc (- x min-val))) 0 nums)))"
      erlang: "-spec min_moves(Nums :: [integer()]) -> integer().\nmin_moves(Nums) ->\n\
        \  MinVal = lists:min(Nums),\n  lists:foldl(fun(X, Acc) -> Acc + (X - MinVal)\
        \ end, 0, Nums)."
      elixir: "defmodule Solution do\n  @spec min_moves(nums :: [integer]) :: integer\n\
        \  def min_moves(nums) do\n    min_val = Enum.min(nums)\n    Enum.reduce(nums,\
        \ 0, fn x, acc -> acc + (x - min_val) end)\n  end\nend"
    approach: 'The problem asks for the minimum moves to make all elements equal by
      incrementing n-1 elements by 1 in each move. Mathematically, incrementing n-1
      elements by 1 is equivalent to decrementing a single element by 1 in terms of
      the relative differences between numbers. Thus, the minimum number of moves required
      to make all elements equal is the same as the total number of operations needed
      to reduce every element in the array down to the initial minimum value found in
      the input.


      To implement this, we first identify the minimum element in the array. We then
      iterate through each element and calculate the difference between that element
      and the minimum value, accumulating these differences into a total sum. This total
      sum represents the number of moves required to reach equality. This approach is
      highly efficient, requiring only linear time and constant extra space, and it
      avoids the need for any complex simulation of the incrementing process.'
    time_complexity: 'O(n) where n is the number of elements in the array. This is because
      we perform two linear passes: one to find the minimum element and another to calculate
      the sum of differences between each element and that minimum.'
    space_complexity: O(1) because we only use a constant amount of extra space for
      variables to store the minimum value and the cumulative move count, regardless
      of the size of the input array.
    elapsed_time: 131.52342557907104
    model: gemini-3-flash-preview
    generated_at: '2026-11-01 03:39:32 '
---

## Problem #453: Minimum Moves to Equal Array Elements

**Difficulty:** Medium

**Topics:** Array, Math

## Problem Description

<p>Given an integer array <code>nums</code> of size <code>n</code>, return <em>the minimum number of moves required to make all array elements equal</em>.</p>

<p>In one move, you can increment <code>n - 1</code> elements of the array by <code>1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Only three moves are needed (remember each move increments two elements):
[1,2,3]  =&gt;  [2,3,3]  =&gt;  [3,4,3]  =&gt;  [4,4,4]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li>The answer is guaranteed to fit in a <strong>32-bit</strong> integer.</li>
</ul>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the minimum moves to make all elements equal by incrementing n-1 elements by 1 in each move. Mathematically, incrementing n-1 elements by 1 is equivalent to decrementing a single element by 1 in terms of the relative differences between numbers. Thus, the minimum number of moves required to make all elements equal is the same as the total number of operations needed to reduce every element in the array down to the initial minimum value found in the input.

To implement this, we first identify the minimum element in the array. We then iterate through each element and calculate the difference between that element and the minimum value, accumulating these differences into a total sum. This total sum represents the number of moves required to reach equality. This approach is highly efficient, requiring only linear time and constant extra space, and it avoids the need for any complex simulation of the incrementing process.

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
    int minMoves(vector<int>& nums) {
        int minVal = nums[0];
        for (int num : nums) {
            if (num < minVal) {
                minVal = num;
            }
        }
        long long moves = 0;
        for (int num : nums) {
            moves += (num - minVal);
        }
        return (int)moves;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minMoves(int[] nums) {
        int minVal = nums[0];
        for (int num : nums) {
            if (num < minVal) {
                minVal = num;
            }
        }
        long moves = 0;
        for (int num : nums) {
            moves += (long)num - minVal;
        }
        return (int)moves;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = min(nums)
        moves = 0
        for num in nums:
            moves += (num - min_val)
        return moves
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_val = min(nums)
        moves = 0
        for num in nums:
            moves += num - min_val
        return moves
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int minMoves(int* nums, int numsSize) {
    int minVal = nums[0];
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] < minVal) {
            minVal = nums[i];
        }
    }
    long long moves = 0;
    for (int i = 0; i < numsSize; i++) {
        moves += (long long)nums[i] - minVal;
    }
    return (int)moves;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinMoves(int[] nums) {
        if (nums == null || nums.Length == 0) return 0;
        int min = nums[0];
        for (int i = 1; i < nums.Length; i++) {
            if (nums[i] < min) {
                min = nums[i];
            }
        }
        int moves = 0;
        for (int i = 0; i < nums.Length; i++) {
            moves += nums[i] - min;
        }
        return moves;
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
var minMoves = function(nums) {
    if (nums.length === 0) return 0;
    let min = nums[0];
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] < min) {
            min = nums[i];
        }
    }
    let moves = 0;
    for (let i = 0; i < nums.length; i++) {
        moves += nums[i] - min;
    }
    return moves;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minMoves(nums: number[]): number {
    if (nums.length === 0) return 0;
    let min = nums[0];
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] < min) {
            min = nums[i];
        }
    }
    let moves = 0;
    for (let i = 0; i < nums.length; i++) {
        moves += nums[i] - min;
    }
    return moves;
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
    function minMoves($nums) {
        if (empty($nums)) return 0;
        $min = $nums[0];
        foreach ($nums as $num) {
            if ($num < $min) {
                $min = $num;
            }
        }
        $moves = 0;
        foreach ($nums as $num) {
            $moves += ($num - $min);
        }
        return $moves;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minMoves(_ nums: [Int]) -> Int {
        guard !nums.isEmpty else { return 0 }
        var minVal = nums[0]
        for num in nums {
            if num < minVal {
                minVal = num
            }
        }
        var moves = 0
        for num in nums {
            moves += (num - minVal)
        }
        return moves
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minMoves(nums: IntArray): Int {
        var minVal = nums[0]
        for (num in nums) {
            if (num < minVal) {
                minVal = num
            }
        }
        var moves = 0
        for (num in nums) {
            moves += num - minVal
        }
        return moves
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minMoves(List<int> nums) {
    int minVal = nums[0];
    for (int i = 1; i < nums.length; i++) {
      if (nums[i] < minVal) {
        minVal = nums[i];
      }
    }
    int moves = 0;
    for (int num in nums) {
      moves += num - minVal;
    }
    return moves;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minMoves(nums []int) int {
    minVal := nums[0]
    for _, num := range nums {
        if num < minVal {
            minVal = num
        }
    }
    moves := 0
    for _, num := range nums {
        moves += num - minVal
    }
    return moves
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def min_moves(nums)
  min_val = nums.min
  moves = 0
  nums.each do |num|
    moves += num - min_val
  end
  moves
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minMoves(nums: Array[Int]): Int = {
        val minVal = nums.min
        var moves = 0
        for (num <- nums) {
            moves += (num - minVal)
        }
        moves
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_moves(nums: Vec<i32>) -> i32 {
        let min_val = *nums.iter().min().unwrap();
        nums.iter().map(|&x| x - min_val).sum()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-moves nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ([min-val (foldl min (car nums) (cdr nums))])
    (foldl (lambda (x acc) (+ acc (- x min-val))) 0 nums)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_moves(Nums :: [integer()]) -> integer().
min_moves(Nums) ->
  MinVal = lists:min(Nums),
  lists:foldl(fun(X, Acc) -> Acc + (X - MinVal) end, 0, Nums).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_moves(nums :: [integer]) :: integer
  def min_moves(nums) do
    min_val = Enum.min(nums)
    Enum.reduce(nums, 0, fn x, acc -> acc + (x - min_val) end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the number of elements in the array. This is because we perform two linear passes: one to find the minimum element and another to calculate the sum of differences between each element and that minimum.
- **Space Complexity:** O(1) because we only use a constant amount of extra space for variables to store the minimum value and the cumulative move count, regardless of the size of the input array.
