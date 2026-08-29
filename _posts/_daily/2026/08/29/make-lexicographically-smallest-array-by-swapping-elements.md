---
layout: post
title: "Make Lexicographically Smallest Array by Swapping Elements"
date: 2026-08-29 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Union-Find", "Sorting"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> lexicographicallySmallestArray(vector<int>&\
        \ nums, int limit) {\n        int n = nums.size();\n        vector<pair<int,\
        \ int>> paired(n);\n        for (int i = 0; i < n; ++i) {\n            paired[i]\
        \ = {nums[i], i};\n        }\n        sort(paired.begin(), paired.end());\n\n\
        \        vector<int> result(n);\n        int i = 0;\n        while (i < n) {\n\
        \            int j = i + 1;\n            while (j < n && paired[j].first - paired[j\
        \ - 1].first <= limit) {\n                j++;\n            }\n            vector<int>\
        \ indices;\n            for (int k = i; k < j; ++k) {\n                indices.push_back(paired[k].second);\n\
        \            }\n            sort(indices.begin(), indices.end());\n        \
        \    for (int k = 0; k < indices.size(); ++k) {\n                result[indices[k]]\
        \ = paired[i + k].first;\n            }\n            i = j;\n        }\n   \
        \     return result;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public int[] lexicographicallySmallestArray(int[]\
        \ nums, int limit) {\n        int n = nums.length;\n        int[][] paired =\
        \ new int[n][2];\n        for (int i = 0; i < n; i++) {\n            paired[i][0]\
        \ = nums[i];\n            paired[i][1] = i;\n        }\n        Arrays.sort(paired,\
        \ (a, b) -> Integer.compare(a[0], b[0]));\n\n        int[] result = new int[n];\n\
        \        int i = 0;\n        while (i < n) {\n            int j = i + 1;\n \
        \           while (j < n && paired[j][0] - paired[j - 1][0] <= limit) {\n  \
        \              j++;\n            }\n            int[] indices = new int[j -\
        \ i];\n            for (int k = 0; k < j - i; k++) {\n                indices[k]\
        \ = paired[i + k][1];\n            }\n            Arrays.sort(indices);\n  \
        \          for (int k = 0; k < indices.length; k++) {\n                result[indices[k]]\
        \ = paired[i + k][0];\n            }\n            i = j;\n        }\n      \
        \  return result;\n    }\n}"
      python: "class Solution(object):\n    def lexicographicallySmallestArray(self,\
        \ nums, limit):\n        \"\"\"\n        :type nums: List[int]\n        :type\
        \ limit: int\n        :rtype: List[int]\n        \"\"\"\n        n = len(nums)\n\
        \        paired = sorted([(nums[i], i) for i in range(n)])\n\n        result\
        \ = [0] * n\n        i = 0\n        while i < n:\n            j = i + 1\n  \
        \          while j < n and paired[j][0] - paired[j - 1][0] <= limit:\n     \
        \           j += 1\n\n            indices = sorted([paired[k][1] for k in range(i,\
        \ j)])\n            for k in range(len(indices)):\n                result[indices[k]]\
        \ = paired[i + k][0]\n            i = j\n\n        return result"
      python3: "class Solution:\n    def lexicographicallySmallestArray(self, nums:\
        \ List[int], limit: int) -> List[int]:\n        n = len(nums)\n        paired\
        \ = sorted([(nums[i], i) for i in range(n)])\n\n        result = [0] * n\n \
        \       i = 0\n        while i < n:\n            j = i + 1\n            while\
        \ j < n and paired[j][0] - paired[j - 1][0] <= limit:\n                j +=\
        \ 1\n\n            indices = sorted([paired[k][1] for k in range(i, j)])\n \
        \           for k in range(len(indices)):\n                result[indices[k]]\
        \ = paired[i + k][0]\n            i = j\n\n        return result"
      c: "typedef struct {\n    int val;\n    int idx;\n} Pair;\n\nint comparePairs(const\
        \ void* a, const void* b) {\n    return ((Pair*)a)->val - ((Pair*)b)->val;\n\
        }\n\nint compareInts(const void* a, const void* b) {\n    return *(int*)a -\
        \ *(int*)b;\n}\n\nint* lexicographicallySmallestArray(int* nums, int numsSize,\
        \ int limit, int* returnSize) {\n    Pair* paired = (Pair*)malloc(numsSize *\
        \ sizeof(Pair));\n    for (int i = 0; i < numsSize; i++) {\n        paired[i].val\
        \ = nums[i];\n        paired[i].idx = i;\n    }\n    qsort(paired, numsSize,\
        \ sizeof(Pair), comparePairs);\n\n    int* result = (int*)malloc(numsSize *\
        \ sizeof(int));\n    int* indices = (int*)malloc(numsSize * sizeof(int));\n\
        \    *returnSize = numsSize;\n\n    int i = 0;\n    while (i < numsSize) {\n\
        \        int j = i + 1;\n        while (j < numsSize && (long long)paired[j].val\
        \ - paired[j - 1].val <= limit) {\n            j++;\n        }\n        int\
        \ groupSize = j - i;\n        for (int k = 0; k < groupSize; k++) {\n      \
        \      indices[k] = paired[i + k].idx;\n        }\n        qsort(indices, groupSize,\
        \ sizeof(int), compareInts);\n        for (int k = 0; k < groupSize; k++) {\n\
        \            result[indices[k]] = paired[i + k].val;\n        }\n        i =\
        \ j;\n    }\n\n    free(paired);\n    free(indices);\n    return result;\n}"
      csharp: "public class Solution {\n    public int[] LexicographicallySmallestArray(int[]\
        \ nums, int limit) {\n        int n = nums.Length;\n        int[] values = (int[])nums.Clone();\n\
        \        int[] indices = new int[n];\n        for (int i = 0; i < n; i++) {\n\
        \            indices[i] = i;\n        }\n        Array.Sort(values, indices);\n\
        \n        int[] res = new int[n];\n        int[] groupIdMap = new int[n];\n\
        \        int[] groupStarts = new int[n];\n        int groupCount = 0;\n\n  \
        \      groupIdMap[indices[0]] = 0;\n        groupStarts[0] = 0;\n\n        for\
        \ (int i = 1; i < n; i++) {\n            if (values[i] - values[i - 1] > limit)\
        \ {\n                groupCount++;\n                groupStarts[groupCount]\
        \ = i;\n            }\n            groupIdMap[indices[i]] = groupCount;\n  \
        \      }\n\n        for (int i = 0; i < n; i++) {\n            int gid = groupIdMap[i];\n\
        \            res[i] = values[groupStarts[gid]];\n            groupStarts[gid]++;\n\
        \        }\n\n        return res;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} limit\n * @return\
        \ {number[]}\n */\nvar lexicographicallySmallestArray = function(nums, limit)\
        \ {\n    const n = nums.length;\n    const pairs = new Array(n);\n    for (let\
        \ i = 0; i < n; i++) {\n        pairs[i] = { v: nums[i], i: i };\n    }\n  \
        \  pairs.sort((a, b) => a.v - b.v);\n\n    const groupIdMap = new Int32Array(n);\n\
        \    const groupStarts = new Int32Array(n);\n    let groupCount = 0;\n\n   \
        \ groupIdMap[pairs[0].i] = 0;\n    groupStarts[0] = 0;\n\n    for (let i = 1;\
        \ i < n; i++) {\n        if (pairs[i].v - pairs[i - 1].v > limit) {\n      \
        \      groupCount++;\n            groupStarts[groupCount] = i;\n        }\n\
        \        groupIdMap[pairs[i].i] = groupCount;\n    }\n\n    const res = new\
        \ Array(n);\n    for (let i = 0; i < n; i++) {\n        const gid = groupIdMap[i];\n\
        \        res[i] = pairs[groupStarts[gid]].v;\n        groupStarts[gid]++;\n\
        \    }\n\n    return res;\n};"
      typescript: "function lexicographicallySmallestArray(nums: number[], limit: number):\
        \ number[] {\n    const n = nums.length;\n    const pairs: { v: number; i: number\
        \ }[] = new Array(n);\n    for (let i = 0; i < n; i++) {\n        pairs[i] =\
        \ { v: nums[i], i: i };\n    }\n    pairs.sort((a, b) => a.v - b.v);\n\n   \
        \ const groupIdMap = new Int32Array(n);\n    const groupStarts = new Int32Array(n);\n\
        \    let groupCount = 0;\n\n    groupIdMap[pairs[0].i] = 0;\n    groupStarts[0]\
        \ = 0;\n\n    for (let i = 1; i < n; i++) {\n        if (pairs[i].v - pairs[i\
        \ - 1].v > limit) {\n            groupCount++;\n            groupStarts[groupCount]\
        \ = i;\n        }\n        groupIdMap[pairs[i].i] = groupCount;\n    }\n\n \
        \   const res: number[] = new Array(n);\n    for (let i = 0; i < n; i++) {\n\
        \        const gid = groupIdMap[i];\n        res[i] = pairs[groupStarts[gid]].v;\n\
        \        groupStarts[gid]++;\n    }\n\n    return res;\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer $limit\n     * @return Integer[]\n     */\n    function lexicographicallySmallestArray($nums,\
        \ $limit) {\n        $n = count($nums);\n        $indices = range(0, $n - 1);\n\
        \        $vals = $nums;\n        array_multisort($vals, SORT_ASC, $indices);\n\
        \n        $groupIdMap = array_fill(0, $n, 0);\n        $groupStarts = array_fill(0,\
        \ $n, 0);\n        $groupCount = 0;\n\n        $groupIdMap[$indices[0]] = 0;\n\
        \        $groupStarts[0] = 0;\n\n        for ($i = 1; $i < $n; $i++) {\n   \
        \         if ($vals[$i] - $vals[$i - 1] > $limit) {\n                $groupCount++;\n\
        \                $groupStarts[$groupCount] = $i;\n            }\n          \
        \  $groupIdMap[$indices[$i]] = $groupCount;\n        }\n\n        $res = array_fill(0,\
        \ $n, 0);\n        for ($i = 0; $i < $n; $i++) {\n            $gid = $groupIdMap[$i];\n\
        \            $res[$i] = $vals[$groupStarts[$gid]];\n            $groupStarts[$gid]++;\n\
        \        }\n\n        return $res;\n    }\n}"
      swift: "class Solution {\n    func lexicographicallySmallestArray(_ nums: [Int],\
        \ _ limit: Int) -> [Int] {\n        let n = nums.count\n        if n == 0 {\
        \ return [] }\n\n        var pairs = [(v: Int, i: Int)]()\n        pairs.reserveCapacity(n)\n\
        \        for i in 0..<n {\n            pairs.append((v: nums[i], i: i))\n  \
        \      }\n        pairs.sort { $0.v < $1.v }\n\n        var groupIdMap = [Int](repeating:\
        \ 0, count: n)\n        var groupStarts = [Int](repeating: 0, count: n)\n  \
        \      var groupCount = 0\n\n        groupIdMap[pairs[0].i] = 0\n        groupStarts[0]\
        \ = 0\n\n        if n > 1 {\n            for i in 1..<n {\n                if\
        \ pairs[i].v - pairs[i - 1].v > limit {\n                    groupCount += 1\n\
        \                    groupStarts[groupCount] = i\n                }\n      \
        \          groupIdMap[pairs[i].i] = groupCount\n            }\n        }\n\n\
        \        var res = [Int](repeating: 0, count: n)\n        for i in 0..<n {\n\
        \            let gid = groupIdMap[i]\n            res[i] = pairs[groupStarts[gid]].v\n\
        \            groupStarts[gid] += 1\n        }\n\n        return res\n    }\n\
        }"
      kotlin: "class Solution {\n    fun lexicographicallySmallestArray(nums: IntArray,\
        \ limit: Int): IntArray {\n        val n = nums.size\n        val sortedNums\
        \ = nums.clone()\n        sortedNums.sort()\n\n        val numToGroup = mutableMapOf<Int,\
        \ Int>()\n        val groups = mutableListOf<MutableList<Int>>()\n\n       \
        \ var groupIdx = 0\n        groups.add(mutableListOf(sortedNums[0]))\n     \
        \   numToGroup[sortedNums[0]] = groupIdx\n\n        for (i in 1 until n) {\n\
        \            if (sortedNums[i] - sortedNums[i - 1] > limit) {\n            \
        \    groupIdx++\n                groups.add(mutableListOf())\n            }\n\
        \            groups[groupIdx].add(sortedNums[i])\n            numToGroup[sortedNums[i]]\
        \ = groupIdx\n        }\n\n        val groupPointers = IntArray(groups.size)\
        \ { 0 }\n        val result = IntArray(n)\n        for (i in 0 until n) {\n\
        \            val gIdx = numToGroup[nums[i]]!!\n            result[i] = groups[gIdx][groupPointers[gIdx]++]\n\
        \        }\n\n        return result\n    }\n}"
      dart: "class Solution {\n  List<int> lexicographicallySmallestArray(List<int>\
        \ nums, int limit) {\n    int n = nums.length;\n    List<int> sortedNums = List.from(nums);\n\
        \    sortedNums.sort();\n\n    Map<int, int> numToGroup = {};\n    List<List<int>>\
        \ groups = [];\n\n    int groupIdx = 0;\n    groups.add([sortedNums[0]]);\n\
        \    numToGroup[sortedNums[0]] = groupIdx;\n\n    for (int i = 1; i < n; i++)\
        \ {\n      if (sortedNums[i] - sortedNums[i - 1] > limit) {\n        groupIdx++;\n\
        \        groups.add([]);\n      }\n      groups[groupIdx].add(sortedNums[i]);\n\
        \      numToGroup[sortedNums[i]] = groupIdx;\n    }\n\n    List<int> groupPointers\
        \ = List.filled(groups.length, 0);\n    List<int> result = List.filled(n, 0);\n\
        \    for (int i = 0; i < n; i++) {\n      int gIdx = numToGroup[nums[i]]!;\n\
        \      result[i] = groups[gIdx][groupPointers[gIdx]];\n      groupPointers[gIdx]++;\n\
        \    }\n\n    return result;\n  }\n}"
      go: "import (\n\t\"sort\"\n)\n\nfunc lexicographicallySmallestArray(nums []int,\
        \ limit int) []int {\n\tn := len(nums)\n\tif n == 0 {\n\t\treturn nums\n\t}\n\
        \n\tsortedNums := make([]int, n)\n\tcopy(sortedNums, nums)\n\tsort.Ints(sortedNums)\n\
        \n\tnumToGroup := make(map[int]int)\n\tgroups := [][]int{}\n\n\tgroupIdx :=\
        \ 0\n\tgroups = append(groups, []int{sortedNums[0]})\n\tnumToGroup[sortedNums[0]]\
        \ = groupIdx\n\n\tfor i := 1; i < n; i++ {\n\t\tif sortedNums[i]-sortedNums[i-1]\
        \ > limit {\n\t\t\tgroupIdx++\n\t\t\tgroups = append(groups, []int{})\n\t\t\
        }\n\t\tgroups[groupIdx] = append(groups[groupIdx], sortedNums[i])\n\t\tnumToGroup[sortedNums[i]]\
        \ = groupIdx\n\t}\n\n\tgroupPointers := make([]int, len(groups))\n\tresult :=\
        \ make([]int, n)\n\tfor i := 0; i < n; i++ {\n\t\tgIdx := numToGroup[nums[i]]\n\
        \t\tresult[i] = groups[gIdx][groupPointers[gIdx]]\n\t\tgroupPointers[gIdx]++\n\
        \t}\n\n\treturn result\n}"
      ruby: "def lexicographically_smallest_array(nums, limit)\n  n = nums.length\n\
        \  sorted_nums = nums.sort\n\n  num_to_group = {}\n  groups = []\n\n  group_idx\
        \ = 0\n  groups << [sorted_nums[0]]\n  num_to_group[sorted_nums[0]] = group_idx\n\
        \n  (1...n).each do |i|\n    if sorted_nums[i] - sorted_nums[i - 1] > limit\n\
        \      group_idx += 1\n      groups << []\n    end\n    groups[group_idx] <<\
        \ sorted_nums[i]\n    num_to_group[sorted_nums[i]] = group_idx\n  end\n\n  group_pointers\
        \ = Array.new(groups.length, 0)\n  result = Array.new(n, 0)\n\n  (0...n).each\
        \ do |i|\n    g_idx = num_to_group[nums[i]]\n    result[i] = groups[g_idx][group_pointers[g_idx]]\n\
        \    group_pointers[g_idx] += 1\n  end\n\n  result\nend"
      scala: "import scala.collection.mutable\nimport scala.util.Sorting\n\nobject Solution\
        \ {\n    def lexicographicallySmallestArray(nums: Array[Int], limit: Int): Array[Int]\
        \ = {\n        val n = nums.length\n        if (n == 0) return nums\n\n    \
        \    val sortedNums = nums.clone()\n        Sorting.quickSort(sortedNums)\n\n\
        \        val numToGroup = mutable.Map[Int, Int]()\n        val groups = mutable.ArrayBuffer[mutable.Queue[Int]]()\n\
        \n        var groupIdx = 0\n        groups += mutable.Queue(sortedNums(0))\n\
        \        numToGroup(sortedNums(0)) = groupIdx\n\n        for (i <- 1 until n)\
        \ {\n            if (sortedNums(i) - sortedNums(i - 1) > limit) {\n        \
        \        groupIdx += 1\n                groups += mutable.Queue[Int]()\n   \
        \         }\n            groups(groupIdx).enqueue(sortedNums(i))\n         \
        \   numToGroup(sortedNums(i)) = groupIdx\n        }\n\n        val result =\
        \ new Array[Int](n)\n        for (i <- 0 until n) {\n            val gIdx =\
        \ numToGroup(nums(i))\n            result(i) = groups(gIdx).dequeue()\n    \
        \    }\n\n        result\n    }\n}"
      rust: "impl Solution {\n    pub fn lexicographically_smallest_array(nums: Vec<i32>,\
        \ limit: i32) -> Vec<i32> {\n        let n = nums.len();\n        let mut pairs:\
        \ Vec<(i32, usize)> = nums.iter().enumerate().map(|(i, &v)| (v, i)).collect();\n\
        \        pairs.sort_unstable_by_key(|p| p.0);\n\n        let mut res = vec![0;\
        \ n];\n        let mut i = 0;\n        while i < n {\n            let mut j\
        \ = i + 1;\n            while j < n && pairs[j].0 - pairs[j - 1].0 <= limit\
        \ {\n                j += 1;\n            }\n\n            let mut component_indices:\
        \ Vec<usize> = (i..j).map(|k| pairs[k].1).collect();\n            component_indices.sort_unstable();\n\
        \n            for k in 0..(j - i) {\n                res[component_indices[k]]\
        \ = pairs[i + k].0;\n            }\n\n            i = j;\n        }\n      \
        \  res\n    }\n}"
      racket: "(define/contract (lexicographically-smallest-array nums limit)\n  (->\
        \ (listof exact-integer?) exact-integer? (listof exact-integer?))\n  (let* ([n\
        \ (length nums)]\n         [indices (build-list n (lambda (i) i))]\n       \
        \  [pairs (sort (map cons nums indices) < #:key car)]\n         [res (make-vector\
        \ n 0)])\n    (let loop ([remaining pairs])\n      (if (null? remaining)\n \
        \         (vector->list res)\n          (let-values ([(current-group rest)\n\
        \                        (let group-loop ([curr (list (car remaining))]\n  \
        \                                       [rem (cdr remaining)])\n           \
        \               (if (and (not (null? rem))\n                               \
        \    (<= (- (caar rem) (caar curr)) limit))\n                              (group-loop\
        \ (cons (car rem) curr) (cdr rem))\n                              (values (reverse\
        \ curr) rem)))])\n            (let* ([g-indices (sort (map cdr current-group)\
        \ <)]\n                   [g-vals (map car current-group)])\n              (for-each\
        \ (lambda (idx val) (vector-set! res idx val)) g-indices g-vals)\n         \
        \     (loop rest)))))))"
      erlang: "-spec lexicographically_smallest_array(Nums :: [integer()], Limit ::\
        \ integer()) -> [integer()].\nlexicographically_smallest_array(Nums, Limit)\
        \ ->\n    N = length(Nums),\n    Indices = lists:seq(0, N - 1),\n    Pairs =\
        \ lists:keysort(1, lists:zip(Nums, Indices)),\n    Groups = group_pairs(Pairs,\
        \ Limit, []),\n    FlatList = lists:flatmap(fun(Group) ->\n        {Vals, Idxs}\
        \ = lists:unzip(Group),\n        SortedIdxs = lists:sort(Idxs),\n        lists:zip(SortedIdxs,\
        \ Vals)\n    end, Groups),\n    SortedFlatList = lists:keysort(1, FlatList),\n\
        \    [V || {_, V} <- SortedFlatList].\n\ngroup_pairs([], _Limit, Acc) -> lists:reverse(Acc);\n\
        group_pairs([H | T], Limit, Acc) ->\n    {Group, Rest} = take_group([H], T,\
        \ Limit),\n    group_pairs(Rest, Limit, [lists:reverse(Group) | Acc]).\n\ntake_group(Group,\
        \ [], _Limit) -> {Group, []};\ntake_group([Last | _] = Group, [Next | Rest],\
        \ Limit) ->\n    {ValLast, _} = Last,\n    {ValNext, _} = Next,\n    if\n  \
        \      ValNext - ValLast =< Limit -> take_group([Next | Group], Rest, Limit);\n\
        \        true -> {Group, [Next | Rest]}\n    end."
      elixir: "defmodule Solution do\n  @spec lexicographically_smallest_array(nums\
        \ :: [integer], limit :: integer) :: [integer]\n  def lexicographically_smallest_array(nums,\
        \ limit) do\n    nums\n    |> Enum.with_index()\n    |> Enum.sort_by(fn {val,\
        \ _idx} -> val end)\n    |> Enum.chunk_while(\n      [],\n      fn\n       \
        \ {val, idx}, [] ->\n          {:cont, [{val, idx}]}\n\n        {val, idx},\
        \ [{prev_val, _} | _] = acc ->\n          if val - prev_val <= limit do\n  \
        \          {:cont, [{val, idx} | acc]}\n          else\n            {:chunk,\
        \ Enum.reverse(acc), [{val, idx}]}\n          end\n      end,\n      fn\n  \
        \      [] -> {:cont, []}\n        acc -> {:cont, Enum.reverse(acc), []}\n  \
        \    end\n    )\n    |> Enum.flat_map(fn group ->\n      {vals, idxs} = Enum.unzip(group)\n\
        \      sorted_idxs = Enum.sort(idxs)\n      Enum.zip(sorted_idxs, vals)\n  \
        \  end)\n    |> Enum.sort_by(fn {idx, _val} -> idx end)\n    |> Enum.map(fn\
        \ {_idx, val} -> val end)\n  end\nend"
    approach: The problem can be modeled as finding connected components in a graph
      where nodes are array indices and an edge exists between $i$ and $j$ if $abs(nums[i]
      - nums[j]) \le limit$. Due to the transitive property of swaps, if index $i$ can
      be swapped with $j$, and $j$ with $k$, then $i$ can effectively be swapped with
      $k$. To find these components efficiently, we sort the elements of the array while
      keeping track of their original indices. In the sorted sequence, if the difference
      between two consecutive elements is within the limit, they belong to the same
      connected component. Otherwise, a new component starts.
    time_complexity: O(N log N) where N is the length of the array. This complexity
      arises from sorting the elements and their original indices. Identifying components
      and placing values back into the result array takes O(N) time because each element
      is processed a constant number of times.
    space_complexity: O(N) where N is the length of the array. This space is required
      to store the sorted version of the input array, the mapping of elements to components,
      and the resulting groups of indices and values.
    elapsed_time: 215.78792905807495
    model: gemini-3-flash-preview
    generated_at: '2026-08-29 05:03:34 '
---

## Problem #2948: Make Lexicographically Smallest Array by Swapping Elements

**Difficulty:** Medium

**Topics:** Array, Union-Find, Sorting

## Problem Description

<p>You are given a <strong>0-indexed</strong> array of <strong>positive</strong> integers <code>nums</code> and a <strong>positive</strong> integer <code>limit</code>.</p>

<p>In one operation, you can choose any two indices <code>i</code> and <code>j</code> and swap <code>nums[i]</code> and <code>nums[j]</code> <strong>if</strong> <code>|nums[i] - nums[j]| &lt;= limit</code>.</p>

<p>Return <em>the <strong>lexicographically smallest array</strong> that can be obtained by performing the operation any number of times</em>.</p>

<p>An array <code>a</code> is lexicographically smaller than an array <code>b</code> if in the first position where <code>a</code> and <code>b</code> differ, array <code>a</code> has an element that is less than the corresponding element in <code>b</code>. For example, the array <code>[2,10,3]</code> is lexicographically smaller than the array <code>[10,2,3]</code> because they differ at index <code>0</code> and <code>2 &lt; 10</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,5,3,9,8], limit = 2
<strong>Output:</strong> [1,3,5,8,9]
<strong>Explanation:</strong> Apply the operation 2 times:
- Swap nums[1] with nums[2]. The array becomes [1,3,5,9,8]
- Swap nums[3] with nums[4]. The array becomes [1,3,5,8,9]
We cannot obtain a lexicographically smaller array by applying any more operations.
Note that it may be possible to get the same result by doing different operations.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,7,6,18,2,1], limit = 3
<strong>Output:</strong> [1,6,7,18,1,2]
<strong>Explanation:</strong> Apply the operation 3 times:
- Swap nums[1] with nums[2]. The array becomes [1,6,7,18,2,1]
- Swap nums[0] with nums[4]. The array becomes [2,6,7,18,1,1]
- Swap nums[0] with nums[5]. The array becomes [1,6,7,18,1,2]
We cannot obtain a lexicographically smaller array by applying any more operations.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,7,28,19,10], limit = 3
<strong>Output:</strong> [1,7,28,19,10]
<strong>Explanation:</strong> [1,7,28,19,10] is the lexicographically smallest array we can obtain because we cannot apply the operation on any two indices.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= limit &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. Construct a virtual graph where all elements in `nums` are nodes and the pairs satisfying the condition have an edge between them.

2. Instead of constructing all edges, we only care about the connected components.

3. Can we use DSU?

4. Sort `nums`. Now we just need to consider if the consecutive elements have an edge to check if they belong to the same connected component. Hence, all connected components become a list of position-consecutive elements after sorting.

5. For each index of `nums` from `0` to `nums.length - 1` we can change it to the current minimum value we have in its connected component and remove that value from the connected component.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be modeled as finding connected components in a graph where nodes are array indices and an edge exists between $i$ and $j$ if $abs(nums[i] - nums[j]) \le limit$. Due to the transitive property of swaps, if index $i$ can be swapped with $j$, and $j$ with $k$, then $i$ can effectively be swapped with $k$. To find these components efficiently, we sort the elements of the array while keeping track of their original indices. In the sorted sequence, if the difference between two consecutive elements is within the limit, they belong to the same connected component. Otherwise, a new component starts.

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
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        int n = nums.size();
        vector<pair<int, int>> paired(n);
        for (int i = 0; i < n; ++i) {
            paired[i] = {nums[i], i};
        }
        sort(paired.begin(), paired.end());

        vector<int> result(n);
        int i = 0;
        while (i < n) {
            int j = i + 1;
            while (j < n && paired[j].first - paired[j - 1].first <= limit) {
                j++;
            }
            vector<int> indices;
            for (int k = i; k < j; ++k) {
                indices.push_back(paired[k].second);
            }
            sort(indices.begin(), indices.end());
            for (int k = 0; k < indices.size(); ++k) {
                result[indices[k]] = paired[i + k].first;
            }
            i = j;
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
import java.util.*;

class Solution {
    public int[] lexicographicallySmallestArray(int[] nums, int limit) {
        int n = nums.length;
        int[][] paired = new int[n][2];
        for (int i = 0; i < n; i++) {
            paired[i][0] = nums[i];
            paired[i][1] = i;
        }
        Arrays.sort(paired, (a, b) -> Integer.compare(a[0], b[0]));

        int[] result = new int[n];
        int i = 0;
        while (i < n) {
            int j = i + 1;
            while (j < n && paired[j][0] - paired[j - 1][0] <= limit) {
                j++;
            }
            int[] indices = new int[j - i];
            for (int k = 0; k < j - i; k++) {
                indices[k] = paired[i + k][1];
            }
            Arrays.sort(indices);
            for (int k = 0; k < indices.length; k++) {
                result[indices[k]] = paired[i + k][0];
            }
            i = j;
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
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        n = len(nums)
        paired = sorted([(nums[i], i) for i in range(n)])

        result = [0] * n
        i = 0
        while i < n:
            j = i + 1
            while j < n and paired[j][0] - paired[j - 1][0] <= limit:
                j += 1

            indices = sorted([paired[k][1] for k in range(i, j)])
            for k in range(len(indices)):
                result[indices[k]] = paired[i + k][0]
            i = j

        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        paired = sorted([(nums[i], i) for i in range(n)])

        result = [0] * n
        i = 0
        while i < n:
            j = i + 1
            while j < n and paired[j][0] - paired[j - 1][0] <= limit:
                j += 1

            indices = sorted([paired[k][1] for k in range(i, j)])
            for k in range(len(indices)):
                result[indices[k]] = paired[i + k][0]
            i = j

        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
typedef struct {
    int val;
    int idx;
} Pair;

int comparePairs(const void* a, const void* b) {
    return ((Pair*)a)->val - ((Pair*)b)->val;
}

int compareInts(const void* a, const void* b) {
    return *(int*)a - *(int*)b;
}

int* lexicographicallySmallestArray(int* nums, int numsSize, int limit, int* returnSize) {
    Pair* paired = (Pair*)malloc(numsSize * sizeof(Pair));
    for (int i = 0; i < numsSize; i++) {
        paired[i].val = nums[i];
        paired[i].idx = i;
    }
    qsort(paired, numsSize, sizeof(Pair), comparePairs);

    int* result = (int*)malloc(numsSize * sizeof(int));
    int* indices = (int*)malloc(numsSize * sizeof(int));
    *returnSize = numsSize;

    int i = 0;
    while (i < numsSize) {
        int j = i + 1;
        while (j < numsSize && (long long)paired[j].val - paired[j - 1].val <= limit) {
            j++;
        }
        int groupSize = j - i;
        for (int k = 0; k < groupSize; k++) {
            indices[k] = paired[i + k].idx;
        }
        qsort(indices, groupSize, sizeof(int), compareInts);
        for (int k = 0; k < groupSize; k++) {
            result[indices[k]] = paired[i + k].val;
        }
        i = j;
    }

    free(paired);
    free(indices);
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int[] LexicographicallySmallestArray(int[] nums, int limit) {
        int n = nums.Length;
        int[] values = (int[])nums.Clone();
        int[] indices = new int[n];
        for (int i = 0; i < n; i++) {
            indices[i] = i;
        }
        Array.Sort(values, indices);

        int[] res = new int[n];
        int[] groupIdMap = new int[n];
        int[] groupStarts = new int[n];
        int groupCount = 0;

        groupIdMap[indices[0]] = 0;
        groupStarts[0] = 0;

        for (int i = 1; i < n; i++) {
            if (values[i] - values[i - 1] > limit) {
                groupCount++;
                groupStarts[groupCount] = i;
            }
            groupIdMap[indices[i]] = groupCount;
        }

        for (int i = 0; i < n; i++) {
            int gid = groupIdMap[i];
            res[i] = values[groupStarts[gid]];
            groupStarts[gid]++;
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
 * @param {number} limit
 * @return {number[]}
 */
var lexicographicallySmallestArray = function(nums, limit) {
    const n = nums.length;
    const pairs = new Array(n);
    for (let i = 0; i < n; i++) {
        pairs[i] = { v: nums[i], i: i };
    }
    pairs.sort((a, b) => a.v - b.v);

    const groupIdMap = new Int32Array(n);
    const groupStarts = new Int32Array(n);
    let groupCount = 0;

    groupIdMap[pairs[0].i] = 0;
    groupStarts[0] = 0;

    for (let i = 1; i < n; i++) {
        if (pairs[i].v - pairs[i - 1].v > limit) {
            groupCount++;
            groupStarts[groupCount] = i;
        }
        groupIdMap[pairs[i].i] = groupCount;
    }

    const res = new Array(n);
    for (let i = 0; i < n; i++) {
        const gid = groupIdMap[i];
        res[i] = pairs[groupStarts[gid]].v;
        groupStarts[gid]++;
    }

    return res;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function lexicographicallySmallestArray(nums: number[], limit: number): number[] {
    const n = nums.length;
    const pairs: { v: number; i: number }[] = new Array(n);
    for (let i = 0; i < n; i++) {
        pairs[i] = { v: nums[i], i: i };
    }
    pairs.sort((a, b) => a.v - b.v);

    const groupIdMap = new Int32Array(n);
    const groupStarts = new Int32Array(n);
    let groupCount = 0;

    groupIdMap[pairs[0].i] = 0;
    groupStarts[0] = 0;

    for (let i = 1; i < n; i++) {
        if (pairs[i].v - pairs[i - 1].v > limit) {
            groupCount++;
            groupStarts[groupCount] = i;
        }
        groupIdMap[pairs[i].i] = groupCount;
    }

    const res: number[] = new Array(n);
    for (let i = 0; i < n; i++) {
        const gid = groupIdMap[i];
        res[i] = pairs[groupStarts[gid]].v;
        groupStarts[gid]++;
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
     * @param Integer $limit
     * @return Integer[]
     */
    function lexicographicallySmallestArray($nums, $limit) {
        $n = count($nums);
        $indices = range(0, $n - 1);
        $vals = $nums;
        array_multisort($vals, SORT_ASC, $indices);

        $groupIdMap = array_fill(0, $n, 0);
        $groupStarts = array_fill(0, $n, 0);
        $groupCount = 0;

        $groupIdMap[$indices[0]] = 0;
        $groupStarts[0] = 0;

        for ($i = 1; $i < $n; $i++) {
            if ($vals[$i] - $vals[$i - 1] > $limit) {
                $groupCount++;
                $groupStarts[$groupCount] = $i;
            }
            $groupIdMap[$indices[$i]] = $groupCount;
        }

        $res = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $gid = $groupIdMap[$i];
            $res[$i] = $vals[$groupStarts[$gid]];
            $groupStarts[$gid]++;
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
    func lexicographicallySmallestArray(_ nums: [Int], _ limit: Int) -> [Int] {
        let n = nums.count
        if n == 0 { return [] }

        var pairs = [(v: Int, i: Int)]()
        pairs.reserveCapacity(n)
        for i in 0..<n {
            pairs.append((v: nums[i], i: i))
        }
        pairs.sort { $0.v < $1.v }

        var groupIdMap = [Int](repeating: 0, count: n)
        var groupStarts = [Int](repeating: 0, count: n)
        var groupCount = 0

        groupIdMap[pairs[0].i] = 0
        groupStarts[0] = 0

        if n > 1 {
            for i in 1..<n {
                if pairs[i].v - pairs[i - 1].v > limit {
                    groupCount += 1
                    groupStarts[groupCount] = i
                }
                groupIdMap[pairs[i].i] = groupCount
            }
        }

        var res = [Int](repeating: 0, count: n)
        for i in 0..<n {
            let gid = groupIdMap[i]
            res[i] = pairs[groupStarts[gid]].v
            groupStarts[gid] += 1
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
    fun lexicographicallySmallestArray(nums: IntArray, limit: Int): IntArray {
        val n = nums.size
        val sortedNums = nums.clone()
        sortedNums.sort()

        val numToGroup = mutableMapOf<Int, Int>()
        val groups = mutableListOf<MutableList<Int>>()

        var groupIdx = 0
        groups.add(mutableListOf(sortedNums[0]))
        numToGroup[sortedNums[0]] = groupIdx

        for (i in 1 until n) {
            if (sortedNums[i] - sortedNums[i - 1] > limit) {
                groupIdx++
                groups.add(mutableListOf())
            }
            groups[groupIdx].add(sortedNums[i])
            numToGroup[sortedNums[i]] = groupIdx
        }

        val groupPointers = IntArray(groups.size) { 0 }
        val result = IntArray(n)
        for (i in 0 until n) {
            val gIdx = numToGroup[nums[i]]!!
            result[i] = groups[gIdx][groupPointers[gIdx]++]
        }

        return result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<int> lexicographicallySmallestArray(List<int> nums, int limit) {
    int n = nums.length;
    List<int> sortedNums = List.from(nums);
    sortedNums.sort();

    Map<int, int> numToGroup = {};
    List<List<int>> groups = [];

    int groupIdx = 0;
    groups.add([sortedNums[0]]);
    numToGroup[sortedNums[0]] = groupIdx;

    for (int i = 1; i < n; i++) {
      if (sortedNums[i] - sortedNums[i - 1] > limit) {
        groupIdx++;
        groups.add([]);
      }
      groups[groupIdx].add(sortedNums[i]);
      numToGroup[sortedNums[i]] = groupIdx;
    }

    List<int> groupPointers = List.filled(groups.length, 0);
    List<int> result = List.filled(n, 0);
    for (int i = 0; i < n; i++) {
      int gIdx = numToGroup[nums[i]]!;
      result[i] = groups[gIdx][groupPointers[gIdx]];
      groupPointers[gIdx]++;
    }

    return result;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import (
	"sort"
)

func lexicographicallySmallestArray(nums []int, limit int) []int {
	n := len(nums)
	if n == 0 {
		return nums
	}

	sortedNums := make([]int, n)
	copy(sortedNums, nums)
	sort.Ints(sortedNums)

	numToGroup := make(map[int]int)
	groups := [][]int{}

	groupIdx := 0
	groups = append(groups, []int{sortedNums[0]})
	numToGroup[sortedNums[0]] = groupIdx

	for i := 1; i < n; i++ {
		if sortedNums[i]-sortedNums[i-1] > limit {
			groupIdx++
			groups = append(groups, []int{})
		}
		groups[groupIdx] = append(groups[groupIdx], sortedNums[i])
		numToGroup[sortedNums[i]] = groupIdx
	}

	groupPointers := make([]int, len(groups))
	result := make([]int, n)
	for i := 0; i < n; i++ {
		gIdx := numToGroup[nums[i]]
		result[i] = groups[gIdx][groupPointers[gIdx]]
		groupPointers[gIdx]++
	}

	return result
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def lexicographically_smallest_array(nums, limit)
  n = nums.length
  sorted_nums = nums.sort

  num_to_group = {}
  groups = []

  group_idx = 0
  groups << [sorted_nums[0]]
  num_to_group[sorted_nums[0]] = group_idx

  (1...n).each do |i|
    if sorted_nums[i] - sorted_nums[i - 1] > limit
      group_idx += 1
      groups << []
    end
    groups[group_idx] << sorted_nums[i]
    num_to_group[sorted_nums[i]] = group_idx
  end

  group_pointers = Array.new(groups.length, 0)
  result = Array.new(n, 0)

  (0...n).each do |i|
    g_idx = num_to_group[nums[i]]
    result[i] = groups[g_idx][group_pointers[g_idx]]
    group_pointers[g_idx] += 1
  end

  result
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable
import scala.util.Sorting

object Solution {
    def lexicographicallySmallestArray(nums: Array[Int], limit: Int): Array[Int] = {
        val n = nums.length
        if (n == 0) return nums

        val sortedNums = nums.clone()
        Sorting.quickSort(sortedNums)

        val numToGroup = mutable.Map[Int, Int]()
        val groups = mutable.ArrayBuffer[mutable.Queue[Int]]()

        var groupIdx = 0
        groups += mutable.Queue(sortedNums(0))
        numToGroup(sortedNums(0)) = groupIdx

        for (i <- 1 until n) {
            if (sortedNums(i) - sortedNums(i - 1) > limit) {
                groupIdx += 1
                groups += mutable.Queue[Int]()
            }
            groups(groupIdx).enqueue(sortedNums(i))
            numToGroup(sortedNums(i)) = groupIdx
        }

        val result = new Array[Int](n)
        for (i <- 0 until n) {
            val gIdx = numToGroup(nums(i))
            result(i) = groups(gIdx).dequeue()
        }

        result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn lexicographically_smallest_array(nums: Vec<i32>, limit: i32) -> Vec<i32> {
        let n = nums.len();
        let mut pairs: Vec<(i32, usize)> = nums.iter().enumerate().map(|(i, &v)| (v, i)).collect();
        pairs.sort_unstable_by_key(|p| p.0);

        let mut res = vec![0; n];
        let mut i = 0;
        while i < n {
            let mut j = i + 1;
            while j < n && pairs[j].0 - pairs[j - 1].0 <= limit {
                j += 1;
            }

            let mut component_indices: Vec<usize> = (i..j).map(|k| pairs[k].1).collect();
            component_indices.sort_unstable();

            for k in 0..(j - i) {
                res[component_indices[k]] = pairs[i + k].0;
            }

            i = j;
        }
        res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (lexicographically-smallest-array nums limit)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (let* ([n (length nums)]
         [indices (build-list n (lambda (i) i))]
         [pairs (sort (map cons nums indices) < #:key car)]
         [res (make-vector n 0)])
    (let loop ([remaining pairs])
      (if (null? remaining)
          (vector->list res)
          (let-values ([(current-group rest)
                        (let group-loop ([curr (list (car remaining))]
                                         [rem (cdr remaining)])
                          (if (and (not (null? rem))
                                   (<= (- (caar rem) (caar curr)) limit))
                              (group-loop (cons (car rem) curr) (cdr rem))
                              (values (reverse curr) rem)))])
            (let* ([g-indices (sort (map cdr current-group) <)]
                   [g-vals (map car current-group)])
              (for-each (lambda (idx val) (vector-set! res idx val)) g-indices g-vals)
              (loop rest)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec lexicographically_smallest_array(Nums :: [integer()], Limit :: integer()) -> [integer()].
lexicographically_smallest_array(Nums, Limit) ->
    N = length(Nums),
    Indices = lists:seq(0, N - 1),
    Pairs = lists:keysort(1, lists:zip(Nums, Indices)),
    Groups = group_pairs(Pairs, Limit, []),
    FlatList = lists:flatmap(fun(Group) ->
        {Vals, Idxs} = lists:unzip(Group),
        SortedIdxs = lists:sort(Idxs),
        lists:zip(SortedIdxs, Vals)
    end, Groups),
    SortedFlatList = lists:keysort(1, FlatList),
    [V || {_, V} <- SortedFlatList].

group_pairs([], _Limit, Acc) -> lists:reverse(Acc);
group_pairs([H | T], Limit, Acc) ->
    {Group, Rest} = take_group([H], T, Limit),
    group_pairs(Rest, Limit, [lists:reverse(Group) | Acc]).

take_group(Group, [], _Limit) -> {Group, []};
take_group([Last | _] = Group, [Next | Rest], Limit) ->
    {ValLast, _} = Last,
    {ValNext, _} = Next,
    if
        ValNext - ValLast =< Limit -> take_group([Next | Group], Rest, Limit);
        true -> {Group, [Next | Rest]}
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec lexicographically_smallest_array(nums :: [integer], limit :: integer) :: [integer]
  def lexicographically_smallest_array(nums, limit) do
    nums
    |> Enum.with_index()
    |> Enum.sort_by(fn {val, _idx} -> val end)
    |> Enum.chunk_while(
      [],
      fn
        {val, idx}, [] ->
          {:cont, [{val, idx}]}

        {val, idx}, [{prev_val, _} | _] = acc ->
          if val - prev_val <= limit do
            {:cont, [{val, idx} | acc]}
          else
            {:chunk, Enum.reverse(acc), [{val, idx}]}
          end
      end,
      fn
        [] -> {:cont, []}
        acc -> {:cont, Enum.reverse(acc), []}
      end
    )
    |> Enum.flat_map(fn group ->
      {vals, idxs} = Enum.unzip(group)
      sorted_idxs = Enum.sort(idxs)
      Enum.zip(sorted_idxs, vals)
    end)
    |> Enum.sort_by(fn {idx, _val} -> idx end)
    |> Enum.map(fn {_idx, val} -> val end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N log N) where N is the length of the array. This complexity arises from sorting the elements and their original indices. Identifying components and placing values back into the result array takes O(N) time because each element is processed a constant number of times.
- **Space Complexity:** O(N) where N is the length of the array. This space is required to store the sorted version of the input array, the mapping of elements to components, and the resulting groups of indices and values.
