---
layout: post
title: "Find X-Sum of All K-Long Subarrays I"
date: 2025-11-04 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Hash Table", "Sliding Window", "Heap (Priority Queue)"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> findXSum(vector<int>& nums, int\
        \ k, int x) {\n        vector<int> answer;\n        for (int start = 0; start\
        \ + k <= nums.size(); ++start) {\n            int freq[51] = {};\n         \
        \   for (int i = start; i < start + k; ++i) {\n                ++freq[nums[i]];\n\
        \            }\n            vector<int> values;\n            for (int value\
        \ = 1; value <= 50; ++value) {\n                if (freq[value] > 0) values.push_back(value);\n\
        \            }\n            sort(values.begin(), values.end(), [&](int a, int\
        \ b) {\n                if (freq[a] != freq[b]) return freq[a] > freq[b];\n\
        \                return a > b;\n            });\n            int sum = 0;\n\
        \            for (int i = 0; i < min(x, static_cast<int>(values.size())); ++i)\
        \ {\n                sum += values[i] * freq[values[i]];\n            }\n  \
        \          answer.push_back(sum);\n        }\n        return answer;\n    }\n\
        };"
      java: "class Solution {\n    public int[] findXSum(int[] nums, int k, int x) {\n\
        \        int[] answer = new int[nums.length - k + 1];\n        for (int start\
        \ = 0; start + k <= nums.length; start++) {\n            int[] freq = new int[51];\n\
        \            for (int i = start; i < start + k; i++) {\n                freq[nums[i]]++;\n\
        \            }\n            Integer[] values = new Integer[50];\n          \
        \  int count = 0;\n            for (int value = 1; value <= 50; value++) {\n\
        \                if (freq[value] > 0) values[count++] = value;\n           \
        \ }\n            Arrays.sort(values, 0, count, (a, b) -> {\n               \
        \ if (freq[a] != freq[b]) return Integer.compare(freq[b], freq[a]);\n      \
        \          return Integer.compare(b, a);\n            });\n            int sum\
        \ = 0;\n            for (int i = 0; i < Math.min(x, count); i++) {\n       \
        \         sum += values[i] * freq[values[i]];\n            }\n            answer[start]\
        \ = sum;\n        }\n        return answer;\n    }\n}"
      python: "class Solution(object):\n    def findXSum(self, nums, k, x):\n      \
        \  \"\"\"\n        :type nums: List[int]\n        :type k: int\n        :type\
        \ x: int\n        :rtype: List[int]\n        \"\"\"\n        answer = []\n \
        \       for start in range(len(nums) - k + 1):\n            freq = {}\n    \
        \        for value in nums[start:start + k]:\n                freq[value] =\
        \ freq.get(value, 0) + 1\n            values = sorted(freq, key=lambda value:\
        \ (freq[value], value), reverse=True)\n            answer.append(sum(value *\
        \ freq[value] for value in values[:x]))\n        return answer"
      python3: "class Solution:\n    def findXSum(self, nums: List[int], k: int, x:\
        \ int) -> List[int]:\n        answer = []\n        for start in range(len(nums)\
        \ - k + 1):\n            freq = {}\n            for value in nums[start:start\
        \ + k]:\n                freq[value] = freq.get(value, 0) + 1\n            values\
        \ = sorted(freq, key=lambda value: (freq[value], value), reverse=True)\n   \
        \         answer.append(sum(value * freq[value] for value in values[:x]))\n\
        \        return answer"
      c: "#include <stdlib.h>\n\nint compareValues(const void* first, const void* second,\
        \ void* context) {\n    int a = *(const int*)first;\n    int b = *(const int*)second;\n\
        \    int* freq = (int*)context;\n    if (freq[a] != freq[b]) return freq[b]\
        \ - freq[a];\n    return b - a;\n}\n\nint* findXSum(int* nums, int numsSize,\
        \ int k, int x, int* returnSize) {\n    *returnSize = numsSize - k + 1;\n  \
        \  int* answer = (int*)malloc((size_t)(*returnSize) * sizeof(int));\n    for\
        \ (int start = 0; start + k <= numsSize; start++) {\n        int freq[51] =\
        \ {0};\n        for (int i = start; i < start + k; i++) freq[nums[i]]++;\n \
        \       int values[50];\n        int count = 0;\n        for (int value = 1;\
        \ value <= 50; value++) {\n            if (freq[value] > 0) values[count++]\
        \ = value;\n        }\n        for (int i = 0; i < count; i++) {\n         \
        \   for (int j = i + 1; j < count; j++) {\n                if (freq[values[j]]\
        \ > freq[values[i]] ||\n                    (freq[values[j]] == freq[values[i]]\
        \ && values[j] > values[i])) {\n                    int temp = values[i];\n\
        \                    values[i] = values[j];\n                    values[j] =\
        \ temp;\n                }\n            }\n        }\n        int sum = 0;\n\
        \        int limit = x < count ? x : count;\n        for (int i = 0; i < limit;\
        \ i++) sum += values[i] * freq[values[i]];\n        answer[start] = sum;\n \
        \   }\n    return answer;\n}"
      csharp: "public class Solution {\n    public int[] FindXSum(int[] nums, int k,\
        \ int x) {\n        int[] answer = new int[nums.Length - k + 1];\n        for\
        \ (int start = 0; start + k <= nums.Length; start++) {\n            int[] freq\
        \ = new int[51];\n            for (int i = start; i < start + k; i++) {\n  \
        \              freq[nums[i]]++;\n            }\n            List<int> values\
        \ = new List<int>();\n            for (int value = 1; value <= 50; value++)\
        \ {\n                if (freq[value] > 0) values.Add(value);\n            }\n\
        \            values.Sort((a, b) => {\n                if (freq[a] != freq[b])\
        \ return freq[b].CompareTo(freq[a]);\n                return b.CompareTo(a);\n\
        \            });\n            int sum = 0;\n            for (int i = 0; i <\
        \ Math.Min(x, values.Count); i++) {\n                sum += values[i] * freq[values[i]];\n\
        \            }\n            answer[start] = sum;\n        }\n        return\
        \ answer;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} k\n * @param {number}\
        \ x\n * @return {number[]}\n */\nvar findXSum = function(nums, k, x) {\n   \
        \ const answer = [];\n    for (let start = 0; start + k <= nums.length; start++)\
        \ {\n        const freq = new Map();\n        for (let i = start; i < start\
        \ + k; i++) {\n            freq.set(nums[i], (freq.get(nums[i]) || 0) + 1);\n\
        \        }\n        const values = Array.from(freq.keys()).sort((a, b) => {\n\
        \            if (freq.get(a) !== freq.get(b)) return freq.get(b) - freq.get(a);\n\
        \            return b - a;\n        });\n        let sum = 0;\n        for (let\
        \ i = 0; i < Math.min(x, values.length); i++) {\n            sum += values[i]\
        \ * freq.get(values[i]);\n        }\n        answer.push(sum);\n    }\n    return\
        \ answer;\n};"
      typescript: "function findXSum(nums: number[], k: number, x: number): number[]\
        \ {\n    const answer: number[] = [];\n    for (let start = 0; start <= nums.length\
        \ - k; start++) {\n        const freq = new Map<number, number>();\n       \
        \ for (let i = start; i < start + k; i++) {\n            const value = nums[i];\n\
        \            freq.set(value, (freq.get(value) ?? 0) + 1);\n        }\n     \
        \   const values = Array.from(freq.keys()).sort((a, b) => {\n            const\
        \ frequencyDifference = freq.get(b)! - freq.get(a)!;\n            return frequencyDifference\
        \ !== 0 ? frequencyDifference : b - a;\n        });\n        let sum = 0;\n\
        \        for (let i = 0; i < Math.min(x, values.length); i++) {\n          \
        \  const value = values[i];\n            sum += value * freq.get(value)!;\n\
        \        }\n        answer.push(sum);\n    }\n    return answer;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer $k\n     * @param Integer $x\n     * @return Integer[]\n     */\n\
        \    function findXSum($nums, $k, $x) {\n        $answer = [];\n        for\
        \ ($start = 0; $start <= count($nums) - $k; $start++) {\n            $freq =\
        \ [];\n            for ($i = $start; $i < $start + $k; $i++) {\n           \
        \     $value = $nums[$i];\n                $freq[$value] = ($freq[$value] ??\
        \ 0) + 1;\n            }\n            $values = array_keys($freq);\n       \
        \     usort($values, function ($a, $b) use ($freq) {\n                if ($freq[$a]\
        \ !== $freq[$b]) {\n                    return $freq[$b] <=> $freq[$a];\n  \
        \              }\n                return $b <=> $a;\n            });\n     \
        \       $sum = 0;\n            for ($i = 0; $i < min($x, count($values)); $i++)\
        \ {\n                $value = $values[$i];\n                $sum += $value *\
        \ $freq[$value];\n            }\n            $answer[] = $sum;\n        }\n\
        \        return $answer;\n    }\n}"
      swift: "class Solution {\n    func findXSum(_ nums: [Int], _ k: Int, _ x: Int)\
        \ -> [Int] {\n        var answer: [Int] = []\n        for start in 0...(nums.count\
        \ - k) {\n            var freq: [Int: Int] = [:]\n            for i in start..<(start\
        \ + k) {\n                freq[nums[i], default: 0] += 1\n            }\n  \
        \          let values = freq.keys.sorted {\n                if freq[$0]! !=\
        \ freq[$1]! {\n                    return freq[$0]! > freq[$1]!\n          \
        \      }\n                return $0 > $1\n            }\n            var sum\
        \ = 0\n            for value in values.prefix(x) {\n                sum += value\
        \ * freq[value]!\n            }\n            answer.append(sum)\n        }\n\
        \        return answer\n    }\n}"
      kotlin: "class Solution {\n    fun findXSum(nums: IntArray, k: Int, x: Int): IntArray\
        \ {\n        val answer = IntArray(nums.size - k + 1)\n        for (start in\
        \ 0..nums.size - k) {\n            val freq = mutableMapOf<Int, Int>()\n   \
        \         for (i in start until start + k) {\n                freq[nums[i]]\
        \ = (freq[nums[i]] ?: 0) + 1\n            }\n            val values = freq.keys.sortedWith(\n\
        \                compareByDescending<Int> { freq[it] }.thenByDescending { it\
        \ }\n            )\n            var sum = 0\n            for (value in values.take(x))\
        \ {\n                sum += value * freq.getValue(value)\n            }\n  \
        \          answer[start] = sum\n        }\n        return answer\n    }\n}"
      dart: "class Solution {\n  List<int> findXSum(List<int> nums, int k, int x) {\n\
        \    final answer = <int>[];\n    for (var start = 0; start <= nums.length -\
        \ k; start++) {\n      final freq = <int, int>{};\n      for (var i = start;\
        \ i < start + k; i++) {\n        final value = nums[i];\n        freq[value]\
        \ = (freq[value] ?? 0) + 1;\n      }\n      final values = freq.keys.toList()\n\
        \        ..sort((a, b) {\n          final frequencyDifference = freq[b]! - freq[a]!;\n\
        \          return frequencyDifference != 0 ? frequencyDifference : b.compareTo(a);\n\
        \        });\n      var sum = 0;\n      for (var i = 0; i < x && i < values.length;\
        \ i++) {\n        final value = values[i];\n        sum += value * freq[value]!;\n\
        \      }\n      answer.add(sum);\n    }\n    return answer;\n  }\n}"
      go: "func findXSum(nums []int, k int, x int) []int {\n\tanswer := make([]int,\
        \ 0, len(nums)-k+1)\n\tfor start := 0; start <= len(nums)-k; start++ {\n\t\t\
        freq := make(map[int]int)\n\t\tfor i := start; i < start+k; i++ {\n\t\t\tfreq[nums[i]]++\n\
        \t\t}\n\t\tvalues := make([]int, 0, len(freq))\n\t\tfor value := range freq\
        \ {\n\t\t\tvalues = append(values, value)\n\t\t}\n\t\tsort.Slice(values, func(i,\
        \ j int) bool {\n\t\t\tif freq[values[i]] != freq[values[j]] {\n\t\t\t\treturn\
        \ freq[values[i]] > freq[values[j]]\n\t\t\t}\n\t\t\treturn values[i] > values[j]\n\
        \t\t})\n\t\tsum := 0\n\t\tlimit := x\n\t\tif limit > len(values) {\n\t\t\tlimit\
        \ = len(values)\n\t\t}\n\t\tfor i := 0; i < limit; i++ {\n\t\t\tvalue := values[i]\n\
        \t\t\tsum += value * freq[value]\n\t\t}\n\t\tanswer = append(answer, sum)\n\t\
        }\n\treturn answer\n}"
      ruby: "# @param {Integer[]} nums\n# @param {Integer} k\n# @param {Integer} x\n\
        # @return {Integer[]}\ndef find_x_sum(nums, k, x)\n    answer = []\n    (0..nums.length\
        \ - k).each do |start|\n        freq = Hash.new(0)\n        nums[start, k].each\
        \ { |value| freq[value] += 1 }\n        values = freq.keys.sort_by { |value|\
        \ [-freq[value], -value] }\n        answer << values.first(x).sum { |value|\
        \ value * freq[value] }\n    end\n    answer\nend"
      scala: "object Solution {\n    def findXSum(nums: Array[Int], k: Int, x: Int):\
        \ Array[Int] = {\n        (0 to nums.length - k).map { start =>\n          \
        \  val freq = scala.collection.mutable.Map[Int, Int]()\n            for (i <-\
        \ start until start + k) {\n                freq(nums(i)) = freq.getOrElse(nums(i),\
        \ 0) + 1\n            }\n            freq.keys.toSeq\n                .sortBy(value\
        \ => (-freq(value), -value))\n                .take(x)\n                .map(value\
        \ => value * freq(value))\n                .sum\n        }.toArray\n    }\n}"
      rust: "impl Solution {\n    pub fn find_x_sum(nums: Vec<i32>, k: i32, x: i32)\
        \ -> Vec<i32> {\n        let k = k as usize;\n        let x = x as usize;\n\
        \        let mut answer = Vec::new();\n\n        for start in 0..=nums.len()\
        \ - k {\n            let mut freq = std::collections::HashMap::new();\n    \
        \        for &value in &nums[start..start + k] {\n                *freq.entry(value).or_insert(0)\
        \ += 1;\n            }\n\n            let mut values: Vec<(i32, i32)> = freq.into_iter().collect();\n\
        \            values.sort_by(|a, b| b.1.cmp(&a.1).then_with(|| b.0.cmp(&a.0)));\n\
        \            let sum = values\n                .iter()\n                .take(x)\n\
        \                .map(|&(value, count)| value * count)\n                .sum();\n\
        \            answer.push(sum);\n        }\n\n        answer\n    }\n}"
      racket: "(define/contract (find-x-sum nums k x)\n  (-> (listof exact-integer?)\
        \ exact-integer? exact-integer? (listof exact-integer?))\n  (define values-vector\
        \ (list->vector nums))\n  (for/list ([start (in-range (+ 1 (- (vector-length\
        \ values-vector) k)))])\n    (define freq (make-hash))\n    (for ([i (in-range\
        \ start (+ start k))])\n      (define value (vector-ref values-vector i))\n\
        \      (hash-set! freq value (add1 (hash-ref freq value 0))))\n    (define ordered\n\
        \      (sort (hash-keys freq)\n            (lambda (a b)\n              (or\
        \ (> (hash-ref freq a) (hash-ref freq b))\n                  (and (= (hash-ref\
        \ freq a) (hash-ref freq b)) (> a b))))))\n    (for/sum ([value (in-list (take\
        \ ordered (min x (length ordered)))]) )\n      (* value (hash-ref freq value)))))"
      erlang: "-spec find_x_sum(Nums :: [integer()], K :: integer(), X :: integer())\
        \ -> [integer()].\nfind_x_sum(Nums, K, X) ->\n  find_x_sum_windows(Nums, K,\
        \ X, 0, length(Nums) - K, []).\n\nfind_x_sum_windows(_Nums, _K, _X, Start, Last,\
        \ Acc) when Start > Last ->\n  lists:reverse(Acc);\nfind_x_sum_windows(Nums,\
        \ K, X, Start, Last, Acc) ->\n  Window = lists:sublist(lists:nthtail(Start,\
        \ Nums), K),\n  Freq = lists:foldl(fun(Value, Map) ->\n    maps:update_with(Value,\
        \ fun(Count) -> Count + 1 end, 1, Map)\n  end, #{}, Window),\n  Ordered = lists:sort(fun({ValueA,\
        \ CountA}, {ValueB, CountB}) ->\n    CountA > CountB orelse (CountA =:= CountB\
        \ andalso ValueA > ValueB)\n  end, maps:to_list(Freq)),\n  Selected = lists:sublist(Ordered,\
        \ X),\n  Sum = lists:sum([Value * Count || {Value, Count} <- Selected]),\n \
        \ find_x_sum_windows(Nums, K, X, Start + 1, Last, [Sum | Acc])."
      elixir: "defmodule Solution do\n  @spec find_x_sum(nums :: [integer], k :: integer,\
        \ x :: integer) :: [integer]\n  def find_x_sum(nums, k, x) do\n    nums\n  \
        \  |> Enum.chunk_every(k, 1, :discard)\n    |> Enum.map(fn window ->\n     \
        \ frequencies = Enum.frequencies(window)\n\n      frequencies\n      |> Enum.sort_by(fn\
        \ {value, count} -> {-count, -value} end)\n      |> Enum.take(x)\n      |> Enum.reduce(0,\
        \ fn {value, count}, sum -> sum + value * count end)\n    end)\n  end\nend"
    approach: 'For each subarray of length k, count how many times each value occurs.
      Sort the distinct values by frequency in descending order, breaking ties by value
      in descending order.


      Sum each selected value multiplied by its frequency, taking at most the first
      x distinct values. Since n is at most 50, recomputing the counts and ordering
      for every subarray is sufficient.'
    time_complexity: O((n - k + 1) * (k + 50 log 50)), since each window is counted
      and its at most 50 distinct values are sorted.
    space_complexity: O(50) auxiliary space for the frequency counts and ordering of
      distinct values, excluding the answer array.
    elapsed_time: 92.31635808944702
    model: gpt-6-luna
    generated_at: '2026-11-13 00:19:47 '
---

## Problem #3318: Find X-Sum of All K-Long Subarrays I

**Difficulty:** Easy

**Topics:** Array, Hash Table, Sliding Window, Heap (Priority Queue)

## Problem Description

<p>You are given an array <code>nums</code> of <code>n</code> integers and two integers <code>k</code> and <code>x</code>.</p>

<p>The <strong>x-sum</strong> of an array is calculated by the following procedure:</p>

<ul>
	<li>Count the occurrences of all elements in the array.</li>
	<li>Keep only the occurrences of the top <code>x</code> most frequent elements. If two elements have the same number of occurrences, the element with the <strong>bigger</strong> value is considered more frequent.</li>
	<li>Calculate the sum of the resulting array.</li>
</ul>

<p><strong>Note</strong> that if an array has less than <code>x</code> distinct elements, its <strong>x-sum</strong> is the sum of the array.</p>

<p>Return an integer array <code>answer</code> of length <code>n - k + 1</code> where <code>answer[i]</code> is the <strong>x-sum</strong> of the <span data-keyword="subarray-nonempty">subarray</span> <code>nums[i..i + k - 1]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,2,2,3,4,2,3], k = 6, x = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">[6,10,12]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>For subarray <code>[1, 1, 2, 2, 3, 4]</code>, only elements 1 and 2 will be kept in the resulting array. Hence, <code>answer[0] = 1 + 1 + 2 + 2</code>.</li>
	<li>For subarray <code>[1, 2, 2, 3, 4, 2]</code>, only elements 2 and 4 will be kept in the resulting array. Hence, <code>answer[1] = 2 + 2 + 2 + 4</code>. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times.</li>
	<li>For subarray <code>[2, 2, 3, 4, 2, 3]</code>, only elements 2 and 3 are kept in the resulting array. Hence, <code>answer[2] = 2 + 2 + 2 + 3 + 3</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,8,7,8,7,5], k = 2, x = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">[11,15,15,15,12]</span></p>

<p><strong>Explanation:</strong></p>

<p>Since <code>k == x</code>, <code>answer[i]</code> is equal to the sum of the subarray <code>nums[i..i + k - 1]</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 50</code></li>
	<li><code>1 &lt;= x &lt;= k &lt;= nums.length</code></li>
</ul>


## Hints

1. Implement the x-sum function. Then, run x-sum on every subarray of `nums` of size `k`.

## 🤖 AI-Generated Solution (gpt-6-luna)

### Approach

For each subarray of length k, count how many times each value occurs. Sort the distinct values by frequency in descending order, breaking ties by value in descending order.

Sum each selected value multiplied by its frequency, taking at most the first x distinct values. Since n is at most 50, recomputing the counts and ordering for every subarray is sufficient.

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
    vector<int> findXSum(vector<int>& nums, int k, int x) {
        vector<int> answer;
        for (int start = 0; start + k <= nums.size(); ++start) {
            int freq[51] = {};
            for (int i = start; i < start + k; ++i) {
                ++freq[nums[i]];
            }
            vector<int> values;
            for (int value = 1; value <= 50; ++value) {
                if (freq[value] > 0) values.push_back(value);
            }
            sort(values.begin(), values.end(), [&](int a, int b) {
                if (freq[a] != freq[b]) return freq[a] > freq[b];
                return a > b;
            });
            int sum = 0;
            for (int i = 0; i < min(x, static_cast<int>(values.size())); ++i) {
                sum += values[i] * freq[values[i]];
            }
            answer.push_back(sum);
        }
        return answer;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int[] findXSum(int[] nums, int k, int x) {
        int[] answer = new int[nums.length - k + 1];
        for (int start = 0; start + k <= nums.length; start++) {
            int[] freq = new int[51];
            for (int i = start; i < start + k; i++) {
                freq[nums[i]]++;
            }
            Integer[] values = new Integer[50];
            int count = 0;
            for (int value = 1; value <= 50; value++) {
                if (freq[value] > 0) values[count++] = value;
            }
            Arrays.sort(values, 0, count, (a, b) -> {
                if (freq[a] != freq[b]) return Integer.compare(freq[b], freq[a]);
                return Integer.compare(b, a);
            });
            int sum = 0;
            for (int i = 0; i < Math.min(x, count); i++) {
                sum += values[i] * freq[values[i]];
            }
            answer[start] = sum;
        }
        return answer;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        answer = []
        for start in range(len(nums) - k + 1):
            freq = {}
            for value in nums[start:start + k]:
                freq[value] = freq.get(value, 0) + 1
            values = sorted(freq, key=lambda value: (freq[value], value), reverse=True)
            answer.append(sum(value * freq[value] for value in values[:x]))
        return answer
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        answer = []
        for start in range(len(nums) - k + 1):
            freq = {}
            for value in nums[start:start + k]:
                freq[value] = freq.get(value, 0) + 1
            values = sorted(freq, key=lambda value: (freq[value], value), reverse=True)
            answer.append(sum(value * freq[value] for value in values[:x]))
        return answer
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

int compareValues(const void* first, const void* second, void* context) {
    int a = *(const int*)first;
    int b = *(const int*)second;
    int* freq = (int*)context;
    if (freq[a] != freq[b]) return freq[b] - freq[a];
    return b - a;
}

int* findXSum(int* nums, int numsSize, int k, int x, int* returnSize) {
    *returnSize = numsSize - k + 1;
    int* answer = (int*)malloc((size_t)(*returnSize) * sizeof(int));
    for (int start = 0; start + k <= numsSize; start++) {
        int freq[51] = {0};
        for (int i = start; i < start + k; i++) freq[nums[i]]++;
        int values[50];
        int count = 0;
        for (int value = 1; value <= 50; value++) {
            if (freq[value] > 0) values[count++] = value;
        }
        for (int i = 0; i < count; i++) {
            for (int j = i + 1; j < count; j++) {
                if (freq[values[j]] > freq[values[i]] ||
                    (freq[values[j]] == freq[values[i]] && values[j] > values[i])) {
                    int temp = values[i];
                    values[i] = values[j];
                    values[j] = temp;
                }
            }
        }
        int sum = 0;
        int limit = x < count ? x : count;
        for (int i = 0; i < limit; i++) sum += values[i] * freq[values[i]];
        answer[start] = sum;
    }
    return answer;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int[] FindXSum(int[] nums, int k, int x) {
        int[] answer = new int[nums.Length - k + 1];
        for (int start = 0; start + k <= nums.Length; start++) {
            int[] freq = new int[51];
            for (int i = start; i < start + k; i++) {
                freq[nums[i]]++;
            }
            List<int> values = new List<int>();
            for (int value = 1; value <= 50; value++) {
                if (freq[value] > 0) values.Add(value);
            }
            values.Sort((a, b) => {
                if (freq[a] != freq[b]) return freq[b].CompareTo(freq[a]);
                return b.CompareTo(a);
            });
            int sum = 0;
            for (int i = 0; i < Math.Min(x, values.Count); i++) {
                sum += values[i] * freq[values[i]];
            }
            answer[start] = sum;
        }
        return answer;
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
 * @param {number} x
 * @return {number[]}
 */
var findXSum = function(nums, k, x) {
    const answer = [];
    for (let start = 0; start + k <= nums.length; start++) {
        const freq = new Map();
        for (let i = start; i < start + k; i++) {
            freq.set(nums[i], (freq.get(nums[i]) || 0) + 1);
        }
        const values = Array.from(freq.keys()).sort((a, b) => {
            if (freq.get(a) !== freq.get(b)) return freq.get(b) - freq.get(a);
            return b - a;
        });
        let sum = 0;
        for (let i = 0; i < Math.min(x, values.length); i++) {
            sum += values[i] * freq.get(values[i]);
        }
        answer.push(sum);
    }
    return answer;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function findXSum(nums: number[], k: number, x: number): number[] {
    const answer: number[] = [];
    for (let start = 0; start <= nums.length - k; start++) {
        const freq = new Map<number, number>();
        for (let i = start; i < start + k; i++) {
            const value = nums[i];
            freq.set(value, (freq.get(value) ?? 0) + 1);
        }
        const values = Array.from(freq.keys()).sort((a, b) => {
            const frequencyDifference = freq.get(b)! - freq.get(a)!;
            return frequencyDifference !== 0 ? frequencyDifference : b - a;
        });
        let sum = 0;
        for (let i = 0; i < Math.min(x, values.length); i++) {
            const value = values[i];
            sum += value * freq.get(value)!;
        }
        answer.push(sum);
    }
    return answer;
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
     * @param Integer $x
     * @return Integer[]
     */
    function findXSum($nums, $k, $x) {
        $answer = [];
        for ($start = 0; $start <= count($nums) - $k; $start++) {
            $freq = [];
            for ($i = $start; $i < $start + $k; $i++) {
                $value = $nums[$i];
                $freq[$value] = ($freq[$value] ?? 0) + 1;
            }
            $values = array_keys($freq);
            usort($values, function ($a, $b) use ($freq) {
                if ($freq[$a] !== $freq[$b]) {
                    return $freq[$b] <=> $freq[$a];
                }
                return $b <=> $a;
            });
            $sum = 0;
            for ($i = 0; $i < min($x, count($values)); $i++) {
                $value = $values[$i];
                $sum += $value * $freq[$value];
            }
            $answer[] = $sum;
        }
        return $answer;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func findXSum(_ nums: [Int], _ k: Int, _ x: Int) -> [Int] {
        var answer: [Int] = []
        for start in 0...(nums.count - k) {
            var freq: [Int: Int] = [:]
            for i in start..<(start + k) {
                freq[nums[i], default: 0] += 1
            }
            let values = freq.keys.sorted {
                if freq[$0]! != freq[$1]! {
                    return freq[$0]! > freq[$1]!
                }
                return $0 > $1
            }
            var sum = 0
            for value in values.prefix(x) {
                sum += value * freq[value]!
            }
            answer.append(sum)
        }
        return answer
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun findXSum(nums: IntArray, k: Int, x: Int): IntArray {
        val answer = IntArray(nums.size - k + 1)
        for (start in 0..nums.size - k) {
            val freq = mutableMapOf<Int, Int>()
            for (i in start until start + k) {
                freq[nums[i]] = (freq[nums[i]] ?: 0) + 1
            }
            val values = freq.keys.sortedWith(
                compareByDescending<Int> { freq[it] }.thenByDescending { it }
            )
            var sum = 0
            for (value in values.take(x)) {
                sum += value * freq.getValue(value)
            }
            answer[start] = sum
        }
        return answer
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<int> findXSum(List<int> nums, int k, int x) {
    final answer = <int>[];
    for (var start = 0; start <= nums.length - k; start++) {
      final freq = <int, int>{};
      for (var i = start; i < start + k; i++) {
        final value = nums[i];
        freq[value] = (freq[value] ?? 0) + 1;
      }
      final values = freq.keys.toList()
        ..sort((a, b) {
          final frequencyDifference = freq[b]! - freq[a]!;
          return frequencyDifference != 0 ? frequencyDifference : b.compareTo(a);
        });
      var sum = 0;
      for (var i = 0; i < x && i < values.length; i++) {
        final value = values[i];
        sum += value * freq[value]!;
      }
      answer.add(sum);
    }
    return answer;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func findXSum(nums []int, k int, x int) []int {
	answer := make([]int, 0, len(nums)-k+1)
	for start := 0; start <= len(nums)-k; start++ {
		freq := make(map[int]int)
		for i := start; i < start+k; i++ {
			freq[nums[i]]++
		}
		values := make([]int, 0, len(freq))
		for value := range freq {
			values = append(values, value)
		}
		sort.Slice(values, func(i, j int) bool {
			if freq[values[i]] != freq[values[j]] {
				return freq[values[i]] > freq[values[j]]
			}
			return values[i] > values[j]
		})
		sum := 0
		limit := x
		if limit > len(values) {
			limit = len(values)
		}
		for i := 0; i < limit; i++ {
			value := values[i]
			sum += value * freq[value]
		}
		answer = append(answer, sum)
	}
	return answer
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} x
# @return {Integer[]}
def find_x_sum(nums, k, x)
    answer = []
    (0..nums.length - k).each do |start|
        freq = Hash.new(0)
        nums[start, k].each { |value| freq[value] += 1 }
        values = freq.keys.sort_by { |value| [-freq[value], -value] }
        answer << values.first(x).sum { |value| value * freq[value] }
    end
    answer
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def findXSum(nums: Array[Int], k: Int, x: Int): Array[Int] = {
        (0 to nums.length - k).map { start =>
            val freq = scala.collection.mutable.Map[Int, Int]()
            for (i <- start until start + k) {
                freq(nums(i)) = freq.getOrElse(nums(i), 0) + 1
            }
            freq.keys.toSeq
                .sortBy(value => (-freq(value), -value))
                .take(x)
                .map(value => value * freq(value))
                .sum
        }.toArray
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn find_x_sum(nums: Vec<i32>, k: i32, x: i32) -> Vec<i32> {
        let k = k as usize;
        let x = x as usize;
        let mut answer = Vec::new();

        for start in 0..=nums.len() - k {
            let mut freq = std::collections::HashMap::new();
            for &value in &nums[start..start + k] {
                *freq.entry(value).or_insert(0) += 1;
            }

            let mut values: Vec<(i32, i32)> = freq.into_iter().collect();
            values.sort_by(|a, b| b.1.cmp(&a.1).then_with(|| b.0.cmp(&a.0)));
            let sum = values
                .iter()
                .take(x)
                .map(|&(value, count)| value * count)
                .sum();
            answer.push(sum);
        }

        answer
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (find-x-sum nums k x)
  (-> (listof exact-integer?) exact-integer? exact-integer? (listof exact-integer?))
  (define values-vector (list->vector nums))
  (for/list ([start (in-range (+ 1 (- (vector-length values-vector) k)))])
    (define freq (make-hash))
    (for ([i (in-range start (+ start k))])
      (define value (vector-ref values-vector i))
      (hash-set! freq value (add1 (hash-ref freq value 0))))
    (define ordered
      (sort (hash-keys freq)
            (lambda (a b)
              (or (> (hash-ref freq a) (hash-ref freq b))
                  (and (= (hash-ref freq a) (hash-ref freq b)) (> a b))))))
    (for/sum ([value (in-list (take ordered (min x (length ordered)))]) )
      (* value (hash-ref freq value)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec find_x_sum(Nums :: [integer()], K :: integer(), X :: integer()) -> [integer()].
find_x_sum(Nums, K, X) ->
  find_x_sum_windows(Nums, K, X, 0, length(Nums) - K, []).

find_x_sum_windows(_Nums, _K, _X, Start, Last, Acc) when Start > Last ->
  lists:reverse(Acc);
find_x_sum_windows(Nums, K, X, Start, Last, Acc) ->
  Window = lists:sublist(lists:nthtail(Start, Nums), K),
  Freq = lists:foldl(fun(Value, Map) ->
    maps:update_with(Value, fun(Count) -> Count + 1 end, 1, Map)
  end, #{}, Window),
  Ordered = lists:sort(fun({ValueA, CountA}, {ValueB, CountB}) ->
    CountA > CountB orelse (CountA =:= CountB andalso ValueA > ValueB)
  end, maps:to_list(Freq)),
  Selected = lists:sublist(Ordered, X),
  Sum = lists:sum([Value * Count || {Value, Count} <- Selected]),
  find_x_sum_windows(Nums, K, X, Start + 1, Last, [Sum | Acc]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec find_x_sum(nums :: [integer], k :: integer, x :: integer) :: [integer]
  def find_x_sum(nums, k, x) do
    nums
    |> Enum.chunk_every(k, 1, :discard)
    |> Enum.map(fn window ->
      frequencies = Enum.frequencies(window)

      frequencies
      |> Enum.sort_by(fn {value, count} -> {-count, -value} end)
      |> Enum.take(x)
      |> Enum.reduce(0, fn {value, count}, sum -> sum + value * count end)
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O((n - k + 1) * (k + 50 log 50)), since each window is counted and its at most 50 distinct values are sorted.
- **Space Complexity:** O(50) auxiliary space for the frequency counts and ordering of distinct values, excluding the answer array.
