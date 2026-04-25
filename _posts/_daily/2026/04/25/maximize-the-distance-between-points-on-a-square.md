---
layout: post
title: "Maximize the Distance Between Points on a Square"
date: 2026-04-25 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Math", "Binary Search", "Geometry", "Sorting"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxDistance(int side, vector<vector<int>>&\
        \ points, int k) {\n        int n = points.size();\n        struct Pt {\n  \
        \          int x, y;\n            long long pos;\n        };\n        vector<Pt>\
        \ pts(n);\n        for (int i = 0; i < n; ++i) {\n            pts[i].x = points[i][0];\n\
        \            pts[i].y = points[i][1];\n            if (pts[i].y == 0) pts[i].pos\
        \ = pts[i].x;\n            else if (pts[i].x == side) pts[i].pos = (long long)side\
        \ + pts[i].y;\n            else if (pts[i].y == side) pts[i].pos = 3LL * side\
        \ - pts[i].x;\n            else pts[i].pos = 4LL * side - pts[i].y;\n      \
        \  }\n\n        sort(pts.begin(), pts.end(), [](const Pt& a, const Pt& b) {\n\
        \            return a.pos < b.pos;\n        });\n\n        vector<Pt> d_pts\
        \ = pts;\n        for (int i = 0; i < n; ++i) {\n            Pt p = pts[i];\n\
        \            p.pos += 4LL * side;\n            d_pts.push_back(p);\n       \
        \ }\n\n        auto get_dist = [&](int i, int j) {\n            return (long\
        \ long)abs(d_pts[i].x - d_pts[j].x) + abs(d_pts[i].y - d_pts[j].y);\n      \
        \  };\n\n        int logK = 0;\n        while ((1 << logK) < k) logK++;\n  \
        \      vector<vector<int>> jump(2 * n, vector<int>(logK));\n\n        auto check\
        \ = [&](int D) {\n            for (int i = 0, j = 0; i < 2 * n; ++i) {\n   \
        \             if (j <= i) j = i + 1;\n                while (j < 2 * n && j\
        \ < i + n && get_dist(i, j) < D) {\n                    j++;\n             \
        \   }\n                jump[i][0] = j;\n            }\n            for (int\
        \ m = 1; m < logK; ++m) {\n                for (int i = 0; i < 2 * n; ++i) {\n\
        \                    if (jump[i][m - 1] < 2 * n) jump[i][m] = jump[jump[i][m\
        \ - 1]][m - 1];\n                    else jump[i][m] = 2 * n;\n            \
        \    }\n            }\n            for (int i = 0; i < n; ++i) {\n         \
        \       int idx = i;\n                for (int m = 0; m < logK; ++m) {\n   \
        \                 if (((k - 1) >> m) & 1) {\n                        idx = jump[idx][m];\n\
        \                        if (idx >= 2 * n) break;\n                    }\n \
        \               }\n                if (idx < i + n && get_dist(idx, i) >= D)\
        \ return true;\n            }\n            return false;\n        };\n\n   \
        \     int low = 1, high = side, ans = 1;\n        while (low <= high) {\n  \
        \          int mid = low + (high - low) / 2;\n            if (check(mid)) {\n\
        \                ans = mid;\n                low = mid + 1;\n            } else\
        \ {\n                high = mid - 1;\n            }\n        }\n        return\
        \ ans;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public int maxDistance(int\
        \ side, int[][] points, int k) {\n        int n = points.length;\n        Point[]\
        \ pts = new Point[n];\n        for (int i = 0; i < n; i++) {\n            long\
        \ pos;\n            int x = points[i][0], y = points[i][1];\n            if\
        \ (y == 0) pos = x;\n            else if (x == side) pos = (long) side + y;\n\
        \            else if (y == side) pos = 3L * side - x;\n            else pos\
        \ = 4L * side - y;\n            pts[i] = new Point(x, y, pos);\n        }\n\n\
        \        Arrays.sort(pts, Comparator.comparingLong(p -> p.pos));\n\n       \
        \ Point[] d_pts = new Point[2 * n];\n        for (int i = 0; i < n; i++) {\n\
        \            d_pts[i] = pts[i];\n            d_pts[i + n] = new Point(pts[i].x,\
        \ pts[i].y, pts[i].pos + 4L * side);\n        }\n\n        int logK = 0;\n \
        \       while ((1 << logK) < k) logK++;\n        int[][] jump = new int[2 *\
        \ n][logK];\n\n        int low = 1, high = side, ans = 1;\n        while (low\
        \ <= high) {\n            int mid = low + (high - low) / 2;\n            if\
        \ (check(mid, n, k, d_pts, jump, logK)) {\n                ans = mid;\n    \
        \            low = mid + 1;\n            } else {\n                high = mid\
        \ - 1;\n            }\n        }\n        return ans;\n    }\n\n    private\
        \ boolean check(int D, int n, int k, Point[] pts, int[][] jump, int logK) {\n\
        \        for (int i = 0, j = 0; i < 2 * n; i++) {\n            if (j <= i) j\
        \ = i + 1;\n            while (j < 2 * n && j < i + n && getDist(pts[i], pts[j])\
        \ < D) {\n                j++;\n            }\n            jump[i][0] = j;\n\
        \        }\n        for (int m = 1; m < logK; m++) {\n            for (int i\
        \ = 0; i < 2 * n; i++) {\n                if (jump[i][m - 1] < 2 * n) jump[i][m]\
        \ = jump[jump[i][m - 1]][m - 1];\n                else jump[i][m] = 2 * n;\n\
        \            }\n        }\n        for (int i = 0; i < n; i++) {\n         \
        \   int idx = i;\n            for (int m = 0; m < logK; m++) {\n           \
        \     if (((k - 1) >> m & 1) == 1) {\n                    idx = jump[idx][m];\n\
        \                    if (idx >= 2 * n) break;\n                }\n         \
        \   }\n            if (idx < i + n && getDist(pts[idx], pts[i]) >= D) return\
        \ true;\n        }\n        return false;\n    }\n\n    private long getDist(Point\
        \ p1, Point p2) {\n        return Math.abs((long) p1.x - p2.x) + Math.abs((long)\
        \ p1.y - p2.y);\n    }\n\n    static class Point {\n        int x, y;\n    \
        \    long pos;\n        Point(int x, int y, long pos) {\n            this.x\
        \ = x;\n            this.y = y;\n            this.pos = pos;\n        }\n  \
        \  }\n}"
      python: "class Solution(object):\n    def maxDistance(self, side, points, k):\n\
        \        \"\"\"\n        :type side: int\n        :type points: List[List[int]]\n\
        \        :type k: int\n        :rtype: int\n        \"\"\"\n        n = len(points)\n\
        \        pts_with_pos = []\n        for x, y in points:\n            if y ==\
        \ 0: pos = x\n            elif x == side: pos = side + y\n            elif y\
        \ == side: pos = 3 * side - x\n            else: pos = 4 * side - y\n      \
        \      pts_with_pos.append((x, y, pos))\n\n        pts_with_pos.sort(key=lambda\
        \ p: p[2])\n        d_pts = pts_with_pos + [(x, y, pos + 4 * side) for x, y,\
        \ pos in pts_with_pos]\n\n        logK = (k - 1).bit_length()\n\n        def\
        \ get_dist(p1, p2):\n            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])\n\
        \n        def check(D):\n            jump = [[2 * n] * logK for _ in range(2\
        \ * n)]\n            j = 0\n            for i in range(2 * n):\n           \
        \     if j <= i: j = i + 1\n                while j < 2 * n and j < i + n and\
        \ get_dist(d_pts[i], d_pts[j]) < D:\n                    j += 1\n          \
        \      jump[i][0] = j\n\n            for m in range(1, logK):\n            \
        \    for i in range(2 * n):\n                    prev = jump[i][m-1]\n     \
        \               if prev < 2 * n:\n                        jump[i][m] = jump[prev][m-1]\n\
        \                    else:\n                        jump[i][m] = 2 * n\n\n \
        \           for i in range(n):\n                idx = i\n                for\
        \ m in range(logK):\n                    if ((k - 1) >> m) & 1:\n          \
        \              idx = jump[idx][m]\n                        if idx >= 2 * n:\
        \ break\n                if idx < i + n and get_dist(d_pts[idx], d_pts[i]) >=\
        \ D:\n                    return True\n            return False\n\n        low,\
        \ high, ans = 1, side, 1\n        while low <= high:\n            mid = (low\
        \ + high) // 2\n            if check(mid):\n                ans = mid\n    \
        \            low = mid + 1\n            else:\n                high = mid -\
        \ 1\n        return ans"
      python3: "class Solution:\n    def maxDistance(self, side: int, points: list[list[int]],\
        \ k: int) -> int:\n        d = []\n        for x, y in points:\n           \
        \ if y == 0:\n                d.append(x)\n            elif x == side:\n   \
        \             d.append(side + y)\n            elif y == side:\n            \
        \    d.append(2 * side + (side - x))\n            else:\n                d.append(3\
        \ * side + (side - y))\n        d.sort()\n        n = len(d)\n        perimeter\
        \ = 4 * side\n        d_ext = d + [x + perimeter for x in d]\n\n        def\
        \ check(D):\n            if D == 0:\n                return True\n         \
        \   nxt = [2 * n] * (2 * n)\n            r = 0\n            for l in range(2\
        \ * n):\n                while r < 2 * n and d_ext[r] - d_ext[l] < D:\n    \
        \                r += 1\n                nxt[l] = r\n\n            limit = d[0]\
        \ + perimeter // k\n            for i in range(n):\n                if d[i]\
        \ > limit:\n                    break\n                curr = i\n          \
        \      possible = True\n                for _ in range(k - 1):\n           \
        \         curr = nxt[curr]\n                    if curr >= 2 * n:\n        \
        \                possible = False\n                        break\n         \
        \       if possible and curr < i + n and (d_ext[i] + perimeter - d_ext[curr])\
        \ >= D:\n                    return True\n            return False\n\n     \
        \   low = 1\n        high = side\n        ans = 0\n        while low <= high:\n\
        \            mid = (low + high) // 2\n            if check(mid):\n         \
        \       ans = mid\n                low = mid + 1\n            else:\n      \
        \          high = mid - 1\n        return ans"
      c: "#include <stdlib.h>\n\nint compareLong(const void* a, const void* b) {\n \
        \   long long arg1 = *(const long long*)a;\n    long long arg2 = *(const long\
        \ long*)b;\n    if (arg1 < arg2) return -1;\n    if (arg1 > arg2) return 1;\n\
        \    return 0;\n}\n\nint check(int D, int n, long long* d_ext, int* nxt, int\
        \ k, long long perimeter) {\n    if (D == 0) return 1;\n    int r = 0;\n   \
        \ for (int l = 0; l < 2 * n; l++) {\n        while (r < 2 * n && d_ext[r] -\
        \ d_ext[l] < D) {\n            r++;\n        }\n        nxt[l] = r;\n    }\n\
        \    long long limit = d_ext[0] + perimeter / k;\n    for (int i = 0; i < n;\
        \ i++) {\n        if (d_ext[i] > limit) break;\n        int curr = i;\n    \
        \    int possible = 1;\n        for (int j = 0; j < k - 1; j++) {\n        \
        \    curr = nxt[curr];\n            if (curr >= 2 * n) {\n                possible\
        \ = 0;\n                break;\n            }\n        }\n        if (possible\
        \ && curr < i + n && (d_ext[i] + perimeter - d_ext[curr]) >= D) {\n        \
        \    return 1;\n        }\n    }\n    return 0;\n}\n\nint maxDistance(int side,\
        \ int** points, int pointsSize, int* pointsColSize, int k) {\n    long long*\
        \ d = (long long*)malloc(pointsSize * sizeof(long long));\n    for (int i =\
        \ 0; i < pointsSize; i++) {\n        long long x = points[i][0];\n        long\
        \ long y = points[i][1];\n        if (y == 0) d[i] = x;\n        else if (x\
        \ == side) d[i] = (long long)side + y;\n        else if (y == side) d[i] = 2LL\
        \ * side + (side - x);\n        else d[i] = 3LL * side + (side - y);\n    }\n\
        \    qsort(d, pointsSize, sizeof(long long), compareLong);\n\n    int n = pointsSize;\n\
        \    long long perimeter = 4LL * side;\n    long long* d_ext = (long long*)malloc(2\
        \ * n * sizeof(long long));\n    for (int i = 0; i < n; i++) {\n        d_ext[i]\
        \ = d[i];\n        d_ext[i + n] = d[i] + perimeter;\n    }\n\n    int* nxt =\
        \ (int*)malloc(2 * n * sizeof(int));\n    int low = 1, high = side, ans = 0;\n\
        \    while (low <= high) {\n        int mid = low + (high - low) / 2;\n    \
        \    if (check(mid, n, d_ext, nxt, k, perimeter)) {\n            ans = mid;\n\
        \            low = mid + 1;\n        } else {\n            high = mid - 1;\n\
        \        }\n    }\n\n    free(d);\n    free(d_ext);\n    free(nxt);\n    return\
        \ ans;\n}"
      csharp: "public class Solution {\n    public int MaxDistance(int side, int[][]\
        \ points, int k) {\n        int n = points.Length;\n        long[] d = new long[n];\n\
        \        long perimeter = 4L * side;\n\n        for (int i = 0; i < n; i++)\
        \ {\n            long x = points[i][0];\n            long y = points[i][1];\n\
        \            if (y == 0) d[i] = x;\n            else if (x == side) d[i] = (long)side\
        \ + y;\n            else if (y == side) d[i] = 2L * side + (side - x);\n   \
        \         else d[i] = 3L * side + (side - y);\n        }\n\n        Array.Sort(d);\n\
        \n        long[] d_ext = new long[2 * n];\n        for (int i = 0; i < n; i++)\
        \ {\n            d_ext[i] = d[i];\n            d_ext[i + n] = d[i] + perimeter;\n\
        \        }\n\n        int[] nxt = new int[2 * n];\n        int low = 1, high\
        \ = side, ans = 0;\n\n        while (low <= high) {\n            int mid = low\
        \ + (high - low) / 2;\n            if (Check(mid, n, d_ext, nxt, k, perimeter))\
        \ {\n                ans = mid;\n                low = mid + 1;\n          \
        \  } else {\n                high = mid - 1;\n            }\n        }\n\n \
        \       return ans;\n    }\n\n    private bool Check(int D, int n, long[] d_ext,\
        \ int[] nxt, int k, long perimeter) {\n        if (D == 0) return true;\n  \
        \      int r = 0;\n        for (int l = 0; l < 2 * n; l++) {\n            while\
        \ (r < 2 * n && d_ext[r] - d_ext[l] < D) {\n                r++;\n         \
        \   }\n            nxt[l] = r;\n        }\n\n        long limit = d_ext[0] +\
        \ perimeter / k;\n        for (int i = 0; i < n; i++) {\n            if (d_ext[i]\
        \ > limit) break;\n            int curr = i;\n            bool possible = true;\n\
        \            for (int j = 0; j < k - 1; j++) {\n                curr = nxt[curr];\n\
        \                if (curr >= 2 * n) {\n                    possible = false;\n\
        \                    break;\n                }\n            }\n            if\
        \ (possible && curr < i + n && (d_ext[i] + perimeter - d_ext[curr]) >= (long)D)\
        \ {\n                return true;\n            }\n        }\n        return\
        \ false;\n    }\n}"
      javascript: "/**\n * @param {number} side\n * @param {number[][]} points\n * @param\
        \ {number} k\n * @return {number}\n */\nvar maxDistance = function(side, points,\
        \ k) {\n    let n = points.length;\n    let d = new Float64Array(n);\n    let\
        \ perimeter = 4 * side;\n\n    for (let i = 0; i < n; i++) {\n        let x\
        \ = points[i][0], y = points[i][1];\n        if (y === 0) d[i] = x;\n      \
        \  else if (x === side) d[i] = side + y;\n        else if (y === side) d[i]\
        \ = 2 * side + (side - x);\n        else d[i] = 3 * side + (side - y);\n   \
        \ }\n\n    d.sort();\n\n    let d_ext = new Float64Array(2 * n);\n    for (let\
        \ i = 0; i < n; i++) {\n        d_ext[i] = d[i];\n        d_ext[i + n] = d[i]\
        \ + perimeter;\n    }\n\n    let nxt = new Int32Array(2 * n);\n\n    function\
        \ check(D) {\n        if (D === 0) return true;\n        let r = 0;\n      \
        \  for (let l = 0; l < 2 * n; l++) {\n            while (r < 2 * n && d_ext[r]\
        \ - d_ext[l] < D) {\n                r++;\n            }\n            nxt[l]\
        \ = r;\n        }\n\n        let limit = d_ext[0] + perimeter / k;\n       \
        \ for (let i = 0; i < n; i++) {\n            if (d_ext[i] > limit) break;\n\
        \            let curr = i;\n            let possible = true;\n            for\
        \ (let j = 0; j < k - 1; j++) {\n                curr = nxt[curr];\n       \
        \         if (curr >= 2 * n) {\n                    possible = false;\n    \
        \                break;\n                }\n            }\n            if (possible\
        \ && curr < i + n && (d_ext[i] + perimeter - d_ext[curr]) >= D) {\n        \
        \        return true;\n            }\n        }\n        return false;\n   \
        \ }\n\n    let low = 1, high = side, ans = 0;\n    while (low <= high) {\n \
        \       let mid = Math.floor((low + high) / 2);\n        if (check(mid)) {\n\
        \            ans = mid;\n            low = mid + 1;\n        } else {\n    \
        \        high = mid - 1;\n        }\n    }\n    return ans;\n};"
      typescript: "function maxDistance(side: number, points: number[][], k: number):\
        \ number {\n    const n = points.length;\n    const d: number[] = points.map(([x,\
        \ y]) => {\n        if (x === 0 && y < side) return y;\n        if (y === side\
        \ && x < side) return side + x;\n        if (x === side && y > 0) return 2 *\
        \ side + (side - y);\n        return 3 * side + (side - x);\n    });\n    d.sort((a,\
        \ b) => a - b);\n\n    const dExpanded = new Float64Array(2 * n);\n    for (let\
        \ i = 0; i < n; i++) {\n        dExpanded[i] = d[i];\n        dExpanded[i +\
        \ n] = d[i] + 4 * side;\n    }\n\n    const up = new Int32Array((2 * n + 1)\
        \ * 5);\n    const fullPerimeter = 4 * side;\n\n    const check = (x: number):\
        \ boolean => {\n        let r = 0;\n        for (let l = 0; l <= 2 * n; l++)\
        \ {\n            while (r < 2 * n && dExpanded[r] < dExpanded[l] + x) {\n  \
        \              r++;\n            }\n            up[l * 5 + 0] = r;\n       \
        \ }\n\n        for (let p = 1; p < 5; p++) {\n            for (let i = 0; i\
        \ <= 2 * n; i++) {\n                const mid = up[i * 5 + (p - 1)];\n     \
        \           if (mid < 2 * n) {\n                    up[i * 5 + p] = up[mid *\
        \ 5 + (p - 1)];\n                } else {\n                    up[i * 5 + p]\
        \ = 2 * n;\n                }\n            }\n        }\n\n        for (let\
        \ i = 0; i < n; i++) {\n            let curr = i;\n            for (let p =\
        \ 0; p < 5; p++) {\n                if (((k - 1) >> p) & 1) {\n            \
        \        curr = up[curr * 5 + p];\n                    if (curr >= 2 * n) break;\n\
        \                }\n            }\n            if (curr < 2 * n && dExpanded[curr]\
        \ + x <= d[i] + fullPerimeter) {\n                return true;\n           \
        \ }\n        }\n        return false;\n    };\n\n    let low = 1, high = side,\
        \ ans = 1;\n    while (low <= high) {\n        const mid = Math.floor((low +\
        \ high) / 2);\n        if (check(mid)) {\n            ans = mid;\n         \
        \   low = mid + 1;\n        } else {\n            high = mid - 1;\n        }\n\
        \    }\n    return ans;\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer $side\n     * @param\
        \ Integer[][] $points\n     * @param Integer $k\n     * @return Integer\n  \
        \   */\n    function maxDistance($side, $points, $k) {\n        $n = count($points);\n\
        \        $d = [];\n        $side = (int)$side;\n        foreach ($points as\
        \ $p) {\n            $x = $p[0];\n            $y = $p[1];\n            if ($x\
        \ == 0 && $y < $side) {\n                $d[] = $y;\n            } else if ($y\
        \ == $side && $x < $side) {\n                $d[] = $side + $x;\n          \
        \  } else if ($x == $side && $y > 0) {\n                $d[] = 2 * $side + ($side\
        \ - $y);\n            } else {\n                $d[] = 3 * $side + ($side -\
        \ $x);\n            }\n        }\n        sort($d);\n\n        $dExpanded =\
        \ [];\n        $fullPerimeter = 4 * $side;\n        for ($i = 0; $i < $n; $i++)\
        \ {\n            $dExpanded[$i] = $d[$i];\n            $dExpanded[$i + $n] =\
        \ $d[$i] + $fullPerimeter;\n        }\n\n        $up = array_fill(0, (2 * $n\
        \ + 1) * 5, 2 * $n);\n\n        $check = function($x) use ($n, $k, $d, $dExpanded,\
        \ $fullPerimeter, &$up) {\n            $r = 0;\n            for ($l = 0; $l\
        \ <= 2 * $n; $l++) {\n                while ($r < 2 * $n && $dExpanded[$r] <\
        \ $dExpanded[$l] + $x) {\n                    $r++;\n                }\n   \
        \             $up[$l * 5 + 0] = $r;\n            }\n\n            for ($p =\
        \ 1; $p < 5; $p++) {\n                for ($i = 0; $i <= 2 * $n; $i++) {\n \
        \                   $mid = $up[$i * 5 + ($p - 1)];\n                    if ($mid\
        \ < 2 * $n) {\n                        $up[$i * 5 + $p] = $up[$mid * 5 + ($p\
        \ - 1)];\n                    } else {\n                        $up[$i * 5 +\
        \ $p] = 2 * $n;\n                    }\n                }\n            }\n\n\
        \            for ($i = 0; $i < $n; $i++) {\n                $curr = $i;\n  \
        \              for ($p = 0; $p < 5; $p++) {\n                    if ((($k -\
        \ 1) >> $p) & 1) {\n                        $curr = $up[$curr * 5 + $p];\n \
        \                       if ($curr >= 2 * $n) break;\n                    }\n\
        \                }\n                if ($curr < 2 * $n && $dExpanded[$curr]\
        \ + $x <= $d[$i] + $fullPerimeter) {\n                    return true;\n   \
        \             }\n            }\n            return false;\n        };\n\n  \
        \      $low = 1;\n        $high = $side;\n        $ans = 1;\n        while ($low\
        \ <= $high) {\n            $mid = floor(($low + $high) / 2);\n            if\
        \ ($check($mid)) {\n                $ans = $mid;\n                $low = $mid\
        \ + 1;\n            } else {\n                $high = $mid - 1;\n          \
        \  }\n        }\n        return $ans;\n    }\n}"
      swift: "class Solution {\n    func maxDistance(_ side: Int, _ points: [[Int]],\
        \ _ k: Int) -> Int {\n        let n = points.count\n        let sideL = Int64(side)\n\
        \        var d = [Int64]()\n        for p in points {\n            let x = Int64(p[0])\n\
        \            let y = Int64(p[1])\n            if x == 0 && y < sideL {\n   \
        \             d.append(y)\n            } else if y == sideL && x < sideL {\n\
        \                d.append(sideL + x)\n            } else if x == sideL && y\
        \ > 0 {\n                d.append(2 * sideL + (sideL - y))\n            } else\
        \ {\n                d.append(3 * sideL + (sideL - x))\n            }\n    \
        \    }\n        d.sort()\n\n        let fullPerimeter = 4 * sideL\n        var\
        \ dExpanded = [Int64](repeating: 0, count: 2 * n)\n        for i in 0..<n {\n\
        \            dExpanded[i] = d[i]\n            dExpanded[i + n] = d[i] + fullPerimeter\n\
        \        }\n\n        var up = [Int](repeating: 2 * n, count: (2 * n + 1) *\
        \ 5)\n\n        func check(_ x: Int64) -> Bool {\n            var r = 0\n  \
        \          for l in 0...(2 * n) {\n                while r < 2 * n && dExpanded[r]\
        \ < dExpanded[l] + x {\n                    r += 1\n                }\n    \
        \            up[l * 5 + 0] = r\n            }\n\n            for p in 1..<5\
        \ {\n                for i in 0...(2 * n) {\n                    let mid = up[i\
        \ * 5 + p - 1]\n                    if mid < 2 * n {\n                     \
        \   up[i * 5 + p] = up[mid * 5 + p - 1]\n                    } else {\n    \
        \                    up[i * 5 + p] = 2 * n\n                    }\n        \
        \        }\n            }\n\n            for i in 0..<n {\n                var\
        \ curr = i\n                for p in 0..<5 {\n                    if (((k -\
        \ 1) >> p) & 1) == 1 {\n                        curr = up[curr * 5 + p]\n  \
        \                      if curr >= 2 * n { break }\n                    }\n \
        \               }\n                if curr < 2 * n && dExpanded[curr] + x <=\
        \ d[i] + fullPerimeter {\n                    return true\n                }\n\
        \            }\n            return false\n        }\n\n        var low: Int64\
        \ = 1\n        var high: Int64 = sideL\n        var ans: Int64 = 1\n       \
        \ while low <= high {\n            let mid = (low + high) / 2\n            if\
        \ check(mid) {\n                ans = mid\n                low = mid + 1\n \
        \           } else {\n                high = mid - 1\n            }\n      \
        \  }\n        return Int(ans)\n    }\n}"
      kotlin: "class Solution {\n    fun maxDistance(side: Int, points: Array<IntArray>,\
        \ k: Int): Int {\n        val n = points.size\n        val sideL = side.toLong()\n\
        \        val d = LongArray(n)\n        for (i in points.indices) {\n       \
        \     val x = points[i][0].toLong()\n            val y = points[i][1].toLong()\n\
        \            if (x == 0L && y < sideL) d[i] = y\n            else if (y == sideL\
        \ && x < sideL) d[i] = sideL + x\n            else if (x == sideL && y > 0L)\
        \ d[i] = 2 * sideL + (sideL - y)\n            else d[i] = 3 * sideL + (sideL\
        \ - x)\n        }\n        d.sort()\n\n        val fullPerimeter = 4 * sideL\n\
        \        val dExpanded = LongArray(2 * n)\n        for (i in 0 until n) {\n\
        \            dExpanded[i] = d[i]\n            dExpanded[i + n] = d[i] + fullPerimeter\n\
        \        }\n\n        val up = IntArray((2 * n + 1) * 5) { 2 * n }\n\n     \
        \   fun check(x: Long): Boolean {\n            var r = 0\n            for (l\
        \ in 0..2 * n) {\n                while (r < 2 * n && dExpanded[r] < dExpanded[l]\
        \ + x) {\n                    r++\n                }\n                up[l *\
        \ 5 + 0] = r\n            }\n\n            for (p in 1 until 5) {\n        \
        \        for (i in 0..2 * n) {\n                    val mid = up[i * 5 + (p\
        \ - 1)]\n                    if (mid < 2 * n) {\n                        up[i\
        \ * 5 + p] = up[mid * 5 + (p - 1)]\n                    } else {\n         \
        \               up[i * 5 + p] = 2 * n\n                    }\n             \
        \   }\n            }\n\n            for (i in 0 until n) {\n               \
        \ var curr = i\n                for (p in 0 until 5) {\n                   \
        \ if (((k - 1) shr p) and 1 == 1) {\n                        curr = up[curr\
        \ * 5 + p]\n                        if (curr >= 2 * n) break\n             \
        \       }\n                }\n                if (curr < 2 * n && dExpanded[curr]\
        \ + x <= d[i] + fullPerimeter) {\n                    return true\n        \
        \        }\n            }\n            return false\n        }\n\n        var\
        \ low = 1L\n        var high = sideL\n        var ans = 1L\n        while (low\
        \ <= high) {\n            val mid = (low + high) / 2\n            if (check(mid))\
        \ {\n                ans = mid\n                low = mid + 1\n            }\
        \ else {\n                high = mid - 1\n            }\n        }\n       \
        \ return ans.toInt()\n    }\n}"
      dart: "import 'dart:typed_data';\n\nclass Solution {\n  int getD(int x, int y,\
        \ int side) {\n    if (y == 0) return x;\n    if (x == side) return side + y;\n\
        \    if (y == side) return 3 * side - x;\n    return 4 * side - y;\n  }\n\n\
        \  bool check(int dVal, int n, int k, int side, Int64List d2n) {\n    int perimeter\
        \ = 4 * side;\n    Int32List nextIdx = Int32List(2 * n);\n    int ptr = 0;\n\
        \    for (int i = 0; i < 2 * n; i++) {\n      while (ptr < 2 * n && d2n[ptr]\
        \ < d2n[i] + dVal) {\n        ptr++;\n      }\n      nextIdx[i] = ptr;\n   \
        \ }\n\n    int limit = d2n[0] + (perimeter ~/ k);\n    for (int i = 0; i < n;\
        \ i++) {\n      if (d2n[i] > limit) break;\n      int curr = i;\n      int count\
        \ = 0;\n      while (count < k - 1) {\n        curr = nextIdx[curr];\n     \
        \   if (curr >= 2 * n) break;\n        count++;\n      }\n      if (count ==\
        \ k - 1 && curr < 2 * n && d2n[i] + perimeter >= d2n[curr] + dVal) {\n     \
        \   return true;\n      }\n    }\n    return false;\n  }\n\n  int maxDistance(int\
        \ side, List<List<int>> points, int k) {\n    int n = points.length;\n    List<int>\
        \ dList = points.map((p) => getD(p[0], p[1], side)).toList()..sort();\n    Int64List\
        \ d2n = Int64List(2 * n);\n    int perimeter = 4 * side;\n    for (int i = 0;\
        \ i < n; i++) {\n      d2n[i] = dList[i].toInt();\n      d2n[i + n] = dList[i].toInt()\
        \ + perimeter;\n    }\n\n    int low = 1, high = side;\n    int ans = 1;\n \
        \   while (low <= high) {\n      int mid = low + (high - low) ~/ 2;\n      if\
        \ (check(mid, n, k, side, d2n)) {\n        ans = mid;\n        low = mid + 1;\n\
        \      } else {\n        high = mid - 1;\n      }\n    }\n    return ans;\n\
        \  }\n}"
      go: "func maxDistance(side int, points [][]int, k int) int {\n\tn := len(points)\n\
        \tgetD := func(x, y, side int) int64 {\n\t\tif y == 0 {\n\t\t\treturn int64(x)\n\
        \t\t}\n\t\tif x == side {\n\t\t\treturn int64(side + y)\n\t\t}\n\t\tif y ==\
        \ side {\n\t\t\treturn int64(3*side - x)\n\t\t}\n\t\treturn int64(4*side - y)\n\
        \t}\n\n\td := make([]int64, n)\n\tfor i := 0; i < n; i++ {\n\t\td[i] = getD(points[i][0],\
        \ points[i][1], side)\n\t}\n\timport \"sort\"\n\tsort.Slice(d, func(i, j int)\
        \ bool { return d[i] < d[j] })\n\n\tperimeter := int64(4) * int64(side)\n\t\
        d2n := make([]int64, 2*n)\n\tfor i := 0; i < n; i++ {\n\t\td2n[i] = d[i]\n\t\
        \td2n[i+n] = d[i] + perimeter\n\t}\n\n\tcheck := func(dVal int64) bool {\n\t\
        \tnextIdx := make([]int, 2*n)\n\t\tptr := 0\n\t\tfor i := 0; i < 2*n; i++ {\n\
        \t\t\tfor ptr < 2*n && d2n[ptr] < d2n[i]+dVal {\n\t\t\t\tptr++\n\t\t\t}\n\t\t\
        \tnextIdx[i] = ptr\n\t\t}\n\n\t\tlimit := d2n[0] + perimeter/int64(k)\n\t\t\
        for i := 0; i < n; i++ {\n\t\t\tif d2n[i] > limit {\n\t\t\t\tbreak\n\t\t\t}\n\
        \t\t\tcurr := i\n\t\t\tcount := 0\n\t\t\tfor count < k-1 {\n\t\t\t\tcurr = nextIdx[curr]\n\
        \t\t\t\tif curr >= 2*n {\n\t\t\t\t\tbreak\n\t\t\t\t}\n\t\t\t\tcount++\n\t\t\t\
        }\n\t\t\tif count == k-1 && curr < 2*n && d2n[i]+perimeter >= d2n[curr]+dVal\
        \ {\n\t\t\t\treturn true\n\t\t\t}\n\t\t}\n\t\treturn false\n\t}\n\n\tlow, high\
        \ := int64(1), int64(side)\n\tans := int64(1)\n\tfor low <= high {\n\t\tmid\
        \ := (low + high) / 2\n\t\tif check(mid) {\n\t\t\tans = mid\n\t\t\tlow = mid\
        \ + 1\n\t\t} else {\n\t\t\thigh = mid - 1\n\t\t}\n\t}\n\treturn int(ans)\n}"
      ruby: "def get_d(x, y, side)\n  return x if y == 0\n  return side + y if x ==\
        \ side\n  return 3 * side - x if y == side\n  4 * side - y\nend\n\ndef check(d_2n,\
        \ n, k, perimeter, d_val)\n  next_idx = Array.new(2 * n)\n  ptr = 0\n  i = 0\n\
        \  while i < 2 * n\n    while ptr < 2 * n && d_2n[ptr] < d_2n[i] + d_val\n \
        \     ptr += 1\n    end\n    next_idx[i] = ptr\n    i += 1\n  end\n\n  limit\
        \ = d_2n[0] + (perimeter / k)\n  i = 0\n  while i < n\n    break if d_2n[i]\
        \ > limit\n    curr = i\n    count = 0\n    while count < k - 1\n      curr\
        \ = next_idx[curr]\n      break if curr >= 2 * n\n      count += 1\n    end\n\
        \    if count == k - 1 && curr < 2 * n && d_2n[i] + perimeter >= d_2n[curr]\
        \ + d_val\n      return true\n    end\n    i += 1\n  end\n  false\nend\n\ndef\
        \ max_distance(side, points, k)\n  d = points.map { |p| get_d(p[0], p[1], side)\
        \ }.sort\n  n = d.length\n  perimeter = 4 * side\n  d_2n = d + d.map { |x| x\
        \ + perimeter }\n\n  low = 1\n  high = side\n  ans = 1\n  while low <= high\n\
        \    mid = (low + high) / 2\n    if check(d_2n, n, k, perimeter, mid)\n    \
        \  ans = mid\n      low = mid + 1\n    else\n      high = mid - 1\n    end\n\
        \  end\n  ans\nend"
      scala: "object Solution {\n    def getD(x: Long, y: Long, side: Long): Long =\
        \ {\n        if (y == 0) return x\n        if (x == side) return side + y\n\
        \        if (y == side) return 3 * side - x\n        4 * side - y\n    }\n\n\
        \    def check(d2n: Array[Long], n: Int, k: Int, side: Int, dVal: Int): Boolean\
        \ = {\n        val perimeter = 4L * side\n        val nextIdx = new Array[Int](2\
        \ * n)\n        var ptr = 0\n        var i = 0\n        while (i < 2 * n) {\n\
        \            while (ptr < 2 * n && d2n(ptr) < d2n(i) + dVal) {\n           \
        \     ptr += 1\n            }\n            nextIdx(i) = ptr\n            i +=\
        \ 1\n        }\n\n        val limit = d2n(0) + (perimeter / k)\n        var\
        \ startIdx = 0\n        while (startIdx < n) {\n            if (d2n(startIdx)\
        \ > limit) return false\n            var curr = startIdx\n            var count\
        \ = 0\n            while (count < k - 1) {\n                curr = nextIdx(curr)\n\
        \                if (curr >= 2 * n) {\n                    count = -1 // Break\
        \ surrogate\n                } else {\n                    count += 1\n    \
        \            }\n                if (count == -1 || count == k - 1) {\n     \
        \               // exit early loop\n                }\n            }\n     \
        \       if (count == k - 1 && curr < 2 * n && d2n(startIdx) + perimeter >= d2n(curr)\
        \ + dVal) {\n                return true\n            }\n            startIdx\
        \ += 1\n        }\n        false\n    }\n\n    def maxDistance(side: Int, points:\
        \ Array[Array[Int]], k: Int): Int = {\n        val n = points.length\n     \
        \   val d = points.map(p => getD(p(0).toLong, p(1).toLong, side.toLong)).sorted\n\
        \        val perimeter = 4L * side\n        val d2n = new Array[Long](2 * n)\n\
        \        for (i <- 0 until n) {\n            d2n(i) = d(i)\n            d2n(i\
        \ + n) = d(i) + perimeter\n        }\n\n        var low = 1\n        var high\
        \ = side\n        var ans = 1\n        while (low <= high) {\n            val\
        \ mid = low + (high - low) / 2\n            if (check(d2n, n, k, side, mid))\
        \ {\n                ans = mid\n                low = mid + 1\n            }\
        \ else {\n                high = mid - 1\n            }\n        }\n       \
        \ ans\n    }\n}"
      rust: "impl Solution {\n    pub fn max_distance(side: i32, points: Vec<Vec<i32>>,\
        \ k: i32) -> i32 {\n        let n = points.len();\n        let side_64 = side\
        \ as i64;\n        let mut d = Vec::with_capacity(n);\n        for p in points\
        \ {\n            let x = p[0] as i64;\n            let y = p[1] as i64;\n  \
        \          let coord = if y == 0 && x < side_64 {\n                x\n     \
        \       } else if x == side_64 && y < side_64 {\n                side_64 + y\n\
        \            } else if y == side_64 && x > 0 {\n                2 * side_64\
        \ + (side_64 - x)\n            } else {\n                3 * side_64 + (side_64\
        \ - y)\n            };\n            d.push(coord);\n        }\n        d.sort_unstable();\n\
        \n        let l = 4 * side_64;\n        let mut d2 = vec![0i64; 2 * n];\n  \
        \      for i in 0..n {\n            d2[i] = d[i];\n            d2[i + n] = d[i]\
        \ + l;\n        }\n\n        let mut low = 1;\n        let mut high = side;\n\
        \        let mut ans = 1;\n\n        while low <= high {\n            let mid\
        \ = low + (high - low) / 2;\n            if Self::check(mid as i64, &d2, n,\
        \ k as usize, l) {\n                ans = mid;\n                low = mid +\
        \ 1;\n            } else {\n                high = mid - 1;\n            }\n\
        \        }\n        ans\n    }\n\n    fn check(x: i64, d: &[i64], n: usize,\
        \ k: usize, l: i64) -> bool {\n        let mut next_idx = vec![0usize; 2 * n];\n\
        \        let mut j = 0;\n        for i in 0..2 * n {\n            while j <\
        \ 2 * n && d[j] < d[i] + x {\n                j += 1;\n            }\n     \
        \       next_idx[i] = j;\n        }\n\n        let max_start = next_idx[0].min(n);\n\
        \        for i in 0..max_start {\n            let mut curr = i;\n          \
        \  let mut possible = true;\n            for _ in 0..k - 1 {\n             \
        \   curr = next_idx[curr];\n                if curr >= i + n {\n           \
        \         possible = false;\n                    break;\n                }\n\
        \            }\n            if possible && d[i] + l - d[curr] >= x {\n     \
        \           return true;\n            }\n        }\n        false\n    }\n}"
      racket: "(define/contract (max-distance side points k)\n  (-> exact-integer? (listof\
        \ (listof exact-integer?)) exact-integer? exact-integer?)\n  (let* ([n (length\
        \ points)]\n         [l (* 4 side)]\n         [d-coords (map (lambda (p)\n \
        \                         (let ([x (car p)] [y (cadr p)])\n                \
        \            (cond\n                              [(and (= y 0) (< x side))\
        \ x]\n                              [(and (= x side) (< y side)) (+ side y)]\n\
        \                              [(and (= y side) (> x 0)) (+ (* 2 side) (- side\
        \ x))]\n                              [else (+ (* 3 side) (- side y))]))) \n\
        \                        points)]\n         [d (list->vector (sort d-coords\
        \ <))]\n         [d2 (make-vector (* 2 n))])\n    (for ([i (in-range n)])\n\
        \      (vector-set! d2 i (vector-ref d i))\n      (vector-set! d2 (+ i n) (+\
        \ (vector-ref d i) l)))\n\n    (define (check x)\n      (let ([next-idx (make-vector\
        \ (* 2 n))]\n            [two-n (* 2 n)])\n        (let loop-j ([i 0] [j 0])\n\
        \          (if (< i two-n)\n              (let ([target (+ (vector-ref d2 i)\
        \ x)])\n                (let loop-find-j ([cur-j j])\n                  (if\
        \ (and (< cur-j two-n) (< (vector-ref d2 cur-j) target))\n                 \
        \     (loop-find-j (+ cur-j 1))\n                      (begin\n            \
        \            (vector-set! next-idx i cur-j)\n                        (loop-j\
        \ (+ i 1) cur-j)))))\n              (void)))\n        (let* ([limit-i (min n\
        \ (vector-ref next-idx 0))])\n          (let loop-i ([i 0])\n            (if\
        \ (< i limit-i)\n                (let loop-k ([curr i] [count (- k 1)])\n  \
        \                (if (= count 0)\n                      (if (>= (+ (vector-ref\
        \ d2 i) l (- (vector-ref d2 curr))) x)\n                          #t\n     \
        \                     (loop-i (+ i 1)))\n                      (let ([next (vector-ref\
        \ next-idx curr)])\n                        (if (>= next (+ i n))\n        \
        \                    (loop-i (+ i 1))\n                            (loop-k next\
        \ (- count 1))))))\n                #f)))))\n\n    (let loop-bs ([low 1] [high\
        \ side] [ans 1])\n      (if (<= low high)\n          (let* ([mid (quotient (+\
        \ low high) 2)])\n            (if (check mid)\n                (loop-bs (+ mid\
        \ 1) high mid)\n                (loop-bs low (- mid 1) ans)))\n          ans))))"
      erlang: "-spec max_distance(Side :: integer(), Points :: [[integer()]], K :: integer())\
        \ -> integer().\nmax_distance(Side, Points, K) ->\n    DCoords = lists:map(fun([X,\
        \ Y]) -> \n        if \n            Y == 0, X < Side -> X;\n            X ==\
        \ Side, Y < Side -> Side + Y;\n            Y == Side, X > 0 -> 2 * Side + (Side\
        \ - X);\n            true -> 3 * Side + (Side - Y)\n        end\n    end, Points),\n\
        \    SortedD = lists:sort(DCoords),\n    N = length(SortedD),\n    L = 4 * Side,\n\
        \    DTuple = list_to_tuple(SortedD ++ [X + L || X <- SortedD]),\n    binary_search(1,\
        \ Side, 1, N, K, L, DTuple).\n\nbinary_search(Low, High, Ans, N, K, L, DTuple)\
        \ when Low =< High ->\n    Mid = (Low + High) div 2,\n    case check(Mid, N,\
        \ K, L, DTuple) of\n        true -> binary_search(Mid + 1, High, Mid, N, K,\
        \ L, DTuple);\n        false -> binary_search(Low, Mid - 1, Ans, N, K, L, DTuple)\n\
        \    end;\nbinary_search(_, _, Ans, _, _, _, _) -> Ans.\n\ncheck(X, N, K, L,\
        \ DTuple) ->\n    NextIdxTuple = compute_next_idx(0, 0, 2 * N, X, DTuple, []),\n\
        \    FirstNext = element(1, NextIdxTuple),\n    MaxI = if FirstNext < N -> FirstNext;\
        \ true -> N end,\n    check_all_i(0, MaxI, N, K, L, X, DTuple, NextIdxTuple).\n\
        \ncompute_next_idx(2 * N, _, _, _, _, Acc) -> list_to_tuple(lists:reverse(Acc));\n\
        compute_next_idx(I, J, TwoN, X, DTuple, Acc) ->\n    NewJ = find_j(J, TwoN,\
        \ element(I + 1, DTuple) + X, DTuple),\n    compute_next_idx(I + 1, NewJ, TwoN,\
        \ X, DTuple, [NewJ | Acc]).\n\nfind_j(J, TwoN, Target, DTuple) when J < TwoN\
        \ ->\n    case element(J + 1, DTuple) < Target of\n        true -> find_j(J\
        \ + 1, TwoN, Target, DTuple);\n        false -> J\n    end;\nfind_j(J, _, _,\
        \ _) -> J.\n\ncheck_all_i(I, MaxI, N, K, L, X, DTuple, NextIdxTuple) when I\
        \ < MaxI ->\n    case check_start_i(I, I + N, K - 1, NextIdxTuple) of\n    \
        \    {ok, LastIdx} ->\n            if (element(I + 1, DTuple) + L - element(LastIdx\
        \ + 1, DTuple)) >= X -> true;\n               true -> check_all_i(I + 1, MaxI,\
        \ N, K, L, X, DTuple, NextIdxTuple)\n            end;\n        error -> check_all_i(I\
        \ + 1, MaxI, N, K, L, X, DTuple, NextIdxTuple)\n    end;\ncheck_all_i(_, _,\
        \ _, _, _, _, _, _) -> false.\n\ncheck_start_i(Curr, _Limit, 0, _NextIdxTuple)\
        \ -> {ok, Curr};\ncheck_start_i(Curr, Limit, KLeft, NextIdxTuple) ->\n    Next\
        \ = element(Curr + 1, NextIdxTuple),\n    if Next >= Limit -> error;\n     \
        \  true -> check_start_i(Next, Limit, KLeft - 1, NextIdxTuple)\n    end."
      elixir: "defmodule Solution do\n  @spec max_distance(side :: integer, points ::\
        \ [[integer]], k :: integer) :: integer\n  def max_distance(side, points, k)\
        \ do\n    d_coords = Enum.map(points, fn [x, y] ->\n      cond do\n        y\
        \ == 0 and x < side -> x\n        x == side and y < side -> side + y\n     \
        \   y == side and x > 0 -> 2 * side + (side - x)\n        true -> 3 * side +\
        \ (side - y)\n      end\n    end)\n    sorted_d = Enum.sort(d_coords)\n    n\
        \ = length(sorted_d)\n    l = 4 * side\n    d2 = sorted_d ++ Enum.map(sorted_d,\
        \ &(&1 + l))\n    d_tuple = List.to_tuple(d2)\n\n    binary_search(1, side,\
        \ 1, n, k, l, d_tuple)\n  end\n\n  defp binary_search(low, high, ans, n, k,\
        \ l, d_tuple) when low <= high do\n    mid = div(low + high, 2)\n    if check(mid,\
        \ n, k, l, d_tuple) do\n      binary_search(mid + 1, high, mid, n, k, l, d_tuple)\n\
        \    else\n      binary_search(low, mid - 1, ans, n, k, l, d_tuple)\n    end\n\
        \  end\n  defp binary_search(_low, _high, ans, _n, _k, _l, _d_tuple), do: ans\n\
        \n  defp check(x, n, k, l, d_tuple) do\n    next_idx_tuple = compute_next_idx(0,\
        \ 0, 2 * n, x, d_tuple, [])\n    first_next = elem(next_idx_tuple, 0)\n    max_i\
        \ = min(n, first_next)\n    check_all_i(0, max_i, n, k, l, x, d_tuple, next_idx_tuple)\n\
        \  end\n\n  defp compute_next_idx(two_n, _j, two_n, _x, _d_tuple, acc), do:\
        \ List.to_tuple(Enum.reverse(acc))\n  defp compute_next_idx(i, j, two_n, x,\
        \ d_tuple, acc) do\n    target = elem(d_tuple, i) + x\n    new_j = find_j(j,\
        \ two_n, target, d_tuple)\n    compute_next_idx(i + 1, new_j, two_n, x, d_tuple,\
        \ [new_j | acc])\n  end\n\n  defp find_j(j, two_n, target, d_tuple) when j <\
        \ two_n do\n    if elem(d_tuple, j) < target do\n      find_j(j + 1, two_n,\
        \ target, d_tuple)\n    else\n      j\n    end\n  end\n  defp find_j(j, _two_n,\
        \ _target, _d_tuple), do: j\n\n  defp check_all_i(i, max_i, n, k, l, x, d_tuple,\
        \ next_idx_tuple) when i < max_i do\n    case check_start_i(i, i + n, k - 1,\
        \ next_idx_tuple) do\n      {:ok, last_idx} ->\n        if (elem(d_tuple, i)\
        \ + l - elem(d_tuple, last_idx)) >= x do\n          true\n        else\n   \
        \       check_all_i(i + 1, max_i, n, k, l, x, d_tuple, next_idx_tuple)\n   \
        \     end\n      :error ->\n        check_all_i(i + 1, max_i, n, k, l, x, d_tuple,\
        \ next_idx_tuple)\n    end\n  end\n  defp check_all_i(_i, _max_i, _n, _k, _l,\
        \ _x, _d_tuple, _next_idx_tuple), do: false\n\n  defp check_start_i(curr, _limit,\
        \ 0, _next_idx_tuple), do: {:ok, curr}\n  defp check_start_i(curr, limit, k_left,\
        \ next_idx_tuple) do\n    next_val = elem(next_idx_tuple, curr)\n    if next_val\
        \ >= limit do\n      :error\n    else\n      check_start_i(next_val, limit,\
        \ k_left - 1, next_idx_tuple)\n    end\n  end\nend"
    approach: 'We map each point on the square boundary to a 1D coordinate representing
      its perimeter position, starting from $(0,0)$ and moving clockwise. Specifically,
      a point $(x, y)$ on the boundary of a square with side length $side$ is mapped
      to $pos$: $x$ if $y=0$, $side+y$ if $x=side$, $3\cdot side-x$ if $y=side$, and
      $4\cdot side-y$ if $x=0$. Sorting the points by this coordinate allows us to treat
      the problem as selecting $k$ points on a circular boundary. We then binary search
      for the maximum possible minimum Manhattan distance $D$. Since $k \ge 4$, $D$
      is at most $side$, ensuring the distance between consecutive selected points along
      the perimeter is monotonic and thus greedy selection is applicable.


      For a fixed $D$, we check if it is possible to select $k$ points using binary
      lifting. For each point $i$, we find $nxt[i]$, the first point in clockwise order
      whose Manhattan distance from $P_i$ is at least $D$. Since $D \le side$, this
      point $P_j$ must satisfy $pos_j \ge pos_i + D$, which we find using two pointers.
      We then build a jump table where $jump[i][m]$ is the point reached after $2^m$
      jumps of size at least $D$. For each starting point $i$, we jump $k-1$ times to
      find $P_{idx}$ and check if $idx < i + n$ and if the Manhattan distance between
      the last point $P_{idx}$ and the starting point $P_i$ is also at least $D$. If
      such a sequence exists for any starting point, then $D$ is feasible.'
    time_complexity: O(N \log N + N \log k \log(side)), where $N$ is the number of points.
      Sorting the points takes $O(N \log N)$. The binary search runs for $O(\log(side))$
      iterations. In each iteration, finding the next jump for all points using two
      pointers takes $O(N)$, building the binary lifting table takes $O(N \log k)$,
      and checking all starting points takes $O(N \log k)$.
    space_complexity: O(N \log k) to store the binary lifting table and the doubled
      points array.
    elapsed_time: 688.5244550704956
    model: gemini-3-flash-preview
    generated_at: '2026-04-25 02:00:15 '
---

## Problem #3464: Maximize the Distance Between Points on a Square

**Difficulty:** Hard

**Topics:** Array, Math, Binary Search, Geometry, Sorting

## Problem Description

<p>You are given an integer <code><font face="monospace">side</font></code>, representing the edge length of a square with corners at <code>(0, 0)</code>, <code>(0, side)</code>, <code>(side, 0)</code>, and <code>(side, side)</code> on a Cartesian plane.</p>

<p>You are also given a <strong>positive</strong> integer <code>k</code> and a 2D integer array <code>points</code>, where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> represents the coordinate of a point lying on the <strong>boundary</strong> of the square.</p>

<p>You need to select <code>k</code> elements among <code>points</code> such that the <strong>minimum</strong> Manhattan distance between any two points is <strong>maximized</strong>.</p>

<p>Return the <strong>maximum</strong> possible <strong>minimum</strong> Manhattan distance between the selected <code>k</code> points.</p>

<p>The Manhattan Distance between two cells <code>(x<sub>i</sub>, y<sub>i</sub>)</code> and <code>(x<sub>j</sub>, y<sub>j</sub>)</code> is <code>|x<sub>i</sub> - x<sub>j</sub>| + |y<sub>i</sub> - y<sub>j</sub>|</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">side = 2, points = [[0,2],[2,0],[2,2],[0,0]], k = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2025/01/28/4080_example0_revised.png" style="width: 200px; height: 200px;" /></p>

<p>Select all four points.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">side = 2, points = [[0,0],[1,2],[2,0],[2,2],[2,1]], k = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2025/01/28/4080_example1_revised.png" style="width: 211px; height: 200px;" /></p>

<p>Select the points <code>(0, 0)</code>, <code>(2, 0)</code>, <code>(2, 2)</code>, and <code>(2, 1)</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">side = 2, points = [[0,0],[0,1],[0,2],[1,2],[2,0],[2,2],[2,1]], k = 5</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2025/01/28/4080_example2_revised.png" style="width: 200px; height: 200px;" /></p>

<p>Select the points <code>(0, 0)</code>, <code>(0, 1)</code>, <code>(0, 2)</code>, <code>(1, 2)</code>, and <code>(2, 2)</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= side &lt;= 10<sup>9</sup></code></li>
	<li><code>4 &lt;= points.length &lt;= min(4 * side, 15 * 10<sup>3</sup>)</code></li>
	<li><code>points[i] == [xi, yi]</code></li>
	<li>The input is generated such that:
	<ul>
		<li><code>points[i]</code> lies on the boundary of the square.</li>
		<li>All <code>points[i]</code> are <strong>unique</strong>.</li>
	</ul>
	</li>
	<li><code>4 &lt;= k &lt;= min(25, points.length)</code></li>
</ul>


## Hints

1. Can we use binary search for this problem?

2. Think of the coordinates on a straight line in clockwise order.

3. Binary search on the minimum Manhattan distance `x`.

4. During the binary search, for each coordinate, find the immediate next coordinate with distance >= `x`.

5. Greedily select up to `k` coordinates.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

We map each point on the square boundary to a 1D coordinate representing its perimeter position, starting from $(0,0)$ and moving clockwise. Specifically, a point $(x, y)$ on the boundary of a square with side length $side$ is mapped to $pos$: $x$ if $y=0$, $side+y$ if $x=side$, $3\cdot side-x$ if $y=side$, and $4\cdot side-y$ if $x=0$. Sorting the points by this coordinate allows us to treat the problem as selecting $k$ points on a circular boundary. We then binary search for the maximum possible minimum Manhattan distance $D$. Since $k \ge 4$, $D$ is at most $side$, ensuring the distance between consecutive selected points along the perimeter is monotonic and thus greedy selection is applicable.

For a fixed $D$, we check if it is possible to select $k$ points using binary lifting. For each point $i$, we find $nxt[i]$, the first point in clockwise order whose Manhattan distance from $P_i$ is at least $D$. Since $D \le side$, this point $P_j$ must satisfy $pos_j \ge pos_i + D$, which we find using two pointers. We then build a jump table where $jump[i][m]$ is the point reached after $2^m$ jumps of size at least $D$. For each starting point $i$, we jump $k-1$ times to find $P_{idx}$ and check if $idx < i + n$ and if the Manhattan distance between the last point $P_{idx}$ and the starting point $P_i$ is also at least $D$. If such a sequence exists for any starting point, then $D$ is feasible.

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
    int maxDistance(int side, vector<vector<int>>& points, int k) {
        int n = points.size();
        struct Pt {
            int x, y;
            long long pos;
        };
        vector<Pt> pts(n);
        for (int i = 0; i < n; ++i) {
            pts[i].x = points[i][0];
            pts[i].y = points[i][1];
            if (pts[i].y == 0) pts[i].pos = pts[i].x;
            else if (pts[i].x == side) pts[i].pos = (long long)side + pts[i].y;
            else if (pts[i].y == side) pts[i].pos = 3LL * side - pts[i].x;
            else pts[i].pos = 4LL * side - pts[i].y;
        }

        sort(pts.begin(), pts.end(), [](const Pt& a, const Pt& b) {
            return a.pos < b.pos;
        });

        vector<Pt> d_pts = pts;
        for (int i = 0; i < n; ++i) {
            Pt p = pts[i];
            p.pos += 4LL * side;
            d_pts.push_back(p);
        }

        auto get_dist = [&](int i, int j) {
            return (long long)abs(d_pts[i].x - d_pts[j].x) + abs(d_pts[i].y - d_pts[j].y);
        };

        int logK = 0;
        while ((1 << logK) < k) logK++;
        vector<vector<int>> jump(2 * n, vector<int>(logK));

        auto check = [&](int D) {
            for (int i = 0, j = 0; i < 2 * n; ++i) {
                if (j <= i) j = i + 1;
                while (j < 2 * n && j < i + n && get_dist(i, j) < D) {
                    j++;
                }
                jump[i][0] = j;
            }
            for (int m = 1; m < logK; ++m) {
                for (int i = 0; i < 2 * n; ++i) {
                    if (jump[i][m - 1] < 2 * n) jump[i][m] = jump[jump[i][m - 1]][m - 1];
                    else jump[i][m] = 2 * n;
                }
            }
            for (int i = 0; i < n; ++i) {
                int idx = i;
                for (int m = 0; m < logK; ++m) {
                    if (((k - 1) >> m) & 1) {
                        idx = jump[idx][m];
                        if (idx >= 2 * n) break;
                    }
                }
                if (idx < i + n && get_dist(idx, i) >= D) return true;
            }
            return false;
        };

        int low = 1, high = side, ans = 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (check(mid)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
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
    public int maxDistance(int side, int[][] points, int k) {
        int n = points.length;
        Point[] pts = new Point[n];
        for (int i = 0; i < n; i++) {
            long pos;
            int x = points[i][0], y = points[i][1];
            if (y == 0) pos = x;
            else if (x == side) pos = (long) side + y;
            else if (y == side) pos = 3L * side - x;
            else pos = 4L * side - y;
            pts[i] = new Point(x, y, pos);
        }

        Arrays.sort(pts, Comparator.comparingLong(p -> p.pos));

        Point[] d_pts = new Point[2 * n];
        for (int i = 0; i < n; i++) {
            d_pts[i] = pts[i];
            d_pts[i + n] = new Point(pts[i].x, pts[i].y, pts[i].pos + 4L * side);
        }

        int logK = 0;
        while ((1 << logK) < k) logK++;
        int[][] jump = new int[2 * n][logK];

        int low = 1, high = side, ans = 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (check(mid, n, k, d_pts, jump, logK)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }

    private boolean check(int D, int n, int k, Point[] pts, int[][] jump, int logK) {
        for (int i = 0, j = 0; i < 2 * n; i++) {
            if (j <= i) j = i + 1;
            while (j < 2 * n && j < i + n && getDist(pts[i], pts[j]) < D) {
                j++;
            }
            jump[i][0] = j;
        }
        for (int m = 1; m < logK; m++) {
            for (int i = 0; i < 2 * n; i++) {
                if (jump[i][m - 1] < 2 * n) jump[i][m] = jump[jump[i][m - 1]][m - 1];
                else jump[i][m] = 2 * n;
            }
        }
        for (int i = 0; i < n; i++) {
            int idx = i;
            for (int m = 0; m < logK; m++) {
                if (((k - 1) >> m & 1) == 1) {
                    idx = jump[idx][m];
                    if (idx >= 2 * n) break;
                }
            }
            if (idx < i + n && getDist(pts[idx], pts[i]) >= D) return true;
        }
        return false;
    }

    private long getDist(Point p1, Point p2) {
        return Math.abs((long) p1.x - p2.x) + Math.abs((long) p1.y - p2.y);
    }

    static class Point {
        int x, y;
        long pos;
        Point(int x, int y, long pos) {
            this.x = x;
            this.y = y;
            this.pos = pos;
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maxDistance(self, side, points, k):
        """
        :type side: int
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(points)
        pts_with_pos = []
        for x, y in points:
            if y == 0: pos = x
            elif x == side: pos = side + y
            elif y == side: pos = 3 * side - x
            else: pos = 4 * side - y
            pts_with_pos.append((x, y, pos))

        pts_with_pos.sort(key=lambda p: p[2])
        d_pts = pts_with_pos + [(x, y, pos + 4 * side) for x, y, pos in pts_with_pos]

        logK = (k - 1).bit_length()

        def get_dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        def check(D):
            jump = [[2 * n] * logK for _ in range(2 * n)]
            j = 0
            for i in range(2 * n):
                if j <= i: j = i + 1
                while j < 2 * n and j < i + n and get_dist(d_pts[i], d_pts[j]) < D:
                    j += 1
                jump[i][0] = j

            for m in range(1, logK):
                for i in range(2 * n):
                    prev = jump[i][m-1]
                    if prev < 2 * n:
                        jump[i][m] = jump[prev][m-1]
                    else:
                        jump[i][m] = 2 * n

            for i in range(n):
                idx = i
                for m in range(logK):
                    if ((k - 1) >> m) & 1:
                        idx = jump[idx][m]
                        if idx >= 2 * n: break
                if idx < i + n and get_dist(d_pts[idx], d_pts[i]) >= D:
                    return True
            return False

        low, high, ans = 1, side, 1
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxDistance(self, side: int, points: list[list[int]], k: int) -> int:
        d = []
        for x, y in points:
            if y == 0:
                d.append(x)
            elif x == side:
                d.append(side + y)
            elif y == side:
                d.append(2 * side + (side - x))
            else:
                d.append(3 * side + (side - y))
        d.sort()
        n = len(d)
        perimeter = 4 * side
        d_ext = d + [x + perimeter for x in d]

        def check(D):
            if D == 0:
                return True
            nxt = [2 * n] * (2 * n)
            r = 0
            for l in range(2 * n):
                while r < 2 * n and d_ext[r] - d_ext[l] < D:
                    r += 1
                nxt[l] = r

            limit = d[0] + perimeter // k
            for i in range(n):
                if d[i] > limit:
                    break
                curr = i
                possible = True
                for _ in range(k - 1):
                    curr = nxt[curr]
                    if curr >= 2 * n:
                        possible = False
                        break
                if possible and curr < i + n and (d_ext[i] + perimeter - d_ext[curr]) >= D:
                    return True
            return False

        low = 1
        high = side
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

int compareLong(const void* a, const void* b) {
    long long arg1 = *(const long long*)a;
    long long arg2 = *(const long long*)b;
    if (arg1 < arg2) return -1;
    if (arg1 > arg2) return 1;
    return 0;
}

int check(int D, int n, long long* d_ext, int* nxt, int k, long long perimeter) {
    if (D == 0) return 1;
    int r = 0;
    for (int l = 0; l < 2 * n; l++) {
        while (r < 2 * n && d_ext[r] - d_ext[l] < D) {
            r++;
        }
        nxt[l] = r;
    }
    long long limit = d_ext[0] + perimeter / k;
    for (int i = 0; i < n; i++) {
        if (d_ext[i] > limit) break;
        int curr = i;
        int possible = 1;
        for (int j = 0; j < k - 1; j++) {
            curr = nxt[curr];
            if (curr >= 2 * n) {
                possible = 0;
                break;
            }
        }
        if (possible && curr < i + n && (d_ext[i] + perimeter - d_ext[curr]) >= D) {
            return 1;
        }
    }
    return 0;
}

int maxDistance(int side, int** points, int pointsSize, int* pointsColSize, int k) {
    long long* d = (long long*)malloc(pointsSize * sizeof(long long));
    for (int i = 0; i < pointsSize; i++) {
        long long x = points[i][0];
        long long y = points[i][1];
        if (y == 0) d[i] = x;
        else if (x == side) d[i] = (long long)side + y;
        else if (y == side) d[i] = 2LL * side + (side - x);
        else d[i] = 3LL * side + (side - y);
    }
    qsort(d, pointsSize, sizeof(long long), compareLong);

    int n = pointsSize;
    long long perimeter = 4LL * side;
    long long* d_ext = (long long*)malloc(2 * n * sizeof(long long));
    for (int i = 0; i < n; i++) {
        d_ext[i] = d[i];
        d_ext[i + n] = d[i] + perimeter;
    }

    int* nxt = (int*)malloc(2 * n * sizeof(int));
    int low = 1, high = side, ans = 0;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (check(mid, n, d_ext, nxt, k, perimeter)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    free(d);
    free(d_ext);
    free(nxt);
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaxDistance(int side, int[][] points, int k) {
        int n = points.Length;
        long[] d = new long[n];
        long perimeter = 4L * side;

        for (int i = 0; i < n; i++) {
            long x = points[i][0];
            long y = points[i][1];
            if (y == 0) d[i] = x;
            else if (x == side) d[i] = (long)side + y;
            else if (y == side) d[i] = 2L * side + (side - x);
            else d[i] = 3L * side + (side - y);
        }

        Array.Sort(d);

        long[] d_ext = new long[2 * n];
        for (int i = 0; i < n; i++) {
            d_ext[i] = d[i];
            d_ext[i + n] = d[i] + perimeter;
        }

        int[] nxt = new int[2 * n];
        int low = 1, high = side, ans = 0;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (Check(mid, n, d_ext, nxt, k, perimeter)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return ans;
    }

    private bool Check(int D, int n, long[] d_ext, int[] nxt, int k, long perimeter) {
        if (D == 0) return true;
        int r = 0;
        for (int l = 0; l < 2 * n; l++) {
            while (r < 2 * n && d_ext[r] - d_ext[l] < D) {
                r++;
            }
            nxt[l] = r;
        }

        long limit = d_ext[0] + perimeter / k;
        for (int i = 0; i < n; i++) {
            if (d_ext[i] > limit) break;
            int curr = i;
            bool possible = true;
            for (int j = 0; j < k - 1; j++) {
                curr = nxt[curr];
                if (curr >= 2 * n) {
                    possible = false;
                    break;
                }
            }
            if (possible && curr < i + n && (d_ext[i] + perimeter - d_ext[curr]) >= (long)D) {
                return true;
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
 * @param {number} side
 * @param {number[][]} points
 * @param {number} k
 * @return {number}
 */
var maxDistance = function(side, points, k) {
    let n = points.length;
    let d = new Float64Array(n);
    let perimeter = 4 * side;

    for (let i = 0; i < n; i++) {
        let x = points[i][0], y = points[i][1];
        if (y === 0) d[i] = x;
        else if (x === side) d[i] = side + y;
        else if (y === side) d[i] = 2 * side + (side - x);
        else d[i] = 3 * side + (side - y);
    }

    d.sort();

    let d_ext = new Float64Array(2 * n);
    for (let i = 0; i < n; i++) {
        d_ext[i] = d[i];
        d_ext[i + n] = d[i] + perimeter;
    }

    let nxt = new Int32Array(2 * n);

    function check(D) {
        if (D === 0) return true;
        let r = 0;
        for (let l = 0; l < 2 * n; l++) {
            while (r < 2 * n && d_ext[r] - d_ext[l] < D) {
                r++;
            }
            nxt[l] = r;
        }

        let limit = d_ext[0] + perimeter / k;
        for (let i = 0; i < n; i++) {
            if (d_ext[i] > limit) break;
            let curr = i;
            let possible = true;
            for (let j = 0; j < k - 1; j++) {
                curr = nxt[curr];
                if (curr >= 2 * n) {
                    possible = false;
                    break;
                }
            }
            if (possible && curr < i + n && (d_ext[i] + perimeter - d_ext[curr]) >= D) {
                return true;
            }
        }
        return false;
    }

    let low = 1, high = side, ans = 0;
    while (low <= high) {
        let mid = Math.floor((low + high) / 2);
        if (check(mid)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxDistance(side: number, points: number[][], k: number): number {
    const n = points.length;
    const d: number[] = points.map(([x, y]) => {
        if (x === 0 && y < side) return y;
        if (y === side && x < side) return side + x;
        if (x === side && y > 0) return 2 * side + (side - y);
        return 3 * side + (side - x);
    });
    d.sort((a, b) => a - b);

    const dExpanded = new Float64Array(2 * n);
    for (let i = 0; i < n; i++) {
        dExpanded[i] = d[i];
        dExpanded[i + n] = d[i] + 4 * side;
    }

    const up = new Int32Array((2 * n + 1) * 5);
    const fullPerimeter = 4 * side;

    const check = (x: number): boolean => {
        let r = 0;
        for (let l = 0; l <= 2 * n; l++) {
            while (r < 2 * n && dExpanded[r] < dExpanded[l] + x) {
                r++;
            }
            up[l * 5 + 0] = r;
        }

        for (let p = 1; p < 5; p++) {
            for (let i = 0; i <= 2 * n; i++) {
                const mid = up[i * 5 + (p - 1)];
                if (mid < 2 * n) {
                    up[i * 5 + p] = up[mid * 5 + (p - 1)];
                } else {
                    up[i * 5 + p] = 2 * n;
                }
            }
        }

        for (let i = 0; i < n; i++) {
            let curr = i;
            for (let p = 0; p < 5; p++) {
                if (((k - 1) >> p) & 1) {
                    curr = up[curr * 5 + p];
                    if (curr >= 2 * n) break;
                }
            }
            if (curr < 2 * n && dExpanded[curr] + x <= d[i] + fullPerimeter) {
                return true;
            }
        }
        return false;
    };

    let low = 1, high = side, ans = 1;
    while (low <= high) {
        const mid = Math.floor((low + high) / 2);
        if (check(mid)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $side
     * @param Integer[][] $points
     * @param Integer $k
     * @return Integer
     */
    function maxDistance($side, $points, $k) {
        $n = count($points);
        $d = [];
        $side = (int)$side;
        foreach ($points as $p) {
            $x = $p[0];
            $y = $p[1];
            if ($x == 0 && $y < $side) {
                $d[] = $y;
            } else if ($y == $side && $x < $side) {
                $d[] = $side + $x;
            } else if ($x == $side && $y > 0) {
                $d[] = 2 * $side + ($side - $y);
            } else {
                $d[] = 3 * $side + ($side - $x);
            }
        }
        sort($d);

        $dExpanded = [];
        $fullPerimeter = 4 * $side;
        for ($i = 0; $i < $n; $i++) {
            $dExpanded[$i] = $d[$i];
            $dExpanded[$i + $n] = $d[$i] + $fullPerimeter;
        }

        $up = array_fill(0, (2 * $n + 1) * 5, 2 * $n);

        $check = function($x) use ($n, $k, $d, $dExpanded, $fullPerimeter, &$up) {
            $r = 0;
            for ($l = 0; $l <= 2 * $n; $l++) {
                while ($r < 2 * $n && $dExpanded[$r] < $dExpanded[$l] + $x) {
                    $r++;
                }
                $up[$l * 5 + 0] = $r;
            }

            for ($p = 1; $p < 5; $p++) {
                for ($i = 0; $i <= 2 * $n; $i++) {
                    $mid = $up[$i * 5 + ($p - 1)];
                    if ($mid < 2 * $n) {
                        $up[$i * 5 + $p] = $up[$mid * 5 + ($p - 1)];
                    } else {
                        $up[$i * 5 + $p] = 2 * $n;
                    }
                }
            }

            for ($i = 0; $i < $n; $i++) {
                $curr = $i;
                for ($p = 0; $p < 5; $p++) {
                    if ((($k - 1) >> $p) & 1) {
                        $curr = $up[$curr * 5 + $p];
                        if ($curr >= 2 * $n) break;
                    }
                }
                if ($curr < 2 * $n && $dExpanded[$curr] + $x <= $d[$i] + $fullPerimeter) {
                    return true;
                }
            }
            return false;
        };

        $low = 1;
        $high = $side;
        $ans = 1;
        while ($low <= $high) {
            $mid = floor(($low + $high) / 2);
            if ($check($mid)) {
                $ans = $mid;
                $low = $mid + 1;
            } else {
                $high = $mid - 1;
            }
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
    func maxDistance(_ side: Int, _ points: [[Int]], _ k: Int) -> Int {
        let n = points.count
        let sideL = Int64(side)
        var d = [Int64]()
        for p in points {
            let x = Int64(p[0])
            let y = Int64(p[1])
            if x == 0 && y < sideL {
                d.append(y)
            } else if y == sideL && x < sideL {
                d.append(sideL + x)
            } else if x == sideL && y > 0 {
                d.append(2 * sideL + (sideL - y))
            } else {
                d.append(3 * sideL + (sideL - x))
            }
        }
        d.sort()

        let fullPerimeter = 4 * sideL
        var dExpanded = [Int64](repeating: 0, count: 2 * n)
        for i in 0..<n {
            dExpanded[i] = d[i]
            dExpanded[i + n] = d[i] + fullPerimeter
        }

        var up = [Int](repeating: 2 * n, count: (2 * n + 1) * 5)

        func check(_ x: Int64) -> Bool {
            var r = 0
            for l in 0...(2 * n) {
                while r < 2 * n && dExpanded[r] < dExpanded[l] + x {
                    r += 1
                }
                up[l * 5 + 0] = r
            }

            for p in 1..<5 {
                for i in 0...(2 * n) {
                    let mid = up[i * 5 + p - 1]
                    if mid < 2 * n {
                        up[i * 5 + p] = up[mid * 5 + p - 1]
                    } else {
                        up[i * 5 + p] = 2 * n
                    }
                }
            }

            for i in 0..<n {
                var curr = i
                for p in 0..<5 {
                    if (((k - 1) >> p) & 1) == 1 {
                        curr = up[curr * 5 + p]
                        if curr >= 2 * n { break }
                    }
                }
                if curr < 2 * n && dExpanded[curr] + x <= d[i] + fullPerimeter {
                    return true
                }
            }
            return false
        }

        var low: Int64 = 1
        var high: Int64 = sideL
        var ans: Int64 = 1
        while low <= high {
            let mid = (low + high) / 2
            if check(mid) {
                ans = mid
                low = mid + 1
            } else {
                high = mid - 1
            }
        }
        return Int(ans)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxDistance(side: Int, points: Array<IntArray>, k: Int): Int {
        val n = points.size
        val sideL = side.toLong()
        val d = LongArray(n)
        for (i in points.indices) {
            val x = points[i][0].toLong()
            val y = points[i][1].toLong()
            if (x == 0L && y < sideL) d[i] = y
            else if (y == sideL && x < sideL) d[i] = sideL + x
            else if (x == sideL && y > 0L) d[i] = 2 * sideL + (sideL - y)
            else d[i] = 3 * sideL + (sideL - x)
        }
        d.sort()

        val fullPerimeter = 4 * sideL
        val dExpanded = LongArray(2 * n)
        for (i in 0 until n) {
            dExpanded[i] = d[i]
            dExpanded[i + n] = d[i] + fullPerimeter
        }

        val up = IntArray((2 * n + 1) * 5) { 2 * n }

        fun check(x: Long): Boolean {
            var r = 0
            for (l in 0..2 * n) {
                while (r < 2 * n && dExpanded[r] < dExpanded[l] + x) {
                    r++
                }
                up[l * 5 + 0] = r
            }

            for (p in 1 until 5) {
                for (i in 0..2 * n) {
                    val mid = up[i * 5 + (p - 1)]
                    if (mid < 2 * n) {
                        up[i * 5 + p] = up[mid * 5 + (p - 1)]
                    } else {
                        up[i * 5 + p] = 2 * n
                    }
                }
            }

            for (i in 0 until n) {
                var curr = i
                for (p in 0 until 5) {
                    if (((k - 1) shr p) and 1 == 1) {
                        curr = up[curr * 5 + p]
                        if (curr >= 2 * n) break
                    }
                }
                if (curr < 2 * n && dExpanded[curr] + x <= d[i] + fullPerimeter) {
                    return true
                }
            }
            return false
        }

        var low = 1L
        var high = sideL
        var ans = 1L
        while (low <= high) {
            val mid = (low + high) / 2
            if (check(mid)) {
                ans = mid
                low = mid + 1
            } else {
                high = mid - 1
            }
        }
        return ans.toInt()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:typed_data';

class Solution {
  int getD(int x, int y, int side) {
    if (y == 0) return x;
    if (x == side) return side + y;
    if (y == side) return 3 * side - x;
    return 4 * side - y;
  }

  bool check(int dVal, int n, int k, int side, Int64List d2n) {
    int perimeter = 4 * side;
    Int32List nextIdx = Int32List(2 * n);
    int ptr = 0;
    for (int i = 0; i < 2 * n; i++) {
      while (ptr < 2 * n && d2n[ptr] < d2n[i] + dVal) {
        ptr++;
      }
      nextIdx[i] = ptr;
    }

    int limit = d2n[0] + (perimeter ~/ k);
    for (int i = 0; i < n; i++) {
      if (d2n[i] > limit) break;
      int curr = i;
      int count = 0;
      while (count < k - 1) {
        curr = nextIdx[curr];
        if (curr >= 2 * n) break;
        count++;
      }
      if (count == k - 1 && curr < 2 * n && d2n[i] + perimeter >= d2n[curr] + dVal) {
        return true;
      }
    }
    return false;
  }

  int maxDistance(int side, List<List<int>> points, int k) {
    int n = points.length;
    List<int> dList = points.map((p) => getD(p[0], p[1], side)).toList()..sort();
    Int64List d2n = Int64List(2 * n);
    int perimeter = 4 * side;
    for (int i = 0; i < n; i++) {
      d2n[i] = dList[i].toInt();
      d2n[i + n] = dList[i].toInt() + perimeter;
    }

    int low = 1, high = side;
    int ans = 1;
    while (low <= high) {
      int mid = low + (high - low) ~/ 2;
      if (check(mid, n, k, side, d2n)) {
        ans = mid;
        low = mid + 1;
      } else {
        high = mid - 1;
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
func maxDistance(side int, points [][]int, k int) int {
	n := len(points)
	getD := func(x, y, side int) int64 {
		if y == 0 {
			return int64(x)
		}
		if x == side {
			return int64(side + y)
		}
		if y == side {
			return int64(3*side - x)
		}
		return int64(4*side - y)
	}

	d := make([]int64, n)
	for i := 0; i < n; i++ {
		d[i] = getD(points[i][0], points[i][1], side)
	}
	import "sort"
	sort.Slice(d, func(i, j int) bool { return d[i] < d[j] })

	perimeter := int64(4) * int64(side)
	d2n := make([]int64, 2*n)
	for i := 0; i < n; i++ {
		d2n[i] = d[i]
		d2n[i+n] = d[i] + perimeter
	}

	check := func(dVal int64) bool {
		nextIdx := make([]int, 2*n)
		ptr := 0
		for i := 0; i < 2*n; i++ {
			for ptr < 2*n && d2n[ptr] < d2n[i]+dVal {
				ptr++
			}
			nextIdx[i] = ptr
		}

		limit := d2n[0] + perimeter/int64(k)
		for i := 0; i < n; i++ {
			if d2n[i] > limit {
				break
			}
			curr := i
			count := 0
			for count < k-1 {
				curr = nextIdx[curr]
				if curr >= 2*n {
					break
				}
				count++
			}
			if count == k-1 && curr < 2*n && d2n[i]+perimeter >= d2n[curr]+dVal {
				return true
			}
		}
		return false
	}

	low, high := int64(1), int64(side)
	ans := int64(1)
	for low <= high {
		mid := (low + high) / 2
		if check(mid) {
			ans = mid
			low = mid + 1
		} else {
			high = mid - 1
		}
	}
	return int(ans)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def get_d(x, y, side)
  return x if y == 0
  return side + y if x == side
  return 3 * side - x if y == side
  4 * side - y
end

def check(d_2n, n, k, perimeter, d_val)
  next_idx = Array.new(2 * n)
  ptr = 0
  i = 0
  while i < 2 * n
    while ptr < 2 * n && d_2n[ptr] < d_2n[i] + d_val
      ptr += 1
    end
    next_idx[i] = ptr
    i += 1
  end

  limit = d_2n[0] + (perimeter / k)
  i = 0
  while i < n
    break if d_2n[i] > limit
    curr = i
    count = 0
    while count < k - 1
      curr = next_idx[curr]
      break if curr >= 2 * n
      count += 1
    end
    if count == k - 1 && curr < 2 * n && d_2n[i] + perimeter >= d_2n[curr] + d_val
      return true
    end
    i += 1
  end
  false
end

def max_distance(side, points, k)
  d = points.map { |p| get_d(p[0], p[1], side) }.sort
  n = d.length
  perimeter = 4 * side
  d_2n = d + d.map { |x| x + perimeter }

  low = 1
  high = side
  ans = 1
  while low <= high
    mid = (low + high) / 2
    if check(d_2n, n, k, perimeter, mid)
      ans = mid
      low = mid + 1
    else
      high = mid - 1
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
    def getD(x: Long, y: Long, side: Long): Long = {
        if (y == 0) return x
        if (x == side) return side + y
        if (y == side) return 3 * side - x
        4 * side - y
    }

    def check(d2n: Array[Long], n: Int, k: Int, side: Int, dVal: Int): Boolean = {
        val perimeter = 4L * side
        val nextIdx = new Array[Int](2 * n)
        var ptr = 0
        var i = 0
        while (i < 2 * n) {
            while (ptr < 2 * n && d2n(ptr) < d2n(i) + dVal) {
                ptr += 1
            }
            nextIdx(i) = ptr
            i += 1
        }

        val limit = d2n(0) + (perimeter / k)
        var startIdx = 0
        while (startIdx < n) {
            if (d2n(startIdx) > limit) return false
            var curr = startIdx
            var count = 0
            while (count < k - 1) {
                curr = nextIdx(curr)
                if (curr >= 2 * n) {
                    count = -1 // Break surrogate
                } else {
                    count += 1
                }
                if (count == -1 || count == k - 1) {
                    // exit early loop
                }
            }
            if (count == k - 1 && curr < 2 * n && d2n(startIdx) + perimeter >= d2n(curr) + dVal) {
                return true
            }
            startIdx += 1
        }
        false
    }

    def maxDistance(side: Int, points: Array[Array[Int]], k: Int): Int = {
        val n = points.length
        val d = points.map(p => getD(p(0).toLong, p(1).toLong, side.toLong)).sorted
        val perimeter = 4L * side
        val d2n = new Array[Long](2 * n)
        for (i <- 0 until n) {
            d2n(i) = d(i)
            d2n(i + n) = d(i) + perimeter
        }

        var low = 1
        var high = side
        var ans = 1
        while (low <= high) {
            val mid = low + (high - low) / 2
            if (check(d2n, n, k, side, mid)) {
                ans = mid
                low = mid + 1
            } else {
                high = mid - 1
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
    pub fn max_distance(side: i32, points: Vec<Vec<i32>>, k: i32) -> i32 {
        let n = points.len();
        let side_64 = side as i64;
        let mut d = Vec::with_capacity(n);
        for p in points {
            let x = p[0] as i64;
            let y = p[1] as i64;
            let coord = if y == 0 && x < side_64 {
                x
            } else if x == side_64 && y < side_64 {
                side_64 + y
            } else if y == side_64 && x > 0 {
                2 * side_64 + (side_64 - x)
            } else {
                3 * side_64 + (side_64 - y)
            };
            d.push(coord);
        }
        d.sort_unstable();

        let l = 4 * side_64;
        let mut d2 = vec![0i64; 2 * n];
        for i in 0..n {
            d2[i] = d[i];
            d2[i + n] = d[i] + l;
        }

        let mut low = 1;
        let mut high = side;
        let mut ans = 1;

        while low <= high {
            let mid = low + (high - low) / 2;
            if Self::check(mid as i64, &d2, n, k as usize, l) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        ans
    }

    fn check(x: i64, d: &[i64], n: usize, k: usize, l: i64) -> bool {
        let mut next_idx = vec![0usize; 2 * n];
        let mut j = 0;
        for i in 0..2 * n {
            while j < 2 * n && d[j] < d[i] + x {
                j += 1;
            }
            next_idx[i] = j;
        }

        let max_start = next_idx[0].min(n);
        for i in 0..max_start {
            let mut curr = i;
            let mut possible = true;
            for _ in 0..k - 1 {
                curr = next_idx[curr];
                if curr >= i + n {
                    possible = false;
                    break;
                }
            }
            if possible && d[i] + l - d[curr] >= x {
                return true;
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
(define/contract (max-distance side points k)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ([n (length points)]
         [l (* 4 side)]
         [d-coords (map (lambda (p)
                          (let ([x (car p)] [y (cadr p)])
                            (cond
                              [(and (= y 0) (< x side)) x]
                              [(and (= x side) (< y side)) (+ side y)]
                              [(and (= y side) (> x 0)) (+ (* 2 side) (- side x))]
                              [else (+ (* 3 side) (- side y))]))) 
                        points)]
         [d (list->vector (sort d-coords <))]
         [d2 (make-vector (* 2 n))])
    (for ([i (in-range n)])
      (vector-set! d2 i (vector-ref d i))
      (vector-set! d2 (+ i n) (+ (vector-ref d i) l)))

    (define (check x)
      (let ([next-idx (make-vector (* 2 n))]
            [two-n (* 2 n)])
        (let loop-j ([i 0] [j 0])
          (if (< i two-n)
              (let ([target (+ (vector-ref d2 i) x)])
                (let loop-find-j ([cur-j j])
                  (if (and (< cur-j two-n) (< (vector-ref d2 cur-j) target))
                      (loop-find-j (+ cur-j 1))
                      (begin
                        (vector-set! next-idx i cur-j)
                        (loop-j (+ i 1) cur-j)))))
              (void)))
        (let* ([limit-i (min n (vector-ref next-idx 0))])
          (let loop-i ([i 0])
            (if (< i limit-i)
                (let loop-k ([curr i] [count (- k 1)])
                  (if (= count 0)
                      (if (>= (+ (vector-ref d2 i) l (- (vector-ref d2 curr))) x)
                          #t
                          (loop-i (+ i 1)))
                      (let ([next (vector-ref next-idx curr)])
                        (if (>= next (+ i n))
                            (loop-i (+ i 1))
                            (loop-k next (- count 1))))))
                #f)))))

    (let loop-bs ([low 1] [high side] [ans 1])
      (if (<= low high)
          (let* ([mid (quotient (+ low high) 2)])
            (if (check mid)
                (loop-bs (+ mid 1) high mid)
                (loop-bs low (- mid 1) ans)))
          ans))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_distance(Side :: integer(), Points :: [[integer()]], K :: integer()) -> integer().
max_distance(Side, Points, K) ->
    DCoords = lists:map(fun([X, Y]) -> 
        if 
            Y == 0, X < Side -> X;
            X == Side, Y < Side -> Side + Y;
            Y == Side, X > 0 -> 2 * Side + (Side - X);
            true -> 3 * Side + (Side - Y)
        end
    end, Points),
    SortedD = lists:sort(DCoords),
    N = length(SortedD),
    L = 4 * Side,
    DTuple = list_to_tuple(SortedD ++ [X + L || X <- SortedD]),
    binary_search(1, Side, 1, N, K, L, DTuple).

binary_search(Low, High, Ans, N, K, L, DTuple) when Low =< High ->
    Mid = (Low + High) div 2,
    case check(Mid, N, K, L, DTuple) of
        true -> binary_search(Mid + 1, High, Mid, N, K, L, DTuple);
        false -> binary_search(Low, Mid - 1, Ans, N, K, L, DTuple)
    end;
binary_search(_, _, Ans, _, _, _, _) -> Ans.

check(X, N, K, L, DTuple) ->
    NextIdxTuple = compute_next_idx(0, 0, 2 * N, X, DTuple, []),
    FirstNext = element(1, NextIdxTuple),
    MaxI = if FirstNext < N -> FirstNext; true -> N end,
    check_all_i(0, MaxI, N, K, L, X, DTuple, NextIdxTuple).

compute_next_idx(2 * N, _, _, _, _, Acc) -> list_to_tuple(lists:reverse(Acc));
compute_next_idx(I, J, TwoN, X, DTuple, Acc) ->
    NewJ = find_j(J, TwoN, element(I + 1, DTuple) + X, DTuple),
    compute_next_idx(I + 1, NewJ, TwoN, X, DTuple, [NewJ | Acc]).

find_j(J, TwoN, Target, DTuple) when J < TwoN ->
    case element(J + 1, DTuple) < Target of
        true -> find_j(J + 1, TwoN, Target, DTuple);
        false -> J
    end;
find_j(J, _, _, _) -> J.

check_all_i(I, MaxI, N, K, L, X, DTuple, NextIdxTuple) when I < MaxI ->
    case check_start_i(I, I + N, K - 1, NextIdxTuple) of
        {ok, LastIdx} ->
            if (element(I + 1, DTuple) + L - element(LastIdx + 1, DTuple)) >= X -> true;
               true -> check_all_i(I + 1, MaxI, N, K, L, X, DTuple, NextIdxTuple)
            end;
        error -> check_all_i(I + 1, MaxI, N, K, L, X, DTuple, NextIdxTuple)
    end;
check_all_i(_, _, _, _, _, _, _, _) -> false.

check_start_i(Curr, _Limit, 0, _NextIdxTuple) -> {ok, Curr};
check_start_i(Curr, Limit, KLeft, NextIdxTuple) ->
    Next = element(Curr + 1, NextIdxTuple),
    if Next >= Limit -> error;
       true -> check_start_i(Next, Limit, KLeft - 1, NextIdxTuple)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_distance(side :: integer, points :: [[integer]], k :: integer) :: integer
  def max_distance(side, points, k) do
    d_coords = Enum.map(points, fn [x, y] ->
      cond do
        y == 0 and x < side -> x
        x == side and y < side -> side + y
        y == side and x > 0 -> 2 * side + (side - x)
        true -> 3 * side + (side - y)
      end
    end)
    sorted_d = Enum.sort(d_coords)
    n = length(sorted_d)
    l = 4 * side
    d2 = sorted_d ++ Enum.map(sorted_d, &(&1 + l))
    d_tuple = List.to_tuple(d2)

    binary_search(1, side, 1, n, k, l, d_tuple)
  end

  defp binary_search(low, high, ans, n, k, l, d_tuple) when low <= high do
    mid = div(low + high, 2)
    if check(mid, n, k, l, d_tuple) do
      binary_search(mid + 1, high, mid, n, k, l, d_tuple)
    else
      binary_search(low, mid - 1, ans, n, k, l, d_tuple)
    end
  end
  defp binary_search(_low, _high, ans, _n, _k, _l, _d_tuple), do: ans

  defp check(x, n, k, l, d_tuple) do
    next_idx_tuple = compute_next_idx(0, 0, 2 * n, x, d_tuple, [])
    first_next = elem(next_idx_tuple, 0)
    max_i = min(n, first_next)
    check_all_i(0, max_i, n, k, l, x, d_tuple, next_idx_tuple)
  end

  defp compute_next_idx(two_n, _j, two_n, _x, _d_tuple, acc), do: List.to_tuple(Enum.reverse(acc))
  defp compute_next_idx(i, j, two_n, x, d_tuple, acc) do
    target = elem(d_tuple, i) + x
    new_j = find_j(j, two_n, target, d_tuple)
    compute_next_idx(i + 1, new_j, two_n, x, d_tuple, [new_j | acc])
  end

  defp find_j(j, two_n, target, d_tuple) when j < two_n do
    if elem(d_tuple, j) < target do
      find_j(j + 1, two_n, target, d_tuple)
    else
      j
    end
  end
  defp find_j(j, _two_n, _target, _d_tuple), do: j

  defp check_all_i(i, max_i, n, k, l, x, d_tuple, next_idx_tuple) when i < max_i do
    case check_start_i(i, i + n, k - 1, next_idx_tuple) do
      {:ok, last_idx} ->
        if (elem(d_tuple, i) + l - elem(d_tuple, last_idx)) >= x do
          true
        else
          check_all_i(i + 1, max_i, n, k, l, x, d_tuple, next_idx_tuple)
        end
      :error ->
        check_all_i(i + 1, max_i, n, k, l, x, d_tuple, next_idx_tuple)
    end
  end
  defp check_all_i(_i, _max_i, _n, _k, _l, _x, _d_tuple, _next_idx_tuple), do: false

  defp check_start_i(curr, _limit, 0, _next_idx_tuple), do: {:ok, curr}
  defp check_start_i(curr, limit, k_left, next_idx_tuple) do
    next_val = elem(next_idx_tuple, curr)
    if next_val >= limit do
      :error
    else
      check_start_i(next_val, limit, k_left - 1, next_idx_tuple)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N \log N + N \log k \log(side)), where $N$ is the number of points. Sorting the points takes $O(N \log N)$. The binary search runs for $O(\log(side))$ iterations. In each iteration, finding the next jump for all points using two pointers takes $O(N)$, building the binary lifting table takes $O(N \log k)$, and checking all starting points takes $O(N \log k)$.
- **Space Complexity:** O(N \log k) to store the binary lifting table and the doubled points array.
