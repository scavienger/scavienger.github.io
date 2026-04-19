---
layout: post
title: "Maximum Distance Between a Pair of Values"
date: 2026-04-19 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Two Pointers", "Binary Search"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxDistance(vector<int>& nums1, vector<int>&\
        \ nums2) {\n        int i = 0, j = 0, maxDist = 0;\n        int n = nums1.size();\n\
        \        int m = nums2.size();\n\n        while (i < n && j < m) {\n       \
        \     if (nums1[i] <= nums2[j]) {\n                maxDist = max(maxDist, j\
        \ - i);\n                j++;\n            } else {\n                i++;\n\
        \            }\n        }\n\n        return maxDist;\n    }\n};"
      java: "class Solution {\n    public int maxDistance(int[] nums1, int[] nums2)\
        \ {\n        int i = 0, j = 0, maxDist = 0;\n        int n = nums1.length;\n\
        \        int m = nums2.length;\n\n        while (i < n && j < m) {\n       \
        \     if (nums1[i] <= nums2[j]) {\n                maxDist = Math.max(maxDist,\
        \ j - i);\n                j++;\n            } else {\n                i++;\n\
        \            }\n        }\n\n        return maxDist;\n    }\n}"
      python: "class Solution(object):\n    def maxDistance(self, nums1, nums2):\n \
        \       \"\"\"\n        :type nums1: List[int]\n        :type nums2: List[int]\n\
        \        :rtype: int\n        \"\"\"\n        i = j = res = 0\n        n1, n2\
        \ = len(nums1), len(nums2)\n        while i < n1 and j < n2:\n            if\
        \ nums1[i] <= nums2[j]:\n                if j - i > res:\n                 \
        \   res = j - i\n                j += 1\n            else:\n               \
        \ i += 1\n        return res"
      python3: "class Solution:\n    def maxDistance(self, nums1: List[int], nums2:\
        \ List[int]) -> int:\n        i = j = res = 0\n        n1, n2 = len(nums1),\
        \ len(nums2)\n        while i < n1 and j < n2:\n            if nums1[i] <= nums2[j]:\n\
        \                res = max(res, j - i)\n                j += 1\n           \
        \ else:\n                i += 1\n        return res"
      c: "int maxDistance(int* nums1, int nums1Size, int* nums2, int nums2Size) {\n\
        \    int i = 0, j = 0, maxDist = 0;\n    while (i < nums1Size && j < nums2Size)\
        \ {\n        if (nums1[i] <= nums2[j]) {\n            if (j - i > maxDist) {\n\
        \                maxDist = j - i;\n            }\n            j++;\n       \
        \ } else {\n            i++;\n        }\n    }\n    return maxDist;\n}"
      csharp: "public class Solution {\n    public int MaxDistance(int[] nums1, int[]\
        \ nums2) {\n        int i = 0, j = 0, maxDist = 0;\n        int n1 = nums1.Length,\
        \ n2 = nums2.Length;\n        while (i < n1 && j < n2) {\n            if (nums1[i]\
        \ <= nums2[j]) {\n                if (j - i > maxDist) {\n                 \
        \   maxDist = j - i;\n                }\n                j++;\n            }\
        \ else {\n                i++;\n            }\n        }\n        return maxDist;\n\
        \    }\n}"
      javascript: "/**\n * @param {number[]} nums1\n * @param {number[]} nums2\n * @return\
        \ {number}\n */\nvar maxDistance = function(nums1, nums2) {\n    let i = 0,\
        \ j = 0, maxDist = 0;\n    const n1 = nums1.length, n2 = nums2.length;\n   \
        \ while (i < n1 && j < n2) {\n        if (nums1[i] <= nums2[j]) {\n        \
        \    maxDist = Math.max(maxDist, j - i);\n            j++;\n        } else {\n\
        \            i++;\n        }\n    }\n    return maxDist;\n};"
      typescript: "function maxDistance(nums1: number[], nums2: number[]): number {\n\
        \    let i = 0, j = 0, maxDist = 0;\n    const n1 = nums1.length, n2 = nums2.length;\n\
        \    while (i < n1 && j < n2) {\n        if (nums1[i] <= nums2[j]) {\n     \
        \       maxDist = Math.max(maxDist, j - i);\n            j++;\n        } else\
        \ {\n            i++;\n        }\n    }\n    return maxDist;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums1\n     * @param\
        \ Integer[] $nums2\n     * @return Integer\n     */\n    function maxDistance($nums1,\
        \ $nums2) {\n        $i = 0;\n        $j = 0;\n        $maxDist = 0;\n     \
        \   $n1 = count($nums1);\n        $n2 = count($nums2);\n        while ($i <\
        \ $n1 && $j < $n2) {\n            if ($nums1[$i] <= $nums2[$j]) {\n        \
        \        $maxDist = max($maxDist, $j - $i);\n                $j++;\n       \
        \     } else {\n                $i++;\n            }\n        }\n        return\
        \ $maxDist;\n    }\n}"
      swift: "class Solution {\n    func maxDistance(_ nums1: [Int], _ nums2: [Int])\
        \ -> Int {\n        var i = 0\n        var j = 0\n        var maxDist = 0\n\
        \        let n1 = nums1.count\n        let n2 = nums2.count\n        while i\
        \ < n1 && j < n2 {\n            if nums1[i] <= nums2[j] {\n                maxDist\
        \ = max(maxDist, j - i)\n                j += 1\n            } else {\n    \
        \            i += 1\n            }\n        }\n        return maxDist\n    }\n\
        }"
      kotlin: "class Solution {\n    fun maxDistance(nums1: IntArray, nums2: IntArray):\
        \ Int {\n        var i = 0\n        var j = 0\n        var maxDist = 0\n   \
        \     val n1 = nums1.size\n        val n2 = nums2.size\n        while (i < n1\
        \ && j < n2) {\n            if (nums1[i] <= nums2[j]) {\n                val\
        \ dist = j - i\n                if (dist > maxDist) {\n                    maxDist\
        \ = dist\n                }\n                j++\n            } else {\n   \
        \             i++\n            }\n        }\n        return maxDist\n    }\n\
        }"
      dart: "class Solution {\n  int maxDistance(List<int> nums1, List<int> nums2) {\n\
        \    int i = 0;\n    int j = 0;\n    int maxDist = 0;\n    int n1 = nums1.length;\n\
        \    int n2 = nums2.length;\n    while (i < n1 && j < n2) {\n      if (nums1[i]\
        \ <= nums2[j]) {\n        int dist = j - i;\n        if (dist > maxDist) {\n\
        \          maxDist = dist;\n        }\n        j++;\n      } else {\n      \
        \  i++;\n      }\n    }\n    return maxDist;\n  }\n}"
      go: "func maxDistance(nums1 []int, nums2 []int) int {\n    i, j, maxDist := 0,\
        \ 0, 0\n    n1, n2 := len(nums1), len(nums2)\n    for i < n1 && j < n2 {\n \
        \       if nums1[i] <= nums2[j] {\n            dist := j - i\n            if\
        \ dist > maxDist {\n                maxDist = dist\n            }\n        \
        \    j++\n        } else {\n            i++\n        }\n    }\n    return maxDist\n\
        }"
      ruby: "# @param {Integer[]} nums1\n# @param {Integer[]} nums2\n# @return {Integer}\n\
        def max_distance(nums1, nums2)\n    i = 0\n    j = 0\n    max_dist = 0\n   \
        \ n1 = nums1.length\n    n2 = nums2.length\n    while i < n1 && j < n2\n   \
        \     if nums1[i] <= nums2[j]\n            dist = j - i\n            max_dist\
        \ = dist if dist > max_dist\n            j += 1\n        else\n            i\
        \ += 1\n        end\n    end\n    max_dist\nend"
      scala: "object Solution {\n    def maxDistance(nums1: Array[Int], nums2: Array[Int]):\
        \ Int = {\n        var i = 0\n        var j = 0\n        var maxDist = 0\n \
        \       val n1 = nums1.length\n        val n2 = nums2.length\n        while\
        \ (i < n1 && j < n2) {\n            if (nums1[i] <= nums2[j]) {\n          \
        \      val dist = j - i\n                if (dist > maxDist) {\n           \
        \         maxDist = dist\n                }\n                j += 1\n      \
        \      } else {\n                i += 1\n            }\n        }\n        maxDist\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn max_distance(nums1: Vec<i32>, nums2: Vec<i32>)\
        \ -> i32 {\n        let mut i: usize = 0;\n        let mut j: usize = 0;\n \
        \       let mut max_dist: i32 = 0;\n        let n1 = nums1.len();\n        let\
        \ n2 = nums2.len();\n\n        while i < n1 && j < n2 {\n            if nums1[i]\
        \ <= nums2[j] {\n                let dist = (j as i32) - (i as i32);\n     \
        \           if dist > max_dist {\n                    max_dist = dist;\n   \
        \             }\n                j += 1;\n            } else {\n           \
        \     i += 1;\n            }\n        }\n\n        max_dist\n    }\n}"
      racket: "(define/contract (max-distance nums1 nums2)\n  (-> (listof exact-integer?)\
        \ (listof exact-integer?) exact-integer?)\n  (let ([v1 (list->vector nums1)]\n\
        \        [v2 (list->vector nums2)])\n    (let ([n1 (vector-length v1)]\n   \
        \       [n2 (vector-length v2)])\n      (let loop ([i 0] [j 0] [res 0])\n  \
        \      (if (or (= i n1) (= j n2))\n            res\n            (if (<= (vector-ref\
        \ v1 i) (vector-ref v2 j))\n                (loop i (+ j 1) (max res (- j i)))\n\
        \                (loop (+ i 1) j res)))))))"
      erlang: "-spec max_distance(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().\n\
        max_distance(Nums1, Nums2) ->\n    do_max_distance(Nums1, Nums2, 0, 0, 0).\n\
        \ndo_max_distance([H1 | T1] = L1, [H2 | T2] = L2, I, J, MaxDist) ->\n    if\n\
        \        H1 =< H2 ->\n            do_max_distance(L1, T2, I, J + 1, erlang:max(MaxDist,\
        \ J - I));\n        true ->\n            do_max_distance(T1, L2, I + 1, J, MaxDist)\n\
        \    end;\ndo_max_distance(_, _, _, _, MaxDist) ->\n    MaxDist."
      elixir: "defmodule Solution do\n  @spec max_distance(nums1 :: [integer], nums2\
        \ :: [integer]) :: integer\n  def max_distance(nums1, nums2) do\n    do_max_distance(nums1,\
        \ nums2, 0, 0, 0)\n  end\n\n  defp do_max_distance([h1 | t1] = l1, [h2 | t2]\
        \ = l2, i, j, max_dist) do\n    if h1 <= h2 do\n      do_max_distance(l1, t2,\
        \ i, j + 1, max(max_dist, j - i))\n    else\n      do_max_distance(t1, l2, i\
        \ + 1, j, max_dist)\n    end\n  end\n\n  defp do_max_distance(_nums1, _nums2,\
        \ _i, _j, max_dist) do\n    max_dist\n  end\nend"
    approach: 'The problem can be solved efficiently using a two-pointer approach because
      both arrays are sorted in non-increasing order. We initialize two pointers, i
      for nums1 and j for nums2, starting at the beginning of each array. Since the
      values in both arrays are non-increasing, if a pair (i, j) satisfies the condition
      nums1[i] ≤ nums2[j], then for the same i, we should try increasing j to find the
      largest possible distance. Conversely, if the condition is not met, it means nums1[i]
      is too large for the current nums2[j], and since nums2 values only decrease further,
      we must increment i to look for a smaller value in nums1.


      Specifically, the algorithm iterates through the arrays as long as i is within
      the bounds of nums1 and j is within the bounds of nums2. At each step, if nums1[i]
      ≤ nums2[j], we update the maximum distance with j - i and move j forward. If the
      condition is false, we move i forward. This strategy works because as i increases,
      the required threshold nums1[i] decreases, potentially allowing even larger j
      indices to satisfy the condition. The two-pointer logic ensures we explore all
      potentially optimal pairs in linear time without redundant comparisons.'
    time_complexity: O(n + m) where n is the length of nums1 and m is the length of
      nums2. Each pointer i and j is incremented at most n and m times respectively,
      resulting in a single pass through the data.
    space_complexity: O(1) because we only use a constant amount of extra space for
      pointers and the maximum distance variable, regardless of the input size.
    elapsed_time: 193.35880661010742
    model: gemini-3-flash-preview
    generated_at: '2026-04-19 02:02:04 '
---

## Problem #1855: Maximum Distance Between a Pair of Values

**Difficulty:** Medium

**Topics:** Array, Two Pointers, Binary Search

## Problem Description

<p>You are given two <strong>non-increasing 0-indexed </strong>integer arrays <code>nums1</code>​​​​​​ and <code>nums2</code>​​​​​​.</p>

<p>A pair of indices <code>(i, j)</code>, where <code>0 &lt;= i &lt; nums1.length</code> and <code>0 &lt;= j &lt; nums2.length</code>, is <strong>valid</strong> if both <code>i &lt;= j</code> and <code>nums1[i] &lt;= nums2[j]</code>. The <strong>distance</strong> of the pair is <code>j - i</code>​​​​.</p>

<p>Return <em>the <strong>maximum distance</strong> of any <strong>valid</strong> pair </em><code>(i, j)</code><em>. If there are no valid pairs, return </em><code>0</code>.</p>

<p>An array <code>arr</code> is <strong>non-increasing</strong> if <code>arr[i-1] &gt;= arr[i]</code> for every <code>1 &lt;= i &lt; arr.length</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The valid pairs are (0,0), (2,2), (2,3), (2,4), (3,3), (3,4), and (4,4).
The maximum distance is 2 with pair (2,4).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [2,2,2], nums2 = [10,10,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The valid pairs are (0,0), (0,1), and (1,1).
The maximum distance is 1 with pair (0,1).
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The valid pairs are (2,2), (2,3), (2,4), (3,3), and (3,4).
The maximum distance is 2 with pair (2,4).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums1[i], nums2[j] &lt;= 10<sup>5</sup></code></li>
	<li>Both <code>nums1</code> and <code>nums2</code> are <strong>non-increasing</strong>.</li>
</ul>


## Hints

1. Since both arrays are sorted in a non-increasing way this means that for each value in the first array. We can find the farthest value smaller than it using binary search.

2. There is another solution using a two pointers approach since the first array is non-increasing the farthest j such that nums2[j] ≥ nums1[i] is at least as far as the farthest j such that nums2[j] ≥ nums1[i-1]

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be solved efficiently using a two-pointer approach because both arrays are sorted in non-increasing order. We initialize two pointers, i for nums1 and j for nums2, starting at the beginning of each array. Since the values in both arrays are non-increasing, if a pair (i, j) satisfies the condition nums1[i] ≤ nums2[j], then for the same i, we should try increasing j to find the largest possible distance. Conversely, if the condition is not met, it means nums1[i] is too large for the current nums2[j], and since nums2 values only decrease further, we must increment i to look for a smaller value in nums1.

Specifically, the algorithm iterates through the arrays as long as i is within the bounds of nums1 and j is within the bounds of nums2. At each step, if nums1[i] ≤ nums2[j], we update the maximum distance with j - i and move j forward. If the condition is false, we move i forward. This strategy works because as i increases, the required threshold nums1[i] decreases, potentially allowing even larger j indices to satisfy the condition. The two-pointer logic ensures we explore all potentially optimal pairs in linear time without redundant comparisons.

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
    int maxDistance(vector<int>& nums1, vector<int>& nums2) {
        int i = 0, j = 0, maxDist = 0;
        int n = nums1.size();
        int m = nums2.size();

        while (i < n && j < m) {
            if (nums1[i] <= nums2[j]) {
                maxDist = max(maxDist, j - i);
                j++;
            } else {
                i++;
            }
        }

        return maxDist;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maxDistance(int[] nums1, int[] nums2) {
        int i = 0, j = 0, maxDist = 0;
        int n = nums1.length;
        int m = nums2.length;

        while (i < n && j < m) {
            if (nums1[i] <= nums2[j]) {
                maxDist = Math.max(maxDist, j - i);
                j++;
            } else {
                i++;
            }
        }

        return maxDist;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        i = j = res = 0
        n1, n2 = len(nums1), len(nums2)
        while i < n1 and j < n2:
            if nums1[i] <= nums2[j]:
                if j - i > res:
                    res = j - i
                j += 1
            else:
                i += 1
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = res = 0
        n1, n2 = len(nums1), len(nums2)
        while i < n1 and j < n2:
            if nums1[i] <= nums2[j]:
                res = max(res, j - i)
                j += 1
            else:
                i += 1
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int maxDistance(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int i = 0, j = 0, maxDist = 0;
    while (i < nums1Size && j < nums2Size) {
        if (nums1[i] <= nums2[j]) {
            if (j - i > maxDist) {
                maxDist = j - i;
            }
            j++;
        } else {
            i++;
        }
    }
    return maxDist;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaxDistance(int[] nums1, int[] nums2) {
        int i = 0, j = 0, maxDist = 0;
        int n1 = nums1.Length, n2 = nums2.Length;
        while (i < n1 && j < n2) {
            if (nums1[i] <= nums2[j]) {
                if (j - i > maxDist) {
                    maxDist = j - i;
                }
                j++;
            } else {
                i++;
            }
        }
        return maxDist;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var maxDistance = function(nums1, nums2) {
    let i = 0, j = 0, maxDist = 0;
    const n1 = nums1.length, n2 = nums2.length;
    while (i < n1 && j < n2) {
        if (nums1[i] <= nums2[j]) {
            maxDist = Math.max(maxDist, j - i);
            j++;
        } else {
            i++;
        }
    }
    return maxDist;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxDistance(nums1: number[], nums2: number[]): number {
    let i = 0, j = 0, maxDist = 0;
    const n1 = nums1.length, n2 = nums2.length;
    while (i < n1 && j < n2) {
        if (nums1[i] <= nums2[j]) {
            maxDist = Math.max(maxDist, j - i);
            j++;
        } else {
            i++;
        }
    }
    return maxDist;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function maxDistance($nums1, $nums2) {
        $i = 0;
        $j = 0;
        $maxDist = 0;
        $n1 = count($nums1);
        $n2 = count($nums2);
        while ($i < $n1 && $j < $n2) {
            if ($nums1[$i] <= $nums2[$j]) {
                $maxDist = max($maxDist, $j - $i);
                $j++;
            } else {
                $i++;
            }
        }
        return $maxDist;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxDistance(_ nums1: [Int], _ nums2: [Int]) -> Int {
        var i = 0
        var j = 0
        var maxDist = 0
        let n1 = nums1.count
        let n2 = nums2.count
        while i < n1 && j < n2 {
            if nums1[i] <= nums2[j] {
                maxDist = max(maxDist, j - i)
                j += 1
            } else {
                i += 1
            }
        }
        return maxDist
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxDistance(nums1: IntArray, nums2: IntArray): Int {
        var i = 0
        var j = 0
        var maxDist = 0
        val n1 = nums1.size
        val n2 = nums2.size
        while (i < n1 && j < n2) {
            if (nums1[i] <= nums2[j]) {
                val dist = j - i
                if (dist > maxDist) {
                    maxDist = dist
                }
                j++
            } else {
                i++
            }
        }
        return maxDist
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maxDistance(List<int> nums1, List<int> nums2) {
    int i = 0;
    int j = 0;
    int maxDist = 0;
    int n1 = nums1.length;
    int n2 = nums2.length;
    while (i < n1 && j < n2) {
      if (nums1[i] <= nums2[j]) {
        int dist = j - i;
        if (dist > maxDist) {
          maxDist = dist;
        }
        j++;
      } else {
        i++;
      }
    }
    return maxDist;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxDistance(nums1 []int, nums2 []int) int {
    i, j, maxDist := 0, 0, 0
    n1, n2 := len(nums1), len(nums2)
    for i < n1 && j < n2 {
        if nums1[i] <= nums2[j] {
            dist := j - i
            if dist > maxDist {
                maxDist = dist
            }
            j++
        } else {
            i++
        }
    }
    return maxDist
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def max_distance(nums1, nums2)
    i = 0
    j = 0
    max_dist = 0
    n1 = nums1.length
    n2 = nums2.length
    while i < n1 && j < n2
        if nums1[i] <= nums2[j]
            dist = j - i
            max_dist = dist if dist > max_dist
            j += 1
        else
            i += 1
        end
    end
    max_dist
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxDistance(nums1: Array[Int], nums2: Array[Int]): Int = {
        var i = 0
        var j = 0
        var maxDist = 0
        val n1 = nums1.length
        val n2 = nums2.length
        while (i < n1 && j < n2) {
            if (nums1[i] <= nums2[j]) {
                val dist = j - i
                if (dist > maxDist) {
                    maxDist = dist
                }
                j += 1
            } else {
                i += 1
            }
        }
        maxDist
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_distance(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let mut i: usize = 0;
        let mut j: usize = 0;
        let mut max_dist: i32 = 0;
        let n1 = nums1.len();
        let n2 = nums2.len();

        while i < n1 && j < n2 {
            if nums1[i] <= nums2[j] {
                let dist = (j as i32) - (i as i32);
                if dist > max_dist {
                    max_dist = dist;
                }
                j += 1;
            } else {
                i += 1;
            }
        }

        max_dist
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (max-distance nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let ([v1 (list->vector nums1)]
        [v2 (list->vector nums2)])
    (let ([n1 (vector-length v1)]
          [n2 (vector-length v2)])
      (let loop ([i 0] [j 0] [res 0])
        (if (or (= i n1) (= j n2))
            res
            (if (<= (vector-ref v1 i) (vector-ref v2 j))
                (loop i (+ j 1) (max res (- j i)))
                (loop (+ i 1) j res)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_distance(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
max_distance(Nums1, Nums2) ->
    do_max_distance(Nums1, Nums2, 0, 0, 0).

do_max_distance([H1 | T1] = L1, [H2 | T2] = L2, I, J, MaxDist) ->
    if
        H1 =< H2 ->
            do_max_distance(L1, T2, I, J + 1, erlang:max(MaxDist, J - I));
        true ->
            do_max_distance(T1, L2, I + 1, J, MaxDist)
    end;
do_max_distance(_, _, _, _, MaxDist) ->
    MaxDist.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_distance(nums1 :: [integer], nums2 :: [integer]) :: integer
  def max_distance(nums1, nums2) do
    do_max_distance(nums1, nums2, 0, 0, 0)
  end

  defp do_max_distance([h1 | t1] = l1, [h2 | t2] = l2, i, j, max_dist) do
    if h1 <= h2 do
      do_max_distance(l1, t2, i, j + 1, max(max_dist, j - i))
    else
      do_max_distance(t1, l2, i + 1, j, max_dist)
    end
  end

  defp do_max_distance(_nums1, _nums2, _i, _j, max_dist) do
    max_dist
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n + m) where n is the length of nums1 and m is the length of nums2. Each pointer i and j is incremented at most n and m times respectively, resulting in a single pass through the data.
- **Space Complexity:** O(1) because we only use a constant amount of extra space for pointers and the maximum distance variable, regardless of the input size.
