---
layout: post
title: "Smallest Palindromic Rearrangement II"
date: 2026-07-29 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Hash Table", "Math", "String", "Combinatorics", "Counting"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    long long combinations(int n, int r, long\
        \ long limit) {\n        if (r < 0 || r > n) return 0;\n        if (r == 0 ||\
        \ r == n) return 1;\n        if (r > n / 2) r = n - r;\n        long long res\
        \ = 1;\n        for (int i = 1; i <= r; ++i) {\n            res = res * (n -\
        \ i + 1) / i;\n            if (res > limit) return limit + 1;\n        }\n \
        \       return res;\n    }\n\n    long long count_perms(const vector<int>& counts,\
        \ int total, long long limit) {\n        long long res = 1;\n        int curr_total\
        \ = total;\n        for (int c : counts) {\n            if (c > 0) {\n     \
        \           long long comb_val = combinations(curr_total, c, limit);\n     \
        \           res *= comb_val;\n                if (res > limit) return limit\
        \ + 1;\n                curr_total -= c;\n            }\n        }\n       \
        \ return res;\n    }\n\n    string smallestPalindrome(string s, int k) {\n \
        \       int n = s.length();\n        vector<int> counts(26, 0);\n        for\
        \ (char c : s) counts[c - 'a']++;\n\n        vector<int> half_counts(26, 0);\n\
        \        string mid = \"\";\n        for (int i = 0; i < 26; ++i) {\n      \
        \      if (counts[i] % 2 != 0) mid = (char)('a' + i);\n            half_counts[i]\
        \ = counts[i] / 2;\n        }\n\n        int m = n / 2;\n        if (count_perms(half_counts,\
        \ m, (long long)k) < (long long)k) return \"\";\n\n        string first_half\
        \ = \"\";\n        long long current_k = k;\n        for (int i = 0; i < m;\
        \ ++i) {\n            for (int j = 0; j < 26; ++j) {\n                if (half_counts[j]\
        \ > 0) {\n                    half_counts[j]--;\n                    long long\
        \ p = count_perms(half_counts, m - 1 - i, current_k);\n                    if\
        \ (p >= current_k) {\n                        first_half += (char)('a' + j);\n\
        \                        break;\n                    } else {\n            \
        \            current_k -= p;\n                        half_counts[j]++;\n  \
        \                  }\n                }\n            }\n        }\n\n      \
        \  string second_half = first_half;\n        reverse(second_half.begin(), second_half.end());\n\
        \        return first_half + mid + second_half;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public String smallestPalindrome(String\
        \ s, int k) {\n        int n = s.length();\n        int[] counts = new int[26];\n\
        \        for (char c : s.toCharArray()) {\n            counts[c - 'a']++;\n\
        \        }\n\n        int[] halfCounts = new int[26];\n        String mid =\
        \ \"\";\n        for (int i = 0; i < 26; i++) {\n            if (counts[i] %\
        \ 2 != 0) {\n                mid = String.valueOf((char) ('a' + i));\n     \
        \       }\n            halfCounts[i] = counts[i] / 2;\n        }\n\n       \
        \ int m = n / 2;\n        long totalPerms = countPerms(halfCounts, m, (long)\
        \ k);\n        if (totalPerms < k) return \"\";\n\n        StringBuilder firstHalf\
        \ = new StringBuilder();\n        long currentK = k;\n        for (int i = 0;\
        \ i < m; i++) {\n            for (int j = 0; j < 26; j++) {\n              \
        \  if (halfCounts[j] > 0) {\n                    halfCounts[j]--;\n        \
        \            long p = countPerms(halfCounts, m - 1 - i, currentK);\n       \
        \             if (p >= currentK) {\n                        firstHalf.append((char)\
        \ ('a' + j));\n                        break;\n                    } else {\n\
        \                        currentK -= p;\n                        halfCounts[j]++;\n\
        \                    }\n                }\n            }\n        }\n\n    \
        \    String fh = firstHalf.toString();\n        String sh = new StringBuilder(fh).reverse().toString();\n\
        \        return fh + mid + sh;\n    }\n\n    private long combinations(int n,\
        \ int r, long limit) {\n        if (r < 0 || r > n) return 0;\n        if (r\
        \ == 0 || r == n) return 1;\n        if (r > n / 2) r = n - r;\n        long\
        \ res = 1;\n        for (int i = 1; i <= r; i++) {\n            res = res *\
        \ (n - i + 1) / i;\n            if (res > limit) return limit + 1;\n       \
        \ }\n        return res;\n    }\n\n    private long countPerms(int[] counts,\
        \ int total, long limit) {\n        long res = 1;\n        int currTotal = total;\n\
        \        for (int c : counts) {\n            if (c > 0) {\n                long\
        \ combVal = combinations(currTotal, c, limit);\n                res *= combVal;\n\
        \                if (res > limit) return limit + 1;\n                currTotal\
        \ -= c;\n            }\n        }\n        return res;\n    }\n}"
      python: "class Solution(object):\n    def smallestPalindrome(self, s, k):\n  \
        \      n = len(s)\n        counts = [0] * 26\n        for char in s:\n     \
        \       counts[ord(char) - ord('a')] += 1\n\n        half_counts = [0] * 26\n\
        \        mid_char = \"\"\n        for i in range(26):\n            if counts[i]\
        \ % 2 != 0:\n                mid_char = chr(ord('a') + i)\n            half_counts[i]\
        \ = counts[i] // 2\n\n        m = n // 2\n\n        def combinations(n_val,\
        \ r_val, limit):\n            if r_val < 0 or r_val > n_val: return 0\n    \
        \        if r_val == 0 or r_val == n_val: return 1\n            if r_val > n_val\
        \ // 2: r_val = n_val - r_val\n            res = 1\n            for i in range(1,\
        \ r_val + 1):\n                res = res * (n_val - i + 1) // i\n          \
        \      if res > limit: return limit + 1\n            return res\n\n        def\
        \ count_perms(cnts, total, limit):\n            res = 1\n            curr_total\
        \ = total\n            for c in cnts:\n                if c > 0:\n         \
        \           comb_val = combinations(curr_total, c, limit)\n                \
        \    res *= comb_val\n                    if res > limit: return limit + 1\n\
        \                    curr_total -= c\n            return res\n\n        if count_perms(half_counts,\
        \ m, k) < k:\n            return \"\"\n\n        res_half = []\n        curr_k\
        \ = k\n        for i in range(m):\n            for j in range(26):\n       \
        \         if half_counts[j] > 0:\n                    half_counts[j] -= 1\n\
        \                    p = count_perms(half_counts, m - 1 - i, curr_k)\n     \
        \               if p >= curr_k:\n                        res_half.append(chr(ord('a')\
        \ + j))\n                        break\n                    else:\n        \
        \                curr_k -= p\n                        half_counts[j] += 1\n\n\
        \        first_half_str = \"\".join(res_half)\n        return first_half_str\
        \ + mid_char + first_half_str[::-1]"
      python3: "class Solution:\n    def smallestPalindrome(self, s: str, k: int) ->\
        \ str:\n        n = len(s)\n        freq = [0] * 26\n        for char in s:\n\
        \            freq[ord(char) - ord('a')] += 1\n\n        half_freq = [0] * 26\n\
        \        mid = \"\"\n        for i in range(26):\n            if freq[i] % 2\
        \ == 1:\n                mid = chr(ord('a') + i)\n            half_freq[i] =\
        \ freq[i] // 2\n\n        h = n // 2\n\n        def count_perms(total_len, counts,\
        \ limit):\n            res = 1\n            curr_n = total_len\n           \
        \ for c in counts:\n                if c > 0:\n                    for i in\
        \ range(1, c + 1):\n                        res = (res * curr_n) // i\n    \
        \                    curr_n -= 1\n                        if res > limit:\n\
        \                            return limit + 1\n            return res\n\n  \
        \      if count_perms(h, half_freq, k) < k:\n            return \"\"\n\n   \
        \     res_half = []\n        current_k = k\n        for i in range(h):\n   \
        \         for j in range(26):\n                if half_freq[j] > 0:\n      \
        \              half_freq[j] -= 1\n                    cnt = count_perms(h -\
        \ 1 - i, half_freq, current_k)\n                    if cnt >= current_k:\n \
        \                       res_half.append(chr(ord('a') + j))\n               \
        \         break\n                    else:\n                        current_k\
        \ -= cnt\n                        half_freq[j] += 1\n\n        first_half =\
        \ \"\".join(res_half)\n        return first_half + mid + first_half[::-1]"
      c: "#include <stdio.h>\n#include <string.h>\n#include <stdlib.h>\n\nlong long\
        \ countPerms(int totalLen, int* counts, long long limit) {\n    long long res\
        \ = 1;\n    int n = totalLen;\n    for (int j = 0; j < 26; j++) {\n        for\
        \ (int i = 1; i <= counts[j]; i++) {\n            res = res * n / i;\n     \
        \       n--;\n            if (res > limit) return limit + 1;\n        }\n  \
        \  }\n    return res;\n}\n\nchar* smallestPalindrome(char* s, int k) {\n   \
        \ int n = strlen(s);\n    int freq[26] = {0};\n    for (int i = 0; i < n; i++)\
        \ {\n        freq[s[i] - 'a']++;\n    }\n\n    int half_freq[26] = {0};\n  \
        \  char mid = '\\0';\n    for (int i = 0; i < 26; i++) {\n        if (freq[i]\
        \ % 2 == 1) {\n            mid = (char)('a' + i);\n        }\n        half_freq[i]\
        \ = freq[i] / 2;\n    }\n\n    int h = n / 2;\n    if (countPerms(h, half_freq,\
        \ (long long)k) < (long long)k) {\n        char* empty = (char*)malloc(1);\n\
        \        empty[0] = '\\0';\n        return empty;\n    }\n\n    char* resHalf\
        \ = (char*)malloc(h + 1);\n    long long currentK = k;\n    for (int i = 0;\
        \ i < h; i++) {\n        for (int j = 0; j < 26; j++) {\n            if (half_freq[j]\
        \ > 0) {\n                half_freq[j]--;\n                long long cnt = countPerms(h\
        \ - 1 - i, half_freq, currentK);\n                if (cnt >= currentK) {\n \
        \                   resHalf[i] = (char)('a' + j);\n                    break;\n\
        \                } else {\n                    currentK -= cnt;\n          \
        \          half_freq[j]++;\n                }\n            }\n        }\n  \
        \  }\n    resHalf[h] = '\\0';\n\n    char* result = (char*)malloc(n + 1);\n\
        \    for (int i = 0; i < h; i++) {\n        result[i] = resHalf[i];\n      \
        \  result[n - 1 - i] = resHalf[i];\n    }\n    if (n % 2 == 1) {\n        result[h]\
        \ = mid;\n    }\n    result[n] = '\\0';\n    free(resHalf);\n    return result;\n\
        }"
      csharp: "using System;\nusing System.Collections.Generic;\nusing System.Text;\n\
        \npublic class Solution {\n    public string SmallestPalindrome(string s, int\
        \ k) {\n        int n = s.Length;\n        int[] freq = new int[26];\n     \
        \   for (int i = 0; i < n; i++) {\n            freq[s[i] - 'a']++;\n       \
        \ }\n\n        int[] halfFreq = new int[26];\n        char mid = '\\0';\n  \
        \      for (int i = 0; i < 26; i++) {\n            if (freq[i] % 2 == 1) {\n\
        \                mid = (char)('a' + i);\n            }\n            halfFreq[i]\
        \ = freq[i] / 2;\n        }\n\n        int h = n / 2;\n        if (CountPerms(h,\
        \ halfFreq, k) < k) {\n            return \"\";\n        }\n\n        char[]\
        \ resHalf = new char[h];\n        long currentK = k;\n        for (int i = 0;\
        \ i < h; i++) {\n            for (int j = 0; j < 26; j++) {\n              \
        \  if (halfFreq[j] > 0) {\n                    halfFreq[j]--;\n            \
        \        long cnt = CountPerms(h - 1 - i, halfFreq, currentK);\n           \
        \         if (cnt >= currentK) {\n                        resHalf[i] = (char)('a'\
        \ + j);\n                        break;\n                    } else {\n    \
        \                    currentK -= cnt;\n                        halfFreq[j]++;\n\
        \                    }\n                }\n            }\n        }\n\n    \
        \    StringBuilder sb = new StringBuilder();\n        sb.Append(resHalf);\n\
        \        if (n % 2 == 1) {\n            sb.Append(mid);\n        }\n       \
        \ for (int i = h - 1; i >= 0; i--) {\n            sb.Append(resHalf[i]);\n \
        \       }\n        return sb.ToString();\n    }\n\n    private long CountPerms(int\
        \ totalLen, int[] counts, long limit) {\n        long res = 1;\n        int\
        \ n = totalLen;\n        for (int j = 0; j < 26; j++) {\n            for (int\
        \ i = 1; i <= counts[j]; i++) {\n                res = res * n / i;\n      \
        \          n--;\n                if (res > limit) return limit + 1;\n      \
        \      }\n        }\n        return res;\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @param {number} k\n * @return {string}\n\
        \ */\nvar smallestPalindrome = function(s, k) {\n    let n = s.length;\n   \
        \ let freq = new Array(26).fill(0);\n    for (let i = 0; i < n; i++) {\n   \
        \     freq[s.charCodeAt(i) - 97]++;\n    }\n\n    let half_freq = new Array(26).fill(0);\n\
        \    let mid = \"\";\n    for (let i = 0; i < 26; i++) {\n        if (freq[i]\
        \ % 2 === 1) {\n            mid = String.fromCharCode(97 + i);\n        }\n\
        \        half_freq[i] = Math.floor(freq[i] / 2);\n    }\n\n    let h = Math.floor(n\
        \ / 2);\n\n    function countPerms(totalLen, counts, limit) {\n        let res\
        \ = 1;\n        let currentN = totalLen;\n        for (let j = 0; j < 26; j++)\
        \ {\n            for (let i = 1; i <= counts[j]; i++) {\n                res\
        \ = (res * currentN) / i;\n                currentN--;\n                if (res\
        \ > limit) return limit + 1;\n            }\n        }\n        return res;\n\
        \    }\n\n    if (countPerms(h, half_freq, k) < k) {\n        return \"\";\n\
        \    }\n\n    let resHalf = [];\n    let currentK = k;\n    for (let i = 0;\
        \ i < h; i++) {\n        for (let j = 0; j < 26; j++) {\n            if (half_freq[j]\
        \ > 0) {\n                half_freq[j]--;\n                let cnt = countPerms(h\
        \ - 1 - i, half_freq, currentK);\n                if (cnt >= currentK) {\n \
        \                   resHalf.push(String.fromCharCode(97 + j));\n           \
        \         break;\n                } else {\n                    currentK -=\
        \ cnt;\n                    half_freq[j]++;\n                }\n           \
        \ }\n        }\n    }\n\n    let firstHalf = resHalf.join('');\n    let secondHalf\
        \ = resHalf.slice().reverse().join('');\n    return firstHalf + mid + secondHalf;\n\
        };"
      typescript: "function smallestPalindrome(s: string, k: number): string {\n   \
        \ const n = s.length;\n    const counts = new Array(26).fill(0);\n    for (let\
        \ i = 0; i < n; i++) {\n        counts[s.charCodeAt(i) - 97]++;\n    }\n\n \
        \   const halfCounts = new Array(26).fill(0);\n    let midChar = \"\";\n   \
        \ for (let i = 0; i < 26; i++) {\n        if (counts[i] % 2 !== 0) {\n     \
        \       midChar = String.fromCharCode(i + 97);\n        }\n        halfCounts[i]\
        \ = Math.floor(counts[i] / 2);\n    }\n\n    const halfLen = Math.floor(n /\
        \ 2);\n    const limit = k + 1;\n\n    function countPermutations(L: number,\
        \ cArr: number[], lim: number): number {\n        if (L === 0) return 1;\n \
        \       let res = 1;\n        let remL = L;\n        for (let i = 0; i < 26;\
        \ i++) {\n            let c = cArr[i];\n            if (c === 0) continue;\n\
        \            let charWays = 1;\n            for (let j = 1; j <= c; j++) {\n\
        \                charWays = Math.floor((charWays * remL) / j);\n           \
        \     remL--;\n                if (charWays >= lim) {\n                    charWays\
        \ = lim;\n                    break;\n                }\n            }\n   \
        \         res *= charWays;\n            if (res >= lim) return lim;\n      \
        \  }\n        return res;\n    }\n\n    if (countPermutations(halfLen, halfCounts,\
        \ limit) < k) {\n        return \"\";\n    }\n\n    let firstHalf = \"\";\n\
        \    const currentHalfCounts = [...halfCounts];\n    for (let i = 0; i < halfLen;\
        \ i++) {\n        for (let j = 0; j < 26; j++) {\n            if (currentHalfCounts[j]\
        \ > 0) {\n                currentHalfCounts[j]--;\n                const ways\
        \ = countPermutations(halfLen - 1 - i, currentHalfCounts, limit);\n        \
        \        if (ways >= k) {\n                    firstHalf += String.fromCharCode(j\
        \ + 97);\n                    break;\n                } else {\n           \
        \         k -= ways;\n                    currentHalfCounts[j]++;\n        \
        \        }\n            }\n        }\n    }\n\n    const secondHalf = firstHalf.split(\"\
        \").reverse().join(\"\");\n    return firstHalf + midChar + secondHalf;\n}"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @param Integer\
        \ $k\n     * @return String\n     */\n    function smallestPalindrome($s, $k)\
        \ {\n        $n = strlen($s);\n        $counts = array_fill(0, 26, 0);\n   \
        \     for ($i = 0; $i < $n; $i++) {\n            $counts[ord($s[$i]) - 97]++;\n\
        \        }\n\n        $halfCounts = array_fill(0, 26, 0);\n        $midChar\
        \ = \"\";\n        for ($i = 0; $i < 26; $i++) {\n            if ($counts[$i]\
        \ % 2 !== 0) {\n                $midChar = chr($i + 97);\n            }\n  \
        \          $halfCounts[$i] = (int)($counts[$i] / 2);\n        }\n\n        $halfLen\
        \ = (int)($n / 2);\n        $limit = $k + 1;\n\n        if ($this->countPermutations($halfLen,\
        \ $halfCounts, $limit) < $k) {\n            return \"\";\n        }\n\n    \
        \    $firstHalf = \"\";\n        $currentHalfCounts = $halfCounts;\n       \
        \ for ($i = 0; $i < $halfLen; $i++) {\n            for ($j = 0; $j < 26; $j++)\
        \ {\n                if ($currentHalfCounts[$j] > 0) {\n                   \
        \ $currentHalfCounts[$j]--;\n                    $ways = $this->countPermutations($halfLen\
        \ - 1 - $i, $currentHalfCounts, $limit);\n                    if ($ways >= $k)\
        \ {\n                        $firstHalf .= chr($j + 97);\n                 \
        \       break;\n                    } else {\n                        $k -=\
        \ $ways;\n                        $currentHalfCounts[$j]++;\n              \
        \      }\n                }\n            }\n        }\n\n        return $firstHalf\
        \ . $midChar . strrev($firstHalf);\n    }\n\n    private function countPermutations($L,\
        \ $cArr, $lim) {\n        if ($L === 0) return 1;\n        $res = 1;\n     \
        \   $remL = $L;\n        for ($i = 0; $i < 26; $i++) {\n            $c = $cArr[$i];\n\
        \            if ($c === 0) continue;\n            $charWays = 1;\n         \
        \   for ($j = 1; $j <= $c; $j++) {\n                $charWays = (int)(($charWays\
        \ * $remL) / $j);\n                $remL--;\n                if ($charWays >=\
        \ $lim) {\n                    $charWays = $lim;\n                    break;\n\
        \                }\n            }\n            $res *= $charWays;\n        \
        \    if ($res >= $lim) return $lim;\n        }\n        return $res;\n    }\n\
        }"
      swift: "class Solution {\n    func smallestPalindrome(_ s: String, _ k: Int) ->\
        \ String {\n        let n = s.count\n        var counts = [Int](repeating: 0,\
        \ count: 26)\n        let aValue = Int(UnicodeScalar(\"a\").value)\n\n     \
        \   for char in s.unicodeScalars {\n            counts[Int(char.value) - aValue]\
        \ += 1\n        }\n\n        var halfCounts = [Int](repeating: 0, count: 26)\n\
        \        var midChar = \"\"\n        for i in 0..<26 {\n            if counts[i]\
        \ % 2 != 0 {\n                midChar = String(UnicodeScalar(aValue + i)!)\n\
        \            }\n            halfCounts[i] = counts[i] / 2\n        }\n\n   \
        \     let halfLen = n / 2\n        let limit = k + 1\n        var currentK =\
        \ k\n\n        if countPermutations(halfLen, halfCounts, limit) < currentK {\n\
        \            return \"\"\n        }\n\n        var firstHalf = \"\"\n      \
        \  var currentHalfCounts = halfCounts\n\n        for i in 0..<halfLen {\n  \
        \          for j in 0..<26 {\n                if currentHalfCounts[j] > 0 {\n\
        \                    currentHalfCounts[j] -= 1\n                    let ways\
        \ = countPermutations(halfLen - 1 - i, currentHalfCounts, limit)\n         \
        \           if ways >= currentK {\n                        firstHalf.append(Character(UnicodeScalar(aValue\
        \ + j)!))\n                        break\n                    } else {\n   \
        \                     currentK -= ways\n                        currentHalfCounts[j]\
        \ += 1\n                    }\n                }\n            }\n        }\n\
        \n        return firstHalf + midChar + String(firstHalf.reversed())\n    }\n\
        \n    private func countPermutations(_ L: Int, _ cArr: [Int], _ lim: Int) ->\
        \ Int {\n        if L == 0 { return 1 }\n        var res = 1\n        var remL\
        \ = L\n        for i in 0..<26 {\n            let c = cArr[i]\n            if\
        \ c == 0 { continue }\n            var charWays = 1\n            for j in 1...c\
        \ {\n                charWays = (charWays * remL) / j\n                remL\
        \ -= 1\n                if charWays >= lim {\n                    charWays =\
        \ lim\n                    break\n                }\n            }\n       \
        \     res *= charWays\n            if res >= lim { return lim }\n        }\n\
        \        return res\n    }\n}"
      kotlin: "class Solution {\n    fun smallestPalindrome(s: String, k: Int): String\
        \ {\n        val n = s.length\n        val counts = IntArray(26)\n        for\
        \ (char in s) {\n            counts[char - 'a']++\n        }\n\n        val\
        \ halfCounts = IntArray(26)\n        var midChar = \"\"\n        for (i in 0\
        \ until 26) {\n            if (counts[i] % 2 != 0) {\n                midChar\
        \ = (i + 'a'.toInt()).toChar().toString()\n            }\n            halfCounts[i]\
        \ = counts[i] / 2\n        }\n\n        val halfLen = n / 2\n        val limit\
        \ = k + 1\n        var currentK = k\n\n        if (countPermutations(halfLen,\
        \ halfCounts, limit) < currentK) {\n            return \"\"\n        }\n\n \
        \       val firstHalf = StringBuilder()\n        val currentHalfCounts = halfCounts.copyOf()\n\
        \        for (i in 0 until halfLen) {\n            for (j in 0 until 26) {\n\
        \                if (currentHalfCounts[j] > 0) {\n                    currentHalfCounts[j]--\n\
        \                    val ways = countPermutations(halfLen - 1 - i, currentHalfCounts,\
        \ limit)\n                    if (ways >= currentK) {\n                    \
        \    firstHalf.append((j + 'a'.toInt()).toChar())\n                        break\n\
        \                    } else {\n                        currentK -= ways\n  \
        \                      currentHalfCounts[j]++\n                    }\n     \
        \           }\n            }\n        }\n\n        val firstHalfStr = firstHalf.toString()\n\
        \        return firstHalfStr + midChar + firstHalfStr.reversed()\n    }\n\n\
        \    private fun countPermutations(L: Int, cArr: IntArray, lim: Int): Int {\n\
        \        if (L == 0) return 1\n        var res: Long = 1\n        var remL =\
        \ L\n        val limitLong = lim.toLong()\n        for (i in 0 until 26) {\n\
        \            val c = cArr[i]\n            if (c == 0) continue\n           \
        \ var charWays: Long = 1\n            for (j in 1..c) {\n                charWays\
        \ = (charWays * remL) / j\n                remL--\n                if (charWays\
        \ >= limitLong) {\n                    charWays = limitLong\n              \
        \      break\n                }\n            }\n            res *= charWays\n\
        \            if (res >= limitLong) return limitLong.toInt()\n        }\n   \
        \     return res.toInt()\n    }\n}"
      dart: "class Solution {\n  String smallestPalindrome(String s, int k) {\n    int\
        \ n = s.length;\n    List<int> charCounts = List.filled(26, 0);\n    for (int\
        \ i = 0; i < n; i++) {\n      charCounts[s.codeUnitAt(i) - 97]++;\n    }\n\n\
        \    List<int> halfCounts = List.filled(26, 0);\n    String midChar = \"\";\n\
        \    for (int i = 0; i < 26; i++) {\n      halfCounts[i] = charCounts[i] ~/\
        \ 2;\n      if (charCounts[i] % 2 != 0) {\n        midChar = String.fromCharCode(97\
        \ + i);\n      }\n    }\n\n    int L = n ~/ 2;\n    int limit = 1000000000000000;\n\
        \    int totalPossible = 1;\n    int currL = 0;\n    for (int i = 0; i < 26;\
        \ i++) {\n      for (int j = 1; j <= halfCounts[i]; j++) {\n        currL++;\n\
        \        if (totalPossible >= limit) {\n          totalPossible = limit;\n \
        \       } else {\n          totalPossible = (totalPossible * currL) ~/ j;\n\
        \          if (totalPossible > limit) totalPossible = limit;\n        }\n  \
        \    }\n    }\n    if (totalPossible > limit) totalPossible = limit;\n\n   \
        \ if (k > totalPossible) return \"\";\n\n    int kLong = k;\n    List<int> firstHalfCodes\
        \ = [];\n    int currentTotal = totalPossible;\n\n    for (int i = 0; i < L;\
        \ i++) {\n      int remLen = L - i;\n      for (int j = 0; j < 26; j++) {\n\
        \        if (halfCounts[j] > 0) {\n          int wj = (currentTotal >= limit)\n\
        \              ? limit\n              : (currentTotal * halfCounts[j]) ~/ remLen;\n\
        \          if (kLong <= wj) {\n            firstHalfCodes.add(97 + j);\n   \
        \         halfCounts[j]--;\n            currentTotal = wj;\n            break;\n\
        \          } else {\n            kLong -= wj;\n          }\n        }\n    \
        \  }\n    }\n\n    List<int> resCodes = List.filled(n, 0);\n    for (int i =\
        \ 0; i < L; i++) {\n      resCodes[i] = firstHalfCodes[i];\n      resCodes[n\
        \ - 1 - i] = firstHalfCodes[i];\n    }\n    if (n % 2 != 0) {\n      resCodes[L]\
        \ = midChar.codeUnitAt(0);\n    }\n    return String.fromCharCodes(resCodes);\n\
        \  }\n}"
      go: "func smallestPalindrome(s string, k int) string {\n\tn := len(s)\n\tcharCounts\
        \ := make([]int, 26)\n\tfor i := 0; i < n; i++ {\n\t\tcharCounts[s[i]-'a']++\n\
        \t}\n\n\thalfCounts := make([]int, 26)\n\tvar midChar byte\n\thasMid := false\n\
        \tfor i := 0; i < 26; i++ {\n\t\thalfCounts[i] = charCounts[i] / 2\n\t\tif charCounts[i]%2\
        \ != 0 {\n\t\t\tmidChar = byte('a' + i)\n\t\t\thasMid = true\n\t\t}\n\t}\n\n\
        \tL := n / 2\n\tlimit := int64(1000000000000000)\n\tvar totalPossible int64\
        \ = 1\n\tcurrL := 0\n\tfor i := 0; i < 26; i++ {\n\t\tfor j := 1; j <= halfCounts[i];\
        \ j++ {\n\t\t\tcurrL++\n\t\t\tif totalPossible >= limit {\n\t\t\t\ttotalPossible\
        \ = limit\n\t\t\t} else {\n\t\t\t\ttotalPossible = (totalPossible * int64(currL))\
        \ / int64(j)\n\t\t\t\tif totalPossible > limit {\n\t\t\t\t\ttotalPossible =\
        \ limit\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\t}\n\n\tif int64(k) > totalPossible {\n\
        \t\treturn \"\"\n\t}\n\n\tk64 := int64(k)\n\tfirstHalf := make([]byte, L)\n\t\
        currentTotal := totalPossible\n\n\tfor i := 0; i < L; i++ {\n\t\tremLen := L\
        \ - i\n\t\tfor j := 0; j < 26; j++ {\n\t\t\tif halfCounts[j] > 0 {\n\t\t\t\t\
        var wj int64\n\t\t\t\tif currentTotal >= limit {\n\t\t\t\t\twj = limit\n\t\t\
        \t\t} else {\n\t\t\t\t\twj = (currentTotal * int64(halfCounts[j])) / int64(remLen)\n\
        \t\t\t\t}\n\t\t\t\tif k64 <= wj {\n\t\t\t\t\tfirstHalf[i] = byte('a' + j)\n\t\
        \t\t\t\thalfCounts[j]--\n\t\t\t\t\tcurrentTotal = wj\n\t\t\t\t\tbreak\n\t\t\t\
        \t} else {\n\t\t\t\t\tk64 -= wj\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\t}\n\n\tres :=\
        \ make([]byte, n)\n\tfor i := 0; i < L; i++ {\n\t\tres[i] = firstHalf[i]\n\t\
        \tres[n-1-i] = firstHalf[i]\n\t}\n\tif hasMid {\n\t\tres[L] = midChar\n\t}\n\
        \treturn string(res)\n}"
      ruby: "# @param {String} s\n# @param {Integer} k\n# @return {String}\ndef smallest_palindrome(s,\
        \ k)\n  n = s.length\n  char_counts = Array.new(26, 0)\n  s.each_char { |c|\
        \ char_counts[c.ord - 'a'.ord] += 1 }\n\n  half_counts = Array.new(26, 0)\n\
        \  mid_char = \"\"\n  char_counts.each_with_index do |count, i|\n    half_counts[i]\
        \ = count / 2\n    mid_char = ('a'.ord + i).chr if count.odd?\n  end\n\n  l_len\
        \ = n / 2\n  limit = 10**15\n  total_possible = 1\n  curr_l = 0\n  half_counts.each\
        \ do |count|\n    (1..count).each do |j|\n      curr_l += 1\n      if total_possible\
        \ >= limit\n        total_possible = limit\n      else\n        total_possible\
        \ = (total_possible * curr_l) / j\n        total_possible = limit if total_possible\
        \ > limit\n      end\n    end\n  end\n\n  return \"\" if k > total_possible\n\
        \n  first_half = \"\"\n  current_total = total_possible\n  l_len.times do |i|\n\
        \    rem_len = l_len - i\n    26.times do |j|\n      if half_counts[j] > 0\n\
        \        w_j = current_total >= limit ? limit : (current_total * half_counts[j])\
        \ / rem_len\n        if k <= w_j\n          first_half << ('a'.ord + j).chr\n\
        \          half_counts[j] -= 1\n          current_total = w_j\n          break\n\
        \        else\n          k -= w_j\n        end\n      end\n    end\n  end\n\n\
        \  first_half + mid_char + first_half.reverse\nend"
      scala: "object Solution {\n  def smallestPalindrome(s: String, k: Int): String\
        \ = {\n    val n = s.length\n    val charCounts = new Array[Int](26)\n    for\
        \ (c <- s) {\n      charCounts(c - 'a') += 1\n    }\n\n    val halfCounts =\
        \ new Array[Int](26)\n    var midChar = \"\"\n    for (i <- 0 until 26) {\n\
        \      halfCounts(i) = charCounts(i) / 2\n      if (charCounts(i) % 2 != 0)\
        \ {\n        midChar = ('a' + i).toChar.toString\n      }\n    }\n\n    val\
        \ L = n / 2\n    val limit = 1000000000000000L\n    var totalPossible = 1L\n\
        \    var currL = 0\n    for (i <- 0 until 26) {\n      for (j <- 1 to halfCounts(i))\
        \ {\n        currL += 1\n        if (totalPossible >= limit) {\n          totalPossible\
        \ = limit\n        } else {\n          totalPossible = (totalPossible * currL)\
        \ / j\n          if (totalPossible > limit) totalPossible = limit\n        }\n\
        \      }\n    }\n\n    if (k.toLong > totalPossible) return \"\"\n\n    var\
        \ kLong = k.toLong\n    val firstHalf = new StringBuilder()\n    var currentTotal\
        \ = totalPossible\n\n    for (i <- 0 until L) {\n      val remLen = L - i\n\
        \      var found = false\n      var j = 0\n      while (j < 26 && !found) {\n\
        \        if (halfCounts(j) > 0) {\n          val wj = if (currentTotal >= limit)\
        \ limit else (currentTotal * halfCounts(j)) / remLen\n          if (kLong <=\
        \ wj) {\n            firstHalf.append(('a' + j).toChar)\n            halfCounts(j)\
        \ -= 1\n            currentTotal = wj\n            found = true\n          }\
        \ else {\n            kLong -= wj\n          }\n        }\n        j += 1\n\
        \      }\n    }\n\n    val firstHalfStr = firstHalf.toString()\n    firstHalfStr\
        \ + midChar + firstHalfStr.reverse\n  }\n}"
      rust: "impl Solution {\n    pub fn smallest_palindrome(s: String, k: i32) -> String\
        \ {\n        let n = s.len();\n        let mut freq = [0; 26];\n        for\
        \ b in s.bytes() {\n            freq[(b - b'a') as usize] += 1;\n        }\n\
        \        let mut half_freq = [0; 26];\n        let mut mid_char = None;\n  \
        \      for i in 0..26 {\n            half_freq[i] = freq[i] / 2;\n         \
        \   if freq[i] % 2 == 1 {\n                mid_char = Some((b'a' + i as u8)\
        \ as char);\n            }\n        }\n        let half_len = n / 2;\n     \
        \   let k_u64 = k as u64;\n        let limit = k_u64 * 10001 + 7;\n        let\
        \ mut w_total = Self::calculate_ways(&half_freq, limit);\n        if w_total\
        \ < k_u64 {\n            return \"\".to_string();\n        }\n        let mut\
        \ res = Vec::new();\n        let mut current_k = k_u64;\n        let mut total_rem\
        \ = half_len as u64;\n        for _ in 0..half_len {\n            for c in 0..26\
        \ {\n                if half_freq[c] > 0 {\n                    let w_c = if\
        \ w_total >= limit {\n                        limit\n                    } else\
        \ {\n                        (w_total * half_freq[c] as u64) / total_rem\n \
        \                   };\n                    if w_c >= current_k {\n        \
        \                res.push((b'a' + c as u8) as char);\n                     \
        \   half_freq[c] -= 1;\n                        w_total = w_c;\n           \
        \             total_rem -= 1;\n                        break;\n            \
        \        } else {\n                        current_k -= w_c;\n             \
        \       }\n                }\n            }\n        }\n        let first_half:\
        \ String = res.into_iter().collect();\n        let mut result = first_half.clone();\n\
        \        if let Some(c) = mid_char {\n            result.push(c);\n        }\n\
        \        result.push_str(&first_half.chars().rev().collect::<String>());\n \
        \       result\n    }\n\n    fn calculate_ways(counts: &[i32; 26], limit: u64)\
        \ -> u64 {\n        let mut res: u64 = 1;\n        let mut current_total: u64\
        \ = 0;\n        for &count in counts {\n            if count == 0 { continue;\
        \ }\n            for j in 1..=(count as u64) {\n                let next_res\
        \ = (res as u128 * (current_total + j) as u128) / j as u128;\n             \
        \   if next_res >= limit as u128 {\n                    return limit;\n    \
        \            } else {\n                    res = next_res as u64;\n        \
        \        }\n            }\n            current_total += count as u64;\n    \
        \    }\n        res\n    }\n}"
      racket: "(define/contract (smallest-palindrome s k)\n  (-> string? exact-integer?\
        \ string?)\n  (let* ([n (string-length s)]\n         [freq (make-vector 26 0)])\n\
        \    (for ([c (in-string s)])\n      (let ([idx (- (char->integer c) 97)])\n\
        \        (vector-set! freq idx (+ (vector-ref freq idx) 1))))\n    (let* ([half-freq\
        \ (make-vector 26 0)]\n           [mid-char \"\"])\n      (for ([i (in-range\
        \ 26)])\n        (vector-set! half-freq i (quotient (vector-ref freq i) 2))\n\
        \        (when (= (remainder (vector-ref freq i) 2) 1)\n          (set! mid-char\
        \ (string (integer->char (+ 97 i))))))\n      (let* ([half-len (quotient n 2)]\n\
        \             [limit (+ (* k 10001) 7)]\n             [calculate-ways\n    \
        \          (lambda (counts limit)\n                (let loop-counts ([idx 0]\
        \ [current-rem 0] [res 1])\n                  (if (= idx 26)\n             \
        \         res\n                      (let ([cnt (vector-ref counts idx)])\n\
        \                        (if (= cnt 0)\n                            (loop-counts\
        \ (+ idx 1) current-rem res)\n                            (let loop-j ([j 1]\
        \ [j-res res] [j-rem current-rem])\n                              (if (> j cnt)\n\
        \                                  (loop-counts (+ idx 1) j-rem j-res)\n   \
        \                               (let ([next-res (quotient (* j-res (+ j-rem\
        \ 1)) j)])\n                                    (if (>= next-res limit)\n  \
        \                                      limit\n                             \
        \           (loop-j (+ j 1) next-res (+ j-rem 1)))))))))))]\n             [w-total\
        \ (calculate-ways half-freq limit)])\n        (if (< w-total k)\n          \
        \  \"\"\n            (let* ([res-indices '()]\n                   [curr-k k]\n\
        \                   [curr-w-total w-total]\n                   [total-rem half-len])\n\
        \              (for ([i (in-range half-len)])\n                (let ([found\
        \ #f])\n                  (for ([c (in-range 26)] #:break found)\n         \
        \           (let ([count (vector-ref half-freq c)])\n                      (when\
        \ (> count 0)\n                        (let ([w-c (if (>= curr-w-total limit)\n\
        \                                       limit\n                            \
        \           (quotient (* curr-w-total count) total-rem))])\n               \
        \           (if (>= w-c curr-k)\n                              (begin\n    \
        \                            (set! res-indices (cons c res-indices))\n     \
        \                           (vector-set! half-freq c (- count 1))\n        \
        \                        (set! curr-w-total w-c)\n                         \
        \       (set! total-rem (- total-rem 1))\n                                (set!\
        \ found #t))\n                              (set! curr-k (- curr-k w-c))))))))\n\
        \              (let* ([first-half-list (map (lambda (c) (integer->char (+ 97\
        \ c))) (reverse res-indices))]\n                     [first-half (list->string\
        \ first-half-list)]\n                     [second-half (list->string (reverse\
        \ first-half-list))])\n                (string-append first-half mid-char second-half))))))))"
      erlang: "-spec smallest_palindrome(S :: unicode:unicode_binary(), K :: integer())\
        \ -> unicode:unicode_binary().\nsmallest_palindrome(S, K) ->\n    N = byte_size(S),\n\
        \    Freqs = lists:foldl(fun(C, Acc) ->\n        Idx = C - $a + 1,\n       \
        \ setelement(Idx, Acc, element(Idx, Acc) + 1)\n    end, {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},\
        \ binary_to_list(S)),\n    {HalfFreq, MidChar} = lists:foldl(fun(I, {H, M})\
        \ ->\n        F = element(I, Freqs),\n        NH = setelement(I, H, F div 2),\n\
        \        NM = if F rem 2 == 1 -> [I + $a - 1 | M]; true -> M end,\n        {NH,\
        \ NM}\n    end, {{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}, []},\
        \ lists:seq(1, 26)),\n    HalfLen = N div 2,\n    Limit = K * 10001 + 7,\n \
        \   WTotal = calculate_ways(HalfFreq, Limit),\n    if\n        WTotal < K ->\
        \ <<\"\">>;\n        true ->\n            {ResCodes, _, _, _} = lists:foldl(fun(_,\
        \ {Acc, CurrK, CurrWTotal, TotalRem, HF}) ->\n                {NewAcc, NewK,\
        \ NewW, NewRem, NewHF} = find_char(1, Acc, CurrK, CurrWTotal, TotalRem, HF,\
        \ Limit),\n                {NewAcc, NewK, NewW, NewRem, NewHF}\n           \
        \ end, {[], K, WTotal, HalfLen, HalfFreq}, lists:seq(1, HalfLen)),\n       \
        \     FirstHalf = lists:reverse(ResCodes),\n            unicode:characters_to_binary(FirstHalf\
        \ ++ MidChar ++ lists:reverse(FirstHalf))\n    end.\n\nfind_char(C, Acc, K,\
        \ WTotal, TotalRem, HF, Limit) ->\n    Count = element(C, HF),\n    if\n   \
        \     Count > 0 ->\n            WC = if WTotal >= Limit -> Limit; true -> (WTotal\
        \ * Count) div TotalRem end,\n            if\n                WC >= K ->\n \
        \                   { [C + $a - 1 | Acc], K, WC, TotalRem - 1, setelement(C,\
        \ HF, Count - 1) };\n                true ->\n                    find_char(C\
        \ + 1, Acc, K - WC, WTotal, TotalRem, HF, Limit)\n            end;\n       \
        \ true ->\n            find_char(C + 1, Acc, K, WTotal, TotalRem, HF, Limit)\n\
        \    end.\n\ncalculate_ways(HF, Limit) ->\n    HFList = tuple_to_list(HF),\n\
        \    lists:foldl(fun(Count, {Res, CurrentTotal}) ->\n        if \n         \
        \   Count == 0 -> {Res, CurrentTotal};\n            true -> \n             \
        \   {NextRes, NextTotal} = combinations_inner(1, Res, CurrentTotal, Count, Limit),\n\
        \                {NextRes, NextTotal}\n        end\n    end, {1, 0}, HFList)\
        \ |> (fun({R, _}) -> R end).\n\ncombinations_inner(J, Res, CurrentTotal, Count,\
        \ Limit) when J =< Count ->\n    NextRes = (Res * (CurrentTotal + J)) div J,\n\
        \    if\n        NextRes >= Limit -> {Limit, CurrentTotal + Count};\n      \
        \  true -> combinations_inner(J + 1, NextRes, CurrentTotal, Count, Limit)\n\
        \    end;\ncombinations_inner(_J, Res, CurrentTotal, _Count, _Limit) -> {Res,\
        \ CurrentTotal}.\n\n'|>' (Val, Fun) -> Fun(Val)."
      elixir: "defmodule Solution do\n  @spec smallest_palindrome(s :: String.t, k ::\
        \ integer) :: String.t\n  def smallest_palindrome(s, k) do\n    n = String.length(s)\n\
        \    freqs = s |> String.to_charlist() |> Enum.reduce(%{}, fn c, acc -> Map.update(acc,\
        \ c, 1, &(&1 + 1)) end)\n\n    {half_freq, mid_char} = Enum.reduce(?a..?z, {%{},\
        \ \"\"}, fn c, {hf, mid} ->\n      count = Map.get(freqs, c, 0)\n      new_hf\
        \ = Map.put(hf, c, div(count, 2))\n      new_mid = if rem(count, 2) == 1, do:\
        \ <<c>>, else: mid\n      {new_hf, new_mid}\n    end)\n\n    half_len = div(n,\
        \ 2)\n    limit = k * 10001 + 7\n    w_total = calculate_ways(half_freq, limit)\n\
        \n    if w_total < k do\n      \"\"\n    else\n      {res_chars, _, _, _, _}\
        \ = Enum.reduce(1..half_len, {[], k, w_total, half_len, half_freq}, fn _, {acc,\
        \ curr_k, curr_w_total, total_rem, hf} ->\n        {char, next_k, next_w, next_rem,\
        \ next_hf} = find_next_char(?a, curr_k, curr_w_total, total_rem, hf, limit)\n\
        \        {[char | acc], next_k, next_w, next_rem, next_hf}\n      end)\n\n \
        \     first_half = res_chars |> Enum.reverse() |> List.to_string()\n      first_half\
        \ <> mid_char <> String.reverse(first_half)\n    end\n  end\n\n  defp find_next_char(c,\
        \ k, w_total, total_rem, hf, limit) do\n    count = Map.get(hf, c, 0)\n    if\
        \ count > 0 do\n      w_c = if w_total >= limit, do: limit, else: div(w_total\
        \ * count, total_rem)\n      if w_c >= k do\n        {c, k, w_c, total_rem -\
        \ 1, Map.put(hf, c, count - 1)}\n      else\n        find_next_char(c + 1, k\
        \ - w_c, w_total, total_rem, hf, limit)\n      end\n    else\n      find_next_char(c\
        \ + 1, k, w_total, total_rem, hf, limit)\n    end\n  end\n\n  defp calculate_ways(hf,\
        \ limit) do\n    {res, _} = Enum.reduce(?a..?z, {1, 0}, fn c, {res, current_total}\
        \ ->\n      count = Map.get(hf, c, 0)\n      if count == 0 do\n        {res,\
        \ current_total}\n      else\n        Enum.reduce_while(1..count, {res, current_total},\
        \ fn j, {r, t} ->\n          next_res = div(r * (t + j), j)\n          if next_res\
        \ >= limit do\n            {:halt, {limit, t + count}}\n          else\n   \
        \         {:cont, {next_res, t + j}}\n          end\n        end)\n      end\n\
        \    end)\n    res\n  end\nend"
    approach: A palindromic string of length $n$ is determined by its first $m = \lfloor
      n/2 \rfloor$ characters. Since the string $s$ is already palindromic, we calculate
      the character frequencies in $s$ and halve them to get the counts for the first
      half of any palindromic rearrangement. If $n$ is odd, the character with an odd
      frequency remains as the central character. The problem is then reduced to finding
      the $k$-th lexicographical permutation of the multiset of characters forming the
      first half.
    time_complexity: O(N · |Σ|^2) where $N$ is the length of the string and $|Σ| = 26$.
      For each of the $N/2$ positions in the first half, we iterate through the alphabet.
      For each candidate, we compute the multinomial coefficient for the remaining characters,
      which is capped at $k$. The combinatorics calculations exit early due to this
      cap, ensuring efficient processing.
    space_complexity: O(N) to store the character counts, the constructed first-half
      string, and the final palindromic result string.
    elapsed_time: 996.1193497180939
    model: gemini-3-flash-preview
    generated_at: '2026-07-29 02:10:12 '
---

## Problem #3518: Smallest Palindromic Rearrangement II

**Difficulty:** Hard

**Topics:** Hash Table, Math, String, Combinatorics, Counting

## Problem Description

<p data-end="332" data-start="99">You are given a <strong><span data-keyword="palindrome-string">palindromic</span></strong> string <code>s</code> and an integer <code>k</code>.</p>

<p>Return the <strong>k-th</strong> <strong><span data-keyword="lexicographically-smaller-string">lexicographically smallest</span></strong> palindromic <span data-keyword="permutation-string">permutation</span> of <code>s</code>. If there are fewer than <code>k</code> distinct palindromic permutations, return an empty string.</p>

<p><strong>Note:</strong> Different rearrangements that yield the same palindromic string are considered identical and are counted once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abba&quot;, k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;baab&quot;</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The two distinct palindromic rearrangements of <code>&quot;abba&quot;</code> are <code>&quot;abba&quot;</code> and <code>&quot;baab&quot;</code>.</li>
	<li>Lexicographically, <code>&quot;abba&quot;</code> comes before <code>&quot;baab&quot;</code>. Since <code>k = 2</code>, the output is <code>&quot;baab&quot;</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;aa&quot;, k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;&quot;</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>There is only one palindromic rearrangement: <code data-end="1112" data-start="1106">&quot;aa&quot;</code>.</li>
	<li>The output is an empty string since <code>k = 2</code> exceeds the number of possible rearrangements.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;bacab&quot;, k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;abcba&quot;</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The two distinct palindromic rearrangements of <code>&quot;bacab&quot;</code> are <code>&quot;abcba&quot;</code> and <code>&quot;bacab&quot;</code>.</li>
	<li>Lexicographically, <code>&quot;abcba&quot;</code> comes before <code>&quot;bacab&quot;</code>. Since <code>k = 1</code>, the output is <code>&quot;abcba&quot;</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
	<li><code>s</code> is guaranteed to be palindromic.</li>
	<li><code>1 &lt;= k &lt;= 10<sup>6</sup></code></li>
</ul>


## Hints

1. Only build `floor(n / 2)` characters (the rest are determined by symmetry).

2. Count character frequencies and use half the counts for construction.

3. Incrementally choose each character (from smallest to largest) and calculate how many valid arrangements result if that character is chosen at the current index.

4. If the count is at least `k`, fix that character; otherwise, subtract the count from `k` and try the next candidate.

5. Use combinatorics to compute the number of permutations at each step.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

A palindromic string of length $n$ is determined by its first $m = \lfloor n/2 \rfloor$ characters. Since the string $s$ is already palindromic, we calculate the character frequencies in $s$ and halve them to get the counts for the first half of any palindromic rearrangement. If $n$ is odd, the character with an odd frequency remains as the central character. The problem is then reduced to finding the $k$-th lexicographical permutation of the multiset of characters forming the first half.

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
    long long combinations(int n, int r, long long limit) {
        if (r < 0 || r > n) return 0;
        if (r == 0 || r == n) return 1;
        if (r > n / 2) r = n - r;
        long long res = 1;
        for (int i = 1; i <= r; ++i) {
            res = res * (n - i + 1) / i;
            if (res > limit) return limit + 1;
        }
        return res;
    }

    long long count_perms(const vector<int>& counts, int total, long long limit) {
        long long res = 1;
        int curr_total = total;
        for (int c : counts) {
            if (c > 0) {
                long long comb_val = combinations(curr_total, c, limit);
                res *= comb_val;
                if (res > limit) return limit + 1;
                curr_total -= c;
            }
        }
        return res;
    }

    string smallestPalindrome(string s, int k) {
        int n = s.length();
        vector<int> counts(26, 0);
        for (char c : s) counts[c - 'a']++;

        vector<int> half_counts(26, 0);
        string mid = "";
        for (int i = 0; i < 26; ++i) {
            if (counts[i] % 2 != 0) mid = (char)('a' + i);
            half_counts[i] = counts[i] / 2;
        }

        int m = n / 2;
        if (count_perms(half_counts, m, (long long)k) < (long long)k) return "";

        string first_half = "";
        long long current_k = k;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < 26; ++j) {
                if (half_counts[j] > 0) {
                    half_counts[j]--;
                    long long p = count_perms(half_counts, m - 1 - i, current_k);
                    if (p >= current_k) {
                        first_half += (char)('a' + j);
                        break;
                    } else {
                        current_k -= p;
                        half_counts[j]++;
                    }
                }
            }
        }

        string second_half = first_half;
        reverse(second_half.begin(), second_half.end());
        return first_half + mid + second_half;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.*;

class Solution {
    public String smallestPalindrome(String s, int k) {
        int n = s.length();
        int[] counts = new int[26];
        for (char c : s.toCharArray()) {
            counts[c - 'a']++;
        }

        int[] halfCounts = new int[26];
        String mid = "";
        for (int i = 0; i < 26; i++) {
            if (counts[i] % 2 != 0) {
                mid = String.valueOf((char) ('a' + i));
            }
            halfCounts[i] = counts[i] / 2;
        }

        int m = n / 2;
        long totalPerms = countPerms(halfCounts, m, (long) k);
        if (totalPerms < k) return "";

        StringBuilder firstHalf = new StringBuilder();
        long currentK = k;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < 26; j++) {
                if (halfCounts[j] > 0) {
                    halfCounts[j]--;
                    long p = countPerms(halfCounts, m - 1 - i, currentK);
                    if (p >= currentK) {
                        firstHalf.append((char) ('a' + j));
                        break;
                    } else {
                        currentK -= p;
                        halfCounts[j]++;
                    }
                }
            }
        }

        String fh = firstHalf.toString();
        String sh = new StringBuilder(fh).reverse().toString();
        return fh + mid + sh;
    }

    private long combinations(int n, int r, long limit) {
        if (r < 0 || r > n) return 0;
        if (r == 0 || r == n) return 1;
        if (r > n / 2) r = n - r;
        long res = 1;
        for (int i = 1; i <= r; i++) {
            res = res * (n - i + 1) / i;
            if (res > limit) return limit + 1;
        }
        return res;
    }

    private long countPerms(int[] counts, int total, long limit) {
        long res = 1;
        int currTotal = total;
        for (int c : counts) {
            if (c > 0) {
                long combVal = combinations(currTotal, c, limit);
                res *= combVal;
                if (res > limit) return limit + 1;
                currTotal -= c;
            }
        }
        return res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def smallestPalindrome(self, s, k):
        n = len(s)
        counts = [0] * 26
        for char in s:
            counts[ord(char) - ord('a')] += 1

        half_counts = [0] * 26
        mid_char = ""
        for i in range(26):
            if counts[i] % 2 != 0:
                mid_char = chr(ord('a') + i)
            half_counts[i] = counts[i] // 2

        m = n // 2

        def combinations(n_val, r_val, limit):
            if r_val < 0 or r_val > n_val: return 0
            if r_val == 0 or r_val == n_val: return 1
            if r_val > n_val // 2: r_val = n_val - r_val
            res = 1
            for i in range(1, r_val + 1):
                res = res * (n_val - i + 1) // i
                if res > limit: return limit + 1
            return res

        def count_perms(cnts, total, limit):
            res = 1
            curr_total = total
            for c in cnts:
                if c > 0:
                    comb_val = combinations(curr_total, c, limit)
                    res *= comb_val
                    if res > limit: return limit + 1
                    curr_total -= c
            return res

        if count_perms(half_counts, m, k) < k:
            return ""

        res_half = []
        curr_k = k
        for i in range(m):
            for j in range(26):
                if half_counts[j] > 0:
                    half_counts[j] -= 1
                    p = count_perms(half_counts, m - 1 - i, curr_k)
                    if p >= curr_k:
                        res_half.append(chr(ord('a') + j))
                        break
                    else:
                        curr_k -= p
                        half_counts[j] += 1

        first_half_str = "".join(res_half)
        return first_half_str + mid_char + first_half_str[::-1]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1

        half_freq = [0] * 26
        mid = ""
        for i in range(26):
            if freq[i] % 2 == 1:
                mid = chr(ord('a') + i)
            half_freq[i] = freq[i] // 2

        h = n // 2

        def count_perms(total_len, counts, limit):
            res = 1
            curr_n = total_len
            for c in counts:
                if c > 0:
                    for i in range(1, c + 1):
                        res = (res * curr_n) // i
                        curr_n -= 1
                        if res > limit:
                            return limit + 1
            return res

        if count_perms(h, half_freq, k) < k:
            return ""

        res_half = []
        current_k = k
        for i in range(h):
            for j in range(26):
                if half_freq[j] > 0:
                    half_freq[j] -= 1
                    cnt = count_perms(h - 1 - i, half_freq, current_k)
                    if cnt >= current_k:
                        res_half.append(chr(ord('a') + j))
                        break
                    else:
                        current_k -= cnt
                        half_freq[j] += 1

        first_half = "".join(res_half)
        return first_half + mid + first_half[::-1]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

long long countPerms(int totalLen, int* counts, long long limit) {
    long long res = 1;
    int n = totalLen;
    for (int j = 0; j < 26; j++) {
        for (int i = 1; i <= counts[j]; i++) {
            res = res * n / i;
            n--;
            if (res > limit) return limit + 1;
        }
    }
    return res;
}

char* smallestPalindrome(char* s, int k) {
    int n = strlen(s);
    int freq[26] = {0};
    for (int i = 0; i < n; i++) {
        freq[s[i] - 'a']++;
    }

    int half_freq[26] = {0};
    char mid = '\0';
    for (int i = 0; i < 26; i++) {
        if (freq[i] % 2 == 1) {
            mid = (char)('a' + i);
        }
        half_freq[i] = freq[i] / 2;
    }

    int h = n / 2;
    if (countPerms(h, half_freq, (long long)k) < (long long)k) {
        char* empty = (char*)malloc(1);
        empty[0] = '\0';
        return empty;
    }

    char* resHalf = (char*)malloc(h + 1);
    long long currentK = k;
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < 26; j++) {
            if (half_freq[j] > 0) {
                half_freq[j]--;
                long long cnt = countPerms(h - 1 - i, half_freq, currentK);
                if (cnt >= currentK) {
                    resHalf[i] = (char)('a' + j);
                    break;
                } else {
                    currentK -= cnt;
                    half_freq[j]++;
                }
            }
        }
    }
    resHalf[h] = '\0';

    char* result = (char*)malloc(n + 1);
    for (int i = 0; i < h; i++) {
        result[i] = resHalf[i];
        result[n - 1 - i] = resHalf[i];
    }
    if (n % 2 == 1) {
        result[h] = mid;
    }
    result[n] = '\0';
    free(resHalf);
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Collections.Generic;
using System.Text;

public class Solution {
    public string SmallestPalindrome(string s, int k) {
        int n = s.Length;
        int[] freq = new int[26];
        for (int i = 0; i < n; i++) {
            freq[s[i] - 'a']++;
        }

        int[] halfFreq = new int[26];
        char mid = '\0';
        for (int i = 0; i < 26; i++) {
            if (freq[i] % 2 == 1) {
                mid = (char)('a' + i);
            }
            halfFreq[i] = freq[i] / 2;
        }

        int h = n / 2;
        if (CountPerms(h, halfFreq, k) < k) {
            return "";
        }

        char[] resHalf = new char[h];
        long currentK = k;
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < 26; j++) {
                if (halfFreq[j] > 0) {
                    halfFreq[j]--;
                    long cnt = CountPerms(h - 1 - i, halfFreq, currentK);
                    if (cnt >= currentK) {
                        resHalf[i] = (char)('a' + j);
                        break;
                    } else {
                        currentK -= cnt;
                        halfFreq[j]++;
                    }
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        sb.Append(resHalf);
        if (n % 2 == 1) {
            sb.Append(mid);
        }
        for (int i = h - 1; i >= 0; i--) {
            sb.Append(resHalf[i]);
        }
        return sb.ToString();
    }

    private long CountPerms(int totalLen, int[] counts, long limit) {
        long res = 1;
        int n = totalLen;
        for (int j = 0; j < 26; j++) {
            for (int i = 1; i <= counts[j]; i++) {
                res = res * n / i;
                n--;
                if (res > limit) return limit + 1;
            }
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
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var smallestPalindrome = function(s, k) {
    let n = s.length;
    let freq = new Array(26).fill(0);
    for (let i = 0; i < n; i++) {
        freq[s.charCodeAt(i) - 97]++;
    }

    let half_freq = new Array(26).fill(0);
    let mid = "";
    for (let i = 0; i < 26; i++) {
        if (freq[i] % 2 === 1) {
            mid = String.fromCharCode(97 + i);
        }
        half_freq[i] = Math.floor(freq[i] / 2);
    }

    let h = Math.floor(n / 2);

    function countPerms(totalLen, counts, limit) {
        let res = 1;
        let currentN = totalLen;
        for (let j = 0; j < 26; j++) {
            for (let i = 1; i <= counts[j]; i++) {
                res = (res * currentN) / i;
                currentN--;
                if (res > limit) return limit + 1;
            }
        }
        return res;
    }

    if (countPerms(h, half_freq, k) < k) {
        return "";
    }

    let resHalf = [];
    let currentK = k;
    for (let i = 0; i < h; i++) {
        for (let j = 0; j < 26; j++) {
            if (half_freq[j] > 0) {
                half_freq[j]--;
                let cnt = countPerms(h - 1 - i, half_freq, currentK);
                if (cnt >= currentK) {
                    resHalf.push(String.fromCharCode(97 + j));
                    break;
                } else {
                    currentK -= cnt;
                    half_freq[j]++;
                }
            }
        }
    }

    let firstHalf = resHalf.join('');
    let secondHalf = resHalf.slice().reverse().join('');
    return firstHalf + mid + secondHalf;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function smallestPalindrome(s: string, k: number): string {
    const n = s.length;
    const counts = new Array(26).fill(0);
    for (let i = 0; i < n; i++) {
        counts[s.charCodeAt(i) - 97]++;
    }

    const halfCounts = new Array(26).fill(0);
    let midChar = "";
    for (let i = 0; i < 26; i++) {
        if (counts[i] % 2 !== 0) {
            midChar = String.fromCharCode(i + 97);
        }
        halfCounts[i] = Math.floor(counts[i] / 2);
    }

    const halfLen = Math.floor(n / 2);
    const limit = k + 1;

    function countPermutations(L: number, cArr: number[], lim: number): number {
        if (L === 0) return 1;
        let res = 1;
        let remL = L;
        for (let i = 0; i < 26; i++) {
            let c = cArr[i];
            if (c === 0) continue;
            let charWays = 1;
            for (let j = 1; j <= c; j++) {
                charWays = Math.floor((charWays * remL) / j);
                remL--;
                if (charWays >= lim) {
                    charWays = lim;
                    break;
                }
            }
            res *= charWays;
            if (res >= lim) return lim;
        }
        return res;
    }

    if (countPermutations(halfLen, halfCounts, limit) < k) {
        return "";
    }

    let firstHalf = "";
    const currentHalfCounts = [...halfCounts];
    for (let i = 0; i < halfLen; i++) {
        for (let j = 0; j < 26; j++) {
            if (currentHalfCounts[j] > 0) {
                currentHalfCounts[j]--;
                const ways = countPermutations(halfLen - 1 - i, currentHalfCounts, limit);
                if (ways >= k) {
                    firstHalf += String.fromCharCode(j + 97);
                    break;
                } else {
                    k -= ways;
                    currentHalfCounts[j]++;
                }
            }
        }
    }

    const secondHalf = firstHalf.split("").reverse().join("");
    return firstHalf + midChar + secondHalf;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return String
     */
    function smallestPalindrome($s, $k) {
        $n = strlen($s);
        $counts = array_fill(0, 26, 0);
        for ($i = 0; $i < $n; $i++) {
            $counts[ord($s[$i]) - 97]++;
        }

        $halfCounts = array_fill(0, 26, 0);
        $midChar = "";
        for ($i = 0; $i < 26; $i++) {
            if ($counts[$i] % 2 !== 0) {
                $midChar = chr($i + 97);
            }
            $halfCounts[$i] = (int)($counts[$i] / 2);
        }

        $halfLen = (int)($n / 2);
        $limit = $k + 1;

        if ($this->countPermutations($halfLen, $halfCounts, $limit) < $k) {
            return "";
        }

        $firstHalf = "";
        $currentHalfCounts = $halfCounts;
        for ($i = 0; $i < $halfLen; $i++) {
            for ($j = 0; $j < 26; $j++) {
                if ($currentHalfCounts[$j] > 0) {
                    $currentHalfCounts[$j]--;
                    $ways = $this->countPermutations($halfLen - 1 - $i, $currentHalfCounts, $limit);
                    if ($ways >= $k) {
                        $firstHalf .= chr($j + 97);
                        break;
                    } else {
                        $k -= $ways;
                        $currentHalfCounts[$j]++;
                    }
                }
            }
        }

        return $firstHalf . $midChar . strrev($firstHalf);
    }

    private function countPermutations($L, $cArr, $lim) {
        if ($L === 0) return 1;
        $res = 1;
        $remL = $L;
        for ($i = 0; $i < 26; $i++) {
            $c = $cArr[$i];
            if ($c === 0) continue;
            $charWays = 1;
            for ($j = 1; $j <= $c; $j++) {
                $charWays = (int)(($charWays * $remL) / $j);
                $remL--;
                if ($charWays >= $lim) {
                    $charWays = $lim;
                    break;
                }
            }
            $res *= $charWays;
            if ($res >= $lim) return $lim;
        }
        return $res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func smallestPalindrome(_ s: String, _ k: Int) -> String {
        let n = s.count
        var counts = [Int](repeating: 0, count: 26)
        let aValue = Int(UnicodeScalar("a").value)

        for char in s.unicodeScalars {
            counts[Int(char.value) - aValue] += 1
        }

        var halfCounts = [Int](repeating: 0, count: 26)
        var midChar = ""
        for i in 0..<26 {
            if counts[i] % 2 != 0 {
                midChar = String(UnicodeScalar(aValue + i)!)
            }
            halfCounts[i] = counts[i] / 2
        }

        let halfLen = n / 2
        let limit = k + 1
        var currentK = k

        if countPermutations(halfLen, halfCounts, limit) < currentK {
            return ""
        }

        var firstHalf = ""
        var currentHalfCounts = halfCounts

        for i in 0..<halfLen {
            for j in 0..<26 {
                if currentHalfCounts[j] > 0 {
                    currentHalfCounts[j] -= 1
                    let ways = countPermutations(halfLen - 1 - i, currentHalfCounts, limit)
                    if ways >= currentK {
                        firstHalf.append(Character(UnicodeScalar(aValue + j)!))
                        break
                    } else {
                        currentK -= ways
                        currentHalfCounts[j] += 1
                    }
                }
            }
        }

        return firstHalf + midChar + String(firstHalf.reversed())
    }

    private func countPermutations(_ L: Int, _ cArr: [Int], _ lim: Int) -> Int {
        if L == 0 { return 1 }
        var res = 1
        var remL = L
        for i in 0..<26 {
            let c = cArr[i]
            if c == 0 { continue }
            var charWays = 1
            for j in 1...c {
                charWays = (charWays * remL) / j
                remL -= 1
                if charWays >= lim {
                    charWays = lim
                    break
                }
            }
            res *= charWays
            if res >= lim { return lim }
        }
        return res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun smallestPalindrome(s: String, k: Int): String {
        val n = s.length
        val counts = IntArray(26)
        for (char in s) {
            counts[char - 'a']++
        }

        val halfCounts = IntArray(26)
        var midChar = ""
        for (i in 0 until 26) {
            if (counts[i] % 2 != 0) {
                midChar = (i + 'a'.toInt()).toChar().toString()
            }
            halfCounts[i] = counts[i] / 2
        }

        val halfLen = n / 2
        val limit = k + 1
        var currentK = k

        if (countPermutations(halfLen, halfCounts, limit) < currentK) {
            return ""
        }

        val firstHalf = StringBuilder()
        val currentHalfCounts = halfCounts.copyOf()
        for (i in 0 until halfLen) {
            for (j in 0 until 26) {
                if (currentHalfCounts[j] > 0) {
                    currentHalfCounts[j]--
                    val ways = countPermutations(halfLen - 1 - i, currentHalfCounts, limit)
                    if (ways >= currentK) {
                        firstHalf.append((j + 'a'.toInt()).toChar())
                        break
                    } else {
                        currentK -= ways
                        currentHalfCounts[j]++
                    }
                }
            }
        }

        val firstHalfStr = firstHalf.toString()
        return firstHalfStr + midChar + firstHalfStr.reversed()
    }

    private fun countPermutations(L: Int, cArr: IntArray, lim: Int): Int {
        if (L == 0) return 1
        var res: Long = 1
        var remL = L
        val limitLong = lim.toLong()
        for (i in 0 until 26) {
            val c = cArr[i]
            if (c == 0) continue
            var charWays: Long = 1
            for (j in 1..c) {
                charWays = (charWays * remL) / j
                remL--
                if (charWays >= limitLong) {
                    charWays = limitLong
                    break
                }
            }
            res *= charWays
            if (res >= limitLong) return limitLong.toInt()
        }
        return res.toInt()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  String smallestPalindrome(String s, int k) {
    int n = s.length;
    List<int> charCounts = List.filled(26, 0);
    for (int i = 0; i < n; i++) {
      charCounts[s.codeUnitAt(i) - 97]++;
    }

    List<int> halfCounts = List.filled(26, 0);
    String midChar = "";
    for (int i = 0; i < 26; i++) {
      halfCounts[i] = charCounts[i] ~/ 2;
      if (charCounts[i] % 2 != 0) {
        midChar = String.fromCharCode(97 + i);
      }
    }

    int L = n ~/ 2;
    int limit = 1000000000000000;
    int totalPossible = 1;
    int currL = 0;
    for (int i = 0; i < 26; i++) {
      for (int j = 1; j <= halfCounts[i]; j++) {
        currL++;
        if (totalPossible >= limit) {
          totalPossible = limit;
        } else {
          totalPossible = (totalPossible * currL) ~/ j;
          if (totalPossible > limit) totalPossible = limit;
        }
      }
    }
    if (totalPossible > limit) totalPossible = limit;

    if (k > totalPossible) return "";

    int kLong = k;
    List<int> firstHalfCodes = [];
    int currentTotal = totalPossible;

    for (int i = 0; i < L; i++) {
      int remLen = L - i;
      for (int j = 0; j < 26; j++) {
        if (halfCounts[j] > 0) {
          int wj = (currentTotal >= limit)
              ? limit
              : (currentTotal * halfCounts[j]) ~/ remLen;
          if (kLong <= wj) {
            firstHalfCodes.add(97 + j);
            halfCounts[j]--;
            currentTotal = wj;
            break;
          } else {
            kLong -= wj;
          }
        }
      }
    }

    List<int> resCodes = List.filled(n, 0);
    for (int i = 0; i < L; i++) {
      resCodes[i] = firstHalfCodes[i];
      resCodes[n - 1 - i] = firstHalfCodes[i];
    }
    if (n % 2 != 0) {
      resCodes[L] = midChar.codeUnitAt(0);
    }
    return String.fromCharCodes(resCodes);
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func smallestPalindrome(s string, k int) string {
	n := len(s)
	charCounts := make([]int, 26)
	for i := 0; i < n; i++ {
		charCounts[s[i]-'a']++
	}

	halfCounts := make([]int, 26)
	var midChar byte
	hasMid := false
	for i := 0; i < 26; i++ {
		halfCounts[i] = charCounts[i] / 2
		if charCounts[i]%2 != 0 {
			midChar = byte('a' + i)
			hasMid = true
		}
	}

	L := n / 2
	limit := int64(1000000000000000)
	var totalPossible int64 = 1
	currL := 0
	for i := 0; i < 26; i++ {
		for j := 1; j <= halfCounts[i]; j++ {
			currL++
			if totalPossible >= limit {
				totalPossible = limit
			} else {
				totalPossible = (totalPossible * int64(currL)) / int64(j)
				if totalPossible > limit {
					totalPossible = limit
				}
			}
		}
	}

	if int64(k) > totalPossible {
		return ""
	}

	k64 := int64(k)
	firstHalf := make([]byte, L)
	currentTotal := totalPossible

	for i := 0; i < L; i++ {
		remLen := L - i
		for j := 0; j < 26; j++ {
			if halfCounts[j] > 0 {
				var wj int64
				if currentTotal >= limit {
					wj = limit
				} else {
					wj = (currentTotal * int64(halfCounts[j])) / int64(remLen)
				}
				if k64 <= wj {
					firstHalf[i] = byte('a' + j)
					halfCounts[j]--
					currentTotal = wj
					break
				} else {
					k64 -= wj
				}
			}
		}
	}

	res := make([]byte, n)
	for i := 0; i < L; i++ {
		res[i] = firstHalf[i]
		res[n-1-i] = firstHalf[i]
	}
	if hasMid {
		res[L] = midChar
	}
	return string(res)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @param {Integer} k
# @return {String}
def smallest_palindrome(s, k)
  n = s.length
  char_counts = Array.new(26, 0)
  s.each_char { |c| char_counts[c.ord - 'a'.ord] += 1 }

  half_counts = Array.new(26, 0)
  mid_char = ""
  char_counts.each_with_index do |count, i|
    half_counts[i] = count / 2
    mid_char = ('a'.ord + i).chr if count.odd?
  end

  l_len = n / 2
  limit = 10**15
  total_possible = 1
  curr_l = 0
  half_counts.each do |count|
    (1..count).each do |j|
      curr_l += 1
      if total_possible >= limit
        total_possible = limit
      else
        total_possible = (total_possible * curr_l) / j
        total_possible = limit if total_possible > limit
      end
    end
  end

  return "" if k > total_possible

  first_half = ""
  current_total = total_possible
  l_len.times do |i|
    rem_len = l_len - i
    26.times do |j|
      if half_counts[j] > 0
        w_j = current_total >= limit ? limit : (current_total * half_counts[j]) / rem_len
        if k <= w_j
          first_half << ('a'.ord + j).chr
          half_counts[j] -= 1
          current_total = w_j
          break
        else
          k -= w_j
        end
      end
    end
  end

  first_half + mid_char + first_half.reverse
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def smallestPalindrome(s: String, k: Int): String = {
    val n = s.length
    val charCounts = new Array[Int](26)
    for (c <- s) {
      charCounts(c - 'a') += 1
    }

    val halfCounts = new Array[Int](26)
    var midChar = ""
    for (i <- 0 until 26) {
      halfCounts(i) = charCounts(i) / 2
      if (charCounts(i) % 2 != 0) {
        midChar = ('a' + i).toChar.toString
      }
    }

    val L = n / 2
    val limit = 1000000000000000L
    var totalPossible = 1L
    var currL = 0
    for (i <- 0 until 26) {
      for (j <- 1 to halfCounts(i)) {
        currL += 1
        if (totalPossible >= limit) {
          totalPossible = limit
        } else {
          totalPossible = (totalPossible * currL) / j
          if (totalPossible > limit) totalPossible = limit
        }
      }
    }

    if (k.toLong > totalPossible) return ""

    var kLong = k.toLong
    val firstHalf = new StringBuilder()
    var currentTotal = totalPossible

    for (i <- 0 until L) {
      val remLen = L - i
      var found = false
      var j = 0
      while (j < 26 && !found) {
        if (halfCounts(j) > 0) {
          val wj = if (currentTotal >= limit) limit else (currentTotal * halfCounts(j)) / remLen
          if (kLong <= wj) {
            firstHalf.append(('a' + j).toChar)
            halfCounts(j) -= 1
            currentTotal = wj
            found = true
          } else {
            kLong -= wj
          }
        }
        j += 1
      }
    }

    val firstHalfStr = firstHalf.toString()
    firstHalfStr + midChar + firstHalfStr.reverse
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn smallest_palindrome(s: String, k: i32) -> String {
        let n = s.len();
        let mut freq = [0; 26];
        for b in s.bytes() {
            freq[(b - b'a') as usize] += 1;
        }
        let mut half_freq = [0; 26];
        let mut mid_char = None;
        for i in 0..26 {
            half_freq[i] = freq[i] / 2;
            if freq[i] % 2 == 1 {
                mid_char = Some((b'a' + i as u8) as char);
            }
        }
        let half_len = n / 2;
        let k_u64 = k as u64;
        let limit = k_u64 * 10001 + 7;
        let mut w_total = Self::calculate_ways(&half_freq, limit);
        if w_total < k_u64 {
            return "".to_string();
        }
        let mut res = Vec::new();
        let mut current_k = k_u64;
        let mut total_rem = half_len as u64;
        for _ in 0..half_len {
            for c in 0..26 {
                if half_freq[c] > 0 {
                    let w_c = if w_total >= limit {
                        limit
                    } else {
                        (w_total * half_freq[c] as u64) / total_rem
                    };
                    if w_c >= current_k {
                        res.push((b'a' + c as u8) as char);
                        half_freq[c] -= 1;
                        w_total = w_c;
                        total_rem -= 1;
                        break;
                    } else {
                        current_k -= w_c;
                    }
                }
            }
        }
        let first_half: String = res.into_iter().collect();
        let mut result = first_half.clone();
        if let Some(c) = mid_char {
            result.push(c);
        }
        result.push_str(&first_half.chars().rev().collect::<String>());
        result
    }

    fn calculate_ways(counts: &[i32; 26], limit: u64) -> u64 {
        let mut res: u64 = 1;
        let mut current_total: u64 = 0;
        for &count in counts {
            if count == 0 { continue; }
            for j in 1..=(count as u64) {
                let next_res = (res as u128 * (current_total + j) as u128) / j as u128;
                if next_res >= limit as u128 {
                    return limit;
                } else {
                    res = next_res as u64;
                }
            }
            current_total += count as u64;
        }
        res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (smallest-palindrome s k)
  (-> string? exact-integer? string?)
  (let* ([n (string-length s)]
         [freq (make-vector 26 0)])
    (for ([c (in-string s)])
      (let ([idx (- (char->integer c) 97)])
        (vector-set! freq idx (+ (vector-ref freq idx) 1))))
    (let* ([half-freq (make-vector 26 0)]
           [mid-char ""])
      (for ([i (in-range 26)])
        (vector-set! half-freq i (quotient (vector-ref freq i) 2))
        (when (= (remainder (vector-ref freq i) 2) 1)
          (set! mid-char (string (integer->char (+ 97 i))))))
      (let* ([half-len (quotient n 2)]
             [limit (+ (* k 10001) 7)]
             [calculate-ways
              (lambda (counts limit)
                (let loop-counts ([idx 0] [current-rem 0] [res 1])
                  (if (= idx 26)
                      res
                      (let ([cnt (vector-ref counts idx)])
                        (if (= cnt 0)
                            (loop-counts (+ idx 1) current-rem res)
                            (let loop-j ([j 1] [j-res res] [j-rem current-rem])
                              (if (> j cnt)
                                  (loop-counts (+ idx 1) j-rem j-res)
                                  (let ([next-res (quotient (* j-res (+ j-rem 1)) j)])
                                    (if (>= next-res limit)
                                        limit
                                        (loop-j (+ j 1) next-res (+ j-rem 1)))))))))))]
             [w-total (calculate-ways half-freq limit)])
        (if (< w-total k)
            ""
            (let* ([res-indices '()]
                   [curr-k k]
                   [curr-w-total w-total]
                   [total-rem half-len])
              (for ([i (in-range half-len)])
                (let ([found #f])
                  (for ([c (in-range 26)] #:break found)
                    (let ([count (vector-ref half-freq c)])
                      (when (> count 0)
                        (let ([w-c (if (>= curr-w-total limit)
                                       limit
                                       (quotient (* curr-w-total count) total-rem))])
                          (if (>= w-c curr-k)
                              (begin
                                (set! res-indices (cons c res-indices))
                                (vector-set! half-freq c (- count 1))
                                (set! curr-w-total w-c)
                                (set! total-rem (- total-rem 1))
                                (set! found #t))
                              (set! curr-k (- curr-k w-c))))))))
              (let* ([first-half-list (map (lambda (c) (integer->char (+ 97 c))) (reverse res-indices))]
                     [first-half (list->string first-half-list)]
                     [second-half (list->string (reverse first-half-list))])
                (string-append first-half mid-char second-half))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec smallest_palindrome(S :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
smallest_palindrome(S, K) ->
    N = byte_size(S),
    Freqs = lists:foldl(fun(C, Acc) ->
        Idx = C - $a + 1,
        setelement(Idx, Acc, element(Idx, Acc) + 1)
    end, {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}, binary_to_list(S)),
    {HalfFreq, MidChar} = lists:foldl(fun(I, {H, M}) ->
        F = element(I, Freqs),
        NH = setelement(I, H, F div 2),
        NM = if F rem 2 == 1 -> [I + $a - 1 | M]; true -> M end,
        {NH, NM}
    end, {{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}, []}, lists:seq(1, 26)),
    HalfLen = N div 2,
    Limit = K * 10001 + 7,
    WTotal = calculate_ways(HalfFreq, Limit),
    if
        WTotal < K -> <<"">>;
        true ->
            {ResCodes, _, _, _} = lists:foldl(fun(_, {Acc, CurrK, CurrWTotal, TotalRem, HF}) ->
                {NewAcc, NewK, NewW, NewRem, NewHF} = find_char(1, Acc, CurrK, CurrWTotal, TotalRem, HF, Limit),
                {NewAcc, NewK, NewW, NewRem, NewHF}
            end, {[], K, WTotal, HalfLen, HalfFreq}, lists:seq(1, HalfLen)),
            FirstHalf = lists:reverse(ResCodes),
            unicode:characters_to_binary(FirstHalf ++ MidChar ++ lists:reverse(FirstHalf))
    end.

find_char(C, Acc, K, WTotal, TotalRem, HF, Limit) ->
    Count = element(C, HF),
    if
        Count > 0 ->
            WC = if WTotal >= Limit -> Limit; true -> (WTotal * Count) div TotalRem end,
            if
                WC >= K ->
                    { [C + $a - 1 | Acc], K, WC, TotalRem - 1, setelement(C, HF, Count - 1) };
                true ->
                    find_char(C + 1, Acc, K - WC, WTotal, TotalRem, HF, Limit)
            end;
        true ->
            find_char(C + 1, Acc, K, WTotal, TotalRem, HF, Limit)
    end.

calculate_ways(HF, Limit) ->
    HFList = tuple_to_list(HF),
    lists:foldl(fun(Count, {Res, CurrentTotal}) ->
        if 
            Count == 0 -> {Res, CurrentTotal};
            true -> 
                {NextRes, NextTotal} = combinations_inner(1, Res, CurrentTotal, Count, Limit),
                {NextRes, NextTotal}
        end
    end, {1, 0}, HFList) |> (fun({R, _}) -> R end).

combinations_inner(J, Res, CurrentTotal, Count, Limit) when J =< Count ->
    NextRes = (Res * (CurrentTotal + J)) div J,
    if
        NextRes >= Limit -> {Limit, CurrentTotal + Count};
        true -> combinations_inner(J + 1, NextRes, CurrentTotal, Count, Limit)
    end;
combinations_inner(_J, Res, CurrentTotal, _Count, _Limit) -> {Res, CurrentTotal}.

'|>' (Val, Fun) -> Fun(Val).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec smallest_palindrome(s :: String.t, k :: integer) :: String.t
  def smallest_palindrome(s, k) do
    n = String.length(s)
    freqs = s |> String.to_charlist() |> Enum.reduce(%{}, fn c, acc -> Map.update(acc, c, 1, &(&1 + 1)) end)

    {half_freq, mid_char} = Enum.reduce(?a..?z, {%{}, ""}, fn c, {hf, mid} ->
      count = Map.get(freqs, c, 0)
      new_hf = Map.put(hf, c, div(count, 2))
      new_mid = if rem(count, 2) == 1, do: <<c>>, else: mid
      {new_hf, new_mid}
    end)

    half_len = div(n, 2)
    limit = k * 10001 + 7
    w_total = calculate_ways(half_freq, limit)

    if w_total < k do
      ""
    else
      {res_chars, _, _, _, _} = Enum.reduce(1..half_len, {[], k, w_total, half_len, half_freq}, fn _, {acc, curr_k, curr_w_total, total_rem, hf} ->
        {char, next_k, next_w, next_rem, next_hf} = find_next_char(?a, curr_k, curr_w_total, total_rem, hf, limit)
        {[char | acc], next_k, next_w, next_rem, next_hf}
      end)

      first_half = res_chars |> Enum.reverse() |> List.to_string()
      first_half <> mid_char <> String.reverse(first_half)
    end
  end

  defp find_next_char(c, k, w_total, total_rem, hf, limit) do
    count = Map.get(hf, c, 0)
    if count > 0 do
      w_c = if w_total >= limit, do: limit, else: div(w_total * count, total_rem)
      if w_c >= k do
        {c, k, w_c, total_rem - 1, Map.put(hf, c, count - 1)}
      else
        find_next_char(c + 1, k - w_c, w_total, total_rem, hf, limit)
      end
    else
      find_next_char(c + 1, k, w_total, total_rem, hf, limit)
    end
  end

  defp calculate_ways(hf, limit) do
    {res, _} = Enum.reduce(?a..?z, {1, 0}, fn c, {res, current_total} ->
      count = Map.get(hf, c, 0)
      if count == 0 do
        {res, current_total}
      else
        Enum.reduce_while(1..count, {res, current_total}, fn j, {r, t} ->
          next_res = div(r * (t + j), j)
          if next_res >= limit do
            {:halt, {limit, t + count}}
          else
            {:cont, {next_res, t + j}}
          end
        end)
      end
    end)
    res
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N · |Σ|^2) where $N$ is the length of the string and $|Σ| = 26$. For each of the $N/2$ positions in the first half, we iterate through the alphabet. For each candidate, we compute the multinomial coefficient for the remaining characters, which is capped at $k$. The combinatorics calculations exit early due to this cap, ensuring efficient processing.
- **Space Complexity:** O(N) to store the character counts, the constructed first-half string, and the final palindromic result string.
