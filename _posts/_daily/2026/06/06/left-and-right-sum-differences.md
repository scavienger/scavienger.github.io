---
layout: post
title: "Left and Right Sum Differences"
date: 2026-06-06 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Prefix Sum"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/left-and-right-sum-differences/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> leftRightDifference(vector<int>&\
        \ nums) {\n        int n = nums.size();\n        int totalSum = 0;\n       \
        \ for (int num : nums) {\n            totalSum += num;\n        }\n\n      \
        \  vector<int> answer(n);\n        int leftSum = 0;\n        for (int i = 0;\
        \ i < n; ++i) {\n            int rightSum = totalSum - leftSum - nums[i];\n\
        \            answer[i] = abs(leftSum - rightSum);\n            leftSum += nums[i];\n\
        \        }\n\n        return answer;\n    }\n};"
      java: "class Solution {\n    public int[] leftRightDifference(int[] nums) {\n\
        \        int n = nums.length;\n        int totalSum = 0;\n        for (int num\
        \ : nums) {\n            totalSum += num;\n        }\n\n        int[] answer\
        \ = new int[n];\n        int leftSum = 0;\n        for (int i = 0; i < n; i++)\
        \ {\n            int rightSum = totalSum - leftSum - nums[i];\n            answer[i]\
        \ = Math.abs(leftSum - rightSum);\n            leftSum += nums[i];\n       \
        \ }\n\n        return answer;\n    }\n}"
      python: "class Solution(object):\n    def leftRightDifference(self, nums):\n \
        \       \"\"\"\n        :type nums: List[int]\n        :rtype: List[int]\n \
        \       \"\"\"\n        total_sum = sum(nums)\n        left_sum = 0\n      \
        \  answer = []\n\n        for num in nums:\n            right_sum = total_sum\
        \ - left_sum - num\n            answer.append(abs(left_sum - right_sum))\n \
        \           left_sum += num\n\n        return answer"
      python3: "class Solution:\n    def leftRightDifference(self, nums: List[int])\
        \ -> List[int]:\n        total_sum = sum(nums)\n        left_sum = 0\n     \
        \   answer = []\n\n        for num in nums:\n            right_sum = total_sum\
        \ - left_sum - num\n            answer.append(abs(left_sum - right_sum))\n \
        \           left_sum += num\n\n        return answer"
      c: "/**\n * Note: The returned array must be malloced, assume caller calls free().\n\
        \ */\nint* leftRightDifference(int* nums, int numsSize, int* returnSize) {\n\
        \    *returnSize = numsSize;\n    int* answer = (int*)malloc(numsSize * sizeof(int));\n\
        \n    long long totalSum = 0;\n    for (int i = 0; i < numsSize; i++) {\n  \
        \      totalSum += nums[i];\n    }\n\n    long long leftSum = 0;\n    for (int\
        \ i = 0; i < numsSize; i++) {\n        long long rightSum = totalSum - leftSum\
        \ - nums[i];\n        long long diff = leftSum - rightSum;\n        answer[i]\
        \ = (int)(diff < 0 ? -diff : diff);\n        leftSum += nums[i];\n    }\n\n\
        \    return answer;\n}"
      csharp: "public class Solution {\n    public int[] LeftRightDifference(int[] nums)\
        \ {\n        int n = nums.Length;\n        int totalSum = 0;\n        foreach\
        \ (int num in nums) {\n            totalSum += num;\n        }\n\n        int[]\
        \ answer = new int[n];\n        int leftSum = 0;\n        for (int i = 0; i\
        \ < n; i++) {\n            int rightSum = totalSum - leftSum - nums[i];\n  \
        \          answer[i] = Math.Abs(leftSum - rightSum);\n            leftSum +=\
        \ nums[i];\n        }\n\n        return answer;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number[]}\n */\nvar leftRightDifference\
        \ = function(nums) {\n    const n = nums.length;\n    let totalSum = 0;\n  \
        \  for (let i = 0; i < n; i++) {\n        totalSum += nums[i];\n    }\n\n  \
        \  const answer = new Array(n);\n    let leftSum = 0;\n    for (let i = 0; i\
        \ < n; i++) {\n        let rightSum = totalSum - leftSum - nums[i];\n      \
        \  answer[i] = Math.abs(leftSum - rightSum);\n        leftSum += nums[i];\n\
        \    }\n\n    return answer;\n};"
      typescript: "function leftRightDifference(nums: number[]): number[] {\n    const\
        \ n = nums.length;\n    let totalSum = 0;\n    for (const num of nums) {\n \
        \       totalSum += num;\n    }\n\n    const answer: number[] = new Array(n);\n\
        \    let leftSum = 0;\n    for (let i = 0; i < n; i++) {\n        const rightSum\
        \ = totalSum - leftSum - nums[i];\n        answer[i] = Math.abs(leftSum - rightSum);\n\
        \        leftSum += nums[i];\n    }\n\n    return answer;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer[]\n     */\n    function leftRightDifference($nums) {\n        $n\
        \ = count($nums);\n        $totalSum = array_sum($nums);\n        $leftSum =\
        \ 0;\n        $answer = [];\n\n        for ($i = 0; $i < $n; $i++) {\n     \
        \       $rightSum = $totalSum - $leftSum - $nums[$i];\n            $answer[]\
        \ = abs($leftSum - $rightSum);\n            $leftSum += $nums[$i];\n       \
        \ }\n\n        return $answer;\n    }\n}"
      swift: "class Solution {\n    func leftRightDifference(_ nums: [Int]) -> [Int]\
        \ {\n        let n = nums.count\n        var totalSum = 0\n        for num in\
        \ nums {\n            totalSum += num\n        }\n\n        var leftSum = 0\n\
        \        var answer = [Int]()\n\n        for i in 0..<n {\n            let rightSum\
        \ = totalSum - leftSum - nums[i]\n            answer.append(abs(leftSum - rightSum))\n\
        \            leftSum += nums[i]\n        }\n\n        return answer\n    }\n\
        }"
      kotlin: "class Solution {\n    fun leftRightDifference(nums: IntArray): IntArray\
        \ {\n        val n = nums.size\n        var totalSum = 0\n        for (num in\
        \ nums) {\n            totalSum += num\n        }\n\n        val answer = IntArray(n)\n\
        \        var leftSum = 0\n\n        for (i in 0 until n) {\n            val\
        \ rightSum = totalSum - leftSum - nums[i]\n            answer[i] = Math.abs(leftSum\
        \ - rightSum)\n            leftSum += nums[i]\n        }\n\n        return answer\n\
        \    }\n}"
      dart: "class Solution {\n  List<int> leftRightDifference(List<int> nums) {\n \
        \   int n = nums.length;\n    int totalSum = 0;\n    for (int num in nums) {\n\
        \        totalSum += num;\n    }\n\n    List<int> answer = [];\n    int leftSum\
        \ = 0;\n\n    for (int i = 0; i < n; i++) {\n      int rightSum = totalSum -\
        \ leftSum - nums[i];\n      answer.add((leftSum - rightSum).abs());\n      leftSum\
        \ += nums[i];\n    }\n\n    return answer;\n  }\n}"
      go: "func leftRightDifference(nums []int) []int {\n    n := len(nums)\n    totalSum\
        \ := 0\n    for _, num := range nums {\n        totalSum += num\n    }\n\n \
        \   answer := make([]int, n)\n    leftSum := 0\n\n    for i := 0; i < n; i++\
        \ {\n        rightSum := totalSum - leftSum - nums[i]\n        diff := leftSum\
        \ - rightSum\n        if diff < 0 {\n            diff = -diff\n        }\n \
        \       answer[i] = diff\n        leftSum += nums[i]\n    }\n\n    return answer\n\
        }"
      ruby: "# @param {Integer[]} nums\n# @return {Integer[]}\ndef left_right_difference(nums)\n\
        \  total_sum = nums.sum\n  left_sum = 0\n  nums.map do |n|\n    right_sum =\
        \ total_sum - left_sum - n\n    diff = (left_sum - right_sum).abs\n    left_sum\
        \ += n\n    diff\n  end\nend"
      scala: "object Solution {\n    def leftRightDifference(nums: Array[Int]): Array[Int]\
        \ = {\n        val totalSum = nums.sum\n        var leftSum = 0\n        nums.map\
        \ { n =>\n            val rightSum = totalSum - leftSum - n\n            val\
        \ diff = math.abs(leftSum - rightSum)\n            leftSum += n\n          \
        \  diff\n        }\n    }\n}"
      rust: "impl Solution {\n    pub fn left_right_difference(nums: Vec<i32>) -> Vec<i32>\
        \ {\n        let total_sum: i32 = nums.iter().sum();\n        let mut left_sum\
        \ = 0;\n        nums.into_iter().map(|n| {\n            let right_sum = total_sum\
        \ - left_sum - n;\n            let diff = (left_sum - right_sum).abs();\n  \
        \          left_sum += n;\n            diff\n        }).collect()\n    }\n}"
      racket: "(define/contract (left-right-difference nums)\n  (-> (listof exact-integer?)\
        \ (listof exact-integer?))\n  (let ([total-sum (apply + nums)])\n    (let loop\
        \ ([ns nums] [l-sum 0] [res '()])\n      (if (null? ns)\n          (reverse\
        \ res)\n          (let* ([n (car ns)]\n                 [r-sum (- total-sum\
        \ l-sum n)]\n                 [diff (abs (- l-sum r-sum))])\n            (loop\
        \ (cdr ns) (+ l-sum n) (cons diff res)))))))"
      erlang: "-spec left_right_difference(Nums :: [integer()]) -> [integer()].\nleft_right_difference(Nums)\
        \ ->\n  TotalSum = lists:sum(Nums),\n  solve(Nums, 0, TotalSum).\n\nsolve([],\
        \ _LeftSum, _TotalSum) -> [];\nsolve([H | T], LeftSum, TotalSum) ->\n  RightSum\
        \ = TotalSum - LeftSum - H,\n  Diff = abs(LeftSum - RightSum),\n  [Diff | solve(T,\
        \ LeftSum + H, TotalSum)]."
      elixir: "defmodule Solution do\n  @spec left_right_difference(nums :: [integer])\
        \ :: [integer]\n  def left_right_difference(nums) do\n    total_sum = Enum.sum(nums)\n\
        \    {result, _} = Enum.map_reduce(nums, 0, fn n, left_sum ->\n      right_sum\
        \ = total_sum - left_sum - n\n      diff = abs(left_sum - right_sum)\n     \
        \ {diff, left_sum + n}\n    end)\n    result\n  end\nend"
    approach: 'To solve this problem efficiently, we first compute the total sum of
      all elements in the input array. We then iterate through the array once more,
      maintaining a running prefix sum which represents the ''leftSum'' for the current
      index. For any given index i, the ''rightSum'' can be calculated by subtracting
      the current element and the ''leftSum'' from the total sum of the array.


      At each step, we compute the absolute difference between the ''leftSum'' and the
      ''rightSum'' and store it in the result array. After computing the difference
      for the current index, we update the ''leftSum'' by adding the value of the current
      element before moving to the next index. This approach ensures that we determine
      the result in linear time using a single pass for calculations after the initial
      sum.'
    time_complexity: O(n) where n is the length of the input array. We traverse the
      array once to calculate the total sum and once more to compute the left sum, right
      sum, and the resulting absolute differences.
    space_complexity: O(1) auxiliary space if the output array is excluded from the
      calculation. If the output array is included, the space complexity is O(n) to
      store the result of the differences.
    elapsed_time: 193.2130787372589
    model: gemini-3-flash-preview
    generated_at: '2026-06-06 02:32:57 '
---

## Problem #2574: Left and Right Sum Differences

**Difficulty:** Easy

**Topics:** Array, Prefix Sum

## Problem Description

<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> of size <code>n</code>.</p>

<p>Define two arrays <code>leftSum</code> and <code>rightSum</code> where:</p>

<ul>
	<li><code>leftSum[i]</code> is the sum of elements to the left of the index <code>i</code> in the array <code>nums</code>. If there is no such element, <code>leftSum[i] = 0</code>.</li>
	<li><code>rightSum[i]</code> is the sum of elements to the right of the index <code>i</code> in the array <code>nums</code>. If there is no such element, <code>rightSum[i] = 0</code>.</li>
</ul>

<p>Return an integer array <code>answer</code> of size <code>n</code> where <code>answer[i] = |leftSum[i] - rightSum[i]|</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,4,8,3]
<strong>Output:</strong> [15,1,11,22]
<strong>Explanation:</strong> The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> [0]
<strong>Explanation:</strong> The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. For each index i, maintain two variables leftSum and rightSum.

2. Iterate on the range j: [0 … i - 1] and add nums[j] to the leftSum and similarly iterate on the range j: [i + 1 … nums.length - 1] and add nums[j] to the rightSum.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To solve this problem efficiently, we first compute the total sum of all elements in the input array. We then iterate through the array once more, maintaining a running prefix sum which represents the 'leftSum' for the current index. For any given index i, the 'rightSum' can be calculated by subtracting the current element and the 'leftSum' from the total sum of the array.

At each step, we compute the absolute difference between the 'leftSum' and the 'rightSum' and store it in the result array. After computing the difference for the current index, we update the 'leftSum' by adding the value of the current element before moving to the next index. This approach ensures that we determine the result in linear time using a single pass for calculations after the initial sum.

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
    vector<int> leftRightDifference(vector<int>& nums) {
        int n = nums.size();
        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }

        vector<int> answer(n);
        int leftSum = 0;
        for (int i = 0; i < n; ++i) {
            int rightSum = totalSum - leftSum - nums[i];
            answer[i] = abs(leftSum - rightSum);
            leftSum += nums[i];
        }

        return answer;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int[] leftRightDifference(int[] nums) {
        int n = nums.length;
        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }

        int[] answer = new int[n];
        int leftSum = 0;
        for (int i = 0; i < n; i++) {
            int rightSum = totalSum - leftSum - nums[i];
            answer[i] = Math.abs(leftSum - rightSum);
            leftSum += nums[i];
        }

        return answer;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total_sum = sum(nums)
        left_sum = 0
        answer = []

        for num in nums:
            right_sum = total_sum - left_sum - num
            answer.append(abs(left_sum - right_sum))
            left_sum += num

        return answer
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        left_sum = 0
        answer = []

        for num in nums:
            right_sum = total_sum - left_sum - num
            answer.append(abs(left_sum - right_sum))
            left_sum += num

        return answer
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* leftRightDifference(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    int* answer = (int*)malloc(numsSize * sizeof(int));

    long long totalSum = 0;
    for (int i = 0; i < numsSize; i++) {
        totalSum += nums[i];
    }

    long long leftSum = 0;
    for (int i = 0; i < numsSize; i++) {
        long long rightSum = totalSum - leftSum - nums[i];
        long long diff = leftSum - rightSum;
        answer[i] = (int)(diff < 0 ? -diff : diff);
        leftSum += nums[i];
    }

    return answer;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int[] LeftRightDifference(int[] nums) {
        int n = nums.Length;
        int totalSum = 0;
        foreach (int num in nums) {
            totalSum += num;
        }

        int[] answer = new int[n];
        int leftSum = 0;
        for (int i = 0; i < n; i++) {
            int rightSum = totalSum - leftSum - nums[i];
            answer[i] = Math.Abs(leftSum - rightSum);
            leftSum += nums[i];
        }

        return answer;
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
 * @return {number[]}
 */
var leftRightDifference = function(nums) {
    const n = nums.length;
    let totalSum = 0;
    for (let i = 0; i < n; i++) {
        totalSum += nums[i];
    }

    const answer = new Array(n);
    let leftSum = 0;
    for (let i = 0; i < n; i++) {
        let rightSum = totalSum - leftSum - nums[i];
        answer[i] = Math.abs(leftSum - rightSum);
        leftSum += nums[i];
    }

    return answer;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function leftRightDifference(nums: number[]): number[] {
    const n = nums.length;
    let totalSum = 0;
    for (const num of nums) {
        totalSum += num;
    }

    const answer: number[] = new Array(n);
    let leftSum = 0;
    for (let i = 0; i < n; i++) {
        const rightSum = totalSum - leftSum - nums[i];
        answer[i] = Math.abs(leftSum - rightSum);
        leftSum += nums[i];
    }

    return answer;
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
     * @return Integer[]
     */
    function leftRightDifference($nums) {
        $n = count($nums);
        $totalSum = array_sum($nums);
        $leftSum = 0;
        $answer = [];

        for ($i = 0; $i < $n; $i++) {
            $rightSum = $totalSum - $leftSum - $nums[$i];
            $answer[] = abs($leftSum - $rightSum);
            $leftSum += $nums[$i];
        }

        return $answer;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func leftRightDifference(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var totalSum = 0
        for num in nums {
            totalSum += num
        }

        var leftSum = 0
        var answer = [Int]()

        for i in 0..<n {
            let rightSum = totalSum - leftSum - nums[i]
            answer.append(abs(leftSum - rightSum))
            leftSum += nums[i]
        }

        return answer
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun leftRightDifference(nums: IntArray): IntArray {
        val n = nums.size
        var totalSum = 0
        for (num in nums) {
            totalSum += num
        }

        val answer = IntArray(n)
        var leftSum = 0

        for (i in 0 until n) {
            val rightSum = totalSum - leftSum - nums[i]
            answer[i] = Math.abs(leftSum - rightSum)
            leftSum += nums[i]
        }

        return answer
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<int> leftRightDifference(List<int> nums) {
    int n = nums.length;
    int totalSum = 0;
    for (int num in nums) {
        totalSum += num;
    }

    List<int> answer = [];
    int leftSum = 0;

    for (int i = 0; i < n; i++) {
      int rightSum = totalSum - leftSum - nums[i];
      answer.add((leftSum - rightSum).abs());
      leftSum += nums[i];
    }

    return answer;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func leftRightDifference(nums []int) []int {
    n := len(nums)
    totalSum := 0
    for _, num := range nums {
        totalSum += num
    }

    answer := make([]int, n)
    leftSum := 0

    for i := 0; i < n; i++ {
        rightSum := totalSum - leftSum - nums[i]
        diff := leftSum - rightSum
        if diff < 0 {
            diff = -diff
        }
        answer[i] = diff
        leftSum += nums[i]
    }

    return answer
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer[]}
def left_right_difference(nums)
  total_sum = nums.sum
  left_sum = 0
  nums.map do |n|
    right_sum = total_sum - left_sum - n
    diff = (left_sum - right_sum).abs
    left_sum += n
    diff
  end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def leftRightDifference(nums: Array[Int]): Array[Int] = {
        val totalSum = nums.sum
        var leftSum = 0
        nums.map { n =>
            val rightSum = totalSum - leftSum - n
            val diff = math.abs(leftSum - rightSum)
            leftSum += n
            diff
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
    pub fn left_right_difference(nums: Vec<i32>) -> Vec<i32> {
        let total_sum: i32 = nums.iter().sum();
        let mut left_sum = 0;
        nums.into_iter().map(|n| {
            let right_sum = total_sum - left_sum - n;
            let diff = (left_sum - right_sum).abs();
            left_sum += n;
            diff
        }).collect()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (left-right-difference nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let ([total-sum (apply + nums)])
    (let loop ([ns nums] [l-sum 0] [res '()])
      (if (null? ns)
          (reverse res)
          (let* ([n (car ns)]
                 [r-sum (- total-sum l-sum n)]
                 [diff (abs (- l-sum r-sum))])
            (loop (cdr ns) (+ l-sum n) (cons diff res)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec left_right_difference(Nums :: [integer()]) -> [integer()].
left_right_difference(Nums) ->
  TotalSum = lists:sum(Nums),
  solve(Nums, 0, TotalSum).

solve([], _LeftSum, _TotalSum) -> [];
solve([H | T], LeftSum, TotalSum) ->
  RightSum = TotalSum - LeftSum - H,
  Diff = abs(LeftSum - RightSum),
  [Diff | solve(T, LeftSum + H, TotalSum)].
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec left_right_difference(nums :: [integer]) :: [integer]
  def left_right_difference(nums) do
    total_sum = Enum.sum(nums)
    {result, _} = Enum.map_reduce(nums, 0, fn n, left_sum ->
      right_sum = total_sum - left_sum - n
      diff = abs(left_sum - right_sum)
      {diff, left_sum + n}
    end)
    result
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the input array. We traverse the array once to calculate the total sum and once more to compute the left sum, right sum, and the resulting absolute differences.
- **Space Complexity:** O(1) auxiliary space if the output array is excluded from the calculation. If the output array is included, the space complexity is O(n) to store the result of the differences.
