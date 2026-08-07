---
layout: post
title: "Smallest Divisible Digit Product II"
date: 2026-08-07 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Math", "String", "Backtracking", "Greedy", "Number Theory"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/smallest-divisible-digit-product-ii/
ai_solutions:
  - solutions:
      cpp: '// Generation failed for C++

        // Reason: Parsing failed'
      java: '// Generation failed for Java

        // Reason: Parsing failed'
      python: '// Generation failed for Python

        // Reason: Parsing failed'
      python3: "class Solution:\n    def smallestNumber(self, num: str, t: int) -> str:\n\
        \        a, b, c, d = 0, 0, 0, 0\n        temp_t = t\n        for p, count in\
        \ [(2, 'a'), (3, 'b'), (5, 'c'), (7, 'd')]:\n            while temp_t % p ==\
        \ 0:\n                if count == 'a': a += 1\n                elif count ==\
        \ 'b': b += 1\n                elif count == 'c': c += 1\n                else:\
        \ d += 1\n                temp_t //= p\n        if temp_t > 1: return \"-1\"\
        \n\n        factors = {2: (1, 0), 3: (0, 1), 4: (2, 0), 6: (1, 1), 8: (3, 0),\
        \ 9: (0, 2)}\n        dp = [[100] * 40 for _ in range(60)]\n        combo =\
        \ [[\"\"] * 40 for _ in range(60)]\n        dp[0][0] = 0\n        for i in range(60):\n\
        \            for j in range(40):\n                if i == 0 and j == 0: continue\n\
        \                for digit in [2, 3, 4, 6, 8, 9]:\n                    da, db\
        \ = factors[digit]\n                    pi, pj = max(0, i - da), max(0, j -\
        \ db)\n                    if dp[pi][pj] + 1 < dp[i][j]:\n                 \
        \       dp[i][j] = dp[pi][pj] + 1\n                        combo[i][j] = \"\"\
        .join(sorted(str(digit) + combo[pi][pj]))\n                    elif dp[pi][pj]\
        \ + 1 == dp[i][j]:\n                        new_c = \"\".join(sorted(str(digit)\
        \ + combo[pi][pj]))\n                        if new_c < combo[i][j]:\n     \
        \                       combo[i][j] = new_c\n\n        n = len(num)\n      \
        \  first_zero = num.find('0')\n        pref_a, pref_b, pref_c, pref_d = [0]\
        \ * (n + 1), [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)\n        for i in range(n):\n\
        \            if num[i] == '0': break\n            digit = int(num[i])\n    \
        \        pref_a[i+1] = pref_a[i] + (1 if digit in [2, 6] else 2 if digit ==\
        \ 4 else 3 if digit == 8 else 0)\n            pref_b[i+1] = pref_b[i] + (1 if\
        \ digit in [3, 6] else 2 if digit == 9 else 0)\n            pref_c[i+1] = pref_c[i]\
        \ + (1 if digit == 5 else 0)\n            pref_d[i+1] = pref_d[i] + (1 if digit\
        \ == 7 else 0)\n\n        if first_zero == -1 and pref_a[n] >= a and pref_b[n]\
        \ >= b and pref_c[n] >= c and pref_d[n] >= d:\n            return num\n\n  \
        \      limit = first_zero if first_zero != -1 else n - 1\n        for i in range(limit,\
        \ -1, -1):\n            start_d = int(num[i]) + 1 if i < first_zero or first_zero\
        \ == -1 else 1\n            for d_val in range(start_d, 10):\n             \
        \   ra, rb = max(0, a - pref_a[i]), max(0, b - pref_b[i])\n                rc,\
        \ rd = max(0, c - pref_c[i]), max(0, d - pref_d[i])\n                da, db\
        \ = factors.get(d_val, (0, 0))\n                ra, rb = max(0, ra - da), max(0,\
        \ rb - db)\n                rc, rd = max(0, rc - (1 if d_val == 5 else 0)),\
        \ max(0, rd - (1 if d_val == 7 else 0))\n                if dp[ra][rb] + rc\
        \ + rd <= n - 1 - i:\n                    needed = combo[ra][rb] + \"5\" * rc\
        \ + \"7\" * rd\n                    ones = \"1\" * (n - 1 - i - len(needed))\n\
        \                    return num[:i] + str(d_val) + ones + \"\".join(sorted(needed))\n\
        \n        L = max(n + 1, dp[a][b] + c + d)\n        needed = combo[a][b] + \"\
        5\" * c + \"7\" * d\n        return \"1\" * (L - len(needed)) + \"\".join(sorted(needed))"
      c: "#include <string.h>\n#include <stdlib.h>\n#include <stdio.h>\n\nint dp[61][41];\n\
        char combo[61][41][61];\nint digit_a[10] = {0, 0, 1, 0, 2, 0, 1, 0, 3, 0};\n\
        int digit_b[10] = {0, 0, 0, 1, 0, 0, 1, 0, 0, 2};\nint digit_c[10] = {0, 0,\
        \ 0, 0, 0, 1, 0, 0, 0, 0};\nint digit_d[10] = {0, 0, 0, 0, 0, 0, 0, 1, 0, 0};\n\
        \nint compare_chars(const void* a, const void* b) {\n    return (*(char*)a -\
        \ *(char*)b);\n}\n\nchar* smallestNumber(char* num, long long t) {\n    long\
        \ long temp_t = t;\n    int a = 0, b = 0, c = 0, d = 0;\n    int primes[] =\
        \ {2, 3, 5, 7};\n    for (int i = 0; i < 4; i++) {\n        while (temp_t %\
        \ primes[i] == 0) {\n            if (i == 0) a++; else if (i == 1) b++; else\
        \ if (i == 2) c++; else d++;\n            temp_t /= primes[i];\n        }\n\
        \    }\n    if (temp_t > 1) return \"-1\";\n\n    for (int i = 0; i < 61; i++)\
        \ {\n        for (int j = 0; j < 41; j++) {\n            dp[i][j] = 100;\n \
        \           combo[i][j][0] = '\\0';\n        }\n    }\n    dp[0][0] = 0;\n \
        \   for (int i = 0; i < 61; i++) {\n        for (int j = 0; j < 41; j++) {\n\
        \            if (i == 0 && j == 0) continue;\n            int digits[] = {2,\
        \ 3, 4, 6, 8, 9};\n            for (int k = 0; k < 6; k++) {\n             \
        \   int cur_d = digits[k];\n                int pi = i - digit_a[cur_d]; if\
        \ (pi < 0) pi = 0;\n                int pj = j - digit_b[cur_d]; if (pj < 0)\
        \ pj = 0;\n                if (dp[pi][pj] + 1 <= dp[i][j]) {\n             \
        \       char next[61];\n                    sprintf(next, \"%d%s\", cur_d, combo[pi][pj]);\n\
        \                    qsort(next, strlen(next), 1, compare_chars);\n        \
        \            if (dp[pi][pj] + 1 < dp[i][j] || strcmp(next, combo[i][j]) < 0)\
        \ {\n                        dp[i][j] = dp[pi][pj] + 1;\n                  \
        \      strcpy(combo[i][j], next);\n                    }\n                }\n\
        \            }\n        }\n    }\n\n    int n = strlen(num);\n    char* first_z_ptr\
        \ = strchr(num, '0');\n    int first_zero = first_z_ptr ? (int)(first_z_ptr\
        \ - num) : -1;\n    int* pref_a = calloc(n + 1, sizeof(int));\n    int* pref_b\
        \ = calloc(n + 1, sizeof(int));\n    int* pref_c = calloc(n + 1, sizeof(int));\n\
        \    int* pref_d = calloc(n + 1, sizeof(int));\n    for (int i = 0; i < n; i++)\
        \ {\n        if (num[i] == '0') break;\n        int val = num[i] - '0';\n  \
        \      pref_a[i+1] = pref_a[i] + digit_a[val];\n        pref_b[i+1] = pref_b[i]\
        \ + digit_b[val];\n        pref_c[i+1] = pref_c[i] + digit_c[val];\n       \
        \ pref_d[i+1] = pref_d[i] + digit_d[val];\n    }\n\n    if (first_zero == -1\
        \ && pref_a[n] >= a && pref_b[n] >= b && pref_c[n] >= c && pref_d[n] >= d) {\n\
        \        free(pref_a); free(pref_b); free(pref_c); free(pref_d);\n        return\
        \ num;\n    }\n\n    int limit = (first_zero == -1) ? n - 1 : first_zero;\n\
        \    for (int i = limit; i >= 0; i--) {\n        int start_d = (first_zero ==\
        \ -1 || i < first_zero) ? (num[i] - '0' + 1) : 1;\n        for (int dv = start_d;\
        \ dv <= 9; dv++) {\n            int ra = a - pref_a[i] - digit_a[dv]; if (ra\
        \ < 0) ra = 0;\n            int rb = b - pref_b[i] - digit_b[dv]; if (rb < 0)\
        \ rb = 0;\n            int rc = c - pref_c[i] - digit_c[dv]; if (rc < 0) rc\
        \ = 0;\n            int rd = d - pref_d[i] - digit_d[dv]; if (rd < 0) rd = 0;\n\
        \            if (dp[ra][rb] + rc + rd <= n - 1 - i) {\n                char*\
        \ res = malloc(n + 10); memset(res, 0, n + 10);\n                strncpy(res,\
        \ num, i); res[i] = dv + '0';\n                char suffix[200005]; int sidx\
        \ = 0;\n                for (int j = 0; j < rc; j++) suffix[sidx++] = '5';\n\
        \                for (int j = 0; j < rd; j++) suffix[sidx++] = '7';\n      \
        \          strcpy(suffix + sidx, combo[ra][rb]); sidx += strlen(combo[ra][rb]);\n\
        \                qsort(suffix, sidx, 1, compare_chars);\n                int\
        \ ones = n - 1 - i - sidx;\n                for (int j = 0; j < ones; j++) res[i\
        \ + 1 + j] = '1';\n                strcpy(res + i + 1 + ones, suffix);\n   \
        \             free(pref_a); free(pref_b); free(pref_c); free(pref_d);\n    \
        \            return res;\n            }\n        }\n    }\n\n    int min_len\
        \ = dp[a][b] + c + d;\n    int L = (n + 1 > min_len) ? n + 1 : min_len;\n  \
        \  char* res = malloc(L + 10); memset(res, '1', L); res[L] = '\\0';\n    char\
        \ suffix[200]; int sidx = 0;\n    for (int j = 0; j < c; j++) suffix[sidx++]\
        \ = '5';\n    for (int j = 0; j < d; j++) suffix[sidx++] = '7';\n    strcpy(suffix\
        \ + sidx, combo[a][b]); sidx += strlen(combo[a][b]);\n    qsort(suffix, sidx,\
        \ 1, compare_chars);\n    strcpy(res + L - sidx, suffix);\n    free(pref_a);\
        \ free(pref_b); free(pref_c); free(pref_d);\n    return res;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\nusing System.Linq;\n\
        using System.Text;\n\npublic class Solution {\n    public string SmallestNumber(string\
        \ num, long t) {\n        long tempT = t;\n        int a = 0, b = 0, c = 0,\
        \ d = 0;\n        long[] primes = { 2, 3, 5, 7 };\n        for (int i = 0; i\
        \ < 4; i++) {\n            while (tempT % primes[i] == 0) {\n              \
        \  if (i == 0) a++; else if (i == 1) b++; else if (i == 2) c++; else d++;\n\
        \                tempT /= primes[i];\n            }\n        }\n        if (tempT\
        \ > 1) return \"-1\";\n\n        int[] digitA = { 0, 0, 1, 0, 2, 0, 1, 0, 3,\
        \ 0 };\n        int[] digitB = { 0, 0, 0, 1, 0, 0, 1, 0, 0, 2 };\n        int[,]\
        \ dp = new int[61, 41];\n        string[,] combo = new string[61, 41];\n\n \
        \       for (int i = 0; i < 61; i++) {\n            for (int j = 0; j < 41;\
        \ j++) {\n                dp[i, j] = 100;\n                combo[i, j] = \"\"\
        ;\n            }\n        }\n        dp[0, 0] = 0;\n        for (int i = 0;\
        \ i < 61; i++) {\n            for (int j = 0; j < 41; j++) {\n             \
        \   if (i == 0 && j == 0) continue;\n                int[] digits = { 2, 3,\
        \ 4, 6, 8, 9 };\n                foreach (int dv in digits) {\n            \
        \        int pi = Math.Max(0, i - digitA[dv]);\n                    int pj =\
        \ Math.Max(0, j - digitB[dv]);\n                    if (dp[pi, pj] + 1 <= dp[i,\
        \ j]) {\n                        char[] nextArr = (dv.ToString() + combo[pi,\
        \ pj]).ToCharArray();\n                        Array.Sort(nextArr);\n      \
        \                  string next = new string(nextArr);\n                    \
        \    if (dp[pi, pj] + 1 < dp[i, j] || string.Compare(next, combo[i, j]) < 0)\
        \ {\n                            dp[i, j] = dp[pi, pj] + 1;\n              \
        \              combo[i, j] = next;\n                        }\n            \
        \        }\n                }\n            }\n        }\n\n        int n = num.Length;\n\
        \        int firstZero = num.IndexOf('0');\n        int[] prefA = new int[n\
        \ + 1], prefB = new int[n + 1], prefC = new int[n + 1], prefD = new int[n +\
        \ 1];\n        for (int i = 0; i < n; i++) {\n            if (num[i] == '0')\
        \ break;\n            int v = num[i] - '0';\n            prefA[i + 1] = prefA[i]\
        \ + digitA[v];\n            prefB[i + 1] = prefB[i] + digitB[v];\n         \
        \   prefC[i + 1] = prefC[i] + (v == 5 ? 1 : 0);\n            prefD[i + 1] =\
        \ prefD[i] + (v == 7 ? 1 : 0);\n        }\n\n        if (firstZero == -1 &&\
        \ prefA[n] >= a && prefB[n] >= b && prefC[n] >= c && prefD[n] >= d) return num;\n\
        \n        int limit = firstZero == -1 ? n - 1 : firstZero;\n        for (int\
        \ i = limit; i >= 0; i--) {\n            int startD = (firstZero == -1 || i\
        \ < firstZero) ? (num[i] - '0' + 1) : 1;\n            for (int dv = startD;\
        \ dv <= 9; dv++) {\n                int ra = Math.Max(0, a - prefA[i] - digitA[dv]);\n\
        \                int rb = Math.Max(0, b - prefB[i] - digitB[dv]);\n        \
        \        int rc = Math.Max(0, c - prefC[i] - (dv == 5 ? 1 : 0));\n         \
        \       int rd = Math.Max(0, d - prefD[i] - (dv == 7 ? 1 : 0));\n          \
        \      if (dp[ra, rb] + rc + rd <= n - 1 - i) {\n                    char[]\
        \ suffixArr = (combo[ra, rb] + new string('5', rc) + new string('7', rd)).ToCharArray();\n\
        \                    Array.Sort(suffixArr);\n                    string ones\
        \ = new string('1', n - 1 - i - suffixArr.Length);\n                    return\
        \ num.Substring(0, i) + dv + ones + new string(suffixArr);\n               \
        \ }\n            }\n        }\n\n        int L = Math.Max(n + 1, dp[a, b] +\
        \ c + d);\n        char[] resArr = (combo[a, b] + new string('5', c) + new string('7',\
        \ d)).ToCharArray();\n        Array.Sort(resArr);\n        return new string('1',\
        \ L - resArr.Length) + new string(resArr);\n    }\n}"
      javascript: "/**\n * @param {string} num\n * @param {number} t\n * @return {string}\n\
        \ */\nvar smallestNumber = function(num, t) {\n    let bigT = BigInt(t);\n \
        \   let a = 0, b = 0, c = 0, d = 0;\n    let primes = [2n, 3n, 5n, 7n];\n  \
        \  for (let i = 0; i < 4; i++) {\n        while (bigT % primes[i] === 0n) {\n\
        \            if (i === 0) a++; else if (i === 1) b++; else if (i === 2) c++;\
        \ else d++;\n            bigT /= primes[i];\n        }\n    }\n    if (bigT\
        \ > 1n) return \"-1\";\n\n    const digitA = [0, 0, 1, 0, 2, 0, 1, 0, 3, 0];\n\
        \    const digitB = [0, 0, 0, 1, 0, 0, 1, 0, 0, 2];\n    let dp = Array.from({\
        \ length: 61 }, () => Array(41).fill(100));\n    let combo = Array.from({ length:\
        \ 61 }, () => Array(41).fill(\"\"));\n\n    dp[0][0] = 0;\n    for (let i =\
        \ 0; i < 61; i++) {\n        for (let j = 0; j < 41; j++) {\n            if\
        \ (i === 0 && j === 0) continue;\n            let digits = [2, 3, 4, 6, 8, 9];\n\
        \            for (let dv of digits) {\n                let pi = Math.max(0,\
        \ i - digitA[dv]);\n                let pj = Math.max(0, j - digitB[dv]);\n\
        \                if (dp[pi][pj] + 1 <= dp[i][j]) {\n                    let\
        \ next = (dv.toString() + combo[pi][pj]).split('').sort().join('');\n      \
        \              if (dp[pi][pj] + 1 < dp[i][j] || next < combo[i][j]) {\n    \
        \                    dp[i][j] = dp[pi][pj] + 1;\n                        combo[i][j]\
        \ = next;\n                    }\n                }\n            }\n       \
        \ }\n    }\n\n    const n = num.length;\n    let firstZero = num.indexOf('0');\n\
        \    let prefA = Array(n + 1).fill(0), prefB = Array(n + 1).fill(0), prefC =\
        \ Array(n + 1).fill(0), prefD = Array(n + 1).fill(0);\n    for (let i = 0; i\
        \ < n; i++) {\n        if (num[i] === '0') break;\n        let v = parseInt(num[i]);\n\
        \        prefA[i + 1] = prefA[i] + digitA[v];\n        prefB[i + 1] = prefB[i]\
        \ + digitB[v];\n        prefC[i + 1] = prefC[i] + (v === 5 ? 1 : 0);\n     \
        \   prefD[i + 1] = prefD[i] + (v === 7 ? 1 : 0);\n    }\n\n    if (firstZero\
        \ === -1 && prefA[n] >= a && prefB[n] >= b && prefC[n] >= c && prefD[n] >= d)\
        \ return num;\n\n    let limit = firstZero === -1 ? n - 1 : firstZero;\n   \
        \ for (let i = limit; i >= 0; i--) {\n        let startD = (firstZero === -1\
        \ || i < firstZero) ? parseInt(num[i]) + 1 : 1;\n        for (let dv = startD;\
        \ dv <= 9; dv++) {\n            let ra = Math.max(0, a - prefA[i] - digitA[dv]);\n\
        \            let rb = Math.max(0, b - prefB[i] - digitB[dv]);\n            let\
        \ rc = Math.max(0, c - prefC[i] - (dv === 5 ? 1 : 0));\n            let rd =\
        \ Math.max(0, d - prefD[i] - (dv === 7 ? 1 : 0));\n            if (dp[ra][rb]\
        \ + rc + rd <= n - 1 - i) {\n                let suffix = (combo[ra][rb] + \"\
        5\".repeat(rc) + \"7\".repeat(rd)).split('').sort().join('');\n            \
        \    let ones = \"1\".repeat(n - 1 - i - suffix.length);\n                return\
        \ num.substring(0, i) + dv + ones + suffix;\n            }\n        }\n    }\n\
        \n    let L = Math.max(n + 1, dp[a][b] + c + d);\n    let suffix = (combo[a][b]\
        \ + \"5\".repeat(c) + \"7\".repeat(d)).split('').sort().join('');\n    return\
        \ \"1\".repeat(L - suffix.length) + suffix;\n};"
      typescript: '// Generation failed for TypeScript

        // Reason: Parsing failed'
      php: '// Generation failed for PHP

        // Reason: Parsing failed'
      swift: '// Generation failed for Swift

        // Reason: Parsing failed'
      kotlin: '// Generation failed for Kotlin

        // Reason: Parsing failed'
      dart: "import 'dart:math';\n\nclass Solution {\n  static final List<int> count2\
        \ = [0, 0, 1, 0, 2, 0, 1, 0, 3, 0];\n  static final List<int> count3 = [0, 0,\
        \ 0, 1, 0, 0, 1, 0, 0, 2];\n  static final List<int> count5 = [0, 0, 0, 0, 0,\
        \ 1, 0, 0, 0, 0];\n  static final List<int> count7 = [0, 0, 0, 0, 0, 0, 0, 1,\
        \ 0, 0];\n  static List<List<int>>? _dp;\n\n  void _precompute() {\n    if (_dp\
        \ != null) return;\n    _dp = List.generate(65, (_) => List.filled(65, 1000));\n\
        \    _dp![0][0] = 0;\n    for (int a = 0; a <= 60; a++) {\n      for (int b\
        \ = 0; b <= 60; b++) {\n        if (a == 0 && b == 0) continue;\n        int\
        \ best = 1000;\n        List<List<int>> choices = [\n          [1, 0], [0, 1],\
        \ [2, 0], [1, 1], [3, 0], [0, 2]\n        ];\n        for (var pair in choices)\
        \ {\n          int ad = pair[0], bd = pair[1];\n          int na = max(0, a\
        \ - ad);\n          int nb = max(0, b - bd);\n          if (na < a || nb < b)\
        \ {\n            best = min(best, 1 + _dp![na][nb]);\n          }\n        }\n\
        \        _dp![a][b] = best;\n      }\n    }\n  }\n\n  String smallestNumber(String\
        \ num, int t) {\n    _precompute();\n    int a0 = 0, b0 = 0, c0 = 0, d0 = 0;\n\
        \    int tempT = t;\n    while (tempT % 2 == 0) { tempT ~/= 2; a0++; }\n   \
        \ while (tempT % 3 == 0) { tempT ~/= 3; b0++; }\n    while (tempT % 5 == 0)\
        \ { tempT ~/= 5; c0++; }\n    while (tempT % 7 == 0) { tempT ~/= 7; d0++; }\n\
        \    if (tempT > 1) return \"-1\";\n\n    int n = num.length;\n    List<int>\
        \ p2 = List.filled(n + 1, 0);\n    List<int> p3 = List.filled(n + 1, 0);\n \
        \   List<int> p5 = List.filled(n + 1, 0);\n    List<int> p7 = List.filled(n\
        \ + 1, 0);\n    int firstZero = n;\n    for (int i = 0; i < n; i++) {\n    \
        \  int d = num.codeUnitAt(i) - 48;\n      if (d == 0) {\n        firstZero =\
        \ i;\n        break;\n      }\n      p2[i + 1] = p2[i] + count2[d];\n      p3[i\
        \ + 1] = p3[i] + count3[d];\n      p5[i + 1] = p5[i] + count5[d];\n      p7[i\
        \ + 1] = p7[i] + count7[d];\n    }\n\n    if (firstZero == n && p2[n] >= a0\
        \ && p3[n] >= b0 && p5[n] >= c0 && p7[n] >= d0) {\n      return num;\n    }\n\
        \n    for (int L = min(n - 1, firstZero); L >= 0; L--) {\n      int curA0 =\
        \ a0 - p2[L], curB0 = b0 - p3[L], curC0 = c0 - p5[L], curD0 = d0 - p7[L];\n\
        \      for (int d = (num.codeUnitAt(L) - 48) + 1; d <= 9; d++) {\n        int\
        \ ra = max(0, curA0 - count2[d]);\n        int rb = max(0, curB0 - count3[d]);\n\
        \        int rc = max(0, curC0 - count5[d]);\n        int rd = max(0, curD0\
        \ - count7[d]);\n        if (rc + rd + _dp![ra][rb] <= n - 1 - L) {\n      \
        \    String res = num.substring(0, L) + d.toString();\n          int remA =\
        \ ra, remB = rb, remC = rc, remD = rd;\n          for (int i = L + 1; i < n;\
        \ i++) {\n            for (int v = 1; v <= 9; v++) {\n              int na =\
        \ max(0, remA - count2[v]);\n              int nb = max(0, remB - count3[v]);\n\
        \              int nc = max(0, remC - count5[v]);\n              int nd = max(0,\
        \ remD - count7[v]);\n              if (nc + nd + _dp![na][nb] <= n - 1 - i)\
        \ {\n                res += v.toString();\n                remA = na; remB =\
        \ nb; remC = nc; remD = nd;\n                break;\n              }\n     \
        \       }\n          }\n          return res;\n        }\n      }\n    }\n\n\
        \    int kLen = max(n + 1, c0 + d0 + _dp![a0][b0]);\n    String res = \"\";\n\
        \    int remA = a0, remB = b0, remC = c0, remD = d0;\n    for (int i = 0; i\
        \ < kLen; i++) {\n      for (int v = 1; v <= 9; v++) {\n        int na = max(0,\
        \ remA - count2[v]);\n        int nb = max(0, remB - count3[v]);\n        int\
        \ nc = max(0, remC - count5[v]);\n        int nd = max(0, remD - count7[v]);\n\
        \        if (nc + nd + _dp![na][nb] <= kLen - 1 - i) {\n          res += v.toString();\n\
        \          remA = na; remB = nb; remC = nc; remD = nd;\n          break;\n \
        \       }\n      }\n    }\n    return res;\n  }\n}"
      go: "func smallestNumber(num string, t int64) string {\n\tcount2 := []int{0, 0,\
        \ 1, 0, 2, 0, 1, 0, 3, 0}\n\tcount3 := []int{0, 0, 0, 1, 0, 0, 1, 0, 0, 2}\n\
        \tcount5 := []int{0, 0, 0, 0, 0, 1, 0, 0, 0, 0}\n\tcount7 := []int{0, 0, 0,\
        \ 0, 0, 0, 0, 1, 0, 0}\n\n\tdp := [65][65]int{}\n\tfor i := 0; i < 65; i++ {\n\
        \t\tfor j := 0; j < 65; j++ {\n\t\t\tdp[i][j] = 1000\n\t\t}\n\t}\n\tdp[0][0]\
        \ = 0\n\tfor a := 0; a <= 60; a++ {\n\t\tfor b := 0; b <= 60; b++ {\n\t\t\t\
        if a == 0 && b == 0 {\n\t\t\t\tcontinue\n\t\t\t}\n\t\t\tchoices := [][]int{{1,\
        \ 0}, {0, 1}, {2, 0}, {1, 1}, {3, 0}, {0, 2}}\n\t\t\tfor _, pair := range choices\
        \ {\n\t\t\t\tna, nb := a-pair[0], b-pair[1]\n\t\t\t\tif na < 0 { na = 0 }\n\t\
        \t\t\tif nb < 0 { nb = 0 }\n\t\t\t\tif na < a || nb < b {\n\t\t\t\t\tif 1+dp[na][nb]\
        \ < dp[a][b] {\n\t\t\t\t\t\tdp[a][b] = 1 + dp[na][nb]\n\t\t\t\t\t}\n\t\t\t\t\
        }\n\t\t\t}\n\t\t}\n\t}\n\n\ta0, b0, c0, d0 := 0, 0, 0, 0\n\ttempT := t\n\tfor\
        \ tempT%2 == 0 { tempT /= 2; a0++ }\n\tfor tempT%3 == 0 { tempT /= 3; b0++ }\n\
        \tfor tempT%5 == 0 { tempT /= 5; c0++ }\n\tfor tempT%7 == 0 { tempT /= 7; d0++\
        \ }\n\tif tempT > 1 { return \"-1\" }\n\n\tn := len(num)\n\tp2, p3, p5, p7 :=\
        \ make([]int, n+1), make([]int, n+1), make([]int, n+1), make([]int, n+1)\n\t\
        firstZero := n\n\tfor i := 0; i < n; i++ {\n\t\td := int(num[i] - '0')\n\t\t\
        if d == 0 {\n\t\t\tfirstZero = i\n\t\t\tbreak\n\t\t}\n\t\tp2[i+1] = p2[i] +\
        \ count2[d]\n\t\tp3[i+1] = p3[i] + count3[d]\n\t\tp5[i+1] = p5[i] + count5[d]\n\
        \t\tp7[i+1] = p7[i] + count7[d]\n\t}\n\n\tif firstZero == n && p2[n] >= a0 &&\
        \ p3[n] >= b0 && p5[n] >= c0 && p7[n] >= d0 {\n\t\treturn num\n\t}\n\n\tfor\
        \ L := firstZero; L >= 0; L-- {\n\t\tif L == n { continue }\n\t\tcurA0, curB0,\
        \ curC0, curD0 := a0-p2[L], b0-p3[L], c0-p5[L], d0-p7[L]\n\t\tfor d := int(num[L]-'0')\
        \ + 1; d <= 9; d++ {\n\t\t\tra, rb, rc, rd := curA0-count2[d], curB0-count3[d],\
        \ curC0-count5[d], curD0-count7[d]\n\t\t\tif ra < 0 { ra = 0 }\n\t\t\tif rb\
        \ < 0 { rb = 0 }\n\t\t\tif rc < 0 { rc = 0 }\n\t\t\tif rd < 0 { rd = 0 }\n\t\
        \t\tif rc+rd+dp[ra][rb] <= n-1-L {\n\t\t\t\tans := num[:L] + string(byte(d+'0'))\n\
        \t\t\t\tremA, remB, remC, remD := ra, rb, rc, rd\n\t\t\t\tfor i := L + 1; i\
        \ < n; i++ {\n\t\t\t\t\tfor v := 1; v <= 9; v++ {\n\t\t\t\t\t\tna, nb, nc, nd\
        \ := remA-count2[v], remB-count3[v], remC-count5[v], remD-count7[v]\n\t\t\t\t\
        \t\tif na < 0 { na = 0 }\n\t\t\t\t\t\tif nb < 0 { nb = 0 }\n\t\t\t\t\t\tif nc\
        \ < 0 { nc = 0 }\n\t\t\t\t\t\tif nd < 0 { nd = 0 }\n\t\t\t\t\t\tif nc+nd+dp[na][nb]\
        \ <= n-1-i {\n\t\t\t\t\t\t\tans += string(byte(v + '0'))\n\t\t\t\t\t\t\tremA,\
        \ remB, remC, remD = na, nb, nc, nd\n\t\t\t\t\t\t\tbreak\n\t\t\t\t\t\t}\n\t\t\
        \t\t\t}\n\t\t\t\t}\n\t\t\t\treturn ans\n\t\t\t}\n\t\t}\n\t}\n\n\tkLen := n +\
        \ 1\n\tif c0+d0+dp[a0][b0] > kLen {\n\t\tkLen = c0 + d0 + dp[a0][b0]\n\t}\n\t\
        ans := \"\"\n\tremA, remB, remC, remD := a0, b0, c0, d0\n\tfor i := 0; i < kLen;\
        \ i++ {\n\t\tfor v := 1; v <= 9; v++ {\n\t\t\tna, nb, nc, nd := remA-count2[v],\
        \ remB-count3[v], remC-count5[v], remD-count7[v]\n\t\t\tif na < 0 { na = 0 }\n\
        \t\t\tif nb < 0 { nb = 0 }\n\t\t\tif nc < 0 { nc = 0 }\n\t\t\tif nd < 0 { nd\
        \ = 0 }\n\t\t\tif nc+nd+dp[na][nb] <= kLen-1-i {\n\t\t\t\tans += string(byte(v\
        \ + '0'))\n\t\t\t\tremA, remB, remC, remD = na, nb, nc, nd\n\t\t\t\tbreak\n\t\
        \t\t}\n\t\t}\n\t}\n\treturn ans\n}"
      ruby: "def smallest_number(num, t)\n  count2 = [0, 0, 1, 0, 2, 0, 1, 0, 3, 0]\n\
        \  count3 = [0, 0, 0, 1, 0, 0, 1, 0, 0, 2]\n  count5 = [0, 0, 0, 0, 0, 1, 0,\
        \ 0, 0, 0]\n  count7 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]\n\n  dp = Array.new(65)\
        \ { Array.new(65, 1000) }\n  dp[0][0] = 0\n  (0..60).each do |a|\n    (0..60).each\
        \ do |b|\n      next if a == 0 && b == 0\n      choices = [[1, 0], [0, 1], [2,\
        \ 0], [1, 1], [3, 0], [0, 2]]\n      choices.each do |ad, bd|\n        na =\
        \ [0, a - ad].max\n        nb = [0, b - bd].max\n        dp[a][b] = [dp[a][b],\
        \ 1 + dp[na][nb]].min if na < a || nb < b\n      end\n    end\n  end\n\n  a0,\
        \ b0, c0, d0 = 0, 0, 0, 0\n  temp_t = t\n  while temp_t % 2 == 0; temp_t /=\
        \ 2; a0 += 1; end\n  while temp_t % 3 == 0; temp_t /= 3; b0 += 1; end\n  while\
        \ temp_t % 5 == 0; temp_t /= 5; c0 += 1; end\n  while temp_t % 7 == 0; temp_t\
        \ /= 7; d0 += 1; end\n  return \"-1\" if temp_t > 1\n\n  n = num.length\n  p2\
        \ = Array.new(n + 1, 0)\n  p3 = Array.new(n + 1, 0)\n  p5 = Array.new(n + 1,\
        \ 0)\n  p7 = Array.new(n + 1, 0)\n  first_zero = n\n  n.times do |i|\n    d\
        \ = num[i].to_i\n    if d == 0\n      first_zero = i\n      break\n    end\n\
        \    p2[i+1] = p2[i] + count2[d]\n    p3[i+1] = p3[i] + count3[d]\n    p5[i+1]\
        \ = p5[i] + count5[d]\n    p7[i+1] = p7[i] + count7[d]\n  end\n\n  if first_zero\
        \ == n && p2[n] >= a0 && p3[n] >= b0 && p5[n] >= c0 && p7[n] >= d0\n    return\
        \ num\n  end\n\n  [n - 1, first_zero].min.downto(0) do |l|\n    cur_a0, cur_b0,\
        \ cur_c0, cur_d0 = a0 - p2[l], b0 - p3[l], c0 - p5[l], d0 - p7[l]\n    (num[l].to_i\
        \ + 1..9).each do |d|\n      ra, rb, rc, rd = [0, cur_a0 - count2[d]].max, [0,\
        \ cur_b0 - count3[d]].max, [0, cur_c0 - count5[d]].max, [0, cur_d0 - count7[d]].max\n\
        \      if rc + rd + dp[ra][rb] <= n - 1 - l\n        ans = num[0...l] + d.to_s\n\
        \        rem_a, rem_b, rem_c, rem_d = ra, rb, rc, rd\n        (l + 1...n).each\
        \ do |i|\n          (1..9).each do |v|\n            na, nb, nc, nd = [0, rem_a\
        \ - count2[v]].max, [0, rem_b - count3[v]].max, [0, rem_c - count5[v]].max,\
        \ [0, rem_d - count7[v]].max\n            if nc + nd + dp[na][nb] <= n - 1 -\
        \ i\n              ans += v.to_s\n              rem_a, rem_b, rem_c, rem_d =\
        \ na, nb, nc, nd\n              break\n            end\n          end\n    \
        \    end\n        return ans\n      end\n    end\n  end\n\n  k_len = [n + 1,\
        \ c0 + d0 + dp[a0][b0]].max\n  ans = \"\"\n  rem_a, rem_b, rem_c, rem_d = a0,\
        \ b0, c0, d0\n  k_len.times do |i|\n    (1..9).each do |v|\n      na, nb, nc,\
        \ nd = [0, rem_a - count2[v]].max, [0, rem_b - count3[v]].max, [0, rem_c - count5[v]].max,\
        \ [0, rem_d - count7[v]].max\n      if nc + nd + dp[na][nb] <= k_len - 1 - i\n\
        \        ans += v.to_s\n        rem_a, rem_b, rem_c, rem_d = na, nb, nc, nd\n\
        \        break\n      end\n    end\n  end\n  ans\nend"
      scala: "object Solution {\n    def smallestNumber(num: String, t: Long): String\
        \ = {\n        val count2 = Array(0, 0, 1, 0, 2, 0, 1, 0, 3, 0)\n        val\
        \ count3 = Array(0, 0, 0, 1, 0, 0, 1, 0, 0, 2)\n        val count5 = Array(0,\
        \ 0, 0, 0, 0, 1, 0, 0, 0, 0)\n        val count7 = Array(0, 0, 0, 0, 0, 0, 0,\
        \ 1, 0, 0)\n\n        val dp = Array.fill(65, 65)(1000)\n        dp(0)(0) =\
        \ 0\n        for (a <- 0 to 60; b <- 0 to 60 if !(a == 0 && b == 0)) {\n   \
        \         val choices = List((1, 0), (0, 1), (2, 0), (1, 1), (3, 0), (0, 2))\n\
        \            for ((ad, bd) <- choices) {\n                val na = Math.max(0,\
        \ a - ad)\n                val nb = Math.max(0, b - bd)\n                if\
        \ (na < a || nb < b) {\n                    dp(a)(b) = Math.min(dp(a)(b), 1\
        \ + dp(na)(nb))\n                }\n            }\n        }\n\n        var\
        \ a0 = 0; var b0 = 0; var c0 = 0; var d0 = 0\n        var tempT = t\n      \
        \  while (tempT % 2 == 0) { tempT /= 2; a0 += 1 }\n        while (tempT % 3\
        \ == 0) { tempT /= 3; b0 += 1 }\n        while (tempT % 5 == 0) { tempT /= 5;\
        \ c0 += 1 }\n        while (tempT % 7 == 0) { tempT /= 7; d0 += 1 }\n      \
        \  if (tempT > 1) return \"-1\"\n\n        val n = num.length\n        val p2\
        \ = new Array[Int](n + 1)\n        val p3 = new Array[Int](n + 1)\n        val\
        \ p5 = new Array[Int](n + 1)\n        val p7 = new Array[Int](n + 1)\n     \
        \   var firstZero = n\n        var i = 0\n        while (i < n) {\n        \
        \    val d = num(i) - '0'\n            if (d == 0) { firstZero = i; i = n }\n\
        \            else {\n                p2(i + 1) = p2(i) + count2(d)\n       \
        \         p3(i + 1) = p3(i) + count3(d)\n                p5(i + 1) = p5(i) +\
        \ count5(d)\n                p7(i + 1) = p7(i) + count7(d)\n               \
        \ i += 1\n            }\n        }\n\n        if (firstZero == n && p2(n) >=\
        \ a0 && p3(n) >= b0 && p5(n) >= c0 && p7(n) >= d0) {\n            return num\n\
        \        }\n\n        for (L <- Math.min(n - 1, firstZero) to 0 by -1) {\n \
        \           val curA0 = a0 - p2(L); val curB0 = b0 - p3(L)\n            val\
        \ curC0 = c0 - p5(L); val curD0 = d0 - p7(L)\n            for (d <- (num(L)\
        \ - '0' + 1) to 9) {\n                val ra = Math.max(0, curA0 - count2(d))\n\
        \                val rb = Math.max(0, curB0 - count3(d))\n                val\
        \ rc = Math.max(0, curC0 - count5(d))\n                val rd = Math.max(0,\
        \ curD0 - count7(d))\n                if (rc + rd + dp(ra)(rb) <= n - 1 - L)\
        \ {\n                    val res = new StringBuilder(num.substring(0, L))\n\
        \                    res.append(d.toString)\n                    var remA =\
        \ ra; var remB = rb; var remC = rc; var remD = rd\n                    for (j\
        \ <- L + 1 until n) {\n                        var found = false\n         \
        \               for (v <- 1 to 9 if !found) {\n                            val\
        \ na = Math.max(0, remA - count2(v))\n                            val nb = Math.max(0,\
        \ remB - count3(v))\n                            val nc = Math.max(0, remC -\
        \ count5(v))\n                            val nd = Math.max(0, remD - count7(v))\n\
        \                            if (nc + nd + dp(na)(nb) <= n - 1 - j) {\n    \
        \                            res.append(v.toString)\n                      \
        \          remA = na; remB = nb; remC = nc; remD = nd\n                    \
        \            found = true\n                            }\n                 \
        \       }\n                    }\n                    return res.toString()\n\
        \                }\n            }\n        }\n\n        val kLen = Math.max(n\
        \ + 1, c0 + d0 + dp(a0)(b0))\n        val res = new StringBuilder\n        var\
        \ remA = a0; var remB = b0; var remC = c0; var remD = d0\n        for (i <-\
        \ 0 until kLen) {\n            var found = false\n            for (v <- 1 to\
        \ 9 if !found) {\n                val na = Math.max(0, remA - count2(v))\n \
        \               val nb = Math.max(0, remB - count3(v))\n                val\
        \ nc = Math.max(0, remC - count5(v))\n                val nd = Math.max(0, remD\
        \ - count7(v))\n                if (nc + nd + dp(na)(nb) <= kLen - 1 - i) {\n\
        \                    res.append(v.toString)\n                    remA = na;\
        \ remB = nb; remC = nc; remD = nd\n                    found = true\n      \
        \          }\n            }\n        }\n        res.toString()\n    }\n}"
      rust: "impl Solution {\n    pub fn smallest_number(num: String, t: i64) -> String\
        \ {\n        let mut temp_t = t;\n        let (mut a, mut b, mut c, mut d) =\
        \ (0, 0, 0, 0);\n        while temp_t % 2 == 0 { temp_t /= 2; a += 1; }\n  \
        \      while temp_t % 3 == 0 { temp_t /= 3; b += 1; }\n        while temp_t\
        \ % 5 == 0 { temp_t /= 5; c += 1; }\n        while temp_t % 7 == 0 { temp_t\
        \ /= 7; d += 1; }\n        if temp_t > 1 { return \"-1\".to_string(); }\n\n\
        \        let mut dp = vec![vec![String::new(); 31]; 48];\n        for i in 0..48\
        \ {\n            for j in 0..31 {\n                if i == 0 && j == 0 { continue;\
        \ }\n                let mut best: Option<String> = None;\n                for\
        \ &(digit, da, db) in &[(2, 1, 0), (3, 0, 1), (4, 2, 0), (6, 1, 1), (8, 3, 0),\
        \ (9, 0, 2)] {\n                    let pi = if i >= da { i - da } else { 0\
        \ };\n                    let pj = if j >= db { j - db } else { 0 };\n     \
        \               let mut s = dp[pi][pj].clone();\n                    s.push(std::char::from_digit(digit\
        \ as u32, 10).unwrap());\n                    let mut sc: Vec<char> = s.chars().collect();\n\
        \                    sc.sort();\n                    let ss: String = sc.into_iter().collect();\n\
        \                    if best.is_none() || ss.len() < best.as_ref().unwrap().len()\
        \ || (ss.len() == best.as_ref().unwrap().len() && ss < *best.as_ref().unwrap())\
        \ {\n                        best = Some(ss);\n                    }\n     \
        \           }\n                dp[i][j] = best.unwrap();\n            }\n  \
        \      }\n\n        let n = num.len();\n        let chars: Vec<char> = num.chars().collect();\n\
        \        let mut first_zero = n;\n        for (i, &ch) in chars.iter().enumerate()\
        \ {\n            if ch == '0' { first_zero = i; break; }\n        }\n\n    \
        \    if first_zero == n {\n            let (mut ra, mut rb, mut rc, mut rd)\
        \ = (a, b, c, d);\n            for &ch in &chars {\n                let (da,\
        \ db, dc, dd) = Self::get_factors(ch.to_digit(10).unwrap());\n             \
        \   ra = ra.saturating_sub(da); rb = rb.saturating_sub(db); rc = rc.saturating_sub(dc);\
        \ rd = rd.saturating_sub(dd);\n            }\n            if ra == 0 && rb ==\
        \ 0 && rc == 0 && rd == 0 { return num; }\n        }\n\n        for i in (0..=first_zero.min(n\
        \ - 1)).rev() {\n            let mut ra = a; let mut rb = b; let mut rc = c;\
        \ let mut rd = d;\n            let mut possible = true;\n            for j in\
        \ 0..i {\n                if chars[j] == '0' { possible = false; break; }\n\
        \                let (da, db, dc, dd) = Self::get_factors(chars[j].to_digit(10).unwrap());\n\
        \                ra = ra.saturating_sub(da); rb = rb.saturating_sub(db); rc\
        \ = rc.saturating_sub(dc); rd = rd.saturating_sub(dd);\n            }\n    \
        \        if !possible { continue; }\n            let start_v = if chars[i] ==\
        \ '0' { 1 } else { chars[i].to_digit(10).unwrap() + 1 };\n            for v\
        \ in start_v..10 {\n                let (da, db, dc, dd) = Self::get_factors(v);\n\
        \                let nra = ra.saturating_sub(da); let nrb = rb.saturating_sub(db);\
        \ let nrc = rc.saturating_sub(dc); let nrd = rd.saturating_sub(dd);\n      \
        \          let needed_str = &dp[nra as usize][nrb as usize];\n             \
        \   let total_needed = nrc as usize + nrd as usize + needed_str.len();\n   \
        \             if total_needed <= n - 1 - i {\n                    let mut res\
        \ = chars[..i].iter().collect::<String>();\n                    res.push(std::char::from_digit(v,\
        \ 10).unwrap());\n                    let mut counts = [0; 10];\n          \
        \          counts[1] = (n - 1 - i - total_needed) as i32;\n                \
        \    counts[5] = nrc as i32; counts[7] = nrd as i32;\n                    for\
        \ ch in needed_str.chars() { counts[ch.to_digit(10).unwrap() as usize] += 1;\
        \ }\n                    for digit in 1..10 { for _ in 0..counts[digit] { res.push(std::char::from_digit(digit\
        \ as u32, 10).unwrap()); } }\n                    return res;\n            \
        \    }\n            }\n        }\n\n        let min_needed_len = (c + d) as\
        \ usize + dp[a as usize][b as usize].len();\n        let target_len = n.max(min_needed_len)\
        \ + 1;\n        let L = if min_needed_len > n { min_needed_len } else { target_len\
        \ };\n        let mut res = String::new();\n        let mut counts = [0; 10];\n\
        \        counts[1] = (L - min_needed_len) as i32; counts[5] = c as i32; counts[7]\
        \ = d as i32;\n        for ch in dp[a as usize][b as usize].chars() { counts[ch.to_digit(10).unwrap()\
        \ as usize] += 1; }\n        for digit in 1..10 { for _ in 0..counts[digit]\
        \ { res.push(std::char::from_digit(digit as u32, 10).unwrap()); } }\n      \
        \  res\n    }\n\n    fn get_factors(v: u32) -> (i64, i64, i64, i64) {\n    \
        \    match v {\n            2 => (1, 0, 0, 0), 3 => (0, 1, 0, 0), 4 => (2, 0,\
        \ 0, 0), 5 => (0, 0, 1, 0),\n            6 => (1, 1, 0, 0), 7 => (0, 0, 0, 1),\
        \ 8 => (3, 0, 0, 0), 9 => (0, 2, 0, 0),\n            _ => (0, 0, 0, 0),\n  \
        \      }\n    }\n}"
      racket: "(define/contract (smallest-number num t)\n  (-> string? exact-integer?\
        \ string?)\n  (define (get-factors v)\n    (cond\n      [(= v 2) '(1 0 0 0)]\
        \ [(= v 3) '(0 1 0 0)] [(= v 4) '(2 0 0 0)] [(= v 5) '(0 0 1 0)]\n      [(=\
        \ v 6) '(1 1 0 0)] [(= v 7) '(0 0 0 1)] [(= v 8) '(3 0 0 0)] [(= v 9) '(0 2\
        \ 0 0)]\n      [else '(0 0 0 0)]))\n  (let* ([a 0] [b 0] [c 0] [d 0] [temp-t\
        \ t])\n    (let-values ([(a temp-t) (let loop ([ca 0] [ct temp-t]) (if (and\
        \ (> ct 0) (= 0 (remainder ct 2))) (loop (+ ca 1) (/ ct 2)) (values ca ct)))]\n\
        \                 [(b temp-t) (let loop ([cb 0] [ct temp-t]) (if (and (> ct\
        \ 0) (= 0 (remainder ct 3))) (loop (+ cb 1) (/ ct 3)) (values cb ct)))]\n  \
        \               [(c temp-t) (let loop ([cc 0] [ct temp-t]) (if (and (> ct 0)\
        \ (= 0 (remainder ct 5))) (loop (+ cc 1) (/ ct 5)) (values cc ct)))]\n     \
        \            [(d temp-t) (let loop ([cd 0] [ct temp-t]) (if (and (> ct 0) (=\
        \ 0 (remainder ct 7))) (loop (+ cd 1) (/ ct 7)) (values cd ct)))])\n      (if\
        \ (> temp-t 1) \"-1\"\n          (let ([dp (make-vector 48)])\n            (for\
        \ ([i 48]) (vector-set! dp i (make-vector 31 \"\")))\n            (for* ([i\
        \ 48] [j 31])\n              (when (not (and (= i 0) (= j 0)))\n           \
        \     (let ([best #f])\n                  (for ([digit '(2 3 4 6 8 9)])\n  \
        \                  (let* ([f (get-factors digit)]\n                        \
        \   [pi (max 0 (- i (car f)))] [pj (max 0 (- j (cadr f)))]\n               \
        \            [s (string-append (vector-ref (vector-ref dp pi) pj) (number->string\
        \ digit))]\n                           [ss (list->string (sort (string->list\
        \ s) char<?))])\n                      (when (or (not best) (< (string-length\
        \ ss) (string-length best)) (and (= (string-length ss) (string-length best))\
        \ (string<? ss best)))\n                        (set! best ss))))\n        \
        \          (vector-set! (vector-ref dp i) j best))))\n            (let* ([n\
        \ (string-length num)] [chars (string->list num)]\n                   [first-zero\
        \ (or (for/first ([i n] #:when (char=? (list-ref chars i) #\\0)) i) n)])\n \
        \             (define (check-orig)\n                (if (= first-zero n)\n \
        \                   (let ([ra a] [rb b] [rc c] [rd d])\n                   \
        \   (for ([ch chars])\n                        (let ([f (get-factors (- (char->integer\
        \ ch) 48))])\n                          (set! ra (max 0 (- ra (car f)))) (set!\
        \ rb (max 0 (- rb (cadr f))))\n                          (set! rc (max 0 (-\
        \ rc (caddr f)))) (set! rd (max 0 (- rd (cadddr f))))))\n                  \
        \    (and (= ra 0) (= rb 0) (= rc 0) (= rd 0)))\n                    #f))\n\
        \              (if (check-orig) num\n                  (let ([ans #f])\n   \
        \                 (for ([i (in-range (min (- n 1) first-zero) -1 -1)] #:break\
        \ ans)\n                      (let ([ra a] [rb b] [rc c] [rd d])\n         \
        \               (for ([j i])\n                          (let ([f (get-factors\
        \ (- (char->integer (list-ref chars j)) 48))])\n                           \
        \ (set! ra (max 0 (- ra (car f)))) (set! rb (max 0 (- rb (cadr f))))\n     \
        \                       (set! rc (max 0 (- rc (caddr f)))) (set! rd (max 0 (-\
        \ rd (cadddr f))))))\n                        (let ([start-v (if (char=? (list-ref\
        \ chars i) #\\0) 1 (+ 1 (- (char->integer (list-ref chars i)) 48)))])\n    \
        \                      (for ([v (in-range start-v 10)] #:break ans)\n      \
        \                      (let* ([f (get-factors v)]\n                        \
        \           [nra (max 0 (- ra (car f)))] [nrb (max 0 (- rb (cadr f)))]\n   \
        \                                [nrc (max 0 (- rc (caddr f)))] [nrd (max 0\
        \ (- rd (cadddr f)))]\n                                   [needed-str (vector-ref\
        \ (vector-ref dp nra) nrb)]\n                                   [total-needed\
        \ (+ nrc nrd (string-length needed-str))])\n                              (when\
        \ (<= total-needed (- n 1 i))\n                                (let ([res (substring\
        \ num 0 i)] [counts (make-vector 10 0)])\n                                 \
        \ (vector-set! counts 1 (- n 1 i total-needed))\n                          \
        \        (vector-set! counts 5 nrc) (vector-set! counts 7 nrd)\n           \
        \                       (for ([ch (string->list needed-str)]) (let ([d (- (char->integer\
        \ ch) 48)]) (vector-set! counts d (+ 1 (vector-ref counts d)))))\n         \
        \                         (let ([suffix (apply string-append (for/list ([d (in-range\
        \ 1 10)]) (make-string (vector-ref counts d) (integer->char (+ d 48)))))]\n\
        \                                        [vs (number->string v)])\n        \
        \                            (set! ans (string-append res vs suffix))))))))))\n\
        \                    (if ans ans\n                        (let* ([min-len (+\
        \ c d (string-length (vector-ref (vector-ref dp a) b)))]\n                 \
        \              [L (max (+ n 1) min-len)] [counts (make-vector 10 0)]\n     \
        \                          [needed-str (vector-ref (vector-ref dp a) b)])\n\
        \                          (vector-set! counts 1 (- L min-len)) (vector-set!\
        \ counts 5 c) (vector-set! counts 7 d)\n                          (for ([ch\
        \ (string->list needed-str)]) (let ([d (- (char->integer ch) 48)]) (vector-set!\
        \ counts d (+ 1 (vector-ref counts d)))))\n                          (apply\
        \ string-append (for/list ([d (in-range 1 10)]) (make-string (vector-ref counts\
        \ d) (integer->char (+ d 48)))))))))))))))"
      erlang: "-spec smallest_number(Num :: unicode:unicode_binary(), T :: integer())\
        \ -> unicode:unicode_binary().\nsmallest_number(Num, T) ->\n    {A, B, C, D,\
        \ TempT} = get_t_factors(T),\n    if TempT > 1 -> <<\"-1\">>;\n       true ->\n\
        \           DP = build_dp(),\n           Chars = binary_to_list(Num),\n    \
        \       N = length(Chars),\n           FirstZero = find_first_zero(Chars, 0,\
        \ N),\n           Check = case FirstZero of\n                       N -> check_orig(Chars,\
        \ A, B, C, D);\n                       _ -> false\n                   end,\n\
        \           if Check -> Num;\n              true -> solve(Num, Chars, N, FirstZero,\
        \ A, B, C, D, DP)\n           end\n    end.\n\nget_t_factors(T) ->\n    {A,\
        \ T1} = count_factors(T, 2, 0),\n    {B, T2} = count_factors(T1, 3, 0),\n  \
        \  {C, T3} = count_factors(T2, 5, 0),\n    {D, T4} = count_factors(T3, 7, 0),\n\
        \    {A, B, C, D, T4}.\n\ncount_factors(T, P, Count) when T > 0, T rem P ==\
        \ 0 -> count_factors(T div P, P, Count + 1);\ncount_factors(T, _, Count) ->\
        \ {Count, T}.\n\nfind_first_zero([], _, N) -> N;\nfind_first_zero([$0|_], I,\
        \ _) -> I;\nfind_first_zero([_|T], I, N) -> find_first_zero(T, I + 1, N).\n\n\
        get_digit_factors($1) -> {0, 0, 0, 0}; get_digit_factors($2) -> {1, 0, 0, 0};\n\
        get_digit_factors($3) -> {0, 1, 0, 0}; get_digit_factors($4) -> {2, 0, 0, 0};\n\
        get_digit_factors($5) -> {0, 0, 1, 0}; get_digit_factors($6) -> {1, 1, 0, 0};\n\
        get_digit_factors($7) -> {0, 0, 0, 1}; get_digit_factors($8) -> {3, 0, 0, 0};\n\
        get_digit_factors($9) -> {0, 2, 0, 0}; get_digit_factors(V) when is_integer(V)\
        \ -> get_digit_factors(V + $0).\n\ncheck_orig([], A, B, C, D) -> A =< 0 andalso\
        \ B =< 0 andalso C =< 0 andalso D =< 0;\ncheck_orig([H|T], A, B, C, D) ->\n\
        \    {DA, DB, DC, DD} = get_digit_factors(H),\n    check_orig(T, A - DA, B -\
        \ DB, C - DC, D - DD).\n\nbuild_dp() ->\n    DP = maps:new(),\n    DP0 = DP#{{0,0}\
        \ => \"\"},\n    Digits = [{2,1,0}, {3,0,1}, {4,2,0}, {6,1,1}, {8,3,0}, {9,0,2}],\n\
        \    lists:foldl(fun(I, AccI) ->\n        lists:foldl(fun(J, AccJ) ->\n    \
        \        if I == 0, J == 0 -> AccJ;\n               true ->\n              \
        \     Best = lists:foldl(fun({Digit, DA, DB}, CurrentBest) ->\n            \
        \           PI = max(0, I - DA), PJ = max(0, J - DB),\n                    \
        \   S = lists:sort([Digit + $0 | maps:get({PI, PJ}, AccJ)]),\n             \
        \          if CurrentBest == undefined -> S;\n                          length(S)\
        \ < length(CurrentBest) -> S;\n                          length(S) == length(CurrentBest),\
        \ S < CurrentBest -> S;\n                          true -> CurrentBest\n   \
        \                    end\n                   end, undefined, Digits),\n    \
        \               AccJ#{{I, J} => Best}\n            end\n        end, AccI, lists:seq(0,\
        \ 30))\n    end, DP0, lists:seq(0, 47)).\n\nsolve(Num, Chars, N, FirstZero,\
        \ A, B, C, D, DP) ->\n    case find_same_length(Num, Chars, N, min(N - 1, FirstZero),\
        \ A, B, C, D, DP) of\n        {ok, Res} -> Res;\n        none ->\n         \
        \   NeededStr = maps:get({A, B}, DP),\n            MinLen = C + D + length(NeededStr),\n\
        \            L = if MinLen > N -> MinLen; true -> N + 1 end,\n            Counts\
        \ = count_sort_suffix(L - MinLen, C, D, NeededStr),\n            list_to_binary(build_from_counts(Counts))\n\
        \    end.\n\nfind_same_length(_, _, _, -1, _, _, _, _, _) -> none;\nfind_same_length(Num,\
        \ Chars, N, I, A, B, C, D, DP) ->\n    Prefix = lists:sublist(Chars, I),\n \
        \   {PA, PB, PC, PD} = prefix_factors(Prefix, 0, 0, 0, 0),\n    RA = max(0,\
        \ A - PA), RB = max(0, B - PB), RC = max(0, C - PC), RD = max(0, D - PD),\n\
        \    StartV = if lists:nth(I + 1, Chars) == $0 -> 1; true -> lists:nth(I + 1,\
        \ Chars) - $0 + 1 end,\n    case try_v(I, N, StartV, RA, RB, RC, RD, DP) of\n\
        \        {ok, Suffix} -> {ok, list_to_binary(lists:sublist(Chars, I) ++ Suffix)};\n\
        \        none -> find_same_length(Num, Chars, N, I - 1, A, B, C, D, DP)\n  \
        \  end.\n\ntry_v(_, _, 10, _, _, _, _, _) -> none;\ntry_v(I, N, V, RA, RB, RC,\
        \ RD, DP) ->\n    {DA, DB, DC, DD} = get_digit_factors(V),\n    NRA = max(0,\
        \ RA - DA), NRB = max(0, RB - DB), NRC = max(0, RC - DC), NRD = max(0, RD -\
        \ DD),\n    NeededStr = maps:get({NRA, NRB}, DP),\n    TotalNeeded = NRC + NRD\
        \ + length(NeededStr),\n    if TotalNeeded =< N - 1 - I ->\n           Counts\
        \ = count_sort_suffix(N - 1 - I - TotalNeeded, NRC, NRD, NeededStr),\n     \
        \      {ok, [V + $0 | build_from_counts(Counts)]};\n       true -> try_v(I,\
        \ N, V + 1, RA, RB, RC, RD, DP)\n    end.\n\nprefix_factors([], A, B, C, D)\
        \ -> {A, B, C, D};\nprefix_factors([H|T], A, B, C, D) ->\n    {DA, DB, DC, DD}\
        \ = get_digit_factors(H),\n    prefix_factors(T, A + DA, B + DB, C + DC, D +\
        \ DD).\n\ncount_sort_suffix(Ones, Fives, Sevens, NeededStr) ->\n    C0 = lists:duplicate(10,\
        \ 0),\n    C1 = set_count(C0, 1, Ones),\n    C2 = set_count(C1, 5, Fives),\n\
        \    C3 = set_count(C2, 7, Sevens),\n    lists:foldl(fun(Ch, Acc) -> \n    \
        \    D = Ch - $0,\n        set_count(Acc, D, lists:nth(D + 1, Acc) + 1)\n  \
        \  end, C3, NeededStr).\n\nset_count(Counts, D, Val) ->\n    lists:sublist(Counts,\
        \ D) ++ [Val] ++ lists:nthtail(D + 1, Counts).\n\nbuild_from_counts(Counts)\
        \ ->\n    lists:flatmap(fun(D) -> lists:duplicate(lists:nth(D + 1, Counts),\
        \ D + $0) end, lists:seq(1, 9))."
      elixir: "defmodule Solution do\n  @spec smallest_number(num :: String.t, t ::\
        \ integer) :: String.t\n  def smallest_number(num, t) do\n    {a, b, c, d, temp_t}\
        \ = get_t_factors(t)\n    if temp_t > 1 do\n      \"-1\"\n    else\n      dp\
        \ = build_dp()\n      chars = String.to_charlist(num)\n      n = length(chars)\n\
        \      first_zero = Enum.find_index(chars, &(&1 == ?0)) || n\n      if first_zero\
        \ == n and check_orig(chars, a, b, c, d) do\n        num\n      else\n     \
        \   solve(num, chars, n, first_zero, a, b, c, d, dp)\n      end\n    end\n \
        \ end\n\n  defp get_t_factors(t) do\n    {a, t1} = count_factors(t, 2, 0)\n\
        \    {b, t2} = count_factors(t1, 3, 0)\n    {c, t3} = count_factors(t2, 5, 0)\n\
        \    {d, t4} = count_factors(t3, 7, 0)\n    {a, b, c, d, t4}\n  end\n\n  defp\
        \ count_factors(t, p, count) when t > 0 and rem(t, p) == 0, do: count_factors(div(t,\
        \ p), p, count + 1)\n  defp count_factors(t, _, count), do: {count, t}\n\n \
        \ defp check_orig([], a, b, c, d), do: a <= 0 and b <= 0 and c <= 0 and d <=\
        \ 0\n  defp check_orig([h | t], a, b, c, d) do\n    {da, db, dc, dd} = get_digit_factors(h)\n\
        \    check_orig(t, a - da, b - db, c - dc, d - dd)\n  end\n\n  defp get_digit_factors(?1),\
        \ do: {0, 0, 0, 0}\n  defp get_digit_factors(?2), do: {1, 0, 0, 0}\n  defp get_digit_factors(?3),\
        \ do: {0, 1, 0, 0}\n  defp get_digit_factors(?4), do: {2, 0, 0, 0}\n  defp get_digit_factors(?5),\
        \ do: {0, 0, 1, 0}\n  defp get_digit_factors(?6), do: {1, 1, 0, 0}\n  defp get_digit_factors(?7),\
        \ do: {0, 0, 0, 1}\n  defp get_digit_factors(?8), do: {3, 0, 0, 0}\n  defp get_digit_factors(?9),\
        \ do: {0, 2, 0, 0}\n  defp get_digit_factors(v) when v in 1..9, do: get_digit_factors(v\
        \ + ?0)\n\n  defp build_dp() do\n    dp = %{{0, 0} => []}\n    digits = [{2,\
        \ 1, 0}, {3, 0, 1}, {4, 2, 0}, {6, 1, 1}, {8, 3, 0}, {9, 0, 2}]\n    Enum.reduce(0..47,\
        \ dp, fn i, acc_i ->\n      Enum.reduce(0..30, acc_i, fn j, acc_j ->\n     \
        \   if i == 0 and j == 0 do\n          acc_j\n        else\n          best =\
        \ Enum.reduce(digits, nil, fn {digit, da, db}, curr_best ->\n            pi\
        \ = max(0, i - da)\n            pj = max(0, j - db)\n            s = Enum.sort([digit\
        \ + ?0 | Map.get(acc_j, {pi, pj})])\n            if is_nil(curr_best) or length(s)\
        \ < length(curr_best) or (length(s) == length(curr_best) and s < curr_best),\
        \ do: s, else: curr_best\n          end)\n          Map.put(acc_j, {i, j}, best)\n\
        \        end\n      end)\n    end)\n  end\n\n  defp solve(num, chars, n, first_zero,\
        \ a, b, c, d, dp) do\n    case find_same_length(chars, n, min(n - 1, first_zero),\
        \ a, b, c, d, dp) do\n      {:ok, res} -> List.to_string(res)\n      :none ->\n\
        \        needed_str = Map.get(dp, {a, b})\n        min_len = c + d + length(needed_str)\n\
        \        l = if min_len > n, do: min_len, else: n + 1\n        counts = count_sort_suffix(l\
        \ - min_len, c, d, needed_str)\n        List.to_string(build_from_counts(counts))\n\
        \    end\n  end\n\n  defp find_same_length(_, _, -1, _, _, _, _, _), do: :none\n\
        \  defp find_same_length(chars, n, i, a, b, c, d, dp) do\n    prefix = Enum.take(chars,\
        \ i)\n    {pa, pb, pc, pd} = Enum.reduce(prefix, {0, 0, 0, 0}, fn ch, {ca, cb,\
        \ cc, cd} ->\n      {da, db, dc, dd} = get_digit_factors(ch)\n      {ca + da,\
        \ cb + db, cc + dc, cd + dd}\n    end)\n    ra = max(0, a - pa)\n    rb = max(0,\
        \ b - pb)\n    rc = max(0, c - pc)\n    rd = max(0, d - pd)\n    start_v = if\
        \ Enum.at(chars, i) == ?0, do: 1, else: Enum.at(chars, i) - ?0 + 1\n    case\
        \ try_v(i, n, start_v, ra, rb, rc, rd, dp) do\n      {:ok, suffix} -> {:ok,\
        \ prefix ++ suffix}\n      :none -> find_same_length(chars, n, i - 1, a, b,\
        \ c, d, dp)\n    end\n  end\n\n  defp try_v(_, _, 10, _, _, _, _, _), do: :none\n\
        \  defp try_v(i, n, v, ra, rb, rc, rd, dp) do\n    {da, db, dc, dd} = get_digit_factors(v)\n\
        \    nra = max(0, ra - da)\n    nrb = max(0, rb - db)\n    nrc = max(0, rc -\
        \ dc)\n    nrd = max(0, rd - dd)\n    needed_str = Map.get(dp, {nra, nrb})\n\
        \    total_needed = nrc + nrd + length(needed_str)\n    if total_needed <= n\
        \ - 1 - i do\n      counts = count_sort_suffix(n - 1 - i - total_needed, nrc,\
        \ nrd, needed_str)\n      {:ok, [v + ?0 | build_from_counts(counts)]}\n    else\n\
        \      try_v(i, n, v + 1, ra, rb, rc, rd, dp)\n    end\n  end\n\n  defp count_sort_suffix(ones,\
        \ fives, sevens, needed_str) do\n    counts = Tuple.duplicate(0, 10)\n    counts\
        \ = put_elem(counts, 1, ones)\n    counts = put_elem(counts, 5, fives)\n   \
        \ counts = put_elem(counts, 7, sevens)\n    Enum.reduce(needed_str, counts,\
        \ fn ch, acc ->\n      d = ch - ?0\n      put_elem(acc, d, elem(acc, d) + 1)\n\
        \    end)\n  end\n\n  defp build_from_counts(counts) do\n    Enum.flat_map(1..9,\
        \ fn d -> List.duplicate(d + ?0, elem(counts, d)) end)\n  end\nend"
    approach: The problem asks for the smallest zero-free number greater than or equal
      to $num$ such that the product of its digits is divisible by $t$. Since only digits
      1-9 are allowed, the product can only contain prime factors 2, 3, 5, and 7. If
      $t$ contains any prime factor larger than 7, it is impossible to satisfy the condition,
      and we return '-1'. We precalculate the prime factorization of $t$ as $2^a 3^b
      5^c 7^d$ and use dynamic programming to determine the minimum number of digits
      ($dp[a][b]$) and the lexicographically smallest set of digits ($combo[a][b]$)
      required to satisfy any required factors of 2 and 3. The factors of 5 and 7 are
      uniquely provided by digits 5 and 7, respectively.
    time_complexity: O(n) where n is the length of num. The algorithm iterates through
      the prefix of the string and for each position, checks up to 9 possible digits.
      Precomputing the DP table for factors of 2 and 3 takes constant time as the exponents
      for $t \le 10^{14}$ are small ($a \le 47, b \le 30$).
    space_complexity: O(n) to store the result string and the prefix prime factor counts.
      The DP table for prime factors of 2 and 3 occupies constant space relative to
      $n$.
    elapsed_time: 1898.408576965332
    model: gemini-3-flash-preview
    generated_at: '2026-08-07 02:45:40 '
---

## Problem #3348: Smallest Divisible Digit Product II

**Difficulty:** Hard

**Topics:** Math, String, Backtracking, Greedy, Number Theory

## Problem Description

<p>You are given a string <code>num</code> which represents a <strong>positive</strong> integer, and an integer <code>t</code>.</p>

<p>A number is called <strong>zero-free</strong> if <em>none</em> of its digits are 0.</p>

<p>Return a string representing the <strong>smallest</strong> <strong>zero-free</strong> number greater than or equal to <code>num</code> such that the <strong>product of its digits</strong> is divisible by <code>t</code>. If no such number exists, return <code>&quot;-1&quot;</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">num = &quot;1234&quot;, t = 256</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;1488&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>The smallest zero-free number that is greater than 1234 and has the product of its digits divisible by 256 is 1488, with the product of its digits equal to 256.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">num = &quot;12355&quot;, t = 50</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;12355&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>12355 is already zero-free and has the product of its digits divisible by 50, with the product of its digits equal to 150.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">num = &quot;11111&quot;, t = 26</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;-1&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>No number greater than 11111 has the product of its digits divisible by 26.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= num.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>num</code> consists only of digits in the range <code>[&#39;0&#39;, &#39;9&#39;]</code>.</li>
	<li><code>num</code> does not contain leading zeros.</li>
	<li><code>1 &lt;= t &lt;= 10<sup>14</sup></code></li>
</ul>


## Hints

1. `t` should only have 2, 3, 5 and 7 as prime factors.

2. Find the shortest suffix that must be changed.

3. Try to form the string greedily.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the smallest zero-free number greater than or equal to $num$ such that the product of its digits is divisible by $t$. Since only digits 1-9 are allowed, the product can only contain prime factors 2, 3, 5, and 7. If $t$ contains any prime factor larger than 7, it is impossible to satisfy the condition, and we return '-1'. We precalculate the prime factorization of $t$ as $2^a 3^b 5^c 7^d$ and use dynamic programming to determine the minimum number of digits ($dp[a][b]$) and the lexicographically smallest set of digits ($combo[a][b]$) required to satisfy any required factors of 2 and 3. The factors of 5 and 7 are uniquely provided by digits 5 and 7, respectively.

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
class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        a, b, c, d = 0, 0, 0, 0
        temp_t = t
        for p, count in [(2, 'a'), (3, 'b'), (5, 'c'), (7, 'd')]:
            while temp_t % p == 0:
                if count == 'a': a += 1
                elif count == 'b': b += 1
                elif count == 'c': c += 1
                else: d += 1
                temp_t //= p
        if temp_t > 1: return "-1"

        factors = {2: (1, 0), 3: (0, 1), 4: (2, 0), 6: (1, 1), 8: (3, 0), 9: (0, 2)}
        dp = [[100] * 40 for _ in range(60)]
        combo = [[""] * 40 for _ in range(60)]
        dp[0][0] = 0
        for i in range(60):
            for j in range(40):
                if i == 0 and j == 0: continue
                for digit in [2, 3, 4, 6, 8, 9]:
                    da, db = factors[digit]
                    pi, pj = max(0, i - da), max(0, j - db)
                    if dp[pi][pj] + 1 < dp[i][j]:
                        dp[i][j] = dp[pi][pj] + 1
                        combo[i][j] = "".join(sorted(str(digit) + combo[pi][pj]))
                    elif dp[pi][pj] + 1 == dp[i][j]:
                        new_c = "".join(sorted(str(digit) + combo[pi][pj]))
                        if new_c < combo[i][j]:
                            combo[i][j] = new_c

        n = len(num)
        first_zero = num.find('0')
        pref_a, pref_b, pref_c, pref_d = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
        for i in range(n):
            if num[i] == '0': break
            digit = int(num[i])
            pref_a[i+1] = pref_a[i] + (1 if digit in [2, 6] else 2 if digit == 4 else 3 if digit == 8 else 0)
            pref_b[i+1] = pref_b[i] + (1 if digit in [3, 6] else 2 if digit == 9 else 0)
            pref_c[i+1] = pref_c[i] + (1 if digit == 5 else 0)
            pref_d[i+1] = pref_d[i] + (1 if digit == 7 else 0)

        if first_zero == -1 and pref_a[n] >= a and pref_b[n] >= b and pref_c[n] >= c and pref_d[n] >= d:
            return num

        limit = first_zero if first_zero != -1 else n - 1
        for i in range(limit, -1, -1):
            start_d = int(num[i]) + 1 if i < first_zero or first_zero == -1 else 1
            for d_val in range(start_d, 10):
                ra, rb = max(0, a - pref_a[i]), max(0, b - pref_b[i])
                rc, rd = max(0, c - pref_c[i]), max(0, d - pref_d[i])
                da, db = factors.get(d_val, (0, 0))
                ra, rb = max(0, ra - da), max(0, rb - db)
                rc, rd = max(0, rc - (1 if d_val == 5 else 0)), max(0, rd - (1 if d_val == 7 else 0))
                if dp[ra][rb] + rc + rd <= n - 1 - i:
                    needed = combo[ra][rb] + "5" * rc + "7" * rd
                    ones = "1" * (n - 1 - i - len(needed))
                    return num[:i] + str(d_val) + ones + "".join(sorted(needed))

        L = max(n + 1, dp[a][b] + c + d)
        needed = combo[a][b] + "5" * c + "7" * d
        return "1" * (L - len(needed)) + "".join(sorted(needed))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

int dp[61][41];
char combo[61][41][61];
int digit_a[10] = {0, 0, 1, 0, 2, 0, 1, 0, 3, 0};
int digit_b[10] = {0, 0, 0, 1, 0, 0, 1, 0, 0, 2};
int digit_c[10] = {0, 0, 0, 0, 0, 1, 0, 0, 0, 0};
int digit_d[10] = {0, 0, 0, 0, 0, 0, 0, 1, 0, 0};

int compare_chars(const void* a, const void* b) {
    return (*(char*)a - *(char*)b);
}

char* smallestNumber(char* num, long long t) {
    long long temp_t = t;
    int a = 0, b = 0, c = 0, d = 0;
    int primes[] = {2, 3, 5, 7};
    for (int i = 0; i < 4; i++) {
        while (temp_t % primes[i] == 0) {
            if (i == 0) a++; else if (i == 1) b++; else if (i == 2) c++; else d++;
            temp_t /= primes[i];
        }
    }
    if (temp_t > 1) return "-1";

    for (int i = 0; i < 61; i++) {
        for (int j = 0; j < 41; j++) {
            dp[i][j] = 100;
            combo[i][j][0] = '\0';
        }
    }
    dp[0][0] = 0;
    for (int i = 0; i < 61; i++) {
        for (int j = 0; j < 41; j++) {
            if (i == 0 && j == 0) continue;
            int digits[] = {2, 3, 4, 6, 8, 9};
            for (int k = 0; k < 6; k++) {
                int cur_d = digits[k];
                int pi = i - digit_a[cur_d]; if (pi < 0) pi = 0;
                int pj = j - digit_b[cur_d]; if (pj < 0) pj = 0;
                if (dp[pi][pj] + 1 <= dp[i][j]) {
                    char next[61];
                    sprintf(next, "%d%s", cur_d, combo[pi][pj]);
                    qsort(next, strlen(next), 1, compare_chars);
                    if (dp[pi][pj] + 1 < dp[i][j] || strcmp(next, combo[i][j]) < 0) {
                        dp[i][j] = dp[pi][pj] + 1;
                        strcpy(combo[i][j], next);
                    }
                }
            }
        }
    }

    int n = strlen(num);
    char* first_z_ptr = strchr(num, '0');
    int first_zero = first_z_ptr ? (int)(first_z_ptr - num) : -1;
    int* pref_a = calloc(n + 1, sizeof(int));
    int* pref_b = calloc(n + 1, sizeof(int));
    int* pref_c = calloc(n + 1, sizeof(int));
    int* pref_d = calloc(n + 1, sizeof(int));
    for (int i = 0; i < n; i++) {
        if (num[i] == '0') break;
        int val = num[i] - '0';
        pref_a[i+1] = pref_a[i] + digit_a[val];
        pref_b[i+1] = pref_b[i] + digit_b[val];
        pref_c[i+1] = pref_c[i] + digit_c[val];
        pref_d[i+1] = pref_d[i] + digit_d[val];
    }

    if (first_zero == -1 && pref_a[n] >= a && pref_b[n] >= b && pref_c[n] >= c && pref_d[n] >= d) {
        free(pref_a); free(pref_b); free(pref_c); free(pref_d);
        return num;
    }

    int limit = (first_zero == -1) ? n - 1 : first_zero;
    for (int i = limit; i >= 0; i--) {
        int start_d = (first_zero == -1 || i < first_zero) ? (num[i] - '0' + 1) : 1;
        for (int dv = start_d; dv <= 9; dv++) {
            int ra = a - pref_a[i] - digit_a[dv]; if (ra < 0) ra = 0;
            int rb = b - pref_b[i] - digit_b[dv]; if (rb < 0) rb = 0;
            int rc = c - pref_c[i] - digit_c[dv]; if (rc < 0) rc = 0;
            int rd = d - pref_d[i] - digit_d[dv]; if (rd < 0) rd = 0;
            if (dp[ra][rb] + rc + rd <= n - 1 - i) {
                char* res = malloc(n + 10); memset(res, 0, n + 10);
                strncpy(res, num, i); res[i] = dv + '0';
                char suffix[200005]; int sidx = 0;
                for (int j = 0; j < rc; j++) suffix[sidx++] = '5';
                for (int j = 0; j < rd; j++) suffix[sidx++] = '7';
                strcpy(suffix + sidx, combo[ra][rb]); sidx += strlen(combo[ra][rb]);
                qsort(suffix, sidx, 1, compare_chars);
                int ones = n - 1 - i - sidx;
                for (int j = 0; j < ones; j++) res[i + 1 + j] = '1';
                strcpy(res + i + 1 + ones, suffix);
                free(pref_a); free(pref_b); free(pref_c); free(pref_d);
                return res;
            }
        }
    }

    int min_len = dp[a][b] + c + d;
    int L = (n + 1 > min_len) ? n + 1 : min_len;
    char* res = malloc(L + 10); memset(res, '1', L); res[L] = '\0';
    char suffix[200]; int sidx = 0;
    for (int j = 0; j < c; j++) suffix[sidx++] = '5';
    for (int j = 0; j < d; j++) suffix[sidx++] = '7';
    strcpy(suffix + sidx, combo[a][b]); sidx += strlen(combo[a][b]);
    qsort(suffix, sidx, 1, compare_chars);
    strcpy(res + L - sidx, suffix);
    free(pref_a); free(pref_b); free(pref_c); free(pref_d);
    return res;
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
using System.Text;

public class Solution {
    public string SmallestNumber(string num, long t) {
        long tempT = t;
        int a = 0, b = 0, c = 0, d = 0;
        long[] primes = { 2, 3, 5, 7 };
        for (int i = 0; i < 4; i++) {
            while (tempT % primes[i] == 0) {
                if (i == 0) a++; else if (i == 1) b++; else if (i == 2) c++; else d++;
                tempT /= primes[i];
            }
        }
        if (tempT > 1) return "-1";

        int[] digitA = { 0, 0, 1, 0, 2, 0, 1, 0, 3, 0 };
        int[] digitB = { 0, 0, 0, 1, 0, 0, 1, 0, 0, 2 };
        int[,] dp = new int[61, 41];
        string[,] combo = new string[61, 41];

        for (int i = 0; i < 61; i++) {
            for (int j = 0; j < 41; j++) {
                dp[i, j] = 100;
                combo[i, j] = "";
            }
        }
        dp[0, 0] = 0;
        for (int i = 0; i < 61; i++) {
            for (int j = 0; j < 41; j++) {
                if (i == 0 && j == 0) continue;
                int[] digits = { 2, 3, 4, 6, 8, 9 };
                foreach (int dv in digits) {
                    int pi = Math.Max(0, i - digitA[dv]);
                    int pj = Math.Max(0, j - digitB[dv]);
                    if (dp[pi, pj] + 1 <= dp[i, j]) {
                        char[] nextArr = (dv.ToString() + combo[pi, pj]).ToCharArray();
                        Array.Sort(nextArr);
                        string next = new string(nextArr);
                        if (dp[pi, pj] + 1 < dp[i, j] || string.Compare(next, combo[i, j]) < 0) {
                            dp[i, j] = dp[pi, pj] + 1;
                            combo[i, j] = next;
                        }
                    }
                }
            }
        }

        int n = num.Length;
        int firstZero = num.IndexOf('0');
        int[] prefA = new int[n + 1], prefB = new int[n + 1], prefC = new int[n + 1], prefD = new int[n + 1];
        for (int i = 0; i < n; i++) {
            if (num[i] == '0') break;
            int v = num[i] - '0';
            prefA[i + 1] = prefA[i] + digitA[v];
            prefB[i + 1] = prefB[i] + digitB[v];
            prefC[i + 1] = prefC[i] + (v == 5 ? 1 : 0);
            prefD[i + 1] = prefD[i] + (v == 7 ? 1 : 0);
        }

        if (firstZero == -1 && prefA[n] >= a && prefB[n] >= b && prefC[n] >= c && prefD[n] >= d) return num;

        int limit = firstZero == -1 ? n - 1 : firstZero;
        for (int i = limit; i >= 0; i--) {
            int startD = (firstZero == -1 || i < firstZero) ? (num[i] - '0' + 1) : 1;
            for (int dv = startD; dv <= 9; dv++) {
                int ra = Math.Max(0, a - prefA[i] - digitA[dv]);
                int rb = Math.Max(0, b - prefB[i] - digitB[dv]);
                int rc = Math.Max(0, c - prefC[i] - (dv == 5 ? 1 : 0));
                int rd = Math.Max(0, d - prefD[i] - (dv == 7 ? 1 : 0));
                if (dp[ra, rb] + rc + rd <= n - 1 - i) {
                    char[] suffixArr = (combo[ra, rb] + new string('5', rc) + new string('7', rd)).ToCharArray();
                    Array.Sort(suffixArr);
                    string ones = new string('1', n - 1 - i - suffixArr.Length);
                    return num.Substring(0, i) + dv + ones + new string(suffixArr);
                }
            }
        }

        int L = Math.Max(n + 1, dp[a, b] + c + d);
        char[] resArr = (combo[a, b] + new string('5', c) + new string('7', d)).ToCharArray();
        Array.Sort(resArr);
        return new string('1', L - resArr.Length) + new string(resArr);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} num
 * @param {number} t
 * @return {string}
 */
var smallestNumber = function(num, t) {
    let bigT = BigInt(t);
    let a = 0, b = 0, c = 0, d = 0;
    let primes = [2n, 3n, 5n, 7n];
    for (let i = 0; i < 4; i++) {
        while (bigT % primes[i] === 0n) {
            if (i === 0) a++; else if (i === 1) b++; else if (i === 2) c++; else d++;
            bigT /= primes[i];
        }
    }
    if (bigT > 1n) return "-1";

    const digitA = [0, 0, 1, 0, 2, 0, 1, 0, 3, 0];
    const digitB = [0, 0, 0, 1, 0, 0, 1, 0, 0, 2];
    let dp = Array.from({ length: 61 }, () => Array(41).fill(100));
    let combo = Array.from({ length: 61 }, () => Array(41).fill(""));

    dp[0][0] = 0;
    for (let i = 0; i < 61; i++) {
        for (let j = 0; j < 41; j++) {
            if (i === 0 && j === 0) continue;
            let digits = [2, 3, 4, 6, 8, 9];
            for (let dv of digits) {
                let pi = Math.max(0, i - digitA[dv]);
                let pj = Math.max(0, j - digitB[dv]);
                if (dp[pi][pj] + 1 <= dp[i][j]) {
                    let next = (dv.toString() + combo[pi][pj]).split('').sort().join('');
                    if (dp[pi][pj] + 1 < dp[i][j] || next < combo[i][j]) {
                        dp[i][j] = dp[pi][pj] + 1;
                        combo[i][j] = next;
                    }
                }
            }
        }
    }

    const n = num.length;
    let firstZero = num.indexOf('0');
    let prefA = Array(n + 1).fill(0), prefB = Array(n + 1).fill(0), prefC = Array(n + 1).fill(0), prefD = Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        if (num[i] === '0') break;
        let v = parseInt(num[i]);
        prefA[i + 1] = prefA[i] + digitA[v];
        prefB[i + 1] = prefB[i] + digitB[v];
        prefC[i + 1] = prefC[i] + (v === 5 ? 1 : 0);
        prefD[i + 1] = prefD[i] + (v === 7 ? 1 : 0);
    }

    if (firstZero === -1 && prefA[n] >= a && prefB[n] >= b && prefC[n] >= c && prefD[n] >= d) return num;

    let limit = firstZero === -1 ? n - 1 : firstZero;
    for (let i = limit; i >= 0; i--) {
        let startD = (firstZero === -1 || i < firstZero) ? parseInt(num[i]) + 1 : 1;
        for (let dv = startD; dv <= 9; dv++) {
            let ra = Math.max(0, a - prefA[i] - digitA[dv]);
            let rb = Math.max(0, b - prefB[i] - digitB[dv]);
            let rc = Math.max(0, c - prefC[i] - (dv === 5 ? 1 : 0));
            let rd = Math.max(0, d - prefD[i] - (dv === 7 ? 1 : 0));
            if (dp[ra][rb] + rc + rd <= n - 1 - i) {
                let suffix = (combo[ra][rb] + "5".repeat(rc) + "7".repeat(rd)).split('').sort().join('');
                let ones = "1".repeat(n - 1 - i - suffix.length);
                return num.substring(0, i) + dv + ones + suffix;
            }
        }
    }

    let L = Math.max(n + 1, dp[a][b] + c + d);
    let suffix = (combo[a][b] + "5".repeat(c) + "7".repeat(d)).split('').sort().join('');
    return "1".repeat(L - suffix.length) + suffix;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
// Generation failed for TypeScript
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
// Generation failed for PHP
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
// Generation failed for Swift
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
// Generation failed for Kotlin
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:math';

class Solution {
  static final List<int> count2 = [0, 0, 1, 0, 2, 0, 1, 0, 3, 0];
  static final List<int> count3 = [0, 0, 0, 1, 0, 0, 1, 0, 0, 2];
  static final List<int> count5 = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0];
  static final List<int> count7 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0];
  static List<List<int>>? _dp;

  void _precompute() {
    if (_dp != null) return;
    _dp = List.generate(65, (_) => List.filled(65, 1000));
    _dp![0][0] = 0;
    for (int a = 0; a <= 60; a++) {
      for (int b = 0; b <= 60; b++) {
        if (a == 0 && b == 0) continue;
        int best = 1000;
        List<List<int>> choices = [
          [1, 0], [0, 1], [2, 0], [1, 1], [3, 0], [0, 2]
        ];
        for (var pair in choices) {
          int ad = pair[0], bd = pair[1];
          int na = max(0, a - ad);
          int nb = max(0, b - bd);
          if (na < a || nb < b) {
            best = min(best, 1 + _dp![na][nb]);
          }
        }
        _dp![a][b] = best;
      }
    }
  }

  String smallestNumber(String num, int t) {
    _precompute();
    int a0 = 0, b0 = 0, c0 = 0, d0 = 0;
    int tempT = t;
    while (tempT % 2 == 0) { tempT ~/= 2; a0++; }
    while (tempT % 3 == 0) { tempT ~/= 3; b0++; }
    while (tempT % 5 == 0) { tempT ~/= 5; c0++; }
    while (tempT % 7 == 0) { tempT ~/= 7; d0++; }
    if (tempT > 1) return "-1";

    int n = num.length;
    List<int> p2 = List.filled(n + 1, 0);
    List<int> p3 = List.filled(n + 1, 0);
    List<int> p5 = List.filled(n + 1, 0);
    List<int> p7 = List.filled(n + 1, 0);
    int firstZero = n;
    for (int i = 0; i < n; i++) {
      int d = num.codeUnitAt(i) - 48;
      if (d == 0) {
        firstZero = i;
        break;
      }
      p2[i + 1] = p2[i] + count2[d];
      p3[i + 1] = p3[i] + count3[d];
      p5[i + 1] = p5[i] + count5[d];
      p7[i + 1] = p7[i] + count7[d];
    }

    if (firstZero == n && p2[n] >= a0 && p3[n] >= b0 && p5[n] >= c0 && p7[n] >= d0) {
      return num;
    }

    for (int L = min(n - 1, firstZero); L >= 0; L--) {
      int curA0 = a0 - p2[L], curB0 = b0 - p3[L], curC0 = c0 - p5[L], curD0 = d0 - p7[L];
      for (int d = (num.codeUnitAt(L) - 48) + 1; d <= 9; d++) {
        int ra = max(0, curA0 - count2[d]);
        int rb = max(0, curB0 - count3[d]);
        int rc = max(0, curC0 - count5[d]);
        int rd = max(0, curD0 - count7[d]);
        if (rc + rd + _dp![ra][rb] <= n - 1 - L) {
          String res = num.substring(0, L) + d.toString();
          int remA = ra, remB = rb, remC = rc, remD = rd;
          for (int i = L + 1; i < n; i++) {
            for (int v = 1; v <= 9; v++) {
              int na = max(0, remA - count2[v]);
              int nb = max(0, remB - count3[v]);
              int nc = max(0, remC - count5[v]);
              int nd = max(0, remD - count7[v]);
              if (nc + nd + _dp![na][nb] <= n - 1 - i) {
                res += v.toString();
                remA = na; remB = nb; remC = nc; remD = nd;
                break;
              }
            }
          }
          return res;
        }
      }
    }

    int kLen = max(n + 1, c0 + d0 + _dp![a0][b0]);
    String res = "";
    int remA = a0, remB = b0, remC = c0, remD = d0;
    for (int i = 0; i < kLen; i++) {
      for (int v = 1; v <= 9; v++) {
        int na = max(0, remA - count2[v]);
        int nb = max(0, remB - count3[v]);
        int nc = max(0, remC - count5[v]);
        int nd = max(0, remD - count7[v]);
        if (nc + nd + _dp![na][nb] <= kLen - 1 - i) {
          res += v.toString();
          remA = na; remB = nb; remC = nc; remD = nd;
          break;
        }
      }
    }
    return res;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func smallestNumber(num string, t int64) string {
	count2 := []int{0, 0, 1, 0, 2, 0, 1, 0, 3, 0}
	count3 := []int{0, 0, 0, 1, 0, 0, 1, 0, 0, 2}
	count5 := []int{0, 0, 0, 0, 0, 1, 0, 0, 0, 0}
	count7 := []int{0, 0, 0, 0, 0, 0, 0, 1, 0, 0}

	dp := [65][65]int{}
	for i := 0; i < 65; i++ {
		for j := 0; j < 65; j++ {
			dp[i][j] = 1000
		}
	}
	dp[0][0] = 0
	for a := 0; a <= 60; a++ {
		for b := 0; b <= 60; b++ {
			if a == 0 && b == 0 {
				continue
			}
			choices := [][]int{{1, 0}, {0, 1}, {2, 0}, {1, 1}, {3, 0}, {0, 2}}
			for _, pair := range choices {
				na, nb := a-pair[0], b-pair[1]
				if na < 0 { na = 0 }
				if nb < 0 { nb = 0 }
				if na < a || nb < b {
					if 1+dp[na][nb] < dp[a][b] {
						dp[a][b] = 1 + dp[na][nb]
					}
				}
			}
		}
	}

	a0, b0, c0, d0 := 0, 0, 0, 0
	tempT := t
	for tempT%2 == 0 { tempT /= 2; a0++ }
	for tempT%3 == 0 { tempT /= 3; b0++ }
	for tempT%5 == 0 { tempT /= 5; c0++ }
	for tempT%7 == 0 { tempT /= 7; d0++ }
	if tempT > 1 { return "-1" }

	n := len(num)
	p2, p3, p5, p7 := make([]int, n+1), make([]int, n+1), make([]int, n+1), make([]int, n+1)
	firstZero := n
	for i := 0; i < n; i++ {
		d := int(num[i] - '0')
		if d == 0 {
			firstZero = i
			break
		}
		p2[i+1] = p2[i] + count2[d]
		p3[i+1] = p3[i] + count3[d]
		p5[i+1] = p5[i] + count5[d]
		p7[i+1] = p7[i] + count7[d]
	}

	if firstZero == n && p2[n] >= a0 && p3[n] >= b0 && p5[n] >= c0 && p7[n] >= d0 {
		return num
	}

	for L := firstZero; L >= 0; L-- {
		if L == n { continue }
		curA0, curB0, curC0, curD0 := a0-p2[L], b0-p3[L], c0-p5[L], d0-p7[L]
		for d := int(num[L]-'0') + 1; d <= 9; d++ {
			ra, rb, rc, rd := curA0-count2[d], curB0-count3[d], curC0-count5[d], curD0-count7[d]
			if ra < 0 { ra = 0 }
			if rb < 0 { rb = 0 }
			if rc < 0 { rc = 0 }
			if rd < 0 { rd = 0 }
			if rc+rd+dp[ra][rb] <= n-1-L {
				ans := num[:L] + string(byte(d+'0'))
				remA, remB, remC, remD := ra, rb, rc, rd
				for i := L + 1; i < n; i++ {
					for v := 1; v <= 9; v++ {
						na, nb, nc, nd := remA-count2[v], remB-count3[v], remC-count5[v], remD-count7[v]
						if na < 0 { na = 0 }
						if nb < 0 { nb = 0 }
						if nc < 0 { nc = 0 }
						if nd < 0 { nd = 0 }
						if nc+nd+dp[na][nb] <= n-1-i {
							ans += string(byte(v + '0'))
							remA, remB, remC, remD = na, nb, nc, nd
							break
						}
					}
				}
				return ans
			}
		}
	}

	kLen := n + 1
	if c0+d0+dp[a0][b0] > kLen {
		kLen = c0 + d0 + dp[a0][b0]
	}
	ans := ""
	remA, remB, remC, remD := a0, b0, c0, d0
	for i := 0; i < kLen; i++ {
		for v := 1; v <= 9; v++ {
			na, nb, nc, nd := remA-count2[v], remB-count3[v], remC-count5[v], remD-count7[v]
			if na < 0 { na = 0 }
			if nb < 0 { nb = 0 }
			if nc < 0 { nc = 0 }
			if nd < 0 { nd = 0 }
			if nc+nd+dp[na][nb] <= kLen-1-i {
				ans += string(byte(v + '0'))
				remA, remB, remC, remD = na, nb, nc, nd
				break
			}
		}
	}
	return ans
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def smallest_number(num, t)
  count2 = [0, 0, 1, 0, 2, 0, 1, 0, 3, 0]
  count3 = [0, 0, 0, 1, 0, 0, 1, 0, 0, 2]
  count5 = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
  count7 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]

  dp = Array.new(65) { Array.new(65, 1000) }
  dp[0][0] = 0
  (0..60).each do |a|
    (0..60).each do |b|
      next if a == 0 && b == 0
      choices = [[1, 0], [0, 1], [2, 0], [1, 1], [3, 0], [0, 2]]
      choices.each do |ad, bd|
        na = [0, a - ad].max
        nb = [0, b - bd].max
        dp[a][b] = [dp[a][b], 1 + dp[na][nb]].min if na < a || nb < b
      end
    end
  end

  a0, b0, c0, d0 = 0, 0, 0, 0
  temp_t = t
  while temp_t % 2 == 0; temp_t /= 2; a0 += 1; end
  while temp_t % 3 == 0; temp_t /= 3; b0 += 1; end
  while temp_t % 5 == 0; temp_t /= 5; c0 += 1; end
  while temp_t % 7 == 0; temp_t /= 7; d0 += 1; end
  return "-1" if temp_t > 1

  n = num.length
  p2 = Array.new(n + 1, 0)
  p3 = Array.new(n + 1, 0)
  p5 = Array.new(n + 1, 0)
  p7 = Array.new(n + 1, 0)
  first_zero = n
  n.times do |i|
    d = num[i].to_i
    if d == 0
      first_zero = i
      break
    end
    p2[i+1] = p2[i] + count2[d]
    p3[i+1] = p3[i] + count3[d]
    p5[i+1] = p5[i] + count5[d]
    p7[i+1] = p7[i] + count7[d]
  end

  if first_zero == n && p2[n] >= a0 && p3[n] >= b0 && p5[n] >= c0 && p7[n] >= d0
    return num
  end

  [n - 1, first_zero].min.downto(0) do |l|
    cur_a0, cur_b0, cur_c0, cur_d0 = a0 - p2[l], b0 - p3[l], c0 - p5[l], d0 - p7[l]
    (num[l].to_i + 1..9).each do |d|
      ra, rb, rc, rd = [0, cur_a0 - count2[d]].max, [0, cur_b0 - count3[d]].max, [0, cur_c0 - count5[d]].max, [0, cur_d0 - count7[d]].max
      if rc + rd + dp[ra][rb] <= n - 1 - l
        ans = num[0...l] + d.to_s
        rem_a, rem_b, rem_c, rem_d = ra, rb, rc, rd
        (l + 1...n).each do |i|
          (1..9).each do |v|
            na, nb, nc, nd = [0, rem_a - count2[v]].max, [0, rem_b - count3[v]].max, [0, rem_c - count5[v]].max, [0, rem_d - count7[v]].max
            if nc + nd + dp[na][nb] <= n - 1 - i
              ans += v.to_s
              rem_a, rem_b, rem_c, rem_d = na, nb, nc, nd
              break
            end
          end
        end
        return ans
      end
    end
  end

  k_len = [n + 1, c0 + d0 + dp[a0][b0]].max
  ans = ""
  rem_a, rem_b, rem_c, rem_d = a0, b0, c0, d0
  k_len.times do |i|
    (1..9).each do |v|
      na, nb, nc, nd = [0, rem_a - count2[v]].max, [0, rem_b - count3[v]].max, [0, rem_c - count5[v]].max, [0, rem_d - count7[v]].max
      if nc + nd + dp[na][nb] <= k_len - 1 - i
        ans += v.to_s
        rem_a, rem_b, rem_c, rem_d = na, nb, nc, nd
        break
      end
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
    def smallestNumber(num: String, t: Long): String = {
        val count2 = Array(0, 0, 1, 0, 2, 0, 1, 0, 3, 0)
        val count3 = Array(0, 0, 0, 1, 0, 0, 1, 0, 0, 2)
        val count5 = Array(0, 0, 0, 0, 0, 1, 0, 0, 0, 0)
        val count7 = Array(0, 0, 0, 0, 0, 0, 0, 1, 0, 0)

        val dp = Array.fill(65, 65)(1000)
        dp(0)(0) = 0
        for (a <- 0 to 60; b <- 0 to 60 if !(a == 0 && b == 0)) {
            val choices = List((1, 0), (0, 1), (2, 0), (1, 1), (3, 0), (0, 2))
            for ((ad, bd) <- choices) {
                val na = Math.max(0, a - ad)
                val nb = Math.max(0, b - bd)
                if (na < a || nb < b) {
                    dp(a)(b) = Math.min(dp(a)(b), 1 + dp(na)(nb))
                }
            }
        }

        var a0 = 0; var b0 = 0; var c0 = 0; var d0 = 0
        var tempT = t
        while (tempT % 2 == 0) { tempT /= 2; a0 += 1 }
        while (tempT % 3 == 0) { tempT /= 3; b0 += 1 }
        while (tempT % 5 == 0) { tempT /= 5; c0 += 1 }
        while (tempT % 7 == 0) { tempT /= 7; d0 += 1 }
        if (tempT > 1) return "-1"

        val n = num.length
        val p2 = new Array[Int](n + 1)
        val p3 = new Array[Int](n + 1)
        val p5 = new Array[Int](n + 1)
        val p7 = new Array[Int](n + 1)
        var firstZero = n
        var i = 0
        while (i < n) {
            val d = num(i) - '0'
            if (d == 0) { firstZero = i; i = n }
            else {
                p2(i + 1) = p2(i) + count2(d)
                p3(i + 1) = p3(i) + count3(d)
                p5(i + 1) = p5(i) + count5(d)
                p7(i + 1) = p7(i) + count7(d)
                i += 1
            }
        }

        if (firstZero == n && p2(n) >= a0 && p3(n) >= b0 && p5(n) >= c0 && p7(n) >= d0) {
            return num
        }

        for (L <- Math.min(n - 1, firstZero) to 0 by -1) {
            val curA0 = a0 - p2(L); val curB0 = b0 - p3(L)
            val curC0 = c0 - p5(L); val curD0 = d0 - p7(L)
            for (d <- (num(L) - '0' + 1) to 9) {
                val ra = Math.max(0, curA0 - count2(d))
                val rb = Math.max(0, curB0 - count3(d))
                val rc = Math.max(0, curC0 - count5(d))
                val rd = Math.max(0, curD0 - count7(d))
                if (rc + rd + dp(ra)(rb) <= n - 1 - L) {
                    val res = new StringBuilder(num.substring(0, L))
                    res.append(d.toString)
                    var remA = ra; var remB = rb; var remC = rc; var remD = rd
                    for (j <- L + 1 until n) {
                        var found = false
                        for (v <- 1 to 9 if !found) {
                            val na = Math.max(0, remA - count2(v))
                            val nb = Math.max(0, remB - count3(v))
                            val nc = Math.max(0, remC - count5(v))
                            val nd = Math.max(0, remD - count7(v))
                            if (nc + nd + dp(na)(nb) <= n - 1 - j) {
                                res.append(v.toString)
                                remA = na; remB = nb; remC = nc; remD = nd
                                found = true
                            }
                        }
                    }
                    return res.toString()
                }
            }
        }

        val kLen = Math.max(n + 1, c0 + d0 + dp(a0)(b0))
        val res = new StringBuilder
        var remA = a0; var remB = b0; var remC = c0; var remD = d0
        for (i <- 0 until kLen) {
            var found = false
            for (v <- 1 to 9 if !found) {
                val na = Math.max(0, remA - count2(v))
                val nb = Math.max(0, remB - count3(v))
                val nc = Math.max(0, remC - count5(v))
                val nd = Math.max(0, remD - count7(v))
                if (nc + nd + dp(na)(nb) <= kLen - 1 - i) {
                    res.append(v.toString)
                    remA = na; remB = nb; remC = nc; remD = nd
                    found = true
                }
            }
        }
        res.toString()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn smallest_number(num: String, t: i64) -> String {
        let mut temp_t = t;
        let (mut a, mut b, mut c, mut d) = (0, 0, 0, 0);
        while temp_t % 2 == 0 { temp_t /= 2; a += 1; }
        while temp_t % 3 == 0 { temp_t /= 3; b += 1; }
        while temp_t % 5 == 0 { temp_t /= 5; c += 1; }
        while temp_t % 7 == 0 { temp_t /= 7; d += 1; }
        if temp_t > 1 { return "-1".to_string(); }

        let mut dp = vec![vec![String::new(); 31]; 48];
        for i in 0..48 {
            for j in 0..31 {
                if i == 0 && j == 0 { continue; }
                let mut best: Option<String> = None;
                for &(digit, da, db) in &[(2, 1, 0), (3, 0, 1), (4, 2, 0), (6, 1, 1), (8, 3, 0), (9, 0, 2)] {
                    let pi = if i >= da { i - da } else { 0 };
                    let pj = if j >= db { j - db } else { 0 };
                    let mut s = dp[pi][pj].clone();
                    s.push(std::char::from_digit(digit as u32, 10).unwrap());
                    let mut sc: Vec<char> = s.chars().collect();
                    sc.sort();
                    let ss: String = sc.into_iter().collect();
                    if best.is_none() || ss.len() < best.as_ref().unwrap().len() || (ss.len() == best.as_ref().unwrap().len() && ss < *best.as_ref().unwrap()) {
                        best = Some(ss);
                    }
                }
                dp[i][j] = best.unwrap();
            }
        }

        let n = num.len();
        let chars: Vec<char> = num.chars().collect();
        let mut first_zero = n;
        for (i, &ch) in chars.iter().enumerate() {
            if ch == '0' { first_zero = i; break; }
        }

        if first_zero == n {
            let (mut ra, mut rb, mut rc, mut rd) = (a, b, c, d);
            for &ch in &chars {
                let (da, db, dc, dd) = Self::get_factors(ch.to_digit(10).unwrap());
                ra = ra.saturating_sub(da); rb = rb.saturating_sub(db); rc = rc.saturating_sub(dc); rd = rd.saturating_sub(dd);
            }
            if ra == 0 && rb == 0 && rc == 0 && rd == 0 { return num; }
        }

        for i in (0..=first_zero.min(n - 1)).rev() {
            let mut ra = a; let mut rb = b; let mut rc = c; let mut rd = d;
            let mut possible = true;
            for j in 0..i {
                if chars[j] == '0' { possible = false; break; }
                let (da, db, dc, dd) = Self::get_factors(chars[j].to_digit(10).unwrap());
                ra = ra.saturating_sub(da); rb = rb.saturating_sub(db); rc = rc.saturating_sub(dc); rd = rd.saturating_sub(dd);
            }
            if !possible { continue; }
            let start_v = if chars[i] == '0' { 1 } else { chars[i].to_digit(10).unwrap() + 1 };
            for v in start_v..10 {
                let (da, db, dc, dd) = Self::get_factors(v);
                let nra = ra.saturating_sub(da); let nrb = rb.saturating_sub(db); let nrc = rc.saturating_sub(dc); let nrd = rd.saturating_sub(dd);
                let needed_str = &dp[nra as usize][nrb as usize];
                let total_needed = nrc as usize + nrd as usize + needed_str.len();
                if total_needed <= n - 1 - i {
                    let mut res = chars[..i].iter().collect::<String>();
                    res.push(std::char::from_digit(v, 10).unwrap());
                    let mut counts = [0; 10];
                    counts[1] = (n - 1 - i - total_needed) as i32;
                    counts[5] = nrc as i32; counts[7] = nrd as i32;
                    for ch in needed_str.chars() { counts[ch.to_digit(10).unwrap() as usize] += 1; }
                    for digit in 1..10 { for _ in 0..counts[digit] { res.push(std::char::from_digit(digit as u32, 10).unwrap()); } }
                    return res;
                }
            }
        }

        let min_needed_len = (c + d) as usize + dp[a as usize][b as usize].len();
        let target_len = n.max(min_needed_len) + 1;
        let L = if min_needed_len > n { min_needed_len } else { target_len };
        let mut res = String::new();
        let mut counts = [0; 10];
        counts[1] = (L - min_needed_len) as i32; counts[5] = c as i32; counts[7] = d as i32;
        for ch in dp[a as usize][b as usize].chars() { counts[ch.to_digit(10).unwrap() as usize] += 1; }
        for digit in 1..10 { for _ in 0..counts[digit] { res.push(std::char::from_digit(digit as u32, 10).unwrap()); } }
        res
    }

    fn get_factors(v: u32) -> (i64, i64, i64, i64) {
        match v {
            2 => (1, 0, 0, 0), 3 => (0, 1, 0, 0), 4 => (2, 0, 0, 0), 5 => (0, 0, 1, 0),
            6 => (1, 1, 0, 0), 7 => (0, 0, 0, 1), 8 => (3, 0, 0, 0), 9 => (0, 2, 0, 0),
            _ => (0, 0, 0, 0),
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (smallest-number num t)
  (-> string? exact-integer? string?)
  (define (get-factors v)
    (cond
      [(= v 2) '(1 0 0 0)] [(= v 3) '(0 1 0 0)] [(= v 4) '(2 0 0 0)] [(= v 5) '(0 0 1 0)]
      [(= v 6) '(1 1 0 0)] [(= v 7) '(0 0 0 1)] [(= v 8) '(3 0 0 0)] [(= v 9) '(0 2 0 0)]
      [else '(0 0 0 0)]))
  (let* ([a 0] [b 0] [c 0] [d 0] [temp-t t])
    (let-values ([(a temp-t) (let loop ([ca 0] [ct temp-t]) (if (and (> ct 0) (= 0 (remainder ct 2))) (loop (+ ca 1) (/ ct 2)) (values ca ct)))]
                 [(b temp-t) (let loop ([cb 0] [ct temp-t]) (if (and (> ct 0) (= 0 (remainder ct 3))) (loop (+ cb 1) (/ ct 3)) (values cb ct)))]
                 [(c temp-t) (let loop ([cc 0] [ct temp-t]) (if (and (> ct 0) (= 0 (remainder ct 5))) (loop (+ cc 1) (/ ct 5)) (values cc ct)))]
                 [(d temp-t) (let loop ([cd 0] [ct temp-t]) (if (and (> ct 0) (= 0 (remainder ct 7))) (loop (+ cd 1) (/ ct 7)) (values cd ct)))])
      (if (> temp-t 1) "-1"
          (let ([dp (make-vector 48)])
            (for ([i 48]) (vector-set! dp i (make-vector 31 "")))
            (for* ([i 48] [j 31])
              (when (not (and (= i 0) (= j 0)))
                (let ([best #f])
                  (for ([digit '(2 3 4 6 8 9)])
                    (let* ([f (get-factors digit)]
                           [pi (max 0 (- i (car f)))] [pj (max 0 (- j (cadr f)))]
                           [s (string-append (vector-ref (vector-ref dp pi) pj) (number->string digit))]
                           [ss (list->string (sort (string->list s) char<?))])
                      (when (or (not best) (< (string-length ss) (string-length best)) (and (= (string-length ss) (string-length best)) (string<? ss best)))
                        (set! best ss))))
                  (vector-set! (vector-ref dp i) j best))))
            (let* ([n (string-length num)] [chars (string->list num)]
                   [first-zero (or (for/first ([i n] #:when (char=? (list-ref chars i) #\0)) i) n)])
              (define (check-orig)
                (if (= first-zero n)
                    (let ([ra a] [rb b] [rc c] [rd d])
                      (for ([ch chars])
                        (let ([f (get-factors (- (char->integer ch) 48))])
                          (set! ra (max 0 (- ra (car f)))) (set! rb (max 0 (- rb (cadr f))))
                          (set! rc (max 0 (- rc (caddr f)))) (set! rd (max 0 (- rd (cadddr f))))))
                      (and (= ra 0) (= rb 0) (= rc 0) (= rd 0)))
                    #f))
              (if (check-orig) num
                  (let ([ans #f])
                    (for ([i (in-range (min (- n 1) first-zero) -1 -1)] #:break ans)
                      (let ([ra a] [rb b] [rc c] [rd d])
                        (for ([j i])
                          (let ([f (get-factors (- (char->integer (list-ref chars j)) 48))])
                            (set! ra (max 0 (- ra (car f)))) (set! rb (max 0 (- rb (cadr f))))
                            (set! rc (max 0 (- rc (caddr f)))) (set! rd (max 0 (- rd (cadddr f))))))
                        (let ([start-v (if (char=? (list-ref chars i) #\0) 1 (+ 1 (- (char->integer (list-ref chars i)) 48)))])
                          (for ([v (in-range start-v 10)] #:break ans)
                            (let* ([f (get-factors v)]
                                   [nra (max 0 (- ra (car f)))] [nrb (max 0 (- rb (cadr f)))]
                                   [nrc (max 0 (- rc (caddr f)))] [nrd (max 0 (- rd (cadddr f)))]
                                   [needed-str (vector-ref (vector-ref dp nra) nrb)]
                                   [total-needed (+ nrc nrd (string-length needed-str))])
                              (when (<= total-needed (- n 1 i))
                                (let ([res (substring num 0 i)] [counts (make-vector 10 0)])
                                  (vector-set! counts 1 (- n 1 i total-needed))
                                  (vector-set! counts 5 nrc) (vector-set! counts 7 nrd)
                                  (for ([ch (string->list needed-str)]) (let ([d (- (char->integer ch) 48)]) (vector-set! counts d (+ 1 (vector-ref counts d)))))
                                  (let ([suffix (apply string-append (for/list ([d (in-range 1 10)]) (make-string (vector-ref counts d) (integer->char (+ d 48)))))]
                                        [vs (number->string v)])
                                    (set! ans (string-append res vs suffix))))))))))
                    (if ans ans
                        (let* ([min-len (+ c d (string-length (vector-ref (vector-ref dp a) b)))]
                               [L (max (+ n 1) min-len)] [counts (make-vector 10 0)]
                               [needed-str (vector-ref (vector-ref dp a) b)])
                          (vector-set! counts 1 (- L min-len)) (vector-set! counts 5 c) (vector-set! counts 7 d)
                          (for ([ch (string->list needed-str)]) (let ([d (- (char->integer ch) 48)]) (vector-set! counts d (+ 1 (vector-ref counts d)))))
                          (apply string-append (for/list ([d (in-range 1 10)]) (make-string (vector-ref counts d) (integer->char (+ d 48)))))))))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec smallest_number(Num :: unicode:unicode_binary(), T :: integer()) -> unicode:unicode_binary().
smallest_number(Num, T) ->
    {A, B, C, D, TempT} = get_t_factors(T),
    if TempT > 1 -> <<"-1">>;
       true ->
           DP = build_dp(),
           Chars = binary_to_list(Num),
           N = length(Chars),
           FirstZero = find_first_zero(Chars, 0, N),
           Check = case FirstZero of
                       N -> check_orig(Chars, A, B, C, D);
                       _ -> false
                   end,
           if Check -> Num;
              true -> solve(Num, Chars, N, FirstZero, A, B, C, D, DP)
           end
    end.

get_t_factors(T) ->
    {A, T1} = count_factors(T, 2, 0),
    {B, T2} = count_factors(T1, 3, 0),
    {C, T3} = count_factors(T2, 5, 0),
    {D, T4} = count_factors(T3, 7, 0),
    {A, B, C, D, T4}.

count_factors(T, P, Count) when T > 0, T rem P == 0 -> count_factors(T div P, P, Count + 1);
count_factors(T, _, Count) -> {Count, T}.

find_first_zero([], _, N) -> N;
find_first_zero([$0|_], I, _) -> I;
find_first_zero([_|T], I, N) -> find_first_zero(T, I + 1, N).

get_digit_factors($1) -> {0, 0, 0, 0}; get_digit_factors($2) -> {1, 0, 0, 0};
get_digit_factors($3) -> {0, 1, 0, 0}; get_digit_factors($4) -> {2, 0, 0, 0};
get_digit_factors($5) -> {0, 0, 1, 0}; get_digit_factors($6) -> {1, 1, 0, 0};
get_digit_factors($7) -> {0, 0, 0, 1}; get_digit_factors($8) -> {3, 0, 0, 0};
get_digit_factors($9) -> {0, 2, 0, 0}; get_digit_factors(V) when is_integer(V) -> get_digit_factors(V + $0).

check_orig([], A, B, C, D) -> A =< 0 andalso B =< 0 andalso C =< 0 andalso D =< 0;
check_orig([H|T], A, B, C, D) ->
    {DA, DB, DC, DD} = get_digit_factors(H),
    check_orig(T, A - DA, B - DB, C - DC, D - DD).

build_dp() ->
    DP = maps:new(),
    DP0 = DP#{{0,0} => ""},
    Digits = [{2,1,0}, {3,0,1}, {4,2,0}, {6,1,1}, {8,3,0}, {9,0,2}],
    lists:foldl(fun(I, AccI) ->
        lists:foldl(fun(J, AccJ) ->
            if I == 0, J == 0 -> AccJ;
               true ->
                   Best = lists:foldl(fun({Digit, DA, DB}, CurrentBest) ->
                       PI = max(0, I - DA), PJ = max(0, J - DB),
                       S = lists:sort([Digit + $0 | maps:get({PI, PJ}, AccJ)]),
                       if CurrentBest == undefined -> S;
                          length(S) < length(CurrentBest) -> S;
                          length(S) == length(CurrentBest), S < CurrentBest -> S;
                          true -> CurrentBest
                       end
                   end, undefined, Digits),
                   AccJ#{{I, J} => Best}
            end
        end, AccI, lists:seq(0, 30))
    end, DP0, lists:seq(0, 47)).

solve(Num, Chars, N, FirstZero, A, B, C, D, DP) ->
    case find_same_length(Num, Chars, N, min(N - 1, FirstZero), A, B, C, D, DP) of
        {ok, Res} -> Res;
        none ->
            NeededStr = maps:get({A, B}, DP),
            MinLen = C + D + length(NeededStr),
            L = if MinLen > N -> MinLen; true -> N + 1 end,
            Counts = count_sort_suffix(L - MinLen, C, D, NeededStr),
            list_to_binary(build_from_counts(Counts))
    end.

find_same_length(_, _, _, -1, _, _, _, _, _) -> none;
find_same_length(Num, Chars, N, I, A, B, C, D, DP) ->
    Prefix = lists:sublist(Chars, I),
    {PA, PB, PC, PD} = prefix_factors(Prefix, 0, 0, 0, 0),
    RA = max(0, A - PA), RB = max(0, B - PB), RC = max(0, C - PC), RD = max(0, D - PD),
    StartV = if lists:nth(I + 1, Chars) == $0 -> 1; true -> lists:nth(I + 1, Chars) - $0 + 1 end,
    case try_v(I, N, StartV, RA, RB, RC, RD, DP) of
        {ok, Suffix} -> {ok, list_to_binary(lists:sublist(Chars, I) ++ Suffix)};
        none -> find_same_length(Num, Chars, N, I - 1, A, B, C, D, DP)
    end.

try_v(_, _, 10, _, _, _, _, _) -> none;
try_v(I, N, V, RA, RB, RC, RD, DP) ->
    {DA, DB, DC, DD} = get_digit_factors(V),
    NRA = max(0, RA - DA), NRB = max(0, RB - DB), NRC = max(0, RC - DC), NRD = max(0, RD - DD),
    NeededStr = maps:get({NRA, NRB}, DP),
    TotalNeeded = NRC + NRD + length(NeededStr),
    if TotalNeeded =< N - 1 - I ->
           Counts = count_sort_suffix(N - 1 - I - TotalNeeded, NRC, NRD, NeededStr),
           {ok, [V + $0 | build_from_counts(Counts)]};
       true -> try_v(I, N, V + 1, RA, RB, RC, RD, DP)
    end.

prefix_factors([], A, B, C, D) -> {A, B, C, D};
prefix_factors([H|T], A, B, C, D) ->
    {DA, DB, DC, DD} = get_digit_factors(H),
    prefix_factors(T, A + DA, B + DB, C + DC, D + DD).

count_sort_suffix(Ones, Fives, Sevens, NeededStr) ->
    C0 = lists:duplicate(10, 0),
    C1 = set_count(C0, 1, Ones),
    C2 = set_count(C1, 5, Fives),
    C3 = set_count(C2, 7, Sevens),
    lists:foldl(fun(Ch, Acc) -> 
        D = Ch - $0,
        set_count(Acc, D, lists:nth(D + 1, Acc) + 1)
    end, C3, NeededStr).

set_count(Counts, D, Val) ->
    lists:sublist(Counts, D) ++ [Val] ++ lists:nthtail(D + 1, Counts).

build_from_counts(Counts) ->
    lists:flatmap(fun(D) -> lists:duplicate(lists:nth(D + 1, Counts), D + $0) end, lists:seq(1, 9)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec smallest_number(num :: String.t, t :: integer) :: String.t
  def smallest_number(num, t) do
    {a, b, c, d, temp_t} = get_t_factors(t)
    if temp_t > 1 do
      "-1"
    else
      dp = build_dp()
      chars = String.to_charlist(num)
      n = length(chars)
      first_zero = Enum.find_index(chars, &(&1 == ?0)) || n
      if first_zero == n and check_orig(chars, a, b, c, d) do
        num
      else
        solve(num, chars, n, first_zero, a, b, c, d, dp)
      end
    end
  end

  defp get_t_factors(t) do
    {a, t1} = count_factors(t, 2, 0)
    {b, t2} = count_factors(t1, 3, 0)
    {c, t3} = count_factors(t2, 5, 0)
    {d, t4} = count_factors(t3, 7, 0)
    {a, b, c, d, t4}
  end

  defp count_factors(t, p, count) when t > 0 and rem(t, p) == 0, do: count_factors(div(t, p), p, count + 1)
  defp count_factors(t, _, count), do: {count, t}

  defp check_orig([], a, b, c, d), do: a <= 0 and b <= 0 and c <= 0 and d <= 0
  defp check_orig([h | t], a, b, c, d) do
    {da, db, dc, dd} = get_digit_factors(h)
    check_orig(t, a - da, b - db, c - dc, d - dd)
  end

  defp get_digit_factors(?1), do: {0, 0, 0, 0}
  defp get_digit_factors(?2), do: {1, 0, 0, 0}
  defp get_digit_factors(?3), do: {0, 1, 0, 0}
  defp get_digit_factors(?4), do: {2, 0, 0, 0}
  defp get_digit_factors(?5), do: {0, 0, 1, 0}
  defp get_digit_factors(?6), do: {1, 1, 0, 0}
  defp get_digit_factors(?7), do: {0, 0, 0, 1}
  defp get_digit_factors(?8), do: {3, 0, 0, 0}
  defp get_digit_factors(?9), do: {0, 2, 0, 0}
  defp get_digit_factors(v) when v in 1..9, do: get_digit_factors(v + ?0)

  defp build_dp() do
    dp = %{{0, 0} => []}
    digits = [{2, 1, 0}, {3, 0, 1}, {4, 2, 0}, {6, 1, 1}, {8, 3, 0}, {9, 0, 2}]
    Enum.reduce(0..47, dp, fn i, acc_i ->
      Enum.reduce(0..30, acc_i, fn j, acc_j ->
        if i == 0 and j == 0 do
          acc_j
        else
          best = Enum.reduce(digits, nil, fn {digit, da, db}, curr_best ->
            pi = max(0, i - da)
            pj = max(0, j - db)
            s = Enum.sort([digit + ?0 | Map.get(acc_j, {pi, pj})])
            if is_nil(curr_best) or length(s) < length(curr_best) or (length(s) == length(curr_best) and s < curr_best), do: s, else: curr_best
          end)
          Map.put(acc_j, {i, j}, best)
        end
      end)
    end)
  end

  defp solve(num, chars, n, first_zero, a, b, c, d, dp) do
    case find_same_length(chars, n, min(n - 1, first_zero), a, b, c, d, dp) do
      {:ok, res} -> List.to_string(res)
      :none ->
        needed_str = Map.get(dp, {a, b})
        min_len = c + d + length(needed_str)
        l = if min_len > n, do: min_len, else: n + 1
        counts = count_sort_suffix(l - min_len, c, d, needed_str)
        List.to_string(build_from_counts(counts))
    end
  end

  defp find_same_length(_, _, -1, _, _, _, _, _), do: :none
  defp find_same_length(chars, n, i, a, b, c, d, dp) do
    prefix = Enum.take(chars, i)
    {pa, pb, pc, pd} = Enum.reduce(prefix, {0, 0, 0, 0}, fn ch, {ca, cb, cc, cd} ->
      {da, db, dc, dd} = get_digit_factors(ch)
      {ca + da, cb + db, cc + dc, cd + dd}
    end)
    ra = max(0, a - pa)
    rb = max(0, b - pb)
    rc = max(0, c - pc)
    rd = max(0, d - pd)
    start_v = if Enum.at(chars, i) == ?0, do: 1, else: Enum.at(chars, i) - ?0 + 1
    case try_v(i, n, start_v, ra, rb, rc, rd, dp) do
      {:ok, suffix} -> {:ok, prefix ++ suffix}
      :none -> find_same_length(chars, n, i - 1, a, b, c, d, dp)
    end
  end

  defp try_v(_, _, 10, _, _, _, _, _), do: :none
  defp try_v(i, n, v, ra, rb, rc, rd, dp) do
    {da, db, dc, dd} = get_digit_factors(v)
    nra = max(0, ra - da)
    nrb = max(0, rb - db)
    nrc = max(0, rc - dc)
    nrd = max(0, rd - dd)
    needed_str = Map.get(dp, {nra, nrb})
    total_needed = nrc + nrd + length(needed_str)
    if total_needed <= n - 1 - i do
      counts = count_sort_suffix(n - 1 - i - total_needed, nrc, nrd, needed_str)
      {:ok, [v + ?0 | build_from_counts(counts)]}
    else
      try_v(i, n, v + 1, ra, rb, rc, rd, dp)
    end
  end

  defp count_sort_suffix(ones, fives, sevens, needed_str) do
    counts = Tuple.duplicate(0, 10)
    counts = put_elem(counts, 1, ones)
    counts = put_elem(counts, 5, fives)
    counts = put_elem(counts, 7, sevens)
    Enum.reduce(needed_str, counts, fn ch, acc ->
      d = ch - ?0
      put_elem(acc, d, elem(acc, d) + 1)
    end)
  end

  defp build_from_counts(counts) do
    Enum.flat_map(1..9, fn d -> List.duplicate(d + ?0, elem(counts, d)) end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of num. The algorithm iterates through the prefix of the string and for each position, checks up to 9 possible digits. Precomputing the DP table for factors of 2 and 3 takes constant time as the exponents for $t \le 10^{14}$ are small ($a \le 47, b \le 30$).
- **Space Complexity:** O(n) to store the result string and the prefix prime factor counts. The DP table for prime factors of 2 and 3 occupies constant space relative to $n$.
