---
layout: post
title: "Earliest Finish Time for Land and Water Rides II"
date: 2026-06-03 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Two Pointers", "Binary Search", "Greedy", "Sorting"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    long long solve(const vector<int>& s1, const\
        \ vector<int>& d1, const vector<int>& s2, const vector<int>& d2) {\n       \
        \ int n = s1.size(), m = s2.size();\n        vector<pair<int, int>> rides2(m);\n\
        \        for (int i = 0; i < m; ++i) rides2[i] = {s2[i], d2[i]};\n        sort(rides2.begin(),\
        \ rides2.end());\n\n        vector<int> prefixMinDur(m);\n        prefixMinDur[0]\
        \ = rides2[0].second;\n        for (int i = 1; i < m; ++i) prefixMinDur[i] =\
        \ min(prefixMinDur[i - 1], rides2[i].second);\n\n        vector<long long> suffixMinFin(m);\n\
        \        suffixMinFin[m - 1] = (long long)rides2[m - 1].first + rides2[m - 1].second;\n\
        \        for (int i = m - 2; i >= 0; --i) suffixMinFin[i] = min(suffixMinFin[i\
        \ + 1], (long long)rides2[i].first + rides2[i].second);\n\n        long long\
        \ minFinish = -1;\n\n        for (int i = 0; i < n; ++i) {\n            long\
        \ long f1 = (long long)s1[i] + d1[i];\n            auto it = upper_bound(rides2.begin(),\
        \ rides2.end(), make_pair((int)f1, 2000000000));\n            int idx = distance(rides2.begin(),\
        \ it);\n\n            long long currentMin = -1;\n            if (idx > 0) {\n\
        \                long long res = f1 + prefixMinDur[idx - 1];\n             \
        \   if (currentMin == -1 || res < currentMin) currentMin = res;\n          \
        \  }\n            if (idx < m) {\n                long long res = suffixMinFin[idx];\n\
        \                if (currentMin == -1 || res < currentMin) currentMin = res;\n\
        \            }\n            if (minFinish == -1 || currentMin < minFinish) minFinish\
        \ = currentMin;\n        }\n        return minFinish;\n    }\n\n    int earliestFinishTime(vector<int>&\
        \ landStartTime, vector<int>& landDuration, vector<int>& waterStartTime, vector<int>&\
        \ waterDuration) {\n        return (int)min(solve(landStartTime, landDuration,\
        \ waterStartTime, waterDuration), \n                        solve(waterStartTime,\
        \ waterDuration, landStartTime, landDuration));\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    static class Ride implements\
        \ Comparable<Ride> {\n        int start, duration;\n        Ride(int s, int\
        \ d) { start = s; duration = d; }\n        public int compareTo(Ride other)\
        \ { return Integer.compare(this.start, other.start); }\n    }\n\n    private\
        \ long solve(int[] s1, int[] d1, int[] s2, int[] d2) {\n        int n = s1.length,\
        \ m = s2.length;\n        Ride[] rides2 = new Ride[m];\n        for (int i =\
        \ 0; i < m; i++) rides2[i] = new Ride(s2[i], d2[i]);\n        Arrays.sort(rides2);\n\
        \n        int[] prefixMinDur = new int[m];\n        prefixMinDur[0] = rides2[0].duration;\n\
        \        for (int i = 1; i < m; i++) prefixMinDur[i] = Math.min(prefixMinDur[i\
        \ - 1], rides2[i].duration);\n\n        long[] suffixMinFin = new long[m];\n\
        \        suffixMinFin[m - 1] = (long) rides2[m - 1].start + rides2[m - 1].duration;\n\
        \        for (int i = m - 2; i >= 0; i--) suffixMinFin[i] = Math.min(suffixMinFin[i\
        \ + 1], (long) rides2[i].start + rides2[i].duration);\n\n        long minFinish\
        \ = Long.MAX_VALUE;\n        for (int i = 0; i < n; i++) {\n            long\
        \ f1 = (long) s1[i] + d1[i];\n            int low = 0, high = m - 1, idx = 0;\n\
        \            while (low <= high) {\n                int mid = (low + high) /\
        \ 2;\n                if (rides2[mid].start <= f1) {\n                    idx\
        \ = mid + 1;\n                    low = mid + 1;\n                } else {\n\
        \                    high = mid - 1;\n                }\n            }\n\n \
        \           long currentMin = Long.MAX_VALUE;\n            if (idx > 0) currentMin\
        \ = Math.min(currentMin, f1 + prefixMinDur[idx - 1]);\n            if (idx <\
        \ m) currentMin = Math.min(currentMin, suffixMinFin[idx]);\n            minFinish\
        \ = Math.min(minFinish, currentMin);\n        }\n        return minFinish;\n\
        \    }\n\n    public int earliestFinishTime(int[] landStartTime, int[] landDuration,\
        \ int[] waterStartTime, int[] waterDuration) {\n        return (int) Math.min(solve(landStartTime,\
        \ landDuration, waterStartTime, waterDuration),\n                          \
        \   solve(waterStartTime, waterDuration, landStartTime, landDuration));\n  \
        \  }\n}"
      python: "import bisect\n\nclass Solution(object):\n    def earliestFinishTime(self,\
        \ landStartTime, landDuration, waterStartTime, waterDuration):\n        def\
        \ solve(s1, d1, s2, d2):\n            m = len(s2)\n            rides2 = sorted(zip(s2,\
        \ d2))\n            starts2 = [r[0] for r in rides2]\n            durs2 = [r[1]\
        \ for r in rides2]\n\n            prefixMinDur = [0] * m\n            prefixMinDur[0]\
        \ = durs2[0]\n            for i in range(1, m):\n                prefixMinDur[i]\
        \ = min(prefixMinDur[i-1], durs2[i])\n\n            suffixMinFin = [0] * m\n\
        \            suffixMinFin[m-1] = starts2[m-1] + durs2[m-1]\n            for\
        \ i in range(m-2, -1, -1):\n                suffixMinFin[i] = min(suffixMinFin[i+1],\
        \ starts2[i] + durs2[i])\n\n            minFinish = float('inf')\n         \
        \   for i in range(len(s1)):\n                f1 = s1[i] + d1[i]\n         \
        \       idx = bisect.bisect_right(starts2, f1)\n\n                res = float('inf')\n\
        \                if idx > 0:\n                    res = min(res, f1 + prefixMinDur[idx-1])\n\
        \                if idx < m:\n                    res = min(res, suffixMinFin[idx])\n\
        \                minFinish = min(minFinish, res)\n            return minFinish\n\
        \n        res1 = solve(landStartTime, landDuration, waterStartTime, waterDuration)\n\
        \        res2 = solve(waterStartTime, waterDuration, landStartTime, landDuration)\n\
        \        return int(min(res1, res2))"
      python3: "import bisect\n\nclass Solution:\n    def earliestFinishTime(self, landStartTime:\
        \ List[int], landDuration: List[int], waterStartTime: List[int], waterDuration:\
        \ List[int]) -> int:\n        def solve(s1, d1, s2, d2):\n            m = len(s2)\n\
        \            rides2 = sorted(zip(s2, d2))\n            starts2 = [r[0] for r\
        \ in rides2]\n            durs2 = [r[1] for r in rides2]\n\n            prefixMinDur\
        \ = [0] * m\n            prefixMinDur[0] = durs2[0]\n            for i in range(1,\
        \ m):\n                prefixMinDur[i] = min(prefixMinDur[i-1], durs2[i])\n\n\
        \            suffixMinFin = [0] * m\n            suffixMinFin[m-1] = starts2[m-1]\
        \ + durs2[m-1]\n            for i in range(m-2, -1, -1):\n                suffixMinFin[i]\
        \ = min(suffixMinFin[i+1], starts2[i] + durs2[i])\n\n            minFinish =\
        \ float('inf')\n            for i in range(len(s1)):\n                f1 = s1[i]\
        \ + d1[i]\n                idx = bisect.bisect_right(starts2, f1)\n\n      \
        \          res = float('inf')\n                if idx > 0:\n               \
        \     res = min(res, f1 + prefixMinDur[idx-1])\n                if idx < m:\n\
        \                    res = min(res, suffixMinFin[idx])\n                minFinish\
        \ = min(minFinish, res)\n            return minFinish\n\n        res1 = solve(landStartTime,\
        \ landDuration, waterStartTime, waterDuration)\n        res2 = solve(waterStartTime,\
        \ waterDuration, landStartTime, landDuration)\n        return int(min(res1,\
        \ res2))"
      c: "#include <stdio.h>\n#include <stdlib.h>\n#include <limits.h>\n\ntypedef struct\
        \ {\n    int start;\n    int duration;\n} Ride;\n\nint compareRides(const void*\
        \ a, const void* b) {\n    return ((Ride*)a)->start - ((Ride*)b)->start;\n}\n\
        \nlong long solve(int* s1, int* d1, int n, int* s2, int* d2, int m) {\n    Ride*\
        \ rides2 = (Ride*)malloc(m * sizeof(Ride));\n    for (int i = 0; i < m; i++)\
        \ {\n        rides2[i].start = s2[i];\n        rides2[i].duration = d2[i];\n\
        \    }\n    qsort(rides2, m, sizeof(Ride), compareRides);\n\n    int* prefixMinDur\
        \ = (int*)malloc(m * sizeof(int));\n    prefixMinDur[0] = rides2[0].duration;\n\
        \    for (int i = 1; i < m; i++) {\n        prefixMinDur[i] = (rides2[i].duration\
        \ < prefixMinDur[i - 1]) ? rides2[i].duration : prefixMinDur[i - 1];\n    }\n\
        \n    long long* suffixMinFin = (long long*)malloc(m * sizeof(long long));\n\
        \    suffixMinFin[m - 1] = (long long)rides2[m - 1].start + rides2[m - 1].duration;\n\
        \    for (int i = m - 2; i >= 0; i--) {\n        long long fin = (long long)rides2[i].start\
        \ + rides2[i].duration;\n        suffixMinFin[i] = (fin < suffixMinFin[i + 1])\
        \ ? fin : suffixMinFin[i + 1];\n    }\n\n    long long minFinish = LLONG_MAX;\n\
        \    for (int i = 0; i < n; i++) {\n        long long f1 = (long long)s1[i]\
        \ + d1[i];\n        int low = 0, high = m - 1, idx = 0;\n        while (low\
        \ <= high) {\n            int mid = low + (high - low) / 2;\n            if\
        \ (rides2[mid].start <= f1) {\n                idx = mid + 1;\n            \
        \    low = mid + 1;\n            } else {\n                high = mid - 1;\n\
        \            }\n        }\n\n        long long currentMin = LLONG_MAX;\n   \
        \     if (idx > 0) {\n            long long res = f1 + prefixMinDur[idx - 1];\n\
        \            if (res < currentMin) currentMin = res;\n        }\n        if\
        \ (idx < m) {\n            long long res = suffixMinFin[idx];\n            if\
        \ (res < currentMin) currentMin = res;\n        }\n        if (currentMin <\
        \ minFinish) minFinish = currentMin;\n    }\n\n    free(rides2);\n    free(prefixMinDur);\n\
        \    free(suffixMinFin);\n    return minFinish;\n}\n\nint earliestFinishTime(int*\
        \ landStartTime, int landStartTimeSize, int* landDuration, int landDurationSize,\
        \ int* waterStartTime, int waterStartTimeSize, int* waterDuration, int waterDurationSize)\
        \ {\n    long long res1 = solve(landStartTime, landDuration, landStartTimeSize,\
        \ waterStartTime, waterDuration, waterStartTimeSize);\n    long long res2 =\
        \ solve(waterStartTime, waterDuration, waterStartTimeSize, landStartTime, landDuration,\
        \ landStartTimeSize);\n    return (int)(res1 < res2 ? res1 : res2);\n}"
      csharp: "using System;\n\npublic class Solution {\n    public int EarliestFinishTime(int[]\
        \ landStartTime, int[] landDuration, int[] waterStartTime, int[] waterDuration)\
        \ {\n        int n = landStartTime.Length;\n        int m = waterStartTime.Length;\n\
        \n        long minFL = long.MaxValue;\n        for (int i = 0; i < n; i++) {\n\
        \            long finish = (long)landStartTime[i] + landDuration[i];\n     \
        \       if (finish < minFL) {\n                minFL = finish;\n           \
        \ }\n        }\n\n        long minFW = long.MaxValue;\n        for (int j =\
        \ 0; j < m; j++) {\n            long finish = (long)waterStartTime[j] + waterDuration[j];\n\
        \            if (finish < minFW) {\n                minFW = finish;\n      \
        \      }\n        }\n\n        long minTotal = long.MaxValue;\n\n        //\
        \ Order: Land then Water\n        for (int j = 0; j < m; j++) {\n          \
        \  long currentFinish = Math.Max(minFL, (long)waterStartTime[j]) + waterDuration[j];\n\
        \            if (currentFinish < minTotal) {\n                minTotal = currentFinish;\n\
        \            }\n        }\n\n        // Order: Water then Land\n        for\
        \ (int i = 0; i < n; i++) {\n            long currentFinish = Math.Max(minFW,\
        \ (long)landStartTime[i]) + landDuration[i];\n            if (currentFinish\
        \ < minTotal) {\n                minTotal = currentFinish;\n            }\n\
        \        }\n\n        return (int)minTotal;\n    }\n}"
      javascript: "/**\n * @param {number[]} landStartTime\n * @param {number[]} landDuration\n\
        \ * @param {number[]} waterStartTime\n * @param {number[]} waterDuration\n *\
        \ @return {number}\n */\nvar earliestFinishTime = function(landStartTime, landDuration,\
        \ waterStartTime, waterDuration) {\n    let minFL = Infinity;\n    const n =\
        \ landStartTime.length;\n    for (let i = 0; i < n; i++) {\n        const finish\
        \ = landStartTime[i] + landDuration[i];\n        if (finish < minFL) {\n   \
        \         minFL = finish;\n        }\n    }\n\n    let minFW = Infinity;\n \
        \   const m = waterStartTime.length;\n    for (let j = 0; j < m; j++) {\n  \
        \      const finish = waterStartTime[j] + waterDuration[j];\n        if (finish\
        \ < minFW) {\n            minFW = finish;\n        }\n    }\n\n    let minTotal\
        \ = Infinity;\n\n    // Order: Land then Water\n    for (let j = 0; j < m; j++)\
        \ {\n        const currentFinish = Math.max(minFL, waterStartTime[j]) + waterDuration[j];\n\
        \        if (currentFinish < minTotal) {\n            minTotal = currentFinish;\n\
        \        }\n    }\n\n    // Order: Water then Land\n    for (let i = 0; i <\
        \ n; i++) {\n        const currentFinish = Math.max(minFW, landStartTime[i])\
        \ + landDuration[i];\n        if (currentFinish < minTotal) {\n            minTotal\
        \ = currentFinish;\n        }\n    }\n\n    return minTotal;\n};"
      typescript: "function earliestFinishTime(landStartTime: number[], landDuration:\
        \ number[], waterStartTime: number[], waterDuration: number[]): number {\n \
        \   let minFL = Infinity;\n    const n = landStartTime.length;\n    for (let\
        \ i = 0; i < n; i++) {\n        const finish = landStartTime[i] + landDuration[i];\n\
        \        if (finish < minFL) {\n            minFL = finish;\n        }\n   \
        \ }\n\n    let minFW = Infinity;\n    const m = waterStartTime.length;\n   \
        \ for (let j = 0; j < m; j++) {\n        const finish = waterStartTime[j] +\
        \ waterDuration[j];\n        if (finish < minFW) {\n            minFW = finish;\n\
        \        }\n    }\n\n    let minTotal = Infinity;\n\n    // Order: Land then\
        \ Water\n    for (let j = 0; j < m; j++) {\n        const currentFinish = Math.max(minFL,\
        \ waterStartTime[j]) + waterDuration[j];\n        if (currentFinish < minTotal)\
        \ {\n            minTotal = currentFinish;\n        }\n    }\n\n    // Order:\
        \ Water then Land\n    for (let i = 0; i < n; i++) {\n        const currentFinish\
        \ = Math.max(minFW, landStartTime[i]) + landDuration[i];\n        if (currentFinish\
        \ < minTotal) {\n            minTotal = currentFinish;\n        }\n    }\n\n\
        \    return minTotal;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $landStartTime\n  \
        \   * @param Integer[] $landDuration\n     * @param Integer[] $waterStartTime\n\
        \     * @param Integer[] $waterDuration\n     * @return Integer\n     */\n \
        \   function earliestFinishTime($landStartTime, $landDuration, $waterStartTime,\
        \ $waterDuration) {\n        $minFL = PHP_INT_MAX;\n        $n = count($landStartTime);\n\
        \        for ($i = 0; $i < $n; $i++) {\n            $finish = $landStartTime[$i]\
        \ + $landDuration[$i];\n            if ($finish < $minFL) {\n              \
        \  $minFL = $finish;\n            }\n        }\n\n        $minFW = PHP_INT_MAX;\n\
        \        $m = count($waterStartTime);\n        for ($j = 0; $j < $m; $j++) {\n\
        \            $finish = $waterStartTime[$j] + $waterDuration[$j];\n         \
        \   if ($finish < $minFW) {\n                $minFW = $finish;\n           \
        \ }\n        }\n\n        $minTotal = PHP_INT_MAX;\n\n        // Order: Land\
        \ then Water\n        for ($j = 0; $j < $m; $j++) {\n            $currentFinish\
        \ = max($minFL, $waterStartTime[$j]) + $waterDuration[$j];\n            if ($currentFinish\
        \ < $minTotal) {\n                $minTotal = $currentFinish;\n            }\n\
        \        }\n\n        // Order: Water then Land\n        for ($i = 0; $i < $n;\
        \ $i++) {\n            $currentFinish = max($minFW, $landStartTime[$i]) + $landDuration[$i];\n\
        \            if ($currentFinish < $minTotal) {\n                $minTotal =\
        \ $currentFinish;\n            }\n        }\n\n        return (int)$minTotal;\n\
        \    }\n}"
      swift: "class Solution {\n    func earliestFinishTime(_ landStartTime: [Int],\
        \ _ landDuration: [Int], _ waterStartTime: [Int], _ waterDuration: [Int]) ->\
        \ Int {\n        let n = landStartTime.count\n        let m = waterStartTime.count\n\
        \n        var minFL = Int.max\n        for i in 0..<n {\n            let finish\
        \ = landStartTime[i] + landDuration[i]\n            if finish < minFL {\n  \
        \              minFL = finish\n            }\n        }\n\n        var minFW\
        \ = Int.max\n        for j in 0..<m {\n            let finish = waterStartTime[j]\
        \ + waterDuration[j]\n            if finish < minFW {\n                minFW\
        \ = finish\n            }\n        }\n\n        var minTotal = Int.max\n\n \
        \       // Order: Land then Water\n        for j in 0..<m {\n            let\
        \ currentFinish = max(minFL, waterStartTime[j]) + waterDuration[j]\n       \
        \     if currentFinish < minTotal {\n                minTotal = currentFinish\n\
        \            }\n        }\n\n        // Order: Water then Land\n        for\
        \ i in 0..<n {\n            let currentFinish = max(minFW, landStartTime[i])\
        \ + landDuration[i]\n            if currentFinish < minTotal {\n           \
        \     minTotal = currentFinish\n            }\n        }\n\n        return minTotal\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun earliestFinishTime(landStartTime: IntArray,\
        \ landDuration: IntArray, waterStartTime: IntArray, waterDuration: IntArray):\
        \ Int {\n        val res1 = solve(landStartTime, landDuration, waterStartTime,\
        \ waterDuration)\n        val res2 = solve(waterStartTime, waterDuration, landStartTime,\
        \ landDuration)\n        return if (res1 < res2) res1 else res2\n    }\n\n \
        \   private fun solve(starts1: IntArray, durations1: IntArray, starts2: IntArray,\
        \ durations2: IntArray): Int {\n        val m = starts2.size\n        val indices\
        \ = Array(m) { it }\n        indices.sortBy { starts2[it] }\n\n        val prefMinDur\
        \ = IntArray(m)\n        prefMinDur[0] = durations2[indices[0]]\n        for\
        \ (j in 1 until m) {\n            prefMinDur[j] = if (prefMinDur[j - 1] < durations2[indices[j]])\
        \ prefMinDur[j - 1] else durations2[indices[j]]\n        }\n\n        val sufMinFinish\
        \ = IntArray(m)\n        sufMinFinish[m - 1] = starts2[indices[m - 1]] + durations2[indices[m\
        \ - 1]]\n        for (j in m - 2 downTo 0) {\n            val currentFinish\
        \ = starts2[indices[j]] + durations2[indices[j]]\n            sufMinFinish[j]\
        \ = if (sufMinFinish[j + 1] < currentFinish) sufMinFinish[j + 1] else currentFinish\n\
        \        }\n\n        var minF2 = Int.MAX_VALUE\n        for (i in starts1.indices)\
        \ {\n            val f1 = starts1[i] + durations1[i]\n\n            var low\
        \ = 0\n            var high = m\n            while (low < high) {\n        \
        \        val mid = (low + high) / 2\n                if (starts2[indices[mid]]\
        \ <= f1) {\n                    low = mid + 1\n                } else {\n  \
        \                  high = mid\n                }\n            }\n          \
        \  val idx = low\n\n            var currentCandidate = Int.MAX_VALUE\n     \
        \       if (idx > 0) {\n                val candidate = f1 + prefMinDur[idx\
        \ - 1]\n                if (candidate < currentCandidate) currentCandidate =\
        \ candidate\n            }\n            if (idx < m) {\n                if (sufMinFinish[idx]\
        \ < currentCandidate) currentCandidate = sufMinFinish[idx]\n            }\n\
        \            if (currentCandidate < minF2) minF2 = currentCandidate\n      \
        \  }\n        return minF2\n    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int earliestFinishTime(List<int>\
        \ landStartTime, List<int> landDuration, List<int> waterStartTime, List<int>\
        \ waterDuration) {\n    int res1 = solve(landStartTime, landDuration, waterStartTime,\
        \ waterDuration);\n    int res2 = solve(waterStartTime, waterDuration, landStartTime,\
        \ landDuration);\n    return min(res1, res2);\n  }\n\n  int solve(List<int>\
        \ starts1, List<int> durations1, List<int> starts2, List<int> durations2) {\n\
        \    int m = starts2.length;\n    List<int> indices = List.generate(m, (i) =>\
        \ i);\n    indices.sort((a, b) => starts2[a].compareTo(starts2[b]));\n\n   \
        \ List<int> prefMinDur = List.filled(m, 0);\n    prefMinDur[0] = durations2[indices[0]];\n\
        \    for (int j = 1; j < m; j++) {\n      prefMinDur[j] = min(prefMinDur[j -\
        \ 1], durations2[indices[j]]);\n    }\n\n    List<int> sufMinFinish = List.filled(m,\
        \ 0);\n    sufMinFinish[m - 1] = starts2[indices[m - 1]] + durations2[indices[m\
        \ - 1]];\n    for (int j = m - 2; j >= 0; j--) {\n      sufMinFinish[j] = min(sufMinFinish[j\
        \ + 1], starts2[indices[j]] + durations2[indices[j]]);\n    }\n\n    int minF2\
        \ = 2000000000;\n    for (int i = 0; i < starts1.length; i++) {\n      int f1\
        \ = starts1[i] + durations1[i];\n\n      int low = 0;\n      int high = m;\n\
        \      while (low < high) {\n        int mid = (low + high) ~/ 2;\n        if\
        \ (starts2[indices[mid]] <= f1) {\n          low = mid + 1;\n        } else\
        \ {\n          high = mid;\n        }\n      }\n      int idx = low;\n\n   \
        \   int currentCandidate = 2000000000;\n      if (idx > 0) {\n        currentCandidate\
        \ = min(currentCandidate, f1 + prefMinDur[idx - 1]);\n      }\n      if (idx\
        \ < m) {\n        currentCandidate = min(currentCandidate, sufMinFinish[idx]);\n\
        \      }\n      minF2 = min(minF2, currentCandidate);\n    }\n    return minF2;\n\
        \  }\n}"
      go: "import \"sort\"\n\nfunc solve(starts1 []int, durations1 []int, starts2 []int,\
        \ durations2 []int) int {\n\tm := len(starts2)\n\ttype ride struct {\n\t\ts,\
        \ d int\n\t}\n\trides2 := make([]ride, m)\n\tfor i := 0; i < m; i++ {\n\t\t\
        rides2[i] = ride{starts2[i], durations2[i]}\n\t}\n\tsort.Slice(rides2, func(i,\
        \ j int) bool {\n\t\treturn rides2[i].s < rides2[j].s\n\t})\n\n\tprefMinDur\
        \ := make([]int, m)\n\tprefMinDur[0] = rides2[0].d\n\tfor i := 1; i < m; i++\
        \ {\n\t\tprefMinDur[i] = prefMinDur[i-1]\n\t\tif rides2[i].d < prefMinDur[i]\
        \ {\n\t\t\tprefMinDur[i] = rides2[i].d\n\t\t}\n\t}\n\n\tsufMinFinish := make([]int,\
        \ m)\n\tsufMinFinish[m-1] = rides2[m-1].s + rides2[m-1].d\n\tfor i := m - 2;\
        \ i >= 0; i-- {\n\t\tsufMinFinish[i] = sufMinFinish[i+1]\n\t\tfinish := rides2[i].s\
        \ + rides2[i].d\n\t\tif finish < sufMinFinish[i] {\n\t\t\tsufMinFinish[i] =\
        \ finish\n\t\t}\n\t}\n\n\tminTotal := 2000000000\n\tfor i := 0; i < len(starts1);\
        \ i++ {\n\t\tf1 := starts1[i] + durations1[i]\n\t\tidx := sort.Search(m, func(j\
        \ int) bool {\n\t\t\treturn rides2[j].s > f1\n\t\t})\n\n\t\tres := 2000000000\n\
        \t\tif idx > 0 {\n\t\t\tif f1+prefMinDur[idx-1] < res {\n\t\t\t\tres = f1 +\
        \ prefMinDur[idx-1]\n\t\t\t}\n\t\t}\n\t\tif idx < m {\n\t\t\tif sufMinFinish[idx]\
        \ < res {\n\t\t\t\tres = sufMinFinish[idx]\n\t\t\t}\n\t\t}\n\t\tif res < minTotal\
        \ {\n\t\t\tminTotal = res\n\t\t}\n\t}\n\treturn minTotal\n}\n\nfunc earliestFinishTime(landStartTime\
        \ []int, landDuration []int, waterStartTime []int, waterDuration []int) int\
        \ {\n\tans1 := solve(landStartTime, landDuration, waterStartTime, waterDuration)\n\
        \tans2 := solve(waterStartTime, waterDuration, landStartTime, landDuration)\n\
        \tif ans1 < ans2 {\n\t\treturn ans1\n\t}\n\treturn ans2\n}"
      ruby: "# @param {Integer[]} land_start_time\n# @param {Integer[]} land_duration\n\
        # @param {Integer[]} water_start_time\n# @param {Integer[]} water_duration\n\
        # @return {Integer}\ndef earliest_finish_time(land_start_time, land_duration,\
        \ water_start_time, water_duration)\n  ans1 = solve(land_start_time, land_duration,\
        \ water_start_time, water_duration)\n  ans2 = solve(water_start_time, water_duration,\
        \ land_start_time, land_duration)\n  [ans1, ans2].min\nend\n\ndef solve(starts1,\
        \ durations1, starts2, durations2)\n  m = starts2.length\n  rides2 = starts2.zip(durations2).sort_by!\
        \ { |r| r[0] }\n\n  pref_min_dur = Array.new(m)\n  pref_min_dur[0] = rides2[0][1]\n\
        \  (1...m).each do |j|\n    pref_min_dur[j] = [pref_min_dur[j - 1], rides2[j][1]].min\n\
        \  end\n\n  suf_min_finish = Array.new(m)\n  suf_min_finish[m - 1] = rides2[m\
        \ - 1][0] + rides2[m - 1][1]\n  (m - 2).downto(0) do |j|\n    suf_min_finish[j]\
        \ = [suf_min_finish[j + 1], rides2[j][0] + rides2[j][1]].min\n  end\n\n  min_f2\
        \ = 2000000000\n  starts1.each_with_index do |s1, i|\n    f1 = s1 + durations1[i]\n\
        \    idx = rides2.bsearch_index { |r| r[0] > f1 } || m\n\n    res = 2000000000\n\
        \    if idx > 0\n      res = [res, f1 + pref_min_dur[idx - 1]].min\n    end\n\
        \    if idx < m\n      res = [res, suf_min_finish[idx]].min\n    end\n    min_f2\
        \ = [min_f2, res].min\n  end\n  min_f2\nend"
      scala: "object Solution {\n  def earliestFinishTime(landStartTime: Array[Int],\
        \ landDuration: Array[Int], waterStartTime: Array[Int], waterDuration: Array[Int]):\
        \ Int = {\n    val ans1 = solve(landStartTime, landDuration, waterStartTime,\
        \ waterDuration)\n    val ans2 = solve(waterStartTime, waterDuration, landStartTime,\
        \ landDuration)\n    math.min(ans1, ans2)\n  }\n\n  def solve(starts1: Array[Int],\
        \ durations1: Array[Int], starts2: Array[Int], durations2: Array[Int]): Int\
        \ = {\n    val m = starts2.length\n    val rides2 = starts2.zip(durations2).sortBy(_._1)\n\
        \n    val prefMinDur = new Array[Int](m)\n    prefMinDur(0) = rides2(0)._2\n\
        \    for (j <- 1 until m) {\n      prefMinDur(j) = math.min(prefMinDur(j - 1),\
        \ rides2(j)._2)\n    }\n\n    val sufMinFinish = new Array[Int](m)\n    sufMinFinish(m\
        \ - 1) = rides2(m - 1)._1 + rides2(m - 1)._2\n    for (j <- m - 2 to 0 by -1)\
        \ {\n      sufMinFinish(j) = math.min(sufMinFinish(j + 1), rides2(j)._1 + rides2(j)._2)\n\
        \    }\n\n    var minF2 = Int.MaxValue\n    for (i <- starts1.indices) {\n \
        \     val f1 = starts1(i) + durations1(i)\n\n      var low = 0\n      var high\
        \ = m\n      while (low < high) {\n        val mid = (low + high) / 2\n    \
        \    if (rides2(mid)._1 <= f1) {\n          low = mid + 1\n        } else {\n\
        \          high = mid\n        }\n      }\n      val idx = low\n\n      var\
        \ res = Int.MaxValue\n      if (idx > 0) {\n        res = math.min(res, f1 +\
        \ prefMinDur(idx - 1))\n      }\n      if (idx < m) {\n        res = math.min(res,\
        \ sufMinFinish(idx))\n      }\n      minF2 = math.min(minF2, res)\n    }\n \
        \   minF2\n  }\n}"
      rust: "impl Solution {\n    pub fn earliest_finish_time(land_start_time: Vec<i32>,\
        \ land_duration: Vec<i32>, water_start_time: Vec<i32>, water_duration: Vec<i32>)\
        \ -> i32 {\n        fn solve(a: &[(i32, i32)], b: &[(i32, i32)]) -> i32 {\n\
        \            let mut a_sorted = a.to_vec();\n            a_sorted.sort_unstable_by_key(|&(s,\
        \ d)| s + d);\n\n            let mut b_sorted = b.to_vec();\n            b_sorted.sort_unstable_by_key(|&(s,\
        \ _d)| s);\n\n            let m = b_sorted.len();\n            let mut suffix_min_finish\
        \ = vec![2000000000; m + 1];\n            for i in (0..m).rev() {\n        \
        \        suffix_min_finish[i] = suffix_min_finish[i + 1].min(b_sorted[i].0 +\
        \ b_sorted[i].1);\n            }\n\n            let mut best = 2000000000;\n\
        \            let mut k = 0;\n            let mut prefix_min_dur = 2000000000;\n\
        \            for &(sa, da) in &a_sorted {\n                let fa = sa + da;\n\
        \                while k < m && b_sorted[k].0 <= fa {\n                    prefix_min_dur\
        \ = prefix_min_dur.min(b_sorted[k].1);\n                    k += 1;\n      \
        \          }\n                if prefix_min_dur != 2000000000 {\n          \
        \          best = best.min(fa + prefix_min_dur);\n                }\n      \
        \          best = best.min(suffix_min_finish[k]);\n            }\n         \
        \   best\n        }\n\n        let land: Vec<(i32, i32)> = land_start_time.into_iter().zip(land_duration.into_iter()).collect();\n\
        \        let water: Vec<(i32, i32)> = water_start_time.into_iter().zip(water_duration.into_iter()).collect();\n\
        \n        solve(&land, &water).min(solve(&water, &land))\n    }\n}"
      racket: "(define/contract (earliest-finish-time landStartTime landDuration waterStartTime\
        \ waterDuration)\n  (-> (listof exact-integer?) (listof exact-integer?) (listof\
        \ exact-integer?) (listof exact-integer?) exact-integer?)\n  (define (solve\
        \ a b)\n    (let* ([a-sorted (sort a < #:key (lambda (x) (+ (car x) (cdr x))))]\n\
        \           [b-sorted (list->vector (sort b < #:key (lambda (x) (car x))))]\n\
        \           [m (vector-length b-sorted)]\n           [suffix-min-finish (make-vector\
        \ (+ m 1) 2000000000)])\n      (for ([i (in-range (- m 1) -1 -1)])\n       \
        \ (let ([b-val (vector-ref b-sorted i)])\n          (vector-set! suffix-min-finish\
        \ i (min (vector-ref suffix-min-finish (+ i 1)) (+ (car b-val) (cdr b-val))))))\n\
        \      (let loop ([a-list a-sorted] [k 0] [prefix-min-dur 2000000000] [best\
        \ 2000000000])\n        (if (null? a-list)\n            best\n            (let*\
        \ ([a-ride (car a-list)]\n                   [fa (+ (car a-ride) (cdr a-ride))])\n\
        \              (let-values ([(new-k new-prefix-min-dur)\n                  \
        \          (let inner-loop ([curr-k k] [curr-prefix-min-dur prefix-min-dur])\n\
        \                              (if (and (< curr-k m) (<= (car (vector-ref b-sorted\
        \ curr-k)) fa))\n                                  (inner-loop (+ curr-k 1)\
        \ (min curr-prefix-min-dur (cdr (vector-ref b-sorted curr-k))))\n          \
        \                        (values curr-k curr-prefix-min-dur)))])\n         \
        \       (let* ([res1 (if (= new-prefix-min-dur 2000000000) 2000000000 (+ fa\
        \ new-prefix-min-dur))]\n                       [res2 (vector-ref suffix-min-finish\
        \ new-k)]\n                       [new-best (min best res1 res2)])\n       \
        \           (loop (cdr a-list) new-k new-prefix-min-dur new-best))))))))\n\n\
        \  (let ([land (map cons landStartTime landDuration)]\n        [water (map cons\
        \ waterStartTime waterDuration)])\n    (min (solve land water) (solve water\
        \ land))))"
      erlang: "-spec earliest_finish_time(LandStartTime :: [integer()], LandDuration\
        \ :: [integer()], WaterStartTime :: [integer()], WaterDuration :: [integer()])\
        \ -> integer().\nearliest_finish_time(LandStartTime, LandDuration, WaterStartTime,\
        \ WaterDuration) ->\n  Land = lists:zip(LandStartTime, LandDuration),\n  Water\
        \ = lists:zip(WaterStartTime, WaterDuration),\n  min(solve(Land, Water), solve(Water,\
        \ Land)).\n\nsolve(A, B) ->\n  ASorted = lists:sort(fun({S1, D1}, {S2, D2})\
        \ -> (S1 + D1) =< (S2 + D2) end, A),\n  BSorted = lists:sort(fun({S1, _D1},\
        \ {S2, _D2}) -> S1 =< S2 end, B),\n  SuffixMinFinish = build_suffix_min_finish(BSorted),\n\
        \  solve_tp(ASorted, BSorted, SuffixMinFinish, 2000000000, 2000000000).\n\n\
        build_suffix_min_finish(BSorted) ->\n  lists:foldr(fun({S, D}, Acc) ->\n   \
        \ [MinSoFar | _] = Acc,\n    [min(MinSoFar, S + D) | Acc]\n  end, [2000000000],\
        \ BSorted).\n\nsolve_tp([], _BSorted, _SuffixMinFinish, _PrefixMinDur, Best)\
        \ ->\n  Best;\nsolve_tp([{SA, DA} | ATail], BSorted, SuffixMinFinish, PrefixMinDur,\
        \ Best) ->\n  FA = SA + DA,\n  {NewBSorted, NewSuffixMinFinish, NewPrefixMinDur}\
        \ = advance_b(BSorted, SuffixMinFinish, PrefixMinDur, FA),\n  Res1 = if NewPrefixMinDur\
        \ == 2000000000 -> 2000000000; true -> FA + NewPrefixMinDur end,\n  Res2 = hd(NewSuffixMinFinish),\n\
        \  NewBest = min(Best, min(Res1, Res2)),\n  solve_tp(ATail, NewBSorted, NewSuffixMinFinish,\
        \ NewPrefixMinDur, NewBest).\n\nadvance_b([{SB, DB} | BTail], [_ | STail], PrefixMinDur,\
        \ FA) when SB =< FA ->\n  advance_b(BTail, STail, min(PrefixMinDur, DB), FA);\n\
        advance_b(BSorted, SuffixMinFinish, PrefixMinDur, _FA) ->\n  {BSorted, SuffixMinFinish,\
        \ PrefixMinDur}."
      elixir: "defmodule Solution do\n  @spec earliest_finish_time(land_start_time ::\
        \ [integer], land_duration :: [integer], water_start_time :: [integer], water_duration\
        \ :: [integer]) :: integer\n  def earliest_finish_time(land_start_time, land_duration,\
        \ water_start_time, water_duration) do\n    land = Enum.zip(land_start_time,\
        \ land_duration)\n    water = Enum.zip(water_start_time, water_duration)\n \
        \   min(solve(land, water), solve(water, land))\n  end\n\n  defp solve(a, b)\
        \ do\n    a_sorted = Enum.sort_by(a, fn {s, d} -> s + d end)\n    b_sorted =\
        \ Enum.sort_by(b, fn {s, _d} -> s end)\n    suffix_min_finish = build_suffix_min_finish(b_sorted)\n\
        \    solve_tp(a_sorted, b_sorted, suffix_min_finish, 2000000000, 2000000000)\n\
        \  end\n\n  defp build_suffix_min_finish(b_sorted) do\n    b_sorted\n    |>\
        \ Enum.reverse()\n    |> Enum.reduce([2000000000], fn {s, d}, [min_so_far |\
        \ _] = acc ->\n      [min(min_so_far, s + d) | acc]\n    end)\n  end\n\n  defp\
        \ solve_tp([], _b_sorted, _suffix_min_finish, _prefix_min_dur, best) do\n  \
        \  best\n  end\n\n  defp solve_tp([{sa, da} | a_tail], b_sorted, suffix_min_finish,\
        \ prefix_min_dur, best) do\n    fa = sa + da\n    {new_b_sorted, new_suffix_min_finish,\
        \ new_prefix_min_dur} = advance_b(b_sorted, suffix_min_finish, prefix_min_dur,\
        \ fa)\n    res1 = if new_prefix_min_dur == 2000000000, do: 2000000000, else:\
        \ fa + new_prefix_min_dur\n    res2 = hd(new_suffix_min_finish)\n    new_best\
        \ = min(best, min(res1, res2))\n    solve_tp(a_tail, new_b_sorted, new_suffix_min_finish,\
        \ new_prefix_min_dur, new_best)\n  end\n\n  defp advance_b([{sb, db} | b_tail],\
        \ [_ | s_tail], prefix_min_dur, fa) when sb <= fa do\n    advance_b(b_tail,\
        \ s_tail, min(prefix_min_dur, db), fa)\n  end\n\n  defp advance_b(b_sorted,\
        \ suffix_min_finish, prefix_min_dur, _fa) do\n    {b_sorted, suffix_min_finish,\
        \ prefix_min_dur}\n  end\nend"
    approach: "To find the earliest finish time, we consider the two possible sequences:\
      \ starting with a land ride followed by a water ride, or starting with a water\
      \ ride followed by a land ride. For a fixed sequence, say Category A then Category\
      \ B, the finish time of the first ride is $F_1 = start_1 + duration_1$. The finish\
      \ time of the second ride is $\\max(F_1, start_2) + duration_2$. To minimize this\
      \ for a given $F_1$, we split Category B rides into two groups based on their\
      \ start times: those where $start_2 \\le F_1$, resulting in a finish time of $F_1\
      \ + duration_2$, and those where $start_2 > F_1$, resulting in a finish time of\
      \ $start_2 + duration_2$. \n\nWe optimize the search for the best ride in Category\
      \ B by first sorting the Category B rides by their start times. We then precompute\
      \ two auxiliary arrays: a prefix minimum array of durations to quickly find the\
      \ smallest $duration_2$ for the first group, and a suffix minimum array of $(start_2\
      \ + duration_2)$ for the second group. For each ride in Category A, we use binary\
      \ search to find the split point in the sorted Category B rides and evaluate the\
      \ minimum finish time using the precomputed values. We repeat this logic for the\
      \ reverse order and return the global minimum."
    time_complexity: O((N + M) log (N + M)) where N and M are the number of land and
      water rides respectively. This accounts for sorting both lists of rides and performing
      binary search for each ride during the evaluation phase.
    space_complexity: O(N + M) to store the sorted ride information and the prefix/suffix
      precomputation arrays.
    elapsed_time: 229.60161209106445
    model: gemini-3-flash-preview
    generated_at: '2026-06-03 03:03:12 '
---

## Problem #3635: Earliest Finish Time for Land and Water Rides II

**Difficulty:** Medium

**Topics:** Array, Two Pointers, Binary Search, Greedy, Sorting

## Problem Description

<p data-end="143" data-start="53">You are given two categories of theme park attractions: <strong data-end="122" data-start="108">land rides</strong> and <strong data-end="142" data-start="127">water rides</strong>.</p>

<ul>
	<li data-end="163" data-start="147"><strong data-end="161" data-start="147">Land rides</strong>

	<ul>
		<li data-end="245" data-start="168"><code data-end="186" data-start="168">landStartTime[i]</code> &ndash; the earliest time the <code>i<sup>th</sup></code> land ride can be boarded.</li>
		<li data-end="306" data-start="250"><code data-end="267" data-start="250">landDuration[i]</code> &ndash; how long the <code>i<sup>th</sup></code> land ride lasts.</li>
	</ul>
	</li>
	<li><strong data-end="325" data-start="310">Water rides</strong>
	<ul>
		<li><code data-end="351" data-start="332">waterStartTime[j]</code> &ndash; the earliest time the <code>j<sup>th</sup></code> water ride can be boarded.</li>
		<li><code data-end="434" data-start="416">waterDuration[j]</code> &ndash; how long the <code>j<sup>th</sup></code> water ride lasts.</li>
	</ul>
	</li>
</ul>

<p data-end="569" data-start="476">A tourist must experience <strong data-end="517" data-start="502">exactly one</strong> ride from <strong data-end="536" data-start="528">each</strong> category, in <strong data-end="566" data-start="550">either order</strong>.</p>

<ul>
	<li data-end="641" data-start="573">A ride may be started at its opening time or <strong data-end="638" data-start="618">any later moment</strong>.</li>
	<li data-end="715" data-start="644">If a ride is started at time <code data-end="676" data-start="673">t</code>, it finishes at time <code data-end="712" data-start="698">t + duration</code>.</li>
	<li data-end="834" data-start="718">Immediately after finishing one ride the tourist may board the other (if it is already open) or wait until it opens.</li>
</ul>

<p data-end="917" data-start="836">Return the <strong data-end="873" data-start="847">earliest possible time</strong> at which the tourist can finish both rides.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">landStartTime = [2,8], landDuration = [4,1], waterStartTime = [6], waterDuration = [3]</span></p>

<p><strong>Output:</strong> <span class="example-io">9</span></p>

<p><strong>Explanation:</strong>​​​​​​​</p>

<ul>
	<li data-end="181" data-start="145">Plan A (land ride 0 &rarr; water ride 0):
	<ul>
		<li data-end="272" data-start="186">Start land ride 0 at time <code data-end="234" data-start="212">landStartTime[0] = 2</code>. Finish at <code data-end="271" data-start="246">2 + landDuration[0] = 6</code>.</li>
		<li data-end="392" data-start="277">Water ride 0 opens at time <code data-end="327" data-start="304">waterStartTime[0] = 6</code>. Start immediately at <code data-end="353" data-start="350">6</code>, finish at <code data-end="391" data-start="365">6 + waterDuration[0] = 9</code>.</li>
	</ul>
	</li>
	<li data-end="432" data-start="396">Plan B (water ride 0 &rarr; land ride 1):
	<ul>
		<li data-end="526" data-start="437">Start water ride 0 at time <code data-end="487" data-start="464">waterStartTime[0] = 6</code>. Finish at <code data-end="525" data-start="499">6 + waterDuration[0] = 9</code>.</li>
		<li data-end="632" data-start="531">Land ride 1 opens at <code data-end="574" data-start="552">landStartTime[1] = 8</code>. Start at time <code data-end="593" data-start="590">9</code>, finish at <code data-end="631" data-start="605">9 + landDuration[1] = 10</code>.</li>
	</ul>
	</li>
	<li data-end="672" data-start="636">Plan C (land ride 1 &rarr; water ride 0):
	<ul>
		<li data-end="763" data-start="677">Start land ride 1 at time <code data-end="725" data-start="703">landStartTime[1] = 8</code>. Finish at <code data-end="762" data-start="737">8 + landDuration[1] = 9</code>.</li>
		<li data-end="873" data-start="768">Water ride 0 opened at <code data-end="814" data-start="791">waterStartTime[0] = 6</code>. Start at time <code data-end="833" data-start="830">9</code>, finish at <code data-end="872" data-start="845">9 + waterDuration[0] = 12</code>.</li>
	</ul>
	</li>
	<li data-end="913" data-start="877">Plan D (water ride 0 &rarr; land ride 0):
	<ul>
		<li data-end="1007" data-start="918">Start water ride 0 at time <code data-end="968" data-start="945">waterStartTime[0] = 6</code>. Finish at <code data-end="1006" data-start="980">6 + waterDuration[0] = 9</code>.</li>
		<li data-end="1114" data-start="1012">Land ride 0 opened at <code data-end="1056" data-start="1034">landStartTime[0] = 2</code>. Start at time <code data-end="1075" data-start="1072">9</code>, finish at <code data-end="1113" data-start="1087">9 + landDuration[0] = 13</code>.</li>
	</ul>
	</li>
</ul>

<p data-end="1161" data-is-last-node="" data-is-only-node="" data-start="1116">Plan A gives the earliest finish time of 9.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">landStartTime = [5], landDuration = [3], waterStartTime = [1], waterDuration = [10]</span></p>

<p><strong>Output:</strong> <span class="example-io">14</span></p>

<p><strong>Explanation:</strong>​​​​​​​</p>

<ul data-end="1589" data-start="1086">
	<li data-end="1124" data-start="1088">Plan A (water ride 0 &rarr; land ride 0):
	<ul>
		<li data-end="1219" data-start="1129">Start water ride 0 at time <code data-end="1179" data-start="1156">waterStartTime[0] = 1</code>. Finish at <code data-end="1218" data-start="1191">1 + waterDuration[0] = 11</code>.</li>
		<li data-end="1338" data-start="1224">Land ride 0 opened at <code data-end="1268" data-start="1246">landStartTime[0] = 5</code>. Start immediately at <code data-end="1295" data-start="1291">11</code> and finish at <code data-end="1337" data-start="1310">11 + landDuration[0] = 14</code>.</li>
	</ul>
	</li>
	<li data-end="1378" data-start="1342">Plan B (land ride 0 &rarr; water ride 0):
	<ul>
		<li data-end="1469" data-start="1383">Start land ride 0 at time <code data-end="1431" data-start="1409">landStartTime[0] = 5</code>. Finish at <code data-end="1468" data-start="1443">5 + landDuration[0] = 8</code>.</li>
		<li data-end="1589" data-start="1474">Water ride 0 opened at <code data-end="1520" data-start="1497">waterStartTime[0] = 1</code>. Start immediately at <code data-end="1546" data-start="1543">8</code> and finish at <code data-end="1588" data-start="1561">8 + waterDuration[0] = 18</code>.</li>
	</ul>
	</li>
</ul>

<p data-end="1640" data-is-last-node="" data-is-only-node="" data-start="1591">Plan A provides the earliest finish time of 14.<strong>​​​​​​​</strong></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li data-end="38" data-start="16"><code data-end="36" data-start="16">1 &lt;= n, m &lt;= 5 * 10<sup>4</sup></code></li>
	<li data-end="93" data-start="41"><code data-end="91" data-start="41">landStartTime.length == landDuration.length == n</code></li>
	<li data-end="150" data-start="96"><code data-end="148" data-start="96">waterStartTime.length == waterDuration.length == m</code></li>
	<li data-end="237" data-start="153"><code data-end="235" data-start="153">1 &lt;= landStartTime[i], landDuration[i], waterStartTime[j], waterDuration[j] &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. Sort each ride list by opening time and build a prefix minimum of ride durations and a suffix minimum of ride finish times (`start + duration`).

2. Try both orders, land then water and water then land. For each ride in the first list compute `finish1 = start1 + duration1`.

3. Binary‑search the second list (sorted by `start`) to split rides into those with `start  finish1`. Use the prefix minimum duration on the early group to get an earliest finish of `finish1 + minDuration` and the suffix minimum finish time on the late group.

4. For each pairing take the smaller finish time and track the overall minimum.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To find the earliest finish time, we consider the two possible sequences: starting with a land ride followed by a water ride, or starting with a water ride followed by a land ride. For a fixed sequence, say Category A then Category B, the finish time of the first ride is $F_1 = start_1 + duration_1$. The finish time of the second ride is $\max(F_1, start_2) + duration_2$. To minimize this for a given $F_1$, we split Category B rides into two groups based on their start times: those where $start_2 \le F_1$, resulting in a finish time of $F_1 + duration_2$, and those where $start_2 > F_1$, resulting in a finish time of $start_2 + duration_2$. 

We optimize the search for the best ride in Category B by first sorting the Category B rides by their start times. We then precompute two auxiliary arrays: a prefix minimum array of durations to quickly find the smallest $duration_2$ for the first group, and a suffix minimum array of $(start_2 + duration_2)$ for the second group. For each ride in Category A, we use binary search to find the split point in the sorted Category B rides and evaluate the minimum finish time using the precomputed values. We repeat this logic for the reverse order and return the global minimum.

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
    long long solve(const vector<int>& s1, const vector<int>& d1, const vector<int>& s2, const vector<int>& d2) {
        int n = s1.size(), m = s2.size();
        vector<pair<int, int>> rides2(m);
        for (int i = 0; i < m; ++i) rides2[i] = {s2[i], d2[i]};
        sort(rides2.begin(), rides2.end());

        vector<int> prefixMinDur(m);
        prefixMinDur[0] = rides2[0].second;
        for (int i = 1; i < m; ++i) prefixMinDur[i] = min(prefixMinDur[i - 1], rides2[i].second);

        vector<long long> suffixMinFin(m);
        suffixMinFin[m - 1] = (long long)rides2[m - 1].first + rides2[m - 1].second;
        for (int i = m - 2; i >= 0; --i) suffixMinFin[i] = min(suffixMinFin[i + 1], (long long)rides2[i].first + rides2[i].second);

        long long minFinish = -1;

        for (int i = 0; i < n; ++i) {
            long long f1 = (long long)s1[i] + d1[i];
            auto it = upper_bound(rides2.begin(), rides2.end(), make_pair((int)f1, 2000000000));
            int idx = distance(rides2.begin(), it);

            long long currentMin = -1;
            if (idx > 0) {
                long long res = f1 + prefixMinDur[idx - 1];
                if (currentMin == -1 || res < currentMin) currentMin = res;
            }
            if (idx < m) {
                long long res = suffixMinFin[idx];
                if (currentMin == -1 || res < currentMin) currentMin = res;
            }
            if (minFinish == -1 || currentMin < minFinish) minFinish = currentMin;
        }
        return minFinish;
    }

    int earliestFinishTime(vector<int>& landStartTime, vector<int>& landDuration, vector<int>& waterStartTime, vector<int>& waterDuration) {
        return (int)min(solve(landStartTime, landDuration, waterStartTime, waterDuration), 
                        solve(waterStartTime, waterDuration, landStartTime, landDuration));
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
    static class Ride implements Comparable<Ride> {
        int start, duration;
        Ride(int s, int d) { start = s; duration = d; }
        public int compareTo(Ride other) { return Integer.compare(this.start, other.start); }
    }

    private long solve(int[] s1, int[] d1, int[] s2, int[] d2) {
        int n = s1.length, m = s2.length;
        Ride[] rides2 = new Ride[m];
        for (int i = 0; i < m; i++) rides2[i] = new Ride(s2[i], d2[i]);
        Arrays.sort(rides2);

        int[] prefixMinDur = new int[m];
        prefixMinDur[0] = rides2[0].duration;
        for (int i = 1; i < m; i++) prefixMinDur[i] = Math.min(prefixMinDur[i - 1], rides2[i].duration);

        long[] suffixMinFin = new long[m];
        suffixMinFin[m - 1] = (long) rides2[m - 1].start + rides2[m - 1].duration;
        for (int i = m - 2; i >= 0; i--) suffixMinFin[i] = Math.min(suffixMinFin[i + 1], (long) rides2[i].start + rides2[i].duration);

        long minFinish = Long.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            long f1 = (long) s1[i] + d1[i];
            int low = 0, high = m - 1, idx = 0;
            while (low <= high) {
                int mid = (low + high) / 2;
                if (rides2[mid].start <= f1) {
                    idx = mid + 1;
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }

            long currentMin = Long.MAX_VALUE;
            if (idx > 0) currentMin = Math.min(currentMin, f1 + prefixMinDur[idx - 1]);
            if (idx < m) currentMin = Math.min(currentMin, suffixMinFin[idx]);
            minFinish = Math.min(minFinish, currentMin);
        }
        return minFinish;
    }

    public int earliestFinishTime(int[] landStartTime, int[] landDuration, int[] waterStartTime, int[] waterDuration) {
        return (int) Math.min(solve(landStartTime, landDuration, waterStartTime, waterDuration),
                             solve(waterStartTime, waterDuration, landStartTime, landDuration));
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
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        def solve(s1, d1, s2, d2):
            m = len(s2)
            rides2 = sorted(zip(s2, d2))
            starts2 = [r[0] for r in rides2]
            durs2 = [r[1] for r in rides2]

            prefixMinDur = [0] * m
            prefixMinDur[0] = durs2[0]
            for i in range(1, m):
                prefixMinDur[i] = min(prefixMinDur[i-1], durs2[i])

            suffixMinFin = [0] * m
            suffixMinFin[m-1] = starts2[m-1] + durs2[m-1]
            for i in range(m-2, -1, -1):
                suffixMinFin[i] = min(suffixMinFin[i+1], starts2[i] + durs2[i])

            minFinish = float('inf')
            for i in range(len(s1)):
                f1 = s1[i] + d1[i]
                idx = bisect.bisect_right(starts2, f1)

                res = float('inf')
                if idx > 0:
                    res = min(res, f1 + prefixMinDur[idx-1])
                if idx < m:
                    res = min(res, suffixMinFin[idx])
                minFinish = min(minFinish, res)
            return minFinish

        res1 = solve(landStartTime, landDuration, waterStartTime, waterDuration)
        res2 = solve(waterStartTime, waterDuration, landStartTime, landDuration)
        return int(min(res1, res2))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import bisect

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def solve(s1, d1, s2, d2):
            m = len(s2)
            rides2 = sorted(zip(s2, d2))
            starts2 = [r[0] for r in rides2]
            durs2 = [r[1] for r in rides2]

            prefixMinDur = [0] * m
            prefixMinDur[0] = durs2[0]
            for i in range(1, m):
                prefixMinDur[i] = min(prefixMinDur[i-1], durs2[i])

            suffixMinFin = [0] * m
            suffixMinFin[m-1] = starts2[m-1] + durs2[m-1]
            for i in range(m-2, -1, -1):
                suffixMinFin[i] = min(suffixMinFin[i+1], starts2[i] + durs2[i])

            minFinish = float('inf')
            for i in range(len(s1)):
                f1 = s1[i] + d1[i]
                idx = bisect.bisect_right(starts2, f1)

                res = float('inf')
                if idx > 0:
                    res = min(res, f1 + prefixMinDur[idx-1])
                if idx < m:
                    res = min(res, suffixMinFin[idx])
                minFinish = min(minFinish, res)
            return minFinish

        res1 = solve(landStartTime, landDuration, waterStartTime, waterDuration)
        res2 = solve(waterStartTime, waterDuration, landStartTime, landDuration)
        return int(min(res1, res2))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

typedef struct {
    int start;
    int duration;
} Ride;

int compareRides(const void* a, const void* b) {
    return ((Ride*)a)->start - ((Ride*)b)->start;
}

long long solve(int* s1, int* d1, int n, int* s2, int* d2, int m) {
    Ride* rides2 = (Ride*)malloc(m * sizeof(Ride));
    for (int i = 0; i < m; i++) {
        rides2[i].start = s2[i];
        rides2[i].duration = d2[i];
    }
    qsort(rides2, m, sizeof(Ride), compareRides);

    int* prefixMinDur = (int*)malloc(m * sizeof(int));
    prefixMinDur[0] = rides2[0].duration;
    for (int i = 1; i < m; i++) {
        prefixMinDur[i] = (rides2[i].duration < prefixMinDur[i - 1]) ? rides2[i].duration : prefixMinDur[i - 1];
    }

    long long* suffixMinFin = (long long*)malloc(m * sizeof(long long));
    suffixMinFin[m - 1] = (long long)rides2[m - 1].start + rides2[m - 1].duration;
    for (int i = m - 2; i >= 0; i--) {
        long long fin = (long long)rides2[i].start + rides2[i].duration;
        suffixMinFin[i] = (fin < suffixMinFin[i + 1]) ? fin : suffixMinFin[i + 1];
    }

    long long minFinish = LLONG_MAX;
    for (int i = 0; i < n; i++) {
        long long f1 = (long long)s1[i] + d1[i];
        int low = 0, high = m - 1, idx = 0;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (rides2[mid].start <= f1) {
                idx = mid + 1;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        long long currentMin = LLONG_MAX;
        if (idx > 0) {
            long long res = f1 + prefixMinDur[idx - 1];
            if (res < currentMin) currentMin = res;
        }
        if (idx < m) {
            long long res = suffixMinFin[idx];
            if (res < currentMin) currentMin = res;
        }
        if (currentMin < minFinish) minFinish = currentMin;
    }

    free(rides2);
    free(prefixMinDur);
    free(suffixMinFin);
    return minFinish;
}

int earliestFinishTime(int* landStartTime, int landStartTimeSize, int* landDuration, int landDurationSize, int* waterStartTime, int waterStartTimeSize, int* waterDuration, int waterDurationSize) {
    long long res1 = solve(landStartTime, landDuration, landStartTimeSize, waterStartTime, waterDuration, waterStartTimeSize);
    long long res2 = solve(waterStartTime, waterDuration, waterStartTimeSize, landStartTime, landDuration, landStartTimeSize);
    return (int)(res1 < res2 ? res1 : res2);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public int EarliestFinishTime(int[] landStartTime, int[] landDuration, int[] waterStartTime, int[] waterDuration) {
        int n = landStartTime.Length;
        int m = waterStartTime.Length;

        long minFL = long.MaxValue;
        for (int i = 0; i < n; i++) {
            long finish = (long)landStartTime[i] + landDuration[i];
            if (finish < minFL) {
                minFL = finish;
            }
        }

        long minFW = long.MaxValue;
        for (int j = 0; j < m; j++) {
            long finish = (long)waterStartTime[j] + waterDuration[j];
            if (finish < minFW) {
                minFW = finish;
            }
        }

        long minTotal = long.MaxValue;

        // Order: Land then Water
        for (int j = 0; j < m; j++) {
            long currentFinish = Math.Max(minFL, (long)waterStartTime[j]) + waterDuration[j];
            if (currentFinish < minTotal) {
                minTotal = currentFinish;
            }
        }

        // Order: Water then Land
        for (int i = 0; i < n; i++) {
            long currentFinish = Math.Max(minFW, (long)landStartTime[i]) + landDuration[i];
            if (currentFinish < minTotal) {
                minTotal = currentFinish;
            }
        }

        return (int)minTotal;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} landStartTime
 * @param {number[]} landDuration
 * @param {number[]} waterStartTime
 * @param {number[]} waterDuration
 * @return {number}
 */
var earliestFinishTime = function(landStartTime, landDuration, waterStartTime, waterDuration) {
    let minFL = Infinity;
    const n = landStartTime.length;
    for (let i = 0; i < n; i++) {
        const finish = landStartTime[i] + landDuration[i];
        if (finish < minFL) {
            minFL = finish;
        }
    }

    let minFW = Infinity;
    const m = waterStartTime.length;
    for (let j = 0; j < m; j++) {
        const finish = waterStartTime[j] + waterDuration[j];
        if (finish < minFW) {
            minFW = finish;
        }
    }

    let minTotal = Infinity;

    // Order: Land then Water
    for (let j = 0; j < m; j++) {
        const currentFinish = Math.max(minFL, waterStartTime[j]) + waterDuration[j];
        if (currentFinish < minTotal) {
            minTotal = currentFinish;
        }
    }

    // Order: Water then Land
    for (let i = 0; i < n; i++) {
        const currentFinish = Math.max(minFW, landStartTime[i]) + landDuration[i];
        if (currentFinish < minTotal) {
            minTotal = currentFinish;
        }
    }

    return minTotal;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function earliestFinishTime(landStartTime: number[], landDuration: number[], waterStartTime: number[], waterDuration: number[]): number {
    let minFL = Infinity;
    const n = landStartTime.length;
    for (let i = 0; i < n; i++) {
        const finish = landStartTime[i] + landDuration[i];
        if (finish < minFL) {
            minFL = finish;
        }
    }

    let minFW = Infinity;
    const m = waterStartTime.length;
    for (let j = 0; j < m; j++) {
        const finish = waterStartTime[j] + waterDuration[j];
        if (finish < minFW) {
            minFW = finish;
        }
    }

    let minTotal = Infinity;

    // Order: Land then Water
    for (let j = 0; j < m; j++) {
        const currentFinish = Math.max(minFL, waterStartTime[j]) + waterDuration[j];
        if (currentFinish < minTotal) {
            minTotal = currentFinish;
        }
    }

    // Order: Water then Land
    for (let i = 0; i < n; i++) {
        const currentFinish = Math.max(minFW, landStartTime[i]) + landDuration[i];
        if (currentFinish < minTotal) {
            minTotal = currentFinish;
        }
    }

    return minTotal;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $landStartTime
     * @param Integer[] $landDuration
     * @param Integer[] $waterStartTime
     * @param Integer[] $waterDuration
     * @return Integer
     */
    function earliestFinishTime($landStartTime, $landDuration, $waterStartTime, $waterDuration) {
        $minFL = PHP_INT_MAX;
        $n = count($landStartTime);
        for ($i = 0; $i < $n; $i++) {
            $finish = $landStartTime[$i] + $landDuration[$i];
            if ($finish < $minFL) {
                $minFL = $finish;
            }
        }

        $minFW = PHP_INT_MAX;
        $m = count($waterStartTime);
        for ($j = 0; $j < $m; $j++) {
            $finish = $waterStartTime[$j] + $waterDuration[$j];
            if ($finish < $minFW) {
                $minFW = $finish;
            }
        }

        $minTotal = PHP_INT_MAX;

        // Order: Land then Water
        for ($j = 0; $j < $m; $j++) {
            $currentFinish = max($minFL, $waterStartTime[$j]) + $waterDuration[$j];
            if ($currentFinish < $minTotal) {
                $minTotal = $currentFinish;
            }
        }

        // Order: Water then Land
        for ($i = 0; $i < $n; $i++) {
            $currentFinish = max($minFW, $landStartTime[$i]) + $landDuration[$i];
            if ($currentFinish < $minTotal) {
                $minTotal = $currentFinish;
            }
        }

        return (int)$minTotal;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func earliestFinishTime(_ landStartTime: [Int], _ landDuration: [Int], _ waterStartTime: [Int], _ waterDuration: [Int]) -> Int {
        let n = landStartTime.count
        let m = waterStartTime.count

        var minFL = Int.max
        for i in 0..<n {
            let finish = landStartTime[i] + landDuration[i]
            if finish < minFL {
                minFL = finish
            }
        }

        var minFW = Int.max
        for j in 0..<m {
            let finish = waterStartTime[j] + waterDuration[j]
            if finish < minFW {
                minFW = finish
            }
        }

        var minTotal = Int.max

        // Order: Land then Water
        for j in 0..<m {
            let currentFinish = max(minFL, waterStartTime[j]) + waterDuration[j]
            if currentFinish < minTotal {
                minTotal = currentFinish
            }
        }

        // Order: Water then Land
        for i in 0..<n {
            let currentFinish = max(minFW, landStartTime[i]) + landDuration[i]
            if currentFinish < minTotal {
                minTotal = currentFinish
            }
        }

        return minTotal
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun earliestFinishTime(landStartTime: IntArray, landDuration: IntArray, waterStartTime: IntArray, waterDuration: IntArray): Int {
        val res1 = solve(landStartTime, landDuration, waterStartTime, waterDuration)
        val res2 = solve(waterStartTime, waterDuration, landStartTime, landDuration)
        return if (res1 < res2) res1 else res2
    }

    private fun solve(starts1: IntArray, durations1: IntArray, starts2: IntArray, durations2: IntArray): Int {
        val m = starts2.size
        val indices = Array(m) { it }
        indices.sortBy { starts2[it] }

        val prefMinDur = IntArray(m)
        prefMinDur[0] = durations2[indices[0]]
        for (j in 1 until m) {
            prefMinDur[j] = if (prefMinDur[j - 1] < durations2[indices[j]]) prefMinDur[j - 1] else durations2[indices[j]]
        }

        val sufMinFinish = IntArray(m)
        sufMinFinish[m - 1] = starts2[indices[m - 1]] + durations2[indices[m - 1]]
        for (j in m - 2 downTo 0) {
            val currentFinish = starts2[indices[j]] + durations2[indices[j]]
            sufMinFinish[j] = if (sufMinFinish[j + 1] < currentFinish) sufMinFinish[j + 1] else currentFinish
        }

        var minF2 = Int.MAX_VALUE
        for (i in starts1.indices) {
            val f1 = starts1[i] + durations1[i]

            var low = 0
            var high = m
            while (low < high) {
                val mid = (low + high) / 2
                if (starts2[indices[mid]] <= f1) {
                    low = mid + 1
                } else {
                    high = mid
                }
            }
            val idx = low

            var currentCandidate = Int.MAX_VALUE
            if (idx > 0) {
                val candidate = f1 + prefMinDur[idx - 1]
                if (candidate < currentCandidate) currentCandidate = candidate
            }
            if (idx < m) {
                if (sufMinFinish[idx] < currentCandidate) currentCandidate = sufMinFinish[idx]
            }
            if (currentCandidate < minF2) minF2 = currentCandidate
        }
        return minF2
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:math';

class Solution {
  int earliestFinishTime(List<int> landStartTime, List<int> landDuration, List<int> waterStartTime, List<int> waterDuration) {
    int res1 = solve(landStartTime, landDuration, waterStartTime, waterDuration);
    int res2 = solve(waterStartTime, waterDuration, landStartTime, landDuration);
    return min(res1, res2);
  }

  int solve(List<int> starts1, List<int> durations1, List<int> starts2, List<int> durations2) {
    int m = starts2.length;
    List<int> indices = List.generate(m, (i) => i);
    indices.sort((a, b) => starts2[a].compareTo(starts2[b]));

    List<int> prefMinDur = List.filled(m, 0);
    prefMinDur[0] = durations2[indices[0]];
    for (int j = 1; j < m; j++) {
      prefMinDur[j] = min(prefMinDur[j - 1], durations2[indices[j]]);
    }

    List<int> sufMinFinish = List.filled(m, 0);
    sufMinFinish[m - 1] = starts2[indices[m - 1]] + durations2[indices[m - 1]];
    for (int j = m - 2; j >= 0; j--) {
      sufMinFinish[j] = min(sufMinFinish[j + 1], starts2[indices[j]] + durations2[indices[j]]);
    }

    int minF2 = 2000000000;
    for (int i = 0; i < starts1.length; i++) {
      int f1 = starts1[i] + durations1[i];

      int low = 0;
      int high = m;
      while (low < high) {
        int mid = (low + high) ~/ 2;
        if (starts2[indices[mid]] <= f1) {
          low = mid + 1;
        } else {
          high = mid;
        }
      }
      int idx = low;

      int currentCandidate = 2000000000;
      if (idx > 0) {
        currentCandidate = min(currentCandidate, f1 + prefMinDur[idx - 1]);
      }
      if (idx < m) {
        currentCandidate = min(currentCandidate, sufMinFinish[idx]);
      }
      minF2 = min(minF2, currentCandidate);
    }
    return minF2;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "sort"

func solve(starts1 []int, durations1 []int, starts2 []int, durations2 []int) int {
	m := len(starts2)
	type ride struct {
		s, d int
	}
	rides2 := make([]ride, m)
	for i := 0; i < m; i++ {
		rides2[i] = ride{starts2[i], durations2[i]}
	}
	sort.Slice(rides2, func(i, j int) bool {
		return rides2[i].s < rides2[j].s
	})

	prefMinDur := make([]int, m)
	prefMinDur[0] = rides2[0].d
	for i := 1; i < m; i++ {
		prefMinDur[i] = prefMinDur[i-1]
		if rides2[i].d < prefMinDur[i] {
			prefMinDur[i] = rides2[i].d
		}
	}

	sufMinFinish := make([]int, m)
	sufMinFinish[m-1] = rides2[m-1].s + rides2[m-1].d
	for i := m - 2; i >= 0; i-- {
		sufMinFinish[i] = sufMinFinish[i+1]
		finish := rides2[i].s + rides2[i].d
		if finish < sufMinFinish[i] {
			sufMinFinish[i] = finish
		}
	}

	minTotal := 2000000000
	for i := 0; i < len(starts1); i++ {
		f1 := starts1[i] + durations1[i]
		idx := sort.Search(m, func(j int) bool {
			return rides2[j].s > f1
		})

		res := 2000000000
		if idx > 0 {
			if f1+prefMinDur[idx-1] < res {
				res = f1 + prefMinDur[idx-1]
			}
		}
		if idx < m {
			if sufMinFinish[idx] < res {
				res = sufMinFinish[idx]
			}
		}
		if res < minTotal {
			minTotal = res
		}
	}
	return minTotal
}

func earliestFinishTime(landStartTime []int, landDuration []int, waterStartTime []int, waterDuration []int) int {
	ans1 := solve(landStartTime, landDuration, waterStartTime, waterDuration)
	ans2 := solve(waterStartTime, waterDuration, landStartTime, landDuration)
	if ans1 < ans2 {
		return ans1
	}
	return ans2
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} land_start_time
# @param {Integer[]} land_duration
# @param {Integer[]} water_start_time
# @param {Integer[]} water_duration
# @return {Integer}
def earliest_finish_time(land_start_time, land_duration, water_start_time, water_duration)
  ans1 = solve(land_start_time, land_duration, water_start_time, water_duration)
  ans2 = solve(water_start_time, water_duration, land_start_time, land_duration)
  [ans1, ans2].min
end

def solve(starts1, durations1, starts2, durations2)
  m = starts2.length
  rides2 = starts2.zip(durations2).sort_by! { |r| r[0] }

  pref_min_dur = Array.new(m)
  pref_min_dur[0] = rides2[0][1]
  (1...m).each do |j|
    pref_min_dur[j] = [pref_min_dur[j - 1], rides2[j][1]].min
  end

  suf_min_finish = Array.new(m)
  suf_min_finish[m - 1] = rides2[m - 1][0] + rides2[m - 1][1]
  (m - 2).downto(0) do |j|
    suf_min_finish[j] = [suf_min_finish[j + 1], rides2[j][0] + rides2[j][1]].min
  end

  min_f2 = 2000000000
  starts1.each_with_index do |s1, i|
    f1 = s1 + durations1[i]
    idx = rides2.bsearch_index { |r| r[0] > f1 } || m

    res = 2000000000
    if idx > 0
      res = [res, f1 + pref_min_dur[idx - 1]].min
    end
    if idx < m
      res = [res, suf_min_finish[idx]].min
    end
    min_f2 = [min_f2, res].min
  end
  min_f2
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def earliestFinishTime(landStartTime: Array[Int], landDuration: Array[Int], waterStartTime: Array[Int], waterDuration: Array[Int]): Int = {
    val ans1 = solve(landStartTime, landDuration, waterStartTime, waterDuration)
    val ans2 = solve(waterStartTime, waterDuration, landStartTime, landDuration)
    math.min(ans1, ans2)
  }

  def solve(starts1: Array[Int], durations1: Array[Int], starts2: Array[Int], durations2: Array[Int]): Int = {
    val m = starts2.length
    val rides2 = starts2.zip(durations2).sortBy(_._1)

    val prefMinDur = new Array[Int](m)
    prefMinDur(0) = rides2(0)._2
    for (j <- 1 until m) {
      prefMinDur(j) = math.min(prefMinDur(j - 1), rides2(j)._2)
    }

    val sufMinFinish = new Array[Int](m)
    sufMinFinish(m - 1) = rides2(m - 1)._1 + rides2(m - 1)._2
    for (j <- m - 2 to 0 by -1) {
      sufMinFinish(j) = math.min(sufMinFinish(j + 1), rides2(j)._1 + rides2(j)._2)
    }

    var minF2 = Int.MaxValue
    for (i <- starts1.indices) {
      val f1 = starts1(i) + durations1(i)

      var low = 0
      var high = m
      while (low < high) {
        val mid = (low + high) / 2
        if (rides2(mid)._1 <= f1) {
          low = mid + 1
        } else {
          high = mid
        }
      }
      val idx = low

      var res = Int.MaxValue
      if (idx > 0) {
        res = math.min(res, f1 + prefMinDur(idx - 1))
      }
      if (idx < m) {
        res = math.min(res, sufMinFinish(idx))
      }
      minF2 = math.min(minF2, res)
    }
    minF2
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn earliest_finish_time(land_start_time: Vec<i32>, land_duration: Vec<i32>, water_start_time: Vec<i32>, water_duration: Vec<i32>) -> i32 {
        fn solve(a: &[(i32, i32)], b: &[(i32, i32)]) -> i32 {
            let mut a_sorted = a.to_vec();
            a_sorted.sort_unstable_by_key(|&(s, d)| s + d);

            let mut b_sorted = b.to_vec();
            b_sorted.sort_unstable_by_key(|&(s, _d)| s);

            let m = b_sorted.len();
            let mut suffix_min_finish = vec![2000000000; m + 1];
            for i in (0..m).rev() {
                suffix_min_finish[i] = suffix_min_finish[i + 1].min(b_sorted[i].0 + b_sorted[i].1);
            }

            let mut best = 2000000000;
            let mut k = 0;
            let mut prefix_min_dur = 2000000000;
            for &(sa, da) in &a_sorted {
                let fa = sa + da;
                while k < m && b_sorted[k].0 <= fa {
                    prefix_min_dur = prefix_min_dur.min(b_sorted[k].1);
                    k += 1;
                }
                if prefix_min_dur != 2000000000 {
                    best = best.min(fa + prefix_min_dur);
                }
                best = best.min(suffix_min_finish[k]);
            }
            best
        }

        let land: Vec<(i32, i32)> = land_start_time.into_iter().zip(land_duration.into_iter()).collect();
        let water: Vec<(i32, i32)> = water_start_time.into_iter().zip(water_duration.into_iter()).collect();

        solve(&land, &water).min(solve(&water, &land))
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (earliest-finish-time landStartTime landDuration waterStartTime waterDuration)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (define (solve a b)
    (let* ([a-sorted (sort a < #:key (lambda (x) (+ (car x) (cdr x))))]
           [b-sorted (list->vector (sort b < #:key (lambda (x) (car x))))]
           [m (vector-length b-sorted)]
           [suffix-min-finish (make-vector (+ m 1) 2000000000)])
      (for ([i (in-range (- m 1) -1 -1)])
        (let ([b-val (vector-ref b-sorted i)])
          (vector-set! suffix-min-finish i (min (vector-ref suffix-min-finish (+ i 1)) (+ (car b-val) (cdr b-val))))))
      (let loop ([a-list a-sorted] [k 0] [prefix-min-dur 2000000000] [best 2000000000])
        (if (null? a-list)
            best
            (let* ([a-ride (car a-list)]
                   [fa (+ (car a-ride) (cdr a-ride))])
              (let-values ([(new-k new-prefix-min-dur)
                            (let inner-loop ([curr-k k] [curr-prefix-min-dur prefix-min-dur])
                              (if (and (< curr-k m) (<= (car (vector-ref b-sorted curr-k)) fa))
                                  (inner-loop (+ curr-k 1) (min curr-prefix-min-dur (cdr (vector-ref b-sorted curr-k))))
                                  (values curr-k curr-prefix-min-dur)))])
                (let* ([res1 (if (= new-prefix-min-dur 2000000000) 2000000000 (+ fa new-prefix-min-dur))]
                       [res2 (vector-ref suffix-min-finish new-k)]
                       [new-best (min best res1 res2)])
                  (loop (cdr a-list) new-k new-prefix-min-dur new-best))))))))

  (let ([land (map cons landStartTime landDuration)]
        [water (map cons waterStartTime waterDuration)])
    (min (solve land water) (solve water land))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec earliest_finish_time(LandStartTime :: [integer()], LandDuration :: [integer()], WaterStartTime :: [integer()], WaterDuration :: [integer()]) -> integer().
earliest_finish_time(LandStartTime, LandDuration, WaterStartTime, WaterDuration) ->
  Land = lists:zip(LandStartTime, LandDuration),
  Water = lists:zip(WaterStartTime, WaterDuration),
  min(solve(Land, Water), solve(Water, Land)).

solve(A, B) ->
  ASorted = lists:sort(fun({S1, D1}, {S2, D2}) -> (S1 + D1) =< (S2 + D2) end, A),
  BSorted = lists:sort(fun({S1, _D1}, {S2, _D2}) -> S1 =< S2 end, B),
  SuffixMinFinish = build_suffix_min_finish(BSorted),
  solve_tp(ASorted, BSorted, SuffixMinFinish, 2000000000, 2000000000).

build_suffix_min_finish(BSorted) ->
  lists:foldr(fun({S, D}, Acc) ->
    [MinSoFar | _] = Acc,
    [min(MinSoFar, S + D) | Acc]
  end, [2000000000], BSorted).

solve_tp([], _BSorted, _SuffixMinFinish, _PrefixMinDur, Best) ->
  Best;
solve_tp([{SA, DA} | ATail], BSorted, SuffixMinFinish, PrefixMinDur, Best) ->
  FA = SA + DA,
  {NewBSorted, NewSuffixMinFinish, NewPrefixMinDur} = advance_b(BSorted, SuffixMinFinish, PrefixMinDur, FA),
  Res1 = if NewPrefixMinDur == 2000000000 -> 2000000000; true -> FA + NewPrefixMinDur end,
  Res2 = hd(NewSuffixMinFinish),
  NewBest = min(Best, min(Res1, Res2)),
  solve_tp(ATail, NewBSorted, NewSuffixMinFinish, NewPrefixMinDur, NewBest).

advance_b([{SB, DB} | BTail], [_ | STail], PrefixMinDur, FA) when SB =< FA ->
  advance_b(BTail, STail, min(PrefixMinDur, DB), FA);
advance_b(BSorted, SuffixMinFinish, PrefixMinDur, _FA) ->
  {BSorted, SuffixMinFinish, PrefixMinDur}.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec earliest_finish_time(land_start_time :: [integer], land_duration :: [integer], water_start_time :: [integer], water_duration :: [integer]) :: integer
  def earliest_finish_time(land_start_time, land_duration, water_start_time, water_duration) do
    land = Enum.zip(land_start_time, land_duration)
    water = Enum.zip(water_start_time, water_duration)
    min(solve(land, water), solve(water, land))
  end

  defp solve(a, b) do
    a_sorted = Enum.sort_by(a, fn {s, d} -> s + d end)
    b_sorted = Enum.sort_by(b, fn {s, _d} -> s end)
    suffix_min_finish = build_suffix_min_finish(b_sorted)
    solve_tp(a_sorted, b_sorted, suffix_min_finish, 2000000000, 2000000000)
  end

  defp build_suffix_min_finish(b_sorted) do
    b_sorted
    |> Enum.reverse()
    |> Enum.reduce([2000000000], fn {s, d}, [min_so_far | _] = acc ->
      [min(min_so_far, s + d) | acc]
    end)
  end

  defp solve_tp([], _b_sorted, _suffix_min_finish, _prefix_min_dur, best) do
    best
  end

  defp solve_tp([{sa, da} | a_tail], b_sorted, suffix_min_finish, prefix_min_dur, best) do
    fa = sa + da
    {new_b_sorted, new_suffix_min_finish, new_prefix_min_dur} = advance_b(b_sorted, suffix_min_finish, prefix_min_dur, fa)
    res1 = if new_prefix_min_dur == 2000000000, do: 2000000000, else: fa + new_prefix_min_dur
    res2 = hd(new_suffix_min_finish)
    new_best = min(best, min(res1, res2))
    solve_tp(a_tail, new_b_sorted, new_suffix_min_finish, new_prefix_min_dur, new_best)
  end

  defp advance_b([{sb, db} | b_tail], [_ | s_tail], prefix_min_dur, fa) when sb <= fa do
    advance_b(b_tail, s_tail, min(prefix_min_dur, db), fa)
  end

  defp advance_b(b_sorted, suffix_min_finish, prefix_min_dur, _fa) do
    {b_sorted, suffix_min_finish, prefix_min_dur}
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O((N + M) log (N + M)) where N and M are the number of land and water rides respectively. This accounts for sorting both lists of rides and performing binary search for each ride during the evaluation phase.
- **Space Complexity:** O(N + M) to store the sorted ride information and the prefix/suffix precomputation arrays.
