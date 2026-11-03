---
layout: post
title: "Minimum Moves to Equal Array Elements III"
date: 2026-11-03 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Math"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minMoves(vector<int>& nums) {\n     \
        \   int maxVal = nums[0];\n        for (int num : nums) {\n            if (num\
        \ > maxVal) {\n                maxVal = num;\n            }\n        }\n   \
        \     int totalMoves = 0;\n        for (int num : nums) {\n            totalMoves\
        \ += (maxVal - num);\n        }\n        return totalMoves;\n    }\n};"
      java: "class Solution {\n    public int minMoves(int[] nums) {\n        int maxVal\
        \ = nums[0];\n        for (int num : nums) {\n            if (num > maxVal)\
        \ {\n                maxVal = num;\n            }\n        }\n        int totalMoves\
        \ = 0;\n        for (int num : nums) {\n            totalMoves += (maxVal -\
        \ num);\n        }\n        return totalMoves;\n    }\n}"
      python: "class Solution(object):\n    def minMoves(self, nums):\n        \"\"\"\
        \n        :type nums: List[int]\n        :rtype: int\n        \"\"\"\n     \
        \   max_val = max(nums)\n        total_moves = 0\n        for num in nums:\n\
        \            total_moves += (max_val - num)\n        return total_moves"
      python3: "class Solution:\n    def minMoves(self, nums: List[int]) -> int:\n \
        \       max_val = max(nums)\n        return sum(max_val - num for num in nums)"
      c: "int minMoves(int* nums, int numsSize) {\n    int maxVal = nums[0];\n    for\
        \ (int i = 1; i < numsSize; i++) {\n        if (nums[i] > maxVal) {\n      \
        \      maxVal = nums[i];\n        }\n    }\n    int totalMoves = 0;\n    for\
        \ (int i = 0; i < numsSize; i++) {\n        totalMoves += (maxVal - nums[i]);\n\
        \    }\n    return totalMoves;\n}"
      csharp: "public class Solution {\n    public int MinMoves(int[] nums) {\n    \
        \    int maxVal = nums[0];\n        foreach (int num in nums) {\n          \
        \  if (num > maxVal) {\n                maxVal = num;\n            }\n     \
        \   }\n        int totalMoves = 0;\n        foreach (int num in nums) {\n  \
        \          totalMoves += (maxVal - num);\n        }\n        return totalMoves;\n\
        \    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar minMoves\
        \ = function(nums) {\n    let maxVal = nums[0];\n    for (let i = 1; i < nums.length;\
        \ i++) {\n        if (nums[i] > maxVal) {\n            maxVal = nums[i];\n \
        \       }\n    }\n    let totalMoves = 0;\n    for (let i = 0; i < nums.length;\
        \ i++) {\n        totalMoves += (maxVal - nums[i]);\n    }\n    return totalMoves;\n\
        };"
      typescript: "function minMoves(nums: number[]): number {\n    let maxVal = nums[0];\n\
        \    for (let i = 1; i < nums.length; i++) {\n        if (nums[i] > maxVal)\
        \ {\n            maxVal = nums[i];\n        }\n    }\n    let moves = 0;\n \
        \   for (let i = 0; i < nums.length; i++) {\n        moves += (maxVal - nums[i]);\n\
        \    }\n    return moves;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function minMoves($nums) {\n        $maxVal = $nums[0];\n\
        \        foreach ($nums as $num) {\n            if ($num > $maxVal) {\n    \
        \            $maxVal = $num;\n            }\n        }\n        $moves = 0;\n\
        \        foreach ($nums as $num) {\n            $moves += ($maxVal - $num);\n\
        \        }\n        return $moves;\n    }\n}"
      swift: "class Solution {\n    func minMoves(_ nums: [Int]) -> Int {\n        guard\
        \ let maxVal = nums.max() else { return 0 }\n        var moves = 0\n       \
        \ for num in nums {\n            moves += (maxVal - num)\n        }\n      \
        \  return moves\n    }\n}"
      kotlin: "class Solution {\n    fun minMoves(nums: IntArray): Int {\n        var\
        \ maxVal = nums[0]\n        for (i in 1 until nums.size) {\n            if (nums[i]\
        \ > maxVal) {\n                maxVal = nums[i]\n            }\n        }\n\
        \        var moves = 0\n        for (num in nums) {\n            moves += (maxVal\
        \ - num)\n        }\n        return moves\n    }\n}"
      dart: "class Solution {\n  int minMoves(List<int> nums) {\n    int maxVal = nums[0];\n\
        \    for (int i = 1; i < nums.length; i++) {\n      if (nums[i] > maxVal) {\n\
        \        maxVal = nums[i];\n      }\n    }\n    int moves = 0;\n    for (int\
        \ num in nums) {\n      moves += (maxVal - num);\n    }\n    return moves;\n\
        \  }\n}"
      go: "func minMoves(nums []int) int {\n    if len(nums) == 0 {\n        return\
        \ 0\n    }\n    maxVal := nums[0]\n    for i := 1; i < len(nums); i++ {\n  \
        \      if nums[i] > maxVal {\n            maxVal = nums[i]\n        }\n    }\n\
        \    moves := 0\n    for _, num := range nums {\n        moves += (maxVal -\
        \ num)\n    }\n    return moves\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef min_moves(nums)\n \
        \ max_val = nums.max\n  nums.sum { |n| max_val - n }\nend"
      scala: "object Solution {\n    def minMoves(nums: Array[Int]): Int = {\n     \
        \   val maxVal = nums.max\n        nums.map(maxVal - _).sum\n    }\n}"
      rust: "impl Solution {\n    pub fn min_moves(nums: Vec<i32>) -> i32 {\n      \
        \  let max_val = *nums.iter().max().unwrap();\n        nums.iter().map(|&x|\
        \ max_val - x).sum()\n    }\n}"
      racket: "(define/contract (min-moves nums)\n  (-> (listof exact-integer?) exact-integer?)\n\
        \  (let ([max-val (apply max nums)])\n    (for/sum ([n nums])\n      (- max-val\
        \ n))))"
      erlang: "-spec min_moves(Nums :: [integer()]) -> integer().\nmin_moves(Nums) ->\n\
        \  MaxVal = lists:max(Nums),\n  lists:sum([MaxVal - X || X <- Nums])."
      elixir: "defmodule Solution do\n  @spec min_moves(nums :: [integer]) :: integer\n\
        \  def min_moves(nums) do\n    max_val = Enum.max(nums)\n    nums |> Enum.map(fn\
        \ x -> max_val - x end) |> Enum.sum()\n  end\nend"
    approach: 'To equalize all elements in an array using only increment operations,
      every element must be raised to a target value that is at least as large as the
      maximum value in the input array. To minimize the total number of moves, we should
      select the smallest possible target value that satisfies this condition, which
      is the current maximum value found within the array.


      The algorithm first identifies the maximum value in the array by iterating through
      the elements. Once the maximum is determined, the total moves are calculated by
      summing the differences between this maximum value and each element in the array.
      This sum represents the minimum number of single-increment steps required to bring
      every number up to the level of the highest value.'
    time_complexity: O(n), where n is the length of the array. The algorithm involves
      finding the maximum element in one pass and summing the differences in another
      pass (or simultaneously), both of which are linear operations.
    space_complexity: O(1), as the solution only requires a constant amount of extra
      space to store the maximum value and the cumulative moves counter, regardless
      of the size of the input array.
    elapsed_time: 91.26395750045776
    model: gemini-3-flash-preview
    generated_at: '2026-11-03 04:48:45 '
---

## Problem #3736: Minimum Moves to Equal Array Elements III

**Difficulty:** Easy

**Topics:** Array, Math

## Problem Description

<p>You are given an integer array <code>nums</code>.</p>

<p>In one move, you may <strong>increase</strong> the value of any single element <code>nums[i]</code> by 1.</p>

<p>Return the <strong>minimum total</strong> number of <strong>moves</strong> required so that all elements in <code>nums</code> become <strong>equal</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,1,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>To make all elements equal:</p>

<ul>
	<li>Increase <code>nums[0] = 2</code> by 1 to make it 3.</li>
	<li>Increase <code>nums[1] = 1</code> by 1 to make it 2.</li>
	<li>Increase <code>nums[1] = 2</code> by 1 to make it 3.</li>
</ul>

<p>Now, all elements of <code>nums</code> are equal to 3. The minimum total moves is <code>3</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,4,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>To make all elements equal:</p>

<ul>
	<li>Increase <code>nums[0] = 4</code> by 1 to make it 5.</li>
	<li>Increase <code>nums[1] = 4</code> by 1 to make it 5.</li>
</ul>

<p>Now, all elements of <code>nums</code> are equal to 5. The minimum total moves is <code>2</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## Hints

1. To make all numbers equal, they must all reach at least the maximum value in the array.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To equalize all elements in an array using only increment operations, every element must be raised to a target value that is at least as large as the maximum value in the input array. To minimize the total number of moves, we should select the smallest possible target value that satisfies this condition, which is the current maximum value found within the array.

The algorithm first identifies the maximum value in the array by iterating through the elements. Once the maximum is determined, the total moves are calculated by summing the differences between this maximum value and each element in the array. This sum represents the minimum number of single-increment steps required to bring every number up to the level of the highest value.

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
        int maxVal = nums[0];
        for (int num : nums) {
            if (num > maxVal) {
                maxVal = num;
            }
        }
        int totalMoves = 0;
        for (int num : nums) {
            totalMoves += (maxVal - num);
        }
        return totalMoves;
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
        int maxVal = nums[0];
        for (int num : nums) {
            if (num > maxVal) {
                maxVal = num;
            }
        }
        int totalMoves = 0;
        for (int num : nums) {
            totalMoves += (maxVal - num);
        }
        return totalMoves;
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
        max_val = max(nums)
        total_moves = 0
        for num in nums:
            total_moves += (max_val - num)
        return total_moves
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_val = max(nums)
        return sum(max_val - num for num in nums)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int minMoves(int* nums, int numsSize) {
    int maxVal = nums[0];
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] > maxVal) {
            maxVal = nums[i];
        }
    }
    int totalMoves = 0;
    for (int i = 0; i < numsSize; i++) {
        totalMoves += (maxVal - nums[i]);
    }
    return totalMoves;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinMoves(int[] nums) {
        int maxVal = nums[0];
        foreach (int num in nums) {
            if (num > maxVal) {
                maxVal = num;
            }
        }
        int totalMoves = 0;
        foreach (int num in nums) {
            totalMoves += (maxVal - num);
        }
        return totalMoves;
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
    let maxVal = nums[0];
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > maxVal) {
            maxVal = nums[i];
        }
    }
    let totalMoves = 0;
    for (let i = 0; i < nums.length; i++) {
        totalMoves += (maxVal - nums[i]);
    }
    return totalMoves;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minMoves(nums: number[]): number {
    let maxVal = nums[0];
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > maxVal) {
            maxVal = nums[i];
        }
    }
    let moves = 0;
    for (let i = 0; i < nums.length; i++) {
        moves += (maxVal - nums[i]);
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
        $maxVal = $nums[0];
        foreach ($nums as $num) {
            if ($num > $maxVal) {
                $maxVal = $num;
            }
        }
        $moves = 0;
        foreach ($nums as $num) {
            $moves += ($maxVal - $num);
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
        guard let maxVal = nums.max() else { return 0 }
        var moves = 0
        for num in nums {
            moves += (maxVal - num)
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
        var maxVal = nums[0]
        for (i in 1 until nums.size) {
            if (nums[i] > maxVal) {
                maxVal = nums[i]
            }
        }
        var moves = 0
        for (num in nums) {
            moves += (maxVal - num)
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
    int maxVal = nums[0];
    for (int i = 1; i < nums.length; i++) {
      if (nums[i] > maxVal) {
        maxVal = nums[i];
      }
    }
    int moves = 0;
    for (int num in nums) {
      moves += (maxVal - num);
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
    if len(nums) == 0 {
        return 0
    }
    maxVal := nums[0]
    for i := 1; i < len(nums); i++ {
        if nums[i] > maxVal {
            maxVal = nums[i]
        }
    }
    moves := 0
    for _, num := range nums {
        moves += (maxVal - num)
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
  max_val = nums.max
  nums.sum { |n| max_val - n }
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minMoves(nums: Array[Int]): Int = {
        val maxVal = nums.max
        nums.map(maxVal - _).sum
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
        let max_val = *nums.iter().max().unwrap();
        nums.iter().map(|&x| max_val - x).sum()
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
  (let ([max-val (apply max nums)])
    (for/sum ([n nums])
      (- max-val n))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_moves(Nums :: [integer()]) -> integer().
min_moves(Nums) ->
  MaxVal = lists:max(Nums),
  lists:sum([MaxVal - X || X <- Nums]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_moves(nums :: [integer]) :: integer
  def min_moves(nums) do
    max_val = Enum.max(nums)
    nums |> Enum.map(fn x -> max_val - x end) |> Enum.sum()
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n), where n is the length of the array. The algorithm involves finding the maximum element in one pass and summing the differences in another pass (or simultaneously), both of which are linear operations.
- **Space Complexity:** O(1), as the solution only requires a constant amount of extra space to store the maximum value and the cumulative moves counter, regardless of the size of the input array.
