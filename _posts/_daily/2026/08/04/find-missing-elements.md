---
layout: post
title: "Find Missing Elements"
date: 2026-08-04 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Hash Table", "Sorting"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/find-missing-elements/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> findMissingElements(vector<int>&\
        \ nums) {\n        if (nums.empty()) return {};\n        int minVal = nums[0];\n\
        \        int maxVal = nums[0];\n        unordered_set<int> seen;\n        for\
        \ (int num : nums) {\n            if (num < minVal) minVal = num;\n        \
        \    if (num > maxVal) maxVal = num;\n            seen.insert(num);\n      \
        \  }\n        vector<int> result;\n        for (int i = minVal; i <= maxVal;\
        \ ++i) {\n            if (seen.find(i) == seen.end()) {\n                result.push_back(i);\n\
        \            }\n        }\n        return result;\n    }\n};"
      java: "class Solution {\n    public List<Integer> findMissingElements(int[] nums)\
        \ {\n        if (nums == null || nums.length == 0) return new ArrayList<>();\n\
        \        int minVal = nums[0];\n        int maxVal = nums[0];\n        Set<Integer>\
        \ seen = new HashSet<>();\n        for (int num : nums) {\n            if (num\
        \ < minVal) minVal = num;\n            if (num > maxVal) maxVal = num;\n   \
        \         seen.add(num);\n        }\n        List<Integer> result = new ArrayList<>();\n\
        \        for (int i = minVal; i <= maxVal; i++) {\n            if (!seen.contains(i))\
        \ {\n                result.add(i);\n            }\n        }\n        return\
        \ result;\n    }\n}"
      python: "class Solution(object):\n    def findMissingElements(self, nums):\n \
        \       \"\"\"\n        :type nums: List[int]\n        :rtype: List[int]\n \
        \       \"\"\"\n        if not nums:\n            return []\n        min_val\
        \ = min(nums)\n        max_val = max(nums)\n        seen = set(nums)\n     \
        \   result = []\n        for i in range(min_val, max_val + 1):\n           \
        \ if i not in seen:\n                result.append(i)\n        return result"
      python3: "class Solution:\n    def findMissingElements(self, nums: List[int])\
        \ -> List[int]:\n        if not nums:\n            return []\n        min_val\
        \ = min(nums)\n        max_val = max(nums)\n        seen = set(nums)\n     \
        \   result = []\n        for i in range(min_val, max_val + 1):\n           \
        \ if i not in seen:\n                result.append(i)\n        return result"
      c: "/**\n * Note: The returned array must be malloced, assume caller calls free().\n\
        \ */\nint* findMissingElements(int* nums, int numsSize, int* returnSize) {\n\
        \    if (numsSize == 0) {\n        *returnSize = 0;\n        return NULL;\n\
        \    }\n    int minVal = nums[0];\n    int maxVal = nums[0];\n    bool exists[101]\
        \ = {false};\n    for (int i = 0; i < numsSize; i++) {\n        if (nums[i]\
        \ < minVal) minVal = nums[i];\n        if (nums[i] > maxVal) maxVal = nums[i];\n\
        \        exists[nums[i]] = true;\n    }\n    int rangeSize = maxVal - minVal\
        \ + 1;\n    int* result = (int*)malloc(sizeof(int) * rangeSize);\n    int count\
        \ = 0;\n    for (int i = minVal; i <= maxVal; i++) {\n        if (!exists[i])\
        \ {\n            result[count++] = i;\n        }\n    }\n    *returnSize = count;\n\
        \    return result;\n}"
      csharp: "public class Solution {\n    public IList<int> FindMissingElements(int[]\
        \ nums) {\n        if (nums == null || nums.Length == 0) return new List<int>();\n\
        \        int minVal = nums[0];\n        int maxVal = nums[0];\n        HashSet<int>\
        \ seen = new HashSet<int>();\n        foreach (int num in nums) {\n        \
        \    if (num < minVal) minVal = num;\n            if (num > maxVal) maxVal =\
        \ num;\n            seen.Add(num);\n        }\n        List<int> result = new\
        \ List<int>();\n        for (int i = minVal; i <= maxVal; i++) {\n         \
        \   if (!seen.Contains(i)) {\n                result.Add(i);\n            }\n\
        \        }\n        return result;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number[]}\n */\nvar findMissingElements\
        \ = function(nums) {\n    if (nums.length === 0) return [];\n    let minVal\
        \ = Math.min(...nums);\n    let maxVal = Math.max(...nums);\n    let seen =\
        \ new Set(nums);\n    let result = [];\n    for (let i = minVal; i <= maxVal;\
        \ i++) {\n        if (!seen.has(i)) {\n            result.push(i);\n       \
        \ }\n    }\n    return result;\n};"
      typescript: "function findMissingElements(nums: number[]): number[] {\n    const\
        \ minVal = Math.min(...nums);\n    const maxVal = Math.max(...nums);\n    const\
        \ numSet = new Set(nums);\n    const result: number[] = [];\n\n    for (let\
        \ i = minVal; i <= maxVal; i++) {\n        if (!numSet.has(i)) {\n         \
        \   result.push(i);\n        }\n    }\n\n    return result;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer[]\n     */\n    function findMissingElements($nums) {\n        if\
        \ (empty($nums)) return [];\n        $minVal = min($nums);\n        $maxVal\
        \ = max($nums);\n        $numSet = array_flip($nums);\n        $result = [];\n\
        \n        for ($i = $minVal; $i <= $maxVal; $i++) {\n            if (!isset($numSet[$i]))\
        \ {\n                $result[] = $i;\n            }\n        }\n\n        return\
        \ $result;\n    }\n}"
      swift: "class Solution {\n    func findMissingElements(_ nums: [Int]) -> [Int]\
        \ {\n        guard let minVal = nums.min(), let maxVal = nums.max() else {\n\
        \            return []\n        }\n        let numSet = Set(nums)\n        var\
        \ result: [Int] = []\n\n        for i in minVal...maxVal {\n            if !numSet.contains(i)\
        \ {\n                result.append(i)\n            }\n        }\n\n        return\
        \ result\n    }\n}"
      kotlin: "class Solution {\n    fun findMissingElements(nums: IntArray): List<Int>\
        \ {\n        if (nums.isEmpty()) return emptyList()\n        val minVal = nums.minOrNull()\
        \ ?: 0\n        val maxVal = nums.maxOrNull() ?: 0\n        val numSet = nums.toSet()\n\
        \        val result = mutableListOf<Int>()\n\n        for (i in minVal..maxVal)\
        \ {\n            if (i !in numSet) {\n                result.add(i)\n      \
        \      }\n        }\n\n        return result\n    }\n}"
      dart: "class Solution {\n  List<int> findMissingElements(List<int> nums) {\n \
        \   if (nums.isEmpty) return [];\n\n    int minVal = nums[0];\n    int maxVal\
        \ = nums[0];\n    for (int i = 1; i < nums.length; i++) {\n      if (nums[i]\
        \ < minVal) minVal = nums[i];\n      if (nums[i] > maxVal) maxVal = nums[i];\n\
        \    }\n\n    Set<int> numSet = nums.toSet();\n    List<int> result = [];\n\n\
        \    for (int i = minVal; i <= maxVal; i++) {\n      if (!numSet.contains(i))\
        \ {\n        result.add(i);\n      }\n    }\n\n    return result;\n  }\n}"
      go: "func findMissingElements(nums []int) []int {\n    if len(nums) == 0 {\n \
        \       return []int{}\n    }\n\n    minVal := nums[0]\n    maxVal := nums[0]\n\
        \    numMap := make(map[int]bool)\n    for _, num := range nums {\n        if\
        \ num < minVal {\n            minVal = num\n        }\n        if num > maxVal\
        \ {\n            maxVal = num\n        }\n        numMap[num] = true\n    }\n\
        \n    result := []int{}\n    for i := minVal; i <= maxVal; i++ {\n        if\
        \ !numMap[i] {\n            result = append(result, i)\n        }\n    }\n\n\
        \    return result\n}"
      ruby: "def find_missing_elements(nums)\n  min_val, max_val = nums.minmax\n  (min_val..max_val).to_a\
        \ - nums\nend"
      scala: "object Solution {\n  def findMissingElements(nums: Array[Int]): List[Int]\
        \ = {\n    val minVal = nums.min\n    val maxVal = nums.max\n    val numSet\
        \ = nums.toSet\n    (minVal to maxVal).filterNot(numSet.contains).toList\n \
        \ }\n}"
      rust: "impl Solution {\n    pub fn find_missing_elements(nums: Vec<i32>) -> Vec<i32>\
        \ {\n        let min = *nums.iter().min().unwrap();\n        let max = *nums.iter().max().unwrap();\n\
        \        let set: std::collections::HashSet<i32> = nums.iter().cloned().collect();\n\
        \        let mut result = Vec::new();\n        for i in min..=max {\n      \
        \      if !set.contains(&i) {\n                result.push(i);\n           \
        \ }\n        }\n        result\n    }\n}"
      racket: "(define/contract (find-missing-elements nums)\n  (-> (listof exact-integer?)\
        \ (listof exact-integer?))\n  (let ([min-val (apply min nums)]\n        [max-val\
        \ (apply max nums)])\n    (filter (lambda (x) (not (member x nums)))\n     \
        \       (range min-val (add1 max-val)))))"
      erlang: "-spec find_missing_elements(Nums :: [integer()]) -> [integer()].\nfind_missing_elements(Nums)\
        \ ->\n  Min = lists:min(Nums),\n  Max = lists:max(Nums),\n  [X || X <- lists:seq(Min,\
        \ Max), not lists:member(X, Nums)]."
      elixir: "defmodule Solution do\n  @spec find_missing_elements(nums :: [integer])\
        \ :: [integer]\n  def find_missing_elements(nums) do\n    min_val = Enum.min(nums)\n\
        \    max_val = Enum.max(nums)\n    Enum.filter(min_val..max_val, fn x -> !Enum.member?(nums,\
        \ x) end)\n  end\nend"
    approach: 'The algorithm begins by determining the minimum and maximum values within
      the given array to define the boundaries of the original range. Since the array
      is guaranteed to contain the smallest and largest integers of the initial sequence,
      these bounds are found by iterating through the array once. A set or a boolean
      lookup array is then created to store all existing elements, allowing for constant-time
      existence checks.


      After identifying the bounds and storing existing values, the solution iterates
      through every integer starting from the minimum to the maximum. For each integer
      in this sequence, it checks whether the value exists in the lookup set. If an
      integer is not present, it is added to a result list. Since the iteration proceeds
      in increasing order, the final list of missing elements is naturally sorted.'
    time_complexity: O(N + K), where N is the number of elements in the input array
      and K is the range between the minimum and maximum values. We traverse the array
      once to find the bounds and populate a lookup table, and then iterate through
      the range K to identify missing elements.
    space_complexity: O(N + K), where N is the space used by the hash set or lookup
      array to store the input elements, and K represents the space required to store
      the list of missing elements in the worst case.
    elapsed_time: 118.54159879684448
    model: gemini-3-flash-preview
    generated_at: '2026-08-04 01:50:52 '
---

## Problem #3731: Find Missing Elements

**Difficulty:** Easy

**Topics:** Array, Hash Table, Sorting

## Problem Description

<p>You are given an integer array <code>nums</code> consisting of <strong>unique</strong> integers.</p>

<p>Originally, <code>nums</code> contained <strong>every integer</strong> within a certain range. However, some integers might have gone <strong>missing</strong> from the array.</p>

<p>The <strong>smallest</strong> and <strong>largest</strong> integers of the original range are still present in <code>nums</code>.</p>

<p>Return a <strong>sorted</strong> list of all the missing integers in this range. If no integers are missing, return an <strong>empty</strong> list.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,4,2,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">[3]</span></p>

<p><strong>Explanation:</strong></p>

<p>The smallest integer is 1 and the largest is 5, so the full range should be <code>[1,2,3,4,5]</code>. Among these, only 3 is missing.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [7,8,6,9]</span></p>

<p><strong>Output:</strong> <span class="example-io">[]</span></p>

<p><strong>Explanation:</strong></p>

<p>The smallest integer is 6 and the largest is 9, so the full range is <code>[6,7,8,9]</code>. All integers are already present, so no integer is missing.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">[2,3,4]</span></p>

<p><strong>Explanation:</strong></p>

<p>The smallest integer is 1 and the largest is 5, so the full range should be <code>[1,2,3,4,5]</code>. The missing integers are 2, 3, and 4.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## Hints

1. First, find the maximum and minimum elements in the array.

2. Then, iterate over all the integers in the range `[min, max]` and check if they are in the array.

3. If not, add them to the array, and return the sorted array at the end.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm begins by determining the minimum and maximum values within the given array to define the boundaries of the original range. Since the array is guaranteed to contain the smallest and largest integers of the initial sequence, these bounds are found by iterating through the array once. A set or a boolean lookup array is then created to store all existing elements, allowing for constant-time existence checks.

After identifying the bounds and storing existing values, the solution iterates through every integer starting from the minimum to the maximum. For each integer in this sequence, it checks whether the value exists in the lookup set. If an integer is not present, it is added to a result list. Since the iteration proceeds in increasing order, the final list of missing elements is naturally sorted.

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
    vector<int> findMissingElements(vector<int>& nums) {
        if (nums.empty()) return {};
        int minVal = nums[0];
        int maxVal = nums[0];
        unordered_set<int> seen;
        for (int num : nums) {
            if (num < minVal) minVal = num;
            if (num > maxVal) maxVal = num;
            seen.insert(num);
        }
        vector<int> result;
        for (int i = minVal; i <= maxVal; ++i) {
            if (seen.find(i) == seen.end()) {
                result.push_back(i);
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
    public List<Integer> findMissingElements(int[] nums) {
        if (nums == null || nums.length == 0) return new ArrayList<>();
        int minVal = nums[0];
        int maxVal = nums[0];
        Set<Integer> seen = new HashSet<>();
        for (int num : nums) {
            if (num < minVal) minVal = num;
            if (num > maxVal) maxVal = num;
            seen.add(num);
        }
        List<Integer> result = new ArrayList<>();
        for (int i = minVal; i <= maxVal; i++) {
            if (!seen.contains(i)) {
                result.add(i);
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
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        min_val = min(nums)
        max_val = max(nums)
        seen = set(nums)
        result = []
        for i in range(min_val, max_val + 1):
            if i not in seen:
                result.append(i)
        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        min_val = min(nums)
        max_val = max(nums)
        seen = set(nums)
        result = []
        for i in range(min_val, max_val + 1):
            if i not in seen:
                result.append(i)
        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findMissingElements(int* nums, int numsSize, int* returnSize) {
    if (numsSize == 0) {
        *returnSize = 0;
        return NULL;
    }
    int minVal = nums[0];
    int maxVal = nums[0];
    bool exists[101] = {false};
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] < minVal) minVal = nums[i];
        if (nums[i] > maxVal) maxVal = nums[i];
        exists[nums[i]] = true;
    }
    int rangeSize = maxVal - minVal + 1;
    int* result = (int*)malloc(sizeof(int) * rangeSize);
    int count = 0;
    for (int i = minVal; i <= maxVal; i++) {
        if (!exists[i]) {
            result[count++] = i;
        }
    }
    *returnSize = count;
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public IList<int> FindMissingElements(int[] nums) {
        if (nums == null || nums.Length == 0) return new List<int>();
        int minVal = nums[0];
        int maxVal = nums[0];
        HashSet<int> seen = new HashSet<int>();
        foreach (int num in nums) {
            if (num < minVal) minVal = num;
            if (num > maxVal) maxVal = num;
            seen.Add(num);
        }
        List<int> result = new List<int>();
        for (int i = minVal; i <= maxVal; i++) {
            if (!seen.Contains(i)) {
                result.Add(i);
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
 * @param {number[]} nums
 * @return {number[]}
 */
var findMissingElements = function(nums) {
    if (nums.length === 0) return [];
    let minVal = Math.min(...nums);
    let maxVal = Math.max(...nums);
    let seen = new Set(nums);
    let result = [];
    for (let i = minVal; i <= maxVal; i++) {
        if (!seen.has(i)) {
            result.push(i);
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
function findMissingElements(nums: number[]): number[] {
    const minVal = Math.min(...nums);
    const maxVal = Math.max(...nums);
    const numSet = new Set(nums);
    const result: number[] = [];

    for (let i = minVal; i <= maxVal; i++) {
        if (!numSet.has(i)) {
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
     * @return Integer[]
     */
    function findMissingElements($nums) {
        if (empty($nums)) return [];
        $minVal = min($nums);
        $maxVal = max($nums);
        $numSet = array_flip($nums);
        $result = [];

        for ($i = $minVal; $i <= $maxVal; $i++) {
            if (!isset($numSet[$i])) {
                $result[] = $i;
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
    func findMissingElements(_ nums: [Int]) -> [Int] {
        guard let minVal = nums.min(), let maxVal = nums.max() else {
            return []
        }
        let numSet = Set(nums)
        var result: [Int] = []

        for i in minVal...maxVal {
            if !numSet.contains(i) {
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
    fun findMissingElements(nums: IntArray): List<Int> {
        if (nums.isEmpty()) return emptyList()
        val minVal = nums.minOrNull() ?: 0
        val maxVal = nums.maxOrNull() ?: 0
        val numSet = nums.toSet()
        val result = mutableListOf<Int>()

        for (i in minVal..maxVal) {
            if (i !in numSet) {
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
  List<int> findMissingElements(List<int> nums) {
    if (nums.isEmpty) return [];

    int minVal = nums[0];
    int maxVal = nums[0];
    for (int i = 1; i < nums.length; i++) {
      if (nums[i] < minVal) minVal = nums[i];
      if (nums[i] > maxVal) maxVal = nums[i];
    }

    Set<int> numSet = nums.toSet();
    List<int> result = [];

    for (int i = minVal; i <= maxVal; i++) {
      if (!numSet.contains(i)) {
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
func findMissingElements(nums []int) []int {
    if len(nums) == 0 {
        return []int{}
    }

    minVal := nums[0]
    maxVal := nums[0]
    numMap := make(map[int]bool)
    for _, num := range nums {
        if num < minVal {
            minVal = num
        }
        if num > maxVal {
            maxVal = num
        }
        numMap[num] = true
    }

    result := []int{}
    for i := minVal; i <= maxVal; i++ {
        if !numMap[i] {
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
def find_missing_elements(nums)
  min_val, max_val = nums.minmax
  (min_val..max_val).to_a - nums
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def findMissingElements(nums: Array[Int]): List[Int] = {
    val minVal = nums.min
    val maxVal = nums.max
    val numSet = nums.toSet
    (minVal to maxVal).filterNot(numSet.contains).toList
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn find_missing_elements(nums: Vec<i32>) -> Vec<i32> {
        let min = *nums.iter().min().unwrap();
        let max = *nums.iter().max().unwrap();
        let set: std::collections::HashSet<i32> = nums.iter().cloned().collect();
        let mut result = Vec::new();
        for i in min..=max {
            if !set.contains(&i) {
                result.push(i);
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
(define/contract (find-missing-elements nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let ([min-val (apply min nums)]
        [max-val (apply max nums)])
    (filter (lambda (x) (not (member x nums)))
            (range min-val (add1 max-val)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec find_missing_elements(Nums :: [integer()]) -> [integer()].
find_missing_elements(Nums) ->
  Min = lists:min(Nums),
  Max = lists:max(Nums),
  [X || X <- lists:seq(Min, Max), not lists:member(X, Nums)].
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec find_missing_elements(nums :: [integer]) :: [integer]
  def find_missing_elements(nums) do
    min_val = Enum.min(nums)
    max_val = Enum.max(nums)
    Enum.filter(min_val..max_val, fn x -> !Enum.member?(nums, x) end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N + K), where N is the number of elements in the input array and K is the range between the minimum and maximum values. We traverse the array once to find the bounds and populate a lookup table, and then iterate through the range K to identify missing elements.
- **Space Complexity:** O(N + K), where N is the space used by the hash set or lookup array to store the input elements, and K represents the space required to store the list of missing elements in the worst case.
