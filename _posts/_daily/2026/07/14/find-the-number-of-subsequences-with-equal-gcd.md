---
layout: post
title: "Find the Number of Subsequences With Equal GCD"
date: 2026-07-14 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Math", "Dynamic Programming", "Number Theory"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int subsequencePairCount(vector<int>& nums)\
        \ {\n        int MOD = 1000000007;\n        int M = 200;\n        vector<vector<int>>\
        \ dp(M + 1, vector<int>(M + 1, 0));\n        dp[0][0] = 1;\n\n        auto gcd\
        \ = [](int a, int b) {\n            while (b) {\n                a %= b;\n \
        \               std::swap(a, b);\n            }\n            return a;\n   \
        \     };\n\n        vector<vector<int>> gcd_table(M + 1, vector<int>(M + 1,\
        \ 0));\n        for (int i = 0; i <= M; ++i) {\n            for (int j = 0;\
        \ j <= M; ++j) {\n                if (i == 0) gcd_table[i][j] = j;\n       \
        \         else if (j == 0) gcd_table[i][j] = i;\n                else gcd_table[i][j]\
        \ = gcd(i, j);\n            }\n        }\n\n        for (int x : nums) {\n \
        \           vector<vector<int>> next_dp = dp;\n            for (int g1 = 0;\
        \ g1 <= M; ++g1) {\n                for (int g2 = 0; g2 <= M; ++g2) {\n    \
        \                if (dp[g1][g2] == 0) continue;\n\n                    int ng1\
        \ = gcd_table[g1][x];\n                    next_dp[ng1][g2] = (next_dp[ng1][g2]\
        \ + dp[g1][g2]) % MOD;\n\n                    int ng2 = gcd_table[g2][x];\n\
        \                    next_dp[g1][ng2] = (next_dp[g1][ng2] + dp[g1][g2]) % MOD;\n\
        \                }\n            }\n            dp = std::move(next_dp);\n  \
        \      }\n\n        long long result = 0;\n        for (int g = 1; g <= M; ++g)\
        \ {\n            result = (result + dp[g][g]) % MOD;\n        }\n        return\
        \ (int)result;\n    }\n};"
      java: "class Solution {\n    public int subsequencePairCount(int[] nums) {\n \
        \       int MOD = 1000000007;\n        int M = 200;\n        int[][] dp = new\
        \ int[M + 1][M + 1];\n        dp[0][0] = 1;\n\n        int[][] gcdTable = new\
        \ int[M + 1][M + 1];\n        for (int i = 0; i <= M; i++) {\n            for\
        \ (int j = 0; j <= M; j++) {\n                if (i == 0) gcdTable[i][j] = j;\n\
        \                else if (j == 0) gcdTable[i][j] = i;\n                else\
        \ gcdTable[i][j] = gcd(i, j);\n            }\n        }\n\n        for (int\
        \ x : nums) {\n            int[][] next_dp = new int[M + 1][M + 1];\n      \
        \      for (int i = 0; i <= M; i++) {\n                System.arraycopy(dp[i],\
        \ 0, next_dp[i], 0, M + 1);\n            }\n            for (int g1 = 0; g1\
        \ <= M; g1++) {\n                for (int g2 = 0; g2 <= M; g2++) {\n       \
        \             if (dp[g1][g2] == 0) continue;\n\n                    int ng1\
        \ = gcdTable[g1][x];\n                    next_dp[ng1][g2] = (next_dp[ng1][g2]\
        \ + dp[g1][g2]) % MOD;\n\n                    int ng2 = gcdTable[g2][x];\n \
        \                   next_dp[g1][ng2] = (next_dp[g1][ng2] + dp[g1][g2]) % MOD;\n\
        \                }\n            }\n            dp = next_dp;\n        }\n\n\
        \        long result = 0;\n        for (int g = 1; g <= M; g++) {\n        \
        \    result = (result + dp[g][g]) % MOD;\n        }\n        return (int) result;\n\
        \    }\n\n    private int gcd(int a, int b) {\n        while (b != 0) {\n  \
        \          a %= b;\n            int temp = a;\n            a = b;\n        \
        \    b = temp;\n        }\n        return a;\n    }\n}"
      python: "import math\n\nclass Solution(object):\n    def subsequencePairCount(self,\
        \ nums):\n        \"\"\"\n        :type nums: List[int]\n        :rtype: int\n\
        \        \"\"\"\n        MOD = 10**9 + 7\n        M = 200\n\n        gcd_table\
        \ = [[0] * (M + 1) for _ in range(M + 1)]\n        for i in range(M + 1):\n\
        \            for j in range(M + 1):\n                if i == 0: gcd_table[i][j]\
        \ = j\n                elif j == 0: gcd_table[i][j] = i\n                else:\n\
        \                    a, b = i, j\n                    while b: a, b = b, a %\
        \ b\n                    gcd_table[i][j] = a\n\n        dp = {(0, 0): 1}\n \
        \       for x in nums:\n            new_dp = dp.copy()\n            for (g1,\
        \ g2), count in dp.items():\n                # Choice 1: Add to first subsequence\n\
        \                ng1 = gcd_table[g1][x]\n                new_dp[(ng1, g2)] =\
        \ (new_dp.get((ng1, g2), 0) + count) % MOD\n\n                # Choice 2: Add\
        \ to second subsequence\n                ng2 = gcd_table[g2][x]\n          \
        \      new_dp[(g1, ng2)] = (new_dp.get((g1, ng2), 0) + count) % MOD\n\n    \
        \        dp = new_dp\n\n        ans = 0\n        for (g1, g2), count in dp.items():\n\
        \            if g1 == g2 and g1 > 0:\n                ans = (ans + count) %\
        \ MOD\n        return ans"
      python3: "class Solution:\n    def subsequencePairCount(self, nums: List[int])\
        \ -> int:\n        import math\n        MOD = 1000000007\n\n        gcd_table\
        \ = [[0] * 201 for _ in range(201)]\n        for i in range(201):\n        \
        \    for j in range(201):\n                if i == 0: gcd_table[i][j] = j\n\
        \                elif j == 0: gcd_table[i][j] = i\n                else: gcd_table[i][j]\
        \ = math.gcd(i, j)\n\n        dp = {(0, 0): 1}\n        for x in nums:\n   \
        \         new_dp = dp.copy()\n            for (g1, g2), count in dp.items():\n\
        \                # Add x to seq1\n                ng1 = gcd_table[g1][x]\n \
        \               if (ng1, g2) in new_dp:\n                    new_dp[(ng1, g2)]\
        \ = (new_dp[(ng1, g2)] + count) % MOD\n                else:\n             \
        \       new_dp[(ng1, g2)] = count\n\n                # Add x to seq2\n     \
        \           ng2 = gcd_table[g2][x]\n                if (g1, ng2) in new_dp:\n\
        \                    new_dp[(g1, ng2)] = (new_dp[(g1, ng2)] + count) % MOD\n\
        \                else:\n                    new_dp[(g1, ng2)] = count\n    \
        \        dp = new_dp\n\n        ans = 0\n        for (g1, g2), count in dp.items():\n\
        \            if g1 == g2 and g1 > 0:\n                ans = (ans + count) %\
        \ MOD\n        return ans"
      c: "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint gcd(int\
        \ a, int b) {\n    if (a == 0) return b;\n    while (b) {\n        int t = a\
        \ % b;\n        a = b;\n        b = t;\n    }\n    return a;\n}\n\nint subsequencePairCount(int*\
        \ nums, int numsSize) {\n    int MOD = 1000000007;\n    int (*dp)[201] = (int\
        \ (*)[201])calloc(201 * 201, sizeof(int));\n    int (*next_dp)[201] = (int (*)[201])calloc(201\
        \ * 201, sizeof(int));\n    int gcd_table[201][201];\n\n    for (int i = 0;\
        \ i <= 200; i++) {\n        for (int j = 0; j <= 200; j++) {\n            gcd_table[i][j]\
        \ = gcd(i, j);\n        }\n    }\n\n    dp[0][0] = 1;\n    for (int i = 0; i\
        \ < numsSize; i++) {\n        int x = nums[i];\n        for (int g1 = 0; g1\
        \ <= 200; g1++) {\n            memcpy(next_dp[g1], dp[g1], 201 * sizeof(int));\n\
        \        }\n        for (int g1 = 0; g1 <= 200; g1++) {\n            for (int\
        \ g2 = 0; g2 <= 200; g2++) {\n                if (dp[g1][g2] == 0) continue;\n\
        \n                int ng1 = gcd_table[g1][x];\n                next_dp[ng1][g2]\
        \ = (next_dp[ng1][g2] + dp[g1][g2]) % MOD;\n\n                int ng2 = gcd_table[g2][x];\n\
        \                next_dp[g1][ng2] = (next_dp[g1][ng2] + dp[g1][g2]) % MOD;\n\
        \            }\n        }\n        int (*temp)[201] = dp;\n        dp = next_dp;\n\
        \        next_dp = temp;\n    }\n\n    long long ans = 0;\n    for (int g =\
        \ 1; g <= 200; g++) {\n        ans = (ans + dp[g][g]) % MOD;\n    }\n\n    free(dp);\n\
        \    free(next_dp);\n    return (int)ans;\n}"
      csharp: "using System;\n\npublic class Solution {\n    public int SubsequencePairCount(int[]\
        \ nums) {\n        int MOD = 1000000007;\n        int[] dp = new int[201 * 201];\n\
        \        int[] nextDp = new int[201 * 201];\n        int[] gcdTable = new int[201\
        \ * 201];\n\n        for (int i = 0; i <= 200; i++) {\n            for (int\
        \ j = 0; j <= 200; j++) {\n                gcdTable[i * 201 + j] = Gcd(i, j);\n\
        \            }\n        }\n\n        dp[0] = 1;\n        foreach (int x in nums)\
        \ {\n            Array.Copy(dp, nextDp, 201 * 201);\n            for (int g1\
        \ = 0; g1 <= 200; g1++) {\n                int offset1 = g1 * 201;\n       \
        \         for (int g2 = 0; g2 <= 200; g2++) {\n                    int count\
        \ = dp[offset1 + g2];\n                    if (count == 0) continue;\n\n   \
        \                 int ng1 = gcdTable[g1 * 201 + x];\n                    int\
        \ idx1 = ng1 * 201 + g2;\n                    nextDp[idx1] = (nextDp[idx1] +\
        \ count) % MOD;\n\n                    int ng2 = gcdTable[g2 * 201 + x];\n \
        \                   int idx2 = offset1 + ng2;\n                    nextDp[idx2]\
        \ = (nextDp[idx2] + count) % MOD;\n                }\n            }\n      \
        \      int[] temp = dp;\n            dp = nextDp;\n            nextDp = temp;\n\
        \        }\n\n        long ans = 0;\n        for (int g = 1; g <= 200; g++)\
        \ {\n            ans = (ans + dp[g * 201 + g]) % MOD;\n        }\n        return\
        \ (int)ans;\n    }\n\n    private int Gcd(int a, int b) {\n        if (a ==\
        \ 0) return b;\n        while (b != 0) {\n            int t = a % b;\n     \
        \       a = b;\n            b = t;\n        }\n        return a;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar subsequencePairCount\
        \ = function(nums) {\n    const MOD = 1000000007;\n    const gcdTable = new\
        \ Int32Array(201 * 201);\n\n    function getGcd(a, b) {\n        if (a === 0)\
        \ return b;\n        while (b !== 0) {\n            let t = b;\n           \
        \ b = a % b;\n            a = t;\n        }\n        return a;\n    }\n\n  \
        \  for (let i = 0; i <= 200; i++) {\n        for (let j = 0; j <= 200; j++)\
        \ {\n            gcdTable[i * 201 + j] = getGcd(i, j);\n        }\n    }\n\n\
        \    let dp = new Int32Array(201 * 201);\n    let nextDp = new Int32Array(201\
        \ * 201);\n    dp[0] = 1;\n\n    for (const x of nums) {\n        nextDp.set(dp);\n\
        \        for (let g1 = 0; g1 <= 200; g1++) {\n            const offset1 = g1\
        \ * 201;\n            for (let g2 = 0; g2 <= 200; g2++) {\n                const\
        \ count = dp[offset1 + g2];\n                if (count === 0) continue;\n\n\
        \                const ng1 = gcdTable[g1 * 201 + x];\n                const\
        \ idx1 = ng1 * 201 + g2;\n                nextDp[idx1] = (nextDp[idx1] + count)\
        \ % MOD;\n\n                const ng2 = gcdTable[g2 * 201 + x];\n          \
        \      const idx2 = offset1 + ng2;\n                nextDp[idx2] = (nextDp[idx2]\
        \ + count) % MOD;\n            }\n        }\n        let temp = dp;\n      \
        \  dp = nextDp;\n        nextDp = temp;\n    }\n\n    let ans = 0;\n    for\
        \ (let g = 1; g <= 200; g++) {\n        ans = (ans + dp[g * 201 + g]) % MOD;\n\
        \    }\n    return ans;\n};"
      typescript: "function subsequencePairCount(nums: number[]): number {\n    const\
        \ MOD = 1000000007;\n    const gcdTable = Array.from({ length: 201 }, (_, i)\
        \ => {\n        const row = new Int32Array(201);\n        for (let j = 0; j\
        \ <= 200; j++) {\n            if (i === 0) row[j] = j;\n            else if\
        \ (j === 0) row[j] = i;\n            else {\n                let a = i, b =\
        \ j;\n                while (b !== 0) {\n                    a %= b;\n     \
        \               const temp = a; a = b; b = temp;\n                }\n      \
        \          row[j] = a;\n            }\n        }\n        return row;\n    });\n\
        \n    let dp = new Int32Array(201 * 201);\n    let nextDp = new Int32Array(201\
        \ * 201);\n    dp[0] = 1;\n\n    for (const x of nums) {\n        nextDp.set(dp);\n\
        \        const gcdX = new Int32Array(201);\n        for (let i = 0; i <= 200;\
        \ i++) gcdX[i] = gcdTable[i][x];\n\n        for (let g1 = 0; g1 <= 200; g1++)\
        \ {\n            const offset1 = g1 * 201;\n            const ng1Offset = gcdX[g1]\
        \ * 201;\n            for (let g2 = 0; g2 <= 200; g2++) {\n                const\
        \ count = dp[offset1 + g2];\n                if (count === 0) continue;\n\n\
        \                const idx1 = ng1Offset + g2;\n                nextDp[idx1]\
        \ = (nextDp[idx1] + count) % MOD;\n\n                const idx2 = offset1 +\
        \ gcdX[g2];\n                nextDp[idx2] = (nextDp[idx2] + count) % MOD;\n\
        \            }\n        }\n        const temp = dp;\n        dp = nextDp;\n\
        \        nextDp = temp;\n    }\n\n    let result = 0;\n    for (let g = 1; g\
        \ <= 200; g++) {\n        result = (result + dp[g * 201 + g]) % MOD;\n    }\n\
        \    return result;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function subsequencePairCount($nums) {\n        $MOD\
        \ = 1000000007;\n        $gcdTable = [];\n        for ($i = 0; $i <= 200; $i++)\
        \ {\n            for ($j = 0; $j <= 200; $j++) {\n                if ($i ==\
        \ 0) $gcdTable[$i][$j] = $j;\n                else if ($j == 0) $gcdTable[$i][$j]\
        \ = $i;\n                else {\n                    $a = $i; $b = $j;\n   \
        \                 while ($b) { $a %= $b; $temp = $a; $a = $b; $b = $temp; }\n\
        \                    $gcdTable[$i][$j] = $a;\n                }\n          \
        \  }\n        }\n\n        $dp = array_fill(0, 40401, 0);\n        $dp[0] =\
        \ 1;\n\n        foreach ($nums as $x) {\n            $nextDp = $dp;\n      \
        \      $gcdX = [];\n            for ($i = 0; $i <= 200; $i++) $gcdX[$i] = $gcdTable[$i][$x];\n\
        \n            for ($g1 = 0; $g1 <= 200; $g1++) {\n                $offset1 =\
        \ $g1 * 201;\n                $ng1Offset = $gcdX[$g1] * 201;\n             \
        \   for ($g2 = 0; $g2 <= 200; $g2++) {\n                    $count = $dp[$offset1\
        \ + $g2];\n                    if ($count === 0) continue;\n\n             \
        \       $idx1 = $ng1Offset + $g2;\n                    $nextDp[$idx1] = ($nextDp[$idx1]\
        \ + $count) % $MOD;\n\n                    $idx2 = $offset1 + $gcdX[$g2];\n\
        \                    $nextDp[$idx2] = ($nextDp[$idx2] + $count) % $MOD;\n  \
        \              }\n            }\n            $dp = $nextDp;\n        }\n\n \
        \       $result = 0;\n        for ($g = 1; $g <= 200; $g++) {\n            $result\
        \ = ($result + $dp[$g * 201 + $g]) % $MOD;\n        }\n        return $result;\n\
        \    }\n}"
      swift: "class Solution {\n    func subsequencePairCount(_ nums: [Int]) -> Int\
        \ {\n        let MOD = 1000000007\n        var gcdTable = [[Int]](repeating:\
        \ [Int](repeating: 0, count: 201), count: 201)\n        for i in 0...200 {\n\
        \            for j in 0...200 {\n                if i == 0 { gcdTable[i][j]\
        \ = j }\n                else if j == 0 { gcdTable[i][j] = i }\n           \
        \     else {\n                    var a = i, b = j\n                    while\
        \ b != 0 {\n                        a %= b\n                        let tmp\
        \ = a\n                        a = b\n                        b = tmp\n    \
        \                }\n                    gcdTable[i][j] = a\n               \
        \ }\n            }\n        }\n\n        var dp = [Int](repeating: 0, count:\
        \ 201 * 201)\n        dp[0] = 1\n\n        for x in nums {\n            var\
        \ nextDp = dp\n            let gcdX = (0...200).map { gcdTable[$0][x] }\n  \
        \          for g1 in 0...200 {\n                let offset1 = g1 * 201\n   \
        \             let ng1Offset = gcdX[g1] * 201\n                for g2 in 0...200\
        \ {\n                    let count = dp[offset1 + g2]\n                    if\
        \ count == 0 { continue }\n\n                    let idx1 = ng1Offset + g2\n\
        \                    nextDp[idx1] = (nextDp[idx1] + count) % MOD\n\n       \
        \             let idx2 = offset1 + gcdX[g2]\n                    nextDp[idx2]\
        \ = (nextDp[idx2] + count) % MOD\n                }\n            }\n       \
        \     dp = nextDp\n        }\n\n        var result = 0\n        for g in 1...200\
        \ {\n            result = (result + dp[g * 201 + g]) % MOD\n        }\n    \
        \    return result\n    }\n}"
      kotlin: "class Solution {\n    fun subsequencePairCount(nums: IntArray): Int {\n\
        \        val MOD = 1000000007\n        val gcdTable = Array(201) { i ->\n  \
        \          IntArray(201) { j ->\n                if (i == 0) j\n           \
        \     else if (j == 0) i\n                else {\n                    var a\
        \ = i\n                    var b = j\n                    while (b != 0) {\n\
        \                        a %= b\n                        val temp = a\n    \
        \                    a = b\n                        b = temp\n             \
        \       }\n                    a\n                }\n            }\n       \
        \ }\n\n        var dp = IntArray(201 * 201)\n        var nextDp = IntArray(201\
        \ * 201)\n        dp[0] = 1\n\n        for (x in nums) {\n            System.arraycopy(dp,\
        \ 0, nextDp, 0, dp.size)\n            val gcdX = IntArray(201) { i -> gcdTable[i][x]\
        \ }\n\n            for (g1 in 0..200) {\n                val offset1 = g1 *\
        \ 201\n                val ng1Offset = gcdX[g1] * 201\n                for (g2\
        \ in 0..200) {\n                    val count = dp[offset1 + g2]\n         \
        \           if (count == 0) continue\n\n                    val idx1 = ng1Offset\
        \ + g2\n                    nextDp[idx1] = (nextDp[idx1] + count) % MOD\n\n\
        \                    val idx2 = offset1 + gcdX[g2]\n                    nextDp[idx2]\
        \ = (nextDp[idx2] + count) % MOD\n                }\n            }\n       \
        \     val temp = dp\n            dp = nextDp\n            nextDp = temp\n  \
        \      }\n\n        var result = 0L\n        for (g in 1..200) {\n         \
        \   result = (result + dp[g * 201 + g]) % MOD\n        }\n        return result.toInt()\n\
        \    }\n}"
      dart: "import 'dart:typed_data';\n\nclass Solution {\n  int subsequencePairCount(List<int>\
        \ nums) {\n    const int MOD = 1000000007;\n    const int MAX_VAL = 200;\n \
        \   const int SIZE = 201;\n\n    List<List<int>> gcdTable = List.generate(SIZE,\
        \ (i) {\n      return List.generate(SIZE, (j) {\n        int a = i;\n      \
        \  int b = j;\n        while (b != 0) {\n          a %= b;\n          int temp\
        \ = a;\n          a = b;\n          b = temp;\n        }\n        return a;\n\
        \      });\n    });\n\n    Int32List dp = Int32List(SIZE * SIZE);\n    dp[0]\
        \ = 1;\n\n    for (int x in nums) {\n      Int32List nextDp = Int32List.fromList(dp);\n\
        \      for (int g1 = 0; g1 < SIZE; g1++) {\n        int g1Off = g1 * SIZE;\n\
        \        int ng1Off = gcdTable[g1][x] * SIZE;\n        for (int g2 = 0; g2 <\
        \ SIZE; g2++) {\n          int v = dp[g1Off + g2];\n          if (v == 0) continue;\n\
        \n          int idx1 = ng1Off + g2;\n          nextDp[idx1] = (nextDp[idx1]\
        \ + v) % MOD;\n\n          int idx2 = g1Off + gcdTable[g2][x];\n          nextDp[idx2]\
        \ = (nextDp[idx2] + v) % MOD;\n        }\n      }\n      dp = nextDp;\n    }\n\
        \n    int ans = 0;\n    for (int g = 1; g < SIZE; g++) {\n      ans = (ans +\
        \ dp[g * SIZE + g]) % MOD;\n    }\n\n    return ans;\n  }\n}"
      go: "func subsequencePairCount(nums []int) int {\n\tconst MOD = 1000000007\n\t\
        const SIZE = 201\n\n\tgcdTable := [SIZE][SIZE]int{}\n\tfor i := 0; i < SIZE;\
        \ i++ {\n\t\tfor j := 0; j < SIZE; j++ {\n\t\t\ta, b := i, j\n\t\t\tfor b !=\
        \ 0 {\n\t\t\t\ta %= b\n\t\t\t\ta, b = b, a\n\t\t\t}\n\t\t\tgcdTable[i][j] =\
        \ a\n\t\t}\n\t}\n\n\tdp := make([]int, SIZE*SIZE)\n\tnewDp := make([]int, SIZE*SIZE)\n\
        \tdp[0] = 1\n\n\tfor _, x := range nums {\n\t\tcopy(newDp, dp)\n\t\tfor g1 :=\
        \ 0; g1 < SIZE; g1++ {\n\t\t\tg1Off := g1 * SIZE\n\t\t\tng1Off := gcdTable[g1][x]\
        \ * SIZE\n\t\t\tfor g2 := 0; g2 < SIZE; g2++ {\n\t\t\t\tv := dp[g1Off+g2]\n\t\
        \t\t\tif v == 0 {\n\t\t\t\t\tcontinue\n\t\t\t\t}\n\t\t\t\tidx1 := ng1Off + g2\n\
        \t\t\t\tnewDp[idx1] = (newDp[idx1] + v) % MOD\n\n\t\t\t\tidx2 := g1Off + gcdTable[g2][x]\n\
        \t\t\t\tnewDp[idx2] = (newDp[idx2] + v) % MOD\n\t\t\t}\n\t\t}\n\t\tdp, newDp\
        \ = newDp, dp\n\t}\n\n\tans := 0\n\tfor g := 1; g < SIZE; g++ {\n\t\tans = (ans\
        \ + dp[g*SIZE+g]) % MOD\n\t}\n\n\treturn ans\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef subsequence_pair_count(nums)\n\
        \  mod = 1_000_000_007\n  size = 201\n  gcd_table = Array.new(size) { Array.new(size)\
        \ }\n  (0...size).each do |i|\n    (0...size).each do |j|\n      gcd_table[i][j]\
        \ = i.gcd(j)\n    end\n  end\n\n  dp = Array.new(size * size, 0)\n  dp[0] =\
        \ 1\n\n  nums.each do |x|\n    new_dp = dp.dup\n    (0...size).each do |g1|\n\
        \      g1_off = g1 * size\n      ng1_off = gcd_table[g1][x] * size\n      (0...size).each\
        \ do |g2|\n        v = dp[g1_off + g2]\n        next if v == 0\n\n        idx1\
        \ = ng1_off + g2\n        new_dp[idx1] = (new_dp[idx1] + v) % mod\n\n      \
        \  idx2 = g1_off + gcd_table[g2][x]\n        new_dp[idx2] = (new_dp[idx2] +\
        \ v) % mod\n      end\n    end\n    dp = new_dp\n  end\n\n  ans = 0\n  (1...size).each\
        \ do |g|\n    ans = (ans + dp[g * size + g]) % mod\n  end\n  ans\nend"
      scala: "object Solution {\n    def subsequencePairCount(nums: Array[Int]): Int\
        \ = {\n        val MOD = 1000000007\n        val SIZE = 201\n        val gcdTable\
        \ = Array.ofDim[Int](SIZE, SIZE)\n\n        def gcd(a: Int, b: Int): Int = {\n\
        \            var x = a\n            var y = b\n            while (y != 0) {\n\
        \                x %= y\n                val temp = x\n                x = y\n\
        \                y = temp\n            }\n            x\n        }\n\n     \
        \   for (i <- 0 until SIZE) {\n            for (j <- 0 until SIZE) {\n     \
        \           gcdTable(i)(j) = gcd(i, j)\n            }\n        }\n\n       \
        \ var dp = new Array[Int](SIZE * SIZE)\n        dp(0) = 1\n\n        for (x\
        \ <- nums) {\n            val nextDp = dp.clone()\n            var g1 = 0\n\
        \            while (g1 < SIZE) {\n                val g1Off = g1 * SIZE\n  \
        \              val ng1Off = gcdTable(g1)(x) * SIZE\n                var g2 =\
        \ 0\n                while (g2 < SIZE) {\n                    val v = dp(g1Off\
        \ + g2)\n                    if (v > 0) {\n                        val idx1\
        \ = ng1Off + g2\n                        nextDp(idx1) = (nextDp(idx1) + v) %\
        \ MOD\n\n                        val idx2 = g1Off + gcdTable(g2)(x)\n      \
        \                  nextDp(idx2) = (nextDp(idx2) + v) % MOD\n               \
        \     }\n                    g2 += 1\n                }\n                g1\
        \ += 1\n            }\n            dp = nextDp\n        }\n\n        var ans\
        \ = 0L\n        for (g <- 1 until SIZE) {\n            ans = (ans + dp(g * SIZE\
        \ + g)) % MOD\n        }\n\n        ans.toInt\n    }\n}"
      rust: "impl Solution {\n    pub fn subsequence_pair_count(nums: Vec<i32>) -> i32\
        \ {\n        let m = 201;\n        let mut dp = vec![0i32; m * m];\n       \
        \ let mod_val = 1_000_000_007;\n\n        fn gcd(mut a: usize, mut b: usize)\
        \ -> usize {\n            while b != 0 {\n                a %= b;\n        \
        \        std::mem::swap(&mut a, &mut b);\n            }\n            a\n   \
        \     }\n\n        dp[0] = 1;\n\n        for &x_i32 in &nums {\n           \
        \ let x = x_i32 as usize;\n            let mut next_dp = dp.clone();\n     \
        \       for g1 in 0..m {\n                let offset = g1 * m;\n           \
        \     for g2 in 0..m {\n                    let count = dp[offset + g2];\n \
        \                   if count == 0 { continue; }\n\n                    let ng1\
        \ = if g1 == 0 { x } else { gcd(g1, x) };\n                    let idx1 = ng1\
        \ * m + g2;\n                    next_dp[idx1] = (next_dp[idx1] + count) % mod_val;\n\
        \n                    let ng2 = if g2 == 0 { x } else { gcd(g2, x) };\n    \
        \                let idx2 = offset + ng2;\n                    next_dp[idx2]\
        \ = (next_dp[idx2] + count) % mod_val;\n                }\n            }\n \
        \           dp = next_dp;\n        }\n\n        let mut ans = 0;\n        for\
        \ g in 1..m {\n            ans = (ans + dp[g * m + g]) % mod_val;\n        }\n\
        \        ans\n    }\n}"
      racket: "(define (gcd-func a b)\n  (if (zero? b) a (gcd-func b (remainder a b))))\n\
        \n(define/contract (subsequence-pair-count nums)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let* ([mod-val 1000000007]\n         [m 201]\n       \
        \  [dp (make-vector (* m m) 0)])\n    (vector-set! dp 0 1)\n    (for ([x nums])\n\
        \      (let ([next-dp (vector-copy dp)])\n        (for ([g1 (in-range m)])\n\
        \          (let ([offset (* g1 m)])\n            (for ([g2 (in-range m)])\n\
        \              (let ([count (vector-ref dp (+ offset g2))])\n              \
        \  (when (> count 0)\n                  (let* ([ng1 (gcd-func g1 x)]\n     \
        \                    [ng2 (gcd-func g2 x)]\n                         [idx1 (+\
        \ (* ng1 m) g2)]\n                         [idx2 (+ offset ng2)])\n        \
        \            (vector-set! next-dp idx1 (modulo (+ (vector-ref next-dp idx1)\
        \ count) mod-val))\n                    (vector-set! next-dp idx2 (modulo (+\
        \ (vector-ref next-dp idx2) count) mod-val))))))))\n        (set! dp next-dp)))\n\
        \    (let ([ans 0])\n      (for ([g (in-range 1 m)])\n        (set! ans (modulo\
        \ (+ ans (vector-ref dp (+ (* g m) g))) mod-val)))\n      ans)))"
      erlang: "-spec subsequence_pair_count(Nums :: [integer()]) -> integer().\nsubsequence_pair_count(Nums)\
        \ ->\n    ModVal = 1000000007,\n    InitialDP = #{{0, 0} => 1},\n    FinalDP\
        \ = lists:foldl(fun(X, AccDP) ->\n        maps:fold(fun({G1, G2}, Count, NextDP)\
        \ ->\n            NG1 = gcd(G1, X),\n            NG2 = gcd(G2, X),\n       \
        \     NextDP1 = maps:put({NG1, G2}, (maps:get({NG1, G2}, NextDP, 0) + Count)\
        \ rem ModVal, NextDP),\n            maps:put({G1, NG2}, (maps:get({G1, NG2},\
        \ NextDP1, 0) + Count) rem ModVal, NextDP1)\n        end, AccDP, AccDP)\n  \
        \  end, InitialDP, Nums),\n    lists:foldl(fun(G, Acc) ->\n        (Acc + maps:get({G,\
        \ G}, FinalDP, 0)) rem ModVal\n    end, 0, lists:seq(1, 200)).\n\ngcd(A, 0)\
        \ -> A;\ngcd(A, B) -> gcd(B, A rem B)."
      elixir: "defmodule Solution do\n  @spec subsequence_pair_count(nums :: [integer])\
        \ :: integer\n  def subsequence_pair_count(nums) do\n    mod_val = 1_000_000_007\n\
        \    initial_dp = %{{0, 0} => 1}\n\n    final_dp = Enum.reduce(nums, initial_dp,\
        \ fn x, acc_dp ->\n      Enum.reduce(acc_dp, acc_dp, fn {{g1, g2}, count}, next_dp\
        \ ->\n        ng1 = if g1 == 0, do: x, else: Integer.gcd(g1, x)\n        ng2\
        \ = if g2 == 0, do: x, else: Integer.gcd(g2, x)\n\n        next_dp = Map.put(next_dp,\
        \ {ng1, g2}, rem(Map.get(next_dp, {ng1, g2}, 0) + count, mod_val))\n       \
        \ Map.put(next_dp, {g1, ng2}, rem(Map.get(next_dp, {g1, ng2}, 0) + count, mod_val))\n\
        \      end)\n    end)\n\n    Enum.reduce(1..200, 0, fn g, acc ->\n      rem(acc\
        \ + Map.get(final_dp, {g, g}, 0), mod_val)\n    end)\n  end\nend"
    approach: 'The problem asks for the number of pairs of disjoint non-empty subsequences
      with equal greatest common divisors (GCD). Since the maximum value in the array
      is 200 and the array length is also up to 200, we can use dynamic programming
      with a state representing the GCDs of the two subsequences. Let $dp[g_1][g_2]$
      be the number of ways to form two disjoint subsequences such that the first has
      GCD $g_1$ and the second has GCD $g_2$. We initialize $dp[0][0] = 1$, where a
      GCD of 0 signifies an empty subsequence. For each element $x$ in the array, we
      can either add it to the first subsequence, the second subsequence, or neither,
      effectively transitioning from the previous state $dp$ to a new state $next\_dp$.


      The transitions are as follows: for each reachable state $(g_1, g_2)$, adding
      $x$ to the first subsequence results in a new GCD $ng_1 = \gcd(g_1, x)$, whereas
      adding it to the second results in $ng_2 = \gcd(g_2, x)$. If $x$ is not added
      to either, the state remains $(g_1, g_2)$. By using a temporary DP table (or a
      copy) for each element, we ensure that every index is used at most once. Finally,
      the answer is the sum of $dp[g][g]$ for all $g \in [1, 200]$, ensuring that both
      subsequences are non-empty and have identical GCDs.'
    time_complexity: O(N * M^2) where N is the length of the input array (up to 200)
      and M is the maximum value in the array (up to 200). For each of the N elements,
      we iterate over a DP table of size $(M+1) \times (M+1)$, leading to approximately
      $200 \times 201^2 \approx 8 \times 10^6$ operations, which is efficient for the
      given constraints.
    space_complexity: O(M^2) as we maintain a 2D DP table of size $(M+1) \times (M+1)$
      to store the number of ways to achieve every possible pair of GCDs. This consumes
      roughly $201 \times 201 \times 4$ bytes, which is well within the typical memory
      limits.
    elapsed_time: 1888.115093946457
    model: gemini-3-flash-preview
    generated_at: '2026-07-14 02:19:46 '
---

## Problem #3336: Find the Number of Subsequences With Equal GCD

**Difficulty:** Hard

**Topics:** Array, Math, Dynamic Programming, Number Theory

## Problem Description

<p>You are given an integer array <code>nums</code>.</p>

<p>Your task is to find the number of pairs of <strong>non-empty</strong> <span data-keyword="subsequence-array">subsequences</span> <code>(seq1, seq2)</code> of <code>nums</code> that satisfy the following conditions:</p>

<ul>
	<li>The subsequences <code>seq1</code> and <code>seq2</code> are <strong>disjoint</strong>, meaning <strong>no index</strong> of <code>nums</code> is common between them.</li>
	<li>The <span data-keyword="gcd-function">GCD</span> of the elements of <code>seq1</code> is equal to the GCD of the elements of <code>seq2</code>.</li>
</ul>

<p>Return the total number of such pairs.</p>

<p>Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">10</span></p>

<p><strong>Explanation:</strong></p>

<p>The subsequence pairs which have the GCD of their elements equal to 1 are:</p>

<ul>
	<li><code>([<strong><u>1</u></strong>, 2, 3, 4], [1, <strong><u>2</u></strong>, <strong><u>3</u></strong>, 4])</code></li>
	<li><code>([<strong><u>1</u></strong>, 2, 3, 4], [1, <strong><u>2</u></strong>, <strong><u>3</u></strong>, <strong><u>4</u></strong>])</code></li>
	<li><code>([<strong><u>1</u></strong>, 2, 3, 4], [1, 2, <strong><u>3</u></strong>, <strong><u>4</u></strong>])</code></li>
	<li><code>([<strong><u>1</u></strong>, <strong><u>2</u></strong>, 3, 4], [1, 2, <strong><u>3</u></strong>, <strong><u>4</u></strong>])</code></li>
	<li><code>([<strong><u>1</u></strong>, 2, 3, <strong><u>4</u></strong>], [1, <strong><u>2</u></strong>, <strong><u>3</u></strong>, 4])</code></li>
	<li><code>([1, <strong><u>2</u></strong>, <strong><u>3</u></strong>, 4], [<strong><u>1</u></strong>, 2, 3, 4])</code></li>
	<li><code>([1, <strong><u>2</u></strong>, <strong><u>3</u></strong>, 4], [<strong><u>1</u></strong>, 2, 3, <strong><u>4</u></strong>])</code></li>
	<li><code>([1, <strong><u>2</u></strong>, <strong><u>3</u></strong>, <strong><u>4</u></strong>], [<strong><u>1</u></strong>, 2, 3, 4])</code></li>
	<li><code>([1, 2, <strong><u>3</u></strong>, <strong><u>4</u></strong>], [<strong><u>1</u></strong>, 2, 3, 4])</code></li>
	<li><code>([1, 2, <strong><u>3</u></strong>, <strong><u>4</u></strong>], [<strong><u>1</u></strong>, <strong><u>2</u></strong>, 3, 4])</code></li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [10,20,30]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The subsequence pairs which have the GCD of their elements equal to 10 are:</p>

<ul>
	<li><code>([<strong><u>10</u></strong>, 20, 30], [10, <strong><u>20</u></strong>, <strong><u>30</u></strong>])</code></li>
	<li><code>([10, <strong><u>20</u></strong>, <strong><u>30</u></strong>], [<strong><u>10</u></strong>, 20, 30])</code></li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,1,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">50</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 200</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 200</code></li>
</ul>


## Hints

1. Use dynamic programming to store number of subsequences up till index `i` with GCD `g1` and `g2`.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the number of pairs of disjoint non-empty subsequences with equal greatest common divisors (GCD). Since the maximum value in the array is 200 and the array length is also up to 200, we can use dynamic programming with a state representing the GCDs of the two subsequences. Let $dp[g_1][g_2]$ be the number of ways to form two disjoint subsequences such that the first has GCD $g_1$ and the second has GCD $g_2$. We initialize $dp[0][0] = 1$, where a GCD of 0 signifies an empty subsequence. For each element $x$ in the array, we can either add it to the first subsequence, the second subsequence, or neither, effectively transitioning from the previous state $dp$ to a new state $next\_dp$.

The transitions are as follows: for each reachable state $(g_1, g_2)$, adding $x$ to the first subsequence results in a new GCD $ng_1 = \gcd(g_1, x)$, whereas adding it to the second results in $ng_2 = \gcd(g_2, x)$. If $x$ is not added to either, the state remains $(g_1, g_2)$. By using a temporary DP table (or a copy) for each element, we ensure that every index is used at most once. Finally, the answer is the sum of $dp[g][g]$ for all $g \in [1, 200]$, ensuring that both subsequences are non-empty and have identical GCDs.

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
    int subsequencePairCount(vector<int>& nums) {
        int MOD = 1000000007;
        int M = 200;
        vector<vector<int>> dp(M + 1, vector<int>(M + 1, 0));
        dp[0][0] = 1;

        auto gcd = [](int a, int b) {
            while (b) {
                a %= b;
                std::swap(a, b);
            }
            return a;
        };

        vector<vector<int>> gcd_table(M + 1, vector<int>(M + 1, 0));
        for (int i = 0; i <= M; ++i) {
            for (int j = 0; j <= M; ++j) {
                if (i == 0) gcd_table[i][j] = j;
                else if (j == 0) gcd_table[i][j] = i;
                else gcd_table[i][j] = gcd(i, j);
            }
        }

        for (int x : nums) {
            vector<vector<int>> next_dp = dp;
            for (int g1 = 0; g1 <= M; ++g1) {
                for (int g2 = 0; g2 <= M; ++g2) {
                    if (dp[g1][g2] == 0) continue;

                    int ng1 = gcd_table[g1][x];
                    next_dp[ng1][g2] = (next_dp[ng1][g2] + dp[g1][g2]) % MOD;

                    int ng2 = gcd_table[g2][x];
                    next_dp[g1][ng2] = (next_dp[g1][ng2] + dp[g1][g2]) % MOD;
                }
            }
            dp = std::move(next_dp);
        }

        long long result = 0;
        for (int g = 1; g <= M; ++g) {
            result = (result + dp[g][g]) % MOD;
        }
        return (int)result;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int subsequencePairCount(int[] nums) {
        int MOD = 1000000007;
        int M = 200;
        int[][] dp = new int[M + 1][M + 1];
        dp[0][0] = 1;

        int[][] gcdTable = new int[M + 1][M + 1];
        for (int i = 0; i <= M; i++) {
            for (int j = 0; j <= M; j++) {
                if (i == 0) gcdTable[i][j] = j;
                else if (j == 0) gcdTable[i][j] = i;
                else gcdTable[i][j] = gcd(i, j);
            }
        }

        for (int x : nums) {
            int[][] next_dp = new int[M + 1][M + 1];
            for (int i = 0; i <= M; i++) {
                System.arraycopy(dp[i], 0, next_dp[i], 0, M + 1);
            }
            for (int g1 = 0; g1 <= M; g1++) {
                for (int g2 = 0; g2 <= M; g2++) {
                    if (dp[g1][g2] == 0) continue;

                    int ng1 = gcdTable[g1][x];
                    next_dp[ng1][g2] = (next_dp[ng1][g2] + dp[g1][g2]) % MOD;

                    int ng2 = gcdTable[g2][x];
                    next_dp[g1][ng2] = (next_dp[g1][ng2] + dp[g1][g2]) % MOD;
                }
            }
            dp = next_dp;
        }

        long result = 0;
        for (int g = 1; g <= M; g++) {
            result = (result + dp[g][g]) % MOD;
        }
        return (int) result;
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            a %= b;
            int temp = a;
            a = b;
            b = temp;
        }
        return a;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import math

class Solution(object):
    def subsequencePairCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        M = 200

        gcd_table = [[0] * (M + 1) for _ in range(M + 1)]
        for i in range(M + 1):
            for j in range(M + 1):
                if i == 0: gcd_table[i][j] = j
                elif j == 0: gcd_table[i][j] = i
                else:
                    a, b = i, j
                    while b: a, b = b, a % b
                    gcd_table[i][j] = a

        dp = {(0, 0): 1}
        for x in nums:
            new_dp = dp.copy()
            for (g1, g2), count in dp.items():
                # Choice 1: Add to first subsequence
                ng1 = gcd_table[g1][x]
                new_dp[(ng1, g2)] = (new_dp.get((ng1, g2), 0) + count) % MOD

                # Choice 2: Add to second subsequence
                ng2 = gcd_table[g2][x]
                new_dp[(g1, ng2)] = (new_dp.get((g1, ng2), 0) + count) % MOD

            dp = new_dp

        ans = 0
        for (g1, g2), count in dp.items():
            if g1 == g2 and g1 > 0:
                ans = (ans + count) % MOD
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        import math
        MOD = 1000000007

        gcd_table = [[0] * 201 for _ in range(201)]
        for i in range(201):
            for j in range(201):
                if i == 0: gcd_table[i][j] = j
                elif j == 0: gcd_table[i][j] = i
                else: gcd_table[i][j] = math.gcd(i, j)

        dp = {(0, 0): 1}
        for x in nums:
            new_dp = dp.copy()
            for (g1, g2), count in dp.items():
                # Add x to seq1
                ng1 = gcd_table[g1][x]
                if (ng1, g2) in new_dp:
                    new_dp[(ng1, g2)] = (new_dp[(ng1, g2)] + count) % MOD
                else:
                    new_dp[(ng1, g2)] = count

                # Add x to seq2
                ng2 = gcd_table[g2][x]
                if (g1, ng2) in new_dp:
                    new_dp[(g1, ng2)] = (new_dp[(g1, ng2)] + count) % MOD
                else:
                    new_dp[(g1, ng2)] = count
            dp = new_dp

        ans = 0
        for (g1, g2), count in dp.items():
            if g1 == g2 and g1 > 0:
                ans = (ans + count) % MOD
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int gcd(int a, int b) {
    if (a == 0) return b;
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

int subsequencePairCount(int* nums, int numsSize) {
    int MOD = 1000000007;
    int (*dp)[201] = (int (*)[201])calloc(201 * 201, sizeof(int));
    int (*next_dp)[201] = (int (*)[201])calloc(201 * 201, sizeof(int));
    int gcd_table[201][201];

    for (int i = 0; i <= 200; i++) {
        for (int j = 0; j <= 200; j++) {
            gcd_table[i][j] = gcd(i, j);
        }
    }

    dp[0][0] = 1;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        for (int g1 = 0; g1 <= 200; g1++) {
            memcpy(next_dp[g1], dp[g1], 201 * sizeof(int));
        }
        for (int g1 = 0; g1 <= 200; g1++) {
            for (int g2 = 0; g2 <= 200; g2++) {
                if (dp[g1][g2] == 0) continue;

                int ng1 = gcd_table[g1][x];
                next_dp[ng1][g2] = (next_dp[ng1][g2] + dp[g1][g2]) % MOD;

                int ng2 = gcd_table[g2][x];
                next_dp[g1][ng2] = (next_dp[g1][ng2] + dp[g1][g2]) % MOD;
            }
        }
        int (*temp)[201] = dp;
        dp = next_dp;
        next_dp = temp;
    }

    long long ans = 0;
    for (int g = 1; g <= 200; g++) {
        ans = (ans + dp[g][g]) % MOD;
    }

    free(dp);
    free(next_dp);
    return (int)ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public int SubsequencePairCount(int[] nums) {
        int MOD = 1000000007;
        int[] dp = new int[201 * 201];
        int[] nextDp = new int[201 * 201];
        int[] gcdTable = new int[201 * 201];

        for (int i = 0; i <= 200; i++) {
            for (int j = 0; j <= 200; j++) {
                gcdTable[i * 201 + j] = Gcd(i, j);
            }
        }

        dp[0] = 1;
        foreach (int x in nums) {
            Array.Copy(dp, nextDp, 201 * 201);
            for (int g1 = 0; g1 <= 200; g1++) {
                int offset1 = g1 * 201;
                for (int g2 = 0; g2 <= 200; g2++) {
                    int count = dp[offset1 + g2];
                    if (count == 0) continue;

                    int ng1 = gcdTable[g1 * 201 + x];
                    int idx1 = ng1 * 201 + g2;
                    nextDp[idx1] = (nextDp[idx1] + count) % MOD;

                    int ng2 = gcdTable[g2 * 201 + x];
                    int idx2 = offset1 + ng2;
                    nextDp[idx2] = (nextDp[idx2] + count) % MOD;
                }
            }
            int[] temp = dp;
            dp = nextDp;
            nextDp = temp;
        }

        long ans = 0;
        for (int g = 1; g <= 200; g++) {
            ans = (ans + dp[g * 201 + g]) % MOD;
        }
        return (int)ans;
    }

    private int Gcd(int a, int b) {
        if (a == 0) return b;
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
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
 * @return {number}
 */
var subsequencePairCount = function(nums) {
    const MOD = 1000000007;
    const gcdTable = new Int32Array(201 * 201);

    function getGcd(a, b) {
        if (a === 0) return b;
        while (b !== 0) {
            let t = b;
            b = a % b;
            a = t;
        }
        return a;
    }

    for (let i = 0; i <= 200; i++) {
        for (let j = 0; j <= 200; j++) {
            gcdTable[i * 201 + j] = getGcd(i, j);
        }
    }

    let dp = new Int32Array(201 * 201);
    let nextDp = new Int32Array(201 * 201);
    dp[0] = 1;

    for (const x of nums) {
        nextDp.set(dp);
        for (let g1 = 0; g1 <= 200; g1++) {
            const offset1 = g1 * 201;
            for (let g2 = 0; g2 <= 200; g2++) {
                const count = dp[offset1 + g2];
                if (count === 0) continue;

                const ng1 = gcdTable[g1 * 201 + x];
                const idx1 = ng1 * 201 + g2;
                nextDp[idx1] = (nextDp[idx1] + count) % MOD;

                const ng2 = gcdTable[g2 * 201 + x];
                const idx2 = offset1 + ng2;
                nextDp[idx2] = (nextDp[idx2] + count) % MOD;
            }
        }
        let temp = dp;
        dp = nextDp;
        nextDp = temp;
    }

    let ans = 0;
    for (let g = 1; g <= 200; g++) {
        ans = (ans + dp[g * 201 + g]) % MOD;
    }
    return ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function subsequencePairCount(nums: number[]): number {
    const MOD = 1000000007;
    const gcdTable = Array.from({ length: 201 }, (_, i) => {
        const row = new Int32Array(201);
        for (let j = 0; j <= 200; j++) {
            if (i === 0) row[j] = j;
            else if (j === 0) row[j] = i;
            else {
                let a = i, b = j;
                while (b !== 0) {
                    a %= b;
                    const temp = a; a = b; b = temp;
                }
                row[j] = a;
            }
        }
        return row;
    });

    let dp = new Int32Array(201 * 201);
    let nextDp = new Int32Array(201 * 201);
    dp[0] = 1;

    for (const x of nums) {
        nextDp.set(dp);
        const gcdX = new Int32Array(201);
        for (let i = 0; i <= 200; i++) gcdX[i] = gcdTable[i][x];

        for (let g1 = 0; g1 <= 200; g1++) {
            const offset1 = g1 * 201;
            const ng1Offset = gcdX[g1] * 201;
            for (let g2 = 0; g2 <= 200; g2++) {
                const count = dp[offset1 + g2];
                if (count === 0) continue;

                const idx1 = ng1Offset + g2;
                nextDp[idx1] = (nextDp[idx1] + count) % MOD;

                const idx2 = offset1 + gcdX[g2];
                nextDp[idx2] = (nextDp[idx2] + count) % MOD;
            }
        }
        const temp = dp;
        dp = nextDp;
        nextDp = temp;
    }

    let result = 0;
    for (let g = 1; g <= 200; g++) {
        result = (result + dp[g * 201 + g]) % MOD;
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
     * @return Integer
     */
    function subsequencePairCount($nums) {
        $MOD = 1000000007;
        $gcdTable = [];
        for ($i = 0; $i <= 200; $i++) {
            for ($j = 0; $j <= 200; $j++) {
                if ($i == 0) $gcdTable[$i][$j] = $j;
                else if ($j == 0) $gcdTable[$i][$j] = $i;
                else {
                    $a = $i; $b = $j;
                    while ($b) { $a %= $b; $temp = $a; $a = $b; $b = $temp; }
                    $gcdTable[$i][$j] = $a;
                }
            }
        }

        $dp = array_fill(0, 40401, 0);
        $dp[0] = 1;

        foreach ($nums as $x) {
            $nextDp = $dp;
            $gcdX = [];
            for ($i = 0; $i <= 200; $i++) $gcdX[$i] = $gcdTable[$i][$x];

            for ($g1 = 0; $g1 <= 200; $g1++) {
                $offset1 = $g1 * 201;
                $ng1Offset = $gcdX[$g1] * 201;
                for ($g2 = 0; $g2 <= 200; $g2++) {
                    $count = $dp[$offset1 + $g2];
                    if ($count === 0) continue;

                    $idx1 = $ng1Offset + $g2;
                    $nextDp[$idx1] = ($nextDp[$idx1] + $count) % $MOD;

                    $idx2 = $offset1 + $gcdX[$g2];
                    $nextDp[$idx2] = ($nextDp[$idx2] + $count) % $MOD;
                }
            }
            $dp = $nextDp;
        }

        $result = 0;
        for ($g = 1; $g <= 200; $g++) {
            $result = ($result + $dp[$g * 201 + $g]) % $MOD;
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
    func subsequencePairCount(_ nums: [Int]) -> Int {
        let MOD = 1000000007
        var gcdTable = [[Int]](repeating: [Int](repeating: 0, count: 201), count: 201)
        for i in 0...200 {
            for j in 0...200 {
                if i == 0 { gcdTable[i][j] = j }
                else if j == 0 { gcdTable[i][j] = i }
                else {
                    var a = i, b = j
                    while b != 0 {
                        a %= b
                        let tmp = a
                        a = b
                        b = tmp
                    }
                    gcdTable[i][j] = a
                }
            }
        }

        var dp = [Int](repeating: 0, count: 201 * 201)
        dp[0] = 1

        for x in nums {
            var nextDp = dp
            let gcdX = (0...200).map { gcdTable[$0][x] }
            for g1 in 0...200 {
                let offset1 = g1 * 201
                let ng1Offset = gcdX[g1] * 201
                for g2 in 0...200 {
                    let count = dp[offset1 + g2]
                    if count == 0 { continue }

                    let idx1 = ng1Offset + g2
                    nextDp[idx1] = (nextDp[idx1] + count) % MOD

                    let idx2 = offset1 + gcdX[g2]
                    nextDp[idx2] = (nextDp[idx2] + count) % MOD
                }
            }
            dp = nextDp
        }

        var result = 0
        for g in 1...200 {
            result = (result + dp[g * 201 + g]) % MOD
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
    fun subsequencePairCount(nums: IntArray): Int {
        val MOD = 1000000007
        val gcdTable = Array(201) { i ->
            IntArray(201) { j ->
                if (i == 0) j
                else if (j == 0) i
                else {
                    var a = i
                    var b = j
                    while (b != 0) {
                        a %= b
                        val temp = a
                        a = b
                        b = temp
                    }
                    a
                }
            }
        }

        var dp = IntArray(201 * 201)
        var nextDp = IntArray(201 * 201)
        dp[0] = 1

        for (x in nums) {
            System.arraycopy(dp, 0, nextDp, 0, dp.size)
            val gcdX = IntArray(201) { i -> gcdTable[i][x] }

            for (g1 in 0..200) {
                val offset1 = g1 * 201
                val ng1Offset = gcdX[g1] * 201
                for (g2 in 0..200) {
                    val count = dp[offset1 + g2]
                    if (count == 0) continue

                    val idx1 = ng1Offset + g2
                    nextDp[idx1] = (nextDp[idx1] + count) % MOD

                    val idx2 = offset1 + gcdX[g2]
                    nextDp[idx2] = (nextDp[idx2] + count) % MOD
                }
            }
            val temp = dp
            dp = nextDp
            nextDp = temp
        }

        var result = 0L
        for (g in 1..200) {
            result = (result + dp[g * 201 + g]) % MOD
        }
        return result.toInt()
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
  int subsequencePairCount(List<int> nums) {
    const int MOD = 1000000007;
    const int MAX_VAL = 200;
    const int SIZE = 201;

    List<List<int>> gcdTable = List.generate(SIZE, (i) {
      return List.generate(SIZE, (j) {
        int a = i;
        int b = j;
        while (b != 0) {
          a %= b;
          int temp = a;
          a = b;
          b = temp;
        }
        return a;
      });
    });

    Int32List dp = Int32List(SIZE * SIZE);
    dp[0] = 1;

    for (int x in nums) {
      Int32List nextDp = Int32List.fromList(dp);
      for (int g1 = 0; g1 < SIZE; g1++) {
        int g1Off = g1 * SIZE;
        int ng1Off = gcdTable[g1][x] * SIZE;
        for (int g2 = 0; g2 < SIZE; g2++) {
          int v = dp[g1Off + g2];
          if (v == 0) continue;

          int idx1 = ng1Off + g2;
          nextDp[idx1] = (nextDp[idx1] + v) % MOD;

          int idx2 = g1Off + gcdTable[g2][x];
          nextDp[idx2] = (nextDp[idx2] + v) % MOD;
        }
      }
      dp = nextDp;
    }

    int ans = 0;
    for (int g = 1; g < SIZE; g++) {
      ans = (ans + dp[g * SIZE + g]) % MOD;
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
func subsequencePairCount(nums []int) int {
	const MOD = 1000000007
	const SIZE = 201

	gcdTable := [SIZE][SIZE]int{}
	for i := 0; i < SIZE; i++ {
		for j := 0; j < SIZE; j++ {
			a, b := i, j
			for b != 0 {
				a %= b
				a, b = b, a
			}
			gcdTable[i][j] = a
		}
	}

	dp := make([]int, SIZE*SIZE)
	newDp := make([]int, SIZE*SIZE)
	dp[0] = 1

	for _, x := range nums {
		copy(newDp, dp)
		for g1 := 0; g1 < SIZE; g1++ {
			g1Off := g1 * SIZE
			ng1Off := gcdTable[g1][x] * SIZE
			for g2 := 0; g2 < SIZE; g2++ {
				v := dp[g1Off+g2]
				if v == 0 {
					continue
				}
				idx1 := ng1Off + g2
				newDp[idx1] = (newDp[idx1] + v) % MOD

				idx2 := g1Off + gcdTable[g2][x]
				newDp[idx2] = (newDp[idx2] + v) % MOD
			}
		}
		dp, newDp = newDp, dp
	}

	ans := 0
	for g := 1; g < SIZE; g++ {
		ans = (ans + dp[g*SIZE+g]) % MOD
	}

	return ans
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def subsequence_pair_count(nums)
  mod = 1_000_000_007
  size = 201
  gcd_table = Array.new(size) { Array.new(size) }
  (0...size).each do |i|
    (0...size).each do |j|
      gcd_table[i][j] = i.gcd(j)
    end
  end

  dp = Array.new(size * size, 0)
  dp[0] = 1

  nums.each do |x|
    new_dp = dp.dup
    (0...size).each do |g1|
      g1_off = g1 * size
      ng1_off = gcd_table[g1][x] * size
      (0...size).each do |g2|
        v = dp[g1_off + g2]
        next if v == 0

        idx1 = ng1_off + g2
        new_dp[idx1] = (new_dp[idx1] + v) % mod

        idx2 = g1_off + gcd_table[g2][x]
        new_dp[idx2] = (new_dp[idx2] + v) % mod
      end
    end
    dp = new_dp
  end

  ans = 0
  (1...size).each do |g|
    ans = (ans + dp[g * size + g]) % mod
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
    def subsequencePairCount(nums: Array[Int]): Int = {
        val MOD = 1000000007
        val SIZE = 201
        val gcdTable = Array.ofDim[Int](SIZE, SIZE)

        def gcd(a: Int, b: Int): Int = {
            var x = a
            var y = b
            while (y != 0) {
                x %= y
                val temp = x
                x = y
                y = temp
            }
            x
        }

        for (i <- 0 until SIZE) {
            for (j <- 0 until SIZE) {
                gcdTable(i)(j) = gcd(i, j)
            }
        }

        var dp = new Array[Int](SIZE * SIZE)
        dp(0) = 1

        for (x <- nums) {
            val nextDp = dp.clone()
            var g1 = 0
            while (g1 < SIZE) {
                val g1Off = g1 * SIZE
                val ng1Off = gcdTable(g1)(x) * SIZE
                var g2 = 0
                while (g2 < SIZE) {
                    val v = dp(g1Off + g2)
                    if (v > 0) {
                        val idx1 = ng1Off + g2
                        nextDp(idx1) = (nextDp(idx1) + v) % MOD

                        val idx2 = g1Off + gcdTable(g2)(x)
                        nextDp(idx2) = (nextDp(idx2) + v) % MOD
                    }
                    g2 += 1
                }
                g1 += 1
            }
            dp = nextDp
        }

        var ans = 0L
        for (g <- 1 until SIZE) {
            ans = (ans + dp(g * SIZE + g)) % MOD
        }

        ans.toInt
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn subsequence_pair_count(nums: Vec<i32>) -> i32 {
        let m = 201;
        let mut dp = vec![0i32; m * m];
        let mod_val = 1_000_000_007;

        fn gcd(mut a: usize, mut b: usize) -> usize {
            while b != 0 {
                a %= b;
                std::mem::swap(&mut a, &mut b);
            }
            a
        }

        dp[0] = 1;

        for &x_i32 in &nums {
            let x = x_i32 as usize;
            let mut next_dp = dp.clone();
            for g1 in 0..m {
                let offset = g1 * m;
                for g2 in 0..m {
                    let count = dp[offset + g2];
                    if count == 0 { continue; }

                    let ng1 = if g1 == 0 { x } else { gcd(g1, x) };
                    let idx1 = ng1 * m + g2;
                    next_dp[idx1] = (next_dp[idx1] + count) % mod_val;

                    let ng2 = if g2 == 0 { x } else { gcd(g2, x) };
                    let idx2 = offset + ng2;
                    next_dp[idx2] = (next_dp[idx2] + count) % mod_val;
                }
            }
            dp = next_dp;
        }

        let mut ans = 0;
        for g in 1..m {
            ans = (ans + dp[g * m + g]) % mod_val;
        }
        ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define (gcd-func a b)
  (if (zero? b) a (gcd-func b (remainder a b))))

(define/contract (subsequence-pair-count nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([mod-val 1000000007]
         [m 201]
         [dp (make-vector (* m m) 0)])
    (vector-set! dp 0 1)
    (for ([x nums])
      (let ([next-dp (vector-copy dp)])
        (for ([g1 (in-range m)])
          (let ([offset (* g1 m)])
            (for ([g2 (in-range m)])
              (let ([count (vector-ref dp (+ offset g2))])
                (when (> count 0)
                  (let* ([ng1 (gcd-func g1 x)]
                         [ng2 (gcd-func g2 x)]
                         [idx1 (+ (* ng1 m) g2)]
                         [idx2 (+ offset ng2)])
                    (vector-set! next-dp idx1 (modulo (+ (vector-ref next-dp idx1) count) mod-val))
                    (vector-set! next-dp idx2 (modulo (+ (vector-ref next-dp idx2) count) mod-val))))))))
        (set! dp next-dp)))
    (let ([ans 0])
      (for ([g (in-range 1 m)])
        (set! ans (modulo (+ ans (vector-ref dp (+ (* g m) g))) mod-val)))
      ans)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec subsequence_pair_count(Nums :: [integer()]) -> integer().
subsequence_pair_count(Nums) ->
    ModVal = 1000000007,
    InitialDP = #{{0, 0} => 1},
    FinalDP = lists:foldl(fun(X, AccDP) ->
        maps:fold(fun({G1, G2}, Count, NextDP) ->
            NG1 = gcd(G1, X),
            NG2 = gcd(G2, X),
            NextDP1 = maps:put({NG1, G2}, (maps:get({NG1, G2}, NextDP, 0) + Count) rem ModVal, NextDP),
            maps:put({G1, NG2}, (maps:get({G1, NG2}, NextDP1, 0) + Count) rem ModVal, NextDP1)
        end, AccDP, AccDP)
    end, InitialDP, Nums),
    lists:foldl(fun(G, Acc) ->
        (Acc + maps:get({G, G}, FinalDP, 0)) rem ModVal
    end, 0, lists:seq(1, 200)).

gcd(A, 0) -> A;
gcd(A, B) -> gcd(B, A rem B).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec subsequence_pair_count(nums :: [integer]) :: integer
  def subsequence_pair_count(nums) do
    mod_val = 1_000_000_007
    initial_dp = %{{0, 0} => 1}

    final_dp = Enum.reduce(nums, initial_dp, fn x, acc_dp ->
      Enum.reduce(acc_dp, acc_dp, fn {{g1, g2}, count}, next_dp ->
        ng1 = if g1 == 0, do: x, else: Integer.gcd(g1, x)
        ng2 = if g2 == 0, do: x, else: Integer.gcd(g2, x)

        next_dp = Map.put(next_dp, {ng1, g2}, rem(Map.get(next_dp, {ng1, g2}, 0) + count, mod_val))
        Map.put(next_dp, {g1, ng2}, rem(Map.get(next_dp, {g1, ng2}, 0) + count, mod_val))
      end)
    end)

    Enum.reduce(1..200, 0, fn g, acc ->
      rem(acc + Map.get(final_dp, {g, g}, 0), mod_val)
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N * M^2) where N is the length of the input array (up to 200) and M is the maximum value in the array (up to 200). For each of the N elements, we iterate over a DP table of size $(M+1) \times (M+1)$, leading to approximately $200 \times 201^2 \approx 8 \times 10^6$ operations, which is efficient for the given constraints.
- **Space Complexity:** O(M^2) as we maintain a 2D DP table of size $(M+1) \times (M+1)$ to store the number of ways to achieve every possible pair of GCDs. This consumes roughly $201 \times 201 \times 4$ bytes, which is well within the typical memory limits.
