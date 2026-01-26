---
layout: post
title: "Minimum Absolute Difference"
date: 2026-01-26 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Sorting"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/minimum-absolute-difference/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<vector<int>> minimumAbsDifference(vector<int>&\
        \ arr) {\n        sort(arr.begin(), arr.end());\n        int minDiff = INT_MAX;\n\
        \        int n = arr.size();\n        for (int i = 0; i < n - 1; ++i) {\n  \
        \          minDiff = min(minDiff, arr[i + 1] - arr[i]);\n        }\n       \
        \ vector<vector<int>> result;\n        for (int i = 0; i < n - 1; ++i) {\n \
        \           if (arr[i + 1] - arr[i] == minDiff) {\n                result.push_back({arr[i],\
        \ arr[i + 1]});\n            }\n        }\n        return result;\n    }\n};"
      java: "class Solution {\n    public List<List<Integer>> minimumAbsDifference(int[]\
        \ arr) {\n        Arrays.sort(arr);\n        int minDiff = Integer.MAX_VALUE;\n\
        \        for (int i = 0; i < arr.length - 1; i++) {\n            minDiff = Math.min(minDiff,\
        \ arr[i + 1] - arr[i]);\n        }\n        List<List<Integer>> result = new\
        \ ArrayList<>();\n        for (int i = 0; i < arr.length - 1; i++) {\n     \
        \       if (arr[i + 1] - arr[i] == minDiff) {\n                List<Integer>\
        \ pair = new ArrayList<>();\n                pair.add(arr[i]);\n           \
        \     pair.add(arr[i + 1]);\n                result.add(pair);\n           \
        \ }\n        }\n        return result;\n    }\n}"
      python: "class Solution(object):\n    def minimumAbsDifference(self, arr):\n \
        \       \"\"\"\n        :type arr: List[int]\n        :rtype: List[List[int]]\n\
        \        \"\"\"\n        arr.sort()\n        min_diff = float('inf')\n     \
        \   for i in range(len(arr) - 1):\n            diff = arr[i+1] - arr[i]\n  \
        \          if diff < min_diff:\n                min_diff = diff\n\n        result\
        \ = []\n        for i in range(len(arr) - 1):\n            if arr[i+1] - arr[i]\
        \ == min_diff:\n                result.append([arr[i], arr[i+1]])\n        return\
        \ result"
      python3: "class Solution:\n    def minimumAbsDifference(self, arr: List[int])\
        \ -> List[List[int]]:\n        arr.sort()\n        min_diff = float('inf')\n\
        \        for i in range(len(arr) - 1):\n            min_diff = min(min_diff,\
        \ arr[i + 1] - arr[i])\n\n        return [[arr[i], arr[i + 1]] for i in range(len(arr)\
        \ - 1) if arr[i + 1] - arr[i] == min_diff]"
      c: "int compare(const void* a, const void* b) {\n    return (*(int*)a - *(int*)b);\n\
        }\n\nint** minimumAbsDifference(int* arr, int arrSize, int* returnSize, int**\
        \ returnColumnSizes) {\n    qsort(arr, arrSize, sizeof(int), compare);\n   \
        \ int minDiff = arr[1] - arr[0];\n    for (int i = 1; i < arrSize - 1; i++)\
        \ {\n        int diff = arr[i + 1] - arr[i];\n        if (diff < minDiff) minDiff\
        \ = diff;\n    }\n    int count = 0;\n    for (int i = 0; i < arrSize - 1; i++)\
        \ {\n        if (arr[i + 1] - arr[i] == minDiff) count++;\n    }\n    *returnSize\
        \ = count;\n    *returnColumnSizes = (int*)malloc(count * sizeof(int));\n  \
        \  int** result = (int**)malloc(count * sizeof(int*));\n    int idx = 0;\n \
        \   for (int i = 0; i < arrSize - 1; i++) {\n        if (arr[i + 1] - arr[i]\
        \ == minDiff) {\n            result[idx] = (int*)malloc(2 * sizeof(int));\n\
        \            result[idx][0] = arr[i];\n            result[idx][1] = arr[i +\
        \ 1];\n            (*returnColumnSizes)[idx] = 2;\n            idx++;\n    \
        \    }\n    }\n    return result;\n}"
      csharp: "public class Solution {\n    public IList<IList<int>> MinimumAbsDifference(int[]\
        \ arr) {\n        Array.Sort(arr);\n        int minDiff = int.MaxValue;\n  \
        \      for (int i = 0; i < arr.Length - 1; i++) {\n            int diff = arr[i\
        \ + 1] - arr[i];\n            if (diff < minDiff) minDiff = diff;\n        }\n\
        \        IList<IList<int>> result = new List<IList<int>>();\n        for (int\
        \ i = 0; i < arr.Length - 1; i++) {\n            if (arr[i + 1] - arr[i] ==\
        \ minDiff) {\n                result.Add(new List<int> { arr[i], arr[i + 1]\
        \ });\n            }\n        }\n        return result;\n    }\n}"
      javascript: "/**\n * @param {number[]} arr\n * @return {number[][]}\n */\nvar\
        \ minimumAbsDifference = function(arr) {\n    arr.sort((a, b) => a - b);\n \
        \   let minDiff = Infinity;\n    for (let i = 0; i < arr.length - 1; i++) {\n\
        \        minDiff = Math.min(minDiff, arr[i + 1] - arr[i]);\n    }\n    const\
        \ result = [];\n    for (let i = 0; i < arr.length - 1; i++) {\n        if (arr[i\
        \ + 1] - arr[i] === minDiff) {\n            result.push([arr[i], arr[i + 1]]);\n\
        \        }\n    }\n    return result;\n};"
      typescript: '// Generation failed for TypeScript

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''The model is overloaded. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      php: '// Generation failed for PHP

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''The model is overloaded. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      swift: '// Generation failed for Swift

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''The model is overloaded. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      kotlin: '// Generation failed for Kotlin

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''The model is overloaded. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      dart: '// Generation failed for Dart

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''The model is overloaded. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      go: '// Generation failed for Go

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''The model is overloaded. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      ruby: "def minimum_abs_difference(arr)\n  arr.sort!\n  min_diff = arr[1] - arr[0]\n\
        \  (1...arr.length - 1).each do |i|\n    diff = arr[i+1] - arr[i]\n    min_diff\
        \ = diff if diff < min_diff\n  end\n  result = []\n  (0...arr.length - 1).each\
        \ do |i|\n    result << [arr[i], arr[i+1]] if arr[i+1] - arr[i] == min_diff\n\
        \  end\n  result\nend"
      scala: "object Solution {\n    def minimumAbsDifference(arr: Array[Int]): List[List[Int]]\
        \ = {\n        val sorted = arr.sorted\n        val pairs = sorted.zip(sorted.tail)\n\
        \        val minDiff = pairs.map(p => p._2 - p._1).min\n        pairs.filter(p\
        \ => p._2 - p._1 == minDiff).map(p => List(p._1, p._2)).toList\n    }\n}"
      rust: "impl Solution {\n    pub fn minimum_abs_difference(mut arr: Vec<i32>) ->\
        \ Vec<Vec<i32>> {\n        arr.sort();\n        let mut min_diff = i32::MAX;\n\
        \        for i in 0..arr.len() - 1 {\n            let diff = arr[i + 1] - arr[i];\n\
        \            if diff < min_diff {\n                min_diff = diff;\n      \
        \      }\n        }\n        let mut result = Vec::new();\n        for i in\
        \ 0..arr.len() - 1 {\n            if arr[i + 1] - arr[i] == min_diff {\n   \
        \             result.push(vec![arr[i], arr[i + 1]]);\n            }\n      \
        \  }\n        result\n    }\n}"
      racket: "(define/contract (minimum-abs-difference arr)\n  (-> (listof exact-integer?)\
        \ (listof (listof exact-integer?)))\n  (let* ([sorted (sort arr <)]\n      \
        \   [pairs (map list (drop-right sorted 1) (cdr sorted))]\n         [min-diff\
        \ (apply min (map (lambda (p) (- (cadr p) (car p))) pairs))])\n    (filter (lambda\
        \ (p) (= (- (cadr p) (car p)) min-diff)) pairs)))"
      erlang: "-spec minimum_abs_difference(Arr :: [integer()]) -> [[integer()]].\n\
        minimum_abs_difference(Arr) ->\n  Sorted = lists:sort(Arr),\n  Pairs = lists:zip(lists:sublist(Sorted,\
        \ length(Sorted) - 1), tl(Sorted)),\n  MinDiff = lists:min([B - A || {A, B}\
        \ <- Pairs]),\n  [[A, B] || {A, B} <- Pairs, B - A =:= MinDiff]."
      elixir: "defmodule Solution do\n  @spec minimum_abs_difference(arr :: [integer])\
        \ :: [[integer]]\n  def minimum_abs_difference(arr) do\n    sorted = Enum.sort(arr)\n\
        \    pairs = Enum.zip(sorted, tl(sorted))\n    min_diff = pairs\n      |> Enum.map(fn\
        \ {a, b} -> b - a end)\n      |> Enum.min()\n    pairs\n      |> Enum.filter(fn\
        \ {a, b} -> b - a == min_diff end)\n      |> Enum.map(fn {a, b} -> [a, b] end)\n\
        \  end\nend"
    approach: 'The algorithm begins by sorting the input array in ascending order. This
      sorting step is crucial because the minimum absolute difference between any two
      elements in the array must occur between two adjacent elements in the sorted sequence.
      By sorting first, we reduce the search space for the minimum difference from all
      possible pairs $O(n^2)$ to only adjacent pairs $O(n)$.


      After sorting, the algorithm performs a single pass to find the minimum difference
      between all consecutive elements. Once this minimum value is determined, a second
      pass iterates through the sorted array again, collecting all pairs whose difference
      matches the calculated minimum. Since we iterate through the sorted array from
      left to right, the collected pairs are naturally added to the result list in ascending
      order, satisfying the problem requirements.'
    time_complexity: O(n log n) where n is the length of the array. This complexity
      is dominated by the sorting step. The subsequent linear scans to find the minimum
      difference and collect the pairs take O(n) time.
    space_complexity: O(log n) to O(n) auxiliary space. This depends on the implementation
      of the sorting algorithm (e.g., Timsort in Python/Java or introsort in C++). The
      space used to store the output pairs is not usually counted as auxiliary space.
    elapsed_time: 358.03108954429626
    model: gemini-3-flash-preview
    generated_at: '2026-01-26 01:29:05 '
---

## Problem #1200: Minimum Absolute Difference

**Difficulty:** Easy

**Topics:** Array, Sorting

## Problem Description

<p>Given an array of <strong>distinct</strong> integers <code>arr</code>, find all pairs of elements with the minimum absolute difference of any two elements.</p>

<p>Return a list of pairs in ascending order(with respect to pairs), each pair <code>[a, b]</code> follows</p>

<ul>
	<li><code>a, b</code> are from <code>arr</code></li>
	<li><code>a &lt; b</code></li>
	<li><code>b - a</code> equals to the minimum absolute difference of any two elements in <code>arr</code></li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [4,2,1,3]
<strong>Output:</strong> [[1,2],[2,3],[3,4]]
<strong>Explanation: </strong>The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,3,6,10,15]
<strong>Output:</strong> [[1,3]]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [3,8,-10,23,19,-4,-14,27]
<strong>Output:</strong> [[-14,-10],[19,23],[23,27]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>6</sup> &lt;= arr[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## Hints

1. Find the minimum absolute difference between two elements in the array.

2. The minimum absolute difference must be a difference between two consecutive elements in the sorted array.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm begins by sorting the input array in ascending order. This sorting step is crucial because the minimum absolute difference between any two elements in the array must occur between two adjacent elements in the sorted sequence. By sorting first, we reduce the search space for the minimum difference from all possible pairs $O(n^2)$ to only adjacent pairs $O(n)$.

After sorting, the algorithm performs a single pass to find the minimum difference between all consecutive elements. Once this minimum value is determined, a second pass iterates through the sorted array again, collecting all pairs whose difference matches the calculated minimum. Since we iterate through the sorted array from left to right, the collected pairs are naturally added to the result list in ascending order, satisfying the problem requirements.

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
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        int minDiff = INT_MAX;
        int n = arr.size();
        for (int i = 0; i < n - 1; ++i) {
            minDiff = min(minDiff, arr[i + 1] - arr[i]);
        }
        vector<vector<int>> result;
        for (int i = 0; i < n - 1; ++i) {
            if (arr[i + 1] - arr[i] == minDiff) {
                result.push_back({arr[i], arr[i + 1]});
            }
        }
        return result;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        Arrays.sort(arr);
        int minDiff = Integer.MAX_VALUE;
        for (int i = 0; i < arr.length - 1; i++) {
            minDiff = Math.min(minDiff, arr[i + 1] - arr[i]);
        }
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i + 1] - arr[i] == minDiff) {
                List<Integer> pair = new ArrayList<>();
                pair.add(arr[i]);
                pair.add(arr[i + 1]);
                result.add(pair);
            }
        }
        return result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        min_diff = float('inf')
        for i in range(len(arr) - 1):
            diff = arr[i+1] - arr[i]
            if diff < min_diff:
                min_diff = diff

        result = []
        for i in range(len(arr) - 1):
            if arr[i+1] - arr[i] == min_diff:
                result.append([arr[i], arr[i+1]])
        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')
        for i in range(len(arr) - 1):
            min_diff = min(min_diff, arr[i + 1] - arr[i])

        return [[arr[i], arr[i + 1]] for i in range(len(arr) - 1) if arr[i + 1] - arr[i] == min_diff]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int** minimumAbsDifference(int* arr, int arrSize, int* returnSize, int** returnColumnSizes) {
    qsort(arr, arrSize, sizeof(int), compare);
    int minDiff = arr[1] - arr[0];
    for (int i = 1; i < arrSize - 1; i++) {
        int diff = arr[i + 1] - arr[i];
        if (diff < minDiff) minDiff = diff;
    }
    int count = 0;
    for (int i = 0; i < arrSize - 1; i++) {
        if (arr[i + 1] - arr[i] == minDiff) count++;
    }
    *returnSize = count;
    *returnColumnSizes = (int*)malloc(count * sizeof(int));
    int** result = (int**)malloc(count * sizeof(int*));
    int idx = 0;
    for (int i = 0; i < arrSize - 1; i++) {
        if (arr[i + 1] - arr[i] == minDiff) {
            result[idx] = (int*)malloc(2 * sizeof(int));
            result[idx][0] = arr[i];
            result[idx][1] = arr[i + 1];
            (*returnColumnSizes)[idx] = 2;
            idx++;
        }
    }
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public IList<IList<int>> MinimumAbsDifference(int[] arr) {
        Array.Sort(arr);
        int minDiff = int.MaxValue;
        for (int i = 0; i < arr.Length - 1; i++) {
            int diff = arr[i + 1] - arr[i];
            if (diff < minDiff) minDiff = diff;
        }
        IList<IList<int>> result = new List<IList<int>>();
        for (int i = 0; i < arr.Length - 1; i++) {
            if (arr[i + 1] - arr[i] == minDiff) {
                result.Add(new List<int> { arr[i], arr[i + 1] });
            }
        }
        return result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} arr
 * @return {number[][]}
 */
var minimumAbsDifference = function(arr) {
    arr.sort((a, b) => a - b);
    let minDiff = Infinity;
    for (let i = 0; i < arr.length - 1; i++) {
        minDiff = Math.min(minDiff, arr[i + 1] - arr[i]);
    }
    const result = [];
    for (let i = 0; i < arr.length - 1; i++) {
        if (arr[i + 1] - arr[i] === minDiff) {
            result.push([arr[i], arr[i + 1]]);
        }
    }
    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
// Generation failed for TypeScript
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'The model is overloaded. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
// Generation failed for PHP
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'The model is overloaded. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
// Generation failed for Swift
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'The model is overloaded. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
// Generation failed for Kotlin
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'The model is overloaded. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
// Generation failed for Dart
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'The model is overloaded. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
// Generation failed for Go
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'The model is overloaded. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def minimum_abs_difference(arr)
  arr.sort!
  min_diff = arr[1] - arr[0]
  (1...arr.length - 1).each do |i|
    diff = arr[i+1] - arr[i]
    min_diff = diff if diff < min_diff
  end
  result = []
  (0...arr.length - 1).each do |i|
    result << [arr[i], arr[i+1]] if arr[i+1] - arr[i] == min_diff
  end
  result
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minimumAbsDifference(arr: Array[Int]): List[List[Int]] = {
        val sorted = arr.sorted
        val pairs = sorted.zip(sorted.tail)
        val minDiff = pairs.map(p => p._2 - p._1).min
        pairs.filter(p => p._2 - p._1 == minDiff).map(p => List(p._1, p._2)).toList
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn minimum_abs_difference(mut arr: Vec<i32>) -> Vec<Vec<i32>> {
        arr.sort();
        let mut min_diff = i32::MAX;
        for i in 0..arr.len() - 1 {
            let diff = arr[i + 1] - arr[i];
            if diff < min_diff {
                min_diff = diff;
            }
        }
        let mut result = Vec::new();
        for i in 0..arr.len() - 1 {
            if arr[i + 1] - arr[i] == min_diff {
                result.push(vec![arr[i], arr[i + 1]]);
            }
        }
        result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (minimum-abs-difference arr)
  (-> (listof exact-integer?) (listof (listof exact-integer?)))
  (let* ([sorted (sort arr <)]
         [pairs (map list (drop-right sorted 1) (cdr sorted))]
         [min-diff (apply min (map (lambda (p) (- (cadr p) (car p))) pairs))])
    (filter (lambda (p) (= (- (cadr p) (car p)) min-diff)) pairs)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec minimum_abs_difference(Arr :: [integer()]) -> [[integer()]].
minimum_abs_difference(Arr) ->
  Sorted = lists:sort(Arr),
  Pairs = lists:zip(lists:sublist(Sorted, length(Sorted) - 1), tl(Sorted)),
  MinDiff = lists:min([B - A || {A, B} <- Pairs]),
  [[A, B] || {A, B} <- Pairs, B - A =:= MinDiff].
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_abs_difference(arr :: [integer]) :: [[integer]]
  def minimum_abs_difference(arr) do
    sorted = Enum.sort(arr)
    pairs = Enum.zip(sorted, tl(sorted))
    min_diff = pairs
      |> Enum.map(fn {a, b} -> b - a end)
      |> Enum.min()
    pairs
      |> Enum.filter(fn {a, b} -> b - a == min_diff end)
      |> Enum.map(fn {a, b} -> [a, b] end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n log n) where n is the length of the array. This complexity is dominated by the sorting step. The subsequent linear scans to find the minimum difference and collect the pairs take O(n) time.
- **Space Complexity:** O(log n) to O(n) auxiliary space. This depends on the implementation of the sorting algorithm (e.g., Timsort in Python/Java or introsort in C++). The space used to store the output pairs is not usually counted as auxiliary space.
