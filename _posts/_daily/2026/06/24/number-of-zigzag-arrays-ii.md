---
layout: post
title: "Number of ZigZag Arrays II"
date: 2026-06-24 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Math", "Dynamic Programming"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/number-of-zigzag-arrays-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int zigZagArrays(int n, int l, int r) {\n\
        \        if (n == 1) return r - l + 1;\n        long long m = r - l + 1;\n \
        \       long long mod = 1e9 + 7;\n        if (n == 2) return (m * (m - 1)) %\
        \ mod;\n\n        auto multiply = [&](const vector<vector<long long>>& A, const\
        \ vector<vector<long long>>& B) {\n            vector<vector<long long>> C(m,\
        \ vector<long long>(m, 0));\n            for (int i = 0; i < m; ++i) {\n   \
        \             for (int k = 0; k < m; ++k) {\n                    if (A[i][k]\
        \ == 0) continue;\n                    for (int j = 0; j < m; ++j) {\n     \
        \                   C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod;\n       \
        \             }\n                }\n            }\n            return C;\n \
        \       };\n\n        vector<vector<long long>> mat(m, vector<long long>(m));\n\
        \        for (int i = 0; i < m; ++i) {\n            for (int j = 0; j < m; ++j)\
        \ {\n                mat[i][j] = min(i, j);\n            }\n        }\n\n  \
        \      long long p = n - 2;\n        long long k = p / 2;\n        vector<vector<long\
        \ long>> res(m, vector<long long>(m, 0));\n        for (int i = 0; i < m; ++i)\
        \ res[i][i] = 1;\n\n        while (k > 0) {\n            if (k & 1) res = multiply(res,\
        \ mat);\n            mat = multiply(mat, mat);\n            k >>= 1;\n     \
        \   }\n\n        vector<long long> v(m);\n        for (int i = 0; i < m; ++i)\
        \ {\n            long long sum = 0;\n            for (int j = 0; j < m; ++j)\
        \ {\n                sum = (sum + res[i][j] * j) % mod;\n            }\n   \
        \         v[i] = sum;\n        }\n\n        long long total = 0;\n        if\
        \ (p % 2 == 0) {\n            for (int i = 0; i < m; ++i) total = (total + v[i])\
        \ % mod;\n        } else {\n            for (int i = 0; i < m; ++i) total =\
        \ (total + v[i] * i) % mod;\n        }\n\n        return (total * 2) % mod;\n\
        \    }\n};"
      java: "class Solution {\n    public int zigZagArrays(int n, int l, int r) {\n\
        \        if (n == 1) return r - l + 1;\n        int m = r - l + 1;\n       \
        \ long mod = 1000000007;\n        if (n == 2) return (int) (((long) m * (m -\
        \ 1)) % mod);\n\n        long[][] mat = new long[m][m];\n        for (int i\
        \ = 0; i < m; i++) {\n            for (int j = 0; j < m; j++) {\n          \
        \      mat[i][j] = Math.min(i, j);\n            }\n        }\n\n        long\
        \ p = n - 2;\n        long k = p / 2;\n        long[][] res = new long[m][m];\n\
        \        for (int i = 0; i < m; i++) res[i][i] = 1;\n\n        while (k > 0)\
        \ {\n            if (k % 2 == 1) res = multiply(res, mat, m, mod);\n       \
        \     mat = multiply(mat, mat, m, mod);\n            k /= 2;\n        }\n\n\
        \        long total = 0;\n        if (p % 2 == 0) {\n            for (int i\
        \ = 0; i < m; i++) {\n                long vi = 0;\n                for (int\
        \ j = 0; j < m; j++) {\n                    vi = (vi + res[i][j] * j) % mod;\n\
        \                }\n                total = (total + vi) % mod;\n          \
        \  }\n        } else {\n            for (int i = 0; i < m; i++) {\n        \
        \        long vi = 0;\n                for (int j = 0; j < m; j++) {\n     \
        \               vi = (vi + res[i][j] * j) % mod;\n                }\n      \
        \          total = (total + vi * i) % mod;\n            }\n        }\n\n   \
        \     return (int) ((total * 2) % mod);\n    }\n\n    private long[][] multiply(long[][]\
        \ A, long[][] B, int m, long mod) {\n        long[][] C = new long[m][m];\n\
        \        for (int i = 0; i < m; i++) {\n            for (int k = 0; k < m; k++)\
        \ {\n                if (A[i][k] == 0) continue;\n                for (int j\
        \ = 0; j < m; j++) {\n                    C[i][j] = (C[i][j] + A[i][k] * B[k][j])\
        \ % mod;\n                }\n            }\n        }\n        return C;\n \
        \   }\n}"
      python: "class Solution(object):\n    def zigZagArrays(self, n, l, r):\n     \
        \   if n == 1: return r - l + 1\n        m = r - l + 1\n        mod = 10**9\
        \ + 7\n        if n == 2: return (m * (m - 1)) % mod\n\n        def multiply(A,\
        \ B, m, mod):\n            C = [[0] * m for _ in range(m)]\n            for\
        \ i in range(m):\n                Ai = A[i]\n                Ci = C[i]\n   \
        \             for k in range(m):\n                    if Ai[k] == 0: continue\n\
        \                    temp = Ai[k]\n                    Bk = B[k]\n         \
        \           for j in range(m):\n                        Ci[j] = (Ci[j] + temp\
        \ * Bk[j]) % mod\n            return C\n\n        mat = [[min(i, j) for j in\
        \ range(m)] for i in range(m)]\n        p = n - 2\n        k = p // 2\n    \
        \    res = [[0] * m for _ in range(m)]\n        for i in range(m): res[i][i]\
        \ = 1\n\n        while k > 0:\n            if k % 2 == 1:\n                res\
        \ = multiply(res, mat, m, mod)\n            mat = multiply(mat, mat, m, mod)\n\
        \            k //= 2\n\n        v = [0] * m\n        for i in range(m):\n  \
        \          row = res[i]\n            curr = 0\n            for j in range(m):\n\
        \                curr = (curr + row[j] * j) % mod\n            v[i] = curr\n\
        \n        total = 0\n        if p % 2 == 0:\n            total = sum(v) % mod\n\
        \        else:\n            for i in range(m):\n                total = (total\
        \ + v[i] * i) % mod\n\n        return (total * 2) % mod"
      python3: "class Solution:\n    def zigZagArrays(self, n: int, l: int, r: int)\
        \ -> int:\n        m = r - l + 1\n        size = 2 * m\n        mod = 10**9\
        \ + 7\n\n        def multiply(A, B):\n            C = [[0] * size for _ in range(size)]\n\
        \            for i in range(size):\n                Ai, Ci = A[i], C[i]\n  \
        \              for k in range(size):\n                    Aik = Ai[k]\n    \
        \                if Aik == 0:\n                        continue\n          \
        \          Bk = B[k]\n                    for j in range(size):\n          \
        \              if Bk[j]:\n                            Ci[j] = (Ci[j] + Aik *\
        \ Bk[j]) % mod\n            return C\n\n        def power(A, p):\n         \
        \   res = [[0] * size for _ in range(size)]\n            for i in range(size):\
        \ \n                res[i][i] = 1\n            while p > 0:\n              \
        \  if p % 2 == 1: \n                    res = multiply(res, A)\n           \
        \     A = multiply(A, A)\n                p //= 2\n            return res\n\n\
        \        T = [[0] * size for _ in range(size)]\n        for i in range(m):\n\
        \            for j in range(m):\n                if i > j: \n              \
        \      T[i][j + m] = 1\n                if i < j: \n                    T[i\
        \ + m][j] = 1\n\n        Tn = power(T, n - 1)\n        ans = 0\n        for\
        \ row in Tn:\n            ans = (ans + sum(row)) % mod\n        return ans"
      c: "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nlong long\
        \ mod = 1000000007;\n\nvoid multiply(int size, long long A[150][150], long long\
        \ B[150][150], long long res[150][150]) {\n    static long long temp[150][150];\n\
        \    for (int i = 0; i < size; i++) {\n        for (int j = 0; j < size; j++)\
        \ temp[i][j] = 0;\n        for (int k = 0; k < size; k++) {\n            if\
        \ (A[i][k] == 0) continue;\n            for (int j = 0; j < size; j++) {\n \
        \               if (B[k][j] == 0) continue;\n                temp[i][j] = (temp[i][j]\
        \ + A[i][k] * B[k][j]) % mod;\n            }\n        }\n    }\n    for (int\
        \ i = 0; i < size; i++) {\n        for (int j = 0; j < size; j++) res[i][j]\
        \ = temp[i][j];\n    }\n}\n\nint zigZagArrays(int n, int l, int r) {\n    int\
        \ m = r - l + 1;\n    int size = 2 * m;\n    long long T[150][150];\n    memset(T,\
        \ 0, sizeof(T));\n    for (int i = 0; i < m; i++) {\n        for (int j = 0;\
        \ j < m; j++) {\n            if (i > j) T[i][j + m] = 1;\n            if (i\
        \ < j) T[i + m][j] = 1;\n        }\n    }\n\n    long long res[150][150];\n\
        \    for (int i = 0; i < size; i++) {\n        for (int j = 0; j < size; j++)\
        \ res[i][j] = (i == j);\n    }\n\n    int p = n - 1;\n    while (p > 0) {\n\
        \        if (p % 2 == 1) multiply(size, res, T, res);\n        multiply(size,\
        \ T, T, T);\n        p /= 2;\n    }\n\n    long long ans = 0;\n    for (int\
        \ i = 0; i < size; i++) {\n        for (int j = 0; j < size; j++) {\n      \
        \      ans = (ans + res[i][j]) % mod;\n        }\n    }\n    return (int)ans;\n\
        }"
      csharp: "public class Solution {\n    public int ZigZagArrays(int n, int l, int\
        \ r) {\n        int m = r - l + 1;\n        int size = 2 * m;\n        long\
        \ mod = 1000000007;\n\n        long[,] T = new long[size, size];\n        for\
        \ (int i = 0; i < m; i++) {\n            for (int j = 0; j < m; j++) {\n   \
        \             if (i > j) T[i, j + m] = 1;\n                if (i < j) T[i +\
        \ m, j] = 1;\n            }\n        }\n\n        long[,] res = MatrixPower(T,\
        \ n - 1, size, mod);\n        long ans = 0;\n        for (int i = 0; i < size;\
        \ i++) {\n            for (int j = 0; j < size; j++) {\n                ans\
        \ = (ans + res[i, j]) % mod;\n            }\n        }\n\n        return (int)ans;\n\
        \    }\n\n    private long[,] MatrixMultiply(long[,] A, long[,] B, int size,\
        \ long mod) {\n        long[,] C = new long[size, size];\n        for (int i\
        \ = 0; i < size; i++) {\n            for (int k = 0; k < size; k++) {\n    \
        \            if (A[i, k] == 0) continue;\n                for (int j = 0; j\
        \ < size; j++) {\n                    if (B[k, j] == 0) continue;\n        \
        \            C[i, j] = (C[i, j] + A[i, k] * B[k, j]) % mod;\n              \
        \  }\n            }\n        }\n        return C;\n    }\n\n    private long[,]\
        \ MatrixPower(long[,] A, int p, int size, long mod) {\n        long[,] res =\
        \ new long[size, size];\n        for (int i = 0; i < size; i++) res[i, i] =\
        \ 1;\n        long[,] baseMat = A;\n        while (p > 0) {\n            if\
        \ (p % 2 == 1) res = MatrixMultiply(res, baseMat, size, mod);\n            baseMat\
        \ = MatrixMultiply(baseMat, baseMat, size, mod);\n            p /= 2;\n    \
        \    }\n        return res;\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @param {number} l\n * @param {number}\
        \ r\n * @return {number}\n */\nvar zigZagArrays = function(n, l, r) {\n    const\
        \ m = r - l + 1;\n    const size = 2 * m;\n    const mod = 1000000007n;\n\n\
        \    function multiply(A, B) {\n        const C = Array.from({ length: size\
        \ }, () => new BigInt64Array(size));\n        for (let i = 0; i < size; i++)\
        \ {\n            for (let k = 0; k < size; k++) {\n                if (A[i][k]\
        \ === 0n) continue;\n                for (let j = 0; j < size; j++) {\n    \
        \                if (B[k][j] === 0n) continue;\n                    C[i][j]\
        \ = (C[i][j] + A[i][k] * B[k][j]) % mod;\n                }\n            }\n\
        \        }\n        return C;\n    }\n\n    function power(A, p) {\n       \
        \ let res = Array.from({ length: size }, (_, i) => {\n            const row\
        \ = new BigInt64Array(size);\n            row[i] = 1n;\n            return row;\n\
        \        });\n        let base = A;\n        while (p > 0) {\n            if\
        \ (p % 2 === 1) res = multiply(res, base);\n            base = multiply(base,\
        \ base);\n            p = Math.floor(p / 2);\n        }\n        return res;\n\
        \    }\n\n    const T = Array.from({ length: size }, () => new BigInt64Array(size));\n\
        \    for (let i = 0; i < m; i++) {\n        for (let j = 0; j < m; j++) {\n\
        \            if (i > j) T[i][j + m] = 1n;\n            if (i < j) T[i + m][j]\
        \ = 1n;\n        }\n    }\n\n    const Tn = power(T, n - 1);\n    let ans =\
        \ 0n;\n    for (let i = 0; i < size; i++) {\n        for (let j = 0; j < size;\
        \ j++) {\n            ans = (ans + Tn[i][j]) % mod;\n        }\n    }\n\n  \
        \  return Number(ans);\n};"
      typescript: "class ZigMatrix {\n  m1: bigint[][];\n  m2: bigint[][];\n  isOff:\
        \ boolean;\n\n  constructor(m1: bigint[][], m2: bigint[][], isOff: boolean)\
        \ {\n    this.m1 = m1;\n    this.m2 = m2;\n    this.isOff = isOff;\n  }\n}\n\
        \nfunction multiply(A: bigint[][], B: bigint[][], m: number): bigint[][] {\n\
        \  const res: bigint[][] = Array.from({ length: m }, () => Array(m).fill(0n));\n\
        \  const MOD = 1000000007n;\n  for (let i = 0; i < m; i++) {\n    for (let k\
        \ = 0; k < m; k++) {\n      if (A[i][k] === 0n) continue;\n      const rowVal\
        \ = A[i][k];\n      for (let j = 0; j < m; j++) {\n        res[i][j] = (res[i][j]\
        \ + rowVal * B[k][j]) % MOD;\n      }\n    }\n  }\n  return res;\n}\n\nfunction\
        \ sumMV(M: bigint[][], V: bigint[], m: number): bigint {\n  let total = 0n;\n\
        \  const MOD = 1000000007n;\n  for (let i = 0; i < m; i++) {\n    for (let j\
        \ = 0; j < m; j++) {\n      total = (total + M[i][j] * V[j]) % MOD;\n    }\n\
        \  }\n  return total;\n}\n\nfunction zigZagArrays(n: number, l: number, r: number):\
        \ number {\n  const m = r - l + 1;\n  const MOD = 1000000007n;\n  if (n ===\
        \ 1) return m % Number(MOD);\n\n  const a: bigint[][] = Array.from({ length:\
        \ m }, (_, i) =>\n    Array.from({ length: m }, (_, j) => (i > j ? 1n : 0n))\n\
        \  );\n  const b: bigint[][] = Array.from({ length: m }, (_, i) =>\n    Array.from({\
        \ length: m }, (_, j) => (i < j ? 1n : 0n))\n  );\n\n  const identityM: bigint[][]\
        \ = Array.from({ length: m }, (_, i) =>\n    Array.from({ length: m }, (_, j)\
        \ => (i === j ? 1n : 0n))\n  );\n\n  let res = new ZigMatrix(identityM, identityM,\
        \ false);\n  let base = new ZigMatrix(a, b, true);\n\n  let p = BigInt(n) -\
        \ 2n;\n  while (p > 0n) {\n    if (p % 2n === 1n) {\n      const m1 = multiply(res.m1,\
        \ res.isOff ? base.m2 : base.m1, m);\n      const m2 = multiply(res.m2, res.isOff\
        \ ? base.m1 : base.m2, m);\n      res = new ZigMatrix(m1, m2, res.isOff !==\
        \ base.isOff);\n    }\n    const m1 = multiply(base.m1, base.isOff ? base.m2\
        \ : base.m1, m);\n    const m2 = multiply(base.m2, base.isOff ? base.m1 : base.m2,\
        \ m);\n    base = new ZigMatrix(m1, m2, false);\n    p = p / 2n;\n  }\n\n  const\
        \ vUp: bigint[] = Array.from({ length: m }, (_, i) => BigInt(i));\n  const vDown:\
        \ bigint[] = Array.from({ length: m }, (_, i) => BigInt(m - 1 - i));\n\n  let\
        \ ans: bigint;\n  if (res.isOff) {\n    ans = (sumMV(res.m1, vDown, m) + sumMV(res.m2,\
        \ vUp, m)) % MOD;\n  } else {\n    ans = (sumMV(res.m1, vUp, m) + sumMV(res.m2,\
        \ vDown, m)) % MOD;\n  }\n\n  return Number(ans);\n}"
      php: "class ZigMatrix {\n    public $m1;\n    public $m2;\n    public $isOff;\n\
        \    function __construct($m1, $m2, $isOff) {\n        $this->m1 = $m1;\n  \
        \      $this->m2 = $m2;\n        $this->isOff = $isOff;\n    }\n}\n\nclass Solution\
        \ {\n\n    /**\n     * @param Integer $n\n     * @param Integer $l\n     * @param\
        \ Integer $r\n     * @return Integer\n     */\n    function zigZagArrays($n,\
        \ $l, $r) {\n        $m = $r - $l + 1;\n        $MOD = 1000000007;\n       \
        \ if ($n == 1) return $m % $MOD;\n\n        $a = array_fill(0, $m, array_fill(0,\
        \ $m, 0));\n        $b = array_fill(0, $m, array_fill(0, $m, 0));\n        $identity\
        \ = array_fill(0, $m, array_fill(0, $m, 0));\n\n        for ($i = 0; $i < $m;\
        \ $i++) {\n            $identity[$i][$i] = 1;\n            for ($j = 0; $j <\
        \ $m; $j++) {\n                if ($i > $j) $a[$i][$j] = 1;\n              \
        \  if ($i < $j) $b[$i][$j] = 1;\n            }\n        }\n\n        $res =\
        \ new ZigMatrix($identity, $identity, false);\n        $base = new ZigMatrix($a,\
        \ $b, true);\n\n        $p = $n - 2;\n        while ($p > 0) {\n           \
        \ if ($p % 2 == 1) {\n                $res = $this->matMulStruct($res, $base,\
        \ $m, $MOD);\n            }\n            $base = $this->matMulStruct($base,\
        \ $base, $m, $MOD);\n            $p = (int)($p / 2);\n        }\n\n        $vUp\
        \ = [];\n        $vDown = [];\n        for ($i = 0; $i < $m; $i++) {\n     \
        \       $vUp[$i] = $i;\n            $vDown[$i] = $m - 1 - $i;\n        }\n\n\
        \        if ($res->isOff) {\n            $ans = ($this->sumMV($res->m1, $vDown,\
        \ $m, $MOD) + $this->sumMV($res->m2, $vUp, $m, $MOD)) % $MOD;\n        } else\
        \ {\n            $ans = ($this->sumMV($res->m1, $vUp, $m, $MOD) + $this->sumMV($res->m2,\
        \ $vDown, $m, $MOD)) % $MOD;\n        }\n\n        return $ans;\n    }\n\n \
        \   function matMulStruct($A, $B, $m, $MOD) {\n        $isOff = $A->isOff ^\
        \ $B->isOff;\n        $m1 = $this->multiply($A->m1, $A->isOff ? $B->m2 : $B->m1,\
        \ $m, $MOD);\n        $m2 = $this->multiply($A->m2, $A->isOff ? $B->m1 : $B->m2,\
        \ $m, $MOD);\n        return new ZigMatrix($m1, $m2, (bool)$isOff);\n    }\n\
        \n    function multiply($A, $B, $m, $MOD) {\n        $res = array_fill(0, $m,\
        \ array_fill(0, $m, 0));\n        for ($i = 0; $i < $m; $i++) {\n          \
        \  for ($k = 0; $k < $m; $k++) {\n                if ($A[$i][$k] == 0) continue;\n\
        \                $rowA = $A[$i][$k];\n                for ($j = 0; $j < $m;\
        \ $j++) {\n                    $res[$i][$j] = ($res[$i][$j] + $rowA * $B[$k][$j])\
        \ % $MOD;\n                }\n            }\n        }\n        return $res;\n\
        \    }\n\n    function sumMV($M, $V, $m, $MOD) {\n        $total = 0;\n    \
        \    for ($i = 0; $i < $m; $i++) {\n            for ($j = 0; $j < $m; $j++)\
        \ {\n                $total = ($total + $M[$i][$j] * $V[$j]) % $MOD;\n     \
        \       }\n        }\n        return $total;\n    }\n}"
      swift: "class Solution {\n    struct ZigMatrix {\n        let m1: [[Int64]]\n\
        \        let m2: [[Int64]]\n        let isOff: Bool\n    }\n\n    func multiply(_\
        \ A: [[Int64]], _ B: [[Int64]], _ m: Int) -> [[Int64]] {\n        let MOD: Int64\
        \ = 1000000007\n        var res = [[Int64]](repeating: [Int64](repeating: 0,\
        \ count: m), count: m)\n        for i in 0..<m {\n            for k in 0..<m\
        \ {\n                if A[i][k] == 0 { continue }\n                let rowVal\
        \ = A[i][k]\n                for j in 0..<m {\n                    res[i][j]\
        \ = (res[i][j] + rowVal * B[k][j]) % MOD\n                }\n            }\n\
        \        }\n        return res\n    }\n\n    func sumMV(_ M: [[Int64]], _ V:\
        \ [Int64], _ m: Int) -> Int64 {\n        let MOD: Int64 = 1000000007\n     \
        \   var total: Int64 = 0\n        for i in 0..<m {\n            for j in 0..<m\
        \ {\n                total = (total + M[i][j] * V[j]) % MOD\n            }\n\
        \        }\n        return total\n    }\n\n    func zigZagArrays(_ n: Int, _\
        \ l: Int, _ r: Int) -> Int {\n        let m = r - l + 1\n        let MOD: Int64\
        \ = 1000000007\n        if n == 1 { return m % Int(MOD) }\n\n        var a =\
        \ [[Int64]](repeating: [Int64](repeating: 0, count: m), count: m)\n        var\
        \ b = [[Int64]](repeating: [Int64](repeating: 0, count: m), count: m)\n    \
        \    var identity = [[Int64]](repeating: [Int64](repeating: 0, count: m), count:\
        \ m)\n\n        for i in 0..<m {\n            identity[i][i] = 1\n         \
        \   for j in 0..<m {\n                if i > j { a[i][j] = 1 }\n           \
        \     if i < j { b[i][j] = 1 }\n            }\n        }\n\n        var res\
        \ = ZigMatrix(m1: identity, m2: identity, isOff: false)\n        var base =\
        \ ZigMatrix(m1: a, m2: b, isOff: true)\n\n        var p = n - 2\n        while\
        \ p > 0 {\n            if p % 2 == 1 {\n                let m1 = multiply(res.m1,\
        \ res.isOff ? base.m2 : base.m1, m)\n                let m2 = multiply(res.m2,\
        \ res.isOff ? base.m1 : base.m2, m)\n                res = ZigMatrix(m1: m1,\
        \ m2: m2, isOff: res.isOff != base.isOff)\n            }\n            let m1\
        \ = multiply(base.m1, base.isOff ? base.m2 : base.m1, m)\n            let m2\
        \ = multiply(base.m2, base.isOff ? base.m1 : base.m2, m)\n            base =\
        \ ZigMatrix(m1: m1, m2: m2, isOff: false)\n            p /= 2\n        }\n\n\
        \        var vUp = [Int64](repeating: 0, count: m)\n        var vDown = [Int64](repeating:\
        \ 0, count: m)\n        for i in 0..<m {\n            vUp[i] = Int64(i)\n  \
        \          vDown[i] = Int64(m - 1 - i)\n        }\n\n        var ans: Int64\
        \ = 0\n        if res.isOff {\n            ans = (sumMV(res.m1, vDown, m) +\
        \ sumMV(res.m2, vUp, m)) % MOD\n        } else {\n            ans = (sumMV(res.m1,\
        \ vUp, m) + sumMV(res.m2, vDown, m)) % MOD\n        }\n\n        return Int(ans)\n\
        \    }\n}"
      kotlin: "class Solution {\n    class ZigMatrix(val m1: Array<LongArray>, val m2:\
        \ Array<LongArray>, val isOff: Boolean)\n\n    private fun multiply(A: Array<LongArray>,\
        \ B: Array<LongArray>, m: Int): Array<LongArray> {\n        val MOD = 1000000007L\n\
        \        val res = Array(m) { LongArray(m) }\n        for (i in 0 until m) {\n\
        \            for (k in 0 until m) {\n                if (A[i][k] == 0L) continue\n\
        \                val rowVal = A[i][k]\n                for (j in 0 until m)\
        \ {\n                    res[i][j] = (res[i][j] + rowVal * B[k][j]) % MOD\n\
        \                }\n            }\n        }\n        return res\n    }\n\n\
        \    private fun sumMV(M: Array<LongArray>, V: LongArray, m: Int): Long {\n\
        \        val MOD = 1000000007L\n        var total = 0L\n        for (i in 0\
        \ until m) {\n            for (j in 0 until m) {\n                total = (total\
        \ + M[i][j] * V[j]) % MOD\n            }\n        }\n        return total\n\
        \    }\n\n    fun zigZagArrays(n: Int, l: Int, r: Int): Int {\n        val m\
        \ = r - l + 1\n        val MOD = 1000000007L\n        if (n == 1) return (m\
        \ % MOD).toInt()\n\n        val a = Array(m) { i -> LongArray(m) { j -> if (i\
        \ > j) 1L else 0L } }\n        val b = Array(m) { i -> LongArray(m) { j -> if\
        \ (i < j) 1L else 0L } }\n        val identity = Array(m) { i -> LongArray(m)\
        \ { j -> if (i == j) 1L else 0L } }\n\n        var res = ZigMatrix(identity,\
        \ identity, false)\n        var base = ZigMatrix(a, b, true)\n\n        var\
        \ p = n.toLong() - 2L\n        while (p > 0) {\n            if (p % 2 == 1L)\
        \ {\n                val m1 = multiply(res.m1, if (res.isOff) base.m2 else base.m1,\
        \ m)\n                val m2 = multiply(res.m2, if (res.isOff) base.m1 else\
        \ base.m2, m)\n                res = ZigMatrix(m1, m2, res.isOff != base.isOff)\n\
        \            }\n            val m1 = multiply(base.m1, if (base.isOff) base.m2\
        \ else base.m1, m)\n            val m2 = multiply(base.m2, if (base.isOff) base.m1\
        \ else base.m2, m)\n            base = ZigMatrix(m1, m2, false)\n          \
        \  p /= 2\n        }\n\n        val vUp = LongArray(m) { it.toLong() }\n   \
        \     val vDown = LongArray(m) { (m - 1 - it).toLong() }\n\n        val ans\
        \ = if (res.isOff) {\n            (sumMV(res.m1, vDown, m) + sumMV(res.m2, vUp,\
        \ m)) % MOD\n        } else {\n            (sumMV(res.m1, vUp, m) + sumMV(res.m2,\
        \ vDown, m)) % MOD\n        }\n\n        return ans.toInt()\n    }\n}"
      dart: "class Solution {\n  static const int MOD = 1000000007;\n\n  List<List<int>>\
        \ multiply(List<List<int>> A, List<List<int>> B, int size) {\n    List<List<int>>\
        \ C = List.generate(size, (_) => List.filled(size, 0));\n    for (int i = 0;\
        \ i < size; i++) {\n      var Ai = A[i];\n      var Ci = C[i];\n      for (int\
        \ k = 0; k < size; k++) {\n        int Aik = Ai[k];\n        if (Aik == 0) continue;\n\
        \        var Bk = B[k];\n        for (int j = 0; j < size; j++) {\n        \
        \  if (Bk[j] == 0) continue;\n          Ci[j] = (Ci[j] + Aik * Bk[j]) % MOD;\n\
        \        }\n      }\n    }\n    return C;\n  }\n\n  List<List<int>> power(List<List<int>>\
        \ a, int n, int size) {\n    List<List<int>> res = List.generate(size, (_) =>\
        \ List.filled(size, 0));\n    for (int i = 0; i < size; i++) res[i][i] = 1;\n\
        \    while (n > 0) {\n      if (n % 2 == 1) res = multiply(res, a, size);\n\
        \      a = multiply(a, a, size);\n      n ~/= 2;\n    }\n    return res;\n \
        \ }\n\n  int zigZagArrays(int n, int l, int r) {\n    int m = r - l + 1;\n \
        \   if (n == 1) return m % MOD;\n    if (n == 2) return (m * (m - 1)) % MOD;\n\
        \n    int size = 2 * m;\n    List<List<int>> T = List.generate(size, (_) =>\
        \ List.filled(size, 0));\n    for (int i = 0; i < m; i++) {\n      for (int\
        \ j = 0; j < m; j++) {\n        if (i > j) T[i][j + m] = 1; // from (j, DOWN)\
        \ to (i, UP)\n        if (i < j) T[i + m][j] = 1; // from (j, UP) to (i, DOWN)\n\
        \      }\n    }\n\n    List<List<int>> TPow = power(T, n - 2, size);\n\n   \
        \ List<int> V2 = List.filled(size, 0);\n    for (int i = 0; i < m; i++) {\n\
        \      V2[i] = i; // (i, UP) counts\n      V2[i + m] = (m - 1) - i; // (i, DOWN)\
        \ counts\n    }\n\n    int total = 0;\n    for (int i = 0; i < size; i++) {\n\
        \      for (int j = 0; j < size; j++) {\n        total = (total + TPow[i][j]\
        \ * V2[j]) % MOD;\n      }\n    }\n\n    return total;\n  }\n}"
      go: "func zigZagArrays(n int, l int, r int) int {\n    const MOD = 1000000007\n\
        \    m := r - l + 1\n    if n == 1 {\n        return m % MOD\n    }\n    if\
        \ n == 2 {\n        return (m * (m - 1)) % MOD\n    }\n\n    size := 2 * m\n\
        \    multiply := func(A, B [][]int64, size int) [][]int64 {\n        C := make([][]int64,\
        \ size)\n        for i := range C {\n            C[i] = make([]int64, size)\n\
        \        }\n        for i := 0; i < size; i++ {\n            Ai := A[i]\n  \
        \          Ci := C[i]\n            for k := 0; k < size; k++ {\n           \
        \     Aik := Ai[k]\n                if Aik == 0 {\n                    continue\n\
        \                }\n                Bk := B[k]\n                for j := 0;\
        \ j < size; j++ {\n                    if Bk[j] == 0 {\n                   \
        \     continue\n                    }\n                    Ci[j] = (Ci[j] +\
        \ Aik*Bk[j]) % MOD\n                }\n            }\n        }\n        return\
        \ C\n    }\n\n    power := func(a [][]int64, p int, size int) [][]int64 {\n\
        \        res := make([][]int64, size)\n        for i := range res {\n      \
        \      res[i] = make([]int64, size)\n            res[i][i] = 1\n        }\n\
        \        for p > 0 {\n            if p%2 == 1 {\n                res = multiply(res,\
        \ a, size)\n            }\n            a = multiply(a, a, size)\n          \
        \  p /= 2\n        }\n        return res\n    }\n\n    T := make([][]int64,\
        \ size)\n    for i := range T {\n        T[i] = make([]int64, size)\n    }\n\
        \    for i := 0; i < m; i++ {\n        for j := 0; j < m; j++ {\n          \
        \  if i > j {\n                T[i][j+m] = 1\n            }\n            if\
        \ i < j {\n                T[i+m][j] = 1\n            }\n        }\n    }\n\n\
        \    TPow := power(T, n-2, size)\n    V2 := make([]int64, size)\n    for i :=\
        \ 0; i < m; i++ {\n        V2[i] = int64(i)\n        V2[i+m] = int64((m - 1)\
        \ - i)\n    }\n\n    total := int64(0)\n    for i := 0; i < size; i++ {\n  \
        \      for j := 0; j < size; j++ {\n            total = (total + TPow[i][j]*V2[j])\
        \ % MOD\n        }\n    }\n\n    return int(total)\n}"
      ruby: "# @param {Integer} n\n# @param {Integer} l\n# @param {Integer} r\n# @return\
        \ {Integer}\ndef zig_zag_arrays(n, l, r)\n  mod = 1_000_000_007\n  m = r - l\
        \ + 1\n  return m % mod if n == 1\n  return (m * (m - 1)) % mod if n == 2\n\n\
        \  size = 2 * m\n\n  def multiply(a, b, size, mod)\n    c = Array.new(size)\
        \ { Array.new(size, 0) }\n    i = 0\n    while i < size\n      ai = a[i]\n \
        \     ci = c[i]\n      k = 0\n      while k < size\n        aik = ai[k]\n  \
        \      if aik != 0\n          bk = b[k]\n          j = 0\n          while j\
        \ < size\n            bkj = bk[j]\n            if bkj != 0\n              ci[j]\
        \ = (ci[j] + aik * bkj) % mod\n            end\n            j += 1\n       \
        \   end\n        end\n        k += 1\n      end\n      i += 1\n    end\n   \
        \ c\n  end\n\n  def power(a, p, size, mod)\n    res = Array.new(size) { Array.new(size,\
        \ 0) }\n    size.times { |i| res[i][i] = 1 }\n    while p > 0\n      res = multiply(res,\
        \ a, size, mod) if p % 2 == 1\n      a = multiply(a, a, size, mod)\n      p\
        \ /= 2\n    end\n    res\n  end\n\n  t = Array.new(size) { Array.new(size, 0)\
        \ }\n  m.times do |i|\n    m.times do |j|\n      t[i][j + m] = 1 if i > j\n\
        \      t[i + m][j] = 1 if i < j\n    end\n  end\n\n  t_pow = power(t, n - 2,\
        \ size, mod)\n  v2 = Array.new(size, 0)\n  m.times do |i|\n    v2[i] = i\n \
        \   v2[i + m] = (m - 1) - i\n  end\n\n  total = 0\n  size.times do |i|\n   \
        \ row = t_pow[i]\n    size.times do |j|\n      if row[j] != 0 && v2[j] != 0\n\
        \        total = (total + row[j] * v2[j]) % mod\n      end\n    end\n  end\n\
        \  total\nend"
      scala: "object Solution {\n    def zigZagArrays(n: Int, l: Int, r: Int): Int =\
        \ {\n        val MOD = 1000000007L\n        val m = r - l + 1\n        if (n\
        \ == 1) return (m % MOD).toInt\n        if (n == 2) return ((m.toLong * (m -\
        \ 1)) % MOD).toInt\n\n        val size = 2 * m\n\n        def multiply(A: Array[Array[Long]],\
        \ B: Array[Array[Long]], size: Int): Array[Array[Long]] = {\n            val\
        \ C = Array.fill(size, size)(0L)\n            for (i <- 0 until size) {\n  \
        \              val Ai = A(i)\n                val Ci = C(i)\n              \
        \  for (k <- 0 until size) {\n                    val Aik = Ai(k)\n        \
        \            if (Aik != 0) {\n                        val Bk = B(k)\n      \
        \                  for (j <- 0 until size) {\n                            if\
        \ (Bk(j) != 0) {\n                                Ci(j) = (Ci(j) + Aik * Bk(j))\
        \ % MOD\n                            }\n                        }\n        \
        \            }\n                }\n            }\n            C\n        }\n\
        \n        def power(a: Array[Array[Long]], p: Int, size: Int): Array[Array[Long]]\
        \ = {\n            var base = a\n            var exp = p\n            var res\
        \ = Array.fill(size, size)(0L)\n            for (i <- 0 until size) res(i)(i)\
        \ = 1L\n            while (exp > 0) {\n                if (exp % 2 == 1) res\
        \ = multiply(res, base, size)\n                base = multiply(base, base, size)\n\
        \                exp /= 2\n            }\n            res\n        }\n\n   \
        \     val T = Array.fill(size, size)(0L)\n        for (i <- 0 until m) {\n \
        \           for (j <- 0 until m) {\n                if (i > j) T(i)(j + m) =\
        \ 1L\n                if (i < j) T(i + m)(j) = 1L\n            }\n        }\n\
        \n        val TPow = power(T, n - 2, size)\n        val V2 = new Array[Long](size)\n\
        \        for (i <- 0 until m) {\n            V2(i) = i.toLong\n            V2(i\
        \ + m) = (m - 1 - i).toLong\n        }\n\n        var total = 0L\n        for\
        \ (i <- 0 until size) {\n            val row = TPow(i)\n            for (j <-\
        \ 0 until size) {\n                if (row(j) != 0 && V2(j) != 0) {\n      \
        \              total = (total + row(j) * V2(j)) % MOD\n                }\n \
        \           }\n        }\n        total.toInt\n    }\n}"
      rust: '// Generation failed for Rust

        // Reason: Parsing failed'
      racket: '// Generation failed for Racket

        // Reason: Parsing failed'
      erlang: '// Generation failed for Erlang

        // Reason: Parsing failed'
      elixir: '// Generation failed for Elixir

        // Reason: Parsing failed'
    approach: The problem can be modeled using dynamic programming where each state
      represents the current length of the ZigZag array, the last element added, and
      the direction of the last transition (UP if the current element is greater than
      the previous, DOWN otherwise). Since $n$ is very large ($10^9$), we use matrix
      exponentiation to compute the number of valid arrays. We define $V_{i, UP}$ as
      a vector where the $j$-th entry is the number of ZigZag arrays of length $i$ ending
      with the $j$-th value in the range $[l, r]$ after an UP transition. Symmetry analysis
      shows that the count of arrays ending in a DOWN transition is simply the reverse
      of the UP vector. This reduces the state space by half.
    time_complexity: O(m^3 \log n) where $m = r - l + 1$. The bottleneck is the matrix
      exponentiation of an $m \times m$ matrix, where $m \le 75$. For $n=10^9$, $\log
      n \approx 30$, leading to approximately $1.2 \times 10^7$ operations, which is
      efficient for the given constraints.
    space_complexity: O(m^2) to store the $m \times m$ transition matrix and its powers,
      which is very small for $m \le 75$.
    elapsed_time: 1007.6912877559662
    model: gemini-3-flash-preview
    generated_at: '2026-06-24 02:51:40 '
---

## Problem #3700: Number of ZigZag Arrays II

**Difficulty:** Hard

**Topics:** Math, Dynamic Programming

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
	<li><code>[5, 4, 5]</code></li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, l = 1, r = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">10</span></p>

<p><strong>Explanation:</strong></p>

<p>​​​​​​​There are 10 valid ZigZag arrays of length <code>n = 3</code> using values in the range <code>[1, 3]</code>:</p>

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
	<li><code>3 &lt;= n &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= l &lt; r &lt;= 75</code>​​​​​​​</li>
</ul>


## Hints

1. Use matrix exponentiation

2. Encode states in a vector of length `2*m` where `m = r - l + 1`: first `m` entries = "next compare = down" for values, next `m` = "next compare = up".

3. Build a transition matrix `T` (size `2*m × 2*m`): from an `up,x` state go to `down,y` for every `y > x`, and from `down,x` go to `up,y` for every `y < x`.

4. Use fast matrix exponentiation to compute `T^(n-1)`, apply it to the initial vector (ones in the block for starting `up` and separately for starting `down`), sum final entries, and add both results (for `n=1` return `m`).

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be modeled using dynamic programming where each state represents the current length of the ZigZag array, the last element added, and the direction of the last transition (UP if the current element is greater than the previous, DOWN otherwise). Since $n$ is very large ($10^9$), we use matrix exponentiation to compute the number of valid arrays. We define $V_{i, UP}$ as a vector where the $j$-th entry is the number of ZigZag arrays of length $i$ ending with the $j$-th value in the range $[l, r]$ after an UP transition. Symmetry analysis shows that the count of arrays ending in a DOWN transition is simply the reverse of the UP vector. This reduces the state space by half.

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
        if (n == 1) return r - l + 1;
        long long m = r - l + 1;
        long long mod = 1e9 + 7;
        if (n == 2) return (m * (m - 1)) % mod;

        auto multiply = [&](const vector<vector<long long>>& A, const vector<vector<long long>>& B) {
            vector<vector<long long>> C(m, vector<long long>(m, 0));
            for (int i = 0; i < m; ++i) {
                for (int k = 0; k < m; ++k) {
                    if (A[i][k] == 0) continue;
                    for (int j = 0; j < m; ++j) {
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod;
                    }
                }
            }
            return C;
        };

        vector<vector<long long>> mat(m, vector<long long>(m));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < m; ++j) {
                mat[i][j] = min(i, j);
            }
        }

        long long p = n - 2;
        long long k = p / 2;
        vector<vector<long long>> res(m, vector<long long>(m, 0));
        for (int i = 0; i < m; ++i) res[i][i] = 1;

        while (k > 0) {
            if (k & 1) res = multiply(res, mat);
            mat = multiply(mat, mat);
            k >>= 1;
        }

        vector<long long> v(m);
        for (int i = 0; i < m; ++i) {
            long long sum = 0;
            for (int j = 0; j < m; ++j) {
                sum = (sum + res[i][j] * j) % mod;
            }
            v[i] = sum;
        }

        long long total = 0;
        if (p % 2 == 0) {
            for (int i = 0; i < m; ++i) total = (total + v[i]) % mod;
        } else {
            for (int i = 0; i < m; ++i) total = (total + v[i] * i) % mod;
        }

        return (total * 2) % mod;
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
        if (n == 1) return r - l + 1;
        int m = r - l + 1;
        long mod = 1000000007;
        if (n == 2) return (int) (((long) m * (m - 1)) % mod);

        long[][] mat = new long[m][m];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                mat[i][j] = Math.min(i, j);
            }
        }

        long p = n - 2;
        long k = p / 2;
        long[][] res = new long[m][m];
        for (int i = 0; i < m; i++) res[i][i] = 1;

        while (k > 0) {
            if (k % 2 == 1) res = multiply(res, mat, m, mod);
            mat = multiply(mat, mat, m, mod);
            k /= 2;
        }

        long total = 0;
        if (p % 2 == 0) {
            for (int i = 0; i < m; i++) {
                long vi = 0;
                for (int j = 0; j < m; j++) {
                    vi = (vi + res[i][j] * j) % mod;
                }
                total = (total + vi) % mod;
            }
        } else {
            for (int i = 0; i < m; i++) {
                long vi = 0;
                for (int j = 0; j < m; j++) {
                    vi = (vi + res[i][j] * j) % mod;
                }
                total = (total + vi * i) % mod;
            }
        }

        return (int) ((total * 2) % mod);
    }

    private long[][] multiply(long[][] A, long[][] B, int m, long mod) {
        long[][] C = new long[m][m];
        for (int i = 0; i < m; i++) {
            for (int k = 0; k < m; k++) {
                if (A[i][k] == 0) continue;
                for (int j = 0; j < m; j++) {
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod;
                }
            }
        }
        return C;
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
        if n == 1: return r - l + 1
        m = r - l + 1
        mod = 10**9 + 7
        if n == 2: return (m * (m - 1)) % mod

        def multiply(A, B, m, mod):
            C = [[0] * m for _ in range(m)]
            for i in range(m):
                Ai = A[i]
                Ci = C[i]
                for k in range(m):
                    if Ai[k] == 0: continue
                    temp = Ai[k]
                    Bk = B[k]
                    for j in range(m):
                        Ci[j] = (Ci[j] + temp * Bk[j]) % mod
            return C

        mat = [[min(i, j) for j in range(m)] for i in range(m)]
        p = n - 2
        k = p // 2
        res = [[0] * m for _ in range(m)]
        for i in range(m): res[i][i] = 1

        while k > 0:
            if k % 2 == 1:
                res = multiply(res, mat, m, mod)
            mat = multiply(mat, mat, m, mod)
            k //= 2

        v = [0] * m
        for i in range(m):
            row = res[i]
            curr = 0
            for j in range(m):
                curr = (curr + row[j] * j) % mod
            v[i] = curr

        total = 0
        if p % 2 == 0:
            total = sum(v) % mod
        else:
            for i in range(m):
                total = (total + v[i] * i) % mod

        return (total * 2) % mod
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1
        size = 2 * m
        mod = 10**9 + 7

        def multiply(A, B):
            C = [[0] * size for _ in range(size)]
            for i in range(size):
                Ai, Ci = A[i], C[i]
                for k in range(size):
                    Aik = Ai[k]
                    if Aik == 0:
                        continue
                    Bk = B[k]
                    for j in range(size):
                        if Bk[j]:
                            Ci[j] = (Ci[j] + Aik * Bk[j]) % mod
            return C

        def power(A, p):
            res = [[0] * size for _ in range(size)]
            for i in range(size): 
                res[i][i] = 1
            while p > 0:
                if p % 2 == 1: 
                    res = multiply(res, A)
                A = multiply(A, A)
                p //= 2
            return res

        T = [[0] * size for _ in range(size)]
        for i in range(m):
            for j in range(m):
                if i > j: 
                    T[i][j + m] = 1
                if i < j: 
                    T[i + m][j] = 1

        Tn = power(T, n - 1)
        ans = 0
        for row in Tn:
            ans = (ans + sum(row)) % mod
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

long long mod = 1000000007;

void multiply(int size, long long A[150][150], long long B[150][150], long long res[150][150]) {
    static long long temp[150][150];
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) temp[i][j] = 0;
        for (int k = 0; k < size; k++) {
            if (A[i][k] == 0) continue;
            for (int j = 0; j < size; j++) {
                if (B[k][j] == 0) continue;
                temp[i][j] = (temp[i][j] + A[i][k] * B[k][j]) % mod;
            }
        }
    }
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) res[i][j] = temp[i][j];
    }
}

int zigZagArrays(int n, int l, int r) {
    int m = r - l + 1;
    int size = 2 * m;
    long long T[150][150];
    memset(T, 0, sizeof(T));
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            if (i > j) T[i][j + m] = 1;
            if (i < j) T[i + m][j] = 1;
        }
    }

    long long res[150][150];
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) res[i][j] = (i == j);
    }

    int p = n - 1;
    while (p > 0) {
        if (p % 2 == 1) multiply(size, res, T, res);
        multiply(size, T, T, T);
        p /= 2;
    }

    long long ans = 0;
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            ans = (ans + res[i][j]) % mod;
        }
    }
    return (int)ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int ZigZagArrays(int n, int l, int r) {
        int m = r - l + 1;
        int size = 2 * m;
        long mod = 1000000007;

        long[,] T = new long[size, size];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                if (i > j) T[i, j + m] = 1;
                if (i < j) T[i + m, j] = 1;
            }
        }

        long[,] res = MatrixPower(T, n - 1, size, mod);
        long ans = 0;
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                ans = (ans + res[i, j]) % mod;
            }
        }

        return (int)ans;
    }

    private long[,] MatrixMultiply(long[,] A, long[,] B, int size, long mod) {
        long[,] C = new long[size, size];
        for (int i = 0; i < size; i++) {
            for (int k = 0; k < size; k++) {
                if (A[i, k] == 0) continue;
                for (int j = 0; j < size; j++) {
                    if (B[k, j] == 0) continue;
                    C[i, j] = (C[i, j] + A[i, k] * B[k, j]) % mod;
                }
            }
        }
        return C;
    }

    private long[,] MatrixPower(long[,] A, int p, int size, long mod) {
        long[,] res = new long[size, size];
        for (int i = 0; i < size; i++) res[i, i] = 1;
        long[,] baseMat = A;
        while (p > 0) {
            if (p % 2 == 1) res = MatrixMultiply(res, baseMat, size, mod);
            baseMat = MatrixMultiply(baseMat, baseMat, size, mod);
            p /= 2;
        }
        return res;
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
    const m = r - l + 1;
    const size = 2 * m;
    const mod = 1000000007n;

    function multiply(A, B) {
        const C = Array.from({ length: size }, () => new BigInt64Array(size));
        for (let i = 0; i < size; i++) {
            for (let k = 0; k < size; k++) {
                if (A[i][k] === 0n) continue;
                for (let j = 0; j < size; j++) {
                    if (B[k][j] === 0n) continue;
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod;
                }
            }
        }
        return C;
    }

    function power(A, p) {
        let res = Array.from({ length: size }, (_, i) => {
            const row = new BigInt64Array(size);
            row[i] = 1n;
            return row;
        });
        let base = A;
        while (p > 0) {
            if (p % 2 === 1) res = multiply(res, base);
            base = multiply(base, base);
            p = Math.floor(p / 2);
        }
        return res;
    }

    const T = Array.from({ length: size }, () => new BigInt64Array(size));
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < m; j++) {
            if (i > j) T[i][j + m] = 1n;
            if (i < j) T[i + m][j] = 1n;
        }
    }

    const Tn = power(T, n - 1);
    let ans = 0n;
    for (let i = 0; i < size; i++) {
        for (let j = 0; j < size; j++) {
            ans = (ans + Tn[i][j]) % mod;
        }
    }

    return Number(ans);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
class ZigMatrix {
  m1: bigint[][];
  m2: bigint[][];
  isOff: boolean;

  constructor(m1: bigint[][], m2: bigint[][], isOff: boolean) {
    this.m1 = m1;
    this.m2 = m2;
    this.isOff = isOff;
  }
}

function multiply(A: bigint[][], B: bigint[][], m: number): bigint[][] {
  const res: bigint[][] = Array.from({ length: m }, () => Array(m).fill(0n));
  const MOD = 1000000007n;
  for (let i = 0; i < m; i++) {
    for (let k = 0; k < m; k++) {
      if (A[i][k] === 0n) continue;
      const rowVal = A[i][k];
      for (let j = 0; j < m; j++) {
        res[i][j] = (res[i][j] + rowVal * B[k][j]) % MOD;
      }
    }
  }
  return res;
}

function sumMV(M: bigint[][], V: bigint[], m: number): bigint {
  let total = 0n;
  const MOD = 1000000007n;
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < m; j++) {
      total = (total + M[i][j] * V[j]) % MOD;
    }
  }
  return total;
}

function zigZagArrays(n: number, l: number, r: number): number {
  const m = r - l + 1;
  const MOD = 1000000007n;
  if (n === 1) return m % Number(MOD);

  const a: bigint[][] = Array.from({ length: m }, (_, i) =>
    Array.from({ length: m }, (_, j) => (i > j ? 1n : 0n))
  );
  const b: bigint[][] = Array.from({ length: m }, (_, i) =>
    Array.from({ length: m }, (_, j) => (i < j ? 1n : 0n))
  );

  const identityM: bigint[][] = Array.from({ length: m }, (_, i) =>
    Array.from({ length: m }, (_, j) => (i === j ? 1n : 0n))
  );

  let res = new ZigMatrix(identityM, identityM, false);
  let base = new ZigMatrix(a, b, true);

  let p = BigInt(n) - 2n;
  while (p > 0n) {
    if (p % 2n === 1n) {
      const m1 = multiply(res.m1, res.isOff ? base.m2 : base.m1, m);
      const m2 = multiply(res.m2, res.isOff ? base.m1 : base.m2, m);
      res = new ZigMatrix(m1, m2, res.isOff !== base.isOff);
    }
    const m1 = multiply(base.m1, base.isOff ? base.m2 : base.m1, m);
    const m2 = multiply(base.m2, base.isOff ? base.m1 : base.m2, m);
    base = new ZigMatrix(m1, m2, false);
    p = p / 2n;
  }

  const vUp: bigint[] = Array.from({ length: m }, (_, i) => BigInt(i));
  const vDown: bigint[] = Array.from({ length: m }, (_, i) => BigInt(m - 1 - i));

  let ans: bigint;
  if (res.isOff) {
    ans = (sumMV(res.m1, vDown, m) + sumMV(res.m2, vUp, m)) % MOD;
  } else {
    ans = (sumMV(res.m1, vUp, m) + sumMV(res.m2, vDown, m)) % MOD;
  }

  return Number(ans);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class ZigMatrix {
    public $m1;
    public $m2;
    public $isOff;
    function __construct($m1, $m2, $isOff) {
        $this->m1 = $m1;
        $this->m2 = $m2;
        $this->isOff = $isOff;
    }
}

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
        if ($n == 1) return $m % $MOD;

        $a = array_fill(0, $m, array_fill(0, $m, 0));
        $b = array_fill(0, $m, array_fill(0, $m, 0));
        $identity = array_fill(0, $m, array_fill(0, $m, 0));

        for ($i = 0; $i < $m; $i++) {
            $identity[$i][$i] = 1;
            for ($j = 0; $j < $m; $j++) {
                if ($i > $j) $a[$i][$j] = 1;
                if ($i < $j) $b[$i][$j] = 1;
            }
        }

        $res = new ZigMatrix($identity, $identity, false);
        $base = new ZigMatrix($a, $b, true);

        $p = $n - 2;
        while ($p > 0) {
            if ($p % 2 == 1) {
                $res = $this->matMulStruct($res, $base, $m, $MOD);
            }
            $base = $this->matMulStruct($base, $base, $m, $MOD);
            $p = (int)($p / 2);
        }

        $vUp = [];
        $vDown = [];
        for ($i = 0; $i < $m; $i++) {
            $vUp[$i] = $i;
            $vDown[$i] = $m - 1 - $i;
        }

        if ($res->isOff) {
            $ans = ($this->sumMV($res->m1, $vDown, $m, $MOD) + $this->sumMV($res->m2, $vUp, $m, $MOD)) % $MOD;
        } else {
            $ans = ($this->sumMV($res->m1, $vUp, $m, $MOD) + $this->sumMV($res->m2, $vDown, $m, $MOD)) % $MOD;
        }

        return $ans;
    }

    function matMulStruct($A, $B, $m, $MOD) {
        $isOff = $A->isOff ^ $B->isOff;
        $m1 = $this->multiply($A->m1, $A->isOff ? $B->m2 : $B->m1, $m, $MOD);
        $m2 = $this->multiply($A->m2, $A->isOff ? $B->m1 : $B->m2, $m, $MOD);
        return new ZigMatrix($m1, $m2, (bool)$isOff);
    }

    function multiply($A, $B, $m, $MOD) {
        $res = array_fill(0, $m, array_fill(0, $m, 0));
        for ($i = 0; $i < $m; $i++) {
            for ($k = 0; $k < $m; $k++) {
                if ($A[$i][$k] == 0) continue;
                $rowA = $A[$i][$k];
                for ($j = 0; $j < $m; $j++) {
                    $res[$i][$j] = ($res[$i][$j] + $rowA * $B[$k][$j]) % $MOD;
                }
            }
        }
        return $res;
    }

    function sumMV($M, $V, $m, $MOD) {
        $total = 0;
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $m; $j++) {
                $total = ($total + $M[$i][$j] * $V[$j]) % $MOD;
            }
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
    struct ZigMatrix {
        let m1: [[Int64]]
        let m2: [[Int64]]
        let isOff: Bool
    }

    func multiply(_ A: [[Int64]], _ B: [[Int64]], _ m: Int) -> [[Int64]] {
        let MOD: Int64 = 1000000007
        var res = [[Int64]](repeating: [Int64](repeating: 0, count: m), count: m)
        for i in 0..<m {
            for k in 0..<m {
                if A[i][k] == 0 { continue }
                let rowVal = A[i][k]
                for j in 0..<m {
                    res[i][j] = (res[i][j] + rowVal * B[k][j]) % MOD
                }
            }
        }
        return res
    }

    func sumMV(_ M: [[Int64]], _ V: [Int64], _ m: Int) -> Int64 {
        let MOD: Int64 = 1000000007
        var total: Int64 = 0
        for i in 0..<m {
            for j in 0..<m {
                total = (total + M[i][j] * V[j]) % MOD
            }
        }
        return total
    }

    func zigZagArrays(_ n: Int, _ l: Int, _ r: Int) -> Int {
        let m = r - l + 1
        let MOD: Int64 = 1000000007
        if n == 1 { return m % Int(MOD) }

        var a = [[Int64]](repeating: [Int64](repeating: 0, count: m), count: m)
        var b = [[Int64]](repeating: [Int64](repeating: 0, count: m), count: m)
        var identity = [[Int64]](repeating: [Int64](repeating: 0, count: m), count: m)

        for i in 0..<m {
            identity[i][i] = 1
            for j in 0..<m {
                if i > j { a[i][j] = 1 }
                if i < j { b[i][j] = 1 }
            }
        }

        var res = ZigMatrix(m1: identity, m2: identity, isOff: false)
        var base = ZigMatrix(m1: a, m2: b, isOff: true)

        var p = n - 2
        while p > 0 {
            if p % 2 == 1 {
                let m1 = multiply(res.m1, res.isOff ? base.m2 : base.m1, m)
                let m2 = multiply(res.m2, res.isOff ? base.m1 : base.m2, m)
                res = ZigMatrix(m1: m1, m2: m2, isOff: res.isOff != base.isOff)
            }
            let m1 = multiply(base.m1, base.isOff ? base.m2 : base.m1, m)
            let m2 = multiply(base.m2, base.isOff ? base.m1 : base.m2, m)
            base = ZigMatrix(m1: m1, m2: m2, isOff: false)
            p /= 2
        }

        var vUp = [Int64](repeating: 0, count: m)
        var vDown = [Int64](repeating: 0, count: m)
        for i in 0..<m {
            vUp[i] = Int64(i)
            vDown[i] = Int64(m - 1 - i)
        }

        var ans: Int64 = 0
        if res.isOff {
            ans = (sumMV(res.m1, vDown, m) + sumMV(res.m2, vUp, m)) % MOD
        } else {
            ans = (sumMV(res.m1, vUp, m) + sumMV(res.m2, vDown, m)) % MOD
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
    class ZigMatrix(val m1: Array<LongArray>, val m2: Array<LongArray>, val isOff: Boolean)

    private fun multiply(A: Array<LongArray>, B: Array<LongArray>, m: Int): Array<LongArray> {
        val MOD = 1000000007L
        val res = Array(m) { LongArray(m) }
        for (i in 0 until m) {
            for (k in 0 until m) {
                if (A[i][k] == 0L) continue
                val rowVal = A[i][k]
                for (j in 0 until m) {
                    res[i][j] = (res[i][j] + rowVal * B[k][j]) % MOD
                }
            }
        }
        return res
    }

    private fun sumMV(M: Array<LongArray>, V: LongArray, m: Int): Long {
        val MOD = 1000000007L
        var total = 0L
        for (i in 0 until m) {
            for (j in 0 until m) {
                total = (total + M[i][j] * V[j]) % MOD
            }
        }
        return total
    }

    fun zigZagArrays(n: Int, l: Int, r: Int): Int {
        val m = r - l + 1
        val MOD = 1000000007L
        if (n == 1) return (m % MOD).toInt()

        val a = Array(m) { i -> LongArray(m) { j -> if (i > j) 1L else 0L } }
        val b = Array(m) { i -> LongArray(m) { j -> if (i < j) 1L else 0L } }
        val identity = Array(m) { i -> LongArray(m) { j -> if (i == j) 1L else 0L } }

        var res = ZigMatrix(identity, identity, false)
        var base = ZigMatrix(a, b, true)

        var p = n.toLong() - 2L
        while (p > 0) {
            if (p % 2 == 1L) {
                val m1 = multiply(res.m1, if (res.isOff) base.m2 else base.m1, m)
                val m2 = multiply(res.m2, if (res.isOff) base.m1 else base.m2, m)
                res = ZigMatrix(m1, m2, res.isOff != base.isOff)
            }
            val m1 = multiply(base.m1, if (base.isOff) base.m2 else base.m1, m)
            val m2 = multiply(base.m2, if (base.isOff) base.m1 else base.m2, m)
            base = ZigMatrix(m1, m2, false)
            p /= 2
        }

        val vUp = LongArray(m) { it.toLong() }
        val vDown = LongArray(m) { (m - 1 - it).toLong() }

        val ans = if (res.isOff) {
            (sumMV(res.m1, vDown, m) + sumMV(res.m2, vUp, m)) % MOD
        } else {
            (sumMV(res.m1, vUp, m) + sumMV(res.m2, vDown, m)) % MOD
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
class Solution {
  static const int MOD = 1000000007;

  List<List<int>> multiply(List<List<int>> A, List<List<int>> B, int size) {
    List<List<int>> C = List.generate(size, (_) => List.filled(size, 0));
    for (int i = 0; i < size; i++) {
      var Ai = A[i];
      var Ci = C[i];
      for (int k = 0; k < size; k++) {
        int Aik = Ai[k];
        if (Aik == 0) continue;
        var Bk = B[k];
        for (int j = 0; j < size; j++) {
          if (Bk[j] == 0) continue;
          Ci[j] = (Ci[j] + Aik * Bk[j]) % MOD;
        }
      }
    }
    return C;
  }

  List<List<int>> power(List<List<int>> a, int n, int size) {
    List<List<int>> res = List.generate(size, (_) => List.filled(size, 0));
    for (int i = 0; i < size; i++) res[i][i] = 1;
    while (n > 0) {
      if (n % 2 == 1) res = multiply(res, a, size);
      a = multiply(a, a, size);
      n ~/= 2;
    }
    return res;
  }

  int zigZagArrays(int n, int l, int r) {
    int m = r - l + 1;
    if (n == 1) return m % MOD;
    if (n == 2) return (m * (m - 1)) % MOD;

    int size = 2 * m;
    List<List<int>> T = List.generate(size, (_) => List.filled(size, 0));
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < m; j++) {
        if (i > j) T[i][j + m] = 1; // from (j, DOWN) to (i, UP)
        if (i < j) T[i + m][j] = 1; // from (j, UP) to (i, DOWN)
      }
    }

    List<List<int>> TPow = power(T, n - 2, size);

    List<int> V2 = List.filled(size, 0);
    for (int i = 0; i < m; i++) {
      V2[i] = i; // (i, UP) counts
      V2[i + m] = (m - 1) - i; // (i, DOWN) counts
    }

    int total = 0;
    for (int i = 0; i < size; i++) {
      for (int j = 0; j < size; j++) {
        total = (total + TPow[i][j] * V2[j]) % MOD;
      }
    }

    return total;
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
    if n == 1 {
        return m % MOD
    }
    if n == 2 {
        return (m * (m - 1)) % MOD
    }

    size := 2 * m
    multiply := func(A, B [][]int64, size int) [][]int64 {
        C := make([][]int64, size)
        for i := range C {
            C[i] = make([]int64, size)
        }
        for i := 0; i < size; i++ {
            Ai := A[i]
            Ci := C[i]
            for k := 0; k < size; k++ {
                Aik := Ai[k]
                if Aik == 0 {
                    continue
                }
                Bk := B[k]
                for j := 0; j < size; j++ {
                    if Bk[j] == 0 {
                        continue
                    }
                    Ci[j] = (Ci[j] + Aik*Bk[j]) % MOD
                }
            }
        }
        return C
    }

    power := func(a [][]int64, p int, size int) [][]int64 {
        res := make([][]int64, size)
        for i := range res {
            res[i] = make([]int64, size)
            res[i][i] = 1
        }
        for p > 0 {
            if p%2 == 1 {
                res = multiply(res, a, size)
            }
            a = multiply(a, a, size)
            p /= 2
        }
        return res
    }

    T := make([][]int64, size)
    for i := range T {
        T[i] = make([]int64, size)
    }
    for i := 0; i < m; i++ {
        for j := 0; j < m; j++ {
            if i > j {
                T[i][j+m] = 1
            }
            if i < j {
                T[i+m][j] = 1
            }
        }
    }

    TPow := power(T, n-2, size)
    V2 := make([]int64, size)
    for i := 0; i < m; i++ {
        V2[i] = int64(i)
        V2[i+m] = int64((m - 1) - i)
    }

    total := int64(0)
    for i := 0; i < size; i++ {
        for j := 0; j < size; j++ {
            total = (total + TPow[i][j]*V2[j]) % MOD
        }
    }

    return int(total)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} n
# @param {Integer} l
# @param {Integer} r
# @return {Integer}
def zig_zag_arrays(n, l, r)
  mod = 1_000_000_007
  m = r - l + 1
  return m % mod if n == 1
  return (m * (m - 1)) % mod if n == 2

  size = 2 * m

  def multiply(a, b, size, mod)
    c = Array.new(size) { Array.new(size, 0) }
    i = 0
    while i < size
      ai = a[i]
      ci = c[i]
      k = 0
      while k < size
        aik = ai[k]
        if aik != 0
          bk = b[k]
          j = 0
          while j < size
            bkj = bk[j]
            if bkj != 0
              ci[j] = (ci[j] + aik * bkj) % mod
            end
            j += 1
          end
        end
        k += 1
      end
      i += 1
    end
    c
  end

  def power(a, p, size, mod)
    res = Array.new(size) { Array.new(size, 0) }
    size.times { |i| res[i][i] = 1 }
    while p > 0
      res = multiply(res, a, size, mod) if p % 2 == 1
      a = multiply(a, a, size, mod)
      p /= 2
    end
    res
  end

  t = Array.new(size) { Array.new(size, 0) }
  m.times do |i|
    m.times do |j|
      t[i][j + m] = 1 if i > j
      t[i + m][j] = 1 if i < j
    end
  end

  t_pow = power(t, n - 2, size, mod)
  v2 = Array.new(size, 0)
  m.times do |i|
    v2[i] = i
    v2[i + m] = (m - 1) - i
  end

  total = 0
  size.times do |i|
    row = t_pow[i]
    size.times do |j|
      if row[j] != 0 && v2[j] != 0
        total = (total + row[j] * v2[j]) % mod
      end
    end
  end
  total
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
        if (n == 1) return (m % MOD).toInt
        if (n == 2) return ((m.toLong * (m - 1)) % MOD).toInt

        val size = 2 * m

        def multiply(A: Array[Array[Long]], B: Array[Array[Long]], size: Int): Array[Array[Long]] = {
            val C = Array.fill(size, size)(0L)
            for (i <- 0 until size) {
                val Ai = A(i)
                val Ci = C(i)
                for (k <- 0 until size) {
                    val Aik = Ai(k)
                    if (Aik != 0) {
                        val Bk = B(k)
                        for (j <- 0 until size) {
                            if (Bk(j) != 0) {
                                Ci(j) = (Ci(j) + Aik * Bk(j)) % MOD
                            }
                        }
                    }
                }
            }
            C
        }

        def power(a: Array[Array[Long]], p: Int, size: Int): Array[Array[Long]] = {
            var base = a
            var exp = p
            var res = Array.fill(size, size)(0L)
            for (i <- 0 until size) res(i)(i) = 1L
            while (exp > 0) {
                if (exp % 2 == 1) res = multiply(res, base, size)
                base = multiply(base, base, size)
                exp /= 2
            }
            res
        }

        val T = Array.fill(size, size)(0L)
        for (i <- 0 until m) {
            for (j <- 0 until m) {
                if (i > j) T(i)(j + m) = 1L
                if (i < j) T(i + m)(j) = 1L
            }
        }

        val TPow = power(T, n - 2, size)
        val V2 = new Array[Long](size)
        for (i <- 0 until m) {
            V2(i) = i.toLong
            V2(i + m) = (m - 1 - i).toLong
        }

        var total = 0L
        for (i <- 0 until size) {
            val row = TPow(i)
            for (j <- 0 until size) {
                if (row(j) != 0 && V2(j) != 0) {
                    total = (total + row(j) * V2(j)) % MOD
                }
            }
        }
        total.toInt
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
// Generation failed for Rust
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
// Generation failed for Racket
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
// Generation failed for Erlang
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
// Generation failed for Elixir
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(m^3 \log n) where $m = r - l + 1$. The bottleneck is the matrix exponentiation of an $m \times m$ matrix, where $m \le 75$. For $n=10^9$, $\log n \approx 30$, leading to approximately $1.2 \times 10^7$ operations, which is efficient for the given constraints.
- **Space Complexity:** O(m^2) to store the $m \times m$ transition matrix and its powers, which is very small for $m \le 75$.
