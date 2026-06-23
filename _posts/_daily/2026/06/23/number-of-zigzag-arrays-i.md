---
layout: post
title: "Number of ZigZag Arrays I"
date: 2026-06-23 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Dynamic Programming", "Prefix Sum"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/number-of-zigzag-arrays-i/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int zigZagArrays(int n, int l, int r) {\n\
        \        int MOD = 1000000007;\n        int m = r - l + 1;\n        if (m <\
        \ 1) return 0;\n\n        vector<int> dp_up(m);\n        vector<int> dp_down(m);\n\
        \n        for (int j = 0; j < m; ++j) {\n            dp_up[j] = j;\n       \
        \     dp_down[j] = m - 1 - j;\n        }\n\n        for (int i = 3; i <= n;\
        \ ++i) {\n            vector<int> next_up(m, 0);\n            vector<int> next_down(m,\
        \ 0);\n            long long s_up = 0;\n            long long s_down = 0;\n\n\
        \            for (int j = 0; j < m; ++j) {\n                next_up[j] = (int)(s_down\
        \ % MOD);\n                s_down = (s_down + dp_down[j]) % MOD;\n         \
        \   }\n\n            for (int j = m - 1; j >= 0; --j) {\n                next_down[j]\
        \ = (int)(s_up % MOD);\n                s_up = (s_up + dp_up[j]) % MOD;\n  \
        \          }\n\n            dp_up = move(next_up);\n            dp_down = move(next_down);\n\
        \        }\n\n        long long total = 0;\n        for (int j = 0; j < m; ++j)\
        \ {\n            total = (total + dp_up[j]) % MOD;\n            total = (total\
        \ + dp_down[j]) % MOD;\n        }\n\n        return (int)total;\n    }\n};"
      java: "class Solution {\n    public int zigZagArrays(int n, int l, int r) {\n\
        \        int MOD = 1000000007;\n        int m = r - l + 1;\n        if (m <\
        \ 1) return 0;\n\n        int[] dp_up = new int[m];\n        int[] dp_down =\
        \ new int[m];\n\n        for (int j = 0; j < m; j++) {\n            dp_up[j]\
        \ = j;\n            dp_down[j] = m - 1 - j;\n        }\n\n        for (int i\
        \ = 3; i <= n; i++) {\n            int[] next_up = new int[m];\n           \
        \ int[] next_down = new int[m];\n            long s_up = 0;\n            long\
        \ s_down = 0;\n\n            for (int j = 0; j < m; j++) {\n               \
        \ next_up[j] = (int) s_down;\n                s_down = (s_down + dp_down[j])\
        \ % MOD;\n            }\n\n            for (int j = m - 1; j >= 0; j--) {\n\
        \                next_down[j] = (int) s_up;\n                s_up = (s_up +\
        \ dp_up[j]) % MOD;\n            }\n\n            dp_up = next_up;\n        \
        \    dp_down = next_down;\n        }\n\n        long total = 0;\n        for\
        \ (int j = 0; j < m; j++) {\n            total = (total + dp_up[j]) % MOD;\n\
        \            total = (total + dp_down[j]) % MOD;\n        }\n\n        return\
        \ (int) total;\n    }\n}"
      python: "class Solution(object):\n    def zigZagArrays(self, n, l, r):\n     \
        \   \"\"\"\n        :type n: int\n        :type l: int\n        :type r: int\n\
        \        :rtype: int\n        \"\"\"\n        MOD = 10**9 + 7\n        m = r\
        \ - l + 1\n        if m < 1:\n            return 0\n\n        # dp_up[v] counts\
        \ sequences ending in v where last step was an increase\n        # dp_down[v]\
        \ counts sequences ending in v where last step was a decrease\n        # Initialize\
        \ for length 2\n        dp_up = [j for j in range(m)]\n        dp_down = [m\
        \ - 1 - j for j in range(m)]\n\n        for _ in range(3, n + 1):\n        \
        \    next_up = [0] * m\n            next_down = [0] * m\n            s_up =\
        \ 0\n            s_down = 0\n\n            # For a new 'up' move at index i,\
        \ previous move at i-1 must have been 'down'\n            for j in range(m):\n\
        \                next_up[j] = s_down\n                s_down = (s_down + dp_down[j])\
        \ % MOD\n\n            # For a new 'down' move at index i, previous move at\
        \ i-1 must have been 'up'\n            for j in range(m - 1, -1, -1):\n    \
        \            next_down[j] = s_up\n                s_up = (s_up + dp_up[j]) %\
        \ MOD\n\n            dp_up = next_up\n            dp_down = next_down\n\n  \
        \      return (sum(dp_up) + sum(dp_down)) % MOD"
      python3: "import itertools\n\nclass Solution:\n    def zigZagArrays(self, n: int,\
        \ l: int, r: int) -> int:\n        MOD = 1000000007\n        m = r - l + 1\n\
        \        if m < 2:\n            return 0\n\n        # dp_up[x] is the number\
        \ of sequences of current length ending at x with an \"up\" move.\n        #\
        \ dp_down[x] is the number of sequences of current length ending at x with a\
        \ \"down\" move.\n        # Initialize for length 2\n        dp_up = [x for\
        \ x in range(m)]\n        dp_down = [m - 1 - x for x in range(m)]\n\n      \
        \  for i in range(3, n + 1):\n            next_up = [0] * m\n            next_down\
        \ = [0] * m\n\n            # For next_up[x], we need sum(dp_down[y] for y <\
        \ x)\n            curr_sum_down = 0\n            for x in range(m):\n      \
        \          next_up[x] = curr_sum_down\n                curr_sum_down = (curr_sum_down\
        \ + dp_down[x]) % MOD\n\n            # For next_down[x], we need sum(dp_up[y]\
        \ for y > x)\n            curr_sum_up = 0\n            for x in range(m - 1,\
        \ -1, -1):\n                next_down[x] = curr_sum_up\n                curr_sum_up\
        \ = (curr_sum_up + dp_up[x]) % MOD\n\n            dp_up, dp_down = next_up,\
        \ next_down\n\n        return (sum(dp_up) + sum(dp_down)) % MOD"
      c: "#include <stdlib.h>\n\nint zigZagArrays(int n, int l, int r) {\n    int m\
        \ = r - l + 1;\n    long long MOD = 1000000007;\n    if (m < 2) return 0;\n\n\
        \    long long* dp_up = (long long*)malloc(m * sizeof(long long));\n    long\
        \ long* dp_down = (long long*)malloc(m * sizeof(long long));\n    long long*\
        \ next_up = (long long*)malloc(m * sizeof(long long));\n    long long* next_down\
        \ = (long long*)malloc(m * sizeof(long long));\n\n    for (int x = 0; x < m;\
        \ x++) {\n        dp_up[x] = (long long)x;\n        dp_down[x] = (long long)(m\
        \ - 1 - x);\n    }\n\n    for (int i = 3; i <= n; i++) {\n        long long\
        \ curr_sum_down = 0;\n        for (int x = 0; x < m; x++) {\n            next_up[x]\
        \ = curr_sum_down;\n            curr_sum_down = (curr_sum_down + dp_down[x])\
        \ % MOD;\n        }\n\n        long long curr_sum_up = 0;\n        for (int\
        \ x = m - 1; x >= 0; x--) {\n            next_down[x] = curr_sum_up;\n     \
        \       curr_sum_up = (curr_sum_up + dp_up[x]) % MOD;\n        }\n\n       \
        \ long long* temp_up = dp_up;\n        dp_up = next_up;\n        next_up = temp_up;\n\
        \n        long long* temp_down = dp_down;\n        dp_down = next_down;\n  \
        \      next_down = temp_down;\n    }\n\n    long long total = 0;\n    for (int\
        \ x = 0; x < m; x++) {\n        total = (total + dp_up[x] + dp_down[x]) % MOD;\n\
        \    }\n\n    free(dp_up);\n    free(dp_down);\n    free(next_up);\n    free(next_down);\n\
        \n    return (int)total;\n}"
      csharp: "public class Solution {\n    public int ZigZagArrays(int n, int l, int\
        \ r) {\n        long MOD = 1000000007;\n        int m = r - l + 1;\n       \
        \ if (m < 2) return 0;\n\n        long[] dp_up = new long[m];\n        long[]\
        \ dp_down = new long[m];\n        long[] next_up = new long[m];\n        long[]\
        \ next_down = new long[m];\n\n        for (int x = 0; x < m; x++) {\n      \
        \      dp_up[x] = x;\n            dp_down[x] = m - 1 - x;\n        }\n\n   \
        \     for (int i = 3; i <= n; i++) {\n            long curr_sum_down = 0;\n\
        \            for (int x = 0; x < m; x++) {\n                next_up[x] = curr_sum_down;\n\
        \                curr_sum_down = (curr_sum_down + dp_down[x]) % MOD;\n     \
        \       }\n\n            long curr_sum_up = 0;\n            for (int x = m -\
        \ 1; x >= 0; x--) {\n                next_down[x] = curr_sum_up;\n         \
        \       curr_sum_up = (curr_sum_up + dp_up[x]) % MOD;\n            }\n\n   \
        \         long[] temp_up = dp_up;\n            dp_up = next_up;\n          \
        \  next_up = temp_up;\n\n            long[] temp_down = dp_down;\n         \
        \   dp_down = next_down;\n            next_down = temp_down;\n        }\n\n\
        \        long total = 0;\n        for (int x = 0; x < m; x++) {\n          \
        \  total = (total + dp_up[x] + dp_down[x]) % MOD;\n        }\n\n        return\
        \ (int)total;\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @param {number} l\n * @param {number}\
        \ r\n * @return {number}\n */\nvar zigZagArrays = function(n, l, r) {\n    const\
        \ MOD = 1000000007;\n    const m = r - l + 1;\n    if (m < 2) return 0;\n\n\
        \    let dp_up = new Float64Array(m);\n    let dp_down = new Float64Array(m);\n\
        \    let next_up = new Float64Array(m);\n    let next_down = new Float64Array(m);\n\
        \n    for (let x = 0; x < m; x++) {\n        dp_up[x] = x;\n        dp_down[x]\
        \ = m - 1 - x;\n    }\n\n    for (let i = 3; i <= n; i++) {\n        let curr_sum_down\
        \ = 0;\n        for (let x = 0; x < m; x++) {\n            next_up[x] = curr_sum_down;\n\
        \            curr_sum_down = (curr_sum_down + dp_down[x]) % MOD;\n        }\n\
        \n        let curr_sum_up = 0;\n        for (let x = m - 1; x >= 0; x--) {\n\
        \            next_down[x] = curr_sum_up;\n            curr_sum_up = (curr_sum_up\
        \ + dp_up[x]) % MOD;\n        }\n\n        let temp_up = dp_up;\n        dp_up\
        \ = next_up;\n        next_up = temp_up;\n\n        let temp_down = dp_down;\n\
        \        dp_down = next_down;\n        next_down = temp_down;\n    }\n\n   \
        \ let total = 0;\n    for (let x = 0; x < m; x++) {\n        total = (total\
        \ + dp_up[x] + dp_down[x]) % MOD;\n    }\n\n    return total;\n};"
      typescript: "function zigZagArrays(n: number, l: number, r: number): number {\n\
        \    const m = r - l + 1;\n    const MOD = 1000000007;\n    let dp0 = new Float64Array(m\
        \ + 1);\n    let dp1 = new Float64Array(m + 1);\n\n    for (let y = 1; y <=\
        \ m; y++) {\n        dp1[y] = y - 1;\n        dp0[y] = m - y;\n    }\n\n   \
        \ for (let i = 3; i <= n; i++) {\n        const prefixDp0 = new Float64Array(m\
        \ + 2);\n        for (let y = 1; y <= m; y++) {\n            prefixDp0[y] =\
        \ (prefixDp0[y - 1] + dp0[y]) % MOD;\n        }\n        const suffixDp1 = new\
        \ Float64Array(m + 2);\n        for (let y = m; y >= 1; y--) {\n           \
        \ suffixDp1[y] = (suffixDp1[y + 1] + dp1[y]) % MOD;\n        }\n        for\
        \ (let y = 1; y <= m; y++) {\n            dp1[y] = prefixDp0[y - 1];\n     \
        \       dp0[y] = suffixDp1[y + 1];\n        }\n    }\n\n    let total = 0;\n\
        \    for (let y = 1; y <= m; y++) {\n        total = (total + dp0[y] + dp1[y])\
        \ % MOD;\n    }\n\n    return total;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @param Integer\
        \ $l\n     * @param Integer $r\n     * @return Integer\n     */\n    function\
        \ zigZagArrays($n, $l, $r) {\n        $m = $r - $l + 1;\n        $MOD = 1000000007;\n\
        \        $dp0 = array_fill(0, $m + 1, 0);\n        $dp1 = array_fill(0, $m +\
        \ 1, 0);\n\n        for ($y = 1; $y <= $m; $y++) {\n            $dp1[$y] = $y\
        \ - 1;\n            $dp0[$y] = $m - $y;\n        }\n\n        for ($i = 3; $i\
        \ <= $n; $i++) {\n            $prefixDp0 = array_fill(0, $m + 2, 0);\n     \
        \       for ($y = 1; $y <= $m; $y++) {\n                $prefixDp0[$y] = ($prefixDp0[$y\
        \ - 1] + $dp0[$y]) % $MOD;\n            }\n            $suffixDp1 = array_fill(0,\
        \ $m + 2, 0);\n            for ($y = $m; $y >= 1; $y--) {\n                $suffixDp1[$y]\
        \ = ($suffixDp1[$y + 1] + $dp1[$y]) % $MOD;\n            }\n            for\
        \ ($y = 1; $y <= $m; $y++) {\n                $dp1[$y] = $prefixDp0[$y - 1];\n\
        \                $dp0[$y] = $suffixDp1[$y + 1];\n            }\n        }\n\n\
        \        $total = 0;\n        for ($y = 1; $y <= $m; $y++) {\n            $total\
        \ = ($total + $dp0[$y] + $dp1[$y]) % $MOD;\n        }\n\n        return $total;\n\
        \    }\n}"
      swift: "class Solution {\n    func zigZagArrays(_ n: Int, _ l: Int, _ r: Int)\
        \ -> Int {\n        let m = r - l + 1\n        let MOD = 1000000007\n      \
        \  var dp0 = [Int](repeating: 0, count: m + 1)\n        var dp1 = [Int](repeating:\
        \ 0, count: m + 1)\n\n        for y in 1...m {\n            dp1[y] = y - 1\n\
        \            dp0[y] = m - y\n        }\n\n        if n > 2 {\n            for\
        \ _ in 3...n {\n                var prefixDp0 = [Int](repeating: 0, count: m\
        \ + 2)\n                for y in 1...m {\n                    prefixDp0[y] =\
        \ (prefixDp0[y - 1] + dp0[y]) % MOD\n                }\n                var\
        \ suffixDp1 = [Int](repeating: 0, count: m + 2)\n                for y in stride(from:\
        \ m, through: 1, by: -1) {\n                    suffixDp1[y] = (suffixDp1[y\
        \ + 1] + dp1[y]) % MOD\n                }\n                for y in 1...m {\n\
        \                    dp1[y] = prefixDp0[y - 1]\n                    dp0[y] =\
        \ suffixDp1[y + 1]\n                }\n            }\n        }\n\n        var\
        \ total = 0\n        for y in 1...m {\n            total = (total + dp0[y] +\
        \ dp1[y]) % MOD\n        }\n\n        return total\n    }\n}"
      kotlin: "class Solution {\n    fun zigZagArrays(n: Int, l: Int, r: Int): Int {\n\
        \        val m = r - l + 1\n        val MOD = 1000000007L\n        var dp0 =\
        \ LongArray(m + 1)\n        var dp1 = LongArray(m + 1)\n\n        for (y in\
        \ 1..m) {\n            dp1[y] = (y - 1).toLong()\n            dp0[y] = (m -\
        \ y).toLong()\n        }\n\n        if (n > 2) {\n            for (i in 3..n)\
        \ {\n                val prefixDp0 = LongArray(m + 2)\n                for (y\
        \ in 1..m) {\n                    prefixDp0[y] = (prefixDp0[y - 1] + dp0[y])\
        \ % MOD\n                }\n                val suffixDp1 = LongArray(m + 2)\n\
        \                for (y in m downTo 1) {\n                    suffixDp1[y] =\
        \ (suffixDp1[y + 1] + dp1[y]) % MOD\n                }\n                for\
        \ (y in 1..m) {\n                    dp1[y] = prefixDp0[y - 1]\n           \
        \         dp0[y] = suffixDp1[y + 1]\n                }\n            }\n    \
        \    }\n\n        var total = 0L\n        for (y in 1..m) {\n            total\
        \ = (total + dp0[y] + dp1[y]) % MOD\n        }\n\n        return total.toInt()\n\
        \    }\n}"
      dart: "class Solution {\n  int zigZagArrays(int n, int l, int r) {\n    int mod\
        \ = 1000000007;\n    int m = r - l + 1;\n    if (m < 1) return 0;\n    List<int>\
        \ dpU = List<int>.filled(m + 1, 0);\n    List<int> dpD = List<int>.filled(m\
        \ + 1, 0);\n    for (int j = 1; j <= m; j++) {\n      dpU[j] = m - j;\n    \
        \  dpD[j] = j - 1;\n    }\n    for (int i = 3; i <= n; i++) {\n      List<int>\
        \ prefixU = List<int>.filled(m + 1, 0);\n      int sumU = 0;\n      for (int\
        \ j = 1; j <= m; j++) {\n        sumU = (sumU + dpU[j]) % mod;\n        prefixU[j]\
        \ = sumU;\n      }\n      List<int> suffixD = List<int>.filled(m + 2, 0);\n\
        \      int sumD = 0;\n      for (int j = m; j >= 1; j--) {\n        sumD = (sumD\
        \ + dpD[j]) % mod;\n        suffixD[j] = sumD;\n      }\n      List<int> nextU\
        \ = List<int>.filled(m + 1, 0);\n      List<int> nextD = List<int>.filled(m\
        \ + 1, 0);\n      for (int j = 1; j <= m; j++) {\n        nextU[j] = suffixD[j\
        \ + 1];\n        nextD[j] = prefixU[j - 1];\n      }\n      dpU = nextU;\n \
        \     dpD = nextD;\n    }\n    int ans = 0;\n    for (int j = 1; j <= m; j++)\
        \ {\n      ans = (ans + dpU[j]) % mod;\n      ans = (ans + dpD[j]) % mod;\n\
        \    }\n    return ans;\n  }\n}"
      go: "func zigZagArrays(n int, l int, r int) int {\n\tconst MOD = 1000000007\n\t\
        m := r - l + 1\n\tdpU := make([]int, m+1)\n\tdpD := make([]int, m+1)\n\tfor\
        \ j := 1; j <= m; j++ {\n\t\tdpU[j] = m - j\n\t\tdpD[j] = j - 1\n\t}\n\tfor\
        \ i := 3; i <= n; i++ {\n\t\tprefixU := make([]int, m+1)\n\t\tsumU := 0\n\t\t\
        for j := 1; j <= m; j++ {\n\t\t\tsumU = (sumU + dpU[j]) % MOD\n\t\t\tprefixU[j]\
        \ = sumU\n\t\t}\n\t\tsuffixD := make([]int, m+2)\n\t\tsumD := 0\n\t\tfor j :=\
        \ m; j >= 1; j-- {\n\t\t\tsumD = (sumD + dpD[j]) % MOD\n\t\t\tsuffixD[j] = sumD\n\
        \t\t}\n\t\tnextU := make([]int, m+1)\n\t\tnextD := make([]int, m+1)\n\t\tfor\
        \ j := 1; j <= m; j++ {\n\t\t\tnextU[j] = suffixD[j+1]\n\t\t\tnextD[j] = prefixU[j-1]\n\
        \t\t}\n\t\tdpU = nextU\n\t\tdpD = nextD\n\t}\n\tans := 0\n\tfor j := 1; j <=\
        \ m; j++ {\n\t\tans = (ans + dpU[j]) % MOD\n\t\tans = (ans + dpD[j]) % MOD\n\
        \t}\n\treturn ans\n}"
      ruby: "def zig_zag_arrays(n, l, r)\n  mod = 1_000_000_007\n  m = r - l + 1\n \
        \ return 0 if m <= 0\n  dp_u = Array.new(m + 1, 0)\n  dp_d = Array.new(m + 1,\
        \ 0)\n  (1..m).each do |j|\n    dp_u[j] = m - j\n    dp_d[j] = j - 1\n  end\n\
        \  (3..n).each do |i|\n    prefix_u = Array.new(m + 1, 0)\n    sum_u = 0\n \
        \   (1..m).each do |j|\n      sum_u = (sum_u + dp_u[j]) % mod\n      prefix_u[j]\
        \ = sum_u\n    end\n    suffix_d = Array.new(m + 2, 0)\n    sum_d = 0\n    m.downto(1).each\
        \ do |j|\n      sum_d = (sum_d + dp_d[j]) % mod\n      suffix_d[j] = sum_d\n\
        \    end\n    new_dp_u = Array.new(m + 1, 0)\n    new_dp_d = Array.new(m + 1,\
        \ 0)\n    (1..m).each do |j|\n      new_dp_u[j] = suffix_d[j + 1]\n      new_dp_d[j]\
        \ = prefix_u[j - 1]\n    end\n    dp_u = new_dp_u\n    dp_d = new_dp_d\n  end\n\
        \  ans = 0\n  (1..m).each do |j|\n    ans = (ans + dp_u[j]) % mod\n    ans =\
        \ (ans + dp_d[j]) % mod\n  end\n  ans\nend"
      scala: "object Solution {\n    def zigZagArrays(n: Int, l: Int, r: Int): Int =\
        \ {\n        val MOD = 1000000007L\n        val m = r - l + 1\n        if (m\
        \ < 1) return 0\n        var dpU = new Array[Long](m + 1)\n        var dpD =\
        \ new Array[Long](m + 1)\n        for (j <- 1 to m) {\n            dpU(j) =\
        \ (m - j).toLong\n            dpD(j) = (j - 1).toLong\n        }\n        for\
        \ (i <- 3 to n) {\n            val prefixU = new Array[Long](m + 1)\n      \
        \      var sumU = 0L\n            for (j <- 1 to m) {\n                sumU\
        \ = (sumU + dpU(j)) % MOD\n                prefixU(j) = sumU\n            }\n\
        \            val suffixD = new Array[Long](m + 2)\n            var sumD = 0L\n\
        \            for (j <- m by -1 to 1) {\n                sumD = (sumD + dpD(j))\
        \ % MOD\n                suffixD(j) = sumD\n            }\n            val nextU\
        \ = new Array[Long](m + 1)\n            val nextD = new Array[Long](m + 1)\n\
        \            for (j <- 1 to m) {\n                nextU(j) = suffixD(j + 1)\n\
        \                nextD(j) = prefixU(j - 1)\n            }\n            dpU =\
        \ nextU\n            dpD = nextD\n        }\n        var ans = 0L\n        for\
        \ (j <- 1 to m) {\n            ans = (ans + dpU(j) + dpD(j)) % MOD\n       \
        \ }\n        ans.toInt\n    }\n}"
      rust: "impl Solution {\n    pub fn zig_zag_arrays(n: i32, l: i32, r: i32) -> i32\
        \ {\n        let n = n as usize;\n        let m = (r - l + 1) as usize;\n  \
        \      let mod_val = 1_000_000_007i64;\n\n        let mut up = vec![0i64; m];\n\
        \        let mut down = vec![0i64; m];\n\n        for i in 0..m {\n        \
        \    up[i] = i as i64;\n            down[i] = (m - 1 - i) as i64;\n        }\n\
        \n        for _ in 3..=n {\n            let mut p_down = vec![0i64; m];\n  \
        \          let mut acc = 0;\n            for j in 0..m {\n                acc\
        \ = (acc + down[j]) % mod_val;\n                p_down[j] = acc;\n         \
        \   }\n\n            let mut s_up = vec![0i64; m];\n            acc = 0;\n \
        \           for j in (0..m).rev() {\n                acc = (acc + up[j]) % mod_val;\n\
        \                s_up[j] = acc;\n            }\n\n            let mut next_up\
        \ = vec![0i64; m];\n            let mut next_down = vec![0i64; m];\n       \
        \     for j in 0..m {\n                if j > 0 {\n                    next_up[j]\
        \ = p_down[j - 1];\n                }\n                if j < m - 1 {\n    \
        \                next_down[j] = s_up[j + 1];\n                }\n          \
        \  }\n            up = next_up;\n            down = next_down;\n        }\n\n\
        \        let mut total = 0i64;\n        for i in 0..m {\n            total =\
        \ (total + up[i]) % mod_val;\n            total = (total + down[i]) % mod_val;\n\
        \        }\n        total as i32\n    }\n}"
      racket: "(define/contract (zig-zag-arrays n l r)\n  (-> exact-integer? exact-integer?\
        \ exact-integer? exact-integer?)\n  (let* ([m (+ (- r l) 1)]\n         [MOD\
        \ 1000000007]\n         [up (make-vector m)]\n         [down (make-vector m)])\n\
        \    (for ([i (in-range m)])\n      (vector-set! up i i)\n      (vector-set!\
        \ down i (- m 1 i)))\n    (for ([_ (in-range (- n 2))])\n      (let ([p-down\
        \ (make-vector m)]\n            [s-up (make-vector m)]\n            [new-up\
        \ (make-vector m)]\n            [new-down (make-vector m)])\n        (for/fold\
        \ ([acc 0]) ([i (in-range m)])\n          (let ([new-acc (modulo (+ acc (vector-ref\
        \ down i)) MOD)])\n            (vector-set! p-down i new-acc)\n            new-acc))\n\
        \        (for/fold ([acc 0]) ([i (in-range (- m 1) -1 -1)])\n          (let\
        \ ([new-acc (modulo (+ acc (vector-ref up i)) MOD)])\n            (vector-set!\
        \ s-up i new-acc)\n            new-acc))\n        (for ([i (in-range m)])\n\
        \          (vector-set! new-up i (if (> i 0) (vector-ref p-down (- i 1)) 0))\n\
        \          (vector-set! new-down i (if (< i (- m 1)) (vector-ref s-up (+ i 1))\
        \ 0)))\n        (for ([i (in-range m)])\n          (vector-set! up i (vector-ref\
        \ new-up i))\n          (vector-set! down i (vector-ref new-down i)))))\n  \
        \  (for/fold ([total 0]) ([i (in-range m)])\n      (modulo (+ total (vector-ref\
        \ up i) (vector-ref down i)) MOD))))"
      erlang: "-spec zig_zag_arrays(N :: integer(), L :: integer(), R :: integer())\
        \ -> integer().\nzig_zag_arrays(N, L, R) ->\n  M = R - L + 1,\n  MOD = 1000000007,\n\
        \  Up = lists:seq(0, M - 1),\n  Down = lists:reverse(Up),\n  Loop = fun(I, CurrentUp,\
        \ CurrentDown, NextF) when I > N -> {CurrentUp, CurrentDown};\n            \
        \ (I, CurrentUp, CurrentDown, NextF) ->\n                 {P_Down, _} = lists:mapfoldl(fun(X,\
        \ Acc) ->\n                     NewAcc = (X + Acc) rem MOD,\n              \
        \       {NewAcc, NewAcc}\n                 end, 0, CurrentDown),\n         \
        \        {S_Up_Rev, _} = lists:mapfoldl(fun(X, Acc) ->\n                   \
        \  NewAcc = (X + Acc) rem MOD,\n                     {NewAcc, NewAcc}\n    \
        \             end, 0, lists:reverse(CurrentUp)),\n                 S_Up = lists:reverse(S_Up_Rev),\n\
        \                 NewUp = [0 | lists:sublist(P_Down, M - 1)],\n            \
        \     NewDown = lists:nthtail(1, S_Up) ++ [0],\n                 NextF(I + 1,\
        \ NewUp, NewDown, NextF)\n  end,\n  {FinalUp, FinalDown} = Loop(3, Up, Down,\
        \ Loop),\n  (lists:sum(FinalUp) + lists:sum(FinalDown)) rem MOD."
      elixir: "defmodule Solution do\n  @spec zig_zag_arrays(n :: integer, l :: integer,\
        \ r :: integer) :: integer\n  def zig_zag_arrays(n, l, r) do\n    m = r - l\
        \ + 1\n    mod = 1_000_000_007\n\n    up = Enum.to_list(0..(m - 1))\n    down\
        \ = Enum.to_list((m - 1)..0)\n\n    {final_up, final_down} = \n      if n <\
        \ 3 do\n        {up, down}\n      else\n        Enum.reduce(3..n, {up, down},\
        \ fn _, {u, d} ->\n          {p_down, _} = Enum.map_reduce(d, 0, fn x, acc ->\n\
        \            new_acc = rem(acc + x, mod)\n            {new_acc, new_acc}\n \
        \         end)\n\n          {s_up_rev, _} = Enum.map_reduce(Enum.reverse(u),\
        \ 0, fn x, acc ->\n            new_acc = rem(acc + x, mod)\n            {new_acc,\
        \ new_acc}\n          end)\n          s_up = Enum.reverse(s_up_rev)\n\n    \
        \      new_u = [0 | Enum.take(p_down, m - 1)]\n          new_d = Enum.drop(s_up,\
        \ 1) ++ [0]\n          {new_u, new_d}\n        end)\n      end\n\n    (Enum.sum(final_up)\
        \ + Enum.sum(final_down)) |> rem(mod)\n  end\nend"
    approach: 'The problem asks to count valid ZigZag arrays of length $n$ where elements
      are in the range $[l, r]$, no two adjacent elements are equal, and no three consecutive
      elements are monotonic. These conditions imply that the direction of inequality
      between adjacent elements must strictly alternate (e.g., $a_1 < a_2 > a_3 < a_4
      > \dots$ or $a_1 > a_2 < a_3 > a_4 < \dots$). We can use dynamic programming where
      $dp\_up[v]$ represents the number of valid sequences of the current length ending
      in value $v$ such that the previous move was an ''up'' move ($prev < v$), and
      $dp\_down[v]$ represents the count where the previous move was a ''down'' move
      ($prev > v$).


      To compute the counts for length $i+1$, we observe that an ''up'' move must follow
      a ''down'' move, and a ''down'' move must follow an ''up'' move. Thus, $dp\_up[v]$
      at length $i+1$ is the sum of all $dp\_down[prev]$ from length $i$ where $prev
      < v$. Similarly, $dp\_down[v]$ at length $i+1$ is the sum of $dp\_up[prev]$ from
      length $i$ where $prev > v$. We optimize these prefix and suffix sums to $O(m)$
      per length increment, where $m = r - l + 1$. The base case is length $i=2$, where
      $dp\_up[v]$ is the number of possible values $prev$ such that $prev < v$, and
      $dp\_down[v]$ is the number of possible values $prev$ such that $prev > v$.'
    time_complexity: 'O(n * (r - l)) with one-paragraph explanation: The algorithm iterates
      from length 3 up to $n$, performing two linear scans of size $m = r - l + 1$ at
      each step to compute prefix and suffix sums. Since each step takes $O(m)$ time
      and there are $O(n)$ steps, the total time complexity is $O(n \cdot m)$. With
      $n, m \le 2000$, the total number of operations is approximately $4 \times 10^6$,
      which is well within the time limit.'
    space_complexity: 'O(r - l) with one-paragraph explanation: The space complexity
      is linear with respect to the number of possible values $m = r - l + 1$. We only
      need to store the current and next DP arrays (each of size $m$), leading to a
      space requirement of $O(m)$.'
    elapsed_time: 335.2569897174835
    model: gemini-3-flash-preview
    generated_at: '2026-06-23 02:39:59 '
---

## Problem #3699: Number of ZigZag Arrays I

**Difficulty:** Hard

**Topics:** Dynamic Programming, Prefix Sum

## Problem Description

<p>You are given three integers <code>n</code>, <code>l</code>, and <code>r</code>.</p>

<p>A <strong>ZigZag</strong> array of length <code>n</code> is defined as follows:</p>

<ul>
	<li>Each element lies in the range <code>[l, r]</code>.</li>
	<li>No <strong>two</strong> adjacent elements are equal.</li>
	<li>No <strong>three</strong> consecutive elements form a <strong>strictly increasing</strong> or <strong>strictly decreasing</strong> sequence.</li>
</ul>

<p>Return the total number of valid <strong>ZigZag</strong> arrays.</p>

<p>Since the answer may be large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>A <strong>sequence</strong> is said to be <strong>strictly increasing</strong> if each element is strictly greater than its previous one (if exists).</p>

<p>A <strong>sequence</strong> is said to be <strong>strictly decreasing</strong> if each element is strictly smaller than its previous one (if exists).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, l = 4, r = 5</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>There are only 2 valid ZigZag arrays of length <code>n = 3</code> using values in the range <code>[4, 5]</code>:</p>

<ul>
	<li><code>[4, 5, 4]</code></li>
	<li><code>[5, 4, 5]</code>​​​​​​​</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, l = 1, r = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">10</span></p>

<p><strong>Explanation:</strong></p>

<p>There are 10 valid ZigZag arrays of length <code>n = 3</code> using values in the range <code>[1, 3]</code>:</p>

<ul>
	<li><code>[1, 2, 1]</code>, <code>[1, 3, 1]</code>, <code>[1, 3, 2]</code></li>
	<li><code>[2, 1, 2]</code>, <code>[2, 1, 3]</code>, <code>[2, 3, 1]</code>, <code>[2, 3, 2]</code></li>
	<li><code>[3, 1, 2]</code>, <code>[3, 1, 3]</code>, <code>[3, 2, 3]</code></li>
</ul>

<p>All arrays meet the ZigZag conditions.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= n &lt;= 2000</code></li>
	<li><code>1 &lt;= l &lt; r &lt;= 2000</code></li>
</ul>


## Hints

1. Use dynamic programming: let `dp[i][dir][x]` be the count of length-`i` sequences ending at value `x` where `dir` is the required next comparison (0 = down, 1 = up).

2. If the required move is `up` (dir=1) do `dp[i+1][0][y] += sum(dp[i][1][x]) for x  y`.

3. Speed up with prefix/suffix sums so each layer updates in O(`m`) instead of O(`m`^2); take values mod `10^9+7`.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks to count valid ZigZag arrays of length $n$ where elements are in the range $[l, r]$, no two adjacent elements are equal, and no three consecutive elements are monotonic. These conditions imply that the direction of inequality between adjacent elements must strictly alternate (e.g., $a_1 < a_2 > a_3 < a_4 > \dots$ or $a_1 > a_2 < a_3 > a_4 < \dots$). We can use dynamic programming where $dp\_up[v]$ represents the number of valid sequences of the current length ending in value $v$ such that the previous move was an 'up' move ($prev < v$), and $dp\_down[v]$ represents the count where the previous move was a 'down' move ($prev > v$).

To compute the counts for length $i+1$, we observe that an 'up' move must follow a 'down' move, and a 'down' move must follow an 'up' move. Thus, $dp\_up[v]$ at length $i+1$ is the sum of all $dp\_down[prev]$ from length $i$ where $prev < v$. Similarly, $dp\_down[v]$ at length $i+1$ is the sum of $dp\_up[prev]$ from length $i$ where $prev > v$. We optimize these prefix and suffix sums to $O(m)$ per length increment, where $m = r - l + 1$. The base case is length $i=2$, where $dp\_up[v]$ is the number of possible values $prev$ such that $prev < v$, and $dp\_down[v]$ is the number of possible values $prev$ such that $prev > v$.

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
    int zigZagArrays(int n, int l, int r) {
        int MOD = 1000000007;
        int m = r - l + 1;
        if (m < 1) return 0;

        vector<int> dp_up(m);
        vector<int> dp_down(m);

        for (int j = 0; j < m; ++j) {
            dp_up[j] = j;
            dp_down[j] = m - 1 - j;
        }

        for (int i = 3; i <= n; ++i) {
            vector<int> next_up(m, 0);
            vector<int> next_down(m, 0);
            long long s_up = 0;
            long long s_down = 0;

            for (int j = 0; j < m; ++j) {
                next_up[j] = (int)(s_down % MOD);
                s_down = (s_down + dp_down[j]) % MOD;
            }

            for (int j = m - 1; j >= 0; --j) {
                next_down[j] = (int)(s_up % MOD);
                s_up = (s_up + dp_up[j]) % MOD;
            }

            dp_up = move(next_up);
            dp_down = move(next_down);
        }

        long long total = 0;
        for (int j = 0; j < m; ++j) {
            total = (total + dp_up[j]) % MOD;
            total = (total + dp_down[j]) % MOD;
        }

        return (int)total;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int zigZagArrays(int n, int l, int r) {
        int MOD = 1000000007;
        int m = r - l + 1;
        if (m < 1) return 0;

        int[] dp_up = new int[m];
        int[] dp_down = new int[m];

        for (int j = 0; j < m; j++) {
            dp_up[j] = j;
            dp_down[j] = m - 1 - j;
        }

        for (int i = 3; i <= n; i++) {
            int[] next_up = new int[m];
            int[] next_down = new int[m];
            long s_up = 0;
            long s_down = 0;

            for (int j = 0; j < m; j++) {
                next_up[j] = (int) s_down;
                s_down = (s_down + dp_down[j]) % MOD;
            }

            for (int j = m - 1; j >= 0; j--) {
                next_down[j] = (int) s_up;
                s_up = (s_up + dp_up[j]) % MOD;
            }

            dp_up = next_up;
            dp_down = next_down;
        }

        long total = 0;
        for (int j = 0; j < m; j++) {
            total = (total + dp_up[j]) % MOD;
            total = (total + dp_down[j]) % MOD;
        }

        return (int) total;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int
        :rtype: int
        """
        MOD = 10**9 + 7
        m = r - l + 1
        if m < 1:
            return 0

        # dp_up[v] counts sequences ending in v where last step was an increase
        # dp_down[v] counts sequences ending in v where last step was a decrease
        # Initialize for length 2
        dp_up = [j for j in range(m)]
        dp_down = [m - 1 - j for j in range(m)]

        for _ in range(3, n + 1):
            next_up = [0] * m
            next_down = [0] * m
            s_up = 0
            s_down = 0

            # For a new 'up' move at index i, previous move at i-1 must have been 'down'
            for j in range(m):
                next_up[j] = s_down
                s_down = (s_down + dp_down[j]) % MOD

            # For a new 'down' move at index i, previous move at i-1 must have been 'up'
            for j in range(m - 1, -1, -1):
                next_down[j] = s_up
                s_up = (s_up + dp_up[j]) % MOD

            dp_up = next_up
            dp_down = next_down

        return (sum(dp_up) + sum(dp_down)) % MOD
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import itertools

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 1000000007
        m = r - l + 1
        if m < 2:
            return 0

        # dp_up[x] is the number of sequences of current length ending at x with an "up" move.
        # dp_down[x] is the number of sequences of current length ending at x with a "down" move.
        # Initialize for length 2
        dp_up = [x for x in range(m)]
        dp_down = [m - 1 - x for x in range(m)]

        for i in range(3, n + 1):
            next_up = [0] * m
            next_down = [0] * m

            # For next_up[x], we need sum(dp_down[y] for y < x)
            curr_sum_down = 0
            for x in range(m):
                next_up[x] = curr_sum_down
                curr_sum_down = (curr_sum_down + dp_down[x]) % MOD

            # For next_down[x], we need sum(dp_up[y] for y > x)
            curr_sum_up = 0
            for x in range(m - 1, -1, -1):
                next_down[x] = curr_sum_up
                curr_sum_up = (curr_sum_up + dp_up[x]) % MOD

            dp_up, dp_down = next_up, next_down

        return (sum(dp_up) + sum(dp_down)) % MOD
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

int zigZagArrays(int n, int l, int r) {
    int m = r - l + 1;
    long long MOD = 1000000007;
    if (m < 2) return 0;

    long long* dp_up = (long long*)malloc(m * sizeof(long long));
    long long* dp_down = (long long*)malloc(m * sizeof(long long));
    long long* next_up = (long long*)malloc(m * sizeof(long long));
    long long* next_down = (long long*)malloc(m * sizeof(long long));

    for (int x = 0; x < m; x++) {
        dp_up[x] = (long long)x;
        dp_down[x] = (long long)(m - 1 - x);
    }

    for (int i = 3; i <= n; i++) {
        long long curr_sum_down = 0;
        for (int x = 0; x < m; x++) {
            next_up[x] = curr_sum_down;
            curr_sum_down = (curr_sum_down + dp_down[x]) % MOD;
        }

        long long curr_sum_up = 0;
        for (int x = m - 1; x >= 0; x--) {
            next_down[x] = curr_sum_up;
            curr_sum_up = (curr_sum_up + dp_up[x]) % MOD;
        }

        long long* temp_up = dp_up;
        dp_up = next_up;
        next_up = temp_up;

        long long* temp_down = dp_down;
        dp_down = next_down;
        next_down = temp_down;
    }

    long long total = 0;
    for (int x = 0; x < m; x++) {
        total = (total + dp_up[x] + dp_down[x]) % MOD;
    }

    free(dp_up);
    free(dp_down);
    free(next_up);
    free(next_down);

    return (int)total;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int ZigZagArrays(int n, int l, int r) {
        long MOD = 1000000007;
        int m = r - l + 1;
        if (m < 2) return 0;

        long[] dp_up = new long[m];
        long[] dp_down = new long[m];
        long[] next_up = new long[m];
        long[] next_down = new long[m];

        for (int x = 0; x < m; x++) {
            dp_up[x] = x;
            dp_down[x] = m - 1 - x;
        }

        for (int i = 3; i <= n; i++) {
            long curr_sum_down = 0;
            for (int x = 0; x < m; x++) {
                next_up[x] = curr_sum_down;
                curr_sum_down = (curr_sum_down + dp_down[x]) % MOD;
            }

            long curr_sum_up = 0;
            for (int x = m - 1; x >= 0; x--) {
                next_down[x] = curr_sum_up;
                curr_sum_up = (curr_sum_up + dp_up[x]) % MOD;
            }

            long[] temp_up = dp_up;
            dp_up = next_up;
            next_up = temp_up;

            long[] temp_down = dp_down;
            dp_down = next_down;
            next_down = temp_down;
        }

        long total = 0;
        for (int x = 0; x < m; x++) {
            total = (total + dp_up[x] + dp_down[x]) % MOD;
        }

        return (int)total;
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
 * @param {number} l
 * @param {number} r
 * @return {number}
 */
var zigZagArrays = function(n, l, r) {
    const MOD = 1000000007;
    const m = r - l + 1;
    if (m < 2) return 0;

    let dp_up = new Float64Array(m);
    let dp_down = new Float64Array(m);
    let next_up = new Float64Array(m);
    let next_down = new Float64Array(m);

    for (let x = 0; x < m; x++) {
        dp_up[x] = x;
        dp_down[x] = m - 1 - x;
    }

    for (let i = 3; i <= n; i++) {
        let curr_sum_down = 0;
        for (let x = 0; x < m; x++) {
            next_up[x] = curr_sum_down;
            curr_sum_down = (curr_sum_down + dp_down[x]) % MOD;
        }

        let curr_sum_up = 0;
        for (let x = m - 1; x >= 0; x--) {
            next_down[x] = curr_sum_up;
            curr_sum_up = (curr_sum_up + dp_up[x]) % MOD;
        }

        let temp_up = dp_up;
        dp_up = next_up;
        next_up = temp_up;

        let temp_down = dp_down;
        dp_down = next_down;
        next_down = temp_down;
    }

    let total = 0;
    for (let x = 0; x < m; x++) {
        total = (total + dp_up[x] + dp_down[x]) % MOD;
    }

    return total;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function zigZagArrays(n: number, l: number, r: number): number {
    const m = r - l + 1;
    const MOD = 1000000007;
    let dp0 = new Float64Array(m + 1);
    let dp1 = new Float64Array(m + 1);

    for (let y = 1; y <= m; y++) {
        dp1[y] = y - 1;
        dp0[y] = m - y;
    }

    for (let i = 3; i <= n; i++) {
        const prefixDp0 = new Float64Array(m + 2);
        for (let y = 1; y <= m; y++) {
            prefixDp0[y] = (prefixDp0[y - 1] + dp0[y]) % MOD;
        }
        const suffixDp1 = new Float64Array(m + 2);
        for (let y = m; y >= 1; y--) {
            suffixDp1[y] = (suffixDp1[y + 1] + dp1[y]) % MOD;
        }
        for (let y = 1; y <= m; y++) {
            dp1[y] = prefixDp0[y - 1];
            dp0[y] = suffixDp1[y + 1];
        }
    }

    let total = 0;
    for (let y = 1; y <= m; y++) {
        total = (total + dp0[y] + dp1[y]) % MOD;
    }

    return total;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $n
     * @param Integer $l
     * @param Integer $r
     * @return Integer
     */
    function zigZagArrays($n, $l, $r) {
        $m = $r - $l + 1;
        $MOD = 1000000007;
        $dp0 = array_fill(0, $m + 1, 0);
        $dp1 = array_fill(0, $m + 1, 0);

        for ($y = 1; $y <= $m; $y++) {
            $dp1[$y] = $y - 1;
            $dp0[$y] = $m - $y;
        }

        for ($i = 3; $i <= $n; $i++) {
            $prefixDp0 = array_fill(0, $m + 2, 0);
            for ($y = 1; $y <= $m; $y++) {
                $prefixDp0[$y] = ($prefixDp0[$y - 1] + $dp0[$y]) % $MOD;
            }
            $suffixDp1 = array_fill(0, $m + 2, 0);
            for ($y = $m; $y >= 1; $y--) {
                $suffixDp1[$y] = ($suffixDp1[$y + 1] + $dp1[$y]) % $MOD;
            }
            for ($y = 1; $y <= $m; $y++) {
                $dp1[$y] = $prefixDp0[$y - 1];
                $dp0[$y] = $suffixDp1[$y + 1];
            }
        }

        $total = 0;
        for ($y = 1; $y <= $m; $y++) {
            $total = ($total + $dp0[$y] + $dp1[$y]) % $MOD;
        }

        return $total;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func zigZagArrays(_ n: Int, _ l: Int, _ r: Int) -> Int {
        let m = r - l + 1
        let MOD = 1000000007
        var dp0 = [Int](repeating: 0, count: m + 1)
        var dp1 = [Int](repeating: 0, count: m + 1)

        for y in 1...m {
            dp1[y] = y - 1
            dp0[y] = m - y
        }

        if n > 2 {
            for _ in 3...n {
                var prefixDp0 = [Int](repeating: 0, count: m + 2)
                for y in 1...m {
                    prefixDp0[y] = (prefixDp0[y - 1] + dp0[y]) % MOD
                }
                var suffixDp1 = [Int](repeating: 0, count: m + 2)
                for y in stride(from: m, through: 1, by: -1) {
                    suffixDp1[y] = (suffixDp1[y + 1] + dp1[y]) % MOD
                }
                for y in 1...m {
                    dp1[y] = prefixDp0[y - 1]
                    dp0[y] = suffixDp1[y + 1]
                }
            }
        }

        var total = 0
        for y in 1...m {
            total = (total + dp0[y] + dp1[y]) % MOD
        }

        return total
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun zigZagArrays(n: Int, l: Int, r: Int): Int {
        val m = r - l + 1
        val MOD = 1000000007L
        var dp0 = LongArray(m + 1)
        var dp1 = LongArray(m + 1)

        for (y in 1..m) {
            dp1[y] = (y - 1).toLong()
            dp0[y] = (m - y).toLong()
        }

        if (n > 2) {
            for (i in 3..n) {
                val prefixDp0 = LongArray(m + 2)
                for (y in 1..m) {
                    prefixDp0[y] = (prefixDp0[y - 1] + dp0[y]) % MOD
                }
                val suffixDp1 = LongArray(m + 2)
                for (y in m downTo 1) {
                    suffixDp1[y] = (suffixDp1[y + 1] + dp1[y]) % MOD
                }
                for (y in 1..m) {
                    dp1[y] = prefixDp0[y - 1]
                    dp0[y] = suffixDp1[y + 1]
                }
            }
        }

        var total = 0L
        for (y in 1..m) {
            total = (total + dp0[y] + dp1[y]) % MOD
        }

        return total.toInt()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int zigZagArrays(int n, int l, int r) {
    int mod = 1000000007;
    int m = r - l + 1;
    if (m < 1) return 0;
    List<int> dpU = List<int>.filled(m + 1, 0);
    List<int> dpD = List<int>.filled(m + 1, 0);
    for (int j = 1; j <= m; j++) {
      dpU[j] = m - j;
      dpD[j] = j - 1;
    }
    for (int i = 3; i <= n; i++) {
      List<int> prefixU = List<int>.filled(m + 1, 0);
      int sumU = 0;
      for (int j = 1; j <= m; j++) {
        sumU = (sumU + dpU[j]) % mod;
        prefixU[j] = sumU;
      }
      List<int> suffixD = List<int>.filled(m + 2, 0);
      int sumD = 0;
      for (int j = m; j >= 1; j--) {
        sumD = (sumD + dpD[j]) % mod;
        suffixD[j] = sumD;
      }
      List<int> nextU = List<int>.filled(m + 1, 0);
      List<int> nextD = List<int>.filled(m + 1, 0);
      for (int j = 1; j <= m; j++) {
        nextU[j] = suffixD[j + 1];
        nextD[j] = prefixU[j - 1];
      }
      dpU = nextU;
      dpD = nextD;
    }
    int ans = 0;
    for (int j = 1; j <= m; j++) {
      ans = (ans + dpU[j]) % mod;
      ans = (ans + dpD[j]) % mod;
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
func zigZagArrays(n int, l int, r int) int {
	const MOD = 1000000007
	m := r - l + 1
	dpU := make([]int, m+1)
	dpD := make([]int, m+1)
	for j := 1; j <= m; j++ {
		dpU[j] = m - j
		dpD[j] = j - 1
	}
	for i := 3; i <= n; i++ {
		prefixU := make([]int, m+1)
		sumU := 0
		for j := 1; j <= m; j++ {
			sumU = (sumU + dpU[j]) % MOD
			prefixU[j] = sumU
		}
		suffixD := make([]int, m+2)
		sumD := 0
		for j := m; j >= 1; j-- {
			sumD = (sumD + dpD[j]) % MOD
			suffixD[j] = sumD
		}
		nextU := make([]int, m+1)
		nextD := make([]int, m+1)
		for j := 1; j <= m; j++ {
			nextU[j] = suffixD[j+1]
			nextD[j] = prefixU[j-1]
		}
		dpU = nextU
		dpD = nextD
	}
	ans := 0
	for j := 1; j <= m; j++ {
		ans = (ans + dpU[j]) % MOD
		ans = (ans + dpD[j]) % MOD
	}
	return ans
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def zig_zag_arrays(n, l, r)
  mod = 1_000_000_007
  m = r - l + 1
  return 0 if m <= 0
  dp_u = Array.new(m + 1, 0)
  dp_d = Array.new(m + 1, 0)
  (1..m).each do |j|
    dp_u[j] = m - j
    dp_d[j] = j - 1
  end
  (3..n).each do |i|
    prefix_u = Array.new(m + 1, 0)
    sum_u = 0
    (1..m).each do |j|
      sum_u = (sum_u + dp_u[j]) % mod
      prefix_u[j] = sum_u
    end
    suffix_d = Array.new(m + 2, 0)
    sum_d = 0
    m.downto(1).each do |j|
      sum_d = (sum_d + dp_d[j]) % mod
      suffix_d[j] = sum_d
    end
    new_dp_u = Array.new(m + 1, 0)
    new_dp_d = Array.new(m + 1, 0)
    (1..m).each do |j|
      new_dp_u[j] = suffix_d[j + 1]
      new_dp_d[j] = prefix_u[j - 1]
    end
    dp_u = new_dp_u
    dp_d = new_dp_d
  end
  ans = 0
  (1..m).each do |j|
    ans = (ans + dp_u[j]) % mod
    ans = (ans + dp_d[j]) % mod
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
    def zigZagArrays(n: Int, l: Int, r: Int): Int = {
        val MOD = 1000000007L
        val m = r - l + 1
        if (m < 1) return 0
        var dpU = new Array[Long](m + 1)
        var dpD = new Array[Long](m + 1)
        for (j <- 1 to m) {
            dpU(j) = (m - j).toLong
            dpD(j) = (j - 1).toLong
        }
        for (i <- 3 to n) {
            val prefixU = new Array[Long](m + 1)
            var sumU = 0L
            for (j <- 1 to m) {
                sumU = (sumU + dpU(j)) % MOD
                prefixU(j) = sumU
            }
            val suffixD = new Array[Long](m + 2)
            var sumD = 0L
            for (j <- m by -1 to 1) {
                sumD = (sumD + dpD(j)) % MOD
                suffixD(j) = sumD
            }
            val nextU = new Array[Long](m + 1)
            val nextD = new Array[Long](m + 1)
            for (j <- 1 to m) {
                nextU(j) = suffixD(j + 1)
                nextD(j) = prefixU(j - 1)
            }
            dpU = nextU
            dpD = nextD
        }
        var ans = 0L
        for (j <- 1 to m) {
            ans = (ans + dpU(j) + dpD(j)) % MOD
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
    pub fn zig_zag_arrays(n: i32, l: i32, r: i32) -> i32 {
        let n = n as usize;
        let m = (r - l + 1) as usize;
        let mod_val = 1_000_000_007i64;

        let mut up = vec![0i64; m];
        let mut down = vec![0i64; m];

        for i in 0..m {
            up[i] = i as i64;
            down[i] = (m - 1 - i) as i64;
        }

        for _ in 3..=n {
            let mut p_down = vec![0i64; m];
            let mut acc = 0;
            for j in 0..m {
                acc = (acc + down[j]) % mod_val;
                p_down[j] = acc;
            }

            let mut s_up = vec![0i64; m];
            acc = 0;
            for j in (0..m).rev() {
                acc = (acc + up[j]) % mod_val;
                s_up[j] = acc;
            }

            let mut next_up = vec![0i64; m];
            let mut next_down = vec![0i64; m];
            for j in 0..m {
                if j > 0 {
                    next_up[j] = p_down[j - 1];
                }
                if j < m - 1 {
                    next_down[j] = s_up[j + 1];
                }
            }
            up = next_up;
            down = next_down;
        }

        let mut total = 0i64;
        for i in 0..m {
            total = (total + up[i]) % mod_val;
            total = (total + down[i]) % mod_val;
        }
        total as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (zig-zag-arrays n l r)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  (let* ([m (+ (- r l) 1)]
         [MOD 1000000007]
         [up (make-vector m)]
         [down (make-vector m)])
    (for ([i (in-range m)])
      (vector-set! up i i)
      (vector-set! down i (- m 1 i)))
    (for ([_ (in-range (- n 2))])
      (let ([p-down (make-vector m)]
            [s-up (make-vector m)]
            [new-up (make-vector m)]
            [new-down (make-vector m)])
        (for/fold ([acc 0]) ([i (in-range m)])
          (let ([new-acc (modulo (+ acc (vector-ref down i)) MOD)])
            (vector-set! p-down i new-acc)
            new-acc))
        (for/fold ([acc 0]) ([i (in-range (- m 1) -1 -1)])
          (let ([new-acc (modulo (+ acc (vector-ref up i)) MOD)])
            (vector-set! s-up i new-acc)
            new-acc))
        (for ([i (in-range m)])
          (vector-set! new-up i (if (> i 0) (vector-ref p-down (- i 1)) 0))
          (vector-set! new-down i (if (< i (- m 1)) (vector-ref s-up (+ i 1)) 0)))
        (for ([i (in-range m)])
          (vector-set! up i (vector-ref new-up i))
          (vector-set! down i (vector-ref new-down i)))))
    (for/fold ([total 0]) ([i (in-range m)])
      (modulo (+ total (vector-ref up i) (vector-ref down i)) MOD))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec zig_zag_arrays(N :: integer(), L :: integer(), R :: integer()) -> integer().
zig_zag_arrays(N, L, R) ->
  M = R - L + 1,
  MOD = 1000000007,
  Up = lists:seq(0, M - 1),
  Down = lists:reverse(Up),
  Loop = fun(I, CurrentUp, CurrentDown, NextF) when I > N -> {CurrentUp, CurrentDown};
             (I, CurrentUp, CurrentDown, NextF) ->
                 {P_Down, _} = lists:mapfoldl(fun(X, Acc) ->
                     NewAcc = (X + Acc) rem MOD,
                     {NewAcc, NewAcc}
                 end, 0, CurrentDown),
                 {S_Up_Rev, _} = lists:mapfoldl(fun(X, Acc) ->
                     NewAcc = (X + Acc) rem MOD,
                     {NewAcc, NewAcc}
                 end, 0, lists:reverse(CurrentUp)),
                 S_Up = lists:reverse(S_Up_Rev),
                 NewUp = [0 | lists:sublist(P_Down, M - 1)],
                 NewDown = lists:nthtail(1, S_Up) ++ [0],
                 NextF(I + 1, NewUp, NewDown, NextF)
  end,
  {FinalUp, FinalDown} = Loop(3, Up, Down, Loop),
  (lists:sum(FinalUp) + lists:sum(FinalDown)) rem MOD.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec zig_zag_arrays(n :: integer, l :: integer, r :: integer) :: integer
  def zig_zag_arrays(n, l, r) do
    m = r - l + 1
    mod = 1_000_000_007

    up = Enum.to_list(0..(m - 1))
    down = Enum.to_list((m - 1)..0)

    {final_up, final_down} = 
      if n < 3 do
        {up, down}
      else
        Enum.reduce(3..n, {up, down}, fn _, {u, d} ->
          {p_down, _} = Enum.map_reduce(d, 0, fn x, acc ->
            new_acc = rem(acc + x, mod)
            {new_acc, new_acc}
          end)

          {s_up_rev, _} = Enum.map_reduce(Enum.reverse(u), 0, fn x, acc ->
            new_acc = rem(acc + x, mod)
            {new_acc, new_acc}
          end)
          s_up = Enum.reverse(s_up_rev)

          new_u = [0 | Enum.take(p_down, m - 1)]
          new_d = Enum.drop(s_up, 1) ++ [0]
          {new_u, new_d}
        end)
      end

    (Enum.sum(final_up) + Enum.sum(final_down)) |> rem(mod)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n * (r - l)) with one-paragraph explanation: The algorithm iterates from length 3 up to $n$, performing two linear scans of size $m = r - l + 1$ at each step to compute prefix and suffix sums. Since each step takes $O(m)$ time and there are $O(n)$ steps, the total time complexity is $O(n \cdot m)$. With $n, m \le 2000$, the total number of operations is approximately $4 \times 10^6$, which is well within the time limit.
- **Space Complexity:** O(r - l) with one-paragraph explanation: The space complexity is linear with respect to the number of possible values $m = r - l + 1$. We only need to store the current and next DP arrays (each of size $m$), leading to a space requirement of $O(m)$.
