---
layout: post
title: "Maximum Number of Non-Overlapping Substrings"
date: 2026-09-18 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Hash Table", "String", "Greedy", "Sorting"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<string> maxNumOfSubstrings(string\
        \ s) {\n        int n = s.length();\n        vector<int> first(26, -1);\n  \
        \      vector<int> last(26, -1);\n        for (int i = 0; i < n; ++i) {\n  \
        \          int c = s[i] - 'a';\n            if (first[c] == -1) first[c] = i;\n\
        \            last[c] = i;\n        }\n\n        vector<pair<int, int>> intervals;\n\
        \        for (int i = 0; i < 26; ++i) {\n            if (first[i] == -1) continue;\n\
        \            int l = first[i];\n            int r = last[i];\n            bool\
        \ possible = true;\n            for (int j = l; j <= r; ++j) {\n           \
        \     int c = s[j] - 'a';\n                if (first[c] < l) {\n           \
        \         possible = false;\n                    break;\n                }\n\
        \                r = max(r, last[c]);\n            }\n            if (possible)\
        \ {\n                intervals.push_back({l, r});\n            }\n        }\n\
        \n        sort(intervals.begin(), intervals.end(), [](const pair<int, int>&\
        \ a, const pair<int, int>& b) {\n            return a.second < b.second;\n \
        \       });\n\n        vector<string> result;\n        int last_end = -1;\n\
        \        for (auto& interval : intervals) {\n            if (interval.first\
        \ > last_end) {\n                result.push_back(s.substr(interval.first, interval.second\
        \ - interval.first + 1));\n                last_end = interval.second;\n   \
        \         }\n        }\n        return result;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public List<String> maxNumOfSubstrings(String\
        \ s) {\n        int n = s.length();\n        int[] first = new int[26];\n  \
        \      int[] last = new int[26];\n        Arrays.fill(first, -1);\n        Arrays.fill(last,\
        \ -1);\n        for (int i = 0; i < n; i++) {\n            int c = s.charAt(i)\
        \ - 'a';\n            if (first[c] == -1) first[c] = i;\n            last[c]\
        \ = i;\n        }\n\n        List<int[]> intervals = new ArrayList<>();\n  \
        \      for (int i = 0; i < 26; i++) {\n            if (first[i] == -1) continue;\n\
        \            int l = first[i];\n            int r = last[i];\n            boolean\
        \ possible = true;\n            for (int j = l; j <= r; j++) {\n           \
        \     int c = s.charAt(j) - 'a';\n                if (first[c] < l) {\n    \
        \                possible = false;\n                    break;\n           \
        \     }\n                r = Math.max(r, last[c]);\n            }\n        \
        \    if (possible) {\n                intervals.add(new int[]{l, r});\n    \
        \        }\n        }\n\n        intervals.sort((a, b) -> Integer.compare(a[1],\
        \ b[1]));\n\n        List<String> result = new ArrayList<>();\n        int lastEnd\
        \ = -1;\n        for (int[] interval : intervals) {\n            if (interval[0]\
        \ > lastEnd) {\n                result.add(s.substring(interval[0], interval[1]\
        \ + 1));\n                lastEnd = interval[1];\n            }\n        }\n\
        \        return result;\n    }\n}"
      python: "class Solution(object):\n    def maxNumOfSubstrings(self, s):\n     \
        \   \"\"\"\n        :type s: str\n        :rtype: List[str]\n        \"\"\"\n\
        \        first = [-1] * 26\n        last = [-1] * 26\n        for i, char in\
        \ enumerate(s):\n            idx = ord(char) - ord('a')\n            if first[idx]\
        \ == -1:\n                first[idx] = i\n            last[idx] = i\n\n    \
        \    intervals = []\n        for i in range(26):\n            if first[i] ==\
        \ -1:\n                continue\n            l = first[i]\n            r = last[i]\n\
        \            possible = True\n            j = l\n            while j <= r:\n\
        \                char_idx = ord(s[j]) - ord('a')\n                if first[char_idx]\
        \ < l:\n                    possible = False\n                    break\n  \
        \              r = max(r, last[char_idx])\n                j += 1\n        \
        \    if possible:\n                intervals.append((l, r))\n\n        intervals.sort(key=lambda\
        \ x: x[1])\n\n        res = []\n        last_end = -1\n        for l, r in intervals:\n\
        \            if l > last_end:\n                res.append(s[l:r+1])\n      \
        \          last_end = r\n        return res"
      python3: "class Solution:\n    def maxNumOfSubstrings(self, s: str) -> list[str]:\n\
        \        first = [-1] * 26\n        last = [-1] * 26\n        s_ints = [ord(c)\
        \ - 97 for c in s]\n        for i, c_idx in enumerate(s_ints):\n           \
        \ if first[c_idx] == -1:\n                first[c_idx] = i\n            last[c_idx]\
        \ = i\n\n        intervals = []\n        for i in range(26):\n            if\
        \ first[i] == -1:\n                continue\n            l, r = first[i], last[i]\n\
        \            valid = True\n            j = l\n            while j <= r:\n  \
        \              c_idx = s_ints[j]\n                if first[c_idx] < l:\n   \
        \                 valid = False\n                    break\n               \
        \ r = max(r, last[c_idx])\n                j += 1\n            if valid:\n \
        \               intervals.append((l, r))\n\n        intervals.sort(key=lambda\
        \ x: (x[1], -x[0]))\n        res = []\n        last_end = -1\n        for l,\
        \ r in intervals:\n            if l > last_end:\n                res.append(s[l\
        \ : r + 1])\n                last_end = r\n        return res"
      c: "#include <stdlib.h>\n#include <string.h>\n#include <stdbool.h>\n\ntypedef\
        \ struct {\n    int l, r;\n} Interval;\n\nint compare(const void* a, const void*\
        \ b) {\n    const Interval* i1 = (const Interval*)a;\n    const Interval* i2\
        \ = (const Interval*)b;\n    if (i1->r != i2->r) return i1->r - i2->r;\n   \
        \ return i2->l - i1->l;\n}\n\n/**\n * Note: The returned array must be malloced,\
        \ assume caller calls free().\n */\nchar** maxNumOfSubstrings(char* s, int*\
        \ returnSize) {\n    int n = strlen(s);\n    int first[26], last[26];\n    for\
        \ (int i = 0; i < 26; i++) first[i] = -1;\n    for (int i = 0; i < n; i++) {\n\
        \        int c = s[i] - 'a';\n        if (first[c] == -1) first[c] = i;\n  \
        \      last[c] = i;\n    }\n\n    Interval intervals[26];\n    int intervalCount\
        \ = 0;\n    for (int i = 0; i < 26; i++) {\n        if (first[i] == -1) continue;\n\
        \        int l = first[i], r = last[i];\n        bool valid = true;\n      \
        \  for (int j = l; j <= r; j++) {\n            int c = s[j] - 'a';\n       \
        \     if (first[c] < l) {\n                valid = false;\n                break;\n\
        \            }\n            if (last[c] > r) r = last[c];\n        }\n     \
        \   if (valid) {\n            intervals[intervalCount].l = l;\n            intervals[intervalCount].r\
        \ = r;\n            intervalCount++;\n        }\n    }\n\n    qsort(intervals,\
        \ intervalCount, sizeof(Interval), compare);\n\n    char** res = (char**)malloc(26\
        \ * sizeof(char*));\n    int count = 0;\n    int last_end = -1;\n    for (int\
        \ i = 0; i < intervalCount; i++) {\n        if (intervals[i].l > last_end) {\n\
        \            int l = intervals[i].l;\n            int r = intervals[i].r;\n\
        \            int len = r - l + 1;\n            res[count] = (char*)malloc((len\
        \ + 1) * sizeof(char));\n            memcpy(res[count], s + l, len);\n     \
        \       res[count][len] = '\\0';\n            last_end = r;\n            count++;\n\
        \        }\n    }\n    *returnSize = count;\n    return res;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\nusing System.Linq;\n\
        \npublic class Solution {\n    public IList<string> MaxNumOfSubstrings(string\
        \ s) {\n        int n = s.Length;\n        int[] first = new int[26];\n    \
        \    int[] last = new int[26];\n        for (int i = 0; i < 26; i++) first[i]\
        \ = -1;\n        for (int i = 0; i < n; i++) {\n            int c = s[i] - 'a';\n\
        \            if (first[c] == -1) first[c] = i;\n            last[c] = i;\n \
        \       }\n\n        var intervals = new List<(int l, int r)>();\n        for\
        \ (int i = 0; i < 26; i++) {\n            if (first[i] == -1) continue;\n  \
        \          int l = first[i], r = last[i];\n            bool valid = true;\n\
        \            for (int j = l; j <= r; j++) {\n                int c = s[j] -\
        \ 'a';\n                if (first[c] < l) {\n                    valid = false;\n\
        \                    break;\n                }\n                if (last[c]\
        \ > r) r = last[c];\n            }\n            if (valid) intervals.Add((l,\
        \ r));\n        }\n\n        var sortedIntervals = intervals.OrderBy(x => x.r).ThenByDescending(x\
        \ => x.l);\n        var res = new List<string>();\n        int lastEnd = -1;\n\
        \        foreach (var interval in sortedIntervals) {\n            if (interval.l\
        \ > lastEnd) {\n                res.Add(s.Substring(interval.l, interval.r -\
        \ interval.l + 1));\n                lastEnd = interval.r;\n            }\n\
        \        }\n        return res;\n    }\n}"
      javascript: "/**\n * @param {string} s\n * @return {string[]}\n */\nvar maxNumOfSubstrings\
        \ = function(s) {\n    const n = s.length;\n    const first = new Array(26).fill(-1);\n\
        \    const last = new Array(26).fill(-1);\n    const aCode = 'a'.charCodeAt(0);\n\
        \n    for (let i = 0; i < n; i++) {\n        const c = s.charCodeAt(i) - aCode;\n\
        \        if (first[c] === -1) first[c] = i;\n        last[c] = i;\n    }\n\n\
        \    const intervals = [];\n    for (let i = 0; i < 26; i++) {\n        if (first[i]\
        \ === -1) continue;\n        let l = first[i], r = last[i];\n        let valid\
        \ = true;\n        for (let j = l; j <= r; j++) {\n            const c = s.charCodeAt(j)\
        \ - aCode;\n            if (first[c] < l) {\n                valid = false;\n\
        \                break;\n            }\n            if (last[c] > r) r = last[c];\n\
        \        }\n        if (valid) intervals.push([l, r]);\n    }\n\n    intervals.sort((a,\
        \ b) => a[1] - b[1] || b[0] - a[0]);\n\n    const res = [];\n    let lastEnd\
        \ = -1;\n    for (const [l, r] of intervals) {\n        if (l > lastEnd) {\n\
        \            res.push(s.substring(l, r + 1));\n            lastEnd = r;\n  \
        \      }\n    }\n    return res;\n};"
      typescript: "function maxNumOfSubstrings(s: string): string[] {\n  const n = s.length;\n\
        \  const first = new Array(26).fill(-1);\n  const last = new Array(26).fill(-1);\n\
        \  const aCode = 97;\n\n  for (let i = 0; i < n; i++) {\n    const charIdx =\
        \ s.charCodeAt(i) - aCode;\n    if (first[charIdx] === -1) first[charIdx] =\
        \ i;\n    last[charIdx] = i;\n  }\n\n  const intervals: [number, number][] =\
        \ [];\n  for (let i = 0; i < 26; i++) {\n    if (first[i] === -1) continue;\n\
        \    let l = first[i];\n    let r = last[i];\n    let valid = true;\n    for\
        \ (let j = l; j <= r; j++) {\n      const charIdx = s.charCodeAt(j) - aCode;\n\
        \      if (first[charIdx] < l) {\n        valid = false;\n        break;\n \
        \     }\n      r = Math.max(r, last[charIdx]);\n    }\n    if (valid) {\n  \
        \    intervals.push([l, r]);\n    }\n  }\n\n  intervals.sort((a, b) => a[1]\
        \ !== b[1] ? a[1] - b[1] : b[0] - a[0]);\n\n  const result: string[] = [];\n\
        \  let lastEnd = -1;\n  for (const [l, r] of intervals) {\n    if (l > lastEnd)\
        \ {\n      result.push(s.substring(l, r + 1));\n      lastEnd = r;\n    }\n\
        \  }\n  return result;\n}"
      php: "class Solution {\n\n    /**\n     * @param String $s\n     * @return String[]\n\
        \     */\n    function maxNumOfSubstrings($s) {\n        $n = strlen($s);\n\
        \        $first = array_fill(0, 26, -1);\n        $last = array_fill(0, 26,\
        \ -1);\n        $aCode = ord('a');\n\n        for ($i = 0; $i < $n; $i++) {\n\
        \            $charIdx = ord($s[$i]) - $aCode;\n            if ($first[$charIdx]\
        \ == -1) {\n                $first[$charIdx] = $i;\n            }\n        \
        \    $last[$charIdx] = $i;\n        }\n\n        $intervals = [];\n        for\
        \ ($i = 0; $i < 26; $i++) {\n            if ($first[$i] == -1) continue;\n \
        \           $l = $first[$i];\n            $r = $last[$i];\n            $valid\
        \ = true;\n            for ($j = $l; $j <= $r; $j++) {\n                $charIdx\
        \ = ord($s[$j]) - $aCode;\n                if ($first[$charIdx] < $l) {\n  \
        \                  $valid = false;\n                    break;\n           \
        \     }\n                $r = max($r, $last[$charIdx]);\n            }\n   \
        \         if ($valid) {\n                $intervals[] = [$l, $r];\n        \
        \    }\n        }\n\n        usort($intervals, function($a, $b) {\n        \
        \    if ($a[1] != $b[1]) {\n                return $a[1] - $b[1];\n        \
        \    }\n            return $b[0] - $a[0];\n        });\n\n        $result =\
        \ [];\n        $lastEnd = -1;\n        foreach ($intervals as $iv) {\n     \
        \       if ($iv[0] > $lastEnd) {\n                $result[] = substr($s, $iv[0],\
        \ $iv[1] - $iv[0] + 1);\n                $lastEnd = $iv[1];\n            }\n\
        \        }\n        return $result;\n    }\n}"
      swift: "class Solution {\n    func maxNumOfSubstrings(_ s: String) -> [String]\
        \ {\n        let sBytes = Array(s.utf8)\n        let n = sBytes.count\n    \
        \    var first = Array(repeating: -1, count: 26)\n        var last = Array(repeating:\
        \ -1, count: 26)\n        let aVal = UInt8(97)\n\n        for i in 0..<n {\n\
        \            let charIdx = Int(sBytes[i] - aVal)\n            if first[charIdx]\
        \ == -1 {\n                first[charIdx] = i\n            }\n            last[charIdx]\
        \ = i\n        }\n\n        var intervals = [(Int, Int)]()\n        for i in\
        \ 0..<26 {\n            if first[i] == -1 { continue }\n            let l =\
        \ first[i]\n            var r = last[i]\n            var valid = true\n    \
        \        var j = l\n            while j <= r {\n                let charIdx\
        \ = Int(sBytes[j] - aVal)\n                if first[charIdx] < l {\n       \
        \             valid = false\n                    break\n                }\n\
        \                r = max(r, last[charIdx])\n                j += 1\n       \
        \     }\n            if valid {\n                intervals.append((l, r))\n\
        \            }\n        }\n\n        intervals.sort { (a, b) -> Bool in\n  \
        \          if a.1 != b.1 {\n                return a.1 < b.1\n            }\n\
        \            return a.0 > b.0\n        }\n\n        var result = [String]()\n\
        \        var lastEnd = -1\n        for (l, r) in intervals {\n            if\
        \ l > lastEnd {\n                let startIdx = s.index(s.startIndex, offsetBy:\
        \ l)\n                let endIdx = s.index(s.startIndex, offsetBy: r)\n    \
        \            result.append(String(s[startIdx...endIdx]))\n                lastEnd\
        \ = r\n            }\n        }\n        return result\n    }\n}"
      kotlin: "class Solution {\n    fun maxNumOfSubstrings(s: String): List<String>\
        \ {\n        val n = s.length\n        val first = IntArray(26) { -1 }\n   \
        \     val last = IntArray(26) { -1 }\n        for (i in 0 until n) {\n     \
        \       val charIdx = s[i] - 'a'\n            if (first[charIdx] == -1) {\n\
        \                first[charIdx] = i\n            }\n            last[charIdx]\
        \ = i\n        }\n\n        val intervals = mutableListOf<Pair<Int, Int>>()\n\
        \        for (i in 0 until 26) {\n            if (first[i] == -1) continue\n\
        \            val l = first[i]\n            var r = last[i]\n            var\
        \ valid = true\n            var j = l\n            while (j <= r) {\n      \
        \          val charIdx = s[j] - 'a'\n                if (first[charIdx] < l)\
        \ {\n                    valid = false\n                    break\n        \
        \        }\n                r = Math.max(r, last[charIdx])\n               \
        \ j++\n            }\n            if (valid) {\n                intervals.add(Pair(l,\
        \ r))\n            }\n        }\n\n        intervals.sortWith(Comparator { a,\
        \ b ->\n            if (a.second != b.second) a.second - b.second\n        \
        \    else b.first - a.first\n        })\n\n        val result = mutableListOf<String>()\n\
        \        var lastEnd = -1\n        for (interval in intervals) {\n         \
        \   if (interval.first > lastEnd) {\n                result.add(s.substring(interval.first,\
        \ interval.second + 1))\n                lastEnd = interval.second\n       \
        \     }\n        }\n        return result\n    }\n}"
      dart: "class Solution {\n  List<String> maxNumOfSubstrings(String s) {\n    List<int>\
        \ first = List.filled(26, -1);\n    List<int> last = List.filled(26, -1);\n\
        \    for (int i = 0; i < s.length; i++) {\n      int charIdx = s.codeUnitAt(i)\
        \ - 97;\n      if (first[charIdx] == -1) first[charIdx] = i;\n      last[charIdx]\
        \ = i;\n    }\n\n    List<List<int>> intervals = [];\n    for (int i = 0; i\
        \ < 26; i++) {\n      if (first[i] != -1) {\n        int start = first[i];\n\
        \        int end = last[i];\n        bool valid = true;\n        int j = start;\n\
        \        while (j <= end) {\n          int charIdx = s.codeUnitAt(j) - 97;\n\
        \          if (first[charIdx] < start) {\n            valid = false;\n     \
        \       break;\n          }\n          if (last[charIdx] > end) {\n        \
        \    end = last[charIdx];\n          }\n          j++;\n        }\n        if\
        \ (valid) {\n          intervals.add([start, end]);\n        }\n      }\n  \
        \  }\n\n    intervals.sort((a, b) {\n      int cmp = a[1].compareTo(b[1]);\n\
        \      if (cmp == 0) return b[0].compareTo(a[0]);\n      return cmp;\n    });\n\
        \n    List<String> result = [];\n    int lastEnd = -1;\n    for (var interval\
        \ in intervals) {\n      if (interval[0] > lastEnd) {\n        result.add(s.substring(interval[0],\
        \ interval[1] + 1));\n        lastEnd = interval[1];\n      }\n    }\n    return\
        \ result;\n  }\n}"
      go: "import (\n\t\"sort\"\n)\n\nfunc maxNumOfSubstrings(s string) []string {\n\
        \tfirst := make([]int, 26)\n\tlast := make([]int, 26)\n\tfor i := 0; i < 26;\
        \ i++ {\n\t\tfirst[i] = -1\n\t\tlast[i] = -1\n\t}\n\n\tfor i := 0; i < len(s);\
        \ i++ {\n\t\tidx := int(s[i] - 'a')\n\t\tif first[idx] == -1 {\n\t\t\tfirst[idx]\
        \ = i\n\t\t}\n\t\tlast[idx] = i\n\t}\n\n\tvar intervals [][]int\n\tfor i :=\
        \ 0; i < 26; i++ {\n\t\tif first[i] != -1 {\n\t\t\tstart := first[i]\n\t\t\t\
        end := last[i]\n\t\t\tvalid := true\n\t\t\tfor j := start; j <= end; j++ {\n\
        \t\t\t\tcIdx := int(s[j] - 'a')\n\t\t\t\tif first[cIdx] < start {\n\t\t\t\t\t\
        valid = false\n\t\t\t\t\tbreak\n\t\t\t\t}\n\t\t\t\tif last[cIdx] > end {\n\t\
        \t\t\t\tend = last[cIdx]\n\t\t\t\t}\n\t\t\t}\n\t\t\tif valid {\n\t\t\t\tintervals\
        \ = append(intervals, []int{start, end})\n\t\t\t}\n\t\t}\n\t}\n\n\tsort.Slice(intervals,\
        \ func(i, j int) bool {\n\t\tif intervals[i][1] == intervals[j][1] {\n\t\t\t\
        return intervals[i][0] > intervals[j][0]\n\t\t}\n\t\treturn intervals[i][1]\
        \ < intervals[j][1]\n\t})\n\n\tvar result []string\n\tlastEnd := -1\n\tfor _,\
        \ interval := range intervals {\n\t\tif interval[0] > lastEnd {\n\t\t\tresult\
        \ = append(result, s[interval[0]:interval[1]+1])\n\t\t\tlastEnd = interval[1]\n\
        \t\t}\n\t}\n\treturn result\n}"
      ruby: "def max_num_of_substrings(s)\n  first = Array.new(26, -1)\n  last = Array.new(26,\
        \ -1)\n\n  s.each_char.with_index do |char, i|\n    idx = char.ord - 'a'.ord\n\
        \    first[idx] = i if first[idx] == -1\n    last[idx] = i\n  end\n\n  intervals\
        \ = []\n  (0...26).each do |i|\n    next if first[i] == -1\n\n    start = first[i]\n\
        \    finish = last[i]\n    valid = true\n    j = start\n    while j <= finish\n\
        \      char_idx = s[j].ord - 'a'.ord\n      if first[char_idx] < start\n   \
        \     valid = false\n        break\n      end\n      finish = last[char_idx]\
        \ if last[char_idx] > finish\n      j += 1\n    end\n\n    intervals << [start,\
        \ finish] if valid\n  end\n\n  intervals.sort_by! { |interval| [interval[1],\
        \ -interval[0]] }\n\n  result = []\n  last_end = -1\n  intervals.each do |start,\
        \ finish|\n    if start > last_end\n      result << s[start..finish]\n     \
        \ last_end = finish\n    end\n  end\n  result\nend"
      scala: "object Solution {\n  def maxNumOfSubstrings(s: String): List[String] =\
        \ {\n    val first = Array.fill(26)(-1)\n    val last = Array.fill(26)(-1)\n\
        \    for (i <- 0 until s.length) {\n      val idx = s(i) - 'a'\n      if (first(idx)\
        \ == -1) first(idx) = i\n      last(idx) = i\n    }\n\n    var intervals = List.empty[(Int,\
        \ Int)]\n    for (i <- 0 until 26) {\n      if (first(i) != -1) {\n        val\
        \ start = first(i)\n        var end = last(i)\n        var j = start\n     \
        \   var valid = true\n        while (j <= end && valid) {\n          val cIdx\
        \ = s(j) - 'a'\n          if (first(cIdx) < start) {\n            valid = false\n\
        \          } else {\n            if (last(cIdx) > end) {\n              end\
        \ = last(cIdx)\n            }\n            j += 1\n          }\n        }\n\
        \        if (valid) {\n          intervals = (start, end) :: intervals\n   \
        \     }\n      }\n    }\n\n    val sorted = intervals.sortBy(x => (x._2, -x._1))\n\
        \    var res = List.empty[String]\n    var lastE = -1\n    for ((start, end)\
        \ <- sorted) {\n      if (start > lastE) {\n        res = s.substring(start,\
        \ end + 1) :: res\n        lastE = end\n      }\n    }\n    res.reverse\n  }\n\
        }"
      rust: "impl Solution {\n    pub fn max_num_of_substrings(s: String) -> Vec<String>\
        \ {\n        let n = s.len();\n        let bytes = s.as_bytes();\n        let\
        \ mut first = vec![usize::MAX; 26];\n        let mut last = vec![0; 26];\n \
        \       let mut exists = vec![false; 26];\n\n        for (i, &b) in bytes.iter().enumerate()\
        \ {\n            let idx = (b - b'a') as usize;\n            if first[idx] ==\
        \ usize::MAX {\n                first[idx] = i;\n            }\n           \
        \ last[idx] = i;\n            exists[idx] = true;\n        }\n\n        let\
        \ mut candidates = Vec::new();\n        for i in 0..26 {\n            if !exists[i]\
        \ {\n                continue;\n            }\n            let l = first[i];\n\
        \            let mut r = last[i];\n            let mut valid = true;\n     \
        \       let mut j = l;\n            while j <= r {\n                let c =\
        \ (bytes[j] - b'a') as usize;\n                if first[c] < l {\n         \
        \           valid = false;\n                    break;\n                }\n\
        \                r = r.max(last[c]);\n                j += 1;\n            }\n\
        \            if valid {\n                candidates.push((l, r));\n        \
        \    }\n        }\n\n        candidates.sort_by(|a, b| a.1.cmp(&b.1).then(b.0.cmp(&a.0)));\n\
        \n        let mut result = Vec::new();\n        let mut last_end: i32 = -1;\n\
        \        for (l, r) in candidates {\n            if l as i32 > last_end {\n\
        \                result.push(s[l..=r].to_string());\n                last_end\
        \ = r as i32;\n            }\n        }\n        result\n    }\n}"
      racket: "(define/contract (max-num-of-substrings s)\n  (-> string? (listof string?))\n\
        \  (let* ([n (string-length s)]\n         [first (make-vector 26 -1)]\n    \
        \     [last (make-vector 26 -1)])\n    (for ([i (in-range n)])\n      (let ([c\
        \ (- (char->integer (string-ref s i)) 97)])\n        (when (= (vector-ref first\
        \ c) -1)\n          (vector-set! first c i))\n        (vector-set! last c i)))\n\
        \    (let* ([candidates\n            (for/fold ([acc '()])\n               \
        \       ([i (in-range 26)])\n              (let ([l (vector-ref first i)])\n\
        \                (if (= l -1)\n                    acc\n                   \
        \ (let-values ([(valid r)\n                                  (let loop ([j l]\
        \ [curr-r (vector-ref last i)])\n                                    (if (<=\
        \ j curr-r)\n                                        (let ([c (- (char->integer\
        \ (string-ref s j)) 97)])\n                                          (if (<\
        \ (vector-ref first c) l)\n                                              (values\
        \ #f curr-r)\n                                              (loop (+ j 1) (max\
        \ curr-r (vector-ref last c)))))\n                                        (values\
        \ #t curr-r)))])\n                      (if valid\n                        \
        \  (cons (cons l r) acc)\n                          acc))))]\n           [sorted\
        \ (sort candidates (lambda (a b)\n                                      (if\
        \ (= (cdr a) (cdr b))\n                                          (> (car a)\
        \ (car b))\n                                          (< (cdr a) (cdr b)))))]\n\
        \           [res-final\n            (let-values ([(picked last-e)\n        \
        \                  (for/fold ([res '()] [last-e -1])\n                     \
        \               ([cand sorted])\n                            (if (> (car cand)\
        \ last-e)\n                                (values (cons (substring s (car cand)\
        \ (+ (cdr cand) 1)) res) (cdr cand))\n                                (values\
        \ res last-e)))])\n              (reverse picked))])\n      res-final)))"
      erlang: "-spec max_num_of_substrings(S :: unicode:unicode_binary()) -> [unicode:unicode_binary()].\n\
        max_num_of_substrings(S) ->\n    N = byte_size(S),\n    First = find_first(S,\
        \ 0, N, #{}),\n    Last = find_last(S, 0, N, #{}),\n    Chars = maps:keys(First),\n\
        \    Candidates = find_candidates(Chars, S, First, Last, []),\n    Sorted =\
        \ lists:sort(fun({L1, R1}, {L2, R2}) -> \n        if R1 == R2 -> L1 > L2; true\
        \ -> R1 < R2 end \n    end, Candidates),\n    pick_substrings(Sorted, -1, S,\
        \ []).\n\nfind_first(S, I, N, Map) when I < N ->\n    C = binary:at(S, I),\n\
        \    NewMap = case maps:is_key(C, Map) of\n        true -> Map;\n        false\
        \ -> Map#{C => I}\n    end,\n    find_first(S, I + 1, N, NewMap);\nfind_first(_,\
        \ _, _, Map) -> Map.\n\nfind_last(S, I, N, Map) when I < N ->\n    C = binary:at(S,\
        \ I),\n    find_last(S, I + 1, N, Map#{C => I});\nfind_last(_, _, _, Map) ->\
        \ Map.\n\nfind_candidates([], _, _, _, Acc) -> Acc;\nfind_candidates([Char |\
        \ T], S, First, Last, Acc) ->\n    L = maps:get(Char, First),\n    case expand_range(L,\
        \ maps:get(Char, Last), L, S, First, Last) of\n        {ok, R} -> find_candidates(T,\
        \ S, First, Last, [{L, R} | Acc]);\n        fail -> find_candidates(T, S, First,\
        \ Last, Acc)\n    end.\n\nexpand_range(J, R, L, S, First, Last) when J =< R\
        \ ->\n    C = binary:at(S, J),\n    CFirst = maps:get(C, First),\n    CLast\
        \ = maps:get(C, Last),\n    if CFirst < L -> fail;\n       true -> expand_range(J\
        \ + 1, erlang:max(R, CLast), L, S, First, Last)\n    end;\nexpand_range(_, R,\
        \ _, _, _, _) -> {ok, R}.\n\npick_substrings([], _, _, Acc) -> lists:reverse(Acc);\n\
        pick_substrings([{L, R} | T], LastEnd, S, Acc) ->\n    if L > LastEnd ->\n \
        \       Sub = binary_part(S, L, R - L + 1),\n        pick_substrings(T, R, S,\
        \ [Sub | Acc]);\n       true ->\n        pick_substrings(T, LastEnd, S, Acc)\n\
        \    end."
      elixir: "defmodule Solution do\n  @spec max_num_of_substrings(s :: String.t())\
        \ :: [String.t()]\n  def max_num_of_substrings(s) do\n    n = byte_size(s)\n\
        \    first = find_first(s, 0, n, %{})\n    last = find_last(s, 0, n, %{})\n\n\
        \    chars = Map.keys(first)\n    candidates = find_candidates(chars, s, first,\
        \ last, [])\n    sorted = Enum.sort(candidates, fn {l1, r1}, {l2, r2} ->\n \
        \     if r1 == r2, do: l1 > l2, else: r1 < r2\n    end)\n\n    pick_substrings(sorted,\
        \ -1, s, [])\n  end\n\n  defp find_first(s, i, n, map) when i < n do\n    char\
        \ = :binary.at(s, i)\n    new_map = if Map.has_key?(map, char), do: map, else:\
        \ Map.put(map, char, i)\n    find_first(s, i + 1, n, new_map)\n  end\n  defp\
        \ find_first(_, _, _, map), do: map\n\n  defp find_last(s, i, n, map) when i\
        \ < n do\n    char = :binary.at(s, i)\n    find_last(s, i + 1, n, Map.put(map,\
        \ char, i))\n  end\n  defp find_last(_, _, _, map), do: map\n\n  defp find_candidates([],\
        \ _, _, _, acc), do: acc\n  defp find_candidates([char | t], s, first, last,\
        \ acc) do\n    l = Map.get(first, char)\n    case expand_range(l, Map.get(last,\
        \ char), l, s, first, last) do\n      {:ok, r} -> find_candidates(t, s, first,\
        \ last, [{l, r} | acc])\n      :fail -> find_candidates(t, s, first, last, acc)\n\
        \    end\n  end\n\n  defp expand_range(j, r, l, s, first, last) when j <= r\
        \ do\n    c = :binary.at(s, j)\n    c_first = Map.get(first, c)\n    c_last\
        \ = Map.get(last, c)\n    if c_first < l do\n      :fail\n    else\n      expand_range(j\
        \ + 1, max(r, c_last), l, s, first, last)\n    end\n  end\n  defp expand_range(_j,\
        \ r, _l, _s, _first, _last), do: {:ok, r}\n\n  defp pick_substrings([], _last_end,\
        \ _s, acc), do: Enum.reverse(acc)\n  defp pick_substrings([{l, r} | t], last_end,\
        \ s, acc) do\n    if l > last_end do\n      sub = binary_part(s, l, r - l +\
        \ 1)\n      pick_substrings(t, r, s, [sub | acc])\n    else\n      pick_substrings(t,\
        \ last_end, s, acc)\n    end\n  end\nend"
    approach: 'The algorithm first identifies the first and last occurrence indices
      for each of the 26 lowercase English characters. For every character present in
      the string, we attempt to find the smallest valid substring starting at its first
      occurrence. A valid substring must satisfy the condition that if it contains any
      character, it must contain all occurrences of that character within the string.
      We expand the initial range $[first[c], last[c]]$ by iteratively including the
      full range of any character encountered within the current bounds. If we find
      a character whose first occurrence is before our starting index, then any valid
      substring containing the current character must start earlier; thus, the substring
      starting at the current index is discarded.


      After collecting all such minimal valid intervals, we apply a greedy strategy
      similar to the classic interval scheduling problem. Given the property that any
      two valid intervals in this problem are either disjoint or nested, sorting the
      intervals by their end positions allows us to pick the maximum number of non-overlapping
      substrings. By picking intervals with the earliest end times, we naturally prioritize
      inner (shorter) intervals when nesting occurs, satisfying the requirement to minimize
      total length for the maximum possible count. We iterate through the sorted candidates
      and pick each interval that starts after the end of the previously selected one.'
    time_complexity: O(N \cdot \Sigma) where N is the length of the string and $\Sigma$
      is the size of the character set (26). We spend O(N) to find the first and last
      occurrences. For each of the 26 characters, we may scan up to O(N) characters
      during the expansion phase, leading to $O(26N)$. Sorting and greedy selection
      are $O(\Sigma \log \Sigma)$ and $O(\Sigma)$, respectively.
    space_complexity: O(N) to store the input string and the resulting substrings. The
      metadata for characters (first/last indices) and the list of candidate intervals
      require $O(\Sigma)$ space, which is constant.
    elapsed_time: 394.03836393356323
    model: gemini-3-flash-preview
    generated_at: '2026-09-18 02:37:46 '
---

## Problem #1520: Maximum Number of Non-Overlapping Substrings

**Difficulty:** Hard

**Topics:** Hash Table, String, Greedy, Sorting

## Problem Description

<p>Given a string <code>s</code> of lowercase letters, you need to find the maximum number of <strong>non-empty</strong> substrings of <code>s</code> that meet the following conditions:</p>

<ol>
	<li>The substrings do not overlap, that is for any two substrings <code>s[i..j]</code> and <code>s[x..y]</code>, either <code>j &lt; x</code> or <code>i &gt; y</code> is true.</li>
	<li>A substring that contains a certain character <code>c</code> must also contain all occurrences of <code>c</code>.</li>
</ol>

<p>Find <em>the maximum number of substrings that meet the above conditions</em>. If there are multiple solutions with the same number of substrings, <em>return the one with minimum total length. </em>It can be shown that there exists a unique solution of minimum total length.</p>

<p>Notice that you can return the substrings in <strong>any</strong> order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;adefaddaccc&quot;
<strong>Output:</strong> [&quot;e&quot;,&quot;f&quot;,&quot;ccc&quot;]
<b>Explanation:</b>&nbsp;The following are all the possible substrings that meet the conditions:
[
&nbsp; &quot;adefaddaccc&quot;
&nbsp; &quot;adefadda&quot;,
&nbsp; &quot;ef&quot;,
&nbsp; &quot;e&quot;,
  &quot;f&quot;,
&nbsp; &quot;ccc&quot;,
]
If we choose the first string, we cannot choose anything else and we&#39;d get only 1. If we choose &quot;adefadda&quot;, we are left with &quot;ccc&quot; which is the only one that doesn&#39;t overlap, thus obtaining 2 substrings. Notice also, that it&#39;s not optimal to choose &quot;ef&quot; since it can be split into two. Therefore, the optimal way is to choose [&quot;e&quot;,&quot;f&quot;,&quot;ccc&quot;] which gives us 3 substrings. No other solution of the same number of substrings exist.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abbaccd&quot;
<strong>Output:</strong> [&quot;d&quot;,&quot;bb&quot;,&quot;cc&quot;]
<b>Explanation: </b>Notice that while the set of substrings [&quot;d&quot;,&quot;abba&quot;,&quot;cc&quot;] also has length 3, it&#39;s considered incorrect since it has larger total length.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
</ul>


## Hints

1. Notice that it's impossible for any two valid substrings to overlap unless one is inside another.

2. We can start by finding the starting and ending index for each character.

3. From these indices, we can form the substrings by expanding each character's range if necessary (if another character exists in the range with smaller/larger starting/ending index).

4. Sort the valid substrings by length and greedily take those with the smallest length, discarding the ones that overlap those we took.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The algorithm first identifies the first and last occurrence indices for each of the 26 lowercase English characters. For every character present in the string, we attempt to find the smallest valid substring starting at its first occurrence. A valid substring must satisfy the condition that if it contains any character, it must contain all occurrences of that character within the string. We expand the initial range $[first[c], last[c]]$ by iteratively including the full range of any character encountered within the current bounds. If we find a character whose first occurrence is before our starting index, then any valid substring containing the current character must start earlier; thus, the substring starting at the current index is discarded.

After collecting all such minimal valid intervals, we apply a greedy strategy similar to the classic interval scheduling problem. Given the property that any two valid intervals in this problem are either disjoint or nested, sorting the intervals by their end positions allows us to pick the maximum number of non-overlapping substrings. By picking intervals with the earliest end times, we naturally prioritize inner (shorter) intervals when nesting occurs, satisfying the requirement to minimize total length for the maximum possible count. We iterate through the sorted candidates and pick each interval that starts after the end of the previously selected one.

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
    vector<string> maxNumOfSubstrings(string s) {
        int n = s.length();
        vector<int> first(26, -1);
        vector<int> last(26, -1);
        for (int i = 0; i < n; ++i) {
            int c = s[i] - 'a';
            if (first[c] == -1) first[c] = i;
            last[c] = i;
        }

        vector<pair<int, int>> intervals;
        for (int i = 0; i < 26; ++i) {
            if (first[i] == -1) continue;
            int l = first[i];
            int r = last[i];
            bool possible = true;
            for (int j = l; j <= r; ++j) {
                int c = s[j] - 'a';
                if (first[c] < l) {
                    possible = false;
                    break;
                }
                r = max(r, last[c]);
            }
            if (possible) {
                intervals.push_back({l, r});
            }
        }

        sort(intervals.begin(), intervals.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
            return a.second < b.second;
        });

        vector<string> result;
        int last_end = -1;
        for (auto& interval : intervals) {
            if (interval.first > last_end) {
                result.push_back(s.substr(interval.first, interval.second - interval.first + 1));
                last_end = interval.second;
            }
        }
        return result;
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
    public List<String> maxNumOfSubstrings(String s) {
        int n = s.length();
        int[] first = new int[26];
        int[] last = new int[26];
        Arrays.fill(first, -1);
        Arrays.fill(last, -1);
        for (int i = 0; i < n; i++) {
            int c = s.charAt(i) - 'a';
            if (first[c] == -1) first[c] = i;
            last[c] = i;
        }

        List<int[]> intervals = new ArrayList<>();
        for (int i = 0; i < 26; i++) {
            if (first[i] == -1) continue;
            int l = first[i];
            int r = last[i];
            boolean possible = true;
            for (int j = l; j <= r; j++) {
                int c = s.charAt(j) - 'a';
                if (first[c] < l) {
                    possible = false;
                    break;
                }
                r = Math.max(r, last[c]);
            }
            if (possible) {
                intervals.add(new int[]{l, r});
            }
        }

        intervals.sort((a, b) -> Integer.compare(a[1], b[1]));

        List<String> result = new ArrayList<>();
        int lastEnd = -1;
        for (int[] interval : intervals) {
            if (interval[0] > lastEnd) {
                result.add(s.substring(interval[0], interval[1] + 1));
                lastEnd = interval[1];
            }
        }
        return result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        first = [-1] * 26
        last = [-1] * 26
        for i, char in enumerate(s):
            idx = ord(char) - ord('a')
            if first[idx] == -1:
                first[idx] = i
            last[idx] = i

        intervals = []
        for i in range(26):
            if first[i] == -1:
                continue
            l = first[i]
            r = last[i]
            possible = True
            j = l
            while j <= r:
                char_idx = ord(s[j]) - ord('a')
                if first[char_idx] < l:
                    possible = False
                    break
                r = max(r, last[char_idx])
                j += 1
            if possible:
                intervals.append((l, r))

        intervals.sort(key=lambda x: x[1])

        res = []
        last_end = -1
        for l, r in intervals:
            if l > last_end:
                res.append(s[l:r+1])
                last_end = r
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = [-1] * 26
        last = [-1] * 26
        s_ints = [ord(c) - 97 for c in s]
        for i, c_idx in enumerate(s_ints):
            if first[c_idx] == -1:
                first[c_idx] = i
            last[c_idx] = i

        intervals = []
        for i in range(26):
            if first[i] == -1:
                continue
            l, r = first[i], last[i]
            valid = True
            j = l
            while j <= r:
                c_idx = s_ints[j]
                if first[c_idx] < l:
                    valid = False
                    break
                r = max(r, last[c_idx])
                j += 1
            if valid:
                intervals.append((l, r))

        intervals.sort(key=lambda x: (x[1], -x[0]))
        res = []
        last_end = -1
        for l, r in intervals:
            if l > last_end:
                res.append(s[l : r + 1])
                last_end = r
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

typedef struct {
    int l, r;
} Interval;

int compare(const void* a, const void* b) {
    const Interval* i1 = (const Interval*)a;
    const Interval* i2 = (const Interval*)b;
    if (i1->r != i2->r) return i1->r - i2->r;
    return i2->l - i1->l;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** maxNumOfSubstrings(char* s, int* returnSize) {
    int n = strlen(s);
    int first[26], last[26];
    for (int i = 0; i < 26; i++) first[i] = -1;
    for (int i = 0; i < n; i++) {
        int c = s[i] - 'a';
        if (first[c] == -1) first[c] = i;
        last[c] = i;
    }

    Interval intervals[26];
    int intervalCount = 0;
    for (int i = 0; i < 26; i++) {
        if (first[i] == -1) continue;
        int l = first[i], r = last[i];
        bool valid = true;
        for (int j = l; j <= r; j++) {
            int c = s[j] - 'a';
            if (first[c] < l) {
                valid = false;
                break;
            }
            if (last[c] > r) r = last[c];
        }
        if (valid) {
            intervals[intervalCount].l = l;
            intervals[intervalCount].r = r;
            intervalCount++;
        }
    }

    qsort(intervals, intervalCount, sizeof(Interval), compare);

    char** res = (char**)malloc(26 * sizeof(char*));
    int count = 0;
    int last_end = -1;
    for (int i = 0; i < intervalCount; i++) {
        if (intervals[i].l > last_end) {
            int l = intervals[i].l;
            int r = intervals[i].r;
            int len = r - l + 1;
            res[count] = (char*)malloc((len + 1) * sizeof(char));
            memcpy(res[count], s + l, len);
            res[count][len] = '\0';
            last_end = r;
            count++;
        }
    }
    *returnSize = count;
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

public class Solution {
    public IList<string> MaxNumOfSubstrings(string s) {
        int n = s.Length;
        int[] first = new int[26];
        int[] last = new int[26];
        for (int i = 0; i < 26; i++) first[i] = -1;
        for (int i = 0; i < n; i++) {
            int c = s[i] - 'a';
            if (first[c] == -1) first[c] = i;
            last[c] = i;
        }

        var intervals = new List<(int l, int r)>();
        for (int i = 0; i < 26; i++) {
            if (first[i] == -1) continue;
            int l = first[i], r = last[i];
            bool valid = true;
            for (int j = l; j <= r; j++) {
                int c = s[j] - 'a';
                if (first[c] < l) {
                    valid = false;
                    break;
                }
                if (last[c] > r) r = last[c];
            }
            if (valid) intervals.Add((l, r));
        }

        var sortedIntervals = intervals.OrderBy(x => x.r).ThenByDescending(x => x.l);
        var res = new List<string>();
        int lastEnd = -1;
        foreach (var interval in sortedIntervals) {
            if (interval.l > lastEnd) {
                res.Add(s.Substring(interval.l, interval.r - interval.l + 1));
                lastEnd = interval.r;
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
 * @return {string[]}
 */
var maxNumOfSubstrings = function(s) {
    const n = s.length;
    const first = new Array(26).fill(-1);
    const last = new Array(26).fill(-1);
    const aCode = 'a'.charCodeAt(0);

    for (let i = 0; i < n; i++) {
        const c = s.charCodeAt(i) - aCode;
        if (first[c] === -1) first[c] = i;
        last[c] = i;
    }

    const intervals = [];
    for (let i = 0; i < 26; i++) {
        if (first[i] === -1) continue;
        let l = first[i], r = last[i];
        let valid = true;
        for (let j = l; j <= r; j++) {
            const c = s.charCodeAt(j) - aCode;
            if (first[c] < l) {
                valid = false;
                break;
            }
            if (last[c] > r) r = last[c];
        }
        if (valid) intervals.push([l, r]);
    }

    intervals.sort((a, b) => a[1] - b[1] || b[0] - a[0]);

    const res = [];
    let lastEnd = -1;
    for (const [l, r] of intervals) {
        if (l > lastEnd) {
            res.push(s.substring(l, r + 1));
            lastEnd = r;
        }
    }
    return res;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxNumOfSubstrings(s: string): string[] {
  const n = s.length;
  const first = new Array(26).fill(-1);
  const last = new Array(26).fill(-1);
  const aCode = 97;

  for (let i = 0; i < n; i++) {
    const charIdx = s.charCodeAt(i) - aCode;
    if (first[charIdx] === -1) first[charIdx] = i;
    last[charIdx] = i;
  }

  const intervals: [number, number][] = [];
  for (let i = 0; i < 26; i++) {
    if (first[i] === -1) continue;
    let l = first[i];
    let r = last[i];
    let valid = true;
    for (let j = l; j <= r; j++) {
      const charIdx = s.charCodeAt(j) - aCode;
      if (first[charIdx] < l) {
        valid = false;
        break;
      }
      r = Math.max(r, last[charIdx]);
    }
    if (valid) {
      intervals.push([l, r]);
    }
  }

  intervals.sort((a, b) => a[1] !== b[1] ? a[1] - b[1] : b[0] - a[0]);

  const result: string[] = [];
  let lastEnd = -1;
  for (const [l, r] of intervals) {
    if (l > lastEnd) {
      result.push(s.substring(l, r + 1));
      lastEnd = r;
    }
  }
  return result;
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
     * @return String[]
     */
    function maxNumOfSubstrings($s) {
        $n = strlen($s);
        $first = array_fill(0, 26, -1);
        $last = array_fill(0, 26, -1);
        $aCode = ord('a');

        for ($i = 0; $i < $n; $i++) {
            $charIdx = ord($s[$i]) - $aCode;
            if ($first[$charIdx] == -1) {
                $first[$charIdx] = $i;
            }
            $last[$charIdx] = $i;
        }

        $intervals = [];
        for ($i = 0; $i < 26; $i++) {
            if ($first[$i] == -1) continue;
            $l = $first[$i];
            $r = $last[$i];
            $valid = true;
            for ($j = $l; $j <= $r; $j++) {
                $charIdx = ord($s[$j]) - $aCode;
                if ($first[$charIdx] < $l) {
                    $valid = false;
                    break;
                }
                $r = max($r, $last[$charIdx]);
            }
            if ($valid) {
                $intervals[] = [$l, $r];
            }
        }

        usort($intervals, function($a, $b) {
            if ($a[1] != $b[1]) {
                return $a[1] - $b[1];
            }
            return $b[0] - $a[0];
        });

        $result = [];
        $lastEnd = -1;
        foreach ($intervals as $iv) {
            if ($iv[0] > $lastEnd) {
                $result[] = substr($s, $iv[0], $iv[1] - $iv[0] + 1);
                $lastEnd = $iv[1];
            }
        }
        return $result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxNumOfSubstrings(_ s: String) -> [String] {
        let sBytes = Array(s.utf8)
        let n = sBytes.count
        var first = Array(repeating: -1, count: 26)
        var last = Array(repeating: -1, count: 26)
        let aVal = UInt8(97)

        for i in 0..<n {
            let charIdx = Int(sBytes[i] - aVal)
            if first[charIdx] == -1 {
                first[charIdx] = i
            }
            last[charIdx] = i
        }

        var intervals = [(Int, Int)]()
        for i in 0..<26 {
            if first[i] == -1 { continue }
            let l = first[i]
            var r = last[i]
            var valid = true
            var j = l
            while j <= r {
                let charIdx = Int(sBytes[j] - aVal)
                if first[charIdx] < l {
                    valid = false
                    break
                }
                r = max(r, last[charIdx])
                j += 1
            }
            if valid {
                intervals.append((l, r))
            }
        }

        intervals.sort { (a, b) -> Bool in
            if a.1 != b.1 {
                return a.1 < b.1
            }
            return a.0 > b.0
        }

        var result = [String]()
        var lastEnd = -1
        for (l, r) in intervals {
            if l > lastEnd {
                let startIdx = s.index(s.startIndex, offsetBy: l)
                let endIdx = s.index(s.startIndex, offsetBy: r)
                result.append(String(s[startIdx...endIdx]))
                lastEnd = r
            }
        }
        return result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxNumOfSubstrings(s: String): List<String> {
        val n = s.length
        val first = IntArray(26) { -1 }
        val last = IntArray(26) { -1 }
        for (i in 0 until n) {
            val charIdx = s[i] - 'a'
            if (first[charIdx] == -1) {
                first[charIdx] = i
            }
            last[charIdx] = i
        }

        val intervals = mutableListOf<Pair<Int, Int>>()
        for (i in 0 until 26) {
            if (first[i] == -1) continue
            val l = first[i]
            var r = last[i]
            var valid = true
            var j = l
            while (j <= r) {
                val charIdx = s[j] - 'a'
                if (first[charIdx] < l) {
                    valid = false
                    break
                }
                r = Math.max(r, last[charIdx])
                j++
            }
            if (valid) {
                intervals.add(Pair(l, r))
            }
        }

        intervals.sortWith(Comparator { a, b ->
            if (a.second != b.second) a.second - b.second
            else b.first - a.first
        })

        val result = mutableListOf<String>()
        var lastEnd = -1
        for (interval in intervals) {
            if (interval.first > lastEnd) {
                result.add(s.substring(interval.first, interval.second + 1))
                lastEnd = interval.second
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
  List<String> maxNumOfSubstrings(String s) {
    List<int> first = List.filled(26, -1);
    List<int> last = List.filled(26, -1);
    for (int i = 0; i < s.length; i++) {
      int charIdx = s.codeUnitAt(i) - 97;
      if (first[charIdx] == -1) first[charIdx] = i;
      last[charIdx] = i;
    }

    List<List<int>> intervals = [];
    for (int i = 0; i < 26; i++) {
      if (first[i] != -1) {
        int start = first[i];
        int end = last[i];
        bool valid = true;
        int j = start;
        while (j <= end) {
          int charIdx = s.codeUnitAt(j) - 97;
          if (first[charIdx] < start) {
            valid = false;
            break;
          }
          if (last[charIdx] > end) {
            end = last[charIdx];
          }
          j++;
        }
        if (valid) {
          intervals.add([start, end]);
        }
      }
    }

    intervals.sort((a, b) {
      int cmp = a[1].compareTo(b[1]);
      if (cmp == 0) return b[0].compareTo(a[0]);
      return cmp;
    });

    List<String> result = [];
    int lastEnd = -1;
    for (var interval in intervals) {
      if (interval[0] > lastEnd) {
        result.add(s.substring(interval[0], interval[1] + 1));
        lastEnd = interval[1];
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
import (
	"sort"
)

func maxNumOfSubstrings(s string) []string {
	first := make([]int, 26)
	last := make([]int, 26)
	for i := 0; i < 26; i++ {
		first[i] = -1
		last[i] = -1
	}

	for i := 0; i < len(s); i++ {
		idx := int(s[i] - 'a')
		if first[idx] == -1 {
			first[idx] = i
		}
		last[idx] = i
	}

	var intervals [][]int
	for i := 0; i < 26; i++ {
		if first[i] != -1 {
			start := first[i]
			end := last[i]
			valid := true
			for j := start; j <= end; j++ {
				cIdx := int(s[j] - 'a')
				if first[cIdx] < start {
					valid = false
					break
				}
				if last[cIdx] > end {
					end = last[cIdx]
				}
			}
			if valid {
				intervals = append(intervals, []int{start, end})
			}
		}
	}

	sort.Slice(intervals, func(i, j int) bool {
		if intervals[i][1] == intervals[j][1] {
			return intervals[i][0] > intervals[j][0]
		}
		return intervals[i][1] < intervals[j][1]
	})

	var result []string
	lastEnd := -1
	for _, interval := range intervals {
		if interval[0] > lastEnd {
			result = append(result, s[interval[0]:interval[1]+1])
			lastEnd = interval[1]
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
def max_num_of_substrings(s)
  first = Array.new(26, -1)
  last = Array.new(26, -1)

  s.each_char.with_index do |char, i|
    idx = char.ord - 'a'.ord
    first[idx] = i if first[idx] == -1
    last[idx] = i
  end

  intervals = []
  (0...26).each do |i|
    next if first[i] == -1

    start = first[i]
    finish = last[i]
    valid = true
    j = start
    while j <= finish
      char_idx = s[j].ord - 'a'.ord
      if first[char_idx] < start
        valid = false
        break
      end
      finish = last[char_idx] if last[char_idx] > finish
      j += 1
    end

    intervals << [start, finish] if valid
  end

  intervals.sort_by! { |interval| [interval[1], -interval[0]] }

  result = []
  last_end = -1
  intervals.each do |start, finish|
    if start > last_end
      result << s[start..finish]
      last_end = finish
    end
  end
  result
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def maxNumOfSubstrings(s: String): List[String] = {
    val first = Array.fill(26)(-1)
    val last = Array.fill(26)(-1)
    for (i <- 0 until s.length) {
      val idx = s(i) - 'a'
      if (first(idx) == -1) first(idx) = i
      last(idx) = i
    }

    var intervals = List.empty[(Int, Int)]
    for (i <- 0 until 26) {
      if (first(i) != -1) {
        val start = first(i)
        var end = last(i)
        var j = start
        var valid = true
        while (j <= end && valid) {
          val cIdx = s(j) - 'a'
          if (first(cIdx) < start) {
            valid = false
          } else {
            if (last(cIdx) > end) {
              end = last(cIdx)
            }
            j += 1
          }
        }
        if (valid) {
          intervals = (start, end) :: intervals
        }
      }
    }

    val sorted = intervals.sortBy(x => (x._2, -x._1))
    var res = List.empty[String]
    var lastE = -1
    for ((start, end) <- sorted) {
      if (start > lastE) {
        res = s.substring(start, end + 1) :: res
        lastE = end
      }
    }
    res.reverse
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_num_of_substrings(s: String) -> Vec<String> {
        let n = s.len();
        let bytes = s.as_bytes();
        let mut first = vec![usize::MAX; 26];
        let mut last = vec![0; 26];
        let mut exists = vec![false; 26];

        for (i, &b) in bytes.iter().enumerate() {
            let idx = (b - b'a') as usize;
            if first[idx] == usize::MAX {
                first[idx] = i;
            }
            last[idx] = i;
            exists[idx] = true;
        }

        let mut candidates = Vec::new();
        for i in 0..26 {
            if !exists[i] {
                continue;
            }
            let l = first[i];
            let mut r = last[i];
            let mut valid = true;
            let mut j = l;
            while j <= r {
                let c = (bytes[j] - b'a') as usize;
                if first[c] < l {
                    valid = false;
                    break;
                }
                r = r.max(last[c]);
                j += 1;
            }
            if valid {
                candidates.push((l, r));
            }
        }

        candidates.sort_by(|a, b| a.1.cmp(&b.1).then(b.0.cmp(&a.0)));

        let mut result = Vec::new();
        let mut last_end: i32 = -1;
        for (l, r) in candidates {
            if l as i32 > last_end {
                result.push(s[l..=r].to_string());
                last_end = r as i32;
            }
        }
        result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (max-num-of-substrings s)
  (-> string? (listof string?))
  (let* ([n (string-length s)]
         [first (make-vector 26 -1)]
         [last (make-vector 26 -1)])
    (for ([i (in-range n)])
      (let ([c (- (char->integer (string-ref s i)) 97)])
        (when (= (vector-ref first c) -1)
          (vector-set! first c i))
        (vector-set! last c i)))
    (let* ([candidates
            (for/fold ([acc '()])
                      ([i (in-range 26)])
              (let ([l (vector-ref first i)])
                (if (= l -1)
                    acc
                    (let-values ([(valid r)
                                  (let loop ([j l] [curr-r (vector-ref last i)])
                                    (if (<= j curr-r)
                                        (let ([c (- (char->integer (string-ref s j)) 97)])
                                          (if (< (vector-ref first c) l)
                                              (values #f curr-r)
                                              (loop (+ j 1) (max curr-r (vector-ref last c)))))
                                        (values #t curr-r)))])
                      (if valid
                          (cons (cons l r) acc)
                          acc))))]
           [sorted (sort candidates (lambda (a b)
                                      (if (= (cdr a) (cdr b))
                                          (> (car a) (car b))
                                          (< (cdr a) (cdr b)))))]
           [res-final
            (let-values ([(picked last-e)
                          (for/fold ([res '()] [last-e -1])
                                    ([cand sorted])
                            (if (> (car cand) last-e)
                                (values (cons (substring s (car cand) (+ (cdr cand) 1)) res) (cdr cand))
                                (values res last-e)))])
              (reverse picked))])
      res-final)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_num_of_substrings(S :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
max_num_of_substrings(S) ->
    N = byte_size(S),
    First = find_first(S, 0, N, #{}),
    Last = find_last(S, 0, N, #{}),
    Chars = maps:keys(First),
    Candidates = find_candidates(Chars, S, First, Last, []),
    Sorted = lists:sort(fun({L1, R1}, {L2, R2}) -> 
        if R1 == R2 -> L1 > L2; true -> R1 < R2 end 
    end, Candidates),
    pick_substrings(Sorted, -1, S, []).

find_first(S, I, N, Map) when I < N ->
    C = binary:at(S, I),
    NewMap = case maps:is_key(C, Map) of
        true -> Map;
        false -> Map#{C => I}
    end,
    find_first(S, I + 1, N, NewMap);
find_first(_, _, _, Map) -> Map.

find_last(S, I, N, Map) when I < N ->
    C = binary:at(S, I),
    find_last(S, I + 1, N, Map#{C => I});
find_last(_, _, _, Map) -> Map.

find_candidates([], _, _, _, Acc) -> Acc;
find_candidates([Char | T], S, First, Last, Acc) ->
    L = maps:get(Char, First),
    case expand_range(L, maps:get(Char, Last), L, S, First, Last) of
        {ok, R} -> find_candidates(T, S, First, Last, [{L, R} | Acc]);
        fail -> find_candidates(T, S, First, Last, Acc)
    end.

expand_range(J, R, L, S, First, Last) when J =< R ->
    C = binary:at(S, J),
    CFirst = maps:get(C, First),
    CLast = maps:get(C, Last),
    if CFirst < L -> fail;
       true -> expand_range(J + 1, erlang:max(R, CLast), L, S, First, Last)
    end;
expand_range(_, R, _, _, _, _) -> {ok, R}.

pick_substrings([], _, _, Acc) -> lists:reverse(Acc);
pick_substrings([{L, R} | T], LastEnd, S, Acc) ->
    if L > LastEnd ->
        Sub = binary_part(S, L, R - L + 1),
        pick_substrings(T, R, S, [Sub | Acc]);
       true ->
        pick_substrings(T, LastEnd, S, Acc)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_num_of_substrings(s :: String.t()) :: [String.t()]
  def max_num_of_substrings(s) do
    n = byte_size(s)
    first = find_first(s, 0, n, %{})
    last = find_last(s, 0, n, %{})

    chars = Map.keys(first)
    candidates = find_candidates(chars, s, first, last, [])
    sorted = Enum.sort(candidates, fn {l1, r1}, {l2, r2} ->
      if r1 == r2, do: l1 > l2, else: r1 < r2
    end)

    pick_substrings(sorted, -1, s, [])
  end

  defp find_first(s, i, n, map) when i < n do
    char = :binary.at(s, i)
    new_map = if Map.has_key?(map, char), do: map, else: Map.put(map, char, i)
    find_first(s, i + 1, n, new_map)
  end
  defp find_first(_, _, _, map), do: map

  defp find_last(s, i, n, map) when i < n do
    char = :binary.at(s, i)
    find_last(s, i + 1, n, Map.put(map, char, i))
  end
  defp find_last(_, _, _, map), do: map

  defp find_candidates([], _, _, _, acc), do: acc
  defp find_candidates([char | t], s, first, last, acc) do
    l = Map.get(first, char)
    case expand_range(l, Map.get(last, char), l, s, first, last) do
      {:ok, r} -> find_candidates(t, s, first, last, [{l, r} | acc])
      :fail -> find_candidates(t, s, first, last, acc)
    end
  end

  defp expand_range(j, r, l, s, first, last) when j <= r do
    c = :binary.at(s, j)
    c_first = Map.get(first, c)
    c_last = Map.get(last, c)
    if c_first < l do
      :fail
    else
      expand_range(j + 1, max(r, c_last), l, s, first, last)
    end
  end
  defp expand_range(_j, r, _l, _s, _first, _last), do: {:ok, r}

  defp pick_substrings([], _last_end, _s, acc), do: Enum.reverse(acc)
  defp pick_substrings([{l, r} | t], last_end, s, acc) do
    if l > last_end do
      sub = binary_part(s, l, r - l + 1)
      pick_substrings(t, r, s, [sub | acc])
    else
      pick_substrings(t, last_end, s, acc)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N \cdot \Sigma) where N is the length of the string and $\Sigma$ is the size of the character set (26). We spend O(N) to find the first and last occurrences. For each of the 26 characters, we may scan up to O(N) characters during the expansion phase, leading to $O(26N)$. Sorting and greedy selection are $O(\Sigma \log \Sigma)$ and $O(\Sigma)$, respectively.
- **Space Complexity:** O(N) to store the input string and the resulting substrings. The metadata for characters (first/last indices) and the list of candidate intervals require $O(\Sigma)$ space, which is constant.
