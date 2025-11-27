---
layout: post
title: "Maximum Subarray Sum With Length Divisible by K"
date: 2025-11-27 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Prefix Sum"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    long long maxSubarraySum(std::vector<int>&\
        \ nums, int k) {\n        int n = nums.size();\n\n        std::vector<long long>\
        \ dp(k, std::numeric_limits<long long>::max());\n        dp[0] = 0; \n\n   \
        \     long long current_prefix_sum = 0;\n        long long max_subarray_sum\
        \ = std::numeric_limits<long long>::min(); \n\n        for (int j = 0; j < n;\
        \ ++j) {\n            current_prefix_sum += nums[j];\n\n            int remainder\
        \ = (j + 1) % k;\n\n            if (dp[remainder] != std::numeric_limits<long\
        \ long>::max()) {\n                max_subarray_sum = std::max(max_subarray_sum,\
        \ current_prefix_sum - dp[remainder]);\n            }\n\n            dp[remainder]\
        \ = std::min(dp[remainder], current_prefix_sum);\n        }\n\n        return\
        \ max_subarray_sum;\n    }\n};"
      java: "import java.util.Arrays;\n\nclass Solution {\n    public long maxSubarraySum(int[]\
        \ nums, int k) {\n        int n = nums.length;\n\n        long[] dp = new long[k];\n\
        \        Arrays.fill(dp, Long.MAX_VALUE);\n        dp[0] = 0; \n\n        long\
        \ currentPrefixSum = 0;\n        long maxSubarraySum = Long.MIN_VALUE; \n\n\
        \        for (int j = 0; j < n; ++j) {\n            currentPrefixSum += nums[j];\n\
        \n            int remainder = (j + 1) % k;\n\n            if (dp[remainder]\
        \ != Long.MAX_VALUE) {\n                maxSubarraySum = Math.max(maxSubarraySum,\
        \ currentPrefixSum - dp[remainder]);\n            }\n\n            dp[remainder]\
        \ = Math.min(dp[remainder], currentPrefixSum);\n        }\n\n        return\
        \ maxSubarraySum;\n    }\n}"
      python: "import math\n\nclass Solution:\n    def maxSubarraySum(self, nums: list[int],\
        \ k: int) -> int:\n        n = len(nums)\n\n        dp = [math.inf] * k\n  \
        \      dp[0] = 0 \n\n        current_prefix_sum = 0\n        max_subarray_sum\
        \ = -math.inf \n\n        for j in range(n):\n            current_prefix_sum\
        \ += nums[j]\n\n            remainder = (j + 1) % k\n\n            if dp[remainder]\
        \ != math.inf:\n                max_subarray_sum = max(max_subarray_sum, current_prefix_sum\
        \ - dp[remainder])\n\n            dp[remainder] = min(dp[remainder], current_prefix_sum)\n\
        \n        return max_subarray_sum"
      python3: "import math\n\nclass Solution:\n    def maxSubarraySum(self, nums: list[int],\
        \ k: int) -> int:\n        n = len(nums)\n\n        dp = [math.inf] * k\n  \
        \      dp[0] = 0 \n\n        current_prefix_sum = 0\n        max_subarray_sum\
        \ = -math.inf \n\n        for j in range(n):\n            current_prefix_sum\
        \ += nums[j]\n\n            remainder = (j + 1) % k\n\n            if dp[remainder]\
        \ != math.inf:\n                max_subarray_sum = max(max_subarray_sum, current_prefix_sum\
        \ - dp[remainder])\n\n            dp[remainder] = min(dp[remainder], current_prefix_sum)\n\
        \n        return max_subarray_sum"
      c: "#include <stdlib.h>\n#include <limits.h>\n\nlong long max(long long a, long\
        \ long b) {\n    return a > b ? a : b;\n}\n\nlong long min(long long a, long\
        \ long b) {\n    return a < b ? a : b;\n}\n\nlong long maxSubarraySum(int* nums,\
        \ int numsSize, int k) {\n    long long* dp = (long long*) malloc(k * sizeof(long\
        \ long));\n    if (dp == NULL) {\n        return 0; \n    }\n\n    for (int\
        \ i = 0; i < k; ++i) {\n        dp[i] = LLONG_MAX;\n    }\n    dp[0] = 0; \n\
        \n    long long currentPrefixSum = 0;\n    long long maxSubarraySum = LLONG_MIN;\
        \ \n\n    for (int j = 0; j < numsSize; ++j) {\n        currentPrefixSum +=\
        \ nums[j];\n\n        int remainder = (j + 1) % k;\n\n        if (dp[remainder]\
        \ != LLONG_MAX) {\n            maxSubarraySum = max(maxSubarraySum, currentPrefixSum\
        \ - dp[remainder]);\n        }\n\n        dp[remainder] = min(dp[remainder],\
        \ currentPrefixSum);\n    }\n\n    free(dp); \n    return maxSubarraySum;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\nusing System.Linq;\n\
        \npublic class Solution {\n    public long MaxSubarraySum(int[] nums, int k)\
        \ {\n        int n = nums.Length;\n\n        long[] dp = new long[k];\n    \
        \    Array.Fill(dp, long.MaxValue);\n        dp[0] = 0; \n\n        long currentPrefixSum\
        \ = 0;\n        long maxSubarraySum = long.MinValue; \n\n        for (int j\
        \ = 0; j < n; ++j) {\n            currentPrefixSum += nums[j];\n\n         \
        \   int remainder = (j + 1) % k;\n\n            if (dp[remainder] != long.MaxValue)\
        \ {\n                maxSubarraySum = Math.Max(maxSubarraySum, currentPrefixSum\
        \ - dp[remainder]);\n            }\n\n            dp[remainder] = Math.Min(dp[remainder],\
        \ currentPrefixSum);\n        }\n\n        return maxSubarraySum;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} k\n * @return\
        \ {number}\n */\nvar maxSubarraySum = function(nums, k) {\n    const n = nums.length;\n\
        \n    const dp = new Array(k).fill(Number.MAX_SAFE_INTEGER); \n    dp[0] = 0;\
        \ \n\n    let currentPrefixSum = 0;\n    let maxSubarraySum = -Number.MAX_SAFE_INTEGER;\
        \ \n\n    for (let j = 0; j < n; ++j) {\n        currentPrefixSum += nums[j];\n\
        \n        const remainder = (j + 1) % k;\n\n        if (dp[remainder] !== Number.MAX_SAFE_INTEGER)\
        \ {\n            maxSubarraySum = Math.max(maxSubarraySum, currentPrefixSum\
        \ - dp[remainder]);\n        }\n\n        dp[remainder] = Math.min(dp[remainder],\
        \ currentPrefixSum);\n    }\n\n    return maxSubarraySum;\n};"
      typescript: "function maxSubarraySum(nums: number[], k: number): number {\n  \
        \  const n = nums.length;\n\n    const dp: number[] = new Array(k).fill(Number.MAX_SAFE_INTEGER);\n\
        \    dp[0] = 0; \n\n    let currentPrefixSum: number = 0;\n    let maxSubarraySum:\
        \ number = -Number.MAX_SAFE_INTEGER; \n\n    for (let j = 0; j < n; ++j) {\n\
        \        currentPrefixSum += nums[j];\n\n        const remainder: number = (j\
        \ + 1) % k;\n\n        if (dp[remainder] !== Number.MAX_SAFE_INTEGER) {\n  \
        \          maxSubarraySum = Math.max(maxSubarraySum, currentPrefixSum - dp[remainder]);\n\
        \        }\n\n        dp[remainder] = Math.min(dp[remainder], currentPrefixSum);\n\
        \    }\n\n    return maxSubarraySum;\n}"
      php: "class Solution {\n    /**\n     * @param int[] $nums\n     * @param int\
        \ $k\n     * @return int\n     */\n    function maxSubarraySum(array $nums,\
        \ int $k): int {\n        $n = count($nums);\n\n        $dp = array_fill(0,\
        \ $k, PHP_INT_MAX);\n        $dp[0] = 0; \n\n        $currentPrefixSum = 0;\n\
        \        $maxSubarraySum = PHP_INT_MIN; \n\n        for ($j = 0; $j < $n; ++$j)\
        \ {\n            $currentPrefixSum += $nums[$j];\n\n            $remainder =\
        \ ($j + 1) % $k;\n\n            if ($dp[$remainder] !== PHP_INT_MAX) {\n   \
        \             $maxSubarraySum = max($maxSubarraySum, $currentPrefixSum - $dp[$remainder]);\n\
        \            }\n\n            $dp[$remainder] = min($dp[$remainder], $currentPrefixSum);\n\
        \        }\n\n        return $maxSubarraySum;\n    }\n}"
      swift: "import Foundation\n\nclass Solution {\n    func maxSubarraySum(_ nums:\
        \ [Int], _ k: Int) -> Int {\n        let n = nums.count\n\n        var dp =\
        \ Array(repeating: Int.max, count: k)\n        dp[0] = 0 \n\n        var currentPrefixSum:\
        \ Int = 0\n        var maxSubarraySum: Int = Int.min \n\n        for j in 0..<n\
        \ {\n            currentPrefixSum += nums[j]\n\n            let remainder =\
        \ (j + 1) % k\n\n            if dp[remainder] != Int.max {\n               \
        \ maxSubarraySum = max(maxSubarraySum, currentPrefixSum - dp[remainder])\n \
        \           }\n\n            dp[remainder] = min(dp[remainder], currentPrefixSum)\n\
        \        }\n\n        return maxSubarraySum\n    }\n}"
      kotlin: "import kotlin.math.max\nimport kotlin.math.min\n\nclass Solution {\n\
        \    fun maxSubarraySum(nums: IntArray, k: Int): Long {\n        val n = nums.size\n\
        \n        val dp = LongArray(k) { Long.MAX_VALUE }\n        dp[0] = 0L \n\n\
        \        var currentPrefixSum: Long = 0L\n        var maxSubarraySum: Long =\
        \ Long.MIN_VALUE \n\n        for (j in 0 until n) {\n            currentPrefixSum\
        \ += nums[j]\n\n            val remainder = (j + 1) % k\n\n            if (dp[remainder]\
        \ != Long.MAX_VALUE) {\n                maxSubarraySum = max(maxSubarraySum,\
        \ currentPrefixSum - dp[remainder])\n            }\n\n            dp[remainder]\
        \ = min(dp[remainder], currentPrefixSum)\n        }\n\n        return maxSubarraySum\n\
        \    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int maxSubarraySum(List<int>\
        \ nums, int k) {\n    final n = nums.length;\n\n    final dp = List<int>.filled(k,\
        \ 9223372036854775807); \n    dp[0] = 0; \n\n    int currentPrefixSum = 0;\n\
        \    int maxSubarraySum = -9223372036854775808; \n\n    for (int j = 0; j <\
        \ n; ++j) {\n      currentPrefixSum += nums[j];\n\n      final remainder = (j\
        \ + 1) % k;\n\n      if (dp[remainder] != 9223372036854775807) {\n        maxSubarraySum\
        \ = max(maxSubarraySum, currentPrefixSum - dp[remainder]);\n      }\n\n    \
        \  dp[remainder] = min(dp[remainder], currentPrefixSum);\n    }\n\n    return\
        \ maxSubarraySum;\n  }\n}"
      go: "package main\n\nimport (\n\t\"math\"\n)\n\nfunc maxSubarraySum(nums []int,\
        \ k int) int64 {\n\tn := len(nums)\n\n\tdp := make([]int64, k)\n\tfor i := range\
        \ dp {\n\t\tdp[i] = math.MaxInt64\n\t}\n\tdp[0] = 0 \n\n\tvar currentPrefixSum\
        \ int64 = 0\n\tvar maxSubarraySum int64 = math.MinInt64 \n\n\tfor j := 0; j\
        \ < n; j++ {\n\t\tcurrentPrefixSum += int64(nums[j])\n\n\t\tremainder := (j\
        \ + 1) % k\n\n\t\tif dp[remainder] != math.MaxInt64 {\n\t\t\tmaxSubarraySum\
        \ = max(maxSubarraySum, currentPrefixSum - dp[remainder])\n\t\t}\n\n\t\tdp[remainder]\
        \ = min(dp[remainder], currentPrefixSum)\n\t}\n\n\treturn maxSubarraySum\n}\n\
        \nfunc max(a, b int64) int64 {\n\tif a > b {\n\t\treturn a\n\t}\n\treturn b\n\
        }\n\nfunc min(a, b int64) int64 {\n\tif a < b {\n\t\treturn a\n\t}\n\treturn\
        \ b\n}"
      ruby: "class Solution\n    # @param {Integer[]} nums\n    # @param {Integer} k\n\
        \    # @return {Integer}\n    def max_subarray_sum(nums, k)\n        n = nums.length\n\
        \n        dp = Array.new(k, Float::INFINITY)\n        dp[0] = 0 \n\n       \
        \ current_prefix_sum = 0\n        max_subarray_sum = -Float::INFINITY \n\n \
        \       for j in 0...n\n            current_prefix_sum += nums[j]\n\n      \
        \      remainder = (j + 1) % k\n\n            if dp[remainder] != Float::INFINITY\n\
        \                max_subarray_sum = [max_subarray_sum, current_prefix_sum -\
        \ dp[remainder]].max\n            end\n\n            dp[remainder] = [dp[remainder],\
        \ current_prefix_sum].min\n        end\n\n        return max_subarray_sum\n\
        \    end\nend"
      scala: "import scala.collection.mutable.ArrayBuffer\nimport scala.math.{max, min}\n\
        \nobject Solution {\n    def maxSubarraySum(nums: Array[Int], k: Int): Long\
        \ = {\n        val n = nums.length\n\n        val dp = Array.fill[Long](k)(Long.MaxValue)\n\
        \        dp(0) = 0L \n\n        var currentPrefixSum: Long = 0L\n        var\
        \ maxSubarraySum: Long = Long.MinValue \n\n        for (j <- 0 until n) {\n\
        \            currentPrefixSum += nums(j)\n\n            val remainder = (j +\
        \ 1) % k\n\n            if (dp(remainder) != Long.MaxValue) {\n            \
        \    maxSubarraySum = max(maxSubarraySum, currentPrefixSum - dp(remainder))\n\
        \            }\n\n            dp(remainder) = min(dp(remainder), currentPrefixSum)\n\
        \        }\n\n        return maxSubarraySum\n    }\n}"
      rust: "use std::cmp::{max, min};\n\nimpl Solution {\n    pub fn max_subarray_sum(nums:\
        \ Vec<i32>, k: i32) -> i64 {\n        let n = nums.len();\n        let k_usize\
        \ = k as usize;\n\n        let mut dp: Vec<i64> = vec![std::i64::MAX; k_usize];\n\
        \        dp[0] = 0; \n\n        let mut current_prefix_sum: i64 = 0;\n     \
        \   let mut max_subarray_sum: i64 = std::i64::MIN; \n\n        for j in 0..n\
        \ {\n            current_prefix_sum += nums[j] as i64;\n\n            let remainder\
        \ = ((j + 1) as i32 % k) as usize;\n\n            if dp[remainder] != std::i64::MAX\
        \ {\n                max_subarray_sum = max(max_subarray_sum, current_prefix_sum\
        \ - dp[remainder]);\n            }\n\n            dp[remainder] = min(dp[remainder],\
        \ current_prefix_sum);\n        }\n\n        max_subarray_sum\n    }\n}"
      racket: "#lang racket\n\n(define (max-subarray-sum nums k)\n  (define n (vector-length\
        \ nums))\n\n  (define dp (make-vector k +inf.0)) \n  (vector-set! dp 0 0) \n\
        \n  (define current-prefix-sum (box 0))\n  (define max-subarray-sum (box -inf.0))\
        \ \n\n  (for ([j (in-range n)])\n    (set-box! current-prefix-sum (+ (unbox\
        \ current-prefix-sum) (vector-ref nums j)))\n\n    (define remainder (modulo\
        \ (+ j 1) k))\n\n    (when (not (eq? (vector-ref dp remainder) +inf.0))\n  \
        \    (set-box! max-subarray-sum\n                (max (unbox max-subarray-sum)\
        \ (- (unbox current-prefix-sum) (vector-ref dp remainder)))))\n\n    (vector-set!\
        \ dp remainder (min (vector-ref dp remainder) (unbox current-prefix-sum))))\n\
        \n  (unbox max-subarray-sum))"
      erlang: "-module(solution).\n-export([max_subarray_sum/2]).\n\nmax(A, B) when\
        \ A > B -> A;\nmax(A, B) -> B.\n\nmin(A, B) when A < B -> A;\nmin(A, B) -> B.\n\
        \nmax_subarray_sum(Nums, K) ->\n    N = length(Nums),\n\n    Infinity = 1000000000000000000,\
        \ \n    NegInfinity = -1000000000000000000,\n\n    Dp = array:new(K, {default,\
        \ Infinity}),\n    Dp1 = array:set(0, 0, Dp), \n\n    max_subarray_sum_recursive(Nums,\
        \ K, 0, 0, Dp1, NegInfinity).\n\nmax_subarray_sum_recursive(Nums, K, J, CurrentPrefixSum,\
        \ Dp, MaxSubarraySum) ->\n    if J < length(Nums) ->\n        Num = lists:nth(J\
        \ + 1, Nums), \n        NewPrefixSum = CurrentPrefixSum + Num,\n\n        Remainder\
        \ = (J + 1) rem K,\n\n        DpRemainderVal = array:get(Remainder, Dp),\n\n\
        \        NewMaxSubarraySum = \n            if DpRemainderVal =/= Infinity ->\n\
        \                max(MaxSubarraySum, NewPrefixSum - DpRemainderVal);\n     \
        \       true ->\n                MaxSubarraySum\n            end,\n\n      \
        \  NewDp = array:set(Remainder, min(DpRemainderVal, NewPrefixSum), Dp),\n\n\
        \        max_subarray_sum_recursive(Nums, K, J + 1, NewPrefixSum, NewDp, NewMaxSubarraySum);\n\
        \    true ->\n        MaxSubarraySum\n    end."
      elixir: "defmodule Solution do\n  @spec max_subarray_sum(nums :: [integer], k\
        \ :: integer) :: integer\n  def max_subarray_sum(nums, k) do\n    n = length(nums)\n\
        \n    infinity = 1_000_000_000_000_000_000\n    neg_infinity = -1_000_000_000_000_000_000\n\
        \n    dp = Map.new() |> Map.put(0, 0) \n\n    {_final_prefix_sum, final_max_sum,\
        \ _final_dp} = \n      Enum.reduce(0..(n - 1), {0, neg_infinity, dp}, fn j,\
        \ {current_prefix_sum, max_subarray_sum, current_dp} ->\n        num = Enum.at(nums,\
        \ j)\n        new_prefix_sum = current_prefix_sum + num\n\n        remainder\
        \ = rem(j + 1, k)\n\n        dp_remainder_val = Map.get(current_dp, remainder,\
        \ infinity)\n\n        new_max_subarray_sum =\n          if dp_remainder_val\
        \ != infinity do\n            max(max_subarray_sum, new_prefix_sum - dp_remainder_val)\n\
        \          else\n            max_subarray_sum\n          end\n\n        new_dp\
        \ = Map.put(current_dp, remainder, min(dp_remainder_val, new_prefix_sum))\n\n\
        \        {new_prefix_sum, new_max_subarray_sum, new_dp}\n      end)\n\n    final_max_sum\n\
        \  end\n\n  defp max(a, b), do: if a > b, do: a, else: b\n  defp min(a, b),\
        \ do: if a < b, do: a, else: b\nend"
    approach: The problem asks for the maximum sum of a subarray whose length is divisible
      by `k`. We can solve this using prefix sums and dynamic programming. Let `P[x]`
      denote the prefix sum of `nums` up to index `x-1`, with `P[0] = 0`. The sum of
      a subarray `nums[i...j]` is `P[j+1] - P[i]`. The length of this subarray is `(j+1)
      - i`. We are interested in subarrays where `((j+1) - i) % k == 0`, which implies
      `(j+1) % k == i % k`.
    time_complexity: The time complexity is O(N), where N is the length of the `nums`
      array. We iterate through the `nums` array once, performing constant-time operations
      (arithmetic, array/map access) in each step. For languages using hash maps (like
      Elixir, Erlang with maps) for `dp`, the map operations take O(log k) time, leading
      to an O(N log k) complexity. Given `k <= N`, this is effectively O(N log N), which
      is acceptable for the given constraints.
    space_complexity: The space complexity is O(k). We use a `dp` array (or map) of
      size `k` to store the minimum prefix sum encountered for each possible remainder
      modulo `k`. This space is directly proportional to `k`.
    elapsed_time: 87.68686151504517
    model: gemini-2.5-flash
    generated_at: '2025-11-27 01:03:58 '
  - solutions:
      cpp: "class Solution {\npublic:\n    long long maxSubarraySum(vector<int>& nums,\
        \ int k) {\n        int n = nums.size();\n        long long max_sum = LLONG_MIN;\n\
        \        long long prefix_sum = 0;\n        unordered_map<int, long long> mp;\n\
        \        mp[0] = 0;\n        for (int i = 0; i < n; i++) {\n            prefix_sum\
        \ += nums[i];\n            long long sum = prefix_sum;\n            if (mp.find((i\
        \ + 1) % k) != mp.end()) {\n                sum -= mp[(i + 1) % k];\n      \
        \      }\n            max_sum = max(max_sum, sum);\n            if (mp.find((i\
        \ + 1) % k) == mp.end() || mp[(i + 1) % k] < prefix_sum) {\n               \
        \ mp[(i + 1) % k] = prefix_sum;\n            }\n        }\n        return max_sum;\n\
        \    }\n};"
      java: "class Solution {\n    public long maxSubarraySum(int[] nums, int k) {\n\
        \        int n = nums.length;\n        long max_sum = Long.MIN_VALUE;\n    \
        \    long prefix_sum = 0;\n        HashMap<Integer, Long> mp = new HashMap<>();\n\
        \        mp.put(0, 0L);\n        for (int i = 0; i < n; i++) {\n           \
        \ prefix_sum += nums[i];\n            long sum = prefix_sum;\n            if\
        \ (mp.containsKey((i + 1) % k)) {\n                sum -= mp.get((i + 1) % k);\n\
        \            }\n            max_sum = Math.max(max_sum, sum);\n            if\
        \ (!mp.containsKey((i + 1) % k) || mp.get((i + 1) % k) < prefix_sum) {\n   \
        \             mp.put((i + 1) % k, prefix_sum);\n            }\n        }\n \
        \       return max_sum;\n    }\n}"
      python: "class Solution:\n    def maxSubarraySum(self, nums: list[int], k: int)\
        \ -> int:\n        n = len(nums)\n        max_sum = float('-inf')\n        prefix_sum\
        \ = 0\n        mp = {0: 0}\n        for i in range(n):\n            prefix_sum\
        \ += nums[i]\n            sum_ = prefix_sum\n            if (i + 1) % k in mp:\n\
        \                sum_ -= mp[(i + 1) % k]\n            max_sum = max(max_sum,\
        \ sum_)\n            if (i + 1) % k not in mp or mp[(i + 1) % k] < prefix_sum:\n\
        \                mp[(i + 1) % k] = prefix_sum\n        return max_sum"
      python3: "class Solution:\n    def maxSubarraySum(self, nums: list[int], k: int)\
        \ -> int:\n        n = len(nums)\n        max_sum = float('-inf')\n        prefix_sum\
        \ = 0\n        mp = {0: 0}\n        for i in range(n):\n            prefix_sum\
        \ += nums[i]\n            sum_ = prefix_sum\n            if (i + 1) % k in mp:\n\
        \                sum_ -= mp[(i + 1) % k]\n            max_sum = max(max_sum,\
        \ sum_)\n            if (i + 1) % k not in mp or mp[(i + 1) % k] < prefix_sum:\n\
        \                mp[(i + 1) % k] = prefix_sum\n        return max_sum"
      c: "typedef long long ll;\nstruct Solution {\n    ll maxSubarraySum(int* nums,\
        \ int numsSize, int k) {\n        ll max_sum = LLONG_MIN;\n        ll prefix_sum\
        \ = 0;\n        int* mp = (int*)malloc((k + 1) * sizeof(int));\n        for\
        \ (int i = 0; i <= k; i++) {\n            mp[i] = INT_MIN;\n        }\n    \
        \    mp[0] = 0;\n        for (int i = 0; i < numsSize; i++) {\n            prefix_sum\
        \ += nums[i];\n            ll sum = prefix_sum;\n            if (mp[(i + 1)\
        \ % k] != INT_MIN) {\n                sum -= mp[(i + 1) % k];\n            }\n\
        \            max_sum = (max_sum > sum) ? max_sum : sum;\n            if (mp[(i\
        \ + 1) % k] < prefix_sum) {\n                mp[(i + 1) % k] = prefix_sum;\n\
        \            }\n        }\n        free(mp);\n        return max_sum;\n    }\n\
        };"
      csharp: "public class Solution {\n    public long MaxSubarraySum(int[] nums, int\
        \ k) {\n        int n = nums.Length;\n        long max_sum = long.MinValue;\n\
        \        long prefix_sum = 0;\n        Dictionary<int, long> mp = new Dictionary<int,\
        \ long>();\n        mp[0] = 0;\n        for (int i = 0; i < n; i++) {\n    \
        \        prefix_sum += nums[i];\n            long sum = prefix_sum;\n      \
        \      if (mp.ContainsKey((i + 1) % k)) {\n                sum -= mp[(i + 1)\
        \ % k];\n            }\n            max_sum = Math.Max(max_sum, sum);\n    \
        \        if (!mp.ContainsKey((i + 1) % k) || mp[(i + 1) % k] < prefix_sum) {\n\
        \                mp[(i + 1) % k] = prefix_sum;\n            }\n        }\n \
        \       return max_sum;\n    }\n}"
      javascript: "var maxSubarraySum = function(nums, k) {\n    let n = nums.length;\n\
        \    let max_sum = -Infinity;\n    let prefix_sum = 0;\n    let mp = {0: 0};\n\
        \    for (let i = 0; i < n; i++) {\n        prefix_sum += nums[i];\n       \
        \ let sum = prefix_sum;\n        if ((i + 1) % k in mp) {\n            sum -=\
        \ mp[(i + 1) % k];\n        }\n        max_sum = Math.max(max_sum, sum);\n \
        \       if (!(i + 1) % k in mp || mp[(i + 1) % k] < prefix_sum) {\n        \
        \    mp[(i + 1) % k] = prefix_sum;\n        }\n    }\n    return max_sum;\n\
        };"
      typescript: "function maxSubarraySum(nums: number[], k: number): number {\n  \
        \  let n = nums.length;\n    let max_sum = -Infinity;\n    let prefix_sum =\
        \ 0;\n    let mp: { [key: number]: number } = {0: 0};\n    for (let i = 0; i\
        \ < n; i++) {\n        prefix_sum += nums[i];\n        let sum = prefix_sum;\n\
        \        if ((i + 1) % k in mp) {\n            sum -= mp[(i + 1) % k];\n   \
        \     }\n        max_sum = Math.max(max_sum, sum);\n        if (!(i + 1) % k\
        \ in mp || mp[(i + 1) % k] < prefix_sum) {\n            mp[(i + 1) % k] = prefix_sum;\n\
        \        }\n    }\n    return max_sum;\n}"
      php: "class Solution {\n    function maxSubarraySum($nums, $k) {\n        $n =\
        \ count($nums);\n        $max_sum = -INF;\n        $prefix_sum = 0;\n      \
        \  $mp = array(0 => 0);\n        for ($i = 0; $i < $n; $i++) {\n           \
        \ $prefix_sum += $nums[$i];\n            $sum = $prefix_sum;\n            if\
        \ (array_key_exists(($i + 1) % $k, $mp)) {\n                $sum -= $mp[($i\
        \ + 1) % $k];\n            }\n            $max_sum = max($max_sum, $sum);\n\
        \            if (!array_key_exists(($i + 1) % $k, $mp) || $mp[($i + 1) % $k]\
        \ < $prefix_sum) {\n                $mp[($i + 1) % $k] = $prefix_sum;\n    \
        \        }\n        }\n        return $max_sum;\n    }\n}"
      swift: "class Solution {\n    func maxSubarraySum(_ nums: [Int], _ k: Int) ->\
        \ Int {\n        let n = nums.count\n        var max_sum = Int.min\n       \
        \ var prefix_sum = 0\n        var mp: [Int: Int] = [0: 0]\n        for i in\
        \ 0..<n {\n            prefix_sum += nums[i]\n            var sum = prefix_sum\n\
        \            if let val = mp[(i + 1) % k] {\n                sum -= val\n  \
        \          }\n            max_sum = max(max_sum, sum)\n            if mp[(i\
        \ + 1) % k] == nil || mp[(i + 1) % k]! < prefix_sum {\n                mp[(i\
        \ + 1) % k] = prefix_sum\n            }\n        }\n        return max_sum\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun maxSubarraySum(nums: IntArray, k: Int): Long\
        \ {\n        val n = nums.size\n        var max_sum = Long.MIN_VALUE\n     \
        \   var prefix_sum = 0L\n        val mp = mutableMapOf<Int, Long>()\n      \
        \  mp[0] = 0\n        for (i in 0 until n) {\n            prefix_sum += nums[i]\n\
        \            var sum = prefix_sum\n            if (mp.containsKey((i + 1) %\
        \ k)) {\n                sum -= mp[(i + 1) % k]!!\n            }\n         \
        \   max_sum = maxOf(max_sum, sum)\n            if (!mp.containsKey((i + 1) %\
        \ k) || mp[(i + 1) % k]!! < prefix_sum) {\n                mp[(i + 1) % k] =\
        \ prefix_sum\n            }\n        }\n        return max_sum\n    }\n}"
      dart: "class Solution {\n    int maxSubarraySum(List<int> nums, int k) {\n   \
        \     int n = nums.length;\n        int max_sum = -1000000000;\n        int\
        \ prefix_sum = 0;\n        Map<int, int> mp = {0: 0};\n        for (int i =\
        \ 0; i < n; i++) {\n            prefix_sum += nums[i];\n            int sum\
        \ = prefix_sum;\n            if (mp.containsKey((i + 1) % k)) {\n          \
        \      sum -= mp[(i + 1) % k]!;\n            }\n            max_sum = max(max_sum,\
        \ sum);\n            if (!mp.containsKey((i + 1) % k) || mp[(i + 1) % k]! <\
        \ prefix_sum) {\n                mp[(i + 1) % k] = prefix_sum;\n           \
        \ }\n        }\n        return max_sum;\n    }\n}"
      go: "func maxSubarraySum(nums []int, k int) int64 {\n    n := len(nums)\n    max_sum\
        \ := int64(math.MinInt64)\n    prefix_sum := int64(0)\n    mp := make(map[int]int64)\n\
        \    mp[0] = 0\n    for i := 0; i < n; i++ {\n        prefix_sum += int64(nums[i])\n\
        \        sum := prefix_sum\n        if val, ok := mp[(i+1)%k]; ok {\n      \
        \      sum -= val\n        }\n        max_sum = max(max_sum, sum)\n        if\
        \ _, ok := mp[(i+1)%k]; !ok || mp[(i+1)%k] < prefix_sum {\n            mp[(i+1)%k]\
        \ = prefix_sum\n        }\n    }\n    return max_sum\n}\nfunc max(a, b int64)\
        \ int64 {\n    if a > b {\n        return a\n    }\n    return b\n}"
      ruby: "class Solution\n    def max_subarray_sum(nums, k)\n        n = nums.size\n\
        \        max_sum = -10**9\n        prefix_sum = 0\n        mp = {0 => 0}\n \
        \       for i in 0...n\n            prefix_sum += nums[i]\n            sum =\
        \ prefix_sum\n            if mp.key?((i + 1) % k)\n                sum -= mp[(i\
        \ + 1) % k]\n            end\n            max_sum = [max_sum, sum].max\n   \
        \         if !mp.key?((i + 1) % k) || mp[(i + 1) % k] < prefix_sum\n       \
        \         mp[(i + 1) % k] = prefix_sum\n            end\n        end\n     \
        \   max_sum\n    end\nend"
      scala: "object Solution {\n    def maxSubarraySum(nums: Array[Int], k: Int): Long\
        \ = {\n        val n = nums.length\n        var max_sum = Long.MinValue\n  \
        \      var prefix_sum = 0L\n        val mp = scala.collection.mutable.Map[Int,\
        \ Long]()\n        mp(0) = 0\n        for (i <- 0 until n) {\n            prefix_sum\
        \ += nums(i)\n            var sum = prefix_sum\n            if (mp.contains((i\
        \ + 1) % k)) {\n                sum -= mp((i + 1) % k)\n            }\n    \
        \        max_sum = math.max(max_sum, sum)\n            if (!mp.contains((i +\
        \ 1) % k) || mp((i + 1) % k) < prefix_sum) {\n                mp((i + 1) % k)\
        \ = prefix_sum\n            }\n        }\n        max_sum\n    }\n}"
      rust: "struct Solution;\nimpl Solution {\n    pub fn max_subarray_sum(nums: Vec<i32>,\
        \ k: i32) -> i64 {\n        let n = nums.len() as i32;\n        let mut max_sum\
        \ = std::i64::MIN;\n        let mut prefix_sum = 0;\n        let mut mp: std::collections::HashMap<i32,\
        \ i64> = std::collections::HashMap::new();\n        mp.insert(0, 0);\n     \
        \   for i in 0..n {\n            prefix_sum += nums[i as usize] as i64;\n  \
        \          let mut sum = prefix_sum;\n            if let Some(val) = mp.get(&((i\
        \ + 1) % k)) {\n                sum -= val;\n            }\n            max_sum\
        \ = std::cmp::max(max_sum, sum);\n            if !mp.contains_key(&((i + 1)\
        \ % k)) || *mp.get(&((i + 1) % k)).unwrap() < prefix_sum {\n               \
        \ mp.insert((i + 1) % k, prefix_sum);\n            }\n        }\n        max_sum\n\
        \    }\n}"
      racket: "define (max-subarray-sum nums k)\n  (let ((n (length nums))\n       \
        \ (max-sum -inf.0)\n        (prefix-sum 0)\n        (mp (make-hash)))\n    (hash-set!\
        \ mp 0 0)\n    (for ((i (range n)))\n      (set! prefix-sum (+ prefix-sum (list-ref\
        \ nums i)))\n      (let ((sum prefix-sum))\n        (if (hash-ref mp (modulo\
        \ (+ i 1) k) #f)\n            (set! sum (- sum (hash-ref mp (modulo (+ i 1)\
        \ k)))))\n        (set! max-sum (max max-sum sum))\n        (if (or (not (hash-ref\
        \ mp (modulo (+ i 1) k) #f))\n                (< (hash-ref mp (modulo (+ i 1)\
        \ k)) prefix-sum))\n            (hash-set! mp (modulo (+ i 1) k) prefix-sum))))\n\
        \    max-sum)"
      erlang: "max_subarray_sum(Nums, K) ->\n    MaxSum = -1000000000,\n    PrefixSum\
        \ = 0,\n    Mp = #{0 => 0},\n    max_subarray_sum(Nums, K, MaxSum, PrefixSum,\
        \ Mp, 0).\nmax_subarray_sum([H|T], K, MaxSum, PrefixSum, Mp, I) ->\n    NewPrefixSum\
        \ = PrefixSum + H,\n    Sum = NewPrefixSum,\n    case maps:get((I+1) rem K,\
        \ Mp, undefined) of\n        undefined -> ok;\n        Val -> Sum = Sum - Val\n\
        \    end,\n    NewMaxSum = max(MaxSum, Sum),\n    case maps:get((I+1) rem K,\
        \ Mp, undefined) of\n        undefined -> NewMp = Mp#{(I+1) rem K => NewPrefixSum};\n\
        \        Val when Val < NewPrefixSum -> NewMp = Mp#{(I+1) rem K => NewPrefixSum};\n\
        \        _ -> NewMp = Mp\n    end,\n    max_subarray_sum(T, K, NewMaxSum, NewPrefixSum,\
        \ NewMp, I+1);\nmax_subarray_sum([], _, MaxSum, _, _, _) -> MaxSum."
      elixir: "defmodule Solution do\n  def max_subarray_sum(nums, k) do\n    n = length(nums)\n\
        \    max_sum = -1000000000\n    prefix_sum = 0\n    mp = %{0 => 0}\n    max_subarray_sum(nums,\
        \ k, max_sum, prefix_sum, mp, 0)\n  end\n  defp max_subarray_sum([h|t], k, max_sum,\
        \ prefix_sum, mp, i) do\n    new_prefix_sum = prefix_sum + h\n    sum = new_prefix_sum\n\
        \    if Map.get(mp, (i+1) |> rem(k), nil) do\n      sum = sum - Map.get(mp,\
        \ (i+1) |> rem(k))\n    end\n    new_max_sum = max(max_sum, sum)\n    if !Map.has_key?(mp,\
        \ (i+1) |> rem(k)) or Map.get(mp, (i+1) |> rem(k)) < new_prefix_sum do\n   \
        \   new_mp = Map.put(mp, (i+1) |> rem(k), new_prefix_sum)\n    else\n      new_mp\
        \ = mp\n    end\n    max_subarray_sum(t, k, new_max_sum, new_prefix_sum, new_mp,\
        \ i+1)\n  end\n  defp max_subarray_sum([], _, max_sum, _, _, _) do\n    max_sum\n\
        \  end\nend"
    approach: 'The algorithm works by maintaining a prefix sum array and then using
      Kadane''s algorithm to find the maximum sum subarray with length divisible by
      k. The key intuition is to consider all possible subarrays and check if their
      length is divisible by k. We can use the prefix sum array to efficiently calculate
      the sum of any subarray in O(1) time. We also maintain a variable to store the
      maximum sum found so far.


      The algorithm iterates over the prefix sum array and for each element, it checks
      all possible subarrays ending at that index. If the length of the subarray is
      divisible by k, it calculates the sum of the subarray using the prefix sum array
      and updates the maximum sum if necessary. This approach ensures that we consider
      all possible subarrays and find the maximum sum subarray with length divisible
      by k in O(n^2) time. However, we can optimize this approach by using Kadane''s
      algorithm to find the maximum sum subarray in O(n) time, resulting in an overall
      time complexity of O(n).'
    time_complexity: The time complexity of the algorithm is O(n) where n is the length
      of the input array. This is because we iterate over the array once to calculate
      the prefix sum and then use Kadane's algorithm to find the maximum sum subarray
      in O(n) time. The space complexity is also O(n) as we need to store the prefix
      sum array and the maximum sum variable.
    space_complexity: The space complexity of the algorithm is O(n) where n is the length
      of the input array. This is because we need to store the prefix sum array which
      requires O(n) space. We also need to store the maximum sum variable which requires
      O(1) space. However, the overall space complexity is dominated by the prefix sum
      array, resulting in a space complexity of O(n).
    elapsed_time: 9.409517049789429
    model: llama-3.3-70b-versatile
    generated_at: '2025-11-27 01:04:08 '
---

## Problem #3381: Maximum Subarray Sum With Length Divisible by K

**Difficulty:** Medium

**Topics:** Array, Hash Table, Prefix Sum

## Problem Description

<p>You are given an array of integers <code>nums</code> and an integer <code>k</code>.</p>

<p>Return the <strong>maximum</strong> sum of a <span data-keyword="subarray-nonempty">subarray</span> of <code>nums</code>, such that the size of the subarray is <strong>divisible</strong> by <code>k</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>The subarray <code>[1, 2]</code> with sum 3 has length equal to 2 which is divisible by 1.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [-1,-2,-3,-4,-5], k = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">-10</span></p>

<p><strong>Explanation:</strong></p>

<p>The maximum sum subarray is <code>[-1, -2, -3, -4]</code> which has length equal to 4 which is divisible by 4.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [-5,1,2,-3,4], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The maximum sum subarray is <code>[1, 2, -3, 4]</code> which has length equal to 4 which is divisible by 2.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. Maintain minimum prefix sum ending at every possible `index%k`.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-27 01:03:58 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks for the maximum sum of a subarray whose length is divisible by `k`. We can solve this using prefix sums and dynamic programming. Let `P[x]` denote the prefix sum of `nums` up to index `x-1`, with `P[0] = 0`. The sum of a subarray `nums[i...j]` is `P[j+1] - P[i]`. The length of this subarray is `(j+1) - i`. We are interested in subarrays where `((j+1) - i) % k == 0`, which implies `(j+1) % k == i % k`.

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-cpp-gemini-2-5-flash" checked>
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-java-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python3-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-c-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-csharp-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-javascript-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-typescript-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-php-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-swift-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-kotlin-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-dart-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-go-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-ruby-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-scala-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-rust-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-racket-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-erlang-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-elixir-gemini-2-5-flash">
  <div class="tab-labels">
    <label for="lang-cpp-gemini-2-5-flash">C++</label>
    <label for="lang-java-gemini-2-5-flash">Java</label>
    <label for="lang-python-gemini-2-5-flash">Python</label>
    <label for="lang-python3-gemini-2-5-flash">Python3</label>
    <label for="lang-c-gemini-2-5-flash">C</label>
    <label for="lang-csharp-gemini-2-5-flash">C#</label>
    <label for="lang-javascript-gemini-2-5-flash">JavaScript</label>
    <label for="lang-typescript-gemini-2-5-flash">TypeScript</label>
    <label for="lang-php-gemini-2-5-flash">PHP</label>
    <label for="lang-swift-gemini-2-5-flash">Swift</label>
    <label for="lang-kotlin-gemini-2-5-flash">Kotlin</label>
    <label for="lang-dart-gemini-2-5-flash">Dart</label>
    <label for="lang-go-gemini-2-5-flash">Go</label>
    <label for="lang-ruby-gemini-2-5-flash">Ruby</label>
    <label for="lang-scala-gemini-2-5-flash">Scala</label>
    <label for="lang-rust-gemini-2-5-flash">Rust</label>
    <label for="lang-racket-gemini-2-5-flash">Racket</label>
    <label for="lang-erlang-gemini-2-5-flash">Erlang</label>
    <label for="lang-elixir-gemini-2-5-flash">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
class Solution {
public:
    long long maxSubarraySum(std::vector<int>& nums, int k) {
        int n = nums.size();

        std::vector<long long> dp(k, std::numeric_limits<long long>::max());
        dp[0] = 0; 

        long long current_prefix_sum = 0;
        long long max_subarray_sum = std::numeric_limits<long long>::min(); 

        for (int j = 0; j < n; ++j) {
            current_prefix_sum += nums[j];

            int remainder = (j + 1) % k;

            if (dp[remainder] != std::numeric_limits<long long>::max()) {
                max_subarray_sum = std::max(max_subarray_sum, current_prefix_sum - dp[remainder]);
            }

            dp[remainder] = std::min(dp[remainder], current_prefix_sum);
        }

        return max_subarray_sum;
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
    public long maxSubarraySum(int[] nums, int k) {
        int n = nums.length;

        long[] dp = new long[k];
        Arrays.fill(dp, Long.MAX_VALUE);
        dp[0] = 0; 

        long currentPrefixSum = 0;
        long maxSubarraySum = Long.MIN_VALUE; 

        for (int j = 0; j < n; ++j) {
            currentPrefixSum += nums[j];

            int remainder = (j + 1) % k;

            if (dp[remainder] != Long.MAX_VALUE) {
                maxSubarraySum = Math.max(maxSubarraySum, currentPrefixSum - dp[remainder]);
            }

            dp[remainder] = Math.min(dp[remainder], currentPrefixSum);
        }

        return maxSubarraySum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import math

class Solution:
    def maxSubarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)

        dp = [math.inf] * k
        dp[0] = 0 

        current_prefix_sum = 0
        max_subarray_sum = -math.inf 

        for j in range(n):
            current_prefix_sum += nums[j]

            remainder = (j + 1) % k

            if dp[remainder] != math.inf:
                max_subarray_sum = max(max_subarray_sum, current_prefix_sum - dp[remainder])

            dp[remainder] = min(dp[remainder], current_prefix_sum)

        return max_subarray_sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import math

class Solution:
    def maxSubarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)

        dp = [math.inf] * k
        dp[0] = 0 

        current_prefix_sum = 0
        max_subarray_sum = -math.inf 

        for j in range(n):
            current_prefix_sum += nums[j]

            remainder = (j + 1) % k

            if dp[remainder] != math.inf:
                max_subarray_sum = max(max_subarray_sum, current_prefix_sum - dp[remainder])

            dp[remainder] = min(dp[remainder], current_prefix_sum)

        return max_subarray_sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <limits.h>

long long max(long long a, long long b) {
    return a > b ? a : b;
}

long long min(long long a, long long b) {
    return a < b ? a : b;
}

long long maxSubarraySum(int* nums, int numsSize, int k) {
    long long* dp = (long long*) malloc(k * sizeof(long long));
    if (dp == NULL) {
        return 0; 
    }

    for (int i = 0; i < k; ++i) {
        dp[i] = LLONG_MAX;
    }
    dp[0] = 0; 

    long long currentPrefixSum = 0;
    long long maxSubarraySum = LLONG_MIN; 

    for (int j = 0; j < numsSize; ++j) {
        currentPrefixSum += nums[j];

        int remainder = (j + 1) % k;

        if (dp[remainder] != LLONG_MAX) {
            maxSubarraySum = max(maxSubarraySum, currentPrefixSum - dp[remainder]);
        }

        dp[remainder] = min(dp[remainder], currentPrefixSum);
    }

    free(dp); 
    return maxSubarraySum;
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
    public long MaxSubarraySum(int[] nums, int k) {
        int n = nums.Length;

        long[] dp = new long[k];
        Array.Fill(dp, long.MaxValue);
        dp[0] = 0; 

        long currentPrefixSum = 0;
        long maxSubarraySum = long.MinValue; 

        for (int j = 0; j < n; ++j) {
            currentPrefixSum += nums[j];

            int remainder = (j + 1) % k;

            if (dp[remainder] != long.MaxValue) {
                maxSubarraySum = Math.Max(maxSubarraySum, currentPrefixSum - dp[remainder]);
            }

            dp[remainder] = Math.Min(dp[remainder], currentPrefixSum);
        }

        return maxSubarraySum;
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
 * @param {number} k
 * @return {number}
 */
var maxSubarraySum = function(nums, k) {
    const n = nums.length;

    const dp = new Array(k).fill(Number.MAX_SAFE_INTEGER); 
    dp[0] = 0; 

    let currentPrefixSum = 0;
    let maxSubarraySum = -Number.MAX_SAFE_INTEGER; 

    for (let j = 0; j < n; ++j) {
        currentPrefixSum += nums[j];

        const remainder = (j + 1) % k;

        if (dp[remainder] !== Number.MAX_SAFE_INTEGER) {
            maxSubarraySum = Math.max(maxSubarraySum, currentPrefixSum - dp[remainder]);
        }

        dp[remainder] = Math.min(dp[remainder], currentPrefixSum);
    }

    return maxSubarraySum;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxSubarraySum(nums: number[], k: number): number {
    const n = nums.length;

    const dp: number[] = new Array(k).fill(Number.MAX_SAFE_INTEGER);
    dp[0] = 0; 

    let currentPrefixSum: number = 0;
    let maxSubarraySum: number = -Number.MAX_SAFE_INTEGER; 

    for (let j = 0; j < n; ++j) {
        currentPrefixSum += nums[j];

        const remainder: number = (j + 1) % k;

        if (dp[remainder] !== Number.MAX_SAFE_INTEGER) {
            maxSubarraySum = Math.max(maxSubarraySum, currentPrefixSum - dp[remainder]);
        }

        dp[remainder] = Math.min(dp[remainder], currentPrefixSum);
    }

    return maxSubarraySum;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    /**
     * @param int[] $nums
     * @param int $k
     * @return int
     */
    function maxSubarraySum(array $nums, int $k): int {
        $n = count($nums);

        $dp = array_fill(0, $k, PHP_INT_MAX);
        $dp[0] = 0; 

        $currentPrefixSum = 0;
        $maxSubarraySum = PHP_INT_MIN; 

        for ($j = 0; $j < $n; ++$j) {
            $currentPrefixSum += $nums[$j];

            $remainder = ($j + 1) % $k;

            if ($dp[$remainder] !== PHP_INT_MAX) {
                $maxSubarraySum = max($maxSubarraySum, $currentPrefixSum - $dp[$remainder]);
            }

            $dp[$remainder] = min($dp[$remainder], $currentPrefixSum);
        }

        return $maxSubarraySum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
import Foundation

class Solution {
    func maxSubarraySum(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count

        var dp = Array(repeating: Int.max, count: k)
        dp[0] = 0 

        var currentPrefixSum: Int = 0
        var maxSubarraySum: Int = Int.min 

        for j in 0..<n {
            currentPrefixSum += nums[j]

            let remainder = (j + 1) % k

            if dp[remainder] != Int.max {
                maxSubarraySum = max(maxSubarraySum, currentPrefixSum - dp[remainder])
            }

            dp[remainder] = min(dp[remainder], currentPrefixSum)
        }

        return maxSubarraySum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import kotlin.math.max
import kotlin.math.min

class Solution {
    fun maxSubarraySum(nums: IntArray, k: Int): Long {
        val n = nums.size

        val dp = LongArray(k) { Long.MAX_VALUE }
        dp[0] = 0L 

        var currentPrefixSum: Long = 0L
        var maxSubarraySum: Long = Long.MIN_VALUE 

        for (j in 0 until n) {
            currentPrefixSum += nums[j]

            val remainder = (j + 1) % k

            if (dp[remainder] != Long.MAX_VALUE) {
                maxSubarraySum = max(maxSubarraySum, currentPrefixSum - dp[remainder])
            }

            dp[remainder] = min(dp[remainder], currentPrefixSum)
        }

        return maxSubarraySum
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
  int maxSubarraySum(List<int> nums, int k) {
    final n = nums.length;

    final dp = List<int>.filled(k, 9223372036854775807); 
    dp[0] = 0; 

    int currentPrefixSum = 0;
    int maxSubarraySum = -9223372036854775808; 

    for (int j = 0; j < n; ++j) {
      currentPrefixSum += nums[j];

      final remainder = (j + 1) % k;

      if (dp[remainder] != 9223372036854775807) {
        maxSubarraySum = max(maxSubarraySum, currentPrefixSum - dp[remainder]);
      }

      dp[remainder] = min(dp[remainder], currentPrefixSum);
    }

    return maxSubarraySum;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

import (
	"math"
)

func maxSubarraySum(nums []int, k int) int64 {
	n := len(nums)

	dp := make([]int64, k)
	for i := range dp {
		dp[i] = math.MaxInt64
	}
	dp[0] = 0 

	var currentPrefixSum int64 = 0
	var maxSubarraySum int64 = math.MinInt64 

	for j := 0; j < n; j++ {
		currentPrefixSum += int64(nums[j])

		remainder := (j + 1) % k

		if dp[remainder] != math.MaxInt64 {
			maxSubarraySum = max(maxSubarraySum, currentPrefixSum - dp[remainder])
		}

		dp[remainder] = min(dp[remainder], currentPrefixSum)
	}

	return maxSubarraySum
}

func max(a, b int64) int64 {
	if a > b {
		return a
	}
	return b
}

func min(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    # @param {Integer[]} nums
    # @param {Integer} k
    # @return {Integer}
    def max_subarray_sum(nums, k)
        n = nums.length

        dp = Array.new(k, Float::INFINITY)
        dp[0] = 0 

        current_prefix_sum = 0
        max_subarray_sum = -Float::INFINITY 

        for j in 0...n
            current_prefix_sum += nums[j]

            remainder = (j + 1) % k

            if dp[remainder] != Float::INFINITY
                max_subarray_sum = [max_subarray_sum, current_prefix_sum - dp[remainder]].max
            end

            dp[remainder] = [dp[remainder], current_prefix_sum].min
        end

        return max_subarray_sum
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable.ArrayBuffer
import scala.math.{max, min}

object Solution {
    def maxSubarraySum(nums: Array[Int], k: Int): Long = {
        val n = nums.length

        val dp = Array.fill[Long](k)(Long.MaxValue)
        dp(0) = 0L 

        var currentPrefixSum: Long = 0L
        var maxSubarraySum: Long = Long.MinValue 

        for (j <- 0 until n) {
            currentPrefixSum += nums(j)

            val remainder = (j + 1) % k

            if (dp(remainder) != Long.MaxValue) {
                maxSubarraySum = max(maxSubarraySum, currentPrefixSum - dp(remainder))
            }

            dp(remainder) = min(dp(remainder), currentPrefixSum)
        }

        return maxSubarraySum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::cmp::{max, min};

impl Solution {
    pub fn max_subarray_sum(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let k_usize = k as usize;

        let mut dp: Vec<i64> = vec![std::i64::MAX; k_usize];
        dp[0] = 0; 

        let mut current_prefix_sum: i64 = 0;
        let mut max_subarray_sum: i64 = std::i64::MIN; 

        for j in 0..n {
            current_prefix_sum += nums[j] as i64;

            let remainder = ((j + 1) as i32 % k) as usize;

            if dp[remainder] != std::i64::MAX {
                max_subarray_sum = max(max_subarray_sum, current_prefix_sum - dp[remainder]);
            }

            dp[remainder] = min(dp[remainder], current_prefix_sum);
        }

        max_subarray_sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (max-subarray-sum nums k)
  (define n (vector-length nums))

  (define dp (make-vector k +inf.0)) 
  (vector-set! dp 0 0) 

  (define current-prefix-sum (box 0))
  (define max-subarray-sum (box -inf.0)) 

  (for ([j (in-range n)])
    (set-box! current-prefix-sum (+ (unbox current-prefix-sum) (vector-ref nums j)))

    (define remainder (modulo (+ j 1) k))

    (when (not (eq? (vector-ref dp remainder) +inf.0))
      (set-box! max-subarray-sum
                (max (unbox max-subarray-sum) (- (unbox current-prefix-sum) (vector-ref dp remainder)))))

    (vector-set! dp remainder (min (vector-ref dp remainder) (unbox current-prefix-sum))))

  (unbox max-subarray-sum))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([max_subarray_sum/2]).

max(A, B) when A > B -> A;
max(A, B) -> B.

min(A, B) when A < B -> A;
min(A, B) -> B.

max_subarray_sum(Nums, K) ->
    N = length(Nums),

    Infinity = 1000000000000000000, 
    NegInfinity = -1000000000000000000,

    Dp = array:new(K, {default, Infinity}),
    Dp1 = array:set(0, 0, Dp), 

    max_subarray_sum_recursive(Nums, K, 0, 0, Dp1, NegInfinity).

max_subarray_sum_recursive(Nums, K, J, CurrentPrefixSum, Dp, MaxSubarraySum) ->
    if J < length(Nums) ->
        Num = lists:nth(J + 1, Nums), 
        NewPrefixSum = CurrentPrefixSum + Num,

        Remainder = (J + 1) rem K,

        DpRemainderVal = array:get(Remainder, Dp),

        NewMaxSubarraySum = 
            if DpRemainderVal =/= Infinity ->
                max(MaxSubarraySum, NewPrefixSum - DpRemainderVal);
            true ->
                MaxSubarraySum
            end,

        NewDp = array:set(Remainder, min(DpRemainderVal, NewPrefixSum), Dp),

        max_subarray_sum_recursive(Nums, K, J + 1, NewPrefixSum, NewDp, NewMaxSubarraySum);
    true ->
        MaxSubarraySum
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_subarray_sum(nums :: [integer], k :: integer) :: integer
  def max_subarray_sum(nums, k) do
    n = length(nums)

    infinity = 1_000_000_000_000_000_000
    neg_infinity = -1_000_000_000_000_000_000

    dp = Map.new() |> Map.put(0, 0) 

    {_final_prefix_sum, final_max_sum, _final_dp} = 
      Enum.reduce(0..(n - 1), {0, neg_infinity, dp}, fn j, {current_prefix_sum, max_subarray_sum, current_dp} ->
        num = Enum.at(nums, j)
        new_prefix_sum = current_prefix_sum + num

        remainder = rem(j + 1, k)

        dp_remainder_val = Map.get(current_dp, remainder, infinity)

        new_max_subarray_sum =
          if dp_remainder_val != infinity do
            max(max_subarray_sum, new_prefix_sum - dp_remainder_val)
          else
            max_subarray_sum
          end

        new_dp = Map.put(current_dp, remainder, min(dp_remainder_val, new_prefix_sum))

        {new_prefix_sum, new_max_subarray_sum, new_dp}
      end)

    final_max_sum
  end

  defp max(a, b), do: if a > b, do: a, else: b
  defp min(a, b), do: if a < b, do: a, else: b
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N), where N is the length of the `nums` array. We iterate through the `nums` array once, performing constant-time operations (arithmetic, array/map access) in each step. For languages using hash maps (like Elixir, Erlang with maps) for `dp`, the map operations take O(log k) time, leading to an O(N log k) complexity. Given `k <= N`, this is effectively O(N log N), which is acceptable for the given constraints.

- **Space Complexity:** The space complexity is O(k). We use a `dp` array (or map) of size `k` to store the minimum prefix sum encountered for each possible remainder modulo `k`. This space is directly proportional to `k`.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-27 01:04:08 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The algorithm works by maintaining a prefix sum array and then using Kadane's algorithm to find the maximum sum subarray with length divisible by k. The key intuition is to consider all possible subarrays and check if their length is divisible by k. We can use the prefix sum array to efficiently calculate the sum of any subarray in O(1) time. We also maintain a variable to store the maximum sum found so far.

The algorithm iterates over the prefix sum array and for each element, it checks all possible subarrays ending at that index. If the length of the subarray is divisible by k, it calculates the sum of the subarray using the prefix sum array and updates the maximum sum if necessary. This approach ensures that we consider all possible subarrays and find the maximum sum subarray with length divisible by k in O(n^2) time. However, we can optimize this approach by using Kadane's algorithm to find the maximum sum subarray in O(n) time, resulting in an overall time complexity of O(n).

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-cpp-llama-3-3-70b-versatile" checked>
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-java-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-python-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-python3-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-c-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-csharp-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-javascript-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-typescript-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-php-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-swift-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-kotlin-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-dart-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-go-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-ruby-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-scala-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-rust-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-racket-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-erlang-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-elixir-llama-3-3-70b-versatile">
  <div class="tab-labels">
    <label for="lang-cpp-llama-3-3-70b-versatile">C++</label>
    <label for="lang-java-llama-3-3-70b-versatile">Java</label>
    <label for="lang-python-llama-3-3-70b-versatile">Python</label>
    <label for="lang-python3-llama-3-3-70b-versatile">Python3</label>
    <label for="lang-c-llama-3-3-70b-versatile">C</label>
    <label for="lang-csharp-llama-3-3-70b-versatile">C#</label>
    <label for="lang-javascript-llama-3-3-70b-versatile">JavaScript</label>
    <label for="lang-typescript-llama-3-3-70b-versatile">TypeScript</label>
    <label for="lang-php-llama-3-3-70b-versatile">PHP</label>
    <label for="lang-swift-llama-3-3-70b-versatile">Swift</label>
    <label for="lang-kotlin-llama-3-3-70b-versatile">Kotlin</label>
    <label for="lang-dart-llama-3-3-70b-versatile">Dart</label>
    <label for="lang-go-llama-3-3-70b-versatile">Go</label>
    <label for="lang-ruby-llama-3-3-70b-versatile">Ruby</label>
    <label for="lang-scala-llama-3-3-70b-versatile">Scala</label>
    <label for="lang-rust-llama-3-3-70b-versatile">Rust</label>
    <label for="lang-racket-llama-3-3-70b-versatile">Racket</label>
    <label for="lang-erlang-llama-3-3-70b-versatile">Erlang</label>
    <label for="lang-elixir-llama-3-3-70b-versatile">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
class Solution {
public:
    long long maxSubarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        long long max_sum = LLONG_MIN;
        long long prefix_sum = 0;
        unordered_map<int, long long> mp;
        mp[0] = 0;
        for (int i = 0; i < n; i++) {
            prefix_sum += nums[i];
            long long sum = prefix_sum;
            if (mp.find((i + 1) % k) != mp.end()) {
                sum -= mp[(i + 1) % k];
            }
            max_sum = max(max_sum, sum);
            if (mp.find((i + 1) % k) == mp.end() || mp[(i + 1) % k] < prefix_sum) {
                mp[(i + 1) % k] = prefix_sum;
            }
        }
        return max_sum;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public long maxSubarraySum(int[] nums, int k) {
        int n = nums.length;
        long max_sum = Long.MIN_VALUE;
        long prefix_sum = 0;
        HashMap<Integer, Long> mp = new HashMap<>();
        mp.put(0, 0L);
        for (int i = 0; i < n; i++) {
            prefix_sum += nums[i];
            long sum = prefix_sum;
            if (mp.containsKey((i + 1) % k)) {
                sum -= mp.get((i + 1) % k);
            }
            max_sum = Math.max(max_sum, sum);
            if (!mp.containsKey((i + 1) % k) || mp.get((i + 1) % k) < prefix_sum) {
                mp.put((i + 1) % k, prefix_sum);
            }
        }
        return max_sum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def maxSubarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_sum = float('-inf')
        prefix_sum = 0
        mp = {0: 0}
        for i in range(n):
            prefix_sum += nums[i]
            sum_ = prefix_sum
            if (i + 1) % k in mp:
                sum_ -= mp[(i + 1) % k]
            max_sum = max(max_sum, sum_)
            if (i + 1) % k not in mp or mp[(i + 1) % k] < prefix_sum:
                mp[(i + 1) % k] = prefix_sum
        return max_sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxSubarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_sum = float('-inf')
        prefix_sum = 0
        mp = {0: 0}
        for i in range(n):
            prefix_sum += nums[i]
            sum_ = prefix_sum
            if (i + 1) % k in mp:
                sum_ -= mp[(i + 1) % k]
            max_sum = max(max_sum, sum_)
            if (i + 1) % k not in mp or mp[(i + 1) % k] < prefix_sum:
                mp[(i + 1) % k] = prefix_sum
        return max_sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
typedef long long ll;
struct Solution {
    ll maxSubarraySum(int* nums, int numsSize, int k) {
        ll max_sum = LLONG_MIN;
        ll prefix_sum = 0;
        int* mp = (int*)malloc((k + 1) * sizeof(int));
        for (int i = 0; i <= k; i++) {
            mp[i] = INT_MIN;
        }
        mp[0] = 0;
        for (int i = 0; i < numsSize; i++) {
            prefix_sum += nums[i];
            ll sum = prefix_sum;
            if (mp[(i + 1) % k] != INT_MIN) {
                sum -= mp[(i + 1) % k];
            }
            max_sum = (max_sum > sum) ? max_sum : sum;
            if (mp[(i + 1) % k] < prefix_sum) {
                mp[(i + 1) % k] = prefix_sum;
            }
        }
        free(mp);
        return max_sum;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public long MaxSubarraySum(int[] nums, int k) {
        int n = nums.Length;
        long max_sum = long.MinValue;
        long prefix_sum = 0;
        Dictionary<int, long> mp = new Dictionary<int, long>();
        mp[0] = 0;
        for (int i = 0; i < n; i++) {
            prefix_sum += nums[i];
            long sum = prefix_sum;
            if (mp.ContainsKey((i + 1) % k)) {
                sum -= mp[(i + 1) % k];
            }
            max_sum = Math.Max(max_sum, sum);
            if (!mp.ContainsKey((i + 1) % k) || mp[(i + 1) % k] < prefix_sum) {
                mp[(i + 1) % k] = prefix_sum;
            }
        }
        return max_sum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var maxSubarraySum = function(nums, k) {
    let n = nums.length;
    let max_sum = -Infinity;
    let prefix_sum = 0;
    let mp = {0: 0};
    for (let i = 0; i < n; i++) {
        prefix_sum += nums[i];
        let sum = prefix_sum;
        if ((i + 1) % k in mp) {
            sum -= mp[(i + 1) % k];
        }
        max_sum = Math.max(max_sum, sum);
        if (!(i + 1) % k in mp || mp[(i + 1) % k] < prefix_sum) {
            mp[(i + 1) % k] = prefix_sum;
        }
    }
    return max_sum;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxSubarraySum(nums: number[], k: number): number {
    let n = nums.length;
    let max_sum = -Infinity;
    let prefix_sum = 0;
    let mp: { [key: number]: number } = {0: 0};
    for (let i = 0; i < n; i++) {
        prefix_sum += nums[i];
        let sum = prefix_sum;
        if ((i + 1) % k in mp) {
            sum -= mp[(i + 1) % k];
        }
        max_sum = Math.max(max_sum, sum);
        if (!(i + 1) % k in mp || mp[(i + 1) % k] < prefix_sum) {
            mp[(i + 1) % k] = prefix_sum;
        }
    }
    return max_sum;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function maxSubarraySum($nums, $k) {
        $n = count($nums);
        $max_sum = -INF;
        $prefix_sum = 0;
        $mp = array(0 => 0);
        for ($i = 0; $i < $n; $i++) {
            $prefix_sum += $nums[$i];
            $sum = $prefix_sum;
            if (array_key_exists(($i + 1) % $k, $mp)) {
                $sum -= $mp[($i + 1) % $k];
            }
            $max_sum = max($max_sum, $sum);
            if (!array_key_exists(($i + 1) % $k, $mp) || $mp[($i + 1) % $k] < $prefix_sum) {
                $mp[($i + 1) % $k] = $prefix_sum;
            }
        }
        return $max_sum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxSubarraySum(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var max_sum = Int.min
        var prefix_sum = 0
        var mp: [Int: Int] = [0: 0]
        for i in 0..<n {
            prefix_sum += nums[i]
            var sum = prefix_sum
            if let val = mp[(i + 1) % k] {
                sum -= val
            }
            max_sum = max(max_sum, sum)
            if mp[(i + 1) % k] == nil || mp[(i + 1) % k]! < prefix_sum {
                mp[(i + 1) % k] = prefix_sum
            }
        }
        return max_sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxSubarraySum(nums: IntArray, k: Int): Long {
        val n = nums.size
        var max_sum = Long.MIN_VALUE
        var prefix_sum = 0L
        val mp = mutableMapOf<Int, Long>()
        mp[0] = 0
        for (i in 0 until n) {
            prefix_sum += nums[i]
            var sum = prefix_sum
            if (mp.containsKey((i + 1) % k)) {
                sum -= mp[(i + 1) % k]!!
            }
            max_sum = maxOf(max_sum, sum)
            if (!mp.containsKey((i + 1) % k) || mp[(i + 1) % k]!! < prefix_sum) {
                mp[(i + 1) % k] = prefix_sum
            }
        }
        return max_sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int maxSubarraySum(List<int> nums, int k) {
        int n = nums.length;
        int max_sum = -1000000000;
        int prefix_sum = 0;
        Map<int, int> mp = {0: 0};
        for (int i = 0; i < n; i++) {
            prefix_sum += nums[i];
            int sum = prefix_sum;
            if (mp.containsKey((i + 1) % k)) {
                sum -= mp[(i + 1) % k]!;
            }
            max_sum = max(max_sum, sum);
            if (!mp.containsKey((i + 1) % k) || mp[(i + 1) % k]! < prefix_sum) {
                mp[(i + 1) % k] = prefix_sum;
            }
        }
        return max_sum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxSubarraySum(nums []int, k int) int64 {
    n := len(nums)
    max_sum := int64(math.MinInt64)
    prefix_sum := int64(0)
    mp := make(map[int]int64)
    mp[0] = 0
    for i := 0; i < n; i++ {
        prefix_sum += int64(nums[i])
        sum := prefix_sum
        if val, ok := mp[(i+1)%k]; ok {
            sum -= val
        }
        max_sum = max(max_sum, sum)
        if _, ok := mp[(i+1)%k]; !ok || mp[(i+1)%k] < prefix_sum {
            mp[(i+1)%k] = prefix_sum
        }
    }
    return max_sum
}
func max(a, b int64) int64 {
    if a > b {
        return a
    }
    return b
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    def max_subarray_sum(nums, k)
        n = nums.size
        max_sum = -10**9
        prefix_sum = 0
        mp = {0 => 0}
        for i in 0...n
            prefix_sum += nums[i]
            sum = prefix_sum
            if mp.key?((i + 1) % k)
                sum -= mp[(i + 1) % k]
            end
            max_sum = [max_sum, sum].max
            if !mp.key?((i + 1) % k) || mp[(i + 1) % k] < prefix_sum
                mp[(i + 1) % k] = prefix_sum
            end
        end
        max_sum
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxSubarraySum(nums: Array[Int], k: Int): Long = {
        val n = nums.length
        var max_sum = Long.MinValue
        var prefix_sum = 0L
        val mp = scala.collection.mutable.Map[Int, Long]()
        mp(0) = 0
        for (i <- 0 until n) {
            prefix_sum += nums(i)
            var sum = prefix_sum
            if (mp.contains((i + 1) % k)) {
                sum -= mp((i + 1) % k)
            }
            max_sum = math.max(max_sum, sum)
            if (!mp.contains((i + 1) % k) || mp((i + 1) % k) < prefix_sum) {
                mp((i + 1) % k) = prefix_sum
            }
        }
        max_sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
struct Solution;
impl Solution {
    pub fn max_subarray_sum(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len() as i32;
        let mut max_sum = std::i64::MIN;
        let mut prefix_sum = 0;
        let mut mp: std::collections::HashMap<i32, i64> = std::collections::HashMap::new();
        mp.insert(0, 0);
        for i in 0..n {
            prefix_sum += nums[i as usize] as i64;
            let mut sum = prefix_sum;
            if let Some(val) = mp.get(&((i + 1) % k)) {
                sum -= val;
            }
            max_sum = std::cmp::max(max_sum, sum);
            if !mp.contains_key(&((i + 1) % k)) || *mp.get(&((i + 1) % k)).unwrap() < prefix_sum {
                mp.insert((i + 1) % k, prefix_sum);
            }
        }
        max_sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
define (max-subarray-sum nums k)
  (let ((n (length nums))
        (max-sum -inf.0)
        (prefix-sum 0)
        (mp (make-hash)))
    (hash-set! mp 0 0)
    (for ((i (range n)))
      (set! prefix-sum (+ prefix-sum (list-ref nums i)))
      (let ((sum prefix-sum))
        (if (hash-ref mp (modulo (+ i 1) k) #f)
            (set! sum (- sum (hash-ref mp (modulo (+ i 1) k)))))
        (set! max-sum (max max-sum sum))
        (if (or (not (hash-ref mp (modulo (+ i 1) k) #f))
                (< (hash-ref mp (modulo (+ i 1) k)) prefix-sum))
            (hash-set! mp (modulo (+ i 1) k) prefix-sum))))
    max-sum)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
max_subarray_sum(Nums, K) ->
    MaxSum = -1000000000,
    PrefixSum = 0,
    Mp = #{0 => 0},
    max_subarray_sum(Nums, K, MaxSum, PrefixSum, Mp, 0).
max_subarray_sum([H|T], K, MaxSum, PrefixSum, Mp, I) ->
    NewPrefixSum = PrefixSum + H,
    Sum = NewPrefixSum,
    case maps:get((I+1) rem K, Mp, undefined) of
        undefined -> ok;
        Val -> Sum = Sum - Val
    end,
    NewMaxSum = max(MaxSum, Sum),
    case maps:get((I+1) rem K, Mp, undefined) of
        undefined -> NewMp = Mp#{(I+1) rem K => NewPrefixSum};
        Val when Val < NewPrefixSum -> NewMp = Mp#{(I+1) rem K => NewPrefixSum};
        _ -> NewMp = Mp
    end,
    max_subarray_sum(T, K, NewMaxSum, NewPrefixSum, NewMp, I+1);
max_subarray_sum([], _, MaxSum, _, _, _) -> MaxSum.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  def max_subarray_sum(nums, k) do
    n = length(nums)
    max_sum = -1000000000
    prefix_sum = 0
    mp = %{0 => 0}
    max_subarray_sum(nums, k, max_sum, prefix_sum, mp, 0)
  end
  defp max_subarray_sum([h|t], k, max_sum, prefix_sum, mp, i) do
    new_prefix_sum = prefix_sum + h
    sum = new_prefix_sum
    if Map.get(mp, (i+1) |> rem(k), nil) do
      sum = sum - Map.get(mp, (i+1) |> rem(k))
    end
    new_max_sum = max(max_sum, sum)
    if !Map.has_key?(mp, (i+1) |> rem(k)) or Map.get(mp, (i+1) |> rem(k)) < new_prefix_sum do
      new_mp = Map.put(mp, (i+1) |> rem(k), new_prefix_sum)
    else
      new_mp = mp
    end
    max_subarray_sum(t, k, new_max_sum, new_prefix_sum, new_mp, i+1)
  end
  defp max_subarray_sum([], _, max_sum, _, _, _) do
    max_sum
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of the algorithm is O(n) where n is the length of the input array. This is because we iterate over the array once to calculate the prefix sum and then use Kadane's algorithm to find the maximum sum subarray in O(n) time. The space complexity is also O(n) as we need to store the prefix sum array and the maximum sum variable.

- **Space Complexity:** The space complexity of the algorithm is O(n) where n is the length of the input array. This is because we need to store the prefix sum array which requires O(n) space. We also need to store the maximum sum variable which requires O(1) space. However, the overall space complexity is dominated by the prefix sum array, resulting in a space complexity of O(n).

</div>
</details>
