---
layout: post
title: "Find the Distance Value Between Two Arrays"
date: 2026-11-05 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Two Pointers", "Binary Search", "Sorting"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int findTheDistanceValue(vector<int>& arr1,\
        \ vector<int>& arr2, int d) {\n        sort(arr2.begin(), arr2.end());\n   \
        \     int count = 0;\n        for (int x : arr1) {\n            auto it = lower_bound(arr2.begin(),\
        \ arr2.end(), x - d);\n            if (it == arr2.end() || *it > x + d) {\n\
        \                count++;\n            }\n        }\n        return count;\n\
        \    }\n};"
      java: "import java.util.Arrays;\n\nclass Solution {\n    public int findTheDistanceValue(int[]\
        \ arr1, int[] arr2, int d) {\n        Arrays.sort(arr2);\n        int count\
        \ = 0;\n        for (int x : arr1) {\n            int idx = Arrays.binarySearch(arr2,\
        \ x - d);\n            if (idx < 0) {\n                idx = -(idx + 1);\n \
        \           }\n            if (idx == arr2.length || arr2[idx] > x + d) {\n\
        \                count++;\n            }\n        }\n        return count;\n\
        \    }\n}"
      python: "class Solution(object):\n    def findTheDistanceValue(self, arr1, arr2,\
        \ d):\n        \"\"\"\n        :type arr1: List[int]\n        :type arr2: List[int]\n\
        \        :type d: int\n        :rtype: int\n        \"\"\"\n        import bisect\n\
        \        arr2.sort()\n        count = 0\n        for x in arr1:\n          \
        \  idx = bisect.bisect_left(arr2, x - d)\n            if idx == len(arr2) or\
        \ arr2[idx] > x + d:\n                count += 1\n        return count"
      python3: "import bisect\n\nclass Solution:\n    def findTheDistanceValue(self,\
        \ arr1: list[int], arr2: list[int], d: int) -> int:\n        arr2.sort()\n \
        \       count = 0\n        for x in arr1:\n            idx = bisect.bisect_left(arr2,\
        \ x - d)\n            if idx == len(arr2) or arr2[idx] > x + d:\n          \
        \      count += 1\n        return count"
      c: "int compare(const void *a, const void *b) {\n    return (*(int*)a - *(int*)b);\n\
        }\n\nint findTheDistanceValue(int* arr1, int arr1Size, int* arr2, int arr2Size,\
        \ int d) {\n    qsort(arr2, arr2Size, sizeof(int), compare);\n    int count\
        \ = 0;\n    for (int i = 0; i < arr1Size; i++) {\n        int x = arr1[i];\n\
        \        int left = 0, right = arr2Size - 1;\n        int found = 0;\n     \
        \   while (left <= right) {\n            int mid = left + (right - left) / 2;\n\
        \            if (arr2[mid] >= x - d && arr2[mid] <= x + d) {\n             \
        \   found = 1;\n                break;\n            } else if (arr2[mid] < x\
        \ - d) {\n                left = mid + 1;\n            } else {\n          \
        \      right = mid - 1;\n            }\n        }\n        if (!found) count++;\n\
        \    }\n    return count;\n}"
      csharp: "using System;\n\npublic class Solution {\n    public int FindTheDistanceValue(int[]\
        \ arr1, int[] arr2, int d) {\n        Array.Sort(arr2);\n        int count =\
        \ 0;\n        foreach (int x in arr1) {\n            int idx = Array.BinarySearch(arr2,\
        \ x - d);\n            if (idx < 0) {\n                idx = ~idx;\n       \
        \     }\n            if (idx == arr2.Length || arr2[idx] > x + d) {\n      \
        \          count++;\n            }\n        }\n        return count;\n    }\n\
        }"
      javascript: "/**\n * @param {number[]} arr1\n * @param {number[]} arr2\n * @param\
        \ {number} d\n * @return {number}\n */\nvar findTheDistanceValue = function(arr1,\
        \ arr2, d) {\n    arr2.sort((a, b) => a - b);\n    let count = 0;\n    for (let\
        \ x of arr1) {\n        let left = 0;\n        let right = arr2.length - 1;\n\
        \        let found = false;\n        while (left <= right) {\n            let\
        \ mid = Math.floor((left + right) / 2);\n            if (arr2[mid] >= x - d\
        \ && arr2[mid] <= x + d) {\n                found = true;\n                break;\n\
        \            } else if (arr2[mid] < x - d) {\n                left = mid + 1;\n\
        \            } else {\n                right = mid - 1;\n            }\n   \
        \     }\n        if (!found) count++;\n    }\n    return count;\n};"
      typescript: "function findTheDistanceValue(arr1: number[], arr2: number[], d:\
        \ number): number {\n    arr2.sort((a, b) => a - b);\n    let count = 0;\n\n\
        \    for (const x of arr1) {\n        let low = 0;\n        let high = arr2.length\
        \ - 1;\n        let isValid = true;\n\n        while (low <= high) {\n     \
        \       const mid = Math.floor((low + high) / 2);\n            if (arr2[mid]\
        \ >= x - d && arr2[mid] <= x + d) {\n                isValid = false;\n    \
        \            break;\n            }\n            if (arr2[mid] < x - d) {\n \
        \               low = mid + 1;\n            } else {\n                high =\
        \ mid - 1;\n            }\n        }\n\n        if (isValid) {\n           \
        \ count++;\n        }\n    }\n\n    return count;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $arr1\n     * @param\
        \ Integer[] $arr2\n     * @param Integer $d\n     * @return Integer\n     */\n\
        \    function findTheDistanceValue($arr1, $arr2, $d) {\n        sort($arr2);\n\
        \        $count = 0;\n        $n2 = count($arr2);\n\n        foreach ($arr1\
        \ as $x) {\n            $low = 0;\n            $high = $n2 - 1;\n          \
        \  $isValid = true;\n\n            while ($low <= $high) {\n               \
        \ $mid = (int)(($low + $high) / 2);\n                if ($arr2[$mid] >= $x -\
        \ $d && $arr2[$mid] <= $x + $d) {\n                    $isValid = false;\n \
        \                   break;\n                }\n                if ($arr2[$mid]\
        \ < $x - $d) {\n                    $low = $mid + 1;\n                } else\
        \ {\n                    $high = $mid - 1;\n                }\n            }\n\
        \n            if ($isValid) {\n                $count++;\n            }\n  \
        \      }\n\n        return $count;\n    }\n}"
      swift: "class Solution {\n    func findTheDistanceValue(_ arr1: [Int], _ arr2:\
        \ [Int], _ d: Int) -> Int {\n        let sortedArr2 = arr2.sorted()\n      \
        \  var count = 0\n\n        for x in arr1 {\n            var low = 0\n     \
        \       var high = sortedArr2.count - 1\n            var isValid = true\n\n\
        \            while low <= high {\n                let mid = low + (high - low)\
        \ / 2\n                if sortedArr2[mid] >= x - d && sortedArr2[mid] <= x +\
        \ d {\n                    isValid = false\n                    break\n    \
        \            }\n                if sortedArr2[mid] < x - d {\n             \
        \       low = mid + 1\n                } else {\n                    high =\
        \ mid - 1\n                }\n            }\n\n            if isValid {\n  \
        \              count += 1\n            }\n        }\n\n        return count\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun findTheDistanceValue(arr1: IntArray, arr2:\
        \ IntArray, d: Int): Int {\n        arr2.sort()\n        var count = 0\n\n \
        \       for (x in arr1) {\n            var low = 0\n            var high = arr2.size\
        \ - 1\n            var isValid = true\n\n            while (low <= high) {\n\
        \                val mid = low + (high - low) / 2\n                if (arr2[mid]\
        \ >= x - d && arr2[mid] <= x + d) {\n                    isValid = false\n \
        \                   break\n                }\n                if (arr2[mid]\
        \ < x - d) {\n                    low = mid + 1\n                } else {\n\
        \                    high = mid - 1\n                }\n            }\n\n  \
        \          if (isValid) {\n                count++\n            }\n        }\n\
        \n        return count\n    }\n}"
      dart: "class Solution {\n  int findTheDistanceValue(List<int> arr1, List<int>\
        \ arr2, int d) {\n    arr2.sort();\n    int count = 0;\n\n    for (int x in\
        \ arr1) {\n      int low = 0;\n      int high = arr2.length - 1;\n      bool\
        \ isValid = true;\n\n      while (low <= high) {\n        int mid = low + (high\
        \ - low) ~/ 2;\n        if (arr2[mid] >= x - d && arr2[mid] <= x + d) {\n  \
        \        isValid = false;\n          break;\n        }\n        if (arr2[mid]\
        \ < x - d) {\n          low = mid + 1;\n        } else {\n          high = mid\
        \ - 1;\n        }\n      }\n\n      if (isValid) {\n        count++;\n     \
        \ }\n    }\n\n    return count;\n  }\n}"
      go: "import \"sort\"\n\nfunc findTheDistanceValue(arr1 []int, arr2 []int, d int)\
        \ int {\n    sort.Ints(arr2)\n    count := 0\n\n    for _, x := range arr1 {\n\
        \        low := 0\n        high := len(arr2) - 1\n        isValid := true\n\n\
        \        for low <= high {\n            mid := low + (high-low)/2\n        \
        \    if arr2[mid] >= x-d && arr2[mid] <= x+d {\n                isValid = false\n\
        \                break\n            }\n            if arr2[mid] < x-d {\n  \
        \              low = mid + 1\n            } else {\n                high = mid\
        \ - 1\n            }\n        }\n\n        if isValid {\n            count++\n\
        \        }\n    }\n\n    return count\n}"
      ruby: "def find_the_distance_value(arr1, arr2, d)\n  arr1.count do |x|\n    arr2.all?\
        \ { |y| (x - y).abs > d }\n  end\nend"
      scala: "object Solution {\n  def findTheDistanceValue(arr1: Array[Int], arr2:\
        \ Array[Int], d: Int): Int = {\n    arr1.count(x => arr2.forall(y => (x - y).abs\
        \ > d))\n  }\n}"
      rust: "impl Solution {\n    pub fn find_the_distance_value(arr1: Vec<i32>, arr2:\
        \ Vec<i32>, d: i32) -> i32 {\n        arr1.iter()\n            .filter(|&&x|\
        \ arr2.iter().all(|&y| (x - y).abs() > d))\n            .count() as i32\n  \
        \  }\n}"
      racket: "(define/contract (find-the-distance-value arr1 arr2 d)\n  (-> (listof\
        \ exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)\n \
        \ (count (lambda (x)\n           (andmap (lambda (y) (> (abs (- x y)) d))\n\
        \                   arr2))\n         arr1))"
      erlang: "-spec find_the_distance_value(Arr1 :: [integer()], Arr2 :: [integer()],\
        \ D :: integer()) -> integer().\nfind_the_distance_value(Arr1, Arr2, D) ->\n\
        \  length([X || X <- Arr1, lists:all(fun(Y) -> abs(X - Y) > D end, Arr2)])."
      elixir: "defmodule Solution do\n  @spec find_the_distance_value(arr1 :: [integer],\
        \ arr2 :: [integer], d :: integer) :: integer\n  def find_the_distance_value(arr1,\
        \ arr2, d) do\n    Enum.count(arr1, fn x ->\n      Enum.all?(arr2, fn y -> abs(x\
        \ - y) > d end)\n    end)\n  end\nend"
    approach: 'The distance value is calculated by counting the elements in arr1 that
      do not have any element in arr2 within the range [arr1[i] - d, arr1[i] + d]. To
      efficiently check this condition, we first sort arr2 in ascending order. For each
      element in arr1, we use binary search to find the position where arr1[i] - d would
      fit into the sorted arr2. This identifies the smallest element in arr2 that is
      greater than or equal to the lower bound of our forbidden range.


      Once we find this potential candidate in arr2 using binary search, we simply check
      if its value is less than or equal to arr1[i] + d. If the candidate exists and
      falls within the upper bound, it means there is at least one element in arr2 that
      satisfies the condition |arr1[i] - arr2[j]| <= d. If no such candidate exists
      or the candidate is outside the range, we increment our distance value counter.
      This approach significantly optimizes the search from a linear scan to logarithmic
      time per element in arr1.'
    time_complexity: O(M log M + N log M), where N is the length of arr1 and M is the
      length of arr2. Sorting arr2 takes O(M log M) time, and for each of the N elements
      in arr1, we perform a binary search on arr2 which takes O(log M) time.
    space_complexity: O(1) or O(M) depending on the sorting implementation. In many
      languages like C++ or Java, the sorting algorithm typically uses O(log M) stack
      space, while in Python, Timsort uses O(M) auxiliary space.
    elapsed_time: 118.87838983535767
    model: gemini-3-flash-preview
    generated_at: '2026-11-05 04:32:56 '
---

## Problem #1385: Find the Distance Value Between Two Arrays

**Difficulty:** Easy

**Topics:** Array, Two Pointers, Binary Search, Sorting

## Problem Description

<p>Given two integer arrays <code>arr1</code> and <code>arr2</code>, and the integer <code>d</code>, <em>return the distance value between the two arrays</em>.</p>

<p>The distance value is defined as the number of elements <code>arr1[i]</code> such that there is not any element <code>arr2[j]</code> where <code>|arr1[i]-arr2[j]| &lt;= d</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
For arr1[0]=4 we have: 
|4-10|=6 &gt; d=2 
|4-9|=5 &gt; d=2 
|4-1|=3 &gt; d=2 
|4-8|=4 &gt; d=2 
For arr1[1]=5 we have: 
|5-10|=5 &gt; d=2 
|5-9|=4 &gt; d=2 
|5-1|=4 &gt; d=2 
|5-8|=3 &gt; d=2
For arr1[2]=8 we have:
<strong>|8-10|=2 &lt;= d=2</strong>
<strong>|8-9|=1 &lt;= d=2</strong>
|8-1|=7 &gt; d=2
<strong>|8-8|=0 &lt;= d=2</strong>
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr1.length, arr2.length &lt;= 500</code></li>
	<li><code>-1000 &lt;= arr1[i], arr2[j] &lt;= 1000</code></li>
	<li><code>0 &lt;= d &lt;= 100</code></li>
</ul>


## Hints

1. Sort 'arr2' and use binary search to get the closest element for each 'arr1[i]', it gives a time complexity of O(nlogn).

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The distance value is calculated by counting the elements in arr1 that do not have any element in arr2 within the range [arr1[i] - d, arr1[i] + d]. To efficiently check this condition, we first sort arr2 in ascending order. For each element in arr1, we use binary search to find the position where arr1[i] - d would fit into the sorted arr2. This identifies the smallest element in arr2 that is greater than or equal to the lower bound of our forbidden range.

Once we find this potential candidate in arr2 using binary search, we simply check if its value is less than or equal to arr1[i] + d. If the candidate exists and falls within the upper bound, it means there is at least one element in arr2 that satisfies the condition |arr1[i] - arr2[j]| <= d. If no such candidate exists or the candidate is outside the range, we increment our distance value counter. This approach significantly optimizes the search from a linear scan to logarithmic time per element in arr1.

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
    int findTheDistanceValue(vector<int>& arr1, vector<int>& arr2, int d) {
        sort(arr2.begin(), arr2.end());
        int count = 0;
        for (int x : arr1) {
            auto it = lower_bound(arr2.begin(), arr2.end(), x - d);
            if (it == arr2.end() || *it > x + d) {
                count++;
            }
        }
        return count;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.Arrays;

class Solution {
    public int findTheDistanceValue(int[] arr1, int[] arr2, int d) {
        Arrays.sort(arr2);
        int count = 0;
        for (int x : arr1) {
            int idx = Arrays.binarySearch(arr2, x - d);
            if (idx < 0) {
                idx = -(idx + 1);
            }
            if (idx == arr2.length || arr2[idx] > x + d) {
                count++;
            }
        }
        return count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        import bisect
        arr2.sort()
        count = 0
        for x in arr1:
            idx = bisect.bisect_left(arr2, x - d)
            if idx == len(arr2) or arr2[idx] > x + d:
                count += 1
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import bisect

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        count = 0
        for x in arr1:
            idx = bisect.bisect_left(arr2, x - d)
            if idx == len(arr2) or arr2[idx] > x + d:
                count += 1
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int findTheDistanceValue(int* arr1, int arr1Size, int* arr2, int arr2Size, int d) {
    qsort(arr2, arr2Size, sizeof(int), compare);
    int count = 0;
    for (int i = 0; i < arr1Size; i++) {
        int x = arr1[i];
        int left = 0, right = arr2Size - 1;
        int found = 0;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr2[mid] >= x - d && arr2[mid] <= x + d) {
                found = 1;
                break;
            } else if (arr2[mid] < x - d) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        if (!found) count++;
    }
    return count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public int FindTheDistanceValue(int[] arr1, int[] arr2, int d) {
        Array.Sort(arr2);
        int count = 0;
        foreach (int x in arr1) {
            int idx = Array.BinarySearch(arr2, x - d);
            if (idx < 0) {
                idx = ~idx;
            }
            if (idx == arr2.Length || arr2[idx] > x + d) {
                count++;
            }
        }
        return count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @param {number} d
 * @return {number}
 */
var findTheDistanceValue = function(arr1, arr2, d) {
    arr2.sort((a, b) => a - b);
    let count = 0;
    for (let x of arr1) {
        let left = 0;
        let right = arr2.length - 1;
        let found = false;
        while (left <= right) {
            let mid = Math.floor((left + right) / 2);
            if (arr2[mid] >= x - d && arr2[mid] <= x + d) {
                found = true;
                break;
            } else if (arr2[mid] < x - d) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        if (!found) count++;
    }
    return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function findTheDistanceValue(arr1: number[], arr2: number[], d: number): number {
    arr2.sort((a, b) => a - b);
    let count = 0;

    for (const x of arr1) {
        let low = 0;
        let high = arr2.length - 1;
        let isValid = true;

        while (low <= high) {
            const mid = Math.floor((low + high) / 2);
            if (arr2[mid] >= x - d && arr2[mid] <= x + d) {
                isValid = false;
                break;
            }
            if (arr2[mid] < x - d) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        if (isValid) {
            count++;
        }
    }

    return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $arr1
     * @param Integer[] $arr2
     * @param Integer $d
     * @return Integer
     */
    function findTheDistanceValue($arr1, $arr2, $d) {
        sort($arr2);
        $count = 0;
        $n2 = count($arr2);

        foreach ($arr1 as $x) {
            $low = 0;
            $high = $n2 - 1;
            $isValid = true;

            while ($low <= $high) {
                $mid = (int)(($low + $high) / 2);
                if ($arr2[$mid] >= $x - $d && $arr2[$mid] <= $x + $d) {
                    $isValid = false;
                    break;
                }
                if ($arr2[$mid] < $x - $d) {
                    $low = $mid + 1;
                } else {
                    $high = $mid - 1;
                }
            }

            if ($isValid) {
                $count++;
            }
        }

        return $count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func findTheDistanceValue(_ arr1: [Int], _ arr2: [Int], _ d: Int) -> Int {
        let sortedArr2 = arr2.sorted()
        var count = 0

        for x in arr1 {
            var low = 0
            var high = sortedArr2.count - 1
            var isValid = true

            while low <= high {
                let mid = low + (high - low) / 2
                if sortedArr2[mid] >= x - d && sortedArr2[mid] <= x + d {
                    isValid = false
                    break
                }
                if sortedArr2[mid] < x - d {
                    low = mid + 1
                } else {
                    high = mid - 1
                }
            }

            if isValid {
                count += 1
            }
        }

        return count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun findTheDistanceValue(arr1: IntArray, arr2: IntArray, d: Int): Int {
        arr2.sort()
        var count = 0

        for (x in arr1) {
            var low = 0
            var high = arr2.size - 1
            var isValid = true

            while (low <= high) {
                val mid = low + (high - low) / 2
                if (arr2[mid] >= x - d && arr2[mid] <= x + d) {
                    isValid = false
                    break
                }
                if (arr2[mid] < x - d) {
                    low = mid + 1
                } else {
                    high = mid - 1
                }
            }

            if (isValid) {
                count++
            }
        }

        return count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int findTheDistanceValue(List<int> arr1, List<int> arr2, int d) {
    arr2.sort();
    int count = 0;

    for (int x in arr1) {
      int low = 0;
      int high = arr2.length - 1;
      bool isValid = true;

      while (low <= high) {
        int mid = low + (high - low) ~/ 2;
        if (arr2[mid] >= x - d && arr2[mid] <= x + d) {
          isValid = false;
          break;
        }
        if (arr2[mid] < x - d) {
          low = mid + 1;
        } else {
          high = mid - 1;
        }
      }

      if (isValid) {
        count++;
      }
    }

    return count;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "sort"

func findTheDistanceValue(arr1 []int, arr2 []int, d int) int {
    sort.Ints(arr2)
    count := 0

    for _, x := range arr1 {
        low := 0
        high := len(arr2) - 1
        isValid := true

        for low <= high {
            mid := low + (high-low)/2
            if arr2[mid] >= x-d && arr2[mid] <= x+d {
                isValid = false
                break
            }
            if arr2[mid] < x-d {
                low = mid + 1
            } else {
                high = mid - 1
            }
        }

        if isValid {
            count++
        }
    }

    return count
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def find_the_distance_value(arr1, arr2, d)
  arr1.count do |x|
    arr2.all? { |y| (x - y).abs > d }
  end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def findTheDistanceValue(arr1: Array[Int], arr2: Array[Int], d: Int): Int = {
    arr1.count(x => arr2.forall(y => (x - y).abs > d))
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn find_the_distance_value(arr1: Vec<i32>, arr2: Vec<i32>, d: i32) -> i32 {
        arr1.iter()
            .filter(|&&x| arr2.iter().all(|&y| (x - y).abs() > d))
            .count() as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (find-the-distance-value arr1 arr2 d)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  (count (lambda (x)
           (andmap (lambda (y) (> (abs (- x y)) d))
                   arr2))
         arr1))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec find_the_distance_value(Arr1 :: [integer()], Arr2 :: [integer()], D :: integer()) -> integer().
find_the_distance_value(Arr1, Arr2, D) ->
  length([X || X <- Arr1, lists:all(fun(Y) -> abs(X - Y) > D end, Arr2)]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec find_the_distance_value(arr1 :: [integer], arr2 :: [integer], d :: integer) :: integer
  def find_the_distance_value(arr1, arr2, d) do
    Enum.count(arr1, fn x ->
      Enum.all?(arr2, fn y -> abs(x - y) > d end)
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(M log M + N log M), where N is the length of arr1 and M is the length of arr2. Sorting arr2 takes O(M log M) time, and for each of the N elements in arr1, we perform a binary search on arr2 which takes O(log M) time.
- **Space Complexity:** O(1) or O(M) depending on the sorting implementation. In many languages like C++ or Java, the sorting algorithm typically uses O(log M) stack space, while in Python, Timsort uses O(M) auxiliary space.
