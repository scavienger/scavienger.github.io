---
layout: post
title: "Minimum Distance to Type a Word Using Two Fingers"
date: 2026-04-12 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["String", "Dynamic Programming"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minimumDistance(string word) {\n    \
        \    int n = word.length();\n        auto getDist = [](int a, int b) {\n   \
        \         if (a == 26 || b == 26) return 0;\n            return abs(a / 6 -\
        \ b / 6) + abs(a % 6 - b % 6);\n        };\n\n        vector<int> dp(27, 1000000);\n\
        \        dp[26] = 0;\n\n        for (int i = 0; i < n - 1; ++i) {\n        \
        \    int curr = word[i] - 'A';\n            int nxt = word[i + 1] - 'A';\n \
        \           vector<int> next_dp(27, 1000000);\n            for (int j = 0; j\
        \ < 27; ++j) {\n                if (dp[j] == 1000000) continue;\n\n        \
        \        int d1 = dp[j] + getDist(curr, nxt);\n                if (d1 < next_dp[j])\
        \ next_dp[j] = d1;\n\n                int d2 = dp[j] + getDist(j, nxt);\n  \
        \              if (d2 < next_dp[curr]) next_dp[curr] = d2;\n            }\n\
        \            dp = next_dp;\n        }\n\n        int res = 1000000;\n      \
        \  for (int d : dp) {\n            if (d < res) res = d;\n        }\n      \
        \  return res;\n    }\n};"
      java: "class Solution {\n    public int minimumDistance(String word) {\n     \
        \   int n = word.length();\n        int[] dp = new int[27];\n        java.util.Arrays.fill(dp,\
        \ 1000000);\n        dp[26] = 0;\n\n        for (int i = 0; i < n - 1; i++)\
        \ {\n            int curr = word.charAt(i) - 'A';\n            int nxt = word.charAt(i\
        \ + 1) - 'A';\n            int[] next_dp = new int[27];\n            java.util.Arrays.fill(next_dp,\
        \ 1000000);\n            for (int j = 0; j < 27; j++) {\n                if\
        \ (dp[j] == 1000000) continue;\n\n                int d1 = dp[j] + getDist(curr,\
        \ nxt);\n                if (d1 < next_dp[j]) next_dp[j] = d1;\n\n         \
        \       int d2 = dp[j] + getDist(j, nxt);\n                if (d2 < next_dp[curr])\
        \ next_dp[curr] = d2;\n            }\n            dp = next_dp;\n        }\n\
        \n        int res = 1000000;\n        for (int d : dp) {\n            if (d\
        \ < res) res = d;\n        }\n        return res;\n    }\n\n    private int\
        \ getDist(int a, int b) {\n        if (a == 26 || b == 26) return 0;\n     \
        \   return Math.abs(a / 6 - b / 6) + Math.abs(a % 6 - b % 6);\n    }\n}"
      python: "class Solution(object):\n    def minimumDistance(self, word):\n     \
        \   \"\"\"\n        :type word: str\n        :rtype: int\n        \"\"\"\n \
        \       def get_dist(a, b):\n            if a == 26 or b == 26:\n          \
        \      return 0\n            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)\n\
        \n        dp = [1000000] * 27\n        dp[26] = 0\n        n = len(word)\n\n\
        \        for i in range(n - 1):\n            curr = ord(word[i]) - ord('A')\n\
        \            nxt = ord(word[i+1]) - ord('A')\n            next_dp = [1000000]\
        \ * 27\n            for j in range(27):\n                if dp[j] == 1000000:\n\
        \                    continue\n\n                d1 = dp[j] + get_dist(curr,\
        \ nxt)\n                if d1 < next_dp[j]:\n                    next_dp[j]\
        \ = d1\n\n                d2 = dp[j] + get_dist(j, nxt)\n                if\
        \ d2 < next_dp[curr]:\n                    next_dp[curr] = d2\n            dp\
        \ = next_dp\n\n        return min(dp)"
      python3: "class Solution:\n    def minimumDistance(self, word: str) -> int:\n\
        \        def dist(a, b):\n            if a == 26:\n                return 0\n\
        \            r1, c1 = a // 6, a % 6\n            r2, c2 = b // 6, b % 6\n  \
        \          return abs(r1 - r2) + abs(c1 - c2)\n\n        dp = [1000000] * 27\n\
        \        dp[26] = 0\n        prev = ord(word[0]) - ord('A')\n\n        for i\
        \ in range(1, len(word)):\n            curr = ord(word[i]) - ord('A')\n    \
        \        next_dp = [1000000] * 27\n            for j in range(27):\n       \
        \         if dp[j] == 1000000:\n                    continue\n\n           \
        \     d1 = dp[j] + dist(prev, curr)\n                if d1 < next_dp[j]:\n \
        \                   next_dp[j] = d1\n\n                d2 = dp[j] + dist(j,\
        \ curr)\n                if d2 < next_dp[prev]:\n                    next_dp[prev]\
        \ = d2\n\n            dp = next_dp\n            prev = curr\n\n        return\
        \ min(dp)"
      c: "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint get_dist(int\
        \ a, int b) {\n    if (a == 26) return 0;\n    int r1 = a / 6, c1 = a % 6;\n\
        \    int r2 = b / 6, c2 = b % 6;\n    return abs(r1 - r2) + abs(c1 - c2);\n\
        }\n\nint minimumDistance(char* word) {\n    int n = strlen(word);\n    if (n\
        \ < 2) return 0;\n\n    int dp[27];\n    int next_dp[27];\n    for (int j =\
        \ 0; j < 27; j++) dp[j] = 1000000;\n\n    dp[26] = 0;\n    int prev = word[0]\
        \ - 'A';\n\n    for (int i = 1; i < n; i++) {\n        int curr = word[i] -\
        \ 'A';\n        for (int j = 0; j < 27; j++) next_dp[j] = 1000000;\n\n     \
        \   for (int j = 0; j < 27; j++) {\n            if (dp[j] == 1000000) continue;\n\
        \n            int d1 = dp[j] + get_dist(prev, curr);\n            if (d1 < next_dp[j])\
        \ next_dp[j] = d1;\n\n            int d2 = dp[j] + get_dist(j, curr);\n    \
        \        if (d2 < next_dp[prev]) next_dp[prev] = d2;\n        }\n        memcpy(dp,\
        \ next_dp, sizeof(int) * 27);\n        prev = curr;\n    }\n\n    int res =\
        \ 1000000;\n    for (int j = 0; j < 27; j++) {\n        if (dp[j] < res) res\
        \ = dp[j];\n    }\n    return res;\n}"
      csharp: "using System;\n\npublic class Solution {\n    private int GetDist(int\
        \ a, int b) {\n        if (a == 26) return 0;\n        int r1 = a / 6, c1 =\
        \ a % 6;\n        int r2 = b / 6, c2 = b % 6;\n        return Math.Abs(r1 -\
        \ r2) + Math.Abs(c1 - c2);\n    }\n\n    public int MinimumDistance(string word)\
        \ {\n        int n = word.Length;\n        if (n < 2) return 0;\n\n        int[]\
        \ dp = new int[27];\n        for (int j = 0; j < 27; j++) dp[j] = 1000000;\n\
        \n        dp[26] = 0;\n        int prev = word[0] - 'A';\n\n        for (int\
        \ i = 1; i < n; i++) {\n            int curr = word[i] - 'A';\n            int[]\
        \ nextDp = new int[27];\n            for (int j = 0; j < 27; j++) nextDp[j]\
        \ = 1000000;\n\n            for (int j = 0; j < 27; j++) {\n               \
        \ if (dp[j] == 1000000) continue;\n\n                int d1 = dp[j] + GetDist(prev,\
        \ curr);\n                if (d1 < nextDp[j]) nextDp[j] = d1;\n\n          \
        \      int d2 = dp[j] + GetDist(j, curr);\n                if (d2 < nextDp[prev])\
        \ nextDp[prev] = d2;\n            }\n            dp = nextDp;\n            prev\
        \ = curr;\n        }\n\n        int res = 1000000;\n        foreach (int d in\
        \ dp) {\n            if (d < res) res = d;\n        }\n        return res;\n\
        \    }\n}"
      javascript: "/**\n * @param {string} word\n * @return {number}\n */\nvar minimumDistance\
        \ = function(word) {\n    const getDist = (a, b) => {\n        if (a === 26)\
        \ return 0;\n        const r1 = Math.floor(a / 6), c1 = a % 6;\n        const\
        \ r2 = Math.floor(b / 6), c2 = b % 6;\n        return Math.abs(r1 - r2) + Math.abs(c1\
        \ - c2);\n    };\n\n    let n = word.length;\n    let dp = new Int32Array(27).fill(1000000);\n\
        \    dp[26] = 0;\n    let prev = word.charCodeAt(0) - 65;\n\n    for (let i\
        \ = 1; i < n; i++) {\n        let curr = word.charCodeAt(i) - 65;\n        let\
        \ nextDp = new Int32Array(27).fill(1000000);\n\n        for (let j = 0; j <=\
        \ 26; j++) {\n            if (dp[j] === 1000000) continue;\n\n            let\
        \ d1 = dp[j] + getDist(prev, curr);\n            if (d1 < nextDp[j]) nextDp[j]\
        \ = d1;\n\n            let d2 = dp[j] + getDist(j, curr);\n            if (d2\
        \ < nextDp[prev]) nextDp[prev] = d2;\n        }\n        dp = nextDp;\n    \
        \    prev = curr;\n    }\n\n    let res = 1000000;\n    for (let j = 0; j <=\
        \ 26; j++) {\n        if (dp[j] < res) res = dp[j];\n    }\n    return res;\n\
        };"
      typescript: "function minimumDistance(word: string): number {\n    const n: number\
        \ = word.length;\n    const getDist = (c1: number, c2: number): number => {\n\
        \        if (c1 === 26) return 0;\n        const r1: number = Math.floor(c1\
        \ / 6), col1: number = c1 % 6;\n        const r2: number = Math.floor(c2 / 6),\
        \ col2: number = c2 % 6;\n        return Math.abs(r1 - r2) + Math.abs(col1 -\
        \ col2);\n    };\n\n    let dp: Int32Array = new Int32Array(27).fill(1000000);\n\
        \    dp[26] = 0;\n\n    for (let i: number = 1; i < n; i++) {\n        const\
        \ prev: number = word.charCodeAt(i - 1) - 65;\n        const curr: number =\
        \ word.charCodeAt(i) - 65;\n        const nextDp: Int32Array = new Int32Array(27).fill(1000000);\n\
        \n        for (let j: number = 0; j <= 26; j++) {\n            if (dp[j] >=\
        \ 1000000) continue;\n\n            const dist1 = getDist(prev, curr);\n   \
        \         if (dp[j] + dist1 < nextDp[j]) {\n                nextDp[j] = dp[j]\
        \ + dist1;\n            }\n\n            const dist2 = getDist(j, curr);\n \
        \           if (dp[j] + dist2 < nextDp[prev]) {\n                nextDp[prev]\
        \ = dp[j] + dist2;\n            }\n        }\n        dp = nextDp;\n    }\n\n\
        \    let minVal: number = dp[0];\n    for (let k: number = 1; k < 27; k++) {\n\
        \        if (dp[k] < minVal) minVal = dp[k];\n    }\n    return minVal;\n}"
      php: "class Solution {\n\n    /**\n     * @param String $word\n     * @return\
        \ Integer\n     */\n    function minimumDistance($word) {\n        $n = strlen($word);\n\
        \        $dp = array_fill(0, 27, 1000000);\n        $dp[26] = 0;\n\n       \
        \ for ($i = 1; $i < $n; $i++) {\n            $prev = ord($word[$i - 1]) - 65;\n\
        \            $curr = ord($word[$i]) - 65;\n            $nextDp = array_fill(0,\
        \ 27, 1000000);\n            for ($j = 0; $j <= 26; $j++) {\n              \
        \  if ($dp[$j] >= 1000000) continue;\n\n                $d1 = $this->getDist($prev,\
        \ $curr);\n                if ($dp[$j] + $d1 < $nextDp[$j]) {\n            \
        \        $nextDp[$j] = $dp[$j] + $d1;\n                }\n\n               \
        \ $d2 = $this->getDist($j, $curr);\n                if ($dp[$j] + $d2 < $nextDp[$prev])\
        \ {\n                    $nextDp[$prev] = $dp[$j] + $d2;\n                }\n\
        \            }\n            $dp = $nextDp;\n        }\n\n        return min($dp);\n\
        \    }\n\n    private function getDist($c1, $c2) {\n        if ($c1 === 26)\
        \ return 0;\n        $r1 = intdiv($c1, 6);\n        $col1 = $c1 % 6;\n     \
        \   $r2 = intdiv($c2, 6);\n        $col2 = $c2 % 6;\n        return abs($r1\
        \ - $r2) + abs($col1 - $col2);\n    }\n}"
      swift: "class Solution {\n    func minimumDistance(_ word: String) -> Int {\n\
        \        let n = word.count\n        if n < 2 { return 0 }\n        let chars\
        \ = word.unicodeScalars.map { Int($0.value) - 65 }\n\n        func getDist(_\
        \ c1: Int, _ c2: Int) -> Int {\n            if c1 == 26 { return 0 }\n     \
        \       let r1 = c1 / 6, col1 = c1 % 6\n            let r2 = c2 / 6, col2 =\
        \ c2 % 6\n            return abs(r1 - r2) + abs(col1 - col2)\n        }\n\n\
        \        var dp = Array(repeating: 1000000, count: 27)\n        dp[26] = 0\n\
        \n        for i in 1..<n {\n            let prev = chars[i - 1]\n          \
        \  let curr = chars[i]\n            var nextDp = Array(repeating: 1000000, count:\
        \ 27)\n            for j in 0...26 {\n                if dp[j] >= 1000000 {\
        \ continue }\n\n                let d1 = getDist(prev, curr)\n             \
        \   if dp[j] + d1 < nextDp[j] {\n                    nextDp[j] = dp[j] + d1\n\
        \                }\n\n                let d2 = getDist(j, curr)\n          \
        \      if dp[j] + d2 < nextDp[prev] {\n                    nextDp[prev] = dp[j]\
        \ + d2\n                }\n            }\n            dp = nextDp\n        }\n\
        \n        return dp.min() ?? 0\n    }\n}"
      kotlin: "class Solution {\n    fun minimumDistance(word: String): Int {\n    \
        \    val n = word.length\n        val chars = IntArray(n) { word[it] - 'A' }\n\
        \n        fun getDist(c1: Int, c2: Int): Int {\n            if (c1 == 26) return\
        \ 0\n            val r1 = c1 / 6\n            val col1 = c1 % 6\n          \
        \  val r2 = c2 / 6\n            val col2 = c2 % 6\n            return Math.abs(r1\
        \ - r2) + Math.abs(col1 - col2)\n        }\n\n        var dp = IntArray(27)\
        \ { 1000000 }\n        dp[26] = 0\n\n        for (i in 1 until n) {\n      \
        \      val prev = chars[i - 1]\n            val curr = chars[i]\n          \
        \  val nextDp = IntArray(27) { 1000000 }\n            for (j in 0..26) {\n \
        \               if (dp[j] >= 1000000) continue\n\n                val dist1\
        \ = getDist(prev, curr)\n                if (dp[j] + dist1 < nextDp[j]) {\n\
        \                    nextDp[j] = dp[j] + dist1\n                }\n\n      \
        \          val dist2 = getDist(j, curr)\n                if (dp[j] + dist2 <\
        \ nextDp[prev]) {\n                    nextDp[prev] = dp[j] + dist2\n      \
        \          }\n            }\n            dp = nextDp\n        }\n\n        return\
        \ dp.minOrNull() ?: 0\n    }\n}"
      dart: "class Solution {\n  int minimumDistance(String word) {\n    int n = word.length;\n\
        \    List<int> dp = List.filled(27, 1000000);\n    dp[26] = 0;\n\n    int getDist(int\
        \ p1, int p2) {\n      if (p1 == 26 || p2 == 26) return 0;\n      return (p1\
        \ ~/ 6 - p2 ~/ 6).abs() + (p1 % 6 - p2 % 6).abs();\n    }\n\n    for (int i\
        \ = 1; i < n; i++) {\n      List<int> nextDp = List.filled(27, 1000000);\n \
        \     int curr = word.codeUnitAt(i) - 65;\n      int prev = word.codeUnitAt(i\
        \ - 1) - 65;\n      for (int j = 0; j < 27; j++) {\n        if (dp[j] == 1000000)\
        \ continue;\n        int d1 = getDist(prev, curr);\n        if (dp[j] + d1 <\
        \ nextDp[j]) nextDp[j] = dp[j] + d1;\n        int d2 = getDist(j, curr);\n \
        \       if (dp[j] + d2 < nextDp[prev]) nextDp[prev] = dp[j] + d2;\n      }\n\
        \      dp = nextDp;\n    }\n\n    int minDist = 1000000;\n    for (int d in\
        \ dp) {\n      if (d < minDist) minDist = d;\n    }\n    return minDist;\n \
        \ }\n}"
      go: "func minimumDistance(word string) int {\n    n := len(word)\n    dp := make([]int,\
        \ 27)\n    for i := range dp {\n        dp[i] = 1000000\n    }\n    dp[26] =\
        \ 0\n    abs := func(x int) int {\n        if x < 0 {\n            return -x\n\
        \        }\n        return x\n    }\n    getDist := func(p1, p2 int) int {\n\
        \        if p1 == 26 || p2 == 26 {\n            return 0\n        }\n      \
        \  r1, c1 := p1/6, p1%6\n        r2, c2 := p2/6, p2%6\n        return abs(r1-r2)\
        \ + abs(c1-c2)\n    }\n    for i := 1; i < n; i++ {\n        nextDp := make([]int,\
        \ 27)\n        for k := range nextDp {\n            nextDp[k] = 1000000\n  \
        \      }\n        curr := int(word[i] - 'A')\n        prev := int(word[i-1]\
        \ - 'A')\n        for j := 0; j < 27; j++ {\n            if dp[j] == 1000000\
        \ {\n                continue\n            }\n            d1 := getDist(prev,\
        \ curr)\n            if dp[j]+d1 < nextDp[j] {\n                nextDp[j] =\
        \ dp[j] + d1\n            }\n            d2 := getDist(j, curr)\n          \
        \  if dp[j]+d2 < nextDp[prev] {\n                nextDp[prev] = dp[j] + d2\n\
        \            }\n        }\n        dp = nextDp\n    }\n    minDist := 1000000\n\
        \    for _, v := range dp {\n        if v < minDist {\n            minDist =\
        \ v\n        }\n    }\n    return minDist\n}"
      ruby: "# @param {String} word\n# @return {Integer}\ndef minimum_distance(word)\n\
        \  n = word.length\n  dp = Array.new(27, 1000000)\n  dp[26] = 0\n  get_dist\
        \ = lambda do |p1, p2|\n    return 0 if p1 == 26 || p2 == 26\n    (p1 / 6 -\
        \ p2 / 6).abs + (p1 % 6 - p2 % 6).abs\n  end\n  (1...n).each do |i|\n    next_dp\
        \ = Array.new(27, 1000000)\n    curr = word[i].ord - 65\n    prev = word[i -\
        \ 1].ord - 65\n    (0..26).each do |j|\n      next if dp[j] == 1000000\n   \
        \   d1 = get_dist.call(prev, curr)\n      next_dp[j] = dp[j] + d1 if dp[j] +\
        \ d1 < next_dp[j]\n      d2 = get_dist.call(j, curr)\n      next_dp[prev] =\
        \ dp[j] + d2 if dp[j] + d2 < next_dp[prev]\n    end\n    dp = next_dp\n  end\n\
        \  dp.min\nend"
      scala: "object Solution {\n    def minimumDistance(word: String): Int = {\n  \
        \      val n = word.length\n        var dp = Array.fill(27)(1000000)\n     \
        \   dp(26) = 0\n        def getDist(p1: Int, p2: Int): Int = {\n           \
        \ if (p1 == 26 || p2 == 26) return 0\n            val r1 = p1 / 6\n        \
        \    val c1 = p1 % 6\n            val r2 = p2 / 6\n            val c2 = p2 %\
        \ 6\n            Math.abs(r1 - r2) + Math.abs(c1 - c2)\n        }\n        for\
        \ (i <- 1 until n) {\n            val nextDp = Array.fill(27)(1000000)\n   \
        \         val curr = word.charAt(i) - 'A'\n            val prev = word.charAt(i\
        \ - 1) - 'A'\n            for (j <- 0 to 26) {\n                if (dp(j) <\
        \ 1000000) {\n                    val d1 = getDist(prev, curr)\n           \
        \         if (dp(j) + d1 < nextDp(j)) {\n                        nextDp(j) =\
        \ dp(j) + d1\n                    }\n                    val d2 = getDist(j,\
        \ curr)\n                    if (dp(j) + d2 < nextDp(prev)) {\n            \
        \            nextDp(prev) = dp(j) + d2\n                    }\n            \
        \    }\n            }\n            dp = nextDp\n        }\n        dp.min\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn minimum_distance(word: String) -> i32 {\n \
        \       let n = word.len();\n        let chars: Vec<usize> = word.bytes().map(|b|\
        \ (b - b'A') as usize).collect();\n        let mut dp = vec![1_000_000; 27];\n\
        \        dp[26] = 0;\n\n        for i in 1..n {\n            let prev = chars[i\
        \ - 1];\n            let curr = chars[i];\n            let mut next_dp = vec![1_000_000;\
        \ 27];\n\n            for other in 0..27 {\n                let val = dp[other];\n\
        \                if val >= 1_000_000 {\n                    continue;\n    \
        \            }\n\n                let d1 = Self::dist(prev, curr);\n       \
        \         if val + d1 < next_dp[other] {\n                    next_dp[other]\
        \ = val + d1;\n                }\n\n                let d2 = Self::dist(other,\
        \ curr);\n                if val + d2 < next_dp[prev] {\n                  \
        \  next_dp[prev] = val + d2;\n                }\n            }\n           \
        \ dp = next_dp;\n        }\n\n        *dp.iter().min().unwrap()\n    }\n\n \
        \   fn dist(a: usize, b: usize) -> i32 {\n        if a == 26 {\n           \
        \ return 0;\n        }\n        let (r1, c1) = ((a / 6) as i32, (a % 6) as i32);\n\
        \        let (r2, c2) = ((b / 6) as i32, (b % 6) as i32);\n        (r1 - r2).abs()\
        \ + (c1 - c2).abs()\n    }\n}"
      racket: "(define/contract (minimum-distance word)\n  (-> string? exact-integer?)\n\
        \  (let* ([chars (map (lambda (c) (- (char->integer c) (char->integer #\\A)))\
        \ (string->list word))]\n         [dist (lambda (a b)\n                 (if\
        \ (= a 26)\n                     0\n                     (let ([r1 (quotient\
        \ a 6)]\n                           [c1 (remainder a 6)]\n                 \
        \          [r2 (quotient b 6)]\n                           [c2 (remainder b\
        \ 6)])\n                       (+ (abs (- r1 r2)) (abs (- c1 c2))))))])\n  \
        \  (let loop ([chars-left (cdr chars)]\n               [prev (car chars)]\n\
        \               [dp (let ([v (make-vector 27 1000000)])\n                  \
        \   (vector-set! v 26 0)\n                     v)])\n      (if (null? chars-left)\n\
        \          (apply min (vector->list dp))\n          (let* ([curr (car chars-left)]\n\
        \                 [next-dp (make-vector 27 1000000)])\n            (for ([other\
        \ (in-range 27)])\n              (let ([val (vector-ref dp other)])\n      \
        \          (when (< val 1000000)\n                  (let* ([d1 (dist prev curr)]\n\
        \                         [d2 (dist other curr)])\n                    (vector-set!\
        \ next-dp other (min (vector-ref next-dp other) (+ val d1)))\n             \
        \       (vector-set! next-dp prev (min (vector-ref next-dp prev) (+ val d2)))))))\n\
        \            (loop (cdr chars-left) curr next-dp))))))"
      erlang: "-spec minimum_distance(Word :: unicode:unicode_binary()) -> integer().\n\
        minimum_distance(Word) ->\n  Chars = [C - $A || C <- binary_to_list(Word)],\n\
        \  InitialDP = #{26 => 0},\n  [First | Rest] = Chars,\n  FinalDP = solve(Rest,\
        \ First, InitialDP),\n  lists:min(maps:values(FinalDP)).\n\nsolve([], _Prev,\
        \ DP) ->\n  DP;\nsolve([Curr | Rest], Prev, DP) ->\n  NextDP = update_dp(maps:to_list(DP),\
        \ Prev, Curr, #{}),\n  solve(Rest, Curr, NextDP).\n\nupdate_dp([], _Prev, _Curr,\
        \ NextDP) ->\n  NextDP;\nupdate_dp([{Other, Val} | Rest], Prev, Curr, NextDP)\
        \ ->\n  D1 = dist(Prev, Curr),\n  D2 = dist(Other, Curr),\n  V1 = Val + D1,\n\
        \  V2 = Val + D2,\n  NextDP1 = maps:put(Other, erlang:min(maps:get(Other, NextDP,\
        \ 1000000), V1), NextDP),\n  NextDP2 = maps:put(Prev, erlang:min(maps:get(Prev,\
        \ NextDP1, 1000000), V2), NextDP1),\n  update_dp(Rest, Prev, Curr, NextDP2).\n\
        \ndist(26, _) -> 0;\ndist(A, B) ->\n  abs(A div 6 - B div 6) + abs(A rem 6 -\
        \ B rem 6)."
      elixir: "defmodule Solution do\n  @spec minimum_distance(word :: String.t) ::\
        \ integer\n  def minimum_distance(word) do\n    chars = for <<c <- word>>, do:\
        \ c - ?A\n    [first | rest] = chars\n    dp = %{26 => 0}\n\n    final_dp =\
        \ Enum.reduce(rest, {first, dp}, fn curr, {prev, dp_acc} ->\n      new_dp =\
        \ Enum.reduce(dp_acc, %{}, fn {other, val}, next_dp ->\n        d1 = dist(prev,\
        \ curr)\n        d2 = dist(other, curr)\n\n        v1 = val + d1\n        next_dp\
        \ = Map.update(next_dp, other, v1, &min(&1, v1))\n\n        v2 = val + d2\n\
        \        Map.update(next_dp, prev, v2, &min(&1, v2))\n      end)\n      {curr,\
        \ new_dp}\n    end) |> elem(1)\n\n    Map.values(final_dp) |> Enum.min()\n \
        \ end\n\n  defp dist(26, _), do: 0\n  defp dist(a, b) do\n    r1 = div(a, 6)\n\
        \    c1 = rem(a, 6)\n    r2 = div(b, 6)\n    c2 = rem(b, 6)\n    abs(r1 - r2)\
        \ + abs(c1 - c2)\n  end\nend"
    approach: The problem can be solved using dynamic programming by observing that
      after typing a character, one of the two fingers must be positioned at that character.
      This allows us to reduce the state to dp[i][j], representing the minimum cost
      after typing the i-th character of the word, where j represents the position of
      the 'other' finger (the one not used to type the i-th character). We use a special
      state (index 26) to represent a finger that hasn't been placed on the keyboard
      yet. The initial state starts after typing the first character with one finger
      at word[0] and the other finger in the 'unplaced' state with a cost of 0.
    time_complexity: O(N * L) where N is the length of the word and L is the number
      of characters in the English alphabet (26). For each character in the word, we
      iterate through all 27 possible positions of the other finger to calculate the
      minimum cost for the next character.
    space_complexity: O(L) where L is the number of characters in the English alphabet
      (26). We only need to store the current and the next state of the DP table, both
      of which have a fixed size of 27.
    elapsed_time: 649.7685830593109
    model: gemini-3-flash-preview
    generated_at: '2026-04-12 02:05:15 '
---

## Problem #1320: Minimum Distance to Type a Word Using Two Fingers

**Difficulty:** Hard

**Topics:** String, Dynamic Programming

## Problem Description

<img alt="" src="https://assets.leetcode.com/uploads/2020/01/02/leetcode_keyboard.png" style="width: 349px; height: 209px;" />
<p>You have a keyboard layout as shown above in the <strong>X-Y</strong> plane, where each English uppercase letter is located at some coordinate.</p>

<ul>
	<li>For example, the letter <code>&#39;A&#39;</code> is located at coordinate <code>(0, 0)</code>, the letter <code>&#39;B&#39;</code> is located at coordinate <code>(0, 1)</code>, the letter <code>&#39;P&#39;</code> is located at coordinate <code>(2, 3)</code> and the letter <code>&#39;Z&#39;</code> is located at coordinate <code>(4, 1)</code>.</li>
</ul>

<p>Given the string <code>word</code>, return <em>the minimum total <strong>distance</strong> to type such string using only two fingers</em>.</p>

<p>The <strong>distance</strong> between coordinates <code>(x<sub>1</sub>, y<sub>1</sub>)</code> and <code>(x<sub>2</sub>, y<sub>2</sub>)</code> is <code>|x<sub>1</sub> - x<sub>2</sub>| + |y<sub>1</sub> - y<sub>2</sub>|</code>.</p>

<p><strong>Note</strong> that the initial positions of your two fingers are considered free so do not count towards your total distance, also your two fingers do not have to start at the first letter or the first two letters.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> word = &quot;CAKE&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> Using two fingers, one optimal way to type &quot;CAKE&quot; is: 
Finger 1 on letter &#39;C&#39; -&gt; cost = 0 
Finger 1 on letter &#39;A&#39; -&gt; cost = Distance from letter &#39;C&#39; to letter &#39;A&#39; = 2 
Finger 2 on letter &#39;K&#39; -&gt; cost = 0 
Finger 2 on letter &#39;E&#39; -&gt; cost = Distance from letter &#39;K&#39; to letter &#39;E&#39; = 1 
Total distance = 3
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> word = &quot;HAPPY&quot;
<strong>Output:</strong> 6
<strong>Explanation:</strong> Using two fingers, one optimal way to type &quot;HAPPY&quot; is:
Finger 1 on letter &#39;H&#39; -&gt; cost = 0
Finger 1 on letter &#39;A&#39; -&gt; cost = Distance from letter &#39;H&#39; to letter &#39;A&#39; = 2
Finger 2 on letter &#39;P&#39; -&gt; cost = 0
Finger 2 on letter &#39;P&#39; -&gt; cost = Distance from letter &#39;P&#39; to letter &#39;P&#39; = 0
Finger 1 on letter &#39;Y&#39; -&gt; cost = Distance from letter &#39;A&#39; to letter &#39;Y&#39; = 4
Total distance = 6
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= word.length &lt;= 300</code></li>
	<li><code>word</code> consists of uppercase English letters.</li>
</ul>


## Hints

1. Use dynamic programming.

2. dp[i][j][k]: smallest movements when you have one finger on i-th char and the other one on j-th char already having written k first characters from word.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be solved using dynamic programming by observing that after typing a character, one of the two fingers must be positioned at that character. This allows us to reduce the state to dp[i][j], representing the minimum cost after typing the i-th character of the word, where j represents the position of the 'other' finger (the one not used to type the i-th character). We use a special state (index 26) to represent a finger that hasn't been placed on the keyboard yet. The initial state starts after typing the first character with one finger at word[0] and the other finger in the 'unplaced' state with a cost of 0.

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
    int minimumDistance(string word) {
        int n = word.length();
        auto getDist = [](int a, int b) {
            if (a == 26 || b == 26) return 0;
            return abs(a / 6 - b / 6) + abs(a % 6 - b % 6);
        };

        vector<int> dp(27, 1000000);
        dp[26] = 0;

        for (int i = 0; i < n - 1; ++i) {
            int curr = word[i] - 'A';
            int nxt = word[i + 1] - 'A';
            vector<int> next_dp(27, 1000000);
            for (int j = 0; j < 27; ++j) {
                if (dp[j] == 1000000) continue;

                int d1 = dp[j] + getDist(curr, nxt);
                if (d1 < next_dp[j]) next_dp[j] = d1;

                int d2 = dp[j] + getDist(j, nxt);
                if (d2 < next_dp[curr]) next_dp[curr] = d2;
            }
            dp = next_dp;
        }

        int res = 1000000;
        for (int d : dp) {
            if (d < res) res = d;
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
    public int minimumDistance(String word) {
        int n = word.length();
        int[] dp = new int[27];
        java.util.Arrays.fill(dp, 1000000);
        dp[26] = 0;

        for (int i = 0; i < n - 1; i++) {
            int curr = word.charAt(i) - 'A';
            int nxt = word.charAt(i + 1) - 'A';
            int[] next_dp = new int[27];
            java.util.Arrays.fill(next_dp, 1000000);
            for (int j = 0; j < 27; j++) {
                if (dp[j] == 1000000) continue;

                int d1 = dp[j] + getDist(curr, nxt);
                if (d1 < next_dp[j]) next_dp[j] = d1;

                int d2 = dp[j] + getDist(j, nxt);
                if (d2 < next_dp[curr]) next_dp[curr] = d2;
            }
            dp = next_dp;
        }

        int res = 1000000;
        for (int d : dp) {
            if (d < res) res = d;
        }
        return res;
    }

    private int getDist(int a, int b) {
        if (a == 26 || b == 26) return 0;
        return Math.abs(a / 6 - b / 6) + Math.abs(a % 6 - b % 6);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minimumDistance(self, word):
        """
        :type word: str
        :rtype: int
        """
        def get_dist(a, b):
            if a == 26 or b == 26:
                return 0
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)

        dp = [1000000] * 27
        dp[26] = 0
        n = len(word)

        for i in range(n - 1):
            curr = ord(word[i]) - ord('A')
            nxt = ord(word[i+1]) - ord('A')
            next_dp = [1000000] * 27
            for j in range(27):
                if dp[j] == 1000000:
                    continue

                d1 = dp[j] + get_dist(curr, nxt)
                if d1 < next_dp[j]:
                    next_dp[j] = d1

                d2 = dp[j] + get_dist(j, nxt)
                if d2 < next_dp[curr]:
                    next_dp[curr] = d2
            dp = next_dp

        return min(dp)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(a, b):
            if a == 26:
                return 0
            r1, c1 = a // 6, a % 6
            r2, c2 = b // 6, b % 6
            return abs(r1 - r2) + abs(c1 - c2)

        dp = [1000000] * 27
        dp[26] = 0
        prev = ord(word[0]) - ord('A')

        for i in range(1, len(word)):
            curr = ord(word[i]) - ord('A')
            next_dp = [1000000] * 27
            for j in range(27):
                if dp[j] == 1000000:
                    continue

                d1 = dp[j] + dist(prev, curr)
                if d1 < next_dp[j]:
                    next_dp[j] = d1

                d2 = dp[j] + dist(j, curr)
                if d2 < next_dp[prev]:
                    next_dp[prev] = d2

            dp = next_dp
            prev = curr

        return min(dp)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int get_dist(int a, int b) {
    if (a == 26) return 0;
    int r1 = a / 6, c1 = a % 6;
    int r2 = b / 6, c2 = b % 6;
    return abs(r1 - r2) + abs(c1 - c2);
}

int minimumDistance(char* word) {
    int n = strlen(word);
    if (n < 2) return 0;

    int dp[27];
    int next_dp[27];
    for (int j = 0; j < 27; j++) dp[j] = 1000000;

    dp[26] = 0;
    int prev = word[0] - 'A';

    for (int i = 1; i < n; i++) {
        int curr = word[i] - 'A';
        for (int j = 0; j < 27; j++) next_dp[j] = 1000000;

        for (int j = 0; j < 27; j++) {
            if (dp[j] == 1000000) continue;

            int d1 = dp[j] + get_dist(prev, curr);
            if (d1 < next_dp[j]) next_dp[j] = d1;

            int d2 = dp[j] + get_dist(j, curr);
            if (d2 < next_dp[prev]) next_dp[prev] = d2;
        }
        memcpy(dp, next_dp, sizeof(int) * 27);
        prev = curr;
    }

    int res = 1000000;
    for (int j = 0; j < 27; j++) {
        if (dp[j] < res) res = dp[j];
    }
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    private int GetDist(int a, int b) {
        if (a == 26) return 0;
        int r1 = a / 6, c1 = a % 6;
        int r2 = b / 6, c2 = b % 6;
        return Math.Abs(r1 - r2) + Math.Abs(c1 - c2);
    }

    public int MinimumDistance(string word) {
        int n = word.Length;
        if (n < 2) return 0;

        int[] dp = new int[27];
        for (int j = 0; j < 27; j++) dp[j] = 1000000;

        dp[26] = 0;
        int prev = word[0] - 'A';

        for (int i = 1; i < n; i++) {
            int curr = word[i] - 'A';
            int[] nextDp = new int[27];
            for (int j = 0; j < 27; j++) nextDp[j] = 1000000;

            for (int j = 0; j < 27; j++) {
                if (dp[j] == 1000000) continue;

                int d1 = dp[j] + GetDist(prev, curr);
                if (d1 < nextDp[j]) nextDp[j] = d1;

                int d2 = dp[j] + GetDist(j, curr);
                if (d2 < nextDp[prev]) nextDp[prev] = d2;
            }
            dp = nextDp;
            prev = curr;
        }

        int res = 1000000;
        foreach (int d in dp) {
            if (d < res) res = d;
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
 * @param {string} word
 * @return {number}
 */
var minimumDistance = function(word) {
    const getDist = (a, b) => {
        if (a === 26) return 0;
        const r1 = Math.floor(a / 6), c1 = a % 6;
        const r2 = Math.floor(b / 6), c2 = b % 6;
        return Math.abs(r1 - r2) + Math.abs(c1 - c2);
    };

    let n = word.length;
    let dp = new Int32Array(27).fill(1000000);
    dp[26] = 0;
    let prev = word.charCodeAt(0) - 65;

    for (let i = 1; i < n; i++) {
        let curr = word.charCodeAt(i) - 65;
        let nextDp = new Int32Array(27).fill(1000000);

        for (let j = 0; j <= 26; j++) {
            if (dp[j] === 1000000) continue;

            let d1 = dp[j] + getDist(prev, curr);
            if (d1 < nextDp[j]) nextDp[j] = d1;

            let d2 = dp[j] + getDist(j, curr);
            if (d2 < nextDp[prev]) nextDp[prev] = d2;
        }
        dp = nextDp;
        prev = curr;
    }

    let res = 1000000;
    for (let j = 0; j <= 26; j++) {
        if (dp[j] < res) res = dp[j];
    }
    return res;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimumDistance(word: string): number {
    const n: number = word.length;
    const getDist = (c1: number, c2: number): number => {
        if (c1 === 26) return 0;
        const r1: number = Math.floor(c1 / 6), col1: number = c1 % 6;
        const r2: number = Math.floor(c2 / 6), col2: number = c2 % 6;
        return Math.abs(r1 - r2) + Math.abs(col1 - col2);
    };

    let dp: Int32Array = new Int32Array(27).fill(1000000);
    dp[26] = 0;

    for (let i: number = 1; i < n; i++) {
        const prev: number = word.charCodeAt(i - 1) - 65;
        const curr: number = word.charCodeAt(i) - 65;
        const nextDp: Int32Array = new Int32Array(27).fill(1000000);

        for (let j: number = 0; j <= 26; j++) {
            if (dp[j] >= 1000000) continue;

            const dist1 = getDist(prev, curr);
            if (dp[j] + dist1 < nextDp[j]) {
                nextDp[j] = dp[j] + dist1;
            }

            const dist2 = getDist(j, curr);
            if (dp[j] + dist2 < nextDp[prev]) {
                nextDp[prev] = dp[j] + dist2;
            }
        }
        dp = nextDp;
    }

    let minVal: number = dp[0];
    for (let k: number = 1; k < 27; k++) {
        if (dp[k] < minVal) minVal = dp[k];
    }
    return minVal;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String $word
     * @return Integer
     */
    function minimumDistance($word) {
        $n = strlen($word);
        $dp = array_fill(0, 27, 1000000);
        $dp[26] = 0;

        for ($i = 1; $i < $n; $i++) {
            $prev = ord($word[$i - 1]) - 65;
            $curr = ord($word[$i]) - 65;
            $nextDp = array_fill(0, 27, 1000000);
            for ($j = 0; $j <= 26; $j++) {
                if ($dp[$j] >= 1000000) continue;

                $d1 = $this->getDist($prev, $curr);
                if ($dp[$j] + $d1 < $nextDp[$j]) {
                    $nextDp[$j] = $dp[$j] + $d1;
                }

                $d2 = $this->getDist($j, $curr);
                if ($dp[$j] + $d2 < $nextDp[$prev]) {
                    $nextDp[$prev] = $dp[$j] + $d2;
                }
            }
            $dp = $nextDp;
        }

        return min($dp);
    }

    private function getDist($c1, $c2) {
        if ($c1 === 26) return 0;
        $r1 = intdiv($c1, 6);
        $col1 = $c1 % 6;
        $r2 = intdiv($c2, 6);
        $col2 = $c2 % 6;
        return abs($r1 - $r2) + abs($col1 - $col2);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minimumDistance(_ word: String) -> Int {
        let n = word.count
        if n < 2 { return 0 }
        let chars = word.unicodeScalars.map { Int($0.value) - 65 }

        func getDist(_ c1: Int, _ c2: Int) -> Int {
            if c1 == 26 { return 0 }
            let r1 = c1 / 6, col1 = c1 % 6
            let r2 = c2 / 6, col2 = c2 % 6
            return abs(r1 - r2) + abs(col1 - col2)
        }

        var dp = Array(repeating: 1000000, count: 27)
        dp[26] = 0

        for i in 1..<n {
            let prev = chars[i - 1]
            let curr = chars[i]
            var nextDp = Array(repeating: 1000000, count: 27)
            for j in 0...26 {
                if dp[j] >= 1000000 { continue }

                let d1 = getDist(prev, curr)
                if dp[j] + d1 < nextDp[j] {
                    nextDp[j] = dp[j] + d1
                }

                let d2 = getDist(j, curr)
                if dp[j] + d2 < nextDp[prev] {
                    nextDp[prev] = dp[j] + d2
                }
            }
            dp = nextDp
        }

        return dp.min() ?? 0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minimumDistance(word: String): Int {
        val n = word.length
        val chars = IntArray(n) { word[it] - 'A' }

        fun getDist(c1: Int, c2: Int): Int {
            if (c1 == 26) return 0
            val r1 = c1 / 6
            val col1 = c1 % 6
            val r2 = c2 / 6
            val col2 = c2 % 6
            return Math.abs(r1 - r2) + Math.abs(col1 - col2)
        }

        var dp = IntArray(27) { 1000000 }
        dp[26] = 0

        for (i in 1 until n) {
            val prev = chars[i - 1]
            val curr = chars[i]
            val nextDp = IntArray(27) { 1000000 }
            for (j in 0..26) {
                if (dp[j] >= 1000000) continue

                val dist1 = getDist(prev, curr)
                if (dp[j] + dist1 < nextDp[j]) {
                    nextDp[j] = dp[j] + dist1
                }

                val dist2 = getDist(j, curr)
                if (dp[j] + dist2 < nextDp[prev]) {
                    nextDp[prev] = dp[j] + dist2
                }
            }
            dp = nextDp
        }

        return dp.minOrNull() ?: 0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minimumDistance(String word) {
    int n = word.length;
    List<int> dp = List.filled(27, 1000000);
    dp[26] = 0;

    int getDist(int p1, int p2) {
      if (p1 == 26 || p2 == 26) return 0;
      return (p1 ~/ 6 - p2 ~/ 6).abs() + (p1 % 6 - p2 % 6).abs();
    }

    for (int i = 1; i < n; i++) {
      List<int> nextDp = List.filled(27, 1000000);
      int curr = word.codeUnitAt(i) - 65;
      int prev = word.codeUnitAt(i - 1) - 65;
      for (int j = 0; j < 27; j++) {
        if (dp[j] == 1000000) continue;
        int d1 = getDist(prev, curr);
        if (dp[j] + d1 < nextDp[j]) nextDp[j] = dp[j] + d1;
        int d2 = getDist(j, curr);
        if (dp[j] + d2 < nextDp[prev]) nextDp[prev] = dp[j] + d2;
      }
      dp = nextDp;
    }

    int minDist = 1000000;
    for (int d in dp) {
      if (d < minDist) minDist = d;
    }
    return minDist;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minimumDistance(word string) int {
    n := len(word)
    dp := make([]int, 27)
    for i := range dp {
        dp[i] = 1000000
    }
    dp[26] = 0
    abs := func(x int) int {
        if x < 0 {
            return -x
        }
        return x
    }
    getDist := func(p1, p2 int) int {
        if p1 == 26 || p2 == 26 {
            return 0
        }
        r1, c1 := p1/6, p1%6
        r2, c2 := p2/6, p2%6
        return abs(r1-r2) + abs(c1-c2)
    }
    for i := 1; i < n; i++ {
        nextDp := make([]int, 27)
        for k := range nextDp {
            nextDp[k] = 1000000
        }
        curr := int(word[i] - 'A')
        prev := int(word[i-1] - 'A')
        for j := 0; j < 27; j++ {
            if dp[j] == 1000000 {
                continue
            }
            d1 := getDist(prev, curr)
            if dp[j]+d1 < nextDp[j] {
                nextDp[j] = dp[j] + d1
            }
            d2 := getDist(j, curr)
            if dp[j]+d2 < nextDp[prev] {
                nextDp[prev] = dp[j] + d2
            }
        }
        dp = nextDp
    }
    minDist := 1000000
    for _, v := range dp {
        if v < minDist {
            minDist = v
        }
    }
    return minDist
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String} word
# @return {Integer}
def minimum_distance(word)
  n = word.length
  dp = Array.new(27, 1000000)
  dp[26] = 0
  get_dist = lambda do |p1, p2|
    return 0 if p1 == 26 || p2 == 26
    (p1 / 6 - p2 / 6).abs + (p1 % 6 - p2 % 6).abs
  end
  (1...n).each do |i|
    next_dp = Array.new(27, 1000000)
    curr = word[i].ord - 65
    prev = word[i - 1].ord - 65
    (0..26).each do |j|
      next if dp[j] == 1000000
      d1 = get_dist.call(prev, curr)
      next_dp[j] = dp[j] + d1 if dp[j] + d1 < next_dp[j]
      d2 = get_dist.call(j, curr)
      next_dp[prev] = dp[j] + d2 if dp[j] + d2 < next_dp[prev]
    end
    dp = next_dp
  end
  dp.min
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minimumDistance(word: String): Int = {
        val n = word.length
        var dp = Array.fill(27)(1000000)
        dp(26) = 0
        def getDist(p1: Int, p2: Int): Int = {
            if (p1 == 26 || p2 == 26) return 0
            val r1 = p1 / 6
            val c1 = p1 % 6
            val r2 = p2 / 6
            val c2 = p2 % 6
            Math.abs(r1 - r2) + Math.abs(c1 - c2)
        }
        for (i <- 1 until n) {
            val nextDp = Array.fill(27)(1000000)
            val curr = word.charAt(i) - 'A'
            val prev = word.charAt(i - 1) - 'A'
            for (j <- 0 to 26) {
                if (dp(j) < 1000000) {
                    val d1 = getDist(prev, curr)
                    if (dp(j) + d1 < nextDp(j)) {
                        nextDp(j) = dp(j) + d1
                    }
                    val d2 = getDist(j, curr)
                    if (dp(j) + d2 < nextDp(prev)) {
                        nextDp(prev) = dp(j) + d2
                    }
                }
            }
            dp = nextDp
        }
        dp.min
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn minimum_distance(word: String) -> i32 {
        let n = word.len();
        let chars: Vec<usize> = word.bytes().map(|b| (b - b'A') as usize).collect();
        let mut dp = vec![1_000_000; 27];
        dp[26] = 0;

        for i in 1..n {
            let prev = chars[i - 1];
            let curr = chars[i];
            let mut next_dp = vec![1_000_000; 27];

            for other in 0..27 {
                let val = dp[other];
                if val >= 1_000_000 {
                    continue;
                }

                let d1 = Self::dist(prev, curr);
                if val + d1 < next_dp[other] {
                    next_dp[other] = val + d1;
                }

                let d2 = Self::dist(other, curr);
                if val + d2 < next_dp[prev] {
                    next_dp[prev] = val + d2;
                }
            }
            dp = next_dp;
        }

        *dp.iter().min().unwrap()
    }

    fn dist(a: usize, b: usize) -> i32 {
        if a == 26 {
            return 0;
        }
        let (r1, c1) = ((a / 6) as i32, (a % 6) as i32);
        let (r2, c2) = ((b / 6) as i32, (b % 6) as i32);
        (r1 - r2).abs() + (c1 - c2).abs()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (minimum-distance word)
  (-> string? exact-integer?)
  (let* ([chars (map (lambda (c) (- (char->integer c) (char->integer #\A))) (string->list word))]
         [dist (lambda (a b)
                 (if (= a 26)
                     0
                     (let ([r1 (quotient a 6)]
                           [c1 (remainder a 6)]
                           [r2 (quotient b 6)]
                           [c2 (remainder b 6)])
                       (+ (abs (- r1 r2)) (abs (- c1 c2))))))])
    (let loop ([chars-left (cdr chars)]
               [prev (car chars)]
               [dp (let ([v (make-vector 27 1000000)])
                     (vector-set! v 26 0)
                     v)])
      (if (null? chars-left)
          (apply min (vector->list dp))
          (let* ([curr (car chars-left)]
                 [next-dp (make-vector 27 1000000)])
            (for ([other (in-range 27)])
              (let ([val (vector-ref dp other)])
                (when (< val 1000000)
                  (let* ([d1 (dist prev curr)]
                         [d2 (dist other curr)])
                    (vector-set! next-dp other (min (vector-ref next-dp other) (+ val d1)))
                    (vector-set! next-dp prev (min (vector-ref next-dp prev) (+ val d2)))))))
            (loop (cdr chars-left) curr next-dp))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec minimum_distance(Word :: unicode:unicode_binary()) -> integer().
minimum_distance(Word) ->
  Chars = [C - $A || C <- binary_to_list(Word)],
  InitialDP = #{26 => 0},
  [First | Rest] = Chars,
  FinalDP = solve(Rest, First, InitialDP),
  lists:min(maps:values(FinalDP)).

solve([], _Prev, DP) ->
  DP;
solve([Curr | Rest], Prev, DP) ->
  NextDP = update_dp(maps:to_list(DP), Prev, Curr, #{}),
  solve(Rest, Curr, NextDP).

update_dp([], _Prev, _Curr, NextDP) ->
  NextDP;
update_dp([{Other, Val} | Rest], Prev, Curr, NextDP) ->
  D1 = dist(Prev, Curr),
  D2 = dist(Other, Curr),
  V1 = Val + D1,
  V2 = Val + D2,
  NextDP1 = maps:put(Other, erlang:min(maps:get(Other, NextDP, 1000000), V1), NextDP),
  NextDP2 = maps:put(Prev, erlang:min(maps:get(Prev, NextDP1, 1000000), V2), NextDP1),
  update_dp(Rest, Prev, Curr, NextDP2).

dist(26, _) -> 0;
dist(A, B) ->
  abs(A div 6 - B div 6) + abs(A rem 6 - B rem 6).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_distance(word :: String.t) :: integer
  def minimum_distance(word) do
    chars = for <<c <- word>>, do: c - ?A
    [first | rest] = chars
    dp = %{26 => 0}

    final_dp = Enum.reduce(rest, {first, dp}, fn curr, {prev, dp_acc} ->
      new_dp = Enum.reduce(dp_acc, %{}, fn {other, val}, next_dp ->
        d1 = dist(prev, curr)
        d2 = dist(other, curr)

        v1 = val + d1
        next_dp = Map.update(next_dp, other, v1, &min(&1, v1))

        v2 = val + d2
        Map.update(next_dp, prev, v2, &min(&1, v2))
      end)
      {curr, new_dp}
    end) |> elem(1)

    Map.values(final_dp) |> Enum.min()
  end

  defp dist(26, _), do: 0
  defp dist(a, b) do
    r1 = div(a, 6)
    c1 = rem(a, 6)
    r2 = div(b, 6)
    c2 = rem(b, 6)
    abs(r1 - r2) + abs(c1 - c2)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N * L) where N is the length of the word and L is the number of characters in the English alphabet (26). For each character in the word, we iterate through all 27 possible positions of the other finger to calculate the minimum cost for the next character.
- **Space Complexity:** O(L) where L is the number of characters in the English alphabet (26). We only need to store the current and the next state of the DP table, both of which have a fixed size of 27.
