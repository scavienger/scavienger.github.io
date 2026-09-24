---
layout: post
title: "Smallest Index With Digit Sum Equal to Index"
date: 2026-09-24 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Math"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int smallestIndex(vector<int>& nums) {\n\
        \        for (int i = 0; i < (int)nums.size(); ++i) {\n            int sum =\
        \ 0;\n            int temp = nums[i];\n            while (temp > 0) {\n    \
        \            sum += temp % 10;\n                temp /= 10;\n            }\n\
        \            if (sum == i) {\n                return i;\n            }\n   \
        \     }\n        return -1;\n    }\n};"
      java: "class Solution {\n    public int smallestIndex(int[] nums) {\n        for\
        \ (int i = 0; i < nums.length; i++) {\n            int sum = 0;\n          \
        \  int temp = nums[i];\n            while (temp > 0) {\n                sum\
        \ += temp % 10;\n                temp /= 10;\n            }\n            if\
        \ (sum == i) {\n                return i;\n            }\n        }\n      \
        \  return -1;\n    }\n}"
      python: "class Solution(object):\n    def smallestIndex(self, nums):\n       \
        \ \"\"\"\n        :type nums: List[int]\n        :rtype: int\n        \"\"\"\
        \n        for i in range(len(nums)):\n            digit_sum = 0\n          \
        \  temp = nums[i]\n            while temp > 0:\n                digit_sum +=\
        \ temp % 10\n                temp //= 10\n            if digit_sum == i:\n \
        \               return i\n        return -1"
      python3: "class Solution:\n    def smallestIndex(self, nums: List[int]) -> int:\n\
        \        for i in range(len(nums)):\n            digit_sum = 0\n           \
        \ temp = nums[i]\n            while temp > 0:\n                digit_sum +=\
        \ temp % 10\n                temp //= 10\n            if digit_sum == i:\n \
        \               return i\n        return -1"
      c: "int smallestIndex(int* nums, int numsSize) {\n    for (int i = 0; i < numsSize;\
        \ i++) {\n        int sum = 0;\n        int temp = nums[i];\n        while (temp\
        \ > 0) {\n            sum += temp % 10;\n            temp /= 10;\n        }\n\
        \        if (sum == i) {\n            return i;\n        }\n    }\n    return\
        \ -1;\n}"
      csharp: "public class Solution {\n    public int SmallestIndex(int[] nums) {\n\
        \        for (int i = 0; i < nums.Length; i++) {\n            int sum = 0;\n\
        \            int temp = nums[i];\n            while (temp > 0) {\n         \
        \       sum += temp % 10;\n                temp /= 10;\n            }\n    \
        \        if (sum == i) {\n                return i;\n            }\n       \
        \ }\n        return -1;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar smallestIndex\
        \ = function(nums) {\n    for (let i = 0; i < nums.length; i++) {\n        let\
        \ sum = 0;\n        let temp = nums[i];\n        while (temp > 0) {\n      \
        \      sum += temp % 10;\n            temp = Math.floor(temp / 10);\n      \
        \  }\n        if (sum === i) {\n            return i;\n        }\n    }\n  \
        \  return -1;\n};"
      typescript: "function smallestIndex(nums: number[]): number {\n    for (let i\
        \ = 0; i < nums.length; i++) {\n        let sum = 0;\n        let num = nums[i];\n\
        \        while (num > 0) {\n            sum += num % 10;\n            num =\
        \ Math.floor(num / 10);\n        }\n        if (sum === i) {\n            return\
        \ i;\n        }\n    }\n    return -1;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function smallestIndex($nums) {\n        for ($i = 0;\
        \ $i < count($nums); $i++) {\n            $sum = 0;\n            $num = $nums[$i];\n\
        \            while ($num > 0) {\n                $sum += $num % 10;\n      \
        \          $num = (int)($num / 10);\n            }\n            if ($sum ===\
        \ $i) {\n                return $i;\n            }\n        }\n        return\
        \ -1;\n    }\n}"
      swift: "class Solution {\n    func smallestIndex(_ nums: [Int]) -> Int {\n   \
        \     for (i, num) in nums.enumerated() {\n            var sum = 0\n       \
        \     var n = num\n            while n > 0 {\n                sum += n % 10\n\
        \                n /= 10\n            }\n            if sum == i {\n       \
        \         return i\n            }\n        }\n        return -1\n    }\n}"
      kotlin: "class Solution {\n    fun smallestIndex(nums: IntArray): Int {\n    \
        \    for (i in nums.indices) {\n            var sum = 0\n            var num\
        \ = nums[i]\n            while (num > 0) {\n                sum += num % 10\n\
        \                num /= 10\n            }\n            if (sum == i) {\n   \
        \             return i\n            }\n        }\n        return -1\n    }\n\
        }"
      dart: "class Solution {\n  int smallestIndex(List<int> nums) {\n    for (int i\
        \ = 0; i < nums.length; i++) {\n      int sum = 0;\n      int num = nums[i];\n\
        \      while (num > 0) {\n        sum += num % 10;\n        num ~/= 10;\n  \
        \    }\n      if (sum == i) {\n        return i;\n      }\n    }\n    return\
        \ -1;\n  }\n}"
      go: "func smallestIndex(nums []int) int {\n    for i, num := range nums {\n  \
        \      sum := 0\n        temp := num\n        for temp > 0 {\n            sum\
        \ += temp % 10\n            temp /= 10\n        }\n        if sum == i {\n \
        \           return i\n        }\n    }\n    return -1\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef smallest_index(nums)\n\
        \  nums.each_with_index do |num, i|\n    return i if num.digits.sum == i\n \
        \ end\n  -1\nend"
      scala: "object Solution {\n  def smallestIndex(nums: Array[Int]): Int = {\n  \
        \  for (i <- nums.indices) {\n      var sum = 0\n      var n = nums(i)\n   \
        \   while (n > 0) {\n        sum += n % 10\n        n /= 10\n      }\n     \
        \ if (sum == i) return i\n    }\n    -1\n  }\n}"
      rust: "impl Solution {\n  pub fn smallest_index(nums: Vec<i32>) -> i32 {\n   \
        \ for (i, &num) in nums.iter().enumerate() {\n      let mut sum = 0;\n     \
        \ let mut n = num;\n      while n > 0 {\n        sum += n % 10;\n        n /=\
        \ 10;\n      }\n      if sum == (i as i32) {\n        return i as i32;\n   \
        \   }\n    }\n    -1\n  }\n}"
      racket: "(define/contract (smallest-index nums)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (define (digit-sum n)\n    (if (= n 0)\n        0\n   \
        \     (+ (remainder n 10) (digit-sum (quotient n 10)))))\n  (let loop ([i 0]\
        \ [l nums])\n    (cond\n      [(null? l) -1]\n      [(= (digit-sum (car l))\
        \ i) i]\n      [else (loop (+ i 1) (cdr l))]))\n)"
      erlang: "-spec smallest_index(Nums :: [integer()]) -> integer().\nsmallest_index(Nums)\
        \ ->\n  find_index(Nums, 0).\n\nfind_index([], _) ->\n  -1;\nfind_index([H|T],\
        \ Index) ->\n  case digit_sum(H) =:= Index of\n    true -> Index;\n    false\
        \ -> find_index(T, Index + 1)\n  end.\n\ndigit_sum(0) ->\n  0;\ndigit_sum(N)\
        \ ->\n  (N rem 10) + digit_sum(N div 10)."
      elixir: "defmodule Solution do\n  @spec smallest_index(nums :: [integer]) :: integer\n\
        \  def smallest_index(nums) do\n    nums\n    |> Enum.with_index()\n    |> Enum.find_value(-1,\
        \ fn {num, i} ->\n      if digit_sum(num) == i, do: i, else: nil\n    end)\n\
        \  end\n\n  defp digit_sum(0), do: 0\n  defp digit_sum(n), do: rem(n, 10) +\
        \ digit_sum(div(n, 10))\nend"
    approach: 'The algorithm employs a single linear scan of the input array starting
      from the first index (i = 0) and proceeding toward the end. For each element at
      index i, we calculate the sum of its digits by extracting each digit one by one
      using the modulo operator and integer division. By iterating from index 0 upward,
      the first index that satisfies the condition ''sum of digits equals index'' is
      guaranteed to be the smallest such index.


      In each iteration, if the calculated digit sum matches the current index, the
      function immediately returns that index. This early termination ensures efficiency.
      If the entire array is traversed and no such match is found, the function returns
      -1. Since the input values are bounded by 1000, the digit sum calculation involves
      at most four digits, making each step of the process constant in time relative
      to the number size.'
    time_complexity: O(N) where N is the length of the input array. For each of the
      N elements, we perform a digit sum calculation. Since the values in the array
      are at most 1000, the digit sum operation takes a maximum of four iterations per
      element, which is O(1). Thus, the total time complexity remains linear.
    space_complexity: O(1) as the solution only uses a few auxiliary integer variables
      to store the current sum, the temporary number being processed, and the loop counter.
      No additional data structures that scale with the input size are required.
    elapsed_time: 478.35411071777344
    model: gemini-3-flash-preview
    generated_at: '2026-09-24 02:38:02 '
---

## Problem #3550: Smallest Index With Digit Sum Equal to Index

**Difficulty:** Easy

**Topics:** Array, Math

## Problem Description

<p>You are given an integer array <code>nums</code>.</p>

<p>Return the <strong>smallest</strong> index <code>i</code> such that the sum of the digits of <code>nums[i]</code> is equal to <code>i</code>.</p>

<p>If no such index exists, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,3,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>For <code>nums[2] = 2</code>, the sum of digits is 2, which is equal to index <code>i = 2</code>. Thus, the output is 2.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,10,11]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>For <code>nums[1] = 10</code>, the sum of digits is <code>1 + 0 = 1</code>, which is equal to index <code>i = 1</code>.</li>
	<li>For <code>nums[2] = 11</code>, the sum of digits is <code>1 + 1 = 2</code>, which is equal to index <code>i = 2</code>.</li>
	<li>Since index 1 is the smallest, the output is 1.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Since no index satisfies the condition, the output is -1.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


## Hints

1. Simulate as described

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm employs a single linear scan of the input array starting from the first index (i = 0) and proceeding toward the end. For each element at index i, we calculate the sum of its digits by extracting each digit one by one using the modulo operator and integer division. By iterating from index 0 upward, the first index that satisfies the condition 'sum of digits equals index' is guaranteed to be the smallest such index.

In each iteration, if the calculated digit sum matches the current index, the function immediately returns that index. This early termination ensures efficiency. If the entire array is traversed and no such match is found, the function returns -1. Since the input values are bounded by 1000, the digit sum calculation involves at most four digits, making each step of the process constant in time relative to the number size.

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
    int smallestIndex(vector<int>& nums) {
        for (int i = 0; i < (int)nums.size(); ++i) {
            int sum = 0;
            int temp = nums[i];
            while (temp > 0) {
                sum += temp % 10;
                temp /= 10;
            }
            if (sum == i) {
                return i;
            }
        }
        return -1;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int smallestIndex(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            int sum = 0;
            int temp = nums[i];
            while (temp > 0) {
                sum += temp % 10;
                temp /= 10;
            }
            if (sum == i) {
                return i;
            }
        }
        return -1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            digit_sum = 0
            temp = nums[i]
            while temp > 0:
                digit_sum += temp % 10
                temp //= 10
            if digit_sum == i:
                return i
        return -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            digit_sum = 0
            temp = nums[i]
            while temp > 0:
                digit_sum += temp % 10
                temp //= 10
            if digit_sum == i:
                return i
        return -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int smallestIndex(int* nums, int numsSize) {
    for (int i = 0; i < numsSize; i++) {
        int sum = 0;
        int temp = nums[i];
        while (temp > 0) {
            sum += temp % 10;
            temp /= 10;
        }
        if (sum == i) {
            return i;
        }
    }
    return -1;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int SmallestIndex(int[] nums) {
        for (int i = 0; i < nums.Length; i++) {
            int sum = 0;
            int temp = nums[i];
            while (temp > 0) {
                sum += temp % 10;
                temp /= 10;
            }
            if (sum == i) {
                return i;
            }
        }
        return -1;
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
var smallestIndex = function(nums) {
    for (let i = 0; i < nums.length; i++) {
        let sum = 0;
        let temp = nums[i];
        while (temp > 0) {
            sum += temp % 10;
            temp = Math.floor(temp / 10);
        }
        if (sum === i) {
            return i;
        }
    }
    return -1;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function smallestIndex(nums: number[]): number {
    for (let i = 0; i < nums.length; i++) {
        let sum = 0;
        let num = nums[i];
        while (num > 0) {
            sum += num % 10;
            num = Math.floor(num / 10);
        }
        if (sum === i) {
            return i;
        }
    }
    return -1;
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
    function smallestIndex($nums) {
        for ($i = 0; $i < count($nums); $i++) {
            $sum = 0;
            $num = $nums[$i];
            while ($num > 0) {
                $sum += $num % 10;
                $num = (int)($num / 10);
            }
            if ($sum === $i) {
                return $i;
            }
        }
        return -1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func smallestIndex(_ nums: [Int]) -> Int {
        for (i, num) in nums.enumerated() {
            var sum = 0
            var n = num
            while n > 0 {
                sum += n % 10
                n /= 10
            }
            if sum == i {
                return i
            }
        }
        return -1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun smallestIndex(nums: IntArray): Int {
        for (i in nums.indices) {
            var sum = 0
            var num = nums[i]
            while (num > 0) {
                sum += num % 10
                num /= 10
            }
            if (sum == i) {
                return i
            }
        }
        return -1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int smallestIndex(List<int> nums) {
    for (int i = 0; i < nums.length; i++) {
      int sum = 0;
      int num = nums[i];
      while (num > 0) {
        sum += num % 10;
        num ~/= 10;
      }
      if (sum == i) {
        return i;
      }
    }
    return -1;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func smallestIndex(nums []int) int {
    for i, num := range nums {
        sum := 0
        temp := num
        for temp > 0 {
            sum += temp % 10
            temp /= 10
        }
        if sum == i {
            return i
        }
    }
    return -1
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def smallest_index(nums)
  nums.each_with_index do |num, i|
    return i if num.digits.sum == i
  end
  -1
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def smallestIndex(nums: Array[Int]): Int = {
    for (i <- nums.indices) {
      var sum = 0
      var n = nums(i)
      while (n > 0) {
        sum += n % 10
        n /= 10
      }
      if (sum == i) return i
    }
    -1
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
  pub fn smallest_index(nums: Vec<i32>) -> i32 {
    for (i, &num) in nums.iter().enumerate() {
      let mut sum = 0;
      let mut n = num;
      while n > 0 {
        sum += n % 10;
        n /= 10;
      }
      if sum == (i as i32) {
        return i as i32;
      }
    }
    -1
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (smallest-index nums)
  (-> (listof exact-integer?) exact-integer?)
  (define (digit-sum n)
    (if (= n 0)
        0
        (+ (remainder n 10) (digit-sum (quotient n 10)))))
  (let loop ([i 0] [l nums])
    (cond
      [(null? l) -1]
      [(= (digit-sum (car l)) i) i]
      [else (loop (+ i 1) (cdr l))]))
)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec smallest_index(Nums :: [integer()]) -> integer().
smallest_index(Nums) ->
  find_index(Nums, 0).

find_index([], _) ->
  -1;
find_index([H|T], Index) ->
  case digit_sum(H) =:= Index of
    true -> Index;
    false -> find_index(T, Index + 1)
  end.

digit_sum(0) ->
  0;
digit_sum(N) ->
  (N rem 10) + digit_sum(N div 10).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec smallest_index(nums :: [integer]) :: integer
  def smallest_index(nums) do
    nums
    |> Enum.with_index()
    |> Enum.find_value(-1, fn {num, i} ->
      if digit_sum(num) == i, do: i, else: nil
    end)
  end

  defp digit_sum(0), do: 0
  defp digit_sum(n), do: rem(n, 10) + digit_sum(div(n, 10))
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) where N is the length of the input array. For each of the N elements, we perform a digit sum calculation. Since the values in the array are at most 1000, the digit sum operation takes a maximum of four iterations per element, which is O(1). Thus, the total time complexity remains linear.
- **Space Complexity:** O(1) as the solution only uses a few auxiliary integer variables to store the current sum, the temporary number being processed, and the loop counter. No additional data structures that scale with the input size are required.
