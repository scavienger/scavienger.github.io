---
layout: post
title: "Number of Unique XOR Triplets II"
date: 2026-07-24 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Math", "Bit Manipulation", "Enumeration"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/number-of-unique-xor-triplets-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int uniqueXorTriplets(vector<int>& nums)\
        \ {\n        bool seen[2048] = {false};\n        vector<int> S;\n        for\
        \ (int x : nums) {\n            if (!seen[x]) {\n                seen[x] = true;\n\
        \                S.push_back(x);\n            }\n        }\n\n        bool pair_exists[2048]\
        \ = {false};\n        for (int i = 0; i < S.size(); ++i) {\n            for\
        \ (int j = i; j < S.size(); ++j) {\n                pair_exists[S[i] ^ S[j]]\
        \ = true;\n            }\n        }\n\n        vector<int> Q;\n        for (int\
        \ i = 0; i < 2048; ++i) {\n            if (pair_exists[i]) Q.push_back(i);\n\
        \        }\n\n        bool triplets[2048] = {false};\n        for (int q : Q)\
        \ {\n            for (int z : S) {\n                triplets[q ^ z] = true;\n\
        \            }\n        }\n\n        int count = 0;\n        for (int i = 0;\
        \ i < 2048; ++i) {\n            if (triplets[i]) count++;\n        }\n     \
        \   return count;\n    }\n};"
      java: "class Solution {\n    public int uniqueXorTriplets(int[] nums) {\n    \
        \    boolean[] seen = new boolean[2048];\n        int uniqueCount = 0;\n   \
        \     for (int x : nums) {\n            if (!seen[x]) {\n                seen[x]\
        \ = true;\n                uniqueCount++;\n            }\n        }\n\n    \
        \    int[] S = new int[uniqueCount];\n        int idx = 0;\n        for (int\
        \ i = 0; i < 2048; i++) {\n            if (seen[i]) S[idx++] = i;\n        }\n\
        \n        boolean[] pairExists = new boolean[2048];\n        for (int i = 0;\
        \ i < S.length; i++) {\n            for (int j = i; j < S.length; j++) {\n \
        \               pairExists[S[i] ^ S[j]] = true;\n            }\n        }\n\n\
        \        int pairCount = 0;\n        for (int i = 0; i < 2048; i++) {\n    \
        \        if (pairExists[i]) pairCount++;\n        }\n        int[] Q = new int[pairCount];\n\
        \        idx = 0;\n        for (int i = 0; i < 2048; i++) {\n            if\
        \ (pairExists[i]) Q[idx++] = i;\n        }\n\n        boolean[] triplets = new\
        \ boolean[2048];\n        for (int q : Q) {\n            for (int z : S) {\n\
        \                triplets[q ^ z] = true;\n            }\n        }\n\n     \
        \   int totalCount = 0;\n        for (int i = 0; i < 2048; i++) {\n        \
        \    if (triplets[i]) totalCount++;\n        }\n        return totalCount;\n\
        \    }\n}"
      python: "class Solution(object):\n    def uniqueXorTriplets(self, nums):\n   \
        \     \"\"\"\n        :type nums: List[int]\n        :rtype: int\n        \"\
        \"\"\n        S = list(set(nums))\n        pairs = [False] * 2048\n        for\
        \ i in range(len(S)):\n            for j in range(i, len(S)):\n            \
        \    pairs[S[i] ^ S[j]] = True\n\n        Q = [q for q in range(2048) if pairs[q]]\n\
        \n        triplets = [False] * 2048\n        for q in Q:\n            for z\
        \ in S:\n                triplets[q ^ z] = True\n\n        return sum(triplets)"
      python3: "class Solution:\n    def uniqueXorTriplets(self, nums: List[int]) ->\
        \ int:\n        S = list(set(nums))\n        pairs = [False] * 2048\n      \
        \  for i in range(len(S)):\n            for j in range(i, len(S)):\n       \
        \         pairs[S[i] ^ S[j]] = True\n\n        Q = [q for q in range(2048) if\
        \ pairs[q]]\n\n        triplets = [False] * 2048\n        for q in Q:\n    \
        \        for z in S:\n                triplets[q ^ z] = True\n\n        return\
        \ sum(triplets)"
      c: "int uniqueXorTriplets(int* nums, int numsSize) {\n    int seen[2048] = {0};\n\
        \    int S[1501];\n    int sSize = 0;\n    for (int i = 0; i < numsSize; i++)\
        \ {\n        if (!seen[nums[i]]) {\n            seen[nums[i]] = 1;\n       \
        \     S[sSize++] = nums[i];\n        }\n    }\n\n    int pairExists[2048] =\
        \ {0};\n    for (int i = 0; i < sSize; i++) {\n        for (int j = i; j < sSize;\
        \ j++) {\n            pairExists[S[i] ^ S[j]] = 1;\n        }\n    }\n\n   \
        \ int Q[2048];\n    int qSize = 0;\n    for (int i = 0; i < 2048; i++) {\n \
        \       if (pairExists[i]) {\n            Q[qSize++] = i;\n        }\n    }\n\
        \n    int triplets[2048] = {0};\n    for (int i = 0; i < qSize; i++) {\n   \
        \     for (int j = 0; j < sSize; j++) {\n            triplets[Q[i] ^ S[j]] =\
        \ 1;\n        }\n    }\n\n    int count = 0;\n    for (int i = 0; i < 2048;\
        \ i++) {\n        if (triplets[i]) count++;\n    }\n    return count;\n}"
      csharp: "public class Solution {\n    public int UniqueXorTriplets(int[] nums)\
        \ {\n        bool[] hasU = new bool[2048];\n        foreach (int n in nums)\
        \ {\n            hasU[n] = true;\n        }\n\n        int[] U = new int[2048];\n\
        \        int uCount = 0;\n        for (int i = 0; i < 2048; i++) {\n       \
        \     if (hasU[i]) {\n                U[uCount++] = i;\n            }\n    \
        \    }\n\n        bool[] hasP = new bool[2048];\n        for (int i = 0; i <\
        \ uCount; i++) {\n            for (int j = i; j < uCount; j++) {\n         \
        \       hasP[U[i] ^ U[j]] = true;\n            }\n        }\n\n        bool[]\
        \ hasS = new bool[2048];\n        int count = 0;\n        for (int p = 0; p\
        \ < 2048; p++) {\n            if (hasP[p]) {\n                for (int k = 0;\
        \ k < uCount; k++) {\n                    int val = p ^ U[k];\n            \
        \        if (!hasS[val]) {\n                        hasS[val] = true;\n    \
        \                    count++;\n                    }\n                }\n  \
        \          }\n        }\n\n        return count;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar uniqueXorTriplets\
        \ = function(nums) {\n    const hasU = new Uint8Array(2048);\n    for (let i\
        \ = 0; i < nums.length; i++) {\n        hasU[nums[i]] = 1;\n    }\n\n    const\
        \ U = [];\n    for (let i = 0; i < 2048; i++) {\n        if (hasU[i]) {\n  \
        \          U.push(i);\n        }\n    }\n\n    const hasP = new Uint8Array(2048);\n\
        \    const uLen = U.length;\n    for (let i = 0; i < uLen; i++) {\n        for\
        \ (let j = i; j < uLen; j++) {\n            hasP[U[i] ^ U[j]] = 1;\n       \
        \ }\n    }\n\n    const hasS = new Uint8Array(2048);\n    let count = 0;\n \
        \   for (let p = 0; p < 2048; p++) {\n        if (hasP[p] === 1) {\n       \
        \     for (let k = 0; k < uLen; k++) {\n                const val = p ^ U[k];\n\
        \                if (hasS[val] === 0) {\n                    hasS[val] = 1;\n\
        \                    count++;\n                }\n            }\n        }\n\
        \    }\n\n    return count;\n};"
      typescript: "function uniqueXorTriplets(nums: number[]): number {\n    const hasU\
        \ = new Uint8Array(2048);\n    for (let i = 0; i < nums.length; i++) {\n   \
        \     hasU[nums[i]] = 1;\n    }\n\n    const U: number[] = [];\n    for (let\
        \ i = 0; i < 2048; i++) {\n        if (hasU[i]) {\n            U.push(i);\n\
        \        }\n    }\n\n    const hasP = new Uint8Array(2048);\n    const uLen\
        \ = U.length;\n    for (let i = 0; i < uLen; i++) {\n        for (let j = i;\
        \ j < uLen; j++) {\n            hasP[U[i] ^ U[j]] = 1;\n        }\n    }\n\n\
        \    const hasS = new Uint8Array(2048);\n    let count = 0;\n    for (let p\
        \ = 0; p < 2048; p++) {\n        if (hasP[p] === 1) {\n            for (let\
        \ k = 0; k < uLen; k++) {\n                const val = p ^ U[k];\n         \
        \       if (hasS[val] === 0) {\n                    hasS[val] = 1;\n       \
        \             count++;\n                }\n            }\n        }\n    }\n\
        \n    return count;\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function uniqueXorTriplets($nums) {\n        $hasU =\
        \ array_fill(0, 2048, false);\n        foreach ($nums as $n) {\n           \
        \ $hasU[$n] = true;\n        }\n\n        $U = [];\n        for ($i = 0; $i\
        \ < 2048; $i++) {\n            if ($hasU[$i]) {\n                $U[] = $i;\n\
        \            }\n        }\n\n        $hasP = array_fill(0, 2048, false);\n \
        \       $uCount = count($U);\n        for ($i = 0; $i < $uCount; $i++) {\n \
        \           for ($j = $i; $j < $uCount; $j++) {\n                $hasP[$U[$i]\
        \ ^ $U[$j]] = true;\n            }\n        }\n\n        $hasS = array_fill(0,\
        \ 2048, false);\n        $count = 0;\n        for ($p = 0; $p < 2048; $p++)\
        \ {\n            if ($hasP[$p]) {\n                foreach ($U as $z) {\n  \
        \                  $val = $p ^ $z;\n                    if (!$hasS[$val]) {\n\
        \                        $hasS[$val] = true;\n                        $count++;\n\
        \                    }\n                }\n            }\n        }\n\n    \
        \    return $count;\n    }\n}"
      swift: "class Solution {\n    func uniqueXorTriplets(_ nums: [Int]) -> Int {\n\
        \        var hasU = [Bool](repeating: false, count: 2048)\n        for n in\
        \ nums {\n            hasU[n] = true\n        }\n\n        var U = [Int]()\n\
        \        for i in 0..<2048 {\n            if hasU[i] {\n                U.append(i)\n\
        \            }\n        }\n\n        var hasP = [Bool](repeating: false, count:\
        \ 2048)\n        let uCount = U.count\n        if uCount > 0 {\n           \
        \ for i in 0..<uCount {\n                for j in i..<uCount {\n           \
        \         hasP[U[i] ^ U[j]] = true\n                }\n            }\n     \
        \   }\n\n        var hasS = [Bool](repeating: false, count: 2048)\n        var\
        \ count = 0\n        for p in 0..<2048 {\n            if hasP[p] {\n       \
        \         for z in U {\n                    let val = p ^ z\n              \
        \      if !hasS[val] {\n                        hasS[val] = true\n         \
        \               count += 1\n                    }\n                }\n     \
        \       }\n        }\n\n        return count\n    }\n}"
      kotlin: "class Solution {\n    fun uniqueXorTriplets(nums: IntArray): Int {\n\
        \        val uniqueNums = nums.distinct().toIntArray()\n        val n = uniqueNums.size\n\
        \        val canXor2 = BooleanArray(2048)\n\n        for (i in 0 until n) {\n\
        \            for (j in i until n) {\n                canXor2[uniqueNums[i] xor\
        \ uniqueNums[j]] = true\n            }\n        }\n\n        val canXor3 = BooleanArray(2048)\n\
        \        for (v2 in 0 until 2048) {\n            if (canXor2[v2]) {\n      \
        \          for (z in uniqueNums) {\n                    canXor3[v2 xor z] =\
        \ true\n                }\n            }\n        }\n\n        var count = 0\n\
        \        for (i in 0 until 2048) {\n            if (canXor3[i]) count++\n  \
        \      }\n        return count\n    }\n}"
      dart: "class Solution {\n  int uniqueXorTriplets(List<int> nums) {\n    var uniqueSet\
        \ = nums.toSet().toList();\n    int n = uniqueSet.length;\n    var canXor2 =\
        \ List<bool>.filled(2048, false);\n\n    for (int i = 0; i < n; i++) {\n   \
        \   for (int j = i; j < n; j++) {\n        canXor2[uniqueSet[i] ^ uniqueSet[j]]\
        \ = true;\n      }\n    }\n\n    var canXor3 = List<bool>.filled(2048, false);\n\
        \    for (int v2 = 0; v2 < 2048; v2++) {\n      if (canXor2[v2]) {\n       \
        \ for (int z in uniqueSet) {\n          canXor3[v2 ^ z] = true;\n        }\n\
        \      }\n    }\n\n    int count = 0;\n    for (int i = 0; i < 2048; i++) {\n\
        \      if (canXor3[i]) count++;\n    }\n    return count;\n  }\n}"
      go: "func uniqueXorTriplets(nums []int) int {\n    uniqueMap := make(map[int]bool)\n\
        \    for _, num := range nums {\n        uniqueMap[num] = true\n    }\n    var\
        \ uniqueNums []int\n    for num := range uniqueMap {\n        uniqueNums = append(uniqueNums,\
        \ num)\n    }\n\n    canXor2 := [2048]bool{}\n    for i := 0; i < len(uniqueNums);\
        \ i++ {\n        for j := i; j < len(uniqueNums); j++ {\n            canXor2[uniqueNums[i]^uniqueNums[j]]\
        \ = true\n        }\n    }\n\n    canXor3 := [2048]bool{}\n    for v2 := 0;\
        \ v2 < 2048; v2++ {\n        if canXor2[v2] {\n            for _, z := range\
        \ uniqueNums {\n                canXor3[v2^z] = true\n            }\n      \
        \  }\n    }\n\n    count := 0\n    for i := 0; i < 2048; i++ {\n        if canXor3[i]\
        \ {\n            count++\n        }\n    }\n    return count\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef unique_xor_triplets(nums)\n\
        \  unique_nums = nums.uniq\n  n = unique_nums.length\n  can_xor2 = Array.new(2048,\
        \ false)\n\n  i = 0\n  while i < n\n    j = i\n    while j < n\n      can_xor2[unique_nums[i]\
        \ ^ unique_nums[j]] = true\n      j += 1\n    end\n    i += 1\n  end\n\n  can_xor3\
        \ = Array.new(2048, false)\n  (0...2048).each do |v2|\n    if can_xor2[v2]\n\
        \      unique_nums.each do |z|\n        can_xor3[v2 ^ z] = true\n      end\n\
        \    end\n  end\n\n  can_xor3.count(true)\nend"
      scala: "object Solution {\n    def uniqueXorTriplets(nums: Array[Int]): Int =\
        \ {\n        val uniqueNums = nums.distinct\n        val n = uniqueNums.length\n\
        \        val canXor2 = new Array[Boolean](2048)\n\n        var i = 0\n     \
        \   while (i < n) {\n            var j = i\n            while (j < n) {\n  \
        \              canXor2(uniqueNums(i) ^ uniqueNums(j)) = true\n             \
        \   j += 1\n            }\n            i += 1\n        }\n\n        val canXor3\
        \ = new Array[Boolean](2048)\n        var v2 = 0\n        while (v2 < 2048)\
        \ {\n            if (canXor2(v2)) {\n                var k = 0\n           \
        \     while (k < n) {\n                    canXor3(v2 ^ uniqueNums(k)) = true\n\
        \                    k += 1\n                }\n            }\n            v2\
        \ += 1\n        }\n\n        var count = 0\n        var idx = 0\n        while\
        \ (idx < 2048) {\n            if (canXor3(idx)) count += 1\n            idx\
        \ += 1\n        }\n        count\n    }\n}"
      rust: "impl Solution {\n    pub fn unique_xor_triplets(nums: Vec<i32>) -> i32\
        \ {\n        let mut u = nums;\n        u.sort_unstable();\n        u.dedup();\n\
        \n        let mut in_p = [false; 2048];\n        for i in 0..u.len() {\n   \
        \         for j in i..u.len() {\n                in_p[(u[i] ^ u[j]) as usize]\
        \ = true;\n            }\n        }\n\n        let mut p_bits = Vec::new();\n\
        \        for i in 0..2048 {\n            if in_p[i] {\n                p_bits.push(i\
        \ as i32);\n            }\n        }\n\n        let mut in_t = [false; 2048];\n\
        \        for &x in &u {\n            for &p in &p_bits {\n                in_t[(x\
        \ ^ p) as usize] = true;\n            }\n        }\n\n        in_t.iter().filter(|&&b|\
        \ b).count() as i32\n    }\n}"
      racket: "(require racket/list)\n(require racket/set)\n\n(define/contract (unique-xor-triplets\
        \ nums)\n  (-> (listof exact-integer?) exact-integer?)\n  (let* ([u (remove-duplicates\
        \ nums)]\n         [in-p (make-vector 2048 #f)]\n         [in-t (make-vector\
        \ 2048 #f)])\n    (for ([y u])\n      (for ([z u])\n        (vector-set! in-p\
        \ (bitwise-xor y z) #t)))\n    (let ([p-bits '()])\n      (for ([p (in-range\
        \ 2048)])\n        (when (vector-ref in-p p)\n          (set! p-bits (cons p\
        \ p-bits))))\n      (for ([x u])\n        (for ([p p-bits])\n          (vector-set!\
        \ in-t (bitwise-xor x p) #t))))\n    (for/fold ([cnt 0])\n              ([i\
        \ (in-range 2048)])\n      (if (vector-ref in-t i)\n          (add1 cnt)\n \
        \         cnt))))"
      erlang: "-spec unique_xor_triplets(Nums :: [integer()]) -> integer().\nunique_xor_triplets(Nums)\
        \ ->\n  U = lists:usort(Nums),\n  InP = lists:foldl(fun(Y, AccP) ->\n    lists:foldl(fun(Z,\
        \ AccZ) ->\n      AccZ bor (1 bsl (Y bxor Z))\n    end, AccP, U)\n  end, 0,\
        \ U),\n  PBits = [P || P <- lists:seq(0, 2047), (InP band (1 bsl P)) /= 0],\n\
        \  InT = lists:foldl(fun(X, AccT) ->\n    lists:foldl(fun(P, AccInner) ->\n\
        \      AccInner bor (1 bsl (X bxor P))\n    end, AccT, PBits)\n  end, 0, U),\n\
        \  count_bits(InT, 0).\n\ncount_bits(0, Acc) -> Acc;\ncount_bits(N, Acc) ->\
        \ count_bits(N band (N - 1), Acc + 1)."
      elixir: "defmodule Solution do\n  @spec unique_xor_triplets(nums :: [integer])\
        \ :: integer\n  def unique_xor_triplets(nums) do\n    import Bitwise\n    u\
        \ = Enum.uniq(nums)\n    in_p = Enum.reduce(u, 0, fn y, acc_p ->\n      Enum.reduce(u,\
        \ acc_p, fn z, acc_z ->\n        acc_z ||| (1 <<< (y ^^^ z))\n      end)\n \
        \   end)\n    p_bits = Enum.filter(0..2047, fn p -> (in_p &&& (1 <<< p)) !=\
        \ 0 end)\n    in_t = Enum.reduce(u, 0, fn x, acc_t ->\n      Enum.reduce(p_bits,\
        \ acc_t, fn p, acc_inner ->\n        acc_inner ||| (1 <<< (x ^^^ p))\n     \
        \ end)\n    end)\n    count_bits(in_t, 0)\n  end\n\n  defp count_bits(0, acc),\
        \ do: acc\n  defp count_bits(n, acc), do: count_bits(n &&& (n - 1), acc + 1)\n\
        end"
    approach: 'The problem asks for the number of unique XOR results from triplets $(i,
      j, k)$ with $i \le j \le k$. Since $i, j, k$ are indices that can be equal, and
      the XOR operation is commutative and associative, the set of all unique triplet
      XOR values is equivalent to the set of all $x \oplus y \oplus z$ where $x, y,
      z$ are any values from the unique set of elements in the input array. This is
      because any combination of values can be formed by choosing their corresponding
      indices and repeating an index if a value is needed fewer than three times (e.g.,
      $x \oplus x \oplus y = y$ and $x \oplus x \oplus x = x$).


      To solve this efficiently, we first identify the set of unique values $S$ in the
      input. We then compute the set $Q$ of all unique XOR sums of two values from $S$.
      Finally, we compute the set of all unique XOR sums by XORing each value in $Q$
      with each value in $S$. Given that the maximum value in the input is 1500, the
      maximum possible XOR sum is 2047, which allows us to use boolean arrays of size
      2048 to track unique sums. This reduces the problem from an $O(n^3)$ search over
      indices to an efficient $O(|S|^2 + |Q||S|)$ approach.'
    time_complexity: O(N + |S|^2 + |Q| \cdot |S|), where $N$ is the number of elements
      in $nums$, $|S|$ is the number of unique values in $nums$ ($|S| \le 1500$), and
      $|Q|$ is the number of unique XOR pairs ($|Q| \le 2048$). The extraction of unique
      values takes $O(N)$, computing all pairs takes $O(|S|^2)$, and computing the final
      triplets takes $O(|Q| \cdot |S|)$, totaling approximately $5 \times 10^6$ operations.
    space_complexity: O(|S| + \text{MAX\_XOR}), where $\text{MAX\_XOR}$ is 2048. We
      store the unique values of $S$, the unique XOR pairs $Q$, and a boolean array
      for the final results, each bounded by 2048.
    elapsed_time: 332.6699011325836
    model: gemini-3-flash-preview
    generated_at: '2026-07-24 02:03:57 '
---

## Problem #3514: Number of Unique XOR Triplets II

**Difficulty:** Medium

**Topics:** Array, Math, Bit Manipulation, Enumeration

## Problem Description

<p data-end="261" data-start="147">You are given an integer array <code>nums</code>.</p>

<p>A <strong>XOR triplet</strong> is defined as the XOR of three elements <code>nums[i] XOR nums[j] XOR nums[k]</code> where <code>i &lt;= j &lt;= k</code>.</p>

<p>Return the number of <strong>unique</strong> XOR triplet values from all possible triplets <code>(i, j, k)</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p data-end="158" data-start="101">The possible XOR triplet values are:</p>

<ul data-end="280" data-start="159">
	<li data-end="188" data-start="159"><code>(0, 0, 0) &rarr; 1 XOR 1 XOR 1 = 1</code></li>
	<li data-end="218" data-start="189"><code>(0, 0, 1) &rarr; 1 XOR 1 XOR 3 = 3</code></li>
	<li data-end="248" data-start="219"><code>(0, 1, 1) &rarr; 1 XOR 3 XOR 3 = 1</code></li>
	<li data-end="280" data-start="249"><code>(1, 1, 1) &rarr; 3 XOR 3 XOR 3 = 3</code></li>
</ul>

<p data-end="343" data-start="282">The unique XOR values are <code data-end="316" data-start="308">{1, 3}</code>. Thus, the output is 2.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [6,7,8,9]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The possible XOR triplet values are <code data-end="275" data-start="267">{6, 7, 8, 9}</code>. Thus, the output is 4.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1500</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1500</code></li>
</ul>


## Hints

1. What is the maximum possible XOR value achievable by any triplet?

2. Let the maximum possible XOR value be stored in `max_xor`.

3. For each index `i`, consider all pairs of indices `(j, k)` such that `i <= j <= k`. For each such pair, compute the triplet XOR as `nums[i] XOR nums[j] XOR nums[k]`.

4. You can optimize the calculation by precomputing or reusing intermediate XOR results. For example, after fixing an index `i`, compute XORs of pairs `(j, k)` in `O(n^2)` time instead of checking all three indices independently.

5. Finally, count the number of unique XOR values obtained from all triplets.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the number of unique XOR results from triplets $(i, j, k)$ with $i \le j \le k$. Since $i, j, k$ are indices that can be equal, and the XOR operation is commutative and associative, the set of all unique triplet XOR values is equivalent to the set of all $x \oplus y \oplus z$ where $x, y, z$ are any values from the unique set of elements in the input array. This is because any combination of values can be formed by choosing their corresponding indices and repeating an index if a value is needed fewer than three times (e.g., $x \oplus x \oplus y = y$ and $x \oplus x \oplus x = x$).

To solve this efficiently, we first identify the set of unique values $S$ in the input. We then compute the set $Q$ of all unique XOR sums of two values from $S$. Finally, we compute the set of all unique XOR sums by XORing each value in $Q$ with each value in $S$. Given that the maximum value in the input is 1500, the maximum possible XOR sum is 2047, which allows us to use boolean arrays of size 2048 to track unique sums. This reduces the problem from an $O(n^3)$ search over indices to an efficient $O(|S|^2 + |Q||S|)$ approach.

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
    int uniqueXorTriplets(vector<int>& nums) {
        bool seen[2048] = {false};
        vector<int> S;
        for (int x : nums) {
            if (!seen[x]) {
                seen[x] = true;
                S.push_back(x);
            }
        }

        bool pair_exists[2048] = {false};
        for (int i = 0; i < S.size(); ++i) {
            for (int j = i; j < S.size(); ++j) {
                pair_exists[S[i] ^ S[j]] = true;
            }
        }

        vector<int> Q;
        for (int i = 0; i < 2048; ++i) {
            if (pair_exists[i]) Q.push_back(i);
        }

        bool triplets[2048] = {false};
        for (int q : Q) {
            for (int z : S) {
                triplets[q ^ z] = true;
            }
        }

        int count = 0;
        for (int i = 0; i < 2048; ++i) {
            if (triplets[i]) count++;
        }
        return count;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int uniqueXorTriplets(int[] nums) {
        boolean[] seen = new boolean[2048];
        int uniqueCount = 0;
        for (int x : nums) {
            if (!seen[x]) {
                seen[x] = true;
                uniqueCount++;
            }
        }

        int[] S = new int[uniqueCount];
        int idx = 0;
        for (int i = 0; i < 2048; i++) {
            if (seen[i]) S[idx++] = i;
        }

        boolean[] pairExists = new boolean[2048];
        for (int i = 0; i < S.length; i++) {
            for (int j = i; j < S.length; j++) {
                pairExists[S[i] ^ S[j]] = true;
            }
        }

        int pairCount = 0;
        for (int i = 0; i < 2048; i++) {
            if (pairExists[i]) pairCount++;
        }
        int[] Q = new int[pairCount];
        idx = 0;
        for (int i = 0; i < 2048; i++) {
            if (pairExists[i]) Q[idx++] = i;
        }

        boolean[] triplets = new boolean[2048];
        for (int q : Q) {
            for (int z : S) {
                triplets[q ^ z] = true;
            }
        }

        int totalCount = 0;
        for (int i = 0; i < 2048; i++) {
            if (triplets[i]) totalCount++;
        }
        return totalCount;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        S = list(set(nums))
        pairs = [False] * 2048
        for i in range(len(S)):
            for j in range(i, len(S)):
                pairs[S[i] ^ S[j]] = True

        Q = [q for q in range(2048) if pairs[q]]

        triplets = [False] * 2048
        for q in Q:
            for z in S:
                triplets[q ^ z] = True

        return sum(triplets)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        S = list(set(nums))
        pairs = [False] * 2048
        for i in range(len(S)):
            for j in range(i, len(S)):
                pairs[S[i] ^ S[j]] = True

        Q = [q for q in range(2048) if pairs[q]]

        triplets = [False] * 2048
        for q in Q:
            for z in S:
                triplets[q ^ z] = True

        return sum(triplets)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int uniqueXorTriplets(int* nums, int numsSize) {
    int seen[2048] = {0};
    int S[1501];
    int sSize = 0;
    for (int i = 0; i < numsSize; i++) {
        if (!seen[nums[i]]) {
            seen[nums[i]] = 1;
            S[sSize++] = nums[i];
        }
    }

    int pairExists[2048] = {0};
    for (int i = 0; i < sSize; i++) {
        for (int j = i; j < sSize; j++) {
            pairExists[S[i] ^ S[j]] = 1;
        }
    }

    int Q[2048];
    int qSize = 0;
    for (int i = 0; i < 2048; i++) {
        if (pairExists[i]) {
            Q[qSize++] = i;
        }
    }

    int triplets[2048] = {0};
    for (int i = 0; i < qSize; i++) {
        for (int j = 0; j < sSize; j++) {
            triplets[Q[i] ^ S[j]] = 1;
        }
    }

    int count = 0;
    for (int i = 0; i < 2048; i++) {
        if (triplets[i]) count++;
    }
    return count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int UniqueXorTriplets(int[] nums) {
        bool[] hasU = new bool[2048];
        foreach (int n in nums) {
            hasU[n] = true;
        }

        int[] U = new int[2048];
        int uCount = 0;
        for (int i = 0; i < 2048; i++) {
            if (hasU[i]) {
                U[uCount++] = i;
            }
        }

        bool[] hasP = new bool[2048];
        for (int i = 0; i < uCount; i++) {
            for (int j = i; j < uCount; j++) {
                hasP[U[i] ^ U[j]] = true;
            }
        }

        bool[] hasS = new bool[2048];
        int count = 0;
        for (int p = 0; p < 2048; p++) {
            if (hasP[p]) {
                for (int k = 0; k < uCount; k++) {
                    int val = p ^ U[k];
                    if (!hasS[val]) {
                        hasS[val] = true;
                        count++;
                    }
                }
            }
        }

        return count;
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
var uniqueXorTriplets = function(nums) {
    const hasU = new Uint8Array(2048);
    for (let i = 0; i < nums.length; i++) {
        hasU[nums[i]] = 1;
    }

    const U = [];
    for (let i = 0; i < 2048; i++) {
        if (hasU[i]) {
            U.push(i);
        }
    }

    const hasP = new Uint8Array(2048);
    const uLen = U.length;
    for (let i = 0; i < uLen; i++) {
        for (let j = i; j < uLen; j++) {
            hasP[U[i] ^ U[j]] = 1;
        }
    }

    const hasS = new Uint8Array(2048);
    let count = 0;
    for (let p = 0; p < 2048; p++) {
        if (hasP[p] === 1) {
            for (let k = 0; k < uLen; k++) {
                const val = p ^ U[k];
                if (hasS[val] === 0) {
                    hasS[val] = 1;
                    count++;
                }
            }
        }
    }

    return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function uniqueXorTriplets(nums: number[]): number {
    const hasU = new Uint8Array(2048);
    for (let i = 0; i < nums.length; i++) {
        hasU[nums[i]] = 1;
    }

    const U: number[] = [];
    for (let i = 0; i < 2048; i++) {
        if (hasU[i]) {
            U.push(i);
        }
    }

    const hasP = new Uint8Array(2048);
    const uLen = U.length;
    for (let i = 0; i < uLen; i++) {
        for (let j = i; j < uLen; j++) {
            hasP[U[i] ^ U[j]] = 1;
        }
    }

    const hasS = new Uint8Array(2048);
    let count = 0;
    for (let p = 0; p < 2048; p++) {
        if (hasP[p] === 1) {
            for (let k = 0; k < uLen; k++) {
                const val = p ^ U[k];
                if (hasS[val] === 0) {
                    hasS[val] = 1;
                    count++;
                }
            }
        }
    }

    return count;
}
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
    function uniqueXorTriplets($nums) {
        $hasU = array_fill(0, 2048, false);
        foreach ($nums as $n) {
            $hasU[$n] = true;
        }

        $U = [];
        for ($i = 0; $i < 2048; $i++) {
            if ($hasU[$i]) {
                $U[] = $i;
            }
        }

        $hasP = array_fill(0, 2048, false);
        $uCount = count($U);
        for ($i = 0; $i < $uCount; $i++) {
            for ($j = $i; $j < $uCount; $j++) {
                $hasP[$U[$i] ^ $U[$j]] = true;
            }
        }

        $hasS = array_fill(0, 2048, false);
        $count = 0;
        for ($p = 0; $p < 2048; $p++) {
            if ($hasP[$p]) {
                foreach ($U as $z) {
                    $val = $p ^ $z;
                    if (!$hasS[$val]) {
                        $hasS[$val] = true;
                        $count++;
                    }
                }
            }
        }

        return $count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func uniqueXorTriplets(_ nums: [Int]) -> Int {
        var hasU = [Bool](repeating: false, count: 2048)
        for n in nums {
            hasU[n] = true
        }

        var U = [Int]()
        for i in 0..<2048 {
            if hasU[i] {
                U.append(i)
            }
        }

        var hasP = [Bool](repeating: false, count: 2048)
        let uCount = U.count
        if uCount > 0 {
            for i in 0..<uCount {
                for j in i..<uCount {
                    hasP[U[i] ^ U[j]] = true
                }
            }
        }

        var hasS = [Bool](repeating: false, count: 2048)
        var count = 0
        for p in 0..<2048 {
            if hasP[p] {
                for z in U {
                    let val = p ^ z
                    if !hasS[val] {
                        hasS[val] = true
                        count += 1
                    }
                }
            }
        }

        return count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun uniqueXorTriplets(nums: IntArray): Int {
        val uniqueNums = nums.distinct().toIntArray()
        val n = uniqueNums.size
        val canXor2 = BooleanArray(2048)

        for (i in 0 until n) {
            for (j in i until n) {
                canXor2[uniqueNums[i] xor uniqueNums[j]] = true
            }
        }

        val canXor3 = BooleanArray(2048)
        for (v2 in 0 until 2048) {
            if (canXor2[v2]) {
                for (z in uniqueNums) {
                    canXor3[v2 xor z] = true
                }
            }
        }

        var count = 0
        for (i in 0 until 2048) {
            if (canXor3[i]) count++
        }
        return count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int uniqueXorTriplets(List<int> nums) {
    var uniqueSet = nums.toSet().toList();
    int n = uniqueSet.length;
    var canXor2 = List<bool>.filled(2048, false);

    for (int i = 0; i < n; i++) {
      for (int j = i; j < n; j++) {
        canXor2[uniqueSet[i] ^ uniqueSet[j]] = true;
      }
    }

    var canXor3 = List<bool>.filled(2048, false);
    for (int v2 = 0; v2 < 2048; v2++) {
      if (canXor2[v2]) {
        for (int z in uniqueSet) {
          canXor3[v2 ^ z] = true;
        }
      }
    }

    int count = 0;
    for (int i = 0; i < 2048; i++) {
      if (canXor3[i]) count++;
    }
    return count;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func uniqueXorTriplets(nums []int) int {
    uniqueMap := make(map[int]bool)
    for _, num := range nums {
        uniqueMap[num] = true
    }
    var uniqueNums []int
    for num := range uniqueMap {
        uniqueNums = append(uniqueNums, num)
    }

    canXor2 := [2048]bool{}
    for i := 0; i < len(uniqueNums); i++ {
        for j := i; j < len(uniqueNums); j++ {
            canXor2[uniqueNums[i]^uniqueNums[j]] = true
        }
    }

    canXor3 := [2048]bool{}
    for v2 := 0; v2 < 2048; v2++ {
        if canXor2[v2] {
            for _, z := range uniqueNums {
                canXor3[v2^z] = true
            }
        }
    }

    count := 0
    for i := 0; i < 2048; i++ {
        if canXor3[i] {
            count++
        }
    }
    return count
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def unique_xor_triplets(nums)
  unique_nums = nums.uniq
  n = unique_nums.length
  can_xor2 = Array.new(2048, false)

  i = 0
  while i < n
    j = i
    while j < n
      can_xor2[unique_nums[i] ^ unique_nums[j]] = true
      j += 1
    end
    i += 1
  end

  can_xor3 = Array.new(2048, false)
  (0...2048).each do |v2|
    if can_xor2[v2]
      unique_nums.each do |z|
        can_xor3[v2 ^ z] = true
      end
    end
  end

  can_xor3.count(true)
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def uniqueXorTriplets(nums: Array[Int]): Int = {
        val uniqueNums = nums.distinct
        val n = uniqueNums.length
        val canXor2 = new Array[Boolean](2048)

        var i = 0
        while (i < n) {
            var j = i
            while (j < n) {
                canXor2(uniqueNums(i) ^ uniqueNums(j)) = true
                j += 1
            }
            i += 1
        }

        val canXor3 = new Array[Boolean](2048)
        var v2 = 0
        while (v2 < 2048) {
            if (canXor2(v2)) {
                var k = 0
                while (k < n) {
                    canXor3(v2 ^ uniqueNums(k)) = true
                    k += 1
                }
            }
            v2 += 1
        }

        var count = 0
        var idx = 0
        while (idx < 2048) {
            if (canXor3(idx)) count += 1
            idx += 1
        }
        count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn unique_xor_triplets(nums: Vec<i32>) -> i32 {
        let mut u = nums;
        u.sort_unstable();
        u.dedup();

        let mut in_p = [false; 2048];
        for i in 0..u.len() {
            for j in i..u.len() {
                in_p[(u[i] ^ u[j]) as usize] = true;
            }
        }

        let mut p_bits = Vec::new();
        for i in 0..2048 {
            if in_p[i] {
                p_bits.push(i as i32);
            }
        }

        let mut in_t = [false; 2048];
        for &x in &u {
            for &p in &p_bits {
                in_t[(x ^ p) as usize] = true;
            }
        }

        in_t.iter().filter(|&&b| b).count() as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(require racket/list)
(require racket/set)

(define/contract (unique-xor-triplets nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([u (remove-duplicates nums)]
         [in-p (make-vector 2048 #f)]
         [in-t (make-vector 2048 #f)])
    (for ([y u])
      (for ([z u])
        (vector-set! in-p (bitwise-xor y z) #t)))
    (let ([p-bits '()])
      (for ([p (in-range 2048)])
        (when (vector-ref in-p p)
          (set! p-bits (cons p p-bits))))
      (for ([x u])
        (for ([p p-bits])
          (vector-set! in-t (bitwise-xor x p) #t))))
    (for/fold ([cnt 0])
              ([i (in-range 2048)])
      (if (vector-ref in-t i)
          (add1 cnt)
          cnt))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec unique_xor_triplets(Nums :: [integer()]) -> integer().
unique_xor_triplets(Nums) ->
  U = lists:usort(Nums),
  InP = lists:foldl(fun(Y, AccP) ->
    lists:foldl(fun(Z, AccZ) ->
      AccZ bor (1 bsl (Y bxor Z))
    end, AccP, U)
  end, 0, U),
  PBits = [P || P <- lists:seq(0, 2047), (InP band (1 bsl P)) /= 0],
  InT = lists:foldl(fun(X, AccT) ->
    lists:foldl(fun(P, AccInner) ->
      AccInner bor (1 bsl (X bxor P))
    end, AccT, PBits)
  end, 0, U),
  count_bits(InT, 0).

count_bits(0, Acc) -> Acc;
count_bits(N, Acc) -> count_bits(N band (N - 1), Acc + 1).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec unique_xor_triplets(nums :: [integer]) :: integer
  def unique_xor_triplets(nums) do
    import Bitwise
    u = Enum.uniq(nums)
    in_p = Enum.reduce(u, 0, fn y, acc_p ->
      Enum.reduce(u, acc_p, fn z, acc_z ->
        acc_z ||| (1 <<< (y ^^^ z))
      end)
    end)
    p_bits = Enum.filter(0..2047, fn p -> (in_p &&& (1 <<< p)) != 0 end)
    in_t = Enum.reduce(u, 0, fn x, acc_t ->
      Enum.reduce(p_bits, acc_t, fn p, acc_inner ->
        acc_inner ||| (1 <<< (x ^^^ p))
      end)
    end)
    count_bits(in_t, 0)
  end

  defp count_bits(0, acc), do: acc
  defp count_bits(n, acc), do: count_bits(n &&& (n - 1), acc + 1)
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N + |S|^2 + |Q| \cdot |S|), where $N$ is the number of elements in $nums$, $|S|$ is the number of unique values in $nums$ ($|S| \le 1500$), and $|Q|$ is the number of unique XOR pairs ($|Q| \le 2048$). The extraction of unique values takes $O(N)$, computing all pairs takes $O(|S|^2)$, and computing the final triplets takes $O(|Q| \cdot |S|)$, totaling approximately $5 \times 10^6$ operations.
- **Space Complexity:** O(|S| + \text{MAX\_XOR}), where $\text{MAX\_XOR}$ is 2048. We store the unique values of $S$, the unique XOR pairs $Q$, and a boolean array for the final results, each bounded by 2048.
