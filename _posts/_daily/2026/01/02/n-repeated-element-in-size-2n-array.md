---
layout: post
title: "N-Repeated Element in Size 2N Array"
date: 2026-01-02 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Hash Table"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <unordered_set>\n\nclass Solution {\npublic:\n\
        \    int repeatedNTimes(std::vector<int>& nums) {\n        std::unordered_set<int>\
        \ seen;\n        for (int num : nums) {\n            if (seen.count(num)) {\n\
        \                return num;\n            }\n            seen.insert(num);\n\
        \        }\n        return -1;\n    }\n};"
      java: "import java.util.HashSet;\nimport java.util.Set;\n\nclass Solution {\n\
        \    public int repeatedNTimes(int[] nums) {\n        Set<Integer> seen = new\
        \ HashSet<>();\n        for (int num : nums) {\n            if (seen.contains(num))\
        \ {\n                return num;\n            }\n            seen.add(num);\n\
        \        }\n        return -1;\n    }\n}"
      python: "class Solution:\n    def repeatedNTimes(self, nums: List[int]) -> int:\n\
        \        seen = set()\n        for num in nums:\n            if num in seen:\n\
        \                return num\n            seen.add(num)\n        return -1"
      python3: "class Solution:\n    def repeatedNTimes(self, nums: List[int]) -> int:\n\
        \        seen = set()\n        for num in nums:\n            if num in seen:\n\
        \                return num\n            seen.add(num)\n        return -1"
      c: "#include <stdlib.h>\n#include <stdbool.h>\n\nint repeatedNTimes(int* nums,\
        \ int numsSize) {\n    bool* seen = (bool*)calloc(10001, sizeof(bool)); \n \
        \   if (seen == NULL) {\n        return -1; \n    }\n\n    for (int i = 0; i\
        \ < numsSize; i++) {\n        int num = nums[i];\n        if (seen[num]) {\n\
        \            free(seen);\n            return num;\n        }\n        seen[num]\
        \ = true;\n    }\n\n    free(seen);\n    return -1;\n}"
      csharp: "using System.Collections.Generic;\n\npublic class Solution {\n    public\
        \ int RepeatedNTimes(int[] nums) {\n        HashSet<int> seen = new HashSet<int>();\n\
        \        foreach (int num in nums) {\n            if (seen.Contains(num)) {\n\
        \                return num;\n            }\n            seen.Add(num);\n  \
        \      }\n        return -1;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar repeatedNTimes\
        \ = function(nums) {\n    const seen = new Set();\n    for (const num of nums)\
        \ {\n        if (seen.has(num)) {\n            return num;\n        }\n    \
        \    seen.add(num);\n    }\n    return -1;\n};"
      typescript: "function repeatedNTimes(nums: number[]): number {\n    const seen:\
        \ Set<number> = new Set();\n    for (const num of nums) {\n        if (seen.has(num))\
        \ {\n            return num;\n        }\n        seen.add(num);\n    }\n   \
        \ return -1;\n};"
      php: "<?php\nclass Solution {\n\n    /**\n     * @param Integer[] $nums\n    \
        \ * @return Integer\n     */\n    function repeatedNTimes($nums) {\n       \
        \ $seen = [];\n        foreach ($nums as $num) {\n            if (isset($seen[$num]))\
        \ {\n                return $num;\n            }\n            $seen[$num] =\
        \ true;\n        }\n        return -1;\n    }\n}\n?>"
      swift: "class Solution {\n    func repeatedNTimes(_ nums: [Int]) -> Int {\n  \
        \      var seen = Set<Int>()\n        for num in nums {\n            if seen.contains(num)\
        \ {\n                return num\n            }\n            seen.insert(num)\n\
        \        }\n        return -1\n    }\n}"
      kotlin: "class Solution {\n    fun repeatedNTimes(nums: IntArray): Int {\n   \
        \     val seen = HashSet<Int>()\n        for (num in nums) {\n            if\
        \ (seen.contains(num)) {\n                return num\n            }\n      \
        \      seen.add(num)\n        }\n        return -1\n    }\n}"
      dart: "import 'dart:collection';\n\nclass Solution {\n  int repeatedNTimes(List<int>\
        \ nums) {\n    final Set<int> seen = HashSet<int>();\n    for (final int num\
        \ in nums) {\n      if (seen.contains(num)) {\n        return num;\n      }\n\
        \      seen.add(num);\n    }\n    return -1;\n  }\n}"
      go: "package main\n\nfunc repeatedNTimes(nums []int) int {\n    seen := make(map[int]bool)\n\
        \    for _, num := range nums {\n        if seen[num] {\n            return\
        \ num\n        }\n        seen[num] = true\n    }\n    return -1\n}"
      ruby: "require 'set'\n\n# @param {Integer[]} nums\n# @return {Integer}\ndef repeated_n_times(nums)\n\
        \    seen = Set.new\n    nums.each do |num|\n        if seen.include?(num)\n\
        \            return num\n        end\n        seen.add(num)\n    end\n    -1\n\
        end"
      scala: "import scala.collection.mutable\n\nobject Solution {\n    def repeatedNTimes(nums:\
        \ Array[Int]): Int = {\n        val seen = mutable.HashSet[Int]()\n        for\
        \ (num <- nums) {\n            if (seen.contains(num)) {\n                return\
        \ num\n            }\n            seen.add(num)\n        }\n        -1\n   \
        \ }\n}"
      rust: "use std::collections::HashSet;\n\nimpl Solution {\n    pub fn repeated_n_times(nums:\
        \ Vec<i32>) -> i32 {\n        let mut seen = HashSet::new();\n        for num\
        \ in nums {\n            if seen.contains(&num) {\n                return num;\n\
        \            }\n            seen.insert(num);\n        }\n        -1\n    }\n\
        }"
      racket: "#lang racket\n\n(require racket/control)\n\n(define/contract (repeated-n-times\
        \ nums)\n  (-> (listof exact-integer?) exact-integer?)\n  (let/ec return-val\n\
        \    (let ([seen (make-hash)])\n      (for-each (lambda (num)\n            \
        \      (when (hash-has-key? seen num)\n                    (return-val num))\n\
        \                  (hash-set! seen num #t))\n                nums))\n    -1))"
      erlang: "-module(solution).\n-export([repeated_n_times/1]).\n\nrepeated_n_times(Nums)\
        \ ->\n    repeated_n_times_recursive(Nums, sets:new()).\n\nrepeated_n_times_recursive([],\
        \ _Seen) ->\n    -1;\nrepeated_n_times_recursive([H|T], Seen) ->\n    case sets:is_element(H,\
        \ Seen) of\n        true -> H;\n        false -> repeated_n_times_recursive(T,\
        \ sets:add_element(H, Seen))\n    end."
      elixir: "defmodule Solution do\n  @spec repeated_n_times(nums :: [integer]) ::\
        \ integer\n  def repeated_n_times(nums) do\n    repeated_n_times_recursive(nums,\
        \ MapSet.new())\n  end\n\n  defp repeated_n_times_recursive([], _seen), do:\
        \ -1\n  defp repeated_n_times_recursive([head | tail], seen) do\n    if MapSet.member?(seen,\
        \ head) do\n      head\n    else\n      repeated_n_times_recursive(tail, MapSet.put(seen,\
        \ head))\n    end\n  end\nend"
    approach: 'The problem states that the input array `nums` has a length of `2 * n`,
      contains `n + 1` unique elements, and exactly one element is repeated `n` times.
      This implies that `n` elements appear exactly once, and one specific element appears
      `n` times. To find this repeated element, we can iterate through the array and
      keep track of elements we have already encountered.


      We can use a hash set (or a frequency map) to store the numbers seen so far. For
      each number in the input array, we check if it is already present in our hash
      set. If it is, then this number must be the one that is repeated `n` times, as
      all other `n` unique elements appear only once. If the number is not in the hash
      set, we add it, indicating that we have now seen this unique element. The first
      number encountered that is already in the set is our answer.'
    time_complexity: The algorithm iterates through the `nums` array once. For each
      element, checking for its presence in a hash set and adding it to the hash set
      takes average `O(1)` time. In the worst case, we might iterate through almost
      all `2n` elements before finding the repeated one. Therefore, the total time complexity
      is `O(N)`, where `N` is the length of the `nums` array (which is `2n`).
    space_complexity: In the worst case, we might add `n` unique elements to the hash
      set before encountering the repeated element. Since there are `n+1` unique elements
      in total, the hash set will store at most `n` distinct elements. Therefore, the
      space complexity is `O(n)`, where `n` is half the length of the `nums` array.
      This is equivalent to `O(N)` where `N` is the length of the `nums` array.
    elapsed_time: 53.23585534095764
    model: gemini-2.5-flash
    generated_at: '2026-01-02 01:09:40 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int repeatedNTimes(vector<int>& nums) {\n\
        \        unordered_map<int, int> count;\n        for (int num : nums) {\n  \
        \          count[num]++;\n        }\n        for (auto& pair : count) {\n  \
        \          if (pair.second == nums.size() / 2) {\n                return pair.first;\n\
        \            }\n        }\n        return -1;\n    }\n};"
      java: "class Solution {\n    public int repeatedNTimes(int[] nums) {\n       \
        \ HashMap<Integer, Integer> count = new HashMap<>();\n        for (int num :\
        \ nums) {\n            count.put(num, count.getOrDefault(num, 0) + 1);\n   \
        \     }\n        for (int num : count.keySet()) {\n            if (count.get(num)\
        \ == nums.length / 2) {\n                return num;\n            }\n      \
        \  }\n        return -1;\n    }\n}"
      python: "class Solution:\n    def repeatedNTimes(self, nums: List[int]) -> int:\n\
        \        count = {}\n        for num in nums:\n            if num in count:\n\
        \                count[num] += 1\n            else:\n                count[num]\
        \ = 1\n        for num, freq in count.items():\n            if freq == len(nums)\
        \ // 2:\n                return num"
      python3: "class Solution:\n    def repeatedNTimes(self, nums: List[int]) -> int:\n\
        \        count = {}\n        for num in nums:\n            if num in count:\n\
        \                count[num] += 1\n            else:\n                count[num]\
        \ = 1\n        for num, freq in count.items():\n            if freq == len(nums)\
        \ // 2:\n                return num"
      c: "int repeatedNTimes(int* nums, int numsSize) {\n    int* count = (int*)calloc(10001,\
        \ sizeof(int));\n    for (int i = 0; i < numsSize; i++) {\n        count[nums[i]]++;\n\
        \    }\n    for (int i = 0; i < 10001; i++) {\n        if (count[i] == numsSize\
        \ / 2) {\n            free(count);\n            return i;\n        }\n    }\n\
        \    free(count);\n    return -1;\n}"
      csharp: "public class Solution {\n    public int RepeatedNTimes(int[] nums) {\n\
        \        Dictionary<int, int> count = new Dictionary<int, int>();\n        foreach\
        \ (int num in nums) {\n            if (count.ContainsKey(num)) {\n         \
        \       count[num]++;\n            } else {\n                count[num] = 1;\n\
        \            }\n        }\n        foreach (var pair in count) {\n         \
        \   if (pair.Value == nums.Length / 2) {\n                return pair.Key;\n\
        \            }\n        }\n        return -1;\n    }\n}"
      javascript: "var repeatedNTimes = function(nums) {\n    let count = {};\n    for\
        \ (let num of nums) {\n        if (num in count) {\n            count[num]++;\n\
        \        } else {\n            count[num] = 1;\n        }\n    }\n    for (let\
        \ num in count) {\n        if (count[num] === nums.length / 2) {\n         \
        \   return parseInt(num);\n        }\n    }\n};"
      typescript: "function repeatedNTimes(nums: number[]): number {\n    let count:\
        \ { [key: number]: number } = {};\n    for (let num of nums) {\n        if (num\
        \ in count) {\n            count[num]++;\n        } else {\n            count[num]\
        \ = 1;\n        }\n    }\n    for (let num in count) {\n        if (count[num]\
        \ === nums.length / 2) {\n            return parseInt(num);\n        }\n   \
        \ }\n}"
      php: "$count = array();\nforeach ($nums as $num) {\n    if (array_key_exists($num,\
        \ $count)) {\n        $count[$num]++;\n    } else {\n        $count[$num] =\
        \ 1;\n    }\n}\nforeach ($count as $num => $freq) {\n    if ($freq == count($nums)\
        \ / 2) {\n        return $num;\n    }\n}"
      swift: "class Solution {\n    func repeatedNTimes(_ nums: [Int]) -> Int {\n  \
        \      var count: [Int: Int] = [:]\n        for num in nums {\n            count[num,\
        \ default: 0] += 1\n        }\n        for (num, freq) in count {\n        \
        \    if freq == nums.count / 2 {\n                return num\n            }\n\
        \        }\n        return -1\n    }\n}"
      kotlin: "class Solution {\n    fun repeatedNTimes(nums: IntArray): Int {\n   \
        \     val count = HashMap<Int, Int>()\n        for (num in nums) {\n       \
        \     count[num] = (count[num] ?: 0) + 1\n        }\n        for ((num, freq)\
        \ in count) {\n            if (freq == nums.size / 2) {\n                return\
        \ num\n            }\n        }\n        return -1\n    }\n}"
      dart: "class Solution {\n    int repeatedNTimes(List<int> nums) {\n        Map<int,\
        \ int> count = {};\n        for (int num in nums) {\n            count[num]\
        \ = (count[num] ?? 0) + 1;\n        }\n        for (var num in count.keys) {\n\
        \            if (count[num] == nums.length / 2) {\n                return num;\n\
        \            }\n        }\n        return -1;\n    }\n}"
      go: "func repeatedNTimes(nums []int) int {\n    count := make(map[int]int)\n \
        \   for _, num := range nums {\n        count[num]++\n    }\n    for num, freq\
        \ := range count {\n        if freq == len(nums)/2 {\n            return num\n\
        \        }\n    }\n    return -1\n}"
      ruby: "def repeated_n_times(nums)\n    count = {}\n    nums.each do |num|\n  \
        \      count[num] ||= 0\n        count[num] += 1\n    end\n    count.each do\
        \ |num, freq|\n        return num if freq == nums.size / 2\n    end\n    -1\n\
        end"
      scala: "object Solution {\n    def repeatedNTimes(nums: Array[Int]): Int = {\n\
        \        val count = nums.groupBy(identity).mapValues(_.size)\n        count.find(_._2\
        \ == nums.length / 2).get._1\n    }\n}"
      rust: "struct Solution;\nimpl Solution {\n    pub fn repeated_n_times(nums: Vec<i32>)\
        \ -> i32 {\n        use std::collections::HashMap;\n        let mut count: HashMap<i32,\
        \ i32> = HashMap::new();\n        for &num in nums.iter() {\n            *count.entry(num).or_insert(0)\
        \ += 1;\n        }\n        for (num, freq) in count {\n            if freq\
        \ == nums.len() as i32 / 2 {\n                return num;\n            }\n \
        \       }\n        -1\n    }\n}"
      racket: "(define (repeated-n-times nums)\n    (let ((count (make-hash)))\n   \
        \     (for-each (lambda (num) (hash-update! count num add1 0)) nums)\n     \
        \   (for-each (lambda (num) (when (= (hash-ref count num) (/ (length nums) 2))\
        \ (display num))) (hash-keys count))\n        (newline)))"
      erlang: "-module(solution).\n-export([repeated_n_times/1]).\nrepeated_n_times(Nums)\
        \ ->\n    Count = lists:foldl(fun (Num, Acc) ->\n        case lists:keytake(Num,\
        \ 1, Acc) of\n            {value, {Num, Freq}, Acc1} ->\n                [{Num,\
        \ Freq + 1} | Acc1];\n            false ->\n                [{Num, 1} | Acc]\n\
        \        end\n    end, [], Nums),\n    lists:foldl(fun ({Num, Freq}, Acc) ->\n\
        \        case Freq == length(Nums) div 2 of\n            true -> Num;\n    \
        \        false -> Acc\n        end\n    end, -1, Count)."
      elixir: "defmodule Solution do\n    def repeated_n_times(nums) do\n        count\
        \ = Enum.reduce(nums, %{}, fn num, acc ->\n            Map.update(acc, num,\
        \ 1, &(&1 + 1))\n        end)\n        Enum.find(count, fn {_, freq} -> freq\
        \ == length(nums) / 2 end) |> elem(0)\n    end\nend"
    approach: The problem can be solved by counting the frequency of each element in
      the array. Since one element is repeated n times, it will have the highest frequency.
      We can use a hash map to store the frequency of each element and then find the
      element with the maximum frequency. Another approach is to sort the array and
      then find the element that appears n times. However, the hash map approach is
      more efficient. The key intuition is that the repeated element will have a frequency
      that is n times higher than any other element, making it easy to identify.
    time_complexity: The time complexity of the solution is O(n) because we need to
      iterate over the array to count the frequency of each element. The space complexity
      is also O(n) because in the worst case, we need to store the frequency of each
      element in the hash map.
    space_complexity: The space complexity of the solution is O(n) because we need to
      store the frequency of each element in the hash map. In the worst case, all elements
      in the array are unique, so we need to store the frequency of each element.
    elapsed_time: 4.824769020080566
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-02 01:09:45 '
---

## Problem #961: N-Repeated Element in Size 2N Array

**Difficulty:** Easy

**Topics:** Array, Hash Table

## Problem Description

<p>You are given an integer array <code>nums</code> with the following properties:</p>

<ul>
	<li><code>nums.length == 2 * n</code>.</li>
	<li><code>nums</code> contains <code>n + 1</code> <strong>unique</strong> elements.</li>
	<li>Exactly one element of <code>nums</code> is repeated <code>n</code> times.</li>
</ul>

<p>Return <em>the element that is repeated </em><code>n</code><em> times</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,3]
<strong>Output:</strong> 3
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [2,1,2,5,3,2]
<strong>Output:</strong> 2
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [5,1,5,2,5,3,5,4]
<strong>Output:</strong> 5
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 5000</code></li>
	<li><code>nums.length == 2 * n</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> contains <code>n + 1</code> <strong>unique</strong> elements and one of them is repeated exactly <code>n</code> times.</li>
</ul>


## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2026-01-02 01:09:40 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem states that the input array `nums` has a length of `2 * n`, contains `n + 1` unique elements, and exactly one element is repeated `n` times. This implies that `n` elements appear exactly once, and one specific element appears `n` times. To find this repeated element, we can iterate through the array and keep track of elements we have already encountered.

We can use a hash set (or a frequency map) to store the numbers seen so far. For each number in the input array, we check if it is already present in our hash set. If it is, then this number must be the one that is repeated `n` times, as all other `n` unique elements appear only once. If the number is not in the hash set, we add it, indicating that we have now seen this unique element. The first number encountered that is already in the set is our answer.

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-cpp-gemini-2-5-flash" checked>
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-java-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python3-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-c-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-csharp-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-javascript-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-typescript-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-php-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-swift-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-kotlin-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-dart-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-go-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-ruby-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-scala-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-rust-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-racket-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-erlang-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-elixir-gemini-2-5-flash">
  <div class="tab-labels">
    <label for="lang-cpp-gemini-2-5-flash">C++</label>
    <label for="lang-java-gemini-2-5-flash">Java</label>
    <label for="lang-python-gemini-2-5-flash">Python</label>
    <label for="lang-python3-gemini-2-5-flash">Python3</label>
    <label for="lang-c-gemini-2-5-flash">C</label>
    <label for="lang-csharp-gemini-2-5-flash">C#</label>
    <label for="lang-javascript-gemini-2-5-flash">JavaScript</label>
    <label for="lang-typescript-gemini-2-5-flash">TypeScript</label>
    <label for="lang-php-gemini-2-5-flash">PHP</label>
    <label for="lang-swift-gemini-2-5-flash">Swift</label>
    <label for="lang-kotlin-gemini-2-5-flash">Kotlin</label>
    <label for="lang-dart-gemini-2-5-flash">Dart</label>
    <label for="lang-go-gemini-2-5-flash">Go</label>
    <label for="lang-ruby-gemini-2-5-flash">Ruby</label>
    <label for="lang-scala-gemini-2-5-flash">Scala</label>
    <label for="lang-rust-gemini-2-5-flash">Rust</label>
    <label for="lang-racket-gemini-2-5-flash">Racket</label>
    <label for="lang-erlang-gemini-2-5-flash">Erlang</label>
    <label for="lang-elixir-gemini-2-5-flash">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
#include <vector>
#include <unordered_set>

class Solution {
public:
    int repeatedNTimes(std::vector<int>& nums) {
        std::unordered_set<int> seen;
        for (int num : nums) {
            if (seen.count(num)) {
                return num;
            }
            seen.insert(num);
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
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int repeatedNTimes(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (int num : nums) {
            if (seen.contains(num)) {
                return num;
            }
            seen.add(num);
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
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <stdbool.h>

int repeatedNTimes(int* nums, int numsSize) {
    bool* seen = (bool*)calloc(10001, sizeof(bool)); 
    if (seen == NULL) {
        return -1; 
    }

    for (int i = 0; i < numsSize; i++) {
        int num = nums[i];
        if (seen[num]) {
            free(seen);
            return num;
        }
        seen[num] = true;
    }

    free(seen);
    return -1;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System.Collections.Generic;

public class Solution {
    public int RepeatedNTimes(int[] nums) {
        HashSet<int> seen = new HashSet<int>();
        foreach (int num in nums) {
            if (seen.Contains(num)) {
                return num;
            }
            seen.Add(num);
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
 * @param {number[]} nums
 * @return {number}
 */
var repeatedNTimes = function(nums) {
    const seen = new Set();
    for (const num of nums) {
        if (seen.has(num)) {
            return num;
        }
        seen.add(num);
    }
    return -1;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function repeatedNTimes(nums: number[]): number {
    const seen: Set<number> = new Set();
    for (const num of nums) {
        if (seen.has(num)) {
            return num;
        }
        seen.add(num);
    }
    return -1;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function repeatedNTimes($nums) {
        $seen = [];
        foreach ($nums as $num) {
            if (isset($seen[$num])) {
                return $num;
            }
            $seen[$num] = true;
        }
        return -1;
    }
}
?>
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func repeatedNTimes(_ nums: [Int]) -> Int {
        var seen = Set<Int>()
        for num in nums {
            if seen.contains(num) {
                return num
            }
            seen.insert(num)
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
    fun repeatedNTimes(nums: IntArray): Int {
        val seen = HashSet<Int>()
        for (num in nums) {
            if (seen.contains(num)) {
                return num
            }
            seen.add(num)
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
import 'dart:collection';

class Solution {
  int repeatedNTimes(List<int> nums) {
    final Set<int> seen = HashSet<int>();
    for (final int num in nums) {
      if (seen.contains(num)) {
        return num;
      }
      seen.add(num);
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
package main

func repeatedNTimes(nums []int) int {
    seen := make(map[int]bool)
    for _, num := range nums {
        if seen[num] {
            return num
        }
        seen[num] = true
    }
    return -1
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
require 'set'

# @param {Integer[]} nums
# @return {Integer}
def repeated_n_times(nums)
    seen = Set.new
    nums.each do |num|
        if seen.include?(num)
            return num
        end
        seen.add(num)
    end
    -1
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

object Solution {
    def repeatedNTimes(nums: Array[Int]): Int = {
        val seen = mutable.HashSet[Int]()
        for (num <- nums) {
            if (seen.contains(num)) {
                return num
            }
            seen.add(num)
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
use std::collections::HashSet;

impl Solution {
    pub fn repeated_n_times(nums: Vec<i32>) -> i32 {
        let mut seen = HashSet::new();
        for num in nums {
            if seen.contains(&num) {
                return num;
            }
            seen.insert(num);
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
#lang racket

(require racket/control)

(define/contract (repeated-n-times nums)
  (-> (listof exact-integer?) exact-integer?)
  (let/ec return-val
    (let ([seen (make-hash)])
      (for-each (lambda (num)
                  (when (hash-has-key? seen num)
                    (return-val num))
                  (hash-set! seen num #t))
                nums))
    -1))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([repeated_n_times/1]).

repeated_n_times(Nums) ->
    repeated_n_times_recursive(Nums, sets:new()).

repeated_n_times_recursive([], _Seen) ->
    -1;
repeated_n_times_recursive([H|T], Seen) ->
    case sets:is_element(H, Seen) of
        true -> H;
        false -> repeated_n_times_recursive(T, sets:add_element(H, Seen))
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec repeated_n_times(nums :: [integer]) :: integer
  def repeated_n_times(nums) do
    repeated_n_times_recursive(nums, MapSet.new())
  end

  defp repeated_n_times_recursive([], _seen), do: -1
  defp repeated_n_times_recursive([head | tail], seen) do
    if MapSet.member?(seen, head) do
      head
    else
      repeated_n_times_recursive(tail, MapSet.put(seen, head))
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The algorithm iterates through the `nums` array once. For each element, checking for its presence in a hash set and adding it to the hash set takes average `O(1)` time. In the worst case, we might iterate through almost all `2n` elements before finding the repeated one. Therefore, the total time complexity is `O(N)`, where `N` is the length of the `nums` array (which is `2n`).

- **Space Complexity:** In the worst case, we might add `n` unique elements to the hash set before encountering the repeated element. Since there are `n+1` unique elements in total, the hash set will store at most `n` distinct elements. Therefore, the space complexity is `O(n)`, where `n` is half the length of the `nums` array. This is equivalent to `O(N)` where `N` is the length of the `nums` array.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-02 01:09:45 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by counting the frequency of each element in the array. Since one element is repeated n times, it will have the highest frequency. We can use a hash map to store the frequency of each element and then find the element with the maximum frequency. Another approach is to sort the array and then find the element that appears n times. However, the hash map approach is more efficient. The key intuition is that the repeated element will have a frequency that is n times higher than any other element, making it easy to identify.

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-cpp-llama-3-3-70b-versatile" checked>
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-java-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-python-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-python3-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-c-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-csharp-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-javascript-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-typescript-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-php-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-swift-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-kotlin-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-dart-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-go-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-ruby-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-scala-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-rust-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-racket-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-erlang-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-elixir-llama-3-3-70b-versatile">
  <div class="tab-labels">
    <label for="lang-cpp-llama-3-3-70b-versatile">C++</label>
    <label for="lang-java-llama-3-3-70b-versatile">Java</label>
    <label for="lang-python-llama-3-3-70b-versatile">Python</label>
    <label for="lang-python3-llama-3-3-70b-versatile">Python3</label>
    <label for="lang-c-llama-3-3-70b-versatile">C</label>
    <label for="lang-csharp-llama-3-3-70b-versatile">C#</label>
    <label for="lang-javascript-llama-3-3-70b-versatile">JavaScript</label>
    <label for="lang-typescript-llama-3-3-70b-versatile">TypeScript</label>
    <label for="lang-php-llama-3-3-70b-versatile">PHP</label>
    <label for="lang-swift-llama-3-3-70b-versatile">Swift</label>
    <label for="lang-kotlin-llama-3-3-70b-versatile">Kotlin</label>
    <label for="lang-dart-llama-3-3-70b-versatile">Dart</label>
    <label for="lang-go-llama-3-3-70b-versatile">Go</label>
    <label for="lang-ruby-llama-3-3-70b-versatile">Ruby</label>
    <label for="lang-scala-llama-3-3-70b-versatile">Scala</label>
    <label for="lang-rust-llama-3-3-70b-versatile">Rust</label>
    <label for="lang-racket-llama-3-3-70b-versatile">Racket</label>
    <label for="lang-erlang-llama-3-3-70b-versatile">Erlang</label>
    <label for="lang-elixir-llama-3-3-70b-versatile">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        unordered_map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }
        for (auto& pair : count) {
            if (pair.second == nums.size() / 2) {
                return pair.first;
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
    public int repeatedNTimes(int[] nums) {
        HashMap<Integer, Integer> count = new HashMap<>();
        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }
        for (int num : count.keySet()) {
            if (count.get(num) == nums.length / 2) {
                return num;
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
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for num, freq in count.items():
            if freq == len(nums) // 2:
                return num
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for num, freq in count.items():
            if freq == len(nums) // 2:
                return num
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int repeatedNTimes(int* nums, int numsSize) {
    int* count = (int*)calloc(10001, sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        count[nums[i]]++;
    }
    for (int i = 0; i < 10001; i++) {
        if (count[i] == numsSize / 2) {
            free(count);
            return i;
        }
    }
    free(count);
    return -1;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int RepeatedNTimes(int[] nums) {
        Dictionary<int, int> count = new Dictionary<int, int>();
        foreach (int num in nums) {
            if (count.ContainsKey(num)) {
                count[num]++;
            } else {
                count[num] = 1;
            }
        }
        foreach (var pair in count) {
            if (pair.Value == nums.Length / 2) {
                return pair.Key;
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
var repeatedNTimes = function(nums) {
    let count = {};
    for (let num of nums) {
        if (num in count) {
            count[num]++;
        } else {
            count[num] = 1;
        }
    }
    for (let num in count) {
        if (count[num] === nums.length / 2) {
            return parseInt(num);
        }
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function repeatedNTimes(nums: number[]): number {
    let count: { [key: number]: number } = {};
    for (let num of nums) {
        if (num in count) {
            count[num]++;
        } else {
            count[num] = 1;
        }
    }
    for (let num in count) {
        if (count[num] === nums.length / 2) {
            return parseInt(num);
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
$count = array();
foreach ($nums as $num) {
    if (array_key_exists($num, $count)) {
        $count[$num]++;
    } else {
        $count[$num] = 1;
    }
}
foreach ($count as $num => $freq) {
    if ($freq == count($nums) / 2) {
        return $num;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func repeatedNTimes(_ nums: [Int]) -> Int {
        var count: [Int: Int] = [:]
        for num in nums {
            count[num, default: 0] += 1
        }
        for (num, freq) in count {
            if freq == nums.count / 2 {
                return num
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
    fun repeatedNTimes(nums: IntArray): Int {
        val count = HashMap<Int, Int>()
        for (num in nums) {
            count[num] = (count[num] ?: 0) + 1
        }
        for ((num, freq) in count) {
            if (freq == nums.size / 2) {
                return num
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
    int repeatedNTimes(List<int> nums) {
        Map<int, int> count = {};
        for (int num in nums) {
            count[num] = (count[num] ?? 0) + 1;
        }
        for (var num in count.keys) {
            if (count[num] == nums.length / 2) {
                return num;
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
func repeatedNTimes(nums []int) int {
    count := make(map[int]int)
    for _, num := range nums {
        count[num]++
    }
    for num, freq := range count {
        if freq == len(nums)/2 {
            return num
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
def repeated_n_times(nums)
    count = {}
    nums.each do |num|
        count[num] ||= 0
        count[num] += 1
    end
    count.each do |num, freq|
        return num if freq == nums.size / 2
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
    def repeatedNTimes(nums: Array[Int]): Int = {
        val count = nums.groupBy(identity).mapValues(_.size)
        count.find(_._2 == nums.length / 2).get._1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
struct Solution;
impl Solution {
    pub fn repeated_n_times(nums: Vec<i32>) -> i32 {
        use std::collections::HashMap;
        let mut count: HashMap<i32, i32> = HashMap::new();
        for &num in nums.iter() {
            *count.entry(num).or_insert(0) += 1;
        }
        for (num, freq) in count {
            if freq == nums.len() as i32 / 2 {
                return num;
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
(define (repeated-n-times nums)
    (let ((count (make-hash)))
        (for-each (lambda (num) (hash-update! count num add1 0)) nums)
        (for-each (lambda (num) (when (= (hash-ref count num) (/ (length nums) 2)) (display num))) (hash-keys count))
        (newline)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([repeated_n_times/1]).
repeated_n_times(Nums) ->
    Count = lists:foldl(fun (Num, Acc) ->
        case lists:keytake(Num, 1, Acc) of
            {value, {Num, Freq}, Acc1} ->
                [{Num, Freq + 1} | Acc1];
            false ->
                [{Num, 1} | Acc]
        end
    end, [], Nums),
    lists:foldl(fun ({Num, Freq}, Acc) ->
        case Freq == length(Nums) div 2 of
            true -> Num;
            false -> Acc
        end
    end, -1, Count).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
    def repeated_n_times(nums) do
        count = Enum.reduce(nums, %{}, fn num, acc ->
            Map.update(acc, num, 1, &(&1 + 1))
        end)
        Enum.find(count, fn {_, freq} -> freq == length(nums) / 2 end) |> elem(0)
    end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of the solution is O(n) because we need to iterate over the array to count the frequency of each element. The space complexity is also O(n) because in the worst case, we need to store the frequency of each element in the hash map.

- **Space Complexity:** The space complexity of the solution is O(n) because we need to store the frequency of each element in the hash map. In the worst case, all elements in the array are unique, so we need to store the frequency of each element.

</div>
</details>
