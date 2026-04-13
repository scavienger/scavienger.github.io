---
layout: post
title: "Minimum Distance to the Target Element"
date: 2026-04-13 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/minimum-distance-to-the-target-element/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int getMinDistance(vector<int>& nums, int\
        \ target, int start) {\n        int min_dist = 10001;\n        for (int i =\
        \ 0; i < nums.size(); ++i) {\n            if (nums[i] == target) {\n       \
        \         int current_dist = abs(i - start);\n                if (current_dist\
        \ < min_dist) {\n                    min_dist = current_dist;\n            \
        \    }\n            }\n        }\n        return min_dist;\n    }\n};"
      java: "class Solution {\n    public int getMinDistance(int[] nums, int target,\
        \ int start) {\n        int minDist = Integer.MAX_VALUE;\n        for (int i\
        \ = 0; i < nums.length; i++) {\n            if (nums[i] == target) {\n     \
        \           int currentDist = Math.abs(i - start);\n                if (currentDist\
        \ < minDist) {\n                    minDist = currentDist;\n               \
        \ }\n            }\n        }\n        return minDist;\n    }\n}"
      python: "class Solution(object):\n    def getMinDistance(self, nums, target, start):\n\
        \        \"\"\"\n        :type nums: List[int]\n        :type target: int\n\
        \        :type start: int\n        :rtype: int\n        \"\"\"\n        min_dist\
        \ = float('inf')\n        for i in range(len(nums)):\n            if nums[i]\
        \ == target:\n                dist = abs(i - start)\n                if dist\
        \ < min_dist:\n                    min_dist = dist\n        return int(min_dist)"
      python3: "class Solution:\n    def getMinDistance(self, nums: List[int], target:\
        \ int, start: int) -> int:\n        min_dist = float('inf')\n        for i,\
        \ num in enumerate(nums):\n            if num == target:\n                dist\
        \ = abs(i - start)\n                if dist < min_dist:\n                  \
        \  min_dist = dist\n        return int(min_dist)"
      c: "int getMinDistance(int* nums, int numsSize, int target, int start) {\n   \
        \ int min_dist = 10001;\n    for (int i = 0; i < numsSize; i++) {\n        if\
        \ (nums[i] == target) {\n            int current_dist = i - start;\n       \
        \     if (current_dist < 0) current_dist = -current_dist;\n            if (current_dist\
        \ < min_dist) {\n                min_dist = current_dist;\n            }\n \
        \       }\n    }\n    return min_dist;\n}"
      csharp: "using System;\n\npublic class Solution {\n    public int GetMinDistance(int[]\
        \ nums, int target, int start) {\n        int minDist = int.MaxValue;\n    \
        \    for (int i = 0; i < nums.Length; i++) {\n            if (nums[i] == target)\
        \ {\n                int currentDist = Math.Abs(i - start);\n              \
        \  if (currentDist < minDist) {\n                    minDist = currentDist;\n\
        \                }\n            }\n        }\n        return minDist;\n    }\n\
        }"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} target\n * @param\
        \ {number} start\n * @return {number}\n */\nvar getMinDistance = function(nums,\
        \ target, start) {\n    let minDist = Infinity;\n    for (let i = 0; i < nums.length;\
        \ i++) {\n        if (nums[i] === target) {\n            let currentDist = Math.abs(i\
        \ - start);\n            if (currentDist < minDist) {\n                minDist\
        \ = currentDist;\n            }\n        }\n    }\n    return minDist;\n};"
      typescript: "function getMinDistance(nums: number[], target: number, start: number):\
        \ number {\n    let minDist = nums.length;\n    for (let i = 0; i < nums.length;\
        \ i++) {\n        if (nums[i] === target) {\n            const dist = Math.abs(i\
        \ - start);\n            if (dist < minDist) {\n                minDist = dist;\n\
        \            }\n        }\n    }\n    return minDist;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer $target\n     * @param Integer $start\n     * @return Integer\n  \
        \   */\n    function getMinDistance($nums, $target, $start) {\n        $minDist\
        \ = count($nums);\n        for ($i = 0; $i < count($nums); $i++) {\n       \
        \     if ($nums[$i] == $target) {\n                $dist = abs($i - $start);\n\
        \                if ($dist < $minDist) {\n                    $minDist = $dist;\n\
        \                }\n            }\n        }\n        return $minDist;\n   \
        \ }\n}"
      swift: "class Solution {\n    func getMinDistance(_ nums: [Int], _ target: Int,\
        \ _ start: Int) -> Int {\n        var minDist = nums.count\n        for i in\
        \ 0..<nums.count {\n            if nums[i] == target {\n                let\
        \ dist = abs(i - start)\n                if dist < minDist {\n             \
        \       minDist = dist\n                }\n            }\n        }\n      \
        \  return minDist\n    }\n}"
      kotlin: "class Solution {\n    fun getMinDistance(nums: IntArray, target: Int,\
        \ start: Int): Int {\n        var minDist = nums.size\n        for (i in nums.indices)\
        \ {\n            if (nums[i] == target) {\n                val dist = if (i\
        \ >= start) i - start else start - i\n                if (dist < minDist) {\n\
        \                    minDist = dist\n                }\n            }\n    \
        \    }\n        return minDist\n    }\n}"
      dart: "class Solution {\n  int getMinDistance(List<int> nums, int target, int\
        \ start) {\n    int minDist = nums.length;\n    for (int i = 0; i < nums.length;\
        \ i++) {\n      if (nums[i] == target) {\n        int dist = (i - start).abs();\n\
        \        if (dist < minDist) {\n          minDist = dist;\n        }\n     \
        \ }\n    }\n    return minDist;\n  }\n}"
      go: "func getMinDistance(nums []int, target int, start int) int {\n    minDist\
        \ := len(nums)\n    for i, num := range nums {\n        if num == target {\n\
        \            dist := i - start\n            if dist < 0 {\n                dist\
        \ = -dist\n            }\n            if dist < minDist {\n                minDist\
        \ = dist\n            }\n        }\n    }\n    return minDist\n}"
      ruby: "def get_min_distance(nums, target, start)\n  min_dist = nums.length\n \
        \ nums.each_with_index do |num, i|\n    if num == target\n      dist = (i -\
        \ start).abs\n      min_dist = dist if dist < min_dist\n    end\n  end\n  min_dist\n\
        end"
      scala: "object Solution {\n    def getMinDistance(nums: Array[Int], target: Int,\
        \ start: Int): Int = {\n        var min_dist = Int.MaxValue\n        for (i\
        \ <- 0 until nums.length) {\n            if (nums(i) == target) {\n        \
        \        val dist = Math.abs(i - start)\n                if (dist < min_dist)\
        \ {\n                    min_dist = dist\n                }\n            }\n\
        \        }\n        min_dist\n    }\n}"
      rust: "impl Solution {\n    pub fn get_min_distance(nums: Vec<i32>, target: i32,\
        \ start: i32) -> i32 {\n        let mut min_dist = i32::MAX;\n        for (i,\
        \ &num) in nums.iter().enumerate() {\n            if num == target {\n     \
        \           let dist = (i as i32 - start).abs();\n                if dist <\
        \ min_dist {\n                    min_dist = dist;\n                }\n    \
        \        }\n        }\n        min_dist\n    }\n}"
      racket: "(define/contract (get-min-distance nums target start)\n  (-> (listof\
        \ exact-integer?) exact-integer? exact-integer? exact-integer?)\n  (let loop\
        \ ([lst nums] [idx 0] [min-dist 1000000])\n    (if (null? lst)\n        min-dist\n\
        \        (let* ([num (car lst)]\n               [dist (abs (- idx start))]\n\
        \               [new-min-dist (if (= num target) (min min-dist dist) min-dist)])\n\
        \          (loop (cdr lst) (+ idx 1) new-min-dist))))\n)"
      erlang: "-spec get_min_distance(Nums :: [integer()], Target :: integer(), Start\
        \ :: integer()) -> integer().\nget_min_distance(Nums, Target, Start) ->\n  find_min_dist(Nums,\
        \ Target, Start, 0, 1000000).\n\nfind_min_dist([], _Target, _Start, _Idx, MinDist)\
        \ ->\n  MinDist;\nfind_min_dist([H | T], Target, Start, Idx, MinDist) ->\n \
        \ if\n    H == Target ->\n      Dist = abs(Idx - Start),\n      NewMinDist =\
        \ if Dist < MinDist -> Dist; true -> MinDist end,\n      find_min_dist(T, Target,\
        \ Start, Idx + 1, NewMinDist);\n    true ->\n      find_min_dist(T, Target,\
        \ Start, Idx + 1, MinDist)\n  end."
      elixir: "defmodule Solution do\n  @spec get_min_distance(nums :: [integer], target\
        \ :: integer, start :: integer) :: integer\n  def get_min_distance(nums, target,\
        \ start) do\n    nums\n    |> Enum.with_index()\n    |> Enum.filter(fn {num,\
        \ _i} -> num == target end)\n    |> Enum.map(fn {_num, i} -> abs(i - start)\
        \ end)\n    |> Enum.min()\n  end\nend"
    approach: 'The algorithm iterates through the input array to identify every index
      i where nums[i] is equal to the specified target. For each matching index, we
      calculate the absolute difference between i and the given start index using the
      formula abs(i - start).


      Since the problem asks for the minimum distance and guarantees that the target
      exists in the array, we initialize a variable with a large value and update it
      whenever a smaller absolute difference is found. This single-pass approach ensures
      we check all possible indices and identify the global minimum distance.'
    time_complexity: O(N) with one-paragraph explanation. The algorithm iterates through
      the entire array of N elements exactly once. At each step, it performs constant-time
      operations such as comparisons and absolute value calculations, resulting in linear
      time complexity relative to the size of the input array.
    space_complexity: O(1) with one-paragraph explanation. The solution uses only a
      fixed amount of extra space for variables like the loop counter and the current
      minimum distance, regardless of the size of the input array.
    elapsed_time: 83.65670084953308
    model: gemini-3-flash-preview
    generated_at: '2026-04-13 02:00:35 '
---

## Problem #1848: Minimum Distance to the Target Element

**Difficulty:** Easy

**Topics:** Array

## Problem Description

<p>Given an integer array <code>nums</code> <strong>(0-indexed)</strong> and two integers <code>target</code> and <code>start</code>, find an index <code>i</code> such that <code>nums[i] == target</code> and <code>abs(i - start)</code> is <strong>minimized</strong>. Note that&nbsp;<code>abs(x)</code>&nbsp;is the absolute value of <code>x</code>.</p>

<p>Return <code>abs(i - start)</code>.</p>

<p>It is <strong>guaranteed</strong> that <code>target</code> exists in <code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5], target = 5, start = 3
<strong>Output:</strong> 1
<strong>Explanation:</strong> nums[4] = 5 is the only value equal to target, so the answer is abs(4 - 3) = 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1], target = 1, start = 0
<strong>Output:</strong> 0
<strong>Explanation:</strong> nums[0] = 1 is the only value equal to target, so the answer is abs(0 - 0) = 0.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1,1,1,1,1,1,1,1], target = 1, start = 0
<strong>Output:</strong> 0
<strong>Explanation:</strong> Every value of nums is 1, but nums[0] minimizes abs(i - start), which is abs(0 - 0) = 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= start &lt; nums.length</code></li>
	<li><code>target</code> is in <code>nums</code>.</li>
</ul>


## Hints

1. Loop in both directions until you find the target element.

2. For each index i such that nums[i] == target calculate abs(i - start).

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm iterates through the input array to identify every index i where nums[i] is equal to the specified target. For each matching index, we calculate the absolute difference between i and the given start index using the formula abs(i - start).

Since the problem asks for the minimum distance and guarantees that the target exists in the array, we initialize a variable with a large value and update it whenever a smaller absolute difference is found. This single-pass approach ensures we check all possible indices and identify the global minimum distance.

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
    int getMinDistance(vector<int>& nums, int target, int start) {
        int min_dist = 10001;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == target) {
                int current_dist = abs(i - start);
                if (current_dist < min_dist) {
                    min_dist = current_dist;
                }
            }
        }
        return min_dist;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int getMinDistance(int[] nums, int target, int start) {
        int minDist = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                int currentDist = Math.abs(i - start);
                if (currentDist < minDist) {
                    minDist = currentDist;
                }
            }
        }
        return minDist;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        min_dist = float('inf')
        for i in range(len(nums)):
            if nums[i] == target:
                dist = abs(i - start)
                if dist < min_dist:
                    min_dist = dist
        return int(min_dist)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_dist = float('inf')
        for i, num in enumerate(nums):
            if num == target:
                dist = abs(i - start)
                if dist < min_dist:
                    min_dist = dist
        return int(min_dist)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int getMinDistance(int* nums, int numsSize, int target, int start) {
    int min_dist = 10001;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == target) {
            int current_dist = i - start;
            if (current_dist < 0) current_dist = -current_dist;
            if (current_dist < min_dist) {
                min_dist = current_dist;
            }
        }
    }
    return min_dist;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public int GetMinDistance(int[] nums, int target, int start) {
        int minDist = int.MaxValue;
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == target) {
                int currentDist = Math.Abs(i - start);
                if (currentDist < minDist) {
                    minDist = currentDist;
                }
            }
        }
        return minDist;
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
 * @param {number} target
 * @param {number} start
 * @return {number}
 */
var getMinDistance = function(nums, target, start) {
    let minDist = Infinity;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === target) {
            let currentDist = Math.abs(i - start);
            if (currentDist < minDist) {
                minDist = currentDist;
            }
        }
    }
    return minDist;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function getMinDistance(nums: number[], target: number, start: number): number {
    let minDist = nums.length;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === target) {
            const dist = Math.abs(i - start);
            if (dist < minDist) {
                minDist = dist;
            }
        }
    }
    return minDist;
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
     * @param Integer $target
     * @param Integer $start
     * @return Integer
     */
    function getMinDistance($nums, $target, $start) {
        $minDist = count($nums);
        for ($i = 0; $i < count($nums); $i++) {
            if ($nums[$i] == $target) {
                $dist = abs($i - $start);
                if ($dist < $minDist) {
                    $minDist = $dist;
                }
            }
        }
        return $minDist;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func getMinDistance(_ nums: [Int], _ target: Int, _ start: Int) -> Int {
        var minDist = nums.count
        for i in 0..<nums.count {
            if nums[i] == target {
                let dist = abs(i - start)
                if dist < minDist {
                    minDist = dist
                }
            }
        }
        return minDist
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun getMinDistance(nums: IntArray, target: Int, start: Int): Int {
        var minDist = nums.size
        for (i in nums.indices) {
            if (nums[i] == target) {
                val dist = if (i >= start) i - start else start - i
                if (dist < minDist) {
                    minDist = dist
                }
            }
        }
        return minDist
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int getMinDistance(List<int> nums, int target, int start) {
    int minDist = nums.length;
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] == target) {
        int dist = (i - start).abs();
        if (dist < minDist) {
          minDist = dist;
        }
      }
    }
    return minDist;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func getMinDistance(nums []int, target int, start int) int {
    minDist := len(nums)
    for i, num := range nums {
        if num == target {
            dist := i - start
            if dist < 0 {
                dist = -dist
            }
            if dist < minDist {
                minDist = dist
            }
        }
    }
    return minDist
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def get_min_distance(nums, target, start)
  min_dist = nums.length
  nums.each_with_index do |num, i|
    if num == target
      dist = (i - start).abs
      min_dist = dist if dist < min_dist
    end
  end
  min_dist
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def getMinDistance(nums: Array[Int], target: Int, start: Int): Int = {
        var min_dist = Int.MaxValue
        for (i <- 0 until nums.length) {
            if (nums(i) == target) {
                val dist = Math.abs(i - start)
                if (dist < min_dist) {
                    min_dist = dist
                }
            }
        }
        min_dist
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn get_min_distance(nums: Vec<i32>, target: i32, start: i32) -> i32 {
        let mut min_dist = i32::MAX;
        for (i, &num) in nums.iter().enumerate() {
            if num == target {
                let dist = (i as i32 - start).abs();
                if dist < min_dist {
                    min_dist = dist;
                }
            }
        }
        min_dist
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (get-min-distance nums target start)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let loop ([lst nums] [idx 0] [min-dist 1000000])
    (if (null? lst)
        min-dist
        (let* ([num (car lst)]
               [dist (abs (- idx start))]
               [new-min-dist (if (= num target) (min min-dist dist) min-dist)])
          (loop (cdr lst) (+ idx 1) new-min-dist))))
)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec get_min_distance(Nums :: [integer()], Target :: integer(), Start :: integer()) -> integer().
get_min_distance(Nums, Target, Start) ->
  find_min_dist(Nums, Target, Start, 0, 1000000).

find_min_dist([], _Target, _Start, _Idx, MinDist) ->
  MinDist;
find_min_dist([H | T], Target, Start, Idx, MinDist) ->
  if
    H == Target ->
      Dist = abs(Idx - Start),
      NewMinDist = if Dist < MinDist -> Dist; true -> MinDist end,
      find_min_dist(T, Target, Start, Idx + 1, NewMinDist);
    true ->
      find_min_dist(T, Target, Start, Idx + 1, MinDist)
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec get_min_distance(nums :: [integer], target :: integer, start :: integer) :: integer
  def get_min_distance(nums, target, start) do
    nums
    |> Enum.with_index()
    |> Enum.filter(fn {num, _i} -> num == target end)
    |> Enum.map(fn {_num, i} -> abs(i - start) end)
    |> Enum.min()
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) with one-paragraph explanation. The algorithm iterates through the entire array of N elements exactly once. At each step, it performs constant-time operations such as comparisons and absolute value calculations, resulting in linear time complexity relative to the size of the input array.
- **Space Complexity:** O(1) with one-paragraph explanation. The solution uses only a fixed amount of extra space for variables like the loop counter and the current minimum distance, regardless of the size of the input array.
