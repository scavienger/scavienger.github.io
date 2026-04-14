---
layout: post
title: "Minimum Total Distance Traveled"
date: 2026-04-14 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Dynamic Programming", "Sorting"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/minimum-total-distance-traveled/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <algorithm>\n#include <cmath>\n\nusing namespace\
        \ std;\n\nclass Solution {\npublic:\n    long long minimumTotalDistance(vector<int>&\
        \ robot, vector<vector<int>>& factory) {\n        sort(robot.begin(), robot.end());\n\
        \        sort(factory.begin(), factory.end());\n        int n = robot.size();\n\
        \        int m = factory.size();\n        const long long INF = 1000000000000000LL;\n\
        \        vector<vector<long long>> dp(n + 1, vector<long long>(m + 1, INF));\n\
        \n        for (int j = 0; j <= m; ++j) {\n            dp[0][j] = 0;\n      \
        \  }\n\n        for (int j = 1; j <= m; ++j) {\n            long long factory_pos\
        \ = factory[j - 1][0];\n            int limit = factory[j - 1][1];\n       \
        \     for (int i = 0; i <= n; ++i) {\n                dp[i][j] = dp[i][j - 1];\n\
        \                long long current_dist = 0;\n                for (int k = 1;\
        \ k <= limit && i - k >= 0; ++k) {\n                    current_dist += abs((long\
        \ long)robot[i - k] - factory_pos);\n                    if (dp[i - k][j - 1]\
        \ != INF) {\n                        dp[i][j] = min(dp[i][j], dp[i - k][j -\
        \ 1] + current_dist);\n                    }\n                }\n          \
        \  }\n        }\n\n        return dp[n][m];\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public long minimumTotalDistance(List<Integer>\
        \ robot, int[][] factory) {\n        Collections.sort(robot);\n        Arrays.sort(factory,\
        \ (a, b) -> Integer.compare(a[0], b[0]));\n        int n = robot.size();\n \
        \       int m = factory.length;\n        long INF = 1000000000000000L;\n   \
        \     long[][] dp = new long[n + 1][m + 1];\n\n        for (int i = 1; i <=\
        \ n; i++) {\n            for (int j = 0; j <= m; j++) {\n                dp[i][j]\
        \ = INF;\n            }\n        }\n\n        for (int j = 1; j <= m; j++) {\n\
        \            long factoryPos = factory[j - 1][0];\n            int limit = factory[j\
        \ - 1][1];\n            for (int i = 0; i <= n; i++) {\n                dp[i][j]\
        \ = dp[i][j - 1];\n                long currentDist = 0;\n                for\
        \ (int k = 1; k <= limit && i - k >= 0; k++) {\n                    currentDist\
        \ += Math.abs((long) robot.get(i - k) - factoryPos);\n                    if\
        \ (dp[i - k][j - 1] != INF) {\n                        dp[i][j] = Math.min(dp[i][j],\
        \ dp[i - k][j - 1] + currentDist);\n                    }\n                }\n\
        \            }\n        }\n\n        return dp[n][m];\n    }\n}"
      python: "class Solution(object):\n    def minimumTotalDistance(self, robot, factory):\n\
        \        \"\"\"\n        :type robot: List[int]\n        :type factory: List[List[int]]\n\
        \        :rtype: int\n        \"\"\"\n        robot.sort()\n        factory.sort()\n\
        \        n, m = len(robot), len(factory)\n        INF = 10**15\n        dp =\
        \ [[INF] * (m + 1) for _ in range(n + 1)]\n\n        for j in range(m + 1):\n\
        \            dp[0][j] = 0\n\n        for j in range(1, m + 1):\n           \
        \ pos, limit = factory[j-1]\n            for i in range(n + 1):\n          \
        \      dp[i][j] = dp[i][j-1]\n                current_dist = 0\n           \
        \     for k in range(1, min(i, limit) + 1):\n                    current_dist\
        \ += abs(robot[i-k] - pos)\n                    if dp[i-k][j-1] != INF:\n  \
        \                      dp[i][j] = min(dp[i][j], dp[i-k][j-1] + current_dist)\n\
        \n        return dp[n][m]"
      python3: "class Solution:\n    def minimumTotalDistance(self, robot: list[int],\
        \ factory: list[list[int]]) -> int:\n        robot.sort()\n        factory.sort()\n\
        \        n, m = len(robot), len(factory)\n        INF = 10**15\n        dp =\
        \ [[INF] * (n + 1) for _ in range(m + 1)]\n        for j in range(m + 1):\n\
        \            dp[j][0] = 0\n\n        for j in range(1, m + 1):\n           \
        \ pos, limit = factory[j-1]\n            for i in range(n + 1):\n          \
        \      dp[j][i] = dp[j-1][i]\n                dist = 0\n                for\
        \ k in range(1, min(i, limit) + 1):\n                    dist += abs(robot[i\
        \ - k] - pos)\n                    if dp[j-1][i - k] != INF:\n             \
        \           if dp[j-1][i - k] + dist < dp[j][i]:\n                         \
        \   dp[j][i] = dp[j-1][i - k] + dist\n        return dp[m][n]"
      c: "#include <stdlib.h>\n#include <string.h>\n#include <math.h>\n\nint cmp_int(const\
        \ void* a, const void* b) {\n    int x = *(const int*)a;\n    int y = *(const\
        \ int*)b;\n    if (x < y) return -1;\n    if (x > y) return 1;\n    return 0;\n\
        }\n\nint cmp_factory(const void* a, const void* b) {\n    const int* f1 = *(const\
        \ int**)a;\n    const int* f2 = *(const int**)b;\n    if (f1[0] < f2[0]) return\
        \ -1;\n    if (f1[0] > f2[0]) return 1;\n    return 0;\n}\n\nlong long minimumTotalDistance(int*\
        \ robot, int robotSize, int** factory, int factorySize, int* factoryColSize)\
        \ {\n    qsort(robot, robotSize, sizeof(int), cmp_int);\n    qsort(factory,\
        \ factorySize, sizeof(int*), cmp_factory);\n\n    long long dp[101][101];\n\
        \    long long INF = 1000000000000000LL;\n    for (int j = 0; j <= factorySize;\
        \ j++) {\n        for (int i = 0; i <= robotSize; i++) {\n            dp[j][i]\
        \ = INF;\n        }\n        dp[j][0] = 0;\n    }\n\n    for (int j = 1; j <=\
        \ factorySize; j++) {\n        long long pos = factory[j - 1][0];\n        int\
        \ limit = factory[j - 1][1];\n        for (int i = 1; i <= robotSize; i++) {\n\
        \            dp[j][i] = dp[j - 1][i];\n            long long dist = 0;\n   \
        \         for (int k = 1; k <= limit && k <= i; k++) {\n                dist\
        \ += llabs((long long)robot[i - k] - pos);\n                if (dp[j - 1][i\
        \ - k] != INF) {\n                    if (dp[j - 1][i - k] + dist < dp[j][i])\
        \ {\n                        dp[j][i] = dp[j - 1][i - k] + dist;\n         \
        \           }\n                }\n            }\n        }\n    }\n\n    return\
        \ dp[factorySize][robotSize];\n}"
      csharp: "using System;\nusing System.Collections.Generic;\nusing System.Linq;\n\
        \npublic class Solution {\n    public long MinimumTotalDistance(IList<int> robot,\
        \ int[][] factory) {\n        int[] sortedRobot = robot.ToArray();\n       \
        \ Array.Sort(sortedRobot);\n        Array.Sort(factory, (a, b) => a[0].CompareTo(b[0]));\n\
        \        int n = sortedRobot.Length;\n        int m = factory.Length;\n    \
        \    long INF = 1000000000000000L;\n        long[,] dp = new long[m + 1, n +\
        \ 1];\n\n        for (int j = 0; j <= m; j++) {\n            for (int i = 0;\
        \ i <= n; i++) {\n                dp[j, i] = INF;\n            }\n         \
        \   dp[j, 0] = 0;\n        }\n\n        for (int j = 1; j <= m; j++) {\n   \
        \         long pos = factory[j - 1][0];\n            int limit = factory[j -\
        \ 1][1];\n            for (int i = 1; i <= n; i++) {\n                dp[j,\
        \ i] = dp[j - 1, i];\n                long dist = 0;\n                for (int\
        \ k = 1; k <= limit && k <= i; k++) {\n                    dist += Math.Abs((long)sortedRobot[i\
        \ - k] - pos);\n                    if (dp[j - 1, i - k] != INF) {\n       \
        \                 if (dp[j - 1, i - k] + dist < dp[j, i]) {\n              \
        \              dp[j, i] = dp[j - 1, i - k] + dist;\n                       \
        \ }\n                    }\n                }\n            }\n        }\n\n\
        \        return dp[m, n];\n    }\n}"
      javascript: "/**\n * @param {number[]} robot\n * @param {number[][]} factory\n\
        \ * @return {number}\n */\nvar minimumTotalDistance = function(robot, factory)\
        \ {\n    robot.sort((a, b) => a - b);\n    factory.sort((a, b) => a[0] - b[0]);\n\
        \    const n = robot.length;\n    const m = factory.length;\n    const INF =\
        \ 1e15;\n    const dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(INF));\n\
        \n    for (let j = 0; j <= m; j++) {\n        dp[j][0] = 0;\n    }\n\n    for\
        \ (let j = 1; j <= m; j++) {\n        let [pos, limit] = factory[j - 1];\n \
        \       for (let i = 1; i <= n; i++) {\n            dp[j][i] = dp[j - 1][i];\n\
        \            let dist = 0;\n            for (let k = 1; k <= limit && k <= i;\
        \ k++) {\n                dist += Math.abs(robot[i - k] - pos);\n          \
        \      if (dp[j - 1][i - k] !== INF) {\n                    if (dp[j - 1][i\
        \ - k] + dist < dp[j][i]) {\n                        dp[j][i] = dp[j - 1][i\
        \ - k] + dist;\n                    }\n                }\n            }\n  \
        \      }\n    }\n\n    return dp[m][n];\n};"
      typescript: "function minimumTotalDistance(robot: number[], factory: number[][]):\
        \ number {\n    robot.sort((a, b) => a - b);\n    factory.sort((a, b) => a[0]\
        \ - b[0]);\n\n    const m = robot.length;\n    const n = factory.length;\n \
        \   const inf = 1000000000000000;\n    const dp: number[][] = Array.from({ length:\
        \ n + 1 }, () => Array(m + 1).fill(inf));\n\n    for (let i = 0; i <= n; i++)\
        \ {\n        dp[i][0] = 0;\n    }\n\n    for (let i = 1; i <= n; i++) {\n  \
        \      const pos = factory[i - 1][0];\n        const limit = factory[i - 1][1];\n\
        \        for (let j = 0; j <= m; j++) {\n            dp[i][j] = dp[i - 1][j];\n\
        \            if (j > 0) {\n                let cost = 0;\n                const\
        \ maxK = Math.min(j, limit);\n                for (let k = 1; k <= maxK; k++)\
        \ {\n                    cost += Math.abs(robot[j - k] - pos);\n           \
        \         if (dp[i - 1][j - k] !== inf) {\n                        dp[i][j]\
        \ = Math.min(dp[i][j], dp[i - 1][j - k] + cost);\n                    }\n  \
        \              }\n            }\n        }\n    }\n\n    return dp[n][m];\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $robot\n     * @param\
        \ Integer[][] $factory\n     * @return Integer\n     */\n    function minimumTotalDistance($robot,\
        \ $factory) {\n        sort($robot);\n        usort($factory, function($a, $b)\
        \ {\n            return $a[0] <=> $b[0];\n        });\n\n        $m = count($robot);\n\
        \        $n = count($factory);\n        $inf = 1000000000000000;\n        $dp\
        \ = array_fill(0, $n + 1, array_fill(0, $m + 1, $inf));\n\n        for ($i =\
        \ 0; $i <= $n; $i++) {\n            $dp[$i][0] = 0;\n        }\n\n        for\
        \ ($i = 1; $i <= $n; $i++) {\n            $pos = $factory[$i - 1][0];\n    \
        \        $limit = $factory[$i - 1][1];\n            for ($j = 0; $j <= $m; $j++)\
        \ {\n                $dp[$i][$j] = $dp[$i - 1][$j];\n                if ($j\
        \ > 0) {\n                    $cost = 0;\n                    $maxK = min($j,\
        \ $limit);\n                    for ($k = 1; $k <= $maxK; $k++) {\n        \
        \                $cost += abs($robot[$j - $k] - $pos);\n                   \
        \     if ($dp[$i - 1][$j - $k] != $inf) {\n                            $val\
        \ = $dp[$i - 1][$j - $k] + $cost;\n                            if ($val < $dp[$i][$j])\
        \ {\n                                $dp[$i][$j] = $val;\n                 \
        \           }\n                        }\n                    }\n          \
        \      }\n            }\n        }\n\n        return $dp[$n][$m];\n    }\n}"
      swift: "class Solution {\n    func minimumTotalDistance(_ robot: [Int], _ factory:\
        \ [[Int]]) -> Int {\n        let robotSorted = robot.sorted()\n        let factorySorted\
        \ = factory.sorted(by: { $0[0] < $1[0] })\n\n        let m = robotSorted.count\n\
        \        let n = factorySorted.count\n        let inf = 1_000_000_000_000_000\n\
        \n        var dp = Array(repeating: Array(repeating: inf, count: m + 1), count:\
        \ n + 1)\n\n        for i in 0...n {\n            dp[i][0] = 0\n        }\n\n\
        \        for i in 1...n {\n            let pos = factorySorted[i - 1][0]\n \
        \           let limit = factorySorted[i - 1][1]\n            for j in 0...m\
        \ {\n                dp[i][j] = dp[i - 1][j]\n                if j > 0 {\n \
        \                   var cost = 0\n                    let maxK = min(j, limit)\n\
        \                    if maxK >= 1 {\n                        for k in 1...maxK\
        \ {\n                            cost += abs(robotSorted[j - k] - pos)\n   \
        \                         if dp[i - 1][j - k] != inf {\n                   \
        \             dp[i][j] = min(dp[i][j], dp[i - 1][j - k] + cost)\n          \
        \                  }\n                        }\n                    }\n   \
        \             }\n            }\n        }\n\n        return dp[n][m]\n    }\n\
        }"
      kotlin: "class Solution {\n    fun minimumTotalDistance(robot: List<Int>, factory:\
        \ Array<IntArray>): Long {\n        val robotSorted = robot.sorted()\n     \
        \   val factorySorted = factory.sortedBy { it[0] }\n\n        val m = robotSorted.size\n\
        \        val n = factorySorted.size\n        val inf = 1_000_000_000_000_000L\n\
        \        val dp = Array(n + 1) { LongArray(m + 1) { inf } }\n\n        for (i\
        \ in 0..n) {\n            dp[i][0] = 0L\n        }\n\n        for (i in 1..n)\
        \ {\n            val pos = factorySorted[i - 1][0]\n            val limit =\
        \ factorySorted[i - 1][1]\n            for (j in 0..m) {\n                dp[i][j]\
        \ = dp[i - 1][j]\n                if (j > 0) {\n                    var cost\
        \ = 0L\n                    val maxK = minOf(j, limit)\n                   \
        \ for (k in 1..maxK) {\n                        cost += Math.abs(robotSorted[j\
        \ - k].toLong() - pos.toLong())\n                        if (dp[i - 1][j - k]\
        \ != inf) {\n                            dp[i][j] = minOf(dp[i][j], dp[i - 1][j\
        \ - k] + cost)\n                        }\n                    }\n         \
        \       }\n            }\n        }\n\n        return dp[n][m]\n    }\n}"
      dart: "class Solution {\n  int minimumTotalDistance(List<int> robot, List<List<int>>\
        \ factory) {\n    robot.sort();\n    factory.sort((a, b) => a[0].compareTo(b[0]));\n\
        \    int n = robot.length;\n    const int INF = 1000000000000000;\n    List<int>\
        \ dp = List.filled(n + 1, INF);\n    dp[0] = 0;\n\n    for (var f in factory)\
        \ {\n      int pos = f[0];\n      int limit = f[1];\n      for (int i = n; i\
        \ >= 1; i--) {\n        int currentDist = 0;\n        for (int k = 1; k <= limit\
        \ && k <= i; k++) {\n          currentDist += (robot[i - k] - pos).abs();\n\
        \          if (dp[i - k] != INF) {\n            if (dp[i - k] + currentDist\
        \ < dp[i]) {\n              dp[i] = dp[i - k] + currentDist;\n            }\n\
        \          }\n        }\n      }\n    }\n    return dp[n];\n  }\n}"
      go: "import (\n\t\"sort\"\n)\n\nfunc minimumTotalDistance(robot []int, factory\
        \ [][]int) int64 {\n\tsort.Ints(robot)\n\tsort.Slice(factory, func(i, j int)\
        \ bool {\n\t\treturn factory[i][0] < factory[j][0]\n\t})\n\n\tn := len(robot)\n\
        \tconst INF = int64(1e15)\n\tdp := make([]int64, n+1)\n\tfor i := 1; i <= n;\
        \ i++ {\n\t\tdp[i] = INF\n\t}\n\tdp[0] = 0\n\n\tfor _, f := range factory {\n\
        \t\tpos := int64(f[0])\n\t\tlimit := f[1]\n\t\tfor i := n; i >= 1; i-- {\n\t\
        \t\tvar currentDist int64\n\t\t\tfor k := 1; k <= limit && k <= i; k++ {\n\t\
        \t\t\td := int64(robot[i-k]) - pos\n\t\t\t\tif d < 0 {\n\t\t\t\t\td = -d\n\t\
        \t\t\t}\n\t\t\t\tcurrentDist += d\n\t\t\t\tif dp[i-k] != INF {\n\t\t\t\t\tif\
        \ val := dp[i-k] + currentDist; val < dp[i] {\n\t\t\t\t\t\tdp[i] = val\n\t\t\
        \t\t\t}\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\t}\n\treturn dp[n]\n}"
      ruby: "def minimum_total_distance(robot, factory)\n  robot.sort!\n  factory.sort_by!\
        \ { |f| f[0] }\n  n = robot.size\n  inf = 10**15\n  dp = Array.new(n + 1, inf)\n\
        \  dp[0] = 0\n\n  factory.each do |f|\n    pos = f[0]\n    limit = f[1]\n  \
        \  n.downto(1) do |i|\n      current_dist = 0\n      max_k = [limit, i].min\n\
        \      1.upto(max_k) do |k|\n        current_dist += (robot[i - k] - pos).abs\n\
        \        if dp[i - k] != inf\n          dp[i] = [dp[i], dp[i - k] + current_dist].min\n\
        \        end\n      end\n    end\n  end\n  dp[n]\nend"
      scala: "object Solution {\n  def minimumTotalDistance(robot: List[Int], factory:\
        \ Array[Array[Int]]): Long = {\n    val robotArr = robot.sorted.toArray\n  \
        \  val sortedFactory = factory.sortBy(_(0))\n    val n = robotArr.length\n \
        \   val inf = 1000000000000000L\n    val dp = Array.fill(n + 1)(inf)\n    dp(0)\
        \ = 0L\n\n    for (f <- sortedFactory) {\n      val pos = f(0).toLong\n    \
        \  val limit = f(1)\n      for (i <- n to 1 by -1) {\n        var currentDist\
        \ = 0L\n        val maxK = Math.min(limit, i)\n        var k = 1\n        while\
        \ (k <= maxK) {\n          currentDist += Math.abs(robotArr(i - k).toLong -\
        \ pos)\n          if (dp(i - k) != inf) {\n            dp(i) = Math.min(dp(i),\
        \ dp(i - k) + currentDist)\n          }\n          k += 1\n        }\n     \
        \ }\n    }\n    dp(n)\n  }\n}"
      rust: "impl Solution {\n    pub fn minimum_total_distance(mut robot: Vec<i32>,\
        \ mut factory: Vec<Vec<i32>>) -> i64 {\n        robot.sort_unstable();\n   \
        \     factory.sort_unstable_by_key(|f| f[0]);\n        let n = robot.len();\n\
        \        let m = factory.len();\n        let inf = 1_000_000_000_000_000i64;\n\
        \n        let mut dp = vec![vec![inf; m + 1]; n + 1];\n\n        for j in 0..=m\
        \ {\n            dp[0][j] = 0;\n        }\n\n        for j in 1..=m {\n    \
        \        let f_pos = factory[j - 1][0] as i64;\n            let f_limit = factory[j\
        \ - 1][1] as usize;\n            for i in 0..=n {\n                dp[i][j]\
        \ = dp[i][j - 1];\n                let mut current_dist = 0;\n             \
        \   for k in 1..=f_limit {\n                    if k > i { break; }\n      \
        \              current_dist += (robot[i - k] as i64 - f_pos).abs();\n      \
        \              if dp[i - k][j - 1] != inf {\n                        dp[i][j]\
        \ = std::cmp::min(dp[i][j], dp[i - k][j - 1] + current_dist);\n            \
        \        }\n                }\n            }\n        }\n\n        dp[n][m]\n\
        \    }\n}"
      racket: "(define/contract (minimum-total-distance robot factory)\n  (-> (listof\
        \ exact-integer?) (listof (listof exact-integer?)) exact-integer?)\n  (let*\
        \ ([sorted-robot (sort robot <)]\n         [sorted-factory (sort factory (lambda\
        \ (a b) (< (car a) (car b))))]\n         [n (length sorted-robot)]\n       \
        \  [m (length sorted-factory)]\n         [inf 1000000000000000]\n         [robot-vec\
        \ (list->vector sorted-robot)]\n         [factory-vec (list->vector (map list->vector\
        \ sorted-factory))]\n         [dp (build-vector (add1 n) (lambda (_) (make-vector\
        \ (add1 m) inf)))])\n    (for ([j (in-range (add1 m))])\n      (vector-set!\
        \ (vector-ref dp 0) j 0))\n    (for ([j (in-range 1 (add1 m))])\n      (let*\
        \ ([f-entry (vector-ref factory-vec (sub1 j))]\n             [f-pos (vector-ref\
        \ f-entry 0)]\n             [f-limit (vector-ref f-entry 1)])\n        (for\
        \ ([i (in-range 0 (add1 n))])\n          (vector-set! (vector-ref dp i) j (vector-ref\
        \ (vector-ref dp i) (sub1 j)))\n          (let loop ([k 1] [current-dist 0])\n\
        \            (when (and (<= k i) (<= k f-limit))\n              (let* ([r-pos\
        \ (vector-ref robot-vec (- i k))]\n                     [new-dist (+ current-dist\
        \ (abs (- r-pos f-pos)))]\n                     [prev-val (vector-ref (vector-ref\
        \ dp (- i k)) (sub1 j))])\n                (when (< prev-val inf)\n        \
        \          (let ([current-val (vector-ref (vector-ref dp i) j)]\n          \
        \              [new-val (+ prev-val new-dist)])\n                    (when (<\
        \ new-val current-val)\n                      (vector-set! (vector-ref dp i)\
        \ j new-val))))\n                (loop (add1 k) new-dist)))))))\n    (vector-ref\
        \ (vector-ref dp n) m)))"
      erlang: "-spec minimum_total_distance(Robot :: [integer()], Factory :: [[integer()]])\
        \ -> integer().\nminimum_total_distance(Robot, Factory) ->\n    SortedRobot\
        \ = lists:sort(Robot),\n    SortedFactory = lists:sort(fun([A, _], [B, _]) ->\
        \ A < B end, Factory),\n    RTuple = list_to_tuple(SortedRobot),\n    FTuple\
        \ = list_to_tuple(SortedFactory),\n    {Result, _} = solve(0, 0, tuple_size(RTuple),\
        \ tuple_size(FTuple), RTuple, FTuple, #{}),\n    Result.\n\nsolve(RIdx, FIdx,\
        \ RCount, FCount, _RTuple, _FTuple, Memo) when RIdx =:= RCount ->\n    {0, Memo};\n\
        solve(_RIdx, FIdx, _RCount, FCount, _RTuple, _FTuple, Memo) when FIdx =:= FCount\
        \ ->\n    {1000000000000000, Memo};\nsolve(RIdx, FIdx, RCount, FCount, RTuple,\
        \ FTuple, Memo) ->\n    case maps:find({RIdx, FIdx}, Memo) of\n        {ok,\
        \ Val} -> {Val, Memo};\n        error ->\n            {ResSkip, Memo1} = solve(RIdx,\
        \ FIdx + 1, RCount, FCount, RTuple, FTuple, Memo),\n            [FPos, FLimit]\
        \ = element(FIdx + 1, FTuple),\n            {FinalRes, FinalMemo} = loop_k(1,\
        \ FLimit, RIdx, FIdx, RCount, FCount, RTuple, FTuple, FPos, 0, ResSkip, Memo1),\n\
        \            {FinalRes, maps:put({RIdx, FIdx}, FinalRes, FinalMemo)}\n    end.\n\
        \nloop_k(K, Limit, RIdx, FIdx, RCount, FCount, RTuple, FTuple, FPos, AccDist,\
        \ MinDist, Memo) ->\n    if\n        K =< Limit andalso RIdx + K =< RCount ->\n\
        \            RobotPos = element(RIdx + K, RTuple),\n            NewAccDist =\
        \ AccDist + abs(RobotPos - FPos),\n            {SubRes, NewMemo} = solve(RIdx\
        \ + K, FIdx + 1, RCount, FCount, RTuple, FTuple, Memo),\n            NewMinDist\
        \ = min(MinDist, NewAccDist + SubRes),\n            loop_k(K + 1, Limit, RIdx,\
        \ FIdx, RCount, FCount, RTuple, FTuple, FPos, NewAccDist, NewMinDist, NewMemo);\n\
        \        true ->\n            {MinDist, Memo}\n    end."
      elixir: "defmodule Solution do\n  @spec minimum_total_distance(robot :: [integer],\
        \ factory :: [[integer]]) :: integer\n  def minimum_total_distance(robot, factory)\
        \ do\n    r_sorted = Enum.sort(robot)\n    f_sorted = Enum.sort_by(factory,\
        \ fn [pos, _] -> pos end)\n    r_tuple = List.to_tuple(r_sorted)\n    f_tuple\
        \ = List.to_tuple(f_sorted)\n    {res, _} = solve(0, 0, tuple_size(r_tuple),\
        \ tuple_size(f_tuple), r_tuple, f_tuple, %{})\n    res\n  end\n\n  defp solve(r_idx,\
        \ f_idx, r_count, _f_count, _r_tuple, _f_tuple, memo) when r_idx == r_count\
        \ do\n    {0, memo}\n  end\n\n  defp solve(_r_idx, f_idx, _r_count, f_count,\
        \ _r_tuple, _f_tuple, memo) when f_idx == f_count do\n    {1_000_000_000_000_000,\
        \ memo}\n  end\n\n  defp solve(r_idx, f_idx, r_count, f_count, r_tuple, f_tuple,\
        \ memo) do\n    case Map.get(memo, {r_idx, f_idx}) do\n      nil ->\n      \
        \  {res_skip, memo1} = solve(r_idx, f_idx + 1, r_count, f_count, r_tuple, f_tuple,\
        \ memo)\n        [f_pos, f_limit] = elem(f_tuple, f_idx)\n        {res, memo2}\
        \ = loop_k(1, f_limit, r_idx, f_idx, r_count, f_count, r_tuple, f_tuple, f_pos,\
        \ 0, res_skip, memo1)\n        {res, Map.put(memo2, {r_idx, f_idx}, res)}\n\
        \      val ->\n        {val, memo}\n    end\n  end\n\n  defp loop_k(k, limit,\
        \ r_idx, f_idx, r_count, f_count, r_tuple, f_tuple, f_pos, acc_dist, min_dist,\
        \ memo) do\n    if k <= limit and r_idx + k <= r_count do\n      r_pos = elem(r_tuple,\
        \ r_idx + k - 1)\n      new_acc_dist = acc_dist + abs(r_pos - f_pos)\n     \
        \ {sub_res, next_memo} = solve(r_idx + k, f_idx + 1, r_count, f_count, r_tuple,\
        \ f_tuple, memo)\n      new_min_dist = min(min_dist, new_acc_dist + sub_res)\n\
        \      loop_k(k + 1, limit, r_idx, f_idx, r_count, f_count, r_tuple, f_tuple,\
        \ f_pos, new_acc_dist, new_min_dist, next_memo)\n    else\n      {min_dist,\
        \ memo}\n    end\n  end\nend"
    approach: 'To solve this problem, we first sort both the robots and the factories
      by their positions on the X-axis. The key intuition is that in an optimal assignment,
      the relative order of robots will be preserved: if robot A is to the left of robot
      B, robot A should be assigned to a factory that is at the same position as or
      to the left of the factory assigned to robot B. This non-crossing property allows
      us to use dynamic programming to solve the problem by considering contiguous subsegments
      of robots assigned to contiguous subsegments of factories.


      We define a 2D DP table where $DP[i][j]$ represents the minimum total distance
      to repair the first $i$ robots using the first $j$ factories. For each factory
      $j$, we can choose to repair $k$ robots, where $0 \le k \le \text{limit}_j$. If
      factory $j$ repairs $k$ robots, these must be the $k$ robots with the largest
      indices among the first $i$ robots (i.e., robots from index $i-k$ to $i-1$). The
      transition is $DP[i][j] = \min(DP[i][j-1], \min_{1 \le k \le \min(i, \text{limit}_j)}
      \{ DP[i-k][j-1] + \text{cost}(i-k \dots i-1, \text{factory } j) \})$. We initialize
      the table with a large value and set $DP[0][j] = 0$ as the base case for repairing
      zero robots.'
    time_complexity: O(M * N^2) where N is the number of robots and M is the number
      of factories. We iterate through each of the M factories, and for each factory,
      we iterate through N possible robot counts. For each robot count, we check up
      to N robots that the current factory could potentially repair. This leads to a
      total of M * N states, each taking up to O(N) time to compute.
    space_complexity: O(M * N) to store the DP table. Given that N and M are at most
      100, the table size (10,000 elements) is well within memory limits. This space
      could be further optimized to O(N) because the current factory's calculation only
      depends on the previous factory's state.
    elapsed_time: 356.9064989089966
    model: gemini-3-flash-preview
    generated_at: '2026-04-14 02:00:05 '
---

## Problem #2463: Minimum Total Distance Traveled

**Difficulty:** Hard

**Topics:** Array, Dynamic Programming, Sorting

## Problem Description

<p>There are some robots and factories on the X-axis. You are given an integer array <code>robot</code> where <code>robot[i]</code> is the position of the <code>i<sup>th</sup></code> robot. You are also given a 2D integer array <code>factory</code> where <code>factory[j] = [position<sub>j</sub>, limit<sub>j</sub>]</code> indicates that <code>position<sub>j</sub></code> is the position of the <code>j<sup>th</sup></code> factory and that the <code>j<sup>th</sup></code> factory can repair at most <code>limit<sub>j</sub></code> robots.</p>

<p>The positions of each robot are <strong>unique</strong>. The positions of each factory are also <strong>unique</strong>. Note that a robot can be <strong>in the same position</strong> as a factory initially.</p>

<p>All the robots are initially broken; they keep moving in one direction. The direction could be the negative or the positive direction of the X-axis. When a robot reaches a factory that did not reach its limit, the factory repairs the robot, and it stops moving.</p>

<p><strong>At any moment</strong>, you can set the initial direction of moving for <strong>some</strong> robot. Your target is to minimize the total distance traveled by all the robots.</p>

<p>Return <em>the minimum total distance traveled by all the robots</em>. The test cases are generated such that all the robots can be repaired.</p>

<p><strong>Note that</strong></p>

<ul>
	<li>All robots move at the same speed.</li>
	<li>If two robots move in the same direction, they will never collide.</li>
	<li>If two robots move in opposite directions and they meet at some point, they do not collide. They cross each other.</li>
	<li>If a robot passes by a factory that reached its limits, it crosses it as if it does not exist.</li>
	<li>If the robot moved from a position <code>x</code> to a position <code>y</code>, the distance it moved is <code>|y - x|</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/09/15/example1.jpg" style="width: 500px; height: 320px;" />
<pre>
<strong>Input:</strong> robot = [0,4,6], factory = [[2,2],[6,2]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> As shown in the figure:
- The first robot at position 0 moves in the positive direction. It will be repaired at the first factory.
- The second robot at position 4 moves in the negative direction. It will be repaired at the first factory.
- The third robot at position 6 will be repaired at the second factory. It does not need to move.
The limit of the first factory is 2, and it fixed 2 robots.
The limit of the second factory is 2, and it fixed 1 robot.
The total distance is |2 - 0| + |2 - 4| + |6 - 6| = 4. It can be shown that we cannot achieve a better total distance than 4.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/09/15/example-2.jpg" style="width: 500px; height: 329px;" />
<pre>
<strong>Input:</strong> robot = [1,-1], factory = [[-2,1],[2,1]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> As shown in the figure:
- The first robot at position 1 moves in the positive direction. It will be repaired at the second factory.
- The second robot at position -1 moves in the negative direction. It will be repaired at the first factory.
The limit of the first factory is 1, and it fixed 1 robot.
The limit of the second factory is 1, and it fixed 1 robot.
The total distance is |2 - 1| + |(-2) - (-1)| = 2. It can be shown that we cannot achieve a better total distance than 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= robot.length, factory.length &lt;= 100</code></li>
	<li><code>factory[j].length == 2</code></li>
	<li><code>-10<sup>9</sup> &lt;= robot[i], position<sub>j</sub> &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= limit<sub>j</sub> &lt;= robot.length</code></li>
	<li>The input will be generated such that it is always possible to repair every robot.</li>
</ul>


## Hints

1. Sort robots and factories by their positions.

2. After sorting, notice that each factory should repair some subsegment of robots.

3. Find the minimum total distance to repair first i robots with first j factories.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To solve this problem, we first sort both the robots and the factories by their positions on the X-axis. The key intuition is that in an optimal assignment, the relative order of robots will be preserved: if robot A is to the left of robot B, robot A should be assigned to a factory that is at the same position as or to the left of the factory assigned to robot B. This non-crossing property allows us to use dynamic programming to solve the problem by considering contiguous subsegments of robots assigned to contiguous subsegments of factories.

We define a 2D DP table where $DP[i][j]$ represents the minimum total distance to repair the first $i$ robots using the first $j$ factories. For each factory $j$, we can choose to repair $k$ robots, where $0 \le k \le \text{limit}_j$. If factory $j$ repairs $k$ robots, these must be the $k$ robots with the largest indices among the first $i$ robots (i.e., robots from index $i-k$ to $i-1$). The transition is $DP[i][j] = \min(DP[i][j-1], \min_{1 \le k \le \min(i, \text{limit}_j)} \{ DP[i-k][j-1] + \text{cost}(i-k \dots i-1, \text{factory } j) \})$. We initialize the table with a large value and set $DP[0][j] = 0$ as the base case for repairing zero robots.

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
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
public:
    long long minimumTotalDistance(vector<int>& robot, vector<vector<int>>& factory) {
        sort(robot.begin(), robot.end());
        sort(factory.begin(), factory.end());
        int n = robot.size();
        int m = factory.size();
        const long long INF = 1000000000000000LL;
        vector<vector<long long>> dp(n + 1, vector<long long>(m + 1, INF));

        for (int j = 0; j <= m; ++j) {
            dp[0][j] = 0;
        }

        for (int j = 1; j <= m; ++j) {
            long long factory_pos = factory[j - 1][0];
            int limit = factory[j - 1][1];
            for (int i = 0; i <= n; ++i) {
                dp[i][j] = dp[i][j - 1];
                long long current_dist = 0;
                for (int k = 1; k <= limit && i - k >= 0; ++k) {
                    current_dist += abs((long long)robot[i - k] - factory_pos);
                    if (dp[i - k][j - 1] != INF) {
                        dp[i][j] = min(dp[i][j], dp[i - k][j - 1] + current_dist);
                    }
                }
            }
        }

        return dp[n][m];
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
    public long minimumTotalDistance(List<Integer> robot, int[][] factory) {
        Collections.sort(robot);
        Arrays.sort(factory, (a, b) -> Integer.compare(a[0], b[0]));
        int n = robot.size();
        int m = factory.length;
        long INF = 1000000000000000L;
        long[][] dp = new long[n + 1][m + 1];

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= m; j++) {
                dp[i][j] = INF;
            }
        }

        for (int j = 1; j <= m; j++) {
            long factoryPos = factory[j - 1][0];
            int limit = factory[j - 1][1];
            for (int i = 0; i <= n; i++) {
                dp[i][j] = dp[i][j - 1];
                long currentDist = 0;
                for (int k = 1; k <= limit && i - k >= 0; k++) {
                    currentDist += Math.abs((long) robot.get(i - k) - factoryPos);
                    if (dp[i - k][j - 1] != INF) {
                        dp[i][j] = Math.min(dp[i][j], dp[i - k][j - 1] + currentDist);
                    }
                }
            }
        }

        return dp[n][m];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        """
        :type robot: List[int]
        :type factory: List[List[int]]
        :rtype: int
        """
        robot.sort()
        factory.sort()
        n, m = len(robot), len(factory)
        INF = 10**15
        dp = [[INF] * (m + 1) for _ in range(n + 1)]

        for j in range(m + 1):
            dp[0][j] = 0

        for j in range(1, m + 1):
            pos, limit = factory[j-1]
            for i in range(n + 1):
                dp[i][j] = dp[i][j-1]
                current_dist = 0
                for k in range(1, min(i, limit) + 1):
                    current_dist += abs(robot[i-k] - pos)
                    if dp[i-k][j-1] != INF:
                        dp[i][j] = min(dp[i][j], dp[i-k][j-1] + current_dist)

        return dp[n][m]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        robot.sort()
        factory.sort()
        n, m = len(robot), len(factory)
        INF = 10**15
        dp = [[INF] * (n + 1) for _ in range(m + 1)]
        for j in range(m + 1):
            dp[j][0] = 0

        for j in range(1, m + 1):
            pos, limit = factory[j-1]
            for i in range(n + 1):
                dp[j][i] = dp[j-1][i]
                dist = 0
                for k in range(1, min(i, limit) + 1):
                    dist += abs(robot[i - k] - pos)
                    if dp[j-1][i - k] != INF:
                        if dp[j-1][i - k] + dist < dp[j][i]:
                            dp[j][i] = dp[j-1][i - k] + dist
        return dp[m][n]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>
#include <math.h>

int cmp_int(const void* a, const void* b) {
    int x = *(const int*)a;
    int y = *(const int*)b;
    if (x < y) return -1;
    if (x > y) return 1;
    return 0;
}

int cmp_factory(const void* a, const void* b) {
    const int* f1 = *(const int**)a;
    const int* f2 = *(const int**)b;
    if (f1[0] < f2[0]) return -1;
    if (f1[0] > f2[0]) return 1;
    return 0;
}

long long minimumTotalDistance(int* robot, int robotSize, int** factory, int factorySize, int* factoryColSize) {
    qsort(robot, robotSize, sizeof(int), cmp_int);
    qsort(factory, factorySize, sizeof(int*), cmp_factory);

    long long dp[101][101];
    long long INF = 1000000000000000LL;
    for (int j = 0; j <= factorySize; j++) {
        for (int i = 0; i <= robotSize; i++) {
            dp[j][i] = INF;
        }
        dp[j][0] = 0;
    }

    for (int j = 1; j <= factorySize; j++) {
        long long pos = factory[j - 1][0];
        int limit = factory[j - 1][1];
        for (int i = 1; i <= robotSize; i++) {
            dp[j][i] = dp[j - 1][i];
            long long dist = 0;
            for (int k = 1; k <= limit && k <= i; k++) {
                dist += llabs((long long)robot[i - k] - pos);
                if (dp[j - 1][i - k] != INF) {
                    if (dp[j - 1][i - k] + dist < dp[j][i]) {
                        dp[j][i] = dp[j - 1][i - k] + dist;
                    }
                }
            }
        }
    }

    return dp[factorySize][robotSize];
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
    public long MinimumTotalDistance(IList<int> robot, int[][] factory) {
        int[] sortedRobot = robot.ToArray();
        Array.Sort(sortedRobot);
        Array.Sort(factory, (a, b) => a[0].CompareTo(b[0]));
        int n = sortedRobot.Length;
        int m = factory.Length;
        long INF = 1000000000000000L;
        long[,] dp = new long[m + 1, n + 1];

        for (int j = 0; j <= m; j++) {
            for (int i = 0; i <= n; i++) {
                dp[j, i] = INF;
            }
            dp[j, 0] = 0;
        }

        for (int j = 1; j <= m; j++) {
            long pos = factory[j - 1][0];
            int limit = factory[j - 1][1];
            for (int i = 1; i <= n; i++) {
                dp[j, i] = dp[j - 1, i];
                long dist = 0;
                for (int k = 1; k <= limit && k <= i; k++) {
                    dist += Math.Abs((long)sortedRobot[i - k] - pos);
                    if (dp[j - 1, i - k] != INF) {
                        if (dp[j - 1, i - k] + dist < dp[j, i]) {
                            dp[j, i] = dp[j - 1, i - k] + dist;
                        }
                    }
                }
            }
        }

        return dp[m, n];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} robot
 * @param {number[][]} factory
 * @return {number}
 */
var minimumTotalDistance = function(robot, factory) {
    robot.sort((a, b) => a - b);
    factory.sort((a, b) => a[0] - b[0]);
    const n = robot.length;
    const m = factory.length;
    const INF = 1e15;
    const dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(INF));

    for (let j = 0; j <= m; j++) {
        dp[j][0] = 0;
    }

    for (let j = 1; j <= m; j++) {
        let [pos, limit] = factory[j - 1];
        for (let i = 1; i <= n; i++) {
            dp[j][i] = dp[j - 1][i];
            let dist = 0;
            for (let k = 1; k <= limit && k <= i; k++) {
                dist += Math.abs(robot[i - k] - pos);
                if (dp[j - 1][i - k] !== INF) {
                    if (dp[j - 1][i - k] + dist < dp[j][i]) {
                        dp[j][i] = dp[j - 1][i - k] + dist;
                    }
                }
            }
        }
    }

    return dp[m][n];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimumTotalDistance(robot: number[], factory: number[][]): number {
    robot.sort((a, b) => a - b);
    factory.sort((a, b) => a[0] - b[0]);

    const m = robot.length;
    const n = factory.length;
    const inf = 1000000000000000;
    const dp: number[][] = Array.from({ length: n + 1 }, () => Array(m + 1).fill(inf));

    for (let i = 0; i <= n; i++) {
        dp[i][0] = 0;
    }

    for (let i = 1; i <= n; i++) {
        const pos = factory[i - 1][0];
        const limit = factory[i - 1][1];
        for (let j = 0; j <= m; j++) {
            dp[i][j] = dp[i - 1][j];
            if (j > 0) {
                let cost = 0;
                const maxK = Math.min(j, limit);
                for (let k = 1; k <= maxK; k++) {
                    cost += Math.abs(robot[j - k] - pos);
                    if (dp[i - 1][j - k] !== inf) {
                        dp[i][j] = Math.min(dp[i][j], dp[i - 1][j - k] + cost);
                    }
                }
            }
        }
    }

    return dp[n][m];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $robot
     * @param Integer[][] $factory
     * @return Integer
     */
    function minimumTotalDistance($robot, $factory) {
        sort($robot);
        usort($factory, function($a, $b) {
            return $a[0] <=> $b[0];
        });

        $m = count($robot);
        $n = count($factory);
        $inf = 1000000000000000;
        $dp = array_fill(0, $n + 1, array_fill(0, $m + 1, $inf));

        for ($i = 0; $i <= $n; $i++) {
            $dp[$i][0] = 0;
        }

        for ($i = 1; $i <= $n; $i++) {
            $pos = $factory[$i - 1][0];
            $limit = $factory[$i - 1][1];
            for ($j = 0; $j <= $m; $j++) {
                $dp[$i][$j] = $dp[$i - 1][$j];
                if ($j > 0) {
                    $cost = 0;
                    $maxK = min($j, $limit);
                    for ($k = 1; $k <= $maxK; $k++) {
                        $cost += abs($robot[$j - $k] - $pos);
                        if ($dp[$i - 1][$j - $k] != $inf) {
                            $val = $dp[$i - 1][$j - $k] + $cost;
                            if ($val < $dp[$i][$j]) {
                                $dp[$i][$j] = $val;
                            }
                        }
                    }
                }
            }
        }

        return $dp[$n][$m];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minimumTotalDistance(_ robot: [Int], _ factory: [[Int]]) -> Int {
        let robotSorted = robot.sorted()
        let factorySorted = factory.sorted(by: { $0[0] < $1[0] })

        let m = robotSorted.count
        let n = factorySorted.count
        let inf = 1_000_000_000_000_000

        var dp = Array(repeating: Array(repeating: inf, count: m + 1), count: n + 1)

        for i in 0...n {
            dp[i][0] = 0
        }

        for i in 1...n {
            let pos = factorySorted[i - 1][0]
            let limit = factorySorted[i - 1][1]
            for j in 0...m {
                dp[i][j] = dp[i - 1][j]
                if j > 0 {
                    var cost = 0
                    let maxK = min(j, limit)
                    if maxK >= 1 {
                        for k in 1...maxK {
                            cost += abs(robotSorted[j - k] - pos)
                            if dp[i - 1][j - k] != inf {
                                dp[i][j] = min(dp[i][j], dp[i - 1][j - k] + cost)
                            }
                        }
                    }
                }
            }
        }

        return dp[n][m]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minimumTotalDistance(robot: List<Int>, factory: Array<IntArray>): Long {
        val robotSorted = robot.sorted()
        val factorySorted = factory.sortedBy { it[0] }

        val m = robotSorted.size
        val n = factorySorted.size
        val inf = 1_000_000_000_000_000L
        val dp = Array(n + 1) { LongArray(m + 1) { inf } }

        for (i in 0..n) {
            dp[i][0] = 0L
        }

        for (i in 1..n) {
            val pos = factorySorted[i - 1][0]
            val limit = factorySorted[i - 1][1]
            for (j in 0..m) {
                dp[i][j] = dp[i - 1][j]
                if (j > 0) {
                    var cost = 0L
                    val maxK = minOf(j, limit)
                    for (k in 1..maxK) {
                        cost += Math.abs(robotSorted[j - k].toLong() - pos.toLong())
                        if (dp[i - 1][j - k] != inf) {
                            dp[i][j] = minOf(dp[i][j], dp[i - 1][j - k] + cost)
                        }
                    }
                }
            }
        }

        return dp[n][m]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minimumTotalDistance(List<int> robot, List<List<int>> factory) {
    robot.sort();
    factory.sort((a, b) => a[0].compareTo(b[0]));
    int n = robot.length;
    const int INF = 1000000000000000;
    List<int> dp = List.filled(n + 1, INF);
    dp[0] = 0;

    for (var f in factory) {
      int pos = f[0];
      int limit = f[1];
      for (int i = n; i >= 1; i--) {
        int currentDist = 0;
        for (int k = 1; k <= limit && k <= i; k++) {
          currentDist += (robot[i - k] - pos).abs();
          if (dp[i - k] != INF) {
            if (dp[i - k] + currentDist < dp[i]) {
              dp[i] = dp[i - k] + currentDist;
            }
          }
        }
      }
    }
    return dp[n];
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

func minimumTotalDistance(robot []int, factory [][]int) int64 {
	sort.Ints(robot)
	sort.Slice(factory, func(i, j int) bool {
		return factory[i][0] < factory[j][0]
	})

	n := len(robot)
	const INF = int64(1e15)
	dp := make([]int64, n+1)
	for i := 1; i <= n; i++ {
		dp[i] = INF
	}
	dp[0] = 0

	for _, f := range factory {
		pos := int64(f[0])
		limit := f[1]
		for i := n; i >= 1; i-- {
			var currentDist int64
			for k := 1; k <= limit && k <= i; k++ {
				d := int64(robot[i-k]) - pos
				if d < 0 {
					d = -d
				}
				currentDist += d
				if dp[i-k] != INF {
					if val := dp[i-k] + currentDist; val < dp[i] {
						dp[i] = val
					}
				}
			}
		}
	}
	return dp[n]
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def minimum_total_distance(robot, factory)
  robot.sort!
  factory.sort_by! { |f| f[0] }
  n = robot.size
  inf = 10**15
  dp = Array.new(n + 1, inf)
  dp[0] = 0

  factory.each do |f|
    pos = f[0]
    limit = f[1]
    n.downto(1) do |i|
      current_dist = 0
      max_k = [limit, i].min
      1.upto(max_k) do |k|
        current_dist += (robot[i - k] - pos).abs
        if dp[i - k] != inf
          dp[i] = [dp[i], dp[i - k] + current_dist].min
        end
      end
    end
  end
  dp[n]
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def minimumTotalDistance(robot: List[Int], factory: Array[Array[Int]]): Long = {
    val robotArr = robot.sorted.toArray
    val sortedFactory = factory.sortBy(_(0))
    val n = robotArr.length
    val inf = 1000000000000000L
    val dp = Array.fill(n + 1)(inf)
    dp(0) = 0L

    for (f <- sortedFactory) {
      val pos = f(0).toLong
      val limit = f(1)
      for (i <- n to 1 by -1) {
        var currentDist = 0L
        val maxK = Math.min(limit, i)
        var k = 1
        while (k <= maxK) {
          currentDist += Math.abs(robotArr(i - k).toLong - pos)
          if (dp(i - k) != inf) {
            dp(i) = Math.min(dp(i), dp(i - k) + currentDist)
          }
          k += 1
        }
      }
    }
    dp(n)
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn minimum_total_distance(mut robot: Vec<i32>, mut factory: Vec<Vec<i32>>) -> i64 {
        robot.sort_unstable();
        factory.sort_unstable_by_key(|f| f[0]);
        let n = robot.len();
        let m = factory.len();
        let inf = 1_000_000_000_000_000i64;

        let mut dp = vec![vec![inf; m + 1]; n + 1];

        for j in 0..=m {
            dp[0][j] = 0;
        }

        for j in 1..=m {
            let f_pos = factory[j - 1][0] as i64;
            let f_limit = factory[j - 1][1] as usize;
            for i in 0..=n {
                dp[i][j] = dp[i][j - 1];
                let mut current_dist = 0;
                for k in 1..=f_limit {
                    if k > i { break; }
                    current_dist += (robot[i - k] as i64 - f_pos).abs();
                    if dp[i - k][j - 1] != inf {
                        dp[i][j] = std::cmp::min(dp[i][j], dp[i - k][j - 1] + current_dist);
                    }
                }
            }
        }

        dp[n][m]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (minimum-total-distance robot factory)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  (let* ([sorted-robot (sort robot <)]
         [sorted-factory (sort factory (lambda (a b) (< (car a) (car b))))]
         [n (length sorted-robot)]
         [m (length sorted-factory)]
         [inf 1000000000000000]
         [robot-vec (list->vector sorted-robot)]
         [factory-vec (list->vector (map list->vector sorted-factory))]
         [dp (build-vector (add1 n) (lambda (_) (make-vector (add1 m) inf)))])
    (for ([j (in-range (add1 m))])
      (vector-set! (vector-ref dp 0) j 0))
    (for ([j (in-range 1 (add1 m))])
      (let* ([f-entry (vector-ref factory-vec (sub1 j))]
             [f-pos (vector-ref f-entry 0)]
             [f-limit (vector-ref f-entry 1)])
        (for ([i (in-range 0 (add1 n))])
          (vector-set! (vector-ref dp i) j (vector-ref (vector-ref dp i) (sub1 j)))
          (let loop ([k 1] [current-dist 0])
            (when (and (<= k i) (<= k f-limit))
              (let* ([r-pos (vector-ref robot-vec (- i k))]
                     [new-dist (+ current-dist (abs (- r-pos f-pos)))]
                     [prev-val (vector-ref (vector-ref dp (- i k)) (sub1 j))])
                (when (< prev-val inf)
                  (let ([current-val (vector-ref (vector-ref dp i) j)]
                        [new-val (+ prev-val new-dist)])
                    (when (< new-val current-val)
                      (vector-set! (vector-ref dp i) j new-val))))
                (loop (add1 k) new-dist)))))))
    (vector-ref (vector-ref dp n) m)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec minimum_total_distance(Robot :: [integer()], Factory :: [[integer()]]) -> integer().
minimum_total_distance(Robot, Factory) ->
    SortedRobot = lists:sort(Robot),
    SortedFactory = lists:sort(fun([A, _], [B, _]) -> A < B end, Factory),
    RTuple = list_to_tuple(SortedRobot),
    FTuple = list_to_tuple(SortedFactory),
    {Result, _} = solve(0, 0, tuple_size(RTuple), tuple_size(FTuple), RTuple, FTuple, #{}),
    Result.

solve(RIdx, FIdx, RCount, FCount, _RTuple, _FTuple, Memo) when RIdx =:= RCount ->
    {0, Memo};
solve(_RIdx, FIdx, _RCount, FCount, _RTuple, _FTuple, Memo) when FIdx =:= FCount ->
    {1000000000000000, Memo};
solve(RIdx, FIdx, RCount, FCount, RTuple, FTuple, Memo) ->
    case maps:find({RIdx, FIdx}, Memo) of
        {ok, Val} -> {Val, Memo};
        error ->
            {ResSkip, Memo1} = solve(RIdx, FIdx + 1, RCount, FCount, RTuple, FTuple, Memo),
            [FPos, FLimit] = element(FIdx + 1, FTuple),
            {FinalRes, FinalMemo} = loop_k(1, FLimit, RIdx, FIdx, RCount, FCount, RTuple, FTuple, FPos, 0, ResSkip, Memo1),
            {FinalRes, maps:put({RIdx, FIdx}, FinalRes, FinalMemo)}
    end.

loop_k(K, Limit, RIdx, FIdx, RCount, FCount, RTuple, FTuple, FPos, AccDist, MinDist, Memo) ->
    if
        K =< Limit andalso RIdx + K =< RCount ->
            RobotPos = element(RIdx + K, RTuple),
            NewAccDist = AccDist + abs(RobotPos - FPos),
            {SubRes, NewMemo} = solve(RIdx + K, FIdx + 1, RCount, FCount, RTuple, FTuple, Memo),
            NewMinDist = min(MinDist, NewAccDist + SubRes),
            loop_k(K + 1, Limit, RIdx, FIdx, RCount, FCount, RTuple, FTuple, FPos, NewAccDist, NewMinDist, NewMemo);
        true ->
            {MinDist, Memo}
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_total_distance(robot :: [integer], factory :: [[integer]]) :: integer
  def minimum_total_distance(robot, factory) do
    r_sorted = Enum.sort(robot)
    f_sorted = Enum.sort_by(factory, fn [pos, _] -> pos end)
    r_tuple = List.to_tuple(r_sorted)
    f_tuple = List.to_tuple(f_sorted)
    {res, _} = solve(0, 0, tuple_size(r_tuple), tuple_size(f_tuple), r_tuple, f_tuple, %{})
    res
  end

  defp solve(r_idx, f_idx, r_count, _f_count, _r_tuple, _f_tuple, memo) when r_idx == r_count do
    {0, memo}
  end

  defp solve(_r_idx, f_idx, _r_count, f_count, _r_tuple, _f_tuple, memo) when f_idx == f_count do
    {1_000_000_000_000_000, memo}
  end

  defp solve(r_idx, f_idx, r_count, f_count, r_tuple, f_tuple, memo) do
    case Map.get(memo, {r_idx, f_idx}) do
      nil ->
        {res_skip, memo1} = solve(r_idx, f_idx + 1, r_count, f_count, r_tuple, f_tuple, memo)
        [f_pos, f_limit] = elem(f_tuple, f_idx)
        {res, memo2} = loop_k(1, f_limit, r_idx, f_idx, r_count, f_count, r_tuple, f_tuple, f_pos, 0, res_skip, memo1)
        {res, Map.put(memo2, {r_idx, f_idx}, res)}
      val ->
        {val, memo}
    end
  end

  defp loop_k(k, limit, r_idx, f_idx, r_count, f_count, r_tuple, f_tuple, f_pos, acc_dist, min_dist, memo) do
    if k <= limit and r_idx + k <= r_count do
      r_pos = elem(r_tuple, r_idx + k - 1)
      new_acc_dist = acc_dist + abs(r_pos - f_pos)
      {sub_res, next_memo} = solve(r_idx + k, f_idx + 1, r_count, f_count, r_tuple, f_tuple, memo)
      new_min_dist = min(min_dist, new_acc_dist + sub_res)
      loop_k(k + 1, limit, r_idx, f_idx, r_count, f_count, r_tuple, f_tuple, f_pos, new_acc_dist, new_min_dist, next_memo)
    else
      {min_dist, memo}
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(M * N^2) where N is the number of robots and M is the number of factories. We iterate through each of the M factories, and for each factory, we iterate through N possible robot counts. For each robot count, we check up to N robots that the current factory could potentially repair. This leads to a total of M * N states, each taking up to O(N) time to compute.
- **Space Complexity:** O(M * N) to store the DP table. Given that N and M are at most 100, the table size (10,000 elements) is well within memory limits. This space could be further optimized to O(N) because the current factory's calculation only depends on the previous factory's state.
