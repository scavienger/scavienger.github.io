---
layout: post
title: "Lexicographically Smallest Palindromic Permutation Greater Than Target"
date: 2026-08-28 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Two Pointers", "String", "Enumeration"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    string lexPalindromicPermutation(string s,\
        \ string target) {\n        int n = s.length();\n        vector<int> counts(26,\
        \ 0);\n        for (char c : s) counts[c - 'a']++;\n\n        int odd_count\
        \ = 0;\n        char mid_char = '\\0';\n        for (int i = 0; i < 26; ++i)\
        \ {\n            if (counts[i] % 2 != 0) {\n                odd_count++;\n \
        \               mid_char = (char)('a' + i);\n            }\n        }\n\n  \
        \      if (odd_count != (n % 2)) return \"\";\n\n        vector<int> half_counts(26);\n\
        \        for (int i = 0; i < 26; ++i) half_counts[i] = counts[i] / 2;\n\n  \
        \      int half_len = n / 2;\n        string mid_str = (mid_char == '\\0') ?\
        \ \"\" : string(1, mid_char);\n\n        // Try Match candidate\n        vector<int>\
        \ temp_counts = half_counts;\n        string H = \"\";\n        bool possible\
        \ = true;\n        for (int i = 0; i < half_len; ++i) {\n            int idx\
        \ = target[i] - 'a';\n            if (temp_counts[idx] > 0) {\n            \
        \    temp_counts[idx]--;\n                H += target[i];\n            } else\
        \ {\n                possible = false;\n                break;\n           \
        \ }\n        }\n\n        if (possible) {\n            string h_rev = H;\n \
        \           reverse(h_rev.begin(), h_rev.end());\n            string P = H +\
        \ mid_str + h_rev;\n            if (P > target) return P;\n        }\n\n   \
        \     // Try Diverge candidate\n        vector<bool> can_form_prefix(half_len\
        \ + 1, false);\n        can_form_prefix[0] = true;\n        temp_counts = half_counts;\n\
        \        for (int i = 1; i <= half_len; ++i) {\n            int idx = target[i\
        \ - 1] - 'a';\n            if (temp_counts[idx] > 0) {\n                temp_counts[idx]--;\n\
        \                can_form_prefix[i] = true;\n            } else break;\n   \
        \     }\n\n        for (int i = half_len - 1; i >= 0; --i) {\n            if\
        \ (!can_form_prefix[i]) continue;\n            temp_counts = half_counts;\n\
        \            for (int j = 0; j < i; ++j) temp_counts[target[j] - 'a']--;\n\n\
        \            for (int c_idx = (target[i] - 'a') + 1; c_idx < 26; ++c_idx) {\n\
        \                if (temp_counts[c_idx] > 0) {\n                    string res_H\
        \ = target.substr(0, i);\n                    res_H += (char)('a' + c_idx);\n\
        \                    temp_counts[c_idx]--;\n                    for (int k =\
        \ 0; k < 26; ++k) {\n                        while (temp_counts[k] > 0) {\n\
        \                            res_H += (char)('a' + k);\n                   \
        \         temp_counts[k]--;\n                        }\n                   \
        \ }\n                    string h_rev = res_H;\n                    reverse(h_rev.begin(),\
        \ h_rev.end());\n                    return res_H + mid_str + h_rev;\n     \
        \           }\n            }\n        }\n\n        return \"\";\n    }\n};"
      java: "class Solution {\n    public String lexPalindromicPermutation(String s,\
        \ String target) {\n        int n = s.length();\n        int[] counts = new\
        \ int[26];\n        for (char c : s.toCharArray()) counts[c - 'a']++;\n\n  \
        \      int oddCount = 0;\n        char midChar = '\\0';\n        for (int i\
        \ = 0; i < 26; i++) {\n            if (counts[i] % 2 != 0) {\n             \
        \   oddCount++;\n                midChar = (char) ('a' + i);\n            }\n\
        \        }\n\n        if (oddCount != (n % 2)) return \"\";\n\n        int[]\
        \ halfCounts = new int[26];\n        for (int i = 0; i < 26; i++) halfCounts[i]\
        \ = counts[i] / 2;\n\n        int halfLen = n / 2;\n        String midStr =\
        \ (midChar == '\\0') ? \"\" : String.valueOf(midChar);\n\n        // Try Match\
        \ candidate\n        int[] tempCounts = halfCounts.clone();\n        StringBuilder\
        \ hMatch = new StringBuilder();\n        boolean possible = true;\n        for\
        \ (int i = 0; i < halfLen; i++) {\n            int idx = target.charAt(i) -\
        \ 'a';\n            if (tempCounts[idx] > 0) {\n                tempCounts[idx]--;\n\
        \                hMatch.append(target.charAt(i));\n            } else {\n  \
        \              possible = false;\n                break;\n            }\n  \
        \      }\n\n        if (possible) {\n            String H = hMatch.toString();\n\
        \            String hRev = new StringBuilder(H).reverse().toString();\n    \
        \        String P = H + midStr + hRev;\n            if (P.compareTo(target)\
        \ > 0) return P;\n        }\n\n        // Try Diverge candidate\n        boolean[]\
        \ canFormPrefix = new boolean[halfLen + 1];\n        canFormPrefix[0] = true;\n\
        \        tempCounts = halfCounts.clone();\n        for (int i = 1; i <= halfLen;\
        \ i++) {\n            int idx = target.charAt(i - 1) - 'a';\n            if\
        \ (tempCounts[idx] > 0) {\n                tempCounts[idx]--;\n            \
        \    canFormPrefix[i] = true;\n            } else break;\n        }\n\n    \
        \    for (int i = halfLen - 1; i >= 0; i--) {\n            if (!canFormPrefix[i])\
        \ continue;\n            tempCounts = halfCounts.clone();\n            for (int\
        \ j = 0; j < i; j++) tempCounts[target.charAt(j) - 'a']--;\n\n            for\
        \ (int cIdx = (target.charAt(i) - 'a') + 1; cIdx < 26; cIdx++) {\n         \
        \       if (tempCounts[cIdx] > 0) {\n                    StringBuilder resH\
        \ = new StringBuilder(target.substring(0, i));\n                    resH.append((char)\
        \ ('a' + cIdx));\n                    tempCounts[cIdx]--;\n                \
        \    for (int k = 0; k < 26; k++) {\n                        while (tempCounts[k]\
        \ > 0) {\n                            resH.append((char) ('a' + k));\n     \
        \                       tempCounts[k]--;\n                        }\n      \
        \              }\n                    String H = resH.toString();\n        \
        \            String hRev = new StringBuilder(H).reverse().toString();\n    \
        \                return H + midStr + hRev;\n                }\n            }\n\
        \        }\n\n        return \"\";\n    }\n}"
      python: "class Solution(object):\n    def lexPalindromicPermutation(self, s, target):\n\
        \        \"\"\"\n        :type s: str\n        :type target: str\n        :rtype:\
        \ str\n        \"\"\"\n        n = len(s)\n        counts = [0] * 26\n     \
        \   for char in s:\n            counts[ord(char) - ord('a')] += 1\n\n      \
        \  odd_indices = [i for i, count in enumerate(counts) if count % 2 != 0]\n \
        \       if len(odd_indices) != (n % 2):\n            return \"\"\n\n       \
        \ mid_char = chr(ord('a') + odd_indices[0]) if odd_indices else \"\"\n     \
        \   half_counts = [count // 2 for count in counts]\n        half_len = n //\
        \ 2\n\n        # Try Match candidate: prefix matches target[:half_len]\n   \
        \     temp_counts = list(half_counts)\n        h_match = []\n        possible\
        \ = True\n        for i in range(half_len):\n            idx = ord(target[i])\
        \ - ord('a')\n            if temp_counts[idx] > 0:\n                temp_counts[idx]\
        \ -= 1\n                h_match.append(target[i])\n            else:\n     \
        \           possible = False\n                break\n\n        if possible:\n\
        \            h_str = \"\".join(h_match)\n            p_match = h_str + mid_char\
        \ + h_str[::-1]\n            if p_match > target:\n                return p_match\n\
        \n        # Try Diverge candidate: find largest i and smallest c > target[i]\n\
        \        can_form_prefix = [False] * (half_len + 1)\n        can_form_prefix[0]\
        \ = True\n        temp_counts = list(half_counts)\n        for i in range(1,\
        \ half_len + 1):\n            idx = ord(target[i-1]) - ord('a')\n          \
        \  if temp_counts[idx] > 0:\n                temp_counts[idx] -= 1\n       \
        \         can_form_prefix[i] = True\n            else:\n                break\n\
        \n        for i in range(half_len - 1, -1, -1):\n            if not can_form_prefix[i]:\n\
        \                continue\n\n            rem_counts = list(half_counts)\n  \
        \          for j in range(i):\n                rem_counts[ord(target[j]) - ord('a')]\
        \ -= 1\n\n            for c_idx in range(ord(target[i]) - ord('a') + 1, 26):\n\
        \                if rem_counts[c_idx] > 0:\n                    h_diverge =\
        \ list(target[:i])\n                    h_diverge.append(chr(ord('a') + c_idx))\n\
        \                    rem_counts[c_idx] -= 1\n                    for k in range(26):\n\
        \                        while rem_counts[k] > 0:\n                        \
        \    h_diverge.append(chr(ord('a') + k))\n                            rem_counts[k]\
        \ -= 1\n\n                    h_str = \"\".join(h_diverge)\n               \
        \     return h_str + mid_char + h_str[::-1]\n\n        return \"\""
      python3: "class Solution:\n    def lexPalindromicPermutation(self, s: str, target:\
        \ str) -> str:\n        n = len(s)\n        counts = [0] * 26\n        for char\
        \ in s:\n            counts[ord(char) - ord('a')] += 1\n\n        odd_count\
        \ = 0\n        mid_char = \"\"\n        half_counts = [0] * 26\n        for\
        \ i in range(26):\n            if counts[i] % 2 != 0:\n                odd_count\
        \ += 1\n                mid_char = chr(ord('a') + i)\n            half_counts[i]\
        \ = counts[i] // 2\n\n        if odd_count != (n % 2):\n            return \"\
        \"\n\n        m = n // 2\n\n        def can_form(prefix, initial_counts):\n\
        \            rem = initial_counts[:]\n            for char in prefix:\n    \
        \            idx = ord(char) - ord('a')\n                if rem[idx] > 0:\n\
        \                    rem[idx] -= 1\n                else:\n                \
        \    return False, None\n            return True, rem\n\n        can_a, rem_a\
        \ = can_form(target[:m], half_counts)\n        if can_a:\n            h = target[:m]\n\
        \            p1 = h + mid_char + h[::-1]\n            if p1 > target:\n    \
        \            return p1\n\n        for i in range(m - 1, -1, -1):\n         \
        \   can_prefix, rem_counts = can_form(target[:i], half_counts)\n           \
        \ if not can_prefix:\n                continue\n\n            for c_idx in range(ord(target[i])\
        \ - ord('a') + 1, 26):\n                if rem_counts[c_idx] > 0:\n        \
        \            rem_counts[c_idx] -= 1\n                    h_list = list(target[:i])\n\
        \                    h_list.append(chr(ord('a') + c_idx))\n                \
        \    for j in range(26):\n                        h_list.extend([chr(ord('a')\
        \ + j)] * rem_counts[j])\n                    h = \"\".join(h_list)\n      \
        \              return h + mid_char + h[::-1]\n\n        return \"\""
      c: "#include <string.h>\n#include <stdlib.h>\n#include <stdio.h>\n\nchar* lexPalindromicPermutation(char*\
        \ s, char* target) {\n    int n = strlen(s);\n    int counts[26] = {0};\n  \
        \  for (int i = 0; i < n; i++) counts[s[i] - 'a']++;\n\n    int odd_count =\
        \ 0;\n    int mid_idx = -1;\n    int half_counts[26];\n    for (int i = 0; i\
        \ < 26; i++) {\n        if (counts[i] % 2 != 0) {\n            odd_count++;\n\
        \            mid_idx = i;\n        }\n        half_counts[i] = counts[i] / 2;\n\
        \    }\n\n    if (odd_count != (n % 2)) return strdup(\"\");\n\n    int m =\
        \ n / 2;\n    char mid_char = (mid_idx == -1) ? '\\0' : (char)('a' + mid_idx);\n\
        \n    int rem[26];\n    memcpy(rem, half_counts, sizeof(rem));\n    int can_a\
        \ = 1;\n    for (int i = 0; i < m; i++) {\n        int idx = target[i] - 'a';\n\
        \        if (rem[idx] > 0) rem[idx]--;\n        else { can_a = 0; break; }\n\
        \    }\n\n    if (can_a) {\n        char* p1 = (char*)malloc(n + 1);\n     \
        \   for (int i = 0; i < m; i++) p1[i] = target[i];\n        int p_idx = m;\n\
        \        if (n % 2 != 0) p1[p_idx++] = mid_char;\n        for (int i = m - 1;\
        \ i >= 0; i--) p1[p_idx++] = target[i];\n        p1[n] = '\\0';\n        if\
        \ (strcmp(p1, target) > 0) return p1;\n        free(p1);\n    }\n\n    for (int\
        \ i = m - 1; i >= 0; i--) {\n        memcpy(rem, half_counts, sizeof(rem));\n\
        \        int possible = 1;\n        for (int j = 0; j < i; j++) {\n        \
        \    int idx = target[j] - 'a';\n            if (rem[idx] > 0) rem[idx]--;\n\
        \            else { possible = 0; break; }\n        }\n        if (!possible)\
        \ continue;\n\n        for (int c_idx = (target[i] - 'a' + 1); c_idx < 26; c_idx++)\
        \ {\n            if (rem[c_idx] > 0) {\n                char* p2 = (char*)malloc(n\
        \ + 1);\n                for (int j = 0; j < i; j++) p2[j] = target[j];\n  \
        \              p2[i] = (char)('a' + c_idx);\n                rem[c_idx]--;\n\
        \                int p_idx = i + 1;\n                for (int j = 0; j < 26;\
        \ j++) {\n                    while (rem[j] > 0) {\n                       \
        \ p2[p_idx++] = (char)('a' + j);\n                        rem[j]--;\n      \
        \              }\n                }\n                if (n % 2 != 0) p2[p_idx++]\
        \ = mid_char;\n                for (int j = m - 1; j >= 0; j--) p2[p_idx++]\
        \ = p2[j];\n                p2[n] = '\\0';\n                return p2;\n   \
        \         }\n        }\n    }\n\n    return strdup(\"\");\n}"
      csharp: "using System;\nusing System.Collections.Generic;\nusing System.Linq;\n\
        using System.Text;\n\npublic class Solution {\n    public string LexPalindromicPermutation(string\
        \ s, string target) {\n        int n = s.Length;\n        int[] counts = new\
        \ int[26];\n        foreach (char c in s) counts[c - 'a']++;\n\n        int\
        \ oddCount = 0;\n        char? midChar = null;\n        int[] halfCounts = new\
        \ int[26];\n        for (int i = 0; i < 26; i++) {\n            if (counts[i]\
        \ % 2 != 0) {\n                oddCount++;\n                midChar = (char)('a'\
        \ + i);\n            }\n            halfCounts[i] = counts[i] / 2;\n       \
        \ }\n\n        if (oddCount != (n % 2)) return \"\";\n\n        int m = n /\
        \ 2;\n        int[] rem = (int[])halfCounts.Clone();\n        bool canA = true;\n\
        \        for (int i = 0; i < m; i++) {\n            int idx = target[i] - 'a';\n\
        \            if (rem[idx] > 0) rem[idx]--;\n            else { canA = false;\
        \ break; }\n        }\n\n        if (canA) {\n            char[] hChars = target.Substring(0,\
        \ m).ToCharArray();\n            StringBuilder sb = new StringBuilder();\n \
        \           sb.Append(hChars);\n            if (midChar.HasValue) sb.Append(midChar.Value);\n\
        \            for (int i = m - 1; i >= 0; i--) sb.Append(hChars[i]);\n      \
        \      string p1 = sb.ToString();\n            if (string.CompareOrdinal(p1,\
        \ target) > 0) return p1;\n        }\n\n        for (int i = m - 1; i >= 0;\
        \ i--) {\n            int[] currentRem = (int[])halfCounts.Clone();\n      \
        \      bool possible = true;\n            for (int j = 0; j < i; j++) {\n  \
        \              int idx = target[j] - 'a';\n                if (currentRem[idx]\
        \ > 0) currentRem[idx]--;\n                else { possible = false; break; }\n\
        \            }\n            if (!possible) continue;\n\n            for (int\
        \ cIdx = (target[i] - 'a' + 1); cIdx < 26; cIdx++) {\n                if (currentRem[cIdx]\
        \ > 0) {\n                    StringBuilder h = new StringBuilder(target.Substring(0,\
        \ i));\n                    h.Append((char)('a' + cIdx));\n                \
        \    currentRem[cIdx]--;\n                    for (int j = 0; j < 26; j++) {\n\
        \                        h.Append((char)('a' + j), currentRem[j]);\n       \
        \             }\n                    string hStr = h.ToString();\n         \
        \           char[] hRevArr = hStr.ToCharArray();\n                    Array.Reverse(hRevArr);\n\
        \                    StringBuilder res = new StringBuilder(hStr);\n        \
        \            if (midChar.HasValue) res.Append(midChar.Value);\n            \
        \        res.Append(hRevArr);\n                    return res.ToString();\n\
        \                }\n            }\n        }\n\n        return \"\";\n    }\n\
        }"
      javascript: "/**\n * @param {string} s\n * @param {string} target\n * @return\
        \ {string}\n */\nvar lexPalindromicPermutation = function(s, target) {\n   \
        \ const n = s.length;\n    const counts = new Array(26).fill(0);\n    for (let\
        \ i = 0; i < n; i++) {\n        counts[s.charCodeAt(i) - 97]++;\n    }\n\n \
        \   let oddCount = 0;\n    let midChar = \"\";\n    let halfCounts = new Array(26).fill(0);\n\
        \    for (let i = 0; i < 26; i++) {\n        if (counts[i] % 2 !== 0) {\n  \
        \          oddCount++;\n            midChar = String.fromCharCode(97 + i);\n\
        \        }\n        halfCounts[i] = Math.floor(counts[i] / 2);\n    }\n\n  \
        \  if (oddCount !== (n % 2)) return \"\";\n\n    const m = Math.floor(n / 2);\n\
        \n    let rem = [...halfCounts];\n    let canFormA = true;\n    for (let i =\
        \ 0; i < m; i++) {\n        let idx = target.charCodeAt(i) - 97;\n        if\
        \ (rem[idx] > 0) rem[idx]--;\n        else {\n            canFormA = false;\n\
        \            break;\n        }\n    }\n\n    if (canFormA) {\n        let h\
        \ = target.substring(0, m);\n        let p1 = h + midChar + h.split(\"\").reverse().join(\"\
        \");\n        if (p1 > target) return p1;\n    }\n\n    for (let i = m - 1;\
        \ i >= 0; i--) {\n        let remB = [...halfCounts];\n        let possible\
        \ = true;\n        for (let j = 0; j < i; j++) {\n            let idx = target.charCodeAt(j)\
        \ - 97;\n            if (remB[idx] > 0) remB[idx]--;\n            else {\n \
        \               possible = false;\n                break;\n            }\n \
        \       }\n        if (!possible) continue;\n\n        for (let cIdx = target.charCodeAt(i)\
        \ - 97 + 1; cIdx < 26; cIdx++) {\n            if (remB[cIdx] > 0) {\n      \
        \          let h = target.substring(0, i) + String.fromCharCode(97 + cIdx);\n\
        \                remB[cIdx]--;\n                for (let j = 0; j < 26; j++)\
        \ {\n                    h += String.fromCharCode(97 + j).repeat(remB[j]);\n\
        \                }\n                return h + midChar + h.split(\"\").reverse().join(\"\
        \");\n            }\n        }\n    }\n\n    return \"\";\n};"
      typescript: "function lexPalindromicPermutation(s: string, target: string): string\
        \ {\n    const n = s.length;\n    const counts = new Array(26).fill(0);\n  \
        \  for (let i = 0; i < n; i++) {\n        counts[s.charCodeAt(i) - 97]++;\n\
        \    }\n\n    let oddCount = 0;\n    let oddChar = '';\n    for (let i = 0;\
        \ i < 26; i++) {\n        if (counts[i] % 2 !== 0) {\n            oddCount++;\n\
        \            oddChar = String.fromCharCode(i + 97);\n        }\n    }\n\n  \
        \  if (oddCount !== (n % 2)) return \"\";\n\n    const halfCounts = new Array(26).fill(0);\n\
        \    for (let i = 0; i < 26; i++) {\n        halfCounts[i] = Math.floor(counts[i]\
        \ / 2);\n    }\n\n    const m = Math.floor(n / 2);\n\n    // Case 1: Try prefix\
        \ matching target's prefix\n    const rem1 = [...halfCounts];\n    let possible1\
        \ = true;\n    for (let i = 0; i < m; i++) {\n        const cIdx = target.charCodeAt(i)\
        \ - 97;\n        if (rem1[cIdx] > 0) {\n            rem1[cIdx]--;\n        }\
        \ else {\n            possible1 = false;\n            break;\n        }\n  \
        \  }\n\n    if (possible1) {\n        const prefix = target.substring(0, m);\n\
        \        const mid = (n % 2 === 1) ? oddChar : \"\";\n        const p = prefix\
        \ + mid + prefix.split('').reverse().join('');\n        if (p > target) return\
        \ p;\n    }\n\n    // Case 2: Find largest i such that prefix can be greater\n\
        \    for (let i = m - 1; i >= 0; i--) {\n        const rem2 = [...halfCounts];\n\
        \        let possiblePrefix = true;\n        for (let j = 0; j < i; j++) {\n\
        \            const cIdx = target.charCodeAt(j) - 97;\n            if (rem2[cIdx]\
        \ > 0) {\n                rem2[cIdx]--;\n            } else {\n            \
        \    possiblePrefix = false;\n                break;\n            }\n      \
        \  }\n\n        if (!possiblePrefix) continue;\n\n        const targetCharIdx\
        \ = target.charCodeAt(i) - 97;\n        for (let cIdx = targetCharIdx + 1; cIdx\
        \ < 26; cIdx++) {\n            if (rem2[cIdx] > 0) {\n                let resPrefix\
        \ = target.substring(0, i) + String.fromCharCode(cIdx + 97);\n             \
        \   const tempRem = [...rem2];\n                tempRem[cIdx]--;\n         \
        \       for (let j = i + 1; j < m; j++) {\n                    for (let k =\
        \ 0; k < 26; k++) {\n                        if (tempRem[k] > 0) {\n       \
        \                     tempRem[k]--;\n                            resPrefix +=\
        \ String.fromCharCode(k + 97);\n                            break;\n       \
        \                 }\n                    }\n                }\n            \
        \    const mid = (n % 2 === 1) ? oddChar : \"\";\n                return resPrefix\
        \ + mid + resPrefix.split('').reverse().join('');\n            }\n        }\n\
        \    }\n\n    return \"\";\n}"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @param String\
        \ $target\n     * @return String\n     */\n    function lexPalindromicPermutation($s,\
        \ $target) {\n        $n = strlen($s);\n        $counts = array_fill(0, 26,\
        \ 0);\n        for ($i = 0; $i < $n; $i++) {\n            $counts[ord($s[$i])\
        \ - 97]++;\n        }\n\n        $oddCount = 0;\n        $oddChar = '';\n  \
        \      for ($i = 0; $i < 26; $i++) {\n            if ($counts[$i] % 2 !== 0)\
        \ {\n                $oddCount++;\n                $oddChar = chr($i + 97);\n\
        \            }\n        }\n\n        if ($oddCount !== ($n % 2)) return \"\"\
        ;\n\n        $halfCounts = array_fill(0, 26, 0);\n        for ($i = 0; $i <\
        \ 26; $i++) {\n            $halfCounts[$i] = (int)($counts[$i] / 2);\n     \
        \   }\n\n        $m = (int)($n / 2);\n\n        // Case 1: Match first half\
        \ of target exactly\n        $rem = $halfCounts;\n        $possible = true;\n\
        \        for ($i = 0; $i < $m; $i++) {\n            $cIdx = ord($target[$i])\
        \ - 97;\n            if ($rem[$cIdx] > 0) $rem[$cIdx]--;\n            else {\
        \ $possible = false; break; }\n        }\n        if ($possible) {\n       \
        \     $prefix = substr($target, 0, $m);\n            $p = $prefix . ($n % 2\
        \ === 1 ? $oddChar : \"\") . strrev($prefix);\n            if ($p > $target)\
        \ return $p;\n        }\n\n        // Case 2: Search for the first divergence\
        \ to get greater string\n        for ($i = $m - 1; $i >= 0; $i--) {\n      \
        \      $rem = $halfCounts;\n            $possiblePrefix = true;\n          \
        \  for ($j = 0; $j < $i; $j++) {\n                $cIdx = ord($target[$j]) -\
        \ 97;\n                if ($rem[$cIdx] > 0) $rem[$cIdx]--;\n               \
        \ else { $possiblePrefix = false; break; }\n            }\n            if (!$possiblePrefix)\
        \ continue;\n\n            $targetCharIdx = ord($target[$i]) - 97;\n       \
        \     for ($cIdx = $targetCharIdx + 1; $cIdx < 26; $cIdx++) {\n            \
        \    if ($rem[$cIdx] > 0) {\n                    $resPrefix = substr($target,\
        \ 0, $i) . chr($cIdx + 97);\n                    $tempRem = $rem;\n        \
        \            $tempRem[$cIdx]--;\n                    for ($j = $i + 1; $j <\
        \ $m; $j++) {\n                        for ($k = 0; $k < 26; $k++) {\n     \
        \                       if ($tempRem[$k] > 0) {\n                          \
        \      $tempRem[$k]--;\n                                $resPrefix .= chr($k\
        \ + 97);\n                                break;\n                         \
        \   }\n                        }\n                    }\n                  \
        \  return $resPrefix . ($n % 2 === 1 ? $oddChar : \"\") . strrev($resPrefix);\n\
        \                }\n            }\n        }\n\n        return \"\";\n    }\n\
        }"
      swift: "class Solution {\n    func lexPalindromicPermutation(_ s: String, _ target:\
        \ String) -> String {\n        let n = s.count\n        let sChars = Array(s)\n\
        \        let tChars = Array(target)\n        var counts = [Int](repeating: 0,\
        \ count: 26)\n        let aValue = Int(Character(\"a\").asciiValue!)\n\n   \
        \     for char in sChars {\n            counts[Int(char.asciiValue!) - aValue]\
        \ += 1\n        }\n\n        var oddCount = 0\n        var oddChar = Character(\"\
        \ \")\n        for i in 0..<26 {\n            if counts[i] % 2 != 0 {\n    \
        \            oddCount += 1\n                oddChar = Character(UnicodeScalar(i\
        \ + aValue)!)\n            }\n        }\n\n        if oddCount != (n % 2) {\n\
        \            return \"\"\n        }\n\n        var halfCounts = [Int](repeating:\
        \ 0, count: 26)\n        for i in 0..<26 {\n            halfCounts[i] = counts[i]\
        \ / 2\n        }\n\n        let m = n / 2\n\n        // Case 1: Try construction\
        \ matching target's prefix exactly\n        var rem1 = halfCounts\n        var\
        \ possible1 = true\n        for i in 0..<m {\n            let cIdx = Int(tChars[i].asciiValue!)\
        \ - aValue\n            if rem1[cIdx] > 0 {\n                rem1[cIdx] -= 1\n\
        \            } else {\n                possible1 = false\n                break\n\
        \            }\n        }\n\n        if possible1 {\n            let prefix\
        \ = String(tChars[0..<m])\n            let mid = (n % 2 == 1) ? String(oddChar)\
        \ : \"\"\n            let p = prefix + mid + String(prefix.reversed())\n   \
        \         if p > target {\n                return p\n            }\n       \
        \ }\n\n        // Case 2: Greedily find the smallest strictly greater first\
        \ half\n        for i in stride(from: m - 1, through: 0, by: -1) {\n       \
        \     var rem2 = halfCounts\n            var possiblePrefix = true\n       \
        \     for j in 0..<i {\n                let cIdx = Int(tChars[j].asciiValue!)\
        \ - aValue\n                if rem2[cIdx] > 0 {\n                    rem2[cIdx]\
        \ -= 1\n                } else {\n                    possiblePrefix = false\n\
        \                    break\n                }\n            }\n\n           \
        \ if !possiblePrefix { continue }\n\n            let targetCharIdx = Int(tChars[i].asciiValue!)\
        \ - aValue\n            for cIdx in (targetCharIdx + 1)..<26 {\n           \
        \     if rem2[cIdx] > 0 {\n                    var resPrefixChars = Array(tChars[0..<i])\n\
        \                    resPrefixChars.append(Character(UnicodeScalar(cIdx + aValue)!))\n\
        \                    var tempRem = rem2\n                    tempRem[cIdx] -=\
        \ 1\n\n                    for _ in (i + 1)..<m {\n                        for\
        \ k in 0..<26 {\n                            if tempRem[k] > 0 {\n         \
        \                       tempRem[k] -= 1\n                                resPrefixChars.append(Character(UnicodeScalar(k\
        \ + aValue)!))\n                                break\n                    \
        \        }\n                        }\n                    }\n\n           \
        \         let resPrefix = String(resPrefixChars)\n                    let mid\
        \ = (n % 2 == 1) ? String(oddChar) : \"\"\n                    return resPrefix\
        \ + mid + String(resPrefix.reversed())\n                }\n            }\n \
        \       }\n\n        return \"\"\n    }\n}"
      kotlin: "class Solution {\n    fun lexPalindromicPermutation(s: String, target:\
        \ String): String {\n        val n = s.length\n        val counts = IntArray(26)\n\
        \        for (char in s) {\n            counts[char - 'a']++\n        }\n\n\
        \        var oddCount = 0\n        var oddChar = ' '\n        for (i in 0 until\
        \ 26) {\n            if (counts[i] % 2 != 0) {\n                oddCount++\n\
        \                oddChar = (i + 'a'.toInt()).toChar()\n            }\n     \
        \   }\n\n        if (oddCount != n % 2) return \"\"\n\n        val halfCounts\
        \ = IntArray(26)\n        for (i in 0 until 26) {\n            halfCounts[i]\
        \ = counts[i] / 2\n        }\n\n        val m = n / 2\n\n        // Case 1:\
        \ Match first half of target exactly if possible\n        val rem1 = halfCounts.clone()\n\
        \        var possible1 = true\n        for (i in 0 until m) {\n            val\
        \ cIdx = target[i] - 'a'\n            if (cIdx in 0..25 && rem1[cIdx] > 0) {\n\
        \                rem1[cIdx]--\n            } else {\n                possible1\
        \ = false\n                break\n            }\n        }\n\n        if (possible1)\
        \ {\n            val prefix = target.substring(0, m)\n            val mid =\
        \ if (n % 2 == 1) oddChar.toString() else \"\"\n            val p = prefix +\
        \ mid + prefix.reversed()\n            if (p > target) return p\n        }\n\
        \n        // Case 2: Greedily search for divergence point to build lexicographically\
        \ smallest string > target\n        for (i in m - 1 downTo 0) {\n          \
        \  val rem2 = halfCounts.clone()\n            var possiblePrefix = true\n  \
        \          for (j in 0 until i) {\n                val cIdx = target[j] - 'a'\n\
        \                if (rem2[cIdx] > 0) {\n                    rem2[cIdx]--\n \
        \               } else {\n                    possiblePrefix = false\n     \
        \               break\n                }\n            }\n\n            if (!possiblePrefix)\
        \ continue\n\n            val targetCharIdx = target[i] - 'a'\n            for\
        \ (cIdx in targetCharIdx + 1 until 26) {\n                if (rem2[cIdx] > 0)\
        \ {\n                    val sb = StringBuilder()\n                    sb.append(target.substring(0,\
        \ i))\n                    sb.append(('a' + cIdx))\n                    val\
        \ currentRem = rem2.clone()\n                    currentRem[cIdx]--\n\n    \
        \                for (j in i + 1 until m) {\n                        for (k\
        \ in 0 until 26) {\n                            if (currentRem[k] > 0) {\n \
        \                               currentRem[k]--\n                          \
        \      sb.append(('a' + k))\n                                break\n       \
        \                     }\n                        }\n                    }\n\n\
        \                    val resPrefix = sb.toString()\n                    val\
        \ mid = if (n % 2 == 1) oddChar.toString() else \"\"\n                    return\
        \ resPrefix + mid + resPrefix.reversed()\n                }\n            }\n\
        \        }\n\n        return \"\"\n    }\n}"
      dart: "class Solution {\n  String lexPalindromicPermutation(String s, String target)\
        \ {\n    int n = s.length;\n    int m = n ~/ 2;\n    List<int> counts = List.filled(26,\
        \ 0);\n    for (int i = 0; i < n; i++) {\n      counts[s.codeUnitAt(i) - 97]++;\n\
        \    }\n\n    int oddCount = 0;\n    String midChar = \"\";\n    for (int i\
        \ = 0; i < 26; i++) {\n      if (counts[i] % 2 == 1) {\n        oddCount++;\n\
        \        midChar = String.fromCharCode(97 + i);\n      }\n    }\n\n    if ((n\
        \ % 2 == 0 && oddCount != 0) || (n % 2 == 1 && oddCount != 1)) {\n      return\
        \ \"\";\n    }\n\n    List<int> halfCounts = List.generate(26, (i) => counts[i]\
        \ ~/ 2);\n\n    String pPrefix1 = target.substring(0, m);\n    List<int> rem1\
        \ = List.from(halfCounts);\n    bool possible1 = true;\n    for (int i = 0;\
        \ i < pPrefix1.length; i++) {\n      int idx = pPrefix1.codeUnitAt(i) - 97;\n\
        \      if (rem1[idx] > 0) {\n        rem1[idx]--;\n      } else {\n        possible1\
        \ = false;\n        break;\n      }\n    }\n\n    if (possible1) {\n      String\
        \ full = pPrefix1 + midChar + pPrefix1.split('').reversed.join('');\n      if\
        \ (full.compareTo(target) > 0) {\n        return full;\n      }\n    }\n\n \
        \   for (int i = m - 1; i >= 0; i--) {\n      String prefix = target.substring(0,\
        \ i);\n      List<int> rem2 = List.from(halfCounts);\n      bool possible2 =\
        \ true;\n      for (int j = 0; j < i; j++) {\n        int idx = target.codeUnitAt(j)\
        \ - 97;\n        if (rem2[idx] > 0) {\n          rem2[idx]--;\n        } else\
        \ {\n          possible2 = false;\n          break;\n        }\n      }\n\n\
        \      if (!possible2) continue;\n\n      for (int cIdx = target.codeUnitAt(i)\
        \ - 97 + 1; cIdx < 26; cIdx++) {\n        if (rem2[cIdx] > 0) {\n          StringBuffer\
        \ sb = StringBuffer(prefix);\n          sb.write(String.fromCharCode(97 + cIdx));\n\
        \          List<int> rem3 = List.from(rem2);\n          rem3[cIdx]--;\n    \
        \      for (int j = 0; j < 26; j++) {\n            while (rem3[j] > 0) {\n \
        \             sb.write(String.fromCharCode(97 + j));\n              rem3[j]--;\n\
        \            }\n          }\n          String firstHalf = sb.toString();\n \
        \         return firstHalf + midChar + firstHalf.split('').reversed.join('');\n\
        \        }\n      }\n    }\n\n    return \"\";\n  }\n}"
      go: "func lexPalindromicPermutation(s string, target string) string {\n\tn :=\
        \ len(s)\n\tm := n / 2\n\tcounts := make([]int, 26)\n\tfor i := 0; i < n; i++\
        \ {\n\t\tcounts[s[i]-'a']++\n\t}\n\n\toddCount := 0\n\tmidChar := \"\"\n\tfor\
        \ i := 0; i < 26; i++ {\n\t\tif counts[i]%2 == 1 {\n\t\t\toddCount++\n\t\t\t\
        midChar = string(rune('a' + i))\n\t\t}\n\t}\n\n\tif (n%2 == 0 && oddCount !=\
        \ 0) || (n%2 == 1 && oddCount != 1) {\n\t\treturn \"\"\n\t}\n\n\thalfCounts\
        \ := make([]int, 26)\n\tfor i := 0; i < 26; i++ {\n\t\thalfCounts[i] = counts[i]\
        \ / 2\n\t}\n\n\tpPrefix1 := target[:m]\n\trem1 := make([]int, 26)\n\tcopy(rem1,\
        \ halfCounts)\n\tpossible1 := true\n\tfor i := 0; i < len(pPrefix1); i++ {\n\
        \t\tidx := pPrefix1[i] - 'a'\n\t\tif rem1[idx] > 0 {\n\t\t\trem1[idx]--\n\t\t\
        } else {\n\t\t\tpossible1 = false\n\t\t\tbreak\n\t\t}\n\t}\n\n\tif possible1\
        \ {\n\t\tfull := pPrefix1 + midChar + reverse(pPrefix1)\n\t\tif full > target\
        \ {\n\t\t\treturn full\n\t\t}\n\t}\n\n\tfor i := m - 1; i >= 0; i-- {\n\t\t\
        prefix := target[:i]\n\t\trem2 := make([]int, 26)\n\t\tcopy(rem2, halfCounts)\n\
        \t\tpossible2 := true\n\t\tfor j := 0; j < i; j++ {\n\t\t\tidx := target[j]\
        \ - 'a'\n\t\t\tif rem2[idx] > 0 {\n\t\t\t\trem2[idx]--\n\t\t\t} else {\n\t\t\
        \t\tpossible2 = false\n\t\t\t\tbreak\n\t\t\t}\n\t\t}\n\n\t\tif !possible2 {\n\
        \t\t\tcontinue\n\t\t}\n\n\t\tfor cIdx := int(target[i]-'a') + 1; cIdx < 26;\
        \ cIdx++ {\n\t\t\tif rem2[cIdx] > 0 {\n\t\t\t\tres := make([]byte, 0, m)\n\t\
        \t\t\tres = append(res, []byte(prefix)...)\n\t\t\t\tres = append(res, byte('a'+cIdx))\n\
        \t\t\t\trem3 := make([]int, 26)\n\t\t\t\tcopy(rem3, rem2)\n\t\t\t\trem3[cIdx]--\n\
        \t\t\t\tfor j := 0; j < 26; j++ {\n\t\t\t\t\tfor rem3[j] > 0 {\n\t\t\t\t\t\t\
        res = append(res, byte('a'+j))\n\t\t\t\t\t\trem3[j]--\n\t\t\t\t\t}\n\t\t\t\t\
        }\n\t\t\t\tfirstHalf := string(res)\n\t\t\t\treturn firstHalf + midChar + reverse(firstHalf)\n\
        \t\t\t}\n\t\t}\n\t}\n\n\treturn \"\"\n}\n\nfunc reverse(s string) string {\n\
        \tbytes := []byte(s)\n\tfor i, j := 0, len(bytes)-1; i < j; i, j = i+1, j-1\
        \ {\n\t\tbytes[i], bytes[j] = bytes[j], bytes[i]\n\t}\n\treturn string(bytes)\n\
        }"
      ruby: "def lex_palindromic_permutation(s, target)\n  n = s.length\n  m = n / 2\n\
        \  counts = Array.new(26, 0)\n  s.each_char { |c| counts[c.ord - 'a'.ord] +=\
        \ 1 }\n\n  odd_count = 0\n  mid_char = \"\"\n  (0...26).each do |i|\n    if\
        \ counts[i] % 2 == 1\n      odd_count += 1\n      mid_char = (i + 'a'.ord).chr\n\
        \    end\n  end\n\n  return \"\" if (n % 2 == 0 && odd_count != 0) || (n % 2\
        \ == 1 && odd_count != 1)\n\n  half_counts = counts.map { |v| v / 2 }\n\n  p_prefix1\
        \ = target[0...m]\n  rem1 = half_counts.dup\n  possible1 = true\n  p_prefix1.each_char\
        \ do |c|\n    idx = c.ord - 'a'.ord\n    if rem1[idx] > 0\n      rem1[idx] -=\
        \ 1\n    else\n      possible1 = false\n      break\n    end\n  end\n\n  if\
        \ possible1\n    full = p_prefix1 + mid_char + p_prefix1.reverse\n    return\
        \ full if full > target\n  end\n\n  (m - 1).downto(0).each do |i|\n    prefix\
        \ = target[0...i]\n    rem2 = half_counts.dup\n    possible2 = true\n    prefix.each_char\
        \ do |c|\n      idx = c.ord - 'a'.ord\n      if rem2[idx] > 0\n        rem2[idx]\
        \ -= 1\n      else\n        possible2 = false\n        break\n      end\n  \
        \  end\n\n    next unless possible2\n\n    ((target[i].ord - 'a'.ord + 1)...26).each\
        \ do |c_idx|\n      if rem2[c_idx] > 0\n        res_prefix = prefix + (c_idx\
        \ + 'a'.ord).chr\n        rem3 = rem2.dup\n        rem3[c_idx] -= 1\n      \
        \  (0...26).each do |j|\n          while rem3[j] > 0\n            res_prefix\
        \ += (j + 'a'.ord).chr\n            rem3[j] -= 1\n          end\n        end\n\
        \        return res_prefix + mid_char + res_prefix.reverse\n      end\n    end\n\
        \  end\n\n  \"\"\nend"
      scala: "object Solution {\n  def lexPalindromicPermutation(s: String, target:\
        \ String): String = {\n    val n = s.length\n    val m = n / 2\n    val counts\
        \ = new Array[Int](26)\n    for (c <- s) counts(c - 'a') += 1\n\n    var oddCount\
        \ = 0\n    var midChar = \"\"\n    for (i <- 0 until 26) {\n      if (counts(i)\
        \ % 2 == 1) {\n        oddCount += 1\n        midChar = (i + 'a').toChar.toString\n\
        \      }\n    }\n\n    if ((n % 2 == 0 && oddCount != 0) || (n % 2 == 1 && oddCount\
        \ != 1)) return \"\"\n\n    val halfCounts = counts.map(_ / 2)\n\n    val pPrefix1\
        \ = target.substring(0, m)\n    val rem1 = halfCounts.clone()\n    var possible1\
        \ = true\n    for (c <- pPrefix1) {\n      val idx = c - 'a'\n      if (rem1(idx)\
        \ > 0) rem1(idx) -= 1\n      else possible1 = false\n    }\n    if (possible1)\
        \ {\n      val full = pPrefix1 + midChar + pPrefix1.reverse\n      if (full.compareTo(target)\
        \ > 0) return full\n    }\n\n    for (i <- m - 1 to 0 by -1) {\n      val prefix\
        \ = target.substring(0, i)\n      val rem2 = halfCounts.clone()\n      var possible2\
        \ = true\n      for (j <- 0 until i) {\n        val idx = target.charAt(j) -\
        \ 'a'\n        if (rem2(idx) > 0) rem2(idx) -= 1\n        else possible2 = false\n\
        \      }\n\n      if (possible2) {\n        for (cIdx <- (target.charAt(i) -\
        \ 'a' + 1) until 26) {\n          if (rem2(cIdx) > 0) {\n            val sb\
        \ = new StringBuilder(prefix)\n            sb.append((cIdx + 'a').toChar)\n\
        \            val rem3 = rem2.clone()\n            rem3(cIdx) -= 1\n        \
        \    for (j <- 0 until 26) {\n              while (rem3(j) > 0) {\n        \
        \        sb.append((j + 'a').toChar)\n                rem3(j) -= 1\n       \
        \       }\n            }\n            val firstHalf = sb.toString()\n      \
        \      return firstHalf + midChar + firstHalf.reverse\n          }\n       \
        \ }\n      }\n    }\n\n    \"\"\n  }\n}"
      rust: "impl Solution {\n    pub fn lex_palindromic_permutation(s: String, target:\
        \ String) -> String {\n        let n = s.len();\n        let mut counts = [0;\
        \ 26];\n        for b in s.bytes() {\n            counts[(b - b'a') as usize]\
        \ += 1;\n        }\n        let mut odd_count = 0;\n        let mut mid_char\
        \ = None;\n        for i in 0..26 {\n            if counts[i] % 2 != 0 {\n \
        \               odd_count += 1;\n                mid_char = Some((b'a' + i as\
        \ u8) as char);\n            }\n        }\n        if odd_count > 1 || (n %\
        \ 2 == 0 && odd_count > 0) {\n            return \"\".to_string();\n       \
        \ }\n\n        let mut half_counts = [0; 26];\n        for i in 0..26 {\n  \
        \          half_counts[i] = counts[i] / 2;\n        }\n\n        let m = n /\
        \ 2;\n        let target_bytes = target.as_bytes();\n\n        let mut can_match_prefix\
        \ = true;\n        let mut temp_counts = half_counts;\n        for i in 0..m\
        \ {\n            let idx = (target_bytes[i] - b'a') as usize;\n            if\
        \ temp_counts[idx] > 0 {\n                temp_counts[idx] -= 1;\n         \
        \   } else {\n                can_match_prefix = false;\n                break;\n\
        \            }\n        }\n\n        if can_match_prefix {\n            let\
        \ mut s_base = target[..m].to_string();\n            if let Some(c) = mid_char\
        \ {\n                s_base.push(c);\n            }\n            let first_half_rev:\
        \ String = target[..m].chars().rev().collect();\n            s_base.push_str(&first_half_rev);\n\
        \            if s_base > target {\n                return s_base;\n        \
        \    }\n        }\n\n        for i in (0..m).rev() {\n            let mut current_counts\
        \ = half_counts;\n            let mut can_form = true;\n            for j in\
        \ 0..i {\n                let idx = (target_bytes[j] - b'a') as usize;\n   \
        \             if current_counts[idx] > 0 {\n                    current_counts[idx]\
        \ -= 1;\n                } else {\n                    can_form = false;\n \
        \                   break;\n                }\n            }\n            if\
        \ !can_form {\n                continue;\n            }\n\n            for c_idx\
        \ in (target_bytes[i] - b'a' + 1) as usize..26 {\n                if current_counts[c_idx]\
        \ > 0 {\n                    let mut res_half = target[..i].to_string();\n \
        \                   res_half.push((b'a' + c_idx as u8) as char);\n         \
        \           let mut remaining_counts = current_counts;\n                   \
        \ remaining_counts[c_idx] -= 1;\n                    for r_idx in 0..26 {\n\
        \                        for _ in 0..remaining_counts[r_idx] {\n           \
        \                 res_half.push((b'a' + r_idx as u8) as char);\n           \
        \             }\n                    }\n                    let mut res = res_half.clone();\n\
        \                    if let Some(c) = mid_char {\n                        res.push(c);\n\
        \                    }\n                    let first_half_rev: String = res_half.chars().rev().collect();\n\
        \                    res.push_str(&first_half_rev);\n                    return\
        \ res;\n                }\n            }\n        }\n\n        \"\".to_string()\n\
        \    }\n}"
      racket: "(define/contract (lex-palindromic-permutation s target)\n  (-> string?\
        \ string? string?)\n  (let* ([n (string-length s)]\n         [counts (make-vector\
        \ 26 0)])\n    (for ([c (string->list s)])\n      (let ([idx (- (char->integer\
        \ c) (char->integer #\\a))])\n        (vector-set! counts idx (+ 1 (vector-ref\
        \ counts idx)))))\n    (let* ([odd-chars (filter (lambda (i) (odd? (vector-ref\
        \ counts i))) (range 26))]\n           [odd-count (length odd-chars)])\n   \
        \   (if (or (> odd-count 1) (and (even? n) (> odd-count 0)))\n          \"\"\
        \n          (let* ([half-counts (make-vector 26 0)]\n                 [mid-char\
        \ (if (= odd-count 1)\n                               (string (integer->char\
        \ (+ (car odd-chars) (char->integer #\\a))))\n                             \
        \  \"\")]\n                 [m (quotient n 2)])\n            (for ([i 26])\n\
        \              (vector-set! half-counts i (quotient (vector-ref counts i) 2)))\n\
        \            (define (can-form-prefix? prefix-list counts-vec)\n           \
        \   (let ([temp (vector-copy counts-vec)]\n                    [ok #t])\n  \
        \              (for ([c prefix-list])\n                  (let ([idx (- (char->integer\
        \ c) (char->integer #\\a))])\n                    (if (> (vector-ref temp idx)\
        \ 0)\n                        (vector-set! temp idx (- (vector-ref temp idx)\
        \ 1))\n                        (set! ok #f))))\n                (if ok temp\
        \ #f)))\n            (let ([target-list (string->list target)])\n          \
        \    (let* ([target-half-list (take target-list m)]\n                     [base-counts\
        \ (can-form-prefix? target-half-list half-counts)]\n                     [s-base\
        \ (if base-counts\n                                 (let* ([h (substring target\
        \ 0 m)])\n                                   (string-append h mid-char (list->string\
        \ (reverse (string->list h)))))\n                                 #f)])\n  \
        \              (if (and s-base (string>? s-base target))\n                 \
        \   s-base\n                    (let loop ([i (- m 1)])\n                  \
        \    (if (< i 0)\n                          \"\"\n                         \
        \ (let* ([prefix-list (take target-list i)]\n                              \
        \   [rem-counts (can-form-prefix? prefix-list half-counts)])\n             \
        \               (if rem-counts\n                                (let ([found-c\
        \ (for/first ([c-idx (range (+ 1 (- (char->integer (list-ref target-list i))\
        \ (char->integer #\\a))) 26)]\n                                            \
        \              #:when (> (vector-ref rem-counts c-idx) 0))\n               \
        \                                  c-idx)])\n                              \
        \    (if found-c\n                                      (let* ([prefix (substring\
        \ target 0 i)]\n                                             [char-i (string\
        \ (integer->char (+ found-c (char->integer #\\a))))]\n                     \
        \                        [final-counts (vector-copy rem-counts)])\n        \
        \                                (vector-set! final-counts found-c (- (vector-ref\
        \ final-counts found-c) 1))\n                                        (let ([rest\
        \ (list->string\n                                                     (append-map\
        \ (lambda (idx) (make-list (vector-ref final-counts idx) (integer->char (+ idx\
        \ (char->integer #\\a)))))\n                                               \
        \                  (range 26)))])\n                                        \
        \  (let ([full-half (string-append prefix char-i rest)])\n                 \
        \                           (string-append full-half mid-char (list->string\
        \ (reverse (string->list full-half)))))))\n                                \
        \      (loop (- i 1))))\n                                (loop (- i 1))))))))))))))"
      erlang: "-spec lex_palindromic_permutation(S :: unicode:unicode_binary(), Target\
        \ :: unicode:unicode_binary()) -> unicode:unicode_binary().\nlex_palindromic_permutation(S,\
        \ Target) ->\n    N = byte_size(S),\n    SList = binary_to_list(S),\n    Counts\
        \ = lists:foldl(fun(C, Acc) -> maps:put(C, maps:get(C, Acc, 0) + 1, Acc) end,\
        \ #{}, SList),\n    Odds = [C || {C, V} <- maps:to_list(Counts), V rem 2 =/=\
        \ 0],\n    OddCount = length(Odds),\n    case (OddCount > 1 orelse (N rem 2\
        \ == 0 andalso OddCount > 0)) of\n        true -> <<>>;\n        false ->\n\
        \            MidChar = case Odds of [C] -> [C]; [] -> [] end,\n            HalfCounts\
        \ = maps:from_list([{C, V div 2} || {C, V} <- maps:to_list(Counts)]),\n    \
        \        M = N div 2,\n            TargetList = binary_to_list(Target),\n  \
        \          TargetHalf = lists:sublist(TargetList, 1, M),\n            SBase\
        \ = case can_form(TargetHalf, HalfCounts) of\n                {ok, _} -> \n\
        \                    Base = list_to_binary(TargetHalf ++ MidChar ++ lists:reverse(TargetHalf)),\n\
        \                    case Base > Target of true -> Base; false -> nil end;\n\
        \                fail -> nil\n            end,\n            case SBase of\n\
        \                nil -> find_greedy(M - 1, TargetList, HalfCounts, MidChar,\
        \ Target);\n                Res -> Res\n            end\n    end.\n\ncan_form([],\
        \ Counts) -> {ok, Counts};\ncan_form([H|T], Counts) ->\n    case maps:get(H,\
        \ Counts, 0) of\n        V when V > 0 -> can_form(T, maps:put(H, V - 1, Counts));\n\
        \        _ -> fail\n    end.\n\nfind_greedy(-1, _, _, _, _) -> <<>>;\nfind_greedy(I,\
        \ TargetList, HalfCounts, MidChar, Target) ->\n    Prefix = lists:sublist(TargetList,\
        \ 1, I),\n    case can_form(Prefix, HalfCounts) of\n        {ok, RemCounts}\
        \ ->\n            TargetI = lists:nth(I + 1, TargetList),\n            case\
        \ find_char(TargetI + 1, RemCounts) of\n                {ok, C} ->\n       \
        \             NewRem = maps:put(C, maps:get(C, RemCounts) - 1, RemCounts),\n\
        \                    Rest = lists:flatmap(fun(RC) -> lists:duplicate(maps:get(RC,\
        \ NewRem, 0), RC) end, lists:seq($a, $z)),\n                    FullHalf = Prefix\
        \ ++ [C] ++ Rest,\n                    list_to_binary(FullHalf ++ MidChar ++\
        \ lists:reverse(FullHalf));\n                nil -> find_greedy(I - 1, TargetList,\
        \ HalfCounts, MidChar, Target)\n            end;\n        fail -> find_greedy(I\
        \ - 1, TargetList, HalfCounts, MidChar, Target)\n    end.\n\nfind_char(C, Counts)\
        \ when C > $z -> nil;\nfind_char(C, Counts) ->\n    case maps:get(C, Counts,\
        \ 0) of\n        V when V > 0 -> {ok, C};\n        _ -> find_char(C + 1, Counts)\n\
        \    end."
      elixir: "defmodule Solution do\n  @spec lex_palindromic_permutation(s :: String.t,\
        \ target :: String.t) :: String.t\n  def lex_palindromic_permutation(s, target)\
        \ do\n    n = String.length(s)\n    m = div(n, 2)\n    s_chars = String.to_charlist(s)\n\
        \    counts = Enum.reduce(s_chars, %{}, fn c, acc -> Map.update(acc, c, 1, &(&1\
        \ + 1)) end)\n    odd_chars = Enum.filter(counts, fn {_, v} -> rem(v, 2) !=\
        \ 0 end)\n\n    if length(odd_chars) > 1 or (rem(n, 2) == 0 and length(odd_chars)\
        \ > 0) do\n      \"\"\n    else\n      mid_char = case odd_chars do\n      \
        \  [{c, _}] -> <<c>>\n        [] -> \"\"\n      end\n      half_counts = Enum.map(counts,\
        \ fn {c, v} -> {c, div(v, 2)} end) |> Enum.into(%{})\n      target_chars = String.to_charlist(target)\n\
        \      target_half = Enum.take(target_chars, m)\n\n      s_base = case can_form(target_half,\
        \ half_counts) do\n        {:ok, _} -> \n          h = List.to_string(target_half)\n\
        \          res = h <> mid_char <> String.reverse(h)\n          if res > target,\
        \ do: res, else: nil\n        _ -> nil\n      end\n\n      if s_base do\n  \
        \      s_base\n      else\n        find_greedy(m - 1, target_chars, half_counts,\
        \ mid_char) || \"\"\n      end\n    end\n  end\n\n  defp can_form(chars, counts)\
        \ do\n    Enum.reduce_while(chars, counts, fn c, acc ->\n      if Map.get(acc,\
        \ c, 0) > 0 do\n        {:cont, Map.update!(acc, c, &(&1 - 1))}\n      else\n\
        \        {:halt, nil}\n      end\n    end) |> case do\n      nil -> :fail\n\
        \      res -> {:ok, res}\n    end\n  end\n\n  defp find_greedy(-1, _, _, _),\
        \ do: nil\n  defp find_greedy(i, target_chars, half_counts, mid_char) do\n \
        \   prefix = Enum.take(target_chars, i)\n    case can_form(prefix, half_counts)\
        \ do\n      {:ok, rem_counts} ->\n        target_i = Enum.at(target_chars, i)\n\
        \        res = Enum.find_value(?a..?z, fn c ->\n          if c > target_i and\
        \ Map.get(rem_counts, c, 0) > 0 do\n            new_rem = Map.update!(rem_counts,\
        \ c, &(&1 - 1))\n            rest = Enum.map(?a..?z, fn rc ->\n            \
        \  String.duplicate(<<rc>>, Map.get(new_rem, rc, 0))\n            end) |> Enum.join(\"\
        \")\n            h = List.to_string(prefix) <> <<c>> <> rest\n            h\
        \ <> mid_char <> String.reverse(h)\n          else\n            nil\n      \
        \    end\n        end)\n        res || find_greedy(i - 1, target_chars, half_counts,\
        \ mid_char)\n      :fail -> find_greedy(i - 1, target_chars, half_counts, mid_char)\n\
        \    end\n  end\nend"
    approach: 'To find the lexicographically smallest palindromic permutation strictly
      greater than the target, we first verify if a palindromic permutation is possible
      by checking that at most one character has an odd frequency (which must be exactly
      one if the length $n$ is odd, and zero if $n$ is even). We define the first half
      of the palindrome (of length $\lfloor n/2 \rfloor$) and a fixed middle character
      for odd $n$. Any valid palindrome is uniquely determined by its first half and
      the middle character. We identify two potential candidates for the smallest palindrome
      greater than the target: the ''Match'' candidate, which uses the first half of
      the target string if possible, and the ''Diverge'' candidate, which deviates from
      the target at the largest possible index $i$ in the first half.


      Specifically, the ''Match'' candidate is formed by taking the first $\lfloor n/2
      \rfloor$ characters of the target as the prefix. If these characters are available
      in the required frequencies, we construct the full palindrome and check if it
      is strictly greater than the target. If not, or if the prefix cannot be formed,
      we search for the largest index $i < \lfloor n/2 \rfloor$ where we can match the
      target''s prefix for $i$ characters and then pick the smallest available character
      $c > target[i]$. To keep the resulting string as small as possible, we fill the
      remaining positions of the first half with the smallest available characters.
      Since any palindrome with a longer matching prefix is smaller than one with a
      shorter matching prefix, the ''Match'' candidate is preferred if it satisfies
      the condition; otherwise, the ''Diverge'' candidate with the largest $i$ is the
      optimal answer.'
    time_complexity: O(n) where $n$ is the length of the string. Counting characters
      takes $O(n)$, and constructing candidates involves iterating through the prefix
      length and a constant-sized alphabet ($26$ characters), resulting in $O(26 \cdot
      n)$ operations.
    space_complexity: O(n) for storing the character frequencies and the resulting palindrome
      string. The alphabet size is constant ($O(26)$), so it does not scale with the
      input length.
    elapsed_time: 1133.6526737213135
    model: gemini-3-flash-preview
    generated_at: '2026-08-28 08:36:13 '
---

## Problem #3734: Lexicographically Smallest Palindromic Permutation Greater Than Target

**Difficulty:** Hard

**Topics:** Two Pointers, String, Enumeration

## Problem Description

<p>You are given two strings <code>s</code> and <code>target</code>, each of length <code>n</code>, consisting of lowercase English letters.</p>

<p>Return the <strong><span data-keyword="lexicographically-smaller-string">lexicographically smallest</span> string</strong> that is <strong>both</strong> a <strong><span data-keyword="palindrome-string">palindromic</span> <span data-keyword="permutation">permutation</span></strong> of <code>s</code> and <strong>strictly</strong> greater than <code>target</code>. If no such permutation exists, return an empty string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;baba&quot;, target = &quot;abba&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;baab&quot;</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The palindromic permutations of <code>s</code> (in lexicographical order) are <code>&quot;abba&quot;</code> and <code>&quot;baab&quot;</code>.</li>
	<li>The lexicographically smallest permutation that is strictly greater than <code>target</code> is <code>&quot;baab&quot;</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;baba&quot;, target = &quot;bbaa&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;&quot;</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The palindromic permutations of <code>s</code> (in lexicographical order) are <code>&quot;abba&quot;</code> and <code>&quot;baab&quot;</code>.</li>
	<li>None of them is lexicographically strictly greater than <code>target</code>. Therefore, the answer is <code>&quot;&quot;</code>.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abc&quot;, target = &quot;abb&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p><code>s</code> has no palindromic permutations. Therefore, the answer is <code>&quot;&quot;</code>.</p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;aac&quot;, target = &quot;abb&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;aca&quot;</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The only palindromic permutation of <code>s</code> is <code>&quot;aca&quot;</code>.</li>
	<li><code>&quot;aca&quot;</code> is strictly greater than <code>target</code>. Therefore, the answer is <code>&quot;aca&quot;</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == s.length == target.length &lt;= 300</code></li>
	<li><code>s</code> and <code>target</code> consist of only lowercase English letters.</li>
</ul>


## Hints

1. A palindromic permutation exists only if at most one character has an odd count (for odd-length strings) or all counts are even (for even-length strings).

2. Focus on constructing the first half of the palindrome. The second half is determined by mirroring.

3. To be lexicographically greater than target, the first half must be greater than or equal to target's first half, with careful handling of the middle character for odd-length strings.

4. Use a backtracking approach or greedy selection for each position in the first half, trying the smallest available character that can still produce a valid palindrome.

5. After building the first half, mirror it (and add the middle character if needed) to form the full palindrome and verify it is strictly greater than target.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To find the lexicographically smallest palindromic permutation strictly greater than the target, we first verify if a palindromic permutation is possible by checking that at most one character has an odd frequency (which must be exactly one if the length $n$ is odd, and zero if $n$ is even). We define the first half of the palindrome (of length $\lfloor n/2 \rfloor$) and a fixed middle character for odd $n$. Any valid palindrome is uniquely determined by its first half and the middle character. We identify two potential candidates for the smallest palindrome greater than the target: the 'Match' candidate, which uses the first half of the target string if possible, and the 'Diverge' candidate, which deviates from the target at the largest possible index $i$ in the first half.

Specifically, the 'Match' candidate is formed by taking the first $\lfloor n/2 \rfloor$ characters of the target as the prefix. If these characters are available in the required frequencies, we construct the full palindrome and check if it is strictly greater than the target. If not, or if the prefix cannot be formed, we search for the largest index $i < \lfloor n/2 \rfloor$ where we can match the target's prefix for $i$ characters and then pick the smallest available character $c > target[i]$. To keep the resulting string as small as possible, we fill the remaining positions of the first half with the smallest available characters. Since any palindrome with a longer matching prefix is smaller than one with a shorter matching prefix, the 'Match' candidate is preferred if it satisfies the condition; otherwise, the 'Diverge' candidate with the largest $i$ is the optimal answer.

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
    string lexPalindromicPermutation(string s, string target) {
        int n = s.length();
        vector<int> counts(26, 0);
        for (char c : s) counts[c - 'a']++;

        int odd_count = 0;
        char mid_char = '\0';
        for (int i = 0; i < 26; ++i) {
            if (counts[i] % 2 != 0) {
                odd_count++;
                mid_char = (char)('a' + i);
            }
        }

        if (odd_count != (n % 2)) return "";

        vector<int> half_counts(26);
        for (int i = 0; i < 26; ++i) half_counts[i] = counts[i] / 2;

        int half_len = n / 2;
        string mid_str = (mid_char == '\0') ? "" : string(1, mid_char);

        // Try Match candidate
        vector<int> temp_counts = half_counts;
        string H = "";
        bool possible = true;
        for (int i = 0; i < half_len; ++i) {
            int idx = target[i] - 'a';
            if (temp_counts[idx] > 0) {
                temp_counts[idx]--;
                H += target[i];
            } else {
                possible = false;
                break;
            }
        }

        if (possible) {
            string h_rev = H;
            reverse(h_rev.begin(), h_rev.end());
            string P = H + mid_str + h_rev;
            if (P > target) return P;
        }

        // Try Diverge candidate
        vector<bool> can_form_prefix(half_len + 1, false);
        can_form_prefix[0] = true;
        temp_counts = half_counts;
        for (int i = 1; i <= half_len; ++i) {
            int idx = target[i - 1] - 'a';
            if (temp_counts[idx] > 0) {
                temp_counts[idx]--;
                can_form_prefix[i] = true;
            } else break;
        }

        for (int i = half_len - 1; i >= 0; --i) {
            if (!can_form_prefix[i]) continue;
            temp_counts = half_counts;
            for (int j = 0; j < i; ++j) temp_counts[target[j] - 'a']--;

            for (int c_idx = (target[i] - 'a') + 1; c_idx < 26; ++c_idx) {
                if (temp_counts[c_idx] > 0) {
                    string res_H = target.substr(0, i);
                    res_H += (char)('a' + c_idx);
                    temp_counts[c_idx]--;
                    for (int k = 0; k < 26; ++k) {
                        while (temp_counts[k] > 0) {
                            res_H += (char)('a' + k);
                            temp_counts[k]--;
                        }
                    }
                    string h_rev = res_H;
                    reverse(h_rev.begin(), h_rev.end());
                    return res_H + mid_str + h_rev;
                }
            }
        }

        return "";
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public String lexPalindromicPermutation(String s, String target) {
        int n = s.length();
        int[] counts = new int[26];
        for (char c : s.toCharArray()) counts[c - 'a']++;

        int oddCount = 0;
        char midChar = '\0';
        for (int i = 0; i < 26; i++) {
            if (counts[i] % 2 != 0) {
                oddCount++;
                midChar = (char) ('a' + i);
            }
        }

        if (oddCount != (n % 2)) return "";

        int[] halfCounts = new int[26];
        for (int i = 0; i < 26; i++) halfCounts[i] = counts[i] / 2;

        int halfLen = n / 2;
        String midStr = (midChar == '\0') ? "" : String.valueOf(midChar);

        // Try Match candidate
        int[] tempCounts = halfCounts.clone();
        StringBuilder hMatch = new StringBuilder();
        boolean possible = true;
        for (int i = 0; i < halfLen; i++) {
            int idx = target.charAt(i) - 'a';
            if (tempCounts[idx] > 0) {
                tempCounts[idx]--;
                hMatch.append(target.charAt(i));
            } else {
                possible = false;
                break;
            }
        }

        if (possible) {
            String H = hMatch.toString();
            String hRev = new StringBuilder(H).reverse().toString();
            String P = H + midStr + hRev;
            if (P.compareTo(target) > 0) return P;
        }

        // Try Diverge candidate
        boolean[] canFormPrefix = new boolean[halfLen + 1];
        canFormPrefix[0] = true;
        tempCounts = halfCounts.clone();
        for (int i = 1; i <= halfLen; i++) {
            int idx = target.charAt(i - 1) - 'a';
            if (tempCounts[idx] > 0) {
                tempCounts[idx]--;
                canFormPrefix[i] = true;
            } else break;
        }

        for (int i = halfLen - 1; i >= 0; i--) {
            if (!canFormPrefix[i]) continue;
            tempCounts = halfCounts.clone();
            for (int j = 0; j < i; j++) tempCounts[target.charAt(j) - 'a']--;

            for (int cIdx = (target.charAt(i) - 'a') + 1; cIdx < 26; cIdx++) {
                if (tempCounts[cIdx] > 0) {
                    StringBuilder resH = new StringBuilder(target.substring(0, i));
                    resH.append((char) ('a' + cIdx));
                    tempCounts[cIdx]--;
                    for (int k = 0; k < 26; k++) {
                        while (tempCounts[k] > 0) {
                            resH.append((char) ('a' + k));
                            tempCounts[k]--;
                        }
                    }
                    String H = resH.toString();
                    String hRev = new StringBuilder(H).reverse().toString();
                    return H + midStr + hRev;
                }
            }
        }

        return "";
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        n = len(s)
        counts = [0] * 26
        for char in s:
            counts[ord(char) - ord('a')] += 1

        odd_indices = [i for i, count in enumerate(counts) if count % 2 != 0]
        if len(odd_indices) != (n % 2):
            return ""

        mid_char = chr(ord('a') + odd_indices[0]) if odd_indices else ""
        half_counts = [count // 2 for count in counts]
        half_len = n // 2

        # Try Match candidate: prefix matches target[:half_len]
        temp_counts = list(half_counts)
        h_match = []
        possible = True
        for i in range(half_len):
            idx = ord(target[i]) - ord('a')
            if temp_counts[idx] > 0:
                temp_counts[idx] -= 1
                h_match.append(target[i])
            else:
                possible = False
                break

        if possible:
            h_str = "".join(h_match)
            p_match = h_str + mid_char + h_str[::-1]
            if p_match > target:
                return p_match

        # Try Diverge candidate: find largest i and smallest c > target[i]
        can_form_prefix = [False] * (half_len + 1)
        can_form_prefix[0] = True
        temp_counts = list(half_counts)
        for i in range(1, half_len + 1):
            idx = ord(target[i-1]) - ord('a')
            if temp_counts[idx] > 0:
                temp_counts[idx] -= 1
                can_form_prefix[i] = True
            else:
                break

        for i in range(half_len - 1, -1, -1):
            if not can_form_prefix[i]:
                continue

            rem_counts = list(half_counts)
            for j in range(i):
                rem_counts[ord(target[j]) - ord('a')] -= 1

            for c_idx in range(ord(target[i]) - ord('a') + 1, 26):
                if rem_counts[c_idx] > 0:
                    h_diverge = list(target[:i])
                    h_diverge.append(chr(ord('a') + c_idx))
                    rem_counts[c_idx] -= 1
                    for k in range(26):
                        while rem_counts[k] > 0:
                            h_diverge.append(chr(ord('a') + k))
                            rem_counts[k] -= 1

                    h_str = "".join(h_diverge)
                    return h_str + mid_char + h_str[::-1]

        return ""
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = [0] * 26
        for char in s:
            counts[ord(char) - ord('a')] += 1

        odd_count = 0
        mid_char = ""
        half_counts = [0] * 26
        for i in range(26):
            if counts[i] % 2 != 0:
                odd_count += 1
                mid_char = chr(ord('a') + i)
            half_counts[i] = counts[i] // 2

        if odd_count != (n % 2):
            return ""

        m = n // 2

        def can_form(prefix, initial_counts):
            rem = initial_counts[:]
            for char in prefix:
                idx = ord(char) - ord('a')
                if rem[idx] > 0:
                    rem[idx] -= 1
                else:
                    return False, None
            return True, rem

        can_a, rem_a = can_form(target[:m], half_counts)
        if can_a:
            h = target[:m]
            p1 = h + mid_char + h[::-1]
            if p1 > target:
                return p1

        for i in range(m - 1, -1, -1):
            can_prefix, rem_counts = can_form(target[:i], half_counts)
            if not can_prefix:
                continue

            for c_idx in range(ord(target[i]) - ord('a') + 1, 26):
                if rem_counts[c_idx] > 0:
                    rem_counts[c_idx] -= 1
                    h_list = list(target[:i])
                    h_list.append(chr(ord('a') + c_idx))
                    for j in range(26):
                        h_list.extend([chr(ord('a') + j)] * rem_counts[j])
                    h = "".join(h_list)
                    return h + mid_char + h[::-1]

        return ""
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

char* lexPalindromicPermutation(char* s, char* target) {
    int n = strlen(s);
    int counts[26] = {0};
    for (int i = 0; i < n; i++) counts[s[i] - 'a']++;

    int odd_count = 0;
    int mid_idx = -1;
    int half_counts[26];
    for (int i = 0; i < 26; i++) {
        if (counts[i] % 2 != 0) {
            odd_count++;
            mid_idx = i;
        }
        half_counts[i] = counts[i] / 2;
    }

    if (odd_count != (n % 2)) return strdup("");

    int m = n / 2;
    char mid_char = (mid_idx == -1) ? '\0' : (char)('a' + mid_idx);

    int rem[26];
    memcpy(rem, half_counts, sizeof(rem));
    int can_a = 1;
    for (int i = 0; i < m; i++) {
        int idx = target[i] - 'a';
        if (rem[idx] > 0) rem[idx]--;
        else { can_a = 0; break; }
    }

    if (can_a) {
        char* p1 = (char*)malloc(n + 1);
        for (int i = 0; i < m; i++) p1[i] = target[i];
        int p_idx = m;
        if (n % 2 != 0) p1[p_idx++] = mid_char;
        for (int i = m - 1; i >= 0; i--) p1[p_idx++] = target[i];
        p1[n] = '\0';
        if (strcmp(p1, target) > 0) return p1;
        free(p1);
    }

    for (int i = m - 1; i >= 0; i--) {
        memcpy(rem, half_counts, sizeof(rem));
        int possible = 1;
        for (int j = 0; j < i; j++) {
            int idx = target[j] - 'a';
            if (rem[idx] > 0) rem[idx]--;
            else { possible = 0; break; }
        }
        if (!possible) continue;

        for (int c_idx = (target[i] - 'a' + 1); c_idx < 26; c_idx++) {
            if (rem[c_idx] > 0) {
                char* p2 = (char*)malloc(n + 1);
                for (int j = 0; j < i; j++) p2[j] = target[j];
                p2[i] = (char)('a' + c_idx);
                rem[c_idx]--;
                int p_idx = i + 1;
                for (int j = 0; j < 26; j++) {
                    while (rem[j] > 0) {
                        p2[p_idx++] = (char)('a' + j);
                        rem[j]--;
                    }
                }
                if (n % 2 != 0) p2[p_idx++] = mid_char;
                for (int j = m - 1; j >= 0; j--) p2[p_idx++] = p2[j];
                p2[n] = '\0';
                return p2;
            }
        }
    }

    return strdup("");
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
    public string LexPalindromicPermutation(string s, string target) {
        int n = s.Length;
        int[] counts = new int[26];
        foreach (char c in s) counts[c - 'a']++;

        int oddCount = 0;
        char? midChar = null;
        int[] halfCounts = new int[26];
        for (int i = 0; i < 26; i++) {
            if (counts[i] % 2 != 0) {
                oddCount++;
                midChar = (char)('a' + i);
            }
            halfCounts[i] = counts[i] / 2;
        }

        if (oddCount != (n % 2)) return "";

        int m = n / 2;
        int[] rem = (int[])halfCounts.Clone();
        bool canA = true;
        for (int i = 0; i < m; i++) {
            int idx = target[i] - 'a';
            if (rem[idx] > 0) rem[idx]--;
            else { canA = false; break; }
        }

        if (canA) {
            char[] hChars = target.Substring(0, m).ToCharArray();
            StringBuilder sb = new StringBuilder();
            sb.Append(hChars);
            if (midChar.HasValue) sb.Append(midChar.Value);
            for (int i = m - 1; i >= 0; i--) sb.Append(hChars[i]);
            string p1 = sb.ToString();
            if (string.CompareOrdinal(p1, target) > 0) return p1;
        }

        for (int i = m - 1; i >= 0; i--) {
            int[] currentRem = (int[])halfCounts.Clone();
            bool possible = true;
            for (int j = 0; j < i; j++) {
                int idx = target[j] - 'a';
                if (currentRem[idx] > 0) currentRem[idx]--;
                else { possible = false; break; }
            }
            if (!possible) continue;

            for (int cIdx = (target[i] - 'a' + 1); cIdx < 26; cIdx++) {
                if (currentRem[cIdx] > 0) {
                    StringBuilder h = new StringBuilder(target.Substring(0, i));
                    h.Append((char)('a' + cIdx));
                    currentRem[cIdx]--;
                    for (int j = 0; j < 26; j++) {
                        h.Append((char)('a' + j), currentRem[j]);
                    }
                    string hStr = h.ToString();
                    char[] hRevArr = hStr.ToCharArray();
                    Array.Reverse(hRevArr);
                    StringBuilder res = new StringBuilder(hStr);
                    if (midChar.HasValue) res.Append(midChar.Value);
                    res.Append(hRevArr);
                    return res.ToString();
                }
            }
        }

        return "";
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
 * @param {string} target
 * @return {string}
 */
var lexPalindromicPermutation = function(s, target) {
    const n = s.length;
    const counts = new Array(26).fill(0);
    for (let i = 0; i < n; i++) {
        counts[s.charCodeAt(i) - 97]++;
    }

    let oddCount = 0;
    let midChar = "";
    let halfCounts = new Array(26).fill(0);
    for (let i = 0; i < 26; i++) {
        if (counts[i] % 2 !== 0) {
            oddCount++;
            midChar = String.fromCharCode(97 + i);
        }
        halfCounts[i] = Math.floor(counts[i] / 2);
    }

    if (oddCount !== (n % 2)) return "";

    const m = Math.floor(n / 2);

    let rem = [...halfCounts];
    let canFormA = true;
    for (let i = 0; i < m; i++) {
        let idx = target.charCodeAt(i) - 97;
        if (rem[idx] > 0) rem[idx]--;
        else {
            canFormA = false;
            break;
        }
    }

    if (canFormA) {
        let h = target.substring(0, m);
        let p1 = h + midChar + h.split("").reverse().join("");
        if (p1 > target) return p1;
    }

    for (let i = m - 1; i >= 0; i--) {
        let remB = [...halfCounts];
        let possible = true;
        for (let j = 0; j < i; j++) {
            let idx = target.charCodeAt(j) - 97;
            if (remB[idx] > 0) remB[idx]--;
            else {
                possible = false;
                break;
            }
        }
        if (!possible) continue;

        for (let cIdx = target.charCodeAt(i) - 97 + 1; cIdx < 26; cIdx++) {
            if (remB[cIdx] > 0) {
                let h = target.substring(0, i) + String.fromCharCode(97 + cIdx);
                remB[cIdx]--;
                for (let j = 0; j < 26; j++) {
                    h += String.fromCharCode(97 + j).repeat(remB[j]);
                }
                return h + midChar + h.split("").reverse().join("");
            }
        }
    }

    return "";
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function lexPalindromicPermutation(s: string, target: string): string {
    const n = s.length;
    const counts = new Array(26).fill(0);
    for (let i = 0; i < n; i++) {
        counts[s.charCodeAt(i) - 97]++;
    }

    let oddCount = 0;
    let oddChar = '';
    for (let i = 0; i < 26; i++) {
        if (counts[i] % 2 !== 0) {
            oddCount++;
            oddChar = String.fromCharCode(i + 97);
        }
    }

    if (oddCount !== (n % 2)) return "";

    const halfCounts = new Array(26).fill(0);
    for (let i = 0; i < 26; i++) {
        halfCounts[i] = Math.floor(counts[i] / 2);
    }

    const m = Math.floor(n / 2);

    // Case 1: Try prefix matching target's prefix
    const rem1 = [...halfCounts];
    let possible1 = true;
    for (let i = 0; i < m; i++) {
        const cIdx = target.charCodeAt(i) - 97;
        if (rem1[cIdx] > 0) {
            rem1[cIdx]--;
        } else {
            possible1 = false;
            break;
        }
    }

    if (possible1) {
        const prefix = target.substring(0, m);
        const mid = (n % 2 === 1) ? oddChar : "";
        const p = prefix + mid + prefix.split('').reverse().join('');
        if (p > target) return p;
    }

    // Case 2: Find largest i such that prefix can be greater
    for (let i = m - 1; i >= 0; i--) {
        const rem2 = [...halfCounts];
        let possiblePrefix = true;
        for (let j = 0; j < i; j++) {
            const cIdx = target.charCodeAt(j) - 97;
            if (rem2[cIdx] > 0) {
                rem2[cIdx]--;
            } else {
                possiblePrefix = false;
                break;
            }
        }

        if (!possiblePrefix) continue;

        const targetCharIdx = target.charCodeAt(i) - 97;
        for (let cIdx = targetCharIdx + 1; cIdx < 26; cIdx++) {
            if (rem2[cIdx] > 0) {
                let resPrefix = target.substring(0, i) + String.fromCharCode(cIdx + 97);
                const tempRem = [...rem2];
                tempRem[cIdx]--;
                for (let j = i + 1; j < m; j++) {
                    for (let k = 0; k < 26; k++) {
                        if (tempRem[k] > 0) {
                            tempRem[k]--;
                            resPrefix += String.fromCharCode(k + 97);
                            break;
                        }
                    }
                }
                const mid = (n % 2 === 1) ? oddChar : "";
                return resPrefix + mid + resPrefix.split('').reverse().join('');
            }
        }
    }

    return "";
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
     * @param String $target
     * @return String
     */
    function lexPalindromicPermutation($s, $target) {
        $n = strlen($s);
        $counts = array_fill(0, 26, 0);
        for ($i = 0; $i < $n; $i++) {
            $counts[ord($s[$i]) - 97]++;
        }

        $oddCount = 0;
        $oddChar = '';
        for ($i = 0; $i < 26; $i++) {
            if ($counts[$i] % 2 !== 0) {
                $oddCount++;
                $oddChar = chr($i + 97);
            }
        }

        if ($oddCount !== ($n % 2)) return "";

        $halfCounts = array_fill(0, 26, 0);
        for ($i = 0; $i < 26; $i++) {
            $halfCounts[$i] = (int)($counts[$i] / 2);
        }

        $m = (int)($n / 2);

        // Case 1: Match first half of target exactly
        $rem = $halfCounts;
        $possible = true;
        for ($i = 0; $i < $m; $i++) {
            $cIdx = ord($target[$i]) - 97;
            if ($rem[$cIdx] > 0) $rem[$cIdx]--;
            else { $possible = false; break; }
        }
        if ($possible) {
            $prefix = substr($target, 0, $m);
            $p = $prefix . ($n % 2 === 1 ? $oddChar : "") . strrev($prefix);
            if ($p > $target) return $p;
        }

        // Case 2: Search for the first divergence to get greater string
        for ($i = $m - 1; $i >= 0; $i--) {
            $rem = $halfCounts;
            $possiblePrefix = true;
            for ($j = 0; $j < $i; $j++) {
                $cIdx = ord($target[$j]) - 97;
                if ($rem[$cIdx] > 0) $rem[$cIdx]--;
                else { $possiblePrefix = false; break; }
            }
            if (!$possiblePrefix) continue;

            $targetCharIdx = ord($target[$i]) - 97;
            for ($cIdx = $targetCharIdx + 1; $cIdx < 26; $cIdx++) {
                if ($rem[$cIdx] > 0) {
                    $resPrefix = substr($target, 0, $i) . chr($cIdx + 97);
                    $tempRem = $rem;
                    $tempRem[$cIdx]--;
                    for ($j = $i + 1; $j < $m; $j++) {
                        for ($k = 0; $k < 26; $k++) {
                            if ($tempRem[$k] > 0) {
                                $tempRem[$k]--;
                                $resPrefix .= chr($k + 97);
                                break;
                            }
                        }
                    }
                    return $resPrefix . ($n % 2 === 1 ? $oddChar : "") . strrev($resPrefix);
                }
            }
        }

        return "";
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func lexPalindromicPermutation(_ s: String, _ target: String) -> String {
        let n = s.count
        let sChars = Array(s)
        let tChars = Array(target)
        var counts = [Int](repeating: 0, count: 26)
        let aValue = Int(Character("a").asciiValue!)

        for char in sChars {
            counts[Int(char.asciiValue!) - aValue] += 1
        }

        var oddCount = 0
        var oddChar = Character(" ")
        for i in 0..<26 {
            if counts[i] % 2 != 0 {
                oddCount += 1
                oddChar = Character(UnicodeScalar(i + aValue)!)
            }
        }

        if oddCount != (n % 2) {
            return ""
        }

        var halfCounts = [Int](repeating: 0, count: 26)
        for i in 0..<26 {
            halfCounts[i] = counts[i] / 2
        }

        let m = n / 2

        // Case 1: Try construction matching target's prefix exactly
        var rem1 = halfCounts
        var possible1 = true
        for i in 0..<m {
            let cIdx = Int(tChars[i].asciiValue!) - aValue
            if rem1[cIdx] > 0 {
                rem1[cIdx] -= 1
            } else {
                possible1 = false
                break
            }
        }

        if possible1 {
            let prefix = String(tChars[0..<m])
            let mid = (n % 2 == 1) ? String(oddChar) : ""
            let p = prefix + mid + String(prefix.reversed())
            if p > target {
                return p
            }
        }

        // Case 2: Greedily find the smallest strictly greater first half
        for i in stride(from: m - 1, through: 0, by: -1) {
            var rem2 = halfCounts
            var possiblePrefix = true
            for j in 0..<i {
                let cIdx = Int(tChars[j].asciiValue!) - aValue
                if rem2[cIdx] > 0 {
                    rem2[cIdx] -= 1
                } else {
                    possiblePrefix = false
                    break
                }
            }

            if !possiblePrefix { continue }

            let targetCharIdx = Int(tChars[i].asciiValue!) - aValue
            for cIdx in (targetCharIdx + 1)..<26 {
                if rem2[cIdx] > 0 {
                    var resPrefixChars = Array(tChars[0..<i])
                    resPrefixChars.append(Character(UnicodeScalar(cIdx + aValue)!))
                    var tempRem = rem2
                    tempRem[cIdx] -= 1

                    for _ in (i + 1)..<m {
                        for k in 0..<26 {
                            if tempRem[k] > 0 {
                                tempRem[k] -= 1
                                resPrefixChars.append(Character(UnicodeScalar(k + aValue)!))
                                break
                            }
                        }
                    }

                    let resPrefix = String(resPrefixChars)
                    let mid = (n % 2 == 1) ? String(oddChar) : ""
                    return resPrefix + mid + String(resPrefix.reversed())
                }
            }
        }

        return ""
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun lexPalindromicPermutation(s: String, target: String): String {
        val n = s.length
        val counts = IntArray(26)
        for (char in s) {
            counts[char - 'a']++
        }

        var oddCount = 0
        var oddChar = ' '
        for (i in 0 until 26) {
            if (counts[i] % 2 != 0) {
                oddCount++
                oddChar = (i + 'a'.toInt()).toChar()
            }
        }

        if (oddCount != n % 2) return ""

        val halfCounts = IntArray(26)
        for (i in 0 until 26) {
            halfCounts[i] = counts[i] / 2
        }

        val m = n / 2

        // Case 1: Match first half of target exactly if possible
        val rem1 = halfCounts.clone()
        var possible1 = true
        for (i in 0 until m) {
            val cIdx = target[i] - 'a'
            if (cIdx in 0..25 && rem1[cIdx] > 0) {
                rem1[cIdx]--
            } else {
                possible1 = false
                break
            }
        }

        if (possible1) {
            val prefix = target.substring(0, m)
            val mid = if (n % 2 == 1) oddChar.toString() else ""
            val p = prefix + mid + prefix.reversed()
            if (p > target) return p
        }

        // Case 2: Greedily search for divergence point to build lexicographically smallest string > target
        for (i in m - 1 downTo 0) {
            val rem2 = halfCounts.clone()
            var possiblePrefix = true
            for (j in 0 until i) {
                val cIdx = target[j] - 'a'
                if (rem2[cIdx] > 0) {
                    rem2[cIdx]--
                } else {
                    possiblePrefix = false
                    break
                }
            }

            if (!possiblePrefix) continue

            val targetCharIdx = target[i] - 'a'
            for (cIdx in targetCharIdx + 1 until 26) {
                if (rem2[cIdx] > 0) {
                    val sb = StringBuilder()
                    sb.append(target.substring(0, i))
                    sb.append(('a' + cIdx))
                    val currentRem = rem2.clone()
                    currentRem[cIdx]--

                    for (j in i + 1 until m) {
                        for (k in 0 until 26) {
                            if (currentRem[k] > 0) {
                                currentRem[k]--
                                sb.append(('a' + k))
                                break
                            }
                        }
                    }

                    val resPrefix = sb.toString()
                    val mid = if (n % 2 == 1) oddChar.toString() else ""
                    return resPrefix + mid + resPrefix.reversed()
                }
            }
        }

        return ""
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  String lexPalindromicPermutation(String s, String target) {
    int n = s.length;
    int m = n ~/ 2;
    List<int> counts = List.filled(26, 0);
    for (int i = 0; i < n; i++) {
      counts[s.codeUnitAt(i) - 97]++;
    }

    int oddCount = 0;
    String midChar = "";
    for (int i = 0; i < 26; i++) {
      if (counts[i] % 2 == 1) {
        oddCount++;
        midChar = String.fromCharCode(97 + i);
      }
    }

    if ((n % 2 == 0 && oddCount != 0) || (n % 2 == 1 && oddCount != 1)) {
      return "";
    }

    List<int> halfCounts = List.generate(26, (i) => counts[i] ~/ 2);

    String pPrefix1 = target.substring(0, m);
    List<int> rem1 = List.from(halfCounts);
    bool possible1 = true;
    for (int i = 0; i < pPrefix1.length; i++) {
      int idx = pPrefix1.codeUnitAt(i) - 97;
      if (rem1[idx] > 0) {
        rem1[idx]--;
      } else {
        possible1 = false;
        break;
      }
    }

    if (possible1) {
      String full = pPrefix1 + midChar + pPrefix1.split('').reversed.join('');
      if (full.compareTo(target) > 0) {
        return full;
      }
    }

    for (int i = m - 1; i >= 0; i--) {
      String prefix = target.substring(0, i);
      List<int> rem2 = List.from(halfCounts);
      bool possible2 = true;
      for (int j = 0; j < i; j++) {
        int idx = target.codeUnitAt(j) - 97;
        if (rem2[idx] > 0) {
          rem2[idx]--;
        } else {
          possible2 = false;
          break;
        }
      }

      if (!possible2) continue;

      for (int cIdx = target.codeUnitAt(i) - 97 + 1; cIdx < 26; cIdx++) {
        if (rem2[cIdx] > 0) {
          StringBuffer sb = StringBuffer(prefix);
          sb.write(String.fromCharCode(97 + cIdx));
          List<int> rem3 = List.from(rem2);
          rem3[cIdx]--;
          for (int j = 0; j < 26; j++) {
            while (rem3[j] > 0) {
              sb.write(String.fromCharCode(97 + j));
              rem3[j]--;
            }
          }
          String firstHalf = sb.toString();
          return firstHalf + midChar + firstHalf.split('').reversed.join('');
        }
      }
    }

    return "";
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func lexPalindromicPermutation(s string, target string) string {
	n := len(s)
	m := n / 2
	counts := make([]int, 26)
	for i := 0; i < n; i++ {
		counts[s[i]-'a']++
	}

	oddCount := 0
	midChar := ""
	for i := 0; i < 26; i++ {
		if counts[i]%2 == 1 {
			oddCount++
			midChar = string(rune('a' + i))
		}
	}

	if (n%2 == 0 && oddCount != 0) || (n%2 == 1 && oddCount != 1) {
		return ""
	}

	halfCounts := make([]int, 26)
	for i := 0; i < 26; i++ {
		halfCounts[i] = counts[i] / 2
	}

	pPrefix1 := target[:m]
	rem1 := make([]int, 26)
	copy(rem1, halfCounts)
	possible1 := true
	for i := 0; i < len(pPrefix1); i++ {
		idx := pPrefix1[i] - 'a'
		if rem1[idx] > 0 {
			rem1[idx]--
		} else {
			possible1 = false
			break
		}
	}

	if possible1 {
		full := pPrefix1 + midChar + reverse(pPrefix1)
		if full > target {
			return full
		}
	}

	for i := m - 1; i >= 0; i-- {
		prefix := target[:i]
		rem2 := make([]int, 26)
		copy(rem2, halfCounts)
		possible2 := true
		for j := 0; j < i; j++ {
			idx := target[j] - 'a'
			if rem2[idx] > 0 {
				rem2[idx]--
			} else {
				possible2 = false
				break
			}
		}

		if !possible2 {
			continue
		}

		for cIdx := int(target[i]-'a') + 1; cIdx < 26; cIdx++ {
			if rem2[cIdx] > 0 {
				res := make([]byte, 0, m)
				res = append(res, []byte(prefix)...)
				res = append(res, byte('a'+cIdx))
				rem3 := make([]int, 26)
				copy(rem3, rem2)
				rem3[cIdx]--
				for j := 0; j < 26; j++ {
					for rem3[j] > 0 {
						res = append(res, byte('a'+j))
						rem3[j]--
					}
				}
				firstHalf := string(res)
				return firstHalf + midChar + reverse(firstHalf)
			}
		}
	}

	return ""
}

func reverse(s string) string {
	bytes := []byte(s)
	for i, j := 0, len(bytes)-1; i < j; i, j = i+1, j-1 {
		bytes[i], bytes[j] = bytes[j], bytes[i]
	}
	return string(bytes)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def lex_palindromic_permutation(s, target)
  n = s.length
  m = n / 2
  counts = Array.new(26, 0)
  s.each_char { |c| counts[c.ord - 'a'.ord] += 1 }

  odd_count = 0
  mid_char = ""
  (0...26).each do |i|
    if counts[i] % 2 == 1
      odd_count += 1
      mid_char = (i + 'a'.ord).chr
    end
  end

  return "" if (n % 2 == 0 && odd_count != 0) || (n % 2 == 1 && odd_count != 1)

  half_counts = counts.map { |v| v / 2 }

  p_prefix1 = target[0...m]
  rem1 = half_counts.dup
  possible1 = true
  p_prefix1.each_char do |c|
    idx = c.ord - 'a'.ord
    if rem1[idx] > 0
      rem1[idx] -= 1
    else
      possible1 = false
      break
    end
  end

  if possible1
    full = p_prefix1 + mid_char + p_prefix1.reverse
    return full if full > target
  end

  (m - 1).downto(0).each do |i|
    prefix = target[0...i]
    rem2 = half_counts.dup
    possible2 = true
    prefix.each_char do |c|
      idx = c.ord - 'a'.ord
      if rem2[idx] > 0
        rem2[idx] -= 1
      else
        possible2 = false
        break
      end
    end

    next unless possible2

    ((target[i].ord - 'a'.ord + 1)...26).each do |c_idx|
      if rem2[c_idx] > 0
        res_prefix = prefix + (c_idx + 'a'.ord).chr
        rem3 = rem2.dup
        rem3[c_idx] -= 1
        (0...26).each do |j|
          while rem3[j] > 0
            res_prefix += (j + 'a'.ord).chr
            rem3[j] -= 1
          end
        end
        return res_prefix + mid_char + res_prefix.reverse
      end
    end
  end

  ""
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def lexPalindromicPermutation(s: String, target: String): String = {
    val n = s.length
    val m = n / 2
    val counts = new Array[Int](26)
    for (c <- s) counts(c - 'a') += 1

    var oddCount = 0
    var midChar = ""
    for (i <- 0 until 26) {
      if (counts(i) % 2 == 1) {
        oddCount += 1
        midChar = (i + 'a').toChar.toString
      }
    }

    if ((n % 2 == 0 && oddCount != 0) || (n % 2 == 1 && oddCount != 1)) return ""

    val halfCounts = counts.map(_ / 2)

    val pPrefix1 = target.substring(0, m)
    val rem1 = halfCounts.clone()
    var possible1 = true
    for (c <- pPrefix1) {
      val idx = c - 'a'
      if (rem1(idx) > 0) rem1(idx) -= 1
      else possible1 = false
    }
    if (possible1) {
      val full = pPrefix1 + midChar + pPrefix1.reverse
      if (full.compareTo(target) > 0) return full
    }

    for (i <- m - 1 to 0 by -1) {
      val prefix = target.substring(0, i)
      val rem2 = halfCounts.clone()
      var possible2 = true
      for (j <- 0 until i) {
        val idx = target.charAt(j) - 'a'
        if (rem2(idx) > 0) rem2(idx) -= 1
        else possible2 = false
      }

      if (possible2) {
        for (cIdx <- (target.charAt(i) - 'a' + 1) until 26) {
          if (rem2(cIdx) > 0) {
            val sb = new StringBuilder(prefix)
            sb.append((cIdx + 'a').toChar)
            val rem3 = rem2.clone()
            rem3(cIdx) -= 1
            for (j <- 0 until 26) {
              while (rem3(j) > 0) {
                sb.append((j + 'a').toChar)
                rem3(j) -= 1
              }
            }
            val firstHalf = sb.toString()
            return firstHalf + midChar + firstHalf.reverse
          }
        }
      }
    }

    ""
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn lex_palindromic_permutation(s: String, target: String) -> String {
        let n = s.len();
        let mut counts = [0; 26];
        for b in s.bytes() {
            counts[(b - b'a') as usize] += 1;
        }
        let mut odd_count = 0;
        let mut mid_char = None;
        for i in 0..26 {
            if counts[i] % 2 != 0 {
                odd_count += 1;
                mid_char = Some((b'a' + i as u8) as char);
            }
        }
        if odd_count > 1 || (n % 2 == 0 && odd_count > 0) {
            return "".to_string();
        }

        let mut half_counts = [0; 26];
        for i in 0..26 {
            half_counts[i] = counts[i] / 2;
        }

        let m = n / 2;
        let target_bytes = target.as_bytes();

        let mut can_match_prefix = true;
        let mut temp_counts = half_counts;
        for i in 0..m {
            let idx = (target_bytes[i] - b'a') as usize;
            if temp_counts[idx] > 0 {
                temp_counts[idx] -= 1;
            } else {
                can_match_prefix = false;
                break;
            }
        }

        if can_match_prefix {
            let mut s_base = target[..m].to_string();
            if let Some(c) = mid_char {
                s_base.push(c);
            }
            let first_half_rev: String = target[..m].chars().rev().collect();
            s_base.push_str(&first_half_rev);
            if s_base > target {
                return s_base;
            }
        }

        for i in (0..m).rev() {
            let mut current_counts = half_counts;
            let mut can_form = true;
            for j in 0..i {
                let idx = (target_bytes[j] - b'a') as usize;
                if current_counts[idx] > 0 {
                    current_counts[idx] -= 1;
                } else {
                    can_form = false;
                    break;
                }
            }
            if !can_form {
                continue;
            }

            for c_idx in (target_bytes[i] - b'a' + 1) as usize..26 {
                if current_counts[c_idx] > 0 {
                    let mut res_half = target[..i].to_string();
                    res_half.push((b'a' + c_idx as u8) as char);
                    let mut remaining_counts = current_counts;
                    remaining_counts[c_idx] -= 1;
                    for r_idx in 0..26 {
                        for _ in 0..remaining_counts[r_idx] {
                            res_half.push((b'a' + r_idx as u8) as char);
                        }
                    }
                    let mut res = res_half.clone();
                    if let Some(c) = mid_char {
                        res.push(c);
                    }
                    let first_half_rev: String = res_half.chars().rev().collect();
                    res.push_str(&first_half_rev);
                    return res;
                }
            }
        }

        "".to_string()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (lex-palindromic-permutation s target)
  (-> string? string? string?)
  (let* ([n (string-length s)]
         [counts (make-vector 26 0)])
    (for ([c (string->list s)])
      (let ([idx (- (char->integer c) (char->integer #\a))])
        (vector-set! counts idx (+ 1 (vector-ref counts idx)))))
    (let* ([odd-chars (filter (lambda (i) (odd? (vector-ref counts i))) (range 26))]
           [odd-count (length odd-chars)])
      (if (or (> odd-count 1) (and (even? n) (> odd-count 0)))
          ""
          (let* ([half-counts (make-vector 26 0)]
                 [mid-char (if (= odd-count 1)
                               (string (integer->char (+ (car odd-chars) (char->integer #\a))))
                               "")]
                 [m (quotient n 2)])
            (for ([i 26])
              (vector-set! half-counts i (quotient (vector-ref counts i) 2)))
            (define (can-form-prefix? prefix-list counts-vec)
              (let ([temp (vector-copy counts-vec)]
                    [ok #t])
                (for ([c prefix-list])
                  (let ([idx (- (char->integer c) (char->integer #\a))])
                    (if (> (vector-ref temp idx) 0)
                        (vector-set! temp idx (- (vector-ref temp idx) 1))
                        (set! ok #f))))
                (if ok temp #f)))
            (let ([target-list (string->list target)])
              (let* ([target-half-list (take target-list m)]
                     [base-counts (can-form-prefix? target-half-list half-counts)]
                     [s-base (if base-counts
                                 (let* ([h (substring target 0 m)])
                                   (string-append h mid-char (list->string (reverse (string->list h)))))
                                 #f)])
                (if (and s-base (string>? s-base target))
                    s-base
                    (let loop ([i (- m 1)])
                      (if (< i 0)
                          ""
                          (let* ([prefix-list (take target-list i)]
                                 [rem-counts (can-form-prefix? prefix-list half-counts)])
                            (if rem-counts
                                (let ([found-c (for/first ([c-idx (range (+ 1 (- (char->integer (list-ref target-list i)) (char->integer #\a))) 26)]
                                                          #:when (> (vector-ref rem-counts c-idx) 0))
                                                 c-idx)])
                                  (if found-c
                                      (let* ([prefix (substring target 0 i)]
                                             [char-i (string (integer->char (+ found-c (char->integer #\a))))]
                                             [final-counts (vector-copy rem-counts)])
                                        (vector-set! final-counts found-c (- (vector-ref final-counts found-c) 1))
                                        (let ([rest (list->string
                                                     (append-map (lambda (idx) (make-list (vector-ref final-counts idx) (integer->char (+ idx (char->integer #\a)))))
                                                                 (range 26)))])
                                          (let ([full-half (string-append prefix char-i rest)])
                                            (string-append full-half mid-char (list->string (reverse (string->list full-half)))))))
                                      (loop (- i 1))))
                                (loop (- i 1))))))))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec lex_palindromic_permutation(S :: unicode:unicode_binary(), Target :: unicode:unicode_binary()) -> unicode:unicode_binary().
lex_palindromic_permutation(S, Target) ->
    N = byte_size(S),
    SList = binary_to_list(S),
    Counts = lists:foldl(fun(C, Acc) -> maps:put(C, maps:get(C, Acc, 0) + 1, Acc) end, #{}, SList),
    Odds = [C || {C, V} <- maps:to_list(Counts), V rem 2 =/= 0],
    OddCount = length(Odds),
    case (OddCount > 1 orelse (N rem 2 == 0 andalso OddCount > 0)) of
        true -> <<>>;
        false ->
            MidChar = case Odds of [C] -> [C]; [] -> [] end,
            HalfCounts = maps:from_list([{C, V div 2} || {C, V} <- maps:to_list(Counts)]),
            M = N div 2,
            TargetList = binary_to_list(Target),
            TargetHalf = lists:sublist(TargetList, 1, M),
            SBase = case can_form(TargetHalf, HalfCounts) of
                {ok, _} -> 
                    Base = list_to_binary(TargetHalf ++ MidChar ++ lists:reverse(TargetHalf)),
                    case Base > Target of true -> Base; false -> nil end;
                fail -> nil
            end,
            case SBase of
                nil -> find_greedy(M - 1, TargetList, HalfCounts, MidChar, Target);
                Res -> Res
            end
    end.

can_form([], Counts) -> {ok, Counts};
can_form([H|T], Counts) ->
    case maps:get(H, Counts, 0) of
        V when V > 0 -> can_form(T, maps:put(H, V - 1, Counts));
        _ -> fail
    end.

find_greedy(-1, _, _, _, _) -> <<>>;
find_greedy(I, TargetList, HalfCounts, MidChar, Target) ->
    Prefix = lists:sublist(TargetList, 1, I),
    case can_form(Prefix, HalfCounts) of
        {ok, RemCounts} ->
            TargetI = lists:nth(I + 1, TargetList),
            case find_char(TargetI + 1, RemCounts) of
                {ok, C} ->
                    NewRem = maps:put(C, maps:get(C, RemCounts) - 1, RemCounts),
                    Rest = lists:flatmap(fun(RC) -> lists:duplicate(maps:get(RC, NewRem, 0), RC) end, lists:seq($a, $z)),
                    FullHalf = Prefix ++ [C] ++ Rest,
                    list_to_binary(FullHalf ++ MidChar ++ lists:reverse(FullHalf));
                nil -> find_greedy(I - 1, TargetList, HalfCounts, MidChar, Target)
            end;
        fail -> find_greedy(I - 1, TargetList, HalfCounts, MidChar, Target)
    end.

find_char(C, Counts) when C > $z -> nil;
find_char(C, Counts) ->
    case maps:get(C, Counts, 0) of
        V when V > 0 -> {ok, C};
        _ -> find_char(C + 1, Counts)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec lex_palindromic_permutation(s :: String.t, target :: String.t) :: String.t
  def lex_palindromic_permutation(s, target) do
    n = String.length(s)
    m = div(n, 2)
    s_chars = String.to_charlist(s)
    counts = Enum.reduce(s_chars, %{}, fn c, acc -> Map.update(acc, c, 1, &(&1 + 1)) end)
    odd_chars = Enum.filter(counts, fn {_, v} -> rem(v, 2) != 0 end)

    if length(odd_chars) > 1 or (rem(n, 2) == 0 and length(odd_chars) > 0) do
      ""
    else
      mid_char = case odd_chars do
        [{c, _}] -> <<c>>
        [] -> ""
      end
      half_counts = Enum.map(counts, fn {c, v} -> {c, div(v, 2)} end) |> Enum.into(%{})
      target_chars = String.to_charlist(target)
      target_half = Enum.take(target_chars, m)

      s_base = case can_form(target_half, half_counts) do
        {:ok, _} -> 
          h = List.to_string(target_half)
          res = h <> mid_char <> String.reverse(h)
          if res > target, do: res, else: nil
        _ -> nil
      end

      if s_base do
        s_base
      else
        find_greedy(m - 1, target_chars, half_counts, mid_char) || ""
      end
    end
  end

  defp can_form(chars, counts) do
    Enum.reduce_while(chars, counts, fn c, acc ->
      if Map.get(acc, c, 0) > 0 do
        {:cont, Map.update!(acc, c, &(&1 - 1))}
      else
        {:halt, nil}
      end
    end) |> case do
      nil -> :fail
      res -> {:ok, res}
    end
  end

  defp find_greedy(-1, _, _, _), do: nil
  defp find_greedy(i, target_chars, half_counts, mid_char) do
    prefix = Enum.take(target_chars, i)
    case can_form(prefix, half_counts) do
      {:ok, rem_counts} ->
        target_i = Enum.at(target_chars, i)
        res = Enum.find_value(?a..?z, fn c ->
          if c > target_i and Map.get(rem_counts, c, 0) > 0 do
            new_rem = Map.update!(rem_counts, c, &(&1 - 1))
            rest = Enum.map(?a..?z, fn rc ->
              String.duplicate(<<rc>>, Map.get(new_rem, rc, 0))
            end) |> Enum.join("")
            h = List.to_string(prefix) <> <<c>> <> rest
            h <> mid_char <> String.reverse(h)
          else
            nil
          end
        end)
        res || find_greedy(i - 1, target_chars, half_counts, mid_char)
      :fail -> find_greedy(i - 1, target_chars, half_counts, mid_char)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where $n$ is the length of the string. Counting characters takes $O(n)$, and constructing candidates involves iterating through the prefix length and a constant-sized alphabet ($26$ characters), resulting in $O(26 \cdot n)$ operations.
- **Space Complexity:** O(n) for storing the character frequencies and the resulting palindrome string. The alphabet size is constant ($O(26)$), so it does not scale with the input length.
