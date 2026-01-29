---
layout: post
title: "Minimum Cost to Convert String I"
date: 2026-01-29 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "String", "Graph Theory", "Shortest Path"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-cost-to-convert-string-i/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    long long minimumCost(string source, string\
        \ target, vector<char>& original, vector<char>& changed, vector<int>& cost)\
        \ {\n        const long long INF = 1e15;\n        vector<vector<long long>>\
        \ dist(26, vector<long long>(26, INF));\n        for (int i = 0; i < 26; ++i)\
        \ dist[i][i] = 0;\n        for (int i = 0; i < original.size(); ++i) {\n   \
        \         int u = original[i] - 'a';\n            int v = changed[i] - 'a';\n\
        \            dist[u][v] = min(dist[u][v], (long long)cost[i]);\n        }\n\
        \        for (int k = 0; k < 26; ++k) {\n            for (int i = 0; i < 26;\
        \ ++i) {\n                for (int j = 0; j < 26; ++j) {\n                 \
        \   if (dist[i][k] < INF && dist[k][j] < INF) {\n                        dist[i][j]\
        \ = min(dist[i][j], dist[i][k] + dist[k][j]);\n                    }\n     \
        \           }\n            }\n        }\n        long long totalCost = 0;\n\
        \        for (int i = 0; i < source.length(); ++i) {\n            if (source[i]\
        \ == target[i]) continue;\n            int u = source[i] - 'a';\n          \
        \  int v = target[i] - 'a';\n            if (dist[u][v] >= INF) return -1;\n\
        \            totalCost += dist[u][v];\n        }\n        return totalCost;\n\
        \    }\n};"
      java: "class Solution {\n    public long minimumCost(String source, String target,\
        \ char[] original, char[] changed, int[] cost) {\n        long INF = 1_000_000_000_000L;\n\
        \        long[][] dist = new long[26][26];\n        for (int i = 0; i < 26;\
        \ i++) {\n            for (int j = 0; j < 26; j++) {\n                dist[i][j]\
        \ = (i == j) ? 0 : INF;\n            }\n        }\n        for (int i = 0; i\
        \ < original.length; i++) {\n            int u = original[i] - 'a';\n      \
        \      int v = changed[i] - 'a';\n            dist[u][v] = Math.min(dist[u][v],\
        \ (long) cost[i]);\n        }\n        for (int k = 0; k < 26; k++) {\n    \
        \        for (int i = 0; i < 26; i++) {\n                for (int j = 0; j <\
        \ 26; j++) {\n                    dist[i][j] = Math.min(dist[i][j], dist[i][k]\
        \ + dist[k][j]);\n                }\n            }\n        }\n        long\
        \ totalCost = 0;\n        for (int i = 0; i < source.length(); i++) {\n    \
        \        int u = source.charAt(i) - 'a';\n            int v = target.charAt(i)\
        \ - 'a';\n            if (dist[u][v] >= INF) return -1;\n            totalCost\
        \ += dist[u][v];\n        }\n        return totalCost;\n    }\n}"
      python: "class Solution(object):\n    def minimumCost(self, source, target, original,\
        \ changed, cost):\n        INF = float('inf')\n        dist = [[INF] * 26 for\
        \ _ in range(26)]\n        for i in range(26):\n            dist[i][i] = 0\n\
        \        for o, c, w in zip(original, changed, cost):\n            u, v = ord(o)\
        \ - ord('a'), ord(c) - ord('a')\n            dist[u][v] = min(dist[u][v], w)\n\
        \        for k in range(26):\n            for i in range(26):\n            \
        \    for j in range(26):\n                    if dist[i][j] > dist[i][k] + dist[k][j]:\n\
        \                        dist[i][j] = dist[i][k] + dist[k][j]\n        total_cost\
        \ = 0\n        for s, t in zip(source, target):\n            if s == t: continue\n\
        \            u, v = ord(s) - ord('a'), ord(t) - ord('a')\n            if dist[u][v]\
        \ == INF:\n                return -1\n            total_cost += dist[u][v]\n\
        \        return total_cost"
      python3: "class Solution:\n    def minimumCost(self, source: str, target: str,\
        \ original: List[str], changed: List[str], cost: List[int]) -> int:\n      \
        \  INF = float('inf')\n        dist = [[INF] * 26 for _ in range(26)]\n    \
        \    for i in range(26):\n            dist[i][i] = 0\n        for o, c, w in\
        \ zip(original, changed, cost):\n            u, v = ord(o) - ord('a'), ord(c)\
        \ - ord('a')\n            if w < dist[u][v]:\n                dist[u][v] = w\n\
        \        for k in range(26):\n            for i in range(26):\n            \
        \    dk = dist[i][k]\n                for j in range(26):\n                \
        \    if dist[i][j] > dk + dist[k][j]:\n                        dist[i][j] =\
        \ dk + dist[k][j]\n        total_cost = 0\n        for s, t in zip(source, target):\n\
        \            if s == t: continue\n            u, v = ord(s) - ord('a'), ord(t)\
        \ - ord('a')\n            res = dist[u][v]\n            if res == INF:\n   \
        \             return -1\n            total_cost += res\n        return total_cost"
      c: "long long minimumCost(char* source, char* target, char* original, int originalSize,\
        \ char* changed, int changedSize, int* cost, int costSize) {\n    const long\
        \ long INF = 1e15;\n    long long dist[26][26];\n    for (int i = 0; i < 26;\
        \ i++) {\n        for (int j = 0; j < 26; j++) {\n            dist[i][j] = (i\
        \ == j) ? 0 : INF;\n        }\n    }\n    for (int i = 0; i < originalSize;\
        \ i++) {\n        int u = original[i] - 'a';\n        int v = changed[i] - 'a';\n\
        \        if (cost[i] < dist[u][v]) dist[u][v] = cost[i];\n    }\n    for (int\
        \ k = 0; k < 26; k++) {\n        for (int i = 0; i < 26; i++) {\n          \
        \  for (int j = 0; j < 26; j++) {\n                if (dist[i][k] + dist[k][j]\
        \ < dist[i][j]) {\n                    dist[i][j] = dist[i][k] + dist[k][j];\n\
        \                }\n            }\n        }\n    }\n    long long totalCost\
        \ = 0;\n    int n = strlen(source);\n    for (int i = 0; i < n; i++) {\n   \
        \     int u = source[i] - 'a';\n        int v = target[i] - 'a';\n        if\
        \ (dist[u][v] >= INF) return -1;\n        totalCost += dist[u][v];\n    }\n\
        \    return totalCost;\n}"
      csharp: "public class Solution {\n    public long MinimumCost(string source, string\
        \ target, char[] original, char[] changed, int[] cost) {\n        long INF =\
        \ 1000000000000L;\n        long[,] dist = new long[26, 26];\n        for (int\
        \ i = 0; i < 26; i++) {\n            for (int j = 0; j < 26; j++) {\n      \
        \          dist[i, j] = (i == j) ? 0 : INF;\n            }\n        }\n    \
        \    for (int i = 0; i < original.Length; i++) {\n            int u = original[i]\
        \ - 'a';\n            int v = changed[i] - 'a';\n            dist[u, v] = Math.Min(dist[u,\
        \ v], (long)cost[i]);\n        }\n        for (int k = 0; k < 26; k++) {\n \
        \           for (int i = 0; i < 26; i++) {\n                for (int j = 0;\
        \ j < 26; j++) {\n                    if (dist[i, k] + dist[k, j] < dist[i,\
        \ j]) {\n                        dist[i, j] = dist[i, k] + dist[k, j];\n   \
        \                 }\n                }\n            }\n        }\n        long\
        \ totalCost = 0;\n        for (int i = 0; i < source.Length; i++) {\n      \
        \      int u = source[i] - 'a';\n            int v = target[i] - 'a';\n    \
        \        if (dist[u, v] >= INF) return -1;\n            totalCost += dist[u,\
        \ v];\n        }\n        return totalCost;\n    }\n}"
      javascript: "/**\n * @param {string} source\n * @param {string} target\n * @param\
        \ {character[]} original\n * @param {character[]} changed\n * @param {number[]}\
        \ cost\n * @return {number}\n */\nvar minimumCost = function(source, target,\
        \ original, changed, cost) {\n    const INF = Infinity;\n    const dist = Array.from({\
        \ length: 26 }, () => Array(26).fill(INF));\n    for (let i = 0; i < 26; i++)\
        \ dist[i][i] = 0;\n    for (let i = 0; i < original.length; i++) {\n       \
        \ const u = original[i].charCodeAt(0) - 97;\n        const v = changed[i].charCodeAt(0)\
        \ - 97;\n        dist[u][v] = Math.min(dist[u][v], cost[i]);\n    }\n    for\
        \ (let k = 0; k < 26; k++) {\n        for (let i = 0; i < 26; i++) {\n     \
        \       for (let j = 0; j < 26; j++) {\n                if (dist[i][k] + dist[k][j]\
        \ < dist[i][j]) {\n                    dist[i][j] = dist[i][k] + dist[k][j];\n\
        \                }\n            }\n        }\n    }\n    let totalCost = 0;\n\
        \    for (let i = 0; i < source.length; i++) {\n        const u = source.charCodeAt(i)\
        \ - 97;\n        const v = target.charCodeAt(i) - 97;\n        if (dist[u][v]\
        \ === INF) return -1;\n        totalCost += dist[u][v];\n    }\n    return totalCost;\n\
        };"
      typescript: "function minimumCost(source: string, target: string, original: string[],\
        \ changed: string[], cost: number[]): number {\n    const INF = 1e15;\n    const\
        \ dist = Array.from({ length: 26 }, () => Array(26).fill(INF));\n\n    for (let\
        \ i = 0; i < 26; i++) dist[i][i] = 0;\n\n    for (let i = 0; i < original.length;\
        \ i++) {\n        const u = original[i].charCodeAt(0) - 97;\n        const v\
        \ = changed[i].charCodeAt(0) - 97;\n        if (cost[i] < dist[u][v]) {\n  \
        \          dist[u][v] = cost[i];\n        }\n    }\n\n    for (let k = 0; k\
        \ < 26; k++) {\n        for (let i = 0; i < 26; i++) {\n            for (let\
        \ j = 0; j < 26; j++) {\n                if (dist[i][k] + dist[k][j] < dist[i][j])\
        \ {\n                    dist[i][j] = dist[i][k] + dist[k][j];\n           \
        \     }\n            }\n        }\n    }\n\n    let totalCost = 0;\n    for\
        \ (let i = 0; i < source.length; i++) {\n        const u = source.charCodeAt(i)\
        \ - 97;\n        const v = target.charCodeAt(i) - 97;\n        if (dist[u][v]\
        \ >= INF) return -1;\n        totalCost += dist[u][v];\n    }\n\n    return\
        \ totalCost;\n};"
      php: "class Solution {\n\n    /**\n     * @param String $source\n     * @param\
        \ String $target\n     * @param String[] $original\n     * @param String[] $changed\n\
        \     * @param Integer[] $cost\n     * @return Integer\n     */\n    function\
        \ minimumCost($source, $target, $original, $changed, $cost) {\n        $INF\
        \ = 1e14;\n        $dist = array_fill(0, 26, array_fill(0, 26, $INF));\n   \
        \     for ($i = 0; $i < 26; $i++) $dist[$i][$i] = 0;\n\n        $n_orig = count($original);\n\
        \        for ($i = 0; $i < $n_orig; $i++) {\n            $u = ord($original[$i])\
        \ - ord('a');\n            $v = ord($changed[$i]) - ord('a');\n            if\
        \ ($cost[$i] < $dist[$u][$v]) {\n                $dist[$u][$v] = $cost[$i];\n\
        \            }\n        }\n\n        for ($k = 0; $k < 26; $k++) {\n       \
        \     for ($i = 0; $i < 26; $i++) {\n                for ($j = 0; $j < 26; $j++)\
        \ {\n                    if ($dist[$i][$k] + $dist[$k][$j] < $dist[$i][$j])\
        \ {\n                        $dist[$i][$j] = $dist[$i][$k] + $dist[$k][$j];\n\
        \                    }\n                }\n            }\n        }\n\n    \
        \    $totalCost = 0;\n        $len = strlen($source);\n        for ($i = 0;\
        \ $i < $len; $i++) {\n            $u = ord($source[$i]) - ord('a');\n      \
        \      $v = ord($target[$i]) - ord('a');\n            if ($dist[$u][$v] >= $INF)\
        \ return -1;\n            $totalCost += $dist[$u][$v];\n        }\n\n      \
        \  return $totalCost;\n    }\n}"
      swift: "class Solution {\n    func minimumCost(_ source: String, _ target: String,\
        \ _ original: [Character], _ changed: [Character], _ cost: [Int]) -> Int {\n\
        \        let INF = Int.max / 4\n        var dist = Array(repeating: Array(repeating:\
        \ INF, count: 26), count: 26)\n        for i in 0..<26 { dist[i][i] = 0 }\n\n\
        \        let base = Character(\"a\").asciiValue!\n        for i in 0..<original.count\
        \ {\n            let u = Int(original[i].asciiValue! - base)\n            let\
        \ v = Int(changed[i].asciiValue! - base)\n            dist[u][v] = min(dist[u][v],\
        \ cost[i])\n        }\n\n        for k in 0..<26 {\n            for i in 0..<26\
        \ {\n                for j in 0..<26 {\n                    if dist[i][k] +\
        \ dist[k][j] < dist[i][j] {\n                        dist[i][j] = dist[i][k]\
        \ + dist[k][j]\n                    }\n                }\n            }\n  \
        \      }\n\n        var totalCost = 0\n        let sourceArr = Array(source)\n\
        \        let targetArr = Array(target)\n        for i in 0..<sourceArr.count\
        \ {\n            let u = Int(sourceArr[i].asciiValue! - base)\n            let\
        \ v = Int(targetArr[i].asciiValue! - base)\n            if dist[u][v] >= INF\
        \ { return -1 }\n            totalCost += dist[u][v]\n        }\n\n        return\
        \ totalCost\n    }\n}"
      kotlin: "class Solution {\n    fun minimumCost(source: String, target: String,\
        \ original: CharArray, changed: CharArray, cost: IntArray): Long {\n       \
        \ val INF = 100000000000000L\n        val dist = Array(26) { LongArray(26) {\
        \ INF } }\n        for (i in 0 until 26) dist[i][i] = 0\n\n        for (i in\
        \ original.indices) {\n            val u = original[i] - 'a'\n            val\
        \ v = changed[i] - 'a'\n            if (cost[i].toLong() < dist[u][v]) {\n \
        \               dist[u][v] = cost[i].toLong()\n            }\n        }\n\n\
        \        for (k in 0 until 26) {\n            for (i in 0 until 26) {\n    \
        \            for (j in 0 until 26) {\n                    if (dist[i][k] + dist[k][j]\
        \ < dist[i][j]) {\n                        dist[i][j] = dist[i][k] + dist[k][j]\n\
        \                    }\n                }\n            }\n        }\n\n    \
        \    var totalCost: Long = 0\n        for (i in source.indices) {\n        \
        \    val u = source[i] - 'a'\n            val v = target[i] - 'a'\n        \
        \    if (dist[u][v] >= INF) return -1\n            totalCost += dist[u][v]\n\
        \        }\n\n        return totalCost\n    }\n}"
      dart: "class Solution {\n  int minimumCost(String source, String target, List<String>\
        \ original, List<String> changed, List<int> cost) {\n    const int INF = 100000000000000;\n\
        \    List<List<int>> dist = List.generate(26, (_) => List.filled(26, INF));\n\
        \    for (int i = 0; i < 26; i++) dist[i][i] = 0;\n\n    int base = 'a'.codeUnitAt(0);\n\
        \    for (int i = 0; i < original.length; i++) {\n      int u = original[i].codeUnitAt(0)\
        \ - base;\n      int v = changed[i].codeUnitAt(0) - base;\n      if (cost[i]\
        \ < dist[u][v]) dist[u][v] = cost[i];\n    }\n\n    for (int k = 0; k < 26;\
        \ k++) {\n      for (int i = 0; i < 26; i++) {\n        for (int j = 0; j <\
        \ 26; j++) {\n          if (dist[i][k] + dist[k][j] < dist[i][j]) {\n      \
        \      dist[i][j] = dist[i][k] + dist[k][j];\n          }\n        }\n     \
        \ }\n    }\n\n    int totalCost = 0;\n    for (int i = 0; i < source.length;\
        \ i++) {\n      int u = source.codeUnitAt(i) - base;\n      int v = target.codeUnitAt(i)\
        \ - base;\n      if (dist[u][v] >= INF) return -1;\n      totalCost += dist[u][v];\n\
        \    }\n\n    return totalCost;\n  }\n}"
      go: "func minimumCost(source string, target string, original []byte, changed []byte,\
        \ cost []int) int64 {\n\tconst INF int64 = 1e15\n\tdist := [26][26]int64{}\n\
        \tfor i := 0; i < 26; i++ {\n\t\tfor j := 0; j < 26; j++ {\n\t\t\tif i == j\
        \ {\n\t\t\t\tdist[i][j] = 0\n\t\t\t} else {\n\t\t\t\tdist[i][j] = INF\n\t\t\t\
        }\n\t\t}\n\t}\n\n\tfor i := 0; i < len(original); i++ {\n\t\tu := int(original[i]\
        \ - 'a')\n\t\tv := int(changed[i] - 'a')\n\t\tif int64(cost[i]) < dist[u][v]\
        \ {\n\t\t\tdist[u][v] = int64(cost[i])\n\t\t}\n\t}\n\n\tfor k := 0; k < 26;\
        \ k++ {\n\t\tfor i := 0; i < 26; i++ {\n\t\t\tfor j := 0; j < 26; j++ {\n\t\t\
        \t\tif dist[i][k]+dist[k][j] < dist[i][j] {\n\t\t\t\t\tdist[i][j] = dist[i][k]\
        \ + dist[k][j]\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\t}\n\n\tvar totalCost int64 = 0\n\
        \tfor i := 0; i < len(source); i++ {\n\t\tu := int(source[i] - 'a')\n\t\tv :=\
        \ int(target[i] - 'a')\n\t\tif dist[u][v] >= INF {\n\t\t\treturn -1\n\t\t}\n\
        \t\ttotalCost += dist[u][v]\n\t}\n\n\treturn totalCost\n}"
      ruby: "def minimum_cost(source, target, original, changed, cost)\n  inf = 10**15\n\
        \  dist = Array.new(26) { Array.new(26, inf) }\n  26.times { |i| dist[i][i]\
        \ = 0 }\n  original.length.times do |i|\n    u = original[i].ord - 'a'.ord\n\
        \    v = changed[i].ord - 'a'.ord\n    dist[u][v] = [dist[u][v], cost[i]].min\n\
        \  end\n  26.times do |k|\n    26.times do |i|\n      26.times do |j|\n    \
        \    if dist[i][k] + dist[k][j] < dist[i][j]\n          dist[i][j] = dist[i][k]\
        \ + dist[k][j]\n        end\n      end\n    end\n  end\n  total_cost = 0\n \
        \ source.length.times do |i|\n    u = source[i].ord - 'a'.ord\n    v = target[i].ord\
        \ - 'a'.ord\n    return -1 if dist[u][v] >= inf\n    total_cost += dist[u][v]\n\
        \  end\n  total_cost\nend"
      scala: "object Solution {\n  def minimumCost(source: String, target: String, original:\
        \ Array[Char], changed: Array[Char], cost: Array[Int]): Long = {\n    val inf\
        \ = 1000000000000000L\n    val dist = Array.fill(26, 26)(inf)\n    for (i <-\
        \ 0 until 26) dist(i)(i) = 0\n    for (i <- original.indices) {\n      val u\
        \ = original(i) - 'a'\n      val v = changed(i) - 'a'\n      dist(u)(v) = math.min(dist(u)(v),\
        \ cost(i).toLong)\n    }\n    for (k <- 0 until 26; i <- 0 until 26; j <- 0\
        \ until 26) {\n      if (dist(i)(k) + dist(k)(j) < dist(i)(j)) {\n        dist(i)(j)\
        \ = dist(i)(k) + dist(k)(j)\n      }\n    }\n    var totalCost = 0L\n    for\
        \ (i <- source.indices) {\n      val u = source(i) - 'a'\n      val v = target(i)\
        \ - 'a'\n      if (dist(u)(v) >= inf) return -1L\n      totalCost += dist(u)(v)\n\
        \    }\n    totalCost\n  }\n}"
      rust: "impl Solution {\n    pub fn minimum_cost(source: String, target: String,\
        \ original: Vec<char>, changed: Vec<char>, cost: Vec<i32>) -> i64 {\n      \
        \  let inf: i64 = 1_000_000_000_000_000;\n        let mut dist = vec![vec![inf;\
        \ 26]; 26];\n        for i in 0..26 { dist[i][i] = 0; }\n        for i in 0..original.len()\
        \ {\n            let u = (original[i] as u8 - b'a') as usize;\n            let\
        \ v = (changed[i] as u8 - b'a') as usize;\n            dist[u][v] = dist[u][v].min(cost[i]\
        \ as i64);\n        }\n        for k in 0..26 {\n            for i in 0..26\
        \ {\n                for j in 0..26 {\n                    if dist[i][k] + dist[k][j]\
        \ < dist[i][j] {\n                        dist[i][j] = dist[i][k] + dist[k][j];\n\
        \                    }\n                }\n            }\n        }\n      \
        \  let mut total_cost: i64 = 0;\n        let s_bytes = source.as_bytes();\n\
        \        let t_bytes = target.as_bytes();\n        for i in 0..s_bytes.len()\
        \ {\n            let u = (s_bytes[i] - b'a') as usize;\n            let v =\
        \ (t_bytes[i] - b'a') as usize;\n            if dist[u][v] >= inf { return -1;\
        \ }\n            total_cost += dist[u][v];\n        }\n        total_cost\n\
        \    }\n}"
      racket: "(define/contract (minimum-cost source target original changed cost)\n\
        \  (-> string? string? (listof char?) (listof char?) (listof exact-integer?)\
        \ exact-integer?)\n  (let* ([inf 1000000000000000]\n         [dist (make-vector\
        \ 676 inf)])\n    (for ([i (in-range 26)])\n      (vector-set! dist (+ (* i\
        \ 26) i) 0))\n    (for ([o original] [c changed] [cs cost])\n      (let* ([u\
        \ (- (char->integer o) (char->integer #\\a))]\n             [v (- (char->integer\
        \ c) (char->integer #\\a))]\n             [idx (+ (* u 26) v)])\n        (vector-set!\
        \ dist idx (min (vector-ref dist idx) cs))))\n    (for ([k (in-range 26)])\n\
        \      (for ([i (in-range 26)])\n        (for ([j (in-range 26)])\n        \
        \  (let ([ik (+ (* i 26) k)]\n                [kj (+ (* k 26) j)]\n        \
        \        [ij (+ (* i 26) j)])\n            (let ([new-cost (+ (vector-ref dist\
        \ ik) (vector-ref dist kj))])\n              (when (< new-cost (vector-ref dist\
        \ ij))\n                (vector-set! dist ij new-cost)))))))\n    (let loop\
        \ ([i 0] [total 0])\n      (if (= i (string-length source))\n          total\n\
        \          (let* ([u (- (char->integer (string-ref source i)) (char->integer\
        \ #\\a))]\n                 [v (- (char->integer (string-ref target i)) (char->integer\
        \ #\\a))]\n                 [c (vector-ref dist (+ (* u 26) v))])\n        \
        \    (if (>= c inf) -1 (loop (+ i 1) (+ total c))))))))"
      erlang: "-spec minimum_cost(Source :: unicode:unicode_binary(), Target :: unicode:unicode_binary(),\
        \ Original :: [char()], Changed :: [char()], Cost :: [integer()]) -> integer().\n\
        minimum_cost(Source, Target, Original, Changed, Cost) ->\n  Inf = 1000000000000000,\n\
        \  InitialDist = maps:from_list([{{I, J}, if I =:= J -> 0; true -> Inf end}\
        \ || I <- lists:seq(0, 25), J <- lists:seq(0, 25)]),\n  PopulateDist = fun({O,\
        \ C, W}, Acc) ->\n    U = O - $a,\n    V = C - $a,\n    Current = maps:get({U,\
        \ V}, Acc),\n    if W < Current -> maps:put({U, V}, W, Acc);\n       true ->\
        \ Acc\n    end\n  end,\n  DistWithEdges = lists:foldl(PopulateDist, InitialDist,\
        \ lists:zip3(Original, Changed, Cost)),\n  FloydWarshall = fun(K, AccK) ->\n\
        \    lists:foldl(fun(I, AccI) ->\n      IK = maps:get({I, K}, AccI),\n     \
        \ if IK >= Inf -> AccI;\n         true ->\n           lists:foldl(fun(J, AccJ)\
        \ ->\n             KJ = maps:get({K, J}, AccJ),\n             IJ = maps:get({I,\
        \ J}, AccJ),\n             if IK + KJ < IJ -> maps:put({I, J}, IK + KJ, AccJ);\n\
        \                true -> AccJ\n             end\n           end, AccI, lists:seq(0,\
        \ 25))\n      end\n    end, AccK, lists:seq(0, 25))\n  end,\n  FinalDist = lists:foldl(FloydWarshall,\
        \ DistWithEdges, lists:seq(0, 25)),\n  SList = binary_to_list(Source),\n  TList\
        \ = binary_to_list(Target),\n  lists:foldl(fun({S, T}, Acc) ->\n    if Acc =:=\
        \ -1 -> -1;\n       true ->\n         W = maps:get({S - $a, T - $a}, FinalDist),\n\
        \         if W >= Inf -> -1;\n            true -> Acc + W\n         end\n  \
        \  end\n  end, 0, lists:zip(SList, TList))."
      elixir: "defmodule Solution do\n  @spec minimum_cost(source :: String.t, target\
        \ :: String.t, original :: [char], changed :: [char], cost :: [integer]) ::\
        \ integer\n  def minimum_cost(source, target, original, changed, cost) do\n\
        \    inf = 1_000_000_000_000_000\n    initial_dist = for i <- 0..25, j <- 0..25,\
        \ into: %{}, do: {{i, j}, if(i == j, do: 0, else: inf)}\n    dist_with_edges\
        \ = Enum.zip([original, changed, cost])\n    |> Enum.reduce(initial_dist, fn\
        \ {o, c, w}, acc ->\n      u = o - ?a\n      v = c - ?a\n      Map.update!(acc,\
        \ {u, v}, &min(&1, w))\n    end)\n    final_dist = Enum.reduce(0..25, dist_with_edges,\
        \ fn k, acc_k ->\n      Enum.reduce(0..25, acc_k, fn i, acc_i ->\n        ik\
        \ = acc_i[{i, k}]\n        if ik >= inf do\n          acc_i\n        else\n\
        \          Enum.reduce(0..25, acc_i, fn j, acc_j ->\n            kj = acc_j[{k,\
        \ j}]\n            ij = acc_j[{i, j}]\n            if ik + kj < ij, do: Map.put(acc_j,\
        \ {i, j}, ik + kj), else: acc_j\n          end)\n        end\n      end)\n \
        \   end)\n    source_chars = String.to_charlist(source)\n    target_chars =\
        \ String.to_charlist(target)\n    Enum.zip(source_chars, target_chars)\n   \
        \ |> Enum.reduce_while(0, fn {s, t}, acc ->\n      u = s - ?a\n      v = t -\
        \ ?a\n      w = final_dist[{u, v}]\n      if w >= inf, do: {:halt, -1}, else:\
        \ {:cont, acc + w}\n    end)\n  end\nend"
    approach: The problem can be modeled as a shortest path problem on a directed graph
      where nodes represent the 26 lowercase English letters. Each transformation rule
      from a character 'u' to 'v' with cost 'w' acts as a weighted directed edge. Since
      we need to find the minimum cost for any sequence of transformations, we can use
      the Floyd-Warshall algorithm to precompute the all-pairs shortest paths between
      all characters. We initialize a 26x26 distance matrix with infinity, set diagonal
      elements to zero, and populate it with the minimum given costs for each character
      pair.
    time_complexity: O(N + M + V^3), where N is the length of the strings, M is the
      number of transformation rules, and V is the size of the alphabet (26). Building
      the initial adjacency matrix takes O(M), the Floyd-Warshall algorithm takes O(V^3),
      and the final pass over the strings takes O(N).
    space_complexity: O(V^2), where V is the size of the alphabet (26). This space is
      used to store the 26x26 distance matrix containing the minimum conversion costs
      between all pairs of characters.
    elapsed_time: 185.48838138580322
    model: gemini-3-flash-preview
    generated_at: '2026-01-29 01:24:00 '
---

## Problem #2976: Minimum Cost to Convert String I

**Difficulty:** Medium

**Topics:** Array, String, Graph Theory, Shortest Path

## Problem Description

<p>You are given two <strong>0-indexed</strong> strings <code>source</code> and <code>target</code>, both of length <code>n</code> and consisting of <strong>lowercase</strong> English letters. You are also given two <strong>0-indexed</strong> character arrays <code>original</code> and <code>changed</code>, and an integer array <code>cost</code>, where <code>cost[i]</code> represents the cost of changing the character <code>original[i]</code> to the character <code>changed[i]</code>.</p>

<p>You start with the string <code>source</code>. In one operation, you can pick a character <code>x</code> from the string and change it to the character <code>y</code> at a cost of <code>z</code> <strong>if</strong> there exists <strong>any</strong> index <code>j</code> such that <code>cost[j] == z</code>, <code>original[j] == x</code>, and <code>changed[j] == y</code>.</p>

<p>Return <em>the <strong>minimum</strong> cost to convert the string </em><code>source</code><em> to the string </em><code>target</code><em> using <strong>any</strong> number of operations. If it is impossible to convert</em> <code>source</code> <em>to</em> <code>target</code>, <em>return</em> <code>-1</code>.</p>

<p><strong>Note</strong> that there may exist indices <code>i</code>, <code>j</code> such that <code>original[j] == original[i]</code> and <code>changed[j] == changed[i]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> source = &quot;abcd&quot;, target = &quot;acbe&quot;, original = [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;,&quot;c&quot;,&quot;e&quot;,&quot;d&quot;], changed = [&quot;b&quot;,&quot;c&quot;,&quot;b&quot;,&quot;e&quot;,&quot;b&quot;,&quot;e&quot;], cost = [2,5,5,1,2,20]
<strong>Output:</strong> 28
<strong>Explanation:</strong> To convert the string &quot;abcd&quot; to string &quot;acbe&quot;:
- Change value at index 1 from &#39;b&#39; to &#39;c&#39; at a cost of 5.
- Change value at index 2 from &#39;c&#39; to &#39;e&#39; at a cost of 1.
- Change value at index 2 from &#39;e&#39; to &#39;b&#39; at a cost of 2.
- Change value at index 3 from &#39;d&#39; to &#39;e&#39; at a cost of 20.
The total cost incurred is 5 + 1 + 2 + 20 = 28.
It can be shown that this is the minimum possible cost.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> source = &quot;aaaa&quot;, target = &quot;bbbb&quot;, original = [&quot;a&quot;,&quot;c&quot;], changed = [&quot;c&quot;,&quot;b&quot;], cost = [1,2]
<strong>Output:</strong> 12
<strong>Explanation:</strong> To change the character &#39;a&#39; to &#39;b&#39; change the character &#39;a&#39; to &#39;c&#39; at a cost of 1, followed by changing the character &#39;c&#39; to &#39;b&#39; at a cost of 2, for a total cost of 1 + 2 = 3. To change all occurrences of &#39;a&#39; to &#39;b&#39;, a total cost of 3 * 4 = 12 is incurred.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> source = &quot;abcd&quot;, target = &quot;abce&quot;, original = [&quot;a&quot;], changed = [&quot;e&quot;], cost = [10000]
<strong>Output:</strong> -1
<strong>Explanation:</strong> It is impossible to convert source to target because the value at index 3 cannot be changed from &#39;d&#39; to &#39;e&#39;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= source.length == target.length &lt;= 10<sup>5</sup></code></li>
	<li><code>source</code>, <code>target</code> consist of lowercase English letters.</li>
	<li><code>1 &lt;= cost.length == original.length == changed.length &lt;= 2000</code></li>
	<li><code>original[i]</code>, <code>changed[i]</code> are lowercase English letters.</li>
	<li><code>1 &lt;= cost[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>original[i] != changed[i]</code></li>
</ul>


## Hints

1. Construct a graph with each letter as a node, and construct an edge `(a, b)` with weight `c` if we can change from character `a` to letter `b` with cost `c`. (Keep the one with the smallest cost in case there are multiple edges between `a` and `b`).

2. Calculate the shortest path for each pair of characters `(source[i], target[i])`. The sum of cost over all `i` in the range `[0, source.length - 1]`. If there is no path between `source[i]` and `target[i]`, the answer is `-1`.

3. Any shortest path algorithms will work since we only have `26` nodes. Since we only have at most `26 * 26` pairs, we can save the result to avoid re-calculation.

4. We can also use Floyd Warshall's algorithm to precompute all the results.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be modeled as a shortest path problem on a directed graph where nodes represent the 26 lowercase English letters. Each transformation rule from a character 'u' to 'v' with cost 'w' acts as a weighted directed edge. Since we need to find the minimum cost for any sequence of transformations, we can use the Floyd-Warshall algorithm to precompute the all-pairs shortest paths between all characters. We initialize a 26x26 distance matrix with infinity, set diagonal elements to zero, and populate it with the minimum given costs for each character pair.

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
    long long minimumCost(string source, string target, vector<char>& original, vector<char>& changed, vector<int>& cost) {
        const long long INF = 1e15;
        vector<vector<long long>> dist(26, vector<long long>(26, INF));
        for (int i = 0; i < 26; ++i) dist[i][i] = 0;
        for (int i = 0; i < original.size(); ++i) {
            int u = original[i] - 'a';
            int v = changed[i] - 'a';
            dist[u][v] = min(dist[u][v], (long long)cost[i]);
        }
        for (int k = 0; k < 26; ++k) {
            for (int i = 0; i < 26; ++i) {
                for (int j = 0; j < 26; ++j) {
                    if (dist[i][k] < INF && dist[k][j] < INF) {
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                    }
                }
            }
        }
        long long totalCost = 0;
        for (int i = 0; i < source.length(); ++i) {
            if (source[i] == target[i]) continue;
            int u = source[i] - 'a';
            int v = target[i] - 'a';
            if (dist[u][v] >= INF) return -1;
            totalCost += dist[u][v];
        }
        return totalCost;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public long minimumCost(String source, String target, char[] original, char[] changed, int[] cost) {
        long INF = 1_000_000_000_000L;
        long[][] dist = new long[26][26];
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < 26; j++) {
                dist[i][j] = (i == j) ? 0 : INF;
            }
        }
        for (int i = 0; i < original.length; i++) {
            int u = original[i] - 'a';
            int v = changed[i] - 'a';
            dist[u][v] = Math.min(dist[u][v], (long) cost[i]);
        }
        for (int k = 0; k < 26; k++) {
            for (int i = 0; i < 26; i++) {
                for (int j = 0; j < 26; j++) {
                    dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
        long totalCost = 0;
        for (int i = 0; i < source.length(); i++) {
            int u = source.charAt(i) - 'a';
            int v = target.charAt(i) - 'a';
            if (dist[u][v] >= INF) return -1;
            totalCost += dist[u][v];
        }
        return totalCost;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        INF = float('inf')
        dist = [[INF] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0
        for o, c, w in zip(original, changed, cost):
            u, v = ord(o) - ord('a'), ord(c) - ord('a')
            dist[u][v] = min(dist[u][v], w)
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        total_cost = 0
        for s, t in zip(source, target):
            if s == t: continue
            u, v = ord(s) - ord('a'), ord(t) - ord('a')
            if dist[u][v] == INF:
                return -1
            total_cost += dist[u][v]
        return total_cost
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = float('inf')
        dist = [[INF] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0
        for o, c, w in zip(original, changed, cost):
            u, v = ord(o) - ord('a'), ord(c) - ord('a')
            if w < dist[u][v]:
                dist[u][v] = w
        for k in range(26):
            for i in range(26):
                dk = dist[i][k]
                for j in range(26):
                    if dist[i][j] > dk + dist[k][j]:
                        dist[i][j] = dk + dist[k][j]
        total_cost = 0
        for s, t in zip(source, target):
            if s == t: continue
            u, v = ord(s) - ord('a'), ord(t) - ord('a')
            res = dist[u][v]
            if res == INF:
                return -1
            total_cost += res
        return total_cost
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
long long minimumCost(char* source, char* target, char* original, int originalSize, char* changed, int changedSize, int* cost, int costSize) {
    const long long INF = 1e15;
    long long dist[26][26];
    for (int i = 0; i < 26; i++) {
        for (int j = 0; j < 26; j++) {
            dist[i][j] = (i == j) ? 0 : INF;
        }
    }
    for (int i = 0; i < originalSize; i++) {
        int u = original[i] - 'a';
        int v = changed[i] - 'a';
        if (cost[i] < dist[u][v]) dist[u][v] = cost[i];
    }
    for (int k = 0; k < 26; k++) {
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < 26; j++) {
                if (dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }
    long long totalCost = 0;
    int n = strlen(source);
    for (int i = 0; i < n; i++) {
        int u = source[i] - 'a';
        int v = target[i] - 'a';
        if (dist[u][v] >= INF) return -1;
        totalCost += dist[u][v];
    }
    return totalCost;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public long MinimumCost(string source, string target, char[] original, char[] changed, int[] cost) {
        long INF = 1000000000000L;
        long[,] dist = new long[26, 26];
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < 26; j++) {
                dist[i, j] = (i == j) ? 0 : INF;
            }
        }
        for (int i = 0; i < original.Length; i++) {
            int u = original[i] - 'a';
            int v = changed[i] - 'a';
            dist[u, v] = Math.Min(dist[u, v], (long)cost[i]);
        }
        for (int k = 0; k < 26; k++) {
            for (int i = 0; i < 26; i++) {
                for (int j = 0; j < 26; j++) {
                    if (dist[i, k] + dist[k, j] < dist[i, j]) {
                        dist[i, j] = dist[i, k] + dist[k, j];
                    }
                }
            }
        }
        long totalCost = 0;
        for (int i = 0; i < source.Length; i++) {
            int u = source[i] - 'a';
            int v = target[i] - 'a';
            if (dist[u, v] >= INF) return -1;
            totalCost += dist[u, v];
        }
        return totalCost;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} source
 * @param {string} target
 * @param {character[]} original
 * @param {character[]} changed
 * @param {number[]} cost
 * @return {number}
 */
var minimumCost = function(source, target, original, changed, cost) {
    const INF = Infinity;
    const dist = Array.from({ length: 26 }, () => Array(26).fill(INF));
    for (let i = 0; i < 26; i++) dist[i][i] = 0;
    for (let i = 0; i < original.length; i++) {
        const u = original[i].charCodeAt(0) - 97;
        const v = changed[i].charCodeAt(0) - 97;
        dist[u][v] = Math.min(dist[u][v], cost[i]);
    }
    for (let k = 0; k < 26; k++) {
        for (let i = 0; i < 26; i++) {
            for (let j = 0; j < 26; j++) {
                if (dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }
    let totalCost = 0;
    for (let i = 0; i < source.length; i++) {
        const u = source.charCodeAt(i) - 97;
        const v = target.charCodeAt(i) - 97;
        if (dist[u][v] === INF) return -1;
        totalCost += dist[u][v];
    }
    return totalCost;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimumCost(source: string, target: string, original: string[], changed: string[], cost: number[]): number {
    const INF = 1e15;
    const dist = Array.from({ length: 26 }, () => Array(26).fill(INF));

    for (let i = 0; i < 26; i++) dist[i][i] = 0;

    for (let i = 0; i < original.length; i++) {
        const u = original[i].charCodeAt(0) - 97;
        const v = changed[i].charCodeAt(0) - 97;
        if (cost[i] < dist[u][v]) {
            dist[u][v] = cost[i];
        }
    }

    for (let k = 0; k < 26; k++) {
        for (let i = 0; i < 26; i++) {
            for (let j = 0; j < 26; j++) {
                if (dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }

    let totalCost = 0;
    for (let i = 0; i < source.length; i++) {
        const u = source.charCodeAt(i) - 97;
        const v = target.charCodeAt(i) - 97;
        if (dist[u][v] >= INF) return -1;
        totalCost += dist[u][v];
    }

    return totalCost;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String $source
     * @param String $target
     * @param String[] $original
     * @param String[] $changed
     * @param Integer[] $cost
     * @return Integer
     */
    function minimumCost($source, $target, $original, $changed, $cost) {
        $INF = 1e14;
        $dist = array_fill(0, 26, array_fill(0, 26, $INF));
        for ($i = 0; $i < 26; $i++) $dist[$i][$i] = 0;

        $n_orig = count($original);
        for ($i = 0; $i < $n_orig; $i++) {
            $u = ord($original[$i]) - ord('a');
            $v = ord($changed[$i]) - ord('a');
            if ($cost[$i] < $dist[$u][$v]) {
                $dist[$u][$v] = $cost[$i];
            }
        }

        for ($k = 0; $k < 26; $k++) {
            for ($i = 0; $i < 26; $i++) {
                for ($j = 0; $j < 26; $j++) {
                    if ($dist[$i][$k] + $dist[$k][$j] < $dist[$i][$j]) {
                        $dist[$i][$j] = $dist[$i][$k] + $dist[$k][$j];
                    }
                }
            }
        }

        $totalCost = 0;
        $len = strlen($source);
        for ($i = 0; $i < $len; $i++) {
            $u = ord($source[$i]) - ord('a');
            $v = ord($target[$i]) - ord('a');
            if ($dist[$u][$v] >= $INF) return -1;
            $totalCost += $dist[$u][$v];
        }

        return $totalCost;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minimumCost(_ source: String, _ target: String, _ original: [Character], _ changed: [Character], _ cost: [Int]) -> Int {
        let INF = Int.max / 4
        var dist = Array(repeating: Array(repeating: INF, count: 26), count: 26)
        for i in 0..<26 { dist[i][i] = 0 }

        let base = Character("a").asciiValue!
        for i in 0..<original.count {
            let u = Int(original[i].asciiValue! - base)
            let v = Int(changed[i].asciiValue! - base)
            dist[u][v] = min(dist[u][v], cost[i])
        }

        for k in 0..<26 {
            for i in 0..<26 {
                for j in 0..<26 {
                    if dist[i][k] + dist[k][j] < dist[i][j] {
                        dist[i][j] = dist[i][k] + dist[k][j]
                    }
                }
            }
        }

        var totalCost = 0
        let sourceArr = Array(source)
        let targetArr = Array(target)
        for i in 0..<sourceArr.count {
            let u = Int(sourceArr[i].asciiValue! - base)
            let v = Int(targetArr[i].asciiValue! - base)
            if dist[u][v] >= INF { return -1 }
            totalCost += dist[u][v]
        }

        return totalCost
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minimumCost(source: String, target: String, original: CharArray, changed: CharArray, cost: IntArray): Long {
        val INF = 100000000000000L
        val dist = Array(26) { LongArray(26) { INF } }
        for (i in 0 until 26) dist[i][i] = 0

        for (i in original.indices) {
            val u = original[i] - 'a'
            val v = changed[i] - 'a'
            if (cost[i].toLong() < dist[u][v]) {
                dist[u][v] = cost[i].toLong()
            }
        }

        for (k in 0 until 26) {
            for (i in 0 until 26) {
                for (j in 0 until 26) {
                    if (dist[i][k] + dist[k][j] < dist[i][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j]
                    }
                }
            }
        }

        var totalCost: Long = 0
        for (i in source.indices) {
            val u = source[i] - 'a'
            val v = target[i] - 'a'
            if (dist[u][v] >= INF) return -1
            totalCost += dist[u][v]
        }

        return totalCost
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minimumCost(String source, String target, List<String> original, List<String> changed, List<int> cost) {
    const int INF = 100000000000000;
    List<List<int>> dist = List.generate(26, (_) => List.filled(26, INF));
    for (int i = 0; i < 26; i++) dist[i][i] = 0;

    int base = 'a'.codeUnitAt(0);
    for (int i = 0; i < original.length; i++) {
      int u = original[i].codeUnitAt(0) - base;
      int v = changed[i].codeUnitAt(0) - base;
      if (cost[i] < dist[u][v]) dist[u][v] = cost[i];
    }

    for (int k = 0; k < 26; k++) {
      for (int i = 0; i < 26; i++) {
        for (int j = 0; j < 26; j++) {
          if (dist[i][k] + dist[k][j] < dist[i][j]) {
            dist[i][j] = dist[i][k] + dist[k][j];
          }
        }
      }
    }

    int totalCost = 0;
    for (int i = 0; i < source.length; i++) {
      int u = source.codeUnitAt(i) - base;
      int v = target.codeUnitAt(i) - base;
      if (dist[u][v] >= INF) return -1;
      totalCost += dist[u][v];
    }

    return totalCost;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minimumCost(source string, target string, original []byte, changed []byte, cost []int) int64 {
	const INF int64 = 1e15
	dist := [26][26]int64{}
	for i := 0; i < 26; i++ {
		for j := 0; j < 26; j++ {
			if i == j {
				dist[i][j] = 0
			} else {
				dist[i][j] = INF
			}
		}
	}

	for i := 0; i < len(original); i++ {
		u := int(original[i] - 'a')
		v := int(changed[i] - 'a')
		if int64(cost[i]) < dist[u][v] {
			dist[u][v] = int64(cost[i])
		}
	}

	for k := 0; k < 26; k++ {
		for i := 0; i < 26; i++ {
			for j := 0; j < 26; j++ {
				if dist[i][k]+dist[k][j] < dist[i][j] {
					dist[i][j] = dist[i][k] + dist[k][j]
				}
			}
		}
	}

	var totalCost int64 = 0
	for i := 0; i < len(source); i++ {
		u := int(source[i] - 'a')
		v := int(target[i] - 'a')
		if dist[u][v] >= INF {
			return -1
		}
		totalCost += dist[u][v]
	}

	return totalCost
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def minimum_cost(source, target, original, changed, cost)
  inf = 10**15
  dist = Array.new(26) { Array.new(26, inf) }
  26.times { |i| dist[i][i] = 0 }
  original.length.times do |i|
    u = original[i].ord - 'a'.ord
    v = changed[i].ord - 'a'.ord
    dist[u][v] = [dist[u][v], cost[i]].min
  end
  26.times do |k|
    26.times do |i|
      26.times do |j|
        if dist[i][k] + dist[k][j] < dist[i][j]
          dist[i][j] = dist[i][k] + dist[k][j]
        end
      end
    end
  end
  total_cost = 0
  source.length.times do |i|
    u = source[i].ord - 'a'.ord
    v = target[i].ord - 'a'.ord
    return -1 if dist[u][v] >= inf
    total_cost += dist[u][v]
  end
  total_cost
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def minimumCost(source: String, target: String, original: Array[Char], changed: Array[Char], cost: Array[Int]): Long = {
    val inf = 1000000000000000L
    val dist = Array.fill(26, 26)(inf)
    for (i <- 0 until 26) dist(i)(i) = 0
    for (i <- original.indices) {
      val u = original(i) - 'a'
      val v = changed(i) - 'a'
      dist(u)(v) = math.min(dist(u)(v), cost(i).toLong)
    }
    for (k <- 0 until 26; i <- 0 until 26; j <- 0 until 26) {
      if (dist(i)(k) + dist(k)(j) < dist(i)(j)) {
        dist(i)(j) = dist(i)(k) + dist(k)(j)
      }
    }
    var totalCost = 0L
    for (i <- source.indices) {
      val u = source(i) - 'a'
      val v = target(i) - 'a'
      if (dist(u)(v) >= inf) return -1L
      totalCost += dist(u)(v)
    }
    totalCost
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn minimum_cost(source: String, target: String, original: Vec<char>, changed: Vec<char>, cost: Vec<i32>) -> i64 {
        let inf: i64 = 1_000_000_000_000_000;
        let mut dist = vec![vec![inf; 26]; 26];
        for i in 0..26 { dist[i][i] = 0; }
        for i in 0..original.len() {
            let u = (original[i] as u8 - b'a') as usize;
            let v = (changed[i] as u8 - b'a') as usize;
            dist[u][v] = dist[u][v].min(cost[i] as i64);
        }
        for k in 0..26 {
            for i in 0..26 {
                for j in 0..26 {
                    if dist[i][k] + dist[k][j] < dist[i][j] {
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }
        let mut total_cost: i64 = 0;
        let s_bytes = source.as_bytes();
        let t_bytes = target.as_bytes();
        for i in 0..s_bytes.len() {
            let u = (s_bytes[i] - b'a') as usize;
            let v = (t_bytes[i] - b'a') as usize;
            if dist[u][v] >= inf { return -1; }
            total_cost += dist[u][v];
        }
        total_cost
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (minimum-cost source target original changed cost)
  (-> string? string? (listof char?) (listof char?) (listof exact-integer?) exact-integer?)
  (let* ([inf 1000000000000000]
         [dist (make-vector 676 inf)])
    (for ([i (in-range 26)])
      (vector-set! dist (+ (* i 26) i) 0))
    (for ([o original] [c changed] [cs cost])
      (let* ([u (- (char->integer o) (char->integer #\a))]
             [v (- (char->integer c) (char->integer #\a))]
             [idx (+ (* u 26) v)])
        (vector-set! dist idx (min (vector-ref dist idx) cs))))
    (for ([k (in-range 26)])
      (for ([i (in-range 26)])
        (for ([j (in-range 26)])
          (let ([ik (+ (* i 26) k)]
                [kj (+ (* k 26) j)]
                [ij (+ (* i 26) j)])
            (let ([new-cost (+ (vector-ref dist ik) (vector-ref dist kj))])
              (when (< new-cost (vector-ref dist ij))
                (vector-set! dist ij new-cost)))))))
    (let loop ([i 0] [total 0])
      (if (= i (string-length source))
          total
          (let* ([u (- (char->integer (string-ref source i)) (char->integer #\a))]
                 [v (- (char->integer (string-ref target i)) (char->integer #\a))]
                 [c (vector-ref dist (+ (* u 26) v))])
            (if (>= c inf) -1 (loop (+ i 1) (+ total c))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec minimum_cost(Source :: unicode:unicode_binary(), Target :: unicode:unicode_binary(), Original :: [char()], Changed :: [char()], Cost :: [integer()]) -> integer().
minimum_cost(Source, Target, Original, Changed, Cost) ->
  Inf = 1000000000000000,
  InitialDist = maps:from_list([{{I, J}, if I =:= J -> 0; true -> Inf end} || I <- lists:seq(0, 25), J <- lists:seq(0, 25)]),
  PopulateDist = fun({O, C, W}, Acc) ->
    U = O - $a,
    V = C - $a,
    Current = maps:get({U, V}, Acc),
    if W < Current -> maps:put({U, V}, W, Acc);
       true -> Acc
    end
  end,
  DistWithEdges = lists:foldl(PopulateDist, InitialDist, lists:zip3(Original, Changed, Cost)),
  FloydWarshall = fun(K, AccK) ->
    lists:foldl(fun(I, AccI) ->
      IK = maps:get({I, K}, AccI),
      if IK >= Inf -> AccI;
         true ->
           lists:foldl(fun(J, AccJ) ->
             KJ = maps:get({K, J}, AccJ),
             IJ = maps:get({I, J}, AccJ),
             if IK + KJ < IJ -> maps:put({I, J}, IK + KJ, AccJ);
                true -> AccJ
             end
           end, AccI, lists:seq(0, 25))
      end
    end, AccK, lists:seq(0, 25))
  end,
  FinalDist = lists:foldl(FloydWarshall, DistWithEdges, lists:seq(0, 25)),
  SList = binary_to_list(Source),
  TList = binary_to_list(Target),
  lists:foldl(fun({S, T}, Acc) ->
    if Acc =:= -1 -> -1;
       true ->
         W = maps:get({S - $a, T - $a}, FinalDist),
         if W >= Inf -> -1;
            true -> Acc + W
         end
    end
  end, 0, lists:zip(SList, TList)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_cost(source :: String.t, target :: String.t, original :: [char], changed :: [char], cost :: [integer]) :: integer
  def minimum_cost(source, target, original, changed, cost) do
    inf = 1_000_000_000_000_000
    initial_dist = for i <- 0..25, j <- 0..25, into: %{}, do: {{i, j}, if(i == j, do: 0, else: inf)}
    dist_with_edges = Enum.zip([original, changed, cost])
    |> Enum.reduce(initial_dist, fn {o, c, w}, acc ->
      u = o - ?a
      v = c - ?a
      Map.update!(acc, {u, v}, &min(&1, w))
    end)
    final_dist = Enum.reduce(0..25, dist_with_edges, fn k, acc_k ->
      Enum.reduce(0..25, acc_k, fn i, acc_i ->
        ik = acc_i[{i, k}]
        if ik >= inf do
          acc_i
        else
          Enum.reduce(0..25, acc_i, fn j, acc_j ->
            kj = acc_j[{k, j}]
            ij = acc_j[{i, j}]
            if ik + kj < ij, do: Map.put(acc_j, {i, j}, ik + kj), else: acc_j
          end)
        end
      end)
    end)
    source_chars = String.to_charlist(source)
    target_chars = String.to_charlist(target)
    Enum.zip(source_chars, target_chars)
    |> Enum.reduce_while(0, fn {s, t}, acc ->
      u = s - ?a
      v = t - ?a
      w = final_dist[{u, v}]
      if w >= inf, do: {:halt, -1}, else: {:cont, acc + w}
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N + M + V^3), where N is the length of the strings, M is the number of transformation rules, and V is the size of the alphabet (26). Building the initial adjacency matrix takes O(M), the Floyd-Warshall algorithm takes O(V^3), and the final pass over the strings takes O(N).
- **Space Complexity:** O(V^2), where V is the size of the alphabet (26). This space is used to store the 26x26 distance matrix containing the minimum conversion costs between all pairs of characters.
