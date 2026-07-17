---
layout: post
title: "Sorted GCD Pair Queries"
date: 2026-07-17 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Hash Table", "Math", "Binary Search", "Combinatorics", "Counting", "Number Theory", "Prefix Sum"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/sorted-gcd-pair-queries/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> gcdValues(vector<int>& nums,\
        \ vector<long long>& queries) {\n        int max_val = 0;\n        for (int\
        \ x : nums) if (x > max_val) max_val = x;\n\n        vector<int> cnt(max_val\
        \ + 1, 0);\n        for (int x : nums) cnt[x]++;\n\n        vector<long long>\
        \ f(max_val + 1, 0);\n        for (int g = max_val; g >= 1; --g) {\n       \
        \     long long multiples = 0;\n            for (int m = g; m <= max_val; m\
        \ += g) {\n                multiples += cnt[m];\n            }\n           \
        \ long long pairs = multiples * (multiples - 1) / 2;\n            for (int m\
        \ = 2 * g; m <= max_val; m += g) {\n                pairs -= f[m];\n       \
        \     }\n            f[g] = pairs;\n        }\n\n        vector<long long> prefix_f(max_val\
        \ + 1, 0);\n        for (int i = 1; i <= max_val; ++i) {\n            prefix_f[i]\
        \ = prefix_f[i - 1] + f[i];\n        }\n\n        vector<int> result;\n    \
        \    result.reserve(queries.size());\n        for (long long q : queries) {\n\
        \            auto it = upper_bound(prefix_f.begin(), prefix_f.end(), q);\n \
        \           result.push_back((int)(distance(prefix_f.begin(), it)));\n     \
        \   }\n\n        return result;\n    }\n};"
      java: "class Solution {\n    public int[] gcdValues(int[] nums, long[] queries)\
        \ {\n        int maxVal = 0;\n        for (int x : nums) {\n            if (x\
        \ > maxVal) maxVal = x;\n        }\n\n        int[] cnt = new int[maxVal + 1];\n\
        \        for (int x : nums) {\n            cnt[x]++;\n        }\n\n        long[]\
        \ f = new long[maxVal + 1];\n        for (int g = maxVal; g >= 1; g--) {\n \
        \           long multiples = 0;\n            for (int m = g; m <= maxVal; m\
        \ += g) {\n                multiples += cnt[m];\n            }\n           \
        \ long pairs = multiples * (multiples - 1) / 2;\n            for (int m = 2\
        \ * g; m <= maxVal; m += g) {\n                pairs -= f[m];\n            }\n\
        \            f[g] = pairs;\n        }\n\n        long[] prefixF = new long[maxVal\
        \ + 1];\n        for (int i = 1; i <= maxVal; i++) {\n            prefixF[i]\
        \ = prefixF[i - 1] + f[i];\n        }\n\n        int[] result = new int[queries.length];\n\
        \        for (int i = 0; i < queries.length; i++) {\n            long q = queries[i];\n\
        \            int low = 1, high = maxVal;\n            int ans = maxVal;\n  \
        \          while (low <= high) {\n                int mid = low + (high - low)\
        \ / 2;\n                if (prefixF[mid] > q) {\n                    ans = mid;\n\
        \                    high = mid - 1;\n                } else {\n           \
        \         low = mid + 1;\n                }\n            }\n            result[i]\
        \ = ans;\n        }\n\n        return result;\n    }\n}"
      python: "import bisect\n\nclass Solution(object):\n    def gcdValues(self, nums,\
        \ queries):\n        \"\"\"\n        :type nums: List[int]\n        :type queries:\
        \ List[int]\n        :rtype: List[int]\n        \"\"\"\n        max_val = max(nums)\n\
        \        cnt = [0] * (max_val + 1)\n        for x in nums:\n            cnt[x]\
        \ += 1\n\n        f = [0] * (max_val + 1)\n        for g in range(max_val, 0,\
        \ -1):\n            multiples = 0\n            for m in range(g, max_val + 1,\
        \ g):\n                multiples += cnt[m]\n\n            pairs = multiples\
        \ * (multiples - 1) // 2\n            for m in range(2 * g, max_val + 1, g):\n\
        \                pairs -= f[m]\n            f[g] = pairs\n\n        prefix_f\
        \ = [0] * (max_val + 1)\n        for i in range(1, max_val + 1):\n         \
        \   prefix_f[i] = prefix_f[i-1] + f[i]\n\n        ans = []\n        for q in\
        \ queries:\n            # Find the smallest index i such that prefix_f[i] >\
        \ q\n            idx = bisect.bisect_right(prefix_f, q)\n            ans.append(idx)\n\
        \n        return ans"
      python3: "from typing import List\nimport bisect\n\nclass Solution:\n    def gcdValues(self,\
        \ nums: List[int], queries: List[int]) -> List[int]:\n        max_val = max(nums)\n\
        \        freq = [0] * (max_val + 1)\n        for x in nums:\n            freq[x]\
        \ += 1\n\n        count = [0] * (max_val + 1)\n        for g in range(1, max_val\
        \ + 1):\n            for m in range(g, max_val + 1, g):\n                count[g]\
        \ += freq[m]\n\n        f = [0] * (max_val + 1)\n        for g in range(max_val,\
        \ 0, -1):\n            total_pairs = (count[g] * (count[g] - 1)) // 2\n    \
        \        f[g] = total_pairs\n            for m in range(2 * g, max_val + 1,\
        \ g):\n                f[g] -= f[m]\n\n        prefix_sum = [0] * (max_val +\
        \ 1)\n        for g in range(1, max_val + 1):\n            prefix_sum[g] = prefix_sum[g\
        \ - 1] + f[g]\n\n        return [bisect.bisect_right(prefix_sum, q) for q in\
        \ queries]"
      c: "#include <stdlib.h>\n\n/**\n * Note: The returned array must be malloced,\
        \ assume caller calls free().\n */\nint* gcdValues(int* nums, int numsSize,\
        \ long long* queries, int queriesSize, int* returnSize) {\n    int maxVal =\
        \ 0;\n    for (int i = 0; i < numsSize; i++) {\n        if (nums[i] > maxVal)\
        \ maxVal = nums[i];\n    }\n\n    int* freq = (int*)calloc(maxVal + 1, sizeof(int));\n\
        \    for (int i = 0; i < numsSize; i++) {\n        freq[nums[i]]++;\n    }\n\
        \n    long long* count = (long long*)calloc(maxVal + 1, sizeof(long long));\n\
        \    for (int g = 1; g <= maxVal; g++) {\n        for (int m = g; m <= maxVal;\
        \ m += g) {\n            count[g] += freq[m];\n        }\n    }\n\n    long\
        \ long* f = (long long*)calloc(maxVal + 1, sizeof(long long));\n    for (int\
        \ g = maxVal; g >= 1; g--) {\n        f[g] = (count[g] * (count[g] - 1)) / 2;\n\
        \        for (int m = 2 * g; m <= maxVal; m += g) {\n            f[g] -= f[m];\n\
        \        }\n    }\n\n    long long* prefixSum = (long long*)calloc(maxVal +\
        \ 1, sizeof(long long));\n    for (int g = 1; g <= maxVal; g++) {\n        prefixSum[g]\
        \ = prefixSum[g - 1] + f[g];\n    }\n\n    int* result = (int*)malloc(queriesSize\
        \ * sizeof(int));\n    *returnSize = queriesSize;\n\n    for (int i = 0; i <\
        \ queriesSize; i++) {\n        long long q = queries[i];\n        int low =\
        \ 1, high = maxVal, res = maxVal;\n        while (low <= high) {\n         \
        \   int mid = low + (high - low) / 2;\n            if (prefixSum[mid] > q) {\n\
        \                res = mid;\n                high = mid - 1;\n            }\
        \ else {\n                low = mid + 1;\n            }\n        }\n       \
        \ result[i] = res;\n    }\n\n    free(freq);\n    free(count);\n    free(f);\n\
        \    free(prefixSum);\n\n    return result;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int[] GcdValues(int[] nums, long[] queries) {\n        int maxVal\
        \ = 0;\n        foreach (int x in nums) {\n            if (x > maxVal) maxVal\
        \ = x;\n        }\n\n        int[] freq = new int[maxVal + 1];\n        foreach\
        \ (int x in nums) {\n            freq[x]++;\n        }\n\n        long[] count\
        \ = new long[maxVal + 1];\n        for (int g = 1; g <= maxVal; g++) {\n   \
        \         for (int m = g; m <= maxVal; m += g) {\n                count[g] +=\
        \ freq[m];\n            }\n        }\n\n        long[] f = new long[maxVal +\
        \ 1];\n        for (int g = maxVal; g >= 1; g--) {\n            f[g] = (count[g]\
        \ * (count[g] - 1)) / 2;\n            for (int m = 2 * g; m <= maxVal; m +=\
        \ g) {\n                f[g] -= f[m];\n            }\n        }\n\n        long[]\
        \ prefixSum = new long[maxVal + 1];\n        for (int g = 1; g <= maxVal; g++)\
        \ {\n            prefixSum[g] = prefixSum[g - 1] + f[g];\n        }\n\n    \
        \    int[] result = new int[queries.Length];\n        for (int i = 0; i < queries.Length;\
        \ i++) {\n            long q = queries[i];\n            int low = 1, high =\
        \ maxVal, res = maxVal;\n            while (low <= high) {\n               \
        \ int mid = low + (high - low) / 2;\n                if (prefixSum[mid] > q)\
        \ {\n                    res = mid;\n                    high = mid - 1;\n \
        \               } else {\n                    low = mid + 1;\n             \
        \   }\n            }\n            result[i] = res;\n        }\n\n        return\
        \ result;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number[]} queries\n *\
        \ @return {number[]}\n */\nvar gcdValues = function(nums, queries) {\n    let\
        \ maxVal = 0;\n    for (let i = 0; i < nums.length; i++) {\n        if (nums[i]\
        \ > maxVal) maxVal = nums[i];\n    }\n\n    let freq = new Int32Array(maxVal\
        \ + 1);\n    for (let i = 0; i < nums.length; i++) {\n        freq[nums[i]]++;\n\
        \    }\n\n    let count = new Float64Array(maxVal + 1);\n    for (let g = 1;\
        \ g <= maxVal; g++) {\n        for (let m = g; m <= maxVal; m += g) {\n    \
        \        count[g] += freq[m];\n        }\n    }\n\n    let f = new Float64Array(maxVal\
        \ + 1);\n    for (let g = maxVal; g >= 1; g--) {\n        f[g] = (count[g] *\
        \ (count[g] - 1)) / 2;\n        for (let m = 2 * g; m <= maxVal; m += g) {\n\
        \            f[g] -= f[m];\n        }\n    }\n\n    let prefixSum = new Float64Array(maxVal\
        \ + 1);\n    for (let g = 1; g <= maxVal; g++) {\n        prefixSum[g] = prefixSum[g\
        \ - 1] + f[g];\n    }\n\n    let results = [];\n    for (let i = 0; i < queries.length;\
        \ i++) {\n        let q = queries[i];\n        let low = 1, high = maxVal, res\
        \ = maxVal;\n        while (low <= high) {\n            let mid = Math.floor((low\
        \ + high) / 2);\n            if (prefixSum[mid] > q) {\n                res\
        \ = mid;\n                high = mid - 1;\n            } else {\n          \
        \      low = mid + 1;\n            }\n        }\n        results.push(res);\n\
        \    }\n    return results;\n};"
      typescript: "function gcdValues(nums: number[], queries: number[]): number[] {\n\
        \    let maxVal = 0;\n    for (let i = 0; i < nums.length; i++) {\n        if\
        \ (nums[i] > maxVal) maxVal = nums[i];\n    }\n\n    const freqMap = new Int32Array(maxVal\
        \ + 1);\n    for (const x of nums) {\n        freqMap[x]++;\n    }\n\n    const\
        \ countGCD = new Float64Array(maxVal + 1);\n    for (let i = maxVal; i >= 1;\
        \ i--) {\n        let c = 0;\n        for (let j = i; j <= maxVal; j += i) {\n\
        \            c += freqMap[j];\n        }\n        let pairs = (c * (c - 1))\
        \ / 2;\n        for (let j = 2 * i; j <= maxVal; j += i) {\n            pairs\
        \ -= countGCD[j];\n        }\n        countGCD[i] = pairs;\n    }\n\n    const\
        \ pref = new Float64Array(maxVal + 1);\n    for (let i = 1; i <= maxVal; i++)\
        \ {\n        pref[i] = pref[i - 1] + countGCD[i];\n    }\n\n    const results\
        \ = new Int32Array(queries.length);\n    for (let k = 0; k < queries.length;\
        \ k++) {\n        const q = queries[k];\n        let low = 1, high = maxVal,\
        \ ans = maxVal;\n        while (low <= high) {\n            let mid = Math.floor((low\
        \ + high) / 2);\n            if (pref[mid] > q) {\n                ans = mid;\n\
        \                high = mid - 1;\n            } else {\n                low\
        \ = mid + 1;\n            }\n        }\n        results[k] = ans;\n    }\n\n\
        \    return Array.from(results);\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer[] $queries\n     * @return Integer[]\n     */\n    function gcdValues($nums,\
        \ $queries) {\n        $maxVal = 0;\n        foreach ($nums as $num) {\n   \
        \         if ($num > $maxVal) $maxVal = $num;\n        }\n\n        $freqMap\
        \ = array_fill(0, $maxVal + 1, 0);\n        foreach ($nums as $num) {\n    \
        \        $freqMap[$num]++;\n        }\n\n        $countGCD = array_fill(0, $maxVal\
        \ + 1, 0);\n        for ($i = $maxVal; $i >= 1; $i--) {\n            $c = 0;\n\
        \            for ($j = $i; $j <= $maxVal; $j += $i) {\n                $c +=\
        \ $freqMap[$j];\n            }\n            $pairs = ($c * ($c - 1)) / 2;\n\
        \            for ($j = 2 * $i; $j <= $maxVal; $j += $i) {\n                $pairs\
        \ -= $countGCD[$j];\n            }\n            $countGCD[$i] = $pairs;\n  \
        \      }\n\n        $pref = array_fill(0, $maxVal + 1, 0);\n        for ($i\
        \ = 1; $i <= $maxVal; $i++) {\n            $pref[$i] = $pref[$i - 1] + $countGCD[$i];\n\
        \        }\n\n        $ans = [];\n        foreach ($queries as $q) {\n     \
        \       $low = 1;\n            $high = $maxVal;\n            $res = $maxVal;\n\
        \            while ($low <= high) {\n                $mid = ($low + $high) >>\
        \ 1;\n                if ($pref[$mid] > $q) {\n                    $res = $mid;\n\
        \                    $high = $mid - 1;\n                } else {\n         \
        \           $low = $mid + 1;\n                }\n            }\n           \
        \ $ans[] = $res;\n        }\n        return $ans;\n    }\n}"
      swift: "class Solution {\n    func gcdValues(_ nums: [Int], _ queries: [Int])\
        \ -> [Int] {\n        let maxVal = nums.max() ?? 0\n        var freqMap = [Int](repeating:\
        \ 0, count: maxVal + 1)\n        for x in nums {\n            freqMap[x] +=\
        \ 1\n        }\n\n        var countGCD = [Int](repeating: 0, count: maxVal +\
        \ 1)\n        for i in stride(from: maxVal, through: 1, by: -1) {\n        \
        \    var c = 0\n            for j in stride(from: i, through: maxVal, by: i)\
        \ {\n                c += freqMap[j]\n            }\n            var pairs =\
        \ c * (c - 1) / 2\n            for j in stride(from: 2 * i, through: maxVal,\
        \ by: i) {\n                pairs -= countGCD[j]\n            }\n          \
        \  countGCD[i] = pairs\n        }\n\n        var pref = [Int](repeating: 0,\
        \ count: maxVal + 1)\n        for i in 1...maxVal {\n            pref[i] = pref[i\
        \ - 1] + countGCD[i]\n        }\n\n        var result = [Int]()\n        result.reserveCapacity(queries.count)\n\
        \        for q in queries {\n            var low = 1\n            var high =\
        \ maxVal\n            var ans = maxVal\n            while low <= high {\n  \
        \              let mid = (low + high) / 2\n                if pref[mid] > q\
        \ {\n                    ans = mid\n                    high = mid - 1\n   \
        \             } else {\n                    low = mid + 1\n                }\n\
        \            }\n            result.append(ans)\n        }\n\n        return\
        \ result\n    }\n}"
      kotlin: "class Solution {\n    fun gcdValues(nums: IntArray, queries: LongArray):\
        \ IntArray {\n        val maxVal = nums.maxOrNull() ?: 0\n        val freqMap\
        \ = IntArray(maxVal + 1)\n        for (x in nums) {\n            freqMap[x]++\n\
        \        }\n\n        val countGCD = LongArray(maxVal + 1)\n        for (i in\
        \ maxVal downTo 1) {\n            var c: Long = 0\n            for (j in i..maxVal\
        \ step i) {\n                c += freqMap[j]\n            }\n            var\
        \ pairs: Long = c * (c - 1) / 2\n            for (j in 2 * i..maxVal step i)\
        \ {\n                pairs -= countGCD[j]\n            }\n            countGCD[i]\
        \ = pairs\n        }\n\n        val pref = LongArray(maxVal + 1)\n        for\
        \ (i in 1..maxVal) {\n            pref[i] = pref[i - 1] + countGCD[i]\n    \
        \    }\n\n        val result = IntArray(queries.size)\n        for (i in queries.indices)\
        \ {\n            val q = queries[i]\n            var low = 1\n            var\
        \ high = maxVal\n            var ans = maxVal\n            while (low <= high)\
        \ {\n                val mid = (low + high) / 2\n                if (pref[mid]\
        \ > q) {\n                    ans = mid\n                    high = mid - 1\n\
        \                } else {\n                    low = mid + 1\n             \
        \   }\n            }\n            result[i] = ans\n        }\n        return\
        \ result\n    }\n}"
      dart: "class Solution {\n  List<int> gcdValues(List<int> nums, List<int> queries)\
        \ {\n    int m = nums[0];\n    for (int x in nums) {\n      if (x > m) m = x;\n\
        \    }\n\n    List<int> freq = List<int>.filled(m + 1, 0);\n    for (int x in\
        \ nums) {\n      freq[x]++;\n    }\n\n    List<int> f = List<int>.filled(m +\
        \ 1, 0);\n    for (int g = m; g >= 1; g--) {\n      int count = 0;\n      for\
        \ (int k = g; k <= m; k += g) {\n        count += freq[k];\n      }\n      int\
        \ totalPairsWithMultipleG = (count * (count - 1)) ~/ 2;\n      int others =\
        \ 0;\n      for (int k = 2 * g; k <= m; k += g) {\n        others += f[k];\n\
        \      }\n      f[g] = totalPairsWithMultipleG - others;\n    }\n\n    List<int>\
        \ pref = List<int>.filled(m + 1, 0);\n    for (int g = 1; g <= m; g++) {\n \
        \     pref[g] = pref[g - 1] + f[g];\n    }\n\n    List<int> ans = List<int>.filled(queries.length,\
        \ 0);\n    for (int i = 0; i < queries.length; i++) {\n      int q = queries[i];\n\
        \      int low = 1, high = m;\n      int result = m;\n      while (low <= high)\
        \ {\n        int mid = low + (high - low) ~/ 2;\n        if (pref[mid] > q)\
        \ {\n          result = mid;\n          high = mid - 1;\n        } else {\n\
        \          low = mid + 1;\n        }\n      }\n      ans[i] = result;\n    }\n\
        \    return ans;\n  }\n}"
      go: "func gcdValues(nums []int, queries []int64) []int {\n\tm := 0\n\tfor _, x\
        \ := range nums {\n\t\tif x > m {\n\t\t\tm = x\n\t\t}\n\t}\n\n\tfreq := make([]int,\
        \ m+1)\n\tfor _, x := range nums {\n\t\tfreq[x]++\n\t}\n\n\tf := make([]int64,\
        \ m+1)\n\tfor g := m; g >= 1; g-- {\n\t\tcount := int64(0)\n\t\tfor k := g;\
        \ k <= m; k += g {\n\t\t\tcount += int64(freq[k])\n\t\t}\n\t\thG := count *\
        \ (count - 1) / 2\n\t\tfor k := 2 * g; k <= m; k += g {\n\t\t\thG -= f[k]\n\t\
        \t}\n\t\tf[g] = hG\n\t}\n\n\tpref := make([]int64, m+1)\n\tfor g := 1; g <=\
        \ m; g++ {\n\t\tpref[g] = pref[g-1] + f[g]\n\t}\n\n\tans := make([]int, len(queries))\n\
        \tfor i, q := range queries {\n\t\tidx := sort.Search(len(pref), func(j int)\
        \ bool {\n\t\t\treturn pref[j] > q\n\t\t})\n\t\tans[i] = idx\n\t}\n\n\treturn\
        \ ans\n}"
      ruby: "# @param {Integer[]} nums\n# @param {Integer[]} queries\n# @return {Integer[]}\n\
        def gcd_values(nums, queries)\n  max_num = nums.max\n  freq = Array.new(max_num\
        \ + 1, 0)\n  nums.each { |x| freq[x] += 1 }\n\n  f = Array.new(max_num + 1,\
        \ 0)\n  max_num.step(1, -1) do |g|\n    count = 0\n    g.step(max_num, g) {\
        \ |k| count += freq[k] }\n\n    h_g = count * (count - 1) / 2\n\n    (2 * g).step(max_num,\
        \ g) { |k| h_g -= f[k] }\n    f[g] = h_g\n  end\n\n  pref = Array.new(max_num\
        \ + 1, 0)\n  (1..max_num).each { |g| pref[g] = pref[g-1] + f[g] }\n\n  queries.map\
        \ do |q|\n    (1..max_num).bsearch { |g| pref[g] > q }\n  end\nend"
      scala: "object Solution {\n    def gcdValues(nums: Array[Int], queries: Array[Long]):\
        \ Array[Int] = {\n        val maxNum = nums.max\n        val freq = new Array[Int](maxNum\
        \ + 1)\n        for (x <- nums) freq(x) += 1\n\n        val f = new Array[Long](maxNum\
        \ + 1)\n        for (g <- maxNum to 1 by -1) {\n            var count = 0L\n\
        \            var k = g\n            while (k <= maxNum) {\n                count\
        \ += freq(k)\n                k += g\n            }\n            var hG = count\
        \ * (count - 1) / 2\n            var k2 = 2 * g\n            while (k2 <= maxNum)\
        \ {\n                hG -= f(k2)\n                k2 += g\n            }\n \
        \           f(g) = hG\n        }\n\n        val pref = new Array[Long](maxNum\
        \ + 1)\n        for (g <- 1 to maxNum) {\n            pref(g) = pref(g - 1)\
        \ + f(g)\n        }\n\n        val ans = new Array[Int](queries.length)\n  \
        \      for (i <- queries.indices) {\n            val q = queries(i)\n      \
        \      var low = 1\n            var high = maxNum\n            var res = maxNum\n\
        \            while (low <= high) {\n                val mid = low + (high -\
        \ low) / 2\n                if (pref(mid) > q) {\n                    res =\
        \ mid\n                    high = mid - 1\n                } else {\n      \
        \              low = mid + 1\n                }\n            }\n           \
        \ ans(i) = res\n        }\n        ans\n    }\n}"
      rust: "impl Solution {\n    pub fn gcd_values(nums: Vec<i32>, queries: Vec<i64>)\
        \ -> Vec<i32> {\n        let max_val = *nums.iter().max().unwrap_or(&0) as usize;\n\
        \        let mut count = vec![0i64; max_val + 1];\n        for &x in &nums {\n\
        \            count[x as usize] += 1;\n        }\n\n        let mut h = vec![0i64;\
        \ max_val + 1];\n        for g in (1..=max_val).rev() {\n            let mut\
        \ c_g = 0i64;\n            let mut i = g;\n            while i <= max_val {\n\
        \                c_g += count[i];\n                i += g;\n            }\n\
        \            let total_pairs_multiple_g = c_g * (c_g - 1) / 2;\n           \
        \ let mut sum_h_multiples = 0i64;\n            let mut j = 2 * g;\n        \
        \    while j <= max_val {\n                sum_h_multiples += h[j];\n      \
        \          j += g;\n            }\n            h[g] = total_pairs_multiple_g\
        \ - sum_h_multiples;\n        }\n\n        let mut pref = vec![0i64; max_val\
        \ + 1];\n        for i in 1..=max_val {\n            pref[i] = pref[i - 1] +\
        \ h[i];\n        }\n\n        queries.into_iter().map(|q| {\n            let\
        \ mut low = 1;\n            let mut high = max_val;\n            let mut ans\
        \ = max_val;\n            while low <= high {\n                let mid = low\
        \ + (high - low) / 2;\n                if pref[mid] > q {\n                \
        \    ans = mid;\n                    high = mid - 1;\n                } else\
        \ {\n                    low = mid + 1;\n                }\n            }\n\
        \            ans as i32\n        }).collect()\n    }\n}"
      racket: "(define/contract (gcd-values nums queries)\n  (-> (listof exact-integer?)\
        \ (listof exact-integer?) (listof exact-integer?))\n  (let* ([max-val (for/fold\
        \ ([m 0]) ([x nums]) (max m x))]\n         [count (make-vector (+ max-val 1)\
        \ 0)])\n    (for ([x nums])\n      (vector-set! count x (+ (vector-ref count\
        \ x) 1)))\n\n    (define h (make-vector (+ max-val 1) 0))\n    (for ([g (in-range\
        \ max-val 0 -1)])\n      (let* ([c-g (for/fold ([acc 0])\n                 \
        \           ([i (in-range g (+ max-val 1) g)])\n                    (+ acc (vector-ref\
        \ count i)))]\n             [total-pairs (quotient (* c-g (- c-g 1)) 2)]\n \
        \            [sum-h (for/fold ([acc 0])\n                              ([i (in-range\
        \ (* 2 g) (+ max-val 1) g)])\n                      (+ acc (vector-ref h i)))])\n\
        \        (vector-set! h g (- total-pairs sum-h))))\n\n    (define pref (make-vector\
        \ (+ max-val 1) 0))\n    (for ([i (in-range 1 (+ max-val 1))])\n      (vector-set!\
        \ pref i (+ (vector-ref pref (- i 1)) (vector-ref h i))))\n\n    (define (binary-search\
        \ target)\n      (let loop ([low 1] [high max-val])\n        (if (> low high)\n\
        \            low\n            (let* ([mid (quotient (+ low high) 2)]\n     \
        \              [val (vector-ref pref mid)])\n              (if (> val target)\n\
        \                  (loop low (- mid 1))\n                  (loop (+ mid 1) high))))))\n\
        \n    (map binary-search queries)))"
      erlang: "-spec gcd_values(Nums :: [integer()], Queries :: [integer()]) -> [integer()].\n\
        gcd_values(Nums, Queries) ->\n  MaxVal = lists:foldl(fn(X, Acc) -> erlang:max(X,\
        \ Acc) end, 0, Nums),\n  Cnts = atomics:new(MaxVal, [{signed, true}]),\n  HAtoms\
        \ = atomics:new(MaxVal, [{signed, true}]),\n  lists:foreach(fn(X) -> atomics:add(Cnts,\
        \ X, 1) end, Nums),\n\n  LoopG = fun(G, Self) ->\n    if G > 0 ->\n      CG\
        \ = get_cg(G, MaxVal, G, 0, Cnts),\n      TotalPairs = CG * (CG - 1) div 2,\n\
        \      SumH = get_sum_h(2 * G, MaxVal, G, 0, HAtoms),\n      atomics:put(HAtoms,\
        \ G, TotalPairs - SumH),\n      Self(G - 1, Self);\n    true -> ok\n    end\n\
        \  end,\n  LoopG(MaxVal, LoopG),\n\n  {_, PrefList} = lists:foldl(fn(G, {Acc,\
        \ L}) ->\n    NewAcc = Acc + atomics:get(HAtoms, G),\n    {NewAcc, [NewAcc |\
        \ L]}\n  end, {0, [0]}, lists:seq(1, MaxVal)),\n\n  PrefTuple = list_to_tuple(lists:reverse(PrefList)),\n\
        \  [binary_search(PrefTuple, Q, 1, MaxVal) || Q <- Queries].\n\nget_cg(I, MaxVal,\
        \ Step, Acc, Cnts) ->\n  if I > MaxVal -> Acc;\n    true -> get_cg(I + Step,\
        \ MaxVal, Step, Acc + atomics:get(Cnts, I), Cnts)\n  end.\n\nget_sum_h(I, MaxVal,\
        \ Step, Acc, HAtoms) ->\n  if I > MaxVal -> Acc;\n    true -> get_sum_h(I +\
        \ Step, MaxVal, Step, Acc + atomics:get(HAtoms, I), HAtoms)\n  end.\n\nbinary_search(PrefTuple,\
        \ Target, Low, High) ->\n  if Low > High -> Low;\n    true ->\n      Mid = (Low\
        \ + High) div 2,\n      Val = element(Mid + 1, PrefTuple),\n      if Val > Target\
        \ -> binary_search(PrefTuple, Target, Low, Mid - 1);\n        true -> binary_search(PrefTuple,\
        \ Target, Mid + 1, High)\n      end\n  end."
      elixir: "defmodule Solution do\n  @spec gcd_values(nums :: [integer], queries\
        \ :: [integer]) :: [integer]\n  def gcd_values(nums, queries) do\n    max_val\
        \ = Enum.reduce(nums, 0, &max/2)\n    cnts = :atomics.new(max_val, [{:signed,\
        \ true}])\n    h_atoms = :atomics.new(max_val, [{:signed, true}])\n\n    Enum.each(nums,\
        \ fn x -> :atomics.add(cnts, x, 1) end)\n\n    for g <- max_val..1 do\n    \
        \  cg = get_cg(g, max_val, g, 0, cnts)\n      total_pairs = div(cg * (cg - 1),\
        \ 2)\n      sum_h = get_sum_h(2 * g, max_val, g, 0, h_atoms)\n      :atomics.put(h_atoms,\
        \ g, total_pairs - sum_h)\n    end\n\n    pref_list = \n      Enum.scan(1..max_val,\
        \ 0, fn g, acc -> \n        acc + :atomics.get(h_atoms, g)\n      end)\n\n \
        \   pref_tuple = List.to_tuple([0 | pref_list])\n\n    Enum.map(queries, fn\
        \ q -> \n      binary_search(pref_tuple, q, 1, max_val)\n    end)\n  end\n\n\
        \  defp get_cg(i, max_val, step, acc, cnts) when i > max_val, do: acc\n  defp\
        \ get_cg(i, max_val, step, acc, cnts) do\n    get_cg(i + step, max_val, step,\
        \ acc + :atomics.get(cnts, i), cnts)\n  end\n\n  defp get_sum_h(i, max_val,\
        \ step, acc, h_atoms) when i > max_val, do: acc\n  defp get_sum_h(i, max_val,\
        \ step, acc, h_atoms) do\n    get_sum_h(i + step, max_val, step, acc + :atomics.get(h_atoms,\
        \ i), h_atoms)\n  end\n\n  defp binary_search(pref_tuple, target, low, high)\
        \ when low > high, do: low\n  defp binary_search(pref_tuple, target, low, high)\
        \ do\n    mid = div(low + high, 2)\n    val = elem(pref_tuple, mid)\n    if\
        \ val > target do\n      binary_search(pref_tuple, target, low, mid - 1)\n \
        \   else\n      binary_search(pref_tuple, target, mid + 1, high)\n    end\n\
        \  end\nend"
    approach: 'To solve this problem efficiently, we count the occurrences of each possible
      GCD value by first determining the frequency of each number in the input array.
      We let $S(g)$ be the number of elements in ''nums'' that are multiples of $g$.
      The number of pairs $(i, j)$ such that both $nums[i]$ and $nums[j]$ are multiples
      of $g$ is given by $P(g) = \frac{S(g)(S(g)-1)}{2}$. However, $P(g)$ includes pairs
      whose GCD is any multiple of $g$ (i.e., $g, 2g, 3g, \dots$). To find the exact
      count of pairs with GCD equal to $g$, denoted as $f(g)$, we use inclusion-exclusion
      (or a backward DP): $f(g) = P(g) - \sum_{k=2}^{\lfloor M/g \rfloor} f(k \cdot
      g)$, where $M$ is the maximum value in ''nums''. By iterating $g$ from $M$ down
      to 1, we can compute all $f(g)$ values in $O(M \log M)$ time.


      Once we have the counts of pairs for each GCD value $g \in [1, M]$, we compute
      the prefix sums of these counts. Let $prefix[g]$ represent the total number of
      pairs $(i, j)$ whose GCD is less than or equal to $g$. Since the array of all
      GCD pairs is sorted in ascending order, the element at a specific index $q$ in
      the sorted ''gcdPairs'' array is the smallest $g$ such that $prefix[g] > q$. For
      each query, we perform a binary search on the prefix sum array to find this smallest
      $g$. This approach is highly efficient given the constraints $n \le 10^5$ and
      $M \le 5 \cdot 10^4$.'
    time_complexity: O(N + M \log M + Q \log M), where $N$ is the number of elements
      in 'nums', $M$ is the maximum value in 'nums' ($5 \cdot 10^4$), and $Q$ is the
      number of queries. Calculating frequencies and $S(g)$ takes $O(N + M \log M)$,
      calculating $f(g)$ takes $O(M \log M)$, and processing $Q$ queries via binary
      search takes $O(Q \log M)$.
    space_complexity: O(N + M), where $N$ is the size of the input and $M$ is the maximum
      value in 'nums'. We store the frequency array, the count of multiples, the GCD
      pair counts, and the prefix sums, all of which are proportional to $M$.
    elapsed_time: 279.66806149482727
    model: gemini-3-flash-preview
    generated_at: '2026-07-17 02:03:06 '
---

## Problem #3312: Sorted GCD Pair Queries

**Difficulty:** Hard

**Topics:** Array, Hash Table, Math, Binary Search, Combinatorics, Counting, Number Theory, Prefix Sum

## Problem Description

<p>You are given an integer array <code>nums</code> of length <code>n</code> and an integer array <code>queries</code>.</p>

<p>Let <code>gcdPairs</code> denote an array obtained by calculating the <span data-keyword="gcd-function">GCD</span> of all possible pairs <code>(nums[i], nums[j])</code>, where <code>0 &lt;= i &lt; j &lt; n</code>, and then sorting these values in <strong>ascending</strong> order.</p>

<p>For each query <code>queries[i]</code>, you need to find the element at index <code>queries[i]</code> in <code>gcdPairs</code>.</p>

<p>Return an integer array <code>answer</code>, where <code>answer[i]</code> is the value at <code>gcdPairs[queries[i]]</code> for each query.</p>

<p>The term <code>gcd(a, b)</code> denotes the <strong>greatest common divisor</strong> of <code>a</code> and <code>b</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,3,4], queries = [0,2,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,2,2]</span></p>

<p><strong>Explanation:</strong></p>

<p><code>gcdPairs = [gcd(nums[0], nums[1]), gcd(nums[0], nums[2]), gcd(nums[1], nums[2])] = [1, 2, 1]</code>.</p>

<p>After sorting in ascending order, <code>gcdPairs = [1, 1, 2]</code>.</p>

<p>So, the answer is <code>[gcdPairs[queries[0]], gcdPairs[queries[1]], gcdPairs[queries[2]]] = [1, 2, 2]</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,4,2,1], queries = [5,3,1,0]</span></p>

<p><strong>Output:</strong> <span class="example-io">[4,2,1,1]</span></p>

<p><strong>Explanation:</strong></p>

<p><code>gcdPairs</code> sorted in ascending order is <code>[1, 1, 1, 2, 2, 4]</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,2], queries = [0,0]</span></p>

<p><strong>Output:</strong> <span class="example-io">[2,2]</span></p>

<p><strong>Explanation:</strong></p>

<p><code>gcdPairs = [2]</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= queries[i] &lt; n * (n - 1) / 2</code></li>
</ul>


## Hints

1. Try counting the number of pairs that have a GCD of g</code.

2. Use inclusion-exclusion.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To solve this problem efficiently, we count the occurrences of each possible GCD value by first determining the frequency of each number in the input array. We let $S(g)$ be the number of elements in 'nums' that are multiples of $g$. The number of pairs $(i, j)$ such that both $nums[i]$ and $nums[j]$ are multiples of $g$ is given by $P(g) = \frac{S(g)(S(g)-1)}{2}$. However, $P(g)$ includes pairs whose GCD is any multiple of $g$ (i.e., $g, 2g, 3g, \dots$). To find the exact count of pairs with GCD equal to $g$, denoted as $f(g)$, we use inclusion-exclusion (or a backward DP): $f(g) = P(g) - \sum_{k=2}^{\lfloor M/g \rfloor} f(k \cdot g)$, where $M$ is the maximum value in 'nums'. By iterating $g$ from $M$ down to 1, we can compute all $f(g)$ values in $O(M \log M)$ time.

Once we have the counts of pairs for each GCD value $g \in [1, M]$, we compute the prefix sums of these counts. Let $prefix[g]$ represent the total number of pairs $(i, j)$ whose GCD is less than or equal to $g$. Since the array of all GCD pairs is sorted in ascending order, the element at a specific index $q$ in the sorted 'gcdPairs' array is the smallest $g$ such that $prefix[g] > q$. For each query, we perform a binary search on the prefix sum array to find this smallest $g$. This approach is highly efficient given the constraints $n \le 10^5$ and $M \le 5 \cdot 10^4$.

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
    vector<int> gcdValues(vector<int>& nums, vector<long long>& queries) {
        int max_val = 0;
        for (int x : nums) if (x > max_val) max_val = x;

        vector<int> cnt(max_val + 1, 0);
        for (int x : nums) cnt[x]++;

        vector<long long> f(max_val + 1, 0);
        for (int g = max_val; g >= 1; --g) {
            long long multiples = 0;
            for (int m = g; m <= max_val; m += g) {
                multiples += cnt[m];
            }
            long long pairs = multiples * (multiples - 1) / 2;
            for (int m = 2 * g; m <= max_val; m += g) {
                pairs -= f[m];
            }
            f[g] = pairs;
        }

        vector<long long> prefix_f(max_val + 1, 0);
        for (int i = 1; i <= max_val; ++i) {
            prefix_f[i] = prefix_f[i - 1] + f[i];
        }

        vector<int> result;
        result.reserve(queries.size());
        for (long long q : queries) {
            auto it = upper_bound(prefix_f.begin(), prefix_f.end(), q);
            result.push_back((int)(distance(prefix_f.begin(), it)));
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
class Solution {
    public int[] gcdValues(int[] nums, long[] queries) {
        int maxVal = 0;
        for (int x : nums) {
            if (x > maxVal) maxVal = x;
        }

        int[] cnt = new int[maxVal + 1];
        for (int x : nums) {
            cnt[x]++;
        }

        long[] f = new long[maxVal + 1];
        for (int g = maxVal; g >= 1; g--) {
            long multiples = 0;
            for (int m = g; m <= maxVal; m += g) {
                multiples += cnt[m];
            }
            long pairs = multiples * (multiples - 1) / 2;
            for (int m = 2 * g; m <= maxVal; m += g) {
                pairs -= f[m];
            }
            f[g] = pairs;
        }

        long[] prefixF = new long[maxVal + 1];
        for (int i = 1; i <= maxVal; i++) {
            prefixF[i] = prefixF[i - 1] + f[i];
        }

        int[] result = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            long q = queries[i];
            int low = 1, high = maxVal;
            int ans = maxVal;
            while (low <= high) {
                int mid = low + (high - low) / 2;
                if (prefixF[mid] > q) {
                    ans = mid;
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }
            result[i] = ans;
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
import bisect

class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        max_val = max(nums)
        cnt = [0] * (max_val + 1)
        for x in nums:
            cnt[x] += 1

        f = [0] * (max_val + 1)
        for g in range(max_val, 0, -1):
            multiples = 0
            for m in range(g, max_val + 1, g):
                multiples += cnt[m]

            pairs = multiples * (multiples - 1) // 2
            for m in range(2 * g, max_val + 1, g):
                pairs -= f[m]
            f[g] = pairs

        prefix_f = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix_f[i] = prefix_f[i-1] + f[i]

        ans = []
        for q in queries:
            # Find the smallest index i such that prefix_f[i] > q
            idx = bisect.bisect_right(prefix_f, q)
            ans.append(idx)

        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from typing import List
import bisect

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        freq = [0] * (max_val + 1)
        for x in nums:
            freq[x] += 1

        count = [0] * (max_val + 1)
        for g in range(1, max_val + 1):
            for m in range(g, max_val + 1, g):
                count[g] += freq[m]

        f = [0] * (max_val + 1)
        for g in range(max_val, 0, -1):
            total_pairs = (count[g] * (count[g] - 1)) // 2
            f[g] = total_pairs
            for m in range(2 * g, max_val + 1, g):
                f[g] -= f[m]

        prefix_sum = [0] * (max_val + 1)
        for g in range(1, max_val + 1):
            prefix_sum[g] = prefix_sum[g - 1] + f[g]

        return [bisect.bisect_right(prefix_sum, q) for q in queries]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* gcdValues(int* nums, int numsSize, long long* queries, int queriesSize, int* returnSize) {
    int maxVal = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > maxVal) maxVal = nums[i];
    }

    int* freq = (int*)calloc(maxVal + 1, sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        freq[nums[i]]++;
    }

    long long* count = (long long*)calloc(maxVal + 1, sizeof(long long));
    for (int g = 1; g <= maxVal; g++) {
        for (int m = g; m <= maxVal; m += g) {
            count[g] += freq[m];
        }
    }

    long long* f = (long long*)calloc(maxVal + 1, sizeof(long long));
    for (int g = maxVal; g >= 1; g--) {
        f[g] = (count[g] * (count[g] - 1)) / 2;
        for (int m = 2 * g; m <= maxVal; m += g) {
            f[g] -= f[m];
        }
    }

    long long* prefixSum = (long long*)calloc(maxVal + 1, sizeof(long long));
    for (int g = 1; g <= maxVal; g++) {
        prefixSum[g] = prefixSum[g - 1] + f[g];
    }

    int* result = (int*)malloc(queriesSize * sizeof(int));
    *returnSize = queriesSize;

    for (int i = 0; i < queriesSize; i++) {
        long long q = queries[i];
        int low = 1, high = maxVal, res = maxVal;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (prefixSum[mid] > q) {
                res = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        result[i] = res;
    }

    free(freq);
    free(count);
    free(f);
    free(prefixSum);

    return result;
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
    public int[] GcdValues(int[] nums, long[] queries) {
        int maxVal = 0;
        foreach (int x in nums) {
            if (x > maxVal) maxVal = x;
        }

        int[] freq = new int[maxVal + 1];
        foreach (int x in nums) {
            freq[x]++;
        }

        long[] count = new long[maxVal + 1];
        for (int g = 1; g <= maxVal; g++) {
            for (int m = g; m <= maxVal; m += g) {
                count[g] += freq[m];
            }
        }

        long[] f = new long[maxVal + 1];
        for (int g = maxVal; g >= 1; g--) {
            f[g] = (count[g] * (count[g] - 1)) / 2;
            for (int m = 2 * g; m <= maxVal; m += g) {
                f[g] -= f[m];
            }
        }

        long[] prefixSum = new long[maxVal + 1];
        for (int g = 1; g <= maxVal; g++) {
            prefixSum[g] = prefixSum[g - 1] + f[g];
        }

        int[] result = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            long q = queries[i];
            int low = 1, high = maxVal, res = maxVal;
            while (low <= high) {
                int mid = low + (high - low) / 2;
                if (prefixSum[mid] > q) {
                    res = mid;
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }
            result[i] = res;
        }

        return result;
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
 * @param {number[]} queries
 * @return {number[]}
 */
var gcdValues = function(nums, queries) {
    let maxVal = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > maxVal) maxVal = nums[i];
    }

    let freq = new Int32Array(maxVal + 1);
    for (let i = 0; i < nums.length; i++) {
        freq[nums[i]]++;
    }

    let count = new Float64Array(maxVal + 1);
    for (let g = 1; g <= maxVal; g++) {
        for (let m = g; m <= maxVal; m += g) {
            count[g] += freq[m];
        }
    }

    let f = new Float64Array(maxVal + 1);
    for (let g = maxVal; g >= 1; g--) {
        f[g] = (count[g] * (count[g] - 1)) / 2;
        for (let m = 2 * g; m <= maxVal; m += g) {
            f[g] -= f[m];
        }
    }

    let prefixSum = new Float64Array(maxVal + 1);
    for (let g = 1; g <= maxVal; g++) {
        prefixSum[g] = prefixSum[g - 1] + f[g];
    }

    let results = [];
    for (let i = 0; i < queries.length; i++) {
        let q = queries[i];
        let low = 1, high = maxVal, res = maxVal;
        while (low <= high) {
            let mid = Math.floor((low + high) / 2);
            if (prefixSum[mid] > q) {
                res = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        results.push(res);
    }
    return results;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function gcdValues(nums: number[], queries: number[]): number[] {
    let maxVal = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > maxVal) maxVal = nums[i];
    }

    const freqMap = new Int32Array(maxVal + 1);
    for (const x of nums) {
        freqMap[x]++;
    }

    const countGCD = new Float64Array(maxVal + 1);
    for (let i = maxVal; i >= 1; i--) {
        let c = 0;
        for (let j = i; j <= maxVal; j += i) {
            c += freqMap[j];
        }
        let pairs = (c * (c - 1)) / 2;
        for (let j = 2 * i; j <= maxVal; j += i) {
            pairs -= countGCD[j];
        }
        countGCD[i] = pairs;
    }

    const pref = new Float64Array(maxVal + 1);
    for (let i = 1; i <= maxVal; i++) {
        pref[i] = pref[i - 1] + countGCD[i];
    }

    const results = new Int32Array(queries.length);
    for (let k = 0; k < queries.length; k++) {
        const q = queries[k];
        let low = 1, high = maxVal, ans = maxVal;
        while (low <= high) {
            let mid = Math.floor((low + high) / 2);
            if (pref[mid] > q) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        results[k] = ans;
    }

    return Array.from(results);
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
     * @param Integer[] $queries
     * @return Integer[]
     */
    function gcdValues($nums, $queries) {
        $maxVal = 0;
        foreach ($nums as $num) {
            if ($num > $maxVal) $maxVal = $num;
        }

        $freqMap = array_fill(0, $maxVal + 1, 0);
        foreach ($nums as $num) {
            $freqMap[$num]++;
        }

        $countGCD = array_fill(0, $maxVal + 1, 0);
        for ($i = $maxVal; $i >= 1; $i--) {
            $c = 0;
            for ($j = $i; $j <= $maxVal; $j += $i) {
                $c += $freqMap[$j];
            }
            $pairs = ($c * ($c - 1)) / 2;
            for ($j = 2 * $i; $j <= $maxVal; $j += $i) {
                $pairs -= $countGCD[$j];
            }
            $countGCD[$i] = $pairs;
        }

        $pref = array_fill(0, $maxVal + 1, 0);
        for ($i = 1; $i <= $maxVal; $i++) {
            $pref[$i] = $pref[$i - 1] + $countGCD[$i];
        }

        $ans = [];
        foreach ($queries as $q) {
            $low = 1;
            $high = $maxVal;
            $res = $maxVal;
            while ($low <= high) {
                $mid = ($low + $high) >> 1;
                if ($pref[$mid] > $q) {
                    $res = $mid;
                    $high = $mid - 1;
                } else {
                    $low = $mid + 1;
                }
            }
            $ans[] = $res;
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
    func gcdValues(_ nums: [Int], _ queries: [Int]) -> [Int] {
        let maxVal = nums.max() ?? 0
        var freqMap = [Int](repeating: 0, count: maxVal + 1)
        for x in nums {
            freqMap[x] += 1
        }

        var countGCD = [Int](repeating: 0, count: maxVal + 1)
        for i in stride(from: maxVal, through: 1, by: -1) {
            var c = 0
            for j in stride(from: i, through: maxVal, by: i) {
                c += freqMap[j]
            }
            var pairs = c * (c - 1) / 2
            for j in stride(from: 2 * i, through: maxVal, by: i) {
                pairs -= countGCD[j]
            }
            countGCD[i] = pairs
        }

        var pref = [Int](repeating: 0, count: maxVal + 1)
        for i in 1...maxVal {
            pref[i] = pref[i - 1] + countGCD[i]
        }

        var result = [Int]()
        result.reserveCapacity(queries.count)
        for q in queries {
            var low = 1
            var high = maxVal
            var ans = maxVal
            while low <= high {
                let mid = (low + high) / 2
                if pref[mid] > q {
                    ans = mid
                    high = mid - 1
                } else {
                    low = mid + 1
                }
            }
            result.append(ans)
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
    fun gcdValues(nums: IntArray, queries: LongArray): IntArray {
        val maxVal = nums.maxOrNull() ?: 0
        val freqMap = IntArray(maxVal + 1)
        for (x in nums) {
            freqMap[x]++
        }

        val countGCD = LongArray(maxVal + 1)
        for (i in maxVal downTo 1) {
            var c: Long = 0
            for (j in i..maxVal step i) {
                c += freqMap[j]
            }
            var pairs: Long = c * (c - 1) / 2
            for (j in 2 * i..maxVal step i) {
                pairs -= countGCD[j]
            }
            countGCD[i] = pairs
        }

        val pref = LongArray(maxVal + 1)
        for (i in 1..maxVal) {
            pref[i] = pref[i - 1] + countGCD[i]
        }

        val result = IntArray(queries.size)
        for (i in queries.indices) {
            val q = queries[i]
            var low = 1
            var high = maxVal
            var ans = maxVal
            while (low <= high) {
                val mid = (low + high) / 2
                if (pref[mid] > q) {
                    ans = mid
                    high = mid - 1
                } else {
                    low = mid + 1
                }
            }
            result[i] = ans
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
  List<int> gcdValues(List<int> nums, List<int> queries) {
    int m = nums[0];
    for (int x in nums) {
      if (x > m) m = x;
    }

    List<int> freq = List<int>.filled(m + 1, 0);
    for (int x in nums) {
      freq[x]++;
    }

    List<int> f = List<int>.filled(m + 1, 0);
    for (int g = m; g >= 1; g--) {
      int count = 0;
      for (int k = g; k <= m; k += g) {
        count += freq[k];
      }
      int totalPairsWithMultipleG = (count * (count - 1)) ~/ 2;
      int others = 0;
      for (int k = 2 * g; k <= m; k += g) {
        others += f[k];
      }
      f[g] = totalPairsWithMultipleG - others;
    }

    List<int> pref = List<int>.filled(m + 1, 0);
    for (int g = 1; g <= m; g++) {
      pref[g] = pref[g - 1] + f[g];
    }

    List<int> ans = List<int>.filled(queries.length, 0);
    for (int i = 0; i < queries.length; i++) {
      int q = queries[i];
      int low = 1, high = m;
      int result = m;
      while (low <= high) {
        int mid = low + (high - low) ~/ 2;
        if (pref[mid] > q) {
          result = mid;
          high = mid - 1;
        } else {
          low = mid + 1;
        }
      }
      ans[i] = result;
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
func gcdValues(nums []int, queries []int64) []int {
	m := 0
	for _, x := range nums {
		if x > m {
			m = x
		}
	}

	freq := make([]int, m+1)
	for _, x := range nums {
		freq[x]++
	}

	f := make([]int64, m+1)
	for g := m; g >= 1; g-- {
		count := int64(0)
		for k := g; k <= m; k += g {
			count += int64(freq[k])
		}
		hG := count * (count - 1) / 2
		for k := 2 * g; k <= m; k += g {
			hG -= f[k]
		}
		f[g] = hG
	}

	pref := make([]int64, m+1)
	for g := 1; g <= m; g++ {
		pref[g] = pref[g-1] + f[g]
	}

	ans := make([]int, len(queries))
	for i, q := range queries {
		idx := sort.Search(len(pref), func(j int) bool {
			return pref[j] > q
		})
		ans[i] = idx
	}

	return ans
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @param {Integer[]} queries
# @return {Integer[]}
def gcd_values(nums, queries)
  max_num = nums.max
  freq = Array.new(max_num + 1, 0)
  nums.each { |x| freq[x] += 1 }

  f = Array.new(max_num + 1, 0)
  max_num.step(1, -1) do |g|
    count = 0
    g.step(max_num, g) { |k| count += freq[k] }

    h_g = count * (count - 1) / 2

    (2 * g).step(max_num, g) { |k| h_g -= f[k] }
    f[g] = h_g
  end

  pref = Array.new(max_num + 1, 0)
  (1..max_num).each { |g| pref[g] = pref[g-1] + f[g] }

  queries.map do |q|
    (1..max_num).bsearch { |g| pref[g] > q }
  end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def gcdValues(nums: Array[Int], queries: Array[Long]): Array[Int] = {
        val maxNum = nums.max
        val freq = new Array[Int](maxNum + 1)
        for (x <- nums) freq(x) += 1

        val f = new Array[Long](maxNum + 1)
        for (g <- maxNum to 1 by -1) {
            var count = 0L
            var k = g
            while (k <= maxNum) {
                count += freq(k)
                k += g
            }
            var hG = count * (count - 1) / 2
            var k2 = 2 * g
            while (k2 <= maxNum) {
                hG -= f(k2)
                k2 += g
            }
            f(g) = hG
        }

        val pref = new Array[Long](maxNum + 1)
        for (g <- 1 to maxNum) {
            pref(g) = pref(g - 1) + f(g)
        }

        val ans = new Array[Int](queries.length)
        for (i <- queries.indices) {
            val q = queries(i)
            var low = 1
            var high = maxNum
            var res = maxNum
            while (low <= high) {
                val mid = low + (high - low) / 2
                if (pref(mid) > q) {
                    res = mid
                    high = mid - 1
                } else {
                    low = mid + 1
                }
            }
            ans(i) = res
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
    pub fn gcd_values(nums: Vec<i32>, queries: Vec<i64>) -> Vec<i32> {
        let max_val = *nums.iter().max().unwrap_or(&0) as usize;
        let mut count = vec![0i64; max_val + 1];
        for &x in &nums {
            count[x as usize] += 1;
        }

        let mut h = vec![0i64; max_val + 1];
        for g in (1..=max_val).rev() {
            let mut c_g = 0i64;
            let mut i = g;
            while i <= max_val {
                c_g += count[i];
                i += g;
            }
            let total_pairs_multiple_g = c_g * (c_g - 1) / 2;
            let mut sum_h_multiples = 0i64;
            let mut j = 2 * g;
            while j <= max_val {
                sum_h_multiples += h[j];
                j += g;
            }
            h[g] = total_pairs_multiple_g - sum_h_multiples;
        }

        let mut pref = vec![0i64; max_val + 1];
        for i in 1..=max_val {
            pref[i] = pref[i - 1] + h[i];
        }

        queries.into_iter().map(|q| {
            let mut low = 1;
            let mut high = max_val;
            let mut ans = max_val;
            while low <= high {
                let mid = low + (high - low) / 2;
                if pref[mid] > q {
                    ans = mid;
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }
            ans as i32
        }).collect()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (gcd-values nums queries)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  (let* ([max-val (for/fold ([m 0]) ([x nums]) (max m x))]
         [count (make-vector (+ max-val 1) 0)])
    (for ([x nums])
      (vector-set! count x (+ (vector-ref count x) 1)))

    (define h (make-vector (+ max-val 1) 0))
    (for ([g (in-range max-val 0 -1)])
      (let* ([c-g (for/fold ([acc 0])
                            ([i (in-range g (+ max-val 1) g)])
                    (+ acc (vector-ref count i)))]
             [total-pairs (quotient (* c-g (- c-g 1)) 2)]
             [sum-h (for/fold ([acc 0])
                              ([i (in-range (* 2 g) (+ max-val 1) g)])
                      (+ acc (vector-ref h i)))])
        (vector-set! h g (- total-pairs sum-h))))

    (define pref (make-vector (+ max-val 1) 0))
    (for ([i (in-range 1 (+ max-val 1))])
      (vector-set! pref i (+ (vector-ref pref (- i 1)) (vector-ref h i))))

    (define (binary-search target)
      (let loop ([low 1] [high max-val])
        (if (> low high)
            low
            (let* ([mid (quotient (+ low high) 2)]
                   [val (vector-ref pref mid)])
              (if (> val target)
                  (loop low (- mid 1))
                  (loop (+ mid 1) high))))))

    (map binary-search queries)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec gcd_values(Nums :: [integer()], Queries :: [integer()]) -> [integer()].
gcd_values(Nums, Queries) ->
  MaxVal = lists:foldl(fn(X, Acc) -> erlang:max(X, Acc) end, 0, Nums),
  Cnts = atomics:new(MaxVal, [{signed, true}]),
  HAtoms = atomics:new(MaxVal, [{signed, true}]),
  lists:foreach(fn(X) -> atomics:add(Cnts, X, 1) end, Nums),

  LoopG = fun(G, Self) ->
    if G > 0 ->
      CG = get_cg(G, MaxVal, G, 0, Cnts),
      TotalPairs = CG * (CG - 1) div 2,
      SumH = get_sum_h(2 * G, MaxVal, G, 0, HAtoms),
      atomics:put(HAtoms, G, TotalPairs - SumH),
      Self(G - 1, Self);
    true -> ok
    end
  end,
  LoopG(MaxVal, LoopG),

  {_, PrefList} = lists:foldl(fn(G, {Acc, L}) ->
    NewAcc = Acc + atomics:get(HAtoms, G),
    {NewAcc, [NewAcc | L]}
  end, {0, [0]}, lists:seq(1, MaxVal)),

  PrefTuple = list_to_tuple(lists:reverse(PrefList)),
  [binary_search(PrefTuple, Q, 1, MaxVal) || Q <- Queries].

get_cg(I, MaxVal, Step, Acc, Cnts) ->
  if I > MaxVal -> Acc;
    true -> get_cg(I + Step, MaxVal, Step, Acc + atomics:get(Cnts, I), Cnts)
  end.

get_sum_h(I, MaxVal, Step, Acc, HAtoms) ->
  if I > MaxVal -> Acc;
    true -> get_sum_h(I + Step, MaxVal, Step, Acc + atomics:get(HAtoms, I), HAtoms)
  end.

binary_search(PrefTuple, Target, Low, High) ->
  if Low > High -> Low;
    true ->
      Mid = (Low + High) div 2,
      Val = element(Mid + 1, PrefTuple),
      if Val > Target -> binary_search(PrefTuple, Target, Low, Mid - 1);
        true -> binary_search(PrefTuple, Target, Mid + 1, High)
      end
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec gcd_values(nums :: [integer], queries :: [integer]) :: [integer]
  def gcd_values(nums, queries) do
    max_val = Enum.reduce(nums, 0, &max/2)
    cnts = :atomics.new(max_val, [{:signed, true}])
    h_atoms = :atomics.new(max_val, [{:signed, true}])

    Enum.each(nums, fn x -> :atomics.add(cnts, x, 1) end)

    for g <- max_val..1 do
      cg = get_cg(g, max_val, g, 0, cnts)
      total_pairs = div(cg * (cg - 1), 2)
      sum_h = get_sum_h(2 * g, max_val, g, 0, h_atoms)
      :atomics.put(h_atoms, g, total_pairs - sum_h)
    end

    pref_list = 
      Enum.scan(1..max_val, 0, fn g, acc -> 
        acc + :atomics.get(h_atoms, g)
      end)

    pref_tuple = List.to_tuple([0 | pref_list])

    Enum.map(queries, fn q -> 
      binary_search(pref_tuple, q, 1, max_val)
    end)
  end

  defp get_cg(i, max_val, step, acc, cnts) when i > max_val, do: acc
  defp get_cg(i, max_val, step, acc, cnts) do
    get_cg(i + step, max_val, step, acc + :atomics.get(cnts, i), cnts)
  end

  defp get_sum_h(i, max_val, step, acc, h_atoms) when i > max_val, do: acc
  defp get_sum_h(i, max_val, step, acc, h_atoms) do
    get_sum_h(i + step, max_val, step, acc + :atomics.get(h_atoms, i), h_atoms)
  end

  defp binary_search(pref_tuple, target, low, high) when low > high, do: low
  defp binary_search(pref_tuple, target, low, high) do
    mid = div(low + high, 2)
    val = elem(pref_tuple, mid)
    if val > target do
      binary_search(pref_tuple, target, low, mid - 1)
    else
      binary_search(pref_tuple, target, mid + 1, high)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N + M \log M + Q \log M), where $N$ is the number of elements in 'nums', $M$ is the maximum value in 'nums' ($5 \cdot 10^4$), and $Q$ is the number of queries. Calculating frequencies and $S(g)$ takes $O(N + M \log M)$, calculating $f(g)$ takes $O(M \log M)$, and processing $Q$ queries via binary search takes $O(Q \log M)$.
- **Space Complexity:** O(N + M), where $N$ is the size of the input and $M$ is the maximum value in 'nums'. We store the frequency array, the count of multiples, the GCD pair counts, and the prefix sums, all of which are proportional to $M$.
