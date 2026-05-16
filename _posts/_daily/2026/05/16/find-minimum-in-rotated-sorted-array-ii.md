---
layout: post
title: "Find Minimum in Rotated Sorted Array II"
date: 2026-05-16 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Binary Search"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int findMin(vector<int>& nums) {\n      \
        \  int left = 0;\n        int right = nums.size() - 1;\n\n        while (left\
        \ < right) {\n            int mid = left + (right - left) / 2;\n           \
        \ if (nums[mid] > nums[right]) {\n                left = mid + 1;\n        \
        \    } else if (nums[mid] < nums[right]) {\n                right = mid;\n \
        \           } else {\n                right--;\n            }\n        }\n\n\
        \        return nums[left];\n    }\n};"
      java: "class Solution {\n    public int findMin(int[] nums) {\n        int left\
        \ = 0;\n        int right = nums.length - 1;\n\n        while (left < right)\
        \ {\n            int mid = left + (right - left) / 2;\n            if (nums[mid]\
        \ > nums[right]) {\n                left = mid + 1;\n            } else if (nums[mid]\
        \ < nums[right]) {\n                right = mid;\n            } else {\n   \
        \             right--;\n            }\n        }\n\n        return nums[left];\n\
        \    }\n}"
      python: "class Solution(object):\n    def findMin(self, nums):\n        \"\"\"\
        \n        :type nums: List[int]\n        :rtype: int\n        \"\"\"\n     \
        \   left = 0\n        right = len(nums) - 1\n\n        while left < right:\n\
        \            mid = left + (right - left) // 2\n            if nums[mid] > nums[right]:\n\
        \                left = mid + 1\n            elif nums[mid] < nums[right]:\n\
        \                right = mid\n            else:\n                right -= 1\n\
        \n        return nums[left]"
      python3: "class Solution:\n    def findMin(self, nums: List[int]) -> int:\n  \
        \      low, high = 0, len(nums) - 1\n        while low < high:\n           \
        \ mid = low + (high - low) // 2\n            if nums[mid] < nums[high]:\n  \
        \              high = mid\n            elif nums[mid] > nums[high]:\n      \
        \          low = mid + 1\n            else:\n                high -= 1\n   \
        \     return nums[low]"
      c: "int findMin(int* nums, int numsSize) {\n    int low = 0;\n    int high = numsSize\
        \ - 1;\n    while (low < high) {\n        int mid = low + (high - low) / 2;\n\
        \        if (nums[mid] < nums[high]) {\n            high = mid;\n        } else\
        \ if (nums[mid] > nums[high]) {\n            low = mid + 1;\n        } else\
        \ {\n            high--;\n        }\n    }\n    return nums[low];\n}"
      csharp: "public class Solution {\n    public int FindMin(int[] nums) {\n     \
        \   int low = 0;\n        int high = nums.Length - 1;\n        while (low <\
        \ high) {\n            int mid = low + (high - low) / 2;\n            if (nums[mid]\
        \ < nums[high]) {\n                high = mid;\n            } else if (nums[mid]\
        \ > nums[high]) {\n                low = mid + 1;\n            } else {\n  \
        \              high--;\n            }\n        }\n        return nums[low];\n\
        \    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar findMin\
        \ = function(nums) {\n    let low = 0;\n    let high = nums.length - 1;\n  \
        \  while (low < high) {\n        let mid = Math.floor(low + (high - low) / 2);\n\
        \        if (nums[mid] < nums[high]) {\n            high = mid;\n        } else\
        \ if (nums[mid] > nums[high]) {\n            low = mid + 1;\n        } else\
        \ {\n            high--;\n        }\n    }\n    return nums[low];\n};"
      typescript: "function findMin(nums: number[]): number {\n    let left = 0;\n \
        \   let right = nums.length - 1;\n\n    while (left < right) {\n        const\
        \ mid = Math.floor(left + (right - left) / 2);\n\n        if (nums[mid] < nums[right])\
        \ {\n            right = mid;\n        } else if (nums[mid] > nums[right]) {\n\
        \            left = mid + 1;\n        } else {\n            right--;\n     \
        \   }\n    }\n\n    return nums[left];\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function findMin($nums) {\n        $left = 0;\n    \
        \    $right = count($nums) - 1;\n\n        while ($left < $right) {\n      \
        \      $mid = $left + (int)(($right - $left) / 2);\n\n            if ($nums[$mid]\
        \ < $nums[$right]) {\n                $right = $mid;\n            } elseif ($nums[$mid]\
        \ > $nums[$right]) {\n                $left = $mid + 1;\n            } else\
        \ {\n                $right--;\n            }\n        }\n\n        return $nums[$left];\n\
        \    }\n}"
      swift: "class Solution {\n    func findMin(_ nums: [Int]) -> Int {\n        var\
        \ left = 0\n        var right = nums.count - 1\n\n        while left < right\
        \ {\n            let mid = left + (right - left) / 2\n\n            if nums[mid]\
        \ < nums[right] {\n                right = mid\n            } else if nums[mid]\
        \ > nums[right] {\n                left = mid + 1\n            } else {\n  \
        \              right -= 1\n            }\n        }\n\n        return nums[left]\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun findMin(nums: IntArray): Int {\n        var\
        \ left = 0\n        var right = nums.size - 1\n\n        while (left < right)\
        \ {\n            val mid = left + (right - left) / 2\n\n            if (nums[mid]\
        \ < nums[right]) {\n                right = mid\n            } else if (nums[mid]\
        \ > nums[right]) {\n                left = mid + 1\n            } else {\n \
        \               right--\n            }\n        }\n\n        return nums[left]\n\
        \    }\n}"
      dart: "class Solution {\n  int findMin(List<int> nums) {\n    int low = 0;\n \
        \   int high = nums.length - 1;\n    while (low < high) {\n      int mid = low\
        \ + (high - low) ~/ 2;\n      if (nums[mid] < nums[high]) {\n        high =\
        \ mid;\n      } else if (nums[mid] > nums[high]) {\n        low = mid + 1;\n\
        \      } else {\n        high--;\n      }\n    }\n    return nums[low];\n  }\n\
        }"
      go: "func findMin(nums []int) int {\n    low := 0\n    high := len(nums) - 1\n\
        \    for low < high {\n        mid := low + (high-low)/2\n        if nums[mid]\
        \ < nums[high] {\n            high = mid\n        } else if nums[mid] > nums[high]\
        \ {\n            low = mid + 1\n        } else {\n            high--\n     \
        \   }\n    }\n    return nums[low]\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef find_min(nums)\n  low\
        \ = 0\n  high = nums.length - 1\n  while low < high\n    mid = low + (high -\
        \ low) / 2\n    if nums[mid] < nums[high]\n      high = mid\n    elsif nums[mid]\
        \ > nums[high]\n      low = mid + 1\n    else\n      high -= 1\n    end\n  end\n\
        \  nums[low]\nend"
      scala: "object Solution {\n    def findMin(nums: Array[Int]): Int = {\n      \
        \  var low = 0\n        var high = nums.length - 1\n        while (low < high)\
        \ {\n            val mid = low + (high - low) / 2\n            if (nums[mid]\
        \ < nums[high]) {\n                high = mid\n            } else if (nums[mid]\
        \ > nums[high]) {\n                low = mid + 1\n            } else {\n   \
        \             high -= 1\n            }\n        }\n        nums[low]\n    }\n\
        }"
      rust: "impl Solution {\n    pub fn find_min(nums: Vec<i32>) -> i32 {\n       \
        \ let mut low = 0;\n        let mut high = nums.len() - 1;\n\n        while\
        \ low < high {\n            let mid = low + (high - low) / 2;\n            if\
        \ nums[mid] < nums[high] {\n                high = mid;\n            } else\
        \ if nums[mid] > nums[high] {\n                low = mid + 1;\n            }\
        \ else {\n                high -= 1;\n            }\n        }\n\n        nums[low]\n\
        \    }\n}"
      racket: "(define/contract (find-min nums)\n  (-> (listof exact-integer?) exact-integer?)\n\
        \  (let ([vec (list->vector nums)])\n    (let loop ([low 0] [high (- (vector-length\
        \ vec) 1)])\n      (if (>= low high)\n          (vector-ref vec low)\n     \
        \     (let* ([mid (+ low (quotient (- high low) 2))]\n                 [mid-val\
        \ (vector-ref vec mid)]\n                 [high-val (vector-ref vec high)])\n\
        \            (cond\n              [(< mid-val high-val) (loop low mid)]\n  \
        \            [(> mid-val high-val) (loop (+ mid 1) high)]\n              [else\
        \ (loop low (- high 1))]))))))"
      erlang: "-spec find_min(Nums :: [integer()]) -> integer().\nfind_min(Nums) ->\n\
        \    Arr = list_to_tuple(Nums),\n    find_min_recursive(Arr, 1, tuple_size(Arr)).\n\
        \nfind_min_recursive(Arr, Low, High) when Low >= High ->\n    element(Low, Arr);\n\
        find_min_recursive(Arr, Low, High) ->\n    Mid = Low + (High - Low) div 2,\n\
        \    MidVal = element(Mid, Arr),\n    HighVal = element(High, Arr),\n    if\n\
        \        MidVal < HighVal -> find_min_recursive(Arr, Low, Mid);\n        MidVal\
        \ > HighVal -> find_min_recursive(Arr, Mid + 1, High);\n        true -> find_min_recursive(Arr,\
        \ Low, High - 1)\n    end."
      elixir: "defmodule Solution do\n  @spec find_min(nums :: [integer]) :: integer\n\
        \  def find_min(nums) do\n    arr = List.to_tuple(nums)\n    find_min_recursive(arr,\
        \ 0, tuple_size(arr) - 1)\n  end\n\n  defp find_min_recursive(arr, low, high)\
        \ when low >= high do\n    elem(arr, low)\n  end\n\n  defp find_min_recursive(arr,\
        \ low, high) do\n    mid = div(low + high, 2)\n    mid_val = elem(arr, mid)\n\
        \    high_val = elem(arr, high)\n    cond do\n      mid_val < high_val -> find_min_recursive(arr,\
        \ low, mid)\n      mid_val > high_val -> find_min_recursive(arr, mid + 1, high)\n\
        \      true -> find_min_recursive(arr, low, high - 1)\n    end\n  end\nend"
    approach: 'The algorithm utilizes a modified binary search to locate the minimum
      element in a rotated sorted array. We maintain two pointers, left and right, and
      calculate the midpoint. The core intuition relies on comparing the value at the
      midpoint with the value at the right boundary. If the midpoint value is strictly
      greater than the right boundary value, the rotation point (and thus the minimum)
      must lie in the right half of the array. If the midpoint value is strictly less
      than the right boundary value, the minimum must be at or to the left of the midpoint,
      allowing us to safely discard the right half of the array.


      The presence of duplicates introduces a scenario where the midpoint value equals
      the right boundary value. In this specific case, we cannot determine which half
      contains the minimum element because both halves could potentially host the rotation
      point (e.g., [1, 1, 0, 1] vs [1, 0, 1, 1]). To handle this safely, we simply decrement
      the right pointer by one. This reduction is safe because even if the element at
      the right boundary was the minimum, an identical value exists at the midpoint,
      ensuring the minimum remains within the search range. The loop continues until
      the pointers converge, identifying the minimum element.'
    time_complexity: O(n) in the worst case and O(log n) on average. The worst case
      occurs when all elements in the array are identical, forcing the algorithm to
      decrement the right pointer linearly. In most cases where elements are distinct
      or duplicates are few, it behaves like a standard binary search with logarithmic
      complexity.
    space_complexity: O(1) because the algorithm only uses a constant amount of extra
      space for pointers and variables, regardless of the size of the input array.
    elapsed_time: 70.99254035949707
    model: gemini-3-flash-preview
    generated_at: '2026-05-16 02:13:47 '
---

## Problem #154: Find Minimum in Rotated Sorted Array II

**Difficulty:** Hard

**Topics:** Array, Binary Search

## Problem Description

<p>Suppose an array of length <code>n</code> sorted in ascending order is <strong>rotated</strong> between <code>1</code> and <code>n</code> times. For example, the array <code>nums = [0,1,4,4,5,6,7]</code> might become:</p>

<ul>
	<li><code>[4,5,6,7,0,1,4]</code> if it was rotated <code>4</code> times.</li>
	<li><code>[0,1,4,4,5,6,7]</code> if it was rotated <code>7</code> times.</li>
</ul>

<p>Notice that <strong>rotating</strong> an array <code>[a[0], a[1], a[2], ..., a[n-1]]</code> 1 time results in the array <code>[a[n-1], a[0], a[1], a[2], ..., a[n-2]]</code>.</p>

<p>Given the sorted rotated array <code>nums</code> that may contain <strong>duplicates</strong>, return <em>the minimum element of this array</em>.</p>

<p>You must decrease the overall operation steps as much as possible.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,3,5]
<strong>Output:</strong> 1
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [2,2,2,0,1]
<strong>Output:</strong> 0
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 5000</code></li>
	<li><code>-5000 &lt;= nums[i] &lt;= 5000</code></li>
	<li><code>nums</code> is sorted and rotated between <code>1</code> and <code>n</code> times.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> This problem is similar to&nbsp;<a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/" target="_blank">Find Minimum in Rotated Sorted Array</a>, but&nbsp;<code>nums</code> may contain <strong>duplicates</strong>. Would this affect the runtime complexity? How and why?</p>

<p>&nbsp;</p>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm utilizes a modified binary search to locate the minimum element in a rotated sorted array. We maintain two pointers, left and right, and calculate the midpoint. The core intuition relies on comparing the value at the midpoint with the value at the right boundary. If the midpoint value is strictly greater than the right boundary value, the rotation point (and thus the minimum) must lie in the right half of the array. If the midpoint value is strictly less than the right boundary value, the minimum must be at or to the left of the midpoint, allowing us to safely discard the right half of the array.

The presence of duplicates introduces a scenario where the midpoint value equals the right boundary value. In this specific case, we cannot determine which half contains the minimum element because both halves could potentially host the rotation point (e.g., [1, 1, 0, 1] vs [1, 0, 1, 1]). To handle this safely, we simply decrement the right pointer by one. This reduction is safe because even if the element at the right boundary was the minimum, an identical value exists at the midpoint, ensuring the minimum remains within the search range. The loop continues until the pointers converge, identifying the minimum element.

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
            } else if (nums[mid] < nums[right]) {
                right = mid;
            } else {
                right--;
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
            } else if (nums[mid] < nums[right]) {
                right = mid;
            } else {
                right--;
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
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1

        return nums[left]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] < nums[high]:
                high = mid
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                high -= 1
        return nums[low]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int findMin(int* nums, int numsSize) {
    int low = 0;
    int high = numsSize - 1;
    while (low < high) {
        int mid = low + (high - low) / 2;
        if (nums[mid] < nums[high]) {
            high = mid;
        } else if (nums[mid] > nums[high]) {
            low = mid + 1;
        } else {
            high--;
        }
    }
    return nums[low];
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int FindMin(int[] nums) {
        int low = 0;
        int high = nums.Length - 1;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (nums[mid] < nums[high]) {
                high = mid;
            } else if (nums[mid] > nums[high]) {
                low = mid + 1;
            } else {
                high--;
            }
        }
        return nums[low];
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
    let low = 0;
    let high = nums.length - 1;
    while (low < high) {
        let mid = Math.floor(low + (high - low) / 2);
        if (nums[mid] < nums[high]) {
            high = mid;
        } else if (nums[mid] > nums[high]) {
            low = mid + 1;
        } else {
            high--;
        }
    }
    return nums[low];
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
        const mid = Math.floor(left + (right - left) / 2);

        if (nums[mid] < nums[right]) {
            right = mid;
        } else if (nums[mid] > nums[right]) {
            left = mid + 1;
        } else {
            right--;
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

            if ($nums[$mid] < $nums[$right]) {
                $right = $mid;
            } elseif ($nums[$mid] > $nums[$right]) {
                $left = $mid + 1;
            } else {
                $right--;
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

            if nums[mid] < nums[right] {
                right = mid
            } else if nums[mid] > nums[right] {
                left = mid + 1
            } else {
                right -= 1
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

            if (nums[mid] < nums[right]) {
                right = mid
            } else if (nums[mid] > nums[right]) {
                left = mid + 1
            } else {
                right--
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
    int low = 0;
    int high = nums.length - 1;
    while (low < high) {
      int mid = low + (high - low) ~/ 2;
      if (nums[mid] < nums[high]) {
        high = mid;
      } else if (nums[mid] > nums[high]) {
        low = mid + 1;
      } else {
        high--;
      }
    }
    return nums[low];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func findMin(nums []int) int {
    low := 0
    high := len(nums) - 1
    for low < high {
        mid := low + (high-low)/2
        if nums[mid] < nums[high] {
            high = mid
        } else if nums[mid] > nums[high] {
            low = mid + 1
        } else {
            high--
        }
    }
    return nums[low]
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
  low = 0
  high = nums.length - 1
  while low < high
    mid = low + (high - low) / 2
    if nums[mid] < nums[high]
      high = mid
    elsif nums[mid] > nums[high]
      low = mid + 1
    else
      high -= 1
    end
  end
  nums[low]
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def findMin(nums: Array[Int]): Int = {
        var low = 0
        var high = nums.length - 1
        while (low < high) {
            val mid = low + (high - low) / 2
            if (nums[mid] < nums[high]) {
                high = mid
            } else if (nums[mid] > nums[high]) {
                low = mid + 1
            } else {
                high -= 1
            }
        }
        nums[low]
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
        let mut low = 0;
        let mut high = nums.len() - 1;

        while low < high {
            let mid = low + (high - low) / 2;
            if nums[mid] < nums[high] {
                high = mid;
            } else if nums[mid] > nums[high] {
                low = mid + 1;
            } else {
                high -= 1;
            }
        }

        nums[low]
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
  (let ([vec (list->vector nums)])
    (let loop ([low 0] [high (- (vector-length vec) 1)])
      (if (>= low high)
          (vector-ref vec low)
          (let* ([mid (+ low (quotient (- high low) 2))]
                 [mid-val (vector-ref vec mid)]
                 [high-val (vector-ref vec high)])
            (cond
              [(< mid-val high-val) (loop low mid)]
              [(> mid-val high-val) (loop (+ mid 1) high)]
              [else (loop low (- high 1))]))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec find_min(Nums :: [integer()]) -> integer().
find_min(Nums) ->
    Arr = list_to_tuple(Nums),
    find_min_recursive(Arr, 1, tuple_size(Arr)).

find_min_recursive(Arr, Low, High) when Low >= High ->
    element(Low, Arr);
find_min_recursive(Arr, Low, High) ->
    Mid = Low + (High - Low) div 2,
    MidVal = element(Mid, Arr),
    HighVal = element(High, Arr),
    if
        MidVal < HighVal -> find_min_recursive(Arr, Low, Mid);
        MidVal > HighVal -> find_min_recursive(Arr, Mid + 1, High);
        true -> find_min_recursive(Arr, Low, High - 1)
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

  defp find_min_recursive(arr, low, high) when low >= high do
    elem(arr, low)
  end

  defp find_min_recursive(arr, low, high) do
    mid = div(low + high, 2)
    mid_val = elem(arr, mid)
    high_val = elem(arr, high)
    cond do
      mid_val < high_val -> find_min_recursive(arr, low, mid)
      mid_val > high_val -> find_min_recursive(arr, mid + 1, high)
      true -> find_min_recursive(arr, low, high - 1)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) in the worst case and O(log n) on average. The worst case occurs when all elements in the array are identical, forcing the algorithm to decrement the right pointer linearly. In most cases where elements are distinct or duplicates are few, it behaves like a standard binary search with logarithmic complexity.
- **Space Complexity:** O(1) because the algorithm only uses a constant amount of extra space for pointers and variables, regardless of the size of the input array.
