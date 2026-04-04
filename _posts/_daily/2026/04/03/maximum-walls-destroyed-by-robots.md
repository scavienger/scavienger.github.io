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
      cpp: '// Generation failed for C++

        // Reason: Parsing failed'
      java: '// Generation failed for Java

        // Reason: Parsing failed'
      python: '// Generation failed for Python

        // Reason: Parsing failed'
      python3: '// Generation failed for Python3

        // Reason: Parsing failed'
      c: "int compareRobots(const void* a, const void* b) {\n    int p1 = *(int*)a,\
        \ p2 = *(int*)b;\n    return (p1 < p2) ? -1 : (p1 > p2 ? 1 : 0);\n}\ntypedef\
        \ struct { int pos, dist; } Robot;\nint compareR(const void* a, const void*\
        \ b) {\n    Robot *r1 = (Robot*)a, *r2 = (Robot*)b;\n    return (r1->pos < r2->pos)\
        \ ? -1 : (r1->pos > r2->pos ? 1 : 0);\n}\nint compareW(const void* a, const\
        \ void* b) {\n    int w1 = *(int*)a, w2 = *(int*)b;\n    return (w1 < w2) ?\
        \ -1 : (w1 > w2 ? 1 : 0);\n}\nint lower_bound(int* arr, int size, int val) {\n\
        \    int low = 0, high = size;\n    while (low < high) {\n        int mid =\
        \ low + (high - low) / 2;\n        if (arr[mid] < val) low = mid + 1; else high\
        \ = mid;\n    }\n    return low;\n}\nint upper_bound(int* arr, int size, int\
        \ val) {\n    int low = 0, high = size;\n    while (low < high) {\n        int\
        \ mid = low + (high - low) / 2;\n        if (arr[mid] <= val) low = mid + 1;\
        \ else high = mid;\n    }\n    return low;\n}\nint getS(int* walls, int size,\
        \ int a, int b) {\n    if (a > b) return 0;\n    int i1 = lower_bound(walls,\
        \ size, a), i2 = upper_bound(walls, size, b);\n    return (i2 > i1) ? (i2 -\
        \ i1) : 0;\n}\nint maxWalls(int* robots, int robotsSize, int* distance, int\
        \ distanceSize, int* walls, int wallsSize) {\n    Robot* r = (Robot*)malloc(robotsSize\
        \ * sizeof(Robot));\n    for (int i = 0; i < robotsSize; i++) { r[i].pos = robots[i];\
        \ r[i].dist = distance[i]; }\n    qsort(r, robotsSize, sizeof(Robot), compareR);\n\
        \    qsort(walls, wallsSize, sizeof(int), compareW);\n    int p0 = 0, p1 = 0,\
        \ pr_lim = 0;\n    for (int i = 0; i < robotsSize; i++) {\n        int ll =\
        \ r[i].pos - r[i].dist;\n        if (i > 0 && ll < r[i-1].pos + 1) ll = r[i-1].pos\
        \ + 1;\n        int rl = r[i].pos + r[i].dist;\n        if (i < robotsSize -\
        \ 1 && rl > r[i+1].pos - 1) rl = r[i+1].pos - 1;\n        int sl = getS(walls,\
        \ wallsSize, ll, r[i].pos), sr = getS(walls, wallsSize, r[i].pos, rl);\n   \
        \     int c0, c1;\n        if (i == 0) { c0 = sl; c1 = sr; } else {\n      \
        \      c1 = (p0 > p1 ? p0 : p1) + sr;\n            int o1 = p0 + sl, start2\
        \ = (ll > pr_lim + 1) ? ll : (pr_lim + 1);\n            int o2 = p1 + getS(walls,\
        \ wallsSize, start2, r[i].pos);\n            c0 = (o1 > o2 ? o1 : o2);\n   \
        \     }\n        p0 = c0; p1 = c1; pr_lim = rl;\n    }\n    free(r);\n    return\
        \ p0 > p1 ? p0 : p1;\n}"
      csharp: "public class Solution {\n    private int LowerBound(int[] arr, int val)\
        \ {\n        int low = 0, high = arr.Length;\n        while (low < high) {\n\
        \            int mid = low + (high - low) / 2;\n            if (arr[mid] < val)\
        \ low = mid + 1; else high = mid;\n        }\n        return low;\n    }\n \
        \   private int UpperBound(int[] arr, int val) {\n        int low = 0, high\
        \ = arr.Length;\n        while (low < high) {\n            int mid = low + (high\
        \ - low) / 2;\n            if (arr[mid] <= val) low = mid + 1; else high = mid;\n\
        \        }\n        return low;\n    }\n    private int GetS(int[] walls, int\
        \ a, int b) {\n        if (a > b) return 0;\n        int i1 = LowerBound(walls,\
        \ a), i2 = UpperBound(walls, b);\n        return i2 > i1 ? i2 - i1 : 0;\n  \
        \  }\n    public int MaxWalls(int[] robots, int[] distance, int[] walls) {\n\
        \        int n = robots.Length;\n        var r = new (int p, int d)[n];\n  \
        \      for (int i = 0; i < n; i++) r[i] = (robots[i], distance[i]);\n      \
        \  System.Array.Sort(r, (a, b) => a.p.CompareTo(b.p));\n        System.Array.Sort(walls);\n\
        \        int p0 = 0, p1 = 0, pr_lim = 0;\n        for (int i = 0; i < n; i++)\
        \ {\n            int ll = Math.Max(r[i].p - r[i].d, i > 0 ? r[i-1].p + 1 : int.MinValue);\n\
        \            int rl = Math.Min(r[i].p + r[i].d, i < n - 1 ? r[i+1].p - 1 : int.MaxValue);\n\
        \            int sl = GetS(walls, ll, r[i].p), sr = GetS(walls, r[i].p, rl);\n\
        \            int c0, c1;\n            if (i == 0) { c0 = sl; c1 = sr; } else\
        \ {\n                c1 = Math.Max(p0, p1) + sr;\n                c0 = Math.Max(p0\
        \ + sl, p1 + GetS(walls, Math.Max(ll, pr_lim + 1), r[i].p));\n            }\n\
        \            p0 = c0; p1 = c1; pr_lim = rl;\n        }\n        return Math.Max(p0,\
        \ p1);\n    }\n}"
      javascript: "/**\n * @param {number[]} robots\n * @param {number[]} distance\n\
        \ * @param {number[]} walls\n * @return {number}\n */\nvar maxWalls = function(robots,\
        \ distance, walls) {\n    const n = robots.length;\n    let r = robots.map((p,\
        \ i) => ({p, d: distance[i]})).sort((a, b) => a.p - b.p);\n    walls.sort((a,\
        \ b) => a - b);\n    const lb = (val) => {\n        let low = 0, high = walls.length;\n\
        \        while (low < high) {\n            let mid = (low + high) >>> 1;\n \
        \           if (walls[mid] < val) low = mid + 1; else high = mid;\n        }\n\
        \        return low;\n    };\n    const ub = (val) => {\n        let low = 0,\
        \ high = walls.length;\n        while (low < high) {\n            let mid =\
        \ (low + high) >>> 1;\n            if (walls[mid] <= val) low = mid + 1; else\
        \ high = mid;\n        }\n        return low;\n    };\n    const getS = (a,\
        \ b) => {\n        if (a > b) return 0;\n        let i1 = lb(a), i2 = ub(b);\n\
        \        return i2 > i1 ? i2 - i1 : 0;\n    };\n    let p0 = 0, p1 = 0, pr_lim\
        \ = 0;\n    for (let i = 0; i < n; i++) {\n        let ll = Math.max(r[i].p\
        \ - r[i].d, i > 0 ? r[i-1].p + 1 : -2e9);\n        let rl = Math.min(r[i].p\
        \ + r[i].d, i < n - 1 ? r[i+1].p - 1 : 2e9);\n        let sl = getS(ll, r[i].p),\
        \ sr = getS(r[i].p, rl);\n        let c0, c1;\n        if (i === 0) {\n    \
        \        c0 = sl; c1 = sr;\n        } else {\n            c1 = Math.max(p0,\
        \ p1) + sr;\n            c0 = Math.max(p0 + sl, p1 + getS(Math.max(ll, pr_lim\
        \ + 1), r[i].p));\n        }\n        p0 = c0; p1 = c1; pr_lim = rl;\n    }\n\
        \    return Math.max(p0, p1);\n};"
      typescript: "function maxWalls(robots: number[], distance: number[], walls: number[]):\
        \ number {\n    const n = robots.length;\n    const comb = robots.map((r, i)\
        \ => [r, distance[i]]).sort((a, b) => a[0] - b[0]);\n    const rPos = comb.map(x\
        \ => x[0]);\n    const rDist = comb.map(x => x[1]);\n    walls.sort((a, b) =>\
        \ a - b);\n    const m = walls.length;\n\n    const lowerBound = (target: number)\
        \ => {\n        let l = 0, r = m;\n        while (l < r) {\n            let\
        \ mid = (l + r) >>> 1;\n            if (walls[mid] < target) l = mid + 1; else\
        \ r = mid;\n        }\n        return l;\n    };\n    const upperBound = (target:\
        \ number) => {\n        let l = 0, r = m;\n        while (l < r) {\n       \
        \     let mid = (l + r) >>> 1;\n            if (walls[mid] <= target) l = mid\
        \ + 1; else r = mid;\n        }\n        return l;\n    };\n    const countInRange\
        \ = (min: number, max: number) => {\n        if (min > max) return 0;\n    \
        \    return upperBound(max) - lowerBound(min);\n    };\n    const hasWall =\
        \ (pos: number) => {\n        const idx = lowerBound(pos);\n        return (idx\
        \ < m && walls[idx] === pos) ? 1 : 0;\n    };\n\n    let prevL = countInRange(rPos[0]\
        \ - rDist[0], rPos[0]);\n    let prevR = countInRange(rPos[0], n > 1 ? Math.min(rPos[1],\
        \ rPos[0] + rDist[0]) : rPos[0] + rDist[0]);\n\n    for (let i = 1; i < n; i++)\
        \ {\n        const Li = countInRange(Math.max(rPos[i - 1], rPos[i] - rDist[i]),\
        \ rPos[i]);\n        const Ri = countInRange(rPos[i], i < n - 1 ? Math.min(rPos[i\
        \ + 1], rPos[i] + rDist[i]) : rPos[i] + rDist[i]);\n        const overlapLL\
        \ = (rPos[i] - rDist[i] <= rPos[i - 1]) ? hasWall(rPos[i - 1]) : 0;\n      \
        \  const overlapRR = (rPos[i - 1] + rDist[i - 1] >= rPos[i]) ? hasWall(rPos[i])\
        \ : 0;\n        const overlapRL = countInRange(Math.max(rPos[i - 1], rPos[i]\
        \ - rDist[i]), Math.min(rPos[i], rPos[i - 1] + rDist[i - 1]));\n\n        const\
        \ currL = Math.max(prevL + Li - overlapLL, prevR + Li - overlapRL);\n      \
        \  const currR = Math.max(prevL + Ri, prevR + Ri - overlapRR);\n        prevL\
        \ = currL;\n        prevR = currR;\n    }\n    return Math.max(prevL, prevR);\n\
        }"
      php: "class Solution {\n    /**\n     * @param Integer[] $robots\n     * @param\
        \ Integer[] $distance\n     * @param Integer[] $walls\n     * @return Integer\n\
        \     */\n    function maxWalls($robots, $distance, $walls) {\n        $n =\
        \ count($robots);\n        $r_pos = $robots;\n        $r_dist = $distance;\n\
        \        array_multisort($r_pos, SORT_ASC, SORT_NUMERIC, $r_dist);\n       \
        \ sort($walls, SORT_NUMERIC);\n        $m = count($walls);\n\n        $lowerBound\
        \ = function($target) use ($walls, $m) {\n            $l = 0; $r = $m;\n   \
        \         while ($l < $r) {\n                $mid = $l + (int)(($r - $l) / 2);\n\
        \                if ($walls[$mid] < $target) $l = $mid + 1;\n              \
        \  else $r = $mid;\n            }\n            return $l;\n        };\n    \
        \    $upperBound = function($target) use ($walls, $m) {\n            $l = 0;\
        \ $r = $m;\n            while ($l < $r) {\n                $mid = $l + (int)(($r\
        \ - $l) / 2);\n                if ($walls[$mid] <= $target) $l = $mid + 1;\n\
        \                else $r = $mid;\n            }\n            return $l;\n  \
        \      };\n        $countInRange = function($minV, $maxV) use ($lowerBound,\
        \ $upperBound) {\n            if ($minV > $maxV) return 0;\n            return\
        \ $upperBound($maxV) - $lowerBound($minV);\n        };\n        $hasWall = function($pos)\
        \ use ($walls, $m, $lowerBound) {\n            $idx = $lowerBound($pos);\n \
        \           return ($idx < $m && $walls[$idx] == $pos) ? 1 : 0;\n        };\n\
        \n        $prevL = $countInRange($r_pos[0] - $r_dist[0], $r_pos[0]);\n     \
        \   $prevR = $countInRange($r_pos[0], $n > 1 ? min($r_pos[1], $r_pos[0] + $r_dist[0])\
        \ : $r_pos[0] + $r_dist[0]);\n\n        for ($i = 1; $i < $n; $i++) {\n    \
        \        $Li = $countInRange(max($r_pos[$i-1], $r_pos[$i] - $r_dist[$i]), $r_pos[$i]);\n\
        \            $Ri = $countInRange($r_pos[$i], ($i < $n - 1 ? min($r_pos[$i+1],\
        \ $r_pos[$i] + $r_dist[$i]) : $r_pos[$i] + $r_dist[$i]));\n            $overlapLL\
        \ = ($r_pos[$i] - $r_dist[$i] <= $r_pos[$i-1]) ? $hasWall($r_pos[$i-1]) : 0;\n\
        \            $overlapRR = ($r_pos[$i-1] + $r_dist[$i-1] >= $r_pos[$i]) ? $hasWall($r_pos[$i])\
        \ : 0;\n            $overlapRL = $countInRange(max($r_pos[$i-1], $r_pos[$i]\
        \ - $r_dist[$i]), min($r_pos[$i], $r_pos[$i-1] + $r_dist[$i-1]));\n        \
        \    $currL = max($prevL + $Li - $overlapLL, $prevR + $Li - $overlapRL);\n \
        \           $currR = max($prevL + $Ri, $prevR + $Ri - $overlapRR);\n       \
        \     $prevL = $currL;\n            $prevR = $currR;\n        }\n        return\
        \ max($prevL, $prevR);\n    }\n}"
      swift: "class Solution {\n    func maxWalls(_ robots: [Int], _ distance: [Int],\
        \ _ walls: [Int]) -> Int {\n        let n = robots.count\n        var robotsWithDist\
        \ = [(Int, Int)]()\n        for i in 0..<n {\n            robotsWithDist.append((robots[i],\
        \ distance[i]))\n        }\n        robotsWithDist.sort { $0.0 < $1.0 }\n  \
        \      let rPos = robotsWithDist.map { $0.0 }\n        let rDist = robotsWithDist.map\
        \ { $0.1 }\n        let sortedWalls = walls.sorted()\n        let m = sortedWalls.count\n\
        \n        func lowerBound(_ target: Int) -> Int {\n            var l = 0, r\
        \ = m\n            while l < r {\n                let mid = l + (r - l) / 2\n\
        \                if sortedWalls[mid] < target { l = mid + 1 } else { r = mid\
        \ }\n            }\n            return l\n        }\n        func upperBound(_\
        \ target: Int) -> Int {\n            var l = 0, r = m\n            while l <\
        \ r {\n                let mid = l + (r - l) / 2\n                if sortedWalls[mid]\
        \ <= target { l = mid + 1 } else { r = mid }\n            }\n            return\
        \ l\n        }\n        func countInRange(_ minV: Int, _ maxV: Int) -> Int {\n\
        \            if minV > maxV { return 0 }\n            return upperBound(maxV)\
        \ - lowerBound(minV)\n        }\n        func hasWall(_ pos: Int) -> Int {\n\
        \            let idx = lowerBound(pos)\n            return (idx < m && sortedWalls[idx]\
        \ == pos) ? 1 : 0\n        }\n\n        var prevL = countInRange(rPos[0] - rDist[0],\
        \ rPos[0])\n        var prevR = countInRange(rPos[0], n > 1 ? min(rPos[1], rPos[0]\
        \ + rDist[0]) : rPos[0] + rDist[0])\n\n        if n > 1 {\n            for i\
        \ in 1..<n {\n                let Li = countInRange(max(rPos[i-1], rPos[i] -\
        \ rDist[i]), rPos[i])\n                let Ri = countInRange(rPos[i], i < n\
        \ - 1 ? min(rPos[i+1], rPos[i] + rDist[i]) : rPos[i] + rDist[i])\n         \
        \       let overlapLL = (rPos[i] - rDist[i] <= rPos[i-1]) ? hasWall(rPos[i-1])\
        \ : 0\n                let overlapRR = (rPos[i-1] + rDist[i-1] >= rPos[i]) ?\
        \ hasWall(rPos[i]) : 0\n                let overlapRL = countInRange(max(rPos[i-1],\
        \ rPos[i] - rDist[i]), min(rPos[i], rPos[i-1] + rDist[i-1]))\n             \
        \   let currL = max(prevL + Li - overlapLL, prevR + Li - overlapRL)\n      \
        \          let currR = max(prevL + Ri, prevR + Ri - overlapRR)\n           \
        \     prevL = currL\n                prevR = currR\n            }\n        }\n\
        \        return max(prevL, prevR)\n    }\n}"
      kotlin: "import java.util.*\n\nclass Solution {\n    fun maxWalls(robots: IntArray,\
        \ distance: IntArray, walls: IntArray): Int {\n        val n = robots.size\n\
        \        val idx = (0 until n).sortedBy { robots[it] }\n        val sortedR\
        \ = IntArray(n) { robots[idx[it]] }\n        val sortedD = IntArray(n) { distance[idx[it]]\
        \ }\n        walls.sort()\n\n        fun lowerBound(a: IntArray, target: Int):\
        \ Int {\n            var low = 0\n            var high = a.size\n          \
        \  while (low < high) {\n                val mid = low + (high - low) / 2\n\
        \                if (a[mid] >= target) high = mid else low = mid + 1\n     \
        \       }\n            return low\n        }\n\n        fun countInRange(a:\
        \ Int, b: Int): Int {\n            if (a > b) return 0\n            return lowerBound(walls,\
        \ b + 1) - lowerBound(walls, a)\n        }\n\n        fun hasWall(pos: Int):\
        \ Boolean {\n            val i = lowerBound(walls, pos)\n            return\
        \ i < walls.size && walls[i] == pos\n        }\n\n        var p0 = countInRange(sortedR[0]\
        \ - sortedD[0], sortedR[0]).toLong()\n        val r1 = if (n > 1) sortedR[1]\
        \ else 2100000000\n        var p1 = countInRange(sortedR[0], minOf(sortedR[0]\
        \ + sortedD[0], r1)).toLong()\n\n        for (i in 1 until n) {\n          \
        \  val rPrev = sortedR[i - 1]\n            val rNext = if (i < n - 1) sortedR[i\
        \ + 1] else 2100000000\n            val cl = countInRange(maxOf(sortedR[i] -\
        \ sortedD[i], rPrev), sortedR[i])\n            val cr = countInRange(sortedR[i],\
        \ minOf(sortedR[i] + sortedD[i], rNext))\n            val overRL = countInRange(maxOf(rPrev,\
        \ sortedR[i] - sortedD[i]), minOf(rPrev + sortedD[i - 1], sortedR[i]))\n   \
        \         val wallAtRprev = if (hasWall(rPrev) && (sortedR[i] - sortedD[i] <=\
        \ rPrev)) 1 else 0\n            val wallAtRi = if (hasWall(sortedR[i]) && (rPrev\
        \ + sortedD[i - 1] >= sortedR[i])) 1 else 0\n\n            val next0 = maxOf(p0\
        \ + cl - wallAtRprev, p1 + cl - overRL)\n            val next1 = maxOf(p0 +\
        \ cr, p1 + cr - wallAtRi)\n            p0 = next0\n            p1 = next1\n\
        \        }\n\n        return maxOf(p0, p1).toInt()\n    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int maxWalls(List<int> robots,\
        \ List<int> distance, List<int> walls) {\n    int n = robots.length;\n    List<int>\
        \ idx = List.generate(n, (i) => i);\n    idx.sort((a, b) => robots[a].compareTo(robots[b]));\n\
        \    List<int> sortedR = idx.map((i) => robots[i]).toList();\n    List<int>\
        \ sortedD = idx.map((i) => distance[i]).toList();\n    walls.sort();\n\n   \
        \ int lowerBound(List<int> a, int target) {\n      int low = 0, high = a.length;\n\
        \      while (low < high) {\n        int mid = (low + high) ~/ 2;\n        if\
        \ (a[mid] >= target) high = mid; else low = mid + 1;\n      }\n      return\
        \ low;\n    }\n\n    int countInRange(int a, int b) {\n      if (a > b) return\
        \ 0;\n      return lowerBound(walls, b + 1) - lowerBound(walls, a);\n    }\n\
        \n    bool hasWall(int pos) {\n      int i = lowerBound(walls, pos);\n     \
        \ return i < walls.length && walls[i] == pos;\n    }\n\n    int r1 = n > 1 ?\
        \ sortedR[1] : 2100000000;\n    int p0 = countInRange(sortedR[0] - sortedD[0],\
        \ sortedR[0]);\n    int p1 = countInRange(sortedR[0], min(sortedR[0] + sortedD[0],\
        \ r1));\n\n    for (int i = 1; i < n; i++) {\n      int rPrev = sortedR[i -\
        \ 1];\n      int rNext = i < n - 1 ? sortedR[i + 1] : 2100000000;\n      int\
        \ cl = countInRange(max(sortedR[i] - sortedD[i], rPrev), sortedR[i]);\n    \
        \  int cr = countInRange(sortedR[i], min(sortedR[i] + sortedD[i], rNext));\n\
        \      int overRL = countInRange(max(rPrev, sortedR[i] - sortedD[i]), min(rPrev\
        \ + sortedD[i - 1], sortedR[i]));\n      int wallAtRprev = (hasWall(rPrev) &&\
        \ (sortedR[i] - sortedD[i] <= rPrev)) ? 1 : 0;\n      int wallAtRi = (hasWall(sortedR[i])\
        \ && (rPrev + sortedD[i - 1] >= sortedR[i])) ? 1 : 0;\n\n      int next0 = max(p0\
        \ + cl - wallAtRprev, p1 + cl - overRL);\n      int next1 = max(p0 + cr, p1\
        \ + cr - wallAtRi);\n      p0 = next0;\n      p1 = next1;\n    }\n\n    return\
        \ max(p0, p1);\n  }\n}"
      go: "import (\n\t\"sort\"\n)\n\nfunc maxWalls(robots []int, distance []int, walls\
        \ []int) int {\n\tsort.Ints(walls)\n\tn := len(robots)\n\ttype robot struct{\
        \ pos, dist int }\n\trList := make([]robot, n)\n\tfor i := range robots {\n\t\
        \trList[i] = robot{robots[i], distance[i]}\n\t}\n\tsort.Slice(rList, func(i,\
        \ j int) bool { return rList[i].pos < rList[j].pos })\n\tsortedR := make([]int,\
        \ n)\n\tsortedD := make([]int, n)\n\tfor i := range rList {\n\t\tsortedR[i],\
        \ sortedD[i] = rList[i].pos, rList[i].dist\n\t}\n\n\tcount := func(a, b int)\
        \ int {\n\t\tif a > b { return 0 }\n\t\treturn sort.SearchInts(walls, b+1) -\
        \ sort.SearchInts(walls, a)\n\t}\n\thasWall := func(pos int) bool {\n\t\ti :=\
        \ sort.SearchInts(walls, pos)\n\t\treturn i < len(walls) && walls[i] == pos\n\
        \t}\n\tmax64 := func(a, b int64) int64 {\n\t\tif a > b { return a }\n\t\treturn\
        \ b\n\t}\n\tmin := func(a, b int) int {\n\t\tif a < b { return a }\n\t\treturn\
        \ b\n\t}\n\tmax := func(a, b int) int {\n\t\tif a > b { return a }\n\t\treturn\
        \ b\n\t}\n\n\tr1 := 2100000000\n\tif n > 1 { r1 = sortedR[1] }\n\tp0 := int64(count(sortedR[0]-sortedD[0],\
        \ sortedR[0]))\n\tp1 := int64(count(sortedR[0], min(sortedR[0]+sortedD[0], r1)))\n\
        \n\tfor i := 1; i < n; i++ {\n\t\trPrev, rNext := sortedR[i-1], 2100000000\n\
        \t\tif i < n-1 { rNext = sortedR[i+1] }\n\t\tcl := int64(count(max(sortedR[i]-sortedD[i],\
        \ rPrev), sortedR[i]))\n\t\tcr := int64(count(sortedR[i], min(sortedR[i]+sortedD[i],\
        \ rNext)))\n\t\toverRL := int64(count(max(rPrev, sortedR[i]-sortedD[i]), min(rPrev+sortedD[i-1],\
        \ sortedR[i])))\n\t\twallAtRprev := int64(0)\n\t\tif hasWall(rPrev) && sortedR[i]-sortedD[i]\
        \ <= rPrev { wallAtRprev = 1 }\n\t\twallAtRi := int64(0)\n\t\tif hasWall(sortedR[i])\
        \ && rPrev+sortedD[i-1] >= sortedR[i] { wallAtRi = 1 }\n\n\t\tnext0 := max64(p0+cl-wallAtRprev,\
        \ p1+cl-overRL)\n\t\tnext1 := max64(p0+cr, p1+cr-wallAtRi)\n\t\tp0, p1 = next0,\
        \ next1\n\t}\n\treturn int(max64(p0, p1))\n}"
      ruby: "def max_walls(robots, distance, walls)\n  n = robots.size\n  m = walls.size\n\
        \  walls.sort!\n  r_sorted = robots.zip(distance).sort_by(&:first)\n\n  def\
        \ lower_bound(walls, val)\n    walls.bsearch_index { |w| w >= val } || walls.size\n\
        \  end\n\n  def upper_bound(walls, val)\n    walls.bsearch_index { |w| w > val\
        \ } || walls.size\n  end\n\n  def get_counts(walls, x_prev, d_prev, x_curr,\
        \ d_curr)\n    a = lower_bound(walls, x_prev + 1)\n    b = lower_bound(walls,\
        \ x_curr) - 1\n    return [0, 0, 0] if a > b\n\n    p_end = upper_bound(walls,\
        \ x_prev + d_prev) - 1\n    q_start = lower_bound(walls, x_curr - d_curr)\n\n\
        \    p_end_eff = [p_end, b].min\n    q_start_eff = [q_start, a].max\n\n    cp\
        \ = [0, p_end_eff - a + 1].max\n    cq = [0, b - q_start_eff + 1].max\n\n  \
        \  if p_end_eff < a\n      cpuq = cq\n    elsif q_start_eff > b\n      cpuq\
        \ = cp\n    elsif p_end_eff >= q_start_eff - 1\n      cpuq = b - a + 1\n   \
        \ else\n      cpuq = cp + cq\n    end\n    [cp, cq, cpuq]\n  end\n\n  dp = Array.new(n)\
        \ { [0, 0] }\n  b0 = lower_bound(walls, r_sorted[0][0]) - 1\n  q_start0 = lower_bound(walls,\
        \ r_sorted[0][0] - r_sorted[0][1])\n  dp[0][0] = [0, b0 - q_start0 + 1].max\n\
        \  dp[0][1] = 0\n\n  (1...n).each do |i|\n    cp, cq, cpuq = get_counts(walls,\
        \ r_sorted[i-1][0], r_sorted[i-1][1], r_sorted[i][0], r_sorted[i][1])\n    dp[i][0]\
        \ = [dp[i-1][0] + cq, dp[i-1][1] + cpuq].max\n    dp[i][1] = [dp[i-1][0], dp[i-1][1]\
        \ + cp].max\n  end\n\n  an = lower_bound(walls, r_sorted[n-1][0] + 1)\n  bn\
        \ = m - 1\n  p_end_n = upper_bound(walls, r_sorted[n-1][0] + r_sorted[n-1][1])\
        \ - 1\n  count_pn = [0, [p_end_n, bn].min - an + 1].max\n\n  total_walls_at_robots\
        \ = 0\n  r_sorted.each do |x, _|\n    idx = lower_bound(walls, x)\n    total_walls_at_robots\
        \ += 1 if idx < m && walls[idx] == x\n  end\n\n  [dp[n-1][0], dp[n-1][1] + count_pn].max\
        \ + total_walls_at_robots\nend"
      scala: "object Solution {\n    def maxWalls(robots: Array[Int], distance: Array[Int],\
        \ walls: Array[Int]): Int = {\n        val n = robots.length\n        val sortedWalls\
        \ = walls.sorted\n        val rSorted = robots.zip(distance).sortBy(_._1)\n\n\
        \        def lowerBound(a: Array[Int], v: Int): Int = {\n            var low\
        \ = 0; var high = a.length\n            while (low < high) {\n             \
        \   val mid = low + (high - low) / 2\n                if (a(mid) < v) low =\
        \ mid + 1 else high = mid\n            }\n            low\n        }\n\n   \
        \     def upperBound(a: Array[Int], v: Int): Int = {\n            var low =\
        \ 0; var high = a.length\n            while (low < high) {\n               \
        \ val mid = low + (high - low) / 2\n                if (a(mid) <= v) low = mid\
        \ + 1 else high = mid\n            }\n            low\n        }\n\n       \
        \ val dp = Array.fill(n, 2)(0)\n        val b0 = lowerBound(sortedWalls, rSorted(0)._1)\
        \ - 1\n        val qStart0 = lowerBound(sortedWalls, rSorted(0)._1 - rSorted(0)._2)\n\
        \        dp(0)(0) = Math.max(0, b0 - qStart0 + 1)\n        dp(0)(1) = 0\n\n\
        \        for (i <- 1 until n) {\n            val xPrev = rSorted(i-1)._1\n \
        \           val dPrev = rSorted(i-1)._2\n            val xCurr = rSorted(i)._1\n\
        \            val dCurr = rSorted(i)._2\n\n            val a = lowerBound(sortedWalls,\
        \ xPrev + 1)\n            val b = lowerBound(sortedWalls, xCurr) - 1\n     \
        \       var cp = 0; var cq = 0; var cpuq = 0\n\n            if (a <= b) {\n\
        \                val pEnd = upperBound(sortedWalls, xPrev + dPrev) - 1\n   \
        \             val qStart = lowerBound(sortedWalls, xCurr - dCurr)\n        \
        \        val pEndEff = Math.min(pEnd, b)\n                val qStartEff = Math.max(qStart,\
        \ a)\n                cp = Math.max(0, pEndEff - a + 1)\n                cq\
        \ = Math.max(0, b - qStartEff + 1)\n                if (pEndEff < a) cpuq =\
        \ cq\n                else if (qStartEff > b) cpuq = cp\n                else\
        \ if (pEndEff >= qStartEff - 1) cpuq = b - a + 1\n                else cpuq\
        \ = cp + cq\n            }\n            dp(i)(0) = Math.max(dp(i-1)(0) + cq,\
        \ dp(i-1)(1) + cpuq)\n            dp(i)(1) = Math.max(dp(i-1)(0), dp(i-1)(1)\
        \ + cp)\n        }\n\n        val an = lowerBound(sortedWalls, rSorted(n-1)._1\
        \ + 1)\n        val bn = sortedWalls.length - 1\n        val pEndN = upperBound(sortedWalls,\
        \ rSorted(n-1)._1 + rSorted(n-1)._2) - 1\n        val countPn = Math.max(0,\
        \ Math.min(pEndN, bn) - an + 1)\n\n        var totalAtRobots = 0\n        for\
        \ (r <- rSorted) {\n            val idx = lowerBound(sortedWalls, r._1)\n  \
        \          if (idx < sortedWalls.length && sortedWalls(idx) == r._1) totalAtRobots\
        \ += 1\n        }\n\n        Math.max(dp(n-1)(0), dp(n-1)(1) + countPn) + totalAtRobots\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn max_walls(robots: Vec<i32>, distance: Vec<i32>,\
        \ walls: Vec<i32>) -> i32 {\n        let n = robots.len();\n        let mut\
        \ sorted_walls = walls;\n        sorted_walls.sort();\n        let mut r_sorted:\
        \ Vec<(i32, i32)> = robots.into_iter().zip(distance.into_iter()).collect();\n\
        \        r_sorted.sort_by_key(|r| r.0);\n\n        let mut dp = vec![[0i32;\
        \ 2]; n];\n        let b0 = sorted_walls.partition_point(|&w| w < r_sorted[0].0)\
        \ as i32 - 1;\n        let q_start0 = sorted_walls.partition_point(|&w| w <\
        \ r_sorted[0].0 - r_sorted[0].1) as i32;\n        dp[0][0] = 0.max(b0 - q_start0\
        \ + 1);\n        dp[0][1] = 0;\n\n        for i in 1..n {\n            let (x_prev,\
        \ d_prev) = r_sorted[i-1];\n            let (x_curr, d_curr) = r_sorted[i];\n\
        \            let a = sorted_walls.partition_point(|&w| w < x_prev + 1) as i32;\n\
        \            let b = sorted_walls.partition_point(|&w| w < x_curr) as i32 -\
        \ 1;\n            let (mut cp, mut cq, mut cpuq) = (0, 0, 0);\n\n          \
        \  if a <= b {\n                let p_end = sorted_walls.partition_point(|&w|\
        \ w <= x_prev + d_prev) as i32 - 1;\n                let q_start = sorted_walls.partition_point(|&w|\
        \ w < x_curr - d_curr) as i32;\n                let p_end_eff = p_end.min(b);\n\
        \                let q_start_eff = q_start.max(a);\n                cp = 0.max(p_end_eff\
        \ - a + 1);\n                cq = 0.max(b - q_start_eff + 1);\n            \
        \    if p_end_eff < a { cpuq = cq; }\n                else if q_start_eff >\
        \ b { cpuq = cp; }\n                else if p_end_eff >= q_start_eff - 1 { cpuq\
        \ = b - a + 1; }\n                else { cpuq = cp + cq; }\n            }\n\
        \            dp[i][0] = (dp[i-1][0] + cq).max(dp[i-1][1] + cpuq);\n        \
        \    dp[i][1] = dp[i-1][0].max(dp[i-1][1] + cp);\n        }\n\n        let an\
        \ = sorted_walls.partition_point(|&w| w < r_sorted[n-1].0 + 1) as i32;\n   \
        \     let bn = sorted_walls.len() as i32 - 1;\n        let p_end_n = sorted_walls.partition_point(|&w|\
        \ w <= r_sorted[n-1].0 + r_sorted[n-1].1) as i32 - 1;\n        let count_pn\
        \ = 0.max(p_end_n.min(bn) - an + 1);\n\n        let mut total_at_robots = 0;\n\
        \        for r in &r_sorted {\n            let idx = sorted_walls.partition_point(|&w|\
        \ w < r.0);\n            if idx < sorted_walls.len() && sorted_walls[idx] ==\
        \ r.0 { total_at_robots += 1; }\n        }\n\n        dp[n-1][0].max(dp[n-1][1]\
        \ + count_pn) + total_at_robots\n    }\n}"
      racket: "(define/contract (max-walls robots distance walls)\n  (-> (listof exact-integer?)\
        \ (listof exact-integer?) (listof exact-integer?) exact-integer?)\n  (let* ([n\
        \ (length robots)]\n         [robots-dist (sort (map list robots distance) <\
        \ #:key car)]\n         [sorted-walls (list->vector (sort walls <))]\n     \
        \    [m (vector-length sorted-walls)])\n    (define (lb val)\n      (let loop\
        \ ([low 0] [high m])\n        (if (< low high)\n            (let ([mid (quotient\
        \ (+ low high) 2)])\n              (if (< (vector-ref sorted-walls mid) val)\n\
        \                  (loop (+ mid 1) high)\n                  (loop low mid)))\n\
        \            low)))\n    (define (ub val)\n      (let loop ([low 0] [high m])\n\
        \        (if (< low high)\n            (let ([mid (quotient (+ low high) 2)])\n\
        \              (if (<= (vector-ref sorted-walls mid) val)\n                \
        \  (loop (+ mid 1) high)\n                  (loop low mid)))\n            low)))\n\
        \    (define (W a b)\n      (if (> a b) 0 (- (ub b) (lb a))))\n    (let loop\
        \ ([rs robots-dist] [px -1] [pd -1] [dp0 0] [dp1 0])\n      (if (null? rs)\n\
        \          (max dp0 dp1)\n          (let* ([curr (car rs)]\n               \
        \  [x (car curr)]\n                 [d (cadr curr)]\n                 [nx (if\
        \ (null? (cdr rs)) 2000000001 (car (cadr rs)))])\n            (if (= px -1)\n\
        \                (loop (cdr rs) x d (W (- x d) x) (W x (min (+ x d) nx)))\n\
        \                (let* ([sr-prev (min (+ px pd) x)]\n                      \
        \ [sl-curr (max (- x d) px)]\n                       [w-left-0 (W (max sl-curr\
        \ (+ px 1)) x)]\n                       [w-left-1 (W (max sl-curr (+ sr-prev\
        \ 1)) x)]\n                       [new-dp0 (max (+ dp0 w-left-0) (+ dp1 w-left-1))]\n\
        \                       [w-right-0 (W x (min (+ x d) nx))]\n               \
        \        [w-right-1 (W (max x (+ sr-prev 1)) (min (+ x d) nx))]\n          \
        \             [new-dp1 (max (+ dp0 w-right-0) (+ dp1 w-right-1))])\n       \
        \           (loop (cdr rs) x d new-dp0 new-dp1))))))))"
      erlang: "-spec max_walls(Robots :: [integer()], Distance :: [integer()], Walls\
        \ :: [integer()]) -> integer().\nmax_walls(Robots, Distance, Walls) ->\n  SortedRobots\
        \ = lists:sort(lists:zip(Robots, Distance)),\n  SortedWalls = list_to_tuple(lists:sort(Walls)),\n\
        \  M = tuple_size(SortedWalls),\n  Xs = [X || {X, _} <- SortedRobots],\n  Ds\
        \ = [D || {_, D} <- SortedRobots],\n  NextXs = tl(Xs) ++ [2000000001],\n  Combined\
        \ = lists:zip3(Xs, Ds, NextXs),\n  [{X0, D0, NX0} | Rest] = Combined,\n  LB\
        \ = fun(A) ->\n    (fun Loop(Low, High) ->\n      if Low < High ->\n       \
        \ Mid = (Low + High) div 2,\n        if element(Mid + 1, SortedWalls) < A ->\
        \ Loop(Mid + 1, High);\n           true -> Loop(Low, Mid) end;\n        true\
        \ -> Low end\n     end)(0, M) end,\n  UB = fun(B) ->\n    (fun Loop(Low, High)\
        \ ->\n      if Low < High ->\n        Mid = (Low + High) div 2,\n        if\
        \ element(Mid + 1, SortedWalls) =< B -> Loop(Mid + 1, High);\n           true\
        \ -> Loop(Low, Mid) end;\n        true -> Low end\n     end)(0, M) end,\n  W\
        \ = fun(A, B) -> if A > B -> 0; true -> UB(B) - LB(A) end end,\n  DP0_0 = W(X0\
        \ - D0, X0),\n  DP1_0 = W(X0, erlang:min(X0 + D0, NX0)),\n  {FinalDP0, FinalDP1,\
        \ _, _} = lists:foldl(fun({X, D, NX}, {AccDP0, AccDP1, PX, PD}) ->\n    SR_Prev\
        \ = erlang:min(PX + PD, X),\n    SL_Curr = erlang:max(X - D, PX),\n    W_Left_0\
        \ = W(erlang:max(SL_Curr, PX + 1), X),\n    W_Left_1 = W(erlang:max(SL_Curr,\
        \ SR_Prev + 1), X),\n    NewDP0 = erlang:max(AccDP0 + W_Left_0, AccDP1 + W_Left_1),\n\
        \    W_Right_0 = W(X, erlang:min(X + D, NX)),\n    W_Right_1 = W(erlang:max(X,\
        \ SR_Prev + 1), erlang:min(X + D, NX)),\n    NewDP1 = erlang:max(AccDP0 + W_Right_0,\
        \ AccDP1 + W_Right_1),\n    {NewDP0, NewDP1, X, D}\n  end, {DP0_0, DP1_0, X0,\
        \ D0}, Rest),\n  erlang:max(FinalDP0, FinalDP1)."
      elixir: "defmodule Solution do\n  @spec max_walls(robots :: [integer], distance\
        \ :: [integer], walls :: [integer]) :: integer\n  def max_walls(robots, distance,\
        \ walls) do\n    robots_sorted = Enum.zip(robots, distance) |> Enum.sort()\n\
        \    xs = Enum.map(robots_sorted, &elem(&1, 0))\n    ds = Enum.map(robots_sorted,\
        \ &elem(&1, 1))\n    next_xs = tl(xs) ++ [2_000_000_001]\n    combined = Enum.zip([xs,\
        \ ds, next_xs])\n    walls_tuple = List.to_tuple(Enum.sort(walls))\n    m =\
        \ tuple_size(walls_tuple)\n    lb = fn val ->\n      (fn f, low, high ->\n \
        \       if low < high do\n          mid = div(low + high, 2)\n          if elem(walls_tuple,\
        \ mid) < val, do: f.(f, mid + 1, high), else: f.(f, low, mid)\n        else\
        \ low end\n      end).(fn f, low, high ->\n        if low < high do\n      \
        \    mid = div(low + high, 2)\n          if elem(walls_tuple, mid) < val, do:\
        \ f.(f, mid + 1, high), else: f.(f, low, mid)\n        else low end\n      end,\
        \ 0, m)\n    end\n    ub = fn val ->\n      (fn f, low, high ->\n        if\
        \ low < high do\n          mid = div(low + high, 2)\n          if elem(walls_tuple,\
        \ mid) <= val, do: f.(f, mid + 1, high), else: f.(f, low, mid)\n        else\
        \ low end\n      end).(fn f, low, high ->\n        if low < high do\n      \
        \    mid = div(low + high, 2)\n          if elem(walls_tuple, mid) <= val, do:\
        \ f.(f, mid + 1, high), else: f.(f, low, mid)\n        else low end\n      end,\
        \ 0, m)\n    end\n    w = fn a, b -> if a > b, do: 0, else: ub.(b) - lb.(a)\
        \ end\n    [{x0, d0, nx0} | rest] = combined\n    dp0 = w.(x0 - d0, x0)\n  \
        \  dp1 = w.(x0, min(x0 + d0, nx0))\n    {fdp0, fdp1, _, _} = Enum.reduce(rest,\
        \ {dp0, dp1, x0, d0}, fn {x, d, nx}, {adp0, adp1, px, pd} ->\n      sr_prev\
        \ = min(px + pd, x)\n      sl_curr = max(x - d, px)\n      w_l_0 = w.(max(sl_curr,\
        \ px + 1), x)\n      w_l_1 = w.(max(sl_curr, sr_prev + 1), x)\n      ndp0 =\
        \ max(adp0 + w_l_0, adp1 + w_l_1)\n      w_r_0 = w.(x, min(x + d, nx))\n   \
        \   w_r_1 = w.(max(x, sr_prev + 1), min(x + d, nx))\n      ndp1 = max(adp0 +\
        \ w_r_0, adp1 + w_r_1)\n      {ndp0, ndp1, x, d}\n    end)\n    max(fdp0, fdp1)\n\
        \  end\nend"
    approach: 'To maximize the number of unique walls destroyed, we first sort both
      the robots (along with their shooting distances) and the walls by their positions.
      A crucial observation is that a robot''s bullet stops immediately upon hitting
      another robot, meaning robot $i$ can only destroy walls in the range $(robots[i-1],
      robots[i+1])$. Specifically, if robot $i$ fires left, it covers a range limited
      by either its distance or $robots[i-1]+1$; if it fires right, the range is limited
      by its distance or $robots[i+1]-1$. The only possible overlap in destroyed walls
      between adjacent robots occurs when robot $i-1$ fires right and robot $i$ fires
      left, as both may target the same walls in the interval $(robots[i-1], robots[i])$.


      We utilize dynamic programming to find the optimal configuration. Let $dp[i][0]$
      be the maximum walls destroyed by robots $0 \dots i$ if robot $i$ fires left,
      and $dp[i][1]$ if it fires right. For $dp[i][1]$, robot $i$ is guaranteed to be
      disjoint from any walls destroyed by $i-1$ (regardless of $i-1$''s direction),
      so we simply add the wall count for robot $i$''s right range to $\max(dp[i-1][0],
      dp[i-1][1])$. For $dp[i][0]$, if $i-1$ fired left, the ranges are disjoint; if
      $i-1$ fired right, we must only count walls in robot $i$''s left range that were
      not already covered by robot $i-1$''s right range. Wall counts for any given range
      are efficiently computed using binary search (lower and upper bounds) on the sorted
      walls array.'
    time_complexity: O(N log N + M log M + N log M), where N is the number of robots
      and M is the number of walls. Sorting robots takes O(N log N), sorting walls takes
      O(M log M), and the DP process takes O(N) iterations, each performing a constant
      number of binary searches on the walls array in O(log M) time.
    space_complexity: O(N + M) to store the sorted walls array, an array of robot-distance
      pairs, and the DP transition variables.
    elapsed_time: 1474.7243876457214
    model: gemini-3-flash-preview
    generated_at: '2026-04-04 08:52:56 '
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

To maximize the number of unique walls destroyed, we first sort both the robots (along with their shooting distances) and the walls by their positions. A crucial observation is that a robot's bullet stops immediately upon hitting another robot, meaning robot $i$ can only destroy walls in the range $(robots[i-1], robots[i+1])$. Specifically, if robot $i$ fires left, it covers a range limited by either its distance or $robots[i-1]+1$; if it fires right, the range is limited by its distance or $robots[i+1]-1$. The only possible overlap in destroyed walls between adjacent robots occurs when robot $i-1$ fires right and robot $i$ fires left, as both may target the same walls in the interval $(robots[i-1], robots[i])$.

We utilize dynamic programming to find the optimal configuration. Let $dp[i][0]$ be the maximum walls destroyed by robots $0 \dots i$ if robot $i$ fires left, and $dp[i][1]$ if it fires right. For $dp[i][1]$, robot $i$ is guaranteed to be disjoint from any walls destroyed by $i-1$ (regardless of $i-1$'s direction), so we simply add the wall count for robot $i$'s right range to $\max(dp[i-1][0], dp[i-1][1])$. For $dp[i][0]$, if $i-1$ fired left, the ranges are disjoint; if $i-1$ fired right, we must only count walls in robot $i$'s left range that were not already covered by robot $i-1$'s right range. Wall counts for any given range are efficiently computed using binary search (lower and upper bounds) on the sorted walls array.

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
// Generation failed for C++
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
// Generation failed for Java
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
// Generation failed for Python
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
// Generation failed for Python3
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int compareRobots(const void* a, const void* b) {
    int p1 = *(int*)a, p2 = *(int*)b;
    return (p1 < p2) ? -1 : (p1 > p2 ? 1 : 0);
}
typedef struct { int pos, dist; } Robot;
int compareR(const void* a, const void* b) {
    Robot *r1 = (Robot*)a, *r2 = (Robot*)b;
    return (r1->pos < r2->pos) ? -1 : (r1->pos > r2->pos ? 1 : 0);
}
int compareW(const void* a, const void* b) {
    int w1 = *(int*)a, w2 = *(int*)b;
    return (w1 < w2) ? -1 : (w1 > w2 ? 1 : 0);
}
int lower_bound(int* arr, int size, int val) {
    int low = 0, high = size;
    while (low < high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] < val) low = mid + 1; else high = mid;
    }
    return low;
}
int upper_bound(int* arr, int size, int val) {
    int low = 0, high = size;
    while (low < high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] <= val) low = mid + 1; else high = mid;
    }
    return low;
}
int getS(int* walls, int size, int a, int b) {
    if (a > b) return 0;
    int i1 = lower_bound(walls, size, a), i2 = upper_bound(walls, size, b);
    return (i2 > i1) ? (i2 - i1) : 0;
}
int maxWalls(int* robots, int robotsSize, int* distance, int distanceSize, int* walls, int wallsSize) {
    Robot* r = (Robot*)malloc(robotsSize * sizeof(Robot));
    for (int i = 0; i < robotsSize; i++) { r[i].pos = robots[i]; r[i].dist = distance[i]; }
    qsort(r, robotsSize, sizeof(Robot), compareR);
    qsort(walls, wallsSize, sizeof(int), compareW);
    int p0 = 0, p1 = 0, pr_lim = 0;
    for (int i = 0; i < robotsSize; i++) {
        int ll = r[i].pos - r[i].dist;
        if (i > 0 && ll < r[i-1].pos + 1) ll = r[i-1].pos + 1;
        int rl = r[i].pos + r[i].dist;
        if (i < robotsSize - 1 && rl > r[i+1].pos - 1) rl = r[i+1].pos - 1;
        int sl = getS(walls, wallsSize, ll, r[i].pos), sr = getS(walls, wallsSize, r[i].pos, rl);
        int c0, c1;
        if (i == 0) { c0 = sl; c1 = sr; } else {
            c1 = (p0 > p1 ? p0 : p1) + sr;
            int o1 = p0 + sl, start2 = (ll > pr_lim + 1) ? ll : (pr_lim + 1);
            int o2 = p1 + getS(walls, wallsSize, start2, r[i].pos);
            c0 = (o1 > o2 ? o1 : o2);
        }
        p0 = c0; p1 = c1; pr_lim = rl;
    }
    free(r);
    return p0 > p1 ? p0 : p1;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    private int LowerBound(int[] arr, int val) {
        int low = 0, high = arr.Length;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (arr[mid] < val) low = mid + 1; else high = mid;
        }
        return low;
    }
    private int UpperBound(int[] arr, int val) {
        int low = 0, high = arr.Length;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (arr[mid] <= val) low = mid + 1; else high = mid;
        }
        return low;
    }
    private int GetS(int[] walls, int a, int b) {
        if (a > b) return 0;
        int i1 = LowerBound(walls, a), i2 = UpperBound(walls, b);
        return i2 > i1 ? i2 - i1 : 0;
    }
    public int MaxWalls(int[] robots, int[] distance, int[] walls) {
        int n = robots.Length;
        var r = new (int p, int d)[n];
        for (int i = 0; i < n; i++) r[i] = (robots[i], distance[i]);
        System.Array.Sort(r, (a, b) => a.p.CompareTo(b.p));
        System.Array.Sort(walls);
        int p0 = 0, p1 = 0, pr_lim = 0;
        for (int i = 0; i < n; i++) {
            int ll = Math.Max(r[i].p - r[i].d, i > 0 ? r[i-1].p + 1 : int.MinValue);
            int rl = Math.Min(r[i].p + r[i].d, i < n - 1 ? r[i+1].p - 1 : int.MaxValue);
            int sl = GetS(walls, ll, r[i].p), sr = GetS(walls, r[i].p, rl);
            int c0, c1;
            if (i == 0) { c0 = sl; c1 = sr; } else {
                c1 = Math.Max(p0, p1) + sr;
                c0 = Math.Max(p0 + sl, p1 + GetS(walls, Math.Max(ll, pr_lim + 1), r[i].p));
            }
            p0 = c0; p1 = c1; pr_lim = rl;
        }
        return Math.Max(p0, p1);
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
    let r = robots.map((p, i) => ({p, d: distance[i]})).sort((a, b) => a.p - b.p);
    walls.sort((a, b) => a - b);
    const lb = (val) => {
        let low = 0, high = walls.length;
        while (low < high) {
            let mid = (low + high) >>> 1;
            if (walls[mid] < val) low = mid + 1; else high = mid;
        }
        return low;
    };
    const ub = (val) => {
        let low = 0, high = walls.length;
        while (low < high) {
            let mid = (low + high) >>> 1;
            if (walls[mid] <= val) low = mid + 1; else high = mid;
        }
        return low;
    };
    const getS = (a, b) => {
        if (a > b) return 0;
        let i1 = lb(a), i2 = ub(b);
        return i2 > i1 ? i2 - i1 : 0;
    };
    let p0 = 0, p1 = 0, pr_lim = 0;
    for (let i = 0; i < n; i++) {
        let ll = Math.max(r[i].p - r[i].d, i > 0 ? r[i-1].p + 1 : -2e9);
        let rl = Math.min(r[i].p + r[i].d, i < n - 1 ? r[i+1].p - 1 : 2e9);
        let sl = getS(ll, r[i].p), sr = getS(r[i].p, rl);
        let c0, c1;
        if (i === 0) {
            c0 = sl; c1 = sr;
        } else {
            c1 = Math.max(p0, p1) + sr;
            c0 = Math.max(p0 + sl, p1 + getS(Math.max(ll, pr_lim + 1), r[i].p));
        }
        p0 = c0; p1 = c1; pr_lim = rl;
    }
    return Math.max(p0, p1);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxWalls(robots: number[], distance: number[], walls: number[]): number {
    const n = robots.length;
    const comb = robots.map((r, i) => [r, distance[i]]).sort((a, b) => a[0] - b[0]);
    const rPos = comb.map(x => x[0]);
    const rDist = comb.map(x => x[1]);
    walls.sort((a, b) => a - b);
    const m = walls.length;

    const lowerBound = (target: number) => {
        let l = 0, r = m;
        while (l < r) {
            let mid = (l + r) >>> 1;
            if (walls[mid] < target) l = mid + 1; else r = mid;
        }
        return l;
    };
    const upperBound = (target: number) => {
        let l = 0, r = m;
        while (l < r) {
            let mid = (l + r) >>> 1;
            if (walls[mid] <= target) l = mid + 1; else r = mid;
        }
        return l;
    };
    const countInRange = (min: number, max: number) => {
        if (min > max) return 0;
        return upperBound(max) - lowerBound(min);
    };
    const hasWall = (pos: number) => {
        const idx = lowerBound(pos);
        return (idx < m && walls[idx] === pos) ? 1 : 0;
    };

    let prevL = countInRange(rPos[0] - rDist[0], rPos[0]);
    let prevR = countInRange(rPos[0], n > 1 ? Math.min(rPos[1], rPos[0] + rDist[0]) : rPos[0] + rDist[0]);

    for (let i = 1; i < n; i++) {
        const Li = countInRange(Math.max(rPos[i - 1], rPos[i] - rDist[i]), rPos[i]);
        const Ri = countInRange(rPos[i], i < n - 1 ? Math.min(rPos[i + 1], rPos[i] + rDist[i]) : rPos[i] + rDist[i]);
        const overlapLL = (rPos[i] - rDist[i] <= rPos[i - 1]) ? hasWall(rPos[i - 1]) : 0;
        const overlapRR = (rPos[i - 1] + rDist[i - 1] >= rPos[i]) ? hasWall(rPos[i]) : 0;
        const overlapRL = countInRange(Math.max(rPos[i - 1], rPos[i] - rDist[i]), Math.min(rPos[i], rPos[i - 1] + rDist[i - 1]));

        const currL = Math.max(prevL + Li - overlapLL, prevR + Li - overlapRL);
        const currR = Math.max(prevL + Ri, prevR + Ri - overlapRR);
        prevL = currL;
        prevR = currR;
    }
    return Math.max(prevL, prevR);
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
        $r_pos = $robots;
        $r_dist = $distance;
        array_multisort($r_pos, SORT_ASC, SORT_NUMERIC, $r_dist);
        sort($walls, SORT_NUMERIC);
        $m = count($walls);

        $lowerBound = function($target) use ($walls, $m) {
            $l = 0; $r = $m;
            while ($l < $r) {
                $mid = $l + (int)(($r - $l) / 2);
                if ($walls[$mid] < $target) $l = $mid + 1;
                else $r = $mid;
            }
            return $l;
        };
        $upperBound = function($target) use ($walls, $m) {
            $l = 0; $r = $m;
            while ($l < $r) {
                $mid = $l + (int)(($r - $l) / 2);
                if ($walls[$mid] <= $target) $l = $mid + 1;
                else $r = $mid;
            }
            return $l;
        };
        $countInRange = function($minV, $maxV) use ($lowerBound, $upperBound) {
            if ($minV > $maxV) return 0;
            return $upperBound($maxV) - $lowerBound($minV);
        };
        $hasWall = function($pos) use ($walls, $m, $lowerBound) {
            $idx = $lowerBound($pos);
            return ($idx < $m && $walls[$idx] == $pos) ? 1 : 0;
        };

        $prevL = $countInRange($r_pos[0] - $r_dist[0], $r_pos[0]);
        $prevR = $countInRange($r_pos[0], $n > 1 ? min($r_pos[1], $r_pos[0] + $r_dist[0]) : $r_pos[0] + $r_dist[0]);

        for ($i = 1; $i < $n; $i++) {
            $Li = $countInRange(max($r_pos[$i-1], $r_pos[$i] - $r_dist[$i]), $r_pos[$i]);
            $Ri = $countInRange($r_pos[$i], ($i < $n - 1 ? min($r_pos[$i+1], $r_pos[$i] + $r_dist[$i]) : $r_pos[$i] + $r_dist[$i]));
            $overlapLL = ($r_pos[$i] - $r_dist[$i] <= $r_pos[$i-1]) ? $hasWall($r_pos[$i-1]) : 0;
            $overlapRR = ($r_pos[$i-1] + $r_dist[$i-1] >= $r_pos[$i]) ? $hasWall($r_pos[$i]) : 0;
            $overlapRL = $countInRange(max($r_pos[$i-1], $r_pos[$i] - $r_dist[$i]), min($r_pos[$i], $r_pos[$i-1] + $r_dist[$i-1]));
            $currL = max($prevL + $Li - $overlapLL, $prevR + $Li - $overlapRL);
            $currR = max($prevL + $Ri, $prevR + $Ri - $overlapRR);
            $prevL = $currL;
            $prevR = $currR;
        }
        return max($prevL, $prevR);
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
        var robotsWithDist = [(Int, Int)]()
        for i in 0..<n {
            robotsWithDist.append((robots[i], distance[i]))
        }
        robotsWithDist.sort { $0.0 < $1.0 }
        let rPos = robotsWithDist.map { $0.0 }
        let rDist = robotsWithDist.map { $0.1 }
        let sortedWalls = walls.sorted()
        let m = sortedWalls.count

        func lowerBound(_ target: Int) -> Int {
            var l = 0, r = m
            while l < r {
                let mid = l + (r - l) / 2
                if sortedWalls[mid] < target { l = mid + 1 } else { r = mid }
            }
            return l
        }
        func upperBound(_ target: Int) -> Int {
            var l = 0, r = m
            while l < r {
                let mid = l + (r - l) / 2
                if sortedWalls[mid] <= target { l = mid + 1 } else { r = mid }
            }
            return l
        }
        func countInRange(_ minV: Int, _ maxV: Int) -> Int {
            if minV > maxV { return 0 }
            return upperBound(maxV) - lowerBound(minV)
        }
        func hasWall(_ pos: Int) -> Int {
            let idx = lowerBound(pos)
            return (idx < m && sortedWalls[idx] == pos) ? 1 : 0
        }

        var prevL = countInRange(rPos[0] - rDist[0], rPos[0])
        var prevR = countInRange(rPos[0], n > 1 ? min(rPos[1], rPos[0] + rDist[0]) : rPos[0] + rDist[0])

        if n > 1 {
            for i in 1..<n {
                let Li = countInRange(max(rPos[i-1], rPos[i] - rDist[i]), rPos[i])
                let Ri = countInRange(rPos[i], i < n - 1 ? min(rPos[i+1], rPos[i] + rDist[i]) : rPos[i] + rDist[i])
                let overlapLL = (rPos[i] - rDist[i] <= rPos[i-1]) ? hasWall(rPos[i-1]) : 0
                let overlapRR = (rPos[i-1] + rDist[i-1] >= rPos[i]) ? hasWall(rPos[i]) : 0
                let overlapRL = countInRange(max(rPos[i-1], rPos[i] - rDist[i]), min(rPos[i], rPos[i-1] + rDist[i-1]))
                let currL = max(prevL + Li - overlapLL, prevR + Li - overlapRL)
                let currR = max(prevL + Ri, prevR + Ri - overlapRR)
                prevL = currL
                prevR = currR
            }
        }
        return max(prevL, prevR)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import java.util.*

class Solution {
    fun maxWalls(robots: IntArray, distance: IntArray, walls: IntArray): Int {
        val n = robots.size
        val idx = (0 until n).sortedBy { robots[it] }
        val sortedR = IntArray(n) { robots[idx[it]] }
        val sortedD = IntArray(n) { distance[idx[it]] }
        walls.sort()

        fun lowerBound(a: IntArray, target: Int): Int {
            var low = 0
            var high = a.size
            while (low < high) {
                val mid = low + (high - low) / 2
                if (a[mid] >= target) high = mid else low = mid + 1
            }
            return low
        }

        fun countInRange(a: Int, b: Int): Int {
            if (a > b) return 0
            return lowerBound(walls, b + 1) - lowerBound(walls, a)
        }

        fun hasWall(pos: Int): Boolean {
            val i = lowerBound(walls, pos)
            return i < walls.size && walls[i] == pos
        }

        var p0 = countInRange(sortedR[0] - sortedD[0], sortedR[0]).toLong()
        val r1 = if (n > 1) sortedR[1] else 2100000000
        var p1 = countInRange(sortedR[0], minOf(sortedR[0] + sortedD[0], r1)).toLong()

        for (i in 1 until n) {
            val rPrev = sortedR[i - 1]
            val rNext = if (i < n - 1) sortedR[i + 1] else 2100000000
            val cl = countInRange(maxOf(sortedR[i] - sortedD[i], rPrev), sortedR[i])
            val cr = countInRange(sortedR[i], minOf(sortedR[i] + sortedD[i], rNext))
            val overRL = countInRange(maxOf(rPrev, sortedR[i] - sortedD[i]), minOf(rPrev + sortedD[i - 1], sortedR[i]))
            val wallAtRprev = if (hasWall(rPrev) && (sortedR[i] - sortedD[i] <= rPrev)) 1 else 0
            val wallAtRi = if (hasWall(sortedR[i]) && (rPrev + sortedD[i - 1] >= sortedR[i])) 1 else 0

            val next0 = maxOf(p0 + cl - wallAtRprev, p1 + cl - overRL)
            val next1 = maxOf(p0 + cr, p1 + cr - wallAtRi)
            p0 = next0
            p1 = next1
        }

        return maxOf(p0, p1).toInt()
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
  int maxWalls(List<int> robots, List<int> distance, List<int> walls) {
    int n = robots.length;
    List<int> idx = List.generate(n, (i) => i);
    idx.sort((a, b) => robots[a].compareTo(robots[b]));
    List<int> sortedR = idx.map((i) => robots[i]).toList();
    List<int> sortedD = idx.map((i) => distance[i]).toList();
    walls.sort();

    int lowerBound(List<int> a, int target) {
      int low = 0, high = a.length;
      while (low < high) {
        int mid = (low + high) ~/ 2;
        if (a[mid] >= target) high = mid; else low = mid + 1;
      }
      return low;
    }

    int countInRange(int a, int b) {
      if (a > b) return 0;
      return lowerBound(walls, b + 1) - lowerBound(walls, a);
    }

    bool hasWall(int pos) {
      int i = lowerBound(walls, pos);
      return i < walls.length && walls[i] == pos;
    }

    int r1 = n > 1 ? sortedR[1] : 2100000000;
    int p0 = countInRange(sortedR[0] - sortedD[0], sortedR[0]);
    int p1 = countInRange(sortedR[0], min(sortedR[0] + sortedD[0], r1));

    for (int i = 1; i < n; i++) {
      int rPrev = sortedR[i - 1];
      int rNext = i < n - 1 ? sortedR[i + 1] : 2100000000;
      int cl = countInRange(max(sortedR[i] - sortedD[i], rPrev), sortedR[i]);
      int cr = countInRange(sortedR[i], min(sortedR[i] + sortedD[i], rNext));
      int overRL = countInRange(max(rPrev, sortedR[i] - sortedD[i]), min(rPrev + sortedD[i - 1], sortedR[i]));
      int wallAtRprev = (hasWall(rPrev) && (sortedR[i] - sortedD[i] <= rPrev)) ? 1 : 0;
      int wallAtRi = (hasWall(sortedR[i]) && (rPrev + sortedD[i - 1] >= sortedR[i])) ? 1 : 0;

      int next0 = max(p0 + cl - wallAtRprev, p1 + cl - overRL);
      int next1 = max(p0 + cr, p1 + cr - wallAtRi);
      p0 = next0;
      p1 = next1;
    }

    return max(p0, p1);
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

func maxWalls(robots []int, distance []int, walls []int) int {
	sort.Ints(walls)
	n := len(robots)
	type robot struct{ pos, dist int }
	rList := make([]robot, n)
	for i := range robots {
		rList[i] = robot{robots[i], distance[i]}
	}
	sort.Slice(rList, func(i, j int) bool { return rList[i].pos < rList[j].pos })
	sortedR := make([]int, n)
	sortedD := make([]int, n)
	for i := range rList {
		sortedR[i], sortedD[i] = rList[i].pos, rList[i].dist
	}

	count := func(a, b int) int {
		if a > b { return 0 }
		return sort.SearchInts(walls, b+1) - sort.SearchInts(walls, a)
	}
	hasWall := func(pos int) bool {
		i := sort.SearchInts(walls, pos)
		return i < len(walls) && walls[i] == pos
	}
	max64 := func(a, b int64) int64 {
		if a > b { return a }
		return b
	}
	min := func(a, b int) int {
		if a < b { return a }
		return b
	}
	max := func(a, b int) int {
		if a > b { return a }
		return b
	}

	r1 := 2100000000
	if n > 1 { r1 = sortedR[1] }
	p0 := int64(count(sortedR[0]-sortedD[0], sortedR[0]))
	p1 := int64(count(sortedR[0], min(sortedR[0]+sortedD[0], r1)))

	for i := 1; i < n; i++ {
		rPrev, rNext := sortedR[i-1], 2100000000
		if i < n-1 { rNext = sortedR[i+1] }
		cl := int64(count(max(sortedR[i]-sortedD[i], rPrev), sortedR[i]))
		cr := int64(count(sortedR[i], min(sortedR[i]+sortedD[i], rNext)))
		overRL := int64(count(max(rPrev, sortedR[i]-sortedD[i]), min(rPrev+sortedD[i-1], sortedR[i])))
		wallAtRprev := int64(0)
		if hasWall(rPrev) && sortedR[i]-sortedD[i] <= rPrev { wallAtRprev = 1 }
		wallAtRi := int64(0)
		if hasWall(sortedR[i]) && rPrev+sortedD[i-1] >= sortedR[i] { wallAtRi = 1 }

		next0 := max64(p0+cl-wallAtRprev, p1+cl-overRL)
		next1 := max64(p0+cr, p1+cr-wallAtRi)
		p0, p1 = next0, next1
	}
	return int(max64(p0, p1))
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def max_walls(robots, distance, walls)
  n = robots.size
  m = walls.size
  walls.sort!
  r_sorted = robots.zip(distance).sort_by(&:first)

  def lower_bound(walls, val)
    walls.bsearch_index { |w| w >= val } || walls.size
  end

  def upper_bound(walls, val)
    walls.bsearch_index { |w| w > val } || walls.size
  end

  def get_counts(walls, x_prev, d_prev, x_curr, d_curr)
    a = lower_bound(walls, x_prev + 1)
    b = lower_bound(walls, x_curr) - 1
    return [0, 0, 0] if a > b

    p_end = upper_bound(walls, x_prev + d_prev) - 1
    q_start = lower_bound(walls, x_curr - d_curr)

    p_end_eff = [p_end, b].min
    q_start_eff = [q_start, a].max

    cp = [0, p_end_eff - a + 1].max
    cq = [0, b - q_start_eff + 1].max

    if p_end_eff < a
      cpuq = cq
    elsif q_start_eff > b
      cpuq = cp
    elsif p_end_eff >= q_start_eff - 1
      cpuq = b - a + 1
    else
      cpuq = cp + cq
    end
    [cp, cq, cpuq]
  end

  dp = Array.new(n) { [0, 0] }
  b0 = lower_bound(walls, r_sorted[0][0]) - 1
  q_start0 = lower_bound(walls, r_sorted[0][0] - r_sorted[0][1])
  dp[0][0] = [0, b0 - q_start0 + 1].max
  dp[0][1] = 0

  (1...n).each do |i|
    cp, cq, cpuq = get_counts(walls, r_sorted[i-1][0], r_sorted[i-1][1], r_sorted[i][0], r_sorted[i][1])
    dp[i][0] = [dp[i-1][0] + cq, dp[i-1][1] + cpuq].max
    dp[i][1] = [dp[i-1][0], dp[i-1][1] + cp].max
  end

  an = lower_bound(walls, r_sorted[n-1][0] + 1)
  bn = m - 1
  p_end_n = upper_bound(walls, r_sorted[n-1][0] + r_sorted[n-1][1]) - 1
  count_pn = [0, [p_end_n, bn].min - an + 1].max

  total_walls_at_robots = 0
  r_sorted.each do |x, _|
    idx = lower_bound(walls, x)
    total_walls_at_robots += 1 if idx < m && walls[idx] == x
  end

  [dp[n-1][0], dp[n-1][1] + count_pn].max + total_walls_at_robots
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
        val sortedWalls = walls.sorted
        val rSorted = robots.zip(distance).sortBy(_._1)

        def lowerBound(a: Array[Int], v: Int): Int = {
            var low = 0; var high = a.length
            while (low < high) {
                val mid = low + (high - low) / 2
                if (a(mid) < v) low = mid + 1 else high = mid
            }
            low
        }

        def upperBound(a: Array[Int], v: Int): Int = {
            var low = 0; var high = a.length
            while (low < high) {
                val mid = low + (high - low) / 2
                if (a(mid) <= v) low = mid + 1 else high = mid
            }
            low
        }

        val dp = Array.fill(n, 2)(0)
        val b0 = lowerBound(sortedWalls, rSorted(0)._1) - 1
        val qStart0 = lowerBound(sortedWalls, rSorted(0)._1 - rSorted(0)._2)
        dp(0)(0) = Math.max(0, b0 - qStart0 + 1)
        dp(0)(1) = 0

        for (i <- 1 until n) {
            val xPrev = rSorted(i-1)._1
            val dPrev = rSorted(i-1)._2
            val xCurr = rSorted(i)._1
            val dCurr = rSorted(i)._2

            val a = lowerBound(sortedWalls, xPrev + 1)
            val b = lowerBound(sortedWalls, xCurr) - 1
            var cp = 0; var cq = 0; var cpuq = 0

            if (a <= b) {
                val pEnd = upperBound(sortedWalls, xPrev + dPrev) - 1
                val qStart = lowerBound(sortedWalls, xCurr - dCurr)
                val pEndEff = Math.min(pEnd, b)
                val qStartEff = Math.max(qStart, a)
                cp = Math.max(0, pEndEff - a + 1)
                cq = Math.max(0, b - qStartEff + 1)
                if (pEndEff < a) cpuq = cq
                else if (qStartEff > b) cpuq = cp
                else if (pEndEff >= qStartEff - 1) cpuq = b - a + 1
                else cpuq = cp + cq
            }
            dp(i)(0) = Math.max(dp(i-1)(0) + cq, dp(i-1)(1) + cpuq)
            dp(i)(1) = Math.max(dp(i-1)(0), dp(i-1)(1) + cp)
        }

        val an = lowerBound(sortedWalls, rSorted(n-1)._1 + 1)
        val bn = sortedWalls.length - 1
        val pEndN = upperBound(sortedWalls, rSorted(n-1)._1 + rSorted(n-1)._2) - 1
        val countPn = Math.max(0, Math.min(pEndN, bn) - an + 1)

        var totalAtRobots = 0
        for (r <- rSorted) {
            val idx = lowerBound(sortedWalls, r._1)
            if (idx < sortedWalls.length && sortedWalls(idx) == r._1) totalAtRobots += 1
        }

        Math.max(dp(n-1)(0), dp(n-1)(1) + countPn) + totalAtRobots
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
        let n = robots.len();
        let mut sorted_walls = walls;
        sorted_walls.sort();
        let mut r_sorted: Vec<(i32, i32)> = robots.into_iter().zip(distance.into_iter()).collect();
        r_sorted.sort_by_key(|r| r.0);

        let mut dp = vec![[0i32; 2]; n];
        let b0 = sorted_walls.partition_point(|&w| w < r_sorted[0].0) as i32 - 1;
        let q_start0 = sorted_walls.partition_point(|&w| w < r_sorted[0].0 - r_sorted[0].1) as i32;
        dp[0][0] = 0.max(b0 - q_start0 + 1);
        dp[0][1] = 0;

        for i in 1..n {
            let (x_prev, d_prev) = r_sorted[i-1];
            let (x_curr, d_curr) = r_sorted[i];
            let a = sorted_walls.partition_point(|&w| w < x_prev + 1) as i32;
            let b = sorted_walls.partition_point(|&w| w < x_curr) as i32 - 1;
            let (mut cp, mut cq, mut cpuq) = (0, 0, 0);

            if a <= b {
                let p_end = sorted_walls.partition_point(|&w| w <= x_prev + d_prev) as i32 - 1;
                let q_start = sorted_walls.partition_point(|&w| w < x_curr - d_curr) as i32;
                let p_end_eff = p_end.min(b);
                let q_start_eff = q_start.max(a);
                cp = 0.max(p_end_eff - a + 1);
                cq = 0.max(b - q_start_eff + 1);
                if p_end_eff < a { cpuq = cq; }
                else if q_start_eff > b { cpuq = cp; }
                else if p_end_eff >= q_start_eff - 1 { cpuq = b - a + 1; }
                else { cpuq = cp + cq; }
            }
            dp[i][0] = (dp[i-1][0] + cq).max(dp[i-1][1] + cpuq);
            dp[i][1] = dp[i-1][0].max(dp[i-1][1] + cp);
        }

        let an = sorted_walls.partition_point(|&w| w < r_sorted[n-1].0 + 1) as i32;
        let bn = sorted_walls.len() as i32 - 1;
        let p_end_n = sorted_walls.partition_point(|&w| w <= r_sorted[n-1].0 + r_sorted[n-1].1) as i32 - 1;
        let count_pn = 0.max(p_end_n.min(bn) - an + 1);

        let mut total_at_robots = 0;
        for r in &r_sorted {
            let idx = sorted_walls.partition_point(|&w| w < r.0);
            if idx < sorted_walls.len() && sorted_walls[idx] == r.0 { total_at_robots += 1; }
        }

        dp[n-1][0].max(dp[n-1][1] + count_pn) + total_at_robots
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
         [robots-dist (sort (map list robots distance) < #:key car)]
         [sorted-walls (list->vector (sort walls <))]
         [m (vector-length sorted-walls)])
    (define (lb val)
      (let loop ([low 0] [high m])
        (if (< low high)
            (let ([mid (quotient (+ low high) 2)])
              (if (< (vector-ref sorted-walls mid) val)
                  (loop (+ mid 1) high)
                  (loop low mid)))
            low)))
    (define (ub val)
      (let loop ([low 0] [high m])
        (if (< low high)
            (let ([mid (quotient (+ low high) 2)])
              (if (<= (vector-ref sorted-walls mid) val)
                  (loop (+ mid 1) high)
                  (loop low mid)))
            low)))
    (define (W a b)
      (if (> a b) 0 (- (ub b) (lb a))))
    (let loop ([rs robots-dist] [px -1] [pd -1] [dp0 0] [dp1 0])
      (if (null? rs)
          (max dp0 dp1)
          (let* ([curr (car rs)]
                 [x (car curr)]
                 [d (cadr curr)]
                 [nx (if (null? (cdr rs)) 2000000001 (car (cadr rs)))])
            (if (= px -1)
                (loop (cdr rs) x d (W (- x d) x) (W x (min (+ x d) nx)))
                (let* ([sr-prev (min (+ px pd) x)]
                       [sl-curr (max (- x d) px)]
                       [w-left-0 (W (max sl-curr (+ px 1)) x)]
                       [w-left-1 (W (max sl-curr (+ sr-prev 1)) x)]
                       [new-dp0 (max (+ dp0 w-left-0) (+ dp1 w-left-1))]
                       [w-right-0 (W x (min (+ x d) nx))]
                       [w-right-1 (W (max x (+ sr-prev 1)) (min (+ x d) nx))]
                       [new-dp1 (max (+ dp0 w-right-0) (+ dp1 w-right-1))])
                  (loop (cdr rs) x d new-dp0 new-dp1))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_walls(Robots :: [integer()], Distance :: [integer()], Walls :: [integer()]) -> integer().
max_walls(Robots, Distance, Walls) ->
  SortedRobots = lists:sort(lists:zip(Robots, Distance)),
  SortedWalls = list_to_tuple(lists:sort(Walls)),
  M = tuple_size(SortedWalls),
  Xs = [X || {X, _} <- SortedRobots],
  Ds = [D || {_, D} <- SortedRobots],
  NextXs = tl(Xs) ++ [2000000001],
  Combined = lists:zip3(Xs, Ds, NextXs),
  [{X0, D0, NX0} | Rest] = Combined,
  LB = fun(A) ->
    (fun Loop(Low, High) ->
      if Low < High ->
        Mid = (Low + High) div 2,
        if element(Mid + 1, SortedWalls) < A -> Loop(Mid + 1, High);
           true -> Loop(Low, Mid) end;
        true -> Low end
     end)(0, M) end,
  UB = fun(B) ->
    (fun Loop(Low, High) ->
      if Low < High ->
        Mid = (Low + High) div 2,
        if element(Mid + 1, SortedWalls) =< B -> Loop(Mid + 1, High);
           true -> Loop(Low, Mid) end;
        true -> Low end
     end)(0, M) end,
  W = fun(A, B) -> if A > B -> 0; true -> UB(B) - LB(A) end end,
  DP0_0 = W(X0 - D0, X0),
  DP1_0 = W(X0, erlang:min(X0 + D0, NX0)),
  {FinalDP0, FinalDP1, _, _} = lists:foldl(fun({X, D, NX}, {AccDP0, AccDP1, PX, PD}) ->
    SR_Prev = erlang:min(PX + PD, X),
    SL_Curr = erlang:max(X - D, PX),
    W_Left_0 = W(erlang:max(SL_Curr, PX + 1), X),
    W_Left_1 = W(erlang:max(SL_Curr, SR_Prev + 1), X),
    NewDP0 = erlang:max(AccDP0 + W_Left_0, AccDP1 + W_Left_1),
    W_Right_0 = W(X, erlang:min(X + D, NX)),
    W_Right_1 = W(erlang:max(X, SR_Prev + 1), erlang:min(X + D, NX)),
    NewDP1 = erlang:max(AccDP0 + W_Right_0, AccDP1 + W_Right_1),
    {NewDP0, NewDP1, X, D}
  end, {DP0_0, DP1_0, X0, D0}, Rest),
  erlang:max(FinalDP0, FinalDP1).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_walls(robots :: [integer], distance :: [integer], walls :: [integer]) :: integer
  def max_walls(robots, distance, walls) do
    robots_sorted = Enum.zip(robots, distance) |> Enum.sort()
    xs = Enum.map(robots_sorted, &elem(&1, 0))
    ds = Enum.map(robots_sorted, &elem(&1, 1))
    next_xs = tl(xs) ++ [2_000_000_001]
    combined = Enum.zip([xs, ds, next_xs])
    walls_tuple = List.to_tuple(Enum.sort(walls))
    m = tuple_size(walls_tuple)
    lb = fn val ->
      (fn f, low, high ->
        if low < high do
          mid = div(low + high, 2)
          if elem(walls_tuple, mid) < val, do: f.(f, mid + 1, high), else: f.(f, low, mid)
        else low end
      end).(fn f, low, high ->
        if low < high do
          mid = div(low + high, 2)
          if elem(walls_tuple, mid) < val, do: f.(f, mid + 1, high), else: f.(f, low, mid)
        else low end
      end, 0, m)
    end
    ub = fn val ->
      (fn f, low, high ->
        if low < high do
          mid = div(low + high, 2)
          if elem(walls_tuple, mid) <= val, do: f.(f, mid + 1, high), else: f.(f, low, mid)
        else low end
      end).(fn f, low, high ->
        if low < high do
          mid = div(low + high, 2)
          if elem(walls_tuple, mid) <= val, do: f.(f, mid + 1, high), else: f.(f, low, mid)
        else low end
      end, 0, m)
    end
    w = fn a, b -> if a > b, do: 0, else: ub.(b) - lb.(a) end
    [{x0, d0, nx0} | rest] = combined
    dp0 = w.(x0 - d0, x0)
    dp1 = w.(x0, min(x0 + d0, nx0))
    {fdp0, fdp1, _, _} = Enum.reduce(rest, {dp0, dp1, x0, d0}, fn {x, d, nx}, {adp0, adp1, px, pd} ->
      sr_prev = min(px + pd, x)
      sl_curr = max(x - d, px)
      w_l_0 = w.(max(sl_curr, px + 1), x)
      w_l_1 = w.(max(sl_curr, sr_prev + 1), x)
      ndp0 = max(adp0 + w_l_0, adp1 + w_l_1)
      w_r_0 = w.(x, min(x + d, nx))
      w_r_1 = w.(max(x, sr_prev + 1), min(x + d, nx))
      ndp1 = max(adp0 + w_r_0, adp1 + w_r_1)
      {ndp0, ndp1, x, d}
    end)
    max(fdp0, fdp1)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N log N + M log M + N log M), where N is the number of robots and M is the number of walls. Sorting robots takes O(N log N), sorting walls takes O(M log M), and the DP process takes O(N) iterations, each performing a constant number of binary searches on the walls array in O(log M) time.
- **Space Complexity:** O(N + M) to store the sorted walls array, an array of robot-distance pairs, and the DP transition variables.
