---
layout: post
title: "Minimum Moves to Equal Array Elements II"
date: 2026-11-02 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Math", "Sorting"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minMoves2(vector<int>& nums) {\n    \
        \    sort(nums.begin(), nums.end());\n        int median = nums[nums.size()\
        \ / 2];\n        long long moves = 0;\n        for (int num : nums) {\n    \
        \        moves += abs((long long)num - median);\n        }\n        return (int)moves;\n\
        \    }\n};"
      java: "import java.util.Arrays;\n\nclass Solution {\n    public int minMoves2(int[]\
        \ nums) {\n        Arrays.sort(nums);\n        int median = nums[nums.length\
        \ / 2];\n        long moves = 0;\n        for (int num : nums) {\n         \
        \   moves += Math.abs((long) num - median);\n        }\n        return (int)\
        \ moves;\n    }\n}"
      python: "class Solution(object):\n    def minMoves2(self, nums):\n        \"\"\
        \"\n        :type nums: List[int]\n        :rtype: int\n        \"\"\"\n   \
        \     nums.sort()\n        median = nums[len(nums) // 2]\n        moves = 0\n\
        \        for num in nums:\n            moves += abs(num - median)\n        return\
        \ moves"
      python3: "class Solution:\n    def minMoves2(self, nums: list[int]) -> int:\n\
        \        nums.sort()\n        median = nums[len(nums) // 2]\n        moves =\
        \ sum(abs(num - median) for num in nums)\n        return moves"
      c: "#include <stdlib.h>\n\nint compare(const void* a, const void* b) {\n    int\
        \ arg1 = *(const int*)a;\n    int arg2 = *(const int*)b;\n    if (arg1 < arg2)\
        \ return -1;\n    if (arg1 > arg2) return 1;\n    return 0;\n}\n\nint minMoves2(int*\
        \ nums, int numsSize) {\n    qsort(nums, numsSize, sizeof(int), compare);\n\
        \    int median = nums[numsSize / 2];\n    long long moves = 0;\n    for (int\
        \ i = 0; i < numsSize; i++) {\n        long long diff = (long long)nums[i] -\
        \ median;\n        moves += (diff < 0) ? -diff : diff;\n    }\n    return (int)moves;\n\
        }"
      csharp: "public class Solution {\n    public int MinMoves2(int[] nums) {\n   \
        \     System.Array.Sort(nums);\n        int median = nums[nums.Length / 2];\n\
        \        long moves = 0;\n        foreach (int num in nums) {\n            moves\
        \ += System.Math.Abs((long)num - median);\n        }\n        return (int)moves;\n\
        \    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar minMoves2\
        \ = function(nums) {\n    nums.sort((a, b) => a - b);\n    const median = nums[Math.floor(nums.length\
        \ / 2)];\n    let moves = 0;\n    for (let i = 0; i < nums.length; i++) {\n\
        \        moves += Math.abs(nums[i] - median);\n    }\n    return moves;\n};"
      typescript: "function minMoves2(nums: number[]): number {\n    nums.sort((a, b)\
        \ => a - b);\n    const median = nums[Math.floor(nums.length / 2)];\n    let\
        \ moves = 0;\n    for (let i = 0; i < nums.length; i++) {\n        moves +=\
        \ Math.abs(nums[i] - median);\n    }\n    return moves;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function minMoves2($nums) {\n        sort($nums);\n\
        \        $median = $nums[(int)(count($nums) / 2)];\n        $moves = 0;\n  \
        \      foreach ($nums as $num) {\n            $moves += abs($num - $median);\n\
        \        }\n        return $moves;\n    }\n}"
      swift: "class Solution {\n    func minMoves2(_ nums: [Int]) -> Int {\n       \
        \ let sortedNums = nums.sorted()\n        let median = sortedNums[sortedNums.count\
        \ / 2]\n        var moves = 0\n        for num in sortedNums {\n           \
        \ moves += abs(num - median)\n        }\n        return moves\n    }\n}"
      kotlin: "class Solution {\n    fun minMoves2(nums: IntArray): Int {\n        nums.sort()\n\
        \        val median = nums[nums.size / 2]\n        var moves: Long = 0\n   \
        \     for (num in nums) {\n            moves += Math.abs(num.toLong() - median.toLong())\n\
        \        }\n        return moves.toInt()\n    }\n}"
      dart: "class Solution {\n  int minMoves2(List<int> nums) {\n    nums.sort();\n\
        \    int median = nums[nums.length ~/ 2];\n    int moves = 0;\n    for (int\
        \ num in nums) {\n      moves += (num - median).abs();\n    }\n    return moves;\n\
        \  }\n}"
      go: "import (\n    \"sort\"\n)\n\nfunc minMoves2(nums []int) int {\n    sort.Ints(nums)\n\
        \    median := nums[len(nums)/2]\n    moves := 0\n    for _, num := range nums\
        \ {\n        if num > median {\n            moves += num - median\n        }\
        \ else {\n            moves += median - num\n        }\n    }\n    return moves\n\
        }"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef min_moves2(nums)\n\
        \  nums.sort!\n  median = nums[nums.length / 2]\n  moves = 0\n  nums.each do\
        \ |num|\n    moves += (num - median).abs\n  end\n  moves\nend"
      scala: "object Solution {\n    def minMoves2(nums: Array[Int]): Int = {\n    \
        \    val sortedNums = nums.sorted\n        val median = sortedNums(sortedNums.length\
        \ / 2)\n        var moves: Long = 0\n        for (num <- sortedNums) {\n   \
        \         moves += Math.abs(num.toLong - median.toLong)\n        }\n       \
        \ moves.toInt\n    }\n}"
      rust: "impl Solution {\n    pub fn min_moves2(nums: Vec<i32>) -> i32 {\n     \
        \   let mut nums = nums;\n        nums.sort_unstable();\n        let n = nums.len();\n\
        \        let median = nums[n / 2] as i64;\n        nums.iter().map(|&x| (x as\
        \ i64 - median).abs()).sum::<i64>() as i32\n    }\n}"
      racket: "(define/contract (min-moves2 nums)\n  (-> (listof exact-integer?) exact-integer?)\n\
        \  (let* ([sorted (sort nums <)]\n         [len (length sorted)]\n         [median\
        \ (list-ref sorted (quotient len 2))])\n    (foldl (lambda (x acc) (+ acc (abs\
        \ (- x median)))) 0 sorted)))"
      erlang: "-spec min_moves2(Nums :: [integer()]) -> integer().\nmin_moves2(Nums)\
        \ ->\n  Sorted = lists:sort(Nums),\n  Len = length(Sorted),\n  Median = lists:nth((Len\
        \ div 2) + 1, Sorted),\n  lists:foldl(fun(X, Acc) -> Acc + abs(X - Median) end,\
        \ 0, Sorted)."
      elixir: "defmodule Solution do\n  @spec min_moves2(nums :: [integer]) :: integer\n\
        \  def min_moves2(nums) do\n    sorted = Enum.sort(nums)\n    len = length(sorted)\n\
        \    median = Enum.at(sorted, div(len, 2))\n    Enum.reduce(sorted, 0, fn x,\
        \ acc -> acc + abs(x - median) end)\n  end\nend"
    approach: 'The problem asks for the minimum moves to make all array elements equal,
      where a move consists of incrementing or decrementing an element by one. This
      is equivalent to finding a target value $x$ that minimizes the sum of absolute
      differences $\sum |nums[i] - x|$. A well-known mathematical result is that the
      value minimizing the sum of absolute deviations from a set of points is the median
      of those points. If the array size is odd, the median is the unique middle element
      after sorting; if the size is even, any value in the range between the two central
      elements will minimize the sum.


      The algorithm begins by sorting the array in ascending order to easily locate
      the median. We then identify the median at index $n/2$. Finally, we iterate through
      the array once more to calculate the total cost by summing the absolute difference
      between every element and the median. Since the problem guarantees the result
      fits in a 32-bit integer, we perform the accumulation and return the total count
      of moves.'
    time_complexity: O(n log n) because the most computationally expensive step is sorting
      the input array of $n$ elements. The subsequent single pass to calculate the sum
      of absolute differences takes $O(n)$ time.
    space_complexity: O(log n) or O(n) depending on the language's sorting implementation.
      For instance, C++'s std::sort typically uses $O(log n)$ stack space for quicksort-based
      logic, while Python and Java use Timsort which requires $O(n)$ auxiliary space.
    elapsed_time: 153.2902479171753
    model: gemini-3-flash-preview
    generated_at: '2026-11-02 03:45:45 '
---

## Problem #462: Minimum Moves to Equal Array Elements II

**Difficulty:** Medium

**Topics:** Array, Math, Sorting

## Problem Description

<p>Given an integer array <code>nums</code> of size <code>n</code>, return <em>the minimum number of moves required to make all array elements equal</em>.</p>

<p>In one move, you can increment or decrement an element of the array by <code>1</code>.</p>

<p>Test cases are designed so that the answer will fit in a <strong>32-bit</strong> integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
Only two moves are needed (remember each move increments or decrements one element):
[<u>1</u>,2,3]  =&gt;  [2,2,<u>3</u>]  =&gt;  [2,2,2]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,10,2,9]
<strong>Output:</strong> 16
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the minimum moves to make all array elements equal, where a move consists of incrementing or decrementing an element by one. This is equivalent to finding a target value $x$ that minimizes the sum of absolute differences $\sum |nums[i] - x|$. A well-known mathematical result is that the value minimizing the sum of absolute deviations from a set of points is the median of those points. If the array size is odd, the median is the unique middle element after sorting; if the size is even, any value in the range between the two central elements will minimize the sum.

The algorithm begins by sorting the array in ascending order to easily locate the median. We then identify the median at index $n/2$. Finally, we iterate through the array once more to calculate the total cost by summing the absolute difference between every element and the median. Since the problem guarantees the result fits in a 32-bit integer, we perform the accumulation and return the total count of moves.

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
    int minMoves2(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int median = nums[nums.size() / 2];
        long long moves = 0;
        for (int num : nums) {
            moves += abs((long long)num - median);
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
import java.util.Arrays;

class Solution {
    public int minMoves2(int[] nums) {
        Arrays.sort(nums);
        int median = nums[nums.length / 2];
        long moves = 0;
        for (int num : nums) {
            moves += Math.abs((long) num - median);
        }
        return (int) moves;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        median = nums[len(nums) // 2]
        moves = 0
        for num in nums:
            moves += abs(num - median)
        return moves
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        moves = sum(abs(num - median) for num in nums)
        return moves
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

int minMoves2(int* nums, int numsSize) {
    qsort(nums, numsSize, sizeof(int), compare);
    int median = nums[numsSize / 2];
    long long moves = 0;
    for (int i = 0; i < numsSize; i++) {
        long long diff = (long long)nums[i] - median;
        moves += (diff < 0) ? -diff : diff;
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
    public int MinMoves2(int[] nums) {
        System.Array.Sort(nums);
        int median = nums[nums.Length / 2];
        long moves = 0;
        foreach (int num in nums) {
            moves += System.Math.Abs((long)num - median);
        }
        return (int)moves;
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
var minMoves2 = function(nums) {
    nums.sort((a, b) => a - b);
    const median = nums[Math.floor(nums.length / 2)];
    let moves = 0;
    for (let i = 0; i < nums.length; i++) {
        moves += Math.abs(nums[i] - median);
    }
    return moves;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minMoves2(nums: number[]): number {
    nums.sort((a, b) => a - b);
    const median = nums[Math.floor(nums.length / 2)];
    let moves = 0;
    for (let i = 0; i < nums.length; i++) {
        moves += Math.abs(nums[i] - median);
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
    function minMoves2($nums) {
        sort($nums);
        $median = $nums[(int)(count($nums) / 2)];
        $moves = 0;
        foreach ($nums as $num) {
            $moves += abs($num - $median);
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
    func minMoves2(_ nums: [Int]) -> Int {
        let sortedNums = nums.sorted()
        let median = sortedNums[sortedNums.count / 2]
        var moves = 0
        for num in sortedNums {
            moves += abs(num - median)
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
    fun minMoves2(nums: IntArray): Int {
        nums.sort()
        val median = nums[nums.size / 2]
        var moves: Long = 0
        for (num in nums) {
            moves += Math.abs(num.toLong() - median.toLong())
        }
        return moves.toInt()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minMoves2(List<int> nums) {
    nums.sort();
    int median = nums[nums.length ~/ 2];
    int moves = 0;
    for (int num in nums) {
      moves += (num - median).abs();
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
import (
    "sort"
)

func minMoves2(nums []int) int {
    sort.Ints(nums)
    median := nums[len(nums)/2]
    moves := 0
    for _, num := range nums {
        if num > median {
            moves += num - median
        } else {
            moves += median - num
        }
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
def min_moves2(nums)
  nums.sort!
  median = nums[nums.length / 2]
  moves = 0
  nums.each do |num|
    moves += (num - median).abs
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
    def minMoves2(nums: Array[Int]): Int = {
        val sortedNums = nums.sorted
        val median = sortedNums(sortedNums.length / 2)
        var moves: Long = 0
        for (num <- sortedNums) {
            moves += Math.abs(num.toLong - median.toLong)
        }
        moves.toInt
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_moves2(nums: Vec<i32>) -> i32 {
        let mut nums = nums;
        nums.sort_unstable();
        let n = nums.len();
        let median = nums[n / 2] as i64;
        nums.iter().map(|&x| (x as i64 - median).abs()).sum::<i64>() as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-moves2 nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([sorted (sort nums <)]
         [len (length sorted)]
         [median (list-ref sorted (quotient len 2))])
    (foldl (lambda (x acc) (+ acc (abs (- x median)))) 0 sorted)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_moves2(Nums :: [integer()]) -> integer().
min_moves2(Nums) ->
  Sorted = lists:sort(Nums),
  Len = length(Sorted),
  Median = lists:nth((Len div 2) + 1, Sorted),
  lists:foldl(fun(X, Acc) -> Acc + abs(X - Median) end, 0, Sorted).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_moves2(nums :: [integer]) :: integer
  def min_moves2(nums) do
    sorted = Enum.sort(nums)
    len = length(sorted)
    median = Enum.at(sorted, div(len, 2))
    Enum.reduce(sorted, 0, fn x, acc -> acc + abs(x - median) end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n log n) because the most computationally expensive step is sorting the input array of $n$ elements. The subsequent single pass to calculate the sum of absolute differences takes $O(n)$ time.
- **Space Complexity:** O(log n) or O(n) depending on the language's sorting implementation. For instance, C++'s std::sort typically uses $O(log n)$ stack space for quicksort-based logic, while Python and Java use Timsort which requires $O(n)$ auxiliary space.
