---
layout: post
title: "Closest Equal Element Queries"
date: 2026-04-16 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Binary Search"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/closest-equal-element-queries/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> solveQueries(vector<int>& nums,\
        \ vector<int>& queries) {\n        int n = nums.size();\n        std::unordered_map<int,\
        \ std::vector<int>> posMap;\n        for (int i = 0; i < n; ++i) {\n       \
        \     posMap[nums[i]].push_back(i);\n        }\n\n        std::vector<int> results;\n\
        \        results.reserve(queries.size());\n\n        for (int qIdx : queries)\
        \ {\n            int target = nums[qIdx];\n            const std::vector<int>&\
        \ indices = posMap[target];\n            int k = indices.size();\n\n       \
        \     if (k == 1) {\n                results.push_back(-1);\n              \
        \  continue;\n            }\n\n            auto it = std::lower_bound(indices.begin(),\
        \ indices.end(), qIdx);\n            int pos = std::distance(indices.begin(),\
        \ it);\n\n            int prevIdx = indices[(pos - 1 + k) % k];\n          \
        \  int nextIdx = indices[(pos + 1) % k];\n\n            auto getDist = [&](int\
        \ i, int j) {\n                int d = std::abs(i - j);\n                return\
        \ std::min(d, n - d);\n            };\n\n            results.push_back(std::min(getDist(qIdx,\
        \ prevIdx), getDist(qIdx, nextIdx)));\n        }\n\n        return results;\n\
        \    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public List<Integer> solveQueries(int[]\
        \ nums, int[] queries) {\n        int n = nums.length;\n        Map<Integer,\
        \ List<Integer>> posMap = new HashMap<>();\n        for (int i = 0; i < n; i++)\
        \ {\n            posMap.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);\n\
        \        }\n\n        List<Integer> result = new ArrayList<>(queries.length);\n\
        \        for (int qIdx : queries) {\n            int target = nums[qIdx];\n\
        \            List<Integer> indices = posMap.get(target);\n            int k\
        \ = indices.size();\n\n            if (k == 1) {\n                result.add(-1);\n\
        \                continue;\n            }\n\n            int pos = Collections.binarySearch(indices,\
        \ qIdx);\n            int prevIdx = indices.get((pos - 1 + k) % k);\n      \
        \      int nextIdx = indices.get((pos + 1) % k);\n\n            int d1 = Math.abs(qIdx\
        \ - prevIdx);\n            int d2 = Math.abs(qIdx - nextIdx);\n            int\
        \ dist1 = Math.min(d1, n - d1);\n            int dist2 = Math.min(d2, n - d2);\n\
        \n            result.add(Math.min(dist1, dist2));\n        }\n\n        return\
        \ result;\n    }\n}"
      python: "from collections import defaultdict\nfrom bisect import bisect_left\n\
        \nclass Solution(object):\n    def solveQueries(self, nums, queries):\n    \
        \    \"\"\"\n        :type nums: List[int]\n        :type queries: List[int]\n\
        \        :rtype: List[int]\n        \"\"\"\n        n = len(nums)\n        pos_map\
        \ = defaultdict(list)\n        for i, val in enumerate(nums):\n            pos_map[val].append(i)\n\
        \n        ans = []\n        for q_idx in queries:\n            val = nums[q_idx]\n\
        \            indices = pos_map[val]\n            k = len(indices)\n        \
        \    if k == 1:\n                ans.append(-1)\n                continue\n\n\
        \            pos = bisect_left(indices, q_idx)\n            prev_idx = indices[(pos\
        \ - 1 + k) % k]\n            next_idx = indices[(pos + 1) % k]\n\n         \
        \   d1 = abs(q_idx - prev_idx)\n            dist1 = min(d1, n - d1)\n      \
        \      d2 = abs(q_idx - next_idx)\n            dist2 = min(d2, n - d2)\n   \
        \         ans.append(min(dist1, dist2))\n        return ans"
      python3: "from collections import defaultdict\nfrom bisect import bisect_left\n\
        from typing import List\n\nclass Solution:\n    def solveQueries(self, nums:\
        \ List[int], queries: List[int]) -> List[int]:\n        n = len(nums)\n    \
        \    pos_map = defaultdict(list)\n        for i, val in enumerate(nums):\n \
        \           pos_map[val].append(i)\n\n        ans = []\n        for q_idx in\
        \ queries:\n            val = nums[q_idx]\n            indices = pos_map[val]\n\
        \            k = len(indices)\n            if k == 1:\n                ans.append(-1)\n\
        \                continue\n\n            pos = bisect_left(indices, q_idx)\n\
        \            prev_idx = indices[(pos - 1 + k) % k]\n            next_idx = indices[(pos\
        \ + 1) % k]\n\n            d1 = abs(q_idx - prev_idx)\n            dist1 = min(d1,\
        \ n - d1)\n            d2 = abs(q_idx - next_idx)\n            dist2 = min(d2,\
        \ n - d2)\n            ans.append(min(dist1, dist2))\n        return ans"
      c: "#include <stdlib.h>\n#include <stdio.h>\n\ntypedef struct {\n    int val;\n\
        \    int idx;\n} Entry;\n\nint cmp(const void* a, const void* b) {\n    Entry*\
        \ e1 = (Entry*)a;\n    Entry* e2 = (Entry*)b;\n    if (e1->val != e2->val) return\
        \ e1->val - e2->val;\n    return e1->idx - e2->idx;\n}\n\nint get_circular_dist(int\
        \ i, int j, int n) {\n    int d = abs(i - j);\n    int d2 = n - d;\n    return\
        \ (d < d2) ? d : d2;\n}\n\n/**\n * Note: The returned array must be malloced,\
        \ assume caller calls free().\n */\nint* solveQueries(int* nums, int numsSize,\
        \ int* queries, int queriesSize, int* returnSize) {\n    Entry* entries = (Entry*)malloc(numsSize\
        \ * sizeof(Entry));\n    for (int i = 0; i < numsSize; i++) {\n        entries[i].val\
        \ = nums[i];\n        entries[i].idx = i;\n    }\n    qsort(entries, numsSize,\
        \ sizeof(Entry), cmp);\n\n    int* result = (int*)malloc(queriesSize * sizeof(int));\n\
        \    *returnSize = queriesSize;\n\n    for (int i = 0; i < queriesSize; i++)\
        \ {\n        int qIdx = queries[i];\n        int target = nums[qIdx];\n\n  \
        \      int first = -1, last = -1;\n        int l = 0, r = numsSize - 1;\n  \
        \      while (l <= r) {\n            int mid = l + (r - l) / 2;\n          \
        \  if (entries[mid].val >= target) {\n                if (entries[mid].val ==\
        \ target) first = mid;\n                r = mid - 1;\n            } else l =\
        \ mid + 1;\n        }\n\n        l = 0, r = numsSize - 1;\n        while (l\
        \ <= r) {\n            int mid = l + (r - l) / 2;\n            if (entries[mid].val\
        \ <= target) {\n                if (entries[mid].val == target) last = mid;\n\
        \                l = mid + 1;\n            } else r = mid - 1;\n        }\n\n\
        \        if (first == -1 || first == last) {\n            result[i] = -1;\n\
        \            continue;\n        }\n\n        int pos = -1;\n        l = first,\
        \ r = last;\n        while (l <= r) {\n            int mid = l + (r - l) / 2;\n\
        \            if (entries[mid].idx == qIdx) {\n                pos = mid;\n \
        \               break;\n            }\n            if (entries[mid].idx < qIdx)\
        \ l = mid + 1;\n            else r = mid - 1;\n        }\n\n        int K =\
        \ last - first + 1;\n        int relPos = pos - first;\n        int idxPrev\
        \ = entries[first + (relPos - 1 + K) % K].idx;\n        int idxNext = entries[first\
        \ + (relPos + 1) % K].idx;\n\n        int d1 = get_circular_dist(qIdx, idxPrev,\
        \ numsSize);\n        int d2 = get_circular_dist(qIdx, idxNext, numsSize);\n\
        \        result[i] = (d1 < d2) ? d1 : d2;\n    }\n\n    free(entries);\n   \
        \ return result;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public IList<int> SolveQueries(int[] nums, int[] queries) {\n     \
        \   int n = nums.Length;\n        Dictionary<int, List<int>> posMap = new Dictionary<int,\
        \ List<int>>();\n        for (int i = 0; i < n; i++) {\n            if (!posMap.ContainsKey(nums[i]))\
        \ {\n                posMap[nums[i]] = new List<int>();\n            }\n   \
        \         posMap[nums[i]].Add(i);\n        }\n\n        int[] ansPerIndex =\
        \ new int[n];\n        foreach (var kvp in posMap) {\n            List<int>\
        \ indices = kvp.Value;\n            int k = indices.Count;\n            if (k\
        \ == 1) {\n                ansPerIndex[indices[0]] = -1;\n            } else\
        \ {\n                for (int p = 0; p < k; p++) {\n                    int\
        \ curr = indices[p];\n                    int prev = indices[(p - 1 + k) % k];\n\
        \                    int next = indices[(p + 1) % k];\n                    int\
        \ d_prev = (curr - prev + n) % n;\n                    int d_next = (next -\
        \ curr + n) % n;\n                    ansPerIndex[curr] = Math.Min(d_prev, d_next);\n\
        \                }\n            }\n        }\n\n        int[] result = new int[queries.Length];\n\
        \        for (int i = 0; i < queries.Length; i++) {\n            result[i] =\
        \ ansPerIndex[queries[i]];\n        }\n        return result;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number[]} queries\n *\
        \ @return {number[]}\n */\nvar solveQueries = function(nums, queries) {\n  \
        \  const n = nums.length;\n    const posMap = new Map();\n    for (let i = 0;\
        \ i < n; i++) {\n        if (!posMap.has(nums[i])) {\n            posMap.set(nums[i],\
        \ []);\n        }\n        posMap.get(nums[i]).push(i);\n    }\n\n    const\
        \ ansPerIndex = new Int32Array(n);\n    for (const indices of posMap.values())\
        \ {\n        const k = indices.length;\n        if (k === 1) {\n           \
        \ ansPerIndex[indices[0]] = -1;\n        } else {\n            for (let p =\
        \ 0; p < k; p++) {\n                const curr = indices[p];\n             \
        \   const prev = indices[(p - 1 + k) % k];\n                const next = indices[(p\
        \ + 1) % k];\n                const d_prev = (curr - prev + n) % n;\n      \
        \          const d_next = (next - curr + n) % n;\n                ansPerIndex[curr]\
        \ = Math.min(d_prev, d_next);\n            }\n        }\n    }\n\n    const\
        \ result = new Array(queries.length);\n    for (let i = 0; i < queries.length;\
        \ i++) {\n        result[i] = ansPerIndex[queries[i]];\n    }\n    return result;\n\
        };"
      typescript: "function solveQueries(nums: number[], queries: number[]): number[]\
        \ {\n    const n = nums.length;\n    const posMap = new Map<number, number[]>();\n\
        \    for (let i = 0; i < n; i++) {\n        if (!posMap.has(nums[i])) {\n  \
        \          posMap.set(nums[i], []);\n        }\n        posMap.get(nums[i])!.push(i);\n\
        \    }\n\n    const ansPerIndex: number[] = new Array(n);\n    for (const indices\
        \ of posMap.values()) {\n        const k = indices.length;\n        if (k ===\
        \ 1) {\n            ansPerIndex[indices[0]] = -1;\n        } else {\n      \
        \      for (let p = 0; p < k; p++) {\n                const curr = indices[p];\n\
        \                const prev = indices[(p - 1 + k) % k];\n                const\
        \ next = indices[(p + 1) % k];\n                const d_prev = (curr - prev\
        \ + n) % n;\n                const d_next = (next - curr + n) % n;\n       \
        \         ansPerIndex[curr] = Math.min(d_prev, d_next);\n            }\n   \
        \     }\n    }\n\n    const result: number[] = new Array(queries.length);\n\
        \    for (let i = 0; i < queries.length; i++) {\n        result[i] = ansPerIndex[queries[i]];\n\
        \    }\n    return result;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer[] $queries\n     * @return Integer[]\n     */\n    function solveQueries($nums,\
        \ $queries) {\n        $n = count($nums);\n        $posMap = [];\n        for\
        \ ($i = 0; $i < $n; $i++) {\n            $posMap[$nums[$i]][] = $i;\n      \
        \  }\n\n        $ansPerIndex = array_fill(0, $n, 0);\n        foreach ($posMap\
        \ as $indices) {\n            $k = count($indices);\n            if ($k ===\
        \ 1) {\n                $ansPerIndex[$indices[0]] = -1;\n            } else\
        \ {\n                for ($p = 0; $p < $k; $p++) {\n                    $curr\
        \ = $indices[$p];\n                    $prev = $indices[($p - 1 + $k) % $k];\n\
        \                    $next = $indices[($p + 1) % $k];\n                    $d_prev\
        \ = ($curr - $prev + $n) % $n;\n                    $d_next = ($next - $curr\
        \ + $n) % $n;\n                    $ansPerIndex[$curr] = min($d_prev, $d_next);\n\
        \                }\n            }\n        }\n\n        $result = [];\n    \
        \    foreach ($queries as $q) {\n            $result[] = $ansPerIndex[$q];\n\
        \        }\n        return $result;\n    }\n}"
      swift: "class Solution {\n    func solveQueries(_ nums: [Int], _ queries: [Int])\
        \ -> [Int] {\n        let n = nums.count\n        var posMap = [Int: [Int]]()\n\
        \        for i in 0..<n {\n            posMap[nums[i], default: []].append(i)\n\
        \        }\n\n        var ansPerIndex = [Int](repeating: 0, count: n)\n    \
        \    for indices in posMap.values {\n            let k = indices.count\n   \
        \         if k == 1 {\n                ansPerIndex[indices[0]] = -1\n      \
        \      } else {\n                for p in 0..<k {\n                    let curr\
        \ = indices[p]\n                    let prev = indices[(p - 1 + k) % k]\n  \
        \                  let next = indices[(p + 1) % k]\n                    let\
        \ d_prev = (curr - prev + n) % n\n                    let d_next = (next - curr\
        \ + n) % n\n                    ansPerIndex[curr] = min(d_prev, d_next)\n  \
        \              }\n            }\n        }\n\n        var result = [Int]()\n\
        \        result.reserveCapacity(queries.count)\n        for q in queries {\n\
        \            result.append(ansPerIndex[q])\n        }\n        return result\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun solveQueries(nums: IntArray, queries: IntArray):\
        \ List<Int> {\n        val n = nums.size\n        val indicesMap = mutableMapOf<Int,\
        \ MutableList<Int>>()\n        for (i in nums.indices) {\n            val value\
        \ = nums[i]\n            if (!indicesMap.containsKey(value)) {\n           \
        \     indicesMap[value] = mutableListOf<Int>()\n            }\n            indicesMap[value]!!.add(i)\n\
        \        }\n\n        return queries.map { qIdx ->\n            val value =\
        \ nums[qIdx]\n            val list = indicesMap[value]!!\n            if (list.size\
        \ <= 1) {\n                -1\n            } else {\n                var low\
        \ = 0\n                var high = list.size - 1\n                var pos = -1\n\
        \                while (low <= high) {\n                    val mid = (low +\
        \ high) / 2\n                    if (list[mid] == qIdx) {\n                \
        \        pos = mid\n                        break\n                    } else\
        \ if (list[mid] < qIdx) {\n                        low = mid + 1\n         \
        \           } else {\n                        high = mid - 1\n             \
        \       }\n                }\n\n                val prevIdx = if (pos == 0)\
        \ list[list.size - 1] else list[pos - 1]\n                val nextIdx = if (pos\
        \ == list.size - 1) list[0] else list[pos + 1]\n\n                fun dist(i:\
        \ Int, j: Int): Int {\n                    val diff = if (i > j) i - j else\
        \ j - i\n                    val d2 = n - diff\n                    return if\
        \ (diff < d2) diff else d2\n                }\n\n                val d1 = dist(qIdx,\
        \ prevIdx)\n                val d2 = dist(qIdx, nextIdx)\n                if\
        \ (d1 < d2) d1 else d2\n            }\n        }\n    }\n}"
      dart: "class Solution {\n  List<int> solveQueries(List<int> nums, List<int> queries)\
        \ {\n    int n = nums.length;\n    Map<int, List<int>> indicesMap = {};\n  \
        \  for (int i = 0; i < n; i++) {\n      indicesMap.putIfAbsent(nums[i], () =>\
        \ []).add(i);\n    }\n\n    List<int> result = [];\n    for (int qIdx in queries)\
        \ {\n      int value = nums[qIdx];\n      List<int> list = indicesMap[value]!;\n\
        \      if (list.length <= 1) {\n        result.add(-1);\n        continue;\n\
        \      }\n\n      int low = 0;\n      int high = list.length - 1;\n      int\
        \ pos = -1;\n      while (low <= high) {\n        int mid = (low + high) ~/\
        \ 2;\n        if (list[mid] == qIdx) {\n          pos = mid;\n          break;\n\
        \        } else if (list[mid] < qIdx) {\n          low = mid + 1;\n        }\
        \ else {\n          high = mid - 1;\n        }\n      }\n\n      int prevIdx\
        \ = (pos == 0) ? list[list.length - 1] : list[pos - 1];\n      int nextIdx =\
        \ (pos == list.length - 1) ? list[0] : list[pos + 1];\n\n      int dist(int\
        \ i, int j) {\n        int diff = (i - j).abs();\n        int d2 = n - diff;\n\
        \        return diff < d2 ? diff : d2;\n      }\n\n      int d1 = dist(qIdx,\
        \ prevIdx);\n      int d2 = dist(qIdx, nextIdx);\n      result.add(d1 < d2 ?\
        \ d1 : d2);\n    }\n    return result;\n  }\n}"
      go: "func solveQueries(nums []int, queries []int) []int {\n    n := len(nums)\n\
        \    indicesMap := make(map[int][]int)\n    for i, val := range nums {\n   \
        \     indicesMap[val] = append(indicesMap[val], i)\n    }\n\n    result := make([]int,\
        \ len(queries))\n    for i, qIdx := range queries {\n        value := nums[qIdx]\n\
        \        list := indicesMap[value]\n        if len(list) <= 1 {\n          \
        \  result[i] = -1\n            continue\n        }\n\n        low, high := 0,\
        \ len(list)-1\n        pos := -1\n        for low <= high {\n            mid\
        \ := low + (high-low)/2\n            if list[mid] == qIdx {\n              \
        \  pos = mid\n                break\n            } else if list[mid] < qIdx\
        \ {\n                low = mid + 1\n            } else {\n                high\
        \ = mid - 1\n            }\n        }\n\n        prevIdx := list[(pos-1+len(list))%len(list)]\n\
        \        nextIdx := list[(pos+1)%len(list)]\n\n        dist := func(a, b int)\
        \ int {\n            diff := a - b\n            if diff < 0 {\n            \
        \    diff = -diff\n            }\n            if n-diff < diff {\n         \
        \       return n - diff\n            }\n            return diff\n        }\n\
        \n        d1 := dist(qIdx, prevIdx)\n        d2 := dist(qIdx, nextIdx)\n   \
        \     if d1 < d2 {\n            result[i] = d1\n        } else {\n         \
        \   result[i] = d2\n        }\n    }\n    return result\n}"
      ruby: "# @param {Integer[]} nums\n# @param {Integer[]} queries\n# @return {Integer[]}\n\
        def solve_queries(nums, queries)\n  n = nums.length\n  indices_map = {}\n  nums.each_with_index\
        \ do |val, idx|\n    indices_map[val] ||= []\n    indices_map[val] << idx\n\
        \  end\n\n  queries.map do |q_idx|\n    val = nums[q_idx]\n    list = indices_map[val]\n\
        \    if list.length <= 1\n      -1\n    else\n      pos = list.bsearch_index\
        \ { |x| x >= q_idx }\n      prev_idx = list[(pos - 1) % list.length]\n     \
        \ next_idx = list[(pos + 1) % list.length]\n\n      d1 = (q_idx - prev_idx).abs\n\
        \      d1 = [d1, n - d1].min\n      d2 = (q_idx - next_idx).abs\n      d2 =\
        \ [d2, n - d2].min\n      [d1, d2].min\n    end\n  end\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n    def solveQueries(nums:\
        \ Array[Int], queries: Array[Int]): List[Int] = {\n        val n = nums.length\n\
        \        val indicesMap = mutable.HashMap[Int, mutable.ArrayBuffer[Int]]()\n\
        \        var i = 0\n        while (i < n) {\n            val value = nums(i)\n\
        \            if (!indicesMap.contains(value)) {\n                indicesMap(value)\
        \ = mutable.ArrayBuffer[Int]()\n            }\n            indicesMap(value)\
        \ += i\n            i += 1\n        }\n\n        queries.toList.map { qIdx =>\n\
        \            val value = nums(qIdx)\n            val list = indicesMap(value)\n\
        \            if (list.length <= 1) {\n                -1\n            } else\
        \ {\n                var low = 0\n                var high = list.length - 1\n\
        \                var pos = -1\n                while (low <= high) {\n     \
        \               val mid = low + (high - low) / 2\n                    if (list(mid)\
        \ == qIdx) {\n                        pos = mid\n                        low\
        \ = high + 1\n                    } else if (list(mid) < qIdx) {\n         \
        \               low = mid + 1\n                    } else {\n              \
        \          high = mid - 1\n                    }\n                }\n\n    \
        \            val prevIdx = if (pos == 0) list(list.length - 1) else list(pos\
        \ - 1)\n                val nextIdx = if (pos == list.length - 1) list(0) else\
        \ list(pos + 1)\n\n                def dist(idx1: Int, idx2: Int): Int = {\n\
        \                    val diff = Math.abs(idx1 - idx2)\n                    if\
        \ (diff < n - diff) diff else n - diff\n                }\n\n              \
        \  val d1 = dist(qIdx, prevIdx)\n                val d2 = dist(qIdx, nextIdx)\n\
        \                if (d1 < d2) d1 else d2\n            }\n        }\n    }\n}"
      rust: "use std::collections::HashMap;\n\nimpl Solution {\n    pub fn solve_queries(nums:\
        \ Vec<i32>, queries: Vec<i32>) -> Vec<i32> {\n        let n = nums.len() as\
        \ i32;\n        let mut groups: HashMap<i32, Vec<i32>> = HashMap::new();\n \
        \       for (idx, &val) in nums.iter().enumerate() {\n            groups.entry(val).or_insert(Vec::new()).push(idx\
        \ as i32);\n        }\n\n        queries.into_iter().map(|q_idx| {\n       \
        \     let val = nums[q_idx as usize];\n            let indices = groups.get(&val).unwrap();\n\
        \            if indices.len() <= 1 {\n                -1\n            } else\
        \ {\n                let pos = indices.binary_search(&q_idx).unwrap();\n   \
        \             let m = indices.len();\n\n                let prev = indices[(pos\
        \ + m - 1) % m];\n                let next = indices[(pos + 1) % m];\n\n   \
        \             let d1 = (q_idx - prev).abs();\n                let d1_circ =\
        \ d1.min(n - d1);\n\n                let d2 = (q_idx - next).abs();\n      \
        \          let d2_circ = d2.min(n - d2);\n\n                d1_circ.min(d2_circ)\n\
        \            }\n        }).collect()\n    }\n}"
      racket: "(define/contract (solve-queries nums queries)\n  (-> (listof exact-integer?)\
        \ (listof exact-integer?) (listof exact-integer?))\n  (let* ([n (length nums)]\n\
        \         [nums-vec (list->vector nums)]\n         [groups (make-hash)])\n \
        \   (for ([val nums] [idx (in-range n)])\n      (hash-update! groups val (lambda\
        \ (lst) (cons idx lst)) '()))\n    (for ([val (hash-keys groups)])\n      (hash-set!\
        \ groups val (list->vector (sort (hash-ref groups val) <))))\n    (map (lambda\
        \ (q-idx)\n           (let* ([val (vector-ref nums-vec q-idx)]\n           \
        \       [indices (hash-ref groups val)]\n                  [m (vector-length\
        \ indices)])\n             (if (<= m 1)\n                 -1\n             \
        \    (let* ([pos (let loop ([low 0] [high (sub1 m)])\n                     \
        \          (if (> low high)\n                                   -1\n       \
        \                            (let ([mid (quotient (+ low high) 2)])\n      \
        \                               (cond\n                                    \
        \   [(= (vector-ref indices mid) q-idx) mid]\n                             \
        \          [(< (vector-ref indices mid) q-idx) (loop (add1 mid) high)]\n   \
        \                                    [else (loop low (sub1 mid))]))))]\n   \
        \                     [prev (vector-ref indices (modulo (sub1 pos) m))]\n  \
        \                      [next (vector-ref indices (modulo (add1 pos) m))]\n \
        \                       [dist (lambda (i j)\n                              \
        \  (let ([d (abs (- i j))])\n                                  (min d (- n d))))])\n\
        \                   (min (dist q-idx prev) (dist q-idx next))))))\n        \
        \ queries)))"
      erlang: "-spec solve_queries(Nums :: [integer()], Queries :: [integer()]) -> [integer()].\n\
        solve_queries(Nums, Queries) ->\n  N = length(Nums),\n  NumsVec = list_to_tuple(Nums),\n\
        \  IndicesMap = build_indices_map(Nums, 0, #{}),\n  IndicesVecMap = maps:map(fun(_,\
        \ L) -> list_to_tuple(lists:sort(L)) end, IndicesMap),\n  [solve_query(QIdx,\
        \ N, NumsVec, IndicesVecMap) || QIdx <- Queries].\n\nbuild_indices_map([], _,\
        \ Map) -> Map;\nbuild_indices_map([H | T], Idx, Map) ->\n  NewList = [Idx |\
        \ maps:get(H, Map, [])],\n  build_indices_map(T, Idx + 1, Map#{H => NewList}).\n\
        \nsolve_query(QIdx, N, NumsVec, IndicesVecMap) ->\n  Val = element(QIdx + 1,\
        \ NumsVec),\n  Indices = maps:get(Val, IndicesVecMap),\n  M = tuple_size(Indices),\n\
        \  case M of\n    1 -> -1;\n    _ ->\n      Pos = binary_search(Indices, QIdx,\
        \ 1, M),\n      PrevIdx = element((Pos - 2 + M) rem M + 1, Indices),\n     \
        \ NextIdx = element(Pos rem M + 1, Indices),\n      D1 = abs(QIdx - PrevIdx),\n\
        \      Dist1 = min(D1, N - D1),\n      D2 = abs(QIdx - NextIdx),\n      Dist2\
        \ = min(D2, N - D2),\n      min(Dist1, Dist2)\n  end.\n\nbinary_search(Tuple,\
        \ Target, Low, High) ->\n  Mid = (Low + High) div 2,\n  Val = element(Mid, Tuple),\n\
        \  if\n    Val == Target -> Mid;\n    Val < Target -> binary_search(Tuple, Target,\
        \ Mid + 1, High);\n    true -> binary_search(Tuple, Target, Low, Mid - 1)\n\
        \  end."
      elixir: "defmodule Solution do\n  @spec solve_queries(nums :: [integer], queries\
        \ :: [integer]) :: [integer]\n  def solve_queries(nums, queries) do\n    n =\
        \ length(nums)\n    nums_vec = List.to_tuple(nums)\n\n    indices_map = nums\n\
        \    |> Enum.with_index()\n    |> Enum.group_by(fn {val, _idx} -> val end, fn\
        \ {_val, idx} -> idx end)\n    |> Map.new(fn {val, idx_list} -> {val, List.to_tuple(Enum.sort(idx_list))}\
        \ end)\n\n    Enum.map(queries, fn q_idx ->\n      val = elem(nums_vec, q_idx)\n\
        \      indices = Map.get(indices_map, val)\n      m = tuple_size(indices)\n\n\
        \      if m <= 1 do\n        -1\n      else\n        pos = binary_search(indices,\
        \ q_idx, 0, m - 1)\n        prev_idx = elem(indices, rem(pos - 1 + m, m))\n\
        \        next_idx = elem(indices, rem(pos + 1, m))\n\n        d1 = abs(q_idx\
        \ - prev_idx)\n        dist1 = min(d1, n - d1)\n        d2 = abs(q_idx - next_idx)\n\
        \        dist2 = min(d2, n - d2)\n        min(dist1, dist2)\n      end\n   \
        \ end)\n  end\n\n  defp binary_search(tuple, target, low, high) do\n    mid\
        \ = div(low + high, 2)\n    val = elem(tuple, mid)\n    cond do\n      val ==\
        \ target -> mid\n      val < target -> binary_search(tuple, target, mid + 1,\
        \ high)\n      true -> binary_search(tuple, target, low, mid - 1)\n    end\n\
        \  end\nend"
    approach: To efficiently find the nearest same-valued element in a circular array,
      we group all indices for each unique value into sorted lists. This pre-processing
      associates each unique value in the array with its list of occurrences, allowing
      us to quickly identify all potential candidates for any query. By iterating through
      the array once, we build this mapping (or sort value-index pairs) so that for
      any value $V$, we can access a sorted list of indices where $V$ appears.
    time_complexity: O((N + Q) \log N) with one-paragraph explanation. Building the
      index map (or sorting in C) takes O(N \log N), and for each of the Q queries,
      we perform binary search within the sorted index list in O(\log N) time to find
      the target's neighbors. Given N and Q up to $10^5$, this fits comfortably within
      the time limit.
    space_complexity: O(N) with one-paragraph explanation. We store the mapping of all
      $N$ indices of the original array, either in a hash map of lists or a sorted auxiliary
      array of structs, which consumes linear space.
    elapsed_time: 252.64363312721252
    model: gemini-3-flash-preview
    generated_at: '2026-04-16 02:02:51 '
---

## Problem #3488: Closest Equal Element Queries

**Difficulty:** Medium

**Topics:** Array, Hash Table, Binary Search

## Problem Description

<p>You are given a <strong>circular</strong> array <code>nums</code> and an array <code>queries</code>.</p>

<p>For each query <code>i</code>, you have to find the following:</p>

<ul>
	<li>The <strong>minimum</strong> distance between the element at index <code>queries[i]</code> and <strong>any</strong> other index <code>j</code> in the <strong>circular</strong> array, where <code>nums[j] == nums[queries[i]]</code>. If no such index exists, the answer for that query should be -1.</li>
</ul>

<p>Return an array <code>answer</code> of the <strong>same</strong> size as <code>queries</code>, where <code>answer[i]</code> represents the result for query <code>i</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,3,1,4,1,3,2], queries = [0,3,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">[2,-1,3]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Query 0: The element at <code>queries[0] = 0</code> is <code>nums[0] = 1</code>. The nearest index with the same value is 2, and the distance between them is 2.</li>
	<li>Query 1: The element at <code>queries[1] = 3</code> is <code>nums[3] = 4</code>. No other index contains 4, so the result is -1.</li>
	<li>Query 2: The element at <code>queries[2] = 5</code> is <code>nums[5] = 3</code>. The nearest index with the same value is 1, and the distance between them is 3 (following the circular path: <code>5 -&gt; 6 -&gt; 0 -&gt; 1</code>).</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4], queries = [0,1,2,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">[-1,-1,-1,-1]</span></p>

<p><strong>Explanation:</strong></p>

<p>Each value in <code>nums</code> is unique, so no index shares the same value as the queried element. This results in -1 for all queries.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= queries.length &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>0 &lt;= queries[i] &lt; nums.length</code></li>
</ul>


## Hints

1. Use a dictionary that maps each unique value in the array to a sorted list of its indices.

2. For each query, use binary search on the sorted indices list to find the nearest occurrences of the target value.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To efficiently find the nearest same-valued element in a circular array, we group all indices for each unique value into sorted lists. This pre-processing associates each unique value in the array with its list of occurrences, allowing us to quickly identify all potential candidates for any query. By iterating through the array once, we build this mapping (or sort value-index pairs) so that for any value $V$, we can access a sorted list of indices where $V$ appears.

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
    vector<int> solveQueries(vector<int>& nums, vector<int>& queries) {
        int n = nums.size();
        std::unordered_map<int, std::vector<int>> posMap;
        for (int i = 0; i < n; ++i) {
            posMap[nums[i]].push_back(i);
        }

        std::vector<int> results;
        results.reserve(queries.size());

        for (int qIdx : queries) {
            int target = nums[qIdx];
            const std::vector<int>& indices = posMap[target];
            int k = indices.size();

            if (k == 1) {
                results.push_back(-1);
                continue;
            }

            auto it = std::lower_bound(indices.begin(), indices.end(), qIdx);
            int pos = std::distance(indices.begin(), it);

            int prevIdx = indices[(pos - 1 + k) % k];
            int nextIdx = indices[(pos + 1) % k];

            auto getDist = [&](int i, int j) {
                int d = std::abs(i - j);
                return std::min(d, n - d);
            };

            results.push_back(std::min(getDist(qIdx, prevIdx), getDist(qIdx, nextIdx)));
        }

        return results;
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
    public List<Integer> solveQueries(int[] nums, int[] queries) {
        int n = nums.length;
        Map<Integer, List<Integer>> posMap = new HashMap<>();
        for (int i = 0; i < n; i++) {
            posMap.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
        }

        List<Integer> result = new ArrayList<>(queries.length);
        for (int qIdx : queries) {
            int target = nums[qIdx];
            List<Integer> indices = posMap.get(target);
            int k = indices.size();

            if (k == 1) {
                result.add(-1);
                continue;
            }

            int pos = Collections.binarySearch(indices, qIdx);
            int prevIdx = indices.get((pos - 1 + k) % k);
            int nextIdx = indices.get((pos + 1) % k);

            int d1 = Math.abs(qIdx - prevIdx);
            int d2 = Math.abs(qIdx - nextIdx);
            int dist1 = Math.min(d1, n - d1);
            int dist2 = Math.min(d2, n - d2);

            result.add(Math.min(dist1, dist2));
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
from collections import defaultdict
from bisect import bisect_left

class Solution(object):
    def solveQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        pos_map = defaultdict(list)
        for i, val in enumerate(nums):
            pos_map[val].append(i)

        ans = []
        for q_idx in queries:
            val = nums[q_idx]
            indices = pos_map[val]
            k = len(indices)
            if k == 1:
                ans.append(-1)
                continue

            pos = bisect_left(indices, q_idx)
            prev_idx = indices[(pos - 1 + k) % k]
            next_idx = indices[(pos + 1) % k]

            d1 = abs(q_idx - prev_idx)
            dist1 = min(d1, n - d1)
            d2 = abs(q_idx - next_idx)
            dist2 = min(d2, n - d2)
            ans.append(min(dist1, dist2))
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from collections import defaultdict
from bisect import bisect_left
from typing import List

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        pos_map = defaultdict(list)
        for i, val in enumerate(nums):
            pos_map[val].append(i)

        ans = []
        for q_idx in queries:
            val = nums[q_idx]
            indices = pos_map[val]
            k = len(indices)
            if k == 1:
                ans.append(-1)
                continue

            pos = bisect_left(indices, q_idx)
            prev_idx = indices[(pos - 1 + k) % k]
            next_idx = indices[(pos + 1) % k]

            d1 = abs(q_idx - prev_idx)
            dist1 = min(d1, n - d1)
            d2 = abs(q_idx - next_idx)
            dist2 = min(d2, n - d2)
            ans.append(min(dist1, dist2))
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <stdio.h>

typedef struct {
    int val;
    int idx;
} Entry;

int cmp(const void* a, const void* b) {
    Entry* e1 = (Entry*)a;
    Entry* e2 = (Entry*)b;
    if (e1->val != e2->val) return e1->val - e2->val;
    return e1->idx - e2->idx;
}

int get_circular_dist(int i, int j, int n) {
    int d = abs(i - j);
    int d2 = n - d;
    return (d < d2) ? d : d2;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* solveQueries(int* nums, int numsSize, int* queries, int queriesSize, int* returnSize) {
    Entry* entries = (Entry*)malloc(numsSize * sizeof(Entry));
    for (int i = 0; i < numsSize; i++) {
        entries[i].val = nums[i];
        entries[i].idx = i;
    }
    qsort(entries, numsSize, sizeof(Entry), cmp);

    int* result = (int*)malloc(queriesSize * sizeof(int));
    *returnSize = queriesSize;

    for (int i = 0; i < queriesSize; i++) {
        int qIdx = queries[i];
        int target = nums[qIdx];

        int first = -1, last = -1;
        int l = 0, r = numsSize - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (entries[mid].val >= target) {
                if (entries[mid].val == target) first = mid;
                r = mid - 1;
            } else l = mid + 1;
        }

        l = 0, r = numsSize - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (entries[mid].val <= target) {
                if (entries[mid].val == target) last = mid;
                l = mid + 1;
            } else r = mid - 1;
        }

        if (first == -1 || first == last) {
            result[i] = -1;
            continue;
        }

        int pos = -1;
        l = first, r = last;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (entries[mid].idx == qIdx) {
                pos = mid;
                break;
            }
            if (entries[mid].idx < qIdx) l = mid + 1;
            else r = mid - 1;
        }

        int K = last - first + 1;
        int relPos = pos - first;
        int idxPrev = entries[first + (relPos - 1 + K) % K].idx;
        int idxNext = entries[first + (relPos + 1) % K].idx;

        int d1 = get_circular_dist(qIdx, idxPrev, numsSize);
        int d2 = get_circular_dist(qIdx, idxNext, numsSize);
        result[i] = (d1 < d2) ? d1 : d2;
    }

    free(entries);
    return result;
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
    public IList<int> SolveQueries(int[] nums, int[] queries) {
        int n = nums.Length;
        Dictionary<int, List<int>> posMap = new Dictionary<int, List<int>>();
        for (int i = 0; i < n; i++) {
            if (!posMap.ContainsKey(nums[i])) {
                posMap[nums[i]] = new List<int>();
            }
            posMap[nums[i]].Add(i);
        }

        int[] ansPerIndex = new int[n];
        foreach (var kvp in posMap) {
            List<int> indices = kvp.Value;
            int k = indices.Count;
            if (k == 1) {
                ansPerIndex[indices[0]] = -1;
            } else {
                for (int p = 0; p < k; p++) {
                    int curr = indices[p];
                    int prev = indices[(p - 1 + k) % k];
                    int next = indices[(p + 1) % k];
                    int d_prev = (curr - prev + n) % n;
                    int d_next = (next - curr + n) % n;
                    ansPerIndex[curr] = Math.Min(d_prev, d_next);
                }
            }
        }

        int[] result = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            result[i] = ansPerIndex[queries[i]];
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
 * @param {number[]} nums
 * @param {number[]} queries
 * @return {number[]}
 */
var solveQueries = function(nums, queries) {
    const n = nums.length;
    const posMap = new Map();
    for (let i = 0; i < n; i++) {
        if (!posMap.has(nums[i])) {
            posMap.set(nums[i], []);
        }
        posMap.get(nums[i]).push(i);
    }

    const ansPerIndex = new Int32Array(n);
    for (const indices of posMap.values()) {
        const k = indices.length;
        if (k === 1) {
            ansPerIndex[indices[0]] = -1;
        } else {
            for (let p = 0; p < k; p++) {
                const curr = indices[p];
                const prev = indices[(p - 1 + k) % k];
                const next = indices[(p + 1) % k];
                const d_prev = (curr - prev + n) % n;
                const d_next = (next - curr + n) % n;
                ansPerIndex[curr] = Math.min(d_prev, d_next);
            }
        }
    }

    const result = new Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        result[i] = ansPerIndex[queries[i]];
    }
    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function solveQueries(nums: number[], queries: number[]): number[] {
    const n = nums.length;
    const posMap = new Map<number, number[]>();
    for (let i = 0; i < n; i++) {
        if (!posMap.has(nums[i])) {
            posMap.set(nums[i], []);
        }
        posMap.get(nums[i])!.push(i);
    }

    const ansPerIndex: number[] = new Array(n);
    for (const indices of posMap.values()) {
        const k = indices.length;
        if (k === 1) {
            ansPerIndex[indices[0]] = -1;
        } else {
            for (let p = 0; p < k; p++) {
                const curr = indices[p];
                const prev = indices[(p - 1 + k) % k];
                const next = indices[(p + 1) % k];
                const d_prev = (curr - prev + n) % n;
                const d_next = (next - curr + n) % n;
                ansPerIndex[curr] = Math.min(d_prev, d_next);
            }
        }
    }

    const result: number[] = new Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        result[i] = ansPerIndex[queries[i]];
    }
    return result;
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
     * @param Integer[] $queries
     * @return Integer[]
     */
    function solveQueries($nums, $queries) {
        $n = count($nums);
        $posMap = [];
        for ($i = 0; $i < $n; $i++) {
            $posMap[$nums[$i]][] = $i;
        }

        $ansPerIndex = array_fill(0, $n, 0);
        foreach ($posMap as $indices) {
            $k = count($indices);
            if ($k === 1) {
                $ansPerIndex[$indices[0]] = -1;
            } else {
                for ($p = 0; $p < $k; $p++) {
                    $curr = $indices[$p];
                    $prev = $indices[($p - 1 + $k) % $k];
                    $next = $indices[($p + 1) % $k];
                    $d_prev = ($curr - $prev + $n) % $n;
                    $d_next = ($next - $curr + $n) % $n;
                    $ansPerIndex[$curr] = min($d_prev, $d_next);
                }
            }
        }

        $result = [];
        foreach ($queries as $q) {
            $result[] = $ansPerIndex[$q];
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
    func solveQueries(_ nums: [Int], _ queries: [Int]) -> [Int] {
        let n = nums.count
        var posMap = [Int: [Int]]()
        for i in 0..<n {
            posMap[nums[i], default: []].append(i)
        }

        var ansPerIndex = [Int](repeating: 0, count: n)
        for indices in posMap.values {
            let k = indices.count
            if k == 1 {
                ansPerIndex[indices[0]] = -1
            } else {
                for p in 0..<k {
                    let curr = indices[p]
                    let prev = indices[(p - 1 + k) % k]
                    let next = indices[(p + 1) % k]
                    let d_prev = (curr - prev + n) % n
                    let d_next = (next - curr + n) % n
                    ansPerIndex[curr] = min(d_prev, d_next)
                }
            }
        }

        var result = [Int]()
        result.reserveCapacity(queries.count)
        for q in queries {
            result.append(ansPerIndex[q])
        }
        return result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun solveQueries(nums: IntArray, queries: IntArray): List<Int> {
        val n = nums.size
        val indicesMap = mutableMapOf<Int, MutableList<Int>>()
        for (i in nums.indices) {
            val value = nums[i]
            if (!indicesMap.containsKey(value)) {
                indicesMap[value] = mutableListOf<Int>()
            }
            indicesMap[value]!!.add(i)
        }

        return queries.map { qIdx ->
            val value = nums[qIdx]
            val list = indicesMap[value]!!
            if (list.size <= 1) {
                -1
            } else {
                var low = 0
                var high = list.size - 1
                var pos = -1
                while (low <= high) {
                    val mid = (low + high) / 2
                    if (list[mid] == qIdx) {
                        pos = mid
                        break
                    } else if (list[mid] < qIdx) {
                        low = mid + 1
                    } else {
                        high = mid - 1
                    }
                }

                val prevIdx = if (pos == 0) list[list.size - 1] else list[pos - 1]
                val nextIdx = if (pos == list.size - 1) list[0] else list[pos + 1]

                fun dist(i: Int, j: Int): Int {
                    val diff = if (i > j) i - j else j - i
                    val d2 = n - diff
                    return if (diff < d2) diff else d2
                }

                val d1 = dist(qIdx, prevIdx)
                val d2 = dist(qIdx, nextIdx)
                if (d1 < d2) d1 else d2
            }
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<int> solveQueries(List<int> nums, List<int> queries) {
    int n = nums.length;
    Map<int, List<int>> indicesMap = {};
    for (int i = 0; i < n; i++) {
      indicesMap.putIfAbsent(nums[i], () => []).add(i);
    }

    List<int> result = [];
    for (int qIdx in queries) {
      int value = nums[qIdx];
      List<int> list = indicesMap[value]!;
      if (list.length <= 1) {
        result.add(-1);
        continue;
      }

      int low = 0;
      int high = list.length - 1;
      int pos = -1;
      while (low <= high) {
        int mid = (low + high) ~/ 2;
        if (list[mid] == qIdx) {
          pos = mid;
          break;
        } else if (list[mid] < qIdx) {
          low = mid + 1;
        } else {
          high = mid - 1;
        }
      }

      int prevIdx = (pos == 0) ? list[list.length - 1] : list[pos - 1];
      int nextIdx = (pos == list.length - 1) ? list[0] : list[pos + 1];

      int dist(int i, int j) {
        int diff = (i - j).abs();
        int d2 = n - diff;
        return diff < d2 ? diff : d2;
      }

      int d1 = dist(qIdx, prevIdx);
      int d2 = dist(qIdx, nextIdx);
      result.add(d1 < d2 ? d1 : d2);
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
func solveQueries(nums []int, queries []int) []int {
    n := len(nums)
    indicesMap := make(map[int][]int)
    for i, val := range nums {
        indicesMap[val] = append(indicesMap[val], i)
    }

    result := make([]int, len(queries))
    for i, qIdx := range queries {
        value := nums[qIdx]
        list := indicesMap[value]
        if len(list) <= 1 {
            result[i] = -1
            continue
        }

        low, high := 0, len(list)-1
        pos := -1
        for low <= high {
            mid := low + (high-low)/2
            if list[mid] == qIdx {
                pos = mid
                break
            } else if list[mid] < qIdx {
                low = mid + 1
            } else {
                high = mid - 1
            }
        }

        prevIdx := list[(pos-1+len(list))%len(list)]
        nextIdx := list[(pos+1)%len(list)]

        dist := func(a, b int) int {
            diff := a - b
            if diff < 0 {
                diff = -diff
            }
            if n-diff < diff {
                return n - diff
            }
            return diff
        }

        d1 := dist(qIdx, prevIdx)
        d2 := dist(qIdx, nextIdx)
        if d1 < d2 {
            result[i] = d1
        } else {
            result[i] = d2
        }
    }
    return result
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @param {Integer[]} queries
# @return {Integer[]}
def solve_queries(nums, queries)
  n = nums.length
  indices_map = {}
  nums.each_with_index do |val, idx|
    indices_map[val] ||= []
    indices_map[val] << idx
  end

  queries.map do |q_idx|
    val = nums[q_idx]
    list = indices_map[val]
    if list.length <= 1
      -1
    else
      pos = list.bsearch_index { |x| x >= q_idx }
      prev_idx = list[(pos - 1) % list.length]
      next_idx = list[(pos + 1) % list.length]

      d1 = (q_idx - prev_idx).abs
      d1 = [d1, n - d1].min
      d2 = (q_idx - next_idx).abs
      d2 = [d2, n - d2].min
      [d1, d2].min
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

object Solution {
    def solveQueries(nums: Array[Int], queries: Array[Int]): List[Int] = {
        val n = nums.length
        val indicesMap = mutable.HashMap[Int, mutable.ArrayBuffer[Int]]()
        var i = 0
        while (i < n) {
            val value = nums(i)
            if (!indicesMap.contains(value)) {
                indicesMap(value) = mutable.ArrayBuffer[Int]()
            }
            indicesMap(value) += i
            i += 1
        }

        queries.toList.map { qIdx =>
            val value = nums(qIdx)
            val list = indicesMap(value)
            if (list.length <= 1) {
                -1
            } else {
                var low = 0
                var high = list.length - 1
                var pos = -1
                while (low <= high) {
                    val mid = low + (high - low) / 2
                    if (list(mid) == qIdx) {
                        pos = mid
                        low = high + 1
                    } else if (list(mid) < qIdx) {
                        low = mid + 1
                    } else {
                        high = mid - 1
                    }
                }

                val prevIdx = if (pos == 0) list(list.length - 1) else list(pos - 1)
                val nextIdx = if (pos == list.length - 1) list(0) else list(pos + 1)

                def dist(idx1: Int, idx2: Int): Int = {
                    val diff = Math.abs(idx1 - idx2)
                    if (diff < n - diff) diff else n - diff
                }

                val d1 = dist(qIdx, prevIdx)
                val d2 = dist(qIdx, nextIdx)
                if (d1 < d2) d1 else d2
            }
        }
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
    pub fn solve_queries(nums: Vec<i32>, queries: Vec<i32>) -> Vec<i32> {
        let n = nums.len() as i32;
        let mut groups: HashMap<i32, Vec<i32>> = HashMap::new();
        for (idx, &val) in nums.iter().enumerate() {
            groups.entry(val).or_insert(Vec::new()).push(idx as i32);
        }

        queries.into_iter().map(|q_idx| {
            let val = nums[q_idx as usize];
            let indices = groups.get(&val).unwrap();
            if indices.len() <= 1 {
                -1
            } else {
                let pos = indices.binary_search(&q_idx).unwrap();
                let m = indices.len();

                let prev = indices[(pos + m - 1) % m];
                let next = indices[(pos + 1) % m];

                let d1 = (q_idx - prev).abs();
                let d1_circ = d1.min(n - d1);

                let d2 = (q_idx - next).abs();
                let d2_circ = d2.min(n - d2);

                d1_circ.min(d2_circ)
            }
        }).collect()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (solve-queries nums queries)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  (let* ([n (length nums)]
         [nums-vec (list->vector nums)]
         [groups (make-hash)])
    (for ([val nums] [idx (in-range n)])
      (hash-update! groups val (lambda (lst) (cons idx lst)) '()))
    (for ([val (hash-keys groups)])
      (hash-set! groups val (list->vector (sort (hash-ref groups val) <))))
    (map (lambda (q-idx)
           (let* ([val (vector-ref nums-vec q-idx)]
                  [indices (hash-ref groups val)]
                  [m (vector-length indices)])
             (if (<= m 1)
                 -1
                 (let* ([pos (let loop ([low 0] [high (sub1 m)])
                               (if (> low high)
                                   -1
                                   (let ([mid (quotient (+ low high) 2)])
                                     (cond
                                       [(= (vector-ref indices mid) q-idx) mid]
                                       [(< (vector-ref indices mid) q-idx) (loop (add1 mid) high)]
                                       [else (loop low (sub1 mid))]))))]
                        [prev (vector-ref indices (modulo (sub1 pos) m))]
                        [next (vector-ref indices (modulo (add1 pos) m))]
                        [dist (lambda (i j)
                                (let ([d (abs (- i j))])
                                  (min d (- n d))))])
                   (min (dist q-idx prev) (dist q-idx next))))))
         queries)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec solve_queries(Nums :: [integer()], Queries :: [integer()]) -> [integer()].
solve_queries(Nums, Queries) ->
  N = length(Nums),
  NumsVec = list_to_tuple(Nums),
  IndicesMap = build_indices_map(Nums, 0, #{}),
  IndicesVecMap = maps:map(fun(_, L) -> list_to_tuple(lists:sort(L)) end, IndicesMap),
  [solve_query(QIdx, N, NumsVec, IndicesVecMap) || QIdx <- Queries].

build_indices_map([], _, Map) -> Map;
build_indices_map([H | T], Idx, Map) ->
  NewList = [Idx | maps:get(H, Map, [])],
  build_indices_map(T, Idx + 1, Map#{H => NewList}).

solve_query(QIdx, N, NumsVec, IndicesVecMap) ->
  Val = element(QIdx + 1, NumsVec),
  Indices = maps:get(Val, IndicesVecMap),
  M = tuple_size(Indices),
  case M of
    1 -> -1;
    _ ->
      Pos = binary_search(Indices, QIdx, 1, M),
      PrevIdx = element((Pos - 2 + M) rem M + 1, Indices),
      NextIdx = element(Pos rem M + 1, Indices),
      D1 = abs(QIdx - PrevIdx),
      Dist1 = min(D1, N - D1),
      D2 = abs(QIdx - NextIdx),
      Dist2 = min(D2, N - D2),
      min(Dist1, Dist2)
  end.

binary_search(Tuple, Target, Low, High) ->
  Mid = (Low + High) div 2,
  Val = element(Mid, Tuple),
  if
    Val == Target -> Mid;
    Val < Target -> binary_search(Tuple, Target, Mid + 1, High);
    true -> binary_search(Tuple, Target, Low, Mid - 1)
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec solve_queries(nums :: [integer], queries :: [integer]) :: [integer]
  def solve_queries(nums, queries) do
    n = length(nums)
    nums_vec = List.to_tuple(nums)

    indices_map = nums
    |> Enum.with_index()
    |> Enum.group_by(fn {val, _idx} -> val end, fn {_val, idx} -> idx end)
    |> Map.new(fn {val, idx_list} -> {val, List.to_tuple(Enum.sort(idx_list))} end)

    Enum.map(queries, fn q_idx ->
      val = elem(nums_vec, q_idx)
      indices = Map.get(indices_map, val)
      m = tuple_size(indices)

      if m <= 1 do
        -1
      else
        pos = binary_search(indices, q_idx, 0, m - 1)
        prev_idx = elem(indices, rem(pos - 1 + m, m))
        next_idx = elem(indices, rem(pos + 1, m))

        d1 = abs(q_idx - prev_idx)
        dist1 = min(d1, n - d1)
        d2 = abs(q_idx - next_idx)
        dist2 = min(d2, n - d2)
        min(dist1, dist2)
      end
    end)
  end

  defp binary_search(tuple, target, low, high) do
    mid = div(low + high, 2)
    val = elem(tuple, mid)
    cond do
      val == target -> mid
      val < target -> binary_search(tuple, target, mid + 1, high)
      true -> binary_search(tuple, target, low, mid - 1)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O((N + Q) \log N) with one-paragraph explanation. Building the index map (or sorting in C) takes O(N \log N), and for each of the Q queries, we perform binary search within the sorted index list in O(\log N) time to find the target's neighbors. Given N and Q up to $10^5$, this fits comfortably within the time limit.
- **Space Complexity:** O(N) with one-paragraph explanation. We store the mapping of all $N$ indices of the original array, either in a hash map of lists or a sorted auxiliary array of structs, which consumes linear space.
