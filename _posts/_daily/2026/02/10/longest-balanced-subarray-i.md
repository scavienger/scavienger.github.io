---
layout: post
title: "Longest Balanced Subarray I"
date: 2026-02-10 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Divide and Conquer", "Segment Tree", "Prefix Sum"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/longest-balanced-subarray-i/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <unordered_set>\n#include <algorithm>\n\nclass\
        \ Solution {\npublic:\n    int longestBalanced(std::vector<int>& nums) {\n \
        \       int n = nums.size();\n        int maxLen = 0;\n        for (int i =\
        \ 0; i < n; ++i) {\n            std::unordered_set<int> evenSet;\n         \
        \   std::unordered_set<int> oddSet;\n            for (int j = i; j < n; ++j)\
        \ {\n                if (nums[j] % 2 == 0) {\n                    evenSet.insert(nums[j]);\n\
        \                } else {\n                    oddSet.insert(nums[j]);\n   \
        \             }\n                if (evenSet.size() == oddSet.size()) {\n  \
        \                  maxLen = std::max(maxLen, j - i + 1);\n                }\n\
        \            }\n        }\n        return maxLen;\n    }\n};"
      java: "import java.util.HashSet;\nimport java.util.Set;\n\nclass Solution {\n\
        \    public int longestBalanced(int[] nums) {\n        int maxLen = 0;\n   \
        \     int n = nums.length;\n        for (int i = 0; i < n; i++) {\n        \
        \    Set<Integer> evenSet = new HashSet<>();\n            Set<Integer> oddSet\
        \ = new HashSet<>();\n            for (int j = i; j < n; j++) {\n          \
        \      if (nums[j] % 2 == 0) {\n                    evenSet.add(nums[j]);\n\
        \                } else {\n                    oddSet.add(nums[j]);\n      \
        \          }\n                if (evenSet.size() == oddSet.size()) {\n     \
        \               maxLen = Math.max(maxLen, j - i + 1);\n                }\n \
        \           }\n        }\n        return maxLen;\n    }\n}"
      python: "class Solution(object):\n    def longestBalanced(self, nums):\n     \
        \   \"\"\"\n        :type nums: List[int]\n        :rtype: int\n        \"\"\
        \"\n        max_len = 0\n        n = len(nums)\n        for i in range(n):\n\
        \            even_set = set()\n            odd_set = set()\n            for\
        \ j in range(i, n):\n                val = nums[j]\n                if val %\
        \ 2 == 0:\n                    even_set.add(val)\n                else:\n  \
        \                  odd_set.add(val)\n                if len(even_set) == len(odd_set):\n\
        \                    curr_len = j - i + 1\n                    if curr_len >\
        \ max_len:\n                        max_len = curr_len\n        return max_len"
      python3: "from typing import List\n\nclass Solution:\n    def longestBalanced(self,\
        \ nums: List[int]) -> int:\n        max_len = 0\n        n = len(nums)\n   \
        \     for i in range(n):\n            even_set = set()\n            odd_set\
        \ = set()\n            for j in range(i, n):\n                val = nums[j]\n\
        \                if val % 2 == 0:\n                    even_set.add(val)\n \
        \               else:\n                    odd_set.add(val)\n              \
        \  if len(even_set) == len(odd_set):\n                    curr_len = j - i +\
        \ 1\n                    if curr_len > max_len:\n                        max_len\
        \ = curr_len\n        return max_len"
      c: "int longestBalanced(int* nums, int numsSize) {\n    int maxLen = 0;\n    int\
        \ visited[100001];\n    for (int k = 0; k < 100001; k++) visited[k] = -1;\n\n\
        \    for (int i = 0; i < numsSize; i++) {\n        int distinctEven = 0;\n \
        \       int distinctOdd = 0;\n        for (int j = i; j < numsSize; j++) {\n\
        \            int val = nums[j];\n            if (visited[val] != i) {\n    \
        \            visited[val] = i;\n                if (val % 2 == 0) {\n      \
        \              distinctEven++;\n                } else {\n                 \
        \   distinctOdd++;\n                }\n            }\n            if (distinctEven\
        \ == distinctOdd) {\n                int currentLen = j - i + 1;\n         \
        \       if (currentLen > maxLen) {\n                    maxLen = currentLen;\n\
        \                }\n            }\n        }\n    }\n    return maxLen;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int LongestBalanced(int[] nums) {\n        int maxLen = 0;\n\
        \        int n = nums.Length;\n        for (int i = 0; i < n; i++) {\n     \
        \       HashSet<int> evenSet = new HashSet<int>();\n            HashSet<int>\
        \ oddSet = new HashSet<int>();\n            for (int j = i; j < n; j++) {\n\
        \                if (nums[j] % 2 == 0) {\n                    evenSet.Add(nums[j]);\n\
        \                } else {\n                    oddSet.Add(nums[j]);\n      \
        \          }\n                if (evenSet.Count == oddSet.Count) {\n       \
        \             maxLen = Math.Max(maxLen, j - i + 1);\n                }\n   \
        \         }\n        }\n        return maxLen;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar longestBalanced\
        \ = function(nums) {\n    let maxLen = 0;\n    const n = nums.length;\n    for\
        \ (let i = 0; i < n; i++) {\n        let evenSet = new Set();\n        let oddSet\
        \ = new Set();\n        for (let j = i; j < n; j++) {\n            if (nums[j]\
        \ % 2 === 0) {\n                evenSet.add(nums[j]);\n            } else {\n\
        \                oddSet.add(nums[j]);\n            }\n            if (evenSet.size\
        \ === oddSet.size) {\n                if (j - i + 1 > maxLen) {\n          \
        \          maxLen = j - i + 1;\n                }\n            }\n        }\n\
        \    }\n    return maxLen;\n};"
      typescript: "function longestBalanced(nums: number[]): number {\n    let maxLen\
        \ = 0;\n    const n = nums.length;\n    for (let i = 0; i < n; i++) {\n    \
        \    const evens = new Set<number>();\n        const odds = new Set<number>();\n\
        \        for (let j = i; j < n; j++) {\n            const val = nums[j];\n \
        \           if (val % 2 === 0) {\n                evens.add(val);\n        \
        \    } else {\n                odds.add(val);\n            }\n            if\
        \ (evens.size === odds.size) {\n                const currentLen = j - i + 1;\n\
        \                if (currentLen > maxLen) {\n                    maxLen = currentLen;\n\
        \                }\n            }\n        }\n    }\n    return maxLen;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function longestBalanced($nums) {\n        $n = count($nums);\n\
        \        $maxLen = 0;\n        for ($i = 0; $i < $n; $i++) {\n            $evens\
        \ = [];\n            $odds = [];\n            for ($j = $i; $j < $n; $j++) {\n\
        \                $val = $nums[$j];\n                if ($val % 2 == 0) {\n \
        \                   $evens[$val] = true;\n                } else {\n       \
        \             $odds[$val] = true;\n                }\n                if (count($evens)\
        \ == count($odds)) {\n                    $currentLen = $j - $i + 1;\n     \
        \               if ($currentLen > $maxLen) {\n                        $maxLen\
        \ = $currentLen;\n                    }\n                }\n            }\n\
        \        }\n        return $maxLen;\n    }\n}"
      swift: "class Solution {\n    func longestBalanced(_ nums: [Int]) -> Int {\n \
        \       let n = nums.count\n        var maxLen = 0\n        for i in 0..<n {\n\
        \            var evens = Set<Int>()\n            var odds = Set<Int>()\n   \
        \         for j in i..<n {\n                let val = nums[j]\n            \
        \    if val % 2 == 0 {\n                    evens.insert(val)\n            \
        \    } else {\n                    odds.insert(val)\n                }\n   \
        \             if evens.count == odds.count {\n                    let currentLen\
        \ = j - i + 1\n                    if currentLen > maxLen {\n              \
        \          maxLen = currentLen\n                    }\n                }\n \
        \           }\n        }\n        return maxLen\n    }\n}"
      kotlin: "class Solution {\n    fun longestBalanced(nums: IntArray): Int {\n  \
        \      val n = nums.size\n        var maxLen = 0\n        for (i in 0 until\
        \ n) {\n            val evens = mutableSetOf<Int>()\n            val odds =\
        \ mutableSetOf<Int>()\n            for (j in i until n) {\n                val\
        \ v = nums[j]\n                if (v % 2 == 0) {\n                    evens.add(v)\n\
        \                } else {\n                    odds.add(v)\n               \
        \ }\n                if (evens.size == odds.size) {\n                    val\
        \ currentLen = j - i + 1\n                    if (currentLen > maxLen) {\n \
        \                       maxLen = currentLen\n                    }\n       \
        \         }\n            }\n        }\n        return maxLen\n    }\n}"
      dart: "class Solution {\n  int longestBalanced(List<int> nums) {\n    int n =\
        \ nums.length;\n    int maxLen = 0;\n    for (int i = 0; i < n; i++) {\n   \
        \   Set<int> evens = {};\n      Set<int> odds = {};\n      for (int j = i; j\
        \ < n; j++) {\n        int val = nums[j];\n        if (val % 2 == 0) {\n   \
        \       evens.add(val);\n        } else {\n          odds.add(val);\n      \
        \  }\n        if (evens.length == odds.length) {\n          int currentLen =\
        \ j - i + 1;\n          if (currentLen > maxLen) {\n            maxLen = currentLen;\n\
        \          }\n        }\n      }\n    }\n    return maxLen;\n  }\n}"
      go: "func longestBalanced(nums []int) int {\n    n := len(nums)\n    maxLen :=\
        \ 0\n    for i := 0; i < n; i++ {\n        evens := make(map[int]bool)\n   \
        \     odds := make(map[int]bool)\n        for j := i; j < n; j++ {\n       \
        \     v := nums[j]\n            if v%2 == 0 {\n                evens[v] = true\n\
        \            } else {\n                odds[v] = true\n            }\n     \
        \       if len(evens) == len(odds) {\n                currentLen := j - i +\
        \ 1\n                if currentLen > maxLen {\n                    maxLen =\
        \ currentLen\n                }\n            }\n        }\n    }\n    return\
        \ maxLen\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef longest_balanced(nums)\n\
        \  max_len = 0\n  n = nums.length\n  (0...n).each do |i|\n    evens = {}\n \
        \   odds = {}\n    (i...n).each do |j|\n      val = nums[j]\n      if val %\
        \ 2 == 0\n        evens[val] = true\n      else\n        odds[val] = true\n\
        \      end\n      if evens.size == odds.size\n        len = j - i + 1\n    \
        \    max_len = len if len > max_len\n      end\n    end\n  end\n  max_len\n\
        end"
      scala: "object Solution {\n  def longestBalanced(nums: Array[Int]): Int = {\n\
        \    var maxLen = 0\n    val n = nums.length\n    for (i <- 0 until n) {\n \
        \     val evens = new scala.collection.mutable.HashSet[Int]()\n      val odds\
        \ = new scala.collection.mutable.HashSet[Int]()\n      for (j <- i until n)\
        \ {\n        val num = nums(j)\n        if (num % 2 == 0) {\n          evens.add(num)\n\
        \        } else {\n          odds.add(num)\n        }\n        if (evens.size\
        \ == odds.size) {\n          val curLen = j - i + 1\n          if (curLen >\
        \ maxLen) {\n            maxLen = curLen\n          }\n        }\n      }\n\
        \    }\n    maxLen\n  }\n}"
      rust: "impl Solution {\n    pub fn longest_balanced(nums: Vec<i32>) -> i32 {\n\
        \        let n = nums.len();\n        let mut max_len = 0;\n        let mut\
        \ seen = vec![0; 100001];\n        for i in 0..n {\n            let mut even_count\
        \ = 0;\n            let mut odd_count = 0;\n            let session_id = (i\
        \ + 1) as i32;\n            for j in i..n {\n                let num = nums[j]\
        \ as usize;\n                if seen[num] != session_id {\n                \
        \    seen[num] = session_id;\n                    if num % 2 == 0 {\n      \
        \                  even_count += 1;\n                    } else {\n        \
        \                odd_count += 1;\n                    }\n                }\n\
        \                if even_count == odd_count {\n                    let cur_len\
        \ = (j - i + 1) as i32;\n                    if cur_len > max_len {\n      \
        \                  max_len = cur_len;\n                    }\n             \
        \   }\n            }\n        }\n        max_len\n    }\n}"
      racket: "(define/contract (longest-balanced nums)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let ([n (length nums)]\n        [vec (list->vector nums)]\n\
        \        [ans 0])\n    (for ([i (in-range n)])\n      (let ([evens (make-hash)]\n\
        \            [odds (make-hash)])\n        (for ([j (in-range i n)])\n      \
        \    (let ([num (vector-ref vec j)])\n            (if (even? num)\n        \
        \        (hash-set! evens num #t)\n                (hash-set! odds num #t))\n\
        \            (when (= (hash-count evens) (hash-count odds))\n              (set!\
        \ ans (max ans (+ (- j i) 1))))))))\n    ans))"
      erlang: "-spec longest_balanced(Nums :: [integer()]) -> integer().\nlongest_balanced(Nums)\
        \ ->\n    Arr = list_to_tuple(Nums),\n    N = tuple_size(Arr),\n    lists:foldl(fun(I,\
        \ MaxLenAcc) ->\n        inner_loop(Arr, N, I, I, sets:new(), sets:new(), MaxLenAcc)\n\
        \    end, 0, lists:seq(1, N)).\n\ninner_loop(_Arr, N, _I, J, _Evens, _Odds,\
        \ MaxLen) when J > N ->\n    MaxLen;\ninner_loop(Arr, N, I, J, Evens, Odds,\
        \ MaxLen) ->\n    Val = element(J, Arr),\n    {NextEvens, NextOdds} = case Val\
        \ rem 2 of\n        0 -> {sets:add_element(Val, Evens), Odds};\n        _ ->\
        \ {Evens, sets:add_element(Val, Odds)}\n    end,\n    NewMaxLen = case sets:size(NextEvens)\
        \ =:= sets:size(NextOdds) of\n        true -> \n            Len = J - I + 1,\n\
        \            if Len > MaxLen -> Len; true -> MaxLen end;\n        false -> MaxLen\n\
        \    end,\n    inner_loop(Arr, N, I, J + 1, NextEvens, NextOdds, NewMaxLen)."
      elixir: "defmodule Solution do\n  @spec longest_balanced(nums :: [integer]) ::\
        \ integer\n  def longest_balanced(nums) do\n    n = length(nums)\n    arr =\
        \ List.to_tuple(nums)\n    Enum.reduce(0..(n - 1), 0, fn i, current_max ->\n\
        \      process_from(arr, n, i, i, MapSet.new(), MapSet.new(), current_max)\n\
        \    end)\n  end\n\n  defp process_from(_arr, n, _i, j, _evens, _odds, max_len)\
        \ when j >= n do\n    max_len\n  end\n\n  defp process_from(arr, n, i, j, evens,\
        \ odds, max_len) do\n    val = elem(arr, j)\n    {new_evens, new_odds} = if\
        \ rem(val, 2) == 0 do\n      {MapSet.put(evens, val), odds}\n    else\n    \
        \  {evens, MapSet.put(odds, val)}\n    end\n    new_max_len = if MapSet.size(new_evens)\
        \ == MapSet.size(new_odds) do\n      max(max_len, j - i + 1)\n    else\n   \
        \   max_len\n    end\n    process_from(arr, n, i, j + 1, new_evens, new_odds,\
        \ new_max_len)\n  end\nend"
    approach: 'The problem asks for the longest subarray where the count of distinct
      even numbers equals the count of distinct odd numbers. Given that the constraints
      on the array length $N$ are relatively small ($N \le 1500$), we can use an $O(N^2)$
      brute-force approach. For every possible starting index $i$ of a subarray, we
      expand it by iterating through all possible ending indices $j$. This allows us
      to examine every possible subarray in the given input array.


      To optimize the counting of distinct numbers, we maintain two sets (or use a frequency/tracking
      array) for each starting position $i$. As the ending index $j$ moves forward,
      we add the current element `nums[j]` to the appropriate set (even or odd) and
      immediately check if the sizes of the two sets are equal. By updating the sets
      incrementally, we avoid re-scanning the subarray for each $j$, ensuring the inner
      operations are efficient. If the condition for a balanced subarray is met, we
      update our maximum length record.'
    time_complexity: O(N^2) where $N$ is the length of the array. The algorithm uses
      two nested loops to iterate through all $N(N+1)/2$ possible subarrays. For each
      subarray, set insertions and size comparisons are performed in $O(1)$ average
      time, leading to a total quadratic runtime.
    space_complexity: O(N + V) where $N$ is the length of the array and $V$ is the maximum
      value in `nums`. We use hash sets to store distinct elements within a subarray,
      which can hold at most $N$ elements. In the C implementation, a fixed-size array
      proportional to the range of values $V$ (up to $10^5$) is used for fast element
      tracking.
    elapsed_time: 274.5155785083771
    model: gemini-3-flash-preview
    generated_at: '2026-02-10 01:54:09 '
---

## Problem #3719: Longest Balanced Subarray I

**Difficulty:** Medium

**Topics:** Array, Hash Table, Divide and Conquer, Segment Tree, Prefix Sum

## Problem Description

<p>You are given an integer array <code>nums</code>.</p>

<p>A <strong><span data-keyword="subarray-nonempty">subarray</span></strong> is called <strong>balanced</strong> if the number of <strong>distinct even</strong> numbers in the subarray is equal to the number of <strong>distinct odd</strong> numbers.</p>

<p>Return the length of the <strong>longest</strong> balanced subarray.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,5,4,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The longest balanced subarray is <code>[2, 5, 4, 3]</code>.</li>
	<li>It has 2 distinct even numbers <code>[2, 4]</code> and 2 distinct odd numbers <code>[5, 3]</code>. Thus, the answer is 4.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,2,2,5,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The longest balanced subarray is <code>[3, 2, 2, 5, 4]</code>.</li>
	<li>It has 2 distinct even numbers <code>[2, 4]</code> and 2 distinct odd numbers <code>[3, 5]</code>. Thus, the answer is 5.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The longest balanced subarray is <code>[2, 3, 2]</code>.</li>
	<li>It has 1 distinct even number <code>[2]</code> and 1 distinct odd number <code>[3]</code>. Thus, the answer is 3.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1500</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. Use brute force

2. Try every subarray and use a map/set data structure to track the distinct even and odd numbers

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the longest subarray where the count of distinct even numbers equals the count of distinct odd numbers. Given that the constraints on the array length $N$ are relatively small ($N \le 1500$), we can use an $O(N^2)$ brute-force approach. For every possible starting index $i$ of a subarray, we expand it by iterating through all possible ending indices $j$. This allows us to examine every possible subarray in the given input array.

To optimize the counting of distinct numbers, we maintain two sets (or use a frequency/tracking array) for each starting position $i$. As the ending index $j$ moves forward, we add the current element `nums[j]` to the appropriate set (even or odd) and immediately check if the sizes of the two sets are equal. By updating the sets incrementally, we avoid re-scanning the subarray for each $j$, ensuring the inner operations are efficient. If the condition for a balanced subarray is met, we update our maximum length record.

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
#include <vector>
#include <unordered_set>
#include <algorithm>

class Solution {
public:
    int longestBalanced(std::vector<int>& nums) {
        int n = nums.size();
        int maxLen = 0;
        for (int i = 0; i < n; ++i) {
            std::unordered_set<int> evenSet;
            std::unordered_set<int> oddSet;
            for (int j = i; j < n; ++j) {
                if (nums[j] % 2 == 0) {
                    evenSet.insert(nums[j]);
                } else {
                    oddSet.insert(nums[j]);
                }
                if (evenSet.size() == oddSet.size()) {
                    maxLen = std::max(maxLen, j - i + 1);
                }
            }
        }
        return maxLen;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int longestBalanced(int[] nums) {
        int maxLen = 0;
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            Set<Integer> evenSet = new HashSet<>();
            Set<Integer> oddSet = new HashSet<>();
            for (int j = i; j < n; j++) {
                if (nums[j] % 2 == 0) {
                    evenSet.add(nums[j]);
                } else {
                    oddSet.add(nums[j]);
                }
                if (evenSet.size() == oddSet.size()) {
                    maxLen = Math.max(maxLen, j - i + 1);
                }
            }
        }
        return maxLen;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def longestBalanced(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        n = len(nums)
        for i in range(n):
            even_set = set()
            odd_set = set()
            for j in range(i, n):
                val = nums[j]
                if val % 2 == 0:
                    even_set.add(val)
                else:
                    odd_set.add(val)
                if len(even_set) == len(odd_set):
                    curr_len = j - i + 1
                    if curr_len > max_len:
                        max_len = curr_len
        return max_len
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        max_len = 0
        n = len(nums)
        for i in range(n):
            even_set = set()
            odd_set = set()
            for j in range(i, n):
                val = nums[j]
                if val % 2 == 0:
                    even_set.add(val)
                else:
                    odd_set.add(val)
                if len(even_set) == len(odd_set):
                    curr_len = j - i + 1
                    if curr_len > max_len:
                        max_len = curr_len
        return max_len
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int longestBalanced(int* nums, int numsSize) {
    int maxLen = 0;
    int visited[100001];
    for (int k = 0; k < 100001; k++) visited[k] = -1;

    for (int i = 0; i < numsSize; i++) {
        int distinctEven = 0;
        int distinctOdd = 0;
        for (int j = i; j < numsSize; j++) {
            int val = nums[j];
            if (visited[val] != i) {
                visited[val] = i;
                if (val % 2 == 0) {
                    distinctEven++;
                } else {
                    distinctOdd++;
                }
            }
            if (distinctEven == distinctOdd) {
                int currentLen = j - i + 1;
                if (currentLen > maxLen) {
                    maxLen = currentLen;
                }
            }
        }
    }
    return maxLen;
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
    public int LongestBalanced(int[] nums) {
        int maxLen = 0;
        int n = nums.Length;
        for (int i = 0; i < n; i++) {
            HashSet<int> evenSet = new HashSet<int>();
            HashSet<int> oddSet = new HashSet<int>();
            for (int j = i; j < n; j++) {
                if (nums[j] % 2 == 0) {
                    evenSet.Add(nums[j]);
                } else {
                    oddSet.Add(nums[j]);
                }
                if (evenSet.Count == oddSet.Count) {
                    maxLen = Math.Max(maxLen, j - i + 1);
                }
            }
        }
        return maxLen;
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
var longestBalanced = function(nums) {
    let maxLen = 0;
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        let evenSet = new Set();
        let oddSet = new Set();
        for (let j = i; j < n; j++) {
            if (nums[j] % 2 === 0) {
                evenSet.add(nums[j]);
            } else {
                oddSet.add(nums[j]);
            }
            if (evenSet.size === oddSet.size) {
                if (j - i + 1 > maxLen) {
                    maxLen = j - i + 1;
                }
            }
        }
    }
    return maxLen;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function longestBalanced(nums: number[]): number {
    let maxLen = 0;
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        const evens = new Set<number>();
        const odds = new Set<number>();
        for (let j = i; j < n; j++) {
            const val = nums[j];
            if (val % 2 === 0) {
                evens.add(val);
            } else {
                odds.add(val);
            }
            if (evens.size === odds.size) {
                const currentLen = j - i + 1;
                if (currentLen > maxLen) {
                    maxLen = currentLen;
                }
            }
        }
    }
    return maxLen;
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
    function longestBalanced($nums) {
        $n = count($nums);
        $maxLen = 0;
        for ($i = 0; $i < $n; $i++) {
            $evens = [];
            $odds = [];
            for ($j = $i; $j < $n; $j++) {
                $val = $nums[$j];
                if ($val % 2 == 0) {
                    $evens[$val] = true;
                } else {
                    $odds[$val] = true;
                }
                if (count($evens) == count($odds)) {
                    $currentLen = $j - $i + 1;
                    if ($currentLen > $maxLen) {
                        $maxLen = $currentLen;
                    }
                }
            }
        }
        return $maxLen;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func longestBalanced(_ nums: [Int]) -> Int {
        let n = nums.count
        var maxLen = 0
        for i in 0..<n {
            var evens = Set<Int>()
            var odds = Set<Int>()
            for j in i..<n {
                let val = nums[j]
                if val % 2 == 0 {
                    evens.insert(val)
                } else {
                    odds.insert(val)
                }
                if evens.count == odds.count {
                    let currentLen = j - i + 1
                    if currentLen > maxLen {
                        maxLen = currentLen
                    }
                }
            }
        }
        return maxLen
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun longestBalanced(nums: IntArray): Int {
        val n = nums.size
        var maxLen = 0
        for (i in 0 until n) {
            val evens = mutableSetOf<Int>()
            val odds = mutableSetOf<Int>()
            for (j in i until n) {
                val v = nums[j]
                if (v % 2 == 0) {
                    evens.add(v)
                } else {
                    odds.add(v)
                }
                if (evens.size == odds.size) {
                    val currentLen = j - i + 1
                    if (currentLen > maxLen) {
                        maxLen = currentLen
                    }
                }
            }
        }
        return maxLen
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int longestBalanced(List<int> nums) {
    int n = nums.length;
    int maxLen = 0;
    for (int i = 0; i < n; i++) {
      Set<int> evens = {};
      Set<int> odds = {};
      for (int j = i; j < n; j++) {
        int val = nums[j];
        if (val % 2 == 0) {
          evens.add(val);
        } else {
          odds.add(val);
        }
        if (evens.length == odds.length) {
          int currentLen = j - i + 1;
          if (currentLen > maxLen) {
            maxLen = currentLen;
          }
        }
      }
    }
    return maxLen;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func longestBalanced(nums []int) int {
    n := len(nums)
    maxLen := 0
    for i := 0; i < n; i++ {
        evens := make(map[int]bool)
        odds := make(map[int]bool)
        for j := i; j < n; j++ {
            v := nums[j]
            if v%2 == 0 {
                evens[v] = true
            } else {
                odds[v] = true
            }
            if len(evens) == len(odds) {
                currentLen := j - i + 1
                if currentLen > maxLen {
                    maxLen = currentLen
                }
            }
        }
    }
    return maxLen
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def longest_balanced(nums)
  max_len = 0
  n = nums.length
  (0...n).each do |i|
    evens = {}
    odds = {}
    (i...n).each do |j|
      val = nums[j]
      if val % 2 == 0
        evens[val] = true
      else
        odds[val] = true
      end
      if evens.size == odds.size
        len = j - i + 1
        max_len = len if len > max_len
      end
    end
  end
  max_len
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def longestBalanced(nums: Array[Int]): Int = {
    var maxLen = 0
    val n = nums.length
    for (i <- 0 until n) {
      val evens = new scala.collection.mutable.HashSet[Int]()
      val odds = new scala.collection.mutable.HashSet[Int]()
      for (j <- i until n) {
        val num = nums(j)
        if (num % 2 == 0) {
          evens.add(num)
        } else {
          odds.add(num)
        }
        if (evens.size == odds.size) {
          val curLen = j - i + 1
          if (curLen > maxLen) {
            maxLen = curLen
          }
        }
      }
    }
    maxLen
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn longest_balanced(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut max_len = 0;
        let mut seen = vec![0; 100001];
        for i in 0..n {
            let mut even_count = 0;
            let mut odd_count = 0;
            let session_id = (i + 1) as i32;
            for j in i..n {
                let num = nums[j] as usize;
                if seen[num] != session_id {
                    seen[num] = session_id;
                    if num % 2 == 0 {
                        even_count += 1;
                    } else {
                        odd_count += 1;
                    }
                }
                if even_count == odd_count {
                    let cur_len = (j - i + 1) as i32;
                    if cur_len > max_len {
                        max_len = cur_len;
                    }
                }
            }
        }
        max_len
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (longest-balanced nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ([n (length nums)]
        [vec (list->vector nums)]
        [ans 0])
    (for ([i (in-range n)])
      (let ([evens (make-hash)]
            [odds (make-hash)])
        (for ([j (in-range i n)])
          (let ([num (vector-ref vec j)])
            (if (even? num)
                (hash-set! evens num #t)
                (hash-set! odds num #t))
            (when (= (hash-count evens) (hash-count odds))
              (set! ans (max ans (+ (- j i) 1))))))))
    ans))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec longest_balanced(Nums :: [integer()]) -> integer().
longest_balanced(Nums) ->
    Arr = list_to_tuple(Nums),
    N = tuple_size(Arr),
    lists:foldl(fun(I, MaxLenAcc) ->
        inner_loop(Arr, N, I, I, sets:new(), sets:new(), MaxLenAcc)
    end, 0, lists:seq(1, N)).

inner_loop(_Arr, N, _I, J, _Evens, _Odds, MaxLen) when J > N ->
    MaxLen;
inner_loop(Arr, N, I, J, Evens, Odds, MaxLen) ->
    Val = element(J, Arr),
    {NextEvens, NextOdds} = case Val rem 2 of
        0 -> {sets:add_element(Val, Evens), Odds};
        _ -> {Evens, sets:add_element(Val, Odds)}
    end,
    NewMaxLen = case sets:size(NextEvens) =:= sets:size(NextOdds) of
        true -> 
            Len = J - I + 1,
            if Len > MaxLen -> Len; true -> MaxLen end;
        false -> MaxLen
    end,
    inner_loop(Arr, N, I, J + 1, NextEvens, NextOdds, NewMaxLen).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec longest_balanced(nums :: [integer]) :: integer
  def longest_balanced(nums) do
    n = length(nums)
    arr = List.to_tuple(nums)
    Enum.reduce(0..(n - 1), 0, fn i, current_max ->
      process_from(arr, n, i, i, MapSet.new(), MapSet.new(), current_max)
    end)
  end

  defp process_from(_arr, n, _i, j, _evens, _odds, max_len) when j >= n do
    max_len
  end

  defp process_from(arr, n, i, j, evens, odds, max_len) do
    val = elem(arr, j)
    {new_evens, new_odds} = if rem(val, 2) == 0 do
      {MapSet.put(evens, val), odds}
    else
      {evens, MapSet.put(odds, val)}
    end
    new_max_len = if MapSet.size(new_evens) == MapSet.size(new_odds) do
      max(max_len, j - i + 1)
    else
      max_len
    end
    process_from(arr, n, i, j + 1, new_evens, new_odds, new_max_len)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N^2) where $N$ is the length of the array. The algorithm uses two nested loops to iterate through all $N(N+1)/2$ possible subarrays. For each subarray, set insertions and size comparisons are performed in $O(1)$ average time, leading to a total quadratic runtime.
- **Space Complexity:** O(N + V) where $N$ is the length of the array and $V$ is the maximum value in `nums`. We use hash sets to store distinct elements within a subarray, which can hold at most $N$ elements. In the C implementation, a fixed-size array proportional to the range of values $V$ (up to $10^5$) is used for fast element tracking.
