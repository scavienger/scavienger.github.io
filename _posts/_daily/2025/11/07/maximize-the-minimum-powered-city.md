---
layout: post
title: "Maximize the Minimum Powered City"
date: 2025-11-07 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Binary Search", "Greedy", "Queue", "Sliding Window", "Prefix Sum"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/maximize-the-minimum-powered-city/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\nbool check(long long target_power, int n, int\
        \ r, long long k, const std::vector<int>& stations) {\nstd::vector<long long>\
        \ diff_initial(n + 1, 0);\nstd::vector<long long> diff_for_new_stations(n +\
        \ 1, 0);\n\nfor (int i = 0; i < n; ++i) {\n    long long val = stations[i];\n\
        \    int start_idx = std::max(0, i - r);\n    int end_idx = std::min(n - 1,\
        \ i + r);\n\n    diff_initial[start_idx] += val;\n    if (end_idx + 1 < n +\
        \ 1) {\n        diff_initial[end_idx + 1] -= val;\n    }\n}\n\nlong long current_total_power_sum\
        \ = 0;\nlong long current_added_power_effect = 0;\nlong long added_k_count =\
        \ 0;\n\nfor (int i = 0; i < n; ++i) {\n    current_total_power_sum += diff_initial[i];\n\
        \    current_added_power_effect += diff_for_new_stations[i];\n\n    long long\
        \ total_power_at_i = current_total_power_sum + current_added_power_effect;\n\
        \n    if (total_power_at_i < target_power) {\n        long long needed = target_power\
        \ - total_power_at_i;\n        added_k_count += needed;\n\n        if (added_k_count\
        \ > k) {\n            return false;\n        }\n\n        diff_for_new_stations[i]\
        \ += needed;\n        int end_effect_idx = std::min(n - 1, i + 2 * r);\n   \
        \     if (end_effect_idx + 1 < n + 1) {\n            diff_for_new_stations[end_effect_idx\
        \ + 1] -= needed;\n        }\n\n        current_added_power_effect += needed;\n\
        \    }\n}\n\nreturn true;\n}\n\nlong long maxPower(std::vector<int>& stations,\
        \ int r, long long k) {\nint n = stations.size();\n\nlong long low = 0;\nlong\
        \ long high = 2LL * 10000000000LL + 1000000000LL; // Max initial power + max\
        \ k\nlong long ans = 0;\n\nwhile (low <= high) {\n    long long mid = low +\
        \ (high - low) / 2;\n    if (check(mid, n, r, k, stations)) {\n        ans =\
        \ mid;\n        low = mid + 1;\n    } else {\n        high = mid - 1;\n    }\n\
        }\n\nreturn ans;\n}\n};"
      java: "import java.util.List;\nimport java.util.ArrayList;\nimport java.util.Arrays;\n\
        \nclass Solution {\n    public long maxPower(int[] stations, int r, long k)\
        \ {\n        int n = stations.length;\n\n        long low = 0;\n        long\
        \ high = 2L * 10000000000L + 1000000000L; // Max initial power + max k\n   \
        \     long ans = 0;\n\n        while (low <= high) {\n            long mid =\
        \ low + (high - low) / 2;\n            if (check(mid, n, r, k, stations)) {\n\
        \                ans = mid;\n                low = mid + 1;\n            } else\
        \ {\n                high = mid - 1;\n            }\n        }\n\n        return\
        \ ans;\n    }\n\n    private boolean check(long targetPower, int n, int r, long\
        \ k, int[] stations) {\n        long[] diffInitial = new long[n + 1];\n    \
        \    long[] diffForNewStations = new long[n + 1];\n\n        for (int i = 0;\
        \ i < n; ++i) {\n            long val = stations[i];\n            int startIdx\
        \ = Math.max(0, i - r);\n            int endIdx = Math.min(n - 1, i + r);\n\n\
        \            diffInitial[startIdx] += val;\n            if (endIdx + 1 < n +\
        \ 1) {\n                diffInitial[endIdx + 1] -= val;\n            }\n   \
        \     }\n\n        long currentTotalPowerSum = 0;\n        long currentAddedPowerEffect\
        \ = 0;\n        long addedKCount = 0;\n\n        for (int i = 0; i < n; ++i)\
        \ {\n            currentTotalPowerSum += diffInitial[i];\n            currentAddedPowerEffect\
        \ += diffForNewStations[i];\n\n            long totalPowerAtI = currentTotalPowerSum\
        \ + currentAddedPowerEffect;\n\n            if (totalPowerAtI < targetPower)\
        \ {\n                long needed = targetPower - totalPowerAtI;\n          \
        \      addedKCount += needed;\n\n                if (addedKCount > k) {\n  \
        \                  return false;\n                }\n\n                diffForNewStations[i]\
        \ += needed;\n                int endEffectIdx = Math.min(n - 1, i + 2 * r);\n\
        \                if (endEffectIdx + 1 < n + 1) {\n                    diffForNewStations[endEffectIdx\
        \ + 1] -= needed;\n                }\n\n                currentAddedPowerEffect\
        \ += needed;\n            }\n        }\n\n        return true;\n    }\n}"
      python: "class Solution:\n    def maxPower(self, stations: List[int], r: int,\
        \ k: int) -> int:\n        n = len(stations)\n\n        def check(target_power:\
        \ int) -> bool:\n            diff_initial = [0] * (n + 1)\n            diff_for_new_stations\
        \ = [0] * (n + 1)\n\n            for i in range(n):\n                val = stations[i]\n\
        \                start_idx = max(0, i - r)\n                end_idx = min(n\
        \ - 1, i + r)\n\n                diff_initial[start_idx] += val\n          \
        \      if end_idx + 1 < n + 1:\n                    diff_initial[end_idx + 1]\
        \ -= val\n\n            current_total_power_sum = 0\n            current_added_power_effect\
        \ = 0\n            added_k_count = 0\n\n            for i in range(n):\n   \
        \             current_total_power_sum += diff_initial[i]\n                current_added_power_effect\
        \ += diff_for_new_stations[i]\n\n                total_power_at_i = current_total_power_sum\
        \ + current_added_power_effect\n\n                if total_power_at_i < target_power:\n\
        \                    needed = target_power - total_power_at_i\n            \
        \        added_k_count += needed\n\n                    if added_k_count > k:\n\
        \                        return False\n\n                    diff_for_new_stations[i]\
        \ += needed\n                    end_effect_idx = min(n - 1, i + 2 * r)\n  \
        \                  if end_effect_idx + 1 < n + 1:\n                        diff_for_new_stations[end_effect_idx\
        \ + 1] -= needed\n\n                    current_added_power_effect += needed\n\
        \n            return True\n\n        low = 0\n        high = 2 * 10**10 + 10**9\
        \ # A sufficiently large upper bound\n        ans = 0\n\n        while low <=\
        \ high:\n            mid = low + (high - low) // 2\n            if check(mid):\n\
        \                ans = mid\n                low = mid + 1\n            else:\n\
        \                high = mid - 1\n\n        return ans"
      python3: "class Solution:\n    def maxPower(self, stations: List[int], r: int,\
        \ k: int) -> int:\n        n = len(stations)\n\n        def check(target_power:\
        \ int) -> bool:\n            diff_initial = [0] * (n + 1)\n            diff_for_new_stations\
        \ = [0] * (n + 1)\n\n            for i in range(n):\n                val = stations[i]\n\
        \                start_idx = max(0, i - r)\n                end_idx = min(n\
        \ - 1, i + r)\n\n                diff_initial[start_idx] += val\n          \
        \      if end_idx + 1 < n + 1:\n                    diff_initial[end_idx + 1]\
        \ -= val\n\n            current_total_power_sum = 0\n            current_added_power_effect\
        \ = 0\n            added_k_count = 0\n\n            for i in range(n):\n   \
        \             current_total_power_sum += diff_initial[i]\n                current_added_power_effect\
        \ += diff_for_new_stations[i]\n\n                total_power_at_i = current_total_power_sum\
        \ + current_added_power_effect\n\n                if total_power_at_i < target_power:\n\
        \                    needed = target_power - total_power_at_i\n            \
        \        added_k_count += needed\n\n                    if added_k_count > k:\n\
        \                        return False\n\n                    diff_for_new_stations[i]\
        \ += needed\n                    end_effect_idx = min(n - 1, i + 2 * r)\n  \
        \                  if end_effect_idx + 1 < n + 1:\n                        diff_for_new_stations[end_effect_idx\
        \ + 1] -= needed\n\n                    current_added_power_effect += needed\n\
        \n            return True\n\n        low = 0\n        high = 2 * 10**10 + 10**9\
        \ # A sufficiently large upper bound\n        ans = 0\n\n        while low <=\
        \ high:\n            mid = low + (high - low) // 2\n            if check(mid):\n\
        \                ans = mid\n                low = mid + 1\n            else:\n\
        \                high = mid - 1\n\n        return ans"
      c: "#include <stdlib.h>\n#include <string.h>\n#include <stdio.h>\n#include <stdbool.h>\n\
        \n// Helper function for max\nlong long max(long long a, long long b) {\n  \
        \  return a > b ? a : b;\n}\n\n// Helper function for min\nlong long min(long\
        \ long a, long long b) {\n    return a < b ? a : b;\n}\n\n// check function\
        \ to determine if a target_power is achievable\nbool check(long long target_power,\
        \ int n, int r, long long k, int* stations) {\n    long long* diff_initial =\
        \ (long long*)calloc(n + 1, sizeof(long long));\n    long long* diff_for_new_stations\
        \ = (long long*)calloc(n + 1, sizeof(long long));\n\n    if (!diff_initial ||\
        \ !diff_for_new_stations) {\n        // Handle memory allocation failure\n \
        \       free(diff_initial);\n        free(diff_for_new_stations);\n        return\
        \ false; // Or throw an error, depending on context\n    }\n\n    for (int i\
        \ = 0; i < n; ++i) {\n        long long val = stations[i];\n        int start_idx\
        \ = max(0, i - r);\n        int end_idx = min(n - 1, i + r);\n\n        diff_initial[start_idx]\
        \ += val;\n        if (end_idx + 1 < n + 1) {\n            diff_initial[end_idx\
        \ + 1] -= val;\n        }\n    }\n\n    long long current_total_power_sum =\
        \ 0;\n    long long current_added_power_effect = 0;\n    long long added_k_count\
        \ = 0;\n\n    for (int i = 0; i < n; ++i) {\n        current_total_power_sum\
        \ += diff_initial[i];\n        current_added_power_effect += diff_for_new_stations[i];\n\
        \n        long long total_power_at_i = current_total_power_sum + current_added_power_effect;\n\
        \n        if (total_power_at_i < target_power) {\n            long long needed\
        \ = target_power - total_power_at_i;\n            added_k_count += needed;\n\
        \n            if (added_k_count > k) {\n                free(diff_initial);\n\
        \                free(diff_for_new_stations);\n                return false;\n\
        \            }\n\n            diff_for_new_stations[i] += needed;\n        \
        \    int end_effect_idx = min(n - 1, i + 2 * r);\n            if (end_effect_idx\
        \ + 1 < n + 1) {\n                diff_for_new_stations[end_effect_idx + 1]\
        \ -= needed;\n            }\n\n            current_added_power_effect += needed;\n\
        \        }\n    }\n\n    free(diff_initial);\n    free(diff_for_new_stations);\n\
        \    return true;\n}\n\n// Main function for LeetCode problem\nlong long maxPower(int*\
        \ stations, int stationsSize, int r, long long k) {\n    int n = stationsSize;\n\
        \n    long long low = 0;\n    long long high = 2LL * 10000000000LL + 1000000000LL;\
        \ // Max initial power + max k\n    long long ans = 0;\n\n    while (low <=\
        \ high) {\n        long long mid = low + (high - low) / 2;\n        if (check(mid,\
        \ n, r, k, stations)) {\n            ans = mid;\n            low = mid + 1;\n\
        \        } else {\n            high = mid - 1;\n        }\n    }\n\n    return\
        \ ans;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\nusing System.Linq;\n\
        \npublic class Solution {\n    public long MaxPower(int[] stations, int r, long\
        \ k) {\n        int n = stations.Length;\n\n        long low = 0;\n        long\
        \ high = 2L * 10_000_000_000L + 1_000_000_000L; // Max initial power + max k\n\
        \        long ans = 0;\n\n        while (low <= high) {\n            long mid\
        \ = low + (high - low) / 2;\n            if (Check(mid, n, r, k, stations))\
        \ {\n                ans = mid;\n                low = mid + 1;\n          \
        \  } else {\n                high = mid - 1;\n            }\n        }\n\n \
        \       return ans;\n    }\n\n    private bool Check(long targetPower, int n,\
        \ int r, long k, int[] stations) {\n        long[] diffInitial = new long[n\
        \ + 1];\n        long[] diffForNewStations = new long[n + 1];\n\n        for\
        \ (int i = 0; i < n; ++i) {\n            long val = stations[i];\n         \
        \   int startIdx = Math.Max(0, i - r);\n            int endIdx = Math.Min(n\
        \ - 1, i + r);\n\n            diffInitial[startIdx] += val;\n            if\
        \ (endIdx + 1 < n + 1) {\n                diffInitial[endIdx + 1] -= val;\n\
        \            }\n        }\n\n        long currentTotalPowerSum = 0;\n      \
        \  long currentAddedPowerEffect = 0;\n        long addedKCount = 0;\n\n    \
        \    for (int i = 0; i < n; ++i) {\n            currentTotalPowerSum += diffInitial[i];\n\
        \            currentAddedPowerEffect += diffForNewStations[i];\n\n         \
        \   long totalPowerAtI = currentTotalPowerSum + currentAddedPowerEffect;\n\n\
        \            if (totalPowerAtI < targetPower) {\n                long needed\
        \ = targetPower - totalPowerAtI;\n                addedKCount += needed;\n\n\
        \                if (addedKCount > k) {\n                    return false;\n\
        \                }\n\n                diffForNewStations[i] += needed;\n   \
        \             int endEffectIdx = Math.Min(n - 1, i + 2 * r);\n             \
        \   if (endEffectIdx + 1 < n + 1) {\n                    diffForNewStations[endEffectIdx\
        \ + 1] -= needed;\n                }\n\n                currentAddedPowerEffect\
        \ += needed;\n            }\n        }\n\n        return true;\n    }\n}"
      javascript: "/**\n * @param {number[]} stations\n * @param {number} r\n * @param\
        \ {number} k\n * @return {number}\n */\nvar maxPower = function(stations, r,\
        \ k) {\n    const n = stations.length;\n\n    const check = (target_power) =>\
        \ {\n        const diff_initial = new Array(n + 1).fill(0);\n        const diff_for_new_stations\
        \ = new Array(n + 1).fill(0);\n\n        for (let i = 0; i < n; ++i) {\n   \
        \         const val = stations[i];\n            const start_idx = Math.max(0,\
        \ i - r);\n            const end_idx = Math.min(n - 1, i + r);\n\n         \
        \   diff_initial[start_idx] += val;\n            if (end_idx + 1 < n + 1) {\n\
        \                diff_initial[end_idx + 1] -= val;\n            }\n        }\n\
        \n        let current_total_power_sum = 0;\n        let current_added_power_effect\
        \ = 0;\n        let added_k_count = 0;\n\n        for (let i = 0; i < n; ++i)\
        \ {\n            current_total_power_sum += diff_initial[i];\n            current_added_power_effect\
        \ += diff_for_new_stations[i];\n\n            const total_power_at_i = current_total_power_sum\
        \ + current_added_power_effect;\n\n            if (total_power_at_i < target_power)\
        \ {\n                const needed = target_power - total_power_at_i;\n     \
        \           added_k_count += needed;\n\n                if (added_k_count >\
        \ k) {\n                    return false;\n                }\n\n           \
        \     diff_for_new_stations[i] += needed;\n                const end_effect_idx\
        \ = Math.min(n - 1, i + 2 * r);\n                if (end_effect_idx + 1 < n\
        \ + 1) {\n                    diff_for_new_stations[end_effect_idx + 1] -= needed;\n\
        \                }\n\n                current_added_power_effect += needed;\n\
        \            }\n        }\n\n        return true;\n    };\n\n    let low = 0;\n\
        \    let high = 2 * 10**10 + 10**9; // A sufficiently large upper bound\n  \
        \  let ans = 0;\n\n    while (low <= high) {\n        const mid = Math.floor(low\
        \ + (high - low) / 2);\n        if (check(mid)) {\n            ans = mid;\n\
        \            low = mid + 1;\n        } else {\n            high = mid - 1;\n\
        \        }\n    }\n\n    return ans;\n};"
      typescript: "function maxPower(stations: number[], r: number, k: number): number\
        \ {\n    const n = stations.length;\n\n    const check = (target_power: number):\
        \ boolean => {\n        const diff_initial: number[] = new Array(n + 1).fill(0);\n\
        \        const diff_for_new_stations: number[] = new Array(n + 1).fill(0);\n\
        \n        for (let i = 0; i < n; ++i) {\n            const val = stations[i];\n\
        \            const start_idx = Math.max(0, i - r);\n            const end_idx\
        \ = Math.min(n - 1, i + r);\n\n            diff_initial[start_idx] += val;\n\
        \            if (end_idx + 1 < n + 1) {\n                diff_initial[end_idx\
        \ + 1] -= val;\n            }\n        }\n\n        let current_total_power_sum\
        \ = 0;\n        let current_added_power_effect = 0;\n        let added_k_count\
        \ = 0;\n\n        for (let i = 0; i < n; ++i) {\n            current_total_power_sum\
        \ += diff_initial[i];\n            current_added_power_effect += diff_for_new_stations[i];\n\
        \n            const total_power_at_i = current_total_power_sum + current_added_power_effect;\n\
        \n            if (total_power_at_i < target_power) {\n                const\
        \ needed = target_power - total_power_at_i;\n                added_k_count +=\
        \ needed;\n\n                if (added_k_count > k) {\n                    return\
        \ false;\n                }\n\n                diff_for_new_stations[i] += needed;\n\
        \                const end_effect_idx = Math.min(n - 1, i + 2 * r);\n      \
        \          if (end_effect_idx + 1 < n + 1) {\n                    diff_for_new_stations[end_effect_idx\
        \ + 1] -= needed;\n                }\n\n                current_added_power_effect\
        \ += needed;\n            }\n        }\n\n        return true;\n    };\n\n \
        \   let low = 0;\n    let high = 2 * 10**10 + 10**9; // A sufficiently large\
        \ upper bound\n    let ans = 0;\n\n    while (low <= high) {\n        const\
        \ mid = Math.floor(low + (high - low) / 2);\n        if (check(mid)) {\n   \
        \         ans = mid;\n            low = mid + 1;\n        } else {\n       \
        \     high = mid - 1;\n        }\n    }\n\n    return ans;\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $stations\n     * @param\
        \ Integer $r\n     * @param Integer $k\n     * @return Integer\n     */\n  \
        \  function maxPower($stations, $r, $k) {\n        $n = count($stations);\n\n\
        \        $check = function($target_power) use ($n, $r, $k, $stations) {\n  \
        \          $diff_initial = array_fill(0, $n + 1, 0);\n            $diff_for_new_stations\
        \ = array_fill(0, $n + 1, 0);\n\n            for ($i = 0; $i < $n; ++$i) {\n\
        \                $val = $stations[$i];\n                $start_idx = max(0,\
        \ $i - $r);\n                $end_idx = min($n - 1, $i + $r);\n\n          \
        \      $diff_initial[$start_idx] += $val;\n                if ($end_idx + 1\
        \ < $n + 1) {\n                    $diff_initial[$end_idx + 1] -= $val;\n  \
        \              }\n            }\n\n            $current_total_power_sum = 0;\n\
        \            $current_added_power_effect = 0;\n            $added_k_count =\
        \ 0;\n\n            for ($i = 0; $i < $n; ++$i) {\n                $current_total_power_sum\
        \ += $diff_initial[$i];\n                $current_added_power_effect += $diff_for_new_stations[$i];\n\
        \n                $total_power_at_i = $current_total_power_sum + $current_added_power_effect;\n\
        \n                if ($total_power_at_i < $target_power) {\n               \
        \     $needed = $target_power - $total_power_at_i;\n                    $added_k_count\
        \ += $needed;\n\n                    if ($added_k_count > $k) {\n          \
        \              return false;\n                    }\n\n                    $diff_for_new_stations[$i]\
        \ += $needed;\n                    $end_effect_idx = min($n - 1, $i + 2 * $r);\n\
        \                    if ($end_effect_idx + 1 < $n + 1) {\n                 \
        \       $diff_for_new_stations[$end_effect_idx + 1] -= $needed;\n          \
        \          }\n\n                    $current_added_power_effect += $needed;\n\
        \                }\n            }\n\n            return true;\n        };\n\n\
        \        $low = 0;\n        $high = 2 * 10**10 + 10**9; // A sufficiently large\
        \ upper bound\n        $ans = 0;\n\n        while ($low <= $high) {\n      \
        \      $mid = floor($low + ($high - $low) / 2);\n            if ($check($mid))\
        \ {\n                $ans = $mid;\n                $low = $mid + 1;\n      \
        \      } else {\n                $high = $mid - 1;\n            }\n        }\n\
        \n        return $ans;\n    }\n}"
      swift: "class Solution {\n    func maxPower(_ stations: [Int], _ r: Int, _ k:\
        \ Int) -> Int {\n        let n = stations.count\n\n        func check(_ target_power:\
        \ Int) -> Bool {\n            var diff_initial = Array(repeating: 0, count:\
        \ n + 1)\n            var diff_for_new_stations = Array(repeating: 0, count:\
        \ n + 1)\n\n            for i in 0..<n {\n                let val = stations[i]\n\
        \                let start_idx = max(0, i - r)\n                let end_idx\
        \ = min(n - 1, i + r)\n\n                diff_initial[start_idx] += val\n  \
        \              if end_idx + 1 < n + 1 {\n                    diff_initial[end_idx\
        \ + 1] -= val\n                }\n            }\n\n            var current_total_power_sum\
        \ = 0\n            var current_added_power_effect = 0\n            var added_k_count\
        \ = 0\n\n            for i in 0..<n {\n                current_total_power_sum\
        \ += diff_initial[i]\n                current_added_power_effect += diff_for_new_stations[i]\n\
        \n                let total_power_at_i = current_total_power_sum + current_added_power_effect\n\
        \n                if total_power_at_i < target_power {\n                   \
        \ let needed = target_power - total_power_at_i\n                    added_k_count\
        \ += needed\n\n                    if added_k_count > k {\n                \
        \        return false\n                    }\n\n                    diff_for_new_stations[i]\
        \ += needed\n                    let end_effect_idx = min(n - 1, i + 2 * r)\n\
        \                    if end_effect_idx + 1 < n + 1 {\n                     \
        \   diff_for_new_stations[end_effect_idx + 1] -= needed\n                  \
        \  }\n\n                    current_added_power_effect += needed\n         \
        \       }\n            }\n\n            return true\n        }\n\n        var\
        \ low = 0\n        var high = 2 * 10_000_000_000 + 1_000_000_000 // A sufficiently\
        \ large upper bound\n        var ans = 0\n\n        while low <= high {\n  \
        \          let mid = low + (high - low) / 2\n            if check(mid) {\n \
        \               ans = mid\n                low = mid + 1\n            } else\
        \ {\n                high = mid - 1\n            }\n        }\n\n        return\
        \ ans\n    }\n}"
      kotlin: "import kotlin.math.max\nimport kotlin.math.min\n\nclass Solution {\n\
        \    fun maxPower(stations: IntArray, r: Int, k: Long): Long {\n        val\
        \ n = stations.size\n\n        fun check(target_power: Long): Boolean {\n  \
        \          val diffInitial = LongArray(n + 1) { 0L }\n            val diffForNewStations\
        \ = LongArray(n + 1) { 0L }\n\n            for (i in 0 until n) {\n        \
        \        val val_ = stations[i].toLong()\n                val start_idx = max(0,\
        \ i - r)\n                val end_idx = min(n - 1, i + r)\n\n              \
        \  diffInitial[start_idx] += val_\n                if (end_idx + 1 < n + 1)\
        \ {\n                    diffInitial[end_idx + 1] -= val_\n                }\n\
        \            }\n\n            var currentTotalPowerSum = 0L\n            var\
        \ currentAddedPowerEffect = 0L\n            var addedKCount = 0L\n\n       \
        \     for (i in 0 until n) {\n                currentTotalPowerSum += diffInitial[i]\n\
        \                currentAddedPowerEffect += diffForNewStations[i]\n\n      \
        \          val totalPowerAtI = currentTotalPowerSum + currentAddedPowerEffect\n\
        \n                if (totalPowerAtI < target_power) {\n                    val\
        \ needed = target_power - totalPowerAtI\n                    addedKCount +=\
        \ needed\n\n                    if (addedKCount > k) {\n                   \
        \     return false\n                    }\n\n                    diffForNewStations[i]\
        \ += needed\n                    val endEffectIdx = min(n - 1, i + 2 * r)\n\
        \                    if (endEffectIdx + 1 < n + 1) {\n                     \
        \   diffForNewStations[endEffectIdx + 1] -= needed\n                    }\n\n\
        \                    currentAddedPowerEffect += needed\n                }\n\
        \            }\n\n            return true\n        }\n\n        var low = 0L\n\
        \        var high = 2L * 10_000_000_000L + 1_000_000_000L // A sufficiently\
        \ large upper bound\n        var ans = 0L\n\n        while (low <= high) {\n\
        \            val mid = low + (high - low) / 2\n            if (check(mid)) {\n\
        \                ans = mid\n                low = mid + 1\n            } else\
        \ {\n                high = mid - 1\n            }\n        }\n\n        return\
        \ ans\n    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int maxPower(List<int> stations,\
        \ int r, int k) {\n    final n = stations.length;\n\n    bool check(int targetPower)\
        \ {\n      final diffInitial = List<int>.filled(n + 1, 0);\n      final diffForNewStations\
        \ = List<int>.filled(n + 1, 0);\n\n      for (int i = 0; i < n; ++i) {\n   \
        \     final val = stations[i];\n        final startIdx = max(0, i - r);\n  \
        \      final endIdx = min(n - 1, i + r);\n\n        diffInitial[startIdx] +=\
        \ val;\n        if (endIdx + 1 < n + 1) {\n          diffInitial[endIdx + 1]\
        \ -= val;\n        }\n      }\n\n      int currentTotalPowerSum = 0;\n     \
        \ int currentAddedPowerEffect = 0;\n      int addedKCount = 0;\n\n      for\
        \ (int i = 0; i < n; ++i) {\n        currentTotalPowerSum += diffInitial[i];\n\
        \        currentAddedPowerEffect += diffForNewStations[i];\n\n        final\
        \ totalPowerAtI = currentTotalPowerSum + currentAddedPowerEffect;\n\n      \
        \  if (totalPowerAtI < targetPower) {\n          final needed = targetPower\
        \ - totalPowerAtI;\n          addedKCount += needed;\n\n          if (addedKCount\
        \ > k) {\n            return false;\n          }\n\n          diffForNewStations[i]\
        \ += needed;\n          final endEffectIdx = min(n - 1, i + 2 * r);\n      \
        \    if (endEffectIdx + 1 < n + 1) {\n            diffForNewStations[endEffectIdx\
        \ + 1] -= needed;\n          }\n\n          currentAddedPowerEffect += needed;\n\
        \        }\n      }\n\n      return true;\n    }\n\n    int low = 0;\n    int\
        \ high = 2 * pow(10, 10).toInt() + pow(10, 9).toInt(); // A sufficiently large\
        \ upper bound\n    int ans = 0;\n\n    while (low <= high) {\n      final mid\
        \ = low + ((high - low) ~/ 2);\n      if (check(mid)) {\n        ans = mid;\n\
        \        low = mid + 1;\n      } else {\n        high = mid - 1;\n      }\n\
        \    }\n\n    return ans;\n  }\n}"
      go: "package main\n\nimport (\n\t\"math\"\n)\n\nfunc maxPower(stations []int,\
        \ r int, k int) int {\n\tn := len(stations)\n\n\tcheck := func(targetPower int)\
        \ bool {\n\t\tdiffInitial := make([]int, n+1)\n\t\tdiffForNewStations := make([]int,\
        \ n+1)\n\n\t\tfor i := 0; i < n; i++ {\n\t\t\tval := stations[i]\n\t\t\tstartIdx\
        \ := int(math.Max(0, float64(i-r)))\n\t\t\tendIdx := int(math.Min(float64(n-1),\
        \ float64(i+r)))\n\n\t\t\tdiffInitial[startIdx] += val\n\t\t\tif endIdx+1 <\
        \ n+1 {\n\t\t\t\tdiffInitial[endIdx+1] -= val\n\t\t\t}\n\t\t}\n\n\t\tcurrentTotalPowerSum\
        \ := 0\n\t\tcurrentAddedPowerEffect := 0\n\t\taddedKCount := 0\n\n\t\tfor i\
        \ := 0; i < n; i++ {\n\t\t\tcurrentTotalPowerSum += diffInitial[i]\n\t\t\tcurrentAddedPowerEffect\
        \ += diffForNewStations[i]\n\n\t\t\ttotalPowerAtI := currentTotalPowerSum +\
        \ currentAddedPowerEffect\n\n\t\t\tif totalPowerAtI < targetPower {\n\t\t\t\t\
        needed := targetPower - totalPowerAtI\n\t\t\t\taddedKCount += needed\n\n\t\t\
        \t\tif addedKCount > k {\n\t\t\t\t\treturn false\n\t\t\t\t}\n\n\t\t\t\tdiffForNewStations[i]\
        \ += needed\n\t\t\t\tendEffectIdx := int(math.Min(float64(n-1), float64(i+2*r)))\n\
        \t\t\t\tif endEffectIdx+1 < n+1 {\n\t\t\t\t\tdiffForNewStations[endEffectIdx+1]\
        \ -= needed\n\t\t\t\t}\n\n\t\t\t\tcurrentAddedPowerEffect += needed\n\t\t\t\
        }\n\t\t}\n\n\t\treturn true\n\t}\n\n\tlow := 0\n\thigh := 2*10000000000 + 1000000000\
        \ // A sufficiently large upper bound\n\tans := 0\n\n\tfor low <= high {\n\t\
        \tmid := low + (high-low)/2\n\t\tif check(mid) {\n\t\t\tans = mid\n\t\t\tlow\
        \ = mid + 1\n\t\t} else {\n\t\t\thigh = mid - 1\n\t\t}\n\t}\n\n\treturn ans\n\
        }"
      ruby: "class Solution\n    # @param {Integer[]} stations\n    # @param {Integer}\
        \ r\n    # @param {Integer} k\n    # @return {Integer}\n    def max_power(stations,\
        \ r, k)\n        n = stations.length\n\n        check = lambda target_power\
        \ do\n            diff_initial = Array.new(n + 1, 0)\n            diff_for_new_stations\
        \ = Array.new(n + 1, 0)\n\n            stations.each_with_index do |val, i|\n\
        \                start_idx = [0, i - r].max\n                end_idx = [n -\
        \ 1, i + r].min\n\n                diff_initial[start_idx] += val\n        \
        \        if end_idx + 1 < n + 1\n                    diff_initial[end_idx +\
        \ 1] -= val\n                end\n            end\n\n            current_total_power_sum\
        \ = 0\n            current_added_power_effect = 0\n            added_k_count\
        \ = 0\n\n            n.times do |i|\n                current_total_power_sum\
        \ += diff_initial[i]\n                current_added_power_effect += diff_for_new_stations[i]\n\
        \n                total_power_at_i = current_total_power_sum + current_added_power_effect\n\
        \n                if total_power_at_i < target_power\n                    needed\
        \ = target_power - total_power_at_i\n                    added_k_count += needed\n\
        \n                    if added_k_count > k\n                        return false\n\
        \                    end\n\n                    diff_for_new_stations[i] +=\
        \ needed\n                    end_effect_idx = [n - 1, i + 2 * r].min\n    \
        \                if end_effect_idx + 1 < n + 1\n                        diff_for_new_stations[end_effect_idx\
        \ + 1] -= needed\n                    end\n\n                    current_added_power_effect\
        \ += needed\n                end\n            end\n\n            true\n    \
        \    end\n\n        low = 0\n        high = 2 * 10**10 + 10**9 # A sufficiently\
        \ large upper bound\n        ans = 0\n\n        while low <= high\n        \
        \    mid = low + (high - low) / 2\n            if check.call(mid)\n        \
        \        ans = mid\n                low = mid + 1\n            else\n      \
        \          high = mid - 1\n            end\n        end\n\n        ans\n   \
        \ end\nend"
      scala: "import scala.collection.mutable.ArrayBuffer\nimport scala.math.{max, min}\n\
        \nobject Solution {\n    def maxPower(stations: Array[Int], r: Int, k: Long):\
        \ Long = {\n        val n = stations.length\n\n        def check(target_power:\
        \ Long): Boolean = {\n            val diffInitial = ArrayBuffer.fill(n + 1)(0L)\n\
        \            val diffForNewStations = ArrayBuffer.fill(n + 1)(0L)\n\n      \
        \      for (i <- 0 until n) {\n                val val_ = stations(i).toLong\n\
        \                val start_idx = max(0, i - r)\n                val end_idx\
        \ = min(n - 1, i + r)\n\n                diffInitial(start_idx) += val_\n  \
        \              if (end_idx + 1 < n + 1) {\n                    diffInitial(end_idx\
        \ + 1) -= val_\n                }\n            }\n\n            var currentTotalPowerSum\
        \ = 0L\n            var currentAddedPowerEffect = 0L\n            var addedKCount\
        \ = 0L\n\n            for (i <- 0 until n) {\n                currentTotalPowerSum\
        \ += diffInitial(i)\n                currentAddedPowerEffect += diffForNewStations(i)\n\
        \n                val totalPowerAtI = currentTotalPowerSum + currentAddedPowerEffect\n\
        \n                if (totalPowerAtI < target_power) {\n                    val\
        \ needed = target_power - totalPowerAtI\n                    addedKCount +=\
        \ needed\n\n                    if (addedKCount > k) {\n                   \
        \     return false\n                    }\n\n                    diffForNewStations(i)\
        \ += needed\n                    val endEffectIdx = min(n - 1, i + 2 * r)\n\
        \                    if (endEffectIdx + 1 < n + 1) {\n                     \
        \   diffForNewStations(endEffectIdx + 1) -= needed\n                    }\n\n\
        \                    currentAddedPowerEffect += needed\n                }\n\
        \            }\n\n            true\n        }\n\n        var low = 0L\n    \
        \    var high = 2L * 10_000_000_000L + 1_000_000_000L // A sufficiently large\
        \ upper bound\n        var ans = 0L\n\n        while (low <= high) {\n     \
        \       val mid = low + (high - low) / 2\n            if (check(mid)) {\n  \
        \              ans = mid\n                low = mid + 1\n            } else\
        \ {\n                high = mid - 1\n            }\n        }\n\n        ans\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn max_power(stations: Vec<i32>, r: i32, k: i64)\
        \ -> i64 {\n        let n = stations.len();\n\n        let check = |target_power:\
        \ i64| -> bool {\n            let mut diff_initial = vec![0i64; n + 1];\n  \
        \          let mut diff_for_new_stations = vec![0i64; n + 1];\n\n          \
        \  for i in 0..n {\n                let val = stations[i] as i64;\n        \
        \        let start_idx = (0).max(i as i32 - r) as usize;\n                let\
        \ end_idx = (n as i32 - 1).min(i as i32 + r) as usize;\n\n                diff_initial[start_idx]\
        \ += val;\n                if end_idx + 1 < n + 1 {\n                    diff_initial[end_idx\
        \ + 1] -= val;\n                }\n            }\n\n            let mut current_total_power_sum\
        \ = 0i64;\n            let mut current_added_power_effect = 0i64;\n        \
        \    let mut added_k_count = 0i64;\n\n            for i in 0..n {\n        \
        \        current_total_power_sum += diff_initial[i];\n                current_added_power_effect\
        \ += diff_for_new_stations[i];\n\n                let total_power_at_i = current_total_power_sum\
        \ + current_added_power_effect;\n\n                if total_power_at_i < target_power\
        \ {\n                    let needed = target_power - total_power_at_i;\n   \
        \                 added_k_count += needed;\n\n                    if added_k_count\
        \ > k {\n                        return false;\n                    }\n\n  \
        \                  diff_for_new_stations[i] += needed;\n                   \
        \ let end_effect_idx = (n as i32 - 1).min(i as i32 + 2 * r) as usize;\n    \
        \                if end_effect_idx + 1 < n + 1 {\n                        diff_for_new_stations[end_effect_idx\
        \ + 1] -= needed;\n                    }\n\n                    current_added_power_effect\
        \ += needed;\n                }\n            }\n\n            true\n       \
        \ };\n\n        let mut low = 0i64;\n        let mut high = 2 * 10_000_000_000i64\
        \ + 1_000_000_000i64; // A sufficiently large upper bound\n        let mut ans\
        \ = 0i64;\n\n        while low <= high {\n            let mid = low + (high\
        \ - low) / 2;\n            if check(mid) {\n                ans = mid;\n   \
        \             low = mid + 1;\n            } else {\n                high = mid\
        \ - 1;\n            }\n        }\n\n        ans\n    }\n}"
      racket: "#lang racket\n\n(define (max-power stations r k)\n  (define n (vector-length\
        \ stations))\n\n  (define (check-fixed target-power)\n    (define diff-initial\
        \ (make-vector (+ n 1) 0))\n    (define diff-for-new-stations (make-vector (+\
        \ n 1) 0))\n\n    (for ([i (in-range n)])\n      (define val (vector-ref stations\
        \ i))\n      (define start-idx (max 0 (- i r)))\n      (define end-idx (min\
        \ (- n 1) (+ i r)))\n\n      (vector-set! diff-initial start-idx (+ (vector-ref\
        \ diff-initial start-idx) val))\n      (when (< (+ end-idx 1) (+ n 1))\n   \
        \     (vector-set! diff-initial (+ end-idx 1) (- (vector-ref diff-initial (+\
        \ end-idx 1)) val))))\n\n    (define current-total-power-sum 0)\n    (define\
        \ current-added-power-effect 0)\n    (define added-k-count 0)\n\n    (for ([i\
        \ (in-range n)])\n      (set! current-total-power-sum (+ current-total-power-sum\
        \ (vector-ref diff-initial i)))\n      (set! current-added-power-effect (+ current-added-power-effect\
        \ (vector-ref diff-for-new-stations i)))\n\n      (define total-power-at-i (+\
        \ current-total-power-sum current-added-power-effect))\n\n      (when (< total-power-at-i\
        \ target-power)\n        (define needed (- target-power total-power-at-i))\n\
        \        (set! added-k-count (+ added-k-count needed))\n\n        (when (> added-k-count\
        \ k)\n          (return-from check-fixed #f)) ; Early exit for false\n\n   \
        \     (vector-set! diff-for-new-stations i (+ (vector-ref diff-for-new-stations\
        \ i) needed))\n        (define end-effect-idx (min (- n 1) (+ i (* 2 r))))\n\
        \        (when (< (+ end-effect-idx 1) (+ n 1))\n          (vector-set! diff-for-new-stations\
        \ (+ end-effect-idx 1) (- (vector-ref diff-for-new-stations (+ end-effect-idx\
        \ 1)) needed)))\n\n        (set! current-added-power-effect (+ current-added-power-effect\
        \ needed))))\n\n    #t)\n\n  (define low 0)\n  (define high (+ (* 2 10000000000)\
        \ 1000000000)) ; A sufficiently large upper bound\n  (define ans 0)\n\n  (let\
        \ loop ((l low) (h high) (a ans))\n    (if (<= l h)\n        (let* ((mid (+\
        \ l (quotient (- h l) 2))))\n          (if (check-fixed mid)\n             \
        \ (loop (+ mid 1) h mid)\n              (loop l (- mid 1) a)))\n        a)))"
      erlang: "-module(solution).\n-export([max_power/3]).\n\nmax_power(Stations, R,\
        \ K) ->\n    N = length(Stations),\n\n    Check = fun(TargetPower) ->\n    \
        \    DiffInitial = array:new(N + 1, {default, 0}),\n        DiffForNewStations\
        \ = array:new(N + 1, {default, 0}),\n\n        % Calculate initial power contributions\
        \ from existing stations\n        DiffInitial1 = lists:foldl(fun(I, AccDiffInitial)\
        \ ->\n            Val = lists:nth(I + 1, Stations),\n            StartIdx =\
        \ max(0, I - R),\n            EndIdx = min(N - 1, I + R),\n\n            AccDiffInitial2\
        \ = array:set(StartIdx, array:get(StartIdx, AccDiffInitial) + Val, AccDiffInitial),\n\
        \            if (EndIdx + 1 < N + 1) ->\n                array:set(EndIdx +\
        \ 1, array:get(EndIdx + 1, AccDiffInitial2) - Val, AccDiffInitial2);\n     \
        \       true ->\n                AccDiffInitial2\n            end\n        end,\
        \ DiffInitial, lists:seq(0, N - 1)),\n\n        CurrentTotalPowerSum = 0,\n\
        \        CurrentAddedPowerEffect = 0,\n        AddedKCount = 0,\n\n        {_,\
        \ _, _, Result} = lists:foldl(fun(I, {AccCurrentTotalPowerSum, AccCurrentAddedPowerEffect,\
        \ AccAddedKCount, Possible}) ->\n            if not Possible ->\n          \
        \      {AccCurrentTotalPowerSum, AccCurrentAddedPowerEffect, AccAddedKCount,\
        \ Possible};\n            true ->\n                NewCurrentTotalPowerSum =\
        \ AccCurrentTotalPowerSum + array:get(I, DiffInitial1),\n                NewCurrentAddedPowerEffect\
        \ = AccCurrentAddedPowerEffect + array:get(I, DiffForNewStations),\n\n     \
        \           TotalPowerAtI = NewCurrentTotalPowerSum + NewCurrentAddedPowerEffect,\n\
        \n                if (TotalPowerAtI < TargetPower) ->\n                    Needed\
        \ = TargetPower - TotalPowerAtI,\n                    NewAddedKCount = AccAddedKCount\
        \ + Needed,\n\n                    if (NewAddedKCount > K) ->\n            \
        \            {NewCurrentTotalPowerSum, NewCurrentAddedPowerEffect, NewAddedKCount,\
        \ false};\n                    true ->\n                        DiffForNewStations1\
        \ = array:set(I, array:get(I, DiffForNewStations) + Needed, DiffForNewStations),\n\
        \                        EndEffectIdx = min(N - 1, I + 2 * R),\n           \
        \             DiffForNewStations2 = if (EndEffectIdx + 1 < N + 1) ->\n     \
        \                       array:set(EndEffectIdx + 1, array:get(EndEffectIdx +\
        \ 1, DiffForNewStations1) - Needed, DiffForNewStations1);\n                \
        \        true ->\n                            DiffForNewStations1\n        \
        \                end,\n                        {NewCurrentTotalPowerSum, NewCurrentAddedPowerEffect\
        \ + Needed, NewAddedKCount, true}\n                    end;\n              \
        \  true ->\n                    {NewCurrentTotalPowerSum, NewCurrentAddedPowerEffect,\
        \ AccAddedKCount, true}\n                end\n            end\n        end,\
        \ {CurrentTotalPowerSum, CurrentAddedPowerEffect, AddedKCount, true}, lists:seq(0,\
        \ N - 1)),\n\n        Result\n    end,\n\n    Low = 0,\n    High = 2 * 10000000000\
        \ + 1000000000, % A sufficiently large upper bound\n    Ans = 0,\n\n    binary_search(Low,\
        \ High, Ans, Check).\n\nbinary_search(Low, High, Ans, Check) when Low =< High\
        \ ->\n    Mid = Low + (High - Low) div 2,\n    case Check(Mid) of\n        true\
        \ ->\n            binary_search(Mid + 1, High, Mid, Check);\n        false ->\n\
        \            binary_search(Low, Mid - 1, Ans, Check)\n    end;\nbinary_search(_,\
        \ _, Ans, _) ->\n    Ans.\n\n% Helper functions for max/min\nmax(A, B) when\
        \ A >= B -> A;\nmax(A, B) -> B.\n\nmin(A, B) when A =< B -> A;\nmin(A, B) ->\
        \ B."
      elixir: "defmodule Solution do\n  @spec max_power(stations :: [integer], r ::\
        \ integer, k :: integer) :: integer\n  def max_power(stations, r, k) do\n  \
        \  n = length(stations)\n\n    check = fn target_power ->\n      diff_initial\
        \ = :array.new(n + 1, default: 0)\n      diff_for_new_stations = :array.new(n\
        \ + 1, default: 0)\n\n      # Calculate initial power contributions from existing\
        \ stations\n      diff_initial = Enum.reduce(0..(n - 1), diff_initial, fn i,\
        \ acc_diff_initial ->\n        val = Enum.at(stations, i)\n        start_idx\
        \ = max(0, i - r)\n        end_idx = min(n - 1, i + r)\n\n        acc_diff_initial_2\
        \ = :array.set(start_idx, :array.get(start_idx, acc_diff_initial) + val, acc_diff_initial)\n\
        \        if end_idx + 1 < n + 1 do\n          :array.set(end_idx + 1, :array.get(end_idx\
        \ + 1, acc_diff_initial_2) - val, acc_diff_initial_2)\n        else\n      \
        \    acc_diff_initial_2\n        end\n      end)\n\n      current_total_power_sum\
        \ = 0\n      current_added_power_effect = 0\n      added_k_count = 0\n\n   \
        \   {_final_sum, _final_effect, _final_k_count, possible} = Enum.reduce_while(0..(n\
        \ - 1), {current_total_power_sum, current_added_power_effect, added_k_count,\
        \ true}, fn i, {acc_current_total_power_sum, acc_current_added_power_effect,\
        \ acc_added_k_count, current_possible} ->\n        if not current_possible do\n\
        \          {:halt, {acc_current_total_power_sum, acc_current_added_power_effect,\
        \ acc_added_k_count, current_possible}}\n        else\n          new_current_total_power_sum\
        \ = acc_current_total_power_sum + :array.get(i, diff_initial)\n          new_current_added_power_effect\
        \ = acc_current_added_power_effect + :array.get(i, diff_for_new_stations)\n\n\
        \          total_power_at_i = new_current_total_power_sum + new_current_added_power_effect\n\
        \n          if total_power_at_i < target_power do\n            needed = target_power\
        \ - total_power_at_i\n            new_added_k_count = acc_added_k_count + needed\n\
        \n            if new_added_k_count > k do\n              {:halt, {new_current_total_power_sum,\
        \ new_current_added_power_effect, new_added_k_count, false}}\n            else\n\
        \              :array.set(i, :array.get(i, diff_for_new_stations) + needed,\
        \ diff_for_new_stations)\n              end_effect_idx = min(n - 1, i + 2 *\
        \ r)\n              if end_effect_idx + 1 < n + 1 do\n                :array.set(end_effect_idx\
        \ + 1, :array.get(end_effect_idx + 1, diff_for_new_stations) - needed, diff_for_new_stations)\n\
        \              else\n                :ok # no change to diff_for_new_stations\n\
        \              end\n              {:cont, {new_current_total_power_sum, new_current_added_power_effect\
        \ + needed, new_added_k_count, true}}\n            end\n          else\n   \
        \         {:cont, {new_current_total_power_sum, new_current_added_power_effect,\
        \ acc_added_k_count, true}}\n          end\n        end\n      end)\n      possible\n\
        \    end\n\n    low = 0\n    high = 2 * :math.pow(10, 10) |> round() + :math.pow(10,\
        \ 9) |> round() # A sufficiently large upper bound\n    ans = 0\n\n    binary_search(low,\
        \ high, ans, check)\n  end\n\n  defp binary_search(low, high, ans, check) when\
        \ low <= high do\n    mid = low + div(high - low, 2)\n    if check.(mid) do\n\
        \      binary_search(mid + 1, high, mid, check)\n    else\n      binary_search(low,\
        \ mid - 1, ans, check)\n    end\n  end\n\n  defp binary_search(_low, _high,\
        \ ans, _check), do: ans\n\n  defp max(a, b), do: if a >= b, do: a, else: b\n\
        \  defp min(a, b), do: if a <= b, do: a, else: b\nend"
    approach: 'The problem asks us to maximize the minimum power of any city by adding
      at most `k` power stations. This is a classic "maximize the minimum" type problem,
      which can typically be solved using binary search on the answer. We can binary
      search for the maximum possible minimum power `X` that can be achieved for all
      cities. The `check(X)` function will determine if it''s possible to make every
      city have at least `X` power using at most `k` additional stations.


      The `check(X)` function employs a greedy strategy combined with a difference array
      (or sweep-line) technique for efficient power calculation. First, we need to calculate
      the initial power provided to each city by the existing `stations`. A naive approach
      of summing stations within range `r` for each city would be O(N*R), which is too
      slow. Instead, we use a difference array `diff_initial`. For each station `stations[s_idx]`,
      it contributes power to cities in the range `[max(0, s_idx - r), min(n-1, s_idx
      + r)]`. We mark the start of its contribution by adding `stations[s_idx]` at `diff_initial[max(0,
      s_idx - r)]` and the end by subtracting `stations[s_idx]` at `diff_initial[min(n-1,
      s_idx + r) + 1]`.


      Next, we iterate through each city `i` from `0` to `n-1`. We maintain a running
      sum of `diff_initial` to get the current power from existing stations. Simultaneously,
      we maintain another running sum for `diff_for_new_stations`, which tracks the
      power contributed by stations we''ve added greedily so far. If the total power
      for city `i` (initial + added) is less than `X`, we must add more stations. To
      do this optimally, we calculate `needed = X - total_power_at_i`. We then add `needed`
      to our `added_k_count`. If `added_k_count` exceeds `k`, it''s impossible to achieve
      `X`, so we return `False`. Otherwise, we place these `needed` stations. The most
      greedy strategy to cover city `i` and maximize their impact on subsequent cities
      is to place them as far right as possible while still covering city `i`. This
      optimal placement is at city `min(n-1, i+r)`. A station placed at `placement_idx`
      contributes power to cities in the range `[max(0, placement_idx - r), min(n-1,
      placement_idx + r)]`. With `placement_idx = min(n-1, i+r)`, these `needed` stations
      will contribute power to cities in the range `[max(0, i), min(n-1, i+2*r)]`. We
      update `diff_for_new_stations` by adding `needed` at index `i` and subtracting
      `needed` at index `min(n-1, i+2*r) + 1`. We also immediately update the `current_added_power_effect`
      for city `i` by adding `needed` to reflect the newly placed stations. After iterating
      through all cities, if we haven''t exceeded `k` stations, we return `True`.'
    time_complexity: 'O(N * log(MAX_POWER)).

      - The `check` function iterates through the `n` cities once. Inside the loop,
      operations are constant time (array access, arithmetic). The initial population
      of `diff_initial` also takes O(N). Thus, `check` runs in O(N) time.

      - The binary search performs `log(MAX_POWER)` iterations. `MAX_POWER` can be up
      to approximately `2 * 10^10` (maximum initial power for a city plus maximum power
      from `k` additional stations). `log(2 * 10^10)` is roughly 34-35 iterations.

      - Therefore, the total time complexity is O(N * log(MAX_POWER)). Given N=10^5,
      this is roughly 10^5 * 35, which is efficient enough.'
    space_complexity: 'O(N).

      - We use two difference arrays, `diff_initial` and `diff_for_new_stations`, each
      of size `n+1`. These arrays store `long long` (or equivalent) values.

      - The space required is directly proportional to `n`.'
    elapsed_time: 145.3145990371704
    model: gemini-2.5-flash
    generated_at: '2025-11-24 20:42:03 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxPower(vector<int>& stations, int r,\
        \ int k) {\n        int n = stations.size();\n        vector<int> power(n);\n\
        \        for (int i = 0; i < n; i++) {\n            for (int j = max(0, i -\
        \ r); j <= min(n - 1, i + r); j++) {\n                power[i] += stations[j];\n\
        \            }\n        }\n        int low = *min_element(power.begin(), power.end());\n\
        \        int high = *max_element(power.begin(), power.end()) + k;\n        while\
        \ (low < high) {\n            int mid = (low + high + 1) / 2;\n            vector<int>\
        \ remaining(k);\n            bool possible = true;\n            for (int i =\
        \ 0; i < n; i++) {\n                if (power[i] < mid) {\n                \
        \    int need = mid - power[i];\n                    for (int j = max(0, i -\
        \ r); j <= min(n - 1, i + r); j++) {\n                        if (remaining[j]\
        \ > 0) {\n                            int give = min(remaining[j], need);\n\
        \                            power[i] += give;\n                           \
        \ remaining[j] -= give;\n                            need -= give;\n       \
        \                 }\n                    }\n                    if (need > 0)\
        \ {\n                        possible = false;\n                        break;\n\
        \                    }\n                }\n            }\n            if (possible)\
        \ {\n                low = mid;\n            } else {\n                high\
        \ = mid - 1;\n            }\n        }\n        return low;\n    }\n};"
      java: "class Solution {\n    public int maxPower(int[] stations, int r, int k)\
        \ {\n        int n = stations.length;\n        int[] power = new int[n];\n \
        \       for (int i = 0; i < n; i++) {\n            for (int j = Math.max(0,\
        \ i - r); j <= Math.min(n - 1, i + r); j++) {\n                power[i] += stations[j];\n\
        \            }\n        }\n        int low = Integer.MAX_VALUE;\n        int\
        \ high = 0;\n        for (int i = 0; i < n; i++) {\n            low = Math.min(low,\
        \ power[i]);\n            high = Math.max(high, power[i] + k);\n        }\n\
        \        while (low < high) {\n            int mid = (low + high + 1) / 2;\n\
        \            int[] remaining = new int[k];\n            boolean possible = true;\n\
        \            for (int i = 0; i < n; i++) {\n                if (power[i] < mid)\
        \ {\n                    int need = mid - power[i];\n                    for\
        \ (int j = Math.max(0, i - r); j <= Math.min(n - 1, i + r); j++) {\n       \
        \                 if (remaining[j] > 0) {\n                            int give\
        \ = Math.min(remaining[j], need);\n                            power[i] += give;\n\
        \                            remaining[j] -= give;\n                       \
        \     need -= give;\n                        }\n                    }\n    \
        \                if (need > 0) {\n                        possible = false;\n\
        \                        break;\n                    }\n                }\n\
        \            }\n            if (possible) {\n                low = mid;\n  \
        \          } else {\n                high = mid - 1;\n            }\n      \
        \  }\n        return low;\n    }\n};"
      python: "class Solution:\n    def maxPower(self, stations: list[int], r: int,\
        \ k: int) -> int:\n        n = len(stations)\n        power = [0] * n\n    \
        \    for i in range(n):\n            for j in range(max(0, i - r), min(n, i\
        \ + r + 1)):\n                power[i] += stations[j]\n        low = min(power)\n\
        \        high = max(power) + k\n        while low < high:\n            mid =\
        \ (low + high + 1) // 2\n            remaining = [0] * n\n            possible\
        \ = True\n            for i in range(n):\n                if power[i] < mid:\n\
        \                    need = mid - power[i]\n                    for j in range(max(0,\
        \ i - r), min(n, i + r + 1)):\n                        if remaining[j] > 0:\n\
        \                            give = min(remaining[j], need)\n              \
        \              power[i] += give\n                            remaining[j] -=\
        \ give\n                            need -= give\n                    if need\
        \ > 0:\n                        possible = False\n                        break\n\
        \            if possible:\n                low = mid\n            else:\n  \
        \              high = mid - 1\n        return low"
      python3: "class Solution:\n    def maxPower(self, stations: list[int], r: int,\
        \ k: int) -> int:\n        n = len(stations)\n        power = [0] * n\n    \
        \    for i in range(n):\n            for j in range(max(0, i - r), min(n, i\
        \ + r + 1)):\n                power[i] += stations[j]\n        low = min(power)\n\
        \        high = max(power) + k\n        while low < high:\n            mid =\
        \ (low + high + 1) // 2\n            remaining = [0] * n\n            possible\
        \ = True\n            for i in range(n):\n                if power[i] < mid:\n\
        \                    need = mid - power[i]\n                    for j in range(max(0,\
        \ i - r), min(n, i + r + 1)):\n                        if remaining[j] > 0:\n\
        \                            give = min(remaining[j], need)\n              \
        \              power[i] += give\n                            remaining[j] -=\
        \ give\n                            need -= give\n                    if need\
        \ > 0:\n                        possible = False\n                        break\n\
        \            if possible:\n                low = mid\n            else:\n  \
        \              high = mid - 1\n        return low"
      c: "#include <stdio.h>\n#include <stdlib.h>\n\nint maxPower(int* stations, int\
        \ stationsSize, int r, int k) {\n    int n = stationsSize;\n    int* power =\
        \ (int*)malloc(n * sizeof(int));\n    for (int i = 0; i < n; i++) {\n      \
        \  power[i] = 0;\n        for (int j = i - r; j <= i + r; j++) {\n         \
        \   if (j >= 0 && j < n) {\n                power[i] += stations[j];\n     \
        \       }\n        }\n    }\n    int low = power[0];\n    int high = power[0]\
        \ + k;\n    for (int i = 1; i < n; i++) {\n        low = (low < power[i]) ?\
        \ low : power[i];\n        high = (high > power[i] + k) ? high : power[i] +\
        \ k;\n    }\n    while (low < high) {\n        int mid = (low + high + 1) /\
        \ 2;\n        int* remaining = (int*)malloc(n * sizeof(int));\n        for (int\
        \ i = 0; i < n; i++) {\n            remaining[i] = 0;\n        }\n        int\
        \ possible = 1;\n        for (int i = 0; i < n; i++) {\n            if (power[i]\
        \ < mid) {\n                int need = mid - power[i];\n                for\
        \ (int j = i - r; j <= i + r; j++) {\n                    if (j >= 0 && j <\
        \ n) {\n                        if (remaining[j] > 0) {\n                  \
        \          int give = (remaining[j] < need) ? remaining[j] : need;\n       \
        \                     power[i] += give;\n                            remaining[j]\
        \ -= give;\n                            need -= give;\n                    \
        \    }\n                    }\n                }\n                if (need >\
        \ 0) {\n                    possible = 0;\n                    break;\n    \
        \            }\n            }\n        }\n        if (possible) {\n        \
        \    low = mid;\n        } else {\n            high = mid - 1;\n        }\n\
        \        free(remaining);\n    }\n    free(power);\n    return low;\n};"
      csharp: "using System;\n\npublic class Solution {\n    public int MaxPower(int[]\
        \ stations, int r, int k) {\n        int n = stations.Length;\n        int[]\
        \ power = new int[n];\n        for (int i = 0; i < n; i++) {\n            for\
        \ (int j = Math.Max(0, i - r); j <= Math.Min(n - 1, i + r); j++) {\n       \
        \         power[i] += stations[j];\n            }\n        }\n        int low\
        \ = int.MaxValue;\n        int high = 0;\n        for (int i = 0; i < n; i++)\
        \ {\n            low = Math.Min(low, power[i]);\n            high = Math.Max(high,\
        \ power[i] + k);\n        }\n        while (low < high) {\n            int mid\
        \ = (low + high + 1) / 2;\n            int[] remaining = new int[n];\n     \
        \       bool possible = true;\n            for (int i = 0; i < n; i++) {\n \
        \               if (power[i] < mid) {\n                    int need = mid -\
        \ power[i];\n                    for (int j = Math.Max(0, i - r); j <= Math.Min(n\
        \ - 1, i + r); j++) {\n                        if (remaining[j] > 0) {\n   \
        \                         int give = Math.Min(remaining[j], need);\n       \
        \                     power[i] += give;\n                            remaining[j]\
        \ -= give;\n                            need -= give;\n                    \
        \    }\n                    }\n                    if (need > 0) {\n       \
        \                 possible = false;\n                        break;\n      \
        \              }\n                }\n            }\n            if (possible)\
        \ {\n                low = mid;\n            } else {\n                high\
        \ = mid - 1;\n            }\n        }\n        return low;\n    }\n};"
      javascript: "function maxPower(stations, r, k) {\n    let n = stations.length;\n\
        \    let power = new Array(n).fill(0);\n    for (let i = 0; i < n; i++) {\n\
        \        for (let j = Math.max(0, i - r); j <= Math.min(n - 1, i + r); j++)\
        \ {\n            power[i] += stations[j];\n        }\n    }\n    let low = Math.min(...power);\n\
        \    let high = Math.max(...power) + k;\n    while (low < high) {\n        let\
        \ mid = Math.floor((low + high + 1) / 2);\n        let remaining = new Array(n).fill(0);\n\
        \        let possible = true;\n        for (let i = 0; i < n; i++) {\n     \
        \       if (power[i] < mid) {\n                let need = mid - power[i];\n\
        \                for (let j = Math.max(0, i - r); j <= Math.min(n - 1, i + r);\
        \ j++) {\n                    if (remaining[j] > 0) {\n                    \
        \    let give = Math.min(remaining[j], need);\n                        power[i]\
        \ += give;\n                        remaining[j] -= give;\n                \
        \        need -= give;\n                    }\n                }\n         \
        \       if (need > 0) {\n                    possible = false;\n           \
        \         break;\n                }\n            }\n        }\n        if (possible)\
        \ {\n            low = mid;\n        } else {\n            high = mid - 1;\n\
        \        }\n    }\n    return low;\n};"
      typescript: "function maxPower(stations: number[], r: number, k: number): number\
        \ {\n    let n = stations.length;\n    let power: number[] = new Array(n).fill(0);\n\
        \    for (let i = 0; i < n; i++) {\n        for (let j = Math.max(0, i - r);\
        \ j <= Math.min(n - 1, i + r); j++) {\n            power[i] += stations[j];\n\
        \        }\n    }\n    let low = Math.min(...power);\n    let high = Math.max(...power)\
        \ + k;\n    while (low < high) {\n        let mid = Math.floor((low + high +\
        \ 1) / 2);\n        let remaining: number[] = new Array(n).fill(0);\n      \
        \  let possible = true;\n        for (let i = 0; i < n; i++) {\n           \
        \ if (power[i] < mid) {\n                let need = mid - power[i];\n      \
        \          for (let j = Math.max(0, i - r); j <= Math.min(n - 1, i + r); j++)\
        \ {\n                    if (remaining[j] > 0) {\n                        let\
        \ give = Math.min(remaining[j], need);\n                        power[i] +=\
        \ give;\n                        remaining[j] -= give;\n                   \
        \     need -= give;\n                    }\n                }\n            \
        \    if (need > 0) {\n                    possible = false;\n              \
        \      break;\n                }\n            }\n        }\n        if (possible)\
        \ {\n            low = mid;\n        } else {\n            high = mid - 1;\n\
        \        }\n    }\n    return low;\n};"
      php: "function maxPower($stations, $r, $k) {\n    $n = count($stations);\n   \
        \ $power = array_fill(0, $n, 0);\n    for ($i = 0; $i < $n; $i++) {\n      \
        \  for ($j = max(0, $i - $r); $j <= min($n - 1, $i + $r); $j++) {\n        \
        \    $power[$i] += $stations[$j];\n        }\n    }\n    $low = min($power);\n\
        \    $high = max($power) + $k;\n    while ($low < $high) {\n        $mid = floor(($low\
        \ + $high + 1) / 2);\n        $remaining = array_fill(0, $n, 0);\n        $possible\
        \ = true;\n        for ($i = 0; $i < $n; $i++) {\n            if ($power[$i]\
        \ < $mid) {\n                $need = $mid - $power[$i];\n                for\
        \ ($j = max(0, $i - $r); $j <= min($n - 1, $i + $r); $j++) {\n             \
        \       if ($remaining[$j] > 0) {\n                        $give = min($remaining[$j],\
        \ $need);\n                        $power[$i] += $give;\n                  \
        \      $remaining[$j] -= $give;\n                        $need -= $give;\n \
        \                   }\n                }\n                if ($need > 0) {\n\
        \                    $possible = false;\n                    break;\n      \
        \          }\n            }\n        }\n        if ($possible) {\n         \
        \   $low = $mid;\n        } else {\n            $high = $mid - 1;\n        }\n\
        \    }\n    return $low;\n};"
      swift: "func maxPower(_ stations: [Int], _ r: Int, _ k: Int) -> Int {\n    let\
        \ n = stations.count\n    var power = [Int](repeating: 0, count: n)\n    for\
        \ i in 0..<n {\n        for j in max(0, i - r)...min(n - 1, i + r) {\n     \
        \       power[i] += stations[j]\n        }\n    }\n    var low = power.min()!\n\
        \    var high = power.max()! + k\n    while low < high {\n        let mid =\
        \ (low + high + 1) / 2\n        var remaining = [Int](repeating: 0, count: n)\n\
        \        var possible = true\n        for i in 0..<n {\n            if power[i]\
        \ < mid {\n                var need = mid - power[i]\n                for j\
        \ in max(0, i - r)...min(n - 1, i + r) {\n                    if remaining[j]\
        \ > 0 {\n                        let give = min(remaining[j], need)\n      \
        \                  power[i] += give\n                        remaining[j] -=\
        \ give\n                        need -= give\n                    }\n      \
        \          }\n                if need > 0 {\n                    possible =\
        \ false\n                    break\n                }\n            }\n     \
        \   }\n        if possible {\n            low = mid\n        } else {\n    \
        \        high = mid - 1\n        }\n    }\n    return low\n};"
      kotlin: "fun maxPower(stations: IntArray, r: Int, k: Int): Int {\n    val n =\
        \ stations.size\n    val power = IntArray(n)\n    for (i in 0 until n) {\n \
        \       for (j in maxOf(0, i - r) until minOf(n - 1, i + r + 1)) {\n       \
        \     power[i] += stations[j]\n        }\n    }\n    var low = power.minOrNull()!!\n\
        \    var high = power.maxOrNull()!! + k\n    while (low < high) {\n        val\
        \ mid = (low + high + 1) / 2\n        val remaining = IntArray(n)\n        var\
        \ possible = true\n        for (i in 0 until n) {\n            if (power[i]\
        \ < mid) {\n                var need = mid - power[i]\n                for (j\
        \ in maxOf(0, i - r) until minOf(n - 1, i + r + 1)) {\n                    if\
        \ (remaining[j] > 0) {\n                        val give = minOf(remaining[j],\
        \ need)\n                        power[i] += give\n                        remaining[j]\
        \ -= give\n                        need -= give\n                    }\n   \
        \             }\n                if (need > 0) {\n                    possible\
        \ = false\n                    break\n                }\n            }\n   \
        \     }\n        if (possible) {\n            low = mid\n        } else {\n\
        \            high = mid - 1\n        }\n    }\n    return low\n};"
      dart: "int maxPower(List<int> stations, int r, int k) {\n    int n = stations.length;\n\
        \    List<int> power = List<int>.filled(n, 0);\n    for (int i = 0; i < n; i++)\
        \ {\n        for (int j = max(0, i - r); j <= min(n - 1, i + r); j++) {\n  \
        \          power[i] += stations[j];\n        }\n    }\n    int low = power.reduce((a,\
        \ b) => a < b ? a : b);\n    int high = power.reduce((a, b) => a > b ? a : b)\
        \ + k;\n    while (low < high) {\n        int mid = (low + high + 1) ~/ 2;\n\
        \        List<int> remaining = List<int>.filled(n, 0);\n        bool possible\
        \ = true;\n        for (int i = 0; i < n; i++) {\n            if (power[i] <\
        \ mid) {\n                int need = mid - power[i];\n                for (int\
        \ j = max(0, i - r); j <= min(n - 1, i + r); j++) {\n                    if\
        \ (remaining[j] > 0) {\n                        int give = min(remaining[j],\
        \ need);\n                        power[i] += give;\n                      \
        \  remaining[j] -= give;\n                        need -= give;\n          \
        \          }\n                }\n                if (need > 0) {\n         \
        \           possible = false;\n                    break;\n                }\n\
        \            }\n        }\n        if (possible) {\n            low = mid;\n\
        \        } else {\n            high = mid - 1;\n        }\n    }\n    return\
        \ low;\n};"
      go: "package main\n\nimport (\n    \"fmt\"\n)\n\nfunc maxPower(stations []int,\
        \ r int, k int) int {\n    n := len(stations)\n    power := make([]int, n)\n\
        \    for i := 0; i < n; i++ {\n        for j := max(0, i-r); j <= min(n-1, i+r);\
        \ j++ {\n            power[i] += stations[j]\n        }\n    }\n    low := power[0]\n\
        \    high := power[0] + k\n    for i := 1; i < n; i++ {\n        if power[i]\
        \ < low {\n            low = power[i]\n        }\n        if power[i]+k > high\
        \ {\n            high = power[i] + k\n        }\n    }\n    for low < high {\n\
        \        mid := (low + high + 1) / 2\n        remaining := make([]int, n)\n\
        \        possible := true\n        for i := 0; i < n; i++ {\n            if\
        \ power[i] < mid {\n                need := mid - power[i]\n               \
        \ for j := max(0, i-r); j <= min(n-1, i+r); j++ {\n                    if remaining[j]\
        \ > 0 {\n                        give := min(remaining[j], need)\n         \
        \               power[i] += give\n                        remaining[j] -= give\n\
        \                        need -= give\n                    }\n             \
        \   }\n                if need > 0 {\n                    possible = false\n\
        \                    break\n                }\n            }\n        }\n  \
        \      if possible {\n            low = mid\n        } else {\n            high\
        \ = mid - 1\n        }\n    }\n    return low\n}\n\nfunc max(a, b int) int {\n\
        \    if a > b {\n        return a\n    }\n    return b\n}\n\nfunc min(a, b int)\
        \ int {\n    if a < b {\n        return a\n    }\n    return b\n};"
      ruby: "def max_power(stations, r, k)\n    n = stations.size\n    power = Array.new(n,\
        \ 0)\n    for i in 0...n\n        for j in [i - r, 0].max...[i + r + 1, n].min\n\
        \            power[i] += stations[j]\n        end\n    end\n    low = power.min\n\
        \    high = power.max + k\n    while low < high\n        mid = (low + high +\
        \ 1) / 2\n        remaining = Array.new(n, 0)\n        possible = true\n   \
        \     for i in 0...n\n            if power[i] < mid\n                need =\
        \ mid - power[i]\n                for j in [i - r, 0].max...[i + r, n - 1].min\n\
        \                    if remaining[j] > 0\n                        give = [remaining[j],\
        \ need].min\n                        power[i] += give\n                    \
        \    remaining[j] -= give\n                        need -= give\n          \
        \          end\n                end\n                if need > 0\n         \
        \           possible = false\n                    break\n                end\n\
        \            end\n        end\n        if possible\n            low = mid\n\
        \        else\n            high = mid - 1\n        end\n    end\n    low\nend;"
      scala: "object Solution {\n    def maxPower(stations: Array[Int], r: Int, k: Int):\
        \ Int = {\n        val n = stations.length\n        val power = Array.fill(n)(0)\n\
        \        for (i <- 0 until n) {\n            for (j <- math.max(0, i - r) to\
        \ math.min(n - 1, i + r)) {\n                power(i) += stations(j)\n     \
        \       }\n        }\n        var low = power.min\n        var high = power.max\
        \ + k\n        while (low < high) {\n            val mid = (low + high + 1)\
        \ / 2\n            val remaining = Array.fill(n)(0)\n            var possible\
        \ = true\n            for (i <- 0 until n) {\n                if (power(i) <\
        \ mid) {\n                    var need = mid - power(i)\n                  \
        \  for (j <- math.max(0, i - r) to math.min(n - 1, i + r)) {\n             \
        \           if (remaining(j) > 0) {\n                            val give =\
        \ math.min(remaining(j), need)\n                            power(i) += give\n\
        \                            remaining(j) -= give\n                        \
        \    need -= give\n                        }\n                    }\n      \
        \              if (need > 0) {\n                        possible = false\n \
        \                       break\n                    }\n                }\n  \
        \          }\n            if (possible) {\n                low = mid\n     \
        \       } else {\n                high = mid - 1\n            }\n        }\n\
        \        low\n    }\n};"
      rust: "fn max_power(stations: Vec<i32>, r: i32, k: i32) -> i32 {\n    let n =\
        \ stations.len();\n    let mut power: Vec<i32> = vec![0; n];\n    for i in 0..n\
        \ {\n        for j in (i as i32 - r).max(0)..=(i as i32 + r).min(n as i32 -\
        \ 1) {\n            power[i] += stations[j as usize];\n        }\n    }\n  \
        \  let mut low = *power.iter().min().unwrap();\n    let mut high = *power.iter().max().unwrap()\
        \ + k;\n    while low < high {\n        let mid = (low + high + 1) / 2;\n  \
        \      let mut remaining: Vec<i32> = vec![0; n];\n        let mut possible =\
        \ true;\n        for i in 0..n {\n            if power[i] < mid {\n        \
        \        let mut need = mid - power[i];\n                for j in (i as i32\
        \ - r).max(0)..=(i as i32 + r).min(n as i32 - 1) {\n                    if remaining[j\
        \ as usize] > 0 {\n                        let give = remaining[j as usize].min(need);\n\
        \                        power[i] += give;\n                        remaining[j\
        \ as usize] -= give;\n                        need -= give;\n              \
        \      }\n                }\n                if need > 0 {\n               \
        \     possible = false;\n                    break;\n                }\n   \
        \         }\n        }\n        if possible {\n            low = mid;\n    \
        \    } else {\n            high = mid - 1;\n        }\n    }\n    low\n};"
      racket: "#lang racket\n(define (max-power stations r k)\n  (let* ((n (length stations))\n\
        \         (power (make-list n 0)))\n    (for ((i (range n)))\n      (for ((j\
        \ (range (max 0 (- i r)) (min n (+ i r 1))))\n        (set! power (list-set\
        \ power i (+ (list-ref power i) (list-ref stations j))))))\n    (let loop ((low\
        \ (apply min power)) (high (+ (apply max power) k)))\n      (if (< low high)\n\
        \          (let ((mid (quotient (+ low high 1) 2)))\n            (let* ((remaining\
        \ (make-list n 0))\n                   (possible #t))\n              (for ((i\
        \ (range n)))\n                (when (< (list-ref power i) mid)\n          \
        \        (let ((need (- mid (list-ref power i))))\n                    (for\
        \ ((j (range (max 0 (- i r)) (min n (+ i r 1))))\n                      (when\
        \ (> (list-ref remaining j) 0)\n                        (let ((give (min (list-ref\
        \ remaining j) need)))\n                          (set! power (list-set power\
        \ i (+ (list-ref power i) give)))\n                          (set! remaining\
        \ (list-set remaining j (- (list-ref remaining j) give)))\n                \
        \          (set! need (- need give))))))\n                    (unless (zero?\
        \ need)\n                      (set! possible #f)\n                      (break))))\n\
        \                (when (not possible)\n                  (break)))\n       \
        \       (if possible\n                  (loop mid high)\n                  (loop\
        \ low (- mid 1)))))\n          low))));"
      erlang: "-module(max_power).\n-export([max_power/3]).\n\nmax_power(Stations, R,\
        \ K) ->\n    N = length(Stations),\n    Power = lists:duplicate(N, 0),\n   \
        \ lists:foldl(\n      fun(I, Acc) ->\n          lists:foldl(\n            fun(J,\
        \ Acc1) ->\n                lists:update(I, Acc1, element(I, Acc1) + lists:nth(J\
        \ + 1, Stations))\n            end,\n            Acc,\n            lists:seq(max(0,\
        \ I - R), min(N - 1, I + R)))\n      end,\n      Power,\n      lists:seq(0,\
        \ N - 1)),\n    Low = lists:min(Power),\n    High = lists:max(Power) + K,\n\
        \    loop(Low, High, Power, Stations, R, K).\n\nloop(Low, High, Power, Stations,\
        \ R, K) when Low < High ->\n    Mid = (Low + High + 1) div 2,\n    Remaining\
        \ = lists:duplicate(length(Power), 0),\n    case possible(Mid, Power, Remaining,\
        \ Stations, R, K) of\n        true -> loop(Mid, High, Power, Stations, R, K);\n\
        \        false -> loop(Low, Mid - 1, Power, Stations, R, K)\n    end;\nloop(Low,\
        \ _High, _Power, _Stations, _R, _K) ->\n    Low.\n\npossible(Mid, Power, Remaining,\
        \ Stations, R, K) ->\n    lists:foldl(\n      fun(I, Acc) ->\n          case\
        \ Acc of\n              false -> false;\n              true ->\n           \
        \       case element(I, Power) < Mid of\n                      true ->\n   \
        \                       Need = Mid - element(I, Power),\n                  \
        \        case lists:foldl(\n                                 fun(J, Acc1) ->\n\
        \                                     case Acc1 of\n                       \
        \                  {need, remaining} ->\n                                  \
        \           case element(J, remaining) of\n                                \
        \                 0 -> {need, remaining};\n                                \
        \                 _ ->\n                                                   \
        \  Give = min(element(J, remaining), need),\n                              \
        \                       {need - Give, lists:update(J, remaining, element(J,\
        \ remaining) - Give)}\n                                             end\n  \
        \                               end,\n                                 {Need,\
        \ Remaining},\n                                 lists:seq(max(0, I - R), min(length(Power)\
        \ - 1, I + R)))\n                           of\n                           \
        \   {0, _} -> true;\n                              _ -> false\n            \
        \              end;\n                      false -> true\n                 \
        \ end\n          end\n      end,\n      true,\n      lists:seq(0, length(Power)\
        \ - 1)).\n\nmax(A, B) when A > B -> A;\nmax(_A, B) -> B.\n\nmin(A, B) when A\
        \ < B -> A;\nmin(_A, B) -> B."
      elixir: "defmodule MaxPower do\n  def max_power(stations, r, k) do\n    n = length(stations)\n\
        \    power = Enum.to_list(0..n-1) |> Enum.map(fn _ -> 0 end)\n    power = Enum.reduce(0..n-1,\
        \ power, fn i, power ->\n      Enum.reduce(max(0, i - r)..min(n - 1, i + r),\
        \ power, fn j, power ->\n        List.update_at(power, i, &(&1 + Enum.at(stations,\
        \ j)))\n      end)\n    end)\n    low = Enum.min(power)\n    high = Enum.max(power)\
        \ + k\n    loop(low, high, power, stations, r, k)\n  end\n\n  defp loop(low,\
        \ high, power, stations, r, k) when low < high do\n    mid = div(low + high\
        \ + 1, 2)\n    remaining = Enum.to_list(0..length(power)-1) |> Enum.map(fn _\
        \ -> 0 end)\n    case possible(mid, power, remaining, stations, r, k) do\n \
        \     true -> loop(mid, high, power, stations, r, k)\n      false -> loop(low,\
        \ mid - 1, power, stations, r, k)\n    end\n  end\n\n  defp loop(low, _high,\
        \ _power, _stations, _r, _k), do: low\n\n  defp possible(mid, power, remaining,\
        \ stations, r, k) do\n    Enum.reduce(0..length(power)-1, true, fn i, acc ->\n\
        \      case acc do\n        false -> false\n        true ->\n          case\
        \ Enum.at(power, i) < mid do\n            true ->\n              need = mid\
        \ - Enum.at(power, i)\n              {need, remaining} = Enum.reduce(max(0,\
        \ i - r)..min(length(power) - 1, i + r), {need, remaining}, fn j, {need, remaining}\
        \ ->\n                case Enum.at(remaining, j) do\n                  0 ->\
        \ {need, remaining}\n                  _ ->\n                    give = min(Enum.at(remaining,\
        \ j), need)\n                    {need - give, List.update_at(remaining, j,\
        \ &(&1 - give))}\n                end\n              end)\n              case\
        \ need do\n                0 -> true\n                _ -> false\n         \
        \     end\n            false -> true\n          end\n      end\n    end)\n \
        \ end\n\n  defp max(a, b) when a > b, do: a\n  defp max(_a, b), do: b\n\n  defp\
        \ min(a, b) when a < b, do: a\n  defp min(_a, b), do: b"
    approach: The problem can be solved using a combination of line sweep and binary
      search. First, we calculate the initial power of each city by considering the
      existing power stations. Then, we use binary search to find the maximum possible
      minimum power of a city. In each iteration of the binary search, we check if it's
      possible to achieve the current minimum power by building the additional power
      stations. If it's possible, we update the minimum power and continue the binary
      search. If it's not possible, we decrease the minimum power and continue the binary
      search. The process continues until we find the maximum possible minimum power
      of a city.
    time_complexity: O(n log m) where n is the number of cities and m is the maximum
      possible minimum power of a city. The time complexity is dominated by the binary
      search, which takes O(log m) time. Inside the binary search, we iterate over the
      cities to check if it's possible to achieve the current minimum power, which takes
      O(n) time.
    space_complexity: O(n) where n is the number of cities. We need to store the initial
      power of each city and the additional power stations that can be built in each
      city.
    elapsed_time: 15.919591665267944
    model: llama-3.3-70b-versatile
    generated_at: '2025-11-24 20:42:19 '
---

## Problem #2528: Maximize the Minimum Powered City

**Difficulty:** Hard

**Topics:** Array, Binary Search, Greedy, Queue, Sliding Window, Prefix Sum

## Problem Description

<p>You are given a <strong>0-indexed</strong> integer array <code>stations</code> of length <code>n</code>, where <code>stations[i]</code> represents the number of power stations in the <code>i<sup>th</sup></code> city.</p>

<p>Each power station can provide power to every city in a fixed <strong>range</strong>. In other words, if the range is denoted by <code>r</code>, then a power station at city <code>i</code> can provide power to all cities <code>j</code> such that <code>|i - j| &lt;= r</code> and <code>0 &lt;= i, j &lt;= n - 1</code>.</p>

<ul>
	<li>Note that <code>|x|</code> denotes <strong>absolute</strong> value. For example, <code>|7 - 5| = 2</code> and <code>|3 - 10| = 7</code>.</li>
</ul>

<p>The <strong>power</strong> of a city is the total number of power stations it is being provided power from.</p>

<p>The government has sanctioned building <code>k</code> more power stations, each of which can be built in any city, and have the same range as the pre-existing ones.</p>

<p>Given the two integers <code>r</code> and <code>k</code>, return <em>the <strong>maximum possible minimum power</strong> of a city, if the additional power stations are built optimally.</em></p>

<p><strong>Note</strong> that you can build the <code>k</code> power stations in multiple cities.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> stations = [1,2,4,5,0], r = 1, k = 2
<strong>Output:</strong> 5
<strong>Explanation:</strong> 
One of the optimal ways is to install both the power stations at city 1. 
So stations will become [1,4,4,5,0].
- City 0 is provided by 1 + 4 = 5 power stations.
- City 1 is provided by 1 + 4 + 4 = 9 power stations.
- City 2 is provided by 4 + 4 + 5 = 13 power stations.
- City 3 is provided by 5 + 4 = 9 power stations.
- City 4 is provided by 5 + 0 = 5 power stations.
So the minimum power of a city is 5.
Since it is not possible to obtain a larger power, we return 5.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> stations = [4,4,4,4], r = 0, k = 3
<strong>Output:</strong> 4
<strong>Explanation:</strong> 
It can be proved that we cannot make the minimum power of a city greater than 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == stations.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= stations[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= r&nbsp;&lt;= n - 1</code></li>
	<li><code>0 &lt;= k&nbsp;&lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. Pre calculate the number of stations on each city using Line Sweep.

2. Use binary search to maximize the minimum.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-24 20:42:03 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to maximize the minimum power of any city by adding at most `k` power stations. This is a classic "maximize the minimum" type problem, which can typically be solved using binary search on the answer. We can binary search for the maximum possible minimum power `X` that can be achieved for all cities. The `check(X)` function will determine if it's possible to make every city have at least `X` power using at most `k` additional stations.

The `check(X)` function employs a greedy strategy combined with a difference array (or sweep-line) technique for efficient power calculation. First, we need to calculate the initial power provided to each city by the existing `stations`. A naive approach of summing stations within range `r` for each city would be O(N*R), which is too slow. Instead, we use a difference array `diff_initial`. For each station `stations[s_idx]`, it contributes power to cities in the range `[max(0, s_idx - r), min(n-1, s_idx + r)]`. We mark the start of its contribution by adding `stations[s_idx]` at `diff_initial[max(0, s_idx - r)]` and the end by subtracting `stations[s_idx]` at `diff_initial[min(n-1, s_idx + r) + 1]`.

Next, we iterate through each city `i` from `0` to `n-1`. We maintain a running sum of `diff_initial` to get the current power from existing stations. Simultaneously, we maintain another running sum for `diff_for_new_stations`, which tracks the power contributed by stations we've added greedily so far. If the total power for city `i` (initial + added) is less than `X`, we must add more stations. To do this optimally, we calculate `needed = X - total_power_at_i`. We then add `needed` to our `added_k_count`. If `added_k_count` exceeds `k`, it's impossible to achieve `X`, so we return `False`. Otherwise, we place these `needed` stations. The most greedy strategy to cover city `i` and maximize their impact on subsequent cities is to place them as far right as possible while still covering city `i`. This optimal placement is at city `min(n-1, i+r)`. A station placed at `placement_idx` contributes power to cities in the range `[max(0, placement_idx - r), min(n-1, placement_idx + r)]`. With `placement_idx = min(n-1, i+r)`, these `needed` stations will contribute power to cities in the range `[max(0, i), min(n-1, i+2*r)]`. We update `diff_for_new_stations` by adding `needed` at index `i` and subtracting `needed` at index `min(n-1, i+2*r) + 1`. We also immediately update the `current_added_power_effect` for city `i` by adding `needed` to reflect the newly placed stations. After iterating through all cities, if we haven't exceeded `k` stations, we return `True`.

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
    bool check(long long target_power, int n, int r, long long k, const std::vector<int>& stations) {
        std::vector<long long> diff_initial(n + 1, 0);
        std::vector<long long> diff_for_new_stations(n + 1, 0);

        for (int i = 0; i < n; ++i) {
            long long val = stations[i];
            int start_idx = std::max(0, i - r);
            int end_idx = std::min(n - 1, i + r);

            diff_initial[start_idx] += val;
            if (end_idx + 1 < n + 1) {
                diff_initial[end_idx + 1] -= val;
            }
        }

        long long current_total_power_sum = 0;
        long long current_added_power_effect = 0;
        long long added_k_count = 0;

        for (int i = 0; i < n; ++i) {
            current_total_power_sum += diff_initial[i];
            current_added_power_effect += diff_for_new_stations[i];

            long long total_power_at_i = current_total_power_sum + current_added_power_effect;

            if (total_power_at_i < target_power) {
                long long needed = target_power - total_power_at_i;
                added_k_count += needed;

                if (added_k_count > k) {
                    return false;
                }

                diff_for_new_stations[i] += needed;
                int end_effect_idx = std::min(n - 1, i + 2 * r);
                if (end_effect_idx + 1 < n + 1) {
                    diff_for_new_stations[end_effect_idx + 1] -= needed;
                }

                current_added_power_effect += needed;
            }
        }

        return true;
    }

    long long maxPower(std::vector<int>& stations, int r, long long k) {
        int n = stations.size();

        long long low = 0;
        long long high = 2LL * 10000000000LL + 1000000000LL; // Max initial power + max k
        long long ans = 0;

        while (low <= high) {
            long long mid = low + (high - low) / 2;
            if (check(mid, n, r, k, stations)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
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
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public long maxPower(int[] stations, int r, long k) {
        int n = stations.length;

        long low = 0;
        long high = 2L * 10000000000L + 1000000000L; // Max initial power + max k
        long ans = 0;

        while (low <= high) {
            long mid = low + (high - low) / 2;
            if (check(mid, n, r, k, stations)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return ans;
    }

    private boolean check(long targetPower, int n, int r, long k, int[] stations) {
        long[] diffInitial = new long[n + 1];
        long[] diffForNewStations = new long[n + 1];

        for (int i = 0; i < n; ++i) {
            long val = stations[i];
            int startIdx = Math.max(0, i - r);
            int endIdx = Math.min(n - 1, i + r);

            diffInitial[startIdx] += val;
            if (endIdx + 1 < n + 1) {
                diffInitial[endIdx + 1] -= val;
            }
        }

        long currentTotalPowerSum = 0;
        long currentAddedPowerEffect = 0;
        long addedKCount = 0;

        for (int i = 0; i < n; ++i) {
            currentTotalPowerSum += diffInitial[i];
            currentAddedPowerEffect += diffForNewStations[i];

            long totalPowerAtI = currentTotalPowerSum + currentAddedPowerEffect;

            if (totalPowerAtI < targetPower) {
                long needed = targetPower - totalPowerAtI;
                addedKCount += needed;

                if (addedKCount > k) {
                    return false;
                }

                diffForNewStations[i] += needed;
                int endEffectIdx = Math.min(n - 1, i + 2 * r);
                if (endEffectIdx + 1 < n + 1) {
                    diffForNewStations[endEffectIdx + 1] -= needed;
                }

                currentAddedPowerEffect += needed;
            }
        }

        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)

        def check(target_power: int) -> bool:
            diff_initial = [0] * (n + 1)
            diff_for_new_stations = [0] * (n + 1)

            for i in range(n):
                val = stations[i]
                start_idx = max(0, i - r)
                end_idx = min(n - 1, i + r)

                diff_initial[start_idx] += val
                if end_idx + 1 < n + 1:
                    diff_initial[end_idx + 1] -= val

            current_total_power_sum = 0
            current_added_power_effect = 0
            added_k_count = 0

            for i in range(n):
                current_total_power_sum += diff_initial[i]
                current_added_power_effect += diff_for_new_stations[i]

                total_power_at_i = current_total_power_sum + current_added_power_effect

                if total_power_at_i < target_power:
                    needed = target_power - total_power_at_i
                    added_k_count += needed

                    if added_k_count > k:
                        return False

                    diff_for_new_stations[i] += needed
                    end_effect_idx = min(n - 1, i + 2 * r)
                    if end_effect_idx + 1 < n + 1:
                        diff_for_new_stations[end_effect_idx + 1] -= needed

                    current_added_power_effect += needed

            return True

        low = 0
        high = 2 * 10**10 + 10**9 # A sufficiently large upper bound
        ans = 0

        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)

        def check(target_power: int) -> bool:
            diff_initial = [0] * (n + 1)
            diff_for_new_stations = [0] * (n + 1)

            for i in range(n):
                val = stations[i]
                start_idx = max(0, i - r)
                end_idx = min(n - 1, i + r)

                diff_initial[start_idx] += val
                if end_idx + 1 < n + 1:
                    diff_initial[end_idx + 1] -= val

            current_total_power_sum = 0
            current_added_power_effect = 0
            added_k_count = 0

            for i in range(n):
                current_total_power_sum += diff_initial[i]
                current_added_power_effect += diff_for_new_stations[i]

                total_power_at_i = current_total_power_sum + current_added_power_effect

                if total_power_at_i < target_power:
                    needed = target_power - total_power_at_i
                    added_k_count += needed

                    if added_k_count > k:
                        return False

                    diff_for_new_stations[i] += needed
                    end_effect_idx = min(n - 1, i + 2 * r)
                    if end_effect_idx + 1 < n + 1:
                        diff_for_new_stations[end_effect_idx + 1] -= needed

                    current_added_power_effect += needed

            return True

        low = 0
        high = 2 * 10**10 + 10**9 # A sufficiently large upper bound
        ans = 0

        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <stdbool.h>

// Helper function for max
long long max(long long a, long long b) {
    return a > b ? a : b;
}

// Helper function for min
long long min(long long a, long long b) {
    return a < b ? a : b;
}

// check function to determine if a target_power is achievable
bool check(long long target_power, int n, int r, long long k, int* stations) {
    long long* diff_initial = (long long*)calloc(n + 1, sizeof(long long));
    long long* diff_for_new_stations = (long long*)calloc(n + 1, sizeof(long long));

    if (!diff_initial || !diff_for_new_stations) {
        // Handle memory allocation failure
        free(diff_initial);
        free(diff_for_new_stations);
        return false; // Or throw an error, depending on context
    }

    for (int i = 0; i < n; ++i) {
        long long val = stations[i];
        int start_idx = max(0, i - r);
        int end_idx = min(n - 1, i + r);

        diff_initial[start_idx] += val;
        if (end_idx + 1 < n + 1) {
            diff_initial[end_idx + 1] -= val;
        }
    }

    long long current_total_power_sum = 0;
    long long current_added_power_effect = 0;
    long long added_k_count = 0;

    for (int i = 0; i < n; ++i) {
        current_total_power_sum += diff_initial[i];
        current_added_power_effect += diff_for_new_stations[i];

        long long total_power_at_i = current_total_power_sum + current_added_power_effect;

        if (total_power_at_i < target_power) {
            long long needed = target_power - total_power_at_i;
            added_k_count += needed;

            if (added_k_count > k) {
                free(diff_initial);
                free(diff_for_new_stations);
                return false;
            }

            diff_for_new_stations[i] += needed;
            int end_effect_idx = min(n - 1, i + 2 * r);
            if (end_effect_idx + 1 < n + 1) {
                diff_for_new_stations[end_effect_idx + 1] -= needed;
            }

            current_added_power_effect += needed;
        }
    }

    free(diff_initial);
    free(diff_for_new_stations);
    return true;
}

// Main function for LeetCode problem
long long maxPower(int* stations, int stationsSize, int r, long long k) {
    int n = stationsSize;

    long long low = 0;
    long long high = 2LL * 10000000000LL + 1000000000LL; // Max initial power + max k
    long long ans = 0;

    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid, n, r, k, stations)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
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
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public long MaxPower(int[] stations, int r, long k) {
        int n = stations.Length;

        long low = 0;
        long high = 2L * 10_000_000_000L + 1_000_000_000L; // Max initial power + max k
        long ans = 0;

        while (low <= high) {
            long mid = low + (high - low) / 2;
            if (Check(mid, n, r, k, stations)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return ans;
    }

    private bool Check(long targetPower, int n, int r, long k, int[] stations) {
        long[] diffInitial = new long[n + 1];
        long[] diffForNewStations = new long[n + 1];

        for (int i = 0; i < n; ++i) {
            long val = stations[i];
            int startIdx = Math.Max(0, i - r);
            int endIdx = Math.Min(n - 1, i + r);

            diffInitial[startIdx] += val;
            if (endIdx + 1 < n + 1) {
                diffInitial[endIdx + 1] -= val;
            }
        }

        long currentTotalPowerSum = 0;
        long currentAddedPowerEffect = 0;
        long addedKCount = 0;

        for (int i = 0; i < n; ++i) {
            currentTotalPowerSum += diffInitial[i];
            currentAddedPowerEffect += diffForNewStations[i];

            long totalPowerAtI = currentTotalPowerSum + currentAddedPowerEffect;

            if (totalPowerAtI < targetPower) {
                long needed = targetPower - totalPowerAtI;
                addedKCount += needed;

                if (addedKCount > k) {
                    return false;
                }

                diffForNewStations[i] += needed;
                int endEffectIdx = Math.Min(n - 1, i + 2 * r);
                if (endEffectIdx + 1 < n + 1) {
                    diffForNewStations[endEffectIdx + 1] -= needed;
                }

                currentAddedPowerEffect += needed;
            }
        }

        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} stations
 * @param {number} r
 * @param {number} k
 * @return {number}
 */
var maxPower = function(stations, r, k) {
    const n = stations.length;

    const check = (target_power) => {
        const diff_initial = new Array(n + 1).fill(0);
        const diff_for_new_stations = new Array(n + 1).fill(0);

        for (let i = 0; i < n; ++i) {
            const val = stations[i];
            const start_idx = Math.max(0, i - r);
            const end_idx = Math.min(n - 1, i + r);

            diff_initial[start_idx] += val;
            if (end_idx + 1 < n + 1) {
                diff_initial[end_idx + 1] -= val;
            }
        }

        let current_total_power_sum = 0;
        let current_added_power_effect = 0;
        let added_k_count = 0;

        for (let i = 0; i < n; ++i) {
            current_total_power_sum += diff_initial[i];
            current_added_power_effect += diff_for_new_stations[i];

            const total_power_at_i = current_total_power_sum + current_added_power_effect;

            if (total_power_at_i < target_power) {
                const needed = target_power - total_power_at_i;
                added_k_count += needed;

                if (added_k_count > k) {
                    return false;
                }

                diff_for_new_stations[i] += needed;
                const end_effect_idx = Math.min(n - 1, i + 2 * r);
                if (end_effect_idx + 1 < n + 1) {
                    diff_for_new_stations[end_effect_idx + 1] -= needed;
                }

                current_added_power_effect += needed;
            }
        }

        return true;
    };

    let low = 0;
    let high = 2 * 10**10 + 10**9; // A sufficiently large upper bound
    let ans = 0;

    while (low <= high) {
        const mid = Math.floor(low + (high - low) / 2);
        if (check(mid)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
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
function maxPower(stations: number[], r: number, k: number): number {
    const n = stations.length;

    const check = (target_power: number): boolean => {
        const diff_initial: number[] = new Array(n + 1).fill(0);
        const diff_for_new_stations: number[] = new Array(n + 1).fill(0);

        for (let i = 0; i < n; ++i) {
            const val = stations[i];
            const start_idx = Math.max(0, i - r);
            const end_idx = Math.min(n - 1, i + r);

            diff_initial[start_idx] += val;
            if (end_idx + 1 < n + 1) {
                diff_initial[end_idx + 1] -= val;
            }
        }

        let current_total_power_sum = 0;
        let current_added_power_effect = 0;
        let added_k_count = 0;

        for (let i = 0; i < n; ++i) {
            current_total_power_sum += diff_initial[i];
            current_added_power_effect += diff_for_new_stations[i];

            const total_power_at_i = current_total_power_sum + current_added_power_effect;

            if (total_power_at_i < target_power) {
                const needed = target_power - total_power_at_i;
                added_k_count += needed;

                if (added_k_count > k) {
                    return false;
                }

                diff_for_new_stations[i] += needed;
                const end_effect_idx = Math.min(n - 1, i + 2 * r);
                if (end_effect_idx + 1 < n + 1) {
                    diff_for_new_stations[end_effect_idx + 1] -= needed;
                }

                current_added_power_effect += needed;
            }
        }

        return true;
    };

    let low = 0;
    let high = 2 * 10**10 + 10**9; // A sufficiently large upper bound
    let ans = 0;

    while (low <= high) {
        const mid = Math.floor(low + (high - low) / 2);
        if (check(mid)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $stations
     * @param Integer $r
     * @param Integer $k
     * @return Integer
     */
    function maxPower($stations, $r, $k) {
        $n = count($stations);

        $check = function($target_power) use ($n, $r, $k, $stations) {
            $diff_initial = array_fill(0, $n + 1, 0);
            $diff_for_new_stations = array_fill(0, $n + 1, 0);

            for ($i = 0; $i < $n; ++$i) {
                $val = $stations[$i];
                $start_idx = max(0, $i - $r);
                $end_idx = min($n - 1, $i + $r);

                $diff_initial[$start_idx] += $val;
                if ($end_idx + 1 < $n + 1) {
                    $diff_initial[$end_idx + 1] -= $val;
                }
            }

            $current_total_power_sum = 0;
            $current_added_power_effect = 0;
            $added_k_count = 0;

            for ($i = 0; $i < $n; ++$i) {
                $current_total_power_sum += $diff_initial[$i];
                $current_added_power_effect += $diff_for_new_stations[$i];

                $total_power_at_i = $current_total_power_sum + $current_added_power_effect;

                if ($total_power_at_i < $target_power) {
                    $needed = $target_power - $total_power_at_i;
                    $added_k_count += $needed;

                    if ($added_k_count > $k) {
                        return false;
                    }

                    $diff_for_new_stations[$i] += $needed;
                    $end_effect_idx = min($n - 1, $i + 2 * $r);
                    if ($end_effect_idx + 1 < $n + 1) {
                        $diff_for_new_stations[$end_effect_idx + 1] -= $needed;
                    }

                    $current_added_power_effect += $needed;
                }
            }

            return true;
        };

        $low = 0;
        $high = 2 * 10**10 + 10**9; // A sufficiently large upper bound
        $ans = 0;

        while ($low <= $high) {
            $mid = floor($low + ($high - $low) / 2);
            if ($check($mid)) {
                $ans = $mid;
                $low = $mid + 1;
            } else {
                $high = $mid - 1;
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
    func maxPower(_ stations: [Int], _ r: Int, _ k: Int) -> Int {
        let n = stations.count

        func check(_ target_power: Int) -> Bool {
            var diff_initial = Array(repeating: 0, count: n + 1)
            var diff_for_new_stations = Array(repeating: 0, count: n + 1)

            for i in 0..<n {
                let val = stations[i]
                let start_idx = max(0, i - r)
                let end_idx = min(n - 1, i + r)

                diff_initial[start_idx] += val
                if end_idx + 1 < n + 1 {
                    diff_initial[end_idx + 1] -= val
                }
            }

            var current_total_power_sum = 0
            var current_added_power_effect = 0
            var added_k_count = 0

            for i in 0..<n {
                current_total_power_sum += diff_initial[i]
                current_added_power_effect += diff_for_new_stations[i]

                let total_power_at_i = current_total_power_sum + current_added_power_effect

                if total_power_at_i < target_power {
                    let needed = target_power - total_power_at_i
                    added_k_count += needed

                    if added_k_count > k {
                        return false
                    }

                    diff_for_new_stations[i] += needed
                    let end_effect_idx = min(n - 1, i + 2 * r)
                    if end_effect_idx + 1 < n + 1 {
                        diff_for_new_stations[end_effect_idx + 1] -= needed
                    }

                    current_added_power_effect += needed
                }
            }

            return true
        }

        var low = 0
        var high = 2 * 10_000_000_000 + 1_000_000_000 // A sufficiently large upper bound
        var ans = 0

        while low <= high {
            let mid = low + (high - low) / 2
            if check(mid) {
                ans = mid
                low = mid + 1
            } else {
                high = mid - 1
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
import kotlin.math.max
import kotlin.math.min

class Solution {
    fun maxPower(stations: IntArray, r: Int, k: Long): Long {
        val n = stations.size

        fun check(target_power: Long): Boolean {
            val diffInitial = LongArray(n + 1) { 0L }
            val diffForNewStations = LongArray(n + 1) { 0L }

            for (i in 0 until n) {
                val val_ = stations[i].toLong()
                val start_idx = max(0, i - r)
                val end_idx = min(n - 1, i + r)

                diffInitial[start_idx] += val_
                if (end_idx + 1 < n + 1) {
                    diffInitial[end_idx + 1] -= val_
                }
            }

            var currentTotalPowerSum = 0L
            var currentAddedPowerEffect = 0L
            var addedKCount = 0L

            for (i in 0 until n) {
                currentTotalPowerSum += diffInitial[i]
                currentAddedPowerEffect += diffForNewStations[i]

                val totalPowerAtI = currentTotalPowerSum + currentAddedPowerEffect

                if (totalPowerAtI < target_power) {
                    val needed = target_power - totalPowerAtI
                    addedKCount += needed

                    if (addedKCount > k) {
                        return false
                    }

                    diffForNewStations[i] += needed
                    val endEffectIdx = min(n - 1, i + 2 * r)
                    if (endEffectIdx + 1 < n + 1) {
                        diffForNewStations[endEffectIdx + 1] -= needed
                    }

                    currentAddedPowerEffect += needed
                }
            }

            return true
        }

        var low = 0L
        var high = 2L * 10_000_000_000L + 1_000_000_000L // A sufficiently large upper bound
        var ans = 0L

        while (low <= high) {
            val mid = low + (high - low) / 2
            if (check(mid)) {
                ans = mid
                low = mid + 1
            } else {
                high = mid - 1
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
import 'dart:math';

class Solution {
  int maxPower(List<int> stations, int r, int k) {
    final n = stations.length;

    bool check(int targetPower) {
      final diffInitial = List<int>.filled(n + 1, 0);
      final diffForNewStations = List<int>.filled(n + 1, 0);

      for (int i = 0; i < n; ++i) {
        final val = stations[i];
        final startIdx = max(0, i - r);
        final endIdx = min(n - 1, i + r);

        diffInitial[startIdx] += val;
        if (endIdx + 1 < n + 1) {
          diffInitial[endIdx + 1] -= val;
        }
      }

      int currentTotalPowerSum = 0;
      int currentAddedPowerEffect = 0;
      int addedKCount = 0;

      for (int i = 0; i < n; ++i) {
        currentTotalPowerSum += diffInitial[i];
        currentAddedPowerEffect += diffForNewStations[i];

        final totalPowerAtI = currentTotalPowerSum + currentAddedPowerEffect;

        if (totalPowerAtI < targetPower) {
          final needed = targetPower - totalPowerAtI;
          addedKCount += needed;

          if (addedKCount > k) {
            return false;
          }

          diffForNewStations[i] += needed;
          final endEffectIdx = min(n - 1, i + 2 * r);
          if (endEffectIdx + 1 < n + 1) {
            diffForNewStations[endEffectIdx + 1] -= needed;
          }

          currentAddedPowerEffect += needed;
        }
      }

      return true;
    }

    int low = 0;
    int high = 2 * pow(10, 10).toInt() + pow(10, 9).toInt(); // A sufficiently large upper bound
    int ans = 0;

    while (low <= high) {
      final mid = low + ((high - low) ~/ 2);
      if (check(mid)) {
        ans = mid;
        low = mid + 1;
      } else {
        high = mid - 1;
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
package main

import (
	"math"
)

func maxPower(stations []int, r int, k int) int {
	n := len(stations)

	check := func(targetPower int) bool {
		diffInitial := make([]int, n+1)
		diffForNewStations := make([]int, n+1)

		for i := 0; i < n; i++ {
			val := stations[i]
			startIdx := int(math.Max(0, float64(i-r)))
			endIdx := int(math.Min(float64(n-1), float64(i+r)))

			diffInitial[startIdx] += val
			if endIdx+1 < n+1 {
				diffInitial[endIdx+1] -= val
			}
		}

		currentTotalPowerSum := 0
		currentAddedPowerEffect := 0
		addedKCount := 0

		for i := 0; i < n; i++ {
			currentTotalPowerSum += diffInitial[i]
			currentAddedPowerEffect += diffForNewStations[i]

			totalPowerAtI := currentTotalPowerSum + currentAddedPowerEffect

			if totalPowerAtI < targetPower {
				needed := targetPower - totalPowerAtI
				addedKCount += needed

				if addedKCount > k {
					return false
				}

				diffForNewStations[i] += needed
				endEffectIdx := int(math.Min(float64(n-1), float64(i+2*r)))
				if endEffectIdx+1 < n+1 {
					diffForNewStations[endEffectIdx+1] -= needed
				}

				currentAddedPowerEffect += needed
			}
		}

		return true
	}

	low := 0
	high := 2*10000000000 + 1000000000 // A sufficiently large upper bound
	ans := 0

	for low <= high {
		mid := low + (high-low)/2
		if check(mid) {
			ans = mid
			low = mid + 1
		} else {
			high = mid - 1
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
class Solution
    # @param {Integer[]} stations
    # @param {Integer} r
    # @param {Integer} k
    # @return {Integer}
    def max_power(stations, r, k)
        n = stations.length

        check = lambda target_power do
            diff_initial = Array.new(n + 1, 0)
            diff_for_new_stations = Array.new(n + 1, 0)

            stations.each_with_index do |val, i|
                start_idx = [0, i - r].max
                end_idx = [n - 1, i + r].min

                diff_initial[start_idx] += val
                if end_idx + 1 < n + 1
                    diff_initial[end_idx + 1] -= val
                end
            end

            current_total_power_sum = 0
            current_added_power_effect = 0
            added_k_count = 0

            n.times do |i|
                current_total_power_sum += diff_initial[i]
                current_added_power_effect += diff_for_new_stations[i]

                total_power_at_i = current_total_power_sum + current_added_power_effect

                if total_power_at_i < target_power
                    needed = target_power - total_power_at_i
                    added_k_count += needed

                    if added_k_count > k
                        return false
                    end

                    diff_for_new_stations[i] += needed
                    end_effect_idx = [n - 1, i + 2 * r].min
                    if end_effect_idx + 1 < n + 1
                        diff_for_new_stations[end_effect_idx + 1] -= needed
                    end

                    current_added_power_effect += needed
                end
            end

            true
        end

        low = 0
        high = 2 * 10**10 + 10**9 # A sufficiently large upper bound
        ans = 0

        while low <= high
            mid = low + (high - low) / 2
            if check.call(mid)
                ans = mid
                low = mid + 1
            else
                high = mid - 1
            end
        end

        ans
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
    def maxPower(stations: Array[Int], r: Int, k: Long): Long = {
        val n = stations.length

        def check(target_power: Long): Boolean = {
            val diffInitial = ArrayBuffer.fill(n + 1)(0L)
            val diffForNewStations = ArrayBuffer.fill(n + 1)(0L)

            for (i <- 0 until n) {
                val val_ = stations(i).toLong
                val start_idx = max(0, i - r)
                val end_idx = min(n - 1, i + r)

                diffInitial(start_idx) += val_
                if (end_idx + 1 < n + 1) {
                    diffInitial(end_idx + 1) -= val_
                }
            }

            var currentTotalPowerSum = 0L
            var currentAddedPowerEffect = 0L
            var addedKCount = 0L

            for (i <- 0 until n) {
                currentTotalPowerSum += diffInitial(i)
                currentAddedPowerEffect += diffForNewStations(i)

                val totalPowerAtI = currentTotalPowerSum + currentAddedPowerEffect

                if (totalPowerAtI < target_power) {
                    val needed = target_power - totalPowerAtI
                    addedKCount += needed

                    if (addedKCount > k) {
                        return false
                    }

                    diffForNewStations(i) += needed
                    val endEffectIdx = min(n - 1, i + 2 * r)
                    if (endEffectIdx + 1 < n + 1) {
                        diffForNewStations(endEffectIdx + 1) -= needed
                    }

                    currentAddedPowerEffect += needed
                }
            }

            true
        }

        var low = 0L
        var high = 2L * 10_000_000_000L + 1_000_000_000L // A sufficiently large upper bound
        var ans = 0L

        while (low <= high) {
            val mid = low + (high - low) / 2
            if (check(mid)) {
                ans = mid
                low = mid + 1
            } else {
                high = mid - 1
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
    pub fn max_power(stations: Vec<i32>, r: i32, k: i64) -> i64 {
        let n = stations.len();

        let check = |target_power: i64| -> bool {
            let mut diff_initial = vec![0i64; n + 1];
            let mut diff_for_new_stations = vec![0i64; n + 1];

            for i in 0..n {
                let val = stations[i] as i64;
                let start_idx = (0).max(i as i32 - r) as usize;
                let end_idx = (n as i32 - 1).min(i as i32 + r) as usize;

                diff_initial[start_idx] += val;
                if end_idx + 1 < n + 1 {
                    diff_initial[end_idx + 1] -= val;
                }
            }

            let mut current_total_power_sum = 0i64;
            let mut current_added_power_effect = 0i64;
            let mut added_k_count = 0i64;

            for i in 0..n {
                current_total_power_sum += diff_initial[i];
                current_added_power_effect += diff_for_new_stations[i];

                let total_power_at_i = current_total_power_sum + current_added_power_effect;

                if total_power_at_i < target_power {
                    let needed = target_power - total_power_at_i;
                    added_k_count += needed;

                    if added_k_count > k {
                        return false;
                    }

                    diff_for_new_stations[i] += needed;
                    let end_effect_idx = (n as i32 - 1).min(i as i32 + 2 * r) as usize;
                    if end_effect_idx + 1 < n + 1 {
                        diff_for_new_stations[end_effect_idx + 1] -= needed;
                    }

                    current_added_power_effect += needed;
                }
            }

            true
        };

        let mut low = 0i64;
        let mut high = 2 * 10_000_000_000i64 + 1_000_000_000i64; // A sufficiently large upper bound
        let mut ans = 0i64;

        while low <= high {
            let mid = low + (high - low) / 2;
            if check(mid) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (max-power stations r k)
  (define n (vector-length stations))

  (define (check-fixed target-power)
    (define diff-initial (make-vector (+ n 1) 0))
    (define diff-for-new-stations (make-vector (+ n 1) 0))

    (for ([i (in-range n)])
      (define val (vector-ref stations i))
      (define start-idx (max 0 (- i r)))
      (define end-idx (min (- n 1) (+ i r)))

      (vector-set! diff-initial start-idx (+ (vector-ref diff-initial start-idx) val))
      (when (< (+ end-idx 1) (+ n 1))
        (vector-set! diff-initial (+ end-idx 1) (- (vector-ref diff-initial (+ end-idx 1)) val))))

    (define current-total-power-sum 0)
    (define current-added-power-effect 0)
    (define added-k-count 0)

    (for ([i (in-range n)])
      (set! current-total-power-sum (+ current-total-power-sum (vector-ref diff-initial i)))
      (set! current-added-power-effect (+ current-added-power-effect (vector-ref diff-for-new-stations i)))

      (define total-power-at-i (+ current-total-power-sum current-added-power-effect))

      (when (< total-power-at-i target-power)
        (define needed (- target-power total-power-at-i))
        (set! added-k-count (+ added-k-count needed))

        (when (> added-k-count k)
          (return-from check-fixed #f)) ; Early exit for false

        (vector-set! diff-for-new-stations i (+ (vector-ref diff-for-new-stations i) needed))
        (define end-effect-idx (min (- n 1) (+ i (* 2 r))))
        (when (< (+ end-effect-idx 1) (+ n 1))
          (vector-set! diff-for-new-stations (+ end-effect-idx 1) (- (vector-ref diff-for-new-stations (+ end-effect-idx 1)) needed)))

        (set! current-added-power-effect (+ current-added-power-effect needed))))

    #t)

  (define low 0)
  (define high (+ (* 2 10000000000) 1000000000)) ; A sufficiently large upper bound
  (define ans 0)

  (let loop ((l low) (h high) (a ans))
    (if (<= l h)
        (let* ((mid (+ l (quotient (- h l) 2))))
          (if (check-fixed mid)
              (loop (+ mid 1) h mid)
              (loop l (- mid 1) a)))
        a)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([max_power/3]).

max_power(Stations, R, K) ->
    N = length(Stations),

    Check = fun(TargetPower) ->
        DiffInitial = array:new(N + 1, {default, 0}),
        DiffForNewStations = array:new(N + 1, {default, 0}),

        % Calculate initial power contributions from existing stations
        DiffInitial1 = lists:foldl(fun(I, AccDiffInitial) ->
            Val = lists:nth(I + 1, Stations),
            StartIdx = max(0, I - R),
            EndIdx = min(N - 1, I + R),

            AccDiffInitial2 = array:set(StartIdx, array:get(StartIdx, AccDiffInitial) + Val, AccDiffInitial),
            if (EndIdx + 1 < N + 1) ->
                array:set(EndIdx + 1, array:get(EndIdx + 1, AccDiffInitial2) - Val, AccDiffInitial2);
            true ->
                AccDiffInitial2
            end
        end, DiffInitial, lists:seq(0, N - 1)),

        CurrentTotalPowerSum = 0,
        CurrentAddedPowerEffect = 0,
        AddedKCount = 0,

        {_, _, _, Result} = lists:foldl(fun(I, {AccCurrentTotalPowerSum, AccCurrentAddedPowerEffect, AccAddedKCount, Possible}) ->
            if not Possible ->
                {AccCurrentTotalPowerSum, AccCurrentAddedPowerEffect, AccAddedKCount, Possible};
            true ->
                NewCurrentTotalPowerSum = AccCurrentTotalPowerSum + array:get(I, DiffInitial1),
                NewCurrentAddedPowerEffect = AccCurrentAddedPowerEffect + array:get(I, DiffForNewStations),

                TotalPowerAtI = NewCurrentTotalPowerSum + NewCurrentAddedPowerEffect,

                if (TotalPowerAtI < TargetPower) ->
                    Needed = TargetPower - TotalPowerAtI,
                    NewAddedKCount = AccAddedKCount + Needed,

                    if (NewAddedKCount > K) ->
                        {NewCurrentTotalPowerSum, NewCurrentAddedPowerEffect, NewAddedKCount, false};
                    true ->
                        DiffForNewStations1 = array:set(I, array:get(I, DiffForNewStations) + Needed, DiffForNewStations),
                        EndEffectIdx = min(N - 1, I + 2 * R),
                        DiffForNewStations2 = if (EndEffectIdx + 1 < N + 1) ->
                            array:set(EndEffectIdx + 1, array:get(EndEffectIdx + 1, DiffForNewStations1) - Needed, DiffForNewStations1);
                        true ->
                            DiffForNewStations1
                        end,
                        {NewCurrentTotalPowerSum, NewCurrentAddedPowerEffect + Needed, NewAddedKCount, true}
                    end;
                true ->
                    {NewCurrentTotalPowerSum, NewCurrentAddedPowerEffect, AccAddedKCount, true}
                end
            end
        end, {CurrentTotalPowerSum, CurrentAddedPowerEffect, AddedKCount, true}, lists:seq(0, N - 1)),

        Result
    end,

    Low = 0,
    High = 2 * 10000000000 + 1000000000, % A sufficiently large upper bound
    Ans = 0,

    binary_search(Low, High, Ans, Check).

binary_search(Low, High, Ans, Check) when Low =< High ->
    Mid = Low + (High - Low) div 2,
    case Check(Mid) of
        true ->
            binary_search(Mid + 1, High, Mid, Check);
        false ->
            binary_search(Low, Mid - 1, Ans, Check)
    end;
binary_search(_, _, Ans, _) ->
    Ans.

% Helper functions for max/min
max(A, B) when A >= B -> A;
max(A, B) -> B.

min(A, B) when A =< B -> A;
min(A, B) -> B.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_power(stations :: [integer], r :: integer, k :: integer) :: integer
  def max_power(stations, r, k) do
    n = length(stations)

    check = fn target_power ->
      diff_initial = :array.new(n + 1, default: 0)
      diff_for_new_stations = :array.new(n + 1, default: 0)

      # Calculate initial power contributions from existing stations
      diff_initial = Enum.reduce(0..(n - 1), diff_initial, fn i, acc_diff_initial ->
        val = Enum.at(stations, i)
        start_idx = max(0, i - r)
        end_idx = min(n - 1, i + r)

        acc_diff_initial_2 = :array.set(start_idx, :array.get(start_idx, acc_diff_initial) + val, acc_diff_initial)
        if end_idx + 1 < n + 1 do
          :array.set(end_idx + 1, :array.get(end_idx + 1, acc_diff_initial_2) - val, acc_diff_initial_2)
        else
          acc_diff_initial_2
        end
      end)

      current_total_power_sum = 0
      current_added_power_effect = 0
      added_k_count = 0

      {_final_sum, _final_effect, _final_k_count, possible} = Enum.reduce_while(0..(n - 1), {current_total_power_sum, current_added_power_effect, added_k_count, true}, fn i, {acc_current_total_power_sum, acc_current_added_power_effect, acc_added_k_count, current_possible} ->
        if not current_possible do
          {:halt, {acc_current_total_power_sum, acc_current_added_power_effect, acc_added_k_count, current_possible}}
        else
          new_current_total_power_sum = acc_current_total_power_sum + :array.get(i, diff_initial)
          new_current_added_power_effect = acc_current_added_power_effect + :array.get(i, diff_for_new_stations)

          total_power_at_i = new_current_total_power_sum + new_current_added_power_effect

          if total_power_at_i < target_power do
            needed = target_power - total_power_at_i
            new_added_k_count = acc_added_k_count + needed

            if new_added_k_count > k do
              {:halt, {new_current_total_power_sum, new_current_added_power_effect, new_added_k_count, false}}
            else
              :array.set(i, :array.get(i, diff_for_new_stations) + needed, diff_for_new_stations)
              end_effect_idx = min(n - 1, i + 2 * r)
              if end_effect_idx + 1 < n + 1 do
                :array.set(end_effect_idx + 1, :array.get(end_effect_idx + 1, diff_for_new_stations) - needed, diff_for_new_stations)
              else
                :ok # no change to diff_for_new_stations
              end
              {:cont, {new_current_total_power_sum, new_current_added_power_effect + needed, new_added_k_count, true}}
            end
          else
            {:cont, {new_current_total_power_sum, new_current_added_power_effect, acc_added_k_count, true}}
          end
        end
      end)
      possible
    end

    low = 0
    high = 2 * :math.pow(10, 10) |> round() + :math.pow(10, 9) |> round() # A sufficiently large upper bound
    ans = 0

    binary_search(low, high, ans, check)
  end

  defp binary_search(low, high, ans, check) when low <= high do
    mid = low + div(high - low, 2)
    if check.(mid) do
      binary_search(mid + 1, high, mid, check)
    else
      binary_search(low, mid - 1, ans, check)
    end
  end

  defp binary_search(_low, _high, ans, _check), do: ans

  defp max(a, b), do: if a >= b, do: a, else: b
  defp min(a, b), do: if a <= b, do: a, else: b
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N * log(MAX_POWER)).
- The `check` function iterates through the `n` cities once. Inside the loop, operations are constant time (array access, arithmetic). The initial population of `diff_initial` also takes O(N). Thus, `check` runs in O(N) time.
- The binary search performs `log(MAX_POWER)` iterations. `MAX_POWER` can be up to approximately `2 * 10^10` (maximum initial power for a city plus maximum power from `k` additional stations). `log(2 * 10^10)` is roughly 34-35 iterations.
- Therefore, the total time complexity is O(N * log(MAX_POWER)). Given N=10^5, this is roughly 10^5 * 35, which is efficient enough.

- **Space Complexity:** O(N).
- We use two difference arrays, `diff_initial` and `diff_for_new_stations`, each of size `n+1`. These arrays store `long long` (or equivalent) values.
- The space required is directly proportional to `n`.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-24 20:42:19 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved using a combination of line sweep and binary search. First, we calculate the initial power of each city by considering the existing power stations. Then, we use binary search to find the maximum possible minimum power of a city. In each iteration of the binary search, we check if it's possible to achieve the current minimum power by building the additional power stations. If it's possible, we update the minimum power and continue the binary search. If it's not possible, we decrease the minimum power and continue the binary search. The process continues until we find the maximum possible minimum power of a city.

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
    int maxPower(vector<int>& stations, int r, int k) {
        int n = stations.size();
        vector<int> power(n);
        for (int i = 0; i < n; i++) {
            for (int j = max(0, i - r); j <= min(n - 1, i + r); j++) {
                power[i] += stations[j];
            }
        }
        int low = *min_element(power.begin(), power.end());
        int high = *max_element(power.begin(), power.end()) + k;
        while (low < high) {
            int mid = (low + high + 1) / 2;
            vector<int> remaining(k);
            bool possible = true;
            for (int i = 0; i < n; i++) {
                if (power[i] < mid) {
                    int need = mid - power[i];
                    for (int j = max(0, i - r); j <= min(n - 1, i + r); j++) {
                        if (remaining[j] > 0) {
                            int give = min(remaining[j], need);
                            power[i] += give;
                            remaining[j] -= give;
                            need -= give;
                        }
                    }
                    if (need > 0) {
                        possible = false;
                        break;
                    }
                }
            }
            if (possible) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        return low;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maxPower(int[] stations, int r, int k) {
        int n = stations.length;
        int[] power = new int[n];
        for (int i = 0; i < n; i++) {
            for (int j = Math.max(0, i - r); j <= Math.min(n - 1, i + r); j++) {
                power[i] += stations[j];
            }
        }
        int low = Integer.MAX_VALUE;
        int high = 0;
        for (int i = 0; i < n; i++) {
            low = Math.min(low, power[i]);
            high = Math.max(high, power[i] + k);
        }
        while (low < high) {
            int mid = (low + high + 1) / 2;
            int[] remaining = new int[k];
            boolean possible = true;
            for (int i = 0; i < n; i++) {
                if (power[i] < mid) {
                    int need = mid - power[i];
                    for (int j = Math.max(0, i - r); j <= Math.min(n - 1, i + r); j++) {
                        if (remaining[j] > 0) {
                            int give = Math.min(remaining[j], need);
                            power[i] += give;
                            remaining[j] -= give;
                            need -= give;
                        }
                    }
                    if (need > 0) {
                        possible = false;
                        break;
                    }
                }
            }
            if (possible) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        return low;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def maxPower(self, stations: list[int], r: int, k: int) -> int:
        n = len(stations)
        power = [0] * n
        for i in range(n):
            for j in range(max(0, i - r), min(n, i + r + 1)):
                power[i] += stations[j]
        low = min(power)
        high = max(power) + k
        while low < high:
            mid = (low + high + 1) // 2
            remaining = [0] * n
            possible = True
            for i in range(n):
                if power[i] < mid:
                    need = mid - power[i]
                    for j in range(max(0, i - r), min(n, i + r + 1)):
                        if remaining[j] > 0:
                            give = min(remaining[j], need)
                            power[i] += give
                            remaining[j] -= give
                            need -= give
                    if need > 0:
                        possible = False
                        break
            if possible:
                low = mid
            else:
                high = mid - 1
        return low
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxPower(self, stations: list[int], r: int, k: int) -> int:
        n = len(stations)
        power = [0] * n
        for i in range(n):
            for j in range(max(0, i - r), min(n, i + r + 1)):
                power[i] += stations[j]
        low = min(power)
        high = max(power) + k
        while low < high:
            mid = (low + high + 1) // 2
            remaining = [0] * n
            possible = True
            for i in range(n):
                if power[i] < mid:
                    need = mid - power[i]
                    for j in range(max(0, i - r), min(n, i + r + 1)):
                        if remaining[j] > 0:
                            give = min(remaining[j], need)
                            power[i] += give
                            remaining[j] -= give
                            need -= give
                    if need > 0:
                        possible = False
                        break
            if possible:
                low = mid
            else:
                high = mid - 1
        return low
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <stdlib.h>

int maxPower(int* stations, int stationsSize, int r, int k) {
    int n = stationsSize;
    int* power = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        power[i] = 0;
        for (int j = i - r; j <= i + r; j++) {
            if (j >= 0 && j < n) {
                power[i] += stations[j];
            }
        }
    }
    int low = power[0];
    int high = power[0] + k;
    for (int i = 1; i < n; i++) {
        low = (low < power[i]) ? low : power[i];
        high = (high > power[i] + k) ? high : power[i] + k;
    }
    while (low < high) {
        int mid = (low + high + 1) / 2;
        int* remaining = (int*)malloc(n * sizeof(int));
        for (int i = 0; i < n; i++) {
            remaining[i] = 0;
        }
        int possible = 1;
        for (int i = 0; i < n; i++) {
            if (power[i] < mid) {
                int need = mid - power[i];
                for (int j = i - r; j <= i + r; j++) {
                    if (j >= 0 && j < n) {
                        if (remaining[j] > 0) {
                            int give = (remaining[j] < need) ? remaining[j] : need;
                            power[i] += give;
                            remaining[j] -= give;
                            need -= give;
                        }
                    }
                }
                if (need > 0) {
                    possible = 0;
                    break;
                }
            }
        }
        if (possible) {
            low = mid;
        } else {
            high = mid - 1;
        }
        free(remaining);
    }
    free(power);
    return low;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public int MaxPower(int[] stations, int r, int k) {
        int n = stations.Length;
        int[] power = new int[n];
        for (int i = 0; i < n; i++) {
            for (int j = Math.Max(0, i - r); j <= Math.Min(n - 1, i + r); j++) {
                power[i] += stations[j];
            }
        }
        int low = int.MaxValue;
        int high = 0;
        for (int i = 0; i < n; i++) {
            low = Math.Min(low, power[i]);
            high = Math.Max(high, power[i] + k);
        }
        while (low < high) {
            int mid = (low + high + 1) / 2;
            int[] remaining = new int[n];
            bool possible = true;
            for (int i = 0; i < n; i++) {
                if (power[i] < mid) {
                    int need = mid - power[i];
                    for (int j = Math.Max(0, i - r); j <= Math.Min(n - 1, i + r); j++) {
                        if (remaining[j] > 0) {
                            int give = Math.Min(remaining[j], need);
                            power[i] += give;
                            remaining[j] -= give;
                            need -= give;
                        }
                    }
                    if (need > 0) {
                        possible = false;
                        break;
                    }
                }
            }
            if (possible) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        return low;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
function maxPower(stations, r, k) {
    let n = stations.length;
    let power = new Array(n).fill(0);
    for (let i = 0; i < n; i++) {
        for (let j = Math.max(0, i - r); j <= Math.min(n - 1, i + r); j++) {
            power[i] += stations[j];
        }
    }
    let low = Math.min(...power);
    let high = Math.max(...power) + k;
    while (low < high) {
        let mid = Math.floor((low + high + 1) / 2);
        let remaining = new Array(n).fill(0);
        let possible = true;
        for (let i = 0; i < n; i++) {
            if (power[i] < mid) {
                let need = mid - power[i];
                for (let j = Math.max(0, i - r); j <= Math.min(n - 1, i + r); j++) {
                    if (remaining[j] > 0) {
                        let give = Math.min(remaining[j], need);
                        power[i] += give;
                        remaining[j] -= give;
                        need -= give;
                    }
                }
                if (need > 0) {
                    possible = false;
                    break;
                }
            }
        }
        if (possible) {
            low = mid;
        } else {
            high = mid - 1;
        }
    }
    return low;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxPower(stations: number[], r: number, k: number): number {
    let n = stations.length;
    let power: number[] = new Array(n).fill(0);
    for (let i = 0; i < n; i++) {
        for (let j = Math.max(0, i - r); j <= Math.min(n - 1, i + r); j++) {
            power[i] += stations[j];
        }
    }
    let low = Math.min(...power);
    let high = Math.max(...power) + k;
    while (low < high) {
        let mid = Math.floor((low + high + 1) / 2);
        let remaining: number[] = new Array(n).fill(0);
        let possible = true;
        for (let i = 0; i < n; i++) {
            if (power[i] < mid) {
                let need = mid - power[i];
                for (let j = Math.max(0, i - r); j <= Math.min(n - 1, i + r); j++) {
                    if (remaining[j] > 0) {
                        let give = Math.min(remaining[j], need);
                        power[i] += give;
                        remaining[j] -= give;
                        need -= give;
                    }
                }
                if (need > 0) {
                    possible = false;
                    break;
                }
            }
        }
        if (possible) {
            low = mid;
        } else {
            high = mid - 1;
        }
    }
    return low;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
function maxPower($stations, $r, $k) {
    $n = count($stations);
    $power = array_fill(0, $n, 0);
    for ($i = 0; $i < $n; $i++) {
        for ($j = max(0, $i - $r); $j <= min($n - 1, $i + $r); $j++) {
            $power[$i] += $stations[$j];
        }
    }
    $low = min($power);
    $high = max($power) + $k;
    while ($low < $high) {
        $mid = floor(($low + $high + 1) / 2);
        $remaining = array_fill(0, $n, 0);
        $possible = true;
        for ($i = 0; $i < $n; $i++) {
            if ($power[$i] < $mid) {
                $need = $mid - $power[$i];
                for ($j = max(0, $i - $r); $j <= min($n - 1, $i + $r); $j++) {
                    if ($remaining[$j] > 0) {
                        $give = min($remaining[$j], $need);
                        $power[$i] += $give;
                        $remaining[$j] -= $give;
                        $need -= $give;
                    }
                }
                if ($need > 0) {
                    $possible = false;
                    break;
                }
            }
        }
        if ($possible) {
            $low = $mid;
        } else {
            $high = $mid - 1;
        }
    }
    return $low;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
func maxPower(_ stations: [Int], _ r: Int, _ k: Int) -> Int {
    let n = stations.count
    var power = [Int](repeating: 0, count: n)
    for i in 0..<n {
        for j in max(0, i - r)...min(n - 1, i + r) {
            power[i] += stations[j]
        }
    }
    var low = power.min()!
    var high = power.max()! + k
    while low < high {
        let mid = (low + high + 1) / 2
        var remaining = [Int](repeating: 0, count: n)
        var possible = true
        for i in 0..<n {
            if power[i] < mid {
                var need = mid - power[i]
                for j in max(0, i - r)...min(n - 1, i + r) {
                    if remaining[j] > 0 {
                        let give = min(remaining[j], need)
                        power[i] += give
                        remaining[j] -= give
                        need -= give
                    }
                }
                if need > 0 {
                    possible = false
                    break
                }
            }
        }
        if possible {
            low = mid
        } else {
            high = mid - 1
        }
    }
    return low
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
fun maxPower(stations: IntArray, r: Int, k: Int): Int {
    val n = stations.size
    val power = IntArray(n)
    for (i in 0 until n) {
        for (j in maxOf(0, i - r) until minOf(n - 1, i + r + 1)) {
            power[i] += stations[j]
        }
    }
    var low = power.minOrNull()!!
    var high = power.maxOrNull()!! + k
    while (low < high) {
        val mid = (low + high + 1) / 2
        val remaining = IntArray(n)
        var possible = true
        for (i in 0 until n) {
            if (power[i] < mid) {
                var need = mid - power[i]
                for (j in maxOf(0, i - r) until minOf(n - 1, i + r + 1)) {
                    if (remaining[j] > 0) {
                        val give = minOf(remaining[j], need)
                        power[i] += give
                        remaining[j] -= give
                        need -= give
                    }
                }
                if (need > 0) {
                    possible = false
                    break
                }
            }
        }
        if (possible) {
            low = mid
        } else {
            high = mid - 1
        }
    }
    return low
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
int maxPower(List<int> stations, int r, int k) {
    int n = stations.length;
    List<int> power = List<int>.filled(n, 0);
    for (int i = 0; i < n; i++) {
        for (int j = max(0, i - r); j <= min(n - 1, i + r); j++) {
            power[i] += stations[j];
        }
    }
    int low = power.reduce((a, b) => a < b ? a : b);
    int high = power.reduce((a, b) => a > b ? a : b) + k;
    while (low < high) {
        int mid = (low + high + 1) ~/ 2;
        List<int> remaining = List<int>.filled(n, 0);
        bool possible = true;
        for (int i = 0; i < n; i++) {
            if (power[i] < mid) {
                int need = mid - power[i];
                for (int j = max(0, i - r); j <= min(n - 1, i + r); j++) {
                    if (remaining[j] > 0) {
                        int give = min(remaining[j], need);
                        power[i] += give;
                        remaining[j] -= give;
                        need -= give;
                    }
                }
                if (need > 0) {
                    possible = false;
                    break;
                }
            }
        }
        if (possible) {
            low = mid;
        } else {
            high = mid - 1;
        }
    }
    return low;
};
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

func maxPower(stations []int, r int, k int) int {
    n := len(stations)
    power := make([]int, n)
    for i := 0; i < n; i++ {
        for j := max(0, i-r); j <= min(n-1, i+r); j++ {
            power[i] += stations[j]
        }
    }
    low := power[0]
    high := power[0] + k
    for i := 1; i < n; i++ {
        if power[i] < low {
            low = power[i]
        }
        if power[i]+k > high {
            high = power[i] + k
        }
    }
    for low < high {
        mid := (low + high + 1) / 2
        remaining := make([]int, n)
        possible := true
        for i := 0; i < n; i++ {
            if power[i] < mid {
                need := mid - power[i]
                for j := max(0, i-r); j <= min(n-1, i+r); j++ {
                    if remaining[j] > 0 {
                        give := min(remaining[j], need)
                        power[i] += give
                        remaining[j] -= give
                        need -= give
                    }
                }
                if need > 0 {
                    possible = false
                    break
                }
            }
        }
        if possible {
            low = mid
        } else {
            high = mid - 1
        }
    }
    return low
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
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def max_power(stations, r, k)
    n = stations.size
    power = Array.new(n, 0)
    for i in 0...n
        for j in [i - r, 0].max...[i + r + 1, n].min
            power[i] += stations[j]
        end
    end
    low = power.min
    high = power.max + k
    while low < high
        mid = (low + high + 1) / 2
        remaining = Array.new(n, 0)
        possible = true
        for i in 0...n
            if power[i] < mid
                need = mid - power[i]
                for j in [i - r, 0].max...[i + r, n - 1].min
                    if remaining[j] > 0
                        give = [remaining[j], need].min
                        power[i] += give
                        remaining[j] -= give
                        need -= give
                    end
                end
                if need > 0
                    possible = false
                    break
                end
            end
        end
        if possible
            low = mid
        else
            high = mid - 1
        end
    end
    low
end;
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxPower(stations: Array[Int], r: Int, k: Int): Int = {
        val n = stations.length
        val power = Array.fill(n)(0)
        for (i <- 0 until n) {
            for (j <- math.max(0, i - r) to math.min(n - 1, i + r)) {
                power(i) += stations(j)
            }
        }
        var low = power.min
        var high = power.max + k
        while (low < high) {
            val mid = (low + high + 1) / 2
            val remaining = Array.fill(n)(0)
            var possible = true
            for (i <- 0 until n) {
                if (power(i) < mid) {
                    var need = mid - power(i)
                    for (j <- math.max(0, i - r) to math.min(n - 1, i + r)) {
                        if (remaining(j) > 0) {
                            val give = math.min(remaining(j), need)
                            power(i) += give
                            remaining(j) -= give
                            need -= give
                        }
                    }
                    if (need > 0) {
                        possible = false
                        break
                    }
                }
            }
            if (possible) {
                low = mid
            } else {
                high = mid - 1
            }
        }
        low
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
fn max_power(stations: Vec<i32>, r: i32, k: i32) -> i32 {
    let n = stations.len();
    let mut power: Vec<i32> = vec![0; n];
    for i in 0..n {
        for j in (i as i32 - r).max(0)..=(i as i32 + r).min(n as i32 - 1) {
            power[i] += stations[j as usize];
        }
    }
    let mut low = *power.iter().min().unwrap();
    let mut high = *power.iter().max().unwrap() + k;
    while low < high {
        let mid = (low + high + 1) / 2;
        let mut remaining: Vec<i32> = vec![0; n];
        let mut possible = true;
        for i in 0..n {
            if power[i] < mid {
                let mut need = mid - power[i];
                for j in (i as i32 - r).max(0)..=(i as i32 + r).min(n as i32 - 1) {
                    if remaining[j as usize] > 0 {
                        let give = remaining[j as usize].min(need);
                        power[i] += give;
                        remaining[j as usize] -= give;
                        need -= give;
                    }
                }
                if need > 0 {
                    possible = false;
                    break;
                }
            }
        }
        if possible {
            low = mid;
        } else {
            high = mid - 1;
        }
    }
    low
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket
(define (max-power stations r k)
  (let* ((n (length stations))
         (power (make-list n 0)))
    (for ((i (range n)))
      (for ((j (range (max 0 (- i r)) (min n (+ i r 1))))
        (set! power (list-set power i (+ (list-ref power i) (list-ref stations j))))))
    (let loop ((low (apply min power)) (high (+ (apply max power) k)))
      (if (< low high)
          (let ((mid (quotient (+ low high 1) 2)))
            (let* ((remaining (make-list n 0))
                   (possible #t))
              (for ((i (range n)))
                (when (< (list-ref power i) mid)
                  (let ((need (- mid (list-ref power i))))
                    (for ((j (range (max 0 (- i r)) (min n (+ i r 1))))
                      (when (> (list-ref remaining j) 0)
                        (let ((give (min (list-ref remaining j) need)))
                          (set! power (list-set power i (+ (list-ref power i) give)))
                          (set! remaining (list-set remaining j (- (list-ref remaining j) give)))
                          (set! need (- need give))))))
                    (unless (zero? need)
                      (set! possible #f)
                      (break))))
                (when (not possible)
                  (break)))
              (if possible
                  (loop mid high)
                  (loop low (- mid 1)))))
          low))));
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(max_power).
-export([max_power/3]).

max_power(Stations, R, K) ->
    N = length(Stations),
    Power = lists:duplicate(N, 0),
    lists:foldl(
      fun(I, Acc) ->
          lists:foldl(
            fun(J, Acc1) ->
                lists:update(I, Acc1, element(I, Acc1) + lists:nth(J + 1, Stations))
            end,
            Acc,
            lists:seq(max(0, I - R), min(N - 1, I + R)))
      end,
      Power,
      lists:seq(0, N - 1)),
    Low = lists:min(Power),
    High = lists:max(Power) + K,
    loop(Low, High, Power, Stations, R, K).

loop(Low, High, Power, Stations, R, K) when Low < High ->
    Mid = (Low + High + 1) div 2,
    Remaining = lists:duplicate(length(Power), 0),
    case possible(Mid, Power, Remaining, Stations, R, K) of
        true -> loop(Mid, High, Power, Stations, R, K);
        false -> loop(Low, Mid - 1, Power, Stations, R, K)
    end;
loop(Low, _High, _Power, _Stations, _R, _K) ->
    Low.

possible(Mid, Power, Remaining, Stations, R, K) ->
    lists:foldl(
      fun(I, Acc) ->
          case Acc of
              false -> false;
              true ->
                  case element(I, Power) < Mid of
                      true ->
                          Need = Mid - element(I, Power),
                          case lists:foldl(
                                 fun(J, Acc1) ->
                                     case Acc1 of
                                         {need, remaining} ->
                                             case element(J, remaining) of
                                                 0 -> {need, remaining};
                                                 _ ->
                                                     Give = min(element(J, remaining), need),
                                                     {need - Give, lists:update(J, remaining, element(J, remaining) - Give)}
                                             end
                                 end,
                                 {Need, Remaining},
                                 lists:seq(max(0, I - R), min(length(Power) - 1, I + R)))
                           of
                              {0, _} -> true;
                              _ -> false
                          end;
                      false -> true
                  end
          end
      end,
      true,
      lists:seq(0, length(Power) - 1)).

max(A, B) when A > B -> A;
max(_A, B) -> B.

min(A, B) when A < B -> A;
min(_A, B) -> B.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule MaxPower do
  def max_power(stations, r, k) do
    n = length(stations)
    power = Enum.to_list(0..n-1) |> Enum.map(fn _ -> 0 end)
    power = Enum.reduce(0..n-1, power, fn i, power ->
      Enum.reduce(max(0, i - r)..min(n - 1, i + r), power, fn j, power ->
        List.update_at(power, i, &(&1 + Enum.at(stations, j)))
      end)
    end)
    low = Enum.min(power)
    high = Enum.max(power) + k
    loop(low, high, power, stations, r, k)
  end

  defp loop(low, high, power, stations, r, k) when low < high do
    mid = div(low + high + 1, 2)
    remaining = Enum.to_list(0..length(power)-1) |> Enum.map(fn _ -> 0 end)
    case possible(mid, power, remaining, stations, r, k) do
      true -> loop(mid, high, power, stations, r, k)
      false -> loop(low, mid - 1, power, stations, r, k)
    end
  end

  defp loop(low, _high, _power, _stations, _r, _k), do: low

  defp possible(mid, power, remaining, stations, r, k) do
    Enum.reduce(0..length(power)-1, true, fn i, acc ->
      case acc do
        false -> false
        true ->
          case Enum.at(power, i) < mid do
            true ->
              need = mid - Enum.at(power, i)
              {need, remaining} = Enum.reduce(max(0, i - r)..min(length(power) - 1, i + r), {need, remaining}, fn j, {need, remaining} ->
                case Enum.at(remaining, j) do
                  0 -> {need, remaining}
                  _ ->
                    give = min(Enum.at(remaining, j), need)
                    {need - give, List.update_at(remaining, j, &(&1 - give))}
                end
              end)
              case need do
                0 -> true
                _ -> false
              end
            false -> true
          end
      end
    end)
  end

  defp max(a, b) when a > b, do: a
  defp max(_a, b), do: b

  defp min(a, b) when a < b, do: a
  defp min(_a, b), do: b
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n log m) where n is the number of cities and m is the maximum possible minimum power of a city. The time complexity is dominated by the binary search, which takes O(log m) time. Inside the binary search, we iterate over the cities to check if it's possible to achieve the current minimum power, which takes O(n) time.

- **Space Complexity:** O(n) where n is the number of cities. We need to store the initial power of each city and the additional power stations that can be built in each city.

</div>
</details>
