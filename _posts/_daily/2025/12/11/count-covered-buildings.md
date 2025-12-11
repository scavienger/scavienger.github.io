---
layout: post
title: "Count Covered Buildings"
date: 2025-12-11 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Sorting"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/count-covered-buildings/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <unordered_map>\n#include <algorithm> // For\
        \ std::min and std::max\n#include <limits>    // For std::numeric_limits\n\n\
        class Solution {\npublic:\n    int countCoveredBuildings(int n, std::vector<std::vector<int>>&\
        \ buildings) {\n        std::unordered_map<int, int> min_y_for_x;\n        std::unordered_map<int,\
        \ int> max_y_for_x;\n        std::unordered_map<int, int> min_x_for_y;\n   \
        \     std::unordered_map<int, int> max_x_for_y;\n\n        for (const auto&\
        \ building : buildings) {\n            int x = building[0];\n            int\
        \ y = building[1];\n\n            if (min_y_for_x.find(x) == min_y_for_x.end())\
        \ {\n                min_y_for_x[x] = std::numeric_limits<int>::max();\n   \
        \         }\n            min_y_for_x[x] = std::min(min_y_for_x[x], y);\n\n \
        \           if (max_y_for_x.find(x) == max_y_for_x.end()) {\n              \
        \  max_y_for_x[x] = std::numeric_limits<int>::min();\n            }\n      \
        \      max_y_for_x[x] = std::max(max_y_for_x[x], y);\n\n            if (min_x_for_y.find(y)\
        \ == min_x_for_y.end()) {\n                min_x_for_y[y] = std::numeric_limits<int>::max();\n\
        \            }\n            min_x_for_y[y] = std::min(min_x_for_y[y], x);\n\n\
        \            if (max_x_for_y.find(y) == max_x_for_y.end()) {\n             \
        \   max_x_for_y[y] = std::numeric_limits<int>::min();\n            }\n     \
        \       max_x_for_y[y] = std::max(max_x_for_y[y], x);\n        }\n\n       \
        \ int uncovered_count = 0;\n        for (const auto& building : buildings) {\n\
        \            int x = building[0];\n            int y = building[1];\n\n    \
        \        if (y == min_y_for_x[x] ||\n                y == max_y_for_x[x] ||\n\
        \                x == min_x_for_y[y] ||\n                x == max_x_for_y[y])\
        \ {\n                uncovered_count++;\n            }\n        }\n\n      \
        \  return buildings.size() - uncovered_count;\n    }\n};"
      java: "import java.util.HashMap;\nimport java.util.List;\n\nclass Solution {\n\
        \    public int countCoveredBuildings(int n, int[][] buildings) {\n        HashMap<Integer,\
        \ Integer> minYForX = new HashMap<>();\n        HashMap<Integer, Integer> maxYForX\
        \ = new HashMap<>();\n        HashMap<Integer, Integer> minXForY = new HashMap<>();\n\
        \        HashMap<Integer, Integer> maxXForY = new HashMap<>();\n\n        for\
        \ (int[] building : buildings) {\n            int x = building[0];\n       \
        \     int y = building[1];\n\n            minYForX.put(x, Math.min(minYForX.getOrDefault(x,\
        \ Integer.MAX_VALUE), y));\n            maxYForX.put(x, Math.max(maxYForX.getOrDefault(x,\
        \ Integer.MIN_VALUE), y));\n            minXForY.put(y, Math.min(minXForY.getOrDefault(y,\
        \ Integer.MAX_VALUE), x));\n            maxXForY.put(y, Math.max(maxXForY.getOrDefault(y,\
        \ Integer.MIN_VALUE), x));\n        }\n\n        int uncoveredCount = 0;\n \
        \       for (int[] building : buildings) {\n            int x = building[0];\n\
        \            int y = building[1];\n\n            if (y == minYForX.get(x) ||\n\
        \                y == maxYForX.get(x) ||\n                x == minXForY.get(y)\
        \ ||\n                x == maxXForY.get(y)) {\n                uncoveredCount++;\n\
        \            }\n        }\n\n        return buildings.length - uncoveredCount;\n\
        \    }\n}"
      python: "import collections\n\nclass Solution:\n    def countCoveredBuildings(self,\
        \ n: int, buildings: List[List[int]]) -> int:\n        min_y_for_x = collections.defaultdict(lambda:\
        \ float('inf'))\n        max_y_for_x = collections.defaultdict(lambda: float('-inf'))\n\
        \        min_x_for_y = collections.defaultdict(lambda: float('inf'))\n     \
        \   max_x_for_y = collections.defaultdict(lambda: float('-inf'))\n\n       \
        \ for x, y in buildings:\n            min_y_for_x[x] = min(min_y_for_x[x], y)\n\
        \            max_y_for_x[x] = max(max_y_for_x[x], y)\n            min_x_for_y[y]\
        \ = min(min_x_for_y[y], x)\n            max_x_for_y[y] = max(max_x_for_y[y],\
        \ x)\n\n        uncovered_count = 0\n        for x, y in buildings:\n      \
        \      if y == min_y_for_x[x] or \\\n               y == max_y_for_x[x] or \\\
        \n               x == min_x_for_y[y] or \\\n               x == max_x_for_y[y]:\n\
        \                uncovered_count += 1\n\n        return len(buildings) - uncovered_count"
      python3: "import collections\n\nclass Solution:\n    def countCoveredBuildings(self,\
        \ n: int, buildings: List[List[int]]) -> int:\n        min_y_for_x = collections.defaultdict(lambda:\
        \ float('inf'))\n        max_y_for_x = collections.defaultdict(lambda: float('-inf'))\n\
        \        min_x_for_y = collections.defaultdict(lambda: float('inf'))\n     \
        \   max_x_for_y = collections.defaultdict(lambda: float('-inf'))\n\n       \
        \ for x, y in buildings:\n            min_y_for_x[x] = min(min_y_for_x[x], y)\n\
        \            max_y_for_x[x] = max(max_y_for_x[x], y)\n            min_x_for_y[y]\
        \ = min(min_x_for_y[y], x)\n            max_x_for_y[y] = max(max_x_for_y[y],\
        \ x)\n\n        uncovered_count = 0\n        for x, y in buildings:\n      \
        \      if y == min_y_for_x[x] or \\\n               y == max_y_for_x[x] or \\\
        \n               x == min_x_for_y[y] or \\\n               x == max_x_for_y[y]:\n\
        \                uncovered_count += 1\n\n        return len(buildings) - uncovered_count"
      c: "#include <stdlib.h> // For malloc, free\n#include <limits.h> // For INT_MAX,\
        \ INT_MIN\n#include <string.h> // For memset\n\n// Helper functions for min/max\n\
        int min(int a, int b) {\n    return a < b ? a : b;\n}\n\nint max(int a, int\
        \ b) {\n    return a > b ? a : b;\n}\n\nint countCoveredBuildings(int n, int**\
        \ buildings, int buildingsSize, int* buildingsColSize) {\n    // Using arrays\
        \ as hash maps, since coordinates are within [1, n]\n    // Max index will be\
        \ n, so size n+1\n    int* min_y_for_x = (int*)malloc((n + 1) * sizeof(int));\n\
        \    int* max_y_for_x = (int*)malloc((n + 1) * sizeof(int));\n    int* min_x_for_y\
        \ = (int*)malloc((n + 1) * sizeof(int));\n    int* max_x_for_y = (int*)malloc((n\
        \ + 1) * sizeof(int));\n\n    // Initialize with extreme values\n    for (int\
        \ i = 0; i <= n; ++i) {\n        min_y_for_x[i] = INT_MAX;\n        max_y_for_x[i]\
        \ = INT_MIN;\n        min_x_for_y[i] = INT_MAX;\n        max_x_for_y[i] = INT_MIN;\n\
        \    }\n\n    for (int i = 0; i < buildingsSize; ++i) {\n        int x = buildings[i][0];\n\
        \        int y = buildings[i][1];\n\n        min_y_for_x[x] = min(min_y_for_x[x],\
        \ y);\n        max_y_for_x[x] = max(max_y_for_x[x], y);\n        min_x_for_y[y]\
        \ = min(min_x_for_y[y], x);\n        max_x_for_y[y] = max(max_x_for_y[y], x);\n\
        \    }\n\n    int uncovered_count = 0;\n    for (int i = 0; i < buildingsSize;\
        \ ++i) {\n        int x = buildings[i][0];\n        int y = buildings[i][1];\n\
        \n        if (y == min_y_for_x[x] ||\n            y == max_y_for_x[x] ||\n \
        \           x == min_x_for_y[y] ||\n            x == max_x_for_y[y]) {\n   \
        \         uncovered_count++;\n        }\n    }\n\n    // Free allocated memory\n\
        \    free(min_y_for_x);\n    free(max_y_for_x);\n    free(min_x_for_y);\n  \
        \  free(max_x_for_y);\n\n    return buildingsSize - uncovered_count;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\nusing System.Linq;\n\
        \npublic class Solution {\n    public int CountCoveredBuildings(int n, int[][]\
        \ buildings) {\n        Dictionary<int, int> minYForX = new Dictionary<int,\
        \ int>();\n        Dictionary<int, int> maxYForX = new Dictionary<int, int>();\n\
        \        Dictionary<int, int> minXForY = new Dictionary<int, int>();\n     \
        \   Dictionary<int, int> maxXForY = new Dictionary<int, int>();\n\n        foreach\
        \ (var building in buildings) {\n            int x = building[0];\n        \
        \    int y = building[1];\n\n            if (!minYForX.ContainsKey(x)) {\n \
        \               minYForX[x] = int.MaxValue;\n                maxYForX[x] = int.MinValue;\n\
        \            }\n            minYForX[x] = Math.Min(minYForX[x], y);\n      \
        \      maxYForX[x] = Math.Max(maxYForX[x], y);\n\n            if (!minXForY.ContainsKey(y))\
        \ {\n                minXForY[y] = int.MaxValue;\n                maxXForY[y]\
        \ = int.MinValue;\n            }\n            minXForY[y] = Math.Min(minXForY[y],\
        \ x);\n            maxXForY[y] = Math.Max(maxXForY[y], x);\n        }\n\n  \
        \      int uncoveredCount = 0;\n        foreach (var building in buildings)\
        \ {\n            int x = building[0];\n            int y = building[1];\n\n\
        \            if (y == minYForX[x] ||\n                y == maxYForX[x] ||\n\
        \                x == minXForY[y] ||\n                x == maxXForY[y]) {\n\
        \                uncoveredCount++;\n            }\n        }\n\n        return\
        \ buildings.Length - uncoveredCount;\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @param {number[][]} buildings\n * @return\
        \ {number}\n */\nvar countCoveredBuildings = function(n, buildings) {\n    const\
        \ minYForX = new Map();\n    const maxYForX = new Map();\n    const minXForY\
        \ = new Map();\n    const maxXForY = new Map();\n\n    for (const [x, y] of\
        \ buildings) {\n        minYForX.set(x, Math.min(minYForX.get(x) ?? Infinity,\
        \ y));\n        maxYForX.set(x, Math.max(maxYForX.get(x) ?? -Infinity, y));\n\
        \        minXForY.set(y, Math.min(minXForY.get(y) ?? Infinity, x));\n      \
        \  maxXForY.set(y, Math.max(maxXForY.get(y) ?? -Infinity, x));\n    }\n\n  \
        \  let uncoveredCount = 0;\n    for (const [x, y] of buildings) {\n        if\
        \ (y === minYForX.get(x) ||\n            y === maxYForX.get(x) ||\n        \
        \    x === minXForY.get(y) ||\n            x === maxXForY.get(y)) {\n      \
        \      uncoveredCount++;\n        }\n    }\n\n    return buildings.length -\
        \ uncoveredCount;\n};"
      typescript: "function countCoveredBuildings(n: number, buildings: number[][]):\
        \ number {\n    const minYForX = new Map<number, number>();\n    const maxYForX\
        \ = new Map<number, number>();\n    const minXForY = new Map<number, number>();\n\
        \    const maxXForY = new Map<number, number>();\n\n    for (const [x, y] of\
        \ buildings) {\n        minYForX.set(x, Math.min(minYForX.get(x) ?? Infinity,\
        \ y));\n        maxYForX.set(x, Math.max(maxYForX.get(x) ?? -Infinity, y));\n\
        \        minXForY.set(y, Math.min(minXForY.get(y) ?? Infinity, x));\n      \
        \  maxXForY.set(y, Math.max(maxXForY.get(y) ?? -Infinity, x));\n    }\n\n  \
        \  let uncoveredCount = 0;\n    for (const [x, y] of buildings) {\n        if\
        \ (y === minYForX.get(x)! ||\n            y === maxYForX.get(x)! ||\n      \
        \      x === minXForY.get(y)! ||\n            x === maxXForY.get(y)!) {\n  \
        \          uncoveredCount++;\n        }\n    }\n\n    return buildings.length\
        \ - uncoveredCount;\n};"
      php: "<?php\nclass Solution {\n\n    /**\n     * @param Integer $n\n     * @param\
        \ Integer[][] $buildings\n     * @return Integer\n     */\n    function countCoveredBuildings($n,\
        \ $buildings) {\n        $minYForX = [];\n        $maxYForX = [];\n        $minXForY\
        \ = [];\n        $maxXForY = [];\n\n        foreach ($buildings as $building)\
        \ {\n            list($x, $y) = $building;\n\n            $minYForX[$x] = min($minYForX[$x]\
        \ ?? PHP_INT_MAX, $y);\n            $maxYForX[$x] = max($maxYForX[$x] ?? PHP_INT_MIN,\
        \ $y);\n            $minXForY[$y] = min($minXForY[$y] ?? PHP_INT_MAX, $x);\n\
        \            $maxXForY[$y] = max($maxXForY[$y] ?? PHP_INT_MIN, $x);\n      \
        \  }\n\n        $uncoveredCount = 0;\n        foreach ($buildings as $building)\
        \ {\n            list($x, $y) = $building;\n\n            if ($y == $minYForX[$x]\
        \ ||\n                $y == $maxYForX[$x] ||\n                $x == $minXForY[$y]\
        \ ||\n                $x == $maxXForY[$y]) {\n                $uncoveredCount++;\n\
        \            }\n        }\n\n        return count($buildings) - $uncoveredCount;\n\
        \    }\n}\n?>"
      swift: "import Foundation\n\nclass Solution {\n    func countCoveredBuildings(_\
        \ n: Int, _ buildings: [[Int]]) -> Int {\n        var minYForX: [Int: Int] =\
        \ [:]\n        var maxYForX: [Int: Int] = [:]\n        var minXForY: [Int: Int]\
        \ = [:]\n        var maxXForY: [Int: Int] = [:]\n\n        for building in buildings\
        \ {\n            let x = building[0]\n            let y = building[1]\n\n  \
        \          minYForX[x] = min(minYForX[x] ?? Int.max, y)\n            maxYForX[x]\
        \ = max(maxYForX[x] ?? Int.min, y)\n            minXForY[y] = min(minXForY[y]\
        \ ?? Int.max, x)\n            maxXForY[y] = max(maxXForY[y] ?? Int.min, x)\n\
        \        }\n\n        var uncoveredCount = 0\n        for building in buildings\
        \ {\n            let x = building[0]\n            let y = building[1]\n\n  \
        \          if y == minYForX[x]! ||\n               y == maxYForX[x]! ||\n  \
        \             x == minXForY[y]! ||\n               x == maxXForY[y]! {\n   \
        \             uncoveredCount += 1\n            }\n        }\n\n        return\
        \ buildings.count - uncoveredCount\n    }\n}"
      kotlin: "import kotlin.math.min\nimport kotlin.math.max\n\nclass Solution {\n\
        \    fun countCoveredBuildings(n: Int, buildings: Array<IntArray>): Int {\n\
        \        val minYForX = mutableMapOf<Int, Int>()\n        val maxYForX = mutableMapOf<Int,\
        \ Int>()\n        val minXForY = mutableMapOf<Int, Int>()\n        val maxXForY\
        \ = mutableMapOf<Int, Int>()\n\n        for (building in buildings) {\n    \
        \        val x = building[0]\n            val y = building[1]\n\n          \
        \  minYForX[x] = min(minYForX.getOrDefault(x, Int.MAX_VALUE), y)\n         \
        \   maxYForX[x] = max(maxYForX.getOrDefault(x, Int.MIN_VALUE), y)\n        \
        \    minXForY[y] = min(minXForY.getOrDefault(y, Int.MAX_VALUE), x)\n       \
        \     maxXForY[y] = max(maxXForY.getOrDefault(y, Int.MIN_VALUE), x)\n      \
        \  }\n\n        var uncoveredCount = 0\n        for (building in buildings)\
        \ {\n            val x = building[0]\n            val y = building[1]\n\n  \
        \          if (y == minYForX[x] ||\n                y == maxYForX[x] ||\n  \
        \              x == minXForY[y] ||\n                x == maxXForY[y]) {\n  \
        \              uncoveredCount++\n            }\n        }\n\n        return\
        \ buildings.size - uncoveredCount\n    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int countCoveredBuildings(int\
        \ n, List<List<int>> buildings) {\n    Map<int, int> minYForX = {};\n    Map<int,\
        \ int> maxYForX = {};\n    Map<int, int> minXForY = {};\n    Map<int, int> maxXForY\
        \ = {};\n\n    for (final building in buildings) {\n      int x = building[0];\n\
        \      int y = building[1];\n\n      minYForX[x] = min(minYForX[x] ?? (1 <<\
        \ 31) - 1, y); // Dart's int.MAX_VALUE for 32-bit\n      maxYForX[x] = max(maxYForX[x]\
        \ ?? -(1 << 31), y); // Dart's int.MIN_VALUE for 32-bit\n      minXForY[y] =\
        \ min(minXForY[y] ?? (1 << 31) - 1, x);\n      maxXForY[y] = max(maxXForY[y]\
        \ ?? -(1 << 31), x);\n    }\n\n    int uncoveredCount = 0;\n    for (final building\
        \ in buildings) {\n      int x = building[0];\n      int y = building[1];\n\n\
        \      if (y == minYForX[x] ||\n          y == maxYForX[x] ||\n          x ==\
        \ minXForY[y] ||\n          x == maxXForY[y]) {\n        uncoveredCount++;\n\
        \      }\n    }\n\n    return buildings.length - uncoveredCount;\n  }\n}"
      go: "package main\n\nimport (\n\t\"math\"\n)\n\nfunc countCoveredBuildings(n int,\
        \ buildings [][]int) int {\n\tminYForX := make(map[int]int)\n\tmaxYForX := make(map[int]int)\n\
        \tminXForY := make(map[int]int)\n\tmaxXForY := make(map[int]int)\n\n\tfor _,\
        \ building := range buildings {\n\t\tx, y := building[0], building[1]\n\n\t\t\
        if _, ok := minYForX[x]; !ok {\n\t\t\tminYForX[x] = math.MaxInt32\n\t\t\tmaxYForX[x]\
        \ = math.MinInt32\n\t\t}\n\t\tminYForX[x] = min(minYForX[x], y)\n\t\tmaxYForX[x]\
        \ = max(maxYForX[x], y)\n\n\t\tif _, ok := minXForY[y]; !ok {\n\t\t\tminXForY[y]\
        \ = math.MaxInt32\n\t\t\tmaxXForY[y] = math.MinInt32\n\t\t}\n\t\tminXForY[y]\
        \ = min(minXForY[y], x)\n\t\tmaxXForY[y] = max(maxXForY[y], x)\n\t}\n\n\tuncoveredCount\
        \ := 0\n\tfor _, building := range buildings {\n\t\tx, y := building[0], building[1]\n\
        \n\t\tif y == minYForX[x] ||\n\t\t\ty == maxYForX[x] ||\n\t\t\tx == minXForY[y]\
        \ ||\n\t\t\tx == maxXForY[y] {\n\t\t\tuncoveredCount++\n\t\t}\n\t}\n\n\treturn\
        \ len(buildings) - uncoveredCount\n}\n\nfunc min(a, b int) int {\n\tif a < b\
        \ {\n\t\treturn a\n\t}\n\treturn b\n}\n\nfunc max(a, b int) int {\n\tif a >\
        \ b {\n\t\treturn a\n\t}\n\treturn b\n}"
      ruby: "# @param {Integer} n\n# @param {Integer[][]} buildings\n# @return {Integer}\n\
        def count_covered_buildings(n, buildings)\n    min_y_for_x = Hash.new { |hash,\
        \ key| hash[key] = Float::INFINITY }\n    max_y_for_x = Hash.new { |hash, key|\
        \ hash[key] = -Float::INFINITY }\n    min_x_for_y = Hash.new { |hash, key| hash[key]\
        \ = Float::INFINITY }\n    max_x_for_y = Hash.new { |hash, key| hash[key] =\
        \ -Float::INFINITY }\n\n    buildings.each do |x, y|\n        min_y_for_x[x]\
        \ = [min_y_for_x[x], y].min\n        max_y_for_x[x] = [max_y_for_x[x], y].max\n\
        \        min_x_for_y[y] = [min_x_for_y[y], x].min\n        max_x_for_y[y] =\
        \ [max_x_for_y[y], x].max\n    end\n\n    uncovered_count = 0\n    buildings.each\
        \ do |x, y|\n        if y == min_y_for_x[x] ||\n           y == max_y_for_x[x]\
        \ ||\n           x == min_x_for_y[y] ||\n           x == max_x_for_y[y]\n  \
        \          uncovered_count += 1\n        end\n    end\n\n    buildings.length\
        \ - uncovered_count\nend"
      scala: "import scala.collection.mutable\nimport scala.math.{min, max}\n\nclass\
        \ Solution {\n    def countCoveredBuildings(n: Int, buildings: Array[Array[Int]]):\
        \ Int = {\n        val minYForX = mutable.Map[Int, Int]().withDefaultValue(Int.MaxValue)\n\
        \        val maxYForX = mutable.Map[Int, Int]().withDefaultValue(Int.MinValue)\n\
        \        val minXForY = mutable.Map[Int, Int]().withDefaultValue(Int.MaxValue)\n\
        \        val maxXForY = mutable.Map[Int, Int]().withDefaultValue(Int.MinValue)\n\
        \n        for (building <- buildings) {\n            val x = building(0)\n \
        \           val y = building(1)\n\n            minYForX(x) = min(minYForX(x),\
        \ y)\n            maxYForX(x) = max(maxYForX(x), y)\n            minXForY(y)\
        \ = min(minXForY(y), x)\n            maxXForY(y) = max(maxXForY(y), x)\n   \
        \     }\n\n        var uncoveredCount = 0\n        for (building <- buildings)\
        \ {\n            val x = building(0)\n            val y = building(1)\n\n  \
        \          if (y == minYForX(x) ||\n                y == maxYForX(x) ||\n  \
        \              x == minXForY(y) ||\n                x == maxXForY(y)) {\n  \
        \              uncoveredCount += 1\n            }\n        }\n\n        buildings.length\
        \ - uncoveredCount\n    }\n}"
      rust: "use std::collections::HashMap;\nuse std::cmp::{min, max};\n\nimpl Solution\
        \ {\n    pub fn count_covered_buildings(n: i32, buildings: Vec<Vec<i32>>) ->\
        \ i32 {\n        let mut min_y_for_x: HashMap<i32, i32> = HashMap::new();\n\
        \        let mut max_y_for_x: HashMap<i32, i32> = HashMap::new();\n        let\
        \ mut min_x_for_y: HashMap<i32, i32> = HashMap::new();\n        let mut max_x_for_y:\
        \ HashMap<i32, i32> = HashMap::new();\n\n        for building in &buildings\
        \ {\n            let x = building[0];\n            let y = building[1];\n\n\
        \            min_y_for_x.entry(x).and_modify(|v| *v = min(*v, y)).or_insert(y);\n\
        \            max_y_for_x.entry(x).and_modify(|v| *v = max(*v, y)).or_insert(y);\n\
        \            min_x_for_y.entry(y).and_modify(|v| *v = min(*v, x)).or_insert(x);\n\
        \            max_x_for_y.entry(y).and_modify(|v| *v = max(*v, x)).or_insert(x);\n\
        \        }\n\n        let mut uncovered_count = 0;\n        for building in\
        \ &buildings {\n            let x = building[0];\n            let y = building[1];\n\
        \n            if y == *min_y_for_x.get(&x).unwrap() ||\n               y ==\
        \ *max_y_for_x.get(&x).unwrap() ||\n               x == *min_x_for_y.get(&y).unwrap()\
        \ ||\n               x == *max_x_for_y.get(&y).unwrap() {\n                uncovered_count\
        \ += 1;\n            }\n        }\n\n        buildings.len() as i32 - uncovered_count\n\
        \    }\n}"
      racket: "#lang racket\n\n(define (count-covered-buildings n buildings)\n  (define\
        \ min-y-for-x (make-hash))\n  (define max-y-for-x (make-hash))\n  (define min-x-for-y\
        \ (make-hash))\n  (define max-x-for-y (make-hash))\n\n  (for ([building buildings])\n\
        \    (define x (vector-ref building 0))\n    (define y (vector-ref building\
        \ 1))\n\n    (hash-update! min-y-for-x x (lambda (v) (min v y)) (add1 n)) ;\
        \ n+1 as initial max value\n    (hash-update! max-y-for-x x (lambda (v) (max\
        \ v y)) 0)        ; 0 as initial min value\n    (hash-update! min-x-for-y y\
        \ (lambda (v) (min v x)) (add1 n))\n    (hash-update! max-x-for-y y (lambda\
        \ (v) (max v x)) 0))\n\n  (define uncovered-count 0)\n  (for ([building buildings])\n\
        \    (define x (vector-ref building 0))\n    (define y (vector-ref building\
        \ 1))\n\n    (when (or (= y (hash-ref min-y-for-x x))\n              (= y (hash-ref\
        \ max-y-for-x x))\n              (= x (hash-ref min-x-for-y y))\n          \
        \    (= x (hash-ref max-x-for-y y)))\n      (set! uncovered-count (add1 uncovered-count))))\n\
        \n  (- (length buildings) uncovered-count))"
      erlang: "-module(solution).\n-export([count_covered_buildings/2]).\n\ncount_covered_buildings(_N,\
        \ Buildings) ->\n    MinYForX = maps:new(),\n    MaxYForX = maps:new(),\n  \
        \  MinXForY = maps:new(),\n    MaxXForY = maps:new(),\n\n    {FinalMinYForX,\
        \ FinalMaxYForX, FinalMinXForY, FinalMaxXForY} =\n        lists:foldl(\n   \
        \         fun([X, Y], {AccMinYForX, AccMaxYForX, AccMinXForY, AccMaxXForY})\
        \ ->\n                NewMinYForX = maps:update_with(X, fun(V) -> min(V, Y)\
        \ end, Y, AccMinYForX),\n                NewMaxYForX = maps:update_with(X, fun(V)\
        \ -> max(V, Y) end, Y, AccMaxYForX),\n                NewMinXForY = maps:update_with(Y,\
        \ fun(V) -> min(V, X) end, X, AccMinXForY),\n                NewMaxXForY = maps:update_with(Y,\
        \ fun(V) -> max(V, X) end, X, AccMaxXForY),\n                {NewMinYForX, NewMaxYForX,\
        \ NewMinXForY, NewMaxXForY}\n            end,\n            {MinYForX, MaxYForX,\
        \ MinXForY, MaxXForY},\n            Buildings\n        ),\n\n    UncoveredCount\
        \ =\n        lists:foldl(\n            fun([X, Y], AccUncovered) ->\n      \
        \          CurrentMinY = maps:get(X, FinalMinYForX),\n                CurrentMaxY\
        \ = maps:get(X, FinalMaxYForX),\n                CurrentMinX = maps:get(Y, FinalMinXForY),\n\
        \                CurrentMaxX = maps:get(Y, FinalMaxXForY),\n\n             \
        \   if\n                    Y == CurrentMinY;\n                    Y == CurrentMaxY;\n\
        \                    X == CurrentMinX;\n                    X == CurrentMaxX\
        \ ->\n                        AccUncovered + 1;\n                    true ->\n\
        \                        AccUncovered\n                end\n            end,\n\
        \            0,\n            Buildings\n        ),\n\n    length(Buildings)\
        \ - UncoveredCount."
      elixir: "defmodule Solution do\n  @spec count_covered_buildings(n :: integer,\
        \ buildings :: [[integer]]) :: integer\n  def count_covered_buildings(n, buildings)\
        \ do\n    {min_y_for_x, max_y_for_x, min_x_for_y, max_x_for_y} =\n      Enum.reduce(buildings,\
        \ {%{}, %{}, %{}, %{}}, fn [x, y], {acc_min_y_x, acc_max_y_x, acc_min_x_y, acc_max_x_y}\
        \ ->\n        new_min_y_x = Map.update(acc_min_y_x, x, y, fn val -> min(val,\
        \ y) end)\n        new_max_y_x = Map.update(acc_max_y_x, x, y, fn val -> max(val,\
        \ y) end)\n        new_min_x_y = Map.update(acc_min_x_y, y, x, fn val -> min(val,\
        \ x) end)\n        new_max_x_y = Map.update(acc_max_x_y, y, x, fn val -> max(val,\
        \ x) end)\n        {new_min_y_x, new_max_y_x, new_min_x_y, new_max_x_y}\n  \
        \    end)\n\n    uncovered_count =\n      Enum.reduce(buildings, 0, fn [x, y],\
        \ acc_uncovered ->\n        current_min_y = Map.fetch!(min_y_for_x, x)\n   \
        \     current_max_y = Map.fetch!(max_y_for_x, x)\n        current_min_x = Map.fetch!(min_x_for_y,\
        \ y)\n        current_max_x = Map.fetch!(max_x_for_y, y)\n\n        if y ==\
        \ current_min_y or\n           y == current_max_y or\n           x == current_min_x\
        \ or\n           x == current_max_x do\n          acc_uncovered + 1\n      \
        \  else\n          acc_uncovered\n        end\n      end)\n\n    length(buildings)\
        \ - uncovered_count\n  end\nend"
    approach: The problem asks us to count buildings that have at least one building
      in all four cardinal directions (left, right, above, below). A building [x, y]
      is covered if there exists [x', y] with x' < x (above), [x'', y] with x'' > x
      (below), [x, y'] with y' < y (left), and [x, y''] with y'' > y (right). Instead
      of directly checking this for each building, which would be inefficient, we can
      identify buildings that are *not* covered and subtract their count from the total
      number of buildings. A building is not covered if it lacks a neighbor in at least
      one of these four directions. This occurs if it is the 'edge' building in its
      row or column.
    time_complexity: The time complexity is O(B) on average, where B is the number of
      buildings. This is because we iterate through the buildings twice. In the first
      pass, we perform constant-time (average) hash map operations (insertions and updates)
      for each of the B buildings. In the second pass, we perform constant-time (average)
      hash map lookups for each of the B buildings. If tree-based maps are used (e.g.,
      std::map in C++), the complexity would be O(B log U) where U is the number of
      unique x or y coordinates, which can be at most B, leading to O(B log B). For
      the C solution, using arrays as direct lookup tables, the complexity is O(B +
      N) due to initialization of N elements.
    space_complexity: The space complexity is O(B) on average. We use four hash maps
      (or arrays in C) to store the minimum and maximum y-coordinates for each x-coordinate,
      and the minimum and maximum x-coordinates for each y-coordinate. In the worst
      case, each unique x or y coordinate could correspond to a distinct entry in these
      maps. Since there are at most B unique x-coordinates and B unique y-coordinates,
      the total space used by these maps is proportional to B. For the C solution, using
      arrays of size N+1, the space complexity is O(N).
    elapsed_time: 93.63370537757874
    model: gemini-2.5-flash
    generated_at: '2025-12-11 01:09:08 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int countCoveredBuildings(int n, vector<vector<int>>&\
        \ buildings) {\n        int count = 0;\n        for (auto& building : buildings)\
        \ {\n            bool covered = true;\n            for (int i = 0; i < 4; i++)\
        \ {\n                bool found = false;\n                for (auto& otherBuilding\
        \ : buildings) {\n                    if (i == 0 && otherBuilding[0] < building[0]\
        \ && otherBuilding[1] == building[1]) found = true;\n                    if\
        \ (i == 1 && otherBuilding[0] > building[0] && otherBuilding[1] == building[1])\
        \ found = true;\n                    if (i == 2 && otherBuilding[0] == building[0]\
        \ && otherBuilding[1] < building[1]) found = true;\n                    if (i\
        \ == 3 && otherBuilding[0] == building[0] && otherBuilding[1] > building[1])\
        \ found = true;\n                }\n                if (!found) covered = false;\n\
        \            }\n            if (covered) count++;\n        }\n        return\
        \ count;\n    }\n};"
      java: "class Solution {\n    public int countCoveredBuildings(int n, int[][] buildings)\
        \ {\n        int count = 0;\n        for (int[] building : buildings) {\n  \
        \          boolean covered = true;\n            for (int i = 0; i < 4; i++)\
        \ {\n                boolean found = false;\n                for (int[] otherBuilding\
        \ : buildings) {\n                    if (i == 0 && otherBuilding[0] < building[0]\
        \ && otherBuilding[1] == building[1]) found = true;\n                    if\
        \ (i == 1 && otherBuilding[0] > building[0] && otherBuilding[1] == building[1])\
        \ found = true;\n                    if (i == 2 && otherBuilding[0] == building[0]\
        \ && otherBuilding[1] < building[1]) found = true;\n                    if (i\
        \ == 3 && otherBuilding[0] == building[0] && otherBuilding[1] > building[1])\
        \ found = true;\n                }\n                if (!found) covered = false;\n\
        \            }\n            if (covered) count++;\n        }\n        return\
        \ count;\n    }\n}"
      python: "class Solution:\n    def countCoveredBuildings(self, n: int, buildings:\
        \ List[List[int]]) -> int:\n        count = 0\n        for building in buildings:\n\
        \            covered = True\n            for i in range(4):\n              \
        \  found = False\n                for otherBuilding in buildings:\n        \
        \            if i == 0 and otherBuilding[0] < building[0] and otherBuilding[1]\
        \ == building[1]: found = True\n                    if i == 1 and otherBuilding[0]\
        \ > building[0] and otherBuilding[1] == building[1]: found = True\n        \
        \            if i == 2 and otherBuilding[0] == building[0] and otherBuilding[1]\
        \ < building[1]: found = True\n                    if i == 3 and otherBuilding[0]\
        \ == building[0] and otherBuilding[1] > building[1]: found = True\n        \
        \        if not found: covered = False\n            if covered: count += 1\n\
        \        return count"
      python3: "class Solution:\n    def countCoveredBuildings(self, n: int, buildings:\
        \ List[List[int]]) -> int:\n        count = 0\n        for building in buildings:\n\
        \            covered = True\n            for i in range(4):\n              \
        \  found = False\n                for otherBuilding in buildings:\n        \
        \            if i == 0 and otherBuilding[0] < building[0] and otherBuilding[1]\
        \ == building[1]: found = True\n                    if i == 1 and otherBuilding[0]\
        \ > building[0] and otherBuilding[1] == building[1]: found = True\n        \
        \            if i == 2 and otherBuilding[0] == building[0] and otherBuilding[1]\
        \ < building[1]: found = True\n                    if i == 3 and otherBuilding[0]\
        \ == building[0] and otherBuilding[1] > building[1]: found = True\n        \
        \        if not found: covered = False\n            if covered: count += 1\n\
        \        return count"
      c: "typedef struct {\n    int x;\n    int y;\n} Building;\n\nint compareBuildings(const\
        \ void *a, const void *b) {\n    Building *buildingA = (Building *)a;\n    Building\
        \ *buildingB = (Building *)b;\n    if (buildingA->x < buildingB->x) return -1;\n\
        \    if (buildingA->x > buildingB->x) return 1;\n    if (buildingA->y < buildingB->y)\
        \ return -1;\n    if (buildingA->y > buildingB->y) return 1;\n    return 0;\n\
        }\n\nint countCoveredBuildings(int n, int **buildings, int buildingsSize) {\n\
        \    int count = 0;\n    for (int i = 0; i < buildingsSize; i++) {\n       \
        \ bool covered = true;\n        for (int j = 0; j < 4; j++) {\n            bool\
        \ found = false;\n            for (int k = 0; k < buildingsSize; k++) {\n  \
        \              if (j == 0 && buildings[k][0] < buildings[i][0] && buildings[k][1]\
        \ == buildings[i][1]) found = true;\n                if (j == 1 && buildings[k][0]\
        \ > buildings[i][0] && buildings[k][1] == buildings[i][1]) found = true;\n \
        \               if (j == 2 && buildings[k][0] == buildings[i][0] && buildings[k][1]\
        \ < buildings[i][1]) found = true;\n                if (j == 3 && buildings[k][0]\
        \ == buildings[i][0] && buildings[k][1] > buildings[i][1]) found = true;\n \
        \           }\n            if (!found) covered = false;\n        }\n       \
        \ if (covered) count++;\n    }\n    return count;\n}"
      csharp: "public class Solution {\n    public int CountCoveredBuildings(int n,\
        \ int[][] buildings) {\n        int count = 0;\n        for (int i = 0; i <\
        \ buildings.Length; i++) {\n            bool covered = true;\n            for\
        \ (int j = 0; j < 4; j++) {\n                bool found = false;\n         \
        \       for (int k = 0; k < buildings.Length; k++) {\n                    if\
        \ (j == 0 && buildings[k][0] < buildings[i][0] && buildings[k][1] == buildings[i][1])\
        \ found = true;\n                    if (j == 1 && buildings[k][0] > buildings[i][0]\
        \ && buildings[k][1] == buildings[i][1]) found = true;\n                   \
        \ if (j == 2 && buildings[k][0] == buildings[i][0] && buildings[k][1] < buildings[i][1])\
        \ found = true;\n                    if (j == 3 && buildings[k][0] == buildings[i][0]\
        \ && buildings[k][1] > buildings[i][1]) found = true;\n                }\n \
        \               if (!found) covered = false;\n            }\n            if\
        \ (covered) count++;\n        }\n        return count;\n    }\n}"
      javascript: "var countCoveredBuildings = function(n, buildings) {\n    let count\
        \ = 0;\n    for (let i = 0; i < buildings.length; i++) {\n        let covered\
        \ = true;\n        for (let j = 0; j < 4; j++) {\n            let found = false;\n\
        \            for (let k = 0; k < buildings.length; k++) {\n                if\
        \ (j == 0 && buildings[k][0] < buildings[i][0] && buildings[k][1] == buildings[i][1])\
        \ found = true;\n                if (j == 1 && buildings[k][0] > buildings[i][0]\
        \ && buildings[k][1] == buildings[i][1]) found = true;\n                if (j\
        \ == 2 && buildings[k][0] == buildings[i][0] && buildings[k][1] < buildings[i][1])\
        \ found = true;\n                if (j == 3 && buildings[k][0] == buildings[i][0]\
        \ && buildings[k][1] > buildings[i][1]) found = true;\n            }\n     \
        \       if (!found) covered = false;\n        }\n        if (covered) count++;\n\
        \    }\n    return count;\n};"
      typescript: "function countCoveredBuildings(n: number, buildings: number[][]):\
        \ number {\n    let count: number = 0;\n    for (let i: number = 0; i < buildings.length;\
        \ i++) {\n        let covered: boolean = true;\n        for (let j: number =\
        \ 0; j < 4; j++) {\n            let found: boolean = false;\n            for\
        \ (let k: number = 0; k < buildings.length; k++) {\n                if (j ==\
        \ 0 && buildings[k][0] < buildings[i][0] && buildings[k][1] == buildings[i][1])\
        \ found = true;\n                if (j == 1 && buildings[k][0] > buildings[i][0]\
        \ && buildings[k][1] == buildings[i][1]) found = true;\n                if (j\
        \ == 2 && buildings[k][0] == buildings[i][0] && buildings[k][1] < buildings[i][1])\
        \ found = true;\n                if (j == 3 && buildings[k][0] == buildings[i][0]\
        \ && buildings[k][1] > buildings[i][1]) found = true;\n            }\n     \
        \       if (!found) covered = false;\n        }\n        if (covered) count++;\n\
        \    }\n    return count;\n}"
      php: "class Solution {\n    function countCoveredBuildings($n, $buildings) {\n\
        \        $count = 0;\n        for ($i = 0; $i < count($buildings); $i++) {\n\
        \            $covered = true;\n            for ($j = 0; $j < 4; $j++) {\n  \
        \              $found = false;\n                for ($k = 0; $k < count($buildings);\
        \ $k++) {\n                    if ($j == 0 && $buildings[$k][0] < $buildings[$i][0]\
        \ && $buildings[$k][1] == $buildings[$i][1]) $found = true;\n              \
        \      if ($j == 1 && $buildings[$k][0] > $buildings[$i][0] && $buildings[$k][1]\
        \ == $buildings[$i][1]) $found = true;\n                    if ($j == 2 && $buildings[$k][0]\
        \ == $buildings[$i][0] && $buildings[$k][1] < $buildings[$i][1]) $found = true;\n\
        \                    if ($j == 3 && $buildings[$k][0] == $buildings[$i][0] &&\
        \ $buildings[$k][1] > $buildings[$i][1]) $found = true;\n                }\n\
        \                if (!$found) $covered = false;\n            }\n           \
        \ if ($covered) $count++;\n        }\n        return $count;\n    }\n}"
      swift: "class Solution {\n    func countCoveredBuildings(_ n: Int, _ buildings:\
        \ [[Int]]) -> Int {\n        var count: Int = 0\n        for i in 0..<buildings.count\
        \ {\n            var covered: Bool = true\n            for j in 0..<4 {\n  \
        \              var found: Bool = false\n                for k in 0..<buildings.count\
        \ {\n                    if j == 0 && buildings[k][0] < buildings[i][0] && buildings[k][1]\
        \ == buildings[i][1] { found = true }\n                    if j == 1 && buildings[k][0]\
        \ > buildings[i][0] && buildings[k][1] == buildings[i][1] { found = true }\n\
        \                    if j == 2 && buildings[k][0] == buildings[i][0] && buildings[k][1]\
        \ < buildings[i][1] { found = true }\n                    if j == 3 && buildings[k][0]\
        \ == buildings[i][0] && buildings[k][1] > buildings[i][1] { found = true }\n\
        \                }\n                if !found { covered = false }\n        \
        \    }\n            if covered { count += 1 }\n        }\n        return count\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun countCoveredBuildings(n: Int, buildings: Array<IntArray>):\
        \ Int {\n        var count: Int = 0\n        for (i in buildings.indices) {\n\
        \            var covered: Boolean = true\n            for (j in 0 until 4) {\n\
        \                var found: Boolean = false\n                for (k in buildings.indices)\
        \ {\n                    if (j == 0 && buildings[k][0] < buildings[i][0] &&\
        \ buildings[k][1] == buildings[i][1]) found = true\n                    if (j\
        \ == 1 && buildings[k][0] > buildings[i][0] && buildings[k][1] == buildings[i][1])\
        \ found = true\n                    if (j == 2 && buildings[k][0] == buildings[i][0]\
        \ && buildings[k][1] < buildings[i][1]) found = true\n                    if\
        \ (j == 3 && buildings[k][0] == buildings[i][0] && buildings[k][1] > buildings[i][1])\
        \ found = true\n                }\n                if (!found) covered = false\n\
        \            }\n            if (covered) count++\n        }\n        return\
        \ count\n    }\n}"
      dart: "class Solution {\n    int countCoveredBuildings(int n, List<List<int>>\
        \ buildings) {\n        int count = 0;\n        for (int i = 0; i < buildings.length;\
        \ i++) {\n            bool covered = true;\n            for (int j = 0; j <\
        \ 4; j++) {\n                bool found = false;\n                for (int k\
        \ = 0; k < buildings.length; k++) {\n                    if (j == 0 && buildings[k][0]\
        \ < buildings[i][0] && buildings[k][1] == buildings[i][1]) found = true;\n \
        \                   if (j == 1 && buildings[k][0] > buildings[i][0] && buildings[k][1]\
        \ == buildings[i][1]) found = true;\n                    if (j == 2 && buildings[k][0]\
        \ == buildings[i][0] && buildings[k][1] < buildings[i][1]) found = true;\n \
        \                   if (j == 3 && buildings[k][0] == buildings[i][0] && buildings[k][1]\
        \ > buildings[i][1]) found = true;\n                }\n                if (!found)\
        \ covered = false;\n            }\n            if (covered) count++;\n     \
        \   }\n        return count;\n    }\n}"
      go: "package main\n\nimport (\n    \"fmt\"\n)\n\ntype Solution struct{}\n\nfunc\
        \ (s *Solution) countCoveredBuildings(n int, buildings [][]int) int {\n    count\
        \ := 0\n    for i := 0; i < len(buildings); i++ {\n        covered := true\n\
        \        for j := 0; j < 4; j++ {\n            found := false\n            for\
        \ k := 0; k < len(buildings); k++ {\n                if j == 0 && buildings[k][0]\
        \ < buildings[i][0] && buildings[k][1] == buildings[i][1] {\n              \
        \      found = true\n                }\n                if j == 1 && buildings[k][0]\
        \ > buildings[i][0] && buildings[k][1] == buildings[i][1] {\n              \
        \      found = true\n                }\n                if j == 2 && buildings[k][0]\
        \ == buildings[i][0] && buildings[k][1] < buildings[i][1] {\n              \
        \      found = true\n                }\n                if j == 3 && buildings[k][0]\
        \ == buildings[i][0] && buildings[k][1] > buildings[i][1] {\n              \
        \      found = true\n                }\n            }\n            if !found\
        \ {\n                covered = false\n            }\n        }\n        if covered\
        \ {\n            count++\n        }\n    }\n    return count\n}"
      ruby: "class Solution\n    def count_covered_buildings(n, buildings)\n       \
        \ count = 0\n        buildings.each_with_index do |building, i|\n          \
        \  covered = true\n            4.times do |j|\n                found = false\n\
        \                buildings.each_with_index do |other_building, k|\n        \
        \            if j == 0 && other_building[0] < building[0] && other_building[1]\
        \ == building[1]\n                        found = true\n                   \
        \ elsif j == 1 && other_building[0] > building[0] && other_building[1] == building[1]\n\
        \                        found = true\n                    elsif j == 2 && other_building[0]\
        \ == building[0] && other_building[1] < building[1]\n                      \
        \  found = true\n                    elsif j == 3 && other_building[0] == building[0]\
        \ && other_building[1] > building[1]\n                        found = true\n\
        \                    end\n                end\n                if !found\n \
        \                   covered = false\n                end\n            end\n\
        \            if covered\n                count += 1\n            end\n     \
        \   end\n        count\n    end\nend"
      scala: "object Solution {\n    def countCoveredBuildings(n: Int, buildings: Array[Array[Int]]):\
        \ Int = {\n        var count: Int = 0\n        for (i <- buildings.indices)\
        \ {\n            var covered: Boolean = true\n            for (j <- 0 until\
        \ 4) {\n                var found: Boolean = false\n                for (k <-\
        \ buildings.indices) {\n                    if (j == 0 && buildings(k)(0) <\
        \ buildings(i)(0) && buildings(k)(1) == buildings(i)(1)) found = true\n    \
        \                if (j == 1 && buildings(k)(0) > buildings(i)(0) && buildings(k)(1)\
        \ == buildings(i)(1)) found = true\n                    if (j == 2 && buildings(k)(0)\
        \ == buildings(i)(0) && buildings(k)(1) < buildings(i)(1)) found = true\n  \
        \                  if (j == 3 && buildings(k)(0) == buildings(i)(0) && buildings(k)(1)\
        \ > buildings(i)(1)) found = true\n                }\n                if (!found)\
        \ covered = false\n            }\n            if (covered) count += 1\n    \
        \    }\n        count\n    }\n}"
      rust: "struct Solution;\n\nimpl Solution {\n    pub fn count_covered_buildings(n:\
        \ i32, buildings: Vec<Vec<i32>>) -> i32 {\n        let mut count: i32 = 0;\n\
        \        for i in 0..buildings.len() {\n            let mut covered: bool =\
        \ true;\n            for j in 0..4 {\n                let mut found: bool =\
        \ false;\n                for k in 0..buildings.len() {\n                  \
        \  if j == 0 && buildings[k][0] < buildings[i][0] && buildings[k][1] == buildings[i][1]\
        \ {\n                        found = true;\n                    }\n        \
        \            if j == 1 && buildings[k][0] > buildings[i][0] && buildings[k][1]\
        \ == buildings[i][1] {\n                        found = true;\n            \
        \        }\n                    if j == 2 && buildings[k][0] == buildings[i][0]\
        \ && buildings[k][1] < buildings[i][1] {\n                        found = true;\n\
        \                    }\n                    if j == 3 && buildings[k][0] ==\
        \ buildings[i][0] && buildings[k][1] > buildings[i][1] {\n                 \
        \       found = true;\n                    }\n                }\n          \
        \      if !found {\n                    covered = false;\n                }\n\
        \            }\n            if covered {\n                count += 1;\n    \
        \        }\n        }\n        count\n    }\n}"
      racket: "define (count-covered-buildings n buildings)\n    (let loop ((i 0) (count\
        \ 0))\n        (if (>= i (length buildings))\n            count\n          \
        \  (let ((building (list-ref buildings i))\n                  (covered #t))\n\
        \                (for-each (lambda (j)\n                            (let ((found\
        \ #f))\n                                (for-each (lambda (k)\n            \
        \                                (when (or (and (= j 0) (< (car k) (car building))\
        \ (= (cadr k) (cadr building)))\n                                          \
        \            (and (= j 1) (> (car k) (car building)) (= (cadr k) (cadr building)))\n\
        \                                                      (and (= j 2) (= (car\
        \ k) (car building)) (< (cadr k) (cadr building)))\n                       \
        \                               (and (= j 3) (= (car k) (car building)) (> (cadr\
        \ k) (cadr building))))\n                                            (set! found\
        \ #t))\n                                          buildings)\n             \
        \                   (when (not found)\n                                    (set!\
        \ covered #f))\n                            )\n                          '(0\
        \ 1 2 3))\n                (loop (+ i 1) (if covered (+ count 1) count))))))"
      erlang: "count_covered_buildings(N, Buildings) ->\n    count_covered_buildings(N,\
        \ Buildings, 0).\n\ncount_covered_buildings(N, [], Count) -> Count;\n\ncount_covered_buildings(N,\
        \ [Building | Buildings], Count) ->\n    case is_covered(Building, Buildings)\
        \ of\n        true -> count_covered_buildings(N, Buildings, Count + 1);\n  \
        \      false -> count_covered_buildings(N, Buildings, Count)\n    end.\n\nis_covered(Building,\
        \ Buildings) ->\n    is_covered(Building, Buildings, [0, 1, 2, 3], true).\n\n\
        is_covered(_Building, _Buildings, [], Covered) -> Covered;\n\nis_covered(Building,\
        \ Buildings, [Direction | Directions], Covered) ->\n    case has_neighbor(Building,\
        \ Direction, Buildings) of\n        true -> is_covered(Building, Buildings,\
        \ Directions, Covered);\n        false -> is_covered(Building, Buildings, Directions,\
        \ false)\n    end.\n\nhas_neighbor(Building, 0, Buildings) -> has_neighbor(Building,\
        \ 0, Buildings, false);\n\nhas_neighbor(Building, 1, Buildings) -> has_neighbor(Building,\
        \ 1, Buildings, false);\n\nhas_neighbor(Building, 2, Buildings) -> has_neighbor(Building,\
        \ 2, Buildings, false);\n\nhas_neighbor(Building, 3, Buildings) -> has_neighbor(Building,\
        \ 3, Buildings, false).\n\nhas_neighbor(_Building, _Direction, [], Found) ->\
        \ Found;\n\nhas_neighbor(Building, 0, [OtherBuilding | Buildings], Found) ->\n\
        \    if\n        OtherBuilding =:= [X, Y],\n        X < element(1, Building),\n\
        \        Y =:= element(2, Building)\n    ->\n        has_neighbor(Building,\
        \ 0, Buildings, true);\n    true -> has_neighbor(Building, 0, Buildings, Found).\n\
        \nhas_neighbor(Building, 1, [OtherBuilding | Buildings], Found) ->\n    if\n\
        \        OtherBuilding =:= [X, Y],\n        X > element(1, Building),\n    \
        \    Y =:= element(2, Building)\n    ->\n        has_neighbor(Building, 1, Buildings,\
        \ true);\n    true -> has_neighbor(Building, 1, Buildings, Found).\n\nhas_neighbor(Building,\
        \ 2, [OtherBuilding | Buildings], Found) ->\n    if\n        OtherBuilding =:=\
        \ [X, Y],\n        X =:= element(1, Building),\n        Y < element(2, Building)\n\
        \    ->\n        has_neighbor(Building, 2, Buildings, true);\n    true -> has_neighbor(Building,\
        \ 2, Buildings, Found).\n\nhas_neighbor(Building, 3, [OtherBuilding | Buildings],\
        \ Found) ->\n    if\n        OtherBuilding =:= [X, Y],\n        X =:= element(1,\
        \ Building),\n        Y > element(2, Building)\n    ->\n        has_neighbor(Building,\
        \ 3, Buildings, true);\n    true -> has_neighbor(Building, 3, Buildings, Found)."
      elixir: "defmodule Solution do\n    def count_covered_buildings(n, buildings)\
        \ do\n        count_covered_buildings(n, buildings, 0)\n    end\n\n    defp\
        \ count_covered_buildings(_n, [], count) do\n        count\n    end\n\n    defp\
        \ count_covered_buildings(n, [building | buildings], count) do\n        if is_covered?(building,\
        \ buildings) do\n            count_covered_buildings(n, buildings, count + 1)\n\
        \        else\n            count_covered_buildings(n, buildings, count)\n  \
        \      end\n    end\n\n    defp is_covered?(building, buildings) do\n      \
        \  is_covered?(building, buildings, [0, 1, 2, 3], true)\n    end\n\n    defp\
        \ is_covered?(_building, _buildings, [], covered) do\n        covered\n    end\n\
        \n    defp is_covered?(building, buildings, [direction | directions], covered)\
        \ do\n        if has_neighbor?(building, direction, buildings) do\n        \
        \    is_covered?(building, buildings, directions, covered)\n        else\n \
        \           is_covered?(building, buildings, directions, false)\n        end\n\
        \    end\n\n    defp has_neighbor?(_building, _direction, []) do\n        false\n\
        \    end\n\n    defp has_neighbor?(building, 0, [other_building | buildings])\
        \ do\n        if other_building == [x, y] and x < elem(building, 0) and y ==\
        \ elem(building, 1) do\n            true\n        else\n            has_neighbor?(building,\
        \ 0, buildings)\n        end\n    end\n\n    defp has_neighbor?(building, 1,\
        \ [other_building | buildings]) do\n        if other_building == [x, y] and\
        \ x > elem(building, 0) and y == elem(building, 1) do\n            true\n  \
        \      else\n            has_neighbor?(building, 1, buildings)\n        end\n\
        \    end\n\n    defp has_neighbor?(building, 2, [other_building | buildings])\
        \ do\n        if other_building == [x, y] and x == elem(building, 0) and y <\
        \ elem(building, 1) do\n            true\n        else\n            has_neighbor?(building,\
        \ 2, buildings)\n        end\n    end\n\n    defp has_neighbor?(building, 3,\
        \ [other_building | buildings]) do\n        if other_building == [x, y] and\
        \ x == elem(building, 0) and y > elem(building, 1) do\n            true\n  \
        \      else\n            has_neighbor?(building, 3, buildings)\n        end\n\
        \    end\nend"
    approach: The problem can be solved by iterating over each building and checking
      if it has at least one building in all four directions. We can use a set to store
      the x and y coordinates of the buildings to efficiently check for the existence
      of buildings in each direction. The key intuition is to understand that a building
      is covered if it has at least one building above, below, to the left, and to the
      right of it. We can use a simple loop to iterate over each building and check
      for the existence of buildings in each direction.
    time_complexity: The time complexity of the solution is O(n^2) where n is the number
      of buildings. This is because we are iterating over each building and checking
      for the existence of buildings in each direction. The space complexity is O(n)
      as we are storing the x and y coordinates of the buildings in a set.
    space_complexity: The space complexity of the solution is O(n) where n is the number
      of buildings. This is because we are storing the x and y coordinates of the buildings
      in a set.
    elapsed_time: 12.646758079528809
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-11 01:09:21 '
---

## Problem #3531: Count Covered Buildings

**Difficulty:** Medium

**Topics:** Array, Hash Table, Sorting

## Problem Description

<p>You are given a positive integer <code>n</code>, representing an <code>n x n</code> city. You are also given a 2D grid <code>buildings</code>, where <code>buildings[i] = [x, y]</code> denotes a <strong>unique</strong> building located at coordinates <code>[x, y]</code>.</p>

<p>A building is <strong>covered</strong> if there is at least one building in all <strong>four</strong> directions: left, right, above, and below.</p>

<p>Return the number of <strong>covered</strong> buildings.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2025/03/04/telegram-cloud-photo-size-5-6212982906394101085-m.jpg" style="width: 200px; height: 204px;" /></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Only building <code>[2,2]</code> is covered as it has at least one building:

	<ul>
		<li>above (<code>[1,2]</code>)</li>
		<li>below (<code>[3,2]</code>)</li>
		<li>left (<code>[2,1]</code>)</li>
		<li>right (<code>[2,3]</code>)</li>
	</ul>
	</li>
	<li>Thus, the count of covered buildings is 1.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2025/03/04/telegram-cloud-photo-size-5-6212982906394101086-m.jpg" style="width: 200px; height: 204px;" /></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, buildings = [[1,1],[1,2],[2,1],[2,2]]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>No building has at least one building in all four directions.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2025/03/16/telegram-cloud-photo-size-5-6248862251436067566-x.jpg" style="width: 202px; height: 205px;" /></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 5, buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Only building <code>[3,3]</code> is covered as it has at least one building:

	<ul>
		<li>above (<code>[1,3]</code>)</li>
		<li>below (<code>[5,3]</code>)</li>
		<li>left (<code>[3,2]</code>)</li>
		<li>right (<code>[3,5]</code>)</li>
	</ul>
	</li>
	<li>Thus, the count of covered buildings is 1.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= buildings.length &lt;= 10<sup>5</sup> </code></li>
	<li><code>buildings[i] = [x, y]</code></li>
	<li><code>1 &lt;= x, y &lt;= n</code></li>
	<li>All coordinates of <code>buildings</code> are <strong>unique</strong>.</li>
</ul>


## Hints

1. Group buildings with the same x or y value together, and sort each group.

2. In each sorted list, the buildings that are not at the first or last positions are covered in that direction.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-11 01:09:08 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to count buildings that have at least one building in all four cardinal directions (left, right, above, below). A building [x, y] is covered if there exists [x', y] with x' < x (above), [x'', y] with x'' > x (below), [x, y'] with y' < y (left), and [x, y''] with y'' > y (right). Instead of directly checking this for each building, which would be inefficient, we can identify buildings that are *not* covered and subtract their count from the total number of buildings. A building is not covered if it lacks a neighbor in at least one of these four directions. This occurs if it is the 'edge' building in its row or column.

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
#include <vector>
#include <unordered_map>
#include <algorithm> // For std::min and std::max
#include <limits>    // For std::numeric_limits

class Solution {
public:
    int countCoveredBuildings(int n, std::vector<std::vector<int>>& buildings) {
        std::unordered_map<int, int> min_y_for_x;
        std::unordered_map<int, int> max_y_for_x;
        std::unordered_map<int, int> min_x_for_y;
        std::unordered_map<int, int> max_x_for_y;

        for (const auto& building : buildings) {
            int x = building[0];
            int y = building[1];

            if (min_y_for_x.find(x) == min_y_for_x.end()) {
                min_y_for_x[x] = std::numeric_limits<int>::max();
            }
            min_y_for_x[x] = std::min(min_y_for_x[x], y);

            if (max_y_for_x.find(x) == max_y_for_x.end()) {
                max_y_for_x[x] = std::numeric_limits<int>::min();
            }
            max_y_for_x[x] = std::max(max_y_for_x[x], y);

            if (min_x_for_y.find(y) == min_x_for_y.end()) {
                min_x_for_y[y] = std::numeric_limits<int>::max();
            }
            min_x_for_y[y] = std::min(min_x_for_y[y], x);

            if (max_x_for_y.find(y) == max_x_for_y.end()) {
                max_x_for_y[y] = std::numeric_limits<int>::min();
            }
            max_x_for_y[y] = std::max(max_x_for_y[y], x);
        }

        int uncovered_count = 0;
        for (const auto& building : buildings) {
            int x = building[0];
            int y = building[1];

            if (y == min_y_for_x[x] ||
                y == max_y_for_x[x] ||
                x == min_x_for_y[y] ||
                x == max_x_for_y[y]) {
                uncovered_count++;
            }
        }

        return buildings.size() - uncovered_count;
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

class Solution {
    public int countCoveredBuildings(int n, int[][] buildings) {
        HashMap<Integer, Integer> minYForX = new HashMap<>();
        HashMap<Integer, Integer> maxYForX = new HashMap<>();
        HashMap<Integer, Integer> minXForY = new HashMap<>();
        HashMap<Integer, Integer> maxXForY = new HashMap<>();

        for (int[] building : buildings) {
            int x = building[0];
            int y = building[1];

            minYForX.put(x, Math.min(minYForX.getOrDefault(x, Integer.MAX_VALUE), y));
            maxYForX.put(x, Math.max(maxYForX.getOrDefault(x, Integer.MIN_VALUE), y));
            minXForY.put(y, Math.min(minXForY.getOrDefault(y, Integer.MAX_VALUE), x));
            maxXForY.put(y, Math.max(maxXForY.getOrDefault(y, Integer.MIN_VALUE), x));
        }

        int uncoveredCount = 0;
        for (int[] building : buildings) {
            int x = building[0];
            int y = building[1];

            if (y == minYForX.get(x) ||
                y == maxYForX.get(x) ||
                x == minXForY.get(y) ||
                x == maxXForY.get(y)) {
                uncoveredCount++;
            }
        }

        return buildings.length - uncoveredCount;
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
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        min_y_for_x = collections.defaultdict(lambda: float('inf'))
        max_y_for_x = collections.defaultdict(lambda: float('-inf'))
        min_x_for_y = collections.defaultdict(lambda: float('inf'))
        max_x_for_y = collections.defaultdict(lambda: float('-inf'))

        for x, y in buildings:
            min_y_for_x[x] = min(min_y_for_x[x], y)
            max_y_for_x[x] = max(max_y_for_x[x], y)
            min_x_for_y[y] = min(min_x_for_y[y], x)
            max_x_for_y[y] = max(max_x_for_y[y], x)

        uncovered_count = 0
        for x, y in buildings:
            if y == min_y_for_x[x] or \
               y == max_y_for_x[x] or \
               x == min_x_for_y[y] or \
               x == max_x_for_y[y]:
                uncovered_count += 1

        return len(buildings) - uncovered_count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import collections

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        min_y_for_x = collections.defaultdict(lambda: float('inf'))
        max_y_for_x = collections.defaultdict(lambda: float('-inf'))
        min_x_for_y = collections.defaultdict(lambda: float('inf'))
        max_x_for_y = collections.defaultdict(lambda: float('-inf'))

        for x, y in buildings:
            min_y_for_x[x] = min(min_y_for_x[x], y)
            max_y_for_x[x] = max(max_y_for_x[x], y)
            min_x_for_y[y] = min(min_x_for_y[y], x)
            max_x_for_y[y] = max(max_x_for_y[y], x)

        uncovered_count = 0
        for x, y in buildings:
            if y == min_y_for_x[x] or \
               y == max_y_for_x[x] or \
               x == min_x_for_y[y] or \
               x == max_x_for_y[y]:
                uncovered_count += 1

        return len(buildings) - uncovered_count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h> // For malloc, free
#include <limits.h> // For INT_MAX, INT_MIN
#include <string.h> // For memset

// Helper functions for min/max
int min(int a, int b) {
    return a < b ? a : b;
}

int max(int a, int b) {
    return a > b ? a : b;
}

int countCoveredBuildings(int n, int** buildings, int buildingsSize, int* buildingsColSize) {
    // Using arrays as hash maps, since coordinates are within [1, n]
    // Max index will be n, so size n+1
    int* min_y_for_x = (int*)malloc((n + 1) * sizeof(int));
    int* max_y_for_x = (int*)malloc((n + 1) * sizeof(int));
    int* min_x_for_y = (int*)malloc((n + 1) * sizeof(int));
    int* max_x_for_y = (int*)malloc((n + 1) * sizeof(int));

    // Initialize with extreme values
    for (int i = 0; i <= n; ++i) {
        min_y_for_x[i] = INT_MAX;
        max_y_for_x[i] = INT_MIN;
        min_x_for_y[i] = INT_MAX;
        max_x_for_y[i] = INT_MIN;
    }

    for (int i = 0; i < buildingsSize; ++i) {
        int x = buildings[i][0];
        int y = buildings[i][1];

        min_y_for_x[x] = min(min_y_for_x[x], y);
        max_y_for_x[x] = max(max_y_for_x[x], y);
        min_x_for_y[y] = min(min_x_for_y[y], x);
        max_x_for_y[y] = max(max_x_for_y[y], x);
    }

    int uncovered_count = 0;
    for (int i = 0; i < buildingsSize; ++i) {
        int x = buildings[i][0];
        int y = buildings[i][1];

        if (y == min_y_for_x[x] ||
            y == max_y_for_x[x] ||
            x == min_x_for_y[y] ||
            x == max_x_for_y[y]) {
            uncovered_count++;
        }
    }

    // Free allocated memory
    free(min_y_for_x);
    free(max_y_for_x);
    free(min_x_for_y);
    free(max_x_for_y);

    return buildingsSize - uncovered_count;
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
    public int CountCoveredBuildings(int n, int[][] buildings) {
        Dictionary<int, int> minYForX = new Dictionary<int, int>();
        Dictionary<int, int> maxYForX = new Dictionary<int, int>();
        Dictionary<int, int> minXForY = new Dictionary<int, int>();
        Dictionary<int, int> maxXForY = new Dictionary<int, int>();

        foreach (var building in buildings) {
            int x = building[0];
            int y = building[1];

            if (!minYForX.ContainsKey(x)) {
                minYForX[x] = int.MaxValue;
                maxYForX[x] = int.MinValue;
            }
            minYForX[x] = Math.Min(minYForX[x], y);
            maxYForX[x] = Math.Max(maxYForX[x], y);

            if (!minXForY.ContainsKey(y)) {
                minXForY[y] = int.MaxValue;
                maxXForY[y] = int.MinValue;
            }
            minXForY[y] = Math.Min(minXForY[y], x);
            maxXForY[y] = Math.Max(maxXForY[y], x);
        }

        int uncoveredCount = 0;
        foreach (var building in buildings) {
            int x = building[0];
            int y = building[1];

            if (y == minYForX[x] ||
                y == maxYForX[x] ||
                x == minXForY[y] ||
                x == maxXForY[y]) {
                uncoveredCount++;
            }
        }

        return buildings.Length - uncoveredCount;
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
 * @param {number[][]} buildings
 * @return {number}
 */
var countCoveredBuildings = function(n, buildings) {
    const minYForX = new Map();
    const maxYForX = new Map();
    const minXForY = new Map();
    const maxXForY = new Map();

    for (const [x, y] of buildings) {
        minYForX.set(x, Math.min(minYForX.get(x) ?? Infinity, y));
        maxYForX.set(x, Math.max(maxYForX.get(x) ?? -Infinity, y));
        minXForY.set(y, Math.min(minXForY.get(y) ?? Infinity, x));
        maxXForY.set(y, Math.max(maxXForY.get(y) ?? -Infinity, x));
    }

    let uncoveredCount = 0;
    for (const [x, y] of buildings) {
        if (y === minYForX.get(x) ||
            y === maxYForX.get(x) ||
            x === minXForY.get(y) ||
            x === maxXForY.get(y)) {
            uncoveredCount++;
        }
    }

    return buildings.length - uncoveredCount;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countCoveredBuildings(n: number, buildings: number[][]): number {
    const minYForX = new Map<number, number>();
    const maxYForX = new Map<number, number>();
    const minXForY = new Map<number, number>();
    const maxXForY = new Map<number, number>();

    for (const [x, y] of buildings) {
        minYForX.set(x, Math.min(minYForX.get(x) ?? Infinity, y));
        maxYForX.set(x, Math.max(maxYForX.get(x) ?? -Infinity, y));
        minXForY.set(y, Math.min(minXForY.get(y) ?? Infinity, x));
        maxXForY.set(y, Math.max(maxXForY.get(y) ?? -Infinity, x));
    }

    let uncoveredCount = 0;
    for (const [x, y] of buildings) {
        if (y === minYForX.get(x)! ||
            y === maxYForX.get(x)! ||
            x === minXForY.get(y)! ||
            x === maxXForY.get(y)!) {
            uncoveredCount++;
        }
    }

    return buildings.length - uncoveredCount;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $buildings
     * @return Integer
     */
    function countCoveredBuildings($n, $buildings) {
        $minYForX = [];
        $maxYForX = [];
        $minXForY = [];
        $maxXForY = [];

        foreach ($buildings as $building) {
            list($x, $y) = $building;

            $minYForX[$x] = min($minYForX[$x] ?? PHP_INT_MAX, $y);
            $maxYForX[$x] = max($maxYForX[$x] ?? PHP_INT_MIN, $y);
            $minXForY[$y] = min($minXForY[$y] ?? PHP_INT_MAX, $x);
            $maxXForY[$y] = max($maxXForY[$y] ?? PHP_INT_MIN, $x);
        }

        $uncoveredCount = 0;
        foreach ($buildings as $building) {
            list($x, $y) = $building;

            if ($y == $minYForX[$x] ||
                $y == $maxYForX[$x] ||
                $x == $minXForY[$y] ||
                $x == $maxXForY[$y]) {
                $uncoveredCount++;
            }
        }

        return count($buildings) - $uncoveredCount;
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
    func countCoveredBuildings(_ n: Int, _ buildings: [[Int]]) -> Int {
        var minYForX: [Int: Int] = [:]
        var maxYForX: [Int: Int] = [:]
        var minXForY: [Int: Int] = [:]
        var maxXForY: [Int: Int] = [:]

        for building in buildings {
            let x = building[0]
            let y = building[1]

            minYForX[x] = min(minYForX[x] ?? Int.max, y)
            maxYForX[x] = max(maxYForX[x] ?? Int.min, y)
            minXForY[y] = min(minXForY[y] ?? Int.max, x)
            maxXForY[y] = max(maxXForY[y] ?? Int.min, x)
        }

        var uncoveredCount = 0
        for building in buildings {
            let x = building[0]
            let y = building[1]

            if y == minYForX[x]! ||
               y == maxYForX[x]! ||
               x == minXForY[y]! ||
               x == maxXForY[y]! {
                uncoveredCount += 1
            }
        }

        return buildings.count - uncoveredCount
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import kotlin.math.min
import kotlin.math.max

class Solution {
    fun countCoveredBuildings(n: Int, buildings: Array<IntArray>): Int {
        val minYForX = mutableMapOf<Int, Int>()
        val maxYForX = mutableMapOf<Int, Int>()
        val minXForY = mutableMapOf<Int, Int>()
        val maxXForY = mutableMapOf<Int, Int>()

        for (building in buildings) {
            val x = building[0]
            val y = building[1]

            minYForX[x] = min(minYForX.getOrDefault(x, Int.MAX_VALUE), y)
            maxYForX[x] = max(maxYForX.getOrDefault(x, Int.MIN_VALUE), y)
            minXForY[y] = min(minXForY.getOrDefault(y, Int.MAX_VALUE), x)
            maxXForY[y] = max(maxXForY.getOrDefault(y, Int.MIN_VALUE), x)
        }

        var uncoveredCount = 0
        for (building in buildings) {
            val x = building[0]
            val y = building[1]

            if (y == minYForX[x] ||
                y == maxYForX[x] ||
                x == minXForY[y] ||
                x == maxXForY[y]) {
                uncoveredCount++
            }
        }

        return buildings.size - uncoveredCount
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
  int countCoveredBuildings(int n, List<List<int>> buildings) {
    Map<int, int> minYForX = {};
    Map<int, int> maxYForX = {};
    Map<int, int> minXForY = {};
    Map<int, int> maxXForY = {};

    for (final building in buildings) {
      int x = building[0];
      int y = building[1];

      minYForX[x] = min(minYForX[x] ?? (1 << 31) - 1, y); // Dart's int.MAX_VALUE for 32-bit
      maxYForX[x] = max(maxYForX[x] ?? -(1 << 31), y); // Dart's int.MIN_VALUE for 32-bit
      minXForY[y] = min(minXForY[y] ?? (1 << 31) - 1, x);
      maxXForY[y] = max(maxXForY[y] ?? -(1 << 31), x);
    }

    int uncoveredCount = 0;
    for (final building in buildings) {
      int x = building[0];
      int y = building[1];

      if (y == minYForX[x] ||
          y == maxYForX[x] ||
          x == minXForY[y] ||
          x == maxXForY[y]) {
        uncoveredCount++;
      }
    }

    return buildings.length - uncoveredCount;
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
	"math"
)

func countCoveredBuildings(n int, buildings [][]int) int {
	minYForX := make(map[int]int)
	maxYForX := make(map[int]int)
	minXForY := make(map[int]int)
	maxXForY := make(map[int]int)

	for _, building := range buildings {
		x, y := building[0], building[1]

		if _, ok := minYForX[x]; !ok {
			minYForX[x] = math.MaxInt32
			maxYForX[x] = math.MinInt32
		}
		minYForX[x] = min(minYForX[x], y)
		maxYForX[x] = max(maxYForX[x], y)

		if _, ok := minXForY[y]; !ok {
			minXForY[y] = math.MaxInt32
			maxXForY[y] = math.MinInt32
		}
		minXForY[y] = min(minXForY[y], x)
		maxXForY[y] = max(maxXForY[y], x)
	}

	uncoveredCount := 0
	for _, building := range buildings {
		x, y := building[0], building[1]

		if y == minYForX[x] ||
			y == maxYForX[x] ||
			x == minXForY[y] ||
			x == maxXForY[y] {
			uncoveredCount++
		}
	}

	return len(buildings) - uncoveredCount
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} n
# @param {Integer[][]} buildings
# @return {Integer}
def count_covered_buildings(n, buildings)
    min_y_for_x = Hash.new { |hash, key| hash[key] = Float::INFINITY }
    max_y_for_x = Hash.new { |hash, key| hash[key] = -Float::INFINITY }
    min_x_for_y = Hash.new { |hash, key| hash[key] = Float::INFINITY }
    max_x_for_y = Hash.new { |hash, key| hash[key] = -Float::INFINITY }

    buildings.each do |x, y|
        min_y_for_x[x] = [min_y_for_x[x], y].min
        max_y_for_x[x] = [max_y_for_x[x], y].max
        min_x_for_y[y] = [min_x_for_y[y], x].min
        max_x_for_y[y] = [max_x_for_y[y], x].max
    end

    uncovered_count = 0
    buildings.each do |x, y|
        if y == min_y_for_x[x] ||
           y == max_y_for_x[x] ||
           x == min_x_for_y[y] ||
           x == max_x_for_y[y]
            uncovered_count += 1
        end
    end

    buildings.length - uncovered_count
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable
import scala.math.{min, max}

class Solution {
    def countCoveredBuildings(n: Int, buildings: Array[Array[Int]]): Int = {
        val minYForX = mutable.Map[Int, Int]().withDefaultValue(Int.MaxValue)
        val maxYForX = mutable.Map[Int, Int]().withDefaultValue(Int.MinValue)
        val minXForY = mutable.Map[Int, Int]().withDefaultValue(Int.MaxValue)
        val maxXForY = mutable.Map[Int, Int]().withDefaultValue(Int.MinValue)

        for (building <- buildings) {
            val x = building(0)
            val y = building(1)

            minYForX(x) = min(minYForX(x), y)
            maxYForX(x) = max(maxYForX(x), y)
            minXForY(y) = min(minXForY(y), x)
            maxXForY(y) = max(maxXForY(y), x)
        }

        var uncoveredCount = 0
        for (building <- buildings) {
            val x = building(0)
            val y = building(1)

            if (y == minYForX(x) ||
                y == maxYForX(x) ||
                x == minXForY(y) ||
                x == maxXForY(y)) {
                uncoveredCount += 1
            }
        }

        buildings.length - uncoveredCount
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::HashMap;
use std::cmp::{min, max};

impl Solution {
    pub fn count_covered_buildings(n: i32, buildings: Vec<Vec<i32>>) -> i32 {
        let mut min_y_for_x: HashMap<i32, i32> = HashMap::new();
        let mut max_y_for_x: HashMap<i32, i32> = HashMap::new();
        let mut min_x_for_y: HashMap<i32, i32> = HashMap::new();
        let mut max_x_for_y: HashMap<i32, i32> = HashMap::new();

        for building in &buildings {
            let x = building[0];
            let y = building[1];

            min_y_for_x.entry(x).and_modify(|v| *v = min(*v, y)).or_insert(y);
            max_y_for_x.entry(x).and_modify(|v| *v = max(*v, y)).or_insert(y);
            min_x_for_y.entry(y).and_modify(|v| *v = min(*v, x)).or_insert(x);
            max_x_for_y.entry(y).and_modify(|v| *v = max(*v, x)).or_insert(x);
        }

        let mut uncovered_count = 0;
        for building in &buildings {
            let x = building[0];
            let y = building[1];

            if y == *min_y_for_x.get(&x).unwrap() ||
               y == *max_y_for_x.get(&x).unwrap() ||
               x == *min_x_for_y.get(&y).unwrap() ||
               x == *max_x_for_y.get(&y).unwrap() {
                uncovered_count += 1;
            }
        }

        buildings.len() as i32 - uncovered_count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (count-covered-buildings n buildings)
  (define min-y-for-x (make-hash))
  (define max-y-for-x (make-hash))
  (define min-x-for-y (make-hash))
  (define max-x-for-y (make-hash))

  (for ([building buildings])
    (define x (vector-ref building 0))
    (define y (vector-ref building 1))

    (hash-update! min-y-for-x x (lambda (v) (min v y)) (add1 n)) ; n+1 as initial max value
    (hash-update! max-y-for-x x (lambda (v) (max v y)) 0)        ; 0 as initial min value
    (hash-update! min-x-for-y y (lambda (v) (min v x)) (add1 n))
    (hash-update! max-x-for-y y (lambda (v) (max v x)) 0))

  (define uncovered-count 0)
  (for ([building buildings])
    (define x (vector-ref building 0))
    (define y (vector-ref building 1))

    (when (or (= y (hash-ref min-y-for-x x))
              (= y (hash-ref max-y-for-x x))
              (= x (hash-ref min-x-for-y y))
              (= x (hash-ref max-x-for-y y)))
      (set! uncovered-count (add1 uncovered-count))))

  (- (length buildings) uncovered-count))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([count_covered_buildings/2]).

count_covered_buildings(_N, Buildings) ->
    MinYForX = maps:new(),
    MaxYForX = maps:new(),
    MinXForY = maps:new(),
    MaxXForY = maps:new(),

    {FinalMinYForX, FinalMaxYForX, FinalMinXForY, FinalMaxXForY} =
        lists:foldl(
            fun([X, Y], {AccMinYForX, AccMaxYForX, AccMinXForY, AccMaxXForY}) ->
                NewMinYForX = maps:update_with(X, fun(V) -> min(V, Y) end, Y, AccMinYForX),
                NewMaxYForX = maps:update_with(X, fun(V) -> max(V, Y) end, Y, AccMaxYForX),
                NewMinXForY = maps:update_with(Y, fun(V) -> min(V, X) end, X, AccMinXForY),
                NewMaxXForY = maps:update_with(Y, fun(V) -> max(V, X) end, X, AccMaxXForY),
                {NewMinYForX, NewMaxYForX, NewMinXForY, NewMaxXForY}
            end,
            {MinYForX, MaxYForX, MinXForY, MaxXForY},
            Buildings
        ),

    UncoveredCount =
        lists:foldl(
            fun([X, Y], AccUncovered) ->
                CurrentMinY = maps:get(X, FinalMinYForX),
                CurrentMaxY = maps:get(X, FinalMaxYForX),
                CurrentMinX = maps:get(Y, FinalMinXForY),
                CurrentMaxX = maps:get(Y, FinalMaxXForY),

                if
                    Y == CurrentMinY;
                    Y == CurrentMaxY;
                    X == CurrentMinX;
                    X == CurrentMaxX ->
                        AccUncovered + 1;
                    true ->
                        AccUncovered
                end
            end,
            0,
            Buildings
        ),

    length(Buildings) - UncoveredCount.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec count_covered_buildings(n :: integer, buildings :: [[integer]]) :: integer
  def count_covered_buildings(n, buildings) do
    {min_y_for_x, max_y_for_x, min_x_for_y, max_x_for_y} =
      Enum.reduce(buildings, {%{}, %{}, %{}, %{}}, fn [x, y], {acc_min_y_x, acc_max_y_x, acc_min_x_y, acc_max_x_y} ->
        new_min_y_x = Map.update(acc_min_y_x, x, y, fn val -> min(val, y) end)
        new_max_y_x = Map.update(acc_max_y_x, x, y, fn val -> max(val, y) end)
        new_min_x_y = Map.update(acc_min_x_y, y, x, fn val -> min(val, x) end)
        new_max_x_y = Map.update(acc_max_x_y, y, x, fn val -> max(val, x) end)
        {new_min_y_x, new_max_y_x, new_min_x_y, new_max_x_y}
      end)

    uncovered_count =
      Enum.reduce(buildings, 0, fn [x, y], acc_uncovered ->
        current_min_y = Map.fetch!(min_y_for_x, x)
        current_max_y = Map.fetch!(max_y_for_x, x)
        current_min_x = Map.fetch!(min_x_for_y, y)
        current_max_x = Map.fetch!(max_x_for_y, y)

        if y == current_min_y or
           y == current_max_y or
           x == current_min_x or
           x == current_max_x do
          acc_uncovered + 1
        else
          acc_uncovered
        end
      end)

    length(buildings) - uncovered_count
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(B) on average, where B is the number of buildings. This is because we iterate through the buildings twice. In the first pass, we perform constant-time (average) hash map operations (insertions and updates) for each of the B buildings. In the second pass, we perform constant-time (average) hash map lookups for each of the B buildings. If tree-based maps are used (e.g., std::map in C++), the complexity would be O(B log U) where U is the number of unique x or y coordinates, which can be at most B, leading to O(B log B). For the C solution, using arrays as direct lookup tables, the complexity is O(B + N) due to initialization of N elements.

- **Space Complexity:** The space complexity is O(B) on average. We use four hash maps (or arrays in C) to store the minimum and maximum y-coordinates for each x-coordinate, and the minimum and maximum x-coordinates for each y-coordinate. In the worst case, each unique x or y coordinate could correspond to a distinct entry in these maps. Since there are at most B unique x-coordinates and B unique y-coordinates, the total space used by these maps is proportional to B. For the C solution, using arrays of size N+1, the space complexity is O(N).

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-11 01:09:21 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by iterating over each building and checking if it has at least one building in all four directions. We can use a set to store the x and y coordinates of the buildings to efficiently check for the existence of buildings in each direction. The key intuition is to understand that a building is covered if it has at least one building above, below, to the left, and to the right of it. We can use a simple loop to iterate over each building and check for the existence of buildings in each direction.

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
    int countCoveredBuildings(int n, vector<vector<int>>& buildings) {
        int count = 0;
        for (auto& building : buildings) {
            bool covered = true;
            for (int i = 0; i < 4; i++) {
                bool found = false;
                for (auto& otherBuilding : buildings) {
                    if (i == 0 && otherBuilding[0] < building[0] && otherBuilding[1] == building[1]) found = true;
                    if (i == 1 && otherBuilding[0] > building[0] && otherBuilding[1] == building[1]) found = true;
                    if (i == 2 && otherBuilding[0] == building[0] && otherBuilding[1] < building[1]) found = true;
                    if (i == 3 && otherBuilding[0] == building[0] && otherBuilding[1] > building[1]) found = true;
                }
                if (!found) covered = false;
            }
            if (covered) count++;
        }
        return count;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int countCoveredBuildings(int n, int[][] buildings) {
        int count = 0;
        for (int[] building : buildings) {
            boolean covered = true;
            for (int i = 0; i < 4; i++) {
                boolean found = false;
                for (int[] otherBuilding : buildings) {
                    if (i == 0 && otherBuilding[0] < building[0] && otherBuilding[1] == building[1]) found = true;
                    if (i == 1 && otherBuilding[0] > building[0] && otherBuilding[1] == building[1]) found = true;
                    if (i == 2 && otherBuilding[0] == building[0] && otherBuilding[1] < building[1]) found = true;
                    if (i == 3 && otherBuilding[0] == building[0] && otherBuilding[1] > building[1]) found = true;
                }
                if (!found) covered = false;
            }
            if (covered) count++;
        }
        return count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        count = 0
        for building in buildings:
            covered = True
            for i in range(4):
                found = False
                for otherBuilding in buildings:
                    if i == 0 and otherBuilding[0] < building[0] and otherBuilding[1] == building[1]: found = True
                    if i == 1 and otherBuilding[0] > building[0] and otherBuilding[1] == building[1]: found = True
                    if i == 2 and otherBuilding[0] == building[0] and otherBuilding[1] < building[1]: found = True
                    if i == 3 and otherBuilding[0] == building[0] and otherBuilding[1] > building[1]: found = True
                if not found: covered = False
            if covered: count += 1
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        count = 0
        for building in buildings:
            covered = True
            for i in range(4):
                found = False
                for otherBuilding in buildings:
                    if i == 0 and otherBuilding[0] < building[0] and otherBuilding[1] == building[1]: found = True
                    if i == 1 and otherBuilding[0] > building[0] and otherBuilding[1] == building[1]: found = True
                    if i == 2 and otherBuilding[0] == building[0] and otherBuilding[1] < building[1]: found = True
                    if i == 3 and otherBuilding[0] == building[0] and otherBuilding[1] > building[1]: found = True
                if not found: covered = False
            if covered: count += 1
        return count
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
typedef struct {
    int x;
    int y;
} Building;

int compareBuildings(const void *a, const void *b) {
    Building *buildingA = (Building *)a;
    Building *buildingB = (Building *)b;
    if (buildingA->x < buildingB->x) return -1;
    if (buildingA->x > buildingB->x) return 1;
    if (buildingA->y < buildingB->y) return -1;
    if (buildingA->y > buildingB->y) return 1;
    return 0;
}

int countCoveredBuildings(int n, int **buildings, int buildingsSize) {
    int count = 0;
    for (int i = 0; i < buildingsSize; i++) {
        bool covered = true;
        for (int j = 0; j < 4; j++) {
            bool found = false;
            for (int k = 0; k < buildingsSize; k++) {
                if (j == 0 && buildings[k][0] < buildings[i][0] && buildings[k][1] == buildings[i][1]) found = true;
                if (j == 1 && buildings[k][0] > buildings[i][0] && buildings[k][1] == buildings[i][1]) found = true;
                if (j == 2 && buildings[k][0] == buildings[i][0] && buildings[k][1] < buildings[i][1]) found = true;
                if (j == 3 && buildings[k][0] == buildings[i][0] && buildings[k][1] > buildings[i][1]) found = true;
            }
            if (!found) covered = false;
        }
        if (covered) count++;
    }
    return count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int CountCoveredBuildings(int n, int[][] buildings) {
        int count = 0;
        for (int i = 0; i < buildings.Length; i++) {
            bool covered = true;
            for (int j = 0; j < 4; j++) {
                bool found = false;
                for (int k = 0; k < buildings.Length; k++) {
                    if (j == 0 && buildings[k][0] < buildings[i][0] && buildings[k][1] == buildings[i][1]) found = true;
                    if (j == 1 && buildings[k][0] > buildings[i][0] && buildings[k][1] == buildings[i][1]) found = true;
                    if (j == 2 && buildings[k][0] == buildings[i][0] && buildings[k][1] < buildings[i][1]) found = true;
                    if (j == 3 && buildings[k][0] == buildings[i][0] && buildings[k][1] > buildings[i][1]) found = true;
                }
                if (!found) covered = false;
            }
            if (covered) count++;
        }
        return count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var countCoveredBuildings = function(n, buildings) {
    let count = 0;
    for (let i = 0; i < buildings.length; i++) {
        let covered = true;
        for (let j = 0; j < 4; j++) {
            let found = false;
            for (let k = 0; k < buildings.length; k++) {
                if (j == 0 && buildings[k][0] < buildings[i][0] && buildings[k][1] == buildings[i][1]) found = true;
                if (j == 1 && buildings[k][0] > buildings[i][0] && buildings[k][1] == buildings[i][1]) found = true;
                if (j == 2 && buildings[k][0] == buildings[i][0] && buildings[k][1] < buildings[i][1]) found = true;
                if (j == 3 && buildings[k][0] == buildings[i][0] && buildings[k][1] > buildings[i][1]) found = true;
            }
            if (!found) covered = false;
        }
        if (covered) count++;
    }
    return count;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countCoveredBuildings(n: number, buildings: number[][]): number {
    let count: number = 0;
    for (let i: number = 0; i < buildings.length; i++) {
        let covered: boolean = true;
        for (let j: number = 0; j < 4; j++) {
            let found: boolean = false;
            for (let k: number = 0; k < buildings.length; k++) {
                if (j == 0 && buildings[k][0] < buildings[i][0] && buildings[k][1] == buildings[i][1]) found = true;
                if (j == 1 && buildings[k][0] > buildings[i][0] && buildings[k][1] == buildings[i][1]) found = true;
                if (j == 2 && buildings[k][0] == buildings[i][0] && buildings[k][1] < buildings[i][1]) found = true;
                if (j == 3 && buildings[k][0] == buildings[i][0] && buildings[k][1] > buildings[i][1]) found = true;
            }
            if (!found) covered = false;
        }
        if (covered) count++;
    }
    return count;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function countCoveredBuildings($n, $buildings) {
        $count = 0;
        for ($i = 0; $i < count($buildings); $i++) {
            $covered = true;
            for ($j = 0; $j < 4; $j++) {
                $found = false;
                for ($k = 0; $k < count($buildings); $k++) {
                    if ($j == 0 && $buildings[$k][0] < $buildings[$i][0] && $buildings[$k][1] == $buildings[$i][1]) $found = true;
                    if ($j == 1 && $buildings[$k][0] > $buildings[$i][0] && $buildings[$k][1] == $buildings[$i][1]) $found = true;
                    if ($j == 2 && $buildings[$k][0] == $buildings[$i][0] && $buildings[$k][1] < $buildings[$i][1]) $found = true;
                    if ($j == 3 && $buildings[$k][0] == $buildings[$i][0] && $buildings[$k][1] > $buildings[$i][1]) $found = true;
                }
                if (!$found) $covered = false;
            }
            if ($covered) $count++;
        }
        return $count;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func countCoveredBuildings(_ n: Int, _ buildings: [[Int]]) -> Int {
        var count: Int = 0
        for i in 0..<buildings.count {
            var covered: Bool = true
            for j in 0..<4 {
                var found: Bool = false
                for k in 0..<buildings.count {
                    if j == 0 && buildings[k][0] < buildings[i][0] && buildings[k][1] == buildings[i][1] { found = true }
                    if j == 1 && buildings[k][0] > buildings[i][0] && buildings[k][1] == buildings[i][1] { found = true }
                    if j == 2 && buildings[k][0] == buildings[i][0] && buildings[k][1] < buildings[i][1] { found = true }
                    if j == 3 && buildings[k][0] == buildings[i][0] && buildings[k][1] > buildings[i][1] { found = true }
                }
                if !found { covered = false }
            }
            if covered { count += 1 }
        }
        return count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun countCoveredBuildings(n: Int, buildings: Array<IntArray>): Int {
        var count: Int = 0
        for (i in buildings.indices) {
            var covered: Boolean = true
            for (j in 0 until 4) {
                var found: Boolean = false
                for (k in buildings.indices) {
                    if (j == 0 && buildings[k][0] < buildings[i][0] && buildings[k][1] == buildings[i][1]) found = true
                    if (j == 1 && buildings[k][0] > buildings[i][0] && buildings[k][1] == buildings[i][1]) found = true
                    if (j == 2 && buildings[k][0] == buildings[i][0] && buildings[k][1] < buildings[i][1]) found = true
                    if (j == 3 && buildings[k][0] == buildings[i][0] && buildings[k][1] > buildings[i][1]) found = true
                }
                if (!found) covered = false
            }
            if (covered) count++
        }
        return count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int countCoveredBuildings(int n, List<List<int>> buildings) {
        int count = 0;
        for (int i = 0; i < buildings.length; i++) {
            bool covered = true;
            for (int j = 0; j < 4; j++) {
                bool found = false;
                for (int k = 0; k < buildings.length; k++) {
                    if (j == 0 && buildings[k][0] < buildings[i][0] && buildings[k][1] == buildings[i][1]) found = true;
                    if (j == 1 && buildings[k][0] > buildings[i][0] && buildings[k][1] == buildings[i][1]) found = true;
                    if (j == 2 && buildings[k][0] == buildings[i][0] && buildings[k][1] < buildings[i][1]) found = true;
                    if (j == 3 && buildings[k][0] == buildings[i][0] && buildings[k][1] > buildings[i][1]) found = true;
                }
                if (!found) covered = false;
            }
            if (covered) count++;
        }
        return count;
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

func (s *Solution) countCoveredBuildings(n int, buildings [][]int) int {
    count := 0
    for i := 0; i < len(buildings); i++ {
        covered := true
        for j := 0; j < 4; j++ {
            found := false
            for k := 0; k < len(buildings); k++ {
                if j == 0 && buildings[k][0] < buildings[i][0] && buildings[k][1] == buildings[i][1] {
                    found = true
                }
                if j == 1 && buildings[k][0] > buildings[i][0] && buildings[k][1] == buildings[i][1] {
                    found = true
                }
                if j == 2 && buildings[k][0] == buildings[i][0] && buildings[k][1] < buildings[i][1] {
                    found = true
                }
                if j == 3 && buildings[k][0] == buildings[i][0] && buildings[k][1] > buildings[i][1] {
                    found = true
                }
            }
            if !found {
                covered = false
            }
        }
        if covered {
            count++
        }
    }
    return count
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    def count_covered_buildings(n, buildings)
        count = 0
        buildings.each_with_index do |building, i|
            covered = true
            4.times do |j|
                found = false
                buildings.each_with_index do |other_building, k|
                    if j == 0 && other_building[0] < building[0] && other_building[1] == building[1]
                        found = true
                    elsif j == 1 && other_building[0] > building[0] && other_building[1] == building[1]
                        found = true
                    elsif j == 2 && other_building[0] == building[0] && other_building[1] < building[1]
                        found = true
                    elsif j == 3 && other_building[0] == building[0] && other_building[1] > building[1]
                        found = true
                    end
                end
                if !found
                    covered = false
                end
            end
            if covered
                count += 1
            end
        end
        count
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def countCoveredBuildings(n: Int, buildings: Array[Array[Int]]): Int = {
        var count: Int = 0
        for (i <- buildings.indices) {
            var covered: Boolean = true
            for (j <- 0 until 4) {
                var found: Boolean = false
                for (k <- buildings.indices) {
                    if (j == 0 && buildings(k)(0) < buildings(i)(0) && buildings(k)(1) == buildings(i)(1)) found = true
                    if (j == 1 && buildings(k)(0) > buildings(i)(0) && buildings(k)(1) == buildings(i)(1)) found = true
                    if (j == 2 && buildings(k)(0) == buildings(i)(0) && buildings(k)(1) < buildings(i)(1)) found = true
                    if (j == 3 && buildings(k)(0) == buildings(i)(0) && buildings(k)(1) > buildings(i)(1)) found = true
                }
                if (!found) covered = false
            }
            if (covered) count += 1
        }
        count
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
    pub fn count_covered_buildings(n: i32, buildings: Vec<Vec<i32>>) -> i32 {
        let mut count: i32 = 0;
        for i in 0..buildings.len() {
            let mut covered: bool = true;
            for j in 0..4 {
                let mut found: bool = false;
                for k in 0..buildings.len() {
                    if j == 0 && buildings[k][0] < buildings[i][0] && buildings[k][1] == buildings[i][1] {
                        found = true;
                    }
                    if j == 1 && buildings[k][0] > buildings[i][0] && buildings[k][1] == buildings[i][1] {
                        found = true;
                    }
                    if j == 2 && buildings[k][0] == buildings[i][0] && buildings[k][1] < buildings[i][1] {
                        found = true;
                    }
                    if j == 3 && buildings[k][0] == buildings[i][0] && buildings[k][1] > buildings[i][1] {
                        found = true;
                    }
                }
                if !found {
                    covered = false;
                }
            }
            if covered {
                count += 1;
            }
        }
        count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
define (count-covered-buildings n buildings)
    (let loop ((i 0) (count 0))
        (if (>= i (length buildings))
            count
            (let ((building (list-ref buildings i))
                  (covered #t))
                (for-each (lambda (j)
                            (let ((found #f))
                                (for-each (lambda (k)
                                            (when (or (and (= j 0) (< (car k) (car building)) (= (cadr k) (cadr building)))
                                                      (and (= j 1) (> (car k) (car building)) (= (cadr k) (cadr building)))
                                                      (and (= j 2) (= (car k) (car building)) (< (cadr k) (cadr building)))
                                                      (and (= j 3) (= (car k) (car building)) (> (cadr k) (cadr building))))
                                            (set! found #t))
                                          buildings)
                                (when (not found)
                                    (set! covered #f))
                            )
                          '(0 1 2 3))
                (loop (+ i 1) (if covered (+ count 1) count))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
count_covered_buildings(N, Buildings) ->
    count_covered_buildings(N, Buildings, 0).

count_covered_buildings(N, [], Count) -> Count;

count_covered_buildings(N, [Building | Buildings], Count) ->
    case is_covered(Building, Buildings) of
        true -> count_covered_buildings(N, Buildings, Count + 1);
        false -> count_covered_buildings(N, Buildings, Count)
    end.

is_covered(Building, Buildings) ->
    is_covered(Building, Buildings, [0, 1, 2, 3], true).

is_covered(_Building, _Buildings, [], Covered) -> Covered;

is_covered(Building, Buildings, [Direction | Directions], Covered) ->
    case has_neighbor(Building, Direction, Buildings) of
        true -> is_covered(Building, Buildings, Directions, Covered);
        false -> is_covered(Building, Buildings, Directions, false)
    end.

has_neighbor(Building, 0, Buildings) -> has_neighbor(Building, 0, Buildings, false);

has_neighbor(Building, 1, Buildings) -> has_neighbor(Building, 1, Buildings, false);

has_neighbor(Building, 2, Buildings) -> has_neighbor(Building, 2, Buildings, false);

has_neighbor(Building, 3, Buildings) -> has_neighbor(Building, 3, Buildings, false).

has_neighbor(_Building, _Direction, [], Found) -> Found;

has_neighbor(Building, 0, [OtherBuilding | Buildings], Found) ->
    if
        OtherBuilding =:= [X, Y],
        X < element(1, Building),
        Y =:= element(2, Building)
    ->
        has_neighbor(Building, 0, Buildings, true);
    true -> has_neighbor(Building, 0, Buildings, Found).

has_neighbor(Building, 1, [OtherBuilding | Buildings], Found) ->
    if
        OtherBuilding =:= [X, Y],
        X > element(1, Building),
        Y =:= element(2, Building)
    ->
        has_neighbor(Building, 1, Buildings, true);
    true -> has_neighbor(Building, 1, Buildings, Found).

has_neighbor(Building, 2, [OtherBuilding | Buildings], Found) ->
    if
        OtherBuilding =:= [X, Y],
        X =:= element(1, Building),
        Y < element(2, Building)
    ->
        has_neighbor(Building, 2, Buildings, true);
    true -> has_neighbor(Building, 2, Buildings, Found).

has_neighbor(Building, 3, [OtherBuilding | Buildings], Found) ->
    if
        OtherBuilding =:= [X, Y],
        X =:= element(1, Building),
        Y > element(2, Building)
    ->
        has_neighbor(Building, 3, Buildings, true);
    true -> has_neighbor(Building, 3, Buildings, Found).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
    def count_covered_buildings(n, buildings) do
        count_covered_buildings(n, buildings, 0)
    end

    defp count_covered_buildings(_n, [], count) do
        count
    end

    defp count_covered_buildings(n, [building | buildings], count) do
        if is_covered?(building, buildings) do
            count_covered_buildings(n, buildings, count + 1)
        else
            count_covered_buildings(n, buildings, count)
        end
    end

    defp is_covered?(building, buildings) do
        is_covered?(building, buildings, [0, 1, 2, 3], true)
    end

    defp is_covered?(_building, _buildings, [], covered) do
        covered
    end

    defp is_covered?(building, buildings, [direction | directions], covered) do
        if has_neighbor?(building, direction, buildings) do
            is_covered?(building, buildings, directions, covered)
        else
            is_covered?(building, buildings, directions, false)
        end
    end

    defp has_neighbor?(_building, _direction, []) do
        false
    end

    defp has_neighbor?(building, 0, [other_building | buildings]) do
        if other_building == [x, y] and x < elem(building, 0) and y == elem(building, 1) do
            true
        else
            has_neighbor?(building, 0, buildings)
        end
    end

    defp has_neighbor?(building, 1, [other_building | buildings]) do
        if other_building == [x, y] and x > elem(building, 0) and y == elem(building, 1) do
            true
        else
            has_neighbor?(building, 1, buildings)
        end
    end

    defp has_neighbor?(building, 2, [other_building | buildings]) do
        if other_building == [x, y] and x == elem(building, 0) and y < elem(building, 1) do
            true
        else
            has_neighbor?(building, 2, buildings)
        end
    end

    defp has_neighbor?(building, 3, [other_building | buildings]) do
        if other_building == [x, y] and x == elem(building, 0) and y > elem(building, 1) do
            true
        else
            has_neighbor?(building, 3, buildings)
        end
    end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of the solution is O(n^2) where n is the number of buildings. This is because we are iterating over each building and checking for the existence of buildings in each direction. The space complexity is O(n) as we are storing the x and y coordinates of the buildings in a set.

- **Space Complexity:** The space complexity of the solution is O(n) where n is the number of buildings. This is because we are storing the x and y coordinates of the buildings in a set.

</div>
</details>
