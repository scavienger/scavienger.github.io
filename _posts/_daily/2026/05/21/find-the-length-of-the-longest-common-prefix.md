---
layout: post
title: "Find the Length of the Longest Common Prefix"
date: 2026-05-21 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "String", "Trie"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <unordered_set>\n#include <algorithm>\n\nclass\
        \ Solution {\npublic:\n    int longestCommonPrefix(std::vector<int>& arr1, std::vector<int>&\
        \ arr2) {\n        std::unordered_set<int> prefixes;\n        prefixes.reserve(arr1.size()\
        \ * 8);\n        for (int val : arr1) {\n            while (val > 0) {\n   \
        \             prefixes.insert(val);\n                val /= 10;\n          \
        \  }\n        }\n\n        int maxLen = 0;\n        for (int val : arr2) {\n\
        \            while (val > 0) {\n                if (prefixes.count(val)) {\n\
        \                    int count = 0;\n                    int temp = val;\n \
        \                   while (temp > 0) {\n                        temp /= 10;\n\
        \                        count++;\n                    }\n                 \
        \   maxLen = std::max(maxLen, count);\n                    break;\n        \
        \        }\n                val /= 10;\n            }\n        }\n        return\
        \ maxLen;\n    }\n};"
      java: "import java.util.HashSet;\n\nclass Solution {\n    public int longestCommonPrefix(int[]\
        \ arr1, int[] arr2) {\n        HashSet<Integer> prefixes = new HashSet<>();\n\
        \        for (int val : arr1) {\n            while (val > 0) {\n           \
        \     prefixes.add(val);\n                val /= 10;\n            }\n      \
        \  }\n\n        int maxLen = 0;\n        for (int val : arr2) {\n          \
        \  while (val > 0) {\n                if (prefixes.contains(val)) {\n      \
        \              int count = 0;\n                    int temp = val;\n       \
        \             while (temp > 0) {\n                        temp /= 10;\n    \
        \                    count++;\n                    }\n                    maxLen\
        \ = Math.max(maxLen, count);\n                    break;\n                }\n\
        \                val /= 10;\n            }\n        }\n        return maxLen;\n\
        \    }\n}"
      python: "class Solution(object):\n    def longestCommonPrefix(self, arr1, arr2):\n\
        \        \"\"\"\n        :type arr1: List[int]\n        :type arr2: List[int]\n\
        \        :rtype: int\n        \"\"\"\n        prefixes = set()\n        for\
        \ val in arr1:\n            while val > 0:\n                prefixes.add(val)\n\
        \                val //= 10\n\n        max_len = 0\n        for val in arr2:\n\
        \            while val > 0:\n                if val in prefixes:\n         \
        \           curr_len = len(str(val))\n                    if curr_len > max_len:\n\
        \                        max_len = curr_len\n                    break\n   \
        \             val //= 10\n        return max_len"
      python3: "from typing import List\n\nclass Solution:\n    def longestCommonPrefix(self,\
        \ arr1: List[int], arr2: List[int]) -> int:\n        prefixes = set()\n    \
        \    for val in arr1:\n            while val > 0:\n                prefixes.add(val)\n\
        \                val //= 10\n\n        max_len = 0\n        for val in arr2:\n\
        \            while val > 0:\n                if val in prefixes:\n         \
        \           curr_len = len(str(val))\n                    if curr_len > max_len:\n\
        \                        max_len = curr_len\n                    break\n   \
        \             val //= 10\n        return max_len"
      c: "#include <stdbool.h>\n#include <string.h>\n\n#define TABLE_SIZE 1300021\n\
        static int hash_table[TABLE_SIZE];\n\nvoid insert_prefix(int val) {\n    unsigned\
        \ int h = (unsigned int)val % TABLE_SIZE;\n    while (hash_table[h] != 0) {\n\
        \        if (hash_table[h] == val) return;\n        h = (h + 1) % TABLE_SIZE;\n\
        \    }\n    hash_table[h] = val;\n}\n\nbool find_prefix(int val) {\n    unsigned\
        \ int h = (unsigned int)val % TABLE_SIZE;\n    while (hash_table[h] != 0) {\n\
        \        if (hash_table[h] == val) return true;\n        h = (h + 1) % TABLE_SIZE;\n\
        \    }\n    return false;\n}\n\nint longestCommonPrefix(int* arr1, int arr1Size,\
        \ int* arr2, int arr2Size) {\n    memset(hash_table, 0, sizeof(hash_table));\n\
        \    for (int i = 0; i < arr1Size; i++) {\n        int val = arr1[i];\n    \
        \    while (val > 0) {\n            insert_prefix(val);\n            val /=\
        \ 10;\n        }\n    }\n\n    int maxLen = 0;\n    for (int i = 0; i < arr2Size;\
        \ i++) {\n        int val = arr2[i];\n        while (val > 0) {\n          \
        \  if (find_prefix(val)) {\n                int count = 0;\n               \
        \ int temp = val;\n                while (temp > 0) {\n                    temp\
        \ /= 10;\n                    count++;\n                }\n                if\
        \ (count > maxLen) maxLen = count;\n                break;\n            }\n\
        \            val /= 10;\n        }\n    }\n    return maxLen;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int LongestCommonPrefix(int[] arr1, int[] arr2) {\n        HashSet<int>\
        \ prefixes = new HashSet<int>();\n        foreach (int val in arr1) {\n    \
        \        int temp = val;\n            while (temp > 0) {\n                prefixes.Add(temp);\n\
        \                temp /= 10;\n            }\n        }\n\n        int maxLength\
        \ = 0;\n        foreach (int val in arr2) {\n            int temp = val;\n \
        \           while (temp > 0) {\n                if (prefixes.Contains(temp))\
        \ {\n                    int currentLen = temp.ToString().Length;\n        \
        \            if (currentLen > maxLength) {\n                        maxLength\
        \ = currentLen;\n                    }\n                    break;\n       \
        \         }\n                temp /= 10;\n            }\n        }\n\n     \
        \   return maxLength;\n    }\n}"
      javascript: "/**\n * @param {number[]} arr1\n * @param {number[]} arr2\n * @return\
        \ {number}\n */\nvar longestCommonPrefix = function(arr1, arr2) {\n    const\
        \ prefixes = new Set();\n    for (let val of arr1) {\n        let temp = val;\n\
        \        while (temp > 0) {\n            prefixes.add(temp);\n            temp\
        \ = Math.floor(temp / 10);\n        }\n    }\n\n    let maxLength = 0;\n   \
        \ for (let val of arr2) {\n        let temp = val;\n        while (temp > 0)\
        \ {\n            if (prefixes.has(temp)) {\n                const currentLen\
        \ = temp.toString().length;\n                if (currentLen > maxLength) {\n\
        \                    maxLength = currentLen;\n                }\n          \
        \      break;\n            }\n            temp = Math.floor(temp / 10);\n  \
        \      }\n    }\n\n    return maxLength;\n};"
      typescript: "function longestCommonPrefix(arr1: number[], arr2: number[]): number\
        \ {\n    const prefixes: Set<number> = new Set();\n    for (let val of arr1)\
        \ {\n        let temp = val;\n        while (temp > 0) {\n            prefixes.add(temp);\n\
        \            temp = Math.floor(temp / 10);\n        }\n    }\n\n    let maxLength:\
        \ number = 0;\n    for (let val of arr2) {\n        let temp = val;\n      \
        \  while (temp > 0) {\n            if (prefixes.has(temp)) {\n             \
        \   const currentLen = temp.toString().length;\n                if (currentLen\
        \ > maxLength) {\n                    maxLength = currentLen;\n            \
        \    }\n                break;\n            }\n            temp = Math.floor(temp\
        \ / 10);\n        }\n    }\n\n    return maxLength;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $arr1\n     * @param\
        \ Integer[] $arr2\n     * @return Integer\n     */\n    function longestCommonPrefix($arr1,\
        \ $arr2) {\n        $prefixes = [];\n        foreach ($arr1 as $val) {\n   \
        \         $temp = $val;\n            while ($temp > 0) {\n                $prefixes[$temp]\
        \ = true;\n                $temp = (int)($temp / 10);\n            }\n     \
        \   }\n\n        $maxLength = 0;\n        foreach ($arr2 as $val) {\n      \
        \      $temp = $val;\n            while ($temp > 0) {\n                if (isset($prefixes[$temp]))\
        \ {\n                    $currentLen = strlen((string)$temp);\n            \
        \        if ($currentLen > $maxLength) {\n                        $maxLength\
        \ = $currentLen;\n                    }\n                    break;\n      \
        \          }\n                $temp = (int)($temp / 10);\n            }\n  \
        \      }\n\n        return $maxLength;\n    }\n}"
      swift: "class Solution {\n    func longestCommonPrefix(_ arr1: [Int], _ arr2:\
        \ [Int]) -> Int {\n        var prefixes = Set<Int>()\n        for val in arr1\
        \ {\n            var temp = val\n            while temp > 0 {\n            \
        \    prefixes.insert(temp)\n                temp /= 10\n            }\n    \
        \    }\n\n        var maxLength = 0\n        for val in arr2 {\n           \
        \ var temp = val\n            while temp > 0 {\n                if prefixes.contains(temp)\
        \ {\n                    let currentLen = String(temp).count\n             \
        \       if currentLen > maxLength {\n                        maxLength = currentLen\n\
        \                    }\n                    break\n                }\n     \
        \           temp /= 10\n            }\n        }\n\n        return maxLength\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun longestCommonPrefix(arr1: IntArray, arr2: IntArray):\
        \ Int {\n        val prefixes = HashSet<Int>()\n        for (x in arr1) {\n\
        \            var n = x\n            while (n > 0) {\n                prefixes.add(n)\n\
        \                n /= 10\n            }\n        }\n        var maxLen = 0\n\
        \        for (y in arr2) {\n            var n = y\n            var currLen =\
        \ 0\n            var temp = n\n            while (temp > 0) {\n            \
        \    temp /= 10\n                currLen++\n            }\n            if (currLen\
        \ <= maxLen) continue\n            while (n > 0 && currLen > maxLen) {\n   \
        \             if (prefixes.contains(n)) {\n                    maxLen = currLen\n\
        \                    break\n                }\n                n /= 10\n   \
        \             currLen--\n            }\n        }\n        return maxLen\n \
        \   }\n}"
      dart: "class Solution {\n  int longestCommonPrefix(List<int> arr1, List<int> arr2)\
        \ {\n    final prefixes = <int>{};\n    for (var x in arr1) {\n      var n =\
        \ x;\n      while (n > 0) {\n        prefixes.add(n);\n        n ~/= 10;\n \
        \     }\n    }\n    int maxLen = 0;\n    for (var y in arr2) {\n      var n\
        \ = y;\n      int currLen = 0;\n      var temp = n;\n      while (temp > 0)\
        \ {\n        temp ~/= 10;\n        currLen++;\n      }\n      if (currLen <=\
        \ maxLen) continue;\n      while (n > 0 && currLen > maxLen) {\n        if (prefixes.contains(n))\
        \ {\n          maxLen = currLen;\n          break;\n        }\n        n ~/=\
        \ 10;\n        currLen--;\n      }\n    }\n    return maxLen;\n  }\n}"
      go: "func longestCommonPrefix(arr1 []int, arr2 []int) int {\n    prefixes := make(map[int]bool)\n\
        \    for _, x := range arr1 {\n        n := x\n        for n > 0 {\n       \
        \     prefixes[n] = true\n            n /= 10\n        }\n    }\n    maxLen\
        \ := 0\n    for _, y := range arr2 {\n        n := y\n        currLen := 0\n\
        \        temp := n\n        for temp > 0 {\n            temp /= 10\n       \
        \     currLen++\n        }\n        if currLen <= maxLen {\n            continue\n\
        \        }\n        for n > 0 && currLen > maxLen {\n            if _, found\
        \ := prefixes[n]; found {\n                maxLen = currLen\n              \
        \  break\n            }\n            n /= 10\n            currLen--\n      \
        \  }\n    }\n    return maxLen\n}"
      ruby: "def longest_common_prefix(arr1, arr2)\n  prefixes = {}\n  arr1.each do\
        \ |x|\n    n = x\n    while n > 0\n      prefixes[n] = true\n      n /= 10\n\
        \    end\n  end\n  max_len = 0\n  arr2.each do |y|\n    n = y\n    curr_len\
        \ = 0\n    temp = n\n    while temp > 0\n      temp /= 10\n      curr_len +=\
        \ 1\n    end\n    next if curr_len <= max_len\n    while n > 0 && curr_len >\
        \ max_len\n      if prefixes[n]\n        max_len = curr_len\n        break\n\
        \      end\n      n /= 10\n      curr_len -= 1\n    end\n  end\n  max_len\n\
        end"
      scala: "import scala.collection.mutable\n\nobject Solution {\n  def longestCommonPrefix(arr1:\
        \ Array[Int], arr2: Array[Int]): Int = {\n    val prefixes = mutable.HashSet[Int]()\n\
        \    for (x <- arr1) {\n      var n = x\n      while (n > 0) {\n        prefixes.add(n)\n\
        \        n /= 10\n      }\n    }\n    var maxLen = 0\n    for (y <- arr2) {\n\
        \      var n = y\n      var currLen = 0\n      var temp = n\n      while (temp\
        \ > 0) {\n        temp /= 10\n        currLen += 1\n      }\n      if (currLen\
        \ > maxLen) {\n        var found = false\n        while (n > 0 && currLen >\
        \ maxLen && !found) {\n          if (prefixes.contains(n)) {\n            maxLen\
        \ = currLen\n            found = true\n          } else {\n            n /=\
        \ 10\n            currLen -= 1\n          }\n        }\n      }\n    }\n   \
        \ maxLen\n  }\n}"
      rust: "use std::collections::HashSet;\n\nimpl Solution {\n    pub fn longest_common_prefix(arr1:\
        \ Vec<i32>, arr2: Vec<i32>) -> i32 {\n        let mut prefixes = HashSet::new();\n\
        \        for mut num in arr1 {\n            while num > 0 {\n              \
        \  if !prefixes.insert(num) {\n                    break;\n                }\n\
        \                num /= 10;\n            }\n        }\n\n        let mut max_len\
        \ = 0;\n        for mut num in arr2 {\n            while num > 0 {\n       \
        \         if prefixes.contains(&num) {\n                    let mut len = 0;\n\
        \                    let mut temp = num;\n                    while temp > 0\
        \ {\n                        temp /= 10;\n                        len += 1;\n\
        \                    }\n                    if len > max_len {\n           \
        \             max_len = len;\n                    }\n                    break;\n\
        \                }\n                num /= 10;\n            }\n        }\n \
        \       max_len\n    }\n}"
      racket: "(define/contract (longest-common-prefix arr1 arr2)\n  (-> (listof exact-integer?)\
        \ (listof exact-integer?) exact-integer?)\n  (let ([prefixes (make-hash)])\n\
        \    (for ([num arr1])\n      (let loop ([n num])\n        (when (and (> n 0)\
        \ (not (hash-has-key? prefixes n)))\n          (hash-set! prefixes n #t)\n \
        \         (loop (quotient n 10)))))\n    (for/fold ([max-len 0])\n         \
        \     ([num arr2])\n      (let loop ([n num])\n        (cond\n          [(<=\
        \ n 0) max-len]\n          [(hash-has-key? prefixes n)\n           (let ([len\
        \ (let len-loop ([temp n] [l 0])\n                        (if (= temp 0) l (len-loop\
        \ (quotient temp 10) (+ l 1))))])\n             (max max-len len))]\n      \
        \    [else (loop (quotient n 10))])))))"
      erlang: "-spec longest_common_prefix(Arr1 :: [integer()], Arr2 :: [integer()])\
        \ -> integer().\nlongest_common_prefix(Arr1, Arr2) ->\n  Prefixes = lists:foldl(fun(Num,\
        \ Acc) ->\n    add_prefixes(Num, Acc)\n  end, sets:new([{version, 2}]), Arr1),\n\
        \  lists:foldl(fun(Num, MaxLen) ->\n    erlang:max(MaxLen, find_longest(Num,\
        \ Prefixes))\n  end, 0, Arr2).\n\nadd_prefixes(0, Acc) -> Acc;\nadd_prefixes(Num,\
        \ Acc) ->\n  case sets:is_element(Num, Acc) of\n    true -> Acc;\n    false\
        \ -> add_prefixes(Num div 10, sets:add_element(Num, Acc))\n  end.\n\nfind_longest(0,\
        \ _Prefixes) -> 0;\nfind_longest(Num, Prefixes) ->\n  case sets:is_element(Num,\
        \ Prefixes) of\n    true -> \n      length(integer_to_list(Num));\n    false\
        \ ->\n      find_longest(Num div 10, Prefixes)\n  end."
      elixir: "defmodule Solution do\n  @spec longest_common_prefix(arr1 :: [integer],\
        \ arr2 :: [integer]) :: integer\n  def longest_common_prefix(arr1, arr2) do\n\
        \    prefixes = Enum.reduce(arr1, MapSet.new(), fn num, acc ->\n      add_prefixes(num,\
        \ acc)\n    end)\n\n    Enum.reduce(arr2, 0, fn num, max_len ->\n      max(max_len,\
        \ find_longest_prefix_len(num, prefixes))\n    end)\n  end\n\n  defp add_prefixes(0,\
        \ acc), do: acc\n  defp add_prefixes(num, acc) do\n    if MapSet.member?(acc,\
        \ num) do\n      acc\n    else\n      add_prefixes(div(num, 10), MapSet.put(acc,\
        \ num))\n    end\n  end\n\n  defp find_longest_prefix_len(0, _prefixes), do:\
        \ 0\n  defp find_longest_prefix_len(num, prefixes) do\n    if MapSet.member?(prefixes,\
        \ num) do\n      num |> Integer.to_string() |> byte_size()\n    else\n     \
        \ find_longest_prefix_len(div(num, 10), prefixes)\n    end\n  end\nend"
    approach: To find the longest common prefix between elements of two arrays, we store
      all possible numeric prefixes of each integer from the first array in a Hash Set.
      For each integer in `arr1`, we generate its prefixes by repeatedly dividing the
      number by 10 until it becomes zero, adding every intermediate value to the set.
      This pre-processing allows us to quickly verify whether any numeric sequence from
      the second array exists as a prefix in the first array.
    time_complexity: O((N + M) * D), where N and M are the sizes of arr1 and arr2, respectively,
      and D is the maximum number of digits in an integer (approx 9). For each array
      element, we extract its prefixes and interact with the hash set in O(D) time.
      Total time is linear relative to the total number of digits processed across all
      elements.
    space_complexity: O(N * D), as we store every unique prefix generated from the integers
      in the first array. In the worst case, each integer in arr1 contributes up to
      9 unique integers to the hash set, leading to a space requirement proportional
      to the number of elements in the first array multiplied by the maximum digit length.
    elapsed_time: 650.5117702484131
    model: gemini-3-flash-preview
    generated_at: '2026-05-21 02:49:25 '
---

## Problem #3043: Find the Length of the Longest Common Prefix

**Difficulty:** Medium

**Topics:** Array, Hash Table, String, Trie

## Problem Description

<p>You are given two arrays with <strong>positive</strong> integers <code>arr1</code> and <code>arr2</code>.</p>

<p>A <strong>prefix</strong> of a positive integer is an integer formed by one or more of its digits, starting from its <strong>leftmost</strong> digit. For example, <code>123</code> is a prefix of the integer <code>12345</code>, while <code>234</code> is <strong>not</strong>.</p>

<p>A <strong>common prefix</strong> of two integers <code>a</code> and <code>b</code> is an integer <code>c</code>, such that <code>c</code> is a prefix of both <code>a</code> and <code>b</code>. For example, <code>5655359</code> and <code>56554</code> have common prefixes <code>565</code> and <code>5655</code> while <code>1223</code> and <code>43456</code> <strong>do not</strong> have a common prefix.</p>

<p>You need to find the length of the <strong>longest common prefix</strong> between all pairs of integers <code>(x, y)</code> such that <code>x</code> belongs to <code>arr1</code> and <code>y</code> belongs to <code>arr2</code>.</p>

<p>Return <em>the length of the <strong>longest</strong> common prefix among all pairs</em>.<em> If no common prefix exists among them</em>, <em>return</em> <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr1 = [1,10,100], arr2 = [1000]
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are 3 pairs (arr1[i], arr2[j]):
- The longest common prefix of (1, 1000) is 1.
- The longest common prefix of (10, 1000) is 10.
- The longest common prefix of (100, 1000) is 100.
The longest common prefix is 100 with a length of 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr1 = [1,2,3], arr2 = [4,4,4]
<strong>Output:</strong> 0
<strong>Explanation:</strong> There exists no common prefix for any pair (arr1[i], arr2[j]), hence we return 0.
Note that common prefixes between elements of the same array do not count.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr1.length, arr2.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= arr1[i], arr2[i] &lt;= 10<sup>8</sup></code></li>
</ul>


## Hints

1. Put all the possible prefixes of each element in `arr1` into a HashSet.

2. For all the possible prefixes of each element in `arr2`, check if it exists in the HashSet.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To find the longest common prefix between elements of two arrays, we store all possible numeric prefixes of each integer from the first array in a Hash Set. For each integer in `arr1`, we generate its prefixes by repeatedly dividing the number by 10 until it becomes zero, adding every intermediate value to the set. This pre-processing allows us to quickly verify whether any numeric sequence from the second array exists as a prefix in the first array.

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
    int longestCommonPrefix(std::vector<int>& arr1, std::vector<int>& arr2) {
        std::unordered_set<int> prefixes;
        prefixes.reserve(arr1.size() * 8);
        for (int val : arr1) {
            while (val > 0) {
                prefixes.insert(val);
                val /= 10;
            }
        }

        int maxLen = 0;
        for (int val : arr2) {
            while (val > 0) {
                if (prefixes.count(val)) {
                    int count = 0;
                    int temp = val;
                    while (temp > 0) {
                        temp /= 10;
                        count++;
                    }
                    maxLen = std::max(maxLen, count);
                    break;
                }
                val /= 10;
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

class Solution {
    public int longestCommonPrefix(int[] arr1, int[] arr2) {
        HashSet<Integer> prefixes = new HashSet<>();
        for (int val : arr1) {
            while (val > 0) {
                prefixes.add(val);
                val /= 10;
            }
        }

        int maxLen = 0;
        for (int val : arr2) {
            while (val > 0) {
                if (prefixes.contains(val)) {
                    int count = 0;
                    int temp = val;
                    while (temp > 0) {
                        temp /= 10;
                        count++;
                    }
                    maxLen = Math.max(maxLen, count);
                    break;
                }
                val /= 10;
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
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        prefixes = set()
        for val in arr1:
            while val > 0:
                prefixes.add(val)
                val //= 10

        max_len = 0
        for val in arr2:
            while val > 0:
                if val in prefixes:
                    curr_len = len(str(val))
                    if curr_len > max_len:
                        max_len = curr_len
                    break
                val //= 10
        return max_len
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        for val in arr1:
            while val > 0:
                prefixes.add(val)
                val //= 10

        max_len = 0
        for val in arr2:
            while val > 0:
                if val in prefixes:
                    curr_len = len(str(val))
                    if curr_len > max_len:
                        max_len = curr_len
                    break
                val //= 10
        return max_len
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdbool.h>
#include <string.h>

#define TABLE_SIZE 1300021
static int hash_table[TABLE_SIZE];

void insert_prefix(int val) {
    unsigned int h = (unsigned int)val % TABLE_SIZE;
    while (hash_table[h] != 0) {
        if (hash_table[h] == val) return;
        h = (h + 1) % TABLE_SIZE;
    }
    hash_table[h] = val;
}

bool find_prefix(int val) {
    unsigned int h = (unsigned int)val % TABLE_SIZE;
    while (hash_table[h] != 0) {
        if (hash_table[h] == val) return true;
        h = (h + 1) % TABLE_SIZE;
    }
    return false;
}

int longestCommonPrefix(int* arr1, int arr1Size, int* arr2, int arr2Size) {
    memset(hash_table, 0, sizeof(hash_table));
    for (int i = 0; i < arr1Size; i++) {
        int val = arr1[i];
        while (val > 0) {
            insert_prefix(val);
            val /= 10;
        }
    }

    int maxLen = 0;
    for (int i = 0; i < arr2Size; i++) {
        int val = arr2[i];
        while (val > 0) {
            if (find_prefix(val)) {
                int count = 0;
                int temp = val;
                while (temp > 0) {
                    temp /= 10;
                    count++;
                }
                if (count > maxLen) maxLen = count;
                break;
            }
            val /= 10;
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
    public int LongestCommonPrefix(int[] arr1, int[] arr2) {
        HashSet<int> prefixes = new HashSet<int>();
        foreach (int val in arr1) {
            int temp = val;
            while (temp > 0) {
                prefixes.Add(temp);
                temp /= 10;
            }
        }

        int maxLength = 0;
        foreach (int val in arr2) {
            int temp = val;
            while (temp > 0) {
                if (prefixes.Contains(temp)) {
                    int currentLen = temp.ToString().Length;
                    if (currentLen > maxLength) {
                        maxLength = currentLen;
                    }
                    break;
                }
                temp /= 10;
            }
        }

        return maxLength;
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
 * @return {number}
 */
var longestCommonPrefix = function(arr1, arr2) {
    const prefixes = new Set();
    for (let val of arr1) {
        let temp = val;
        while (temp > 0) {
            prefixes.add(temp);
            temp = Math.floor(temp / 10);
        }
    }

    let maxLength = 0;
    for (let val of arr2) {
        let temp = val;
        while (temp > 0) {
            if (prefixes.has(temp)) {
                const currentLen = temp.toString().length;
                if (currentLen > maxLength) {
                    maxLength = currentLen;
                }
                break;
            }
            temp = Math.floor(temp / 10);
        }
    }

    return maxLength;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function longestCommonPrefix(arr1: number[], arr2: number[]): number {
    const prefixes: Set<number> = new Set();
    for (let val of arr1) {
        let temp = val;
        while (temp > 0) {
            prefixes.add(temp);
            temp = Math.floor(temp / 10);
        }
    }

    let maxLength: number = 0;
    for (let val of arr2) {
        let temp = val;
        while (temp > 0) {
            if (prefixes.has(temp)) {
                const currentLen = temp.toString().length;
                if (currentLen > maxLength) {
                    maxLength = currentLen;
                }
                break;
            }
            temp = Math.floor(temp / 10);
        }
    }

    return maxLength;
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
     * @return Integer
     */
    function longestCommonPrefix($arr1, $arr2) {
        $prefixes = [];
        foreach ($arr1 as $val) {
            $temp = $val;
            while ($temp > 0) {
                $prefixes[$temp] = true;
                $temp = (int)($temp / 10);
            }
        }

        $maxLength = 0;
        foreach ($arr2 as $val) {
            $temp = $val;
            while ($temp > 0) {
                if (isset($prefixes[$temp])) {
                    $currentLen = strlen((string)$temp);
                    if ($currentLen > $maxLength) {
                        $maxLength = $currentLen;
                    }
                    break;
                }
                $temp = (int)($temp / 10);
            }
        }

        return $maxLength;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func longestCommonPrefix(_ arr1: [Int], _ arr2: [Int]) -> Int {
        var prefixes = Set<Int>()
        for val in arr1 {
            var temp = val
            while temp > 0 {
                prefixes.insert(temp)
                temp /= 10
            }
        }

        var maxLength = 0
        for val in arr2 {
            var temp = val
            while temp > 0 {
                if prefixes.contains(temp) {
                    let currentLen = String(temp).count
                    if currentLen > maxLength {
                        maxLength = currentLen
                    }
                    break
                }
                temp /= 10
            }
        }

        return maxLength
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun longestCommonPrefix(arr1: IntArray, arr2: IntArray): Int {
        val prefixes = HashSet<Int>()
        for (x in arr1) {
            var n = x
            while (n > 0) {
                prefixes.add(n)
                n /= 10
            }
        }
        var maxLen = 0
        for (y in arr2) {
            var n = y
            var currLen = 0
            var temp = n
            while (temp > 0) {
                temp /= 10
                currLen++
            }
            if (currLen <= maxLen) continue
            while (n > 0 && currLen > maxLen) {
                if (prefixes.contains(n)) {
                    maxLen = currLen
                    break
                }
                n /= 10
                currLen--
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
  int longestCommonPrefix(List<int> arr1, List<int> arr2) {
    final prefixes = <int>{};
    for (var x in arr1) {
      var n = x;
      while (n > 0) {
        prefixes.add(n);
        n ~/= 10;
      }
    }
    int maxLen = 0;
    for (var y in arr2) {
      var n = y;
      int currLen = 0;
      var temp = n;
      while (temp > 0) {
        temp ~/= 10;
        currLen++;
      }
      if (currLen <= maxLen) continue;
      while (n > 0 && currLen > maxLen) {
        if (prefixes.contains(n)) {
          maxLen = currLen;
          break;
        }
        n ~/= 10;
        currLen--;
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
func longestCommonPrefix(arr1 []int, arr2 []int) int {
    prefixes := make(map[int]bool)
    for _, x := range arr1 {
        n := x
        for n > 0 {
            prefixes[n] = true
            n /= 10
        }
    }
    maxLen := 0
    for _, y := range arr2 {
        n := y
        currLen := 0
        temp := n
        for temp > 0 {
            temp /= 10
            currLen++
        }
        if currLen <= maxLen {
            continue
        }
        for n > 0 && currLen > maxLen {
            if _, found := prefixes[n]; found {
                maxLen = currLen
                break
            }
            n /= 10
            currLen--
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
def longest_common_prefix(arr1, arr2)
  prefixes = {}
  arr1.each do |x|
    n = x
    while n > 0
      prefixes[n] = true
      n /= 10
    end
  end
  max_len = 0
  arr2.each do |y|
    n = y
    curr_len = 0
    temp = n
    while temp > 0
      temp /= 10
      curr_len += 1
    end
    next if curr_len <= max_len
    while n > 0 && curr_len > max_len
      if prefixes[n]
        max_len = curr_len
        break
      end
      n /= 10
      curr_len -= 1
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
import scala.collection.mutable

object Solution {
  def longestCommonPrefix(arr1: Array[Int], arr2: Array[Int]): Int = {
    val prefixes = mutable.HashSet[Int]()
    for (x <- arr1) {
      var n = x
      while (n > 0) {
        prefixes.add(n)
        n /= 10
      }
    }
    var maxLen = 0
    for (y <- arr2) {
      var n = y
      var currLen = 0
      var temp = n
      while (temp > 0) {
        temp /= 10
        currLen += 1
      }
      if (currLen > maxLen) {
        var found = false
        while (n > 0 && currLen > maxLen && !found) {
          if (prefixes.contains(n)) {
            maxLen = currLen
            found = true
          } else {
            n /= 10
            currLen -= 1
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
use std::collections::HashSet;

impl Solution {
    pub fn longest_common_prefix(arr1: Vec<i32>, arr2: Vec<i32>) -> i32 {
        let mut prefixes = HashSet::new();
        for mut num in arr1 {
            while num > 0 {
                if !prefixes.insert(num) {
                    break;
                }
                num /= 10;
            }
        }

        let mut max_len = 0;
        for mut num in arr2 {
            while num > 0 {
                if prefixes.contains(&num) {
                    let mut len = 0;
                    let mut temp = num;
                    while temp > 0 {
                        temp /= 10;
                        len += 1;
                    }
                    if len > max_len {
                        max_len = len;
                    }
                    break;
                }
                num /= 10;
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
(define/contract (longest-common-prefix arr1 arr2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let ([prefixes (make-hash)])
    (for ([num arr1])
      (let loop ([n num])
        (when (and (> n 0) (not (hash-has-key? prefixes n)))
          (hash-set! prefixes n #t)
          (loop (quotient n 10)))))
    (for/fold ([max-len 0])
              ([num arr2])
      (let loop ([n num])
        (cond
          [(<= n 0) max-len]
          [(hash-has-key? prefixes n)
           (let ([len (let len-loop ([temp n] [l 0])
                        (if (= temp 0) l (len-loop (quotient temp 10) (+ l 1))))])
             (max max-len len))]
          [else (loop (quotient n 10))])))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec longest_common_prefix(Arr1 :: [integer()], Arr2 :: [integer()]) -> integer().
longest_common_prefix(Arr1, Arr2) ->
  Prefixes = lists:foldl(fun(Num, Acc) ->
    add_prefixes(Num, Acc)
  end, sets:new([{version, 2}]), Arr1),
  lists:foldl(fun(Num, MaxLen) ->
    erlang:max(MaxLen, find_longest(Num, Prefixes))
  end, 0, Arr2).

add_prefixes(0, Acc) -> Acc;
add_prefixes(Num, Acc) ->
  case sets:is_element(Num, Acc) of
    true -> Acc;
    false -> add_prefixes(Num div 10, sets:add_element(Num, Acc))
  end.

find_longest(0, _Prefixes) -> 0;
find_longest(Num, Prefixes) ->
  case sets:is_element(Num, Prefixes) of
    true -> 
      length(integer_to_list(Num));
    false ->
      find_longest(Num div 10, Prefixes)
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec longest_common_prefix(arr1 :: [integer], arr2 :: [integer]) :: integer
  def longest_common_prefix(arr1, arr2) do
    prefixes = Enum.reduce(arr1, MapSet.new(), fn num, acc ->
      add_prefixes(num, acc)
    end)

    Enum.reduce(arr2, 0, fn num, max_len ->
      max(max_len, find_longest_prefix_len(num, prefixes))
    end)
  end

  defp add_prefixes(0, acc), do: acc
  defp add_prefixes(num, acc) do
    if MapSet.member?(acc, num) do
      acc
    else
      add_prefixes(div(num, 10), MapSet.put(acc, num))
    end
  end

  defp find_longest_prefix_len(0, _prefixes), do: 0
  defp find_longest_prefix_len(num, prefixes) do
    if MapSet.member?(prefixes, num) do
      num |> Integer.to_string() |> byte_size()
    else
      find_longest_prefix_len(div(num, 10), prefixes)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O((N + M) * D), where N and M are the sizes of arr1 and arr2, respectively, and D is the maximum number of digits in an integer (approx 9). For each array element, we extract its prefixes and interact with the hash set in O(D) time. Total time is linear relative to the total number of digits processed across all elements.
- **Space Complexity:** O(N * D), as we store every unique prefix generated from the integers in the first array. In the worst case, each integer in arr1 contributes up to 9 unique integers to the hash set, leading to a space requirement proportional to the number of elements in the first array multiplied by the maximum digit length.
