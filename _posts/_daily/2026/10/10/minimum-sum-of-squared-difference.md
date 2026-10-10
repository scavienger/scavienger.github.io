---
layout: post
title: "Minimum Sum of Squared Difference"
date: 2026-10-10 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Binary Search", "Greedy", "Sorting", "Heap (Priority Queue)"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-sum-of-squared-difference/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    long long minSumSquareDiff(vector<int>& nums1,\
        \ vector<int>& nums2, int k1, int k2) {\n        long long k = (long long)k1\
        \ + k2;\n        int n = nums1.size();\n        long long freq[100001] = {0};\n\
        \        int max_d = 0;\n        for (int i = 0; i < n; ++i) {\n           \
        \ int d = std::abs(nums1[i] - nums2[i]);\n            freq[d]++;\n         \
        \   if (d > max_d) max_d = d;\n        }\n\n        for (int i = max_d; i >\
        \ 0; --i) {\n            if (k <= 0) break;\n            long long take = std::min(k,\
        \ freq[i]);\n            freq[i] -= take;\n            freq[i - 1] += take;\n\
        \            k -= take;\n        }\n\n        long long result = 0;\n      \
        \  for (int i = 1; i <= max_d; ++i) {\n            if (freq[i] > 0) {\n    \
        \            result += (long long)freq[i] * i * i;\n            }\n        }\n\
        \        return result;\n    }\n};"
      java: "class Solution {\n    public long minSumSquareDiff(int[] nums1, int[] nums2,\
        \ int k1, int k2) {\n        long k = (long) k1 + k2;\n        int n = nums1.length;\n\
        \        long[] freq = new long[100001];\n        int maxD = 0;\n        for\
        \ (int i = 0; i < n; i++) {\n            int d = Math.abs(nums1[i] - nums2[i]);\n\
        \            freq[d]++;\n            if (d > maxD) maxD = d;\n        }\n\n\
        \        for (int i = maxD; i > 0; i--) {\n            if (k <= 0) break;\n\
        \            long take = Math.min(k, freq[i]);\n            freq[i] -= take;\n\
        \            freq[i - 1] += take;\n            k -= take;\n        }\n\n   \
        \     long result = 0;\n        for (int i = 1; i <= maxD; i++) {\n        \
        \    if (freq[i] > 0) {\n                result += freq[i] * (long) i * i;\n\
        \            }\n        }\n        return result;\n    }\n}"
      python: "class Solution(object):\n    def minSumSquareDiff(self, nums1, nums2,\
        \ k1, k2):\n        \"\"\"\n        :type nums1: List[int]\n        :type nums2:\
        \ List[int]\n        :type k1: int\n        :type k2: int\n        :rtype: int\n\
        \        \"\"\"\n        k = k1 + k2\n        freq = [0] * 100001\n        max_d\
        \ = 0\n        for i in range(len(nums1)):\n            diff = abs(nums1[i]\
        \ - nums2[i])\n            freq[diff] += 1\n            if diff > max_d: max_d\
        \ = diff\n\n        for i in range(max_d, 0, -1):\n            if k <= 0: break\n\
        \            take = min(k, freq[i])\n            freq[i] -= take\n         \
        \   freq[i-1] += take\n            k -= take\n\n        ans = 0\n        for\
        \ i in range(1, max_d + 1):\n            if freq[i] > 0:\n                ans\
        \ += freq[i] * (i ** 2)\n        return ans"
      python3: "class Solution:\n    def minSumSquareDiff(self, nums1: list[int], nums2:\
        \ list[int], k1: int, k2: int) -> int:\n        k = k1 + k2\n        freq =\
        \ [0] * 100001\n        max_d = 0\n        for n1, n2 in zip(nums1, nums2):\n\
        \            diff = abs(n1 - n2)\n            freq[diff] += 1\n            if\
        \ diff > max_d: max_d = diff\n\n        for i in range(max_d, 0, -1):\n    \
        \        if k <= 0:\n                break\n            take = min(k, freq[i])\n\
        \            freq[i] -= take\n            freq[i-1] += take\n            k -=\
        \ take\n\n        return sum(freq[i] * i * i for i in range(1, max_d + 1))"
      c: "#include <stdlib.h>\n#include <math.h>\n\nlong long minSumSquareDiff(int*\
        \ nums1, int nums1Size, int* nums2, int nums2Size, int k1, int k2) {\n    long\
        \ long k = (long long)k1 + k2;\n    long long freq[100001] = {0};\n    int max_d\
        \ = 0;\n\n    for (int i = 0; i < nums1Size; i++) {\n        int d = abs(nums1[i]\
        \ - nums2[i]);\n        freq[d]++;\n        if (d > max_d) max_d = d;\n    }\n\
        \n    for (int i = max_d; i > 0; i--) {\n        if (k <= 0) break;\n      \
        \  long long take = (k < freq[i]) ? k : freq[i];\n        freq[i] -= take;\n\
        \        freq[i-1] += take;\n        k -= take;\n    }\n\n    long long res\
        \ = 0;\n    for (int i = 1; i <= max_d; i++) {\n        if (freq[i] > 0) {\n\
        \            res += freq[i] * (long long)i * i;\n        }\n    }\n    return\
        \ res;\n}"
      csharp: "public class Solution {\n    public long MinSumSquareDiff(int[] nums1,\
        \ int[] nums2, int k1, int k2) {\n        int n = nums1.Length;\n        long\
        \ k = (long)k1 + k2;\n        int maxDiff = 0;\n        for (int i = 0; i <\
        \ n; i++) {\n            int d = Math.Abs(nums1[i] - nums2[i]);\n          \
        \  if (d > maxDiff) maxDiff = d;\n        }\n\n        if (maxDiff == 0) return\
        \ 0;\n\n        int[] counts = new int[maxDiff + 1];\n        for (int i = 0;\
        \ i < n; i++) {\n            counts[Math.Abs(nums1[i] - nums2[i])]++;\n    \
        \    }\n\n        for (int i = maxDiff; i > 0; i--) {\n            if (counts[i]\
        \ > 0) {\n                int take = (int)Math.Min((long)counts[i], k);\n  \
        \              counts[i] -= take;\n                counts[i - 1] += take;\n\
        \                k -= take;\n                if (k == 0) break;\n          \
        \  }\n        }\n\n        long result = 0;\n        for (int i = 1; i <= maxDiff;\
        \ i++) {\n            if (counts[i] > 0) {\n                result += (long)counts[i]\
        \ * (long)i * i;\n            }\n        }\n        return result;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums1\n * @param {number[]} nums2\n * @param\
        \ {number} k1\n * @param {number} k2\n * @return {number}\n */\nvar minSumSquareDiff\
        \ = function(nums1, nums2, k1, k2) {\n    const n = nums1.length;\n    let k\
        \ = k1 + k2;\n    let maxDiff = 0;\n    for (let i = 0; i < n; i++) {\n    \
        \    let d = Math.abs(nums1[i] - nums2[i]);\n        if (d > maxDiff) maxDiff\
        \ = d;\n    }\n\n    if (maxDiff === 0) return 0;\n\n    const counts = new\
        \ Int32Array(maxDiff + 1);\n    for (let i = 0; i < n; i++) {\n        counts[Math.abs(nums1[i]\
        \ - nums2[i])]++;\n    }\n\n    for (let i = maxDiff; i > 0; i--) {\n      \
        \  if (counts[i] > 0) {\n            let take = Math.min(k, counts[i]);\n  \
        \          counts[i] -= take;\n            counts[i - 1] += take;\n        \
        \    k -= take;\n            if (k === 0) break;\n        }\n    }\n\n    let\
        \ result = BigInt(0);\n    for (let i = 1; i <= maxDiff; i++) {\n        if\
        \ (counts[i] > 0) {\n            result += BigInt(counts[i]) * BigInt(i) * BigInt(i);\n\
        \        }\n    }\n    return Number(result);\n};"
      typescript: "function minSumSquareDiff(nums1: number[], nums2: number[], k1: number,\
        \ k2: number): number {\n    const n = nums1.length;\n    let k = k1 + k2;\n\
        \    let maxDiff = 0;\n    for (let i = 0; i < n; i++) {\n        const d =\
        \ Math.abs(nums1[i] - nums2[i]);\n        if (d > maxDiff) maxDiff = d;\n  \
        \  }\n\n    if (maxDiff === 0) return 0;\n\n    const counts = new Int32Array(maxDiff\
        \ + 1);\n    for (let i = 0; i < n; i++) {\n        counts[Math.abs(nums1[i]\
        \ - nums2[i])]++;\n    }\n\n    for (let i = maxDiff; i > 0; i--) {\n      \
        \  if (counts[i] > 0) {\n            const take = Math.min(k, counts[i]);\n\
        \            counts[i] -= take;\n            counts[i - 1] += take;\n      \
        \      k -= take;\n            if (k === 0) break;\n        }\n    }\n\n   \
        \ let result = BigInt(0);\n    for (let i = 1; i <= maxDiff; i++) {\n      \
        \  if (counts[i] > 0) {\n            result += BigInt(counts[i]) * BigInt(i)\
        \ * BigInt(i);\n        }\n    }\n    return Number(result);\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums1\n     * @param\
        \ Integer[] $nums2\n     * @param Integer $k1\n     * @param Integer $k2\n \
        \    * @return Integer\n     */\n    function minSumSquareDiff($nums1, $nums2,\
        \ $k1, $k2) {\n        $n = count($nums1);\n        $k = $k1 + $k2;\n      \
        \  $maxDiff = 0;\n        for ($i = 0; $i < $n; $i++) {\n            $d = abs($nums1[$i]\
        \ - $nums2[$i]);\n            if ($d > $maxDiff) $maxDiff = $d;\n        }\n\
        \n        if ($maxDiff == 0) return 0;\n\n        $counts = array_fill(0, $maxDiff\
        \ + 1, 0);\n        for ($i = 0; $i < $n; $i++) {\n            $counts[abs($nums1[$i]\
        \ - $nums2[$i])]++;\n        }\n\n        for ($i = $maxDiff; $i > 0; $i--)\
        \ {\n            if ($counts[$i] > 0) {\n                $take = min($k, $counts[$i]);\n\
        \                $counts[$i] -= $take;\n                $counts[$i - 1] += $take;\n\
        \                $k -= $take;\n                if ($k == 0) break;\n       \
        \     }\n        }\n\n        $result = 0;\n        for ($i = 1; $i <= $maxDiff;\
        \ $i++) {\n            if ($counts[$i] > 0) {\n                $result += $counts[$i]\
        \ * $i * $i;\n            }\n        }\n        return $result;\n    }\n}"
      swift: "class Solution {\n    func minSumSquareDiff(_ nums1: [Int], _ nums2: [Int],\
        \ _ k1: Int, _ k2: Int) -> Int {\n        let n = nums1.count\n        var k\
        \ = k1 + k2\n        var maxDiff = 0\n        for i in 0..<n {\n           \
        \ let d = abs(nums1[i] - nums2[i])\n            if d > maxDiff { maxDiff = d\
        \ }\n        }\n\n        if maxDiff == 0 { return 0 }\n\n        var counts\
        \ = [Int](repeating: 0, count: maxDiff + 1)\n        for i in 0..<n {\n    \
        \        counts[abs(nums1[i] - nums2[i])] += 1\n        }\n\n        for i in\
        \ stride(from: maxDiff, through: 1, by: -1) {\n            if counts[i] > 0\
        \ {\n                let take = min(k, counts[i])\n                counts[i]\
        \ -= take\n                counts[i - 1] += take\n                k -= take\n\
        \                if k == 0 { break }\n            }\n        }\n\n        var\
        \ result: Int64 = 0\n        for i in 1...maxDiff {\n            if counts[i]\
        \ > 0 {\n                result += Int64(counts[i]) * Int64(i) * Int64(i)\n\
        \            }\n        }\n        return Int(result)\n    }\n}"
      kotlin: "class Solution {\n    fun minSumSquareDiff(nums1: IntArray, nums2: IntArray,\
        \ k1: Int, k2: Int): Long {\n        val n = nums1.size\n        val diffs =\
        \ LongArray(100001)\n        var maxD = 0\n        for (i in 0 until n) {\n\
        \            val d = if (nums1[i] > nums2[i]) nums1[i] - nums2[i] else nums2[i]\
        \ - nums1[i]\n            if (d > 0) {\n                diffs[d]++\n       \
        \         if (d > maxD) maxD = d\n            }\n        }\n        var k =\
        \ k1.toLong() + k2.toLong()\n        for (v in maxD downTo 1) {\n          \
        \  if (k <= 0) break\n            if (diffs[v] > 0) {\n                val take\
        \ = if (k < diffs[v]) k else diffs[v]\n                diffs[v] -= take\n  \
        \              diffs[v - 1] += take\n                k -= take\n           \
        \ }\n        }\n        var ans = 0L\n        for (v in 1..maxD) {\n       \
        \     if (diffs[v] > 0) {\n                ans += diffs[v] * v.toLong() * v.toLong()\n\
        \            }\n        }\n        return ans\n    }\n}"
      dart: "class Solution {\n  int minSumSquareDiff(List<int> nums1, List<int> nums2,\
        \ int k1, int k2) {\n    int n = nums1.length;\n    List<int> diffs = List.filled(100001,\
        \ 0);\n    int maxD = 0;\n    for (int i = 0; i < n; i++) {\n      int d = (nums1[i]\
        \ - nums2[i]).abs();\n      if (d > 0) {\n        diffs[d]++;\n        if (d\
        \ > maxD) maxD = d;\n      }\n    }\n    int k = k1 + k2;\n    for (int v =\
        \ maxD; v >= 1; v--) {\n      if (k <= 0) break;\n      if (diffs[v] > 0) {\n\
        \        int take = k < diffs[v] ? k : diffs[v];\n        diffs[v] -= take;\n\
        \        diffs[v - 1] += take;\n        k -= take;\n      }\n    }\n    int\
        \ ans = 0;\n    for (int v = 1; v <= maxD; v++) {\n      if (diffs[v] > 0) {\n\
        \        ans += diffs[v] * v * v;\n      }\n    }\n    return ans;\n  }\n}"
      go: "func minSumSquareDiff(nums1 []int, nums2 []int, k1 int, k2 int) int64 {\n\
        \    n := len(nums1)\n    diffs := make([]int64, 100001)\n    maxDiff := 0\n\
        \    for i := 0; i < n; i++ {\n        d := nums1[i] - nums2[i]\n        if\
        \ d < 0 {\n            d = -d\n        }\n        if d > 0 {\n            diffs[d]++\n\
        \            if d > maxDiff {\n                maxDiff = d\n            }\n\
        \        }\n    }\n    k := int64(k1) + int64(k2)\n    for v := maxDiff; v >=\
        \ 1; v-- {\n        if k <= 0 {\n            break\n        }\n        if diffs[v]\
        \ > 0 {\n            take := diffs[v]\n            if k < take {\n         \
        \       take = k\n            }\n            diffs[v] -= take\n            diffs[v-1]\
        \ += take\n            k -= take\n        }\n    }\n    var ans int64 = 0\n\
        \    for v := 1; v <= maxDiff; v++ {\n        if diffs[v] > 0 {\n          \
        \  ans += diffs[v] * int64(v) * int64(v)\n        }\n    }\n    return ans\n\
        }"
      ruby: "# @param {Integer[]} nums1\n# @param {Integer[]} nums2\n# @param {Integer}\
        \ k1\n# @param {Integer} k2\n# @return {Integer}\ndef min_sum_square_diff(nums1,\
        \ nums2, k1, k2)\n  n = nums1.length\n  diffs = Array.new(100001, 0)\n  max_d\
        \ = 0\n  n.times do |i|\n    d = (nums1[i] - nums2[i]).abs\n    if d > 0\n \
        \     diffs[d] += 1\n      max_d = d if d > max_d\n    end\n  end\n  k = k1\
        \ + k2\n  max_d.downto(1) do |v|\n    break if k <= 0\n    if diffs[v] > 0\n\
        \      take = k < diffs[v] ? k : diffs[v]\n      diffs[v] -= take\n      diffs[v\
        \ - 1] += take\n      k -= take\n    end\n  end\n  ans = 0\n  (1..max_d).each\
        \ do |v|\n    ans += diffs[v] * v * v if diffs[v] > 0\n  end\n  ans\nend"
      scala: "object Solution {\n    def minSumSquareDiff(nums1: Array[Int], nums2:\
        \ Array[Int], k1: Int, k2: Int): Long = {\n        val n = nums1.length\n  \
        \      val diffs = new Array[Long](100001)\n        var maxD = 0\n        for\
        \ (i <- 0 until n) {\n            val d = Math.abs(nums1(i) - nums2(i))\n  \
        \          if (d > 0) {\n                diffs(d) += 1\n                if (d\
        \ > maxD) maxD = d\n            }\n        }\n        var k = k1.toLong + k2.toLong\n\
        \        var v = maxD\n        while (v >= 1 && k > 0) {\n            if (diffs(v)\
        \ > 0) {\n                val take = Math.min(k, diffs(v))\n               \
        \ diffs(v) -= take\n                diffs(v - 1) += take\n                k\
        \ -= take\n            }\n            v -= 1\n        }\n        var ans: Long\
        \ = 0\n        for (v <- 1 to maxD) {\n            if (diffs(v) > 0) {\n   \
        \             ans += diffs(v) * v.toLong * v.toLong\n            }\n       \
        \ }\n        ans\n    }\n}"
      rust: "impl Solution {\n    pub fn min_sum_square_diff(nums1: Vec<i32>, nums2:\
        \ Vec<i32>, k1: i32, k2: i32) -> i64 {\n        let mut freq = vec![0i64; 100001];\n\
        \        for i in 0..nums1.len() {\n            let d = (nums1[i] - nums2[i]).abs()\
        \ as usize;\n            if d > 0 {\n                freq[d] += 1;\n       \
        \     }\n        }\n\n        let mut k = k1 as i64 + k2 as i64;\n        for\
        \ v in (1..=100000).rev() {\n            if freq[v] > 0 {\n                let\
        \ take = if k < freq[v] { k } else { freq[v] };\n                freq[v] -=\
        \ take;\n                freq[v - 1] += take;\n                k -= take;\n\
        \            }\n            if k == 0 {\n                break;\n          \
        \  }\n        }\n\n        let mut sum_sq: i64 = 0;\n        for v in 1..=100000\
        \ {\n            if freq[v] > 0 {\n                let v_i64 = v as i64;\n \
        \               sum_sq += v_i64 * v_i64 * freq[v];\n            }\n        }\n\
        \        sum_sq\n    }\n}"
      racket: "(define/contract (min-sum-square-diff nums1 nums2 k1 k2)\n  (-> (listof\
        \ exact-integer?) (listof exact-integer?) exact-integer? exact-integer? exact-integer?)\n\
        \  (let ([freq (make-vector 100001 0)]\n        [total-k (+ k1 k2)])\n    (for\
        \ ([n1 nums1] [n2 nums2])\n      (let ([d (abs (- n1 n2))])\n        (when (>\
        \ d 0)\n          (vector-set! freq d (+ (vector-ref freq d) 1)))))\n    (let\
        \ loop ([v 100000] [k total-k])\n      (when (and (> v 0) (> k 0))\n       \
        \ (let* ([count (vector-ref freq v)]\n               [take (min k count)])\n\
        \          (vector-set! freq v (- count take))\n          (vector-set! freq\
        \ (- v 1) (+ (vector-ref freq (- v 1)) take))\n          (loop (- v 1) (- k\
        \ take)))))\n    (for/fold ([sum-sq 0])\n              ([v (in-range 1 100001)])\n\
        \      (+ sum-sq (* v v (vector-ref freq v))))))"
      erlang: "-spec min_sum_square_diff(Nums1 :: [integer()], Nums2 :: [integer()],\
        \ K1 :: integer(), K2 :: integer()) -> integer().\nmin_sum_square_diff(Nums1,\
        \ Nums2, K1, K2) ->\n    FreqMap = build_freq(Nums1, Nums2, #{}),\n    TotalK\
        \ = K1 + K2,\n    Keys = maps:keys(FreqMap),\n    case Keys of\n        [] ->\
        \ 0;\n        _ ->\n            MaxD = lists:max(Keys),\n            FinalFreq\
        \ = perform_reduction(MaxD, TotalK, FreqMap),\n            maps:fold(fun(V,\
        \ Count, Acc) -> Acc + V * V * Count end, 0, FinalFreq)\n    end.\n\nbuild_freq([],\
        \ [], Map) -> Map;\nbuild_freq([H1|T1], [H2|T2], Map) ->\n    D = abs(H1 - H2),\n\
        \    if D > 0 ->\n        Count = maps:get(D, Map, 0),\n        build_freq(T1,\
        \ T2, maps:put(D, Count + 1, Map));\n       true ->\n        build_freq(T1,\
        \ T2, Map)\n    end.\n\nperform_reduction(0, _K, FreqMap) -> FreqMap;\nperform_reduction(_V,\
        \ 0, FreqMap) -> FreqMap;\nperform_reduction(V, K, FreqMap) ->\n    case maps:get(V,\
        \ FreqMap, 0) of\n        0 -> perform_reduction(V - 1, K, FreqMap);\n     \
        \   Count ->\n            Take = if K < Count -> K; true -> Count end,\n   \
        \         NewFreq = maps:put(V, Count - Take, FreqMap),\n            NewFreq2\
        \ = if V > 1 -> maps:put(V-1, maps:get(V-1, NewFreq, 0) + Take, NewFreq);\n\
        \                          true -> NewFreq\n                       end,\n  \
        \          perform_reduction(V - 1, K - Take, NewFreq2)\n    end."
      elixir: "defmodule Solution do\n  @spec min_sum_square_diff(nums1 :: [integer],\
        \ nums2 :: [integer], k1 :: integer, k2 :: integer) :: integer\n  def min_sum_square_diff(nums1,\
        \ nums2, k1, k2) do\n    freqs = Enum.zip(nums1, nums2)\n    |> Enum.reduce(%{},\
        \ fn {n1, n2}, acc ->\n      d = abs(n1 - n2)\n      if d > 0 do\n        Map.update(acc,\
        \ d, 1, &(&1 + 1))\n      else\n        acc\n      end\n    end)\n\n    total_k\
        \ = k1 + k2\n    keys = Map.keys(freqs)\n\n    if keys == [] do\n      0\n \
        \   else\n      max_d = Enum.max(keys)\n      {final_freqs, _} = Enum.reduce(max_d..1,\
        \ {freqs, total_k}, fn\n        _v, {acc_freqs, 0} -> {acc_freqs, 0}\n     \
        \   v, {acc_freqs, k} ->\n          count = Map.get(acc_freqs, v, 0)\n     \
        \     take = min(k, count)\n          new_acc = Map.put(acc_freqs, v, count\
        \ - take)\n          new_acc = if v > 1 do\n            Map.update(new_acc,\
        \ v - 1, take, &(&1 + take))\n          else\n            new_acc\n        \
        \  end\n          {new_acc, k - take}\n      end)\n\n      Enum.reduce(final_freqs,\
        \ 0, fn {v, count}, sum ->\n        sum + v * v * count\n      end)\n    end\n\
        \  end\nend"
    approach: 'To minimize the sum of squared differences, we combine the two modification
      budgets k1 and k2 into a single total budget k, as modifying an element in either
      array by 1 has the same impact on their absolute difference. We calculate the
      absolute differences d_i = |nums1[i] - nums2[i]| for all indices. The key intuition
      is that reducing larger differences yields a greater reduction in the total sum
      of squares because the square function $x^2$ grows more rapidly as $x$ increases
      ($x^2 - (x-1)^2 = 2x-1$). Therefore, we greedily prioritize reducing the largest
      differences first until our total budget k is exhausted.


      To implement this efficiently, we use a frequency array (bucket sort) to count
      the occurrences of each difference value up to the maximum possible difference
      ($10^5$). We iterate through this array from the highest possible difference down
      to 1. For each difference level i, we shift as many elements as possible to the
      level i-1 based on the remaining budget k. Once the budget is depleted or all
      differences have been processed, we calculate the final sum of squared differences
      using the updated counts in the frequency array. This approach is optimal and
      efficient, running in linear time relative to the input size and the range of
      difference values.'
    time_complexity: O(n + M) where n is the length of the input arrays and M is the
      maximum possible difference (100,000). We iterate through the arrays once to calculate
      differences and then perform a single pass through the frequency buckets.
    space_complexity: O(M) where M is the maximum possible difference (100,000). We
      use a frequency array of size M + 1 to store the count of each difference value.
    elapsed_time: 346.94964933395386
    model: gemini-3-flash-preview
    generated_at: '2026-10-10 03:45:15 '
---

## Problem #2333: Minimum Sum of Squared Difference

**Difficulty:** Medium

**Topics:** Array, Binary Search, Greedy, Sorting, Heap (Priority Queue)

## Problem Description

<p>You are given two positive <strong>0-indexed</strong> integer arrays <code>nums1</code> and <code>nums2</code>, both of length <code>n</code>.</p>

<p>The <strong>sum of squared difference</strong> of arrays <code>nums1</code> and <code>nums2</code> is defined as the <strong>sum</strong> of <code>(nums1[i] - nums2[i])<sup>2</sup></code> for each <code>0 &lt;= i &lt; n</code>.</p>

<p>You are also given two positive integers <code>k1</code> and <code>k2</code>. You can modify any of the elements of <code>nums1</code> by <code>+1</code> or <code>-1</code> at most <code>k1</code> times. Similarly, you can modify any of the elements of <code>nums2</code> by <code>+1</code> or <code>-1</code> at most <code>k2</code> times.</p>

<p>Return <em>the minimum <strong>sum of squared difference</strong> after modifying array </em><code>nums1</code><em> at most </em><code>k1</code><em> times and modifying array </em><code>nums2</code><em> at most </em><code>k2</code><em> times</em>.</p>

<p><strong>Note</strong>: You are allowed to modify the array elements to become <strong>negative</strong> integers.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0
<strong>Output:</strong> 579
<strong>Explanation:</strong> The elements in nums1 and nums2 cannot be modified because k1 = 0 and k2 = 0. 
The sum of square difference will be: (1 - 2)<sup>2 </sup>+ (2 - 10)<sup>2 </sup>+ (3 - 20)<sup>2 </sup>+ (4 - 19)<sup>2</sup>&nbsp;= 579.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1
<strong>Output:</strong> 43
<strong>Explanation:</strong> One way to obtain the minimum sum of square difference is: 
- Increase nums1[0] once.
- Increase nums2[2] once.
The minimum of the sum of square difference will be: 
(2 - 5)<sup>2 </sup>+ (4 - 8)<sup>2 </sup>+ (10 - 7)<sup>2 </sup>+ (12 - 9)<sup>2</sup>&nbsp;= 43.
Note that, there are other ways to obtain the minimum of the sum of square difference, but there is no way to obtain a sum smaller than 43.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums1.length == nums2.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= k1, k2 &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. There is no difference between the purpose of k1 and k2. Adding +1 to one element in nums1 is same as performing -1 to one element in nums2, and vice versa.

2. Reduce the sum of squared difference greedily. One operation of k should use the index that has the current maximum difference.

3. Binary search the maximum difference for the final result.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To minimize the sum of squared differences, we combine the two modification budgets k1 and k2 into a single total budget k, as modifying an element in either array by 1 has the same impact on their absolute difference. We calculate the absolute differences d_i = |nums1[i] - nums2[i]| for all indices. The key intuition is that reducing larger differences yields a greater reduction in the total sum of squares because the square function $x^2$ grows more rapidly as $x$ increases ($x^2 - (x-1)^2 = 2x-1$). Therefore, we greedily prioritize reducing the largest differences first until our total budget k is exhausted.

To implement this efficiently, we use a frequency array (bucket sort) to count the occurrences of each difference value up to the maximum possible difference ($10^5$). We iterate through this array from the highest possible difference down to 1. For each difference level i, we shift as many elements as possible to the level i-1 based on the remaining budget k. Once the budget is depleted or all differences have been processed, we calculate the final sum of squared differences using the updated counts in the frequency array. This approach is optimal and efficient, running in linear time relative to the input size and the range of difference values.

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
    long long minSumSquareDiff(vector<int>& nums1, vector<int>& nums2, int k1, int k2) {
        long long k = (long long)k1 + k2;
        int n = nums1.size();
        long long freq[100001] = {0};
        int max_d = 0;
        for (int i = 0; i < n; ++i) {
            int d = std::abs(nums1[i] - nums2[i]);
            freq[d]++;
            if (d > max_d) max_d = d;
        }

        for (int i = max_d; i > 0; --i) {
            if (k <= 0) break;
            long long take = std::min(k, freq[i]);
            freq[i] -= take;
            freq[i - 1] += take;
            k -= take;
        }

        long long result = 0;
        for (int i = 1; i <= max_d; ++i) {
            if (freq[i] > 0) {
                result += (long long)freq[i] * i * i;
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
    public long minSumSquareDiff(int[] nums1, int[] nums2, int k1, int k2) {
        long k = (long) k1 + k2;
        int n = nums1.length;
        long[] freq = new long[100001];
        int maxD = 0;
        for (int i = 0; i < n; i++) {
            int d = Math.abs(nums1[i] - nums2[i]);
            freq[d]++;
            if (d > maxD) maxD = d;
        }

        for (int i = maxD; i > 0; i--) {
            if (k <= 0) break;
            long take = Math.min(k, freq[i]);
            freq[i] -= take;
            freq[i - 1] += take;
            k -= take;
        }

        long result = 0;
        for (int i = 1; i <= maxD; i++) {
            if (freq[i] > 0) {
                result += freq[i] * (long) i * i;
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
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """
        k = k1 + k2
        freq = [0] * 100001
        max_d = 0
        for i in range(len(nums1)):
            diff = abs(nums1[i] - nums2[i])
            freq[diff] += 1
            if diff > max_d: max_d = diff

        for i in range(max_d, 0, -1):
            if k <= 0: break
            take = min(k, freq[i])
            freq[i] -= take
            freq[i-1] += take
            k -= take

        ans = 0
        for i in range(1, max_d + 1):
            if freq[i] > 0:
                ans += freq[i] * (i ** 2)
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        freq = [0] * 100001
        max_d = 0
        for n1, n2 in zip(nums1, nums2):
            diff = abs(n1 - n2)
            freq[diff] += 1
            if diff > max_d: max_d = diff

        for i in range(max_d, 0, -1):
            if k <= 0:
                break
            take = min(k, freq[i])
            freq[i] -= take
            freq[i-1] += take
            k -= take

        return sum(freq[i] * i * i for i in range(1, max_d + 1))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <math.h>

long long minSumSquareDiff(int* nums1, int nums1Size, int* nums2, int nums2Size, int k1, int k2) {
    long long k = (long long)k1 + k2;
    long long freq[100001] = {0};
    int max_d = 0;

    for (int i = 0; i < nums1Size; i++) {
        int d = abs(nums1[i] - nums2[i]);
        freq[d]++;
        if (d > max_d) max_d = d;
    }

    for (int i = max_d; i > 0; i--) {
        if (k <= 0) break;
        long long take = (k < freq[i]) ? k : freq[i];
        freq[i] -= take;
        freq[i-1] += take;
        k -= take;
    }

    long long res = 0;
    for (int i = 1; i <= max_d; i++) {
        if (freq[i] > 0) {
            res += freq[i] * (long long)i * i;
        }
    }
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public long MinSumSquareDiff(int[] nums1, int[] nums2, int k1, int k2) {
        int n = nums1.Length;
        long k = (long)k1 + k2;
        int maxDiff = 0;
        for (int i = 0; i < n; i++) {
            int d = Math.Abs(nums1[i] - nums2[i]);
            if (d > maxDiff) maxDiff = d;
        }

        if (maxDiff == 0) return 0;

        int[] counts = new int[maxDiff + 1];
        for (int i = 0; i < n; i++) {
            counts[Math.Abs(nums1[i] - nums2[i])]++;
        }

        for (int i = maxDiff; i > 0; i--) {
            if (counts[i] > 0) {
                int take = (int)Math.Min((long)counts[i], k);
                counts[i] -= take;
                counts[i - 1] += take;
                k -= take;
                if (k == 0) break;
            }
        }

        long result = 0;
        for (int i = 1; i <= maxDiff; i++) {
            if (counts[i] > 0) {
                result += (long)counts[i] * (long)i * i;
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
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k1
 * @param {number} k2
 * @return {number}
 */
var minSumSquareDiff = function(nums1, nums2, k1, k2) {
    const n = nums1.length;
    let k = k1 + k2;
    let maxDiff = 0;
    for (let i = 0; i < n; i++) {
        let d = Math.abs(nums1[i] - nums2[i]);
        if (d > maxDiff) maxDiff = d;
    }

    if (maxDiff === 0) return 0;

    const counts = new Int32Array(maxDiff + 1);
    for (let i = 0; i < n; i++) {
        counts[Math.abs(nums1[i] - nums2[i])]++;
    }

    for (let i = maxDiff; i > 0; i--) {
        if (counts[i] > 0) {
            let take = Math.min(k, counts[i]);
            counts[i] -= take;
            counts[i - 1] += take;
            k -= take;
            if (k === 0) break;
        }
    }

    let result = BigInt(0);
    for (let i = 1; i <= maxDiff; i++) {
        if (counts[i] > 0) {
            result += BigInt(counts[i]) * BigInt(i) * BigInt(i);
        }
    }
    return Number(result);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minSumSquareDiff(nums1: number[], nums2: number[], k1: number, k2: number): number {
    const n = nums1.length;
    let k = k1 + k2;
    let maxDiff = 0;
    for (let i = 0; i < n; i++) {
        const d = Math.abs(nums1[i] - nums2[i]);
        if (d > maxDiff) maxDiff = d;
    }

    if (maxDiff === 0) return 0;

    const counts = new Int32Array(maxDiff + 1);
    for (let i = 0; i < n; i++) {
        counts[Math.abs(nums1[i] - nums2[i])]++;
    }

    for (let i = maxDiff; i > 0; i--) {
        if (counts[i] > 0) {
            const take = Math.min(k, counts[i]);
            counts[i] -= take;
            counts[i - 1] += take;
            k -= take;
            if (k === 0) break;
        }
    }

    let result = BigInt(0);
    for (let i = 1; i <= maxDiff; i++) {
        if (counts[i] > 0) {
            result += BigInt(counts[i]) * BigInt(i) * BigInt(i);
        }
    }
    return Number(result);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @param Integer $k1
     * @param Integer $k2
     * @return Integer
     */
    function minSumSquareDiff($nums1, $nums2, $k1, $k2) {
        $n = count($nums1);
        $k = $k1 + $k2;
        $maxDiff = 0;
        for ($i = 0; $i < $n; $i++) {
            $d = abs($nums1[$i] - $nums2[$i]);
            if ($d > $maxDiff) $maxDiff = $d;
        }

        if ($maxDiff == 0) return 0;

        $counts = array_fill(0, $maxDiff + 1, 0);
        for ($i = 0; $i < $n; $i++) {
            $counts[abs($nums1[$i] - $nums2[$i])]++;
        }

        for ($i = $maxDiff; $i > 0; $i--) {
            if ($counts[$i] > 0) {
                $take = min($k, $counts[$i]);
                $counts[$i] -= $take;
                $counts[$i - 1] += $take;
                $k -= $take;
                if ($k == 0) break;
            }
        }

        $result = 0;
        for ($i = 1; $i <= $maxDiff; $i++) {
            if ($counts[$i] > 0) {
                $result += $counts[$i] * $i * $i;
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
    func minSumSquareDiff(_ nums1: [Int], _ nums2: [Int], _ k1: Int, _ k2: Int) -> Int {
        let n = nums1.count
        var k = k1 + k2
        var maxDiff = 0
        for i in 0..<n {
            let d = abs(nums1[i] - nums2[i])
            if d > maxDiff { maxDiff = d }
        }

        if maxDiff == 0 { return 0 }

        var counts = [Int](repeating: 0, count: maxDiff + 1)
        for i in 0..<n {
            counts[abs(nums1[i] - nums2[i])] += 1
        }

        for i in stride(from: maxDiff, through: 1, by: -1) {
            if counts[i] > 0 {
                let take = min(k, counts[i])
                counts[i] -= take
                counts[i - 1] += take
                k -= take
                if k == 0 { break }
            }
        }

        var result: Int64 = 0
        for i in 1...maxDiff {
            if counts[i] > 0 {
                result += Int64(counts[i]) * Int64(i) * Int64(i)
            }
        }
        return Int(result)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minSumSquareDiff(nums1: IntArray, nums2: IntArray, k1: Int, k2: Int): Long {
        val n = nums1.size
        val diffs = LongArray(100001)
        var maxD = 0
        for (i in 0 until n) {
            val d = if (nums1[i] > nums2[i]) nums1[i] - nums2[i] else nums2[i] - nums1[i]
            if (d > 0) {
                diffs[d]++
                if (d > maxD) maxD = d
            }
        }
        var k = k1.toLong() + k2.toLong()
        for (v in maxD downTo 1) {
            if (k <= 0) break
            if (diffs[v] > 0) {
                val take = if (k < diffs[v]) k else diffs[v]
                diffs[v] -= take
                diffs[v - 1] += take
                k -= take
            }
        }
        var ans = 0L
        for (v in 1..maxD) {
            if (diffs[v] > 0) {
                ans += diffs[v] * v.toLong() * v.toLong()
            }
        }
        return ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minSumSquareDiff(List<int> nums1, List<int> nums2, int k1, int k2) {
    int n = nums1.length;
    List<int> diffs = List.filled(100001, 0);
    int maxD = 0;
    for (int i = 0; i < n; i++) {
      int d = (nums1[i] - nums2[i]).abs();
      if (d > 0) {
        diffs[d]++;
        if (d > maxD) maxD = d;
      }
    }
    int k = k1 + k2;
    for (int v = maxD; v >= 1; v--) {
      if (k <= 0) break;
      if (diffs[v] > 0) {
        int take = k < diffs[v] ? k : diffs[v];
        diffs[v] -= take;
        diffs[v - 1] += take;
        k -= take;
      }
    }
    int ans = 0;
    for (int v = 1; v <= maxD; v++) {
      if (diffs[v] > 0) {
        ans += diffs[v] * v * v;
      }
    }
    return ans;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minSumSquareDiff(nums1 []int, nums2 []int, k1 int, k2 int) int64 {
    n := len(nums1)
    diffs := make([]int64, 100001)
    maxDiff := 0
    for i := 0; i < n; i++ {
        d := nums1[i] - nums2[i]
        if d < 0 {
            d = -d
        }
        if d > 0 {
            diffs[d]++
            if d > maxDiff {
                maxDiff = d
            }
        }
    }
    k := int64(k1) + int64(k2)
    for v := maxDiff; v >= 1; v-- {
        if k <= 0 {
            break
        }
        if diffs[v] > 0 {
            take := diffs[v]
            if k < take {
                take = k
            }
            diffs[v] -= take
            diffs[v-1] += take
            k -= take
        }
    }
    var ans int64 = 0
    for v := 1; v <= maxDiff; v++ {
        if diffs[v] > 0 {
            ans += diffs[v] * int64(v) * int64(v)
        }
    }
    return ans
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} k1
# @param {Integer} k2
# @return {Integer}
def min_sum_square_diff(nums1, nums2, k1, k2)
  n = nums1.length
  diffs = Array.new(100001, 0)
  max_d = 0
  n.times do |i|
    d = (nums1[i] - nums2[i]).abs
    if d > 0
      diffs[d] += 1
      max_d = d if d > max_d
    end
  end
  k = k1 + k2
  max_d.downto(1) do |v|
    break if k <= 0
    if diffs[v] > 0
      take = k < diffs[v] ? k : diffs[v]
      diffs[v] -= take
      diffs[v - 1] += take
      k -= take
    end
  end
  ans = 0
  (1..max_d).each do |v|
    ans += diffs[v] * v * v if diffs[v] > 0
  end
  ans
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minSumSquareDiff(nums1: Array[Int], nums2: Array[Int], k1: Int, k2: Int): Long = {
        val n = nums1.length
        val diffs = new Array[Long](100001)
        var maxD = 0
        for (i <- 0 until n) {
            val d = Math.abs(nums1(i) - nums2(i))
            if (d > 0) {
                diffs(d) += 1
                if (d > maxD) maxD = d
            }
        }
        var k = k1.toLong + k2.toLong
        var v = maxD
        while (v >= 1 && k > 0) {
            if (diffs(v) > 0) {
                val take = Math.min(k, diffs(v))
                diffs(v) -= take
                diffs(v - 1) += take
                k -= take
            }
            v -= 1
        }
        var ans: Long = 0
        for (v <- 1 to maxD) {
            if (diffs(v) > 0) {
                ans += diffs(v) * v.toLong * v.toLong
            }
        }
        ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_sum_square_diff(nums1: Vec<i32>, nums2: Vec<i32>, k1: i32, k2: i32) -> i64 {
        let mut freq = vec![0i64; 100001];
        for i in 0..nums1.len() {
            let d = (nums1[i] - nums2[i]).abs() as usize;
            if d > 0 {
                freq[d] += 1;
            }
        }

        let mut k = k1 as i64 + k2 as i64;
        for v in (1..=100000).rev() {
            if freq[v] > 0 {
                let take = if k < freq[v] { k } else { freq[v] };
                freq[v] -= take;
                freq[v - 1] += take;
                k -= take;
            }
            if k == 0 {
                break;
            }
        }

        let mut sum_sq: i64 = 0;
        for v in 1..=100000 {
            if freq[v] > 0 {
                let v_i64 = v as i64;
                sum_sq += v_i64 * v_i64 * freq[v];
            }
        }
        sum_sq
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-sum-square-diff nums1 nums2 k1 k2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let ([freq (make-vector 100001 0)]
        [total-k (+ k1 k2)])
    (for ([n1 nums1] [n2 nums2])
      (let ([d (abs (- n1 n2))])
        (when (> d 0)
          (vector-set! freq d (+ (vector-ref freq d) 1)))))
    (let loop ([v 100000] [k total-k])
      (when (and (> v 0) (> k 0))
        (let* ([count (vector-ref freq v)]
               [take (min k count)])
          (vector-set! freq v (- count take))
          (vector-set! freq (- v 1) (+ (vector-ref freq (- v 1)) take))
          (loop (- v 1) (- k take)))))
    (for/fold ([sum-sq 0])
              ([v (in-range 1 100001)])
      (+ sum-sq (* v v (vector-ref freq v))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_sum_square_diff(Nums1 :: [integer()], Nums2 :: [integer()], K1 :: integer(), K2 :: integer()) -> integer().
min_sum_square_diff(Nums1, Nums2, K1, K2) ->
    FreqMap = build_freq(Nums1, Nums2, #{}),
    TotalK = K1 + K2,
    Keys = maps:keys(FreqMap),
    case Keys of
        [] -> 0;
        _ ->
            MaxD = lists:max(Keys),
            FinalFreq = perform_reduction(MaxD, TotalK, FreqMap),
            maps:fold(fun(V, Count, Acc) -> Acc + V * V * Count end, 0, FinalFreq)
    end.

build_freq([], [], Map) -> Map;
build_freq([H1|T1], [H2|T2], Map) ->
    D = abs(H1 - H2),
    if D > 0 ->
        Count = maps:get(D, Map, 0),
        build_freq(T1, T2, maps:put(D, Count + 1, Map));
       true ->
        build_freq(T1, T2, Map)
    end.

perform_reduction(0, _K, FreqMap) -> FreqMap;
perform_reduction(_V, 0, FreqMap) -> FreqMap;
perform_reduction(V, K, FreqMap) ->
    case maps:get(V, FreqMap, 0) of
        0 -> perform_reduction(V - 1, K, FreqMap);
        Count ->
            Take = if K < Count -> K; true -> Count end,
            NewFreq = maps:put(V, Count - Take, FreqMap),
            NewFreq2 = if V > 1 -> maps:put(V-1, maps:get(V-1, NewFreq, 0) + Take, NewFreq);
                          true -> NewFreq
                       end,
            perform_reduction(V - 1, K - Take, NewFreq2)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_sum_square_diff(nums1 :: [integer], nums2 :: [integer], k1 :: integer, k2 :: integer) :: integer
  def min_sum_square_diff(nums1, nums2, k1, k2) do
    freqs = Enum.zip(nums1, nums2)
    |> Enum.reduce(%{}, fn {n1, n2}, acc ->
      d = abs(n1 - n2)
      if d > 0 do
        Map.update(acc, d, 1, &(&1 + 1))
      else
        acc
      end
    end)

    total_k = k1 + k2
    keys = Map.keys(freqs)

    if keys == [] do
      0
    else
      max_d = Enum.max(keys)
      {final_freqs, _} = Enum.reduce(max_d..1, {freqs, total_k}, fn
        _v, {acc_freqs, 0} -> {acc_freqs, 0}
        v, {acc_freqs, k} ->
          count = Map.get(acc_freqs, v, 0)
          take = min(k, count)
          new_acc = Map.put(acc_freqs, v, count - take)
          new_acc = if v > 1 do
            Map.update(new_acc, v - 1, take, &(&1 + take))
          else
            new_acc
          end
          {new_acc, k - take}
      end)

      Enum.reduce(final_freqs, 0, fn {v, count}, sum ->
        sum + v * v * count
      end)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n + M) where n is the length of the input arrays and M is the maximum possible difference (100,000). We iterate through the arrays once to calculate differences and then perform a single pass through the frequency buckets.
- **Space Complexity:** O(M) where M is the maximum possible difference (100,000). We use a frequency array of size M + 1 to store the count of each difference value.
