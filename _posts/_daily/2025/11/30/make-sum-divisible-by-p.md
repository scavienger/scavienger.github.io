---
layout: post
title: "Make Sum Divisible by P"
date: 2025-11-30 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Prefix Sum"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/make-sum-divisible-by-p/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minSubarray(std::vector<int>& nums, int\
        \ p) {\n        long long total_sum = 0;\n        for (int num : nums) {\n \
        \           total_sum += num;\n        }\n\n        int target_rem = total_sum\
        \ % p;\n\n        if (target_rem == 0) {\n            return 0;\n        }\n\
        \n        std::unordered_map<int, int> prefix_rem_map;\n        prefix_rem_map[0]\
        \ = -1; // Represents prefix sum 0 before index 0\n\n        long long current_prefix_sum\
        \ = 0;\n        int min_len = nums.size();\n\n        for (int i = 0; i < nums.size();\
        \ ++i) {\n            current_prefix_sum = (current_prefix_sum + nums[i]) %\
        \ p;\n\n            // We need (current_prefix_sum - prev_prefix_sum_rem + p)\
        \ % p == target_rem\n            // So, prev_prefix_sum_rem = (current_prefix_sum\
        \ - target_rem + p) % p\n            int required_prev_rem = (current_prefix_sum\
        \ - target_rem + p) % p;\n\n            if (prefix_rem_map.count(required_prev_rem))\
        \ {\n                min_len = std::min(min_len, i - prefix_rem_map[required_prev_rem]);\n\
        \            }\n            prefix_rem_map[current_prefix_sum] = i;\n      \
        \  }\n\n        return min_len == nums.size() ? -1 : min_len;\n    }\n};"
      java: "import java.util.HashMap;\nimport java.util.Map;\n\nclass Solution {\n\
        \    public int minSubarray(int[] nums, int p) {\n        long totalSum = 0;\n\
        \        for (int num : nums) {\n            totalSum += num;\n        }\n\n\
        \        int targetRem = (int) (totalSum % p);\n\n        if (targetRem == 0)\
        \ {\n            return 0;\n        }\n\n        Map<Integer, Integer> prefixRemMap\
        \ = new HashMap<>();\n        prefixRemMap.put(0, -1); // Represents prefix\
        \ sum 0 before index 0\n\n        long currentPrefixSum = 0;\n        int minLen\
        \ = nums.length;\n\n        for (int i = 0; i < nums.length; ++i) {\n      \
        \      currentPrefixSum = (currentPrefixSum + nums[i]) % p;\n\n            //\
        \ We need (currentPrefixSum - prevPrefixSumRem + p) % p == targetRem\n     \
        \       // So, prevPrefixSumRem = (currentPrefixSum - targetRem + p) % p\n \
        \           int requiredPrevRem = (int) ((currentPrefixSum - targetRem + p)\
        \ % p);\n\n            if (prefixRemMap.containsKey(requiredPrevRem)) {\n  \
        \              minLen = Math.min(minLen, i - prefixRemMap.get(requiredPrevRem));\n\
        \            }\n            prefixRemMap.put((int) currentPrefixSum, i);\n \
        \       }\n\n        return minLen == nums.length ? -1 : minLen;\n    }\n}"
      python: "class Solution:\n    def minSubarray(self, nums: list[int], p: int) ->\
        \ int:\n        total_sum = sum(nums)\n        target_rem = total_sum % p\n\n\
        \        if target_rem == 0:\n            return 0\n\n        prefix_rem_map\
        \ = {0: -1} # Represents prefix sum 0 before index 0\n        current_prefix_sum\
        \ = 0\n        min_len = len(nums)\n\n        for i, num in enumerate(nums):\n\
        \            current_prefix_sum = (current_prefix_sum + num) % p\n\n       \
        \     # We need (current_prefix_sum - prev_prefix_sum_rem + p) % p == target_rem\n\
        \            # So, prev_prefix_sum_rem = (current_prefix_sum - target_rem +\
        \ p) % p\n            required_prev_rem = (current_prefix_sum - target_rem +\
        \ p) % p\n\n            if required_prev_rem in prefix_rem_map:\n          \
        \      min_len = min(min_len, i - prefix_rem_map[required_prev_rem])\n\n   \
        \         prefix_rem_map[current_prefix_sum] = i\n\n        return min_len if\
        \ min_len != len(nums) else -1"
      python3: "class Solution:\n    def minSubarray(self, nums: list[int], p: int)\
        \ -> int:\n        total_sum = sum(nums)\n        target_rem = total_sum % p\n\
        \n        if target_rem == 0:\n            return 0\n\n        prefix_rem_map\
        \ = {0: -1} # Represents prefix sum 0 before index 0\n        current_prefix_sum\
        \ = 0\n        min_len = len(nums)\n\n        for i, num in enumerate(nums):\n\
        \            current_prefix_sum = (current_prefix_sum + num) % p\n\n       \
        \     # We need (current_prefix_sum - prev_prefix_sum_rem + p) % p == target_rem\n\
        \            # So, prev_prefix_sum_rem = (current_prefix_sum - target_rem +\
        \ p) % p\n            required_prev_rem = (current_prefix_sum - target_rem +\
        \ p) % p\n\n            if required_prev_rem in prefix_rem_map:\n          \
        \      min_len = min(min_len, i - prefix_rem_map[required_prev_rem])\n\n   \
        \         prefix_rem_map[current_prefix_sum] = i\n\n        return min_len if\
        \ min_len != len(nums) else -1"
      c: "#include <stdlib.h>\n#include <string.h>\n#include <stdio.h>\n\n// Basic hash\
        \ table implementation for (remainder, index) pairs\n// Using open addressing\
        \ with linear probing\n\ntypedef struct {\n    int key; // remainder\n    int\
        \ value; // index\n    int occupied; // 0: empty, 1: occupied\n} Entry;\n\n\
        typedef struct {\n    Entry* table;\n    int capacity;\n    int size;\n} HashTable;\n\
        \n// A simple hash function\nunsigned int hash(int key, int capacity) {\n  \
        \  return (unsigned int)key % capacity;\n}\n\n// Initialize hash table\nHashTable*\
        \ createHashTable(int capacity) {\n    HashTable* ht = (HashTable*)malloc(sizeof(HashTable));\n\
        \    ht->capacity = capacity;\n    ht->size = 0;\n    ht->table = (Entry*)calloc(capacity,\
        \ sizeof(Entry));\n    return ht;\n}\n\n// Insert or update an entry\nvoid ht_put(HashTable*\
        \ ht, int key, int value) {\n    unsigned int index = hash(key, ht->capacity);\n\
        \    while (ht->table[index].occupied) {\n        if (ht->table[index].key ==\
        \ key) {\n            ht->table[index].value = value; // Update value\n    \
        \        return;\n        }\n        index = (index + 1) % ht->capacity;\n \
        \   }\n    // Found an empty slot or key not found\n    ht->table[index].key\
        \ = key;\n    ht->table[index].value = value;\n    ht->table[index].occupied\
        \ = 1;\n    ht->size++;\n}\n\n// Get an entry\nint ht_get(HashTable* ht, int\
        \ key, int* value) {\n    unsigned int index = hash(key, ht->capacity);\n  \
        \  while (ht->table[index].occupied) {\n        if (ht->table[index].key ==\
        \ key) {\n            *value = ht->table[index].value;\n            return 1;\
        \ // Found\n        }\n        index = (index + 1) % ht->capacity;\n    }\n\
        \    return 0; // Not found\n}\n\n// Free hash table\nvoid freeHashTable(HashTable*\
        \ ht) {\n    free(ht->table);\n    free(ht);\n}\n\nint min(int a, int b) {\n\
        \    return a < b ? a : b;\n}\n\nint minSubarray(int* nums, int numsSize, int\
        \ p) {\n    long long total_sum = 0;\n    for (int i = 0; i < numsSize; ++i)\
        \ {\n        total_sum += nums[i];\n    }\n\n    int target_rem = total_sum\
        \ % p;\n\n    if (target_rem == 0) {\n        return 0;\n    }\n\n    // Hash\
        \ table capacity should be a prime number larger than numsSize\n    // For simplicity,\
        \ using numsSize * 2. A more robust solution might use a prime number.\n   \
        \ HashTable* prefix_rem_map = createHashTable(numsSize * 2 + 1); \n    ht_put(prefix_rem_map,\
        \ 0, -1); // Represents prefix sum 0 before index 0\n\n    long long current_prefix_sum\
        \ = 0;\n    int min_len = numsSize;\n\n    for (int i = 0; i < numsSize; ++i)\
        \ {\n        current_prefix_sum = (current_prefix_sum + nums[i]) % p;\n\n  \
        \      // We need (current_prefix_sum - prev_prefix_sum_rem + p) % p == target_rem\n\
        \        // So, prev_prefix_sum_rem = (current_prefix_sum - target_rem + p)\
        \ % p\n        int required_prev_rem = (current_prefix_sum - target_rem + p)\
        \ % p;\n\n        int prev_idx;\n        if (ht_get(prefix_rem_map, required_prev_rem,\
        \ &prev_idx)) {\n            min_len = min(min_len, i - prev_idx);\n       \
        \ }\n        ht_put(prefix_rem_map, current_prefix_sum, i);\n    }\n\n    freeHashTable(prefix_rem_map);\n\
        \n    return min_len == numsSize ? -1 : min_len;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int MinSubarray(int[] nums, int p) {\n        long totalSum\
        \ = 0;\n        foreach (int num in nums) {\n            totalSum += num;\n\
        \        }\n\n        int targetRem = (int)(totalSum % p);\n\n        if (targetRem\
        \ == 0) {\n            return 0;\n        }\n\n        Dictionary<int, int>\
        \ prefixRemMap = new Dictionary<int, int>();\n        prefixRemMap[0] = -1;\
        \ // Represents prefix sum 0 before index 0\n\n        long currentPrefixSum\
        \ = 0;\n        int minLen = nums.Length;\n\n        for (int i = 0; i < nums.Length;\
        \ ++i) {\n            currentPrefixSum = (currentPrefixSum + nums[i]) % p;\n\
        \n            // We need (currentPrefixSum - prevPrefixSumRem + p) % p == targetRem\n\
        \            // So, prevPrefixSumRem = (currentPrefixSum - targetRem + p) %\
        \ p\n            int requiredPrevRem = (int)((currentPrefixSum - targetRem +\
        \ p) % p);\n\n            if (prefixRemMap.ContainsKey(requiredPrevRem)) {\n\
        \                minLen = Math.Min(minLen, i - prefixRemMap[requiredPrevRem]);\n\
        \            }\n            prefixRemMap[(int)currentPrefixSum] = i;\n     \
        \   }\n\n        return minLen == nums.Length ? -1 : minLen;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} p\n * @return\
        \ {number}\n */\nvar minSubarray = function(nums, p) {\n    let totalSum = 0n;\
        \ // Use BigInt for total sum\n    for (let num of nums) {\n        totalSum\
        \ += BigInt(num);\n    }\n\n    const P_BIGINT = BigInt(p);\n    let targetRem\
        \ = totalSum % P_BIGINT;\n\n    if (targetRem === 0n) {\n        return 0;\n\
        \    }\n\n    const prefixRemMap = new Map();\n    prefixRemMap.set(0, -1);\
        \ // Represents prefix sum 0 before index 0\n\n    let currentPrefixSum = 0n;\
        \ // Use BigInt for current prefix sum\n    let minLen = nums.length;\n\n  \
        \  for (let i = 0; i < nums.length; ++i) {\n        currentPrefixSum = (currentPrefixSum\
        \ + BigInt(nums[i])) % P_BIGINT;\n\n        // We need (currentPrefixSum - prevPrefixSumRem\
        \ + P_BIGINT) % P_BIGINT == targetRem\n        // So, prevPrefixSumRem = (currentPrefixSum\
        \ - targetRem + P_BIGINT) % P_BIGINT\n        let requiredPrevRem = (currentPrefixSum\
        \ - targetRem + P_BIGINT) % P_BIGINT;\n\n        // Convert BigInt remainder\
        \ back to number for map key\n        if (prefixRemMap.has(Number(requiredPrevRem)))\
        \ {\n            minLen = Math.min(minLen, i - prefixRemMap.get(Number(requiredPrevRem)));\n\
        \        }\n        prefixRemMap.set(Number(currentPrefixSum), i);\n    }\n\n\
        \    return minLen === nums.length ? -1 : minLen;\n};"
      typescript: "function minSubarray(nums: number[], p: number): number {\n    let\
        \ totalSum: bigint = 0n; // Use BigInt for total sum\n    for (let num of nums)\
        \ {\n        totalSum += BigInt(num);\n    }\n\n    const P_BIGINT: bigint =\
        \ BigInt(p);\n    let targetRem: bigint = totalSum % P_BIGINT;\n\n    if (targetRem\
        \ === 0n) {\n        return 0;\n    }\n\n    const prefixRemMap: Map<number,\
        \ number> = new Map();\n    prefixRemMap.set(0, -1); // Represents prefix sum\
        \ 0 before index 0\n\n    let currentPrefixSum: bigint = 0n; // Use BigInt for\
        \ current prefix sum\n    let minLen: number = nums.length;\n\n    for (let\
        \ i = 0; i < nums.length; ++i) {\n        currentPrefixSum = (currentPrefixSum\
        \ + BigInt(nums[i])) % P_BIGINT;\n\n        // We need (currentPrefixSum - prevPrefixSumRem\
        \ + P_BIGINT) % P_BIGINT == targetRem\n        // So, prevPrefixSumRem = (currentPrefixSum\
        \ - targetRem + P_BIGINT) % P_BIGINT\n        let requiredPrevRem: bigint =\
        \ (currentPrefixSum - targetRem + P_BIGINT) % P_BIGINT;\n\n        // Convert\
        \ BigInt remainder back to number for map key\n        if (prefixRemMap.has(Number(requiredPrevRem)))\
        \ {\n            minLen = Math.min(minLen, i - prefixRemMap.get(Number(requiredPrevRem))!);\n\
        \        }\n        prefixRemMap.set(Number(currentPrefixSum), i);\n    }\n\n\
        \    return minLen === nums.length ? -1 : minLen;\n}"
      php: "<?php\nclass Solution {\n    /**\n     * @param Integer[] $nums\n     *\
        \ @param Integer $p\n     * @return Integer\n     */\n    function minSubarray($nums,\
        \ $p) {\n        $totalSum = 0;\n        foreach ($nums as $num) {\n       \
        \     $totalSum += $num;\n        }\n\n        $targetRem = $totalSum % $p;\n\
        \n        if ($targetRem == 0) {\n            return 0;\n        }\n\n     \
        \   $prefixRemMap = [0 => -1]; // Represents prefix sum 0 before index 0\n\n\
        \        $currentPrefixSum = 0;\n        $minLen = count($nums);\n\n       \
        \ for ($i = 0; $i < count($nums); ++$i) {\n            $currentPrefixSum = ($currentPrefixSum\
        \ + $nums[$i]) % $p;\n\n            // We need (currentPrefixSum - prevPrefixSumRem\
        \ + p) % p == targetRem\n            // So, prevPrefixSumRem = (currentPrefixSum\
        \ - targetRem + p) % p\n            $requiredPrevRem = ($currentPrefixSum -\
        \ $targetRem + $p) % $p;\n\n            if (array_key_exists($requiredPrevRem,\
        \ $prefixRemMap)) {\n                $minLen = min($minLen, $i - $prefixRemMap[$requiredPrevRem]);\n\
        \            }\n            $prefixRemMap[$currentPrefixSum] = $i;\n       \
        \ }\n\n        return $minLen == count($nums) ? -1 : $minLen;\n    }\n}"
      swift: "class Solution {\n    func minSubarray(_ nums: [Int], _ p: Int) -> Int\
        \ {\n        var totalSum: Int = 0\n        for num in nums {\n            totalSum\
        \ += num\n        }\n\n        let targetRem: Int = totalSum % p\n\n       \
        \ if targetRem == 0 {\n            return 0\n        }\n\n        var prefixRemMap:\
        \ [Int: Int] = [0: -1] // Represents prefix sum 0 before index 0\n\n       \
        \ var currentPrefixSum: Int = 0\n        var minLen: Int = nums.count\n\n  \
        \      for i in 0..<nums.count {\n            currentPrefixSum = (currentPrefixSum\
        \ + nums[i]) % p\n\n            // We need (currentPrefixSum - prevPrefixSumRem\
        \ + p) % p == targetRem\n            // So, prevPrefixSumRem = (currentPrefixSum\
        \ - targetRem + p) % p\n            let requiredPrevRem: Int = (currentPrefixSum\
        \ - targetRem + p) % p\n\n            if let prevIdx = prefixRemMap[requiredPrevRem]\
        \ {\n                minLen = min(minLen, i - prevIdx)\n            }\n    \
        \        prefixRemMap[currentPrefixSum] = i\n        }\n\n        return minLen\
        \ == nums.count ? -1 : minLen\n    }\n}"
      kotlin: "class Solution {\n    fun minSubarray(nums: IntArray, p: Int): Int {\n\
        \        var totalSum: Long = 0\n        for (num in nums) {\n            totalSum\
        \ += num\n        }\n\n        val targetRem: Int = (totalSum % p).toInt()\n\
        \n        if (targetRem == 0) {\n            return 0\n        }\n\n       \
        \ val prefixRemMap: MutableMap<Int, Int> = mutableMapOf()\n        prefixRemMap[0]\
        \ = -1 // Represents prefix sum 0 before index 0\n\n        var currentPrefixSum:\
        \ Long = 0\n        var minLen: Int = nums.size\n\n        for (i in nums.indices)\
        \ {\n            currentPrefixSum = (currentPrefixSum + nums[i]) % p\n\n   \
        \         // We need (currentPrefixSum - prevPrefixSumRem + p) % p == targetRem\n\
        \            // So, prevPrefixSumRem = (currentPrefixSum - targetRem + p) %\
        \ p\n            val requiredPrevRem: Int = ((currentPrefixSum - targetRem +\
        \ p) % p).toInt()\n\n            if (prefixRemMap.containsKey(requiredPrevRem))\
        \ {\n                minLen = minOf(minLen, i - prefixRemMap[requiredPrevRem]!!)\n\
        \            }\n            prefixRemMap[currentPrefixSum.toInt()] = i\n   \
        \     }\n\n        return if (minLen == nums.size) -1 else minLen\n    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int minSubarray(List<int> nums,\
        \ int p) {\n    BigInt totalSum = BigInt.zero;\n    for (int num in nums) {\n\
        \      totalSum += BigInt.from(num);\n    }\n\n    BigInt pBigInt = BigInt.from(p);\n\
        \    BigInt targetRem = totalSum % pBigInt;\n\n    if (targetRem == BigInt.zero)\
        \ {\n      return 0;\n    }\n\n    Map<int, int> prefixRemMap = {0: -1}; //\
        \ Represents prefix sum 0 before index 0\n\n    BigInt currentPrefixSum = BigInt.zero;\n\
        \    int minLen = nums.length;\n\n    for (int i = 0; i < nums.length; ++i)\
        \ {\n      currentPrefixSum = (currentPrefixSum + BigInt.from(nums[i])) % pBigInt;\n\
        \n      // We need (currentPrefixSum - prevPrefixSumRem + pBigInt) % pBigInt\
        \ == targetRem\n      // So, prevPrefixSumRem = (currentPrefixSum - targetRem\
        \ + pBigInt) % pBigInt\n      BigInt requiredPrevRemBigInt = (currentPrefixSum\
        \ - targetRem + pBigInt) % pBigInt;\n      int requiredPrevRem = requiredPrevRemBigInt.toInt();\n\
        \n      if (prefixRemMap.containsKey(requiredPrevRem)) {\n        minLen = min(minLen,\
        \ i - prefixRemMap[requiredPrevRem]!);\n      }\n      prefixRemMap[currentPrefixSum.toInt()]\
        \ = i;\n    }\n\n    return minLen == nums.length ? -1 : minLen;\n  }\n}"
      go: "package main\n\nimport (\n\t\"math\"\n)\n\nfunc minSubarray(nums []int, p\
        \ int) int {\n    var totalSum int64 = 0\n    for _, num := range nums {\n \
        \       totalSum += int64(num)\n    }\n\n    targetRem := int(totalSum % int64(p))\n\
        \n    if targetRem == 0 {\n        return 0\n    }\n\n    prefixRemMap := make(map[int]int)\n\
        \    prefixRemMap[0] = -1 // Represents prefix sum 0 before index 0\n\n    var\
        \ currentPrefixSum int64 = 0\n    minLen := len(nums)\n\n    for i := 0; i <\
        \ len(nums); i++ {\n        currentPrefixSum = (currentPrefixSum + int64(nums[i]))\
        \ % int64(p)\n\n        // We need (currentPrefixSum - prevPrefixSumRem + p)\
        \ % p == targetRem\n        // So, prevPrefixSumRem = (currentPrefixSum - targetRem\
        \ + p) % p\n        requiredPrevRem := int((currentPrefixSum - int64(targetRem)\
        \ + int64(p)) % int64(p))\n\n        if prevIdx, ok := prefixRemMap[requiredPrevRem];\
        \ ok {\n            minLen = int(math.Min(float64(minLen), float64(i - prevIdx)))\n\
        \        }\n        prefixRemMap[int(currentPrefixSum)] = i\n    }\n\n    if\
        \ minLen == len(nums) {\n        return -1\n    }\n    return minLen\n}"
      ruby: "class Solution\n    def min_subarray(nums, p)\n        total_sum = nums.sum\n\
        \        target_rem = total_sum % p\n\n        return 0 if target_rem == 0\n\
        \n        prefix_rem_map = {0 => -1} # Represents prefix sum 0 before index\
        \ 0\n        current_prefix_sum = 0\n        min_len = nums.length\n\n     \
        \   nums.each_with_index do |num, i|\n            current_prefix_sum = (current_prefix_sum\
        \ + num) % p\n\n            # We need (current_prefix_sum - prev_prefix_sum_rem\
        \ + p) % p == target_rem\n            # So, prev_prefix_sum_rem = (current_prefix_sum\
        \ - target_rem + p) % p\n            required_prev_rem = (current_prefix_sum\
        \ - target_rem + p) % p\n\n            if prefix_rem_map.key?(required_prev_rem)\n\
        \                min_len = [min_len, i - prefix_rem_map[required_prev_rem]].min\n\
        \            end\n            prefix_rem_map[current_prefix_sum] = i\n     \
        \   end\n\n        min_len == nums.length ? -1 : min_len\n    end\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n    def minSubarray(nums:\
        \ Array[Int], p: Int): Int = {\n        var totalSum: Long = nums.map(_.toLong).sum\n\
        \        val targetRem: Int = (totalSum % p).toInt\n\n        if (targetRem\
        \ == 0) {\n            return 0\n        }\n\n        val prefixRemMap: mutable.HashMap[Int,\
        \ Int] = mutable.HashMap(0 -> -1) // Represents prefix sum 0 before index 0\n\
        \n        var currentPrefixSum: Long = 0\n        var minLen: Int = nums.length\n\
        \n        for (i <- nums.indices) {\n            currentPrefixSum = (currentPrefixSum\
        \ + nums(i)) % p\n\n            // We need (currentPrefixSum - prevPrefixSumRem\
        \ + p) % p == targetRem\n            // So, prevPrefixSumRem = (currentPrefixSum\
        \ - targetRem + p) % p\n            val requiredPrevRem: Int = ((currentPrefixSum\
        \ - targetRem + p) % p).toInt\n\n            if (prefixRemMap.contains(requiredPrevRem))\
        \ {\n                minLen = math.min(minLen, i - prefixRemMap(requiredPrevRem))\n\
        \            }\n            prefixRemMap(currentPrefixSum.toInt) = i\n     \
        \   }\n\n        if (minLen == nums.length) -1 else minLen\n    }\n}"
      rust: "use std::collections::HashMap;\nuse std::cmp::min;\n\nimpl Solution {\n\
        \    pub fn min_subarray(nums: Vec<i32>, p: i32) -> i32 {\n        let mut total_sum:\
        \ i64 = 0;\n        for &num in &nums {\n            total_sum += num as i64;\n\
        \        }\n\n        let target_rem: i32 = (total_sum % p as i64) as i32;\n\
        \n        if target_rem == 0 {\n            return 0;\n        }\n\n       \
        \ let mut prefix_rem_map: HashMap<i32, i32> = HashMap::new();\n        prefix_rem_map.insert(0,\
        \ -1); // Represents prefix sum 0 before index 0\n\n        let mut current_prefix_sum:\
        \ i64 = 0;\n        let mut min_len: i32 = nums.len() as i32;\n\n        for\
        \ i in 0..nums.len() {\n            current_prefix_sum = (current_prefix_sum\
        \ + nums[i] as i64) % p as i64;\n\n            // We need (current_prefix_sum\
        \ - prev_prefix_sum_rem + p) % p == target_rem\n            // So, prev_prefix_sum_rem\
        \ = (current_prefix_sum - target_rem + p) % p\n            let required_prev_rem:\
        \ i32 = ((current_prefix_sum - target_rem as i64 + p as i64) % p as i64) as\
        \ i32;\n\n            if let Some(&prev_idx) = prefix_rem_map.get(&required_prev_rem)\
        \ {\n                min_len = min(min_len, i as i32 - prev_idx);\n        \
        \    }\n            prefix_rem_map.insert(current_prefix_sum as i32, i as i32);\n\
        \        }\n\n        if min_len == nums.len() as i32 {\n            -1\n  \
        \      } else {\n            min_len\n        }\n    }\n}"
      racket: "#lang racket\n\n(define (min-subarray nums p)\n  (define total-sum (apply\
        \ + nums))\n  (define target-rem (modulo total-sum p))\n\n  (when (= target-rem\
        \ 0)\n    (hash-clear! (make-hash))\n    (void))\n\n  (if (= target-rem 0)\n\
        \      0\n      (let* ((prefix-rem-map (make-hash))\n             (n (length\
        \ nums))\n             (min-len n))\n        (hash-set! prefix-rem-map 0 -1)\n\
        \        (define current-prefix-sum 0)\n\n        (for ([num (in-list nums)]\n\
        \              [i (in-range n)])\n          (set! current-prefix-sum (modulo\
        \ (+ current-prefix-sum num) p))\n\n          (define required-prev-rem (modulo\
        \ (- (+ current-prefix-sum p) target-rem) p))\n\n          (when (hash-has-key?\
        \ prefix-rem-map required-prev-rem)\n            (set! min-len (min min-len\
        \ (- i (hash-ref prefix-rem-map required-prev-rem)))))\n\n          (hash-set!\
        \ prefix-rem-map current-prefix-sum i))\n\n        (if (= min-len n) -1 min-len))))"
      erlang: "-module(solution).\n-export([min_subarray/2]).\n\nmin_subarray(Nums,\
        \ P) ->\nTotalSum = lists:sum(Nums),\nTargetRem = TotalSum rem P,\n\nif TargetRem\
        \ == 0 ->\n0;\ntrue ->\nPrefixRemMap = maps:put(0, -1, #{}),\nCurrentPrefixSum\
        \ = 0,\nMinLen = length(Nums),\n\nmin_subarray_loop(Nums, P, TargetRem, PrefixRemMap,\
        \ CurrentPrefixSum, MinLen, 0)\nend.\n\nmin_subarray_loop([], _P, _TargetRem,\
        \ _PrefixRemMap, _CurrentPrefixSum, MinLen, N) ->\nif MinLen == N -> -1; true\
        \ -> MinLen end;\nmin_subarray_loop([Num | Rest], P, TargetRem, PrefixRemMap,\
        \ CurrentPrefixSum, MinLen, I) ->\nNewCurrentPrefixSum = (CurrentPrefixSum +\
        \ Num) rem P,\n\nRequiredPrevRem = (NewCurrentPrefixSum - TargetRem + P) rem\
        \ P,\n\nNewMinLen = \ncase maps:find(RequiredPrevRem, PrefixRemMap) of\n   \
        \ {ok, PrevIdx} -> min(MinLen, I - PrevIdx);\n    _ -> MinLen\nend,\n\nNewPrefixRemMap\
        \ = maps:put(NewCurrentPrefixSum, I, PrefixRemMap),\n\nmin_subarray_loop(Rest,\
        \ P, TargetRem, NewPrefixRemMap, NewCurrentPrefixSum, NewMinLen, I + 1)."
      elixir: "defmodule Solution do\n  @spec min_subarray(nums :: [integer], p :: integer)\
        \ :: integer\n  def min_subarray(nums, p) do\n    total_sum = Enum.sum(nums)\n\
        \    target_rem = rem(total_sum, p)\n\n    if target_rem == 0 do\n      0\n\
        \    else\n      prefix_rem_map = %{0 => -1}\n      current_prefix_sum = 0\n\
        \      min_len = length(nums)\n\n      {_final_prefix_rem_map, final_min_len}\
        \ = Enum.reduce(0..(length(nums) - 1), {prefix_rem_map, min_len, current_prefix_sum},\
        \ fn i, {acc_map, acc_min_len, acc_current_prefix_sum} ->\n        num = Enum.at(nums,\
        \ i)\n        new_current_prefix_sum = rem(acc_current_prefix_sum + num, p)\n\
        \n        required_prev_rem = rem(new_current_prefix_sum - target_rem + p, p)\n\
        \n        new_min_len = \n          case Map.fetch(acc_map, required_prev_rem)\
        \ do\n            {:ok, prev_idx} -> min(acc_min_len, i - prev_idx)\n      \
        \      :error -> acc_min_len\n          end\n\n        new_acc_map = Map.put(acc_map,\
        \ new_current_prefix_sum, i)\n        {new_acc_map, new_min_len, new_current_prefix_sum}\n\
        \      end)\n\n      if final_min_len == length(nums) do\n        -1\n     \
        \ else\n        final_min_len\n      end\n    end\n  end\nend"
    approach: The problem asks us to find the smallest subarray to remove such that
      the sum of the remaining elements is divisible by `p`. Let `S` be the total sum
      of all elements in `nums`. If we remove a subarray with sum `S_sub`, the sum of
      the remaining elements is `S - S_sub`. We want `(S - S_sub) % p == 0`, which implies
      `S % p == S_sub % p`. Let `target_rem = S % p`. If `target_rem` is 0, the total
      sum is already divisible by `p`, so we don't need to remove anything, and the
      answer is 0. Otherwise, we need to find a subarray `nums[k...i]` whose sum `S_sub`
      satisfies `S_sub % p == target_rem`, and we want this subarray to be as short
      as possible. We are not allowed to remove the entire array.
    time_complexity: The time complexity is O(N), where N is the length of the `nums`
      array. We iterate through the array once to calculate the total sum and once more
      to compute prefix sums and update the hash map. Each hash map operation (insertion
      and lookup) takes O(1) on average.
    space_complexity: The space complexity is O(N) in the worst case. The hash map stores
      at most N distinct prefix sum remainders along with their indices. In the worst
      case, all N prefix sum remainders modulo `p` could be unique, requiring N entries
      in the map.
    elapsed_time: 79.46930694580078
    model: gemini-2.5-flash
    generated_at: '2025-11-30 01:12:49 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int minSubarray(vector<int>& nums, int p)\
        \ {\n        int n = nums.size();\n        long long sum = 0;\n        for (int\
        \ num : nums) sum += num;\n        if (sum % p == 0) return 0;\n        long\
        \ long target = sum % p;\n        long long currSum = 0;\n        int res =\
        \ n;\n        for (int i = 0; i < n; i++) {\n            currSum = 0;\n    \
        \        for (int j = i; j < n; j++) {\n                currSum += nums[j];\n\
        \                if ((sum - currSum) % p == 0) res = min(res, j - i + 1);\n\
        \            }\n        }\n        return res == n ? -1 : res;\n    }\n};"
      java: "class Solution {\n    public int minSubarray(int[] nums, int p) {\n   \
        \     int n = nums.length;\n        long sum = 0;\n        for (int num : nums)\
        \ sum += num;\n        if (sum % p == 0) return 0;\n        long target = sum\
        \ % p;\n        long currSum = 0;\n        int res = n;\n        for (int i\
        \ = 0; i < n; i++) {\n            currSum = 0;\n            for (int j = i;\
        \ j < n; j++) {\n                currSum += nums[j];\n                if ((sum\
        \ - currSum) % p == 0) res = Math.min(res, j - i + 1);\n            }\n    \
        \    }\n        return res == n ? -1 : res;\n    }\n}"
      python: "class Solution:\n    def minSubarray(self, nums: list[int], p: int) ->\
        \ int:\n        n = len(nums)\n        total_sum = sum(nums)\n        if total_sum\
        \ % p == 0: return 0\n        target = total_sum % p\n        curr_sum = 0\n\
        \        res = n\n        for i in range(n):\n            curr_sum = 0\n   \
        \         for j in range(i, n):\n                curr_sum += nums[j]\n     \
        \           if (total_sum - curr_sum) % p == 0: res = min(res, j - i + 1)\n\
        \        return res if res < n else -1"
      python3: "class Solution:\n    def minSubarray(self, nums: list[int], p: int)\
        \ -> int:\n        n = len(nums)\n        total_sum = sum(nums)\n        if\
        \ total_sum % p == 0: return 0\n        target = total_sum % p\n        curr_sum\
        \ = 0\n        res = n\n        for i in range(n):\n            curr_sum = 0\n\
        \            for j in range(i, n):\n                curr_sum += nums[j]\n  \
        \              if (total_sum - curr_sum) % p == 0: res = min(res, j - i + 1)\n\
        \        return res if res < n else -1"
      c: "typedef struct {\n    int* data;\n    int size;\n} Solution;\n\nint minSubarray(int*\
        \ nums, int numsSize, int p) {\n    int n = numsSize;\n    long long sum = 0;\n\
        \    for (int i = 0; i < n; i++) sum += nums[i];\n    if (sum % p == 0) return\
        \ 0;\n    long long target = sum % p;\n    long long currSum = 0;\n    int res\
        \ = n;\n    for (int i = 0; i < n; i++) {\n        currSum = 0;\n        for\
        \ (int j = i; j < n; j++) {\n            currSum += nums[j];\n            if\
        \ ((sum - currSum) % p == 0) res = (res < j - i + 1) ? res : j - i + 1;\n  \
        \      }\n    }\n    return res == n ? -1 : res;\n}"
      csharp: "public class Solution {\n    public int MinSubarray(int[] nums, int p)\
        \ {\n        int n = nums.Length;\n        long sum = 0;\n        foreach (int\
        \ num in nums) sum += num;\n        if (sum % p == 0) return 0;\n        long\
        \ target = sum % p;\n        long currSum = 0;\n        int res = n;\n     \
        \   for (int i = 0; i < n; i++) {\n            currSum = 0;\n            for\
        \ (int j = i; j < n; j++) {\n                currSum += nums[j];\n         \
        \       if ((sum - currSum) % p == 0) res = Math.Min(res, j - i + 1);\n    \
        \        }\n        }\n        return res == n ? -1 : res;\n    }\n}"
      javascript: "var minSubarray = function(nums, p) {\n    let n = nums.length;\n\
        \    let sum = 0;\n    for (let num of nums) sum += num;\n    if (sum % p ==\
        \ 0) return 0;\n    let target = sum % p;\n    let currSum = 0;\n    let res\
        \ = n;\n    for (let i = 0; i < n; i++) {\n        currSum = 0;\n        for\
        \ (let j = i; j < n; j++) {\n            currSum += nums[j];\n            if\
        \ ((sum - currSum) % p == 0) res = Math.min(res, j - i + 1);\n        }\n  \
        \  }\n    return res == n ? -1 : res;\n};"
      typescript: "function minSubarray(nums: number[], p: number): number {\n    let\
        \ n = nums.length;\n    let sum = 0;\n    for (let num of nums) sum += num;\n\
        \    if (sum % p == 0) return 0;\n    let target = sum % p;\n    let currSum\
        \ = 0;\n    let res = n;\n    for (let i = 0; i < n; i++) {\n        currSum\
        \ = 0;\n        for (let j = i; j < n; j++) {\n            currSum += nums[j];\n\
        \            if ((sum - currSum) % p == 0) res = Math.min(res, j - i + 1);\n\
        \        }\n    }\n    return res == n ? -1 : res;\n}"
      php: "class Solution {\n    function minSubarray($nums, $p) {\n        $n = count($nums);\n\
        \        $sum = 0;\n        foreach ($nums as $num) $sum += $num;\n        if\
        \ ($sum % $p == 0) return 0;\n        $target = $sum % $p;\n        $currSum\
        \ = 0;\n        $res = $n;\n        for ($i = 0; $i < $n; $i++) {\n        \
        \    $currSum = 0;\n            for ($j = $i; $j < $n; $j++) {\n           \
        \     $currSum += $nums[$j];\n                if (($sum - $currSum) % $p ==\
        \ 0) $res = min($res, $j - $i + 1);\n            }\n        }\n        return\
        \ $res == $n ? -1 : $res;\n    }\n}"
      swift: "class Solution {\n    func minSubarray(_ nums: [Int], _ p: Int) -> Int\
        \ {\n        let n = nums.count\n        var sum = 0\n        for num in nums\
        \ {\n            sum += num\n        }\n        if sum % p == 0 {\n        \
        \    return 0\n        }\n        let target = sum % p\n        var currSum\
        \ = 0\n        var res = n\n        for i in 0..<n {\n            currSum =\
        \ 0\n            for j in i..<n {\n                currSum += nums[j]\n    \
        \            if (sum - currSum) % p == 0 {\n                    res = min(res,\
        \ j - i + 1)\n                }\n            }\n        }\n        return res\
        \ == n ? -1 : res\n    }\n}"
      kotlin: "class Solution {\n    fun minSubarray(nums: IntArray, p: Int): Int {\n\
        \        val n = nums.size\n        var sum = 0\n        for (num in nums) sum\
        \ += num\n        if (sum % p == 0) return 0\n        val target = sum % p\n\
        \        var currSum = 0\n        var res = n\n        for (i in 0 until n)\
        \ {\n            currSum = 0\n            for (j in i until n) {\n         \
        \       currSum += nums[j]\n                if ((sum - currSum) % p == 0) res\
        \ = minOf(res, j - i + 1)\n            }\n        }\n        return if (res\
        \ == n) -1 else res\n    }\n}"
      dart: "class Solution {\n    int minSubarray(List<int> nums, int p) {\n      \
        \  int n = nums.length;\n        int sum = 0;\n        for (int num in nums)\
        \ sum += num;\n        if (sum % p == 0) return 0;\n        int target = sum\
        \ % p;\n        int currSum = 0;\n        int res = n;\n        for (int i =\
        \ 0; i < n; i++) {\n            currSum = 0;\n            for (int j = i; j\
        \ < n; j++) {\n                currSum += nums[j];\n                if ((sum\
        \ - currSum) % p == 0) res = res < j - i + 1 ? res : j - i + 1;\n          \
        \  }\n        }\n        return res == n ? -1 : res;\n    }\n}"
      go: "func minSubarray(nums []int, p int) int {\n    n := len(nums)\n    sum :=\
        \ 0\n    for _, num := range nums {\n        sum += num\n    }\n    if sum%p\
        \ == 0 {\n        return 0\n    }\n    target := sum % p\n    currSum := 0\n\
        \    res := n\n    for i := 0; i < n; i++ {\n        currSum = 0\n        for\
        \ j := i; j < n; j++ {\n            currSum += nums[j]\n            if (sum-currSum)%p\
        \ == 0 {\n                if res > j-i+1 {\n                    res = j - i\
        \ + 1\n                }\n            }\n        }\n    }\n    if res == n {\n\
        \        return -1\n    }\n    return res\n}"
      ruby: "class Solution\n    def min_subarray(nums, p)\n        n = nums.size\n\
        \        sum = 0\n        nums.each { |num| sum += num }\n        return 0 if\
        \ sum % p == 0\n        target = sum % p\n        curr_sum = 0\n        res\
        \ = n\n        (0...n).each do |i|\n            curr_sum = 0\n            (i...n).each\
        \ do |j|\n                curr_sum += nums[j]\n                if (sum - curr_sum)\
        \ % p == 0\n                    res = [res, j - i + 1].min\n               \
        \ end\n            end\n        end\n        res == n ? -1 : res\n    end\n\
        end"
      scala: "object Solution {\n    def minSubarray(nums: Array[Int], p: Int): Int\
        \ = {\n        val n = nums.length\n        var sum = 0\n        for (num <-\
        \ nums) sum += num\n        if (sum % p == 0) return 0\n        val target =\
        \ sum % p\n        var currSum = 0\n        var res = n\n        for (i <- 0\
        \ until n) {\n            currSum = 0\n            for (j <- i until n) {\n\
        \                currSum += nums(j)\n                if ((sum - currSum) % p\
        \ == 0) res = Math.min(res, j - i + 1)\n            }\n        }\n        if\
        \ (res == n) -1 else res\n    }\n}"
      rust: "struct Solution;\n\nimpl Solution {\n    pub fn min_subarray(nums: Vec<i32>,\
        \ p: i32) -> i32 {\n        let n = nums.len() as i32;\n        let mut sum:\
        \ i64 = 0;\n        for &num in nums.iter() {\n            sum += num as i64;\n\
        \        }\n        if sum % p as i64 == 0 {\n            return 0;\n      \
        \  }\n        let target = sum % p as i64;\n        let mut curr_sum = 0;\n\
        \        let mut res = n;\n        for i in 0..n {\n            curr_sum = 0;\n\
        \            for j in i..n {\n                curr_sum += nums[j as usize] as\
        \ i64;\n                if (sum - curr_sum) % p as i64 == 0 {\n            \
        \        res = res.min(j - i + 1);\n                }\n            }\n     \
        \   }\n        if res == n {\n            -1\n        } else {\n           \
        \ res\n        }\n    }\n}"
      racket: "define (min-subarray nums p)\n    (let* (\n        (n (length nums))\n\
        \        (sum (apply + nums))\n        (target (modulo sum p))\n        (curr-sum\
        \ 0)\n        (res n))\n        (if (zero? target)\n            0\n        \
        \    (begin\n                (for (\n                    (i (range n))\n   \
        \                 (j (range i n)))\n                    (set! curr-sum 0)\n\
        \                    (for (\n                        (k (range i (add1 j))))\n\
        \                        (set! curr-sum (+ curr-sum (list-ref nums k))))\n \
        \                   (when (zero? (modulo (- sum curr-sum) p))\n            \
        \            (set! res (min res (- j i 1))))))\n                (if (= res n)\n\
        \                    -1\n                    res))))"
      erlang: "min_subarray(Nums, P) ->\n    N = length(Nums),\n    Sum = lists:sum(Nums),\n\
        \    case Sum rem P of\n        0 -> 0;\n        _ ->\n            Target =\
        \ Sum rem P,\n            CurrSum = 0,\n            Res = N,\n            lists:foldl(\n\
        \                fun(I, {Res, CurrSum}) ->\n                    CurrSum1 = 0,\n\
        \                    lists:foldl(\n                        fun(J, {Res, CurrSum})\
        \ ->\n                            CurrSum1 = CurrSum + lists:nth(J + 1, Nums),\n\
        \                            case (Sum - CurrSum1) rem P of\n              \
        \                  0 -> {min(Res, J - I + 1), CurrSum1};\n                 \
        \               _ -> {Res, CurrSum1}\n                            end\n    \
        \                    end,\n                        {Res, CurrSum},\n       \
        \                 lists:seq(I, N - 1))\n                end,\n             \
        \   {Res, CurrSum},\n                lists:seq(0, N - 1)),\n            case\
        \ Res of\n                N -> -1;\n                _ -> Res\n            end\n\
        \    end."
      elixir: "def min_subarray(nums, p) do\n    n = length(nums)\n    sum = Enum.sum(nums)\n\
        \    cond do\n        rem(sum, p) == 0 -> 0\n        true ->\n            target\
        \ = rem(sum, p)\n            curr_sum = 0\n            res = n\n           \
        \ Enum.reduce(0..n-1, {res, curr_sum}, fn i, {res, curr_sum} ->\n          \
        \      curr_sum = 0\n                Enum.reduce(i..n-1, {res, curr_sum}, fn\
        \ j, {res, curr_sum} ->\n                    curr_sum = curr_sum + Enum.at(nums,\
        \ j)\n                    if rem(sum - curr_sum, p) == 0 do\n              \
        \          {min(res, j - i + 1), curr_sum}\n                    else\n     \
        \                   {res, curr_sum}\n                    end\n             \
        \   end)\n            end)\n            |> (fn {res, _} -> if res == n, do:\
        \ -1, else: res end)\n    end\nend"
    approach: The problem can be solved by using prefix sums to calculate the subarray
      sums. We first calculate the total sum of the array and its remainder when divided
      by p. If the remainder is 0, we can return 0 as no subarray needs to be removed.
      Otherwise, we iterate over all possible subarrays, calculate their sums, and check
      if removing them would make the remaining sum divisible by p. We keep track of
      the smallest subarray that satisfies this condition. Another approach is to use
      a map to keep track of the rightmost index for every prefix sum % p. This allows
      us to efficiently find the smallest subarray that needs to be removed to make
      the remaining sum divisible by p.
    time_complexity: The time complexity of the solution is O(n^2) where n is the number
      of elements in the array. This is because we are iterating over all possible subarrays
      in the worst case. However, using a map to keep track of the rightmost index for
      every prefix sum % p can reduce the time complexity to O(n).
    space_complexity: The space complexity of the solution is O(n) where n is the number
      of elements in the array. This is because we need to store the prefix sums and
      the map of rightmost indices for every prefix sum % p.
    elapsed_time: 8.393427848815918
    model: llama-3.3-70b-versatile
    generated_at: '2025-11-30 01:12:57 '
---

## Problem #1590: Make Sum Divisible by P

**Difficulty:** Medium

**Topics:** Array, Hash Table, Prefix Sum

## Problem Description

<p>Given an array of positive integers <code>nums</code>, remove the <strong>smallest</strong> subarray (possibly <strong>empty</strong>) such that the <strong>sum</strong> of the remaining elements is divisible by <code>p</code>. It is <strong>not</strong> allowed to remove the whole array.</p>

<p>Return <em>the length of the smallest subarray that you need to remove, or </em><code>-1</code><em> if it&#39;s impossible</em>.</p>

<p>A <strong>subarray</strong> is defined as a contiguous block of elements in the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,1,4,2], p = 6
<strong>Output:</strong> 1
<strong>Explanation:</strong> The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [6,3,5,2], p = 9
<strong>Output:</strong> 2
<strong>Explanation:</strong> We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3], p = 3
<strong>Output:</strong> 0
<strong>Explanation:</strong> Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= p &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. Use prefix sums to calculate the subarray sums.

2. Suppose you know the remainder for the sum of the entire array. How does removing a subarray affect that remainder? What remainder does the subarray need to have in order to make the rest of the array sum up to be divisible by k?

3. Use a map to keep track of the rightmost index for every prefix sum % p.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-30 01:12:49 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to find the smallest subarray to remove such that the sum of the remaining elements is divisible by `p`. Let `S` be the total sum of all elements in `nums`. If we remove a subarray with sum `S_sub`, the sum of the remaining elements is `S - S_sub`. We want `(S - S_sub) % p == 0`, which implies `S % p == S_sub % p`. Let `target_rem = S % p`. If `target_rem` is 0, the total sum is already divisible by `p`, so we don't need to remove anything, and the answer is 0. Otherwise, we need to find a subarray `nums[k...i]` whose sum `S_sub` satisfies `S_sub % p == target_rem`, and we want this subarray to be as short as possible. We are not allowed to remove the entire array.

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
    int minSubarray(std::vector<int>& nums, int p) {
        long long total_sum = 0;
        for (int num : nums) {
            total_sum += num;
        }

        int target_rem = total_sum % p;

        if (target_rem == 0) {
            return 0;
        }

        std::unordered_map<int, int> prefix_rem_map;
        prefix_rem_map[0] = -1; // Represents prefix sum 0 before index 0

        long long current_prefix_sum = 0;
        int min_len = nums.size();

        for (int i = 0; i < nums.size(); ++i) {
            current_prefix_sum = (current_prefix_sum + nums[i]) % p;

            // We need (current_prefix_sum - prev_prefix_sum_rem + p) % p == target_rem
            // So, prev_prefix_sum_rem = (current_prefix_sum - target_rem + p) % p
            int required_prev_rem = (current_prefix_sum - target_rem + p) % p;

            if (prefix_rem_map.count(required_prev_rem)) {
                min_len = std::min(min_len, i - prefix_rem_map[required_prev_rem]);
            }
            prefix_rem_map[current_prefix_sum] = i;
        }

        return min_len == nums.size() ? -1 : min_len;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int minSubarray(int[] nums, int p) {
        long totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }

        int targetRem = (int) (totalSum % p);

        if (targetRem == 0) {
            return 0;
        }

        Map<Integer, Integer> prefixRemMap = new HashMap<>();
        prefixRemMap.put(0, -1); // Represents prefix sum 0 before index 0

        long currentPrefixSum = 0;
        int minLen = nums.length;

        for (int i = 0; i < nums.length; ++i) {
            currentPrefixSum = (currentPrefixSum + nums[i]) % p;

            // We need (currentPrefixSum - prevPrefixSumRem + p) % p == targetRem
            // So, prevPrefixSumRem = (currentPrefixSum - targetRem + p) % p
            int requiredPrevRem = (int) ((currentPrefixSum - targetRem + p) % p);

            if (prefixRemMap.containsKey(requiredPrevRem)) {
                minLen = Math.min(minLen, i - prefixRemMap.get(requiredPrevRem));
            }
            prefixRemMap.put((int) currentPrefixSum, i);
        }

        return minLen == nums.length ? -1 : minLen;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        total_sum = sum(nums)
        target_rem = total_sum % p

        if target_rem == 0:
            return 0

        prefix_rem_map = {0: -1} # Represents prefix sum 0 before index 0
        current_prefix_sum = 0
        min_len = len(nums)

        for i, num in enumerate(nums):
            current_prefix_sum = (current_prefix_sum + num) % p

            # We need (current_prefix_sum - prev_prefix_sum_rem + p) % p == target_rem
            # So, prev_prefix_sum_rem = (current_prefix_sum - target_rem + p) % p
            required_prev_rem = (current_prefix_sum - target_rem + p) % p

            if required_prev_rem in prefix_rem_map:
                min_len = min(min_len, i - prefix_rem_map[required_prev_rem])

            prefix_rem_map[current_prefix_sum] = i

        return min_len if min_len != len(nums) else -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        total_sum = sum(nums)
        target_rem = total_sum % p

        if target_rem == 0:
            return 0

        prefix_rem_map = {0: -1} # Represents prefix sum 0 before index 0
        current_prefix_sum = 0
        min_len = len(nums)

        for i, num in enumerate(nums):
            current_prefix_sum = (current_prefix_sum + num) % p

            # We need (current_prefix_sum - prev_prefix_sum_rem + p) % p == target_rem
            # So, prev_prefix_sum_rem = (current_prefix_sum - target_rem + p) % p
            required_prev_rem = (current_prefix_sum - target_rem + p) % p

            if required_prev_rem in prefix_rem_map:
                min_len = min(min_len, i - prefix_rem_map[required_prev_rem])

            prefix_rem_map[current_prefix_sum] = i

        return min_len if min_len != len(nums) else -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

// Basic hash table implementation for (remainder, index) pairs
// Using open addressing with linear probing

typedef struct {
    int key; // remainder
    int value; // index
    int occupied; // 0: empty, 1: occupied
} Entry;

typedef struct {
    Entry* table;
    int capacity;
    int size;
} HashTable;

// A simple hash function
unsigned int hash(int key, int capacity) {
    return (unsigned int)key % capacity;
}

// Initialize hash table
HashTable* createHashTable(int capacity) {
    HashTable* ht = (HashTable*)malloc(sizeof(HashTable));
    ht->capacity = capacity;
    ht->size = 0;
    ht->table = (Entry*)calloc(capacity, sizeof(Entry));
    return ht;
}

// Insert or update an entry
void ht_put(HashTable* ht, int key, int value) {
    unsigned int index = hash(key, ht->capacity);
    while (ht->table[index].occupied) {
        if (ht->table[index].key == key) {
            ht->table[index].value = value; // Update value
            return;
        }
        index = (index + 1) % ht->capacity;
    }
    // Found an empty slot or key not found
    ht->table[index].key = key;
    ht->table[index].value = value;
    ht->table[index].occupied = 1;
    ht->size++;
}

// Get an entry
int ht_get(HashTable* ht, int key, int* value) {
    unsigned int index = hash(key, ht->capacity);
    while (ht->table[index].occupied) {
        if (ht->table[index].key == key) {
            *value = ht->table[index].value;
            return 1; // Found
        }
        index = (index + 1) % ht->capacity;
    }
    return 0; // Not found
}

// Free hash table
void freeHashTable(HashTable* ht) {
    free(ht->table);
    free(ht);
}

int min(int a, int b) {
    return a < b ? a : b;
}

int minSubarray(int* nums, int numsSize, int p) {
    long long total_sum = 0;
    for (int i = 0; i < numsSize; ++i) {
        total_sum += nums[i];
    }

    int target_rem = total_sum % p;

    if (target_rem == 0) {
        return 0;
    }

    // Hash table capacity should be a prime number larger than numsSize
    // For simplicity, using numsSize * 2. A more robust solution might use a prime number.
    HashTable* prefix_rem_map = createHashTable(numsSize * 2 + 1); 
    ht_put(prefix_rem_map, 0, -1); // Represents prefix sum 0 before index 0

    long long current_prefix_sum = 0;
    int min_len = numsSize;

    for (int i = 0; i < numsSize; ++i) {
        current_prefix_sum = (current_prefix_sum + nums[i]) % p;

        // We need (current_prefix_sum - prev_prefix_sum_rem + p) % p == target_rem
        // So, prev_prefix_sum_rem = (current_prefix_sum - target_rem + p) % p
        int required_prev_rem = (current_prefix_sum - target_rem + p) % p;

        int prev_idx;
        if (ht_get(prefix_rem_map, required_prev_rem, &prev_idx)) {
            min_len = min(min_len, i - prev_idx);
        }
        ht_put(prefix_rem_map, current_prefix_sum, i);
    }

    freeHashTable(prefix_rem_map);

    return min_len == numsSize ? -1 : min_len;
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
    public int MinSubarray(int[] nums, int p) {
        long totalSum = 0;
        foreach (int num in nums) {
            totalSum += num;
        }

        int targetRem = (int)(totalSum % p);

        if (targetRem == 0) {
            return 0;
        }

        Dictionary<int, int> prefixRemMap = new Dictionary<int, int>();
        prefixRemMap[0] = -1; // Represents prefix sum 0 before index 0

        long currentPrefixSum = 0;
        int minLen = nums.Length;

        for (int i = 0; i < nums.Length; ++i) {
            currentPrefixSum = (currentPrefixSum + nums[i]) % p;

            // We need (currentPrefixSum - prevPrefixSumRem + p) % p == targetRem
            // So, prevPrefixSumRem = (currentPrefixSum - targetRem + p) % p
            int requiredPrevRem = (int)((currentPrefixSum - targetRem + p) % p);

            if (prefixRemMap.ContainsKey(requiredPrevRem)) {
                minLen = Math.Min(minLen, i - prefixRemMap[requiredPrevRem]);
            }
            prefixRemMap[(int)currentPrefixSum] = i;
        }

        return minLen == nums.Length ? -1 : minLen;
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
 * @param {number} p
 * @return {number}
 */
var minSubarray = function(nums, p) {
    let totalSum = 0n; // Use BigInt for total sum
    for (let num of nums) {
        totalSum += BigInt(num);
    }

    const P_BIGINT = BigInt(p);
    let targetRem = totalSum % P_BIGINT;

    if (targetRem === 0n) {
        return 0;
    }

    const prefixRemMap = new Map();
    prefixRemMap.set(0, -1); // Represents prefix sum 0 before index 0

    let currentPrefixSum = 0n; // Use BigInt for current prefix sum
    let minLen = nums.length;

    for (let i = 0; i < nums.length; ++i) {
        currentPrefixSum = (currentPrefixSum + BigInt(nums[i])) % P_BIGINT;

        // We need (currentPrefixSum - prevPrefixSumRem + P_BIGINT) % P_BIGINT == targetRem
        // So, prevPrefixSumRem = (currentPrefixSum - targetRem + P_BIGINT) % P_BIGINT
        let requiredPrevRem = (currentPrefixSum - targetRem + P_BIGINT) % P_BIGINT;

        // Convert BigInt remainder back to number for map key
        if (prefixRemMap.has(Number(requiredPrevRem))) {
            minLen = Math.min(minLen, i - prefixRemMap.get(Number(requiredPrevRem)));
        }
        prefixRemMap.set(Number(currentPrefixSum), i);
    }

    return minLen === nums.length ? -1 : minLen;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minSubarray(nums: number[], p: number): number {
    let totalSum: bigint = 0n; // Use BigInt for total sum
    for (let num of nums) {
        totalSum += BigInt(num);
    }

    const P_BIGINT: bigint = BigInt(p);
    let targetRem: bigint = totalSum % P_BIGINT;

    if (targetRem === 0n) {
        return 0;
    }

    const prefixRemMap: Map<number, number> = new Map();
    prefixRemMap.set(0, -1); // Represents prefix sum 0 before index 0

    let currentPrefixSum: bigint = 0n; // Use BigInt for current prefix sum
    let minLen: number = nums.length;

    for (let i = 0; i < nums.length; ++i) {
        currentPrefixSum = (currentPrefixSum + BigInt(nums[i])) % P_BIGINT;

        // We need (currentPrefixSum - prevPrefixSumRem + P_BIGINT) % P_BIGINT == targetRem
        // So, prevPrefixSumRem = (currentPrefixSum - targetRem + P_BIGINT) % P_BIGINT
        let requiredPrevRem: bigint = (currentPrefixSum - targetRem + P_BIGINT) % P_BIGINT;

        // Convert BigInt remainder back to number for map key
        if (prefixRemMap.has(Number(requiredPrevRem))) {
            minLen = Math.min(minLen, i - prefixRemMap.get(Number(requiredPrevRem))!);
        }
        prefixRemMap.set(Number(currentPrefixSum), i);
    }

    return minLen === nums.length ? -1 : minLen;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php
class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $p
     * @return Integer
     */
    function minSubarray($nums, $p) {
        $totalSum = 0;
        foreach ($nums as $num) {
            $totalSum += $num;
        }

        $targetRem = $totalSum % $p;

        if ($targetRem == 0) {
            return 0;
        }

        $prefixRemMap = [0 => -1]; // Represents prefix sum 0 before index 0

        $currentPrefixSum = 0;
        $minLen = count($nums);

        for ($i = 0; $i < count($nums); ++$i) {
            $currentPrefixSum = ($currentPrefixSum + $nums[$i]) % $p;

            // We need (currentPrefixSum - prevPrefixSumRem + p) % p == targetRem
            // So, prevPrefixSumRem = (currentPrefixSum - targetRem + p) % p
            $requiredPrevRem = ($currentPrefixSum - $targetRem + $p) % $p;

            if (array_key_exists($requiredPrevRem, $prefixRemMap)) {
                $minLen = min($minLen, $i - $prefixRemMap[$requiredPrevRem]);
            }
            $prefixRemMap[$currentPrefixSum] = $i;
        }

        return $minLen == count($nums) ? -1 : $minLen;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minSubarray(_ nums: [Int], _ p: Int) -> Int {
        var totalSum: Int = 0
        for num in nums {
            totalSum += num
        }

        let targetRem: Int = totalSum % p

        if targetRem == 0 {
            return 0
        }

        var prefixRemMap: [Int: Int] = [0: -1] // Represents prefix sum 0 before index 0

        var currentPrefixSum: Int = 0
        var minLen: Int = nums.count

        for i in 0..<nums.count {
            currentPrefixSum = (currentPrefixSum + nums[i]) % p

            // We need (currentPrefixSum - prevPrefixSumRem + p) % p == targetRem
            // So, prevPrefixSumRem = (currentPrefixSum - targetRem + p) % p
            let requiredPrevRem: Int = (currentPrefixSum - targetRem + p) % p

            if let prevIdx = prefixRemMap[requiredPrevRem] {
                minLen = min(minLen, i - prevIdx)
            }
            prefixRemMap[currentPrefixSum] = i
        }

        return minLen == nums.count ? -1 : minLen
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minSubarray(nums: IntArray, p: Int): Int {
        var totalSum: Long = 0
        for (num in nums) {
            totalSum += num
        }

        val targetRem: Int = (totalSum % p).toInt()

        if (targetRem == 0) {
            return 0
        }

        val prefixRemMap: MutableMap<Int, Int> = mutableMapOf()
        prefixRemMap[0] = -1 // Represents prefix sum 0 before index 0

        var currentPrefixSum: Long = 0
        var minLen: Int = nums.size

        for (i in nums.indices) {
            currentPrefixSum = (currentPrefixSum + nums[i]) % p

            // We need (currentPrefixSum - prevPrefixSumRem + p) % p == targetRem
            // So, prevPrefixSumRem = (currentPrefixSum - targetRem + p) % p
            val requiredPrevRem: Int = ((currentPrefixSum - targetRem + p) % p).toInt()

            if (prefixRemMap.containsKey(requiredPrevRem)) {
                minLen = minOf(minLen, i - prefixRemMap[requiredPrevRem]!!)
            }
            prefixRemMap[currentPrefixSum.toInt()] = i
        }

        return if (minLen == nums.size) -1 else minLen
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
  int minSubarray(List<int> nums, int p) {
    BigInt totalSum = BigInt.zero;
    for (int num in nums) {
      totalSum += BigInt.from(num);
    }

    BigInt pBigInt = BigInt.from(p);
    BigInt targetRem = totalSum % pBigInt;

    if (targetRem == BigInt.zero) {
      return 0;
    }

    Map<int, int> prefixRemMap = {0: -1}; // Represents prefix sum 0 before index 0

    BigInt currentPrefixSum = BigInt.zero;
    int minLen = nums.length;

    for (int i = 0; i < nums.length; ++i) {
      currentPrefixSum = (currentPrefixSum + BigInt.from(nums[i])) % pBigInt;

      // We need (currentPrefixSum - prevPrefixSumRem + pBigInt) % pBigInt == targetRem
      // So, prevPrefixSumRem = (currentPrefixSum - targetRem + pBigInt) % pBigInt
      BigInt requiredPrevRemBigInt = (currentPrefixSum - targetRem + pBigInt) % pBigInt;
      int requiredPrevRem = requiredPrevRemBigInt.toInt();

      if (prefixRemMap.containsKey(requiredPrevRem)) {
        minLen = min(minLen, i - prefixRemMap[requiredPrevRem]!);
      }
      prefixRemMap[currentPrefixSum.toInt()] = i;
    }

    return minLen == nums.length ? -1 : minLen;
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

func minSubarray(nums []int, p int) int {
    var totalSum int64 = 0
    for _, num := range nums {
        totalSum += int64(num)
    }

    targetRem := int(totalSum % int64(p))

    if targetRem == 0 {
        return 0
    }

    prefixRemMap := make(map[int]int)
    prefixRemMap[0] = -1 // Represents prefix sum 0 before index 0

    var currentPrefixSum int64 = 0
    minLen := len(nums)

    for i := 0; i < len(nums); i++ {
        currentPrefixSum = (currentPrefixSum + int64(nums[i])) % int64(p)

        // We need (currentPrefixSum - prevPrefixSumRem + p) % p == targetRem
        // So, prevPrefixSumRem = (currentPrefixSum - targetRem + p) % p
        requiredPrevRem := int((currentPrefixSum - int64(targetRem) + int64(p)) % int64(p))

        if prevIdx, ok := prefixRemMap[requiredPrevRem]; ok {
            minLen = int(math.Min(float64(minLen), float64(i - prevIdx)))
        }
        prefixRemMap[int(currentPrefixSum)] = i
    }

    if minLen == len(nums) {
        return -1
    }
    return minLen
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    def min_subarray(nums, p)
        total_sum = nums.sum
        target_rem = total_sum % p

        return 0 if target_rem == 0

        prefix_rem_map = {0 => -1} # Represents prefix sum 0 before index 0
        current_prefix_sum = 0
        min_len = nums.length

        nums.each_with_index do |num, i|
            current_prefix_sum = (current_prefix_sum + num) % p

            # We need (current_prefix_sum - prev_prefix_sum_rem + p) % p == target_rem
            # So, prev_prefix_sum_rem = (current_prefix_sum - target_rem + p) % p
            required_prev_rem = (current_prefix_sum - target_rem + p) % p

            if prefix_rem_map.key?(required_prev_rem)
                min_len = [min_len, i - prefix_rem_map[required_prev_rem]].min
            end
            prefix_rem_map[current_prefix_sum] = i
        end

        min_len == nums.length ? -1 : min_len
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

object Solution {
    def minSubarray(nums: Array[Int], p: Int): Int = {
        var totalSum: Long = nums.map(_.toLong).sum
        val targetRem: Int = (totalSum % p).toInt

        if (targetRem == 0) {
            return 0
        }

        val prefixRemMap: mutable.HashMap[Int, Int] = mutable.HashMap(0 -> -1) // Represents prefix sum 0 before index 0

        var currentPrefixSum: Long = 0
        var minLen: Int = nums.length

        for (i <- nums.indices) {
            currentPrefixSum = (currentPrefixSum + nums(i)) % p

            // We need (currentPrefixSum - prevPrefixSumRem + p) % p == targetRem
            // So, prevPrefixSumRem = (currentPrefixSum - targetRem + p) % p
            val requiredPrevRem: Int = ((currentPrefixSum - targetRem + p) % p).toInt

            if (prefixRemMap.contains(requiredPrevRem)) {
                minLen = math.min(minLen, i - prefixRemMap(requiredPrevRem))
            }
            prefixRemMap(currentPrefixSum.toInt) = i
        }

        if (minLen == nums.length) -1 else minLen
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::HashMap;
use std::cmp::min;

impl Solution {
    pub fn min_subarray(nums: Vec<i32>, p: i32) -> i32 {
        let mut total_sum: i64 = 0;
        for &num in &nums {
            total_sum += num as i64;
        }

        let target_rem: i32 = (total_sum % p as i64) as i32;

        if target_rem == 0 {
            return 0;
        }

        let mut prefix_rem_map: HashMap<i32, i32> = HashMap::new();
        prefix_rem_map.insert(0, -1); // Represents prefix sum 0 before index 0

        let mut current_prefix_sum: i64 = 0;
        let mut min_len: i32 = nums.len() as i32;

        for i in 0..nums.len() {
            current_prefix_sum = (current_prefix_sum + nums[i] as i64) % p as i64;

            // We need (current_prefix_sum - prev_prefix_sum_rem + p) % p == target_rem
            // So, prev_prefix_sum_rem = (current_prefix_sum - target_rem + p) % p
            let required_prev_rem: i32 = ((current_prefix_sum - target_rem as i64 + p as i64) % p as i64) as i32;

            if let Some(&prev_idx) = prefix_rem_map.get(&required_prev_rem) {
                min_len = min(min_len, i as i32 - prev_idx);
            }
            prefix_rem_map.insert(current_prefix_sum as i32, i as i32);
        }

        if min_len == nums.len() as i32 {
            -1
        } else {
            min_len
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (min-subarray nums p)
  (define total-sum (apply + nums))
  (define target-rem (modulo total-sum p))

  (when (= target-rem 0)
    (hash-clear! (make-hash))
    (void))

  (if (= target-rem 0)
      0
      (let* ((prefix-rem-map (make-hash))
             (n (length nums))
             (min-len n))
        (hash-set! prefix-rem-map 0 -1)
        (define current-prefix-sum 0)

        (for ([num (in-list nums)]
              [i (in-range n)])
          (set! current-prefix-sum (modulo (+ current-prefix-sum num) p))

          (define required-prev-rem (modulo (- (+ current-prefix-sum p) target-rem) p))

          (when (hash-has-key? prefix-rem-map required-prev-rem)
            (set! min-len (min min-len (- i (hash-ref prefix-rem-map required-prev-rem)))))

          (hash-set! prefix-rem-map current-prefix-sum i))

        (if (= min-len n) -1 min-len))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([min_subarray/2]).

min_subarray(Nums, P) ->
TotalSum = lists:sum(Nums),
TargetRem = TotalSum rem P,

if TargetRem == 0 ->
0;
true ->
PrefixRemMap = maps:put(0, -1, #{}),
CurrentPrefixSum = 0,
MinLen = length(Nums),

min_subarray_loop(Nums, P, TargetRem, PrefixRemMap, CurrentPrefixSum, MinLen, 0)
end.

min_subarray_loop([], _P, _TargetRem, _PrefixRemMap, _CurrentPrefixSum, MinLen, N) ->
if MinLen == N -> -1; true -> MinLen end;
min_subarray_loop([Num | Rest], P, TargetRem, PrefixRemMap, CurrentPrefixSum, MinLen, I) ->
NewCurrentPrefixSum = (CurrentPrefixSum + Num) rem P,

RequiredPrevRem = (NewCurrentPrefixSum - TargetRem + P) rem P,

NewMinLen = 
case maps:find(RequiredPrevRem, PrefixRemMap) of
    {ok, PrevIdx} -> min(MinLen, I - PrevIdx);
    _ -> MinLen
end,

NewPrefixRemMap = maps:put(NewCurrentPrefixSum, I, PrefixRemMap),

min_subarray_loop(Rest, P, TargetRem, NewPrefixRemMap, NewCurrentPrefixSum, NewMinLen, I + 1).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_subarray(nums :: [integer], p :: integer) :: integer
  def min_subarray(nums, p) do
    total_sum = Enum.sum(nums)
    target_rem = rem(total_sum, p)

    if target_rem == 0 do
      0
    else
      prefix_rem_map = %{0 => -1}
      current_prefix_sum = 0
      min_len = length(nums)

      {_final_prefix_rem_map, final_min_len} = Enum.reduce(0..(length(nums) - 1), {prefix_rem_map, min_len, current_prefix_sum}, fn i, {acc_map, acc_min_len, acc_current_prefix_sum} ->
        num = Enum.at(nums, i)
        new_current_prefix_sum = rem(acc_current_prefix_sum + num, p)

        required_prev_rem = rem(new_current_prefix_sum - target_rem + p, p)

        new_min_len = 
          case Map.fetch(acc_map, required_prev_rem) do
            {:ok, prev_idx} -> min(acc_min_len, i - prev_idx)
            :error -> acc_min_len
          end

        new_acc_map = Map.put(acc_map, new_current_prefix_sum, i)
        {new_acc_map, new_min_len, new_current_prefix_sum}
      end)

      if final_min_len == length(nums) do
        -1
      else
        final_min_len
      end
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N), where N is the length of the `nums` array. We iterate through the array once to calculate the total sum and once more to compute prefix sums and update the hash map. Each hash map operation (insertion and lookup) takes O(1) on average.

- **Space Complexity:** The space complexity is O(N) in the worst case. The hash map stores at most N distinct prefix sum remainders along with their indices. In the worst case, all N prefix sum remainders modulo `p` could be unique, requiring N entries in the map.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-30 01:12:57 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by using prefix sums to calculate the subarray sums. We first calculate the total sum of the array and its remainder when divided by p. If the remainder is 0, we can return 0 as no subarray needs to be removed. Otherwise, we iterate over all possible subarrays, calculate their sums, and check if removing them would make the remaining sum divisible by p. We keep track of the smallest subarray that satisfies this condition. Another approach is to use a map to keep track of the rightmost index for every prefix sum % p. This allows us to efficiently find the smallest subarray that needs to be removed to make the remaining sum divisible by p.

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
    int minSubarray(vector<int>& nums, int p) {
        int n = nums.size();
        long long sum = 0;
        for (int num : nums) sum += num;
        if (sum % p == 0) return 0;
        long long target = sum % p;
        long long currSum = 0;
        int res = n;
        for (int i = 0; i < n; i++) {
            currSum = 0;
            for (int j = i; j < n; j++) {
                currSum += nums[j];
                if ((sum - currSum) % p == 0) res = min(res, j - i + 1);
            }
        }
        return res == n ? -1 : res;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minSubarray(int[] nums, int p) {
        int n = nums.length;
        long sum = 0;
        for (int num : nums) sum += num;
        if (sum % p == 0) return 0;
        long target = sum % p;
        long currSum = 0;
        int res = n;
        for (int i = 0; i < n; i++) {
            currSum = 0;
            for (int j = i; j < n; j++) {
                currSum += nums[j];
                if ((sum - currSum) % p == 0) res = Math.min(res, j - i + 1);
            }
        }
        return res == n ? -1 : res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        n = len(nums)
        total_sum = sum(nums)
        if total_sum % p == 0: return 0
        target = total_sum % p
        curr_sum = 0
        res = n
        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                if (total_sum - curr_sum) % p == 0: res = min(res, j - i + 1)
        return res if res < n else -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        n = len(nums)
        total_sum = sum(nums)
        if total_sum % p == 0: return 0
        target = total_sum % p
        curr_sum = 0
        res = n
        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                if (total_sum - curr_sum) % p == 0: res = min(res, j - i + 1)
        return res if res < n else -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
typedef struct {
    int* data;
    int size;
} Solution;

int minSubarray(int* nums, int numsSize, int p) {
    int n = numsSize;
    long long sum = 0;
    for (int i = 0; i < n; i++) sum += nums[i];
    if (sum % p == 0) return 0;
    long long target = sum % p;
    long long currSum = 0;
    int res = n;
    for (int i = 0; i < n; i++) {
        currSum = 0;
        for (int j = i; j < n; j++) {
            currSum += nums[j];
            if ((sum - currSum) % p == 0) res = (res < j - i + 1) ? res : j - i + 1;
        }
    }
    return res == n ? -1 : res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinSubarray(int[] nums, int p) {
        int n = nums.Length;
        long sum = 0;
        foreach (int num in nums) sum += num;
        if (sum % p == 0) return 0;
        long target = sum % p;
        long currSum = 0;
        int res = n;
        for (int i = 0; i < n; i++) {
            currSum = 0;
            for (int j = i; j < n; j++) {
                currSum += nums[j];
                if ((sum - currSum) % p == 0) res = Math.Min(res, j - i + 1);
            }
        }
        return res == n ? -1 : res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var minSubarray = function(nums, p) {
    let n = nums.length;
    let sum = 0;
    for (let num of nums) sum += num;
    if (sum % p == 0) return 0;
    let target = sum % p;
    let currSum = 0;
    let res = n;
    for (let i = 0; i < n; i++) {
        currSum = 0;
        for (let j = i; j < n; j++) {
            currSum += nums[j];
            if ((sum - currSum) % p == 0) res = Math.min(res, j - i + 1);
        }
    }
    return res == n ? -1 : res;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minSubarray(nums: number[], p: number): number {
    let n = nums.length;
    let sum = 0;
    for (let num of nums) sum += num;
    if (sum % p == 0) return 0;
    let target = sum % p;
    let currSum = 0;
    let res = n;
    for (let i = 0; i < n; i++) {
        currSum = 0;
        for (let j = i; j < n; j++) {
            currSum += nums[j];
            if ((sum - currSum) % p == 0) res = Math.min(res, j - i + 1);
        }
    }
    return res == n ? -1 : res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function minSubarray($nums, $p) {
        $n = count($nums);
        $sum = 0;
        foreach ($nums as $num) $sum += $num;
        if ($sum % $p == 0) return 0;
        $target = $sum % $p;
        $currSum = 0;
        $res = $n;
        for ($i = 0; $i < $n; $i++) {
            $currSum = 0;
            for ($j = $i; $j < $n; $j++) {
                $currSum += $nums[$j];
                if (($sum - $currSum) % $p == 0) $res = min($res, $j - $i + 1);
            }
        }
        return $res == $n ? -1 : $res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minSubarray(_ nums: [Int], _ p: Int) -> Int {
        let n = nums.count
        var sum = 0
        for num in nums {
            sum += num
        }
        if sum % p == 0 {
            return 0
        }
        let target = sum % p
        var currSum = 0
        var res = n
        for i in 0..<n {
            currSum = 0
            for j in i..<n {
                currSum += nums[j]
                if (sum - currSum) % p == 0 {
                    res = min(res, j - i + 1)
                }
            }
        }
        return res == n ? -1 : res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minSubarray(nums: IntArray, p: Int): Int {
        val n = nums.size
        var sum = 0
        for (num in nums) sum += num
        if (sum % p == 0) return 0
        val target = sum % p
        var currSum = 0
        var res = n
        for (i in 0 until n) {
            currSum = 0
            for (j in i until n) {
                currSum += nums[j]
                if ((sum - currSum) % p == 0) res = minOf(res, j - i + 1)
            }
        }
        return if (res == n) -1 else res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int minSubarray(List<int> nums, int p) {
        int n = nums.length;
        int sum = 0;
        for (int num in nums) sum += num;
        if (sum % p == 0) return 0;
        int target = sum % p;
        int currSum = 0;
        int res = n;
        for (int i = 0; i < n; i++) {
            currSum = 0;
            for (int j = i; j < n; j++) {
                currSum += nums[j];
                if ((sum - currSum) % p == 0) res = res < j - i + 1 ? res : j - i + 1;
            }
        }
        return res == n ? -1 : res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minSubarray(nums []int, p int) int {
    n := len(nums)
    sum := 0
    for _, num := range nums {
        sum += num
    }
    if sum%p == 0 {
        return 0
    }
    target := sum % p
    currSum := 0
    res := n
    for i := 0; i < n; i++ {
        currSum = 0
        for j := i; j < n; j++ {
            currSum += nums[j]
            if (sum-currSum)%p == 0 {
                if res > j-i+1 {
                    res = j - i + 1
                }
            }
        }
    }
    if res == n {
        return -1
    }
    return res
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    def min_subarray(nums, p)
        n = nums.size
        sum = 0
        nums.each { |num| sum += num }
        return 0 if sum % p == 0
        target = sum % p
        curr_sum = 0
        res = n
        (0...n).each do |i|
            curr_sum = 0
            (i...n).each do |j|
                curr_sum += nums[j]
                if (sum - curr_sum) % p == 0
                    res = [res, j - i + 1].min
                end
            end
        end
        res == n ? -1 : res
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minSubarray(nums: Array[Int], p: Int): Int = {
        val n = nums.length
        var sum = 0
        for (num <- nums) sum += num
        if (sum % p == 0) return 0
        val target = sum % p
        var currSum = 0
        var res = n
        for (i <- 0 until n) {
            currSum = 0
            for (j <- i until n) {
                currSum += nums(j)
                if ((sum - currSum) % p == 0) res = Math.min(res, j - i + 1)
            }
        }
        if (res == n) -1 else res
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
    pub fn min_subarray(nums: Vec<i32>, p: i32) -> i32 {
        let n = nums.len() as i32;
        let mut sum: i64 = 0;
        for &num in nums.iter() {
            sum += num as i64;
        }
        if sum % p as i64 == 0 {
            return 0;
        }
        let target = sum % p as i64;
        let mut curr_sum = 0;
        let mut res = n;
        for i in 0..n {
            curr_sum = 0;
            for j in i..n {
                curr_sum += nums[j as usize] as i64;
                if (sum - curr_sum) % p as i64 == 0 {
                    res = res.min(j - i + 1);
                }
            }
        }
        if res == n {
            -1
        } else {
            res
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
define (min-subarray nums p)
    (let* (
        (n (length nums))
        (sum (apply + nums))
        (target (modulo sum p))
        (curr-sum 0)
        (res n))
        (if (zero? target)
            0
            (begin
                (for (
                    (i (range n))
                    (j (range i n)))
                    (set! curr-sum 0)
                    (for (
                        (k (range i (add1 j))))
                        (set! curr-sum (+ curr-sum (list-ref nums k))))
                    (when (zero? (modulo (- sum curr-sum) p))
                        (set! res (min res (- j i 1))))))
                (if (= res n)
                    -1
                    res))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
min_subarray(Nums, P) ->
    N = length(Nums),
    Sum = lists:sum(Nums),
    case Sum rem P of
        0 -> 0;
        _ ->
            Target = Sum rem P,
            CurrSum = 0,
            Res = N,
            lists:foldl(
                fun(I, {Res, CurrSum}) ->
                    CurrSum1 = 0,
                    lists:foldl(
                        fun(J, {Res, CurrSum}) ->
                            CurrSum1 = CurrSum + lists:nth(J + 1, Nums),
                            case (Sum - CurrSum1) rem P of
                                0 -> {min(Res, J - I + 1), CurrSum1};
                                _ -> {Res, CurrSum1}
                            end
                        end,
                        {Res, CurrSum},
                        lists:seq(I, N - 1))
                end,
                {Res, CurrSum},
                lists:seq(0, N - 1)),
            case Res of
                N -> -1;
                _ -> Res
            end
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
def min_subarray(nums, p) do
    n = length(nums)
    sum = Enum.sum(nums)
    cond do
        rem(sum, p) == 0 -> 0
        true ->
            target = rem(sum, p)
            curr_sum = 0
            res = n
            Enum.reduce(0..n-1, {res, curr_sum}, fn i, {res, curr_sum} ->
                curr_sum = 0
                Enum.reduce(i..n-1, {res, curr_sum}, fn j, {res, curr_sum} ->
                    curr_sum = curr_sum + Enum.at(nums, j)
                    if rem(sum - curr_sum, p) == 0 do
                        {min(res, j - i + 1), curr_sum}
                    else
                        {res, curr_sum}
                    end
                end)
            end)
            |> (fn {res, _} -> if res == n, do: -1, else: res end)
    end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of the solution is O(n^2) where n is the number of elements in the array. This is because we are iterating over all possible subarrays in the worst case. However, using a map to keep track of the rightmost index for every prefix sum % p can reduce the time complexity to O(n).

- **Space Complexity:** The space complexity of the solution is O(n) where n is the number of elements in the array. This is because we need to store the prefix sums and the map of rightmost indices for every prefix sum % p.

</div>
</details>
