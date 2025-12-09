---
layout: post
title: "Count Special Triplets"
date: 2025-12-09 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Counting"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/count-special-triplets/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int specialTriplets(std::vector<int>& nums)\
        \ {\n        int n = nums.size();\n        long long total_triplets = 0;\n \
        \       long long MOD = 1e9 + 7;\n        int MAX_VAL = 200001; // Max nums[i]\
        \ is 10^5, so nums[j]*2 can be 2*10^5\n\n        std::vector<int> freq_prev(MAX_VAL,\
        \ 0);\n        std::vector<int> freq_next(MAX_VAL, 0);\n\n        for (int x\
        \ : nums) {\n            freq_next[x]++;\n        }\n\n        for (int j =\
        \ 0; j < n; ++j) {\n            freq_next[nums[j]]--;\n\n            long long\
        \ target_val = (long long)nums[j] * 2;\n\n            if (target_val < MAX_VAL)\
        \ {\n                long long count_i = freq_prev[target_val];\n          \
        \      long long count_k = freq_next[target_val];\n                total_triplets\
        \ = (total_triplets + (count_i * count_k) % MOD) % MOD;\n            }\n\n \
        \           freq_prev[nums[j]]++;\n        }\n\n        return static_cast<int>(total_triplets);\n\
        \    }\n};"
      java: "import java.util.List;\n\nclass Solution {\n    public int specialTriplets(List<Integer>\
        \ nums) {\n        int n = nums.size();\n        long totalTriplets = 0;\n \
        \       long MOD = 1_000_000_007;\n        int MAX_VAL = 200001; // Max nums[i]\
        \ is 10^5, so nums[j]*2 can be 2*10^5\n\n        int[] freqPrev = new int[MAX_VAL];\
        \ // Initialized to zeros by default\n        int[] freqNext = new int[MAX_VAL];\
        \ // Initialized to zeros by default\n\n        for (int x : nums) {\n     \
        \       freqNext[x]++;\n        }\n\n        for (int j = 0; j < n; ++j) {\n\
        \            int currentNum = nums.get(j);\n            freqNext[currentNum]--;\n\
        \n            long targetVal = (long)currentNum * 2;\n\n            if (targetVal\
        \ < MAX_VAL) {\n                long countI = freqPrev[(int)targetVal];\n  \
        \              long countK = freqNext[(int)targetVal];\n                totalTriplets\
        \ = (totalTriplets + (countI * countK) % MOD) % MOD;\n            }\n\n    \
        \        freqPrev[currentNum]++;\n        }\n\n        return (int)totalTriplets;\n\
        \    }\n}"
      python: "class Solution:\n    def specialTriplets(self, nums: List[int]) -> int:\n\
        \        n = len(nums)\n        total_triplets = 0\n        MOD = 10**9 + 7\n\
        \        MAX_VAL = 200001  # Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5\n\
        \n        freq_prev = [0] * MAX_VAL\n        freq_next = [0] * MAX_VAL\n\n \
        \       for x in nums:\n            freq_next[x] += 1\n\n        for j in range(n):\n\
        \            current_num = nums[j]\n            freq_next[current_num] -= 1\n\
        \n            target_val = current_num * 2\n\n            if target_val < MAX_VAL:\n\
        \                count_i = freq_prev[target_val]\n                count_k =\
        \ freq_next[target_val]\n                total_triplets = (total_triplets +\
        \ (count_i * count_k) % MOD) % MOD\n\n            freq_prev[current_num] +=\
        \ 1\n\n        return total_triplets"
      python3: "class Solution:\n    def specialTriplets(self, nums: List[int]) -> int:\n\
        \        n = len(nums)\n        total_triplets = 0\n        MOD = 10**9 + 7\n\
        \        MAX_VAL = 200001  # Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5\n\
        \n        freq_prev = [0] * MAX_VAL\n        freq_next = [0] * MAX_VAL\n\n \
        \       for x in nums:\n            freq_next[x] += 1\n\n        for j in range(n):\n\
        \            current_num = nums[j]\n            freq_next[current_num] -= 1\n\
        \n            target_val = current_num * 2\n\n            if target_val < MAX_VAL:\n\
        \                count_i = freq_prev[target_val]\n                count_k =\
        \ freq_next[target_val]\n                total_triplets = (total_triplets +\
        \ (count_i * count_k) % MOD) % MOD\n\n            freq_prev[current_num] +=\
        \ 1\n\n        return total_triplets"
      c: "#include <stdlib.h>\n#include <string.h>\n\n#define MOD 1000000007\n#define\
        \ MAX_VAL 200001 // Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5\n\nint specialTriplets(int*\
        \ nums, int numsSize) {\n    long long total_triplets = 0;\n\n    int* freq_prev\
        \ = (int*)calloc(MAX_VAL, sizeof(int));\n    int* freq_next = (int*)calloc(MAX_VAL,\
        \ sizeof(int));\n\n    if (freq_prev == NULL || freq_next == NULL) {\n     \
        \   // Handle memory allocation failure\n        if (freq_prev) free(freq_prev);\n\
        \        if (freq_next) free(freq_next);\n        return 0; // Or throw an error,\
        \ depending on requirements\n    }\n\n    for (int i = 0; i < numsSize; ++i)\
        \ {\n        freq_next[nums[i]]++;\n    }\n\n    for (int j = 0; j < numsSize;\
        \ ++j) {\n        int current_num = nums[j];\n        freq_next[current_num]--;\n\
        \n        long long target_val = (long long)current_num * 2;\n\n        if (target_val\
        \ < MAX_VAL) {\n            long long count_i = freq_prev[target_val];\n   \
        \         long long count_k = freq_next[target_val];\n            total_triplets\
        \ = (total_triplets + (count_i * count_k) % MOD) % MOD;\n        }\n\n     \
        \   freq_prev[current_num]++;\n    }\n\n    free(freq_prev);\n    free(freq_next);\n\
        \n    return (int)total_triplets;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int SpecialTriplets(int[] nums) {\n        int n = nums.Length;\n\
        \        long totalTriplets = 0;\n        long MOD = 1_000_000_007;\n      \
        \  int MAX_VAL = 200001; // Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5\n\
        \n        int[] freqPrev = new int[MAX_VAL]; // Initialized to zeros by default\n\
        \        int[] freqNext = new int[MAX_VAL]; // Initialized to zeros by default\n\
        \n        foreach (int x in nums) {\n            freqNext[x]++;\n        }\n\
        \n        for (int j = 0; j < n; ++j) {\n            int currentNum = nums[j];\n\
        \            freqNext[currentNum]--;\n\n            long targetVal = (long)currentNum\
        \ * 2;\n\n            if (targetVal < MAX_VAL) {\n                long countI\
        \ = freqPrev[(int)targetVal];\n                long countK = freqNext[(int)targetVal];\n\
        \                totalTriplets = (totalTriplets + (countI * countK) % MOD) %\
        \ MOD;\n            }\n\n            freqPrev[currentNum]++;\n        }\n\n\
        \        return (int)totalTriplets;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar specialTriplets\
        \ = function(nums) {\n    const n = nums.length;\n    let totalTriplets = 0;\n\
        \    const MOD = 10**9 + 7;\n    const MAX_VAL = 200001; // Max nums[i] is 10^5,\
        \ so nums[j]*2 can be 2*10^5\n\n    const freqPrev = new Array(MAX_VAL).fill(0);\n\
        \    const freqNext = new Array(MAX_VAL).fill(0);\n\n    for (const x of nums)\
        \ {\n        freqNext[x]++;\n    }\n\n    for (let j = 0; j < n; ++j) {\n  \
        \      const currentNum = nums[j];\n        freqNext[currentNum]--;\n\n    \
        \    const targetVal = currentNum * 2;\n\n        if (targetVal < MAX_VAL) {\n\
        \            const countI = freqPrev[targetVal];\n            const countK =\
        \ freqNext[targetVal];\n            totalTriplets = (totalTriplets + (countI\
        \ * countK) % MOD) % MOD;\n        }\n\n        freqPrev[currentNum]++;\n  \
        \  }\n\n    return totalTriplets;\n};"
      typescript: "function specialTriplets(nums: number[]): number {\n    const n =\
        \ nums.length;\n    let totalTriplets = 0;\n    const MOD = 10**9 + 7;\n   \
        \ const MAX_VAL = 200001; // Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5\n\
        \n    const freqPrev: number[] = new Array(MAX_VAL).fill(0);\n    const freqNext:\
        \ number[] = new Array(MAX_VAL).fill(0);\n\n    for (const x of nums) {\n  \
        \      freqNext[x]++;\n    }\n\n    for (let j = 0; j < n; ++j) {\n        const\
        \ currentNum = nums[j];\n        freqNext[currentNum]--;\n\n        const targetVal\
        \ = currentNum * 2;\n\n        if (targetVal < MAX_VAL) {\n            const\
        \ countI = freqPrev[targetVal];\n            const countK = freqNext[targetVal];\n\
        \            totalTriplets = (totalTriplets + (countI * countK) % MOD) % MOD;\n\
        \        }\n\n        freqPrev[currentNum]++;\n    }\n\n    return totalTriplets;\n\
        }"
      php: "class Solution {\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function specialTriplets($nums) {\n        $n = count($nums);\n\
        \        $totalTriplets = 0;\n        $MOD = 10**9 + 7;\n        $MAX_VAL =\
        \ 200001; // Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5\n\n        $freqPrev\
        \ = array_fill(0, $MAX_VAL, 0);\n        $freqNext = array_fill(0, $MAX_VAL,\
        \ 0);\n\n        foreach ($nums as $x) {\n            $freqNext[$x]++;\n   \
        \     }\n\n        for ($j = 0; $j < $n; ++$j) {\n            $currentNum =\
        \ $nums[$j];\n            $freqNext[$currentNum]--;\n\n            $targetVal\
        \ = $currentNum * 2;\n\n            if ($targetVal < $MAX_VAL) {\n         \
        \       $countI = $freqPrev[$targetVal];\n                $countK = $freqNext[$targetVal];\n\
        \                $totalTriplets = ($totalTriplets + ($countI * $countK) % $MOD)\
        \ % $MOD;\n            }\n\n            $freqPrev[$currentNum]++;\n        }\n\
        \n        return $totalTriplets;\n    }\n}"
      swift: "class Solution {\n    func specialTriplets(_ nums: [Int]) -> Int {\n \
        \       let n = nums.count\n        var totalTriplets = 0\n        let MOD =\
        \ 1_000_000_007\n        let MAX_VAL = 200001 // Max nums[i] is 10^5, so nums[j]*2\
        \ can be 2*10^5\n\n        var freqPrev = Array(repeating: 0, count: MAX_VAL)\n\
        \        var freqNext = Array(repeating: 0, count: MAX_VAL)\n\n        for x\
        \ in nums {\n            freqNext[x] += 1\n        }\n\n        for j in 0..<n\
        \ {\n            let currentNum = nums[j]\n            freqNext[currentNum]\
        \ -= 1\n\n            let targetVal = currentNum * 2\n\n            if targetVal\
        \ < MAX_VAL {\n                let countI = freqPrev[targetVal]\n          \
        \      let countK = freqNext[targetVal]\n                totalTriplets = (totalTriplets\
        \ + (countI * countK) % MOD) % MOD\n            }\n\n            freqPrev[currentNum]\
        \ += 1\n        }\n\n        return totalTriplets\n    }\n}"
      kotlin: "class Solution {\n    fun specialTriplets(nums: List<Int>): Int {\n \
        \       val n = nums.size\n        var totalTriplets: Long = 0\n        val\
        \ MOD: Long = 1_000_000_007\n        val MAX_VAL = 200001 // Max nums[i] is\
        \ 10^5, so nums[j]*2 can be 2*10^5\n\n        val freqPrev = IntArray(MAX_VAL)\
        \ // Initialized to zeros by default\n        val freqNext = IntArray(MAX_VAL)\
        \ // Initialized to zeros by default\n\n        for (x in nums) {\n        \
        \    freqNext[x]++\n        }\n\n        for (j in 0 until n) {\n          \
        \  val currentNum = nums[j]\n            freqNext[currentNum]--\n\n        \
        \    val targetVal = currentNum * 2L // Use Long for multiplication to prevent\
        \ overflow\n\n            if (targetVal < MAX_VAL) {\n                val countI\
        \ = freqPrev[targetVal.toInt()].toLong()\n                val countK = freqNext[targetVal.toInt()].toLong()\n\
        \                totalTriplets = (totalTriplets + (countI * countK) % MOD) %\
        \ MOD\n            }\n\n            freqPrev[currentNum]++\n        }\n\n  \
        \      return totalTriplets.toInt()\n    }\n}"
      dart: "class Solution {\n  int specialTriplets(List<int> nums) {\n    final n\
        \ = nums.length;\n    int totalTriplets = 0;\n    final MOD = 1000000007;\n\
        \    final MAX_VAL = 200001; // Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5\n\
        \n    final freqPrev = List<int>.filled(MAX_VAL, 0);\n    final freqNext = List<int>.filled(MAX_VAL,\
        \ 0);\n\n    for (final x in nums) {\n      freqNext[x]++;\n    }\n\n    for\
        \ (var j = 0; j < n; ++j) {\n      final currentNum = nums[j];\n      freqNext[currentNum]--;\n\
        \n      final targetVal = currentNum * 2;\n\n      if (targetVal < MAX_VAL)\
        \ {\n        final countI = freqPrev[targetVal];\n        final countK = freqNext[targetVal];\n\
        \        totalTriplets = (totalTriplets + (countI * countK) % MOD) % MOD;\n\
        \      }\n\n      freqPrev[currentNum]++;\n    }\n\n    return totalTriplets;\n\
        \  }\n}"
      go: "package main\n\nfunc specialTriplets(nums []int) int {\n    n := len(nums)\n\
        \    var totalTriplets int64 = 0\n    const MOD int64 = 1e9 + 7\n    const MAX_VAL\
        \ int = 200001 // Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5\n\n    freqPrev\
        \ := make([]int, MAX_VAL)\n    freqNext := make([]int, MAX_VAL)\n\n    for _,\
        \ x := range nums {\n        freqNext[x]++\n    }\n\n    for j := 0; j < n;\
        \ j++ {\n        currentNum := nums[j]\n        freqNext[currentNum]--\n\n \
        \       targetVal := currentNum * 2\n\n        if targetVal < MAX_VAL {\n  \
        \          countI := int64(freqPrev[targetVal])\n            countK := int64(freqNext[targetVal])\n\
        \            totalTriplets = (totalTriplets + (countI * countK) % MOD) % MOD\n\
        \        }\n\n        freqPrev[currentNum]++\n    }\n\n    return int(totalTriplets)\n\
        }"
      ruby: "class Solution\n    def special_triplets(nums)\n        n = nums.length\n\
        \        total_triplets = 0\n        mod = 10**9 + 7\n        max_val = 200001\
        \ # Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5\n\n        freq_prev = Array.new(max_val,\
        \ 0)\n        freq_next = Array.new(max_val, 0)\n\n        nums.each do |x|\n\
        \            freq_next[x] += 1\n        end\n\n        (0...n).each do |j|\n\
        \            current_num = nums[j]\n            freq_next[current_num] -= 1\n\
        \n            target_val = current_num * 2\n\n            if target_val < max_val\n\
        \                count_i = freq_prev[target_val]\n                count_k =\
        \ freq_next[target_val]\n                total_triplets = (total_triplets +\
        \ (count_i * count_k) % mod) % mod\n            end\n\n            freq_prev[current_num]\
        \ += 1\n        end\n\n        total_triplets\n    end\nend"
      scala: "import scala.collection.mutable.ArrayBuffer\n\nobject Solution {\n   \
        \ def specialTriplets(nums: List[Int]): Int = {\n        val n = nums.length\n\
        \        var totalTriplets: Long = 0\n        val MOD: Long = 1_000_000_007\n\
        \        val MAX_VAL = 200001 // Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5\n\
        \n        val freqPrev = Array.fill(MAX_VAL)(0)\n        val freqNext = Array.fill(MAX_VAL)(0)\n\
        \n        for (x <- nums) {\n            freqNext(x) += 1\n        }\n\n   \
        \     for (j <- 0 until n) {\n            val currentNum = nums(j)\n       \
        \     freqNext(currentNum) -= 1\n\n            val targetVal = currentNum *\
        \ 2L // Use Long for multiplication to prevent overflow\n\n            if (targetVal\
        \ < MAX_VAL) {\n                val countI = freqPrev(targetVal.toInt).toLong\n\
        \                val countK = freqNext(targetVal.toInt).toLong\n           \
        \     totalTriplets = (totalTriplets + (countI * countK) % MOD) % MOD\n    \
        \        }\n\n            freqPrev(currentNum) += 1\n        }\n\n        totalTriplets.toInt\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn special_triplets(nums: Vec<i32>) -> i32 {\n\
        \        let n = nums.len();\n        let mut total_triplets: i64 = 0;\n   \
        \     let modular: i64 = 1_000_000_007;\n        let max_val = 200001; // Max\
        \ nums[i] is 10^5, so nums[j]*2 can be 2*10^5\n\n        let mut freq_prev =\
        \ vec![0; max_val];\n        let mut freq_next = vec![0; max_val];\n\n     \
        \   for &x in nums.iter() {\n            freq_next[x as usize] += 1;\n     \
        \   }\n\n        for j in 0..n {\n            let current_num = nums[j];\n \
        \           freq_next[current_num as usize] -= 1;\n\n            let target_val\
        \ = current_num as i64 * 2;\n\n            if target_val < max_val as i64 {\n\
        \                let count_i = freq_prev[target_val as usize] as i64;\n    \
        \            let count_k = freq_next[target_val as usize] as i64;\n        \
        \        total_triplets = (total_triplets + (count_i * count_k) % modular) %\
        \ modular;\n            }\n\n            freq_prev[current_num as usize] +=\
        \ 1;\n        }\n\n        total_triplets as i32\n    }\n}"
      racket: "#lang racket\n\n(define (special-triplets nums)\n  (define n (vector-length\
        \ nums))\n  (define mod 1000000007)\n  (define max-val 200001) ; Max nums[i]\
        \ is 10^5, so nums[j]*2 can be 2*10^5\n\n  (define freq-prev (make-vector max-val\
        \ 0))\n  (define freq-next (make-vector max-val 0))\n\n  ;; Populate freq-next\n\
        \  (for ([x (in-vector nums)])\n    (vector-set! freq-next x (+ (vector-ref\
        \ freq-next x) 1)))\n\n  (define total-triplets 0)\n\n  (for ([j (in-range n)])\n\
        \    (define current-num (vector-ref nums j))\n    (vector-set! freq-next current-num\
        \ (- (vector-ref freq-next current-num) 1))\n\n    (define target-val (* current-num\
        \ 2))\n\n    (when (< target-val max-val)\n      (define count-i (vector-ref\
        \ freq-prev target-val))\n      (define count-k (vector-ref freq-next target-val))\n\
        \      (set! total-triplets\n            (modulo (+ total-triplets (modulo (*\
        \ count-i count-k) mod)) mod)))\n\n    (vector-set! freq-prev current-num (+\
        \ (vector-ref freq-prev current-num) 1)))\n\n  total-triplets)"
      erlang: "-module(solution).\n-export([special_triplets/1]).\n\n-define(MOD, 1000000007).\n\
        -define(MAX_VAL, 200001). %% Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5\n\
        \nspecial_triplets(Nums) ->\n    %% Pre-populate FreqNext\n    FreqNext = lists:foldl(fun(X,\
        \ Acc) -> maps:update_with(X, fun(Val) -> Val + 1 end, 1, Acc) end, #{}, Nums),\n\
        \n    special_triplets_loop(Nums, #{}, FreqNext, 0).\n\nspecial_triplets_loop([],\
        \ _FreqPrev, _FreqNext, TotalTriplets) ->\n    TotalTriplets;\nspecial_triplets_loop([CurrentNum\
        \ | RestNums], FreqPrev, FreqNext, TotalTriplets) ->\n    NewFreqNext = maps:update_with(CurrentNum,\
        \ fun(Val) -> Val - 1 end, 0, FreqNext),\n\n    TargetVal = CurrentNum * 2,\n\
        \n    NewTotalTriplets = \n        if TargetVal < ?MAX_VAL ->\n            CountI\
        \ = maps:get(TargetVal, FreqPrev, 0),\n            CountK = maps:get(TargetVal,\
        \ NewFreqNext, 0),\n            (TotalTriplets + (CountI * CountK) rem ?MOD)\
        \ rem ?MOD;\n        true ->\n            TotalTriplets\n        end,\n\n  \
        \  NewFreqPrev = maps:update_with(CurrentNum, fun(Val) -> Val + 1 end, 1, FreqPrev),\n\
        \n    special_triplets_loop(RestNums, NewFreqPrev, NewFreqNext, NewTotalTriplets)."
      elixir: "defmodule Solution do\n  @mod 1_000_000_007\n  @max_val 200_001 # Max\
        \ nums[i] is 10^5, so nums[j]*2 can be 2*10^5\n\n  @spec special_triplets(nums\
        \ :: [integer]) :: integer\n  def special_triplets(nums) do\n    # Initialize\
        \ freq_next by counting all elements\n    freq_next = Enum.reduce(nums, %{},\
        \ fn x, acc ->\n      Map.update(acc, x, 1, &(&1 + 1))\n    end)\n\n    # Iterate\
        \ through nums directly\n    Enum.reduce(nums, {0, %{}, freq_next}, fn current_num,\
        \ {total_triplets, freq_prev, freq_next_current} ->\n      # Decrement freq_next\
        \ for current_num\n      new_freq_next = Map.update(freq_next_current, current_num,\
        \ 0, &(&1 - 1))\n\n      target_val = current_num * 2\n\n      new_total_triplets\
        \ = \n        if target_val < @max_val do\n          count_i = Map.get(freq_prev,\
        \ target_val, 0)\n          count_k = Map.get(new_freq_next, target_val, 0)\n\
        \          rem(total_triplets + rem(count_i * count_k, @mod), @mod)\n      \
        \  else\n          total_triplets\n        end\n\n      # Increment freq_prev\
        \ for current_num\n      new_freq_prev = Map.update(freq_prev, current_num,\
        \ 1, &(&1 + 1))\n\n      {new_total_triplets, new_freq_prev, new_freq_next}\n\
        \    end)\n    |> elem(0) # Extract the final total_triplets\n  end\nend"
    approach: 'The problem asks us to count triplets (i, j, k) such that 0 <= i < j
      < k < n, nums[i] == nums[j] * 2, and nums[k] == nums[j] * 2. The core idea is
      to iterate through each possible middle index j and, for each j, efficiently count
      how many valid i''s exist before j and how many valid k''s exist after j. If nums[j]
      is X, we are looking for nums[i] = 2X and nums[k] = 2X.

      To achieve this efficiently, we use two frequency arrays: freq_prev and freq_next.
      freq_prev[val] stores the count of val in nums at indices less than the current
      j, and freq_next[val] stores the count of val at indices greater than the current
      j. We first pre-populate freq_next with counts of all numbers in the entire array.
      Then, as we iterate j from 0 to n-1, we decrement freq_next[nums[j]] (because
      nums[j] is no longer "after" j), calculate the contribution for the current j
      by multiplying freq_prev[nums[j]*2] and freq_next[nums[j]*2], add this to our
      total (modulo 10^9 + 7), and finally increment freq_prev[nums[j]] (because nums[j]
      is now "before" the next j). This ensures that freq_prev and freq_next always
      reflect the counts of elements strictly before and strictly after the current
      j, respectively.

      Maximum value for nums[i] is 10^5, so nums[j] * 2 can be up to 2 * 10^5. The frequency
      arrays are sized accordingly to 2 * 10^5 + 1. The total count is accumulated modulo
      10^9 + 7 to prevent overflow.'
    time_complexity: The algorithm involves a single pass through the nums array. Initializing
      freq_next takes O(N) time. The main loop iterates N times, and inside the loop,
      array accesses and arithmetic operations take constant time. For languages using
      hash maps for frequency counts (like Erlang/Elixir), map operations take O(log
      M) time where M is the number of distinct elements, leading to an overall O(N
      log M) time complexity. Given M <= 2 * 10^5, log M is small, making it practically
      efficient. Therefore, the total time complexity is O(N) or O(N log MAX_VALUE).
    space_complexity: The algorithm uses two frequency arrays, freq_prev and freq_next.
      The maximum possible value for nums[i] is 10^5, so nums[j] * 2 can be up to 2
      * 10^5. Each frequency array needs to store counts for values up to 2 * 10^5,
      requiring a size of 2 * 10^5 + 1. Thus, the space complexity is O(MAX_VALUE *
      2), which simplifies to O(MAX_VALUE), where MAX_VALUE is the maximum possible
      value of nums[i] (i.e., 10^5).
    elapsed_time: 84.89951968193054
    model: gemini-2.5-flash
    generated_at: '2025-12-09 01:06:27 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int specialTriplets(vector<int>& nums) {\n\
        \        int n = nums.size();\n        int mod = 1e9 + 7;\n        int res =\
        \ 0;\n        unordered_map<int, int> freqPrev;\n        unordered_map<int,\
        \ int> freqNext;\n        for (int i = 0; i < n; i++) {\n            freqNext[nums[i]]++;\n\
        \        }\n        for (int i = 0; i < n; i++) {\n            freqNext[nums[i]]--;\n\
        \            if (freqPrev.find(nums[i] * 2) != freqPrev.end() && freqNext.find(nums[i]\
        \ * 2) != freqNext.end()) {\n                res = (res + freqPrev[nums[i] *\
        \ 2] * freqNext[nums[i] * 2]) % mod;\n            }\n            freqPrev[nums[i]]++;\n\
        \        }\n        return res;\n    }\n};"
      java: "class Solution {\n    public int specialTriplets(int[] nums) {\n      \
        \  int n = nums.length;\n        int mod = (int)1e9 + 7;\n        int res =\
        \ 0;\n        HashMap<Integer, Integer> freqPrev = new HashMap<>();\n      \
        \  HashMap<Integer, Integer> freqNext = new HashMap<>();\n        for (int i\
        \ = 0; i < n; i++) {\n            freqNext.put(nums[i], freqNext.getOrDefault(nums[i],\
        \ 0) + 1);\n        }\n        for (int i = 0; i < n; i++) {\n            freqNext.put(nums[i],\
        \ freqNext.get(nums[i]) - 1);\n            if (freqPrev.containsKey(nums[i]\
        \ * 2) && freqNext.containsKey(nums[i] * 2)) {\n                res = (res +\
        \ freqPrev.get(nums[i] * 2) * freqNext.get(nums[i] * 2)) % mod;\n          \
        \  }\n            freqPrev.put(nums[i], freqPrev.getOrDefault(nums[i], 0) +\
        \ 1);\n        }\n        return res;\n    }\n}"
      python: "class Solution:\n    def specialTriplets(self, nums: list[int]) -> int:\n\
        \        n = len(nums)\n        mod = 10**9 + 7\n        res = 0\n        freqPrev\
        \ = {}\n        freqNext = {}\n        for i in range(n):\n            freqNext[nums[i]]\
        \ = freqNext.get(nums[i], 0) + 1\n        for i in range(n):\n            freqNext[nums[i]]\
        \ -= 1\n            if nums[i] * 2 in freqPrev and nums[i] * 2 in freqNext:\n\
        \                res = (res + freqPrev[nums[i] * 2] * freqNext[nums[i] * 2])\
        \ % mod\n            freqPrev[nums[i]] = freqPrev.get(nums[i], 0) + 1\n    \
        \    return res"
      python3: "class Solution:\n    def specialTriplets(self, nums: list[int]) -> int:\n\
        \        n = len(nums)\n        mod = 10**9 + 7\n        res = 0\n        freqPrev\
        \ = {}\n        freqNext = {}\n        for i in range(n):\n            freqNext[nums[i]]\
        \ = freqNext.get(nums[i], 0) + 1\n        for i in range(n):\n            freqNext[nums[i]]\
        \ -= 1\n            if nums[i] * 2 in freqPrev and nums[i] * 2 in freqNext:\n\
        \                res = (res + freqPrev[nums[i] * 2] * freqNext[nums[i] * 2])\
        \ % mod\n            freqPrev[nums[i]] = freqPrev.get(nums[i], 0) + 1\n    \
        \    return res"
      c: "typedef struct {\n    int key;\n    int value;\n} HashMap;\n\nint specialTriplets(int*\
        \ nums, int numsSize) {\n    int mod = 1000000007;\n    int res = 0;\n    HashMap*\
        \ freqPrev = (HashMap*)malloc(numsSize * sizeof(HashMap));\n    HashMap* freqNext\
        \ = (HashMap*)malloc(numsSize * sizeof(HashMap));\n    int freqPrevSize = 0;\n\
        \    int freqNextSize = 0;\n    for (int i = 0; i < numsSize; i++) {\n     \
        \   int found = 0;\n        for (int j = 0; j < freqNextSize; j++) {\n     \
        \       if (freqNext[j].key == nums[i]) {\n                freqNext[j].value++;\n\
        \                found = 1;\n                break;\n            }\n       \
        \ }\n        if (!found) {\n            freqNext[freqNextSize].key = nums[i];\n\
        \            freqNext[freqNextSize].value = 1;\n            freqNextSize++;\n\
        \        }\n    }\n    for (int i = 0; i < numsSize; i++) {\n        int found\
        \ = 0;\n        for (int j = 0; j < freqNextSize; j++) {\n            if (freqNext[j].key\
        \ == nums[i]) {\n                freqNext[j].value--;\n                found\
        \ = 1;\n                break;\n            }\n        }\n        if (nums[i]\
        \ * 2 != 0) {\n            int foundPrev = 0;\n            int foundNext = 0;\n\
        \            for (int j = 0; j < freqPrevSize; j++) {\n                if (freqPrev[j].key\
        \ == nums[i] * 2) {\n                    foundPrev = 1;\n                  \
        \  break;\n                }\n            }\n            for (int j = 0; j <\
        \ freqNextSize; j++) {\n                if (freqNext[j].key == nums[i] * 2)\
        \ {\n                    foundNext = 1;\n                    break;\n      \
        \          }\n            }\n            if (foundPrev && foundNext) {\n   \
        \             res = (res + freqPrev[freqPrevSize - 1].value * freqNext[freqNextSize\
        \ - 1].value) % mod;\n            }\n        }\n        int found2 = 0;\n  \
        \      for (int j = 0; j < freqPrevSize; j++) {\n            if (freqPrev[j].key\
        \ == nums[i]) {\n                freqPrev[j].value++;\n                found2\
        \ = 1;\n                break;\n            }\n        }\n        if (!found2)\
        \ {\n            freqPrev[freqPrevSize].key = nums[i];\n            freqPrev[freqPrevSize].value\
        \ = 1;\n            freqPrevSize++;\n        }\n    }\n    free(freqPrev);\n\
        \    free(freqNext);\n    return res;\n}"
      csharp: "public class Solution {\n    public int SpecialTriplets(int[] nums) {\n\
        \        int n = nums.Length;\n        int mod = (int)1e9 + 7;\n        int\
        \ res = 0;\n        Dictionary<int, int> freqPrev = new Dictionary<int, int>();\n\
        \        Dictionary<int, int> freqNext = new Dictionary<int, int>();\n     \
        \   for (int i = 0; i < n; i++) {\n            if (freqNext.ContainsKey(nums[i]))\
        \ {\n                freqNext[nums[i]]++;\n            } else {\n          \
        \      freqNext[nums[i]] = 1;\n            }\n        }\n        for (int i\
        \ = 0; i < n; i++) {\n            if (freqNext.ContainsKey(nums[i])) {\n   \
        \             freqNext[nums[i]]--;\n            }\n            if (freqPrev.ContainsKey(nums[i]\
        \ * 2) && freqNext.ContainsKey(nums[i] * 2)) {\n                res = (res +\
        \ freqPrev[nums[i] * 2] * freqNext[nums[i] * 2]) % mod;\n            }\n   \
        \         if (freqPrev.ContainsKey(nums[i])) {\n                freqPrev[nums[i]]++;\n\
        \            } else {\n                freqPrev[nums[i]] = 1;\n            }\n\
        \        }\n        return res;\n    }\n}"
      javascript: "var specialTriplets = function(nums) {\n    let n = nums.length;\n\
        \    let mod = 10**9 + 7;\n    let res = 0;\n    let freqPrev = {};\n    let\
        \ freqNext = {};\n    for (let i = 0; i < n; i++) {\n        freqNext[nums[i]]\
        \ = (freqNext[nums[i]] || 0) + 1;\n    }\n    for (let i = 0; i < n; i++) {\n\
        \        freqNext[nums[i]]--;\n        if (freqPrev[nums[i] * 2] !== undefined\
        \ && freqNext[nums[i] * 2] !== undefined) {\n            res = (res + freqPrev[nums[i]\
        \ * 2] * freqNext[nums[i] * 2]) % mod;\n        }\n        freqPrev[nums[i]]\
        \ = (freqPrev[nums[i]] || 0) + 1;\n    }\n    return res;\n};"
      typescript: "function specialTriplets(nums: number[]): number {\n    let n: number\
        \ = nums.length;\n    let mod: number = 10**9 + 7;\n    let res: number = 0;\n\
        \    let freqPrev: { [key: number]: number } = {};\n    let freqNext: { [key:\
        \ number]: number } = {};\n    for (let i: number = 0; i < n; i++) {\n     \
        \   freqNext[nums[i]] = (freqNext[nums[i]] || 0) + 1;\n    }\n    for (let i:\
        \ number = 0; i < n; i++) {\n        freqNext[nums[i]]--;\n        if (freqPrev[nums[i]\
        \ * 2] !== undefined && freqNext[nums[i] * 2] !== undefined) {\n           \
        \ res = (res + freqPrev[nums[i] * 2] * freqNext[nums[i] * 2]) % mod;\n     \
        \   }\n        freqPrev[nums[i]] = (freqPrev[nums[i]] || 0) + 1;\n    }\n  \
        \  return res;\n}"
      php: "class Solution {\n    function specialTriplets($nums) {\n        $n = count($nums);\n\
        \        $mod = 10**9 + 7;\n        $res = 0;\n        $freqPrev = array();\n\
        \        $freqNext = array();\n        for ($i = 0; $i < $n; $i++) {\n     \
        \       if (array_key_exists($nums[$i], $freqNext)) {\n                $freqNext[$nums[$i]]++;\n\
        \            } else {\n                $freqNext[$nums[$i]] = 1;\n         \
        \   }\n        }\n        for ($i = 0; $i < $n; $i++) {\n            if (array_key_exists($nums[$i],\
        \ $freqNext)) {\n                $freqNext[$nums[$i]]--;\n            }\n  \
        \          if (array_key_exists($nums[$i] * 2, $freqPrev) && array_key_exists($nums[$i]\
        \ * 2, $freqNext)) {\n                $res = ($res + $freqPrev[$nums[$i] * 2]\
        \ * $freqNext[$nums[$i] * 2]) % $mod;\n            }\n            if (array_key_exists($nums[$i],\
        \ $freqPrev)) {\n                $freqPrev[$nums[$i]]++;\n            } else\
        \ {\n                $freqPrev[$nums[$i]] = 1;\n            }\n        }\n \
        \       return $res;\n    }\n}"
      swift: "class Solution {\n    func specialTriplets(_ nums: [Int]) -> Int {\n \
        \       let n = nums.count\n        let mod: Int = Int(1e9 + 7)\n        var\
        \ res = 0\n        var freqPrev: [Int: Int] = [:]\n        var freqNext: [Int:\
        \ Int] = [:]\n        for i in 0..<n {\n            freqNext[nums[i], default:\
        \ 0] += 1\n        }\n        for i in 0..<n {\n            freqNext[nums[i],\
        \ default: 0] -= 1\n            if let prev = freqPrev[nums[i] * 2], let next\
        \ = freqNext[nums[i] * 2] {\n                res = (res + prev * next) % mod\n\
        \            }\n            freqPrev[nums[i], default: 0] += 1\n        }\n\
        \        return res\n    }\n}"
      kotlin: "class Solution {\n    fun specialTriplets(nums: IntArray): Int {\n  \
        \      val n = nums.size\n        val mod = 1000000007\n        var res = 0\n\
        \        val freqPrev = mutableMapOf<Int, Int>()\n        val freqNext = mutableMapOf<Int,\
        \ Int>()\n        for (i in 0 until n) {\n            freqNext[nums[i]] = (freqNext[nums[i]]\
        \ ?: 0) + 1\n        }\n        for (i in 0 until n) {\n            freqNext[nums[i]]\
        \ = (freqNext[nums[i]] ?: 0) - 1\n            if (freqPrev.contains(nums[i]\
        \ * 2) && freqNext.contains(nums[i] * 2)) {\n                res = (res + (freqPrev[nums[i]\
        \ * 2] ?: 0) * (freqNext[nums[i] * 2] ?: 0)) % mod\n            }\n        \
        \    freqPrev[nums[i]] = (freqPrev[nums[i]] ?: 0) + 1\n        }\n        return\
        \ res\n    }\n}"
      dart: "class Solution {\n    int specialTriplets(List<int> nums) {\n        int\
        \ n = nums.length;\n        int mod = 1000000007;\n        int res = 0;\n  \
        \      Map<int, int> freqPrev = {};\n        Map<int, int> freqNext = {};\n\
        \        for (int i = 0; i < n; i++) {\n            freqNext[nums[i]] = (freqNext[nums[i]]\
        \ ?? 0) + 1;\n        }\n        for (int i = 0; i < n; i++) {\n           \
        \ freqNext[nums[i]] = (freqNext[nums[i]] ?? 0) - 1;\n            if (freqPrev.containsKey(nums[i]\
        \ * 2) && freqNext.containsKey(nums[i] * 2)) {\n                res = (res +\
        \ (freqPrev[nums[i] * 2] ?? 0) * (freqNext[nums[i] * 2] ?? 0)) % mod;\n    \
        \        }\n            freqPrev[nums[i]] = (freqPrev[nums[i]] ?? 0) + 1;\n\
        \        }\n        return res;\n    }\n}"
      go: "package main\n\nimport (\n    \"fmt\"\n)\n\ntype Solution struct{}\n\nfunc\
        \ (s Solution) specialTriplets(nums []int) int {\n    n := len(nums)\n    mod\
        \ := 1000000007\n    res := 0\n    freqPrev := make(map[int]int)\n    freqNext\
        \ := make(map[int]int)\n    for i := 0; i < n; i++ {\n        freqNext[nums[i]]++\n\
        \    }\n    for i := 0; i < n; i++ {\n        freqNext[nums[i]]--\n        if\
        \ _, ok := freqPrev[nums[i]*2]; ok && _, ok := freqNext[nums[i]*2]; ok {\n \
        \           res = (res + freqPrev[nums[i]*2]*freqNext[nums[i]*2]) % mod\n  \
        \      }\n        freqPrev[nums[i]]++\n    }\n    return res\n}\n\nfunc main()\
        \ {\n    solution := Solution{}\n    nums := []int{6, 3, 6}\n    fmt.Println(solution.specialTriplets(nums))\n\
        }"
      ruby: "class Solution\n    def special_triplets(nums)\n        n = nums.size\n\
        \        mod = 10**9 + 7\n        res = 0\n        freq_prev = {}\n        freq_next\
        \ = {}\n        nums.each do |num|\n            freq_next[num] = (freq_next[num]\
        \ || 0) + 1\n        end\n        nums.each_with_index do |num, i|\n       \
        \     freq_next[num] -= 1\n            if freq_prev.key?(num * 2) && freq_next.key?(num\
        \ * 2)\n                res = (res + freq_prev[num * 2] * freq_next[num * 2])\
        \ % mod\n            end\n            freq_prev[num] = (freq_prev[num] || 0)\
        \ + 1\n        end\n        res\n    end\nend"
      scala: "object Solution {\n    def specialTriplets(nums: Array[Int]): Int = {\n\
        \        val n = nums.length\n        val mod = 1000000007\n        var res\
        \ = 0\n        val freqPrev = scala.collection.mutable.Map[Int, Int]().withDefaultValue(0)\n\
        \        val freqNext = scala.collection.mutable.Map[Int, Int]().withDefaultValue(0)\n\
        \        for (i <- 0 until n) {\n            freqNext(nums(i)) += 1\n      \
        \  }\n        for (i <- 0 until n) {\n            freqNext(nums(i)) -= 1\n \
        \           if (freqPrev.contains(nums(i) * 2) && freqNext.contains(nums(i)\
        \ * 2)) {\n                res = (res + freqPrev(nums(i) * 2) * freqNext(nums(i)\
        \ * 2)) % mod\n            }\n            freqPrev(nums(i)) += 1\n        }\n\
        \        res\n    }\n}"
      rust: "struct Solution;\n\nimpl Solution {\n    pub fn special_triplests(nums:\
        \ Vec<i32>) -> i32 {\n        let n = nums.len() as i32;\n        let mod =\
        \ 1000000007;\n        let mut res = 0;\n        let mut freq_prev: std::collections::HashMap<i32,\
        \ i32> = std::collections::HashMap::new();\n        let mut freq_next: std::collections::HashMap<i32,\
        \ i32> = std::collections::HashMap::new();\n        for &num in nums.iter()\
        \ {\n            *freq_next.entry(num).or_insert(0) += 1;\n        }\n     \
        \   for &num in nums.iter() {\n            *freq_next.entry(num).or_insert(0)\
        \ -= 1;\n            if let Some(&prev) = freq_prev.get(&(num * 2)) {\n    \
        \            if let Some(&next) = freq_next.get(&(num * 2)) {\n            \
        \        res = (res + prev * next) % mod;\n                }\n            }\n\
        \            *freq_prev.entry(num).or_insert(0) += 1;\n        }\n        res\n\
        \    }\n}"
      racket: "define (special-triplets nums)\n    (let* (\n        (n (length nums))\n\
        \        (mod 1000000007)\n        (res 0)\n        (freq-prev (make-hash))\n\
        \        (freq-next (make-hash))\n        )\n        (for (\n            (\n\
        \            (i 0)\n            (< i n)\n            (add1 i)\n            )\n\
        \            )\n            (hash-set! freq-next (list-ref nums i) (+ (hash-ref\
        \ freq-next (list-ref nums i) 0) 1))\n            )\n        (for (\n      \
        \      (\n            (i 0)\n            (< i n)\n            (add1 i)\n   \
        \         )\n            )\n            (begin\n                (hash-set! freq-next\
        \ (list-ref nums i) (- (hash-ref freq-next (list-ref nums i) 0) 1))\n      \
        \          (when (and (hash-has-key? freq-prev (* (list-ref nums i) 2)) (hash-has-key?\
        \ freq-next (* (list-ref nums i) 2)))\n                    (set! res (modulo\
        \ (+ res (* (hash-ref freq-prev (* (list-ref nums i) 2) 0) (hash-ref freq-next\
        \ (* (list-ref nums i) 2) 0))) mod))\n                    )\n              \
        \  (hash-set! freq-prev (list-ref nums i) (+ (hash-ref freq-prev (list-ref nums\
        \ i) 0) 1))\n                )\n            )\n        res\n        )"
      erlang: "special_triplests(Nums) ->\n    Res = special_triplests(Nums, 0, dict:new(),\
        \ dict:new()),\n    Res.\n\nspecial_triplests([], Res, _, _) -> Res;\nspecial_triplests([Num|Nums],\
        \ Res, FreqPrev, FreqNext) ->\n    NewFreqNext = dict:update_counter(Num, 1,\
        \ FreqNext),\n    special_triplests(Nums, Res, FreqPrev, NewFreqNext).\n\nspecial_triplests(Nums)\
        \ ->\n    special_triplests(Nums, 0, dict:new(), dict:new()).\n\nspecial_triplests([Num|Nums],\
        \ Res, FreqPrev, FreqNext) ->\n    NewFreqNext = dict:update_counter(Num, -1,\
        \ FreqNext),\n    case dict:find(Num*2, FreqPrev) of\n        {ok, Prev} ->\n\
        \            case dict:find(Num*2, FreqNext) of\n                {ok, Next}\
        \ ->\n                    NewRes = (Res + Prev*Next) rem 1000000007,\n     \
        \               special_triplests(Nums, NewRes, dict:update_counter(Num, 1,\
        \ FreqPrev), NewFreqNext);\n                _ -> special_triplests(Nums, Res,\
        \ dict:update_counter(Num, 1, FreqPrev), NewFreqNext)\n            end;\n  \
        \      _ -> special_triplests(Nums, Res, dict:update_counter(Num, 1, FreqPrev),\
        \ NewFreqNext)\n    end."
      elixir: "defmodule Solution do\n    def special_triplests(nums) do\n        n\
        \ = length(nums)\n        mod = 1000000007\n        res = 0\n        freq_prev\
        \ = %{}\n        freq_next = %{}\n        Enum.reduce(nums, {res, freq_prev,\
        \ freq_next}, fn num, {res, freq_prev, freq_next} ->\n            freq_next\
        \ = Map.update(freq_next, num, 1, &(&1 + 1))\n            {res, freq_prev, freq_next}\n\
        \        end)\n        |> elem(1)\n        |> Enum.reduce(nums, fn num, {res,\
        \ freq_prev, freq_next} ->\n            freq_next = Map.update(freq_next, num,\
        \ 0, &(&1 - 1))\n            if Map.has_key?(freq_prev, num * 2) and Map.has_key?(freq_next,\
        \ num * 2) do\n                res = rem(res + Map.get(freq_prev, num * 2) *\
        \ Map.get(freq_next, num * 2), mod)\n            end\n            freq_prev\
        \ = Map.update(freq_prev, num, 1, &(&1 + 1))\n            {res, freq_prev, freq_next}\n\
        \        end)\n        |> elem(0)\n    end\nend"
    approach: The problem can be solved by iterating over the array and for each element,
      checking all previous and next elements to find special triplets. The key intuition
      is to use frequency arrays or maps to track how many times each value appears
      before and after the current index. This allows us to efficiently compute the
      contribution of each index to the answer. We can iterate over the array and for
      each index j, compute its contribution to the answer using the frequency counts.
      The frequency counts can be updated as we iterate over the array, allowing us
      to efficiently compute the answer in a single pass.
    time_complexity: The time complexity of the algorithm is O(n), where n is the length
      of the input array. This is because we iterate over the array once, and for each
      index, we perform a constant amount of work to compute its contribution to the
      answer and update the frequency counts.
    space_complexity: The space complexity of the algorithm is O(n), where n is the
      length of the input array. This is because we need to store the frequency counts
      for each value in the array, and in the worst case, every value in the array is
      unique, requiring O(n) space to store the frequency counts.
    elapsed_time: 12.375578880310059
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-09 01:06:39 '
---

## Problem #3583: Count Special Triplets

**Difficulty:** Medium

**Topics:** Array, Hash Table, Counting

## Problem Description

<p>You are given an integer array <code>nums</code>.</p>

<p>A <strong>special triplet</strong> is defined as a triplet of indices <code>(i, j, k)</code> such that:</p>

<ul>
	<li><code>0 &lt;= i &lt; j &lt; k &lt; n</code>, where <code>n = nums.length</code></li>
	<li><code>nums[i] == nums[j] * 2</code></li>
	<li><code>nums[k] == nums[j] * 2</code></li>
</ul>

<p>Return the total number of <strong>special triplets</strong> in the array.</p>

<p>Since the answer may be large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [6,3,6]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>The only special triplet is <code>(i, j, k) = (0, 1, 2)</code>, where:</p>

<ul>
	<li><code>nums[0] = 6</code>, <code>nums[1] = 3</code>, <code>nums[2] = 6</code></li>
	<li><code>nums[0] = nums[1] * 2 = 3 * 2 = 6</code></li>
	<li><code>nums[2] = nums[1] * 2 = 3 * 2 = 6</code></li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [0,1,0,0]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>The only special triplet is <code>(i, j, k) = (0, 2, 3)</code>, where:</p>

<ul>
	<li><code>nums[0] = 0</code>, <code>nums[2] = 0</code>, <code>nums[3] = 0</code></li>
	<li><code>nums[0] = nums[2] * 2 = 0 * 2 = 0</code></li>
	<li><code>nums[3] = nums[2] * 2 = 0 * 2 = 0</code></li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [8,4,2,8,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>There are exactly two special triplets:</p>

<ul>
	<li><code>(i, j, k) = (0, 1, 3)</code>

	<ul>
		<li><code>nums[0] = 8</code>, <code>nums[1] = 4</code>, <code>nums[3] = 8</code></li>
		<li><code>nums[0] = nums[1] * 2 = 4 * 2 = 8</code></li>
		<li><code>nums[3] = nums[1] * 2 = 4 * 2 = 8</code></li>
	</ul>
	</li>
	<li><code>(i, j, k) = (1, 2, 4)</code>
	<ul>
		<li><code>nums[1] = 4</code>, <code>nums[2] = 2</code>, <code>nums[4] = 4</code></li>
		<li><code>nums[1] = nums[2] * 2 = 2 * 2 = 4</code></li>
		<li><code>nums[4] = nums[2] * 2 = 2 * 2 = 4</code></li>
	</ul>
	</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. Use frequency arrays or maps, e.g. `freqPrev` and `freqNext`—to track how many times each value appears before and after the current index.

2. For each index `j` in the triplet (`i`,`j`,`k`), compute its contribution to the answer using your freqPrev and freqNext counts.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-09 01:06:27 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to count triplets (i, j, k) such that 0 <= i < j < k < n, nums[i] == nums[j] * 2, and nums[k] == nums[j] * 2. The core idea is to iterate through each possible middle index j and, for each j, efficiently count how many valid i's exist before j and how many valid k's exist after j. If nums[j] is X, we are looking for nums[i] = 2X and nums[k] = 2X.
To achieve this efficiently, we use two frequency arrays: freq_prev and freq_next. freq_prev[val] stores the count of val in nums at indices less than the current j, and freq_next[val] stores the count of val at indices greater than the current j. We first pre-populate freq_next with counts of all numbers in the entire array. Then, as we iterate j from 0 to n-1, we decrement freq_next[nums[j]] (because nums[j] is no longer "after" j), calculate the contribution for the current j by multiplying freq_prev[nums[j]*2] and freq_next[nums[j]*2], add this to our total (modulo 10^9 + 7), and finally increment freq_prev[nums[j]] (because nums[j] is now "before" the next j). This ensures that freq_prev and freq_next always reflect the counts of elements strictly before and strictly after the current j, respectively.
Maximum value for nums[i] is 10^5, so nums[j] * 2 can be up to 2 * 10^5. The frequency arrays are sized accordingly to 2 * 10^5 + 1. The total count is accumulated modulo 10^9 + 7 to prevent overflow.

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
    int specialTriplets(std::vector<int>& nums) {
        int n = nums.size();
        long long total_triplets = 0;
        long long MOD = 1e9 + 7;
        int MAX_VAL = 200001; // Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5

        std::vector<int> freq_prev(MAX_VAL, 0);
        std::vector<int> freq_next(MAX_VAL, 0);

        for (int x : nums) {
            freq_next[x]++;
        }

        for (int j = 0; j < n; ++j) {
            freq_next[nums[j]]--;

            long long target_val = (long long)nums[j] * 2;

            if (target_val < MAX_VAL) {
                long long count_i = freq_prev[target_val];
                long long count_k = freq_next[target_val];
                total_triplets = (total_triplets + (count_i * count_k) % MOD) % MOD;
            }

            freq_prev[nums[j]]++;
        }

        return static_cast<int>(total_triplets);
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.List;

class Solution {
    public int specialTriplets(List<Integer> nums) {
        int n = nums.size();
        long totalTriplets = 0;
        long MOD = 1_000_000_007;
        int MAX_VAL = 200001; // Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5

        int[] freqPrev = new int[MAX_VAL]; // Initialized to zeros by default
        int[] freqNext = new int[MAX_VAL]; // Initialized to zeros by default

        for (int x : nums) {
            freqNext[x]++;
        }

        for (int j = 0; j < n; ++j) {
            int currentNum = nums.get(j);
            freqNext[currentNum]--;

            long targetVal = (long)currentNum * 2;

            if (targetVal < MAX_VAL) {
                long countI = freqPrev[(int)targetVal];
                long countK = freqNext[(int)targetVal];
                totalTriplets = (totalTriplets + (countI * countK) % MOD) % MOD;
            }

            freqPrev[currentNum]++;
        }

        return (int)totalTriplets;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        total_triplets = 0
        MOD = 10**9 + 7
        MAX_VAL = 200001  # Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5

        freq_prev = [0] * MAX_VAL
        freq_next = [0] * MAX_VAL

        for x in nums:
            freq_next[x] += 1

        for j in range(n):
            current_num = nums[j]
            freq_next[current_num] -= 1

            target_val = current_num * 2

            if target_val < MAX_VAL:
                count_i = freq_prev[target_val]
                count_k = freq_next[target_val]
                total_triplets = (total_triplets + (count_i * count_k) % MOD) % MOD

            freq_prev[current_num] += 1

        return total_triplets
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        total_triplets = 0
        MOD = 10**9 + 7
        MAX_VAL = 200001  # Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5

        freq_prev = [0] * MAX_VAL
        freq_next = [0] * MAX_VAL

        for x in nums:
            freq_next[x] += 1

        for j in range(n):
            current_num = nums[j]
            freq_next[current_num] -= 1

            target_val = current_num * 2

            if target_val < MAX_VAL:
                count_i = freq_prev[target_val]
                count_k = freq_next[target_val]
                total_triplets = (total_triplets + (count_i * count_k) % MOD) % MOD

            freq_prev[current_num] += 1

        return total_triplets
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

#define MOD 1000000007
#define MAX_VAL 200001 // Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5

int specialTriplets(int* nums, int numsSize) {
    long long total_triplets = 0;

    int* freq_prev = (int*)calloc(MAX_VAL, sizeof(int));
    int* freq_next = (int*)calloc(MAX_VAL, sizeof(int));

    if (freq_prev == NULL || freq_next == NULL) {
        // Handle memory allocation failure
        if (freq_prev) free(freq_prev);
        if (freq_next) free(freq_next);
        return 0; // Or throw an error, depending on requirements
    }

    for (int i = 0; i < numsSize; ++i) {
        freq_next[nums[i]]++;
    }

    for (int j = 0; j < numsSize; ++j) {
        int current_num = nums[j];
        freq_next[current_num]--;

        long long target_val = (long long)current_num * 2;

        if (target_val < MAX_VAL) {
            long long count_i = freq_prev[target_val];
            long long count_k = freq_next[target_val];
            total_triplets = (total_triplets + (count_i * count_k) % MOD) % MOD;
        }

        freq_prev[current_num]++;
    }

    free(freq_prev);
    free(freq_next);

    return (int)total_triplets;
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
    public int SpecialTriplets(int[] nums) {
        int n = nums.Length;
        long totalTriplets = 0;
        long MOD = 1_000_000_007;
        int MAX_VAL = 200001; // Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5

        int[] freqPrev = new int[MAX_VAL]; // Initialized to zeros by default
        int[] freqNext = new int[MAX_VAL]; // Initialized to zeros by default

        foreach (int x in nums) {
            freqNext[x]++;
        }

        for (int j = 0; j < n; ++j) {
            int currentNum = nums[j];
            freqNext[currentNum]--;

            long targetVal = (long)currentNum * 2;

            if (targetVal < MAX_VAL) {
                long countI = freqPrev[(int)targetVal];
                long countK = freqNext[(int)targetVal];
                totalTriplets = (totalTriplets + (countI * countK) % MOD) % MOD;
            }

            freqPrev[currentNum]++;
        }

        return (int)totalTriplets;
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
var specialTriplets = function(nums) {
    const n = nums.length;
    let totalTriplets = 0;
    const MOD = 10**9 + 7;
    const MAX_VAL = 200001; // Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5

    const freqPrev = new Array(MAX_VAL).fill(0);
    const freqNext = new Array(MAX_VAL).fill(0);

    for (const x of nums) {
        freqNext[x]++;
    }

    for (let j = 0; j < n; ++j) {
        const currentNum = nums[j];
        freqNext[currentNum]--;

        const targetVal = currentNum * 2;

        if (targetVal < MAX_VAL) {
            const countI = freqPrev[targetVal];
            const countK = freqNext[targetVal];
            totalTriplets = (totalTriplets + (countI * countK) % MOD) % MOD;
        }

        freqPrev[currentNum]++;
    }

    return totalTriplets;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function specialTriplets(nums: number[]): number {
    const n = nums.length;
    let totalTriplets = 0;
    const MOD = 10**9 + 7;
    const MAX_VAL = 200001; // Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5

    const freqPrev: number[] = new Array(MAX_VAL).fill(0);
    const freqNext: number[] = new Array(MAX_VAL).fill(0);

    for (const x of nums) {
        freqNext[x]++;
    }

    for (let j = 0; j < n; ++j) {
        const currentNum = nums[j];
        freqNext[currentNum]--;

        const targetVal = currentNum * 2;

        if (targetVal < MAX_VAL) {
            const countI = freqPrev[targetVal];
            const countK = freqNext[targetVal];
            totalTriplets = (totalTriplets + (countI * countK) % MOD) % MOD;
        }

        freqPrev[currentNum]++;
    }

    return totalTriplets;
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
    function specialTriplets($nums) {
        $n = count($nums);
        $totalTriplets = 0;
        $MOD = 10**9 + 7;
        $MAX_VAL = 200001; // Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5

        $freqPrev = array_fill(0, $MAX_VAL, 0);
        $freqNext = array_fill(0, $MAX_VAL, 0);

        foreach ($nums as $x) {
            $freqNext[$x]++;
        }

        for ($j = 0; $j < $n; ++$j) {
            $currentNum = $nums[$j];
            $freqNext[$currentNum]--;

            $targetVal = $currentNum * 2;

            if ($targetVal < $MAX_VAL) {
                $countI = $freqPrev[$targetVal];
                $countK = $freqNext[$targetVal];
                $totalTriplets = ($totalTriplets + ($countI * $countK) % $MOD) % $MOD;
            }

            $freqPrev[$currentNum]++;
        }

        return $totalTriplets;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func specialTriplets(_ nums: [Int]) -> Int {
        let n = nums.count
        var totalTriplets = 0
        let MOD = 1_000_000_007
        let MAX_VAL = 200001 // Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5

        var freqPrev = Array(repeating: 0, count: MAX_VAL)
        var freqNext = Array(repeating: 0, count: MAX_VAL)

        for x in nums {
            freqNext[x] += 1
        }

        for j in 0..<n {
            let currentNum = nums[j]
            freqNext[currentNum] -= 1

            let targetVal = currentNum * 2

            if targetVal < MAX_VAL {
                let countI = freqPrev[targetVal]
                let countK = freqNext[targetVal]
                totalTriplets = (totalTriplets + (countI * countK) % MOD) % MOD
            }

            freqPrev[currentNum] += 1
        }

        return totalTriplets
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun specialTriplets(nums: List<Int>): Int {
        val n = nums.size
        var totalTriplets: Long = 0
        val MOD: Long = 1_000_000_007
        val MAX_VAL = 200001 // Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5

        val freqPrev = IntArray(MAX_VAL) // Initialized to zeros by default
        val freqNext = IntArray(MAX_VAL) // Initialized to zeros by default

        for (x in nums) {
            freqNext[x]++
        }

        for (j in 0 until n) {
            val currentNum = nums[j]
            freqNext[currentNum]--

            val targetVal = currentNum * 2L // Use Long for multiplication to prevent overflow

            if (targetVal < MAX_VAL) {
                val countI = freqPrev[targetVal.toInt()].toLong()
                val countK = freqNext[targetVal.toInt()].toLong()
                totalTriplets = (totalTriplets + (countI * countK) % MOD) % MOD
            }

            freqPrev[currentNum]++
        }

        return totalTriplets.toInt()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int specialTriplets(List<int> nums) {
    final n = nums.length;
    int totalTriplets = 0;
    final MOD = 1000000007;
    final MAX_VAL = 200001; // Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5

    final freqPrev = List<int>.filled(MAX_VAL, 0);
    final freqNext = List<int>.filled(MAX_VAL, 0);

    for (final x in nums) {
      freqNext[x]++;
    }

    for (var j = 0; j < n; ++j) {
      final currentNum = nums[j];
      freqNext[currentNum]--;

      final targetVal = currentNum * 2;

      if (targetVal < MAX_VAL) {
        final countI = freqPrev[targetVal];
        final countK = freqNext[targetVal];
        totalTriplets = (totalTriplets + (countI * countK) % MOD) % MOD;
      }

      freqPrev[currentNum]++;
    }

    return totalTriplets;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

func specialTriplets(nums []int) int {
    n := len(nums)
    var totalTriplets int64 = 0
    const MOD int64 = 1e9 + 7
    const MAX_VAL int = 200001 // Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5

    freqPrev := make([]int, MAX_VAL)
    freqNext := make([]int, MAX_VAL)

    for _, x := range nums {
        freqNext[x]++
    }

    for j := 0; j < n; j++ {
        currentNum := nums[j]
        freqNext[currentNum]--

        targetVal := currentNum * 2

        if targetVal < MAX_VAL {
            countI := int64(freqPrev[targetVal])
            countK := int64(freqNext[targetVal])
            totalTriplets = (totalTriplets + (countI * countK) % MOD) % MOD
        }

        freqPrev[currentNum]++
    }

    return int(totalTriplets)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    def special_triplets(nums)
        n = nums.length
        total_triplets = 0
        mod = 10**9 + 7
        max_val = 200001 # Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5

        freq_prev = Array.new(max_val, 0)
        freq_next = Array.new(max_val, 0)

        nums.each do |x|
            freq_next[x] += 1
        end

        (0...n).each do |j|
            current_num = nums[j]
            freq_next[current_num] -= 1

            target_val = current_num * 2

            if target_val < max_val
                count_i = freq_prev[target_val]
                count_k = freq_next[target_val]
                total_triplets = (total_triplets + (count_i * count_k) % mod) % mod
            end

            freq_prev[current_num] += 1
        end

        total_triplets
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable.ArrayBuffer

object Solution {
    def specialTriplets(nums: List[Int]): Int = {
        val n = nums.length
        var totalTriplets: Long = 0
        val MOD: Long = 1_000_000_007
        val MAX_VAL = 200001 // Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5

        val freqPrev = Array.fill(MAX_VAL)(0)
        val freqNext = Array.fill(MAX_VAL)(0)

        for (x <- nums) {
            freqNext(x) += 1
        }

        for (j <- 0 until n) {
            val currentNum = nums(j)
            freqNext(currentNum) -= 1

            val targetVal = currentNum * 2L // Use Long for multiplication to prevent overflow

            if (targetVal < MAX_VAL) {
                val countI = freqPrev(targetVal.toInt).toLong
                val countK = freqNext(targetVal.toInt).toLong
                totalTriplets = (totalTriplets + (countI * countK) % MOD) % MOD
            }

            freqPrev(currentNum) += 1
        }

        totalTriplets.toInt
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn special_triplets(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut total_triplets: i64 = 0;
        let modular: i64 = 1_000_000_007;
        let max_val = 200001; // Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5

        let mut freq_prev = vec![0; max_val];
        let mut freq_next = vec![0; max_val];

        for &x in nums.iter() {
            freq_next[x as usize] += 1;
        }

        for j in 0..n {
            let current_num = nums[j];
            freq_next[current_num as usize] -= 1;

            let target_val = current_num as i64 * 2;

            if target_val < max_val as i64 {
                let count_i = freq_prev[target_val as usize] as i64;
                let count_k = freq_next[target_val as usize] as i64;
                total_triplets = (total_triplets + (count_i * count_k) % modular) % modular;
            }

            freq_prev[current_num as usize] += 1;
        }

        total_triplets as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (special-triplets nums)
  (define n (vector-length nums))
  (define mod 1000000007)
  (define max-val 200001) ; Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5

  (define freq-prev (make-vector max-val 0))
  (define freq-next (make-vector max-val 0))

  ;; Populate freq-next
  (for ([x (in-vector nums)])
    (vector-set! freq-next x (+ (vector-ref freq-next x) 1)))

  (define total-triplets 0)

  (for ([j (in-range n)])
    (define current-num (vector-ref nums j))
    (vector-set! freq-next current-num (- (vector-ref freq-next current-num) 1))

    (define target-val (* current-num 2))

    (when (< target-val max-val)
      (define count-i (vector-ref freq-prev target-val))
      (define count-k (vector-ref freq-next target-val))
      (set! total-triplets
            (modulo (+ total-triplets (modulo (* count-i count-k) mod)) mod)))

    (vector-set! freq-prev current-num (+ (vector-ref freq-prev current-num) 1)))

  total-triplets)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([special_triplets/1]).

-define(MOD, 1000000007).
-define(MAX_VAL, 200001). %% Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5

special_triplets(Nums) ->
    %% Pre-populate FreqNext
    FreqNext = lists:foldl(fun(X, Acc) -> maps:update_with(X, fun(Val) -> Val + 1 end, 1, Acc) end, #{}, Nums),

    special_triplets_loop(Nums, #{}, FreqNext, 0).

special_triplets_loop([], _FreqPrev, _FreqNext, TotalTriplets) ->
    TotalTriplets;
special_triplets_loop([CurrentNum | RestNums], FreqPrev, FreqNext, TotalTriplets) ->
    NewFreqNext = maps:update_with(CurrentNum, fun(Val) -> Val - 1 end, 0, FreqNext),

    TargetVal = CurrentNum * 2,

    NewTotalTriplets = 
        if TargetVal < ?MAX_VAL ->
            CountI = maps:get(TargetVal, FreqPrev, 0),
            CountK = maps:get(TargetVal, NewFreqNext, 0),
            (TotalTriplets + (CountI * CountK) rem ?MOD) rem ?MOD;
        true ->
            TotalTriplets
        end,

    NewFreqPrev = maps:update_with(CurrentNum, fun(Val) -> Val + 1 end, 1, FreqPrev),

    special_triplets_loop(RestNums, NewFreqPrev, NewFreqNext, NewTotalTriplets).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @mod 1_000_000_007
  @max_val 200_001 # Max nums[i] is 10^5, so nums[j]*2 can be 2*10^5

  @spec special_triplets(nums :: [integer]) :: integer
  def special_triplets(nums) do
    # Initialize freq_next by counting all elements
    freq_next = Enum.reduce(nums, %{}, fn x, acc ->
      Map.update(acc, x, 1, &(&1 + 1))
    end)

    # Iterate through nums directly
    Enum.reduce(nums, {0, %{}, freq_next}, fn current_num, {total_triplets, freq_prev, freq_next_current} ->
      # Decrement freq_next for current_num
      new_freq_next = Map.update(freq_next_current, current_num, 0, &(&1 - 1))

      target_val = current_num * 2

      new_total_triplets = 
        if target_val < @max_val do
          count_i = Map.get(freq_prev, target_val, 0)
          count_k = Map.get(new_freq_next, target_val, 0)
          rem(total_triplets + rem(count_i * count_k, @mod), @mod)
        else
          total_triplets
        end

      # Increment freq_prev for current_num
      new_freq_prev = Map.update(freq_prev, current_num, 1, &(&1 + 1))

      {new_total_triplets, new_freq_prev, new_freq_next}
    end)
    |> elem(0) # Extract the final total_triplets
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The algorithm involves a single pass through the nums array. Initializing freq_next takes O(N) time. The main loop iterates N times, and inside the loop, array accesses and arithmetic operations take constant time. For languages using hash maps for frequency counts (like Erlang/Elixir), map operations take O(log M) time where M is the number of distinct elements, leading to an overall O(N log M) time complexity. Given M <= 2 * 10^5, log M is small, making it practically efficient. Therefore, the total time complexity is O(N) or O(N log MAX_VALUE).

- **Space Complexity:** The algorithm uses two frequency arrays, freq_prev and freq_next. The maximum possible value for nums[i] is 10^5, so nums[j] * 2 can be up to 2 * 10^5. Each frequency array needs to store counts for values up to 2 * 10^5, requiring a size of 2 * 10^5 + 1. Thus, the space complexity is O(MAX_VALUE * 2), which simplifies to O(MAX_VALUE), where MAX_VALUE is the maximum possible value of nums[i] (i.e., 10^5).

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-09 01:06:39 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by iterating over the array and for each element, checking all previous and next elements to find special triplets. The key intuition is to use frequency arrays or maps to track how many times each value appears before and after the current index. This allows us to efficiently compute the contribution of each index to the answer. We can iterate over the array and for each index j, compute its contribution to the answer using the frequency counts. The frequency counts can be updated as we iterate over the array, allowing us to efficiently compute the answer in a single pass.

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
    int specialTriplets(vector<int>& nums) {
        int n = nums.size();
        int mod = 1e9 + 7;
        int res = 0;
        unordered_map<int, int> freqPrev;
        unordered_map<int, int> freqNext;
        for (int i = 0; i < n; i++) {
            freqNext[nums[i]]++;
        }
        for (int i = 0; i < n; i++) {
            freqNext[nums[i]]--;
            if (freqPrev.find(nums[i] * 2) != freqPrev.end() && freqNext.find(nums[i] * 2) != freqNext.end()) {
                res = (res + freqPrev[nums[i] * 2] * freqNext[nums[i] * 2]) % mod;
            }
            freqPrev[nums[i]]++;
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
    public int specialTriplets(int[] nums) {
        int n = nums.length;
        int mod = (int)1e9 + 7;
        int res = 0;
        HashMap<Integer, Integer> freqPrev = new HashMap<>();
        HashMap<Integer, Integer> freqNext = new HashMap<>();
        for (int i = 0; i < n; i++) {
            freqNext.put(nums[i], freqNext.getOrDefault(nums[i], 0) + 1);
        }
        for (int i = 0; i < n; i++) {
            freqNext.put(nums[i], freqNext.get(nums[i]) - 1);
            if (freqPrev.containsKey(nums[i] * 2) && freqNext.containsKey(nums[i] * 2)) {
                res = (res + freqPrev.get(nums[i] * 2) * freqNext.get(nums[i] * 2)) % mod;
            }
            freqPrev.put(nums[i], freqPrev.getOrDefault(nums[i], 0) + 1);
        }
        return res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def specialTriplets(self, nums: list[int]) -> int:
        n = len(nums)
        mod = 10**9 + 7
        res = 0
        freqPrev = {}
        freqNext = {}
        for i in range(n):
            freqNext[nums[i]] = freqNext.get(nums[i], 0) + 1
        for i in range(n):
            freqNext[nums[i]] -= 1
            if nums[i] * 2 in freqPrev and nums[i] * 2 in freqNext:
                res = (res + freqPrev[nums[i] * 2] * freqNext[nums[i] * 2]) % mod
            freqPrev[nums[i]] = freqPrev.get(nums[i], 0) + 1
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def specialTriplets(self, nums: list[int]) -> int:
        n = len(nums)
        mod = 10**9 + 7
        res = 0
        freqPrev = {}
        freqNext = {}
        for i in range(n):
            freqNext[nums[i]] = freqNext.get(nums[i], 0) + 1
        for i in range(n):
            freqNext[nums[i]] -= 1
            if nums[i] * 2 in freqPrev and nums[i] * 2 in freqNext:
                res = (res + freqPrev[nums[i] * 2] * freqNext[nums[i] * 2]) % mod
            freqPrev[nums[i]] = freqPrev.get(nums[i], 0) + 1
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
typedef struct {
    int key;
    int value;
} HashMap;

int specialTriplets(int* nums, int numsSize) {
    int mod = 1000000007;
    int res = 0;
    HashMap* freqPrev = (HashMap*)malloc(numsSize * sizeof(HashMap));
    HashMap* freqNext = (HashMap*)malloc(numsSize * sizeof(HashMap));
    int freqPrevSize = 0;
    int freqNextSize = 0;
    for (int i = 0; i < numsSize; i++) {
        int found = 0;
        for (int j = 0; j < freqNextSize; j++) {
            if (freqNext[j].key == nums[i]) {
                freqNext[j].value++;
                found = 1;
                break;
            }
        }
        if (!found) {
            freqNext[freqNextSize].key = nums[i];
            freqNext[freqNextSize].value = 1;
            freqNextSize++;
        }
    }
    for (int i = 0; i < numsSize; i++) {
        int found = 0;
        for (int j = 0; j < freqNextSize; j++) {
            if (freqNext[j].key == nums[i]) {
                freqNext[j].value--;
                found = 1;
                break;
            }
        }
        if (nums[i] * 2 != 0) {
            int foundPrev = 0;
            int foundNext = 0;
            for (int j = 0; j < freqPrevSize; j++) {
                if (freqPrev[j].key == nums[i] * 2) {
                    foundPrev = 1;
                    break;
                }
            }
            for (int j = 0; j < freqNextSize; j++) {
                if (freqNext[j].key == nums[i] * 2) {
                    foundNext = 1;
                    break;
                }
            }
            if (foundPrev && foundNext) {
                res = (res + freqPrev[freqPrevSize - 1].value * freqNext[freqNextSize - 1].value) % mod;
            }
        }
        int found2 = 0;
        for (int j = 0; j < freqPrevSize; j++) {
            if (freqPrev[j].key == nums[i]) {
                freqPrev[j].value++;
                found2 = 1;
                break;
            }
        }
        if (!found2) {
            freqPrev[freqPrevSize].key = nums[i];
            freqPrev[freqPrevSize].value = 1;
            freqPrevSize++;
        }
    }
    free(freqPrev);
    free(freqNext);
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int SpecialTriplets(int[] nums) {
        int n = nums.Length;
        int mod = (int)1e9 + 7;
        int res = 0;
        Dictionary<int, int> freqPrev = new Dictionary<int, int>();
        Dictionary<int, int> freqNext = new Dictionary<int, int>();
        for (int i = 0; i < n; i++) {
            if (freqNext.ContainsKey(nums[i])) {
                freqNext[nums[i]]++;
            } else {
                freqNext[nums[i]] = 1;
            }
        }
        for (int i = 0; i < n; i++) {
            if (freqNext.ContainsKey(nums[i])) {
                freqNext[nums[i]]--;
            }
            if (freqPrev.ContainsKey(nums[i] * 2) && freqNext.ContainsKey(nums[i] * 2)) {
                res = (res + freqPrev[nums[i] * 2] * freqNext[nums[i] * 2]) % mod;
            }
            if (freqPrev.ContainsKey(nums[i])) {
                freqPrev[nums[i]]++;
            } else {
                freqPrev[nums[i]] = 1;
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
var specialTriplets = function(nums) {
    let n = nums.length;
    let mod = 10**9 + 7;
    let res = 0;
    let freqPrev = {};
    let freqNext = {};
    for (let i = 0; i < n; i++) {
        freqNext[nums[i]] = (freqNext[nums[i]] || 0) + 1;
    }
    for (let i = 0; i < n; i++) {
        freqNext[nums[i]]--;
        if (freqPrev[nums[i] * 2] !== undefined && freqNext[nums[i] * 2] !== undefined) {
            res = (res + freqPrev[nums[i] * 2] * freqNext[nums[i] * 2]) % mod;
        }
        freqPrev[nums[i]] = (freqPrev[nums[i]] || 0) + 1;
    }
    return res;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function specialTriplets(nums: number[]): number {
    let n: number = nums.length;
    let mod: number = 10**9 + 7;
    let res: number = 0;
    let freqPrev: { [key: number]: number } = {};
    let freqNext: { [key: number]: number } = {};
    for (let i: number = 0; i < n; i++) {
        freqNext[nums[i]] = (freqNext[nums[i]] || 0) + 1;
    }
    for (let i: number = 0; i < n; i++) {
        freqNext[nums[i]]--;
        if (freqPrev[nums[i] * 2] !== undefined && freqNext[nums[i] * 2] !== undefined) {
            res = (res + freqPrev[nums[i] * 2] * freqNext[nums[i] * 2]) % mod;
        }
        freqPrev[nums[i]] = (freqPrev[nums[i]] || 0) + 1;
    }
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function specialTriplets($nums) {
        $n = count($nums);
        $mod = 10**9 + 7;
        $res = 0;
        $freqPrev = array();
        $freqNext = array();
        for ($i = 0; $i < $n; $i++) {
            if (array_key_exists($nums[$i], $freqNext)) {
                $freqNext[$nums[$i]]++;
            } else {
                $freqNext[$nums[$i]] = 1;
            }
        }
        for ($i = 0; $i < $n; $i++) {
            if (array_key_exists($nums[$i], $freqNext)) {
                $freqNext[$nums[$i]]--;
            }
            if (array_key_exists($nums[$i] * 2, $freqPrev) && array_key_exists($nums[$i] * 2, $freqNext)) {
                $res = ($res + $freqPrev[$nums[$i] * 2] * $freqNext[$nums[$i] * 2]) % $mod;
            }
            if (array_key_exists($nums[$i], $freqPrev)) {
                $freqPrev[$nums[$i]]++;
            } else {
                $freqPrev[$nums[$i]] = 1;
            }
        }
        return $res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func specialTriplets(_ nums: [Int]) -> Int {
        let n = nums.count
        let mod: Int = Int(1e9 + 7)
        var res = 0
        var freqPrev: [Int: Int] = [:]
        var freqNext: [Int: Int] = [:]
        for i in 0..<n {
            freqNext[nums[i], default: 0] += 1
        }
        for i in 0..<n {
            freqNext[nums[i], default: 0] -= 1
            if let prev = freqPrev[nums[i] * 2], let next = freqNext[nums[i] * 2] {
                res = (res + prev * next) % mod
            }
            freqPrev[nums[i], default: 0] += 1
        }
        return res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun specialTriplets(nums: IntArray): Int {
        val n = nums.size
        val mod = 1000000007
        var res = 0
        val freqPrev = mutableMapOf<Int, Int>()
        val freqNext = mutableMapOf<Int, Int>()
        for (i in 0 until n) {
            freqNext[nums[i]] = (freqNext[nums[i]] ?: 0) + 1
        }
        for (i in 0 until n) {
            freqNext[nums[i]] = (freqNext[nums[i]] ?: 0) - 1
            if (freqPrev.contains(nums[i] * 2) && freqNext.contains(nums[i] * 2)) {
                res = (res + (freqPrev[nums[i] * 2] ?: 0) * (freqNext[nums[i] * 2] ?: 0)) % mod
            }
            freqPrev[nums[i]] = (freqPrev[nums[i]] ?: 0) + 1
        }
        return res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int specialTriplets(List<int> nums) {
        int n = nums.length;
        int mod = 1000000007;
        int res = 0;
        Map<int, int> freqPrev = {};
        Map<int, int> freqNext = {};
        for (int i = 0; i < n; i++) {
            freqNext[nums[i]] = (freqNext[nums[i]] ?? 0) + 1;
        }
        for (int i = 0; i < n; i++) {
            freqNext[nums[i]] = (freqNext[nums[i]] ?? 0) - 1;
            if (freqPrev.containsKey(nums[i] * 2) && freqNext.containsKey(nums[i] * 2)) {
                res = (res + (freqPrev[nums[i] * 2] ?? 0) * (freqNext[nums[i] * 2] ?? 0)) % mod;
            }
            freqPrev[nums[i]] = (freqPrev[nums[i]] ?? 0) + 1;
        }
        return res;
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
    "fmt"
)

type Solution struct{}

func (s Solution) specialTriplets(nums []int) int {
    n := len(nums)
    mod := 1000000007
    res := 0
    freqPrev := make(map[int]int)
    freqNext := make(map[int]int)
    for i := 0; i < n; i++ {
        freqNext[nums[i]]++
    }
    for i := 0; i < n; i++ {
        freqNext[nums[i]]--
        if _, ok := freqPrev[nums[i]*2]; ok && _, ok := freqNext[nums[i]*2]; ok {
            res = (res + freqPrev[nums[i]*2]*freqNext[nums[i]*2]) % mod
        }
        freqPrev[nums[i]]++
    }
    return res
}

func main() {
    solution := Solution{}
    nums := []int{6, 3, 6}
    fmt.Println(solution.specialTriplets(nums))
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    def special_triplets(nums)
        n = nums.size
        mod = 10**9 + 7
        res = 0
        freq_prev = {}
        freq_next = {}
        nums.each do |num|
            freq_next[num] = (freq_next[num] || 0) + 1
        end
        nums.each_with_index do |num, i|
            freq_next[num] -= 1
            if freq_prev.key?(num * 2) && freq_next.key?(num * 2)
                res = (res + freq_prev[num * 2] * freq_next[num * 2]) % mod
            end
            freq_prev[num] = (freq_prev[num] || 0) + 1
        end
        res
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def specialTriplets(nums: Array[Int]): Int = {
        val n = nums.length
        val mod = 1000000007
        var res = 0
        val freqPrev = scala.collection.mutable.Map[Int, Int]().withDefaultValue(0)
        val freqNext = scala.collection.mutable.Map[Int, Int]().withDefaultValue(0)
        for (i <- 0 until n) {
            freqNext(nums(i)) += 1
        }
        for (i <- 0 until n) {
            freqNext(nums(i)) -= 1
            if (freqPrev.contains(nums(i) * 2) && freqNext.contains(nums(i) * 2)) {
                res = (res + freqPrev(nums(i) * 2) * freqNext(nums(i) * 2)) % mod
            }
            freqPrev(nums(i)) += 1
        }
        res
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
    pub fn special_triplests(nums: Vec<i32>) -> i32 {
        let n = nums.len() as i32;
        let mod = 1000000007;
        let mut res = 0;
        let mut freq_prev: std::collections::HashMap<i32, i32> = std::collections::HashMap::new();
        let mut freq_next: std::collections::HashMap<i32, i32> = std::collections::HashMap::new();
        for &num in nums.iter() {
            *freq_next.entry(num).or_insert(0) += 1;
        }
        for &num in nums.iter() {
            *freq_next.entry(num).or_insert(0) -= 1;
            if let Some(&prev) = freq_prev.get(&(num * 2)) {
                if let Some(&next) = freq_next.get(&(num * 2)) {
                    res = (res + prev * next) % mod;
                }
            }
            *freq_prev.entry(num).or_insert(0) += 1;
        }
        res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
define (special-triplets nums)
    (let* (
        (n (length nums))
        (mod 1000000007)
        (res 0)
        (freq-prev (make-hash))
        (freq-next (make-hash))
        )
        (for (
            (
            (i 0)
            (< i n)
            (add1 i)
            )
            )
            (hash-set! freq-next (list-ref nums i) (+ (hash-ref freq-next (list-ref nums i) 0) 1))
            )
        (for (
            (
            (i 0)
            (< i n)
            (add1 i)
            )
            )
            (begin
                (hash-set! freq-next (list-ref nums i) (- (hash-ref freq-next (list-ref nums i) 0) 1))
                (when (and (hash-has-key? freq-prev (* (list-ref nums i) 2)) (hash-has-key? freq-next (* (list-ref nums i) 2)))
                    (set! res (modulo (+ res (* (hash-ref freq-prev (* (list-ref nums i) 2) 0) (hash-ref freq-next (* (list-ref nums i) 2) 0))) mod))
                    )
                (hash-set! freq-prev (list-ref nums i) (+ (hash-ref freq-prev (list-ref nums i) 0) 1))
                )
            )
        res
        )
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
special_triplests(Nums) ->
    Res = special_triplests(Nums, 0, dict:new(), dict:new()),
    Res.

special_triplests([], Res, _, _) -> Res;
special_triplests([Num|Nums], Res, FreqPrev, FreqNext) ->
    NewFreqNext = dict:update_counter(Num, 1, FreqNext),
    special_triplests(Nums, Res, FreqPrev, NewFreqNext).

special_triplests(Nums) ->
    special_triplests(Nums, 0, dict:new(), dict:new()).

special_triplests([Num|Nums], Res, FreqPrev, FreqNext) ->
    NewFreqNext = dict:update_counter(Num, -1, FreqNext),
    case dict:find(Num*2, FreqPrev) of
        {ok, Prev} ->
            case dict:find(Num*2, FreqNext) of
                {ok, Next} ->
                    NewRes = (Res + Prev*Next) rem 1000000007,
                    special_triplests(Nums, NewRes, dict:update_counter(Num, 1, FreqPrev), NewFreqNext);
                _ -> special_triplests(Nums, Res, dict:update_counter(Num, 1, FreqPrev), NewFreqNext)
            end;
        _ -> special_triplests(Nums, Res, dict:update_counter(Num, 1, FreqPrev), NewFreqNext)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
    def special_triplests(nums) do
        n = length(nums)
        mod = 1000000007
        res = 0
        freq_prev = %{}
        freq_next = %{}
        Enum.reduce(nums, {res, freq_prev, freq_next}, fn num, {res, freq_prev, freq_next} ->
            freq_next = Map.update(freq_next, num, 1, &(&1 + 1))
            {res, freq_prev, freq_next}
        end)
        |> elem(1)
        |> Enum.reduce(nums, fn num, {res, freq_prev, freq_next} ->
            freq_next = Map.update(freq_next, num, 0, &(&1 - 1))
            if Map.has_key?(freq_prev, num * 2) and Map.has_key?(freq_next, num * 2) do
                res = rem(res + Map.get(freq_prev, num * 2) * Map.get(freq_next, num * 2), mod)
            end
            freq_prev = Map.update(freq_prev, num, 1, &(&1 + 1))
            {res, freq_prev, freq_next}
        end)
        |> elem(0)
    end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of the algorithm is O(n), where n is the length of the input array. This is because we iterate over the array once, and for each index, we perform a constant amount of work to compute its contribution to the answer and update the frequency counts.

- **Space Complexity:** The space complexity of the algorithm is O(n), where n is the length of the input array. This is because we need to store the frequency counts for each value in the array, and in the worst case, every value in the array is unique, requiring O(n) space to store the frequency counts.

</div>
</details>
