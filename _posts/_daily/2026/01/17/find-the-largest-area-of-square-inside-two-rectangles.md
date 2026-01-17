---
layout: post
title: "Find the Largest Area of Square Inside Two Rectangles"
date: 2026-01-17 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Math", "Geometry"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\nlong long largestSquareArea(vector<vector<int>>&\
        \ bottomLeft, vector<vector<int>>& topRight) {\nint n = bottomLeft.size();\n\
        long long max_side_length = 0;\n\nfor (int i = 0; i < n; ++i) {\nfor (int j\
        \ = i + 1; j < n; ++j) {\n    // Rectangle i: (x1_i, y1_i) to (x2_i, y2_i)\n\
        \    long long x1_i = bottomLeft[i][0];\n    long long y1_i = bottomLeft[i][1];\n\
        \    long long x2_i = topRight[i][0];\n    long long y2_i = topRight[i][1];\n\
        \n    // Rectangle j: (x1_j, y1_j) to (x2_j, y2_j)\n    long long x1_j = bottomLeft[j][0];\n\
        \    long long y1_j = bottomLeft[j][1];\n    long long x2_j = topRight[j][0];\n\
        \    long long y2_j = topRight[j][1];\n\n    // Calculate intersection coordinates\n\
        \    long long intersect_x_left = max(x1_i, x1_j);\n    long long intersect_y_bottom\
        \ = max(y1_i, y1_j);\n    long long intersect_x_right = min(x2_i, x2_j);\n \
        \   long long intersect_y_top = min(y2_i, y2_j);\n\n    // Check if an intersection\
        \ exists (positive width and height)\n    if (intersect_x_left < intersect_x_right\
        \ && intersect_y_bottom < intersect_y_top) {\n        long long current_width\
        \ = intersect_x_right - intersect_x_left;\n        long long current_height\
        \ = intersect_y_top - intersect_y_bottom;\n        long long current_side =\
        \ min(current_width, current_height);\n        max_side_length = max(max_side_length,\
        \ current_side);\n    }\n}\n}\n\nreturn max_side_length * max_side_length;\n\
        }\n};"
      java: "class Solution {\n    public long largestSquareArea(int[][] bottomLeft,\
        \ int[][] topRight) {\n        int n = bottomLeft.length;\n        long maxSideLength\
        \ = 0;\n\n        for (int i = 0; i < n; i++) {\n            for (int j = i\
        \ + 1; j < n; j++) {\n                // Rectangle i: (x1_i, y1_i) to (x2_i,\
        \ y2_i)\n                long x1_i = bottomLeft[i][0];\n                long\
        \ y1_i = bottomLeft[i][1];\n                long x2_i = topRight[i][0];\n  \
        \              long y2_i = topRight[i][1];\n\n                // Rectangle j:\
        \ (x1_j, y1_j) to (x2_j, y2_j)\n                long x1_j = bottomLeft[j][0];\n\
        \                long y1_j = bottomLeft[j][1];\n                long x2_j =\
        \ topRight[j][0];\n                long y2_j = topRight[j][1];\n\n         \
        \       // Calculate intersection coordinates\n                long intersect_x_left\
        \ = Math.max(x1_i, x1_j);\n                long intersect_y_bottom = Math.max(y1_i,\
        \ y1_j);\n                long intersect_x_right = Math.min(x2_i, x2_j);\n \
        \               long intersect_y_top = Math.min(y2_i, y2_j);\n\n           \
        \     // Check if an intersection exists (positive width and height)\n     \
        \           if (intersect_x_left < intersect_x_right && intersect_y_bottom <\
        \ intersect_y_top) {\n                    long current_width = intersect_x_right\
        \ - intersect_x_left;\n                    long current_height = intersect_y_top\
        \ - intersect_y_bottom;\n                    long current_side = Math.min(current_width,\
        \ current_height);\n                    maxSideLength = Math.max(maxSideLength,\
        \ current_side);\n                }\n            }\n        }\n\n        return\
        \ maxSideLength * maxSideLength;\n    }\n}"
      python: "class Solution(object):\n    def largestSquareArea(self, bottomLeft,\
        \ topRight):\n        \"\"\"\n        :type bottomLeft: List[List[int]]\n  \
        \      :type topRight: List[List[int]]\n        :rtype: int\n        \"\"\"\n\
        \        n = len(bottomLeft)\n        max_side_length = 0\n\n        for i in\
        \ range(n):\n            for j in range(i + 1, n):\n                # Rectangle\
        \ i: (x1_i, y1_i) to (x2_i, y2_i)\n                x1_i, y1_i = bottomLeft[i][0],\
        \ bottomLeft[i][1]\n                x2_i, y2_i = topRight[i][0], topRight[i][1]\n\
        \n                # Rectangle j: (x1_j, y1_j) to (x2_j, y2_j)\n            \
        \    x1_j, y1_j = bottomLeft[j][0], bottomLeft[j][1]\n                x2_j,\
        \ y2_j = topRight[j][0], topRight[j][1]\n\n                # Calculate intersection\
        \ coordinates\n                intersect_x_left = max(x1_i, x1_j)\n        \
        \        intersect_y_bottom = max(y1_i, y1_j)\n                intersect_x_right\
        \ = min(x2_i, x2_j)\n                intersect_y_top = min(y2_i, y2_j)\n\n \
        \               # Check if an intersection exists (positive width and height)\n\
        \                if intersect_x_left < intersect_x_right and intersect_y_bottom\
        \ < intersect_y_top:\n                    current_width = intersect_x_right\
        \ - intersect_x_left\n                    current_height = intersect_y_top -\
        \ intersect_y_bottom\n                    current_side = min(current_width,\
        \ current_height)\n                    max_side_length = max(max_side_length,\
        \ current_side)\n\n        return max_side_length * max_side_length"
      python3: "class Solution:\n    def largestSquareArea(self, bottomLeft: List[List[int]],\
        \ topRight: List[List[int]]) -> int:\n        n = len(bottomLeft)\n        max_side_length\
        \ = 0\n\n        for i in range(n):\n            for j in range(i + 1, n):\n\
        \                # Rectangle i: (x1_i, y1_i) to (x2_i, y2_i)\n             \
        \   x1_i, y1_i = bottomLeft[i][0], bottomLeft[i][1]\n                x2_i, y2_i\
        \ = topRight[i][0], topRight[i][1]\n\n                # Rectangle j: (x1_j,\
        \ y1_j) to (x2_j, y2_j)\n                x1_j, y1_j = bottomLeft[j][0], bottomLeft[j][1]\n\
        \                x2_j, y2_j = topRight[j][0], topRight[j][1]\n\n           \
        \     # Calculate intersection coordinates\n                intersect_x_left\
        \ = max(x1_i, x1_j)\n                intersect_y_bottom = max(y1_i, y1_j)\n\
        \                intersect_x_right = min(x2_i, x2_j)\n                intersect_y_top\
        \ = min(y2_i, y2_j)\n\n                # Check if an intersection exists (positive\
        \ width and height)\n                if intersect_x_left < intersect_x_right\
        \ and intersect_y_bottom < intersect_y_top:\n                    current_width\
        \ = intersect_x_right - intersect_x_left\n                    current_height\
        \ = intersect_y_top - intersect_y_bottom\n                    current_side =\
        \ min(current_width, current_height)\n                    max_side_length =\
        \ max(max_side_length, current_side)\n\n        return max_side_length * max_side_length"
      c: "long long largestSquareArea(int** bottomLeft, int bottomLeftSize, int* bottomLeftColSize,\
        \ int** topRight, int topRightSize, int* topRightColSize) {\nint n = bottomLeftSize;\n\
        long long max_side_length = 0;\n\nfor (int i = 0; i < n; ++i) {\nfor (int j\
        \ = i + 1; j < n; ++j) {\n// Rectangle i: (x1_i, y1_i) to (x2_i, y2_i)\nlong\
        \ long x1_i = bottomLeft[i][0];\nlong long y1_i = bottomLeft[i][1];\nlong long\
        \ x2_i = topRight[i][0];\nlong long y2_i = topRight[i][1];\n\n// Rectangle j:\
        \ (x1_j, y1_j) to (x2_j, y2_j)\nlong long x1_j = bottomLeft[j][0];\nlong long\
        \ y1_j = bottomLeft[j][1];\nlong long x2_j = topRight[j][0];\nlong long y2_j\
        \ = topRight[j][1];\n\n// Calculate intersection coordinates\nlong long intersect_x_left\
        \ = (x1_i > x1_j) ? x1_i : x1_j; // max\nlong long intersect_y_bottom = (y1_i\
        \ > y1_j) ? y1_i : y1_j; // max\nlong long intersect_x_right = (x2_i < x2_j)\
        \ ? x2_i : x2_j; // min\nlong long intersect_y_top = (y2_i < y2_j) ? y2_i :\
        \ y2_j; // min\n\n// Check if an intersection exists (positive width and height)\n\
        if (intersect_x_left < intersect_x_right && intersect_y_bottom < intersect_y_top)\
        \ {\n    long long current_width = intersect_x_right - intersect_x_left;\n \
        \   long long current_height = intersect_y_top - intersect_y_bottom;\n    long\
        \ long current_side = (current_width < current_height) ? current_width : current_height;\
        \ // min\n    max_side_length = (max_side_length > current_side) ? max_side_length\
        \ : current_side; // max\n}\n}\n}\n\nreturn max_side_length * max_side_length;\n\
        }"
      csharp: "public class Solution {\n    public long LargestSquareArea(int[][] bottomLeft,\
        \ int[][] topRight) {\n        int n = bottomLeft.Length;\n        long maxSideLength\
        \ = 0;\n\n        for (int i = 0; i < n; i++) {\n            for (int j = i\
        \ + 1; j < n; j++) {\n                // Rectangle i: (x1_i, y1_i) to (x2_i,\
        \ y2_i)\n                long x1_i = bottomLeft[i][0];\n                long\
        \ y1_i = bottomLeft[i][1];\n                long x2_i = topRight[i][0];\n  \
        \              long y2_i = topRight[i][1];\n\n                // Rectangle j:\
        \ (x1_j, y1_j) to (x2_j, y2_j)\n                long x1_j = bottomLeft[j][0];\n\
        \                long y1_j = bottomLeft[j][1];\n                long x2_j =\
        \ topRight[j][0];\n                long y2_j = topRight[j][1];\n\n         \
        \       // Calculate intersection coordinates\n                long intersect_x_left\
        \ = Math.Max(x1_i, x1_j);\n                long intersect_y_bottom = Math.Max(y1_i,\
        \ y1_j);\n                long intersect_x_right = Math.Min(x2_i, x2_j);\n \
        \               long intersect_y_top = Math.Min(y2_i, y2_j);\n\n           \
        \     // Check if an intersection exists (positive width and height)\n     \
        \           if (intersect_x_left < intersect_x_right && intersect_y_bottom <\
        \ intersect_y_top) {\n                    long current_width = intersect_x_right\
        \ - intersect_x_left;\n                    long current_height = intersect_y_top\
        \ - intersect_y_bottom;\n                    long current_side = Math.Min(current_width,\
        \ current_height);\n                    maxSideLength = Math.Max(maxSideLength,\
        \ current_side);\n                }\n            }\n        }\n\n        return\
        \ maxSideLength * maxSideLength;\n    }\n}"
      javascript: "/**\n * @param {number[][]} bottomLeft\n * @param {number[][]} topRight\n\
        \ * @return {number}\n */\nvar largestSquareArea = function(bottomLeft, topRight)\
        \ {\n    const n = bottomLeft.length;\n    let maxSideLength = 0;\n\n    for\
        \ (let i = 0; i < n; i++) {\n        for (let j = i + 1; j < n; j++) {\n   \
        \         // Rectangle i: (x1_i, y1_i) to (x2_i, y2_i)\n            const x1_i\
        \ = bottomLeft[i][0];\n            const y1_i = bottomLeft[i][1];\n        \
        \    const x2_i = topRight[i][0];\n            const y2_i = topRight[i][1];\n\
        \n            // Rectangle j: (x1_j, y1_j) to (x2_j, y2_j)\n            const\
        \ x1_j = bottomLeft[j][0];\n            const y1_j = bottomLeft[j][1];\n   \
        \         const x2_j = topRight[j][0];\n            const y2_j = topRight[j][1];\n\
        \n            // Calculate intersection coordinates\n            const intersect_x_left\
        \ = Math.max(x1_i, x1_j);\n            const intersect_y_bottom = Math.max(y1_i,\
        \ y1_j);\n            const intersect_x_right = Math.min(x2_i, x2_j);\n    \
        \        const intersect_y_top = Math.min(y2_i, y2_j);\n\n            // Check\
        \ if an intersection exists (positive width and height)\n            if (intersect_x_left\
        \ < intersect_x_right && intersect_y_bottom < intersect_y_top) {\n         \
        \       const current_width = intersect_x_right - intersect_x_left;\n      \
        \          const current_height = intersect_y_top - intersect_y_bottom;\n  \
        \              const current_side = Math.min(current_width, current_height);\n\
        \                maxSideLength = Math.max(maxSideLength, current_side);\n  \
        \          }\n        }\n    }\n\n    return maxSideLength * maxSideLength;\n\
        };"
      typescript: "function largestSquareArea(bottomLeft: number[][], topRight: number[][]):\
        \ number {\n    const n = bottomLeft.length;\n    let maxSideLength = 0;\n\n\
        \    for (let i = 0; i < n; i++) {\n        for (let j = i + 1; j < n; j++)\
        \ {\n            // Rectangle i: (x1_i, y1_i) to (x2_i, y2_i)\n            const\
        \ x1_i = bottomLeft[i][0];\n            const y1_i = bottomLeft[i][1];\n   \
        \         const x2_i = topRight[i][0];\n            const y2_i = topRight[i][1];\n\
        \n            // Rectangle j: (x1_j, y1_j) to (x2_j, y2_j)\n            const\
        \ x1_j = bottomLeft[j][0];\n            const y1_j = bottomLeft[j][1];\n   \
        \         const x2_j = topRight[j][0];\n            const y2_j = topRight[j][1];\n\
        \n            // Calculate intersection coordinates\n            const intersect_x_left\
        \ = Math.max(x1_i, x1_j);\n            const intersect_y_bottom = Math.max(y1_i,\
        \ y1_j);\n            const intersect_x_right = Math.min(x2_i, x2_j);\n    \
        \        const intersect_y_top = Math.min(y2_i, y2_j);\n\n            // Check\
        \ if an intersection exists (positive width and height)\n            if (intersect_x_left\
        \ < intersect_x_right && intersect_y_bottom < intersect_y_top) {\n         \
        \       const current_width = intersect_x_right - intersect_x_left;\n      \
        \          const current_height = intersect_y_top - intersect_y_bottom;\n  \
        \              const current_side = Math.min(current_width, current_height);\n\
        \                maxSideLength = Math.max(maxSideLength, current_side);\n  \
        \          }\n        }\n    }\n\n    return maxSideLength * maxSideLength;\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $bottomLeft\n   \
        \  * @param Integer[][] $topRight\n     * @return Integer\n     */\n    function\
        \ largestSquareArea($bottomLeft, $topRight) {\n        $n = count($bottomLeft);\n\
        \        $maxSideLength = 0;\n\n        for ($i = 0; $i < $n; $i++) {\n    \
        \        for ($j = $i + 1; $j < $n; $j++) {\n                // Rectangle i:\
        \ (x1_i, y1_i) to (x2_i, y2_i)\n                $x1_i = $bottomLeft[$i][0];\n\
        \                $y1_i = $bottomLeft[$i][1];\n                $x2_i = $topRight[$i][0];\n\
        \                $y2_i = $topRight[$i][1];\n\n                // Rectangle j:\
        \ (x1_j, y1_j) to (x2_j, y2_j)\n                $x1_j = $bottomLeft[$j][0];\n\
        \                $y1_j = $bottomLeft[$j][1];\n                $x2_j = $topRight[$j][0];\n\
        \                $y2_j = $topRight[$j][1];\n\n                // Calculate intersection\
        \ coordinates\n                $intersect_x_left = max($x1_i, $x1_j);\n    \
        \            $intersect_y_bottom = max($y1_i, $y1_j);\n                $intersect_x_right\
        \ = min($x2_i, $x2_j);\n                $intersect_y_top = min($y2_i, $y2_j);\n\
        \n                // Check if an intersection exists (positive width and height)\n\
        \                if ($intersect_x_left < $intersect_x_right && $intersect_y_bottom\
        \ < $intersect_y_top) {\n                    $current_width = $intersect_x_right\
        \ - $intersect_x_left;\n                    $current_height = $intersect_y_top\
        \ - $intersect_y_bottom;\n                    $current_side = min($current_width,\
        \ $current_height);\n                    $maxSideLength = max($maxSideLength,\
        \ $current_side);\n                }\n            }\n        }\n\n        return\
        \ $maxSideLength * $maxSideLength;\n    }\n}"
      swift: "class Solution {\n    func largestSquareArea(_ bottomLeft: [[Int]], _\
        \ topRight: [[Int]]) -> Int {\n        let n = bottomLeft.count\n        var\
        \ maxSideLength: Int = 0\n\n        for i in 0..<n {\n            for j in i\
        \ + 1..<n {\n                // Rectangle i: (x1_i, y1_i) to (x2_i, y2_i)\n\
        \                let x1_i = bottomLeft[i][0]\n                let y1_i = bottomLeft[i][1]\n\
        \                let x2_i = topRight[i][0]\n                let y2_i = topRight[i][1]\n\
        \n                // Rectangle j: (x1_j, y1_j) to (x2_j, y2_j)\n           \
        \     let x1_j = bottomLeft[j][0]\n                let y1_j = bottomLeft[j][1]\n\
        \                let x2_j = topRight[j][0]\n                let y2_j = topRight[j][1]\n\
        \n                // Calculate intersection coordinates\n                let\
        \ intersect_x_left = max(x1_i, x1_j)\n                let intersect_y_bottom\
        \ = max(y1_i, y1_j)\n                let intersect_x_right = min(x2_i, x2_j)\n\
        \                let intersect_y_top = min(y2_i, y2_j)\n\n                //\
        \ Check if an intersection exists (positive width and height)\n            \
        \    if intersect_x_left < intersect_x_right && intersect_y_bottom < intersect_y_top\
        \ {\n                    let current_width = intersect_x_right - intersect_x_left\n\
        \                    let current_height = intersect_y_top - intersect_y_bottom\n\
        \                    let current_side = min(current_width, current_height)\n\
        \                    maxSideLength = max(maxSideLength, current_side)\n    \
        \            }\n            }\n        }\n\n        return maxSideLength * maxSideLength\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun largestSquareArea(bottomLeft: Array<IntArray>,\
        \ topRight: Array<IntArray>): Long {\n        var maxSide: Long = 0\n      \
        \  val n = bottomLeft.size\n\n        for (i in 0 until n) {\n            for\
        \ (j in i + 1 until n) {\n                val x1_i = bottomLeft[i][0]\n    \
        \            val y1_i = bottomLeft[i][1]\n                val x2_i = topRight[i][0]\n\
        \                val y2_i = topRight[i][1]\n\n                val x1_j = bottomLeft[j][0]\n\
        \                val y1_j = bottomLeft[j][1]\n                val x2_j = topRight[j][0]\n\
        \                val y2_j = topRight[j][1]\n\n                val intersect_x1\
        \ = maxOf(x1_i, x1_j)\n                val intersect_y1 = maxOf(y1_i, y1_j)\n\
        \                val intersect_x2 = minOf(x2_i, x2_j)\n                val intersect_y2\
        \ = minOf(y2_i, y2_j)\n\n                if (intersect_x1 < intersect_x2 &&\
        \ intersect_y1 < intersect_y2) {\n                    val width = (intersect_x2\
        \ - intersect_x1).toLong()\n                    val height = (intersect_y2 -\
        \ intersect_y1).toLong()\n                    val currentSide = minOf(width,\
        \ height)\n                    maxSide = maxOf(maxSide, currentSide)\n     \
        \           }\n            }\n        }\n        return maxSide * maxSide\n\
        \    }\n}"
      dart: "class Solution {\n  int largestSquareArea(List<List<int>> bottomLeft, List<List<int>>\
        \ topRight) {\n    int maxSide = 0;\n    int n = bottomLeft.length;\n\n    for\
        \ (int i = 0; i < n; i++) {\n      for (int j = i + 1; j < n; j++) {\n     \
        \   int x1_i = bottomLeft[i][0];\n        int y1_i = bottomLeft[i][1];\n   \
        \     int x2_i = topRight[i][0];\n        int y2_i = topRight[i][1];\n\n   \
        \     int x1_j = bottomLeft[j][0];\n        int y1_j = bottomLeft[j][1];\n \
        \       int x2_j = topRight[j][0];\n        int y2_j = topRight[j][1];\n\n \
        \       int intersect_x1 = x1_i > x1_j ? x1_i : x1_j;\n        int intersect_y1\
        \ = y1_i > y1_j ? y1_i : y1_j;\n        int intersect_x2 = x2_i < x2_j ? x2_i\
        \ : x2_j;\n        int intersect_y2 = y2_i < y2_j ? y2_i : y2_j;\n\n       \
        \ if (intersect_x1 < intersect_x2 && intersect_y1 < intersect_y2) {\n      \
        \    int width = intersect_x2 - intersect_x1;\n          int height = intersect_y2\
        \ - intersect_y1;\n          int currentSide = width < height ? width : height;\n\
        \          if (currentSide > maxSide) {\n            maxSide = currentSide;\n\
        \          }\n        }\n      }\n    }\n    return maxSide * maxSide;\n  }\n\
        }"
      go: "func largestSquareArea(bottomLeft [][]int, topRight [][]int) int64 {\n  \
        \  var maxSide int64 = 0\n    n := len(bottomLeft)\n\n    for i := 0; i < n;\
        \ i++ {\n        for j := i + 1; j < n; j++ {\n            x1_i, y1_i := bottomLeft[i][0],\
        \ bottomLeft[i][1]\n            x2_i, y2_i := topRight[i][0], topRight[i][1]\n\
        \n            x1_j, y1_j := bottomLeft[j][0], bottomLeft[j][1]\n           \
        \ x2_j, y2_j := topRight[j][0], topRight[j][1]\n\n            intersect_x1 :=\
        \ x1_i\n            if x1_j > intersect_x1 {\n                intersect_x1 =\
        \ x1_j\n            }\n            intersect_y1 := y1_i\n            if y1_j\
        \ > intersect_y1 {\n                intersect_y1 = y1_j\n            }\n\n \
        \           intersect_x2 := x2_i\n            if x2_j < intersect_x2 {\n   \
        \             intersect_x2 = x2_j\n            }\n            intersect_y2 :=\
        \ y2_i\n            if y2_j < intersect_y2 {\n                intersect_y2 =\
        \ y2_j\n            }\n\n            if intersect_x1 < intersect_x2 && intersect_y1\
        \ < intersect_y2 {\n                width := int64(intersect_x2 - intersect_x1)\n\
        \                height := int64(intersect_y2 - intersect_y1)\n            \
        \    currentSide := width\n                if height < currentSide {\n     \
        \               currentSide = height\n                }\n                if\
        \ currentSide > maxSide {\n                    maxSide = currentSide\n     \
        \           }\n            }\n        }\n    }\n    return maxSide * maxSide\n\
        }"
      ruby: "# @param {Integer[][]} bottom_left\n# @param {Integer[][]} top_right\n\
        # @return {Integer}\ndef largest_square_area(bottom_left, top_right)\n    max_side\
        \ = 0\n    n = bottom_left.length\n\n    (0...n).each do |i|\n        (i + 1...n).each\
        \ do |j|\n            x1_i, y1_i = bottom_left[i][0], bottom_left[i][1]\n  \
        \          x2_i, y2_i = top_right[i][0], top_right[i][1]\n\n            x1_j,\
        \ y1_j = bottom_left[j][0], bottom_left[j][1]\n            x2_j, y2_j = top_right[j][0],\
        \ top_right[j][1]\n\n            intersect_x1 = [x1_i, x1_j].max\n         \
        \   intersect_y1 = [y1_i, y1_j].max\n            intersect_x2 = [x2_i, x2_j].min\n\
        \            intersect_y2 = [y2_i, y2_j].min\n\n            if intersect_x1\
        \ < intersect_x2 && intersect_y1 < intersect_y2\n                width = intersect_x2\
        \ - intersect_x1\n                height = intersect_y2 - intersect_y1\n   \
        \             current_side = [width, height].min\n                max_side =\
        \ [max_side, current_side].max\n            end\n        end\n    end\n    max_side\
        \ * max_side\nend"
      scala: "object Solution {\n    def largestSquareArea(bottomLeft: Array[Array[Int]],\
        \ topRight: Array[Array[Int]]): Long = {\n        var maxSide: Long = 0\n  \
        \      val n = bottomLeft.length\n\n        for (i <- 0 until n) {\n       \
        \     for (j <- i + 1 until n) {\n                val x1_i = bottomLeft(i)(0)\n\
        \                val y1_i = bottomLeft(i)(1)\n                val x2_i = topRight(i)(0)\n\
        \                val y2_i = topRight(i)(1)\n\n                val x1_j = bottomLeft(j)(0)\n\
        \                val y1_j = bottomLeft(j)(1)\n                val x2_j = topRight(j)(0)\n\
        \                val y2_j = topRight(j)(1)\n\n                val intersect_x1\
        \ = math.max(x1_i, x1_j)\n                val intersect_y1 = math.max(y1_i,\
        \ y1_j)\n                val intersect_x2 = math.min(x2_i, x2_j)\n         \
        \       val intersect_y2 = math.min(y2_i, y2_j)\n\n                if (intersect_x1\
        \ < intersect_x2 && intersect_y1 < intersect_y2) {\n                    val\
        \ width = (intersect_x2 - intersect_x1).toLong\n                    val height\
        \ = (intersect_y2 - intersect_y1).toLong\n                    val currentSide\
        \ = math.min(width, height)\n                    maxSide = math.max(maxSide,\
        \ currentSide)\n                }\n            }\n        }\n        maxSide\
        \ * maxSide\n    }\n}"
      rust: "impl Solution {\n    pub fn largest_square_area(bottom_left: Vec<Vec<i32>>,\
        \ top_right: Vec<Vec<i32>>) -> i64 {\n        let mut max_side: i64 = 0;\n \
        \       let n = bottom_left.len();\n\n        for i in 0..n {\n            for\
        \ j in (i + 1)..n {\n                let x1_i = bottom_left[i][0];\n       \
        \         let y1_i = bottom_left[i][1];\n                let x2_i = top_right[i][0];\n\
        \                let y2_i = top_right[i][1];\n\n                let x1_j = bottom_left[j][0];\n\
        \                let y1_j = bottom_left[j][1];\n                let x2_j = top_right[j][0];\n\
        \                let y2_j = top_right[j][1];\n\n                let intersect_x1\
        \ = x1_i.max(x1_j);\n                let intersect_y1 = y1_i.max(y1_j);\n  \
        \              let intersect_x2 = x2_i.min(x2_j);\n                let intersect_y2\
        \ = y2_i.min(y2_j);\n\n                if intersect_x1 < intersect_x2 && intersect_y1\
        \ < intersect_y2 {\n                    let width = (intersect_x2 - intersect_x1)\
        \ as i64;\n                    let height = (intersect_y2 - intersect_y1) as\
        \ i64;\n                    let current_side = width.min(height);\n        \
        \            max_side = max_side.max(current_side);\n                }\n   \
        \         }\n        }\n        max_side * max_side\n    }\n}"
      racket: "(define/contract (largest-square-area bottomLeft topRight)\n  (-> (listof\
        \ (listof exact-integer?)) (listof (listof exact-integer?)) exact-integer?)\n\
        \  (let* ([n (length bottomLeft)]\n         [max-side 0])\n    (for* ([i (range\
        \ n)]\n           [j (range (+ i 1) n)])\n      (let* ([rect-i-bl (list-ref\
        \ bottomLeft i)]\n             [rect-i-tr (list-ref topRight i)]\n         \
        \    [x1-i (list-ref rect-i-bl 0)]\n             [y1-i (list-ref rect-i-bl 1)]\n\
        \             [x2-i (list-ref rect-i-tr 0)]\n             [y2-i (list-ref rect-i-tr\
        \ 1)]\n\n             [rect-j-bl (list-ref bottomLeft j)]\n             [rect-j-tr\
        \ (list-ref topRight j)]\n             [x1-j (list-ref rect-j-bl 0)]\n     \
        \        [y1-j (list-ref rect-j-bl 1)]\n             [x2-j (list-ref rect-j-tr\
        \ 0)]\n             [y2-j (list-ref rect-j-tr 1)]\n\n             [intersect-x1\
        \ (max x1-i x1-j)]\n             [intersect-y1 (max y1-i y1-j)]\n          \
        \   [intersect-x2 (min x2-i x2-j)]\n             [intersect-y2 (min y2-i y2-j)])\n\
        \        (when (and (< intersect-x1 intersect-x2)\n                   (< intersect-y1\
        \ intersect-y2))\n          (let* ([width (- intersect-x2 intersect-x1)]\n \
        \                [height (- intersect-y2 intersect-y1)]\n                 [current-side\
        \ (min width height)])\n            (set! max-side (max max-side current-side))))))\n\
        \    (* max-side max-side)))"
      erlang: "-spec largest_square_area(BottomLeft :: [[integer()]], TopRight :: [[integer()]])\
        \ -> integer().\nlargest_square_area(BottomLeft, TopRight) ->\n    N = length(BottomLeft),\n\
        \    BottomLeftArray = array:from_list(BottomLeft),\n    TopRightArray = array:from_list(TopRight),\n\
        \    largest_square_area_loop(0, N, BottomLeftArray, TopRightArray, 0).\n\n\
        largest_square_area_loop(I, N, BottomLeftArray, TopRightArray, MaxSide) when\
        \ I < N ->\n    largest_square_area_inner_loop(I, I + 1, N, BottomLeftArray,\
        \ TopRightArray, MaxSide);\nlargest_square_area_loop(N, N, _BottomLeftArray,\
        \ _TopRightArray, MaxSide) ->\n    MaxSide * MaxSide.\n\nlargest_square_area_inner_loop(I,\
        \ J, N, BottomLeftArray, TopRightArray, MaxSide) when J < N ->\n    [X1_i, Y1_i]\
        \ = array:get(I, BottomLeftArray),\n    [X2_i, Y2_i] = array:get(I, TopRightArray),\n\
        \n    [X1_j, Y1_j] = array:get(J, BottomLeftArray),\n    [X2_j, Y2_j] = array:get(J,\
        \ TopRightArray),\n\n    IntersectX1 = max(X1_i, X1_j),\n    IntersectY1 = max(Y1_i,\
        \ Y1_j),\n    IntersectX2 = min(X2_i, X2_j),\n    IntersectY2 = min(Y2_i, Y2_j),\n\
        \n    NewMaxSide =\n        if\n            IntersectX1 < IntersectX2 andalso\
        \ IntersectY1 < IntersectY2 ->\n                Width = IntersectX2 - IntersectX1,\n\
        \                Height = IntersectY2 - IntersectY1,\n                CurrentSide\
        \ = min(Width, Height),\n                max(MaxSide, CurrentSide);\n      \
        \      true ->\n                MaxSide\n        end,\n    largest_square_area_inner_loop(I,\
        \ J + 1, N, BottomLeftArray, TopRightArray, NewMaxSide);\nlargest_square_area_inner_loop(I,\
        \ N, N, BottomLeftArray, TopRightArray, MaxSide) ->\n    largest_square_area_loop(I\
        \ + 1, N, BottomLeftArray, TopRightArray, MaxSide)."
      elixir: "defmodule Solution do\n  @spec largest_square_area(bottom_left :: [[integer]],\
        \ top_right :: [[integer]]) :: integer\n  def largest_square_area(bottom_left,\
        \ top_right) do\n    n = length(bottom_left)\n\n    bottom_left_map = Enum.with_index(bottom_left)\
        \ |> Map.new(fn {rect, idx} -> {idx, rect} end)\n    top_right_map = Enum.with_index(top_right)\
        \ |> Map.new(fn {rect, idx} -> {idx, rect} end)\n\n    max_side = \n      for\
        \ i <- 0..(n - 1),\n          j <- (i + 1)..(n - 1),\n          reduce: 0 do\n\
        \        acc_max_side ->\n          [x1_i, y1_i] = Map.fetch!(bottom_left_map,\
        \ i)\n          [x2_i, y2_i] = Map.fetch!(top_right_map, i)\n\n          [x1_j,\
        \ y1_j] = Map.fetch!(bottom_left_map, j)\n          [x2_j, y2_j] = Map.fetch!(top_right_map,\
        \ j)\n\n          intersect_x1 = max(x1_i, x1_j)\n          intersect_y1 = max(y1_i,\
        \ y1_j)\n          intersect_x2 = min(x2_i, x2_j)\n          intersect_y2 =\
        \ min(y2_i, y2_j)\n\n          if intersect_x1 < intersect_x2 && intersect_y1\
        \ < intersect_y2 do\n            width = intersect_x2 - intersect_x1\n     \
        \       height = intersect_y2 - intersect_y1\n            current_side = min(width,\
        \ height)\n            max(acc_max_side, current_side)\n          else\n   \
        \         acc_max_side\n          end\n      end\n\n    max_side * max_side\n\
        \  end\nend"
    approach: 'The problem requires finding the maximum area of a square that can fit
      within the intersecting region of at least two rectangles. A straightforward approach
      is to iterate through all unique pairs of rectangles. For each pair, we calculate
      their intersection. If two rectangles R1 (defined by bottom-left (x1_bl, y1_bl)
      and top-right (x1_tr, y1_tr)) and R2 (defined by (x2_bl, y2_bl) and (x2_tr, y2_tr))
      intersect, their intersection forms a new rectangle. The bottom-left corner of
      this intersection rectangle is (max(x1_bl, x2_bl), max(y1_bl, y2_bl)), and its
      top-right corner is (min(x1_tr, x2_tr), min(y1_tr, y2_tr)).


      After determining the intersection rectangle''s coordinates, we check if it''s
      a valid, non-empty region (i.e., its calculated bottom-left x-coordinate is less
      than its top-right x-coordinate, and similarly for y-coordinates). If it is valid,
      we calculate its width and height. The largest square that can fit inside this
      intersection rectangle will have a side length equal to the minimum of its width
      and height. We keep track of the maximum such side length found across all pairs.
      Finally, the result is the square of this maximum side length, representing the
      maximum possible square area.'
    time_complexity: The time complexity is O(N^2), where N is the number of rectangles.
      This is because we iterate through all unique pairs of rectangles. There are N
      * (N - 1) / 2 such pairs. For each pair, calculating the intersection and its
      dimensions involves a constant number of comparisons and arithmetic operations.
      For languages like Erlang and Elixir, where list indexing (e.g., `lists:nth` or
      `Enum.at`) is O(N), an initial conversion to an array or map for O(1) access is
      performed, adding an O(N) overhead, but keeping the overall pair-wise processing
      at O(N^2).
    space_complexity: The space complexity is O(1) for most languages, as we only store
      a few variables to track the maximum side length and temporary intersection coordinates.
      For Erlang and Elixir, if the input lists are converted to arrays or maps for
      O(1) access, this conversion adds O(N) space complexity to store these auxiliary
      data structures. However, this is typically considered part of the input processing
      and not additional space for the core algorithm logic itself, or it's within acceptable
      limits for the problem's constraints.
    elapsed_time: 122.0866162776947
    model: gemini-2.5-flash
    generated_at: '2026-01-17 01:08:58 '
  - solutions:
      cpp: "class Solution {\npublic:\n    long long largestSquareArea(vector<vector<int>>&\
        \ bottomLeft, vector<vector<int>>& topRight) {\n        long long maxArea =\
        \ 0;\n        for (int i = 0; i < bottomLeft.size(); i++) {\n            for\
        \ (int j = i + 1; j < bottomLeft.size(); j++) {\n                int x1 = max(bottomLeft[i][0],\
        \ bottomLeft[j][0]);\n                int y1 = max(bottomLeft[i][1], bottomLeft[j][1]);\n\
        \                int x2 = min(topRight[i][0], topRight[j][0]);\n           \
        \     int y2 = min(topRight[i][1], topRight[j][1]);\n                if (x1\
        \ < x2 && y1 < y2) {\n                    int side = min(x2 - x1, y2 - y1);\n\
        \                    maxArea = max(maxArea, (long long)side * side);\n     \
        \           }\n            }\n        }\n        return maxArea;\n    }\n};"
      java: "class Solution {\n    public long largestSquareArea(int[][] bottomLeft,\
        \ int[][] topRight) {\n        long maxArea = 0;\n        for (int i = 0; i\
        \ < bottomLeft.length; i++) {\n            for (int j = i + 1; j < bottomLeft.length;\
        \ j++) {\n                int x1 = Math.max(bottomLeft[i][0], bottomLeft[j][0]);\n\
        \                int y1 = Math.max(bottomLeft[i][1], bottomLeft[j][1]);\n  \
        \              int x2 = Math.min(topRight[i][0], topRight[j][0]);\n        \
        \        int y2 = Math.min(topRight[i][1], topRight[j][1]);\n              \
        \  if (x1 < x2 && y1 < y2) {\n                    int side = Math.min(x2 - x1,\
        \ y2 - y1);\n                    maxArea = Math.max(maxArea, (long)side * side);\n\
        \                }\n            }\n        }\n        return maxArea;\n    }\n\
        }"
      python: "class Solution(object):\n    def largestSquareArea(self, bottomLeft,\
        \ topRight):\n        maxArea = 0\n        for i in range(len(bottomLeft)):\n\
        \            for j in range(i + 1, len(bottomLeft)):\n                x1 = max(bottomLeft[i][0],\
        \ bottomLeft[j][0])\n                y1 = max(bottomLeft[i][1], bottomLeft[j][1])\n\
        \                x2 = min(topRight[i][0], topRight[j][0])\n                y2\
        \ = min(topRight[i][1], topRight[j][1])\n                if x1 < x2 and y1 <\
        \ y2:\n                    side = min(x2 - x1, y2 - y1)\n                  \
        \  maxArea = max(maxArea, side * side)\n        return maxArea"
      python3: "class Solution:\n    def largestSquareArea(self, bottomLeft: list[list[int]],\
        \ topRight: list[list[int]]) -> int:\n        maxArea = 0\n        for i in\
        \ range(len(bottomLeft)):\n            for j in range(i + 1, len(bottomLeft)):\n\
        \                x1 = max(bottomLeft[i][0], bottomLeft[j][0])\n            \
        \    y1 = max(bottomLeft[i][1], bottomLeft[j][1])\n                x2 = min(topRight[i][0],\
        \ topRight[j][0])\n                y2 = min(topRight[i][1], topRight[j][1])\n\
        \                if x1 < x2 and y1 < y2:\n                    side = min(x2\
        \ - x1, y2 - y1)\n                    maxArea = max(maxArea, side * side)\n\
        \        return maxArea"
      c: "long long largestSquareArea(int** bottomLeft, int bottomLeftSize, int* bottomLeftColSize,\
        \ int** topRight, int topRightSize, int* topRightColSize) {\n    long long maxArea\
        \ = 0;\n    for (int i = 0; i < bottomLeftSize; i++) {\n        for (int j =\
        \ i + 1; j < bottomLeftSize; j++) {\n            int x1 = (bottomLeft[i][0]\
        \ > bottomLeft[j][0]) ? bottomLeft[i][0] : bottomLeft[j][0];\n            int\
        \ y1 = (bottomLeft[i][1] > bottomLeft[j][1]) ? bottomLeft[i][1] : bottomLeft[j][1];\n\
        \            int x2 = (topRight[i][0] < topRight[j][0]) ? topRight[i][0] : topRight[j][0];\n\
        \            int y2 = (topRight[i][1] < topRight[j][1]) ? topRight[i][1] : topRight[j][1];\n\
        \            if (x1 < x2 && y1 < y2) {\n                int side = (x2 - x1\
        \ < y2 - y1) ? x2 - x1 : y2 - y1;\n                maxArea = (maxArea > side\
        \ * side) ? maxArea : side * side;\n            }\n        }\n    }\n    return\
        \ maxArea;\n}"
      csharp: "public class Solution {\n    public long LargestSquareArea(int[][] bottomLeft,\
        \ int[][] topRight) {\n        long maxArea = 0;\n        for (int i = 0; i\
        \ < bottomLeft.Length; i++) {\n            for (int j = i + 1; j < bottomLeft.Length;\
        \ j++) {\n                int x1 = Math.Max(bottomLeft[i][0], bottomLeft[j][0]);\n\
        \                int y1 = Math.Max(bottomLeft[i][1], bottomLeft[j][1]);\n  \
        \              int x2 = Math.Min(topRight[i][0], topRight[j][0]);\n        \
        \        int y2 = Math.Min(topRight[i][1], topRight[j][1]);\n              \
        \  if (x1 < x2 && y1 < y2) {\n                    int side = Math.Min(x2 - x1,\
        \ y2 - y1);\n                    maxArea = Math.Max(maxArea, (long)side * side);\n\
        \                }\n            }\n        }\n        return maxArea;\n    }\n\
        }"
      javascript: "var largestSquareArea = function(bottomLeft, topRight) {\n    let\
        \ maxArea = 0;\n    for (let i = 0; i < bottomLeft.length; i++) {\n        for\
        \ (let j = i + 1; j < bottomLeft.length; j++) {\n            let x1 = Math.max(bottomLeft[i][0],\
        \ bottomLeft[j][0]);\n            let y1 = Math.max(bottomLeft[i][1], bottomLeft[j][1]);\n\
        \            let x2 = Math.min(topRight[i][0], topRight[j][0]);\n          \
        \  let y2 = Math.min(topRight[i][1], topRight[j][1]);\n            if (x1 <\
        \ x2 && y1 < y2) {\n                let side = Math.min(x2 - x1, y2 - y1);\n\
        \                maxArea = Math.max(maxArea, side * side);\n            }\n\
        \        }\n    }\n    return maxArea;\n};"
      typescript: "function largestSquareArea(bottomLeft: number[][], topRight: number[][]):\
        \ number {\n    let maxArea = 0;\n    for (let i = 0; i < bottomLeft.length;\
        \ i++) {\n        for (let j = i + 1; j < bottomLeft.length; j++) {\n      \
        \      let x1 = Math.max(bottomLeft[i][0], bottomLeft[j][0]);\n            let\
        \ y1 = Math.max(bottomLeft[i][1], bottomLeft[j][1]);\n            let x2 = Math.min(topRight[i][0],\
        \ topRight[j][0]);\n            let y2 = Math.min(topRight[i][1], topRight[j][1]);\n\
        \            if (x1 < x2 && y1 < y2) {\n                let side = Math.min(x2\
        \ - x1, y2 - y1);\n                maxArea = Math.max(maxArea, side * side);\n\
        \            }\n        }\n    }\n    return maxArea;\n}"
      php: "class Solution {\n    function largestSquareArea($bottomLeft, $topRight)\
        \ {\n        $maxArea = 0;\n        for ($i = 0; $i < count($bottomLeft); $i++)\
        \ {\n            for ($j = $i + 1; $j < count($bottomLeft); $j++) {\n      \
        \          $x1 = max($bottomLeft[$i][0], $bottomLeft[$j][0]);\n            \
        \    $y1 = max($bottomLeft[$i][1], $bottomLeft[$j][1]);\n                $x2\
        \ = min($topRight[$i][0], $topRight[$j][0]);\n                $y2 = min($topRight[$i][1],\
        \ $topRight[$j][1]);\n                if ($x1 < $x2 && $y1 < $y2) {\n      \
        \              $side = min($x2 - $x1, $y2 - $y1);\n                    $maxArea\
        \ = max($maxArea, $side * $side);\n                }\n            }\n      \
        \  }\n        return $maxArea;\n    }\n}"
      swift: "class Solution {\n    func largestSquareArea(_ bottomLeft: [[Int]], _\
        \ topRight: [[Int]]) -> Int {\n        var maxArea = 0\n        for i in 0..<bottomLeft.count\
        \ {\n            for j in i + 1..<bottomLeft.count {\n                let x1\
        \ = max(bottomLeft[i][0], bottomLeft[j][0])\n                let y1 = max(bottomLeft[i][1],\
        \ bottomLeft[j][1])\n                let x2 = min(topRight[i][0], topRight[j][0])\n\
        \                let y2 = min(topRight[i][1], topRight[j][1])\n            \
        \    if x1 < x2 && y1 < y2 {\n                    let side = min(x2 - x1, y2\
        \ - y1)\n                    maxArea = max(maxArea, side * side)\n         \
        \       }\n            }\n        }\n        return maxArea\n    }\n}"
      kotlin: "class Solution {\n    fun largestSquareArea(bottomLeft: Array<IntArray>,\
        \ topRight: Array<IntArray>): Long {\n        var maxArea = 0L\n        for\
        \ (i in bottomLeft.indices) {\n            for (j in i + 1 until bottomLeft.size)\
        \ {\n                val x1 = maxOf(bottomLeft[i][0], bottomLeft[j][0])\n  \
        \              val y1 = maxOf(bottomLeft[i][1], bottomLeft[j][1])\n        \
        \        val x2 = minOf(topRight[i][0], topRight[j][0])\n                val\
        \ y2 = minOf(topRight[i][1], topRight[j][1])\n                if (x1 < x2 &&\
        \ y1 < y2) {\n                    val side = minOf(x2 - x1, y2 - y1)\n     \
        \               maxArea = maxOf(maxArea, side.toLong() * side)\n           \
        \     }\n            }\n        }\n        return maxArea\n    }\n}"
      dart: "class Solution {\n  int largestSquareArea(List<List<int>> bottomLeft, List<List<int>>\
        \ topRight) {\n    int maxArea = 0;\n    for (int i = 0; i < bottomLeft.length;\
        \ i++) {\n      for (int j = i + 1; j < bottomLeft.length; j++) {\n        int\
        \ x1 = bottomLeft[i][0] > bottomLeft[j][0] ? bottomLeft[i][0] : bottomLeft[j][0];\n\
        \        int y1 = bottomLeft[i][1] > bottomLeft[j][1] ? bottomLeft[i][1] : bottomLeft[j][1];\n\
        \        int x2 = topRight[i][0] < topRight[j][0] ? topRight[i][0] : topRight[j][0];\n\
        \        int y2 = topRight[i][1] < topRight[j][1] ? topRight[i][1] : topRight[j][1];\n\
        \        if (x1 < x2 && y1 < y2) {\n          int side = x2 - x1 < y2 - y1 ?\
        \ x2 - x1 : y2 - y1;\n          maxArea = maxArea > side * side ? maxArea :\
        \ side * side;\n        }\n      }\n    }\n    return maxArea;\n  }\n}"
      go: "func largestSquareArea(bottomLeft [][]int, topRight [][]int) int64 {\n  \
        \  maxArea := int64(0)\n    for i := 0; i < len(bottomLeft); i++ {\n       \
        \ for j := i + 1; j < len(bottomLeft); j++ {\n            x1 := max(bottomLeft[i][0],\
        \ bottomLeft[j][0])\n            y1 := max(bottomLeft[i][1], bottomLeft[j][1])\n\
        \            x2 := min(topRight[i][0], topRight[j][0])\n            y2 := min(topRight[i][1],\
        \ topRight[j][1])\n            if x1 < x2 && y1 < y2 {\n                side\
        \ := min(x2-x1, y2-y1)\n                if int64(side)*int64(side) > maxArea\
        \ {\n                    maxArea = int64(side) * int64(side)\n             \
        \   }\n            }\n        }\n    }\n    return maxArea\n}\nfunc max(a, b\
        \ int) int {\n    if a > b {\n        return a\n    }\n    return b\n}\nfunc\
        \ min(a, b int) int {\n    if a < b {\n        return a\n    }\n    return b\n\
        }"
      ruby: "def largest_square_area(bottom_left, top_right)\n    max_area = 0\n   \
        \ (0...bottom_left.size).each do |i|\n        (i + 1...bottom_left.size).each\
        \ do |j|\n            x1 = [bottom_left[i][0], bottom_left[j][0]].max\n    \
        \        y1 = [bottom_left[i][1], bottom_left[j][1]].max\n            x2 = [top_right[i][0],\
        \ top_right[j][0]].min\n            y2 = [top_right[i][1], top_right[j][1]].min\n\
        \            if x1 < x2 && y1 < y2\n                side = [x2 - x1, y2 - y1].min\n\
        \                max_area = [max_area, side * side].max\n            end\n \
        \       end\n    end\n    max_area\nend"
      scala: "object Solution {\n    def largestSquareArea(bottomLeft: Array[Array[Int]],\
        \ topRight: Array[Array[Int]]): Long = {\n        var maxArea = 0L\n       \
        \ for (i <- bottomLeft.indices) {\n            for (j <- i + 1 until bottomLeft.length)\
        \ {\n                val x1 = math.max(bottomLeft(i)(0), bottomLeft(j)(0))\n\
        \                val y1 = math.max(bottomLeft(i)(1), bottomLeft(j)(1))\n   \
        \             val x2 = math.min(topRight(i)(0), topRight(j)(0))\n          \
        \      val y2 = math.min(topRight(i)(1), topRight(j)(1))\n                if\
        \ (x1 < x2 && y1 < y2) {\n                    val side = math.min(x2 - x1, y2\
        \ - y1)\n                    maxArea = math.max(maxArea, side.toLong * side)\n\
        \                }\n            }\n        }\n        maxArea\n    }\n}"
      rust: "impl Solution {\n    pub fn largest_square_area(bottom_left: Vec<Vec<i32>>,\
        \ top_right: Vec<Vec<i32>>) -> i64 {\n        let mut max_area = 0;\n      \
        \  for i in 0..bottom_left.len() {\n            for j in i + 1..bottom_left.len()\
        \ {\n                let x1 = bottom_left[i][0].max(bottom_left[j][0]);\n  \
        \              let y1 = bottom_left[i][1].max(bottom_left[j][1]);\n        \
        \        let x2 = top_right[i][0].min(top_right[j][0]);\n                let\
        \ y2 = top_right[i][1].min(top_right[j][1]);\n                if x1 < x2 &&\
        \ y1 < y2 {\n                    let side = (x2 - x1).min(y2 - y1);\n      \
        \              max_area = max_area.max((side as i64) * (side as i64));\n   \
        \             }\n            }\n        }\n        max_area as i64\n    }\n}"
      racket: "(define/contract (largest-square-area bottomLeft topRight)\n  (-> (listof\
        \ (listof exact-integer?)) (listof (listof exact-integer?)) exact-integer?)\n\
        \  (let loop ([i 0]\n             [max-area 0])\n    (if (= i (length bottomLeft))\n\
        \        max-area\n        (let loop2 ([j (add1 i)]\n                   [max-area\
        \ max-area])\n          (if (= j (length bottomLeft))\n              (loop (add1\
        \ i) max-area)\n              (let* ([x1 (max (list-ref (list-ref bottomLeft\
        \ i) 0) (list-ref (list-ref bottomLeft j) 0))]\n                     [y1 (max\
        \ (list-ref (list-ref bottomLeft i) 1) (list-ref (list-ref bottomLeft j) 1))]\n\
        \                     [x2 (min (list-ref (list-ref topRight i) 0) (list-ref\
        \ (list-ref topRight j) 0))]\n                     [y2 (min (list-ref (list-ref\
        \ topRight i) 1) (list-ref (list-ref topRight j) 1))]\n                    \
        \ [side (min (- x2 x1) (- y2 y1))])\n                (if (and (< x1 x2) (< y1\
        \ y2))\n                    (loop2 (add1 j) (max max-area (* side side)))\n\
        \                    (loop2 (add1 j) max-area))))))))"
      erlang: "-module(solution).\n-export([largest_square_area/2]).\n\nlargest_square_area(BottomLeft,\
        \ TopRight) ->\n    lists:foldl(\n      fun({I, MaxArea}, {BottomLeftI, TopRightI})\
        \ ->\n              lists:foldl(\n                fun({J, MaxArea1}, {BottomLeftJ,\
        \ TopRightJ}) ->\n                        X1 = max(lists:nth(1, BottomLeftI),\
        \ lists:nth(1, BottomLeftJ)),\n                        Y1 = max(lists:nth(2,\
        \ BottomLeftI), lists:nth(2, BottomLeftJ)),\n                        X2 = min(lists:nth(1,\
        \ TopRightI), lists:nth(1, TopRightJ)),\n                        Y2 = min(lists:nth(2,\
        \ TopRightI), lists:nth(2, TopRightJ)),\n                        Side = min(X2\
        \ - X1, Y2 - Y1),\n                        if\n                          X1\
        \ < X2 andalso Y1 < Y2 ->\n                            {J + 1, max(MaxArea1,\
        \ Side * Side)};\n                          true ->\n                      \
        \      {J + 1, MaxArea1}\n                        end\n                end,\n\
        \                {I + 1, MaxArea},\n                lists:zip(BottomLeft, TopRight)\n\
        \              end,\n              {0, 0},\n              lists:zip(BottomLeft,\
        \ TopRight)\n      end,\n      {0, 0},\n      lists:zip(BottomLeft, TopRight)\n\
        \    )."
      elixir: "defmodule Solution do\n  @spec largest_square_area(bottom_left :: [[integer]],\
        \ top_right :: [[integer]]) :: integer\n  def largest_square_area(bottom_left,\
        \ top_right) do\n    max_area = 0\n    for i <- 0..(length(bottom_left) - 1)\
        \ do\n      for j <- (i + 1)..(length(bottom_left) - 1) do\n        x1 = max(Enum.at(Enum.at(bottom_left,\
        \ i), 0), Enum.at(Enum.at(bottom_left, j), 0))\n        y1 = max(Enum.at(Enum.at(bottom_left,\
        \ i), 1), Enum.at(Enum.at(bottom_left, j), 1))\n        x2 = min(Enum.at(Enum.at(top_right,\
        \ i), 0), Enum.at(Enum.at(top_right, j), 0))\n        y2 = min(Enum.at(Enum.at(top_right,\
        \ i), 1), Enum.at(Enum.at(top_right, j), 1))\n        if x1 < x2 and y1 < y2\
        \ do\n          side = min(x2 - x1, y2 - y1)\n          max_area = max(max_area,\
        \ side * side)\n        end\n      end\n    end\n    max_area\n  end\nend"
    approach: "The problem can be solved by iterating over all pairs of rectangles and\
      \ checking if they intersect. If two rectangles intersect, we calculate the intersection\
      \ area and find the maximum square that can fit inside this area. We keep track\
      \ of the maximum square area found so far. The key intuition is that the intersection\
      \ area of two rectangles is also a rectangle, and the maximum square that can\
      \ fit inside this area will have a side length equal to the minimum of the width\
      \ and height of the intersection area.\n\n  The algorithm works by first defining\
      \ a function to calculate the intersection area of two rectangles. Then, it iterates\
      \ over all pairs of rectangles, calculates their intersection area, and finds\
      \ the maximum square that can fit inside this area. If the maximum square area\
      \ is greater than the current maximum, it updates the maximum area. Finally, it\
      \ returns the maximum square area found."
    time_complexity: The time complexity of the algorithm is O(n^2) where n is the number
      of rectangles. This is because we are iterating over all pairs of rectangles,
      and for each pair, we are calculating the intersection area and finding the maximum
      square that can fit inside this area.
    space_complexity: The space complexity of the algorithm is O(1) as we are not using
      any additional space that scales with the input size. We are only using a constant
      amount of space to store the maximum square area and other variables.
    elapsed_time: 10.836902141571045
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-17 01:09:14 '
---

## Problem #3047: Find the Largest Area of Square Inside Two Rectangles

**Difficulty:** Medium

**Topics:** Array, Math, Geometry

## Problem Description

<p>There exist <code>n</code> rectangles in a 2D plane with edges parallel to the x and y axis. You are given two 2D integer arrays&nbsp;<code>bottomLeft</code> and <code>topRight</code>&nbsp;where <code>bottomLeft[i] = [a_i, b_i]</code> and <code>topRight[i] = [c_i, d_i]</code> represent&nbsp;the <strong>bottom-left</strong> and <strong>top-right</strong> coordinates of the <code>i<sup>th</sup></code> rectangle, respectively.</p>

<p>You need to find the <strong>maximum</strong> area of a <strong>square</strong> that can fit inside the intersecting region of at least two rectangles. Return <code>0</code> if such a square does not exist.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/01/05/example12.png" style="width: 443px; height: 364px; padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem;" />
<p><strong>Input:</strong> bottomLeft = [[1,1],[2,2],[3,1]], topRight = [[3,3],[4,4],[6,6]]</p>

<p><strong>Output:</strong> 1</p>

<p><strong>Explanation:</strong></p>

<p>A square with side length 1 can fit inside either the intersecting region of rectangles 0 and 1 or the intersecting region of rectangles 1 and 2. Hence the maximum area is 1. It can be shown that a square with a greater side length can not fit inside any intersecting region of two rectangles.</p>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/07/15/diag.png" style="width: 451px; height: 470px; padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem;" />
<p><strong>Input:</strong> bottomLeft = [[1,1],[1,3],[1,5]], topRight = [[5,5],[5,7],[5,9]]</p>

<p><strong>Output:</strong> 4</p>

<p><strong>Explanation:</strong></p>

<p>A square with side length 2 can fit inside either the intersecting region of rectangles 0 and 1 or the intersecting region of rectangles 1 and 2. Hence the maximum area is <code>2 * 2 = 4</code>. It can be shown that a square with a greater side length can not fit inside any intersecting region of two rectangles.</p>

<p><strong class="example">Example 3:</strong></p>
<code> <img alt="" src="https://assets.leetcode.com/uploads/2024/01/04/rectanglesexample2.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 445px; height: 365px;" /> </code>

<p><strong>Input:</strong> bottomLeft = [[1,1],[2,2],[1,2]], topRight = [[3,3],[4,4],[3,4]]</p>

<p><strong>Output:</strong> 1</p>

<p><strong>Explanation:</strong></p>

<p>A square with side length 1 can fit inside the intersecting region of any two rectangles. Also, no larger square can, so the maximum area is 1. Note that the region can be formed by the intersection of more than 2 rectangles.</p>

<p><strong class="example">Example 4:</strong></p>
<code> <img alt="" src="https://assets.leetcode.com/uploads/2024/01/04/rectanglesexample3.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 444px; height: 364px;" /> </code>

<p><strong>Input:&nbsp;</strong>bottomLeft = [[1,1],[3,3],[3,1]], topRight = [[2,2],[4,4],[4,2]]</p>

<p><strong>Output:</strong> 0</p>

<p><strong>Explanation:</strong></p>

<p>No pair of rectangles intersect, hence, the answer is 0.</p>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == bottomLeft.length == topRight.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>3</sup></code></li>
	<li><code>bottomLeft[i].length == topRight[i].length == 2</code></li>
	<li><code>1 &lt;= bottomLeft[i][0], bottomLeft[i][1] &lt;= 10<sup>7</sup></code></li>
	<li><code>1 &lt;= topRight[i][0], topRight[i][1] &lt;= 10<sup>7</sup></code></li>
	<li><code>bottomLeft[i][0] &lt; topRight[i][0]</code></li>
	<li><code>bottomLeft[i][1] &lt; topRight[i][1]</code></li>
</ul>


## Hints

1. Brute Force the intersection area of each pair of rectangles.

2. Two rectangles will not overlap when the bottom left x coordinate of one rectangle is greater than the top right x coordinate of the other rectangle. The same is true for the y coordinate.

3. The intersection area (if any) is also a rectangle. Find its corners.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2026-01-17 01:08:58 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem requires finding the maximum area of a square that can fit within the intersecting region of at least two rectangles. A straightforward approach is to iterate through all unique pairs of rectangles. For each pair, we calculate their intersection. If two rectangles R1 (defined by bottom-left (x1_bl, y1_bl) and top-right (x1_tr, y1_tr)) and R2 (defined by (x2_bl, y2_bl) and (x2_tr, y2_tr)) intersect, their intersection forms a new rectangle. The bottom-left corner of this intersection rectangle is (max(x1_bl, x2_bl), max(y1_bl, y2_bl)), and its top-right corner is (min(x1_tr, x2_tr), min(y1_tr, y2_tr)).

After determining the intersection rectangle's coordinates, we check if it's a valid, non-empty region (i.e., its calculated bottom-left x-coordinate is less than its top-right x-coordinate, and similarly for y-coordinates). If it is valid, we calculate its width and height. The largest square that can fit inside this intersection rectangle will have a side length equal to the minimum of its width and height. We keep track of the maximum such side length found across all pairs. Finally, the result is the square of this maximum side length, representing the maximum possible square area.

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
long long largestSquareArea(vector<vector<int>>& bottomLeft, vector<vector<int>>& topRight) {
int n = bottomLeft.size();
long long max_side_length = 0;

for (int i = 0; i < n; ++i) {
for (int j = i + 1; j < n; ++j) {
    // Rectangle i: (x1_i, y1_i) to (x2_i, y2_i)
    long long x1_i = bottomLeft[i][0];
    long long y1_i = bottomLeft[i][1];
    long long x2_i = topRight[i][0];
    long long y2_i = topRight[i][1];

    // Rectangle j: (x1_j, y1_j) to (x2_j, y2_j)
    long long x1_j = bottomLeft[j][0];
    long long y1_j = bottomLeft[j][1];
    long long x2_j = topRight[j][0];
    long long y2_j = topRight[j][1];

    // Calculate intersection coordinates
    long long intersect_x_left = max(x1_i, x1_j);
    long long intersect_y_bottom = max(y1_i, y1_j);
    long long intersect_x_right = min(x2_i, x2_j);
    long long intersect_y_top = min(y2_i, y2_j);

    // Check if an intersection exists (positive width and height)
    if (intersect_x_left < intersect_x_right && intersect_y_bottom < intersect_y_top) {
        long long current_width = intersect_x_right - intersect_x_left;
        long long current_height = intersect_y_top - intersect_y_bottom;
        long long current_side = min(current_width, current_height);
        max_side_length = max(max_side_length, current_side);
    }
}
}

return max_side_length * max_side_length;
}
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public long largestSquareArea(int[][] bottomLeft, int[][] topRight) {
        int n = bottomLeft.length;
        long maxSideLength = 0;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                // Rectangle i: (x1_i, y1_i) to (x2_i, y2_i)
                long x1_i = bottomLeft[i][0];
                long y1_i = bottomLeft[i][1];
                long x2_i = topRight[i][0];
                long y2_i = topRight[i][1];

                // Rectangle j: (x1_j, y1_j) to (x2_j, y2_j)
                long x1_j = bottomLeft[j][0];
                long y1_j = bottomLeft[j][1];
                long x2_j = topRight[j][0];
                long y2_j = topRight[j][1];

                // Calculate intersection coordinates
                long intersect_x_left = Math.max(x1_i, x1_j);
                long intersect_y_bottom = Math.max(y1_i, y1_j);
                long intersect_x_right = Math.min(x2_i, x2_j);
                long intersect_y_top = Math.min(y2_i, y2_j);

                // Check if an intersection exists (positive width and height)
                if (intersect_x_left < intersect_x_right && intersect_y_bottom < intersect_y_top) {
                    long current_width = intersect_x_right - intersect_x_left;
                    long current_height = intersect_y_top - intersect_y_bottom;
                    long current_side = Math.min(current_width, current_height);
                    maxSideLength = Math.max(maxSideLength, current_side);
                }
            }
        }

        return maxSideLength * maxSideLength;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def largestSquareArea(self, bottomLeft, topRight):
        """
        :type bottomLeft: List[List[int]]
        :type topRight: List[List[int]]
        :rtype: int
        """
        n = len(bottomLeft)
        max_side_length = 0

        for i in range(n):
            for j in range(i + 1, n):
                # Rectangle i: (x1_i, y1_i) to (x2_i, y2_i)
                x1_i, y1_i = bottomLeft[i][0], bottomLeft[i][1]
                x2_i, y2_i = topRight[i][0], topRight[i][1]

                # Rectangle j: (x1_j, y1_j) to (x2_j, y2_j)
                x1_j, y1_j = bottomLeft[j][0], bottomLeft[j][1]
                x2_j, y2_j = topRight[j][0], topRight[j][1]

                # Calculate intersection coordinates
                intersect_x_left = max(x1_i, x1_j)
                intersect_y_bottom = max(y1_i, y1_j)
                intersect_x_right = min(x2_i, x2_j)
                intersect_y_top = min(y2_i, y2_j)

                # Check if an intersection exists (positive width and height)
                if intersect_x_left < intersect_x_right and intersect_y_bottom < intersect_y_top:
                    current_width = intersect_x_right - intersect_x_left
                    current_height = intersect_y_top - intersect_y_bottom
                    current_side = min(current_width, current_height)
                    max_side_length = max(max_side_length, current_side)

        return max_side_length * max_side_length
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_side_length = 0

        for i in range(n):
            for j in range(i + 1, n):
                # Rectangle i: (x1_i, y1_i) to (x2_i, y2_i)
                x1_i, y1_i = bottomLeft[i][0], bottomLeft[i][1]
                x2_i, y2_i = topRight[i][0], topRight[i][1]

                # Rectangle j: (x1_j, y1_j) to (x2_j, y2_j)
                x1_j, y1_j = bottomLeft[j][0], bottomLeft[j][1]
                x2_j, y2_j = topRight[j][0], topRight[j][1]

                # Calculate intersection coordinates
                intersect_x_left = max(x1_i, x1_j)
                intersect_y_bottom = max(y1_i, y1_j)
                intersect_x_right = min(x2_i, x2_j)
                intersect_y_top = min(y2_i, y2_j)

                # Check if an intersection exists (positive width and height)
                if intersect_x_left < intersect_x_right and intersect_y_bottom < intersect_y_top:
                    current_width = intersect_x_right - intersect_x_left
                    current_height = intersect_y_top - intersect_y_bottom
                    current_side = min(current_width, current_height)
                    max_side_length = max(max_side_length, current_side)

        return max_side_length * max_side_length
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
long long largestSquareArea(int** bottomLeft, int bottomLeftSize, int* bottomLeftColSize, int** topRight, int topRightSize, int* topRightColSize) {
int n = bottomLeftSize;
long long max_side_length = 0;

for (int i = 0; i < n; ++i) {
for (int j = i + 1; j < n; ++j) {
// Rectangle i: (x1_i, y1_i) to (x2_i, y2_i)
long long x1_i = bottomLeft[i][0];
long long y1_i = bottomLeft[i][1];
long long x2_i = topRight[i][0];
long long y2_i = topRight[i][1];

// Rectangle j: (x1_j, y1_j) to (x2_j, y2_j)
long long x1_j = bottomLeft[j][0];
long long y1_j = bottomLeft[j][1];
long long x2_j = topRight[j][0];
long long y2_j = topRight[j][1];

// Calculate intersection coordinates
long long intersect_x_left = (x1_i > x1_j) ? x1_i : x1_j; // max
long long intersect_y_bottom = (y1_i > y1_j) ? y1_i : y1_j; // max
long long intersect_x_right = (x2_i < x2_j) ? x2_i : x2_j; // min
long long intersect_y_top = (y2_i < y2_j) ? y2_i : y2_j; // min

// Check if an intersection exists (positive width and height)
if (intersect_x_left < intersect_x_right && intersect_y_bottom < intersect_y_top) {
    long long current_width = intersect_x_right - intersect_x_left;
    long long current_height = intersect_y_top - intersect_y_bottom;
    long long current_side = (current_width < current_height) ? current_width : current_height; // min
    max_side_length = (max_side_length > current_side) ? max_side_length : current_side; // max
}
}
}

return max_side_length * max_side_length;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public long LargestSquareArea(int[][] bottomLeft, int[][] topRight) {
        int n = bottomLeft.Length;
        long maxSideLength = 0;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                // Rectangle i: (x1_i, y1_i) to (x2_i, y2_i)
                long x1_i = bottomLeft[i][0];
                long y1_i = bottomLeft[i][1];
                long x2_i = topRight[i][0];
                long y2_i = topRight[i][1];

                // Rectangle j: (x1_j, y1_j) to (x2_j, y2_j)
                long x1_j = bottomLeft[j][0];
                long y1_j = bottomLeft[j][1];
                long x2_j = topRight[j][0];
                long y2_j = topRight[j][1];

                // Calculate intersection coordinates
                long intersect_x_left = Math.Max(x1_i, x1_j);
                long intersect_y_bottom = Math.Max(y1_i, y1_j);
                long intersect_x_right = Math.Min(x2_i, x2_j);
                long intersect_y_top = Math.Min(y2_i, y2_j);

                // Check if an intersection exists (positive width and height)
                if (intersect_x_left < intersect_x_right && intersect_y_bottom < intersect_y_top) {
                    long current_width = intersect_x_right - intersect_x_left;
                    long current_height = intersect_y_top - intersect_y_bottom;
                    long current_side = Math.Min(current_width, current_height);
                    maxSideLength = Math.Max(maxSideLength, current_side);
                }
            }
        }

        return maxSideLength * maxSideLength;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[][]} bottomLeft
 * @param {number[][]} topRight
 * @return {number}
 */
var largestSquareArea = function(bottomLeft, topRight) {
    const n = bottomLeft.length;
    let maxSideLength = 0;

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            // Rectangle i: (x1_i, y1_i) to (x2_i, y2_i)
            const x1_i = bottomLeft[i][0];
            const y1_i = bottomLeft[i][1];
            const x2_i = topRight[i][0];
            const y2_i = topRight[i][1];

            // Rectangle j: (x1_j, y1_j) to (x2_j, y2_j)
            const x1_j = bottomLeft[j][0];
            const y1_j = bottomLeft[j][1];
            const x2_j = topRight[j][0];
            const y2_j = topRight[j][1];

            // Calculate intersection coordinates
            const intersect_x_left = Math.max(x1_i, x1_j);
            const intersect_y_bottom = Math.max(y1_i, y1_j);
            const intersect_x_right = Math.min(x2_i, x2_j);
            const intersect_y_top = Math.min(y2_i, y2_j);

            // Check if an intersection exists (positive width and height)
            if (intersect_x_left < intersect_x_right && intersect_y_bottom < intersect_y_top) {
                const current_width = intersect_x_right - intersect_x_left;
                const current_height = intersect_y_top - intersect_y_bottom;
                const current_side = Math.min(current_width, current_height);
                maxSideLength = Math.max(maxSideLength, current_side);
            }
        }
    }

    return maxSideLength * maxSideLength;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function largestSquareArea(bottomLeft: number[][], topRight: number[][]): number {
    const n = bottomLeft.length;
    let maxSideLength = 0;

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            // Rectangle i: (x1_i, y1_i) to (x2_i, y2_i)
            const x1_i = bottomLeft[i][0];
            const y1_i = bottomLeft[i][1];
            const x2_i = topRight[i][0];
            const y2_i = topRight[i][1];

            // Rectangle j: (x1_j, y1_j) to (x2_j, y2_j)
            const x1_j = bottomLeft[j][0];
            const y1_j = bottomLeft[j][1];
            const x2_j = topRight[j][0];
            const y2_j = topRight[j][1];

            // Calculate intersection coordinates
            const intersect_x_left = Math.max(x1_i, x1_j);
            const intersect_y_bottom = Math.max(y1_i, y1_j);
            const intersect_x_right = Math.min(x2_i, x2_j);
            const intersect_y_top = Math.min(y2_i, y2_j);

            // Check if an intersection exists (positive width and height)
            if (intersect_x_left < intersect_x_right && intersect_y_bottom < intersect_y_top) {
                const current_width = intersect_x_right - intersect_x_left;
                const current_height = intersect_y_top - intersect_y_bottom;
                const current_side = Math.min(current_width, current_height);
                maxSideLength = Math.max(maxSideLength, current_side);
            }
        }
    }

    return maxSideLength * maxSideLength;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[][] $bottomLeft
     * @param Integer[][] $topRight
     * @return Integer
     */
    function largestSquareArea($bottomLeft, $topRight) {
        $n = count($bottomLeft);
        $maxSideLength = 0;

        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                // Rectangle i: (x1_i, y1_i) to (x2_i, y2_i)
                $x1_i = $bottomLeft[$i][0];
                $y1_i = $bottomLeft[$i][1];
                $x2_i = $topRight[$i][0];
                $y2_i = $topRight[$i][1];

                // Rectangle j: (x1_j, y1_j) to (x2_j, y2_j)
                $x1_j = $bottomLeft[$j][0];
                $y1_j = $bottomLeft[$j][1];
                $x2_j = $topRight[$j][0];
                $y2_j = $topRight[$j][1];

                // Calculate intersection coordinates
                $intersect_x_left = max($x1_i, $x1_j);
                $intersect_y_bottom = max($y1_i, $y1_j);
                $intersect_x_right = min($x2_i, $x2_j);
                $intersect_y_top = min($y2_i, $y2_j);

                // Check if an intersection exists (positive width and height)
                if ($intersect_x_left < $intersect_x_right && $intersect_y_bottom < $intersect_y_top) {
                    $current_width = $intersect_x_right - $intersect_x_left;
                    $current_height = $intersect_y_top - $intersect_y_bottom;
                    $current_side = min($current_width, $current_height);
                    $maxSideLength = max($maxSideLength, $current_side);
                }
            }
        }

        return $maxSideLength * $maxSideLength;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func largestSquareArea(_ bottomLeft: [[Int]], _ topRight: [[Int]]) -> Int {
        let n = bottomLeft.count
        var maxSideLength: Int = 0

        for i in 0..<n {
            for j in i + 1..<n {
                // Rectangle i: (x1_i, y1_i) to (x2_i, y2_i)
                let x1_i = bottomLeft[i][0]
                let y1_i = bottomLeft[i][1]
                let x2_i = topRight[i][0]
                let y2_i = topRight[i][1]

                // Rectangle j: (x1_j, y1_j) to (x2_j, y2_j)
                let x1_j = bottomLeft[j][0]
                let y1_j = bottomLeft[j][1]
                let x2_j = topRight[j][0]
                let y2_j = topRight[j][1]

                // Calculate intersection coordinates
                let intersect_x_left = max(x1_i, x1_j)
                let intersect_y_bottom = max(y1_i, y1_j)
                let intersect_x_right = min(x2_i, x2_j)
                let intersect_y_top = min(y2_i, y2_j)

                // Check if an intersection exists (positive width and height)
                if intersect_x_left < intersect_x_right && intersect_y_bottom < intersect_y_top {
                    let current_width = intersect_x_right - intersect_x_left
                    let current_height = intersect_y_top - intersect_y_bottom
                    let current_side = min(current_width, current_height)
                    maxSideLength = max(maxSideLength, current_side)
                }
            }
        }

        return maxSideLength * maxSideLength
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun largestSquareArea(bottomLeft: Array<IntArray>, topRight: Array<IntArray>): Long {
        var maxSide: Long = 0
        val n = bottomLeft.size

        for (i in 0 until n) {
            for (j in i + 1 until n) {
                val x1_i = bottomLeft[i][0]
                val y1_i = bottomLeft[i][1]
                val x2_i = topRight[i][0]
                val y2_i = topRight[i][1]

                val x1_j = bottomLeft[j][0]
                val y1_j = bottomLeft[j][1]
                val x2_j = topRight[j][0]
                val y2_j = topRight[j][1]

                val intersect_x1 = maxOf(x1_i, x1_j)
                val intersect_y1 = maxOf(y1_i, y1_j)
                val intersect_x2 = minOf(x2_i, x2_j)
                val intersect_y2 = minOf(y2_i, y2_j)

                if (intersect_x1 < intersect_x2 && intersect_y1 < intersect_y2) {
                    val width = (intersect_x2 - intersect_x1).toLong()
                    val height = (intersect_y2 - intersect_y1).toLong()
                    val currentSide = minOf(width, height)
                    maxSide = maxOf(maxSide, currentSide)
                }
            }
        }
        return maxSide * maxSide
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int largestSquareArea(List<List<int>> bottomLeft, List<List<int>> topRight) {
    int maxSide = 0;
    int n = bottomLeft.length;

    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {
        int x1_i = bottomLeft[i][0];
        int y1_i = bottomLeft[i][1];
        int x2_i = topRight[i][0];
        int y2_i = topRight[i][1];

        int x1_j = bottomLeft[j][0];
        int y1_j = bottomLeft[j][1];
        int x2_j = topRight[j][0];
        int y2_j = topRight[j][1];

        int intersect_x1 = x1_i > x1_j ? x1_i : x1_j;
        int intersect_y1 = y1_i > y1_j ? y1_i : y1_j;
        int intersect_x2 = x2_i < x2_j ? x2_i : x2_j;
        int intersect_y2 = y2_i < y2_j ? y2_i : y2_j;

        if (intersect_x1 < intersect_x2 && intersect_y1 < intersect_y2) {
          int width = intersect_x2 - intersect_x1;
          int height = intersect_y2 - intersect_y1;
          int currentSide = width < height ? width : height;
          if (currentSide > maxSide) {
            maxSide = currentSide;
          }
        }
      }
    }
    return maxSide * maxSide;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func largestSquareArea(bottomLeft [][]int, topRight [][]int) int64 {
    var maxSide int64 = 0
    n := len(bottomLeft)

    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            x1_i, y1_i := bottomLeft[i][0], bottomLeft[i][1]
            x2_i, y2_i := topRight[i][0], topRight[i][1]

            x1_j, y1_j := bottomLeft[j][0], bottomLeft[j][1]
            x2_j, y2_j := topRight[j][0], topRight[j][1]

            intersect_x1 := x1_i
            if x1_j > intersect_x1 {
                intersect_x1 = x1_j
            }
            intersect_y1 := y1_i
            if y1_j > intersect_y1 {
                intersect_y1 = y1_j
            }

            intersect_x2 := x2_i
            if x2_j < intersect_x2 {
                intersect_x2 = x2_j
            }
            intersect_y2 := y2_i
            if y2_j < intersect_y2 {
                intersect_y2 = y2_j
            }

            if intersect_x1 < intersect_x2 && intersect_y1 < intersect_y2 {
                width := int64(intersect_x2 - intersect_x1)
                height := int64(intersect_y2 - intersect_y1)
                currentSide := width
                if height < currentSide {
                    currentSide = height
                }
                if currentSide > maxSide {
                    maxSide = currentSide
                }
            }
        }
    }
    return maxSide * maxSide
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[][]} bottom_left
# @param {Integer[][]} top_right
# @return {Integer}
def largest_square_area(bottom_left, top_right)
    max_side = 0
    n = bottom_left.length

    (0...n).each do |i|
        (i + 1...n).each do |j|
            x1_i, y1_i = bottom_left[i][0], bottom_left[i][1]
            x2_i, y2_i = top_right[i][0], top_right[i][1]

            x1_j, y1_j = bottom_left[j][0], bottom_left[j][1]
            x2_j, y2_j = top_right[j][0], top_right[j][1]

            intersect_x1 = [x1_i, x1_j].max
            intersect_y1 = [y1_i, y1_j].max
            intersect_x2 = [x2_i, x2_j].min
            intersect_y2 = [y2_i, y2_j].min

            if intersect_x1 < intersect_x2 && intersect_y1 < intersect_y2
                width = intersect_x2 - intersect_x1
                height = intersect_y2 - intersect_y1
                current_side = [width, height].min
                max_side = [max_side, current_side].max
            end
        end
    end
    max_side * max_side
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def largestSquareArea(bottomLeft: Array[Array[Int]], topRight: Array[Array[Int]]): Long = {
        var maxSide: Long = 0
        val n = bottomLeft.length

        for (i <- 0 until n) {
            for (j <- i + 1 until n) {
                val x1_i = bottomLeft(i)(0)
                val y1_i = bottomLeft(i)(1)
                val x2_i = topRight(i)(0)
                val y2_i = topRight(i)(1)

                val x1_j = bottomLeft(j)(0)
                val y1_j = bottomLeft(j)(1)
                val x2_j = topRight(j)(0)
                val y2_j = topRight(j)(1)

                val intersect_x1 = math.max(x1_i, x1_j)
                val intersect_y1 = math.max(y1_i, y1_j)
                val intersect_x2 = math.min(x2_i, x2_j)
                val intersect_y2 = math.min(y2_i, y2_j)

                if (intersect_x1 < intersect_x2 && intersect_y1 < intersect_y2) {
                    val width = (intersect_x2 - intersect_x1).toLong
                    val height = (intersect_y2 - intersect_y1).toLong
                    val currentSide = math.min(width, height)
                    maxSide = math.max(maxSide, currentSide)
                }
            }
        }
        maxSide * maxSide
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn largest_square_area(bottom_left: Vec<Vec<i32>>, top_right: Vec<Vec<i32>>) -> i64 {
        let mut max_side: i64 = 0;
        let n = bottom_left.len();

        for i in 0..n {
            for j in (i + 1)..n {
                let x1_i = bottom_left[i][0];
                let y1_i = bottom_left[i][1];
                let x2_i = top_right[i][0];
                let y2_i = top_right[i][1];

                let x1_j = bottom_left[j][0];
                let y1_j = bottom_left[j][1];
                let x2_j = top_right[j][0];
                let y2_j = top_right[j][1];

                let intersect_x1 = x1_i.max(x1_j);
                let intersect_y1 = y1_i.max(y1_j);
                let intersect_x2 = x2_i.min(x2_j);
                let intersect_y2 = y2_i.min(y2_j);

                if intersect_x1 < intersect_x2 && intersect_y1 < intersect_y2 {
                    let width = (intersect_x2 - intersect_x1) as i64;
                    let height = (intersect_y2 - intersect_y1) as i64;
                    let current_side = width.min(height);
                    max_side = max_side.max(current_side);
                }
            }
        }
        max_side * max_side
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (largest-square-area bottomLeft topRight)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)) exact-integer?)
  (let* ([n (length bottomLeft)]
         [max-side 0])
    (for* ([i (range n)]
           [j (range (+ i 1) n)])
      (let* ([rect-i-bl (list-ref bottomLeft i)]
             [rect-i-tr (list-ref topRight i)]
             [x1-i (list-ref rect-i-bl 0)]
             [y1-i (list-ref rect-i-bl 1)]
             [x2-i (list-ref rect-i-tr 0)]
             [y2-i (list-ref rect-i-tr 1)]

             [rect-j-bl (list-ref bottomLeft j)]
             [rect-j-tr (list-ref topRight j)]
             [x1-j (list-ref rect-j-bl 0)]
             [y1-j (list-ref rect-j-bl 1)]
             [x2-j (list-ref rect-j-tr 0)]
             [y2-j (list-ref rect-j-tr 1)]

             [intersect-x1 (max x1-i x1-j)]
             [intersect-y1 (max y1-i y1-j)]
             [intersect-x2 (min x2-i x2-j)]
             [intersect-y2 (min y2-i y2-j)])
        (when (and (< intersect-x1 intersect-x2)
                   (< intersect-y1 intersect-y2))
          (let* ([width (- intersect-x2 intersect-x1)]
                 [height (- intersect-y2 intersect-y1)]
                 [current-side (min width height)])
            (set! max-side (max max-side current-side))))))
    (* max-side max-side)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec largest_square_area(BottomLeft :: [[integer()]], TopRight :: [[integer()]]) -> integer().
largest_square_area(BottomLeft, TopRight) ->
    N = length(BottomLeft),
    BottomLeftArray = array:from_list(BottomLeft),
    TopRightArray = array:from_list(TopRight),
    largest_square_area_loop(0, N, BottomLeftArray, TopRightArray, 0).

largest_square_area_loop(I, N, BottomLeftArray, TopRightArray, MaxSide) when I < N ->
    largest_square_area_inner_loop(I, I + 1, N, BottomLeftArray, TopRightArray, MaxSide);
largest_square_area_loop(N, N, _BottomLeftArray, _TopRightArray, MaxSide) ->
    MaxSide * MaxSide.

largest_square_area_inner_loop(I, J, N, BottomLeftArray, TopRightArray, MaxSide) when J < N ->
    [X1_i, Y1_i] = array:get(I, BottomLeftArray),
    [X2_i, Y2_i] = array:get(I, TopRightArray),

    [X1_j, Y1_j] = array:get(J, BottomLeftArray),
    [X2_j, Y2_j] = array:get(J, TopRightArray),

    IntersectX1 = max(X1_i, X1_j),
    IntersectY1 = max(Y1_i, Y1_j),
    IntersectX2 = min(X2_i, X2_j),
    IntersectY2 = min(Y2_i, Y2_j),

    NewMaxSide =
        if
            IntersectX1 < IntersectX2 andalso IntersectY1 < IntersectY2 ->
                Width = IntersectX2 - IntersectX1,
                Height = IntersectY2 - IntersectY1,
                CurrentSide = min(Width, Height),
                max(MaxSide, CurrentSide);
            true ->
                MaxSide
        end,
    largest_square_area_inner_loop(I, J + 1, N, BottomLeftArray, TopRightArray, NewMaxSide);
largest_square_area_inner_loop(I, N, N, BottomLeftArray, TopRightArray, MaxSide) ->
    largest_square_area_loop(I + 1, N, BottomLeftArray, TopRightArray, MaxSide).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec largest_square_area(bottom_left :: [[integer]], top_right :: [[integer]]) :: integer
  def largest_square_area(bottom_left, top_right) do
    n = length(bottom_left)

    bottom_left_map = Enum.with_index(bottom_left) |> Map.new(fn {rect, idx} -> {idx, rect} end)
    top_right_map = Enum.with_index(top_right) |> Map.new(fn {rect, idx} -> {idx, rect} end)

    max_side = 
      for i <- 0..(n - 1),
          j <- (i + 1)..(n - 1),
          reduce: 0 do
        acc_max_side ->
          [x1_i, y1_i] = Map.fetch!(bottom_left_map, i)
          [x2_i, y2_i] = Map.fetch!(top_right_map, i)

          [x1_j, y1_j] = Map.fetch!(bottom_left_map, j)
          [x2_j, y2_j] = Map.fetch!(top_right_map, j)

          intersect_x1 = max(x1_i, x1_j)
          intersect_y1 = max(y1_i, y1_j)
          intersect_x2 = min(x2_i, x2_j)
          intersect_y2 = min(y2_i, y2_j)

          if intersect_x1 < intersect_x2 && intersect_y1 < intersect_y2 do
            width = intersect_x2 - intersect_x1
            height = intersect_y2 - intersect_y1
            current_side = min(width, height)
            max(acc_max_side, current_side)
          else
            acc_max_side
          end
      end

    max_side * max_side
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N^2), where N is the number of rectangles. This is because we iterate through all unique pairs of rectangles. There are N * (N - 1) / 2 such pairs. For each pair, calculating the intersection and its dimensions involves a constant number of comparisons and arithmetic operations. For languages like Erlang and Elixir, where list indexing (e.g., `lists:nth` or `Enum.at`) is O(N), an initial conversion to an array or map for O(1) access is performed, adding an O(N) overhead, but keeping the overall pair-wise processing at O(N^2).

- **Space Complexity:** The space complexity is O(1) for most languages, as we only store a few variables to track the maximum side length and temporary intersection coordinates. For Erlang and Elixir, if the input lists are converted to arrays or maps for O(1) access, this conversion adds O(N) space complexity to store these auxiliary data structures. However, this is typically considered part of the input processing and not additional space for the core algorithm logic itself, or it's within acceptable limits for the problem's constraints.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-17 01:09:14 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by iterating over all pairs of rectangles and checking if they intersect. If two rectangles intersect, we calculate the intersection area and find the maximum square that can fit inside this area. We keep track of the maximum square area found so far. The key intuition is that the intersection area of two rectangles is also a rectangle, and the maximum square that can fit inside this area will have a side length equal to the minimum of the width and height of the intersection area.

  The algorithm works by first defining a function to calculate the intersection area of two rectangles. Then, it iterates over all pairs of rectangles, calculates their intersection area, and finds the maximum square that can fit inside this area. If the maximum square area is greater than the current maximum, it updates the maximum area. Finally, it returns the maximum square area found.

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
    long long largestSquareArea(vector<vector<int>>& bottomLeft, vector<vector<int>>& topRight) {
        long long maxArea = 0;
        for (int i = 0; i < bottomLeft.size(); i++) {
            for (int j = i + 1; j < bottomLeft.size(); j++) {
                int x1 = max(bottomLeft[i][0], bottomLeft[j][0]);
                int y1 = max(bottomLeft[i][1], bottomLeft[j][1]);
                int x2 = min(topRight[i][0], topRight[j][0]);
                int y2 = min(topRight[i][1], topRight[j][1]);
                if (x1 < x2 && y1 < y2) {
                    int side = min(x2 - x1, y2 - y1);
                    maxArea = max(maxArea, (long long)side * side);
                }
            }
        }
        return maxArea;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public long largestSquareArea(int[][] bottomLeft, int[][] topRight) {
        long maxArea = 0;
        for (int i = 0; i < bottomLeft.length; i++) {
            for (int j = i + 1; j < bottomLeft.length; j++) {
                int x1 = Math.max(bottomLeft[i][0], bottomLeft[j][0]);
                int y1 = Math.max(bottomLeft[i][1], bottomLeft[j][1]);
                int x2 = Math.min(topRight[i][0], topRight[j][0]);
                int y2 = Math.min(topRight[i][1], topRight[j][1]);
                if (x1 < x2 && y1 < y2) {
                    int side = Math.min(x2 - x1, y2 - y1);
                    maxArea = Math.max(maxArea, (long)side * side);
                }
            }
        }
        return maxArea;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def largestSquareArea(self, bottomLeft, topRight):
        maxArea = 0
        for i in range(len(bottomLeft)):
            for j in range(i + 1, len(bottomLeft)):
                x1 = max(bottomLeft[i][0], bottomLeft[j][0])
                y1 = max(bottomLeft[i][1], bottomLeft[j][1])
                x2 = min(topRight[i][0], topRight[j][0])
                y2 = min(topRight[i][1], topRight[j][1])
                if x1 < x2 and y1 < y2:
                    side = min(x2 - x1, y2 - y1)
                    maxArea = max(maxArea, side * side)
        return maxArea
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def largestSquareArea(self, bottomLeft: list[list[int]], topRight: list[list[int]]) -> int:
        maxArea = 0
        for i in range(len(bottomLeft)):
            for j in range(i + 1, len(bottomLeft)):
                x1 = max(bottomLeft[i][0], bottomLeft[j][0])
                y1 = max(bottomLeft[i][1], bottomLeft[j][1])
                x2 = min(topRight[i][0], topRight[j][0])
                y2 = min(topRight[i][1], topRight[j][1])
                if x1 < x2 and y1 < y2:
                    side = min(x2 - x1, y2 - y1)
                    maxArea = max(maxArea, side * side)
        return maxArea
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
long long largestSquareArea(int** bottomLeft, int bottomLeftSize, int* bottomLeftColSize, int** topRight, int topRightSize, int* topRightColSize) {
    long long maxArea = 0;
    for (int i = 0; i < bottomLeftSize; i++) {
        for (int j = i + 1; j < bottomLeftSize; j++) {
            int x1 = (bottomLeft[i][0] > bottomLeft[j][0]) ? bottomLeft[i][0] : bottomLeft[j][0];
            int y1 = (bottomLeft[i][1] > bottomLeft[j][1]) ? bottomLeft[i][1] : bottomLeft[j][1];
            int x2 = (topRight[i][0] < topRight[j][0]) ? topRight[i][0] : topRight[j][0];
            int y2 = (topRight[i][1] < topRight[j][1]) ? topRight[i][1] : topRight[j][1];
            if (x1 < x2 && y1 < y2) {
                int side = (x2 - x1 < y2 - y1) ? x2 - x1 : y2 - y1;
                maxArea = (maxArea > side * side) ? maxArea : side * side;
            }
        }
    }
    return maxArea;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public long LargestSquareArea(int[][] bottomLeft, int[][] topRight) {
        long maxArea = 0;
        for (int i = 0; i < bottomLeft.Length; i++) {
            for (int j = i + 1; j < bottomLeft.Length; j++) {
                int x1 = Math.Max(bottomLeft[i][0], bottomLeft[j][0]);
                int y1 = Math.Max(bottomLeft[i][1], bottomLeft[j][1]);
                int x2 = Math.Min(topRight[i][0], topRight[j][0]);
                int y2 = Math.Min(topRight[i][1], topRight[j][1]);
                if (x1 < x2 && y1 < y2) {
                    int side = Math.Min(x2 - x1, y2 - y1);
                    maxArea = Math.Max(maxArea, (long)side * side);
                }
            }
        }
        return maxArea;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var largestSquareArea = function(bottomLeft, topRight) {
    let maxArea = 0;
    for (let i = 0; i < bottomLeft.length; i++) {
        for (let j = i + 1; j < bottomLeft.length; j++) {
            let x1 = Math.max(bottomLeft[i][0], bottomLeft[j][0]);
            let y1 = Math.max(bottomLeft[i][1], bottomLeft[j][1]);
            let x2 = Math.min(topRight[i][0], topRight[j][0]);
            let y2 = Math.min(topRight[i][1], topRight[j][1]);
            if (x1 < x2 && y1 < y2) {
                let side = Math.min(x2 - x1, y2 - y1);
                maxArea = Math.max(maxArea, side * side);
            }
        }
    }
    return maxArea;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function largestSquareArea(bottomLeft: number[][], topRight: number[][]): number {
    let maxArea = 0;
    for (let i = 0; i < bottomLeft.length; i++) {
        for (let j = i + 1; j < bottomLeft.length; j++) {
            let x1 = Math.max(bottomLeft[i][0], bottomLeft[j][0]);
            let y1 = Math.max(bottomLeft[i][1], bottomLeft[j][1]);
            let x2 = Math.min(topRight[i][0], topRight[j][0]);
            let y2 = Math.min(topRight[i][1], topRight[j][1]);
            if (x1 < x2 && y1 < y2) {
                let side = Math.min(x2 - x1, y2 - y1);
                maxArea = Math.max(maxArea, side * side);
            }
        }
    }
    return maxArea;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function largestSquareArea($bottomLeft, $topRight) {
        $maxArea = 0;
        for ($i = 0; $i < count($bottomLeft); $i++) {
            for ($j = $i + 1; $j < count($bottomLeft); $j++) {
                $x1 = max($bottomLeft[$i][0], $bottomLeft[$j][0]);
                $y1 = max($bottomLeft[$i][1], $bottomLeft[$j][1]);
                $x2 = min($topRight[$i][0], $topRight[$j][0]);
                $y2 = min($topRight[$i][1], $topRight[$j][1]);
                if ($x1 < $x2 && $y1 < $y2) {
                    $side = min($x2 - $x1, $y2 - $y1);
                    $maxArea = max($maxArea, $side * $side);
                }
            }
        }
        return $maxArea;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func largestSquareArea(_ bottomLeft: [[Int]], _ topRight: [[Int]]) -> Int {
        var maxArea = 0
        for i in 0..<bottomLeft.count {
            for j in i + 1..<bottomLeft.count {
                let x1 = max(bottomLeft[i][0], bottomLeft[j][0])
                let y1 = max(bottomLeft[i][1], bottomLeft[j][1])
                let x2 = min(topRight[i][0], topRight[j][0])
                let y2 = min(topRight[i][1], topRight[j][1])
                if x1 < x2 && y1 < y2 {
                    let side = min(x2 - x1, y2 - y1)
                    maxArea = max(maxArea, side * side)
                }
            }
        }
        return maxArea
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun largestSquareArea(bottomLeft: Array<IntArray>, topRight: Array<IntArray>): Long {
        var maxArea = 0L
        for (i in bottomLeft.indices) {
            for (j in i + 1 until bottomLeft.size) {
                val x1 = maxOf(bottomLeft[i][0], bottomLeft[j][0])
                val y1 = maxOf(bottomLeft[i][1], bottomLeft[j][1])
                val x2 = minOf(topRight[i][0], topRight[j][0])
                val y2 = minOf(topRight[i][1], topRight[j][1])
                if (x1 < x2 && y1 < y2) {
                    val side = minOf(x2 - x1, y2 - y1)
                    maxArea = maxOf(maxArea, side.toLong() * side)
                }
            }
        }
        return maxArea
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int largestSquareArea(List<List<int>> bottomLeft, List<List<int>> topRight) {
    int maxArea = 0;
    for (int i = 0; i < bottomLeft.length; i++) {
      for (int j = i + 1; j < bottomLeft.length; j++) {
        int x1 = bottomLeft[i][0] > bottomLeft[j][0] ? bottomLeft[i][0] : bottomLeft[j][0];
        int y1 = bottomLeft[i][1] > bottomLeft[j][1] ? bottomLeft[i][1] : bottomLeft[j][1];
        int x2 = topRight[i][0] < topRight[j][0] ? topRight[i][0] : topRight[j][0];
        int y2 = topRight[i][1] < topRight[j][1] ? topRight[i][1] : topRight[j][1];
        if (x1 < x2 && y1 < y2) {
          int side = x2 - x1 < y2 - y1 ? x2 - x1 : y2 - y1;
          maxArea = maxArea > side * side ? maxArea : side * side;
        }
      }
    }
    return maxArea;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func largestSquareArea(bottomLeft [][]int, topRight [][]int) int64 {
    maxArea := int64(0)
    for i := 0; i < len(bottomLeft); i++ {
        for j := i + 1; j < len(bottomLeft); j++ {
            x1 := max(bottomLeft[i][0], bottomLeft[j][0])
            y1 := max(bottomLeft[i][1], bottomLeft[j][1])
            x2 := min(topRight[i][0], topRight[j][0])
            y2 := min(topRight[i][1], topRight[j][1])
            if x1 < x2 && y1 < y2 {
                side := min(x2-x1, y2-y1)
                if int64(side)*int64(side) > maxArea {
                    maxArea = int64(side) * int64(side)
                }
            }
        }
    }
    return maxArea
}
func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
func min(a, b int) int {
    if a < b {
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
def largest_square_area(bottom_left, top_right)
    max_area = 0
    (0...bottom_left.size).each do |i|
        (i + 1...bottom_left.size).each do |j|
            x1 = [bottom_left[i][0], bottom_left[j][0]].max
            y1 = [bottom_left[i][1], bottom_left[j][1]].max
            x2 = [top_right[i][0], top_right[j][0]].min
            y2 = [top_right[i][1], top_right[j][1]].min
            if x1 < x2 && y1 < y2
                side = [x2 - x1, y2 - y1].min
                max_area = [max_area, side * side].max
            end
        end
    end
    max_area
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def largestSquareArea(bottomLeft: Array[Array[Int]], topRight: Array[Array[Int]]): Long = {
        var maxArea = 0L
        for (i <- bottomLeft.indices) {
            for (j <- i + 1 until bottomLeft.length) {
                val x1 = math.max(bottomLeft(i)(0), bottomLeft(j)(0))
                val y1 = math.max(bottomLeft(i)(1), bottomLeft(j)(1))
                val x2 = math.min(topRight(i)(0), topRight(j)(0))
                val y2 = math.min(topRight(i)(1), topRight(j)(1))
                if (x1 < x2 && y1 < y2) {
                    val side = math.min(x2 - x1, y2 - y1)
                    maxArea = math.max(maxArea, side.toLong * side)
                }
            }
        }
        maxArea
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn largest_square_area(bottom_left: Vec<Vec<i32>>, top_right: Vec<Vec<i32>>) -> i64 {
        let mut max_area = 0;
        for i in 0..bottom_left.len() {
            for j in i + 1..bottom_left.len() {
                let x1 = bottom_left[i][0].max(bottom_left[j][0]);
                let y1 = bottom_left[i][1].max(bottom_left[j][1]);
                let x2 = top_right[i][0].min(top_right[j][0]);
                let y2 = top_right[i][1].min(top_right[j][1]);
                if x1 < x2 && y1 < y2 {
                    let side = (x2 - x1).min(y2 - y1);
                    max_area = max_area.max((side as i64) * (side as i64));
                }
            }
        }
        max_area as i64
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (largest-square-area bottomLeft topRight)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)) exact-integer?)
  (let loop ([i 0]
             [max-area 0])
    (if (= i (length bottomLeft))
        max-area
        (let loop2 ([j (add1 i)]
                   [max-area max-area])
          (if (= j (length bottomLeft))
              (loop (add1 i) max-area)
              (let* ([x1 (max (list-ref (list-ref bottomLeft i) 0) (list-ref (list-ref bottomLeft j) 0))]
                     [y1 (max (list-ref (list-ref bottomLeft i) 1) (list-ref (list-ref bottomLeft j) 1))]
                     [x2 (min (list-ref (list-ref topRight i) 0) (list-ref (list-ref topRight j) 0))]
                     [y2 (min (list-ref (list-ref topRight i) 1) (list-ref (list-ref topRight j) 1))]
                     [side (min (- x2 x1) (- y2 y1))])
                (if (and (< x1 x2) (< y1 y2))
                    (loop2 (add1 j) (max max-area (* side side)))
                    (loop2 (add1 j) max-area))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([largest_square_area/2]).

largest_square_area(BottomLeft, TopRight) ->
    lists:foldl(
      fun({I, MaxArea}, {BottomLeftI, TopRightI}) ->
              lists:foldl(
                fun({J, MaxArea1}, {BottomLeftJ, TopRightJ}) ->
                        X1 = max(lists:nth(1, BottomLeftI), lists:nth(1, BottomLeftJ)),
                        Y1 = max(lists:nth(2, BottomLeftI), lists:nth(2, BottomLeftJ)),
                        X2 = min(lists:nth(1, TopRightI), lists:nth(1, TopRightJ)),
                        Y2 = min(lists:nth(2, TopRightI), lists:nth(2, TopRightJ)),
                        Side = min(X2 - X1, Y2 - Y1),
                        if
                          X1 < X2 andalso Y1 < Y2 ->
                            {J + 1, max(MaxArea1, Side * Side)};
                          true ->
                            {J + 1, MaxArea1}
                        end
                end,
                {I + 1, MaxArea},
                lists:zip(BottomLeft, TopRight)
              end,
              {0, 0},
              lists:zip(BottomLeft, TopRight)
      end,
      {0, 0},
      lists:zip(BottomLeft, TopRight)
    ).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec largest_square_area(bottom_left :: [[integer]], top_right :: [[integer]]) :: integer
  def largest_square_area(bottom_left, top_right) do
    max_area = 0
    for i <- 0..(length(bottom_left) - 1) do
      for j <- (i + 1)..(length(bottom_left) - 1) do
        x1 = max(Enum.at(Enum.at(bottom_left, i), 0), Enum.at(Enum.at(bottom_left, j), 0))
        y1 = max(Enum.at(Enum.at(bottom_left, i), 1), Enum.at(Enum.at(bottom_left, j), 1))
        x2 = min(Enum.at(Enum.at(top_right, i), 0), Enum.at(Enum.at(top_right, j), 0))
        y2 = min(Enum.at(Enum.at(top_right, i), 1), Enum.at(Enum.at(top_right, j), 1))
        if x1 < x2 and y1 < y2 do
          side = min(x2 - x1, y2 - y1)
          max_area = max(max_area, side * side)
        end
      end
    end
    max_area
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of the algorithm is O(n^2) where n is the number of rectangles. This is because we are iterating over all pairs of rectangles, and for each pair, we are calculating the intersection area and finding the maximum square that can fit inside this area.

- **Space Complexity:** The space complexity of the algorithm is O(1) as we are not using any additional space that scales with the input size. We are only using a constant amount of space to store the maximum square area and other variables.

</div>
</details>
