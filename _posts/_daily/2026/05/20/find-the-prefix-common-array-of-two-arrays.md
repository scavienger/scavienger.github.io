---
layout: post
title: "Find the Prefix Common Array of Two Arrays"
date: 2026-05-20 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Bit Manipulation"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> findThePrefixCommonArray(vector<int>&\
        \ A, vector<int>& B) {\n        int n = A.size();\n        vector<int> C(n);\n\
        \        vector<int> freq(n + 1, 0);\n        int commonCount = 0;\n\n     \
        \   for (int i = 0; i < n; ++i) {\n            if (++freq[A[i]] == 2) {\n  \
        \              commonCount++;\n            }\n            if (++freq[B[i]] ==\
        \ 2) {\n                commonCount++;\n            }\n            C[i] = commonCount;\n\
        \        }\n\n        return C;\n    }\n};"
      java: "class Solution {\n    public int[] findThePrefixCommonArray(int[] A, int[]\
        \ B) {\n        int n = A.length;\n        int[] C = new int[n];\n        int[]\
        \ freq = new int[n + 1];\n        int commonCount = 0;\n\n        for (int i\
        \ = 0; i < n; i++) {\n            if (++freq[A[i]] == 2) {\n               \
        \ commonCount++;\n            }\n            if (++freq[B[i]] == 2) {\n    \
        \            commonCount++;\n            }\n            C[i] = commonCount;\n\
        \        }\n\n        return C;\n    }\n}"
      python: "class Solution(object):\n    def findThePrefixCommonArray(self, A, B):\n\
        \        \"\"\"\n        :type A: List[int]\n        :type B: List[int]\n  \
        \      :rtype: List[int]\n        \"\"\"\n        n = len(A)\n        C = [0]\
        \ * n\n        freq = [0] * (n + 1)\n        common_count = 0\n\n        for\
        \ i in range(n):\n            freq[A[i]] += 1\n            if freq[A[i]] ==\
        \ 2:\n                common_count += 1\n\n            freq[B[i]] += 1\n   \
        \         if freq[B[i]] == 2:\n                common_count += 1\n\n       \
        \     C[i] = common_count\n\n        return C"
      python3: "class Solution:\n    def findThePrefixCommonArray(self, A: List[int],\
        \ B: List[int]) -> List[int]:\n        n = len(A)\n        C = [0] * n\n   \
        \     freq = [0] * (n + 1)\n        common_count = 0\n\n        for i in range(n):\n\
        \            freq[A[i]] += 1\n            if freq[A[i]] == 2:\n            \
        \    common_count += 1\n\n            freq[B[i]] += 1\n            if freq[B[i]]\
        \ == 2:\n                common_count += 1\n\n            C[i] = common_count\n\
        \n        return C"
      c: "/**\n * Note: The returned array must be malloced, assume caller calls free().\n\
        \ */\nint* findThePrefixCommonArray(int* A, int ASize, int* B, int BSize, int*\
        \ returnSize) {\n    int* C = (int*)malloc(ASize * sizeof(int));\n    int freq[51]\
        \ = {0};\n    int commonCount = 0;\n    *returnSize = ASize;\n\n    for (int\
        \ i = 0; i < ASize; i++) {\n        freq[A[i]]++;\n        if (freq[A[i]] ==\
        \ 2) {\n            commonCount++;\n        }\n        freq[B[i]]++;\n     \
        \   if (freq[B[i]] == 2) {\n            commonCount++;\n        }\n        C[i]\
        \ = commonCount;\n    }\n\n    return C;\n}"
      csharp: "public class Solution {\n    public int[] FindThePrefixCommonArray(int[]\
        \ A, int[] B) {\n        int n = A.Length;\n        int[] C = new int[n];\n\
        \        int[] freq = new int[n + 1];\n        int commonCount = 0;\n      \
        \  for (int i = 0; i < n; i++) {\n            freq[A[i]]++;\n            if\
        \ (freq[A[i]] == 2) {\n                commonCount++;\n            }\n     \
        \       freq[B[i]]++;\n            if (freq[B[i]] == 2) {\n                commonCount++;\n\
        \            }\n            C[i] = commonCount;\n        }\n        return C;\n\
        \    }\n}"
      javascript: "/**\n * @param {number[]} A\n * @param {number[]} B\n * @return {number[]}\n\
        \ */\nvar findThePrefixCommonArray = function(A, B) {\n    const n = A.length;\n\
        \    const C = new Array(n);\n    const freq = new Array(n + 1).fill(0);\n \
        \   let commonCount = 0;\n    for (let i = 0; i < n; i++) {\n        freq[A[i]]++;\n\
        \        if (freq[A[i]] === 2) {\n            commonCount++;\n        }\n  \
        \      freq[B[i]]++;\n        if (freq[B[i]] === 2) {\n            commonCount++;\n\
        \        }\n        C[i] = commonCount;\n    }\n    return C;\n};"
      typescript: "function findThePrefixCommonArray(A: number[], B: number[]): number[]\
        \ {\n    const n = A.length;\n    const C: number[] = new Array(n);\n    const\
        \ freq: number[] = new Array(n + 1).fill(0);\n    let commonCount = 0;\n   \
        \ for (let i = 0; i < n; i++) {\n        freq[A[i]]++;\n        if (freq[A[i]]\
        \ === 2) {\n            commonCount++;\n        }\n        freq[B[i]]++;\n \
        \       if (freq[B[i]] === 2) {\n            commonCount++;\n        }\n   \
        \     C[i] = commonCount;\n    }\n    return C;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $A\n     * @param Integer[]\
        \ $B\n     * @return Integer[]\n     */\n    function findThePrefixCommonArray($A,\
        \ $B) {\n        $n = count($A);\n        $C = array_fill(0, $n, 0);\n     \
        \   $freq = array_fill(0, $n + 1, 0);\n        $commonCount = 0;\n        for\
        \ ($i = 0; $i < $n; $i++) {\n            $freq[$A[$i]]++;\n            if ($freq[$A[$i]]\
        \ == 2) {\n                $commonCount++;\n            }\n            $freq[$B[$i]]++;\n\
        \            if ($freq[$B[$i]] == 2) {\n                $commonCount++;\n  \
        \          }\n            $C[$i] = $commonCount;\n        }\n        return\
        \ $C;\n    }\n}"
      swift: "class Solution {\n    func findThePrefixCommonArray(_ A: [Int], _ B: [Int])\
        \ -> [Int] {\n        let n = A.count\n        var C = [Int](repeating: 0, count:\
        \ n)\n        var freq = [Int](repeating: 0, count: n + 1)\n        var commonCount\
        \ = 0\n        for i in 0..<n {\n            freq[A[i]] += 1\n            if\
        \ freq[A[i]] == 2 {\n                commonCount += 1\n            }\n     \
        \       freq[B[i]] += 1\n            if freq[B[i]] == 2 {\n                commonCount\
        \ += 1\n            }\n            C[i] = commonCount\n        }\n        return\
        \ C\n    }\n}"
      kotlin: "class Solution {\n    fun findThePrefixCommonArray(A: IntArray, B: IntArray):\
        \ IntArray {\n        val n = A.size\n        val res = IntArray(n)\n      \
        \  val freq = IntArray(n + 1)\n        var commonCount = 0\n        for (i in\
        \ 0 until n) {\n            freq[A[i]]++\n            if (freq[A[i]] == 2) {\n\
        \                commonCount++\n            }\n            freq[B[i]]++\n  \
        \          if (freq[B[i]] == 2) {\n                commonCount++\n         \
        \   }\n            res[i] = commonCount\n        }\n        return res\n   \
        \ }\n}"
      dart: "class Solution {\n  List<int> findThePrefixCommonArray(List<int> A, List<int>\
        \ B) {\n    int n = A.length;\n    List<int> res = List.filled(n, 0);\n    List<int>\
        \ freq = List.filled(n + 1, 0);\n    int commonCount = 0;\n    for (int i =\
        \ 0; i < n; i++) {\n      freq[A[i]]++;\n      if (freq[A[i]] == 2) {\n    \
        \    commonCount++;\n      }\n      freq[B[i]]++;\n      if (freq[B[i]] == 2)\
        \ {\n        commonCount++;\n      }\n      res[i] = commonCount;\n    }\n \
        \   return res;\n  }\n}"
      go: "func findThePrefixCommonArray(A []int, B []int) []int {\n    n := len(A)\n\
        \    res := make([]int, n)\n    freq := make([]int, n+1)\n    commonCount :=\
        \ 0\n    for i := 0; i < n; i++ {\n        freq[A[i]]++\n        if freq[A[i]]\
        \ == 2 {\n            commonCount++\n        }\n        freq[B[i]]++\n     \
        \   if freq[B[i]] == 2 {\n            commonCount++\n        }\n        res[i]\
        \ = commonCount\n    }\n    return res\n}"
      ruby: "# @param {Integer[]} a\n# @param {Integer[]} b\n# @return {Integer[]}\n\
        def find_the_prefix_common_array(a, b)\n    n = a.length\n    res = Array.new(n,\
        \ 0)\n    freq = Array.new(n + 1, 0)\n    common_count = 0\n    (0...n).each\
        \ do |i|\n        freq[a[i]] += 1\n        common_count += 1 if freq[a[i]] ==\
        \ 2\n        freq[b[i]] += 1\n        common_count += 1 if freq[b[i]] == 2\n\
        \        res[i] = common_count\n    end\n    res\nend"
      scala: "object Solution {\n    def findThePrefixCommonArray(A: Array[Int], B:\
        \ Array[Int]): Array[Int] = {\n        val n = A.length\n        val res = new\
        \ Array[Int](n)\n        val freq = new Array[Int](n + 1)\n        var commonCount\
        \ = 0\n        for (i <- 0 until n) {\n            freq(A(i)) += 1\n       \
        \     if (freq(A(i)) == 2) {\n                commonCount += 1\n           \
        \ }\n            freq(B(i)) += 1\n            if (freq(B(i)) == 2) {\n     \
        \           commonCount += 1\n            }\n            res(i) = commonCount\n\
        \        }\n        res\n    }\n}"
      rust: "impl Solution {\n    pub fn find_the_prefix_common_array(a: Vec<i32>, b:\
        \ Vec<i32>) -> Vec<i32> {\n        let n = a.len();\n        let mut counts\
        \ = vec![0; n + 1];\n        let mut common = 0;\n        let mut result = Vec::with_capacity(n);\n\
        \        for i in 0..n {\n            let val_a = a[i] as usize;\n         \
        \   counts[val_a] += 1;\n            if counts[val_a] == 2 {\n             \
        \   common += 1;\n            }\n            let val_b = b[i] as usize;\n  \
        \          counts[val_b] += 1;\n            if counts[val_b] == 2 {\n      \
        \          common += 1;\n            }\n            result.push(common);\n \
        \       }\n        result\n    }\n}"
      racket: "(define/contract (find-the-prefix-common-array A B)\n  (-> (listof exact-integer?)\
        \ (listof exact-integer?) (listof exact-integer?))\n  (let loop ([A A] [B B]\
        \ [seen (set)] [common 0] [res '()])\n    (if (null? A)\n        (reverse res)\n\
        \        (let* ([val-a (car A)]\n               [val-b (car B)]\n          \
        \     [common-a (if (set-member? seen val-a) (+ common 1) common)]\n       \
        \        [seen-a (set-add seen val-a)]\n               [common-b (if (set-member?\
        \ seen-a val-b) (+ common-a 1) common-a)]\n               [seen-b (set-add seen-a\
        \ val-b)])\n          (loop (cdr A) (cdr B) seen-b common-b (cons common-b res))))))"
      erlang: "-spec find_the_prefix_common_array(A :: [integer()], B :: [integer()])\
        \ -> [integer()].\nfind_the_prefix_common_array(A, B) ->\n    solve(A, B, sets:new(),\
        \ 0, []).\n\nsolve([], [], _Seen, _Common, Acc) ->\n    lists:reverse(Acc);\n\
        solve([H1 | T1], [H2 | T2], Seen, Common, Acc) ->\n    {Seen1, Common1} = case\
        \ sets:is_element(H1, Seen) of\n        true -> {Seen, Common + 1};\n      \
        \  false -> {sets:add_element(H1, Seen), Common}\n    end,\n    {Seen2, Common2}\
        \ = case sets:is_element(H2, Seen1) of\n        true -> {Seen1, Common1 + 1};\n\
        \        false -> {sets:add_element(H2, Seen1), Common1}\n    end,\n    solve(T1,\
        \ T2, Seen2, Common2, [Common2 | Acc])."
      elixir: "defmodule Solution do\n  @spec find_the_prefix_common_array(a :: [integer],\
        \ b :: [integer]) :: [integer]\n  def find_the_prefix_common_array(a, b) do\n\
        \    {_seen, _common, res} = \n      Enum.zip(a, b)\n      |> Enum.reduce({MapSet.new(),\
        \ 0, []}, fn {val_a, val_b}, {seen, common, acc} ->\n        {common_a, seen_a}\
        \ = if MapSet.member?(seen, val_a), do: {common + 1, seen}, else: {common, MapSet.put(seen,\
        \ val_a)}\n        {common_b, seen_b} = if MapSet.member?(seen_a, val_b), do:\
        \ {common_a + 1, seen_a}, else: {common_a, MapSet.put(seen_a, val_b)}\n    \
        \    {seen_b, common_b, [common_b | acc]}\n      end)\n\n    Enum.reverse(res)\n\
        \  end\nend"
    approach: 'The algorithm uses a frequency-based tracking system to identify common
      elements in the prefixes of two permutations. Since both arrays A and B are permutations
      of the same $n$ integers, an element is common to both prefixes at index $i$ if
      and only if it has appeared twice in total when considering the elements $A[0...i]$
      and $B[0...i]$ combined. We use a frequency array to store the counts of each
      integer as we iterate through both arrays simultaneously.


      At each index $i$, we increment the frequency counts for the current elements
      $A[i]$ and $B[i]$. Whenever a count reaches 2, it indicates that the number has
      now appeared once in the prefix of A and once in the prefix of B, so we increment
      a running counter of common elements. We then record the value of this counter
      in the result array at position $i$. This approach allows us to determine the
      prefix common counts efficiently in a single linear pass through the input arrays.'
    time_complexity: O(n) where n is the length of the permutations A and B. The algorithm
      performs a single pass through the arrays, and each update to the frequency array
      and common counter takes constant $O(1)$ time.
    space_complexity: O(n) to store the result array and the frequency array. Specifically,
      the frequency array requires $O(n)$ space to store counts for all integers from
      1 to $n$.
    elapsed_time: 164.4078814983368
    model: gemini-3-flash-preview
    generated_at: '2026-05-20 02:39:35 '
---

## Problem #2657: Find the Prefix Common Array of Two Arrays

**Difficulty:** Medium

**Topics:** Array, Hash Table, Bit Manipulation

## Problem Description

<p>You are given two <strong>0-indexed </strong>integer<strong> </strong>permutations <code>A</code> and <code>B</code> of length <code>n</code>.</p>

<p>A <strong>prefix common array</strong> of <code>A</code> and <code>B</code> is an array <code>C</code> such that <code>C[i]</code> is equal to the count of numbers that are present at or before the index <code>i</code> in both <code>A</code> and <code>B</code>.</p>

<p>Return <em>the <strong>prefix common array</strong> of </em><code>A</code><em> and </em><code>B</code>.</p>

<p>A sequence of <code>n</code> integers is called a&nbsp;<strong>permutation</strong> if it contains all integers from <code>1</code> to <code>n</code> exactly once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> A = [1,3,2,4], B = [3,1,2,4]
<strong>Output:</strong> [0,2,3,4]
<strong>Explanation:</strong> At i = 0: no number is common, so C[0] = 0.
At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> A = [2,3,1], B = [3,1,2]
<strong>Output:</strong> [0,1,3]
<strong>Explanation:</strong> At i = 0: no number is common, so C[0] = 0.
At i = 1: only 3 is common in A and B, so C[1] = 1.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= A.length == B.length == n &lt;= 50</code></li>
	<li><code>1 &lt;= A[i], B[i] &lt;= n</code></li>
	<li><code>It is guaranteed that A and B are both a permutation of n integers.</code></li>
</ul>


## Hints

1. Consider keeping a frequency array that stores the count of occurrences of each number till index i.

2. If a number occurred two times, it means it occurred in both A and B since they’re both permutations so add one to the answer.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm uses a frequency-based tracking system to identify common elements in the prefixes of two permutations. Since both arrays A and B are permutations of the same $n$ integers, an element is common to both prefixes at index $i$ if and only if it has appeared twice in total when considering the elements $A[0...i]$ and $B[0...i]$ combined. We use a frequency array to store the counts of each integer as we iterate through both arrays simultaneously.

At each index $i$, we increment the frequency counts for the current elements $A[i]$ and $B[i]$. Whenever a count reaches 2, it indicates that the number has now appeared once in the prefix of A and once in the prefix of B, so we increment a running counter of common elements. We then record the value of this counter in the result array at position $i$. This approach allows us to determine the prefix common counts efficiently in a single linear pass through the input arrays.

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
    vector<int> findThePrefixCommonArray(vector<int>& A, vector<int>& B) {
        int n = A.size();
        vector<int> C(n);
        vector<int> freq(n + 1, 0);
        int commonCount = 0;

        for (int i = 0; i < n; ++i) {
            if (++freq[A[i]] == 2) {
                commonCount++;
            }
            if (++freq[B[i]] == 2) {
                commonCount++;
            }
            C[i] = commonCount;
        }

        return C;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int[] findThePrefixCommonArray(int[] A, int[] B) {
        int n = A.length;
        int[] C = new int[n];
        int[] freq = new int[n + 1];
        int commonCount = 0;

        for (int i = 0; i < n; i++) {
            if (++freq[A[i]] == 2) {
                commonCount++;
            }
            if (++freq[B[i]] == 2) {
                commonCount++;
            }
            C[i] = commonCount;
        }

        return C;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        n = len(A)
        C = [0] * n
        freq = [0] * (n + 1)
        common_count = 0

        for i in range(n):
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                common_count += 1

            freq[B[i]] += 1
            if freq[B[i]] == 2:
                common_count += 1

            C[i] = common_count

        return C
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        C = [0] * n
        freq = [0] * (n + 1)
        common_count = 0

        for i in range(n):
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                common_count += 1

            freq[B[i]] += 1
            if freq[B[i]] == 2:
                common_count += 1

            C[i] = common_count

        return C
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findThePrefixCommonArray(int* A, int ASize, int* B, int BSize, int* returnSize) {
    int* C = (int*)malloc(ASize * sizeof(int));
    int freq[51] = {0};
    int commonCount = 0;
    *returnSize = ASize;

    for (int i = 0; i < ASize; i++) {
        freq[A[i]]++;
        if (freq[A[i]] == 2) {
            commonCount++;
        }
        freq[B[i]]++;
        if (freq[B[i]] == 2) {
            commonCount++;
        }
        C[i] = commonCount;
    }

    return C;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int[] FindThePrefixCommonArray(int[] A, int[] B) {
        int n = A.Length;
        int[] C = new int[n];
        int[] freq = new int[n + 1];
        int commonCount = 0;
        for (int i = 0; i < n; i++) {
            freq[A[i]]++;
            if (freq[A[i]] == 2) {
                commonCount++;
            }
            freq[B[i]]++;
            if (freq[B[i]] == 2) {
                commonCount++;
            }
            C[i] = commonCount;
        }
        return C;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number[]}
 */
var findThePrefixCommonArray = function(A, B) {
    const n = A.length;
    const C = new Array(n);
    const freq = new Array(n + 1).fill(0);
    let commonCount = 0;
    for (let i = 0; i < n; i++) {
        freq[A[i]]++;
        if (freq[A[i]] === 2) {
            commonCount++;
        }
        freq[B[i]]++;
        if (freq[B[i]] === 2) {
            commonCount++;
        }
        C[i] = commonCount;
    }
    return C;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function findThePrefixCommonArray(A: number[], B: number[]): number[] {
    const n = A.length;
    const C: number[] = new Array(n);
    const freq: number[] = new Array(n + 1).fill(0);
    let commonCount = 0;
    for (let i = 0; i < n; i++) {
        freq[A[i]]++;
        if (freq[A[i]] === 2) {
            commonCount++;
        }
        freq[B[i]]++;
        if (freq[B[i]] === 2) {
            commonCount++;
        }
        C[i] = commonCount;
    }
    return C;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $A
     * @param Integer[] $B
     * @return Integer[]
     */
    function findThePrefixCommonArray($A, $B) {
        $n = count($A);
        $C = array_fill(0, $n, 0);
        $freq = array_fill(0, $n + 1, 0);
        $commonCount = 0;
        for ($i = 0; $i < $n; $i++) {
            $freq[$A[$i]]++;
            if ($freq[$A[$i]] == 2) {
                $commonCount++;
            }
            $freq[$B[$i]]++;
            if ($freq[$B[$i]] == 2) {
                $commonCount++;
            }
            $C[$i] = $commonCount;
        }
        return $C;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func findThePrefixCommonArray(_ A: [Int], _ B: [Int]) -> [Int] {
        let n = A.count
        var C = [Int](repeating: 0, count: n)
        var freq = [Int](repeating: 0, count: n + 1)
        var commonCount = 0
        for i in 0..<n {
            freq[A[i]] += 1
            if freq[A[i]] == 2 {
                commonCount += 1
            }
            freq[B[i]] += 1
            if freq[B[i]] == 2 {
                commonCount += 1
            }
            C[i] = commonCount
        }
        return C
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun findThePrefixCommonArray(A: IntArray, B: IntArray): IntArray {
        val n = A.size
        val res = IntArray(n)
        val freq = IntArray(n + 1)
        var commonCount = 0
        for (i in 0 until n) {
            freq[A[i]]++
            if (freq[A[i]] == 2) {
                commonCount++
            }
            freq[B[i]]++
            if (freq[B[i]] == 2) {
                commonCount++
            }
            res[i] = commonCount
        }
        return res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<int> findThePrefixCommonArray(List<int> A, List<int> B) {
    int n = A.length;
    List<int> res = List.filled(n, 0);
    List<int> freq = List.filled(n + 1, 0);
    int commonCount = 0;
    for (int i = 0; i < n; i++) {
      freq[A[i]]++;
      if (freq[A[i]] == 2) {
        commonCount++;
      }
      freq[B[i]]++;
      if (freq[B[i]] == 2) {
        commonCount++;
      }
      res[i] = commonCount;
    }
    return res;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func findThePrefixCommonArray(A []int, B []int) []int {
    n := len(A)
    res := make([]int, n)
    freq := make([]int, n+1)
    commonCount := 0
    for i := 0; i < n; i++ {
        freq[A[i]]++
        if freq[A[i]] == 2 {
            commonCount++
        }
        freq[B[i]]++
        if freq[B[i]] == 2 {
            commonCount++
        }
        res[i] = commonCount
    }
    return res
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} a
# @param {Integer[]} b
# @return {Integer[]}
def find_the_prefix_common_array(a, b)
    n = a.length
    res = Array.new(n, 0)
    freq = Array.new(n + 1, 0)
    common_count = 0
    (0...n).each do |i|
        freq[a[i]] += 1
        common_count += 1 if freq[a[i]] == 2
        freq[b[i]] += 1
        common_count += 1 if freq[b[i]] == 2
        res[i] = common_count
    end
    res
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def findThePrefixCommonArray(A: Array[Int], B: Array[Int]): Array[Int] = {
        val n = A.length
        val res = new Array[Int](n)
        val freq = new Array[Int](n + 1)
        var commonCount = 0
        for (i <- 0 until n) {
            freq(A(i)) += 1
            if (freq(A(i)) == 2) {
                commonCount += 1
            }
            freq(B(i)) += 1
            if (freq(B(i)) == 2) {
                commonCount += 1
            }
            res(i) = commonCount
        }
        res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn find_the_prefix_common_array(a: Vec<i32>, b: Vec<i32>) -> Vec<i32> {
        let n = a.len();
        let mut counts = vec![0; n + 1];
        let mut common = 0;
        let mut result = Vec::with_capacity(n);
        for i in 0..n {
            let val_a = a[i] as usize;
            counts[val_a] += 1;
            if counts[val_a] == 2 {
                common += 1;
            }
            let val_b = b[i] as usize;
            counts[val_b] += 1;
            if counts[val_b] == 2 {
                common += 1;
            }
            result.push(common);
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
(define/contract (find-the-prefix-common-array A B)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  (let loop ([A A] [B B] [seen (set)] [common 0] [res '()])
    (if (null? A)
        (reverse res)
        (let* ([val-a (car A)]
               [val-b (car B)]
               [common-a (if (set-member? seen val-a) (+ common 1) common)]
               [seen-a (set-add seen val-a)]
               [common-b (if (set-member? seen-a val-b) (+ common-a 1) common-a)]
               [seen-b (set-add seen-a val-b)])
          (loop (cdr A) (cdr B) seen-b common-b (cons common-b res))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec find_the_prefix_common_array(A :: [integer()], B :: [integer()]) -> [integer()].
find_the_prefix_common_array(A, B) ->
    solve(A, B, sets:new(), 0, []).

solve([], [], _Seen, _Common, Acc) ->
    lists:reverse(Acc);
solve([H1 | T1], [H2 | T2], Seen, Common, Acc) ->
    {Seen1, Common1} = case sets:is_element(H1, Seen) of
        true -> {Seen, Common + 1};
        false -> {sets:add_element(H1, Seen), Common}
    end,
    {Seen2, Common2} = case sets:is_element(H2, Seen1) of
        true -> {Seen1, Common1 + 1};
        false -> {sets:add_element(H2, Seen1), Common1}
    end,
    solve(T1, T2, Seen2, Common2, [Common2 | Acc]).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec find_the_prefix_common_array(a :: [integer], b :: [integer]) :: [integer]
  def find_the_prefix_common_array(a, b) do
    {_seen, _common, res} = 
      Enum.zip(a, b)
      |> Enum.reduce({MapSet.new(), 0, []}, fn {val_a, val_b}, {seen, common, acc} ->
        {common_a, seen_a} = if MapSet.member?(seen, val_a), do: {common + 1, seen}, else: {common, MapSet.put(seen, val_a)}
        {common_b, seen_b} = if MapSet.member?(seen_a, val_b), do: {common_a + 1, seen_a}, else: {common_a, MapSet.put(seen_a, val_b)}
        {seen_b, common_b, [common_b | acc]}
      end)

    Enum.reverse(res)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the permutations A and B. The algorithm performs a single pass through the arrays, and each update to the frequency array and common counter takes constant $O(1)$ time.
- **Space Complexity:** O(n) to store the result array and the frequency array. Specifically, the frequency array requires $O(n)$ space to store counts for all integers from 1 to $n$.
