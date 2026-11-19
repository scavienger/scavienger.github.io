---
layout: post
title: "Minimum Score by Changing Two Elements"
date: 2026-11-19 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Greedy", "Sorting"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-score-by-changing-two-elements/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minimizeSum(vector<int>& nums) {\n  \
        \      sort(nums.begin(), nums.end());\n        int n = nums.size();\n     \
        \   return min({nums[n - 1] - nums[2], nums[n - 2] - nums[1], nums[n - 3] -\
        \ nums[0]});\n    }\n};"
      java: "class Solution {\n    public int minimizeSum(int[] nums) {\n        Arrays.sort(nums);\n\
        \        int n = nums.length;\n        int ans = nums[n - 1] - nums[2];\n  \
        \      ans = Math.min(ans, nums[n - 2] - nums[1]);\n        ans = Math.min(ans,\
        \ nums[n - 3] - nums[0]);\n        return ans;\n    }\n}"
      python: "class Solution(object):\n    def minimizeSum(self, nums):\n        \"\
        \"\"\n        :type nums: List[int]\n        :rtype: int\n        \"\"\"\n \
        \       nums.sort()\n        return min(nums[-1] - nums[2], nums[-2] - nums[1],\
        \ nums[-3] - nums[0])"
      python3: "class Solution:\n    def minimizeSum(self, nums: List[int]) -> int:\n\
        \        nums.sort()\n        return min(nums[-1] - nums[2], nums[-2] - nums[1],\
        \ nums[-3] - nums[0])"
      c: "int cmp(const void* a, const void* b) {\n    int x = *(const int*)a;\n   \
        \ int y = *(const int*)b;\n    if (x < y) return -1;\n    if (x > y) return\
        \ 1;\n    return 0;\n}\n\nint minimizeSum(int* nums, int numsSize) {\n    qsort(nums,\
        \ numsSize, sizeof(int), cmp);\n    int ans = nums[numsSize - 1] - nums[2];\n\
        \    int opt2 = nums[numsSize - 2] - nums[1];\n    int opt3 = nums[numsSize\
        \ - 3] - nums[0];\n    if (opt2 < ans) ans = opt2;\n    if (opt3 < ans) ans\
        \ = opt3;\n    return ans;\n}"
      csharp: "public class Solution {\n    public int MinimizeSum(int[] nums) {\n \
        \       Array.Sort(nums);\n        int n = nums.Length;\n        return Math.Min(nums[n\
        \ - 1] - nums[2], Math.Min(nums[n - 2] - nums[1], nums[n - 3] - nums[0]));\n\
        \    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar minimizeSum\
        \ = function(nums) {\n    nums.sort((a, b) => a - b);\n    const n = nums.length;\n\
        \    return Math.min(nums[n - 1] - nums[2], nums[n - 2] - nums[1], nums[n -\
        \ 3] - nums[0]);\n};"
      typescript: "function minimizeSum(nums: number[]): number {\n    nums.sort((a,\
        \ b) => a - b);\n    const n = nums.length;\n    return Math.min(nums[n - 1]\
        \ - nums[2], nums[n - 2] - nums[1], nums[n - 3] - nums[0]);\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function minimizeSum($nums) {\n        sort($nums);\n\
        \        $n = count($nums);\n        return min($nums[$n - 1] - $nums[2], $nums[$n\
        \ - 2] - $nums[1], $nums[$n - 3] - $nums[0]);\n    }\n}"
      swift: "class Solution {\n    func minimizeSum(_ nums: [Int]) -> Int {\n     \
        \   let sortedNums = nums.sorted()\n        let n = sortedNums.count\n     \
        \   return min(sortedNums[n - 1] - sortedNums[2], sortedNums[n - 2] - sortedNums[1],\
        \ sortedNums[n - 3] - sortedNums[0])\n    }\n}"
      kotlin: "class Solution {\n    fun minimizeSum(nums: IntArray): Int {\n      \
        \  nums.sort()\n        val n = nums.size\n        return minOf(nums[n - 1]\
        \ - nums[2], nums[n - 2] - nums[1], nums[n - 3] - nums[0])\n    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int minimizeSum(List<int> nums)\
        \ {\n    nums.sort();\n    int n = nums.length;\n    int option1 = nums[n -\
        \ 1] - nums[2];\n    int option2 = nums[n - 2] - nums[1];\n    int option3 =\
        \ nums[n - 3] - nums[0];\n    return min(option1, min(option2, option3));\n\
        \  }\n}"
      go: "import \"sort\"\n\nfunc minimizeSum(nums []int) int {\n    sort.Ints(nums)\n\
        \    n := len(nums)\n    a := nums[n-1] - nums[2]\n    b := nums[n-2] - nums[1]\n\
        \    c := nums[n-3] - nums[0]\n\n    res := a\n    if b < res {\n        res\
        \ = b\n    }\n    if c < res {\n        res = c\n    }\n    return res\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef minimize_sum(nums)\n\
        \    nums.sort!\n    n = nums.length\n    [nums[n - 1] - nums[2], nums[n - 2]\
        \ - nums[1], nums[n - 3] - nums[0]].min\nend"
      scala: "import java.util.Arrays\n\nobject Solution {\n    def minimizeSum(nums:\
        \ Array[Int]): Int = {\n        Arrays.sort(nums)\n        val n = nums.length\n\
        \        val a = nums(n - 1) - nums(2)\n        val b = nums(n - 2) - nums(1)\n\
        \        val c = nums(n - 3) - nums(0)\n        math.min(a, math.min(b, c))\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn minimize_sum(nums: Vec<i32>) -> i32 {\n   \
        \     let mut nums = nums;\n        nums.sort();\n        let n = nums.len();\n\
        \        let opt1 = nums[n - 1] - nums[2];\n        let opt2 = nums[n - 2] -\
        \ nums[1];\n        let opt3 = nums[n - 3] - nums[0];\n        std::cmp::min(opt1,\
        \ std::cmp::min(opt2, opt3))\n    }\n}"
      racket: "(define/contract (minimize-sum nums)\n  (-> (listof exact-integer?) exact-integer?)\n\
        \  (let* ([sorted (sort nums <)]\n         [v (list->vector sorted)]\n     \
        \    [n (vector-length v)])\n    (min (- (vector-ref v (- n 1)) (vector-ref\
        \ v 2))\n         (- (vector-ref v (- n 2)) (vector-ref v 1))\n         (- (vector-ref\
        \ v (- n 3)) (vector-ref v 0)))))"
      erlang: "-spec minimize_sum(Nums :: [integer()]) -> integer().\nminimize_sum(Nums)\
        \ ->\n  Sorted = lists:sort(Nums),\n  N = length(Sorted),\n  Arr = list_to_tuple(Sorted),\n\
        \  Opt1 = element(N, Arr) - element(3, Arr),\n  Opt2 = element(N - 1, Arr) -\
        \ element(2, Arr),\n  Opt3 = element(N - 2, Arr) - element(1, Arr),\n  lists:min([Opt1,\
        \ Opt2, Opt3])."
      elixir: "defmodule Solution do\n  @spec minimize_sum(nums :: [integer]) :: integer\n\
        \  def minimize_sum(nums) do\n    sorted = Enum.sort(nums)\n    n = length(sorted)\n\
        \    arr = List.to_tuple(sorted)\n\n    opt1 = elem(arr, n - 1) - elem(arr,\
        \ 2)\n    opt2 = elem(arr, n - 2) - elem(arr, 1)\n    opt3 = elem(arr, n - 3)\
        \ - elem(arr, 0)\n\n    Enum.min([opt1, opt2, opt3])\n  end\nend"
    approach: 'The score of the array is the sum of the minimum and maximum absolute
      differences between any two elements. Since the array length is at least three,
      we can always choose to set one of the modified elements equal to an existing
      element, which makes the minimum absolute difference (the low score) equal to
      zero. Therefore, minimizing the total score reduces entirely to minimizing the
      high score, which is the difference between the maximum and minimum elements in
      the array after altering up to two values.


      Altering an element allows us to effectively remove it from defining the boundary
      values by setting its value inside the range of the remaining elements. By sorting
      the array in non-decreasing order, the optimal choices correspond to either removing
      the two largest elements, removing the two smallest elements, or removing one
      smallest and one largest element. Consequently, the minimum possible score is
      the minimum among nums[n - 3] - nums[0], nums[n - 1] - nums[2], and nums[n - 2]
      - nums[1].'
    time_complexity: O(n log n), where n is the number of elements in nums. This time
      is dominated by sorting the array. Once sorted, finding the answer takes O(1)
      time.
    space_complexity: O(1) auxiliary space beyond the memory needed by the sorting algorithm,
      which ranges from O(1) to O(n) depending on the language and standard library
      implementation.
    elapsed_time: 674.1346497535706
    model: gemini-3-flash-preview
    generated_at: '2026-11-19 05:31:06 '
---

## Problem #2567: Minimum Score by Changing Two Elements

**Difficulty:** Medium

**Topics:** Array, Greedy, Sorting

## Problem Description

<p>You are given an integer array <code>nums</code>.</p>

<ul>
	<li>The <strong>low</strong> score of <code>nums</code> is the <strong>minimum</strong> absolute difference between any two integers.</li>
	<li>The <strong>high</strong> score of <code>nums</code> is the <strong>maximum</strong> absolute difference between any two integers.</li>
	<li>The <strong>score</strong> of <code>nums</code> is the sum of the <strong>high</strong> and <strong>low</strong> scores.</li>
</ul>

<p>Return the <strong>minimum score</strong> after <strong>changing two elements</strong> of <code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,4,7,8,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Change <code>nums[0]</code> and <code>nums[1]</code> to be 6 so that <code>nums</code> becomes [6,6,7,8,5].</li>
	<li>The low score is the minimum absolute difference: |6 - 6| = 0.</li>
	<li>The high score is the maximum absolute difference: |8 - 5| = 3.</li>
	<li>The sum of high and low score is 3.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,4,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Change <code>nums[1]</code> and <code>nums[2]</code> to 1 so that <code>nums</code> becomes [1,1,1].</li>
	<li>The sum of maximum absolute difference and minimum absolute difference is 0.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. Changing the minimum or maximum values will only minimize the score.

2. Think about what all possible pairs of minimum and maximum values can be changed to form the minimum score.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The score of the array is the sum of the minimum and maximum absolute differences between any two elements. Since the array length is at least three, we can always choose to set one of the modified elements equal to an existing element, which makes the minimum absolute difference (the low score) equal to zero. Therefore, minimizing the total score reduces entirely to minimizing the high score, which is the difference between the maximum and minimum elements in the array after altering up to two values.

Altering an element allows us to effectively remove it from defining the boundary values by setting its value inside the range of the remaining elements. By sorting the array in non-decreasing order, the optimal choices correspond to either removing the two largest elements, removing the two smallest elements, or removing one smallest and one largest element. Consequently, the minimum possible score is the minimum among nums[n - 3] - nums[0], nums[n - 1] - nums[2], and nums[n - 2] - nums[1].

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
    int minimizeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        return min({nums[n - 1] - nums[2], nums[n - 2] - nums[1], nums[n - 3] - nums[0]});
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minimizeSum(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        int ans = nums[n - 1] - nums[2];
        ans = Math.min(ans, nums[n - 2] - nums[1]);
        ans = Math.min(ans, nums[n - 3] - nums[0]);
        return ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minimizeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return min(nums[-1] - nums[2], nums[-2] - nums[1], nums[-3] - nums[0])
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        return min(nums[-1] - nums[2], nums[-2] - nums[1], nums[-3] - nums[0])
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int cmp(const void* a, const void* b) {
    int x = *(const int*)a;
    int y = *(const int*)b;
    if (x < y) return -1;
    if (x > y) return 1;
    return 0;
}

int minimizeSum(int* nums, int numsSize) {
    qsort(nums, numsSize, sizeof(int), cmp);
    int ans = nums[numsSize - 1] - nums[2];
    int opt2 = nums[numsSize - 2] - nums[1];
    int opt3 = nums[numsSize - 3] - nums[0];
    if (opt2 < ans) ans = opt2;
    if (opt3 < ans) ans = opt3;
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinimizeSum(int[] nums) {
        Array.Sort(nums);
        int n = nums.Length;
        return Math.Min(nums[n - 1] - nums[2], Math.Min(nums[n - 2] - nums[1], nums[n - 3] - nums[0]));
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
var minimizeSum = function(nums) {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    return Math.min(nums[n - 1] - nums[2], nums[n - 2] - nums[1], nums[n - 3] - nums[0]);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimizeSum(nums: number[]): number {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    return Math.min(nums[n - 1] - nums[2], nums[n - 2] - nums[1], nums[n - 3] - nums[0]);
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
    function minimizeSum($nums) {
        sort($nums);
        $n = count($nums);
        return min($nums[$n - 1] - $nums[2], $nums[$n - 2] - $nums[1], $nums[$n - 3] - $nums[0]);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minimizeSum(_ nums: [Int]) -> Int {
        let sortedNums = nums.sorted()
        let n = sortedNums.count
        return min(sortedNums[n - 1] - sortedNums[2], sortedNums[n - 2] - sortedNums[1], sortedNums[n - 3] - sortedNums[0])
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minimizeSum(nums: IntArray): Int {
        nums.sort()
        val n = nums.size
        return minOf(nums[n - 1] - nums[2], nums[n - 2] - nums[1], nums[n - 3] - nums[0])
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:math';

class Solution {
  int minimizeSum(List<int> nums) {
    nums.sort();
    int n = nums.length;
    int option1 = nums[n - 1] - nums[2];
    int option2 = nums[n - 2] - nums[1];
    int option3 = nums[n - 3] - nums[0];
    return min(option1, min(option2, option3));
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "sort"

func minimizeSum(nums []int) int {
    sort.Ints(nums)
    n := len(nums)
    a := nums[n-1] - nums[2]
    b := nums[n-2] - nums[1]
    c := nums[n-3] - nums[0]

    res := a
    if b < res {
        res = b
    }
    if c < res {
        res = c
    }
    return res
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def minimize_sum(nums)
    nums.sort!
    n = nums.length
    [nums[n - 1] - nums[2], nums[n - 2] - nums[1], nums[n - 3] - nums[0]].min
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import java.util.Arrays

object Solution {
    def minimizeSum(nums: Array[Int]): Int = {
        Arrays.sort(nums)
        val n = nums.length
        val a = nums(n - 1) - nums(2)
        val b = nums(n - 2) - nums(1)
        val c = nums(n - 3) - nums(0)
        math.min(a, math.min(b, c))
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn minimize_sum(nums: Vec<i32>) -> i32 {
        let mut nums = nums;
        nums.sort();
        let n = nums.len();
        let opt1 = nums[n - 1] - nums[2];
        let opt2 = nums[n - 2] - nums[1];
        let opt3 = nums[n - 3] - nums[0];
        std::cmp::min(opt1, std::cmp::min(opt2, opt3))
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (minimize-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([sorted (sort nums <)]
         [v (list->vector sorted)]
         [n (vector-length v)])
    (min (- (vector-ref v (- n 1)) (vector-ref v 2))
         (- (vector-ref v (- n 2)) (vector-ref v 1))
         (- (vector-ref v (- n 3)) (vector-ref v 0)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec minimize_sum(Nums :: [integer()]) -> integer().
minimize_sum(Nums) ->
  Sorted = lists:sort(Nums),
  N = length(Sorted),
  Arr = list_to_tuple(Sorted),
  Opt1 = element(N, Arr) - element(3, Arr),
  Opt2 = element(N - 1, Arr) - element(2, Arr),
  Opt3 = element(N - 2, Arr) - element(1, Arr),
  lists:min([Opt1, Opt2, Opt3]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimize_sum(nums :: [integer]) :: integer
  def minimize_sum(nums) do
    sorted = Enum.sort(nums)
    n = length(sorted)
    arr = List.to_tuple(sorted)

    opt1 = elem(arr, n - 1) - elem(arr, 2)
    opt2 = elem(arr, n - 2) - elem(arr, 1)
    opt3 = elem(arr, n - 3) - elem(arr, 0)

    Enum.min([opt1, opt2, opt3])
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n log n), where n is the number of elements in nums. This time is dominated by sorting the array. Once sorted, finding the answer takes O(1) time.
- **Space Complexity:** O(1) auxiliary space beyond the memory needed by the sorting algorithm, which ranges from O(1) to O(n) depending on the language and standard library implementation.
