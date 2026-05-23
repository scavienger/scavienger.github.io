---
layout: post
title: "Check if Array Is Sorted and Rotated"
date: 2026-05-23 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool check(vector<int>& nums) {\n       \
        \ int count = 0;\n        int n = nums.size();\n        for (int i = 0; i <\
        \ n; i++) {\n            if (nums[i] > nums[(i + 1) % n]) {\n              \
        \  count++;\n            }\n        }\n        return count <= 1;\n    }\n};"
      java: "class Solution {\n    public boolean check(int[] nums) {\n        int count\
        \ = 0;\n        int n = nums.length;\n        for (int i = 0; i < n; i++) {\n\
        \            if (nums[i] > nums[(i + 1) % n]) {\n                count++;\n\
        \            }\n        }\n        return count <= 1;\n    }\n}"
      python: "class Solution(object):\n    def check(self, nums):\n        \"\"\"\n\
        \        :type nums: List[int]\n        :rtype: bool\n        \"\"\"\n     \
        \   count = 0\n        n = len(nums)\n        for i in range(n):\n         \
        \   if nums[i] > nums[(i + 1) % n]:\n                count += 1\n        return\
        \ count <= 1"
      python3: "class Solution:\n    def check(self, nums: List[int]) -> bool:\n   \
        \     count = 0\n        n = len(nums)\n        for i in range(n):\n       \
        \     if nums[i] > nums[(i + 1) % n]:\n                count += 1\n        return\
        \ count <= 1"
      c: "bool check(int* nums, int numsSize) {\n    int count = 0;\n    for (int i\
        \ = 0; i < numsSize; i++) {\n        if (nums[i] > nums[(i + 1) % numsSize])\
        \ {\n            count++;\n        }\n    }\n    return count <= 1;\n}"
      csharp: "public class Solution {\n    public bool Check(int[] nums) {\n      \
        \  int count = 0;\n        int n = nums.Length;\n        for (int i = 0; i <\
        \ n; i++) {\n            if (nums[i] > nums[(i + 1) % n]) {\n              \
        \  count++;\n            }\n        }\n        return count <= 1;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {boolean}\n */\nvar check\
        \ = function(nums) {\n    let count = 0;\n    const n = nums.length;\n    for\
        \ (let i = 0; i < n; i++) {\n        if (nums[i] > nums[(i + 1) % n]) {\n  \
        \          count++;\n        }\n    }\n    return count <= 1;\n};"
      typescript: "function check(nums: number[]): boolean {\n    let count = 0;\n \
        \   const n = nums.length;\n    for (let i = 0; i < n; i++) {\n        if (nums[i]\
        \ > nums[(i + 1) % n]) {\n            count++;\n        }\n    }\n    return\
        \ count <= 1;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Boolean\n     */\n    function check($nums) {\n        $count = 0;\n     \
        \   $n = count($nums);\n        for ($i = 0; $i < $n; $i++) {\n            if\
        \ ($nums[$i] > $nums[($i + 1) % $n]) {\n                $count++;\n        \
        \    }\n        }\n        return $count <= 1;\n    }\n}"
      swift: "class Solution {\n    func check(_ nums: [Int]) -> Bool {\n        var\
        \ count = 0\n        let n = nums.count\n        for i in 0..<n {\n        \
        \    if nums[i] > nums[(i + 1) % n] {\n                count += 1\n        \
        \    }\n        }\n        return count <= 1\n    }\n}"
      kotlin: "class Solution {\n    fun check(nums: IntArray): Boolean {\n        var\
        \ count = 0\n        val n = nums.size\n        for (i in 0 until n) {\n   \
        \         if (nums[i] > nums[(i + 1) % n]) {\n                count++\n    \
        \        }\n        }\n        return count <= 1\n    }\n}"
      dart: "class Solution {\n  bool check(List<int> nums) {\n    int count = 0;\n\
        \    int n = nums.length;\n    for (int i = 0; i < n; i++) {\n      if (nums[i]\
        \ > nums[(i + 1) % n]) {\n        count++;\n      }\n    }\n    return count\
        \ <= 1;\n  }\n}"
      go: "func check(nums []int) bool {\n    count := 0\n    n := len(nums)\n    for\
        \ i := 0; i < n; i++ {\n        if nums[i] > nums[(i + 1) % n] {\n         \
        \   count++\n        }\n    }\n    return count <= 1\n}"
      ruby: "def check(nums)\n  count = 0\n  n = nums.length\n  n.times do |i|\n   \
        \ if nums[i] > nums[(i + 1) % n]\n      count += 1\n    end\n  end\n  count\
        \ <= 1\nend"
      scala: "object Solution {\n  def check(nums: Array[Int]): Boolean = {\n    var\
        \ count = 0\n    val n = nums.length\n    for (i <- 0 until n) {\n      if (nums(i)\
        \ > nums((i + 1) % n)) {\n        count += 1\n      }\n    }\n    count <= 1\n\
        \  }\n}"
      rust: "impl Solution {\n    pub fn check(nums: Vec<i32>) -> bool {\n        let\
        \ n = nums.len();\n        let mut count = 0;\n        for i in 0..n {\n   \
        \         if nums[i] > nums[(i + 1) % n] {\n                count += 1;\n  \
        \          }\n        }\n        count <= 1\n    }\n}"
      racket: "(define/contract (check nums)\n  (-> (listof exact-integer?) boolean?)\n\
        \  (let* ([n (length nums)]\n         [vec (list->vector nums)])\n    (let loop\
        \ ([i 0] [count 0])\n      (if (= i n)\n          (<= count 1)\n          (let*\
        \ ([curr (vector-ref vec i)]\n                 [next (vector-ref vec (modulo\
        \ (+ i 1) n))]\n                 [new-count (if (> curr next) (+ count 1) count)])\n\
        \            (loop (+ i 1) new-count))))))"
      erlang: "-spec check(Nums :: [integer()]) -> boolean().\ncheck(Nums) ->\n  T =\
        \ list_to_tuple(Nums),\n  N = tuple_size(T),\n  count_drops(T, N, 1, 0) =< 1.\n\
        \ncount_drops(T, N, I, C) when I < N ->\n  A = element(I, T),\n  B = element(I\
        \ + 1, T),\n  NewC = if A > B -> C + 1; true -> C end,\n  count_drops(T, N,\
        \ I + 1, NewC);\ncount_drops(T, N, N, C) ->\n  A = element(N, T),\n  B = element(1,\
        \ T),\n  if A > B -> C + 1; true -> C end."
      elixir: "defmodule Solution do\n  @spec check(nums :: [integer]) :: boolean\n\
        \  def check(nums) do\n    [head | _] = nums\n    rotated = Enum.drop(nums,\
        \ 1) ++ [head]\n    count = Enum.zip(nums, rotated)\n            |> Enum.count(fn\
        \ {a, b} -> a > b end)\n    count <= 1\n  end\nend"
    approach: "The algorithm works by counting the number of 'descending' points in\
      \ the array while treating the array as circular. In a non-decreasingly sorted\
      \ array, there are zero such points (every element is less than or equal to the\
      \ next). When such an array is rotated, at most one descending point is created\
      \ at the pivot where the largest element is followed by the smallest element.\
      \ \n\nWe iterate through the array once, comparing each element nums[i] with its\
      \ circular successor nums[(i + 1) % n]. If nums[i] is greater than its successor,\
      \ we increment a violation counter. If the total number of violations is less\
      \ than or equal to one, the array satisfies the condition of being a rotated sorted\
      \ array. If the count exceeds one, it means the array has multiple descending\
      \ segments that cannot be resolved by a single rotation."
    time_complexity: O(n) with one-paragraph explanation, where n is the number of elements
      in the input array. We perform a single linear pass through the array to check
      the adjacent pairs.
    space_complexity: O(1) with one-paragraph explanation, as we only use a single integer
      variable to store the count of descending points, regardless of the input size.
    elapsed_time: 62.58964014053345
    model: gemini-3-flash-preview
    generated_at: '2026-05-23 02:26:26 '
---

## Problem #1752: Check if Array Is Sorted and Rotated

**Difficulty:** Easy

**Topics:** Array

## Problem Description

<p>Given an array <code>nums</code>, return <code>true</code><em> if the array was originally sorted in non-decreasing order, then rotated <strong>some</strong> number of positions (including zero)</em>. Otherwise, return <code>false</code>.</p>

<p>There may be <strong>duplicates</strong> in the original array.</p>

<p><strong>Note:</strong> An array <code>A</code> rotated by <code>x</code> positions results in an array <code>B</code> of the same length such that <code>B[i] == A[(i+x) % A.length]</code> for every valid index <code>i</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,4,5,1,2]
<strong>Output:</strong> true
<strong>Explanation:</strong> [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 2 positions to begin on the element of value 3: [3,4,5,1,2].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,1,3,4]
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no sorted array once rotated that can make nums.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> true
<strong>Explanation:</strong> [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## Hints

1. Brute force and check if it is possible for a sorted array to start from each position.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm works by counting the number of 'descending' points in the array while treating the array as circular. In a non-decreasingly sorted array, there are zero such points (every element is less than or equal to the next). When such an array is rotated, at most one descending point is created at the pivot where the largest element is followed by the smallest element. 

We iterate through the array once, comparing each element nums[i] with its circular successor nums[(i + 1) % n]. If nums[i] is greater than its successor, we increment a violation counter. If the total number of violations is less than or equal to one, the array satisfies the condition of being a rotated sorted array. If the count exceeds one, it means the array has multiple descending segments that cannot be resolved by a single rotation.

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
    bool check(vector<int>& nums) {
        int count = 0;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            if (nums[i] > nums[(i + 1) % n]) {
                count++;
            }
        }
        return count <= 1;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean check(int[] nums) {
        int count = 0;
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            if (nums[i] > nums[(i + 1) % n]) {
                count++;
            }
        }
        return count <= 1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
        return count <= 1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
        return count <= 1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
bool check(int* nums, int numsSize) {
    int count = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > nums[(i + 1) % numsSize]) {
            count++;
        }
    }
    return count <= 1;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool Check(int[] nums) {
        int count = 0;
        int n = nums.Length;
        for (int i = 0; i < n; i++) {
            if (nums[i] > nums[(i + 1) % n]) {
                count++;
            }
        }
        return count <= 1;
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
 * @return {boolean}
 */
var check = function(nums) {
    let count = 0;
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        if (nums[i] > nums[(i + 1) % n]) {
            count++;
        }
    }
    return count <= 1;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function check(nums: number[]): boolean {
    let count = 0;
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        if (nums[i] > nums[(i + 1) % n]) {
            count++;
        }
    }
    return count <= 1;
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
     * @return Boolean
     */
    function check($nums) {
        $count = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($nums[$i] > $nums[($i + 1) % $n]) {
                $count++;
            }
        }
        return $count <= 1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func check(_ nums: [Int]) -> Bool {
        var count = 0
        let n = nums.count
        for i in 0..<n {
            if nums[i] > nums[(i + 1) % n] {
                count += 1
            }
        }
        return count <= 1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun check(nums: IntArray): Boolean {
        var count = 0
        val n = nums.size
        for (i in 0 until n) {
            if (nums[i] > nums[(i + 1) % n]) {
                count++
            }
        }
        return count <= 1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool check(List<int> nums) {
    int count = 0;
    int n = nums.length;
    for (int i = 0; i < n; i++) {
      if (nums[i] > nums[(i + 1) % n]) {
        count++;
      }
    }
    return count <= 1;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func check(nums []int) bool {
    count := 0
    n := len(nums)
    for i := 0; i < n; i++ {
        if nums[i] > nums[(i + 1) % n] {
            count++
        }
    }
    return count <= 1
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def check(nums)
  count = 0
  n = nums.length
  n.times do |i|
    if nums[i] > nums[(i + 1) % n]
      count += 1
    end
  end
  count <= 1
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def check(nums: Array[Int]): Boolean = {
    var count = 0
    val n = nums.length
    for (i <- 0 until n) {
      if (nums(i) > nums((i + 1) % n)) {
        count += 1
      }
    }
    count <= 1
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn check(nums: Vec<i32>) -> bool {
        let n = nums.len();
        let mut count = 0;
        for i in 0..n {
            if nums[i] > nums[(i + 1) % n] {
                count += 1;
            }
        }
        count <= 1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (check nums)
  (-> (listof exact-integer?) boolean?)
  (let* ([n (length nums)]
         [vec (list->vector nums)])
    (let loop ([i 0] [count 0])
      (if (= i n)
          (<= count 1)
          (let* ([curr (vector-ref vec i)]
                 [next (vector-ref vec (modulo (+ i 1) n))]
                 [new-count (if (> curr next) (+ count 1) count)])
            (loop (+ i 1) new-count))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec check(Nums :: [integer()]) -> boolean().
check(Nums) ->
  T = list_to_tuple(Nums),
  N = tuple_size(T),
  count_drops(T, N, 1, 0) =< 1.

count_drops(T, N, I, C) when I < N ->
  A = element(I, T),
  B = element(I + 1, T),
  NewC = if A > B -> C + 1; true -> C end,
  count_drops(T, N, I + 1, NewC);
count_drops(T, N, N, C) ->
  A = element(N, T),
  B = element(1, T),
  if A > B -> C + 1; true -> C end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec check(nums :: [integer]) :: boolean
  def check(nums) do
    [head | _] = nums
    rotated = Enum.drop(nums, 1) ++ [head]
    count = Enum.zip(nums, rotated)
            |> Enum.count(fn {a, b} -> a > b end)
    count <= 1
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) with one-paragraph explanation, where n is the number of elements in the input array. We perform a single linear pass through the array to check the adjacent pairs.
- **Space Complexity:** O(1) with one-paragraph explanation, as we only use a single integer variable to store the count of descending points, regardless of the input size.
