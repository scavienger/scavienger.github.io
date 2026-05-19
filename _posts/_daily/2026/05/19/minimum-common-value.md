---
layout: post
title: "Minimum Common Value"
date: 2026-05-19 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Hash Table", "Two Pointers", "Binary Search"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/minimum-common-value/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int getCommon(vector<int>& nums1, vector<int>&\
        \ nums2) {\n        int i = 0, j = 0;\n        int n1 = nums1.size();\n    \
        \    int n2 = nums2.size();\n        while (i < n1 && j < n2) {\n          \
        \  if (nums1[i] == nums2[j]) {\n                return nums1[i];\n         \
        \   } else if (nums1[i] < nums2[j]) {\n                i++;\n            } else\
        \ {\n                j++;\n            }\n        }\n        return -1;\n  \
        \  }\n};"
      java: "class Solution {\n    public int getCommon(int[] nums1, int[] nums2) {\n\
        \        int i = 0, j = 0;\n        while (i < nums1.length && j < nums2.length)\
        \ {\n            if (nums1[i] == nums2[j]) {\n                return nums1[i];\n\
        \            } else if (nums1[i] < nums2[j]) {\n                i++;\n     \
        \       } else {\n                j++;\n            }\n        }\n        return\
        \ -1;\n    }\n}"
      python: "class Solution(object):\n    def getCommon(self, nums1, nums2):\n   \
        \     \"\"\"\n        :type nums1: List[int]\n        :type nums2: List[int]\n\
        \        :rtype: int\n        \"\"\"\n        i, j = 0, 0\n        n1, n2 =\
        \ len(nums1), len(nums2)\n        while i < n1 and j < n2:\n            if nums1[i]\
        \ == nums2[j]:\n                return nums1[i]\n            elif nums1[i] <\
        \ nums2[j]:\n                i += 1\n            else:\n                j +=\
        \ 1\n        return -1"
      python3: "class Solution:\n    def getCommon(self, nums1: List[int], nums2: List[int])\
        \ -> int:\n        i, j = 0, 0\n        n1, n2 = len(nums1), len(nums2)\n  \
        \      while i < n1 and j < n2:\n            if nums1[i] == nums2[j]:\n    \
        \            return nums1[i]\n            elif nums1[i] < nums2[j]:\n      \
        \          i += 1\n            else:\n                j += 1\n        return\
        \ -1"
      c: "int getCommon(int* nums1, int nums1Size, int* nums2, int nums2Size) {\n  \
        \  int i = 0, j = 0;\n    while (i < nums1Size && j < nums2Size) {\n       \
        \ if (nums1[i] == nums2[j]) {\n            return nums1[i];\n        } else\
        \ if (nums1[i] < nums2[j]) {\n            i++;\n        } else {\n         \
        \   j++;\n        }\n    }\n    return -1;\n}"
      csharp: "public class Solution {\n    public int GetCommon(int[] nums1, int[]\
        \ nums2) {\n        int i = 0, j = 0;\n        while (i < nums1.Length && j\
        \ < nums2.Length) {\n            if (nums1[i] == nums2[j]) {\n             \
        \   return nums1[i];\n            } else if (nums1[i] < nums2[j]) {\n      \
        \          i++;\n            } else {\n                j++;\n            }\n\
        \        }\n        return -1;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums1\n * @param {number[]} nums2\n * @return\
        \ {number}\n */\nvar getCommon = function(nums1, nums2) {\n    let i = 0, j\
        \ = 0;\n    while (i < nums1.length && j < nums2.length) {\n        if (nums1[i]\
        \ === nums2[j]) {\n            return nums1[i];\n        } else if (nums1[i]\
        \ < nums2[j]) {\n            i++;\n        } else {\n            j++;\n    \
        \    }\n    }\n    return -1;\n};"
      typescript: "function getCommon(nums1: number[], nums2: number[]): number {\n\
        \    let i = 0;\n    let j = 0;\n    while (i < nums1.length && j < nums2.length)\
        \ {\n        if (nums1[i] === nums2[j]) {\n            return nums1[i];\n  \
        \      } else if (nums1[i] < nums2[j]) {\n            i++;\n        } else {\n\
        \            j++;\n        }\n    }\n    return -1;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums1\n     * @param\
        \ Integer[] $nums2\n     * @return Integer\n     */\n    function getCommon($nums1,\
        \ $nums2) {\n        $i = 0;\n        $j = 0;\n        $len1 = count($nums1);\n\
        \        $len2 = count($nums2);\n        while ($i < $len1 && $j < $len2) {\n\
        \            if ($nums1[$i] === $nums2[$j]) {\n                return $nums1[$i];\n\
        \            } else if ($nums1[$i] < $nums2[$j]) {\n                $i++;\n\
        \            } else {\n                $j++;\n            }\n        }\n   \
        \     return -1;\n    }\n}"
      swift: "class Solution {\n    func getCommon(_ nums1: [Int], _ nums2: [Int]) ->\
        \ Int {\n        var i = 0\n        var j = 0\n        while i < nums1.count\
        \ && j < nums2.count {\n            if nums1[i] == nums2[j] {\n            \
        \    return nums1[i]\n            } else if nums1[i] < nums2[j] {\n        \
        \        i += 1\n            } else {\n                j += 1\n            }\n\
        \        }\n        return -1\n    }\n}"
      kotlin: "class Solution {\n    fun getCommon(nums1: IntArray, nums2: IntArray):\
        \ Int {\n        var i = 0\n        var j = 0\n        while (i < nums1.size\
        \ && j < nums2.size) {\n            if (nums1[i] == nums2[j]) {\n          \
        \      return nums1[i]\n            } else if (nums1[i] < nums2[j]) {\n    \
        \            i++\n            } else {\n                j++\n            }\n\
        \        }\n        return -1\n    }\n}"
      dart: "class Solution {\n  int getCommon(List<int> nums1, List<int> nums2) {\n\
        \    int i = 0;\n    int j = 0;\n    while (i < nums1.length && j < nums2.length)\
        \ {\n      if (nums1[i] == nums2[j]) {\n        return nums1[i];\n      } else\
        \ if (nums1[i] < nums2[j]) {\n        i++;\n      } else {\n        j++;\n \
        \     }\n    }\n    return -1;\n  }\n}"
      go: "func getCommon(nums1 []int, nums2 []int) int {\n    i, j := 0, 0\n    for\
        \ i < len(nums1) && j < len(nums2) {\n        if nums1[i] == nums2[j] {\n  \
        \          return nums1[i]\n        } else if nums1[i] < nums2[j] {\n      \
        \      i++\n        } else {\n            j++\n        }\n    }\n    return\
        \ -1\n}"
      ruby: "# @param {Integer[]} nums1\n# @param {Integer[]} nums2\n# @return {Integer}\n\
        def get_common(nums1, nums2)\n  i = 0\n  j = 0\n  n1 = nums1.length\n  n2 =\
        \ nums2.length\n  while i < n1 && j < n2\n    if nums1[i] == nums2[j]\n    \
        \  return nums1[i]\n    elsif nums1[i] < nums2[j]\n      i += 1\n    else\n\
        \      j += 1\n    end\n  end\n  -1\nend"
      scala: "object Solution {\n    def getCommon(nums1: Array[Int], nums2: Array[Int]):\
        \ Int = {\n        var i = 0\n        var j = 0\n        val n1 = nums1.length\n\
        \        val n2 = nums2.length\n        while (i < n1 && j < n2) {\n       \
        \     if (nums1(i) == nums2(j)) {\n                return nums1(i)\n       \
        \     } else if (nums1(i) < nums2(j)) {\n                i += 1\n          \
        \  } else {\n                j += 1\n            }\n        }\n        -1\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn get_common(nums1: Vec<i32>, nums2: Vec<i32>)\
        \ -> i32 {\n        let mut i = 0;\n        let mut j = 0;\n        while i\
        \ < nums1.len() && j < nums2.len() {\n            if nums1[i] == nums2[j] {\n\
        \                return nums1[i];\n            } else if nums1[i] < nums2[j]\
        \ {\n                i += 1;\n            } else {\n                j += 1;\n\
        \            }\n        }\n        -1\n    }\n}"
      racket: "(define/contract (get-common nums1 nums2)\n  (-> (listof exact-integer?)\
        \ (listof exact-integer?) exact-integer?)\n  (let loop ([l1 nums1]\n       \
        \      [l2 nums2])\n    (cond\n      [(or (null? l1) (null? l2)) -1]\n     \
        \ [(= (car l1) (car l2)) (car l1)]\n      [(< (car l1) (car l2)) (loop (cdr\
        \ l1) l2)]\n      [else (loop l1 (cdr l2))]))\n  )"
      erlang: "-spec get_common(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().\n\
        get_common(Nums1, Nums2) ->\n  find_common(Nums1, Nums2).\n\nfind_common([],\
        \ _) -> -1;\nfind_common(_, []) -> -1;\nfind_common([H1|T1], [H2|T2]) ->\n \
        \ if\n    H1 == H2 -> H1;\n    H1 < H2 -> find_common(T1, [H2|T2]);\n    true\
        \ -> find_common([H1|T1], T2)\n  end."
      elixir: "defmodule Solution do\n  @spec get_common(nums1 :: [integer], nums2 ::\
        \ [integer]) :: integer\n  def get_common(nums1, nums2) do\n    find_common(nums1,\
        \ nums2)\n  end\n\n  defp find_common([], _), do: -1\n  defp find_common(_,\
        \ []), do: -1\n  defp find_common([h1 | t1] = l1, [h2 | t2] = l2) do\n    cond\
        \ do\n      h1 == h2 -> h1\n      h1 < h2 -> find_common(t1, l2)\n      true\
        \ -> find_common(l1, t2)\n    end\n  end\nend"
    approach: 'The algorithm uses a two-pointer approach to leverage the fact that both
      input arrays are already sorted in non-decreasing order. Two indices, i and j,
      are initialized to the beginning of nums1 and nums2, respectively. By comparing
      the elements at these indices, we can efficiently traverse both arrays in a single
      pass. If the values at both pointers are equal, that value is the smallest common
      integer since the pointers move from left to right, and we return it immediately.


      If the values are not equal, we increment the pointer that points to the smaller
      value. This is because all subsequent values in that array are greater than or
      equal to the current value, and any possible common element must be at least as
      large as the value at the other pointer. This process continues until a match
      is found or until one of the pointers moves beyond the end of its respective array.
      If the loop concludes without finding a match, the function returns -1.'
    time_complexity: O(n + m), where n is the length of nums1 and m is the length of
      nums2. In the worst case, each pointer travels the full length of its array exactly
      once, resulting in a linear traversal relative to the total number of elements.
    space_complexity: O(1). The solution only uses a fixed number of integer variables
      for indexing (i and j), regardless of the size of the input arrays, meaning no
      extra memory proportional to the input size is required.
    elapsed_time: 67.11519455909729
    model: gemini-3-flash-preview
    generated_at: '2026-05-19 02:37:29 '
---

## Problem #2540: Minimum Common Value

**Difficulty:** Easy

**Topics:** Array, Hash Table, Two Pointers, Binary Search

## Problem Description

<p>Given two integer arrays <code>nums1</code> and <code>nums2</code>, sorted in non-decreasing order, return <em>the <strong>minimum integer common</strong> to both arrays</em>. If there is no common integer amongst <code>nums1</code> and <code>nums2</code>, return <code>-1</code>.</p>

<p>Note that an integer is said to be <strong>common</strong> to <code>nums1</code> and <code>nums2</code> if both arrays have <strong>at least one</strong> occurrence of that integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2,3], nums2 = [2,4]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The smallest element common to both arrays is 2, so we return 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2,3,6], nums2 = [2,3,4,5]
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums1[i], nums2[j] &lt;= 10<sup>9</sup></code></li>
	<li>Both <code>nums1</code> and <code>nums2</code> are sorted in <strong>non-decreasing</strong> order.</li>
</ul>


## Hints

1. Try to use a set.

2. Otherwise, try to use a two-pointer approach.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm uses a two-pointer approach to leverage the fact that both input arrays are already sorted in non-decreasing order. Two indices, i and j, are initialized to the beginning of nums1 and nums2, respectively. By comparing the elements at these indices, we can efficiently traverse both arrays in a single pass. If the values at both pointers are equal, that value is the smallest common integer since the pointers move from left to right, and we return it immediately.

If the values are not equal, we increment the pointer that points to the smaller value. This is because all subsequent values in that array are greater than or equal to the current value, and any possible common element must be at least as large as the value at the other pointer. This process continues until a match is found or until one of the pointers moves beyond the end of its respective array. If the loop concludes without finding a match, the function returns -1.

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
    int getCommon(vector<int>& nums1, vector<int>& nums2) {
        int i = 0, j = 0;
        int n1 = nums1.size();
        int n2 = nums2.size();
        while (i < n1 && j < n2) {
            if (nums1[i] == nums2[j]) {
                return nums1[i];
            } else if (nums1[i] < nums2[j]) {
                i++;
            } else {
                j++;
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
    public int getCommon(int[] nums1, int[] nums2) {
        int i = 0, j = 0;
        while (i < nums1.length && j < nums2.length) {
            if (nums1[i] == nums2[j]) {
                return nums1[i];
            } else if (nums1[i] < nums2[j]) {
                i++;
            } else {
                j++;
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
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        i, j = 0, 0
        n1, n2 = len(nums1), len(nums2)
        while i < n1 and j < n2:
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        n1, n2 = len(nums1), len(nums2)
        while i < n1 and j < n2:
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int getCommon(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int i = 0, j = 0;
    while (i < nums1Size && j < nums2Size) {
        if (nums1[i] == nums2[j]) {
            return nums1[i];
        } else if (nums1[i] < nums2[j]) {
            i++;
        } else {
            j++;
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
    public int GetCommon(int[] nums1, int[] nums2) {
        int i = 0, j = 0;
        while (i < nums1.Length && j < nums2.Length) {
            if (nums1[i] == nums2[j]) {
                return nums1[i];
            } else if (nums1[i] < nums2[j]) {
                i++;
            } else {
                j++;
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
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var getCommon = function(nums1, nums2) {
    let i = 0, j = 0;
    while (i < nums1.length && j < nums2.length) {
        if (nums1[i] === nums2[j]) {
            return nums1[i];
        } else if (nums1[i] < nums2[j]) {
            i++;
        } else {
            j++;
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
function getCommon(nums1: number[], nums2: number[]): number {
    let i = 0;
    let j = 0;
    while (i < nums1.length && j < nums2.length) {
        if (nums1[i] === nums2[j]) {
            return nums1[i];
        } else if (nums1[i] < nums2[j]) {
            i++;
        } else {
            j++;
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
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function getCommon($nums1, $nums2) {
        $i = 0;
        $j = 0;
        $len1 = count($nums1);
        $len2 = count($nums2);
        while ($i < $len1 && $j < $len2) {
            if ($nums1[$i] === $nums2[$j]) {
                return $nums1[$i];
            } else if ($nums1[$i] < $nums2[$j]) {
                $i++;
            } else {
                $j++;
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
    func getCommon(_ nums1: [Int], _ nums2: [Int]) -> Int {
        var i = 0
        var j = 0
        while i < nums1.count && j < nums2.count {
            if nums1[i] == nums2[j] {
                return nums1[i]
            } else if nums1[i] < nums2[j] {
                i += 1
            } else {
                j += 1
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
    fun getCommon(nums1: IntArray, nums2: IntArray): Int {
        var i = 0
        var j = 0
        while (i < nums1.size && j < nums2.size) {
            if (nums1[i] == nums2[j]) {
                return nums1[i]
            } else if (nums1[i] < nums2[j]) {
                i++
            } else {
                j++
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
  int getCommon(List<int> nums1, List<int> nums2) {
    int i = 0;
    int j = 0;
    while (i < nums1.length && j < nums2.length) {
      if (nums1[i] == nums2[j]) {
        return nums1[i];
      } else if (nums1[i] < nums2[j]) {
        i++;
      } else {
        j++;
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
func getCommon(nums1 []int, nums2 []int) int {
    i, j := 0, 0
    for i < len(nums1) && j < len(nums2) {
        if nums1[i] == nums2[j] {
            return nums1[i]
        } else if nums1[i] < nums2[j] {
            i++
        } else {
            j++
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
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def get_common(nums1, nums2)
  i = 0
  j = 0
  n1 = nums1.length
  n2 = nums2.length
  while i < n1 && j < n2
    if nums1[i] == nums2[j]
      return nums1[i]
    elsif nums1[i] < nums2[j]
      i += 1
    else
      j += 1
    end
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
    def getCommon(nums1: Array[Int], nums2: Array[Int]): Int = {
        var i = 0
        var j = 0
        val n1 = nums1.length
        val n2 = nums2.length
        while (i < n1 && j < n2) {
            if (nums1(i) == nums2(j)) {
                return nums1(i)
            } else if (nums1(i) < nums2(j)) {
                i += 1
            } else {
                j += 1
            }
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
    pub fn get_common(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let mut i = 0;
        let mut j = 0;
        while i < nums1.len() && j < nums2.len() {
            if nums1[i] == nums2[j] {
                return nums1[i];
            } else if nums1[i] < nums2[j] {
                i += 1;
            } else {
                j += 1;
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
(define/contract (get-common nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let loop ([l1 nums1]
             [l2 nums2])
    (cond
      [(or (null? l1) (null? l2)) -1]
      [(= (car l1) (car l2)) (car l1)]
      [(< (car l1) (car l2)) (loop (cdr l1) l2)]
      [else (loop l1 (cdr l2))]))
  )
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec get_common(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
get_common(Nums1, Nums2) ->
  find_common(Nums1, Nums2).

find_common([], _) -> -1;
find_common(_, []) -> -1;
find_common([H1|T1], [H2|T2]) ->
  if
    H1 == H2 -> H1;
    H1 < H2 -> find_common(T1, [H2|T2]);
    true -> find_common([H1|T1], T2)
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec get_common(nums1 :: [integer], nums2 :: [integer]) :: integer
  def get_common(nums1, nums2) do
    find_common(nums1, nums2)
  end

  defp find_common([], _), do: -1
  defp find_common(_, []), do: -1
  defp find_common([h1 | t1] = l1, [h2 | t2] = l2) do
    cond do
      h1 == h2 -> h1
      h1 < h2 -> find_common(t1, l2)
      true -> find_common(l1, t2)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n + m), where n is the length of nums1 and m is the length of nums2. In the worst case, each pointer travels the full length of its array exactly once, resulting in a linear traversal relative to the total number of elements.
- **Space Complexity:** O(1). The solution only uses a fixed number of integer variables for indexing (i and j), regardless of the size of the input arrays, meaning no extra memory proportional to the input size is required.
