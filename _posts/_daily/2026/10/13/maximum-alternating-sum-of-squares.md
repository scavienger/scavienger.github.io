---
layout: post
title: "Maximum Alternating Sum of Squares"
date: 2026-10-13 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Greedy", "Sorting"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/maximum-alternating-sum-of-squares/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    long long maxAlternatingSum(vector<int>&\
        \ nums) {\n        int n = nums.size();\n        std::vector<long long> squares(n);\n\
        \        for (int i = 0; i < n; ++i) {\n            squares[i] = (long long)nums[i]\
        \ * nums[i];\n        }\n        std::sort(squares.begin(), squares.end());\n\
        \        long long result = 0;\n        int negCount = n / 2;\n        for (int\
        \ i = 0; i < negCount; ++i) {\n            result -= squares[i];\n        }\n\
        \        for (int i = negCount; i < n; ++i) {\n            result += squares[i];\n\
        \        }\n        return result;\n    }\n};"
      java: "class Solution {\n    public long maxAlternatingSum(int[] nums) {\n   \
        \     int n = nums.length;\n        long[] squares = new long[n];\n        for\
        \ (int i = 0; i < n; i++) {\n            squares[i] = (long) nums[i] * nums[i];\n\
        \        }\n        java.util.Arrays.sort(squares);\n        long result = 0;\n\
        \        int negCount = n / 2;\n        for (int i = 0; i < negCount; i++) {\n\
        \            result -= squares[i];\n        }\n        for (int i = negCount;\
        \ i < n; i++) {\n            result += squares[i];\n        }\n        return\
        \ result;\n    }\n}"
      python: "class Solution(object):\n    def maxAlternatingSum(self, nums):\n   \
        \     \"\"\"\n        :type nums: List[int]\n        :rtype: int\n        \"\
        \"\"\n        squares = sorted([float(x) * x for x in nums])\n        n = len(squares)\n\
        \        neg_count = n // 2\n        res = 0\n        for i in range(neg_count):\n\
        \            res -= squares[i]\n        for i in range(neg_count, n):\n    \
        \        res += squares[i]\n        return int(res)"
      python3: "class Solution:\n    def maxAlternatingSum(self, nums: List[int]) ->\
        \ int:\n        squares = sorted([x * x for x in nums])\n        n = len(squares)\n\
        \        neg_count = n // 2\n        return sum(squares[neg_count:]) - sum(squares[:neg_count])"
      c: "#include <stdlib.h>\n\nint compareSquares(const void* a, const void* b) {\n\
        \    long long l = *(const long long*)a;\n    long long r = *(const long long*)b;\n\
        \    if (l < r) return -1;\n    if (l > r) return 1;\n    return 0;\n}\n\nlong\
        \ long maxAlternatingSum(int* nums, int numsSize) {\n    long long* squares\
        \ = (long long*)malloc(numsSize * sizeof(long long));\n    for (int i = 0; i\
        \ < numsSize; i++) {\n        squares[i] = (long long)nums[i] * nums[i];\n \
        \   }\n    qsort(squares, numsSize, sizeof(long long), compareSquares);\n  \
        \  long long result = 0;\n    int negCount = numsSize / 2;\n    for (int i =\
        \ 0; i < negCount; i++) {\n        result -= squares[i];\n    }\n    for (int\
        \ i = negCount; i < numsSize; i++) {\n        result += squares[i];\n    }\n\
        \    free(squares);\n    return result;\n}"
      csharp: "public class Solution {\n    public long MaxAlternatingSum(int[] nums)\
        \ {\n        int n = nums.Length;\n        long[] squares = new long[n];\n \
        \       for (int i = 0; i < n; i++) {\n            squares[i] = (long)nums[i]\
        \ * nums[i];\n        }\n        System.Array.Sort(squares);\n        int m\
        \ = n / 2;\n        long result = 0;\n        for (int i = 0; i < m; i++) {\n\
        \            result -= squares[i];\n        }\n        for (int i = m; i < n;\
        \ i++) {\n            result += squares[i];\n        }\n        return result;\n\
        \    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar maxAlternatingSum\
        \ = function(nums) {\n    const n = nums.length;\n    const squares = new Array(n);\n\
        \    for (let i = 0; i < n; i++) {\n        squares[i] = nums[i] * nums[i];\n\
        \    }\n    squares.sort((a, b) => a - b);\n    const m = Math.floor(n / 2);\n\
        \    let result = 0;\n    for (let i = 0; i < m; i++) {\n        result -= squares[i];\n\
        \    }\n    for (let i = m; i < n; i++) {\n        result += squares[i];\n \
        \   }\n    return result;\n};"
      typescript: "function maxAlternatingSum(nums: number[]): number {\n    const n:\
        \ number = nums.length;\n    const squares: number[] = new Array(n);\n    for\
        \ (let i = 0; i < n; i++) {\n        squares[i] = nums[i] * nums[i];\n    }\n\
        \    squares.sort((a, b) => a - b);\n    const m: number = Math.floor(n / 2);\n\
        \    let result: number = 0;\n    for (let i = 0; i < m; i++) {\n        result\
        \ -= squares[i];\n    }\n    for (let i = m; i < n; i++) {\n        result +=\
        \ squares[i];\n    }\n    return result;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function maxAlternatingSum($nums) {\n        $n = count($nums);\n\
        \        $squares = [];\n        for ($i = 0; $i < $n; $i++) {\n           \
        \ $squares[] = $nums[$i] * $nums[$i];\n        }\n        sort($squares);\n\
        \        $m = (int)($n / 2);\n        $result = 0;\n        for ($i = 0; $i\
        \ < $m; $i++) {\n            $result -= $squares[$i];\n        }\n        for\
        \ ($i = $m; $i < $n; $i++) {\n            $result += $squares[$i];\n       \
        \ }\n        return $result;\n    }\n}"
      swift: "class Solution {\n    func maxAlternatingSum(_ nums: [Int]) -> Int {\n\
        \        let n = nums.count\n        var squares = nums.map { $0 * $0 }\n  \
        \      squares.sort()\n        let m = n / 2\n        var result = 0\n     \
        \   for i in 0..<m {\n            result -= squares[i]\n        }\n        for\
        \ i in m..<n {\n            result += squares[i]\n        }\n        return\
        \ result;\n    }\n}"
      kotlin: "class Solution {\n    fun maxAlternatingSum(nums: IntArray): Long {\n\
        \        val n = nums.size\n        val squares = LongArray(n)\n        for\
        \ (i in 0 until n) {\n            val v = nums[i].toLong()\n            squares[i]\
        \ = v * v\n        }\n        squares.sort()\n        var result: Long = 0\n\
        \        val m = n / 2\n        for (i in 0 until m) {\n            result -=\
        \ squares[i]\n        }\n        for (i in m until n) {\n            result\
        \ += squares[i]\n        }\n        return result\n    }\n}"
      dart: "class Solution {\n  int maxAlternatingSum(List<int> nums) {\n    int n\
        \ = nums.length;\n    List<int> squares = nums.map((x) => x * x).toList();\n\
        \    squares.sort();\n    int result = 0;\n    int m = n ~/ 2;\n    for (int\
        \ i = 0; i < m; i++) {\n      result -= squares[i];\n    }\n    for (int i =\
        \ m; i < n; i++) {\n      result += squares[i];\n    }\n    return result;\n\
        \  }\n}"
      go: "import \"sort\"\n\nfunc maxAlternatingSum(nums []int) int64 {\n    n := len(nums)\n\
        \    squares := make([]int64, n)\n    for i, v := range nums {\n        squares[i]\
        \ = int64(v) * int64(v)\n    }\n    sort.Slice(squares, func(i, j int) bool\
        \ {\n        return squares[i] < squares[j]\n    })\n    var result int64 =\
        \ 0\n    m := n / 2\n    for i := 0; i < m; i++ {\n        result -= squares[i]\n\
        \    }\n    for i := m; i < n; i++ {\n        result += squares[i]\n    }\n\
        \    return result\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef max_alternating_sum(nums)\n\
        \  squares = nums.map { |x| x * x }\n  squares.sort!\n  n = squares.length\n\
        \  m = n / 2\n  result = 0\n  (0...m).each do |i|\n    result -= squares[i]\n\
        \  end\n  (m...n).each do |i|\n    result += squares[i]\n  end\n  result\nend"
      scala: "object Solution {\n    def maxAlternatingSum(nums: Array[Int]): Long =\
        \ {\n        val squares = nums.map(x => x.toLong * x).sorted\n        val n\
        \ = squares.length\n        val m = n / 2\n        var result: Long = 0\n  \
        \      for (i <- 0 until m) {\n            result -= squares(i)\n        }\n\
        \        for (i <- m until n) {\n            result += squares(i)\n        }\n\
        \        result\n    }\n}"
      rust: "impl Solution {\n    pub fn max_alternating_sum(nums: Vec<i32>) -> i64\
        \ {\n        let mut squares: Vec<i64> = nums.into_iter().map(|x| (x as i64)\
        \ * (x as i64)).collect();\n        squares.sort_unstable();\n        let n\
        \ = squares.len();\n        let m = n / 2;\n        let mut total: i64 = 0;\n\
        \        for (i, &val) in squares.iter().enumerate() {\n            if i < m\
        \ {\n                total -= val;\n            } else {\n                total\
        \ += val;\n            }\n        }\n        total\n    }\n}"
      racket: "(define/contract (max-alternating-sum nums)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let* ([squares (sort (map (lambda (x) (* x x)) nums) <)]\n\
        \         [n (length squares)]\n         [m (quotient n 2)])\n    (let loop\
        \ ([lst squares]\n               [i 0]\n               [acc 0])\n      (if (null?\
        \ lst)\n          acc\n          (if (< i m)\n              (loop (cdr lst)\
        \ (+ i 1) (- acc (car lst)))\n              (loop (cdr lst) (+ i 1) (+ acc (car\
        \ lst))))))))"
      erlang: "-spec max_alternating_sum(Nums :: [integer()]) -> integer().\nmax_alternating_sum(Nums)\
        \ ->\n    Squares = lists:sort([X * X || X <- Nums]),\n    N = length(Squares),\n\
        \    M = N div 2,\n    {Small, Large} = lists:split(M, Squares),\n    lists:sum(Large)\
        \ - lists:sum(Small)."
      elixir: "defmodule Solution do\n  @spec max_alternating_sum(nums :: [integer])\
        \ :: integer\n  def max_alternating_sum(nums) do\n    squares = nums\n     \
        \         |> Enum.map(fn x -> x * x end)\n              |> Enum.sort()\n   \
        \ n = length(squares)\n    m = div(n, 2)\n    {small, large} = Enum.split(squares,\
        \ m)\n    Enum.sum(large) - Enum.sum(small)\n  end\nend"
    approach: 'The problem asks to maximize the alternating sum of squares $x_0^2 -
      x_1^2 + x_2^2 - x_3^2 + \dots$ by rearranging an input array. Since the formula
      involves squares, the original sign of each number in the array is irrelevant;
      only its absolute value matters. In the alternating sum, terms at even indices
      (0, 2, 4, etc.) contribute positively, while terms at odd indices (1, 3, 5, etc.)
      contribute negatively. To maximize the total score, we want to assign the largest
      available squares to the positive terms and the smallest available squares to
      the negative terms.


      Specifically, for an array of size $n$, there are exactly $\lfloor n/2 \rfloor$
      negative terms and $\lceil n/2 \rceil$ positive terms. The optimal strategy is
      to calculate the square of every element in the array and sort these values in
      ascending order. We then sum the largest $n - \lfloor n/2 \rfloor$ values and
      subtract the $\lfloor n/2 \rfloor$ smallest values. This greedy approach ensures
      that the total sum is maximized by emphasizing the largest contributions and minimizing
      the subtractions.'
    time_complexity: O(N log N) where N is the length of the input array. This is primarily
      due to the sorting of the squared values. Squaring the elements and performing
      the final summation both take linear O(N) time.
    space_complexity: O(N) because we create an auxiliary array of size N to store the
      squared values of the original numbers. The sorting algorithm itself may also
      use additional O(log N) or O(N) space depending on the language's internal implementation.
    elapsed_time: 2091.995047569275
    model: gemini-3-flash-preview
    generated_at: '2026-10-13 05:24:11 '
---

## Problem #3727: Maximum Alternating Sum of Squares

**Difficulty:** Medium

**Topics:** Array, Greedy, Sorting

## Problem Description

<p>You are given an integer array <code>nums</code>. You may <strong>rearrange the elements</strong> in any order.</p>

<p>The <strong>alternating score</strong> of an array <code>arr</code> is defined as:</p>

<ul>
	<li><code>score = arr[0]<sup>2</sup> - arr[1]<sup>2</sup> + arr[2]<sup>2</sup> - arr[3]<sup>2</sup> + ...</code></li>
</ul>

<p>Return an integer denoting the <strong>maximum possible alternating score</strong> of <code>nums</code> after rearranging its elements.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">12</span></p>

<p><strong>Explanation:</strong></p>

<p>A possible rearrangement for <code>nums</code> is <code>[2,1,3]</code>, which gives the maximum alternating score among all possible rearrangements.</p>

<p>The alternating score is calculated as:</p>

<p><code>score = 2<sup>2</sup> - 1<sup>2</sup> + 3<sup>2</sup> = 4 - 1 + 9 = 12</code></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,-1,2,-2,3,-3]</span></p>

<p><strong>Output:</strong> <span class="example-io">16</span></p>

<p><strong>Explanation:</strong></p>

<p>A possible rearrangement for <code>nums</code> is <code>[-3,-1,-2,1,3,2]</code>, which gives the maximum alternating score among all possible rearrangements.</p>

<p>The alternating score is calculated as:</p>

<p><code>score = (-3)<sup>2</sup> - (-1)<sup>2</sup> + (-2)<sup>2</sup> - (1)<sup>2</sup> + (3)<sup>2</sup> - (2)<sup>2</sup> = 9 - 1 + 4 - 1 + 9 - 4 = 16</code></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-4 * 10<sup>4</sup> &lt;= nums[i] &lt;= 4 * 10<sup>4</sup></code></li>
</ul>


## Hints

1. The score uses squares of values. The original signs of `nums` don't affect the squared terms.

2. In the alternating sum, even indices contribute positively and odd indices negatively.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks to maximize the alternating sum of squares $x_0^2 - x_1^2 + x_2^2 - x_3^2 + \dots$ by rearranging an input array. Since the formula involves squares, the original sign of each number in the array is irrelevant; only its absolute value matters. In the alternating sum, terms at even indices (0, 2, 4, etc.) contribute positively, while terms at odd indices (1, 3, 5, etc.) contribute negatively. To maximize the total score, we want to assign the largest available squares to the positive terms and the smallest available squares to the negative terms.

Specifically, for an array of size $n$, there are exactly $\lfloor n/2 \rfloor$ negative terms and $\lceil n/2 \rceil$ positive terms. The optimal strategy is to calculate the square of every element in the array and sort these values in ascending order. We then sum the largest $n - \lfloor n/2 \rfloor$ values and subtract the $\lfloor n/2 \rfloor$ smallest values. This greedy approach ensures that the total sum is maximized by emphasizing the largest contributions and minimizing the subtractions.

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
    long long maxAlternatingSum(vector<int>& nums) {
        int n = nums.size();
        std::vector<long long> squares(n);
        for (int i = 0; i < n; ++i) {
            squares[i] = (long long)nums[i] * nums[i];
        }
        std::sort(squares.begin(), squares.end());
        long long result = 0;
        int negCount = n / 2;
        for (int i = 0; i < negCount; ++i) {
            result -= squares[i];
        }
        for (int i = negCount; i < n; ++i) {
            result += squares[i];
        }
        return result;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public long maxAlternatingSum(int[] nums) {
        int n = nums.length;
        long[] squares = new long[n];
        for (int i = 0; i < n; i++) {
            squares[i] = (long) nums[i] * nums[i];
        }
        java.util.Arrays.sort(squares);
        long result = 0;
        int negCount = n / 2;
        for (int i = 0; i < negCount; i++) {
            result -= squares[i];
        }
        for (int i = negCount; i < n; i++) {
            result += squares[i];
        }
        return result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        squares = sorted([float(x) * x for x in nums])
        n = len(squares)
        neg_count = n // 2
        res = 0
        for i in range(neg_count):
            res -= squares[i]
        for i in range(neg_count, n):
            res += squares[i]
        return int(res)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted([x * x for x in nums])
        n = len(squares)
        neg_count = n // 2
        return sum(squares[neg_count:]) - sum(squares[:neg_count])
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

int compareSquares(const void* a, const void* b) {
    long long l = *(const long long*)a;
    long long r = *(const long long*)b;
    if (l < r) return -1;
    if (l > r) return 1;
    return 0;
}

long long maxAlternatingSum(int* nums, int numsSize) {
    long long* squares = (long long*)malloc(numsSize * sizeof(long long));
    for (int i = 0; i < numsSize; i++) {
        squares[i] = (long long)nums[i] * nums[i];
    }
    qsort(squares, numsSize, sizeof(long long), compareSquares);
    long long result = 0;
    int negCount = numsSize / 2;
    for (int i = 0; i < negCount; i++) {
        result -= squares[i];
    }
    for (int i = negCount; i < numsSize; i++) {
        result += squares[i];
    }
    free(squares);
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public long MaxAlternatingSum(int[] nums) {
        int n = nums.Length;
        long[] squares = new long[n];
        for (int i = 0; i < n; i++) {
            squares[i] = (long)nums[i] * nums[i];
        }
        System.Array.Sort(squares);
        int m = n / 2;
        long result = 0;
        for (int i = 0; i < m; i++) {
            result -= squares[i];
        }
        for (int i = m; i < n; i++) {
            result += squares[i];
        }
        return result;
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
var maxAlternatingSum = function(nums) {
    const n = nums.length;
    const squares = new Array(n);
    for (let i = 0; i < n; i++) {
        squares[i] = nums[i] * nums[i];
    }
    squares.sort((a, b) => a - b);
    const m = Math.floor(n / 2);
    let result = 0;
    for (let i = 0; i < m; i++) {
        result -= squares[i];
    }
    for (let i = m; i < n; i++) {
        result += squares[i];
    }
    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxAlternatingSum(nums: number[]): number {
    const n: number = nums.length;
    const squares: number[] = new Array(n);
    for (let i = 0; i < n; i++) {
        squares[i] = nums[i] * nums[i];
    }
    squares.sort((a, b) => a - b);
    const m: number = Math.floor(n / 2);
    let result: number = 0;
    for (let i = 0; i < m; i++) {
        result -= squares[i];
    }
    for (let i = m; i < n; i++) {
        result += squares[i];
    }
    return result;
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
    function maxAlternatingSum($nums) {
        $n = count($nums);
        $squares = [];
        for ($i = 0; $i < $n; $i++) {
            $squares[] = $nums[$i] * $nums[$i];
        }
        sort($squares);
        $m = (int)($n / 2);
        $result = 0;
        for ($i = 0; $i < $m; $i++) {
            $result -= $squares[$i];
        }
        for ($i = $m; $i < $n; $i++) {
            $result += $squares[$i];
        }
        return $result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxAlternatingSum(_ nums: [Int]) -> Int {
        let n = nums.count
        var squares = nums.map { $0 * $0 }
        squares.sort()
        let m = n / 2
        var result = 0
        for i in 0..<m {
            result -= squares[i]
        }
        for i in m..<n {
            result += squares[i]
        }
        return result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxAlternatingSum(nums: IntArray): Long {
        val n = nums.size
        val squares = LongArray(n)
        for (i in 0 until n) {
            val v = nums[i].toLong()
            squares[i] = v * v
        }
        squares.sort()
        var result: Long = 0
        val m = n / 2
        for (i in 0 until m) {
            result -= squares[i]
        }
        for (i in m until n) {
            result += squares[i]
        }
        return result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maxAlternatingSum(List<int> nums) {
    int n = nums.length;
    List<int> squares = nums.map((x) => x * x).toList();
    squares.sort();
    int result = 0;
    int m = n ~/ 2;
    for (int i = 0; i < m; i++) {
      result -= squares[i];
    }
    for (int i = m; i < n; i++) {
      result += squares[i];
    }
    return result;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "sort"

func maxAlternatingSum(nums []int) int64 {
    n := len(nums)
    squares := make([]int64, n)
    for i, v := range nums {
        squares[i] = int64(v) * int64(v)
    }
    sort.Slice(squares, func(i, j int) bool {
        return squares[i] < squares[j]
    })
    var result int64 = 0
    m := n / 2
    for i := 0; i < m; i++ {
        result -= squares[i]
    }
    for i := m; i < n; i++ {
        result += squares[i]
    }
    return result
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def max_alternating_sum(nums)
  squares = nums.map { |x| x * x }
  squares.sort!
  n = squares.length
  m = n / 2
  result = 0
  (0...m).each do |i|
    result -= squares[i]
  end
  (m...n).each do |i|
    result += squares[i]
  end
  result
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxAlternatingSum(nums: Array[Int]): Long = {
        val squares = nums.map(x => x.toLong * x).sorted
        val n = squares.length
        val m = n / 2
        var result: Long = 0
        for (i <- 0 until m) {
            result -= squares(i)
        }
        for (i <- m until n) {
            result += squares(i)
        }
        result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_alternating_sum(nums: Vec<i32>) -> i64 {
        let mut squares: Vec<i64> = nums.into_iter().map(|x| (x as i64) * (x as i64)).collect();
        squares.sort_unstable();
        let n = squares.len();
        let m = n / 2;
        let mut total: i64 = 0;
        for (i, &val) in squares.iter().enumerate() {
            if i < m {
                total -= val;
            } else {
                total += val;
            }
        }
        total
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (max-alternating-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([squares (sort (map (lambda (x) (* x x)) nums) <)]
         [n (length squares)]
         [m (quotient n 2)])
    (let loop ([lst squares]
               [i 0]
               [acc 0])
      (if (null? lst)
          acc
          (if (< i m)
              (loop (cdr lst) (+ i 1) (- acc (car lst)))
              (loop (cdr lst) (+ i 1) (+ acc (car lst))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_alternating_sum(Nums :: [integer()]) -> integer().
max_alternating_sum(Nums) ->
    Squares = lists:sort([X * X || X <- Nums]),
    N = length(Squares),
    M = N div 2,
    {Small, Large} = lists:split(M, Squares),
    lists:sum(Large) - lists:sum(Small).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_alternating_sum(nums :: [integer]) :: integer
  def max_alternating_sum(nums) do
    squares = nums
              |> Enum.map(fn x -> x * x end)
              |> Enum.sort()
    n = length(squares)
    m = div(n, 2)
    {small, large} = Enum.split(squares, m)
    Enum.sum(large) - Enum.sum(small)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N log N) where N is the length of the input array. This is primarily due to the sorting of the squared values. Squaring the elements and performing the final summation both take linear O(N) time.
- **Space Complexity:** O(N) because we create an auxiliary array of size N to store the squared values of the original numbers. The sorting algorithm itself may also use additional O(log N) or O(N) space depending on the language's internal implementation.
