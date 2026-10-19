---
layout: post
title: "Find Target Indices After Sorting Array"
date: 2026-10-19 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Binary Search", "Sorting"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/find-target-indices-after-sorting-array/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> targetIndices(vector<int>& nums,\
        \ int target) {\n        int smaller = 0;\n        int count = 0;\n        for\
        \ (int num : nums) {\n            if (num < target) {\n                smaller++;\n\
        \            } else if (num == target) {\n                count++;\n       \
        \     }\n        }\n        vector<int> result;\n        for (int i = 0; i <\
        \ count; i++) {\n            result.push_back(smaller + i);\n        }\n   \
        \     return result;\n    }\n};"
      java: "import java.util.ArrayList;\nimport java.util.List;\n\nclass Solution {\n\
        \    public List<Integer> targetIndices(int[] nums, int target) {\n        int\
        \ smaller = 0;\n        int count = 0;\n        for (int num : nums) {\n   \
        \         if (num < target) {\n                smaller++;\n            } else\
        \ if (num == target) {\n                count++;\n            }\n        }\n\
        \        List<Integer> result = new ArrayList<>();\n        for (int i = 0;\
        \ i < count; i++) {\n            result.add(smaller + i);\n        }\n     \
        \   return result;\n    }\n}"
      python: "class Solution(object):\n    def targetIndices(self, nums, target):\n\
        \        \"\"\"\n        :type nums: List[int]\n        :type target: int\n\
        \        :rtype: List[int]\n        \"\"\"\n        smaller = 0\n        count\
        \ = 0\n        for num in nums:\n            if num < target:\n            \
        \    smaller += 1\n            elif num == target:\n                count +=\
        \ 1\n\n        result = []\n        for i in range(smaller, smaller + count):\n\
        \            result.append(i)\n        return result"
      python3: "class Solution:\n    def targetIndices(self, nums: list[int], target:\
        \ int) -> list[int]:\n        smaller = 0\n        count = 0\n        for num\
        \ in nums:\n            if num < target:\n                smaller += 1\n   \
        \         elif num == target:\n                count += 1\n\n        return\
        \ [i for i in range(smaller, smaller + count)]"
      c: "#include <stdlib.h>\n\n/**\n * Note: The returned array must be malloced,\
        \ assume caller calls free().\n */\nint* targetIndices(int* nums, int numsSize,\
        \ int target, int* returnSize) {\n    int smaller = 0;\n    int count = 0;\n\
        \    for (int i = 0; i < numsSize; i++) {\n        if (nums[i] < target) {\n\
        \            smaller++;\n        } else if (nums[i] == target) {\n         \
        \   count++;\n        }\n    }\n\n    *returnSize = count;\n    int* result\
        \ = (int*)malloc(count * sizeof(int));\n    for (int i = 0; i < count; i++)\
        \ {\n        result[i] = smaller + i;\n    }\n    return result;\n}"
      csharp: "using System.Collections.Generic;\n\npublic class Solution {\n    public\
        \ IList<int> TargetIndices(int[] nums, int target) {\n        int smaller =\
        \ 0;\n        int count = 0;\n        foreach (int num in nums) {\n        \
        \    if (num < target) {\n                smaller++;\n            } else if\
        \ (num == target) {\n                count++;\n            }\n        }\n\n\
        \        List<int> result = new List<int>();\n        for (int i = 0; i < count;\
        \ i++) {\n            result.Add(smaller + i);\n        }\n        return result;\n\
        \    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} target\n * @return\
        \ {number[]}\n */\nvar targetIndices = function(nums, target) {\n    let smaller\
        \ = 0;\n    let count = 0;\n    for (let num of nums) {\n        if (num < target)\
        \ {\n            smaller++;\n        } else if (num === target) {\n        \
        \    count++;\n        }\n    }\n\n    const result = [];\n    for (let i =\
        \ 0; i < count; i++) {\n        result.push(smaller + i);\n    }\n    return\
        \ result;\n};"
      typescript: "function targetIndices(nums: number[], target: number): number[]\
        \ {\n    nums.sort((a, b) => a - b);\n    const result: number[] = [];\n   \
        \ for (let i = 0; i < nums.length; i++) {\n        if (nums[i] === target) {\n\
        \            result.push(i);\n        }\n    }\n    return result;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer $target\n     * @return Integer[]\n     */\n    function targetIndices($nums,\
        \ $target) {\n        sort($nums);\n        $result = [];\n        foreach ($nums\
        \ as $index => $value) {\n            if ($value == $target) {\n           \
        \     $result[] = $index;\n            }\n        }\n        return $result;\n\
        \    }\n}"
      swift: "class Solution {\n    func targetIndices(_ nums: [Int], _ target: Int)\
        \ -> [Int] {\n        let sortedNums = nums.sorted()\n        var result = [Int]()\n\
        \        for i in 0..<sortedNums.count {\n            if sortedNums[i] == target\
        \ {\n                result.append(i)\n            }\n        }\n        return\
        \ result\n    }\n}"
      kotlin: "class Solution {\n    fun targetIndices(nums: IntArray, target: Int):\
        \ List<Int> {\n        nums.sort()\n        val result = mutableListOf<Int>()\n\
        \        for (i in nums.indices) {\n            if (nums[i] == target) {\n \
        \               result.add(i)\n            }\n        }\n        return result\n\
        \    }\n}"
      dart: "class Solution {\n  List<int> targetIndices(List<int> nums, int target)\
        \ {\n    nums.sort();\n    List<int> result = [];\n    for (int i = 0; i < nums.length;\
        \ i++) {\n      if (nums[i] == target) {\n        result.add(i);\n      }\n\
        \    }\n    return result;\n  }\n}"
      go: "import \"sort\"\n\nfunc targetIndices(nums []int, target int) []int {\n \
        \   sort.Ints(nums)\n    result := []int{}\n    for i, val := range nums {\n\
        \        if val == target {\n            result = append(result, i)\n      \
        \  }\n    }\n    return result\n}"
      ruby: "def target_indices(nums, target)\n  sorted_nums = nums.sort\n  result =\
        \ []\n  sorted_nums.each_with_index do |num, index|\n    result << index if\
        \ num == target\n  end\n  result\nend"
      scala: "object Solution {\n    def targetIndices(nums: Array[Int], target: Int):\
        \ List[Int] = {\n        val sortedNums = nums.sorted\n        sortedNums.zipWithIndex.filter\
        \ { case (num, index) => num == target }.map(_._2).toList\n    }\n}"
      rust: "impl Solution {\n    pub fn target_indices(nums: Vec<i32>, target: i32)\
        \ -> Vec<i32> {\n        let mut sorted_nums = nums;\n        sorted_nums.sort();\n\
        \        let mut result = Vec::new();\n        for (i, &num) in sorted_nums.iter().enumerate()\
        \ {\n            if num == target {\n                result.push(i as i32);\n\
        \            }\n        }\n        result\n    }\n}"
      racket: "(define/contract (target-indices nums target)\n  (-> (listof exact-integer?)\
        \ exact-integer? (listof exact-integer?))\n  (let ([sorted-nums (sort nums <)])\n\
        \    (for/list ([n sorted-nums]\n               [i (in-naturals)]\n        \
        \       #:when (= n target))\n      i)))"
      erlang: "-spec target_indices(Nums :: [integer()], Target :: integer()) -> [integer()].\n\
        target_indices(Nums, Target) ->\n  SortedNums = lists:sort(Nums),\n  IndexedNums\
        \ = lists:zip(lists:seq(0, length(SortedNums) - 1), SortedNums),\n  [Index ||\
        \ {Index, Num} <- IndexedNums, Num =:= Target]."
      elixir: "defmodule Solution do\n  @spec target_indices(nums :: [integer], target\
        \ :: integer) :: [integer]\n  def target_indices(nums, target) do\n    nums\n\
        \    |> Enum.sort()\n    |> Enum.with_index()\n    |> Enum.filter(fn {num, _index}\
        \ -> num == target end)\n    |> Enum.map(fn {_num, index} -> index end)\n  end\n\
        end"
    approach: 'To solve this problem efficiently without an explicit sort, we can utilize
      the properties of a sorted array by counting elements. In a non-decreasing sorted
      array, all elements smaller than a given target will occupy the initial indices.
      By iterating through the input array once, we count how many elements are strictly
      smaller than the target and how many elements are exactly equal to the target.
      The first occurrence of the target in a sorted version of the array will always
      start at the index equal to the count of elements smaller than it.


      Once the starting index and the frequency of the target are determined, we can
      generate the list of indices by starting from the calculated index and incrementing
      it for each occurrence of the target. This linear approach avoids the $O(n \log
      n)$ cost of sorting the entire array, which is particularly useful for larger
      inputs, although the current constraints are small. The resulting indices are
      naturally generated in increasing order, meeting the problem requirements.'
    time_complexity: O(n), where n is the length of the input array. We traverse the
      array once to count elements smaller than and equal to the target, and then run
      a simple loop to build the result list based on those counts.
    space_complexity: O(n) in the worst case, representing the space needed to store
      the list of target indices if all elements in the input array match the target.
      The auxiliary space used for counters is O(1).
    elapsed_time: 55.73088216781616
    model: gemini-3-flash-preview
    generated_at: '2026-10-19 02:39:31 '
---

## Problem #2089: Find Target Indices After Sorting Array

**Difficulty:** Easy

**Topics:** Array, Binary Search, Sorting

## Problem Description

<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> and a target element <code>target</code>.</p>

<p>A <strong>target index</strong> is an index <code>i</code> such that <code>nums[i] == target</code>.</p>

<p>Return <em>a list of the target indices of</em> <code>nums</code> after<em> sorting </em><code>nums</code><em> in <strong>non-decreasing</strong> order</em>. If there are no target indices, return <em>an <strong>empty</strong> list</em>. The returned list must be sorted in <strong>increasing</strong> order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,5,2,3], target = 2
<strong>Output:</strong> [1,2]
<strong>Explanation:</strong> After sorting, nums is [1,<u><strong>2</strong></u>,<u><strong>2</strong></u>,3,5].
The indices where nums[i] == 2 are 1 and 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,5,2,3], target = 3
<strong>Output:</strong> [3]
<strong>Explanation:</strong> After sorting, nums is [1,2,2,<u><strong>3</strong></u>,5].
The index where nums[i] == 3 is 3.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,5,2,3], target = 5
<strong>Output:</strong> [4]
<strong>Explanation:</strong> After sorting, nums is [1,2,2,3,<u><strong>5</strong></u>].
The index where nums[i] == 5 is 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i], target &lt;= 100</code></li>
</ul>


## Hints

1. Try "sorting" the array first.

2. Now find all indices in the array whose values are equal to target.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To solve this problem efficiently without an explicit sort, we can utilize the properties of a sorted array by counting elements. In a non-decreasing sorted array, all elements smaller than a given target will occupy the initial indices. By iterating through the input array once, we count how many elements are strictly smaller than the target and how many elements are exactly equal to the target. The first occurrence of the target in a sorted version of the array will always start at the index equal to the count of elements smaller than it.

Once the starting index and the frequency of the target are determined, we can generate the list of indices by starting from the calculated index and incrementing it for each occurrence of the target. This linear approach avoids the $O(n \log n)$ cost of sorting the entire array, which is particularly useful for larger inputs, although the current constraints are small. The resulting indices are naturally generated in increasing order, meeting the problem requirements.

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
    vector<int> targetIndices(vector<int>& nums, int target) {
        int smaller = 0;
        int count = 0;
        for (int num : nums) {
            if (num < target) {
                smaller++;
            } else if (num == target) {
                count++;
            }
        }
        vector<int> result;
        for (int i = 0; i < count; i++) {
            result.push_back(smaller + i);
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
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> targetIndices(int[] nums, int target) {
        int smaller = 0;
        int count = 0;
        for (int num : nums) {
            if (num < target) {
                smaller++;
            } else if (num == target) {
                count++;
            }
        }
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < count; i++) {
            result.add(smaller + i);
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
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        smaller = 0
        count = 0
        for num in nums:
            if num < target:
                smaller += 1
            elif num == target:
                count += 1

        result = []
        for i in range(smaller, smaller + count):
            result.append(i)
        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        smaller = 0
        count = 0
        for num in nums:
            if num < target:
                smaller += 1
            elif num == target:
                count += 1

        return [i for i in range(smaller, smaller + count)]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* targetIndices(int* nums, int numsSize, int target, int* returnSize) {
    int smaller = 0;
    int count = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] < target) {
            smaller++;
        } else if (nums[i] == target) {
            count++;
        }
    }

    *returnSize = count;
    int* result = (int*)malloc(count * sizeof(int));
    for (int i = 0; i < count; i++) {
        result[i] = smaller + i;
    }
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System.Collections.Generic;

public class Solution {
    public IList<int> TargetIndices(int[] nums, int target) {
        int smaller = 0;
        int count = 0;
        foreach (int num in nums) {
            if (num < target) {
                smaller++;
            } else if (num == target) {
                count++;
            }
        }

        List<int> result = new List<int>();
        for (int i = 0; i < count; i++) {
            result.Add(smaller + i);
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
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var targetIndices = function(nums, target) {
    let smaller = 0;
    let count = 0;
    for (let num of nums) {
        if (num < target) {
            smaller++;
        } else if (num === target) {
            count++;
        }
    }

    const result = [];
    for (let i = 0; i < count; i++) {
        result.push(smaller + i);
    }
    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function targetIndices(nums: number[], target: number): number[] {
    nums.sort((a, b) => a - b);
    const result: number[] = [];
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === target) {
            result.push(i);
        }
    }
    return result;
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
     * @return Integer[]
     */
    function targetIndices($nums, $target) {
        sort($nums);
        $result = [];
        foreach ($nums as $index => $value) {
            if ($value == $target) {
                $result[] = $index;
            }
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
    func targetIndices(_ nums: [Int], _ target: Int) -> [Int] {
        let sortedNums = nums.sorted()
        var result = [Int]()
        for i in 0..<sortedNums.count {
            if sortedNums[i] == target {
                result.append(i)
            }
        }
        return result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun targetIndices(nums: IntArray, target: Int): List<Int> {
        nums.sort()
        val result = mutableListOf<Int>()
        for (i in nums.indices) {
            if (nums[i] == target) {
                result.add(i)
            }
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
  List<int> targetIndices(List<int> nums, int target) {
    nums.sort();
    List<int> result = [];
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] == target) {
        result.add(i);
      }
    }
    return result;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "sort"

func targetIndices(nums []int, target int) []int {
    sort.Ints(nums)
    result := []int{}
    for i, val := range nums {
        if val == target {
            result = append(result, i)
        }
    }
    return result
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def target_indices(nums, target)
  sorted_nums = nums.sort
  result = []
  sorted_nums.each_with_index do |num, index|
    result << index if num == target
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
    def targetIndices(nums: Array[Int], target: Int): List[Int] = {
        val sortedNums = nums.sorted
        sortedNums.zipWithIndex.filter { case (num, index) => num == target }.map(_._2).toList
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn target_indices(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut sorted_nums = nums;
        sorted_nums.sort();
        let mut result = Vec::new();
        for (i, &num) in sorted_nums.iter().enumerate() {
            if num == target {
                result.push(i as i32);
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
(define/contract (target-indices nums target)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let ([sorted-nums (sort nums <)])
    (for/list ([n sorted-nums]
               [i (in-naturals)]
               #:when (= n target))
      i)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec target_indices(Nums :: [integer()], Target :: integer()) -> [integer()].
target_indices(Nums, Target) ->
  SortedNums = lists:sort(Nums),
  IndexedNums = lists:zip(lists:seq(0, length(SortedNums) - 1), SortedNums),
  [Index || {Index, Num} <- IndexedNums, Num =:= Target].
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec target_indices(nums :: [integer], target :: integer) :: [integer]
  def target_indices(nums, target) do
    nums
    |> Enum.sort()
    |> Enum.with_index()
    |> Enum.filter(fn {num, _index} -> num == target end)
    |> Enum.map(fn {_num, index} -> index end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n), where n is the length of the input array. We traverse the array once to count elements smaller than and equal to the target, and then run a simple loop to build the result list based on those counts.
- **Space Complexity:** O(n) in the worst case, representing the space needed to store the list of target indices if all elements in the input array match the target. The auxiliary space used for counters is O(1).
