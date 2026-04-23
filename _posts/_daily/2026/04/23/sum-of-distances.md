---
layout: post
title: "Sum of Distances"
date: 2026-04-23 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Prefix Sum"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/sum-of-distances/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <unordered_map>\n\nusing namespace std;\n\n\
        class Solution {\npublic:\n    vector<long long> distance(vector<int>& nums)\
        \ {\n        int n = nums.size();\n        vector<long long> res(n, 0);\n  \
        \      unordered_map<int, vector<int>> groups;\n        for (int i = 0; i <\
        \ n; ++i) {\n            groups[nums[i]].push_back(i);\n        }\n\n      \
        \  for (auto& entry : groups) {\n            const vector<int>& indices = entry.second;\n\
        \            long long totalSum = 0;\n            for (int idx : indices) {\n\
        \                totalSum += idx;\n            }\n\n            long long prefixSum\
        \ = 0;\n            int k = indices.size();\n            for (int i = 0; i <\
        \ k; ++i) {\n                long long curIdx = indices[i];\n              \
        \  prefixSum += curIdx;\n                long long leftContribution = (long\
        \ long)i * curIdx - (prefixSum - curIdx);\n                long long rightContribution\
        \ = (totalSum - prefixSum) - (long long)(k - 1 - i) * curIdx;\n            \
        \    res[curIdx] = leftContribution + rightContribution;\n            }\n  \
        \      }\n        return res;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public long[] distance(int[]\
        \ nums) {\n        int n = nums.length;\n        long[] res = new long[n];\n\
        \        Map<Integer, List<Integer>> groups = new HashMap<>();\n\n        for\
        \ (int i = 0; i < n; i++) {\n            groups.computeIfAbsent(nums[i], k ->\
        \ new ArrayList<>()).add(i);\n        }\n\n        for (List<Integer> indices\
        \ : groups.values()) {\n            long totalSum = 0;\n            for (int\
        \ idx : indices) {\n                totalSum += idx;\n            }\n\n    \
        \        long prefixSum = 0;\n            int k = indices.size();\n        \
        \    for (int i = 0; i < k; i++) {\n                long curIdx = indices.get(i);\n\
        \                prefixSum += curIdx;\n                long left = (long) i\
        \ * curIdx - (prefixSum - curIdx);\n                long right = (totalSum -\
        \ prefixSum) - (long) (k - 1 - i) * curIdx;\n                res[(int) curIdx]\
        \ = left + right;\n            }\n        }\n\n        return res;\n    }\n}"
      python: "class Solution(object):\n    def distance(self, nums):\n        \"\"\"\
        \n        :type nums: List[int]\n        :rtype: List[int]\n        \"\"\"\n\
        \        groups = {}\n        for i, x in enumerate(nums):\n            if x\
        \ not in groups:\n                groups[x] = []\n            groups[x].append(i)\n\
        \n        n = len(nums)\n        res = [0] * n\n\n        for x in groups:\n\
        \            indices = groups[x]\n            total_sum = sum(indices)\n   \
        \         prefix_sum = 0\n            k = len(indices)\n            for i, idx\
        \ in enumerate(indices):\n                prefix_sum += idx\n              \
        \  left = i * idx - (prefix_sum - idx)\n                right = (total_sum -\
        \ prefix_sum) - (k - 1 - i) * idx\n                res[idx] = left + right\n\
        \n        return res"
      python3: "from typing import List\nfrom collections import defaultdict\n\nclass\
        \ Solution:\n    def distance(self, nums: List[int]) -> List[int]:\n       \
        \ groups = defaultdict(list)\n        for i, x in enumerate(nums):\n       \
        \     groups[x].append(i)\n\n        n = len(nums)\n        res = [0] * n\n\n\
        \        for x in groups:\n            indices = groups[x]\n            total_sum\
        \ = sum(indices)\n            prefix_sum = 0\n            k = len(indices)\n\
        \            for i, idx in enumerate(indices):\n                prefix_sum +=\
        \ idx\n                left = i * idx - (prefix_sum - idx)\n               \
        \ right = (total_sum - prefix_sum) - (k - 1 - i) * idx\n                res[idx]\
        \ = left + right\n\n        return res"
      c: "#include <stdio.h>\n#include <stdlib.h>\n\ntypedef struct {\n    int val;\n\
        \    int original_idx;\n} Pair;\n\nint compare(const void* a, const void* b)\
        \ {\n    const Pair* p1 = (const Pair*)a;\n    const Pair* p2 = (const Pair*)b;\n\
        \    if (p1->val != p2->val) return (p1->val < p2->val) ? -1 : 1;\n    return\
        \ (p1->original_idx < p2->original_idx) ? -1 : 1;\n}\n\n/**\n * Note: The returned\
        \ array must be malloced, assume caller calls free().\n */\nlong long* distance(int*\
        \ nums, int numsSize, int* returnSize) {\n    *returnSize = numsSize;\n    Pair*\
        \ pairs = (Pair*)malloc(sizeof(Pair) * numsSize);\n    for (int i = 0; i < numsSize;\
        \ i++) {\n        pairs[i].val = nums[i];\n        pairs[i].original_idx = i;\n\
        \    }\n\n    qsort(pairs, numsSize, sizeof(Pair), compare);\n\n    long long*\
        \ res = (long long*)calloc(numsSize, sizeof(long long));\n\n    int i = 0;\n\
        \    while (i < numsSize) {\n        int j = i;\n        long long group_sum\
        \ = 0;\n        while (j < numsSize && pairs[j].val == pairs[i].val) {\n   \
        \         group_sum += pairs[j].original_idx;\n            j++;\n        }\n\
        \n        int count = j - i;\n        long long prefix = 0;\n        for (int\
        \ k = 0; k < count; k++) {\n            long long cur_idx = pairs[i + k].original_idx;\n\
        \            prefix += cur_idx;\n            long long left = (long long)k *\
        \ cur_idx - (prefix - cur_idx);\n            long long right = (group_sum -\
        \ prefix) - (long long)(count - 1 - k) * cur_idx;\n            res[cur_idx]\
        \ = left + right;\n        }\n        i = j;\n    }\n\n    free(pairs);\n  \
        \  return res;\n}"
      csharp: "public class Solution {\n    public long[] Distance(int[] nums) {\n \
        \       int n = nums.Length;\n        long[] res = new long[n];\n        Dictionary<int,\
        \ List<int>> groups = new Dictionary<int, List<int>>();\n        for (int i\
        \ = 0; i < n; i++) {\n            if (!groups.TryGetValue(nums[i], out List<int>\
        \ indices)) {\n                indices = new List<int>();\n                groups[nums[i]]\
        \ = indices;\n            }\n            indices.Add(i);\n        }\n\n    \
        \    foreach (var indices in groups.Values) {\n            int k = indices.Count;\n\
        \            long totalSum = 0;\n            foreach (int idx in indices) {\n\
        \                totalSum += idx;\n            }\n\n            long leftSum\
        \ = 0;\n            for (int i = 0; i < k; i++) {\n                int p_i_idx\
        \ = indices[i];\n                long p_i = (long)p_i_idx;\n               \
        \ long rightSum = totalSum - leftSum - p_i;\n                res[p_i_idx] =\
        \ ((long)i * p_i - leftSum) + (rightSum - (long)(k - 1 - i) * p_i);\n      \
        \          leftSum += p_i;\n            }\n        }\n\n        return res;\n\
        \    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number[]}\n */\nvar distance\
        \ = function(nums) {\n    const n = nums.length;\n    const res = new Array(n).fill(0);\n\
        \    const groups = new Map();\n\n    for (let i = 0; i < n; i++) {\n      \
        \  if (!groups.has(nums[i])) {\n            groups.set(nums[i], []);\n     \
        \   }\n        groups.get(nums[i]).push(i);\n    }\n\n    for (const indices\
        \ of groups.values()) {\n        const k = indices.length;\n        let totalSum\
        \ = 0;\n        for (let i = 0; i < k; i++) {\n            totalSum += indices[i];\n\
        \        }\n\n        let leftSum = 0;\n        for (let i = 0; i < k; i++)\
        \ {\n            const p_i = indices[i];\n            const rightSum = totalSum\
        \ - leftSum - p_i;\n            res[p_i] = (i * p_i - leftSum) + (rightSum -\
        \ (k - 1 - i) * p_i);\n            leftSum += p_i;\n        }\n    }\n\n   \
        \ return res;\n};"
      typescript: "function distance(nums: number[]): number[] {\n    const n: number\
        \ = nums.length;\n    const res: number[] = new Array(n).fill(0);\n    const\
        \ groups: Map<number, number[]> = new Map();\n\n    for (let i = 0; i < n; i++)\
        \ {\n        if (!groups.has(nums[i])) {\n            groups.set(nums[i], []);\n\
        \        }\n        groups.get(nums[i])!.push(i);\n    }\n\n    for (const indices\
        \ of groups.values()) {\n        const k: number = indices.length;\n       \
        \ let totalSum: number = 0;\n        for (let i = 0; i < k; i++) {\n       \
        \     totalSum += indices[i];\n        }\n\n        let leftSum: number = 0;\n\
        \        for (let i = 0; i < k; i++) {\n            const p_i: number = indices[i];\n\
        \            const rightSum: number = totalSum - leftSum - p_i;\n          \
        \  res[p_i] = (i * p_i - leftSum) + (rightSum - (k - 1 - i) * p_i);\n      \
        \      leftSum += p_i;\n        }\n    }\n\n    return res;\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer[]\n     */\n    function distance($nums) {\n        $n = count($nums);\n\
        \        $res = array_fill(0, $n, 0);\n        $groups = [];\n\n        for\
        \ ($i = 0; $i < $n; $i++) {\n            $groups[$nums[$i]][] = $i;\n      \
        \  }\n\n        foreach ($groups as $indices) {\n            $k = count($indices);\n\
        \            $totalSum = array_sum($indices);\n            $leftSum = 0;\n\n\
        \            for ($i = 0; $i < $k; $i++) {\n                $p_i = $indices[$i];\n\
        \                $rightSum = $totalSum - $leftSum - $p_i;\n                $res[$p_i]\
        \ = ($i * $p_i - $leftSum) + ($rightSum - ($k - 1 - $i) * $p_i);\n         \
        \       $leftSum += $p_i;\n            }\n        }\n\n        return $res;\n\
        \    }\n}"
      swift: "class Solution {\n    func distance(_ nums: [Int]) -> [Int] {\n      \
        \  let n = nums.count\n        var res = [Int](repeating: 0, count: n)\n   \
        \     var groups = [Int: [Int]]()\n\n        for i in 0..<n {\n            groups[nums[i],\
        \ default: []].append(i)\n        }\n\n        for indices in groups.values\
        \ {\n            let k = indices.count\n            let totalSum = indices.reduce(0,\
        \ +)\n            var leftSum = 0\n\n            for i in 0..<k {\n        \
        \        let p_i = indices[i]\n                let rightSum = totalSum - leftSum\
        \ - p_i\n                res[p_i] = (i * p_i - leftSum) + (rightSum - (k - 1\
        \ - i) * p_i)\n                leftSum += p_i\n            }\n        }\n\n\
        \        return res\n    }\n}"
      kotlin: "class Solution {\n    fun distance(nums: IntArray): LongArray {\n   \
        \     val n = nums.size\n        val res = LongArray(n)\n        val groups\
        \ = mutableMapOf<Int, MutableList<Int>>()\n        for (i in nums.indices) {\n\
        \            groups.getOrPut(nums[i]) { mutableListOf() }.add(i)\n        }\n\
        \n        for (indices in groups.values) {\n            val k = indices.size\n\
        \            if (k <= 1) continue\n\n            var totalSum = 0L\n       \
        \     for (idx in indices) {\n                totalSum += idx.toLong()\n   \
        \         }\n\n            var prefixSum = 0L\n            for (i in indices.indices)\
        \ {\n                val p_i = indices[i].toLong()\n                prefixSum\
        \ += p_i\n\n                val left = i.toLong() * p_i - (prefixSum - p_i)\n\
        \                val right = (totalSum - prefixSum) - (k.toLong() - 1 - i) *\
        \ p_i\n                res[indices[i]] = left + right\n            }\n     \
        \   }\n        return res\n    }\n}"
      dart: "class Solution {\n  List<int> distance(List<int> nums) {\n    int n = nums.length;\n\
        \    List<int> res = List<int>.filled(n, 0);\n    Map<int, List<int>> groups\
        \ = {};\n\n    for (int i = 0; i < n; i++) {\n      groups.putIfAbsent(nums[i],\
        \ () => []).add(i);\n    }\n\n    groups.forEach((key, indices) {\n      int\
        \ k = indices.length;\n      if (k > 1) {\n        int totalSum = 0;\n     \
        \   for (int idx in indices) {\n          totalSum += idx;\n        }\n\n  \
        \      int prefixSum = 0;\n        for (int i = 0; i < k; i++) {\n         \
        \ int p_i = indices[i];\n          prefixSum += p_i;\n\n          int left =\
        \ i * p_i - (prefixSum - p_i);\n          int right = (totalSum - prefixSum)\
        \ - (k - 1 - i) * p_i;\n          res[p_i] = left + right;\n        }\n    \
        \  }\n    });\n\n    return res;\n  }\n}"
      go: "func distance(nums []int) []int64 {\n    n := len(nums)\n    res := make([]int64,\
        \ n)\n    groups := make(map[int][]int)\n\n    for i, val := range nums {\n\
        \        groups[val] = append(groups[val], i)\n    }\n\n    for _, indices :=\
        \ range groups {\n        k := len(indices)\n        if k <= 1 {\n         \
        \   continue\n        }\n\n        var totalSum int64 = 0\n        for _, idx\
        \ := range indices {\n            totalSum += int64(idx)\n        }\n\n    \
        \    var prefixSum int64 = 0\n        for i, idx := range indices {\n      \
        \      p_i := int64(idx)\n            prefixSum += p_i\n\n            left :=\
        \ int64(i)*p_i - (prefixSum - p_i)\n            right := (totalSum - prefixSum)\
        \ - int64(k-1-i)*p_i\n            res[idx] = left + right\n        }\n    }\n\
        \n    return res\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer[]}\ndef distance(nums)\n\
        \  n = nums.length\n  res = Array.new(n, 0)\n  groups = {}\n\n  nums.each_with_index\
        \ do |val, i|\n    groups[val] ||= []\n    groups[val] << i\n  end\n\n  groups.each_value\
        \ do |indices|\n    k = indices.length\n    next if k <= 1\n\n    total_sum\
        \ = 0\n    indices.each { |idx| total_sum += idx }\n\n    prefix_sum = 0\n \
        \   indices.each_with_index do |p_i, i|\n      prefix_sum += p_i\n\n      left\
        \ = i * p_i - (prefix_sum - p_i)\n      right = (total_sum - prefix_sum) - (k\
        \ - 1 - i) * p_i\n      res[p_i] = left + right\n    end\n  end\n\n  res\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n    def distance(nums:\
        \ Array[Int]): Array[Long] = {\n        val n = nums.length\n        val res\
        \ = new Array[Long](n)\n        val groups = mutable.Map[Int, mutable.ArrayBuffer[Int]]()\n\
        \n        var i = 0\n        while (i < n) {\n            groups.getOrElseUpdate(nums(i),\
        \ mutable.ArrayBuffer[Int]()) += i\n            i += 1\n        }\n\n      \
        \  for (indices <- groups.values) {\n            val k = indices.length\n  \
        \          if (k > 1) {\n                var totalSum: Long = 0\n          \
        \      for (idx <- indices) {\n                    totalSum += idx.toLong\n\
        \                }\n\n                var prefixSum: Long = 0\n            \
        \    for (j <- 0 until k) {\n                    val p_j: Long = indices(j).toLong\n\
        \                    prefixSum += p_j\n\n                    val left: Long\
        \ = j.toLong * p_j - (prefixSum - p_j)\n                    val right: Long\
        \ = (totalSum - prefixSum) - (k.toLong - 1 - j) * p_j\n                    res(indices(j))\
        \ = left + right\n                }\n            }\n        }\n        res\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn distance(nums: Vec<i32>) -> Vec<i64> {\n  \
        \      let n = nums.len();\n        let mut indices_map: std::collections::HashMap<i32,\
        \ Vec<usize>> = std::collections::HashMap::with_capacity(n);\n        for (i,\
        \ &num) in nums.iter().enumerate() {\n            indices_map.entry(num).or_insert_with(Vec::new).push(i);\n\
        \        }\n\n        let mut arr = vec![0i64; n];\n        for indices in indices_map.values()\
        \ {\n            let k = indices.len() as i64;\n            let mut total_sum:\
        \ i64 = 0;\n            for &idx in indices {\n                total_sum +=\
        \ idx as i64;\n            }\n\n            let mut left_sum: i64 = 0;\n   \
        \         for (m, &idx) in indices.iter().enumerate() {\n                let\
        \ m_i64 = m as i64;\n                let idx_i64 = idx as i64;\n\n         \
        \       let left_part = m_i64 * idx_i64 - left_sum;\n                let right_part\
        \ = (total_sum - left_sum - idx_i64) - (k - m_i64 - 1) * idx_i64;\n\n      \
        \          arr[idx] = left_part + right_part;\n                left_sum += idx_i64;\n\
        \            }\n        }\n        arr\n    }\n}"
      racket: "(define/contract (distance nums)\n  (-> (listof exact-integer?) (listof\
        \ exact-integer?))\n  (let* ([n (length nums)]\n         [res (make-vector n\
        \ 0)]\n         [indices-map (make-hash)])\n    (for ([num nums] [i (in-range\
        \ n)])\n      (hash-update! indices-map num (lambda (v) (cons i v)) '()))\n\
        \    (for ([(val indices-rev) (in-hash indices-map)])\n      (let* ([indices\
        \ (reverse indices-rev)]\n             [k (length indices)]\n             [total-sum\
        \ (foldl + 0 indices)])\n        (for/fold ([left-sum 0])\n                \
        \  ([idx indices]\n                   [m (in-range k)])\n          (let* ([left-part\
        \ (- (* m idx) left-sum)]\n                 [right-part (- (- total-sum left-sum\
        \ idx) (* (- k m 1) idx))])\n            (vector-set! res idx (+ left-part right-part))\n\
        \            (+ left-sum idx)))))\n    (vector->list res)))"
      erlang: "-spec distance(Nums :: [integer()]) -> [integer()].\ndistance(Nums) ->\n\
        \  {IndicesMap, N} = lists:foldl(\n    fun(Num, {AccMap, I}) ->\n      {maps:update_with(Num,\
        \ fun(L) -> [I | L] end, [I], AccMap), I + 1}\n    end,\n    {#{}, 0},\n   \
        \ Nums\n  ),\n  ResMap = maps:fold(\n    fun(_Num, IndicesRev, AccResMap) ->\n\
        \      Indices = lists:reverse(IndicesRev),\n      K = length(Indices),\n  \
        \    TotalSum = lists:sum(Indices),\n      {_, _, FinalAccResMap} = lists:foldl(\n\
        \        fun(Idx, {M, LeftSum, InnerAcc}) ->\n          LeftPart = M * Idx -\
        \ LeftSum,\n          RightPart = (TotalSum - LeftSum - Idx) - (K - M - 1) *\
        \ Idx,\n          {M + 1, LeftSum + Idx, maps:put(Idx, LeftPart + RightPart,\
        \ InnerAcc)}\n        end,\n        {0, 0, AccResMap},\n        Indices\n  \
        \    ),\n      FinalAccResMap\n    end,\n    #{}, \n    IndicesMap\n  ),\n \
        \ [maps:get(I, ResMap) || I <- lists:seq(0, N - 1)]."
      elixir: "defmodule Solution do\n  @spec distance(nums :: [integer]) :: [integer]\n\
        \  def distance(nums) do\n    n = length(nums)\n    indices_map = \n      nums\n\
        \      |> Enum.with_index()\n      |> Enum.group_by(fn {num, _i} -> num end,\
        \ fn {_num, i} -> i end)\n\n    res_map = \n      indices_map\n      |> Enum.reduce(%{},\
        \ fn {_num, indices}, acc_res ->\n        k = length(indices)\n        total_sum\
        \ = Enum.sum(indices)\n\n        {_, _, final_acc} = \n          Enum.reduce(indices,\
        \ {0, 0, acc_res}, fn idx, {m, left_sum, inner_acc} ->\n            left_part\
        \ = m * idx - left_sum\n            right_part = (total_sum - left_sum - idx)\
        \ - (k - m - 1) * idx\n            {m + 1, left_sum + idx, Map.put(inner_acc,\
        \ idx, left_part + right_part)}\n          end)\n        final_acc\n      end)\n\
        \n    0..(n - 1)\n    |> Enum.map(&Map.get(res_map, &1))\n  end\nend"
    approach: 'The core idea is to group the indices of identical elements together
      and use a mathematical optimization to calculate the sum of absolute differences.
      For any given value that appears at sorted indices $p_0, p_1, \dots, p_{k-1}$,
      the distance sum for an index $p_i$ is the sum of $(p_i - p_j)$ for all $j < i$
      plus the sum of $(p_j - p_i)$ for all $j > i$. Calculating this directly for each
      occurrence would result in $O(n^2)$ time, but it can be computed in linear time
      using the prefix and suffix sums of the index group. Specifically, the left distance
      sum is $(i \cdot p_i - \text{prefixSum}_{i-1})$ and the right distance sum is
      $(\text{suffixSum}_{i+1} - (k - 1 - i) \cdot p_i)$.


      To implement this, we first traverse the array to group indices by their corresponding
      values in a hash map or by sorting pairs of values and indices. For each group
      of indices, we calculate the total sum of indices. Then, as we iterate through
      the indices within each group, we maintain a running prefix sum. This allows us
      to calculate the left and right distance contributions in $O(1)$ for each element,
      totaling $O(n)$ time for all elements. This strategy efficiently avoids the nested
      loop and scales effectively within the given constraints.'
    time_complexity: O(n) for HashMap-based solutions (C++, Java, Python) as we traverse
      the input array once to build the map and once more to calculate the sums. For
      the C solution, the complexity is O(n log n) because it sorts the elements before
      processing them in linear time.
    space_complexity: O(n) since we need to store either a mapping of each unique value
      to its list of indices or an auxiliary array of structs/pairs of size n, in addition
      to the result array.
    elapsed_time: 255.74968242645264
    model: gemini-3-flash-preview
    generated_at: '2026-04-23 02:02:51 '
---

## Problem #2615: Sum of Distances

**Difficulty:** Medium

**Topics:** Array, Hash Table, Prefix Sum

## Problem Description

<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code>. There exists an array <code>arr</code> of length <code>nums.length</code>, where <code>arr[i]</code> is the sum of <code>|i - j|</code> over all <code>j</code> such that <code>nums[j] == nums[i]</code> and <code>j != i</code>. If there is no such <code>j</code>, set <code>arr[i]</code> to be <code>0</code>.</p>

<p>Return <em>the array </em><code>arr</code><em>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,1,1,2]
<strong>Output:</strong> [5,0,3,4,0]
<strong>Explanation:</strong> 
When i = 0, nums[0] == nums[2] and nums[0] == nums[3]. Therefore, arr[0] = |0 - 2| + |0 - 3| = 5. 
When i = 1, arr[1] = 0 because there is no other index with value 3.
When i = 2, nums[2] == nums[0] and nums[2] == nums[3]. Therefore, arr[2] = |2 - 0| + |2 - 3| = 3. 
When i = 3, nums[3] == nums[0] and nums[3] == nums[2]. Therefore, arr[3] = |3 - 0| + |3 - 2| = 4. 
When i = 4, arr[4] = 0 because there is no other index with value 2. 

</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,5,3]
<strong>Output:</strong> [0,0,0]
<strong>Explanation:</strong> Since each element in nums is distinct, arr[i] = 0 for all i.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as <a href="https://leetcode.com/problems/intervals-between-identical-elements/description/" target="_blank"> 2121: Intervals Between Identical Elements.</a></p>


## Hints

1. Can we use the prefix sum here?

2. For each number x, collect all the indices where x occurs, and calculate the prefix sum of the array.

3. For each occurrence of x, the indices to the right will be regular subtraction while the indices to the left will be reversed subtraction.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The core idea is to group the indices of identical elements together and use a mathematical optimization to calculate the sum of absolute differences. For any given value that appears at sorted indices $p_0, p_1, \dots, p_{k-1}$, the distance sum for an index $p_i$ is the sum of $(p_i - p_j)$ for all $j < i$ plus the sum of $(p_j - p_i)$ for all $j > i$. Calculating this directly for each occurrence would result in $O(n^2)$ time, but it can be computed in linear time using the prefix and suffix sums of the index group. Specifically, the left distance sum is $(i \cdot p_i - \text{prefixSum}_{i-1})$ and the right distance sum is $(\text{suffixSum}_{i+1} - (k - 1 - i) \cdot p_i)$.

To implement this, we first traverse the array to group indices by their corresponding values in a hash map or by sorting pairs of values and indices. For each group of indices, we calculate the total sum of indices. Then, as we iterate through the indices within each group, we maintain a running prefix sum. This allows us to calculate the left and right distance contributions in $O(1)$ for each element, totaling $O(n)$ time for all elements. This strategy efficiently avoids the nested loop and scales effectively within the given constraints.

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
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<long long> distance(vector<int>& nums) {
        int n = nums.size();
        vector<long long> res(n, 0);
        unordered_map<int, vector<int>> groups;
        for (int i = 0; i < n; ++i) {
            groups[nums[i]].push_back(i);
        }

        for (auto& entry : groups) {
            const vector<int>& indices = entry.second;
            long long totalSum = 0;
            for (int idx : indices) {
                totalSum += idx;
            }

            long long prefixSum = 0;
            int k = indices.size();
            for (int i = 0; i < k; ++i) {
                long long curIdx = indices[i];
                prefixSum += curIdx;
                long long leftContribution = (long long)i * curIdx - (prefixSum - curIdx);
                long long rightContribution = (totalSum - prefixSum) - (long long)(k - 1 - i) * curIdx;
                res[curIdx] = leftContribution + rightContribution;
            }
        }
        return res;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.*;

class Solution {
    public long[] distance(int[] nums) {
        int n = nums.length;
        long[] res = new long[n];
        Map<Integer, List<Integer>> groups = new HashMap<>();

        for (int i = 0; i < n; i++) {
            groups.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
        }

        for (List<Integer> indices : groups.values()) {
            long totalSum = 0;
            for (int idx : indices) {
                totalSum += idx;
            }

            long prefixSum = 0;
            int k = indices.size();
            for (int i = 0; i < k; i++) {
                long curIdx = indices.get(i);
                prefixSum += curIdx;
                long left = (long) i * curIdx - (prefixSum - curIdx);
                long right = (totalSum - prefixSum) - (long) (k - 1 - i) * curIdx;
                res[(int) curIdx] = left + right;
            }
        }

        return res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def distance(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        groups = {}
        for i, x in enumerate(nums):
            if x not in groups:
                groups[x] = []
            groups[x].append(i)

        n = len(nums)
        res = [0] * n

        for x in groups:
            indices = groups[x]
            total_sum = sum(indices)
            prefix_sum = 0
            k = len(indices)
            for i, idx in enumerate(indices):
                prefix_sum += idx
                left = i * idx - (prefix_sum - idx)
                right = (total_sum - prefix_sum) - (k - 1 - i) * idx
                res[idx] = left + right

        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from typing import List
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        groups = defaultdict(list)
        for i, x in enumerate(nums):
            groups[x].append(i)

        n = len(nums)
        res = [0] * n

        for x in groups:
            indices = groups[x]
            total_sum = sum(indices)
            prefix_sum = 0
            k = len(indices)
            for i, idx in enumerate(indices):
                prefix_sum += idx
                left = i * idx - (prefix_sum - idx)
                right = (total_sum - prefix_sum) - (k - 1 - i) * idx
                res[idx] = left + right

        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int val;
    int original_idx;
} Pair;

int compare(const void* a, const void* b) {
    const Pair* p1 = (const Pair*)a;
    const Pair* p2 = (const Pair*)b;
    if (p1->val != p2->val) return (p1->val < p2->val) ? -1 : 1;
    return (p1->original_idx < p2->original_idx) ? -1 : 1;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* distance(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    Pair* pairs = (Pair*)malloc(sizeof(Pair) * numsSize);
    for (int i = 0; i < numsSize; i++) {
        pairs[i].val = nums[i];
        pairs[i].original_idx = i;
    }

    qsort(pairs, numsSize, sizeof(Pair), compare);

    long long* res = (long long*)calloc(numsSize, sizeof(long long));

    int i = 0;
    while (i < numsSize) {
        int j = i;
        long long group_sum = 0;
        while (j < numsSize && pairs[j].val == pairs[i].val) {
            group_sum += pairs[j].original_idx;
            j++;
        }

        int count = j - i;
        long long prefix = 0;
        for (int k = 0; k < count; k++) {
            long long cur_idx = pairs[i + k].original_idx;
            prefix += cur_idx;
            long long left = (long long)k * cur_idx - (prefix - cur_idx);
            long long right = (group_sum - prefix) - (long long)(count - 1 - k) * cur_idx;
            res[cur_idx] = left + right;
        }
        i = j;
    }

    free(pairs);
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public long[] Distance(int[] nums) {
        int n = nums.Length;
        long[] res = new long[n];
        Dictionary<int, List<int>> groups = new Dictionary<int, List<int>>();
        for (int i = 0; i < n; i++) {
            if (!groups.TryGetValue(nums[i], out List<int> indices)) {
                indices = new List<int>();
                groups[nums[i]] = indices;
            }
            indices.Add(i);
        }

        foreach (var indices in groups.Values) {
            int k = indices.Count;
            long totalSum = 0;
            foreach (int idx in indices) {
                totalSum += idx;
            }

            long leftSum = 0;
            for (int i = 0; i < k; i++) {
                int p_i_idx = indices[i];
                long p_i = (long)p_i_idx;
                long rightSum = totalSum - leftSum - p_i;
                res[p_i_idx] = ((long)i * p_i - leftSum) + (rightSum - (long)(k - 1 - i) * p_i);
                leftSum += p_i;
            }
        }

        return res;
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
var distance = function(nums) {
    const n = nums.length;
    const res = new Array(n).fill(0);
    const groups = new Map();

    for (let i = 0; i < n; i++) {
        if (!groups.has(nums[i])) {
            groups.set(nums[i], []);
        }
        groups.get(nums[i]).push(i);
    }

    for (const indices of groups.values()) {
        const k = indices.length;
        let totalSum = 0;
        for (let i = 0; i < k; i++) {
            totalSum += indices[i];
        }

        let leftSum = 0;
        for (let i = 0; i < k; i++) {
            const p_i = indices[i];
            const rightSum = totalSum - leftSum - p_i;
            res[p_i] = (i * p_i - leftSum) + (rightSum - (k - 1 - i) * p_i);
            leftSum += p_i;
        }
    }

    return res;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function distance(nums: number[]): number[] {
    const n: number = nums.length;
    const res: number[] = new Array(n).fill(0);
    const groups: Map<number, number[]> = new Map();

    for (let i = 0; i < n; i++) {
        if (!groups.has(nums[i])) {
            groups.set(nums[i], []);
        }
        groups.get(nums[i])!.push(i);
    }

    for (const indices of groups.values()) {
        const k: number = indices.length;
        let totalSum: number = 0;
        for (let i = 0; i < k; i++) {
            totalSum += indices[i];
        }

        let leftSum: number = 0;
        for (let i = 0; i < k; i++) {
            const p_i: number = indices[i];
            const rightSum: number = totalSum - leftSum - p_i;
            res[p_i] = (i * p_i - leftSum) + (rightSum - (k - 1 - i) * p_i);
            leftSum += p_i;
        }
    }

    return res;
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
     * @return Integer[]
     */
    function distance($nums) {
        $n = count($nums);
        $res = array_fill(0, $n, 0);
        $groups = [];

        for ($i = 0; $i < $n; $i++) {
            $groups[$nums[$i]][] = $i;
        }

        foreach ($groups as $indices) {
            $k = count($indices);
            $totalSum = array_sum($indices);
            $leftSum = 0;

            for ($i = 0; $i < $k; $i++) {
                $p_i = $indices[$i];
                $rightSum = $totalSum - $leftSum - $p_i;
                $res[$p_i] = ($i * $p_i - $leftSum) + ($rightSum - ($k - 1 - $i) * $p_i);
                $leftSum += $p_i;
            }
        }

        return $res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func distance(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var res = [Int](repeating: 0, count: n)
        var groups = [Int: [Int]]()

        for i in 0..<n {
            groups[nums[i], default: []].append(i)
        }

        for indices in groups.values {
            let k = indices.count
            let totalSum = indices.reduce(0, +)
            var leftSum = 0

            for i in 0..<k {
                let p_i = indices[i]
                let rightSum = totalSum - leftSum - p_i
                res[p_i] = (i * p_i - leftSum) + (rightSum - (k - 1 - i) * p_i)
                leftSum += p_i
            }
        }

        return res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun distance(nums: IntArray): LongArray {
        val n = nums.size
        val res = LongArray(n)
        val groups = mutableMapOf<Int, MutableList<Int>>()
        for (i in nums.indices) {
            groups.getOrPut(nums[i]) { mutableListOf() }.add(i)
        }

        for (indices in groups.values) {
            val k = indices.size
            if (k <= 1) continue

            var totalSum = 0L
            for (idx in indices) {
                totalSum += idx.toLong()
            }

            var prefixSum = 0L
            for (i in indices.indices) {
                val p_i = indices[i].toLong()
                prefixSum += p_i

                val left = i.toLong() * p_i - (prefixSum - p_i)
                val right = (totalSum - prefixSum) - (k.toLong() - 1 - i) * p_i
                res[indices[i]] = left + right
            }
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
  List<int> distance(List<int> nums) {
    int n = nums.length;
    List<int> res = List<int>.filled(n, 0);
    Map<int, List<int>> groups = {};

    for (int i = 0; i < n; i++) {
      groups.putIfAbsent(nums[i], () => []).add(i);
    }

    groups.forEach((key, indices) {
      int k = indices.length;
      if (k > 1) {
        int totalSum = 0;
        for (int idx in indices) {
          totalSum += idx;
        }

        int prefixSum = 0;
        for (int i = 0; i < k; i++) {
          int p_i = indices[i];
          prefixSum += p_i;

          int left = i * p_i - (prefixSum - p_i);
          int right = (totalSum - prefixSum) - (k - 1 - i) * p_i;
          res[p_i] = left + right;
        }
      }
    });

    return res;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func distance(nums []int) []int64 {
    n := len(nums)
    res := make([]int64, n)
    groups := make(map[int][]int)

    for i, val := range nums {
        groups[val] = append(groups[val], i)
    }

    for _, indices := range groups {
        k := len(indices)
        if k <= 1 {
            continue
        }

        var totalSum int64 = 0
        for _, idx := range indices {
            totalSum += int64(idx)
        }

        var prefixSum int64 = 0
        for i, idx := range indices {
            p_i := int64(idx)
            prefixSum += p_i

            left := int64(i)*p_i - (prefixSum - p_i)
            right := (totalSum - prefixSum) - int64(k-1-i)*p_i
            res[idx] = left + right
        }
    }

    return res
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer[]}
def distance(nums)
  n = nums.length
  res = Array.new(n, 0)
  groups = {}

  nums.each_with_index do |val, i|
    groups[val] ||= []
    groups[val] << i
  end

  groups.each_value do |indices|
    k = indices.length
    next if k <= 1

    total_sum = 0
    indices.each { |idx| total_sum += idx }

    prefix_sum = 0
    indices.each_with_index do |p_i, i|
      prefix_sum += p_i

      left = i * p_i - (prefix_sum - p_i)
      right = (total_sum - prefix_sum) - (k - 1 - i) * p_i
      res[p_i] = left + right
    end
  end

  res
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

object Solution {
    def distance(nums: Array[Int]): Array[Long] = {
        val n = nums.length
        val res = new Array[Long](n)
        val groups = mutable.Map[Int, mutable.ArrayBuffer[Int]]()

        var i = 0
        while (i < n) {
            groups.getOrElseUpdate(nums(i), mutable.ArrayBuffer[Int]()) += i
            i += 1
        }

        for (indices <- groups.values) {
            val k = indices.length
            if (k > 1) {
                var totalSum: Long = 0
                for (idx <- indices) {
                    totalSum += idx.toLong
                }

                var prefixSum: Long = 0
                for (j <- 0 until k) {
                    val p_j: Long = indices(j).toLong
                    prefixSum += p_j

                    val left: Long = j.toLong * p_j - (prefixSum - p_j)
                    val right: Long = (totalSum - prefixSum) - (k.toLong - 1 - j) * p_j
                    res(indices(j)) = left + right
                }
            }
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
    pub fn distance(nums: Vec<i32>) -> Vec<i64> {
        let n = nums.len();
        let mut indices_map: std::collections::HashMap<i32, Vec<usize>> = std::collections::HashMap::with_capacity(n);
        for (i, &num) in nums.iter().enumerate() {
            indices_map.entry(num).or_insert_with(Vec::new).push(i);
        }

        let mut arr = vec![0i64; n];
        for indices in indices_map.values() {
            let k = indices.len() as i64;
            let mut total_sum: i64 = 0;
            for &idx in indices {
                total_sum += idx as i64;
            }

            let mut left_sum: i64 = 0;
            for (m, &idx) in indices.iter().enumerate() {
                let m_i64 = m as i64;
                let idx_i64 = idx as i64;

                let left_part = m_i64 * idx_i64 - left_sum;
                let right_part = (total_sum - left_sum - idx_i64) - (k - m_i64 - 1) * idx_i64;

                arr[idx] = left_part + right_part;
                left_sum += idx_i64;
            }
        }
        arr
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (distance nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ([n (length nums)]
         [res (make-vector n 0)]
         [indices-map (make-hash)])
    (for ([num nums] [i (in-range n)])
      (hash-update! indices-map num (lambda (v) (cons i v)) '()))
    (for ([(val indices-rev) (in-hash indices-map)])
      (let* ([indices (reverse indices-rev)]
             [k (length indices)]
             [total-sum (foldl + 0 indices)])
        (for/fold ([left-sum 0])
                  ([idx indices]
                   [m (in-range k)])
          (let* ([left-part (- (* m idx) left-sum)]
                 [right-part (- (- total-sum left-sum idx) (* (- k m 1) idx))])
            (vector-set! res idx (+ left-part right-part))
            (+ left-sum idx)))))
    (vector->list res)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec distance(Nums :: [integer()]) -> [integer()].
distance(Nums) ->
  {IndicesMap, N} = lists:foldl(
    fun(Num, {AccMap, I}) ->
      {maps:update_with(Num, fun(L) -> [I | L] end, [I], AccMap), I + 1}
    end,
    {#{}, 0},
    Nums
  ),
  ResMap = maps:fold(
    fun(_Num, IndicesRev, AccResMap) ->
      Indices = lists:reverse(IndicesRev),
      K = length(Indices),
      TotalSum = lists:sum(Indices),
      {_, _, FinalAccResMap} = lists:foldl(
        fun(Idx, {M, LeftSum, InnerAcc}) ->
          LeftPart = M * Idx - LeftSum,
          RightPart = (TotalSum - LeftSum - Idx) - (K - M - 1) * Idx,
          {M + 1, LeftSum + Idx, maps:put(Idx, LeftPart + RightPart, InnerAcc)}
        end,
        {0, 0, AccResMap},
        Indices
      ),
      FinalAccResMap
    end,
    #{}, 
    IndicesMap
  ),
  [maps:get(I, ResMap) || I <- lists:seq(0, N - 1)].
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec distance(nums :: [integer]) :: [integer]
  def distance(nums) do
    n = length(nums)
    indices_map = 
      nums
      |> Enum.with_index()
      |> Enum.group_by(fn {num, _i} -> num end, fn {_num, i} -> i end)

    res_map = 
      indices_map
      |> Enum.reduce(%{}, fn {_num, indices}, acc_res ->
        k = length(indices)
        total_sum = Enum.sum(indices)

        {_, _, final_acc} = 
          Enum.reduce(indices, {0, 0, acc_res}, fn idx, {m, left_sum, inner_acc} ->
            left_part = m * idx - left_sum
            right_part = (total_sum - left_sum - idx) - (k - m - 1) * idx
            {m + 1, left_sum + idx, Map.put(inner_acc, idx, left_part + right_part)}
          end)
        final_acc
      end)

    0..(n - 1)
    |> Enum.map(&Map.get(res_map, &1))
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) for HashMap-based solutions (C++, Java, Python) as we traverse the input array once to build the map and once more to calculate the sums. For the C solution, the complexity is O(n log n) because it sorts the elements before processing them in linear time.
- **Space Complexity:** O(n) since we need to store either a mapping of each unique value to its list of indices or an auxiliary array of structs/pairs of size n, in addition to the result array.
