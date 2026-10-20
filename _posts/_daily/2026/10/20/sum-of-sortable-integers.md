---
layout: post
title: "Sum of Sortable Integers"
date: 2026-10-20 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Math", "Sorting", "Enumeration"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/sum-of-sortable-integers/
ai_solutions:
  - solutions:
      cpp: '// Generation failed for C++

        // Reason: Error: 500 INTERNAL. {''error'': {''code'': 500, ''message'': ''Internal
        error encountered.'', ''status'': ''INTERNAL''}}'
      java: '// Generation failed for Java

        // Reason: Error: 500 INTERNAL. {''error'': {''code'': 500, ''message'': ''Internal
        error encountered.'', ''status'': ''INTERNAL''}}'
      python: '// Generation failed for Python

        // Reason: Error: 500 INTERNAL. {''error'': {''code'': 500, ''message'': ''Internal
        error encountered.'', ''status'': ''INTERNAL''}}'
      python3: "import random\n\nclass Solution:\n    def sortableIntegers(self, nums:\
        \ list[int]) -> int:\n        n = len(nums)\n        if n == 0: return 0\n\n\
        \        S = sorted(nums)\n        unique_nums = list(set(nums))\n        val_map\
        \ = {v: random.getrandbits(64) for v in unique_nums}\n\n        P = [0] * (n\
        \ + 1)\n        Q = [0] * (n + 1)\n        for i in range(n):\n            P[i+1]\
        \ = P[i] + val_map[nums[i]]\n            Q[i+1] = Q[i] + val_map[S[i]]\n\n \
        \       preD = [0] * n\n        for i in range(n - 1):\n            preD[i+1]\
        \ = preD[i] + (1 if nums[i] > nums[i+1] else 0)\n\n        def check(k):\n \
        \           for j in range(0, n, k):\n                if P[j+k] - P[j] != Q[j+k]\
        \ - Q[j]:\n                    return False\n                desc_cnt = preD[j+k-1]\
        \ - preD[j]\n                if desc_cnt > 1:\n                    return False\n\
        \                if desc_cnt == 1:\n                    if nums[j] < nums[j+k-1]:\n\
        \                        return False\n            return True\n\n        ans\
        \ = 0\n        for k in range(1, int(n**0.5) + 1):\n            if n % k ==\
        \ 0:\n                if check(k): ans += k\n                if k * k != n:\n\
        \                    if check(n // k): ans += n // k\n        return ans"
      c: "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nunsigned long\
        \ long splitmix64(unsigned long long x) {\n    x += 0x9e3779b97f4a7c15ULL;\n\
        \    x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;\n    x = (x ^ (x >> 27)) *\
        \ 0x94d049bb133111ebULL;\n    return x ^ (x >> 31);\n}\n\nint compare(const\
        \ void* a, const void* b) {\n    int arg1 = *(const int*)a;\n    int arg2 =\
        \ *(const int*)b;\n    if (arg1 < arg2) return -1;\n    if (arg1 > arg2) return\
        \ 1;\n    return 0;\n}\n\nint sortableIntegers(int* nums, int numsSize) {\n\
        \    int n = numsSize;\n    int* S = (int*)malloc(n * sizeof(int));\n    memcpy(S,\
        \ nums, n * sizeof(int));\n    qsort(S, n, sizeof(int), compare);\n\n    unsigned\
        \ long long* valMap = (unsigned long long*)malloc(100001 * sizeof(unsigned long\
        \ long));\n    for (int i = 0; i <= 100000; i++) valMap[i] = splitmix64(i);\n\
        \n    unsigned long long* P = (unsigned long long*)malloc((n + 1) * sizeof(unsigned\
        \ long long));\n    unsigned long long* Q = (unsigned long long*)malloc((n +\
        \ 1) * sizeof(unsigned long long));\n    P[0] = Q[0] = 0;\n    for (int i =\
        \ 0; i < n; i++) {\n        P[i + 1] = P[i] + valMap[nums[i]];\n        Q[i\
        \ + 1] = Q[i] + valMap[S[i]];\n    }\n\n    int* preD = (int*)malloc(n * sizeof(int));\n\
        \    preD[0] = 0;\n    for (int i = 0; i < n - 1; i++) {\n        preD[i + 1]\
        \ = preD[i] + (nums[i] > nums[i + 1] ? 1 : 0);\n    }\n\n    long long totalK\
        \ = 0;\n    for (int k = 1; k <= n; k++) {\n        if (n % k == 0) {\n    \
        \        int possible = 1;\n            for (int j = 0; j < n; j += k) {\n \
        \               if (P[j + k] - P[j] != Q[j + k] - Q[j]) {\n                \
        \    possible = 0;\n                    break;\n                }\n        \
        \        int desc_cnt = preD[j + k - 1] - preD[j];\n                if (desc_cnt\
        \ > 1) {\n                    possible = 0;\n                    break;\n  \
        \              }\n                if (desc_cnt == 1) {\n                   \
        \ if (nums[j] < nums[j + k - 1]) {\n                        possible = 0;\n\
        \                        break;\n                    }\n                }\n\
        \            }\n            if (possible) totalK += k;\n        }\n    }\n\n\
        \    free(S); free(valMap); free(P); free(Q); free(preD);\n    return (int)totalK;\n\
        }"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int SortableIntegers(int[] nums) {\n        int n = nums.Length;\n\
        \        int[] sorted = (int[])nums.Clone();\n        Array.Sort(sorted);\n\n\
        \        ulong[] valMap = new ulong[100001];\n        for (int i = 0; i <= 100000;\
        \ i++) {\n            ulong x = (ulong)i + 0x9e3779b97f4a7c15UL;\n         \
        \   x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9UL;\n            x = (x ^ (x >>\
        \ 27)) * 0x94d049bb133111ebUL;\n            valMap[i] = x ^ (x >> 31);\n   \
        \     }\n\n        ulong[] P = new ulong[n + 1];\n        ulong[] Q = new ulong[n\
        \ + 1];\n        P[0] = Q[0] = 0;\n        for (int i = 0; i < n; i++) {\n \
        \           P[i + 1] = P[i] + valMap[nums[i]];\n            Q[i + 1] = Q[i]\
        \ + valMap[sorted[i]];\n        }\n\n        int[] preD = new int[n];\n    \
        \    preD[0] = 0;\n        for (int i = 0; i < n - 1; i++) {\n            preD[i\
        \ + 1] = preD[i] + (nums[i] > nums[i + 1] ? 1 : 0);\n        }\n\n        long\
        \ sumK = 0;\n        for (int k = 1; k <= n; k++) {\n            if (n % k ==\
        \ 0) {\n                bool possible = true;\n                for (int j =\
        \ 0; j < n; j += k) {\n                    if (P[j + k] - P[j] != Q[j + k] -\
        \ Q[j]) {\n                        possible = false;\n                     \
        \   break;\n                    }\n                    int descCnt = preD[j\
        \ + k - 1] - preD[j];\n                    if (descCnt > 1) {\n            \
        \            possible = false;\n                        break;\n           \
        \         }\n                    if (descCnt == 1 && nums[j] < nums[j + k -\
        \ 1]) {\n                        possible = false;\n                       \
        \ break;\n                    }\n                }\n                if (possible)\
        \ sumK += k;\n            }\n        }\n\n        return (int)sumK;\n    }\n\
        }"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar sortableIntegers\
        \ = function(nums) {\n    const n = nums.length;\n    const S = [...nums].sort((a,\
        \ b) => a - b);\n    const valMap = new BigUint64Array(100001);\n    for (let\
        \ i = 0; i <= 100000; i++) {\n        let x = BigInt(i) + 0x9e3779b97f4a7c15n;\n\
        \        x = (x ^ (x >> 30n)) * 0xbf58476d1ce4e5b9n;\n        x = (x ^ (x >>\
        \ 27n)) * 0x94d049bb133111ebn;\n        valMap[i] = x ^ (x >> 31n);\n    }\n\
        \n    const P = new BigUint64Array(n + 1);\n    const Q = new BigUint64Array(n\
        \ + 1);\n    P[0] = 0n; Q[0] = 0n;\n    for (let i = 0; i < n; i++) {\n    \
        \    P[i + 1] = P[i] + valMap[nums[i]];\n        Q[i + 1] = Q[i] + valMap[S[i]];\n\
        \    }\n\n    const preD = new Int32Array(n);\n    preD[0] = 0;\n    for (let\
        \ i = 0; i < n - 1; i++) {\n        preD[i + 1] = preD[i] + (nums[i] > nums[i\
        \ + 1] ? 1 : 0);\n    }\n\n    let sumK = 0;\n    for (let k = 1; k <= n; k++)\
        \ {\n        if (n % k === 0) {\n            let possible = true;\n        \
        \    for (let j = 0; j < n; j += k) {\n                if (P[j + k] - P[j] !==\
        \ Q[j + k] - Q[j]) {\n                    possible = false;\n              \
        \      break;\n                }\n                const descCnt = preD[j + k\
        \ - 1] - preD[j];\n                if (descCnt > 1) {\n                    possible\
        \ = false;\n                    break;\n                }\n                if\
        \ (descCnt === 1 && nums[j] < nums[j + k - 1]) {\n                    possible\
        \ = false;\n                    break;\n                }\n            }\n \
        \           if (possible) sumK += k;\n        }\n    }\n\n    return sumK;\n\
        };"
      typescript: "function sortableIntegers(nums: number[]): number {\n    const n\
        \ = nums.length;\n    const target = [...nums].sort((a, b) => a - b);\n    const\
        \ hashes = new BigUint64Array(100001);\n    let hSeed = 123456789n;\n    for\
        \ (let i = 0; i <= 100000; i++) {\n        hSeed = (hSeed * 6364136223846793005n\
        \ + 1442695040888963407n) & 0xFFFFFFFFFFFFFFFFn;\n        hashes[i] = hSeed;\n\
        \    }\n\n    const prefixHashNums = new BigUint64Array(n + 1);\n    const prefixHashTarget\
        \ = new BigUint64Array(n + 1);\n    for (let i = 0; i < n; i++) {\n        prefixHashNums[i\
        \ + 1] = (prefixHashNums[i] + hashes[nums[i]]) & 0xFFFFFFFFFFFFFFFFn;\n    \
        \    prefixHashTarget[i + 1] = (prefixHashTarget[i] + hashes[target[i]]) & 0xFFFFFFFFFFFFFFFFn;\n\
        \    }\n\n    const prefixDrops = new Int32Array(n);\n    for (let i = 0; i\
        \ < n - 1; i++) {\n        prefixDrops[i] = nums[i] > nums[i + 1] ? 1 : 0;\n\
        \        if (i > 0) prefixDrops[i] += prefixDrops[i - 1];\n    }\n\n    const\
        \ check = (k: number): boolean => {\n        const mCount = n / k;\n       \
        \ for (let m = 0; m < mCount; m++) {\n            const start = m * k;\n   \
        \         const end = (m + 1) * k - 1;\n            const hNums = (prefixHashNums[end\
        \ + 1] - prefixHashNums[start]) & 0xFFFFFFFFFFFFFFFFn;\n            const hTarget\
        \ = (prefixHashTarget[end + 1] - prefixHashTarget[start]) & 0xFFFFFFFFFFFFFFFFn;\n\
        \            if (hNums !== hTarget) return false;\n            if (k > 1) {\n\
        \                let numDrops = prefixDrops[end - 1];\n                if (start\
        \ > 0) numDrops -= prefixDrops[start - 1];\n                if (numDrops > 1)\
        \ return false;\n                if (numDrops === 1 && nums[end] > nums[start])\
        \ return false;\n            }\n        }\n        return true;\n    };\n\n\
        \    let totalSum = 0;\n    for (let k = 1; k * k <= n; k++) {\n        if (n\
        \ % k === 0) {\n            if (check(k)) totalSum += k;\n            const\
        \ otherK = n / k;\n            if (otherK !== k && check(otherK)) totalSum +=\
        \ otherK;\n        }\n    }\n\n    return totalSum;\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function sortableIntegers($nums) {\n        $n = count($nums);\n\
        \        $target = $nums;\n        sort($target);\n\n        $hashes1 = [];\n\
        \        $hashes2 = [];\n        $h_seed1 = 123456789;\n        $h_seed2 = 987654321;\n\
        \        for ($i = 0; $i <= 100000; $i++) {\n            $h_seed1 = ($h_seed1\
        \ * 1103515245 + 12345) % 1000000007;\n            $h_seed2 = ($h_seed2 * 1103515245\
        \ + 12345) % 1000000009;\n            $hashes1[$i] = $h_seed1;\n           \
        \ $hashes2[$i] = $h_seed2;\n        }\n\n        $prefixHash1 = array_fill(0,\
        \ $n + 1, 0);\n        $prefixHash2 = array_fill(0, $n + 1, 0);\n        $targetPrefix1\
        \ = array_fill(0, $n + 1, 0);\n        $targetPrefix2 = array_fill(0, $n + 1,\
        \ 0);\n\n        for ($i = 0; $i < $n; $i++) {\n            $prefixHash1[$i\
        \ + 1] = ($prefixHash1[$i] + $hashes1[$nums[$i]]) % 1000000007;\n          \
        \  $prefixHash2[$i + 1] = ($prefixHash2[$i] + $hashes2[$nums[$i]]) % 1000000009;\n\
        \            $targetPrefix1[$i + 1] = ($targetPrefix1[$i] + $hashes1[$target[$i]])\
        \ % 1000000007;\n            $targetPrefix2[$i + 1] = ($targetPrefix2[$i] +\
        \ $hashes2[$target[$i]]) % 1000000009;\n        }\n\n        $prefixDrops =\
        \ array_fill(0, $n, 0);\n        for ($i = 0; $i < $n - 1; $i++) {\n       \
        \     $prefixDrops[$i] = ($nums[$i] > $nums[$i + 1]) ? 1 : 0;\n            if\
        \ ($i > 0) $prefixDrops[$i] += $prefixDrops[$i - 1];\n        }\n\n        $totalSum\
        \ = 0;\n        $divs = [];\n        for ($i = 1; $i * $i <= $n; $i++) {\n \
        \           if ($n % $i == 0) {\n                $divs[] = $i;\n           \
        \     if ($i * $i != $n) $divs[] = $n / $i;\n            }\n        }\n\n  \
        \      foreach ($divs as $k) {\n            $mCount = $n / $k;\n           \
        \ $ok = true;\n            for ($m = 0; $m < $mCount; $m++) {\n            \
        \    $start = $m * $k;\n                $end = ($m + 1) * $k - 1;\n\n      \
        \          $sum1 = ($prefixHash1[$end + 1] - $prefixHash1[$start] + 1000000007)\
        \ % 1000000007;\n                $tSum1 = ($targetPrefix1[$end + 1] - $targetPrefix1[$start]\
        \ + 1000000007) % 1000000007;\n                if ($sum1 !== $tSum1) { $ok =\
        \ false; break; }\n\n                $sum2 = ($prefixHash2[$end + 1] - $prefixHash2[$start]\
        \ + 1000000009) % 1000000009;\n                $tSum2 = ($targetPrefix2[$end\
        \ + 1] - $targetPrefix2[$start] + 1000000009) % 1000000009;\n              \
        \  if ($sum2 !== $tSum2) { $ok = false; break; }\n\n                if ($k >\
        \ 1) {\n                    $numDrops = $prefixDrops[$end - 1];\n          \
        \          if ($start > 0) $numDrops -= $prefixDrops[$start - 1];\n        \
        \            if ($numDrops > 1) { $ok = false; break; }\n                  \
        \  if ($numDrops == 1 && $nums[$end] > $nums[$start]) { $ok = false; break;\
        \ }\n                }\n            }\n            if ($ok) $totalSum += $k;\n\
        \        }\n\n        return $totalSum;\n    }\n}"
      swift: "class Solution {\n    func sortableIntegers(_ nums: [Int]) -> Int {\n\
        \        let n = nums.count\n        let target = nums.sorted()\n        var\
        \ hashes = [UInt64](repeating: 0, count: 100001)\n        var hSeed: UInt64\
        \ = 123456789\n        for i in 0...100000 {\n            hSeed = hSeed.multipliedReportingOverflow(by:\
        \ 6364136223846793005).partialValue &+ 1442695040888963407\n            hashes[i]\
        \ = hSeed\n        }\n\n        var prefixHashNums = [UInt64](repeating: 0,\
        \ count: n + 1)\n        var prefixHashTarget = [UInt64](repeating: 0, count:\
        \ n + 1)\n        for i in 0..<n {\n            prefixHashNums[i + 1] = prefixHashNums[i]\
        \ &+ hashes[nums[i]]\n            prefixHashTarget[i + 1] = prefixHashTarget[i]\
        \ &+ hashes[target[i]]\n        }\n\n        var prefixDrops = [Int](repeating:\
        \ 0, count: n)\n        if n > 1 {\n            for i in 0..<n-1 {\n       \
        \         prefixDrops[i] = (nums[i] > nums[i + 1] ? 1 : 0)\n               \
        \ if i > 0 { prefixDrops[i] += prefixDrops[i - 1] }\n            }\n       \
        \ }\n\n        func check(_ k: Int) -> Bool {\n            let mCount = n /\
        \ k\n            for m in 0..<mCount {\n                let start = m * k\n\
        \                let end = (m + 1) * k - 1\n                let hNums = prefixHashNums[end\
        \ + 1] &- prefixHashNums[start]\n                let hTarget = prefixHashTarget[end\
        \ + 1] &- prefixHashTarget[start]\n                if hNums != hTarget { return\
        \ false }\n                if k > 1 {\n                    var numDrops = prefixDrops[end\
        \ - 1]\n                    if start > 0 { numDrops -= prefixDrops[start - 1]\
        \ }\n                    if numDrops > 1 { return false }\n                \
        \    if numDrops == 1 && nums[end] > nums[start] { return false }\n        \
        \        }\n            }\n            return true\n        }\n\n        var\
        \ totalSum = 0\n        for k in 1...Int(Double(n).squareRoot()) {\n       \
        \     if n % k == 0 {\n                if check(k) { totalSum += k }\n     \
        \           let otherK = n / k\n                if otherK != k && check(otherK)\
        \ { totalSum += otherK }\n            }\n        }\n\n        return totalSum\n\
        \    }\n}"
      kotlin: "import kotlin.random.Random\n\nclass Solution {\n    fun sortableIntegers(nums:\
        \ IntArray): Int {\n        val n = nums.size\n        val target = nums.copyOf().apply\
        \ { sort() }\n        val random = java.util.Random(42)\n        val hashes\
        \ = LongArray(100001) { random.nextLong() }\n\n        val prefixHashNums =\
        \ LongArray(n + 1)\n        val prefixHashTarget = LongArray(n + 1)\n      \
        \  for (i in 0 until n) {\n            prefixHashNums[i + 1] = prefixHashNums[i]\
        \ + hashes[nums[i]]\n            prefixHashTarget[i + 1] = prefixHashTarget[i]\
        \ + hashes[target[i]]\n        }\n\n        val prefixDrops = IntArray(n)\n\
        \        for (i in 0 until n - 1) {\n            prefixDrops[i] = if (nums[i]\
        \ > nums[i + 1]) 1 else 0\n            if (i > 0) prefixDrops[i] += prefixDrops[i\
        \ - 1]\n        }\n\n        fun check(k: Int): Boolean {\n            val mCount\
        \ = n / k\n            for (m in 0 until mCount) {\n                val start\
        \ = m * k\n                val end = (m + 1) * k - 1\n                val hNums\
        \ = prefixHashNums[end + 1] - prefixHashNums[start]\n                val hTarget\
        \ = prefixHashTarget[end + 1] - prefixHashTarget[start]\n                if\
        \ (hNums != hTarget) return false\n                if (k > 1) {\n          \
        \          var numDrops = prefixDrops[end - 1]\n                    if (start\
        \ > 0) numDrops -= prefixDrops[start - 1]\n                    if (numDrops\
        \ > 1) return false\n                    if (numDrops == 1 && nums[end] > nums[start])\
        \ return false\n                }\n            }\n            return true\n\
        \        }\n\n        var totalSum = 0\n        var k = 1\n        while (k\
        \ * k <= n) {\n            if (n % k == 0) {\n                if (check(k))\
        \ totalSum += k\n                val otherK = n / k\n                if (otherK\
        \ != k && check(otherK)) totalSum += otherK\n            }\n            k++\n\
        \        }\n\n        return totalSum\n    }\n}"
      dart: "class Solution {\n  int sortableIntegers(List<int> nums) {\n    int n =\
        \ nums.length;\n    List<int> divisors = [];\n    for (int i = 1; i * i <= n;\
        \ i++) {\n      if (n % i == 0) {\n        divisors.add(i);\n        if (i *\
        \ i != n) {\n          divisors.add(n ~/ i);\n        }\n      }\n    }\n\n\
        \    int sum = 0;\n    for (int k in divisors) {\n      if (check(k, nums, n))\
        \ {\n        sum += k;\n      }\n    }\n    return sum;\n  }\n\n  bool check(int\
        \ k, List<int> nums, int n) {\n    int prevMax = -1;\n    for (int i = 0; i\
        \ < n; i += k) {\n      int bMin = nums[i];\n      int bMax = nums[i];\n   \
        \   int drops = 0;\n      for (int j = i; j < i + k; j++) {\n        int val\
        \ = nums[j];\n        if (val < bMin) bMin = val;\n        if (val > bMax) bMax\
        \ = val;\n        if (j < i + k - 1 && nums[j] > nums[j + 1]) {\n          drops++;\n\
        \        }\n      }\n      if (drops > 1) return false;\n      if (drops ==\
        \ 1 && nums[i + k - 1] > nums[i]) return false;\n      if (prevMax != -1 &&\
        \ prevMax > bMin) return false;\n      prevMax = bMax;\n    }\n    return true;\n\
        \  }\n}"
      go: "func sortableIntegers(nums []int) int {\n\tn := len(nums)\n\tdivisors :=\
        \ []int{}\n\tfor i := 1; i*i <= n; i++ {\n\t\tif n%i == 0 {\n\t\t\tdivisors\
        \ = append(divisors, i)\n\t\t\tif i*i != n {\n\t\t\t\tdivisors = append(divisors,\
        \ n/i)\n\t\t\t}\n\t\t}\n\t}\n\n\tsum := 0\n\tfor _, k := range divisors {\n\t\
        \tif check(k, nums, n) {\n\t\t\tsum += k\n\t\t}\n\t}\n\treturn sum\n}\n\nfunc\
        \ check(k int, nums []int, n int) bool {\n\tprevMax := -1\n\tfor i := 0; i <\
        \ n; i += k {\n\t\tbMin := nums[i]\n\t\tbMax := nums[i]\n\t\tdrops := 0\n\t\t\
        for j := i; j < i+k; j++ {\n\t\t\tval := nums[j]\n\t\t\tif val < bMin {\n\t\t\
        \t\tbMin = val\n\t\t\t}\n\t\t\tif val > bMax {\n\t\t\t\tbMax = val\n\t\t\t}\n\
        \t\t\tif j < i+k-1 && nums[j] > nums[j+1] {\n\t\t\t\tdrops++\n\t\t\t}\n\t\t\
        }\n\t\tif drops > 1 {\n\t\t\treturn false\n\t\t}\n\t\tif drops == 1 && nums[i+k-1]\
        \ > nums[i] {\n\t\t\treturn false\n\t\t}\n\t\tif prevMax != -1 && prevMax >\
        \ bMin {\n\t\t\treturn false\n\t\t}\n\t\tprevMax = bMax\n\t}\n\treturn true\n\
        }"
      ruby: "def sortable_integers(nums)\n  n = nums.length\n  divisors = []\n  i =\
        \ 1\n  while i * i <= n\n    if n % i == 0\n      divisors << i\n      divisors\
        \ << n / i if i * i != n\n    end\n    i += 1\n  end\n\n  sum = 0\n  divisors.each\
        \ do |k|\n    sum += k if check_sortable(k, nums, n)\n  end\n  sum\nend\n\n\
        def check_sortable(k, nums, n)\n  prev_max = -1\n  i = 0\n  while i < n\n  \
        \  b_min = nums[i]\n    b_max = nums[i]\n    drops = 0\n    j = i\n    while\
        \ j < i + k\n      val = nums[j]\n      b_min = val if val < b_min\n      b_max\
        \ = val if val > b_max\n      if j < i + k - 1 && nums[j] > nums[j + 1]\n  \
        \      drops += 1\n      end\n      j += 1\n    end\n    return false if drops\
        \ > 1\n    return false if drops == 1 && nums[i + k - 1] > nums[i]\n    return\
        \ false if prev_max != -1 && prev_max > b_min\n    prev_max = b_max\n    i +=\
        \ k\n  end\n  true\nend"
      scala: "object Solution {\n  def sortableIntegers(nums: Array[Int]): Int = {\n\
        \    val n = nums.length\n    val divisors = scala.collection.mutable.ArrayBuffer[Int]()\n\
        \    var i = 1\n    while (i * i <= n) {\n      if (n % i == 0) {\n        divisors\
        \ += i\n        if (i * i != n) {\n          divisors += n / i\n        }\n\
        \      }\n      i += 1\n    }\n\n    var sum = 0\n    for (k <- divisors) {\n\
        \      if (check(k, nums, n)) {\n        sum += k\n      }\n    }\n    sum\n\
        \  }\n\n  private def check(k: Int, nums: Array[Int], n: Int): Boolean = {\n\
        \    var prevMax = -1\n    var i = 0\n    while (i < n) {\n      var bMin =\
        \ nums(i)\n      var bMax = nums(i)\n      var drops = 0\n      var j = i\n\
        \      while (j < i + k) {\n        val v = nums(j)\n        if (v < bMin) bMin\
        \ = v\n        if (v > bMax) bMax = v\n        if (j < i + k - 1 && nums(j)\
        \ > nums(j + 1)) {\n          drops += 1\n        }\n        j += 1\n      }\n\
        \      if (drops > 1) return false\n      if (drops == 1 && nums(i + k - 1)\
        \ > nums(i)) return false\n      if (prevMax != -1 && prevMax > bMin) return\
        \ false\n      prevMax = bMax\n      i += k\n    }\n    true\n  }\n}"
      rust: "impl Solution {\n    pub fn sortable_integers(nums: Vec<i32>) -> i32 {\n\
        \        let n = nums.len();\n        if n == 0 { return 0; }\n        let mut\
        \ s = nums.clone();\n        s.sort_unstable();\n\n        let mut val_hashes\
        \ = vec![0u64; 100001];\n        let mut h: u64 = 123456789;\n        for i\
        \ in 0..100001 {\n            h = h.wrapping_mul(6364136223846793005).wrapping_add(1);\n\
        \            val_hashes[i] = h;\n        }\n\n        let mut prefix_h_nums\
        \ = vec![0u64; n + 1];\n        let mut prefix_h_s = vec![0u64; n + 1];\n  \
        \      for i in 0..n {\n            prefix_h_nums[i + 1] = prefix_h_nums[i].wrapping_add(val_hashes[nums[i]\
        \ as usize]);\n            prefix_h_s[i + 1] = prefix_h_s[i].wrapping_add(val_hashes[s[i]\
        \ as usize]);\n        }\n\n        let mut prefix_desc = vec![0; n];\n    \
        \    for i in 0..n - 1 {\n            let d = if nums[i] > nums[i + 1] { 1 }\
        \ else { 0 };\n            prefix_desc[i + 1] = prefix_desc[i] + d;\n      \
        \  }\n\n        let mut total_sum = 0;\n        for k in 1..=n {\n         \
        \   if n % k == 0 {\n                let mut possible = true;\n            \
        \    for i in (0..n).step_by(k) {\n                    if prefix_h_nums[i +\
        \ k] - prefix_h_nums[i] != prefix_h_s[i + k] - prefix_h_s[i] {\n           \
        \             possible = false;\n                        break;\n          \
        \          }\n                    let num_descents = prefix_desc[i + k - 1]\
        \ - prefix_desc[i];\n                    if num_descents > 1 {\n           \
        \             possible = false;\n                        break;\n          \
        \          }\n                    if num_descents == 1 && nums[i + k - 1] >\
        \ nums[i] {\n                        possible = false;\n                   \
        \     break;\n                    }\n                }\n                if possible\
        \ {\n                    total_sum += k;\n                }\n            }\n\
        \        }\n        total_sum as i32\n    }\n}"
      racket: "(define/contract (sortable-integers nums)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let* ([n (length nums)]\n         [nums-vec (list->vector\
        \ nums)]\n         [s-vec (list->vector (sort nums <))]\n         [val-hashes\
        \ (let ([v (make-vector 100001)])\n                       (let loop ([i 0] [h\
        \ 123456789])\n                         (if (< i 100001)\n                 \
        \            (let ([next-h (modulo (+ (* h 6364136223846793005) 1) (expt 2 64))])\n\
        \                               (vector-set! v i next-h)\n                 \
        \              (loop (+ i 1) next-h))\n                             v)))]\n\
        \         [prefix-h-nums (let ([v (make-vector (+ n 1) 0)])\n              \
        \            (for ([i (in-range n)])\n                            (vector-set!\
        \ v (+ i 1) (+ (vector-ref v i) (vector-ref val-hashes (vector-ref nums-vec\
        \ i)))))\n                          v)]\n         [prefix-h-s (let ([v (make-vector\
        \ (+ n 1) 0)])\n                       (for ([i (in-range n)])\n           \
        \              (vector-set! v (+ i 1) (+ (vector-ref v i) (vector-ref val-hashes\
        \ (vector-ref s-vec i)))))\n                       v)]\n         [prefix-desc\
        \ (let ([v (make-vector n 0)])\n                        (for ([i (in-range (-\
        \ n 1))])\n                          (let ([d (if (> (vector-ref nums-vec i)\
        \ (vector-ref nums-vec (+ i 1))) 1 0)])\n                            (vector-set!\
        \ v (+ i 1) (+ (vector-ref v i) d))))\n                        v)])\n    (for/fold\
        \ ([total-sum 0])\n              ([k (in-range 1 (+ n 1))]\n               #:when\
        \ (zero? (remainder n k)))\n      (let ([possible (for/and ([i (in-range 0 n\
        \ k)])\n                        (and (= (- (vector-ref prefix-h-nums (+ i k))\
        \ (vector-ref prefix-h-nums i))\n                                (- (vector-ref\
        \ prefix-h-s (+ i k)) (vector-ref prefix-h-s i)))\n                        \
        \     (let ([num-descents (- (vector-ref prefix-desc (+ i k -1)) (vector-ref\
        \ prefix-desc i))])\n                               (or (zero? num-descents)\n\
        \                                   (and (= num-descents 1)\n              \
        \                          (<= (vector-ref nums-vec (+ i k -1)) (vector-ref\
        \ nums-vec i)))))))])\n        (if possible (+ total-sum k) total-sum)))))"
      erlang: "-spec sortable_integers(Nums :: [integer()]) -> integer().\nsortable_integers(Nums)\
        \ ->\n  N = length(Nums),\n  NumsVec = list_to_tuple(Nums),\n  SortedNums =\
        \ lists:sort(Nums),\n  SortedVec = list_to_tuple(SortedNums),\n\n  GenerateHashes\
        \ = fun F(0, _H, Acc) -> Acc;\n                       F(I, H, Acc) ->\n    \
        \                     NextH = (H * 6364136223846793005 + 1) band 18446744073709551615,\n\
        \                         F(I - 1, NextH, [NextH | Acc])\n                 \
        \  end,\n  ValHashes = list_to_tuple(GenerateHashes(100001, 123456789, [])),\n\
        \n  PrefixHNums = list_to_tuple(lists:reverse(lists:foldl(fun(X, [H|T]) -> [H\
        \ + element(X + 1, ValHashes) | [H|T]] end, [0], Nums))),\n  PrefixHS = list_to_tuple(lists:reverse(lists:foldl(fun(X,\
        \ [H|T]) -> [H + element(X + 1, ValHashes) | [H|T]] end, [0], SortedNums))),\n\
        \n  Descents = [if element(I, NumsVec) > element(I + 1, NumsVec) -> 1; true\
        \ -> 0 end || I <- lists:seq(1, N - 1)],\n  PrefixDesc = list_to_tuple(lists:reverse(lists:foldl(fun(X,\
        \ [H|T]) -> [H + X | [H|T]] end, [0], Descents))),\n\n  Divisors = [K || K <-\
        \ lists:seq(1, N), N rem K =:= 0],\n\n  CheckBlock = fun(I, K) ->\n        \
        \         MultisetMatch = (element(I + K + 1, PrefixHNums) - element(I + 1,\
        \ PrefixHNums)) =:= (element(I + K + 1, PrefixHS) - element(I + 1, PrefixHS)),\n\
        \                 NumDesc = if K > 1 -> element(I + K, PrefixDesc) - element(I\
        \ + 1, PrefixDesc); true -> 0 end,\n                 CyclicallySorted = (NumDesc\
        \ =:= 0) or ((NumDesc =:= 1) and (element(I + K, NumsVec) =< element(I + 1,\
        \ NumsVec))),\n                 MultisetMatch and CyclicallySorted\n       \
        \        end,\n\n  CheckK = fun(K) ->\n             lists:all(fun(I) -> CheckBlock(I,\
        \ K) end, lists:seq(0, N - K, K))\n           end,\n\n  lists:foldl(fun(K, Sum)\
        \ -> if CheckK(K) -> Sum + K; true -> Sum end end, 0, Divisors)."
      elixir: "defmodule Solution do\n  @spec sortable_integers(nums :: [integer]) ::\
        \ integer\n  def sortable_integers(nums) do\n    n = length(nums)\n    nums_tuple\
        \ = List.to_tuple(nums)\n    sorted_nums = Enum.sort(nums)\n    sorted_tuple\
        \ = List.to_tuple(sorted_nums)\n\n    generate_hashes = fn count, seed ->\n\
        \      Enum.reduce(0..count, {[], seed}, fn _, {acc, h} ->\n        next_h =\
        \ rem(h * 6364136223846793005 + 1, 18446744073709551616)\n        {[next_h |\
        \ acc], next_h}\n      end) |> elem(0) |> Enum.reverse() |> List.to_tuple()\n\
        \    end\n    val_hashes = generate_hashes.(100000, 123456789)\n\n    prefix_h_nums\
        \ = Enum.reduce(nums, [0], fn x, [h | t] -> [h + elem(val_hashes, x) | [h |\
        \ t]] end) |> Enum.reverse() |> List.to_tuple()\n    prefix_h_s = Enum.reduce(sorted_nums,\
        \ [0], fn x, [h | t] -> [h + elem(val_hashes, x) | [h | t]] end) |> Enum.reverse()\
        \ |> List.to_tuple()\n\n    descents = for i <- 0..(n - 2), n > 1, do: (if elem(nums_tuple,\
        \ i) > elem(nums_tuple, i + 1), do: 1, else: 0)\n    prefix_desc = Enum.reduce(descents,\
        \ [0], fn x, [h | t] -> [h + x | [h | t]] end) |> Enum.reverse() |> List.to_tuple()\n\
        \n    divisors = for k <- 1..n, rem(n, k) == 0, do: k\n\n    Enum.reduce(divisors,\
        \ 0, fn k, sum ->\n      possible = Enum.all?(0..max(0, n - k) |> Stream.take_every(k),\
        \ fn i ->\n        multiset_match = (elem(prefix_h_nums, i + k) - elem(prefix_h_nums,\
        \ i)) == (elem(prefix_h_s, i + k) - elem(prefix_h_s, i))\n        num_desc =\
        \ if k > 1, do: elem(prefix_desc, i + k - 1) - elem(prefix_desc, i), else: 0\n\
        \        cyclically_sorted = (num_desc == 0) or (num_desc == 1 and elem(nums_tuple,\
        \ i + k - 1) <= elem(nums_tuple, i))\n        multiset_match and cyclically_sorted\n\
        \      end)\n      if possible, do: sum + k, else: sum\n    end)\n  end\nend"
    approach: 'The core problem is to determine which divisors $k$ of $n$ allow the
      array to be sorted by independently rotating each $k$-length block. A block can
      be cyclically rotated into its sorted counterpart if and only if two conditions
      are met: the block must be a ''circularly sorted'' array (containing at most one
      descent, and if one exists, the first element must be greater than or equal to
      the last), and the multiset of elements in the block must match the multiset of
      elements in the corresponding segment of the globally sorted array. Checking these
      conditions for every divisor $k$ efficiently is key.'
    time_complexity: O(n \log n + \sigma(n)), where n is the length of the array and
      \sigma(n)$ is the sum of divisors of $n$. Sorting takes $O(n \log n)$, while precalculating
      prefix hashes and descents takes $O(n)$. The final check for all divisors $k$
      iterates through blocks, resulting in a total of $\sum_{k|n} n/k = \sigma(n)$
      operations. For $n=10^5$, $\sigma(n)$ is at most 248,760, making the algorithm
      extremely efficient.
    space_complexity: O(n), as we store the sorted array, prefix sums of multiset hashes,
      and prefix counts of descents, each requiring $O(n)$ space.
    elapsed_time: 663.3029618263245
    model: gemini-3-flash-preview
    generated_at: '2026-10-20 03:01:46 '
---

## Problem #3886: Sum of Sortable Integers

**Difficulty:** Hard

**Topics:** Array, Math, Sorting, Enumeration

## Problem Description

<p>You are given an integer array <code>nums</code> of length <code>n</code>.</p>

<p>An integer <code>k</code> is called <strong>sortable</strong> if <code>k</code> <strong>divides</strong> <code>n</code> and you can sort <code>nums</code> in <strong>non-decreasing</strong> order by sequentially performing the following operations:</p>

<ul>
	<li>Partition <code>nums</code> into <strong>consecutive <span data-keyword="subarray-nonempty">subarrays</span></strong> of length <code>k</code>.</li>
	<li><strong>Cyclically rotate each subarray independently</strong> any number of times to the left or to the right.</li>
</ul>

<p>Return an integer denoting the sum of all possible sortable integers <code>k</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,1,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong>​​​​​​​</p>

<ul>
	<li>For <code>n = 3</code>, possible divisors are 1 and 3.</li>
	<li>For <code>k = 1</code>: each subarray has one element. No rotation can sort the array.</li>
	<li>For <code>k = 3</code>: the single subarray <code>[3, 1, 2]</code> can be rotated once to produce <code>[1, 2, 3]</code>, which is sorted.</li>
	<li>Only <code>k = 3</code> is sortable. Hence, the answer is 3.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [7,6,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>For <code>n = 3</code>, possible divisors are 1 and 3.</li>
	<li>For <code>k = 1</code>: each subarray has one element. No rotation can sort the array.</li>
	<li>For <code>k = 3</code>: the single subarray <code>[7, 6, 5]</code> cannot be rotated into non-decreasing order.</li>
	<li>No <code>k</code> is sortable. Hence, the answer is 0.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,8]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong>​​​​​​​</p>

<ul>
	<li>For <code>n = 2</code>, possible divisors are 1 and 2.</li>
	<li>Since <code>[5, 8]</code> is already sorted, every divisor is sortable. Hence, the answer is <code>1 + 2 = 3</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. First, observe that `k` must divide `n`, since the array is partitioned into subarrays of length `k`. Iterate over all divisors of `n`.

2. Let `s` be the sorted version of the array. For each divisor `k`, check every block `[i, i+k)`.

3. A block can be rotated to match its sorted counterpart if the sorted segment `s[i..i+k-1]` appears as a cyclic rotation of `nums[i..i+k-1]`.

4. You can test this by checking whether the sorted segment exists inside two concatenated copies of the block. If all blocks satisfy this, then `k` is sortable.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The core problem is to determine which divisors $k$ of $n$ allow the array to be sorted by independently rotating each $k$-length block. A block can be cyclically rotated into its sorted counterpart if and only if two conditions are met: the block must be a 'circularly sorted' array (containing at most one descent, and if one exists, the first element must be greater than or equal to the last), and the multiset of elements in the block must match the multiset of elements in the corresponding segment of the globally sorted array. Checking these conditions for every divisor $k$ efficiently is key.

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
// Generation failed for C++
// Reason: Error: 500 INTERNAL. {'error': {'code': 500, 'message': 'Internal error encountered.', 'status': 'INTERNAL'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
// Generation failed for Java
// Reason: Error: 500 INTERNAL. {'error': {'code': 500, 'message': 'Internal error encountered.', 'status': 'INTERNAL'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
// Generation failed for Python
// Reason: Error: 500 INTERNAL. {'error': {'code': 500, 'message': 'Internal error encountered.', 'status': 'INTERNAL'}}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import random

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0: return 0

        S = sorted(nums)
        unique_nums = list(set(nums))
        val_map = {v: random.getrandbits(64) for v in unique_nums}

        P = [0] * (n + 1)
        Q = [0] * (n + 1)
        for i in range(n):
            P[i+1] = P[i] + val_map[nums[i]]
            Q[i+1] = Q[i] + val_map[S[i]]

        preD = [0] * n
        for i in range(n - 1):
            preD[i+1] = preD[i] + (1 if nums[i] > nums[i+1] else 0)

        def check(k):
            for j in range(0, n, k):
                if P[j+k] - P[j] != Q[j+k] - Q[j]:
                    return False
                desc_cnt = preD[j+k-1] - preD[j]
                if desc_cnt > 1:
                    return False
                if desc_cnt == 1:
                    if nums[j] < nums[j+k-1]:
                        return False
            return True

        ans = 0
        for k in range(1, int(n**0.5) + 1):
            if n % k == 0:
                if check(k): ans += k
                if k * k != n:
                    if check(n // k): ans += n // k
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

unsigned long long splitmix64(unsigned long long x) {
    x += 0x9e3779b97f4a7c15ULL;
    x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
    x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
    return x ^ (x >> 31);
}

int compare(const void* a, const void* b) {
    int arg1 = *(const int*)a;
    int arg2 = *(const int*)b;
    if (arg1 < arg2) return -1;
    if (arg1 > arg2) return 1;
    return 0;
}

int sortableIntegers(int* nums, int numsSize) {
    int n = numsSize;
    int* S = (int*)malloc(n * sizeof(int));
    memcpy(S, nums, n * sizeof(int));
    qsort(S, n, sizeof(int), compare);

    unsigned long long* valMap = (unsigned long long*)malloc(100001 * sizeof(unsigned long long));
    for (int i = 0; i <= 100000; i++) valMap[i] = splitmix64(i);

    unsigned long long* P = (unsigned long long*)malloc((n + 1) * sizeof(unsigned long long));
    unsigned long long* Q = (unsigned long long*)malloc((n + 1) * sizeof(unsigned long long));
    P[0] = Q[0] = 0;
    for (int i = 0; i < n; i++) {
        P[i + 1] = P[i] + valMap[nums[i]];
        Q[i + 1] = Q[i] + valMap[S[i]];
    }

    int* preD = (int*)malloc(n * sizeof(int));
    preD[0] = 0;
    for (int i = 0; i < n - 1; i++) {
        preD[i + 1] = preD[i] + (nums[i] > nums[i + 1] ? 1 : 0);
    }

    long long totalK = 0;
    for (int k = 1; k <= n; k++) {
        if (n % k == 0) {
            int possible = 1;
            for (int j = 0; j < n; j += k) {
                if (P[j + k] - P[j] != Q[j + k] - Q[j]) {
                    possible = 0;
                    break;
                }
                int desc_cnt = preD[j + k - 1] - preD[j];
                if (desc_cnt > 1) {
                    possible = 0;
                    break;
                }
                if (desc_cnt == 1) {
                    if (nums[j] < nums[j + k - 1]) {
                        possible = 0;
                        break;
                    }
                }
            }
            if (possible) totalK += k;
        }
    }

    free(S); free(valMap); free(P); free(Q); free(preD);
    return (int)totalK;
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
    public int SortableIntegers(int[] nums) {
        int n = nums.Length;
        int[] sorted = (int[])nums.Clone();
        Array.Sort(sorted);

        ulong[] valMap = new ulong[100001];
        for (int i = 0; i <= 100000; i++) {
            ulong x = (ulong)i + 0x9e3779b97f4a7c15UL;
            x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9UL;
            x = (x ^ (x >> 27)) * 0x94d049bb133111ebUL;
            valMap[i] = x ^ (x >> 31);
        }

        ulong[] P = new ulong[n + 1];
        ulong[] Q = new ulong[n + 1];
        P[0] = Q[0] = 0;
        for (int i = 0; i < n; i++) {
            P[i + 1] = P[i] + valMap[nums[i]];
            Q[i + 1] = Q[i] + valMap[sorted[i]];
        }

        int[] preD = new int[n];
        preD[0] = 0;
        for (int i = 0; i < n - 1; i++) {
            preD[i + 1] = preD[i] + (nums[i] > nums[i + 1] ? 1 : 0);
        }

        long sumK = 0;
        for (int k = 1; k <= n; k++) {
            if (n % k == 0) {
                bool possible = true;
                for (int j = 0; j < n; j += k) {
                    if (P[j + k] - P[j] != Q[j + k] - Q[j]) {
                        possible = false;
                        break;
                    }
                    int descCnt = preD[j + k - 1] - preD[j];
                    if (descCnt > 1) {
                        possible = false;
                        break;
                    }
                    if (descCnt == 1 && nums[j] < nums[j + k - 1]) {
                        possible = false;
                        break;
                    }
                }
                if (possible) sumK += k;
            }
        }

        return (int)sumK;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} nums
 * @return {number}
 */
var sortableIntegers = function(nums) {
    const n = nums.length;
    const S = [...nums].sort((a, b) => a - b);
    const valMap = new BigUint64Array(100001);
    for (let i = 0; i <= 100000; i++) {
        let x = BigInt(i) + 0x9e3779b97f4a7c15n;
        x = (x ^ (x >> 30n)) * 0xbf58476d1ce4e5b9n;
        x = (x ^ (x >> 27n)) * 0x94d049bb133111ebn;
        valMap[i] = x ^ (x >> 31n);
    }

    const P = new BigUint64Array(n + 1);
    const Q = new BigUint64Array(n + 1);
    P[0] = 0n; Q[0] = 0n;
    for (let i = 0; i < n; i++) {
        P[i + 1] = P[i] + valMap[nums[i]];
        Q[i + 1] = Q[i] + valMap[S[i]];
    }

    const preD = new Int32Array(n);
    preD[0] = 0;
    for (let i = 0; i < n - 1; i++) {
        preD[i + 1] = preD[i] + (nums[i] > nums[i + 1] ? 1 : 0);
    }

    let sumK = 0;
    for (let k = 1; k <= n; k++) {
        if (n % k === 0) {
            let possible = true;
            for (let j = 0; j < n; j += k) {
                if (P[j + k] - P[j] !== Q[j + k] - Q[j]) {
                    possible = false;
                    break;
                }
                const descCnt = preD[j + k - 1] - preD[j];
                if (descCnt > 1) {
                    possible = false;
                    break;
                }
                if (descCnt === 1 && nums[j] < nums[j + k - 1]) {
                    possible = false;
                    break;
                }
            }
            if (possible) sumK += k;
        }
    }

    return sumK;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function sortableIntegers(nums: number[]): number {
    const n = nums.length;
    const target = [...nums].sort((a, b) => a - b);
    const hashes = new BigUint64Array(100001);
    let hSeed = 123456789n;
    for (let i = 0; i <= 100000; i++) {
        hSeed = (hSeed * 6364136223846793005n + 1442695040888963407n) & 0xFFFFFFFFFFFFFFFFn;
        hashes[i] = hSeed;
    }

    const prefixHashNums = new BigUint64Array(n + 1);
    const prefixHashTarget = new BigUint64Array(n + 1);
    for (let i = 0; i < n; i++) {
        prefixHashNums[i + 1] = (prefixHashNums[i] + hashes[nums[i]]) & 0xFFFFFFFFFFFFFFFFn;
        prefixHashTarget[i + 1] = (prefixHashTarget[i] + hashes[target[i]]) & 0xFFFFFFFFFFFFFFFFn;
    }

    const prefixDrops = new Int32Array(n);
    for (let i = 0; i < n - 1; i++) {
        prefixDrops[i] = nums[i] > nums[i + 1] ? 1 : 0;
        if (i > 0) prefixDrops[i] += prefixDrops[i - 1];
    }

    const check = (k: number): boolean => {
        const mCount = n / k;
        for (let m = 0; m < mCount; m++) {
            const start = m * k;
            const end = (m + 1) * k - 1;
            const hNums = (prefixHashNums[end + 1] - prefixHashNums[start]) & 0xFFFFFFFFFFFFFFFFn;
            const hTarget = (prefixHashTarget[end + 1] - prefixHashTarget[start]) & 0xFFFFFFFFFFFFFFFFn;
            if (hNums !== hTarget) return false;
            if (k > 1) {
                let numDrops = prefixDrops[end - 1];
                if (start > 0) numDrops -= prefixDrops[start - 1];
                if (numDrops > 1) return false;
                if (numDrops === 1 && nums[end] > nums[start]) return false;
            }
        }
        return true;
    };

    let totalSum = 0;
    for (let k = 1; k * k <= n; k++) {
        if (n % k === 0) {
            if (check(k)) totalSum += k;
            const otherK = n / k;
            if (otherK !== k && check(otherK)) totalSum += otherK;
        }
    }

    return totalSum;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function sortableIntegers($nums) {
        $n = count($nums);
        $target = $nums;
        sort($target);

        $hashes1 = [];
        $hashes2 = [];
        $h_seed1 = 123456789;
        $h_seed2 = 987654321;
        for ($i = 0; $i <= 100000; $i++) {
            $h_seed1 = ($h_seed1 * 1103515245 + 12345) % 1000000007;
            $h_seed2 = ($h_seed2 * 1103515245 + 12345) % 1000000009;
            $hashes1[$i] = $h_seed1;
            $hashes2[$i] = $h_seed2;
        }

        $prefixHash1 = array_fill(0, $n + 1, 0);
        $prefixHash2 = array_fill(0, $n + 1, 0);
        $targetPrefix1 = array_fill(0, $n + 1, 0);
        $targetPrefix2 = array_fill(0, $n + 1, 0);

        for ($i = 0; $i < $n; $i++) {
            $prefixHash1[$i + 1] = ($prefixHash1[$i] + $hashes1[$nums[$i]]) % 1000000007;
            $prefixHash2[$i + 1] = ($prefixHash2[$i] + $hashes2[$nums[$i]]) % 1000000009;
            $targetPrefix1[$i + 1] = ($targetPrefix1[$i] + $hashes1[$target[$i]]) % 1000000007;
            $targetPrefix2[$i + 1] = ($targetPrefix2[$i] + $hashes2[$target[$i]]) % 1000000009;
        }

        $prefixDrops = array_fill(0, $n, 0);
        for ($i = 0; $i < $n - 1; $i++) {
            $prefixDrops[$i] = ($nums[$i] > $nums[$i + 1]) ? 1 : 0;
            if ($i > 0) $prefixDrops[$i] += $prefixDrops[$i - 1];
        }

        $totalSum = 0;
        $divs = [];
        for ($i = 1; $i * $i <= $n; $i++) {
            if ($n % $i == 0) {
                $divs[] = $i;
                if ($i * $i != $n) $divs[] = $n / $i;
            }
        }

        foreach ($divs as $k) {
            $mCount = $n / $k;
            $ok = true;
            for ($m = 0; $m < $mCount; $m++) {
                $start = $m * $k;
                $end = ($m + 1) * $k - 1;

                $sum1 = ($prefixHash1[$end + 1] - $prefixHash1[$start] + 1000000007) % 1000000007;
                $tSum1 = ($targetPrefix1[$end + 1] - $targetPrefix1[$start] + 1000000007) % 1000000007;
                if ($sum1 !== $tSum1) { $ok = false; break; }

                $sum2 = ($prefixHash2[$end + 1] - $prefixHash2[$start] + 1000000009) % 1000000009;
                $tSum2 = ($targetPrefix2[$end + 1] - $targetPrefix2[$start] + 1000000009) % 1000000009;
                if ($sum2 !== $tSum2) { $ok = false; break; }

                if ($k > 1) {
                    $numDrops = $prefixDrops[$end - 1];
                    if ($start > 0) $numDrops -= $prefixDrops[$start - 1];
                    if ($numDrops > 1) { $ok = false; break; }
                    if ($numDrops == 1 && $nums[$end] > $nums[$start]) { $ok = false; break; }
                }
            }
            if ($ok) $totalSum += $k;
        }

        return $totalSum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func sortableIntegers(_ nums: [Int]) -> Int {
        let n = nums.count
        let target = nums.sorted()
        var hashes = [UInt64](repeating: 0, count: 100001)
        var hSeed: UInt64 = 123456789
        for i in 0...100000 {
            hSeed = hSeed.multipliedReportingOverflow(by: 6364136223846793005).partialValue &+ 1442695040888963407
            hashes[i] = hSeed
        }

        var prefixHashNums = [UInt64](repeating: 0, count: n + 1)
        var prefixHashTarget = [UInt64](repeating: 0, count: n + 1)
        for i in 0..<n {
            prefixHashNums[i + 1] = prefixHashNums[i] &+ hashes[nums[i]]
            prefixHashTarget[i + 1] = prefixHashTarget[i] &+ hashes[target[i]]
        }

        var prefixDrops = [Int](repeating: 0, count: n)
        if n > 1 {
            for i in 0..<n-1 {
                prefixDrops[i] = (nums[i] > nums[i + 1] ? 1 : 0)
                if i > 0 { prefixDrops[i] += prefixDrops[i - 1] }
            }
        }

        func check(_ k: Int) -> Bool {
            let mCount = n / k
            for m in 0..<mCount {
                let start = m * k
                let end = (m + 1) * k - 1
                let hNums = prefixHashNums[end + 1] &- prefixHashNums[start]
                let hTarget = prefixHashTarget[end + 1] &- prefixHashTarget[start]
                if hNums != hTarget { return false }
                if k > 1 {
                    var numDrops = prefixDrops[end - 1]
                    if start > 0 { numDrops -= prefixDrops[start - 1] }
                    if numDrops > 1 { return false }
                    if numDrops == 1 && nums[end] > nums[start] { return false }
                }
            }
            return true
        }

        var totalSum = 0
        for k in 1...Int(Double(n).squareRoot()) {
            if n % k == 0 {
                if check(k) { totalSum += k }
                let otherK = n / k
                if otherK != k && check(otherK) { totalSum += otherK }
            }
        }

        return totalSum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import kotlin.random.Random

class Solution {
    fun sortableIntegers(nums: IntArray): Int {
        val n = nums.size
        val target = nums.copyOf().apply { sort() }
        val random = java.util.Random(42)
        val hashes = LongArray(100001) { random.nextLong() }

        val prefixHashNums = LongArray(n + 1)
        val prefixHashTarget = LongArray(n + 1)
        for (i in 0 until n) {
            prefixHashNums[i + 1] = prefixHashNums[i] + hashes[nums[i]]
            prefixHashTarget[i + 1] = prefixHashTarget[i] + hashes[target[i]]
        }

        val prefixDrops = IntArray(n)
        for (i in 0 until n - 1) {
            prefixDrops[i] = if (nums[i] > nums[i + 1]) 1 else 0
            if (i > 0) prefixDrops[i] += prefixDrops[i - 1]
        }

        fun check(k: Int): Boolean {
            val mCount = n / k
            for (m in 0 until mCount) {
                val start = m * k
                val end = (m + 1) * k - 1
                val hNums = prefixHashNums[end + 1] - prefixHashNums[start]
                val hTarget = prefixHashTarget[end + 1] - prefixHashTarget[start]
                if (hNums != hTarget) return false
                if (k > 1) {
                    var numDrops = prefixDrops[end - 1]
                    if (start > 0) numDrops -= prefixDrops[start - 1]
                    if (numDrops > 1) return false
                    if (numDrops == 1 && nums[end] > nums[start]) return false
                }
            }
            return true
        }

        var totalSum = 0
        var k = 1
        while (k * k <= n) {
            if (n % k == 0) {
                if (check(k)) totalSum += k
                val otherK = n / k
                if (otherK != k && check(otherK)) totalSum += otherK
            }
            k++
        }

        return totalSum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int sortableIntegers(List<int> nums) {
    int n = nums.length;
    List<int> divisors = [];
    for (int i = 1; i * i <= n; i++) {
      if (n % i == 0) {
        divisors.add(i);
        if (i * i != n) {
          divisors.add(n ~/ i);
        }
      }
    }

    int sum = 0;
    for (int k in divisors) {
      if (check(k, nums, n)) {
        sum += k;
      }
    }
    return sum;
  }

  bool check(int k, List<int> nums, int n) {
    int prevMax = -1;
    for (int i = 0; i < n; i += k) {
      int bMin = nums[i];
      int bMax = nums[i];
      int drops = 0;
      for (int j = i; j < i + k; j++) {
        int val = nums[j];
        if (val < bMin) bMin = val;
        if (val > bMax) bMax = val;
        if (j < i + k - 1 && nums[j] > nums[j + 1]) {
          drops++;
        }
      }
      if (drops > 1) return false;
      if (drops == 1 && nums[i + k - 1] > nums[i]) return false;
      if (prevMax != -1 && prevMax > bMin) return false;
      prevMax = bMax;
    }
    return true;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func sortableIntegers(nums []int) int {
	n := len(nums)
	divisors := []int{}
	for i := 1; i*i <= n; i++ {
		if n%i == 0 {
			divisors = append(divisors, i)
			if i*i != n {
				divisors = append(divisors, n/i)
			}
		}
	}

	sum := 0
	for _, k := range divisors {
		if check(k, nums, n) {
			sum += k
		}
	}
	return sum
}

func check(k int, nums []int, n int) bool {
	prevMax := -1
	for i := 0; i < n; i += k {
		bMin := nums[i]
		bMax := nums[i]
		drops := 0
		for j := i; j < i+k; j++ {
			val := nums[j]
			if val < bMin {
				bMin = val
			}
			if val > bMax {
				bMax = val
			}
			if j < i+k-1 && nums[j] > nums[j+1] {
				drops++
			}
		}
		if drops > 1 {
			return false
		}
		if drops == 1 && nums[i+k-1] > nums[i] {
			return false
		}
		if prevMax != -1 && prevMax > bMin {
			return false
		}
		prevMax = bMax
	}
	return true
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def sortable_integers(nums)
  n = nums.length
  divisors = []
  i = 1
  while i * i <= n
    if n % i == 0
      divisors << i
      divisors << n / i if i * i != n
    end
    i += 1
  end

  sum = 0
  divisors.each do |k|
    sum += k if check_sortable(k, nums, n)
  end
  sum
end

def check_sortable(k, nums, n)
  prev_max = -1
  i = 0
  while i < n
    b_min = nums[i]
    b_max = nums[i]
    drops = 0
    j = i
    while j < i + k
      val = nums[j]
      b_min = val if val < b_min
      b_max = val if val > b_max
      if j < i + k - 1 && nums[j] > nums[j + 1]
        drops += 1
      end
      j += 1
    end
    return false if drops > 1
    return false if drops == 1 && nums[i + k - 1] > nums[i]
    return false if prev_max != -1 && prev_max > b_min
    prev_max = b_max
    i += k
  end
  true
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def sortableIntegers(nums: Array[Int]): Int = {
    val n = nums.length
    val divisors = scala.collection.mutable.ArrayBuffer[Int]()
    var i = 1
    while (i * i <= n) {
      if (n % i == 0) {
        divisors += i
        if (i * i != n) {
          divisors += n / i
        }
      }
      i += 1
    }

    var sum = 0
    for (k <- divisors) {
      if (check(k, nums, n)) {
        sum += k
      }
    }
    sum
  }

  private def check(k: Int, nums: Array[Int], n: Int): Boolean = {
    var prevMax = -1
    var i = 0
    while (i < n) {
      var bMin = nums(i)
      var bMax = nums(i)
      var drops = 0
      var j = i
      while (j < i + k) {
        val v = nums(j)
        if (v < bMin) bMin = v
        if (v > bMax) bMax = v
        if (j < i + k - 1 && nums(j) > nums(j + 1)) {
          drops += 1
        }
        j += 1
      }
      if (drops > 1) return false
      if (drops == 1 && nums(i + k - 1) > nums(i)) return false
      if (prevMax != -1 && prevMax > bMin) return false
      prevMax = bMax
      i += k
    }
    true
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn sortable_integers(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 0 { return 0; }
        let mut s = nums.clone();
        s.sort_unstable();

        let mut val_hashes = vec![0u64; 100001];
        let mut h: u64 = 123456789;
        for i in 0..100001 {
            h = h.wrapping_mul(6364136223846793005).wrapping_add(1);
            val_hashes[i] = h;
        }

        let mut prefix_h_nums = vec![0u64; n + 1];
        let mut prefix_h_s = vec![0u64; n + 1];
        for i in 0..n {
            prefix_h_nums[i + 1] = prefix_h_nums[i].wrapping_add(val_hashes[nums[i] as usize]);
            prefix_h_s[i + 1] = prefix_h_s[i].wrapping_add(val_hashes[s[i] as usize]);
        }

        let mut prefix_desc = vec![0; n];
        for i in 0..n - 1 {
            let d = if nums[i] > nums[i + 1] { 1 } else { 0 };
            prefix_desc[i + 1] = prefix_desc[i] + d;
        }

        let mut total_sum = 0;
        for k in 1..=n {
            if n % k == 0 {
                let mut possible = true;
                for i in (0..n).step_by(k) {
                    if prefix_h_nums[i + k] - prefix_h_nums[i] != prefix_h_s[i + k] - prefix_h_s[i] {
                        possible = false;
                        break;
                    }
                    let num_descents = prefix_desc[i + k - 1] - prefix_desc[i];
                    if num_descents > 1 {
                        possible = false;
                        break;
                    }
                    if num_descents == 1 && nums[i + k - 1] > nums[i] {
                        possible = false;
                        break;
                    }
                }
                if possible {
                    total_sum += k;
                }
            }
        }
        total_sum as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (sortable-integers nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([n (length nums)]
         [nums-vec (list->vector nums)]
         [s-vec (list->vector (sort nums <))]
         [val-hashes (let ([v (make-vector 100001)])
                       (let loop ([i 0] [h 123456789])
                         (if (< i 100001)
                             (let ([next-h (modulo (+ (* h 6364136223846793005) 1) (expt 2 64))])
                               (vector-set! v i next-h)
                               (loop (+ i 1) next-h))
                             v)))]
         [prefix-h-nums (let ([v (make-vector (+ n 1) 0)])
                          (for ([i (in-range n)])
                            (vector-set! v (+ i 1) (+ (vector-ref v i) (vector-ref val-hashes (vector-ref nums-vec i)))))
                          v)]
         [prefix-h-s (let ([v (make-vector (+ n 1) 0)])
                       (for ([i (in-range n)])
                         (vector-set! v (+ i 1) (+ (vector-ref v i) (vector-ref val-hashes (vector-ref s-vec i)))))
                       v)]
         [prefix-desc (let ([v (make-vector n 0)])
                        (for ([i (in-range (- n 1))])
                          (let ([d (if (> (vector-ref nums-vec i) (vector-ref nums-vec (+ i 1))) 1 0)])
                            (vector-set! v (+ i 1) (+ (vector-ref v i) d))))
                        v)])
    (for/fold ([total-sum 0])
              ([k (in-range 1 (+ n 1))]
               #:when (zero? (remainder n k)))
      (let ([possible (for/and ([i (in-range 0 n k)])
                        (and (= (- (vector-ref prefix-h-nums (+ i k)) (vector-ref prefix-h-nums i))
                                (- (vector-ref prefix-h-s (+ i k)) (vector-ref prefix-h-s i)))
                             (let ([num-descents (- (vector-ref prefix-desc (+ i k -1)) (vector-ref prefix-desc i))])
                               (or (zero? num-descents)
                                   (and (= num-descents 1)
                                        (<= (vector-ref nums-vec (+ i k -1)) (vector-ref nums-vec i)))))))])
        (if possible (+ total-sum k) total-sum)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec sortable_integers(Nums :: [integer()]) -> integer().
sortable_integers(Nums) ->
  N = length(Nums),
  NumsVec = list_to_tuple(Nums),
  SortedNums = lists:sort(Nums),
  SortedVec = list_to_tuple(SortedNums),

  GenerateHashes = fun F(0, _H, Acc) -> Acc;
                       F(I, H, Acc) ->
                         NextH = (H * 6364136223846793005 + 1) band 18446744073709551615,
                         F(I - 1, NextH, [NextH | Acc])
                   end,
  ValHashes = list_to_tuple(GenerateHashes(100001, 123456789, [])),

  PrefixHNums = list_to_tuple(lists:reverse(lists:foldl(fun(X, [H|T]) -> [H + element(X + 1, ValHashes) | [H|T]] end, [0], Nums))),
  PrefixHS = list_to_tuple(lists:reverse(lists:foldl(fun(X, [H|T]) -> [H + element(X + 1, ValHashes) | [H|T]] end, [0], SortedNums))),

  Descents = [if element(I, NumsVec) > element(I + 1, NumsVec) -> 1; true -> 0 end || I <- lists:seq(1, N - 1)],
  PrefixDesc = list_to_tuple(lists:reverse(lists:foldl(fun(X, [H|T]) -> [H + X | [H|T]] end, [0], Descents))),

  Divisors = [K || K <- lists:seq(1, N), N rem K =:= 0],

  CheckBlock = fun(I, K) ->
                 MultisetMatch = (element(I + K + 1, PrefixHNums) - element(I + 1, PrefixHNums)) =:= (element(I + K + 1, PrefixHS) - element(I + 1, PrefixHS)),
                 NumDesc = if K > 1 -> element(I + K, PrefixDesc) - element(I + 1, PrefixDesc); true -> 0 end,
                 CyclicallySorted = (NumDesc =:= 0) or ((NumDesc =:= 1) and (element(I + K, NumsVec) =< element(I + 1, NumsVec))),
                 MultisetMatch and CyclicallySorted
               end,

  CheckK = fun(K) ->
             lists:all(fun(I) -> CheckBlock(I, K) end, lists:seq(0, N - K, K))
           end,

  lists:foldl(fun(K, Sum) -> if CheckK(K) -> Sum + K; true -> Sum end end, 0, Divisors).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec sortable_integers(nums :: [integer]) :: integer
  def sortable_integers(nums) do
    n = length(nums)
    nums_tuple = List.to_tuple(nums)
    sorted_nums = Enum.sort(nums)
    sorted_tuple = List.to_tuple(sorted_nums)

    generate_hashes = fn count, seed ->
      Enum.reduce(0..count, {[], seed}, fn _, {acc, h} ->
        next_h = rem(h * 6364136223846793005 + 1, 18446744073709551616)
        {[next_h | acc], next_h}
      end) |> elem(0) |> Enum.reverse() |> List.to_tuple()
    end
    val_hashes = generate_hashes.(100000, 123456789)

    prefix_h_nums = Enum.reduce(nums, [0], fn x, [h | t] -> [h + elem(val_hashes, x) | [h | t]] end) |> Enum.reverse() |> List.to_tuple()
    prefix_h_s = Enum.reduce(sorted_nums, [0], fn x, [h | t] -> [h + elem(val_hashes, x) | [h | t]] end) |> Enum.reverse() |> List.to_tuple()

    descents = for i <- 0..(n - 2), n > 1, do: (if elem(nums_tuple, i) > elem(nums_tuple, i + 1), do: 1, else: 0)
    prefix_desc = Enum.reduce(descents, [0], fn x, [h | t] -> [h + x | [h | t]] end) |> Enum.reverse() |> List.to_tuple()

    divisors = for k <- 1..n, rem(n, k) == 0, do: k

    Enum.reduce(divisors, 0, fn k, sum ->
      possible = Enum.all?(0..max(0, n - k) |> Stream.take_every(k), fn i ->
        multiset_match = (elem(prefix_h_nums, i + k) - elem(prefix_h_nums, i)) == (elem(prefix_h_s, i + k) - elem(prefix_h_s, i))
        num_desc = if k > 1, do: elem(prefix_desc, i + k - 1) - elem(prefix_desc, i), else: 0
        cyclically_sorted = (num_desc == 0) or (num_desc == 1 and elem(nums_tuple, i + k - 1) <= elem(nums_tuple, i))
        multiset_match and cyclically_sorted
      end)
      if possible, do: sum + k, else: sum
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n \log n + \sigma(n)), where n is the length of the array and \sigma(n)$ is the sum of divisors of $n$. Sorting takes $O(n \log n)$, while precalculating prefix hashes and descents takes $O(n)$. The final check for all divisors $k$ iterates through blocks, resulting in a total of $\sum_{k|n} n/k = \sigma(n)$ operations. For $n=10^5$, $\sigma(n)$ is at most 248,760, making the algorithm extremely efficient.
- **Space Complexity:** O(n), as we store the sorted array, prefix sums of multiset hashes, and prefix counts of descents, each requiring $O(n)$ space.
