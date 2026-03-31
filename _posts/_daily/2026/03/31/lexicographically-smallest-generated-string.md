---
layout: post
title: "Lexicographically Smallest Generated String"
date: 2026-03-31 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["String", "Greedy", "String Matching"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/lexicographically-smallest-generated-string/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    string generateString(string str1, string\
        \ str2) {\n        int n = str1.length();\n        int m = str2.length();\n\
        \        int L = n + m - 1;\n        string res(L, '?');\n\n        for (int\
        \ i = 0; i < n; ++i) {\n            if (str1[i] == 'T') {\n                for\
        \ (int k = 0; k < m; ++k) {\n                    if (res[i + k] != '?' && res[i\
        \ + k] != str2[k]) return \"\";\n                    res[i + k] = str2[k];\n\
        \                }\n            }\n        }\n\n        vector<int> count_q(n,\
        \ 0);\n        vector<int> count_match(n, 0);\n        for (int i = 0; i < n;\
        \ ++i) {\n            for (int k = 0; k < m; ++k) {\n                if (res[i\
        \ + k] == '?') count_q[i]++;\n                else if (res[i + k] == str2[k])\
        \ count_match[i]++;\n            }\n            if (str1[i] == 'F' && count_q[i]\
        \ == 0 && count_match[i] == m) return \"\";\n        }\n\n        for (int j\
        \ = 0; j < L; ++j) {\n            if (res[j] == '?') {\n                int\
        \ forbidden = 0;\n                int start_i = max(0, j - m + 1);\n       \
        \         int end_i = min(j, n - 1);\n                for (int i = start_i;\
        \ i <= end_i; ++i) {\n                    if (str1[i] == 'F' && count_q[i] ==\
        \ 1 && count_match[i] == m - 1) {\n                        forbidden |= (1 <<\
        \ (str2[j - i] - 'a'));\n                    }\n                }\n        \
        \        int chosen_c = -1;\n                for (int k = 0; k < 26; ++k) {\n\
        \                    if (!(forbidden & (1 << k))) {\n                      \
        \  chosen_c = k;\n                        break;\n                    }\n  \
        \              }\n                if (chosen_c == -1) return \"\";\n       \
        \         res[j] = 'a' + chosen_c;\n                for (int i = start_i; i\
        \ <= end_i; ++i) {\n                    count_q[i]--;\n                    if\
        \ (res[j] == str2[j - i]) count_match[i]++;\n                }\n           \
        \ }\n        }\n        return res;\n    }\n};"
      java: "class Solution {\n    public String generateString(String str1, String\
        \ str2) {\n        int n = str1.length();\n        int m = str2.length();\n\
        \        int L = n + m - 1;\n        char[] res = new char[L];\n        for\
        \ (int i = 0; i < L; i++) res[i] = '?';\n\n        for (int i = 0; i < n; i++)\
        \ {\n            if (str1.charAt(i) == 'T') {\n                for (int k =\
        \ 0; k < m; k++) {\n                    if (res[i + k] != '?' && res[i + k]\
        \ != str2.charAt(k)) return \"\";\n                    res[i + k] = str2.charAt(k);\n\
        \                }\n            }\n        }\n\n        int[] count_q = new\
        \ int[n];\n        int[] count_match = new int[n];\n        for (int i = 0;\
        \ i < n; i++) {\n            for (int k = 0; k < m; k++) {\n               \
        \ if (res[i + k] == '?') count_q[i]++;\n                else if (res[i + k]\
        \ == str2.charAt(k)) count_match[i]++;\n            }\n            if (str1.charAt(i)\
        \ == 'F' && count_q[i] == 0 && count_match[i] == m) return \"\";\n        }\n\
        \n        for (int j = 0; j < L; j++) {\n            if (res[j] == '?') {\n\
        \                int forbidden = 0;\n                int start_i = Math.max(0,\
        \ j - m + 1);\n                int end_i = Math.min(j, n - 1);\n           \
        \     for (int i = start_i; i <= end_i; i++) {\n                    if (str1.charAt(i)\
        \ == 'F' && count_q[i] == 1 && count_match[i] == m - 1) {\n                \
        \        forbidden |= (1 << (str2.charAt(j - i) - 'a'));\n                 \
        \   }\n                }\n                int chosen_c = -1;\n             \
        \   for (int k = 0; k < 26; k++) {\n                    if ((forbidden & (1\
        \ << k)) == 0) {\n                        chosen_c = k;\n                  \
        \      break;\n                    }\n                }\n                if\
        \ (chosen_c == -1) return \"\";\n                res[j] = (char)('a' + chosen_c);\n\
        \                for (int i = start_i; i <= end_i; i++) {\n                \
        \    count_q[i]--;\n                    if (res[j] == str2.charAt(j - i)) count_match[i]++;\n\
        \                }\n            }\n        }\n        return new String(res);\n\
        \    }\n}"
      python: "class Solution(object):\n    def generateString(self, str1, str2):\n\
        \        n, m = len(str1), len(str2)\n        l = n + m - 1\n        res = ['?']\
        \ * l\n        str2_ints = [ord(c) - ord('a') for c in str2]\n\n        for\
        \ i in range(n):\n            if str1[i] == 'T':\n                for k in range(m):\n\
        \                    if res[i + k] != '?' and res[i + k] != str2[k]:\n     \
        \                   return \"\"\n                    res[i + k] = str2[k]\n\n\
        \        count_q, count_match = [0] * n, [0] * n\n        for i in range(n):\n\
        \            for k in range(m):\n                if res[i + k] == '?':\n   \
        \                 count_q[i] += 1\n                elif res[i + k] == str2[k]:\n\
        \                    count_match[i] += 1\n            if str1[i] == 'F' and\
        \ count_q[i] == 0 and count_match[i] == m:\n                return \"\"\n\n\
        \        for j in range(l):\n            if res[j] == '?':\n               \
        \ forbidden = 0\n                start_i = max(0, j - m + 1)\n             \
        \   end_i = min(j, n - 1)\n                for i in range(start_i, end_i + 1):\n\
        \                    if str1[i] == 'F' and count_q[i] == 1 and count_match[i]\
        \ == m - 1:\n                        forbidden |= (1 << str2_ints[j - i])\n\n\
        \                chosen_c = -1\n                for k in range(26):\n      \
        \              if not (forbidden & (1 << k)):\n                        chosen_c\
        \ = k\n                        break\n                if chosen_c == -1: return\
        \ \"\"\n                res[j] = chr(ord('a') + chosen_c)\n                for\
        \ i in range(start_i, end_i + 1):\n                    count_q[i] -= 1\n   \
        \                 if chosen_c == str2_ints[j - i]:\n                       \
        \ count_match[i] += 1\n        return \"\".join(res)"
      python3: "class Solution:\n    def generateString(self, str1: str, str2: str)\
        \ -> str:\n        n, m = len(str1), len(str2)\n        l = n + m - 1\n    \
        \    res = ['?'] * l\n        str2_ints = [ord(c) - ord('a') for c in str2]\n\
        \n        for i in range(n):\n            if str1[i] == 'T':\n             \
        \   for k in range(m):\n                    if res[i + k] != '?' and res[i +\
        \ k] != str2[k]:\n                        return \"\"\n                    res[i\
        \ + k] = str2[k]\n\n        count_q, count_match = [0] * n, [0] * n\n      \
        \  for i in range(n):\n            for k in range(m):\n                if res[i\
        \ + k] == '?':\n                    count_q[i] += 1\n                elif res[i\
        \ + k] == str2[k]:\n                    count_match[i] += 1\n            if\
        \ str1[i] == 'F' and count_q[i] == 0 and count_match[i] == m:\n            \
        \    return \"\"\n\n        for j in range(l):\n            if res[j] == '?':\n\
        \                forbidden = 0\n                start_i = max(0, j - m + 1)\n\
        \                end_i = min(j, n - 1)\n                for i in range(start_i,\
        \ end_i + 1):\n                    if str1[i] == 'F' and count_q[i] == 1 and\
        \ count_match[i] == m - 1:\n                        forbidden |= (1 << str2_ints[j\
        \ - i])\n\n                chosen_c = -1\n                for k in range(26):\n\
        \                    if not (forbidden & (1 << k)):\n                      \
        \  chosen_c = k\n                        break\n                if chosen_c\
        \ == -1: return \"\"\n                res[j] = chr(ord('a') + chosen_c)\n  \
        \              for i in range(start_i, end_i + 1):\n                    count_q[i]\
        \ -= 1\n                    if chosen_c == str2_ints[j - i]:\n             \
        \           count_match[i] += 1\n        return \"\".join(res)"
      c: "#define MAX(a, b) ((a) > (b) ? (a) : (b))\n#define MIN(a, b) ((a) < (b) ?\
        \ (a) : (b))\nchar* generateString(char* str1, char* str2) {\n    int n = strlen(str1),\
        \ m = strlen(str2);\n    int L = n + m - 1;\n    char* res = (char*)malloc(L\
        \ + 1);\n    for (int i = 0; i < L; i++) res[i] = '?';\n    res[L] = '\\0';\n\
        \n    for (int i = 0; i < n; i++) {\n        if (str1[i] == 'T') {\n       \
        \     for (int k = 0; k < m; k++) {\n                if (res[i + k] != '?' &&\
        \ res[i + k] != str2[k]) { free(res); return \"\"; }\n                res[i\
        \ + k] = str2[k];\n            }\n        }\n    }\n\n    int* cq = (int*)calloc(n,\
        \ sizeof(int));\n    int* cm = (int*)calloc(n, sizeof(int));\n    for (int i\
        \ = 0; i < n; i++) {\n        for (int k = 0; k < m; k++) {\n            if\
        \ (res[i + k] == '?') cq[i]++;\n            else if (res[i + k] == str2[k])\
        \ cm[i]++;\n        }\n        if (str1[i] == 'F' && cq[i] == 0 && cm[i] ==\
        \ m) { free(res); free(cq); free(cm); return \"\"; }\n    }\n\n    for (int\
        \ j = 0; j < L; j++) {\n        if (res[j] == '?') {\n            int forbidden\
        \ = 0;\n            int s_i = MAX(0, j - m + 1), e_i = MIN(j, n - 1);\n    \
        \        for (int i = s_i; i <= e_i; i++) {\n                if (str1[i] ==\
        \ 'F' && cq[i] == 1 && cm[i] == m - 1) forbidden |= (1 << (str2[j - i] - 'a'));\n\
        \            }\n            int chosen = -1;\n            for (int k = 0; k\
        \ < 26; k++) if (!(forbidden & (1 << k))) { chosen = k; break; }\n         \
        \   if (chosen == -1) { free(res); free(cq); free(cm); return \"\"; }\n    \
        \        res[j] = 'a' + chosen;\n            for (int i = s_i; i <= e_i; i++)\
        \ {\n                cq[i]--;\n                if (res[j] == str2[j - i]) cm[i]++;\n\
        \            }\n        }\n    }\n    free(cq); free(cm);\n    return res;\n\
        }"
      csharp: "public class Solution {\n    public string GenerateString(string str1,\
        \ string str2) {\n        int n = str1.Length, m = str2.Length;\n        int\
        \ L = n + m - 1;\n        char[] res = new char[L];\n        for (int i = 0;\
        \ i < L; i++) res[i] = '?';\n\n        for (int i = 0; i < n; i++) {\n     \
        \       if (str1[i] == 'T') {\n                for (int k = 0; k < m; k++) {\n\
        \                    if (res[i + k] != '?' && res[i + k] != str2[k]) return\
        \ \"\";\n                    res[i + k] = str2[k];\n                }\n    \
        \        }\n        }\n\n        int[] cq = new int[n], cm = new int[n];\n \
        \       for (int i = 0; i < n; i++) {\n            for (int k = 0; k < m; k++)\
        \ {\n                if (res[i + k] == '?') cq[i]++;\n                else if\
        \ (res[i + k] == str2[k]) cm[i]++;\n            }\n            if (str1[i] ==\
        \ 'F' && cq[i] == 0 && cm[i] == m) return \"\";\n        }\n\n        for (int\
        \ j = 0; j < L; j++) {\n            if (res[j] == '?') {\n                int\
        \ forbidden = 0;\n                int s_i = Math.Max(0, j - m + 1), e_i = Math.Min(j,\
        \ n - 1);\n                for (int i = s_i; i <= e_i; i++) {\n            \
        \        if (str1[i] == 'F' && cq[i] == 1 && cm[i] == m - 1)\n             \
        \           forbidden |= (1 << (str2[j - i] - 'a'));\n                }\n  \
        \              int chosen = -1;\n                for (int k = 0; k < 26; k++)\
        \ if ((forbidden & (1 << k)) == 0) { chosen = k; break; }\n                if\
        \ (chosen == -1) return \"\";\n                res[j] = (char)('a' + chosen);\n\
        \                for (int i = s_i; i <= e_i; i++) {\n                    cq[i]--;\n\
        \                    if (res[j] == str2[j - i]) cm[i]++;\n                }\n\
        \            }\n        }\n        return new string(res);\n    }\n}"
      javascript: "/**\n * @param {string} str1\n * @param {string} str2\n * @return\
        \ {string}\n */\nvar generateString = function(str1, str2) {\n    let n = str1.length,\
        \ m = str2.length, L = n + m - 1;\n    let res = new Array(L).fill('?');\n\n\
        \    for (let i = 0; i < n; i++) {\n        if (str1[i] === 'T') {\n       \
        \     for (let k = 0; k < m; k++) {\n                if (res[i + k] !== '?'\
        \ && res[i + k] !== str2[k]) return \"\";\n                res[i + k] = str2[k];\n\
        \            }\n        }\n    }\n\n    let cq = new Int32Array(n), cm = new\
        \ Int32Array(n);\n    for (let i = 0; i < n; i++) {\n        for (let k = 0;\
        \ k < m; k++) {\n            if (res[i + k] === '?') cq[i]++;\n            else\
        \ if (res[i + k] === str2[k]) cm[i]++;\n        }\n        if (str1[i] === 'F'\
        \ && cq[i] === 0 && cm[i] === m) return \"\";\n    }\n\n    for (let j = 0;\
        \ j < L; j++) {\n        if (res[j] === '?') {\n            let forbidden =\
        \ 0;\n            let s_i = Math.max(0, j - m + 1), e_i = Math.min(j, n - 1);\n\
        \            for (let i = s_i; i <= e_i; i++) {\n                if (str1[i]\
        \ === 'F' && cq[i] === 1 && cm[i] === m - 1) {\n                    forbidden\
        \ |= (1 << (str2.charCodeAt(j - i) - 97));\n                }\n            }\n\
        \            let chosen = -1;\n            for (let k = 0; k < 26; k++) if (!(forbidden\
        \ & (1 << k))) { chosen = k; break; }\n            if (chosen === -1) return\
        \ \"\";\n            res[j] = String.fromCharCode(97 + chosen);\n          \
        \  for (let i = s_i; i <= e_i; i++) {\n                cq[i]--;\n          \
        \      if (res[j] === str2[i + (j - i) - i] && res[j] === str2[j - i]) cm[i]++;\n\
        \            }\n        }\n    }\n    return res.join('');\n};"
      typescript: "function generateString(str1: string, str2: string): string {\n \
        \   const n = str1.length;\n    const m = str2.length;\n    const L = n + m\
        \ - 1;\n\n    const fixed: (string | null)[] = new Array(L).fill(null);\n  \
        \  for (let i = 0; i < n; i++) {\n        if (str1[i] === 'T') {\n         \
        \   for (let j = 0; j < m; j++) {\n                if (fixed[i + j] !== null\
        \ && fixed[i + j] !== str2[j]) return \"\";\n                fixed[i + j] =\
        \ str2[j];\n            }\n        }\n    }\n\n    const pi = new Int32Array(m);\n\
        \    for (let i = 1; i < m; i++) {\n        let j = pi[i - 1];\n        while\
        \ (j > 0 && str2[i] !== str2[j]) j = pi[j - 1];\n        if (str2[i] === str2[j])\
        \ j++;\n        pi[i] = j;\n    }\n\n    const nxt_state = new Int32Array(m\
        \ * 26);\n    const is_nj_m = new Uint8Array(m * 26);\n    for (let j = 0; j\
        \ < m; j++) {\n        for (let c = 0; c < 26; c++) {\n            const char\
        \ = String.fromCharCode(97 + c);\n            let nj = j;\n            while\
        \ (nj > 0 && char !== str2[nj]) nj = pi[nj - 1];\n            if (char === str2[nj])\
        \ nj++;\n\n            if (nj === m) {\n                is_nj_m[j * 26 + c]\
        \ = 1;\n                nxt_state[j * 26 + c] = pi[m - 1];\n            } else\
        \ {\n                is_nj_m[j * 26 + c] = 0;\n                nxt_state[j *\
        \ 26 + c] = nj;\n            }\n        }\n    }\n\n    const dp = new Uint8Array((L\
        \ + 1) * m);\n    for (let j = 0; j < m; j++) dp[L * m + j] = 1;\n\n    for\
        \ (let i = L - 1; i >= 0; i--) {\n        const cond_T = (i >= m - 1 && str1[i\
        \ - m + 1] === 'T');\n        const cond_F = (i >= m - 1 && str1[i - m + 1]\
        \ === 'F');\n        for (let j = 0; j < m; j++) {\n            if (fixed[i]\
        \ !== null) {\n                const c = fixed[i]!.charCodeAt(0) - 97;\n   \
        \             const nj_m = is_nj_m[j * 26 + c];\n                if ((!cond_T\
        \ || nj_m) && (!cond_F || !nj_m)) {\n                    if (dp[(i + 1) * m\
        \ + nxt_state[j * 26 + c]]) dp[i * m + j] = 1;\n                }\n        \
        \    } else {\n                for (let c = 0; c < 26; c++) {\n            \
        \        const nj_m = is_nj_m[j * 26 + c];\n                    if ((!cond_T\
        \ || nj_m) && (!cond_F || !nj_m)) {\n                        if (dp[(i + 1)\
        \ * m + nxt_state[j * 26 + c]]) {\n                            dp[i * m + j]\
        \ = 1;\n                            break;\n                        }\n    \
        \                }\n                }\n            }\n        }\n    }\n\n \
        \   if (!dp[0]) return \"\";\n    let curr_j = 0;\n    let res = \"\";\n   \
        \ for (let i = 0; i < L; i++) {\n        const cond_T = (i >= m - 1 && str1[i\
        \ - m + 1] === 'T');\n        const cond_F = (i >= m - 1 && str1[i - m + 1]\
        \ === 'F');\n        let found = false;\n        for (let c = 0; c < 26; c++)\
        \ {\n            const char = String.fromCharCode(97 + c);\n            if (fixed[i]\
        \ !== null && fixed[i] !== char) continue;\n\n            const nj_m = is_nj_m[curr_j\
        \ * 26 + c];\n            if ((!cond_T || nj_m) && (!cond_F || !nj_m)) {\n \
        \               const nj = nxt_state[curr_j * 26 + c];\n                if (dp[(i\
        \ + 1) * m + nj]) {\n                    res += char;\n                    curr_j\
        \ = nj;\n                    found = true;\n                    break;\n   \
        \             }\n            }\n        }\n        if (!found) return \"\";\n\
        \    }\n    return res;\n}"
      php: "class Solution {\n    function generateString($str1, $str2) {\n        $n\
        \ = strlen($str1);\n        $m = strlen($str2);\n        $L = $n + $m - 1;\n\
        \        $fixed = str_repeat(\"\\0\", $L);\n        for ($i = 0; $i < $n; $i++)\
        \ {\n            if ($str1[$i] === 'T') {\n                for ($j = 0; $j <\
        \ $m; $j++) {\n                    if ($fixed[$i + $j] !== \"\\0\" && $fixed[$i\
        \ + $j] !== $str2[$j]) return \"\";\n                    $fixed[$i + $j] = $str2[$j];\n\
        \                }\n            }\n        }\n        $pi = array_fill(0, $m,\
        \ 0);\n        for ($i = 1; $i < $m; $i++) {\n            $j = $pi[$i - 1];\n\
        \            while ($j > 0 && $str2[$i] !== $str2[$j]) $j = $pi[$j - 1];\n \
        \           if ($str2[$i] === $str2[$j]) $j++;\n            $pi[$i] = $j;\n\
        \        }\n        $nxt_state = new SplFixedArray($m * 26);\n        $is_nj_m\
        \ = new SplFixedArray($m * 26);\n        for ($j = 0; $j < $m; $j++) {\n   \
        \         for ($c = 0; $c < 26; $c++) {\n                $char = chr(97 + $c);\n\
        \                $nj = $j;\n                while ($nj > 0 && $char !== $str2[$nj])\
        \ $nj = $pi[$nj - 1];\n                if ($char === $str2[$nj]) $nj++;\n  \
        \              if ($nj === $m) {\n                    $is_nj_m[$j * 26 + $c]\
        \ = true;\n                    $nxt_state[$j * 26 + $c] = $pi[$m - 1];\n   \
        \             } else {\n                    $is_nj_m[$j * 26 + $c] = false;\n\
        \                    $nxt_state[$j * 26 + $c] = $nj;\n                }\n  \
        \          }\n        }\n        $dp = str_repeat(\"\\0\", ($L + 1) * $m);\n\
        \        for ($j = 0; $j < $m; $j++) $dp[$L * $m + $j] = \"\\1\";\n        for\
        \ ($i = $L - 1; $i >= 0; $i--) {\n            $cond_T = ($i >= $m - 1 && $str1[$i\
        \ - $m + 1] === 'T');\n            $cond_F = ($i >= $m - 1 && $str1[$i - $m\
        \ + 1] === 'F');\n            for ($j = 0; $j < $m; $j++) {\n              \
        \  if ($fixed[$i] !== \"\\0\") {\n                    $c = ord($fixed[$i]) -\
        \ 97;\n                    $nj_m = $is_nj_m[$j * 26 + $c];\n               \
        \     if ((!$cond_T || $nj_m) && (!$cond_F || !$nj_m)) {\n                 \
        \       if ($dp[($i + 1) * $m + $nxt_state[$j * 26 + $c]] === \"\\1\") $dp[$i\
        \ * $m + $j] = \"\\1\";\n                    }\n                } else {\n \
        \                   for ($c = 0; $c < 26; $c++) {\n                        $nj_m\
        \ = $is_nj_m[$j * 26 + $c];\n                        if ((!$cond_T || $nj_m)\
        \ && (!$cond_F || !$nj_m)) {\n                            if ($dp[($i + 1) *\
        \ $m + $nxt_state[$j * 26 + $c]] === \"\\1\") {\n                          \
        \      $dp[$i * $m + $j] = \"\\1\";\n                                break;\n\
        \                            }\n                        }\n                \
        \    }\n                }\n            }\n        }\n        if ($dp[0] ===\
        \ \"\\0\") return \"\";\n        $curr_j = 0; $res = [];\n        for ($i =\
        \ 0; $i < $L; $i++) {\n            $cond_T = ($i >= $m - 1 && $str1[$i - $m\
        \ + 1] === 'T');\n            $cond_F = ($i >= $m - 1 && $str1[$i - $m + 1]\
        \ === 'F');\n            for ($c = 0; $c < 26; $c++) {\n                $char\
        \ = chr(97 + $c);\n                if ($fixed[$i] !== \"\\0\" && $fixed[$i]\
        \ !== $char) continue;\n                $nj_m = $is_nj_m[$curr_j * 26 + $c];\n\
        \                if ((!$cond_T || $nj_m) && (!$cond_F || !$nj_m)) {\n      \
        \              $nj = $nxt_state[$curr_j * 26 + $c];\n                    if\
        \ ($dp[($i + 1) * $m + $nj] === \"\\1\") {\n                        $res[] =\
        \ $char;\n                        $curr_j = $nj;\n                        break;\n\
        \                    }\n                }\n            }\n        }\n      \
        \  return implode(\"\", $res);\n    }\n}"
      swift: "class Solution {\n    func generateString(_ str1: String, _ str2: String)\
        \ -> String {\n        let s1 = Array(str1), s2 = Array(str2)\n        let n\
        \ = s1.count, m = s2.count\n        let L = n + m - 1\n        var fixed = [Character?](repeating:\
        \ nil, count: L)\n        for i in 0..<n {\n            if s1[i] == \"T\" {\n\
        \                for j in 0..<m {\n                    if let f = fixed[i +\
        \ j], f != s2[j] { return \"\" }\n                    fixed[i + j] = s2[j]\n\
        \                }\n            }\n        }\n        var pi = [Int](repeating:\
        \ 0, count: m)\n        for i in 1..<m {\n            var j = pi[i - 1]\n  \
        \          while j > 0 && s2[i] != s2[j] { j = pi[j - 1] }\n            if s2[i]\
        \ == s2[j] { j += 1 }\n            pi[i] = j\n        }\n        var nxt_state\
        \ = [Int](repeating: 0, count: m * 26)\n        var is_nj_m = [Bool](repeating:\
        \ false, count: m * 26)\n        let chars = (0..<26).map { Character(UnicodeScalar(97\
        \ + $0)!) }\n        for j in 0..<m {\n            for c in 0..<26 {\n     \
        \           let char = chars[c]\n                var nj = j\n              \
        \  while nj > 0 && char != s2[nj] { nj = pi[nj - 1] }\n                if char\
        \ == s2[nj] { nj += 1 }\n                if nj == m {\n                    is_nj_m[j\
        \ * 26 + c] = true\n                    nxt_state[j * 26 + c] = pi[m - 1]\n\
        \                } else {\n                    is_nj_m[j * 26 + c] = false\n\
        \                    nxt_state[j * 26 + c] = nj\n                }\n       \
        \     }\n        }\n        var dp = [Bool](repeating: false, count: (L + 1)\
        \ * m)\n        for j in 0..<m { dp[L * m + j] = true }\n        for i in (0..<L).reversed()\
        \ {\n            let cond_T = (i >= m - 1 && s1[i - m + 1] == \"T\")\n     \
        \       let cond_F = (i >= m - 1 && s1[i - m + 1] == \"F\")\n            for\
        \ j in 0..<m {\n                if let f = fixed[i] {\n                    let\
        \ c = Int(f.asciiValue! - 97)\n                    let nj_m = is_nj_m[j * 26\
        \ + c]\n                    if (!cond_T || nj_m) && (!cond_F || !nj_m) {\n \
        \                       if dp[(i + 1) * m + nxt_state[j * 26 + c]] { dp[i *\
        \ m + j] = true }\n                    }\n                } else {\n       \
        \             for c in 0..<26 {\n                        let nj_m = is_nj_m[j\
        \ * 26 + c]\n                        if (!cond_T || nj_m) && (!cond_F || !nj_m)\
        \ {\n                            if dp[(i + 1) * m + nxt_state[j * 26 + c]]\
        \ {\n                                dp[i * m + j] = true\n                \
        \                break\n                            }\n                    \
        \    }\n                    }\n                }\n            }\n        }\n\
        \        if !dp[0] { return \"\" }\n        var curr_j = 0, res = \"\"\n   \
        \     for i in 0..<L {\n            let cond_T = (i >= m - 1 && s1[i - m + 1]\
        \ == \"T\")\n            let cond_F = (i >= m - 1 && s1[i - m + 1] == \"F\"\
        )\n            for c in 0..<26 {\n                let char = chars[c]\n    \
        \            if let f = fixed[i], f != char { continue }\n                let\
        \ nj_m = is_nj_m[curr_j * 26 + c]\n                if (!cond_T || nj_m) && (!cond_F\
        \ || !nj_m) {\n                    let nj = nxt_state[curr_j * 26 + c]\n   \
        \                 if dp[(i + 1) * m + nj] {\n                        res.append(char)\n\
        \                        curr_j = nj\n                        break\n      \
        \              }\n                }\n            }\n        }\n        return\
        \ res\n    }\n}"
      kotlin: "class Solution {\n    fun generateString(str1: String, str2: String):\
        \ String {\n        val n = str1.length\n        val m = str2.length\n     \
        \   val L = n + m - 1\n        val fixed = CharArray(L) { '\\u0000' }\n    \
        \    for (i in 0 until n) {\n            if (str1[i] == 'T') {\n           \
        \     for (j in 0 until m) {\n                    if (fixed[i + j] != '\\u0000'\
        \ && fixed[i + j] != str2[j]) return \"\"\n                    fixed[i + j]\
        \ = str2[j]\n                }\n            }\n        }\n        val pi = IntArray(m)\n\
        \        for (i in 1 until m) {\n            var j = pi[i - 1]\n           \
        \ while (j > 0 && str2[i] != str2[j]) j = pi[j - 1]\n            if (str2[i]\
        \ == str2[j]) j++\n            pi[i] = j\n        }\n        val nxtState =\
        \ IntArray(m * 26)\n        val isNjM = BooleanArray(m * 26)\n        for (j\
        \ in 0 until m) {\n            for (c in 0 until 26) {\n                val\
        \ char = ('a' + c)\n                var nj = j\n                while (nj >\
        \ 0 && char != str2[nj]) nj = pi[nj - 1]\n                if (char == str2[nj])\
        \ nj++\n                if (nj == m) {\n                    isNjM[j * 26 + c]\
        \ = true\n                    nxtState[j * 26 + c] = pi[m - 1]\n           \
        \     } else {\n                    isNjM[j * 26 + c] = false\n            \
        \        nxtState[j * 26 + c] = nj\n                }\n            }\n     \
        \   }\n        val dp = java.util.BitSet((L + 1) * m)\n        for (j in 0 until\
        \ m) dp.set(L * m + j)\n        for (i in L - 1 downTo 0) {\n            val\
        \ condT = i >= m - 1 && str1[i - m + 1] == 'T'\n            val condF = i >=\
        \ m - 1 && str1[i - m + 1] == 'F'\n            for (j in 0 until m) {\n    \
        \            if (fixed[i] != '\\u0000') {\n                    val c = fixed[i]\
        \ - 'a'\n                    val njM = isNjM[j * 26 + c]\n                 \
        \   if ((!condT || njM) && (!condF || !njM)) {\n                        if (dp.get((i\
        \ + 1) * m + nxtState[j * 26 + c])) dp.set(i * m + j)\n                    }\n\
        \                } else {\n                    for (c in 0 until 26) {\n   \
        \                     val njM = isNjM[j * 26 + c]\n                        if\
        \ ((!condT || njM) && (!condF || !njM)) {\n                            if (dp.get((i\
        \ + 1) * m + nxtState[j * 26 + c])) {\n                                dp.set(i\
        \ * m + j)\n                                break\n                        \
        \    }\n                        }\n                    }\n                }\n\
        \            }\n        }\n        if (!dp.get(0)) return \"\"\n        var\
        \ currJ = 0\n        val res = StringBuilder()\n        for (i in 0 until L)\
        \ {\n            val condT = i >= m - 1 && str1[i - m + 1] == 'T'\n        \
        \    val condF = i >= m - 1 && str1[i - m + 1] == 'F'\n            for (c in\
        \ 0 until 26) {\n                val char = ('a' + c)\n                if (fixed[i]\
        \ != '\\u0000' && fixed[i] != char) continue\n                val njM = isNjM[currJ\
        \ * 26 + c]\n                if ((!condT || njM) && (!condF || !njM)) {\n  \
        \                  val nj = nxtState[currJ * 26 + c]\n                    if\
        \ (dp.get((i + 1) * m + nj)) {\n                        res.append(char)\n \
        \                       currJ = nj\n                        break\n        \
        \            }\n                }\n            }\n        }\n        return\
        \ res.toString()\n    }\n}"
      dart: "import 'dart:typed_data';\n\nclass Solution {\n  String generateString(String\
        \ str1, String str2) {\n    int n = str1.length, m = str2.length, L = n + m\
        \ - 1;\n    List<String?> fixed = List.filled(L, null);\n    for (int i = 0;\
        \ i < n; i++) {\n      if (str1[i] == 'T') {\n        for (int j = 0; j < m;\
        \ j++) {\n          if (fixed[i + j] != null && fixed[i + j] != str2[j]) return\
        \ \"\";\n          fixed[i + j] = str2[j];\n        }\n      }\n    }\n    Int32List\
        \ pi = Int32List(m);\n    for (int i = 1; i < m; i++) {\n      int j = pi[i\
        \ - 1];\n      while (j > 0 && str2[i] != str2[j]) j = pi[j - 1];\n      if\
        \ (str2[i] == str2[j]) j++;\n      pi[i] = j;\n    }\n    Int32List nxtState\
        \ = Int32List(m * 26);\n    Uint8List isNjM = Uint8List(m * 26);\n    for (int\
        \ j = 0; j < m; j++) {\n      for (int c = 0; c < 26; c++) {\n        String\
        \ char = String.fromCharCode(97 + c);\n        int nj = j;\n        while (nj\
        \ > 0 && char != str2[nj]) nj = pi[nj - 1];\n        if (char == str2[nj]) nj++;\n\
        \        if (nj == m) {\n          isNjM[j * 26 + c] = 1;\n          nxtState[j\
        \ * 26 + c] = pi[m - 1];\n        } else {\n          isNjM[j * 26 + c] = 0;\n\
        \          nxtState[j * 26 + c] = nj;\n        }\n      }\n    }\n    Uint8List\
        \ dp = Uint8List((L + 1) * m);\n    for (int j = 0; j < m; j++) dp[L * m + j]\
        \ = 1;\n    for (int i = L - 1; i >= 0; i--) {\n      bool condT = (i >= m -\
        \ 1 && str1[i - m + 1] == 'T');\n      bool condF = (i >= m - 1 && str1[i -\
        \ m + 1] == 'F');\n      for (int j = 0; j < m; j++) {\n        if (fixed[i]\
        \ != null) {\n          int c = fixed[i]!.codeUnitAt(0) - 97;\n          bool\
        \ njM = isNjM[j * 26 + c] == 1;\n          if ((!condT || njM) && (!condF ||\
        \ !njM)) {\n            if (dp[(i + 1) * m + nxtState[j * 26 + c]] == 1) dp[i\
        \ * m + j] = 1;\n          }\n        } else {\n          for (int c = 0; c\
        \ < 26; c++) {\n            bool njM = isNjM[j * 26 + c] == 1;\n           \
        \ if ((!condT || njM) && (!condF || !njM)) {\n              if (dp[(i + 1) *\
        \ m + nxtState[j * 26 + c]] == 1) {\n                dp[i * m + j] = 1;\n  \
        \              break;\n              }\n            }\n          }\n       \
        \ }\n      }\n    }\n    if (dp[0] == 0) return \"\";\n    int currJ = 0; StringBuffer\
        \ res = StringBuffer();\n    for (int i = 0; i < L; i++) {\n      bool condT\
        \ = (i >= m - 1 && str1[i - m + 1] == 'T');\n      bool condF = (i >= m - 1\
        \ && str1[i - m + 1] == 'F');\n      for (int c = 0; c < 26; c++) {\n      \
        \  String char = String.fromCharCode(97 + c);\n        if (fixed[i] != null\
        \ && fixed[i] != char) continue;\n        bool njM = isNjM[currJ * 26 + c] ==\
        \ 1;\n        if ((!condT || njM) && (!condF || !njM)) {\n          int nj =\
        \ nxtState[currJ * 26 + c];\n          if (dp[(i + 1) * m + nj] == 1) {\n  \
        \          res.write(char); currJ = nj; break;\n          }\n        }\n   \
        \   }\n    }\n    return res.toString();\n  }\n}"
      go: "func generateString(str1 string, str2 string) string {\n\tn := len(str1)\n\
        \tm := len(str2)\n\tL := n + m - 1\n\tfixed := make([]byte, L)\n\tfor i := 0;\
        \ i < n; i++ {\n\t\tif str1[i] == 'T' {\n\t\t\tfor j := 0; j < m; j++ {\n\t\t\
        \t\tif fixed[i+j] != 0 && fixed[i+j] != str2[j] {\n\t\t\t\t\treturn \"\"\n\t\
        \t\t\t}\n\t\t\t\tfixed[i+j] = str2[j]\n\t\t\t}\n\t\t}\n\t}\n\tpi := make([]int,\
        \ m)\n\tfor i := 1; i < m; i++ {\n\t\tj := pi[i-1]\n\t\tfor j > 0 && str2[i]\
        \ != str2[j] {\n\t\t\tj = pi[j-1]\n\t\t}\n\t\tif str2[i] == str2[j] {\n\t\t\t\
        j++\n\t\t}\n\t\tpi[i] = j\n\t}\n\tnxtState := make([]int, m*26)\n\tisNjM :=\
        \ make([]bool, m*26)\n\tfor j := 0; j < m; j++ {\n\t\tfor c := 0; c < 26; c++\
        \ {\n\t\t\tchar := byte('a' + c)\n\t\t\tnj := j\n\t\t\tfor nj > 0 && char !=\
        \ str2[nj] {\n\t\t\t\tnj = pi[nj-1]\n\t\t\t}\n\t\t\tif char == str2[nj] {\n\t\
        \t\t\tnj++\n\t\t\t}\n\t\t\tif nj == m {\n\t\t\t\tisNjM[j*26+c] = true\n\t\t\t\
        \tnxtState[j*26+c] = pi[m-1]\n\t\t\t} else {\n\t\t\t\tisNjM[j*26+c] = false\n\
        \t\t\t\tnxtState[j*26+c] = nj\n\t\t\t}\n\t\t}\n\t}\n\tdp := make([]byte, (L+1)*m)\n\
        \tfor j := 0; j < m; j++ {\n\t\tdp[L*m+j] = 1\n\t}\n\tfor i := L - 1; i >= 0;\
        \ i-- {\n\t\tcondT := i >= m-1 && str1[i-m+1] == 'T'\n\t\tcondF := i >= m-1\
        \ && str1[i-m+1] == 'F'\n\t\tfor j := 0; j < m; j++ {\n\t\t\tif fixed[i] !=\
        \ 0 {\n\t\t\t\tc := int(fixed[i] - 'a')\n\t\t\t\tnjM := isNjM[j*26+c]\n\t\t\t\
        \tif (!condT || njM) && (!condF || !njM) {\n\t\t\t\t\tif dp[(i+1)*m+nxtState[j*26+c]]\
        \ == 1 {\n\t\t\t\t\t\tdp[i*m+j] = 1\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t} else {\n\
        \t\t\t\tfor c := 0; c < 26; c++ {\n\t\t\t\t\tnjM := isNjM[j*26+c]\n\t\t\t\t\t\
        if (!condT || njM) && (!condF || !njM) {\n\t\t\t\t\t\tif dp[(i+1)*m+nxtState[j*26+c]]\
        \ == 1 {\n\t\t\t\t\t\t\tdp[i*m+j] = 1\n\t\t\t\t\t\t\tbreak\n\t\t\t\t\t\t}\n\t\
        \t\t\t\t}\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\t}\n\tif dp[0] == 0 {\n\t\treturn \"\"\
        \n\t}\n\tvar res strings.Builder\n\tcurrJ := 0\n\tfor i := 0; i < L; i++ {\n\
        \t\tcondT := i >= m-1 && str1[i-m+1] == 'T'\n\t\tcondF := i >= m-1 && str1[i-m+1]\
        \ == 'F'\n\t\tfor c := 0; c < 26; c++ {\n\t\t\tchar := byte('a' + c)\n\t\t\t\
        if fixed[i] != 0 && fixed[i] != char {\n\t\t\t\tcontinue\n\t\t\t}\n\t\t\tnjM\
        \ := isNjM[currJ*26+c]\n\t\t\tif (!condT || njM) && (!condF || !njM) {\n\t\t\
        \t\tnj := nxtState[currJ*26+c]\n\t\t\t\tif dp[(i+1)*m+nj] == 1 {\n\t\t\t\t\t\
        res.WriteByte(char)\n\t\t\t\t\tcurrJ = nj\n\t\t\t\t\tbreak\n\t\t\t\t}\n\t\t\t\
        }\n\t\t}\n\t}\n\treturn res.String()\n}"
      ruby: '// Generation failed for Ruby

        // Reason: Parsing failed'
      scala: '// Generation failed for Scala

        // Reason: Parsing failed'
      rust: '// Generation failed for Rust

        // Reason: Parsing failed'
      racket: '// Generation failed for Racket

        // Reason: Parsing failed'
      erlang: '// Generation failed for Erlang

        // Reason: Parsing failed'
      elixir: '// Generation failed for Elixir

        // Reason: Parsing failed'
    approach: 'The algorithm follows a greedy approach combined with fixed-constraint
      satisfaction. First, we initialize a character array of length $n + m - 1$ with
      a placeholder. We iterate through `str1`, and for every index $i$ where `str1[i]
      == ''T''`, we fill the window starting at $i$ with `str2`. If we encounter any
      conflict (trying to overwrite a character with a different one), it''s impossible
      to satisfy the ''T'' constraints, so we return an empty string. After filling
      ''T'' constraints, we count the number of placeholder characters and matching
      characters in each window to pre-identify which ''F'' constraints are already
      satisfied or are at risk of being violated.


      Next, we greedily fill the remaining placeholder positions from left to right.
      For each placeholder at index $j$, we check all windows $i$ that cover $j$ where
      `str1[i] == ''F''`. If a window $i$ has only one placeholder left (at index $j$)
      and all its other characters already match `str2`, index $j$ becomes the ''last
      chance'' to satisfy that ''F'' constraint. We collect all characters that would
      cause a violation in such windows and pick the lexicographically smallest available
      character (''a'', ''b'', etc.) that is not forbidden. If all characters are forbidden,
      return an empty string. Finally, we perform a quick check to ensure no ''F'' constraint
      was violated by the initial ''T'' fills and return the resulting string.'
    time_complexity: O(nm) where $n$ is the length of `str1` and $m$ is the length of
      `str2`. Filling 'T' constraints, initializing window counters, and the greedy
      filling process each involve iterating over windows or positions at most $O(nm)$
      times.
    space_complexity: O(n + m) to store the result string of length $n + m - 1$, the
      counters for each window (length $n$), and auxiliary data structures for constraints.
    elapsed_time: 458.16304302215576
    model: gemini-3-flash-preview
    generated_at: '2026-03-31 05:56:25 '
---

## Problem #3474: Lexicographically Smallest Generated String

**Difficulty:** Hard

**Topics:** String, Greedy, String Matching

## Problem Description

<p>You are given two strings, <code>str1</code> and <code>str2</code>, of lengths <code>n</code> and <code>m</code>, respectively.</p>

<p>A string <code>word</code> of length <code>n + m - 1</code> is defined to be <strong>generated</strong> by <code>str1</code> and <code>str2</code> if it satisfies the following conditions for <strong>each</strong> index <code>0 &lt;= i &lt;= n - 1</code>:</p>

<ul>
	<li>If <code>str1[i] == &#39;T&#39;</code>, the <strong><span data-keyword="substring-nonempty">substring</span></strong> of <code>word</code> with size <code>m</code> starting at index <code>i</code> is <strong>equal</strong> to <code>str2</code>, i.e., <code>word[i..(i + m - 1)] == str2</code>.</li>
	<li>If <code>str1[i] == &#39;F&#39;</code>, the <strong><span data-keyword="substring-nonempty">substring</span></strong> of <code>word</code> with size <code>m</code> starting at index <code>i</code> is <strong>not equal</strong> to <code>str2</code>, i.e., <code>word[i..(i + m - 1)] != str2</code>.</li>
</ul>

<p>Return the <strong><span data-keyword="lexicographically-smaller-string">lexicographically smallest</span></strong> possible string that can be <strong>generated</strong> by <code>str1</code> and <code>str2</code>. If no string can be generated, return an empty string <code>&quot;&quot;</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">str1 = &quot;TFTF&quot;, str2 = &quot;ab&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;ababa&quot;</span></p>

<p><strong>Explanation:</strong></p>

<h4>The table below represents the string <code>&quot;ababa&quot;</code></h4>

<table>
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Index</th>
			<th style="border: 1px solid black;">T/F</th>
			<th style="border: 1px solid black;">Substring of length <code>m</code></th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;"><code>&#39;T&#39;</code></td>
			<td style="border: 1px solid black;">&quot;ab&quot;</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;"><code>&#39;F&#39;</code></td>
			<td style="border: 1px solid black;">&quot;ba&quot;</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;"><code>&#39;T&#39;</code></td>
			<td style="border: 1px solid black;">&quot;ab&quot;</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;"><code>&#39;F&#39;</code></td>
			<td style="border: 1px solid black;">&quot;ba&quot;</td>
		</tr>
	</tbody>
</table>

<p>The strings <code>&quot;ababa&quot;</code> and <code>&quot;ababb&quot;</code> can be generated by <code>str1</code> and <code>str2</code>.</p>

<p>Return <code>&quot;ababa&quot;</code> since it is the lexicographically smaller string.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">str1 = &quot;TFTF&quot;, str2 = &quot;abc&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>No string that satisfies the conditions can be generated.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">str1 = &quot;F&quot;, str2 = &quot;d&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;a&quot;</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == str1.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= m == str2.length &lt;= 500</code></li>
	<li><code>str1</code> consists only of <code>&#39;T&#39;</code> or <code>&#39;F&#39;</code>.</li>
	<li><code>str2</code> consists only of lowercase English characters.</li>
</ul>


## Hints

1. Use dynamic programming.

2. Fill the fixed part.

3. Use KMP's next table for DP.

4. The state is the prefix length and the longest suffix length that matches the pattern.

5. Each unknown character can be selected from `['a', 'b']`.

6. Can you think of a greedy approach?

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm follows a greedy approach combined with fixed-constraint satisfaction. First, we initialize a character array of length $n + m - 1$ with a placeholder. We iterate through `str1`, and for every index $i$ where `str1[i] == 'T'`, we fill the window starting at $i$ with `str2`. If we encounter any conflict (trying to overwrite a character with a different one), it's impossible to satisfy the 'T' constraints, so we return an empty string. After filling 'T' constraints, we count the number of placeholder characters and matching characters in each window to pre-identify which 'F' constraints are already satisfied or are at risk of being violated.

Next, we greedily fill the remaining placeholder positions from left to right. For each placeholder at index $j$, we check all windows $i$ that cover $j$ where `str1[i] == 'F'`. If a window $i$ has only one placeholder left (at index $j$) and all its other characters already match `str2`, index $j$ becomes the 'last chance' to satisfy that 'F' constraint. We collect all characters that would cause a violation in such windows and pick the lexicographically smallest available character ('a', 'b', etc.) that is not forbidden. If all characters are forbidden, return an empty string. Finally, we perform a quick check to ensure no 'F' constraint was violated by the initial 'T' fills and return the resulting string.

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
    string generateString(string str1, string str2) {
        int n = str1.length();
        int m = str2.length();
        int L = n + m - 1;
        string res(L, '?');

        for (int i = 0; i < n; ++i) {
            if (str1[i] == 'T') {
                for (int k = 0; k < m; ++k) {
                    if (res[i + k] != '?' && res[i + k] != str2[k]) return "";
                    res[i + k] = str2[k];
                }
            }
        }

        vector<int> count_q(n, 0);
        vector<int> count_match(n, 0);
        for (int i = 0; i < n; ++i) {
            for (int k = 0; k < m; ++k) {
                if (res[i + k] == '?') count_q[i]++;
                else if (res[i + k] == str2[k]) count_match[i]++;
            }
            if (str1[i] == 'F' && count_q[i] == 0 && count_match[i] == m) return "";
        }

        for (int j = 0; j < L; ++j) {
            if (res[j] == '?') {
                int forbidden = 0;
                int start_i = max(0, j - m + 1);
                int end_i = min(j, n - 1);
                for (int i = start_i; i <= end_i; ++i) {
                    if (str1[i] == 'F' && count_q[i] == 1 && count_match[i] == m - 1) {
                        forbidden |= (1 << (str2[j - i] - 'a'));
                    }
                }
                int chosen_c = -1;
                for (int k = 0; k < 26; ++k) {
                    if (!(forbidden & (1 << k))) {
                        chosen_c = k;
                        break;
                    }
                }
                if (chosen_c == -1) return "";
                res[j] = 'a' + chosen_c;
                for (int i = start_i; i <= end_i; ++i) {
                    count_q[i]--;
                    if (res[j] == str2[j - i]) count_match[i]++;
                }
            }
        }
        return res;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public String generateString(String str1, String str2) {
        int n = str1.length();
        int m = str2.length();
        int L = n + m - 1;
        char[] res = new char[L];
        for (int i = 0; i < L; i++) res[i] = '?';

        for (int i = 0; i < n; i++) {
            if (str1.charAt(i) == 'T') {
                for (int k = 0; k < m; k++) {
                    if (res[i + k] != '?' && res[i + k] != str2.charAt(k)) return "";
                    res[i + k] = str2.charAt(k);
                }
            }
        }

        int[] count_q = new int[n];
        int[] count_match = new int[n];
        for (int i = 0; i < n; i++) {
            for (int k = 0; k < m; k++) {
                if (res[i + k] == '?') count_q[i]++;
                else if (res[i + k] == str2.charAt(k)) count_match[i]++;
            }
            if (str1.charAt(i) == 'F' && count_q[i] == 0 && count_match[i] == m) return "";
        }

        for (int j = 0; j < L; j++) {
            if (res[j] == '?') {
                int forbidden = 0;
                int start_i = Math.max(0, j - m + 1);
                int end_i = Math.min(j, n - 1);
                for (int i = start_i; i <= end_i; i++) {
                    if (str1.charAt(i) == 'F' && count_q[i] == 1 && count_match[i] == m - 1) {
                        forbidden |= (1 << (str2.charAt(j - i) - 'a'));
                    }
                }
                int chosen_c = -1;
                for (int k = 0; k < 26; k++) {
                    if ((forbidden & (1 << k)) == 0) {
                        chosen_c = k;
                        break;
                    }
                }
                if (chosen_c == -1) return "";
                res[j] = (char)('a' + chosen_c);
                for (int i = start_i; i <= end_i; i++) {
                    count_q[i]--;
                    if (res[j] == str2.charAt(j - i)) count_match[i]++;
                }
            }
        }
        return new String(res);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def generateString(self, str1, str2):
        n, m = len(str1), len(str2)
        l = n + m - 1
        res = ['?'] * l
        str2_ints = [ord(c) - ord('a') for c in str2]

        for i in range(n):
            if str1[i] == 'T':
                for k in range(m):
                    if res[i + k] != '?' and res[i + k] != str2[k]:
                        return ""
                    res[i + k] = str2[k]

        count_q, count_match = [0] * n, [0] * n
        for i in range(n):
            for k in range(m):
                if res[i + k] == '?':
                    count_q[i] += 1
                elif res[i + k] == str2[k]:
                    count_match[i] += 1
            if str1[i] == 'F' and count_q[i] == 0 and count_match[i] == m:
                return ""

        for j in range(l):
            if res[j] == '?':
                forbidden = 0
                start_i = max(0, j - m + 1)
                end_i = min(j, n - 1)
                for i in range(start_i, end_i + 1):
                    if str1[i] == 'F' and count_q[i] == 1 and count_match[i] == m - 1:
                        forbidden |= (1 << str2_ints[j - i])

                chosen_c = -1
                for k in range(26):
                    if not (forbidden & (1 << k)):
                        chosen_c = k
                        break
                if chosen_c == -1: return ""
                res[j] = chr(ord('a') + chosen_c)
                for i in range(start_i, end_i + 1):
                    count_q[i] -= 1
                    if chosen_c == str2_ints[j - i]:
                        count_match[i] += 1
        return "".join(res)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        l = n + m - 1
        res = ['?'] * l
        str2_ints = [ord(c) - ord('a') for c in str2]

        for i in range(n):
            if str1[i] == 'T':
                for k in range(m):
                    if res[i + k] != '?' and res[i + k] != str2[k]:
                        return ""
                    res[i + k] = str2[k]

        count_q, count_match = [0] * n, [0] * n
        for i in range(n):
            for k in range(m):
                if res[i + k] == '?':
                    count_q[i] += 1
                elif res[i + k] == str2[k]:
                    count_match[i] += 1
            if str1[i] == 'F' and count_q[i] == 0 and count_match[i] == m:
                return ""

        for j in range(l):
            if res[j] == '?':
                forbidden = 0
                start_i = max(0, j - m + 1)
                end_i = min(j, n - 1)
                for i in range(start_i, end_i + 1):
                    if str1[i] == 'F' and count_q[i] == 1 and count_match[i] == m - 1:
                        forbidden |= (1 << str2_ints[j - i])

                chosen_c = -1
                for k in range(26):
                    if not (forbidden & (1 << k)):
                        chosen_c = k
                        break
                if chosen_c == -1: return ""
                res[j] = chr(ord('a') + chosen_c)
                for i in range(start_i, end_i + 1):
                    count_q[i] -= 1
                    if chosen_c == str2_ints[j - i]:
                        count_match[i] += 1
        return "".join(res)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
char* generateString(char* str1, char* str2) {
    int n = strlen(str1), m = strlen(str2);
    int L = n + m - 1;
    char* res = (char*)malloc(L + 1);
    for (int i = 0; i < L; i++) res[i] = '?';
    res[L] = '\0';

    for (int i = 0; i < n; i++) {
        if (str1[i] == 'T') {
            for (int k = 0; k < m; k++) {
                if (res[i + k] != '?' && res[i + k] != str2[k]) { free(res); return ""; }
                res[i + k] = str2[k];
            }
        }
    }

    int* cq = (int*)calloc(n, sizeof(int));
    int* cm = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < n; i++) {
        for (int k = 0; k < m; k++) {
            if (res[i + k] == '?') cq[i]++;
            else if (res[i + k] == str2[k]) cm[i]++;
        }
        if (str1[i] == 'F' && cq[i] == 0 && cm[i] == m) { free(res); free(cq); free(cm); return ""; }
    }

    for (int j = 0; j < L; j++) {
        if (res[j] == '?') {
            int forbidden = 0;
            int s_i = MAX(0, j - m + 1), e_i = MIN(j, n - 1);
            for (int i = s_i; i <= e_i; i++) {
                if (str1[i] == 'F' && cq[i] == 1 && cm[i] == m - 1) forbidden |= (1 << (str2[j - i] - 'a'));
            }
            int chosen = -1;
            for (int k = 0; k < 26; k++) if (!(forbidden & (1 << k))) { chosen = k; break; }
            if (chosen == -1) { free(res); free(cq); free(cm); return ""; }
            res[j] = 'a' + chosen;
            for (int i = s_i; i <= e_i; i++) {
                cq[i]--;
                if (res[j] == str2[j - i]) cm[i]++;
            }
        }
    }
    free(cq); free(cm);
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public string GenerateString(string str1, string str2) {
        int n = str1.Length, m = str2.Length;
        int L = n + m - 1;
        char[] res = new char[L];
        for (int i = 0; i < L; i++) res[i] = '?';

        for (int i = 0; i < n; i++) {
            if (str1[i] == 'T') {
                for (int k = 0; k < m; k++) {
                    if (res[i + k] != '?' && res[i + k] != str2[k]) return "";
                    res[i + k] = str2[k];
                }
            }
        }

        int[] cq = new int[n], cm = new int[n];
        for (int i = 0; i < n; i++) {
            for (int k = 0; k < m; k++) {
                if (res[i + k] == '?') cq[i]++;
                else if (res[i + k] == str2[k]) cm[i]++;
            }
            if (str1[i] == 'F' && cq[i] == 0 && cm[i] == m) return "";
        }

        for (int j = 0; j < L; j++) {
            if (res[j] == '?') {
                int forbidden = 0;
                int s_i = Math.Max(0, j - m + 1), e_i = Math.Min(j, n - 1);
                for (int i = s_i; i <= e_i; i++) {
                    if (str1[i] == 'F' && cq[i] == 1 && cm[i] == m - 1)
                        forbidden |= (1 << (str2[j - i] - 'a'));
                }
                int chosen = -1;
                for (int k = 0; k < 26; k++) if ((forbidden & (1 << k)) == 0) { chosen = k; break; }
                if (chosen == -1) return "";
                res[j] = (char)('a' + chosen);
                for (int i = s_i; i <= e_i; i++) {
                    cq[i]--;
                    if (res[j] == str2[j - i]) cm[i]++;
                }
            }
        }
        return new string(res);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var generateString = function(str1, str2) {
    let n = str1.length, m = str2.length, L = n + m - 1;
    let res = new Array(L).fill('?');

    for (let i = 0; i < n; i++) {
        if (str1[i] === 'T') {
            for (let k = 0; k < m; k++) {
                if (res[i + k] !== '?' && res[i + k] !== str2[k]) return "";
                res[i + k] = str2[k];
            }
        }
    }

    let cq = new Int32Array(n), cm = new Int32Array(n);
    for (let i = 0; i < n; i++) {
        for (let k = 0; k < m; k++) {
            if (res[i + k] === '?') cq[i]++;
            else if (res[i + k] === str2[k]) cm[i]++;
        }
        if (str1[i] === 'F' && cq[i] === 0 && cm[i] === m) return "";
    }

    for (let j = 0; j < L; j++) {
        if (res[j] === '?') {
            let forbidden = 0;
            let s_i = Math.max(0, j - m + 1), e_i = Math.min(j, n - 1);
            for (let i = s_i; i <= e_i; i++) {
                if (str1[i] === 'F' && cq[i] === 1 && cm[i] === m - 1) {
                    forbidden |= (1 << (str2.charCodeAt(j - i) - 97));
                }
            }
            let chosen = -1;
            for (let k = 0; k < 26; k++) if (!(forbidden & (1 << k))) { chosen = k; break; }
            if (chosen === -1) return "";
            res[j] = String.fromCharCode(97 + chosen);
            for (let i = s_i; i <= e_i; i++) {
                cq[i]--;
                if (res[j] === str2[i + (j - i) - i] && res[j] === str2[j - i]) cm[i]++;
            }
        }
    }
    return res.join('');
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function generateString(str1: string, str2: string): string {
    const n = str1.length;
    const m = str2.length;
    const L = n + m - 1;

    const fixed: (string | null)[] = new Array(L).fill(null);
    for (let i = 0; i < n; i++) {
        if (str1[i] === 'T') {
            for (let j = 0; j < m; j++) {
                if (fixed[i + j] !== null && fixed[i + j] !== str2[j]) return "";
                fixed[i + j] = str2[j];
            }
        }
    }

    const pi = new Int32Array(m);
    for (let i = 1; i < m; i++) {
        let j = pi[i - 1];
        while (j > 0 && str2[i] !== str2[j]) j = pi[j - 1];
        if (str2[i] === str2[j]) j++;
        pi[i] = j;
    }

    const nxt_state = new Int32Array(m * 26);
    const is_nj_m = new Uint8Array(m * 26);
    for (let j = 0; j < m; j++) {
        for (let c = 0; c < 26; c++) {
            const char = String.fromCharCode(97 + c);
            let nj = j;
            while (nj > 0 && char !== str2[nj]) nj = pi[nj - 1];
            if (char === str2[nj]) nj++;

            if (nj === m) {
                is_nj_m[j * 26 + c] = 1;
                nxt_state[j * 26 + c] = pi[m - 1];
            } else {
                is_nj_m[j * 26 + c] = 0;
                nxt_state[j * 26 + c] = nj;
            }
        }
    }

    const dp = new Uint8Array((L + 1) * m);
    for (let j = 0; j < m; j++) dp[L * m + j] = 1;

    for (let i = L - 1; i >= 0; i--) {
        const cond_T = (i >= m - 1 && str1[i - m + 1] === 'T');
        const cond_F = (i >= m - 1 && str1[i - m + 1] === 'F');
        for (let j = 0; j < m; j++) {
            if (fixed[i] !== null) {
                const c = fixed[i]!.charCodeAt(0) - 97;
                const nj_m = is_nj_m[j * 26 + c];
                if ((!cond_T || nj_m) && (!cond_F || !nj_m)) {
                    if (dp[(i + 1) * m + nxt_state[j * 26 + c]]) dp[i * m + j] = 1;
                }
            } else {
                for (let c = 0; c < 26; c++) {
                    const nj_m = is_nj_m[j * 26 + c];
                    if ((!cond_T || nj_m) && (!cond_F || !nj_m)) {
                        if (dp[(i + 1) * m + nxt_state[j * 26 + c]]) {
                            dp[i * m + j] = 1;
                            break;
                        }
                    }
                }
            }
        }
    }

    if (!dp[0]) return "";
    let curr_j = 0;
    let res = "";
    for (let i = 0; i < L; i++) {
        const cond_T = (i >= m - 1 && str1[i - m + 1] === 'T');
        const cond_F = (i >= m - 1 && str1[i - m + 1] === 'F');
        let found = false;
        for (let c = 0; c < 26; c++) {
            const char = String.fromCharCode(97 + c);
            if (fixed[i] !== null && fixed[i] !== char) continue;

            const nj_m = is_nj_m[curr_j * 26 + c];
            if ((!cond_T || nj_m) && (!cond_F || !nj_m)) {
                const nj = nxt_state[curr_j * 26 + c];
                if (dp[(i + 1) * m + nj]) {
                    res += char;
                    curr_j = nj;
                    found = true;
                    break;
                }
            }
        }
        if (!found) return "";
    }
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function generateString($str1, $str2) {
        $n = strlen($str1);
        $m = strlen($str2);
        $L = $n + $m - 1;
        $fixed = str_repeat("\0", $L);
        for ($i = 0; $i < $n; $i++) {
            if ($str1[$i] === 'T') {
                for ($j = 0; $j < $m; $j++) {
                    if ($fixed[$i + $j] !== "\0" && $fixed[$i + $j] !== $str2[$j]) return "";
                    $fixed[$i + $j] = $str2[$j];
                }
            }
        }
        $pi = array_fill(0, $m, 0);
        for ($i = 1; $i < $m; $i++) {
            $j = $pi[$i - 1];
            while ($j > 0 && $str2[$i] !== $str2[$j]) $j = $pi[$j - 1];
            if ($str2[$i] === $str2[$j]) $j++;
            $pi[$i] = $j;
        }
        $nxt_state = new SplFixedArray($m * 26);
        $is_nj_m = new SplFixedArray($m * 26);
        for ($j = 0; $j < $m; $j++) {
            for ($c = 0; $c < 26; $c++) {
                $char = chr(97 + $c);
                $nj = $j;
                while ($nj > 0 && $char !== $str2[$nj]) $nj = $pi[$nj - 1];
                if ($char === $str2[$nj]) $nj++;
                if ($nj === $m) {
                    $is_nj_m[$j * 26 + $c] = true;
                    $nxt_state[$j * 26 + $c] = $pi[$m - 1];
                } else {
                    $is_nj_m[$j * 26 + $c] = false;
                    $nxt_state[$j * 26 + $c] = $nj;
                }
            }
        }
        $dp = str_repeat("\0", ($L + 1) * $m);
        for ($j = 0; $j < $m; $j++) $dp[$L * $m + $j] = "\1";
        for ($i = $L - 1; $i >= 0; $i--) {
            $cond_T = ($i >= $m - 1 && $str1[$i - $m + 1] === 'T');
            $cond_F = ($i >= $m - 1 && $str1[$i - $m + 1] === 'F');
            for ($j = 0; $j < $m; $j++) {
                if ($fixed[$i] !== "\0") {
                    $c = ord($fixed[$i]) - 97;
                    $nj_m = $is_nj_m[$j * 26 + $c];
                    if ((!$cond_T || $nj_m) && (!$cond_F || !$nj_m)) {
                        if ($dp[($i + 1) * $m + $nxt_state[$j * 26 + $c]] === "\1") $dp[$i * $m + $j] = "\1";
                    }
                } else {
                    for ($c = 0; $c < 26; $c++) {
                        $nj_m = $is_nj_m[$j * 26 + $c];
                        if ((!$cond_T || $nj_m) && (!$cond_F || !$nj_m)) {
                            if ($dp[($i + 1) * $m + $nxt_state[$j * 26 + $c]] === "\1") {
                                $dp[$i * $m + $j] = "\1";
                                break;
                            }
                        }
                    }
                }
            }
        }
        if ($dp[0] === "\0") return "";
        $curr_j = 0; $res = [];
        for ($i = 0; $i < $L; $i++) {
            $cond_T = ($i >= $m - 1 && $str1[$i - $m + 1] === 'T');
            $cond_F = ($i >= $m - 1 && $str1[$i - $m + 1] === 'F');
            for ($c = 0; $c < 26; $c++) {
                $char = chr(97 + $c);
                if ($fixed[$i] !== "\0" && $fixed[$i] !== $char) continue;
                $nj_m = $is_nj_m[$curr_j * 26 + $c];
                if ((!$cond_T || $nj_m) && (!$cond_F || !$nj_m)) {
                    $nj = $nxt_state[$curr_j * 26 + $c];
                    if ($dp[($i + 1) * $m + $nj] === "\1") {
                        $res[] = $char;
                        $curr_j = $nj;
                        break;
                    }
                }
            }
        }
        return implode("", $res);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func generateString(_ str1: String, _ str2: String) -> String {
        let s1 = Array(str1), s2 = Array(str2)
        let n = s1.count, m = s2.count
        let L = n + m - 1
        var fixed = [Character?](repeating: nil, count: L)
        for i in 0..<n {
            if s1[i] == "T" {
                for j in 0..<m {
                    if let f = fixed[i + j], f != s2[j] { return "" }
                    fixed[i + j] = s2[j]
                }
            }
        }
        var pi = [Int](repeating: 0, count: m)
        for i in 1..<m {
            var j = pi[i - 1]
            while j > 0 && s2[i] != s2[j] { j = pi[j - 1] }
            if s2[i] == s2[j] { j += 1 }
            pi[i] = j
        }
        var nxt_state = [Int](repeating: 0, count: m * 26)
        var is_nj_m = [Bool](repeating: false, count: m * 26)
        let chars = (0..<26).map { Character(UnicodeScalar(97 + $0)!) }
        for j in 0..<m {
            for c in 0..<26 {
                let char = chars[c]
                var nj = j
                while nj > 0 && char != s2[nj] { nj = pi[nj - 1] }
                if char == s2[nj] { nj += 1 }
                if nj == m {
                    is_nj_m[j * 26 + c] = true
                    nxt_state[j * 26 + c] = pi[m - 1]
                } else {
                    is_nj_m[j * 26 + c] = false
                    nxt_state[j * 26 + c] = nj
                }
            }
        }
        var dp = [Bool](repeating: false, count: (L + 1) * m)
        for j in 0..<m { dp[L * m + j] = true }
        for i in (0..<L).reversed() {
            let cond_T = (i >= m - 1 && s1[i - m + 1] == "T")
            let cond_F = (i >= m - 1 && s1[i - m + 1] == "F")
            for j in 0..<m {
                if let f = fixed[i] {
                    let c = Int(f.asciiValue! - 97)
                    let nj_m = is_nj_m[j * 26 + c]
                    if (!cond_T || nj_m) && (!cond_F || !nj_m) {
                        if dp[(i + 1) * m + nxt_state[j * 26 + c]] { dp[i * m + j] = true }
                    }
                } else {
                    for c in 0..<26 {
                        let nj_m = is_nj_m[j * 26 + c]
                        if (!cond_T || nj_m) && (!cond_F || !nj_m) {
                            if dp[(i + 1) * m + nxt_state[j * 26 + c]] {
                                dp[i * m + j] = true
                                break
                            }
                        }
                    }
                }
            }
        }
        if !dp[0] { return "" }
        var curr_j = 0, res = ""
        for i in 0..<L {
            let cond_T = (i >= m - 1 && s1[i - m + 1] == "T")
            let cond_F = (i >= m - 1 && s1[i - m + 1] == "F")
            for c in 0..<26 {
                let char = chars[c]
                if let f = fixed[i], f != char { continue }
                let nj_m = is_nj_m[curr_j * 26 + c]
                if (!cond_T || nj_m) && (!cond_F || !nj_m) {
                    let nj = nxt_state[curr_j * 26 + c]
                    if dp[(i + 1) * m + nj] {
                        res.append(char)
                        curr_j = nj
                        break
                    }
                }
            }
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
    fun generateString(str1: String, str2: String): String {
        val n = str1.length
        val m = str2.length
        val L = n + m - 1
        val fixed = CharArray(L) { '\u0000' }
        for (i in 0 until n) {
            if (str1[i] == 'T') {
                for (j in 0 until m) {
                    if (fixed[i + j] != '\u0000' && fixed[i + j] != str2[j]) return ""
                    fixed[i + j] = str2[j]
                }
            }
        }
        val pi = IntArray(m)
        for (i in 1 until m) {
            var j = pi[i - 1]
            while (j > 0 && str2[i] != str2[j]) j = pi[j - 1]
            if (str2[i] == str2[j]) j++
            pi[i] = j
        }
        val nxtState = IntArray(m * 26)
        val isNjM = BooleanArray(m * 26)
        for (j in 0 until m) {
            for (c in 0 until 26) {
                val char = ('a' + c)
                var nj = j
                while (nj > 0 && char != str2[nj]) nj = pi[nj - 1]
                if (char == str2[nj]) nj++
                if (nj == m) {
                    isNjM[j * 26 + c] = true
                    nxtState[j * 26 + c] = pi[m - 1]
                } else {
                    isNjM[j * 26 + c] = false
                    nxtState[j * 26 + c] = nj
                }
            }
        }
        val dp = java.util.BitSet((L + 1) * m)
        for (j in 0 until m) dp.set(L * m + j)
        for (i in L - 1 downTo 0) {
            val condT = i >= m - 1 && str1[i - m + 1] == 'T'
            val condF = i >= m - 1 && str1[i - m + 1] == 'F'
            for (j in 0 until m) {
                if (fixed[i] != '\u0000') {
                    val c = fixed[i] - 'a'
                    val njM = isNjM[j * 26 + c]
                    if ((!condT || njM) && (!condF || !njM)) {
                        if (dp.get((i + 1) * m + nxtState[j * 26 + c])) dp.set(i * m + j)
                    }
                } else {
                    for (c in 0 until 26) {
                        val njM = isNjM[j * 26 + c]
                        if ((!condT || njM) && (!condF || !njM)) {
                            if (dp.get((i + 1) * m + nxtState[j * 26 + c])) {
                                dp.set(i * m + j)
                                break
                            }
                        }
                    }
                }
            }
        }
        if (!dp.get(0)) return ""
        var currJ = 0
        val res = StringBuilder()
        for (i in 0 until L) {
            val condT = i >= m - 1 && str1[i - m + 1] == 'T'
            val condF = i >= m - 1 && str1[i - m + 1] == 'F'
            for (c in 0 until 26) {
                val char = ('a' + c)
                if (fixed[i] != '\u0000' && fixed[i] != char) continue
                val njM = isNjM[currJ * 26 + c]
                if ((!condT || njM) && (!condF || !njM)) {
                    val nj = nxtState[currJ * 26 + c]
                    if (dp.get((i + 1) * m + nj)) {
                        res.append(char)
                        currJ = nj
                        break
                    }
                }
            }
        }
        return res.toString()
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
  String generateString(String str1, String str2) {
    int n = str1.length, m = str2.length, L = n + m - 1;
    List<String?> fixed = List.filled(L, null);
    for (int i = 0; i < n; i++) {
      if (str1[i] == 'T') {
        for (int j = 0; j < m; j++) {
          if (fixed[i + j] != null && fixed[i + j] != str2[j]) return "";
          fixed[i + j] = str2[j];
        }
      }
    }
    Int32List pi = Int32List(m);
    for (int i = 1; i < m; i++) {
      int j = pi[i - 1];
      while (j > 0 && str2[i] != str2[j]) j = pi[j - 1];
      if (str2[i] == str2[j]) j++;
      pi[i] = j;
    }
    Int32List nxtState = Int32List(m * 26);
    Uint8List isNjM = Uint8List(m * 26);
    for (int j = 0; j < m; j++) {
      for (int c = 0; c < 26; c++) {
        String char = String.fromCharCode(97 + c);
        int nj = j;
        while (nj > 0 && char != str2[nj]) nj = pi[nj - 1];
        if (char == str2[nj]) nj++;
        if (nj == m) {
          isNjM[j * 26 + c] = 1;
          nxtState[j * 26 + c] = pi[m - 1];
        } else {
          isNjM[j * 26 + c] = 0;
          nxtState[j * 26 + c] = nj;
        }
      }
    }
    Uint8List dp = Uint8List((L + 1) * m);
    for (int j = 0; j < m; j++) dp[L * m + j] = 1;
    for (int i = L - 1; i >= 0; i--) {
      bool condT = (i >= m - 1 && str1[i - m + 1] == 'T');
      bool condF = (i >= m - 1 && str1[i - m + 1] == 'F');
      for (int j = 0; j < m; j++) {
        if (fixed[i] != null) {
          int c = fixed[i]!.codeUnitAt(0) - 97;
          bool njM = isNjM[j * 26 + c] == 1;
          if ((!condT || njM) && (!condF || !njM)) {
            if (dp[(i + 1) * m + nxtState[j * 26 + c]] == 1) dp[i * m + j] = 1;
          }
        } else {
          for (int c = 0; c < 26; c++) {
            bool njM = isNjM[j * 26 + c] == 1;
            if ((!condT || njM) && (!condF || !njM)) {
              if (dp[(i + 1) * m + nxtState[j * 26 + c]] == 1) {
                dp[i * m + j] = 1;
                break;
              }
            }
          }
        }
      }
    }
    if (dp[0] == 0) return "";
    int currJ = 0; StringBuffer res = StringBuffer();
    for (int i = 0; i < L; i++) {
      bool condT = (i >= m - 1 && str1[i - m + 1] == 'T');
      bool condF = (i >= m - 1 && str1[i - m + 1] == 'F');
      for (int c = 0; c < 26; c++) {
        String char = String.fromCharCode(97 + c);
        if (fixed[i] != null && fixed[i] != char) continue;
        bool njM = isNjM[currJ * 26 + c] == 1;
        if ((!condT || njM) && (!condF || !njM)) {
          int nj = nxtState[currJ * 26 + c];
          if (dp[(i + 1) * m + nj] == 1) {
            res.write(char); currJ = nj; break;
          }
        }
      }
    }
    return res.toString();
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func generateString(str1 string, str2 string) string {
	n := len(str1)
	m := len(str2)
	L := n + m - 1
	fixed := make([]byte, L)
	for i := 0; i < n; i++ {
		if str1[i] == 'T' {
			for j := 0; j < m; j++ {
				if fixed[i+j] != 0 && fixed[i+j] != str2[j] {
					return ""
				}
				fixed[i+j] = str2[j]
			}
		}
	}
	pi := make([]int, m)
	for i := 1; i < m; i++ {
		j := pi[i-1]
		for j > 0 && str2[i] != str2[j] {
			j = pi[j-1]
		}
		if str2[i] == str2[j] {
			j++
		}
		pi[i] = j
	}
	nxtState := make([]int, m*26)
	isNjM := make([]bool, m*26)
	for j := 0; j < m; j++ {
		for c := 0; c < 26; c++ {
			char := byte('a' + c)
			nj := j
			for nj > 0 && char != str2[nj] {
				nj = pi[nj-1]
			}
			if char == str2[nj] {
				nj++
			}
			if nj == m {
				isNjM[j*26+c] = true
				nxtState[j*26+c] = pi[m-1]
			} else {
				isNjM[j*26+c] = false
				nxtState[j*26+c] = nj
			}
		}
	}
	dp := make([]byte, (L+1)*m)
	for j := 0; j < m; j++ {
		dp[L*m+j] = 1
	}
	for i := L - 1; i >= 0; i-- {
		condT := i >= m-1 && str1[i-m+1] == 'T'
		condF := i >= m-1 && str1[i-m+1] == 'F'
		for j := 0; j < m; j++ {
			if fixed[i] != 0 {
				c := int(fixed[i] - 'a')
				njM := isNjM[j*26+c]
				if (!condT || njM) && (!condF || !njM) {
					if dp[(i+1)*m+nxtState[j*26+c]] == 1 {
						dp[i*m+j] = 1
					}
				}
			} else {
				for c := 0; c < 26; c++ {
					njM := isNjM[j*26+c]
					if (!condT || njM) && (!condF || !njM) {
						if dp[(i+1)*m+nxtState[j*26+c]] == 1 {
							dp[i*m+j] = 1
							break
						}
					}
				}
			}
		}
	}
	if dp[0] == 0 {
		return ""
	}
	var res strings.Builder
	currJ := 0
	for i := 0; i < L; i++ {
		condT := i >= m-1 && str1[i-m+1] == 'T'
		condF := i >= m-1 && str1[i-m+1] == 'F'
		for c := 0; c < 26; c++ {
			char := byte('a' + c)
			if fixed[i] != 0 && fixed[i] != char {
				continue
			}
			njM := isNjM[currJ*26+c]
			if (!condT || njM) && (!condF || !njM) {
				nj := nxtState[currJ*26+c]
				if dp[(i+1)*m+nj] == 1 {
					res.WriteByte(char)
					currJ = nj
					break
				}
			}
		}
	}
	return res.String()
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
// Generation failed for Ruby
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
// Generation failed for Scala
// Reason: Parsing failed
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

- **Time Complexity:** O(nm) where $n$ is the length of `str1` and $m$ is the length of `str2`. Filling 'T' constraints, initializing window counters, and the greedy filling process each involve iterating over windows or positions at most $O(nm)$ times.
- **Space Complexity:** O(n + m) to store the result string of length $n + m - 1$, the counters for each window (length $n$), and auxiliary data structures for constraints.
