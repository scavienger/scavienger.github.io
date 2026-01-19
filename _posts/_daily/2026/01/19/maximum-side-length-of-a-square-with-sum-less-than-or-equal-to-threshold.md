---
layout: post
title: "Maximum Side Length of a Square with Sum Less than or Equal to Threshold"
date: 2026-01-19 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Binary Search", "Matrix", "Prefix Sum"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxSideLength(vector<vector<int>>& mat,\
        \ int threshold) {\n        int m = mat.size();\n        int n = mat[0].size();\n\
        \n        vector<vector<int>> ps(m + 1, vector<int>(n + 1, 0));\n\n        for\
        \ (int i = 0; i < m; ++i) {\n            for (int j = 0; j < n; ++j) {\n   \
        \             ps[i + 1][j + 1] = mat[i][j] + ps[i][j + 1] + ps[i + 1][j] - ps[i][j];\n\
        \            }\n        }\n\n        auto getSquareSum = [&](int r1, int c1,\
        \ int r2, int c2) {\n            // r1, c1, r2, c2 are 0-indexed for the original\
        \ matrix\n            // ps array is 1-indexed for convenience\n           \
        \ return (long long)ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1];\n\
        \        };\n\n        auto check = [&](int k) {\n            if (k == 0) return\
        \ true; // A 0x0 square always has sum 0 <= threshold\n            for (int\
        \ r = 0; r <= m - k; ++r) {\n                for (int c = 0; c <= n - k; ++c)\
        \ {\n                    if (getSquareSum(r, c, r + k - 1, c + k - 1) <= threshold)\
        \ {\n                        return true;\n                    }\n         \
        \       }\n            }\n            return false;\n        };\n\n        int\
        \ low = 0;\n        int high = min(m, n);\n        int ans = 0;\n\n        while\
        \ (low <= high) {\n            int mid = low + (high - low) / 2;\n         \
        \   if (check(mid)) {\n                ans = mid;\n                low = mid\
        \ + 1;\n            } else {\n                high = mid - 1;\n            }\n\
        \        }\n\n        return ans;\n    }\n};"
      java: "class Solution {\n    public int maxSideLength(int[][] mat, int threshold)\
        \ {\n        int m = mat.length;\n        int n = mat[0].length;\n\n       \
        \ int[][] ps = new int[m + 1][n + 1];\n\n        for (int i = 0; i < m; ++i)\
        \ {\n            for (int j = 0; j < n; ++j) {\n                ps[i + 1][j\
        \ + 1] = mat[i][j] + ps[i][j + 1] + ps[i + 1][j] - ps[i][j];\n            }\n\
        \        }\n\n        // Helper function to get sum of a square from (r1, c1)\
        \ to (r2, c2)\n        // Note: r1, c1, r2, c2 are 0-indexed for the original\
        \ matrix\n        // ps array is 1-indexed for convenience\n        // Using\
        \ a lambda for clarity, but could be an inner method or inlined.\n        java.util.function.Function<int[],\
        \ Long> getSquareSum = (coords) -> {\n            int r1 = coords[0], c1 = coords[1],\
        \ r2 = coords[2], c2 = coords[3];\n            return (long)ps[r2 + 1][c2 +\
        \ 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1];\n        };\n\n       \
        \ // Helper function to check if a square of side length k exists\n        java.util.function.IntPredicate\
        \ check = (k) -> {\n            if (k == 0) return true; // A 0x0 square always\
        \ has sum 0 <= threshold\n            for (int r = 0; r <= m - k; ++r) {\n \
        \               for (int c = 0; c <= n - k; ++c) {\n                    if (getSquareSum.apply(new\
        \ int[]{r, c, r + k - 1, c + k - 1}) <= threshold) {\n                     \
        \   return true;\n                    }\n                }\n            }\n\
        \            return false;\n        };\n\n        int low = 0;\n        int\
        \ high = Math.min(m, n);\n        int ans = 0;\n\n        while (low <= high)\
        \ {\n            int mid = low + (high - low) / 2;\n            if (check.test(mid))\
        \ {\n                ans = mid;\n                low = mid + 1;\n          \
        \  } else {\n                high = mid - 1;\n            }\n        }\n\n \
        \       return ans;\n    }\n}"
      python: "class Solution(object):\n    def maxSideLength(self, mat, threshold):\n\
        \        \"\"\"\n        :type mat: List[List[int]]\n        :type threshold:\
        \ int\n        :rtype: int\n        \"\"\"\n        m = len(mat)\n        n\
        \ = len(mat[0])\n\n        ps = [[0] * (n + 1) for _ in range(m + 1)]\n\n  \
        \      for i in range(m):\n            for j in range(n):\n                ps[i\
        \ + 1][j + 1] = mat[i][j] + ps[i][j + 1] + ps[i + 1][j] - ps[i][j]\n\n     \
        \   def get_square_sum(r1, c1, r2, c2):\n            # r1, c1, r2, c2 are 0-indexed\
        \ for the original matrix\n            # ps array is 1-indexed for convenience\n\
        \            return ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1]\n\
        \n        def check(k):\n            if k == 0: return True # A 0x0 square always\
        \ has sum 0 <= threshold\n            for r in range(m - k + 1):\n         \
        \       for c in range(n - k + 1):\n                    if get_square_sum(r,\
        \ c, r + k - 1, c + k - 1) <= threshold:\n                        return True\n\
        \            return False\n\n        low = 0\n        high = min(m, n)\n   \
        \     ans = 0\n\n        while low <= high:\n            mid = low + (high -\
        \ low) // 2\n            if check(mid):\n                ans = mid\n       \
        \         low = mid + 1\n            else:\n                high = mid - 1\n\
        \n        return ans"
      python3: "class Solution:\n    def maxSideLength(self, mat: List[List[int]], threshold:\
        \ int) -> int:\n        m = len(mat)\n        n = len(mat[0])\n\n        ps\
        \ = [[0] * (n + 1) for _ in range(m + 1)]\n\n        for i in range(m):\n  \
        \          for j in range(n):\n                ps[i + 1][j + 1] = mat[i][j]\
        \ + ps[i][j + 1] + ps[i + 1][j] - ps[i][j]\n\n        def get_square_sum(r1:\
        \ int, c1: int, r2: int, c2: int) -> int:\n            # r1, c1, r2, c2 are\
        \ 0-indexed for the original matrix\n            # ps array is 1-indexed for\
        \ convenience\n            return ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2\
        \ + 1][c1] + ps[r1][c1]\n\n        def check(k: int) -> bool:\n            if\
        \ k == 0: return True # A 0x0 square always has sum 0 <= threshold\n       \
        \     for r in range(m - k + 1):\n                for c in range(n - k + 1):\n\
        \                    if get_square_sum(r, c, r + k - 1, c + k - 1) <= threshold:\n\
        \                        return True\n            return False\n\n        low\
        \ = 0\n        high = min(m, n)\n        ans = 0\n\n        while low <= high:\n\
        \            mid = low + (high - low) // 2\n            if check(mid):\n   \
        \             ans = mid\n                low = mid + 1\n            else:\n\
        \                high = mid - 1\n\n        return ans"
      c: "int maxSideLength(int** mat, int matSize, int* matColSize, int threshold)\
        \ {\n    int m = matSize;\n    int n = matColSize[0]; // Assuming all rows have\
        \ the same number of columns\n\n    // Allocate and initialize prefix sum array\n\
        \    int** ps = (int**)malloc((m + 1) * sizeof(int*));\n    for (int i = 0;\
        \ i <= m; ++i) {\n        ps[i] = (int*)malloc((n + 1) * sizeof(int));\n   \
        \     for (int j = 0; j <= n; ++j) {\n            ps[i][j] = 0;\n        }\n\
        \    }\n\n    for (int i = 0; i < m; ++i) {\n        for (int j = 0; j < n;\
        \ ++j) {\n            ps[i + 1][j + 1] = mat[i][j] + ps[i][j + 1] + ps[i + 1][j]\
        \ - ps[i][j];\n        }\n    }\n\n    int low = 0;\n    int high = (m < n)\
        \ ? m : n;\n    int ans = 0;\n\n    while (low <= high) {\n        int mid =\
        \ low + (high - low) / 2;\n\n        // check(mid) logic inline\n        int\
        \ found = 0;\n        if (mid == 0) {\n            found = 1; // A 0x0 square\
        \ always has sum 0 <= threshold\n        } else {\n            for (int r =\
        \ 0; r <= m - mid; ++r) {\n                for (int c = 0; c <= n - mid; ++c)\
        \ {\n                    // Calculate sum for square with top-left (r, c) and\
        \ side 'mid'\n                    // Bottom-right is (r + mid - 1, c + mid -\
        \ 1)\n                    // Using ps array (1-indexed): ps[r+mid][c+mid] -\
        \ ps[r][c+mid] - ps[r+mid][c] + ps[r][c]\n                    long long current_sum\
        \ = (long long)ps[r + mid][c + mid] - ps[r][c + mid] - ps[r + mid][c] + ps[r][c];\n\
        \                    if (current_sum <= threshold) {\n                     \
        \   found = 1;\n                        break;\n                    }\n    \
        \            }\n                if (found) break;\n            }\n        }\n\
        \n        if (found) {\n            ans = mid;\n            low = mid + 1;\n\
        \        } else {\n            high = mid - 1;\n        }\n    }\n\n    // Free\
        \ allocated memory for ps\n    for (int i = 0; i <= m; ++i) {\n        free(ps[i]);\n\
        \    }\n    free(ps);\n\n    return ans;\n}"
      csharp: "public class Solution {\n    public int MaxSideLength(int[][] mat, int\
        \ threshold) {\n        int m = mat.Length;\n        int n = mat[0].Length;\n\
        \n        int[][] ps = new int[m + 1][];\n        for (int i = 0; i <= m; i++)\
        \ {\n            ps[i] = new int[n + 1];\n        }\n\n        for (int i =\
        \ 0; i < m; ++i) {\n            for (int j = 0; j < n; ++j) {\n            \
        \    ps[i + 1][j + 1] = mat[i][j] + ps[i][j + 1] + ps[i + 1][j] - ps[i][j];\n\
        \            }\n        }\n\n        // Helper function to get sum of a square\
        \ from (r1, c1) to (r2, c2)\n        // Note: r1, c1, r2, c2 are 0-indexed for\
        \ the original matrix\n        // ps array is 1-indexed for convenience\n  \
        \      long GetSquareSum(int r1, int c1, int r2, int c2) {\n            return\
        \ (long)ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1];\n\
        \        }\n\n        // Helper function to check if a square of side length\
        \ k exists\n        bool Check(int k) {\n            if (k == 0) return true;\
        \ // A 0x0 square always has sum 0 <= threshold\n            for (int r = 0;\
        \ r <= m - k; ++r) {\n                for (int c = 0; c <= n - k; ++c) {\n \
        \                   if (GetSquareSum(r, c, r + k - 1, c + k - 1) <= threshold)\
        \ {\n                        return true;\n                    }\n         \
        \       }\n            }\n            return false;\n        }\n\n        int\
        \ low = 0;\n        int high = Math.Min(m, n);\n        int ans = 0;\n\n   \
        \     while (low <= high) {\n            int mid = low + (high - low) / 2;\n\
        \            if (Check(mid)) {\n                ans = mid;\n               \
        \ low = mid + 1;\n            } else {\n                high = mid - 1;\n  \
        \          }\n        }\n\n        return ans;\n    }\n}"
      javascript: "/**\n * @param {number[][]} mat\n * @param {number} threshold\n *\
        \ @return {number}\n */\nvar maxSideLength = function(mat, threshold) {\n  \
        \  const m = mat.length;\n    const n = mat[0].length;\n\n    const ps = Array(m\
        \ + 1).fill(0).map(() => Array(n + 1).fill(0));\n\n    for (let i = 0; i < m;\
        \ ++i) {\n        for (let j = 0; j < n; ++j) {\n            ps[i + 1][j + 1]\
        \ = mat[i][j] + ps[i][j + 1] + ps[i + 1][j] - ps[i][j];\n        }\n    }\n\n\
        \    // Helper function to get sum of a square from (r1, c1) to (r2, c2)\n \
        \   // Note: r1, c1, r2, c2 are 0-indexed for the original matrix\n    // ps\
        \ array is 1-indexed for convenience\n    const getSquareSum = (r1, c1, r2,\
        \ c2) => {\n        return ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1]\
        \ + ps[r1][c1];\n    };\n\n    // Helper function to check if a square of side\
        \ length k exists\n    const check = (k) => {\n        if (k === 0) return true;\
        \ // A 0x0 square always has sum 0 <= threshold\n        for (let r = 0; r <=\
        \ m - k; ++r) {\n            for (let c = 0; c <= n - k; ++c) {\n          \
        \      if (getSquareSum(r, c, r + k - 1, c + k - 1) <= threshold) {\n      \
        \              return true;\n                }\n            }\n        }\n \
        \       return false;\n    };\n\n    let low = 0;\n    let high = Math.min(m,\
        \ n);\n    let ans = 0;\n\n    while (low <= high) {\n        let mid = Math.floor(low\
        \ + (high - low) / 2);\n        if (check(mid)) {\n            ans = mid;\n\
        \            low = mid + 1;\n        } else {\n            high = mid - 1;\n\
        \        }\n    }\n\n    return ans;\n};"
      typescript: "function maxSideLength(mat: number[][], threshold: number): number\
        \ {\n    const m = mat.length;\n    const n = mat[0].length;\n\n    const ps:\
        \ number[][] = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));\n\n   \
        \ for (let i = 0; i < m; ++i) {\n        for (let j = 0; j < n; ++j) {\n   \
        \         ps[i + 1][j + 1] = mat[i][j] + ps[i][j + 1] + ps[i + 1][j] - ps[i][j];\n\
        \        }\n    }\n\n    // Helper function to get sum of a square from (r1,\
        \ c1) to (r2, c2)\n    // Note: r1, c1, r2, c2 are 0-indexed for the original\
        \ matrix\n    // ps array is 1-indexed for convenience\n    const getSquareSum\
        \ = (r1: number, c1: number, r2: number, c2: number): number => {\n        return\
        \ ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1];\n    };\n\
        \n    // Helper function to check if a square of side length k exists\n    const\
        \ check = (k: number): boolean => {\n        if (k === 0) return true; // A\
        \ 0x0 square always has sum 0 <= threshold\n        for (let r = 0; r <= m -\
        \ k; ++r) {\n            for (let c = 0; c <= n - k; ++c) {\n              \
        \  if (getSquareSum(r, c, r + k - 1, c + k - 1) <= threshold) {\n          \
        \          return true;\n                }\n            }\n        }\n     \
        \   return false;\n    };\n\n    let low = 0;\n    let high = Math.min(m, n);\n\
        \    let ans = 0;\n\n    while (low <= high) {\n        let mid = Math.floor(low\
        \ + (high - low) / 2);\n        if (check(mid)) {\n            ans = mid;\n\
        \            low = mid + 1;\n        } else {\n            high = mid - 1;\n\
        \        }\n    }\n\n    return ans;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $mat\n     * @param\
        \ Integer $threshold\n     * @return Integer\n     */\n    function maxSideLength($mat,\
        \ $threshold) {\n        $m = count($mat);\n        $n = count($mat[0]);\n\n\
        \        $ps = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));\n\n        for\
        \ ($i = 0; $i < $m; ++$i) {\n            for ($j = 0; $j < $n; ++$j) {\n   \
        \             $ps[$i + 1][$j + 1] = $mat[$i][$j] + $ps[$i][$j + 1] + $ps[$i\
        \ + 1][$j] - $ps[$i][$j];\n            }\n        }\n\n        // Helper function\
        \ to get sum of a square from (r1, c1) to (r2, c2)\n        // Note: r1, c1,\
        \ r2, c2 are 0-indexed for the original matrix\n        // ps array is 1-indexed\
        \ for convenience\n        $getSquareSum = function($r1, $c1, $r2, $c2) use\
        \ ($ps) {\n            return $ps[$r2 + 1][$c2 + 1] - $ps[$r1][$c2 + 1] - $ps[$r2\
        \ + 1][$c1] + $ps[$r1][$c1];\n        };\n\n        // Helper function to check\
        \ if a square of side length k exists\n        $check = function($k) use ($m,\
        \ $n, $threshold, $getSquareSum) {\n            if ($k == 0) return true; //\
        \ A 0x0 square always has sum 0 <= threshold\n            for ($r = 0; $r <=\
        \ $m - $k; ++$r) {\n                for ($c = 0; $c <= $n - $k; ++$c) {\n  \
        \                  if ($getSquareSum($r, $c, $r + $k - 1, $c + $k - 1) <= $threshold)\
        \ {\n                        return true;\n                    }\n         \
        \       }\n            }\n            return false;\n        };\n\n        $low\
        \ = 0;\n        $high = min($m, $n);\n        $ans = 0;\n\n        while ($low\
        \ <= $high) {\n            $mid = floor($low + ($high - $low) / 2);\n      \
        \      if ($check($mid)) {\n                $ans = $mid;\n                $low\
        \ = $mid + 1;\n            } else {\n                $high = $mid - 1;\n   \
        \         }\n        }\n\n        return $ans;\n    }\n}"
      swift: "class Solution {\n    func maxSideLength(_ mat: [[Int]], _ threshold:\
        \ Int) -> Int {\n        let m = mat.count\n        let n = mat[0].count\n\n\
        \        var ps = Array(repeating: Array(repeating: 0, count: n + 1), count:\
        \ m + 1)\n\n        for i in 0..<m {\n            for j in 0..<n {\n       \
        \         ps[i + 1][j + 1] = mat[i][j] + ps[i][j + 1] + ps[i + 1][j] - ps[i][j]\n\
        \            }\n        }\n\n        // Helper function to get sum of a square\
        \ from (r1, c1) to (r2, c2)\n        // Note: r1, c1, r2, c2 are 0-indexed for\
        \ the original matrix\n        // ps array is 1-indexed for convenience\n  \
        \      func getSquareSum(_ r1: Int, _ c1: Int, _ r2: Int, _ c2: Int) -> Int\
        \ {\n            return ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1]\
        \ + ps[r1][c1]\n        }\n\n        // Helper function to check if a square\
        \ of side length k exists\n        func check(_ k: Int) -> Bool {\n        \
        \    if k == 0 { return true } // A 0x0 square always has sum 0 <= threshold\n\
        \            for r in 0...(m - k) {\n                for c in 0...(n - k) {\n\
        \                    if getSquareSum(r, c, r + k - 1, c + k - 1) <= threshold\
        \ {\n                        return true\n                    }\n          \
        \      }\n            }\n            return false\n        }\n\n        var\
        \ low = 0\n        var high = min(m, n)\n        var ans = 0\n\n        while\
        \ low <= high {\n            let mid = low + (high - low) / 2\n            if\
        \ check(mid) {\n                ans = mid\n                low = mid + 1\n \
        \           } else {\n                high = mid - 1\n            }\n      \
        \  }\n\n        return ans\n    }\n}"
      kotlin: "class Solution {\n    fun maxSideLength(mat: Array<IntArray>, threshold:\
        \ Int): Int {\n        val m = mat.size\n        val n = mat[0].size\n\n   \
        \     val ps = Array(m + 1) { IntArray(n + 1) }\n        for (r in 0 until m)\
        \ {\n            for (c in 0 until n) {\n                ps[r + 1][c + 1] =\
        \ mat[r][c] + ps[r][c + 1] + ps[r + 1][c] - ps[r][c]\n            }\n      \
        \  }\n\n        fun getSquareSum(r1: Int, c1: Int, k: Int): Int {\n        \
        \    val r2 = r1 + k - 1\n            val c2 = c1 + k - 1\n            return\
        \ ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1]\n      \
        \  }\n\n        fun check(k: Int): Boolean {\n            if (k == 0) return\
        \ true\n            if (k > m || k > n) return false\n\n            for (r in\
        \ 0..(m - k)) {\n                for (c in 0..(n - k)) {\n                 \
        \   if (getSquareSum(r, c, k) <= threshold) {\n                        return\
        \ true\n                    }\n                }\n            }\n          \
        \  return false\n        }\n\n        var low = 0\n        var high = Math.min(m,\
        \ n)\n        var ans = 0\n\n        while (low <= high) {\n            val\
        \ mid = low + (high - low) / 2\n            if (check(mid)) {\n            \
        \    ans = mid\n                low = mid + 1\n            } else {\n      \
        \          high = mid - 1\n            }\n        }\n\n        return ans\n\
        \    }\n}"
      dart: "class Solution {\n  int maxSideLength(List<List<int>> mat, int threshold)\
        \ {\n    final m = mat.length;\n    final n = mat[0].length;\n\n    final ps\
        \ = List.generate(m + 1, (_) => List.filled(n + 1, 0));\n    for (var r = 0;\
        \ r < m; r++) {\n      for (var c = 0; c < n; c++) {\n        ps[r + 1][c +\
        \ 1] = mat[r][c] + ps[r][c + 1] + ps[r + 1][c] - ps[r][c];\n      }\n    }\n\
        \n    int getSquareSum(int r1, int c1, int k) {\n      final r2 = r1 + k - 1;\n\
        \      final c2 = c1 + k - 1;\n      return ps[r2 + 1][c2 + 1] - ps[r1][c2 +\
        \ 1] - ps[r2 + 1][c1] + ps[r1][c1];\n    }\n\n    bool check(int k) {\n    \
        \  if (k == 0) return true;\n      if (k > m || k > n) return false;\n\n   \
        \   for (var r = 0; r <= (m - k); r++) {\n        for (var c = 0; c <= (n -\
        \ k); c++) {\n          if (getSquareSum(r, c, k) <= threshold) {\n        \
        \    return true;\n          }\n        }\n      }\n      return false;\n  \
        \  }\n\n    var low = 0;\n    var high = m < n ? m : n;\n    var ans = 0;\n\n\
        \    while (low <= high) {\n      final mid = low + (high - low) ~/ 2;\n   \
        \   if (check(mid)) {\n        ans = mid;\n        low = mid + 1;\n      } else\
        \ {\n        high = mid - 1;\n      }\n    }\n\n    return ans;\n  }\n}"
      go: "func maxSideLength(mat [][]int, threshold int) int {\n    m := len(mat)\n\
        \    n := len(mat[0])\n\n    ps := make([][]int, m+1)\n    for i := range ps\
        \ {\n        ps[i] = make([]int, n+1)\n    }\n\n    for r := 0; r < m; r++ {\n\
        \        for c := 0; c < n; c++ {\n            ps[r+1][c+1] = mat[r][c] + ps[r][c+1]\
        \ + ps[r+1][c] - ps[r][c]\n        }\n    }\n\n    getSquareSum := func(r1,\
        \ c1, k int) int {\n        r2 := r1 + k - 1\n        c2 := c1 + k - 1\n   \
        \     return ps[r2+1][c2+1] - ps[r1][c2+1] - ps[r2+1][c1] + ps[r1][c1]\n   \
        \ }\n\n    check := func(k int) bool {\n        if k == 0 {\n            return\
        \ true\n        }\n        if k > m || k > n {\n            return false\n \
        \       }\n\n        for r := 0; r <= (m - k); r++ {\n            for c := 0;\
        \ c <= (n - k); c++ {\n                if getSquareSum(r, c, k) <= threshold\
        \ {\n                    return true\n                }\n            }\n   \
        \     }\n        return false\n    }\n\n    low := 0\n    high := min(m, n)\n\
        \    ans := 0\n\n    for low <= high {\n        mid := low + (high - low) /\
        \ 2\n        if check(mid) {\n            ans = mid\n            low = mid +\
        \ 1\n        } else {\n            high = mid - 1\n        }\n    }\n\n    return\
        \ ans\n}\n\nfunc min(a, b int) int {\n    if a < b {\n        return a\n   \
        \ }\n    return b\n}"
      ruby: "# @param {Integer[][]} mat\n# @param {Integer} threshold\n# @return {Integer}\n\
        def max_side_length(mat, threshold)\n    m = mat.length\n    n = mat[0].length\n\
        \n    ps = Array.new(m + 1) { Array.new(n + 1, 0) }\n    (0...m).each do |r|\n\
        \        (0...n).each do |c|\n            ps[r + 1][c + 1] = mat[r][c] + ps[r][c\
        \ + 1] + ps[r + 1][c] - ps[r][c]\n        end\n    end\n\n    get_square_sum\
        \ = lambda do |r1, c1, k|\n        r2 = r1 + k - 1\n        c2 = c1 + k - 1\n\
        \        ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1]\n\
        \    end\n\n    check = lambda do |k|\n        return true if k == 0\n     \
        \   return false if k > m || k > n\n\n        (0..(m - k)).each do |r|\n   \
        \         (0..(n - k)).each do |c|\n                if get_square_sum.call(r,\
        \ c, k) <= threshold\n                    return true\n                end\n\
        \            end\n        end\n        false\n    end\n\n    low = 0\n    high\
        \ = [m, n].min\n    ans = 0\n\n    while low <= high\n        mid = low + (high\
        \ - low) / 2\n        if check.call(mid)\n            ans = mid\n          \
        \  low = mid + 1\n        else\n            high = mid - 1\n        end\n  \
        \  end\n\n    ans\nend"
      scala: "object Solution {\n    def maxSideLength(mat: Array[Array[Int]], threshold:\
        \ Int): Int = {\n        val m = mat.length\n        val n = mat(0).length\n\
        \n        val ps = Array.ofDim[Int](m + 1, n + 1)\n        for (r <- 0 until\
        \ m) {\n            for (c <- 0 until n) {\n                ps(r + 1)(c + 1)\
        \ = mat(r)(c) + ps(r)(c + 1) + ps(r + 1)(c) - ps(r)(c)\n            }\n    \
        \    }\n\n        def getSquareSum(r1: Int, c1: Int, k: Int): Int = {\n    \
        \        val r2 = r1 + k - 1\n            val c2 = c1 + k - 1\n            ps(r2\
        \ + 1)(c2 + 1) - ps(r1)(c2 + 1) - ps(r2 + 1)(c1) + ps(r1)(c1)\n        }\n\n\
        \        def check(k: Int): Boolean = {\n            if (k == 0) return true\n\
        \            if (k > m || k > n) return false\n\n            for (r <- 0 to\
        \ (m - k)) {\n                for (c <- 0 to (n - k)) {\n                  \
        \  if (getSquareSum(r, c, k) <= threshold) {\n                        return\
        \ true\n                    }\n                }\n            }\n          \
        \  false\n        }\n\n        var low = 0\n        var high = Math.min(m, n)\n\
        \        var ans = 0\n\n        while (low <= high) {\n            val mid =\
        \ low + (high - low) / 2\n            if (check(mid)) {\n                ans\
        \ = mid\n                low = mid + 1\n            } else {\n             \
        \   high = mid - 1\n            }\n        }\n\n        ans\n    }\n}"
      rust: "impl Solution {\n    pub fn max_side_length(mat: Vec<Vec<i32>>, threshold:\
        \ i32) -> i32 {\n        let m = mat.len();\n        let n = mat[0].len();\n\
        \n        let mut ps = vec![vec![0; n + 1]; m + 1];\n        for r in 0..m {\n\
        \            for c in 0..n {\n                ps[r + 1][c + 1] = mat[r][c] +\
        \ ps[r][c + 1] + ps[r + 1][c] - ps[r][c];\n            }\n        }\n\n    \
        \    let get_square_sum = |r1: usize, c1: usize, k: usize| -> i32 {\n      \
        \      let r2 = r1 + k - 1;\n            let c2 = c1 + k - 1;\n            ps[r2\
        \ + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1]\n        };\n\n\
        \        let check = |k: usize| -> bool {\n            if k == 0 {\n       \
        \         return true;\n            }\n            if k > m || k > n {\n   \
        \             return false;\n            }\n\n            for r in 0..=(m -\
        \ k) {\n                for c in 0..=(n - k) {\n                    if get_square_sum(r,\
        \ c, k) <= threshold {\n                        return true;\n             \
        \       }\n                }\n            }\n            false\n        };\n\
        \n        let mut low = 0;\n        let mut high = std::cmp::min(m, n);\n  \
        \      let mut ans = 0;\n\n        while low <= high {\n            let mid\
        \ = low + (high - low) / 2;\n            if check(mid) {\n                ans\
        \ = mid;\n                low = mid + 1;\n            } else {\n           \
        \     high = mid - 1;\n            }\n        }\n\n        ans as i32\n    }\n\
        }"
      racket: "(define/contract (max-side-length mat threshold)\n  (-> (listof (listof\
        \ exact-integer?)) exact-integer? exact-integer?)\n  (let* ([m (length mat)]\n\
        \         [n (length (car mat))]\n         [ps (build-vector (+ m 1) (lambda\
        \ (_) (build-vector (+ n 1) (lambda (_) 0))))])\n\n    (for* ([r (in-range m)]\n\
        \           [c (in-range n)])\n      (vector-set! (vector-ref ps (+ r 1)) (+\
        \ c 1)\n                   (+ (list-ref (list-ref mat r) c)\n              \
        \        (vector-ref (vector-ref ps r) (+ c 1))\n                      (vector-ref\
        \ (vector-ref ps (+ r 1)) c)\n                      (- (vector-ref (vector-ref\
        \ ps r) c))))))\n\n    (define (get-square-sum r1 c1 k)\n      (let* ([r2 (+\
        \ r1 k -1)]\n             [c2 (+ c1 k -1)])\n        (+ (vector-ref (vector-ref\
        \ ps (+ r2 1)) (+ c2 1))\n           (- (vector-ref (vector-ref ps r1) (+ c2\
        \ 1)))\n           (- (vector-ref (vector-ref ps (+ r2 1)) c1))\n          \
        \ (vector-ref (vector-ref ps r1) c1))))\n\n    (define (check k)\n      (cond\n\
        \        [(= k 0) #t]\n        [(or (> k m) (> k n)) #f]\n        [else\n  \
        \       (let loop ([r 0])\n           (cond\n             [(> r (- m k)) #f]\n\
        \             [else\n              (let loop-inner ([c 0])\n               \
        \ (cond\n                  [(> c (- n k)) (loop (+ r 1))]\n                \
        \  [else\n                   (if (<= (get-square-sum r c k) threshold)\n   \
        \                    #t\n                       (loop-inner (+ c 1)))]))]))]))\n\
        \n    (let loop-bs ([low 0] [high (min m n)] [ans 0])\n      (if (> low high)\n\
        \          ans\n          (let ([mid (+ low (quotient (- high low) 2))])\n \
        \           (if (check mid)\n                (loop-bs (+ mid 1) high mid)\n\
        \                (loop-bs low (- mid 1) ans)))))))"
      erlang: "-spec max_side_length(Mat :: [[integer()]], Threshold :: integer()) ->\
        \ integer().\nmax_side_length(Mat, Threshold) ->\n  M = length(Mat),\n  N =\
        \ length(hd(Mat)),\n\n  InitialRow = array:new([{size, N + 1}, {fixed, true},\
        \ {default, 0}]),\n  PsArray = array:new([{size, M + 1}, {fixed, true}, {default,\
        \ InitialRow}]),\n\n  PsArrayFinal = build_ps_array(Mat, M, N, PsArray),\n\n\
        \  GetSquareSum = fun(R1, C1, K) ->\n    R2 = R1 + K - 1,\n    C2 = C1 + K -\
        \ 1,\n    array:get(C2 + 1, array:get(R2 + 1, PsArrayFinal))\n    - array:get(C2\
        \ + 1, array:get(R1, PsArrayFinal))\n    - array:get(C1, array:get(R2 + 1, PsArrayFinal))\n\
        \    + array:get(C1, array:get(R1, PsArrayFinal))\n  end,\n\n  Check = fun\n\
        \    (0) -> true;\n    (K) when K > M; K > N -> false;\n    (K) ->\n      lists:any(\n\
        \        fun(R) ->\n          lists:any(\n            fun(C) ->\n          \
        \    GetSquareSum(R, C, K) =< Threshold\n            end,\n            lists:seq(0,\
        \ N - K)\n          )\n        end,\n        lists:seq(0, M - K)\n      )\n\
        \  end,\n\n  Low = 0,\n  High = min(M, N),\n  binary_search_erlang(Low, High,\
        \ 0, Check).\n\nbinary_search_erlang(Low, High, Ans, Check) ->\n  if\n    Low\
        \ > High -> Ans;\n    true ->\n      Mid = Low + (High - Low) div 2,\n     \
        \ if\n        Check(Mid) -> binary_search_erlang(Mid + 1, High, Mid, Check);\n\
        \        true -> binary_search_erlang(Low, Mid - 1, Ans, Check)\n      end\n\
        \  end.\n\nbuild_ps_array(Mat, M, N, PsArray) ->\n  build_ps_array_rows(Mat,\
        \ M, N, 0, PsArray).\n\nbuild_ps_array_rows(_Mat, M, _N, M, PsArray) ->\n  PsArray;\n\
        build_ps_array_rows(Mat, M, N, R_idx, AccPsArray) ->\n  CurrentMatRow = lists:nth(R_idx\
        \ + 1, Mat),\n\n  PrevPsRowArray = array:get(R_idx, AccPsArray),\n  CurrentPsRowArray\
        \ = array:get(R_idx + 1, AccPsArray),\n\n  UpdatedCurrentPsRowArray = build_current_ps_array_row(CurrentMatRow,\
        \ PrevPsRowArray, CurrentPsRowArray, N, 0),\n\n  NewPsArray = array:set(R_idx\
        \ + 1, UpdatedCurrentPsRowArray, AccPsArray),\n  build_ps_array_rows(Mat, M,\
        \ N, R_idx + 1, NewPsArray).\n\nbuild_current_ps_array_row(_CurrentMatRow, _PrevPsRowArray,\
        \ CurrentPsRowArray, N, N) ->\n  CurrentPsRowArray;\nbuild_current_ps_array_row(CurrentMatRow,\
        \ PrevPsRowArray, CurrentPsRowArray, N, C_idx) ->\n  MatVal = lists:nth(C_idx\
        \ + 1, CurrentMatRow),\n\n  PsPrevRowCurrentCol = array:get(C_idx + 1, PrevPsRowArray),\n\
        \  PsCurrentRowPrevCol = array:get(C_idx, CurrentPsRowArray),\n  PsPrevRowPrevCol\
        \ = array:get(C_idx, PrevPsRowArray),\n\n  NewSum = MatVal + PsPrevRowCurrentCol\
        \ + PsCurrentRowPrevCol - PsPrevRowPrevCol,\n\n  UpdatedCurrentPsRowArray =\
        \ array:set(C_idx + 1, NewSum, CurrentPsRowArray),\n  build_current_ps_array_row(CurrentMatRow,\
        \ PrevPsRowArray, UpdatedCurrentPsRowArray, N, C_idx + 1)."
      elixir: "defmodule Solution do\n  @spec max_side_length(mat :: [[integer]], threshold\
        \ :: integer) :: integer\n  def max_side_length(mat, threshold) do\n    m =\
        \ length(mat)\n    n = length(hd(mat))\n\n    ps_matrix = build_ps_map(mat,\
        \ m, n)\n\n    get_square_sum = fn r1, c1, k ->\n      r2 = r1 + k - 1\n   \
        \   c2 = c1 + k - 1\n      Map.get(Map.get(ps_matrix, r2 + 1), c2 + 1) -\n \
        \       Map.get(Map.get(ps_matrix, r1), c2 + 1) -\n        Map.get(Map.get(ps_matrix,\
        \ r2 + 1), c1) +\n        Map.get(Map.get(ps_matrix, r1), c1)\n    end\n\n \
        \   check = fn k ->\n      cond do\n        k == 0 -> true\n        k > m or\
        \ k > n -> false\n        true ->\n          0..(m - k)\n          |> Enum.any?(fn\
        \ r ->\n            0..(n - k)\n            |> Enum.any?(fn c ->\n         \
        \     get_square_sum.(r, c, k) <= threshold\n            end)\n          end)\n\
        \      end\n    end\n\n    low = 0\n    high = min(m, n)\n    ans = 0\n\n  \
        \  binary_search(low, high, ans, check)\n  end\n\n  defp binary_search(low,\
        \ high, ans, check) when low > high, do: ans\n  defp binary_search(low, high,\
        \ ans, check) do\n    mid = low + div(high - low, 2)\n    if check.(mid) do\n\
        \      binary_search(mid + 1, high, mid, check)\n    else\n      binary_search(low,\
        \ mid - 1, ans, check)\n    end\n  end\n\n  defp build_ps_map(mat, m, n) do\n\
        \    initial_ps_map = %{0 => Map.new(0..n, fn c -> {c, 0} end)}\n    build_ps_rows_map(mat,\
        \ m, n, 0, initial_ps_map)\n  end\n\n  defp build_ps_rows_map(_mat, m, _n, m,\
        \ ps_map), do: ps_map\n  defp build_ps_rows_map(mat, m, n, r_idx, acc_ps_map)\
        \ do\n    current_mat_row = Enum.at(mat, r_idx)\n\n    current_ps_row_map =\
        \ build_current_ps_row_map(current_mat_row, acc_ps_map, r_idx, n, 0, %{0 =>\
        \ 0})\n\n    build_ps_rows_map(mat, m, n, r_idx + 1, Map.put(acc_ps_map, r_idx\
        \ + 1, current_ps_row_map))\n  end\n\n  defp build_current_ps_row_map(_current_mat_row,\
        \ _acc_ps_map, _r_idx, n, n, acc_current_ps_row_map), do: acc_current_ps_row_map\n\
        \  defp build_current_ps_row_map(current_mat_row, acc_ps_map, r_idx, n, c_idx,\
        \ acc_current_ps_row_map) do\n    mat_val = Enum.at(current_mat_row, c_idx)\n\
        \n    ps_prev_row_current_col = Map.get(Map.get(acc_ps_map, r_idx), c_idx +\
        \ 1)\n    ps_current_row_prev_col = Map.get(acc_current_ps_row_map, c_idx)\n\
        \    ps_prev_row_prev_col = Map.get(Map.get(acc_ps_map, r_idx), c_idx)\n\n \
        \   new_sum = mat_val + ps_prev_row_current_col + ps_current_row_prev_col -\
        \ ps_prev_row_prev_col\n\n    build_current_ps_row_map(current_mat_row, acc_ps_map,\
        \ r_idx, n, c_idx + 1, Map.put(acc_current_ps_row_map, c_idx + 1, new_sum))\n\
        \  end\nend"
    approach: 'The problem asks for the maximum side-length of a square submatrix whose
      sum is less than or equal to a given threshold. This problem exhibits a monotonic
      property: if a square of side-length ''k'' satisfies the condition, then any square
      of side-length ''k'''' where k'' < k will also satisfy the condition (since all
      matrix elements are non-negative). This monotonicity allows us to use binary search
      on the possible side-lengths, which range from 0 to min(m, n).


      To efficiently check if a square of a given side-length ''k'' exists with a sum
      less than or equal to the threshold, we first precompute a 2D prefix sum array
      (also known as an integral image). This array, `ps[i][j]`, stores the sum of all
      elements in the rectangle from `(0,0)` to `(i-1, j-1)`. With this prefix sum array,
      the sum of any sub-rectangle (including a square) can be calculated in O(1) time.
      The binary search repeatedly calls a `check(k)` function. This function iterates
      through all possible top-left corners `(r, c)` for a square of side `k` and uses
      the prefix sum array to calculate its sum. If any square''s sum is within the
      threshold, `check(k)` returns true; otherwise, it returns false. The binary search
      then adjusts its range (low or high) based on the result of `check(k)` to find
      the largest valid `k`.'
    time_complexity: 'The time complexity is dominated by two parts: building the prefix
      sum array and the binary search. Building the prefix sum array takes O(m*n) time.
      The binary search performs O(log(min(m, n))) iterations. In each iteration, the
      `check(k)` function iterates through all possible top-left corners for a square
      of side `k`, which is approximately (m-k+1) * (n-k+1) operations. Each sum calculation
      is O(1) using the prefix sum array. Thus, `check(k)` takes O(m*n) time. Combining
      these, the total time complexity is O(m*n + log(min(m, n)) * m*n), which simplifies
      to O(m*n * log(min(m, n))).'
    space_complexity: The space complexity is determined by the 2D prefix sum array,
      which requires O(m*n) additional space to store the sums for all sub-rectangles.
      No other significant data structures are used that would exceed this complexity.
    elapsed_time: 186.13848543167114
    model: gemini-2.5-flash
    generated_at: '2026-01-19 01:17:12 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxSideLength(vector<vector<int>>& mat,\
        \ int threshold) {\n        int m = mat.size();\n        int n = mat[0].size();\n\
        \        vector<vector<int>> prefix(m + 1, vector<int>(n + 1, 0));\n       \
        \ for (int i = 1; i <= m; i++) {\n            for (int j = 1; j <= n; j++) {\n\
        \                prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i\
        \ - 1][j - 1] + mat[i - 1][j - 1];\n            }\n        }\n        int low\
        \ = 0;\n        int high = min(m, n);\n        while (low <= high) {\n     \
        \       int mid = low + (high - low) / 2;\n            bool found = false;\n\
        \            for (int i = 0; i <= m - mid; i++) {\n                for (int\
        \ j = 0; j <= n - mid; j++) {\n                    int sum = prefix[i + mid][j\
        \ + mid] - prefix[i + mid][j] - prefix[i][j + mid] + prefix[i][j];\n       \
        \             if (sum <= threshold) {\n                        found = true;\n\
        \                        break;\n                    }\n                }\n\
        \                if (found) break;\n            }\n            if (found) low\
        \ = mid + 1;\n            else high = mid - 1;\n        }\n        return high;\n\
        \    }\n};"
      java: "class Solution {\n    public int maxSideLength(int[][] mat, int threshold)\
        \ {\n        int m = mat.length;\n        int n = mat[0].length;\n        int[][]\
        \ prefix = new int[m + 1][n + 1];\n        for (int i = 1; i <= m; i++) {\n\
        \            for (int j = 1; j <= n; j++) {\n                prefix[i][j] =\
        \ prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + mat[i - 1][j\
        \ - 1];\n            }\n        }\n        int low = 0;\n        int high =\
        \ Math.min(m, n);\n        while (low <= high) {\n            int mid = low\
        \ + (high - low) / 2;\n            boolean found = false;\n            for (int\
        \ i = 0; i <= m - mid; i++) {\n                for (int j = 0; j <= n - mid;\
        \ j++) {\n                    int sum = prefix[i + mid][j + mid] - prefix[i\
        \ + mid][j] - prefix[i][j + mid] + prefix[i][j];\n                    if (sum\
        \ <= threshold) {\n                        found = true;\n                 \
        \       break;\n                    }\n                }\n                if\
        \ (found) break;\n            }\n            if (found) low = mid + 1;\n   \
        \         else high = mid - 1;\n        }\n        return high;\n    }\n}"
      python: "class Solution:\n    def maxSideLength(self, mat, threshold):\n     \
        \   m, n = len(mat), len(mat[0])\n        prefix = [[0] * (n + 1) for _ in range(m\
        \ + 1)]\n        for i in range(1, m + 1):\n            for j in range(1, n\
        \ + 1):\n                prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1]\
        \ - prefix[i - 1][j - 1] + mat[i - 1][j - 1]\n        low, high = 0, min(m,\
        \ n)\n        while low <= high:\n            mid = (low + high) // 2\n    \
        \        found = False\n            for i in range(m - mid + 1):\n         \
        \       for j in range(n - mid + 1):\n                    sum = prefix[i + mid][j\
        \ + mid] - prefix[i + mid][j] - prefix[i][j + mid] + prefix[i][j]\n        \
        \            if sum <= threshold:\n                        found = True\n  \
        \                      break\n                if found: break\n            if\
        \ found: low = mid + 1\n            else: high = mid - 1\n        return high"
      python3: "class Solution:\n    def maxSideLength(self, mat: list[list[int]], threshold:\
        \ int) -> int:\n        m, n = len(mat), len(mat[0])\n        prefix = [[0]\
        \ * (n + 1) for _ in range(m + 1)]\n        for i in range(1, m + 1):\n    \
        \        for j in range(1, n + 1):\n                prefix[i][j] = prefix[i\
        \ - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + mat[i - 1][j - 1]\n  \
        \      low, high = 0, min(m, n)\n        while low <= high:\n            mid\
        \ = (low + high) // 2\n            found = False\n            for i in range(m\
        \ - mid + 1):\n                for j in range(n - mid + 1):\n              \
        \      sum = prefix[i + mid][j + mid] - prefix[i + mid][j] - prefix[i][j + mid]\
        \ + prefix[i][j]\n                    if sum <= threshold:\n               \
        \         found = True\n                        break\n                if found:\
        \ break\n            if found: low = mid + 1\n            else: high = mid -\
        \ 1\n        return high"
      c: "int maxSideLength(int** mat, int matSize, int* matColSize, int threshold)\
        \ {\n    int m = matSize;\n    int n = matColSize[0];\n    int** prefix = (int**)malloc((m\
        \ + 1) * sizeof(int*));\n    for (int i = 0; i <= m; i++) {\n        prefix[i]\
        \ = (int*)malloc((n + 1) * sizeof(int));\n    }\n    for (int i = 1; i <= m;\
        \ i++) {\n        for (int j = 1; j <= n; j++) {\n            prefix[i][j] =\
        \ prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + mat[i - 1][j\
        \ - 1];\n        }\n    }\n    int low = 0;\n    int high = (m < n) ? m : n;\n\
        \    while (low <= high) {\n        int mid = low + (high - low) / 2;\n    \
        \    int found = 0;\n        for (int i = 0; i <= m - mid; i++) {\n        \
        \    for (int j = 0; j <= n - mid; j++) {\n                int sum = prefix[i\
        \ + mid][j + mid] - prefix[i + mid][j] - prefix[i][j + mid] + prefix[i][j];\n\
        \                if (sum <= threshold) {\n                    found = 1;\n \
        \                   break;\n                }\n            }\n            if\
        \ (found) break;\n        }\n        if (found) low = mid + 1;\n        else\
        \ high = mid - 1;\n    }\n    return high;\n}"
      csharp: "public class Solution {\n    public int MaxSideLength(int[][] mat, int\
        \ threshold) {\n        int m = mat.Length;\n        int n = mat[0].Length;\n\
        \        int[][] prefix = new int[m + 1][];\n        for (int i = 0; i <= m;\
        \ i++) {\n            prefix[i] = new int[n + 1];\n        }\n        for (int\
        \ i = 1; i <= m; i++) {\n            for (int j = 1; j <= n; j++) {\n      \
        \          prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j\
        \ - 1] + mat[i - 1][j - 1];\n            }\n        }\n        int low = 0;\n\
        \        int high = Math.Min(m, n);\n        while (low <= high) {\n       \
        \     int mid = low + (high - low) / 2;\n            bool found = false;\n \
        \           for (int i = 0; i <= m - mid; i++) {\n                for (int j\
        \ = 0; j <= n - mid; j++) {\n                    int sum = prefix[i + mid][j\
        \ + mid] - prefix[i + mid][j] - prefix[i][j + mid] + prefix[i][j];\n       \
        \             if (sum <= threshold) {\n                        found = true;\n\
        \                        break;\n                    }\n                }\n\
        \                if (found) break;\n            }\n            if (found) low\
        \ = mid + 1;\n            else high = mid - 1;\n        }\n        return high;\n\
        \    }\n}"
      javascript: "var maxSideLength = function(mat, threshold) {\n    let m = mat.length;\n\
        \    let n = mat[0].length;\n    let prefix = Array(m + 1).fill(0).map(() =>\
        \ Array(n + 1).fill(0));\n    for (let i = 1; i <= m; i++) {\n        for (let\
        \ j = 1; j <= n; j++) {\n            prefix[i][j] = prefix[i - 1][j] + prefix[i][j\
        \ - 1] - prefix[i - 1][j - 1] + mat[i - 1][j - 1];\n        }\n    }\n    let\
        \ low = 0;\n    let high = Math.min(m, n);\n    while (low <= high) {\n    \
        \    let mid = low + Math.floor((high - low) / 2);\n        let found = false;\n\
        \        for (let i = 0; i <= m - mid; i++) {\n            for (let j = 0; j\
        \ <= n - mid; j++) {\n                let sum = prefix[i + mid][j + mid] - prefix[i\
        \ + mid][j] - prefix[i][j + mid] + prefix[i][j];\n                if (sum <=\
        \ threshold) {\n                    found = true;\n                    break;\n\
        \                }\n            }\n            if (found) break;\n        }\n\
        \        if (found) low = mid + 1;\n        else high = mid - 1;\n    }\n  \
        \  return high;\n};"
      typescript: "function maxSideLength(mat: number[][], threshold: number): number\
        \ {\n    let m: number = mat.length;\n    let n: number = mat[0].length;\n \
        \   let prefix: number[][] = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));\n\
        \    for (let i = 1; i <= m; i++) {\n        for (let j = 1; j <= n; j++) {\n\
        \            prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i -\
        \ 1][j - 1] + mat[i - 1][j - 1];\n        }\n    }\n    let low: number = 0;\n\
        \    let high: number = Math.min(m, n);\n    while (low <= high) {\n       \
        \ let mid: number = low + Math.floor((high - low) / 2);\n        let found:\
        \ boolean = false;\n        for (let i = 0; i <= m - mid; i++) {\n         \
        \   for (let j = 0; j <= n - mid; j++) {\n                let sum: number =\
        \ prefix[i + mid][j + mid] - prefix[i + mid][j] - prefix[i][j + mid] + prefix[i][j];\n\
        \                if (sum <= threshold) {\n                    found = true;\n\
        \                    break;\n                }\n            }\n            if\
        \ (found) break;\n        }\n        if (found) low = mid + 1;\n        else\
        \ high = mid - 1;\n    }\n    return high;\n}"
      php: "class Solution {\n    function maxSideLength($mat, $threshold) {\n     \
        \   $m = count($mat);\n        $n = count($mat[0]);\n        $prefix = array_fill(0,\
        \ $m + 1, array_fill(0, $n + 1, 0));\n        for ($i = 1; $i <= $m; $i++) {\n\
        \            for ($j = 1; $j <= $n; $j++) {\n                $prefix[$i][$j]\
        \ = $prefix[$i - 1][$j] + $prefix[$i][$j - 1] - $prefix[$i - 1][$j - 1] + $mat[$i\
        \ - 1][$j - 1];\n            }\n        }\n        $low = 0;\n        $high\
        \ = min($m, $n);\n        while ($low <= $high) {\n            $mid = $low +\
        \ floor(($high - $low) / 2);\n            $found = false;\n            for ($i\
        \ = 0; $i <= $m - $mid; $i++) {\n                for ($j = 0; $j <= $n - $mid;\
        \ $j++) {\n                    $sum = $prefix[$i + $mid][$j + $mid] - $prefix[$i\
        \ + $mid][$j] - $prefix[$i][$j + $mid] + $prefix[$i][$j];\n                \
        \    if ($sum <= $threshold) {\n                        $found = true;\n   \
        \                     break;\n                    }\n                }\n   \
        \             if ($found) break;\n            }\n            if ($found) $low\
        \ = $mid + 1;\n            else $high = $mid - 1;\n        }\n        return\
        \ $high;\n    }\n}"
      swift: "class Solution {\n    func maxSideLength(_ mat: [[Int]], _ threshold:\
        \ Int) -> Int {\n        let m = mat.count\n        let n = mat[0].count\n \
        \       var prefix = Array(repeating: Array(repeating: 0, count: n + 1), count:\
        \ m + 1)\n        for i in 1...m {\n            for j in 1...n {\n         \
        \       prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j\
        \ - 1] + mat[i - 1][j - 1]\n            }\n        }\n        var low = 0\n\
        \        var high = min(m, n)\n        while low <= high {\n            let\
        \ mid = low + (high - low) / 2\n            var found = false\n            for\
        \ i in 0...m - mid {\n                for j in 0...n - mid {\n             \
        \       let sum = prefix[i + mid][j + mid] - prefix[i + mid][j] - prefix[i][j\
        \ + mid] + prefix[i][j]\n                    if sum <= threshold {\n       \
        \                 found = true\n                        break\n            \
        \        }\n                }\n                if found { break }\n        \
        \    }\n            if found { low = mid + 1 }\n            else { high = mid\
        \ - 1 }\n        }\n        return high\n    }\n}"
      kotlin: "class Solution {\n    fun maxSideLength(mat: Array<IntArray>, threshold:\
        \ Int): Int {\n        val m = mat.size\n        val n = mat[0].size\n     \
        \   val prefixSum = Array(m + 1) { IntArray(n + 1) }\n        for (i in 1..m)\
        \ {\n            for (j in 1..n) {\n                prefixSum[i][j] = prefixSum[i\
        \ - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1] + mat[i - 1][j - 1]\n\
        \            }\n        }\n        var low = 1\n        var high = minOf(m,\
        \ n)\n        var ans = 0\n        while (low <= high) {\n            val mid\
        \ = (low + high) / 2\n            if (possible(mat, prefixSum, threshold, mid))\
        \ {\n                ans = mid\n                low = mid + 1\n            }\
        \ else {\n                high = mid - 1\n            }\n        }\n       \
        \ return ans\n    }\n\n    fun possible(mat: Array<IntArray>, prefixSum: Array<IntArray>,\
        \ threshold: Int, side: Int): Boolean {\n        val m = mat.size\n        val\
        \ n = mat[0].size\n        for (i in 0 until m - side + 1) {\n            for\
        \ (j in 0 until n - side + 1) {\n                val sum = prefixSum[i + side][j\
        \ + side] - prefixSum[i + side][j] - prefixSum[i][j + side] + prefixSum[i][j]\n\
        \                if (sum <= threshold) return true\n            }\n        }\n\
        \        return false\n    }\n}"
      dart: "class Solution {\n  int maxSideLength(List<List<int>> mat, int threshold)\
        \ {\n    int m = mat.length;\n    int n = mat[0].length;\n    List<List<int>>\
        \ prefixSum = List.generate(m + 1, (i) => List.generate(n + 1, (j) => 0));\n\
        \    for (int i = 1; i <= m; i++) {\n      for (int j = 1; j <= n; j++) {\n\
        \        prefixSum[i][j] = prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i\
        \ - 1][j - 1] + mat[i - 1][j - 1];\n      }\n    }\n    int low = 1;\n    int\
        \ high = m < n ? m : n;\n    int ans = 0;\n    while (low <= high) {\n     \
        \ int mid = (low + high) ~/ 2;\n      if (possible(mat, prefixSum, threshold,\
        \ mid)) {\n        ans = mid;\n        low = mid + 1;\n      } else {\n    \
        \    high = mid - 1;\n      }\n    }\n    return ans;\n  }\n\n  bool possible(List<List<int>>\
        \ mat, List<List<int>> prefixSum, int threshold, int side) {\n    int m = mat.length;\n\
        \    int n = mat[0].length;\n    for (int i = 0; i <= m - side; i++) {\n   \
        \   for (int j = 0; j <= n - side; j++) {\n        int sum = prefixSum[i + side][j\
        \ + side] - prefixSum[i + side][j] - prefixSum[i][j + side] + prefixSum[i][j];\n\
        \        if (sum <= threshold) return true;\n      }\n    }\n    return false;\n\
        \  }\n}"
      go: "func maxSideLength(mat [][]int, threshold int) int {\n    m, n := len(mat),\
        \ len(mat[0])\n    prefixSum := make([][]int, m+1)\n    for i := range prefixSum\
        \ {\n        prefixSum[i] = make([]int, n+1)\n    }\n    for i := 1; i <= m;\
        \ i++ {\n        for j := 1; j <= n; j++ {\n            prefixSum[i][j] = prefixSum[i-1][j]\
        \ + prefixSum[i][j-1] - prefixSum[i-1][j-1] + mat[i-1][j-1]\n        }\n   \
        \ }\n    low, high := 1, min(m, n)\n    ans := 0\n    for low <= high {\n  \
        \      mid := (low + high) / 2\n        if possible(mat, prefixSum, threshold,\
        \ mid) {\n            ans = mid\n            low = mid + 1\n        } else {\n\
        \            high = mid - 1\n        }\n    }\n    return ans\n}\n\nfunc possible(mat\
        \ [][]int, prefixSum [][]int, threshold, side int) bool {\n    m, n := len(mat),\
        \ len(mat[0])\n    for i := 0; i <= m-side; i++ {\n        for j := 0; j <=\
        \ n-side; j++ {\n            sum := prefixSum[i+side][j+side] - prefixSum[i+side][j]\
        \ - prefixSum[i][j+side] + prefixSum[i][j]\n            if sum <= threshold\
        \ {\n                return true\n            }\n        }\n    }\n    return\
        \ false\n}"
      ruby: "def max_side_length(mat, threshold)\n    m, n = mat.size, mat[0].size\n\
        \    prefix_sum = Array.new(m + 1) { Array.new(n + 1, 0) }\n    (1..m).each\
        \ do |i|\n        (1..n).each do |j|\n            prefix_sum[i][j] = prefix_sum[i\
        \ - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + mat[i - 1][j -\
        \ 1]\n        end\n    end\n    low, high = 1, [m, n].min\n    ans = 0\n   \
        \ while low <= high\n        mid = (low + high) / 2\n        if possible(mat,\
        \ prefix_sum, threshold, mid)\n            ans = mid\n            low = mid\
        \ + 1\n        else\n            high = mid - 1\n        end\n    end\n    ans\n\
        end\n\ndef possible(mat, prefix_sum, threshold, side)\n    m, n = mat.size,\
        \ mat[0].size\n    (0...m - side + 1).each do |i|\n        (0...n - side + 1).each\
        \ do |j|\n            sum = prefix_sum[i + side][j + side] - prefix_sum[i +\
        \ side][j] - prefix_sum[i][j + side] + prefix_sum[i][j]\n            return\
        \ true if sum <= threshold\n        end\n    end\n    false\nend"
      scala: "object Solution {\n    def maxSideLength(mat: Array[Array[Int]], threshold:\
        \ Int): Int = {\n        val m = mat.length\n        val n = mat(0).length\n\
        \        val prefixSum = Array.ofDim[Int](m + 1, n + 1)\n        for (i <- 1\
        \ to m) {\n            for (j <- 1 to n) {\n                prefixSum(i)(j)\
        \ = prefixSum(i - 1)(j) + prefixSum(i)(j - 1) - prefixSum(i - 1)(j - 1) + mat(i\
        \ - 1)(j - 1)\n            }\n        }\n        var low = 1\n        var high\
        \ = math.min(m, n)\n        var ans = 0\n        while (low <= high) {\n   \
        \         val mid = (low + high) / 2\n            if (possible(mat, prefixSum,\
        \ threshold, mid)) {\n                ans = mid\n                low = mid +\
        \ 1\n            } else {\n                high = mid - 1\n            }\n \
        \       }\n        ans\n    }\n\n    def possible(mat: Array[Array[Int]], prefixSum:\
        \ Array[Array[Int]], threshold: Int, side: Int): Boolean = {\n        val m\
        \ = mat.length\n        val n = mat(0).length\n        for (i <- 0 until m -\
        \ side + 1) {\n            for (j <- 0 until n - side + 1) {\n             \
        \   val sum = prefixSum(i + side)(j + side) - prefixSum(i + side)(j) - prefixSum(i)(j\
        \ + side) + prefixSum(i)(j)\n                if (sum <= threshold) return true\n\
        \            }\n        }\n        false\n    }\n}"
      rust: "impl Solution {\n    pub fn max_side_length(mat: Vec<Vec<i32>>, threshold:\
        \ i32) -> i32 {\n        let m = mat.len() as i32;\n        let n = mat[0].len()\
        \ as i32;\n        let mut prefix_sum = vec![vec![0; (n + 1) as usize]; (m +\
        \ 1) as usize];\n        for i in 1..=m {\n            for j in 1..=n {\n  \
        \              prefix_sum[i as usize][j as usize] = prefix_sum[(i - 1) as usize][j\
        \ as usize] + prefix_sum[i as usize][(j - 1) as usize] - prefix_sum[(i - 1)\
        \ as usize][(j - 1) as usize] + mat[(i - 1) as usize][(j - 1) as usize];\n \
        \           }\n        }\n        let mut low = 1;\n        let mut high = m.min(n);\n\
        \        let mut ans = 0;\n        while low <= high {\n            let mid\
        \ = (low + high) / 2;\n            if Solution::possible(&mat, &prefix_sum,\
        \ threshold, mid) {\n                ans = mid;\n                low = mid +\
        \ 1;\n            } else {\n                high = mid - 1;\n            }\n\
        \        }\n        ans\n    }\n\n    fn possible(mat: &Vec<Vec<i32>>, prefix_sum:\
        \ &Vec<Vec<i32>>, threshold: i32, side: i32) -> bool {\n        let m = mat.len()\
        \ as i32;\n        let n = mat[0].len() as i32;\n        for i in 0..=m - side\
        \ {\n            for j in 0..=n - side {\n                let sum = prefix_sum[(i\
        \ + side) as usize][(j + side) as usize] - prefix_sum[(i + side) as usize][j\
        \ as usize] - prefix_sum[i as usize][(j + side) as usize] + prefix_sum[i as\
        \ usize][j as usize];\n                if sum <= threshold {\n             \
        \       return true;\n                }\n            }\n        }\n        false\n\
        \    }\n}"
      racket: "(define/contract (max-side-length mat threshold)\n  (-> (listof (listof\
        \ exact-integer?)) exact-integer? exact-integer?)\n  (let* (\n         (m (length\
        \ mat))\n         (n (length (car mat)))\n         (prefix-sum (make-list (add1\
        \ m) (lambda (x) (make-list (add1 n) 0))))\n         )\n    (for* (\n      \
        \     (i (range 1 (add1 m)))\n           (j (range 1 (add1 n)))\n          \
        \ )\n      (set! (list-ref (list-ref prefix-sum i) j)\n            (+ (list-ref\
        \ (list-ref prefix-sum (sub1 i)) j)\n               (list-ref (list-ref prefix-sum\
        \ i) (sub1 j))\n               (- (list-ref (list-ref prefix-sum (sub1 i)) (sub1\
        \ j)))\n               (list-ref (list-ref mat (sub1 i)) (sub1 j))\n       \
        \        ))\n      )\n    (let loop (\n           (low 1)\n           (high\
        \ (min m n))\n           (ans 0)\n           )\n      (if (> low high)\n   \
        \       ans\n          (let (\n                (mid (quotient (+ low high) 2))\n\
        \                )\n            (if (possible mat prefix-sum threshold mid)\n\
        \                (loop (add1 mid) high mid)\n                (loop low (sub1\
        \ mid) ans)\n                ))\n           )\n      )\n    )\n  )\n\n(define/contract\
        \ (possible mat prefix-sum threshold side)\n  (-> (listof (listof exact-integer?))\
        \ (listof (listof exact-integer?)) exact-integer? exact-integer? boolean?)\n\
        \  (let* (\n         (m (length mat))\n         (n (length (car mat)))\n   \
        \      )\n    (for*/or (\n             (i (range 0 (- m side + 1)))\n      \
        \       (j (range 0 (- n side + 1)))\n             )\n      (let (\n       \
        \     (sum (+ (list-ref (list-ref prefix-sum (+ i side)) (+ j side))\n     \
        \              (- (list-ref (list-ref prefix-sum (+ i side)) j))\n         \
        \          (- (list-ref (list-ref prefix-sum i) (+ j side)))\n             \
        \      (list-ref (list-ref prefix-sum i) j)\n                   ))\n       \
        \     )\n        (<= sum threshold)\n        )\n      )\n    )\n  )"
      erlang: "max_side_length(Mat, Threshold) ->\n    M = length(Mat),\n    N = length(hd(Mat)),\n\
        \    PrefixSum = array:new([{size, M + 1}, {default, 0}, {fixed, true}]),\n\
        \    lists:foreach(fun(I) ->\n                         lists:foreach(fun(J)\
        \ ->\n                                           array:set(I + 1, J + 1, array:get(I,\
        \ J + 1) + array:get(I + 1, J) - array:get(I, J) + lists:nth(J, lists:nth(I,\
        \ Mat)), PrefixSum)\n                                   end, lists:seq(1, N))\n\
        \                     end, lists:seq(1, M)),\n    Low = 1,\n    High = min(M,\
        \ N),\n    Ans = 0,\n    max_side_length_loop(Low, High, Ans, Mat, PrefixSum,\
        \ Threshold).\n\nmax_side_length_loop(Low, High, Ans, Mat, PrefixSum, Threshold)\
        \ when Low > High ->\n    Ans;\nmax_side_length_loop(Low, High, Ans, Mat, PrefixSum,\
        \ Threshold) ->\n    Mid = (Low + High) div 2,\n    case possible(Mat, PrefixSum,\
        \ Threshold, Mid) of\n        true -> max_side_length_loop(Mid + 1, High, Mid,\
        \ Mat, PrefixSum, Threshold);\n        false -> max_side_length_loop(Low, Mid\
        \ - 1, Ans, Mat, PrefixSum, Threshold)\n    end.\n\npossible(Mat, PrefixSum,\
        \ Threshold, Side) ->\n    M = length(Mat),\n    N = length(hd(Mat)),\n    lists:any(fun(I)\
        \ ->\n                   lists:any(fun(J) ->\n                             \
        \  Sum = array:get(I + Side, J + Side, PrefixSum) - array:get(I + Side, J, PrefixSum)\
        \ - array:get(I, J + Side, PrefixSum) + array:get(I, J, PrefixSum),\n      \
        \                         Sum =< Threshold\n                           end,\
        \ lists:seq(1, N - Side + 1))\n               end, lists:seq(1, M - Side + 1))."
      elixir: "defmodule Solution do\n  def max_side_length(mat, threshold) do\n   \
        \ m = length(mat)\n    n = length(Enum.at(mat, 0))\n    prefix_sum = Array.new(m\
        \ + 1, n + 1, 0)\n    Enum.reduce(1..m, prefix_sum, fn i, prefix_sum ->\n  \
        \    Enum.reduce(1..n, prefix_sum, fn j, prefix_sum ->\n        Array.set(prefix_sum,\
        \ {i, j}, Array.get(prefix_sum, {i - 1, j}) + Array.get(prefix_sum, {i, j -\
        \ 1}) - Array.get(prefix_sum, {i - 1, j - 1}) + Enum.at(Enum.at(mat, i - 1),\
        \ j - 1))\n      end)\n    end)\n    low = 1\n    high = min(m, n)\n    ans\
        \ = 0\n    max_side_length_loop(low, high, ans, mat, prefix_sum, threshold)\n\
        \  end\n\n  defp max_side_length_loop(low, high, ans, mat, prefix_sum, threshold)\
        \ when low > high do\n    ans\n  end\n\n  defp max_side_length_loop(low, high,\
        \ ans, mat, prefix_sum, threshold) do\n    mid = div(low + high, 2)\n    if\
        \ possible(mat, prefix_sum, threshold, mid) do\n      max_side_length_loop(mid\
        \ + 1, high, mid, mat, prefix_sum, threshold)\n    else\n      max_side_length_loop(low,\
        \ mid - 1, ans, mat, prefix_sum, threshold)\n    end\n  end\n\n  defp possible(mat,\
        \ prefix_sum, threshold, side) do\n    m = length(mat)\n    n = length(Enum.at(mat,\
        \ 0))\n    Enum.any?(1..m - side + 1, fn i ->\n      Enum.any?(1..n - side +\
        \ 1, fn j ->\n        sum = Array.get(prefix_sum, {i + side, j + side}) - Array.get(prefix_sum,\
        \ {i + side, j}) - Array.get(prefix_sum, {i, j + side}) + Array.get(prefix_sum,\
        \ {i, j}),\n        sum <= threshold\n      end)\n    end)\n  end\nend"
    approach: "The problem can be solved by using a prefix sum array to store the cumulative\
      \ sum of all sub-matrices in the given matrix. This allows us to calculate the\
      \ sum of any sub-matrix in constant time. We then use binary search to find the\
      \ maximum side length of a square with a sum less than or equal to the threshold.\
      \ We start by checking if a square of side length 1 is valid, then we check for\
      \ larger side lengths until we find the maximum valid side length.\n\n  The key\
      \ intuition behind this approach is that if a square of side length x is valid,\
      \ then any square with a side length less than x is also valid. This allows us\
      \ to use binary search to find the maximum valid side length in logarithmic time.\
      \ We also use the prefix sum array to calculate the sum of any sub-matrix in constant\
      \ time, which makes the overall algorithm more efficient."
    time_complexity: The time complexity of this algorithm is O(m*n*log(min(m,n))) where
      m and n are the dimensions of the matrix. This is because we are using binary
      search to find the maximum valid side length, and for each side length, we are
      checking all possible sub-matrices of that size. The prefix sum array allows us
      to calculate the sum of any sub-matrix in constant time, which reduces the overall
      time complexity.
    space_complexity: The space complexity of this algorithm is O(m*n) where m and n
      are the dimensions of the matrix. This is because we are storing the prefix sum
      array, which has the same dimensions as the input matrix. We also need to store
      the input matrix itself, which requires additional space.
    elapsed_time: 16.129555702209473
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-19 01:17:33 '
---

## Problem #1292: Maximum Side Length of a Square with Sum Less than or Equal to Threshold

**Difficulty:** Medium

**Topics:** Array, Binary Search, Matrix, Prefix Sum

## Problem Description

<p>Given a <code>m x n</code> matrix <code>mat</code> and an integer <code>threshold</code>, return <em>the maximum side-length of a square with a sum less than or equal to </em><code>threshold</code><em> or return </em><code>0</code><em> if there is no such square</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/12/05/e1.png" style="width: 335px; height: 186px;" />
<pre>
<strong>Input:</strong> mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
<strong>Output:</strong> 2
<strong>Explanation:</strong> The maximum side length of square with sum less than 4 is 2 as shown.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 300</code></li>
	<li><code>0 &lt;= mat[i][j] &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= threshold &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. Store prefix sum of all grids in another 2D array.

2. Try all possible solutions and if you cannot find one return -1.

3. If x is a valid answer then any y < x is also valid answer. Use binary search to find answer.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2026-01-19 01:17:12 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks for the maximum side-length of a square submatrix whose sum is less than or equal to a given threshold. This problem exhibits a monotonic property: if a square of side-length 'k' satisfies the condition, then any square of side-length 'k'' where k' < k will also satisfy the condition (since all matrix elements are non-negative). This monotonicity allows us to use binary search on the possible side-lengths, which range from 0 to min(m, n).

To efficiently check if a square of a given side-length 'k' exists with a sum less than or equal to the threshold, we first precompute a 2D prefix sum array (also known as an integral image). This array, `ps[i][j]`, stores the sum of all elements in the rectangle from `(0,0)` to `(i-1, j-1)`. With this prefix sum array, the sum of any sub-rectangle (including a square) can be calculated in O(1) time. The binary search repeatedly calls a `check(k)` function. This function iterates through all possible top-left corners `(r, c)` for a square of side `k` and uses the prefix sum array to calculate its sum. If any square's sum is within the threshold, `check(k)` returns true; otherwise, it returns false. The binary search then adjusts its range (low or high) based on the result of `check(k)` to find the largest valid `k`.

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
    int maxSideLength(vector<vector<int>>& mat, int threshold) {
        int m = mat.size();
        int n = mat[0].size();

        vector<vector<int>> ps(m + 1, vector<int>(n + 1, 0));

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                ps[i + 1][j + 1] = mat[i][j] + ps[i][j + 1] + ps[i + 1][j] - ps[i][j];
            }
        }

        auto getSquareSum = [&](int r1, int c1, int r2, int c2) {
            // r1, c1, r2, c2 are 0-indexed for the original matrix
            // ps array is 1-indexed for convenience
            return (long long)ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1];
        };

        auto check = [&](int k) {
            if (k == 0) return true; // A 0x0 square always has sum 0 <= threshold
            for (int r = 0; r <= m - k; ++r) {
                for (int c = 0; c <= n - k; ++c) {
                    if (getSquareSum(r, c, r + k - 1, c + k - 1) <= threshold) {
                        return true;
                    }
                }
            }
            return false;
        };

        int low = 0;
        int high = min(m, n);
        int ans = 0;

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
class Solution {
    public int maxSideLength(int[][] mat, int threshold) {
        int m = mat.length;
        int n = mat[0].length;

        int[][] ps = new int[m + 1][n + 1];

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                ps[i + 1][j + 1] = mat[i][j] + ps[i][j + 1] + ps[i + 1][j] - ps[i][j];
            }
        }

        // Helper function to get sum of a square from (r1, c1) to (r2, c2)
        // Note: r1, c1, r2, c2 are 0-indexed for the original matrix
        // ps array is 1-indexed for convenience
        // Using a lambda for clarity, but could be an inner method or inlined.
        java.util.function.Function<int[], Long> getSquareSum = (coords) -> {
            int r1 = coords[0], c1 = coords[1], r2 = coords[2], c2 = coords[3];
            return (long)ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1];
        };

        // Helper function to check if a square of side length k exists
        java.util.function.IntPredicate check = (k) -> {
            if (k == 0) return true; // A 0x0 square always has sum 0 <= threshold
            for (int r = 0; r <= m - k; ++r) {
                for (int c = 0; c <= n - k; ++c) {
                    if (getSquareSum.apply(new int[]{r, c, r + k - 1, c + k - 1}) <= threshold) {
                        return true;
                    }
                }
            }
            return false;
        };

        int low = 0;
        int high = Math.min(m, n);
        int ans = 0;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (check.test(mid)) {
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

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        m = len(mat)
        n = len(mat[0])

        ps = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                ps[i + 1][j + 1] = mat[i][j] + ps[i][j + 1] + ps[i + 1][j] - ps[i][j]

        def get_square_sum(r1, c1, r2, c2):
            # r1, c1, r2, c2 are 0-indexed for the original matrix
            # ps array is 1-indexed for convenience
            return ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1]

        def check(k):
            if k == 0: return True # A 0x0 square always has sum 0 <= threshold
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if get_square_sum(r, c, r + k - 1, c + k - 1) <= threshold:
                        return True
            return False

        low = 0
        high = min(m, n)
        ans = 0

        while low <= high:
            mid = low + (high - low) // 2
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
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])

        ps = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                ps[i + 1][j + 1] = mat[i][j] + ps[i][j + 1] + ps[i + 1][j] - ps[i][j]

        def get_square_sum(r1: int, c1: int, r2: int, c2: int) -> int:
            # r1, c1, r2, c2 are 0-indexed for the original matrix
            # ps array is 1-indexed for convenience
            return ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1]

        def check(k: int) -> bool:
            if k == 0: return True # A 0x0 square always has sum 0 <= threshold
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if get_square_sum(r, c, r + k - 1, c + k - 1) <= threshold:
                        return True
            return False

        low = 0
        high = min(m, n)
        ans = 0

        while low <= high:
            mid = low + (high - low) // 2
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
int maxSideLength(int** mat, int matSize, int* matColSize, int threshold) {
    int m = matSize;
    int n = matColSize[0]; // Assuming all rows have the same number of columns

    // Allocate and initialize prefix sum array
    int** ps = (int**)malloc((m + 1) * sizeof(int*));
    for (int i = 0; i <= m; ++i) {
        ps[i] = (int*)malloc((n + 1) * sizeof(int));
        for (int j = 0; j <= n; ++j) {
            ps[i][j] = 0;
        }
    }

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            ps[i + 1][j + 1] = mat[i][j] + ps[i][j + 1] + ps[i + 1][j] - ps[i][j];
        }
    }

    int low = 0;
    int high = (m < n) ? m : n;
    int ans = 0;

    while (low <= high) {
        int mid = low + (high - low) / 2;

        // check(mid) logic inline
        int found = 0;
        if (mid == 0) {
            found = 1; // A 0x0 square always has sum 0 <= threshold
        } else {
            for (int r = 0; r <= m - mid; ++r) {
                for (int c = 0; c <= n - mid; ++c) {
                    // Calculate sum for square with top-left (r, c) and side 'mid'
                    // Bottom-right is (r + mid - 1, c + mid - 1)
                    // Using ps array (1-indexed): ps[r+mid][c+mid] - ps[r][c+mid] - ps[r+mid][c] + ps[r][c]
                    long long current_sum = (long long)ps[r + mid][c + mid] - ps[r][c + mid] - ps[r + mid][c] + ps[r][c];
                    if (current_sum <= threshold) {
                        found = 1;
                        break;
                    }
                }
                if (found) break;
            }
        }

        if (found) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    // Free allocated memory for ps
    for (int i = 0; i <= m; ++i) {
        free(ps[i]);
    }
    free(ps);

    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaxSideLength(int[][] mat, int threshold) {
        int m = mat.Length;
        int n = mat[0].Length;

        int[][] ps = new int[m + 1][];
        for (int i = 0; i <= m; i++) {
            ps[i] = new int[n + 1];
        }

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                ps[i + 1][j + 1] = mat[i][j] + ps[i][j + 1] + ps[i + 1][j] - ps[i][j];
            }
        }

        // Helper function to get sum of a square from (r1, c1) to (r2, c2)
        // Note: r1, c1, r2, c2 are 0-indexed for the original matrix
        // ps array is 1-indexed for convenience
        long GetSquareSum(int r1, int c1, int r2, int c2) {
            return (long)ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1];
        }

        // Helper function to check if a square of side length k exists
        bool Check(int k) {
            if (k == 0) return true; // A 0x0 square always has sum 0 <= threshold
            for (int r = 0; r <= m - k; ++r) {
                for (int c = 0; c <= n - k; ++c) {
                    if (GetSquareSum(r, c, r + k - 1, c + k - 1) <= threshold) {
                        return true;
                    }
                }
            }
            return false;
        }

        int low = 0;
        int high = Math.Min(m, n);
        int ans = 0;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (Check(mid)) {
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

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[][]} mat
 * @param {number} threshold
 * @return {number}
 */
var maxSideLength = function(mat, threshold) {
    const m = mat.length;
    const n = mat[0].length;

    const ps = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));

    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            ps[i + 1][j + 1] = mat[i][j] + ps[i][j + 1] + ps[i + 1][j] - ps[i][j];
        }
    }

    // Helper function to get sum of a square from (r1, c1) to (r2, c2)
    // Note: r1, c1, r2, c2 are 0-indexed for the original matrix
    // ps array is 1-indexed for convenience
    const getSquareSum = (r1, c1, r2, c2) => {
        return ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1];
    };

    // Helper function to check if a square of side length k exists
    const check = (k) => {
        if (k === 0) return true; // A 0x0 square always has sum 0 <= threshold
        for (let r = 0; r <= m - k; ++r) {
            for (let c = 0; c <= n - k; ++c) {
                if (getSquareSum(r, c, r + k - 1, c + k - 1) <= threshold) {
                    return true;
                }
            }
        }
        return false;
    };

    let low = 0;
    let high = Math.min(m, n);
    let ans = 0;

    while (low <= high) {
        let mid = Math.floor(low + (high - low) / 2);
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
function maxSideLength(mat: number[][], threshold: number): number {
    const m = mat.length;
    const n = mat[0].length;

    const ps: number[][] = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));

    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            ps[i + 1][j + 1] = mat[i][j] + ps[i][j + 1] + ps[i + 1][j] - ps[i][j];
        }
    }

    // Helper function to get sum of a square from (r1, c1) to (r2, c2)
    // Note: r1, c1, r2, c2 are 0-indexed for the original matrix
    // ps array is 1-indexed for convenience
    const getSquareSum = (r1: number, c1: number, r2: number, c2: number): number => {
        return ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1];
    };

    // Helper function to check if a square of side length k exists
    const check = (k: number): boolean => {
        if (k === 0) return true; // A 0x0 square always has sum 0 <= threshold
        for (let r = 0; r <= m - k; ++r) {
            for (let c = 0; c <= n - k; ++c) {
                if (getSquareSum(r, c, r + k - 1, c + k - 1) <= threshold) {
                    return true;
                }
            }
        }
        return false;
    };

    let low = 0;
    let high = Math.min(m, n);
    let ans = 0;

    while (low <= high) {
        let mid = Math.floor(low + (high - low) / 2);
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

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[][] $mat
     * @param Integer $threshold
     * @return Integer
     */
    function maxSideLength($mat, $threshold) {
        $m = count($mat);
        $n = count($mat[0]);

        $ps = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));

        for ($i = 0; $i < $m; ++$i) {
            for ($j = 0; $j < $n; ++$j) {
                $ps[$i + 1][$j + 1] = $mat[$i][$j] + $ps[$i][$j + 1] + $ps[$i + 1][$j] - $ps[$i][$j];
            }
        }

        // Helper function to get sum of a square from (r1, c1) to (r2, c2)
        // Note: r1, c1, r2, c2 are 0-indexed for the original matrix
        // ps array is 1-indexed for convenience
        $getSquareSum = function($r1, $c1, $r2, $c2) use ($ps) {
            return $ps[$r2 + 1][$c2 + 1] - $ps[$r1][$c2 + 1] - $ps[$r2 + 1][$c1] + $ps[$r1][$c1];
        };

        // Helper function to check if a square of side length k exists
        $check = function($k) use ($m, $n, $threshold, $getSquareSum) {
            if ($k == 0) return true; // A 0x0 square always has sum 0 <= threshold
            for ($r = 0; $r <= $m - $k; ++$r) {
                for ($c = 0; $c <= $n - $k; ++$c) {
                    if ($getSquareSum($r, $c, $r + $k - 1, $c + $k - 1) <= $threshold) {
                        return true;
                    }
                }
            }
            return false;
        };

        $low = 0;
        $high = min($m, $n);
        $ans = 0;

        while ($low <= $high) {
            $mid = floor($low + ($high - $low) / 2);
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
    func maxSideLength(_ mat: [[Int]], _ threshold: Int) -> Int {
        let m = mat.count
        let n = mat[0].count

        var ps = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)

        for i in 0..<m {
            for j in 0..<n {
                ps[i + 1][j + 1] = mat[i][j] + ps[i][j + 1] + ps[i + 1][j] - ps[i][j]
            }
        }

        // Helper function to get sum of a square from (r1, c1) to (r2, c2)
        // Note: r1, c1, r2, c2 are 0-indexed for the original matrix
        // ps array is 1-indexed for convenience
        func getSquareSum(_ r1: Int, _ c1: Int, _ r2: Int, _ c2: Int) -> Int {
            return ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1]
        }

        // Helper function to check if a square of side length k exists
        func check(_ k: Int) -> Bool {
            if k == 0 { return true } // A 0x0 square always has sum 0 <= threshold
            for r in 0...(m - k) {
                for c in 0...(n - k) {
                    if getSquareSum(r, c, r + k - 1, c + k - 1) <= threshold {
                        return true
                    }
                }
            }
            return false
        }

        var low = 0
        var high = min(m, n)
        var ans = 0

        while low <= high {
            let mid = low + (high - low) / 2
            if check(mid) {
                ans = mid
                low = mid + 1
            } else {
                high = mid - 1
            }
        }

        return ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxSideLength(mat: Array<IntArray>, threshold: Int): Int {
        val m = mat.size
        val n = mat[0].size

        val ps = Array(m + 1) { IntArray(n + 1) }
        for (r in 0 until m) {
            for (c in 0 until n) {
                ps[r + 1][c + 1] = mat[r][c] + ps[r][c + 1] + ps[r + 1][c] - ps[r][c]
            }
        }

        fun getSquareSum(r1: Int, c1: Int, k: Int): Int {
            val r2 = r1 + k - 1
            val c2 = c1 + k - 1
            return ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1]
        }

        fun check(k: Int): Boolean {
            if (k == 0) return true
            if (k > m || k > n) return false

            for (r in 0..(m - k)) {
                for (c in 0..(n - k)) {
                    if (getSquareSum(r, c, k) <= threshold) {
                        return true
                    }
                }
            }
            return false
        }

        var low = 0
        var high = Math.min(m, n)
        var ans = 0

        while (low <= high) {
            val mid = low + (high - low) / 2
            if (check(mid)) {
                ans = mid
                low = mid + 1
            } else {
                high = mid - 1
            }
        }

        return ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maxSideLength(List<List<int>> mat, int threshold) {
    final m = mat.length;
    final n = mat[0].length;

    final ps = List.generate(m + 1, (_) => List.filled(n + 1, 0));
    for (var r = 0; r < m; r++) {
      for (var c = 0; c < n; c++) {
        ps[r + 1][c + 1] = mat[r][c] + ps[r][c + 1] + ps[r + 1][c] - ps[r][c];
      }
    }

    int getSquareSum(int r1, int c1, int k) {
      final r2 = r1 + k - 1;
      final c2 = c1 + k - 1;
      return ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1];
    }

    bool check(int k) {
      if (k == 0) return true;
      if (k > m || k > n) return false;

      for (var r = 0; r <= (m - k); r++) {
        for (var c = 0; c <= (n - k); c++) {
          if (getSquareSum(r, c, k) <= threshold) {
            return true;
          }
        }
      }
      return false;
    }

    var low = 0;
    var high = m < n ? m : n;
    var ans = 0;

    while (low <= high) {
      final mid = low + (high - low) ~/ 2;
      if (check(mid)) {
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
func maxSideLength(mat [][]int, threshold int) int {
    m := len(mat)
    n := len(mat[0])

    ps := make([][]int, m+1)
    for i := range ps {
        ps[i] = make([]int, n+1)
    }

    for r := 0; r < m; r++ {
        for c := 0; c < n; c++ {
            ps[r+1][c+1] = mat[r][c] + ps[r][c+1] + ps[r+1][c] - ps[r][c]
        }
    }

    getSquareSum := func(r1, c1, k int) int {
        r2 := r1 + k - 1
        c2 := c1 + k - 1
        return ps[r2+1][c2+1] - ps[r1][c2+1] - ps[r2+1][c1] + ps[r1][c1]
    }

    check := func(k int) bool {
        if k == 0 {
            return true
        }
        if k > m || k > n {
            return false
        }

        for r := 0; r <= (m - k); r++ {
            for c := 0; c <= (n - k); c++ {
                if getSquareSum(r, c, k) <= threshold {
                    return true
                }
            }
        }
        return false
    }

    low := 0
    high := min(m, n)
    ans := 0

    for low <= high {
        mid := low + (high - low) / 2
        if check(mid) {
            ans = mid
            low = mid + 1
        } else {
            high = mid - 1
        }
    }

    return ans
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
# @param {Integer[][]} mat
# @param {Integer} threshold
# @return {Integer}
def max_side_length(mat, threshold)
    m = mat.length
    n = mat[0].length

    ps = Array.new(m + 1) { Array.new(n + 1, 0) }
    (0...m).each do |r|
        (0...n).each do |c|
            ps[r + 1][c + 1] = mat[r][c] + ps[r][c + 1] + ps[r + 1][c] - ps[r][c]
        end
    end

    get_square_sum = lambda do |r1, c1, k|
        r2 = r1 + k - 1
        c2 = c1 + k - 1
        ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1]
    end

    check = lambda do |k|
        return true if k == 0
        return false if k > m || k > n

        (0..(m - k)).each do |r|
            (0..(n - k)).each do |c|
                if get_square_sum.call(r, c, k) <= threshold
                    return true
                end
            end
        end
        false
    end

    low = 0
    high = [m, n].min
    ans = 0

    while low <= high
        mid = low + (high - low) / 2
        if check.call(mid)
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
    def maxSideLength(mat: Array[Array[Int]], threshold: Int): Int = {
        val m = mat.length
        val n = mat(0).length

        val ps = Array.ofDim[Int](m + 1, n + 1)
        for (r <- 0 until m) {
            for (c <- 0 until n) {
                ps(r + 1)(c + 1) = mat(r)(c) + ps(r)(c + 1) + ps(r + 1)(c) - ps(r)(c)
            }
        }

        def getSquareSum(r1: Int, c1: Int, k: Int): Int = {
            val r2 = r1 + k - 1
            val c2 = c1 + k - 1
            ps(r2 + 1)(c2 + 1) - ps(r1)(c2 + 1) - ps(r2 + 1)(c1) + ps(r1)(c1)
        }

        def check(k: Int): Boolean = {
            if (k == 0) return true
            if (k > m || k > n) return false

            for (r <- 0 to (m - k)) {
                for (c <- 0 to (n - k)) {
                    if (getSquareSum(r, c, k) <= threshold) {
                        return true
                    }
                }
            }
            false
        }

        var low = 0
        var high = Math.min(m, n)
        var ans = 0

        while (low <= high) {
            val mid = low + (high - low) / 2
            if (check(mid)) {
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
    pub fn max_side_length(mat: Vec<Vec<i32>>, threshold: i32) -> i32 {
        let m = mat.len();
        let n = mat[0].len();

        let mut ps = vec![vec![0; n + 1]; m + 1];
        for r in 0..m {
            for c in 0..n {
                ps[r + 1][c + 1] = mat[r][c] + ps[r][c + 1] + ps[r + 1][c] - ps[r][c];
            }
        }

        let get_square_sum = |r1: usize, c1: usize, k: usize| -> i32 {
            let r2 = r1 + k - 1;
            let c2 = c1 + k - 1;
            ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1]
        };

        let check = |k: usize| -> bool {
            if k == 0 {
                return true;
            }
            if k > m || k > n {
                return false;
            }

            for r in 0..=(m - k) {
                for c in 0..=(n - k) {
                    if get_square_sum(r, c, k) <= threshold {
                        return true;
                    }
                }
            }
            false
        };

        let mut low = 0;
        let mut high = std::cmp::min(m, n);
        let mut ans = 0;

        while low <= high {
            let mid = low + (high - low) / 2;
            if check(mid) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        ans as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (max-side-length mat threshold)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* ([m (length mat)]
         [n (length (car mat))]
         [ps (build-vector (+ m 1) (lambda (_) (build-vector (+ n 1) (lambda (_) 0))))])

    (for* ([r (in-range m)]
           [c (in-range n)])
      (vector-set! (vector-ref ps (+ r 1)) (+ c 1)
                   (+ (list-ref (list-ref mat r) c)
                      (vector-ref (vector-ref ps r) (+ c 1))
                      (vector-ref (vector-ref ps (+ r 1)) c)
                      (- (vector-ref (vector-ref ps r) c))))))

    (define (get-square-sum r1 c1 k)
      (let* ([r2 (+ r1 k -1)]
             [c2 (+ c1 k -1)])
        (+ (vector-ref (vector-ref ps (+ r2 1)) (+ c2 1))
           (- (vector-ref (vector-ref ps r1) (+ c2 1)))
           (- (vector-ref (vector-ref ps (+ r2 1)) c1))
           (vector-ref (vector-ref ps r1) c1))))

    (define (check k)
      (cond
        [(= k 0) #t]
        [(or (> k m) (> k n)) #f]
        [else
         (let loop ([r 0])
           (cond
             [(> r (- m k)) #f]
             [else
              (let loop-inner ([c 0])
                (cond
                  [(> c (- n k)) (loop (+ r 1))]
                  [else
                   (if (<= (get-square-sum r c k) threshold)
                       #t
                       (loop-inner (+ c 1)))]))]))]))

    (let loop-bs ([low 0] [high (min m n)] [ans 0])
      (if (> low high)
          ans
          (let ([mid (+ low (quotient (- high low) 2))])
            (if (check mid)
                (loop-bs (+ mid 1) high mid)
                (loop-bs low (- mid 1) ans)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_side_length(Mat :: [[integer()]], Threshold :: integer()) -> integer().
max_side_length(Mat, Threshold) ->
  M = length(Mat),
  N = length(hd(Mat)),

  InitialRow = array:new([{size, N + 1}, {fixed, true}, {default, 0}]),
  PsArray = array:new([{size, M + 1}, {fixed, true}, {default, InitialRow}]),

  PsArrayFinal = build_ps_array(Mat, M, N, PsArray),

  GetSquareSum = fun(R1, C1, K) ->
    R2 = R1 + K - 1,
    C2 = C1 + K - 1,
    array:get(C2 + 1, array:get(R2 + 1, PsArrayFinal))
    - array:get(C2 + 1, array:get(R1, PsArrayFinal))
    - array:get(C1, array:get(R2 + 1, PsArrayFinal))
    + array:get(C1, array:get(R1, PsArrayFinal))
  end,

  Check = fun
    (0) -> true;
    (K) when K > M; K > N -> false;
    (K) ->
      lists:any(
        fun(R) ->
          lists:any(
            fun(C) ->
              GetSquareSum(R, C, K) =< Threshold
            end,
            lists:seq(0, N - K)
          )
        end,
        lists:seq(0, M - K)
      )
  end,

  Low = 0,
  High = min(M, N),
  binary_search_erlang(Low, High, 0, Check).

binary_search_erlang(Low, High, Ans, Check) ->
  if
    Low > High -> Ans;
    true ->
      Mid = Low + (High - Low) div 2,
      if
        Check(Mid) -> binary_search_erlang(Mid + 1, High, Mid, Check);
        true -> binary_search_erlang(Low, Mid - 1, Ans, Check)
      end
  end.

build_ps_array(Mat, M, N, PsArray) ->
  build_ps_array_rows(Mat, M, N, 0, PsArray).

build_ps_array_rows(_Mat, M, _N, M, PsArray) ->
  PsArray;
build_ps_array_rows(Mat, M, N, R_idx, AccPsArray) ->
  CurrentMatRow = lists:nth(R_idx + 1, Mat),

  PrevPsRowArray = array:get(R_idx, AccPsArray),
  CurrentPsRowArray = array:get(R_idx + 1, AccPsArray),

  UpdatedCurrentPsRowArray = build_current_ps_array_row(CurrentMatRow, PrevPsRowArray, CurrentPsRowArray, N, 0),

  NewPsArray = array:set(R_idx + 1, UpdatedCurrentPsRowArray, AccPsArray),
  build_ps_array_rows(Mat, M, N, R_idx + 1, NewPsArray).

build_current_ps_array_row(_CurrentMatRow, _PrevPsRowArray, CurrentPsRowArray, N, N) ->
  CurrentPsRowArray;
build_current_ps_array_row(CurrentMatRow, PrevPsRowArray, CurrentPsRowArray, N, C_idx) ->
  MatVal = lists:nth(C_idx + 1, CurrentMatRow),

  PsPrevRowCurrentCol = array:get(C_idx + 1, PrevPsRowArray),
  PsCurrentRowPrevCol = array:get(C_idx, CurrentPsRowArray),
  PsPrevRowPrevCol = array:get(C_idx, PrevPsRowArray),

  NewSum = MatVal + PsPrevRowCurrentCol + PsCurrentRowPrevCol - PsPrevRowPrevCol,

  UpdatedCurrentPsRowArray = array:set(C_idx + 1, NewSum, CurrentPsRowArray),
  build_current_ps_array_row(CurrentMatRow, PrevPsRowArray, UpdatedCurrentPsRowArray, N, C_idx + 1).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_side_length(mat :: [[integer]], threshold :: integer) :: integer
  def max_side_length(mat, threshold) do
    m = length(mat)
    n = length(hd(mat))

    ps_matrix = build_ps_map(mat, m, n)

    get_square_sum = fn r1, c1, k ->
      r2 = r1 + k - 1
      c2 = c1 + k - 1
      Map.get(Map.get(ps_matrix, r2 + 1), c2 + 1) -
        Map.get(Map.get(ps_matrix, r1), c2 + 1) -
        Map.get(Map.get(ps_matrix, r2 + 1), c1) +
        Map.get(Map.get(ps_matrix, r1), c1)
    end

    check = fn k ->
      cond do
        k == 0 -> true
        k > m or k > n -> false
        true ->
          0..(m - k)
          |> Enum.any?(fn r ->
            0..(n - k)
            |> Enum.any?(fn c ->
              get_square_sum.(r, c, k) <= threshold
            end)
          end)
      end
    end

    low = 0
    high = min(m, n)
    ans = 0

    binary_search(low, high, ans, check)
  end

  defp binary_search(low, high, ans, check) when low > high, do: ans
  defp binary_search(low, high, ans, check) do
    mid = low + div(high - low, 2)
    if check.(mid) do
      binary_search(mid + 1, high, mid, check)
    else
      binary_search(low, mid - 1, ans, check)
    end
  end

  defp build_ps_map(mat, m, n) do
    initial_ps_map = %{0 => Map.new(0..n, fn c -> {c, 0} end)}
    build_ps_rows_map(mat, m, n, 0, initial_ps_map)
  end

  defp build_ps_rows_map(_mat, m, _n, m, ps_map), do: ps_map
  defp build_ps_rows_map(mat, m, n, r_idx, acc_ps_map) do
    current_mat_row = Enum.at(mat, r_idx)

    current_ps_row_map = build_current_ps_row_map(current_mat_row, acc_ps_map, r_idx, n, 0, %{0 => 0})

    build_ps_rows_map(mat, m, n, r_idx + 1, Map.put(acc_ps_map, r_idx + 1, current_ps_row_map))
  end

  defp build_current_ps_row_map(_current_mat_row, _acc_ps_map, _r_idx, n, n, acc_current_ps_row_map), do: acc_current_ps_row_map
  defp build_current_ps_row_map(current_mat_row, acc_ps_map, r_idx, n, c_idx, acc_current_ps_row_map) do
    mat_val = Enum.at(current_mat_row, c_idx)

    ps_prev_row_current_col = Map.get(Map.get(acc_ps_map, r_idx), c_idx + 1)
    ps_current_row_prev_col = Map.get(acc_current_ps_row_map, c_idx)
    ps_prev_row_prev_col = Map.get(Map.get(acc_ps_map, r_idx), c_idx)

    new_sum = mat_val + ps_prev_row_current_col + ps_current_row_prev_col - ps_prev_row_prev_col

    build_current_ps_row_map(current_mat_row, acc_ps_map, r_idx, n, c_idx + 1, Map.put(acc_current_ps_row_map, c_idx + 1, new_sum))
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is dominated by two parts: building the prefix sum array and the binary search. Building the prefix sum array takes O(m*n) time. The binary search performs O(log(min(m, n))) iterations. In each iteration, the `check(k)` function iterates through all possible top-left corners for a square of side `k`, which is approximately (m-k+1) * (n-k+1) operations. Each sum calculation is O(1) using the prefix sum array. Thus, `check(k)` takes O(m*n) time. Combining these, the total time complexity is O(m*n + log(min(m, n)) * m*n), which simplifies to O(m*n * log(min(m, n))).

- **Space Complexity:** The space complexity is determined by the 2D prefix sum array, which requires O(m*n) additional space to store the sums for all sub-rectangles. No other significant data structures are used that would exceed this complexity.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-19 01:17:33 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by using a prefix sum array to store the cumulative sum of all sub-matrices in the given matrix. This allows us to calculate the sum of any sub-matrix in constant time. We then use binary search to find the maximum side length of a square with a sum less than or equal to the threshold. We start by checking if a square of side length 1 is valid, then we check for larger side lengths until we find the maximum valid side length.

  The key intuition behind this approach is that if a square of side length x is valid, then any square with a side length less than x is also valid. This allows us to use binary search to find the maximum valid side length in logarithmic time. We also use the prefix sum array to calculate the sum of any sub-matrix in constant time, which makes the overall algorithm more efficient.

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
    int maxSideLength(vector<vector<int>>& mat, int threshold) {
        int m = mat.size();
        int n = mat[0].size();
        vector<vector<int>> prefix(m + 1, vector<int>(n + 1, 0));
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + mat[i - 1][j - 1];
            }
        }
        int low = 0;
        int high = min(m, n);
        while (low <= high) {
            int mid = low + (high - low) / 2;
            bool found = false;
            for (int i = 0; i <= m - mid; i++) {
                for (int j = 0; j <= n - mid; j++) {
                    int sum = prefix[i + mid][j + mid] - prefix[i + mid][j] - prefix[i][j + mid] + prefix[i][j];
                    if (sum <= threshold) {
                        found = true;
                        break;
                    }
                }
                if (found) break;
            }
            if (found) low = mid + 1;
            else high = mid - 1;
        }
        return high;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maxSideLength(int[][] mat, int threshold) {
        int m = mat.length;
        int n = mat[0].length;
        int[][] prefix = new int[m + 1][n + 1];
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + mat[i - 1][j - 1];
            }
        }
        int low = 0;
        int high = Math.min(m, n);
        while (low <= high) {
            int mid = low + (high - low) / 2;
            boolean found = false;
            for (int i = 0; i <= m - mid; i++) {
                for (int j = 0; j <= n - mid; j++) {
                    int sum = prefix[i + mid][j + mid] - prefix[i + mid][j] - prefix[i][j + mid] + prefix[i][j];
                    if (sum <= threshold) {
                        found = true;
                        break;
                    }
                }
                if (found) break;
            }
            if (found) low = mid + 1;
            else high = mid - 1;
        }
        return high;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def maxSideLength(self, mat, threshold):
        m, n = len(mat), len(mat[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + mat[i - 1][j - 1]
        low, high = 0, min(m, n)
        while low <= high:
            mid = (low + high) // 2
            found = False
            for i in range(m - mid + 1):
                for j in range(n - mid + 1):
                    sum = prefix[i + mid][j + mid] - prefix[i + mid][j] - prefix[i][j + mid] + prefix[i][j]
                    if sum <= threshold:
                        found = True
                        break
                if found: break
            if found: low = mid + 1
            else: high = mid - 1
        return high
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxSideLength(self, mat: list[list[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + mat[i - 1][j - 1]
        low, high = 0, min(m, n)
        while low <= high:
            mid = (low + high) // 2
            found = False
            for i in range(m - mid + 1):
                for j in range(n - mid + 1):
                    sum = prefix[i + mid][j + mid] - prefix[i + mid][j] - prefix[i][j + mid] + prefix[i][j]
                    if sum <= threshold:
                        found = True
                        break
                if found: break
            if found: low = mid + 1
            else: high = mid - 1
        return high
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int maxSideLength(int** mat, int matSize, int* matColSize, int threshold) {
    int m = matSize;
    int n = matColSize[0];
    int** prefix = (int**)malloc((m + 1) * sizeof(int*));
    for (int i = 0; i <= m; i++) {
        prefix[i] = (int*)malloc((n + 1) * sizeof(int));
    }
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + mat[i - 1][j - 1];
        }
    }
    int low = 0;
    int high = (m < n) ? m : n;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        int found = 0;
        for (int i = 0; i <= m - mid; i++) {
            for (int j = 0; j <= n - mid; j++) {
                int sum = prefix[i + mid][j + mid] - prefix[i + mid][j] - prefix[i][j + mid] + prefix[i][j];
                if (sum <= threshold) {
                    found = 1;
                    break;
                }
            }
            if (found) break;
        }
        if (found) low = mid + 1;
        else high = mid - 1;
    }
    return high;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaxSideLength(int[][] mat, int threshold) {
        int m = mat.Length;
        int n = mat[0].Length;
        int[][] prefix = new int[m + 1][];
        for (int i = 0; i <= m; i++) {
            prefix[i] = new int[n + 1];
        }
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + mat[i - 1][j - 1];
            }
        }
        int low = 0;
        int high = Math.Min(m, n);
        while (low <= high) {
            int mid = low + (high - low) / 2;
            bool found = false;
            for (int i = 0; i <= m - mid; i++) {
                for (int j = 0; j <= n - mid; j++) {
                    int sum = prefix[i + mid][j + mid] - prefix[i + mid][j] - prefix[i][j + mid] + prefix[i][j];
                    if (sum <= threshold) {
                        found = true;
                        break;
                    }
                }
                if (found) break;
            }
            if (found) low = mid + 1;
            else high = mid - 1;
        }
        return high;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var maxSideLength = function(mat, threshold) {
    let m = mat.length;
    let n = mat[0].length;
    let prefix = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + mat[i - 1][j - 1];
        }
    }
    let low = 0;
    let high = Math.min(m, n);
    while (low <= high) {
        let mid = low + Math.floor((high - low) / 2);
        let found = false;
        for (let i = 0; i <= m - mid; i++) {
            for (let j = 0; j <= n - mid; j++) {
                let sum = prefix[i + mid][j + mid] - prefix[i + mid][j] - prefix[i][j + mid] + prefix[i][j];
                if (sum <= threshold) {
                    found = true;
                    break;
                }
            }
            if (found) break;
        }
        if (found) low = mid + 1;
        else high = mid - 1;
    }
    return high;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxSideLength(mat: number[][], threshold: number): number {
    let m: number = mat.length;
    let n: number = mat[0].length;
    let prefix: number[][] = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + mat[i - 1][j - 1];
        }
    }
    let low: number = 0;
    let high: number = Math.min(m, n);
    while (low <= high) {
        let mid: number = low + Math.floor((high - low) / 2);
        let found: boolean = false;
        for (let i = 0; i <= m - mid; i++) {
            for (let j = 0; j <= n - mid; j++) {
                let sum: number = prefix[i + mid][j + mid] - prefix[i + mid][j] - prefix[i][j + mid] + prefix[i][j];
                if (sum <= threshold) {
                    found = true;
                    break;
                }
            }
            if (found) break;
        }
        if (found) low = mid + 1;
        else high = mid - 1;
    }
    return high;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function maxSideLength($mat, $threshold) {
        $m = count($mat);
        $n = count($mat[0]);
        $prefix = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));
        for ($i = 1; $i <= $m; $i++) {
            for ($j = 1; $j <= $n; $j++) {
                $prefix[$i][$j] = $prefix[$i - 1][$j] + $prefix[$i][$j - 1] - $prefix[$i - 1][$j - 1] + $mat[$i - 1][$j - 1];
            }
        }
        $low = 0;
        $high = min($m, $n);
        while ($low <= $high) {
            $mid = $low + floor(($high - $low) / 2);
            $found = false;
            for ($i = 0; $i <= $m - $mid; $i++) {
                for ($j = 0; $j <= $n - $mid; $j++) {
                    $sum = $prefix[$i + $mid][$j + $mid] - $prefix[$i + $mid][$j] - $prefix[$i][$j + $mid] + $prefix[$i][$j];
                    if ($sum <= $threshold) {
                        $found = true;
                        break;
                    }
                }
                if ($found) break;
            }
            if ($found) $low = $mid + 1;
            else $high = $mid - 1;
        }
        return $high;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxSideLength(_ mat: [[Int]], _ threshold: Int) -> Int {
        let m = mat.count
        let n = mat[0].count
        var prefix = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)
        for i in 1...m {
            for j in 1...n {
                prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + mat[i - 1][j - 1]
            }
        }
        var low = 0
        var high = min(m, n)
        while low <= high {
            let mid = low + (high - low) / 2
            var found = false
            for i in 0...m - mid {
                for j in 0...n - mid {
                    let sum = prefix[i + mid][j + mid] - prefix[i + mid][j] - prefix[i][j + mid] + prefix[i][j]
                    if sum <= threshold {
                        found = true
                        break
                    }
                }
                if found { break }
            }
            if found { low = mid + 1 }
            else { high = mid - 1 }
        }
        return high
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxSideLength(mat: Array<IntArray>, threshold: Int): Int {
        val m = mat.size
        val n = mat[0].size
        val prefixSum = Array(m + 1) { IntArray(n + 1) }
        for (i in 1..m) {
            for (j in 1..n) {
                prefixSum[i][j] = prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1] + mat[i - 1][j - 1]
            }
        }
        var low = 1
        var high = minOf(m, n)
        var ans = 0
        while (low <= high) {
            val mid = (low + high) / 2
            if (possible(mat, prefixSum, threshold, mid)) {
                ans = mid
                low = mid + 1
            } else {
                high = mid - 1
            }
        }
        return ans
    }

    fun possible(mat: Array<IntArray>, prefixSum: Array<IntArray>, threshold: Int, side: Int): Boolean {
        val m = mat.size
        val n = mat[0].size
        for (i in 0 until m - side + 1) {
            for (j in 0 until n - side + 1) {
                val sum = prefixSum[i + side][j + side] - prefixSum[i + side][j] - prefixSum[i][j + side] + prefixSum[i][j]
                if (sum <= threshold) return true
            }
        }
        return false
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maxSideLength(List<List<int>> mat, int threshold) {
    int m = mat.length;
    int n = mat[0].length;
    List<List<int>> prefixSum = List.generate(m + 1, (i) => List.generate(n + 1, (j) => 0));
    for (int i = 1; i <= m; i++) {
      for (int j = 1; j <= n; j++) {
        prefixSum[i][j] = prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1] + mat[i - 1][j - 1];
      }
    }
    int low = 1;
    int high = m < n ? m : n;
    int ans = 0;
    while (low <= high) {
      int mid = (low + high) ~/ 2;
      if (possible(mat, prefixSum, threshold, mid)) {
        ans = mid;
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }
    return ans;
  }

  bool possible(List<List<int>> mat, List<List<int>> prefixSum, int threshold, int side) {
    int m = mat.length;
    int n = mat[0].length;
    for (int i = 0; i <= m - side; i++) {
      for (int j = 0; j <= n - side; j++) {
        int sum = prefixSum[i + side][j + side] - prefixSum[i + side][j] - prefixSum[i][j + side] + prefixSum[i][j];
        if (sum <= threshold) return true;
      }
    }
    return false;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxSideLength(mat [][]int, threshold int) int {
    m, n := len(mat), len(mat[0])
    prefixSum := make([][]int, m+1)
    for i := range prefixSum {
        prefixSum[i] = make([]int, n+1)
    }
    for i := 1; i <= m; i++ {
        for j := 1; j <= n; j++ {
            prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1] + mat[i-1][j-1]
        }
    }
    low, high := 1, min(m, n)
    ans := 0
    for low <= high {
        mid := (low + high) / 2
        if possible(mat, prefixSum, threshold, mid) {
            ans = mid
            low = mid + 1
        } else {
            high = mid - 1
        }
    }
    return ans
}

func possible(mat [][]int, prefixSum [][]int, threshold, side int) bool {
    m, n := len(mat), len(mat[0])
    for i := 0; i <= m-side; i++ {
        for j := 0; j <= n-side; j++ {
            sum := prefixSum[i+side][j+side] - prefixSum[i+side][j] - prefixSum[i][j+side] + prefixSum[i][j]
            if sum <= threshold {
                return true
            }
        }
    }
    return false
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def max_side_length(mat, threshold)
    m, n = mat.size, mat[0].size
    prefix_sum = Array.new(m + 1) { Array.new(n + 1, 0) }
    (1..m).each do |i|
        (1..n).each do |j|
            prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + mat[i - 1][j - 1]
        end
    end
    low, high = 1, [m, n].min
    ans = 0
    while low <= high
        mid = (low + high) / 2
        if possible(mat, prefix_sum, threshold, mid)
            ans = mid
            low = mid + 1
        else
            high = mid - 1
        end
    end
    ans
end

def possible(mat, prefix_sum, threshold, side)
    m, n = mat.size, mat[0].size
    (0...m - side + 1).each do |i|
        (0...n - side + 1).each do |j|
            sum = prefix_sum[i + side][j + side] - prefix_sum[i + side][j] - prefix_sum[i][j + side] + prefix_sum[i][j]
            return true if sum <= threshold
        end
    end
    false
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxSideLength(mat: Array[Array[Int]], threshold: Int): Int = {
        val m = mat.length
        val n = mat(0).length
        val prefixSum = Array.ofDim[Int](m + 1, n + 1)
        for (i <- 1 to m) {
            for (j <- 1 to n) {
                prefixSum(i)(j) = prefixSum(i - 1)(j) + prefixSum(i)(j - 1) - prefixSum(i - 1)(j - 1) + mat(i - 1)(j - 1)
            }
        }
        var low = 1
        var high = math.min(m, n)
        var ans = 0
        while (low <= high) {
            val mid = (low + high) / 2
            if (possible(mat, prefixSum, threshold, mid)) {
                ans = mid
                low = mid + 1
            } else {
                high = mid - 1
            }
        }
        ans
    }

    def possible(mat: Array[Array[Int]], prefixSum: Array[Array[Int]], threshold: Int, side: Int): Boolean = {
        val m = mat.length
        val n = mat(0).length
        for (i <- 0 until m - side + 1) {
            for (j <- 0 until n - side + 1) {
                val sum = prefixSum(i + side)(j + side) - prefixSum(i + side)(j) - prefixSum(i)(j + side) + prefixSum(i)(j)
                if (sum <= threshold) return true
            }
        }
        false
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_side_length(mat: Vec<Vec<i32>>, threshold: i32) -> i32 {
        let m = mat.len() as i32;
        let n = mat[0].len() as i32;
        let mut prefix_sum = vec![vec![0; (n + 1) as usize]; (m + 1) as usize];
        for i in 1..=m {
            for j in 1..=n {
                prefix_sum[i as usize][j as usize] = prefix_sum[(i - 1) as usize][j as usize] + prefix_sum[i as usize][(j - 1) as usize] - prefix_sum[(i - 1) as usize][(j - 1) as usize] + mat[(i - 1) as usize][(j - 1) as usize];
            }
        }
        let mut low = 1;
        let mut high = m.min(n);
        let mut ans = 0;
        while low <= high {
            let mid = (low + high) / 2;
            if Solution::possible(&mat, &prefix_sum, threshold, mid) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        ans
    }

    fn possible(mat: &Vec<Vec<i32>>, prefix_sum: &Vec<Vec<i32>>, threshold: i32, side: i32) -> bool {
        let m = mat.len() as i32;
        let n = mat[0].len() as i32;
        for i in 0..=m - side {
            for j in 0..=n - side {
                let sum = prefix_sum[(i + side) as usize][(j + side) as usize] - prefix_sum[(i + side) as usize][j as usize] - prefix_sum[i as usize][(j + side) as usize] + prefix_sum[i as usize][j as usize];
                if sum <= threshold {
                    return true;
                }
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
(define/contract (max-side-length mat threshold)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  (let* (
         (m (length mat))
         (n (length (car mat)))
         (prefix-sum (make-list (add1 m) (lambda (x) (make-list (add1 n) 0))))
         )
    (for* (
           (i (range 1 (add1 m)))
           (j (range 1 (add1 n)))
           )
      (set! (list-ref (list-ref prefix-sum i) j)
            (+ (list-ref (list-ref prefix-sum (sub1 i)) j)
               (list-ref (list-ref prefix-sum i) (sub1 j))
               (- (list-ref (list-ref prefix-sum (sub1 i)) (sub1 j)))
               (list-ref (list-ref mat (sub1 i)) (sub1 j))
               ))
      )
    (let loop (
           (low 1)
           (high (min m n))
           (ans 0)
           )
      (if (> low high)
          ans
          (let (
                (mid (quotient (+ low high) 2))
                )
            (if (possible mat prefix-sum threshold mid)
                (loop (add1 mid) high mid)
                (loop low (sub1 mid) ans)
                ))
           )
      )
    )
  )

(define/contract (possible mat prefix-sum threshold side)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)) exact-integer? exact-integer? boolean?)
  (let* (
         (m (length mat))
         (n (length (car mat)))
         )
    (for*/or (
             (i (range 0 (- m side + 1)))
             (j (range 0 (- n side + 1)))
             )
      (let (
            (sum (+ (list-ref (list-ref prefix-sum (+ i side)) (+ j side))
                   (- (list-ref (list-ref prefix-sum (+ i side)) j))
                   (- (list-ref (list-ref prefix-sum i) (+ j side)))
                   (list-ref (list-ref prefix-sum i) j)
                   ))
            )
        (<= sum threshold)
        )
      )
    )
  )
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
max_side_length(Mat, Threshold) ->
    M = length(Mat),
    N = length(hd(Mat)),
    PrefixSum = array:new([{size, M + 1}, {default, 0}, {fixed, true}]),
    lists:foreach(fun(I) ->
                         lists:foreach(fun(J) ->
                                           array:set(I + 1, J + 1, array:get(I, J + 1) + array:get(I + 1, J) - array:get(I, J) + lists:nth(J, lists:nth(I, Mat)), PrefixSum)
                                   end, lists:seq(1, N))
                     end, lists:seq(1, M)),
    Low = 1,
    High = min(M, N),
    Ans = 0,
    max_side_length_loop(Low, High, Ans, Mat, PrefixSum, Threshold).

max_side_length_loop(Low, High, Ans, Mat, PrefixSum, Threshold) when Low > High ->
    Ans;
max_side_length_loop(Low, High, Ans, Mat, PrefixSum, Threshold) ->
    Mid = (Low + High) div 2,
    case possible(Mat, PrefixSum, Threshold, Mid) of
        true -> max_side_length_loop(Mid + 1, High, Mid, Mat, PrefixSum, Threshold);
        false -> max_side_length_loop(Low, Mid - 1, Ans, Mat, PrefixSum, Threshold)
    end.

possible(Mat, PrefixSum, Threshold, Side) ->
    M = length(Mat),
    N = length(hd(Mat)),
    lists:any(fun(I) ->
                   lists:any(fun(J) ->
                               Sum = array:get(I + Side, J + Side, PrefixSum) - array:get(I + Side, J, PrefixSum) - array:get(I, J + Side, PrefixSum) + array:get(I, J, PrefixSum),
                               Sum =< Threshold
                           end, lists:seq(1, N - Side + 1))
               end, lists:seq(1, M - Side + 1)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  def max_side_length(mat, threshold) do
    m = length(mat)
    n = length(Enum.at(mat, 0))
    prefix_sum = Array.new(m + 1, n + 1, 0)
    Enum.reduce(1..m, prefix_sum, fn i, prefix_sum ->
      Enum.reduce(1..n, prefix_sum, fn j, prefix_sum ->
        Array.set(prefix_sum, {i, j}, Array.get(prefix_sum, {i - 1, j}) + Array.get(prefix_sum, {i, j - 1}) - Array.get(prefix_sum, {i - 1, j - 1}) + Enum.at(Enum.at(mat, i - 1), j - 1))
      end)
    end)
    low = 1
    high = min(m, n)
    ans = 0
    max_side_length_loop(low, high, ans, mat, prefix_sum, threshold)
  end

  defp max_side_length_loop(low, high, ans, mat, prefix_sum, threshold) when low > high do
    ans
  end

  defp max_side_length_loop(low, high, ans, mat, prefix_sum, threshold) do
    mid = div(low + high, 2)
    if possible(mat, prefix_sum, threshold, mid) do
      max_side_length_loop(mid + 1, high, mid, mat, prefix_sum, threshold)
    else
      max_side_length_loop(low, mid - 1, ans, mat, prefix_sum, threshold)
    end
  end

  defp possible(mat, prefix_sum, threshold, side) do
    m = length(mat)
    n = length(Enum.at(mat, 0))
    Enum.any?(1..m - side + 1, fn i ->
      Enum.any?(1..n - side + 1, fn j ->
        sum = Array.get(prefix_sum, {i + side, j + side}) - Array.get(prefix_sum, {i + side, j}) - Array.get(prefix_sum, {i, j + side}) + Array.get(prefix_sum, {i, j}),
        sum <= threshold
      end)
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this algorithm is O(m*n*log(min(m,n))) where m and n are the dimensions of the matrix. This is because we are using binary search to find the maximum valid side length, and for each side length, we are checking all possible sub-matrices of that size. The prefix sum array allows us to calculate the sum of any sub-matrix in constant time, which reduces the overall time complexity.

- **Space Complexity:** The space complexity of this algorithm is O(m*n) where m and n are the dimensions of the matrix. This is because we are storing the prefix sum array, which has the same dimensions as the input matrix. We also need to store the input matrix itself, which requires additional space.

</div>
</details>
