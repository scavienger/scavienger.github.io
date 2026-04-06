---
layout: post
title: "Maximum Walls Destroyed by Robots"
date: 2026-04-03 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Binary Search", "Dynamic Programming", "Sorting"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/maximum-walls-destroyed-by-robots/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int countWallsInRange(const std::vector<int>&\
        \ walls, int a, int b) {\n        if (a > b) return 0;\n        auto it1 = std::lower_bound(walls.begin(),\
        \ walls.end(), a);\n        auto it2 = std::upper_bound(walls.begin(), walls.end(),\
        \ b);\n        return std::distance(it1, it2);\n    }\n\n    int maxWalls(std::vector<int>&\
        \ robots, std::vector<int>& distance, std::vector<int>& walls) {\n        int\
        \ n = robots.size();\n        std::vector<std::pair<int, int>> rd(n);\n    \
        \    for (int i = 0; i < n; ++i) {\n            rd[i] = {robots[i], distance[i]};\n\
        \        }\n        std::sort(rd.begin(), rd.end());\n        for (int i = 0;\
        \ i < n; ++i) {\n            robots[i] = rd[i].first;\n            distance[i]\
        \ = rd[i].second;\n        }\n        std::sort(walls.begin(), walls.end());\n\
        \n        std::vector<long long> dp0(n, 0);\n        std::vector<long long>\
        \ dp1(n, 0);\n\n        dp0[0] = countWallsInRange(walls, robots[0] - distance[0],\
        \ robots[0] - 1);\n        int r0_end = robots[0] + distance[0];\n        if\
        \ (n > 1) r0_end = std::min(r0_end, robots[1] - 1);\n        dp1[0] = countWallsInRange(walls,\
        \ robots[0] + 1, r0_end);\n\n        for (int i = 1; i < n; ++i) {\n       \
        \     int li_start = std::max(robots[i] - distance[i], robots[i - 1] + 1);\n\
        \            int li_end = robots[i] - 1;\n            int c_li = countWallsInRange(walls,\
        \ li_start, li_end);\n\n            int ri_prev_end = std::min(robots[i - 1]\
        \ + distance[i - 1], robots[i] - 1);\n            int c_li_rem = countWallsInRange(walls,\
        \ std::max(li_start, ri_prev_end + 1), li_end);\n\n            dp0[i] = std::max(dp0[i\
        \ - 1] + c_li, dp1[i - 1] + c_li_rem);\n\n            int ri_end = robots[i]\
        \ + distance[i];\n            if (i < n - 1) ri_end = std::min(ri_end, robots[i\
        \ + 1] - 1);\n            dp1[i] = std::max(dp0[i - 1], dp1[i - 1]) + countWallsInRange(walls,\
        \ robots[i] + 1, ri_end);\n        }\n\n        int walls_at_robots = 0;\n \
        \       for (int r : robots) {\n            if (std::binary_search(walls.begin(),\
        \ walls.end(), r)) {\n                walls_at_robots++;\n            }\n  \
        \      }\n\n        return (int)(std::max(dp0[n - 1], dp1[n - 1]) + walls_at_robots);\n\
        \    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public int maxWalls(int[]\
        \ robots, int[] distance, int[] walls) {\n        int n = robots.length;\n \
        \       long[] combined = new long[n];\n        for (int i = 0; i < n; i++)\
        \ {\n            combined[i] = ((long) robots[i] << 32) | (distance[i] & 0xFFFFFFFFL);\n\
        \        }\n        Arrays.sort(combined);\n        for (int i = 0; i < n; i++)\
        \ {\n            robots[i] = (int) (combined[i] >> 32);\n            distance[i]\
        \ = (int) (combined[i] & 0xFFFFFFFFL);\n        }\n        Arrays.sort(walls);\n\
        \n        long[] dp0 = new long[n];\n        long[] dp1 = new long[n];\n\n \
        \       dp0[0] = countWallsInRange(walls, robots[0] - distance[0], robots[0]\
        \ - 1);\n        int r0End = robots[0] + distance[0];\n        if (n > 1) r0End\
        \ = Math.min(r0End, robots[1] - 1);\n        dp1[0] = countWallsInRange(walls,\
        \ robots[0] + 1, r0End);\n\n        for (int i = 1; i < n; i++) {\n        \
        \    int liStart = Math.max(robots[i] - distance[i], robots[i - 1] + 1);\n \
        \           int liEnd = robots[i] - 1;\n            int cLi = countWallsInRange(walls,\
        \ liStart, liEnd);\n\n            int riPrevEnd = Math.min(robots[i - 1] + distance[i\
        \ - 1], robots[i] - 1);\n            int cLiRem = countWallsInRange(walls, Math.max(liStart,\
        \ riPrevEnd + 1), liEnd);\n\n            dp0[i] = Math.max(dp0[i - 1] + cLi,\
        \ dp1[i - 1] + cLiRem);\n\n            int riEnd = robots[i] + distance[i];\n\
        \            if (i < n - 1) riEnd = Math.min(riEnd, robots[i + 1] - 1);\n  \
        \          dp1[i] = Math.max(dp0[i - 1], dp1[i - 1]) + countWallsInRange(walls,\
        \ robots[i] + 1, riEnd);\n        }\n\n        int wallsAtRobots = 0;\n    \
        \    for (int r : robots) {\n            if (Arrays.binarySearch(walls, r) >=\
        \ 0) {\n                wallsAtRobots++;\n            }\n        }\n\n     \
        \   return (int) (Math.max(dp0[n - 1], dp1[n - 1]) + wallsAtRobots);\n    }\n\
        \n    private int countWallsInRange(int[] walls, int a, int b) {\n        if\
        \ (a > b) return 0;\n        int idx1 = Arrays.binarySearch(walls, a);\n   \
        \     int lower = (idx1 < 0) ? -(idx1 + 1) : idx1;\n        int idx2 = Arrays.binarySearch(walls,\
        \ b);\n        int upper = (idx2 < 0) ? -(idx2 + 1) : idx2 + 1;\n        return\
        \ upper - lower;\n    }\n}"
      python: "import bisect\n\nclass Solution(object):\n    def maxWalls(self, robots,\
        \ distance, walls):\n        \"\"\"\n        :type robots: List[int]\n     \
        \   :type distance: List[int]\n        :type walls: List[int]\n        :rtype:\
        \ int\n        \"\"\"\n        n = len(robots)\n        rd = sorted(zip(robots,\
        \ distance))\n        robots = [x[0] for x in rd]\n        distance = [x[1]\
        \ for x in rd]\n        walls.sort()\n\n        def count(a, b):\n         \
        \   if a > b:\n                return 0\n            return bisect.bisect_right(walls,\
        \ b) - bisect.bisect_left(walls, a)\n\n        dp0 = [0] * n\n        dp1 =\
        \ [0] * n\n\n        dp0[0] = count(robots[0] - distance[0], robots[0] - 1)\n\
        \        r0_end = robots[0] + distance[0]\n        if n > 1:\n            r0_end\
        \ = min(r0_end, robots[1] - 1)\n        dp1[0] = count(robots[0] + 1, r0_end)\n\
        \n        for i in range(1, n):\n            li_start = max(robots[i] - distance[i],\
        \ robots[i-1] + 1)\n            li_end = robots[i] - 1\n            c_li = count(li_start,\
        \ li_end)\n\n            ri_prev_end = min(robots[i-1] + distance[i-1], robots[i]\
        \ - 1)\n            c_li_rem = count(max(li_start, ri_prev_end + 1), li_end)\n\
        \n            dp0[i] = max(dp0[i-1] + c_li, dp1[i-1] + c_li_rem)\n\n       \
        \     ri_end = robots[i] + distance[i]\n            if i < n - 1:\n        \
        \        ri_end = min(ri_end, robots[i+1] - 1)\n            dp1[i] = max(dp0[i-1],\
        \ dp1[i-1]) + count(robots[i] + 1, ri_end)\n\n        walls_at_robots = 0\n\
        \        for r in robots:\n            idx = bisect.bisect_left(walls, r)\n\
        \            if idx < len(walls) and walls[idx] == r:\n                walls_at_robots\
        \ += 1\n\n        return int(max(dp0[n-1], dp1[n-1]) + walls_at_robots)"
      python3: "import bisect\n\nclass Solution:\n    def maxWalls(self, robots: list[int],\
        \ distance: list[int], walls: list[int]) -> int:\n        n = len(robots)\n\
        \        rd = sorted(zip(robots, distance))\n        robots = [x[0] for x in\
        \ rd]\n        distance = [x[1] for x in rd]\n        walls.sort()\n\n     \
        \   def count(a, b):\n            if a > b:\n                return 0\n    \
        \        return bisect.bisect_right(walls, b) - bisect.bisect_left(walls, a)\n\
        \n        dp0 = [0] * n\n        dp1 = [0] * n\n\n        dp0[0] = count(robots[0]\
        \ - distance[0], robots[0] - 1)\n        r0_end = robots[0] + distance[0]\n\
        \        if n > 1:\n            r0_end = min(r0_end, robots[1] - 1)\n      \
        \  dp1[0] = count(robots[0] + 1, r0_end)\n\n        for i in range(1, n):\n\
        \            li_start = max(robots[i] - distance[i], robots[i-1] + 1)\n    \
        \        li_end = robots[i] - 1\n            c_li = count(li_start, li_end)\n\
        \n            ri_prev_end = min(robots[i-1] + distance[i-1], robots[i] - 1)\n\
        \            c_li_rem = count(max(li_start, ri_prev_end + 1), li_end)\n\n  \
        \          dp0[i] = max(dp0[i-1] + c_li, dp1[i-1] + c_li_rem)\n\n          \
        \  ri_end = robots[i] + distance[i]\n            if i < n - 1:\n           \
        \     ri_end = min(ri_end, robots[i+1] - 1)\n            dp1[i] = max(dp0[i-1],\
        \ dp1[i-1]) + count(robots[i] + 1, ri_end)\n\n        walls_at_robots = 0\n\
        \        for r in robots:\n            idx = bisect.bisect_left(walls, r)\n\
        \            if idx < len(walls) and walls[idx] == r:\n                walls_at_robots\
        \ += 1\n\n        return int(max(dp0[n-1], dp1[n-1]) + walls_at_robots)"
      c: "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\ntypedef struct\
        \ {\n    int pos;\n    int dist;\n} Robot;\n\nint compareRobots(const void*\
        \ a, const void* b) {\n    Robot* r1 = (Robot*)a;\n    Robot* r2 = (Robot*)b;\n\
        \    if (r1->pos < r2->pos) return -1;\n    if (r1->pos > r2->pos) return 1;\n\
        \    return 0;\n}\n\nint compareWalls(const void* a, const void* b) {\n    int\
        \ w1 = *(int*)a;\n    int w2 = *(int*)b;\n    if (w1 < w2) return -1;\n    if\
        \ (w1 > w2) return 1;\n    return 0;\n}\n\nint lower_bound(int* arr, int size,\
        \ long long val) {\n    int low = 0, high = size;\n    while (low < high) {\n\
        \        int mid = low + (high - low) / 2;\n        if (arr[mid] >= val) high\
        \ = mid;\n        else low = mid + 1;\n    }\n    return low;\n}\n\nint upper_bound(int*\
        \ arr, int size, long long val) {\n    int low = 0, high = size;\n    while\
        \ (low < high) {\n        int mid = low + (high - low) / 2;\n        if (arr[mid]\
        \ > val) high = mid;\n        else low = mid + 1;\n    }\n    return low;\n\
        }\n\nint countInRange(int* walls, int wallsSize, long long a, long long b) {\n\
        \    if (a > b) return 0;\n    return upper_bound(walls, wallsSize, b) - lower_bound(walls,\
        \ wallsSize, a);\n}\n\nint maxWalls(int* robots, int robotsSize, int* distance,\
        \ int distanceSize, int* walls, int wallsSize) {\n    Robot* sorted_robots =\
        \ (Robot*)malloc(sizeof(Robot) * robotsSize);\n    for (int i = 0; i < robotsSize;\
        \ i++) {\n        sorted_robots[i].pos = robots[i];\n        sorted_robots[i].dist\
        \ = distance[i];\n    }\n    qsort(sorted_robots, robotsSize, sizeof(Robot),\
        \ compareRobots);\n    qsort(walls, wallsSize, sizeof(int), compareWalls);\n\
        \n    int (*dp)[2] = malloc(sizeof(int) * robotsSize * 2);\n\n    long long\
        \ b0_r = (robotsSize == 1) ? ((long long)sorted_robots[0].pos + sorted_robots[0].dist)\
        \ : ((long long)sorted_robots[0].pos + sorted_robots[0].dist);\n    if (robotsSize\
        \ > 1 && b0_r > sorted_robots[1].pos) b0_r = sorted_robots[1].pos;\n\n    dp[0][0]\
        \ = countInRange(walls, wallsSize, (long long)sorted_robots[0].pos - sorted_robots[0].dist,\
        \ sorted_robots[0].pos);\n    dp[0][1] = countInRange(walls, wallsSize, sorted_robots[0].pos,\
        \ b0_r);\n\n    for (int i = 1; i < robotsSize; i++) {\n        long long b_prev_r\
        \ = (long long)sorted_robots[i-1].pos + sorted_robots[i-1].dist;\n        if\
        \ (b_prev_r > sorted_robots[i].pos) b_prev_r = sorted_robots[i].pos;\n\n   \
        \     long long b_i_l = (long long)sorted_robots[i].pos - sorted_robots[i].dist;\n\
        \        if (b_i_l < sorted_robots[i-1].pos) b_i_l = sorted_robots[i-1].pos;\n\
        \n        long long b_i_r;\n        if (i == robotsSize - 1) {\n           \
        \ b_i_r = (long long)sorted_robots[i].pos + sorted_robots[i].dist;\n       \
        \ } else {\n            b_i_r = (long long)sorted_robots[i].pos + sorted_robots[i].dist;\n\
        \            if (b_i_r > sorted_robots[i+1].pos) b_i_r = sorted_robots[i+1].pos;\n\
        \        }\n\n        long long prev_r_pos = sorted_robots[i-1].pos;\n     \
        \   long long curr_r_pos = sorted_robots[i].pos;\n\n        int dp0_from_dp0\
        \ = dp[i-1][0] + countInRange(walls, wallsSize, b_i_l > prev_r_pos + 1 ? b_i_l\
        \ : prev_r_pos + 1, curr_r_pos);\n        int dp0_from_dp1 = dp[i-1][1] + countInRange(walls,\
        \ wallsSize, b_i_l > b_prev_r + 1 ? b_i_l : b_prev_r + 1, curr_r_pos);\n   \
        \     dp[i][0] = dp0_from_dp0 > dp0_from_dp1 ? dp0_from_dp0 : dp0_from_dp1;\n\
        \n        int dp1_from_dp0 = dp[i-1][0] + countInRange(walls, wallsSize, curr_r_pos,\
        \ b_i_r);\n        int dp1_from_dp1 = dp[i-1][1] + countInRange(walls, wallsSize,\
        \ curr_r_pos > b_prev_r + 1 ? curr_r_pos : b_prev_r + 1, b_i_r);\n        dp[i][1]\
        \ = dp1_from_dp0 > dp1_from_dp1 ? dp1_from_dp0 : dp1_from_dp1;\n    }\n\n  \
        \  int result = dp[robotsSize - 1][0] > dp[robotsSize - 1][1] ? dp[robotsSize\
        \ - 1][0] : dp[robotsSize - 1][1];\n\n    free(sorted_robots);\n    free(dp);\n\
        \    return result;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int MaxWalls(int[] robots, int[] distance, int[] walls) {\n\
        \        int n = robots.Length;\n        var sortedRobots = new (long pos, long\
        \ dist)[n];\n        for (int i = 0; i < n; i++) {\n            sortedRobots[i]\
        \ = (robots[i], distance[i]);\n        }\n        Array.Sort(sortedRobots, (a,\
        \ b) => a.pos.CompareTo(b.pos));\n        Array.Sort(walls);\n\n        int[,]\
        \ dp = new int[n, 2];\n\n        long b0_r = (n == 1) ? (sortedRobots[0].pos\
        \ + sortedRobots[0].dist) : Math.Min(sortedRobots[0].pos + sortedRobots[0].dist,\
        \ sortedRobots[1].pos);\n        dp[0, 0] = CountInRange(walls, sortedRobots[0].pos\
        \ - sortedRobots[0].dist, sortedRobots[0].pos);\n        dp[0, 1] = CountInRange(walls,\
        \ sortedRobots[0].pos, b0_r);\n\n        for (int i = 1; i < n; i++) {\n   \
        \         long b_prev_r = Math.Min(sortedRobots[i - 1].pos + sortedRobots[i\
        \ - 1].dist, sortedRobots[i].pos);\n            long b_i_l = Math.Max(sortedRobots[i].pos\
        \ - sortedRobots[i].dist, sortedRobots[i - 1].pos);\n            long b_i_r\
        \ = (i == n - 1) ? (sortedRobots[i].pos + sortedRobots[i].dist) : Math.Min(sortedRobots[i].pos\
        \ + sortedRobots[i].dist, sortedRobots[i + 1].pos);\n\n            long prev_r_pos\
        \ = sortedRobots[i - 1].pos;\n            long curr_r_pos = sortedRobots[i].pos;\n\
        \n            dp[i, 0] = Math.Max(\n                dp[i - 1, 0] + CountInRange(walls,\
        \ Math.Max(b_i_l, prev_r_pos + 1), curr_r_pos),\n                dp[i - 1, 1]\
        \ + CountInRange(walls, Math.Max(b_i_l, b_prev_r + 1), curr_r_pos)\n       \
        \     );\n\n            dp[i, 1] = Math.Max(\n                dp[i - 1, 0] +\
        \ CountInRange(walls, curr_r_pos, b_i_r),\n                dp[i - 1, 1] + CountInRange(walls,\
        \ Math.Max(curr_r_pos, b_prev_r + 1), b_i_r)\n            );\n        }\n\n\
        \        return Math.Max(dp[n - 1, 0], dp[n - 1, 1]);\n    }\n\n    private\
        \ int CountInRange(int[] walls, long a, long b) {\n        if (a > b) return\
        \ 0;\n        int start = Array.BinarySearch(walls, (int)a);\n        if (start\
        \ < 0) start = ~start;\n        int end = Array.BinarySearch(walls, (int)b);\n\
        \        if (end < 0) end = ~end - 1;\n        if (start <= end) return end\
        \ - start + 1;\n        return 0;\n    }\n}"
      javascript: "/**\n * @param {number[]} robots\n * @param {number[]} distance\n\
        \ * @param {number[]} walls\n * @return {number}\n */\nvar maxWalls = function(robots,\
        \ distance, walls) {\n    const n = robots.length;\n    const indices = new\
        \ Int32Array(n);\n    for (let i = 0; i < n; i++) indices[i] = i;\n    indices.sort((a,\
        \ b) => robots[a] - robots[b]);\n\n    const sortedWalls = new Int32Array(walls);\n\
        \    sortedWalls.sort();\n\n    function lowerBound(arr, val) {\n        let\
        \ low = 0, high = arr.length;\n        while (low < high) {\n            let\
        \ mid = (low + high) >>> 1;\n            if (arr[mid] >= val) high = mid;\n\
        \            else low = mid + 1;\n        }\n        return low;\n    }\n\n\
        \    function upperBound(arr, val) {\n        let low = 0, high = arr.length;\n\
        \        while (low < high) {\n            let mid = (low + high) >>> 1;\n \
        \           if (arr[mid] > val) high = mid;\n            else low = mid + 1;\n\
        \        }\n        return low;\n    }\n\n    function countInRange(a, b) {\n\
        \        if (a > b) return 0;\n        return upperBound(sortedWalls, b) - lowerBound(sortedWalls,\
        \ a);\n    }\n\n    const dp0 = new Int32Array(n);\n    const dp1 = new Int32Array(n);\n\
        \n    const r0_pos = robots[indices[0]];\n    const r0_dist = distance[indices[0]];\n\
        \    const b0_r = (n === 1) ? (r0_pos + r0_dist) : Math.min(r0_pos + r0_dist,\
        \ robots[indices[1]]);\n\n    dp0[0] = countInRange(r0_pos - r0_dist, r0_pos);\n\
        \    dp1[0] = countInRange(r0_pos, b0_r);\n\n    for (let i = 1; i < n; i++)\
        \ {\n        const idx = indices[i];\n        const prevIdx = indices[i - 1];\n\
        \        const r_pos = robots[idx];\n        const r_dist = distance[idx];\n\
        \        const prev_pos = robots[prevIdx];\n        const prev_dist = distance[prevIdx];\n\
        \n        const b_prev_r = Math.min(prev_pos + prev_dist, r_pos);\n        const\
        \ b_i_l = Math.max(r_pos - r_dist, prev_pos);\n        const b_i_r = (i ===\
        \ n - 1) ? (r_pos + r_dist) : Math.min(r_pos + r_dist, robots[indices[i + 1]]);\n\
        \n        dp0[i] = Math.max(\n            dp0[i - 1] + countInRange(Math.max(b_i_l,\
        \ prev_pos + 1), r_pos),\n            dp1[i - 1] + countInRange(Math.max(b_i_l,\
        \ b_prev_r + 1), r_pos)\n        );\n\n        dp1[i] = Math.max(\n        \
        \    dp0[i - 1] + countInRange(r_pos, b_i_r),\n            dp1[i - 1] + countInRange(Math.max(r_pos,\
        \ b_prev_r + 1), b_i_r)\n        );\n    }\n\n    return Math.max(dp0[n - 1],\
        \ dp1[n - 1]);\n};"
      typescript: "function maxWalls(robots: number[], distance: number[], walls: number[]):\
        \ number {\n    const n = robots.length;\n    const combined = robots.map((p,\
        \ i) => ({ p, d: distance[i] }));\n    combined.sort((a, b) => a.p - b.p);\n\
        \    const P = combined.map(c => c.p);\n    const D = combined.map(c => c.d);\n\
        \    walls.sort((a, b) => a - b);\n\n    const lowerBound = (target: number)\
        \ => {\n        let l = 0, r = walls.length;\n        while (l < r) {\n    \
        \        let m = (l + r) >> 1;\n            if (walls[m] < target) l = m + 1;\n\
        \            else r = m;\n        }\n        return l;\n    };\n\n    const\
        \ upperBound = (target: number) => {\n        let l = 0, r = walls.length;\n\
        \        while (l < r) {\n            let m = (l + r) >> 1;\n            if\
        \ (walls[m] <= target) l = m + 1;\n            else r = m;\n        }\n    \
        \    return l;\n    };\n\n    const countWalls = (a: number, b: number) => {\n\
        \        if (a > b) return 0;\n        return upperBound(b) - lowerBound(a);\n\
        \    };\n\n    const hasWall = (pos: number) => {\n        const idx = lowerBound(pos);\n\
        \        return (idx < walls.length && walls[idx] === pos) ? 1 : 0;\n    };\n\
        \n    const lBoundaries = new Int32Array(n);\n    const rBoundaries = new Int32Array(n);\n\
        \    for (let i = 0; i < n; i++) {\n        lBoundaries[i] = Math.max(P[i] -\
        \ D[i], i > 0 ? P[i - 1] : -2000000000);\n        rBoundaries[i] = Math.min(P[i]\
        \ + D[i], i < n - 1 ? P[i + 1] : 2000000000);\n    }\n\n    const dp = new Int32Array(n\
        \ * 2);\n    dp[0] = countWalls(lBoundaries[0], P[0]);\n    dp[1] = countWalls(P[0],\
        \ rBoundaries[0]);\n\n    for (let i = 1; i < n; i++) {\n        const val1\
        \ = dp[(i - 1) * 2] + countWalls(lBoundaries[i], P[i]) - (lBoundaries[i] ===\
        \ P[i - 1] ? hasWall(P[i - 1]) : 0);\n        const val2 = dp[(i - 1) * 2 +\
        \ 1] + countWalls(lBoundaries[i], P[i]) - countWalls(lBoundaries[i], rBoundaries[i\
        \ - 1]);\n        dp[i * 2] = Math.max(val1, val2);\n\n        const val3 =\
        \ dp[(i - 1) * 2] + countWalls(P[i], rBoundaries[i]);\n        const val4 =\
        \ dp[(i - 1) * 2 + 1] + countWalls(P[i], rBoundaries[i]) - (rBoundaries[i -\
        \ 1] === P[i] ? hasWall(P[i]) : 0);\n        dp[i * 2 + 1] = Math.max(val3,\
        \ val4);\n    }\n\n    return Math.max(dp[(n - 1) * 2], dp[(n - 1) * 2 + 1]);\n\
        }"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $robots\n     * @param\
        \ Integer[] $distance\n     * @param Integer[] $walls\n     * @return Integer\n\
        \     */\n    function maxWalls($robots, $distance, $walls) {\n        $n =\
        \ count($robots);\n        array_multisort($robots, SORT_ASC, $distance);\n\
        \        sort($walls);\n\n        $lBoundaries = array_fill(0, $n, 0);\n   \
        \     $rBoundaries = array_fill(0, $n, 0);\n        for ($i = 0; $i < $n; $i++)\
        \ {\n            $lBoundaries[$i] = max($robots[$i] - $distance[$i], $i > 0\
        \ ? $robots[$i - 1] : -2000000000);\n            $rBoundaries[$i] = min($robots[$i]\
        \ + $distance[$i], $i < $n - 1 ? $robots[$i + 1] : 2000000000);\n        }\n\
        \n        $lowerBound = function($target) use (&$walls) {\n            $l =\
        \ 0; $r = count($walls);\n            while ($l < $r) {\n                $m\
        \ = (int)(($l + $r) / 2);\n                if ($walls[$m] < $target) $l = $m\
        \ + 1;\n                else $r = $m;\n            }\n            return $l;\n\
        \        };\n\n        $upperBound = function($target) use (&$walls) {\n   \
        \         $l = 0; $r = count($walls);\n            while ($l < $r) {\n     \
        \           $m = (int)(($l + $r) / 2);\n                if ($walls[$m] <= $target)\
        \ $l = $m + 1;\n                else $r = $m;\n            }\n            return\
        \ $l;\n        };\n\n        $countWalls = function($a, $b) use ($lowerBound,\
        \ $upperBound) {\n            if ($a > $b) return 0;\n            return $upperBound($b)\
        \ - $lowerBound($a);\n        };\n\n        $hasWall = function($pos) use ($lowerBound,\
        \ &$walls) {\n            $idx = $lowerBound($pos);\n            return ($idx\
        \ < count($walls) && $walls[$idx] == $pos) ? 1 : 0;\n        };\n\n        $dp\
        \ = array_fill(0, $n * 2, 0);\n        $dp[0] = $countWalls($lBoundaries[0],\
        \ $robots[0]);\n        $dp[1] = $countWalls($robots[0], $rBoundaries[0]);\n\
        \n        for ($i = 1; $i < $n; $i++) {\n            $val1 = $dp[($i - 1) *\
        \ 2] + $countWalls($lBoundaries[$i], $robots[$i]) - ($lBoundaries[$i] == $robots[$i\
        \ - 1] ? $hasWall($robots[$i - 1]) : 0);\n            $val2 = $dp[($i - 1) *\
        \ 2 + 1] + $countWalls($lBoundaries[$i], $robots[$i]) - $countWalls($lBoundaries[$i],\
        \ $rBoundaries[$i - 1]);\n            $dp[$i * 2] = max($val1, $val2);\n\n \
        \           $val3 = $dp[($i - 1) * 2] + $countWalls($robots[$i], $rBoundaries[$i]);\n\
        \            $val4 = $dp[($i - 1) * 2 + 1] + $countWalls($robots[$i], $rBoundaries[$i])\
        \ - ($rBoundaries[$i - 1] == $robots[$i] ? $hasWall($robots[$i]) : 0);\n   \
        \         $dp[$i * 2 + 1] = max($val3, $val4);\n        }\n\n        return\
        \ max($dp[($n - 1) * 2], $dp[($n - 1) * 2 + 1]);\n    }\n}"
      swift: "class Solution {\n    func maxWalls(_ robots: [Int], _ distance: [Int],\
        \ _ walls: [Int]) -> Int {\n        let n = robots.count\n        let sortedIndices\
        \ = (0..<n).sorted { robots[$0] < robots[$1] }\n        let sortedRobots = sortedIndices.map\
        \ { robots[$0] }\n        let sortedDistances = sortedIndices.map { distance[$0]\
        \ }\n        let sortedWalls = walls.sorted()\n\n        func lowerBound(_ arr:\
        \ [Int], _ target: Int) -> Int {\n            var l = 0, r = arr.count\n   \
        \         while l < r {\n                let m = l + (r - l) / 2\n         \
        \       if arr[m] < target { l = m + 1 } else { r = m }\n            }\n   \
        \         return l\n        }\n\n        func upperBound(_ arr: [Int], _ target:\
        \ Int) -> Int {\n            var l = 0, r = arr.count\n            while l <\
        \ r {\n                let m = l + (r - l) / 2\n                if arr[m] <=\
        \ target { l = m + 1 } else { r = m }\n            }\n            return l\n\
        \        }\n\n        func countWalls(_ a: Int, _ b: Int) -> Int {\n       \
        \     if a > b { return 0 }\n            return upperBound(sortedWalls, b) -\
        \ lowerBound(sortedWalls, a)\n        }\n\n        func hasWall(_ pos: Int)\
        \ -> Int {\n            let idx = lowerBound(sortedWalls, pos)\n           \
        \ return (idx < sortedWalls.count && sortedWalls[idx] == pos) ? 1 : 0\n    \
        \    }\n\n        var lBoundaries = [Int](repeating: 0, count: n)\n        var\
        \ rBoundaries = [Int](repeating: 0, count: n)\n        for i in 0..<n {\n  \
        \          lBoundaries[i] = max(sortedRobots[i] - sortedDistances[i], i > 0\
        \ ? sortedRobots[i - 1] : -2000000000)\n            rBoundaries[i] = min(sortedRobots[i]\
        \ + sortedDistances[i], i < n - 1 ? sortedRobots[i + 1] : 2000000000)\n    \
        \    }\n\n        var dp = [Int](repeating: 0, count: n * 2)\n        dp[0]\
        \ = countWalls(lBoundaries[0], sortedRobots[0])\n        dp[1] = countWalls(sortedRobots[0],\
        \ rBoundaries[0])\n\n        if n > 1 {\n            for i in 1..<n {\n    \
        \            let val1 = dp[(i - 1) * 2] + countWalls(lBoundaries[i], sortedRobots[i])\
        \ - (lBoundaries[i] == sortedRobots[i - 1] ? hasWall(sortedRobots[i - 1]) :\
        \ 0)\n                let val2 = dp[(i - 1) * 2 + 1] + countWalls(lBoundaries[i],\
        \ sortedRobots[i]) - countWalls(lBoundaries[i], rBoundaries[i - 1])\n      \
        \          dp[i * 2] = max(val1, val2)\n\n                let val3 = dp[(i -\
        \ 1) * 2] + countWalls(sortedRobots[i], rBoundaries[i])\n                let\
        \ val4 = dp[(i - 1) * 2 + 1] + countWalls(sortedRobots[i], rBoundaries[i]) -\
        \ (rBoundaries[i - 1] == sortedRobots[i] ? hasWall(sortedRobots[i]) : 0)\n \
        \               dp[i * 2 + 1] = max(val3, val4)\n            }\n        }\n\n\
        \        return max(dp[(n - 1) * 2], dp[(n - 1) * 2 + 1])\n    }\n}"
      kotlin: "class Solution {\n    fun maxWalls(robots: IntArray, distance: IntArray,\
        \ walls: IntArray): Int {\n        val n = robots.size\n        data class Robot(val\
        \ pos: Int, val dist: Int)\n        val rbs = Array(n) { i -> Robot(robots[i],\
        \ distance[i]) }.sortedBy { it.pos }\n        walls.sort()\n\n        fun count(a:\
        \ Int, b: Int): Int {\n            if (a > b) return 0\n            var idxA\
        \ = walls.binarySearch(a)\n            if (idxA < 0) idxA = -idxA - 1\n    \
        \        var idxB = walls.binarySearch(b)\n            if (idxB < 0) idxB =\
        \ -idxB - 1 else idxB += 1\n            return idxB - idxA\n        }\n\n  \
        \      val dp = Array(n) { IntArray(2) }\n        var prevPos = -1000000000\n\
        \        for (i in 0 until n) {\n            val nextPos = if (i < n - 1) rbs[i\
        \ + 1].pos else 2000000000\n            val li = maxOf(rbs[i].pos - rbs[i].dist,\
        \ prevPos)\n            val ri = minOf(rbs[i].pos + rbs[i].dist, nextPos)\n\n\
        \            if (i == 0) {\n                dp[0][0] = count(li, rbs[0].pos)\n\
        \                dp[0][1] = count(rbs[0].pos, ri)\n            } else {\n  \
        \              val riPrev = minOf(rbs[i - 1].pos + rbs[i - 1].dist, rbs[i].pos)\n\
        \n                dp[i][0] = maxOf(\n                    dp[i - 1][0] + count(li,\
        \ rbs[i].pos) - count(li, rbs[i - 1].pos),\n                    dp[i - 1][1]\
        \ + count(li, rbs[i].pos) - count(li, riPrev)\n                )\n         \
        \       dp[i][1] = maxOf(\n                    dp[i - 1][0] + count(rbs[i].pos,\
        \ ri),\n                    dp[i - 1][1] + count(rbs[i].pos, ri) - count(rbs[i].pos,\
        \ riPrev)\n                )\n            }\n            prevPos = rbs[i].pos\n\
        \        }\n\n        return maxOf(dp[n - 1][0], dp[n - 1][1])\n    }\n}"
      dart: "class Solution {\n  int maxWalls(List<int> robots, List<int> distance,\
        \ List<int> walls) {\n    int n = robots.length;\n    List<Robot> rbs = List.generate(n,\
        \ (i) => Robot(robots[i], distance[i]));\n    rbs.sort((a, b) => a.pos.compareTo(b.pos));\n\
        \    walls.sort();\n\n    int lowerBound(List<int> sortedList, int value) {\n\
        \      int low = 0, high = sortedList.length;\n      while (low < high) {\n\
        \        int mid = low + ((high - low) >> 1);\n        if (sortedList[mid] <\
        \ value) low = mid + 1;\n        else high = mid;\n      }\n      return low;\n\
        \    }\n\n    int upperBound(List<int> sortedList, int value) {\n      int low\
        \ = 0, high = sortedList.length;\n      while (low < high) {\n        int mid\
        \ = low + ((high - low) >> 1);\n        if (sortedList[mid] <= value) low =\
        \ mid + 1;\n        else high = mid;\n      }\n      return low;\n    }\n\n\
        \    int count(int a, int b) {\n      if (a > b) return 0;\n      return upperBound(walls,\
        \ b) - lowerBound(walls, a);\n    }\n\n    List<List<int>> dp = List.generate(n,\
        \ (_) => List.filled(2, 0));\n    int prevPos = -1000000000;\n\n    for (int\
        \ i = 0; i < n; i++) {\n      int nextPos = (i < n - 1) ? rbs[i + 1].pos : 2000000000;\n\
        \      int li = (rbs[i].pos - rbs[i].dist > prevPos) ? rbs[i].pos - rbs[i].dist\
        \ : prevPos;\n      int ri = (rbs[i].pos + rbs[i].dist < nextPos) ? rbs[i].pos\
        \ + rbs[i].dist : nextPos;\n\n      if (i == 0) {\n        dp[0][0] = count(li,\
        \ rbs[0].pos);\n        dp[0][1] = count(rbs[0].pos, ri);\n      } else {\n\
        \        int riPrev = (rbs[i - 1].pos + rbs[i - 1].dist < rbs[i].pos) ? rbs[i\
        \ - 1].pos + rbs[i - 1].dist : rbs[i].pos;\n\n        int c1 = dp[i - 1][0]\
        \ + count(li, rbs[i].pos) - count(li, rbs[i - 1].pos);\n        int c2 = dp[i\
        \ - 1][1] + count(li, rbs[i].pos) - count(li, riPrev);\n        dp[i][0] = (c1\
        \ > c2) ? c1 : c2;\n\n        int c3 = dp[i - 1][0] + count(rbs[i].pos, ri);\n\
        \        int c4 = dp[i - 1][1] + count(rbs[i].pos, ri) - count(rbs[i].pos, riPrev);\n\
        \        dp[i][1] = (c3 > c4) ? c3 : c4;\n      }\n      prevPos = rbs[i].pos;\n\
        \    }\n\n    return (dp[n - 1][0] > dp[n - 1][1]) ? dp[n - 1][0] : dp[n - 1][1];\n\
        \  }\n}\n\nclass Robot {\n  final int pos;\n  final int dist;\n  Robot(this.pos,\
        \ this.dist);\n}"
      go: "import (\n    \"sort\"\n)\n\ntype Robot struct {\n    pos  int\n    dist\
        \ int\n}\n\nfunc maxWalls(robots []int, distance []int, walls []int) int {\n\
        \    n := len(robots)\n    rbs := make([]Robot, n)\n    for i := range robots\
        \ {\n        rbs[i] = Robot{robots[i], distance[i]}\n    }\n    sort.Slice(rbs,\
        \ func(i, j int) bool { return rbs[i].pos < rbs[j].pos })\n    sort.Ints(walls)\n\
        \n    count := func(a, b int) int {\n        if a > b {\n            return\
        \ 0\n        }\n        idxA := sort.SearchInts(walls, a)\n        idxB := sort.SearchInts(walls,\
        \ b+1)\n        return idxB - idxA\n    }\n\n    maxVal := func(a, b int) int\
        \ {\n        if a > b { return a }\n        return b\n    }\n    minVal := func(a,\
        \ b int) int {\n        if a < b { return a }\n        return b\n    }\n\n \
        \   dp := make([][2]int, n)\n    prevPos := -1000000000\n\n    for i := 0; i\
        \ < n; i++ {\n        nextPos := 2000000000\n        if i < n-1 {\n        \
        \    nextPos = rbs[i+1].pos\n        }\n\n        li := maxVal(rbs[i].pos -\
        \ rbs[i].dist, prevPos)\n        ri := minVal(rbs[i].pos + rbs[i].dist, nextPos)\n\
        \n        if i == 0 {\n            dp[0][0] = count(li, rbs[0].pos)\n      \
        \      dp[0][1] = count(rbs[0].pos, ri)\n        } else {\n            riPrev\
        \ := minVal(rbs[i-1].pos + rbs[i-1].dist, rbs[i].pos)\n\n            dp[i][0]\
        \ = maxVal(\n                dp[i-1][0] + count(li, rbs[i].pos) - count(li,\
        \ rbs[i-1].pos),\n                dp[i-1][1] + count(li, rbs[i].pos) - count(li,\
        \ riPrev),\n            )\n            dp[i][1] = maxVal(\n                dp[i-1][0]\
        \ + count(rbs[i].pos, ri),\n                dp[i-1][1] + count(rbs[i].pos, ri)\
        \ - count(rbs[i].pos, riPrev),\n            )\n        }\n        prevPos =\
        \ rbs[i].pos\n    }\n\n    return maxVal(dp[n-1][0], dp[n-1][1])\n}"
      ruby: "def max_walls(robots, distance, walls)\n  n = robots.size\n  combined =\
        \ robots.zip(distance).sort_by { |r, d| r }\n  r = combined.map { |x| x[0] }\n\
        \  d = combined.map { |x| x[1] }\n  walls.sort!\n  n_walls = walls.size\n\n\
        \  count = ->(a, b) {\n    return 0 if a > b\n    idx1 = walls.bsearch_index\
        \ { |x| x >= a } || n_walls\n    idx2 = walls.bsearch_index { |x| x > b } ||\
        \ n_walls\n    idx2 - idx1\n  }\n\n  dp = Array.new(n) { [0, 0] }\n  dp[0][0]\
        \ = count.call([r[0] - d[0], -2000000000].max, r[0])\n  dp[0][1] = count.call(r[0],\
        \ [r[0] + d[0], (n > 1 ? r[1] : 2000000000)].min)\n\n  (1...n).each do |i|\n\
        \    ri = r[i]\n    di = d[i]\n    ri_prev = r[i - 1]\n    di_prev = d[i - 1]\n\
        \    ri_next = (i + 1 < n) ? r[i + 1] : 2000000000\n\n    l_range_start = [ri\
        \ - di, ri_prev].max\n    l_range_end = ri\n    r_range_start = ri\n    r_range_end\
        \ = [ri + di, ri_next].min\n\n    c_li = count.call(l_range_start, l_range_end)\n\
        \    c_ri = count.call(r_range_start, r_range_end)\n\n    wall_at_ri_prev =\
        \ count.call(ri_prev, ri_prev)\n    wall_at_ri = count.call(ri, ri)\n\n    overlap_start\
        \ = [ri_prev, ri - di].max\n    overlap_end = [ri_prev + di_prev, ri].min\n\
        \    c_overlap = count.call(overlap_start, overlap_end)\n\n    dp[i][0] = [\n\
        \      dp[i - 1][0] + c_li - (ri - di <= ri_prev ? wall_at_ri_prev : 0),\n \
        \     dp[i - 1][1] + c_li - c_overlap\n    ].max\n\n    dp[i][1] = [\n     \
        \ dp[i - 1][0] + c_ri,\n      dp[i - 1][1] + c_ri - (ri_prev + di_prev >= ri\
        \ ? wall_at_ri : 0)\n    ].max\n  end\n\n  [dp[n - 1][0], dp[n - 1][1]].max\n\
        end"
      scala: "object Solution {\n  def maxWalls(robots: Array[Int], distance: Array[Int],\
        \ walls: Array[Int]): Int = {\n    val n = robots.length\n    val combined =\
        \ robots.zip(distance).sortBy(_._1)\n    val r = combined.map(_._1)\n    val\
        \ d = combined.map(_._2)\n    val sortedWalls = walls.sorted\n\n    def partitionPoint(arr:\
        \ Array[Int], p: Int => Boolean): Int = {\n      var low = 0\n      var high\
        \ = arr.length\n      while (low < high) {\n        val mid = low + (high -\
        \ low) / 2\n        if (p(arr(mid))) low = mid + 1\n        else high = mid\n\
        \      }\n      low\n    }\n\n    def count(a: Int, b: Int): Int = {\n     \
        \ if (a > b) 0\n      else {\n        val idx1 = partitionPoint(sortedWalls,\
        \ (x: Int) => x < a)\n        val idx2 = partitionPoint(sortedWalls, (x: Int)\
        \ => x <= b)\n        idx2 - idx1\n      }\n    }\n\n    val dp = Array.ofDim[Int](n,\
        \ 2)\n    dp(0)(0) = count(math.max(r(0) - d(0), -2000000000), r(0))\n    dp(0)(1)\
        \ = count(r(0), math.min(r(0) + d(0), if (n > 1) r(1) else 2000000000))\n\n\
        \    for (i <- 1 until n) {\n      val ri = r(i)\n      val di = d(i)\n    \
        \  val riPrev = r(i - 1)\n      val diPrev = d(i - 1)\n      val riNext = if\
        \ (i + 1 < n) r(i + 1) else 2000000000\n\n      val lRangeStart = math.max(ri\
        \ - di, riPrev)\n      val lRangeEnd = ri\n      val rRangeStart = ri\n    \
        \  val rRangeEnd = math.min(ri + di, riNext)\n\n      val cLi = count(lRangeStart,\
        \ lRangeEnd)\n      val cRi = count(rRangeStart, rRangeEnd)\n\n      val wallAtRiPrev\
        \ = if (java.util.Arrays.binarySearch(sortedWalls, riPrev) >= 0) 1 else 0\n\
        \      val wallAtRi = if (java.util.Arrays.binarySearch(sortedWalls, ri) >=\
        \ 0) 1 else 0\n\n      val overlapStart = math.max(riPrev, ri - di)\n      val\
        \ overlapEnd = math.min(riPrev + diPrev, ri)\n      val cOverlap = count(overlapStart,\
        \ overlapEnd)\n\n      dp(i)(0) = math.max(\n        dp(i - 1)(0) + cLi - (if\
        \ (ri - di <= riPrev) wallAtRiPrev else 0),\n        dp(i - 1)(1) + cLi - cOverlap\n\
        \      )\n\n      dp(i)(1) = math.max(\n        dp(i - 1)(0) + cRi,\n      \
        \  dp(i - 1)(1) + cRi - (if (riPrev + diPrev >= ri) wallAtRi else 0)\n     \
        \ )\n    }\n\n    math.max(dp(n - 1)(0), dp(n - 1)(1))\n  }\n}"
      rust: "impl Solution {\n    pub fn max_walls(robots: Vec<i32>, distance: Vec<i32>,\
        \ walls: Vec<i32>) -> i32 {\n        let mut sorted_walls = walls;\n       \
        \ sorted_walls.sort_unstable();\n        let mut combined: Vec<(i32, i32)> =\
        \ robots.into_iter().zip(distance.into_iter()).collect();\n        combined.sort_unstable_by_key(|&(pos,\
        \ _)| pos);\n        let r: Vec<i32> = combined.iter().map(|&(pos, _)| pos).collect();\n\
        \        let d: Vec<i32> = combined.iter().map(|&(_, dist)| dist).collect();\n\
        \        let n = r.len();\n\n        let count = |a: i32, b: i32| -> i32 {\n\
        \            if a > b {\n                0\n            } else {\n         \
        \       let idx1 = sorted_walls.partition_point(|&x| x < a);\n             \
        \   let idx2 = sorted_walls.partition_point(|&x| x <= b);\n                (idx2\
        \ - idx1) as i32\n            }\n        };\n\n        let mut dp = vec![[0,\
        \ 0]; n];\n\n        dp[0][0] = count(r[0].saturating_sub(d[0]).max(-2_000_000_000),\
        \ r[0]);\n        dp[0][1] = count(r[0], r[0].saturating_add(d[0]).min(if n\
        \ > 1 { r[1] } else { 2_000_000_000 }));\n\n        for i in 1..n {\n      \
        \      let ri = r[i];\n            let di = d[i];\n            let ri_prev =\
        \ r[i - 1];\n            let di_prev = d[i - 1];\n            let ri_next =\
        \ if i + 1 < n { r[i + 1] } else { 2_000_000_000 };\n\n            let l_range_start\
        \ = (ri - di).max(ri_prev);\n            let l_range_end = ri;\n           \
        \ let r_range_start = ri;\n            let r_range_end = (ri + di).min(ri_next);\n\
        \n            let c_li = count(l_range_start, l_range_end);\n            let\
        \ c_ri = count(r_range_start, r_range_end);\n\n            let wall_at_ri_prev\
        \ = if sorted_walls.binary_search(&ri_prev).is_ok() { 1 } else { 0 };\n    \
        \        let wall_at_ri = if sorted_walls.binary_search(&ri).is_ok() { 1 } else\
        \ { 0 };\n\n            let overlap_start = ri_prev.max(ri - di);\n        \
        \    let overlap_end = (ri_prev + di_prev).min(ri);\n            let c_overlap\
        \ = count(overlap_start, overlap_end);\n\n            dp[i][0] = (\n       \
        \         dp[i - 1][0] + c_li - if ri - di <= ri_prev { wall_at_ri_prev } else\
        \ { 0 }\n            ).max(\n                dp[i - 1][1] + c_li - c_overlap\n\
        \            );\n\n            dp[i][1] = (\n                dp[i - 1][0] +\
        \ c_ri\n            ).max(\n                dp[i - 1][1] + c_ri - if ri_prev\
        \ + di_prev >= ri { wall_at_ri } else { 0 }\n            );\n        }\n\n \
        \       dp[n - 1][0].max(dp[n - 1][1])\n    }\n}"
      racket: "(define/contract (max-walls robots distance walls)\n  (-> (listof exact-integer?)\
        \ (listof exact-integer?) (listof exact-integer?) exact-integer?)\n  (let* ([n\
        \ (length robots)]\n         [robots-with-dist (sort (map list robots distance)\
        \ < #:key car)]\n         [robot-positions (list->vector (map car robots-with-dist))]\n\
        \         [robot-distances (list->vector (map cadr robots-with-dist))]\n   \
        \      [sorted-walls (list->vector (sort walls <))]\n         [m (vector-length\
        \ sorted-walls)])\n    (define (lower-bound val)\n      (let loop ([low 0] [high\
        \ m])\n        (if (< low high)\n            (let ([mid (quotient (+ low high)\
        \ 2)])\n              (if (< (vector-ref sorted-walls mid) val)\n          \
        \        (loop (+ mid 1) high)\n                  (loop low mid)))\n       \
        \     low)))\n    (define (upper-bound val)\n      (let loop ([low 0] [high\
        \ m])\n        (if (< low high)\n            (let ([mid (quotient (+ low high)\
        \ 2)])\n              (if (<= (vector-ref sorted-walls mid) val)\n         \
        \         (loop (+ mid 1) high)\n                  (loop low mid)))\n      \
        \      low)))\n    (define (count a b)\n      (if (> a b) 0\n          (- (upper-bound\
        \ b) (lower-bound a))))\n    (let* ([r0 (vector-ref robot-positions 0)]\n  \
        \         [d0 (vector-ref robot-distances 0)]\n           [r1 (if (> n 1) (vector-ref\
        \ robot-positions 1) 2000000000)]\n           [dp0L (count (- r0 d0) r0)]\n\
        \           [dp0R (count r0 (min r1 (+ r0 d0)))])\n      (let loop ([i 1] [prevL\
        \ dp0L] [prevR dp0R])\n        (if (< i n)\n            (let* ([r_prev (vector-ref\
        \ robot-positions (- i 1))]\n                   [d_prev (vector-ref robot-distances\
        \ (- i 1))]\n                   [r_curr (vector-ref robot-positions i)]\n  \
        \                 [d_curr (vector-ref robot-distances i)]\n                \
        \   [r_next (if (< i (- n 1)) (vector-ref robot-positions (+ i 1)) 2000000000)]\n\
        \                   [new_L_prev_L (- (count (max r_prev (- r_curr d_curr)) r_curr)\
        \ (count (max r_prev (- r_curr d_curr)) r_prev))]\n                   [new_L_prev_R\
        \ (- (count (max r_prev (- r_curr d_curr)) r_curr) (count (max r_prev (- r_curr\
        \ d_curr)) (min r_curr (+ r_prev d_prev))))]\n                   [dpL (max (+\
        \ prevL new_L_prev_L) (+ prevR new_L_prev_R))]\n                   [new_R_prev_L\
        \ (count r_curr (min r_next (+ r_curr d_curr)))]\n                   [new_R_prev_R\
        \ (- (count r_curr (min r_next (+ r_curr d_curr))) (count r_curr (min r_curr\
        \ (+ r_prev d_prev))))]\n                   [dpR (max (+ prevL new_R_prev_L)\
        \ (+ prevR new_R_prev_R))])\n              (loop (+ i 1) dpL dpR))\n       \
        \     (max prevL prevR))))))"
      erlang: "-spec max_walls(Robots :: [integer()], Distance :: [integer()], Walls\
        \ :: [integer()]) -> integer().\nmax_walls(Robots, Distance, Walls) ->\n   \
        \ SortedWalls = lists:sort(Walls),\n    WallsTuple = list_to_tuple(SortedWalls),\n\
        \    M = tuple_size(WallsTuple),\n    SortedRD = lists:sort(lists:zip(Robots,\
        \ Distance)),\n    N = length(SortedRD),\n    {RPList, RDList} = lists:unzip(SortedRD),\n\
        \    RPTuple = list_to_tuple(RPList),\n    RDTuple = list_to_tuple(RDList),\n\
        \    R0 = element(1, RPTuple),\n    D0 = element(1, RDTuple),\n    R1 = if N\
        \ > 1 -> element(2, RPTuple); true -> 2000000000 end,\n    DP0L = count(WallsTuple,\
        \ M, R0 - D0, R0),\n    DP0R = count(WallsTuple, M, R0, erlang:min(R1, R0 +\
        \ D0)),\n    solve(1, N, RPTuple, RDTuple, WallsTuple, M, DP0L, DP0R).\n\nsolve(I,\
        \ N, RPTuple, RDTuple, WallsTuple, M, PrevL, PrevR) ->\n    if I < N ->\n  \
        \      RPrev = element(I, RPTuple),\n        DPrev = element(I, RDTuple),\n\
        \        RCurr = element(I + 1, RPTuple),\n        DCurr = element(I + 1, RDTuple),\n\
        \        RNext = if I + 1 < N -> element(I + 2, RPTuple); true -> 2000000000\
        \ end,\n\n        New_L_prev_L = count(WallsTuple, M, erlang:max(RPrev, RCurr\
        \ - DCurr), RCurr) - count(WallsTuple, M, erlang:max(RPrev, RCurr - DCurr),\
        \ RPrev),\n        New_L_prev_R = count(WallsTuple, M, erlang:max(RPrev, RCurr\
        \ - DCurr), RCurr) - count(WallsTuple, M, erlang:max(RPrev, RCurr - DCurr),\
        \ erlang:min(RCurr, RPrev + DPrev)),\n        DPCurrL = erlang:max(PrevL + New_L_prev_L,\
        \ PrevR + New_L_prev_R),\n\n        New_R_prev_L = count(WallsTuple, M, RCurr,\
        \ erlang:min(RNext, RCurr + DCurr)),\n        New_R_prev_R = count(WallsTuple,\
        \ M, RCurr, erlang:min(RNext, RCurr + DCurr)) - count(WallsTuple, M, RCurr,\
        \ erlang:min(RCurr, RPrev + DPrev)),\n        DPCurrR = erlang:max(PrevL + New_R_prev_L,\
        \ PrevR + New_R_prev_R),\n\n        solve(I + 1, N, RPTuple, RDTuple, WallsTuple,\
        \ M, DPCurrL, DPCurrR);\n    true ->\n        erlang:max(PrevL, PrevR)\n   \
        \ end.\n\ncount(Walls, M, A, B) ->\n    if A > B -> 0;\n    true ->\n      \
        \  upper_bound(Walls, M, B, 0, M) - lower_bound(Walls, M, A, 0, M)\n    end.\n\
        \nlower_bound(Tuple, M, Val, Low, High) when Low < High ->\n    Mid = (Low +\
        \ High) div 2,\n    case element(Mid + 1, Tuple) < Val of\n        true -> lower_bound(Tuple,\
        \ M, Val, Mid + 1, High);\n        false -> lower_bound(Tuple, M, Val, Low,\
        \ Mid)\n    end;\nlower_bound(_, _, _, Low, _) -> Low.\n\nupper_bound(Tuple,\
        \ M, Val, Low, High) when Low < High ->\n    Mid = (Low + High) div 2,\n   \
        \ case element(Mid + 1, Tuple) =< Val of\n        true -> upper_bound(Tuple,\
        \ M, Val, Mid + 1, High);\n        false -> upper_bound(Tuple, M, Val, Low,\
        \ Mid)\n    end;\nupper_bound(_, _, _, Low, _) -> Low."
      elixir: "defmodule Solution do\n  @spec max_walls(robots :: [integer], distance\
        \ :: [integer], walls :: [integer]) :: integer\n  def max_walls(robots, distance,\
        \ walls) do\n    sorted_walls = walls |> Enum.sort() |> List.to_tuple()\n  \
        \  m = tuple_size(sorted_walls)\n    sorted_rd = Enum.zip(robots, distance)\
        \ |> Enum.sort_by(fn {r, _d} -> r end)\n    n = length(sorted_rd)\n    rp_tuple\
        \ = sorted_rd |> Enum.map(fn {r, _d} -> r end) |> List.to_tuple()\n    rd_tuple\
        \ = sorted_rd |> Enum.map(fn {_r, d} -> d end) |> List.to_tuple()\n\n    r0\
        \ = elem(rp_tuple, 0)\n    d0 = elem(rd_tuple, 0)\n    r1 = if n > 1, do: elem(rp_tuple,\
        \ 1), else: 2000000000\n\n    dp0l = count(sorted_walls, m, r0 - d0, r0)\n \
        \   dp0r = count(sorted_walls, m, r0, min(r1, r0 + d0))\n\n    solve(1, n, rp_tuple,\
        \ rd_tuple, sorted_walls, m, dp0l, dp0r)\n  end\n\n  defp solve(i, n, rp_tuple,\
        \ rd_tuple, walls, m, prev_l, prev_r) do\n    if i < n do\n      r_prev = elem(rp_tuple,\
        \ i - 1)\n      d_prev = elem(rd_tuple, i - 1)\n      r_curr = elem(rp_tuple,\
        \ i)\n      d_curr = elem(rd_tuple, i)\n      r_next = if i + 1 < n, do: elem(rp_tuple,\
        \ i + 1), else: 2000000000\n\n      new_l_prev_l = count(walls, m, max(r_prev,\
        \ r_curr - d_curr), r_curr) - count(walls, m, max(r_prev, r_curr - d_curr),\
        \ r_prev)\n      new_l_prev_r = count(walls, m, max(r_prev, r_curr - d_curr),\
        \ r_curr) - count(walls, m, max(r_prev, r_curr - d_curr), min(r_curr, r_prev\
        \ + d_prev))\n      dp_curr_l = max(prev_l + new_l_prev_l, prev_r + new_l_prev_r)\n\
        \n      new_r_prev_l = count(walls, m, r_curr, min(r_next, r_curr + d_curr))\n\
        \      new_r_prev_r = count(walls, m, r_curr, min(r_next, r_curr + d_curr))\
        \ - count(walls, m, r_curr, min(r_curr, r_prev + d_prev))\n      dp_curr_r =\
        \ max(prev_l + new_r_prev_l, prev_r + new_r_prev_r)\n\n      solve(i + 1, n,\
        \ rp_tuple, rd_tuple, walls, m, dp_curr_l, dp_curr_r)\n    else\n      max(prev_l,\
        \ prev_r)\n    end\n  end\n\n  defp count(walls, m, a, b) do\n    if a > b do\n\
        \      0\n    else\n      upper_bound(walls, m, b, 0, m) - lower_bound(walls,\
        \ m, a, 0, m)\n    end\n  end\n\n  defp lower_bound(tuple, m, val, low, high)\
        \ do\n    if low < high do\n      mid = div(low + high, 2)\n      if elem(tuple,\
        \ mid) < val do\n        lower_bound(tuple, m, val, mid + 1, high)\n      else\n\
        \        lower_bound(tuple, m, val, low, mid)\n      end\n    else\n      low\n\
        \    end\n  end\n\n  defp upper_bound(tuple, m, val, low, high) do\n    if low\
        \ < high do\n      mid = div(low + high, 2)\n      if elem(tuple, mid) <= val\
        \ do\n        upper_bound(tuple, m, val, mid + 1, high)\n      else\n      \
        \  upper_bound(tuple, m, val, low, mid)\n      end\n    else\n      low\n  \
        \  end\n  end\nend"
    approach: 'Sort the robots and walls by position to process them efficiently. Each
      robot $i$ at position $R_i$ can destroy walls at its own position $R_i$ and hit
      ranges within the constraints of its distance $d_i$ and the positions of neighboring
      robots $R_{i-1}$ and $R_{i+1}$. The robots act as fixed obstacles, meaning a bullet
      from robot $i$ can cover a left-range of $[\max(R_{i-1}, R_i - d_i), R_i]$ and
      a right-range of $[R_i, \min(R_{i+1}, R_i + d_i)]$. By partitioning all walls
      into those at robot positions, those between robots, and those outside the robot
      range, the problem can be modeled using dynamic programming.


      Define $DP[i][0]$ and $DP[i][1]$ as the maximum unique walls destroyed by the
      first $i$ robots where robot $i$ shoots left or right, respectively. The transition
      for $DP[i][0]$ considers whether robot $i-1$ shot left or right, accounting for
      the union of wall coverage in the interval $(R_{i-1}, R_i)$ to avoid double-counting.
      $DP[i][1]$ simply adds the walls in the interval $(R_i, R_{i+1})$ hit by robot
      $i$ to the maximum of $DP[i-1][0]$ or $DP[i-1][1]$. The wall at each robot''s
      position $R_i$ is always counted exactly once because every robot must fire and
      every fire range includes the robot''s own position. Binary search (lower and
      upper bounds) is used to count walls in specific intervals in $O(\log M)$ time.'
    time_complexity: O((N + M) \log M + N \log N), where N is the number of robots and
      M is the number of walls. This accounts for sorting both robots and walls and
      performing a constant number of binary search range queries for each of the N
      robots during the dynamic programming phase.
    space_complexity: O(N + M), required to store the sorted robots, walls, and the
      dynamic programming table of size $N \times 2$.
    elapsed_time: 1035.5841674804688
    model: gemini-3-flash-preview
    generated_at: '2026-04-06 05:35:19 '
---

## Problem #3661: Maximum Walls Destroyed by Robots

**Difficulty:** Hard

**Topics:** Array, Binary Search, Dynamic Programming, Sorting

## Problem Description

<div data-docx-has-block-data="false" data-lark-html-role="root" data-page-id="Rax8d6clvoFeVtx7bzXcvkVynwf">
<div class="old-record-id-Y5dGdSKIMoNTttxGhHLccrpEnaf">There is an endless straight line populated with some robots and walls. You are given integer arrays <code>robots</code>, <code>distance</code>, and <code>walls</code>:</div>
</div>

<ul>
	<li><code>robots[i]</code> is the position of the <code>i<sup>th</sup></code> robot.</li>
	<li><code>distance[i]</code> is the <strong>maximum</strong> distance the <code>i<sup>th</sup></code> robot&#39;s bullet can travel.</li>
	<li><code>walls[j]</code> is the position of the <code>j<sup>th</sup></code> wall.</li>
</ul>

<p>Every robot has <strong>one</strong> bullet that can either fire to the left or the right <strong>at most </strong><code>distance[i]</code> meters.</p>

<p>A bullet destroys every wall in its path that lies within its range. Robots are fixed obstacles: if a bullet hits another robot before reaching a wall, it <strong>immediately stops</strong> at that robot and cannot continue.</p>

<p>Return the <strong>maximum</strong> number of <strong>unique</strong> walls that can be destroyed by the robots.</p>

<p>Notes:</p>

<ul>
	<li>A wall and a robot may share the same position; the wall can be destroyed by the robot at that position.</li>
	<li>Robots are not destroyed by bullets.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">robots = [4], distance = [3], walls = [1,10]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li><code>robots[0] = 4</code> fires <strong>left</strong> with <code>distance[0] = 3</code>, covering <code>[1, 4]</code> and destroys <code>walls[0] = 1</code>.</li>
	<li>Thus, the answer is 1.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">robots = [10,2], distance = [5,1], walls = [5,2,7]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li><code>robots[0] = 10</code> fires <strong>left</strong> with <code>distance[0] = 5</code>, covering <code>[5, 10]</code> and destroys <code>walls[0] = 5</code> and <code>walls[2] = 7</code>.</li>
	<li><code>robots[1] = 2</code> fires <strong>left</strong> with <code>distance[1] = 1</code>, covering <code>[1, 2]</code> and destroys <code>walls[1] = 2</code>.</li>
	<li>Thus, the answer is 3.</li>
</ul>
</div>
<strong class="example">Example 3:</strong>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">robots = [1,2], distance = [100,1], walls = [10]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>In this example, only <code>robots[0]</code> can reach the wall, but its shot to the <strong>right</strong> is blocked by <code>robots[1]</code>; thus the answer is 0.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= robots.length == distance.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= walls.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= robots[i], walls[j] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= distance[i] &lt;= 10<sup>5</sup></code></li>
	<li>All values in <code>robots</code> are <strong>unique</strong></li>
	<li>All values in <code>walls</code> are <strong>unique</strong></li>
</ul>


## Hints

1. Sort both the robots and walls arrays. This will help in efficiently processing positions and performing range queries.

2. Each robot can shoot either left or right. However, if a robot fires and another robot is in its path, the bullet stops. You need to use the positions of neighboring robots to limit the shooting range.

3. Use binary search (lower_bound and upper_bound) to count how many walls fall within a certain range.

4. You can use dynamic programming to keep track of the maximum number of walls destroyed so far, depending on the direction the previous robot shot.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

Sort the robots and walls by position to process them efficiently. Each robot $i$ at position $R_i$ can destroy walls at its own position $R_i$ and hit ranges within the constraints of its distance $d_i$ and the positions of neighboring robots $R_{i-1}$ and $R_{i+1}$. The robots act as fixed obstacles, meaning a bullet from robot $i$ can cover a left-range of $[\max(R_{i-1}, R_i - d_i), R_i]$ and a right-range of $[R_i, \min(R_{i+1}, R_i + d_i)]$. By partitioning all walls into those at robot positions, those between robots, and those outside the robot range, the problem can be modeled using dynamic programming.

Define $DP[i][0]$ and $DP[i][1]$ as the maximum unique walls destroyed by the first $i$ robots where robot $i$ shoots left or right, respectively. The transition for $DP[i][0]$ considers whether robot $i-1$ shot left or right, accounting for the union of wall coverage in the interval $(R_{i-1}, R_i)$ to avoid double-counting. $DP[i][1]$ simply adds the walls in the interval $(R_i, R_{i+1})$ hit by robot $i$ to the maximum of $DP[i-1][0]$ or $DP[i-1][1]$. The wall at each robot's position $R_i$ is always counted exactly once because every robot must fire and every fire range includes the robot's own position. Binary search (lower and upper bounds) is used to count walls in specific intervals in $O(\log M)$ time.

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
    int countWallsInRange(const std::vector<int>& walls, int a, int b) {
        if (a > b) return 0;
        auto it1 = std::lower_bound(walls.begin(), walls.end(), a);
        auto it2 = std::upper_bound(walls.begin(), walls.end(), b);
        return std::distance(it1, it2);
    }

    int maxWalls(std::vector<int>& robots, std::vector<int>& distance, std::vector<int>& walls) {
        int n = robots.size();
        std::vector<std::pair<int, int>> rd(n);
        for (int i = 0; i < n; ++i) {
            rd[i] = {robots[i], distance[i]};
        }
        std::sort(rd.begin(), rd.end());
        for (int i = 0; i < n; ++i) {
            robots[i] = rd[i].first;
            distance[i] = rd[i].second;
        }
        std::sort(walls.begin(), walls.end());

        std::vector<long long> dp0(n, 0);
        std::vector<long long> dp1(n, 0);

        dp0[0] = countWallsInRange(walls, robots[0] - distance[0], robots[0] - 1);
        int r0_end = robots[0] + distance[0];
        if (n > 1) r0_end = std::min(r0_end, robots[1] - 1);
        dp1[0] = countWallsInRange(walls, robots[0] + 1, r0_end);

        for (int i = 1; i < n; ++i) {
            int li_start = std::max(robots[i] - distance[i], robots[i - 1] + 1);
            int li_end = robots[i] - 1;
            int c_li = countWallsInRange(walls, li_start, li_end);

            int ri_prev_end = std::min(robots[i - 1] + distance[i - 1], robots[i] - 1);
            int c_li_rem = countWallsInRange(walls, std::max(li_start, ri_prev_end + 1), li_end);

            dp0[i] = std::max(dp0[i - 1] + c_li, dp1[i - 1] + c_li_rem);

            int ri_end = robots[i] + distance[i];
            if (i < n - 1) ri_end = std::min(ri_end, robots[i + 1] - 1);
            dp1[i] = std::max(dp0[i - 1], dp1[i - 1]) + countWallsInRange(walls, robots[i] + 1, ri_end);
        }

        int walls_at_robots = 0;
        for (int r : robots) {
            if (std::binary_search(walls.begin(), walls.end(), r)) {
                walls_at_robots++;
            }
        }

        return (int)(std::max(dp0[n - 1], dp1[n - 1]) + walls_at_robots);
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
    public int maxWalls(int[] robots, int[] distance, int[] walls) {
        int n = robots.length;
        long[] combined = new long[n];
        for (int i = 0; i < n; i++) {
            combined[i] = ((long) robots[i] << 32) | (distance[i] & 0xFFFFFFFFL);
        }
        Arrays.sort(combined);
        for (int i = 0; i < n; i++) {
            robots[i] = (int) (combined[i] >> 32);
            distance[i] = (int) (combined[i] & 0xFFFFFFFFL);
        }
        Arrays.sort(walls);

        long[] dp0 = new long[n];
        long[] dp1 = new long[n];

        dp0[0] = countWallsInRange(walls, robots[0] - distance[0], robots[0] - 1);
        int r0End = robots[0] + distance[0];
        if (n > 1) r0End = Math.min(r0End, robots[1] - 1);
        dp1[0] = countWallsInRange(walls, robots[0] + 1, r0End);

        for (int i = 1; i < n; i++) {
            int liStart = Math.max(robots[i] - distance[i], robots[i - 1] + 1);
            int liEnd = robots[i] - 1;
            int cLi = countWallsInRange(walls, liStart, liEnd);

            int riPrevEnd = Math.min(robots[i - 1] + distance[i - 1], robots[i] - 1);
            int cLiRem = countWallsInRange(walls, Math.max(liStart, riPrevEnd + 1), liEnd);

            dp0[i] = Math.max(dp0[i - 1] + cLi, dp1[i - 1] + cLiRem);

            int riEnd = robots[i] + distance[i];
            if (i < n - 1) riEnd = Math.min(riEnd, robots[i + 1] - 1);
            dp1[i] = Math.max(dp0[i - 1], dp1[i - 1]) + countWallsInRange(walls, robots[i] + 1, riEnd);
        }

        int wallsAtRobots = 0;
        for (int r : robots) {
            if (Arrays.binarySearch(walls, r) >= 0) {
                wallsAtRobots++;
            }
        }

        return (int) (Math.max(dp0[n - 1], dp1[n - 1]) + wallsAtRobots);
    }

    private int countWallsInRange(int[] walls, int a, int b) {
        if (a > b) return 0;
        int idx1 = Arrays.binarySearch(walls, a);
        int lower = (idx1 < 0) ? -(idx1 + 1) : idx1;
        int idx2 = Arrays.binarySearch(walls, b);
        int upper = (idx2 < 0) ? -(idx2 + 1) : idx2 + 1;
        return upper - lower;
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
    def maxWalls(self, robots, distance, walls):
        """
        :type robots: List[int]
        :type distance: List[int]
        :type walls: List[int]
        :rtype: int
        """
        n = len(robots)
        rd = sorted(zip(robots, distance))
        robots = [x[0] for x in rd]
        distance = [x[1] for x in rd]
        walls.sort()

        def count(a, b):
            if a > b:
                return 0
            return bisect.bisect_right(walls, b) - bisect.bisect_left(walls, a)

        dp0 = [0] * n
        dp1 = [0] * n

        dp0[0] = count(robots[0] - distance[0], robots[0] - 1)
        r0_end = robots[0] + distance[0]
        if n > 1:
            r0_end = min(r0_end, robots[1] - 1)
        dp1[0] = count(robots[0] + 1, r0_end)

        for i in range(1, n):
            li_start = max(robots[i] - distance[i], robots[i-1] + 1)
            li_end = robots[i] - 1
            c_li = count(li_start, li_end)

            ri_prev_end = min(robots[i-1] + distance[i-1], robots[i] - 1)
            c_li_rem = count(max(li_start, ri_prev_end + 1), li_end)

            dp0[i] = max(dp0[i-1] + c_li, dp1[i-1] + c_li_rem)

            ri_end = robots[i] + distance[i]
            if i < n - 1:
                ri_end = min(ri_end, robots[i+1] - 1)
            dp1[i] = max(dp0[i-1], dp1[i-1]) + count(robots[i] + 1, ri_end)

        walls_at_robots = 0
        for r in robots:
            idx = bisect.bisect_left(walls, r)
            if idx < len(walls) and walls[idx] == r:
                walls_at_robots += 1

        return int(max(dp0[n-1], dp1[n-1]) + walls_at_robots)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import bisect

class Solution:
    def maxWalls(self, robots: list[int], distance: list[int], walls: list[int]) -> int:
        n = len(robots)
        rd = sorted(zip(robots, distance))
        robots = [x[0] for x in rd]
        distance = [x[1] for x in rd]
        walls.sort()

        def count(a, b):
            if a > b:
                return 0
            return bisect.bisect_right(walls, b) - bisect.bisect_left(walls, a)

        dp0 = [0] * n
        dp1 = [0] * n

        dp0[0] = count(robots[0] - distance[0], robots[0] - 1)
        r0_end = robots[0] + distance[0]
        if n > 1:
            r0_end = min(r0_end, robots[1] - 1)
        dp1[0] = count(robots[0] + 1, r0_end)

        for i in range(1, n):
            li_start = max(robots[i] - distance[i], robots[i-1] + 1)
            li_end = robots[i] - 1
            c_li = count(li_start, li_end)

            ri_prev_end = min(robots[i-1] + distance[i-1], robots[i] - 1)
            c_li_rem = count(max(li_start, ri_prev_end + 1), li_end)

            dp0[i] = max(dp0[i-1] + c_li, dp1[i-1] + c_li_rem)

            ri_end = robots[i] + distance[i]
            if i < n - 1:
                ri_end = min(ri_end, robots[i+1] - 1)
            dp1[i] = max(dp0[i-1], dp1[i-1]) + count(robots[i] + 1, ri_end)

        walls_at_robots = 0
        for r in robots:
            idx = bisect.bisect_left(walls, r)
            if idx < len(walls) and walls[idx] == r:
                walls_at_robots += 1

        return int(max(dp0[n-1], dp1[n-1]) + walls_at_robots)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int pos;
    int dist;
} Robot;

int compareRobots(const void* a, const void* b) {
    Robot* r1 = (Robot*)a;
    Robot* r2 = (Robot*)b;
    if (r1->pos < r2->pos) return -1;
    if (r1->pos > r2->pos) return 1;
    return 0;
}

int compareWalls(const void* a, const void* b) {
    int w1 = *(int*)a;
    int w2 = *(int*)b;
    if (w1 < w2) return -1;
    if (w1 > w2) return 1;
    return 0;
}

int lower_bound(int* arr, int size, long long val) {
    int low = 0, high = size;
    while (low < high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] >= val) high = mid;
        else low = mid + 1;
    }
    return low;
}

int upper_bound(int* arr, int size, long long val) {
    int low = 0, high = size;
    while (low < high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] > val) high = mid;
        else low = mid + 1;
    }
    return low;
}

int countInRange(int* walls, int wallsSize, long long a, long long b) {
    if (a > b) return 0;
    return upper_bound(walls, wallsSize, b) - lower_bound(walls, wallsSize, a);
}

int maxWalls(int* robots, int robotsSize, int* distance, int distanceSize, int* walls, int wallsSize) {
    Robot* sorted_robots = (Robot*)malloc(sizeof(Robot) * robotsSize);
    for (int i = 0; i < robotsSize; i++) {
        sorted_robots[i].pos = robots[i];
        sorted_robots[i].dist = distance[i];
    }
    qsort(sorted_robots, robotsSize, sizeof(Robot), compareRobots);
    qsort(walls, wallsSize, sizeof(int), compareWalls);

    int (*dp)[2] = malloc(sizeof(int) * robotsSize * 2);

    long long b0_r = (robotsSize == 1) ? ((long long)sorted_robots[0].pos + sorted_robots[0].dist) : ((long long)sorted_robots[0].pos + sorted_robots[0].dist);
    if (robotsSize > 1 && b0_r > sorted_robots[1].pos) b0_r = sorted_robots[1].pos;

    dp[0][0] = countInRange(walls, wallsSize, (long long)sorted_robots[0].pos - sorted_robots[0].dist, sorted_robots[0].pos);
    dp[0][1] = countInRange(walls, wallsSize, sorted_robots[0].pos, b0_r);

    for (int i = 1; i < robotsSize; i++) {
        long long b_prev_r = (long long)sorted_robots[i-1].pos + sorted_robots[i-1].dist;
        if (b_prev_r > sorted_robots[i].pos) b_prev_r = sorted_robots[i].pos;

        long long b_i_l = (long long)sorted_robots[i].pos - sorted_robots[i].dist;
        if (b_i_l < sorted_robots[i-1].pos) b_i_l = sorted_robots[i-1].pos;

        long long b_i_r;
        if (i == robotsSize - 1) {
            b_i_r = (long long)sorted_robots[i].pos + sorted_robots[i].dist;
        } else {
            b_i_r = (long long)sorted_robots[i].pos + sorted_robots[i].dist;
            if (b_i_r > sorted_robots[i+1].pos) b_i_r = sorted_robots[i+1].pos;
        }

        long long prev_r_pos = sorted_robots[i-1].pos;
        long long curr_r_pos = sorted_robots[i].pos;

        int dp0_from_dp0 = dp[i-1][0] + countInRange(walls, wallsSize, b_i_l > prev_r_pos + 1 ? b_i_l : prev_r_pos + 1, curr_r_pos);
        int dp0_from_dp1 = dp[i-1][1] + countInRange(walls, wallsSize, b_i_l > b_prev_r + 1 ? b_i_l : b_prev_r + 1, curr_r_pos);
        dp[i][0] = dp0_from_dp0 > dp0_from_dp1 ? dp0_from_dp0 : dp0_from_dp1;

        int dp1_from_dp0 = dp[i-1][0] + countInRange(walls, wallsSize, curr_r_pos, b_i_r);
        int dp1_from_dp1 = dp[i-1][1] + countInRange(walls, wallsSize, curr_r_pos > b_prev_r + 1 ? curr_r_pos : b_prev_r + 1, b_i_r);
        dp[i][1] = dp1_from_dp0 > dp1_from_dp1 ? dp1_from_dp0 : dp1_from_dp1;
    }

    int result = dp[robotsSize - 1][0] > dp[robotsSize - 1][1] ? dp[robotsSize - 1][0] : dp[robotsSize - 1][1];

    free(sorted_robots);
    free(dp);
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
    public int MaxWalls(int[] robots, int[] distance, int[] walls) {
        int n = robots.Length;
        var sortedRobots = new (long pos, long dist)[n];
        for (int i = 0; i < n; i++) {
            sortedRobots[i] = (robots[i], distance[i]);
        }
        Array.Sort(sortedRobots, (a, b) => a.pos.CompareTo(b.pos));
        Array.Sort(walls);

        int[,] dp = new int[n, 2];

        long b0_r = (n == 1) ? (sortedRobots[0].pos + sortedRobots[0].dist) : Math.Min(sortedRobots[0].pos + sortedRobots[0].dist, sortedRobots[1].pos);
        dp[0, 0] = CountInRange(walls, sortedRobots[0].pos - sortedRobots[0].dist, sortedRobots[0].pos);
        dp[0, 1] = CountInRange(walls, sortedRobots[0].pos, b0_r);

        for (int i = 1; i < n; i++) {
            long b_prev_r = Math.Min(sortedRobots[i - 1].pos + sortedRobots[i - 1].dist, sortedRobots[i].pos);
            long b_i_l = Math.Max(sortedRobots[i].pos - sortedRobots[i].dist, sortedRobots[i - 1].pos);
            long b_i_r = (i == n - 1) ? (sortedRobots[i].pos + sortedRobots[i].dist) : Math.Min(sortedRobots[i].pos + sortedRobots[i].dist, sortedRobots[i + 1].pos);

            long prev_r_pos = sortedRobots[i - 1].pos;
            long curr_r_pos = sortedRobots[i].pos;

            dp[i, 0] = Math.Max(
                dp[i - 1, 0] + CountInRange(walls, Math.Max(b_i_l, prev_r_pos + 1), curr_r_pos),
                dp[i - 1, 1] + CountInRange(walls, Math.Max(b_i_l, b_prev_r + 1), curr_r_pos)
            );

            dp[i, 1] = Math.Max(
                dp[i - 1, 0] + CountInRange(walls, curr_r_pos, b_i_r),
                dp[i - 1, 1] + CountInRange(walls, Math.Max(curr_r_pos, b_prev_r + 1), b_i_r)
            );
        }

        return Math.Max(dp[n - 1, 0], dp[n - 1, 1]);
    }

    private int CountInRange(int[] walls, long a, long b) {
        if (a > b) return 0;
        int start = Array.BinarySearch(walls, (int)a);
        if (start < 0) start = ~start;
        int end = Array.BinarySearch(walls, (int)b);
        if (end < 0) end = ~end - 1;
        if (start <= end) return end - start + 1;
        return 0;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} robots
 * @param {number[]} distance
 * @param {number[]} walls
 * @return {number}
 */
var maxWalls = function(robots, distance, walls) {
    const n = robots.length;
    const indices = new Int32Array(n);
    for (let i = 0; i < n; i++) indices[i] = i;
    indices.sort((a, b) => robots[a] - robots[b]);

    const sortedWalls = new Int32Array(walls);
    sortedWalls.sort();

    function lowerBound(arr, val) {
        let low = 0, high = arr.length;
        while (low < high) {
            let mid = (low + high) >>> 1;
            if (arr[mid] >= val) high = mid;
            else low = mid + 1;
        }
        return low;
    }

    function upperBound(arr, val) {
        let low = 0, high = arr.length;
        while (low < high) {
            let mid = (low + high) >>> 1;
            if (arr[mid] > val) high = mid;
            else low = mid + 1;
        }
        return low;
    }

    function countInRange(a, b) {
        if (a > b) return 0;
        return upperBound(sortedWalls, b) - lowerBound(sortedWalls, a);
    }

    const dp0 = new Int32Array(n);
    const dp1 = new Int32Array(n);

    const r0_pos = robots[indices[0]];
    const r0_dist = distance[indices[0]];
    const b0_r = (n === 1) ? (r0_pos + r0_dist) : Math.min(r0_pos + r0_dist, robots[indices[1]]);

    dp0[0] = countInRange(r0_pos - r0_dist, r0_pos);
    dp1[0] = countInRange(r0_pos, b0_r);

    for (let i = 1; i < n; i++) {
        const idx = indices[i];
        const prevIdx = indices[i - 1];
        const r_pos = robots[idx];
        const r_dist = distance[idx];
        const prev_pos = robots[prevIdx];
        const prev_dist = distance[prevIdx];

        const b_prev_r = Math.min(prev_pos + prev_dist, r_pos);
        const b_i_l = Math.max(r_pos - r_dist, prev_pos);
        const b_i_r = (i === n - 1) ? (r_pos + r_dist) : Math.min(r_pos + r_dist, robots[indices[i + 1]]);

        dp0[i] = Math.max(
            dp0[i - 1] + countInRange(Math.max(b_i_l, prev_pos + 1), r_pos),
            dp1[i - 1] + countInRange(Math.max(b_i_l, b_prev_r + 1), r_pos)
        );

        dp1[i] = Math.max(
            dp0[i - 1] + countInRange(r_pos, b_i_r),
            dp1[i - 1] + countInRange(Math.max(r_pos, b_prev_r + 1), b_i_r)
        );
    }

    return Math.max(dp0[n - 1], dp1[n - 1]);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxWalls(robots: number[], distance: number[], walls: number[]): number {
    const n = robots.length;
    const combined = robots.map((p, i) => ({ p, d: distance[i] }));
    combined.sort((a, b) => a.p - b.p);
    const P = combined.map(c => c.p);
    const D = combined.map(c => c.d);
    walls.sort((a, b) => a - b);

    const lowerBound = (target: number) => {
        let l = 0, r = walls.length;
        while (l < r) {
            let m = (l + r) >> 1;
            if (walls[m] < target) l = m + 1;
            else r = m;
        }
        return l;
    };

    const upperBound = (target: number) => {
        let l = 0, r = walls.length;
        while (l < r) {
            let m = (l + r) >> 1;
            if (walls[m] <= target) l = m + 1;
            else r = m;
        }
        return l;
    };

    const countWalls = (a: number, b: number) => {
        if (a > b) return 0;
        return upperBound(b) - lowerBound(a);
    };

    const hasWall = (pos: number) => {
        const idx = lowerBound(pos);
        return (idx < walls.length && walls[idx] === pos) ? 1 : 0;
    };

    const lBoundaries = new Int32Array(n);
    const rBoundaries = new Int32Array(n);
    for (let i = 0; i < n; i++) {
        lBoundaries[i] = Math.max(P[i] - D[i], i > 0 ? P[i - 1] : -2000000000);
        rBoundaries[i] = Math.min(P[i] + D[i], i < n - 1 ? P[i + 1] : 2000000000);
    }

    const dp = new Int32Array(n * 2);
    dp[0] = countWalls(lBoundaries[0], P[0]);
    dp[1] = countWalls(P[0], rBoundaries[0]);

    for (let i = 1; i < n; i++) {
        const val1 = dp[(i - 1) * 2] + countWalls(lBoundaries[i], P[i]) - (lBoundaries[i] === P[i - 1] ? hasWall(P[i - 1]) : 0);
        const val2 = dp[(i - 1) * 2 + 1] + countWalls(lBoundaries[i], P[i]) - countWalls(lBoundaries[i], rBoundaries[i - 1]);
        dp[i * 2] = Math.max(val1, val2);

        const val3 = dp[(i - 1) * 2] + countWalls(P[i], rBoundaries[i]);
        const val4 = dp[(i - 1) * 2 + 1] + countWalls(P[i], rBoundaries[i]) - (rBoundaries[i - 1] === P[i] ? hasWall(P[i]) : 0);
        dp[i * 2 + 1] = Math.max(val3, val4);
    }

    return Math.max(dp[(n - 1) * 2], dp[(n - 1) * 2 + 1]);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $robots
     * @param Integer[] $distance
     * @param Integer[] $walls
     * @return Integer
     */
    function maxWalls($robots, $distance, $walls) {
        $n = count($robots);
        array_multisort($robots, SORT_ASC, $distance);
        sort($walls);

        $lBoundaries = array_fill(0, $n, 0);
        $rBoundaries = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $lBoundaries[$i] = max($robots[$i] - $distance[$i], $i > 0 ? $robots[$i - 1] : -2000000000);
            $rBoundaries[$i] = min($robots[$i] + $distance[$i], $i < $n - 1 ? $robots[$i + 1] : 2000000000);
        }

        $lowerBound = function($target) use (&$walls) {
            $l = 0; $r = count($walls);
            while ($l < $r) {
                $m = (int)(($l + $r) / 2);
                if ($walls[$m] < $target) $l = $m + 1;
                else $r = $m;
            }
            return $l;
        };

        $upperBound = function($target) use (&$walls) {
            $l = 0; $r = count($walls);
            while ($l < $r) {
                $m = (int)(($l + $r) / 2);
                if ($walls[$m] <= $target) $l = $m + 1;
                else $r = $m;
            }
            return $l;
        };

        $countWalls = function($a, $b) use ($lowerBound, $upperBound) {
            if ($a > $b) return 0;
            return $upperBound($b) - $lowerBound($a);
        };

        $hasWall = function($pos) use ($lowerBound, &$walls) {
            $idx = $lowerBound($pos);
            return ($idx < count($walls) && $walls[$idx] == $pos) ? 1 : 0;
        };

        $dp = array_fill(0, $n * 2, 0);
        $dp[0] = $countWalls($lBoundaries[0], $robots[0]);
        $dp[1] = $countWalls($robots[0], $rBoundaries[0]);

        for ($i = 1; $i < $n; $i++) {
            $val1 = $dp[($i - 1) * 2] + $countWalls($lBoundaries[$i], $robots[$i]) - ($lBoundaries[$i] == $robots[$i - 1] ? $hasWall($robots[$i - 1]) : 0);
            $val2 = $dp[($i - 1) * 2 + 1] + $countWalls($lBoundaries[$i], $robots[$i]) - $countWalls($lBoundaries[$i], $rBoundaries[$i - 1]);
            $dp[$i * 2] = max($val1, $val2);

            $val3 = $dp[($i - 1) * 2] + $countWalls($robots[$i], $rBoundaries[$i]);
            $val4 = $dp[($i - 1) * 2 + 1] + $countWalls($robots[$i], $rBoundaries[$i]) - ($rBoundaries[$i - 1] == $robots[$i] ? $hasWall($robots[$i]) : 0);
            $dp[$i * 2 + 1] = max($val3, $val4);
        }

        return max($dp[($n - 1) * 2], $dp[($n - 1) * 2 + 1]);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxWalls(_ robots: [Int], _ distance: [Int], _ walls: [Int]) -> Int {
        let n = robots.count
        let sortedIndices = (0..<n).sorted { robots[$0] < robots[$1] }
        let sortedRobots = sortedIndices.map { robots[$0] }
        let sortedDistances = sortedIndices.map { distance[$0] }
        let sortedWalls = walls.sorted()

        func lowerBound(_ arr: [Int], _ target: Int) -> Int {
            var l = 0, r = arr.count
            while l < r {
                let m = l + (r - l) / 2
                if arr[m] < target { l = m + 1 } else { r = m }
            }
            return l
        }

        func upperBound(_ arr: [Int], _ target: Int) -> Int {
            var l = 0, r = arr.count
            while l < r {
                let m = l + (r - l) / 2
                if arr[m] <= target { l = m + 1 } else { r = m }
            }
            return l
        }

        func countWalls(_ a: Int, _ b: Int) -> Int {
            if a > b { return 0 }
            return upperBound(sortedWalls, b) - lowerBound(sortedWalls, a)
        }

        func hasWall(_ pos: Int) -> Int {
            let idx = lowerBound(sortedWalls, pos)
            return (idx < sortedWalls.count && sortedWalls[idx] == pos) ? 1 : 0
        }

        var lBoundaries = [Int](repeating: 0, count: n)
        var rBoundaries = [Int](repeating: 0, count: n)
        for i in 0..<n {
            lBoundaries[i] = max(sortedRobots[i] - sortedDistances[i], i > 0 ? sortedRobots[i - 1] : -2000000000)
            rBoundaries[i] = min(sortedRobots[i] + sortedDistances[i], i < n - 1 ? sortedRobots[i + 1] : 2000000000)
        }

        var dp = [Int](repeating: 0, count: n * 2)
        dp[0] = countWalls(lBoundaries[0], sortedRobots[0])
        dp[1] = countWalls(sortedRobots[0], rBoundaries[0])

        if n > 1 {
            for i in 1..<n {
                let val1 = dp[(i - 1) * 2] + countWalls(lBoundaries[i], sortedRobots[i]) - (lBoundaries[i] == sortedRobots[i - 1] ? hasWall(sortedRobots[i - 1]) : 0)
                let val2 = dp[(i - 1) * 2 + 1] + countWalls(lBoundaries[i], sortedRobots[i]) - countWalls(lBoundaries[i], rBoundaries[i - 1])
                dp[i * 2] = max(val1, val2)

                let val3 = dp[(i - 1) * 2] + countWalls(sortedRobots[i], rBoundaries[i])
                let val4 = dp[(i - 1) * 2 + 1] + countWalls(sortedRobots[i], rBoundaries[i]) - (rBoundaries[i - 1] == sortedRobots[i] ? hasWall(sortedRobots[i]) : 0)
                dp[i * 2 + 1] = max(val3, val4)
            }
        }

        return max(dp[(n - 1) * 2], dp[(n - 1) * 2 + 1])
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxWalls(robots: IntArray, distance: IntArray, walls: IntArray): Int {
        val n = robots.size
        data class Robot(val pos: Int, val dist: Int)
        val rbs = Array(n) { i -> Robot(robots[i], distance[i]) }.sortedBy { it.pos }
        walls.sort()

        fun count(a: Int, b: Int): Int {
            if (a > b) return 0
            var idxA = walls.binarySearch(a)
            if (idxA < 0) idxA = -idxA - 1
            var idxB = walls.binarySearch(b)
            if (idxB < 0) idxB = -idxB - 1 else idxB += 1
            return idxB - idxA
        }

        val dp = Array(n) { IntArray(2) }
        var prevPos = -1000000000
        for (i in 0 until n) {
            val nextPos = if (i < n - 1) rbs[i + 1].pos else 2000000000
            val li = maxOf(rbs[i].pos - rbs[i].dist, prevPos)
            val ri = minOf(rbs[i].pos + rbs[i].dist, nextPos)

            if (i == 0) {
                dp[0][0] = count(li, rbs[0].pos)
                dp[0][1] = count(rbs[0].pos, ri)
            } else {
                val riPrev = minOf(rbs[i - 1].pos + rbs[i - 1].dist, rbs[i].pos)

                dp[i][0] = maxOf(
                    dp[i - 1][0] + count(li, rbs[i].pos) - count(li, rbs[i - 1].pos),
                    dp[i - 1][1] + count(li, rbs[i].pos) - count(li, riPrev)
                )
                dp[i][1] = maxOf(
                    dp[i - 1][0] + count(rbs[i].pos, ri),
                    dp[i - 1][1] + count(rbs[i].pos, ri) - count(rbs[i].pos, riPrev)
                )
            }
            prevPos = rbs[i].pos
        }

        return maxOf(dp[n - 1][0], dp[n - 1][1])
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maxWalls(List<int> robots, List<int> distance, List<int> walls) {
    int n = robots.length;
    List<Robot> rbs = List.generate(n, (i) => Robot(robots[i], distance[i]));
    rbs.sort((a, b) => a.pos.compareTo(b.pos));
    walls.sort();

    int lowerBound(List<int> sortedList, int value) {
      int low = 0, high = sortedList.length;
      while (low < high) {
        int mid = low + ((high - low) >> 1);
        if (sortedList[mid] < value) low = mid + 1;
        else high = mid;
      }
      return low;
    }

    int upperBound(List<int> sortedList, int value) {
      int low = 0, high = sortedList.length;
      while (low < high) {
        int mid = low + ((high - low) >> 1);
        if (sortedList[mid] <= value) low = mid + 1;
        else high = mid;
      }
      return low;
    }

    int count(int a, int b) {
      if (a > b) return 0;
      return upperBound(walls, b) - lowerBound(walls, a);
    }

    List<List<int>> dp = List.generate(n, (_) => List.filled(2, 0));
    int prevPos = -1000000000;

    for (int i = 0; i < n; i++) {
      int nextPos = (i < n - 1) ? rbs[i + 1].pos : 2000000000;
      int li = (rbs[i].pos - rbs[i].dist > prevPos) ? rbs[i].pos - rbs[i].dist : prevPos;
      int ri = (rbs[i].pos + rbs[i].dist < nextPos) ? rbs[i].pos + rbs[i].dist : nextPos;

      if (i == 0) {
        dp[0][0] = count(li, rbs[0].pos);
        dp[0][1] = count(rbs[0].pos, ri);
      } else {
        int riPrev = (rbs[i - 1].pos + rbs[i - 1].dist < rbs[i].pos) ? rbs[i - 1].pos + rbs[i - 1].dist : rbs[i].pos;

        int c1 = dp[i - 1][0] + count(li, rbs[i].pos) - count(li, rbs[i - 1].pos);
        int c2 = dp[i - 1][1] + count(li, rbs[i].pos) - count(li, riPrev);
        dp[i][0] = (c1 > c2) ? c1 : c2;

        int c3 = dp[i - 1][0] + count(rbs[i].pos, ri);
        int c4 = dp[i - 1][1] + count(rbs[i].pos, ri) - count(rbs[i].pos, riPrev);
        dp[i][1] = (c3 > c4) ? c3 : c4;
      }
      prevPos = rbs[i].pos;
    }

    return (dp[n - 1][0] > dp[n - 1][1]) ? dp[n - 1][0] : dp[n - 1][1];
  }
}

class Robot {
  final int pos;
  final int dist;
  Robot(this.pos, this.dist);
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

type Robot struct {
    pos  int
    dist int
}

func maxWalls(robots []int, distance []int, walls []int) int {
    n := len(robots)
    rbs := make([]Robot, n)
    for i := range robots {
        rbs[i] = Robot{robots[i], distance[i]}
    }
    sort.Slice(rbs, func(i, j int) bool { return rbs[i].pos < rbs[j].pos })
    sort.Ints(walls)

    count := func(a, b int) int {
        if a > b {
            return 0
        }
        idxA := sort.SearchInts(walls, a)
        idxB := sort.SearchInts(walls, b+1)
        return idxB - idxA
    }

    maxVal := func(a, b int) int {
        if a > b { return a }
        return b
    }
    minVal := func(a, b int) int {
        if a < b { return a }
        return b
    }

    dp := make([][2]int, n)
    prevPos := -1000000000

    for i := 0; i < n; i++ {
        nextPos := 2000000000
        if i < n-1 {
            nextPos = rbs[i+1].pos
        }

        li := maxVal(rbs[i].pos - rbs[i].dist, prevPos)
        ri := minVal(rbs[i].pos + rbs[i].dist, nextPos)

        if i == 0 {
            dp[0][0] = count(li, rbs[0].pos)
            dp[0][1] = count(rbs[0].pos, ri)
        } else {
            riPrev := minVal(rbs[i-1].pos + rbs[i-1].dist, rbs[i].pos)

            dp[i][0] = maxVal(
                dp[i-1][0] + count(li, rbs[i].pos) - count(li, rbs[i-1].pos),
                dp[i-1][1] + count(li, rbs[i].pos) - count(li, riPrev),
            )
            dp[i][1] = maxVal(
                dp[i-1][0] + count(rbs[i].pos, ri),
                dp[i-1][1] + count(rbs[i].pos, ri) - count(rbs[i].pos, riPrev),
            )
        }
        prevPos = rbs[i].pos
    }

    return maxVal(dp[n-1][0], dp[n-1][1])
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def max_walls(robots, distance, walls)
  n = robots.size
  combined = robots.zip(distance).sort_by { |r, d| r }
  r = combined.map { |x| x[0] }
  d = combined.map { |x| x[1] }
  walls.sort!
  n_walls = walls.size

  count = ->(a, b) {
    return 0 if a > b
    idx1 = walls.bsearch_index { |x| x >= a } || n_walls
    idx2 = walls.bsearch_index { |x| x > b } || n_walls
    idx2 - idx1
  }

  dp = Array.new(n) { [0, 0] }
  dp[0][0] = count.call([r[0] - d[0], -2000000000].max, r[0])
  dp[0][1] = count.call(r[0], [r[0] + d[0], (n > 1 ? r[1] : 2000000000)].min)

  (1...n).each do |i|
    ri = r[i]
    di = d[i]
    ri_prev = r[i - 1]
    di_prev = d[i - 1]
    ri_next = (i + 1 < n) ? r[i + 1] : 2000000000

    l_range_start = [ri - di, ri_prev].max
    l_range_end = ri
    r_range_start = ri
    r_range_end = [ri + di, ri_next].min

    c_li = count.call(l_range_start, l_range_end)
    c_ri = count.call(r_range_start, r_range_end)

    wall_at_ri_prev = count.call(ri_prev, ri_prev)
    wall_at_ri = count.call(ri, ri)

    overlap_start = [ri_prev, ri - di].max
    overlap_end = [ri_prev + di_prev, ri].min
    c_overlap = count.call(overlap_start, overlap_end)

    dp[i][0] = [
      dp[i - 1][0] + c_li - (ri - di <= ri_prev ? wall_at_ri_prev : 0),
      dp[i - 1][1] + c_li - c_overlap
    ].max

    dp[i][1] = [
      dp[i - 1][0] + c_ri,
      dp[i - 1][1] + c_ri - (ri_prev + di_prev >= ri ? wall_at_ri : 0)
    ].max
  end

  [dp[n - 1][0], dp[n - 1][1]].max
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def maxWalls(robots: Array[Int], distance: Array[Int], walls: Array[Int]): Int = {
    val n = robots.length
    val combined = robots.zip(distance).sortBy(_._1)
    val r = combined.map(_._1)
    val d = combined.map(_._2)
    val sortedWalls = walls.sorted

    def partitionPoint(arr: Array[Int], p: Int => Boolean): Int = {
      var low = 0
      var high = arr.length
      while (low < high) {
        val mid = low + (high - low) / 2
        if (p(arr(mid))) low = mid + 1
        else high = mid
      }
      low
    }

    def count(a: Int, b: Int): Int = {
      if (a > b) 0
      else {
        val idx1 = partitionPoint(sortedWalls, (x: Int) => x < a)
        val idx2 = partitionPoint(sortedWalls, (x: Int) => x <= b)
        idx2 - idx1
      }
    }

    val dp = Array.ofDim[Int](n, 2)
    dp(0)(0) = count(math.max(r(0) - d(0), -2000000000), r(0))
    dp(0)(1) = count(r(0), math.min(r(0) + d(0), if (n > 1) r(1) else 2000000000))

    for (i <- 1 until n) {
      val ri = r(i)
      val di = d(i)
      val riPrev = r(i - 1)
      val diPrev = d(i - 1)
      val riNext = if (i + 1 < n) r(i + 1) else 2000000000

      val lRangeStart = math.max(ri - di, riPrev)
      val lRangeEnd = ri
      val rRangeStart = ri
      val rRangeEnd = math.min(ri + di, riNext)

      val cLi = count(lRangeStart, lRangeEnd)
      val cRi = count(rRangeStart, rRangeEnd)

      val wallAtRiPrev = if (java.util.Arrays.binarySearch(sortedWalls, riPrev) >= 0) 1 else 0
      val wallAtRi = if (java.util.Arrays.binarySearch(sortedWalls, ri) >= 0) 1 else 0

      val overlapStart = math.max(riPrev, ri - di)
      val overlapEnd = math.min(riPrev + diPrev, ri)
      val cOverlap = count(overlapStart, overlapEnd)

      dp(i)(0) = math.max(
        dp(i - 1)(0) + cLi - (if (ri - di <= riPrev) wallAtRiPrev else 0),
        dp(i - 1)(1) + cLi - cOverlap
      )

      dp(i)(1) = math.max(
        dp(i - 1)(0) + cRi,
        dp(i - 1)(1) + cRi - (if (riPrev + diPrev >= ri) wallAtRi else 0)
      )
    }

    math.max(dp(n - 1)(0), dp(n - 1)(1))
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_walls(robots: Vec<i32>, distance: Vec<i32>, walls: Vec<i32>) -> i32 {
        let mut sorted_walls = walls;
        sorted_walls.sort_unstable();
        let mut combined: Vec<(i32, i32)> = robots.into_iter().zip(distance.into_iter()).collect();
        combined.sort_unstable_by_key(|&(pos, _)| pos);
        let r: Vec<i32> = combined.iter().map(|&(pos, _)| pos).collect();
        let d: Vec<i32> = combined.iter().map(|&(_, dist)| dist).collect();
        let n = r.len();

        let count = |a: i32, b: i32| -> i32 {
            if a > b {
                0
            } else {
                let idx1 = sorted_walls.partition_point(|&x| x < a);
                let idx2 = sorted_walls.partition_point(|&x| x <= b);
                (idx2 - idx1) as i32
            }
        };

        let mut dp = vec![[0, 0]; n];

        dp[0][0] = count(r[0].saturating_sub(d[0]).max(-2_000_000_000), r[0]);
        dp[0][1] = count(r[0], r[0].saturating_add(d[0]).min(if n > 1 { r[1] } else { 2_000_000_000 }));

        for i in 1..n {
            let ri = r[i];
            let di = d[i];
            let ri_prev = r[i - 1];
            let di_prev = d[i - 1];
            let ri_next = if i + 1 < n { r[i + 1] } else { 2_000_000_000 };

            let l_range_start = (ri - di).max(ri_prev);
            let l_range_end = ri;
            let r_range_start = ri;
            let r_range_end = (ri + di).min(ri_next);

            let c_li = count(l_range_start, l_range_end);
            let c_ri = count(r_range_start, r_range_end);

            let wall_at_ri_prev = if sorted_walls.binary_search(&ri_prev).is_ok() { 1 } else { 0 };
            let wall_at_ri = if sorted_walls.binary_search(&ri).is_ok() { 1 } else { 0 };

            let overlap_start = ri_prev.max(ri - di);
            let overlap_end = (ri_prev + di_prev).min(ri);
            let c_overlap = count(overlap_start, overlap_end);

            dp[i][0] = (
                dp[i - 1][0] + c_li - if ri - di <= ri_prev { wall_at_ri_prev } else { 0 }
            ).max(
                dp[i - 1][1] + c_li - c_overlap
            );

            dp[i][1] = (
                dp[i - 1][0] + c_ri
            ).max(
                dp[i - 1][1] + c_ri - if ri_prev + di_prev >= ri { wall_at_ri } else { 0 }
            );
        }

        dp[n - 1][0].max(dp[n - 1][1])
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (max-walls robots distance walls)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ([n (length robots)]
         [robots-with-dist (sort (map list robots distance) < #:key car)]
         [robot-positions (list->vector (map car robots-with-dist))]
         [robot-distances (list->vector (map cadr robots-with-dist))]
         [sorted-walls (list->vector (sort walls <))]
         [m (vector-length sorted-walls)])
    (define (lower-bound val)
      (let loop ([low 0] [high m])
        (if (< low high)
            (let ([mid (quotient (+ low high) 2)])
              (if (< (vector-ref sorted-walls mid) val)
                  (loop (+ mid 1) high)
                  (loop low mid)))
            low)))
    (define (upper-bound val)
      (let loop ([low 0] [high m])
        (if (< low high)
            (let ([mid (quotient (+ low high) 2)])
              (if (<= (vector-ref sorted-walls mid) val)
                  (loop (+ mid 1) high)
                  (loop low mid)))
            low)))
    (define (count a b)
      (if (> a b) 0
          (- (upper-bound b) (lower-bound a))))
    (let* ([r0 (vector-ref robot-positions 0)]
           [d0 (vector-ref robot-distances 0)]
           [r1 (if (> n 1) (vector-ref robot-positions 1) 2000000000)]
           [dp0L (count (- r0 d0) r0)]
           [dp0R (count r0 (min r1 (+ r0 d0)))])
      (let loop ([i 1] [prevL dp0L] [prevR dp0R])
        (if (< i n)
            (let* ([r_prev (vector-ref robot-positions (- i 1))]
                   [d_prev (vector-ref robot-distances (- i 1))]
                   [r_curr (vector-ref robot-positions i)]
                   [d_curr (vector-ref robot-distances i)]
                   [r_next (if (< i (- n 1)) (vector-ref robot-positions (+ i 1)) 2000000000)]
                   [new_L_prev_L (- (count (max r_prev (- r_curr d_curr)) r_curr) (count (max r_prev (- r_curr d_curr)) r_prev))]
                   [new_L_prev_R (- (count (max r_prev (- r_curr d_curr)) r_curr) (count (max r_prev (- r_curr d_curr)) (min r_curr (+ r_prev d_prev))))]
                   [dpL (max (+ prevL new_L_prev_L) (+ prevR new_L_prev_R))]
                   [new_R_prev_L (count r_curr (min r_next (+ r_curr d_curr)))]
                   [new_R_prev_R (- (count r_curr (min r_next (+ r_curr d_curr))) (count r_curr (min r_curr (+ r_prev d_prev))))]
                   [dpR (max (+ prevL new_R_prev_L) (+ prevR new_R_prev_R))])
              (loop (+ i 1) dpL dpR))
            (max prevL prevR))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_walls(Robots :: [integer()], Distance :: [integer()], Walls :: [integer()]) -> integer().
max_walls(Robots, Distance, Walls) ->
    SortedWalls = lists:sort(Walls),
    WallsTuple = list_to_tuple(SortedWalls),
    M = tuple_size(WallsTuple),
    SortedRD = lists:sort(lists:zip(Robots, Distance)),
    N = length(SortedRD),
    {RPList, RDList} = lists:unzip(SortedRD),
    RPTuple = list_to_tuple(RPList),
    RDTuple = list_to_tuple(RDList),
    R0 = element(1, RPTuple),
    D0 = element(1, RDTuple),
    R1 = if N > 1 -> element(2, RPTuple); true -> 2000000000 end,
    DP0L = count(WallsTuple, M, R0 - D0, R0),
    DP0R = count(WallsTuple, M, R0, erlang:min(R1, R0 + D0)),
    solve(1, N, RPTuple, RDTuple, WallsTuple, M, DP0L, DP0R).

solve(I, N, RPTuple, RDTuple, WallsTuple, M, PrevL, PrevR) ->
    if I < N ->
        RPrev = element(I, RPTuple),
        DPrev = element(I, RDTuple),
        RCurr = element(I + 1, RPTuple),
        DCurr = element(I + 1, RDTuple),
        RNext = if I + 1 < N -> element(I + 2, RPTuple); true -> 2000000000 end,

        New_L_prev_L = count(WallsTuple, M, erlang:max(RPrev, RCurr - DCurr), RCurr) - count(WallsTuple, M, erlang:max(RPrev, RCurr - DCurr), RPrev),
        New_L_prev_R = count(WallsTuple, M, erlang:max(RPrev, RCurr - DCurr), RCurr) - count(WallsTuple, M, erlang:max(RPrev, RCurr - DCurr), erlang:min(RCurr, RPrev + DPrev)),
        DPCurrL = erlang:max(PrevL + New_L_prev_L, PrevR + New_L_prev_R),

        New_R_prev_L = count(WallsTuple, M, RCurr, erlang:min(RNext, RCurr + DCurr)),
        New_R_prev_R = count(WallsTuple, M, RCurr, erlang:min(RNext, RCurr + DCurr)) - count(WallsTuple, M, RCurr, erlang:min(RCurr, RPrev + DPrev)),
        DPCurrR = erlang:max(PrevL + New_R_prev_L, PrevR + New_R_prev_R),

        solve(I + 1, N, RPTuple, RDTuple, WallsTuple, M, DPCurrL, DPCurrR);
    true ->
        erlang:max(PrevL, PrevR)
    end.

count(Walls, M, A, B) ->
    if A > B -> 0;
    true ->
        upper_bound(Walls, M, B, 0, M) - lower_bound(Walls, M, A, 0, M)
    end.

lower_bound(Tuple, M, Val, Low, High) when Low < High ->
    Mid = (Low + High) div 2,
    case element(Mid + 1, Tuple) < Val of
        true -> lower_bound(Tuple, M, Val, Mid + 1, High);
        false -> lower_bound(Tuple, M, Val, Low, Mid)
    end;
lower_bound(_, _, _, Low, _) -> Low.

upper_bound(Tuple, M, Val, Low, High) when Low < High ->
    Mid = (Low + High) div 2,
    case element(Mid + 1, Tuple) =< Val of
        true -> upper_bound(Tuple, M, Val, Mid + 1, High);
        false -> upper_bound(Tuple, M, Val, Low, Mid)
    end;
upper_bound(_, _, _, Low, _) -> Low.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_walls(robots :: [integer], distance :: [integer], walls :: [integer]) :: integer
  def max_walls(robots, distance, walls) do
    sorted_walls = walls |> Enum.sort() |> List.to_tuple()
    m = tuple_size(sorted_walls)
    sorted_rd = Enum.zip(robots, distance) |> Enum.sort_by(fn {r, _d} -> r end)
    n = length(sorted_rd)
    rp_tuple = sorted_rd |> Enum.map(fn {r, _d} -> r end) |> List.to_tuple()
    rd_tuple = sorted_rd |> Enum.map(fn {_r, d} -> d end) |> List.to_tuple()

    r0 = elem(rp_tuple, 0)
    d0 = elem(rd_tuple, 0)
    r1 = if n > 1, do: elem(rp_tuple, 1), else: 2000000000

    dp0l = count(sorted_walls, m, r0 - d0, r0)
    dp0r = count(sorted_walls, m, r0, min(r1, r0 + d0))

    solve(1, n, rp_tuple, rd_tuple, sorted_walls, m, dp0l, dp0r)
  end

  defp solve(i, n, rp_tuple, rd_tuple, walls, m, prev_l, prev_r) do
    if i < n do
      r_prev = elem(rp_tuple, i - 1)
      d_prev = elem(rd_tuple, i - 1)
      r_curr = elem(rp_tuple, i)
      d_curr = elem(rd_tuple, i)
      r_next = if i + 1 < n, do: elem(rp_tuple, i + 1), else: 2000000000

      new_l_prev_l = count(walls, m, max(r_prev, r_curr - d_curr), r_curr) - count(walls, m, max(r_prev, r_curr - d_curr), r_prev)
      new_l_prev_r = count(walls, m, max(r_prev, r_curr - d_curr), r_curr) - count(walls, m, max(r_prev, r_curr - d_curr), min(r_curr, r_prev + d_prev))
      dp_curr_l = max(prev_l + new_l_prev_l, prev_r + new_l_prev_r)

      new_r_prev_l = count(walls, m, r_curr, min(r_next, r_curr + d_curr))
      new_r_prev_r = count(walls, m, r_curr, min(r_next, r_curr + d_curr)) - count(walls, m, r_curr, min(r_curr, r_prev + d_prev))
      dp_curr_r = max(prev_l + new_r_prev_l, prev_r + new_r_prev_r)

      solve(i + 1, n, rp_tuple, rd_tuple, walls, m, dp_curr_l, dp_curr_r)
    else
      max(prev_l, prev_r)
    end
  end

  defp count(walls, m, a, b) do
    if a > b do
      0
    else
      upper_bound(walls, m, b, 0, m) - lower_bound(walls, m, a, 0, m)
    end
  end

  defp lower_bound(tuple, m, val, low, high) do
    if low < high do
      mid = div(low + high, 2)
      if elem(tuple, mid) < val do
        lower_bound(tuple, m, val, mid + 1, high)
      else
        lower_bound(tuple, m, val, low, mid)
      end
    else
      low
    end
  end

  defp upper_bound(tuple, m, val, low, high) do
    if low < high do
      mid = div(low + high, 2)
      if elem(tuple, mid) <= val do
        upper_bound(tuple, m, val, mid + 1, high)
      else
        upper_bound(tuple, m, val, low, mid)
      end
    else
      low
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O((N + M) \log M + N \log N), where N is the number of robots and M is the number of walls. This accounts for sorting both robots and walls and performing a constant number of binary search range queries for each of the N robots during the dynamic programming phase.
- **Space Complexity:** O(N + M), required to store the sorted robots, walls, and the dynamic programming table of size $N \times 2$.
