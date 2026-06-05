---
layout: post
title: "Total Waviness of Numbers in Range II"
date: 2026-06-05 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Math", "Dynamic Programming"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\n    struct Result {\n        long long w, c;\n    };\n\
        \    Result memo[20][2][2][11][11];\n    string S;\n\n    Result dfs(int pos,\
        \ bool tight, bool isLeading, int last1, int last2) {\n        if (pos == S.size())\
        \ return {0, 1};\n        if (memo[pos][tight][isLeading][last1][last2].w !=\
        \ -1) \n            return memo[pos][tight][isLeading][last1][last2];\n\n  \
        \      long long totalW = 0, totalC = 0;\n        int limit = tight ? S[pos]\
        \ - '0' : 9;\n        for (int d = 0; d <= limit; ++d) {\n            bool nextTight\
        \ = tight && (d == limit);\n            bool nextIsLeading = isLeading && (d\
        \ == 0);\n            int nextLast1 = nextIsLeading ? 10 : d;\n            int\
        \ nextLast2 = isLeading ? 10 : last1;\n\n            bool isWV = (!isLeading\
        \ && last2 != 10 && ((last2 < last1 && last1 > d) || (last2 > last1 && last1\
        \ < d)));\n            Result res = dfs(pos + 1, nextTight, nextIsLeading, nextLast1,\
        \ nextLast2);\n            totalW += res.w + (isWV ? res.c : 0);\n         \
        \   totalC += res.c;\n        }\n        return memo[pos][tight][isLeading][last1][last2]\
        \ = {totalW, totalC};\n    }\n\n    long long countWaviness(long long n) {\n\
        \        if (n < 100) return 0;\n        S = to_string(n);\n        for (int\
        \ a=0; a<20; ++a) for (int b=0; b<2; ++b) for (int c=0; c<2; ++c) \n       \
        \     for (int d=0; d<11; ++d) for (int e=0; e<11; ++e) memo[a][b][c][d][e]\
        \ = {-1, -1};\n        return dfs(0, true, true, 10, 10).w;\n    }\n\npublic:\n\
        \    long long totalWaviness(long long num1, long long num2) {\n        return\
        \ countWaviness(num2) - countWaviness(num1 - 1);\n    }\n};"
      java: "class Solution {\n    long[][][][][] memoW;\n    long[][][][][] memoC;\n\
        \    String S;\n\n    private long[] dfs(int pos, int tight, int isLeading,\
        \ int last1, int last2) {\n        if (pos == S.length()) return new long[]{0,\
        \ 1};\n        if (memoW[pos][tight][isLeading][last1][last2] != -1)\n     \
        \       return new long[]{memoW[pos][tight][isLeading][last1][last2], memoC[pos][tight][isLeading][last1][last2]};\n\
        \n        long totalW = 0, totalC = 0;\n        int limit = tight == 1 ? S.charAt(pos)\
        \ - '0' : 9;\n\n        for (int d = 0; d <= limit; d++) {\n            int\
        \ nextTight = (tight == 1 && d == limit) ? 1 : 0;\n            int nextIsLeading\
        \ = (isLeading == 1 && d == 0) ? 1 : 0;\n            int nextLast1 = nextIsLeading\
        \ == 1 ? 10 : d;\n            int nextLast2 = isLeading == 1 ? 10 : last1;\n\
        \n            boolean isWV = (isLeading == 0 && last2 != 10 && ((last2 < last1\
        \ && last1 > d) || (last2 > last1 && last1 < d)));\n            long[] res =\
        \ dfs(pos + 1, nextTight, nextIsLeading, nextLast1, nextLast2);\n          \
        \  totalW += res[0] + (isWV ? res[1] : 0);\n            totalC += res[1];\n\
        \        }\n\n        memoW[pos][tight][isLeading][last1][last2] = totalW;\n\
        \        memoC[pos][tight][isLeading][last1][last2] = totalC;\n        return\
        \ new long[]{totalW, totalC};\n    }\n\n    private long countWaviness(long\
        \ n) {\n        if (n < 100) return 0;\n        S = String.valueOf(n);\n   \
        \     int len = S.length();\n        memoW = new long[len + 1][2][2][11][11];\n\
        \        memoC = new long[len + 1][2][2][11][11];\n        for (int i = 0; i\
        \ <= len; i++)\n            for (int j = 0; j < 2; j++)\n                for\
        \ (int k = 0; k < 2; k++)\n                    for (int l = 0; l < 11; l++)\n\
        \                        for (int m = 0; m < 11; m++)\n                    \
        \        memoW[i][j][k][l][m] = -1;\n\n        return dfs(0, 1, 1, 10, 10)[0];\n\
        \    }\n\n    public long totalWaviness(long num1, long num2) {\n        return\
        \ countWaviness(num2) - countWaviness(num1 - 1);\n    }\n}"
      python: "import functools\n\nclass Solution(object):\n    def totalWaviness(self,\
        \ num1, num2):\n        \"\"\"\n        :type num1: int\n        :type num2:\
        \ int\n        :rtype: int\n        \"\"\"\n        def count_waviness(n):\n\
        \            if n < 100: return 0\n            s = str(n)\n\n            @functools.lru_cache(None)\n\
        \            def dp(pos, tight, is_leading, last1, last2):\n               \
        \ if pos == len(s):\n                    return 0, 1\n\n                res_w,\
        \ res_c = 0, 0\n                limit = int(s[pos]) if tight else 9\n\n    \
        \            for d in range(limit + 1):\n                    nt = tight and\
        \ (d == limit)\n                    nl = is_leading and (d == 0)\n         \
        \           n1 = 10 if nl else d\n                    n2 = 10 if is_leading\
        \ else last1\n\n                    is_wv = False\n                    if not\
        \ is_leading and last2 != 10:\n                        if (last2 < last1 and\
        \ last1 > d) or (last2 > last1 and last1 < d):\n                           \
        \ is_wv = True\n\n                    w, c = dp(pos + 1, nt, nl, n1, n2)\n \
        \                   res_w += w + (c if is_wv else 0)\n                    res_c\
        \ += c\n                return res_w, res_c\n\n            return dp(0, True,\
        \ True, 10, 10)[0]\n\n        return count_waviness(num2) - count_waviness(num1\
        \ - 1)"
      python3: "class Solution:\n    def totalWaviness(self, num1: int, num2: int) ->\
        \ int:\n        import sys\n        from functools import lru_cache\n      \
        \  sys.setrecursionlimit(2000)\n\n        def f(X: int) -> int:\n          \
        \  if X < 100:\n                return 0\n            S = str(X)\n         \
        \   n = len(S)\n\n            @lru_cache(None)\n            def dp(idx, tight,\
        \ is_leading, last, second_last):\n                if idx == n:\n          \
        \          return 1, 0\n\n                res_count, res_sum = 0, 0\n      \
        \          limit = int(S[idx]) if tight else 9\n\n                for d in range(limit\
        \ + 1):\n                    new_tight = tight and (d == limit)\n          \
        \          new_is_leading = is_leading and (d == 0)\n\n                    wav_inc\
        \ = 0\n                    if not is_leading and second_last != 10:\n      \
        \                  if (second_last < last > d) or (second_last > last < d):\n\
        \                            wav_inc = 1\n\n                    if new_is_leading:\n\
        \                        n_last, n_second = 10, 10\n                    else:\n\
        \                        n_last = d\n                        n_second = 10 if\
        \ is_leading else last\n\n                    cnt, s = dp(idx + 1, new_tight,\
        \ new_is_leading, n_last, n_second)\n                    res_count += cnt\n\
        \                    res_sum += s + cnt * wav_inc\n\n                return\
        \ res_count, res_sum\n\n            return dp(0, True, True, 10, 10)[1]\n\n\
        \        return f(num2) - f(num1 - 1)"
      c: "#include <string.h>\n#include <stdio.h>\n\nstatic long long memo_cnt[20][2][2][11][11];\n\
        static long long memo_sum[20][2][2][11][11];\nstatic char S_buf[25];\nstatic\
        \ int n_val;\n\ntypedef struct {\n    long long cnt;\n    long long sum;\n}\
        \ Result;\n\nResult dp(int idx, int tight, int is_leading, int last, int second_last)\
        \ {\n    if (idx == n_val) {\n        Result r = {1, 0};\n        return r;\n\
        \    }\n    if (memo_cnt[idx][tight][is_leading][last][second_last] != -1) {\n\
        \        Result r = {memo_cnt[idx][tight][is_leading][last][second_last], \n\
        \                    memo_sum[idx][tight][is_leading][last][second_last]};\n\
        \        return r;\n    }\n\n    long long res_count = 0;\n    long long res_sum\
        \ = 0;\n    int limit = tight ? (S_buf[idx] - '0') : 9;\n\n    for (int d =\
        \ 0; d <= limit; d++) {\n        int new_tight = tight && (d == limit);\n  \
        \      int new_is_leading = is_leading && (d == 0);\n\n        int wav_inc =\
        \ 0;\n        if (!is_leading && second_last != 10) {\n            if ((second_last\
        \ < last && last > d) || (second_last > last && last < d)) {\n             \
        \   wav_inc = 1;\n            }\n        }\n\n        int n_last, n_second;\n\
        \        if (new_is_leading) {\n            n_last = 10;\n            n_second\
        \ = 10;\n        } else {\n            n_last = d;\n            n_second = is_leading\
        \ ? 10 : last;\n        }\n\n        Result res = dp(idx + 1, new_tight, new_is_leading,\
        \ n_last, n_second);\n        res_count += res.cnt;\n        res_sum += res.sum\
        \ + res.cnt * wav_inc;\n    }\n\n    memo_cnt[idx][tight][is_leading][last][second_last]\
        \ = res_count;\n    memo_sum[idx][tight][is_leading][last][second_last] = res_sum;\n\
        \    Result r = {res_count, res_sum};\n    return r;\n}\n\nlong long f(long\
        \ long X) {\n    if (X < 100) return 0;\n    sprintf(S_buf, \"%lld\", X);\n\
        \    n_val = strlen(S_buf);\n    memset(memo_cnt, -1, sizeof(memo_cnt));\n \
        \   memset(memo_sum, -1, sizeof(memo_sum));\n    return dp(0, 1, 1, 10, 10).sum;\n\
        }\n\nlong long totalWaviness(long long num1, long long num2) {\n    return f(num2)\
        \ - f(num1 - 1);\n}"
      csharp: "public class Solution {\n    private long[,,,,] memoCnt = new long[20,\
        \ 2, 2, 11, 11];\n    private long[,,,,] memoSum = new long[20, 2, 2, 11, 11];\n\
        \    private string S;\n    private int n;\n\n    private (long cnt, long sum)\
        \ Dp(int idx, bool tight, bool isLeading, int last, int secondLast) {\n    \
        \    if (idx == n) {\n            return (1, 0);\n        }\n\n        int t\
        \ = tight ? 1 : 0;\n        int il = isLeading ? 1 : 0;\n        if (memoCnt[idx,\
        \ t, il, last, secondLast] != -1) {\n            return (memoCnt[idx, t, il,\
        \ last, secondLast], memoSum[idx, t, il, last, secondLast]);\n        }\n\n\
        \        long resCount = 0;\n        long resSum = 0;\n        int limit = tight\
        \ ? (S[idx] - '0') : 9;\n\n        for (int d = 0; d <= limit; d++) {\n    \
        \        bool newTight = tight && (d == limit);\n            bool newIsLeading\
        \ = isLeading && (d == 0);\n\n            long wavInc = 0;\n            if (!isLeading\
        \ && secondLast != 10) {\n                if ((secondLast < last && last > d)\
        \ || (secondLast > last && last < d)) {\n                    wavInc = 1;\n \
        \               }\n            }\n\n            int nextLast, nextSecond;\n\
        \            if (newIsLeading) {\n                nextLast = 10;\n         \
        \       nextSecond = 10;\n            } else {\n                nextLast = d;\n\
        \                nextSecond = isLeading ? 10 : last;\n            }\n\n    \
        \        var (cnt, sum) = Dp(idx + 1, newTight, newIsLeading, nextLast, nextSecond);\n\
        \            resCount += cnt;\n            resSum += sum + cnt * wavInc;\n \
        \       }\n\n        memoCnt[idx, t, il, last, secondLast] = resCount;\n   \
        \     memoSum[idx, t, il, last, secondLast] = resSum;\n        return (resCount,\
        \ resSum);\n    }\n\n    private long F(long X) {\n        if (X < 100) return\
        \ 0;\n        S = X.ToString();\n        n = S.Length;\n\n        for (int i\
        \ = 0; i < 20; i++)\n            for (int j = 0; j < 2; j++)\n             \
        \   for (int k = 0; k < 2; k++)\n                    for (int l = 0; l < 11;\
        \ l++)\n                        for (int m = 0; m < 11; m++) {\n           \
        \                 memoCnt[i, j, k, l, m] = -1;\n                           \
        \ memoSum[i, j, k, l, m] = -1;\n                        }\n\n        return\
        \ Dp(0, true, true, 10, 10).sum;\n    }\n\n    public long TotalWaviness(long\
        \ num1, long num2) {\n        return F(num2) - F(num1 - 1);\n    }\n}"
      javascript: "/**\n * @param {number} num1\n * @param {number} num2\n * @return\
        \ {number}\n */\nvar totalWaviness = function(num1, num2) {\n    const f = (X)\
        \ => {\n        if (X < 100n) return 0n;\n        const S = X.toString();\n\
        \        const n = S.length;\n\n        const memoCnt = Array.from({ length:\
        \ n + 1 }, () =>\n            Array.from({ length: 2 }, () =>\n            \
        \    Array.from({ length: 2 }, () =>\n                    Array.from({ length:\
        \ 11 }, () =>\n                        new BigInt64Array(11).fill(-1n)\n   \
        \                 )\n                )\n            )\n        );\n        const\
        \ memoSum = Array.from({ length: n + 1 }, () =>\n            Array.from({ length:\
        \ 2 }, () =>\n                Array.from({ length: 2 }, () =>\n            \
        \        Array.from({ length: 11 }, () =>\n                        new BigInt64Array(11).fill(-1n)\n\
        \                    )\n                )\n            )\n        );\n\n   \
        \     const dp = (idx, tight, isLeading, last, secondLast) => {\n          \
        \  if (idx === n) return [1n, 0n];\n            const t = tight ? 1 : 0;\n \
        \           const il = isLeading ? 1 : 0;\n\n            if (memoCnt[idx][t][il][last][secondLast]\
        \ !== -1n) {\n                return [memoCnt[idx][t][il][last][secondLast],\
        \ memoSum[idx][t][il][last][secondLast]];\n            }\n\n            let\
        \ totalCount = 0n;\n            let totalSum = 0n;\n            const limit\
        \ = tight ? Number(S[idx]) : 9;\n\n            for (let d = 0; d <= limit; d++)\
        \ {\n                const newTight = tight && (d === limit);\n            \
        \    const newIsLeading = isLeading && (d === 0);\n\n                let wavInc\
        \ = 0n;\n                if (!isLeading && secondLast !== 10) {\n          \
        \          if ((secondLast < last && last > d) || (secondLast > last && last\
        \ < d)) {\n                        wavInc = 1n;\n                    }\n   \
        \             }\n\n                let newLast, newSecond;\n               \
        \ if (newIsLeading) {\n                    newLast = 10;\n                 \
        \   newSecond = 10;\n                } else {\n                    newLast =\
        \ d;\n                    newSecond = isLeading ? 10 : last;\n             \
        \   }\n\n                const [cnt, s] = dp(idx + 1, newTight, newIsLeading,\
        \ newLast, newSecond);\n                totalCount += cnt;\n               \
        \ totalSum += s + cnt * wavInc;\n            }\n\n            memoCnt[idx][t][il][last][secondLast]\
        \ = totalCount;\n            memoSum[idx][t][il][last][secondLast] = totalSum;\n\
        \            return [totalCount, totalSum];\n        };\n\n        return dp(0,\
        \ true, true, 10, 10)[1];\n    };\n\n    const res = f(BigInt(num2)) - f(BigInt(num1)\
        \ - 1n);\n    return Number(res);\n};"
      typescript: "function totalWaviness(num1: number, num2: number): number {\n  \
        \  const countMemo = new BigInt64Array(8228);\n    const sumMemo = new BigInt64Array(8228);\n\
        \n    function solve(n: bigint): bigint {\n        if (n < 0n) return 0n;\n\
        \        const nStr = n.toString();\n        countMemo.fill(-1n);\n        sumMemo.fill(-1n);\n\
        \n        function dp(pos: number, tight: boolean, isLeading: boolean, d1: number,\
        \ d2: number): { count: bigint, sum: bigint } {\n            if (pos === nStr.length)\
        \ {\n                return { count: 1n, sum: 0n };\n            }\n\n     \
        \       const tightVal = tight ? 1 : 0;\n            const leadingVal = isLeading\
        \ ? 1 : 0;\n            const stateIdx = ((((pos * 2 + tightVal) * 2 + leadingVal)\
        \ * 11 + (d1 + 1)) * 11 + (d2 + 1));\n\n            if (countMemo[stateIdx]\
        \ !== -1n) {\n                return { count: countMemo[stateIdx], sum: sumMemo[stateIdx]\
        \ };\n            }\n\n            let resCount = 0n;\n            let resSum\
        \ = 0n;\n            const limit = tight ? parseInt(nStr[pos]) : 9;\n\n    \
        \        for (let d = 0; d <= limit; d++) {\n                const newTight\
        \ = tight && (d === limit);\n                const newIsLeading = isLeading\
        \ && (d === 0);\n\n                let addedWaviness = 0n;\n               \
        \ if (!isLeading && d1 !== -1 && d2 !== -1) {\n                    if ((d2 <\
        \ d1 && d < d1) || (d2 > d1 && d > d1)) {\n                        addedWaviness\
        \ = 1n;\n                    }\n                }\n\n                const res\
        \ = newIsLeading \n                    ? dp(pos + 1, newTight, true, -1, -1)\n\
        \                    : dp(pos + 1, newTight, false, d, d1);\n\n            \
        \    resCount += res.count;\n                resSum += res.sum + (addedWaviness\
        \ * res.count);\n            }\n\n            countMemo[stateIdx] = resCount;\n\
        \            sumMemo[stateIdx] = resSum;\n            return { count: resCount,\
        \ sum: resSum };\n        }\n\n        return dp(0, true, true, -1, -1).sum;\n\
        \    }\n\n    return Number(solve(BigInt(num2)) - solve(BigInt(num1) - 1n));\n\
        }"
      php: "class Solution {\n\n    private $memoCount;\n    private $memoSum;\n\n \
        \   /**\n     * @param Integer $num1\n     * @param Integer $num2\n     * @return\
        \ Integer\n     */\n    function totalWaviness($num1, $num2) {\n        return\
        \ $this->solve($num2) - $this->solve($num1 - 1);\n    }\n\n    private function\
        \ solve($n) {\n        if ($n < 0) return 0;\n        $nStr = (string)$n;\n\
        \        $this->memoCount = [];\n        $this->memoSum = [];\n        $res\
        \ = $this->dp(0, true, true, -1, -1, $nStr);\n        return $res[1];\n    }\n\
        \n    private function dp($pos, $tight, $isLeading, $d1, $d2, $nStr) {\n   \
        \     if ($pos === strlen($nStr)) {\n            return [1, 0];\n        }\n\
        \n        $tightInt = $tight ? 1 : 0;\n        $leadingInt = $isLeading ? 1\
        \ : 0;\n        $key = \"$pos,$tightInt,$leadingInt,$d1,$d2\";\n        if (isset($this->memoCount[$key]))\
        \ {\n            return [$this->memoCount[$key], $this->memoSum[$key]];\n  \
        \      }\n\n        $resCount = 0;\n        $resSum = 0;\n        $limit = $tight\
        \ ? (int)$nStr[$pos] : 9;\n\n        for ($d = 0; $d <= $limit; $d++) {\n  \
        \          $newTight = $tight && ($d === $limit);\n            $newIsLeading\
        \ = $isLeading && ($d === 0);\n\n            $addedWaviness = 0;\n         \
        \   if (!$isLeading && $d1 !== -1 && $d2 !== -1) {\n                if (($d2\
        \ < $d1 && $d < $d1) || ($d2 > $d1 && $d > $d1)) {\n                    $addedWaviness\
        \ = 1;\n                }\n            }\n\n            $res = $newIsLeading\
        \ \n                ? $this->dp($pos + 1, $newTight, true, -1, -1, $nStr)\n\
        \                : $this->dp($pos + 1, $newTight, false, $d, $d1, $nStr);\n\n\
        \            $resCount += $res[0];\n            $resSum += $res[1] + ($addedWaviness\
        \ * $res[0]);\n        }\n\n        $this->memoCount[$key] = $resCount;\n  \
        \      $this->memoSum[$key] = $resSum;\n        return [$resCount, $resSum];\n\
        \    }\n}"
      swift: "class Solution {\n    private var memoCount = [Int64](repeating: -1, count:\
        \ 8228)\n    private var memoSum = [Int64](repeating: -1, count: 8228)\n\n \
        \   func totalWaviness(_ num1: Int, _ num2: Int) -> Int {\n        return Int(solve(Int64(num2))\
        \ - solve(Int64(num1) - 1))\n    }\n\n    private func solve(_ n: Int64) ->\
        \ Int64 {\n        if n < 0 { return 0 }\n        let nStr = String(n).compactMap\
        \ { Int(String($0)) }\n        memoCount = [Int64](repeating: -1, count: 8228)\n\
        \        memoSum = [Int64](repeating: -1, count: 8228)\n        return dp(0,\
        \ true, true, -1, -1, nStr).sum\n    }\n\n    private func dp(_ pos: Int, _\
        \ tight: Bool, _ isLeading: Bool, _ d1: Int, _ d2: Int, _ nStr: [Int]) -> (count:\
        \ Int64, sum: Int64) {\n        if pos == nStr.count {\n            return (1,\
        \ 0)\n        }\n\n        let tightVal = tight ? 1 : 0\n        let leadingVal\
        \ = isLeading ? 1 : 0\n        let stateIdx = ((((pos * 2 + tightVal) * 2 +\
        \ leadingVal) * 11 + (d1 + 1)) * 11 + (d2 + 1))\n\n        if memoCount[stateIdx]\
        \ != -1 {\n            return (memoCount[stateIdx], memoSum[stateIdx])\n   \
        \     }\n\n        var resCount: Int64 = 0\n        var resSum: Int64 = 0\n\
        \        let limit = tight ? nStr[pos] : 9\n\n        for d in 0...limit {\n\
        \            let newTight = tight && (d == limit)\n            let newIsLeading\
        \ = isLeading && (d == 0)\n\n            var addedWaviness: Int64 = 0\n    \
        \        if !isLeading && d1 != -1 && d2 != -1 {\n                if (d2 < d1\
        \ && d < d1) || (d2 > d1 && d > d1) {\n                    addedWaviness = 1\n\
        \                }\n            }\n\n            let res = newIsLeading\n  \
        \              ? dp(pos + 1, newTight, true, -1, -1, nStr)\n               \
        \ : dp(pos + 1, newTight, false, d, d1, nStr)\n\n            resCount += res.count\n\
        \            resSum += res.sum + (addedWaviness * res.count)\n        }\n\n\
        \        memoCount[stateIdx] = resCount\n        memoSum[stateIdx] = resSum\n\
        \        return (resCount, resSum)\n    }\n}"
      kotlin: "class Solution {\n    private val memoCount = LongArray(8228)\n    private\
        \ val memoSum = LongArray(8228)\n    private var nStr: String = \"\"\n\n   \
        \ fun totalWaviness(num1: Long, num2: Long): Long {\n        return solve(num2)\
        \ - solve(num1 - 1)\n    }\n\n    private fun solve(n: Long): Long {\n     \
        \   if (n < 0) return 0L\n        nStr = n.toString()\n        memoCount.fill(-1L)\n\
        \        memoSum.fill(-1L)\n        return dp(0, true, true, -1, -1).second\n\
        \    }\n\n    private fun dp(pos: Int, tight: Boolean, isLeading: Boolean, d1:\
        \ Int, d2: Int): Pair<Long, Long> {\n        if (pos == nStr.length) {\n   \
        \         return Pair(1L, 0L)\n        }\n\n        val tightVal = if (tight)\
        \ 1 else 0\n        val leadingVal = if (isLeading) 1 else 0\n        val stateIdx\
        \ = ((((pos * 2 + tightVal) * 2 + leadingVal) * 11 + (d1 + 1)) * 11 + (d2 +\
        \ 1))\n\n        if (memoCount[stateIdx] != -1L) {\n            return Pair(memoCount[stateIdx],\
        \ memoSum[stateIdx])\n        }\n\n        var resCount = 0L\n        var resSum\
        \ = 0L\n        val limit = if (tight) nStr[pos] - '0' else 9\n\n        for\
        \ (d in 0..limit) {\n            val newTight = tight && (d == limit)\n    \
        \        val newIsLeading = isLeading && (d == 0)\n\n            var addedWaviness\
        \ = 0L\n            if (!isLeading && d1 != -1 && d2 != -1) {\n            \
        \    if ((d2 < d1 && d < d1) || (d2 > d1 && d > d1)) {\n                   \
        \ addedWaviness = 1L\n                }\n            }\n\n            val res\
        \ = if (newIsLeading) {\n                dp(pos + 1, newTight, true, -1, -1)\n\
        \            } else {\n                dp(pos + 1, newTight, false, d, d1)\n\
        \            }\n\n            resCount += res.first\n            resSum += res.second\
        \ + (addedWaviness * res.first)\n        }\n\n        memoCount[stateIdx] =\
        \ resCount\n        memoSum[stateIdx] = resSum\n        return Pair(resCount,\
        \ resSum)\n    }\n}"
      dart: "class Result {\n  final int count;\n  final int waviness;\n  Result(this.count,\
        \ this.waviness);\n}\n\nclass Solution {\n  int totalWaviness(int num1, int\
        \ num2) {\n    return _solve(num2) - _solve(num1 - 1);\n  }\n\n  int _solve(int\
        \ n) {\n    if (n < 0) return 0;\n    String s = n.toString();\n    List<int>\
        \ digits = s.split('').map(int.parse).toList();\n    List<Result?> memo = List.filled(20\
        \ * 2 * 2 * 11 * 11, null);\n\n    Result dp(int pos, bool tight, bool leading,\
        \ int last, int secLast) {\n      if (pos == digits.length) {\n        return\
        \ Result(1, 0);\n      }\n      int tIdx = tight ? 1 : 0;\n      int lIdx =\
        \ leading ? 1 : 0;\n      int idx = (((pos * 2 + tIdx) * 2 + lIdx) * 11 + last)\
        \ * 11 + secLast;\n      if (memo[idx] != null) return memo[idx]!;\n\n     \
        \ int count = 0;\n      int waviness = 0;\n      int limit = tight ? digits[pos]\
        \ : 9;\n\n      for (int d = 0; d <= limit; d++) {\n        bool nextTight =\
        \ tight && (d == limit);\n        bool nextLeading = leading && (d == 0);\n\
        \        int delta = 0;\n        if (!leading && secLast != 10) {\n        \
        \  if ((last > secLast && last > d) || (last < secLast && last < d)) {\n   \
        \         delta = 1;\n          }\n        }\n\n        int nextLast = 10;\n\
        \        int nextSecLast = 10;\n        if (!nextLeading) {\n          nextLast\
        \ = d;\n          nextSecLast = last;\n        }\n\n        Result res = dp(pos\
        \ + 1, nextTight, nextLeading, nextLast, nextSecLast);\n        count += res.count;\n\
        \        waviness += res.waviness + delta * res.count;\n      }\n\n      memo[idx]\
        \ = Result(count, waviness);\n      return memo[idx]!;\n    }\n\n    return\
        \ dp(0, true, true, 10, 10).waviness;\n  }\n}"
      go: "import (\n\t\"strconv\"\n)\n\ntype Result struct {\n\tcount    int64\n\t\
        waviness int64\n}\n\nfunc totalWaviness(num1 int64, num2 int64) int64 {\n\t\
        return solve(num2) - solve(num1-1)\n}\n\nfunc solve(n int64) int64 {\n\tif n\
        \ < 0 {\n\t\treturn 0\n\t}\n\ts := strconv.FormatInt(n, 10)\n\tdigits := make([]int,\
        \ len(s))\n\tfor i, r := range s {\n\t\tdigits[i] = int(r - '0')\n\t}\n\n\t\
        memoCount := make([]int64, 20*2*2*11*11)\n\tmemoWaviness := make([]int64, 20*2*2*11*11)\n\
        \tfor i := range memoCount {\n\t\tmemoCount[i] = -1\n\t}\n\n\tvar dp func(int,\
        \ bool, bool, int, int) Result\n\tdp = func(pos int, tight, leading bool, last,\
        \ secLast int) Result {\n\t\tif pos == len(digits) {\n\t\t\treturn Result{1,\
        \ 0}\n\t\t}\n\t\ttIdx, lIdx := 0, 0\n\t\tif tight {\n\t\t\ttIdx = 1\n\t\t}\n\
        \t\tif leading {\n\t\t\tlIdx = 1\n\t\t}\n\t\tidx := (((pos*2+tIdx)*2+lIdx)*11+last)*11\
        \ + secLast\n\t\tif memoCount[idx] != -1 {\n\t\t\treturn Result{memoCount[idx],\
        \ memoWaviness[idx]}\n\t\t}\n\n\t\tvar count, waviness int64\n\t\tlimit := 9\n\
        \t\tif tight {\n\t\t\tlimit = digits[pos]\n\t\t}\n\n\t\tfor d := 0; d <= limit;\
        \ d++ {\n\t\t\tnextTight := tight && (d == limit)\n\t\t\tnextLeading := leading\
        \ && (d == 0)\n\n\t\t\tdelta := int64(0)\n\t\t\tif !leading && secLast != 10\
        \ {\n\t\t\t\tif (last > secLast && last > d) || (last < secLast && last < d)\
        \ {\n\t\t\t\t\tdelta = 1\n\t\t\t\t}\n\t\t\t}\n\n\t\t\tnextLast, nextSecLast\
        \ := 10, 10\n\t\t\tif !nextLeading {\n\t\t\t\tnextLast, nextSecLast = d, last\n\
        \t\t\t}\n\n\t\t\tres := dp(pos+1, nextTight, nextLeading, nextLast, nextSecLast)\n\
        \t\t\tcount += res.count\n\t\t\twaviness += res.waviness + delta*res.count\n\
        \t\t}\n\n\t\tmemoCount[idx] = count\n\t\tmemoWaviness[idx] = waviness\n\t\t\
        return Result{count, waviness}\n\t}\n\n\treturn dp(0, true, true, 10, 10).waviness\n\
        }"
      ruby: "def total_waviness(num1, num2)\n  solve(num2) - solve(num1 - 1)\nend\n\n\
        def solve(n)\n  return 0 if n < 0\n  digits = n.to_s.chars.map(&:to_i)\n  memo\
        \ = {}\n\n  dp = lambda do |pos, tight, leading, last, sec_last|\n    state\
        \ = [pos, tight, leading, last, sec_last]\n    return memo[state] if memo.key?(state)\n\
        \n    if pos == digits.length\n      return [1, 0]\n    end\n\n    count = 0\n\
        \    waviness = 0\n    limit = tight ? digits[pos] : 9\n\n    (0..limit).each\
        \ do |d|\n      next_tight = tight && (d == limit)\n      next_leading = leading\
        \ && (d == 0)\n\n      delta = 0\n      if !leading && sec_last != 10\n    \
        \    if (last > sec_last && last > d) || (last < sec_last && last < d)\n   \
        \       delta = 1\n        end\n      end\n\n      next_last = 10\n      next_sec_last\
        \ = 10\n      unless next_leading\n        next_last = d\n        next_sec_last\
        \ = last\n      end\n\n      res = dp.call(pos + 1, next_tight, next_leading,\
        \ next_last, next_sec_last)\n      count += res[0]\n      waviness += res[1]\
        \ + delta * res[0]\n    end\n\n    memo[state] = [count, waviness]\n  end\n\n\
        \  dp.call(0, true, true, 10, 10)[1]\nend"
      scala: "object Solution {\n    def totalWaviness(num1: Long, num2: Long): Long\
        \ = {\n        solve(num2) - solve(num1 - 1)\n    }\n\n    def solve(n: Long):\
        \ Long = {\n        if (n < 0) return 0\n        val digits = n.toString.map(_.asDigit).toArray\n\
        \        val memoCount = Array.fill(20 * 2 * 2 * 11 * 11)(-1L)\n        val\
        \ memoWaviness = Array.fill(20 * 2 * 2 * 11 * 11)(-1L)\n\n        def dp(pos:\
        \ Int, tight: Boolean, leading: Boolean, last: Int, secLast: Int): (Long, Long)\
        \ = {\n            if (pos == digits.length) {\n                return (1L,\
        \ 0L)\n            }\n            val tIdx = if (tight) 1 else 0\n         \
        \   val lIdx = if (leading) 1 else 0\n            val idx = (((pos * 2 + tIdx)\
        \ * 2 + lIdx) * 11 + last) * 11 + secLast\n            if (memoCount(idx) !=\
        \ -1L) return (memoCount(idx), memoWaviness(idx))\n\n            var count =\
        \ 0L\n            var waviness = 0L\n            val limit = if (tight) digits(pos)\
        \ else 9\n\n            var d = 0\n            while (d <= limit) {\n      \
        \          val nextTight = tight && (d == limit)\n                val nextLeading\
        \ = leading && (d == 0)\n                var delta = 0L\n                if\
        \ (!leading && secLast != 10) {\n                    if ((last > secLast &&\
        \ last > d) || (last < secLast && last < d)) {\n                        delta\
        \ = 1L\n                    }\n                }\n\n                var nextLast\
        \ = 10\n                var nextSecLast = 10\n                if (!nextLeading)\
        \ {\n                    nextLast = d\n                    nextSecLast = last\n\
        \                }\n\n                val res = dp(pos + 1, nextTight, nextLeading,\
        \ nextLast, nextSecLast)\n                count += res._1\n                waviness\
        \ += res._2 + delta * res._1\n                d += 1\n            }\n\n    \
        \        memoCount(idx) = count\n            memoWaviness(idx) = waviness\n\
        \            (count, waviness)\n        }\n\n        dp(0, true, true, 10, 10)._2\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn total_waviness(num1: i64, num2: i64) -> i64\
        \ {\n        fn solve(num: i64) -> i64 {\n            if num <= 0 {\n      \
        \          return 0;\n            }\n            let s = num.to_string();\n\
        \            let digits: Vec<i32> = s.chars().map(|c| c.to_digit(10).unwrap()\
        \ as i32).collect();\n            let n = digits.len();\n            let mut\
        \ memo = vec![vec![vec![vec![vec![None; 11]; 11]; 2]; 2]; n + 1];\n        \
        \    dp(0, true, false, 10, 10, &digits, &mut memo).1\n        }\n\n       \
        \ fn dp(\n            pos: usize,\n            tight: bool,\n            started:\
        \ bool,\n            p1: i32,\n            p2: i32,\n            digits: &Vec<i32>,\n\
        \            memo: &mut Vec<Vec<Vec<Vec<Vec<Option<(i64, i64)>>>>>>,\n     \
        \   ) -> (i64, i64) {\n            if pos == digits.len() {\n              \
        \  return (1, 0);\n            }\n            if let Some(res) = memo[pos][tight\
        \ as usize][started as usize][p1 as usize][p2 as usize] {\n                return\
        \ res;\n            }\n\n            let mut total_cnt: i64 = 0;\n         \
        \   let mut total_wav: i64 = 0;\n            let limit = if tight { digits[pos]\
        \ } else { 9 };\n\n            for d in 0..=limit {\n                let new_tight\
        \ = tight && (d == limit);\n                let mut is_wav = 0;\n          \
        \      let (new_started, new_p1, new_p2) = if !started {\n                 \
        \   if d == 0 {\n                        (false, 10, 10)\n                 \
        \   } else {\n                        (true, d, 10)\n                    }\n\
        \                } else {\n                    if p2 != 10 {\n             \
        \           if (p1 > p2 && p1 > d) || (p1 < p2 && p1 < d) {\n              \
        \              is_wav = 1;\n                        }\n                    }\n\
        \                    (true, d, p1)\n                };\n\n                let\
        \ (cnt, wav) = dp(pos + 1, new_tight, new_started, new_p1, new_p2, digits, memo);\n\
        \                total_cnt += cnt;\n                total_wav += wav + (is_wav\
        \ as i64) * cnt;\n            }\n\n            memo[pos][tight as usize][started\
        \ as usize][p1 as usize][p2 as usize] = Some((total_cnt, total_wav));\n    \
        \        (total_cnt, total_wav)\n        }\n\n        solve(num2) - solve(num1\
        \ - 1)\n    }\n}"
      racket: "(define/contract (total-waviness num1 num2)\n  (-> exact-integer? exact-integer?\
        \ exact-integer?)\n  (define (solve n)\n    (if (<= n 0)\n        0\n      \
        \  (let* ([s (number->string n)]\n               [digits (list->vector (map\
        \ (lambda (c) (- (char->integer c) (char->integer #\\0))) (string->list s)))]\n\
        \               [len (vector-length digits)]\n               [memo (make-hash)])\n\
        \          (letrec ([dp (lambda (pos tight started p1 p2)\n                \
        \         (let ([key (list pos tight started p1 p2)])\n                    \
        \       (cond\n                             [(hash-has-key? memo key) (hash-ref\
        \ memo key)]\n                             [(= pos len) (cons 1 0)]\n      \
        \                       [else\n                              (let* ([limit (if\
        \ tight (vector-ref digits pos) 9)]\n                                     [res\
        \ (for/fold ([acc (cons 0 0)])\n                                           \
        \         ([d (in-range (+ limit 1))])\n                                   \
        \         (let* ([new-tight (and tight (= d limit))]\n                     \
        \                              [is-wav (if (and started (not (= p2 10))\n  \
        \                                                                  (or (and\
        \ (> p1 p2) (> p1 d))\n                                                    \
        \                    (and (< p1 p2) (< p1 d))))\n                          \
        \                                     1 0)]\n                              \
        \                     [new-params (if (not started)\n                      \
        \                                             (if (= d 0) (list #f 10 10) (list\
        \ #t d 10))\n                                                              \
        \     (list #t d p1))]\n                                                   [next-res\
        \ (dp (+ pos 1) new-tight (car new-params) (cadr new-params) (caddr new-params))])\n\
        \                                              (cons (+ (car acc) (car next-res))\n\
        \                                                    (+ (cdr acc) (cdr next-res)\
        \ (* is-wav (car next-res))))))])\n                                (hash-set!\
        \ memo key res)\n                                res)])))])\n            (cdr\
        \ (dp 0 #t #f 10 10))))))\n  (- (solve num2) (solve (- num1 1))))"
      erlang: "-spec total_waviness(Num1 :: integer(), Num2 :: integer()) -> integer().\n\
        total_waviness(Num1, Num2) ->\n  solve(Num2) - solve(Num1 - 1).\n\nsolve(Num)\
        \ ->\n  if Num =< 0 -> 0;\n     true ->\n       DigitsList = [D - $0 || D <-\
        \ integer_to_list(Num)],\n       DigitsTuple = list_to_tuple(DigitsList),\n\
        \       L = tuple_size(DigitsTuple),\n       {_, Wav, _} = dp(0, true, false,\
        \ 10, 10, DigitsTuple, L, #{}),\n       Wav\n  end.\n\ndp(Pos, Tight, Started,\
        \ P1, P2, DigitsTuple, L, Memo) ->\n  Key = {Pos, Tight, Started, P1, P2},\n\
        \  case maps:find(Key, Memo) of\n    {ok, {Cnt, Wav}} -> {Cnt, Wav, Memo};\n\
        \    error ->\n      if Pos == L -> {1, 0, Memo};\n         true ->\n      \
        \     Limit = if Tight -> element(Pos + 1, DigitsTuple); true -> 9 end,\n  \
        \         {TCnt, TWav, TMemo} = \n             lists:foldl(fun(D, {AccCnt, AccWav,\
        \ M}) ->\n               NTight = Tight andalso (D == Limit),\n            \
        \   {NStarted, NP1, NP2, IsWav} =\n                 if not Started ->\n    \
        \                if D == 0 -> {false, 10, 10, 0};\n                       true\
        \ -> {true, D, 10, 0}\n                    end;\n                 true ->\n\
        \                    W = if (P2 /= 10) andalso (((P1 > P2) andalso (P1 > D))\
        \ orelse ((P1 < P2) andalso (P1 < D))) -> 1;\n                           true\
        \ -> 0\n                        end,\n                    {true, D, P1, W}\n\
        \                 end,\n               {Cnt, Wav, NM} = dp(Pos + 1, NTight,\
        \ NStarted, NP1, NP2, DigitsTuple, L, M),\n               {AccCnt + Cnt, AccWav\
        \ + Wav + IsWav * Cnt, NM}\n             end, {0, 0, Memo}, lists:seq(0, Limit)),\n\
        \           {TCnt, TWav, maps:put(Key, {TCnt, TWav}, TMemo)}\n      end\n  end."
      elixir: "defmodule Solution do\n  @spec total_waviness(num1 :: integer, num2 ::\
        \ integer) :: integer\n  def total_waviness(num1, num2) do\n    solve(num2)\
        \ - solve(num1 - 1)\n  end\n\n  defp solve(num) do\n    if num <= 0 do\n   \
        \   0\n    else\n      digits_list = Integer.to_string(num) |> String.to_charlist()\
        \ |> Enum.map(&(&1 - ?0))\n      digits_tuple = List.to_tuple(digits_list)\n\
        \      l = tuple_size(digits_tuple)\n      {{_cnt, wav}, _memo} = dp(0, true,\
        \ false, 10, 10, digits_tuple, l, %{})\n      wav\n    end\n  end\n\n  defp\
        \ dp(pos, tight, started, p1, p2, digits_tuple, l, memo) do\n    key = {pos,\
        \ tight, started, p1, p2}\n    if Map.has_key?(memo, key) do\n      {Map.get(memo,\
        \ key), memo}\n    else\n      if pos == l do\n        {{1, 0}, memo}\n    \
        \  else\n        limit = if tight, do: elem(digits_tuple, pos), else: 9\n  \
        \      {total_cnt, total_wav, final_memo} = \n          Enum.reduce(0..limit,\
        \ {0, 0, memo}, fn d, {acc_cnt, acc_wav, current_memo} ->\n            new_tight\
        \ = tight and (d == limit)\n            {new_started, new_p1, new_p2, is_wav}\
        \ = \n              if not started do\n                if d == 0, do: {false,\
        \ 10, 10, 0}, else: {true, d, 10, 0}\n              else\n                w\
        \ = if p2 != 10 and ((p1 > p2 and p1 > d) or (p1 < p2 and p1 < d)), do: 1, else:\
        \ 0\n                {true, d, p1, w}\n              end\n            {{cnt,\
        \ wav}, next_memo} = dp(pos + 1, new_tight, new_started, new_p1, new_p2, digits_tuple,\
        \ l, current_memo)\n            {acc_cnt + cnt, acc_wav + wav + is_wav * cnt,\
        \ next_memo}\n          end)\n        res = {total_cnt, total_wav}\n       \
        \ {res, Map.put(final_memo, key, res)}\n      end\n    end\n  end\nend"
    approach: 'The problem asks for the total waviness of all numbers in a range, where
      waviness is the count of peaks and valleys. This can be solved using digit dynamic
      programming. We define a function `countWaviness(n)` that returns the total waviness
      of all integers in the range $[0, n]$. The result for the range $[num1, num2]$
      is then `countWaviness(num2) - countWaviness(num1 - 1)`. The digit DP state is
      defined as `(pos, tight, isLeading, last1, last2)`, where `pos` is the current
      digit index, `tight` is a flag for the upper bound restriction, `isLeading` handles
      leading zeros, `last1` is the digit at `pos-1`, and `last2` is the digit at `pos-2`.
      To compute the total sum of waviness, each state returns a pair: the total waviness
      sum of all numbers formed from that point and the total count of valid numbers
      formed.


      During transition, we iterate through all possible digits $d$ for the current
      position. A peak or valley is identified at position `pos-1` if the digits `last2`,
      `last1`, and $d$ satisfy the strictly greater-than (peak) or strictly less-than
      (valley) condition. If such a condition is met, the contribution to the total
      waviness is the number of valid ways to complete the number from the next position.
      The `isLeading` state ensures that we only begin counting peaks and valleys once
      at least two digits of a number have been placed. This approach efficiently counts
      waviness across the range by aggregating results from overlapping subproblems
      stored in a memoization table.'
    time_complexity: O(L * D^3), where L is the maximum number of digits (log10 of num2)
      and D is the base (10). The state space size is L * 2 * 2 * 11 * 11, and each
      state involves a transition loop of size D.
    space_complexity: O(L * D^2), where L is the maximum number of digits and D is the
      base (10). This space is used to store the memoization table for the DP states.
    elapsed_time: 440.6523370742798
    model: gemini-3-flash-preview
    generated_at: '2026-06-05 02:49:56 '
---

## Problem #3753: Total Waviness of Numbers in Range II

**Difficulty:** Hard

**Topics:** Math, Dynamic Programming

## Problem Description

<p>You are given two integers <code>num1</code> and <code>num2</code> representing an <strong>inclusive</strong> range <code>[num1, num2]</code>.</p>

<p>The <strong>waviness</strong> of a number is defined as the total count of its <strong>peaks</strong> and <strong>valleys</strong>:</p>

<ul>
	<li>A digit is a <strong>peak</strong> if it is <strong>strictly greater</strong> than both of its immediate neighbors.</li>
	<li>A digit is a <strong>valley</strong> if it is <strong>strictly less</strong> than both of its immediate neighbors.</li>
	<li>The first and last digits of a number <strong>cannot</strong> be peaks or valleys.</li>
	<li>Any number with fewer than 3 digits has a waviness of 0.</li>
</ul>
Return the total sum of waviness for all numbers in the range <code>[num1, num2]</code>.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">num1 = 120, num2 = 130</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>In the range <code>[120, 130]</code>:</p>

<ul>
	<li><code>120</code>: middle digit 2 is a peak, waviness = 1.</li>
	<li><code>121</code>: middle digit 2 is a peak, waviness = 1.</li>
	<li><code>130</code>: middle digit 3 is a peak, waviness = 1.</li>
	<li>All other numbers in the range have a waviness of 0.</li>
</ul>

<p>Thus, total waviness is <code>1 + 1 + 1 = 3</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">num1 = 198, num2 = 202</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>In the range <code>[198, 202]</code>:</p>

<ul>
	<li><code>198</code>: middle digit 9 is a peak, waviness = 1.</li>
	<li><code>201</code>: middle digit 0 is a valley, waviness = 1.</li>
	<li><code>202</code>: middle digit 0 is a valley, waviness = 1.</li>
	<li>All other numbers in the range have a waviness of 0.</li>
</ul>

<p>Thus, total waviness is <code>1 + 1 + 1 = 3</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">num1 = 4848, num2 = 4848</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>Number <code>4848</code>: the second digit 8 is a peak, and the third digit 4 is a valley, giving a waviness of 2.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num1 &lt;= num2 &lt;= 10<sup>15</sup></code>​​​​​​​</li>
</ul>


## Hints

1. Use digit dynamic programming

2. Build a digit-DP state `(position, tight, lastDigit, secondLastDigit)`

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the total waviness of all numbers in a range, where waviness is the count of peaks and valleys. This can be solved using digit dynamic programming. We define a function `countWaviness(n)` that returns the total waviness of all integers in the range $[0, n]$. The result for the range $[num1, num2]$ is then `countWaviness(num2) - countWaviness(num1 - 1)`. The digit DP state is defined as `(pos, tight, isLeading, last1, last2)`, where `pos` is the current digit index, `tight` is a flag for the upper bound restriction, `isLeading` handles leading zeros, `last1` is the digit at `pos-1`, and `last2` is the digit at `pos-2`. To compute the total sum of waviness, each state returns a pair: the total waviness sum of all numbers formed from that point and the total count of valid numbers formed.

During transition, we iterate through all possible digits $d$ for the current position. A peak or valley is identified at position `pos-1` if the digits `last2`, `last1`, and $d$ satisfy the strictly greater-than (peak) or strictly less-than (valley) condition. If such a condition is met, the contribution to the total waviness is the number of valid ways to complete the number from the next position. The `isLeading` state ensures that we only begin counting peaks and valleys once at least two digits of a number have been placed. This approach efficiently counts waviness across the range by aggregating results from overlapping subproblems stored in a memoization table.

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
    struct Result {
        long long w, c;
    };
    Result memo[20][2][2][11][11];
    string S;

    Result dfs(int pos, bool tight, bool isLeading, int last1, int last2) {
        if (pos == S.size()) return {0, 1};
        if (memo[pos][tight][isLeading][last1][last2].w != -1) 
            return memo[pos][tight][isLeading][last1][last2];

        long long totalW = 0, totalC = 0;
        int limit = tight ? S[pos] - '0' : 9;
        for (int d = 0; d <= limit; ++d) {
            bool nextTight = tight && (d == limit);
            bool nextIsLeading = isLeading && (d == 0);
            int nextLast1 = nextIsLeading ? 10 : d;
            int nextLast2 = isLeading ? 10 : last1;

            bool isWV = (!isLeading && last2 != 10 && ((last2 < last1 && last1 > d) || (last2 > last1 && last1 < d)));
            Result res = dfs(pos + 1, nextTight, nextIsLeading, nextLast1, nextLast2);
            totalW += res.w + (isWV ? res.c : 0);
            totalC += res.c;
        }
        return memo[pos][tight][isLeading][last1][last2] = {totalW, totalC};
    }

    long long countWaviness(long long n) {
        if (n < 100) return 0;
        S = to_string(n);
        for (int a=0; a<20; ++a) for (int b=0; b<2; ++b) for (int c=0; c<2; ++c) 
            for (int d=0; d<11; ++d) for (int e=0; e<11; ++e) memo[a][b][c][d][e] = {-1, -1};
        return dfs(0, true, true, 10, 10).w;
    }

public:
    long long totalWaviness(long long num1, long long num2) {
        return countWaviness(num2) - countWaviness(num1 - 1);
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    long[][][][][] memoW;
    long[][][][][] memoC;
    String S;

    private long[] dfs(int pos, int tight, int isLeading, int last1, int last2) {
        if (pos == S.length()) return new long[]{0, 1};
        if (memoW[pos][tight][isLeading][last1][last2] != -1)
            return new long[]{memoW[pos][tight][isLeading][last1][last2], memoC[pos][tight][isLeading][last1][last2]};

        long totalW = 0, totalC = 0;
        int limit = tight == 1 ? S.charAt(pos) - '0' : 9;

        for (int d = 0; d <= limit; d++) {
            int nextTight = (tight == 1 && d == limit) ? 1 : 0;
            int nextIsLeading = (isLeading == 1 && d == 0) ? 1 : 0;
            int nextLast1 = nextIsLeading == 1 ? 10 : d;
            int nextLast2 = isLeading == 1 ? 10 : last1;

            boolean isWV = (isLeading == 0 && last2 != 10 && ((last2 < last1 && last1 > d) || (last2 > last1 && last1 < d)));
            long[] res = dfs(pos + 1, nextTight, nextIsLeading, nextLast1, nextLast2);
            totalW += res[0] + (isWV ? res[1] : 0);
            totalC += res[1];
        }

        memoW[pos][tight][isLeading][last1][last2] = totalW;
        memoC[pos][tight][isLeading][last1][last2] = totalC;
        return new long[]{totalW, totalC};
    }

    private long countWaviness(long n) {
        if (n < 100) return 0;
        S = String.valueOf(n);
        int len = S.length();
        memoW = new long[len + 1][2][2][11][11];
        memoC = new long[len + 1][2][2][11][11];
        for (int i = 0; i <= len; i++)
            for (int j = 0; j < 2; j++)
                for (int k = 0; k < 2; k++)
                    for (int l = 0; l < 11; l++)
                        for (int m = 0; m < 11; m++)
                            memoW[i][j][k][l][m] = -1;

        return dfs(0, 1, 1, 10, 10)[0];
    }

    public long totalWaviness(long num1, long num2) {
        return countWaviness(num2) - countWaviness(num1 - 1);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import functools

class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        def count_waviness(n):
            if n < 100: return 0
            s = str(n)

            @functools.lru_cache(None)
            def dp(pos, tight, is_leading, last1, last2):
                if pos == len(s):
                    return 0, 1

                res_w, res_c = 0, 0
                limit = int(s[pos]) if tight else 9

                for d in range(limit + 1):
                    nt = tight and (d == limit)
                    nl = is_leading and (d == 0)
                    n1 = 10 if nl else d
                    n2 = 10 if is_leading else last1

                    is_wv = False
                    if not is_leading and last2 != 10:
                        if (last2 < last1 and last1 > d) or (last2 > last1 and last1 < d):
                            is_wv = True

                    w, c = dp(pos + 1, nt, nl, n1, n2)
                    res_w += w + (c if is_wv else 0)
                    res_c += c
                return res_w, res_c

            return dp(0, True, True, 10, 10)[0]

        return count_waviness(num2) - count_waviness(num1 - 1)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        import sys
        from functools import lru_cache
        sys.setrecursionlimit(2000)

        def f(X: int) -> int:
            if X < 100:
                return 0
            S = str(X)
            n = len(S)

            @lru_cache(None)
            def dp(idx, tight, is_leading, last, second_last):
                if idx == n:
                    return 1, 0

                res_count, res_sum = 0, 0
                limit = int(S[idx]) if tight else 9

                for d in range(limit + 1):
                    new_tight = tight and (d == limit)
                    new_is_leading = is_leading and (d == 0)

                    wav_inc = 0
                    if not is_leading and second_last != 10:
                        if (second_last < last > d) or (second_last > last < d):
                            wav_inc = 1

                    if new_is_leading:
                        n_last, n_second = 10, 10
                    else:
                        n_last = d
                        n_second = 10 if is_leading else last

                    cnt, s = dp(idx + 1, new_tight, new_is_leading, n_last, n_second)
                    res_count += cnt
                    res_sum += s + cnt * wav_inc

                return res_count, res_sum

            return dp(0, True, True, 10, 10)[1]

        return f(num2) - f(num1 - 1)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <string.h>
#include <stdio.h>

static long long memo_cnt[20][2][2][11][11];
static long long memo_sum[20][2][2][11][11];
static char S_buf[25];
static int n_val;

typedef struct {
    long long cnt;
    long long sum;
} Result;

Result dp(int idx, int tight, int is_leading, int last, int second_last) {
    if (idx == n_val) {
        Result r = {1, 0};
        return r;
    }
    if (memo_cnt[idx][tight][is_leading][last][second_last] != -1) {
        Result r = {memo_cnt[idx][tight][is_leading][last][second_last], 
                    memo_sum[idx][tight][is_leading][last][second_last]};
        return r;
    }

    long long res_count = 0;
    long long res_sum = 0;
    int limit = tight ? (S_buf[idx] - '0') : 9;

    for (int d = 0; d <= limit; d++) {
        int new_tight = tight && (d == limit);
        int new_is_leading = is_leading && (d == 0);

        int wav_inc = 0;
        if (!is_leading && second_last != 10) {
            if ((second_last < last && last > d) || (second_last > last && last < d)) {
                wav_inc = 1;
            }
        }

        int n_last, n_second;
        if (new_is_leading) {
            n_last = 10;
            n_second = 10;
        } else {
            n_last = d;
            n_second = is_leading ? 10 : last;
        }

        Result res = dp(idx + 1, new_tight, new_is_leading, n_last, n_second);
        res_count += res.cnt;
        res_sum += res.sum + res.cnt * wav_inc;
    }

    memo_cnt[idx][tight][is_leading][last][second_last] = res_count;
    memo_sum[idx][tight][is_leading][last][second_last] = res_sum;
    Result r = {res_count, res_sum};
    return r;
}

long long f(long long X) {
    if (X < 100) return 0;
    sprintf(S_buf, "%lld", X);
    n_val = strlen(S_buf);
    memset(memo_cnt, -1, sizeof(memo_cnt));
    memset(memo_sum, -1, sizeof(memo_sum));
    return dp(0, 1, 1, 10, 10).sum;
}

long long totalWaviness(long long num1, long long num2) {
    return f(num2) - f(num1 - 1);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    private long[,,,,] memoCnt = new long[20, 2, 2, 11, 11];
    private long[,,,,] memoSum = new long[20, 2, 2, 11, 11];
    private string S;
    private int n;

    private (long cnt, long sum) Dp(int idx, bool tight, bool isLeading, int last, int secondLast) {
        if (idx == n) {
            return (1, 0);
        }

        int t = tight ? 1 : 0;
        int il = isLeading ? 1 : 0;
        if (memoCnt[idx, t, il, last, secondLast] != -1) {
            return (memoCnt[idx, t, il, last, secondLast], memoSum[idx, t, il, last, secondLast]);
        }

        long resCount = 0;
        long resSum = 0;
        int limit = tight ? (S[idx] - '0') : 9;

        for (int d = 0; d <= limit; d++) {
            bool newTight = tight && (d == limit);
            bool newIsLeading = isLeading && (d == 0);

            long wavInc = 0;
            if (!isLeading && secondLast != 10) {
                if ((secondLast < last && last > d) || (secondLast > last && last < d)) {
                    wavInc = 1;
                }
            }

            int nextLast, nextSecond;
            if (newIsLeading) {
                nextLast = 10;
                nextSecond = 10;
            } else {
                nextLast = d;
                nextSecond = isLeading ? 10 : last;
            }

            var (cnt, sum) = Dp(idx + 1, newTight, newIsLeading, nextLast, nextSecond);
            resCount += cnt;
            resSum += sum + cnt * wavInc;
        }

        memoCnt[idx, t, il, last, secondLast] = resCount;
        memoSum[idx, t, il, last, secondLast] = resSum;
        return (resCount, resSum);
    }

    private long F(long X) {
        if (X < 100) return 0;
        S = X.ToString();
        n = S.Length;

        for (int i = 0; i < 20; i++)
            for (int j = 0; j < 2; j++)
                for (int k = 0; k < 2; k++)
                    for (int l = 0; l < 11; l++)
                        for (int m = 0; m < 11; m++) {
                            memoCnt[i, j, k, l, m] = -1;
                            memoSum[i, j, k, l, m] = -1;
                        }

        return Dp(0, true, true, 10, 10).sum;
    }

    public long TotalWaviness(long num1, long num2) {
        return F(num2) - F(num1 - 1);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} num1
 * @param {number} num2
 * @return {number}
 */
var totalWaviness = function(num1, num2) {
    const f = (X) => {
        if (X < 100n) return 0n;
        const S = X.toString();
        const n = S.length;

        const memoCnt = Array.from({ length: n + 1 }, () =>
            Array.from({ length: 2 }, () =>
                Array.from({ length: 2 }, () =>
                    Array.from({ length: 11 }, () =>
                        new BigInt64Array(11).fill(-1n)
                    )
                )
            )
        );
        const memoSum = Array.from({ length: n + 1 }, () =>
            Array.from({ length: 2 }, () =>
                Array.from({ length: 2 }, () =>
                    Array.from({ length: 11 }, () =>
                        new BigInt64Array(11).fill(-1n)
                    )
                )
            )
        );

        const dp = (idx, tight, isLeading, last, secondLast) => {
            if (idx === n) return [1n, 0n];
            const t = tight ? 1 : 0;
            const il = isLeading ? 1 : 0;

            if (memoCnt[idx][t][il][last][secondLast] !== -1n) {
                return [memoCnt[idx][t][il][last][secondLast], memoSum[idx][t][il][last][secondLast]];
            }

            let totalCount = 0n;
            let totalSum = 0n;
            const limit = tight ? Number(S[idx]) : 9;

            for (let d = 0; d <= limit; d++) {
                const newTight = tight && (d === limit);
                const newIsLeading = isLeading && (d === 0);

                let wavInc = 0n;
                if (!isLeading && secondLast !== 10) {
                    if ((secondLast < last && last > d) || (secondLast > last && last < d)) {
                        wavInc = 1n;
                    }
                }

                let newLast, newSecond;
                if (newIsLeading) {
                    newLast = 10;
                    newSecond = 10;
                } else {
                    newLast = d;
                    newSecond = isLeading ? 10 : last;
                }

                const [cnt, s] = dp(idx + 1, newTight, newIsLeading, newLast, newSecond);
                totalCount += cnt;
                totalSum += s + cnt * wavInc;
            }

            memoCnt[idx][t][il][last][secondLast] = totalCount;
            memoSum[idx][t][il][last][secondLast] = totalSum;
            return [totalCount, totalSum];
        };

        return dp(0, true, true, 10, 10)[1];
    };

    const res = f(BigInt(num2)) - f(BigInt(num1) - 1n);
    return Number(res);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function totalWaviness(num1: number, num2: number): number {
    const countMemo = new BigInt64Array(8228);
    const sumMemo = new BigInt64Array(8228);

    function solve(n: bigint): bigint {
        if (n < 0n) return 0n;
        const nStr = n.toString();
        countMemo.fill(-1n);
        sumMemo.fill(-1n);

        function dp(pos: number, tight: boolean, isLeading: boolean, d1: number, d2: number): { count: bigint, sum: bigint } {
            if (pos === nStr.length) {
                return { count: 1n, sum: 0n };
            }

            const tightVal = tight ? 1 : 0;
            const leadingVal = isLeading ? 1 : 0;
            const stateIdx = ((((pos * 2 + tightVal) * 2 + leadingVal) * 11 + (d1 + 1)) * 11 + (d2 + 1));

            if (countMemo[stateIdx] !== -1n) {
                return { count: countMemo[stateIdx], sum: sumMemo[stateIdx] };
            }

            let resCount = 0n;
            let resSum = 0n;
            const limit = tight ? parseInt(nStr[pos]) : 9;

            for (let d = 0; d <= limit; d++) {
                const newTight = tight && (d === limit);
                const newIsLeading = isLeading && (d === 0);

                let addedWaviness = 0n;
                if (!isLeading && d1 !== -1 && d2 !== -1) {
                    if ((d2 < d1 && d < d1) || (d2 > d1 && d > d1)) {
                        addedWaviness = 1n;
                    }
                }

                const res = newIsLeading 
                    ? dp(pos + 1, newTight, true, -1, -1)
                    : dp(pos + 1, newTight, false, d, d1);

                resCount += res.count;
                resSum += res.sum + (addedWaviness * res.count);
            }

            countMemo[stateIdx] = resCount;
            sumMemo[stateIdx] = resSum;
            return { count: resCount, sum: resSum };
        }

        return dp(0, true, true, -1, -1).sum;
    }

    return Number(solve(BigInt(num2)) - solve(BigInt(num1) - 1n));
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    private $memoCount;
    private $memoSum;

    /**
     * @param Integer $num1
     * @param Integer $num2
     * @return Integer
     */
    function totalWaviness($num1, $num2) {
        return $this->solve($num2) - $this->solve($num1 - 1);
    }

    private function solve($n) {
        if ($n < 0) return 0;
        $nStr = (string)$n;
        $this->memoCount = [];
        $this->memoSum = [];
        $res = $this->dp(0, true, true, -1, -1, $nStr);
        return $res[1];
    }

    private function dp($pos, $tight, $isLeading, $d1, $d2, $nStr) {
        if ($pos === strlen($nStr)) {
            return [1, 0];
        }

        $tightInt = $tight ? 1 : 0;
        $leadingInt = $isLeading ? 1 : 0;
        $key = "$pos,$tightInt,$leadingInt,$d1,$d2";
        if (isset($this->memoCount[$key])) {
            return [$this->memoCount[$key], $this->memoSum[$key]];
        }

        $resCount = 0;
        $resSum = 0;
        $limit = $tight ? (int)$nStr[$pos] : 9;

        for ($d = 0; $d <= $limit; $d++) {
            $newTight = $tight && ($d === $limit);
            $newIsLeading = $isLeading && ($d === 0);

            $addedWaviness = 0;
            if (!$isLeading && $d1 !== -1 && $d2 !== -1) {
                if (($d2 < $d1 && $d < $d1) || ($d2 > $d1 && $d > $d1)) {
                    $addedWaviness = 1;
                }
            }

            $res = $newIsLeading 
                ? $this->dp($pos + 1, $newTight, true, -1, -1, $nStr)
                : $this->dp($pos + 1, $newTight, false, $d, $d1, $nStr);

            $resCount += $res[0];
            $resSum += $res[1] + ($addedWaviness * $res[0]);
        }

        $this->memoCount[$key] = $resCount;
        $this->memoSum[$key] = $resSum;
        return [$resCount, $resSum];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    private var memoCount = [Int64](repeating: -1, count: 8228)
    private var memoSum = [Int64](repeating: -1, count: 8228)

    func totalWaviness(_ num1: Int, _ num2: Int) -> Int {
        return Int(solve(Int64(num2)) - solve(Int64(num1) - 1))
    }

    private func solve(_ n: Int64) -> Int64 {
        if n < 0 { return 0 }
        let nStr = String(n).compactMap { Int(String($0)) }
        memoCount = [Int64](repeating: -1, count: 8228)
        memoSum = [Int64](repeating: -1, count: 8228)
        return dp(0, true, true, -1, -1, nStr).sum
    }

    private func dp(_ pos: Int, _ tight: Bool, _ isLeading: Bool, _ d1: Int, _ d2: Int, _ nStr: [Int]) -> (count: Int64, sum: Int64) {
        if pos == nStr.count {
            return (1, 0)
        }

        let tightVal = tight ? 1 : 0
        let leadingVal = isLeading ? 1 : 0
        let stateIdx = ((((pos * 2 + tightVal) * 2 + leadingVal) * 11 + (d1 + 1)) * 11 + (d2 + 1))

        if memoCount[stateIdx] != -1 {
            return (memoCount[stateIdx], memoSum[stateIdx])
        }

        var resCount: Int64 = 0
        var resSum: Int64 = 0
        let limit = tight ? nStr[pos] : 9

        for d in 0...limit {
            let newTight = tight && (d == limit)
            let newIsLeading = isLeading && (d == 0)

            var addedWaviness: Int64 = 0
            if !isLeading && d1 != -1 && d2 != -1 {
                if (d2 < d1 && d < d1) || (d2 > d1 && d > d1) {
                    addedWaviness = 1
                }
            }

            let res = newIsLeading
                ? dp(pos + 1, newTight, true, -1, -1, nStr)
                : dp(pos + 1, newTight, false, d, d1, nStr)

            resCount += res.count
            resSum += res.sum + (addedWaviness * res.count)
        }

        memoCount[stateIdx] = resCount
        memoSum[stateIdx] = resSum
        return (resCount, resSum)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    private val memoCount = LongArray(8228)
    private val memoSum = LongArray(8228)
    private var nStr: String = ""

    fun totalWaviness(num1: Long, num2: Long): Long {
        return solve(num2) - solve(num1 - 1)
    }

    private fun solve(n: Long): Long {
        if (n < 0) return 0L
        nStr = n.toString()
        memoCount.fill(-1L)
        memoSum.fill(-1L)
        return dp(0, true, true, -1, -1).second
    }

    private fun dp(pos: Int, tight: Boolean, isLeading: Boolean, d1: Int, d2: Int): Pair<Long, Long> {
        if (pos == nStr.length) {
            return Pair(1L, 0L)
        }

        val tightVal = if (tight) 1 else 0
        val leadingVal = if (isLeading) 1 else 0
        val stateIdx = ((((pos * 2 + tightVal) * 2 + leadingVal) * 11 + (d1 + 1)) * 11 + (d2 + 1))

        if (memoCount[stateIdx] != -1L) {
            return Pair(memoCount[stateIdx], memoSum[stateIdx])
        }

        var resCount = 0L
        var resSum = 0L
        val limit = if (tight) nStr[pos] - '0' else 9

        for (d in 0..limit) {
            val newTight = tight && (d == limit)
            val newIsLeading = isLeading && (d == 0)

            var addedWaviness = 0L
            if (!isLeading && d1 != -1 && d2 != -1) {
                if ((d2 < d1 && d < d1) || (d2 > d1 && d > d1)) {
                    addedWaviness = 1L
                }
            }

            val res = if (newIsLeading) {
                dp(pos + 1, newTight, true, -1, -1)
            } else {
                dp(pos + 1, newTight, false, d, d1)
            }

            resCount += res.first
            resSum += res.second + (addedWaviness * res.first)
        }

        memoCount[stateIdx] = resCount
        memoSum[stateIdx] = resSum
        return Pair(resCount, resSum)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Result {
  final int count;
  final int waviness;
  Result(this.count, this.waviness);
}

class Solution {
  int totalWaviness(int num1, int num2) {
    return _solve(num2) - _solve(num1 - 1);
  }

  int _solve(int n) {
    if (n < 0) return 0;
    String s = n.toString();
    List<int> digits = s.split('').map(int.parse).toList();
    List<Result?> memo = List.filled(20 * 2 * 2 * 11 * 11, null);

    Result dp(int pos, bool tight, bool leading, int last, int secLast) {
      if (pos == digits.length) {
        return Result(1, 0);
      }
      int tIdx = tight ? 1 : 0;
      int lIdx = leading ? 1 : 0;
      int idx = (((pos * 2 + tIdx) * 2 + lIdx) * 11 + last) * 11 + secLast;
      if (memo[idx] != null) return memo[idx]!;

      int count = 0;
      int waviness = 0;
      int limit = tight ? digits[pos] : 9;

      for (int d = 0; d <= limit; d++) {
        bool nextTight = tight && (d == limit);
        bool nextLeading = leading && (d == 0);
        int delta = 0;
        if (!leading && secLast != 10) {
          if ((last > secLast && last > d) || (last < secLast && last < d)) {
            delta = 1;
          }
        }

        int nextLast = 10;
        int nextSecLast = 10;
        if (!nextLeading) {
          nextLast = d;
          nextSecLast = last;
        }

        Result res = dp(pos + 1, nextTight, nextLeading, nextLast, nextSecLast);
        count += res.count;
        waviness += res.waviness + delta * res.count;
      }

      memo[idx] = Result(count, waviness);
      return memo[idx]!;
    }

    return dp(0, true, true, 10, 10).waviness;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import (
	"strconv"
)

type Result struct {
	count    int64
	waviness int64
}

func totalWaviness(num1 int64, num2 int64) int64 {
	return solve(num2) - solve(num1-1)
}

func solve(n int64) int64 {
	if n < 0 {
		return 0
	}
	s := strconv.FormatInt(n, 10)
	digits := make([]int, len(s))
	for i, r := range s {
		digits[i] = int(r - '0')
	}

	memoCount := make([]int64, 20*2*2*11*11)
	memoWaviness := make([]int64, 20*2*2*11*11)
	for i := range memoCount {
		memoCount[i] = -1
	}

	var dp func(int, bool, bool, int, int) Result
	dp = func(pos int, tight, leading bool, last, secLast int) Result {
		if pos == len(digits) {
			return Result{1, 0}
		}
		tIdx, lIdx := 0, 0
		if tight {
			tIdx = 1
		}
		if leading {
			lIdx = 1
		}
		idx := (((pos*2+tIdx)*2+lIdx)*11+last)*11 + secLast
		if memoCount[idx] != -1 {
			return Result{memoCount[idx], memoWaviness[idx]}
		}

		var count, waviness int64
		limit := 9
		if tight {
			limit = digits[pos]
		}

		for d := 0; d <= limit; d++ {
			nextTight := tight && (d == limit)
			nextLeading := leading && (d == 0)

			delta := int64(0)
			if !leading && secLast != 10 {
				if (last > secLast && last > d) || (last < secLast && last < d) {
					delta = 1
				}
			}

			nextLast, nextSecLast := 10, 10
			if !nextLeading {
				nextLast, nextSecLast = d, last
			}

			res := dp(pos+1, nextTight, nextLeading, nextLast, nextSecLast)
			count += res.count
			waviness += res.waviness + delta*res.count
		}

		memoCount[idx] = count
		memoWaviness[idx] = waviness
		return Result{count, waviness}
	}

	return dp(0, true, true, 10, 10).waviness
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def total_waviness(num1, num2)
  solve(num2) - solve(num1 - 1)
end

def solve(n)
  return 0 if n < 0
  digits = n.to_s.chars.map(&:to_i)
  memo = {}

  dp = lambda do |pos, tight, leading, last, sec_last|
    state = [pos, tight, leading, last, sec_last]
    return memo[state] if memo.key?(state)

    if pos == digits.length
      return [1, 0]
    end

    count = 0
    waviness = 0
    limit = tight ? digits[pos] : 9

    (0..limit).each do |d|
      next_tight = tight && (d == limit)
      next_leading = leading && (d == 0)

      delta = 0
      if !leading && sec_last != 10
        if (last > sec_last && last > d) || (last < sec_last && last < d)
          delta = 1
        end
      end

      next_last = 10
      next_sec_last = 10
      unless next_leading
        next_last = d
        next_sec_last = last
      end

      res = dp.call(pos + 1, next_tight, next_leading, next_last, next_sec_last)
      count += res[0]
      waviness += res[1] + delta * res[0]
    end

    memo[state] = [count, waviness]
  end

  dp.call(0, true, true, 10, 10)[1]
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def totalWaviness(num1: Long, num2: Long): Long = {
        solve(num2) - solve(num1 - 1)
    }

    def solve(n: Long): Long = {
        if (n < 0) return 0
        val digits = n.toString.map(_.asDigit).toArray
        val memoCount = Array.fill(20 * 2 * 2 * 11 * 11)(-1L)
        val memoWaviness = Array.fill(20 * 2 * 2 * 11 * 11)(-1L)

        def dp(pos: Int, tight: Boolean, leading: Boolean, last: Int, secLast: Int): (Long, Long) = {
            if (pos == digits.length) {
                return (1L, 0L)
            }
            val tIdx = if (tight) 1 else 0
            val lIdx = if (leading) 1 else 0
            val idx = (((pos * 2 + tIdx) * 2 + lIdx) * 11 + last) * 11 + secLast
            if (memoCount(idx) != -1L) return (memoCount(idx), memoWaviness(idx))

            var count = 0L
            var waviness = 0L
            val limit = if (tight) digits(pos) else 9

            var d = 0
            while (d <= limit) {
                val nextTight = tight && (d == limit)
                val nextLeading = leading && (d == 0)
                var delta = 0L
                if (!leading && secLast != 10) {
                    if ((last > secLast && last > d) || (last < secLast && last < d)) {
                        delta = 1L
                    }
                }

                var nextLast = 10
                var nextSecLast = 10
                if (!nextLeading) {
                    nextLast = d
                    nextSecLast = last
                }

                val res = dp(pos + 1, nextTight, nextLeading, nextLast, nextSecLast)
                count += res._1
                waviness += res._2 + delta * res._1
                d += 1
            }

            memoCount(idx) = count
            memoWaviness(idx) = waviness
            (count, waviness)
        }

        dp(0, true, true, 10, 10)._2
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn total_waviness(num1: i64, num2: i64) -> i64 {
        fn solve(num: i64) -> i64 {
            if num <= 0 {
                return 0;
            }
            let s = num.to_string();
            let digits: Vec<i32> = s.chars().map(|c| c.to_digit(10).unwrap() as i32).collect();
            let n = digits.len();
            let mut memo = vec![vec![vec![vec![vec![None; 11]; 11]; 2]; 2]; n + 1];
            dp(0, true, false, 10, 10, &digits, &mut memo).1
        }

        fn dp(
            pos: usize,
            tight: bool,
            started: bool,
            p1: i32,
            p2: i32,
            digits: &Vec<i32>,
            memo: &mut Vec<Vec<Vec<Vec<Vec<Option<(i64, i64)>>>>>>,
        ) -> (i64, i64) {
            if pos == digits.len() {
                return (1, 0);
            }
            if let Some(res) = memo[pos][tight as usize][started as usize][p1 as usize][p2 as usize] {
                return res;
            }

            let mut total_cnt: i64 = 0;
            let mut total_wav: i64 = 0;
            let limit = if tight { digits[pos] } else { 9 };

            for d in 0..=limit {
                let new_tight = tight && (d == limit);
                let mut is_wav = 0;
                let (new_started, new_p1, new_p2) = if !started {
                    if d == 0 {
                        (false, 10, 10)
                    } else {
                        (true, d, 10)
                    }
                } else {
                    if p2 != 10 {
                        if (p1 > p2 && p1 > d) || (p1 < p2 && p1 < d) {
                            is_wav = 1;
                        }
                    }
                    (true, d, p1)
                };

                let (cnt, wav) = dp(pos + 1, new_tight, new_started, new_p1, new_p2, digits, memo);
                total_cnt += cnt;
                total_wav += wav + (is_wav as i64) * cnt;
            }

            memo[pos][tight as usize][started as usize][p1 as usize][p2 as usize] = Some((total_cnt, total_wav));
            (total_cnt, total_wav)
        }

        solve(num2) - solve(num1 - 1)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (total-waviness num1 num2)
  (-> exact-integer? exact-integer? exact-integer?)
  (define (solve n)
    (if (<= n 0)
        0
        (let* ([s (number->string n)]
               [digits (list->vector (map (lambda (c) (- (char->integer c) (char->integer #\0))) (string->list s)))]
               [len (vector-length digits)]
               [memo (make-hash)])
          (letrec ([dp (lambda (pos tight started p1 p2)
                         (let ([key (list pos tight started p1 p2)])
                           (cond
                             [(hash-has-key? memo key) (hash-ref memo key)]
                             [(= pos len) (cons 1 0)]
                             [else
                              (let* ([limit (if tight (vector-ref digits pos) 9)]
                                     [res (for/fold ([acc (cons 0 0)])
                                                    ([d (in-range (+ limit 1))])
                                            (let* ([new-tight (and tight (= d limit))]
                                                   [is-wav (if (and started (not (= p2 10))
                                                                    (or (and (> p1 p2) (> p1 d))
                                                                        (and (< p1 p2) (< p1 d))))
                                                               1 0)]
                                                   [new-params (if (not started)
                                                                   (if (= d 0) (list #f 10 10) (list #t d 10))
                                                                   (list #t d p1))]
                                                   [next-res (dp (+ pos 1) new-tight (car new-params) (cadr new-params) (caddr new-params))])
                                              (cons (+ (car acc) (car next-res))
                                                    (+ (cdr acc) (cdr next-res) (* is-wav (car next-res))))))])
                                (hash-set! memo key res)
                                res)])))])
            (cdr (dp 0 #t #f 10 10))))))
  (- (solve num2) (solve (- num1 1))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec total_waviness(Num1 :: integer(), Num2 :: integer()) -> integer().
total_waviness(Num1, Num2) ->
  solve(Num2) - solve(Num1 - 1).

solve(Num) ->
  if Num =< 0 -> 0;
     true ->
       DigitsList = [D - $0 || D <- integer_to_list(Num)],
       DigitsTuple = list_to_tuple(DigitsList),
       L = tuple_size(DigitsTuple),
       {_, Wav, _} = dp(0, true, false, 10, 10, DigitsTuple, L, #{}),
       Wav
  end.

dp(Pos, Tight, Started, P1, P2, DigitsTuple, L, Memo) ->
  Key = {Pos, Tight, Started, P1, P2},
  case maps:find(Key, Memo) of
    {ok, {Cnt, Wav}} -> {Cnt, Wav, Memo};
    error ->
      if Pos == L -> {1, 0, Memo};
         true ->
           Limit = if Tight -> element(Pos + 1, DigitsTuple); true -> 9 end,
           {TCnt, TWav, TMemo} = 
             lists:foldl(fun(D, {AccCnt, AccWav, M}) ->
               NTight = Tight andalso (D == Limit),
               {NStarted, NP1, NP2, IsWav} =
                 if not Started ->
                    if D == 0 -> {false, 10, 10, 0};
                       true -> {true, D, 10, 0}
                    end;
                 true ->
                    W = if (P2 /= 10) andalso (((P1 > P2) andalso (P1 > D)) orelse ((P1 < P2) andalso (P1 < D))) -> 1;
                           true -> 0
                        end,
                    {true, D, P1, W}
                 end,
               {Cnt, Wav, NM} = dp(Pos + 1, NTight, NStarted, NP1, NP2, DigitsTuple, L, M),
               {AccCnt + Cnt, AccWav + Wav + IsWav * Cnt, NM}
             end, {0, 0, Memo}, lists:seq(0, Limit)),
           {TCnt, TWav, maps:put(Key, {TCnt, TWav}, TMemo)}
      end
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec total_waviness(num1 :: integer, num2 :: integer) :: integer
  def total_waviness(num1, num2) do
    solve(num2) - solve(num1 - 1)
  end

  defp solve(num) do
    if num <= 0 do
      0
    else
      digits_list = Integer.to_string(num) |> String.to_charlist() |> Enum.map(&(&1 - ?0))
      digits_tuple = List.to_tuple(digits_list)
      l = tuple_size(digits_tuple)
      {{_cnt, wav}, _memo} = dp(0, true, false, 10, 10, digits_tuple, l, %{})
      wav
    end
  end

  defp dp(pos, tight, started, p1, p2, digits_tuple, l, memo) do
    key = {pos, tight, started, p1, p2}
    if Map.has_key?(memo, key) do
      {Map.get(memo, key), memo}
    else
      if pos == l do
        {{1, 0}, memo}
      else
        limit = if tight, do: elem(digits_tuple, pos), else: 9
        {total_cnt, total_wav, final_memo} = 
          Enum.reduce(0..limit, {0, 0, memo}, fn d, {acc_cnt, acc_wav, current_memo} ->
            new_tight = tight and (d == limit)
            {new_started, new_p1, new_p2, is_wav} = 
              if not started do
                if d == 0, do: {false, 10, 10, 0}, else: {true, d, 10, 0}
              else
                w = if p2 != 10 and ((p1 > p2 and p1 > d) or (p1 < p2 and p1 < d)), do: 1, else: 0
                {true, d, p1, w}
              end
            {{cnt, wav}, next_memo} = dp(pos + 1, new_tight, new_started, new_p1, new_p2, digits_tuple, l, current_memo)
            {acc_cnt + cnt, acc_wav + wav + is_wav * cnt, next_memo}
          end)
        res = {total_cnt, total_wav}
        {res, Map.put(final_memo, key, res)}
      end
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(L * D^3), where L is the maximum number of digits (log10 of num2) and D is the base (10). The state space size is L * 2 * 2 * 11 * 11, and each state involves a transition loop of size D.
- **Space Complexity:** O(L * D^2), where L is the maximum number of digits and D is the base (10). This space is used to store the memoization table for the DP states.
