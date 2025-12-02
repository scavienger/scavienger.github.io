---
layout: post
title: "Count Number of Trapezoids I"
date: 2025-12-02 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Math", "Geometry"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/count-number-of-trapezoids-i/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int countTrapezoids(std::vector<std::vector<int>>&\
        \ points) {\n        long long MOD = 1e9 + 7;\n\n        std::map<int, std::vector<int>>\
        \ y_to_x_coords;\n        for (const auto& point : points) {\n            y_to_x_coords[point[1]].push_back(point[0]);\n\
        \        }\n\n        long long sum_C_n_2 = 0;\n        long long sum_C_n_2_sq\
        \ = 0;\n\n        for (const auto& pair : y_to_x_coords) {\n            long\
        \ long n = pair.second.size();\n            if (n >= 2) {\n                long\
        \ long c_n_2 = (n * (n - 1) / 2) % MOD;\n\n                sum_C_n_2 = (sum_C_n_2\
        \ + c_n_2) % MOD;\n                sum_C_n_2_sq = (sum_C_n_2_sq + (c_n_2 * c_n_2)\
        \ % MOD) % MOD;\n            }\n        }\n\n        long long total_trapezoids\
        \ = (sum_C_n_2 * sum_C_n_2) % MOD;\n        total_trapezoids = (total_trapezoids\
        \ - sum_C_n_2_sq + MOD) % MOD;\n\n        long long inv2 = 500000004; // (MOD\
        \ + 1) / 2\n\n        total_trapezoids = (total_trapezoids * inv2) % MOD;\n\n\
        \        return static_cast<int>(total_trapezoids);\n    }\n};"
      java: "import java.util.HashMap;\nimport java.util.List;\nimport java.util.ArrayList;\n\
        import java.util.Map;\n\nclass Solution {\n    public int countTrapezoids(List<List<Integer>>\
        \ points) {\n        long MOD = 1_000_000_007;\n\n        Map<Integer, List<Integer>>\
        \ yToXCoords = new HashMap<>();\n        for (List<Integer> point : points)\
        \ {\n            int x = point.get(0);\n            int y = point.get(1);\n\
        \            yToXCoords.computeIfAbsent(y, k -> new ArrayList<>()).add(x);\n\
        \        }\n\n        long sumCn2 = 0;\n        long sumCn2Sq = 0;\n\n     \
        \   for (List<Integer> xCoords : yToXCoords.values()) {\n            long n\
        \ = xCoords.size();\n            if (n >= 2) {\n                long cn2 = (n\
        \ * (n - 1) / 2) % MOD;\n\n                sumCn2 = (sumCn2 + cn2) % MOD;\n\
        \                sumCn2Sq = (sumCn2Sq + (cn2 * cn2) % MOD) % MOD;\n        \
        \    }\n        }\n\n        long totalTrapezoids = (sumCn2 * sumCn2) % MOD;\n\
        \        totalTrapezoids = (totalTrapezoids - sumCn2Sq + MOD) % MOD;\n\n   \
        \     long inv2 = 500000004; // (MOD + 1) / 2\n\n        totalTrapezoids = (totalTrapezoids\
        \ * inv2) % MOD;\n\n        return (int) totalTrapezoids;\n    }\n}"
      python: "import collections\n\nclass Solution:\n    def countTrapezoids(self,\
        \ points: List[List[int]]) -> int:\n        MOD = 10**9 + 7\n\n        y_to_x_coords\
        \ = collections.defaultdict(list)\n        for x, y in points:\n           \
        \ y_to_x_coords[y].append(x)\n\n        sum_C_n_2 = 0\n        sum_C_n_2_sq\
        \ = 0\n\n        for y in y_to_x_coords:\n            n = len(y_to_x_coords[y])\n\
        \            if n >= 2:\n                c_n_2 = (n * (n - 1) // 2) % MOD\n\n\
        \                sum_C_n_2 = (sum_C_n_2 + c_n_2) % MOD\n                sum_C_n_2_sq\
        \ = (sum_C_n_2_sq + (c_n_2 * c_n_2) % MOD) % MOD\n\n        total_trapezoids\
        \ = (sum_C_n_2 * sum_C_n_2) % MOD\n        total_trapezoids = (total_trapezoids\
        \ - sum_C_n_2_sq + MOD) % MOD\n\n        inv2 = pow(2, MOD - 2, MOD)\n     \
        \   total_trapezoids = (total_trapezoids * inv2) % MOD\n\n        return total_trapezoids"
      python3: "import collections\n\nclass Solution:\n    def countTrapezoids(self,\
        \ points: List[List[int]]) -> int:\n        MOD = 10**9 + 7\n\n        y_to_x_coords\
        \ = collections.defaultdict(list)\n        for x, y in points:\n           \
        \ y_to_x_coords[y].append(x)\n\n        sum_C_n_2 = 0\n        sum_C_n_2_sq\
        \ = 0\n\n        for y in y_to_x_coords:\n            n = len(y_to_x_coords[y])\n\
        \            if n >= 2:\n                c_n_2 = (n * (n - 1) // 2) % MOD\n\n\
        \                sum_C_n_2 = (sum_C_n_2 + c_n_2) % MOD\n                sum_C_n_2_sq\
        \ = (sum_C_n_2_sq + (c_n_2 * c_n_2) % MOD) % MOD\n\n        total_trapezoids\
        \ = (sum_C_n_2 * sum_C_n_2) % MOD\n        total_trapezoids = (total_trapezoids\
        \ - sum_C_n_2_sq + MOD) % MOD\n\n        inv2 = pow(2, MOD - 2, MOD)\n     \
        \   total_trapezoids = (total_trapezoids * inv2) % MOD\n\n        return total_trapezoids"
      c: "#include <stdlib.h>\n#include <stdio.h>\n\ntypedef struct {\n    int x;\n\
        \    int y;\n} Point;\n\nint comparePoints(const void *a, const void *b) {\n\
        \    Point *pa = (Point *)a;\n    Point *pb = (Point *)b;\n    if (pa->y !=\
        \ pb->y) {\n        return pa->y - pb->y;\n    }\n    return pa->x - pb->x;\n\
        }\n\nlong long power(long long base, long long exp) {\n    long long res = 1;\n\
        \    long long MOD = 1000000007;\n    base %= MOD;\n    while (exp > 0) {\n\
        \        if (exp % 2 == 1) res = (res * base) % MOD;\n        base = (base *\
        \ base) % MOD;\n        exp /= 2;\n    }\n    return res;\n}\n\nint countTrapezoids(int**\
        \ points, int pointsSize, int* pointsColSize) {\n    long long MOD = 1000000007;\n\
        \n    Point* pts = (Point*)malloc(pointsSize * sizeof(Point));\n    if (pts\
        \ == NULL) {\n        return 0; \n    }\n    for (int i = 0; i < pointsSize;\
        \ ++i) {\n        pts[i].x = points[i][0];\n        pts[i].y = points[i][1];\n\
        \    }\n\n    qsort(pts, pointsSize, sizeof(Point), comparePoints);\n\n    long\
        \ long sum_C_n_2 = 0;\n    long long sum_C_n_2_sq = 0;\n\n    int i = 0;\n \
        \   while (i < pointsSize) {\n        int current_y = pts[i].y;\n        long\
        \ long count_on_current_y = 0;\n        int j = i;\n        while (j < pointsSize\
        \ && pts[j].y == current_y) {\n            count_on_current_y++;\n         \
        \   j++;\n        }\n\n        if (count_on_current_y >= 2) {\n            long\
        \ long c_n_2 = (count_on_current_y * (count_on_current_y - 1) / 2) % MOD;\n\n\
        \            sum_C_n_2 = (sum_C_n_2 + c_n_2) % MOD;\n            sum_C_n_2_sq\
        \ = (sum_C_n_2_sq + (c_n_2 * c_n_2) % MOD) % MOD;\n        }\n        i = j;\n\
        \    }\n\n    long long total_trapezoids = (sum_C_n_2 * sum_C_n_2) % MOD;\n\
        \    total_trapezoids = (total_trapezoids - sum_C_n_2_sq + MOD) % MOD;\n\n \
        \   long long inv2 = power(2, MOD - 2);\n\n    total_trapezoids = (total_trapezoids\
        \ * inv2) % MOD;\n\n    free(pts);\n    return (int)total_trapezoids;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\nusing System.Linq;\n\
        \npublic class Solution {\n    public int CountTrapezoids(IList<IList<int>>\
        \ points) {\n        long MOD = 1_000_000_007;\n\n        Dictionary<int, List<int>>\
        \ yToXCoords = new Dictionary<int, List<int>>();\n        foreach (var point\
        \ in points) {\n            int x = point[0];\n            int y = point[1];\n\
        \            if (!yToXCoords.ContainsKey(y)) {\n                yToXCoords[y]\
        \ = new List<int>();\n            }\n            yToXCoords[y].Add(x);\n   \
        \     }\n\n        long sumCn2 = 0;\n        long sumCn2Sq = 0;\n\n        foreach\
        \ (var xCoordsList in yToXCoords.Values) {\n            long n = xCoordsList.Count;\n\
        \            if (n >= 2) {\n                long cn2 = (n * (n - 1) / 2) % MOD;\n\
        \n                sumCn2 = (sumCn2 + cn2) % MOD;\n                sumCn2Sq =\
        \ (sumCn2Sq + (cn2 * cn2) % MOD) % MOD;\n            }\n        }\n\n      \
        \  long totalTrapezoids = (sumCn2 * sumCn2) % MOD;\n        totalTrapezoids\
        \ = (totalTrapezoids - sumCn2Sq + MOD) % MOD;\n\n        long inv2 = 500000004;\
        \ // (MOD + 1) / 2\n\n        totalTrapezoids = (totalTrapezoids * inv2) % MOD;\n\
        \n        return (int) totalTrapezoids;\n    }\n}"
      javascript: "/**\n * @param {number[][]} points\n * @return {number}\n */\nvar\
        \ countTrapezoids = function(points) {\n    const MOD = 1_000_000_007;\n\n \
        \   const yToXCoords = new Map();\n    for (const point of points) {\n     \
        \   const x = point[0];\n        const y = point[1];\n        if (!yToXCoords.has(y))\
        \ {\n            yToXCoords.set(y, []);\n        }\n        yToXCoords.get(y).push(x);\n\
        \    }\n\n    let sumCn2 = 0;\n    let sumCn2Sq = 0;\n\n    for (const xCoords\
        \ of yToXCoords.values()) {\n        const n = xCoords.length;\n        if (n\
        \ >= 2) {\n            const cn2 = (n * (n - 1) / 2) % MOD;\n\n            sumCn2\
        \ = (sumCn2 + cn2) % MOD;\n            sumCn2Sq = (sumCn2Sq + (cn2 * cn2) %\
        \ MOD) % MOD;\n        }\n    }\n\n    let totalTrapezoids = (sumCn2 * sumCn2)\
        \ % MOD;\n    totalTrapezoids = (totalTrapezoids - sumCn2Sq + MOD) % MOD;\n\n\
        \    const inv2 = 500000004; // (MOD + 1) / 2\n\n    totalTrapezoids = (totalTrapezoids\
        \ * inv2) % MOD;\n\n    return totalTrapezoids;\n};"
      typescript: "function countTrapezoids(points: number[][]): number {\n    const\
        \ MOD = 1_000_000_007;\n\n    const yToXCoords = new Map<number, number[]>();\n\
        \    for (const point of points) {\n        const x = point[0];\n        const\
        \ y = point[1];\n        if (!yToXCoords.has(y)) {\n            yToXCoords.set(y,\
        \ []);\n        }\n        yToXCoords.get(y)!.push(x);\n    }\n\n    let sumCn2\
        \ = 0;\n    let sumCn2Sq = 0;\n\n    for (const xCoords of yToXCoords.values())\
        \ {\n        const n = xCoords.length;\n        if (n >= 2) {\n            const\
        \ cn2 = (n * (n - 1) / 2) % MOD;\n\n            sumCn2 = (sumCn2 + cn2) % MOD;\n\
        \            sumCn2Sq = (sumCn2Sq + (cn2 * cn2) % MOD) % MOD;\n        }\n \
        \   }\n\n    let totalTrapezoids = (sumCn2 * sumCn2) % MOD;\n    totalTrapezoids\
        \ = (totalTrapezoids - sumCn2Sq + MOD) % MOD;\n\n    const inv2 = 500000004;\
        \ // (MOD + 1) / 2\n\n    totalTrapezoids = (totalTrapezoids * inv2) % MOD;\n\
        \n    return totalTrapezoids;\n}"
      php: "<?php\nclass Solution {\n\n    /**\n     * @param Integer[][] $points\n\
        \     * @return Integer\n     */\n    function countTrapezoids($points) {\n\
        \        $MOD = 1_000_000_007;\n\n        $yToXCoords = [];\n        foreach\
        \ ($points as $point) {\n            $x = $point[0];\n            $y = $point[1];\n\
        \            if (!isset($yToXCoords[$y])) {\n                $yToXCoords[$y]\
        \ = [];\n            }\n            $yToXCoords[$y][] = $x;\n        }\n\n \
        \       $sumCn2 = 0;\n        $sumCn2Sq = 0;\n\n        foreach ($yToXCoords\
        \ as $y => $xCoords) {\n            $n = count($xCoords);\n            if ($n\
        \ >= 2) {\n                $cn2 = (int)(((float)$n * ($n - 1) / 2) % $MOD);\n\
        \n                $sumCn2 = ($sumCn2 + $cn2) % $MOD;\n                $sumCn2Sq\
        \ = ($sumCn2Sq + ($cn2 * $cn2) % $MOD) % $MOD;\n            }\n        }\n\n\
        \        $totalTrapezoids = ($sumCn2 * $sumCn2) % $MOD;\n        $totalTrapezoids\
        \ = ($totalTrapezoids - $sumCn2Sq + $MOD) % $MOD;\n\n        $inv2 = 500000004;\
        \ // (MOD + 1) / 2\n\n        $totalTrapezoids = ($totalTrapezoids * $inv2)\
        \ % $MOD;\n\n        return $totalTrapezoids;\n    }\n}\n?>"
      swift: "import Foundation\n\nclass Solution {\n    func countTrapezoids(_ points:\
        \ [[Int]]) -> Int {\n        let MOD: Int = 1_000_000_007\n\n        var yToXCoords:\
        \ [Int: [Int]] = [:]\n        for point in points {\n            let x = point[0]\n\
        \            let y = point[1]\n            yToXCoords[y, default: []].append(x)\n\
        \        }\n\n        var sumCn2: Int = 0\n        var sumCn2Sq: Int = 0\n\n\
        \        for xCoords in yToXCoords.values {\n            let n = xCoords.count\n\
        \            if n >= 2 {\n                let cn2 = (n * (n - 1) / 2) % MOD\n\
        \n                sumCn2 = (sumCn2 + cn2) % MOD\n                sumCn2Sq =\
        \ (sumCn2Sq + (cn2 * cn2) % MOD) % MOD\n            }\n        }\n\n       \
        \ var totalTrapezoids = (sumCn2 * sumCn2) % MOD\n        totalTrapezoids = (totalTrapezoids\
        \ - sumCn2Sq + MOD) % MOD\n\n        let inv2 = 500000004 // (MOD + 1) / 2\n\
        \n        totalTrapezoids = (totalTrapezoids * inv2) % MOD\n\n        return\
        \ totalTrapezoids\n    }\n}"
      kotlin: "class Solution {\n    fun countTrapezoids(points: List<List<Int>>): Int\
        \ {\n        val MOD = 1_000_000_007L\n\n        val yToXCoords = mutableMapOf<Int,\
        \ MutableList<Int>>()\n        for (point in points) {\n            val x =\
        \ point[0]\n            val y = point[1]\n            yToXCoords.getOrPut(y)\
        \ { mutableListOf() }.add(x)\n        }\n\n        var sumCn2: Long = 0\n  \
        \      var sumCn2Sq: Long = 0\n\n        for (xCoords in yToXCoords.values)\
        \ {\n            val n = xCoords.size.toLong()\n            if (n >= 2) {\n\
        \                val cn2 = (n * (n - 1) / 2) % MOD\n\n                sumCn2\
        \ = (sumCn2 + cn2) % MOD\n                sumCn2Sq = (sumCn2Sq + (cn2 * cn2)\
        \ % MOD) % MOD\n            }\n        }\n\n        var totalTrapezoids = (sumCn2\
        \ * sumCn2) % MOD\n        totalTrapezoids = (totalTrapezoids - sumCn2Sq + MOD)\
        \ % MOD\n\n        val inv2 = 500000004L // (MOD + 1) / 2\n\n        totalTrapezoids\
        \ = (totalTrapezoids * inv2) % MOD\n\n        return totalTrapezoids.toInt()\n\
        \    }\n}"
      dart: "import 'dart:collection';\n\nclass Solution {\n  int countTrapezoids(List<List<int>>\
        \ points) {\n    final int MOD = 1_000_000_007;\n\n    final Map<int, List<int>>\
        \ yToXCoords = HashMap();\n    for (final point in points) {\n      final int\
        \ x = point[0];\n      final int y = point[1];\n      yToXCoords.putIfAbsent(y,\
        \ () => []).add(x);\n    }\n\n    int sumCn2 = 0;\n    int sumCn2Sq = 0;\n\n\
        \    for (final xCoords in yToXCoords.values) {\n      final int n = xCoords.length;\n\
        \      if (n >= 2) {\n        final int cn2 = ((n * (n - 1)) ~/ 2) % MOD;\n\n\
        \        sumCn2 = (sumCn2 + cn2) % MOD;\n        sumCn2Sq = (sumCn2Sq + (cn2\
        \ * cn2) % MOD) % MOD;\n      }\n    }\n\n    int totalTrapezoids = (sumCn2\
        \ * sumCn2) % MOD;\n    totalTrapezoids = (totalTrapezoids - sumCn2Sq + MOD)\
        \ % MOD;\n\n    final int inv2 = 500000004; // (MOD + 1) / 2\n\n    totalTrapezoids\
        \ = (totalTrapezoids * inv2) % MOD;\n\n    return totalTrapezoids;\n  }\n}"
      go: "package main\n\nimport (\n\t\"fmt\"\n)\n\nfunc countTrapezoids(points [][]int)\
        \ int {\n\tMOD := 1_000_000_007\n\n\tyToXCoords := make(map[int][]int)\n\tfor\
        \ _, point := range points {\n\t\tx, y := point[0], point[1]\n\t\tyToXCoords[y]\
        \ = append(yToXCoords[y], x)\n\t}\n\n\tvar sumCn2 int = 0\n\tvar sumCn2Sq int\
        \ = 0\n\n\tfor _, xCoords := range yToXCoords {\n\t\tn := len(xCoords)\n\t\t\
        if n >= 2 {\n\t\t\tcn2 := (n * (n - 1) / 2) % MOD\n\n\t\t\tsumCn2 = (sumCn2\
        \ + cn2) % MOD\n\t\t\tsumCn2Sq = (sumCn2Sq + (cn2 * cn2) % MOD) % MOD\n\t\t\
        }\n\t}\n\n\ttotalTrapezoids := (sumCn2 * sumCn2) % MOD\n\ttotalTrapezoids =\
        \ (totalTrapezoids - sumCn2Sq + MOD) % MOD\n\n\tinv2 := 500000004 // (MOD +\
        \ 1) / 2\n\n\ttotalTrapezoids = (totalTrapezoids * inv2) % MOD\n\n\treturn totalTrapezoids\n\
        }"
      ruby: "# @param {Integer[][]} points\n# @return {Integer}\ndef count_trapezoids(points)\n\
        \    mod = 1_000_000_007\n\n    y_to_x_coords = Hash.new { |hash, key| hash[key]\
        \ = [] }\n    points.each do |x, y|\n        y_to_x_coords[y] << x\n    end\n\
        \n    sum_cn2 = 0\n    sum_cn2_sq = 0\n\n    y_to_x_coords.each_value do |x_coords|\n\
        \        n = x_coords.length\n        if n >= 2\n            cn2 = (n * (n -\
        \ 1) / 2) % mod\n\n            sum_cn2 = (sum_cn2 + cn2) % mod\n           \
        \ sum_cn2_sq = (sum_cn2_sq + (cn2 * cn2) % mod) % mod\n        end\n    end\n\
        \n    total_trapezoids = (sum_cn2 * sum_cn2) % mod\n    total_trapezoids = (total_trapezoids\
        \ - sum_cn2_sq + mod) % mod\n\n    inv2 = 500000004 # (mod + 1) / 2\n\n    total_trapezoids\
        \ = (total_trapezoids * inv2) % mod\n\n    return total_trapezoids\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n    def countTrapezoids(points:\
        \ Array[Array[Int]]): Int = {\n        val MOD: Long = 1_000_000_007L\n\n  \
        \      val yToXCoords = mutable.HashMap.empty[Int, mutable.ListBuffer[Int]]\n\
        \        for (point <- points) {\n            val x = point(0)\n           \
        \ val y = point(1)\n            yToXCoords.getOrElseUpdate(y, mutable.ListBuffer.empty[Int]).append(x)\n\
        \        }\n\n        var sumCn2: Long = 0\n        var sumCn2Sq: Long = 0\n\
        \n        for (xCoords <- yToXCoords.values) {\n            val n = xCoords.length.toLong\n\
        \            if (n >= 2) {\n                val cn2 = (n * (n - 1) / 2) % MOD\n\
        \n                sumCn2 = (sumCn2 + cn2) % MOD\n                sumCn2Sq =\
        \ (sumCn2Sq + (cn2 * cn2) % MOD) % MOD\n            }\n        }\n\n       \
        \ var totalTrapezoids = (sumCn2 * sumCn2) % MOD\n        totalTrapezoids = (totalTrapezoids\
        \ - sumCn2Sq + MOD) % MOD\n\n        val inv2 = 500000004L // (MOD + 1) / 2\n\
        \n        totalTrapezoids = (totalTrapezoids * inv2) % MOD\n\n        totalTrapezoids.toInt\n\
        \    }\n}"
      rust: "use std::collections::HashMap;\n\nimpl Solution {\n    pub fn count_trapezoids(points:\
        \ Vec<Vec<i32>>) -> i32 {\n        let modular: i64 = 1_000_000_007;\n\n   \
        \     let mut y_to_x_coords: HashMap<i32, Vec<i32>> = HashMap::new();\n    \
        \    for point in points {\n            let x = point[0];\n            let y\
        \ = point[1];\n            y_to_x_coords.entry(y).or_insert_with(Vec::new).push(x);\n\
        \        }\n\n        let mut sum_cn2: i64 = 0;\n        let mut sum_cn2_sq:\
        \ i64 = 0;\n\n        for x_coords in y_to_x_coords.values() {\n           \
        \ let n = x_coords.len() as i64;\n            if n >= 2 {\n                let\
        \ cn2 = (n * (n - 1) / 2) % modular;\n\n                sum_cn2 = (sum_cn2 +\
        \ cn2) % modular;\n                sum_cn2_sq = (sum_cn2_sq + (cn2 * cn2) %\
        \ modular) % modular;\n            }\n        }\n\n        let mut total_trapezoids\
        \ = (sum_cn2 * sum_cn2) % modular;\n        total_trapezoids = (total_trapezoids\
        \ - sum_cn2_sq + modular) % modular;\n\n        let inv2: i64 = 500000004; //\
        \ (MOD + 1) / 2\n\n        total_trapezoids = (total_trapezoids * inv2) % modular;\n\
        \n        total_trapezoids as i32\n    }\n}"
      racket: "#lang racket\n\n(provide (struct-out Solution) (method-in Solution count-trapezoids))\n\
        \n(define MOD 1000000007)\n\n(define (power base exp)\n  (define (loop res base\
        \ exp)\n    (cond\n      [(= exp 0) res]\n      [(odd? exp) (loop (modulo (*\
        \ res base) MOD) (modulo (* base base) MOD) (quotient exp 2))]\n      [else\
        \ (loop res (modulo (* base base) MOD) (quotient exp 2))]))\n  (loop 1 (modulo\
        \ base MOD) exp))\n\n(define (count-trapezoids points)\n  (define y-to-x-coords\
        \ (make-hash))\n  (for-each (lambda (point)\n              (define x (vector-ref\
        \ point 0))\n              (define y (vector-ref point 1))\n              (hash-update!\
        \ y-to-x-coords y (lambda (lst) (cons x lst)) '()))\n            points)\n\n\
        \  (define sum-cn2 0)\n  (define sum-cn2-sq 0)\n\n  (for-each (lambda (x-coords)\n\
        \              (define n (length x-coords))\n              (when (>= n 2)\n\
        \                (define cn2 (modulo (quotient (* n (- n 1)) 2) MOD))\n    \
        \            (set! sum-cn2 (modulo (+ sum-cn2 cn2) MOD))\n                (set!\
        \ sum-cn2-sq (modulo (+ sum-cn2-sq (modulo (* cn2 cn2) MOD)) MOD))))\n     \
        \       (hash-values y-to-x-coords))\n\n  (define total-trapezoids (modulo (*\
        \ sum-cn2 sum-cn2) MOD))\n  (set! total-trapezoids (modulo (+ (- total-trapezoids\
        \ sum-cn2-sq) MOD) MOD))\n\n  (define inv2 (power 2 (- MOD 2)))\n  (set! total-trapezoids\
        \ (modulo (* total-trapezoids inv2) MOD))\n\n  total-trapezoids)\n\n(define-struct\
        \ Solution ())\n(define-method (count-trapezoids (self Solution) points)\n \
        \ (count-trapezoids points))"
      erlang: "-module(solution).\n-export([count_trapezoids/1]).\n\ncount_trapezoids(Points)\
        \ ->\n    MOD = 1_000_000_007,\n\n    YToXCoords = lists:foldl(\n        fun([_X,\
        \ Y], Acc) ->\n            maps:update_with(Y, fun(List) -> List ++ [_X] end,\
        \ [_X], Acc)\n        end,\n        maps:new(),\n        Points\n    ),\n\n\
        \    {SumCn2, SumCn2Sq} = maps:fold(\n        fun(_Y, XCoords, {AccSumCn2, AccSumCn2Sq})\
        \ ->\n            N = length(XCoords),\n            if N >= 2 ->\n         \
        \       Cn2 = ((N * (N - 1)) div 2) rem MOD,\n                NewAccSumCn2 =\
        \ (AccSumCn2 + Cn2) rem MOD,\n                NewAccSumCn2Sq = (AccSumCn2Sq\
        \ + (Cn2 * Cn2) rem MOD) rem MOD,\n                {NewAccSumCn2, NewAccSumCn2Sq};\n\
        \            true ->\n                {AccSumCn2, AccSumCn2Sq}\n           \
        \ end\n        end,\n        {0, 0},\n        YToXCoords\n    ),\n\n    TotalTrapezoids\
        \ = (SumCn2 * SumCn2) rem MOD,\n    TotalTrapezoidsAdjusted = (TotalTrapezoids\
        \ - SumCn2Sq + MOD) rem MOD,\n\n    Inv2 = 500000004, % (MOD + 1) div 2\n\n\
        \    (TotalTrapezoidsAdjusted * Inv2) rem MOD."
      elixir: "defmodule Solution do\n  @spec count_trapezoids(points :: [[integer]])\
        \ :: integer\n  def count_trapezoids(points) do\n    mod = 1_000_000_007\n\n\
        \    y_to_x_coords =\n      Enum.reduce(points, %{}, fn [x, y], acc ->\n   \
        \     Map.update(acc, y, [x], fn list -> [x | list] end)\n      end)\n\n   \
        \ {sum_cn2, sum_cn2_sq} =\n      Enum.reduce(Map.values(y_to_x_coords), {0,\
        \ 0}, fn x_coords, {acc_sum_cn2, acc_sum_cn2_sq} ->\n        n = length(x_coords)\n\
        \        if n >= 2 do\n          cn2 = div(n * (n - 1), 2) |> rem(mod)\n   \
        \       new_acc_sum_cn2 = (acc_sum_cn2 + cn2) |> rem(mod)\n          new_acc_sum_cn2_sq\
        \ = (acc_sum_cn2_sq + (cn2 * cn2) |> rem(mod)) |> rem(mod)\n          {new_acc_sum_cn2,\
        \ new_acc_sum_cn2_sq}\n        else\n          {acc_sum_cn2, acc_sum_cn2_sq}\n\
        \        end\n      end)\n\n    total_trapezoids = (sum_cn2 * sum_cn2) |> rem(mod)\n\
        \    total_trapezoids = (total_trapezoids - sum_cn2_sq + mod) |> rem(mod)\n\n\
        \    inv2 = 500_000_004 # (mod + 1) / 2\n\n    (total_trapezoids * inv2) |>\
        \ rem(mod)\n  end\nend"
    approach: The problem asks us to count the number of unique horizontal trapezoids
      formed by choosing any four distinct points from a given set of points. A horizontal
      trapezoid is defined as a convex quadrilateral with at least one pair of horizontal
      sides. This implies that the four chosen points must lie on exactly two distinct
      horizontal lines (i.e., have two distinct y-coordinates). If we select two points
      from one horizontal line and two points from another distinct horizontal line,
      these four points will always form a convex quadrilateral with two parallel horizontal
      sides, thus satisfying the definition of a horizontal trapezoid.
    time_complexity: The time complexity is O(N), where N is the number of points. This
      is because we first iterate through all N points to group them by their y-coordinates,
      which takes O(N) time (average for hash map, O(N log D) for tree map where D is
      distinct y-coordinates, but D <= N). Then, we iterate through the distinct y-coordinate
      groups (at most D groups) to calculate the combinations and update sums. This
      takes O(D) time. Since D <= N, the overall time complexity is dominated by O(N).
    space_complexity: The space complexity is O(N), where N is the number of points.
      This is primarily due to storing the points grouped by their y-coordinates in
      a hash map (or similar data structure). In the worst case, all N points could
      have distinct y-coordinates, or all could have the same y-coordinate, but in either
      scenario, we store approximately N x-coordinates in total across all lists in
      the map.
    elapsed_time: 89.691903591156
    model: gemini-2.5-flash
    generated_at: '2025-12-02 01:06:20 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int countTrapezoids(vector<vector<int>>&\
        \ points) {\n        map<int, vector<int>> groups;\n        for (auto& point\
        \ : points) {\n            groups[point[1]].push_back(point[0]);\n        }\n\
        \        int count = 0;\n        for (auto& group1 : groups) {\n           \
        \ for (auto& group2 : groups) {\n                if (group1.first != group2.first)\
        \ {\n                    int n1 = group1.second.size(), n2 = group2.second.size();\n\
        \                    count += n1 * (n1 - 1) / 2 * n2 * (n2 - 1) / 2;\n     \
        \           }\n            }\n        }\n        return count % (1000000007);\n\
        \    }\n};"
      java: "class Solution {\n    public int countTrapezoids(int[][] points) {\n  \
        \      Map<Integer, List<Integer>> groups = new HashMap<>();\n        for (int[]\
        \ point : points) {\n            groups.computeIfAbsent(point[1], k -> new ArrayList<>()).add(point[0]);\n\
        \        }\n        int count = 0;\n        for (int y1 : groups.keySet()) {\n\
        \            for (int y2 : groups.keySet()) {\n                if (y1 != y2)\
        \ {\n                    int n1 = groups.get(y1).size(), n2 = groups.get(y2).size();\n\
        \                    count += n1 * (n1 - 1) / 2 * n2 * (n2 - 1) / 2;\n     \
        \           }\n            }\n        }\n        return count % 1000000007;\n\
        \    }\n}"
      python: "class Solution:\n    def countTrapezoids(self, points: List[List[int]])\
        \ -> int:\n        groups = {}\n        for x, y in points:\n            if\
        \ y not in groups:\n                groups[y] = []\n            groups[y].append(x)\n\
        \        count = 0\n        for y1 in groups:\n            for y2 in groups:\n\
        \                if y1 != y2:\n                    n1, n2 = len(groups[y1]),\
        \ len(groups[y2])\n                    count += n1 * (n1 - 1) // 2 * n2 * (n2\
        \ - 1) // 2\n        return count % 1000000007"
      python3: "class Solution:\n    def countTrapezoids(self, points: List[List[int]])\
        \ -> int:\n        groups = {}\n        for x, y in points:\n            if\
        \ y not in groups:\n                groups[y] = []\n            groups[y].append(x)\n\
        \        count = 0\n        for y1 in groups:\n            for y2 in groups:\n\
        \                if y1 != y2:\n                    n1, n2 = len(groups[y1]),\
        \ len(groups[y2])\n                    count += n1 * (n1 - 1) // 2 * n2 * (n2\
        \ - 1) // 2\n        return count % 1000000007"
      c: "typedef struct {\n    int x;\n    int y;\n} Point;\n\nint compare(const void\
        \ *a, const void *b) {\n    Point *p1 = (Point *)a;\n    Point *p2 = (Point\
        \ *)b;\n    return p1->y - p2->y;\n}\n\nint countTrapezoids(int **points, int\
        \ pointsSize, int *pointsColSize) {\n    int count = 0;\n    qsort(points, pointsSize,\
        \ sizeof(int *), compare);\n    for (int i = 0; i < pointsSize; i++) {\n   \
        \     for (int j = i + 1; j < pointsSize; j++) {\n            if (points[i][1]\
        \ != points[j][1]) {\n                int n1 = 0, n2 = 0;\n                for\
        \ (int k = 0; k < pointsSize; k++) {\n                    if (points[k][1] ==\
        \ points[i][1]) n1++;\n                    if (points[k][1] == points[j][1])\
        \ n2++;\n                }\n                count += n1 * (n1 - 1) / 2 * n2\
        \ * (n2 - 1) / 2;\n            }\n        }\n    }\n    return count % 1000000007;\n\
        }"
      csharp: "public class Solution {\n    public int CountTrapezoids(int[][] points)\
        \ {\n        Dictionary<int, List<int>> groups = new Dictionary<int, List<int>>();\n\
        \        foreach (int[] point in points) {\n            if (!groups.ContainsKey(point[1]))\
        \ {\n                groups[point[1]] = new List<int>();\n            }\n  \
        \          groups[point[1]].Add(point[0]);\n        }\n        int count = 0;\n\
        \        foreach (int y1 in groups.Keys) {\n            foreach (int y2 in groups.Keys)\
        \ {\n                if (y1 != y2) {\n                    int n1 = groups[y1].Count,\
        \ n2 = groups[y2].Count;\n                    count += n1 * (n1 - 1) / 2 * n2\
        \ * (n2 - 1) / 2;\n                }\n            }\n        }\n        return\
        \ count % 1000000007;\n    }\n}"
      javascript: "var countTrapezoids = function(points) {\n    let groups = {};\n\
        \    for (let point of points) {\n        if (!(point[1] in groups)) {\n   \
        \         groups[point[1]] = [];\n        }\n        groups[point[1]].push(point[0]);\n\
        \    }\n    let count = 0;\n    for (let y1 in groups) {\n        for (let y2\
        \ in groups) {\n            if (y1 != y2) {\n                let n1 = groups[y1].length,\
        \ n2 = groups[y2].length;\n                count += n1 * (n1 - 1) / 2 * n2 *\
        \ (n2 - 1) / 2;\n            }\n        }\n    }\n    return count % 1000000007;\n\
        };"
      typescript: "function countTrapezoids(points: number[][]): number {\n    let groups:\
        \ { [key: number]: number[] } = {};\n    for (let point of points) {\n     \
        \   if (!(point[1] in groups)) {\n            groups[point[1]] = [];\n     \
        \   }\n        groups[point[1]].push(point[0]);\n    }\n    let count: number\
        \ = 0;\n    for (let y1 in groups) {\n        for (let y2 in groups) {\n   \
        \         if (y1 != y2) {\n                let n1: number = groups[y1].length,\
        \ n2: number = groups[y2].length;\n                count += n1 * (n1 - 1) /\
        \ 2 * n2 * (n2 - 1) / 2;\n            }\n        }\n    }\n    return count\
        \ % 1000000007;\n}"
      php: "$count = 0;\n$groups = [];\nforeach ($points as $point) {\n    if (!isset($groups[$point[1]]))\
        \ {\n        $groups[$point[1]] = [];\n    }\n    $groups[$point[1]][] = $point[0];\n\
        }\nforeach ($groups as $y1 => $group1) {\n    foreach ($groups as $y2 => $group2)\
        \ {\n        if ($y1 != $y2) {\n            $n1 = count($group1);\n        \
        \    $n2 = count($group2);\n            $count += $n1 * ($n1 - 1) / 2 * $n2\
        \ * ($n2 - 1) / 2;\n        }\n    }\n}\necho $count % 1000000007;"
      swift: "class Solution {\n    func countTrapezoids(_ points: [[Int]]) -> Int {\n\
        \        var groups: [Int: [Int]] = [:]\n        for point in points {\n   \
        \         if groups[point[1]] == nil {\n                groups[point[1]] = []\n\
        \            }\n            groups[point[1]]!.append(point[0])\n        }\n\
        \        var count = 0\n        for y1 in groups.keys {\n            for y2\
        \ in groups.keys {\n                if y1 != y2 {\n                    let n1\
        \ = groups[y1]!.count\n                    let n2 = groups[y2]!.count\n    \
        \                count += n1 * (n1 - 1) / 2 * n2 * (n2 - 1) / 2\n          \
        \      }\n            }\n        }\n        return count % 1000000007\n    }\n\
        }"
      kotlin: "class Solution {\n    fun countTrapezoids(points: Array<IntArray>): Int\
        \ {\n        val groups = mutableMapOf<Int, MutableList<Int>>()\n        for\
        \ (point in points) {\n            if (!groups.containsKey(point[1])) {\n  \
        \              groups[point[1]] = mutableListOf()\n            }\n         \
        \   groups[point[1]]!!.add(point[0])\n        }\n        var count = 0\n   \
        \     for (y1 in groups.keys) {\n            for (y2 in groups.keys) {\n   \
        \             if (y1 != y2) {\n                    val n1 = groups[y1]!!.size\n\
        \                    val n2 = groups[y2]!!.size\n                    count +=\
        \ n1 * (n1 - 1) / 2 * n2 * (n2 - 1) / 2\n                }\n            }\n\
        \        }\n        return count % 1000000007\n    }\n}"
      dart: "class Solution {\n    int countTrapezoids(List<List<int>> points) {\n \
        \       Map<int, List<int>> groups = {};\n        for (var point in points)\
        \ {\n            if (!groups.containsKey(point[1])) {\n                groups[point[1]]\
        \ = [];\n            }\n            groups[point[1]]!.add(point[0]);\n     \
        \   }\n        int count = 0;\n        for (var y1 in groups.keys) {\n     \
        \       for (var y2 in groups.keys) {\n                if (y1 != y2) {\n   \
        \                 int n1 = groups[y1]!.length;\n                    int n2 =\
        \ groups[y2]!.length;\n                    count += n1 * (n1 - 1) ~/ 2 * n2\
        \ * (n2 - 1) ~/ 2;\n                }\n            }\n        }\n        return\
        \ count % 1000000007;\n    }\n}"
      go: "package main\n\nimport (\n    \"fmt\"\n)\n\ntype Solution struct{}\n\nfunc\
        \ (s Solution) countTrapezoids(points [][]int) int {\n    groups := map[int][]int{}\n\
        \    for _, point := range points {\n        if _, ok := groups[point[1]]; !ok\
        \ {\n            groups[point[1]] = []int{}\n        }\n        groups[point[1]]\
        \ = append(groups[point[1]], point[0])\n    }\n    count := 0\n    for y1 :=\
        \ range groups {\n        for y2 := range groups {\n            if y1 != y2\
        \ {\n                n1 := len(groups[y1])\n                n2 := len(groups[y2])\n\
        \                count += n1*(n1-1)/2 * n2*(n2-1)/2\n            }\n       \
        \ }\n    }\n    return count % 1000000007\n}"
      ruby: "def count_trapezoids(points)\n    groups = {}\n    points.each do |point|\n\
        \        if !groups.key?(point[1])\n            groups[point[1]] = []\n    \
        \    end\n        groups[point[1]] << point[0]\n    end\n    count = 0\n   \
        \ groups.keys.each do |y1|\n        groups.keys.each do |y2|\n            if\
        \ y1 != y2\n                n1 = groups[y1].size\n                n2 = groups[y2].size\n\
        \                count += n1 * (n1 - 1) / 2 * n2 * (n2 - 1) / 2\n          \
        \  end\n        end\n    end\n    count % 1000000007\nend"
      scala: "object Solution {\n    def countTrapezoids(points: Array[Array[Int]]):\
        \ Int = {\n        val groups = scala.collection.mutable.Map[Int, List[Int]]()\n\
        \        for (point <- points) {\n            if (!groups.contains(point(1)))\
        \ {\n                groups(point(1)) = List()\n            }\n            groups(point(1))\
        \ = point(0) :: groups(point(1))\n        }\n        var count = 0\n       \
        \ for (y1 <- groups.keys) {\n            for (y2 <- groups.keys) {\n       \
        \         if (y1 != y2) {\n                    val n1 = groups(y1).size\n  \
        \                  val n2 = groups(y2).size\n                    count += n1\
        \ * (n1 - 1) / 2 * n2 * (n2 - 1) / 2\n                }\n            }\n   \
        \     }\n        count % 1000000007\n    }\n}"
      rust: "struct Solution;\n\nimpl Solution {\n    pub fn count_trapezoids(points:\
        \ Vec<Vec<i32>>) -> i32 {\n        let mut groups: std::collections::HashMap<i32,\
        \ Vec<i32>> = std::collections::HashMap::new();\n        for point in points\
        \ {\n            if !groups.contains_key(&point[1]) {\n                groups.insert(point[1],\
        \ Vec::new());\n            }\n            groups.get_mut(&point[1]).unwrap().push(point[0]);\n\
        \        }\n        let mut count = 0;\n        for y1 in groups.keys() {\n\
        \            for y2 in groups.keys() {\n                if y1 != y2 {\n    \
        \                let n1 = groups.get(y1).unwrap().len();\n                 \
        \   let n2 = groups.get(y2).unwrap().len();\n                    count += n1\
        \ * (n1 - 1) / 2 * n2 * (n2 - 1) / 2;\n                }\n            }\n  \
        \      }\n        count % 1000000007\n    }\n}"
      racket: "(define (count-trapezoids points)\n    (let ((groups (make-hash)))\n\
        \        (for-each (lambda (point)\n                    (let ((y (cadr point)))\n\
        \                        (if (not (hash-ref groups y))\n                   \
        \         (hash-set! groups y '()))\n                        (hash-set! groups\
        \ y (cons (car point) (hash-ref groups y)))))\n                  points)\n \
        \       (let loop ((y1 (hash-keys groups))\n                   (count 0))\n\
        \            (if (null? y1)\n                (modulo count 1000000007)\n   \
        \             (let loop2 ((y2 (hash-keys groups))\n                        \
        \   (count2 count))\n                    (if (null? y2)\n                  \
        \      (loop (cdr y1) count2)\n                        (if (not (eq? (car y1)\
        \ (car y2)))\n                            (loop2 (cdr y2) (+ count2 (/ (* (length\
        \ (hash-ref groups (car y1)))\n                                            \
        \        (- (length (hash-ref groups (car y1))) 1))\n                      \
        \                            2)\n                                          \
        \        (/ (* (length (hash-ref groups (car y2)))\n                       \
        \                             (- (length (hash-ref groups (car y2))) 1))\n \
        \                                                 2)))\n                   \
        \         (loop2 (cdr y2) count2))))))))"
      erlang: "-module(solution).\n-export([count_trapezoids/1]).\n\ncount_trapezoids(Points)\
        \ ->\n    Groups = group_points(Points),\n    Count = count_trapezoids(Groups,\
        \ 0),\n    Count rem 1000000007.\n\ngroup_points(Points) ->\n    group_points(Points,\
        \ []).\n\ngroup_points([], Groups) ->\n    lists:reverse(Groups);\n\ngroup_points([Point|Points],\
        \ Groups) ->\n    {Y, X} = Point,\n    case lists:keytake(Y, 1, Groups) of\n\
        \        {value, {Y, Xs}, Groups1} ->\n            group_points(Points, [{Y,\
        \ [X|Xs]}|Groups1]);\n        false ->\n            group_points(Points, [{Y,\
        \ [X]}|Groups])\n    end.\n\ncount_trapezoids([], Count) -> Count;\n\ncount_trapezoids([Group|Groups],\
        \ Count) ->\n    count_trapezoids(Groups, Count + count_trapezoids(Group, Groups,\
        \ 0)).\n\ncount_trapezoids({Y1, Xs1}, Groups, Count) ->\n    count_trapezoids(Groups,\
        \ Count, Y1, Xs1, length(Xs1)).\n\ncount_trapezoids([], _, _, _, _) -> 0;\n\n\
        count_trapezoids([Group|Groups], Count, Y1, Xs1, N1) ->\n    {Y2, Xs2} = Group,\n\
        \    if Y1 =:= Y2 ->\n        count_trapezoids(Groups, Count, Y1, Xs1, N1);\n\
        \    true ->\n        count_trapezoids(Groups, Count + (N1 * (N1 - 1) div 2)\
        \ * (length(Xs2) * (length(Xs2) - 1) div 2), Y1, Xs1, N1)"
      elixir: "defmodule Solution do\n    def count_trapezoids(points) do\n        groups\
        \ = Enum.reduce(points, %{}, fn [x, y], groups ->\n            Map.update(groups,\
        \ y, [x], fn x -> [x | x] end)\n        end)\n        count = Enum.reduce(groups,\
        \ 0, fn {y1, xs1}, count ->\n            Enum.reduce(groups, count, fn {y2,\
        \ xs2}, count ->\n                if y1 != y2 do\n                    count\
        \ + length(xs1) * (length(xs1) - 1) * length(xs2) * (length(xs2) - 1) div 4\n\
        \                else\n                    count\n                end\n    \
        \        end)\n        end)\n        rem(count, 1_000_000_007)\n    end\nend"
    approach: The problem can be solved by first grouping the points by their y-coordinates.
      Then, we can choose two distinct groups (two horizontal lines), and from each
      group select two points to form a trapezoid. This approach ensures that we consider
      all possible combinations of points that can form a horizontal trapezoid. The
      key intuition here is that for a line parallel to the x-axis, all its points must
      share the same y-coordinate, which allows us to group the points by their y-coordinates
      and then select points from each group to form a trapezoid.
    time_complexity: The time complexity of this solution is O(n^2 * m^2) where n is
      the number of distinct y-coordinates and m is the maximum number of points with
      the same y-coordinate. This is because we are iterating over all pairs of distinct
      y-coordinates and for each pair, we are iterating over all pairs of points in
      each group.
    space_complexity: The space complexity of this solution is O(n * m) where n is the
      number of distinct y-coordinates and m is the maximum number of points with the
      same y-coordinate. This is because we need to store the points grouped by their
      y-coordinates.
    elapsed_time: 9.954662084579468
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-02 01:06:30 '
---

## Problem #3623: Count Number of Trapezoids I

**Difficulty:** Medium

**Topics:** Array, Hash Table, Math, Geometry

## Problem Description

<p data-end="189" data-start="146">You are given a 2D integer array <code>points</code>, where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> represents the coordinates of the <code>i<sup>th</sup></code> point on the Cartesian plane.</p>

<p data-end="579" data-start="405">A <strong>horizontal</strong> <strong>trapezoid</strong> is a convex quadrilateral with <strong data-end="496" data-start="475">at least one pair</strong> of horizontal sides (i.e. parallel to the x-axis). Two lines are parallel if and only if they have the same slope.</p>

<p data-end="579" data-start="405">Return the <em data-end="330" data-start="297"> number of unique </em><strong><em>horizontal</em> <em>trapezoids</em></strong> that can be formed by choosing any four distinct points from <code>points</code>.</p>

<p>Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">points = [[1,0],[2,0],[3,0],[2,2],[3,2]]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2025/05/01/desmos-graph-6.png" style="width: 250px; height: 250px;" /> <img alt="" src="https://assets.leetcode.com/uploads/2025/05/01/desmos-graph-7.png" style="width: 250px; height: 250px;" /> <img alt="" src="https://assets.leetcode.com/uploads/2025/05/01/desmos-graph-8.png" style="width: 250px; height: 250px;" /></p>

<p>There are three distinct ways to pick four points that form a horizontal trapezoid:</p>

<ul>
	<li data-end="247" data-start="193">Using points <code data-end="213" data-start="206">[1,0]</code>, <code data-end="222" data-start="215">[2,0]</code>, <code data-end="231" data-start="224">[3,2]</code>, and <code data-end="244" data-start="237">[2,2]</code>.</li>
	<li data-end="305" data-start="251">Using points <code data-end="271" data-start="264">[2,0]</code>, <code data-end="280" data-start="273">[3,0]</code>, <code data-end="289" data-start="282">[3,2]</code>, and <code data-end="302" data-start="295">[2,2]</code>.</li>
	<li data-end="361" data-start="309">Using points <code data-end="329" data-start="322">[1,0]</code>, <code data-end="338" data-start="331">[3,0]</code>, <code data-end="347" data-start="340">[3,2]</code>, and <code data-end="360" data-start="353">[2,2]</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">points = [[0,0],[1,0],[0,1],[2,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2025/04/29/desmos-graph-5.png" style="width: 250px; height: 250px;" /></p>

<p>There is only one horizontal trapezoid that can be formed.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>4 &lt;= points.length &lt;= 10<sup>5</sup></code></li>
	<li><code>&ndash;10<sup>8</sup> &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>8</sup></code></li>
	<li>All points are pairwise distinct.</li>
</ul>


## Hints

1. For a line parallel to the x‑axis, all its points must share the same y‑coordinate.

2. Group the points by their y‑coordinate.

3. Choose two distinct groups (two horizontal lines), and from each group select two points to form a trapezoid.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-02 01:06:20 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to count the number of unique horizontal trapezoids formed by choosing any four distinct points from a given set of points. A horizontal trapezoid is defined as a convex quadrilateral with at least one pair of horizontal sides. This implies that the four chosen points must lie on exactly two distinct horizontal lines (i.e., have two distinct y-coordinates). If we select two points from one horizontal line and two points from another distinct horizontal line, these four points will always form a convex quadrilateral with two parallel horizontal sides, thus satisfying the definition of a horizontal trapezoid.

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-cpp-gemini-2-5-flash" checked>
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-java-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python3-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-c-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-csharp-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-javascript-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-typescript-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-php-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-swift-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-kotlin-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-dart-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-go-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-ruby-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-scala-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-rust-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-racket-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-erlang-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-elixir-gemini-2-5-flash">
  <div class="tab-labels">
    <label for="lang-cpp-gemini-2-5-flash">C++</label>
    <label for="lang-java-gemini-2-5-flash">Java</label>
    <label for="lang-python-gemini-2-5-flash">Python</label>
    <label for="lang-python3-gemini-2-5-flash">Python3</label>
    <label for="lang-c-gemini-2-5-flash">C</label>
    <label for="lang-csharp-gemini-2-5-flash">C#</label>
    <label for="lang-javascript-gemini-2-5-flash">JavaScript</label>
    <label for="lang-typescript-gemini-2-5-flash">TypeScript</label>
    <label for="lang-php-gemini-2-5-flash">PHP</label>
    <label for="lang-swift-gemini-2-5-flash">Swift</label>
    <label for="lang-kotlin-gemini-2-5-flash">Kotlin</label>
    <label for="lang-dart-gemini-2-5-flash">Dart</label>
    <label for="lang-go-gemini-2-5-flash">Go</label>
    <label for="lang-ruby-gemini-2-5-flash">Ruby</label>
    <label for="lang-scala-gemini-2-5-flash">Scala</label>
    <label for="lang-rust-gemini-2-5-flash">Rust</label>
    <label for="lang-racket-gemini-2-5-flash">Racket</label>
    <label for="lang-erlang-gemini-2-5-flash">Erlang</label>
    <label for="lang-elixir-gemini-2-5-flash">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
class Solution {
public:
    int countTrapezoids(std::vector<std::vector<int>>& points) {
        long long MOD = 1e9 + 7;

        std::map<int, std::vector<int>> y_to_x_coords;
        for (const auto& point : points) {
            y_to_x_coords[point[1]].push_back(point[0]);
        }

        long long sum_C_n_2 = 0;
        long long sum_C_n_2_sq = 0;

        for (const auto& pair : y_to_x_coords) {
            long long n = pair.second.size();
            if (n >= 2) {
                long long c_n_2 = (n * (n - 1) / 2) % MOD;

                sum_C_n_2 = (sum_C_n_2 + c_n_2) % MOD;
                sum_C_n_2_sq = (sum_C_n_2_sq + (c_n_2 * c_n_2) % MOD) % MOD;
            }
        }

        long long total_trapezoids = (sum_C_n_2 * sum_C_n_2) % MOD;
        total_trapezoids = (total_trapezoids - sum_C_n_2_sq + MOD) % MOD;

        long long inv2 = 500000004; // (MOD + 1) / 2

        total_trapezoids = (total_trapezoids * inv2) % MOD;

        return static_cast<int>(total_trapezoids);
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;

class Solution {
    public int countTrapezoids(List<List<Integer>> points) {
        long MOD = 1_000_000_007;

        Map<Integer, List<Integer>> yToXCoords = new HashMap<>();
        for (List<Integer> point : points) {
            int x = point.get(0);
            int y = point.get(1);
            yToXCoords.computeIfAbsent(y, k -> new ArrayList<>()).add(x);
        }

        long sumCn2 = 0;
        long sumCn2Sq = 0;

        for (List<Integer> xCoords : yToXCoords.values()) {
            long n = xCoords.size();
            if (n >= 2) {
                long cn2 = (n * (n - 1) / 2) % MOD;

                sumCn2 = (sumCn2 + cn2) % MOD;
                sumCn2Sq = (sumCn2Sq + (cn2 * cn2) % MOD) % MOD;
            }
        }

        long totalTrapezoids = (sumCn2 * sumCn2) % MOD;
        totalTrapezoids = (totalTrapezoids - sumCn2Sq + MOD) % MOD;

        long inv2 = 500000004; // (MOD + 1) / 2

        totalTrapezoids = (totalTrapezoids * inv2) % MOD;

        return (int) totalTrapezoids;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import collections

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7

        y_to_x_coords = collections.defaultdict(list)
        for x, y in points:
            y_to_x_coords[y].append(x)

        sum_C_n_2 = 0
        sum_C_n_2_sq = 0

        for y in y_to_x_coords:
            n = len(y_to_x_coords[y])
            if n >= 2:
                c_n_2 = (n * (n - 1) // 2) % MOD

                sum_C_n_2 = (sum_C_n_2 + c_n_2) % MOD
                sum_C_n_2_sq = (sum_C_n_2_sq + (c_n_2 * c_n_2) % MOD) % MOD

        total_trapezoids = (sum_C_n_2 * sum_C_n_2) % MOD
        total_trapezoids = (total_trapezoids - sum_C_n_2_sq + MOD) % MOD

        inv2 = pow(2, MOD - 2, MOD)
        total_trapezoids = (total_trapezoids * inv2) % MOD

        return total_trapezoids
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import collections

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7

        y_to_x_coords = collections.defaultdict(list)
        for x, y in points:
            y_to_x_coords[y].append(x)

        sum_C_n_2 = 0
        sum_C_n_2_sq = 0

        for y in y_to_x_coords:
            n = len(y_to_x_coords[y])
            if n >= 2:
                c_n_2 = (n * (n - 1) // 2) % MOD

                sum_C_n_2 = (sum_C_n_2 + c_n_2) % MOD
                sum_C_n_2_sq = (sum_C_n_2_sq + (c_n_2 * c_n_2) % MOD) % MOD

        total_trapezoids = (sum_C_n_2 * sum_C_n_2) % MOD
        total_trapezoids = (total_trapezoids - sum_C_n_2_sq + MOD) % MOD

        inv2 = pow(2, MOD - 2, MOD)
        total_trapezoids = (total_trapezoids * inv2) % MOD

        return total_trapezoids
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <stdio.h>

typedef struct {
    int x;
    int y;
} Point;

int comparePoints(const void *a, const void *b) {
    Point *pa = (Point *)a;
    Point *pb = (Point *)b;
    if (pa->y != pb->y) {
        return pa->y - pb->y;
    }
    return pa->x - pb->x;
}

long long power(long long base, long long exp) {
    long long res = 1;
    long long MOD = 1000000007;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

int countTrapezoids(int** points, int pointsSize, int* pointsColSize) {
    long long MOD = 1000000007;

    Point* pts = (Point*)malloc(pointsSize * sizeof(Point));
    if (pts == NULL) {
        return 0; 
    }
    for (int i = 0; i < pointsSize; ++i) {
        pts[i].x = points[i][0];
        pts[i].y = points[i][1];
    }

    qsort(pts, pointsSize, sizeof(Point), comparePoints);

    long long sum_C_n_2 = 0;
    long long sum_C_n_2_sq = 0;

    int i = 0;
    while (i < pointsSize) {
        int current_y = pts[i].y;
        long long count_on_current_y = 0;
        int j = i;
        while (j < pointsSize && pts[j].y == current_y) {
            count_on_current_y++;
            j++;
        }

        if (count_on_current_y >= 2) {
            long long c_n_2 = (count_on_current_y * (count_on_current_y - 1) / 2) % MOD;

            sum_C_n_2 = (sum_C_n_2 + c_n_2) % MOD;
            sum_C_n_2_sq = (sum_C_n_2_sq + (c_n_2 * c_n_2) % MOD) % MOD;
        }
        i = j;
    }

    long long total_trapezoids = (sum_C_n_2 * sum_C_n_2) % MOD;
    total_trapezoids = (total_trapezoids - sum_C_n_2_sq + MOD) % MOD;

    long long inv2 = power(2, MOD - 2);

    total_trapezoids = (total_trapezoids * inv2) % MOD;

    free(pts);
    return (int)total_trapezoids;
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
    public int CountTrapezoids(IList<IList<int>> points) {
        long MOD = 1_000_000_007;

        Dictionary<int, List<int>> yToXCoords = new Dictionary<int, List<int>>();
        foreach (var point in points) {
            int x = point[0];
            int y = point[1];
            if (!yToXCoords.ContainsKey(y)) {
                yToXCoords[y] = new List<int>();
            }
            yToXCoords[y].Add(x);
        }

        long sumCn2 = 0;
        long sumCn2Sq = 0;

        foreach (var xCoordsList in yToXCoords.Values) {
            long n = xCoordsList.Count;
            if (n >= 2) {
                long cn2 = (n * (n - 1) / 2) % MOD;

                sumCn2 = (sumCn2 + cn2) % MOD;
                sumCn2Sq = (sumCn2Sq + (cn2 * cn2) % MOD) % MOD;
            }
        }

        long totalTrapezoids = (sumCn2 * sumCn2) % MOD;
        totalTrapezoids = (totalTrapezoids - sumCn2Sq + MOD) % MOD;

        long inv2 = 500000004; // (MOD + 1) / 2

        totalTrapezoids = (totalTrapezoids * inv2) % MOD;

        return (int) totalTrapezoids;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[][]} points
 * @return {number}
 */
var countTrapezoids = function(points) {
    const MOD = 1_000_000_007;

    const yToXCoords = new Map();
    for (const point of points) {
        const x = point[0];
        const y = point[1];
        if (!yToXCoords.has(y)) {
            yToXCoords.set(y, []);
        }
        yToXCoords.get(y).push(x);
    }

    let sumCn2 = 0;
    let sumCn2Sq = 0;

    for (const xCoords of yToXCoords.values()) {
        const n = xCoords.length;
        if (n >= 2) {
            const cn2 = (n * (n - 1) / 2) % MOD;

            sumCn2 = (sumCn2 + cn2) % MOD;
            sumCn2Sq = (sumCn2Sq + (cn2 * cn2) % MOD) % MOD;
        }
    }

    let totalTrapezoids = (sumCn2 * sumCn2) % MOD;
    totalTrapezoids = (totalTrapezoids - sumCn2Sq + MOD) % MOD;

    const inv2 = 500000004; // (MOD + 1) / 2

    totalTrapezoids = (totalTrapezoids * inv2) % MOD;

    return totalTrapezoids;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countTrapezoids(points: number[][]): number {
    const MOD = 1_000_000_007;

    const yToXCoords = new Map<number, number[]>();
    for (const point of points) {
        const x = point[0];
        const y = point[1];
        if (!yToXCoords.has(y)) {
            yToXCoords.set(y, []);
        }
        yToXCoords.get(y)!.push(x);
    }

    let sumCn2 = 0;
    let sumCn2Sq = 0;

    for (const xCoords of yToXCoords.values()) {
        const n = xCoords.length;
        if (n >= 2) {
            const cn2 = (n * (n - 1) / 2) % MOD;

            sumCn2 = (sumCn2 + cn2) % MOD;
            sumCn2Sq = (sumCn2Sq + (cn2 * cn2) % MOD) % MOD;
        }
    }

    let totalTrapezoids = (sumCn2 * sumCn2) % MOD;
    totalTrapezoids = (totalTrapezoids - sumCn2Sq + MOD) % MOD;

    const inv2 = 500000004; // (MOD + 1) / 2

    totalTrapezoids = (totalTrapezoids * inv2) % MOD;

    return totalTrapezoids;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function countTrapezoids($points) {
        $MOD = 1_000_000_007;

        $yToXCoords = [];
        foreach ($points as $point) {
            $x = $point[0];
            $y = $point[1];
            if (!isset($yToXCoords[$y])) {
                $yToXCoords[$y] = [];
            }
            $yToXCoords[$y][] = $x;
        }

        $sumCn2 = 0;
        $sumCn2Sq = 0;

        foreach ($yToXCoords as $y => $xCoords) {
            $n = count($xCoords);
            if ($n >= 2) {
                $cn2 = (int)(((float)$n * ($n - 1) / 2) % $MOD);

                $sumCn2 = ($sumCn2 + $cn2) % $MOD;
                $sumCn2Sq = ($sumCn2Sq + ($cn2 * $cn2) % $MOD) % $MOD;
            }
        }

        $totalTrapezoids = ($sumCn2 * $sumCn2) % $MOD;
        $totalTrapezoids = ($totalTrapezoids - $sumCn2Sq + $MOD) % $MOD;

        $inv2 = 500000004; // (MOD + 1) / 2

        $totalTrapezoids = ($totalTrapezoids * $inv2) % $MOD;

        return $totalTrapezoids;
    }
}
?>
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
import Foundation

class Solution {
    func countTrapezoids(_ points: [[Int]]) -> Int {
        let MOD: Int = 1_000_000_007

        var yToXCoords: [Int: [Int]] = [:]
        for point in points {
            let x = point[0]
            let y = point[1]
            yToXCoords[y, default: []].append(x)
        }

        var sumCn2: Int = 0
        var sumCn2Sq: Int = 0

        for xCoords in yToXCoords.values {
            let n = xCoords.count
            if n >= 2 {
                let cn2 = (n * (n - 1) / 2) % MOD

                sumCn2 = (sumCn2 + cn2) % MOD
                sumCn2Sq = (sumCn2Sq + (cn2 * cn2) % MOD) % MOD
            }
        }

        var totalTrapezoids = (sumCn2 * sumCn2) % MOD
        totalTrapezoids = (totalTrapezoids - sumCn2Sq + MOD) % MOD

        let inv2 = 500000004 // (MOD + 1) / 2

        totalTrapezoids = (totalTrapezoids * inv2) % MOD

        return totalTrapezoids
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun countTrapezoids(points: List<List<Int>>): Int {
        val MOD = 1_000_000_007L

        val yToXCoords = mutableMapOf<Int, MutableList<Int>>()
        for (point in points) {
            val x = point[0]
            val y = point[1]
            yToXCoords.getOrPut(y) { mutableListOf() }.add(x)
        }

        var sumCn2: Long = 0
        var sumCn2Sq: Long = 0

        for (xCoords in yToXCoords.values) {
            val n = xCoords.size.toLong()
            if (n >= 2) {
                val cn2 = (n * (n - 1) / 2) % MOD

                sumCn2 = (sumCn2 + cn2) % MOD
                sumCn2Sq = (sumCn2Sq + (cn2 * cn2) % MOD) % MOD
            }
        }

        var totalTrapezoids = (sumCn2 * sumCn2) % MOD
        totalTrapezoids = (totalTrapezoids - sumCn2Sq + MOD) % MOD

        val inv2 = 500000004L // (MOD + 1) / 2

        totalTrapezoids = (totalTrapezoids * inv2) % MOD

        return totalTrapezoids.toInt()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:collection';

class Solution {
  int countTrapezoids(List<List<int>> points) {
    final int MOD = 1_000_000_007;

    final Map<int, List<int>> yToXCoords = HashMap();
    for (final point in points) {
      final int x = point[0];
      final int y = point[1];
      yToXCoords.putIfAbsent(y, () => []).add(x);
    }

    int sumCn2 = 0;
    int sumCn2Sq = 0;

    for (final xCoords in yToXCoords.values) {
      final int n = xCoords.length;
      if (n >= 2) {
        final int cn2 = ((n * (n - 1)) ~/ 2) % MOD;

        sumCn2 = (sumCn2 + cn2) % MOD;
        sumCn2Sq = (sumCn2Sq + (cn2 * cn2) % MOD) % MOD;
      }
    }

    int totalTrapezoids = (sumCn2 * sumCn2) % MOD;
    totalTrapezoids = (totalTrapezoids - sumCn2Sq + MOD) % MOD;

    final int inv2 = 500000004; // (MOD + 1) / 2

    totalTrapezoids = (totalTrapezoids * inv2) % MOD;

    return totalTrapezoids;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

import (
	"fmt"
)

func countTrapezoids(points [][]int) int {
	MOD := 1_000_000_007

	yToXCoords := make(map[int][]int)
	for _, point := range points {
		x, y := point[0], point[1]
		yToXCoords[y] = append(yToXCoords[y], x)
	}

	var sumCn2 int = 0
	var sumCn2Sq int = 0

	for _, xCoords := range yToXCoords {
		n := len(xCoords)
		if n >= 2 {
			cn2 := (n * (n - 1) / 2) % MOD

			sumCn2 = (sumCn2 + cn2) % MOD
			sumCn2Sq = (sumCn2Sq + (cn2 * cn2) % MOD) % MOD
		}
	}

	totalTrapezoids := (sumCn2 * sumCn2) % MOD
	totalTrapezoids = (totalTrapezoids - sumCn2Sq + MOD) % MOD

	inv2 := 500000004 // (MOD + 1) / 2

	totalTrapezoids = (totalTrapezoids * inv2) % MOD

	return totalTrapezoids
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[][]} points
# @return {Integer}
def count_trapezoids(points)
    mod = 1_000_000_007

    y_to_x_coords = Hash.new { |hash, key| hash[key] = [] }
    points.each do |x, y|
        y_to_x_coords[y] << x
    end

    sum_cn2 = 0
    sum_cn2_sq = 0

    y_to_x_coords.each_value do |x_coords|
        n = x_coords.length
        if n >= 2
            cn2 = (n * (n - 1) / 2) % mod

            sum_cn2 = (sum_cn2 + cn2) % mod
            sum_cn2_sq = (sum_cn2_sq + (cn2 * cn2) % mod) % mod
        end
    end

    total_trapezoids = (sum_cn2 * sum_cn2) % mod
    total_trapezoids = (total_trapezoids - sum_cn2_sq + mod) % mod

    inv2 = 500000004 # (mod + 1) / 2

    total_trapezoids = (total_trapezoids * inv2) % mod

    return total_trapezoids
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

object Solution {
    def countTrapezoids(points: Array[Array[Int]]): Int = {
        val MOD: Long = 1_000_000_007L

        val yToXCoords = mutable.HashMap.empty[Int, mutable.ListBuffer[Int]]
        for (point <- points) {
            val x = point(0)
            val y = point(1)
            yToXCoords.getOrElseUpdate(y, mutable.ListBuffer.empty[Int]).append(x)
        }

        var sumCn2: Long = 0
        var sumCn2Sq: Long = 0

        for (xCoords <- yToXCoords.values) {
            val n = xCoords.length.toLong
            if (n >= 2) {
                val cn2 = (n * (n - 1) / 2) % MOD

                sumCn2 = (sumCn2 + cn2) % MOD
                sumCn2Sq = (sumCn2Sq + (cn2 * cn2) % MOD) % MOD
            }
        }

        var totalTrapezoids = (sumCn2 * sumCn2) % MOD
        totalTrapezoids = (totalTrapezoids - sumCn2Sq + MOD) % MOD

        val inv2 = 500000004L // (MOD + 1) / 2

        totalTrapezoids = (totalTrapezoids * inv2) % MOD

        totalTrapezoids.toInt
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
    pub fn count_trapezoids(points: Vec<Vec<i32>>) -> i32 {
        let modular: i64 = 1_000_000_007;

        let mut y_to_x_coords: HashMap<i32, Vec<i32>> = HashMap::new();
        for point in points {
            let x = point[0];
            let y = point[1];
            y_to_x_coords.entry(y).or_insert_with(Vec::new).push(x);
        }

        let mut sum_cn2: i64 = 0;
        let mut sum_cn2_sq: i64 = 0;

        for x_coords in y_to_x_coords.values() {
            let n = x_coords.len() as i64;
            if n >= 2 {
                let cn2 = (n * (n - 1) / 2) % modular;

                sum_cn2 = (sum_cn2 + cn2) % modular;
                sum_cn2_sq = (sum_cn2_sq + (cn2 * cn2) % modular) % modular;
            }
        }

        let mut total_trapezoids = (sum_cn2 * sum_cn2) % modular;
        total_trapezoids = (total_trapezoids - sum_cn2_sq + modular) % modular;

        let inv2: i64 = 500000004; // (MOD + 1) / 2

        total_trapezoids = (total_trapezoids * inv2) % modular;

        total_trapezoids as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(provide (struct-out Solution) (method-in Solution count-trapezoids))

(define MOD 1000000007)

(define (power base exp)
  (define (loop res base exp)
    (cond
      [(= exp 0) res]
      [(odd? exp) (loop (modulo (* res base) MOD) (modulo (* base base) MOD) (quotient exp 2))]
      [else (loop res (modulo (* base base) MOD) (quotient exp 2))]))
  (loop 1 (modulo base MOD) exp))

(define (count-trapezoids points)
  (define y-to-x-coords (make-hash))
  (for-each (lambda (point)
              (define x (vector-ref point 0))
              (define y (vector-ref point 1))
              (hash-update! y-to-x-coords y (lambda (lst) (cons x lst)) '()))
            points)

  (define sum-cn2 0)
  (define sum-cn2-sq 0)

  (for-each (lambda (x-coords)
              (define n (length x-coords))
              (when (>= n 2)
                (define cn2 (modulo (quotient (* n (- n 1)) 2) MOD))
                (set! sum-cn2 (modulo (+ sum-cn2 cn2) MOD))
                (set! sum-cn2-sq (modulo (+ sum-cn2-sq (modulo (* cn2 cn2) MOD)) MOD))))
            (hash-values y-to-x-coords))

  (define total-trapezoids (modulo (* sum-cn2 sum-cn2) MOD))
  (set! total-trapezoids (modulo (+ (- total-trapezoids sum-cn2-sq) MOD) MOD))

  (define inv2 (power 2 (- MOD 2)))
  (set! total-trapezoids (modulo (* total-trapezoids inv2) MOD))

  total-trapezoids)

(define-struct Solution ())
(define-method (count-trapezoids (self Solution) points)
  (count-trapezoids points))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([count_trapezoids/1]).

count_trapezoids(Points) ->
    MOD = 1_000_000_007,

    YToXCoords = lists:foldl(
        fun([_X, Y], Acc) ->
            maps:update_with(Y, fun(List) -> List ++ [_X] end, [_X], Acc)
        end,
        maps:new(),
        Points
    ),

    {SumCn2, SumCn2Sq} = maps:fold(
        fun(_Y, XCoords, {AccSumCn2, AccSumCn2Sq}) ->
            N = length(XCoords),
            if N >= 2 ->
                Cn2 = ((N * (N - 1)) div 2) rem MOD,
                NewAccSumCn2 = (AccSumCn2 + Cn2) rem MOD,
                NewAccSumCn2Sq = (AccSumCn2Sq + (Cn2 * Cn2) rem MOD) rem MOD,
                {NewAccSumCn2, NewAccSumCn2Sq};
            true ->
                {AccSumCn2, AccSumCn2Sq}
            end
        end,
        {0, 0},
        YToXCoords
    ),

    TotalTrapezoids = (SumCn2 * SumCn2) rem MOD,
    TotalTrapezoidsAdjusted = (TotalTrapezoids - SumCn2Sq + MOD) rem MOD,

    Inv2 = 500000004, % (MOD + 1) div 2

    (TotalTrapezoidsAdjusted * Inv2) rem MOD.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec count_trapezoids(points :: [[integer]]) :: integer
  def count_trapezoids(points) do
    mod = 1_000_000_007

    y_to_x_coords =
      Enum.reduce(points, %{}, fn [x, y], acc ->
        Map.update(acc, y, [x], fn list -> [x | list] end)
      end)

    {sum_cn2, sum_cn2_sq} =
      Enum.reduce(Map.values(y_to_x_coords), {0, 0}, fn x_coords, {acc_sum_cn2, acc_sum_cn2_sq} ->
        n = length(x_coords)
        if n >= 2 do
          cn2 = div(n * (n - 1), 2) |> rem(mod)
          new_acc_sum_cn2 = (acc_sum_cn2 + cn2) |> rem(mod)
          new_acc_sum_cn2_sq = (acc_sum_cn2_sq + (cn2 * cn2) |> rem(mod)) |> rem(mod)
          {new_acc_sum_cn2, new_acc_sum_cn2_sq}
        else
          {acc_sum_cn2, acc_sum_cn2_sq}
        end
      end)

    total_trapezoids = (sum_cn2 * sum_cn2) |> rem(mod)
    total_trapezoids = (total_trapezoids - sum_cn2_sq + mod) |> rem(mod)

    inv2 = 500_000_004 # (mod + 1) / 2

    (total_trapezoids * inv2) |> rem(mod)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N), where N is the number of points. This is because we first iterate through all N points to group them by their y-coordinates, which takes O(N) time (average for hash map, O(N log D) for tree map where D is distinct y-coordinates, but D <= N). Then, we iterate through the distinct y-coordinate groups (at most D groups) to calculate the combinations and update sums. This takes O(D) time. Since D <= N, the overall time complexity is dominated by O(N).

- **Space Complexity:** The space complexity is O(N), where N is the number of points. This is primarily due to storing the points grouped by their y-coordinates in a hash map (or similar data structure). In the worst case, all N points could have distinct y-coordinates, or all could have the same y-coordinate, but in either scenario, we store approximately N x-coordinates in total across all lists in the map.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-02 01:06:30 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by first grouping the points by their y-coordinates. Then, we can choose two distinct groups (two horizontal lines), and from each group select two points to form a trapezoid. This approach ensures that we consider all possible combinations of points that can form a horizontal trapezoid. The key intuition here is that for a line parallel to the x-axis, all its points must share the same y-coordinate, which allows us to group the points by their y-coordinates and then select points from each group to form a trapezoid.

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-cpp-llama-3-3-70b-versatile" checked>
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-java-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-python-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-python3-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-c-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-csharp-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-javascript-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-typescript-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-php-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-swift-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-kotlin-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-dart-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-go-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-ruby-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-scala-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-rust-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-racket-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-erlang-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-elixir-llama-3-3-70b-versatile">
  <div class="tab-labels">
    <label for="lang-cpp-llama-3-3-70b-versatile">C++</label>
    <label for="lang-java-llama-3-3-70b-versatile">Java</label>
    <label for="lang-python-llama-3-3-70b-versatile">Python</label>
    <label for="lang-python3-llama-3-3-70b-versatile">Python3</label>
    <label for="lang-c-llama-3-3-70b-versatile">C</label>
    <label for="lang-csharp-llama-3-3-70b-versatile">C#</label>
    <label for="lang-javascript-llama-3-3-70b-versatile">JavaScript</label>
    <label for="lang-typescript-llama-3-3-70b-versatile">TypeScript</label>
    <label for="lang-php-llama-3-3-70b-versatile">PHP</label>
    <label for="lang-swift-llama-3-3-70b-versatile">Swift</label>
    <label for="lang-kotlin-llama-3-3-70b-versatile">Kotlin</label>
    <label for="lang-dart-llama-3-3-70b-versatile">Dart</label>
    <label for="lang-go-llama-3-3-70b-versatile">Go</label>
    <label for="lang-ruby-llama-3-3-70b-versatile">Ruby</label>
    <label for="lang-scala-llama-3-3-70b-versatile">Scala</label>
    <label for="lang-rust-llama-3-3-70b-versatile">Rust</label>
    <label for="lang-racket-llama-3-3-70b-versatile">Racket</label>
    <label for="lang-erlang-llama-3-3-70b-versatile">Erlang</label>
    <label for="lang-elixir-llama-3-3-70b-versatile">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
class Solution {
public:
    int countTrapezoids(vector<vector<int>>& points) {
        map<int, vector<int>> groups;
        for (auto& point : points) {
            groups[point[1]].push_back(point[0]);
        }
        int count = 0;
        for (auto& group1 : groups) {
            for (auto& group2 : groups) {
                if (group1.first != group2.first) {
                    int n1 = group1.second.size(), n2 = group2.second.size();
                    count += n1 * (n1 - 1) / 2 * n2 * (n2 - 1) / 2;
                }
            }
        }
        return count % (1000000007);
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int countTrapezoids(int[][] points) {
        Map<Integer, List<Integer>> groups = new HashMap<>();
        for (int[] point : points) {
            groups.computeIfAbsent(point[1], k -> new ArrayList<>()).add(point[0]);
        }
        int count = 0;
        for (int y1 : groups.keySet()) {
            for (int y2 : groups.keySet()) {
                if (y1 != y2) {
                    int n1 = groups.get(y1).size(), n2 = groups.get(y2).size();
                    count += n1 * (n1 - 1) / 2 * n2 * (n2 - 1) / 2;
                }
            }
        }
        return count % 1000000007;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        groups = {}
        for x, y in points:
            if y not in groups:
                groups[y] = []
            groups[y].append(x)
        count = 0
        for y1 in groups:
            for y2 in groups:
                if y1 != y2:
                    n1, n2 = len(groups[y1]), len(groups[y2])
                    count += n1 * (n1 - 1) // 2 * n2 * (n2 - 1) // 2
        return count % 1000000007
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        groups = {}
        for x, y in points:
            if y not in groups:
                groups[y] = []
            groups[y].append(x)
        count = 0
        for y1 in groups:
            for y2 in groups:
                if y1 != y2:
                    n1, n2 = len(groups[y1]), len(groups[y2])
                    count += n1 * (n1 - 1) // 2 * n2 * (n2 - 1) // 2
        return count % 1000000007
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
typedef struct {
    int x;
    int y;
} Point;

int compare(const void *a, const void *b) {
    Point *p1 = (Point *)a;
    Point *p2 = (Point *)b;
    return p1->y - p2->y;
}

int countTrapezoids(int **points, int pointsSize, int *pointsColSize) {
    int count = 0;
    qsort(points, pointsSize, sizeof(int *), compare);
    for (int i = 0; i < pointsSize; i++) {
        for (int j = i + 1; j < pointsSize; j++) {
            if (points[i][1] != points[j][1]) {
                int n1 = 0, n2 = 0;
                for (int k = 0; k < pointsSize; k++) {
                    if (points[k][1] == points[i][1]) n1++;
                    if (points[k][1] == points[j][1]) n2++;
                }
                count += n1 * (n1 - 1) / 2 * n2 * (n2 - 1) / 2;
            }
        }
    }
    return count % 1000000007;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int CountTrapezoids(int[][] points) {
        Dictionary<int, List<int>> groups = new Dictionary<int, List<int>>();
        foreach (int[] point in points) {
            if (!groups.ContainsKey(point[1])) {
                groups[point[1]] = new List<int>();
            }
            groups[point[1]].Add(point[0]);
        }
        int count = 0;
        foreach (int y1 in groups.Keys) {
            foreach (int y2 in groups.Keys) {
                if (y1 != y2) {
                    int n1 = groups[y1].Count, n2 = groups[y2].Count;
                    count += n1 * (n1 - 1) / 2 * n2 * (n2 - 1) / 2;
                }
            }
        }
        return count % 1000000007;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var countTrapezoids = function(points) {
    let groups = {};
    for (let point of points) {
        if (!(point[1] in groups)) {
            groups[point[1]] = [];
        }
        groups[point[1]].push(point[0]);
    }
    let count = 0;
    for (let y1 in groups) {
        for (let y2 in groups) {
            if (y1 != y2) {
                let n1 = groups[y1].length, n2 = groups[y2].length;
                count += n1 * (n1 - 1) / 2 * n2 * (n2 - 1) / 2;
            }
        }
    }
    return count % 1000000007;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countTrapezoids(points: number[][]): number {
    let groups: { [key: number]: number[] } = {};
    for (let point of points) {
        if (!(point[1] in groups)) {
            groups[point[1]] = [];
        }
        groups[point[1]].push(point[0]);
    }
    let count: number = 0;
    for (let y1 in groups) {
        for (let y2 in groups) {
            if (y1 != y2) {
                let n1: number = groups[y1].length, n2: number = groups[y2].length;
                count += n1 * (n1 - 1) / 2 * n2 * (n2 - 1) / 2;
            }
        }
    }
    return count % 1000000007;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
$count = 0;
$groups = [];
foreach ($points as $point) {
    if (!isset($groups[$point[1]])) {
        $groups[$point[1]] = [];
    }
    $groups[$point[1]][] = $point[0];
}
foreach ($groups as $y1 => $group1) {
    foreach ($groups as $y2 => $group2) {
        if ($y1 != $y2) {
            $n1 = count($group1);
            $n2 = count($group2);
            $count += $n1 * ($n1 - 1) / 2 * $n2 * ($n2 - 1) / 2;
        }
    }
}
echo $count % 1000000007;
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func countTrapezoids(_ points: [[Int]]) -> Int {
        var groups: [Int: [Int]] = [:]
        for point in points {
            if groups[point[1]] == nil {
                groups[point[1]] = []
            }
            groups[point[1]]!.append(point[0])
        }
        var count = 0
        for y1 in groups.keys {
            for y2 in groups.keys {
                if y1 != y2 {
                    let n1 = groups[y1]!.count
                    let n2 = groups[y2]!.count
                    count += n1 * (n1 - 1) / 2 * n2 * (n2 - 1) / 2
                }
            }
        }
        return count % 1000000007
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun countTrapezoids(points: Array<IntArray>): Int {
        val groups = mutableMapOf<Int, MutableList<Int>>()
        for (point in points) {
            if (!groups.containsKey(point[1])) {
                groups[point[1]] = mutableListOf()
            }
            groups[point[1]]!!.add(point[0])
        }
        var count = 0
        for (y1 in groups.keys) {
            for (y2 in groups.keys) {
                if (y1 != y2) {
                    val n1 = groups[y1]!!.size
                    val n2 = groups[y2]!!.size
                    count += n1 * (n1 - 1) / 2 * n2 * (n2 - 1) / 2
                }
            }
        }
        return count % 1000000007
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int countTrapezoids(List<List<int>> points) {
        Map<int, List<int>> groups = {};
        for (var point in points) {
            if (!groups.containsKey(point[1])) {
                groups[point[1]] = [];
            }
            groups[point[1]]!.add(point[0]);
        }
        int count = 0;
        for (var y1 in groups.keys) {
            for (var y2 in groups.keys) {
                if (y1 != y2) {
                    int n1 = groups[y1]!.length;
                    int n2 = groups[y2]!.length;
                    count += n1 * (n1 - 1) ~/ 2 * n2 * (n2 - 1) ~/ 2;
                }
            }
        }
        return count % 1000000007;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

import (
    "fmt"
)

type Solution struct{}

func (s Solution) countTrapezoids(points [][]int) int {
    groups := map[int][]int{}
    for _, point := range points {
        if _, ok := groups[point[1]]; !ok {
            groups[point[1]] = []int{}
        }
        groups[point[1]] = append(groups[point[1]], point[0])
    }
    count := 0
    for y1 := range groups {
        for y2 := range groups {
            if y1 != y2 {
                n1 := len(groups[y1])
                n2 := len(groups[y2])
                count += n1*(n1-1)/2 * n2*(n2-1)/2
            }
        }
    }
    return count % 1000000007
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def count_trapezoids(points)
    groups = {}
    points.each do |point|
        if !groups.key?(point[1])
            groups[point[1]] = []
        end
        groups[point[1]] << point[0]
    end
    count = 0
    groups.keys.each do |y1|
        groups.keys.each do |y2|
            if y1 != y2
                n1 = groups[y1].size
                n2 = groups[y2].size
                count += n1 * (n1 - 1) / 2 * n2 * (n2 - 1) / 2
            end
        end
    end
    count % 1000000007
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def countTrapezoids(points: Array[Array[Int]]): Int = {
        val groups = scala.collection.mutable.Map[Int, List[Int]]()
        for (point <- points) {
            if (!groups.contains(point(1))) {
                groups(point(1)) = List()
            }
            groups(point(1)) = point(0) :: groups(point(1))
        }
        var count = 0
        for (y1 <- groups.keys) {
            for (y2 <- groups.keys) {
                if (y1 != y2) {
                    val n1 = groups(y1).size
                    val n2 = groups(y2).size
                    count += n1 * (n1 - 1) / 2 * n2 * (n2 - 1) / 2
                }
            }
        }
        count % 1000000007
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
struct Solution;

impl Solution {
    pub fn count_trapezoids(points: Vec<Vec<i32>>) -> i32 {
        let mut groups: std::collections::HashMap<i32, Vec<i32>> = std::collections::HashMap::new();
        for point in points {
            if !groups.contains_key(&point[1]) {
                groups.insert(point[1], Vec::new());
            }
            groups.get_mut(&point[1]).unwrap().push(point[0]);
        }
        let mut count = 0;
        for y1 in groups.keys() {
            for y2 in groups.keys() {
                if y1 != y2 {
                    let n1 = groups.get(y1).unwrap().len();
                    let n2 = groups.get(y2).unwrap().len();
                    count += n1 * (n1 - 1) / 2 * n2 * (n2 - 1) / 2;
                }
            }
        }
        count % 1000000007
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define (count-trapezoids points)
    (let ((groups (make-hash)))
        (for-each (lambda (point)
                    (let ((y (cadr point)))
                        (if (not (hash-ref groups y))
                            (hash-set! groups y '()))
                        (hash-set! groups y (cons (car point) (hash-ref groups y)))))
                  points)
        (let loop ((y1 (hash-keys groups))
                   (count 0))
            (if (null? y1)
                (modulo count 1000000007)
                (let loop2 ((y2 (hash-keys groups))
                           (count2 count))
                    (if (null? y2)
                        (loop (cdr y1) count2)
                        (if (not (eq? (car y1) (car y2)))
                            (loop2 (cdr y2) (+ count2 (/ (* (length (hash-ref groups (car y1)))
                                                    (- (length (hash-ref groups (car y1))) 1))
                                                  2)
                                                  (/ (* (length (hash-ref groups (car y2)))
                                                    (- (length (hash-ref groups (car y2))) 1))
                                                  2)))
                            (loop2 (cdr y2) count2))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([count_trapezoids/1]).

count_trapezoids(Points) ->
    Groups = group_points(Points),
    Count = count_trapezoids(Groups, 0),
    Count rem 1000000007.

group_points(Points) ->
    group_points(Points, []).

group_points([], Groups) ->
    lists:reverse(Groups);

group_points([Point|Points], Groups) ->
    {Y, X} = Point,
    case lists:keytake(Y, 1, Groups) of
        {value, {Y, Xs}, Groups1} ->
            group_points(Points, [{Y, [X|Xs]}|Groups1]);
        false ->
            group_points(Points, [{Y, [X]}|Groups])
    end.

count_trapezoids([], Count) -> Count;

count_trapezoids([Group|Groups], Count) ->
    count_trapezoids(Groups, Count + count_trapezoids(Group, Groups, 0)).

count_trapezoids({Y1, Xs1}, Groups, Count) ->
    count_trapezoids(Groups, Count, Y1, Xs1, length(Xs1)).

count_trapezoids([], _, _, _, _) -> 0;

count_trapezoids([Group|Groups], Count, Y1, Xs1, N1) ->
    {Y2, Xs2} = Group,
    if Y1 =:= Y2 ->
        count_trapezoids(Groups, Count, Y1, Xs1, N1);
    true ->
        count_trapezoids(Groups, Count + (N1 * (N1 - 1) div 2) * (length(Xs2) * (length(Xs2) - 1) div 2), Y1, Xs1, N1)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
    def count_trapezoids(points) do
        groups = Enum.reduce(points, %{}, fn [x, y], groups ->
            Map.update(groups, y, [x], fn x -> [x | x] end)
        end)
        count = Enum.reduce(groups, 0, fn {y1, xs1}, count ->
            Enum.reduce(groups, count, fn {y2, xs2}, count ->
                if y1 != y2 do
                    count + length(xs1) * (length(xs1) - 1) * length(xs2) * (length(xs2) - 1) div 4
                else
                    count
                end
            end)
        end)
        rem(count, 1_000_000_007)
    end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this solution is O(n^2 * m^2) where n is the number of distinct y-coordinates and m is the maximum number of points with the same y-coordinate. This is because we are iterating over all pairs of distinct y-coordinates and for each pair, we are iterating over all pairs of points in each group.

- **Space Complexity:** The space complexity of this solution is O(n * m) where n is the number of distinct y-coordinates and m is the maximum number of points with the same y-coordinate. This is because we need to store the points grouped by their y-coordinates.

</div>
</details>
