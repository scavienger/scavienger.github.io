---
layout: post
title: "Trionic Array I"
date: 2026-02-03 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/trionic-array-i/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool isTrionic(vector<int>& nums) {\n   \
        \     int n = nums.size();\n        for (int p = 1; p < n - 2; ++p) {\n    \
        \        for (int q = p + 1; q < n - 1; ++q) {\n                bool valid =\
        \ true;\n                for (int i = 0; i < p; ++i) {\n                   \
        \ if (nums[i] >= nums[i + 1]) { valid = false; break; }\n                }\n\
        \                if (!valid) continue;\n                for (int i = p; i <\
        \ q; ++i) {\n                    if (nums[i] <= nums[i + 1]) { valid = false;\
        \ break; }\n                }\n                if (!valid) continue;\n     \
        \           for (int i = q; i < n - 1; ++i) {\n                    if (nums[i]\
        \ >= nums[i + 1]) { valid = false; break; }\n                }\n           \
        \     if (valid) return true;\n            }\n        }\n        return false;\n\
        \    }\n};"
      java: "class Solution {\n    public boolean isTrionic(int[] nums) {\n        int\
        \ n = nums.length;\n        for (int p = 1; p < n - 2; p++) {\n            for\
        \ (int q = p + 1; q < n - 1; q++) {\n                boolean valid = true;\n\
        \                for (int i = 0; i < p; i++) {\n                    if (nums[i]\
        \ >= nums[i + 1]) { valid = false; break; }\n                }\n           \
        \     if (!valid) continue;\n                for (int i = p; i < q; i++) {\n\
        \                    if (nums[i] <= nums[i + 1]) { valid = false; break; }\n\
        \                }\n                if (!valid) continue;\n                for\
        \ (int i = q; i < n - 1; i++) {\n                    if (nums[i] >= nums[i +\
        \ 1]) { valid = false; break; }\n                }\n                if (valid)\
        \ return true;\n            }\n        }\n        return false;\n    }\n}"
      python: "class Solution(object):\n    def isTrionic(self, nums):\n        \"\"\
        \"\n        :type nums: List[int]\n        :rtype: bool\n        \"\"\"\n  \
        \      n = len(nums)\n        for p in range(1, n - 2):\n            for q in\
        \ range(p + 1, n - 1):\n                valid = True\n                for i\
        \ in range(p):\n                    if nums[i] >= nums[i + 1]:\n           \
        \             valid = False\n                        break\n               \
        \ if not valid: continue\n                for i in range(p, q):\n          \
        \          if nums[i] <= nums[i + 1]:\n                        valid = False\n\
        \                        break\n                if not valid: continue\n   \
        \             for i in range(q, n - 1):\n                    if nums[i] >= nums[i\
        \ + 1]:\n                        valid = False\n                        break\n\
        \                if valid:\n                    return True\n        return\
        \ False"
      python3: "class Solution:\n    def isTrionic(self, nums: List[int]) -> bool:\n\
        \        n = len(nums)\n        for p in range(1, n - 2):\n            for q\
        \ in range(p + 1, n - 1):\n                valid = True\n                for\
        \ i in range(p):\n                    if nums[i] >= nums[i+1]:\n           \
        \             valid = False\n                        break\n               \
        \ if not valid: continue\n                for i in range(p, q):\n          \
        \          if nums[i] <= nums[i+1]:\n                        valid = False\n\
        \                        break\n                if not valid: continue\n   \
        \             for i in range(q, n - 1):\n                    if nums[i] >= nums[i+1]:\n\
        \                        valid = False\n                        break\n    \
        \            if valid:\n                    return True\n        return False"
      c: "bool isTrionic(int* nums, int numsSize) {\n    for (int p = 1; p < numsSize\
        \ - 2; ++p) {\n        for (int q = p + 1; q < numsSize - 1; ++q) {\n      \
        \      bool valid = true;\n            for (int i = 0; i < p; ++i) {\n     \
        \           if (nums[i] >= nums[i + 1]) { valid = false; break; }\n        \
        \    }\n            if (!valid) continue;\n            for (int i = p; i < q;\
        \ ++i) {\n                if (nums[i] <= nums[i + 1]) { valid = false; break;\
        \ }\n            }\n            if (!valid) continue;\n            for (int\
        \ i = q; i < numsSize - 1; ++i) {\n                if (nums[i] >= nums[i + 1])\
        \ { valid = false; break; }\n            }\n            if (valid) return true;\n\
        \        }\n    }\n    return false;\n}"
      csharp: "public class Solution {\n    public bool IsTrionic(int[] nums) {\n  \
        \      int n = nums.Length;\n        for (int p = 1; p < n - 2; p++) {\n   \
        \         for (int q = p + 1; q < n - 1; q++) {\n                bool valid\
        \ = true;\n                for (int i = 0; i < p; i++) {\n                 \
        \   if (nums[i] >= nums[i + 1]) { valid = false; break; }\n                }\n\
        \                if (!valid) continue;\n                for (int i = p; i <\
        \ q; i++) {\n                    if (nums[i] <= nums[i + 1]) { valid = false;\
        \ break; }\n                }\n                if (!valid) continue;\n     \
        \           for (int i = q; i < n - 1; i++) {\n                    if (nums[i]\
        \ >= nums[i + 1]) { valid = false; break; }\n                }\n           \
        \     if (valid) return true;\n            }\n        }\n        return false;\n\
        \    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {boolean}\n */\nvar isTrionic\
        \ = function(nums) {\n    const n = nums.length;\n    for (let p = 1; p < n\
        \ - 2; p++) {\n        for (let q = p + 1; q < n - 1; q++) {\n            let\
        \ valid = true;\n            for (let i = 0; i < p; i++) {\n               \
        \ if (nums[i] >= nums[i + 1]) { valid = false; break; }\n            }\n   \
        \         if (!valid) continue;\n            for (let i = p; i < q; i++) {\n\
        \                if (nums[i] <= nums[i + 1]) { valid = false; break; }\n   \
        \         }\n            if (!valid) continue;\n            for (let i = q;\
        \ i < n - 1; i++) {\n                if (nums[i] >= nums[i + 1]) { valid = false;\
        \ break; }\n            }\n            if (valid) return true;\n        }\n\
        \    }\n    return false;\n};"
      typescript: "function isTrionic(nums: number[]): boolean {\n    const n = nums.length;\n\
        \    for (let p = 1; p < n - 2; p++) {\n        for (let q = p + 1; q < n -\
        \ 1; q++) {\n            let ok = true;\n            for (let i = 0; i < p;\
        \ i++) {\n                if (nums[i] >= nums[i + 1]) {\n                  \
        \  ok = false;\n                    break;\n                }\n            }\n\
        \            if (!ok) continue;\n            for (let i = p; i < q; i++) {\n\
        \                if (nums[i] <= nums[i + 1]) {\n                    ok = false;\n\
        \                    break;\n                }\n            }\n            if\
        \ (!ok) continue;\n            for (let i = q; i < n - 1; i++) {\n         \
        \       if (nums[i] >= nums[i + 1]) {\n                    ok = false;\n   \
        \                 break;\n                }\n            }\n            if (ok)\
        \ return true;\n        }\n    }\n    return false;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Boolean\n     */\n    function isTrionic($nums) {\n        $n = count($nums);\n\
        \        for ($p = 1; $p < $n - 2; $p++) {\n            for ($q = $p + 1; $q\
        \ < $n - 1; $q++) {\n                $ok = true;\n                for ($i =\
        \ 0; $i < $p; $i++) {\n                    if ($nums[$i] >= $nums[$i + 1]) {\n\
        \                        $ok = false;\n                        break;\n    \
        \                }\n                }\n                if (!$ok) continue;\n\
        \                for ($i = $p; $i < $q; $i++) {\n                    if ($nums[$i]\
        \ <= $nums[$i + 1]) {\n                        $ok = false;\n              \
        \          break;\n                    }\n                }\n              \
        \  if (!$ok) continue;\n                for ($i = $q; $i < $n - 1; $i++) {\n\
        \                    if ($nums[$i] >= $nums[$i + 1]) {\n                   \
        \     $ok = false;\n                        break;\n                    }\n\
        \                }\n                if ($ok) return true;\n            }\n \
        \       }\n        return false;\n    }\n}"
      swift: "class Solution {\n    func isTrionic(_ nums: [Int]) -> Bool {\n      \
        \  let n = nums.count\n        if n < 4 { return false }\n        for p in 1..<(n\
        \ - 2) {\n            for q in (p + 1)..<(n - 1) {\n                var ok =\
        \ true\n                for i in 0..<p {\n                    if nums[i] >=\
        \ nums[i + 1] {\n                        ok = false\n                      \
        \  break\n                    }\n                }\n                if !ok {\
        \ continue }\n                for i in p..<q {\n                    if nums[i]\
        \ <= nums[i + 1] {\n                        ok = false\n                   \
        \     break\n                    }\n                }\n                if !ok\
        \ { continue }\n                for i in q..<(n - 1) {\n                   \
        \ if nums[i] >= nums[i + 1] {\n                        ok = false\n        \
        \                break\n                    }\n                }\n         \
        \       if ok { return true }\n            }\n        }\n        return false\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun isTrionic(nums: IntArray): Boolean {\n    \
        \    val n = nums.size\n        for (p in 1 until n - 2) {\n            for\
        \ (q in p + 1 until n - 1) {\n                var ok = true\n              \
        \  for (i in 0 until p) {\n                    if (nums[i] >= nums[i + 1]) {\n\
        \                        ok = false\n                        break\n       \
        \             }\n                }\n                if (!ok) continue\n    \
        \            for (i in p until q) {\n                    if (nums[i] <= nums[i\
        \ + 1]) {\n                        ok = false\n                        break\n\
        \                    }\n                }\n                if (!ok) continue\n\
        \                for (i in q until n - 1) {\n                    if (nums[i]\
        \ >= nums[i + 1]) {\n                        ok = false\n                  \
        \      break\n                    }\n                }\n                if (ok)\
        \ return true\n            }\n        }\n        return false\n    }\n}"
      dart: "class Solution {\n  bool isTrionic(List<int> nums) {\n    int n = nums.length;\n\
        \    for (int p = 1; p < n - 2; p++) {\n      for (int q = p + 1; q < n - 1;\
        \ q++) {\n        bool ok = true;\n        for (int i = 0; i < p; i++) {\n \
        \         if (nums[i] >= nums[i + 1]) {\n            ok = false;\n         \
        \   break;\n          }\n        }\n        if (!ok) continue;\n        for\
        \ (int i = p; i < q; i++) {\n          if (nums[i] <= nums[i + 1]) {\n     \
        \       ok = false;\n            break;\n          }\n        }\n        if\
        \ (!ok) continue;\n        for (int i = q; i < n - 1; i++) {\n          if (nums[i]\
        \ >= nums[i + 1]) {\n            ok = false;\n            break;\n         \
        \ }\n        }\n        if (ok) return true;\n      }\n    }\n    return false;\n\
        \  }\n}"
      go: "func isTrionic(nums []int) bool {\n\tn := len(nums)\n\tfor p := 1; p < n-2;\
        \ p++ {\n\t\tfor q := p + 1; q < n-1; q++ {\n\t\t\tok := true\n\t\t\tfor i :=\
        \ 0; i < p; i++ {\n\t\t\t\tif nums[i] >= nums[i+1] {\n\t\t\t\t\tok = false\n\
        \t\t\t\t\tbreak\n\t\t\t\t}\n\t\t\t}\n\t\t\tif !ok {\n\t\t\t\tcontinue\n\t\t\t\
        }\n\t\t\tfor i := p; i < q; i++ {\n\t\t\t\tif nums[i] <= nums[i+1] {\n\t\t\t\
        \t\tok = false\n\t\t\t\t\tbreak\n\t\t\t\t}\n\t\t\t}\n\t\t\tif !ok {\n\t\t\t\t\
        continue\n\t\t\t}\n\t\t\tfor i := q; i < n-1; i++ {\n\t\t\t\tif nums[i] >= nums[i+1]\
        \ {\n\t\t\t\t\tok = false\n\t\t\t\t\tbreak\n\t\t\t\t}\n\t\t\t}\n\t\t\tif ok\
        \ {\n\t\t\t\treturn true\n\t\t\t}\n\t\t}\n\t}\n\treturn false\n}"
      ruby: "def is_trionic(nums)\n  n = nums.length\n  return false if n < 4\n  (1...n\
        \ - 2).each do |p|\n    (p + 1...n - 1).each do |q|\n      valid = true\n  \
        \    (0...p).each { |i| valid = false if nums[i] >= nums[i+1] }\n      (p...q).each\
        \ { |i| valid = false if nums[i] <= nums[i+1] }\n      (q...n - 1).each { |i|\
        \ valid = false if nums[i] >= nums[i+1] }\n      return true if valid\n    end\n\
        \  end\n  false\nend"
      scala: "object Solution {\n  def isTrionic(nums: Array[Int]): Boolean = {\n  \
        \  val n = nums.length\n    if (n < 4) return false\n    for (p <- 1 until n\
        \ - 2) {\n      for (q <- p + 1 until n - 1) {\n        var valid = true\n \
        \       for (i <- 0 until p) if (nums(i) >= nums(i + 1)) valid = false\n   \
        \     for (i <- p until q) if (nums(i) <= nums(i + 1)) valid = false\n     \
        \   for (i <- q until n - 1) if (nums(i) >= nums(i + 1)) valid = false\n   \
        \     if (valid) return true\n      }\n    }\n    false\n  }\n}"
      rust: "impl Solution {\n    pub fn is_trionic(nums: Vec<i32>) -> bool {\n    \
        \    let n = nums.len();\n        if n < 4 {\n            return false;\n  \
        \      }\n        for p in 1..n - 2 {\n            for q in p + 1..n - 1 {\n\
        \                let mut valid = true;\n                for i in 0..p {\n  \
        \                  if nums[i] >= nums[i + 1] { valid = false; }\n          \
        \      }\n                for i in p..q {\n                    if nums[i] <=\
        \ nums[i + 1] { valid = false; }\n                }\n                for i in\
        \ q..n - 1 {\n                    if nums[i] >= nums[i + 1] { valid = false;\
        \ }\n                }\n                if valid {\n                    return\
        \ true;\n                }\n            }\n        }\n        false\n    }\n\
        }"
      racket: "(define/contract (is-trionic nums)\n  (-> (listof exact-integer?) boolean?)\n\
        \  (let* ([n (length nums)]\n         [arr (list->vector nums)])\n    (if (<\
        \ n 4)\n        #f\n        (for*/or ([p (in-range 1 (- n 2))]\n           \
        \       [q (in-range (+ p 1) (- n 1))])\n          (and (for/and ([i (in-range\
        \ 0 p)])\n                 (< (vector-ref arr i) (vector-ref arr (+ i 1))))\n\
        \               (for/and ([i (in-range p q)])\n                 (> (vector-ref\
        \ arr i) (vector-ref arr (+ i 1))))\n               (for/and ([i (in-range q\
        \ (- n 1))])\n                 (< (vector-ref arr i) (vector-ref arr (+ i 1)))))))))"
      erlang: "-spec is_trionic(Nums :: [integer()]) -> boolean().\nis_trionic(Nums)\
        \ ->\n  N = length(Nums),\n  if\n    N < 4 -> false;\n    true ->\n      Arr\
        \ = list_to_tuple(Nums),\n      check_p(1, N, Arr)\n  end.\n\ncheck_p(P, N,\
        \ Arr) when P < N - 2 ->\n  case check_q(P, P + 1, N, Arr) of\n    true -> true;\n\
        \    false -> check_p(P + 1, N, Arr)\n  end;\ncheck_p(_, _, _) -> false.\n\n\
        check_q(P, Q, N, Arr) when Q < N - 1 ->\n  Valid = check_inc(0, P, Arr) andalso\
        \ check_dec(P, Q, Arr) andalso check_inc(Q, N - 1, Arr),\n  if\n    Valid ->\
        \ true;\n    true -> check_q(P, Q + 1, N, Arr)\n  end;\ncheck_q(_, _, _, _)\
        \ -> false.\n\ncheck_inc(Start, End, Arr) ->\n  lists:all(fun(I) -> element(I\
        \ + 1, Arr) < element(I + 2, Arr) end, lists:seq(Start, End - 1)).\n\ncheck_dec(Start,\
        \ End, Arr) ->\n  lists:all(fun(I) -> element(I + 1, Arr) > element(I + 2, Arr)\
        \ end, lists:seq(Start, End - 1))."
      elixir: "defmodule Solution do\n  @spec is_trionic(nums :: [integer]) :: boolean\n\
        \  def is_trionic(nums) do\n    n = length(nums)\n    if n < 4 do\n      false\n\
        \    else\n      arr = List.to_tuple(nums)\n      Enum.any?(1..(n - 3), fn p\
        \ ->\n        Enum.any?((p + 1)..(n - 2), fn q ->\n          check_inc(arr,\
        \ 0, p) and check_dec(arr, p, q) and check_inc(arr, q, n - 1)\n        end)\n\
        \      end)\n    end\n  end\n\n  defp check_inc(arr, start_idx, end_idx) do\n\
        \    Enum.all?(start_idx..(end_idx - 1), fn i ->\n      elem(arr, i) < elem(arr,\
        \ i + 1)\n    end)\n  end\n\n  defp check_dec(arr, start_idx, end_idx) do\n\
        \    Enum.all?(start_idx..(end_idx - 1), fn i ->\n      elem(arr, i) > elem(arr,\
        \ i + 1)\n    end)\n  end\nend"
    approach: 'The algorithm employs a brute-force search over all possible split points
      p and q that satisfy the condition 0 < p < q < n - 1. For every valid pair of
      indices (p, q), we partition the array into three distinct segments: the prefix
      from index 0 to p, the middle section from p to q, and the suffix from q to n
      - 1. We then verify if the prefix is strictly increasing, the middle section is
      strictly decreasing, and the suffix is strictly increasing.


      Key intuition relies on the observation that p acts as a local maximum (peak)
      and q acts as a local minimum (valley). Since the array length n is relatively
      small (up to 100), iterating through all O(n^2) possible split points and performing
      O(n) checks for each pair results in an O(n^3) complexity, which is well within
      the acceptable performance limits for this problem. If any pair (p, q) is found
      that satisfies all monotonic requirements, we return true; otherwise, we return
      false.'
    time_complexity: O(n^3) where n is the length of the input array. There are two
      nested loops to select indices p and q, and inside these loops, we perform three
      linear checks to verify the strict monotonicity of the array segments.
    space_complexity: O(1) as we only use a constant amount of extra space for loop
      counters and boolean flags, regardless of the size of the input array.
    elapsed_time: 320.84507870674133
    model: gemini-3-flash-preview
    generated_at: '2026-02-03 01:30:14 '
---

## Problem #3637: Trionic Array I

**Difficulty:** Easy

**Topics:** Array

## Problem Description

<p data-end="128" data-start="0">You are given an integer array <code data-end="37" data-start="31">nums</code> of length <code data-end="51" data-start="48">n</code>.</p>

<p data-end="128" data-start="0">An array is <strong data-end="76" data-start="65">trionic</strong> if there exist indices <code data-end="117" data-start="100">0 &lt; p &lt; q &lt; n &minus; 1</code> such that:</p>

<ul>
	<li data-end="170" data-start="132"><code data-end="144" data-start="132">nums[0...p]</code> is <strong>strictly</strong> increasing,</li>
	<li data-end="211" data-start="173"><code data-end="185" data-start="173">nums[p...q]</code> is <strong>strictly</strong> decreasing,</li>
	<li data-end="252" data-start="214"><code data-end="228" data-start="214">nums[q...n &minus; 1]</code> is <strong>strictly</strong> increasing.</li>
</ul>

<p data-end="315" data-is-last-node="" data-is-only-node="" data-start="254">Return <code data-end="267" data-start="261">true</code> if <code data-end="277" data-start="271">nums</code> is trionic, otherwise return <code data-end="314" data-start="307">false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,3,5,4,2,6]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>Pick <code data-end="91" data-start="84">p = 2</code>, <code data-end="100" data-start="93">q = 4</code>:</p>

<ul>
	<li><code data-end="130" data-start="108">nums[0...2] = [1, 3, 5]</code> is strictly increasing (<code data-end="166" data-start="155">1 &lt; 3 &lt; 5</code>).</li>
	<li><code data-end="197" data-start="175">nums[2...4] = [5, 4, 2]</code> is strictly decreasing (<code data-end="233" data-start="222">5 &gt; 4 &gt; 2</code>).</li>
	<li><code data-end="262" data-start="242">nums[4...5] = [2, 6]</code> is strictly increasing (<code data-end="294" data-start="287">2 &lt; 6</code>).</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,1,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p>There is no way to pick <code>p</code> and <code>q</code> to form the required three segments.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li data-end="41" data-start="26"><code data-end="39" data-start="26">3 &lt;= n &lt;= 100</code></li>
	<li data-end="70" data-start="44"><code data-end="70" data-start="44">-1000 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


## Hints

1. Use brute force

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm employs a brute-force search over all possible split points p and q that satisfy the condition 0 < p < q < n - 1. For every valid pair of indices (p, q), we partition the array into three distinct segments: the prefix from index 0 to p, the middle section from p to q, and the suffix from q to n - 1. We then verify if the prefix is strictly increasing, the middle section is strictly decreasing, and the suffix is strictly increasing.

Key intuition relies on the observation that p acts as a local maximum (peak) and q acts as a local minimum (valley). Since the array length n is relatively small (up to 100), iterating through all O(n^2) possible split points and performing O(n) checks for each pair results in an O(n^3) complexity, which is well within the acceptable performance limits for this problem. If any pair (p, q) is found that satisfies all monotonic requirements, we return true; otherwise, we return false.

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
    bool isTrionic(vector<int>& nums) {
        int n = nums.size();
        for (int p = 1; p < n - 2; ++p) {
            for (int q = p + 1; q < n - 1; ++q) {
                bool valid = true;
                for (int i = 0; i < p; ++i) {
                    if (nums[i] >= nums[i + 1]) { valid = false; break; }
                }
                if (!valid) continue;
                for (int i = p; i < q; ++i) {
                    if (nums[i] <= nums[i + 1]) { valid = false; break; }
                }
                if (!valid) continue;
                for (int i = q; i < n - 1; ++i) {
                    if (nums[i] >= nums[i + 1]) { valid = false; break; }
                }
                if (valid) return true;
            }
        }
        return false;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public boolean isTrionic(int[] nums) {
        int n = nums.length;
        for (int p = 1; p < n - 2; p++) {
            for (int q = p + 1; q < n - 1; q++) {
                boolean valid = true;
                for (int i = 0; i < p; i++) {
                    if (nums[i] >= nums[i + 1]) { valid = false; break; }
                }
                if (!valid) continue;
                for (int i = p; i < q; i++) {
                    if (nums[i] <= nums[i + 1]) { valid = false; break; }
                }
                if (!valid) continue;
                for (int i = q; i < n - 1; i++) {
                    if (nums[i] >= nums[i + 1]) { valid = false; break; }
                }
                if (valid) return true;
            }
        }
        return false;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        for p in range(1, n - 2):
            for q in range(p + 1, n - 1):
                valid = True
                for i in range(p):
                    if nums[i] >= nums[i + 1]:
                        valid = False
                        break
                if not valid: continue
                for i in range(p, q):
                    if nums[i] <= nums[i + 1]:
                        valid = False
                        break
                if not valid: continue
                for i in range(q, n - 1):
                    if nums[i] >= nums[i + 1]:
                        valid = False
                        break
                if valid:
                    return True
        return False
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        for p in range(1, n - 2):
            for q in range(p + 1, n - 1):
                valid = True
                for i in range(p):
                    if nums[i] >= nums[i+1]:
                        valid = False
                        break
                if not valid: continue
                for i in range(p, q):
                    if nums[i] <= nums[i+1]:
                        valid = False
                        break
                if not valid: continue
                for i in range(q, n - 1):
                    if nums[i] >= nums[i+1]:
                        valid = False
                        break
                if valid:
                    return True
        return False
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
bool isTrionic(int* nums, int numsSize) {
    for (int p = 1; p < numsSize - 2; ++p) {
        for (int q = p + 1; q < numsSize - 1; ++q) {
            bool valid = true;
            for (int i = 0; i < p; ++i) {
                if (nums[i] >= nums[i + 1]) { valid = false; break; }
            }
            if (!valid) continue;
            for (int i = p; i < q; ++i) {
                if (nums[i] <= nums[i + 1]) { valid = false; break; }
            }
            if (!valid) continue;
            for (int i = q; i < numsSize - 1; ++i) {
                if (nums[i] >= nums[i + 1]) { valid = false; break; }
            }
            if (valid) return true;
        }
    }
    return false;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public bool IsTrionic(int[] nums) {
        int n = nums.Length;
        for (int p = 1; p < n - 2; p++) {
            for (int q = p + 1; q < n - 1; q++) {
                bool valid = true;
                for (int i = 0; i < p; i++) {
                    if (nums[i] >= nums[i + 1]) { valid = false; break; }
                }
                if (!valid) continue;
                for (int i = p; i < q; i++) {
                    if (nums[i] <= nums[i + 1]) { valid = false; break; }
                }
                if (!valid) continue;
                for (int i = q; i < n - 1; i++) {
                    if (nums[i] >= nums[i + 1]) { valid = false; break; }
                }
                if (valid) return true;
            }
        }
        return false;
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
 * @return {boolean}
 */
var isTrionic = function(nums) {
    const n = nums.length;
    for (let p = 1; p < n - 2; p++) {
        for (let q = p + 1; q < n - 1; q++) {
            let valid = true;
            for (let i = 0; i < p; i++) {
                if (nums[i] >= nums[i + 1]) { valid = false; break; }
            }
            if (!valid) continue;
            for (let i = p; i < q; i++) {
                if (nums[i] <= nums[i + 1]) { valid = false; break; }
            }
            if (!valid) continue;
            for (let i = q; i < n - 1; i++) {
                if (nums[i] >= nums[i + 1]) { valid = false; break; }
            }
            if (valid) return true;
        }
    }
    return false;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function isTrionic(nums: number[]): boolean {
    const n = nums.length;
    for (let p = 1; p < n - 2; p++) {
        for (let q = p + 1; q < n - 1; q++) {
            let ok = true;
            for (let i = 0; i < p; i++) {
                if (nums[i] >= nums[i + 1]) {
                    ok = false;
                    break;
                }
            }
            if (!ok) continue;
            for (let i = p; i < q; i++) {
                if (nums[i] <= nums[i + 1]) {
                    ok = false;
                    break;
                }
            }
            if (!ok) continue;
            for (let i = q; i < n - 1; i++) {
                if (nums[i] >= nums[i + 1]) {
                    ok = false;
                    break;
                }
            }
            if (ok) return true;
        }
    }
    return false;
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
     * @return Boolean
     */
    function isTrionic($nums) {
        $n = count($nums);
        for ($p = 1; $p < $n - 2; $p++) {
            for ($q = $p + 1; $q < $n - 1; $q++) {
                $ok = true;
                for ($i = 0; $i < $p; $i++) {
                    if ($nums[$i] >= $nums[$i + 1]) {
                        $ok = false;
                        break;
                    }
                }
                if (!$ok) continue;
                for ($i = $p; $i < $q; $i++) {
                    if ($nums[$i] <= $nums[$i + 1]) {
                        $ok = false;
                        break;
                    }
                }
                if (!$ok) continue;
                for ($i = $q; $i < $n - 1; $i++) {
                    if ($nums[$i] >= $nums[$i + 1]) {
                        $ok = false;
                        break;
                    }
                }
                if ($ok) return true;
            }
        }
        return false;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func isTrionic(_ nums: [Int]) -> Bool {
        let n = nums.count
        if n < 4 { return false }
        for p in 1..<(n - 2) {
            for q in (p + 1)..<(n - 1) {
                var ok = true
                for i in 0..<p {
                    if nums[i] >= nums[i + 1] {
                        ok = false
                        break
                    }
                }
                if !ok { continue }
                for i in p..<q {
                    if nums[i] <= nums[i + 1] {
                        ok = false
                        break
                    }
                }
                if !ok { continue }
                for i in q..<(n - 1) {
                    if nums[i] >= nums[i + 1] {
                        ok = false
                        break
                    }
                }
                if ok { return true }
            }
        }
        return false
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun isTrionic(nums: IntArray): Boolean {
        val n = nums.size
        for (p in 1 until n - 2) {
            for (q in p + 1 until n - 1) {
                var ok = true
                for (i in 0 until p) {
                    if (nums[i] >= nums[i + 1]) {
                        ok = false
                        break
                    }
                }
                if (!ok) continue
                for (i in p until q) {
                    if (nums[i] <= nums[i + 1]) {
                        ok = false
                        break
                    }
                }
                if (!ok) continue
                for (i in q until n - 1) {
                    if (nums[i] >= nums[i + 1]) {
                        ok = false
                        break
                    }
                }
                if (ok) return true
            }
        }
        return false
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  bool isTrionic(List<int> nums) {
    int n = nums.length;
    for (int p = 1; p < n - 2; p++) {
      for (int q = p + 1; q < n - 1; q++) {
        bool ok = true;
        for (int i = 0; i < p; i++) {
          if (nums[i] >= nums[i + 1]) {
            ok = false;
            break;
          }
        }
        if (!ok) continue;
        for (int i = p; i < q; i++) {
          if (nums[i] <= nums[i + 1]) {
            ok = false;
            break;
          }
        }
        if (!ok) continue;
        for (int i = q; i < n - 1; i++) {
          if (nums[i] >= nums[i + 1]) {
            ok = false;
            break;
          }
        }
        if (ok) return true;
      }
    }
    return false;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func isTrionic(nums []int) bool {
	n := len(nums)
	for p := 1; p < n-2; p++ {
		for q := p + 1; q < n-1; q++ {
			ok := true
			for i := 0; i < p; i++ {
				if nums[i] >= nums[i+1] {
					ok = false
					break
				}
			}
			if !ok {
				continue
			}
			for i := p; i < q; i++ {
				if nums[i] <= nums[i+1] {
					ok = false
					break
				}
			}
			if !ok {
				continue
			}
			for i := q; i < n-1; i++ {
				if nums[i] >= nums[i+1] {
					ok = false
					break
				}
			}
			if ok {
				return true
			}
		}
	}
	return false
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def is_trionic(nums)
  n = nums.length
  return false if n < 4
  (1...n - 2).each do |p|
    (p + 1...n - 1).each do |q|
      valid = true
      (0...p).each { |i| valid = false if nums[i] >= nums[i+1] }
      (p...q).each { |i| valid = false if nums[i] <= nums[i+1] }
      (q...n - 1).each { |i| valid = false if nums[i] >= nums[i+1] }
      return true if valid
    end
  end
  false
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def isTrionic(nums: Array[Int]): Boolean = {
    val n = nums.length
    if (n < 4) return false
    for (p <- 1 until n - 2) {
      for (q <- p + 1 until n - 1) {
        var valid = true
        for (i <- 0 until p) if (nums(i) >= nums(i + 1)) valid = false
        for (i <- p until q) if (nums(i) <= nums(i + 1)) valid = false
        for (i <- q until n - 1) if (nums(i) >= nums(i + 1)) valid = false
        if (valid) return true
      }
    }
    false
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn is_trionic(nums: Vec<i32>) -> bool {
        let n = nums.len();
        if n < 4 {
            return false;
        }
        for p in 1..n - 2 {
            for q in p + 1..n - 1 {
                let mut valid = true;
                for i in 0..p {
                    if nums[i] >= nums[i + 1] { valid = false; }
                }
                for i in p..q {
                    if nums[i] <= nums[i + 1] { valid = false; }
                }
                for i in q..n - 1 {
                    if nums[i] >= nums[i + 1] { valid = false; }
                }
                if valid {
                    return true;
                }
            }
        }
        false
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (is-trionic nums)
  (-> (listof exact-integer?) boolean?)
  (let* ([n (length nums)]
         [arr (list->vector nums)])
    (if (< n 4)
        #f
        (for*/or ([p (in-range 1 (- n 2))]
                  [q (in-range (+ p 1) (- n 1))])
          (and (for/and ([i (in-range 0 p)])
                 (< (vector-ref arr i) (vector-ref arr (+ i 1))))
               (for/and ([i (in-range p q)])
                 (> (vector-ref arr i) (vector-ref arr (+ i 1))))
               (for/and ([i (in-range q (- n 1))])
                 (< (vector-ref arr i) (vector-ref arr (+ i 1)))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec is_trionic(Nums :: [integer()]) -> boolean().
is_trionic(Nums) ->
  N = length(Nums),
  if
    N < 4 -> false;
    true ->
      Arr = list_to_tuple(Nums),
      check_p(1, N, Arr)
  end.

check_p(P, N, Arr) when P < N - 2 ->
  case check_q(P, P + 1, N, Arr) of
    true -> true;
    false -> check_p(P + 1, N, Arr)
  end;
check_p(_, _, _) -> false.

check_q(P, Q, N, Arr) when Q < N - 1 ->
  Valid = check_inc(0, P, Arr) andalso check_dec(P, Q, Arr) andalso check_inc(Q, N - 1, Arr),
  if
    Valid -> true;
    true -> check_q(P, Q + 1, N, Arr)
  end;
check_q(_, _, _, _) -> false.

check_inc(Start, End, Arr) ->
  lists:all(fun(I) -> element(I + 1, Arr) < element(I + 2, Arr) end, lists:seq(Start, End - 1)).

check_dec(Start, End, Arr) ->
  lists:all(fun(I) -> element(I + 1, Arr) > element(I + 2, Arr) end, lists:seq(Start, End - 1)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec is_trionic(nums :: [integer]) :: boolean
  def is_trionic(nums) do
    n = length(nums)
    if n < 4 do
      false
    else
      arr = List.to_tuple(nums)
      Enum.any?(1..(n - 3), fn p ->
        Enum.any?((p + 1)..(n - 2), fn q ->
          check_inc(arr, 0, p) and check_dec(arr, p, q) and check_inc(arr, q, n - 1)
        end)
      end)
    end
  end

  defp check_inc(arr, start_idx, end_idx) do
    Enum.all?(start_idx..(end_idx - 1), fn i ->
      elem(arr, i) < elem(arr, i + 1)
    end)
  end

  defp check_dec(arr, start_idx, end_idx) do
    Enum.all?(start_idx..(end_idx - 1), fn i ->
      elem(arr, i) > elem(arr, i + 1)
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n^3) where n is the length of the input array. There are two nested loops to select indices p and q, and inside these loops, we perform three linear checks to verify the strict monotonicity of the array segments.
- **Space Complexity:** O(1) as we only use a constant amount of extra space for loop counters and boolean flags, regardless of the size of the input array.
