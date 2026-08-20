---
layout: post
title: "Distribute Elements Into Two Arrays I"
date: 2026-08-20 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Simulation"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/distribute-elements-into-two-arrays-i/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> resultArray(vector<int>& nums)\
        \ {\n        int n = nums.size();\n        vector<int> arr1, arr2;\n       \
        \ arr1.push_back(nums[0]);\n        arr2.push_back(nums[1]);\n        for (int\
        \ i = 2; i < n; ++i) {\n            if (arr1.back() > arr2.back()) {\n     \
        \           arr1.push_back(nums[i]);\n            } else {\n               \
        \ arr2.push_back(nums[i]);\n            }\n        }\n        arr1.insert(arr1.end(),\
        \ arr2.begin(), arr2.end());\n        return arr1;\n    }\n};"
      java: "class Solution {\n    public int[] resultArray(int[] nums) {\n        int\
        \ n = nums.length;\n        int[] arr1 = new int[n];\n        int[] arr2 = new\
        \ int[n];\n        int size1 = 0, size2 = 0;\n        arr1[size1++] = nums[0];\n\
        \        arr2[size2++] = nums[1];\n        for (int i = 2; i < n; i++) {\n \
        \           if (arr1[size1 - 1] > arr2[size2 - 1]) {\n                arr1[size1++]\
        \ = nums[i];\n            } else {\n                arr2[size2++] = nums[i];\n\
        \            }\n        }\n        int[] result = new int[n];\n        int k\
        \ = 0;\n        for (int i = 0; i < size1; i++) result[k++] = arr1[i];\n   \
        \     for (int i = 0; i < size2; i++) result[k++] = arr2[i];\n        return\
        \ result;\n    }\n}"
      python: "class Solution(object):\n    def resultArray(self, nums):\n        \"\
        \"\"\n        :type nums: List[int]\n        :rtype: List[int]\n        \"\"\
        \"\n        arr1 = [nums[0]]\n        arr2 = [nums[1]]\n        for i in range(2,\
        \ len(nums)):\n            if arr1[-1] > arr2[-1]:\n                arr1.append(nums[i])\n\
        \            else:\n                arr2.append(nums[i])\n        return arr1\
        \ + arr2"
      python3: "class Solution:\n    def resultArray(self, nums: List[int]) -> List[int]:\n\
        \        arr1 = [nums[0]]\n        arr2 = [nums[1]]\n        for i in range(2,\
        \ len(nums)):\n            if arr1[-1] > arr2[-1]:\n                arr1.append(nums[i])\n\
        \            else:\n                arr2.append(nums[i])\n        return arr1\
        \ + arr2"
      c: "/**\n * Note: The returned array must be malloced, assume caller calls free().\n\
        \ */\nint* resultArray(int* nums, int numsSize, int* returnSize) {\n    int*\
        \ arr1 = (int*)malloc(numsSize * sizeof(int));\n    int* arr2 = (int*)malloc(numsSize\
        \ * sizeof(int));\n    int size1 = 0, size2 = 0;\n    arr1[size1++] = nums[0];\n\
        \    arr2[size2++] = nums[1];\n    for (int i = 2; i < numsSize; i++) {\n  \
        \      if (arr1[size1 - 1] > arr2[size2 - 1]) {\n            arr1[size1++] =\
        \ nums[i];\n        } else {\n            arr2[size2++] = nums[i];\n       \
        \ }\n    }\n    int* result = (int*)malloc(numsSize * sizeof(int));\n    int\
        \ k = 0;\n    for (int i = 0; i < size1; i++) result[k++] = arr1[i];\n    for\
        \ (int i = 0; i < size2; i++) result[k++] = arr2[i];\n    free(arr1);\n    free(arr2);\n\
        \    *returnSize = numsSize;\n    return result;\n}"
      csharp: "using System.Collections.Generic;\n\npublic class Solution {\n    public\
        \ int[] ResultArray(int[] nums) {\n        List<int> arr1 = new List<int>();\n\
        \        List<int> arr2 = new List<int>();\n        arr1.Add(nums[0]);\n   \
        \     arr2.Add(nums[1]);\n        for (int i = 2; i < nums.Length; i++) {\n\
        \            if (arr1[arr1.Count - 1] > arr2[arr2.Count - 1]) {\n          \
        \      arr1.Add(nums[i]);\n            } else {\n                arr2.Add(nums[i]);\n\
        \            }\n        }\n        arr1.AddRange(arr2);\n        return arr1.ToArray();\n\
        \    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number[]}\n */\nvar resultArray\
        \ = function(nums) {\n    let arr1 = [nums[0]];\n    let arr2 = [nums[1]];\n\
        \    for (let i = 2; i < nums.length; i++) {\n        if (arr1[arr1.length -\
        \ 1] > arr2[arr2.length - 1]) {\n            arr1.push(nums[i]);\n        }\
        \ else {\n            arr2.push(nums[i]);\n        }\n    }\n    return arr1.concat(arr2);\n\
        };"
      typescript: "function resultArray(nums: number[]): number[] {\n    let arr1: number[]\
        \ = [nums[0]];\n    let arr2: number[] = [nums[1]];\n    for (let i = 2; i <\
        \ nums.length; i++) {\n        if (arr1[arr1.length - 1] > arr2[arr2.length\
        \ - 1]) {\n            arr1.push(nums[i]);\n        } else {\n            arr2.push(nums[i]);\n\
        \        }\n    }\n    return arr1.concat(arr2);\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer[]\n     */\n    function resultArray($nums) {\n        $arr1 = [$nums[0]];\n\
        \        $arr2 = [$nums[1]];\n        $n = count($nums);\n        for ($i =\
        \ 2; $i < $n; $i++) {\n            if ($arr1[count($arr1) - 1] > $arr2[count($arr2)\
        \ - 1]) {\n                $arr1[] = $nums[$i];\n            } else {\n    \
        \            $arr2[] = $nums[$i];\n            }\n        }\n        return\
        \ array_merge($arr1, $arr2);\n    }\n}"
      swift: "class Solution {\n    func resultArray(_ nums: [Int]) -> [Int] {\n   \
        \     var arr1: [Int] = [nums[0]]\n        var arr2: [Int] = [nums[1]]\n   \
        \     for i in 2..<nums.count {\n            if arr1.last! > arr2.last! {\n\
        \                arr1.append(nums[i])\n            } else {\n              \
        \  arr2.append(nums[i])\n            }\n        }\n        return arr1 + arr2\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun resultArray(nums: IntArray): IntArray {\n \
        \       val arr1 = mutableListOf<Int>(nums[0])\n        val arr2 = mutableListOf<Int>(nums[1])\n\
        \        for (i in 2 until nums.size) {\n            if (arr1.last() > arr2.last())\
        \ {\n                arr1.add(nums[i])\n            } else {\n             \
        \   arr2.add(nums[i])\n            }\n        }\n        val result = IntArray(nums.size)\n\
        \        var idx = 0\n        for (x in arr1) result[idx++] = x\n        for\
        \ (x in arr2) result[idx++] = x\n        return result\n    }\n}"
      dart: "class Solution {\n  List<int> resultArray(List<int> nums) {\n    List<int>\
        \ arr1 = [nums[0]];\n    List<int> arr2 = [nums[1]];\n    for (int i = 2; i\
        \ < nums.length; i++) {\n      if (arr1.last > arr2.last) {\n        arr1.add(nums[i]);\n\
        \      } else {\n        arr2.add(nums[i]);\n      }\n    }\n    return [...arr1,\
        \ ...arr2];\n  }\n}"
      go: "func resultArray(nums []int) []int {\n    arr1 := []int{nums[0]}\n    arr2\
        \ := []int{nums[1]}\n    for i := 2; i < len(nums); i++ {\n        if arr1[len(arr1)-1]\
        \ > arr2[len(arr2)-1] {\n            arr1 = append(arr1, nums[i])\n        }\
        \ else {\n            arr2 = append(arr2, nums[i])\n        }\n    }\n    return\
        \ append(arr1, arr2...)\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer[]}\ndef result_array(nums)\n\
        \  arr1 = [nums[0]]\n  arr2 = [nums[1]]\n  (2...nums.length).each do |i|\n \
        \   if arr1.last > arr2.last\n      arr1 << nums[i]\n    else\n      arr2 <<\
        \ nums[i]\n    end\n  end\n  arr1 + arr2\nend"
      scala: "import scala.collection.mutable.ArrayBuffer\n\nobject Solution {\n   \
        \ def resultArray(nums: Array[Int]): Array[Int] = {\n        val arr1 = ArrayBuffer[Int](nums(0))\n\
        \        val arr2 = ArrayBuffer[Int](nums(1))\n        for (i <- 2 until nums.length)\
        \ {\n            if (arr1.last > arr2.last) {\n                arr1 += nums(i)\n\
        \            } else {\n                arr2 += nums(i)\n            }\n    \
        \    }\n        (arr1 ++ arr2).toArray\n    }\n}"
      rust: "impl Solution {\n    pub fn result_array(nums: Vec<i32>) -> Vec<i32> {\n\
        \        let mut arr1 = vec![nums[0]];\n        let mut arr2 = vec![nums[1]];\n\
        \        for i in 2..nums.len() {\n            if arr1.last().unwrap() > arr2.last().unwrap()\
        \ {\n                arr1.push(nums[i]);\n            } else {\n           \
        \     arr2.push(nums[i]);\n            }\n        }\n        arr1.extend(arr2);\n\
        \        arr1\n    }\n}"
      racket: "(define/contract (result-array nums)\n  (-> (listof exact-integer?) (listof\
        \ exact-integer?))\n  (let loop ([rem (cddr nums)]\n             [a1 (list (car\
        \ nums))]\n             [a2 (list (cadr nums))])\n    (if (null? rem)\n    \
        \    (append (reverse a1) (reverse a2))\n        (if (> (car a1) (car a2))\n\
        \            (loop (cdr rem) (cons (car rem) a1) a2)\n            (loop (cdr\
        \ rem) a1 (cons (car rem) a2))))))"
      erlang: "-spec result_array(Nums :: [integer()]) -> [integer()].\nresult_array(Nums)\
        \ ->\n  [N1, N2 | Rest] = Nums,\n  {Arr1, Arr2} = process(Rest, [N1], [N2]),\n\
        \  lists:reverse(Arr1) ++ lists:reverse(Arr2).\n\nprocess([], Arr1, Arr2) ->\n\
        \  {Arr1, Arr2};\nprocess([H | T], [L1 | _] = Arr1, [L2 | _] = Arr2) ->\n  if\n\
        \    L1 > L2 -> process(T, [H | Arr1], Arr2);\n    true -> process(T, Arr1,\
        \ [H | Arr2])\n  end."
      elixir: "defmodule Solution do\n  @spec result_array(nums :: [integer]) :: [integer]\n\
        \  def result_array(nums) do\n    [n1, n2 | rest] = nums\n    {arr1, arr2} =\
        \ process(rest, [n1], [n2])\n    Enum.reverse(arr1) ++ Enum.reverse(arr2)\n\
        \  end\n\n  defp process([], arr1, arr2), do: {arr1, arr2}\n  defp process([h\
        \ | t], [l1 | _] = arr1, [l2 | _] = arr2) do\n    if l1 > l2 do\n      process(t,\
        \ [h | arr1], arr2)\n    else\n      process(t, arr1, [h | arr2])\n    end\n\
        \  end\nend"
    approach: 'The problem asks to distribute elements of an array into two separate
      arrays based on a simple comparison rule. We initialize ''arr1'' with the first
      element and ''arr2'' with the second element of the input array. For each subsequent
      element, we compare the most recently added element of ''arr1'' with the most
      recently added element of ''arr2''. If the last element of ''arr1'' is strictly
      greater than the last element of ''arr2'', we append the current element to ''arr1'';
      otherwise, we append it to ''arr2''.


      After iterating through all the elements of the input array, the final result
      is obtained by concatenating ''arr1'' and ''arr2'' in that specific order. Since
      the size of the array is small (up to 50), this simulation using dynamic lists
      or standard arrays with tracking indices is both simple and efficient, ensuring
      each operation is executed in constant time.'
    time_complexity: O(n) where n is the length of the input array. We traverse the
      input array once starting from the third element, performing constant-time comparisons
      and appends, and finally concatenate the two resulting arrays in linear time.
    space_complexity: O(n) because we use auxiliary structures to store the distributed
      elements, and the total number of stored elements across both structures is exactly
      n.
    elapsed_time: 96.49709558486938
    model: gemini-3-flash-preview
    generated_at: '2026-08-20 00:48:02 '
---

## Problem #3069: Distribute Elements Into Two Arrays I

**Difficulty:** Easy

**Topics:** Array, Simulation

## Problem Description

<p>You are given a <strong>1-indexed</strong> array of <strong>distinct</strong> integers <code>nums</code> of length <code>n</code>.</p>

<p>You need to distribute all the elements of <code>nums</code> between two arrays <code>arr1</code> and <code>arr2</code> using <code>n</code> operations. In the first operation, append <code>nums[1]</code> to <code>arr1</code>. In the second operation, append <code>nums[2]</code> to <code>arr2</code>. Afterwards, in the <code>i<sup>th</sup></code> operation:</p>

<ul>
	<li>If the last element of <code>arr1</code> is<strong> greater</strong> than the last element of <code>arr2</code>, append <code>nums[i]</code> to <code>arr1</code>. Otherwise, append <code>nums[i]</code> to <code>arr2</code>.</li>
</ul>

<p>The array <code>result</code> is formed by concatenating the arrays <code>arr1</code> and <code>arr2</code>. For example, if <code>arr1 == [1,2,3]</code> and <code>arr2 == [4,5,6]</code>, then <code>result = [1,2,3,4,5,6]</code>.</p>

<p>Return <em>the array</em> <code>result</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,1,3]
<strong>Output:</strong> [2,3,1]
<strong>Explanation:</strong> After the first 2 operations, arr1 = [2] and arr2 = [1].
In the 3<sup>rd</sup> operation, as the last element of arr1 is greater than the last element of arr2 (2 &gt; 1), append nums[3] to arr1.
After 3 operations, arr1 = [2,3] and arr2 = [1].
Hence, the array result formed by concatenation is [2,3,1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,4,3,8]
<strong>Output:</strong> [5,3,4,8]
<strong>Explanation:</strong> After the first 2 operations, arr1 = [5] and arr2 = [4].
In the 3<sup>rd</sup> operation, as the last element of arr1 is greater than the last element of arr2 (5 &gt; 4), append nums[3] to arr1, hence arr1 becomes [5,3].
In the 4<sup>th</sup> operation, as the last element of arr2 is greater than the last element of arr1 (4 &gt; 3), append nums[4] to arr2, hence arr2 becomes [4,8].
After 4 operations, arr1 = [5,3] and arr2 = [4,8].
Hence, the array result formed by concatenation is [5,3,4,8].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= n &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
	<li>All elements in <code>nums</code> are distinct.</li>
</ul>


## Hints

1. Divide the array into two arrays by keeping track of the last elements of both subarrays.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks to distribute elements of an array into two separate arrays based on a simple comparison rule. We initialize 'arr1' with the first element and 'arr2' with the second element of the input array. For each subsequent element, we compare the most recently added element of 'arr1' with the most recently added element of 'arr2'. If the last element of 'arr1' is strictly greater than the last element of 'arr2', we append the current element to 'arr1'; otherwise, we append it to 'arr2'.

After iterating through all the elements of the input array, the final result is obtained by concatenating 'arr1' and 'arr2' in that specific order. Since the size of the array is small (up to 50), this simulation using dynamic lists or standard arrays with tracking indices is both simple and efficient, ensuring each operation is executed in constant time.

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
    vector<int> resultArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> arr1, arr2;
        arr1.push_back(nums[0]);
        arr2.push_back(nums[1]);
        for (int i = 2; i < n; ++i) {
            if (arr1.back() > arr2.back()) {
                arr1.push_back(nums[i]);
            } else {
                arr2.push_back(nums[i]);
            }
        }
        arr1.insert(arr1.end(), arr2.begin(), arr2.end());
        return arr1;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int[] resultArray(int[] nums) {
        int n = nums.length;
        int[] arr1 = new int[n];
        int[] arr2 = new int[n];
        int size1 = 0, size2 = 0;
        arr1[size1++] = nums[0];
        arr2[size2++] = nums[1];
        for (int i = 2; i < n; i++) {
            if (arr1[size1 - 1] > arr2[size2 - 1]) {
                arr1[size1++] = nums[i];
            } else {
                arr2[size2++] = nums[i];
            }
        }
        int[] result = new int[n];
        int k = 0;
        for (int i = 0; i < size1; i++) result[k++] = arr1[i];
        for (int i = 0; i < size2; i++) result[k++] = arr2[i];
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
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        return arr1 + arr2
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        return arr1 + arr2
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* resultArray(int* nums, int numsSize, int* returnSize) {
    int* arr1 = (int*)malloc(numsSize * sizeof(int));
    int* arr2 = (int*)malloc(numsSize * sizeof(int));
    int size1 = 0, size2 = 0;
    arr1[size1++] = nums[0];
    arr2[size2++] = nums[1];
    for (int i = 2; i < numsSize; i++) {
        if (arr1[size1 - 1] > arr2[size2 - 1]) {
            arr1[size1++] = nums[i];
        } else {
            arr2[size2++] = nums[i];
        }
    }
    int* result = (int*)malloc(numsSize * sizeof(int));
    int k = 0;
    for (int i = 0; i < size1; i++) result[k++] = arr1[i];
    for (int i = 0; i < size2; i++) result[k++] = arr2[i];
    free(arr1);
    free(arr2);
    *returnSize = numsSize;
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
    public int[] ResultArray(int[] nums) {
        List<int> arr1 = new List<int>();
        List<int> arr2 = new List<int>();
        arr1.Add(nums[0]);
        arr2.Add(nums[1]);
        for (int i = 2; i < nums.Length; i++) {
            if (arr1[arr1.Count - 1] > arr2[arr2.Count - 1]) {
                arr1.Add(nums[i]);
            } else {
                arr2.Add(nums[i]);
            }
        }
        arr1.AddRange(arr2);
        return arr1.ToArray();
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
 * @return {number[]}
 */
var resultArray = function(nums) {
    let arr1 = [nums[0]];
    let arr2 = [nums[1]];
    for (let i = 2; i < nums.length; i++) {
        if (arr1[arr1.length - 1] > arr2[arr2.length - 1]) {
            arr1.push(nums[i]);
        } else {
            arr2.push(nums[i]);
        }
    }
    return arr1.concat(arr2);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function resultArray(nums: number[]): number[] {
    let arr1: number[] = [nums[0]];
    let arr2: number[] = [nums[1]];
    for (let i = 2; i < nums.length; i++) {
        if (arr1[arr1.length - 1] > arr2[arr2.length - 1]) {
            arr1.push(nums[i]);
        } else {
            arr2.push(nums[i]);
        }
    }
    return arr1.concat(arr2);
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
     * @return Integer[]
     */
    function resultArray($nums) {
        $arr1 = [$nums[0]];
        $arr2 = [$nums[1]];
        $n = count($nums);
        for ($i = 2; $i < $n; $i++) {
            if ($arr1[count($arr1) - 1] > $arr2[count($arr2) - 1]) {
                $arr1[] = $nums[$i];
            } else {
                $arr2[] = $nums[$i];
            }
        }
        return array_merge($arr1, $arr2);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func resultArray(_ nums: [Int]) -> [Int] {
        var arr1: [Int] = [nums[0]]
        var arr2: [Int] = [nums[1]]
        for i in 2..<nums.count {
            if arr1.last! > arr2.last! {
                arr1.append(nums[i])
            } else {
                arr2.append(nums[i])
            }
        }
        return arr1 + arr2
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun resultArray(nums: IntArray): IntArray {
        val arr1 = mutableListOf<Int>(nums[0])
        val arr2 = mutableListOf<Int>(nums[1])
        for (i in 2 until nums.size) {
            if (arr1.last() > arr2.last()) {
                arr1.add(nums[i])
            } else {
                arr2.add(nums[i])
            }
        }
        val result = IntArray(nums.size)
        var idx = 0
        for (x in arr1) result[idx++] = x
        for (x in arr2) result[idx++] = x
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
  List<int> resultArray(List<int> nums) {
    List<int> arr1 = [nums[0]];
    List<int> arr2 = [nums[1]];
    for (int i = 2; i < nums.length; i++) {
      if (arr1.last > arr2.last) {
        arr1.add(nums[i]);
      } else {
        arr2.add(nums[i]);
      }
    }
    return [...arr1, ...arr2];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func resultArray(nums []int) []int {
    arr1 := []int{nums[0]}
    arr2 := []int{nums[1]}
    for i := 2; i < len(nums); i++ {
        if arr1[len(arr1)-1] > arr2[len(arr2)-1] {
            arr1 = append(arr1, nums[i])
        } else {
            arr2 = append(arr2, nums[i])
        }
    }
    return append(arr1, arr2...)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer[]}
def result_array(nums)
  arr1 = [nums[0]]
  arr2 = [nums[1]]
  (2...nums.length).each do |i|
    if arr1.last > arr2.last
      arr1 << nums[i]
    else
      arr2 << nums[i]
    end
  end
  arr1 + arr2
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable.ArrayBuffer

object Solution {
    def resultArray(nums: Array[Int]): Array[Int] = {
        val arr1 = ArrayBuffer[Int](nums(0))
        val arr2 = ArrayBuffer[Int](nums(1))
        for (i <- 2 until nums.length) {
            if (arr1.last > arr2.last) {
                arr1 += nums(i)
            } else {
                arr2 += nums(i)
            }
        }
        (arr1 ++ arr2).toArray
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn result_array(nums: Vec<i32>) -> Vec<i32> {
        let mut arr1 = vec![nums[0]];
        let mut arr2 = vec![nums[1]];
        for i in 2..nums.len() {
            if arr1.last().unwrap() > arr2.last().unwrap() {
                arr1.push(nums[i]);
            } else {
                arr2.push(nums[i]);
            }
        }
        arr1.extend(arr2);
        arr1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (result-array nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let loop ([rem (cddr nums)]
             [a1 (list (car nums))]
             [a2 (list (cadr nums))])
    (if (null? rem)
        (append (reverse a1) (reverse a2))
        (if (> (car a1) (car a2))
            (loop (cdr rem) (cons (car rem) a1) a2)
            (loop (cdr rem) a1 (cons (car rem) a2))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec result_array(Nums :: [integer()]) -> [integer()].
result_array(Nums) ->
  [N1, N2 | Rest] = Nums,
  {Arr1, Arr2} = process(Rest, [N1], [N2]),
  lists:reverse(Arr1) ++ lists:reverse(Arr2).

process([], Arr1, Arr2) ->
  {Arr1, Arr2};
process([H | T], [L1 | _] = Arr1, [L2 | _] = Arr2) ->
  if
    L1 > L2 -> process(T, [H | Arr1], Arr2);
    true -> process(T, Arr1, [H | Arr2])
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec result_array(nums :: [integer]) :: [integer]
  def result_array(nums) do
    [n1, n2 | rest] = nums
    {arr1, arr2} = process(rest, [n1], [n2])
    Enum.reverse(arr1) ++ Enum.reverse(arr2)
  end

  defp process([], arr1, arr2), do: {arr1, arr2}
  defp process([h | t], [l1 | _] = arr1, [l2 | _] = arr2) do
    if l1 > l2 do
      process(t, [h | arr1], arr2)
    else
      process(t, arr1, [h | arr2])
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the input array. We traverse the input array once starting from the third element, performing constant-time comparisons and appends, and finally concatenate the two resulting arrays in linear time.
- **Space Complexity:** O(n) because we use auxiliary structures to store the distributed elements, and the total number of stored elements across both structures is exactly n.
