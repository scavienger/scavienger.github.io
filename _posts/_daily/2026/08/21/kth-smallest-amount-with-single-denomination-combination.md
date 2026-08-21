---
layout: post
title: "Kth Smallest Amount With Single Denomination Combination"
date: 2026-08-21 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Math", "Binary Search", "Bit Manipulation", "Combinatorics", "Number Theory"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    long long findKthSmallest(vector<int>& coins,\
        \ int k) {\n        sort(coins.begin(), coins.end());\n        vector<int> filtered;\n\
        \        for (int i = 0; i < coins.size(); ++i) {\n            bool redundant\
        \ = false;\n            for (int j = 0; j < i; ++j) {\n                if (coins[i]\
        \ % coins[j] == 0) {\n                    redundant = true;\n              \
        \      break;\n                }\n            }\n            if (!redundant)\
        \ filtered.push_back(coins[i]);\n        }\n\n        long long limit = (long\
        \ long)filtered[0] * k;\n        vector<pair<long long, int>> subsetsLcm;\n\
        \        function<void(int, long long, int)> generate = [&](int idx, long long\
        \ currentLcm, int count) {\n            for (int i = idx; i < filtered.size();\
        \ ++i) {\n                long long g = std::gcd(currentLcm, (long long)filtered[i]);\n\
        \                long long nextLcm = (currentLcm / g) * filtered[i];\n     \
        \           if (nextLcm <= limit) {\n                    int sign = ((count\
        \ + 1) % 2 == 1) ? 1 : -1;\n                    subsetsLcm.push_back({nextLcm,\
        \ sign});\n                    generate(i + 1, nextLcm, count + 1);\n      \
        \          }\n            }\n        };\n        generate(0, 1, 0);\n\n    \
        \    long long low = 1, high = limit, ans = limit;\n        while (low <= high)\
        \ {\n            long long mid = low + (high - low) / 2;\n            long long\
        \ cnt = 0;\n            for (auto& item : subsetsLcm) {\n                cnt\
        \ += item.second * (mid / item.first);\n            }\n            if (cnt >=\
        \ k) {\n                ans = mid;\n                high = mid - 1;\n      \
        \      } else {\n                low = mid + 1;\n            }\n        }\n\
        \        return ans;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public long findKthSmallest(int[]\
        \ coins, int k) {\n        Arrays.sort(coins);\n        List<Integer> filtered\
        \ = new ArrayList<>();\n        for (int i = 0; i < coins.length; i++) {\n \
        \           boolean redundant = false;\n            for (int j = 0; j < i; j++)\
        \ {\n                if (coins[i] % coins[j] == 0) {\n                    redundant\
        \ = true;\n                    break;\n                }\n            }\n  \
        \          if (!redundant) filtered.add(coins[i]);\n        }\n\n        long\
        \ limit = (long) filtered.get(0) * k;\n        List<long[]> subsetsLcm = new\
        \ ArrayList<>();\n        generateLcm(0, 1, 0, filtered, subsetsLcm, limit);\n\
        \n        long low = 1, high = limit, ans = limit;\n        while (low <= high)\
        \ {\n            long mid = low + (high - low) / 2;\n            long count\
        \ = 0;\n            for (long[] item : subsetsLcm) {\n                count\
        \ += item[1] * (mid / item[0]);\n            }\n            if (count >= (long)\
        \ k) {\n                ans = mid;\n                high = mid - 1;\n      \
        \      } else {\n                low = mid + 1;\n            }\n        }\n\
        \        return ans;\n    }\n\n    private void generateLcm(int idx, long currentLcm,\
        \ int count, List<Integer> filtered, List<long[]> subsetsLcm, long limit) {\n\
        \        for (int i = idx; i < filtered.size(); i++) {\n            long coin\
        \ = filtered.get(i);\n            long g = gcd(currentLcm, coin);\n        \
        \    long nextLcm = (currentLcm / g) * coin;\n            if (nextLcm <= limit)\
        \ {\n                int sign = ((count + 1) % 2 == 1) ? 1 : -1;\n         \
        \       subsetsLcm.add(new long[]{nextLcm, sign});\n                generateLcm(i\
        \ + 1, nextLcm, count + 1, filtered, subsetsLcm, limit);\n            }\n  \
        \      }\n    }\n\n    private long gcd(long a, long b) {\n        while (b\
        \ != 0) {\n            long temp = b;\n            b = a % b;\n            a\
        \ = temp;\n        }\n        return a;\n    }\n}"
      python: "import math\n\nclass Solution(object):\n    def findKthSmallest(self,\
        \ coins, k):\n        \"\"\"\n        :type coins: List[int]\n        :type\
        \ k: int\n        :rtype: int\n        \"\"\"\n        coins.sort()\n      \
        \  filtered = []\n        for i in range(len(coins)):\n            redundant\
        \ = False\n            for j in range(i):\n                if coins[i] % coins[j]\
        \ == 0:\n                    redundant = True\n                    break\n \
        \           if not redundant:\n                filtered.append(coins[i])\n\n\
        \        n = len(filtered)\n        limit = filtered[0] * k\n        subsets_lcm\
        \ = []\n\n        def generate_lcm(idx, current_lcm, count):\n            for\
        \ i in range(idx, n):\n                coin = filtered[i]\n                g\
        \ = math.gcd(current_lcm, coin)\n                next_lcm = (current_lcm //\
        \ g) * coin\n                if next_lcm <= limit:\n                    sign\
        \ = 1 if (count + 1) % 2 == 1 else -1\n                    subsets_lcm.append((next_lcm,\
        \ sign))\n                    generate_lcm(i + 1, next_lcm, count + 1)\n\n \
        \       generate_lcm(0, 1, 0)\n\n        plus = [l for l, s in subsets_lcm if\
        \ s == 1]\n        minus = [l for l, s in subsets_lcm if s == -1]\n\n      \
        \  low, high = 1, limit\n        ans = limit\n        while low <= high:\n \
        \           mid = (low + high) // 2\n            cnt = sum(mid // l for l in\
        \ plus) - sum(mid // l for l in minus)\n            if cnt >= k:\n         \
        \       ans = mid\n                high = mid - 1\n            else:\n     \
        \           low = mid + 1\n        return ans"
      python3: "from typing import List\nimport math\n\nclass Solution:\n    def findKthSmallest(self,\
        \ coins: List[int], k: int) -> int:\n        coins.sort()\n        refined =\
        \ []\n        for c in coins:\n            for r in refined:\n             \
        \   if c % r == 0:\n                    break\n            else:\n         \
        \       refined.append(c)\n\n        n = len(refined)\n        subset_lcms =\
        \ []\n        for i in range(1, 1 << n):\n            curr_lcm = 1\n       \
        \     bits = 0\n            for j in range(n):\n                if (i >> j)\
        \ & 1:\n                    curr_lcm = math.lcm(curr_lcm, refined[j])\n    \
        \                bits += 1\n            subset_lcms.append((curr_lcm, 1 if bits\
        \ % 2 == 1 else -1))\n\n        low = 1\n        high = refined[0] * k\n   \
        \     ans = high\n        while low <= high:\n            mid = (low + high)\
        \ // 2\n            count = 0\n            for l, sign in subset_lcms:\n   \
        \             count += (mid // l) * sign\n            if count >= k:\n     \
        \           ans = mid\n                high = mid - 1\n            else:\n \
        \               low = mid + 1\n        return ans"
      c: "#include <stdlib.h>\n\nlong long gcd(long long a, long long b) {\nwhile (b)\
        \ {\na %= b;\nlong long tmp = a;\na = b;\nb = tmp;\n}\nreturn a;\n}\n\nlong\
        \ long lcm(long long a, long long b) {\nif (a == 0 || b == 0) return 0;\nreturn\
        \ (a / gcd(a, b)) * b;\n}\n\nint cmp(const void* a, const void* b) {\nint val1\
        \ = *(const int*)a;\nint val2 = *(const int*)b;\nreturn (val1 > val2) - (val1\
        \ < val2);\n}\n\nlong long findKthSmallest(int* coins, int coinsSize, int k)\
        \ {\nqsort(coins, coinsSize, sizeof(int), cmp);\nint refined[15];\nint refinedSize\
        \ = 0;\nfor (int i = 0; i < coinsSize; i++) {\nint redundant = 0;\nfor (int\
        \ j = 0; j < refinedSize; j++) {\n    if (coins[i] % refined[j] == 0) {\n  \
        \      redundant = 1;\n        break;\n    }\n}\nif (!redundant) {\n    refined[refinedSize++]\
        \ = coins[i];\n}\n}\n\nint numSubsets = (1 << refinedSize) - 1;\nlong long*\
        \ subsetLcms = (long long*)malloc(numSubsets * sizeof(long long));\nint* signs\
        \ = (int*)malloc(numSubsets * sizeof(int));\nfor (int i = 1; i < (1 << refinedSize);\
        \ i++) {\nlong long currentLcm = 1;\nint bits = 0;\nfor (int j = 0; j < refinedSize;\
        \ j++) {\n    if ((i >> j) & 1) {\n        currentLcm = lcm(currentLcm, (long\
        \ long)refined[j]);\n        bits++;\n    }\n}\nsubsetLcms[i - 1] = currentLcm;\n\
        signs[i - 1] = (bits % 2 == 1) ? 1 : -1;\n}\n\nlong long low = 1, high = (long\
        \ long)refined[0] * k;\nlong long ans = high;\nwhile (low <= high) {\nlong long\
        \ mid = low + (high - low) / 2;\nlong long count = 0;\nfor (int i = 0; i < numSubsets;\
        \ i++) {\n    count += (mid / subsetLcms[i]) * signs[i];\n}\nif (count >= (long\
        \ long)k) {\n    ans = mid;\n    high = mid - 1;\n} else {\n    low = mid +\
        \ 1;\n}\n}\nfree(subsetLcms);\nfree(signs);\nreturn ans;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public long FindKthSmallest(int[] coins, int k) {\n        Array.Sort(coins);\n\
        \        List<int> refined = new List<int>();\n        foreach (int c in coins)\
        \ {\n            bool redundant = false;\n            foreach (int r in refined)\
        \ {\n                if (c % r == 0) {\n                    redundant = true;\n\
        \                    break;\n                }\n            }\n            if\
        \ (!redundant) refined.Add(c);\n        }\n\n        int n = refined.Count;\n\
        \        int numSubsets = (1 << n) - 1;\n        long[] subsetLcms = new long[numSubsets];\n\
        \        int[] signs = new int[numSubsets];\n\n        for (int i = 1; i < (1\
        \ << n); i++) {\n            long currentLcm = 1;\n            int bits = 0;\n\
        \            for (int j = 0; j < n; j++) {\n                if (((i >> j) &\
        \ 1) == 1) {\n                    currentLcm = GetLcm(currentLcm, (long)refined[j]);\n\
        \                    bits++;\n                }\n            }\n           \
        \ subsetLcms[i - 1] = currentLcm;\n            signs[i - 1] = (bits % 2 == 1)\
        \ ? 1 : -1;\n        }\n\n        long low = 1, high = (long)refined[0] * k;\n\
        \        long ans = high;\n        while (low <= high) {\n            long mid\
        \ = low + (high - low) / 2;\n            long count = 0;\n            for (int\
        \ i = 0; i < numSubsets; i++) {\n                count += (mid / subsetLcms[i])\
        \ * signs[i];\n            }\n            if (count >= (long)k) {\n        \
        \        ans = mid;\n                high = mid - 1;\n            } else {\n\
        \                low = mid + 1;\n            }\n        }\n        return ans;\n\
        \    }\n\n    private long GetGcd(long a, long b) {\n        while (b != 0)\
        \ {\n            a %= b;\n            long tmp = a;\n            a = b;\n  \
        \          b = tmp;\n        }\n        return a;\n    }\n\n    private long\
        \ GetLcm(long a, long b) {\n        if (a == 0 || b == 0) return 0;\n      \
        \  return (a / GetGcd(a, b)) * b;\n    }\n}"
      javascript: "/**\n * @param {number[]} coins\n * @param {number} k\n * @return\
        \ {number}\n */\nvar findKthSmallest = function(coins, k) {\n    const gcd =\
        \ (a, b) => (b === 0n ? a : gcd(b, a % b));\n    const lcm = (a, b) => (a *\
        \ b) / gcd(a, b);\n\n    coins.sort((a, b) => a - b);\n    const refined = [];\n\
        \    for (const c of coins) {\n        let redundant = false;\n        for (const\
        \ r of refined) {\n            if (c % r === 0) {\n                redundant\
        \ = true;\n                break;\n            }\n        }\n        if (!redundant)\
        \ refined.push(c);\n    }\n\n    const n = refined.length;\n    const subsetLcms\
        \ = [];\n    const signs = [];\n    for (let i = 1; i < (1 << n); i++) {\n \
        \       let currentLcm = 1n;\n        let bits = 0;\n        for (let j = 0;\
        \ j < n; j++) {\n            if ((i >> j) & 1) {\n                currentLcm\
        \ = lcm(currentLcm, BigInt(refined[j]));\n                bits++;\n        \
        \    }\n        }\n        subsetLcms.push(currentLcm);\n        signs.push(bits\
        \ % 2 === 1 ? 1n : -1n);\n    }\n\n    let low = 1n;\n    let high = BigInt(refined[0])\
        \ * BigInt(k);\n    let ans = high;\n    const kBi = BigInt(k);\n\n    while\
        \ (low <= high) {\n        let mid = (low + high) / 2n;\n        let count =\
        \ 0n;\n        for (let i = 0; i < subsetLcms.length; i++) {\n            count\
        \ += (mid / subsetLcms[i]) * signs[i];\n        }\n        if (count >= kBi)\
        \ {\n            ans = mid;\n            high = mid - 1n;\n        } else {\n\
        \            low = mid + 1n;\n        }\n    }\n    return Number(ans);\n};"
      typescript: "function findKthSmallest(coins: number[], k: number): number {\n\
        \    coins.sort((a, b) => a - b);\n    const filtered: number[] = [];\n    for\
        \ (const c of coins) {\n        let redundant = false;\n        for (const f\
        \ of filtered) {\n            if (c % f === 0) {\n                redundant\
        \ = true;\n                break;\n            }\n        }\n        if (!redundant)\
        \ filtered.push(c);\n    }\n\n    const lcms: bigint[] = [];\n    const signs:\
        \ number[] = [];\n    const m = filtered.length;\n\n    function gcd(a: bigint,\
        \ b: bigint): bigint {\n        while (b > 0n) {\n            a %= b;\n    \
        \        const temp = a; a = b; b = temp;\n        }\n        return a;\n  \
        \  }\n\n    function generate(idx: number, currentLcm: bigint, count: number)\
        \ {\n        if (idx === m) {\n            if (count > 0) {\n              \
        \  lcms.push(currentLcm);\n                signs.push(count % 2 === 1 ? 1 :\
        \ -1);\n            }\n            return;\n        }\n        generate(idx\
        \ + 1, currentLcm, count);\n        const nextLcm = (currentLcm / gcd(currentLcm,\
        \ BigInt(filtered[idx]))) * BigInt(filtered[idx]);\n        generate(idx + 1,\
        \ nextLcm, count + 1);\n    }\n\n    generate(0, 1n, 0);\n\n    let low = 1n;\n\
        \    let high = BigInt(filtered[0]) * BigInt(k);\n    let ans = high;\n\n  \
        \  while (low <= high) {\n        const mid = low + (high - low) / 2n;\n   \
        \     let cnt = 0n;\n        for (let i = 0; i < lcms.length; i++) {\n     \
        \       if (signs[i] === 1) cnt += mid / lcms[i];\n            else cnt -= mid\
        \ / lcms[i];\n        }\n\n        if (cnt >= BigInt(k)) {\n            ans\
        \ = mid;\n            high = mid - 1n;\n        } else {\n            low =\
        \ mid + 1n;\n        }\n    }\n    return Number(ans);\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $coins\n     * @param\
        \ Integer $k\n     * @return Integer\n     */\n    private $lcms = [];\n   \
        \ private $signs = [];\n\n    private function gcd($a, $b) {\n        while\
        \ ($b > 0) {\n            $a %= $b;\n            $temp = $a; $a = $b; $b = $temp;\n\
        \        }\n        return $a;\n    }\n\n    private function generate($idx,\
        \ $currentLcm, $count, $m, $filtered) {\n        if ($idx == $m) {\n       \
        \     if ($count > 0) {\n                $this->lcms[] = $currentLcm;\n    \
        \            $this->signs[] = ($count % 2 == 1 ? 1 : -1);\n            }\n \
        \           return;\n        }\n        $this->generate($idx + 1, $currentLcm,\
        \ $count, $m, $filtered);\n        $nextLcm = intdiv($currentLcm, $this->gcd($currentLcm,\
        \ $filtered[$idx])) * $filtered[$idx];\n        $this->generate($idx + 1, $nextLcm,\
        \ $count + 1, $m, $filtered);\n    }\n\n    function findKthSmallest($coins,\
        \ $k) {\n        sort($coins);\n        $filtered = [];\n        foreach ($coins\
        \ as $c) {\n            $redundant = false;\n            foreach ($filtered\
        \ as $f) {\n                if ($c % $f == 0) {\n                    $redundant\
        \ = true;\n                    break;\n                }\n            }\n  \
        \          if (!$redundant) $filtered[] = $c;\n        }\n\n        $this->lcms\
        \ = [];\n        $this->signs = [];\n        $this->generate(0, 1, 0, count($filtered),\
        \ $filtered);\n\n        $low = 1;\n        $high = $filtered[0] * $k;\n   \
        \     $ans = $high;\n        $m_lcms = count($this->lcms);\n\n        while\
        \ ($low <= $high) {\n            $mid = intdiv($low + $high, 2);\n         \
        \   $cnt = 0;\n            for ($i = 0; $i < $m_lcms; $i++) {\n            \
        \    if ($this->signs[$i] == 1) {\n                    $cnt += intdiv($mid,\
        \ $this->lcms[$i]);\n                } else {\n                    $cnt -= intdiv($mid,\
        \ $this->lcms[$i]);\n                }\n            }\n            if ($cnt\
        \ >= $k) {\n                $ans = $mid;\n                $high = $mid - 1;\n\
        \            } else {\n                $low = $mid + 1;\n            }\n   \
        \     }\n        return $ans;\n    }\n}"
      swift: "class Solution {\n    func findKthSmallest(_ coins: [Int], _ k: Int) ->\
        \ Int {\n        let sortedCoins = coins.sorted()\n        var filtered: [Int]\
        \ = []\n        for c in sortedCoins {\n            var redundant = false\n\
        \            for f in filtered {\n                if c % f == 0 {\n        \
        \            redundant = true\n                    break\n                }\n\
        \            }\n            if !redundant {\n                filtered.append(c)\n\
        \            }\n        }\n\n        var lcms: [Int64] = []\n        var signs:\
        \ [Int64] = []\n\n        func gcd(_ a: Int64, _ b: Int64) -> Int64 {\n    \
        \        var x = a\n            var y = b\n            while y > 0 {\n     \
        \           x %= y\n                let temp = x\n                x = y\n  \
        \              y = temp\n            }\n            return x\n        }\n\n\
        \        func generate(_ idx: Int, _ currentLcm: Int64, _ count: Int) {\n  \
        \          if idx == filtered.count {\n                if count > 0 {\n    \
        \                lcms.append(currentLcm)\n                    signs.append(count\
        \ % 2 == 1 ? 1 : -1)\n                }\n                return\n          \
        \  }\n            generate(idx + 1, currentLcm, count)\n            let nextLcm\
        \ = (currentLcm / gcd(currentLcm, Int64(filtered[idx]))) * Int64(filtered[idx])\n\
        \            generate(idx + 1, nextLcm, count + 1)\n        }\n\n        generate(0,\
        \ 1, 0)\n\n        var low: Int64 = 1\n        var high: Int64 = Int64(filtered[0])\
        \ * Int64(k)\n        var ans: Int64 = high\n\n        while low <= high {\n\
        \            let mid = low + (high - low) / 2\n            var cnt: Int64 =\
        \ 0\n            for i in 0..<lcms.count {\n                cnt += signs[i]\
        \ * (mid / lcms[i])\n            }\n            if cnt >= Int64(k) {\n     \
        \           ans = mid\n                high = mid - 1\n            } else {\n\
        \                low = mid + 1\n            }\n        }\n        return Int(ans)\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun findKthSmallest(coins: IntArray, k: Int): Long\
        \ {\n        coins.sort()\n        val filtered = mutableListOf<Int>()\n   \
        \     for (c in coins) {\n            var redundant = false\n            for\
        \ (f in filtered) {\n                if (c % f == 0) {\n                   \
        \ redundant = true\n                    break\n                }\n         \
        \   }\n            if (!redundant) filtered.add(c)\n        }\n\n        val\
        \ lcms = mutableListOf<Long>()\n        val signs = mutableListOf<Int>()\n\n\
        \        fun gcd(a: Long, b: Long): Long {\n            var x = a\n        \
        \    var y = b\n            while (y > 0) {\n                x %= y\n      \
        \          val temp = x\n                x = y\n                y = temp\n \
        \           }\n            return x\n        }\n\n        fun generate(idx:\
        \ Int, currentLcm: Long, count: Int) {\n            if (idx == filtered.size)\
        \ {\n                if (count > 0) {\n                    lcms.add(currentLcm)\n\
        \                    signs.add(if (count % 2 == 1) 1 else -1)\n            \
        \    }\n                return\n            }\n            generate(idx + 1,\
        \ currentLcm, count)\n            val nextLcm = (currentLcm / gcd(currentLcm,\
        \ filtered[idx].toLong())) * filtered[idx].toLong()\n            generate(idx\
        \ + 1, nextLcm, count + 1)\n        }\n\n        generate(0, 1L, 0)\n      \
        \  val lcmsArr = lcms.toLongArray()\n        val signsArr = signs.toIntArray()\n\
        \n        var low = 1L\n        var high = filtered[0].toLong() * k\n      \
        \  var ans = high\n\n        while (low <= high) {\n            val mid = low\
        \ + (high - low) / 2\n            var cnt = 0L\n            for (i in lcmsArr.indices)\
        \ {\n                if (signsArr[i] == 1) {\n                    cnt += mid\
        \ / lcmsArr[i]\n                } else {\n                    cnt -= mid / lcmsArr[i]\n\
        \                }\n            }\n            if (cnt >= k.toLong()) {\n  \
        \              ans = mid\n                high = mid - 1\n            } else\
        \ {\n                low = mid + 1\n            }\n        }\n        return\
        \ ans\n    }\n}"
      dart: "class Solution {\n  int _gcd(int a, int b) {\n    while (b != 0) {\n  \
        \    int t = b;\n      b = a % b;\n      a = t;\n    }\n    return a;\n  }\n\
        \n  int findKthSmallest(List<int> coins, int k) {\n    coins.sort();\n    List<int>\
        \ uniqueCoins = [];\n    for (int i = 0; i < coins.length; i++) {\n      bool\
        \ redundant = false;\n      for (int j = 0; j < i; j++) {\n        if (coins[i]\
        \ % coins[j] == 0) {\n          redundant = true;\n          break;\n      \
        \  }\n      }\n      if (!redundant) uniqueCoins.add(coins[i]);\n    }\n\n \
        \   int n = uniqueCoins.length;\n    List<int> subsetsLcm = [];\n    List<int>\
        \ subsetsSign = [];\n    for (int i = 1; i < (1 << n); i++) {\n      int currentLcm\
        \ = -1;\n      int bits = 0;\n      for (int j = 0; j < n; j++) {\n        if\
        \ ((i & (1 << j)) != 0) {\n          if (currentLcm == -1) {\n            currentLcm\
        \ = uniqueCoins[j];\n          } else {\n            currentLcm = (currentLcm\
        \ ~/ _gcd(currentLcm, uniqueCoins[j])) * uniqueCoins[j];\n          }\n    \
        \      bits++;\n        }\n      }\n      subsetsLcm.add(currentLcm);\n    \
        \  subsetsSign.add((bits % 2 == 1) ? 1 : -1);\n    }\n\n    int low = 1;\n \
        \   int high = uniqueCoins[0] * k;\n    int ans = high;\n\n    while (low <=\
        \ high) {\n      int mid = low + ((high - low) ~/ 2);\n      int count = 0;\n\
        \      for (int i = 0; i < subsetsLcm.length; i++) {\n        count += subsetsSign[i]\
        \ * (mid ~/ subsetsLcm[i]);\n      }\n      if (count >= k) {\n        ans =\
        \ mid;\n        high = mid - 1;\n      } else {\n        low = mid + 1;\n  \
        \    }\n    }\n    return ans;\n  }\n}"
      go: "import \"sort\"\n\nfunc findKthSmallest(coins []int, k int) int64 {\n   \
        \ sort.Ints(coins)\n    var unique []int64\n    for i, c := range coins {\n\
        \        redundant := false\n        for j := 0; j < i; j++ {\n            if\
        \ c%coins[j] == 0 {\n                redundant = true\n                break\n\
        \            }\n        }\n        if !redundant {\n            unique = append(unique,\
        \ int64(c))\n        }\n    }\n\n    type subset struct {\n        lcm  int64\n\
        \        sign int64\n    }\n    var subsets []subset\n    n := len(unique)\n\
        \    for i := 1; i < (1 << n); i++ {\n        var currentLcm int64 = -1\n  \
        \      bits := 0\n        for j := 0; j < n; j++ {\n            if (i>>j)&1\
        \ == 1 {\n                if currentLcm == -1 {\n                    currentLcm\
        \ = unique[j]\n                } else {\n                    g := gcd(currentLcm,\
        \ unique[j])\n                    currentLcm = (currentLcm / g) * unique[j]\n\
        \                }\n                bits++\n            }\n        }\n     \
        \   sign := int64(-1)\n        if bits%2 == 1 {\n            sign = 1\n    \
        \    }\n        subsets = append(subsets, subset{currentLcm, sign})\n    }\n\
        \n    low := int64(1)\n    high := unique[0] * int64(k)\n    ans := high\n \
        \   for low <= high {\n        mid := low + (high-low)/2\n        var count\
        \ int64 = 0\n        for _, s := range subsets {\n            count += s.sign\
        \ * (mid / s.lcm)\n        }\n        if count >= int64(k) {\n            ans\
        \ = mid\n            high = mid - 1\n        } else {\n            low = mid\
        \ + 1\n        }\n    }\n    return ans\n}\n\nfunc gcd(a, b int64) int64 {\n\
        \    for b != 0 {\n        a %= b\n        a, b = b, a\n    }\n    return a\n\
        }"
      ruby: "# @param {Integer[]} coins\n# @param {Integer} k\n# @return {Integer}\n\
        def find_kth_smallest(coins, k)\n  coins.sort!\n  unique = []\n  coins.each_with_index\
        \ do |c, i|\n    redundant = false\n    (0...i).each do |j|\n      if c % coins[j]\
        \ == 0\n        redundant = true\n        break\n      end\n    end\n    unique\
        \ << c unless redundant\n  end\n\n  subsets = []\n  n = unique.length\n  (1...(1\
        \ << n)).each do |i|\n    current_lcm = -1\n    bits = 0\n    (0...n).each do\
        \ |j|\n      if (i >> j) & 1 == 1\n        if current_lcm == -1\n          current_lcm\
        \ = unique[j]\n        else\n          current_lcm = (current_lcm / current_lcm.gcd(unique[j]))\
        \ * unique[j]\n        end\n        bits += 1\n      end\n    end\n    subsets\
        \ << [current_lcm, bits.odd? ? 1 : -1]\n  end\n\n  low = 1\n  high = unique[0]\
        \ * k\n  ans = high\n  while low <= high\n    mid = low + (high - low) / 2\n\
        \    count = 0\n    subsets.each do |lcm, sign|\n      count += sign * (mid\
        \ / lcm)\n    end\n    if count >= k\n      ans = mid\n      high = mid - 1\n\
        \    else\n      low = mid + 1\n    end\n  end\n  ans\nend"
      scala: "object Solution {\n    def findKthSmallest(coins: Array[Int], k: Int):\
        \ Long = {\n        val sortedCoins = coins.sorted\n        val unique = scala.collection.mutable.ArrayBuffer[Long]()\n\
        \        for (i <- sortedCoins.indices) {\n            var redundant = false\n\
        \            for (j <- 0 until i) {\n                if (sortedCoins(i) % sortedCoins(j)\
        \ == 0) redundant = true\n            }\n            if (!redundant) unique\
        \ += sortedCoins(i).toLong\n        }\n\n        val n = unique.length\n   \
        \     val subsetsLcm = new Array[Long]((1 << n) - 1)\n        val subsetsSign\
        \ = new Array[Int]((1 << n) - 1)\n\n        for (i <- 1 until (1 << n)) {\n\
        \            var currentLcm: Long = -1\n            var bits = 0\n         \
        \   for (j <- 0 until n) {\n                if (((i >> j) & 1) == 1) {\n   \
        \                 if (currentLcm == -1) {\n                        currentLcm\
        \ = unique(j)\n                    } else {\n                        currentLcm\
        \ = (currentLcm / gcd(currentLcm, unique(j))) * unique(j)\n                \
        \    }\n                    bits += 1\n                }\n            }\n  \
        \          subsetsLcm(i - 1) = currentLcm\n            subsetsSign(i - 1) =\
        \ if (bits % 2 == 1) 1 else -1\n        }\n\n        var low: Long = 1\n   \
        \     var high: Long = unique(0) * k.toLong\n        var ans: Long = high\n\n\
        \        while (low <= high) {\n            val mid: Long = low + (high - low)\
        \ / 2\n            var count: Long = 0\n            var idx = 0\n          \
        \  while (idx < subsetsLcm.length) {\n                count += subsetsSign(idx).toLong\
        \ * (mid / subsetsLcm(idx))\n                idx += 1\n            }\n     \
        \       if (count >= k.toLong) {\n                ans = mid\n              \
        \  high = mid - 1\n            } else {\n                low = mid + 1\n   \
        \         }\n        }\n        ans\n    }\n\n    def gcd(a: Long, b: Long):\
        \ Long = {\n        var x = a\n        var y = b\n        while (y != 0) {\n\
        \            val t = y\n            y = x % y\n            x = t\n        }\n\
        \        x\n    }\n}"
      rust: "impl Solution {\n    pub fn find_kth_smallest(coins: Vec<i32>, k: i32)\
        \ -> i64 {\n        let mut cleaned_coins = Vec::new();\n        for &c in &coins\
        \ {\n            let mut redundant = false;\n            for &other in &coins\
        \ {\n                if c != other && c % other == 0 {\n                   \
        \ redundant = true;\n                    break;\n                }\n       \
        \     }\n            if !redundant {\n                cleaned_coins.push(c as\
        \ i64);\n            }\n        }\n\n        let n = cleaned_coins.len();\n\
        \        let mut subsets = Vec::new();\n        for i in 1..(1 << n) {\n   \
        \         let mut l = 1i64;\n            let mut count = 0;\n            for\
        \ j in 0..n {\n                if (i >> j) & 1 == 1 {\n                    l\
        \ = Self::lcm(l, cleaned_coins[j]);\n                    count += 1;\n     \
        \           }\n            }\n            subsets.push((l, if count % 2 == 1\
        \ { 1i64 } else { -1i64 }));\n        }\n\n        let min_coin = *cleaned_coins.iter().min().unwrap();\n\
        \        let mut low = 1i64;\n        let mut high = min_coin as i64 * k as\
        \ i64;\n        let mut ans = high;\n\n        while low <= high {\n       \
        \     let mid = low + (high - low) / 2;\n            let mut count = 0i64;\n\
        \            for &(l, sign) in &subsets {\n                count += (mid / l)\
        \ * sign;\n            }\n            if count >= k as i64 {\n             \
        \   ans = mid;\n                high = mid - 1;\n            } else {\n    \
        \            low = mid + 1;\n            }\n        }\n        ans\n    }\n\n\
        \    fn gcd(mut a: i64, mut b: i64) -> i64 {\n        while b != 0 {\n     \
        \       let tmp = b;\n            b = a % b;\n            a = tmp;\n       \
        \ }\n        a\n    }\n\n    fn lcm(a: i64, b: i64) -> i64 {\n        (a / Self::gcd(a,\
        \ b)) * b\n    }\n}"
      racket: "(define/contract (find-kth-smallest coins k)\n  (-> (listof exact-integer?)\
        \ exact-integer? exact-integer?)\n  (let* ([cleaned-coins (filter (lambda (c)\n\
        \                                  (not (ormap (lambda (other)\n           \
        \                                     (and (not (= c other))\n             \
        \                                        (= 0 (remainder c other))))\n     \
        \                                         coins)))\n                       \
        \         coins)]\n         [min-coin (apply min cleaned-coins)]\n         [generate-subsets\
        \ (lambda (cs)\n                             (letrec ([helper (lambda (lst)\n\
        \                                                (if (empty? lst)\n        \
        \                                            '()\n                         \
        \                           (let* ([first-coin (first lst)]\n              \
        \                                             [rest-subsets (helper (rest lst))])\n\
        \                                                      (append (list (list first-coin\
        \ 1))\n                                                              (map (lambda\
        \ (s) (list (lcm first-coin (first s)) (- (second s)))) rest-subsets)\n    \
        \                                                          rest-subsets))))])\n\
        \                               (helper cs)))]\n         [subsets (generate-subsets\
        \ cleaned-coins)]\n         [calculate-count (lambda (mid subs)\n          \
        \                  (foldl (lambda (s acc) (+ acc (* (quotient mid (first s))\
        \ (second s)))) 0 subs))])\n    (let loop ([low 1]\n               [high (*\
        \ min-coin k)]\n               [ans (* min-coin k)])\n      (if (> low high)\n\
        \          ans\n          (let* ([mid (quotient (+ low high) 2)]\n         \
        \        [count (calculate-count mid subsets)])\n            (if (>= count k)\n\
        \                (loop low (- mid 1) mid)\n                (loop (+ mid 1) high\
        \ ans)))))))"
      erlang: "-spec find_kth_smallest(Coins :: [integer()], K :: integer()) -> integer().\n\
        find_kth_smallest(Coins, K) ->\n  Cleaned = [C || C <- Coins, not lists:any(fun(Other)\
        \ -> (C /= Other) and (C rem Other == 0) end, Coins)],\n  Subsets = generate_subsets(Cleaned),\n\
        \  Low = 1,\n  High = lists:min(Cleaned) * K,\n  binary_search(Low, High, High,\
        \ K, Subsets).\n\ngenerate_subsets([]) -> [];\ngenerate_subsets([H | T]) ->\n\
        \  Rest = generate_subsets(T),\n  [{H, 1}] ++ [{lcm(H, L), -S} || {L, S} <-\
        \ Rest] ++ Rest.\n\ngcd(A, 0) -> A;\ngcd(A, B) -> gcd(B, A rem B).\n\nlcm(A,\
        \ B) -> (A div gcd(A, B)) * B.\n\nbinary_search(Low, High, Ans, K, Subsets)\
        \ when Low =< High ->\n  Mid = Low + (High - Low) div 2,\n  Count = calculate_count(Mid,\
        \ Subsets),\n  if\n    Count >= K -> binary_search(Low, Mid - 1, Mid, K, Subsets);\n\
        \    true -> binary_search(Mid + 1, High, Ans, K, Subsets)\n  end;\nbinary_search(_Low,\
        \ _High, Ans, _K, _Subsets) -> Ans.\n\ncalculate_count(Mid, Subsets) ->\n  lists:foldl(fun({L,\
        \ S}, Acc) -> Acc + (Mid div L) * S end, 0, Subsets)."
      elixir: "defmodule Solution do\n  @spec find_kth_smallest(coins :: [integer],\
        \ k :: integer) :: integer\n  def find_kth_smallest(coins, k) do\n    cleaned\
        \ = Enum.filter(coins, fn c ->\n      !Enum.any?(coins, fn other -> c != other\
        \ and rem(c, other) == 0 end)\n    end)\n    subsets = generate_subsets(cleaned)\n\
        \    low = 1\n    high = Enum.min(cleaned) * k\n    binary_search(low, high,\
        \ high, k, subsets)\n  end\n\n  defp generate_subsets([]), do: []\n  defp generate_subsets([h\
        \ | t]) do\n    rest = generate_subsets(t)\n    [{h, 1}] ++ Enum.map(rest, fn\
        \ {l, s} -> {lcm(h, l), -s} end) ++ rest\n  end\n\n  defp gcd(a, 0), do: a\n\
        \  defp gcd(a, b), do: gcd(b, rem(a, b))\n\n  defp lcm(a, b), do: div(a, gcd(a,\
        \ b)) * b\n\n  defp binary_search(low, high, ans, k, subsets) when low <= high\
        \ do\n    mid = div(low + high, 2)\n    count = calculate_count(mid, subsets)\n\
        \    if count >= k do\n      binary_search(low, mid - 1, mid, k, subsets)\n\
        \    else\n      binary_search(mid + 1, high, ans, k, subsets)\n    end\n  end\n\
        \  defp binary_search(_low, _high, ans, _k, _subsets), do: ans\n\n  defp calculate_count(mid,\
        \ subsets) do\n    Enum.reduce(subsets, 0, fn {l, s}, acc -> acc + div(mid,\
        \ l) * s end)\n  end\nend"
    approach: The problem asks for the $k$-th smallest integer that is a multiple of
      at least one denomination from the provided set. Since the function $f(x)$, which
      counts the number of such multiples in the range $[1, x]$, is monotonically increasing,
      we can use binary search to find the smallest $x$ such that $f(x) \ge k$. The
      maximum possible value for the answer is $k \times \min(\text{coins})$, which
      for $k = 2 \cdot 10^9$ and $\min(\text{coins}) = 25$ is $5 \cdot 10^{10}$, well
      within the range of a 64-bit integer.
    time_complexity: O(2^n \cdot \log(k \cdot \min(c)) + n^2), where $n$ is the number
      of distinct coins. We first filter out redundant coins (those that are multiples
      of another coin in the set) in $O(n^2)$. We then precompute the LCM and sign for
      all $2^n - 1$ subsets of coins whose LCM does not exceed our search bound. The
      binary search takes $O(\log(k \cdot \min(c)))$ iterations, and each iteration
      evaluates the Inclusion-Exclusion Principle sum in $O(2^n)$. With $n \le 15$ and
      approximately 40 binary search steps, the algorithm executes roughly $1.3 \times
      10^6$ operations.
    space_complexity: O(2^n) to store the precomputed LCMs and signs of all subsets.
      For $n = 15$, this results in $2^{15} - 1 = 32,767$ entries, which is well within
      standard memory limits.
    elapsed_time: 335.2766156196594
    model: gemini-3-flash-preview
    generated_at: '2026-08-21 00:57:24 '
---

## Problem #3116: Kth Smallest Amount With Single Denomination Combination

**Difficulty:** Hard

**Topics:** Array, Math, Binary Search, Bit Manipulation, Combinatorics, Number Theory

## Problem Description

<p>You are given an integer array <code>coins</code> representing coins of different denominations and an integer <code>k</code>.</p>

<p>You have an infinite number of coins of each denomination. However, you are <strong>not allowed</strong> to combine coins of different denominations.</p>

<p>Return the <code>k<sup>th</sup></code> <strong>smallest</strong> amount that can be made using these coins.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block" style="
    border-color: var(--border-tertiary);
    border-left-width: 2px;
    color: var(--text-secondary);
    font-size: .875rem;
    margin-bottom: 1rem;
    margin-top: 1rem;
    overflow: visible;
    padding-left: 1rem;
">
<p><strong>Input:</strong> <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">coins = [3,6,9], k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
"> 9</span></p>

<p><strong>Explanation:</strong> The given coins can make the following amounts:<br />
Coin 3 produces multiples of 3: 3, 6, 9, 12, 15, etc.<br />
Coin 6 produces multiples of 6: 6, 12, 18, 24, etc.<br />
Coin 9 produces multiples of 9: 9, 18, 27, 36, etc.<br />
All of the coins combined produce: 3, 6, <u><strong>9</strong></u>, 12, 15, etc.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block" style="
    border-color: var(--border-tertiary);
    border-left-width: 2px;
    color: var(--text-secondary);
    font-size: .875rem;
    margin-bottom: 1rem;
    margin-top: 1rem;
    overflow: visible;
    padding-left: 1rem;
">
<p><strong>Input:</strong><span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
"> coins = [5,2], k = 7</span></p>

<p><strong>Output:</strong><span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
"> 12 </span></p>

<p><strong>Explanation:</strong> The given coins can make the following amounts:<br />
Coin 5 produces multiples of 5: 5, 10, 15, 20, etc.<br />
Coin 2 produces multiples of 2: 2, 4, 6, 8, 10, 12, etc.<br />
All of the coins combined produce: 2, 4, 5, 6, 8, 10, <u><strong>12</strong></u>, 14, 15, etc.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= coins.length &lt;= 15</code></li>
	<li><code>1 &lt;= coins[i] &lt;= 25</code></li>
	<li><code>1 &lt;= k &lt;= 2 * 10<sup>9</sup></code></li>
	<li><code>coins</code> contains pairwise distinct integers.</li>
</ul>


## Hints

1. Binary search the answer `x`.

2. Use the inclusion-exclusion principle to count the number of distinct amounts that can be made up to `x`.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the $k$-th smallest integer that is a multiple of at least one denomination from the provided set. Since the function $f(x)$, which counts the number of such multiples in the range $[1, x]$, is monotonically increasing, we can use binary search to find the smallest $x$ such that $f(x) \ge k$. The maximum possible value for the answer is $k \times \min(\text{coins})$, which for $k = 2 \cdot 10^9$ and $\min(\text{coins}) = 25$ is $5 \cdot 10^{10}$, well within the range of a 64-bit integer.

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
    long long findKthSmallest(vector<int>& coins, int k) {
        sort(coins.begin(), coins.end());
        vector<int> filtered;
        for (int i = 0; i < coins.size(); ++i) {
            bool redundant = false;
            for (int j = 0; j < i; ++j) {
                if (coins[i] % coins[j] == 0) {
                    redundant = true;
                    break;
                }
            }
            if (!redundant) filtered.push_back(coins[i]);
        }

        long long limit = (long long)filtered[0] * k;
        vector<pair<long long, int>> subsetsLcm;
        function<void(int, long long, int)> generate = [&](int idx, long long currentLcm, int count) {
            for (int i = idx; i < filtered.size(); ++i) {
                long long g = std::gcd(currentLcm, (long long)filtered[i]);
                long long nextLcm = (currentLcm / g) * filtered[i];
                if (nextLcm <= limit) {
                    int sign = ((count + 1) % 2 == 1) ? 1 : -1;
                    subsetsLcm.push_back({nextLcm, sign});
                    generate(i + 1, nextLcm, count + 1);
                }
            }
        };
        generate(0, 1, 0);

        long long low = 1, high = limit, ans = limit;
        while (low <= high) {
            long long mid = low + (high - low) / 2;
            long long cnt = 0;
            for (auto& item : subsetsLcm) {
                cnt += item.second * (mid / item.first);
            }
            if (cnt >= k) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
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
    public long findKthSmallest(int[] coins, int k) {
        Arrays.sort(coins);
        List<Integer> filtered = new ArrayList<>();
        for (int i = 0; i < coins.length; i++) {
            boolean redundant = false;
            for (int j = 0; j < i; j++) {
                if (coins[i] % coins[j] == 0) {
                    redundant = true;
                    break;
                }
            }
            if (!redundant) filtered.add(coins[i]);
        }

        long limit = (long) filtered.get(0) * k;
        List<long[]> subsetsLcm = new ArrayList<>();
        generateLcm(0, 1, 0, filtered, subsetsLcm, limit);

        long low = 1, high = limit, ans = limit;
        while (low <= high) {
            long mid = low + (high - low) / 2;
            long count = 0;
            for (long[] item : subsetsLcm) {
                count += item[1] * (mid / item[0]);
            }
            if (count >= (long) k) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }

    private void generateLcm(int idx, long currentLcm, int count, List<Integer> filtered, List<long[]> subsetsLcm, long limit) {
        for (int i = idx; i < filtered.size(); i++) {
            long coin = filtered.get(i);
            long g = gcd(currentLcm, coin);
            long nextLcm = (currentLcm / g) * coin;
            if (nextLcm <= limit) {
                int sign = ((count + 1) % 2 == 1) ? 1 : -1;
                subsetsLcm.add(new long[]{nextLcm, sign});
                generateLcm(i + 1, nextLcm, count + 1, filtered, subsetsLcm, limit);
            }
        }
    }

    private long gcd(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import math

class Solution(object):
    def findKthSmallest(self, coins, k):
        """
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        coins.sort()
        filtered = []
        for i in range(len(coins)):
            redundant = False
            for j in range(i):
                if coins[i] % coins[j] == 0:
                    redundant = True
                    break
            if not redundant:
                filtered.append(coins[i])

        n = len(filtered)
        limit = filtered[0] * k
        subsets_lcm = []

        def generate_lcm(idx, current_lcm, count):
            for i in range(idx, n):
                coin = filtered[i]
                g = math.gcd(current_lcm, coin)
                next_lcm = (current_lcm // g) * coin
                if next_lcm <= limit:
                    sign = 1 if (count + 1) % 2 == 1 else -1
                    subsets_lcm.append((next_lcm, sign))
                    generate_lcm(i + 1, next_lcm, count + 1)

        generate_lcm(0, 1, 0)

        plus = [l for l, s in subsets_lcm if s == 1]
        minus = [l for l, s in subsets_lcm if s == -1]

        low, high = 1, limit
        ans = limit
        while low <= high:
            mid = (low + high) // 2
            cnt = sum(mid // l for l in plus) - sum(mid // l for l in minus)
            if cnt >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from typing import List
import math

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        refined = []
        for c in coins:
            for r in refined:
                if c % r == 0:
                    break
            else:
                refined.append(c)

        n = len(refined)
        subset_lcms = []
        for i in range(1, 1 << n):
            curr_lcm = 1
            bits = 0
            for j in range(n):
                if (i >> j) & 1:
                    curr_lcm = math.lcm(curr_lcm, refined[j])
                    bits += 1
            subset_lcms.append((curr_lcm, 1 if bits % 2 == 1 else -1))

        low = 1
        high = refined[0] * k
        ans = high
        while low <= high:
            mid = (low + high) // 2
            count = 0
            for l, sign in subset_lcms:
                count += (mid // l) * sign
            if count >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

long long gcd(long long a, long long b) {
while (b) {
a %= b;
long long tmp = a;
a = b;
b = tmp;
}
return a;
}

long long lcm(long long a, long long b) {
if (a == 0 || b == 0) return 0;
return (a / gcd(a, b)) * b;
}

int cmp(const void* a, const void* b) {
int val1 = *(const int*)a;
int val2 = *(const int*)b;
return (val1 > val2) - (val1 < val2);
}

long long findKthSmallest(int* coins, int coinsSize, int k) {
qsort(coins, coinsSize, sizeof(int), cmp);
int refined[15];
int refinedSize = 0;
for (int i = 0; i < coinsSize; i++) {
int redundant = 0;
for (int j = 0; j < refinedSize; j++) {
    if (coins[i] % refined[j] == 0) {
        redundant = 1;
        break;
    }
}
if (!redundant) {
    refined[refinedSize++] = coins[i];
}
}

int numSubsets = (1 << refinedSize) - 1;
long long* subsetLcms = (long long*)malloc(numSubsets * sizeof(long long));
int* signs = (int*)malloc(numSubsets * sizeof(int));
for (int i = 1; i < (1 << refinedSize); i++) {
long long currentLcm = 1;
int bits = 0;
for (int j = 0; j < refinedSize; j++) {
    if ((i >> j) & 1) {
        currentLcm = lcm(currentLcm, (long long)refined[j]);
        bits++;
    }
}
subsetLcms[i - 1] = currentLcm;
signs[i - 1] = (bits % 2 == 1) ? 1 : -1;
}

long long low = 1, high = (long long)refined[0] * k;
long long ans = high;
while (low <= high) {
long long mid = low + (high - low) / 2;
long long count = 0;
for (int i = 0; i < numSubsets; i++) {
    count += (mid / subsetLcms[i]) * signs[i];
}
if (count >= (long long)k) {
    ans = mid;
    high = mid - 1;
} else {
    low = mid + 1;
}
}
free(subsetLcms);
free(signs);
return ans;
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
    public long FindKthSmallest(int[] coins, int k) {
        Array.Sort(coins);
        List<int> refined = new List<int>();
        foreach (int c in coins) {
            bool redundant = false;
            foreach (int r in refined) {
                if (c % r == 0) {
                    redundant = true;
                    break;
                }
            }
            if (!redundant) refined.Add(c);
        }

        int n = refined.Count;
        int numSubsets = (1 << n) - 1;
        long[] subsetLcms = new long[numSubsets];
        int[] signs = new int[numSubsets];

        for (int i = 1; i < (1 << n); i++) {
            long currentLcm = 1;
            int bits = 0;
            for (int j = 0; j < n; j++) {
                if (((i >> j) & 1) == 1) {
                    currentLcm = GetLcm(currentLcm, (long)refined[j]);
                    bits++;
                }
            }
            subsetLcms[i - 1] = currentLcm;
            signs[i - 1] = (bits % 2 == 1) ? 1 : -1;
        }

        long low = 1, high = (long)refined[0] * k;
        long ans = high;
        while (low <= high) {
            long mid = low + (high - low) / 2;
            long count = 0;
            for (int i = 0; i < numSubsets; i++) {
                count += (mid / subsetLcms[i]) * signs[i];
            }
            if (count >= (long)k) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }

    private long GetGcd(long a, long b) {
        while (b != 0) {
            a %= b;
            long tmp = a;
            a = b;
            b = tmp;
        }
        return a;
    }

    private long GetLcm(long a, long b) {
        if (a == 0 || b == 0) return 0;
        return (a / GetGcd(a, b)) * b;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} coins
 * @param {number} k
 * @return {number}
 */
var findKthSmallest = function(coins, k) {
    const gcd = (a, b) => (b === 0n ? a : gcd(b, a % b));
    const lcm = (a, b) => (a * b) / gcd(a, b);

    coins.sort((a, b) => a - b);
    const refined = [];
    for (const c of coins) {
        let redundant = false;
        for (const r of refined) {
            if (c % r === 0) {
                redundant = true;
                break;
            }
        }
        if (!redundant) refined.push(c);
    }

    const n = refined.length;
    const subsetLcms = [];
    const signs = [];
    for (let i = 1; i < (1 << n); i++) {
        let currentLcm = 1n;
        let bits = 0;
        for (let j = 0; j < n; j++) {
            if ((i >> j) & 1) {
                currentLcm = lcm(currentLcm, BigInt(refined[j]));
                bits++;
            }
        }
        subsetLcms.push(currentLcm);
        signs.push(bits % 2 === 1 ? 1n : -1n);
    }

    let low = 1n;
    let high = BigInt(refined[0]) * BigInt(k);
    let ans = high;
    const kBi = BigInt(k);

    while (low <= high) {
        let mid = (low + high) / 2n;
        let count = 0n;
        for (let i = 0; i < subsetLcms.length; i++) {
            count += (mid / subsetLcms[i]) * signs[i];
        }
        if (count >= kBi) {
            ans = mid;
            high = mid - 1n;
        } else {
            low = mid + 1n;
        }
    }
    return Number(ans);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function findKthSmallest(coins: number[], k: number): number {
    coins.sort((a, b) => a - b);
    const filtered: number[] = [];
    for (const c of coins) {
        let redundant = false;
        for (const f of filtered) {
            if (c % f === 0) {
                redundant = true;
                break;
            }
        }
        if (!redundant) filtered.push(c);
    }

    const lcms: bigint[] = [];
    const signs: number[] = [];
    const m = filtered.length;

    function gcd(a: bigint, b: bigint): bigint {
        while (b > 0n) {
            a %= b;
            const temp = a; a = b; b = temp;
        }
        return a;
    }

    function generate(idx: number, currentLcm: bigint, count: number) {
        if (idx === m) {
            if (count > 0) {
                lcms.push(currentLcm);
                signs.push(count % 2 === 1 ? 1 : -1);
            }
            return;
        }
        generate(idx + 1, currentLcm, count);
        const nextLcm = (currentLcm / gcd(currentLcm, BigInt(filtered[idx]))) * BigInt(filtered[idx]);
        generate(idx + 1, nextLcm, count + 1);
    }

    generate(0, 1n, 0);

    let low = 1n;
    let high = BigInt(filtered[0]) * BigInt(k);
    let ans = high;

    while (low <= high) {
        const mid = low + (high - low) / 2n;
        let cnt = 0n;
        for (let i = 0; i < lcms.length; i++) {
            if (signs[i] === 1) cnt += mid / lcms[i];
            else cnt -= mid / lcms[i];
        }

        if (cnt >= BigInt(k)) {
            ans = mid;
            high = mid - 1n;
        } else {
            low = mid + 1n;
        }
    }
    return Number(ans);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $coins
     * @param Integer $k
     * @return Integer
     */
    private $lcms = [];
    private $signs = [];

    private function gcd($a, $b) {
        while ($b > 0) {
            $a %= $b;
            $temp = $a; $a = $b; $b = $temp;
        }
        return $a;
    }

    private function generate($idx, $currentLcm, $count, $m, $filtered) {
        if ($idx == $m) {
            if ($count > 0) {
                $this->lcms[] = $currentLcm;
                $this->signs[] = ($count % 2 == 1 ? 1 : -1);
            }
            return;
        }
        $this->generate($idx + 1, $currentLcm, $count, $m, $filtered);
        $nextLcm = intdiv($currentLcm, $this->gcd($currentLcm, $filtered[$idx])) * $filtered[$idx];
        $this->generate($idx + 1, $nextLcm, $count + 1, $m, $filtered);
    }

    function findKthSmallest($coins, $k) {
        sort($coins);
        $filtered = [];
        foreach ($coins as $c) {
            $redundant = false;
            foreach ($filtered as $f) {
                if ($c % $f == 0) {
                    $redundant = true;
                    break;
                }
            }
            if (!$redundant) $filtered[] = $c;
        }

        $this->lcms = [];
        $this->signs = [];
        $this->generate(0, 1, 0, count($filtered), $filtered);

        $low = 1;
        $high = $filtered[0] * $k;
        $ans = $high;
        $m_lcms = count($this->lcms);

        while ($low <= $high) {
            $mid = intdiv($low + $high, 2);
            $cnt = 0;
            for ($i = 0; $i < $m_lcms; $i++) {
                if ($this->signs[$i] == 1) {
                    $cnt += intdiv($mid, $this->lcms[$i]);
                } else {
                    $cnt -= intdiv($mid, $this->lcms[$i]);
                }
            }
            if ($cnt >= $k) {
                $ans = $mid;
                $high = $mid - 1;
            } else {
                $low = $mid + 1;
            }
        }
        return $ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func findKthSmallest(_ coins: [Int], _ k: Int) -> Int {
        let sortedCoins = coins.sorted()
        var filtered: [Int] = []
        for c in sortedCoins {
            var redundant = false
            for f in filtered {
                if c % f == 0 {
                    redundant = true
                    break
                }
            }
            if !redundant {
                filtered.append(c)
            }
        }

        var lcms: [Int64] = []
        var signs: [Int64] = []

        func gcd(_ a: Int64, _ b: Int64) -> Int64 {
            var x = a
            var y = b
            while y > 0 {
                x %= y
                let temp = x
                x = y
                y = temp
            }
            return x
        }

        func generate(_ idx: Int, _ currentLcm: Int64, _ count: Int) {
            if idx == filtered.count {
                if count > 0 {
                    lcms.append(currentLcm)
                    signs.append(count % 2 == 1 ? 1 : -1)
                }
                return
            }
            generate(idx + 1, currentLcm, count)
            let nextLcm = (currentLcm / gcd(currentLcm, Int64(filtered[idx]))) * Int64(filtered[idx])
            generate(idx + 1, nextLcm, count + 1)
        }

        generate(0, 1, 0)

        var low: Int64 = 1
        var high: Int64 = Int64(filtered[0]) * Int64(k)
        var ans: Int64 = high

        while low <= high {
            let mid = low + (high - low) / 2
            var cnt: Int64 = 0
            for i in 0..<lcms.count {
                cnt += signs[i] * (mid / lcms[i])
            }
            if cnt >= Int64(k) {
                ans = mid
                high = mid - 1
            } else {
                low = mid + 1
            }
        }
        return Int(ans)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun findKthSmallest(coins: IntArray, k: Int): Long {
        coins.sort()
        val filtered = mutableListOf<Int>()
        for (c in coins) {
            var redundant = false
            for (f in filtered) {
                if (c % f == 0) {
                    redundant = true
                    break
                }
            }
            if (!redundant) filtered.add(c)
        }

        val lcms = mutableListOf<Long>()
        val signs = mutableListOf<Int>()

        fun gcd(a: Long, b: Long): Long {
            var x = a
            var y = b
            while (y > 0) {
                x %= y
                val temp = x
                x = y
                y = temp
            }
            return x
        }

        fun generate(idx: Int, currentLcm: Long, count: Int) {
            if (idx == filtered.size) {
                if (count > 0) {
                    lcms.add(currentLcm)
                    signs.add(if (count % 2 == 1) 1 else -1)
                }
                return
            }
            generate(idx + 1, currentLcm, count)
            val nextLcm = (currentLcm / gcd(currentLcm, filtered[idx].toLong())) * filtered[idx].toLong()
            generate(idx + 1, nextLcm, count + 1)
        }

        generate(0, 1L, 0)
        val lcmsArr = lcms.toLongArray()
        val signsArr = signs.toIntArray()

        var low = 1L
        var high = filtered[0].toLong() * k
        var ans = high

        while (low <= high) {
            val mid = low + (high - low) / 2
            var cnt = 0L
            for (i in lcmsArr.indices) {
                if (signsArr[i] == 1) {
                    cnt += mid / lcmsArr[i]
                } else {
                    cnt -= mid / lcmsArr[i]
                }
            }
            if (cnt >= k.toLong()) {
                ans = mid
                high = mid - 1
            } else {
                low = mid + 1
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
class Solution {
  int _gcd(int a, int b) {
    while (b != 0) {
      int t = b;
      b = a % b;
      a = t;
    }
    return a;
  }

  int findKthSmallest(List<int> coins, int k) {
    coins.sort();
    List<int> uniqueCoins = [];
    for (int i = 0; i < coins.length; i++) {
      bool redundant = false;
      for (int j = 0; j < i; j++) {
        if (coins[i] % coins[j] == 0) {
          redundant = true;
          break;
        }
      }
      if (!redundant) uniqueCoins.add(coins[i]);
    }

    int n = uniqueCoins.length;
    List<int> subsetsLcm = [];
    List<int> subsetsSign = [];
    for (int i = 1; i < (1 << n); i++) {
      int currentLcm = -1;
      int bits = 0;
      for (int j = 0; j < n; j++) {
        if ((i & (1 << j)) != 0) {
          if (currentLcm == -1) {
            currentLcm = uniqueCoins[j];
          } else {
            currentLcm = (currentLcm ~/ _gcd(currentLcm, uniqueCoins[j])) * uniqueCoins[j];
          }
          bits++;
        }
      }
      subsetsLcm.add(currentLcm);
      subsetsSign.add((bits % 2 == 1) ? 1 : -1);
    }

    int low = 1;
    int high = uniqueCoins[0] * k;
    int ans = high;

    while (low <= high) {
      int mid = low + ((high - low) ~/ 2);
      int count = 0;
      for (int i = 0; i < subsetsLcm.length; i++) {
        count += subsetsSign[i] * (mid ~/ subsetsLcm[i]);
      }
      if (count >= k) {
        ans = mid;
        high = mid - 1;
      } else {
        low = mid + 1;
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
import "sort"

func findKthSmallest(coins []int, k int) int64 {
    sort.Ints(coins)
    var unique []int64
    for i, c := range coins {
        redundant := false
        for j := 0; j < i; j++ {
            if c%coins[j] == 0 {
                redundant = true
                break
            }
        }
        if !redundant {
            unique = append(unique, int64(c))
        }
    }

    type subset struct {
        lcm  int64
        sign int64
    }
    var subsets []subset
    n := len(unique)
    for i := 1; i < (1 << n); i++ {
        var currentLcm int64 = -1
        bits := 0
        for j := 0; j < n; j++ {
            if (i>>j)&1 == 1 {
                if currentLcm == -1 {
                    currentLcm = unique[j]
                } else {
                    g := gcd(currentLcm, unique[j])
                    currentLcm = (currentLcm / g) * unique[j]
                }
                bits++
            }
        }
        sign := int64(-1)
        if bits%2 == 1 {
            sign = 1
        }
        subsets = append(subsets, subset{currentLcm, sign})
    }

    low := int64(1)
    high := unique[0] * int64(k)
    ans := high
    for low <= high {
        mid := low + (high-low)/2
        var count int64 = 0
        for _, s := range subsets {
            count += s.sign * (mid / s.lcm)
        }
        if count >= int64(k) {
            ans = mid
            high = mid - 1
        } else {
            low = mid + 1
        }
    }
    return ans
}

func gcd(a, b int64) int64 {
    for b != 0 {
        a %= b
        a, b = b, a
    }
    return a
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} coins
# @param {Integer} k
# @return {Integer}
def find_kth_smallest(coins, k)
  coins.sort!
  unique = []
  coins.each_with_index do |c, i|
    redundant = false
    (0...i).each do |j|
      if c % coins[j] == 0
        redundant = true
        break
      end
    end
    unique << c unless redundant
  end

  subsets = []
  n = unique.length
  (1...(1 << n)).each do |i|
    current_lcm = -1
    bits = 0
    (0...n).each do |j|
      if (i >> j) & 1 == 1
        if current_lcm == -1
          current_lcm = unique[j]
        else
          current_lcm = (current_lcm / current_lcm.gcd(unique[j])) * unique[j]
        end
        bits += 1
      end
    end
    subsets << [current_lcm, bits.odd? ? 1 : -1]
  end

  low = 1
  high = unique[0] * k
  ans = high
  while low <= high
    mid = low + (high - low) / 2
    count = 0
    subsets.each do |lcm, sign|
      count += sign * (mid / lcm)
    end
    if count >= k
      ans = mid
      high = mid - 1
    else
      low = mid + 1
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
    def findKthSmallest(coins: Array[Int], k: Int): Long = {
        val sortedCoins = coins.sorted
        val unique = scala.collection.mutable.ArrayBuffer[Long]()
        for (i <- sortedCoins.indices) {
            var redundant = false
            for (j <- 0 until i) {
                if (sortedCoins(i) % sortedCoins(j) == 0) redundant = true
            }
            if (!redundant) unique += sortedCoins(i).toLong
        }

        val n = unique.length
        val subsetsLcm = new Array[Long]((1 << n) - 1)
        val subsetsSign = new Array[Int]((1 << n) - 1)

        for (i <- 1 until (1 << n)) {
            var currentLcm: Long = -1
            var bits = 0
            for (j <- 0 until n) {
                if (((i >> j) & 1) == 1) {
                    if (currentLcm == -1) {
                        currentLcm = unique(j)
                    } else {
                        currentLcm = (currentLcm / gcd(currentLcm, unique(j))) * unique(j)
                    }
                    bits += 1
                }
            }
            subsetsLcm(i - 1) = currentLcm
            subsetsSign(i - 1) = if (bits % 2 == 1) 1 else -1
        }

        var low: Long = 1
        var high: Long = unique(0) * k.toLong
        var ans: Long = high

        while (low <= high) {
            val mid: Long = low + (high - low) / 2
            var count: Long = 0
            var idx = 0
            while (idx < subsetsLcm.length) {
                count += subsetsSign(idx).toLong * (mid / subsetsLcm(idx))
                idx += 1
            }
            if (count >= k.toLong) {
                ans = mid
                high = mid - 1
            } else {
                low = mid + 1
            }
        }
        ans
    }

    def gcd(a: Long, b: Long): Long = {
        var x = a
        var y = b
        while (y != 0) {
            val t = y
            y = x % y
            x = t
        }
        x
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn find_kth_smallest(coins: Vec<i32>, k: i32) -> i64 {
        let mut cleaned_coins = Vec::new();
        for &c in &coins {
            let mut redundant = false;
            for &other in &coins {
                if c != other && c % other == 0 {
                    redundant = true;
                    break;
                }
            }
            if !redundant {
                cleaned_coins.push(c as i64);
            }
        }

        let n = cleaned_coins.len();
        let mut subsets = Vec::new();
        for i in 1..(1 << n) {
            let mut l = 1i64;
            let mut count = 0;
            for j in 0..n {
                if (i >> j) & 1 == 1 {
                    l = Self::lcm(l, cleaned_coins[j]);
                    count += 1;
                }
            }
            subsets.push((l, if count % 2 == 1 { 1i64 } else { -1i64 }));
        }

        let min_coin = *cleaned_coins.iter().min().unwrap();
        let mut low = 1i64;
        let mut high = min_coin as i64 * k as i64;
        let mut ans = high;

        while low <= high {
            let mid = low + (high - low) / 2;
            let mut count = 0i64;
            for &(l, sign) in &subsets {
                count += (mid / l) * sign;
            }
            if count >= k as i64 {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        ans
    }

    fn gcd(mut a: i64, mut b: i64) -> i64 {
        while b != 0 {
            let tmp = b;
            b = a % b;
            a = tmp;
        }
        a
    }

    fn lcm(a: i64, b: i64) -> i64 {
        (a / Self::gcd(a, b)) * b
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (find-kth-smallest coins k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([cleaned-coins (filter (lambda (c)
                                  (not (ormap (lambda (other)
                                                (and (not (= c other))
                                                     (= 0 (remainder c other))))
                                              coins)))
                                coins)]
         [min-coin (apply min cleaned-coins)]
         [generate-subsets (lambda (cs)
                             (letrec ([helper (lambda (lst)
                                                (if (empty? lst)
                                                    '()
                                                    (let* ([first-coin (first lst)]
                                                           [rest-subsets (helper (rest lst))])
                                                      (append (list (list first-coin 1))
                                                              (map (lambda (s) (list (lcm first-coin (first s)) (- (second s)))) rest-subsets)
                                                              rest-subsets))))])
                               (helper cs)))]
         [subsets (generate-subsets cleaned-coins)]
         [calculate-count (lambda (mid subs)
                            (foldl (lambda (s acc) (+ acc (* (quotient mid (first s)) (second s)))) 0 subs))])
    (let loop ([low 1]
               [high (* min-coin k)]
               [ans (* min-coin k)])
      (if (> low high)
          ans
          (let* ([mid (quotient (+ low high) 2)]
                 [count (calculate-count mid subsets)])
            (if (>= count k)
                (loop low (- mid 1) mid)
                (loop (+ mid 1) high ans)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec find_kth_smallest(Coins :: [integer()], K :: integer()) -> integer().
find_kth_smallest(Coins, K) ->
  Cleaned = [C || C <- Coins, not lists:any(fun(Other) -> (C /= Other) and (C rem Other == 0) end, Coins)],
  Subsets = generate_subsets(Cleaned),
  Low = 1,
  High = lists:min(Cleaned) * K,
  binary_search(Low, High, High, K, Subsets).

generate_subsets([]) -> [];
generate_subsets([H | T]) ->
  Rest = generate_subsets(T),
  [{H, 1}] ++ [{lcm(H, L), -S} || {L, S} <- Rest] ++ Rest.

gcd(A, 0) -> A;
gcd(A, B) -> gcd(B, A rem B).

lcm(A, B) -> (A div gcd(A, B)) * B.

binary_search(Low, High, Ans, K, Subsets) when Low =< High ->
  Mid = Low + (High - Low) div 2,
  Count = calculate_count(Mid, Subsets),
  if
    Count >= K -> binary_search(Low, Mid - 1, Mid, K, Subsets);
    true -> binary_search(Mid + 1, High, Ans, K, Subsets)
  end;
binary_search(_Low, _High, Ans, _K, _Subsets) -> Ans.

calculate_count(Mid, Subsets) ->
  lists:foldl(fun({L, S}, Acc) -> Acc + (Mid div L) * S end, 0, Subsets).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec find_kth_smallest(coins :: [integer], k :: integer) :: integer
  def find_kth_smallest(coins, k) do
    cleaned = Enum.filter(coins, fn c ->
      !Enum.any?(coins, fn other -> c != other and rem(c, other) == 0 end)
    end)
    subsets = generate_subsets(cleaned)
    low = 1
    high = Enum.min(cleaned) * k
    binary_search(low, high, high, k, subsets)
  end

  defp generate_subsets([]), do: []
  defp generate_subsets([h | t]) do
    rest = generate_subsets(t)
    [{h, 1}] ++ Enum.map(rest, fn {l, s} -> {lcm(h, l), -s} end) ++ rest
  end

  defp gcd(a, 0), do: a
  defp gcd(a, b), do: gcd(b, rem(a, b))

  defp lcm(a, b), do: div(a, gcd(a, b)) * b

  defp binary_search(low, high, ans, k, subsets) when low <= high do
    mid = div(low + high, 2)
    count = calculate_count(mid, subsets)
    if count >= k do
      binary_search(low, mid - 1, mid, k, subsets)
    else
      binary_search(mid + 1, high, ans, k, subsets)
    end
  end
  defp binary_search(_low, _high, ans, _k, _subsets), do: ans

  defp calculate_count(mid, subsets) do
    Enum.reduce(subsets, 0, fn {l, s}, acc -> acc + div(mid, l) * s end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(2^n \cdot \log(k \cdot \min(c)) + n^2), where $n$ is the number of distinct coins. We first filter out redundant coins (those that are multiples of another coin in the set) in $O(n^2)$. We then precompute the LCM and sign for all $2^n - 1$ subsets of coins whose LCM does not exceed our search bound. The binary search takes $O(\log(k \cdot \min(c)))$ iterations, and each iteration evaluates the Inclusion-Exclusion Principle sum in $O(2^n)$. With $n \le 15$ and approximately 40 binary search steps, the algorithm executes roughly $1.3 \times 10^6$ operations.
- **Space Complexity:** O(2^n) to store the precomputed LCMs and signs of all subsets. For $n = 15$, this results in $2^{15} - 1 = 32,767$ entries, which is well within standard memory limits.
