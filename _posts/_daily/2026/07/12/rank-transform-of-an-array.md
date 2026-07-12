---
layout: post
title: "Rank Transform of an Array"
date: 2026-07-12 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Hash Table", "Sorting"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/rank-transform-of-an-array/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> arrayRankTransform(vector<int>&\
        \ arr) {\n        if (arr.empty()) return {};\n        vector<int> sortedArr\
        \ = arr;\n        sort(sortedArr.begin(), sortedArr.end());\n\n        unordered_map<int,\
        \ int> rankMap;\n        int rank = 1;\n        for (int num : sortedArr) {\n\
        \            if (rankMap.find(num) == rankMap.end()) {\n                rankMap[num]\
        \ = rank++;\n            }\n        }\n\n        vector<int> result;\n     \
        \   result.reserve(arr.size());\n        for (int num : arr) {\n           \
        \ result.push_back(rankMap[num]);\n        }\n        return result;\n    }\n\
        };"
      java: "class Solution {\n    public int[] arrayRankTransform(int[] arr) {\n  \
        \      int[] sortedArr = arr.clone();\n        Arrays.sort(sortedArr);\n\n \
        \       Map<Integer, Integer> rankMap = new HashMap<>();\n        int rank =\
        \ 1;\n        for (int num : sortedArr) {\n            if (!rankMap.containsKey(num))\
        \ {\n                rankMap.put(num, rank++);\n            }\n        }\n\n\
        \        int[] result = new int[arr.length];\n        for (int i = 0; i < arr.length;\
        \ i++) {\n            result[i] = rankMap.get(arr[i]);\n        }\n        return\
        \ result;\n    }\n}"
      python: "class Solution(object):\n    def arrayRankTransform(self, arr):\n   \
        \     \"\"\"\n        :type arr: List[int]\n        :rtype: List[int]\n    \
        \    \"\"\"\n        sorted_unique = sorted(list(set(arr)))\n        rank_map\
        \ = {val: i + 1 for i, val in enumerate(sorted_unique)}\n        return [rank_map[x]\
        \ for x in arr]"
      python3: "class Solution:\n    def arrayRankTransform(self, arr: List[int]) ->\
        \ List[int]:\n        sorted_unique = sorted(list(set(arr)))\n        rank_map\
        \ = {val: i + 1 for i, val in enumerate(sorted_unique)}\n        return [rank_map[x]\
        \ for x in arr]"
      c: "#include <stdlib.h>\n\nint compare(const void* a, const void* b) {\n    int\
        \ arg1 = *(const int*)a;\n    int arg2 = *(const int*)b;\n    if (arg1 < arg2)\
        \ return -1;\n    if (arg1 > arg2) return 1;\n    return 0;\n}\n\n/**\n * Note:\
        \ The returned array must be malloced, assume caller calls free().\n */\nint*\
        \ arrayRankTransform(int* arr, int arrSize, int* returnSize) {\n    *returnSize\
        \ = arrSize;\n    if (arrSize == 0) return NULL;\n\n    int* sortedArr = (int*)malloc(arrSize\
        \ * sizeof(int));\n    for (int i = 0; i < arrSize; i++) sortedArr[i] = arr[i];\n\
        \n    qsort(sortedArr, arrSize, sizeof(int), compare);\n\n    int uniqueSize\
        \ = 0;\n    if (arrSize > 0) {\n        uniqueSize = 1;\n        for (int i\
        \ = 1; i < arrSize; i++) {\n            if (sortedArr[i] != sortedArr[i - 1])\
        \ {\n                sortedArr[uniqueSize++] = sortedArr[i];\n            }\n\
        \        }\n    }\n\n    int* result = (int*)malloc(arrSize * sizeof(int));\n\
        \    for (int i = 0; i < arrSize; i++) {\n        int low = 0, high = uniqueSize\
        \ - 1;\n        while (low <= high) {\n            int mid = low + (high - low)\
        \ / 2;\n            if (sortedArr[mid] == arr[i]) {\n                result[i]\
        \ = mid + 1;\n                break;\n            } else if (sortedArr[mid]\
        \ < arr[i]) {\n                low = mid + 1;\n            } else {\n      \
        \          high = mid - 1;\n            }\n        }\n    }\n\n    free(sortedArr);\n\
        \    return result;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int[] ArrayRankTransform(int[] arr) {\n        int[] sortedArr\
        \ = (int[])arr.Clone();\n        Array.Sort(sortedArr);\n\n        Dictionary<int,\
        \ int> rankMap = new Dictionary<int, int>();\n        int rank = 1;\n      \
        \  foreach (int num in sortedArr) {\n            if (!rankMap.ContainsKey(num))\
        \ {\n                rankMap[num] = rank++;\n            }\n        }\n\n  \
        \      int[] result = new int[arr.Length];\n        for (int i = 0; i < arr.Length;\
        \ i++) {\n            result[i] = rankMap[arr[i]];\n        }\n        return\
        \ result;\n    }\n}"
      javascript: "/**\n * @param {number[]} arr\n * @return {number[]}\n */\nvar arrayRankTransform\
        \ = function(arr) {\n    const sortedUnique = [...new Set(arr)].sort((a, b)\
        \ => a - b);\n    const rankMap = new Map();\n    for (let i = 0; i < sortedUnique.length;\
        \ i++) {\n        rankMap.set(sortedUnique[i], i + 1);\n    }\n\n    return\
        \ arr.map(num => rankMap.get(num));\n};"
      typescript: "function arrayRankTransform(arr: number[]): number[] {\n    const\
        \ sortedUnique = Array.from(new Set(arr)).sort((a, b) => a - b);\n    const\
        \ rankMap = new Map<number, number>();\n    for (let i = 0; i < sortedUnique.length;\
        \ i++) {\n        rankMap.set(sortedUnique[i], i + 1);\n    }\n    return arr.map(num\
        \ => rankMap.get(num)!);\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $arr\n     * @return\
        \ Integer[]\n     */\n    function arrayRankTransform($arr) {\n        $sorted\
        \ = $arr;\n        sort($sorted);\n        $rankMap = [];\n        $rank = 1;\n\
        \        foreach ($sorted as $num) {\n            if (!isset($rankMap[$num]))\
        \ {\n                $rankMap[$num] = $rank++;\n            }\n        }\n \
        \       $result = [];\n        foreach ($arr as $num) {\n            $result[]\
        \ = $rankMap[$num];\n        }\n        return $result;\n    }\n}"
      swift: "class Solution {\n    func arrayRankTransform(_ arr: [Int]) -> [Int] {\n\
        \        let sortedUnique = Array(Set(arr)).sorted()\n        var rankMap =\
        \ [Int: Int]()\n        for (index, value) in sortedUnique.enumerated() {\n\
        \            rankMap[value] = index + 1\n        }\n        return arr.map {\
        \ rankMap[$0]! }\n    }\n}"
      kotlin: "class Solution {\n    fun arrayRankTransform(arr: IntArray): IntArray\
        \ {\n        val sortedUnique = arr.distinct().sorted()\n        val rankMap\
        \ = mutableMapOf<Int, Int>()\n        for ((index, value) in sortedUnique.withIndex())\
        \ {\n            rankMap[value] = index + 1\n        }\n        val result =\
        \ IntArray(arr.size)\n        for (i in arr.indices) {\n            result[i]\
        \ = rankMap[arr[i]]!!\n        }\n        return result\n    }\n}"
      dart: "class Solution {\n  List<int> arrayRankTransform(List<int> arr) {\n   \
        \ List<int> sortedUnique = arr.toSet().toList()..sort();\n    Map<int, int>\
        \ rankMap = {};\n    for (int i = 0; i < sortedUnique.length; i++) {\n     \
        \ rankMap[sortedUnique[i]] = i + 1;\n    }\n    return arr.map((e) => rankMap[e]!).toList();\n\
        \  }\n}"
      go: "import \"sort\"\n\nfunc arrayRankTransform(arr []int) []int {\n    n := len(arr)\n\
        \    sorted := make([]int, n)\n    copy(sorted, arr)\n    sort.Ints(sorted)\n\
        \n    rankMap := make(map[int]int)\n    rank := 1\n    for _, val := range sorted\
        \ {\n        if _, exists := rankMap[val]; !exists {\n            rankMap[val]\
        \ = rank\n            rank++\n        }\n    }\n\n    result := make([]int,\
        \ n)\n    for i, val := range arr {\n        result[i] = rankMap[val]\n    }\n\
        \    return result\n}"
      ruby: "def array_rank_transform(arr)\n  sorted_unique = arr.uniq.sort\n  rank_map\
        \ = {}\n  sorted_unique.each_with_index do |val, idx|\n    rank_map[val] = idx\
        \ + 1\n  end\n  arr.map { |val| rank_map[val] }\nend"
      scala: "object Solution {\n    def arrayRankTransform(arr: Array[Int]): Array[Int]\
        \ = {\n        val sortedUnique = arr.distinct.sorted\n        val rankMap =\
        \ sortedUnique.zipWithIndex.map { case (v, i) => (v, i + 1) }.toMap\n      \
        \  arr.map(rankMap)\n    }\n}"
      rust: "use std::collections::HashMap;\n\nimpl Solution {\n    pub fn array_rank_transform(arr:\
        \ Vec<i32>) -> Vec<i32> {\n        let mut sorted = arr.clone();\n        sorted.sort_unstable();\n\
        \        sorted.dedup();\n        let mut rank_map = HashMap::with_capacity(sorted.len());\n\
        \        for (i, &val) in sorted.iter().enumerate() {\n            rank_map.insert(val,\
        \ (i + 1) as i32);\n        }\n        arr.into_iter().map(|x| *rank_map.get(&x).unwrap()).collect()\n\
        \    }\n}"
      racket: "(define/contract (array-rank-transform arr)\n  (-> (listof exact-integer?)\
        \ (listof exact-integer?))\n  (let* ([sorted (sort (remove-duplicates arr) <)]\n\
        \         [rank-hash (make-hash)])\n    (for ([val sorted] [i (in-naturals 1)])\n\
        \      (hash-set! rank-hash val i))\n    (map (lambda (x) (hash-ref rank-hash\
        \ x)) arr)))"
      erlang: "array_rank_transform(Arr) ->\n  Sorted = lists:usort(Arr),\n  RankMap\
        \ = maps:from_list(lists:zip(Sorted, lists:seq(1, length(Sorted)))),\n  [maps:get(X,\
        \ RankMap) || X <- Arr]."
      elixir: "defmodule Solution do\n  @spec array_rank_transform(arr :: [integer])\
        \ :: [integer]\n  def array_rank_transform(arr) do\n    ranks = arr\n    |>\
        \ Enum.uniq()\n    |> Enum.sort()\n    |> Enum.with_index(1)\n    |> Map.new()\n\
        \n    Enum.map(arr, fn x -> Map.get(ranks, x) end)\n  end\nend"
    approach: 'The algorithm works by first determining the relative order of the unique
      elements in the input array. We create a copy of the original array and sort it.
      Sorting ensures that we can assign ranks in ascending order based on the values.
      We then iterate through the sorted list, maintaining a rank counter that starts
      at 1 and increments only when a new unique value is encountered. A hash map or
      dictionary is used to store the mapping from each unique value to its calculated
      rank.


      After the mapping is complete, we iterate through the original array one last
      time. For each element, we retrieve its rank from the hash map and store it in
      the result array. This approach naturally handles duplicates by mapping them to
      the same rank and ensures that ranks are consecutive integers starting from 1,
      fulfilling all the problem requirements efficiently.'
    time_complexity: O(N log N), where N is the length of the input array. This complexity
      is dominated by the sorting step. Building the unique rank map and the final pass
      to transform the array both take linear time, O(N).
    space_complexity: O(N), where N is the length of the input array. We require extra
      space to store a copy of the array for sorting, a hash map to store the ranks
      of unique elements, and the final output array.
    elapsed_time: 222.23695731163025
    model: gemini-3-flash-preview
    generated_at: '2026-07-12 02:03:19 '
---

## Problem #1331: Rank Transform of an Array

**Difficulty:** Easy

**Topics:** Array, Hash Table, Sorting

## Problem Description

<p>Given an array of integers&nbsp;<code>arr</code>, replace each element with its rank.</p>

<p>The rank represents how large the element is. The rank has the following rules:</p>

<ul>
	<li>Rank is an integer starting from 1.</li>
	<li>The larger the element, the larger the rank. If two elements are equal, their rank must be the same.</li>
	<li>Rank should be as small as possible.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [40,10,20,30]
<strong>Output:</strong> [4,1,2,3]
<strong>Explanation</strong>: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [100,100,100]
<strong>Output:</strong> [1,1,1]
<strong>Explanation</strong>: Same elements share the same rank.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [37,12,28,9,100,56,80,5,12]
<strong>Output:</strong> [5,3,4,2,8,6,7,1,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= arr[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. Use a temporary array to copy the array and sort it.

2. The rank of each element is the number of unique elements smaller than it in the sorted array plus one.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm works by first determining the relative order of the unique elements in the input array. We create a copy of the original array and sort it. Sorting ensures that we can assign ranks in ascending order based on the values. We then iterate through the sorted list, maintaining a rank counter that starts at 1 and increments only when a new unique value is encountered. A hash map or dictionary is used to store the mapping from each unique value to its calculated rank.

After the mapping is complete, we iterate through the original array one last time. For each element, we retrieve its rank from the hash map and store it in the result array. This approach naturally handles duplicates by mapping them to the same rank and ensures that ranks are consecutive integers starting from 1, fulfilling all the problem requirements efficiently.

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
    vector<int> arrayRankTransform(vector<int>& arr) {
        if (arr.empty()) return {};
        vector<int> sortedArr = arr;
        sort(sortedArr.begin(), sortedArr.end());

        unordered_map<int, int> rankMap;
        int rank = 1;
        for (int num : sortedArr) {
            if (rankMap.find(num) == rankMap.end()) {
                rankMap[num] = rank++;
            }
        }

        vector<int> result;
        result.reserve(arr.size());
        for (int num : arr) {
            result.push_back(rankMap[num]);
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
    public int[] arrayRankTransform(int[] arr) {
        int[] sortedArr = arr.clone();
        Arrays.sort(sortedArr);

        Map<Integer, Integer> rankMap = new HashMap<>();
        int rank = 1;
        for (int num : sortedArr) {
            if (!rankMap.containsKey(num)) {
                rankMap.put(num, rank++);
            }
        }

        int[] result = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            result[i] = rankMap.get(arr[i]);
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
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        sorted_unique = sorted(list(set(arr)))
        rank_map = {val: i + 1 for i, val in enumerate(sorted_unique)}
        return [rank_map[x] for x in arr]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_unique = sorted(list(set(arr)))
        rank_map = {val: i + 1 for i, val in enumerate(sorted_unique)}
        return [rank_map[x] for x in arr]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

int compare(const void* a, const void* b) {
    int arg1 = *(const int*)a;
    int arg2 = *(const int*)b;
    if (arg1 < arg2) return -1;
    if (arg1 > arg2) return 1;
    return 0;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* arrayRankTransform(int* arr, int arrSize, int* returnSize) {
    *returnSize = arrSize;
    if (arrSize == 0) return NULL;

    int* sortedArr = (int*)malloc(arrSize * sizeof(int));
    for (int i = 0; i < arrSize; i++) sortedArr[i] = arr[i];

    qsort(sortedArr, arrSize, sizeof(int), compare);

    int uniqueSize = 0;
    if (arrSize > 0) {
        uniqueSize = 1;
        for (int i = 1; i < arrSize; i++) {
            if (sortedArr[i] != sortedArr[i - 1]) {
                sortedArr[uniqueSize++] = sortedArr[i];
            }
        }
    }

    int* result = (int*)malloc(arrSize * sizeof(int));
    for (int i = 0; i < arrSize; i++) {
        int low = 0, high = uniqueSize - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (sortedArr[mid] == arr[i]) {
                result[i] = mid + 1;
                break;
            } else if (sortedArr[mid] < arr[i]) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
    }

    free(sortedArr);
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Collections.Generic;

public class Solution {
    public int[] ArrayRankTransform(int[] arr) {
        int[] sortedArr = (int[])arr.Clone();
        Array.Sort(sortedArr);

        Dictionary<int, int> rankMap = new Dictionary<int, int>();
        int rank = 1;
        foreach (int num in sortedArr) {
            if (!rankMap.ContainsKey(num)) {
                rankMap[num] = rank++;
            }
        }

        int[] result = new int[arr.Length];
        for (int i = 0; i < arr.Length; i++) {
            result[i] = rankMap[arr[i]];
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
 * @return {number[]}
 */
var arrayRankTransform = function(arr) {
    const sortedUnique = [...new Set(arr)].sort((a, b) => a - b);
    const rankMap = new Map();
    for (let i = 0; i < sortedUnique.length; i++) {
        rankMap.set(sortedUnique[i], i + 1);
    }

    return arr.map(num => rankMap.get(num));
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function arrayRankTransform(arr: number[]): number[] {
    const sortedUnique = Array.from(new Set(arr)).sort((a, b) => a - b);
    const rankMap = new Map<number, number>();
    for (let i = 0; i < sortedUnique.length; i++) {
        rankMap.set(sortedUnique[i], i + 1);
    }
    return arr.map(num => rankMap.get(num)!);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer[]
     */
    function arrayRankTransform($arr) {
        $sorted = $arr;
        sort($sorted);
        $rankMap = [];
        $rank = 1;
        foreach ($sorted as $num) {
            if (!isset($rankMap[$num])) {
                $rankMap[$num] = $rank++;
            }
        }
        $result = [];
        foreach ($arr as $num) {
            $result[] = $rankMap[$num];
        }
        return $result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func arrayRankTransform(_ arr: [Int]) -> [Int] {
        let sortedUnique = Array(Set(arr)).sorted()
        var rankMap = [Int: Int]()
        for (index, value) in sortedUnique.enumerated() {
            rankMap[value] = index + 1
        }
        return arr.map { rankMap[$0]! }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun arrayRankTransform(arr: IntArray): IntArray {
        val sortedUnique = arr.distinct().sorted()
        val rankMap = mutableMapOf<Int, Int>()
        for ((index, value) in sortedUnique.withIndex()) {
            rankMap[value] = index + 1
        }
        val result = IntArray(arr.size)
        for (i in arr.indices) {
            result[i] = rankMap[arr[i]]!!
        }
        return result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<int> arrayRankTransform(List<int> arr) {
    List<int> sortedUnique = arr.toSet().toList()..sort();
    Map<int, int> rankMap = {};
    for (int i = 0; i < sortedUnique.length; i++) {
      rankMap[sortedUnique[i]] = i + 1;
    }
    return arr.map((e) => rankMap[e]!).toList();
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "sort"

func arrayRankTransform(arr []int) []int {
    n := len(arr)
    sorted := make([]int, n)
    copy(sorted, arr)
    sort.Ints(sorted)

    rankMap := make(map[int]int)
    rank := 1
    for _, val := range sorted {
        if _, exists := rankMap[val]; !exists {
            rankMap[val] = rank
            rank++
        }
    }

    result := make([]int, n)
    for i, val := range arr {
        result[i] = rankMap[val]
    }
    return result
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def array_rank_transform(arr)
  sorted_unique = arr.uniq.sort
  rank_map = {}
  sorted_unique.each_with_index do |val, idx|
    rank_map[val] = idx + 1
  end
  arr.map { |val| rank_map[val] }
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def arrayRankTransform(arr: Array[Int]): Array[Int] = {
        val sortedUnique = arr.distinct.sorted
        val rankMap = sortedUnique.zipWithIndex.map { case (v, i) => (v, i + 1) }.toMap
        arr.map(rankMap)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::HashMap;

impl Solution {
    pub fn array_rank_transform(arr: Vec<i32>) -> Vec<i32> {
        let mut sorted = arr.clone();
        sorted.sort_unstable();
        sorted.dedup();
        let mut rank_map = HashMap::with_capacity(sorted.len());
        for (i, &val) in sorted.iter().enumerate() {
            rank_map.insert(val, (i + 1) as i32);
        }
        arr.into_iter().map(|x| *rank_map.get(&x).unwrap()).collect()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (array-rank-transform arr)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ([sorted (sort (remove-duplicates arr) <)]
         [rank-hash (make-hash)])
    (for ([val sorted] [i (in-naturals 1)])
      (hash-set! rank-hash val i))
    (map (lambda (x) (hash-ref rank-hash x)) arr)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
array_rank_transform(Arr) ->
  Sorted = lists:usort(Arr),
  RankMap = maps:from_list(lists:zip(Sorted, lists:seq(1, length(Sorted)))),
  [maps:get(X, RankMap) || X <- Arr].
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec array_rank_transform(arr :: [integer]) :: [integer]
  def array_rank_transform(arr) do
    ranks = arr
    |> Enum.uniq()
    |> Enum.sort()
    |> Enum.with_index(1)
    |> Map.new()

    Enum.map(arr, fn x -> Map.get(ranks, x) end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N log N), where N is the length of the input array. This complexity is dominated by the sorting step. Building the unique rank map and the final pass to transform the array both take linear time, O(N).
- **Space Complexity:** O(N), where N is the length of the input array. We require extra space to store a copy of the array for sorting, a hash map to store the ranks of unique elements, and the final output array.
