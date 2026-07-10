---
layout: post
title: "Path Existence Queries in a Graph II"
date: 2026-07-10 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Two Pointers", "Binary Search", "Dynamic Programming", "Greedy", "Bit Manipulation", "Graph Theory", "Sorting"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> pathExistenceQueries(int n, vector<int>&\
        \ nums, int maxDiff, vector<vector<int>>& queries) {\n        vector<int> unique_vals\
        \ = nums;\n        sort(unique_vals.begin(), unique_vals.end());\n        unique_vals.erase(unique(unique_vals.begin(),\
        \ unique_vals.end()), unique_vals.end());\n\n        int n_unique = unique_vals.size();\n\
        \        int max_log = 17;\n        vector<vector<int>> up(max_log + 1, vector<int>(n_unique));\n\
        \n        for (int i = 0; i < n_unique; ++i) {\n            int target = unique_vals[i]\
        \ + maxDiff;\n            auto it = upper_bound(unique_vals.begin(), unique_vals.end(),\
        \ target);\n            up[0][i] = distance(unique_vals.begin(), it) - 1;\n\
        \        }\n\n        for (int j = 1; j <= max_log; ++j) {\n            for\
        \ (int i = 0; i < n_unique; ++i) {\n                up[j][i] = up[j - 1][up[j\
        \ - 1][i]];\n            }\n        }\n\n        vector<int> ans;\n        ans.reserve(queries.size());\n\
        \        for (const auto& q : queries) {\n            int u = q[0], v = q[1];\n\
        \            if (u == v) {\n                ans.push_back(0);\n            \
        \    continue;\n            }\n            int v1 = nums[u], v2 = nums[v];\n\
        \            if (v1 > v2) swap(v1, v2);\n\n            int idx1 = lower_bound(unique_vals.begin(),\
        \ unique_vals.end(), v1) - unique_vals.begin();\n            int idx2 = lower_bound(unique_vals.begin(),\
        \ unique_vals.end(), v2) - unique_vals.begin();\n\n            if (up[max_log][idx1]\
        \ < idx2) {\n                ans.push_back(-1);\n            } else {\n    \
        \            int dist = 0;\n                int curr = idx1;\n             \
        \   for (int j = max_log; j >= 0; --j) {\n                    if (up[j][curr]\
        \ < idx2) {\n                        curr = up[j][curr];\n                 \
        \       dist += (1 << j);\n                    }\n                }\n      \
        \          ans.push_back(dist + 1);\n            }\n        }\n        return\
        \ ans;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public int[] pathExistenceQueries(int\
        \ n, int[] nums, int maxDiff, int[][] queries) {\n        int[] sortedNums =\
        \ nums.clone();\n        Arrays.sort(sortedNums);\n\n        int k = 0;\n  \
        \      if (n > 0) {\n            k = 1;\n            for (int i = 1; i < n;\
        \ i++) {\n                if (sortedNums[i] != sortedNums[i - 1]) {\n      \
        \              sortedNums[k++] = sortedNums[i];\n                }\n       \
        \     }\n        }\n        int nUnique = k;\n        int[] uniqueVals = Arrays.copyOf(sortedNums,\
        \ nUnique);\n\n        int maxLog = 17;\n        int[][] up = new int[maxLog\
        \ + 1][nUnique];\n\n        for (int i = 0; i < nUnique; i++) {\n          \
        \  int target = uniqueVals[i] + maxDiff;\n            int idx = Arrays.binarySearch(uniqueVals,\
        \ target);\n            if (idx < 0) {\n                idx = -(idx + 1) - 1;\n\
        \            }\n            up[0][i] = idx;\n        }\n\n        for (int j\
        \ = 1; j <= maxLog; j++) {\n            for (int i = 0; i < nUnique; i++) {\n\
        \                up[j][i] = up[j - 1][up[j - 1][i]];\n            }\n      \
        \  }\n\n        int[] results = new int[queries.length];\n        for (int i\
        \ = 0; i < queries.length; i++) {\n            int u = queries[i][0];\n    \
        \        int v = queries[i][1];\n            if (u == v) {\n               \
        \ results[i] = 0;\n                continue;\n            }\n            int\
        \ v1 = nums[u], v2 = nums[v];\n            if (v1 > v2) {\n                int\
        \ temp = v1;\n                v1 = v2;\n                v2 = temp;\n       \
        \     }\n\n            int idx1 = Arrays.binarySearch(uniqueVals, v1);\n   \
        \         int idx2 = Arrays.binarySearch(uniqueVals, v2);\n\n            if\
        \ (up[maxLog][idx1] < idx2) {\n                results[i] = -1;\n          \
        \  } else {\n                int dist = 0;\n                int curr = idx1;\n\
        \                for (int j = maxLog; j >= 0; j--) {\n                    if\
        \ (up[j][curr] < idx2) {\n                        curr = up[j][curr];\n    \
        \                    dist += (1 << j);\n                    }\n            \
        \    }\n                results[i] = dist + 1;\n            }\n        }\n \
        \       return results;\n    }\n}"
      python: "import bisect\n\nclass Solution(object):\n    def pathExistenceQueries(self,\
        \ n, nums, maxDiff, queries):\n        unique_vals = sorted(list(set(nums)))\n\
        \        val_to_idx = {v: i for i, v in enumerate(unique_vals)}\n        n_unique\
        \ = len(unique_vals)\n        MAX_LOG = 17\n\n        up = [[] for _ in range(MAX_LOG\
        \ + 1)]\n        first_jumps = []\n        for v in unique_vals:\n         \
        \   target = v + maxDiff\n            idx = bisect.bisect_right(unique_vals,\
        \ target) - 1\n            first_jumps.append(idx)\n\n        up[0] = first_jumps\n\
        \        for j in range(1, MAX_LOG + 1):\n            prev_up = up[j-1]\n  \
        \          up[j] = [prev_up[prev_up[i]] for i in range(n_unique)]\n\n      \
        \  res = []\n        ML = MAX_LOG\n        for u, v in queries:\n          \
        \  if u == v:\n                res.append(0)\n                continue\n   \
        \         v1, v2 = nums[u], nums[v]\n            if v1 > v2: v1, v2 = v2, v1\n\
        \n            idx1 = val_to_idx[v1]\n            idx2 = val_to_idx[v2]\n\n \
        \           if up[ML][idx1] < idx2:\n                res.append(-1)\n      \
        \      else:\n                dist = 0\n                curr = idx1\n      \
        \          for j in range(ML, -1, -1):\n                    up_j = up[j]\n \
        \                   if up_j[curr] < idx2:\n                        curr = up_j[curr]\n\
        \                        dist += (1 << j)\n                res.append(dist +\
        \ 1)\n        return res"
      python3: "from bisect import bisect_right\n\nclass Solution:\n    def pathExistenceQueries(self,\
        \ n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:\n\
        \        unique_vals = sorted(list(set(nums)))\n        val_to_idx = {v: i for\
        \ i, v in enumerate(unique_vals)}\n        m = len(unique_vals)\n        LOG\
        \ = 18\n\n        jump = [[0] * m for _ in range(LOG)]\n        for i in range(m):\n\
        \            target_val = unique_vals[i] + maxDiff\n            idx = bisect_right(unique_vals,\
        \ target_val) - 1\n            jump[0][i] = idx\n\n        for k in range(1,\
        \ LOG):\n            for i in range(m):\n                jump[k][i] = jump[k\
        \ - 1][jump[k - 1][i]]\n\n        results = []\n        for u, v in queries:\n\
        \            if u == v:\n                results.append(0)\n               \
        \ continue\n            if nums[u] == nums[v]:\n                results.append(1)\n\
        \                continue\n\n            val_u, val_v = nums[u], nums[v]\n \
        \           if val_u > val_v:\n                val_u, val_v = val_v, val_u\n\
        \n            curr = val_to_idx[val_u]\n            target = val_to_idx[val_v]\n\
        \            steps = 0\n            for k in range(LOG - 1, -1, -1):\n     \
        \           if jump[k][curr] < target:\n                    curr = jump[k][curr]\n\
        \                    steps += (1 << k)\n\n            if jump[0][curr] >= target:\n\
        \                results.append(steps + 1)\n            else:\n            \
        \    results.append(-1)\n\n        return results"
      c: "#include <stdlib.h>\n#include <string.h>\n\nint compareInts(const void* a,\
        \ const void* b) {\n    int x = *(const int*)a;\n    int y = *(const int*)b;\n\
        \    if (x < y) return -1;\n    if (x > y) return 1;\n    return 0;\n}\n\nint\
        \ upper_bound(int* arr, int size, int val) {\n    int low = 0, high = size;\n\
        \    while (low < high) {\n        int mid = low + (high - low) / 2;\n     \
        \   if (arr[mid] <= val) low = mid + 1;\n        else high = mid;\n    }\n \
        \   return low;\n}\n\nint get_idx(int* arr, int size, int val) {\n    int low\
        \ = 0, high = size - 1;\n    while (low <= high) {\n        int mid = low +\
        \ (high - low) / 2;\n        if (arr[mid] == val) return mid;\n        if (arr[mid]\
        \ < val) low = mid + 1;\n        else high = mid;\n    }\n    return -1;\n}\n\
        \nint* pathExistenceQueries(int n, int* nums, int numsSize, int maxDiff, int**\
        \ queries, int queriesSize, int* queriesColSize, int* returnSize) {\n    int*\
        \ sorted_nums = (int*)malloc(n * sizeof(int));\n    memcpy(sorted_nums, nums,\
        \ n * sizeof(int));\n    qsort(sorted_nums, n, sizeof(int), compareInts);\n\n\
        \    int m = 0;\n    if (n > 0) {\n        m = 1;\n        for (int i = 1; i\
        \ < n; i++) {\n            if (sorted_nums[i] != sorted_nums[i-1]) {\n     \
        \           sorted_nums[m++] = sorted_nums[i];\n            }\n        }\n \
        \   }\n\n    const int LOG = 18;\n    int* jump = (int*)malloc(LOG * m * sizeof(int));\n\
        \    for (int i = 0; i < m; i++) {\n        int target_val = sorted_nums[i]\
        \ + maxDiff;\n        int idx = upper_bound(sorted_nums, m, target_val) - 1;\n\
        \        jump[0 * m + i] = idx;\n    }\n\n    for (int k = 1; k < LOG; k++)\
        \ {\n        for (int i = 0; i < m; i++) {\n            jump[k * m + i] = jump[(k\
        \ - 1) * m + jump[(k - 1) * m + i]];\n        }\n    }\n\n    *returnSize =\
        \ queriesSize;\n    int* results = (int*)malloc(queriesSize * sizeof(int));\n\
        \    for (int i = 0; i < queriesSize; i++) {\n        int u = queries[i][0];\n\
        \        int v = queries[i][1];\n        if (u == v) {\n            results[i]\
        \ = 0;\n            continue;\n        }\n        if (nums[u] == nums[v]) {\n\
        \            results[i] = 1;\n            continue;\n        }\n\n        int\
        \ val_u = nums[u], val_v = nums[v];\n        if (val_u > val_v) {\n        \
        \    int temp = val_u;\n            val_u = val_v;\n            val_v = temp;\n\
        \        }\n\n        int curr = get_idx(sorted_nums, m, val_u);\n        int\
        \ target = get_idx(sorted_nums, m, val_v);\n        int steps = 0;\n       \
        \ for (int k = LOG - 1; k >= 0; k--) {\n            if (jump[k * m + curr] <\
        \ target) {\n                curr = jump[k * m + curr];\n                steps\
        \ += (1 << k);\n            }\n        }\n\n        if (jump[0 * m + curr] >=\
        \ target) {\n            results[i] = steps + 1;\n        } else {\n       \
        \     results[i] = -1;\n        }\n    }\n\n    free(jump);\n    free(sorted_nums);\n\
        \    return results;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\nusing System.Linq;\n\
        \npublic class Solution {\n    public int[] PathExistenceQueries(int n, int[]\
        \ nums, int maxDiff, int[][] queries) {\n        int[] uniqueVals = nums.Distinct().ToArray();\n\
        \        Array.Sort(uniqueVals);\n        int m = uniqueVals.Length;\n     \
        \   int LOG = 18;\n\n        int[,] jump = new int[LOG, m];\n        for (int\
        \ i = 0; i < m; i++) {\n            int targetVal = uniqueVals[i] + maxDiff;\n\
        \            int idx = Array.BinarySearch(uniqueVals, targetVal);\n        \
        \    if (idx < 0) idx = ~idx - 1;\n            jump[0, i] = idx;\n        }\n\
        \n        for (int k = 1; k < LOG; k++) {\n            for (int i = 0; i < m;\
        \ i++) {\n                jump[k, i] = jump[k - 1, jump[k - 1, i]];\n      \
        \      }\n        }\n\n        int[] results = new int[queries.Length];\n  \
        \      for (int i = 0; i < queries.Length; i++) {\n            int u = queries[i][0];\n\
        \            int v = queries[i][1];\n            if (u == v) {\n           \
        \     results[i] = 0;\n                continue;\n            }\n          \
        \  if (nums[u] == nums[v]) {\n                results[i] = 1;\n            \
        \    continue;\n            }\n\n            int valU = nums[u], valV = nums[v];\n\
        \            if (valU > valV) {\n                int temp = valU;\n        \
        \        valU = valV;\n                valV = temp;\n            }\n\n     \
        \       int curr = Array.BinarySearch(uniqueVals, valU);\n            int target\
        \ = Array.BinarySearch(uniqueVals, valV);\n            int steps = 0;\n    \
        \        for (int k = LOG - 1; k >= 0; k--) {\n                if (jump[k, curr]\
        \ < target) {\n                    curr = jump[k, curr];\n                 \
        \   steps += (1 << k);\n                }\n            }\n\n            if (jump[0,\
        \ curr] >= target) {\n                results[i] = steps + 1;\n            }\
        \ else {\n                results[i] = -1;\n            }\n        }\n\n   \
        \     return results;\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @param {number[]} nums\n * @param {number}\
        \ maxDiff\n * @param {number[][]} queries\n * @return {number[]}\n */\nvar pathExistenceQueries\
        \ = function(n, nums, maxDiff, queries) {\n    let uniqueVals = Array.from(new\
        \ Set(nums)).sort((a, b) => a - b);\n    let m = uniqueVals.length;\n    const\
        \ LOG = 18;\n\n    let jump = new Int32Array(LOG * m);\n\n    function upperBound(arr,\
        \ val) {\n        let low = 0, high = arr.length;\n        while (low < high)\
        \ {\n            let mid = (low + high) >>> 1;\n            if (arr[mid] <=\
        \ val) low = mid + 1;\n            else high = mid;\n        }\n        return\
        \ low;\n    }\n\n    function getIdx(arr, val) {\n        let low = 0, high\
        \ = arr.length - 1;\n        while (low <= high) {\n            let mid = (low\
        \ + high) >>> 1;\n            if (arr[mid] === val) return mid;\n          \
        \  if (arr[mid] < val) low = mid + 1;\n            else high = mid - 1;\n  \
        \      }\n        return -1;\n    }\n\n    for (let i = 0; i < m; i++) {\n \
        \       let targetVal = uniqueVals[i] + maxDiff;\n        let idx = upperBound(uniqueVals,\
        \ targetVal) - 1;\n        jump[0 * m + i] = idx;\n    }\n\n    for (let k =\
        \ 1; k < LOG; k++) {\n        for (let i = 0; i < m; i++) {\n            jump[k\
        \ * m + i] = jump[(k - 1) * m + jump[(k - 1) * m + i]];\n        }\n    }\n\n\
        \    let results = new Int32Array(queries.length);\n    for (let i = 0; i <\
        \ queries.length; i++) {\n        let u = queries[i][0];\n        let v = queries[i][1];\n\
        \        if (u === v) {\n            results[i] = 0;\n            continue;\n\
        \        }\n        if (nums[u] === nums[v]) {\n            results[i] = 1;\n\
        \            continue;\n        }\n\n        let valU = nums[u], valV = nums[v];\n\
        \        if (valU > valV) {\n            [valU, valV] = [valV, valU];\n    \
        \    }\n\n        let curr = getIdx(uniqueVals, valU);\n        let target =\
        \ getIdx(uniqueVals, valV);\n        let steps = 0;\n        for (let k = LOG\
        \ - 1; k >= 0; k--) {\n            if (jump[k * m + curr] < target) {\n    \
        \            curr = jump[k * m + curr];\n                steps += (1 << k);\n\
        \            }\n        }\n\n        if (jump[0 * m + curr] >= target) {\n \
        \           results[i] = steps + 1;\n        } else {\n            results[i]\
        \ = -1;\n        }\n    }\n\n    return Array.from(results);\n};"
      typescript: "function pathExistenceQueries(n: number, nums: number[], maxDiff:\
        \ number, queries: number[][]): number[] {\n    const unique = Array.from(new\
        \ Set(nums)).sort((a, b) => a - b);\n    const nU = unique.length;\n    const\
        \ valToIdx = new Map<number, number>();\n    for (let i = 0; i < nU; i++) {\n\
        \        valToIdx.set(unique[i], i);\n    }\n\n    const gaps = new Int32Array(nU);\n\
        \    gaps[0] = 0;\n    for (let i = 0; i < nU - 1; i++) {\n        gaps[i +\
        \ 1] = gaps[i] + (unique[i + 1] - unique[i] > maxDiff ? 1 : 0);\n    }\n\n \
        \   const LOG = 17;\n    const jump = new Int32Array(LOG * nU);\n    let r =\
        \ 0;\n    for (let i = 0; i < nU; i++) {\n        while (r + 1 < nU && unique[r\
        \ + 1] <= unique[i] + maxDiff) {\n            r++;\n        }\n        jump[i]\
        \ = r;\n    }\n\n    for (let p = 1; p < LOG; p++) {\n        const offset =\
        \ p * nU;\n        const prevOffset = (p - 1) * nU;\n        for (let i = 0;\
        \ i < nU; i++) {\n            const mid = jump[prevOffset + i];\n          \
        \  jump[offset + i] = jump[prevOffset + mid];\n        }\n    }\n\n    const\
        \ results: number[] = [];\n    for (const [u, v] of queries) {\n        if (u\
        \ === v) {\n            results.push(0);\n            continue;\n        }\n\
        \        const valU = nums[u];\n        const valV = nums[v];\n        const\
        \ diff = Math.abs(valU - valV);\n        if (diff <= maxDiff) {\n          \
        \  results.push(1);\n            continue;\n        }\n\n        const idxU\
        \ = valToIdx.get(valU)!;\n        const idxV = valToIdx.get(valV)!;\n      \
        \  const startIdx = Math.min(idxU, idxV);\n        const endIdx = Math.max(idxU,\
        \ idxV);\n\n        if (gaps[endIdx] - gaps[startIdx] > 0) {\n            results.push(-1);\n\
        \            continue;\n        }\n\n        let dist = 0;\n        let curr\
        \ = startIdx;\n        for (let p = LOG - 1; p >= 0; p--) {\n            const\
        \ next = jump[p * nU + curr];\n            if (next < endIdx) {\n          \
        \      curr = next;\n                dist += (1 << p);\n            }\n    \
        \    }\n        results.push(dist + 1);\n    }\n    return results;\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @param Integer[]\
        \ $nums\n     * @param Integer $maxDiff\n     * @param Integer[][] $queries\n\
        \     * @return Integer[]\n     */\n    function pathExistenceQueries($n, $nums,\
        \ $maxDiff, $queries) {\n        $unique = array_unique($nums);\n        sort($unique);\n\
        \        $unique = array_values($unique);\n        $nU = count($unique);\n \
        \       $valToIdx = [];\n        foreach ($unique as $i => $val) {\n       \
        \     $valToIdx[$val] = $i;\n        }\n\n        $gaps = new SplFixedArray($nU);\n\
        \        $gaps[0] = 0;\n        for ($i = 0; $i < $nU - 1; $i++) {\n       \
        \     $gaps[$i + 1] = $gaps[$i] + ($unique[$i + 1] - $unique[$i] > $maxDiff\
        \ ? 1 : 0);\n        }\n\n        $LOG = 17;\n        $jump = [];\n        for\
        \ ($p = 0; $p < $LOG; $p++) {\n            $jump[$p] = new SplFixedArray($nU);\n\
        \        }\n\n        $r = 0;\n        for ($i = 0; $i < $nU; $i++) {\n    \
        \        while ($r + 1 < $nU && $unique[$r + 1] <= $unique[$i] + $maxDiff) {\n\
        \                $r++;\n            }\n            $jump[0][$i] = $r;\n    \
        \    }\n\n        for ($p = 1; $p < $LOG; $p++) {\n            for ($i = 0;\
        \ $i < $nU; $i++) {\n                $mid = $jump[$p - 1][$i];\n           \
        \     $jump[$p][$i] = $jump[$p - 1][$mid];\n            }\n        }\n\n   \
        \     $ans = [];\n        foreach ($queries as $q) {\n            $u = $q[0];\n\
        \            $v = $q[1];\n            if ($u == $v) {\n                $ans[]\
        \ = 0;\n                continue;\n            }\n            $valU = $nums[$u];\n\
        \            $valV = $nums[$v];\n            if (abs($valU - $valV) <= $maxDiff)\
        \ {\n                $ans[] = 1;\n                continue;\n            }\n\
        \n            $idxU = $valToIdx[$valU];\n            $idxV = $valToIdx[$valV];\n\
        \            $start = $idxU < $idxV ? $idxU : $idxV;\n            $end = $idxU\
        \ > $idxV ? $idxU : $idxV;\n\n            if ($gaps[$end] - $gaps[$start] >\
        \ 0) {\n                $ans[] = -1;\n                continue;\n          \
        \  }\n\n            $dist = 0;\n            $curr = $start;\n            for\
        \ ($p = $LOG - 1; $p >= 0; $p--) {\n                if ($jump[$p][$curr] < $end)\
        \ {\n                    $curr = $jump[$p][$curr];\n                    $dist\
        \ += (1 << $p);\n                }\n            }\n            $ans[] = $dist\
        \ + 1;\n        }\n        return $ans;\n    }\n}"
      swift: "class Solution {\n    func pathExistenceQueries(_ n: Int, _ nums: [Int],\
        \ _ maxDiff: Int, _ queries: [[Int]]) -> [Int] {\n        let unique = Array(Set(nums)).sorted()\n\
        \        let nU = unique.count\n        var valToIdx = [Int: Int]()\n      \
        \  for i in 0..<nU {\n            valToIdx[unique[i]] = i\n        }\n\n   \
        \     var gaps = [Int](repeating: 0, count: nU)\n        for i in 0..<nU - 1\
        \ {\n            gaps[i + 1] = gaps[i] + (unique[i + 1] - unique[i] > maxDiff\
        \ ? 1 : 0)\n        }\n\n        let LOG = 17\n        var jump = [Int](repeating:\
        \ 0, count: LOG * nU)\n        var r = 0\n        for i in 0..<nU {\n      \
        \      while r + 1 < nU && unique[r + 1] <= unique[i] + maxDiff {\n        \
        \        r += 1\n            }\n            jump[i] = r\n        }\n\n     \
        \   for p in 1..<LOG {\n            let offset = p * nU\n            let prevOffset\
        \ = (p - 1) * nU\n            for i in 0..<nU {\n                let mid = jump[prevOffset\
        \ + i]\n                jump[offset + i] = jump[prevOffset + mid]\n        \
        \    }\n        }\n\n        var results = [Int]()\n        results.reserveCapacity(queries.count)\n\
        \        for q in queries {\n            let u = q[0]\n            let v = q[1]\n\
        \            if u == v {\n                results.append(0)\n              \
        \  continue\n            }\n            let valU = nums[u]\n            let\
        \ valV = nums[v]\n            if abs(valU - valV) <= maxDiff {\n           \
        \     results.append(1)\n                continue\n            }\n         \
        \   guard let idxU = valToIdx[valU], let idxV = valToIdx[valV] else {\n    \
        \            results.append(-1)\n                continue\n            }\n \
        \           let startIdx = min(idxU, idxV)\n            let endIdx = max(idxU,\
        \ idxV)\n\n            if gaps[endIdx] - gaps[startIdx] > 0 {\n            \
        \    results.append(-1)\n                continue\n            }\n\n       \
        \     var dist = 0\n            var curr = startIdx\n            for p in (0..<LOG).reversed()\
        \ {\n                let next = jump[p * nU + curr]\n                if next\
        \ < endIdx {\n                    curr = next\n                    dist += (1\
        \ << p)\n                }\n            }\n            results.append(dist +\
        \ 1)\n        }\n        return results\n    }\n}"
      kotlin: "import java.util.*\nimport kotlin.math.*\n\nclass Solution {\n    fun\
        \ pathExistenceQueries(n: Int, nums: IntArray, maxDiff: Int, queries: Array<IntArray>):\
        \ IntArray {\n        val unique = nums.distinct().toIntArray()\n        unique.sort()\n\
        \        val nU = unique.size\n        val valToIdx = mutableMapOf<Int, Int>()\n\
        \        for (i in unique.indices) {\n            valToIdx[unique[i]] = i\n\
        \        }\n\n        val gaps = IntArray(nU)\n        for (i in 0 until nU\
        \ - 1) {\n            gaps[i + 1] = gaps[i] + if (unique[i + 1] - unique[i]\
        \ > maxDiff) 1 else 0\n        }\n\n        val LOG = 17\n        val jump =\
        \ Array(LOG) { IntArray(nU) }\n        var r = 0\n        for (i in 0 until\
        \ nU) {\n            while (r + 1 < nU && unique[r + 1] <= unique[i] + maxDiff)\
        \ {\n                r++\n            }\n            jump[0][i] = r\n      \
        \  }\n\n        for (p in 1 until LOG) {\n            for (i in 0 until nU)\
        \ {\n                val mid = jump[p - 1][i]\n                jump[p][i] =\
        \ jump[p - 1][mid]\n            }\n        }\n\n        val results = IntArray(queries.size)\n\
        \        for (i in queries.indices) {\n            val u = queries[i][0]\n \
        \           val v = queries[i][1]\n            if (u == v) {\n             \
        \   results[i] = 0\n                continue\n            }\n            val\
        \ valU = nums[u]\n            val valV = nums[v]\n            if (abs(valU -\
        \ valV) <= maxDiff) {\n                results[i] = 1\n                continue\n\
        \            }\n\n            val idxU = valToIdx[valU]!!\n            val idxV\
        \ = valToIdx[valV]!!\n            val startIdx = min(idxU, idxV)\n         \
        \   val endIdx = max(idxU, idxV)\n\n            if (gaps[endIdx] - gaps[startIdx]\
        \ > 0) {\n                results[i] = -1\n                continue\n      \
        \      }\n\n            var dist = 0\n            var curr = startIdx\n    \
        \        for (p in LOG - 1 downTo 0) {\n                if (jump[p][curr] <\
        \ endIdx) {\n                    curr = jump[p][curr]\n                    dist\
        \ += (1 shl p)\n                }\n            }\n            results[i] = dist\
        \ + 1\n        }\n        return results\n    }\n}"
      dart: "class Solution {\n  List<int> pathExistenceQueries(int n, List<int> nums,\
        \ int maxDiff, List<List<int>> queries) {\n    List<int> sortedUnique = nums.toSet().toList()..sort();\n\
        \    int m = sortedUnique.length;\n\n    List<int> comp = List.filled(m, 0);\n\
        \    for (int i = 1; i < m; i++) {\n      if (sortedUnique[i] - sortedUnique[i\
        \ - 1] <= maxDiff) {\n        comp[i] = comp[i - 1];\n      } else {\n     \
        \   comp[i] = comp[i - 1] + 1;\n      }\n    }\n\n    List<List<int>> jump =\
        \ List.generate(m, (_) => List.filled(17, 0));\n    for (int i = 0; i < m; i++)\
        \ {\n      int target = sortedUnique[i] + maxDiff;\n      int low = 0, high\
        \ = m;\n      while (low < high) {\n        int mid = low + ((high - low) ~/\
        \ 2);\n        if (sortedUnique[mid] <= target) low = mid + 1;\n        else\
        \ high = mid;\n      }\n      jump[i][0] = low - 1;\n    }\n\n    for (int k\
        \ = 1; k < 17; k++) {\n      for (int i = 0; i < m; i++) {\n        jump[i][k]\
        \ = jump[jump[i][k - 1]][k - 1];\n      }\n    }\n\n    int findIdx(int val)\
        \ {\n      int low = 0, high = m - 1;\n      while (low <= high) {\n       \
        \ int mid = low + ((high - low) ~/ 2);\n        if (sortedUnique[mid] == val)\
        \ return mid;\n        if (sortedUnique[mid] < val) low = mid + 1;\n       \
        \ else high = mid - 1;\n      }\n      return -1;\n    }\n\n    List<int> results\
        \ = List.filled(queries.length, 0);\n    for (int i = 0; i < queries.length;\
        \ i++) {\n      int u = queries[i][0];\n      int v = queries[i][1];\n     \
        \ if (u == v) {\n        results[i] = 0;\n        continue;\n      }\n     \
        \ if (nums[u] == nums[v]) {\n        results[i] = 1;\n        continue;\n  \
        \    }\n\n      int idxX = findIdx(nums[u]);\n      int idxY = findIdx(nums[v]);\n\
        \      if (idxX > idxY) {\n        int temp = idxX;\n        idxX = idxY;\n\
        \        idxY = temp;\n      }\n\n      if (comp[idxX] != comp[idxY]) {\n  \
        \      results[i] = -1;\n      } else {\n        int current = idxX;\n     \
        \   int steps = 0;\n        for (int k = 16; k >= 0; k--) {\n          if (jump[current][k]\
        \ < idxY) {\n            current = jump[current][k];\n            steps += (1\
        \ << k);\n          }\n        }\n        results[i] = steps + 1;\n      }\n\
        \    }\n    return results;\n  }\n}"
      go: "func pathExistenceQueries(n int, nums []int, maxDiff int, queries [][]int)\
        \ []int {\n    v := make([]int, len(nums))\n    copy(v, nums)\n    sort.Ints(v)\n\
        \n    m := 0\n    if len(v) > 0 {\n        for i := 1; i < len(v); i++ {\n \
        \           if v[i] != v[m] {\n                m++\n                v[m] = v[i]\n\
        \            }\n        }\n        v = v[:m+1]\n    }\n    m = len(v)\n\n  \
        \  comp := make([]int, m)\n    for i := 1; i < m; i++ {\n        if v[i]-v[i-1]\
        \ <= maxDiff {\n            comp[i] = comp[i-1]\n        } else {\n        \
        \    comp[i] = comp[i-1] + 1\n        }\n    }\n\n    jump := make([][17]int,\
        \ m)\n    for i := 0; i < m; i++ {\n        target := v[i] + maxDiff\n     \
        \   idx := sort.Search(m, func(j int) bool {\n            return v[j] > target\n\
        \        }) - 1\n        jump[i][0] = idx\n    }\n\n    for k := 1; k < 17;\
        \ k++ {\n        for i := 0; i < m; i++ {\n            jump[i][k] = jump[jump[i][k-1]][k-1]\n\
        \        }\n    }\n\n    pos := make(map[int]int)\n    for i, val := range v\
        \ {\n        pos[val] = i\n    }\n\n    ans := make([]int, len(queries))\n \
        \   for i, q := range queries {\n        u, v_idx := q[0], q[1]\n        if\
        \ u == v_idx {\n            ans[i] = 0\n            continue\n        }\n  \
        \      if nums[u] == nums[v_idx] {\n            ans[i] = 1\n            continue\n\
        \        }\n\n        idxX := pos[nums[u]]\n        idxY := pos[nums[v_idx]]\n\
        \        if idxX > idxY {\n            idxX, idxY = idxY, idxX\n        }\n\n\
        \        if comp[idxX] != comp[idxY] {\n            ans[i] = -1\n        } else\
        \ {\n            current := idxX\n            steps := 0\n            for k\
        \ := 16; k >= 0; k-- {\n                if jump[current][k] < idxY {\n     \
        \               current = jump[current][k]\n                    steps += (1\
        \ << k)\n                }\n            }\n            ans[i] = steps + 1\n\
        \        }\n    }\n\n    return ans\n}"
      ruby: "def path_existence_queries(n, nums, max_diff, queries)\n  v = nums.uniq.sort\n\
        \  m = v.size\n  pos = {}\n  v.each_with_index { |val, idx| pos[val] = idx }\n\
        \n  comp = Array.new(m, 0)\n  (1...m).each do |i|\n    if v[i] - v[i - 1] <=\
        \ max_diff\n      comp[i] = comp[i - 1]\n    else\n      comp[i] = comp[i -\
        \ 1] + 1\n    end\n  end\n\n  jump = Array.new(m * 17)\n  (0...m).each do |i|\n\
        \    target = v[i] + max_diff\n    idx = v.bsearch_index { |x| x > target }\
        \ || m\n    jump[i * 17 + 0] = idx - 1\n  end\n\n  (1..16).each do |k|\n   \
        \ (0...m).each do |i|\n      mid = jump[i * 17 + k - 1]\n      jump[i * 17 +\
        \ k] = jump[mid * 17 + k - 1]\n    end\n  end\n\n  ans = Array.new(queries.size)\n\
        \  queries.each_with_index do |q, i|\n    u, node_v = q[0], q[1]\n    if u ==\
        \ node_v\n      ans[i] = 0\n      next\n    end\n    if nums[u] == nums[node_v]\n\
        \      ans[i] = 1\n      next\n    end\n\n    idx_x = pos[nums[u]]\n    idx_y\
        \ = pos[nums[node_v]]\n    idx_x, idx_y = idx_y, idx_x if idx_x > idx_y\n\n\
        \    if comp[idx_x] != comp[idx_y]\n      ans[i] = -1\n    else\n      current\
        \ = idx_x\n      steps = 0\n      (16).step(0, -1).each do |k|\n        jump_idx\
        \ = jump[current * 17 + k]\n        if jump_idx < idx_y\n          current =\
        \ jump_idx\n          steps += (1 << k)\n        end\n      end\n      ans[i]\
        \ = steps + 1\n    end\n  end\n  ans\nend"
      scala: "object Solution {\n  import scala.collection.mutable\n\n  def pathExistenceQueries(n:\
        \ Int, nums: Array[Int], maxDiff: Int, queries: Array[Array[Int]]): Array[Int]\
        \ = {\n    val v = nums.distinct.sorted\n    val m = v.length\n\n    val comp\
        \ = new Array[Int](m)\n    var i = 1\n    while (i < m) {\n      if (v(i) -\
        \ v(i - 1) <= maxDiff) {\n        comp(i) = comp(i - 1)\n      } else {\n  \
        \      comp(i) = comp(i - 1) + 1\n      }\n      i += 1\n    }\n\n    val jump\
        \ = Array.ofDim[Int](m, 17)\n    i = 0\n    while (i < m) {\n      val target\
        \ = v(i) + maxDiff\n      var low = 0\n      var high = m\n      while (low\
        \ < high) {\n        val mid = low + (high - low) / 2\n        if (v(mid) <=\
        \ target) low = mid + 1\n        else high = mid\n      }\n      jump(i)(0)\
        \ = low - 1\n      i += 1\n    }\n\n    for (k <- 1 until 17) {\n      for (j\
        \ <- 0 until m) {\n        jump(j)(k) = jump(jump(j)(k - 1))(k - 1)\n      }\n\
        \    }\n\n    val results = new Array[Int](queries.length)\n    var qIdx = 0\n\
        \    while (qIdx < queries.length) {\n      val u = queries(qIdx)(0)\n     \
        \ val nV = queries(qIdx)(1)\n      if (u == nV) {\n        results(qIdx) = 0\n\
        \      } else if (nums(u) == nums(nV)) {\n        results(qIdx) = 1\n      }\
        \ else {\n        var idxX = java.util.Arrays.binarySearch(v, nums(u))\n   \
        \     var idxY = java.util.Arrays.binarySearch(v, nums(nV))\n        if (idxX\
        \ > idxY) {\n          val temp = idxX\n          idxX = idxY\n          idxY\
        \ = temp\n        }\n\n        if (comp(idxX) != comp(idxY)) {\n          results(qIdx)\
        \ = -1\n        } else {\n          var current = idxX\n          var steps\
        \ = 0\n          for (k <- 16 to 0 by -1) {\n            if (jump(current)(k)\
        \ < idxY) {\n              current = jump(current)(k)\n              steps +=\
        \ (1 << k)\n            }\n          }\n          results(qIdx) = steps + 1\n\
        \        }\n      }\n      qIdx += 1\n    }\n    results\n  }\n}"
      rust: "impl Solution {\n    pub fn path_existence_queries(n: i32, nums: Vec<i32>,\
        \ max_diff: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {\n        let n = n as\
        \ usize;\n        let mut p: Vec<usize> = (0..n).collect();\n        p.sort_by(|&a,\
        \ &b| {\n            if nums[a] == nums[b] {\n                a.cmp(&b)\n  \
        \          } else {\n                nums[a].cmp(&nums[b])\n            }\n\
        \        });\n\n        let mut sorted_nums = vec![0; n];\n        let mut sorted_idx\
        \ = vec![0; n];\n        for i in 0..n {\n            sorted_nums[i] = nums[p[i]];\n\
        \            sorted_idx[p[i]] = i;\n        }\n\n        let mut jump_l = vec![vec![0;\
        \ n]; 17];\n        let mut jump_r = vec![vec![0; n]; 17];\n\n        let mut\
        \ l_ptr = 0;\n        for i in 0..n {\n            while sorted_nums[i] - sorted_nums[l_ptr]\
        \ > max_diff {\n                l_ptr += 1;\n            }\n            jump_l[0][i]\
        \ = l_ptr;\n        }\n\n        let mut r_ptr = 0;\n        for i in 0..n {\n\
        \            while r_ptr + 1 < n && sorted_nums[r_ptr + 1] - sorted_nums[i]\
        \ <= max_diff {\n                r_ptr += 1;\n            }\n            jump_r[0][i]\
        \ = r_ptr;\n        }\n\n        for k in 1..17 {\n            for i in 0..n\
        \ {\n                jump_l[k][i] = jump_l[k - 1][jump_l[k - 1][i]];\n     \
        \           jump_r[k][i] = jump_r[k - 1][jump_r[k - 1][i]];\n            }\n\
        \        }\n\n        let mut answer = Vec::with_capacity(queries.len());\n\
        \        for q in queries {\n            let u = q[0] as usize;\n          \
        \  let v = q[1] as usize;\n            if u == v {\n                answer.push(0);\n\
        \                continue;\n            }\n\n            let i = sorted_idx[u];\n\
        \            let j = sorted_idx[v];\n\n            if i < j {\n            \
        \    if jump_r[16][i] < j {\n                    answer.push(-1);\n        \
        \        } else {\n                    let mut curr = i;\n                 \
        \   let mut dist = 0;\n                    for k in (0..17).rev() {\n      \
        \                  if jump_r[k][curr] < j {\n                            curr\
        \ = jump_r[k][curr];\n                            dist += 1 << k;\n        \
        \                }\n                    }\n                    answer.push(dist\
        \ + 1);\n                }\n            } else {\n                if jump_l[16][i]\
        \ > j {\n                    answer.push(-1);\n                } else {\n  \
        \                  let mut curr = i;\n                    let mut dist = 0;\n\
        \                    for k in (0..17).rev() {\n                        if jump_l[k][curr]\
        \ > j {\n                            curr = jump_l[k][curr];\n             \
        \               dist += 1 << k;\n                        }\n               \
        \     }\n                    answer.push(dist + 1);\n                }\n   \
        \         }\n        }\n        answer\n    }\n}"
      racket: "(define/contract (path-existence-queries n nums maxDiff queries)\n  (->\
        \ exact-integer? (listof exact-integer?) exact-integer? (listof (listof exact-integer?))\
        \ (listof exact-integer?))\n  (let* ([nums-vec (list->vector nums)]\n      \
        \   [nodes (sort (range n)\n                      (lambda (i j)\n          \
        \              (let ([vi (vector-ref nums-vec i)]\n                        \
        \      [vj (vector-ref nums-vec j)])\n                          (if (= vi vj)\
        \ (< i j) (< vi vj)))))]\n         [sorted-nums (for/vector ([i nodes]) (vector-ref\
        \ nums-vec i))]\n         [sorted-idx (make-vector n)]\n         [_ (for ([pos\
        \ (in-range n)] [orig nodes]) (vector-set! sorted-idx orig pos))]\n        \
        \ [jumpL (make-vector 17)]\n         [jumpR (make-vector 17)])\n    (vector-set!\
        \ jumpL 0\n                 (let ([l-res (make-vector n)] [l-ptr 0])\n     \
        \              (for ([i (in-range n)])\n                     (while (> (- (vector-ref\
        \ sorted-nums i) (vector-ref sorted-nums l-ptr)) maxDiff)\n                \
        \            (set! l-ptr (+ l-ptr 1)))\n                     (vector-set! l-res\
        \ i l-ptr))\n                   l-res))\n    (vector-set! jumpR 0\n        \
        \         (let ([r-res (make-vector n)] [r-ptr 0])\n                   (for\
        \ ([i (in-range n)])\n                     (while (and (< (+ r-ptr 1) n) (<=\
        \ (- (vector-ref sorted-nums (+ r-ptr 1)) (vector-ref sorted-nums i)) maxDiff))\n\
        \                            (set! r-ptr (+ r-ptr 1)))\n                   \
        \  (vector-set! r-res i r-ptr))\n                   r-res))\n    (for ([k (in-range\
        \ 1 17)])\n      (let* ([prevL (vector-ref jumpL (- k 1))]\n             [prevR\
        \ (vector-ref jumpR (- k 1))]\n             [currL (make-vector n)]\n      \
        \       [currR (make-vector n)])\n        (for ([i (in-range n)])\n        \
        \  (vector-set! currL i (vector-ref prevL (vector-ref prevL i)))\n         \
        \ (vector-set! currR i (vector-ref prevR (vector-ref prevR i))))\n        (vector-set!\
        \ jumpL k currL)\n        (vector-set! jumpR k currR)))\n    (map (lambda (q)\n\
        \           (let ([u (car q)] [v (cadr q)])\n             (if (= u v) 0\n  \
        \               (let ([i (vector-ref sorted-idx u)] [j (vector-ref sorted-idx\
        \ v)])\n                   (if (< i j)\n                       (if (< (vector-ref\
        \ (vector-ref jumpR 16) i) j) -1\n                           (let-values ([(curr\
        \ dist)\n                                         (for/fold ([c i] [d 0]) ([k\
        \ (in-range 16 -1 -1)])\n                                           (let ([next\
        \ (vector-ref (vector-ref jumpR k) c)])\n                                  \
        \           (if (< next j) (values next (+ d (arithmetic-shift 1 k))) (values\
        \ c d))))])\n                             (+ dist 1)))\n                   \
        \    (if (> (vector-ref (vector-ref jumpL 16) i) j) -1\n                   \
        \        (let-values ([(curr dist)\n                                       \
        \  (for/fold ([c i] [d 0]) ([k (in-range 16 -1 -1)])\n                     \
        \                      (let ([next (vector-ref (vector-ref jumpL k) c)])\n \
        \                                            (if (> next j) (values next (+\
        \ d (arithmetic-shift 1 k))) (values c d))))])\n                           \
        \  (+ dist 1))))))))\n         queries)))\n\n(define-syntax-rule (while condition\
        \ body ...)\n  (let loop () (when condition body ... (loop))))"
      erlang: "-spec path_existence_queries(N :: integer(), Nums :: [integer()], MaxDiff\
        \ :: integer(), Queries :: [[integer()]]) -> [integer()].\npath_existence_queries(N,\
        \ Nums, MaxDiff, Queries) ->\n  IndexedNums = lists:zip(Nums, lists:seq(0, N\
        \ - 1)),\n  SortedWithIdx = lists:sort(IndexedNums),\n  SortedNums = list_to_tuple([V\
        \ || {V, _} <- SortedWithIdx]),\n  SortedIdxMap = lists:sort([{OrigIdx, Pos}\
        \ || {{_, OrigIdx}, Pos} <- lists:zip(SortedWithIdx, lists:seq(0, N - 1))]),\n\
        \  SortedIdx = list_to_tuple([Pos || {_, Pos} <- SortedIdxMap]),\n\n  L0 = list_to_tuple(compute_l(0,\
        \ 0, SortedNums, MaxDiff, N, [])),\n  R0 = list_to_tuple(compute_r(0, 0, SortedNums,\
        \ MaxDiff, N, [])),\n\n  {JumpL, JumpR} = build_jump_tables(1, L0, R0, N, [L0],\
        \ [R0]),\n\n  [process_query(Q, SortedIdx, JumpL, JumpR) || Q <- Queries].\n\
        \ncompute_l(N, _, _, _, N, Acc) -> lists:reverse(Acc);\ncompute_l(I, LPtr, SortedNums,\
        \ MaxDiff, N, Acc) ->\n  ValI = element(I + 1, SortedNums),\n  NewLPtr = find_lptr(LPtr,\
        \ ValI, SortedNums, MaxDiff),\n  compute_l(I + 1, NewLPtr, SortedNums, MaxDiff,\
        \ N, [NewLPtr | Acc]).\n\nfind_lptr(LPtr, ValI, SortedNums, MaxDiff) ->\n  ValL\
        \ = element(LPtr + 1, SortedNums),\n  if ValI - ValL > MaxDiff -> find_lptr(LPtr\
        \ + 1, ValI, SortedNums, MaxDiff);\n     true -> LPtr\n  end.\n\ncompute_r(N,\
        \ _, _, _, N, Acc) -> lists:reverse(Acc);\ncompute_r(I, RPtr, SortedNums, MaxDiff,\
        \ N, Acc) ->\n  ValI = element(I + 1, SortedNums),\n  NewRPtr = find_rptr(RPtr,\
        \ ValI, SortedNums, MaxDiff, N),\n  compute_r(I + 1, NewRPtr, SortedNums, MaxDiff,\
        \ N, [NewRPtr | Acc]).\n\nfind_rptr(RPtr, ValI, SortedNums, MaxDiff, N) ->\n\
        \  if RPtr + 1 < N ->\n       ValNext = element(RPtr + 2, SortedNums),\n   \
        \    if ValNext - ValI =< MaxDiff -> find_rptr(RPtr + 1, ValI, SortedNums, MaxDiff,\
        \ N);\n          true -> RPtr\n       end;\n     true -> RPtr\n  end.\n\nbuild_jump_tables(17,\
        \ _, _, _, AccL, AccR) -> {list_to_tuple(lists:reverse(AccL)), list_to_tuple(lists:reverse(AccR))};\n\
        build_jump_tables(K, PrevL, PrevR, N, AccL, AccR) ->\n  CurrL = list_to_tuple([element(element(I,\
        \ PrevL) + 1, PrevL) || I <- lists:seq(1, N)]),\n  CurrR = list_to_tuple([element(element(I,\
        \ PrevR) + 1, PrevR) || I <- lists:seq(1, N)]),\n  build_jump_tables(K + 1,\
        \ CurrL, CurrR, N, [CurrL | AccL], [CurrR | AccR]).\n\nprocess_query([U, V],\
        \ SortedIdx, JumpL, JumpR) ->\n  if U == V -> 0;\n     true ->\n       I = element(U\
        \ + 1, SortedIdx),\n       J = element(V + 1, SortedIdx),\n       if I < J ->\n\
        \            MaxReachable = element(I + 1, element(17, JumpR)),\n          \
        \  if MaxReachable < J -> -1;\n               true -> jump_dist(16, I, J, JumpR,\
        \ 0) + 1\n            end;\n          true ->\n            MinReachable = element(I\
        \ + 1, element(17, JumpL)),\n            if MinReachable > J -> -1;\n      \
        \         true -> jump_dist_l(16, I, J, JumpL, 0) + 1\n            end\n   \
        \    end\n  end.\n\njump_dist(-1, _, _, _, Dist) -> Dist;\njump_dist(K, Curr,\
        \ Target, Table, Dist) ->\n  Next = element(Curr + 1, element(K + 1, Table)),\n\
        \  if Next < Target -> jump_dist(K - 1, Next, Target, Table, Dist + (1 bsl K));\n\
        \     true -> jump_dist(K - 1, Curr, Target, Table, Dist)\n  end.\n\njump_dist_l(-1,\
        \ _, _, _, Dist) -> Dist;\njump_dist_l(K, Curr, Target, Table, Dist) ->\n  Next\
        \ = element(Curr + 1, element(K + 1, Table)),\n  if Next > Target -> jump_dist_l(K\
        \ - 1, Next, Target, Table, Dist + (1 bsl K));\n     true -> jump_dist_l(K -\
        \ 1, Curr, Target, Table, Dist)\n  end."
      elixir: "defmodule Solution do\n  import Bitwise\n\n  @spec path_existence_queries(n\
        \ :: integer, nums :: [integer], max_diff :: integer, queries :: [[integer]])\
        \ :: [integer]\n  def path_existence_queries(n, nums, max_diff, queries) do\n\
        \    nums_with_idx = Enum.with_index(nums)\n    sorted_with_idx = Enum.sort(nums_with_idx)\n\
        \    sorted_nums = sorted_with_idx |> Enum.map(fn {v, _} -> v end) |> List.to_tuple()\n\
        \n    sorted_idx_map = Enum.with_index(sorted_with_idx)\n      |> Enum.map(fn\
        \ {{_v, orig_idx}, pos} -> {orig_idx, pos} end)\n      |> Enum.sort()\n    \
        \  |> Enum.map(fn {_, pos} -> pos end)\n      |> List.to_tuple()\n\n    l0 =\
        \ compute_l(0, 0, sorted_nums, max_diff, n, []) |> List.to_tuple()\n    r0 =\
        \ compute_r(0, 0, sorted_nums, max_diff, n, []) |> List.to_tuple()\n\n    {jump_l,\
        \ jump_r} = build_jump_tables(1, l0, r0, n, [l0], [r0])\n\n    Enum.map(queries,\
        \ fn [u, v] ->\n      if u == v do\n        0\n      else\n        i = elem(sorted_idx_map,\
        \ u)\n        j = elem(sorted_idx_map, v)\n        if i < j do\n          if\
        \ elem(elem(jump_r, 16), i) < j do\n            -1\n          else\n       \
        \     jump_dist_r(16, i, j, jump_r, 0) + 1\n          end\n        else\n  \
        \        if elem(elem(jump_l, 16), i) > j do\n            -1\n          else\n\
        \            jump_dist_l(16, i, j, jump_l, 0) + 1\n          end\n        end\n\
        \      end\n    end)\n  end\n\n  defp compute_l(n, _lptr, _nums, _diff, n, acc),\
        \ do: Enum.reverse(acc)\n  defp compute_l(i, lptr, nums, diff, n, acc) do\n\
        \    val_i = elem(nums, i)\n    new_lptr = find_lptr(lptr, val_i, nums, diff)\n\
        \    compute_l(i + 1, new_lptr, nums, diff, n, [new_lptr | acc])\n  end\n\n\
        \  defp find_lptr(lptr, val_i, nums, diff) do\n    if val_i - elem(nums, lptr)\
        \ > diff do\n      find_lptr(lptr + 1, val_i, nums, diff)\n    else\n      lptr\n\
        \    end\n  end\n\n  defp compute_r(n, _rptr, _nums, _diff, n, acc), do: Enum.reverse(acc)\n\
        \  defp compute_r(i, rptr, nums, diff, n, acc) do\n    val_i = elem(nums, i)\n\
        \    new_rptr = find_rptr(rptr, val_i, nums, diff, n)\n    compute_r(i + 1,\
        \ new_rptr, nums, diff, n, [new_rptr | acc])\n  end\n\n  defp find_rptr(rptr,\
        \ val_i, nums, diff, n) do\n    if rptr + 1 < n and elem(nums, rptr + 1) - val_i\
        \ <= diff do\n      find_rptr(rptr + 1, val_i, nums, diff, n)\n    else\n  \
        \    rptr\n    end\n  end\n\n  defp build_jump_tables(17, _pl, _pr, _n, accl,\
        \ accr) do\n    {List.to_tuple(Enum.reverse(accl)), List.to_tuple(Enum.reverse(accr))}\n\
        \  end\n  defp build_jump_tables(k, pl, pr, n, accl, accr) do\n    cl = Enum.map(0..(n\
        \ - 1), fn i -> elem(pl, elem(pl, i)) end) |> List.to_tuple()\n    cr = Enum.map(0..(n\
        \ - 1), fn i -> elem(pr, elem(pr, i)) end) |> List.to_tuple()\n    build_jump_tables(k\
        \ + 1, cl, cr, n, [cl | accl], [cr | accr])\n  end\n\n  defp jump_dist_r(-1,\
        \ _curr, _target, _table, dist), do: dist\n  defp jump_dist_r(k, curr, target,\
        \ table, dist) do\n    next = elem(elem(table, k), curr)\n    if next < target\
        \ do\n      jump_dist_r(k - 1, next, target, table, dist + bsl(1, k))\n    else\n\
        \      jump_dist_r(k - 1, curr, target, table, dist)\n    end\n  end\n\n  defp\
        \ jump_dist_l(-1, _curr, _target, _table, dist), do: dist\n  defp jump_dist_l(k,\
        \ curr, target, table, dist) do\n    next = elem(elem(table, k), curr)\n   \
        \ if next > target do\n      jump_dist_l(k - 1, next, target, table, dist +\
        \ bsl(1, k))\n    else\n      jump_dist_l(k - 1, curr, target, table, dist)\n\
        \    end\n  end\nend"
    approach: 'The problem asks for the minimum unweighted distance between two nodes
      in a graph where an edge exists between nodes $i$ and $j$ if $|nums[i] - nums[j]|
      \le maxDiff$. Since we want the shortest path in an unweighted graph where connectivity
      is determined by numerical closeness, a greedy approach is optimal. If we want
      to reach node $v$ from node $u$ (assuming $nums[u] < nums[v]$), the most efficient
      path consists of repeatedly jumping to the node with the largest value that is
      within $maxDiff$ of the current node''s value until the target value $nums[v]$
      is reached or exceeded. If at any point the next largest available value doesn''t
      allow for further progress (a gap $> maxDiff$ exists), the nodes are disconnected.


      To implement this efficiently, we sort the unique values of $nums$ and use binary
      lifting (a sparse table). Let $U$ be the sorted unique values. We define $up[0][i]$
      as the index of the largest value in $U$ reachable from $U[i]$ in one step (i.e.,
      the largest $U[j] \le U[i] + maxDiff$). Using binary lifting, we pre-calculate
      $up[k][i]$ as the index reached after $2^k$ steps. For each query $(u, v)$, if
      $u = v$, the distance is 0. If $u \ne v$ and $nums[u] = nums[v]$, the distance
      is 1. Otherwise, we calculate the distance between their values using the sparse
      table in $O(\log n)$ time. This greedy strategy correctly finds the minimum distance
      because any path jumping over $nums[v]$ could have instead jumped to $nums[v]$
      in the same number of steps.'
    time_complexity: O((n + q) \log n) where $n$ is the number of nodes and $q$ is the
      number of queries. Sorting unique values and building the binary lifting table
      take $O(n \log n)$, and each of the $q$ queries is resolved in $O(\log n)$ using
      binary jumping.
    space_complexity: O(n \log n) primarily due to the sparse table, which stores $18$
      levels of jumps for up to $n$ unique values.
    elapsed_time: 1248.5043859481812
    model: gemini-3-flash-preview
    generated_at: '2026-07-10 02:31:41 '
---

## Problem #3534: Path Existence Queries in a Graph II

**Difficulty:** Hard

**Topics:** Array, Two Pointers, Binary Search, Dynamic Programming, Greedy, Bit Manipulation, Graph Theory, Sorting

## Problem Description

<p>You are given an integer <code>n</code> representing the number of nodes in a graph, labeled from 0 to <code>n - 1</code>.</p>

<p>You are also given an integer array <code>nums</code> of length <code>n</code> and an integer <code>maxDiff</code>.</p>

<p>An <strong>undirected </strong>edge exists between nodes <code>i</code> and <code>j</code> if the <strong>absolute</strong> difference between <code>nums[i]</code> and <code>nums[j]</code> is <strong>at most</strong> <code>maxDiff</code> (i.e., <code>|nums[i] - nums[j]| &lt;= maxDiff</code>).</p>

<p>You are also given a 2D integer array <code>queries</code>. For each <code>queries[i] = [u<sub>i</sub>, v<sub>i</sub>]</code>, find the <strong>minimum</strong> distance between nodes <code>u<sub>i</sub></code> and <code>v<sub>i</sub></code><sub>.</sub> If no path exists between the two nodes, return -1 for that query.</p>

<p>Return an array <code>answer</code>, where <code>answer[i]</code> is the result of the <code>i<sup>th</sup></code> query.</p>

<p><strong>Note:</strong> The edges between the nodes are unweighted.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 5, nums = [1,8,3,4,2], maxDiff = 3, queries = [[0,3],[2,4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,1]</span></p>

<p><strong>Explanation:</strong></p>

<p>The resulting graph is:</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2025/03/25/4149example1drawio.png" style="width: 281px; height: 161px;" /></p>

<table>
	<tbody>
		<tr>
			<th>Query</th>
			<th>Shortest Path</th>
			<th>Minimum Distance</th>
		</tr>
		<tr>
			<td>[0, 3]</td>
			<td>0 &rarr; 3</td>
			<td>1</td>
		</tr>
		<tr>
			<td>[2, 4]</td>
			<td>2 &rarr; 4</td>
			<td>1</td>
		</tr>
	</tbody>
</table>

<p>Thus, the output is <code>[1, 1]</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 5, nums = [5,3,1,9,10], maxDiff = 2, queries = [[0,1],[0,2],[2,3],[4,3]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,2,-1,1]</span></p>

<p><strong>Explanation:</strong></p>

<p>The resulting graph is:</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2025/03/25/4149example2drawio.png" style="width: 281px; height: 121px;" /></p>
</div>

<table>
	<tbody>
		<tr>
			<th>Query</th>
			<th>Shortest Path</th>
			<th>Minimum Distance</th>
		</tr>
		<tr>
			<td>[0, 1]</td>
			<td>0 &rarr; 1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>[0, 2]</td>
			<td>0 &rarr; 1 &rarr; 2</td>
			<td>2</td>
		</tr>
		<tr>
			<td>[2, 3]</td>
			<td>None</td>
			<td>-1</td>
		</tr>
		<tr>
			<td>[4, 3]</td>
			<td>3 &rarr; 4</td>
			<td>1</td>
		</tr>
	</tbody>
</table>

<p>Thus, the output is <code>[1, 2, -1, 1]</code>.</p>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, nums = [3,6,1], maxDiff = 1, queries = [[0,0],[0,1],[1,2]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,-1,-1]</span></p>

<p><strong>Explanation:</strong></p>

<p>There are no edges between any two nodes because:</p>

<ul>
	<li>Nodes 0 and 1: <code>|nums[0] - nums[1]| = |3 - 6| = 3 &gt; 1</code></li>
	<li>Nodes 0 and 2: <code>|nums[0] - nums[2]| = |3 - 1| = 2 &gt; 1</code></li>
	<li>Nodes 1 and 2: <code>|nums[1] - nums[2]| = |6 - 1| = 5 &gt; 1</code></li>
</ul>

<p>Thus, no node can reach any other node, and the output is <code>[0, -1, -1]</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= maxDiff &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>queries[i] == [u<sub>i</sub>, v<sub>i</sub>]</code></li>
	<li><code>0 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt; n</code></li>
</ul>


## Hints

1. Sort the nodes according to `nums[i]`.

2. Can we use binary jumping?

3. Use binary jumping with a sparse table data structure.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the minimum unweighted distance between two nodes in a graph where an edge exists between nodes $i$ and $j$ if $|nums[i] - nums[j]| \le maxDiff$. Since we want the shortest path in an unweighted graph where connectivity is determined by numerical closeness, a greedy approach is optimal. If we want to reach node $v$ from node $u$ (assuming $nums[u] < nums[v]$), the most efficient path consists of repeatedly jumping to the node with the largest value that is within $maxDiff$ of the current node's value until the target value $nums[v]$ is reached or exceeded. If at any point the next largest available value doesn't allow for further progress (a gap $> maxDiff$ exists), the nodes are disconnected.

To implement this efficiently, we sort the unique values of $nums$ and use binary lifting (a sparse table). Let $U$ be the sorted unique values. We define $up[0][i]$ as the index of the largest value in $U$ reachable from $U[i]$ in one step (i.e., the largest $U[j] \le U[i] + maxDiff$). Using binary lifting, we pre-calculate $up[k][i]$ as the index reached after $2^k$ steps. For each query $(u, v)$, if $u = v$, the distance is 0. If $u \ne v$ and $nums[u] = nums[v]$, the distance is 1. Otherwise, we calculate the distance between their values using the sparse table in $O(\log n)$ time. This greedy strategy correctly finds the minimum distance because any path jumping over $nums[v]$ could have instead jumped to $nums[v]$ in the same number of steps.

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
    vector<int> pathExistenceQueries(int n, vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {
        vector<int> unique_vals = nums;
        sort(unique_vals.begin(), unique_vals.end());
        unique_vals.erase(unique(unique_vals.begin(), unique_vals.end()), unique_vals.end());

        int n_unique = unique_vals.size();
        int max_log = 17;
        vector<vector<int>> up(max_log + 1, vector<int>(n_unique));

        for (int i = 0; i < n_unique; ++i) {
            int target = unique_vals[i] + maxDiff;
            auto it = upper_bound(unique_vals.begin(), unique_vals.end(), target);
            up[0][i] = distance(unique_vals.begin(), it) - 1;
        }

        for (int j = 1; j <= max_log; ++j) {
            for (int i = 0; i < n_unique; ++i) {
                up[j][i] = up[j - 1][up[j - 1][i]];
            }
        }

        vector<int> ans;
        ans.reserve(queries.size());
        for (const auto& q : queries) {
            int u = q[0], v = q[1];
            if (u == v) {
                ans.push_back(0);
                continue;
            }
            int v1 = nums[u], v2 = nums[v];
            if (v1 > v2) swap(v1, v2);

            int idx1 = lower_bound(unique_vals.begin(), unique_vals.end(), v1) - unique_vals.begin();
            int idx2 = lower_bound(unique_vals.begin(), unique_vals.end(), v2) - unique_vals.begin();

            if (up[max_log][idx1] < idx2) {
                ans.push_back(-1);
            } else {
                int dist = 0;
                int curr = idx1;
                for (int j = max_log; j >= 0; --j) {
                    if (up[j][curr] < idx2) {
                        curr = up[j][curr];
                        dist += (1 << j);
                    }
                }
                ans.push_back(dist + 1);
            }
        }
        return ans;
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
    public int[] pathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
        int[] sortedNums = nums.clone();
        Arrays.sort(sortedNums);

        int k = 0;
        if (n > 0) {
            k = 1;
            for (int i = 1; i < n; i++) {
                if (sortedNums[i] != sortedNums[i - 1]) {
                    sortedNums[k++] = sortedNums[i];
                }
            }
        }
        int nUnique = k;
        int[] uniqueVals = Arrays.copyOf(sortedNums, nUnique);

        int maxLog = 17;
        int[][] up = new int[maxLog + 1][nUnique];

        for (int i = 0; i < nUnique; i++) {
            int target = uniqueVals[i] + maxDiff;
            int idx = Arrays.binarySearch(uniqueVals, target);
            if (idx < 0) {
                idx = -(idx + 1) - 1;
            }
            up[0][i] = idx;
        }

        for (int j = 1; j <= maxLog; j++) {
            for (int i = 0; i < nUnique; i++) {
                up[j][i] = up[j - 1][up[j - 1][i]];
            }
        }

        int[] results = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int u = queries[i][0];
            int v = queries[i][1];
            if (u == v) {
                results[i] = 0;
                continue;
            }
            int v1 = nums[u], v2 = nums[v];
            if (v1 > v2) {
                int temp = v1;
                v1 = v2;
                v2 = temp;
            }

            int idx1 = Arrays.binarySearch(uniqueVals, v1);
            int idx2 = Arrays.binarySearch(uniqueVals, v2);

            if (up[maxLog][idx1] < idx2) {
                results[i] = -1;
            } else {
                int dist = 0;
                int curr = idx1;
                for (int j = maxLog; j >= 0; j--) {
                    if (up[j][curr] < idx2) {
                        curr = up[j][curr];
                        dist += (1 << j);
                    }
                }
                results[i] = dist + 1;
            }
        }
        return results;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import bisect

class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        unique_vals = sorted(list(set(nums)))
        val_to_idx = {v: i for i, v in enumerate(unique_vals)}
        n_unique = len(unique_vals)
        MAX_LOG = 17

        up = [[] for _ in range(MAX_LOG + 1)]
        first_jumps = []
        for v in unique_vals:
            target = v + maxDiff
            idx = bisect.bisect_right(unique_vals, target) - 1
            first_jumps.append(idx)

        up[0] = first_jumps
        for j in range(1, MAX_LOG + 1):
            prev_up = up[j-1]
            up[j] = [prev_up[prev_up[i]] for i in range(n_unique)]

        res = []
        ML = MAX_LOG
        for u, v in queries:
            if u == v:
                res.append(0)
                continue
            v1, v2 = nums[u], nums[v]
            if v1 > v2: v1, v2 = v2, v1

            idx1 = val_to_idx[v1]
            idx2 = val_to_idx[v2]

            if up[ML][idx1] < idx2:
                res.append(-1)
            else:
                dist = 0
                curr = idx1
                for j in range(ML, -1, -1):
                    up_j = up[j]
                    if up_j[curr] < idx2:
                        curr = up_j[curr]
                        dist += (1 << j)
                res.append(dist + 1)
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from bisect import bisect_right

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        unique_vals = sorted(list(set(nums)))
        val_to_idx = {v: i for i, v in enumerate(unique_vals)}
        m = len(unique_vals)
        LOG = 18

        jump = [[0] * m for _ in range(LOG)]
        for i in range(m):
            target_val = unique_vals[i] + maxDiff
            idx = bisect_right(unique_vals, target_val) - 1
            jump[0][i] = idx

        for k in range(1, LOG):
            for i in range(m):
                jump[k][i] = jump[k - 1][jump[k - 1][i]]

        results = []
        for u, v in queries:
            if u == v:
                results.append(0)
                continue
            if nums[u] == nums[v]:
                results.append(1)
                continue

            val_u, val_v = nums[u], nums[v]
            if val_u > val_v:
                val_u, val_v = val_v, val_u

            curr = val_to_idx[val_u]
            target = val_to_idx[val_v]
            steps = 0
            for k in range(LOG - 1, -1, -1):
                if jump[k][curr] < target:
                    curr = jump[k][curr]
                    steps += (1 << k)

            if jump[0][curr] >= target:
                results.append(steps + 1)
            else:
                results.append(-1)

        return results
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

int compareInts(const void* a, const void* b) {
    int x = *(const int*)a;
    int y = *(const int*)b;
    if (x < y) return -1;
    if (x > y) return 1;
    return 0;
}

int upper_bound(int* arr, int size, int val) {
    int low = 0, high = size;
    while (low < high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] <= val) low = mid + 1;
        else high = mid;
    }
    return low;
}

int get_idx(int* arr, int size, int val) {
    int low = 0, high = size - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == val) return mid;
        if (arr[mid] < val) low = mid + 1;
        else high = mid;
    }
    return -1;
}

int* pathExistenceQueries(int n, int* nums, int numsSize, int maxDiff, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    int* sorted_nums = (int*)malloc(n * sizeof(int));
    memcpy(sorted_nums, nums, n * sizeof(int));
    qsort(sorted_nums, n, sizeof(int), compareInts);

    int m = 0;
    if (n > 0) {
        m = 1;
        for (int i = 1; i < n; i++) {
            if (sorted_nums[i] != sorted_nums[i-1]) {
                sorted_nums[m++] = sorted_nums[i];
            }
        }
    }

    const int LOG = 18;
    int* jump = (int*)malloc(LOG * m * sizeof(int));
    for (int i = 0; i < m; i++) {
        int target_val = sorted_nums[i] + maxDiff;
        int idx = upper_bound(sorted_nums, m, target_val) - 1;
        jump[0 * m + i] = idx;
    }

    for (int k = 1; k < LOG; k++) {
        for (int i = 0; i < m; i++) {
            jump[k * m + i] = jump[(k - 1) * m + jump[(k - 1) * m + i]];
        }
    }

    *returnSize = queriesSize;
    int* results = (int*)malloc(queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; i++) {
        int u = queries[i][0];
        int v = queries[i][1];
        if (u == v) {
            results[i] = 0;
            continue;
        }
        if (nums[u] == nums[v]) {
            results[i] = 1;
            continue;
        }

        int val_u = nums[u], val_v = nums[v];
        if (val_u > val_v) {
            int temp = val_u;
            val_u = val_v;
            val_v = temp;
        }

        int curr = get_idx(sorted_nums, m, val_u);
        int target = get_idx(sorted_nums, m, val_v);
        int steps = 0;
        for (int k = LOG - 1; k >= 0; k--) {
            if (jump[k * m + curr] < target) {
                curr = jump[k * m + curr];
                steps += (1 << k);
            }
        }

        if (jump[0 * m + curr] >= target) {
            results[i] = steps + 1;
        } else {
            results[i] = -1;
        }
    }

    free(jump);
    free(sorted_nums);
    return results;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] PathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
        int[] uniqueVals = nums.Distinct().ToArray();
        Array.Sort(uniqueVals);
        int m = uniqueVals.Length;
        int LOG = 18;

        int[,] jump = new int[LOG, m];
        for (int i = 0; i < m; i++) {
            int targetVal = uniqueVals[i] + maxDiff;
            int idx = Array.BinarySearch(uniqueVals, targetVal);
            if (idx < 0) idx = ~idx - 1;
            jump[0, i] = idx;
        }

        for (int k = 1; k < LOG; k++) {
            for (int i = 0; i < m; i++) {
                jump[k, i] = jump[k - 1, jump[k - 1, i]];
            }
        }

        int[] results = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            int u = queries[i][0];
            int v = queries[i][1];
            if (u == v) {
                results[i] = 0;
                continue;
            }
            if (nums[u] == nums[v]) {
                results[i] = 1;
                continue;
            }

            int valU = nums[u], valV = nums[v];
            if (valU > valV) {
                int temp = valU;
                valU = valV;
                valV = temp;
            }

            int curr = Array.BinarySearch(uniqueVals, valU);
            int target = Array.BinarySearch(uniqueVals, valV);
            int steps = 0;
            for (int k = LOG - 1; k >= 0; k--) {
                if (jump[k, curr] < target) {
                    curr = jump[k, curr];
                    steps += (1 << k);
                }
            }

            if (jump[0, curr] >= target) {
                results[i] = steps + 1;
            } else {
                results[i] = -1;
            }
        }

        return results;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} n
 * @param {number[]} nums
 * @param {number} maxDiff
 * @param {number[][]} queries
 * @return {number[]}
 */
var pathExistenceQueries = function(n, nums, maxDiff, queries) {
    let uniqueVals = Array.from(new Set(nums)).sort((a, b) => a - b);
    let m = uniqueVals.length;
    const LOG = 18;

    let jump = new Int32Array(LOG * m);

    function upperBound(arr, val) {
        let low = 0, high = arr.length;
        while (low < high) {
            let mid = (low + high) >>> 1;
            if (arr[mid] <= val) low = mid + 1;
            else high = mid;
        }
        return low;
    }

    function getIdx(arr, val) {
        let low = 0, high = arr.length - 1;
        while (low <= high) {
            let mid = (low + high) >>> 1;
            if (arr[mid] === val) return mid;
            if (arr[mid] < val) low = mid + 1;
            else high = mid - 1;
        }
        return -1;
    }

    for (let i = 0; i < m; i++) {
        let targetVal = uniqueVals[i] + maxDiff;
        let idx = upperBound(uniqueVals, targetVal) - 1;
        jump[0 * m + i] = idx;
    }

    for (let k = 1; k < LOG; k++) {
        for (let i = 0; i < m; i++) {
            jump[k * m + i] = jump[(k - 1) * m + jump[(k - 1) * m + i]];
        }
    }

    let results = new Int32Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        let u = queries[i][0];
        let v = queries[i][1];
        if (u === v) {
            results[i] = 0;
            continue;
        }
        if (nums[u] === nums[v]) {
            results[i] = 1;
            continue;
        }

        let valU = nums[u], valV = nums[v];
        if (valU > valV) {
            [valU, valV] = [valV, valU];
        }

        let curr = getIdx(uniqueVals, valU);
        let target = getIdx(uniqueVals, valV);
        let steps = 0;
        for (let k = LOG - 1; k >= 0; k--) {
            if (jump[k * m + curr] < target) {
                curr = jump[k * m + curr];
                steps += (1 << k);
            }
        }

        if (jump[0 * m + curr] >= target) {
            results[i] = steps + 1;
        } else {
            results[i] = -1;
        }
    }

    return Array.from(results);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function pathExistenceQueries(n: number, nums: number[], maxDiff: number, queries: number[][]): number[] {
    const unique = Array.from(new Set(nums)).sort((a, b) => a - b);
    const nU = unique.length;
    const valToIdx = new Map<number, number>();
    for (let i = 0; i < nU; i++) {
        valToIdx.set(unique[i], i);
    }

    const gaps = new Int32Array(nU);
    gaps[0] = 0;
    for (let i = 0; i < nU - 1; i++) {
        gaps[i + 1] = gaps[i] + (unique[i + 1] - unique[i] > maxDiff ? 1 : 0);
    }

    const LOG = 17;
    const jump = new Int32Array(LOG * nU);
    let r = 0;
    for (let i = 0; i < nU; i++) {
        while (r + 1 < nU && unique[r + 1] <= unique[i] + maxDiff) {
            r++;
        }
        jump[i] = r;
    }

    for (let p = 1; p < LOG; p++) {
        const offset = p * nU;
        const prevOffset = (p - 1) * nU;
        for (let i = 0; i < nU; i++) {
            const mid = jump[prevOffset + i];
            jump[offset + i] = jump[prevOffset + mid];
        }
    }

    const results: number[] = [];
    for (const [u, v] of queries) {
        if (u === v) {
            results.push(0);
            continue;
        }
        const valU = nums[u];
        const valV = nums[v];
        const diff = Math.abs(valU - valV);
        if (diff <= maxDiff) {
            results.push(1);
            continue;
        }

        const idxU = valToIdx.get(valU)!;
        const idxV = valToIdx.get(valV)!;
        const startIdx = Math.min(idxU, idxV);
        const endIdx = Math.max(idxU, idxV);

        if (gaps[endIdx] - gaps[startIdx] > 0) {
            results.push(-1);
            continue;
        }

        let dist = 0;
        let curr = startIdx;
        for (let p = LOG - 1; p >= 0; p--) {
            const next = jump[p * nU + curr];
            if (next < endIdx) {
                curr = next;
                dist += (1 << p);
            }
        }
        results.push(dist + 1);
    }
    return results;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $nums
     * @param Integer $maxDiff
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function pathExistenceQueries($n, $nums, $maxDiff, $queries) {
        $unique = array_unique($nums);
        sort($unique);
        $unique = array_values($unique);
        $nU = count($unique);
        $valToIdx = [];
        foreach ($unique as $i => $val) {
            $valToIdx[$val] = $i;
        }

        $gaps = new SplFixedArray($nU);
        $gaps[0] = 0;
        for ($i = 0; $i < $nU - 1; $i++) {
            $gaps[$i + 1] = $gaps[$i] + ($unique[$i + 1] - $unique[$i] > $maxDiff ? 1 : 0);
        }

        $LOG = 17;
        $jump = [];
        for ($p = 0; $p < $LOG; $p++) {
            $jump[$p] = new SplFixedArray($nU);
        }

        $r = 0;
        for ($i = 0; $i < $nU; $i++) {
            while ($r + 1 < $nU && $unique[$r + 1] <= $unique[$i] + $maxDiff) {
                $r++;
            }
            $jump[0][$i] = $r;
        }

        for ($p = 1; $p < $LOG; $p++) {
            for ($i = 0; $i < $nU; $i++) {
                $mid = $jump[$p - 1][$i];
                $jump[$p][$i] = $jump[$p - 1][$mid];
            }
        }

        $ans = [];
        foreach ($queries as $q) {
            $u = $q[0];
            $v = $q[1];
            if ($u == $v) {
                $ans[] = 0;
                continue;
            }
            $valU = $nums[$u];
            $valV = $nums[$v];
            if (abs($valU - $valV) <= $maxDiff) {
                $ans[] = 1;
                continue;
            }

            $idxU = $valToIdx[$valU];
            $idxV = $valToIdx[$valV];
            $start = $idxU < $idxV ? $idxU : $idxV;
            $end = $idxU > $idxV ? $idxU : $idxV;

            if ($gaps[$end] - $gaps[$start] > 0) {
                $ans[] = -1;
                continue;
            }

            $dist = 0;
            $curr = $start;
            for ($p = $LOG - 1; $p >= 0; $p--) {
                if ($jump[$p][$curr] < $end) {
                    $curr = $jump[$p][$curr];
                    $dist += (1 << $p);
                }
            }
            $ans[] = $dist + 1;
        }
        return $ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func pathExistenceQueries(_ n: Int, _ nums: [Int], _ maxDiff: Int, _ queries: [[Int]]) -> [Int] {
        let unique = Array(Set(nums)).sorted()
        let nU = unique.count
        var valToIdx = [Int: Int]()
        for i in 0..<nU {
            valToIdx[unique[i]] = i
        }

        var gaps = [Int](repeating: 0, count: nU)
        for i in 0..<nU - 1 {
            gaps[i + 1] = gaps[i] + (unique[i + 1] - unique[i] > maxDiff ? 1 : 0)
        }

        let LOG = 17
        var jump = [Int](repeating: 0, count: LOG * nU)
        var r = 0
        for i in 0..<nU {
            while r + 1 < nU && unique[r + 1] <= unique[i] + maxDiff {
                r += 1
            }
            jump[i] = r
        }

        for p in 1..<LOG {
            let offset = p * nU
            let prevOffset = (p - 1) * nU
            for i in 0..<nU {
                let mid = jump[prevOffset + i]
                jump[offset + i] = jump[prevOffset + mid]
            }
        }

        var results = [Int]()
        results.reserveCapacity(queries.count)
        for q in queries {
            let u = q[0]
            let v = q[1]
            if u == v {
                results.append(0)
                continue
            }
            let valU = nums[u]
            let valV = nums[v]
            if abs(valU - valV) <= maxDiff {
                results.append(1)
                continue
            }
            guard let idxU = valToIdx[valU], let idxV = valToIdx[valV] else {
                results.append(-1)
                continue
            }
            let startIdx = min(idxU, idxV)
            let endIdx = max(idxU, idxV)

            if gaps[endIdx] - gaps[startIdx] > 0 {
                results.append(-1)
                continue
            }

            var dist = 0
            var curr = startIdx
            for p in (0..<LOG).reversed() {
                let next = jump[p * nU + curr]
                if next < endIdx {
                    curr = next
                    dist += (1 << p)
                }
            }
            results.append(dist + 1)
        }
        return results
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import java.util.*
import kotlin.math.*

class Solution {
    fun pathExistenceQueries(n: Int, nums: IntArray, maxDiff: Int, queries: Array<IntArray>): IntArray {
        val unique = nums.distinct().toIntArray()
        unique.sort()
        val nU = unique.size
        val valToIdx = mutableMapOf<Int, Int>()
        for (i in unique.indices) {
            valToIdx[unique[i]] = i
        }

        val gaps = IntArray(nU)
        for (i in 0 until nU - 1) {
            gaps[i + 1] = gaps[i] + if (unique[i + 1] - unique[i] > maxDiff) 1 else 0
        }

        val LOG = 17
        val jump = Array(LOG) { IntArray(nU) }
        var r = 0
        for (i in 0 until nU) {
            while (r + 1 < nU && unique[r + 1] <= unique[i] + maxDiff) {
                r++
            }
            jump[0][i] = r
        }

        for (p in 1 until LOG) {
            for (i in 0 until nU) {
                val mid = jump[p - 1][i]
                jump[p][i] = jump[p - 1][mid]
            }
        }

        val results = IntArray(queries.size)
        for (i in queries.indices) {
            val u = queries[i][0]
            val v = queries[i][1]
            if (u == v) {
                results[i] = 0
                continue
            }
            val valU = nums[u]
            val valV = nums[v]
            if (abs(valU - valV) <= maxDiff) {
                results[i] = 1
                continue
            }

            val idxU = valToIdx[valU]!!
            val idxV = valToIdx[valV]!!
            val startIdx = min(idxU, idxV)
            val endIdx = max(idxU, idxV)

            if (gaps[endIdx] - gaps[startIdx] > 0) {
                results[i] = -1
                continue
            }

            var dist = 0
            var curr = startIdx
            for (p in LOG - 1 downTo 0) {
                if (jump[p][curr] < endIdx) {
                    curr = jump[p][curr]
                    dist += (1 shl p)
                }
            }
            results[i] = dist + 1
        }
        return results
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<int> pathExistenceQueries(int n, List<int> nums, int maxDiff, List<List<int>> queries) {
    List<int> sortedUnique = nums.toSet().toList()..sort();
    int m = sortedUnique.length;

    List<int> comp = List.filled(m, 0);
    for (int i = 1; i < m; i++) {
      if (sortedUnique[i] - sortedUnique[i - 1] <= maxDiff) {
        comp[i] = comp[i - 1];
      } else {
        comp[i] = comp[i - 1] + 1;
      }
    }

    List<List<int>> jump = List.generate(m, (_) => List.filled(17, 0));
    for (int i = 0; i < m; i++) {
      int target = sortedUnique[i] + maxDiff;
      int low = 0, high = m;
      while (low < high) {
        int mid = low + ((high - low) ~/ 2);
        if (sortedUnique[mid] <= target) low = mid + 1;
        else high = mid;
      }
      jump[i][0] = low - 1;
    }

    for (int k = 1; k < 17; k++) {
      for (int i = 0; i < m; i++) {
        jump[i][k] = jump[jump[i][k - 1]][k - 1];
      }
    }

    int findIdx(int val) {
      int low = 0, high = m - 1;
      while (low <= high) {
        int mid = low + ((high - low) ~/ 2);
        if (sortedUnique[mid] == val) return mid;
        if (sortedUnique[mid] < val) low = mid + 1;
        else high = mid - 1;
      }
      return -1;
    }

    List<int> results = List.filled(queries.length, 0);
    for (int i = 0; i < queries.length; i++) {
      int u = queries[i][0];
      int v = queries[i][1];
      if (u == v) {
        results[i] = 0;
        continue;
      }
      if (nums[u] == nums[v]) {
        results[i] = 1;
        continue;
      }

      int idxX = findIdx(nums[u]);
      int idxY = findIdx(nums[v]);
      if (idxX > idxY) {
        int temp = idxX;
        idxX = idxY;
        idxY = temp;
      }

      if (comp[idxX] != comp[idxY]) {
        results[i] = -1;
      } else {
        int current = idxX;
        int steps = 0;
        for (int k = 16; k >= 0; k--) {
          if (jump[current][k] < idxY) {
            current = jump[current][k];
            steps += (1 << k);
          }
        }
        results[i] = steps + 1;
      }
    }
    return results;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func pathExistenceQueries(n int, nums []int, maxDiff int, queries [][]int) []int {
    v := make([]int, len(nums))
    copy(v, nums)
    sort.Ints(v)

    m := 0
    if len(v) > 0 {
        for i := 1; i < len(v); i++ {
            if v[i] != v[m] {
                m++
                v[m] = v[i]
            }
        }
        v = v[:m+1]
    }
    m = len(v)

    comp := make([]int, m)
    for i := 1; i < m; i++ {
        if v[i]-v[i-1] <= maxDiff {
            comp[i] = comp[i-1]
        } else {
            comp[i] = comp[i-1] + 1
        }
    }

    jump := make([][17]int, m)
    for i := 0; i < m; i++ {
        target := v[i] + maxDiff
        idx := sort.Search(m, func(j int) bool {
            return v[j] > target
        }) - 1
        jump[i][0] = idx
    }

    for k := 1; k < 17; k++ {
        for i := 0; i < m; i++ {
            jump[i][k] = jump[jump[i][k-1]][k-1]
        }
    }

    pos := make(map[int]int)
    for i, val := range v {
        pos[val] = i
    }

    ans := make([]int, len(queries))
    for i, q := range queries {
        u, v_idx := q[0], q[1]
        if u == v_idx {
            ans[i] = 0
            continue
        }
        if nums[u] == nums[v_idx] {
            ans[i] = 1
            continue
        }

        idxX := pos[nums[u]]
        idxY := pos[nums[v_idx]]
        if idxX > idxY {
            idxX, idxY = idxY, idxX
        }

        if comp[idxX] != comp[idxY] {
            ans[i] = -1
        } else {
            current := idxX
            steps := 0
            for k := 16; k >= 0; k-- {
                if jump[current][k] < idxY {
                    current = jump[current][k]
                    steps += (1 << k)
                }
            }
            ans[i] = steps + 1
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
def path_existence_queries(n, nums, max_diff, queries)
  v = nums.uniq.sort
  m = v.size
  pos = {}
  v.each_with_index { |val, idx| pos[val] = idx }

  comp = Array.new(m, 0)
  (1...m).each do |i|
    if v[i] - v[i - 1] <= max_diff
      comp[i] = comp[i - 1]
    else
      comp[i] = comp[i - 1] + 1
    end
  end

  jump = Array.new(m * 17)
  (0...m).each do |i|
    target = v[i] + max_diff
    idx = v.bsearch_index { |x| x > target } || m
    jump[i * 17 + 0] = idx - 1
  end

  (1..16).each do |k|
    (0...m).each do |i|
      mid = jump[i * 17 + k - 1]
      jump[i * 17 + k] = jump[mid * 17 + k - 1]
    end
  end

  ans = Array.new(queries.size)
  queries.each_with_index do |q, i|
    u, node_v = q[0], q[1]
    if u == node_v
      ans[i] = 0
      next
    end
    if nums[u] == nums[node_v]
      ans[i] = 1
      next
    end

    idx_x = pos[nums[u]]
    idx_y = pos[nums[node_v]]
    idx_x, idx_y = idx_y, idx_x if idx_x > idx_y

    if comp[idx_x] != comp[idx_y]
      ans[i] = -1
    else
      current = idx_x
      steps = 0
      (16).step(0, -1).each do |k|
        jump_idx = jump[current * 17 + k]
        if jump_idx < idx_y
          current = jump_idx
          steps += (1 << k)
        end
      end
      ans[i] = steps + 1
    end
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
  import scala.collection.mutable

  def pathExistenceQueries(n: Int, nums: Array[Int], maxDiff: Int, queries: Array[Array[Int]]): Array[Int] = {
    val v = nums.distinct.sorted
    val m = v.length

    val comp = new Array[Int](m)
    var i = 1
    while (i < m) {
      if (v(i) - v(i - 1) <= maxDiff) {
        comp(i) = comp(i - 1)
      } else {
        comp(i) = comp(i - 1) + 1
      }
      i += 1
    }

    val jump = Array.ofDim[Int](m, 17)
    i = 0
    while (i < m) {
      val target = v(i) + maxDiff
      var low = 0
      var high = m
      while (low < high) {
        val mid = low + (high - low) / 2
        if (v(mid) <= target) low = mid + 1
        else high = mid
      }
      jump(i)(0) = low - 1
      i += 1
    }

    for (k <- 1 until 17) {
      for (j <- 0 until m) {
        jump(j)(k) = jump(jump(j)(k - 1))(k - 1)
      }
    }

    val results = new Array[Int](queries.length)
    var qIdx = 0
    while (qIdx < queries.length) {
      val u = queries(qIdx)(0)
      val nV = queries(qIdx)(1)
      if (u == nV) {
        results(qIdx) = 0
      } else if (nums(u) == nums(nV)) {
        results(qIdx) = 1
      } else {
        var idxX = java.util.Arrays.binarySearch(v, nums(u))
        var idxY = java.util.Arrays.binarySearch(v, nums(nV))
        if (idxX > idxY) {
          val temp = idxX
          idxX = idxY
          idxY = temp
        }

        if (comp(idxX) != comp(idxY)) {
          results(qIdx) = -1
        } else {
          var current = idxX
          var steps = 0
          for (k <- 16 to 0 by -1) {
            if (jump(current)(k) < idxY) {
              current = jump(current)(k)
              steps += (1 << k)
            }
          }
          results(qIdx) = steps + 1
        }
      }
      qIdx += 1
    }
    results
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn path_existence_queries(n: i32, nums: Vec<i32>, max_diff: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = n as usize;
        let mut p: Vec<usize> = (0..n).collect();
        p.sort_by(|&a, &b| {
            if nums[a] == nums[b] {
                a.cmp(&b)
            } else {
                nums[a].cmp(&nums[b])
            }
        });

        let mut sorted_nums = vec![0; n];
        let mut sorted_idx = vec![0; n];
        for i in 0..n {
            sorted_nums[i] = nums[p[i]];
            sorted_idx[p[i]] = i;
        }

        let mut jump_l = vec![vec![0; n]; 17];
        let mut jump_r = vec![vec![0; n]; 17];

        let mut l_ptr = 0;
        for i in 0..n {
            while sorted_nums[i] - sorted_nums[l_ptr] > max_diff {
                l_ptr += 1;
            }
            jump_l[0][i] = l_ptr;
        }

        let mut r_ptr = 0;
        for i in 0..n {
            while r_ptr + 1 < n && sorted_nums[r_ptr + 1] - sorted_nums[i] <= max_diff {
                r_ptr += 1;
            }
            jump_r[0][i] = r_ptr;
        }

        for k in 1..17 {
            for i in 0..n {
                jump_l[k][i] = jump_l[k - 1][jump_l[k - 1][i]];
                jump_r[k][i] = jump_r[k - 1][jump_r[k - 1][i]];
            }
        }

        let mut answer = Vec::with_capacity(queries.len());
        for q in queries {
            let u = q[0] as usize;
            let v = q[1] as usize;
            if u == v {
                answer.push(0);
                continue;
            }

            let i = sorted_idx[u];
            let j = sorted_idx[v];

            if i < j {
                if jump_r[16][i] < j {
                    answer.push(-1);
                } else {
                    let mut curr = i;
                    let mut dist = 0;
                    for k in (0..17).rev() {
                        if jump_r[k][curr] < j {
                            curr = jump_r[k][curr];
                            dist += 1 << k;
                        }
                    }
                    answer.push(dist + 1);
                }
            } else {
                if jump_l[16][i] > j {
                    answer.push(-1);
                } else {
                    let mut curr = i;
                    let mut dist = 0;
                    for k in (0..17).rev() {
                        if jump_l[k][curr] > j {
                            curr = jump_l[k][curr];
                            dist += 1 << k;
                        }
                    }
                    answer.push(dist + 1);
                }
            }
        }
        answer
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (path-existence-queries n nums maxDiff queries)
  (-> exact-integer? (listof exact-integer?) exact-integer? (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ([nums-vec (list->vector nums)]
         [nodes (sort (range n)
                      (lambda (i j)
                        (let ([vi (vector-ref nums-vec i)]
                              [vj (vector-ref nums-vec j)])
                          (if (= vi vj) (< i j) (< vi vj)))))]
         [sorted-nums (for/vector ([i nodes]) (vector-ref nums-vec i))]
         [sorted-idx (make-vector n)]
         [_ (for ([pos (in-range n)] [orig nodes]) (vector-set! sorted-idx orig pos))]
         [jumpL (make-vector 17)]
         [jumpR (make-vector 17)])
    (vector-set! jumpL 0
                 (let ([l-res (make-vector n)] [l-ptr 0])
                   (for ([i (in-range n)])
                     (while (> (- (vector-ref sorted-nums i) (vector-ref sorted-nums l-ptr)) maxDiff)
                            (set! l-ptr (+ l-ptr 1)))
                     (vector-set! l-res i l-ptr))
                   l-res))
    (vector-set! jumpR 0
                 (let ([r-res (make-vector n)] [r-ptr 0])
                   (for ([i (in-range n)])
                     (while (and (< (+ r-ptr 1) n) (<= (- (vector-ref sorted-nums (+ r-ptr 1)) (vector-ref sorted-nums i)) maxDiff))
                            (set! r-ptr (+ r-ptr 1)))
                     (vector-set! r-res i r-ptr))
                   r-res))
    (for ([k (in-range 1 17)])
      (let* ([prevL (vector-ref jumpL (- k 1))]
             [prevR (vector-ref jumpR (- k 1))]
             [currL (make-vector n)]
             [currR (make-vector n)])
        (for ([i (in-range n)])
          (vector-set! currL i (vector-ref prevL (vector-ref prevL i)))
          (vector-set! currR i (vector-ref prevR (vector-ref prevR i))))
        (vector-set! jumpL k currL)
        (vector-set! jumpR k currR)))
    (map (lambda (q)
           (let ([u (car q)] [v (cadr q)])
             (if (= u v) 0
                 (let ([i (vector-ref sorted-idx u)] [j (vector-ref sorted-idx v)])
                   (if (< i j)
                       (if (< (vector-ref (vector-ref jumpR 16) i) j) -1
                           (let-values ([(curr dist)
                                         (for/fold ([c i] [d 0]) ([k (in-range 16 -1 -1)])
                                           (let ([next (vector-ref (vector-ref jumpR k) c)])
                                             (if (< next j) (values next (+ d (arithmetic-shift 1 k))) (values c d))))])
                             (+ dist 1)))
                       (if (> (vector-ref (vector-ref jumpL 16) i) j) -1
                           (let-values ([(curr dist)
                                         (for/fold ([c i] [d 0]) ([k (in-range 16 -1 -1)])
                                           (let ([next (vector-ref (vector-ref jumpL k) c)])
                                             (if (> next j) (values next (+ d (arithmetic-shift 1 k))) (values c d))))])
                             (+ dist 1))))))))
         queries)))

(define-syntax-rule (while condition body ...)
  (let loop () (when condition body ... (loop))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec path_existence_queries(N :: integer(), Nums :: [integer()], MaxDiff :: integer(), Queries :: [[integer()]]) -> [integer()].
path_existence_queries(N, Nums, MaxDiff, Queries) ->
  IndexedNums = lists:zip(Nums, lists:seq(0, N - 1)),
  SortedWithIdx = lists:sort(IndexedNums),
  SortedNums = list_to_tuple([V || {V, _} <- SortedWithIdx]),
  SortedIdxMap = lists:sort([{OrigIdx, Pos} || {{_, OrigIdx}, Pos} <- lists:zip(SortedWithIdx, lists:seq(0, N - 1))]),
  SortedIdx = list_to_tuple([Pos || {_, Pos} <- SortedIdxMap]),

  L0 = list_to_tuple(compute_l(0, 0, SortedNums, MaxDiff, N, [])),
  R0 = list_to_tuple(compute_r(0, 0, SortedNums, MaxDiff, N, [])),

  {JumpL, JumpR} = build_jump_tables(1, L0, R0, N, [L0], [R0]),

  [process_query(Q, SortedIdx, JumpL, JumpR) || Q <- Queries].

compute_l(N, _, _, _, N, Acc) -> lists:reverse(Acc);
compute_l(I, LPtr, SortedNums, MaxDiff, N, Acc) ->
  ValI = element(I + 1, SortedNums),
  NewLPtr = find_lptr(LPtr, ValI, SortedNums, MaxDiff),
  compute_l(I + 1, NewLPtr, SortedNums, MaxDiff, N, [NewLPtr | Acc]).

find_lptr(LPtr, ValI, SortedNums, MaxDiff) ->
  ValL = element(LPtr + 1, SortedNums),
  if ValI - ValL > MaxDiff -> find_lptr(LPtr + 1, ValI, SortedNums, MaxDiff);
     true -> LPtr
  end.

compute_r(N, _, _, _, N, Acc) -> lists:reverse(Acc);
compute_r(I, RPtr, SortedNums, MaxDiff, N, Acc) ->
  ValI = element(I + 1, SortedNums),
  NewRPtr = find_rptr(RPtr, ValI, SortedNums, MaxDiff, N),
  compute_r(I + 1, NewRPtr, SortedNums, MaxDiff, N, [NewRPtr | Acc]).

find_rptr(RPtr, ValI, SortedNums, MaxDiff, N) ->
  if RPtr + 1 < N ->
       ValNext = element(RPtr + 2, SortedNums),
       if ValNext - ValI =< MaxDiff -> find_rptr(RPtr + 1, ValI, SortedNums, MaxDiff, N);
          true -> RPtr
       end;
     true -> RPtr
  end.

build_jump_tables(17, _, _, _, AccL, AccR) -> {list_to_tuple(lists:reverse(AccL)), list_to_tuple(lists:reverse(AccR))};
build_jump_tables(K, PrevL, PrevR, N, AccL, AccR) ->
  CurrL = list_to_tuple([element(element(I, PrevL) + 1, PrevL) || I <- lists:seq(1, N)]),
  CurrR = list_to_tuple([element(element(I, PrevR) + 1, PrevR) || I <- lists:seq(1, N)]),
  build_jump_tables(K + 1, CurrL, CurrR, N, [CurrL | AccL], [CurrR | AccR]).

process_query([U, V], SortedIdx, JumpL, JumpR) ->
  if U == V -> 0;
     true ->
       I = element(U + 1, SortedIdx),
       J = element(V + 1, SortedIdx),
       if I < J ->
            MaxReachable = element(I + 1, element(17, JumpR)),
            if MaxReachable < J -> -1;
               true -> jump_dist(16, I, J, JumpR, 0) + 1
            end;
          true ->
            MinReachable = element(I + 1, element(17, JumpL)),
            if MinReachable > J -> -1;
               true -> jump_dist_l(16, I, J, JumpL, 0) + 1
            end
       end
  end.

jump_dist(-1, _, _, _, Dist) -> Dist;
jump_dist(K, Curr, Target, Table, Dist) ->
  Next = element(Curr + 1, element(K + 1, Table)),
  if Next < Target -> jump_dist(K - 1, Next, Target, Table, Dist + (1 bsl K));
     true -> jump_dist(K - 1, Curr, Target, Table, Dist)
  end.

jump_dist_l(-1, _, _, _, Dist) -> Dist;
jump_dist_l(K, Curr, Target, Table, Dist) ->
  Next = element(Curr + 1, element(K + 1, Table)),
  if Next > Target -> jump_dist_l(K - 1, Next, Target, Table, Dist + (1 bsl K));
     true -> jump_dist_l(K - 1, Curr, Target, Table, Dist)
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  import Bitwise

  @spec path_existence_queries(n :: integer, nums :: [integer], max_diff :: integer, queries :: [[integer]]) :: [integer]
  def path_existence_queries(n, nums, max_diff, queries) do
    nums_with_idx = Enum.with_index(nums)
    sorted_with_idx = Enum.sort(nums_with_idx)
    sorted_nums = sorted_with_idx |> Enum.map(fn {v, _} -> v end) |> List.to_tuple()

    sorted_idx_map = Enum.with_index(sorted_with_idx)
      |> Enum.map(fn {{_v, orig_idx}, pos} -> {orig_idx, pos} end)
      |> Enum.sort()
      |> Enum.map(fn {_, pos} -> pos end)
      |> List.to_tuple()

    l0 = compute_l(0, 0, sorted_nums, max_diff, n, []) |> List.to_tuple()
    r0 = compute_r(0, 0, sorted_nums, max_diff, n, []) |> List.to_tuple()

    {jump_l, jump_r} = build_jump_tables(1, l0, r0, n, [l0], [r0])

    Enum.map(queries, fn [u, v] ->
      if u == v do
        0
      else
        i = elem(sorted_idx_map, u)
        j = elem(sorted_idx_map, v)
        if i < j do
          if elem(elem(jump_r, 16), i) < j do
            -1
          else
            jump_dist_r(16, i, j, jump_r, 0) + 1
          end
        else
          if elem(elem(jump_l, 16), i) > j do
            -1
          else
            jump_dist_l(16, i, j, jump_l, 0) + 1
          end
        end
      end
    end)
  end

  defp compute_l(n, _lptr, _nums, _diff, n, acc), do: Enum.reverse(acc)
  defp compute_l(i, lptr, nums, diff, n, acc) do
    val_i = elem(nums, i)
    new_lptr = find_lptr(lptr, val_i, nums, diff)
    compute_l(i + 1, new_lptr, nums, diff, n, [new_lptr | acc])
  end

  defp find_lptr(lptr, val_i, nums, diff) do
    if val_i - elem(nums, lptr) > diff do
      find_lptr(lptr + 1, val_i, nums, diff)
    else
      lptr
    end
  end

  defp compute_r(n, _rptr, _nums, _diff, n, acc), do: Enum.reverse(acc)
  defp compute_r(i, rptr, nums, diff, n, acc) do
    val_i = elem(nums, i)
    new_rptr = find_rptr(rptr, val_i, nums, diff, n)
    compute_r(i + 1, new_rptr, nums, diff, n, [new_rptr | acc])
  end

  defp find_rptr(rptr, val_i, nums, diff, n) do
    if rptr + 1 < n and elem(nums, rptr + 1) - val_i <= diff do
      find_rptr(rptr + 1, val_i, nums, diff, n)
    else
      rptr
    end
  end

  defp build_jump_tables(17, _pl, _pr, _n, accl, accr) do
    {List.to_tuple(Enum.reverse(accl)), List.to_tuple(Enum.reverse(accr))}
  end
  defp build_jump_tables(k, pl, pr, n, accl, accr) do
    cl = Enum.map(0..(n - 1), fn i -> elem(pl, elem(pl, i)) end) |> List.to_tuple()
    cr = Enum.map(0..(n - 1), fn i -> elem(pr, elem(pr, i)) end) |> List.to_tuple()
    build_jump_tables(k + 1, cl, cr, n, [cl | accl], [cr | accr])
  end

  defp jump_dist_r(-1, _curr, _target, _table, dist), do: dist
  defp jump_dist_r(k, curr, target, table, dist) do
    next = elem(elem(table, k), curr)
    if next < target do
      jump_dist_r(k - 1, next, target, table, dist + bsl(1, k))
    else
      jump_dist_r(k - 1, curr, target, table, dist)
    end
  end

  defp jump_dist_l(-1, _curr, _target, _table, dist), do: dist
  defp jump_dist_l(k, curr, target, table, dist) do
    next = elem(elem(table, k), curr)
    if next > target do
      jump_dist_l(k - 1, next, target, table, dist + bsl(1, k))
    else
      jump_dist_l(k - 1, curr, target, table, dist)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O((n + q) \log n) where $n$ is the number of nodes and $q$ is the number of queries. Sorting unique values and building the binary lifting table take $O(n \log n)$, and each of the $q$ queries is resolved in $O(\log n)$ using binary jumping.
- **Space Complexity:** O(n \log n) primarily due to the sparse table, which stores $18$ levels of jumps for up to $n$ unique values.
