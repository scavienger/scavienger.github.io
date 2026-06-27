---
layout: post
title: "Find the Maximum Number of Elements in Subset"
date: 2026-06-27 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Enumeration"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int maximumLength(vector<int>& nums) {\n\
        \        std::map<long long, int> counts;\n        for (int x : nums) counts[x]++;\n\
        \n        int max_len = 1;\n        if (counts.count(1)) {\n            int\
        \ c = counts[1];\n            max_len = (c % 2 == 0) ? c - 1 : c;\n        }\n\
        \n        for (auto const& [x, count] : counts) {\n            if (x == 1) continue;\n\
        \            long long curr = x;\n            int current_len = 0;\n       \
        \     bool peak_found = false;\n            while (counts[curr] >= 2) {\n  \
        \              long long nxt = curr * curr;\n                if (nxt <= 1000000000\
        \ && counts.count(nxt)) {\n                    current_len += 2;\n         \
        \           curr = nxt;\n                } else {\n                    current_len\
        \ += 1;\n                    peak_found = true;\n                    break;\n\
        \                }\n            }\n            if (!peak_found) {\n        \
        \        current_len += 1;\n            }\n            max_len = std::max(max_len,\
        \ current_len);\n        }\n\n        return max_len;\n    }\n};"
      java: "class Solution {\n    public int maximumLength(int[] nums) {\n        Map<Long,\
        \ Integer> counts = new HashMap<>();\n        for (int x : nums) {\n       \
        \     long val = (long) x;\n            counts.put(val, counts.getOrDefault(val,\
        \ 0) + 1);\n        }\n\n        int maxLen = 1;\n        if (counts.containsKey(1L))\
        \ {\n            int c = counts.get(1L);\n            maxLen = (c % 2 == 0)\
        \ ? c - 1 : c;\n        }\n\n        for (long x : counts.keySet()) {\n    \
        \        if (x == 1) continue;\n            int currentLen = 0;\n          \
        \  long curr = x;\n            boolean peakFound = false;\n            while\
        \ (counts.getOrDefault(curr, 0) >= 2) {\n                long nxt = curr * curr;\n\
        \                if (nxt <= 1000000000 && counts.containsKey(nxt)) {\n     \
        \               currentLen += 2;\n                    curr = nxt;\n        \
        \        } else {\n                    currentLen += 1;\n                  \
        \  peakFound = true;\n                    break;\n                }\n      \
        \      }\n            if (!peakFound) {\n                currentLen += 1;\n\
        \            }\n            maxLen = Math.max(maxLen, currentLen);\n       \
        \ }\n\n        return maxLen;\n    }\n}"
      python: "import collections\n\nclass Solution(object):\n    def maximumLength(self,\
        \ nums):\n        \"\"\"\n        :type nums: List[int]\n        :rtype: int\n\
        \        \"\"\"\n        counts = collections.Counter(nums)\n        res = 1\n\
        \        if 1 in counts:\n            c = counts[1]\n            res = c if\
        \ c % 2 != 0 else c - 1\n\n        for x in counts.keys():\n            if x\
        \ == 1: continue\n            curr_len = 0\n            curr = x\n         \
        \   peak_found = False\n            while counts[curr] >= 2:\n             \
        \   nxt = curr * curr\n                if nxt in counts:\n                 \
        \   curr_len += 2\n                    curr = nxt\n                else:\n \
        \                   curr_len += 1\n                    peak_found = True\n \
        \                   break\n            if not peak_found:\n                curr_len\
        \ += 1\n            res = max(res, curr_len)\n\n        return res"
      python3: "from collections import Counter\n\nclass Solution:\n    def maximumLength(self,\
        \ nums: List[int]) -> int:\n        counts = Counter(nums)\n        res = 1\n\
        \        if 1 in counts:\n            c = counts[1]\n            res = c if\
        \ c % 2 != 0 else c - 1\n\n        for x in counts.keys():\n            if x\
        \ == 1: continue\n            curr_len = 0\n            curr = x\n         \
        \   peak_found = False\n            while counts[curr] >= 2:\n             \
        \   nxt = curr * curr\n                if nxt in counts:\n                 \
        \   curr_len += 2\n                    curr = nxt\n                else:\n \
        \                   curr_len += 1\n                    peak_found = True\n \
        \                   break\n            if not peak_found:\n                curr_len\
        \ += 1\n            res = max(res, curr_len)\n\n        return res"
      c: "#include <stdlib.h>\n#include <math.h>\n\ntypedef struct {\n    long long\
        \ val;\n    int freq;\n} Pair;\n\nint comparePairs(const void* a, const void*\
        \ b) {\n    long long v1 = ((Pair*)a)->val;\n    long long v2 = ((Pair*)b)->val;\n\
        \    if (v1 < v2) return -1;\n    if (v1 > v2) return 1;\n    return 0;\n}\n\
        \nint compareInts(const void* a, const void* b) {\n    int v1 = *(const int*)a;\n\
        \    int v2 = *(const int*)b;\n    if (v1 < v2) return -1;\n    if (v1 > v2)\
        \ return 1;\n    return 0;\n}\n\nint find_freq(long long val, Pair* pairs, int\
        \ size) {\n    if (val > 1000000000) return 0;\n    int low = 0, high = size\
        \ - 1;\n    while (low <= high) {\n        int mid = low + (high - low) / 2;\n\
        \        if (pairs[mid].val == val) return pairs[mid].freq;\n        if (pairs[mid].val\
        \ < val) low = mid + 1;\n        else high = mid - 1;\n    }\n    return 0;\n\
        }\n\nint maximumLength(int* nums, int numsSize) {\n    if (numsSize == 0) return\
        \ 0;\n    qsort(nums, numsSize, sizeof(int), compareInts);\n\n    Pair* pairs\
        \ = (Pair*)malloc(sizeof(Pair) * numsSize);\n    int unique_count = 0;\n   \
        \ pairs[0].val = nums[0];\n    pairs[0].freq = 1;\n    unique_count = 1;\n \
        \   for (int i = 1; i < numsSize; i++) {\n        if (nums[i] == nums[i - 1])\
        \ {\n            pairs[unique_count - 1].freq++;\n        } else {\n       \
        \     pairs[unique_count].val = nums[i];\n            pairs[unique_count].freq\
        \ = 1;\n            unique_count++;\n        }\n    }\n\n    int max_len = 1;\n\
        \    int start_idx = 0;\n    if (pairs[0].val == 1) {\n        int c = pairs[0].freq;\n\
        \        max_len = (c % 2 == 0) ? c - 1 : c;\n        start_idx = 1;\n    }\n\
        \n    for (int i = start_idx; i < unique_count; i++) {\n        long long curr\
        \ = pairs[i].val;\n        int current_len = 0;\n        int peak_found = 0;\n\
        \        while (find_freq(curr, pairs, unique_count) >= 2) {\n            long\
        \ long nxt = curr * curr;\n            if (find_freq(nxt, pairs, unique_count)\
        \ >= 1) {\n                current_len += 2;\n                curr = nxt;\n\
        \            } else {\n                current_len += 1;\n                peak_found\
        \ = 1;\n                break;\n            }\n        }\n        if (!peak_found)\
        \ {\n            current_len += 1;\n        }\n        if (current_len > max_len)\
        \ max_len = current_len;\n    }\n\n    free(pairs);\n    return max_len;\n}"
      csharp: '// Generation failed for C#

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      javascript: '// Generation failed for JavaScript

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      typescript: '// Generation failed for TypeScript

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      php: '// Generation failed for PHP

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      swift: '// Generation failed for Swift

        // Reason: Error: 503 UNAVAILABLE. {''error'': {''code'': 503, ''message'':
        ''This model is currently experiencing high demand. Spikes in demand are usually
        temporary. Please try again later.'', ''status'': ''UNAVAILABLE''}}'
      kotlin: "class Solution {\n    fun maximumLength(nums: IntArray): Int {\n    \
        \    val counts = mutableMapOf<Long, Int>()\n        for (num in nums) {\n \
        \           val n = num.toLong()\n            counts[n] = counts.getOrDefault(n,\
        \ 0) + 1\n        }\n\n        var maxLen = 1\n        if (counts.containsKey(1L))\
        \ {\n            val c1 = counts[1L]!!\n            if (c1 % 2 == 0) {\n   \
        \             maxLen = c1 - 1\n            } else {\n                maxLen\
        \ = c1\n            }\n        }\n\n        for (x in counts.keys) {\n     \
        \       if (x == 1L) continue\n\n            var currLen = 0\n            var\
        \ curr = x\n            while (counts.getOrDefault(curr, 0) >= 2) {\n      \
        \          currLen += 2\n                val nextCurr = curr * curr\n      \
        \          curr = nextCurr\n                if (curr > 1000000000L) break\n\
        \            }\n\n            if (counts.getOrDefault(curr, 0) >= 1) {\n   \
        \             currLen += 1\n            } else {\n                currLen -=\
        \ 1\n            }\n\n            if (currLen > maxLen) {\n                maxLen\
        \ = currLen\n            }\n        }\n\n        return maxLen\n    }\n}"
      dart: "class Solution {\n  int maximumLength(List<int> nums) {\n    Map<int, int>\
        \ counts = {};\n    for (var num in nums) {\n      counts[num] = (counts[num]\
        \ ?? 0) + 1;\n    }\n\n    int maxLen = 1;\n    if (counts.containsKey(1)) {\n\
        \      int c1 = counts[1]!;\n      if (c1 % 2 == 0) {\n        maxLen = c1 -\
        \ 1;\n      } else {\n        maxLen = c1;\n      }\n    }\n\n    for (var x\
        \ in counts.keys) {\n      if (x == 1) continue;\n\n      int currLen = 0;\n\
        \      int curr = x;\n      while ((counts[curr] ?? 0) >= 2) {\n        currLen\
        \ += 2;\n        int nextCurr = curr * curr;\n        curr = nextCurr;\n   \
        \     if (curr > 1000000000) break;\n      }\n\n      if ((counts[curr] ?? 0)\
        \ >= 1) {\n        currLen += 1;\n      } else {\n        currLen -= 1;\n  \
        \    }\n\n      if (currLen > maxLen) {\n        maxLen = currLen;\n      }\n\
        \    }\n\n    return maxLen;\n  }\n}"
      go: "func maximumLength(nums []int) int {\n\tcounts := make(map[int64]int)\n\t\
        for _, num := range nums {\n\t\tcounts[int64(num)]++\n\t}\n\n\tmaxLen := 1\n\
        \tif c1, ok := counts[1]; ok {\n\t\tif c1%2 == 0 {\n\t\t\tmaxLen = c1 - 1\n\t\
        \t} else {\n\t\t\tmaxLen = c1\n\t\t}\n\t}\n\n\tfor x, _ := range counts {\n\t\
        \tif x == 1 {\n\t\t\tcontinue\n\t\t}\n\n\t\tcurrLen := 0\n\t\tcurr := x\n\t\t\
        for counts[curr] >= 2 {\n\t\t\tcurrLen += 2\n\t\t\tnextCurr := curr * curr\n\
        \t\t\tcurr = nextCurr\n\t\t\tif curr > 1000000000 {\n\t\t\t\tbreak\n\t\t\t}\n\
        \t\t}\n\n\t\tif counts[curr] >= 1 {\n\t\t\tcurrLen += 1\n\t\t} else {\n\t\t\t\
        currLen -= 1\n\t\t}\n\n\t\tif currLen > maxLen {\n\t\t\tmaxLen = currLen\n\t\
        \t}\n\t}\n\n\treturn maxLen\n}"
      ruby: "def maximum_length(nums)\n  counts = Hash.new(0)\n  nums.each { |num| counts[num]\
        \ += 1 }\n\n  max_len = 1\n  if counts[1] > 0\n    if counts[1] % 2 == 0\n \
        \     max_len = counts[1] - 1\n    else\n      max_len = counts[1]\n    end\n\
        \  end\n\n  counts.each_key do |x|\n    next if x == 1\n\n    curr_len = 0\n\
        \    curr = x\n    while counts[curr] >= 2\n      curr_len += 2\n      next_curr\
        \ = curr * curr\n      curr = next_curr\n      break if curr > 1000000000\n\
        \    end\n\n    if counts[curr] >= 1\n      curr_len += 1\n    else\n      curr_len\
        \ -= 1\n    end\n\n    max_len = curr_len if curr_len > max_len\n  end\n\n \
        \ max_len\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n  def maximumLength(nums:\
        \ Array[Int]): Int = {\n    val counts = mutable.Map[Long, Int]().withDefaultValue(0)\n\
        \    for (num <- nums) {\n      counts(num.toLong) += 1\n    }\n\n    var maxLen\
        \ = 1\n    if (counts.contains(1L)) {\n      val c1 = counts(1L)\n      if (c1\
        \ % 2 == 0) {\n        maxLen = c1 - 1\n      } else {\n        maxLen = c1\n\
        \      }\n    }\n\n    for (x <- counts.keys) {\n      if (x != 1L) {\n    \
        \    var currLen = 0\n        var curr = x\n        var keepGoing = true\n \
        \       while (keepGoing && counts.getOrElse(curr, 0) >= 2) {\n          currLen\
        \ += 2\n          val nextCurr = curr * curr\n          curr = nextCurr\n  \
        \        if (curr > 1000000000L) {\n            keepGoing = false\n        \
        \  }\n        }\n\n        if (counts.getOrElse(curr, 0) >= 1) {\n         \
        \ currLen += 1\n        } else {\n          currLen -= 1\n        }\n\n    \
        \    if (currLen > maxLen) {\n          maxLen = currLen\n        }\n      }\n\
        \    }\n\n    maxLen\n  }\n}"
      rust: "use std::collections::HashMap;\n\nimpl Solution {\n    pub fn maximum_length(nums:\
        \ Vec<i32>) -> i32 {\n        let mut counts: HashMap<i64, i64> = HashMap::new();\n\
        \        for &num in &nums {\n            *counts.entry(num as i64).or_insert(0)\
        \ += 1;\n        }\n\n        let mut ans = 1;\n        if let Some(&c1) = counts.get(&1i64)\
        \ {\n            ans = if c1 % 2 == 1 { c1 as i32 } else { (c1 - 1) as i32 };\n\
        \        }\n\n        for (&val, _) in &counts {\n            if val == 1 {\n\
        \                continue;\n            }\n            let mut res = 0;\n  \
        \          let mut curr = val;\n            loop {\n                let count\
        \ = *counts.get(&curr).unwrap_or(&0);\n                if count >= 2 {\n   \
        \                 res += 2;\n                    if curr > 31622 {\n       \
        \                 res -= 1;\n                        break;\n              \
        \      }\n                    curr = curr * curr;\n                } else if\
        \ count == 1 {\n                    res += 1;\n                    break;\n\
        \                } else {\n                    res -= 1;\n                 \
        \   break;\n                }\n            }\n            if res > ans {\n \
        \               ans = res as i32;\n            }\n        }\n        ans\n \
        \   }\n}"
      racket: "(define/contract (maximum-length nums)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let ([counts (make-hash)])\n    (for ([num nums])\n  \
        \    (hash-update! counts num (lambda (x) (+ x 1)) 0))\n    (let* ([c1 (hash-ref\
        \ counts 1 0)]\n           [ans-initial (if (zero? c1) 1 (if (odd? c1) c1 (-\
        \ c1 1)))])\n      (foldl (lambda (val acc)\n               (if (= val 1)\n\
        \                   acc\n                   (max acc\n                     \
        \   (let loop ([curr val] [res 0])\n                          (let ([count (hash-ref\
        \ counts curr 0)])\n                            (cond\n                    \
        \          [(>= count 2)\n                               (if (> curr 31622)\n\
        \                                   (+ res 1)\n                            \
        \       (loop (* curr curr) (+ res 2)))]\n                              [(=\
        \ count 1)\n                               (+ res 1)]\n                    \
        \          [else\n                               (- res 1)]))))))\n        \
        \     ans-initial\n             (hash-keys counts)))))"
      erlang: "-spec maximum_length(Nums :: [integer()]) -> integer().\nmaximum_length(Nums)\
        \ ->\n  Counts = lists:foldl(fun(X, Acc) ->\n    maps:put(X, maps:get(X, Acc,\
        \ 0) + 1, Acc)\n  end, #{}, Nums),\n  C1 = maps:get(1, Counts, 0),\n  AnsInitial\
        \ = if C1 == 0 -> 1;\n                  C1 rem 2 == 1 -> C1;\n             \
        \     true -> C1 - 1\n               end,\n  lists:foldl(fun(Val, MaxAns) ->\n\
        \    if Val == 1 -> MaxAns;\n       true ->\n         Res = calculate(Val, Counts,\
        \ 0),\n         if Res > MaxAns -> Res; true -> MaxAns end\n    end\n  end,\
        \ AnsInitial, maps:keys(Counts)).\n\ncalculate(Curr, Counts, Res) ->\n  Count\
        \ = maps:get(Curr, Counts, 0),\n  if Count >= 2 ->\n    if Curr > 31622 -> Res\
        \ + 1;\n       true -> calculate(Curr * Curr, Counts, Res + 2)\n    end;\n \
        \   Count == 1 -> Res + 1;\n    true -> Res - 1\n  end."
      elixir: "defmodule Solution do\n  @spec maximum_length(nums :: [integer]) :: integer\n\
        \  def maximum_length(nums) do\n    counts = Enum.reduce(nums, %{}, fn x, acc\
        \ ->\n      Map.update(acc, x, 1, &(&1 + 1))\n    end)\n\n    c1 = Map.get(counts,\
        \ 1, 0)\n    ans_initial = if c1 == 0, do: 1, else: (if rem(c1, 2) == 1, do:\
        \ c1, else: c1 - 1)\n\n    Enum.reduce(counts, ans_initial, fn {val, _count},\
        \ max_ans ->\n      if val == 1 do\n        max_ans\n      else\n        res\
        \ = calculate(val, counts, 0)\n        max(max_ans, res)\n      end\n    end)\n\
        \  end\n\n  defp calculate(curr, counts, res) do\n    count = Map.get(counts,\
        \ curr, 0)\n    cond do\n      count >= 2 ->\n        if curr > 31622 do\n \
        \         res + 1\n        else\n          calculate(curr * curr, counts, res\
        \ + 2)\n        end\n      count == 1 ->\n        res + 1\n      true ->\n \
        \       res - 1\n    end\n  end\nend"
    approach: 'The core of the problem lies in recognizing that the pattern follows
      an odd-length sequence of powers: $x^{2^0}, x^{2^1}, \dots, x^{2^n}, \dots, x^{2^1},
      x^{2^0}$. This means every element except the central peak ($x^{2^n}$) must appear
      at least twice in the subset, while the peak element must appear at least once.
      For the special case where $x=1$, any odd number of 1s satisfies the condition
      because $1^2=1$, so we simply find the largest odd frequency of 1s available in
      the input array.


      For elements $x > 1$, we iterate through each unique number as a potential base
      $x$ and traverse the square-chain $x, x^2, x^4, \dots$ using a frequency map.
      At each step, if the current element has a frequency $\ge 2$ and its square exists
      in the array, we add two to our current sequence length and proceed to the square.
      If the current element has a frequency of 1 (or its square does not exist), it
      must serve as the peak of the sequence, adding one to the length and terminating
      the chain. Because the powers grow exponentially ($x^{2^n}$), the chain length
      is extremely small ($O(\log \log \text{max}(nums))$), making the brute-force traversal
      efficient.'
    time_complexity: O(N \log N) or O(N) depending on the language's frequency map implementation.
      Sorting the array or using a balanced BST map (like C++ `std::map`) results in
      O(N \log N). Using a hash map (like Python `Counter` or Java `HashMap`) results
      in O(N) average time complexity. The chain traversal takes O(log log M) per unique
      element, where M is the maximum value in nums.
    space_complexity: O(N) to store the frequency map or the unique element pairs extracted
      from the input array.
    elapsed_time: 678.6774129867554
    model: gemini-3-flash-preview
    generated_at: '2026-06-27 02:57:03 '
---

## Problem #3020: Find the Maximum Number of Elements in Subset

**Difficulty:** Medium

**Topics:** Array, Hash Table, Enumeration

## Problem Description

<p>You are given an array of <strong>positive</strong> integers <code>nums</code>.</p>

<p>You need to select a <span data-keyword="subset">subset</span> of <code>nums</code> which satisfies the following condition:</p>

<ul>
	<li>You can place the selected elements in a <strong>0-indexed</strong> array such that it follows the pattern: <code>[x, x<sup>2</sup>, x<sup>4</sup>, ..., x<sup>k/2</sup>, x<sup>k</sup>, x<sup>k/2</sup>, ..., x<sup>4</sup>, x<sup>2</sup>, x]</code> (<strong>Note</strong> that <code>k</code> can be be any <strong>non-negative</strong> power of <code>2</code>). For example, <code>[2, 4, 16, 4, 2]</code> and <code>[3, 9, 3]</code> follow the pattern while <code>[2, 4, 8, 4, 2]</code> does not.</li>
</ul>

<p>Return <em>the <strong>maximum</strong> number of elements in a subset that satisfies these conditions.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,4,1,2,2]
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can select the subset {4,2,2}, which can be placed in the array as [2,4,2] which follows the pattern and 2<sup>2</sup> == 4. Hence the answer is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,2,4]
<strong>Output:</strong> 1
<strong>Explanation:</strong> We can select the subset {1}, which can be placed in the array as [1] which follows the pattern. Hence the answer is 1. Note that we could have also selected the subsets {2}, {3}, or {4}, there may be multiple subsets which provide the same answer. 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. We can select an odd number of `1`’s.

2. Put all the values into a HashSet. We can start from each `x > 1` as the smallest chosen value and we can find the longest subset by checking the new values (which are the square of the previous value) in the set by brute force.

3. Note when `x > 1`, `x^2`, `x^4`, `x^8`, … increases very fast, the longest subset with smallest value x cannot be very long. (The length is `O(log(log(10^9)))`.

4. Hence we can directly check all lengths less than `10` for all values of `x`.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The core of the problem lies in recognizing that the pattern follows an odd-length sequence of powers: $x^{2^0}, x^{2^1}, \dots, x^{2^n}, \dots, x^{2^1}, x^{2^0}$. This means every element except the central peak ($x^{2^n}$) must appear at least twice in the subset, while the peak element must appear at least once. For the special case where $x=1$, any odd number of 1s satisfies the condition because $1^2=1$, so we simply find the largest odd frequency of 1s available in the input array.

For elements $x > 1$, we iterate through each unique number as a potential base $x$ and traverse the square-chain $x, x^2, x^4, \dots$ using a frequency map. At each step, if the current element has a frequency $\ge 2$ and its square exists in the array, we add two to our current sequence length and proceed to the square. If the current element has a frequency of 1 (or its square does not exist), it must serve as the peak of the sequence, adding one to the length and terminating the chain. Because the powers grow exponentially ($x^{2^n}$), the chain length is extremely small ($O(\log \log \text{max}(nums))$), making the brute-force traversal efficient.

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
    int maximumLength(vector<int>& nums) {
        std::map<long long, int> counts;
        for (int x : nums) counts[x]++;

        int max_len = 1;
        if (counts.count(1)) {
            int c = counts[1];
            max_len = (c % 2 == 0) ? c - 1 : c;
        }

        for (auto const& [x, count] : counts) {
            if (x == 1) continue;
            long long curr = x;
            int current_len = 0;
            bool peak_found = false;
            while (counts[curr] >= 2) {
                long long nxt = curr * curr;
                if (nxt <= 1000000000 && counts.count(nxt)) {
                    current_len += 2;
                    curr = nxt;
                } else {
                    current_len += 1;
                    peak_found = true;
                    break;
                }
            }
            if (!peak_found) {
                current_len += 1;
            }
            max_len = std::max(max_len, current_len);
        }

        return max_len;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maximumLength(int[] nums) {
        Map<Long, Integer> counts = new HashMap<>();
        for (int x : nums) {
            long val = (long) x;
            counts.put(val, counts.getOrDefault(val, 0) + 1);
        }

        int maxLen = 1;
        if (counts.containsKey(1L)) {
            int c = counts.get(1L);
            maxLen = (c % 2 == 0) ? c - 1 : c;
        }

        for (long x : counts.keySet()) {
            if (x == 1) continue;
            int currentLen = 0;
            long curr = x;
            boolean peakFound = false;
            while (counts.getOrDefault(curr, 0) >= 2) {
                long nxt = curr * curr;
                if (nxt <= 1000000000 && counts.containsKey(nxt)) {
                    currentLen += 2;
                    curr = nxt;
                } else {
                    currentLen += 1;
                    peakFound = true;
                    break;
                }
            }
            if (!peakFound) {
                currentLen += 1;
            }
            maxLen = Math.max(maxLen, currentLen);
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
import collections

class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = collections.Counter(nums)
        res = 1
        if 1 in counts:
            c = counts[1]
            res = c if c % 2 != 0 else c - 1

        for x in counts.keys():
            if x == 1: continue
            curr_len = 0
            curr = x
            peak_found = False
            while counts[curr] >= 2:
                nxt = curr * curr
                if nxt in counts:
                    curr_len += 2
                    curr = nxt
                else:
                    curr_len += 1
                    peak_found = True
                    break
            if not peak_found:
                curr_len += 1
            res = max(res, curr_len)

        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counts = Counter(nums)
        res = 1
        if 1 in counts:
            c = counts[1]
            res = c if c % 2 != 0 else c - 1

        for x in counts.keys():
            if x == 1: continue
            curr_len = 0
            curr = x
            peak_found = False
            while counts[curr] >= 2:
                nxt = curr * curr
                if nxt in counts:
                    curr_len += 2
                    curr = nxt
                else:
                    curr_len += 1
                    peak_found = True
                    break
            if not peak_found:
                curr_len += 1
            res = max(res, curr_len)

        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <math.h>

typedef struct {
    long long val;
    int freq;
} Pair;

int comparePairs(const void* a, const void* b) {
    long long v1 = ((Pair*)a)->val;
    long long v2 = ((Pair*)b)->val;
    if (v1 < v2) return -1;
    if (v1 > v2) return 1;
    return 0;
}

int compareInts(const void* a, const void* b) {
    int v1 = *(const int*)a;
    int v2 = *(const int*)b;
    if (v1 < v2) return -1;
    if (v1 > v2) return 1;
    return 0;
}

int find_freq(long long val, Pair* pairs, int size) {
    if (val > 1000000000) return 0;
    int low = 0, high = size - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (pairs[mid].val == val) return pairs[mid].freq;
        if (pairs[mid].val < val) low = mid + 1;
        else high = mid - 1;
    }
    return 0;
}

int maximumLength(int* nums, int numsSize) {
    if (numsSize == 0) return 0;
    qsort(nums, numsSize, sizeof(int), compareInts);

    Pair* pairs = (Pair*)malloc(sizeof(Pair) * numsSize);
    int unique_count = 0;
    pairs[0].val = nums[0];
    pairs[0].freq = 1;
    unique_count = 1;
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] == nums[i - 1]) {
            pairs[unique_count - 1].freq++;
        } else {
            pairs[unique_count].val = nums[i];
            pairs[unique_count].freq = 1;
            unique_count++;
        }
    }

    int max_len = 1;
    int start_idx = 0;
    if (pairs[0].val == 1) {
        int c = pairs[0].freq;
        max_len = (c % 2 == 0) ? c - 1 : c;
        start_idx = 1;
    }

    for (int i = start_idx; i < unique_count; i++) {
        long long curr = pairs[i].val;
        int current_len = 0;
        int peak_found = 0;
        while (find_freq(curr, pairs, unique_count) >= 2) {
            long long nxt = curr * curr;
            if (find_freq(nxt, pairs, unique_count) >= 1) {
                current_len += 2;
                curr = nxt;
            } else {
                current_len += 1;
                peak_found = 1;
                break;
            }
        }
        if (!peak_found) {
            current_len += 1;
        }
        if (current_len > max_len) max_len = current_len;
    }

    free(pairs);
    return max_len;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
// Generation failed for C#
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
// Generation failed for JavaScript
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
// Generation failed for TypeScript
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
// Generation failed for PHP
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
// Generation failed for Swift
// Reason: Error: 503 UNAVAILABLE. {'error': {'code': 503, 'message': 'This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.', 'status': 'UNAVAILABLE'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maximumLength(nums: IntArray): Int {
        val counts = mutableMapOf<Long, Int>()
        for (num in nums) {
            val n = num.toLong()
            counts[n] = counts.getOrDefault(n, 0) + 1
        }

        var maxLen = 1
        if (counts.containsKey(1L)) {
            val c1 = counts[1L]!!
            if (c1 % 2 == 0) {
                maxLen = c1 - 1
            } else {
                maxLen = c1
            }
        }

        for (x in counts.keys) {
            if (x == 1L) continue

            var currLen = 0
            var curr = x
            while (counts.getOrDefault(curr, 0) >= 2) {
                currLen += 2
                val nextCurr = curr * curr
                curr = nextCurr
                if (curr > 1000000000L) break
            }

            if (counts.getOrDefault(curr, 0) >= 1) {
                currLen += 1
            } else {
                currLen -= 1
            }

            if (currLen > maxLen) {
                maxLen = currLen
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
  int maximumLength(List<int> nums) {
    Map<int, int> counts = {};
    for (var num in nums) {
      counts[num] = (counts[num] ?? 0) + 1;
    }

    int maxLen = 1;
    if (counts.containsKey(1)) {
      int c1 = counts[1]!;
      if (c1 % 2 == 0) {
        maxLen = c1 - 1;
      } else {
        maxLen = c1;
      }
    }

    for (var x in counts.keys) {
      if (x == 1) continue;

      int currLen = 0;
      int curr = x;
      while ((counts[curr] ?? 0) >= 2) {
        currLen += 2;
        int nextCurr = curr * curr;
        curr = nextCurr;
        if (curr > 1000000000) break;
      }

      if ((counts[curr] ?? 0) >= 1) {
        currLen += 1;
      } else {
        currLen -= 1;
      }

      if (currLen > maxLen) {
        maxLen = currLen;
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
func maximumLength(nums []int) int {
	counts := make(map[int64]int)
	for _, num := range nums {
		counts[int64(num)]++
	}

	maxLen := 1
	if c1, ok := counts[1]; ok {
		if c1%2 == 0 {
			maxLen = c1 - 1
		} else {
			maxLen = c1
		}
	}

	for x, _ := range counts {
		if x == 1 {
			continue
		}

		currLen := 0
		curr := x
		for counts[curr] >= 2 {
			currLen += 2
			nextCurr := curr * curr
			curr = nextCurr
			if curr > 1000000000 {
				break
			}
		}

		if counts[curr] >= 1 {
			currLen += 1
		} else {
			currLen -= 1
		}

		if currLen > maxLen {
			maxLen = currLen
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
def maximum_length(nums)
  counts = Hash.new(0)
  nums.each { |num| counts[num] += 1 }

  max_len = 1
  if counts[1] > 0
    if counts[1] % 2 == 0
      max_len = counts[1] - 1
    else
      max_len = counts[1]
    end
  end

  counts.each_key do |x|
    next if x == 1

    curr_len = 0
    curr = x
    while counts[curr] >= 2
      curr_len += 2
      next_curr = curr * curr
      curr = next_curr
      break if curr > 1000000000
    end

    if counts[curr] >= 1
      curr_len += 1
    else
      curr_len -= 1
    end

    max_len = curr_len if curr_len > max_len
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
  def maximumLength(nums: Array[Int]): Int = {
    val counts = mutable.Map[Long, Int]().withDefaultValue(0)
    for (num <- nums) {
      counts(num.toLong) += 1
    }

    var maxLen = 1
    if (counts.contains(1L)) {
      val c1 = counts(1L)
      if (c1 % 2 == 0) {
        maxLen = c1 - 1
      } else {
        maxLen = c1
      }
    }

    for (x <- counts.keys) {
      if (x != 1L) {
        var currLen = 0
        var curr = x
        var keepGoing = true
        while (keepGoing && counts.getOrElse(curr, 0) >= 2) {
          currLen += 2
          val nextCurr = curr * curr
          curr = nextCurr
          if (curr > 1000000000L) {
            keepGoing = false
          }
        }

        if (counts.getOrElse(curr, 0) >= 1) {
          currLen += 1
        } else {
          currLen -= 1
        }

        if (currLen > maxLen) {
          maxLen = currLen
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
use std::collections::HashMap;

impl Solution {
    pub fn maximum_length(nums: Vec<i32>) -> i32 {
        let mut counts: HashMap<i64, i64> = HashMap::new();
        for &num in &nums {
            *counts.entry(num as i64).or_insert(0) += 1;
        }

        let mut ans = 1;
        if let Some(&c1) = counts.get(&1i64) {
            ans = if c1 % 2 == 1 { c1 as i32 } else { (c1 - 1) as i32 };
        }

        for (&val, _) in &counts {
            if val == 1 {
                continue;
            }
            let mut res = 0;
            let mut curr = val;
            loop {
                let count = *counts.get(&curr).unwrap_or(&0);
                if count >= 2 {
                    res += 2;
                    if curr > 31622 {
                        res -= 1;
                        break;
                    }
                    curr = curr * curr;
                } else if count == 1 {
                    res += 1;
                    break;
                } else {
                    res -= 1;
                    break;
                }
            }
            if res > ans {
                ans = res as i32;
            }
        }
        ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (maximum-length nums)
  (-> (listof exact-integer?) exact-integer?)
  (let ([counts (make-hash)])
    (for ([num nums])
      (hash-update! counts num (lambda (x) (+ x 1)) 0))
    (let* ([c1 (hash-ref counts 1 0)]
           [ans-initial (if (zero? c1) 1 (if (odd? c1) c1 (- c1 1)))])
      (foldl (lambda (val acc)
               (if (= val 1)
                   acc
                   (max acc
                        (let loop ([curr val] [res 0])
                          (let ([count (hash-ref counts curr 0)])
                            (cond
                              [(>= count 2)
                               (if (> curr 31622)
                                   (+ res 1)
                                   (loop (* curr curr) (+ res 2)))]
                              [(= count 1)
                               (+ res 1)]
                              [else
                               (- res 1)]))))))
             ans-initial
             (hash-keys counts)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec maximum_length(Nums :: [integer()]) -> integer().
maximum_length(Nums) ->
  Counts = lists:foldl(fun(X, Acc) ->
    maps:put(X, maps:get(X, Acc, 0) + 1, Acc)
  end, #{}, Nums),
  C1 = maps:get(1, Counts, 0),
  AnsInitial = if C1 == 0 -> 1;
                  C1 rem 2 == 1 -> C1;
                  true -> C1 - 1
               end,
  lists:foldl(fun(Val, MaxAns) ->
    if Val == 1 -> MaxAns;
       true ->
         Res = calculate(Val, Counts, 0),
         if Res > MaxAns -> Res; true -> MaxAns end
    end
  end, AnsInitial, maps:keys(Counts)).

calculate(Curr, Counts, Res) ->
  Count = maps:get(Curr, Counts, 0),
  if Count >= 2 ->
    if Curr > 31622 -> Res + 1;
       true -> calculate(Curr * Curr, Counts, Res + 2)
    end;
    Count == 1 -> Res + 1;
    true -> Res - 1
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec maximum_length(nums :: [integer]) :: integer
  def maximum_length(nums) do
    counts = Enum.reduce(nums, %{}, fn x, acc ->
      Map.update(acc, x, 1, &(&1 + 1))
    end)

    c1 = Map.get(counts, 1, 0)
    ans_initial = if c1 == 0, do: 1, else: (if rem(c1, 2) == 1, do: c1, else: c1 - 1)

    Enum.reduce(counts, ans_initial, fn {val, _count}, max_ans ->
      if val == 1 do
        max_ans
      else
        res = calculate(val, counts, 0)
        max(max_ans, res)
      end
    end)
  end

  defp calculate(curr, counts, res) do
    count = Map.get(counts, curr, 0)
    cond do
      count >= 2 ->
        if curr > 31622 do
          res + 1
        else
          calculate(curr * curr, counts, res + 2)
        end
      count == 1 ->
        res + 1
      true ->
        res - 1
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N \log N) or O(N) depending on the language's frequency map implementation. Sorting the array or using a balanced BST map (like C++ `std::map`) results in O(N \log N). Using a hash map (like Python `Counter` or Java `HashMap`) results in O(N) average time complexity. The chain traversal takes O(log log M) per unique element, where M is the maximum value in nums.
- **Space Complexity:** O(N) to store the frequency map or the unique element pairs extracted from the input array.
