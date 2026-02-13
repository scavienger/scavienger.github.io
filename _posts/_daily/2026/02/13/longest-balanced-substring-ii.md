---
layout: post
title: "Longest Balanced Substring II"
date: 2026-02-13 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Hash Table", "String", "Prefix Sum"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/longest-balanced-substring-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int longestBalanced(string s) {\n       \
        \ int n = s.length();\n        int res = 0;\n        for (char c : {'a', 'b',\
        \ 'c'}) {\n            int cur = 0;\n            for (char x : s) {\n      \
        \          if (x == c) res = max(res, ++cur);\n                else cur = 0;\n\
        \            }\n        }\n        char chars[3] = {'a', 'b', 'c'};\n      \
        \  for (int i = 0; i < 3; ++i) {\n            char x = chars[i], y = chars[(i\
        \ + 1) % 3], other = chars[(i + 2) % 3];\n            unordered_map<int, int>\
        \ d;\n            d[0] = -1;\n            int cur = 0, start = -1;\n       \
        \     for (int j = 0; j < n; ++j) {\n                if (s[j] == other) {\n\
        \                    d.clear();\n                    cur = 0;\n            \
        \        start = j;\n                    d[0] = j;\n                } else {\n\
        \                    cur += (s[j] == x ? 1 : -1);\n                    if (d.count(cur))\
        \ res = max(res, j - d[cur]);\n                    else d[cur] = j;\n      \
        \          }\n            }\n        }\n        unordered_map<long long, int>\
        \ d3;\n        d3[0] = -1;\n        int na = 0, nb = 0, nc = 0;\n        for\
        \ (int i = 0; i < n; ++i) {\n            if (s[i] == 'a') na++;\n          \
        \  else if (s[i] == 'b') nb++;\n            else nc++;\n            long long\
        \ key = ((long long)(nb - na + 100000) << 32) | (nc - na + 100000);\n      \
        \      if (d3.count(key)) res = max(res, i - d3[key]);\n            else d3[key]\
        \ = i;\n        }\n        return res;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public int longestBalanced(String\
        \ s) {\n        int n = s.length();\n        int res = 0;\n        char[] chars\
        \ = {'a', 'b', 'c'};\n        for (char c : chars) {\n            int cur =\
        \ 0;\n            for (int i = 0; i < n; i++) {\n                if (s.charAt(i)\
        \ == c) res = Math.max(res, ++cur);\n                else cur = 0;\n       \
        \     }\n        }\n        for (int p = 0; p < 3; p++) {\n            char\
        \ x = chars[p], y = chars[(p + 1) % 3], other = chars[(p + 2) % 3];\n      \
        \      Map<Integer, Integer> d = new HashMap<>();\n            d.put(0, -1);\n\
        \            int cur = 0;\n            for (int i = 0; i < n; i++) {\n     \
        \           if (s.charAt(i) == other) {\n                    d.clear();\n  \
        \                  cur = 0;\n                    d.put(0, i);\n            \
        \    } else {\n                    cur += (s.charAt(i) == x ? 1 : -1);\n   \
        \                 if (d.containsKey(cur)) res = Math.max(res, i - d.get(cur));\n\
        \                    else d.put(cur, i);\n                }\n            }\n\
        \        }\n        Map<Long, Integer> d3 = new HashMap<>();\n        d3.put(0L,\
        \ -1);\n        int na = 0, nb = 0, nc = 0;\n        for (int i = 0; i < n;\
        \ i++) {\n            char c = s.charAt(i);\n            if (c == 'a') na++;\
        \ else if (c == 'b') nb++; else nc++;\n            long key = ((long)(nb - na\
        \ + 100000) << 32) | (nc - na + 100000);\n            if (d3.containsKey(key))\
        \ res = Math.max(res, i - d3.get(key));\n            else d3.put(key, i);\n\
        \        }\n        return res;\n    }\n}"
      python: "class Solution(object):\n    def longestBalanced(self, s):\n        res\
        \ = 0\n        for char in 'abc':\n            l = 0\n            for c in s:\n\
        \                if c == char: l += 1; res = max(res, l)\n                else:\
        \ l = 0\n        for x, y, other in [('a', 'b', 'c'), ('a', 'c', 'b'), ('b',\
        \ 'c', 'a')]:\n            for seg in s.split(other):\n                d = {0:\
        \ -1}\n                cur = 0\n                for i, c in enumerate(seg):\n\
        \                    cur += (1 if c == x else -1)\n                    if cur\
        \ in d: res = max(res, i - d[cur])\n                    else: d[cur] = i\n \
        \       d3 = {(0, 0): -1}\n        na = nb = nc = 0\n        for i, c in enumerate(s):\n\
        \            if c == 'a': na += 1\n            elif c == 'b': nb += 1\n    \
        \        else: nc += 1\n            key = (nb - na, nc - na)\n            if\
        \ key in d3: res = max(res, i - d3[key])\n            else: d3[key] = i\n  \
        \      return res"
      python3: "class Solution:\n    def longestBalanced(self, s: str) -> int:\n   \
        \     res = 0\n        for char in 'abc':\n            l = 0\n            for\
        \ c in s:\n                if c == char: l += 1; res = max(res, l)\n       \
        \         else: l = 0\n        for x, y, other in [('a', 'b', 'c'), ('a', 'c',\
        \ 'b'), ('b', 'c', 'a')]:\n            for seg in s.split(other):\n        \
        \        d = {0: -1}\n                cur = 0\n                for i, c in enumerate(seg):\n\
        \                    cur += (1 if c == x else -1)\n                    if cur\
        \ in d: res = max(res, i - d[cur])\n                    else: d[cur] = i\n \
        \       d3 = {(0, 0): -1}\n        na = nb = nc = 0\n        for i, c in enumerate(s):\n\
        \            if c == 'a': na += 1\n            elif c == 'b': nb += 1\n    \
        \        else: nc += 1\n            key = (nb - na, nc - na)\n            if\
        \ key in d3: res = max(res, i - d3[key])\n            else: d3[key] = i\n  \
        \      return res"
      c: "#include <string.h>\n#include <stdlib.h>\n#define MAXN 100005\n\ntypedef struct\
        \ { long long key; int val; } Entry;\nEntry table[300007];\n\nvoid insert(long\
        \ long key, int val, int* res, int i) {\n    int h = (unsigned long long)key\
        \ % 300007;\n    while (table[h].val != -2) {\n        if (table[h].key == key)\
        \ {\n            if (i - table[h].val > *res) *res = i - table[h].val;\n   \
        \         return;\n        }\n        h = (h + 1) % 300007;\n    }\n    table[h].key\
        \ = key; table[h].val = val;\n}\n\nint longestBalanced(char* s) {\n    int n\
        \ = strlen(s), res = 0, first[200005], used[200005];\n    for (char c = 'a';\
        \ c <= 'c'; c++) {\n        int l = 0;\n        for (int i = 0; i < n; i++)\
        \ {\n            if (s[i] == c) { l++; if (l > res) res = l; } else l = 0;\n\
        \        }\n    }\n    char pairs[3][3] = {{'a','b','c'}, {'a','c','b'}, {'b','c','a'}};\n\
        \    for (int p = 0; p < 200005; p++) first[p] = -2;\n    for (int p = 0; p\
        \ < 3; p++) {\n        char x = pairs[p][0], y = pairs[p][1], other = pairs[p][2];\n\
        \        int cur = 0, used_ptr = 0;\n        first[MAXN] = -1; used[used_ptr++]\
        \ = MAXN;\n        for (int i = 0; i < n; i++) {\n            if (s[i] == other)\
        \ {\n                while (used_ptr > 0) first[used[--used_ptr]] = -2;\n  \
        \              cur = 0; first[MAXN] = i; used[used_ptr++] = MAXN;\n        \
        \    } else {\n                cur += (s[i] == x ? 1 : -1);\n              \
        \  if (first[cur + MAXN] != -2) { if (i - first[cur + MAXN] > res) res = i -\
        \ first[cur + MAXN]; }\n                else { first[cur + MAXN] = i; used[used_ptr++]\
        \ = cur + MAXN; }\n            }\n        }\n        while (used_ptr > 0) first[used[--used_ptr]]\
        \ = -2;\n    }\n    for (int i = 0; i < 300007; i++) table[i].val = -2;\n  \
        \  int na = 0, nb = 0, nc = 0;\n    insert(0, -1, &res, -1);\n    for (int i\
        \ = 0; i < n; i++) {\n        if (s[i] == 'a') na++; else if (s[i] == 'b') nb++;\
        \ else nc++;\n        long long key = (long long)(nb - na + MAXN) << 32 | (nc\
        \ - na + MAXN);\n        insert(key, i, &res, i);\n    }\n    return res;\n}"
      csharp: "public class Solution {\n    public int LongestBalanced(string s) {\n\
        \        int n = s.Length, res = 0;\n        char[] chars = {'a', 'b', 'c'};\n\
        \        foreach (char c in chars) {\n            int l = 0;\n            for\
        \ (int i = 0; i < n; i++) {\n                if (s[i] == c) res = Math.Max(res,\
        \ ++l);\n                else l = 0;\n            }\n        }\n        for\
        \ (int p = 0; p < 3; p++) {\n            char x = chars[p], y = chars[(p + 1)\
        \ % 3], other = chars[(p + 2) % 3];\n            var d = new Dictionary<int,\
        \ int>();\n            d[0] = -1; int cur = 0;\n            for (int i = 0;\
        \ i < n; i++) {\n                if (s[i] == other) {\n                    d.Clear();\
        \ cur = 0; d[0] = i;\n                } else {\n                    cur += (s[i]\
        \ == x ? 1 : -1);\n                    if (d.ContainsKey(cur)) res = Math.Max(res,\
        \ i - d[cur]);\n                    else d[cur] = i;\n                }\n  \
        \          }\n        }\n        var d3 = new Dictionary<long, int>();\n   \
        \     d3[0L] = -1; int na = 0, nb = 0, nc = 0;\n        for (int i = 0; i <\
        \ n; i++) {\n            if (s[i] == 'a') na++; else if (s[i] == 'b') nb++;\
        \ else nc++;\n            long key = ((long)(nb - na + 100000) << 32) | (long)(nc\
        \ - na + 100000);\n            if (d3.ContainsKey(key)) res = Math.Max(res,\
        \ i - d3[key]);\n            else d3[key] = i;\n        }\n        return res;\n\
        \    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {number}\n */\nvar longestBalanced\
        \ = function(s) {\n    let n = s.length, res = 0;\n    ['a', 'b', 'c'].forEach(char\
        \ => {\n        let l = 0;\n        for (let i = 0; i < n; i++) {\n        \
        \    if (s[i] === char) res = Math.max(res, ++l);\n            else l = 0;\n\
        \        }\n    });\n    const pairs = [['a', 'b', 'c'], ['a', 'c', 'b'], ['b',\
        \ 'c', 'a']];\n    pairs.forEach(([x, y, other]) => {\n        s.split(other).forEach(seg\
        \ => {\n            let d = new Map([[0, -1]]), cur = 0;\n            for (let\
        \ i = 0; i < seg.length; i++) {\n                cur += (seg[i] === x ? 1 :\
        \ -1);\n                if (d.has(cur)) res = Math.max(res, i - d.get(cur));\n\
        \                else d.set(cur, i);\n            }\n        });\n    });\n\
        \    let d3 = new Map([[\"0,0\", -1]]), na = 0, nb = 0, nc = 0;\n    for (let\
        \ i = 0; i < n; i++) {\n        if (s[i] === 'a') na++; else if (s[i] === 'b')\
        \ nb++; else nc++;\n        let key = (nb - na) + \",\" + (nc - na);\n     \
        \   if (d3.has(key)) res = Math.max(res, i - d3.get(key));\n        else d3.set(key,\
        \ i);\n    }\n    return res;\n};"
      typescript: "function longestBalanced(s: string): number {\n    const n = s.length;\n\
        \    let ans = 0;\n\n    if (n > 0) {\n        ans = 1;\n        let count =\
        \ 1;\n        for (let i = 1; i < n; i++) {\n            if (s[i] === s[i -\
        \ 1]) count++;\n            else count = 1;\n            ans = Math.max(ans,\
        \ count);\n        }\n    }\n\n    function solve2(c1: string, c2: string, other:\
        \ string): void {\n        const parts = s.split(other);\n        for (const\
        \ part of parts) {\n            let diff = 0;\n            const first = new\
        \ Map<number, number>();\n            first.set(0, -1);\n            for (let\
        \ i = 0; i < part.length; i++) {\n                if (part[i] === c1) diff++;\n\
        \                else if (part[i] === c2) diff--;\n                if (first.has(diff))\
        \ {\n                    ans = Math.max(ans, i - first.get(diff)!);\n      \
        \          } else {\n                    first.set(diff, i);\n             \
        \   }\n            }\n        }\n    }\n\n    solve2('a', 'b', 'c');\n    solve2('a',\
        \ 'c', 'b');\n    solve2('b', 'c', 'a');\n\n    let d1 = 0, d2 = 0;\n    const\
        \ first3 = new Map<string, number>();\n    first3.set(\"0,0\", -1);\n    for\
        \ (let i = 0; i < n; i++) {\n        if (s[i] === 'a') {\n            d1++;\n\
        \            d2++;\n        } else if (s[i] === 'b') {\n            d1--;\n\
        \        } else if (s[i] === 'c') {\n            d2--;\n        }\n        const\
        \ key = `${d1},${d2}`;\n        if (first3.has(key)) {\n            ans = Math.max(ans,\
        \ i - first3.get(key)!);\n        } else {\n            first3.set(key, i);\n\
        \        }\n    }\n\n    return ans;\n}"
      php: "class Solution {\n    /**\n     * @param String $s\n     * @return Integer\n\
        \     */\n    function longestBalanced($s) {\n        $n = strlen($s);\n   \
        \     $ans = 0;\n        if ($n > 0) {\n            $ans = 1;\n            $count\
        \ = 1;\n            for ($i = 1; $i < $n; $i++) {\n                if ($s[$i]\
        \ == $s[$i - 1]) $count++;\n                else $count = 1;\n             \
        \   if ($count > $ans) $ans = $count;\n            }\n        }\n        $this->solve2($s,\
        \ 'a', 'b', 'c', $ans);\n        $this->solve2($s, 'a', 'c', 'b', $ans);\n \
        \       $this->solve2($s, 'b', 'c', 'a', $ans);\n        $d1 = 0; $d2 = 0;\n\
        \        $first3 = array(\"0,0\" => -1);\n        for ($i = 0; $i < $n; $i++)\
        \ {\n            if ($s[$i] == 'a') { $d1++; $d2++; }\n            else if ($s[$i]\
        \ == 'b') { $d1--; }\n            else if ($s[$i] == 'c') { $d2--; }\n     \
        \       $key = \"$d1,$d2\";\n            if (isset($first3[$key])) {\n     \
        \           $len = $i - $first3[$key];\n                if ($len > $ans) $ans\
        \ = $len;\n            } else {\n                $first3[$key] = $i;\n     \
        \       }\n        }\n        return $ans;\n    }\n    private function solve2($s,\
        \ $c1, $c2, $other, &$ans) {\n        $parts = explode($other, $s);\n      \
        \  foreach ($parts as $part) {\n            $diff = 0;\n            $first =\
        \ array(0 => -1);\n            $lp = strlen($part);\n            for ($i = 0;\
        \ $i < $lp; $i++) {\n                if ($part[$i] == $c1) $diff++;\n      \
        \          else if ($part[$i] == $c2) $diff--;\n                if (isset($first[$diff]))\
        \ {\n                    $len = $i - $first[$diff];\n                    if\
        \ ($len > $ans) $ans = $len;\n                } else {\n                   \
        \ $first[$diff] = $i;\n                }\n            }\n        }\n    }\n}"
      swift: "class Solution {\n    func longestBalanced(_ s: String) -> Int {\n   \
        \     let n = s.count\n        if n == 0 { return 0 }\n        var ans = 1\n\
        \        let chars = Array(s)\n        var count = 1\n        for i in 1..<n\
        \ {\n            if chars[i] == chars[i-1] { count += 1 }\n            else\
        \ { count = 1 }\n            ans = max(ans, count)\n        }\n        func\
        \ solve2(_ c1: Character, _ c2: Character, _ other: Character) {\n         \
        \   let parts = s.split(separator: other, omittingEmptySubsequences: false)\n\
        \            for part in parts {\n                var diff = 0\n           \
        \     var first = [0: -1]\n                for (i, char) in part.enumerated()\
        \ {\n                    if char == c1 { diff += 1 }\n                    else\
        \ if char == c2 { diff -= 1 }\n                    if let val = first[diff]\
        \ {\n                        ans = max(ans, i - val)\n                    }\
        \ else {\n                        first[diff] = i\n                    }\n \
        \               }\n            }\n        }\n        solve2(\"a\", \"b\", \"\
        c\")\n        solve2(\"a\", \"c\", \"b\")\n        solve2(\"b\", \"c\", \"a\"\
        )\n        var d1 = 0, d2 = 0\n        var first3 = [\"0,0\": -1]\n        for\
        \ (i, char) in chars.enumerated() {\n            if char == \"a\" { d1 += 1;\
        \ d2 += 1 }\n            else if char == \"b\" { d1 -= 1 }\n            else\
        \ if char == \"c\" { d2 -= 1 }\n            let key = \"\\(d1),\\(d2)\"\n  \
        \          if let val = first3[key] {\n                ans = max(ans, i - val)\n\
        \            } else {\n                first3[key] = i\n            }\n    \
        \    }\n        return ans\n    }\n}"
      kotlin: "import kotlin.math.max\n\nclass Solution {\n    fun longestBalanced(s:\
        \ String): Int {\n        val n = s.length\n        var ans = if (n > 0) 1 else\
        \ 0\n        var curCount = 1\n        for (i in 1 until n) {\n            if\
        \ (s[i] == s[i - 1]) curCount++\n            else curCount = 1\n           \
        \ ans = max(ans, curCount)\n        }\n\n        fun solve2(c1: Char, c2: Char,\
        \ other: Char) {\n            val parts = s.split(other)\n            for (part\
        \ in parts) {\n                var diff = 0\n                val first = mutableMapOf(0\
        \ to -1)\n                for (i in part.indices) {\n                    if\
        \ (part[i] == c1) diff++\n                    else if (part[i] == c2) diff--\n\
        \                    if (first.containsKey(diff)) {\n                      \
        \  ans = max(ans, i - first[diff]!!)\n                    } else {\n       \
        \                 first[diff] = i\n                    }\n                }\n\
        \            }\n        }\n\n        solve2('a', 'b', 'c')\n        solve2('a',\
        \ 'c', 'b')\n        solve2('b', 'c', 'a')\n\n        var d1 = 0\n        var\
        \ d2 = 0\n        val first3 = mutableMapOf(Pair(0, 0) to -1)\n        for (i\
        \ in s.indices) {\n            when (s[i]) {\n                'a' -> { d1++;\
        \ d2++ }\n                'b' -> d1--\n                'c' -> d2--\n       \
        \     }\n            val key = Pair(d1, d2)\n            if (first3.containsKey(key))\
        \ {\n                ans = max(ans, i - first3[key]!!)\n            } else {\n\
        \                first3[key] = i\n            }\n        }\n        return ans\n\
        \    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int longestBalanced(String s)\
        \ {\n    int n = s.length;\n    int ans = n > 0 ? 1 : 0;\n    int count = 1;\n\
        \    for (int i = 1; i < n; i++) {\n      if (s[i] == s[i - 1]) count++;\n \
        \     else count = 1;\n      ans = max(ans, count);\n    }\n\n    void solve2(String\
        \ c1, String c2, String other) {\n      List<String> parts = s.split(other);\n\
        \      for (var part in parts) {\n        int diff = 0;\n        Map<int, int>\
        \ first = {0: -1};\n        for (int i = 0; i < part.length; i++) {\n      \
        \    if (part[i] == c1) diff++;\n          else if (part[i] == c2) diff--;\n\
        \          if (first.containsKey(diff)) {\n            ans = max(ans, i - first[diff]!);\n\
        \          } else {\n            first[diff] = i;\n          }\n        }\n\
        \      }\n    }\n\n    solve2('a', 'b', 'c');\n    solve2('a', 'c', 'b');\n\
        \    solve2('b', 'c', 'a');\n\n    int d1 = 0, d2 = 0;\n    Map<String, int>\
        \ first3 = {\"0,0\": -1};\n    for (int i = 0; i < n; i++) {\n      if (s[i]\
        \ == 'a') { d1++; d2++; }\n      else if (s[i] == 'b') { d1--; }\n      else\
        \ if (s[i] == 'c') { d2--; }\n      String key = \"$d1,$d2\";\n      if (first3.containsKey(key))\
        \ {\n        ans = max(ans, i - first3[key]!);\n      } else {\n        first3[key]\
        \ = i;\n      }\n    }\n    return ans;\n  }\n}"
      go: "import \"strings\"\n\nfunc longestBalanced(s string) int {\n    n := len(s)\n\
        \    ans := 0\n    if n > 0 {\n        ans = 1\n        count := 1\n       \
        \ for i := 1; i < n; i++ {\n            if s[i] == s[i-1] {\n              \
        \  count++\n            } else {\n                count = 1\n            }\n\
        \            if count > ans { ans = count }\n        }\n    }\n\n    solve2\
        \ := func(c1, c2 byte, other string) {\n        parts := strings.Split(s, other)\n\
        \        for _, part := range parts {\n            diff := 0\n            first\
        \ := make(map[int]int)\n            first[0] = -1\n            for i := 0; i\
        \ < len(part); i++ {\n                if part[i] == c1 { diff++ }\n        \
        \        else if part[i] == c2 { diff-- }\n                if val, ok := first[diff];\
        \ ok {\n                    l := i - val\n                    if l > ans { ans\
        \ = l }\n                } else {\n                    first[diff] = i\n   \
        \             }\n            }\n        }\n    }\n\n    solve2('a', 'b', \"\
        c\")\n    solve2('a', 'c', \"b\")\n    solve2('b', 'c', \"a\")\n\n    d1, d2\
        \ := 0, 0\n    type pair struct { d1, d2 int }\n    first3 := make(map[pair]int)\n\
        \    first3[pair{0, 0}] = -1\n    for i := 0; i < n; i++ {\n        if s[i]\
        \ == 'a' { d1++; d2++ }\n        else if s[i] == 'b' { d1-- }\n        else\
        \ if s[i] == 'c' { d2-- }\n        key := pair{d1, d2}\n        if val, ok :=\
        \ first3[key]; ok {\n            l := i - val\n            if l > ans { ans\
        \ = l }\n        } else {\n            first3[key] = i\n        }\n    }\n \
        \   return ans\n}"
      ruby: "def longest_balanced(s)\n  n = s.length\n  ans = 1\n  curr_run = 1\n  (1...n).each\
        \ do |i|\n    if s[i] == s[i - 1]\n      curr_run += 1\n    else\n      ans\
        \ = [ans, curr_run].max\n      curr_run = 1\n    end\n  end\n  ans = [ans, curr_run].max\n\
        \n  [['a', 'b', 'c'], ['b', 'c', 'a'], ['a', 'c', 'b']].each do |c1, c2, other|\n\
        \    s.split(other).each do |block|\n      map = { 0 => -1 }\n      diff = 0\n\
        \      block.each_char.with_index do |ch, i|\n        diff -= 1 if ch == c1\n\
        \        diff += 1 if ch == c2\n        if map.key?(diff)\n          ans = [ans,\
        \ i - map[diff]].max\n        else\n          map[diff] = i\n        end\n \
        \     end\n    end\n  end\n\n  map3 = { [0, 0] => -1 }\n  ca = cb = cc = 0\n\
        \  s.each_char.with_index do |ch, i|\n    ca += 1 if ch == 'a'\n    cb += 1\
        \ if ch == 'b'\n    cc += 1 if ch == 'c'\n    key = [cb - ca, cc - ca]\n   \
        \ if map3.key?(key)\n      ans = [ans, i - map3[key]].max\n    else\n      map3[key]\
        \ = i\n    end\n  end\n  ans\nend"
      scala: "object Solution {\n    def longestBalanced(s: String): Int = {\n     \
        \   var ans = 1\n        val n = s.length\n        var currRun = 1\n       \
        \ for (i <- 1 until n) {\n            if (s(i) == s(i - 1)) currRun += 1\n \
        \           else {\n                ans = Math.max(ans, currRun)\n         \
        \       currRun = 1\n            }\n        }\n        ans = Math.max(ans, currRun)\n\
        \n        val pairs = Array(('a', 'b', \"c\"), ('b', 'c', \"a\"), ('a', 'c',\
        \ \"b\"))\n        for ((c1, c2, other) <- pairs) {\n            for (block\
        \ <- s.split(other)) {\n                val map = scala.collection.mutable.HashMap[Int,\
        \ Int](0 -> -1)\n                var diff = 0\n                for (i <- 0 until\
        \ block.length) {\n                    if (block(i) == c1) diff -= 1\n     \
        \               else if (block(i) == c2) diff += 1\n                    if (map.contains(diff))\
        \ ans = Math.max(ans, i - map(diff))\n                    else map(diff) = i\n\
        \                }\n            }\n        }\n\n        val map3 = scala.collection.mutable.HashMap[(Int,\
        \ Int), Int]((0, 0) -> -1)\n        var (ca, cb, cc) = (0, 0, 0)\n        for\
        \ (i <- 0 until n) {\n            if (s(i) == 'a') ca += 1\n            else\
        \ if (s(i) == 'b') cb += 1\n            else if (s(i) == 'c') cc += 1\n    \
        \        val key = (cb - ca, cc - ca)\n            if (map3.contains(key)) ans\
        \ = Math.max(ans, i - map3(key))\n            else map3(key) = i\n        }\n\
        \        ans\n    }\n}"
      rust: "impl Solution {\n    pub fn longest_balanced(s: String) -> i32 {\n    \
        \    let s_bytes = s.as_bytes();\n        let n = s_bytes.len();\n        let\
        \ mut ans = 1;\n        let mut curr_run = 1;\n        for i in 1..n {\n   \
        \         if s_bytes[i] == s_bytes[i - 1] {\n                curr_run += 1;\n\
        \            } else {\n                ans = ans.max(curr_run);\n          \
        \      curr_run = 1;\n            }\n        }\n        ans = ans.max(curr_run);\n\
        \n        let pairs = [('a', 'b', \"c\"), ('b', 'c', \"a\"), ('a', 'c', \"b\"\
        )];\n        for &(c1, c2, other) in &pairs {\n            for block in s.split(other)\
        \ {\n                let mut map = std::collections::HashMap::new();\n     \
        \           map.insert(0, -1);\n                let mut diff = 0;\n        \
        \        for (i, ch) in block.chars().enumerate() {\n                    if\
        \ ch == c1 { diff -= 1; }\n                    else if ch == c2 { diff += 1;\
        \ }\n                    if let Some(&prev) = map.get(&diff) {\n           \
        \             ans = ans.max((i as i32) - prev);\n                    } else\
        \ {\n                        map.insert(diff, i as i32);\n                 \
        \   }\n                }\n            }\n        }\n\n        let mut map3 =\
        \ std::collections::HashMap::new();\n        map3.insert((0, 0), -1);\n    \
        \    let (mut ca, mut cb, mut cc) = (0, 0, 0);\n        for (i, ch) in s.chars().enumerate()\
        \ {\n            match ch {\n                'a' => ca += 1,\n             \
        \   'b' => cb += 1,\n                'c' => cc += 1,\n                _ => ()\n\
        \            }\n            let key = (cb - ca, cc - ca);\n            if let\
        \ Some(&prev) = map3.get(&key) {\n                ans = ans.max((i as i32) -\
        \ prev);\n            } else {\n                map3.insert(key, i as i32);\n\
        \            }\n        }\n        ans\n    }\n}"
      racket: "(define/contract (longest-balanced s)\n  (-> string? exact-integer?)\n\
        \  (let* ([n (string-length s)]\n         [ans (if (> n 0)\n               \
        \   (for/fold ([max-r 1] [curr 1]) ([i (in-range 1 n)])\n                  \
        \  (if (char=? (string-ref s i) (string-ref s (- i 1)))\n                  \
        \      (values (max max-r (+ curr 1)) (+ curr 1))\n                        (values\
        \ max-r 1)))\n                  0)]\n         [ans1 (if (pair? ans) (car ans)\
        \ ans)])\n    (let* ([ans2 (for/fold ([max-l ans1])\n                      \
        \     ([pair '((#\\a #\\b \"c\") (#\\b #\\c \"a\") (#\\a #\\c \"b\"))])\n  \
        \                 (let* ([c1 (first pair)] [c2 (second pair)] [other (third\
        \ pair)]\n                          [blocks (string-split s other #:trim? #f)])\n\
        \                     (for/fold ([max-l2 max-l]) ([block blocks])\n        \
        \               (let-values ([(ml d f) (for/fold ([ml3 max-l2] [diff 0] [f-occ\
        \ (hash 0 -1)])\n                                                        ([ch\
        \ (in-string block)] [i (in-naturals)])\n                                  \
        \              (let ([nd (cond [(char=? ch c1) (- diff 1)]\n               \
        \                                                 [(char=? ch c2) (+ diff 1)]\n\
        \                                                                [else diff])])\n\
        \                                                  (if (hash-has-key? f-occ\
        \ nd)\n                                                      (values (max ml3\
        \ (- i (hash-ref f-occ nd))) nd f-occ)\n                                   \
        \                   (values ml3 nd (hash-set f-occ nd i)))))])\n           \
        \              ml))))]\n           [ans3 (for/fold ([max-l ans2] [ca 0] [cb\
        \ 0] [cc 0] [f-occ (hash (cons 0 0) -1)])\n                           ([ch (in-string\
        \ s)] [i (in-naturals)])\n                   (let* ([na (if (char=? ch #\\a)\
        \ (+ ca 1) ca)]\n                          [nb (if (char=? ch #\\b) (+ cb 1)\
        \ cb)]\n                          [nc (if (char=? ch #\\c) (+ cc 1) cc)]\n \
        \                         [key (cons (- nb na) (- nc na))])\n              \
        \       (if (hash-has-key? f-occ key)\n                         (values (max\
        \ max-l (- i (hash-ref f-occ key))) na nb nc f-occ)\n                      \
        \   (values max-l na nb nc (hash-set f-occ key i)))))])\n      (if (pair? ans3)\
        \ (car ans3) ans3))))"
      erlang: "-spec longest_balanced(S :: unicode:unicode_binary()) -> integer().\n\
        longest_balanced(S) ->\n  Chars = binary_to_list(S),\n  Ans1 = solve_case1(Chars),\n\
        \  Ans2 = solve_case2(S, Ans1),\n  solve_case3(Chars, Ans2).\n\nsolve_case1([])\
        \ -> 0;\nsolve_case1([H|T]) -> solve_case1(T, H, 1, 1).\nsolve_case1([], _,\
        \ _, Max) -> Max;\nsolve_case1([H|T], H, Curr, Max) -> solve_case1(T, H, Curr\
        \ + 1, lists:max([Max, Curr + 1]));\nsolve_case1([H|T], _, _, Max) -> solve_case1(T,\
        \ H, 1, Max).\n\nsolve_case2(S, Ans) ->\n  Pairs = [{$a, $b, <<\"c\">>}, {$b,\
        \ $c, <<\"a\">>}, {$a, $c, <<\"b\">>}],\n  lists:foldl(fun({C1, C2, Other},\
        \ Acc) ->\n    Blocks = binary:split(S, Other, [global]),\n    lists:foldl(fun(Block,\
        \ Acc2) -> solve_block(Block, C1, C2, Acc2) end, Acc, Blocks)\n  end, Ans, Pairs).\n\
        \nsolve_block(Block, C1, C2, MaxL) ->\n  solve_block(Block, 0, 0, #{0 => -1},\
        \ MaxL).\nsolve_block(Block, I, Diff, Map, MaxL) when I < byte_size(Block) ->\n\
        \  Ch = binary:at(Block, I),\n  ND = if Ch =:= C1 -> Diff - 1; Ch =:= C2 ->\
        \ Diff + 1; true -> Diff end,\n  case maps:find(ND, Map) of\n    {ok, Prev}\
        \ -> solve_block(Block, I + 1, ND, Map, lists:max([MaxL, I - Prev]));\n    error\
        \ -> solve_block(Block, I + 1, ND, maps:put(ND, I, Map), MaxL)\n  end;\nsolve_block(_,\
        \ _, _, _, MaxL) -> MaxL.\n\nsolve_case3(Chars, Ans) ->\n  {FinalAns, _, _,\
        \ _} = lists:foldl(fun(Ch, {MaxL, Ca, Cb, Cc, Map}) ->\n    {Na, Nb, Nc} = if\
        \ Ch =:= $a -> {Ca + 1, Cb, Cc}; Ch =:= $b -> {Ca, Cb + 1, Cc}; true -> {Ca,\
        \ Cb, Cc + 1} end,\n    Key = {Nb - Na, Nc - Na},\n    case maps:find(Key, Map)\
        \ of\n      {ok, Prev} -> {lists:max([MaxL, maps:get(I, #{I => length(Chars)\
        \ - length(Chars)} ) + 1 + length(Chars) - length(Chars), maps:get(I, #{I =>\
        \ 0}) + (length(Chars) - length(tl(Chars))) - 1 - Prev]), Na, Nb, Nc, Map};\n\
        \      error -> {MaxL, Na, Nb, Nc, maps:put(Key, (length(Chars) - length(tl(Chars)))\
        \ - 1, Map)}\n    end\n  end, {Ans, 0, 0, 0, #{{0, 0} => -1}}, Chars, 0).\n\n\
        solve_case3(Chars, Ans, _) ->\n  {FA, _, _, _, _} = lists:foldl(fun(Ch, {ML,\
        \ Ca, Cb, Cc, M, I}) ->\n    {Na, Nb, Nc} = if Ch =:= $a -> {Ca+1, Cb, Cc};\
        \ Ch =:= $b -> {Ca, Cb+1, Cc}; Ch =:= $c -> {Ca, Cb, Cc+1}; true -> {Ca, Cb,\
        \ Cc} end,\n    K = {Nb-Na, Nc-Na},\n    case maps:find(K, M) of {ok, P} ->\
        \ {lists:max([ML, I - P]), Na, Nb, Nc, M, I+1}; error -> {ML, Na, Nb, Nc, maps:put(K,\
        \ I, M), I+1} end\n  end, {Ans, 0, 0, 0, #{{0,0} => -1}, 0}, Chars),\n  FA."
      elixir: "defmodule Solution do\n  @spec longest_balanced(s :: String.t) :: integer\n\
        \  def longest_balanced(s) do\n    chars = String.to_charlist(s)\n    n = length(chars)\n\
        \    ans = if n > 0 do\n      {max_r, _} = Enum.reduce(tl(chars), {1, {1, hd(chars)}},\
        \ fn ch, {max_r, {curr, prev}} ->\n        if ch == prev, do: {max(max_r, curr\
        \ + 1), {curr + 1, ch}}, else: {max_r, {1, ch}}\n      end)\n      max_r\n \
        \   else 0 end\n\n    ans = Enum.reduce([{\"a\",\"b\",\"c\"},{\"b\",\"c\",\"\
        a\"},{\"a\",\"c\",\"b\"}], ans, fn {c1, c2, other}, acc ->\n      blocks = String.split(s,\
        \ other)\n      Enum.reduce(blocks, acc, fn block, acc2 ->\n        {res, _}\
        \ = Enum.reduce(String.to_charlist(block) |> Enum.with_index(), {acc2, %{0 =>\
        \ -1}, 0}, fn {ch, i}, {ml, map, diff} ->\n          nd = cond do ch == hd(String.to_charlist(c1))\
        \ -> diff - 1; ch == hd(String.to_charlist(c2)) -> diff + 1; true -> diff end\n\
        \          if Map.has_key?(map, nd), do: {max(ml, i - Map.get(map, nd)), map,\
        \ nd}, else: {ml, Map.put(map, nd, i), nd}\n        end)\n        res\n    \
        \  end)\n    end)\n\n    {ans, _, _, _, _} = Enum.reduce(chars |> Enum.with_index(),\
        \ {ans, 0, 0, 0, %{{0,0} => -1}}, fn {ch, i}, {ml, ca, cb, cc, map} ->\n   \
        \   {na, nb, nc} = cond do ch == ?a -> {ca+1, cb, cc}; ch == ?b -> {ca, cb+1,\
        \ cc}; ch == ?c -> {ca, cb, cc+1}; true -> {ca, cb, cc} end\n      key = {nb-na,\
        \ nc-na}\n      if Map.has_key?(map, key), do: {max(ml, i - Map.get(map, key)),\
        \ na, nb, nc, map}, else: {ml, na, nb, nc, Map.put(map, key, i)}\n    end)\n\
        \    ans\n  end\nend"
    approach: 'A substring is balanced if all its distinct characters appear with the
      same frequency. We can divide this into three exhaustive cases based on the number
      of distinct characters present: one, two, or three. For Case 1 (one distinct character),
      any contiguous run of the same character is balanced; the longest such run across
      all characters gives the maximal length. For Case 2 (exactly two distinct characters),
      we iterate through all three pairs of characters (a-b, b-c, a-c). For each pair,
      we identify segments that do not contain the third character and find the longest
      substring within these segments where the frequencies of the two chosen characters
      are equal using a prefix difference and a hash map (or array) to store the earliest
      occurrence of each difference.'
    time_complexity: O(n) where n is the length of the string. We process the string
      a constant number of times (once for single character runs, three times for pairs,
      and once for triples). Each pass uses either simple iteration or hash map operations
      that average O(1).
    space_complexity: O(n) to store the first occurrences of prefix sums or difference
      pairs in hash maps or arrays. The size of these structures scales linearly with
      the length of the string.
    elapsed_time: 418.00668811798096
    model: gemini-3-flash-preview
    generated_at: '2026-02-13 01:36:05 '
---

## Problem #3714: Longest Balanced Substring II

**Difficulty:** Medium

**Topics:** Hash Table, String, Prefix Sum

## Problem Description

<p>You are given a string <code>s</code> consisting only of the characters <code>&#39;a&#39;</code>, <code>&#39;b&#39;</code>, and <code>&#39;c&#39;</code>.</p>

<p>A <strong><span data-keyword="substring-nonempty">substring</span></strong> of <code>s</code> is called <strong>balanced</strong> if all <strong>distinct</strong> characters in the <strong>substring</strong> appear the <strong>same</strong> number of times.</p>

<p>Return the <strong>length of the longest balanced substring</strong> of <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abbac&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The longest balanced substring is <code>&quot;abba&quot;</code> because both distinct characters <code>&#39;a&#39;</code> and <code>&#39;b&#39;</code> each appear exactly 2 times.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;aabcc&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>The longest balanced substring is <code>&quot;abc&quot;</code> because all distinct characters <code>&#39;a&#39;</code>, <code>&#39;b&#39;</code> and <code>&#39;c&#39;</code> each appear exactly 1 time.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;aba&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>One of the longest balanced substrings is <code>&quot;ab&quot;</code> because both distinct characters <code>&#39;a&#39;</code> and <code>&#39;b&#39;</code> each appear exactly 1 time. Another longest balanced substring is <code>&quot;ba&quot;</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> contains only the characters <code>&#39;a&#39;</code>, <code>&#39;b&#39;</code>, and <code>&#39;c&#39;</code>.</li>
</ul>


## Hints

1. Solve for three cases: all-equal characters, exactly two distinct characters, and all three characters present. Treat each case separately and take the maximum length.

2. Case 1: single character: the longest balanced substring is the longest run of the same character; report its length.

3. Case 2: two distinct characters: reduce to that pair (ignore the third character) and use prefix differences of their counts; equal counts between two indices mean the substring between them is balanced for those two chars.

4. Case 3: all three characters: use prefix counts and hash the pair `(count_b - count_a, count_c - count_a)` for each prefix; if the same pair appears at two indices the substring between them has equal counts for a, b, and c. Store earliest index per pair to get maximal length.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

A substring is balanced if all its distinct characters appear with the same frequency. We can divide this into three exhaustive cases based on the number of distinct characters present: one, two, or three. For Case 1 (one distinct character), any contiguous run of the same character is balanced; the longest such run across all characters gives the maximal length. For Case 2 (exactly two distinct characters), we iterate through all three pairs of characters (a-b, b-c, a-c). For each pair, we identify segments that do not contain the third character and find the longest substring within these segments where the frequencies of the two chosen characters are equal using a prefix difference and a hash map (or array) to store the earliest occurrence of each difference.

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
    int longestBalanced(string s) {
        int n = s.length();
        int res = 0;
        for (char c : {'a', 'b', 'c'}) {
            int cur = 0;
            for (char x : s) {
                if (x == c) res = max(res, ++cur);
                else cur = 0;
            }
        }
        char chars[3] = {'a', 'b', 'c'};
        for (int i = 0; i < 3; ++i) {
            char x = chars[i], y = chars[(i + 1) % 3], other = chars[(i + 2) % 3];
            unordered_map<int, int> d;
            d[0] = -1;
            int cur = 0, start = -1;
            for (int j = 0; j < n; ++j) {
                if (s[j] == other) {
                    d.clear();
                    cur = 0;
                    start = j;
                    d[0] = j;
                } else {
                    cur += (s[j] == x ? 1 : -1);
                    if (d.count(cur)) res = max(res, j - d[cur]);
                    else d[cur] = j;
                }
            }
        }
        unordered_map<long long, int> d3;
        d3[0] = -1;
        int na = 0, nb = 0, nc = 0;
        for (int i = 0; i < n; ++i) {
            if (s[i] == 'a') na++;
            else if (s[i] == 'b') nb++;
            else nc++;
            long long key = ((long long)(nb - na + 100000) << 32) | (nc - na + 100000);
            if (d3.count(key)) res = max(res, i - d3[key]);
            else d3[key] = i;
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
import java.util.*;

class Solution {
    public int longestBalanced(String s) {
        int n = s.length();
        int res = 0;
        char[] chars = {'a', 'b', 'c'};
        for (char c : chars) {
            int cur = 0;
            for (int i = 0; i < n; i++) {
                if (s.charAt(i) == c) res = Math.max(res, ++cur);
                else cur = 0;
            }
        }
        for (int p = 0; p < 3; p++) {
            char x = chars[p], y = chars[(p + 1) % 3], other = chars[(p + 2) % 3];
            Map<Integer, Integer> d = new HashMap<>();
            d.put(0, -1);
            int cur = 0;
            for (int i = 0; i < n; i++) {
                if (s.charAt(i) == other) {
                    d.clear();
                    cur = 0;
                    d.put(0, i);
                } else {
                    cur += (s.charAt(i) == x ? 1 : -1);
                    if (d.containsKey(cur)) res = Math.max(res, i - d.get(cur));
                    else d.put(cur, i);
                }
            }
        }
        Map<Long, Integer> d3 = new HashMap<>();
        d3.put(0L, -1);
        int na = 0, nb = 0, nc = 0;
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c == 'a') na++; else if (c == 'b') nb++; else nc++;
            long key = ((long)(nb - na + 100000) << 32) | (nc - na + 100000);
            if (d3.containsKey(key)) res = Math.max(res, i - d3.get(key));
            else d3.put(key, i);
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
    def longestBalanced(self, s):
        res = 0
        for char in 'abc':
            l = 0
            for c in s:
                if c == char: l += 1; res = max(res, l)
                else: l = 0
        for x, y, other in [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'c', 'a')]:
            for seg in s.split(other):
                d = {0: -1}
                cur = 0
                for i, c in enumerate(seg):
                    cur += (1 if c == x else -1)
                    if cur in d: res = max(res, i - d[cur])
                    else: d[cur] = i
        d3 = {(0, 0): -1}
        na = nb = nc = 0
        for i, c in enumerate(s):
            if c == 'a': na += 1
            elif c == 'b': nb += 1
            else: nc += 1
            key = (nb - na, nc - na)
            if key in d3: res = max(res, i - d3[key])
            else: d3[key] = i
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def longestBalanced(self, s: str) -> int:
        res = 0
        for char in 'abc':
            l = 0
            for c in s:
                if c == char: l += 1; res = max(res, l)
                else: l = 0
        for x, y, other in [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'c', 'a')]:
            for seg in s.split(other):
                d = {0: -1}
                cur = 0
                for i, c in enumerate(seg):
                    cur += (1 if c == x else -1)
                    if cur in d: res = max(res, i - d[cur])
                    else: d[cur] = i
        d3 = {(0, 0): -1}
        na = nb = nc = 0
        for i, c in enumerate(s):
            if c == 'a': na += 1
            elif c == 'b': nb += 1
            else: nc += 1
            key = (nb - na, nc - na)
            if key in d3: res = max(res, i - d3[key])
            else: d3[key] = i
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <string.h>
#include <stdlib.h>
#define MAXN 100005

typedef struct { long long key; int val; } Entry;
Entry table[300007];

void insert(long long key, int val, int* res, int i) {
    int h = (unsigned long long)key % 300007;
    while (table[h].val != -2) {
        if (table[h].key == key) {
            if (i - table[h].val > *res) *res = i - table[h].val;
            return;
        }
        h = (h + 1) % 300007;
    }
    table[h].key = key; table[h].val = val;
}

int longestBalanced(char* s) {
    int n = strlen(s), res = 0, first[200005], used[200005];
    for (char c = 'a'; c <= 'c'; c++) {
        int l = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] == c) { l++; if (l > res) res = l; } else l = 0;
        }
    }
    char pairs[3][3] = {{'a','b','c'}, {'a','c','b'}, {'b','c','a'}};
    for (int p = 0; p < 200005; p++) first[p] = -2;
    for (int p = 0; p < 3; p++) {
        char x = pairs[p][0], y = pairs[p][1], other = pairs[p][2];
        int cur = 0, used_ptr = 0;
        first[MAXN] = -1; used[used_ptr++] = MAXN;
        for (int i = 0; i < n; i++) {
            if (s[i] == other) {
                while (used_ptr > 0) first[used[--used_ptr]] = -2;
                cur = 0; first[MAXN] = i; used[used_ptr++] = MAXN;
            } else {
                cur += (s[i] == x ? 1 : -1);
                if (first[cur + MAXN] != -2) { if (i - first[cur + MAXN] > res) res = i - first[cur + MAXN]; }
                else { first[cur + MAXN] = i; used[used_ptr++] = cur + MAXN; }
            }
        }
        while (used_ptr > 0) first[used[--used_ptr]] = -2;
    }
    for (int i = 0; i < 300007; i++) table[i].val = -2;
    int na = 0, nb = 0, nc = 0;
    insert(0, -1, &res, -1);
    for (int i = 0; i < n; i++) {
        if (s[i] == 'a') na++; else if (s[i] == 'b') nb++; else nc++;
        long long key = (long long)(nb - na + MAXN) << 32 | (nc - na + MAXN);
        insert(key, i, &res, i);
    }
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int LongestBalanced(string s) {
        int n = s.Length, res = 0;
        char[] chars = {'a', 'b', 'c'};
        foreach (char c in chars) {
            int l = 0;
            for (int i = 0; i < n; i++) {
                if (s[i] == c) res = Math.Max(res, ++l);
                else l = 0;
            }
        }
        for (int p = 0; p < 3; p++) {
            char x = chars[p], y = chars[(p + 1) % 3], other = chars[(p + 2) % 3];
            var d = new Dictionary<int, int>();
            d[0] = -1; int cur = 0;
            for (int i = 0; i < n; i++) {
                if (s[i] == other) {
                    d.Clear(); cur = 0; d[0] = i;
                } else {
                    cur += (s[i] == x ? 1 : -1);
                    if (d.ContainsKey(cur)) res = Math.Max(res, i - d[cur]);
                    else d[cur] = i;
                }
            }
        }
        var d3 = new Dictionary<long, int>();
        d3[0L] = -1; int na = 0, nb = 0, nc = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] == 'a') na++; else if (s[i] == 'b') nb++; else nc++;
            long key = ((long)(nb - na + 100000) << 32) | (long)(nc - na + 100000);
            if (d3.ContainsKey(key)) res = Math.Max(res, i - d3[key]);
            else d3[key] = i;
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
 * @return {number}
 */
var longestBalanced = function(s) {
    let n = s.length, res = 0;
    ['a', 'b', 'c'].forEach(char => {
        let l = 0;
        for (let i = 0; i < n; i++) {
            if (s[i] === char) res = Math.max(res, ++l);
            else l = 0;
        }
    });
    const pairs = [['a', 'b', 'c'], ['a', 'c', 'b'], ['b', 'c', 'a']];
    pairs.forEach(([x, y, other]) => {
        s.split(other).forEach(seg => {
            let d = new Map([[0, -1]]), cur = 0;
            for (let i = 0; i < seg.length; i++) {
                cur += (seg[i] === x ? 1 : -1);
                if (d.has(cur)) res = Math.max(res, i - d.get(cur));
                else d.set(cur, i);
            }
        });
    });
    let d3 = new Map([["0,0", -1]]), na = 0, nb = 0, nc = 0;
    for (let i = 0; i < n; i++) {
        if (s[i] === 'a') na++; else if (s[i] === 'b') nb++; else nc++;
        let key = (nb - na) + "," + (nc - na);
        if (d3.has(key)) res = Math.max(res, i - d3.get(key));
        else d3.set(key, i);
    }
    return res;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function longestBalanced(s: string): number {
    const n = s.length;
    let ans = 0;

    if (n > 0) {
        ans = 1;
        let count = 1;
        for (let i = 1; i < n; i++) {
            if (s[i] === s[i - 1]) count++;
            else count = 1;
            ans = Math.max(ans, count);
        }
    }

    function solve2(c1: string, c2: string, other: string): void {
        const parts = s.split(other);
        for (const part of parts) {
            let diff = 0;
            const first = new Map<number, number>();
            first.set(0, -1);
            for (let i = 0; i < part.length; i++) {
                if (part[i] === c1) diff++;
                else if (part[i] === c2) diff--;
                if (first.has(diff)) {
                    ans = Math.max(ans, i - first.get(diff)!);
                } else {
                    first.set(diff, i);
                }
            }
        }
    }

    solve2('a', 'b', 'c');
    solve2('a', 'c', 'b');
    solve2('b', 'c', 'a');

    let d1 = 0, d2 = 0;
    const first3 = new Map<string, number>();
    first3.set("0,0", -1);
    for (let i = 0; i < n; i++) {
        if (s[i] === 'a') {
            d1++;
            d2++;
        } else if (s[i] === 'b') {
            d1--;
        } else if (s[i] === 'c') {
            d2--;
        }
        const key = `${d1},${d2}`;
        if (first3.has(key)) {
            ans = Math.max(ans, i - first3.get(key)!);
        } else {
            first3.set(key, i);
        }
    }

    return ans;
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
     * @return Integer
     */
    function longestBalanced($s) {
        $n = strlen($s);
        $ans = 0;
        if ($n > 0) {
            $ans = 1;
            $count = 1;
            for ($i = 1; $i < $n; $i++) {
                if ($s[$i] == $s[$i - 1]) $count++;
                else $count = 1;
                if ($count > $ans) $ans = $count;
            }
        }
        $this->solve2($s, 'a', 'b', 'c', $ans);
        $this->solve2($s, 'a', 'c', 'b', $ans);
        $this->solve2($s, 'b', 'c', 'a', $ans);
        $d1 = 0; $d2 = 0;
        $first3 = array("0,0" => -1);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] == 'a') { $d1++; $d2++; }
            else if ($s[$i] == 'b') { $d1--; }
            else if ($s[$i] == 'c') { $d2--; }
            $key = "$d1,$d2";
            if (isset($first3[$key])) {
                $len = $i - $first3[$key];
                if ($len > $ans) $ans = $len;
            } else {
                $first3[$key] = $i;
            }
        }
        return $ans;
    }
    private function solve2($s, $c1, $c2, $other, &$ans) {
        $parts = explode($other, $s);
        foreach ($parts as $part) {
            $diff = 0;
            $first = array(0 => -1);
            $lp = strlen($part);
            for ($i = 0; $i < $lp; $i++) {
                if ($part[$i] == $c1) $diff++;
                else if ($part[$i] == $c2) $diff--;
                if (isset($first[$diff])) {
                    $len = $i - $first[$diff];
                    if ($len > $ans) $ans = $len;
                } else {
                    $first[$diff] = $i;
                }
            }
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func longestBalanced(_ s: String) -> Int {
        let n = s.count
        if n == 0 { return 0 }
        var ans = 1
        let chars = Array(s)
        var count = 1
        for i in 1..<n {
            if chars[i] == chars[i-1] { count += 1 }
            else { count = 1 }
            ans = max(ans, count)
        }
        func solve2(_ c1: Character, _ c2: Character, _ other: Character) {
            let parts = s.split(separator: other, omittingEmptySubsequences: false)
            for part in parts {
                var diff = 0
                var first = [0: -1]
                for (i, char) in part.enumerated() {
                    if char == c1 { diff += 1 }
                    else if char == c2 { diff -= 1 }
                    if let val = first[diff] {
                        ans = max(ans, i - val)
                    } else {
                        first[diff] = i
                    }
                }
            }
        }
        solve2("a", "b", "c")
        solve2("a", "c", "b")
        solve2("b", "c", "a")
        var d1 = 0, d2 = 0
        var first3 = ["0,0": -1]
        for (i, char) in chars.enumerated() {
            if char == "a" { d1 += 1; d2 += 1 }
            else if char == "b" { d1 -= 1 }
            else if char == "c" { d2 -= 1 }
            let key = "\(d1),\(d2)"
            if let val = first3[key] {
                ans = max(ans, i - val)
            } else {
                first3[key] = i
            }
        }
        return ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import kotlin.math.max

class Solution {
    fun longestBalanced(s: String): Int {
        val n = s.length
        var ans = if (n > 0) 1 else 0
        var curCount = 1
        for (i in 1 until n) {
            if (s[i] == s[i - 1]) curCount++
            else curCount = 1
            ans = max(ans, curCount)
        }

        fun solve2(c1: Char, c2: Char, other: Char) {
            val parts = s.split(other)
            for (part in parts) {
                var diff = 0
                val first = mutableMapOf(0 to -1)
                for (i in part.indices) {
                    if (part[i] == c1) diff++
                    else if (part[i] == c2) diff--
                    if (first.containsKey(diff)) {
                        ans = max(ans, i - first[diff]!!)
                    } else {
                        first[diff] = i
                    }
                }
            }
        }

        solve2('a', 'b', 'c')
        solve2('a', 'c', 'b')
        solve2('b', 'c', 'a')

        var d1 = 0
        var d2 = 0
        val first3 = mutableMapOf(Pair(0, 0) to -1)
        for (i in s.indices) {
            when (s[i]) {
                'a' -> { d1++; d2++ }
                'b' -> d1--
                'c' -> d2--
            }
            val key = Pair(d1, d2)
            if (first3.containsKey(key)) {
                ans = max(ans, i - first3[key]!!)
            } else {
                first3[key] = i
            }
        }
        return ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:math';

class Solution {
  int longestBalanced(String s) {
    int n = s.length;
    int ans = n > 0 ? 1 : 0;
    int count = 1;
    for (int i = 1; i < n; i++) {
      if (s[i] == s[i - 1]) count++;
      else count = 1;
      ans = max(ans, count);
    }

    void solve2(String c1, String c2, String other) {
      List<String> parts = s.split(other);
      for (var part in parts) {
        int diff = 0;
        Map<int, int> first = {0: -1};
        for (int i = 0; i < part.length; i++) {
          if (part[i] == c1) diff++;
          else if (part[i] == c2) diff--;
          if (first.containsKey(diff)) {
            ans = max(ans, i - first[diff]!);
          } else {
            first[diff] = i;
          }
        }
      }
    }

    solve2('a', 'b', 'c');
    solve2('a', 'c', 'b');
    solve2('b', 'c', 'a');

    int d1 = 0, d2 = 0;
    Map<String, int> first3 = {"0,0": -1};
    for (int i = 0; i < n; i++) {
      if (s[i] == 'a') { d1++; d2++; }
      else if (s[i] == 'b') { d1--; }
      else if (s[i] == 'c') { d2--; }
      String key = "$d1,$d2";
      if (first3.containsKey(key)) {
        ans = max(ans, i - first3[key]!);
      } else {
        first3[key] = i;
      }
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
import "strings"

func longestBalanced(s string) int {
    n := len(s)
    ans := 0
    if n > 0 {
        ans = 1
        count := 1
        for i := 1; i < n; i++ {
            if s[i] == s[i-1] {
                count++
            } else {
                count = 1
            }
            if count > ans { ans = count }
        }
    }

    solve2 := func(c1, c2 byte, other string) {
        parts := strings.Split(s, other)
        for _, part := range parts {
            diff := 0
            first := make(map[int]int)
            first[0] = -1
            for i := 0; i < len(part); i++ {
                if part[i] == c1 { diff++ }
                else if part[i] == c2 { diff-- }
                if val, ok := first[diff]; ok {
                    l := i - val
                    if l > ans { ans = l }
                } else {
                    first[diff] = i
                }
            }
        }
    }

    solve2('a', 'b', "c")
    solve2('a', 'c', "b")
    solve2('b', 'c', "a")

    d1, d2 := 0, 0
    type pair struct { d1, d2 int }
    first3 := make(map[pair]int)
    first3[pair{0, 0}] = -1
    for i := 0; i < n; i++ {
        if s[i] == 'a' { d1++; d2++ }
        else if s[i] == 'b' { d1-- }
        else if s[i] == 'c' { d2-- }
        key := pair{d1, d2}
        if val, ok := first3[key]; ok {
            l := i - val
            if l > ans { ans = l }
        } else {
            first3[key] = i
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
def longest_balanced(s)
  n = s.length
  ans = 1
  curr_run = 1
  (1...n).each do |i|
    if s[i] == s[i - 1]
      curr_run += 1
    else
      ans = [ans, curr_run].max
      curr_run = 1
    end
  end
  ans = [ans, curr_run].max

  [['a', 'b', 'c'], ['b', 'c', 'a'], ['a', 'c', 'b']].each do |c1, c2, other|
    s.split(other).each do |block|
      map = { 0 => -1 }
      diff = 0
      block.each_char.with_index do |ch, i|
        diff -= 1 if ch == c1
        diff += 1 if ch == c2
        if map.key?(diff)
          ans = [ans, i - map[diff]].max
        else
          map[diff] = i
        end
      end
    end
  end

  map3 = { [0, 0] => -1 }
  ca = cb = cc = 0
  s.each_char.with_index do |ch, i|
    ca += 1 if ch == 'a'
    cb += 1 if ch == 'b'
    cc += 1 if ch == 'c'
    key = [cb - ca, cc - ca]
    if map3.key?(key)
      ans = [ans, i - map3[key]].max
    else
      map3[key] = i
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
    def longestBalanced(s: String): Int = {
        var ans = 1
        val n = s.length
        var currRun = 1
        for (i <- 1 until n) {
            if (s(i) == s(i - 1)) currRun += 1
            else {
                ans = Math.max(ans, currRun)
                currRun = 1
            }
        }
        ans = Math.max(ans, currRun)

        val pairs = Array(('a', 'b', "c"), ('b', 'c', "a"), ('a', 'c', "b"))
        for ((c1, c2, other) <- pairs) {
            for (block <- s.split(other)) {
                val map = scala.collection.mutable.HashMap[Int, Int](0 -> -1)
                var diff = 0
                for (i <- 0 until block.length) {
                    if (block(i) == c1) diff -= 1
                    else if (block(i) == c2) diff += 1
                    if (map.contains(diff)) ans = Math.max(ans, i - map(diff))
                    else map(diff) = i
                }
            }
        }

        val map3 = scala.collection.mutable.HashMap[(Int, Int), Int]((0, 0) -> -1)
        var (ca, cb, cc) = (0, 0, 0)
        for (i <- 0 until n) {
            if (s(i) == 'a') ca += 1
            else if (s(i) == 'b') cb += 1
            else if (s(i) == 'c') cc += 1
            val key = (cb - ca, cc - ca)
            if (map3.contains(key)) ans = Math.max(ans, i - map3(key))
            else map3(key) = i
        }
        ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn longest_balanced(s: String) -> i32 {
        let s_bytes = s.as_bytes();
        let n = s_bytes.len();
        let mut ans = 1;
        let mut curr_run = 1;
        for i in 1..n {
            if s_bytes[i] == s_bytes[i - 1] {
                curr_run += 1;
            } else {
                ans = ans.max(curr_run);
                curr_run = 1;
            }
        }
        ans = ans.max(curr_run);

        let pairs = [('a', 'b', "c"), ('b', 'c', "a"), ('a', 'c', "b")];
        for &(c1, c2, other) in &pairs {
            for block in s.split(other) {
                let mut map = std::collections::HashMap::new();
                map.insert(0, -1);
                let mut diff = 0;
                for (i, ch) in block.chars().enumerate() {
                    if ch == c1 { diff -= 1; }
                    else if ch == c2 { diff += 1; }
                    if let Some(&prev) = map.get(&diff) {
                        ans = ans.max((i as i32) - prev);
                    } else {
                        map.insert(diff, i as i32);
                    }
                }
            }
        }

        let mut map3 = std::collections::HashMap::new();
        map3.insert((0, 0), -1);
        let (mut ca, mut cb, mut cc) = (0, 0, 0);
        for (i, ch) in s.chars().enumerate() {
            match ch {
                'a' => ca += 1,
                'b' => cb += 1,
                'c' => cc += 1,
                _ => ()
            }
            let key = (cb - ca, cc - ca);
            if let Some(&prev) = map3.get(&key) {
                ans = ans.max((i as i32) - prev);
            } else {
                map3.insert(key, i as i32);
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
(define/contract (longest-balanced s)
  (-> string? exact-integer?)
  (let* ([n (string-length s)]
         [ans (if (> n 0)
                  (for/fold ([max-r 1] [curr 1]) ([i (in-range 1 n)])
                    (if (char=? (string-ref s i) (string-ref s (- i 1)))
                        (values (max max-r (+ curr 1)) (+ curr 1))
                        (values max-r 1)))
                  0)]
         [ans1 (if (pair? ans) (car ans) ans)])
    (let* ([ans2 (for/fold ([max-l ans1])
                           ([pair '((#\a #\b "c") (#\b #\c "a") (#\a #\c "b"))])
                   (let* ([c1 (first pair)] [c2 (second pair)] [other (third pair)]
                          [blocks (string-split s other #:trim? #f)])
                     (for/fold ([max-l2 max-l]) ([block blocks])
                       (let-values ([(ml d f) (for/fold ([ml3 max-l2] [diff 0] [f-occ (hash 0 -1)])
                                                        ([ch (in-string block)] [i (in-naturals)])
                                                (let ([nd (cond [(char=? ch c1) (- diff 1)]
                                                                [(char=? ch c2) (+ diff 1)]
                                                                [else diff])])
                                                  (if (hash-has-key? f-occ nd)
                                                      (values (max ml3 (- i (hash-ref f-occ nd))) nd f-occ)
                                                      (values ml3 nd (hash-set f-occ nd i)))))])
                         ml))))]
           [ans3 (for/fold ([max-l ans2] [ca 0] [cb 0] [cc 0] [f-occ (hash (cons 0 0) -1)])
                           ([ch (in-string s)] [i (in-naturals)])
                   (let* ([na (if (char=? ch #\a) (+ ca 1) ca)]
                          [nb (if (char=? ch #\b) (+ cb 1) cb)]
                          [nc (if (char=? ch #\c) (+ cc 1) cc)]
                          [key (cons (- nb na) (- nc na))])
                     (if (hash-has-key? f-occ key)
                         (values (max max-l (- i (hash-ref f-occ key))) na nb nc f-occ)
                         (values max-l na nb nc (hash-set f-occ key i)))))])
      (if (pair? ans3) (car ans3) ans3))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec longest_balanced(S :: unicode:unicode_binary()) -> integer().
longest_balanced(S) ->
  Chars = binary_to_list(S),
  Ans1 = solve_case1(Chars),
  Ans2 = solve_case2(S, Ans1),
  solve_case3(Chars, Ans2).

solve_case1([]) -> 0;
solve_case1([H|T]) -> solve_case1(T, H, 1, 1).
solve_case1([], _, _, Max) -> Max;
solve_case1([H|T], H, Curr, Max) -> solve_case1(T, H, Curr + 1, lists:max([Max, Curr + 1]));
solve_case1([H|T], _, _, Max) -> solve_case1(T, H, 1, Max).

solve_case2(S, Ans) ->
  Pairs = [{$a, $b, <<"c">>}, {$b, $c, <<"a">>}, {$a, $c, <<"b">>}],
  lists:foldl(fun({C1, C2, Other}, Acc) ->
    Blocks = binary:split(S, Other, [global]),
    lists:foldl(fun(Block, Acc2) -> solve_block(Block, C1, C2, Acc2) end, Acc, Blocks)
  end, Ans, Pairs).

solve_block(Block, C1, C2, MaxL) ->
  solve_block(Block, 0, 0, #{0 => -1}, MaxL).
solve_block(Block, I, Diff, Map, MaxL) when I < byte_size(Block) ->
  Ch = binary:at(Block, I),
  ND = if Ch =:= C1 -> Diff - 1; Ch =:= C2 -> Diff + 1; true -> Diff end,
  case maps:find(ND, Map) of
    {ok, Prev} -> solve_block(Block, I + 1, ND, Map, lists:max([MaxL, I - Prev]));
    error -> solve_block(Block, I + 1, ND, maps:put(ND, I, Map), MaxL)
  end;
solve_block(_, _, _, _, MaxL) -> MaxL.

solve_case3(Chars, Ans) ->
  {FinalAns, _, _, _} = lists:foldl(fun(Ch, {MaxL, Ca, Cb, Cc, Map}) ->
    {Na, Nb, Nc} = if Ch =:= $a -> {Ca + 1, Cb, Cc}; Ch =:= $b -> {Ca, Cb + 1, Cc}; true -> {Ca, Cb, Cc + 1} end,
    Key = {Nb - Na, Nc - Na},
    case maps:find(Key, Map) of
      {ok, Prev} -> {lists:max([MaxL, maps:get(I, #{I => length(Chars) - length(Chars)} ) + 1 + length(Chars) - length(Chars), maps:get(I, #{I => 0}) + (length(Chars) - length(tl(Chars))) - 1 - Prev]), Na, Nb, Nc, Map};
      error -> {MaxL, Na, Nb, Nc, maps:put(Key, (length(Chars) - length(tl(Chars))) - 1, Map)}
    end
  end, {Ans, 0, 0, 0, #{{0, 0} => -1}}, Chars, 0).

solve_case3(Chars, Ans, _) ->
  {FA, _, _, _, _} = lists:foldl(fun(Ch, {ML, Ca, Cb, Cc, M, I}) ->
    {Na, Nb, Nc} = if Ch =:= $a -> {Ca+1, Cb, Cc}; Ch =:= $b -> {Ca, Cb+1, Cc}; Ch =:= $c -> {Ca, Cb, Cc+1}; true -> {Ca, Cb, Cc} end,
    K = {Nb-Na, Nc-Na},
    case maps:find(K, M) of {ok, P} -> {lists:max([ML, I - P]), Na, Nb, Nc, M, I+1}; error -> {ML, Na, Nb, Nc, maps:put(K, I, M), I+1} end
  end, {Ans, 0, 0, 0, #{{0,0} => -1}, 0}, Chars),
  FA.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec longest_balanced(s :: String.t) :: integer
  def longest_balanced(s) do
    chars = String.to_charlist(s)
    n = length(chars)
    ans = if n > 0 do
      {max_r, _} = Enum.reduce(tl(chars), {1, {1, hd(chars)}}, fn ch, {max_r, {curr, prev}} ->
        if ch == prev, do: {max(max_r, curr + 1), {curr + 1, ch}}, else: {max_r, {1, ch}}
      end)
      max_r
    else 0 end

    ans = Enum.reduce([{"a","b","c"},{"b","c","a"},{"a","c","b"}], ans, fn {c1, c2, other}, acc ->
      blocks = String.split(s, other)
      Enum.reduce(blocks, acc, fn block, acc2 ->
        {res, _} = Enum.reduce(String.to_charlist(block) |> Enum.with_index(), {acc2, %{0 => -1}, 0}, fn {ch, i}, {ml, map, diff} ->
          nd = cond do ch == hd(String.to_charlist(c1)) -> diff - 1; ch == hd(String.to_charlist(c2)) -> diff + 1; true -> diff end
          if Map.has_key?(map, nd), do: {max(ml, i - Map.get(map, nd)), map, nd}, else: {ml, Map.put(map, nd, i), nd}
        end)
        res
      end)
    end)

    {ans, _, _, _, _} = Enum.reduce(chars |> Enum.with_index(), {ans, 0, 0, 0, %{{0,0} => -1}}, fn {ch, i}, {ml, ca, cb, cc, map} ->
      {na, nb, nc} = cond do ch == ?a -> {ca+1, cb, cc}; ch == ?b -> {ca, cb+1, cc}; ch == ?c -> {ca, cb, cc+1}; true -> {ca, cb, cc} end
      key = {nb-na, nc-na}
      if Map.has_key?(map, key), do: {max(ml, i - Map.get(map, key)), na, nb, nc, map}, else: {ml, na, nb, nc, Map.put(map, key, i)}
    end)
    ans
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the string. We process the string a constant number of times (once for single character runs, three times for pairs, and once for triples). Each pass uses either simple iteration or hash map operations that average O(1).
- **Space Complexity:** O(n) to store the first occurrences of prefix sums or difference pairs in hash maps or arrays. The size of these structures scales linearly with the length of the string.
