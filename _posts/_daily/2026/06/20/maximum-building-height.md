---
layout: post
title: "Maximum Building Height"
date: 2026-06-20 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Math", "Sorting"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/maximum-building-height/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxBuilding(int n, vector<vector<int>>&\
        \ restrictions) {\n        vector<vector<int>> res = restrictions;\n       \
        \ res.push_back({1, 0});\n        sort(res.begin(), res.end());\n\n        int\
        \ m = res.size();\n        for (int i = 1; i < m; ++i) {\n            res[i][1]\
        \ = (int)min((long long)res[i][1], (long long)res[i - 1][1] + res[i][0] - res[i\
        \ - 1][0]);\n        }\n        for (int i = m - 2; i >= 0; --i) {\n       \
        \     res[i][1] = (int)min((long long)res[i][1], (long long)res[i + 1][1] +\
        \ res[i + 1][0] - res[i][0]);\n        }\n\n        int ans = 0;\n        for\
        \ (int i = 0; i < m - 1; ++i) {\n            int id1 = res[i][0], h1 = res[i][1];\n\
        \            int id2 = res[i + 1][0], h2 = res[i + 1][1];\n            int peak\
        \ = (int)(((long long)id2 - id1 + h1 + h2) / 2);\n            ans = max(ans,\
        \ peak);\n        }\n\n        ans = max(ans, (int)((long long)res[m - 1][1]\
        \ + n - res[m - 1][0]));\n        return ans;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public int maxBuilding(int\
        \ n, int[][] restrictions) {\n        int m = restrictions.length;\n       \
        \ int[][] res = new int[m + 1][2];\n        for (int i = 0; i < m; i++) {\n\
        \            res[i][0] = restrictions[i][0];\n            res[i][1] = restrictions[i][1];\n\
        \        }\n        res[m][0] = 1;\n        res[m][1] = 0;\n\n        Arrays.sort(res,\
        \ (a, b) -> Integer.compare(a[0], b[0]));\n\n        int total = m + 1;\n  \
        \      for (int i = 1; i < total; i++) {\n            res[i][1] = (int) Math.min((long)\
        \ res[i][1], (long) res[i - 1][1] + res[i][0] - res[i - 1][0]);\n        }\n\
        \        for (int i = total - 2; i >= 0; i--) {\n            res[i][1] = (int)\
        \ Math.min((long) res[i][1], (long) res[i + 1][1] + res[i + 1][0] - res[i][0]);\n\
        \        }\n\n        int ans = 0;\n        for (int i = 0; i < total - 1; i++)\
        \ {\n            int id1 = res[i][0], h1 = res[i][1];\n            int id2 =\
        \ res[i + 1][0], h2 = res[i + 1][1];\n            int peak = (int) (((long)\
        \ id2 - id1 + h1 + h2) / 2);\n            ans = Math.max(ans, peak);\n     \
        \   }\n\n        ans = Math.max(ans, (int) ((long) res[total - 1][1] + n - res[total\
        \ - 1][0]));\n        return ans;\n    }\n}"
      python: "class Solution(object):\n    def maxBuilding(self, n, restrictions):\n\
        \        \"\"\"\n        :type n: int\n        :type restrictions: List[List[int]]\n\
        \        :rtype: int\n        \"\"\"\n        res = [list(r) for r in restrictions]\n\
        \        res.append([1, 0])\n        res.sort()\n\n        m = len(res)\n  \
        \      for i in range(1, m):\n            res[i][1] = min(res[i][1], res[i -\
        \ 1][1] + res[i][0] - res[i - 1][0])\n\n        for i in range(m - 2, -1, -1):\n\
        \            res[i][1] = min(res[i][1], res[i + 1][1] + res[i + 1][0] - res[i][0])\n\
        \n        max_h = 0\n        for i in range(m - 1):\n            id1, h1 = res[i]\n\
        \            id2, h2 = res[i + 1]\n            peak = (id2 - id1 + h1 + h2)\
        \ // 2\n            max_h = max(max_h, peak)\n\n        max_h = max(max_h, res[m\
        \ - 1][1] + n - res[m - 1][0])\n        return max_h"
      python3: "class Solution:\n    def maxBuilding(self, n: int, restrictions: List[List[int]])\
        \ -> int:\n        res = restrictions + [[1, 0]]\n        res.sort()\n\n   \
        \     m = len(res)\n        for i in range(1, m):\n            res[i][1] = min(res[i][1],\
        \ res[i-1][1] + res[i][0] - res[i-1][0])\n\n        for i in range(m - 2, -1,\
        \ -1):\n            res[i][1] = min(res[i][1], res[i+1][1] + res[i+1][0] - res[i][0])\n\
        \n        max_h = 0\n        for i in range(m - 1):\n            h1, id1 = res[i][1],\
        \ res[i][0]\n            h2, id2 = res[i+1][1], res[i+1][0]\n            max_h\
        \ = max(max_h, (h1 + h2 + id2 - id1) // 2)\n\n        max_h = max(max_h, res[-1][1]\
        \ + n - res[-1][0])\n\n        return int(max_h)"
      c: "#include <stdlib.h>\n#include <math.h>\n\ntypedef struct {\n    int id;\n\
        \    int h;\n} Building;\n\nint compare(const void* a, const void* b) {\n  \
        \  const Building* b1 = (const Building*)a;\n    const Building* b2 = (const\
        \ Building*)b;\n    if (b1->id < b2->id) return -1;\n    if (b1->id > b2->id)\
        \ return 1;\n    return 0;\n}\n\nint maxBuilding(int n, int** restrictions,\
        \ int restrictionsSize, int* restrictionsColSize) {\n    int m = restrictionsSize\
        \ + 1;\n    Building* b = (Building*)malloc(m * sizeof(Building));\n    for\
        \ (int i = 0; i < restrictionsSize; i++) {\n        b[i].id = restrictions[i][0];\n\
        \        b[i].h = restrictions[i][1];\n    }\n    b[restrictionsSize].id = 1;\n\
        \    b[restrictionsSize].h = 0;\n\n    qsort(b, m, sizeof(Building), compare);\n\
        \n    for (int i = 1; i < m; i++) {\n        int diff = b[i].id - b[i-1].id;\n\
        \        if (b[i].h > b[i-1].h + diff) {\n            b[i].h = b[i-1].h + diff;\n\
        \        }\n    }\n\n    for (int i = m - 2; i >= 0; i--) {\n        int diff\
        \ = b[i+1].id - b[i].id;\n        if (b[i].h > b[i+1].h + diff) {\n        \
        \    b[i].h = b[i+1].h + diff;\n        }\n    }\n\n    long long max_h = 0;\n\
        \    for (int i = 0; i < m - 1; i++) {\n        long long h1 = b[i].h;\n   \
        \     long long h2 = b[i+1].h;\n        long long id1 = b[i].id;\n        long\
        \ long id2 = b[i+1].id;\n        long long peak = (h1 + h2 + id2 - id1) / 2;\n\
        \        if (peak > max_h) max_h = peak;\n    }\n    long long last_peak = (long\
        \ long)b[m-1].h + (n - b[m-1].id);\n    if (last_peak > max_h) max_h = last_peak;\n\
        \n    free(b);\n    return (int)max_h;\n}"
      csharp: "using System;\n\npublic class Solution {\n    public int MaxBuilding(int\
        \ n, int[][] restrictions) {\n        int m = restrictions.Length;\n       \
        \ int[][] res = new int[m + 1][];\n        for (int i = 0; i < m; i++) {\n \
        \           res[i] = new int[] { restrictions[i][0], restrictions[i][1] };\n\
        \        }\n        res[m] = new int[] { 1, 0 };\n\n        Array.Sort(res,\
        \ (a, b) => a[0].CompareTo(b[0]));\n\n        int len = res.Length;\n      \
        \  for (int i = 1; i < len; i++) {\n            res[i][1] = Math.Min(res[i][1],\
        \ res[i - 1][1] + (res[i][0] - res[i - 1][0]));\n        }\n\n        for (int\
        \ i = len - 2; i >= 0; i--) {\n            res[i][1] = Math.Min(res[i][1], res[i\
        \ + 1][1] + (res[i + 1][0] - res[i][0]));\n        }\n\n        long maxH =\
        \ 0;\n        for (int i = 0; i < len - 1; i++) {\n            long h1 = res[i][1];\n\
        \            long h2 = res[i + 1][1];\n            long id1 = res[i][0];\n \
        \           long id2 = res[i + 1][0];\n            long peak = (h1 + h2 + id2\
        \ - id1) / 2;\n            if (peak > maxH) {\n                maxH = peak;\n\
        \            }\n        }\n\n        long lastPeak = (long)res[len - 1][1] +\
        \ (n - res[len - 1][0]);\n        if (lastPeak > maxH) {\n            maxH =\
        \ lastPeak;\n        }\n\n        return (int)maxH;\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @param {number[][]} restrictions\n\
        \ * @return {number}\n */\nvar maxBuilding = function(n, restrictions) {\n \
        \   let res = [...restrictions, [1, 0]];\n    res.sort((a, b) => a[0] - b[0]);\n\
        \n    const m = res.length;\n    for (let i = 1; i < m; i++) {\n        res[i][1]\
        \ = Math.min(res[i][1], res[i - 1][1] + res[i][0] - res[i - 1][0]);\n    }\n\
        \n    for (let i = m - 2; i >= 0; i--) {\n        res[i][1] = Math.min(res[i][1],\
        \ res[i + 1][1] + res[i + 1][0] - res[i][0]);\n    }\n\n    let maxH = 0;\n\
        \    for (let i = 0; i < m - 1; i++) {\n        let h1 = res[i][1], id1 = res[i][0];\n\
        \        let h2 = res[i + 1][1], id2 = res[i + 1][0];\n        maxH = Math.max(maxH,\
        \ Math.floor((h1 + h2 + id2 - id1) / 2));\n    }\n\n    maxH = Math.max(maxH,\
        \ res[m - 1][1] + n - res[m - 1][0]);\n\n    return maxH;\n};"
      typescript: "function maxBuilding(n: number, restrictions: number[][]): number\
        \ {\n    const res = [...restrictions, [1, 0]];\n    res.sort((a, b) => a[0]\
        \ - b[0]);\n    const m = res.length;\n\n    for (let i = 1; i < m; i++) {\n\
        \        res[i][1] = Math.min(res[i][1], res[i - 1][1] + (res[i][0] - res[i\
        \ - 1][0]));\n    }\n\n    for (let i = m - 2; i >= 0; i--) {\n        res[i][1]\
        \ = Math.min(res[i][1], res[i + 1][1] + (res[i + 1][0] - res[i][0]));\n    }\n\
        \n    let maxH = 0;\n    for (let i = 0; i < m - 1; i++) {\n        const h1\
        \ = res[i][1];\n        const h2 = res[i + 1][1];\n        const d = res[i +\
        \ 1][0] - res[i][0];\n        maxH = Math.max(maxH, Math.floor((h1 + h2 + d)\
        \ / 2));\n    }\n    maxH = Math.max(maxH, res[m - 1][1] + (n - res[m - 1][0]));\n\
        \    return maxH;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @param Integer[][]\
        \ $restrictions\n     * @return Integer\n     */\n    function maxBuilding($n,\
        \ $restrictions) {\n        $restrictions[] = [1, 0];\n        usort($restrictions,\
        \ function($a, $b) {\n            return $a[0] <=> $b[0];\n        });\n\n \
        \       $m = count($restrictions);\n        for ($i = 1; $i < $m; $i++) {\n\
        \            $restrictions[$i][1] = min($restrictions[$i][1], $restrictions[$i\
        \ - 1][1] + ($restrictions[$i][0] - $restrictions[$i - 1][0]));\n        }\n\
        \n        for ($i = $m - 2; $i >= 0; $i--) {\n            $restrictions[$i][1]\
        \ = min($restrictions[$i][1], $restrictions[$i + 1][1] + ($restrictions[$i +\
        \ 1][0] - $restrictions[$i][0]));\n        }\n\n        $maxH = 0;\n       \
        \ for ($i = 0; $i < $m - 1; $i++) {\n            $h1 = $restrictions[$i][1];\n\
        \            $h2 = $restrictions[$i + 1][1];\n            $d = $restrictions[$i\
        \ + 1][0] - $restrictions[$i][0];\n            $maxH = max($maxH, (int)(($h1\
        \ + $h2 + $d) / 2));\n        }\n        $maxH = max($maxH, $restrictions[$m\
        \ - 1][1] + ($n - $restrictions[$m - 1][0]));\n\n        return (int)$maxH;\n\
        \    }\n}"
      swift: "class Solution {\n    func maxBuilding(_ n: Int, _ restrictions: [[Int]])\
        \ -> Int {\n        var res = restrictions\n        res.append([1, 0])\n   \
        \     res.sort { $0[0] < $1[0] }\n\n        let m = res.count\n        for i\
        \ in 1..<m {\n            res[i][1] = min(res[i][1], res[i - 1][1] + (res[i][0]\
        \ - res[i - 1][0]))\n        }\n\n        for i in (0..<m - 1).reversed() {\n\
        \            res[i][1] = min(res[i][1], res[i + 1][1] + (res[i + 1][0] - res[i][0]))\n\
        \        }\n\n        var maxH = 0\n        for i in 0..<m - 1 {\n         \
        \   let h1 = res[i][1]\n            let h2 = res[i + 1][1]\n            let\
        \ d = res[i + 1][0] - res[i][0]\n            maxH = max(maxH, (h1 + h2 + d)\
        \ / 2)\n        }\n        maxH = max(maxH, res[m - 1][1] + (n - res[m - 1][0]))\n\
        \n        return maxH\n    }\n}"
      kotlin: "class Solution {\n    fun maxBuilding(n: Int, restrictions: Array<IntArray>):\
        \ Int {\n        val mOrig = restrictions.size\n        val res = Array(mOrig\
        \ + 1) { IntArray(2) }\n        for (i in 0 until mOrig) {\n            res[i][0]\
        \ = restrictions[i][0]\n            res[i][1] = restrictions[i][1]\n       \
        \ }\n        res[mOrig][0] = 1\n        res[mOrig][1] = 0\n        res.sortBy\
        \ { it[0] }\n\n        val m = res.size\n        for (i in 1 until m) {\n  \
        \          res[i][1] = minOf(res[i][1].toLong(), res[i - 1][1].toLong() + (res[i][0]\
        \ - res[i - 1][0])).toInt()\n        }\n\n        for (i in m - 2 downTo 0)\
        \ {\n            res[i][1] = minOf(res[i][1].toLong(), res[i + 1][1].toLong()\
        \ + (res[i + 1][0] - res[i][0])).toInt()\n        }\n\n        var maxH = 0L\n\
        \        for (i in 0 until m - 1) {\n            val h1 = res[i][1].toLong()\n\
        \            val h2 = res[i + 1][1].toLong()\n            val d = (res[i + 1][0]\
        \ - res[i][0]).toLong()\n            maxH = maxOf(maxH, (h1 + h2 + d) / 2)\n\
        \        }\n        maxH = maxOf(maxH, res[m - 1][1].toLong() + (n - res[m -\
        \ 1][0]))\n\n        return maxH.toInt()\n    }\n}"
      dart: "class Solution {\n  int maxBuilding(int n, List<List<int>> restrictions)\
        \ {\n    List<List<int>> r = restrictions.map((e) => List<int>.from(e)).toList();\n\
        \    r.add([1, 0]);\n    r.sort((a, b) => a[0].compareTo(b[0]));\n\n    if (r.last[0]\
        \ != n) {\n      r.add([n, n - 1]);\n    }\n\n    int m = r.length;\n    for\
        \ (int i = 1; i < m; i++) {\n      int dist = r[i][0] - r[i - 1][0];\n     \
        \ if (r[i][1] > r[i - 1][1] + dist) {\n        r[i][1] = r[i - 1][1] + dist;\n\
        \      }\n    }\n\n    for (int i = m - 2; i >= 0; i--) {\n      int dist =\
        \ r[i + 1][0] - r[i][0];\n      if (r[i][1] > r[i + 1][1] + dist) {\n      \
        \  r[i][1] = r[i + 1][1] + dist;\n      }\n    }\n\n    int maxH = 0;\n    for\
        \ (int i = 0; i < m - 1; i++) {\n      int id1 = r[i][0], h1 = r[i][1];\n  \
        \    int id2 = r[i + 1][0], h2 = r[i + 1][1];\n      int peak = (h1 + h2 + id2\
        \ - id1) ~/ 2;\n      if (peak > maxH) {\n        maxH = peak;\n      }\n  \
        \  }\n    return maxH;\n  }\n}"
      go: "import \"sort\"\n\nfunc maxBuilding(n int, restrictions [][]int) int {\n\t\
        r := make([][]int, len(restrictions))\n\tfor i := range restrictions {\n\t\t\
        r[i] = []int{restrictions[i][0], restrictions[i][1]}\n\t}\n\tr = append(r, []int{1,\
        \ 0})\n\tsort.Slice(r, func(i, j int) bool {\n\t\treturn r[i][0] < r[j][0]\n\
        \t})\n\tif r[len(r)-1][0] != n {\n\t\tr = append(r, []int{n, n - 1})\n\t}\n\n\
        \tm := len(r)\n\tfor i := 1; i < m; i++ {\n\t\tdist := r[i][0] - r[i-1][0]\n\
        \t\tif r[i][1] > r[i-1][1]+dist {\n\t\t\tr[i][1] = r[i-1][1] + dist\n\t\t}\n\
        \t}\n\n\tfor i := m - 2; i >= 0; i-- {\n\t\tdist := r[i+1][0] - r[i][0]\n\t\t\
        if r[i][1] > r[i+1][1]+dist {\n\t\t\tr[i][1] = r[i+1][1] + dist\n\t\t}\n\t}\n\
        \n\tmaxH := 0\n\tfor i := 0; i < m-1; i++ {\n\t\tid1, h1 := r[i][0], r[i][1]\n\
        \t\tid2, h2 := r[i+1][0], r[i+1][1]\n\t\tpeak := (h1 + h2 + id2 - id1) / 2\n\
        \t\tif peak > maxH {\n\t\t\tmaxH = peak\n\t\t}\n\t}\n\treturn maxH\n}"
      ruby: "# @param {Integer} n\n# @param {Integer[][]} restrictions\n# @return {Integer}\n\
        def max_building(n, restrictions)\n  r = restrictions.map(&:dup)\n  r << [1,\
        \ 0]\n  r.sort_by! { |x| x[0] }\n  if r.last[0] != n\n    r << [n, n - 1]\n\
        \  end\n\n  m = r.length\n  (1...m).each do |i|\n    dist = r[i][0] - r[i -\
        \ 1][0]\n    r[i][1] = [r[i][1], r[i - 1][1] + dist].min\n  end\n\n  (m - 2).downto(0).each\
        \ do |i|\n    dist = r[i + 1][0] - r[i][0]\n    r[i][1] = [r[i][1], r[i + 1][1]\
        \ + dist].min\n  end\n\n  max_h = 0\n  (0...m - 1).each do |i|\n    id1, h1\
        \ = r[i]\n    id2, h2 = r[i + 1]\n    peak = (h1 + h2 + id2 - id1) / 2\n   \
        \ max_h = peak if peak > max_h\n  end\n  max_h\nend"
      scala: "object Solution {\n    def maxBuilding(n: Int, restrictions: Array[Array[Int]]):\
        \ Int = {\n        val r = (restrictions.map(_.clone) :+ Array(1, 0)).sortBy(_(0))\n\
        \        val finalR = if (r.last(0) != n) r :+ Array(n, n - 1) else r\n    \
        \    val m = finalR.length\n\n        for (i <- 1 until m) {\n            val\
        \ dist = finalR(i)(0) - finalR(i - 1)(0)\n            finalR(i)(1) = math.min(finalR(i)(1),\
        \ finalR(i - 1)(1) + dist)\n        }\n\n        for (i <- m - 2 to 0 by -1)\
        \ {\n            val dist = finalR(i + 1)(0) - finalR(i)(0)\n            finalR(i)(1)\
        \ = math.min(finalR(i)(1), finalR(i + 1)(1) + dist)\n        }\n\n        var\
        \ maxH = 0L\n        for (i <- 0 until m - 1) {\n            val id1 = finalR(i)(0).toLong\n\
        \            val h1 = finalR(i)(1).toLong\n            val id2 = finalR(i +\
        \ 1)(0).toLong\n            val h2 = finalR(i + 1)(1).toLong\n            val\
        \ peak = (h1 + h2 + id2 - id1) / 2\n            if (peak > maxH) maxH = peak\n\
        \        }\n        maxH.toInt\n    }\n}"
      rust: "impl Solution {\n    pub fn max_building(n: i32, restrictions: Vec<Vec<i32>>)\
        \ -> i32 {\n        let mut r = restrictions;\n        r.push(vec![1, 0]);\n\
        \        r.sort_unstable();\n\n        let m = r.len();\n        for i in 1..m\
        \ {\n            let id_diff = r[i][0] - r[i - 1][0];\n            r[i][1] =\
        \ r[i][1].min(r[i - 1][1] + id_diff);\n        }\n        for i in (0..m - 1).rev()\
        \ {\n            let id_diff = r[i + 1][0] - r[i][0];\n            r[i][1] =\
        \ r[i][1].min(r[i + 1][1] + id_diff);\n        }\n\n        let mut max_h =\
        \ 0i64;\n        for i in 0..m - 1 {\n            let id1 = r[i][0] as i64;\n\
        \            let h1 = r[i][1] as i64;\n            let id2 = r[i + 1][0] as\
        \ i64;\n            let h2 = r[i + 1][1] as i64;\n            let peak = (h1\
        \ + h2 + id2 - id1) / 2;\n            if peak > max_h {\n                max_h\
        \ = peak;\n            }\n        }\n\n        let last_id = r[m - 1][0] as\
        \ i64;\n        let last_h = r[m - 1][1] as i64;\n        let result = max_h.max(last_h\
        \ + (n as i64 - last_id));\n\n        result as i32\n    }\n}"
      racket: "(define/contract (max-building n restrictions)\n  (-> exact-integer?\
        \ (listof (listof exact-integer?)) exact-integer?)\n  (let* ([rs (sort (cons\
        \ (list 1 0) restrictions) < #:key car)]\n         [pass-l-to-r (lambda (lst)\n\
        \                        (if (null? lst)\n                            '()\n\
        \                            (let loop ([curr (car lst)] [rest (cdr lst)] [acc\
        \ (list (car lst))])\n                              (if (null? rest)\n     \
        \                             (reverse acc)\n                              \
        \    (let* ([next (car rest)]\n                                         [id1\
        \ (car curr)]\n                                         [h1 (cadr curr)]\n \
        \                                        [id2 (car next)]\n                \
        \                         [h2 (cadr next)]\n                               \
        \          [nh2 (min h2 (+ h1 (- id2 id1)))]\n                             \
        \            [ncurr (list id2 nh2)])\n                                    (loop\
        \ ncurr (cdr rest) (cons ncurr acc)))))))]\n         [pass-r-to-l (lambda (lst)\n\
        \                        (if (null? lst)\n                            '()\n\
        \                            (let loop ([curr (car lst)] [rest (cdr lst)] [acc\
        \ (list (car lst))])\n                              (if (null? rest)\n     \
        \                             acc\n                                  (let* ([next\
        \ (car rest)]\n                                         [id2 (car curr)]\n \
        \                                        [h2 (cadr curr)]\n                \
        \                         [id1 (car next)]\n                               \
        \          [h1 (cadr next)]\n                                         [nh1 (min\
        \ h1 (+ h2 (- id2 id1)))]\n                                         [nnext (list\
        \ id1 nh1)])\n                                    (loop nnext (cdr rest) (cons\
        \ nnext acc)))))))]\n         [rs-l (pass-l-to-r rs)]\n         [rs-final (pass-r-to-l\
        \ (reverse rs-l))]\n         [peaks (if (or (null? rs-final) (null? (cdr rs-final)))\n\
        \                    '()\n                    (map (lambda (r1 r2)\n       \
        \                    (quotient (+ (cadr r1) (cadr r2) (- (car r2) (car r1)))\
        \ 2))\n                         rs-final (cdr rs-final)))]\n         [m1 (if\
        \ (null? peaks) 0 (apply max peaks))]\n         [last-r (car (reverse rs-final))]\n\
        \         [m2 (+ (cadr last-r) (- n (car last-r)))])\n    (max m1 m2)))"
      erlang: "-spec max_building(N :: integer(), Restrictions :: [[integer()]]) ->\
        \ integer().\nmax_building(N, Restrictions) ->\n    Sorted = lists:sort([[1,\
        \ 0] | Restrictions]),\n    LtoR = pass_l_to_r(Sorted),\n    RtoL = pass_r_to_l(lists:reverse(LtoR)),\n\
        \    M1 = find_max_peaks(RtoL, 0),\n    [LastId, LastH] = lists:last(RtoL),\n\
        \    M2 = LastH + (N - LastId),\n    erlang:max(M1, M2).\n\npass_l_to_r([H |\
        \ T]) ->\n    pass_l_to_r(T, [H]).\npass_l_to_r([], Acc) ->\n    lists:reverse(Acc);\n\
        pass_l_to_r([[Id2, H2] | T], [[Id1, H1] | _] = Acc) ->\n    NH2 = erlang:min(H2,\
        \ H1 + (Id2 - Id1)),\n    pass_l_to_r(T, [[Id2, NH2] | Acc]).\n\npass_r_to_l([H\
        \ | T]) ->\n    pass_r_to_l(T, [H]).\npass_r_to_l([], Acc) ->\n    Acc;\npass_r_to_l([[Id1,\
        \ H1] | T], [[Id2, H2] | _] = Acc) ->\n    NH1 = erlang:min(H1, H2 + (Id2 -\
        \ Id1)),\n    pass_r_to_l(T, [[Id1, NH1] | Acc]).\n\nfind_max_peaks([_], Max)\
        \ -> Max;\nfind_max_peaks([[Id1, H1], [Id2, H2] | T], Max) ->\n    Peak = (H1\
        \ + H2 + Id2 - Id1) div 2,\n    find_max_peaks([[Id2, H2] | T], erlang:max(Max,\
        \ Peak))."
      elixir: "defmodule Solution do\n  @spec max_building(n :: integer, restrictions\
        \ :: [[integer]]) :: integer\n  def max_building(n, restrictions) do\n    rs\
        \ = [[1, 0] | restrictions] |> Enum.sort()\n\n    rs = Enum.reduce(tl(rs), [hd(rs)],\
        \ fn [id2, h2], acc ->\n      [id1, h1] = hd(acc)\n      nh2 = min(h2, h1 +\
        \ (id2 - id1))\n      [[id2, nh2] | acc]\n    end) |> Enum.reverse()\n\n   \
        \ rs = Enum.reduce(tl(Enum.reverse(rs)), [hd(Enum.reverse(rs))], fn [id1, h1],\
        \ acc ->\n      [id2, h2] = hd(acc)\n      nh1 = min(h1, h2 + (id2 - id1))\n\
        \      [[id1, nh1] | acc]\n    end)\n\n    m1 = compute_peaks(rs, 0)\n    [last_id,\
        \ last_h] = List.last(rs)\n    m2 = last_h + (n - last_id)\n    max(m1, m2)\n\
        \  end\n\n  defp compute_peaks([_], max_p), do: max_p\n  defp compute_peaks([[id1,\
        \ h1], [id2, h2] | tail], max_p) do\n    peak = div(h1 + h2 + id2 - id1, 2)\n\
        \    compute_peaks([[id2, h2] | tail], max(max_p, peak))\n  end\nend"
    approach: 'The problem can be solved by viewing each restriction as a set of upper
      bounds that propagate across buildings. Since the height difference between any
      two adjacent buildings is at most 1, a restriction $(id, h)$ implies that for
      any other building $j$, its height $h_j$ cannot exceed $h + |id - j|$. To find
      the tightest possible upper bound for each restricted building, we must also consider
      the constraint that building 1 has height 0. We start by adding building 1 as
      a restriction with height 0 and sorting all restrictions by their building indices.
      Then, we perform two passes: a left-to-right pass ensures each building''s height
      is consistent with the preceding restricted building, and a right-to-left pass
      ensures consistency with the subsequent restricted building.'
    time_complexity: O(M log M) where M is the number of restrictions. This complexity
      is dominated by the sorting step. The subsequent left-to-right and right-to-left
      passes, as well as the final peak calculation, all take O(M) time.
    space_complexity: O(M) to store the copy of the restrictions. We allocate an auxiliary
      list or vector of size M+1 to facilitate the sorting and propagation steps.
    elapsed_time: 439.7530839443207
    model: gemini-3-flash-preview
    generated_at: '2026-06-20 02:47:37 '
---

## Problem #1840: Maximum Building Height

**Difficulty:** Hard

**Topics:** Array, Math, Sorting

## Problem Description

<p>You want to build <code>n</code> new buildings in a city. The new buildings will be built in a line and are labeled from <code>1</code> to <code>n</code>.</p>

<p>However, there are city restrictions on the heights of the new buildings:</p>

<ul>
	<li>The height of each building must be a non-negative integer.</li>
	<li>The height of the first building <strong>must</strong> be <code>0</code>.</li>
	<li>The height difference between any two adjacent buildings <strong>cannot exceed</strong> <code>1</code>.</li>
</ul>

<p>Additionally, there are city restrictions on the maximum height of specific buildings. These restrictions are given as a 2D integer array <code>restrictions</code> where <code>restrictions[i] = [id<sub>i</sub>, maxHeight<sub>i</sub>]</code> indicates that building <code>id<sub>i</sub></code> must have a height <strong>less than or equal to</strong> <code>maxHeight<sub>i</sub></code>.</p>

<p>It is guaranteed that each building will appear <strong>at most once</strong> in <code>restrictions</code>, and building <code>1</code> will <strong>not</strong> be in <code>restrictions</code>.</p>

<p>Return <em>the <strong>maximum possible height</strong> of the <strong>tallest</strong> building</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/ic236-q4-ex1-1.png" style="width: 400px; height: 253px;" />
<pre>
<strong>Input:</strong> n = 5, restrictions = [[2,1],[4,1]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The green area in the image indicates the maximum allowed height for each building.
We can build the buildings with heights [0,1,2,1,2], and the tallest building has a height of 2.</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/ic236-q4-ex2.png" style="width: 500px; height: 269px;" />
<pre>
<strong>Input:</strong> n = 6, restrictions = []
<strong>Output:</strong> 5
<strong>Explanation:</strong> The green area in the image indicates the maximum allowed height for each building.
We can build the buildings with heights [0,1,2,3,4,5], and the tallest building has a height of 5.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/ic236-q4-ex3.png" style="width: 500px; height: 187px;" />
<pre>
<strong>Input:</strong> n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]]
<strong>Output:</strong> 5
<strong>Explanation:</strong> The green area in the image indicates the maximum allowed height for each building.
We can build the buildings with heights [0,1,2,3,3,4,4,5,4,3], and the tallest building has a height of 5.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= restrictions.length &lt;= min(n - 1, 10<sup>5</sup>)</code></li>
	<li><code>2 &lt;= id<sub>i</sub> &lt;= n</code></li>
	<li><code>id<sub>i</sub></code>&nbsp;is <strong>unique</strong>.</li>
	<li><code>0 &lt;= maxHeight<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. Is it possible to find the max height if given the height range of a particular building?

2. You can find the height range of a restricted building by doing 2 passes from the left and right.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be solved by viewing each restriction as a set of upper bounds that propagate across buildings. Since the height difference between any two adjacent buildings is at most 1, a restriction $(id, h)$ implies that for any other building $j$, its height $h_j$ cannot exceed $h + |id - j|$. To find the tightest possible upper bound for each restricted building, we must also consider the constraint that building 1 has height 0. We start by adding building 1 as a restriction with height 0 and sorting all restrictions by their building indices. Then, we perform two passes: a left-to-right pass ensures each building's height is consistent with the preceding restricted building, and a right-to-left pass ensures consistency with the subsequent restricted building.

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
    int maxBuilding(int n, vector<vector<int>>& restrictions) {
        vector<vector<int>> res = restrictions;
        res.push_back({1, 0});
        sort(res.begin(), res.end());

        int m = res.size();
        for (int i = 1; i < m; ++i) {
            res[i][1] = (int)min((long long)res[i][1], (long long)res[i - 1][1] + res[i][0] - res[i - 1][0]);
        }
        for (int i = m - 2; i >= 0; --i) {
            res[i][1] = (int)min((long long)res[i][1], (long long)res[i + 1][1] + res[i + 1][0] - res[i][0]);
        }

        int ans = 0;
        for (int i = 0; i < m - 1; ++i) {
            int id1 = res[i][0], h1 = res[i][1];
            int id2 = res[i + 1][0], h2 = res[i + 1][1];
            int peak = (int)(((long long)id2 - id1 + h1 + h2) / 2);
            ans = max(ans, peak);
        }

        ans = max(ans, (int)((long long)res[m - 1][1] + n - res[m - 1][0]));
        return ans;
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
    public int maxBuilding(int n, int[][] restrictions) {
        int m = restrictions.length;
        int[][] res = new int[m + 1][2];
        for (int i = 0; i < m; i++) {
            res[i][0] = restrictions[i][0];
            res[i][1] = restrictions[i][1];
        }
        res[m][0] = 1;
        res[m][1] = 0;

        Arrays.sort(res, (a, b) -> Integer.compare(a[0], b[0]));

        int total = m + 1;
        for (int i = 1; i < total; i++) {
            res[i][1] = (int) Math.min((long) res[i][1], (long) res[i - 1][1] + res[i][0] - res[i - 1][0]);
        }
        for (int i = total - 2; i >= 0; i--) {
            res[i][1] = (int) Math.min((long) res[i][1], (long) res[i + 1][1] + res[i + 1][0] - res[i][0]);
        }

        int ans = 0;
        for (int i = 0; i < total - 1; i++) {
            int id1 = res[i][0], h1 = res[i][1];
            int id2 = res[i + 1][0], h2 = res[i + 1][1];
            int peak = (int) (((long) id2 - id1 + h1 + h2) / 2);
            ans = Math.max(ans, peak);
        }

        ans = Math.max(ans, (int) ((long) res[total - 1][1] + n - res[total - 1][0]));
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
    def maxBuilding(self, n, restrictions):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :rtype: int
        """
        res = [list(r) for r in restrictions]
        res.append([1, 0])
        res.sort()

        m = len(res)
        for i in range(1, m):
            res[i][1] = min(res[i][1], res[i - 1][1] + res[i][0] - res[i - 1][0])

        for i in range(m - 2, -1, -1):
            res[i][1] = min(res[i][1], res[i + 1][1] + res[i + 1][0] - res[i][0])

        max_h = 0
        for i in range(m - 1):
            id1, h1 = res[i]
            id2, h2 = res[i + 1]
            peak = (id2 - id1 + h1 + h2) // 2
            max_h = max(max_h, peak)

        max_h = max(max_h, res[m - 1][1] + n - res[m - 1][0])
        return max_h
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        res = restrictions + [[1, 0]]
        res.sort()

        m = len(res)
        for i in range(1, m):
            res[i][1] = min(res[i][1], res[i-1][1] + res[i][0] - res[i-1][0])

        for i in range(m - 2, -1, -1):
            res[i][1] = min(res[i][1], res[i+1][1] + res[i+1][0] - res[i][0])

        max_h = 0
        for i in range(m - 1):
            h1, id1 = res[i][1], res[i][0]
            h2, id2 = res[i+1][1], res[i+1][0]
            max_h = max(max_h, (h1 + h2 + id2 - id1) // 2)

        max_h = max(max_h, res[-1][1] + n - res[-1][0])

        return int(max_h)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <math.h>

typedef struct {
    int id;
    int h;
} Building;

int compare(const void* a, const void* b) {
    const Building* b1 = (const Building*)a;
    const Building* b2 = (const Building*)b;
    if (b1->id < b2->id) return -1;
    if (b1->id > b2->id) return 1;
    return 0;
}

int maxBuilding(int n, int** restrictions, int restrictionsSize, int* restrictionsColSize) {
    int m = restrictionsSize + 1;
    Building* b = (Building*)malloc(m * sizeof(Building));
    for (int i = 0; i < restrictionsSize; i++) {
        b[i].id = restrictions[i][0];
        b[i].h = restrictions[i][1];
    }
    b[restrictionsSize].id = 1;
    b[restrictionsSize].h = 0;

    qsort(b, m, sizeof(Building), compare);

    for (int i = 1; i < m; i++) {
        int diff = b[i].id - b[i-1].id;
        if (b[i].h > b[i-1].h + diff) {
            b[i].h = b[i-1].h + diff;
        }
    }

    for (int i = m - 2; i >= 0; i--) {
        int diff = b[i+1].id - b[i].id;
        if (b[i].h > b[i+1].h + diff) {
            b[i].h = b[i+1].h + diff;
        }
    }

    long long max_h = 0;
    for (int i = 0; i < m - 1; i++) {
        long long h1 = b[i].h;
        long long h2 = b[i+1].h;
        long long id1 = b[i].id;
        long long id2 = b[i+1].id;
        long long peak = (h1 + h2 + id2 - id1) / 2;
        if (peak > max_h) max_h = peak;
    }
    long long last_peak = (long long)b[m-1].h + (n - b[m-1].id);
    if (last_peak > max_h) max_h = last_peak;

    free(b);
    return (int)max_h;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public int MaxBuilding(int n, int[][] restrictions) {
        int m = restrictions.Length;
        int[][] res = new int[m + 1][];
        for (int i = 0; i < m; i++) {
            res[i] = new int[] { restrictions[i][0], restrictions[i][1] };
        }
        res[m] = new int[] { 1, 0 };

        Array.Sort(res, (a, b) => a[0].CompareTo(b[0]));

        int len = res.Length;
        for (int i = 1; i < len; i++) {
            res[i][1] = Math.Min(res[i][1], res[i - 1][1] + (res[i][0] - res[i - 1][0]));
        }

        for (int i = len - 2; i >= 0; i--) {
            res[i][1] = Math.Min(res[i][1], res[i + 1][1] + (res[i + 1][0] - res[i][0]));
        }

        long maxH = 0;
        for (int i = 0; i < len - 1; i++) {
            long h1 = res[i][1];
            long h2 = res[i + 1][1];
            long id1 = res[i][0];
            long id2 = res[i + 1][0];
            long peak = (h1 + h2 + id2 - id1) / 2;
            if (peak > maxH) {
                maxH = peak;
            }
        }

        long lastPeak = (long)res[len - 1][1] + (n - res[len - 1][0]);
        if (lastPeak > maxH) {
            maxH = lastPeak;
        }

        return (int)maxH;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} n
 * @param {number[][]} restrictions
 * @return {number}
 */
var maxBuilding = function(n, restrictions) {
    let res = [...restrictions, [1, 0]];
    res.sort((a, b) => a[0] - b[0]);

    const m = res.length;
    for (let i = 1; i < m; i++) {
        res[i][1] = Math.min(res[i][1], res[i - 1][1] + res[i][0] - res[i - 1][0]);
    }

    for (let i = m - 2; i >= 0; i--) {
        res[i][1] = Math.min(res[i][1], res[i + 1][1] + res[i + 1][0] - res[i][0]);
    }

    let maxH = 0;
    for (let i = 0; i < m - 1; i++) {
        let h1 = res[i][1], id1 = res[i][0];
        let h2 = res[i + 1][1], id2 = res[i + 1][0];
        maxH = Math.max(maxH, Math.floor((h1 + h2 + id2 - id1) / 2));
    }

    maxH = Math.max(maxH, res[m - 1][1] + n - res[m - 1][0]);

    return maxH;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxBuilding(n: number, restrictions: number[][]): number {
    const res = [...restrictions, [1, 0]];
    res.sort((a, b) => a[0] - b[0]);
    const m = res.length;

    for (let i = 1; i < m; i++) {
        res[i][1] = Math.min(res[i][1], res[i - 1][1] + (res[i][0] - res[i - 1][0]));
    }

    for (let i = m - 2; i >= 0; i--) {
        res[i][1] = Math.min(res[i][1], res[i + 1][1] + (res[i + 1][0] - res[i][0]));
    }

    let maxH = 0;
    for (let i = 0; i < m - 1; i++) {
        const h1 = res[i][1];
        const h2 = res[i + 1][1];
        const d = res[i + 1][0] - res[i][0];
        maxH = Math.max(maxH, Math.floor((h1 + h2 + d) / 2));
    }
    maxH = Math.max(maxH, res[m - 1][1] + (n - res[m - 1][0]));
    return maxH;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $restrictions
     * @return Integer
     */
    function maxBuilding($n, $restrictions) {
        $restrictions[] = [1, 0];
        usort($restrictions, function($a, $b) {
            return $a[0] <=> $b[0];
        });

        $m = count($restrictions);
        for ($i = 1; $i < $m; $i++) {
            $restrictions[$i][1] = min($restrictions[$i][1], $restrictions[$i - 1][1] + ($restrictions[$i][0] - $restrictions[$i - 1][0]));
        }

        for ($i = $m - 2; $i >= 0; $i--) {
            $restrictions[$i][1] = min($restrictions[$i][1], $restrictions[$i + 1][1] + ($restrictions[$i + 1][0] - $restrictions[$i][0]));
        }

        $maxH = 0;
        for ($i = 0; $i < $m - 1; $i++) {
            $h1 = $restrictions[$i][1];
            $h2 = $restrictions[$i + 1][1];
            $d = $restrictions[$i + 1][0] - $restrictions[$i][0];
            $maxH = max($maxH, (int)(($h1 + $h2 + $d) / 2));
        }
        $maxH = max($maxH, $restrictions[$m - 1][1] + ($n - $restrictions[$m - 1][0]));

        return (int)$maxH;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxBuilding(_ n: Int, _ restrictions: [[Int]]) -> Int {
        var res = restrictions
        res.append([1, 0])
        res.sort { $0[0] < $1[0] }

        let m = res.count
        for i in 1..<m {
            res[i][1] = min(res[i][1], res[i - 1][1] + (res[i][0] - res[i - 1][0]))
        }

        for i in (0..<m - 1).reversed() {
            res[i][1] = min(res[i][1], res[i + 1][1] + (res[i + 1][0] - res[i][0]))
        }

        var maxH = 0
        for i in 0..<m - 1 {
            let h1 = res[i][1]
            let h2 = res[i + 1][1]
            let d = res[i + 1][0] - res[i][0]
            maxH = max(maxH, (h1 + h2 + d) / 2)
        }
        maxH = max(maxH, res[m - 1][1] + (n - res[m - 1][0]))

        return maxH
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxBuilding(n: Int, restrictions: Array<IntArray>): Int {
        val mOrig = restrictions.size
        val res = Array(mOrig + 1) { IntArray(2) }
        for (i in 0 until mOrig) {
            res[i][0] = restrictions[i][0]
            res[i][1] = restrictions[i][1]
        }
        res[mOrig][0] = 1
        res[mOrig][1] = 0
        res.sortBy { it[0] }

        val m = res.size
        for (i in 1 until m) {
            res[i][1] = minOf(res[i][1].toLong(), res[i - 1][1].toLong() + (res[i][0] - res[i - 1][0])).toInt()
        }

        for (i in m - 2 downTo 0) {
            res[i][1] = minOf(res[i][1].toLong(), res[i + 1][1].toLong() + (res[i + 1][0] - res[i][0])).toInt()
        }

        var maxH = 0L
        for (i in 0 until m - 1) {
            val h1 = res[i][1].toLong()
            val h2 = res[i + 1][1].toLong()
            val d = (res[i + 1][0] - res[i][0]).toLong()
            maxH = maxOf(maxH, (h1 + h2 + d) / 2)
        }
        maxH = maxOf(maxH, res[m - 1][1].toLong() + (n - res[m - 1][0]))

        return maxH.toInt()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maxBuilding(int n, List<List<int>> restrictions) {
    List<List<int>> r = restrictions.map((e) => List<int>.from(e)).toList();
    r.add([1, 0]);
    r.sort((a, b) => a[0].compareTo(b[0]));

    if (r.last[0] != n) {
      r.add([n, n - 1]);
    }

    int m = r.length;
    for (int i = 1; i < m; i++) {
      int dist = r[i][0] - r[i - 1][0];
      if (r[i][1] > r[i - 1][1] + dist) {
        r[i][1] = r[i - 1][1] + dist;
      }
    }

    for (int i = m - 2; i >= 0; i--) {
      int dist = r[i + 1][0] - r[i][0];
      if (r[i][1] > r[i + 1][1] + dist) {
        r[i][1] = r[i + 1][1] + dist;
      }
    }

    int maxH = 0;
    for (int i = 0; i < m - 1; i++) {
      int id1 = r[i][0], h1 = r[i][1];
      int id2 = r[i + 1][0], h2 = r[i + 1][1];
      int peak = (h1 + h2 + id2 - id1) ~/ 2;
      if (peak > maxH) {
        maxH = peak;
      }
    }
    return maxH;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "sort"

func maxBuilding(n int, restrictions [][]int) int {
	r := make([][]int, len(restrictions))
	for i := range restrictions {
		r[i] = []int{restrictions[i][0], restrictions[i][1]}
	}
	r = append(r, []int{1, 0})
	sort.Slice(r, func(i, j int) bool {
		return r[i][0] < r[j][0]
	})
	if r[len(r)-1][0] != n {
		r = append(r, []int{n, n - 1})
	}

	m := len(r)
	for i := 1; i < m; i++ {
		dist := r[i][0] - r[i-1][0]
		if r[i][1] > r[i-1][1]+dist {
			r[i][1] = r[i-1][1] + dist
		}
	}

	for i := m - 2; i >= 0; i-- {
		dist := r[i+1][0] - r[i][0]
		if r[i][1] > r[i+1][1]+dist {
			r[i][1] = r[i+1][1] + dist
		}
	}

	maxH := 0
	for i := 0; i < m-1; i++ {
		id1, h1 := r[i][0], r[i][1]
		id2, h2 := r[i+1][0], r[i+1][1]
		peak := (h1 + h2 + id2 - id1) / 2
		if peak > maxH {
			maxH = peak
		}
	}
	return maxH
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} n
# @param {Integer[][]} restrictions
# @return {Integer}
def max_building(n, restrictions)
  r = restrictions.map(&:dup)
  r << [1, 0]
  r.sort_by! { |x| x[0] }
  if r.last[0] != n
    r << [n, n - 1]
  end

  m = r.length
  (1...m).each do |i|
    dist = r[i][0] - r[i - 1][0]
    r[i][1] = [r[i][1], r[i - 1][1] + dist].min
  end

  (m - 2).downto(0).each do |i|
    dist = r[i + 1][0] - r[i][0]
    r[i][1] = [r[i][1], r[i + 1][1] + dist].min
  end

  max_h = 0
  (0...m - 1).each do |i|
    id1, h1 = r[i]
    id2, h2 = r[i + 1]
    peak = (h1 + h2 + id2 - id1) / 2
    max_h = peak if peak > max_h
  end
  max_h
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxBuilding(n: Int, restrictions: Array[Array[Int]]): Int = {
        val r = (restrictions.map(_.clone) :+ Array(1, 0)).sortBy(_(0))
        val finalR = if (r.last(0) != n) r :+ Array(n, n - 1) else r
        val m = finalR.length

        for (i <- 1 until m) {
            val dist = finalR(i)(0) - finalR(i - 1)(0)
            finalR(i)(1) = math.min(finalR(i)(1), finalR(i - 1)(1) + dist)
        }

        for (i <- m - 2 to 0 by -1) {
            val dist = finalR(i + 1)(0) - finalR(i)(0)
            finalR(i)(1) = math.min(finalR(i)(1), finalR(i + 1)(1) + dist)
        }

        var maxH = 0L
        for (i <- 0 until m - 1) {
            val id1 = finalR(i)(0).toLong
            val h1 = finalR(i)(1).toLong
            val id2 = finalR(i + 1)(0).toLong
            val h2 = finalR(i + 1)(1).toLong
            val peak = (h1 + h2 + id2 - id1) / 2
            if (peak > maxH) maxH = peak
        }
        maxH.toInt
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_building(n: i32, restrictions: Vec<Vec<i32>>) -> i32 {
        let mut r = restrictions;
        r.push(vec![1, 0]);
        r.sort_unstable();

        let m = r.len();
        for i in 1..m {
            let id_diff = r[i][0] - r[i - 1][0];
            r[i][1] = r[i][1].min(r[i - 1][1] + id_diff);
        }
        for i in (0..m - 1).rev() {
            let id_diff = r[i + 1][0] - r[i][0];
            r[i][1] = r[i][1].min(r[i + 1][1] + id_diff);
        }

        let mut max_h = 0i64;
        for i in 0..m - 1 {
            let id1 = r[i][0] as i64;
            let h1 = r[i][1] as i64;
            let id2 = r[i + 1][0] as i64;
            let h2 = r[i + 1][1] as i64;
            let peak = (h1 + h2 + id2 - id1) / 2;
            if peak > max_h {
                max_h = peak;
            }
        }

        let last_id = r[m - 1][0] as i64;
        let last_h = r[m - 1][1] as i64;
        let result = max_h.max(last_h + (n as i64 - last_id));

        result as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (max-building n restrictions)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let* ([rs (sort (cons (list 1 0) restrictions) < #:key car)]
         [pass-l-to-r (lambda (lst)
                        (if (null? lst)
                            '()
                            (let loop ([curr (car lst)] [rest (cdr lst)] [acc (list (car lst))])
                              (if (null? rest)
                                  (reverse acc)
                                  (let* ([next (car rest)]
                                         [id1 (car curr)]
                                         [h1 (cadr curr)]
                                         [id2 (car next)]
                                         [h2 (cadr next)]
                                         [nh2 (min h2 (+ h1 (- id2 id1)))]
                                         [ncurr (list id2 nh2)])
                                    (loop ncurr (cdr rest) (cons ncurr acc)))))))]
         [pass-r-to-l (lambda (lst)
                        (if (null? lst)
                            '()
                            (let loop ([curr (car lst)] [rest (cdr lst)] [acc (list (car lst))])
                              (if (null? rest)
                                  acc
                                  (let* ([next (car rest)]
                                         [id2 (car curr)]
                                         [h2 (cadr curr)]
                                         [id1 (car next)]
                                         [h1 (cadr next)]
                                         [nh1 (min h1 (+ h2 (- id2 id1)))]
                                         [nnext (list id1 nh1)])
                                    (loop nnext (cdr rest) (cons nnext acc)))))))]
         [rs-l (pass-l-to-r rs)]
         [rs-final (pass-r-to-l (reverse rs-l))]
         [peaks (if (or (null? rs-final) (null? (cdr rs-final)))
                    '()
                    (map (lambda (r1 r2)
                           (quotient (+ (cadr r1) (cadr r2) (- (car r2) (car r1))) 2))
                         rs-final (cdr rs-final)))]
         [m1 (if (null? peaks) 0 (apply max peaks))]
         [last-r (car (reverse rs-final))]
         [m2 (+ (cadr last-r) (- n (car last-r)))])
    (max m1 m2)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_building(N :: integer(), Restrictions :: [[integer()]]) -> integer().
max_building(N, Restrictions) ->
    Sorted = lists:sort([[1, 0] | Restrictions]),
    LtoR = pass_l_to_r(Sorted),
    RtoL = pass_r_to_l(lists:reverse(LtoR)),
    M1 = find_max_peaks(RtoL, 0),
    [LastId, LastH] = lists:last(RtoL),
    M2 = LastH + (N - LastId),
    erlang:max(M1, M2).

pass_l_to_r([H | T]) ->
    pass_l_to_r(T, [H]).
pass_l_to_r([], Acc) ->
    lists:reverse(Acc);
pass_l_to_r([[Id2, H2] | T], [[Id1, H1] | _] = Acc) ->
    NH2 = erlang:min(H2, H1 + (Id2 - Id1)),
    pass_l_to_r(T, [[Id2, NH2] | Acc]).

pass_r_to_l([H | T]) ->
    pass_r_to_l(T, [H]).
pass_r_to_l([], Acc) ->
    Acc;
pass_r_to_l([[Id1, H1] | T], [[Id2, H2] | _] = Acc) ->
    NH1 = erlang:min(H1, H2 + (Id2 - Id1)),
    pass_r_to_l(T, [[Id1, NH1] | Acc]).

find_max_peaks([_], Max) -> Max;
find_max_peaks([[Id1, H1], [Id2, H2] | T], Max) ->
    Peak = (H1 + H2 + Id2 - Id1) div 2,
    find_max_peaks([[Id2, H2] | T], erlang:max(Max, Peak)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_building(n :: integer, restrictions :: [[integer]]) :: integer
  def max_building(n, restrictions) do
    rs = [[1, 0] | restrictions] |> Enum.sort()

    rs = Enum.reduce(tl(rs), [hd(rs)], fn [id2, h2], acc ->
      [id1, h1] = hd(acc)
      nh2 = min(h2, h1 + (id2 - id1))
      [[id2, nh2] | acc]
    end) |> Enum.reverse()

    rs = Enum.reduce(tl(Enum.reverse(rs)), [hd(Enum.reverse(rs))], fn [id1, h1], acc ->
      [id2, h2] = hd(acc)
      nh1 = min(h1, h2 + (id2 - id1))
      [[id1, nh1] | acc]
    end)

    m1 = compute_peaks(rs, 0)
    [last_id, last_h] = List.last(rs)
    m2 = last_h + (n - last_id)
    max(m1, m2)
  end

  defp compute_peaks([_], max_p), do: max_p
  defp compute_peaks([[id1, h1], [id2, h2] | tail], max_p) do
    peak = div(h1 + h2 + id2 - id1, 2)
    compute_peaks([[id2, h2] | tail], max(max_p, peak))
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(M log M) where M is the number of restrictions. This complexity is dominated by the sorting step. The subsequent left-to-right and right-to-left passes, as well as the final peak calculation, all take O(M) time.
- **Space Complexity:** O(M) to store the copy of the restrictions. We allocate an auxiliary list or vector of size M+1 to facilitate the sorting and propagation steps.
