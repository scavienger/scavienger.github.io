---
layout: post
title: "Find the Lexicographically Smallest Valid Sequence"
date: 2026-08-08 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Two Pointers", "String", "Dynamic Programming", "Greedy"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> validSequence(string word1, string\
        \ word2) {\n        int n = word1.length();\n        int m = word2.length();\n\
        \        vector<int> suffix(n + 1, 0);\n        for (int i = n - 1; i >= 0;\
        \ i--) {\n            suffix[i] = suffix[i + 1];\n            if (suffix[i +\
        \ 1] < m && word1[i] == word2[m - 1 - suffix[i + 1]]) {\n                suffix[i]\
        \ = suffix[i + 1] + 1;\n            }\n        }\n\n        vector<int> res;\n\
        \        int i = 0;\n        bool changed = false;\n        for (int j = 0;\
        \ j < m; j++) {\n            bool found = false;\n            while (i < n)\
        \ {\n                if (word1[i] == word2[j]) {\n                    bool can_finish\
        \ = changed ? (suffix[i + 1] >= m - j - 1) : (suffix[i + 1] >= m - j - 2);\n\
        \                    if (can_finish) {\n                        res.push_back(i);\n\
        \                        i++;\n                        found = true;\n     \
        \                   break;\n                    }\n                } else if\
        \ (!changed) {\n                    if (suffix[i + 1] >= m - j - 1) {\n    \
        \                    changed = true;\n                        res.push_back(i);\n\
        \                        i++;\n                        found = true;\n     \
        \                   break;\n                    }\n                }\n     \
        \           i++;\n            }\n            if (!found) return {};\n      \
        \  }\n        return res;\n    }\n};"
      java: "class Solution {\n    public int[] validSequence(String word1, String word2)\
        \ {\n        int n = word1.length();\n        int m = word2.length();\n    \
        \    int[] suffix = new int[n + 1];\n        for (int i = n - 1; i >= 0; i--)\
        \ {\n            suffix[i] = suffix[i + 1];\n            if (suffix[i + 1] <\
        \ m && word1.charAt(i) == word2.charAt(m - 1 - suffix[i + 1])) {\n         \
        \       suffix[i] = suffix[i + 1] + 1;\n            }\n        }\n\n       \
        \ int[] res = new int[m];\n        int i = 0;\n        boolean changed = false;\n\
        \        for (int j = 0; j < m; j++) {\n            boolean found = false;\n\
        \            while (i < n) {\n                if (word1.charAt(i) == word2.charAt(j))\
        \ {\n                    boolean canFinish = changed ? (suffix[i + 1] >= m -\
        \ j - 1) : (suffix[i + 1] >= m - j - 2);\n                    if (canFinish)\
        \ {\n                        res[j] = i;\n                        i++;\n   \
        \                     found = true;\n                        break;\n      \
        \              }\n                } else if (!changed) {\n                 \
        \   if (suffix[i + 1] >= m - j - 1) {\n                        res[j] = i;\n\
        \                        changed = true;\n                        i++;\n   \
        \                     found = true;\n                        break;\n      \
        \              }\n                }\n                i++;\n            }\n \
        \           if (!found) return new int[0];\n        }\n        return res;\n\
        \    }\n}"
      python: "class Solution(object):\n    def validSequence(self, word1, word2):\n\
        \        \"\"\"\n        :type word1: str\n        :type word2: str\n      \
        \  :rtype: List[int]\n        \"\"\"\n        n = len(word1)\n        m = len(word2)\n\
        \        suffix = [0] * (n + 1)\n        for i in range(n - 1, -1, -1):\n  \
        \          suffix[i] = suffix[i+1]\n            if suffix[i+1] < m and word1[i]\
        \ == word2[m - 1 - suffix[i+1]]:\n                suffix[i] = suffix[i+1] +\
        \ 1\n\n        res = []\n        i = 0\n        changed = False\n        for\
        \ j in range(m):\n            found = False\n            while i < n:\n    \
        \            if word1[i] == word2[j]:\n                    can_finish = (suffix[i+1]\
        \ >= m - j - 1) if changed else (suffix[i+1] >= m - j - 2)\n               \
        \     if can_finish:\n                        res.append(i)\n              \
        \          i += 1\n                        found = True\n                  \
        \      break\n                elif not changed:\n                    if suffix[i+1]\
        \ >= m - j - 1:\n                        res.append(i)\n                   \
        \     changed = True\n                        i += 1\n                     \
        \   found = True\n                        break\n                i += 1\n  \
        \          if not found:\n                return []\n        return res"
      python3: "class Solution:\n    def validSequence(self, word1: str, word2: str)\
        \ -> List[int]:\n        n, m = len(word1), len(word2)\n        suffix = [0]\
        \ * (n + 1)\n        for i in range(n - 1, -1, -1):\n            suffix[i] =\
        \ suffix[i + 1]\n            if suffix[i + 1] < m and word1[i] == word2[m -\
        \ 1 - suffix[i + 1]]:\n                suffix[i] = suffix[i + 1] + 1\n\n   \
        \     res = []\n        i = 0\n        changed = False\n        for j in range(m):\n\
        \            found = False\n            while i < n:\n                if word1[i]\
        \ == word2[j]:\n                    can_finish = (suffix[i + 1] >= m - j - 1)\
        \ if changed else (suffix[i + 1] >= m - j - 2)\n                    if can_finish:\n\
        \                        res.append(i)\n                        i += 1\n   \
        \                     found = True\n                        break\n        \
        \        elif not changed:\n                    if suffix[i + 1] >= m - j -\
        \ 1:\n                        res.append(i)\n                        changed\
        \ = True\n                        i += 1\n                        found = True\n\
        \                        break\n                i += 1\n            if not found:\n\
        \                return []\n        return res"
      c: "#include <stdlib.h>\n#include <string.h>\n#include <stdbool.h>\n\n/**\n *\
        \ Note: The returned array must be malloced, assume caller calls free().\n */\n\
        int* validSequence(char* word1, char* word2, int* returnSize) {\n    int n =\
        \ (int)strlen(word1);\n    int m = (int)strlen(word2);\n    int* suffix = (int*)calloc(n\
        \ + 1, sizeof(int));\n\n    for (int i = n - 1; i >= 0; i--) {\n        suffix[i]\
        \ = suffix[i + 1];\n        if (suffix[i + 1] < m && word1[i] == word2[m - 1\
        \ - suffix[i + 1]]) {\n            suffix[i] = suffix[i + 1] + 1;\n        }\n\
        \    }\n\n    int* res = (int*)malloc(m * sizeof(int));\n    int i = 0;\n  \
        \  bool changed = false;\n    int count = 0;\n\n    for (int j = 0; j < m; j++)\
        \ {\n        bool found = false;\n        while (i < n) {\n            if (word1[i]\
        \ == word2[j]) {\n                bool can_finish = changed ? (suffix[i + 1]\
        \ >= m - j - 1) : (suffix[i + 1] >= m - j - 2);\n                if (can_finish)\
        \ {\n                    res[count++] = i;\n                    i++;\n     \
        \               found = true;\n                    break;\n                }\n\
        \            } else if (!changed) {\n                if (suffix[i + 1] >= m\
        \ - j - 1) {\n                    changed = true;\n                    res[count++]\
        \ = i;\n                    i++;\n                    found = true;\n      \
        \              break;\n                }\n            }\n            i++;\n\
        \        }\n        if (!found) {\n            free(suffix);\n            free(res);\n\
        \            *returnSize = 0;\n            return NULL;\n        }\n    }\n\n\
        \    free(suffix);\n    *returnSize = m;\n    return res;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int[] ValidSequence(string word1, string word2) {\n        int\
        \ n = word1.Length;\n        int m = word2.Length;\n\n        int[] suffixMatch\
        \ = new int[m + 1];\n        for (int i = 0; i <= m; i++) suffixMatch[i] = -1;\n\
        \        suffixMatch[m] = n;\n\n        int curr = n - 1;\n        for (int\
        \ j = m - 1; j >= 0; j--) {\n            while (curr >= 0 && word1[curr] !=\
        \ word2[j]) {\n                curr--;\n            }\n            if (curr\
        \ >= 0) {\n                suffixMatch[j] = curr;\n                curr--;\n\
        \            }\n        }\n\n        List<int> result = new List<int>();\n \
        \       bool usedChange = false;\n        int w1Idx = 0;\n\n        for (int\
        \ w2Idx = 0; w2Idx < m; w2Idx++) {\n            bool found = false;\n      \
        \      while (w1Idx < n) {\n                if (word1[w1Idx] == word2[w2Idx])\
        \ {\n                    if (!usedChange || suffixMatch[w2Idx + 1] > w1Idx)\
        \ {\n                        result.Add(w1Idx);\n                        w1Idx++;\n\
        \                        found = true;\n                        break;\n   \
        \                 }\n                } else if (!usedChange && suffixMatch[w2Idx\
        \ + 1] > w1Idx) {\n                    result.Add(w1Idx);\n                \
        \    usedChange = true;\n                    w1Idx++;\n                    found\
        \ = true;\n                    break;\n                }\n                w1Idx++;\n\
        \            }\n\n            if (!found) return new int[0];\n        }\n\n\
        \        return result.ToArray();\n    }\n}"
      javascript: "/**\n * @param {string} word1\n * @param {string} word2\n * @return\
        \ {number[]}\n */\nvar validSequence = function(word1, word2) {\n    const n\
        \ = word1.length;\n    const m = word2.length;\n\n    const suffixMatch = new\
        \ Int32Array(m + 1).fill(-1);\n    suffixMatch[m] = n;\n\n    let curr = n -\
        \ 1;\n    for (let j = m - 1; j >= 0; j--) {\n        while (curr >= 0 && word1[curr]\
        \ !== word2[j]) {\n            curr--;\n        }\n        if (curr >= 0) {\n\
        \            suffixMatch[j] = curr;\n            curr--;\n        }\n    }\n\
        \n    const seq = [];\n    let usedChange = false;\n    let w1Idx = 0;\n\n \
        \   for (let w2Idx = 0; w2Idx < m; w2Idx++) {\n        let found = false;\n\
        \        while (w1Idx < n) {\n            if (word1[w1Idx] === word2[w2Idx])\
        \ {\n                if (!usedChange || suffixMatch[w2Idx + 1] > w1Idx) {\n\
        \                    seq.push(w1Idx);\n                    w1Idx++;\n      \
        \              found = true;\n                    break;\n                }\n\
        \            } else if (!usedChange && suffixMatch[w2Idx + 1] > w1Idx) {\n \
        \               seq.push(w1Idx);\n                usedChange = true;\n     \
        \           w1Idx++;\n                found = true;\n                break;\n\
        \            }\n            w1Idx++;\n        }\n\n        if (!found) return\
        \ [];\n    }\n\n    return seq;\n};"
      typescript: "function validSequence(word1: string, word2: string): number[] {\n\
        \    const n = word1.length;\n    const m = word2.length;\n\n    const suffixMatch\
        \ = new Int32Array(m + 1).fill(-1);\n    suffixMatch[m] = n;\n\n    let curr\
        \ = n - 1;\n    for (let j = m - 1; j >= 0; j--) {\n        while (curr >= 0\
        \ && word1[curr] !== word2[j]) {\n            curr--;\n        }\n        if\
        \ (curr >= 0) {\n            suffixMatch[j] = curr;\n            curr--;\n \
        \       }\n    }\n\n    const seq: number[] = [];\n    let usedChange = false;\n\
        \    let w1Idx = 0;\n\n    for (let w2Idx = 0; w2Idx < m; w2Idx++) {\n     \
        \   let found = false;\n        while (w1Idx < n) {\n            if (word1[w1Idx]\
        \ === word2[w2Idx]) {\n                if (!usedChange || suffixMatch[w2Idx\
        \ + 1] > w1Idx) {\n                    seq.push(w1Idx);\n                  \
        \  w1Idx++;\n                    found = true;\n                    break;\n\
        \                }\n            } else if (!usedChange && suffixMatch[w2Idx\
        \ + 1] > w1Idx) {\n                seq.push(w1Idx);\n                usedChange\
        \ = true;\n                w1Idx++;\n                found = true;\n       \
        \         break;\n            }\n            w1Idx++;\n        }\n\n       \
        \ if (!found) return [];\n    }\n\n    return seq;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $word1\n     * @param\
        \ String $word2\n     * @return Integer[]\n     */\n    function validSequence($word1,\
        \ $word2) {\n        $n = strlen($word1);\n        $m = strlen($word2);\n\n\
        \        $suffixMatch = array_fill(0, $m + 1, -1);\n        $suffixMatch[$m]\
        \ = $n;\n\n        $curr = $n - 1;\n        for ($j = $m - 1; $j >= 0; $j--)\
        \ {\n            while ($curr >= 0 && $word1[$curr] !== $word2[$j]) {\n    \
        \            $curr--;\n            }\n            if ($curr >= 0) {\n      \
        \          $suffixMatch[$j] = $curr;\n                $curr--;\n           \
        \ }\n        }\n\n        $seq = [];\n        $usedChange = false;\n       \
        \ $w1Idx = 0;\n\n        for ($w2Idx = 0; $w2Idx < $m; $w2Idx++) {\n       \
        \     $found = false;\n            while ($w1Idx < $n) {\n                if\
        \ ($word1[$w1Idx] === $word2[$w2Idx]) {\n                    if (!$usedChange\
        \ || $suffixMatch[$w2Idx + 1] > $w1Idx) {\n                        $seq[] =\
        \ $w1Idx;\n                        $w1Idx++;\n                        $found\
        \ = true;\n                        break;\n                    }\n         \
        \       } else if (!$usedChange && $suffixMatch[$w2Idx + 1] > $w1Idx) {\n  \
        \                  $seq[] = $w1Idx;\n                    $usedChange = true;\n\
        \                    $w1Idx++;\n                    $found = true;\n       \
        \             break;\n                }\n                $w1Idx++;\n       \
        \     }\n\n            if (!$found) return [];\n        }\n\n        return\
        \ $seq;\n    }\n}"
      swift: "class Solution {\n    func validSequence(_ word1: String, _ word2: String)\
        \ -> [Int] {\n        let s1 = Array(word1)\n        let s2 = Array(word2)\n\
        \        let n = s1.count\n        let m = s2.count\n\n        var suffixMatch\
        \ = Array(repeating: -1, count: m + 1)\n        suffixMatch[m] = n\n\n     \
        \   var curr = n - 1\n        for j in stride(from: m - 1, through: 0, by: -1)\
        \ {\n            while curr >= 0 && s1[curr] != s2[j] {\n                curr\
        \ -= 1\n            }\n            if curr >= 0 {\n                suffixMatch[j]\
        \ = curr\n                curr -= 1\n            }\n        }\n\n        var\
        \ seq = [Int]()\n        var usedChange = false\n        var w1Idx = 0\n\n \
        \       for w2Idx in 0..<m {\n            var found = false\n            while\
        \ w1Idx < n {\n                if s1[w1Idx] == s2[w2Idx] {\n               \
        \     if !usedChange || suffixMatch[w2Idx + 1] > w1Idx {\n                 \
        \       seq.append(w1Idx)\n                        w1Idx += 1\n            \
        \            found = true\n                        break\n                 \
        \   }\n                } else if !usedChange && suffixMatch[w2Idx + 1] > w1Idx\
        \ {\n                    seq.append(w1Idx)\n                    usedChange =\
        \ true\n                    w1Idx += 1\n                    found = true\n \
        \                   break\n                }\n                w1Idx += 1\n \
        \           }\n\n            if !found {\n                return []\n      \
        \      }\n        }\n\n        return seq\n    }\n}"
      kotlin: "class Solution {\n    fun validSequence(word1: String, word2: String):\
        \ IntArray {\n        val n = word1.length\n        val m = word2.length\n \
        \       val suffixMatch = IntArray(n + 1)\n        var p2 = m - 1\n        for\
        \ (i in n - 1 downTo 0) {\n            suffixMatch[i] = suffixMatch[i + 1]\n\
        \            if (p2 >= 0 && word1[i] == word2[p2]) {\n                suffixMatch[i]++\n\
        \                p2--\n            }\n        }\n\n        val res = IntArray(m)\n\
        \        var usedChange = false\n        var p1 = 0\n        for (p2Idx in 0\
        \ until m) {\n            var found = false\n            while (p1 < n) {\n\
        \                if (word1[p1] == word2[p2Idx]) {\n                    res[p2Idx]\
        \ = p1\n                    p1++\n                    found = true\n       \
        \             break\n                } else if (!usedChange && suffixMatch[p1\
        \ + 1] >= m - 1 - p2Idx) {\n                    res[p2Idx] = p1\n          \
        \          p1++\n                    usedChange = true\n                   \
        \ found = true\n                    break\n                } else {\n      \
        \              p1++\n                }\n            }\n            if (!found)\
        \ return intArrayOf()\n        }\n        return res\n    }\n}"
      dart: "class Solution {\n  List<int> validSequence(String word1, String word2)\
        \ {\n    int n = word1.length;\n    int m = word2.length;\n    List<int> suffixMatch\
        \ = List.filled(n + 1, 0);\n    int p2 = m - 1;\n    for (int i = n - 1; i >=\
        \ 0; i--) {\n      suffixMatch[i] = suffixMatch[i + 1];\n      if (p2 >= 0 &&\
        \ word1[i] == word2[p2]) {\n        suffixMatch[i] += 1;\n        p2 -= 1;\n\
        \      }\n    }\n\n    List<int> res = [];\n    bool usedChange = false;\n \
        \   int p1 = 0;\n    for (int p2Idx = 0; p2Idx < m; p2Idx++) {\n      bool found\
        \ = false;\n      while (p1 < n) {\n        if (word1[p1] == word2[p2Idx]) {\n\
        \          res.add(p1);\n          p1++;\n          found = true;\n        \
        \  break;\n        } else if (!usedChange && suffixMatch[p1 + 1] >= m - 1 -\
        \ p2Idx) {\n          res.add(p1);\n          p1++;\n          usedChange =\
        \ true;\n          found = true;\n          break;\n        } else {\n     \
        \     p1++;\n        }\n      }\n      if (!found) return [];\n    }\n    return\
        \ res;\n  }\n}"
      go: "func validSequence(word1 string, word2 string) []int {\n    n := len(word1)\n\
        \    m := len(word2)\n    suffixMatch := make([]int, n+1)\n    p2 := m - 1\n\
        \    for i := n - 1; i >= 0; i-- {\n        suffixMatch[i] = suffixMatch[i+1]\n\
        \        if p2 >= 0 && word1[i] == word2[p2] {\n            suffixMatch[i]++\n\
        \            p2--\n        }\n    }\n\n    res := make([]int, 0, m)\n    usedChange\
        \ := false\n    p1 := 0\n    for p2Idx := 0; p2Idx < m; p2Idx++ {\n        found\
        \ := false\n        for p1 < n {\n            if word1[p1] == word2[p2Idx] {\n\
        \                res = append(res, p1)\n                p1++\n             \
        \   found = true\n                break\n            } else if !usedChange &&\
        \ suffixMatch[p1+1] >= m-1-p2Idx {\n                res = append(res, p1)\n\
        \                p1++\n                usedChange = true\n                found\
        \ = true\n                break\n            } else {\n                p1++\n\
        \            }\n        }\n        if !found {\n            return []int{}\n\
        \        }\n    }\n    return res\n}"
      ruby: "# @param {String} word1\n# @param {String} word2\n# @return {Integer[]}\n\
        def valid_sequence(word1, word2)\n  n = word1.length\n  m = word2.length\n \
        \ suffix_match = Array.new(n + 1, 0)\n  p2 = m - 1\n  (n - 1).downto(0) do |i|\n\
        \    suffix_match[i] = suffix_match[i + 1]\n    if p2 >= 0 && word1[i] == word2[p2]\n\
        \      suffix_match[i] += 1\n      p2 -= 1\n    end\n  end\n\n  res = []\n \
        \ used_change = false\n  p1 = 0\n  (0...m).each do |p2_idx|\n    found = false\n\
        \    while p1 < n\n      if word1[p1] == word2[p2_idx]\n        res << p1\n\
        \        p1 += 1\n        found = true\n        break\n      elsif !used_change\
        \ && suffix_match[p1 + 1] >= m - 1 - p2_idx\n        res << p1\n        p1 +=\
        \ 1\n        used_change = true\n        found = true\n        break\n     \
        \ else\n        p1 += 1\n      end\n    end\n    return [] unless found\n  end\n\
        \  res\nend"
      scala: "object Solution {\n  def validSequence(word1: String, word2: String):\
        \ Array[Int] = {\n    val n = word1.length\n    val m = word2.length\n    val\
        \ suffixMatch = new Array[Int](n + 1)\n    var p2 = m - 1\n    for (i <- n -\
        \ 1 to 0 by -1) {\n      suffixMatch(i) = suffixMatch(i + 1)\n      if (p2 >=\
        \ 0 && word1(i) == word2(p2)) {\n        suffixMatch(i) += 1\n        p2 -=\
        \ 1\n      }\n    }\n\n    val res = new scala.collection.mutable.ArrayBuffer[Int]()\n\
        \    var usedChange = false\n    var p1 = 0\n    for (p2Idx <- 0 until m) {\n\
        \      var found = false\n      while (p1 < n && !found) {\n        if (word1(p1)\
        \ == word2(p2Idx)) {\n          res += p1\n          p1 += 1\n          found\
        \ = true\n        } else if (!usedChange && suffixMatch(p1 + 1) >= m - 1 - p2Idx)\
        \ {\n          res += p1\n          p1 += 1\n          usedChange = true\n \
        \         found = true\n        } else {\n          p1 += 1\n        }\n   \
        \   }\n      if (!found) return Array[Int]()\n    }\n    res.toArray\n  }\n}"
      rust: "impl Solution {\n    pub fn valid_sequence(word1: String, word2: String)\
        \ -> Vec<i32> {\n        let n = word1.len();\n        let m = word2.len();\n\
        \        let w1 = word1.as_bytes();\n        let w2 = word2.as_bytes();\n  \
        \      let mut dp = vec![0; n + 1];\n\n        for i in (0..n).rev() {\n   \
        \         dp[i] = dp[i + 1];\n            if dp[i] < m && w1[i] == w2[m - 1\
        \ - dp[i]] {\n                dp[i] += 1;\n            }\n        }\n\n    \
        \    let mut ans = Vec::with_capacity(m);\n        let mut p1 = 0;\n       \
        \ let mut changed = false;\n\n        for p2 in 0..m {\n            let mut\
        \ found = false;\n            while p1 < n {\n                let match_char\
        \ = w1[p1] == w2[p2];\n                let can_skip = !changed && dp[p1 + 1]\
        \ >= (m - 1 - p2);\n                if match_char || can_skip {\n          \
        \          if !match_char {\n                        changed = true;\n     \
        \               }\n                    ans.push(p1 as i32);\n              \
        \      p1 += 1;\n                    found = true;\n                    break;\n\
        \                }\n                p1 += 1;\n            }\n            if\
        \ !found {\n                return vec![];\n            }\n        }\n\n   \
        \     ans\n    }\n}"
      racket: "(define/contract (valid-sequence word1 word2)\n  (-> string? string?\
        \ (listof exact-integer?))\n  (let* ([n (string-length word1)]\n         [m\
        \ (string-length word2)]\n         [dp (make-vector (+ n 1) 0)])\n    (for ([i\
        \ (in-range (- n 1) -1 -1)])\n      (let ([char1 (string-ref word1 i)]\n   \
        \         [next-dp (vector-ref dp (+ i 1))])\n        (if (and (< next-dp m)\n\
        \                 (char=? char1 (string-ref word2 (- m 1 next-dp))))\n     \
        \       (vector-set! dp i (+ next-dp 1))\n            (vector-set! dp i next-dp))))\n\
        \    (let loop ([p1 0] [p2 0] [changed #f] [ans '()])\n      (cond\n       \
        \ [(= p2 m) (reverse ans)]\n        [(= p1 n) '()]\n        [else\n        \
        \ (let* ([char1 (string-ref word1 p1)]\n                [char2 (string-ref word2\
        \ p2)]\n                [match? (char=? char1 char2)]\n                [can-skip?\
        \ (and (not changed)\n                                (>= (vector-ref dp (+\
        \ p1 1)) (- m 1 p2)))])\n           (if (or match? can-skip?)\n            \
        \   (loop (+ p1 1) (+ p2 1) (if match? changed #t) (cons p1 ans))\n        \
        \       (loop (+ p1 1) p2 changed ans)))]))))"
      erlang: "-spec valid_sequence(Word1 :: unicode:unicode_binary(), Word2 :: unicode:unicode_binary())\
        \ -> [integer()].\nvalid_sequence(Word1, Word2) ->\n    N = byte_size(Word1),\n\
        \    M = byte_size(Word2),\n    DPList = build_dp(N - 1, 0, Word1, Word2, M,\
        \ [0]),\n    solve(0, 0, false, Word1, Word2, N, M, DPList, []).\n\nbuild_dp(I,\
        \ PrevDP, W1, W2, M, Acc) when I >= 0 ->\n    Char1 = binary:at(W1, I),\n  \
        \  NextDP = if (PrevDP < M) andalso (Char1 =:= binary:at(W2, M - 1 - PrevDP))\
        \ ->\n                  PrevDP + 1;\n              true ->\n               \
        \   PrevDP\n             end,\n    build_dp(I - 1, NextDP, W1, W2, M, [NextDP\
        \ | Acc]);\nbuild_dp(-1, _, _, _, _, Acc) ->\n    Acc.\n\nsolve(P2, _P1, _Changed,\
        \ _W1, _W2, _N, M, _DPList, Ans) when P2 =:= M ->\n    lists:reverse(Ans);\n\
        solve(_P2, P1, _Changed, _W1, _W2, N, _M, _DPList, _Ans) when P1 =:= N ->\n\
        \    [];\nsolve(P2, P1, Changed, W1, W2, N, M, [_DP_P1 | [DP_P1plus1 | _] =\
        \ RestDP], Ans) ->\n    Match = binary:at(W1, P1) =:= binary:at(W2, P2),\n \
        \   CanSkip = (not Changed) andalso (DP_P1plus1 >= (M - 1 - P2)),\n    if\n\
        \        Match -> solve(P2 + 1, P1 + 1, Changed, W1, W2, N, M, RestDP, [P1 |\
        \ Ans]);\n        CanSkip -> solve(P2 + 1, P1 + 1, true, W1, W2, N, M, RestDP,\
        \ [P1 | Ans]);\n        true -> solve(P2, P1 + 1, Changed, W1, W2, N, M, RestDP,\
        \ Ans)\n    end."
      elixir: "defmodule Solution do\n  @spec valid_sequence(word1 :: String.t, word2\
        \ :: String.t) :: [integer]\n  def valid_sequence(word1, word2) do\n    n =\
        \ byte_size(word1)\n    m = byte_size(word2)\n    dp_list = build_dp(n - 1,\
        \ 0, word1, word2, m, [0])\n    solve(0, 0, false, word1, word2, n, m, dp_list,\
        \ [])\n  end\n\n  defp build_dp(i, prev_dp, w1, w2, m, acc) when i >= 0 do\n\
        \    char1 = :binary.at(w1, i)\n    next_dp = if prev_dp < m and char1 == :binary.at(w2,\
        \ m - 1 - prev_dp) do\n      prev_dp + 1\n    else\n      prev_dp\n    end\n\
        \    build_dp(i - 1, next_dp, w1, w2, m, [next_dp | acc])\n  end\n  defp build_dp(-1,\
        \ _prev_dp, _w1, _w2, _m, acc), do: acc\n\n  defp solve(p2, _p1, _changed, _w1,\
        \ _w2, _n, m, _dp_list, ans) when p2 == m do\n    Enum.reverse(ans)\n  end\n\
        \  defp solve(_p2, p1, _changed, _w1, _w2, n, _m, _dp_list, _ans) when p1 ==\
        \ n do\n    []\n  end\n  defp solve(p2, p1, changed, w1, w2, n, m, [_dp_p1 |\
        \ [dp_p1plus1 | _] = rest_dp], ans) do\n    char1 = :binary.at(w1, p1)\n   \
        \ char2 = :binary.at(w2, p2)\n    match = char1 == char2\n    can_skip = (not\
        \ changed) and (dp_p1plus1 >= m - 1 - p2)\n    if match or can_skip do\n   \
        \   solve(p2 + 1, p1 + 1, (if match, do: changed, else: true), w1, w2, n, m,\
        \ rest_dp, [p1 | ans])\n    else\n      solve(p2, p1 + 1, changed, w1, w2, n,\
        \ m, rest_dp, ans)\n    end\n  end\nend"
    approach: To find the lexicographically smallest sequence, we can use a greedy approach
      combined with precomputed information about the suffixes of the strings. We precalculate
      an array `suffix` where `suffix[i]` represents the length of the longest suffix
      of `word2` that can be matched as a subsequence in the suffix of `word1` starting
      from index `i`. This array allows us to quickly determine if the remaining portion
      of `word2` can be completed as a subsequence in the remaining portion of `word1`
      with a specific number of changes (either zero or one).
    time_complexity: O(N + M) where N is the length of `word1` and M is the length of
      `word2`. The precomputation of the `suffix` array takes O(N) time, and the greedy
      construction of the index sequence takes O(N + M) time because we iterate through
      `word1` and `word2` at most once.
    space_complexity: O(N) to store the `suffix` array, which holds values for each
      index in `word1`. The resulting index sequence also takes O(M) space.
    elapsed_time: 352.72173595428467
    model: gemini-3-flash-preview
    generated_at: '2026-08-08 01:08:15 '
---

## Problem #3302: Find the Lexicographically Smallest Valid Sequence

**Difficulty:** Medium

**Topics:** Two Pointers, String, Dynamic Programming, Greedy

## Problem Description

<p>You are given two strings <code>word1</code> and <code>word2</code>.</p>

<p>A string <code>x</code> is called <strong>almost equal</strong> to <code>y</code> if you can change <strong>at most</strong> one character in <code>x</code> to make it <em>identical</em> to <code>y</code>.</p>

<p>A sequence of indices <code>seq</code> is called <strong>valid</strong> if:</p>

<ul>
	<li>The indices are sorted in <strong>ascending</strong> order.</li>
	<li><em>Concatenating</em> the characters at these indices in <code>word1</code> in <strong>the same</strong> order results in a string that is <strong>almost equal</strong> to <code>word2</code>.</li>
</ul>

<p>Return an array of size <code>word2.length</code> representing the <span data-keyword="lexicographically-smaller-array">lexicographically smallest</span> <strong>valid</strong> sequence of indices. If no such sequence of indices exists, return an <strong>empty</strong> array.</p>

<p><strong>Note</strong> that the answer must represent the <em>lexicographically smallest array</em>, <strong>not</strong> the corresponding string formed by those indices.<!-- notionvc: 2ff8e782-bd6f-4813-a421-ec25f7e84c1e --></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word1 = &quot;vbcca&quot;, word2 = &quot;abc&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,1,2]</span></p>

<p><strong>Explanation:</strong></p>

<p>The lexicographically smallest valid sequence of indices is <code>[0, 1, 2]</code>:</p>

<ul>
	<li>Change <code>word1[0]</code> to <code>&#39;a&#39;</code>.</li>
	<li><code>word1[1]</code> is already <code>&#39;b&#39;</code>.</li>
	<li><code>word1[2]</code> is already <code>&#39;c&#39;</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word1 = &quot;bacdc&quot;, word2 = &quot;abc&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,2,4]</span></p>

<p><strong>Explanation:</strong></p>

<p>The lexicographically smallest valid sequence of indices is <code>[1, 2, 4]</code>:</p>

<ul>
	<li><code>word1[1]</code> is already <code>&#39;a&#39;</code>.</li>
	<li>Change <code>word1[2]</code> to <code>&#39;b&#39;</code>.</li>
	<li><code>word1[4]</code> is already <code>&#39;c&#39;</code>.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word1 = &quot;aaaaaa&quot;, word2 = &quot;aaabc&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">[]</span></p>

<p><strong>Explanation:</strong></p>

<p>There is no valid sequence of indices.</p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word1 = &quot;abc&quot;, word2 = &quot;ab&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,1]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word2.length &lt; word1.length &lt;= 3 * 10<sup>5</sup></code></li>
	<li><code>word1</code> and <code>word2</code> consist only of lowercase English letters.</li>
</ul>


## Hints

1. Let `dp[i]` be the longest suffix of `word2` that exists as a subsequence of suffix of the substring of `word1` starting at index `i`.

2. If `dp[i + 1] < m` and `word1[i] == word2[m - dp[i + 1] - 1]`,`dp[i] =  dp[i + 1] + 1`. Otherwise, `dp[i] =  dp[i + 1]`.

3. For each index `i`, greedily select characters using the `dp` array to know whether a solution exists.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To find the lexicographically smallest sequence, we can use a greedy approach combined with precomputed information about the suffixes of the strings. We precalculate an array `suffix` where `suffix[i]` represents the length of the longest suffix of `word2` that can be matched as a subsequence in the suffix of `word1` starting from index `i`. This array allows us to quickly determine if the remaining portion of `word2` can be completed as a subsequence in the remaining portion of `word1` with a specific number of changes (either zero or one).

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
    vector<int> validSequence(string word1, string word2) {
        int n = word1.length();
        int m = word2.length();
        vector<int> suffix(n + 1, 0);
        for (int i = n - 1; i >= 0; i--) {
            suffix[i] = suffix[i + 1];
            if (suffix[i + 1] < m && word1[i] == word2[m - 1 - suffix[i + 1]]) {
                suffix[i] = suffix[i + 1] + 1;
            }
        }

        vector<int> res;
        int i = 0;
        bool changed = false;
        for (int j = 0; j < m; j++) {
            bool found = false;
            while (i < n) {
                if (word1[i] == word2[j]) {
                    bool can_finish = changed ? (suffix[i + 1] >= m - j - 1) : (suffix[i + 1] >= m - j - 2);
                    if (can_finish) {
                        res.push_back(i);
                        i++;
                        found = true;
                        break;
                    }
                } else if (!changed) {
                    if (suffix[i + 1] >= m - j - 1) {
                        changed = true;
                        res.push_back(i);
                        i++;
                        found = true;
                        break;
                    }
                }
                i++;
            }
            if (!found) return {};
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
    public int[] validSequence(String word1, String word2) {
        int n = word1.length();
        int m = word2.length();
        int[] suffix = new int[n + 1];
        for (int i = n - 1; i >= 0; i--) {
            suffix[i] = suffix[i + 1];
            if (suffix[i + 1] < m && word1.charAt(i) == word2.charAt(m - 1 - suffix[i + 1])) {
                suffix[i] = suffix[i + 1] + 1;
            }
        }

        int[] res = new int[m];
        int i = 0;
        boolean changed = false;
        for (int j = 0; j < m; j++) {
            boolean found = false;
            while (i < n) {
                if (word1.charAt(i) == word2.charAt(j)) {
                    boolean canFinish = changed ? (suffix[i + 1] >= m - j - 1) : (suffix[i + 1] >= m - j - 2);
                    if (canFinish) {
                        res[j] = i;
                        i++;
                        found = true;
                        break;
                    }
                } else if (!changed) {
                    if (suffix[i + 1] >= m - j - 1) {
                        res[j] = i;
                        changed = true;
                        i++;
                        found = true;
                        break;
                    }
                }
                i++;
            }
            if (!found) return new int[0];
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
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        n = len(word1)
        m = len(word2)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i+1]
            if suffix[i+1] < m and word1[i] == word2[m - 1 - suffix[i+1]]:
                suffix[i] = suffix[i+1] + 1

        res = []
        i = 0
        changed = False
        for j in range(m):
            found = False
            while i < n:
                if word1[i] == word2[j]:
                    can_finish = (suffix[i+1] >= m - j - 1) if changed else (suffix[i+1] >= m - j - 2)
                    if can_finish:
                        res.append(i)
                        i += 1
                        found = True
                        break
                elif not changed:
                    if suffix[i+1] >= m - j - 1:
                        res.append(i)
                        changed = True
                        i += 1
                        found = True
                        break
                i += 1
            if not found:
                return []
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1]
            if suffix[i + 1] < m and word1[i] == word2[m - 1 - suffix[i + 1]]:
                suffix[i] = suffix[i + 1] + 1

        res = []
        i = 0
        changed = False
        for j in range(m):
            found = False
            while i < n:
                if word1[i] == word2[j]:
                    can_finish = (suffix[i + 1] >= m - j - 1) if changed else (suffix[i + 1] >= m - j - 2)
                    if can_finish:
                        res.append(i)
                        i += 1
                        found = True
                        break
                elif not changed:
                    if suffix[i + 1] >= m - j - 1:
                        res.append(i)
                        changed = True
                        i += 1
                        found = True
                        break
                i += 1
            if not found:
                return []
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* validSequence(char* word1, char* word2, int* returnSize) {
    int n = (int)strlen(word1);
    int m = (int)strlen(word2);
    int* suffix = (int*)calloc(n + 1, sizeof(int));

    for (int i = n - 1; i >= 0; i--) {
        suffix[i] = suffix[i + 1];
        if (suffix[i + 1] < m && word1[i] == word2[m - 1 - suffix[i + 1]]) {
            suffix[i] = suffix[i + 1] + 1;
        }
    }

    int* res = (int*)malloc(m * sizeof(int));
    int i = 0;
    bool changed = false;
    int count = 0;

    for (int j = 0; j < m; j++) {
        bool found = false;
        while (i < n) {
            if (word1[i] == word2[j]) {
                bool can_finish = changed ? (suffix[i + 1] >= m - j - 1) : (suffix[i + 1] >= m - j - 2);
                if (can_finish) {
                    res[count++] = i;
                    i++;
                    found = true;
                    break;
                }
            } else if (!changed) {
                if (suffix[i + 1] >= m - j - 1) {
                    changed = true;
                    res[count++] = i;
                    i++;
                    found = true;
                    break;
                }
            }
            i++;
        }
        if (!found) {
            free(suffix);
            free(res);
            *returnSize = 0;
            return NULL;
        }
    }

    free(suffix);
    *returnSize = m;
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

public class Solution {
    public int[] ValidSequence(string word1, string word2) {
        int n = word1.Length;
        int m = word2.Length;

        int[] suffixMatch = new int[m + 1];
        for (int i = 0; i <= m; i++) suffixMatch[i] = -1;
        suffixMatch[m] = n;

        int curr = n - 1;
        for (int j = m - 1; j >= 0; j--) {
            while (curr >= 0 && word1[curr] != word2[j]) {
                curr--;
            }
            if (curr >= 0) {
                suffixMatch[j] = curr;
                curr--;
            }
        }

        List<int> result = new List<int>();
        bool usedChange = false;
        int w1Idx = 0;

        for (int w2Idx = 0; w2Idx < m; w2Idx++) {
            bool found = false;
            while (w1Idx < n) {
                if (word1[w1Idx] == word2[w2Idx]) {
                    if (!usedChange || suffixMatch[w2Idx + 1] > w1Idx) {
                        result.Add(w1Idx);
                        w1Idx++;
                        found = true;
                        break;
                    }
                } else if (!usedChange && suffixMatch[w2Idx + 1] > w1Idx) {
                    result.Add(w1Idx);
                    usedChange = true;
                    w1Idx++;
                    found = true;
                    break;
                }
                w1Idx++;
            }

            if (!found) return new int[0];
        }

        return result.ToArray();
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} word1
 * @param {string} word2
 * @return {number[]}
 */
var validSequence = function(word1, word2) {
    const n = word1.length;
    const m = word2.length;

    const suffixMatch = new Int32Array(m + 1).fill(-1);
    suffixMatch[m] = n;

    let curr = n - 1;
    for (let j = m - 1; j >= 0; j--) {
        while (curr >= 0 && word1[curr] !== word2[j]) {
            curr--;
        }
        if (curr >= 0) {
            suffixMatch[j] = curr;
            curr--;
        }
    }

    const seq = [];
    let usedChange = false;
    let w1Idx = 0;

    for (let w2Idx = 0; w2Idx < m; w2Idx++) {
        let found = false;
        while (w1Idx < n) {
            if (word1[w1Idx] === word2[w2Idx]) {
                if (!usedChange || suffixMatch[w2Idx + 1] > w1Idx) {
                    seq.push(w1Idx);
                    w1Idx++;
                    found = true;
                    break;
                }
            } else if (!usedChange && suffixMatch[w2Idx + 1] > w1Idx) {
                seq.push(w1Idx);
                usedChange = true;
                w1Idx++;
                found = true;
                break;
            }
            w1Idx++;
        }

        if (!found) return [];
    }

    return seq;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function validSequence(word1: string, word2: string): number[] {
    const n = word1.length;
    const m = word2.length;

    const suffixMatch = new Int32Array(m + 1).fill(-1);
    suffixMatch[m] = n;

    let curr = n - 1;
    for (let j = m - 1; j >= 0; j--) {
        while (curr >= 0 && word1[curr] !== word2[j]) {
            curr--;
        }
        if (curr >= 0) {
            suffixMatch[j] = curr;
            curr--;
        }
    }

    const seq: number[] = [];
    let usedChange = false;
    let w1Idx = 0;

    for (let w2Idx = 0; w2Idx < m; w2Idx++) {
        let found = false;
        while (w1Idx < n) {
            if (word1[w1Idx] === word2[w2Idx]) {
                if (!usedChange || suffixMatch[w2Idx + 1] > w1Idx) {
                    seq.push(w1Idx);
                    w1Idx++;
                    found = true;
                    break;
                }
            } else if (!usedChange && suffixMatch[w2Idx + 1] > w1Idx) {
                seq.push(w1Idx);
                usedChange = true;
                w1Idx++;
                found = true;
                break;
            }
            w1Idx++;
        }

        if (!found) return [];
    }

    return seq;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String $word1
     * @param String $word2
     * @return Integer[]
     */
    function validSequence($word1, $word2) {
        $n = strlen($word1);
        $m = strlen($word2);

        $suffixMatch = array_fill(0, $m + 1, -1);
        $suffixMatch[$m] = $n;

        $curr = $n - 1;
        for ($j = $m - 1; $j >= 0; $j--) {
            while ($curr >= 0 && $word1[$curr] !== $word2[$j]) {
                $curr--;
            }
            if ($curr >= 0) {
                $suffixMatch[$j] = $curr;
                $curr--;
            }
        }

        $seq = [];
        $usedChange = false;
        $w1Idx = 0;

        for ($w2Idx = 0; $w2Idx < $m; $w2Idx++) {
            $found = false;
            while ($w1Idx < $n) {
                if ($word1[$w1Idx] === $word2[$w2Idx]) {
                    if (!$usedChange || $suffixMatch[$w2Idx + 1] > $w1Idx) {
                        $seq[] = $w1Idx;
                        $w1Idx++;
                        $found = true;
                        break;
                    }
                } else if (!$usedChange && $suffixMatch[$w2Idx + 1] > $w1Idx) {
                    $seq[] = $w1Idx;
                    $usedChange = true;
                    $w1Idx++;
                    $found = true;
                    break;
                }
                $w1Idx++;
            }

            if (!$found) return [];
        }

        return $seq;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func validSequence(_ word1: String, _ word2: String) -> [Int] {
        let s1 = Array(word1)
        let s2 = Array(word2)
        let n = s1.count
        let m = s2.count

        var suffixMatch = Array(repeating: -1, count: m + 1)
        suffixMatch[m] = n

        var curr = n - 1
        for j in stride(from: m - 1, through: 0, by: -1) {
            while curr >= 0 && s1[curr] != s2[j] {
                curr -= 1
            }
            if curr >= 0 {
                suffixMatch[j] = curr
                curr -= 1
            }
        }

        var seq = [Int]()
        var usedChange = false
        var w1Idx = 0

        for w2Idx in 0..<m {
            var found = false
            while w1Idx < n {
                if s1[w1Idx] == s2[w2Idx] {
                    if !usedChange || suffixMatch[w2Idx + 1] > w1Idx {
                        seq.append(w1Idx)
                        w1Idx += 1
                        found = true
                        break
                    }
                } else if !usedChange && suffixMatch[w2Idx + 1] > w1Idx {
                    seq.append(w1Idx)
                    usedChange = true
                    w1Idx += 1
                    found = true
                    break
                }
                w1Idx += 1
            }

            if !found {
                return []
            }
        }

        return seq
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun validSequence(word1: String, word2: String): IntArray {
        val n = word1.length
        val m = word2.length
        val suffixMatch = IntArray(n + 1)
        var p2 = m - 1
        for (i in n - 1 downTo 0) {
            suffixMatch[i] = suffixMatch[i + 1]
            if (p2 >= 0 && word1[i] == word2[p2]) {
                suffixMatch[i]++
                p2--
            }
        }

        val res = IntArray(m)
        var usedChange = false
        var p1 = 0
        for (p2Idx in 0 until m) {
            var found = false
            while (p1 < n) {
                if (word1[p1] == word2[p2Idx]) {
                    res[p2Idx] = p1
                    p1++
                    found = true
                    break
                } else if (!usedChange && suffixMatch[p1 + 1] >= m - 1 - p2Idx) {
                    res[p2Idx] = p1
                    p1++
                    usedChange = true
                    found = true
                    break
                } else {
                    p1++
                }
            }
            if (!found) return intArrayOf()
        }
        return res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<int> validSequence(String word1, String word2) {
    int n = word1.length;
    int m = word2.length;
    List<int> suffixMatch = List.filled(n + 1, 0);
    int p2 = m - 1;
    for (int i = n - 1; i >= 0; i--) {
      suffixMatch[i] = suffixMatch[i + 1];
      if (p2 >= 0 && word1[i] == word2[p2]) {
        suffixMatch[i] += 1;
        p2 -= 1;
      }
    }

    List<int> res = [];
    bool usedChange = false;
    int p1 = 0;
    for (int p2Idx = 0; p2Idx < m; p2Idx++) {
      bool found = false;
      while (p1 < n) {
        if (word1[p1] == word2[p2Idx]) {
          res.add(p1);
          p1++;
          found = true;
          break;
        } else if (!usedChange && suffixMatch[p1 + 1] >= m - 1 - p2Idx) {
          res.add(p1);
          p1++;
          usedChange = true;
          found = true;
          break;
        } else {
          p1++;
        }
      }
      if (!found) return [];
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
func validSequence(word1 string, word2 string) []int {
    n := len(word1)
    m := len(word2)
    suffixMatch := make([]int, n+1)
    p2 := m - 1
    for i := n - 1; i >= 0; i-- {
        suffixMatch[i] = suffixMatch[i+1]
        if p2 >= 0 && word1[i] == word2[p2] {
            suffixMatch[i]++
            p2--
        }
    }

    res := make([]int, 0, m)
    usedChange := false
    p1 := 0
    for p2Idx := 0; p2Idx < m; p2Idx++ {
        found := false
        for p1 < n {
            if word1[p1] == word2[p2Idx] {
                res = append(res, p1)
                p1++
                found = true
                break
            } else if !usedChange && suffixMatch[p1+1] >= m-1-p2Idx {
                res = append(res, p1)
                p1++
                usedChange = true
                found = true
                break
            } else {
                p1++
            }
        }
        if !found {
            return []int{}
        }
    }
    return res
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} word1
# @param {String} word2
# @return {Integer[]}
def valid_sequence(word1, word2)
  n = word1.length
  m = word2.length
  suffix_match = Array.new(n + 1, 0)
  p2 = m - 1
  (n - 1).downto(0) do |i|
    suffix_match[i] = suffix_match[i + 1]
    if p2 >= 0 && word1[i] == word2[p2]
      suffix_match[i] += 1
      p2 -= 1
    end
  end

  res = []
  used_change = false
  p1 = 0
  (0...m).each do |p2_idx|
    found = false
    while p1 < n
      if word1[p1] == word2[p2_idx]
        res << p1
        p1 += 1
        found = true
        break
      elsif !used_change && suffix_match[p1 + 1] >= m - 1 - p2_idx
        res << p1
        p1 += 1
        used_change = true
        found = true
        break
      else
        p1 += 1
      end
    end
    return [] unless found
  end
  res
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def validSequence(word1: String, word2: String): Array[Int] = {
    val n = word1.length
    val m = word2.length
    val suffixMatch = new Array[Int](n + 1)
    var p2 = m - 1
    for (i <- n - 1 to 0 by -1) {
      suffixMatch(i) = suffixMatch(i + 1)
      if (p2 >= 0 && word1(i) == word2(p2)) {
        suffixMatch(i) += 1
        p2 -= 1
      }
    }

    val res = new scala.collection.mutable.ArrayBuffer[Int]()
    var usedChange = false
    var p1 = 0
    for (p2Idx <- 0 until m) {
      var found = false
      while (p1 < n && !found) {
        if (word1(p1) == word2(p2Idx)) {
          res += p1
          p1 += 1
          found = true
        } else if (!usedChange && suffixMatch(p1 + 1) >= m - 1 - p2Idx) {
          res += p1
          p1 += 1
          usedChange = true
          found = true
        } else {
          p1 += 1
        }
      }
      if (!found) return Array[Int]()
    }
    res.toArray
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn valid_sequence(word1: String, word2: String) -> Vec<i32> {
        let n = word1.len();
        let m = word2.len();
        let w1 = word1.as_bytes();
        let w2 = word2.as_bytes();
        let mut dp = vec![0; n + 1];

        for i in (0..n).rev() {
            dp[i] = dp[i + 1];
            if dp[i] < m && w1[i] == w2[m - 1 - dp[i]] {
                dp[i] += 1;
            }
        }

        let mut ans = Vec::with_capacity(m);
        let mut p1 = 0;
        let mut changed = false;

        for p2 in 0..m {
            let mut found = false;
            while p1 < n {
                let match_char = w1[p1] == w2[p2];
                let can_skip = !changed && dp[p1 + 1] >= (m - 1 - p2);
                if match_char || can_skip {
                    if !match_char {
                        changed = true;
                    }
                    ans.push(p1 as i32);
                    p1 += 1;
                    found = true;
                    break;
                }
                p1 += 1;
            }
            if !found {
                return vec![];
            }
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
(define/contract (valid-sequence word1 word2)
  (-> string? string? (listof exact-integer?))
  (let* ([n (string-length word1)]
         [m (string-length word2)]
         [dp (make-vector (+ n 1) 0)])
    (for ([i (in-range (- n 1) -1 -1)])
      (let ([char1 (string-ref word1 i)]
            [next-dp (vector-ref dp (+ i 1))])
        (if (and (< next-dp m)
                 (char=? char1 (string-ref word2 (- m 1 next-dp))))
            (vector-set! dp i (+ next-dp 1))
            (vector-set! dp i next-dp))))
    (let loop ([p1 0] [p2 0] [changed #f] [ans '()])
      (cond
        [(= p2 m) (reverse ans)]
        [(= p1 n) '()]
        [else
         (let* ([char1 (string-ref word1 p1)]
                [char2 (string-ref word2 p2)]
                [match? (char=? char1 char2)]
                [can-skip? (and (not changed)
                                (>= (vector-ref dp (+ p1 1)) (- m 1 p2)))])
           (if (or match? can-skip?)
               (loop (+ p1 1) (+ p2 1) (if match? changed #t) (cons p1 ans))
               (loop (+ p1 1) p2 changed ans)))]))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec valid_sequence(Word1 :: unicode:unicode_binary(), Word2 :: unicode:unicode_binary()) -> [integer()].
valid_sequence(Word1, Word2) ->
    N = byte_size(Word1),
    M = byte_size(Word2),
    DPList = build_dp(N - 1, 0, Word1, Word2, M, [0]),
    solve(0, 0, false, Word1, Word2, N, M, DPList, []).

build_dp(I, PrevDP, W1, W2, M, Acc) when I >= 0 ->
    Char1 = binary:at(W1, I),
    NextDP = if (PrevDP < M) andalso (Char1 =:= binary:at(W2, M - 1 - PrevDP)) ->
                  PrevDP + 1;
              true ->
                  PrevDP
             end,
    build_dp(I - 1, NextDP, W1, W2, M, [NextDP | Acc]);
build_dp(-1, _, _, _, _, Acc) ->
    Acc.

solve(P2, _P1, _Changed, _W1, _W2, _N, M, _DPList, Ans) when P2 =:= M ->
    lists:reverse(Ans);
solve(_P2, P1, _Changed, _W1, _W2, N, _M, _DPList, _Ans) when P1 =:= N ->
    [];
solve(P2, P1, Changed, W1, W2, N, M, [_DP_P1 | [DP_P1plus1 | _] = RestDP], Ans) ->
    Match = binary:at(W1, P1) =:= binary:at(W2, P2),
    CanSkip = (not Changed) andalso (DP_P1plus1 >= (M - 1 - P2)),
    if
        Match -> solve(P2 + 1, P1 + 1, Changed, W1, W2, N, M, RestDP, [P1 | Ans]);
        CanSkip -> solve(P2 + 1, P1 + 1, true, W1, W2, N, M, RestDP, [P1 | Ans]);
        true -> solve(P2, P1 + 1, Changed, W1, W2, N, M, RestDP, Ans)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec valid_sequence(word1 :: String.t, word2 :: String.t) :: [integer]
  def valid_sequence(word1, word2) do
    n = byte_size(word1)
    m = byte_size(word2)
    dp_list = build_dp(n - 1, 0, word1, word2, m, [0])
    solve(0, 0, false, word1, word2, n, m, dp_list, [])
  end

  defp build_dp(i, prev_dp, w1, w2, m, acc) when i >= 0 do
    char1 = :binary.at(w1, i)
    next_dp = if prev_dp < m and char1 == :binary.at(w2, m - 1 - prev_dp) do
      prev_dp + 1
    else
      prev_dp
    end
    build_dp(i - 1, next_dp, w1, w2, m, [next_dp | acc])
  end
  defp build_dp(-1, _prev_dp, _w1, _w2, _m, acc), do: acc

  defp solve(p2, _p1, _changed, _w1, _w2, _n, m, _dp_list, ans) when p2 == m do
    Enum.reverse(ans)
  end
  defp solve(_p2, p1, _changed, _w1, _w2, n, _m, _dp_list, _ans) when p1 == n do
    []
  end
  defp solve(p2, p1, changed, w1, w2, n, m, [_dp_p1 | [dp_p1plus1 | _] = rest_dp], ans) do
    char1 = :binary.at(w1, p1)
    char2 = :binary.at(w2, p2)
    match = char1 == char2
    can_skip = (not changed) and (dp_p1plus1 >= m - 1 - p2)
    if match or can_skip do
      solve(p2 + 1, p1 + 1, (if match, do: changed, else: true), w1, w2, n, m, rest_dp, [p1 | ans])
    else
      solve(p2, p1 + 1, changed, w1, w2, n, m, rest_dp, ans)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N + M) where N is the length of `word1` and M is the length of `word2`. The precomputation of the `suffix` array takes O(N) time, and the greedy construction of the index sequence takes O(N + M) time because we iterate through `word1` and `word2` at most once.
- **Space Complexity:** O(N) to store the `suffix` array, which holds values for each index in `word1`. The resulting index sequence also takes O(M) space.
