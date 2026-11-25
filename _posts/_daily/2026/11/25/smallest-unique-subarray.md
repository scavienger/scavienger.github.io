---
layout: post
title: "Smallest Unique Subarray"
date: 2026-11-25 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Hash Table", "Binary Search", "Rolling Hash", "Suffix Array", "Hash Function"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/smallest-unique-subarray/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <algorithm>\n#include <cstdint>\n\nusing namespace\
        \ std;\n\nclass Solution {\npublic:\n    int smallestUniqueSubarray(vector<int>&\
        \ nums) {\n        int n = nums.size();\n        int low = 1, high = n, ans\
        \ = n;\n        while (low <= high) {\n            int mid = low + (high - low)\
        \ / 2;\n            if (check(mid, n, nums)) {\n                ans = mid;\n\
        \                high = mid - 1;\n            } else {\n                low\
        \ = mid + 1;\n            }\n        }\n        return ans;\n    }\n\nprivate:\n\
        \    bool check(int len, int n, const vector<int>& nums) {\n        if (len\
        \ <= 0) return false;\n        long long mod1 = 1000000007LL;\n        long\
        \ long mod2 = 1000000009LL;\n        long long base1 = 100019LL;\n        long\
        \ long base2 = 100043LL;\n        long long h1 = 0, h2 = 0;\n        long long\
        \ p1 = 1, p2 = 1;\n\n        for (int i = 0; i < len; ++i) {\n            h1\
        \ = (h1 * base1 + nums[i]) % mod1;\n            h2 = (h2 * base2 + nums[i])\
        \ % mod2;\n            if (i > 0) {\n                p1 = (p1 * base1) % mod1;\n\
        \                p2 = (p2 * base2) % mod2;\n            }\n        }\n\n   \
        \     vector<uint64_t> hashes;\n        hashes.reserve(n - len + 1);\n     \
        \   hashes.push_back(((uint64_t)h1 << 32) | (uint64_t)h2);\n\n        for (int\
        \ i = len; i < n; ++i) {\n            h1 = (h1 - nums[i - len] * p1 % mod1 +\
        \ mod1) % mod1;\n            h1 = (h1 * base1 + nums[i]) % mod1;\n         \
        \   h2 = (h2 - nums[i - len] * p2 % mod2 + mod2) % mod2;\n            h2 = (h2\
        \ * base2 + nums[i]) % mod2;\n            hashes.push_back(((uint64_t)h1 <<\
        \ 32) | (uint64_t)h2);\n        }\n\n        sort(hashes.begin(), hashes.end());\n\
        \n        for (size_t i = 0; i < hashes.size(); ++i) {\n            if ((i ==\
        \ 0 || hashes[i] != hashes[i - 1]) &&\n                (i == hashes.size() -\
        \ 1 || hashes[i] != hashes[i + 1])) {\n                return true;\n      \
        \      }\n        }\n        return false;\n    }\n};"
      java: "import java.util.Arrays;\n\nclass Solution {\n    public int smallestUniqueSubarray(int[]\
        \ nums) {\n        int n = nums.length;\n        int low = 1, high = n, ans\
        \ = n;\n        while (low <= high) {\n            int mid = low + (high - low)\
        \ / 2;\n            if (check(mid, n, nums)) {\n                ans = mid;\n\
        \                high = mid - 1;\n            } else {\n                low\
        \ = mid + 1;\n            }\n        }\n        return ans;\n    }\n\n    private\
        \ boolean check(int len, int n, int[] nums) {\n        long mod1 = 1000000007L;\n\
        \        long mod2 = 1000000009L;\n        long base1 = 100019L;\n        long\
        \ base2 = 100043L;\n        long h1 = 0, h2 = 0;\n        long p1 = 1, p2 =\
        \ 1;\n\n        for (int i = 0; i < len; i++) {\n            h1 = (h1 * base1\
        \ + nums[i]) % mod1;\n            h2 = (h2 * base2 + nums[i]) % mod2;\n    \
        \        if (i > 0) {\n                p1 = (p1 * base1) % mod1;\n         \
        \       p2 = (p2 * base2) % mod2;\n            }\n        }\n\n        long[]\
        \ hashes = new long[n - len + 1];\n        hashes[0] = ((long) h1 << 32) | (h2\
        \ & 0xFFFFFFFFL);\n\n        for (int i = len; i < n; i++) {\n            h1\
        \ = (h1 - (nums[i - len] * p1) % mod1 + mod1) % mod1;\n            h1 = (h1\
        \ * base1 + nums[i]) % mod1;\n            h2 = (h2 - (nums[i - len] * p2) %\
        \ mod2 + mod2) % mod2;\n            h2 = (h2 * base2 + nums[i]) % mod2;\n  \
        \          hashes[i - len + 1] = ((long) h1 << 32) | (h2 & 0xFFFFFFFFL);\n \
        \       }\n\n        Arrays.sort(hashes);\n\n        for (int i = 0; i < hashes.length;\
        \ i++) {\n            if ((i == 0 || hashes[i] != hashes[i - 1]) &&\n      \
        \          (i == hashes.length - 1 || hashes[i] != hashes[i + 1])) {\n     \
        \           return true;\n            }\n        }\n        return false;\n\
        \    }\n}"
      python: "class Solution(object):\n    def smallestUniqueSubarray(self, nums):\n\
        \        \"\"\"\n        :type nums: List[int]\n        :rtype: int\n      \
        \  \"\"\"\n        n = len(nums)\n        low, high, ans = 1, n, n\n\n     \
        \   def check(length):\n            if length <= 0:\n                return\
        \ False\n            MOD = (1 << 61) - 1\n            BASE = 100019\n      \
        \      P = pow(BASE, length - 1, MOD)\n            h = 0\n            for i\
        \ in range(length):\n                h = (h * BASE + nums[i]) % MOD\n\n    \
        \        hashes = [h]\n            for i in range(length, n):\n            \
        \    h = ((h - nums[i-length] * P) * BASE + nums[i]) % MOD\n               \
        \ hashes.append(h)\n\n            hashes.sort()\n            for i in range(len(hashes)):\n\
        \                if (i == 0 or hashes[i] != hashes[i-1]) and \\\n          \
        \         (i == len(hashes) - 1 or hashes[i] != hashes[i+1]):\n            \
        \        return True\n            return False\n\n        while low <= high:\n\
        \            mid = (low + high) // 2\n            if check(mid):\n         \
        \       ans = mid\n                high = mid - 1\n            else:\n     \
        \           low = mid + 1\n        return ans"
      python3: "from typing import List\n\nclass Solution:\n    def smallestUniqueSubarray(self,\
        \ nums: List[int]) -> int:\n        n = len(nums)\n        low, high, ans =\
        \ 1, n, n\n\n        def check(length: int) -> bool:\n            if length\
        \ <= 0:\n                return False\n            MOD = (1 << 61) - 1\n   \
        \         BASE = 100019\n            P = pow(BASE, length - 1, MOD)\n      \
        \      h = 0\n            for i in range(length):\n                h = (h *\
        \ BASE + nums[i]) % MOD\n\n            num_hashes = n - length + 1\n       \
        \     hashes = [0] * num_hashes\n            hashes[0] = h\n            for\
        \ i in range(length, n):\n                h = ((h - nums[i - length] * P) *\
        \ BASE + nums[i]) % MOD\n                hashes[i - length + 1] = h\n\n    \
        \        hashes.sort()\n            for i in range(num_hashes):\n          \
        \      if (i == 0 or hashes[i] != hashes[i - 1]) and \\\n                  \
        \ (i == num_hashes - 1 or hashes[i] != hashes[i + 1]):\n                   \
        \ return True\n            return False\n\n        while low <= high:\n    \
        \        mid = (low + high) // 2\n            if check(mid):\n             \
        \   ans = mid\n                high = mid - 1\n            else:\n         \
        \       low = mid + 1\n        return ans"
      c: "#include <stdlib.h>\n#include <stdint.h>\n\ntypedef unsigned long long ull;\n\
        typedef __uint128_t u128;\n\nstatic ull mul_mod(ull a, ull b) {\n    ull mod\
        \ = (1ULL << 61) - 1;\n    u128 res = (u128)a * b;\n    ull ans = (ull)(res\
        \ >> 61) + (ull)(res & mod);\n    if (ans >= mod) ans -= mod;\n    return ans;\n\
        }\n\nstatic ull mod_pow(ull base, int exp) {\n    ull res = 1;\n    ull mod\
        \ = (1ULL << 61) - 1;\n    base %= mod;\n    while (exp > 0) {\n        if (exp\
        \ % 2 == 1) res = mul_mod(res, base);\n        base = mul_mod(base, base);\n\
        \        exp /= 2;\n    }\n    return res;\n}\n\nstatic int compare(const void*\
        \ a, const void* b) {\n    ull val1 = *(ull*)a;\n    ull val2 = *(ull*)b;\n\
        \    if (val1 < val2) return -1;\n    if (val1 > val2) return 1;\n    return\
        \ 0;\n}\n\nstatic int check(int length, int* nums, int numsSize) {\n    if (length\
        \ <= 0) return 0;\n    ull mod = (1ULL << 61) - 1;\n    ull base = 100019;\n\
        \    ull p = mod_pow(base, length - 1);\n    ull h = 0;\n    for (int i = 0;\
        \ i < length; i++) {\n        h = (mul_mod(h, base) + (ull)nums[i]) % mod;\n\
        \    }\n    int num_hashes = numsSize - length + 1;\n    ull* hashes = (ull*)malloc(num_hashes\
        \ * sizeof(ull));\n    hashes[0] = h;\n    for (int i = length; i < numsSize;\
        \ i++) {\n        ull p_term = mul_mod((ull)nums[i - length], p);\n        h\
        \ = (h + mod - p_term) % mod;\n        h = (mul_mod(h, base) + (ull)nums[i])\
        \ % mod;\n        hashes[i - length + 1] = h;\n    }\n    qsort(hashes, num_hashes,\
        \ sizeof(ull), compare);\n    int found = 0;\n    for (int i = 0; i < num_hashes;\
        \ i++) {\n        if ((i == 0 || hashes[i] != hashes[i - 1]) && \n         \
        \   (i == num_hashes - 1 || hashes[i] != hashes[i + 1])) {\n            found\
        \ = 1;\n            break;\n        }\n    }\n    free(hashes);\n    return\
        \ found;\n}\n\nint smallestUniqueSubarray(int* nums, int numsSize) {\n    int\
        \ low = 1, high = numsSize, ans = numsSize;\n    while (low <= high) {\n   \
        \     int mid = low + (high - low) / 2;\n        if (check(mid, nums, numsSize))\
        \ {\n            ans = mid;\n            high = mid - 1;\n        } else {\n\
        \            low = mid + 1;\n        }\n    }\n    return ans;\n}"
      csharp: "using System;\nusing System.Numerics;\n\npublic class Solution {\n  \
        \  public int SmallestUniqueSubarray(int[] nums) {\n        int n = nums.Length;\n\
        \        int low = 1, high = n, ans = n;\n        while (low <= high) {\n  \
        \          int mid = low + (high - low) / 2;\n            if (Check(mid, nums))\
        \ {\n                ans = mid;\n                high = mid - 1;\n         \
        \   } else {\n                low = mid + 1;\n            }\n        }\n   \
        \     return ans;\n    }\n\n    private bool Check(int length, int[] nums) {\n\
        \        if (length <= 0) return false;\n        int n = nums.Length;\n    \
        \    BigInteger MOD = (BigInteger.One << 61) - 1;\n        BigInteger BASE =\
        \ 100019;\n        BigInteger P = BigInteger.ModPow(BASE, length - 1, MOD);\n\
        \        BigInteger h = 0;\n        for (int i = 0; i < length; i++) {\n   \
        \         h = (h * BASE + nums[i]) % MOD;\n        }\n        int numHashes\
        \ = n - length + 1;\n        ulong[] hashes = new ulong[numHashes];\n      \
        \  hashes[0] = (ulong)h;\n        for (int i = length; i < n; i++) {\n     \
        \       h = ((h - (BigInteger)nums[i - length] * P % MOD + MOD) * BASE + nums[i])\
        \ % MOD;\n            hashes[i - length + 1] = (ulong)h;\n        }\n      \
        \  Array.Sort(hashes);\n        for (int i = 0; i < numHashes; i++) {\n    \
        \        if ((i == 0 || hashes[i] != hashes[i - 1]) && \n                (i\
        \ == numHashes - 1 || hashes[i] != hashes[i + 1])) {\n                return\
        \ true;\n            }\n        }\n        return false;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar smallestUniqueSubarray\
        \ = function(nums) {\n    const n = nums.length;\n    const MOD = (1n << 61n)\
        \ - 1n;\n    const BASE = 100019n;\n\n    const modPow = (base, exp, mod) =>\
        \ {\n        let res = 1n;\n        base %= mod;\n        while (exp > 0n) {\n\
        \            if (exp % 2n === 1n) res = (res * base) % mod;\n            base\
        \ = (base * base) % mod;\n            exp /= 2n;\n        }\n        return\
        \ res;\n    };\n\n    const check = (length) => {\n        if (length <= 0)\
        \ return false;\n        let P = modPow(BASE, BigInt(length - 1), MOD);\n  \
        \      let h = 0n;\n        for (let i = 0; i < length; i++) {\n           \
        \ h = (h * BASE + BigInt(nums[i])) % MOD;\n        }\n        let numHashes\
        \ = n - length + 1;\n        let hashes = new BigUint64Array(numHashes);\n \
        \       hashes[0] = h;\n        for (let i = length; i < n; i++) {\n       \
        \     let pTerm = (BigInt(nums[i - length]) * P) % MOD;\n            h = ((h\
        \ + MOD - pTerm) * BASE + BigInt(nums[i])) % MOD;\n            hashes[i - length\
        \ + 1] = h;\n        }\n        hashes.sort();\n        for (let i = 0; i <\
        \ numHashes; i++) {\n            if ((i === 0 || hashes[i] !== hashes[i - 1])\
        \ && \n                (i === numHashes - 1 || hashes[i] !== hashes[i + 1]))\
        \ {\n                return true;\n            }\n        }\n        return\
        \ false;\n    };\n\n    let low = 1, high = n, ans = n;\n    while (low <= high)\
        \ {\n        let mid = Math.floor((low + high) / 2);\n        if (check(mid))\
        \ {\n            ans = mid;\n            high = mid - 1;\n        } else {\n\
        \            low = mid + 1;\n        }\n    }\n    return ans;\n};"
      typescript: "function smallestUniqueSubarray(nums: number[]): number {\n    const\
        \ n = nums.length;\n    const MOD = (1n << 61n) - 1n;\n    const BASE = 100019n;\n\
        \n    function check(len: number): boolean {\n        if (len <= 0) return false;\n\
        \        let p = 1n;\n        for (let i = 0; i < len - 1; i++) {\n        \
        \    p = (p * BASE) % MOD;\n        }\n\n        let h = 0n;\n        for (let\
        \ i = 0; i < len; i++) {\n            h = (h * BASE + BigInt(nums[i])) % MOD;\n\
        \        }\n\n        const numHashes = n - len + 1;\n        const hashes =\
        \ new BigUint64Array(numHashes);\n        hashes[0] = h;\n        for (let i\
        \ = len; i < n; i++) {\n            let term = (BigInt(nums[i - len]) * p) %\
        \ MOD;\n            h = (h - term + MOD) % MOD;\n            h = (h * BASE +\
        \ BigInt(nums[i])) % MOD;\n            hashes[i - len + 1] = h;\n        }\n\
        \n        hashes.sort();\n        for (let i = 0; i < numHashes; i++) {\n  \
        \          if ((i === 0 || hashes[i] !== hashes[i - 1]) &&\n               \
        \ (i === numHashes - 1 || hashes[i] !== hashes[i + 1])) {\n                return\
        \ true;\n            }\n        }\n        return false;\n    }\n\n    let low\
        \ = 1, high = n, ans = n;\n    while (low <= high) {\n        let mid = Math.floor((low\
        \ + high) / 2);\n        if (check(mid)) {\n            ans = mid;\n       \
        \     high = mid - 1;\n        } else {\n            low = mid + 1;\n      \
        \  }\n    }\n    return ans;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function smallestUniqueSubarray($nums) {\n        $n\
        \ = count($nums);\n        $low = 1;\n        $high = $n;\n        $ans = $n;\n\
        \n        while ($low <= $high) {\n            $mid = (int)(($low + $high) /\
        \ 2);\n            if ($this->check($nums, $mid, $n)) {\n                $ans\
        \ = $mid;\n                $high = $mid - 1;\n            } else {\n       \
        \         $low = $mid + 1;\n            }\n        }\n        return $ans;\n\
        \    }\n\n    private function check($nums, $len, $n) {\n        $m1 = 1000000007;\n\
        \        $m2 = 1000000009;\n        $b = 100019;\n\n        $p1 = 1;\n     \
        \   $p2 = 1;\n        for ($i = 0; $i < $len - 1; $i++) {\n            $p1 =\
        \ ($p1 * $b) % $m1;\n            $p2 = ($p2 * $b) % $m2;\n        }\n\n    \
        \    $h1 = 0;\n        $h2 = 0;\n        for ($i = 0; $i < $len; $i++) {\n \
        \           $h1 = ($h1 * $b + $nums[$i]) % $m1;\n            $h2 = ($h2 * $b\
        \ + $nums[$i]) % $m2;\n        }\n\n        $hashes = [];\n        $hashes[]\
        \ = ($h1 << 32) | $h2;\n\n        for ($i = $len; $i < $n; $i++) {\n       \
        \     $h1 = ($h1 - ($nums[$i - $len] * $p1) % $m1 + $m1) % $m1;\n          \
        \  $h1 = ($h1 * $b + $nums[$i]) % $m1;\n            $h2 = ($h2 - ($nums[$i -\
        \ $len] * $p2) % $m2 + $m2) % $m2;\n            $h2 = ($h2 * $b + $nums[$i])\
        \ % $m2;\n            $hashes[] = ($h1 << 32) | $h2;\n        }\n\n        sort($hashes);\n\
        \        $numHashes = count($hashes);\n        for ($i = 0; $i < $numHashes;\
        \ $i++) {\n            if (($i == 0 || $hashes[$i] != $hashes[$i - 1]) &&\n\
        \                ($i == $numHashes - 1 || $hashes[$i] != $hashes[$i + 1])) {\n\
        \                return true;\n            }\n        }\n        return false;\n\
        \    }\n}"
      swift: "class Solution {\n    func smallestUniqueSubarray(_ nums: [Int]) -> Int\
        \ {\n        let n = nums.count\n        var low = 1\n        var high = n\n\
        \        var ans = n\n\n        func check(_ length: Int) -> Bool {\n      \
        \      let m1: Int64 = 1000000007\n            let m2: Int64 = 1000000009\n\
        \            let b: Int64 = 100019\n\n            var p1: Int64 = 1\n      \
        \      var p2: Int64 = 1\n            for _ in 0..<(length - 1) {\n        \
        \        p1 = (p1 * b) % m1\n                p2 = (p2 * b) % m2\n          \
        \  }\n\n            var h1: Int64 = 0\n            var h2: Int64 = 0\n     \
        \       for i in 0..<length {\n                h1 = (h1 * b + Int64(nums[i]))\
        \ % m1\n                h2 = (h2 * b + Int64(nums[i])) % m2\n            }\n\
        \n            let numHashes = n - length + 1\n            var hashes = [Int64](repeating:\
        \ 0, count: numHashes)\n            hashes[0] = (h1 << 32) | h2\n\n        \
        \    if n > length {\n                for i in length..<n {\n              \
        \      h1 = (h1 - (Int64(nums[i - length]) * p1) % m1 + m1) % m1\n         \
        \           h1 = (h1 * b + Int64(nums[i])) % m1\n                    h2 = (h2\
        \ - (Int64(nums[i - length]) * p2) % m2 + m2) % m2\n                    h2 =\
        \ (h2 * b + Int64(nums[i])) % m2\n                    hashes[i - length + 1]\
        \ = (h1 << 32) | h2\n                }\n            }\n\n            hashes.sort()\n\
        \            for i in 0..<numHashes {\n                if (i == 0 || hashes[i]\
        \ != hashes[i - 1]) &&\n                   (i == numHashes - 1 || hashes[i]\
        \ != hashes[i + 1]) {\n                    return true\n                }\n\
        \            }\n            return false\n        }\n\n        while low <=\
        \ high {\n            let mid = (low + high) / 2\n            if check(mid)\
        \ {\n                ans = mid\n                high = mid - 1\n           \
        \ } else {\n                low = mid + 1\n            }\n        }\n      \
        \  return ans\n    }\n}"
      kotlin: "class Solution {\n    fun smallestUniqueSubarray(nums: IntArray): Int\
        \ {\n        val n = nums.size\n        var low = 1\n        var high = n\n\
        \        var ans = n\n\n        fun check(len: Int): Boolean {\n           \
        \ val m1 = 1000000007L\n            val m2 = 1000000009L\n            val b\
        \ = 100019L\n\n            var p1 = 1L\n            var p2 = 1L\n          \
        \  for (i in 0 until len - 1) {\n                p1 = (p1 * b) % m1\n      \
        \          p2 = (p2 * b) % m2\n            }\n\n            var h1 = 0L\n  \
        \          var h2 = 0L\n            for (i in 0 until len) {\n             \
        \   h1 = (h1 * b + nums[i].toLong()) % m1\n                h2 = (h2 * b + nums[i].toLong())\
        \ % m2\n            }\n\n            val numHashes = n - len + 1\n         \
        \   val hashes = LongArray(numHashes)\n            hashes[0] = (h1 shl 32) or\
        \ h2\n\n            for (i in len until n) {\n                h1 = (h1 - (nums[i\
        \ - len].toLong() * p1) % m1 + m1) % m1\n                h1 = (h1 * b + nums[i].toLong())\
        \ % m1\n                h2 = (h2 - (nums[i - len].toLong() * p2) % m2 + m2)\
        \ % m2\n                h2 = (h2 * b + nums[i].toLong()) % m2\n            \
        \    hashes[i - len + 1] = (h1 shl 32) or h2\n            }\n\n            hashes.sort()\n\
        \            for (i in 0 until numHashes) {\n                if ((i == 0 ||\
        \ hashes[i] != hashes[i - 1]) &&\n                    (i == numHashes - 1 ||\
        \ hashes[i] != hashes[i + 1])) {\n                    return true\n        \
        \        }\n            }\n            return false\n        }\n\n        while\
        \ (low <= high) {\n            val mid = (low + high) / 2\n            if (check(mid))\
        \ {\n                ans = mid\n                high = mid - 1\n           \
        \ } else {\n                low = mid + 1\n            }\n        }\n      \
        \  return ans\n    }\n}"
      dart: "class Solution {\n  int smallestUniqueSubarray(List<int> nums) {\n    int\
        \ n = nums.length;\n    int low = 1, high = n, ans = n;\n    final BigInt mod\
        \ = (BigInt.from(1) << 61) - BigInt.from(1);\n    final BigInt base = BigInt.from(100019);\n\
        \n    bool check(int length) {\n      if (length <= 0) return false;\n     \
        \ BigInt p = base.modPow(BigInt.from(length - 1), mod);\n      BigInt h = BigInt.zero;\n\
        \      for (int i = 0; i < length; i++) {\n        h = (h * base + BigInt.from(nums[i]))\
        \ % mod;\n      }\n      int numHashes = n - length + 1;\n      List<BigInt>\
        \ hashes = List.filled(numHashes, BigInt.zero);\n      hashes[0] = h;\n    \
        \  for (int i = length; i < n; i++) {\n        BigInt sub = (BigInt.from(nums[i\
        \ - length]) * p) % mod;\n        h = ((h - sub + mod) % mod * base + BigInt.from(nums[i]))\
        \ % mod;\n        hashes[i - length + 1] = h;\n      }\n      hashes.sort();\n\
        \      for (int i = 0; i < numHashes; i++) {\n        if ((i == 0 || hashes[i]\
        \ != hashes[i - 1]) &&\n            (i == numHashes - 1 || hashes[i] != hashes[i\
        \ + 1])) {\n          return true;\n        }\n      }\n      return false;\n\
        \    }\n\n    while (low <= high) {\n      int mid = low + (high - low) ~/ 2;\n\
        \      if (check(mid)) {\n        ans = mid;\n        high = mid - 1;\n    \
        \  } else {\n        low = mid + 1;\n      }\n    }\n    return ans;\n  }\n}"
      go: "import (\n\t\"math/bits\"\n\t\"sort\"\n)\n\nfunc smallestUniqueSubarray(nums\
        \ []int) int {\n\tn := len(nums)\n\tlow, high, ans := 1, n, n\n\tconst mod uint64\
        \ = (1 << 61) - 1\n\tconst base uint64 = 100019\n\n\tmulMod := func(a, b uint64)\
        \ uint64 {\n\t\thi, lo := bits.Mul64(a, b)\n\t\tres := (hi << 3) + (lo >> 61)\
        \ + (lo & mod)\n\t\tres = (res >> 61) + (res & mod)\n\t\tif res >= mod {\n\t\
        \t\tres -= mod\n\t\t}\n\t\treturn res\n\t}\n\n\tpowMod := func(a, b uint64)\
        \ uint64 {\n\t\tres := uint64(1)\n\t\ta %= mod\n\t\tfor b > 0 {\n\t\t\tif b%2\
        \ == 1 {\n\t\t\t\tres = mulMod(res, a)\n\t\t\t}\n\t\t\ta = mulMod(a, a)\n\t\t\
        \tb /= 2\n\t\t}\n\t\treturn res\n\t}\n\n\tcheck := func(length int) bool {\n\
        \t\tif length <= 0 {\n\t\t\treturn false\n\t\t}\n\t\tp := powMod(base, uint64(length-1))\n\
        \t\tvar h uint64\n\t\tfor i := 0; i < length; i++ {\n\t\t\th = (mulMod(h, base)\
        \ + uint64(nums[i])) % mod\n\t\t}\n\n\t\tnumHashes := n - length + 1\n\t\thashes\
        \ := make([]uint64, numHashes)\n\t\thashes[0] = h\n\t\tfor i := length; i <\
        \ n; i++ {\n\t\t\tsub := mulMod(uint64(nums[i-length]), p)\n\t\t\tvar nextH\
        \ uint64\n\t\t\tif h < sub {\n\t\t\t\tnextH = h + mod - sub\n\t\t\t} else {\n\
        \t\t\t\tnextH = h - sub\n\t\t\t}\n\t\t\th = (mulMod(nextH, base) + uint64(nums[i]))\
        \ % mod\n\t\t\thashes[i-length+1] = h\n\t\t}\n\n\t\tsort.Uint64s(hashes)\n\t\
        \tfor i := 0; i < numHashes; i++ {\n\t\t\tif (i == 0 || hashes[i] != hashes[i-1])\
        \ &&\n\t\t\t\t(i == numHashes-1 || hashes[i] != hashes[i+1]) {\n\t\t\t\treturn\
        \ true\n\t\t\t}\n\t\t}\n\t\treturn false\n\t}\n\n\tfor low <= high {\n\t\tmid\
        \ := (low + high) / 2\n\t\tif check(mid) {\n\t\t\tans = mid\n\t\t\thigh = mid\
        \ - 1\n\t\t} else {\n\t\t\tlow = mid + 1\n\t\t}\n\t}\n\treturn ans\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef smallest_unique_subarray(nums)\n\
        \  n = nums.length\n  low, high, ans = 1, n, n\n  mod = (1 << 61) - 1\n  base\
        \ = 100019\n\n  check = lambda do |length|\n    return false if length <= 0\n\
        \    p = base.pow(length - 1, mod)\n    h = 0\n    (0...length).each { |i| h\
        \ = (h * base + nums[i]) % mod }\n\n    num_hashes = n - length + 1\n    hashes\
        \ = Array.new(num_hashes)\n    hashes[0] = h\n    (length...n).each do |i|\n\
        \      sub = (nums[i - length] * p) % mod\n      h = ((h - sub + mod) % mod\
        \ * base + nums[i]) % mod\n      hashes[i - length + 1] = h\n    end\n\n   \
        \ hashes.sort!\n    (0...num_hashes).each do |i|\n      if (i == 0 || hashes[i]\
        \ != hashes[i - 1]) && (i == num_hashes - 1 || hashes[i] != hashes[i + 1])\n\
        \        return true\n      end\n    end\n    false\n  end\n\n  while low <=\
        \ high\n    mid = (low + high) / 2\n    if check.call(mid)\n      ans = mid\n\
        \      high = mid - 1\n    else\n      low = mid + 1\n    end\n  end\n  ans\n\
        end"
      scala: "import java.util.Arrays\n\nobject Solution {\n    def smallestUniqueSubarray(nums:\
        \ Array[Int]): Int = {\n        val n = nums.length\n        var low = 1\n \
        \       var high = n\n        var ans = n\n        val MOD = (BigInt(1) << 61)\
        \ - 1\n        val BASE = BigInt(100019)\n\n        def check(length: Int):\
        \ Boolean = {\n            if (length <= 0) return false\n            val P\
        \ = BASE.modPow(BigInt(length - 1), MOD)\n            var h = BigInt(0)\n  \
        \          for (i <- 0 until length) {\n                h = (h * BASE + BigInt(nums(i)))\
        \ % MOD\n            }\n            val numHashes = n - length + 1\n       \
        \     val hashes = new Array[Long](numHashes)\n            hashes(0) = h.toLong\n\
        \            for (i <- length until n) {\n                val sub = (BigInt(nums(i\
        \ - length)) * P) % MOD\n                h = ((h - sub + MOD) % MOD * BASE +\
        \ BigInt(nums(i))) % MOD\n                hashes(i - length + 1) = h.toLong\n\
        \            }\n            Arrays.sort(hashes)\n            for (i <- 0 until\
        \ numHashes) {\n                if ((i == 0 || hashes(i) != hashes(i - 1)) &&\
        \ (i == numHashes - 1 || hashes(i) != hashes(i + 1))) {\n                  \
        \  return true\n                }\n            }\n            false\n      \
        \  }\n\n        while (low <= high) {\n            val mid = (low + high) /\
        \ 2\n            if (check(mid)) {\n                ans = mid\n            \
        \    high = mid - 1\n            } else {\n                low = mid + 1\n \
        \           }\n        }\n        ans\n    }\n}"
      rust: "impl Solution {\n    pub fn smallest_unique_subarray(nums: Vec<i32>) ->\
        \ i32 {\n        let n = nums.len();\n        let mut low = 1;\n        let\
        \ mut high = n;\n        let mut ans = n;\n        let mod_val: u64 = (1u64\
        \ << 61) - 1;\n        let base: u64 = 100019;\n\n        while low <= high\
        \ {\n            let mid = low + (high - low) / 2;\n            if Self::check(mid,\
        \ &nums, mod_val, base) {\n                ans = mid;\n                high\
        \ = mid - 1;\n            } else {\n                low = mid + 1;\n       \
        \     }\n        }\n        ans as i32\n    }\n\n    fn check(length: usize,\
        \ nums: &[i32], mod_val: u64, base: u64) -> bool {\n        if length == 0 {\n\
        \            return false;\n        }\n        let n = nums.len();\n       \
        \ let mut p: u64 = 1;\n        for _ in 0..length - 1 {\n            p = ((p\
        \ as u128 * base as u128) % mod_val as u128) as u64;\n        }\n\n        let\
        \ mut h: u64 = 0;\n        for i in 0..length {\n            h = ((h as u128\
        \ * base as u128 + nums[i] as u128) % mod_val as u128) as u64;\n        }\n\n\
        \        let num_hashes = n - length + 1;\n        let mut hashes = Vec::with_capacity(num_hashes);\n\
        \        hashes.push(h);\n\n        for i in length..n {\n            let term\
        \ = (nums[i - length] as u128 * p as u128) % mod_val as u128;\n            h\
        \ = (((h as u128 + mod_val as u128 - term) % mod_val as u128 * base as u128\
        \ + nums[i] as u128) % mod_val as u128) as u64;\n            hashes.push(h);\n\
        \        }\n\n        hashes.sort_unstable();\n        for i in 0..num_hashes\
        \ {\n            if (i == 0 || hashes[i] != hashes[i - 1]) && (i == num_hashes\
        \ - 1 || hashes[i] != hashes[i + 1]) {\n                return true;\n     \
        \       }\n        }\n        false\n    }\n}"
      racket: "(define/contract (smallest-unique-subarray nums)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let* ((n (length nums))\n         (vec (list->vector nums))\n\
        \         (m (- (expt 2 61) 1))\n         (base 100019))\n    (define (pow-mod\
        \ b e m)\n      (let loop ((b b) (e e) (res 1))\n        (cond\n          [(=\
        \ e 0) res]\n          [(even? e) (loop (remainder (* b b) m) (quotient e 2)\
        \ res)]\n          [else (loop (remainder (* b b) m) (quotient e 2) (remainder\
        \ (* res b) m))])))\n    (define (check len)\n      (if (<= len 0) #f\n    \
        \      (let* ([p (pow-mod base (- len 1) m)]\n                 [h-start (for/fold\
        \ ([h 0]) ([i (in-range len)])\n                            (remainder (+ (*\
        \ h base) (vector-ref vec i)) m))])\n            (let-values ([(last-h all-hashes)\n\
        \                          (for/fold ([h h-start] [acc (list h-start)])\n  \
        \                                  ([i (in-range len n)])\n                \
        \            (let* ([term (remainder (* (vector-ref vec (- i len)) p) m)]\n\
        \                                   [h-next (remainder (+ (* (remainder (+ (-\
        \ h term) m) m) base) (vector-ref vec i)) m)])\n                           \
        \   (values h-next (cons h-next acc))))])\n              (let ([sorted (sort\
        \ all-hashes <)])\n                (let loop-find ([lst sorted] [prev -1])\n\
        \                  (cond\n                    [(null? lst) #f]\n           \
        \         [(and (not (= (car lst) prev))\n                          (or (null?\
        \ (cdr lst)) (not (= (car lst) (cadr lst))))) #t]\n                    [else\
        \ (loop-find (cdr lst) (car lst))])))))))\n    (let loop-bs ([low 1] [high n]\
        \ [ans n])\n      (if (<= low high)\n          (let ([mid (quotient (+ low high)\
        \ 2)])\n            (if (check mid)\n                (loop-bs low (- mid 1)\
        \ mid)\n                (loop-bs (+ mid 1) high ans)))\n          ans))))"
      erlang: "-spec smallest_unique_subarray(Nums :: [integer()]) -> integer().\nsmallest_unique_subarray(Nums)\
        \ ->\n    N = length(Nums),\n    Arr = list_to_tuple(Nums),\n    Mod = (1 bsl\
        \ 61) - 1,\n    Base = 100019,\n    bs(1, N, N, Arr, N, Mod, Base).\n\nbs(Low,\
        \ High, Ans, Arr, N, Mod, Base) ->\n    if Low > High -> Ans;\n       true ->\n\
        \           Mid = (Low + High) div 2,\n           case check(Mid, Arr, N, Mod,\
        \ Base) of\n               true -> bs(Low, Mid - 1, Mid, Arr, N, Mod, Base);\n\
        \               false -> bs(Mid + 1, High, Ans, Arr, N, Mod, Base)\n       \
        \    end\n    end.\n\ncheck(Len, Arr, N, Mod, Base) ->\n    if Len =< 0 -> false;\n\
        \       true ->\n           P = pow_mod(Base, Len - 1, Mod),\n           H0\
        \ = calculate_initial_hash(Len, Arr, Base, Mod),\n           Hashes = calculate_all_hashes(Len,\
        \ Arr, N, Mod, Base, P, H0),\n           SortedHashes = lists:sort(Hashes),\n\
        \           has_unique_rec(SortedHashes, -1)\n    end.\n\npow_mod(_B, 0, _M)\
        \ -> 1;\npow_mod(B, E, M) ->\n    Half = E div 2,\n    Res = pow_mod(B, Half,\
        \ M),\n    Res2 = (Res * Res) rem M,\n    if E rem 2 == 0 -> Res2;\n       true\
        \ -> (Res2 * B) rem M\n    end.\n\ncalculate_initial_hash(Len, Arr, Base, Mod)\
        \ ->\n    calculate_initial_hash_rec(1, Len, Arr, Base, Mod, 0).\n\ncalculate_initial_hash_rec(I,\
        \ Len, Arr, Base, Mod, H) when I =< Len ->\n    calculate_initial_hash_rec(I\
        \ + 1, Len, Arr, Base, Mod, (H * Base + element(I, Arr)) rem Mod);\ncalculate_initial_hash_rec(_I,\
        \ _Len, _Arr, _Base, _Mod, H) -> H.\n\ncalculate_all_hashes(Len, Arr, N, Mod,\
        \ Base, P, H0) ->\n    calculate_all_hashes_rec(Len + 1, Arr, N, Mod, Base,\
        \ P, H0, Len, [H0]).\n\ncalculate_all_hashes_rec(I, Arr, N, Mod, Base, P, H,\
        \ Len, Acc) when I =< N ->\n    Term = (element(I - Len, Arr) * P) rem Mod,\n\
        \    HNext = (((H + Mod - Term) rem Mod) * Base + element(I, Arr)) rem Mod,\n\
        \    calculate_all_hashes_rec(I + 1, Arr, N, Mod, Base, P, HNext, Len, [HNext\
        \ | Acc]);\ncalculate_all_hashes_rec(_I, _Arr, _N, _Mod, _Base, _P, _H, _Len,\
        \ Acc) -> Acc.\n\nhas_unique_rec([], _Prev) -> false;\nhas_unique_rec([H], Prev)\
        \ -> H /= Prev;\nhas_unique_rec([H1, H2 | T], Prev) ->\n    if (H1 /= Prev)\
        \ and (H1 /= H2) -> true;\n       true -> has_unique_rec([H2 | T], H1)\n   \
        \ end."
      elixir: "defmodule Solution do\n  @spec smallest_unique_subarray(nums :: [integer])\
        \ :: integer\n  def smallest_unique_subarray(nums) do\n    n = length(nums)\n\
        \    arr = List.to_tuple(nums)\n    mod_val = Bitwise.bsl(1, 61) - 1\n    base\
        \ = 100019\n    binary_search(1, n, n, arr, n, mod_val, base)\n  end\n\n  defp\
        \ binary_search(low, high, ans, arr, n, mod_val, base) do\n    if low > high\
        \ do\n      ans\n    else\n      mid = div(low + high, 2)\n      if check(mid,\
        \ arr, n, mod_val, base) do\n        binary_search(low, mid - 1, mid, arr, n,\
        \ mod_val, base)\n      else\n        binary_search(mid + 1, high, ans, arr,\
        \ n, mod_val, base)\n      end\n    end\n  end\n\n  defp check(len, arr, n,\
        \ mod_val, base) do\n    if len <= 0 do\n      false\n    else\n      p = pow_mod(base,\
        \ len - 1, mod_val)\n      h0 = calculate_initial_hash(len, arr, base, mod_val)\n\
        \      hashes = calculate_all_hashes(len, arr, n, mod_val, base, p, h0)\n  \
        \    sorted_hashes = Enum.sort(hashes)\n      has_unique?(sorted_hashes, -1)\n\
        \    end\n  end\n\n  defp pow_mod(_base, 0, _m), do: 1\n  defp pow_mod(base,\
        \ exp, m) do\n    half = pow_mod(base, div(exp, 2), m)\n    res = rem(half *\
        \ half, m)\n    if rem(exp, 2) == 0 do\n      res\n    else\n      rem(res *\
        \ base, m)\n    end\n  end\n\n  defp calculate_initial_hash(len, arr, base,\
        \ mod_val) do\n    Enum.reduce(0..(len - 1), 0, fn i, acc ->\n      rem(acc\
        \ * base + elem(arr, i), mod_val)\n    end)\n  end\n\n  defp calculate_all_hashes(len,\
        \ arr, n, mod_val, base, p, h0) do\n    if len >= n do\n      [h0]\n    else\n\
        \      calculate_all_hashes_rec(len, arr, n, mod_val, base, p, h0, len, [h0])\n\
        \    end\n  end\n\n  defp calculate_all_hashes_rec(i, arr, n, mod_val, base,\
        \ p, h, len, acc) when i < n do\n    term = rem(elem(arr, i - len) * p, mod_val)\n\
        \    h_next = rem(rem(h + mod_val - term, mod_val) * base + elem(arr, i), mod_val)\n\
        \    calculate_all_hashes_rec(i + 1, arr, n, mod_val, base, p, h_next, len,\
        \ [h_next | acc])\n  end\n  defp calculate_all_hashes_rec(_i, _arr, _n, _mod_val,\
        \ _base, _p, _h, _len, acc), do: acc\n\n  defp has_unique?([], _prev), do: false\n\
        \  defp has_unique?([h], prev), do: h != prev\n  defp has_unique?([h1, h2 |\
        \ t], prev) do\n    if h1 != prev and h1 != h2 do\n      true\n    else\n  \
        \    has_unique?([h2 | t], h1)\n    end\n  end\nend"
    approach: 'The problem asks for the minimum length of a subarray that appears exactly
      once in the given array. We observe that the property of ''having at least one
      unique subarray of length L'' is monotonic: if a unique subarray of length L exists,
      then any subarray of length L+1 containing it must also be unique. This allows
      us to use binary search to find the smallest length L in the range [1, N].'
    time_complexity: O(N \log^2 N). Each step of the binary search (which runs $O(\log
      N)$ times) involves computing rolling hashes for all subarrays of the current
      length in $O(N)$ time, followed by sorting these hashes in $O(N \log N)$ time
      to identify unique occurrences. For $N = 10^5$, this results in approximately
      $3 \times 10^7$ operations, fitting within the standard time limit.
    space_complexity: O(N). We store $O(N)$ rolling hash values in an array/list during
      each step of the binary search, and precompute hash constants and powers, which
      all consume linear space.
    elapsed_time: 620.7726216316223
    model: gemini-3-flash-preview
    generated_at: '2026-11-25 06:31:45 '
---

## Problem #3934: Smallest Unique Subarray

**Difficulty:** Hard

**Topics:** Array, Hash Table, Binary Search, Rolling Hash, Suffix Array, Hash Function

## Problem Description

<p>You are given an integer array <code>nums</code>.</p>

<p>Find the <strong>minimum </strong>length of a <span data-keyword="subarray">subarray</span> that is <strong>not</strong> <strong>identical</strong> to any other <strong>subarray</strong> in <code>nums</code>.</p>

<p>Return an integer denoting the <strong>minimum possible length</strong> of such a <strong>subarray</strong>.</p>

<p>Two <strong>subarrays</strong> are considered identical if they have the same length and the same elements in corresponding positions.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,3,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Subarrays of length 1: <code>[3]</code> &rarr; appears 3 times</li>
	<li>Subarrays of length 2: <code>[3, 3]</code> &rarr; appears 2 times</li>
	<li>Subarrays of length 3: <code>[3, 3, 3]</code> &rarr; appears once</li>
</ul>

<p>The subarray <code>[3, 3, 3]</code> is unique, so the smallest unique subarray length is 3.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,1,2,3,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>Subarrays of length 1:</p>

<ul>
	<li><code>[2]</code> &rarr; appears 2 times</li>
	<li><code>[1]</code> &rarr; appears once</li>
	<li><code>[3]</code> &rarr; appears 2 times</li>
</ul>
The subarray <code>[1]</code> is unique, so the smallest unique subarray length is 1.</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,2,2,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>Subarrays of length 1:</p>

<ul>
	<li><code>[1]</code> &rarr; appears 3 times</li>
	<li><code>[2]</code> &rarr; appears 2 times</li>
</ul>

<p>Subarrays of length 2:</p>

<ul>
	<li><code>[1, 1]</code> &rarr; appears once</li>
	<li><code>[1, 2]</code> &rarr; appears once</li>
	<li><code>[2, 2]</code> &rarr; appears once</li>
	<li><code>[2, 1]</code> &rarr; appears once</li>
</ul>
There is at least one subarray of length 2 that is unique, so the smallest unique subarray length is 2.</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. Think in terms of checking a fixed length `len`: count all subarrays of length `len`, and see whether any one appears exactly once.

2. Use rolling hash so each subarray can be represented in `O(1)` after preprocessing, instead of comparing arrays directly.

3. The answer can be binary searched because if there is a unique subarray of length `len`, then there is also a unique subarray of some length `> len`.

4. For each checked length, store frequencies of hashes in a hashmap. If any hash has frequency 1, that length works.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the minimum length of a subarray that appears exactly once in the given array. We observe that the property of 'having at least one unique subarray of length L' is monotonic: if a unique subarray of length L exists, then any subarray of length L+1 containing it must also be unique. This allows us to use binary search to find the smallest length L in the range [1, N].

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
#include <cstdint>

using namespace std;

class Solution {
public:
    int smallestUniqueSubarray(vector<int>& nums) {
        int n = nums.size();
        int low = 1, high = n, ans = n;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (check(mid, n, nums)) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }

private:
    bool check(int len, int n, const vector<int>& nums) {
        if (len <= 0) return false;
        long long mod1 = 1000000007LL;
        long long mod2 = 1000000009LL;
        long long base1 = 100019LL;
        long long base2 = 100043LL;
        long long h1 = 0, h2 = 0;
        long long p1 = 1, p2 = 1;

        for (int i = 0; i < len; ++i) {
            h1 = (h1 * base1 + nums[i]) % mod1;
            h2 = (h2 * base2 + nums[i]) % mod2;
            if (i > 0) {
                p1 = (p1 * base1) % mod1;
                p2 = (p2 * base2) % mod2;
            }
        }

        vector<uint64_t> hashes;
        hashes.reserve(n - len + 1);
        hashes.push_back(((uint64_t)h1 << 32) | (uint64_t)h2);

        for (int i = len; i < n; ++i) {
            h1 = (h1 - nums[i - len] * p1 % mod1 + mod1) % mod1;
            h1 = (h1 * base1 + nums[i]) % mod1;
            h2 = (h2 - nums[i - len] * p2 % mod2 + mod2) % mod2;
            h2 = (h2 * base2 + nums[i]) % mod2;
            hashes.push_back(((uint64_t)h1 << 32) | (uint64_t)h2);
        }

        sort(hashes.begin(), hashes.end());

        for (size_t i = 0; i < hashes.size(); ++i) {
            if ((i == 0 || hashes[i] != hashes[i - 1]) &&
                (i == hashes.size() - 1 || hashes[i] != hashes[i + 1])) {
                return true;
            }
        }
        return false;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.Arrays;

class Solution {
    public int smallestUniqueSubarray(int[] nums) {
        int n = nums.length;
        int low = 1, high = n, ans = n;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (check(mid, n, nums)) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }

    private boolean check(int len, int n, int[] nums) {
        long mod1 = 1000000007L;
        long mod2 = 1000000009L;
        long base1 = 100019L;
        long base2 = 100043L;
        long h1 = 0, h2 = 0;
        long p1 = 1, p2 = 1;

        for (int i = 0; i < len; i++) {
            h1 = (h1 * base1 + nums[i]) % mod1;
            h2 = (h2 * base2 + nums[i]) % mod2;
            if (i > 0) {
                p1 = (p1 * base1) % mod1;
                p2 = (p2 * base2) % mod2;
            }
        }

        long[] hashes = new long[n - len + 1];
        hashes[0] = ((long) h1 << 32) | (h2 & 0xFFFFFFFFL);

        for (int i = len; i < n; i++) {
            h1 = (h1 - (nums[i - len] * p1) % mod1 + mod1) % mod1;
            h1 = (h1 * base1 + nums[i]) % mod1;
            h2 = (h2 - (nums[i - len] * p2) % mod2 + mod2) % mod2;
            h2 = (h2 * base2 + nums[i]) % mod2;
            hashes[i - len + 1] = ((long) h1 << 32) | (h2 & 0xFFFFFFFFL);
        }

        Arrays.sort(hashes);

        for (int i = 0; i < hashes.length; i++) {
            if ((i == 0 || hashes[i] != hashes[i - 1]) &&
                (i == hashes.length - 1 || hashes[i] != hashes[i + 1])) {
                return true;
            }
        }
        return false;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def smallestUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        low, high, ans = 1, n, n

        def check(length):
            if length <= 0:
                return False
            MOD = (1 << 61) - 1
            BASE = 100019
            P = pow(BASE, length - 1, MOD)
            h = 0
            for i in range(length):
                h = (h * BASE + nums[i]) % MOD

            hashes = [h]
            for i in range(length, n):
                h = ((h - nums[i-length] * P) * BASE + nums[i]) % MOD
                hashes.append(h)

            hashes.sort()
            for i in range(len(hashes)):
                if (i == 0 or hashes[i] != hashes[i-1]) and \
                   (i == len(hashes) - 1 or hashes[i] != hashes[i+1]):
                    return True
            return False

        while low <= high:
            mid = (low + high) // 2
            if check(mid):
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

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        low, high, ans = 1, n, n

        def check(length: int) -> bool:
            if length <= 0:
                return False
            MOD = (1 << 61) - 1
            BASE = 100019
            P = pow(BASE, length - 1, MOD)
            h = 0
            for i in range(length):
                h = (h * BASE + nums[i]) % MOD

            num_hashes = n - length + 1
            hashes = [0] * num_hashes
            hashes[0] = h
            for i in range(length, n):
                h = ((h - nums[i - length] * P) * BASE + nums[i]) % MOD
                hashes[i - length + 1] = h

            hashes.sort()
            for i in range(num_hashes):
                if (i == 0 or hashes[i] != hashes[i - 1]) and \
                   (i == num_hashes - 1 or hashes[i] != hashes[i + 1]):
                    return True
            return False

        while low <= high:
            mid = (low + high) // 2
            if check(mid):
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
#include <stdint.h>

typedef unsigned long long ull;
typedef __uint128_t u128;

static ull mul_mod(ull a, ull b) {
    ull mod = (1ULL << 61) - 1;
    u128 res = (u128)a * b;
    ull ans = (ull)(res >> 61) + (ull)(res & mod);
    if (ans >= mod) ans -= mod;
    return ans;
}

static ull mod_pow(ull base, int exp) {
    ull res = 1;
    ull mod = (1ULL << 61) - 1;
    base %= mod;
    while (exp > 0) {
        if (exp % 2 == 1) res = mul_mod(res, base);
        base = mul_mod(base, base);
        exp /= 2;
    }
    return res;
}

static int compare(const void* a, const void* b) {
    ull val1 = *(ull*)a;
    ull val2 = *(ull*)b;
    if (val1 < val2) return -1;
    if (val1 > val2) return 1;
    return 0;
}

static int check(int length, int* nums, int numsSize) {
    if (length <= 0) return 0;
    ull mod = (1ULL << 61) - 1;
    ull base = 100019;
    ull p = mod_pow(base, length - 1);
    ull h = 0;
    for (int i = 0; i < length; i++) {
        h = (mul_mod(h, base) + (ull)nums[i]) % mod;
    }
    int num_hashes = numsSize - length + 1;
    ull* hashes = (ull*)malloc(num_hashes * sizeof(ull));
    hashes[0] = h;
    for (int i = length; i < numsSize; i++) {
        ull p_term = mul_mod((ull)nums[i - length], p);
        h = (h + mod - p_term) % mod;
        h = (mul_mod(h, base) + (ull)nums[i]) % mod;
        hashes[i - length + 1] = h;
    }
    qsort(hashes, num_hashes, sizeof(ull), compare);
    int found = 0;
    for (int i = 0; i < num_hashes; i++) {
        if ((i == 0 || hashes[i] != hashes[i - 1]) && 
            (i == num_hashes - 1 || hashes[i] != hashes[i + 1])) {
            found = 1;
            break;
        }
    }
    free(hashes);
    return found;
}

int smallestUniqueSubarray(int* nums, int numsSize) {
    int low = 1, high = numsSize, ans = numsSize;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (check(mid, nums, numsSize)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Numerics;

public class Solution {
    public int SmallestUniqueSubarray(int[] nums) {
        int n = nums.Length;
        int low = 1, high = n, ans = n;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (Check(mid, nums)) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }

    private bool Check(int length, int[] nums) {
        if (length <= 0) return false;
        int n = nums.Length;
        BigInteger MOD = (BigInteger.One << 61) - 1;
        BigInteger BASE = 100019;
        BigInteger P = BigInteger.ModPow(BASE, length - 1, MOD);
        BigInteger h = 0;
        for (int i = 0; i < length; i++) {
            h = (h * BASE + nums[i]) % MOD;
        }
        int numHashes = n - length + 1;
        ulong[] hashes = new ulong[numHashes];
        hashes[0] = (ulong)h;
        for (int i = length; i < n; i++) {
            h = ((h - (BigInteger)nums[i - length] * P % MOD + MOD) * BASE + nums[i]) % MOD;
            hashes[i - length + 1] = (ulong)h;
        }
        Array.Sort(hashes);
        for (int i = 0; i < numHashes; i++) {
            if ((i == 0 || hashes[i] != hashes[i - 1]) && 
                (i == numHashes - 1 || hashes[i] != hashes[i + 1])) {
                return true;
            }
        }
        return false;
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
var smallestUniqueSubarray = function(nums) {
    const n = nums.length;
    const MOD = (1n << 61n) - 1n;
    const BASE = 100019n;

    const modPow = (base, exp, mod) => {
        let res = 1n;
        base %= mod;
        while (exp > 0n) {
            if (exp % 2n === 1n) res = (res * base) % mod;
            base = (base * base) % mod;
            exp /= 2n;
        }
        return res;
    };

    const check = (length) => {
        if (length <= 0) return false;
        let P = modPow(BASE, BigInt(length - 1), MOD);
        let h = 0n;
        for (let i = 0; i < length; i++) {
            h = (h * BASE + BigInt(nums[i])) % MOD;
        }
        let numHashes = n - length + 1;
        let hashes = new BigUint64Array(numHashes);
        hashes[0] = h;
        for (let i = length; i < n; i++) {
            let pTerm = (BigInt(nums[i - length]) * P) % MOD;
            h = ((h + MOD - pTerm) * BASE + BigInt(nums[i])) % MOD;
            hashes[i - length + 1] = h;
        }
        hashes.sort();
        for (let i = 0; i < numHashes; i++) {
            if ((i === 0 || hashes[i] !== hashes[i - 1]) && 
                (i === numHashes - 1 || hashes[i] !== hashes[i + 1])) {
                return true;
            }
        }
        return false;
    };

    let low = 1, high = n, ans = n;
    while (low <= high) {
        let mid = Math.floor((low + high) / 2);
        if (check(mid)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function smallestUniqueSubarray(nums: number[]): number {
    const n = nums.length;
    const MOD = (1n << 61n) - 1n;
    const BASE = 100019n;

    function check(len: number): boolean {
        if (len <= 0) return false;
        let p = 1n;
        for (let i = 0; i < len - 1; i++) {
            p = (p * BASE) % MOD;
        }

        let h = 0n;
        for (let i = 0; i < len; i++) {
            h = (h * BASE + BigInt(nums[i])) % MOD;
        }

        const numHashes = n - len + 1;
        const hashes = new BigUint64Array(numHashes);
        hashes[0] = h;
        for (let i = len; i < n; i++) {
            let term = (BigInt(nums[i - len]) * p) % MOD;
            h = (h - term + MOD) % MOD;
            h = (h * BASE + BigInt(nums[i])) % MOD;
            hashes[i - len + 1] = h;
        }

        hashes.sort();
        for (let i = 0; i < numHashes; i++) {
            if ((i === 0 || hashes[i] !== hashes[i - 1]) &&
                (i === numHashes - 1 || hashes[i] !== hashes[i + 1])) {
                return true;
            }
        }
        return false;
    }

    let low = 1, high = n, ans = n;
    while (low <= high) {
        let mid = Math.floor((low + high) / 2);
        if (check(mid)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return ans;
};
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
    function smallestUniqueSubarray($nums) {
        $n = count($nums);
        $low = 1;
        $high = $n;
        $ans = $n;

        while ($low <= $high) {
            $mid = (int)(($low + $high) / 2);
            if ($this->check($nums, $mid, $n)) {
                $ans = $mid;
                $high = $mid - 1;
            } else {
                $low = $mid + 1;
            }
        }
        return $ans;
    }

    private function check($nums, $len, $n) {
        $m1 = 1000000007;
        $m2 = 1000000009;
        $b = 100019;

        $p1 = 1;
        $p2 = 1;
        for ($i = 0; $i < $len - 1; $i++) {
            $p1 = ($p1 * $b) % $m1;
            $p2 = ($p2 * $b) % $m2;
        }

        $h1 = 0;
        $h2 = 0;
        for ($i = 0; $i < $len; $i++) {
            $h1 = ($h1 * $b + $nums[$i]) % $m1;
            $h2 = ($h2 * $b + $nums[$i]) % $m2;
        }

        $hashes = [];
        $hashes[] = ($h1 << 32) | $h2;

        for ($i = $len; $i < $n; $i++) {
            $h1 = ($h1 - ($nums[$i - $len] * $p1) % $m1 + $m1) % $m1;
            $h1 = ($h1 * $b + $nums[$i]) % $m1;
            $h2 = ($h2 - ($nums[$i - $len] * $p2) % $m2 + $m2) % $m2;
            $h2 = ($h2 * $b + $nums[$i]) % $m2;
            $hashes[] = ($h1 << 32) | $h2;
        }

        sort($hashes);
        $numHashes = count($hashes);
        for ($i = 0; $i < $numHashes; $i++) {
            if (($i == 0 || $hashes[$i] != $hashes[$i - 1]) &&
                ($i == $numHashes - 1 || $hashes[$i] != $hashes[$i + 1])) {
                return true;
            }
        }
        return false;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func smallestUniqueSubarray(_ nums: [Int]) -> Int {
        let n = nums.count
        var low = 1
        var high = n
        var ans = n

        func check(_ length: Int) -> Bool {
            let m1: Int64 = 1000000007
            let m2: Int64 = 1000000009
            let b: Int64 = 100019

            var p1: Int64 = 1
            var p2: Int64 = 1
            for _ in 0..<(length - 1) {
                p1 = (p1 * b) % m1
                p2 = (p2 * b) % m2
            }

            var h1: Int64 = 0
            var h2: Int64 = 0
            for i in 0..<length {
                h1 = (h1 * b + Int64(nums[i])) % m1
                h2 = (h2 * b + Int64(nums[i])) % m2
            }

            let numHashes = n - length + 1
            var hashes = [Int64](repeating: 0, count: numHashes)
            hashes[0] = (h1 << 32) | h2

            if n > length {
                for i in length..<n {
                    h1 = (h1 - (Int64(nums[i - length]) * p1) % m1 + m1) % m1
                    h1 = (h1 * b + Int64(nums[i])) % m1
                    h2 = (h2 - (Int64(nums[i - length]) * p2) % m2 + m2) % m2
                    h2 = (h2 * b + Int64(nums[i])) % m2
                    hashes[i - length + 1] = (h1 << 32) | h2
                }
            }

            hashes.sort()
            for i in 0..<numHashes {
                if (i == 0 || hashes[i] != hashes[i - 1]) &&
                   (i == numHashes - 1 || hashes[i] != hashes[i + 1]) {
                    return true
                }
            }
            return false
        }

        while low <= high {
            let mid = (low + high) / 2
            if check(mid) {
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

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun smallestUniqueSubarray(nums: IntArray): Int {
        val n = nums.size
        var low = 1
        var high = n
        var ans = n

        fun check(len: Int): Boolean {
            val m1 = 1000000007L
            val m2 = 1000000009L
            val b = 100019L

            var p1 = 1L
            var p2 = 1L
            for (i in 0 until len - 1) {
                p1 = (p1 * b) % m1
                p2 = (p2 * b) % m2
            }

            var h1 = 0L
            var h2 = 0L
            for (i in 0 until len) {
                h1 = (h1 * b + nums[i].toLong()) % m1
                h2 = (h2 * b + nums[i].toLong()) % m2
            }

            val numHashes = n - len + 1
            val hashes = LongArray(numHashes)
            hashes[0] = (h1 shl 32) or h2

            for (i in len until n) {
                h1 = (h1 - (nums[i - len].toLong() * p1) % m1 + m1) % m1
                h1 = (h1 * b + nums[i].toLong()) % m1
                h2 = (h2 - (nums[i - len].toLong() * p2) % m2 + m2) % m2
                h2 = (h2 * b + nums[i].toLong()) % m2
                hashes[i - len + 1] = (h1 shl 32) or h2
            }

            hashes.sort()
            for (i in 0 until numHashes) {
                if ((i == 0 || hashes[i] != hashes[i - 1]) &&
                    (i == numHashes - 1 || hashes[i] != hashes[i + 1])) {
                    return true
                }
            }
            return false
        }

        while (low <= high) {
            val mid = (low + high) / 2
            if (check(mid)) {
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
  int smallestUniqueSubarray(List<int> nums) {
    int n = nums.length;
    int low = 1, high = n, ans = n;
    final BigInt mod = (BigInt.from(1) << 61) - BigInt.from(1);
    final BigInt base = BigInt.from(100019);

    bool check(int length) {
      if (length <= 0) return false;
      BigInt p = base.modPow(BigInt.from(length - 1), mod);
      BigInt h = BigInt.zero;
      for (int i = 0; i < length; i++) {
        h = (h * base + BigInt.from(nums[i])) % mod;
      }
      int numHashes = n - length + 1;
      List<BigInt> hashes = List.filled(numHashes, BigInt.zero);
      hashes[0] = h;
      for (int i = length; i < n; i++) {
        BigInt sub = (BigInt.from(nums[i - length]) * p) % mod;
        h = ((h - sub + mod) % mod * base + BigInt.from(nums[i])) % mod;
        hashes[i - length + 1] = h;
      }
      hashes.sort();
      for (int i = 0; i < numHashes; i++) {
        if ((i == 0 || hashes[i] != hashes[i - 1]) &&
            (i == numHashes - 1 || hashes[i] != hashes[i + 1])) {
          return true;
        }
      }
      return false;
    }

    while (low <= high) {
      int mid = low + (high - low) ~/ 2;
      if (check(mid)) {
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
import (
	"math/bits"
	"sort"
)

func smallestUniqueSubarray(nums []int) int {
	n := len(nums)
	low, high, ans := 1, n, n
	const mod uint64 = (1 << 61) - 1
	const base uint64 = 100019

	mulMod := func(a, b uint64) uint64 {
		hi, lo := bits.Mul64(a, b)
		res := (hi << 3) + (lo >> 61) + (lo & mod)
		res = (res >> 61) + (res & mod)
		if res >= mod {
			res -= mod
		}
		return res
	}

	powMod := func(a, b uint64) uint64 {
		res := uint64(1)
		a %= mod
		for b > 0 {
			if b%2 == 1 {
				res = mulMod(res, a)
			}
			a = mulMod(a, a)
			b /= 2
		}
		return res
	}

	check := func(length int) bool {
		if length <= 0 {
			return false
		}
		p := powMod(base, uint64(length-1))
		var h uint64
		for i := 0; i < length; i++ {
			h = (mulMod(h, base) + uint64(nums[i])) % mod
		}

		numHashes := n - length + 1
		hashes := make([]uint64, numHashes)
		hashes[0] = h
		for i := length; i < n; i++ {
			sub := mulMod(uint64(nums[i-length]), p)
			var nextH uint64
			if h < sub {
				nextH = h + mod - sub
			} else {
				nextH = h - sub
			}
			h = (mulMod(nextH, base) + uint64(nums[i])) % mod
			hashes[i-length+1] = h
		}

		sort.Uint64s(hashes)
		for i := 0; i < numHashes; i++ {
			if (i == 0 || hashes[i] != hashes[i-1]) &&
				(i == numHashes-1 || hashes[i] != hashes[i+1]) {
				return true
			}
		}
		return false
	}

	for low <= high {
		mid := (low + high) / 2
		if check(mid) {
			ans = mid
			high = mid - 1
		} else {
			low = mid + 1
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
# @param {Integer[]} nums
# @return {Integer}
def smallest_unique_subarray(nums)
  n = nums.length
  low, high, ans = 1, n, n
  mod = (1 << 61) - 1
  base = 100019

  check = lambda do |length|
    return false if length <= 0
    p = base.pow(length - 1, mod)
    h = 0
    (0...length).each { |i| h = (h * base + nums[i]) % mod }

    num_hashes = n - length + 1
    hashes = Array.new(num_hashes)
    hashes[0] = h
    (length...n).each do |i|
      sub = (nums[i - length] * p) % mod
      h = ((h - sub + mod) % mod * base + nums[i]) % mod
      hashes[i - length + 1] = h
    end

    hashes.sort!
    (0...num_hashes).each do |i|
      if (i == 0 || hashes[i] != hashes[i - 1]) && (i == num_hashes - 1 || hashes[i] != hashes[i + 1])
        return true
      end
    end
    false
  end

  while low <= high
    mid = (low + high) / 2
    if check.call(mid)
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
import java.util.Arrays

object Solution {
    def smallestUniqueSubarray(nums: Array[Int]): Int = {
        val n = nums.length
        var low = 1
        var high = n
        var ans = n
        val MOD = (BigInt(1) << 61) - 1
        val BASE = BigInt(100019)

        def check(length: Int): Boolean = {
            if (length <= 0) return false
            val P = BASE.modPow(BigInt(length - 1), MOD)
            var h = BigInt(0)
            for (i <- 0 until length) {
                h = (h * BASE + BigInt(nums(i))) % MOD
            }
            val numHashes = n - length + 1
            val hashes = new Array[Long](numHashes)
            hashes(0) = h.toLong
            for (i <- length until n) {
                val sub = (BigInt(nums(i - length)) * P) % MOD
                h = ((h - sub + MOD) % MOD * BASE + BigInt(nums(i))) % MOD
                hashes(i - length + 1) = h.toLong
            }
            Arrays.sort(hashes)
            for (i <- 0 until numHashes) {
                if ((i == 0 || hashes(i) != hashes(i - 1)) && (i == numHashes - 1 || hashes(i) != hashes(i + 1))) {
                    return true
                }
            }
            false
        }

        while (low <= high) {
            val mid = (low + high) / 2
            if (check(mid)) {
                ans = mid
                high = mid - 1
            } else {
                low = mid + 1
            }
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
    pub fn smallest_unique_subarray(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut low = 1;
        let mut high = n;
        let mut ans = n;
        let mod_val: u64 = (1u64 << 61) - 1;
        let base: u64 = 100019;

        while low <= high {
            let mid = low + (high - low) / 2;
            if Self::check(mid, &nums, mod_val, base) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        ans as i32
    }

    fn check(length: usize, nums: &[i32], mod_val: u64, base: u64) -> bool {
        if length == 0 {
            return false;
        }
        let n = nums.len();
        let mut p: u64 = 1;
        for _ in 0..length - 1 {
            p = ((p as u128 * base as u128) % mod_val as u128) as u64;
        }

        let mut h: u64 = 0;
        for i in 0..length {
            h = ((h as u128 * base as u128 + nums[i] as u128) % mod_val as u128) as u64;
        }

        let num_hashes = n - length + 1;
        let mut hashes = Vec::with_capacity(num_hashes);
        hashes.push(h);

        for i in length..n {
            let term = (nums[i - length] as u128 * p as u128) % mod_val as u128;
            h = (((h as u128 + mod_val as u128 - term) % mod_val as u128 * base as u128 + nums[i] as u128) % mod_val as u128) as u64;
            hashes.push(h);
        }

        hashes.sort_unstable();
        for i in 0..num_hashes {
            if (i == 0 || hashes[i] != hashes[i - 1]) && (i == num_hashes - 1 || hashes[i] != hashes[i + 1]) {
                return true;
            }
        }
        false
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (smallest-unique-subarray nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ((n (length nums))
         (vec (list->vector nums))
         (m (- (expt 2 61) 1))
         (base 100019))
    (define (pow-mod b e m)
      (let loop ((b b) (e e) (res 1))
        (cond
          [(= e 0) res]
          [(even? e) (loop (remainder (* b b) m) (quotient e 2) res)]
          [else (loop (remainder (* b b) m) (quotient e 2) (remainder (* res b) m))])))
    (define (check len)
      (if (<= len 0) #f
          (let* ([p (pow-mod base (- len 1) m)]
                 [h-start (for/fold ([h 0]) ([i (in-range len)])
                            (remainder (+ (* h base) (vector-ref vec i)) m))])
            (let-values ([(last-h all-hashes)
                          (for/fold ([h h-start] [acc (list h-start)])
                                    ([i (in-range len n)])
                            (let* ([term (remainder (* (vector-ref vec (- i len)) p) m)]
                                   [h-next (remainder (+ (* (remainder (+ (- h term) m) m) base) (vector-ref vec i)) m)])
                              (values h-next (cons h-next acc))))])
              (let ([sorted (sort all-hashes <)])
                (let loop-find ([lst sorted] [prev -1])
                  (cond
                    [(null? lst) #f]
                    [(and (not (= (car lst) prev))
                          (or (null? (cdr lst)) (not (= (car lst) (cadr lst))))) #t]
                    [else (loop-find (cdr lst) (car lst))])))))))
    (let loop-bs ([low 1] [high n] [ans n])
      (if (<= low high)
          (let ([mid (quotient (+ low high) 2)])
            (if (check mid)
                (loop-bs low (- mid 1) mid)
                (loop-bs (+ mid 1) high ans)))
          ans))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec smallest_unique_subarray(Nums :: [integer()]) -> integer().
smallest_unique_subarray(Nums) ->
    N = length(Nums),
    Arr = list_to_tuple(Nums),
    Mod = (1 bsl 61) - 1,
    Base = 100019,
    bs(1, N, N, Arr, N, Mod, Base).

bs(Low, High, Ans, Arr, N, Mod, Base) ->
    if Low > High -> Ans;
       true ->
           Mid = (Low + High) div 2,
           case check(Mid, Arr, N, Mod, Base) of
               true -> bs(Low, Mid - 1, Mid, Arr, N, Mod, Base);
               false -> bs(Mid + 1, High, Ans, Arr, N, Mod, Base)
           end
    end.

check(Len, Arr, N, Mod, Base) ->
    if Len =< 0 -> false;
       true ->
           P = pow_mod(Base, Len - 1, Mod),
           H0 = calculate_initial_hash(Len, Arr, Base, Mod),
           Hashes = calculate_all_hashes(Len, Arr, N, Mod, Base, P, H0),
           SortedHashes = lists:sort(Hashes),
           has_unique_rec(SortedHashes, -1)
    end.

pow_mod(_B, 0, _M) -> 1;
pow_mod(B, E, M) ->
    Half = E div 2,
    Res = pow_mod(B, Half, M),
    Res2 = (Res * Res) rem M,
    if E rem 2 == 0 -> Res2;
       true -> (Res2 * B) rem M
    end.

calculate_initial_hash(Len, Arr, Base, Mod) ->
    calculate_initial_hash_rec(1, Len, Arr, Base, Mod, 0).

calculate_initial_hash_rec(I, Len, Arr, Base, Mod, H) when I =< Len ->
    calculate_initial_hash_rec(I + 1, Len, Arr, Base, Mod, (H * Base + element(I, Arr)) rem Mod);
calculate_initial_hash_rec(_I, _Len, _Arr, _Base, _Mod, H) -> H.

calculate_all_hashes(Len, Arr, N, Mod, Base, P, H0) ->
    calculate_all_hashes_rec(Len + 1, Arr, N, Mod, Base, P, H0, Len, [H0]).

calculate_all_hashes_rec(I, Arr, N, Mod, Base, P, H, Len, Acc) when I =< N ->
    Term = (element(I - Len, Arr) * P) rem Mod,
    HNext = (((H + Mod - Term) rem Mod) * Base + element(I, Arr)) rem Mod,
    calculate_all_hashes_rec(I + 1, Arr, N, Mod, Base, P, HNext, Len, [HNext | Acc]);
calculate_all_hashes_rec(_I, _Arr, _N, _Mod, _Base, _P, _H, _Len, Acc) -> Acc.

has_unique_rec([], _Prev) -> false;
has_unique_rec([H], Prev) -> H /= Prev;
has_unique_rec([H1, H2 | T], Prev) ->
    if (H1 /= Prev) and (H1 /= H2) -> true;
       true -> has_unique_rec([H2 | T], H1)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec smallest_unique_subarray(nums :: [integer]) :: integer
  def smallest_unique_subarray(nums) do
    n = length(nums)
    arr = List.to_tuple(nums)
    mod_val = Bitwise.bsl(1, 61) - 1
    base = 100019
    binary_search(1, n, n, arr, n, mod_val, base)
  end

  defp binary_search(low, high, ans, arr, n, mod_val, base) do
    if low > high do
      ans
    else
      mid = div(low + high, 2)
      if check(mid, arr, n, mod_val, base) do
        binary_search(low, mid - 1, mid, arr, n, mod_val, base)
      else
        binary_search(mid + 1, high, ans, arr, n, mod_val, base)
      end
    end
  end

  defp check(len, arr, n, mod_val, base) do
    if len <= 0 do
      false
    else
      p = pow_mod(base, len - 1, mod_val)
      h0 = calculate_initial_hash(len, arr, base, mod_val)
      hashes = calculate_all_hashes(len, arr, n, mod_val, base, p, h0)
      sorted_hashes = Enum.sort(hashes)
      has_unique?(sorted_hashes, -1)
    end
  end

  defp pow_mod(_base, 0, _m), do: 1
  defp pow_mod(base, exp, m) do
    half = pow_mod(base, div(exp, 2), m)
    res = rem(half * half, m)
    if rem(exp, 2) == 0 do
      res
    else
      rem(res * base, m)
    end
  end

  defp calculate_initial_hash(len, arr, base, mod_val) do
    Enum.reduce(0..(len - 1), 0, fn i, acc ->
      rem(acc * base + elem(arr, i), mod_val)
    end)
  end

  defp calculate_all_hashes(len, arr, n, mod_val, base, p, h0) do
    if len >= n do
      [h0]
    else
      calculate_all_hashes_rec(len, arr, n, mod_val, base, p, h0, len, [h0])
    end
  end

  defp calculate_all_hashes_rec(i, arr, n, mod_val, base, p, h, len, acc) when i < n do
    term = rem(elem(arr, i - len) * p, mod_val)
    h_next = rem(rem(h + mod_val - term, mod_val) * base + elem(arr, i), mod_val)
    calculate_all_hashes_rec(i + 1, arr, n, mod_val, base, p, h_next, len, [h_next | acc])
  end
  defp calculate_all_hashes_rec(_i, _arr, _n, _mod_val, _base, _p, _h, _len, acc), do: acc

  defp has_unique?([], _prev), do: false
  defp has_unique?([h], prev), do: h != prev
  defp has_unique?([h1, h2 | t], prev) do
    if h1 != prev and h1 != h2 do
      true
    else
      has_unique?([h2 | t], h1)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N \log^2 N). Each step of the binary search (which runs $O(\log N)$ times) involves computing rolling hashes for all subarrays of the current length in $O(N)$ time, followed by sorting these hashes in $O(N \log N)$ time to identify unique occurrences. For $N = 10^5$, this results in approximately $3 \times 10^7$ operations, fitting within the standard time limit.
- **Space Complexity:** O(N). We store $O(N)$ rolling hash values in an array/list during each step of the binary search, and precompute hash constants and powers, which all consume linear space.
