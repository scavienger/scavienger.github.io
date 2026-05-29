---
layout: post
title: "Minimum Element After Replacement With Digit Sum"
date: 2026-05-29 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Math"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minElement(vector<int>& nums) {\n   \
        \     int min_val = 1e9;\n        for (int num : nums) {\n            int sum\
        \ = 0;\n            int temp = num;\n            while (temp > 0) {\n      \
        \          sum += temp % 10;\n                temp /= 10;\n            }\n \
        \           if (sum < min_val) {\n                min_val = sum;\n         \
        \   }\n        }\n        return min_val;\n    }\n};"
      java: "class Solution {\n    public int minElement(int[] nums) {\n        int\
        \ minVal = Integer.MAX_VALUE;\n        for (int num : nums) {\n            int\
        \ sum = 0;\n            int temp = num;\n            while (temp > 0) {\n  \
        \              sum += temp % 10;\n                temp /= 10;\n            }\n\
        \            if (sum < minVal) {\n                minVal = sum;\n          \
        \  }\n        }\n        return minVal;\n    }\n}"
      python: "class Solution(object):\n    def minElement(self, nums):\n        \"\"\
        \"\n        :type nums: List[int]\n        :rtype: int\n        \"\"\"\n   \
        \     min_val = float('inf')\n        for num in nums:\n            curr_sum\
        \ = 0\n            temp = num\n            while temp > 0:\n               \
        \ curr_sum += temp % 10\n                temp //= 10\n            if curr_sum\
        \ < min_val:\n                min_val = curr_sum\n        return int(min_val)"
      python3: "class Solution:\n    def minElement(self, nums: List[int]) -> int:\n\
        \        min_val = float('inf')\n        for num in nums:\n            curr_sum\
        \ = 0\n            temp = num\n            while temp > 0:\n               \
        \ curr_sum += temp % 10\n                temp //= 10\n            if curr_sum\
        \ < min_val:\n                min_val = curr_sum\n        return int(min_val)"
      c: "int minElement(int* nums, int numsSize) {\n    int min_val = 1000000;\n  \
        \  for (int i = 0; i < numsSize; i++) {\n        int sum = 0;\n        int temp\
        \ = nums[i];\n        while (temp > 0) {\n            sum += temp % 10;\n  \
        \          temp /= 10;\n        }\n        if (sum < min_val) {\n          \
        \  min_val = sum;\n        }\n    }\n    return min_val;\n}"
      csharp: "public class Solution {\n    public int MinElement(int[] nums) {\n  \
        \      int minVal = int.MaxValue;\n        foreach (int num in nums) {\n   \
        \         int sum = 0;\n            int temp = num;\n            while (temp\
        \ > 0) {\n                sum += temp % 10;\n                temp /= 10;\n \
        \           }\n            if (sum < minVal) {\n                minVal = sum;\n\
        \            }\n        }\n        return minVal;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar minElement\
        \ = function(nums) {\n    let minVal = Infinity;\n    for (let num of nums)\
        \ {\n        let sum = 0;\n        let temp = num;\n        while (temp > 0)\
        \ {\n            sum += temp % 10;\n            temp = Math.floor(temp / 10);\n\
        \        }\n        if (sum < minVal) {\n            minVal = sum;\n       \
        \ }\n    }\n    return minVal;\n};"
      typescript: "function minElement(nums: number[]): number {\n    let minVal = Infinity;\n\
        \    for (const n of nums) {\n        let sum = 0;\n        let temp = n;\n\
        \        while (temp > 0) {\n            sum += temp % 10;\n            temp\
        \ = Math.floor(temp / 10);\n        }\n        if (sum < minVal) {\n       \
        \     minVal = sum;\n        }\n    }\n    return minVal;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function minElement($nums) {\n        $minVal = 1000000;\n\
        \        foreach ($nums as $num) {\n            $sum = 0;\n            $temp\
        \ = $num;\n            while ($temp > 0) {\n                $sum += $temp %\
        \ 10;\n                $temp = intdiv($temp, 10);\n            }\n         \
        \   if ($sum < $minVal) {\n                $minVal = $sum;\n            }\n\
        \        }\n        return $minVal;\n    }\n}"
      swift: "class Solution {\n    func minElement(_ nums: [Int]) -> Int {\n      \
        \  var minVal = Int.max\n        for n in nums {\n            var sum = 0\n\
        \            var temp = n\n            while temp > 0 {\n                sum\
        \ += temp % 10\n                temp /= 10\n            }\n            if sum\
        \ < minVal {\n                minVal = sum\n            }\n        }\n     \
        \   return minVal\n    }\n}"
      kotlin: "class Solution {\n    fun minElement(nums: IntArray): Int {\n       \
        \ var minVal = Int.MAX_VALUE\n        for (n in nums) {\n            var sum\
        \ = 0\n            var temp = n\n            while (temp > 0) {\n          \
        \      sum += temp % 10\n                temp /= 10\n            }\n       \
        \     if (sum < minVal) {\n                minVal = sum\n            }\n   \
        \     }\n        return minVal\n    }\n}"
      dart: "class Solution {\n  int minElement(List<int> nums) {\n    int minVal =\
        \ 1000000;\n    for (int n in nums) {\n      int sum = 0;\n      int temp =\
        \ n;\n      while (temp > 0) {\n        sum += temp % 10;\n        temp ~/=\
        \ 10;\n      }\n      if (sum < minVal) {\n        minVal = sum;\n      }\n\
        \    }\n    return minVal;\n  }\n}"
      go: "func minElement(nums []int) int {\n    minVal := 1000000\n    for _, n :=\
        \ range nums {\n        sum := 0\n        temp := n\n        for temp > 0 {\n\
        \            sum += temp % 10\n            temp /= 10\n        }\n        if\
        \ sum < minVal {\n            minVal = sum\n        }\n    }\n    return minVal\n\
        }"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef min_element(nums)\n\
        \  nums.map { |n| n.digits.sum }.min\nend"
      scala: "object Solution {\n    def minElement(nums: Array[Int]): Int = {\n   \
        \     nums.map { n =>\n            var sum = 0\n            var temp = n\n \
        \           while (temp > 0) {\n                sum += temp % 10\n         \
        \       temp /= 10\n            }\n            sum\n        }.min\n    }\n}"
      rust: "impl Solution {\n    pub fn min_element(nums: Vec<i32>) -> i32 {\n    \
        \    nums.iter().map(|&n| {\n            let mut sum = 0;\n            let mut\
        \ temp = n;\n            while temp > 0 {\n                sum += temp % 10;\n\
        \                temp /= 10;\n            }\n            sum\n        }).min().unwrap()\n\
        \    }\n}"
      racket: "(define/contract (min-element nums)\n  (-> (listof exact-integer?) exact-integer?)\n\
        \  (apply min (map (lambda (n)\n                    (let loop ([v n] [s 0])\n\
        \                      (if (zero? v)\n                          s\n        \
        \                  (loop (quotient v 10) (+ s (remainder v 10))))))\n      \
        \            nums)))"
      erlang: "-spec min_element(Nums :: [integer()]) -> integer().\nmin_element(Nums)\
        \ ->\n  lists:min([lists:sum([C - $0 || C <- integer_to_list(X)]) || X <- Nums])."
      elixir: "defmodule Solution do\n  @spec min_element(nums :: [integer]) :: integer\n\
        \  def min_element(nums) do\n    nums\n    |> Enum.map(fn n -> n |> Integer.digits()\
        \ |> Enum.sum() end)\n    |> Enum.min()\n  end\nend"
    approach: 'The algorithm processes the input array by iterating through each integer
      and calculating the sum of its individual digits. To compute the digit sum, the
      code repeatedly extracts the last digit using the modulo operator (number % 10)
      and then removes it using integer division (number / 10) until the value reaches
      zero. This mathematical approach is efficient as it avoids the overhead of converting
      numbers to strings.


      During the iteration, a global tracking variable is maintained to store the minimum
      digit sum encountered so far. By initializing this variable to a large value (or
      the first element''s digit sum) and updating it whenever a smaller sum is calculated,
      we can determine the minimum element in the transformed array in a single pass.
      This ensures that every element in the input array is visited exactly once.'
    time_complexity: O(n * log10(M)) where n is the length of the input array and M
      is the maximum value of an element in the array. Since the maximum value in the
      constraints is 10,000, the inner digit-sum loop runs at most 5 times for any number.
    space_complexity: O(1) because the algorithm only uses a fixed number of integer
      variables to store the current sum, the running minimum, and loop indices, regardless
      of the input size.
    elapsed_time: 255.5255036354065
    model: gemini-3-flash-preview
    generated_at: '2026-05-29 02:38:24 '
---

## Problem #3300: Minimum Element After Replacement With Digit Sum

**Difficulty:** Easy

**Topics:** Array, Math

## Problem Description

<p>You are given an integer array <code>nums</code>.</p>

<p>You replace each element in <code>nums</code> with the <strong>sum</strong> of its digits.</p>

<p>Return the <strong>minimum</strong> element in <code>nums</code> after all replacements.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [10,12,13,14]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p><code>nums</code> becomes <code>[1, 3, 4, 5]</code> after all replacements, with minimum element 1.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p><code>nums</code> becomes <code>[1, 2, 3, 4]</code> after all replacements, with minimum element 1.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [999,19,199]</span></p>

<p><strong>Output:</strong> <span class="example-io">10</span></p>

<p><strong>Explanation:</strong></p>

<p><code>nums</code> becomes <code>[27, 10, 19]</code> after all replacements, with minimum element 10.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## Hints

1. Convert to string and calculate the sum for each element.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm processes the input array by iterating through each integer and calculating the sum of its individual digits. To compute the digit sum, the code repeatedly extracts the last digit using the modulo operator (number % 10) and then removes it using integer division (number / 10) until the value reaches zero. This mathematical approach is efficient as it avoids the overhead of converting numbers to strings.

During the iteration, a global tracking variable is maintained to store the minimum digit sum encountered so far. By initializing this variable to a large value (or the first element's digit sum) and updating it whenever a smaller sum is calculated, we can determine the minimum element in the transformed array in a single pass. This ensures that every element in the input array is visited exactly once.

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
    int minElement(vector<int>& nums) {
        int min_val = 1e9;
        for (int num : nums) {
            int sum = 0;
            int temp = num;
            while (temp > 0) {
                sum += temp % 10;
                temp /= 10;
            }
            if (sum < min_val) {
                min_val = sum;
            }
        }
        return min_val;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minElement(int[] nums) {
        int minVal = Integer.MAX_VALUE;
        for (int num : nums) {
            int sum = 0;
            int temp = num;
            while (temp > 0) {
                sum += temp % 10;
                temp /= 10;
            }
            if (sum < minVal) {
                minVal = sum;
            }
        }
        return minVal;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = float('inf')
        for num in nums:
            curr_sum = 0
            temp = num
            while temp > 0:
                curr_sum += temp % 10
                temp //= 10
            if curr_sum < min_val:
                min_val = curr_sum
        return int(min_val)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_val = float('inf')
        for num in nums:
            curr_sum = 0
            temp = num
            while temp > 0:
                curr_sum += temp % 10
                temp //= 10
            if curr_sum < min_val:
                min_val = curr_sum
        return int(min_val)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int minElement(int* nums, int numsSize) {
    int min_val = 1000000;
    for (int i = 0; i < numsSize; i++) {
        int sum = 0;
        int temp = nums[i];
        while (temp > 0) {
            sum += temp % 10;
            temp /= 10;
        }
        if (sum < min_val) {
            min_val = sum;
        }
    }
    return min_val;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinElement(int[] nums) {
        int minVal = int.MaxValue;
        foreach (int num in nums) {
            int sum = 0;
            int temp = num;
            while (temp > 0) {
                sum += temp % 10;
                temp /= 10;
            }
            if (sum < minVal) {
                minVal = sum;
            }
        }
        return minVal;
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
var minElement = function(nums) {
    let minVal = Infinity;
    for (let num of nums) {
        let sum = 0;
        let temp = num;
        while (temp > 0) {
            sum += temp % 10;
            temp = Math.floor(temp / 10);
        }
        if (sum < minVal) {
            minVal = sum;
        }
    }
    return minVal;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minElement(nums: number[]): number {
    let minVal = Infinity;
    for (const n of nums) {
        let sum = 0;
        let temp = n;
        while (temp > 0) {
            sum += temp % 10;
            temp = Math.floor(temp / 10);
        }
        if (sum < minVal) {
            minVal = sum;
        }
    }
    return minVal;
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
    function minElement($nums) {
        $minVal = 1000000;
        foreach ($nums as $num) {
            $sum = 0;
            $temp = $num;
            while ($temp > 0) {
                $sum += $temp % 10;
                $temp = intdiv($temp, 10);
            }
            if ($sum < $minVal) {
                $minVal = $sum;
            }
        }
        return $minVal;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minElement(_ nums: [Int]) -> Int {
        var minVal = Int.max
        for n in nums {
            var sum = 0
            var temp = n
            while temp > 0 {
                sum += temp % 10
                temp /= 10
            }
            if sum < minVal {
                minVal = sum
            }
        }
        return minVal
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minElement(nums: IntArray): Int {
        var minVal = Int.MAX_VALUE
        for (n in nums) {
            var sum = 0
            var temp = n
            while (temp > 0) {
                sum += temp % 10
                temp /= 10
            }
            if (sum < minVal) {
                minVal = sum
            }
        }
        return minVal
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minElement(List<int> nums) {
    int minVal = 1000000;
    for (int n in nums) {
      int sum = 0;
      int temp = n;
      while (temp > 0) {
        sum += temp % 10;
        temp ~/= 10;
      }
      if (sum < minVal) {
        minVal = sum;
      }
    }
    return minVal;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minElement(nums []int) int {
    minVal := 1000000
    for _, n := range nums {
        sum := 0
        temp := n
        for temp > 0 {
            sum += temp % 10
            temp /= 10
        }
        if sum < minVal {
            minVal = sum
        }
    }
    return minVal
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def min_element(nums)
  nums.map { |n| n.digits.sum }.min
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minElement(nums: Array[Int]): Int = {
        nums.map { n =>
            var sum = 0
            var temp = n
            while (temp > 0) {
                sum += temp % 10
                temp /= 10
            }
            sum
        }.min
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_element(nums: Vec<i32>) -> i32 {
        nums.iter().map(|&n| {
            let mut sum = 0;
            let mut temp = n;
            while temp > 0 {
                sum += temp % 10;
                temp /= 10;
            }
            sum
        }).min().unwrap()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-element nums)
  (-> (listof exact-integer?) exact-integer?)
  (apply min (map (lambda (n)
                    (let loop ([v n] [s 0])
                      (if (zero? v)
                          s
                          (loop (quotient v 10) (+ s (remainder v 10))))))
                  nums)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_element(Nums :: [integer()]) -> integer().
min_element(Nums) ->
  lists:min([lists:sum([C - $0 || C <- integer_to_list(X)]) || X <- Nums]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_element(nums :: [integer]) :: integer
  def min_element(nums) do
    nums
    |> Enum.map(fn n -> n |> Integer.digits() |> Enum.sum() end)
    |> Enum.min()
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n * log10(M)) where n is the length of the input array and M is the maximum value of an element in the array. Since the maximum value in the constraints is 10,000, the inner digit-sum loop runs at most 5 times for any number.
- **Space Complexity:** O(1) because the algorithm only uses a fixed number of integer variables to store the current sum, the running minimum, and loop indices, regardless of the input size.
