---
layout: post
title: "Find Minimum in Rotated Sorted Array"
date: 2026-05-15 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Binary Search"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int findMin(vector<int>& nums) {\n      \
        \  int left = 0;\n        int right = nums.size() - 1;\n\n        while (left\
        \ < right) {\n            int mid = left + (right - left) / 2;\n\n         \
        \   if (nums[mid] > nums[right]) {\n                left = mid + 1;\n      \
        \      } else {\n                right = mid;\n            }\n        }\n\n\
        \        return nums[left];\n    }\n};"
      java: "class Solution {\n    public int findMin(int[] nums) {\n        int left\
        \ = 0;\n        int right = nums.length - 1;\n\n        while (left < right)\
        \ {\n            int mid = left + (right - left) / 2;\n\n            if (nums[mid]\
        \ > nums[right]) {\n                left = mid + 1;\n            } else {\n\
        \                right = mid;\n            }\n        }\n\n        return nums[left];\n\
        \    }\n}"
      python: "class Solution(object):\n    def findMin(self, nums):\n        \"\"\"\
        \n        :type nums: List[int]\n        :rtype: int\n        \"\"\"\n     \
        \   left = 0\n        right = len(nums) - 1\n\n        while left < right:\n\
        \            mid = left + (right - left) // 2\n\n            if nums[mid] >\
        \ nums[right]:\n                left = mid + 1\n            else:\n        \
        \        right = mid\n\n        return nums[left]"
      python3: "class Solution:\n    def findMin(self, nums: List[int]) -> int:\n  \
        \      left = 0\n        right = len(nums) - 1\n\n        while left < right:\n\
        \            mid = left + (right - left) // 2\n\n            if nums[mid] >\
        \ nums[right]:\n                left = mid + 1\n            else:\n        \
        \        right = mid\n\n        return nums[left]"
      c: "int findMin(int* nums, int numsSize) {\n    int left = 0;\n    int right =\
        \ numsSize - 1;\n\n    while (left < right) {\n        int mid = left + (right\
        \ - left) / 2;\n\n        if (nums[mid] > nums[right]) {\n            left =\
        \ mid + 1;\n        } else {\n            right = mid;\n        }\n    }\n\n\
        \    return nums[left];\n}"
      csharp: "public class Solution {\n    public int FindMin(int[] nums) {\n     \
        \   int left = 0;\n        int right = nums.Length - 1;\n        while (left\
        \ < right) {\n            int mid = left + (right - left) / 2;\n           \
        \ if (nums[mid] > nums[right]) {\n                left = mid + 1;\n        \
        \    } else {\n                right = mid;\n            }\n        }\n    \
        \    return nums[left];\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar findMin\
        \ = function(nums) {\n    let left = 0;\n    let right = nums.length - 1;\n\
        \    while (left < right) {\n        let mid = Math.floor(left + (right - left)\
        \ / 2);\n        if (nums[mid] > nums[right]) {\n            left = mid + 1;\n\
        \        } else {\n            right = mid;\n        }\n    }\n    return nums[left];\n\
        };"
      typescript: "function findMin(nums: number[]): number {\n    let left = 0;\n \
        \   let right = nums.length - 1;\n    while (left < right) {\n        let mid\
        \ = Math.floor(left + (right - left) / 2);\n        if (nums[mid] > nums[right])\
        \ {\n            left = mid + 1;\n        } else {\n            right = mid;\n\
        \        }\n    }\n    return nums[left];\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function findMin($nums) {\n        $left = 0;\n    \
        \    $right = count($nums) - 1;\n        while ($left < $right) {\n        \
        \    $mid = $left + (int)(($right - $left) / 2);\n            if ($nums[$mid]\
        \ > $nums[$right]) {\n                $left = $mid + 1;\n            } else\
        \ {\n                $right = $mid;\n            }\n        }\n        return\
        \ $nums[$left];\n    }\n}"
      swift: "class Solution {\n    func findMin(_ nums: [Int]) -> Int {\n        var\
        \ left = 0\n        var right = nums.count - 1\n        while left < right {\n\
        \            let mid = left + (right - left) / 2\n            if nums[mid] >\
        \ nums[right] {\n                left = mid + 1\n            } else {\n    \
        \            right = mid\n            }\n        }\n        return nums[left]\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun findMin(nums: IntArray): Int {\n        var\
        \ left = 0\n        var right = nums.size - 1\n        while (left < right)\
        \ {\n            val mid = left + (right - left) / 2\n            if (nums[mid]\
        \ > nums[right]) {\n                left = mid + 1\n            } else {\n \
        \               right = mid\n            }\n        }\n        return nums[left]\n\
        \    }\n}"
      dart: "class Solution {\n  int findMin(List<int> nums) {\n    int left = 0;\n\
        \    int right = nums.length - 1;\n    while (left < right) {\n      int mid\
        \ = left + (right - left) ~/ 2;\n      if (nums[mid] > nums[right]) {\n    \
        \    left = mid + 1;\n      } else {\n        right = mid;\n      }\n    }\n\
        \    return nums[left];\n  }\n}"
      go: "func findMin(nums []int) int {\n    left := 0\n    right := len(nums) - 1\n\
        \    for left < right {\n        mid := left + (right - left) / 2\n        if\
        \ nums[mid] > nums[right] {\n            left = mid + 1\n        } else {\n\
        \            right = mid\n        }\n    }\n    return nums[left]\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef find_min(nums)\n  \
        \  left = 0\n    right = nums.length - 1\n    while left < right\n        mid\
        \ = left + (right - left) / 2\n        if nums[mid] > nums[right]\n        \
        \    left = mid + 1\n        else\n            right = mid\n        end\n  \
        \  end\n    return nums[left]\nend"
      scala: "object Solution {\n    def findMin(nums: Array[Int]): Int = {\n      \
        \  var left = 0\n        var right = nums.length - 1\n        while (left <\
        \ right) {\n            val mid = left + (right - left) / 2\n            if\
        \ (nums(mid) > nums(right)) {\n                left = mid + 1\n            }\
        \ else {\n                right = mid\n            }\n        }\n        nums(left)\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn find_min(nums: Vec<i32>) -> i32 {\n       \
        \ let mut left = 0;\n        let mut right = nums.len() - 1;\n        while\
        \ left < right {\n            let mid = left + (right - left) / 2;\n       \
        \     if nums[mid] > nums[right] {\n                left = mid + 1;\n      \
        \      } else {\n                right = mid;\n            }\n        }\n  \
        \      nums[left]\n    }\n}"
      racket: "(define/contract (find-min nums)\n  (-> (listof exact-integer?) exact-integer?)\n\
        \  (let ([arr (list->vector nums)])\n    (let loop ([left 0]\n             \
        \  [right (- (vector-length arr) 1)])\n      (if (>= left right)\n         \
        \ (vector-ref arr left)\n          (let* ([mid (+ left (quotient (- right left)\
        \ 2))]\n                 [mid-val (vector-ref arr mid)]\n                 [right-val\
        \ (vector-ref arr right)])\n            (if (> mid-val right-val)\n        \
        \        (loop (+ mid 1) right)\n                (loop left mid)))))))"
      erlang: "-spec find_min(Nums :: [integer()]) -> integer().\nfind_min(Nums) ->\n\
        \  Arr = list_to_tuple(Nums),\n  find_min_helper(Arr, 1, tuple_size(Arr)).\n\
        \nfind_min_helper(Arr, Left, Right) ->\n  if\n    Left >= Right ->\n      element(Left,\
        \ Arr);\n    true ->\n      Mid = Left + (Right - Left) div 2,\n      MidVal\
        \ = element(Mid, Arr),\n      RightVal = element(Right, Arr),\n      if\n  \
        \      MidVal > RightVal ->\n          find_min_helper(Arr, Mid + 1, Right);\n\
        \        true ->\n          find_min_helper(Arr, Left, Mid)\n      end\n  end."
      elixir: "defmodule Solution do\n  @spec find_min(nums :: [integer]) :: integer\n\
        \  def find_min(nums) do\n    arr = List.to_tuple(nums)\n    find_min_recursive(arr,\
        \ 0, tuple_size(arr) - 1)\n  end\n\n  defp find_min_recursive(arr, left, right)\
        \ when left >= right do\n    elem(arr, left)\n  end\n\n  defp find_min_recursive(arr,\
        \ left, right) do\n    mid = left + div(right - left, 2)\n    mid_val = elem(arr,\
        \ mid)\n    right_val = elem(arr, right)\n\n    if mid_val > right_val do\n\
        \      find_min_recursive(arr, mid + 1, right)\n    else\n      find_min_recursive(arr,\
        \ left, mid)\n    end\n  end\nend"
    approach: 'The algorithm employs a binary search strategy to locate the minimum
      element in $O(\log n)$ time. Since the array is sorted and then rotated, it consists
      of two sorted sub-sequences where every element in the first part is greater than
      the elements in the second part (assuming rotation happened). The key intuition
      is to compare the middle element with the rightmost element of the current search
      space. If the middle element is greater than the rightmost element, the inflection
      point (the minimum) must exist to the right of the middle index. Otherwise, the
      minimum element is either the middle element itself or lies to its left.


      By initializing two pointers, ''left'' at the start and ''right'' at the end of
      the array, we iteratively narrow down the range. In each step, we compute ''mid''
      and adjust ''left'' to ''mid + 1'' if ''nums[mid] > nums[right]'', or adjust ''right''
      to ''mid'' if ''nums[mid] <= nums[right]''. This process continues until ''left''
      and ''right'' converge at the same index, which identifies the smallest value
      in the array. This approach effectively handles both rotated and non-rotated (fully
      sorted) arrays without special cases.'
    time_complexity: O(log n) because the search space is divided by half in each iteration
      of the binary search loop, where n is the number of elements in the array.
    space_complexity: O(1) because the algorithm only uses a constant amount of extra
      space for the pointers and the midpoint variable, regardless of the input size.
    elapsed_time: 50.1964430809021
    model: gemini-3-flash-preview
    generated_at: '2026-05-15 02:31:05 '
---

## Problem #153: Find Minimum in Rotated Sorted Array

**Difficulty:** Medium

**Topics:** Array, Binary Search

## Problem Description

<p>Suppose an array of length <code>n</code> sorted in ascending order is <strong>rotated</strong> between <code>1</code> and <code>n</code> times. For example, the array <code>nums = [0,1,2,4,5,6,7]</code> might become:</p>

<ul>
	<li><code>[4,5,6,7,0,1,2]</code> if it was rotated <code>4</code> times.</li>
	<li><code>[0,1,2,4,5,6,7]</code> if it was rotated <code>7</code> times.</li>
</ul>

<p>Notice that <strong>rotating</strong> an array <code>[a[0], a[1], a[2], ..., a[n-1]]</code> 1 time results in the array <code>[a[n-1], a[0], a[1], a[2], ..., a[n-2]]</code>.</p>

<p>Given the sorted rotated array <code>nums</code> of <strong>unique</strong> elements, return <em>the minimum element of this array</em>.</p>

<p>You must write an algorithm that runs in&nbsp;<code>O(log n) time</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,4,5,1,2]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The original array was [1,2,3,4,5] rotated 3 times.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,5,6,7,0,1,2]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [11,13,15,17]
<strong>Output:</strong> 11
<strong>Explanation:</strong> The original array was [11,13,15,17] and it was rotated 4 times. 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 5000</code></li>
	<li><code>-5000 &lt;= nums[i] &lt;= 5000</code></li>
	<li>All the integers of <code>nums</code> are <strong>unique</strong>.</li>
	<li><code>nums</code> is sorted and rotated between <code>1</code> and <code>n</code> times.</li>
</ul>


## Hints

1. Array was originally in ascending order. Now that the array is rotated, there would be a point in the array where there is a small deflection from the increasing sequence. eg. The array would be something like [4, 5, 6, 7, 0, 1, 2].

2. You can divide the search space into two and see which direction to go.
Can you think of an algorithm which has O(logN) search complexity?

3. - All the elements to the left of inflection point > first element of the array.
- All the elements to the right of inflection point

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm employs a binary search strategy to locate the minimum element in $O(\log n)$ time. Since the array is sorted and then rotated, it consists of two sorted sub-sequences where every element in the first part is greater than the elements in the second part (assuming rotation happened). The key intuition is to compare the middle element with the rightmost element of the current search space. If the middle element is greater than the rightmost element, the inflection point (the minimum) must exist to the right of the middle index. Otherwise, the minimum element is either the middle element itself or lies to its left.

By initializing two pointers, 'left' at the start and 'right' at the end of the array, we iteratively narrow down the range. In each step, we compute 'mid' and adjust 'left' to 'mid + 1' if 'nums[mid] > nums[right]', or adjust 'right' to 'mid' if 'nums[mid] <= nums[right]'. This process continues until 'left' and 'right' converge at the same index, which identifies the smallest value in the array. This approach effectively handles both rotated and non-rotated (fully sorted) arrays without special cases.

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
    int findMin(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return nums[left];
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return nums[left];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int findMin(int* nums, int numsSize) {
    int left = 0;
    int right = numsSize - 1;

    while (left < right) {
        int mid = left + (right - left) / 2;

        if (nums[mid] > nums[right]) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    return nums[left];
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int FindMin(int[] nums) {
        int left = 0;
        int right = nums.Length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return nums[left];
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
var findMin = function(nums) {
    let left = 0;
    let right = nums.length - 1;
    while (left < right) {
        let mid = Math.floor(left + (right - left) / 2);
        if (nums[mid] > nums[right]) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return nums[left];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function findMin(nums: number[]): number {
    let left = 0;
    let right = nums.length - 1;
    while (left < right) {
        let mid = Math.floor(left + (right - left) / 2);
        if (nums[mid] > nums[right]) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return nums[left];
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
    function findMin($nums) {
        $left = 0;
        $right = count($nums) - 1;
        while ($left < $right) {
            $mid = $left + (int)(($right - $left) / 2);
            if ($nums[$mid] > $nums[$right]) {
                $left = $mid + 1;
            } else {
                $right = $mid;
            }
        }
        return $nums[$left];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func findMin(_ nums: [Int]) -> Int {
        var left = 0
        var right = nums.count - 1
        while left < right {
            let mid = left + (right - left) / 2
            if nums[mid] > nums[right] {
                left = mid + 1
            } else {
                right = mid
            }
        }
        return nums[left]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun findMin(nums: IntArray): Int {
        var left = 0
        var right = nums.size - 1
        while (left < right) {
            val mid = left + (right - left) / 2
            if (nums[mid] > nums[right]) {
                left = mid + 1
            } else {
                right = mid
            }
        }
        return nums[left]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int findMin(List<int> nums) {
    int left = 0;
    int right = nums.length - 1;
    while (left < right) {
      int mid = left + (right - left) ~/ 2;
      if (nums[mid] > nums[right]) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }
    return nums[left];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func findMin(nums []int) int {
    left := 0
    right := len(nums) - 1
    for left < right {
        mid := left + (right - left) / 2
        if nums[mid] > nums[right] {
            left = mid + 1
        } else {
            right = mid
        }
    }
    return nums[left]
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def find_min(nums)
    left = 0
    right = nums.length - 1
    while left < right
        mid = left + (right - left) / 2
        if nums[mid] > nums[right]
            left = mid + 1
        else
            right = mid
        end
    end
    return nums[left]
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def findMin(nums: Array[Int]): Int = {
        var left = 0
        var right = nums.length - 1
        while (left < right) {
            val mid = left + (right - left) / 2
            if (nums(mid) > nums(right)) {
                left = mid + 1
            } else {
                right = mid
            }
        }
        nums(left)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn find_min(nums: Vec<i32>) -> i32 {
        let mut left = 0;
        let mut right = nums.len() - 1;
        while left < right {
            let mid = left + (right - left) / 2;
            if nums[mid] > nums[right] {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        nums[left]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (find-min nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ([arr (list->vector nums)])
    (let loop ([left 0]
               [right (- (vector-length arr) 1)])
      (if (>= left right)
          (vector-ref arr left)
          (let* ([mid (+ left (quotient (- right left) 2))]
                 [mid-val (vector-ref arr mid)]
                 [right-val (vector-ref arr right)])
            (if (> mid-val right-val)
                (loop (+ mid 1) right)
                (loop left mid)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec find_min(Nums :: [integer()]) -> integer().
find_min(Nums) ->
  Arr = list_to_tuple(Nums),
  find_min_helper(Arr, 1, tuple_size(Arr)).

find_min_helper(Arr, Left, Right) ->
  if
    Left >= Right ->
      element(Left, Arr);
    true ->
      Mid = Left + (Right - Left) div 2,
      MidVal = element(Mid, Arr),
      RightVal = element(Right, Arr),
      if
        MidVal > RightVal ->
          find_min_helper(Arr, Mid + 1, Right);
        true ->
          find_min_helper(Arr, Left, Mid)
      end
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec find_min(nums :: [integer]) :: integer
  def find_min(nums) do
    arr = List.to_tuple(nums)
    find_min_recursive(arr, 0, tuple_size(arr) - 1)
  end

  defp find_min_recursive(arr, left, right) when left >= right do
    elem(arr, left)
  end

  defp find_min_recursive(arr, left, right) do
    mid = left + div(right - left, 2)
    mid_val = elem(arr, mid)
    right_val = elem(arr, right)

    if mid_val > right_val do
      find_min_recursive(arr, mid + 1, right)
    else
      find_min_recursive(arr, left, mid)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(log n) because the search space is divided by half in each iteration of the binary search loop, where n is the number of elements in the array.
- **Space Complexity:** O(1) because the algorithm only uses a constant amount of extra space for the pointers and the midpoint variable, regardless of the input size.
