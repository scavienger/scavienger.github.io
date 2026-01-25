---
layout: post
title: "Minimum Difference Between Highest and Lowest of K Scores"
date: 2026-01-25 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Sliding Window", "Sorting"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minimumDifference(vector<int>& nums,\
        \ int k) {\n        if (k == 1) return 0;\n        sort(nums.begin(), nums.end());\n\
        \        int min_diff = nums[k - 1] - nums[0];\n        int n = nums.size();\n\
        \        for (int i = 1; i <= n - k; ++i) {\n            min_diff = min(min_diff,\
        \ nums[i + k - 1] - nums[i]);\n        }\n        return min_diff;\n    }\n\
        };"
      java: "class Solution {\n    public int minimumDifference(int[] nums, int k) {\n\
        \        if (k == 1) return 0;\n        Arrays.sort(nums);\n        int n =\
        \ nums.length;\n        int minDiff = Integer.MAX_VALUE;\n        for (int i\
        \ = 0; i <= n - k; i++) {\n            int currentDiff = nums[i + k - 1] - nums[i];\n\
        \            if (currentDiff < minDiff) {\n                minDiff = currentDiff;\n\
        \            }\n        }\n        return minDiff;\n    }\n}"
      python: "class Solution(object):\n    def minimumDifference(self, nums, k):\n\
        \        \"\"\"\n        :type nums: List[int]\n        :type k: int\n     \
        \   :rtype: int\n        \"\"\"\n        if k == 1: return 0\n        nums.sort()\n\
        \        min_diff = float('inf')\n        for i in range(len(nums) - k + 1):\n\
        \            diff = nums[i + k - 1] - nums[i]\n            if diff < min_diff:\n\
        \                min_diff = diff\n        return min_diff"
      python3: "class Solution:\n    def minimumDifference(self, nums: List[int], k:\
        \ int) -> int:\n        if k == 1: return 0\n        nums.sort()\n        n\
        \ = len(nums)\n        min_diff = nums[k - 1] - nums[0]\n        for i in range(1,\
        \ n - k + 1):\n            min_diff = min(min_diff, nums[i + k - 1] - nums[i])\n\
        \        return min_diff"
      c: "int compare(const void* a, const void* b) {\n    return (*(int*)a - *(int*)b);\n\
        }\n\nint minimumDifference(int* nums, int numsSize, int k) {\n    if (k == 1)\
        \ return 0;\n    qsort(nums, numsSize, sizeof(int), compare);\n    int minDiff\
        \ = nums[k - 1] - nums[0];\n    for (int i = 1; i <= numsSize - k; i++) {\n\
        \        int diff = nums[i + k - 1] - nums[i];\n        if (diff < minDiff)\
        \ {\n            minDiff = diff;\n        }\n    }\n    return minDiff;\n}"
      csharp: "public class Solution {\n    public int MinimumDifference(int[] nums,\
        \ int k) {\n        if (k == 1) return 0;\n        Array.Sort(nums);\n     \
        \   int minDiff = int.MaxValue;\n        for (int i = 0; i <= nums.Length -\
        \ k; i++) {\n            int currentDiff = nums[i + k - 1] - nums[i];\n    \
        \        if (currentDiff < minDiff) {\n                minDiff = currentDiff;\n\
        \            }\n        }\n        return minDiff;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} k\n * @return\
        \ {number}\n */\nvar minimumDifference = function(nums, k) {\n    if (k ===\
        \ 1) return 0;\n    nums.sort((a, b) => a - b);\n    let minDiff = Infinity;\n\
        \    for (let i = 0; i <= nums.length - k; i++) {\n        let currentDiff =\
        \ nums[i + k - 1] - nums[i];\n        if (currentDiff < minDiff) {\n       \
        \     minDiff = currentDiff;\n        }\n    }\n    return minDiff;\n};"
      typescript: "function minimumDifference(nums: number[], k: number): number {\n\
        \  if (k === 1) return 0;\n  nums.sort((a, b) => a - b);\n  let minDiff = Infinity;\n\
        \  for (let i = 0; i <= nums.length - k; i++) {\n    minDiff = Math.min(minDiff,\
        \ nums[i + k - 1] - nums[i]);\n  }\n  return minDiff;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer $k\n     * @return Integer\n     */\n    function minimumDifference($nums,\
        \ $k) {\n        if ($k === 1) return 0;\n        sort($nums);\n        $minDiff\
        \ = $nums[$k - 1] - $nums[0];\n        $n = count($nums);\n        for ($i =\
        \ 1; $i <= $n - $k; $i++) {\n            $minDiff = min($minDiff, $nums[$i +\
        \ $k - 1] - $nums[$i]);\n        }\n        return $minDiff;\n    }\n}"
      swift: "class Solution {\n    func minimumDifference(_ nums: [Int], _ k: Int)\
        \ -> Int {\n        if k == 1 { return 0 }\n        let sortedNums = nums.sorted()\n\
        \        var minDiff = Int.max\n        for i in 0...(sortedNums.count - k)\
        \ {\n            let diff = sortedNums[i + k - 1] - sortedNums[i]\n        \
        \    if diff < minDiff {\n                minDiff = diff\n            }\n  \
        \      }\n        return minDiff\n    }\n}"
      kotlin: "class Solution {\n    fun minimumDifference(nums: IntArray, k: Int):\
        \ Int {\n        if (k == 1) return 0\n        nums.sort()\n        var minDiff\
        \ = Int.MAX_VALUE\n        for (i in 0..nums.size - k) {\n            val diff\
        \ = nums[i + k - 1] - nums[i]\n            if (diff < minDiff) {\n         \
        \       minDiff = diff\n            }\n        }\n        return minDiff\n \
        \   }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int minimumDifference(List<int>\
        \ nums, int k) {\n    if (k == 1) return 0;\n    nums.sort();\n    int minDiff\
        \ = nums[k - 1] - nums[0];\n    for (int i = 1; i <= nums.length - k; i++) {\n\
        \      minDiff = min(minDiff, nums[i + k - 1] - nums[i]);\n    }\n    return\
        \ minDiff;\n  }\n}"
      go: "import \"sort\"\n\nfunc minimumDifference(nums []int, k int) int {\n    if\
        \ k == 1 {\n        return 0\n    }\n    sort.Ints(nums)\n    minDiff := nums[k-1]\
        \ - nums[0]\n    for i := 1; i <= len(nums)-k; i++ {\n        diff := nums[i+k-1]\
        \ - nums[i]\n        if diff < minDiff {\n            minDiff = diff\n     \
        \   }\n    }\n    return minDiff\n}"
      ruby: "def minimum_difference(nums, k)\n  return 0 if k <= 1\n  nums.sort!\n \
        \ min_diff = nums[k - 1] - nums[0]\n  (1..nums.length - k).each do |i|\n   \
        \ diff = nums[i + k - 1] - nums[i]\n    min_diff = diff if diff < min_diff\n\
        \  end\n  min_diff\nend"
      scala: "object Solution {\n  def minimumDifference(nums: Array[Int], k: Int):\
        \ Int = {\n    if (k <= 1) return 0\n    val sortedNums = nums.sorted\n    var\
        \ minDiff = sortedNums(k - 1) - sortedNums(0)\n    for (i <- 1 to (sortedNums.length\
        \ - k)) {\n      val diff = sortedNums(i + k - 1) - sortedNums(i)\n      if\
        \ (diff < minDiff) minDiff = diff\n    }\n    minDiff\n  }\n}"
      rust: "impl Solution {\n    pub fn minimum_difference(nums: Vec<i32>, k: i32)\
        \ -> i32 {\n        if k <= 1 {\n            return 0;\n        }\n        let\
        \ mut nums = nums;\n        nums.sort();\n        let k_size = k as usize;\n\
        \        let mut min_diff = i32::MAX;\n        for i in 0..=(nums.len() - k_size)\
        \ {\n            let diff = nums[i + k_size - 1] - nums[i];\n            if\
        \ diff < min_diff {\n                min_diff = diff;\n            }\n     \
        \   }\n        min_diff\n    }\n}"
      racket: "(define/contract (minimum-difference nums k)\n  (-> (listof exact-integer?)\
        \ exact-integer? exact-integer?)\n  (let* ([sorted-nums (sort nums <)]\n   \
        \      [vec (list->vector sorted-nums)]\n         [len (vector-length vec)])\n\
        \    (if (<= k 1)\n        0\n        (for/fold ([min-diff 10000000])\n    \
        \              ([i (in-range 0 (+ 1 (- len k)))])\n          (min min-diff (-\
        \ (vector-ref vec (+ i k - 1)) (vector-ref vec i)))))))"
      erlang: "minimum_difference(Nums, K) ->\n  Sorted = lists:sort(Nums),\n  Len =\
        \ length(Sorted),\n  find_min(Sorted, K, Len, 1000000).\n\nfind_min(_List, K,\
        \ Len, Min) when Len < K ->\n  Min;\nfind_min(List = [H | T], K, Len, Min) ->\n\
        \  Diff = lists:nth(K, List) - H,\n  NewMin = if Diff < Min -> Diff; true ->\
        \ Min end,\n  find_min(T, K, Len - 1, NewMin)."
      elixir: "defmodule Solution do\n  @spec minimum_difference(nums :: [integer],\
        \ k :: integer) :: integer\n  def minimum_difference(nums, k) do\n    if k <=\
        \ 1 do\n      0\n    else\n      nums\n      |> Enum.sort()\n      |> Enum.chunk_every(k,\
        \ 1, :discard)\n      |> Enum.map(fn window -> List.last(window) - hd(window)\
        \ end)\n      |> Enum.min()\n    end\n  end\nend"
    approach: 'To minimize the difference between the highest and lowest scores of k
      students, we must select scores that are as close to each other as possible. The
      most effective way to identify such clusters is to sort the array in non-decreasing
      order. Once sorted, any set of k elements that could minimize the range must be
      a contiguous subarray. If we were to pick k elements that are not contiguous in
      the sorted array, we could reduce the range by shifting the outlier elements towards
      the rest of the group until they are contiguous.


      After sorting the array, we iterate through it using a sliding window of size
      k. For each window starting at index i and ending at index i + k - 1, we calculate
      the difference between the last and first elements of the window (nums[i + k -
      1] - nums[i]). We keep track of the minimum difference encountered during this
      single pass. The result of this process is the minimum possible difference for
      any k selected scores.'
    time_complexity: O(n log n), where n is the number of elements in the array. This
      complexity is primarily determined by the sorting step. The subsequent linear
      scan with the sliding window takes O(n) time, which does not change the overall
      asymptotic complexity.
    space_complexity: O(log n) to O(n), depending on the implementation of the sorting
      algorithm. Many standard library sorting implementations (like Timsort or intro-sort)
      utilize O(log n) or O(n) auxiliary space for recursion or temporary storage.
    elapsed_time: 208.387033700943
    model: gemini-3-pro-preview
    generated_at: '2026-01-25 01:20:47 '
---

## Problem #1984: Minimum Difference Between Highest and Lowest of K Scores

**Difficulty:** Easy

**Topics:** Array, Sliding Window, Sorting

## Problem Description

<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code>, where <code>nums[i]</code> represents the score of the <code>i<sup>th</sup></code> student. You are also given an integer <code>k</code>.</p>

<p>Pick the scores of any <code>k</code> students from the array so that the <strong>difference</strong> between the <strong>highest</strong> and the <strong>lowest</strong> of the <code>k</code> scores is <strong>minimized</strong>.</p>

<p>Return <em>the <strong>minimum</strong> possible difference</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [90], k = 1
<strong>Output:</strong> 0
<strong>Explanation:</strong> There is one way to pick score(s) of one student:
- [<strong><u>90</u></strong>]. The difference between the highest and lowest score is 90 - 90 = 0.
The minimum possible difference is 0.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [9,4,1,7], k = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are six ways to pick score(s) of two students:
- [<strong><u>9</u></strong>,<strong><u>4</u></strong>,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
- [<strong><u>9</u></strong>,4,<strong><u>1</u></strong>,7]. The difference between the highest and lowest score is 9 - 1 = 8.
- [<strong><u>9</u></strong>,4,1,<strong><u>7</u></strong>]. The difference between the highest and lowest score is 9 - 7 = 2.
- [9,<strong><u>4</u></strong>,<strong><u>1</u></strong>,7]. The difference between the highest and lowest score is 4 - 1 = 3.
- [9,<strong><u>4</u></strong>,1,<strong><u>7</u></strong>]. The difference between the highest and lowest score is 7 - 4 = 3.
- [9,4,<strong><u>1</u></strong>,<strong><u>7</u></strong>]. The difference between the highest and lowest score is 7 - 1 = 6.
The minimum possible difference is 2.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. For the difference between the highest and lowest element to be minimized, the k chosen scores need to be as close to each other as possible.

2. What if the array was sorted?

3. After sorting the scores, any contiguous k scores are as close to each other as possible.

4. Apply a sliding window solution to iterate over each contiguous k scores, and find the minimum of the differences of all windows.

## ✨ AI-Generated Solution (gemini-3-pro-preview)

### Approach

To minimize the difference between the highest and lowest scores of k students, we must select scores that are as close to each other as possible. The most effective way to identify such clusters is to sort the array in non-decreasing order. Once sorted, any set of k elements that could minimize the range must be a contiguous subarray. If we were to pick k elements that are not contiguous in the sorted array, we could reduce the range by shifting the outlier elements towards the rest of the group until they are contiguous.

After sorting the array, we iterate through it using a sliding window of size k. For each window starting at index i and ending at index i + k - 1, we calculate the difference between the last and first elements of the window (nums[i + k - 1] - nums[i]). We keep track of the minimum difference encountered during this single pass. The result of this process is the minimum possible difference for any k selected scores.

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
    int minimumDifference(vector<int>& nums, int k) {
        if (k == 1) return 0;
        sort(nums.begin(), nums.end());
        int min_diff = nums[k - 1] - nums[0];
        int n = nums.size();
        for (int i = 1; i <= n - k; ++i) {
            min_diff = min(min_diff, nums[i + k - 1] - nums[i]);
        }
        return min_diff;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minimumDifference(int[] nums, int k) {
        if (k == 1) return 0;
        Arrays.sort(nums);
        int n = nums.length;
        int minDiff = Integer.MAX_VALUE;
        for (int i = 0; i <= n - k; i++) {
            int currentDiff = nums[i + k - 1] - nums[i];
            if (currentDiff < minDiff) {
                minDiff = currentDiff;
            }
        }
        return minDiff;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 1: return 0
        nums.sort()
        min_diff = float('inf')
        for i in range(len(nums) - k + 1):
            diff = nums[i + k - 1] - nums[i]
            if diff < min_diff:
                min_diff = diff
        return min_diff
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1: return 0
        nums.sort()
        n = len(nums)
        min_diff = nums[k - 1] - nums[0]
        for i in range(1, n - k + 1):
            min_diff = min(min_diff, nums[i + k - 1] - nums[i])
        return min_diff
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int minimumDifference(int* nums, int numsSize, int k) {
    if (k == 1) return 0;
    qsort(nums, numsSize, sizeof(int), compare);
    int minDiff = nums[k - 1] - nums[0];
    for (int i = 1; i <= numsSize - k; i++) {
        int diff = nums[i + k - 1] - nums[i];
        if (diff < minDiff) {
            minDiff = diff;
        }
    }
    return minDiff;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinimumDifference(int[] nums, int k) {
        if (k == 1) return 0;
        Array.Sort(nums);
        int minDiff = int.MaxValue;
        for (int i = 0; i <= nums.Length - k; i++) {
            int currentDiff = nums[i + k - 1] - nums[i];
            if (currentDiff < minDiff) {
                minDiff = currentDiff;
            }
        }
        return minDiff;
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
 * @param {number} k
 * @return {number}
 */
var minimumDifference = function(nums, k) {
    if (k === 1) return 0;
    nums.sort((a, b) => a - b);
    let minDiff = Infinity;
    for (let i = 0; i <= nums.length - k; i++) {
        let currentDiff = nums[i + k - 1] - nums[i];
        if (currentDiff < minDiff) {
            minDiff = currentDiff;
        }
    }
    return minDiff;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimumDifference(nums: number[], k: number): number {
  if (k === 1) return 0;
  nums.sort((a, b) => a - b);
  let minDiff = Infinity;
  for (let i = 0; i <= nums.length - k; i++) {
    minDiff = Math.min(minDiff, nums[i + k - 1] - nums[i]);
  }
  return minDiff;
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
     * @param Integer $k
     * @return Integer
     */
    function minimumDifference($nums, $k) {
        if ($k === 1) return 0;
        sort($nums);
        $minDiff = $nums[$k - 1] - $nums[0];
        $n = count($nums);
        for ($i = 1; $i <= $n - $k; $i++) {
            $minDiff = min($minDiff, $nums[$i + $k - 1] - $nums[$i]);
        }
        return $minDiff;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minimumDifference(_ nums: [Int], _ k: Int) -> Int {
        if k == 1 { return 0 }
        let sortedNums = nums.sorted()
        var minDiff = Int.max
        for i in 0...(sortedNums.count - k) {
            let diff = sortedNums[i + k - 1] - sortedNums[i]
            if diff < minDiff {
                minDiff = diff
            }
        }
        return minDiff
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minimumDifference(nums: IntArray, k: Int): Int {
        if (k == 1) return 0
        nums.sort()
        var minDiff = Int.MAX_VALUE
        for (i in 0..nums.size - k) {
            val diff = nums[i + k - 1] - nums[i]
            if (diff < minDiff) {
                minDiff = diff
            }
        }
        return minDiff
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
  int minimumDifference(List<int> nums, int k) {
    if (k == 1) return 0;
    nums.sort();
    int minDiff = nums[k - 1] - nums[0];
    for (int i = 1; i <= nums.length - k; i++) {
      minDiff = min(minDiff, nums[i + k - 1] - nums[i]);
    }
    return minDiff;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "sort"

func minimumDifference(nums []int, k int) int {
    if k == 1 {
        return 0
    }
    sort.Ints(nums)
    minDiff := nums[k-1] - nums[0]
    for i := 1; i <= len(nums)-k; i++ {
        diff := nums[i+k-1] - nums[i]
        if diff < minDiff {
            minDiff = diff
        }
    }
    return minDiff
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def minimum_difference(nums, k)
  return 0 if k <= 1
  nums.sort!
  min_diff = nums[k - 1] - nums[0]
  (1..nums.length - k).each do |i|
    diff = nums[i + k - 1] - nums[i]
    min_diff = diff if diff < min_diff
  end
  min_diff
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def minimumDifference(nums: Array[Int], k: Int): Int = {
    if (k <= 1) return 0
    val sortedNums = nums.sorted
    var minDiff = sortedNums(k - 1) - sortedNums(0)
    for (i <- 1 to (sortedNums.length - k)) {
      val diff = sortedNums(i + k - 1) - sortedNums(i)
      if (diff < minDiff) minDiff = diff
    }
    minDiff
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn minimum_difference(nums: Vec<i32>, k: i32) -> i32 {
        if k <= 1 {
            return 0;
        }
        let mut nums = nums;
        nums.sort();
        let k_size = k as usize;
        let mut min_diff = i32::MAX;
        for i in 0..=(nums.len() - k_size) {
            let diff = nums[i + k_size - 1] - nums[i];
            if diff < min_diff {
                min_diff = diff;
            }
        }
        min_diff
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (minimum-difference nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([sorted-nums (sort nums <)]
         [vec (list->vector sorted-nums)]
         [len (vector-length vec)])
    (if (<= k 1)
        0
        (for/fold ([min-diff 10000000])
                  ([i (in-range 0 (+ 1 (- len k)))])
          (min min-diff (- (vector-ref vec (+ i k - 1)) (vector-ref vec i)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
minimum_difference(Nums, K) ->
  Sorted = lists:sort(Nums),
  Len = length(Sorted),
  find_min(Sorted, K, Len, 1000000).

find_min(_List, K, Len, Min) when Len < K ->
  Min;
find_min(List = [H | T], K, Len, Min) ->
  Diff = lists:nth(K, List) - H,
  NewMin = if Diff < Min -> Diff; true -> Min end,
  find_min(T, K, Len - 1, NewMin).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_difference(nums :: [integer], k :: integer) :: integer
  def minimum_difference(nums, k) do
    if k <= 1 do
      0
    else
      nums
      |> Enum.sort()
      |> Enum.chunk_every(k, 1, :discard)
      |> Enum.map(fn window -> List.last(window) - hd(window) end)
      |> Enum.min()
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n log n), where n is the number of elements in the array. This complexity is primarily determined by the sorting step. The subsequent linear scan with the sliding window takes O(n) time, which does not change the overall asymptotic complexity.
- **Space Complexity:** O(log n) to O(n), depending on the implementation of the sorting algorithm. Many standard library sorting implementations (like Timsort or intro-sort) utilize O(log n) or O(n) auxiliary space for recursion or temporary storage.
