---
layout: post
title: "Concatenate Non-Zero Digits and Multiply by Sum II"
date: 2026-07-08 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Math", "String", "Prefix Sum"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> sumAndMultiply(string s, vector<vector<int>>&\
        \ queries) {\n        int m = s.length();\n        long long MOD = 1000000007LL;\n\
        \        vector<int> v;\n        vector<int> v_orig_idx;\n        for (int i\
        \ = 0; i < m; ++i) {\n            if (s[i] != '0') {\n                v.push_back(s[i]\
        \ - '0');\n                v_orig_idx.push_back(i);\n            }\n       \
        \ }\n\n        int v_size = v.size();\n        vector<int> first_idx(m, v_size);\n\
        \        int v_ptr = 0;\n        for (int i = 0; i < m; ++i) {\n           \
        \ while (v_ptr < v_size && v_orig_idx[v_ptr] < i) v_ptr++;\n            first_idx[i]\
        \ = v_ptr;\n        }\n\n        vector<int> last_idx(m, -1);\n        int curr_last\
        \ = -1;\n        for (int i = 0; i < m; ++i) {\n            if (s[i] != '0')\
        \ curr_last++;\n            last_idx[i] = curr_last;\n        }\n\n        vector<long\
        \ long> P(v_size + 1, 0);\n        vector<long long> prefixSum(v_size + 1, 0);\n\
        \        vector<long long> pow10(v_size + 1, 1);\n        for (int i = 0; i\
        \ < v_size; ++i) {\n            P[i + 1] = (P[i] * 10 + v[i]) % MOD;\n     \
        \       prefixSum[i + 1] = prefixSum[i] + v[i];\n            pow10[i + 1] =\
        \ (pow10[i] * 10) % MOD;\n        }\n\n        int n = queries.size();\n   \
        \     vector<int> ans(n);\n        for (int i = 0; i < n; ++i) {\n         \
        \   int L = first_idx[queries[i][0]];\n            int R = last_idx[queries[i][1]];\n\
        \            if (L > R) {\n                ans[i] = 0;\n            } else {\n\
        \                long long x = (P[R + 1] - (P[L] * pow10[R - L + 1]) % MOD +\
        \ MOD) % MOD;\n                long long s_val = (prefixSum[R + 1] - prefixSum[L]);\n\
        \                ans[i] = (int)((x * (s_val % MOD)) % MOD);\n            }\n\
        \        }\n        return ans;\n    }\n};"
      java: "class Solution {\n    public int[] sumAndMultiply(String s, int[][] queries)\
        \ {\n        int m = s.length();\n        long MOD = 1000000007L;\n        int\
        \ v_size = 0;\n        for (int i = 0; i < m; i++) if (s.charAt(i) != '0') v_size++;\n\
        \n        int[] v = new int[v_size];\n        int[] v_orig_idx = new int[v_size];\n\
        \        int idx = 0;\n        for (int i = 0; i < m; i++) {\n            if\
        \ (s.charAt(i) != '0') {\n                v[idx] = s.charAt(i) - '0';\n    \
        \            v_orig_idx[idx] = i;\n                idx++;\n            }\n \
        \       }\n\n        int[] first_idx = new int[m];\n        int v_ptr = 0;\n\
        \        for (int i = 0; i < m; i++) {\n            while (v_ptr < v_size &&\
        \ v_orig_idx[v_ptr] < i) v_ptr++;\n            first_idx[i] = v_ptr;\n     \
        \   }\n\n        int[] last_idx = new int[m];\n        int curr_last = -1;\n\
        \        for (int i = 0; i < m; i++) {\n            if (s.charAt(i) != '0')\
        \ curr_last++;\n            last_idx[i] = curr_last;\n        }\n\n        long[]\
        \ P = new long[v_size + 1];\n        long[] prefixSum = new long[v_size + 1];\n\
        \        long[] pow10 = new long[v_size + 1];\n        pow10[0] = 1;\n     \
        \   for (int i = 0; i < v_size; i++) {\n            P[i + 1] = (P[i] * 10 +\
        \ v[i]) % MOD;\n            prefixSum[i + 1] = prefixSum[i] + v[i];\n      \
        \      pow10[i + 1] = (pow10[i] * 10) % MOD;\n        }\n\n        int n = queries.length;\n\
        \        int[] ans = new int[n];\n        for (int i = 0; i < n; i++) {\n  \
        \          int L = first_idx[queries[i][0]];\n            int R = last_idx[queries[i][1]];\n\
        \            if (L > R) {\n                ans[i] = 0;\n            } else {\n\
        \                long x = (P[R + 1] - (P[L] * pow10[R - L + 1]) % MOD + MOD)\
        \ % MOD;\n                long s_val = prefixSum[R + 1] - prefixSum[L];\n  \
        \              ans[i] = (int)((x * (s_val % MOD)) % MOD);\n            }\n \
        \       }\n        return ans;\n    }\n}"
      python: "class Solution(object):\n    def sumAndMultiply(self, s, queries):\n\
        \        \"\"\"\n        :type s: str\n        :type queries: List[List[int]]\n\
        \        :rtype: List[int]\n        \"\"\"\n        MOD = 1000000007\n     \
        \   m = len(s)\n        v = [ord(c) - 48 for c in s if c != '0']\n        v_orig_idx\
        \ = [i for i, c in enumerate(s) if c != '0']\n        v_size = len(v)\n\n  \
        \      first_idx = [0] * m\n        v_ptr = 0\n        for i in xrange(m):\n\
        \            while v_ptr < v_size and v_orig_idx[v_ptr] < i:\n             \
        \   v_ptr += 1\n            first_idx[i] = v_ptr\n\n        last_idx = [0] *\
        \ m\n        curr_last = -1\n        for i in xrange(m):\n            if s[i]\
        \ != '0':\n                curr_last += 1\n            last_idx[i] = curr_last\n\
        \n        P = [0] * (v_size + 1)\n        prefixSum = [0] * (v_size + 1)\n \
        \       pow10 = [1] * (v_size + 1)\n        for i in xrange(v_size):\n     \
        \       P[i+1] = (P[i] * 10 + v[i]) % MOD\n            prefixSum[i+1] = prefixSum[i]\
        \ + v[i]\n            pow10[i+1] = (pow10[i] * 10) % MOD\n\n        ans = [0]\
        \ * len(queries)\n        for i in xrange(len(queries)):\n            l, r =\
        \ queries[i]\n            L, R = first_idx[l], last_idx[r]\n            if L\
        \ > R:\n                ans[i] = 0\n            else:\n                x = (P[R+1]\
        \ - P[L] * pow10[R-L+1]) % MOD\n                s_val = prefixSum[R+1] - prefixSum[L]\n\
        \                ans[i] = (x * s_val) % MOD\n        return ans"
      python3: "class Solution:\n    def sumAndMultiply(self, s: str, queries: List[List[int]])\
        \ -> List[int]:\n        MOD = 1000000007\n        m = len(s)\n        v = [ord(c)\
        \ - 48 for c in s if c != '0']\n        v_orig_idx = [i for i, c in enumerate(s)\
        \ if c != '0']\n        v_size = len(v)\n\n        first_idx = [0] * m\n   \
        \     v_ptr = 0\n        for i in range(m):\n            while v_ptr < v_size\
        \ and v_orig_idx[v_ptr] < i:\n                v_ptr += 1\n            first_idx[i]\
        \ = v_ptr\n\n        last_idx = [0] * m\n        curr_last = -1\n        for\
        \ i in range(m):\n            if s[i] != '0':\n                curr_last +=\
        \ 1\n            last_idx[i] = curr_last\n\n        P = [0] * (v_size + 1)\n\
        \        prefixSum = [0] * (v_size + 1)\n        pow10 = [1] * (v_size + 1)\n\
        \        for i in range(v_size):\n            P[i+1] = (P[i] * 10 + v[i]) %\
        \ MOD\n            prefixSum[i+1] = prefixSum[i] + v[i]\n            pow10[i+1]\
        \ = (pow10[i] * 10) % MOD\n\n        ans = [0] * len(queries)\n        for i\
        \ in range(len(queries)):\n            l, r = queries[i]\n            L, R =\
        \ first_idx[l], last_idx[r]\n            if L > R:\n                ans[i] =\
        \ 0\n            else:\n                x = (P[R+1] - P[L] * pow10[R-L+1]) %\
        \ MOD\n                s_val = prefixSum[R+1] - prefixSum[L]\n             \
        \   ans[i] = (x * s_val) % MOD\n        return ans"
      c: "#include <stdlib.h>\n#include <string.h>\n\n/**\n * Note: The returned array\
        \ must be malloced, assume caller calls free().\n */\nint* sumAndMultiply(char*\
        \ s, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {\n\
        \    int m = strlen(s);\n    int* v = (int*)malloc(sizeof(int) * m);\n    int*\
        \ v_orig_idx = (int*)malloc(sizeof(int) * m);\n    int v_size = 0;\n    int*\
        \ last_idx = (int*)malloc(sizeof(int) * m);\n    int curr_last = -1;\n    for\
        \ (int i = 0; i < m; i++) {\n        if (s[i] != '0') {\n            v[v_size]\
        \ = s[i] - '0';\n            v_orig_idx[v_size] = i;\n            v_size++;\n\
        \            curr_last++;\n        }\n        last_idx[i] = curr_last;\n   \
        \ }\n\n    int* first_idx = (int*)malloc(sizeof(int) * m);\n    int v_ptr =\
        \ 0;\n    for (int i = 0; i < m; i++) {\n        while (v_ptr < v_size && v_orig_idx[v_ptr]\
        \ < i) v_ptr++;\n        first_idx[i] = v_ptr;\n    }\n\n    long long mod =\
        \ 1000000007;\n    long long* P = (long long*)malloc(sizeof(long long) * (v_size\
        \ + 1));\n    long long* prefixSum = (long long*)malloc(sizeof(long long) *\
        \ (v_size + 1));\n    long long* pow10 = (long long*)malloc(sizeof(long long)\
        \ * (v_size + 1));\n    P[0] = 0;\n    prefixSum[0] = 0;\n    pow10[0] = 1;\n\
        \    for (int i = 0; i < v_size; i++) {\n        P[i + 1] = (P[i] * 10 + v[i])\
        \ % mod;\n        prefixSum[i + 1] = prefixSum[i] + v[i];\n        pow10[i +\
        \ 1] = (pow10[i] * 10) % mod;\n    }\n\n    int* ans = (int*)malloc(sizeof(int)\
        \ * queriesSize);\n    *returnSize = queriesSize;\n    for (int i = 0; i < queriesSize;\
        \ i++) {\n        int l = queries[i][0];\n        int r = queries[i][1];\n \
        \       int L = first_idx[l];\n        int R = last_idx[r];\n        if (L >\
        \ R) {\n            ans[i] = 0;\n        } else {\n            long long x =\
        \ (P[R + 1] - (P[L] * pow10[R - L + 1]) % mod + mod) % mod;\n            long\
        \ long s_val = prefixSum[R + 1] - prefixSum[L];\n            ans[i] = (int)((x\
        \ * (s_val % mod)) % mod);\n        }\n    }\n\n    free(v); free(v_orig_idx);\
        \ free(last_idx); free(first_idx); free(P); free(prefixSum); free(pow10);\n\
        \    return ans;\n}"
      csharp: "public class Solution {\n    public int[] SumAndMultiply(string s, int[][]\
        \ queries) {\n        int m = s.Length;\n        long MOD = 1000000007L;\n \
        \       System.Collections.Generic.List<int> nzVals = new System.Collections.Generic.List<int>();\n\
        \        System.Collections.Generic.List<int> nzPos = new System.Collections.Generic.List<int>();\n\
        \n        for (int k = 0; k < m; k++) {\n            if (s[k] != '0') {\n  \
        \              nzVals.Add(s[k] - '0');\n                nzPos.Add(k);\n    \
        \        }\n        }\n\n        int nzCount = nzVals.Count;\n        long[]\
        \ P_sum = new long[nzCount + 1];\n        long[] P_concat = new long[nzCount\
        \ + 1];\n        long[] pow10 = new long[nzCount + 1];\n        pow10[0] = 1;\n\
        \n        for (int i = 0; i < nzCount; i++) {\n            P_sum[i + 1] = P_sum[i]\
        \ + nzVals[i];\n            P_concat[i + 1] = (P_concat[i] * 10 + nzVals[i])\
        \ % MOD;\n            pow10[i + 1] = (pow10[i] * 10) % MOD;\n        }\n\n \
        \       int[] nextIdx = new int[m];\n        int ptr = 0;\n        for (int\
        \ i = 0; i < m; i++) {\n            while (ptr < nzCount && nzPos[ptr] < i)\
        \ ptr++;\n            nextIdx[i] = ptr;\n        }\n\n        int[] prevIdx\
        \ = new int[m];\n        ptr = nzCount - 1;\n        for (int i = m - 1; i >=\
        \ 0; i--) {\n            while (ptr >= 0 && nzPos[ptr] > i) ptr--;\n       \
        \     prevIdx[i] = ptr;\n        }\n\n        int[] results = new int[queries.Length];\n\
        \        for (int q = 0; q < queries.Length; q++) {\n            int l = queries[q][0];\n\
        \            int r = queries[q][1];\n            int iIdx = nextIdx[l];\n  \
        \          int jIdx = prevIdx[r];\n\n            if (iIdx > jIdx) {\n      \
        \          results[q] = 0;\n            } else {\n                int numElements\
        \ = jIdx - iIdx + 1;\n                long x = (P_concat[jIdx + 1] - (P_concat[iIdx]\
        \ * pow10[numElements]) % MOD + MOD) % MOD;\n                long sVal = P_sum[jIdx\
        \ + 1] - P_sum[iIdx];\n                results[q] = (int)((x * (sVal % MOD))\
        \ % MOD);\n            }\n        }\n\n        return results;\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @param {number[][]} queries\n * @return\
        \ {number[]}\n */\nvar sumAndMultiply = function(s, queries) {\n    const m\
        \ = s.length;\n    const MOD = 1000000007n;\n    const nzVals = [];\n    const\
        \ nzPos = [];\n    for (let k = 0; k < m; k++) {\n        if (s[k] !== '0')\
        \ {\n            nzVals.push(Number(s[k]));\n            nzPos.push(k);\n  \
        \      }\n    }\n\n    const nzCount = nzVals.length;\n    const P_sum = new\
        \ BigInt64Array(nzCount + 1);\n    const P_concat = new BigInt64Array(nzCount\
        \ + 1);\n    const pow10 = new BigInt64Array(nzCount + 1);\n    pow10[0] = 1n;\n\
        \n    for (let i = 0; i < nzCount; i++) {\n        P_sum[i + 1] = P_sum[i] +\
        \ BigInt(nzVals[i]);\n        P_concat[i + 1] = (P_concat[i] * 10n + BigInt(nzVals[i]))\
        \ % MOD;\n        pow10[i + 1] = (pow10[i] * 10n) % MOD;\n    }\n\n    const\
        \ nextIdx = new Int32Array(m);\n    let ptr = 0;\n    for (let i = 0; i < m;\
        \ i++) {\n        while (ptr < nzCount && nzPos[ptr] < i) ptr++;\n        nextIdx[i]\
        \ = ptr;\n    }\n\n    const prevIdx = new Int32Array(m);\n    ptr = nzCount\
        \ - 1;\n    for (let i = m - 1; i >= 0; i--) {\n        while (ptr >= 0 && nzPos[ptr]\
        \ > i) ptr--;\n        prevIdx[i] = ptr;\n    }\n\n    const results = [];\n\
        \    for (let q = 0; q < queries.length; q++) {\n        const l = queries[q][0];\n\
        \        const r = queries[q][1];\n        const iIdx = nextIdx[l];\n      \
        \  const jIdx = prevIdx[r];\n\n        if (iIdx > jIdx) {\n            results.push(0);\n\
        \        } else {\n            const numElements = jIdx - iIdx + 1;\n      \
        \      const x = (P_concat[jIdx + 1] - (P_concat[iIdx] * pow10[numElements])\
        \ % MOD + MOD) % MOD;\n            const sVal = P_sum[jIdx + 1] - P_sum[iIdx];\n\
        \            results.push(Number((x * (sVal % MOD)) % MOD));\n        }\n  \
        \  }\n\n    return results;\n};"
      typescript: "function sumAndMultiply(s: string, queries: number[][]): number[]\
        \ {\n    const m = s.length;\n    const MOD = 1000000007n;\n    const nzVals:\
        \ number[] = [];\n    const nzPos: number[] = [];\n    for (let k = 0; k < m;\
        \ k++) {\n        if (s[k] !== '0') {\n            nzVals.push(Number(s[k]));\n\
        \            nzPos.push(k);\n        }\n    }\n\n    const nzCount = nzVals.length;\n\
        \    const P_sum = new BigInt64Array(nzCount + 1);\n    const P_concat = new\
        \ BigInt64Array(nzCount + 1);\n    const pow10 = new BigInt64Array(nzCount +\
        \ 1);\n    pow10[0] = 1n;\n\n    for (let i = 0; i < nzCount; i++) {\n     \
        \   P_sum[i + 1] = P_sum[i] + BigInt(nzVals[i]);\n        P_concat[i + 1] =\
        \ (P_concat[i] * 10n + BigInt(nzVals[i])) % MOD;\n        pow10[i + 1] = (pow10[i]\
        \ * 10n) % MOD;\n    }\n\n    const nextIdx = new Int32Array(m);\n    let ptr\
        \ = 0;\n    for (let i = 0; i < m; i++) {\n        while (ptr < nzCount && nzPos[ptr]\
        \ < i) ptr++;\n        nextIdx[i] = ptr;\n    }\n\n    const prevIdx = new Int32Array(m);\n\
        \    ptr = nzCount - 1;\n    for (let i = m - 1; i >= 0; i--) {\n        while\
        \ (ptr >= 0 && nzPos[ptr] > i) ptr--;\n        prevIdx[i] = ptr;\n    }\n\n\
        \    const results: number[] = [];\n    for (let q = 0; q < queries.length;\
        \ q++) {\n        const l = queries[q][0];\n        const r = queries[q][1];\n\
        \        const iIdx = nextIdx[l];\n        const jIdx = prevIdx[r];\n\n    \
        \    if (iIdx > jIdx) {\n            results.push(0);\n        } else {\n  \
        \          const numElements = jIdx - iIdx + 1;\n            const x = (P_concat[jIdx\
        \ + 1] - (P_concat[iIdx] * pow10[numElements]) % MOD + MOD) % MOD;\n       \
        \     const sVal = P_sum[jIdx + 1] - P_sum[iIdx];\n            results.push(Number((x\
        \ * (sVal % MOD)) % MOD));\n        }\n    }\n\n    return results;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @param Integer[][]\
        \ $queries\n     * @return Integer[]\n     */\n    function sumAndMultiply($s,\
        \ $queries) {\n        $m = strlen($s);\n        $MOD = 1000000007;\n      \
        \  $nz_vals = [];\n        $nz_pos = [];\n        for ($k = 0; $k < $m; $k++)\
        \ {\n            if ($s[$k] !== '0') {\n                $nz_vals[] = (int)$s[$k];\n\
        \                $nz_pos[] = $k;\n            }\n        }\n\n        $nz_count\
        \ = count($nz_vals);\n        $P_sum = array_fill(0, $nz_count + 1, 0);\n  \
        \      $P_concat = array_fill(0, $nz_count + 1, 0);\n        $pow10 = array_fill(0,\
        \ $nz_count + 1, 0);\n        $pow10[0] = 1;\n\n        for ($i = 0; $i < $nz_count;\
        \ $i++) {\n            $P_sum[$i + 1] = $P_sum[$i] + $nz_vals[$i];\n       \
        \     $P_concat[$i + 1] = ($P_concat[$i] * 10 + $nz_vals[$i]) % $MOD;\n    \
        \        $pow10[$i + 1] = ($pow10[$i] * 10) % $MOD;\n        }\n\n        $next_idx\
        \ = array_fill(0, $m, 0);\n        $ptr = 0;\n        for ($i = 0; $i < $m;\
        \ $i++) {\n            while ($ptr < $nz_count && $nz_pos[$ptr] < $i) $ptr++;\n\
        \            $next_idx[$i] = $ptr;\n        }\n\n        $prev_idx = array_fill(0,\
        \ $m, -1);\n        $ptr = $nz_count - 1;\n        for ($i = $m - 1; $i >= 0;\
        \ $i--) {\n            while ($ptr >= 0 && $nz_pos[$ptr] > $i) $ptr--;\n   \
        \         $prev_idx[$i] = $ptr;\n        }\n\n        $results = [];\n     \
        \   foreach ($queries as $query) {\n            $l = $query[0];\n          \
        \  $r = $query[1];\n            $iIdx = $next_idx[$l];\n            $jIdx =\
        \ $prev_idx[$r];\n\n            if ($iIdx > $jIdx) {\n                $results[]\
        \ = 0;\n            } else {\n                $num_elements = $jIdx - $iIdx\
        \ + 1;\n                $x = ($P_concat[$jIdx + 1] - ($P_concat[$iIdx] * $pow10[$num_elements])\
        \ % $MOD + $MOD) % $MOD;\n                $s_val = $P_sum[$jIdx + 1] - $P_sum[$iIdx];\n\
        \                $results[] = (int)(($x * ($s_val % $MOD)) % $MOD);\n      \
        \      }\n        }\n\n        return $results;\n    }\n}"
      swift: "class Solution {\n    func sumAndMultiply(_ s: String, _ queries: [[Int]])\
        \ -> [Int] {\n        let sBytes = [UInt8](s.utf8)\n        let m = sBytes.count\n\
        \        let MOD: Int64 = 1000000007\n\n        var nzVals: [Int] = []\n   \
        \     var nzPos: [Int] = []\n        for k in 0..<m {\n            if sBytes[k]\
        \ != 48 {\n                nzVals.append(Int(sBytes[k] - 48))\n            \
        \    nzPos.append(k)\n            }\n        }\n\n        let nzCount = nzVals.count\n\
        \        var P_sum = [Int64](repeating: 0, count: nzCount + 1)\n        var\
        \ P_concat = [Int64](repeating: 0, count: nzCount + 1)\n        var pow10 =\
        \ [Int64](repeating: 0, count: nzCount + 1)\n        pow10[0] = 1\n\n      \
        \  for i in 0..<nzCount {\n            P_sum[i + 1] = P_sum[i] + Int64(nzVals[i])\n\
        \            P_concat[i + 1] = (P_concat[i] * 10 + Int64(nzVals[i])) % MOD\n\
        \            pow10[i + 1] = (pow10[i] * 10) % MOD\n        }\n\n        var\
        \ nextIdx = [Int](repeating: 0, count: m)\n        var ptr = 0\n        for\
        \ i in 0..<m {\n            while ptr < nzCount && nzPos[ptr] < i {\n      \
        \          ptr += 1\n            }\n            nextIdx[i] = ptr\n        }\n\
        \n        var prevIdx = [Int](repeating: -1, count: m)\n        ptr = nzCount\
        \ - 1\n        for i in (0..<m).reversed() {\n            while ptr >= 0 &&\
        \ nzPos[ptr] > i {\n                ptr -= 1\n            }\n            prevIdx[i]\
        \ = ptr\n        }\n\n        var results: [Int] = []\n        for query in\
        \ queries {\n            let l = query[0]\n            let r = query[1]\n  \
        \          let iIdx = nextIdx[l]\n            let jIdx = prevIdx[r]\n\n    \
        \        if iIdx > jIdx {\n                results.append(0)\n            }\
        \ else {\n                let numElements = jIdx - iIdx + 1\n              \
        \  let x = (P_concat[jIdx + 1] - (P_concat[iIdx] * pow10[numElements]) % MOD\
        \ + MOD) % MOD\n                let sVal = P_sum[jIdx + 1] - P_sum[iIdx]\n \
        \               results.append(Int((x * (sVal % MOD)) % MOD))\n            }\n\
        \        }\n\n        return results\n    }\n}"
      kotlin: "class Solution {\n    fun sumAndMultiply(s: String, queries: Array<IntArray>):\
        \ IntArray {\n        val m = s.length\n        val mod = 1000000007L\n\n  \
        \      val nzDigits = mutableListOf<Int>()\n        for (i in 0 until m) {\n\
        \            val digit = s[i] - '0'\n            if (digit != 0) {\n       \
        \         nzDigits.add(digit)\n            }\n        }\n\n        val n = nzDigits.size\n\
        \        val prefixSum = LongArray(n + 1)\n        val prefixVal = LongArray(n\
        \ + 1)\n        val pow10 = LongArray(n + 1)\n        pow10[0] = 1\n       \
        \ for (i in 0 until n) {\n            prefixSum[i + 1] = prefixSum[i] + nzDigits[i]\n\
        \            prefixVal[i + 1] = (prefixVal[i] * 10 + nzDigits[i]) % mod\n  \
        \          pow10[i + 1] = (pow10[i] * 10) % mod\n        }\n\n        val nextNz\
        \ = IntArray(m) { -1 }\n        var firstNzIdx = n\n        for (i in m - 1\
        \ downTo 0) {\n            if (s[i] != '0') {\n                firstNzIdx--\n\
        \            }\n            if (firstNzIdx < n) {\n                nextNz[i]\
        \ = firstNzIdx\n            }\n        }\n\n        val prevNz = IntArray(m)\
        \ { -1 }\n        var lastNzIdx = -1\n        for (i in 0 until m) {\n     \
        \       if (s[i] != '0') {\n                lastNzIdx++\n            }\n   \
        \         prevNz[i] = lastNzIdx\n        }\n\n        val result = IntArray(queries.size)\n\
        \        for (i in queries.indices) {\n            val l = queries[i][0]\n \
        \           val r = queries[i][1]\n            val first = nextNz[l]\n     \
        \       val last = prevNz[r]\n\n            if (first == -1 || last == -1 ||\
        \ first > last) {\n                result[i] = 0\n            } else {\n   \
        \             val numElements = last - first + 1\n                val x = (prefixVal[last\
        \ + 1] - (prefixVal[first] * pow10[numElements]) % mod + mod) % mod\n      \
        \          val sum = (prefixSum[last + 1] - prefixSum[first]) % mod\n      \
        \          result[i] = ((x * sum) % mod).toInt()\n            }\n        }\n\
        \        return result\n    }\n}"
      dart: "class Solution {\n  List<int> sumAndMultiply(String s, List<List<int>>\
        \ queries) {\n    int m = s.length;\n    int mod = 1000000007;\n\n    List<int>\
        \ nzDigits = [];\n    for (int i = 0; i < m; i++) {\n      int digit = s.codeUnitAt(i)\
        \ - 48;\n      if (digit != 0) {\n        nzDigits.add(digit);\n      }\n  \
        \  }\n\n    int n = nzDigits.length;\n    List<int> prefixSum = List<int>.filled(n\
        \ + 1, 0);\n    List<int> prefixVal = List<int>.filled(n + 1, 0);\n    List<int>\
        \ pow10 = List<int>.filled(n + 1, 0);\n    pow10[0] = 1;\n    for (int i = 0;\
        \ i < n; i++) {\n      prefixSum[i + 1] = prefixSum[i] + nzDigits[i];\n    \
        \  prefixVal[i + 1] = (prefixVal[i] * 10 + nzDigits[i]) % mod;\n      pow10[i\
        \ + 1] = (pow10[i] * 10) % mod;\n    }\n\n    List<int> nextNz = List<int>.filled(m,\
        \ -1);\n    int firstNzIdx = n;\n    for (int i = m - 1; i >= 0; i--) {\n  \
        \    if (s.codeUnitAt(i) != 48) {\n        firstNzIdx--;\n      }\n      if\
        \ (firstNzIdx < n) {\n        nextNz[i] = firstNzIdx;\n      }\n    }\n\n  \
        \  List<int> prevNz = List<int>.filled(m, -1);\n    int lastNzIdx = -1;\n  \
        \  for (int i = 0; i < m; i++) {\n      if (s.codeUnitAt(i) != 48) {\n     \
        \   lastNzIdx++;\n      }\n      prevNz[i] = lastNzIdx;\n    }\n\n    List<int>\
        \ result = List<int>.filled(queries.length, 0);\n    for (int i = 0; i < queries.length;\
        \ i++) {\n      int l = queries[i][0];\n      int r = queries[i][1];\n     \
        \ int first = nextNz[l];\n      int last = prevNz[r];\n\n      if (first ==\
        \ -1 || last == -1 || first > last) {\n        result[i] = 0;\n      } else\
        \ {\n        int numElements = last - first + 1;\n        int x = (prefixVal[last\
        \ + 1] - (prefixVal[first] * pow10[numElements]) % mod + mod) % mod;\n     \
        \   int sum = (prefixSum[last + 1] - prefixSum[first]) % mod;\n        result[i]\
        \ = (x * sum) % mod;\n      }\n    }\n    return result;\n  }\n}"
      go: "func sumAndMultiply(s string, queries [][]int) []int {\n\tm := len(s)\n\t\
        mod := int64(1000000007)\n\n\tnzDigits := make([]int, 0, m)\n\tfor i := 0; i\
        \ < m; i++ {\n\t\tdigit := int(s[i] - '0')\n\t\tif digit != 0 {\n\t\t\tnzDigits\
        \ = append(nzDigits, digit)\n\t\t}\n\t}\n\n\tn := len(nzDigits)\n\tprefixSum\
        \ := make([]int64, n+1)\n\tprefixVal := make([]int64, n+1)\n\tpow10 := make([]int64,\
        \ n+1)\n\tpow10[0] = 1\n\tfor i := 0; i < n; i++ {\n\t\tprefixSum[i+1] = prefixSum[i]\
        \ + int64(nzDigits[i])\n\t\tprefixVal[i+1] = (prefixVal[i]*10 + int64(nzDigits[i]))\
        \ % mod\n\t\tpow10[i+1] = (pow10[i] * 10) % mod\n\t}\n\n\tnextNz := make([]int,\
        \ m)\n\tfor i := range nextNz {\n\t\tnextNz[i] = -1\n\t}\n\tfirstNzIdx := n\n\
        \tfor i := m - 1; i >= 0; i-- {\n\t\tif s[i] != '0' {\n\t\t\tfirstNzIdx--\n\t\
        \t}\n\t\tif firstNzIdx < n {\n\t\t\tnextNz[i] = firstNzIdx\n\t\t}\n\t}\n\n\t\
        prevNz := make([]int, m)\n\tfor i := range prevNz {\n\t\tprevNz[i] = -1\n\t\
        }\n\tlastNzIdx := -1\n\tfor i := 0; i < m; i++ {\n\t\tif s[i] != '0' {\n\t\t\
        \tlastNzIdx++\n\t\t}\n\t\tprevNz[i] = lastNzIdx\n\t}\n\n\tresult := make([]int,\
        \ len(queries))\n\tfor i, q := range queries {\n\t\tl, r := q[0], q[1]\n\t\t\
        first := nextNz[l]\n\t\tlast := prevNz[r]\n\n\t\tif first == -1 || last == -1\
        \ || first > last {\n\t\t\tresult[i] = 0\n\t\t} else {\n\t\t\tnumElements :=\
        \ last - first + 1\n\t\t\tx := (prefixVal[last+1] - (prefixVal[first]*pow10[numElements])%mod\
        \ + mod) % mod\n\t\t\tsum := (prefixSum[last+1] - prefixSum[first]) % mod\n\t\
        \t\tresult[i] = int((x * sum) % mod)\n\t\t}\n\t}\n\treturn result\n}"
      ruby: "def sum_and_multiply(s, queries)\n  m = s.length\n  mod = 1000000007\n\n\
        \  nz_digits = []\n  s.each_char do |c|\n    d = c.to_i\n    nz_digits << d\
        \ if d != 0\n  end\n\n  n = nz_digits.length\n  prefix_sum = Array.new(n + 1,\
        \ 0)\n  prefix_val = Array.new(n + 1, 0)\n  pow10 = Array.new(n + 1, 0)\n  pow10[0]\
        \ = 1\n  (0...n).each do |i|\n    prefix_sum[i + 1] = prefix_sum[i] + nz_digits[i]\n\
        \    prefix_val[i + 1] = (prefix_val[i] * 10 + nz_digits[i]) % mod\n    pow10[i\
        \ + 1] = (pow10[i] * 10) % mod\n  end\n\n  next_nz = Array.new(m, -1)\n  first_nz_idx\
        \ = n\n  (m - 1).downto(0) do |i|\n    first_nz_idx -= 1 if s[i] != '0'\n  \
        \  next_nz[i] = first_nz_idx if first_nz_idx < n\n  end\n\n  prev_nz = Array.new(m,\
        \ -1)\n  last_nz_idx = -1\n  (0...m).each do |i|\n    last_nz_idx += 1 if s[i]\
        \ != '0'\n    prev_nz[i] = last_nz_idx\n  end\n\n  queries.map do |l, r|\n \
        \   first = next_nz[l]\n    last = prev_nz[r]\n    if first == -1 || last ==\
        \ -1 || first > last\n      0\n    else\n      num_elements = last - first +\
        \ 1\n      x = (prefix_val[last + 1] - (prefix_val[first] * pow10[num_elements])\
        \ % mod) % mod\n      sum = (prefix_sum[last + 1] - prefix_sum[first]) % mod\n\
        \      (x * sum) % mod\n    end\n  end\nend"
      scala: "object Solution {\n  def sumAndMultiply(s: String, queries: Array[Array[Int]]):\
        \ Array[Int] = {\n    val m = s.length\n    val mod = 1000000007L\n\n    val\
        \ nzDigits = new scala.collection.mutable.ArrayBuffer[Int]()\n    var idx =\
        \ 0\n    while (idx < m) {\n      val d = s(idx) - '0'\n      if (d != 0) {\n\
        \        nzDigits += d\n      }\n      idx += 1\n    }\n\n    val n = nzDigits.length\n\
        \    val prefixSum = new Array[Long](n + 1)\n    val prefixVal = new Array[Long](n\
        \ + 1)\n    val pow10 = new Array[Long](n + 1)\n    pow10(0) = 1\n    for (i\
        \ <- 0 until n) {\n      prefixSum(i + 1) = prefixSum(i) + nzDigits(i)\n   \
        \   prefixVal(i + 1) = (prefixVal(i) * 10 + nzDigits(i)) % mod\n      pow10(i\
        \ + 1) = (pow10(i) * 10) % mod\n    }\n\n    val nextNz = Array.fill(m)(-1)\n\
        \    var firstNzIdx = n\n    for (i <- m - 1 to 0 by -1) {\n      if (s(i) !=\
        \ '0') {\n        firstNzIdx -= 1\n      }\n      if (firstNzIdx < n) {\n  \
        \      nextNz(i) = firstNzIdx\n      }\n    }\n\n    val prevNz = Array.fill(m)(-1)\n\
        \    var lastNzIdx = -1\n    for (i <- 0 until m) {\n      if (s(i) != '0')\
        \ {\n        lastNzIdx += 1\n      }\n      prevNz(i) = lastNzIdx\n    }\n\n\
        \    val result = new Array[Int](queries.length)\n    for (i <- queries.indices)\
        \ {\n      val l = queries(i)(0)\n      val r = queries(i)(1)\n      val first\
        \ = nextNz(l)\n      val last = prevNz(r)\n\n      if (first == -1 || last ==\
        \ -1 || first > last) {\n        result(i) = 0\n      } else {\n        val\
        \ numElements = last - first + 1\n        val x = (prefixVal(last + 1) - (prefixVal(first)\
        \ * pow10(numElements)) % mod + mod) % mod\n        val sum = (prefixSum(last\
        \ + 1) - prefixSum(first)) % mod\n        result(i) = ((x * sum) % mod).toInt\n\
        \      }\n    }\n    result\n  }\n}"
      rust: "impl Solution {\n    pub fn sum_and_multiply(s: String, queries: Vec<Vec<i32>>)\
        \ -> Vec<i32> {\n        let n = s.len();\n        let s_bytes = s.as_bytes();\n\
        \        let mut nz = Vec::new();\n        let mut nz_idx = Vec::new();\n  \
        \      for (i, &b) in s_bytes.iter().enumerate() {\n            if b != b'0'\
        \ {\n                nz.push((b - b'0') as i64);\n                nz_idx.push(i);\n\
        \            }\n        }\n\n        let nz_len = nz.len();\n        let mut\
        \ prefix_sum = vec![0i64; nz_len + 1];\n        let mut prefix_concat = vec![0i64;\
        \ nz_len + 1];\n        let mod_val = 1_000_000_007i64;\n        let mut pow10\
        \ = vec![1i64; nz_len + 1];\n\n        for i in 0..nz_len {\n            prefix_sum[i\
        \ + 1] = prefix_sum[i] + nz[i];\n            prefix_concat[i + 1] = (prefix_concat[i]\
        \ * 10 + nz[i]) % mod_val;\n            pow10[i + 1] = (pow10[i] * 10) % mod_val;\n\
        \        }\n\n        let mut first_nz = vec![nz_len as i32; n];\n        let\
        \ mut last_nz = vec![-1i32; n];\n\n        let mut cur = 0;\n        for i in\
        \ 0..n {\n            while cur < nz_len && nz_idx[cur] < i {\n            \
        \    cur += 1;\n            }\n            if cur < nz_len {\n             \
        \   first_nz[i] = cur as i32;\n            }\n        }\n\n        let mut cur\
        \ = (nz_len as i32) - 1;\n        for i in (0..n).rev() {\n            while\
        \ cur >= 0 && nz_idx[cur as usize] > i {\n                cur -= 1;\n      \
        \      }\n            if cur >= 0 {\n                last_nz[i] = cur;\n   \
        \         }\n        }\n\n        queries.into_iter().map(|q| {\n          \
        \  let l = q[0] as usize;\n            let r = q[1] as usize;\n            let\
        \ i = first_nz[l];\n            let j = last_nz[r];\n            if i > j ||\
        \ i == nz_len as i32 || j == -1 {\n                0\n            } else {\n\
        \                let i_u = i as usize;\n                let j_u = j as usize;\n\
        \                let sum = prefix_sum[j_u + 1] - prefix_sum[i_u];\n        \
        \        let x = (prefix_concat[j_u + 1] - (prefix_concat[i_u] * pow10[j_u -\
        \ i_u + 1]) % mod_val + mod_val) % mod_val;\n                ((x * (sum % mod_val))\
        \ % mod_val) as i32\n            }\n        }).collect()\n    }\n}"
      racket: "(define/contract (sum-and-multiply s queries)\n  (-> string? (listof\
        \ (listof exact-integer?)) (listof exact-integer?))\n  (let* ([n (string-length\
        \ s)]\n         [mod 1000000007]\n         [nz-data (let loop ([i 0] [nz '()]\
        \ [nz-idx '()])\n                    (if (= i n)\n                        (list\
        \ (reverse nz) (reverse nz-idx))\n                        (let ([digit (- (char->integer\
        \ (string-ref s i)) 48)])\n                          (if (zero? digit)\n   \
        \                           (loop (+ i 1) nz nz-idx)\n                     \
        \         (loop (+ i 1) (cons digit nz) (cons i nz-idx))))))]\n         [nz\
        \ (list->vector (car nz-data))]\n         [nz-idx (list->vector (cadr nz-data))]\n\
        \         [nz-len (vector-length nz)]\n         [prefix-sum (make-vector (+\
        \ nz-len 1) 0)]\n         [prefix-concat (make-vector (+ nz-len 1) 0)]\n   \
        \      [pow10 (make-vector (+ nz-len 1) 1)]\n         [first-nz (make-vector\
        \ n nz-len)]\n         [last-nz (make-vector n -1)])\n    (for ([i (in-range\
        \ nz-len)])\n      (let ([digit (vector-ref nz i)])\n        (vector-set! prefix-sum\
        \ (+ i 1) (+ (vector-ref prefix-sum i) digit))\n        (vector-set! prefix-concat\
        \ (+ i 1) (modulo (+ (* (vector-ref prefix-concat i) 10) digit) mod))\n    \
        \    (vector-set! pow10 (+ i 1) (modulo (* (vector-ref pow10 i) 10) mod))))\n\
        \    (let loop ([i 0] [cur 0])\n      (when (< i n)\n        (let ([next-cur\
        \ (let loop2 ([cur cur])\n                          (if (and (< cur nz-len)\
        \ (< (vector-ref nz-idx cur) i))\n                              (loop2 (+ cur\
        \ 1))\n                              cur))])\n          (when (< next-cur nz-len)\n\
        \            (vector-set! first-nz i next-cur))\n          (loop (+ i 1) next-cur))))\n\
        \    (let loop ([i (- n 1)] [cur (- nz-len 1)])\n      (when (>= i 0)\n    \
        \    (let ([next-cur (let loop2 ([cur cur])\n                          (if (and\
        \ (>= cur 0) (> (vector-ref nz-idx cur) i))\n                              (loop2\
        \ (- cur 1))\n                              cur))])\n          (when (>= next-cur\
        \ 0)\n            (vector-set! last-nz i next-cur))\n          (loop (- i 1)\
        \ next-cur))))\n    (map (lambda (q)\n           (let* ([l (car q)]\n      \
        \            [r (cadr q)]\n                  [i (vector-ref first-nz l)]\n \
        \                 [j (vector-ref last-nz r)])\n             (if (or (> i j)\
        \ (= i nz-len) (= j -1))\n                 0\n                 (let* ([sum-val\
        \ (- (vector-ref prefix-sum (+ j 1)) (vector-ref prefix-sum i))]\n         \
        \               [p-j1 (vector-ref prefix-concat (+ j 1))]\n                \
        \        [p-i (vector-ref prefix-concat i)]\n                        [pw (vector-ref\
        \ pow10 (+ (- j i) 1))]\n                        [x (modulo (- p-j1 (modulo\
        \ (* p-i pw) mod)) mod)])\n                   (modulo (* x (modulo sum-val mod))\
        \ mod)))))\n         queries)))"
      erlang: "-spec sum_and_multiply(S :: unicode:unicode_binary(), Queries :: [[integer()]])\
        \ -> [integer()].\nsum_and_multiply(S, Queries) ->\n    N = byte_size(S),\n\
        \    Mod = 1000000007,\n    SList = binary_to_list(S),\n    {NZList, NZIdxList,\
        \ _} = lists:foldl(\n        fun(C, {AccNZ, AccIdx, I}) ->\n            D =\
        \ C - $0,\n            if D /= 0 -> {[D | AccNZ], [I | AccIdx], I + 1};\n  \
        \             true -> {AccNZ, AccIdx, I + 1}\n            end\n        end,\n\
        \        {[], [], 0},\n        SList\n    ),\n    NZ = list_to_tuple(lists:reverse(NZList)),\n\
        \    NZIdx = list_to_tuple(lists:reverse(NZIdxList)),\n    NZLen = tuple_size(NZ),\n\
        \    PrefixSum = list_to_tuple(lists:reverse(lists:foldl(\n        fun(I, [H\
        \ | _] = Acc) -> [(H + element(I, NZ)) | Acc] end,\n        [0],\n        lists:seq(1,\
        \ NZLen)\n    ))),\n    PrefixConcat = list_to_tuple(lists:reverse(lists:foldl(\n\
        \        fun(I, [H | _] = Acc) -> [(H * 10 + element(I, NZ)) rem Mod | Acc]\
        \ end,\n        [0],\n        lists:seq(1, NZLen)\n    ))),\n    Pow10 = list_to_tuple(lists:reverse(lists:foldl(\n\
        \        fun(_, [H | _] = Acc) -> [(H * 10) rem Mod | Acc] end,\n        [1],\n\
        \        lists:seq(1, NZLen)\n    ))),\n    FirstNZ = build_first_nz(N, NZIdx,\
        \ NZLen),\n    LastNZ = build_last_nz(N, NZIdx, NZLen),\n    [get_query_ans(Q,\
        \ FirstNZ, LastNZ, PrefixSum, PrefixConcat, Pow10, NZLen, Mod) || Q <- Queries].\n\
        \nbuild_first_nz(N, NZIdx, NZLen) ->\n    {_, FirstNZList} = lists:foldl(\n\
        \        fun(I, {Cur, Acc}) ->\n            NewCur = find_first_idx(I, Cur,\
        \ NZIdx, NZLen),\n            {NewCur, [NewCur | Acc]}\n        end,\n     \
        \   {1, []},\n        lists:seq(0, N - 1)\n    ),\n    list_to_tuple(lists:reverse(FirstNZList)).\n\
        \nfind_first_idx(I, Cur, NZIdx, NZLen) ->\n    if Cur =< NZLen ->\n        if\
        \ element(Cur, NZIdx) < I -> find_first_idx(I, Cur + 1, NZIdx, NZLen);\n   \
        \        true -> Cur\n        end;\n       true -> NZLen + 1\n    end.\n\nbuild_last_nz(N,\
        \ NZIdx, NZLen) ->\n    {_, LastNZList} = lists:foldl(\n        fun(I, {Cur,\
        \ Acc}) ->\n            NewCur = find_last_idx(I, Cur, NZIdx),\n           \
        \ {NewCur, [NewCur | Acc]}\n        end,\n        {NZLen, []},\n        lists:seq(N\
        \ - 1, 0, -1)\n    ),\n    list_to_tuple(LastNZList).\n\nfind_last_idx(I, Cur,\
        \ NZIdx) ->\n    if Cur >= 1 ->\n        if element(Cur, NZIdx) > I -> find_last_idx(I,\
        \ Cur - 1, NZIdx);\n           true -> Cur\n        end;\n       true -> 0\n\
        \    end.\n\nget_query_ans([L, R], FirstNZ, LastNZ, PrefixSum, PrefixConcat,\
        \ Pow10, NZLen, Mod) ->\n    I = element(L + 1, FirstNZ),\n    J = element(R\
        \ + 1, LastNZ),\n    if I > J orelse I > NZLen orelse J < 1 -> 0;\n       true\
        \ ->\n           Sum = element(J + 1, PrefixSum) - element(I, PrefixSum),\n\
        \           PJ1 = element(J + 1, PrefixConcat),\n           PI = element(I,\
        \ PrefixConcat),\n           PW = element(J - I + 2, Pow10),\n           X =\
        \ (PJ1 - (PI * PW) rem Mod + Mod) rem Mod,\n           (X * (Sum rem Mod)) rem\
        \ Mod\n    end."
      elixir: "defmodule Solution do\n  @spec sum_and_multiply(s :: String.t, queries\
        \ :: [[integer]]) :: [integer]\n  def sum_and_multiply(s, queries) do\n    n\
        \ = String.length(s)\n    mod = 1_000_000_007\n    chars = String.to_charlist(s)\n\
        \n    {nz_list, nz_idx_list} = Enum.reduce(Enum.with_index(chars), {[], []},\
        \ fn {char, idx}, {acc_nz, acc_idx} ->\n      digit = char - ?0\n      if digit\
        \ != 0 do\n        {[digit | acc_nz], [idx | acc_idx]}\n      else\n       \
        \ {acc_nz, acc_idx}\n      end\n    end)\n\n    nz = nz_list |> Enum.reverse()\
        \ |> List.to_tuple()\n    nz_idx = nz_idx_list |> Enum.reverse() |> List.to_tuple()\n\
        \    nz_len = tuple_size(nz)\n\n    prefix_sum = if nz_len > 0 do\n      Enum.reduce(1..nz_len,\
        \ [0], fn i, acc ->\n        [hd(acc) + elem(nz, i - 1) | acc]\n      end) |>\
        \ Enum.reverse() |> List.to_tuple()\n    else\n      {0}\n    end\n\n    prefix_concat\
        \ = if nz_len > 0 do\n      Enum.reduce(1..nz_len, [0], fn i, acc ->\n     \
        \   [(hd(acc) * 10 + elem(nz, i - 1)) |> rem(mod) | acc]\n      end) |> Enum.reverse()\
        \ |> List.to_tuple()\n    else\n      {0}\n    end\n\n    pow10 = if nz_len\
        \ > 0 do\n      Enum.reduce(1..nz_len, [1], fn _i, acc ->\n        [(hd(acc)\
        \ * 10) |> rem(mod) | acc]\n      end) |> Enum.reverse() |> List.to_tuple()\n\
        \    else\n      {1}\n    end\n\n    first_nz = build_first_nz(n, nz_idx, nz_len)\n\
        \    last_nz = build_last_nz(n, nz_idx, nz_len)\n\n    Enum.map(queries, fn\
        \ [l, r] ->\n      i = elem(first_nz, l)\n      j = elem(last_nz, r)\n     \
        \ if i > j or i >= nz_len or j < 0 do\n        0\n      else\n        sum_val\
        \ = elem(prefix_sum, j + 1) - elem(prefix_sum, i)\n        p_j1 = elem(prefix_concat,\
        \ j + 1)\n        p_i = elem(prefix_concat, i)\n        pw = elem(pow10, j -\
        \ i + 1)\n        x = Integer.mod(p_j1 - Integer.mod(p_i * pw, mod), mod)\n\
        \        Integer.mod(x * Integer.mod(sum_val, mod), mod)\n      end\n    end)\n\
        \  end\n\n  defp build_first_nz(n, nz_idx, nz_len) do\n    {_final_cur, first_nz_list}\
        \ = Enum.reduce(0..(n - 1), {0, []}, fn i, {cur, acc} ->\n      new_cur = find_first(i,\
        \ cur, nz_idx, nz_len)\n      {new_cur, [new_cur | acc]}\n    end)\n    first_nz_list\
        \ |> Enum.reverse() |> List.to_tuple()\n  end\n\n  defp find_first(i, cur, nz_idx,\
        \ nz_len) do\n    if cur < nz_len and elem(nz_idx, cur) < i do\n      find_first(i,\
        \ cur + 1, nz_idx, nz_len)\n    else\n      cur\n    end\n  end\n\n  defp build_last_nz(n,\
        \ nz_idx, nz_len) do\n    {_final_cur, last_nz_list} = Enum.reduce((n - 1)..0,\
        \ {nz_len - 1, []}, fn i, {cur, acc} ->\n      new_cur = find_last(i, cur, nz_idx)\n\
        \      {new_cur, [new_cur | acc]}\n    end)\n    last_nz_list |> List.to_tuple()\n\
        \  end\n\n  defp find_last(i, cur, nz_idx) do\n    if cur >= 0 and elem(nz_idx,\
        \ cur) > i do\n      find_last(i, cur - 1, nz_idx)\n    else\n      cur\n  \
        \  end\n  end\nend"
    approach: "The algorithm identifies and compresses the string by focusing only on\
      \ non-zero digits. First, we identify all non-zero digits and their original indices\
      \ in $s$, storing them in an auxiliary array $v$. We then precompute three essential\
      \ prefix arrays for $v$: a prefix sum array to calculate the digit sum of any\
      \ compressed substring in $O(1)$, a 'rolling hash' prefix array to calculate the\
      \ numerical value $x$ of any concatenated sequence of non-zero digits modulo $10^9+7$,\
      \ and an array of powers of 10 to assist in the numerical value calculation. \n\
      \nTo handle queries efficiently, we create two mapping arrays, `first_idx` and\
      \ `last_idx`. For each index $i$ in the original string, `first_idx[i]` stores\
      \ the index in $v$ of the first non-zero digit appearing at or after $i$, and\
      \ `last_idx[i]` stores the index in $v$ of the last non-zero digit appearing at\
      \ or before $i$. For any query range $[l, r]$, these arrays allow us to find the\
      \ corresponding range $[L, R]$ in $v$ in $O(1)$. If $L \\le R$, we compute $x\
      \ = (P[R+1] - P[L] \\cdot 10^{R-L+1}) \\pmod{10^9+7}$ and the digit sum from the\
      \ prefix sum array, then return their product modulo $10^9+7$. If $L > R$, the\
      \ range contains only zeros, so the answer is 0."
    time_complexity: O(m + n), where m is the length of string s and n is the number
      of queries. Precomputing the non-zero digits, mappings, and prefix arrays takes
      $O(m)$ time. Each query is processed in $O(1)$ time by performing lookups and
      basic arithmetic operations.
    space_complexity: O(m), as we maintain several arrays (non-zero digits, original
      indices, prefix sums, prefix values, powers of 10, and two mapping arrays) of
      size at most m. The result array for n queries takes $O(n)$ space.
    elapsed_time: 263.04711055755615
    model: gemini-3-flash-preview
    generated_at: '2026-07-08 02:02:28 '
---

## Problem #3756: Concatenate Non-Zero Digits and Multiply by Sum II

**Difficulty:** Medium

**Topics:** Math, String, Prefix Sum

## Problem Description

<p>You are given a string <code>s</code> of length <code>m</code> consisting of digits. You are also given a 2D integer array <code>queries</code>, where <code>queries[i] = [l<sub>i</sub>, r<sub>i</sub>]</code>.</p>

<p>For each <code>queries[i]</code>, extract the <strong><span data-keyword="substring-nonempty">substring</span></strong> <code>s[l<sub>i</sub>..r<sub>i</sub>]</code>. Then, perform the following:</p>

<ul>
	<li>Form a new integer <code>x</code> by concatenating all the <strong>non-zero digits</strong> from the substring in their original order. If there are no non-zero digits, <code>x = 0</code>.</li>
	<li>Let <code>sum</code> be the <strong>sum of digits</strong> in <code>x</code>. The answer is <code>x * sum</code>.</li>
</ul>

<p>Return an array of integers <code>answer</code> where <code>answer[i]</code> is the answer to the <code>i<sup>th</sup></code> query.</p>

<p>Since the answers may be very large, return them <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;10203004&quot;, queries = [[0,7],[1,3],[4,6]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[12340, 4, 9]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li><code>s[0..7] = &quot;10203004&quot;</code>

	<ul>
		<li><code>x = 1234</code></li>
		<li><code>sum = 1 + 2 + 3 + 4 = 10</code></li>
		<li>Therefore, answer is <code>1234 * 10 = 12340</code>.</li>
	</ul>
	</li>
	<li><code>s[1..3] = &quot;020&quot;</code>
	<ul>
		<li><code>x = 2</code></li>
		<li><code>sum = 2</code></li>
		<li>Therefore, the answer is <code>2 * 2 = 4</code>.</li>
	</ul>
	</li>
	<li><code>s[4..6] = &quot;300&quot;</code>
	<ul>
		<li><code>x = 3</code></li>
		<li><code>sum = 3</code></li>
		<li>Therefore, the answer is <code>3 * 3 = 9</code>.</li>
	</ul>
	</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;1000&quot;, queries = [[0,3],[1,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1, 0]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li><code>s[0..3] = &quot;1000&quot;</code>

	<ul>
		<li><code>x = 1</code></li>
		<li><code>sum = 1</code></li>
		<li>Therefore, the answer is <code>1 * 1 = 1</code>.</li>
	</ul>
	</li>
	<li><code>s[1..1] = &quot;0&quot;</code>
	<ul>
		<li><code>x = 0</code></li>
		<li><code>sum = 0</code></li>
		<li>Therefore, the answer is <code>0 * 0 = 0</code>.</li>
	</ul>
	</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;9876543210&quot;, queries = [[0,9]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[444444137]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li><code>s[0..9] = &quot;9876543210&quot;</code>

	<ul>
		<li><code>x = 987654321</code></li>
		<li><code>sum = 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 45</code></li>
		<li>Therefore, the answer is <code>987654321 * 45 = 44444444445</code>.</li>
		<li>We return <code>44444444445 modulo (10<sup>9</sup> + 7) = 444444137</code>.</li>
	</ul>
	</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m == s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of digits only.</li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>queries[i] = [l<sub>i</sub>, r<sub>i</sub>]</code></li>
	<li><code>0 &lt;= l<sub>i</sub> &lt;= r<sub>i</sub> &lt; m</code></li>
</ul>


## Hints

1. Track only nonzero digits: store their values and positions and keep a prefix sum for digit sums.

2. Also build prefix concatenation values `P`, `pow10`, and set `mod = 10^9+7` so any compressed substring number is obtainable from prefixes.

3. Map each query `[l, r]` to the compressed list using precomputed mapping arrays (first nonzero at or after `i`

4. If the mapped range is empty return `0`; otherwise get `x` from `P`, get `sum` from the digit-prefix, and return `(x * sum) % mod`.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm identifies and compresses the string by focusing only on non-zero digits. First, we identify all non-zero digits and their original indices in $s$, storing them in an auxiliary array $v$. We then precompute three essential prefix arrays for $v$: a prefix sum array to calculate the digit sum of any compressed substring in $O(1)$, a 'rolling hash' prefix array to calculate the numerical value $x$ of any concatenated sequence of non-zero digits modulo $10^9+7$, and an array of powers of 10 to assist in the numerical value calculation. 

To handle queries efficiently, we create two mapping arrays, `first_idx` and `last_idx`. For each index $i$ in the original string, `first_idx[i]` stores the index in $v$ of the first non-zero digit appearing at or after $i$, and `last_idx[i]` stores the index in $v$ of the last non-zero digit appearing at or before $i$. For any query range $[l, r]$, these arrays allow us to find the corresponding range $[L, R]$ in $v$ in $O(1)$. If $L \le R$, we compute $x = (P[R+1] - P[L] \cdot 10^{R-L+1}) \pmod{10^9+7}$ and the digit sum from the prefix sum array, then return their product modulo $10^9+7$. If $L > R$, the range contains only zeros, so the answer is 0.

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
    vector<int> sumAndMultiply(string s, vector<vector<int>>& queries) {
        int m = s.length();
        long long MOD = 1000000007LL;
        vector<int> v;
        vector<int> v_orig_idx;
        for (int i = 0; i < m; ++i) {
            if (s[i] != '0') {
                v.push_back(s[i] - '0');
                v_orig_idx.push_back(i);
            }
        }

        int v_size = v.size();
        vector<int> first_idx(m, v_size);
        int v_ptr = 0;
        for (int i = 0; i < m; ++i) {
            while (v_ptr < v_size && v_orig_idx[v_ptr] < i) v_ptr++;
            first_idx[i] = v_ptr;
        }

        vector<int> last_idx(m, -1);
        int curr_last = -1;
        for (int i = 0; i < m; ++i) {
            if (s[i] != '0') curr_last++;
            last_idx[i] = curr_last;
        }

        vector<long long> P(v_size + 1, 0);
        vector<long long> prefixSum(v_size + 1, 0);
        vector<long long> pow10(v_size + 1, 1);
        for (int i = 0; i < v_size; ++i) {
            P[i + 1] = (P[i] * 10 + v[i]) % MOD;
            prefixSum[i + 1] = prefixSum[i] + v[i];
            pow10[i + 1] = (pow10[i] * 10) % MOD;
        }

        int n = queries.size();
        vector<int> ans(n);
        for (int i = 0; i < n; ++i) {
            int L = first_idx[queries[i][0]];
            int R = last_idx[queries[i][1]];
            if (L > R) {
                ans[i] = 0;
            } else {
                long long x = (P[R + 1] - (P[L] * pow10[R - L + 1]) % MOD + MOD) % MOD;
                long long s_val = (prefixSum[R + 1] - prefixSum[L]);
                ans[i] = (int)((x * (s_val % MOD)) % MOD);
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
    public int[] sumAndMultiply(String s, int[][] queries) {
        int m = s.length();
        long MOD = 1000000007L;
        int v_size = 0;
        for (int i = 0; i < m; i++) if (s.charAt(i) != '0') v_size++;

        int[] v = new int[v_size];
        int[] v_orig_idx = new int[v_size];
        int idx = 0;
        for (int i = 0; i < m; i++) {
            if (s.charAt(i) != '0') {
                v[idx] = s.charAt(i) - '0';
                v_orig_idx[idx] = i;
                idx++;
            }
        }

        int[] first_idx = new int[m];
        int v_ptr = 0;
        for (int i = 0; i < m; i++) {
            while (v_ptr < v_size && v_orig_idx[v_ptr] < i) v_ptr++;
            first_idx[i] = v_ptr;
        }

        int[] last_idx = new int[m];
        int curr_last = -1;
        for (int i = 0; i < m; i++) {
            if (s.charAt(i) != '0') curr_last++;
            last_idx[i] = curr_last;
        }

        long[] P = new long[v_size + 1];
        long[] prefixSum = new long[v_size + 1];
        long[] pow10 = new long[v_size + 1];
        pow10[0] = 1;
        for (int i = 0; i < v_size; i++) {
            P[i + 1] = (P[i] * 10 + v[i]) % MOD;
            prefixSum[i + 1] = prefixSum[i] + v[i];
            pow10[i + 1] = (pow10[i] * 10) % MOD;
        }

        int n = queries.length;
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            int L = first_idx[queries[i][0]];
            int R = last_idx[queries[i][1]];
            if (L > R) {
                ans[i] = 0;
            } else {
                long x = (P[R + 1] - (P[L] * pow10[R - L + 1]) % MOD + MOD) % MOD;
                long s_val = prefixSum[R + 1] - prefixSum[L];
                ans[i] = (int)((x * (s_val % MOD)) % MOD);
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
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 1000000007
        m = len(s)
        v = [ord(c) - 48 for c in s if c != '0']
        v_orig_idx = [i for i, c in enumerate(s) if c != '0']
        v_size = len(v)

        first_idx = [0] * m
        v_ptr = 0
        for i in xrange(m):
            while v_ptr < v_size and v_orig_idx[v_ptr] < i:
                v_ptr += 1
            first_idx[i] = v_ptr

        last_idx = [0] * m
        curr_last = -1
        for i in xrange(m):
            if s[i] != '0':
                curr_last += 1
            last_idx[i] = curr_last

        P = [0] * (v_size + 1)
        prefixSum = [0] * (v_size + 1)
        pow10 = [1] * (v_size + 1)
        for i in xrange(v_size):
            P[i+1] = (P[i] * 10 + v[i]) % MOD
            prefixSum[i+1] = prefixSum[i] + v[i]
            pow10[i+1] = (pow10[i] * 10) % MOD

        ans = [0] * len(queries)
        for i in xrange(len(queries)):
            l, r = queries[i]
            L, R = first_idx[l], last_idx[r]
            if L > R:
                ans[i] = 0
            else:
                x = (P[R+1] - P[L] * pow10[R-L+1]) % MOD
                s_val = prefixSum[R+1] - prefixSum[L]
                ans[i] = (x * s_val) % MOD
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 1000000007
        m = len(s)
        v = [ord(c) - 48 for c in s if c != '0']
        v_orig_idx = [i for i, c in enumerate(s) if c != '0']
        v_size = len(v)

        first_idx = [0] * m
        v_ptr = 0
        for i in range(m):
            while v_ptr < v_size and v_orig_idx[v_ptr] < i:
                v_ptr += 1
            first_idx[i] = v_ptr

        last_idx = [0] * m
        curr_last = -1
        for i in range(m):
            if s[i] != '0':
                curr_last += 1
            last_idx[i] = curr_last

        P = [0] * (v_size + 1)
        prefixSum = [0] * (v_size + 1)
        pow10 = [1] * (v_size + 1)
        for i in range(v_size):
            P[i+1] = (P[i] * 10 + v[i]) % MOD
            prefixSum[i+1] = prefixSum[i] + v[i]
            pow10[i+1] = (pow10[i] * 10) % MOD

        ans = [0] * len(queries)
        for i in range(len(queries)):
            l, r = queries[i]
            L, R = first_idx[l], last_idx[r]
            if L > R:
                ans[i] = 0
            else:
                x = (P[R+1] - P[L] * pow10[R-L+1]) % MOD
                s_val = prefixSum[R+1] - prefixSum[L]
                ans[i] = (x * s_val) % MOD
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sumAndMultiply(char* s, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    int m = strlen(s);
    int* v = (int*)malloc(sizeof(int) * m);
    int* v_orig_idx = (int*)malloc(sizeof(int) * m);
    int v_size = 0;
    int* last_idx = (int*)malloc(sizeof(int) * m);
    int curr_last = -1;
    for (int i = 0; i < m; i++) {
        if (s[i] != '0') {
            v[v_size] = s[i] - '0';
            v_orig_idx[v_size] = i;
            v_size++;
            curr_last++;
        }
        last_idx[i] = curr_last;
    }

    int* first_idx = (int*)malloc(sizeof(int) * m);
    int v_ptr = 0;
    for (int i = 0; i < m; i++) {
        while (v_ptr < v_size && v_orig_idx[v_ptr] < i) v_ptr++;
        first_idx[i] = v_ptr;
    }

    long long mod = 1000000007;
    long long* P = (long long*)malloc(sizeof(long long) * (v_size + 1));
    long long* prefixSum = (long long*)malloc(sizeof(long long) * (v_size + 1));
    long long* pow10 = (long long*)malloc(sizeof(long long) * (v_size + 1));
    P[0] = 0;
    prefixSum[0] = 0;
    pow10[0] = 1;
    for (int i = 0; i < v_size; i++) {
        P[i + 1] = (P[i] * 10 + v[i]) % mod;
        prefixSum[i + 1] = prefixSum[i] + v[i];
        pow10[i + 1] = (pow10[i] * 10) % mod;
    }

    int* ans = (int*)malloc(sizeof(int) * queriesSize);
    *returnSize = queriesSize;
    for (int i = 0; i < queriesSize; i++) {
        int l = queries[i][0];
        int r = queries[i][1];
        int L = first_idx[l];
        int R = last_idx[r];
        if (L > R) {
            ans[i] = 0;
        } else {
            long long x = (P[R + 1] - (P[L] * pow10[R - L + 1]) % mod + mod) % mod;
            long long s_val = prefixSum[R + 1] - prefixSum[L];
            ans[i] = (int)((x * (s_val % mod)) % mod);
        }
    }

    free(v); free(v_orig_idx); free(last_idx); free(first_idx); free(P); free(prefixSum); free(pow10);
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int[] SumAndMultiply(string s, int[][] queries) {
        int m = s.Length;
        long MOD = 1000000007L;
        System.Collections.Generic.List<int> nzVals = new System.Collections.Generic.List<int>();
        System.Collections.Generic.List<int> nzPos = new System.Collections.Generic.List<int>();

        for (int k = 0; k < m; k++) {
            if (s[k] != '0') {
                nzVals.Add(s[k] - '0');
                nzPos.Add(k);
            }
        }

        int nzCount = nzVals.Count;
        long[] P_sum = new long[nzCount + 1];
        long[] P_concat = new long[nzCount + 1];
        long[] pow10 = new long[nzCount + 1];
        pow10[0] = 1;

        for (int i = 0; i < nzCount; i++) {
            P_sum[i + 1] = P_sum[i] + nzVals[i];
            P_concat[i + 1] = (P_concat[i] * 10 + nzVals[i]) % MOD;
            pow10[i + 1] = (pow10[i] * 10) % MOD;
        }

        int[] nextIdx = new int[m];
        int ptr = 0;
        for (int i = 0; i < m; i++) {
            while (ptr < nzCount && nzPos[ptr] < i) ptr++;
            nextIdx[i] = ptr;
        }

        int[] prevIdx = new int[m];
        ptr = nzCount - 1;
        for (int i = m - 1; i >= 0; i--) {
            while (ptr >= 0 && nzPos[ptr] > i) ptr--;
            prevIdx[i] = ptr;
        }

        int[] results = new int[queries.Length];
        for (int q = 0; q < queries.Length; q++) {
            int l = queries[q][0];
            int r = queries[q][1];
            int iIdx = nextIdx[l];
            int jIdx = prevIdx[r];

            if (iIdx > jIdx) {
                results[q] = 0;
            } else {
                int numElements = jIdx - iIdx + 1;
                long x = (P_concat[jIdx + 1] - (P_concat[iIdx] * pow10[numElements]) % MOD + MOD) % MOD;
                long sVal = P_sum[jIdx + 1] - P_sum[iIdx];
                results[q] = (int)((x * (sVal % MOD)) % MOD);
            }
        }

        return results;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} s
 * @param {number[][]} queries
 * @return {number[]}
 */
var sumAndMultiply = function(s, queries) {
    const m = s.length;
    const MOD = 1000000007n;
    const nzVals = [];
    const nzPos = [];
    for (let k = 0; k < m; k++) {
        if (s[k] !== '0') {
            nzVals.push(Number(s[k]));
            nzPos.push(k);
        }
    }

    const nzCount = nzVals.length;
    const P_sum = new BigInt64Array(nzCount + 1);
    const P_concat = new BigInt64Array(nzCount + 1);
    const pow10 = new BigInt64Array(nzCount + 1);
    pow10[0] = 1n;

    for (let i = 0; i < nzCount; i++) {
        P_sum[i + 1] = P_sum[i] + BigInt(nzVals[i]);
        P_concat[i + 1] = (P_concat[i] * 10n + BigInt(nzVals[i])) % MOD;
        pow10[i + 1] = (pow10[i] * 10n) % MOD;
    }

    const nextIdx = new Int32Array(m);
    let ptr = 0;
    for (let i = 0; i < m; i++) {
        while (ptr < nzCount && nzPos[ptr] < i) ptr++;
        nextIdx[i] = ptr;
    }

    const prevIdx = new Int32Array(m);
    ptr = nzCount - 1;
    for (let i = m - 1; i >= 0; i--) {
        while (ptr >= 0 && nzPos[ptr] > i) ptr--;
        prevIdx[i] = ptr;
    }

    const results = [];
    for (let q = 0; q < queries.length; q++) {
        const l = queries[q][0];
        const r = queries[q][1];
        const iIdx = nextIdx[l];
        const jIdx = prevIdx[r];

        if (iIdx > jIdx) {
            results.push(0);
        } else {
            const numElements = jIdx - iIdx + 1;
            const x = (P_concat[jIdx + 1] - (P_concat[iIdx] * pow10[numElements]) % MOD + MOD) % MOD;
            const sVal = P_sum[jIdx + 1] - P_sum[iIdx];
            results.push(Number((x * (sVal % MOD)) % MOD));
        }
    }

    return results;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function sumAndMultiply(s: string, queries: number[][]): number[] {
    const m = s.length;
    const MOD = 1000000007n;
    const nzVals: number[] = [];
    const nzPos: number[] = [];
    for (let k = 0; k < m; k++) {
        if (s[k] !== '0') {
            nzVals.push(Number(s[k]));
            nzPos.push(k);
        }
    }

    const nzCount = nzVals.length;
    const P_sum = new BigInt64Array(nzCount + 1);
    const P_concat = new BigInt64Array(nzCount + 1);
    const pow10 = new BigInt64Array(nzCount + 1);
    pow10[0] = 1n;

    for (let i = 0; i < nzCount; i++) {
        P_sum[i + 1] = P_sum[i] + BigInt(nzVals[i]);
        P_concat[i + 1] = (P_concat[i] * 10n + BigInt(nzVals[i])) % MOD;
        pow10[i + 1] = (pow10[i] * 10n) % MOD;
    }

    const nextIdx = new Int32Array(m);
    let ptr = 0;
    for (let i = 0; i < m; i++) {
        while (ptr < nzCount && nzPos[ptr] < i) ptr++;
        nextIdx[i] = ptr;
    }

    const prevIdx = new Int32Array(m);
    ptr = nzCount - 1;
    for (let i = m - 1; i >= 0; i--) {
        while (ptr >= 0 && nzPos[ptr] > i) ptr--;
        prevIdx[i] = ptr;
    }

    const results: number[] = [];
    for (let q = 0; q < queries.length; q++) {
        const l = queries[q][0];
        const r = queries[q][1];
        const iIdx = nextIdx[l];
        const jIdx = prevIdx[r];

        if (iIdx > jIdx) {
            results.push(0);
        } else {
            const numElements = jIdx - iIdx + 1;
            const x = (P_concat[jIdx + 1] - (P_concat[iIdx] * pow10[numElements]) % MOD + MOD) % MOD;
            const sVal = P_sum[jIdx + 1] - P_sum[iIdx];
            results.push(Number((x * (sVal % MOD)) % MOD));
        }
    }

    return results;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String $s
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function sumAndMultiply($s, $queries) {
        $m = strlen($s);
        $MOD = 1000000007;
        $nz_vals = [];
        $nz_pos = [];
        for ($k = 0; $k < $m; $k++) {
            if ($s[$k] !== '0') {
                $nz_vals[] = (int)$s[$k];
                $nz_pos[] = $k;
            }
        }

        $nz_count = count($nz_vals);
        $P_sum = array_fill(0, $nz_count + 1, 0);
        $P_concat = array_fill(0, $nz_count + 1, 0);
        $pow10 = array_fill(0, $nz_count + 1, 0);
        $pow10[0] = 1;

        for ($i = 0; $i < $nz_count; $i++) {
            $P_sum[$i + 1] = $P_sum[$i] + $nz_vals[$i];
            $P_concat[$i + 1] = ($P_concat[$i] * 10 + $nz_vals[$i]) % $MOD;
            $pow10[$i + 1] = ($pow10[$i] * 10) % $MOD;
        }

        $next_idx = array_fill(0, $m, 0);
        $ptr = 0;
        for ($i = 0; $i < $m; $i++) {
            while ($ptr < $nz_count && $nz_pos[$ptr] < $i) $ptr++;
            $next_idx[$i] = $ptr;
        }

        $prev_idx = array_fill(0, $m, -1);
        $ptr = $nz_count - 1;
        for ($i = $m - 1; $i >= 0; $i--) {
            while ($ptr >= 0 && $nz_pos[$ptr] > $i) $ptr--;
            $prev_idx[$i] = $ptr;
        }

        $results = [];
        foreach ($queries as $query) {
            $l = $query[0];
            $r = $query[1];
            $iIdx = $next_idx[$l];
            $jIdx = $prev_idx[$r];

            if ($iIdx > $jIdx) {
                $results[] = 0;
            } else {
                $num_elements = $jIdx - $iIdx + 1;
                $x = ($P_concat[$jIdx + 1] - ($P_concat[$iIdx] * $pow10[$num_elements]) % $MOD + $MOD) % $MOD;
                $s_val = $P_sum[$jIdx + 1] - $P_sum[$iIdx];
                $results[] = (int)(($x * ($s_val % $MOD)) % $MOD);
            }
        }

        return $results;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func sumAndMultiply(_ s: String, _ queries: [[Int]]) -> [Int] {
        let sBytes = [UInt8](s.utf8)
        let m = sBytes.count
        let MOD: Int64 = 1000000007

        var nzVals: [Int] = []
        var nzPos: [Int] = []
        for k in 0..<m {
            if sBytes[k] != 48 {
                nzVals.append(Int(sBytes[k] - 48))
                nzPos.append(k)
            }
        }

        let nzCount = nzVals.count
        var P_sum = [Int64](repeating: 0, count: nzCount + 1)
        var P_concat = [Int64](repeating: 0, count: nzCount + 1)
        var pow10 = [Int64](repeating: 0, count: nzCount + 1)
        pow10[0] = 1

        for i in 0..<nzCount {
            P_sum[i + 1] = P_sum[i] + Int64(nzVals[i])
            P_concat[i + 1] = (P_concat[i] * 10 + Int64(nzVals[i])) % MOD
            pow10[i + 1] = (pow10[i] * 10) % MOD
        }

        var nextIdx = [Int](repeating: 0, count: m)
        var ptr = 0
        for i in 0..<m {
            while ptr < nzCount && nzPos[ptr] < i {
                ptr += 1
            }
            nextIdx[i] = ptr
        }

        var prevIdx = [Int](repeating: -1, count: m)
        ptr = nzCount - 1
        for i in (0..<m).reversed() {
            while ptr >= 0 && nzPos[ptr] > i {
                ptr -= 1
            }
            prevIdx[i] = ptr
        }

        var results: [Int] = []
        for query in queries {
            let l = query[0]
            let r = query[1]
            let iIdx = nextIdx[l]
            let jIdx = prevIdx[r]

            if iIdx > jIdx {
                results.append(0)
            } else {
                let numElements = jIdx - iIdx + 1
                let x = (P_concat[jIdx + 1] - (P_concat[iIdx] * pow10[numElements]) % MOD + MOD) % MOD
                let sVal = P_sum[jIdx + 1] - P_sum[iIdx]
                results.append(Int((x * (sVal % MOD)) % MOD))
            }
        }

        return results
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun sumAndMultiply(s: String, queries: Array<IntArray>): IntArray {
        val m = s.length
        val mod = 1000000007L

        val nzDigits = mutableListOf<Int>()
        for (i in 0 until m) {
            val digit = s[i] - '0'
            if (digit != 0) {
                nzDigits.add(digit)
            }
        }

        val n = nzDigits.size
        val prefixSum = LongArray(n + 1)
        val prefixVal = LongArray(n + 1)
        val pow10 = LongArray(n + 1)
        pow10[0] = 1
        for (i in 0 until n) {
            prefixSum[i + 1] = prefixSum[i] + nzDigits[i]
            prefixVal[i + 1] = (prefixVal[i] * 10 + nzDigits[i]) % mod
            pow10[i + 1] = (pow10[i] * 10) % mod
        }

        val nextNz = IntArray(m) { -1 }
        var firstNzIdx = n
        for (i in m - 1 downTo 0) {
            if (s[i] != '0') {
                firstNzIdx--
            }
            if (firstNzIdx < n) {
                nextNz[i] = firstNzIdx
            }
        }

        val prevNz = IntArray(m) { -1 }
        var lastNzIdx = -1
        for (i in 0 until m) {
            if (s[i] != '0') {
                lastNzIdx++
            }
            prevNz[i] = lastNzIdx
        }

        val result = IntArray(queries.size)
        for (i in queries.indices) {
            val l = queries[i][0]
            val r = queries[i][1]
            val first = nextNz[l]
            val last = prevNz[r]

            if (first == -1 || last == -1 || first > last) {
                result[i] = 0
            } else {
                val numElements = last - first + 1
                val x = (prefixVal[last + 1] - (prefixVal[first] * pow10[numElements]) % mod + mod) % mod
                val sum = (prefixSum[last + 1] - prefixSum[first]) % mod
                result[i] = ((x * sum) % mod).toInt()
            }
        }
        return result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<int> sumAndMultiply(String s, List<List<int>> queries) {
    int m = s.length;
    int mod = 1000000007;

    List<int> nzDigits = [];
    for (int i = 0; i < m; i++) {
      int digit = s.codeUnitAt(i) - 48;
      if (digit != 0) {
        nzDigits.add(digit);
      }
    }

    int n = nzDigits.length;
    List<int> prefixSum = List<int>.filled(n + 1, 0);
    List<int> prefixVal = List<int>.filled(n + 1, 0);
    List<int> pow10 = List<int>.filled(n + 1, 0);
    pow10[0] = 1;
    for (int i = 0; i < n; i++) {
      prefixSum[i + 1] = prefixSum[i] + nzDigits[i];
      prefixVal[i + 1] = (prefixVal[i] * 10 + nzDigits[i]) % mod;
      pow10[i + 1] = (pow10[i] * 10) % mod;
    }

    List<int> nextNz = List<int>.filled(m, -1);
    int firstNzIdx = n;
    for (int i = m - 1; i >= 0; i--) {
      if (s.codeUnitAt(i) != 48) {
        firstNzIdx--;
      }
      if (firstNzIdx < n) {
        nextNz[i] = firstNzIdx;
      }
    }

    List<int> prevNz = List<int>.filled(m, -1);
    int lastNzIdx = -1;
    for (int i = 0; i < m; i++) {
      if (s.codeUnitAt(i) != 48) {
        lastNzIdx++;
      }
      prevNz[i] = lastNzIdx;
    }

    List<int> result = List<int>.filled(queries.length, 0);
    for (int i = 0; i < queries.length; i++) {
      int l = queries[i][0];
      int r = queries[i][1];
      int first = nextNz[l];
      int last = prevNz[r];

      if (first == -1 || last == -1 || first > last) {
        result[i] = 0;
      } else {
        int numElements = last - first + 1;
        int x = (prefixVal[last + 1] - (prefixVal[first] * pow10[numElements]) % mod + mod) % mod;
        int sum = (prefixSum[last + 1] - prefixSum[first]) % mod;
        result[i] = (x * sum) % mod;
      }
    }
    return result;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func sumAndMultiply(s string, queries [][]int) []int {
	m := len(s)
	mod := int64(1000000007)

	nzDigits := make([]int, 0, m)
	for i := 0; i < m; i++ {
		digit := int(s[i] - '0')
		if digit != 0 {
			nzDigits = append(nzDigits, digit)
		}
	}

	n := len(nzDigits)
	prefixSum := make([]int64, n+1)
	prefixVal := make([]int64, n+1)
	pow10 := make([]int64, n+1)
	pow10[0] = 1
	for i := 0; i < n; i++ {
		prefixSum[i+1] = prefixSum[i] + int64(nzDigits[i])
		prefixVal[i+1] = (prefixVal[i]*10 + int64(nzDigits[i])) % mod
		pow10[i+1] = (pow10[i] * 10) % mod
	}

	nextNz := make([]int, m)
	for i := range nextNz {
		nextNz[i] = -1
	}
	firstNzIdx := n
	for i := m - 1; i >= 0; i-- {
		if s[i] != '0' {
			firstNzIdx--
		}
		if firstNzIdx < n {
			nextNz[i] = firstNzIdx
		}
	}

	prevNz := make([]int, m)
	for i := range prevNz {
		prevNz[i] = -1
	}
	lastNzIdx := -1
	for i := 0; i < m; i++ {
		if s[i] != '0' {
			lastNzIdx++
		}
		prevNz[i] = lastNzIdx
	}

	result := make([]int, len(queries))
	for i, q := range queries {
		l, r := q[0], q[1]
		first := nextNz[l]
		last := prevNz[r]

		if first == -1 || last == -1 || first > last {
			result[i] = 0
		} else {
			numElements := last - first + 1
			x := (prefixVal[last+1] - (prefixVal[first]*pow10[numElements])%mod + mod) % mod
			sum := (prefixSum[last+1] - prefixSum[first]) % mod
			result[i] = int((x * sum) % mod)
		}
	}
	return result
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def sum_and_multiply(s, queries)
  m = s.length
  mod = 1000000007

  nz_digits = []
  s.each_char do |c|
    d = c.to_i
    nz_digits << d if d != 0
  end

  n = nz_digits.length
  prefix_sum = Array.new(n + 1, 0)
  prefix_val = Array.new(n + 1, 0)
  pow10 = Array.new(n + 1, 0)
  pow10[0] = 1
  (0...n).each do |i|
    prefix_sum[i + 1] = prefix_sum[i] + nz_digits[i]
    prefix_val[i + 1] = (prefix_val[i] * 10 + nz_digits[i]) % mod
    pow10[i + 1] = (pow10[i] * 10) % mod
  end

  next_nz = Array.new(m, -1)
  first_nz_idx = n
  (m - 1).downto(0) do |i|
    first_nz_idx -= 1 if s[i] != '0'
    next_nz[i] = first_nz_idx if first_nz_idx < n
  end

  prev_nz = Array.new(m, -1)
  last_nz_idx = -1
  (0...m).each do |i|
    last_nz_idx += 1 if s[i] != '0'
    prev_nz[i] = last_nz_idx
  end

  queries.map do |l, r|
    first = next_nz[l]
    last = prev_nz[r]
    if first == -1 || last == -1 || first > last
      0
    else
      num_elements = last - first + 1
      x = (prefix_val[last + 1] - (prefix_val[first] * pow10[num_elements]) % mod) % mod
      sum = (prefix_sum[last + 1] - prefix_sum[first]) % mod
      (x * sum) % mod
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def sumAndMultiply(s: String, queries: Array[Array[Int]]): Array[Int] = {
    val m = s.length
    val mod = 1000000007L

    val nzDigits = new scala.collection.mutable.ArrayBuffer[Int]()
    var idx = 0
    while (idx < m) {
      val d = s(idx) - '0'
      if (d != 0) {
        nzDigits += d
      }
      idx += 1
    }

    val n = nzDigits.length
    val prefixSum = new Array[Long](n + 1)
    val prefixVal = new Array[Long](n + 1)
    val pow10 = new Array[Long](n + 1)
    pow10(0) = 1
    for (i <- 0 until n) {
      prefixSum(i + 1) = prefixSum(i) + nzDigits(i)
      prefixVal(i + 1) = (prefixVal(i) * 10 + nzDigits(i)) % mod
      pow10(i + 1) = (pow10(i) * 10) % mod
    }

    val nextNz = Array.fill(m)(-1)
    var firstNzIdx = n
    for (i <- m - 1 to 0 by -1) {
      if (s(i) != '0') {
        firstNzIdx -= 1
      }
      if (firstNzIdx < n) {
        nextNz(i) = firstNzIdx
      }
    }

    val prevNz = Array.fill(m)(-1)
    var lastNzIdx = -1
    for (i <- 0 until m) {
      if (s(i) != '0') {
        lastNzIdx += 1
      }
      prevNz(i) = lastNzIdx
    }

    val result = new Array[Int](queries.length)
    for (i <- queries.indices) {
      val l = queries(i)(0)
      val r = queries(i)(1)
      val first = nextNz(l)
      val last = prevNz(r)

      if (first == -1 || last == -1 || first > last) {
        result(i) = 0
      } else {
        val numElements = last - first + 1
        val x = (prefixVal(last + 1) - (prefixVal(first) * pow10(numElements)) % mod + mod) % mod
        val sum = (prefixSum(last + 1) - prefixSum(first)) % mod
        result(i) = ((x * sum) % mod).toInt
      }
    }
    result
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn sum_and_multiply(s: String, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let n = s.len();
        let s_bytes = s.as_bytes();
        let mut nz = Vec::new();
        let mut nz_idx = Vec::new();
        for (i, &b) in s_bytes.iter().enumerate() {
            if b != b'0' {
                nz.push((b - b'0') as i64);
                nz_idx.push(i);
            }
        }

        let nz_len = nz.len();
        let mut prefix_sum = vec![0i64; nz_len + 1];
        let mut prefix_concat = vec![0i64; nz_len + 1];
        let mod_val = 1_000_000_007i64;
        let mut pow10 = vec![1i64; nz_len + 1];

        for i in 0..nz_len {
            prefix_sum[i + 1] = prefix_sum[i] + nz[i];
            prefix_concat[i + 1] = (prefix_concat[i] * 10 + nz[i]) % mod_val;
            pow10[i + 1] = (pow10[i] * 10) % mod_val;
        }

        let mut first_nz = vec![nz_len as i32; n];
        let mut last_nz = vec![-1i32; n];

        let mut cur = 0;
        for i in 0..n {
            while cur < nz_len && nz_idx[cur] < i {
                cur += 1;
            }
            if cur < nz_len {
                first_nz[i] = cur as i32;
            }
        }

        let mut cur = (nz_len as i32) - 1;
        for i in (0..n).rev() {
            while cur >= 0 && nz_idx[cur as usize] > i {
                cur -= 1;
            }
            if cur >= 0 {
                last_nz[i] = cur;
            }
        }

        queries.into_iter().map(|q| {
            let l = q[0] as usize;
            let r = q[1] as usize;
            let i = first_nz[l];
            let j = last_nz[r];
            if i > j || i == nz_len as i32 || j == -1 {
                0
            } else {
                let i_u = i as usize;
                let j_u = j as usize;
                let sum = prefix_sum[j_u + 1] - prefix_sum[i_u];
                let x = (prefix_concat[j_u + 1] - (prefix_concat[i_u] * pow10[j_u - i_u + 1]) % mod_val + mod_val) % mod_val;
                ((x * (sum % mod_val)) % mod_val) as i32
            }
        }).collect()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (sum-and-multiply s queries)
  (-> string? (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ([n (string-length s)]
         [mod 1000000007]
         [nz-data (let loop ([i 0] [nz '()] [nz-idx '()])
                    (if (= i n)
                        (list (reverse nz) (reverse nz-idx))
                        (let ([digit (- (char->integer (string-ref s i)) 48)])
                          (if (zero? digit)
                              (loop (+ i 1) nz nz-idx)
                              (loop (+ i 1) (cons digit nz) (cons i nz-idx))))))]
         [nz (list->vector (car nz-data))]
         [nz-idx (list->vector (cadr nz-data))]
         [nz-len (vector-length nz)]
         [prefix-sum (make-vector (+ nz-len 1) 0)]
         [prefix-concat (make-vector (+ nz-len 1) 0)]
         [pow10 (make-vector (+ nz-len 1) 1)]
         [first-nz (make-vector n nz-len)]
         [last-nz (make-vector n -1)])
    (for ([i (in-range nz-len)])
      (let ([digit (vector-ref nz i)])
        (vector-set! prefix-sum (+ i 1) (+ (vector-ref prefix-sum i) digit))
        (vector-set! prefix-concat (+ i 1) (modulo (+ (* (vector-ref prefix-concat i) 10) digit) mod))
        (vector-set! pow10 (+ i 1) (modulo (* (vector-ref pow10 i) 10) mod))))
    (let loop ([i 0] [cur 0])
      (when (< i n)
        (let ([next-cur (let loop2 ([cur cur])
                          (if (and (< cur nz-len) (< (vector-ref nz-idx cur) i))
                              (loop2 (+ cur 1))
                              cur))])
          (when (< next-cur nz-len)
            (vector-set! first-nz i next-cur))
          (loop (+ i 1) next-cur))))
    (let loop ([i (- n 1)] [cur (- nz-len 1)])
      (when (>= i 0)
        (let ([next-cur (let loop2 ([cur cur])
                          (if (and (>= cur 0) (> (vector-ref nz-idx cur) i))
                              (loop2 (- cur 1))
                              cur))])
          (when (>= next-cur 0)
            (vector-set! last-nz i next-cur))
          (loop (- i 1) next-cur))))
    (map (lambda (q)
           (let* ([l (car q)]
                  [r (cadr q)]
                  [i (vector-ref first-nz l)]
                  [j (vector-ref last-nz r)])
             (if (or (> i j) (= i nz-len) (= j -1))
                 0
                 (let* ([sum-val (- (vector-ref prefix-sum (+ j 1)) (vector-ref prefix-sum i))]
                        [p-j1 (vector-ref prefix-concat (+ j 1))]
                        [p-i (vector-ref prefix-concat i)]
                        [pw (vector-ref pow10 (+ (- j i) 1))]
                        [x (modulo (- p-j1 (modulo (* p-i pw) mod)) mod)])
                   (modulo (* x (modulo sum-val mod)) mod)))))
         queries)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec sum_and_multiply(S :: unicode:unicode_binary(), Queries :: [[integer()]]) -> [integer()].
sum_and_multiply(S, Queries) ->
    N = byte_size(S),
    Mod = 1000000007,
    SList = binary_to_list(S),
    {NZList, NZIdxList, _} = lists:foldl(
        fun(C, {AccNZ, AccIdx, I}) ->
            D = C - $0,
            if D /= 0 -> {[D | AccNZ], [I | AccIdx], I + 1};
               true -> {AccNZ, AccIdx, I + 1}
            end
        end,
        {[], [], 0},
        SList
    ),
    NZ = list_to_tuple(lists:reverse(NZList)),
    NZIdx = list_to_tuple(lists:reverse(NZIdxList)),
    NZLen = tuple_size(NZ),
    PrefixSum = list_to_tuple(lists:reverse(lists:foldl(
        fun(I, [H | _] = Acc) -> [(H + element(I, NZ)) | Acc] end,
        [0],
        lists:seq(1, NZLen)
    ))),
    PrefixConcat = list_to_tuple(lists:reverse(lists:foldl(
        fun(I, [H | _] = Acc) -> [(H * 10 + element(I, NZ)) rem Mod | Acc] end,
        [0],
        lists:seq(1, NZLen)
    ))),
    Pow10 = list_to_tuple(lists:reverse(lists:foldl(
        fun(_, [H | _] = Acc) -> [(H * 10) rem Mod | Acc] end,
        [1],
        lists:seq(1, NZLen)
    ))),
    FirstNZ = build_first_nz(N, NZIdx, NZLen),
    LastNZ = build_last_nz(N, NZIdx, NZLen),
    [get_query_ans(Q, FirstNZ, LastNZ, PrefixSum, PrefixConcat, Pow10, NZLen, Mod) || Q <- Queries].

build_first_nz(N, NZIdx, NZLen) ->
    {_, FirstNZList} = lists:foldl(
        fun(I, {Cur, Acc}) ->
            NewCur = find_first_idx(I, Cur, NZIdx, NZLen),
            {NewCur, [NewCur | Acc]}
        end,
        {1, []},
        lists:seq(0, N - 1)
    ),
    list_to_tuple(lists:reverse(FirstNZList)).

find_first_idx(I, Cur, NZIdx, NZLen) ->
    if Cur =< NZLen ->
        if element(Cur, NZIdx) < I -> find_first_idx(I, Cur + 1, NZIdx, NZLen);
           true -> Cur
        end;
       true -> NZLen + 1
    end.

build_last_nz(N, NZIdx, NZLen) ->
    {_, LastNZList} = lists:foldl(
        fun(I, {Cur, Acc}) ->
            NewCur = find_last_idx(I, Cur, NZIdx),
            {NewCur, [NewCur | Acc]}
        end,
        {NZLen, []},
        lists:seq(N - 1, 0, -1)
    ),
    list_to_tuple(LastNZList).

find_last_idx(I, Cur, NZIdx) ->
    if Cur >= 1 ->
        if element(Cur, NZIdx) > I -> find_last_idx(I, Cur - 1, NZIdx);
           true -> Cur
        end;
       true -> 0
    end.

get_query_ans([L, R], FirstNZ, LastNZ, PrefixSum, PrefixConcat, Pow10, NZLen, Mod) ->
    I = element(L + 1, FirstNZ),
    J = element(R + 1, LastNZ),
    if I > J orelse I > NZLen orelse J < 1 -> 0;
       true ->
           Sum = element(J + 1, PrefixSum) - element(I, PrefixSum),
           PJ1 = element(J + 1, PrefixConcat),
           PI = element(I, PrefixConcat),
           PW = element(J - I + 2, Pow10),
           X = (PJ1 - (PI * PW) rem Mod + Mod) rem Mod,
           (X * (Sum rem Mod)) rem Mod
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec sum_and_multiply(s :: String.t, queries :: [[integer]]) :: [integer]
  def sum_and_multiply(s, queries) do
    n = String.length(s)
    mod = 1_000_000_007
    chars = String.to_charlist(s)

    {nz_list, nz_idx_list} = Enum.reduce(Enum.with_index(chars), {[], []}, fn {char, idx}, {acc_nz, acc_idx} ->
      digit = char - ?0
      if digit != 0 do
        {[digit | acc_nz], [idx | acc_idx]}
      else
        {acc_nz, acc_idx}
      end
    end)

    nz = nz_list |> Enum.reverse() |> List.to_tuple()
    nz_idx = nz_idx_list |> Enum.reverse() |> List.to_tuple()
    nz_len = tuple_size(nz)

    prefix_sum = if nz_len > 0 do
      Enum.reduce(1..nz_len, [0], fn i, acc ->
        [hd(acc) + elem(nz, i - 1) | acc]
      end) |> Enum.reverse() |> List.to_tuple()
    else
      {0}
    end

    prefix_concat = if nz_len > 0 do
      Enum.reduce(1..nz_len, [0], fn i, acc ->
        [(hd(acc) * 10 + elem(nz, i - 1)) |> rem(mod) | acc]
      end) |> Enum.reverse() |> List.to_tuple()
    else
      {0}
    end

    pow10 = if nz_len > 0 do
      Enum.reduce(1..nz_len, [1], fn _i, acc ->
        [(hd(acc) * 10) |> rem(mod) | acc]
      end) |> Enum.reverse() |> List.to_tuple()
    else
      {1}
    end

    first_nz = build_first_nz(n, nz_idx, nz_len)
    last_nz = build_last_nz(n, nz_idx, nz_len)

    Enum.map(queries, fn [l, r] ->
      i = elem(first_nz, l)
      j = elem(last_nz, r)
      if i > j or i >= nz_len or j < 0 do
        0
      else
        sum_val = elem(prefix_sum, j + 1) - elem(prefix_sum, i)
        p_j1 = elem(prefix_concat, j + 1)
        p_i = elem(prefix_concat, i)
        pw = elem(pow10, j - i + 1)
        x = Integer.mod(p_j1 - Integer.mod(p_i * pw, mod), mod)
        Integer.mod(x * Integer.mod(sum_val, mod), mod)
      end
    end)
  end

  defp build_first_nz(n, nz_idx, nz_len) do
    {_final_cur, first_nz_list} = Enum.reduce(0..(n - 1), {0, []}, fn i, {cur, acc} ->
      new_cur = find_first(i, cur, nz_idx, nz_len)
      {new_cur, [new_cur | acc]}
    end)
    first_nz_list |> Enum.reverse() |> List.to_tuple()
  end

  defp find_first(i, cur, nz_idx, nz_len) do
    if cur < nz_len and elem(nz_idx, cur) < i do
      find_first(i, cur + 1, nz_idx, nz_len)
    else
      cur
    end
  end

  defp build_last_nz(n, nz_idx, nz_len) do
    {_final_cur, last_nz_list} = Enum.reduce((n - 1)..0, {nz_len - 1, []}, fn i, {cur, acc} ->
      new_cur = find_last(i, cur, nz_idx)
      {new_cur, [new_cur | acc]}
    end)
    last_nz_list |> List.to_tuple()
  end

  defp find_last(i, cur, nz_idx) do
    if cur >= 0 and elem(nz_idx, cur) > i do
      find_last(i, cur - 1, nz_idx)
    else
      cur
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(m + n), where m is the length of string s and n is the number of queries. Precomputing the non-zero digits, mappings, and prefix arrays takes $O(m)$ time. Each query is processed in $O(1)$ time by performing lookups and basic arithmetic operations.
- **Space Complexity:** O(m), as we maintain several arrays (non-zero digits, original indices, prefix sums, prefix values, powers of 10, and two mapping arrays) of size at most m. The result array for n queries takes $O(n)$ space.
