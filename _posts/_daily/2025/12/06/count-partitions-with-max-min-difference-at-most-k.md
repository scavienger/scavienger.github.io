---
layout: post
title: "Count Partitions With Max-Min Difference at Most K"
date: 2025-12-06 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Dynamic Programming", "Queue", "Sliding Window", "Prefix Sum", "Monotonic Queue"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int countPartitions(std::vector<int>& nums,\
        \ int k) {\n        int n = nums.size();\n        long long MOD = 1e9 + 7;\n\
        \n        std::vector<long long> dp(n + 1, 0);\n        dp[0] = 1;\n\n     \
        \   std::vector<long long> prefix_sum_dp(n + 2, 0);\n        prefix_sum_dp[0]\
        \ = 0;\n        prefix_sum_dp[1] = 1;\n\n        std::deque<int> min_deque;\n\
        \        std::deque<int> max_deque;\n\n        int left = 0;\n\n        for\
        \ (int i = 1; i <= n; ++i) {\n            int current_num_idx = i - 1;\n   \
        \         int current_num_val = nums[current_num_idx];\n\n            while\
        \ (!min_deque.empty() && nums[min_deque.back()] >= current_num_val) {\n    \
        \            min_deque.pop_back();\n            }\n            min_deque.push_back(current_num_idx);\n\
        \n            while (!max_deque.empty() && nums[max_deque.back()] <= current_num_val)\
        \ {\n                max_deque.pop_back();\n            }\n            max_deque.push_back(current_num_idx);\n\
        \n            while (nums[max_deque.front()] - nums[min_deque.front()] > k)\
        \ {\n                left++;\n                if (min_deque.front() < left)\
        \ {\n                    min_deque.pop_front();\n                }\n       \
        \         if (max_deque.front() < left) {\n                    max_deque.pop_front();\n\
        \                }\n            }\n\n            dp[i] = (prefix_sum_dp[i] -\
        \ prefix_sum_dp[left] + MOD) % MOD;\n            prefix_sum_dp[i+1] = (prefix_sum_dp[i]\
        \ + dp[i]) % MOD;\n        }\n\n        return dp[n];\n    }\n};"
      java: "import java.util.ArrayDeque;\nimport java.util.Deque;\n\nclass Solution\
        \ {\n    public int countPartitions(int[] nums, int k) {\n        int n = nums.length;\n\
        \        long MOD = 1_000_000_007;\n\n        long[] dp = new long[n + 1];\n\
        \        dp[0] = 1;\n\n        long[] prefixSumDp = new long[n + 2];\n     \
        \   prefixSumDp[0] = 0;\n        prefixSumDp[1] = 1;\n\n        Deque<Integer>\
        \ minDeque = new ArrayDeque<>();\n        Deque<Integer> maxDeque = new ArrayDeque<>();\n\
        \n        int left = 0;\n\n        for (int i = 1; i <= n; ++i) {\n        \
        \    int currentNumIdx = i - 1;\n            int currentNumVal = nums[currentNumIdx];\n\
        \n            while (!minDeque.isEmpty() && nums[minDeque.peekLast()] >= currentNumVal)\
        \ {\n                minDeque.removeLast();\n            }\n            minDeque.addLast(currentNumIdx);\n\
        \n            while (!maxDeque.isEmpty() && nums[maxDeque.peekLast()] <= currentNumVal)\
        \ {\n                maxDeque.removeLast();\n            }\n            maxDeque.addLast(currentNumIdx);\n\
        \n            while (nums[maxDeque.peekFirst()] - nums[minDeque.peekFirst()]\
        \ > k) {\n                left++;\n                if (minDeque.peekFirst()\
        \ < left) {\n                    minDeque.removeFirst();\n                }\n\
        \                if (maxDeque.peekFirst() < left) {\n                    maxDeque.removeFirst();\n\
        \                }\n            }\n\n            dp[i] = (prefixSumDp[i] - prefixSumDp[left]\
        \ + MOD) % MOD;\n            prefixSumDp[i+1] = (prefixSumDp[i] + dp[i]) % MOD;\n\
        \        }\n\n        return (int) dp[n];\n    }\n}"
      python: "import collections\n\nclass Solution:\n    def countPartitions(self,\
        \ nums: list[int], k: int) -> int:\n        n = len(nums)\n        MOD = 10**9\
        \ + 7\n\n        dp = [0] * (n + 1)\n        dp[0] = 1\n\n        prefix_sum_dp\
        \ = [0] * (n + 2)\n        prefix_sum_dp[0] = 0\n        prefix_sum_dp[1] =\
        \ 1\n\n        min_deque = collections.deque() # Stores indices of elements\
        \ in increasing order of value\n        max_deque = collections.deque() # Stores\
        \ indices of elements in decreasing order of value\n\n        left = 0 # Left\
        \ pointer of the sliding window\n\n        for i in range(1, n + 1):\n     \
        \       current_num_idx = i - 1\n            current_num_val = nums[current_num_idx]\n\
        \n            # Maintain min_deque\n            while min_deque and nums[min_deque[-1]]\
        \ >= current_num_val:\n                min_deque.pop()\n            min_deque.append(current_num_idx)\n\
        \n            # Maintain max_deque\n            while max_deque and nums[max_deque[-1]]\
        \ <= current_num_val:\n                max_deque.pop()\n            max_deque.append(current_num_idx)\n\
        \n            # Shrink window from left if condition (max - min <= k) is violated\n\
        \            while nums[max_deque[0]] - nums[min_deque[0]] > k:\n          \
        \      left += 1\n                # Remove elements from deques if their indices\
        \ are outside the current window [left...current_num_idx]\n                if\
        \ min_deque[0] < left:\n                    min_deque.popleft()\n          \
        \      if max_deque[0] < left:\n                    max_deque.popleft()\n\n\
        \            # dp[i] = sum(dp[p] for p in [left, i-1])\n            # This sum\
        \ is (prefix_sum_dp[i] - prefix_sum_dp[left] + MOD) % MOD\n            dp[i]\
        \ = (prefix_sum_dp[i] - prefix_sum_dp[left] + MOD) % MOD\n\n            # Update\
        \ prefix_sum_dp for the next iteration\n            prefix_sum_dp[i+1] = (prefix_sum_dp[i]\
        \ + dp[i]) % MOD\n\n        return dp[n]"
      python3: "import collections\n\nclass Solution:\n    def countPartitions(self,\
        \ nums: list[int], k: int) -> int:\n        n = len(nums)\n        MOD = 10**9\
        \ + 7\n\n        dp = [0] * (n + 1)\n        dp[0] = 1\n\n        prefix_sum_dp\
        \ = [0] * (n + 2)\n        prefix_sum_dp[0] = 0\n        prefix_sum_dp[1] =\
        \ 1\n\n        min_deque = collections.deque() # Stores indices of elements\
        \ in increasing order of value\n        max_deque = collections.deque() # Stores\
        \ indices of elements in decreasing order of value\n\n        left = 0 # Left\
        \ pointer of the sliding window\n\n        for i in range(1, n + 1):\n     \
        \       current_num_idx = i - 1\n            current_num_val = nums[current_num_idx]\n\
        \n            # Maintain min_deque\n            while min_deque and nums[min_deque[-1]]\
        \ >= current_num_val:\n                min_deque.pop()\n            min_deque.append(current_num_idx)\n\
        \n            # Maintain max_deque\n            while max_deque and nums[max_deque[-1]]\
        \ <= current_num_val:\n                max_deque.pop()\n            max_deque.append(current_num_idx)\n\
        \n            # Shrink window from left if condition (max - min <= k) is violated\n\
        \            while nums[max_deque[0]] - nums[min_deque[0]] > k:\n          \
        \      left += 1\n                # Remove elements from deques if their indices\
        \ are outside the current window [left...current_num_idx]\n                if\
        \ min_deque[0] < left:\n                    min_deque.popleft()\n          \
        \      if max_deque[0] < left:\n                    max_deque.popleft()\n\n\
        \            # dp[i] = sum(dp[p] for p in [left, i-1])\n            # This sum\
        \ is (prefix_sum_dp[i] - prefix_sum_dp[left] + MOD) % MOD\n            dp[i]\
        \ = (prefix_sum_dp[i] - prefix_sum_dp[left] + MOD) % MOD\n\n            # Update\
        \ prefix_sum_dp for the next iteration\n            prefix_sum_dp[i+1] = (prefix_sum_dp[i]\
        \ + dp[i]) % MOD\n\n        return dp[n]"
      c: "#include <stdlib.h>\n#include <stdio.h>\n#include <stdbool.h>\n\n// A simple\
        \ deque implementation for integers (indices)\ntypedef struct {\n    int* arr;\n\
        \    int front;\n    int rear;\n    int capacity;\n    int size;\n} Deque;\n\
        \nDeque* createDeque(int capacity) {\n    Deque* deque = (Deque*)malloc(sizeof(Deque));\n\
        \    deque->capacity = capacity;\n    deque->arr = (int*)malloc(capacity * sizeof(int));\n\
        \    deque->front = 0;\n    deque->rear = -1;\n    deque->size = 0;\n    return\
        \ deque;\n}\n\nvoid freeDeque(Deque* deque) {\n    free(deque->arr);\n    free(deque);\n\
        }\n\nbool isEmpty(Deque* deque) {\n    return deque->size == 0;\n}\n\nvoid addLast(Deque*\
        \ deque, int item) {\n    if (deque->size == deque->capacity) return; // Should\
        \ not happen with proper capacity\n    deque->rear = (deque->rear + 1) % deque->capacity;\n\
        \    deque->arr[deque->rear] = item;\n    deque->size++;\n}\n\nint removeLast(Deque*\
        \ deque) {\n    if (isEmpty(deque)) return -1; // Error or sentinel\n    int\
        \ item = deque->arr[deque->rear];\n    deque->rear = (deque->rear - 1 + deque->capacity)\
        \ % deque->capacity;\n    deque->size--;\n    return item;\n}\n\nint peekLast(Deque*\
        \ deque) {\n    if (isEmpty(deque)) return -1; // Error or sentinel\n    return\
        \ deque->arr[deque->rear];\n}\n\nvoid addFirst(Deque* deque, int item) {\n \
        \   if (deque->size == deque->capacity) return; // Should not happen\n    deque->front\
        \ = (deque->front - 1 + deque->capacity) % deque->capacity;\n    deque->arr[deque->front]\
        \ = item;\n    deque->size++;\n}\n\nint removeFirst(Deque* deque) {\n    if\
        \ (isEmpty(deque)) return -1; // Error or sentinel\n    int item = deque->arr[deque->front];\n\
        \    deque->front = (deque->front + 1) % deque->capacity;\n    deque->size--;\n\
        \    return item;\n}\n\nint peekFirst(Deque* deque) {\n    if (isEmpty(deque))\
        \ return -1; // Error or sentinel\n    return deque->arr[deque->front];\n}\n\
        \nlong long countPartitions(int* nums, int numsSize, int k) {\n    int n = numsSize;\n\
        \    long long MOD = 1e9 + 7;\n\n    long long* dp = (long long*)calloc(n +\
        \ 1, sizeof(long long));\n    dp[0] = 1;\n\n    long long* prefix_sum_dp = (long\
        \ long*)calloc(n + 2, sizeof(long long));\n    prefix_sum_dp[0] = 0;\n    prefix_sum_dp[1]\
        \ = 1;\n\n    Deque* min_deque = createDeque(n);\n    Deque* max_deque = createDeque(n);\n\
        \n    int left = 0;\n\n    for (int i = 1; i <= n; ++i) {\n        int current_num_idx\
        \ = i - 1;\n        int current_num_val = nums[current_num_idx];\n\n       \
        \ while (!isEmpty(min_deque) && nums[peekLast(min_deque)] >= current_num_val)\
        \ {\n            removeLast(min_deque);\n        }\n        addLast(min_deque,\
        \ current_num_idx);\n\n        while (!isEmpty(max_deque) && nums[peekLast(max_deque)]\
        \ <= current_num_val) {\n            removeLast(max_deque);\n        }\n   \
        \     addLast(max_deque, current_num_idx);\n\n        while (nums[peekFirst(max_deque)]\
        \ - nums[peekFirst(min_deque)] > k) {\n            left++;\n            if (peekFirst(min_deque)\
        \ < left) {\n                removeFirst(min_deque);\n            }\n      \
        \      if (peekFirst(max_deque) < left) {\n                removeFirst(max_deque);\n\
        \            }\n        }\n\n        dp[i] = (prefix_sum_dp[i] - prefix_sum_dp[left]\
        \ + MOD) % MOD;\n        prefix_sum_dp[i+1] = (prefix_sum_dp[i] + dp[i]) % MOD;\n\
        \    }\n\n    long long result = dp[n];\n\n    free(dp);\n    free(prefix_sum_dp);\n\
        \    freeDeque(min_deque);\n    freeDeque(max_deque);\n\n    return result;\n\
        }"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int CountPartitions(int[] nums, int k) {\n        int n = nums.Length;\n\
        \        long MOD = 1_000_000_007;\n\n        long[] dp = new long[n + 1];\n\
        \        dp[0] = 1;\n\n        long[] prefixSumDp = new long[n + 2];\n     \
        \   prefixSumDp[0] = 0;\n        prefixSumDp[1] = 1;\n\n        LinkedList<int>\
        \ minDeque = new LinkedList<int>(); // Stores indices of elements in increasing\
        \ order of value\n        LinkedList<int> maxDeque = new LinkedList<int>();\
        \ // Stores indices of elements in decreasing order of value\n\n        int\
        \ left = 0; // Left pointer of the sliding window\n\n        for (int i = 1;\
        \ i <= n; ++i) {\n            int currentNumIdx = i - 1;\n            int currentNumVal\
        \ = nums[currentNumIdx];\n\n            // Maintain minDeque\n            while\
        \ (minDeque.Count > 0 && nums[minDeque.Last.Value] >= currentNumVal) {\n   \
        \             minDeque.RemoveLast();\n            }\n            minDeque.AddLast(currentNumIdx);\n\
        \n            // Maintain maxDeque\n            while (maxDeque.Count > 0 &&\
        \ nums[maxDeque.Last.Value] <= currentNumVal) {\n                maxDeque.RemoveLast();\n\
        \            }\n            maxDeque.AddLast(currentNumIdx);\n\n           \
        \ // Shrink window from left if condition (max - min <= k) is violated\n   \
        \         while (nums[maxDeque.First.Value] - nums[minDeque.First.Value] > k)\
        \ {\n                left++;\n                // Remove elements from deques\
        \ if their indices are outside the current window [left...currentNumIdx]\n \
        \               if (minDeque.First.Value < left) {\n                    minDeque.RemoveFirst();\n\
        \                }\n                if (maxDeque.First.Value < left) {\n   \
        \                 maxDeque.RemoveFirst();\n                }\n            }\n\
        \n            // dp[i] = sum(dp[p] for p in [left, i-1])\n            // This\
        \ sum is (prefixSumDp[i] - prefixSumDp[left] + MOD) % MOD\n            dp[i]\
        \ = (prefixSumDp[i] - prefixSumDp[left] + MOD) % MOD;\n\n            // Update\
        \ prefixSumDp for the next iteration\n            prefixSumDp[i+1] = (prefixSumDp[i]\
        \ + dp[i]) % MOD;\n        }\n\n        return (int)dp[n];\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} k\n * @return\
        \ {number}\n */\nvar countPartitions = function(nums, k) {\n    const n = nums.length;\n\
        \    const MOD = 10**9 + 7;\n\n    const dp = new Array(n + 1).fill(0);\n  \
        \  dp[0] = 1;\n\n    const prefixSumDp = new Array(n + 2).fill(0);\n    prefixSumDp[0]\
        \ = 0;\n    prefixSumDp[1] = 1;\n\n    const minDeque = []; // Stores indices\
        \ of elements in increasing order of value\n    const maxDeque = []; // Stores\
        \ indices of elements in decreasing order of value\n\n    let left = 0; // Left\
        \ pointer of the sliding window\n\n    for (let i = 1; i <= n; ++i) {\n    \
        \    const currentNumIdx = i - 1;\n        const currentNumVal = nums[currentNumIdx];\n\
        \n        // Maintain minDeque\n        while (minDeque.length > 0 && nums[minDeque[minDeque.length\
        \ - 1]] >= currentNumVal) {\n            minDeque.pop();\n        }\n      \
        \  minDeque.push(currentNumIdx);\n\n        // Maintain maxDeque\n        while\
        \ (maxDeque.length > 0 && nums[maxDeque[maxDeque.length - 1]] <= currentNumVal)\
        \ {\n            maxDeque.pop();\n        }\n        maxDeque.push(currentNumIdx);\n\
        \n        // Shrink window from left if condition (max - min <= k) is violated\n\
        \        while (nums[maxDeque[0]] - nums[minDeque[0]] > k) {\n            left++;\n\
        \            // Remove elements from deques if their indices are outside the\
        \ current window [left...currentNumIdx]\n            if (minDeque[0] < left)\
        \ {\n                minDeque.shift();\n            }\n            if (maxDeque[0]\
        \ < left) {\n                maxDeque.shift();\n            }\n        }\n\n\
        \        // dp[i] = sum(dp[p] for p in [left, i-1])\n        // This sum is\
        \ (prefixSumDp[i] - prefixSumDp[left] + MOD) % MOD\n        dp[i] = (prefixSumDp[i]\
        \ - prefixSumDp[left] + MOD) % MOD;\n\n        // Update prefixSumDp for the\
        \ next iteration\n        prefixSumDp[i+1] = (prefixSumDp[i] + dp[i]) % MOD;\n\
        \    }\n\n    return dp[n];\n};"
      typescript: "function countPartitions(nums: number[], k: number): number {\n \
        \   const n = nums.length;\n    const MOD = 10**9 + 7;\n\n    const dp: number[]\
        \ = new Array(n + 1).fill(0);\n    dp[0] = 1;\n\n    const prefixSumDp: number[]\
        \ = new Array(n + 2).fill(0);\n    prefixSumDp[0] = 0;\n    prefixSumDp[1] =\
        \ 1;\n\n    const minDeque: number[] = []; // Stores indices of elements in\
        \ increasing order of value\n    const maxDeque: number[] = []; // Stores indices\
        \ of elements in decreasing order of value\n\n    let left = 0; // Left pointer\
        \ of the sliding window\n\n    for (let i = 1; i <= n; ++i) {\n        const\
        \ currentNumIdx = i - 1;\n        const currentNumVal = nums[currentNumIdx];\n\
        \n        // Maintain minDeque\n        while (minDeque.length > 0 && nums[minDeque[minDeque.length\
        \ - 1]] >= currentNumVal) {\n            minDeque.pop();\n        }\n      \
        \  minDeque.push(currentNumIdx);\n\n        // Maintain maxDeque\n        while\
        \ (maxDeque.length > 0 && nums[maxDeque[maxDeque.length - 1]] <= currentNumVal)\
        \ {\n            maxDeque.pop();\n        }\n        maxDeque.push(currentNumIdx);\n\
        \n        // Shrink window from left if condition (max - min <= k) is violated\n\
        \        while (nums[maxDeque[0]] - nums[minDeque[0]] > k) {\n            left++;\n\
        \            // Remove elements from deques if their indices are outside the\
        \ current window [left...currentNumIdx]\n            if (minDeque[0] < left)\
        \ {\n                minDeque.shift();\n            }\n            if (maxDeque[0]\
        \ < left) {\n                maxDeque.shift();\n            }\n        }\n\n\
        \        // dp[i] = sum(dp[p] for p in [left, i-1])\n        // This sum is\
        \ (prefixSumDp[i] - prefixSumDp[left] + MOD) % MOD\n        dp[i] = (prefixSumDp[i]\
        \ - prefixSumDp[left] + MOD) % MOD;\n\n        // Update prefixSumDp for the\
        \ next iteration\n        prefixSumDp[i+1] = (prefixSumDp[i] + dp[i]) % MOD;\n\
        \    }\n\n    return dp[n];\n}"
      php: "<?php\nclass Solution {\n\n    /**\n     * @param Integer[] $nums\n    \
        \ * @param Integer $k\n     * @return Integer\n     */\n    function countPartitions($nums,\
        \ $k) {\n        $n = count($nums);\n        $MOD = 10**9 + 7;\n\n        $dp\
        \ = array_fill(0, $n + 1, 0);\n        $dp[0] = 1;\n\n        $prefixSumDp =\
        \ array_fill(0, $n + 2, 0);\n        $prefixSumDp[0] = 0;\n        $prefixSumDp[1]\
        \ = 1;\n\n        $minDeque = new SplDoublyLinkedList(); // Stores indices of\
        \ elements in increasing order of value\n        $maxDeque = new SplDoublyLinkedList();\
        \ // Stores indices of elements in decreasing order of value\n\n        $left\
        \ = 0; // Left pointer of the sliding window\n\n        for ($i = 1; $i <= $n;\
        \ ++$i) {\n            $currentNumIdx = $i - 1;\n            $currentNumVal\
        \ = $nums[$currentNumIdx];\n\n            // Maintain minDeque\n           \
        \ while (!$minDeque->isEmpty() && $nums[$minDeque->bottom()] >= $currentNumVal)\
        \ {\n                $minDeque->pop();\n            }\n            $minDeque->push($currentNumIdx);\n\
        \n            // Maintain maxDeque\n            while (!$maxDeque->isEmpty()\
        \ && $nums[$maxDeque->bottom()] <= $currentNumVal) {\n                $maxDeque->pop();\n\
        \            }\n            $maxDeque->push($currentNumIdx);\n\n           \
        \ // Shrink window from left if condition (max - min <= k) is violated\n   \
        \         while ($nums[$maxDeque->top()] - $nums[$minDeque->top()] > $k) {\n\
        \                $left++;\n                // Remove elements from deques if\
        \ their indices are outside the current window [left...currentNumIdx]\n    \
        \            if ($minDeque->top() < $left) {\n                    $minDeque->shift();\n\
        \                }\n                if ($maxDeque->top() < $left) {\n      \
        \              $maxDeque->shift();\n                }\n            }\n\n   \
        \         // dp[i] = sum(dp[p] for p in [left, i-1])\n            // This sum\
        \ is (prefixSumDp[i] - prefixSumDp[left] + MOD) % MOD\n            $dp[$i] =\
        \ ($prefixSumDp[$i] - $prefixSumDp[$left] + $MOD) % $MOD;\n\n            //\
        \ Update prefixSumDp for the next iteration\n            $prefixSumDp[$i+1]\
        \ = ($prefixSumDp[$i] + $dp[$i]) % $MOD;\n        }\n\n        return $dp[$n];\n\
        \    }\n}"
      swift: "import Foundation\n\nclass Solution {\n    func countPartitions(_ nums:\
        \ [Int], _ k: Int) -> Int {\n        let n = nums.count\n        let MOD = 1_000_000_007\n\
        \n        var dp = [Int](repeating: 0, count: n + 1)\n        dp[0] = 1\n\n\
        \        var prefixSumDp = [Int](repeating: 0, count: n + 2)\n        prefixSumDp[0]\
        \ = 0\n        prefixSumDp[1] = 1\n\n        var minDeque = [Int]() // Stores\
        \ indices of elements in increasing order of value\n        var maxDeque = [Int]()\
        \ // Stores indices of elements in decreasing order of value\n\n        var\
        \ left = 0 // Left pointer of the sliding window\n\n        for i in 1...n {\n\
        \            let currentNumIdx = i - 1\n            let currentNumVal = nums[currentNumIdx]\n\
        \n            // Maintain minDeque\n            while !minDeque.isEmpty && nums[minDeque.last!]\
        \ >= currentNumVal {\n                minDeque.removeLast()\n            }\n\
        \            minDeque.append(currentNumIdx)\n\n            // Maintain maxDeque\n\
        \            while !maxDeque.isEmpty && nums[maxDeque.last!] <= currentNumVal\
        \ {\n                maxDeque.removeLast()\n            }\n            maxDeque.append(currentNumIdx)\n\
        \n            // Shrink window from left if condition (max - min <= k) is violated\n\
        \            while nums[maxDeque.first!] - nums[minDeque.first!] > k {\n   \
        \             left += 1\n                // Remove elements from deques if their\
        \ indices are outside the current window [left...currentNumIdx]\n          \
        \      if minDeque.first! < left {\n                    minDeque.removeFirst()\n\
        \                }\n                if maxDeque.first! < left {\n          \
        \          maxDeque.removeFirst()\n                }\n            }\n\n    \
        \        // dp[i] = sum(dp[p] for p in [left, i-1])\n            // This sum\
        \ is (prefixSumDp[i] - prefixSumDp[left] + MOD) % MOD\n            dp[i] = (prefixSumDp[i]\
        \ - prefixSumDp[left] + MOD) % MOD\n\n            // Update prefixSumDp for\
        \ the next iteration\n            prefixSumDp[i+1] = (prefixSumDp[i] + dp[i])\
        \ % MOD\n        }\n\n        return dp[n]\n    }\n}"
      kotlin: "import java.util.ArrayDeque\n\nclass Solution {\n    fun countPartitions(nums:\
        \ IntArray, k: Int): Int {\n        val n = nums.size\n        val MOD = 1_000_000_007L\n\
        \n        val dp = LongArray(n + 1) { 0L }\n        dp[0] = 1L\n\n        val\
        \ prefixSumDp = LongArray(n + 2) { 0L }\n        prefixSumDp[0] = 0L\n     \
        \   prefixSumDp[1] = 1L\n\n        val minDeque = ArrayDeque<Int>() // Stores\
        \ indices of elements in increasing order of value\n        val maxDeque = ArrayDeque<Int>()\
        \ // Stores indices of elements in decreasing order of value\n\n        var\
        \ left = 0 // Left pointer of the sliding window\n\n        for (i in 1..n)\
        \ {\n            val currentNumIdx = i - 1\n            val currentNumVal =\
        \ nums[currentNumIdx]\n\n            // Maintain minDeque\n            while\
        \ (minDeque.isNotEmpty() && nums[minDeque.last()] >= currentNumVal) {\n    \
        \            minDeque.removeLast()\n            }\n            minDeque.addLast(currentNumIdx)\n\
        \n            // Maintain maxDeque\n            while (maxDeque.isNotEmpty()\
        \ && nums[maxDeque.last()] <= currentNumVal) {\n                maxDeque.removeLast()\n\
        \            }\n            maxDeque.addLast(currentNumIdx)\n\n            //\
        \ Shrink window from left if condition (max - min <= k) is violated\n      \
        \      while (nums[maxDeque.first()] - nums[minDeque.first()] > k) {\n     \
        \           left++\n                // Remove elements from deques if their\
        \ indices are outside the current window [left...currentNumIdx]\n          \
        \      if (minDeque.first() < left) {\n                    minDeque.removeFirst()\n\
        \                }\n                if (maxDeque.first() < left) {\n       \
        \             maxDeque.removeFirst()\n                }\n            }\n\n \
        \           // dp[i] = sum(dp[p] for p in [left, i-1])\n            // This\
        \ sum is (prefixSumDp[i] - prefixSumDp[left] + MOD) % MOD\n            dp[i]\
        \ = (prefixSumDp[i] - prefixSumDp[left] + MOD) % MOD\n\n            // Update\
        \ prefixSumDp for the next iteration\n            prefixSumDp[i+1] = (prefixSumDp[i]\
        \ + dp[i]) % MOD\n        }\n\n        return dp[n].toInt()\n    }\n}"
      dart: "import 'dart:collection';\n\nclass Solution {\n  int countPartitions(List<int>\
        \ nums, int k) {\n    final n = nums.length;\n    final MOD = 1000000007;\n\n\
        \    final dp = List<int>.filled(n + 1, 0);\n    dp[0] = 1;\n\n    final prefixSumDp\
        \ = List<int>.filled(n + 2, 0);\n    prefixSumDp[0] = 0;\n    prefixSumDp[1]\
        \ = 1;\n\n    final minDeque = DoubleLinkedQueue<int>(); // Stores indices of\
        \ elements in increasing order of value\n    final maxDeque = DoubleLinkedQueue<int>();\
        \ // Stores indices of elements in decreasing order of value\n\n    var left\
        \ = 0; // Left pointer of the sliding window\n\n    for (var i = 1; i <= n;\
        \ ++i) {\n      final currentNumIdx = i - 1;\n      final currentNumVal = nums[currentNumIdx];\n\
        \n      // Maintain minDeque\n      while (minDeque.isNotEmpty && nums[minDeque.last]\
        \ >= currentNumVal) {\n        minDeque.removeLast();\n      }\n      minDeque.addLast(currentNumIdx);\n\
        \n      // Maintain maxDeque\n      while (maxDeque.isNotEmpty && nums[maxDeque.last]\
        \ <= currentNumVal) {\n        maxDeque.removeLast();\n      }\n      maxDeque.addLast(currentNumIdx);\n\
        \n      // Shrink window from left if condition (max - min <= k) is violated\n\
        \      while (nums[maxDeque.first] - nums[minDeque.first] > k) {\n        left++;\n\
        \        // Remove elements from deques if their indices are outside the current\
        \ window [left...currentNumIdx]\n        if (minDeque.first < left) {\n    \
        \      minDeque.removeFirst();\n        }\n        if (maxDeque.first < left)\
        \ {\n          maxDeque.removeFirst();\n        }\n      }\n\n      // dp[i]\
        \ = sum(dp[p] for p in [left, i-1])\n      // This sum is (prefixSumDp[i] -\
        \ prefixSumDp[left] + MOD) % MOD\n      dp[i] = (prefixSumDp[i] - prefixSumDp[left]\
        \ + MOD) % MOD;\n\n      // Update prefixSumDp for the next iteration\n    \
        \  prefixSumDp[i+1] = (prefixSumDp[i] + dp[i]) % MOD;\n    }\n\n    return dp[n];\n\
        \  }\n}"
      go: "package main\n\nimport (\n\t\"container/list\"\n)\n\n// Solution struct for\
        \ the problem\ntype Solution struct{}\n\nfunc (s *Solution) countPartitions(nums\
        \ []int, k int) int {\n    n := len(nums)\n    MOD := 1_000_000_007\n\n    dp\
        \ := make([]int, n + 1)\n    dp[0] = 1\n\n    prefixSumDp := make([]int, n +\
        \ 2)\n    prefixSumDp[0] = 0\n    prefixSumDp[1] = 1\n\n    minDeque := list.New()\
        \ // Stores indices of elements in increasing order of value\n    maxDeque :=\
        \ list.New() // Stores indices of elements in decreasing order of value\n\n\
        \    left := 0 // Left pointer of the sliding window\n\n    for i := 1; i <=\
        \ n; i++ {\n        currentNumIdx := i - 1\n        currentNumVal := nums[currentNumIdx]\n\
        \n        // Maintain minDeque\n        for minDeque.Len() > 0 && nums[minDeque.Back().Value.(int)]\
        \ >= currentNumVal {\n            minDeque.Remove(minDeque.Back())\n       \
        \ }\n        minDeque.PushBack(currentNumIdx)\n\n        // Maintain maxDeque\n\
        \        for maxDeque.Len() > 0 && nums[maxDeque.Back().Value.(int)] <= currentNumVal\
        \ {\n            maxDeque.Remove(maxDeque.Back())\n        }\n        maxDeque.PushBack(currentNumIdx)\n\
        \n        // Shrink window from left if condition (max - min <= k) is violated\n\
        \        for nums[maxDeque.Front().Value.(int)] - nums[minDeque.Front().Value.(int)]\
        \ > k {\n            left++\n            // Remove elements from deques if their\
        \ indices are outside the current window [left...currentNumIdx]\n          \
        \  if minDeque.Front().Value.(int) < left {\n                minDeque.Remove(minDeque.Front())\n\
        \            }\n            if maxDeque.Front().Value.(int) < left {\n     \
        \           maxDeque.Remove(maxDeque.Front())\n            }\n        }\n\n\
        \        // dp[i] = sum(dp[p] for p in [left, i-1])\n        // This sum is\
        \ (prefixSumDp[i] - prefixSumDp[left] + MOD) % MOD\n        dp[i] = (prefixSumDp[i]\
        \ - prefixSumDp[left] + MOD) % MOD\n\n        // Update prefixSumDp for the\
        \ next iteration\n        prefixSumDp[i+1] = (prefixSumDp[i] + dp[i]) % MOD\n\
        \    }\n\n    return dp[n]\n}"
      ruby: "class Solution\n    # @param {Integer[]} nums\n    # @param {Integer} k\n\
        \    # @return {Integer}\n    def count_partitions(nums, k)\n        n = nums.length\n\
        \        mod = 10**9 + 7\n\n        dp = Array.new(n + 1, 0)\n        dp[0]\
        \ = 1\n\n        prefix_sum_dp = Array.new(n + 2, 0)\n        prefix_sum_dp[0]\
        \ = 0\n        prefix_sum_dp[1] = 1\n\n        min_deque = [] # Stores indices\
        \ of elements in increasing order of value\n        max_deque = [] # Stores\
        \ indices of elements in decreasing order of value\n\n        left = 0 # Left\
        \ pointer of the sliding window\n\n        (1..n).each do |i|\n            current_num_idx\
        \ = i - 1\n            current_num_val = nums[current_num_idx]\n\n         \
        \   # Maintain min_deque\n            while !min_deque.empty? && nums[min_deque.last]\
        \ >= current_num_val\n                min_deque.pop\n            end\n     \
        \       min_deque.push(current_num_idx)\n\n            # Maintain max_deque\n\
        \            while !max_deque.empty? && nums[max_deque.last] <= current_num_val\n\
        \                max_deque.pop\n            end\n            max_deque.push(current_num_idx)\n\
        \n            # Shrink window from left if condition (max - min <= k) is violated\n\
        \            while nums[max_deque.first] - nums[min_deque.first] > k\n     \
        \           left += 1\n                # Remove elements from deques if their\
        \ indices are outside the current window [left...current_num_idx]\n        \
        \        min_deque.shift if min_deque.first < left\n                max_deque.shift\
        \ if max_deque.first < left\n            end\n\n            # dp[i] = sum(dp[p]\
        \ for p in [left, i-1])\n            # This sum is (prefix_sum_dp[i] - prefix_sum_dp[left]\
        \ + MOD) % MOD\n            dp[i] = (prefix_sum_dp[i] - prefix_sum_dp[left]\
        \ + mod) % mod\n\n            # Update prefix_sum_dp for the next iteration\n\
        \            prefix_sum_dp[i+1] = (prefix_sum_dp[i] + dp[i]) % mod\n       \
        \ end\n\n        dp[n]\n    end\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n    def countPartitions(nums:\
        \ Array[Int], k: Int): Int = {\n        val n = nums.length\n        val MOD\
        \ = 1_000_000_007L\n\n        val dp = Array.fill(n + 1)(0L)\n        dp(0)\
        \ = 1L\n\n        val prefixSumDp = Array.fill(n + 2)(0L)\n        prefixSumDp(0)\
        \ = 0L\n        prefixSumDp(1) = 1L\n\n        val minDeque = mutable.ArrayDeque[Int]()\
        \ // Stores indices of elements in increasing order of value\n        val maxDeque\
        \ = mutable.ArrayDeque[Int]() // Stores indices of elements in decreasing order\
        \ of value\n\n        var left = 0 // Left pointer of the sliding window\n\n\
        \        for (i <- 1 to n) {\n            val currentNumIdx = i - 1\n      \
        \      val currentNumVal = nums(currentNumIdx)\n\n            // Maintain minDeque\n\
        \            while (minDeque.nonEmpty && nums(minDeque.last) >= currentNumVal)\
        \ {\n                minDeque.removeLast()\n            }\n            minDeque.addLast(currentNumIdx)\n\
        \n            // Maintain maxDeque\n            while (maxDeque.nonEmpty &&\
        \ nums(maxDeque.last) <= currentNumVal) {\n                maxDeque.removeLast()\n\
        \            }\n            maxDeque.addLast(currentNumIdx)\n\n            //\
        \ Shrink window from left if condition (max - min <= k) is violated\n      \
        \      while (nums(maxDeque.head) - nums(minDeque.head) > k) {\n           \
        \     left += 1\n                // Remove elements from deques if their indices\
        \ are outside the current window [left...currentNumIdx]\n                if\
        \ (minDeque.head < left) {\n                    minDeque.removeHead()\n    \
        \            }\n                if (maxDeque.head < left) {\n              \
        \      maxDeque.removeHead()\n                }\n            }\n\n         \
        \   // dp(i) = sum(dp(p) for p in [left, i-1])\n            // This sum is (prefixSumDp(i)\
        \ - prefixSumDp(left) + MOD) % MOD\n            dp(i) = (prefixSumDp(i) - prefixSumDp(left)\
        \ + MOD) % MOD\n\n            // Update prefixSumDp for the next iteration\n\
        \            prefixSumDp(i+1) = (prefixSumDp(i) + dp(i)) % MOD\n        }\n\n\
        \        dp(n).toInt\n    }\n}"
      rust: "use std::collections::VecDeque;\n\nimpl Solution {\n    pub fn count_partitions(nums:\
        \ Vec<i32>, k: i32) -> i32 {\n        let n = nums.len();\n        let k_long\
        \ = k as i64;\n        let modular = 1_000_000_007;\n\n        let mut dp =\
        \ vec![0; n + 1];\n        dp[0] = 1;\n\n        let mut prefix_sum_dp = vec![0;\
        \ n + 2];\n        prefix_sum_dp[0] = 0;\n        prefix_sum_dp[1] = 1;\n\n\
        \        let mut min_deque: VecDeque<usize> = VecDeque::new(); // Stores indices\
        \ of elements in increasing order of value\n        let mut max_deque: VecDeque<usize>\
        \ = VecDeque::new(); // Stores indices of elements in decreasing order of value\n\
        \n        let mut left = 0; // Left pointer of the sliding window\n\n      \
        \  for i in 1..=n {\n            let current_num_idx = i - 1;\n            let\
        \ current_num_val = nums[current_num_idx];\n\n            // Maintain min_deque\n\
        \            while let Some(&last_idx) = min_deque.back() {\n              \
        \  if nums[last_idx] >= current_num_val {\n                    min_deque.pop_back();\n\
        \                } else {\n                    break;\n                }\n \
        \           }\n            min_deque.push_back(current_num_idx);\n\n       \
        \     // Maintain max_deque\n            while let Some(&last_idx) = max_deque.back()\
        \ {\n                if nums[last_idx] <= current_num_val {\n              \
        \      max_deque.pop_back();\n                } else {\n                   \
        \ break;\n                }\n            }\n            max_deque.push_back(current_num_idx);\n\
        \n            // Shrink window from left if condition (max - min <= k) is violated\n\
        \            while (nums[*max_deque.front().unwrap()] as i64) - (nums[*min_deque.front().unwrap()]\
        \ as i64) > k_long {\n                left += 1;\n                // Remove\
        \ elements from deques if their indices are outside the current window [left...current_num_idx]\n\
        \                if *min_deque.front().unwrap() < left {\n                 \
        \   min_deque.pop_front();\n                }\n                if *max_deque.front().unwrap()\
        \ < left {\n                    max_deque.pop_front();\n                }\n\
        \            }\n\n            // dp[i] = sum(dp[p] for p in [left, i-1])\n \
        \           // This sum is (prefix_sum_dp[i] - prefix_sum_dp[left] + MOD) %\
        \ MOD\n            dp[i] = (prefix_sum_dp[i] - prefix_sum_dp[left] + modular)\
        \ % modular;\n\n            // Update prefix_sum_dp for the next iteration\n\
        \            prefix_sum_dp[i+1] = (prefix_sum_dp[i] + dp[i]) % modular;\n  \
        \      }\n\n        dp[n] as i32\n    }\n}"
      racket: "#lang racket\n\n(define (count-partitions nums k)\n  (define n (vector-length\
        \ nums))\n  (define MOD 1000000007)\n\n  (define dp (make-vector (+ n 1) 0))\n\
        \  (vector-set! dp 0 1)\n\n  (define prefix-sum-dp (make-vector (+ n 2) 0))\n\
        \  (vector-set! prefix-sum-dp 0 0)\n  (vector-set! prefix-sum-dp 1 1)\n\n  (define\
        \ min-deque (make-deque)) ; Stores indices of elements in increasing order of\
        \ value\n  (define max-deque (make-deque)) ; Stores indices of elements in decreasing\
        \ order of value\n\n  (define left (box 0)) ; Left pointer of the sliding window\n\
        \n  (for ([i (in-range 1 (+ n 1))])\n    (define current-num-idx (- i 1))\n\
        \    (define current-num-val (vector-ref nums current-num-idx))\n\n    ; Maintain\
        \ min-deque\n    (while (and (not (deque-empty? min-deque))\n              \
        \  (>= (vector-ref nums (deque-back min-deque)) current-num-val))\n      (deque-pop-back!\
        \ min-deque))\n    (deque-push-back! min-num-idx)\n\n    ; Maintain max-deque\n\
        \    (while (and (not (deque-empty? max-deque))\n                (<= (vector-ref\
        \ nums (deque-back max-deque)) current-num-val))\n      (deque-pop-back! max-deque))\n\
        \    (deque-push-back! max-deque current-num-idx)\n\n    ; Shrink window from\
        \ left if condition (max - min <= k) is violated\n    (while (> (- (vector-ref\
        \ nums (deque-front max-deque))\n                 (vector-ref nums (deque-front\
        \ min-deque)))\n              k)\n      (set-box! left (+ (unbox left) 1))\n\
        \      ; Remove elements from deques if their indices are outside the current\
        \ window [left...current-num-idx]\n      (when (< (deque-front min-deque) (unbox\
        \ left))\n        (deque-pop-front! min-deque))\n      (when (< (deque-front\
        \ max-deque) (unbox left))\n        (deque-pop-front! max-deque)))\n\n    ;\
        \ dp[i] = sum(dp[p] for p in [left, i-1])\n    ; This sum is (prefix-sum-dp[i]\
        \ - prefix-sum-dp[left] + MOD) % MOD\n    (vector-set! dp i\n              \
        \   (modulo (+ (- (vector-ref prefix-sum-dp i)\n                           \
        \     (vector-ref prefix-sum-dp (unbox left)))\n                           \
        \ MOD)\n                         MOD))\n\n    ; Update prefix-sum-dp for the\
        \ next iteration\n    (vector-set! prefix-sum-dp (+ i 1)\n                 (modulo\
        \ (+ (vector-ref prefix-sum-dp i)\n                            (vector-ref dp\
        \ i))\n                         MOD)))\n\n  (vector-ref dp n))"
      erlang: "-module(solution).\n-export([count_partitions/2]).\n\ncount_partitions(Nums,\
        \ K) ->\n    N = length(Nums),\n    MOD = 1000000007,\n\n    Dp = array:new([{size,\
        \ N + 1}, {fixed, true}, {default, 0}]),\n    Dp1 = array:set(0, 1, Dp),\n\n\
        \    PrefixSumDp = array:new([{size, N + 2}, {fixed, true}, {default, 0}]),\n\
        \    PrefixSumDp1 = array:set(0, 0, PrefixSumDp),\n    PrefixSumDp2 = array:set(1,\
        \ 1, PrefixSumDp1),\n\n    MinDeque = queue:new(), % Stores indices of elements\
        \ in increasing order of value\n    MaxDeque = queue:new(), % Stores indices\
        \ of elements in decreasing order of value\n\n    Left = 0, % Left pointer of\
        \ the sliding window\n\n    count_partitions_loop(1, N, Nums, K, MOD, Dp1, PrefixSumDp2,\
        \ MinDeque, MaxDeque, Left).\n\ncount_partitions_loop(I, N, Nums, K, MOD, Dp,\
        \ PrefixSumDp, MinDeque, MaxDeque, Left) when I =< N ->\n    CurrentNumIdx =\
        \ I - 1,\n    CurrentNumVal = lists:nth(CurrentNumIdx + 1, Nums),\n\n    % Maintain\
        \ MinDeque\n    MinDeque1 = update_min_deque(MinDeque, Nums, CurrentNumIdx,\
        \ CurrentNumVal),\n\n    % Maintain MaxDeque\n    MaxDeque1 = update_max_deque(MaxDeque,\
        \ Nums, CurrentNumIdx, CurrentNumVal),\n\n    % Shrink window from left if condition\
        \ (max - min <= k) is violated\n    {Left1, MinDeque2, MaxDeque2} = shrink_window(Left,\
        \ Nums, K, MinDeque1, MaxDeque1),\n\n    % Dp[I] = sum(Dp[P] for P in [Left1,\
        \ I-1])\n    % This sum is (PrefixSumDp[I] - PrefixSumDp[Left1] + MOD) % MOD\n\
        \    DpI = (array:get(I, PrefixSumDp) - array:get(Left1, PrefixSumDp) + MOD)\
        \ rem MOD,\n    Dp3 = array:set(I, DpI, Dp),\n\n    % Update PrefixSumDp for\
        \ the next iteration\n    PrefixSumDpIPlus1 = (array:get(I, PrefixSumDp) + DpI)\
        \ rem MOD,\n    PrefixSumDp3 = array:set(I + 1, PrefixSumDpIPlus1, PrefixSumDp),\n\
        \n    count_partitions_loop(I + 1, N, Nums, K, MOD, Dp3, PrefixSumDp3, MinDeque2,\
        \ MaxDeque2, Left1);\ncount_partitions_loop(I, N, _Nums, _K, _MOD, Dp, _PrefixSumDp,\
        \ _MinDeque, _MaxDeque, _Left) when I > N ->\n    array:get(N, Dp).\n\nupdate_min_deque(MinDeque,\
        \ Nums, CurrentNumIdx, CurrentNumVal) ->\n    case queue:is_empty(MinDeque)\
        \ of\n        true -> queue:in(CurrentNumIdx, MinDeque);\n        false ->\n\
        \            LastIdx = queue:last(MinDeque),\n            case lists:nth(LastIdx\
        \ + 1, Nums) >= CurrentNumVal of\n                true -> update_min_deque(queue:del_last(MinDeque),\
        \ Nums, CurrentNumIdx, CurrentNumVal);\n                false -> queue:in(CurrentNumIdx,\
        \ MinDeque)\n            end\n    end.\n\nupdate_max_deque(MaxDeque, Nums, CurrentNumIdx,\
        \ CurrentNumVal) ->\n    case queue:is_empty(MaxDeque) of\n        true -> queue:in(CurrentNumIdx,\
        \ MaxDeque);\n        false ->\n            LastIdx = queue:last(MaxDeque),\n\
        \            case lists:nth(LastIdx + 1, Nums) <= CurrentNumVal of\n       \
        \         true -> update_max_deque(queue:del_last(MaxDeque), Nums, CurrentNumIdx,\
        \ CurrentNumVal);\n                false -> queue:in(CurrentNumIdx, MaxDeque)\n\
        \            end\n    end.\n\nshrink_window(Left, Nums, K, MinDeque, MaxDeque)\
        \ ->\n    MaxVal = lists:nth(queue:head(MaxDeque) + 1, Nums),\n    MinVal =\
        \ lists:nth(queue:head(MinDeque) + 1, Nums),\n    case MaxVal - MinVal > K of\n\
        \        true ->\n            Left1 = Left + 1,\n            MinDeque1 = case\
        \ queue:head(MinDeque) < Left1 of\n                            true -> queue:del_head(MinDeque);\n\
        \                            false -> MinDeque\n                        end,\n\
        \            MaxDeque1 = case queue:head(MaxDeque) < Left1 of\n            \
        \                true -> queue:del_head(MaxDeque);\n                       \
        \     false -> MaxDeque\n                        end,\n            shrink_window(Left1,\
        \ Nums, K, MinDeque1, MaxDeque1);\n        false ->\n            {Left, MinDeque,\
        \ MaxDeque}\n    end."
      elixir: "defmodule Solution do\n  @moduledoc \"\"\"Solution for Count Partitions\
        \ With Max-Min Difference at Most K.\"\"\"\n\n  @spec count_partitions(nums\
        \ :: [integer], k :: integer) :: integer\n  def count_partitions(nums, k) do\n\
        \    n = length(nums)\n    mod = 1_000_000_007\n\n    # dp[i] will store the\
        \ number of ways to partition nums[0...i-1]\n    # dp[0] = 1 represents one\
        \ way to partition an empty prefix (base case)\n    dp = :array.new([{size:\
        \ n + 1, fixed: true, default: 0}])\n    dp = :array.set(0, 1, dp)\n\n    #\
        \ prefix_sum_dp[i] will store (dp[0] + ... + dp[i-1]) % MOD\n    # This allows\
        \ calculating sum(dp[j] for j in [left, i-1]) as (prefix_sum_dp[i] - prefix_sum_dp[left]\
        \ + MOD) % MOD\n    prefix_sum_dp = :array.new([{size: n + 2, fixed: true, default:\
        \ 0}])\n    prefix_sum_dp = :array.set(0, 0, prefix_sum_dp)\n    prefix_sum_dp\
        \ = :array.set(1, 1, prefix_sum_dp)\n\n    # Deques to maintain min and max\
        \ in the current window [left...i-1]\n    min_deque = :queue.new() # Stores\
        \ indices of elements in increasing order of value\n    max_deque = :queue.new()\
        \ # Stores indices of elements in decreasing order of value\n\n    left = 0\
        \ # Left pointer of the sliding window\n\n    # Elixir's for loop is a comprehension,\
        \ not suitable for mutable state like this.\n    # Using a recursive helper\
        \ function to simulate the loop.\n    loop_partitions(1, n, nums, k, mod, dp,\
        \ prefix_sum_dp, min_deque, max_deque, left)\n  end\n\n  defp loop_partitions(i,\
        \ n, nums, k, mod, dp, prefix_sum_dp, min_deque, max_deque, left) when i <=\
        \ n do\n    current_num_idx = i - 1\n    current_num_val = Enum.at(nums, current_num_idx)\n\
        \n    # Maintain min_deque\n    min_deque = update_min_deque(min_deque, nums,\
        \ current_num_idx, current_num_val)\n\n    # Maintain max_deque\n    max_deque\
        \ = update_max_deque(max_deque, nums, current_num_idx, current_num_val)\n\n\
        \    # Shrink window from left if condition (max - min <= k) is violated\n \
        \   {left, min_deque, max_deque} = shrink_window(left, nums, k, min_deque, max_deque)\n\
        \n    # dp[i] = sum(dp[p] for p in [left, i-1])\n    # This sum is (prefix_sum_dp[i]\
        \ - prefix_sum_dp[left] + MOD) % MOD\n    dp_i = (:array.get(i, prefix_sum_dp)\
        \ - :array.get(left, prefix_sum_dp) + mod) |> rem(mod)\n    dp = :array.set(i,\
        \ dp_i, dp)\n\n    # Update prefix_sum_dp for the next iteration\n    prefix_sum_dp_i_plus_1\
        \ = (:array.get(i, prefix_sum_dp) + dp_i) |> rem(mod)\n    prefix_sum_dp = :array.set(i\
        \ + 1, prefix_sum_dp_i_plus_1, prefix_sum_dp)\n\n    loop_partitions(i + 1,\
        \ n, nums, k, mod, dp, prefix_sum_dp, min_deque, max_deque, left)\n  end\n\n\
        \  defp loop_partitions(_i, n, _nums, _k, _mod, dp, _prefix_sum_dp, _min_deque,\
        \ _max_deque, _left) do\n    :array.get(n, dp)\n  end\n\n  defp update_min_deque(min_deque,\
        \ nums, current_num_idx, current_num_val) do\n    case :queue.is_empty(min_deque)\
        \ do\n      true -> :queue.in(current_num_idx, min_deque)\n      false ->\n\
        \        {_val, last_idx} = :queue.last(min_deque)\n        if Enum.at(nums,\
        \ last_idx) >= current_num_val do\n          update_min_deque(:queue.del_last(min_deque),\
        \ nums, current_num_idx, current_num_val)\n        else\n          :queue.in(current_num_idx,\
        \ min_deque)\n        end\n    end\n  end\n\n  defp update_max_deque(max_deque,\
        \ nums, current_num_idx, current_num_val) do\n    case :queue.is_empty(max_deque)\
        \ do\n      true -> :queue.in(current_num_idx, max_deque)\n      false ->\n\
        \        {_val, last_idx} = :queue.last(max_deque)\n        if Enum.at(nums,\
        \ last_idx) <= current_num_val do\n          update_max_deque(:queue.del_last(max_deque),\
        \ nums, current_num_idx, current_num_val)\n        else\n          :queue.in(current_num_idx,\
        \ max_deque)\n        end\n    end\n  end\n\n  defp shrink_window(left, nums,\
        \ k, min_deque, max_deque) do\n    {_val, max_idx} = :queue.head(max_deque)\n\
        \    {_val, min_idx} = :queue.head(min_deque)\n    max_val = Enum.at(nums, max_idx)\n\
        \    min_val = Enum.at(nums, min_idx)\n\n    if max_val - min_val > k do\n \
        \     left_new = left + 1\n      min_deque_new = if min_idx < left_new, do:\
        \ :queue.del_head(min_deque), else: min_deque\n      max_deque_new = if max_idx\
        \ < left_new, do: :queue.del_head(max_deque), else: max_deque\n      shrink_window(left_new,\
        \ nums, k, min_deque_new, max_deque_new)\n    else\n      {left, min_deque,\
        \ max_deque}\n    end\n  end\nend"
    approach: 'The problem asks for the number of ways to partition an array `nums`
      into contiguous segments such that the difference between the maximum and minimum
      elements in each segment is at most `k`. This can be solved using dynamic programming.
      Let `dp[i]` be the number of ways to partition the prefix `nums[0...i-1]` according
      to the given conditions. The base case is `dp[0] = 1`, representing one way to
      partition an empty prefix. To compute `dp[i]`, we consider the last segment ending
      at `nums[i-1]`. This segment could start at any index `j` (where `0 <= j < i`)
      such that `nums[j...i-1]` is a valid segment (i.e., `max(nums[j...i-1]) - min(nums[j...i-1])
      <= k`). If `nums[j...i-1]` is a valid segment, then we can add `dp[j]` to `dp[i]`.
      Thus, `dp[i] = sum(dp[j])` for all valid `j`s.


      To efficiently find the valid `j`s and compute their sum, we use a sliding window
      approach combined with prefix sums. As we iterate `i` from `1` to `N` (where `N`
      is `nums.length`), we maintain a window `nums[left...i-1]` that represents the
      longest valid segment ending at `i-1`. We use two monotonic deques (one for minimums,
      one for maximums) to keep track of the min and max elements within this window
      in O(1) time. If `max(window) - min(window) > k`, we shrink the window from the
      `left` until the condition is met. Once the `left` pointer is established for
      `i`, all segments `nums[p...i-1]` where `p` is in `[left, i-1]` are valid. The
      sum `sum(dp[p])` for `p` from `left` to `i-1` can be calculated using a `prefix_sum_dp`
      array: `(prefix_sum_dp[i] - prefix_sum_dp[left] + MOD) % MOD`. The `prefix_sum_dp[x]`
      stores the sum `dp[0] + ... + dp[x-1]`. The final answer is `dp[N].`'
    time_complexity: The time complexity is O(N), where N is the length of the `nums`
      array. The main loop iterates N times (from `i = 1` to `N`). Inside the loop,
      each element is added to and removed from the monotonic deques at most once. The
      `left` pointer for the sliding window also moves forward at most N times in total.
      All operations within the loop (deque operations, arithmetic calculations) take
      O(1) time. Therefore, the overall time complexity is linear with respect to the
      input array size.
    space_complexity: The space complexity is O(N). We use a `dp` array of size `N+1`
      and a `prefix_sum_dp` array of size `N+2` to store intermediate results. Additionally,
      two monotonic deques are used to efficiently track the minimum and maximum elements
      within the sliding window. In the worst case, each deque can store up to N indices.
      Thus, the total space required is proportional to N.
    elapsed_time: 133.6131021976471
    model: gemini-2.5-flash
    generated_at: '2025-12-06 01:04:14 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int countPartitions(vector<int>& nums, int\
        \ k) {\n        int n = nums.size();\n        vector<int> dp(n + 1, 0);\n  \
        \      dp[0] = 1;\n        for (int i = 1; i <= n; i++) {\n            int maxVal\
        \ = nums[i - 1];\n            int minVal = nums[i - 1];\n            for (int\
        \ j = i - 1; j >= 0; j--) {\n                maxVal = max(maxVal, nums[j]);\n\
        \                minVal = min(minVal, nums[j]);\n                if (maxVal\
        \ - minVal <= k) {\n                    dp[i] = (dp[i] + dp[j]) % (1000000007);\n\
        \                }\n            }\n        }\n        return dp[n];\n    }\n\
        };"
      java: "class Solution {\n    public int countPartitions(int[] nums, int k) {\n\
        \        int n = nums.length;\n        int[] dp = new int[n + 1];\n        dp[0]\
        \ = 1;\n        for (int i = 1; i <= n; i++) {\n            int maxVal = nums[i\
        \ - 1];\n            int minVal = nums[i - 1];\n            for (int j = i -\
        \ 1; j >= 0; j--) {\n                maxVal = Math.max(maxVal, nums[j]);\n \
        \               minVal = Math.min(minVal, nums[j]);\n                if (maxVal\
        \ - minVal <= k) {\n                    dp[i] = (dp[i] + dp[j]) % 1000000007;\n\
        \                }\n            }\n        }\n        return dp[n];\n    }\n\
        }"
      python: "class Solution:\n    def countPartitions(self, nums: list[int], k: int)\
        \ -> int:\n        n = len(nums)\n        dp = [0] * (n + 1)\n        dp[0]\
        \ = 1\n        for i in range(1, n + 1):\n            max_val = nums[i - 1]\n\
        \            min_val = nums[i - 1]\n            for j in range(i - 1, -1, -1):\n\
        \                max_val = max(max_val, nums[j])\n                min_val =\
        \ min(min_val, nums[j])\n                if max_val - min_val <= k:\n      \
        \              dp[i] = (dp[i] + dp[j]) % 1000000007\n        return dp[n]"
      python3: "class Solution:\n    def countPartitions(self, nums: list[int], k: int)\
        \ -> int:\n        n = len(nums)\n        dp = [0] * (n + 1)\n        dp[0]\
        \ = 1\n        for i in range(1, n + 1):\n            max_val = nums[i - 1]\n\
        \            min_val = nums[i - 1]\n            for j in range(i - 1, -1, -1):\n\
        \                max_val = max(max_val, nums[j])\n                min_val =\
        \ min(min_val, nums[j])\n                if max_val - min_val <= k:\n      \
        \              dp[i] = (dp[i] + dp[j]) % 1000000007\n        return dp[n]"
      c: "typedef long long ll;\n\nstruct Solution {\n    int countPartitions(int* nums,\
        \ int numsSize, int k) {\n        int* dp = (int*)malloc((numsSize + 1) * sizeof(int));\n\
        \        dp[0] = 1;\n        for (int i = 1; i <= numsSize; i++) {\n       \
        \     int maxVal = nums[i - 1];\n            int minVal = nums[i - 1];\n   \
        \         for (int j = i - 1; j >= 0; j--) {\n                maxVal = (maxVal\
        \ > nums[j]) ? maxVal : nums[j];\n                minVal = (minVal < nums[j])\
        \ ? minVal : nums[j];\n                if (maxVal - minVal <= k) {\n       \
        \             dp[i] = (dp[i] + dp[j]) % 1000000007;\n                }\n   \
        \         }\n        }\n        int result = dp[numsSize];\n        free(dp);\n\
        \        return result;\n    }\n};"
      csharp: "public class Solution {\n    public int CountPartitions(int[] nums, int\
        \ k) {\n        int n = nums.Length;\n        int[] dp = new int[n + 1];\n \
        \       dp[0] = 1;\n        for (int i = 1; i <= n; i++) {\n            int\
        \ maxVal = nums[i - 1];\n            int minVal = nums[i - 1];\n           \
        \ for (int j = i - 1; j >= 0; j--) {\n                maxVal = Math.Max(maxVal,\
        \ nums[j]);\n                minVal = Math.Min(minVal, nums[j]);\n         \
        \       if (maxVal - minVal <= k) {\n                    dp[i] = (dp[i] + dp[j])\
        \ % 1000000007;\n                }\n            }\n        }\n        return\
        \ dp[n];\n    }\n}"
      javascript: "var countPartitions = function(nums, k) {\n    let n = nums.length;\n\
        \    let dp = new Array(n + 1).fill(0);\n    dp[0] = 1;\n    for (let i = 1;\
        \ i <= n; i++) {\n        let maxVal = nums[i - 1];\n        let minVal = nums[i\
        \ - 1];\n        for (let j = i - 1; j >= 0; j--) {\n            maxVal = Math.max(maxVal,\
        \ nums[j]);\n            minVal = Math.min(minVal, nums[j]);\n            if\
        \ (maxVal - minVal <= k) {\n                dp[i] = (dp[i] + dp[j]) % 1000000007;\n\
        \            }\n        }\n    }\n    return dp[n];\n};"
      typescript: "function countPartitions(nums: number[], k: number): number {\n \
        \   let n = nums.length;\n    let dp: number[] = new Array(n + 1).fill(0);\n\
        \    dp[0] = 1;\n    for (let i = 1; i <= n; i++) {\n        let maxVal = nums[i\
        \ - 1];\n        let minVal = nums[i - 1];\n        for (let j = i - 1; j >=\
        \ 0; j--) {\n            maxVal = Math.max(maxVal, nums[j]);\n            minVal\
        \ = Math.min(minVal, nums[j]);\n            if (maxVal - minVal <= k) {\n  \
        \              dp[i] = (dp[i] + dp[j]) % 1000000007;\n            }\n      \
        \  }\n    }\n    return dp[n];\n}"
      php: "class Solution {\n    function countPartitions($nums, $k) {\n        $n\
        \ = count($nums);\n        $dp = array_fill(0, $n + 1, 0);\n        $dp[0] =\
        \ 1;\n        for ($i = 1; $i <= $n; $i++) {\n            $maxVal = $nums[$i\
        \ - 1];\n            $minVal = $nums[$i - 1];\n            for ($j = $i - 1;\
        \ $j >= 0; $j--) {\n                $maxVal = max($maxVal, $nums[$j]);\n   \
        \             $minVal = min($minVal, $nums[$j]);\n                if ($maxVal\
        \ - $minVal <= $k) {\n                    $dp[$i] = ($dp[$i] + $dp[$j]) % 1000000007;\n\
        \                }\n            }\n        }\n        return $dp[$n];\n    }\n\
        }"
      swift: "class Solution {\n    func countPartitions(_ nums: [Int], _ k: Int) ->\
        \ Int {\n        let n = nums.count\n        var dp = [Int](repeating: 0, count:\
        \ n + 1)\n        dp[0] = 1\n        for i in 1...n {\n            var maxVal\
        \ = nums[i - 1]\n            var minVal = nums[i - 1]\n            for j in\
        \ stride(from: i - 1, through: 0, by: -1) {\n                maxVal = max(maxVal,\
        \ nums[j])\n                minVal = min(minVal, nums[j])\n                if\
        \ maxVal - minVal <= k {\n                    dp[i] = (dp[i] + dp[j]) % 1000000007\n\
        \                }\n            }\n        }\n        return dp[n]\n    }\n}"
      kotlin: "class Solution {\n    fun countPartitions(nums: IntArray, k: Int): Int\
        \ {\n        val n = nums.size\n        val dp = IntArray(n + 1)\n        dp[0]\
        \ = 1\n        for (i in 1..n) {\n            var maxVal = nums[i - 1]\n   \
        \         var minVal = nums[i - 1]\n            for (j in i - 1 downTo 0) {\n\
        \                maxVal = maxOf(maxVal, nums[j])\n                minVal = minOf(minVal,\
        \ nums[j])\n                if (maxVal - minVal <= k) {\n                  \
        \  dp[i] = (dp[i] + dp[j]) % 1000000007\n                }\n            }\n\
        \        }\n        return dp[n]\n    }\n}"
      dart: "class Solution {\n    int countPartitions(List<int> nums, int k) {\n  \
        \      int n = nums.length;\n        List<int> dp = List<int>.filled(n + 1,\
        \ 0);\n        dp[0] = 1;\n        for (int i = 1; i <= n; i++) {\n        \
        \    int maxVal = nums[i - 1];\n            int minVal = nums[i - 1];\n    \
        \        for (int j = i - 1; j >= 0; j--) {\n                maxVal = max(maxVal,\
        \ nums[j]);\n                minVal = min(minVal, nums[j]);\n              \
        \  if (maxVal - minVal <= k) {\n                    dp[i] = (dp[i] + dp[j])\
        \ % 1000000007;\n                }\n            }\n        }\n        return\
        \ dp[n];\n    }\n}"
      go: "func countPartitions(nums []int, k int) int {\n    n := len(nums)\n    dp\
        \ := make([]int, n+1)\n    dp[0] = 1\n    for i := 1; i <= n; i++ {\n      \
        \  maxVal := nums[i-1]\n        minVal := nums[i-1]\n        for j := i - 1;\
        \ j >= 0; j-- {\n            maxVal = max(maxVal, nums[j])\n            minVal\
        \ = min(minVal, nums[j])\n            if maxVal-minVal <= k {\n            \
        \    dp[i] = (dp[i] + dp[j]) % 1000000007\n            }\n        }\n    }\n\
        \    return dp[n]\n}\n\nfunc max(a, b int) int {\n    if a > b {\n        return\
        \ a\n    }\n    return b\n}\n\nfunc min(a, b int) int {\n    if a < b {\n  \
        \      return a\n    }\n    return b\n}"
      ruby: "class Solution\n    def count_partitions(nums, k)\n        n = nums.size\n\
        \        dp = Array.new(n + 1, 0)\n        dp[0] = 1\n        for i in 1..n\n\
        \            max_val = nums[i - 1]\n            min_val = nums[i - 1]\n    \
        \        for j in (i - 1).downto(0)\n                max_val = [max_val, nums[j]].max\n\
        \                min_val = [min_val, nums[j]].min\n                if max_val\
        \ - min_val <= k\n                    dp[i] = (dp[i] + dp[j]) % 1000000007\n\
        \                end\n            end\n        end\n        dp[n]\n    end\n\
        end"
      scala: "object Solution {\n    def countPartitions(nums: Array[Int], k: Int):\
        \ Int = {\n        val n = nums.length\n        val dp = Array.ofDim[Int](n\
        \ + 1)\n        dp(0) = 1\n        for (i <- 1 to n) {\n            var maxVal\
        \ = nums(i - 1)\n            var minVal = nums(i - 1)\n            for (j <-\
        \ i - 1 to 0 by -1) {\n                maxVal = maxVal.max(nums(j))\n      \
        \          minVal = minVal.min(nums(j))\n                if (maxVal - minVal\
        \ <= k) {\n                    dp(i) = (dp(i) + dp(j)) % 1000000007\n      \
        \          }\n            }\n        }\n        dp(n)\n    }\n}"
      rust: "struct Solution;\n\nimpl Solution {\n    pub fn count_partitions(nums:\
        \ Vec<i32>, k: i32) -> i32 {\n        let n = nums.len();\n        let mut dp:\
        \ Vec<i32> = vec![0; n + 1];\n        dp[0] = 1;\n        for i in 1..=n {\n\
        \            let mut max_val = nums[i - 1];\n            let mut min_val = nums[i\
        \ - 1];\n            for j in (0..i).rev() {\n                max_val = max_val.max(nums[j]);\n\
        \                min_val = min_val.min(nums[j]);\n                if max_val\
        \ - min_val <= k {\n                    dp[i] = (dp[i] + dp[j]) % 1000000007;\n\
        \                }\n            }\n        }\n        dp[n]\n    }\n}"
      racket: "(define (count-partitions nums k)\n    (let ((n (length nums))\n    \
        \      (dp (make-vector (add1 n) 0)))\n        (vector-set! dp 0 1)\n      \
        \  (for ((i (range 1 (add1 n))))\n            (let ((max-val (list-ref nums\
        \ (sub1 i)))\n                  (min-val (list-ref nums (sub1 i))))\n      \
        \          (for ((j (range (sub1 i) -1 -1)))\n                    (set! max-val\
        \ (max max-val (list-ref nums j)))\n                    (set! min-val (min min-val\
        \ (list-ref nums j)))\n                    (when (<= (- max-val min-val) k)\n\
        \                        (set! (vector-ref dp i) (+ (vector-ref dp i) (vector-ref\
        \ dp j)))\n                        (set! (vector-ref dp i) (modulo (vector-ref\
        \ dp i) 1000000007))))))\n        (vector-ref dp n)))"
      erlang: "count_partitions(Nums, K) ->\n    count_partitions(Nums, K, length(Nums),\
        \ 0, []).\n\ncount_partitions([H|T], K, N, I, DP) when I < N ->\n    Max = H,\n\
        \    Min = H,\n    count_partitions(T, K, N, I + 1, [DP|[(fun() ->\n       \
        \ lists:foldl(fun(J, Acc) ->\n            Max1 = max(Max, lists:nth(J, [H|T])),\n\
        \            Min1 = min(Min, lists:nth(J, [H|T])),\n            if Max1 - Min1\
        \ =< K -> Acc + lists:nth(J, DP);\n            true -> Acc\n        end, 0,\
        \ lists:seq(0, I - 1)))()]]);\n\ncount_partitions([], _, _, _, DP) ->\n    lists:nth(length(DP)\
        \ - 1, DP)."
      elixir: "defmodule Solution do\n    def count_partitions(nums, k) do\n       \
        \ n = length(nums)\n        dp = Array.new(n + 1, 0)\n        dp\n        |>\
        \ Array.put(0, 1)\n        |> count_partitions(nums, k, 1, n)\n        |> Array.get(n)\n\
        \    end\n\n    defp count_partitions(dp, nums, k, i, n) when i <= n do\n  \
        \      max_val = Enum.at(nums, i - 1)\n        min_val = Enum.at(nums, i - 1)\n\
        \        dp\n        |> count_partitions(dp, nums, k, i - 1, max_val, min_val)\n\
        \        |> Array.put(i, dp\n                      |> Array.get(i) +\n     \
        \                 (if max_val - min_val <= k do\n                          \
        \ Array.get(dp, i - 1)\n                       else\n                      \
        \     0\n                       end))\n        |> count_partitions(nums, k,\
        \ i + 1, n)\n    end\n\n    defp count_partitions(dp, _, _, _, _) do\n     \
        \   dp\n    end\n\n    defp count_partitions(dp, nums, k, i, max_val, min_val)\
        \ when i >= 0 do\n        max_val1 = max(max_val, Enum.at(nums, i))\n      \
        \  min_val1 = min(min_val, Enum.at(nums, i))\n        if max_val1 - min_val1\
        \ <= k do\n            dp\n            |> Array.put(i, Array.get(dp, i) + Array.get(dp,\
        \ i - 1))\n            |> count_partitions(nums, k, i - 1, max_val1, min_val1)\n\
        \        else\n            dp\n            |> count_partitions(nums, k, i -\
        \ 1, max_val1, min_val1)\n        end\n    end\n\n    defp count_partitions(dp,\
        \ _, _, -1, _, _) do\n        dp\n    end\nend"
    approach: The problem can be solved using dynamic programming. We can define a dynamic
      programming array dp where dp[i] represents the number of ways to partition the
      array up to index i. We can then iterate over the array and for each index, we
      can try to extend the current partition by including the current element. If the
      difference between the maximum and minimum elements in the current partition is
      less than or equal to k, we can update dp[i] accordingly. The key intuition here
      is to use a sliding window approach to track the minimum and maximum elements
      in the current partition. This allows us to efficiently calculate the difference
      between the maximum and minimum elements in the current partition.
    time_complexity: The time complexity of the solution is O(n^2) where n is the length
      of the input array. This is because we are using a nested loop to iterate over
      the array and calculate the number of ways to partition the array up to each index.
    space_complexity: The space complexity of the solution is O(n) where n is the length
      of the input array. This is because we are using a dynamic programming array of
      size n to store the number of ways to partition the array up to each index.
    elapsed_time: 9.70496940612793
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-06 01:04:23 '
---

## Problem #3578: Count Partitions With Max-Min Difference at Most K

**Difficulty:** Medium

**Topics:** Array, Dynamic Programming, Queue, Sliding Window, Prefix Sum, Monotonic Queue

## Problem Description

<p>You are given an integer array <code>nums</code> and an integer <code>k</code>. Your task is to partition <code>nums</code> into one or more <strong>non-empty</strong> contiguous segments such that in each segment, the difference between its <strong>maximum</strong> and <strong>minimum</strong> elements is <strong>at most</strong> <code>k</code>.</p>

<p>Return the total number of ways to partition <code>nums</code> under this condition.</p>

<p>Since the answer may be too large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [9,4,1,3,7], k = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<p>There are 6 valid partitions where the difference between the maximum and minimum elements in each segment is at most <code>k = 4</code>:</p>

<ul>
	<li><code>[[9], [4], [1], [3], [7]]</code></li>
	<li><code>[[9], [4], [1], [3, 7]]</code></li>
	<li><code>[[9], [4], [1, 3], [7]]</code></li>
	<li><code>[[9], [4, 1], [3], [7]]</code></li>
	<li><code>[[9], [4, 1], [3, 7]]</code></li>
	<li><code>[[9], [4, 1, 3], [7]]</code></li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,3,4], k = 0</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>There are 2 valid partitions that satisfy the given conditions:</p>

<ul>
	<li><code>[[3], [3], [4]]</code></li>
	<li><code>[[3, 3], [4]]</code></li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. Use dynamic programming.

2. Let `dp[idx]` be the count of ways to partition the array with the last partition ending at index `idx`.

3. Try using a sliding window; we can track the minimum and maximum in the window using deques.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-06 01:04:14 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks for the number of ways to partition an array `nums` into contiguous segments such that the difference between the maximum and minimum elements in each segment is at most `k`. This can be solved using dynamic programming. Let `dp[i]` be the number of ways to partition the prefix `nums[0...i-1]` according to the given conditions. The base case is `dp[0] = 1`, representing one way to partition an empty prefix. To compute `dp[i]`, we consider the last segment ending at `nums[i-1]`. This segment could start at any index `j` (where `0 <= j < i`) such that `nums[j...i-1]` is a valid segment (i.e., `max(nums[j...i-1]) - min(nums[j...i-1]) <= k`). If `nums[j...i-1]` is a valid segment, then we can add `dp[j]` to `dp[i]`. Thus, `dp[i] = sum(dp[j])` for all valid `j`s.

To efficiently find the valid `j`s and compute their sum, we use a sliding window approach combined with prefix sums. As we iterate `i` from `1` to `N` (where `N` is `nums.length`), we maintain a window `nums[left...i-1]` that represents the longest valid segment ending at `i-1`. We use two monotonic deques (one for minimums, one for maximums) to keep track of the min and max elements within this window in O(1) time. If `max(window) - min(window) > k`, we shrink the window from the `left` until the condition is met. Once the `left` pointer is established for `i`, all segments `nums[p...i-1]` where `p` is in `[left, i-1]` are valid. The sum `sum(dp[p])` for `p` from `left` to `i-1` can be calculated using a `prefix_sum_dp` array: `(prefix_sum_dp[i] - prefix_sum_dp[left] + MOD) % MOD`. The `prefix_sum_dp[x]` stores the sum `dp[0] + ... + dp[x-1]`. The final answer is `dp[N].`

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
    int countPartitions(std::vector<int>& nums, int k) {
        int n = nums.size();
        long long MOD = 1e9 + 7;

        std::vector<long long> dp(n + 1, 0);
        dp[0] = 1;

        std::vector<long long> prefix_sum_dp(n + 2, 0);
        prefix_sum_dp[0] = 0;
        prefix_sum_dp[1] = 1;

        std::deque<int> min_deque;
        std::deque<int> max_deque;

        int left = 0;

        for (int i = 1; i <= n; ++i) {
            int current_num_idx = i - 1;
            int current_num_val = nums[current_num_idx];

            while (!min_deque.empty() && nums[min_deque.back()] >= current_num_val) {
                min_deque.pop_back();
            }
            min_deque.push_back(current_num_idx);

            while (!max_deque.empty() && nums[max_deque.back()] <= current_num_val) {
                max_deque.pop_back();
            }
            max_deque.push_back(current_num_idx);

            while (nums[max_deque.front()] - nums[min_deque.front()] > k) {
                left++;
                if (min_deque.front() < left) {
                    min_deque.pop_front();
                }
                if (max_deque.front() < left) {
                    max_deque.pop_front();
                }
            }

            dp[i] = (prefix_sum_dp[i] - prefix_sum_dp[left] + MOD) % MOD;
            prefix_sum_dp[i+1] = (prefix_sum_dp[i] + dp[i]) % MOD;
        }

        return dp[n];
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int countPartitions(int[] nums, int k) {
        int n = nums.length;
        long MOD = 1_000_000_007;

        long[] dp = new long[n + 1];
        dp[0] = 1;

        long[] prefixSumDp = new long[n + 2];
        prefixSumDp[0] = 0;
        prefixSumDp[1] = 1;

        Deque<Integer> minDeque = new ArrayDeque<>();
        Deque<Integer> maxDeque = new ArrayDeque<>();

        int left = 0;

        for (int i = 1; i <= n; ++i) {
            int currentNumIdx = i - 1;
            int currentNumVal = nums[currentNumIdx];

            while (!minDeque.isEmpty() && nums[minDeque.peekLast()] >= currentNumVal) {
                minDeque.removeLast();
            }
            minDeque.addLast(currentNumIdx);

            while (!maxDeque.isEmpty() && nums[maxDeque.peekLast()] <= currentNumVal) {
                maxDeque.removeLast();
            }
            maxDeque.addLast(currentNumIdx);

            while (nums[maxDeque.peekFirst()] - nums[minDeque.peekFirst()] > k) {
                left++;
                if (minDeque.peekFirst() < left) {
                    minDeque.removeFirst();
                }
                if (maxDeque.peekFirst() < left) {
                    maxDeque.removeFirst();
                }
            }

            dp[i] = (prefixSumDp[i] - prefixSumDp[left] + MOD) % MOD;
            prefixSumDp[i+1] = (prefixSumDp[i] + dp[i]) % MOD;
        }

        return (int) dp[n];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import collections

class Solution:
    def countPartitions(self, nums: list[int], k: int) -> int:
        n = len(nums)
        MOD = 10**9 + 7

        dp = [0] * (n + 1)
        dp[0] = 1

        prefix_sum_dp = [0] * (n + 2)
        prefix_sum_dp[0] = 0
        prefix_sum_dp[1] = 1

        min_deque = collections.deque() # Stores indices of elements in increasing order of value
        max_deque = collections.deque() # Stores indices of elements in decreasing order of value

        left = 0 # Left pointer of the sliding window

        for i in range(1, n + 1):
            current_num_idx = i - 1
            current_num_val = nums[current_num_idx]

            # Maintain min_deque
            while min_deque and nums[min_deque[-1]] >= current_num_val:
                min_deque.pop()
            min_deque.append(current_num_idx)

            # Maintain max_deque
            while max_deque and nums[max_deque[-1]] <= current_num_val:
                max_deque.pop()
            max_deque.append(current_num_idx)

            # Shrink window from left if condition (max - min <= k) is violated
            while nums[max_deque[0]] - nums[min_deque[0]] > k:
                left += 1
                # Remove elements from deques if their indices are outside the current window [left...current_num_idx]
                if min_deque[0] < left:
                    min_deque.popleft()
                if max_deque[0] < left:
                    max_deque.popleft()

            # dp[i] = sum(dp[p] for p in [left, i-1])
            # This sum is (prefix_sum_dp[i] - prefix_sum_dp[left] + MOD) % MOD
            dp[i] = (prefix_sum_dp[i] - prefix_sum_dp[left] + MOD) % MOD

            # Update prefix_sum_dp for the next iteration
            prefix_sum_dp[i+1] = (prefix_sum_dp[i] + dp[i]) % MOD

        return dp[n]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import collections

class Solution:
    def countPartitions(self, nums: list[int], k: int) -> int:
        n = len(nums)
        MOD = 10**9 + 7

        dp = [0] * (n + 1)
        dp[0] = 1

        prefix_sum_dp = [0] * (n + 2)
        prefix_sum_dp[0] = 0
        prefix_sum_dp[1] = 1

        min_deque = collections.deque() # Stores indices of elements in increasing order of value
        max_deque = collections.deque() # Stores indices of elements in decreasing order of value

        left = 0 # Left pointer of the sliding window

        for i in range(1, n + 1):
            current_num_idx = i - 1
            current_num_val = nums[current_num_idx]

            # Maintain min_deque
            while min_deque and nums[min_deque[-1]] >= current_num_val:
                min_deque.pop()
            min_deque.append(current_num_idx)

            # Maintain max_deque
            while max_deque and nums[max_deque[-1]] <= current_num_val:
                max_deque.pop()
            max_deque.append(current_num_idx)

            # Shrink window from left if condition (max - min <= k) is violated
            while nums[max_deque[0]] - nums[min_deque[0]] > k:
                left += 1
                # Remove elements from deques if their indices are outside the current window [left...current_num_idx]
                if min_deque[0] < left:
                    min_deque.popleft()
                if max_deque[0] < left:
                    max_deque.popleft()

            # dp[i] = sum(dp[p] for p in [left, i-1])
            # This sum is (prefix_sum_dp[i] - prefix_sum_dp[left] + MOD) % MOD
            dp[i] = (prefix_sum_dp[i] - prefix_sum_dp[left] + MOD) % MOD

            # Update prefix_sum_dp for the next iteration
            prefix_sum_dp[i+1] = (prefix_sum_dp[i] + dp[i]) % MOD

        return dp[n]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

// A simple deque implementation for integers (indices)
typedef struct {
    int* arr;
    int front;
    int rear;
    int capacity;
    int size;
} Deque;

Deque* createDeque(int capacity) {
    Deque* deque = (Deque*)malloc(sizeof(Deque));
    deque->capacity = capacity;
    deque->arr = (int*)malloc(capacity * sizeof(int));
    deque->front = 0;
    deque->rear = -1;
    deque->size = 0;
    return deque;
}

void freeDeque(Deque* deque) {
    free(deque->arr);
    free(deque);
}

bool isEmpty(Deque* deque) {
    return deque->size == 0;
}

void addLast(Deque* deque, int item) {
    if (deque->size == deque->capacity) return; // Should not happen with proper capacity
    deque->rear = (deque->rear + 1) % deque->capacity;
    deque->arr[deque->rear] = item;
    deque->size++;
}

int removeLast(Deque* deque) {
    if (isEmpty(deque)) return -1; // Error or sentinel
    int item = deque->arr[deque->rear];
    deque->rear = (deque->rear - 1 + deque->capacity) % deque->capacity;
    deque->size--;
    return item;
}

int peekLast(Deque* deque) {
    if (isEmpty(deque)) return -1; // Error or sentinel
    return deque->arr[deque->rear];
}

void addFirst(Deque* deque, int item) {
    if (deque->size == deque->capacity) return; // Should not happen
    deque->front = (deque->front - 1 + deque->capacity) % deque->capacity;
    deque->arr[deque->front] = item;
    deque->size++;
}

int removeFirst(Deque* deque) {
    if (isEmpty(deque)) return -1; // Error or sentinel
    int item = deque->arr[deque->front];
    deque->front = (deque->front + 1) % deque->capacity;
    deque->size--;
    return item;
}

int peekFirst(Deque* deque) {
    if (isEmpty(deque)) return -1; // Error or sentinel
    return deque->arr[deque->front];
}

long long countPartitions(int* nums, int numsSize, int k) {
    int n = numsSize;
    long long MOD = 1e9 + 7;

    long long* dp = (long long*)calloc(n + 1, sizeof(long long));
    dp[0] = 1;

    long long* prefix_sum_dp = (long long*)calloc(n + 2, sizeof(long long));
    prefix_sum_dp[0] = 0;
    prefix_sum_dp[1] = 1;

    Deque* min_deque = createDeque(n);
    Deque* max_deque = createDeque(n);

    int left = 0;

    for (int i = 1; i <= n; ++i) {
        int current_num_idx = i - 1;
        int current_num_val = nums[current_num_idx];

        while (!isEmpty(min_deque) && nums[peekLast(min_deque)] >= current_num_val) {
            removeLast(min_deque);
        }
        addLast(min_deque, current_num_idx);

        while (!isEmpty(max_deque) && nums[peekLast(max_deque)] <= current_num_val) {
            removeLast(max_deque);
        }
        addLast(max_deque, current_num_idx);

        while (nums[peekFirst(max_deque)] - nums[peekFirst(min_deque)] > k) {
            left++;
            if (peekFirst(min_deque) < left) {
                removeFirst(min_deque);
            }
            if (peekFirst(max_deque) < left) {
                removeFirst(max_deque);
            }
        }

        dp[i] = (prefix_sum_dp[i] - prefix_sum_dp[left] + MOD) % MOD;
        prefix_sum_dp[i+1] = (prefix_sum_dp[i] + dp[i]) % MOD;
    }

    long long result = dp[n];

    free(dp);
    free(prefix_sum_dp);
    freeDeque(min_deque);
    freeDeque(max_deque);

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
    public int CountPartitions(int[] nums, int k) {
        int n = nums.Length;
        long MOD = 1_000_000_007;

        long[] dp = new long[n + 1];
        dp[0] = 1;

        long[] prefixSumDp = new long[n + 2];
        prefixSumDp[0] = 0;
        prefixSumDp[1] = 1;

        LinkedList<int> minDeque = new LinkedList<int>(); // Stores indices of elements in increasing order of value
        LinkedList<int> maxDeque = new LinkedList<int>(); // Stores indices of elements in decreasing order of value

        int left = 0; // Left pointer of the sliding window

        for (int i = 1; i <= n; ++i) {
            int currentNumIdx = i - 1;
            int currentNumVal = nums[currentNumIdx];

            // Maintain minDeque
            while (minDeque.Count > 0 && nums[minDeque.Last.Value] >= currentNumVal) {
                minDeque.RemoveLast();
            }
            minDeque.AddLast(currentNumIdx);

            // Maintain maxDeque
            while (maxDeque.Count > 0 && nums[maxDeque.Last.Value] <= currentNumVal) {
                maxDeque.RemoveLast();
            }
            maxDeque.AddLast(currentNumIdx);

            // Shrink window from left if condition (max - min <= k) is violated
            while (nums[maxDeque.First.Value] - nums[minDeque.First.Value] > k) {
                left++;
                // Remove elements from deques if their indices are outside the current window [left...currentNumIdx]
                if (minDeque.First.Value < left) {
                    minDeque.RemoveFirst();
                }
                if (maxDeque.First.Value < left) {
                    maxDeque.RemoveFirst();
                }
            }

            // dp[i] = sum(dp[p] for p in [left, i-1])
            // This sum is (prefixSumDp[i] - prefixSumDp[left] + MOD) % MOD
            dp[i] = (prefixSumDp[i] - prefixSumDp[left] + MOD) % MOD;

            // Update prefixSumDp for the next iteration
            prefixSumDp[i+1] = (prefixSumDp[i] + dp[i]) % MOD;
        }

        return (int)dp[n];
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
var countPartitions = function(nums, k) {
    const n = nums.length;
    const MOD = 10**9 + 7;

    const dp = new Array(n + 1).fill(0);
    dp[0] = 1;

    const prefixSumDp = new Array(n + 2).fill(0);
    prefixSumDp[0] = 0;
    prefixSumDp[1] = 1;

    const minDeque = []; // Stores indices of elements in increasing order of value
    const maxDeque = []; // Stores indices of elements in decreasing order of value

    let left = 0; // Left pointer of the sliding window

    for (let i = 1; i <= n; ++i) {
        const currentNumIdx = i - 1;
        const currentNumVal = nums[currentNumIdx];

        // Maintain minDeque
        while (minDeque.length > 0 && nums[minDeque[minDeque.length - 1]] >= currentNumVal) {
            minDeque.pop();
        }
        minDeque.push(currentNumIdx);

        // Maintain maxDeque
        while (maxDeque.length > 0 && nums[maxDeque[maxDeque.length - 1]] <= currentNumVal) {
            maxDeque.pop();
        }
        maxDeque.push(currentNumIdx);

        // Shrink window from left if condition (max - min <= k) is violated
        while (nums[maxDeque[0]] - nums[minDeque[0]] > k) {
            left++;
            // Remove elements from deques if their indices are outside the current window [left...currentNumIdx]
            if (minDeque[0] < left) {
                minDeque.shift();
            }
            if (maxDeque[0] < left) {
                maxDeque.shift();
            }
        }

        // dp[i] = sum(dp[p] for p in [left, i-1])
        // This sum is (prefixSumDp[i] - prefixSumDp[left] + MOD) % MOD
        dp[i] = (prefixSumDp[i] - prefixSumDp[left] + MOD) % MOD;

        // Update prefixSumDp for the next iteration
        prefixSumDp[i+1] = (prefixSumDp[i] + dp[i]) % MOD;
    }

    return dp[n];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countPartitions(nums: number[], k: number): number {
    const n = nums.length;
    const MOD = 10**9 + 7;

    const dp: number[] = new Array(n + 1).fill(0);
    dp[0] = 1;

    const prefixSumDp: number[] = new Array(n + 2).fill(0);
    prefixSumDp[0] = 0;
    prefixSumDp[1] = 1;

    const minDeque: number[] = []; // Stores indices of elements in increasing order of value
    const maxDeque: number[] = []; // Stores indices of elements in decreasing order of value

    let left = 0; // Left pointer of the sliding window

    for (let i = 1; i <= n; ++i) {
        const currentNumIdx = i - 1;
        const currentNumVal = nums[currentNumIdx];

        // Maintain minDeque
        while (minDeque.length > 0 && nums[minDeque[minDeque.length - 1]] >= currentNumVal) {
            minDeque.pop();
        }
        minDeque.push(currentNumIdx);

        // Maintain maxDeque
        while (maxDeque.length > 0 && nums[maxDeque[maxDeque.length - 1]] <= currentNumVal) {
            maxDeque.pop();
        }
        maxDeque.push(currentNumIdx);

        // Shrink window from left if condition (max - min <= k) is violated
        while (nums[maxDeque[0]] - nums[minDeque[0]] > k) {
            left++;
            // Remove elements from deques if their indices are outside the current window [left...currentNumIdx]
            if (minDeque[0] < left) {
                minDeque.shift();
            }
            if (maxDeque[0] < left) {
                maxDeque.shift();
            }
        }

        // dp[i] = sum(dp[p] for p in [left, i-1])
        // This sum is (prefixSumDp[i] - prefixSumDp[left] + MOD) % MOD
        dp[i] = (prefixSumDp[i] - prefixSumDp[left] + MOD) % MOD;

        // Update prefixSumDp for the next iteration
        prefixSumDp[i+1] = (prefixSumDp[i] + dp[i]) % MOD;
    }

    return dp[n];
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
     * @param Integer $k
     * @return Integer
     */
    function countPartitions($nums, $k) {
        $n = count($nums);
        $MOD = 10**9 + 7;

        $dp = array_fill(0, $n + 1, 0);
        $dp[0] = 1;

        $prefixSumDp = array_fill(0, $n + 2, 0);
        $prefixSumDp[0] = 0;
        $prefixSumDp[1] = 1;

        $minDeque = new SplDoublyLinkedList(); // Stores indices of elements in increasing order of value
        $maxDeque = new SplDoublyLinkedList(); // Stores indices of elements in decreasing order of value

        $left = 0; // Left pointer of the sliding window

        for ($i = 1; $i <= $n; ++$i) {
            $currentNumIdx = $i - 1;
            $currentNumVal = $nums[$currentNumIdx];

            // Maintain minDeque
            while (!$minDeque->isEmpty() && $nums[$minDeque->bottom()] >= $currentNumVal) {
                $minDeque->pop();
            }
            $minDeque->push($currentNumIdx);

            // Maintain maxDeque
            while (!$maxDeque->isEmpty() && $nums[$maxDeque->bottom()] <= $currentNumVal) {
                $maxDeque->pop();
            }
            $maxDeque->push($currentNumIdx);

            // Shrink window from left if condition (max - min <= k) is violated
            while ($nums[$maxDeque->top()] - $nums[$minDeque->top()] > $k) {
                $left++;
                // Remove elements from deques if their indices are outside the current window [left...currentNumIdx]
                if ($minDeque->top() < $left) {
                    $minDeque->shift();
                }
                if ($maxDeque->top() < $left) {
                    $maxDeque->shift();
                }
            }

            // dp[i] = sum(dp[p] for p in [left, i-1])
            // This sum is (prefixSumDp[i] - prefixSumDp[left] + MOD) % MOD
            $dp[$i] = ($prefixSumDp[$i] - $prefixSumDp[$left] + $MOD) % $MOD;

            // Update prefixSumDp for the next iteration
            $prefixSumDp[$i+1] = ($prefixSumDp[$i] + $dp[$i]) % $MOD;
        }

        return $dp[$n];
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
    func countPartitions(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        let MOD = 1_000_000_007

        var dp = [Int](repeating: 0, count: n + 1)
        dp[0] = 1

        var prefixSumDp = [Int](repeating: 0, count: n + 2)
        prefixSumDp[0] = 0
        prefixSumDp[1] = 1

        var minDeque = [Int]() // Stores indices of elements in increasing order of value
        var maxDeque = [Int]() // Stores indices of elements in decreasing order of value

        var left = 0 // Left pointer of the sliding window

        for i in 1...n {
            let currentNumIdx = i - 1
            let currentNumVal = nums[currentNumIdx]

            // Maintain minDeque
            while !minDeque.isEmpty && nums[minDeque.last!] >= currentNumVal {
                minDeque.removeLast()
            }
            minDeque.append(currentNumIdx)

            // Maintain maxDeque
            while !maxDeque.isEmpty && nums[maxDeque.last!] <= currentNumVal {
                maxDeque.removeLast()
            }
            maxDeque.append(currentNumIdx)

            // Shrink window from left if condition (max - min <= k) is violated
            while nums[maxDeque.first!] - nums[minDeque.first!] > k {
                left += 1
                // Remove elements from deques if their indices are outside the current window [left...currentNumIdx]
                if minDeque.first! < left {
                    minDeque.removeFirst()
                }
                if maxDeque.first! < left {
                    maxDeque.removeFirst()
                }
            }

            // dp[i] = sum(dp[p] for p in [left, i-1])
            // This sum is (prefixSumDp[i] - prefixSumDp[left] + MOD) % MOD
            dp[i] = (prefixSumDp[i] - prefixSumDp[left] + MOD) % MOD

            // Update prefixSumDp for the next iteration
            prefixSumDp[i+1] = (prefixSumDp[i] + dp[i]) % MOD
        }

        return dp[n]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import java.util.ArrayDeque

class Solution {
    fun countPartitions(nums: IntArray, k: Int): Int {
        val n = nums.size
        val MOD = 1_000_000_007L

        val dp = LongArray(n + 1) { 0L }
        dp[0] = 1L

        val prefixSumDp = LongArray(n + 2) { 0L }
        prefixSumDp[0] = 0L
        prefixSumDp[1] = 1L

        val minDeque = ArrayDeque<Int>() // Stores indices of elements in increasing order of value
        val maxDeque = ArrayDeque<Int>() // Stores indices of elements in decreasing order of value

        var left = 0 // Left pointer of the sliding window

        for (i in 1..n) {
            val currentNumIdx = i - 1
            val currentNumVal = nums[currentNumIdx]

            // Maintain minDeque
            while (minDeque.isNotEmpty() && nums[minDeque.last()] >= currentNumVal) {
                minDeque.removeLast()
            }
            minDeque.addLast(currentNumIdx)

            // Maintain maxDeque
            while (maxDeque.isNotEmpty() && nums[maxDeque.last()] <= currentNumVal) {
                maxDeque.removeLast()
            }
            maxDeque.addLast(currentNumIdx)

            // Shrink window from left if condition (max - min <= k) is violated
            while (nums[maxDeque.first()] - nums[minDeque.first()] > k) {
                left++
                // Remove elements from deques if their indices are outside the current window [left...currentNumIdx]
                if (minDeque.first() < left) {
                    minDeque.removeFirst()
                }
                if (maxDeque.first() < left) {
                    maxDeque.removeFirst()
                }
            }

            // dp[i] = sum(dp[p] for p in [left, i-1])
            // This sum is (prefixSumDp[i] - prefixSumDp[left] + MOD) % MOD
            dp[i] = (prefixSumDp[i] - prefixSumDp[left] + MOD) % MOD

            // Update prefixSumDp for the next iteration
            prefixSumDp[i+1] = (prefixSumDp[i] + dp[i]) % MOD
        }

        return dp[n].toInt()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:collection';

class Solution {
  int countPartitions(List<int> nums, int k) {
    final n = nums.length;
    final MOD = 1000000007;

    final dp = List<int>.filled(n + 1, 0);
    dp[0] = 1;

    final prefixSumDp = List<int>.filled(n + 2, 0);
    prefixSumDp[0] = 0;
    prefixSumDp[1] = 1;

    final minDeque = DoubleLinkedQueue<int>(); // Stores indices of elements in increasing order of value
    final maxDeque = DoubleLinkedQueue<int>(); // Stores indices of elements in decreasing order of value

    var left = 0; // Left pointer of the sliding window

    for (var i = 1; i <= n; ++i) {
      final currentNumIdx = i - 1;
      final currentNumVal = nums[currentNumIdx];

      // Maintain minDeque
      while (minDeque.isNotEmpty && nums[minDeque.last] >= currentNumVal) {
        minDeque.removeLast();
      }
      minDeque.addLast(currentNumIdx);

      // Maintain maxDeque
      while (maxDeque.isNotEmpty && nums[maxDeque.last] <= currentNumVal) {
        maxDeque.removeLast();
      }
      maxDeque.addLast(currentNumIdx);

      // Shrink window from left if condition (max - min <= k) is violated
      while (nums[maxDeque.first] - nums[minDeque.first] > k) {
        left++;
        // Remove elements from deques if their indices are outside the current window [left...currentNumIdx]
        if (minDeque.first < left) {
          minDeque.removeFirst();
        }
        if (maxDeque.first < left) {
          maxDeque.removeFirst();
        }
      }

      // dp[i] = sum(dp[p] for p in [left, i-1])
      // This sum is (prefixSumDp[i] - prefixSumDp[left] + MOD) % MOD
      dp[i] = (prefixSumDp[i] - prefixSumDp[left] + MOD) % MOD;

      // Update prefixSumDp for the next iteration
      prefixSumDp[i+1] = (prefixSumDp[i] + dp[i]) % MOD;
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
package main

import (
	"container/list"
)

// Solution struct for the problem
type Solution struct{}

func (s *Solution) countPartitions(nums []int, k int) int {
    n := len(nums)
    MOD := 1_000_000_007

    dp := make([]int, n + 1)
    dp[0] = 1

    prefixSumDp := make([]int, n + 2)
    prefixSumDp[0] = 0
    prefixSumDp[1] = 1

    minDeque := list.New() // Stores indices of elements in increasing order of value
    maxDeque := list.New() // Stores indices of elements in decreasing order of value

    left := 0 // Left pointer of the sliding window

    for i := 1; i <= n; i++ {
        currentNumIdx := i - 1
        currentNumVal := nums[currentNumIdx]

        // Maintain minDeque
        for minDeque.Len() > 0 && nums[minDeque.Back().Value.(int)] >= currentNumVal {
            minDeque.Remove(minDeque.Back())
        }
        minDeque.PushBack(currentNumIdx)

        // Maintain maxDeque
        for maxDeque.Len() > 0 && nums[maxDeque.Back().Value.(int)] <= currentNumVal {
            maxDeque.Remove(maxDeque.Back())
        }
        maxDeque.PushBack(currentNumIdx)

        // Shrink window from left if condition (max - min <= k) is violated
        for nums[maxDeque.Front().Value.(int)] - nums[minDeque.Front().Value.(int)] > k {
            left++
            // Remove elements from deques if their indices are outside the current window [left...currentNumIdx]
            if minDeque.Front().Value.(int) < left {
                minDeque.Remove(minDeque.Front())
            }
            if maxDeque.Front().Value.(int) < left {
                maxDeque.Remove(maxDeque.Front())
            }
        }

        // dp[i] = sum(dp[p] for p in [left, i-1])
        // This sum is (prefixSumDp[i] - prefixSumDp[left] + MOD) % MOD
        dp[i] = (prefixSumDp[i] - prefixSumDp[left] + MOD) % MOD

        // Update prefixSumDp for the next iteration
        prefixSumDp[i+1] = (prefixSumDp[i] + dp[i]) % MOD
    }

    return dp[n]
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
    def count_partitions(nums, k)
        n = nums.length
        mod = 10**9 + 7

        dp = Array.new(n + 1, 0)
        dp[0] = 1

        prefix_sum_dp = Array.new(n + 2, 0)
        prefix_sum_dp[0] = 0
        prefix_sum_dp[1] = 1

        min_deque = [] # Stores indices of elements in increasing order of value
        max_deque = [] # Stores indices of elements in decreasing order of value

        left = 0 # Left pointer of the sliding window

        (1..n).each do |i|
            current_num_idx = i - 1
            current_num_val = nums[current_num_idx]

            # Maintain min_deque
            while !min_deque.empty? && nums[min_deque.last] >= current_num_val
                min_deque.pop
            end
            min_deque.push(current_num_idx)

            # Maintain max_deque
            while !max_deque.empty? && nums[max_deque.last] <= current_num_val
                max_deque.pop
            end
            max_deque.push(current_num_idx)

            # Shrink window from left if condition (max - min <= k) is violated
            while nums[max_deque.first] - nums[min_deque.first] > k
                left += 1
                # Remove elements from deques if their indices are outside the current window [left...current_num_idx]
                min_deque.shift if min_deque.first < left
                max_deque.shift if max_deque.first < left
            end

            # dp[i] = sum(dp[p] for p in [left, i-1])
            # This sum is (prefix_sum_dp[i] - prefix_sum_dp[left] + MOD) % MOD
            dp[i] = (prefix_sum_dp[i] - prefix_sum_dp[left] + mod) % mod

            # Update prefix_sum_dp for the next iteration
            prefix_sum_dp[i+1] = (prefix_sum_dp[i] + dp[i]) % mod
        end

        dp[n]
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
    def countPartitions(nums: Array[Int], k: Int): Int = {
        val n = nums.length
        val MOD = 1_000_000_007L

        val dp = Array.fill(n + 1)(0L)
        dp(0) = 1L

        val prefixSumDp = Array.fill(n + 2)(0L)
        prefixSumDp(0) = 0L
        prefixSumDp(1) = 1L

        val minDeque = mutable.ArrayDeque[Int]() // Stores indices of elements in increasing order of value
        val maxDeque = mutable.ArrayDeque[Int]() // Stores indices of elements in decreasing order of value

        var left = 0 // Left pointer of the sliding window

        for (i <- 1 to n) {
            val currentNumIdx = i - 1
            val currentNumVal = nums(currentNumIdx)

            // Maintain minDeque
            while (minDeque.nonEmpty && nums(minDeque.last) >= currentNumVal) {
                minDeque.removeLast()
            }
            minDeque.addLast(currentNumIdx)

            // Maintain maxDeque
            while (maxDeque.nonEmpty && nums(maxDeque.last) <= currentNumVal) {
                maxDeque.removeLast()
            }
            maxDeque.addLast(currentNumIdx)

            // Shrink window from left if condition (max - min <= k) is violated
            while (nums(maxDeque.head) - nums(minDeque.head) > k) {
                left += 1
                // Remove elements from deques if their indices are outside the current window [left...currentNumIdx]
                if (minDeque.head < left) {
                    minDeque.removeHead()
                }
                if (maxDeque.head < left) {
                    maxDeque.removeHead()
                }
            }

            // dp(i) = sum(dp(p) for p in [left, i-1])
            // This sum is (prefixSumDp(i) - prefixSumDp(left) + MOD) % MOD
            dp(i) = (prefixSumDp(i) - prefixSumDp(left) + MOD) % MOD

            // Update prefixSumDp for the next iteration
            prefixSumDp(i+1) = (prefixSumDp(i) + dp(i)) % MOD
        }

        dp(n).toInt
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::VecDeque;

impl Solution {
    pub fn count_partitions(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let k_long = k as i64;
        let modular = 1_000_000_007;

        let mut dp = vec![0; n + 1];
        dp[0] = 1;

        let mut prefix_sum_dp = vec![0; n + 2];
        prefix_sum_dp[0] = 0;
        prefix_sum_dp[1] = 1;

        let mut min_deque: VecDeque<usize> = VecDeque::new(); // Stores indices of elements in increasing order of value
        let mut max_deque: VecDeque<usize> = VecDeque::new(); // Stores indices of elements in decreasing order of value

        let mut left = 0; // Left pointer of the sliding window

        for i in 1..=n {
            let current_num_idx = i - 1;
            let current_num_val = nums[current_num_idx];

            // Maintain min_deque
            while let Some(&last_idx) = min_deque.back() {
                if nums[last_idx] >= current_num_val {
                    min_deque.pop_back();
                } else {
                    break;
                }
            }
            min_deque.push_back(current_num_idx);

            // Maintain max_deque
            while let Some(&last_idx) = max_deque.back() {
                if nums[last_idx] <= current_num_val {
                    max_deque.pop_back();
                } else {
                    break;
                }
            }
            max_deque.push_back(current_num_idx);

            // Shrink window from left if condition (max - min <= k) is violated
            while (nums[*max_deque.front().unwrap()] as i64) - (nums[*min_deque.front().unwrap()] as i64) > k_long {
                left += 1;
                // Remove elements from deques if their indices are outside the current window [left...current_num_idx]
                if *min_deque.front().unwrap() < left {
                    min_deque.pop_front();
                }
                if *max_deque.front().unwrap() < left {
                    max_deque.pop_front();
                }
            }

            // dp[i] = sum(dp[p] for p in [left, i-1])
            // This sum is (prefix_sum_dp[i] - prefix_sum_dp[left] + MOD) % MOD
            dp[i] = (prefix_sum_dp[i] - prefix_sum_dp[left] + modular) % modular;

            // Update prefix_sum_dp for the next iteration
            prefix_sum_dp[i+1] = (prefix_sum_dp[i] + dp[i]) % modular;
        }

        dp[n] as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (count-partitions nums k)
  (define n (vector-length nums))
  (define MOD 1000000007)

  (define dp (make-vector (+ n 1) 0))
  (vector-set! dp 0 1)

  (define prefix-sum-dp (make-vector (+ n 2) 0))
  (vector-set! prefix-sum-dp 0 0)
  (vector-set! prefix-sum-dp 1 1)

  (define min-deque (make-deque)) ; Stores indices of elements in increasing order of value
  (define max-deque (make-deque)) ; Stores indices of elements in decreasing order of value

  (define left (box 0)) ; Left pointer of the sliding window

  (for ([i (in-range 1 (+ n 1))])
    (define current-num-idx (- i 1))
    (define current-num-val (vector-ref nums current-num-idx))

    ; Maintain min-deque
    (while (and (not (deque-empty? min-deque))
                (>= (vector-ref nums (deque-back min-deque)) current-num-val))
      (deque-pop-back! min-deque))
    (deque-push-back! min-num-idx)

    ; Maintain max-deque
    (while (and (not (deque-empty? max-deque))
                (<= (vector-ref nums (deque-back max-deque)) current-num-val))
      (deque-pop-back! max-deque))
    (deque-push-back! max-deque current-num-idx)

    ; Shrink window from left if condition (max - min <= k) is violated
    (while (> (- (vector-ref nums (deque-front max-deque))
                 (vector-ref nums (deque-front min-deque)))
              k)
      (set-box! left (+ (unbox left) 1))
      ; Remove elements from deques if their indices are outside the current window [left...current-num-idx]
      (when (< (deque-front min-deque) (unbox left))
        (deque-pop-front! min-deque))
      (when (< (deque-front max-deque) (unbox left))
        (deque-pop-front! max-deque)))

    ; dp[i] = sum(dp[p] for p in [left, i-1])
    ; This sum is (prefix-sum-dp[i] - prefix-sum-dp[left] + MOD) % MOD
    (vector-set! dp i
                 (modulo (+ (- (vector-ref prefix-sum-dp i)
                                (vector-ref prefix-sum-dp (unbox left)))
                            MOD)
                         MOD))

    ; Update prefix-sum-dp for the next iteration
    (vector-set! prefix-sum-dp (+ i 1)
                 (modulo (+ (vector-ref prefix-sum-dp i)
                            (vector-ref dp i))
                         MOD)))

  (vector-ref dp n))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([count_partitions/2]).

count_partitions(Nums, K) ->
    N = length(Nums),
    MOD = 1000000007,

    Dp = array:new([{size, N + 1}, {fixed, true}, {default, 0}]),
    Dp1 = array:set(0, 1, Dp),

    PrefixSumDp = array:new([{size, N + 2}, {fixed, true}, {default, 0}]),
    PrefixSumDp1 = array:set(0, 0, PrefixSumDp),
    PrefixSumDp2 = array:set(1, 1, PrefixSumDp1),

    MinDeque = queue:new(), % Stores indices of elements in increasing order of value
    MaxDeque = queue:new(), % Stores indices of elements in decreasing order of value

    Left = 0, % Left pointer of the sliding window

    count_partitions_loop(1, N, Nums, K, MOD, Dp1, PrefixSumDp2, MinDeque, MaxDeque, Left).

count_partitions_loop(I, N, Nums, K, MOD, Dp, PrefixSumDp, MinDeque, MaxDeque, Left) when I =< N ->
    CurrentNumIdx = I - 1,
    CurrentNumVal = lists:nth(CurrentNumIdx + 1, Nums),

    % Maintain MinDeque
    MinDeque1 = update_min_deque(MinDeque, Nums, CurrentNumIdx, CurrentNumVal),

    % Maintain MaxDeque
    MaxDeque1 = update_max_deque(MaxDeque, Nums, CurrentNumIdx, CurrentNumVal),

    % Shrink window from left if condition (max - min <= k) is violated
    {Left1, MinDeque2, MaxDeque2} = shrink_window(Left, Nums, K, MinDeque1, MaxDeque1),

    % Dp[I] = sum(Dp[P] for P in [Left1, I-1])
    % This sum is (PrefixSumDp[I] - PrefixSumDp[Left1] + MOD) % MOD
    DpI = (array:get(I, PrefixSumDp) - array:get(Left1, PrefixSumDp) + MOD) rem MOD,
    Dp3 = array:set(I, DpI, Dp),

    % Update PrefixSumDp for the next iteration
    PrefixSumDpIPlus1 = (array:get(I, PrefixSumDp) + DpI) rem MOD,
    PrefixSumDp3 = array:set(I + 1, PrefixSumDpIPlus1, PrefixSumDp),

    count_partitions_loop(I + 1, N, Nums, K, MOD, Dp3, PrefixSumDp3, MinDeque2, MaxDeque2, Left1);
count_partitions_loop(I, N, _Nums, _K, _MOD, Dp, _PrefixSumDp, _MinDeque, _MaxDeque, _Left) when I > N ->
    array:get(N, Dp).

update_min_deque(MinDeque, Nums, CurrentNumIdx, CurrentNumVal) ->
    case queue:is_empty(MinDeque) of
        true -> queue:in(CurrentNumIdx, MinDeque);
        false ->
            LastIdx = queue:last(MinDeque),
            case lists:nth(LastIdx + 1, Nums) >= CurrentNumVal of
                true -> update_min_deque(queue:del_last(MinDeque), Nums, CurrentNumIdx, CurrentNumVal);
                false -> queue:in(CurrentNumIdx, MinDeque)
            end
    end.

update_max_deque(MaxDeque, Nums, CurrentNumIdx, CurrentNumVal) ->
    case queue:is_empty(MaxDeque) of
        true -> queue:in(CurrentNumIdx, MaxDeque);
        false ->
            LastIdx = queue:last(MaxDeque),
            case lists:nth(LastIdx + 1, Nums) <= CurrentNumVal of
                true -> update_max_deque(queue:del_last(MaxDeque), Nums, CurrentNumIdx, CurrentNumVal);
                false -> queue:in(CurrentNumIdx, MaxDeque)
            end
    end.

shrink_window(Left, Nums, K, MinDeque, MaxDeque) ->
    MaxVal = lists:nth(queue:head(MaxDeque) + 1, Nums),
    MinVal = lists:nth(queue:head(MinDeque) + 1, Nums),
    case MaxVal - MinVal > K of
        true ->
            Left1 = Left + 1,
            MinDeque1 = case queue:head(MinDeque) < Left1 of
                            true -> queue:del_head(MinDeque);
                            false -> MinDeque
                        end,
            MaxDeque1 = case queue:head(MaxDeque) < Left1 of
                            true -> queue:del_head(MaxDeque);
                            false -> MaxDeque
                        end,
            shrink_window(Left1, Nums, K, MinDeque1, MaxDeque1);
        false ->
            {Left, MinDeque, MaxDeque}
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @moduledoc """Solution for Count Partitions With Max-Min Difference at Most K."""

  @spec count_partitions(nums :: [integer], k :: integer) :: integer
  def count_partitions(nums, k) do
    n = length(nums)
    mod = 1_000_000_007

    # dp[i] will store the number of ways to partition nums[0...i-1]
    # dp[0] = 1 represents one way to partition an empty prefix (base case)
    dp = :array.new([{size: n + 1, fixed: true, default: 0}])
    dp = :array.set(0, 1, dp)

    # prefix_sum_dp[i] will store (dp[0] + ... + dp[i-1]) % MOD
    # This allows calculating sum(dp[j] for j in [left, i-1]) as (prefix_sum_dp[i] - prefix_sum_dp[left] + MOD) % MOD
    prefix_sum_dp = :array.new([{size: n + 2, fixed: true, default: 0}])
    prefix_sum_dp = :array.set(0, 0, prefix_sum_dp)
    prefix_sum_dp = :array.set(1, 1, prefix_sum_dp)

    # Deques to maintain min and max in the current window [left...i-1]
    min_deque = :queue.new() # Stores indices of elements in increasing order of value
    max_deque = :queue.new() # Stores indices of elements in decreasing order of value

    left = 0 # Left pointer of the sliding window

    # Elixir's for loop is a comprehension, not suitable for mutable state like this.
    # Using a recursive helper function to simulate the loop.
    loop_partitions(1, n, nums, k, mod, dp, prefix_sum_dp, min_deque, max_deque, left)
  end

  defp loop_partitions(i, n, nums, k, mod, dp, prefix_sum_dp, min_deque, max_deque, left) when i <= n do
    current_num_idx = i - 1
    current_num_val = Enum.at(nums, current_num_idx)

    # Maintain min_deque
    min_deque = update_min_deque(min_deque, nums, current_num_idx, current_num_val)

    # Maintain max_deque
    max_deque = update_max_deque(max_deque, nums, current_num_idx, current_num_val)

    # Shrink window from left if condition (max - min <= k) is violated
    {left, min_deque, max_deque} = shrink_window(left, nums, k, min_deque, max_deque)

    # dp[i] = sum(dp[p] for p in [left, i-1])
    # This sum is (prefix_sum_dp[i] - prefix_sum_dp[left] + MOD) % MOD
    dp_i = (:array.get(i, prefix_sum_dp) - :array.get(left, prefix_sum_dp) + mod) |> rem(mod)
    dp = :array.set(i, dp_i, dp)

    # Update prefix_sum_dp for the next iteration
    prefix_sum_dp_i_plus_1 = (:array.get(i, prefix_sum_dp) + dp_i) |> rem(mod)
    prefix_sum_dp = :array.set(i + 1, prefix_sum_dp_i_plus_1, prefix_sum_dp)

    loop_partitions(i + 1, n, nums, k, mod, dp, prefix_sum_dp, min_deque, max_deque, left)
  end

  defp loop_partitions(_i, n, _nums, _k, _mod, dp, _prefix_sum_dp, _min_deque, _max_deque, _left) do
    :array.get(n, dp)
  end

  defp update_min_deque(min_deque, nums, current_num_idx, current_num_val) do
    case :queue.is_empty(min_deque) do
      true -> :queue.in(current_num_idx, min_deque)
      false ->
        {_val, last_idx} = :queue.last(min_deque)
        if Enum.at(nums, last_idx) >= current_num_val do
          update_min_deque(:queue.del_last(min_deque), nums, current_num_idx, current_num_val)
        else
          :queue.in(current_num_idx, min_deque)
        end
    end
  end

  defp update_max_deque(max_deque, nums, current_num_idx, current_num_val) do
    case :queue.is_empty(max_deque) do
      true -> :queue.in(current_num_idx, max_deque)
      false ->
        {_val, last_idx} = :queue.last(max_deque)
        if Enum.at(nums, last_idx) <= current_num_val do
          update_max_deque(:queue.del_last(max_deque), nums, current_num_idx, current_num_val)
        else
          :queue.in(current_num_idx, max_deque)
        end
    end
  end

  defp shrink_window(left, nums, k, min_deque, max_deque) do
    {_val, max_idx} = :queue.head(max_deque)
    {_val, min_idx} = :queue.head(min_deque)
    max_val = Enum.at(nums, max_idx)
    min_val = Enum.at(nums, min_idx)

    if max_val - min_val > k do
      left_new = left + 1
      min_deque_new = if min_idx < left_new, do: :queue.del_head(min_deque), else: min_deque
      max_deque_new = if max_idx < left_new, do: :queue.del_head(max_deque), else: max_deque
      shrink_window(left_new, nums, k, min_deque_new, max_deque_new)
    else
      {left, min_deque, max_deque}
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N), where N is the length of the `nums` array. The main loop iterates N times (from `i = 1` to `N`). Inside the loop, each element is added to and removed from the monotonic deques at most once. The `left` pointer for the sliding window also moves forward at most N times in total. All operations within the loop (deque operations, arithmetic calculations) take O(1) time. Therefore, the overall time complexity is linear with respect to the input array size.

- **Space Complexity:** The space complexity is O(N). We use a `dp` array of size `N+1` and a `prefix_sum_dp` array of size `N+2` to store intermediate results. Additionally, two monotonic deques are used to efficiently track the minimum and maximum elements within the sliding window. In the worst case, each deque can store up to N indices. Thus, the total space required is proportional to N.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-06 01:04:23 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved using dynamic programming. We can define a dynamic programming array dp where dp[i] represents the number of ways to partition the array up to index i. We can then iterate over the array and for each index, we can try to extend the current partition by including the current element. If the difference between the maximum and minimum elements in the current partition is less than or equal to k, we can update dp[i] accordingly. The key intuition here is to use a sliding window approach to track the minimum and maximum elements in the current partition. This allows us to efficiently calculate the difference between the maximum and minimum elements in the current partition.

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
    int countPartitions(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> dp(n + 1, 0);
        dp[0] = 1;
        for (int i = 1; i <= n; i++) {
            int maxVal = nums[i - 1];
            int minVal = nums[i - 1];
            for (int j = i - 1; j >= 0; j--) {
                maxVal = max(maxVal, nums[j]);
                minVal = min(minVal, nums[j]);
                if (maxVal - minVal <= k) {
                    dp[i] = (dp[i] + dp[j]) % (1000000007);
                }
            }
        }
        return dp[n];
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int countPartitions(int[] nums, int k) {
        int n = nums.length;
        int[] dp = new int[n + 1];
        dp[0] = 1;
        for (int i = 1; i <= n; i++) {
            int maxVal = nums[i - 1];
            int minVal = nums[i - 1];
            for (int j = i - 1; j >= 0; j--) {
                maxVal = Math.max(maxVal, nums[j]);
                minVal = Math.min(minVal, nums[j]);
                if (maxVal - minVal <= k) {
                    dp[i] = (dp[i] + dp[j]) % 1000000007;
                }
            }
        }
        return dp[n];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def countPartitions(self, nums: list[int], k: int) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            max_val = nums[i - 1]
            min_val = nums[i - 1]
            for j in range(i - 1, -1, -1):
                max_val = max(max_val, nums[j])
                min_val = min(min_val, nums[j])
                if max_val - min_val <= k:
                    dp[i] = (dp[i] + dp[j]) % 1000000007
        return dp[n]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countPartitions(self, nums: list[int], k: int) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            max_val = nums[i - 1]
            min_val = nums[i - 1]
            for j in range(i - 1, -1, -1):
                max_val = max(max_val, nums[j])
                min_val = min(min_val, nums[j])
                if max_val - min_val <= k:
                    dp[i] = (dp[i] + dp[j]) % 1000000007
        return dp[n]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
typedef long long ll;

struct Solution {
    int countPartitions(int* nums, int numsSize, int k) {
        int* dp = (int*)malloc((numsSize + 1) * sizeof(int));
        dp[0] = 1;
        for (int i = 1; i <= numsSize; i++) {
            int maxVal = nums[i - 1];
            int minVal = nums[i - 1];
            for (int j = i - 1; j >= 0; j--) {
                maxVal = (maxVal > nums[j]) ? maxVal : nums[j];
                minVal = (minVal < nums[j]) ? minVal : nums[j];
                if (maxVal - minVal <= k) {
                    dp[i] = (dp[i] + dp[j]) % 1000000007;
                }
            }
        }
        int result = dp[numsSize];
        free(dp);
        return result;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int CountPartitions(int[] nums, int k) {
        int n = nums.Length;
        int[] dp = new int[n + 1];
        dp[0] = 1;
        for (int i = 1; i <= n; i++) {
            int maxVal = nums[i - 1];
            int minVal = nums[i - 1];
            for (int j = i - 1; j >= 0; j--) {
                maxVal = Math.Max(maxVal, nums[j]);
                minVal = Math.Min(minVal, nums[j]);
                if (maxVal - minVal <= k) {
                    dp[i] = (dp[i] + dp[j]) % 1000000007;
                }
            }
        }
        return dp[n];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var countPartitions = function(nums, k) {
    let n = nums.length;
    let dp = new Array(n + 1).fill(0);
    dp[0] = 1;
    for (let i = 1; i <= n; i++) {
        let maxVal = nums[i - 1];
        let minVal = nums[i - 1];
        for (let j = i - 1; j >= 0; j--) {
            maxVal = Math.max(maxVal, nums[j]);
            minVal = Math.min(minVal, nums[j]);
            if (maxVal - minVal <= k) {
                dp[i] = (dp[i] + dp[j]) % 1000000007;
            }
        }
    }
    return dp[n];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countPartitions(nums: number[], k: number): number {
    let n = nums.length;
    let dp: number[] = new Array(n + 1).fill(0);
    dp[0] = 1;
    for (let i = 1; i <= n; i++) {
        let maxVal = nums[i - 1];
        let minVal = nums[i - 1];
        for (let j = i - 1; j >= 0; j--) {
            maxVal = Math.max(maxVal, nums[j]);
            minVal = Math.min(minVal, nums[j]);
            if (maxVal - minVal <= k) {
                dp[i] = (dp[i] + dp[j]) % 1000000007;
            }
        }
    }
    return dp[n];
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function countPartitions($nums, $k) {
        $n = count($nums);
        $dp = array_fill(0, $n + 1, 0);
        $dp[0] = 1;
        for ($i = 1; $i <= $n; $i++) {
            $maxVal = $nums[$i - 1];
            $minVal = $nums[$i - 1];
            for ($j = $i - 1; $j >= 0; $j--) {
                $maxVal = max($maxVal, $nums[$j]);
                $minVal = min($minVal, $nums[$j]);
                if ($maxVal - $minVal <= $k) {
                    $dp[$i] = ($dp[$i] + $dp[$j]) % 1000000007;
                }
            }
        }
        return $dp[$n];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func countPartitions(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var dp = [Int](repeating: 0, count: n + 1)
        dp[0] = 1
        for i in 1...n {
            var maxVal = nums[i - 1]
            var minVal = nums[i - 1]
            for j in stride(from: i - 1, through: 0, by: -1) {
                maxVal = max(maxVal, nums[j])
                minVal = min(minVal, nums[j])
                if maxVal - minVal <= k {
                    dp[i] = (dp[i] + dp[j]) % 1000000007
                }
            }
        }
        return dp[n]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun countPartitions(nums: IntArray, k: Int): Int {
        val n = nums.size
        val dp = IntArray(n + 1)
        dp[0] = 1
        for (i in 1..n) {
            var maxVal = nums[i - 1]
            var minVal = nums[i - 1]
            for (j in i - 1 downTo 0) {
                maxVal = maxOf(maxVal, nums[j])
                minVal = minOf(minVal, nums[j])
                if (maxVal - minVal <= k) {
                    dp[i] = (dp[i] + dp[j]) % 1000000007
                }
            }
        }
        return dp[n]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int countPartitions(List<int> nums, int k) {
        int n = nums.length;
        List<int> dp = List<int>.filled(n + 1, 0);
        dp[0] = 1;
        for (int i = 1; i <= n; i++) {
            int maxVal = nums[i - 1];
            int minVal = nums[i - 1];
            for (int j = i - 1; j >= 0; j--) {
                maxVal = max(maxVal, nums[j]);
                minVal = min(minVal, nums[j]);
                if (maxVal - minVal <= k) {
                    dp[i] = (dp[i] + dp[j]) % 1000000007;
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
func countPartitions(nums []int, k int) int {
    n := len(nums)
    dp := make([]int, n+1)
    dp[0] = 1
    for i := 1; i <= n; i++ {
        maxVal := nums[i-1]
        minVal := nums[i-1]
        for j := i - 1; j >= 0; j-- {
            maxVal = max(maxVal, nums[j])
            minVal = min(minVal, nums[j])
            if maxVal-minVal <= k {
                dp[i] = (dp[i] + dp[j]) % 1000000007
            }
        }
    }
    return dp[n]
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func min(a, b int) int {
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
    def count_partitions(nums, k)
        n = nums.size
        dp = Array.new(n + 1, 0)
        dp[0] = 1
        for i in 1..n
            max_val = nums[i - 1]
            min_val = nums[i - 1]
            for j in (i - 1).downto(0)
                max_val = [max_val, nums[j]].max
                min_val = [min_val, nums[j]].min
                if max_val - min_val <= k
                    dp[i] = (dp[i] + dp[j]) % 1000000007
                end
            end
        end
        dp[n]
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def countPartitions(nums: Array[Int], k: Int): Int = {
        val n = nums.length
        val dp = Array.ofDim[Int](n + 1)
        dp(0) = 1
        for (i <- 1 to n) {
            var maxVal = nums(i - 1)
            var minVal = nums(i - 1)
            for (j <- i - 1 to 0 by -1) {
                maxVal = maxVal.max(nums(j))
                minVal = minVal.min(nums(j))
                if (maxVal - minVal <= k) {
                    dp(i) = (dp(i) + dp(j)) % 1000000007
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
struct Solution;

impl Solution {
    pub fn count_partitions(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let mut dp: Vec<i32> = vec![0; n + 1];
        dp[0] = 1;
        for i in 1..=n {
            let mut max_val = nums[i - 1];
            let mut min_val = nums[i - 1];
            for j in (0..i).rev() {
                max_val = max_val.max(nums[j]);
                min_val = min_val.min(nums[j]);
                if max_val - min_val <= k {
                    dp[i] = (dp[i] + dp[j]) % 1000000007;
                }
            }
        }
        dp[n]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define (count-partitions nums k)
    (let ((n (length nums))
          (dp (make-vector (add1 n) 0)))
        (vector-set! dp 0 1)
        (for ((i (range 1 (add1 n))))
            (let ((max-val (list-ref nums (sub1 i)))
                  (min-val (list-ref nums (sub1 i))))
                (for ((j (range (sub1 i) -1 -1)))
                    (set! max-val (max max-val (list-ref nums j)))
                    (set! min-val (min min-val (list-ref nums j)))
                    (when (<= (- max-val min-val) k)
                        (set! (vector-ref dp i) (+ (vector-ref dp i) (vector-ref dp j)))
                        (set! (vector-ref dp i) (modulo (vector-ref dp i) 1000000007))))))
        (vector-ref dp n)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
count_partitions(Nums, K) ->
    count_partitions(Nums, K, length(Nums), 0, []).

count_partitions([H|T], K, N, I, DP) when I < N ->
    Max = H,
    Min = H,
    count_partitions(T, K, N, I + 1, [DP|[(fun() ->
        lists:foldl(fun(J, Acc) ->
            Max1 = max(Max, lists:nth(J, [H|T])),
            Min1 = min(Min, lists:nth(J, [H|T])),
            if Max1 - Min1 =< K -> Acc + lists:nth(J, DP);
            true -> Acc
        end, 0, lists:seq(0, I - 1)))()]]);

count_partitions([], _, _, _, DP) ->
    lists:nth(length(DP) - 1, DP).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
    def count_partitions(nums, k) do
        n = length(nums)
        dp = Array.new(n + 1, 0)
        dp
        |> Array.put(0, 1)
        |> count_partitions(nums, k, 1, n)
        |> Array.get(n)
    end

    defp count_partitions(dp, nums, k, i, n) when i <= n do
        max_val = Enum.at(nums, i - 1)
        min_val = Enum.at(nums, i - 1)
        dp
        |> count_partitions(dp, nums, k, i - 1, max_val, min_val)
        |> Array.put(i, dp
                      |> Array.get(i) +
                      (if max_val - min_val <= k do
                           Array.get(dp, i - 1)
                       else
                           0
                       end))
        |> count_partitions(nums, k, i + 1, n)
    end

    defp count_partitions(dp, _, _, _, _) do
        dp
    end

    defp count_partitions(dp, nums, k, i, max_val, min_val) when i >= 0 do
        max_val1 = max(max_val, Enum.at(nums, i))
        min_val1 = min(min_val, Enum.at(nums, i))
        if max_val1 - min_val1 <= k do
            dp
            |> Array.put(i, Array.get(dp, i) + Array.get(dp, i - 1))
            |> count_partitions(nums, k, i - 1, max_val1, min_val1)
        else
            dp
            |> count_partitions(nums, k, i - 1, max_val1, min_val1)
        end
    end

    defp count_partitions(dp, _, _, -1, _, _) do
        dp
    end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of the solution is O(n^2) where n is the length of the input array. This is because we are using a nested loop to iterate over the array and calculate the number of ways to partition the array up to each index.

- **Space Complexity:** The space complexity of the solution is O(n) where n is the length of the input array. This is because we are using a dynamic programming array of size n to store the number of ways to partition the array up to each index.

</div>
</details>
