---
layout: post
title: "Lexicographically Smallest Permutation Greater Than Target"
date: 2026-08-27 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Hash Table", "String", "Greedy", "Counting", "Enumeration"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    string lexGreaterPermutation(string s, string\
        \ target) {\n        int n = s.length();\n        vector<int> counts(26, 0);\n\
        \        for (char c : s) counts[c - 'a']++;\n\n        vector<int> temp_counts\
        \ = counts;\n        int L = 0;\n        for (int j = 0; j < n; j++) {\n   \
        \         int idx = target[j] - 'a';\n            if (temp_counts[idx] > 0)\
        \ {\n                temp_counts[idx]--;\n                L++;\n           \
        \ } else {\n                break;\n            }\n        }\n\n        if (L\
        \ == n) {\n            L = n - 1;\n            temp_counts[target[n - 1] - 'a']++;\n\
        \        }\n\n        for (int i = L; i >= 0; i--) {\n            int target_idx\
        \ = target[i] - 'a';\n            for (int char_idx = target_idx + 1; char_idx\
        \ < 26; char_idx++) {\n                if (temp_counts[char_idx] > 0) {\n  \
        \                  string res = target.substr(0, i);\n                    res\
        \ += (char)('a' + char_idx);\n                    temp_counts[char_idx]--;\n\
        \                    for (int k = 0; k < 26; k++) {\n                      \
        \  while (temp_counts[k] > 0) {\n                            res += (char)('a'\
        \ + k);\n                            temp_counts[k]--;\n                   \
        \     }\n                    }\n                    return res;\n          \
        \      }\n            }\n            if (i > 0) {\n                temp_counts[target[i\
        \ - 1] - 'a']++;\n            }\n        }\n\n        return \"\";\n    }\n\
        };"
      java: "class Solution {\n    public String lexGreaterPermutation(String s, String\
        \ target) {\n        int n = s.length();\n        int[] counts = new int[26];\n\
        \        for (char c : s.toCharArray()) counts[c - 'a']++;\n\n        int[]\
        \ tempCounts = counts.clone();\n        int L = 0;\n        for (int j = 0;\
        \ j < n; j++) {\n            int idx = target.charAt(j) - 'a';\n           \
        \ if (tempCounts[idx] > 0) {\n                tempCounts[idx]--;\n         \
        \       L++;\n            } else {\n                break;\n            }\n\
        \        }\n\n        if (L == n) {\n            L = n - 1;\n            tempCounts[target.charAt(n\
        \ - 1) - 'a']++;\n        }\n\n        for (int i = L; i >= 0; i--) {\n    \
        \        int targetIdx = target.charAt(i) - 'a';\n            for (int charIdx\
        \ = targetIdx + 1; charIdx < 26; charIdx++) {\n                if (tempCounts[charIdx]\
        \ > 0) {\n                    StringBuilder res = new StringBuilder();\n   \
        \                 res.append(target.substring(0, i));\n                    res.append((char)\
        \ ('a' + charIdx));\n                    tempCounts[charIdx]--;\n          \
        \          for (int k = 0; k < 26; k++) {\n                        while (tempCounts[k]\
        \ > 0) {\n                            res.append((char) ('a' + k));\n      \
        \                      tempCounts[k]--;\n                        }\n       \
        \             }\n                    return res.toString();\n              \
        \  }\n            }\n            if (i > 0) {\n                tempCounts[target.charAt(i\
        \ - 1) - 'a']++;\n            }\n        }\n\n        return \"\";\n    }\n}"
      python: "class Solution(object):\n    def lexGreaterPermutation(self, s, target):\n\
        \        \"\"\"\n        :type s: str\n        :type target: str\n        :rtype:\
        \ str\n        \"\"\"\n        n = len(s)\n        counts = [0] * 26\n     \
        \   for char in s:\n            counts[ord(char) - ord('a')] += 1\n\n      \
        \  temp_counts = list(counts)\n        L = 0\n        for char in target:\n\
        \            idx = ord(char) - ord('a')\n            if temp_counts[idx] > 0:\n\
        \                temp_counts[idx] -= 1\n                L += 1\n           \
        \ else:\n                break\n\n        if L == n:\n            L = n - 1\n\
        \            temp_counts[ord(target[n - 1]) - ord('a')] += 1\n\n        for\
        \ i in range(L, -1, -1):\n            target_char_idx = ord(target[i]) - ord('a')\n\
        \            for char_idx in range(target_char_idx + 1, 26):\n             \
        \   if temp_counts[char_idx] > 0:\n                    res = list(target[:i])\n\
        \                    res.append(chr(ord('a') + char_idx))\n                \
        \    temp_counts[char_idx] -= 1\n                    for k in range(26):\n \
        \                       while temp_counts[k] > 0:\n                        \
        \    res.append(chr(ord('a') + k))\n                            temp_counts[k]\
        \ -= 1\n                    return \"\".join(res)\n\n            if i > 0:\n\
        \                temp_counts[ord(target[i - 1]) - ord('a')] += 1\n\n       \
        \ return \"\""
      python3: "class Solution:\n    def lexGreaterPermutation(self, s: str, target:\
        \ str) -> str:\n        n = len(s)\n        counts = [0] * 26\n        for char\
        \ in s:\n            counts[ord(char) - ord('a')] += 1\n\n        temp_counts\
        \ = list(counts)\n        L = 0\n        for char in target:\n            idx\
        \ = ord(char) - ord('a')\n            if temp_counts[idx] > 0:\n           \
        \     temp_counts[idx] -= 1\n                L += 1\n            else:\n   \
        \             break\n\n        if L == n:\n            L = n - 1\n         \
        \   temp_counts[ord(target[n - 1]) - ord('a')] += 1\n\n        for i in range(L,\
        \ -1, -1):\n            target_char_idx = ord(target[i]) - ord('a')\n      \
        \      for char_idx in range(target_char_idx + 1, 26):\n                if temp_counts[char_idx]\
        \ > 0:\n                    res = list(target[:i])\n                    res.append(chr(ord('a')\
        \ + char_idx))\n                    temp_counts[char_idx] -= 1\n           \
        \         for k in range(26):\n                        while temp_counts[k]\
        \ > 0:\n                            res.append(chr(ord('a') + k))\n        \
        \                    temp_counts[k] -= 1\n                    return \"\".join(res)\n\
        \n            if i > 0:\n                temp_counts[ord(target[i - 1]) - ord('a')]\
        \ += 1\n\n        return \"\""
      c: "#include <stdio.h>\n#include <string.h>\n#include <stdlib.h>\n\nchar* lexGreaterPermutation(char*\
        \ s, char* target) {\n    int n = strlen(s);\n    int counts[26] = {0};\n  \
        \  for (int i = 0; i < n; i++) counts[s[i] - 'a']++;\n\n    int temp_counts[26];\n\
        \    for (int i = 0; i < 26; i++) temp_counts[i] = counts[i];\n\n    int L =\
        \ 0;\n    for (int j = 0; j < n; j++) {\n        int idx = target[j] - 'a';\n\
        \        if (temp_counts[idx] > 0) {\n            temp_counts[idx]--;\n    \
        \        L++;\n        } else {\n            break;\n        }\n    }\n\n  \
        \  if (L == n) {\n        L = n - 1;\n        temp_counts[target[n - 1] - 'a']++;\n\
        \    }\n\n    for (int i = L; i >= 0; i--) {\n        int target_idx = target[i]\
        \ - 'a';\n        for (int char_idx = target_idx + 1; char_idx < 26; char_idx++)\
        \ {\n            if (temp_counts[char_idx] > 0) {\n                char* res\
        \ = (char*)malloc((n + 1) * sizeof(char));\n                for (int k = 0;\
        \ k < i; k++) res[k] = target[k];\n                res[i] = 'a' + char_idx;\n\
        \                temp_counts[char_idx]--;\n                int pos = i + 1;\n\
        \                for (int k = 0; k < 26; k++) {\n                    while (temp_counts[k]\
        \ > 0) {\n                        res[pos++] = 'a' + k;\n                  \
        \      temp_counts[k]--;\n                    }\n                }\n       \
        \         res[n] = '\\0';\n                return res;\n            }\n    \
        \    }\n        if (i > 0) {\n            temp_counts[target[i - 1] - 'a']++;\n\
        \        }\n    }\n\n    return \"\";\n}"
      csharp: "using System;\nusing System.Text;\n\npublic class Solution {\n    public\
        \ string LexGreaterPermutation(string s, string target) {\n        int n = s.Length;\n\
        \        int[] counts = new int[26];\n        foreach (char c in s) {\n    \
        \        counts[c - 'a']++;\n        }\n\n        int matchedUntil = -1;\n \
        \       for (int i = 0; i < n; i++) {\n            int idx = target[i] - 'a';\n\
        \            if (counts[idx] > 0) {\n                counts[idx]--;\n      \
        \          matchedUntil = i;\n            } else {\n                break;\n\
        \            }\n        }\n\n        for (int j = Math.Min(n - 1, matchedUntil\
        \ + 1); j >= 0; j--) {\n            if (j <= matchedUntil) {\n             \
        \   counts[target[j] - 'a']++;\n            }\n\n            for (int c = (target[j]\
        \ - 'a') + 1; c < 26; c++) {\n                if (counts[c] > 0) {\n       \
        \             char[] result = new char[n];\n                    for (int k =\
        \ 0; k < j; k++) {\n                        result[k] = target[k];\n       \
        \             }\n                    result[j] = (char)('a' + c);\n        \
        \            counts[c]--;\n\n                    int ptr = j + 1;\n        \
        \            for (int k = 0; k < 26; k++) {\n                        while (counts[k]\
        \ > 0) {\n                            result[ptr++] = (char)('a' + k);\n   \
        \                         counts[k]--;\n                        }\n        \
        \            }\n                    return new string(result);\n           \
        \     }\n            }\n        }\n\n        return \"\";\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @param {string} target\n * @return\
        \ {string}\n */\nvar lexGreaterPermutation = function(s, target) {\n    const\
        \ n = s.length;\n    const counts = new Array(26).fill(0);\n    const aCode\
        \ = 'a'.charCodeAt(0);\n    for (let i = 0; i < n; i++) {\n        counts[s.charCodeAt(i)\
        \ - aCode]++;\n    }\n\n    let matchedUntil = -1;\n    for (let i = 0; i <\
        \ n; i++) {\n        const idx = target.charCodeAt(i) - aCode;\n        if (counts[idx]\
        \ > 0) {\n            counts[idx]--;\n            matchedUntil = i;\n      \
        \  } else {\n            break;\n        }\n    }\n\n    for (let j = Math.min(n\
        \ - 1, matchedUntil + 1); j >= 0; j--) {\n        if (j <= matchedUntil) {\n\
        \            counts[target.charCodeAt(j) - aCode]++;\n        }\n\n        const\
        \ targetCharIdx = target.charCodeAt(j) - aCode;\n        for (let c = targetCharIdx\
        \ + 1; c < 26; c++) {\n            if (counts[c] > 0) {\n                const\
        \ result = new Array(n);\n                for (let k = 0; k < j; k++) {\n  \
        \                  result[k] = target[k];\n                }\n             \
        \   result[j] = String.fromCharCode(aCode + c);\n                counts[c]--;\n\
        \n                let ptr = j + 1;\n                for (let k = 0; k < 26;\
        \ k++) {\n                    while (counts[k] > 0) {\n                    \
        \    result[ptr++] = String.fromCharCode(aCode + k);\n                     \
        \   counts[k]--;\n                    }\n                }\n               \
        \ return result.join('');\n            }\n        }\n    }\n\n    return \"\"\
        ;\n};"
      typescript: "function lexGreaterPermutation(s: string, target: string): string\
        \ {\n    const n = s.length;\n    const counts = new Int32Array(26);\n    const\
        \ aCode = 'a'.charCodeAt(0);\n    for (let i = 0; i < n; i++) {\n        counts[s.charCodeAt(i)\
        \ - aCode]++;\n    }\n\n    let matchedUntil = -1;\n    for (let i = 0; i <\
        \ n; i++) {\n        const idx = target.charCodeAt(i) - aCode;\n        if (counts[idx]\
        \ > 0) {\n            counts[idx]--;\n            matchedUntil = i;\n      \
        \  } else {\n            break;\n        }\n    }\n\n    for (let j = Math.min(n\
        \ - 1, matchedUntil + 1); j >= 0; j--) {\n        if (j <= matchedUntil) {\n\
        \            counts[target.charCodeAt(j) - aCode]++;\n        }\n\n        const\
        \ targetCharIdx = target.charCodeAt(j) - aCode;\n        for (let c = targetCharIdx\
        \ + 1; c < 26; c++) {\n            if (counts[c] > 0) {\n                const\
        \ result: string[] = new Array(n);\n                for (let k = 0; k < j; k++)\
        \ {\n                    result[k] = target[k];\n                }\n       \
        \         result[j] = String.fromCharCode(aCode + c);\n                counts[c]--;\n\
        \n                let ptr = j + 1;\n                for (let k = 0; k < 26;\
        \ k++) {\n                    while (counts[k] > 0) {\n                    \
        \    result[ptr++] = String.fromCharCode(aCode + k);\n                     \
        \   counts[k]--;\n                    }\n                }\n               \
        \ return result.join('');\n            }\n        }\n    }\n\n    return \"\"\
        ;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @param String\
        \ $target\n     * @return String\n     */\n    function lexGreaterPermutation($s,\
        \ $target) {\n        $n = strlen($s);\n        $counts = array_fill(0, 26,\
        \ 0);\n        $aOrd = ord('a');\n        for ($i = 0; $i < $n; $i++) {\n  \
        \          $counts[ord($s[$i]) - $aOrd]++;\n        }\n\n        $matchedUntil\
        \ = -1;\n        for ($i = 0; $i < $n; $i++) {\n            $idx = ord($target[$i])\
        \ - $aOrd;\n            if ($counts[$idx] > 0) {\n                $counts[$idx]--;\n\
        \                $matchedUntil = $i;\n            } else {\n               \
        \ break;\n            }\n        }\n\n        for ($j = min($n - 1, $matchedUntil\
        \ + 1); $j >= 0; $j--) {\n            if ($j <= $matchedUntil) {\n         \
        \       $counts[ord($target[$j]) - $aOrd]++;\n            }\n\n            $targetCharIdx\
        \ = ord($target[$j]) - $aOrd;\n            for ($c = $targetCharIdx + 1; $c\
        \ < 26; $c++) {\n                if ($counts[$c] > 0) {\n                  \
        \  $result = array_fill(0, $n, '');\n                    for ($k = 0; $k < $j;\
        \ $k++) {\n                        $result[$k] = $target[$k];\n            \
        \        }\n                    $result[$j] = chr($aOrd + $c);\n           \
        \         $counts[$c]--;\n\n                    $ptr = $j + 1;\n           \
        \         for ($k = 0; $k < 26; $k++) {\n                        while ($counts[$k]\
        \ > 0) {\n                            $result[$ptr++] = chr($aOrd + $k);\n \
        \                           $counts[$k]--;\n                        }\n    \
        \                }\n                    return implode('', $result);\n     \
        \           }\n            }\n        }\n\n        return \"\";\n    }\n}"
      swift: "class Solution {\n    func lexGreaterPermutation(_ s: String, _ target:\
        \ String) -> String {\n        let n = s.count\n        let sChars = Array(s)\n\
        \        let tChars = Array(target)\n        var counts = [Int](repeating: 0,\
        \ count: 26)\n        let aOrd = Int(UnicodeScalar(\"a\").value)\n\n       \
        \ for char in sChars {\n            counts[Int(char.unicodeScalars.first!.value)\
        \ - aOrd] += 1\n        }\n\n        var matchedUntil = -1\n        for i in\
        \ 0..<n {\n            let idx = Int(tChars[i].unicodeScalars.first!.value)\
        \ - aOrd\n            if counts[idx] > 0 {\n                counts[idx] -= 1\n\
        \                matchedUntil = i\n            } else {\n                break\n\
        \            }\n        }\n\n        for j in stride(from: min(n - 1, matchedUntil\
        \ + 1), through: 0, by: -1) {\n            if j <= matchedUntil {\n        \
        \        let idx = Int(tChars[j].unicodeScalars.first!.value) - aOrd\n     \
        \           counts[idx] += 1\n            }\n\n            let targetCharIdx\
        \ = Int(tChars[j].unicodeScalars.first!.value) - aOrd\n            for c in\
        \ (targetCharIdx + 1)..<26 {\n                if counts[c] > 0 {\n         \
        \           var result = [Character](repeating: \" \", count: n)\n         \
        \           for k in 0..<j {\n                        result[k] = tChars[k]\n\
        \                    }\n                    result[j] = Character(UnicodeScalar(c\
        \ + aOrd)!)\n                    counts[c] -= 1\n\n                    var ptr\
        \ = j + 1\n                    for k in 0..<26 {\n                        while\
        \ counts[k] > 0 {\n                            result[ptr] = Character(UnicodeScalar(k\
        \ + aOrd)!)\n                            ptr += 1\n                        \
        \    counts[k] -= 1\n                        }\n                    }\n    \
        \                return String(result)\n                }\n            }\n \
        \       }\n\n        return \"\"\n    }\n}"
      kotlin: "class Solution {\n    fun lexGreaterPermutation(s: String, target: String):\
        \ String {\n        val n = s.length\n        val counts = IntArray(26)\n  \
        \      for (char in s) counts[char - 'a']++\n\n        val currentCounts = counts.copyOf()\n\
        \        var matchedLen = 0\n        while (matchedLen < n && currentCounts[target[matchedLen]\
        \ - 'a'] > 0) {\n            currentCounts[target[matchedLen] - 'a']--\n   \
        \         matchedLen++\n        }\n\n        for (i in n - 1 downTo 0) {\n \
        \           if (matchedLen > i) {\n                matchedLen--\n          \
        \      currentCounts[target[matchedLen] - 'a']++\n            }\n\n        \
        \    if (matchedLen == i) {\n                val targetCharIdx = target[i] -\
        \ 'a'\n                for (cIdx in targetCharIdx + 1 until 26) {\n        \
        \            if (currentCounts[cIdx] > 0) {\n                        val res\
        \ = StringBuilder()\n                        res.append(target.substring(0,\
        \ i))\n                        res.append(('a' + cIdx).toChar())\n         \
        \               currentCounts[cIdx]--\n                        for (k in 0 until\
        \ 26) {\n                            repeat(currentCounts[k]) {\n          \
        \                      res.append(('a' + k).toChar())\n                    \
        \        }\n                        }\n                        return res.toString()\n\
        \                    }\n                }\n            }\n        }\n      \
        \  return \"\"\n    }\n}"
      dart: "class Solution {\n  String lexGreaterPermutation(String s, String target)\
        \ {\n    int n = s.length;\n    List<int> counts = List.filled(26, 0);\n   \
        \ for (int i = 0; i < n; i++) {\n      counts[s.codeUnitAt(i) - 97]++;\n   \
        \ }\n\n    List<int> currentCounts = List.from(counts);\n    int matchedLen\
        \ = 0;\n    while (matchedLen < n && currentCounts[target.codeUnitAt(matchedLen)\
        \ - 97] > 0) {\n      currentCounts[target.codeUnitAt(matchedLen) - 97]--;\n\
        \      matchedLen++;\n    }\n\n    for (int i = n - 1; i >= 0; i--) {\n    \
        \  if (matchedLen > i) {\n        matchedLen--;\n        currentCounts[target.codeUnitAt(matchedLen)\
        \ - 97]++;\n      }\n\n      if (matchedLen == i) {\n        int targetCharIdx\
        \ = target.codeUnitAt(i) - 97;\n        for (int cIdx = targetCharIdx + 1; cIdx\
        \ < 26; cIdx++) {\n          if (currentCounts[cIdx] > 0) {\n            StringBuffer\
        \ res = StringBuffer();\n            res.write(target.substring(0, i));\n  \
        \          res.write(String.fromCharCode(97 + cIdx));\n            currentCounts[cIdx]--;\n\
        \            for (int k = 0; k < 26; k++) {\n              for (int j = 0; j\
        \ < currentCounts[k]; j++) {\n                res.write(String.fromCharCode(97\
        \ + k));\n              }\n            }\n            return res.toString();\n\
        \          }\n        }\n      }\n    }\n    return \"\";\n  }\n}"
      go: "func lexGreaterPermutation(s string, target string) string {\n\tn := len(s)\n\
        \tcounts := make([]int, 26)\n\tfor i := 0; i < n; i++ {\n\t\tcounts[s[i]-'a']++\n\
        \t}\n\n\tcurrentCounts := make([]int, 26)\n\tcopy(currentCounts, counts)\n\t\
        matchedLen := 0\n\tfor matchedLen < n && currentCounts[target[matchedLen]-'a']\
        \ > 0 {\n\t\tcurrentCounts[target[matchedLen]-'a']--\n\t\tmatchedLen++\n\t}\n\
        \n\tfor i := n - 1; i >= 0; i-- {\n\t\tif matchedLen > i {\n\t\t\tmatchedLen--\n\
        \t\t\tcurrentCounts[target[matchedLen]-'a']++\n\t\t}\n\n\t\tif matchedLen ==\
        \ i {\n\t\t\ttargetCharIdx := int(target[i] - 'a')\n\t\t\tfor cIdx := targetCharIdx\
        \ + 1; cIdx < 26; cIdx++ {\n\t\t\t\tif currentCounts[cIdx] > 0 {\n\t\t\t\t\t\
        res := make([]byte, 0, n)\n\t\t\t\t\tres = append(res, target[:i]...)\n\t\t\t\
        \t\tres = append(res, byte('a'+cIdx))\n\t\t\t\t\tcurrentCounts[cIdx]--\n\t\t\
        \t\t\tfor k := 0; k < 26; k++ {\n\t\t\t\t\t\tfor j := 0; j < currentCounts[k];\
        \ j++ {\n\t\t\t\t\t\t\tres = append(res, byte('a'+k))\n\t\t\t\t\t\t}\n\t\t\t\
        \t\t}\n\t\t\t\t\treturn string(res)\n\t\t\t\tif }\n\t\t\t}\n\t\t}\n\t}\n\treturn\
        \ \"\"\n}"
      ruby: "# @param {String} s\n# @param {String} target\n# @return {String}\ndef\
        \ lex_greater_permutation(s, target)\n  n = s.length\n  counts = Array.new(26,\
        \ 0)\n  s.each_char { |char| counts[char.ord - 'a'.ord] += 1 }\n\n  current_counts\
        \ = counts.dup\n  matched_len = 0\n  while matched_len < n && current_counts[target[matched_len].ord\
        \ - 'a'.ord] > 0\n    current_counts[target[matched_len].ord - 'a'.ord] -= 1\n\
        \    matched_len += 1\n  end\n\n  (n - 1).step(0, -1) do |i|\n    if matched_len\
        \ > i\n      matched_len -= 1\n      current_counts[target[matched_len].ord\
        \ - 'a'.ord] += 1\n    end\n\n    if matched_len == i\n      target_char_idx\
        \ = target[i].ord - 'a'.ord\n      (target_char_idx + 1...26).each do |c_idx|\n\
        \        if current_counts[c_idx] > 0\n          res = target[0...i]\n     \
        \     res += ('a'.ord + c_idx).chr\n          current_counts[c_idx] -= 1\n \
        \         (0...26).each do |k|\n            res += ('a'.ord + k).chr * current_counts[k]\n\
        \          end\n          return res\n        end\n      end\n    end\n  end\n\
        \  \"\"\nend"
      scala: "object Solution {\n    def lexGreaterPermutation(s: String, target: String):\
        \ String = {\n        val n = s.length\n        val counts = new Array[Int](26)\n\
        \        var i = 0\n        while (i < n) {\n            counts(s.charAt(i)\
        \ - 'a') += 1\n            i += 1\n        }\n\n        val currentCounts =\
        \ counts.clone()\n        var matchedLen = 0\n        while (matchedLen < n\
        \ && currentCounts(target.charAt(matchedLen) - 'a') > 0) {\n            currentCounts(target.charAt(matchedLen)\
        \ - 'a') -= 1\n            matchedLen += 1\n        }\n\n        var idx = n\
        \ - 1\n        while (idx >= 0) {\n            if (matchedLen > idx) {\n   \
        \             matchedLen -= 1\n                currentCounts(target.charAt(matchedLen)\
        \ - 'a') += 1\n            }\n\n            if (matchedLen == idx) {\n     \
        \           val targetCharIdx = target.charAt(idx) - 'a'\n                var\
        \ cIdx = targetCharIdx + 1\n                var found = false\n            \
        \    while (cIdx < 26 && !found) {\n                    if (currentCounts(cIdx)\
        \ > 0) {\n                        val res = new StringBuilder()\n          \
        \              res.append(target.substring(0, idx))\n                      \
        \  res.append(('a' + cIdx).toChar)\n                        currentCounts(cIdx)\
        \ -= 1\n                        var k = 0\n                        while (k\
        \ < 26) {\n                            var count = 0\n                     \
        \       while (count < currentCounts(k)) {\n                               \
        \ res.append(('a' + k).toChar)\n                                count += 1\n\
        \                            }\n                            k += 1\n       \
        \                 }\n                        return res.toString()\n       \
        \             }\n                    cIdx += 1\n                }\n        \
        \    }\n            idx -= 1\n        }\n        \"\"\n    }\n}"
      rust: "impl Solution {\n    pub fn lex_greater_permutation(s: String, target:\
        \ String) -> String {\n        let n = s.len();\n        let mut freq = [0;\
        \ 26];\n        for b in s.bytes() {\n            freq[(b - b'a') as usize]\
        \ += 1;\n        }\n        let target_bytes = target.as_bytes();\n        let\
        \ mut prefixes = Vec::with_capacity(n + 1);\n        prefixes.push(freq);\n\n\
        \        let mut last_match: i32 = -1;\n        let mut current_freq = freq;\n\
        \        for i in 0..n {\n            let c_idx = (target_bytes[i] - b'a') as\
        \ usize;\n            if current_freq[c_idx] > 0 {\n                current_freq[c_idx]\
        \ -= 1;\n                prefixes.push(current_freq);\n                last_match\
        \ = i as i32;\n            } else {\n                break;\n            }\n\
        \        }\n\n        for i in (0..=std::cmp::min(last_match + 1, (n - 1) as\
        \ i32)).rev() {\n            let idx = i as usize;\n            let f = prefixes[idx];\n\
        \            let target_char_idx = (target_bytes[idx] - b'a') as usize;\n  \
        \          for c_idx in (target_char_idx + 1)..26 {\n                if f[c_idx]\
        \ > 0 {\n                    let mut res = Vec::with_capacity(n);\n        \
        \            res.extend_from_slice(&target_bytes[..idx]);\n                \
        \    res.push(b'a' + c_idx as u8);\n                    let mut remaining_freq\
        \ = f;\n                    remaining_freq[c_idx] -= 1;\n                  \
        \  for char_idx in 0..26 {\n                        for _ in 0..remaining_freq[char_idx]\
        \ {\n                            res.push(b'a' + char_idx as u8);\n        \
        \                }\n                    }\n                    return String::from_utf8(res).unwrap();\n\
        \                }\n            }\n        }\n        \"\".to_string()\n   \
        \ }\n}"
      racket: "(define/contract (lex-greater-permutation s target)\n  (-> string? string?\
        \ string?)\n  (let* ([n (string-length s)]\n         [s-list (string->list s)]\n\
        \         [t-list (string->list target)]\n         [freq (let ([h (make-hasheqv)])\n\
        \                 (for ([c s-list])\n                   (hash-set! h c (+ (hash-ref\
        \ h c 0) 1)))\n                 h)])\n    (define (build-prefixes t-list freq\
        \ prefixes last-match i)\n      (if (null? t-list)\n          (values (reverse\
        \ prefixes) last-match)\n          (let* ([c (car t-list)]\n               \
        \  [count (hash-ref freq c 0)])\n            (if (> count 0)\n             \
        \   (let ([new-freq (hash-copy freq)])\n                  (hash-set! new-freq\
        \ c (- count 1))\n                  (build-prefixes (cdr t-list) new-freq (cons\
        \ new-freq prefixes) i (+ i 1)))\n                (values (reverse prefixes)\
        \ last-match)))))\n\n    (let-values ([(prefixes last-match) (build-prefixes\
        \ t-list freq (list freq) -1 0)])\n      (let ([prefix-vec (list->vector prefixes)]\n\
        \            [target-vec (list->vector t-list)])\n        (let loop-i ([i (min\
        \ (+ last_match 1) (- n 1))])\n          (if (< i 0)\n              \"\"\n \
        \             (let* ([f (vector-ref prefix-vec i)]\n                     [target-char\
        \ (vector-ref target-vec i)]\n                     [target-char-code (char->integer\
        \ target-char)])\n                (let loop-c ([c-code (+ target-char-code 1)])\n\
        \                  (if (> c-code (char->integer #\\z))\n                   \
        \   (loop-i (- i 1))\n                      (let* ([c (integer->char c-code)]\n\
        \                             [count (hash-ref f c 0)])\n                  \
        \      (if (> count 0)\n                            (let* ([res-prefix (substring\
        \ target 0 i)]\n                                   [new-f (hash-copy f)])\n\
        \                              (hash-set! new-f c (- count 1))\n           \
        \                   (let ([suffix (apply string-append\n                   \
        \                                (map (lambda (ch-code)\n                  \
        \                                        (make-string (hash-ref new-f (integer->char\
        \ ch-code) 0)\n                                                            \
        \           (integer->char ch-code)))\n                                    \
        \                    (range (char->integer #\\a) (+ (char->integer #\\z) 1))))])\n\
        \                                (string-append res-prefix (string c) suffix)))\n\
        \                            (loop-c (+ c-code 1)))))))))))))"
      erlang: "-spec lex_greater_permutation(S :: unicode:unicode_binary(), Target ::\
        \ unicode:unicode_binary()) -> unicode:unicode_binary().\nlex_greater_permutation(S,\
        \ Target) ->\n  SB = binary_to_list(S),\n  TB = binary_to_list(Target),\n  N\
        \ = length(SB),\n  Freq = lists:foldl(fn(C, Acc) -> maps:put(C, maps:get(C,\
        \ Acc, 0) + 1, Acc) end, #{}, SB),\n  {Prefixes, LastMatch} = build_prefixes(TB,\
        \ Freq, [Freq], -1, 0),\n  Res = find_result(TB, list_to_tuple(Prefixes), LastMatch,\
        \ N),\n  list_to_binary(Res).\n\nbuild_prefixes([H|T], Freq, Prefixes, LastMatch,\
        \ I) ->\n  Count = maps:get(H, Freq, 0),\n  if Count > 0 ->\n    NewFreq = maps:put(H,\
        \ Count - 1, Freq),\n    build_prefixes(T, NewFreq, [NewFreq|Prefixes], I, I\
        \ + 1);\n  true ->\n    {lists:reverse(Prefixes), LastMatch}\n  end;\nbuild_prefixes([],\
        \ _, Prefixes, LastMatch, _) ->\n  {lists:reverse(Prefixes), LastMatch}.\n\n\
        find_result(TargetChars, PrefixTuple, LastMatch, N) ->\n  Limit = if LastMatch\
        \ + 1 < N -> LastMatch + 1; true -> N - 1 end,\n  search_i(Limit, TargetChars,\
        \ PrefixTuple).\n\nsearch_i(I, TargetChars, PrefixTuple) when I >= 0 ->\n  F\
        \ = element(I + 1, PrefixTuple),\n  TargetChar = lists:nth(I + 1, TargetChars),\n\
        \  case search_c(TargetChar + 1, F) of\n    {ok, C} ->\n      Prefix = lists:sublist(TargetChars,\
        \ I),\n      NewF = maps:put(C, maps:get(C, F) - 1, F),\n      Suffix = build_suffix(NewF),\n\
        \      Prefix ++ [C] ++ Suffix;\n    none ->\n      search_i(I - 1, TargetChars,\
        \ PrefixTuple)\n  end;\nsearch_i(_, _, _) -> \"\".\n\nsearch_c(C, F) when C\
        \ =< $z ->\n  case maps:get(C, F, 0) of\n    Count when Count > 0 -> {ok, C};\n\
        \    _ -> search_c(C + 1, F)\n  end;\nsearch_c(_, _) -> none.\n\nbuild_suffix(F)\
        \ ->\n  lists:flatmap(fn(C) -> lists:duplicate(maps:get(C, F, 0), C) end, lists:seq($a,\
        \ $z))."
      elixir: "defmodule Solution do\n  @spec lex_greater_permutation(s :: String.t,\
        \ target :: String.t) :: String.t\n  def lex_greater_permutation(s, target)\
        \ do\n    n = String.length(s)\n    s_chars = String.to_charlist(s)\n    target_chars\
        \ = String.to_charlist(target)\n\n    freq = Enum.reduce(s_chars, %{}, fn char,\
        \ acc -> Map.update(acc, char, 1, &(&1 + 1)) end)\n\n    {prefixes, last_match}\
        \ = build_prefixes(target_chars, freq, [freq], -1, 0)\n    prefix_vec = List.to_tuple(prefixes)\n\
        \    target_vec = List.to_tuple(target_chars)\n\n    limit = min(last_match\
        \ + 1, n - 1)\n\n    Enum.find_value(limit..0, \"\", fn i ->\n      f = elem(prefix_vec,\
        \ i)\n      target_char = elem(target_vec, i)\n      c_range = if target_char\
        \ < ?z, do: (target_char + 1)..?z, else: []\n\n      Enum.find_value(c_range,\
        \ fn c ->\n        if Map.get(f, c, 0) > 0 do\n          res_prefix = Enum.take(target_chars,\
        \ i)\n          new_f = Map.update!(f, c, &(&1 - 1))\n          suffix = Enum.flat_map(?a..?z,\
        \ fn char_code ->\n            List.duplicate(char_code, Map.get(new_f, char_code,\
        \ 0))\n          end)\n          List.to_string(res_prefix ++ [c] ++ suffix)\n\
        \        else\n          nil\n        end\n      end)\n    end)\n  end\n\n \
        \ defp build_prefixes([h | t], freq, prefixes, last_match, i) do\n    count\
        \ = Map.get(freq, h, 0)\n    if count > 0 do\n      new_freq = Map.update!(freq,\
        \ h, &(&1 - 1))\n      build_prefixes(t, new_freq, [new_freq | prefixes], i,\
        \ i + 1)\n    else\n      {Enum.reverse(prefixes), last_match}\n    end\n  end\n\
        \  defp build_prefixes([], _freq, prefixes, last_match, _i) do\n    {Enum.reverse(prefixes),\
        \ last_match}\n  end\nend"
    approach: The problem asks for the lexicographically smallest permutation of string
      's' that is strictly greater than string 'target'. We solve this by finding the
      longest prefix of 'target' that can be formed using the characters available in
      's'. Let this length be 'L'. Since we need a string strictly greater than 'target',
      we cannot simply use the entire matched prefix if it leads to a result equal to
      'target'. Therefore, we backtrack from the rightmost possible index 'i', which
      is either the first mismatch position or the last position of the string, and
      try to find a character in the remaining available characters of 's' that is strictly
      larger than 'target[i]'.
    time_complexity: O(n * K) where n is the length of the string and K is the size
      of the lowercase English alphabet (26). We perform a linear scan to find the longest
      matching prefix and then a backward scan of at most n steps. In each step, we
      check up to K characters to find a lexicographically larger one, and building
      the final string takes O(n) time.
    space_complexity: O(n + K) where n is the length of the string and K is the alphabet
      size (26). We store the frequency count of characters in an array of size K and
      build the output string of length n.
    elapsed_time: 817.081650018692
    model: gemini-3-flash-preview
    generated_at: '2026-08-27 06:39:41 '
---

## Problem #3720: Lexicographically Smallest Permutation Greater Than Target

**Difficulty:** Medium

**Topics:** Hash Table, String, Greedy, Counting, Enumeration

## Problem Description

<p>You are given two strings <code>s</code> and <code>target</code>, both having length <code>n</code>, consisting of lowercase English letters.</p>

<p>Return the <strong>lexicographically smallest <span data-keyword="permutation-string">permutation</span></strong> of <code>s</code> that is <strong>strictly</strong> greater than <code>target</code>. If no permutation of <code>s</code> is lexicographically strictly greater than <code>target</code>, return an empty string.</p>

<p>A string <code>a</code> is <strong>lexicographically strictly greater </strong>than a string <code>b</code> (of the same length) if in the first position where <code>a</code> and <code>b</code> differ, string <code>a</code> has a letter that appears later in the alphabet than the corresponding letter in <code>b</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abc&quot;, target = &quot;bba&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;bca&quot;</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The permutations of <code>s</code> (in lexicographical order) are <code>&quot;abc&quot;</code>, <code>&quot;acb&quot;</code>, <code>&quot;bac&quot;</code>, <code>&quot;bca&quot;</code>, <code>&quot;cab&quot;</code>, and <code>&quot;cba&quot;</code>.</li>
	<li>The lexicographically smallest permutation that is strictly greater than <code>target</code> is <code>&quot;bca&quot;</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;leet&quot;, target = &quot;code&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;eelt&quot;</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The permutations of <code>s</code> (in lexicographical order) are <code>&quot;eelt&quot;</code>, <code>&quot;eetl&quot;</code>, <code>&quot;elet&quot;</code>, <code>&quot;elte&quot;</code>, <code>&quot;etel&quot;</code>, <code>&quot;etle&quot;</code>, <code>&quot;leet&quot;</code>, <code>&quot;lete&quot;</code>, <code>&quot;ltee&quot;</code>, <code>&quot;teel&quot;</code>, <code>&quot;tele&quot;</code>, and <code>&quot;tlee&quot;</code>.</li>
	<li>The lexicographically smallest permutation that is strictly greater than <code>target</code> is <code>&quot;eelt&quot;</code>.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;baba&quot;, target = &quot;bbaa&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;&quot;</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The permutations of <code>s</code> (in lexicographical order) are <code>&quot;aabb&quot;</code>, <code>&quot;abab&quot;</code>, <code>&quot;abba&quot;</code>, <code>&quot;baab&quot;</code>, <code>&quot;baba&quot;</code>, and <code>&quot;bbaa&quot;</code>.</li>
	<li>None of them is lexicographically strictly greater than <code>target</code>. Therefore, the answer is <code>&quot;&quot;</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length == target.length &lt;= 300</code></li>
	<li><code>s</code> and <code>target</code> consist of only lowercase English letters.</li>
</ul>


## Hints

1. Maintain frequency counts of `s`.

2. Walk left-to-right; if equal to `target[i]` is possible, take it and continue.

3. If not, try the smallest letter strictly greater than `target[i]`.

4. If neither, backtrack left to the most recent index where you matched `target` and try to bump there.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the lexicographically smallest permutation of string 's' that is strictly greater than string 'target'. We solve this by finding the longest prefix of 'target' that can be formed using the characters available in 's'. Let this length be 'L'. Since we need a string strictly greater than 'target', we cannot simply use the entire matched prefix if it leads to a result equal to 'target'. Therefore, we backtrack from the rightmost possible index 'i', which is either the first mismatch position or the last position of the string, and try to find a character in the remaining available characters of 's' that is strictly larger than 'target[i]'.

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
    string lexGreaterPermutation(string s, string target) {
        int n = s.length();
        vector<int> counts(26, 0);
        for (char c : s) counts[c - 'a']++;

        vector<int> temp_counts = counts;
        int L = 0;
        for (int j = 0; j < n; j++) {
            int idx = target[j] - 'a';
            if (temp_counts[idx] > 0) {
                temp_counts[idx]--;
                L++;
            } else {
                break;
            }
        }

        if (L == n) {
            L = n - 1;
            temp_counts[target[n - 1] - 'a']++;
        }

        for (int i = L; i >= 0; i--) {
            int target_idx = target[i] - 'a';
            for (int char_idx = target_idx + 1; char_idx < 26; char_idx++) {
                if (temp_counts[char_idx] > 0) {
                    string res = target.substr(0, i);
                    res += (char)('a' + char_idx);
                    temp_counts[char_idx]--;
                    for (int k = 0; k < 26; k++) {
                        while (temp_counts[k] > 0) {
                            res += (char)('a' + k);
                            temp_counts[k]--;
                        }
                    }
                    return res;
                }
            }
            if (i > 0) {
                temp_counts[target[i - 1] - 'a']++;
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
    public String lexGreaterPermutation(String s, String target) {
        int n = s.length();
        int[] counts = new int[26];
        for (char c : s.toCharArray()) counts[c - 'a']++;

        int[] tempCounts = counts.clone();
        int L = 0;
        for (int j = 0; j < n; j++) {
            int idx = target.charAt(j) - 'a';
            if (tempCounts[idx] > 0) {
                tempCounts[idx]--;
                L++;
            } else {
                break;
            }
        }

        if (L == n) {
            L = n - 1;
            tempCounts[target.charAt(n - 1) - 'a']++;
        }

        for (int i = L; i >= 0; i--) {
            int targetIdx = target.charAt(i) - 'a';
            for (int charIdx = targetIdx + 1; charIdx < 26; charIdx++) {
                if (tempCounts[charIdx] > 0) {
                    StringBuilder res = new StringBuilder();
                    res.append(target.substring(0, i));
                    res.append((char) ('a' + charIdx));
                    tempCounts[charIdx]--;
                    for (int k = 0; k < 26; k++) {
                        while (tempCounts[k] > 0) {
                            res.append((char) ('a' + k));
                            tempCounts[k]--;
                        }
                    }
                    return res.toString();
                }
            }
            if (i > 0) {
                tempCounts[target.charAt(i - 1) - 'a']++;
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
    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        n = len(s)
        counts = [0] * 26
        for char in s:
            counts[ord(char) - ord('a')] += 1

        temp_counts = list(counts)
        L = 0
        for char in target:
            idx = ord(char) - ord('a')
            if temp_counts[idx] > 0:
                temp_counts[idx] -= 1
                L += 1
            else:
                break

        if L == n:
            L = n - 1
            temp_counts[ord(target[n - 1]) - ord('a')] += 1

        for i in range(L, -1, -1):
            target_char_idx = ord(target[i]) - ord('a')
            for char_idx in range(target_char_idx + 1, 26):
                if temp_counts[char_idx] > 0:
                    res = list(target[:i])
                    res.append(chr(ord('a') + char_idx))
                    temp_counts[char_idx] -= 1
                    for k in range(26):
                        while temp_counts[k] > 0:
                            res.append(chr(ord('a') + k))
                            temp_counts[k] -= 1
                    return "".join(res)

            if i > 0:
                temp_counts[ord(target[i - 1]) - ord('a')] += 1

        return ""
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = [0] * 26
        for char in s:
            counts[ord(char) - ord('a')] += 1

        temp_counts = list(counts)
        L = 0
        for char in target:
            idx = ord(char) - ord('a')
            if temp_counts[idx] > 0:
                temp_counts[idx] -= 1
                L += 1
            else:
                break

        if L == n:
            L = n - 1
            temp_counts[ord(target[n - 1]) - ord('a')] += 1

        for i in range(L, -1, -1):
            target_char_idx = ord(target[i]) - ord('a')
            for char_idx in range(target_char_idx + 1, 26):
                if temp_counts[char_idx] > 0:
                    res = list(target[:i])
                    res.append(chr(ord('a') + char_idx))
                    temp_counts[char_idx] -= 1
                    for k in range(26):
                        while temp_counts[k] > 0:
                            res.append(chr(ord('a') + k))
                            temp_counts[k] -= 1
                    return "".join(res)

            if i > 0:
                temp_counts[ord(target[i - 1]) - ord('a')] += 1

        return ""
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* lexGreaterPermutation(char* s, char* target) {
    int n = strlen(s);
    int counts[26] = {0};
    for (int i = 0; i < n; i++) counts[s[i] - 'a']++;

    int temp_counts[26];
    for (int i = 0; i < 26; i++) temp_counts[i] = counts[i];

    int L = 0;
    for (int j = 0; j < n; j++) {
        int idx = target[j] - 'a';
        if (temp_counts[idx] > 0) {
            temp_counts[idx]--;
            L++;
        } else {
            break;
        }
    }

    if (L == n) {
        L = n - 1;
        temp_counts[target[n - 1] - 'a']++;
    }

    for (int i = L; i >= 0; i--) {
        int target_idx = target[i] - 'a';
        for (int char_idx = target_idx + 1; char_idx < 26; char_idx++) {
            if (temp_counts[char_idx] > 0) {
                char* res = (char*)malloc((n + 1) * sizeof(char));
                for (int k = 0; k < i; k++) res[k] = target[k];
                res[i] = 'a' + char_idx;
                temp_counts[char_idx]--;
                int pos = i + 1;
                for (int k = 0; k < 26; k++) {
                    while (temp_counts[k] > 0) {
                        res[pos++] = 'a' + k;
                        temp_counts[k]--;
                    }
                }
                res[n] = '\0';
                return res;
            }
        }
        if (i > 0) {
            temp_counts[target[i - 1] - 'a']++;
        }
    }

    return "";
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Text;

public class Solution {
    public string LexGreaterPermutation(string s, string target) {
        int n = s.Length;
        int[] counts = new int[26];
        foreach (char c in s) {
            counts[c - 'a']++;
        }

        int matchedUntil = -1;
        for (int i = 0; i < n; i++) {
            int idx = target[i] - 'a';
            if (counts[idx] > 0) {
                counts[idx]--;
                matchedUntil = i;
            } else {
                break;
            }
        }

        for (int j = Math.Min(n - 1, matchedUntil + 1); j >= 0; j--) {
            if (j <= matchedUntil) {
                counts[target[j] - 'a']++;
            }

            for (int c = (target[j] - 'a') + 1; c < 26; c++) {
                if (counts[c] > 0) {
                    char[] result = new char[n];
                    for (int k = 0; k < j; k++) {
                        result[k] = target[k];
                    }
                    result[j] = (char)('a' + c);
                    counts[c]--;

                    int ptr = j + 1;
                    for (int k = 0; k < 26; k++) {
                        while (counts[k] > 0) {
                            result[ptr++] = (char)('a' + k);
                            counts[k]--;
                        }
                    }
                    return new string(result);
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
var lexGreaterPermutation = function(s, target) {
    const n = s.length;
    const counts = new Array(26).fill(0);
    const aCode = 'a'.charCodeAt(0);
    for (let i = 0; i < n; i++) {
        counts[s.charCodeAt(i) - aCode]++;
    }

    let matchedUntil = -1;
    for (let i = 0; i < n; i++) {
        const idx = target.charCodeAt(i) - aCode;
        if (counts[idx] > 0) {
            counts[idx]--;
            matchedUntil = i;
        } else {
            break;
        }
    }

    for (let j = Math.min(n - 1, matchedUntil + 1); j >= 0; j--) {
        if (j <= matchedUntil) {
            counts[target.charCodeAt(j) - aCode]++;
        }

        const targetCharIdx = target.charCodeAt(j) - aCode;
        for (let c = targetCharIdx + 1; c < 26; c++) {
            if (counts[c] > 0) {
                const result = new Array(n);
                for (let k = 0; k < j; k++) {
                    result[k] = target[k];
                }
                result[j] = String.fromCharCode(aCode + c);
                counts[c]--;

                let ptr = j + 1;
                for (let k = 0; k < 26; k++) {
                    while (counts[k] > 0) {
                        result[ptr++] = String.fromCharCode(aCode + k);
                        counts[k]--;
                    }
                }
                return result.join('');
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
function lexGreaterPermutation(s: string, target: string): string {
    const n = s.length;
    const counts = new Int32Array(26);
    const aCode = 'a'.charCodeAt(0);
    for (let i = 0; i < n; i++) {
        counts[s.charCodeAt(i) - aCode]++;
    }

    let matchedUntil = -1;
    for (let i = 0; i < n; i++) {
        const idx = target.charCodeAt(i) - aCode;
        if (counts[idx] > 0) {
            counts[idx]--;
            matchedUntil = i;
        } else {
            break;
        }
    }

    for (let j = Math.min(n - 1, matchedUntil + 1); j >= 0; j--) {
        if (j <= matchedUntil) {
            counts[target.charCodeAt(j) - aCode]++;
        }

        const targetCharIdx = target.charCodeAt(j) - aCode;
        for (let c = targetCharIdx + 1; c < 26; c++) {
            if (counts[c] > 0) {
                const result: string[] = new Array(n);
                for (let k = 0; k < j; k++) {
                    result[k] = target[k];
                }
                result[j] = String.fromCharCode(aCode + c);
                counts[c]--;

                let ptr = j + 1;
                for (let k = 0; k < 26; k++) {
                    while (counts[k] > 0) {
                        result[ptr++] = String.fromCharCode(aCode + k);
                        counts[k]--;
                    }
                }
                return result.join('');
            }
        }
    }

    return "";
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
     * @param String $target
     * @return String
     */
    function lexGreaterPermutation($s, $target) {
        $n = strlen($s);
        $counts = array_fill(0, 26, 0);
        $aOrd = ord('a');
        for ($i = 0; $i < $n; $i++) {
            $counts[ord($s[$i]) - $aOrd]++;
        }

        $matchedUntil = -1;
        for ($i = 0; $i < $n; $i++) {
            $idx = ord($target[$i]) - $aOrd;
            if ($counts[$idx] > 0) {
                $counts[$idx]--;
                $matchedUntil = $i;
            } else {
                break;
            }
        }

        for ($j = min($n - 1, $matchedUntil + 1); $j >= 0; $j--) {
            if ($j <= $matchedUntil) {
                $counts[ord($target[$j]) - $aOrd]++;
            }

            $targetCharIdx = ord($target[$j]) - $aOrd;
            for ($c = $targetCharIdx + 1; $c < 26; $c++) {
                if ($counts[$c] > 0) {
                    $result = array_fill(0, $n, '');
                    for ($k = 0; $k < $j; $k++) {
                        $result[$k] = $target[$k];
                    }
                    $result[$j] = chr($aOrd + $c);
                    $counts[$c]--;

                    $ptr = $j + 1;
                    for ($k = 0; $k < 26; $k++) {
                        while ($counts[$k] > 0) {
                            $result[$ptr++] = chr($aOrd + $k);
                            $counts[$k]--;
                        }
                    }
                    return implode('', $result);
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
    func lexGreaterPermutation(_ s: String, _ target: String) -> String {
        let n = s.count
        let sChars = Array(s)
        let tChars = Array(target)
        var counts = [Int](repeating: 0, count: 26)
        let aOrd = Int(UnicodeScalar("a").value)

        for char in sChars {
            counts[Int(char.unicodeScalars.first!.value) - aOrd] += 1
        }

        var matchedUntil = -1
        for i in 0..<n {
            let idx = Int(tChars[i].unicodeScalars.first!.value) - aOrd
            if counts[idx] > 0 {
                counts[idx] -= 1
                matchedUntil = i
            } else {
                break
            }
        }

        for j in stride(from: min(n - 1, matchedUntil + 1), through: 0, by: -1) {
            if j <= matchedUntil {
                let idx = Int(tChars[j].unicodeScalars.first!.value) - aOrd
                counts[idx] += 1
            }

            let targetCharIdx = Int(tChars[j].unicodeScalars.first!.value) - aOrd
            for c in (targetCharIdx + 1)..<26 {
                if counts[c] > 0 {
                    var result = [Character](repeating: " ", count: n)
                    for k in 0..<j {
                        result[k] = tChars[k]
                    }
                    result[j] = Character(UnicodeScalar(c + aOrd)!)
                    counts[c] -= 1

                    var ptr = j + 1
                    for k in 0..<26 {
                        while counts[k] > 0 {
                            result[ptr] = Character(UnicodeScalar(k + aOrd)!)
                            ptr += 1
                            counts[k] -= 1
                        }
                    }
                    return String(result)
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
    fun lexGreaterPermutation(s: String, target: String): String {
        val n = s.length
        val counts = IntArray(26)
        for (char in s) counts[char - 'a']++

        val currentCounts = counts.copyOf()
        var matchedLen = 0
        while (matchedLen < n && currentCounts[target[matchedLen] - 'a'] > 0) {
            currentCounts[target[matchedLen] - 'a']--
            matchedLen++
        }

        for (i in n - 1 downTo 0) {
            if (matchedLen > i) {
                matchedLen--
                currentCounts[target[matchedLen] - 'a']++
            }

            if (matchedLen == i) {
                val targetCharIdx = target[i] - 'a'
                for (cIdx in targetCharIdx + 1 until 26) {
                    if (currentCounts[cIdx] > 0) {
                        val res = StringBuilder()
                        res.append(target.substring(0, i))
                        res.append(('a' + cIdx).toChar())
                        currentCounts[cIdx]--
                        for (k in 0 until 26) {
                            repeat(currentCounts[k]) {
                                res.append(('a' + k).toChar())
                            }
                        }
                        return res.toString()
                    }
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
  String lexGreaterPermutation(String s, String target) {
    int n = s.length;
    List<int> counts = List.filled(26, 0);
    for (int i = 0; i < n; i++) {
      counts[s.codeUnitAt(i) - 97]++;
    }

    List<int> currentCounts = List.from(counts);
    int matchedLen = 0;
    while (matchedLen < n && currentCounts[target.codeUnitAt(matchedLen) - 97] > 0) {
      currentCounts[target.codeUnitAt(matchedLen) - 97]--;
      matchedLen++;
    }

    for (int i = n - 1; i >= 0; i--) {
      if (matchedLen > i) {
        matchedLen--;
        currentCounts[target.codeUnitAt(matchedLen) - 97]++;
      }

      if (matchedLen == i) {
        int targetCharIdx = target.codeUnitAt(i) - 97;
        for (int cIdx = targetCharIdx + 1; cIdx < 26; cIdx++) {
          if (currentCounts[cIdx] > 0) {
            StringBuffer res = StringBuffer();
            res.write(target.substring(0, i));
            res.write(String.fromCharCode(97 + cIdx));
            currentCounts[cIdx]--;
            for (int k = 0; k < 26; k++) {
              for (int j = 0; j < currentCounts[k]; j++) {
                res.write(String.fromCharCode(97 + k));
              }
            }
            return res.toString();
          }
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
func lexGreaterPermutation(s string, target string) string {
	n := len(s)
	counts := make([]int, 26)
	for i := 0; i < n; i++ {
		counts[s[i]-'a']++
	}

	currentCounts := make([]int, 26)
	copy(currentCounts, counts)
	matchedLen := 0
	for matchedLen < n && currentCounts[target[matchedLen]-'a'] > 0 {
		currentCounts[target[matchedLen]-'a']--
		matchedLen++
	}

	for i := n - 1; i >= 0; i-- {
		if matchedLen > i {
			matchedLen--
			currentCounts[target[matchedLen]-'a']++
		}

		if matchedLen == i {
			targetCharIdx := int(target[i] - 'a')
			for cIdx := targetCharIdx + 1; cIdx < 26; cIdx++ {
				if currentCounts[cIdx] > 0 {
					res := make([]byte, 0, n)
					res = append(res, target[:i]...)
					res = append(res, byte('a'+cIdx))
					currentCounts[cIdx]--
					for k := 0; k < 26; k++ {
						for j := 0; j < currentCounts[k]; j++ {
							res = append(res, byte('a'+k))
						}
					}
					return string(res)
				if }
			}
		}
	}
	return ""
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} s
# @param {String} target
# @return {String}
def lex_greater_permutation(s, target)
  n = s.length
  counts = Array.new(26, 0)
  s.each_char { |char| counts[char.ord - 'a'.ord] += 1 }

  current_counts = counts.dup
  matched_len = 0
  while matched_len < n && current_counts[target[matched_len].ord - 'a'.ord] > 0
    current_counts[target[matched_len].ord - 'a'.ord] -= 1
    matched_len += 1
  end

  (n - 1).step(0, -1) do |i|
    if matched_len > i
      matched_len -= 1
      current_counts[target[matched_len].ord - 'a'.ord] += 1
    end

    if matched_len == i
      target_char_idx = target[i].ord - 'a'.ord
      (target_char_idx + 1...26).each do |c_idx|
        if current_counts[c_idx] > 0
          res = target[0...i]
          res += ('a'.ord + c_idx).chr
          current_counts[c_idx] -= 1
          (0...26).each do |k|
            res += ('a'.ord + k).chr * current_counts[k]
          end
          return res
        end
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
    def lexGreaterPermutation(s: String, target: String): String = {
        val n = s.length
        val counts = new Array[Int](26)
        var i = 0
        while (i < n) {
            counts(s.charAt(i) - 'a') += 1
            i += 1
        }

        val currentCounts = counts.clone()
        var matchedLen = 0
        while (matchedLen < n && currentCounts(target.charAt(matchedLen) - 'a') > 0) {
            currentCounts(target.charAt(matchedLen) - 'a') -= 1
            matchedLen += 1
        }

        var idx = n - 1
        while (idx >= 0) {
            if (matchedLen > idx) {
                matchedLen -= 1
                currentCounts(target.charAt(matchedLen) - 'a') += 1
            }

            if (matchedLen == idx) {
                val targetCharIdx = target.charAt(idx) - 'a'
                var cIdx = targetCharIdx + 1
                var found = false
                while (cIdx < 26 && !found) {
                    if (currentCounts(cIdx) > 0) {
                        val res = new StringBuilder()
                        res.append(target.substring(0, idx))
                        res.append(('a' + cIdx).toChar)
                        currentCounts(cIdx) -= 1
                        var k = 0
                        while (k < 26) {
                            var count = 0
                            while (count < currentCounts(k)) {
                                res.append(('a' + k).toChar)
                                count += 1
                            }
                            k += 1
                        }
                        return res.toString()
                    }
                    cIdx += 1
                }
            }
            idx -= 1
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
    pub fn lex_greater_permutation(s: String, target: String) -> String {
        let n = s.len();
        let mut freq = [0; 26];
        for b in s.bytes() {
            freq[(b - b'a') as usize] += 1;
        }
        let target_bytes = target.as_bytes();
        let mut prefixes = Vec::with_capacity(n + 1);
        prefixes.push(freq);

        let mut last_match: i32 = -1;
        let mut current_freq = freq;
        for i in 0..n {
            let c_idx = (target_bytes[i] - b'a') as usize;
            if current_freq[c_idx] > 0 {
                current_freq[c_idx] -= 1;
                prefixes.push(current_freq);
                last_match = i as i32;
            } else {
                break;
            }
        }

        for i in (0..=std::cmp::min(last_match + 1, (n - 1) as i32)).rev() {
            let idx = i as usize;
            let f = prefixes[idx];
            let target_char_idx = (target_bytes[idx] - b'a') as usize;
            for c_idx in (target_char_idx + 1)..26 {
                if f[c_idx] > 0 {
                    let mut res = Vec::with_capacity(n);
                    res.extend_from_slice(&target_bytes[..idx]);
                    res.push(b'a' + c_idx as u8);
                    let mut remaining_freq = f;
                    remaining_freq[c_idx] -= 1;
                    for char_idx in 0..26 {
                        for _ in 0..remaining_freq[char_idx] {
                            res.push(b'a' + char_idx as u8);
                        }
                    }
                    return String::from_utf8(res).unwrap();
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
(define/contract (lex-greater-permutation s target)
  (-> string? string? string?)
  (let* ([n (string-length s)]
         [s-list (string->list s)]
         [t-list (string->list target)]
         [freq (let ([h (make-hasheqv)])
                 (for ([c s-list])
                   (hash-set! h c (+ (hash-ref h c 0) 1)))
                 h)])
    (define (build-prefixes t-list freq prefixes last-match i)
      (if (null? t-list)
          (values (reverse prefixes) last-match)
          (let* ([c (car t-list)]
                 [count (hash-ref freq c 0)])
            (if (> count 0)
                (let ([new-freq (hash-copy freq)])
                  (hash-set! new-freq c (- count 1))
                  (build-prefixes (cdr t-list) new-freq (cons new-freq prefixes) i (+ i 1)))
                (values (reverse prefixes) last-match)))))

    (let-values ([(prefixes last-match) (build-prefixes t-list freq (list freq) -1 0)])
      (let ([prefix-vec (list->vector prefixes)]
            [target-vec (list->vector t-list)])
        (let loop-i ([i (min (+ last_match 1) (- n 1))])
          (if (< i 0)
              ""
              (let* ([f (vector-ref prefix-vec i)]
                     [target-char (vector-ref target-vec i)]
                     [target-char-code (char->integer target-char)])
                (let loop-c ([c-code (+ target-char-code 1)])
                  (if (> c-code (char->integer #\z))
                      (loop-i (- i 1))
                      (let* ([c (integer->char c-code)]
                             [count (hash-ref f c 0)])
                        (if (> count 0)
                            (let* ([res-prefix (substring target 0 i)]
                                   [new-f (hash-copy f)])
                              (hash-set! new-f c (- count 1))
                              (let ([suffix (apply string-append
                                                   (map (lambda (ch-code)
                                                          (make-string (hash-ref new-f (integer->char ch-code) 0)
                                                                       (integer->char ch-code)))
                                                        (range (char->integer #\a) (+ (char->integer #\z) 1))))])
                                (string-append res-prefix (string c) suffix)))
                            (loop-c (+ c-code 1)))))))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec lex_greater_permutation(S :: unicode:unicode_binary(), Target :: unicode:unicode_binary()) -> unicode:unicode_binary().
lex_greater_permutation(S, Target) ->
  SB = binary_to_list(S),
  TB = binary_to_list(Target),
  N = length(SB),
  Freq = lists:foldl(fn(C, Acc) -> maps:put(C, maps:get(C, Acc, 0) + 1, Acc) end, #{}, SB),
  {Prefixes, LastMatch} = build_prefixes(TB, Freq, [Freq], -1, 0),
  Res = find_result(TB, list_to_tuple(Prefixes), LastMatch, N),
  list_to_binary(Res).

build_prefixes([H|T], Freq, Prefixes, LastMatch, I) ->
  Count = maps:get(H, Freq, 0),
  if Count > 0 ->
    NewFreq = maps:put(H, Count - 1, Freq),
    build_prefixes(T, NewFreq, [NewFreq|Prefixes], I, I + 1);
  true ->
    {lists:reverse(Prefixes), LastMatch}
  end;
build_prefixes([], _, Prefixes, LastMatch, _) ->
  {lists:reverse(Prefixes), LastMatch}.

find_result(TargetChars, PrefixTuple, LastMatch, N) ->
  Limit = if LastMatch + 1 < N -> LastMatch + 1; true -> N - 1 end,
  search_i(Limit, TargetChars, PrefixTuple).

search_i(I, TargetChars, PrefixTuple) when I >= 0 ->
  F = element(I + 1, PrefixTuple),
  TargetChar = lists:nth(I + 1, TargetChars),
  case search_c(TargetChar + 1, F) of
    {ok, C} ->
      Prefix = lists:sublist(TargetChars, I),
      NewF = maps:put(C, maps:get(C, F) - 1, F),
      Suffix = build_suffix(NewF),
      Prefix ++ [C] ++ Suffix;
    none ->
      search_i(I - 1, TargetChars, PrefixTuple)
  end;
search_i(_, _, _) -> "".

search_c(C, F) when C =< $z ->
  case maps:get(C, F, 0) of
    Count when Count > 0 -> {ok, C};
    _ -> search_c(C + 1, F)
  end;
search_c(_, _) -> none.

build_suffix(F) ->
  lists:flatmap(fn(C) -> lists:duplicate(maps:get(C, F, 0), C) end, lists:seq($a, $z)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec lex_greater_permutation(s :: String.t, target :: String.t) :: String.t
  def lex_greater_permutation(s, target) do
    n = String.length(s)
    s_chars = String.to_charlist(s)
    target_chars = String.to_charlist(target)

    freq = Enum.reduce(s_chars, %{}, fn char, acc -> Map.update(acc, char, 1, &(&1 + 1)) end)

    {prefixes, last_match} = build_prefixes(target_chars, freq, [freq], -1, 0)
    prefix_vec = List.to_tuple(prefixes)
    target_vec = List.to_tuple(target_chars)

    limit = min(last_match + 1, n - 1)

    Enum.find_value(limit..0, "", fn i ->
      f = elem(prefix_vec, i)
      target_char = elem(target_vec, i)
      c_range = if target_char < ?z, do: (target_char + 1)..?z, else: []

      Enum.find_value(c_range, fn c ->
        if Map.get(f, c, 0) > 0 do
          res_prefix = Enum.take(target_chars, i)
          new_f = Map.update!(f, c, &(&1 - 1))
          suffix = Enum.flat_map(?a..?z, fn char_code ->
            List.duplicate(char_code, Map.get(new_f, char_code, 0))
          end)
          List.to_string(res_prefix ++ [c] ++ suffix)
        else
          nil
        end
      end)
    end)
  end

  defp build_prefixes([h | t], freq, prefixes, last_match, i) do
    count = Map.get(freq, h, 0)
    if count > 0 do
      new_freq = Map.update!(freq, h, &(&1 - 1))
      build_prefixes(t, new_freq, [new_freq | prefixes], i, i + 1)
    else
      {Enum.reverse(prefixes), last_match}
    end
  end
  defp build_prefixes([], _freq, prefixes, last_match, _i) do
    {Enum.reverse(prefixes), last_match}
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n * K) where n is the length of the string and K is the size of the lowercase English alphabet (26). We perform a linear scan to find the longest matching prefix and then a backward scan of at most n steps. In each step, we check up to K characters to find a lexicographically larger one, and building the final string takes O(n) time.
- **Space Complexity:** O(n + K) where n is the length of the string and K is the alphabet size (26). We store the frequency count of characters in an array of size K and build the output string of length n.
