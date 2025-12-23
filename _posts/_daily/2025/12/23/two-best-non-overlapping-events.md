---
layout: post
title: "Two Best Non-Overlapping Events"
date: 2025-12-23 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Binary Search", "Dynamic Programming", "Sorting", "Heap (Priority Queue)"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/two-best-non-overlapping-events/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <algorithm>\n\nclass Solution {\npublic:\n \
        \   int maxTwoEvents(std::vector<std::vector<int>>& events) {\n        // Sort\
        \ events by start time\n        std::sort(events.begin(), events.end());\n\n\
        \        int n = events.size();\n\n        // suffixMaxValues[i] stores the\
        \ maximum value of an event from events[i] to events[n-1]\n        std::vector<int>\
        \ suffixMaxValues(n);\n        suffixMaxValues[n - 1] = events[n - 1][2];\n\
        \        for (int i = n - 2; i >= 0; --i) {\n            suffixMaxValues[i]\
        \ = std::max(events[i][2], suffixMaxValues[i + 1]);\n        }\n\n        int\
        \ maxTotalValue = 0;\n\n        // Extract start times for binary search\n \
        \       std::vector<int> startTimes(n);\n        for (int i = 0; i < n; ++i)\
        \ {\n            startTimes[i] = events[i][0];\n        }\n\n        for (int\
        \ i = 0; i < n; ++i) {\n            int s_i = events[i][0];\n            int\
        \ e_i = events[i][1];\n            int v_i = events[i][2];\n\n            //\
        \ Case 1: Pick only event i\n            maxTotalValue = std::max(maxTotalValue,\
        \ v_i);\n\n            // Case 2: Pick event i and another non-overlapping event\
        \ after it\n            // Find the first event that starts at or after e_i\
        \ + 1\n            int targetStartTime = e_i + 1;\n\n            // Use std::lower_bound\
        \ to find the iterator to the first element\n            // in the range [startTimes.begin()\
        \ + i + 1, startTimes.end())\n            // that is not less than targetStartTime.\n\
        \            auto it = std::lower_bound(startTimes.begin() + i + 1, startTimes.end(),\
        \ targetStartTime);\n\n            // Calculate the index\n            int idx\
        \ = std::distance(startTimes.begin(), it);\n\n            if (idx < n) {\n \
        \               // If such an event exists, add its maximum possible value (from\
        \ suffixMaxValues)\n                maxTotalValue = std::max(maxTotalValue,\
        \ v_i + suffixMaxValues[idx]);\n            }\n        }\n\n        return maxTotalValue;\n\
        \    }\n};"
      java: "import java.util.Arrays;\nimport java.util.Comparator;\nimport java.util.List;\n\
        \nclass Solution {\n    public int maxTwoEvents(int[][] events) {\n        //\
        \ Sort events by start time\n        Arrays.sort(events, Comparator.comparingInt(a\
        \ -> a[0]));\n\n        int n = events.length;\n\n        // suffixMaxValues[i]\
        \ stores the maximum value of an event from events[i] to events[n-1]\n     \
        \   int[] suffixMaxValues = new int[n];\n        suffixMaxValues[n - 1] = events[n\
        \ - 1][2];\n        for (int i = n - 2; i >= 0; i--) {\n            suffixMaxValues[i]\
        \ = Math.max(events[i][2], suffixMaxValues[i + 1]);\n        }\n\n        int\
        \ maxTotalValue = 0;\n\n        // Extract start times for binary search\n \
        \       int[] startTimes = new int[n];\n        for (int i = 0; i < n; i++)\
        \ {\n            startTimes[i] = events[i][0];\n        }\n\n        for (int\
        \ i = 0; i < n; i++) {\n            int s_i = events[i][0];\n            int\
        \ e_i = events[i][1];\n            int v_i = events[i][2];\n\n            //\
        \ Case 1: Pick only event i\n            maxTotalValue = Math.max(maxTotalValue,\
        \ v_i);\n\n            // Case 2: Pick event i and another non-overlapping event\
        \ after it\n            // Find the first event that starts at or after e_i\
        \ + 1\n            int targetStartTime = e_i + 1;\n\n            // Use binary\
        \ search to find the index of the first event whose start time is >= targetStartTime\n\
        \            // Search only in events after the current one (i+1 to n-1)\n \
        \           // Arrays.binarySearch returns: index if found, or (-(insertion\
        \ point) - 1) if not found.\n            // The insertion point is the index\
        \ of the first element greater than the key, or n if all elements are less than\
        \ the key.\n            int idx = Arrays.binarySearch(startTimes, i + 1, n,\
        \ targetStartTime);\n\n            if (idx < 0) { // Not found, convert to insertion\
        \ point\n                idx = -(idx + 1);\n            }\n\n            if\
        \ (idx < n) {\n                // If such an event exists, add its maximum possible\
        \ value (from suffixMaxValues)\n                maxTotalValue = Math.max(maxTotalValue,\
        \ v_i + suffixMaxValues[idx]);\n            }\n        }\n\n        return maxTotalValue;\n\
        \    }\n}"
      python: "import bisect\n\nclass Solution:\n    def maxTwoEvents(self, events:\
        \ list[list[int]]) -> int:\n        events.sort() # Sort by start time\n   \
        \     n = len(events)\n\n        # suffix_max_values[i] stores the maximum value\
        \ of an event from events[i] to events[n-1]\n        suffix_max_values = [0]\
        \ * n\n        suffix_max_values[n-1] = events[n-1][2]\n        for i in range(n\
        \ - 2, -1, -1):\n            suffix_max_values[i] = max(events[i][2], suffix_max_values[i+1])\n\
        \n        max_total_value = 0\n\n        # Extract start times for binary search\n\
        \        start_times = [event[0] for event in events]\n\n        for i in range(n):\n\
        \            s_i, e_i, v_i = events[i]\n\n            # Case 1: Pick only event\
        \ i\n            max_total_value = max(max_total_value, v_i)\n\n           \
        \ # Case 2: Pick event i and another non-overlapping event after it\n      \
        \      # Find the first event that starts at or after e_i + 1\n            target_start_time\
        \ = e_i + 1\n\n            # Use bisect_left to find the index of the first\
        \ event whose start time is >= target_start_time\n            # Search only\
        \ in events after the current one (i+1 to n-1)\n            idx = bisect.bisect_left(start_times,\
        \ target_start_time, lo=i+1)\n\n            if idx < n:\n                # If\
        \ such an event exists, add its maximum possible value (from suffix_max_values)\n\
        \                max_total_value = max(max_total_value, v_i + suffix_max_values[idx])\n\
        \n        return max_total_value"
      python3: "import bisect\n\nclass Solution:\n    def maxTwoEvents(self, events:\
        \ list[list[int]]) -> int:\n        events.sort() # Sort by start time\n   \
        \     n = len(events)\n\n        # suffix_max_values[i] stores the maximum value\
        \ of an event from events[i] to events[n-1]\n        suffix_max_values = [0]\
        \ * n\n        suffix_max_values[n-1] = events[n-1][2]\n        for i in range(n\
        \ - 2, -1, -1):\n            suffix_max_values[i] = max(events[i][2], suffix_max_values[i+1])\n\
        \n        max_total_value = 0\n\n        # Extract start times for binary search\n\
        \        start_times = [event[0] for event in events]\n\n        for i in range(n):\n\
        \            s_i, e_i, v_i = events[i]\n\n            # Case 1: Pick only event\
        \ i\n            max_total_value = max(max_total_value, v_i)\n\n           \
        \ # Case 2: Pick event i and another non-overlapping event after it\n      \
        \      # Find the first event that starts at or after e_i + 1\n            target_start_time\
        \ = e_i + 1\n\n            # Use bisect_left to find the index of the first\
        \ event whose start time is >= target_start_time\n            # Search only\
        \ in events after the current one (i+1 to n-1)\n            idx = bisect.bisect_left(start_times,\
        \ target_start_time, lo=i+1)\n\n            if idx < n:\n                # If\
        \ such an event exists, add its maximum possible value (from suffix_max_values)\n\
        \                max_total_value = max(max_total_value, v_i + suffix_max_values[idx])\n\
        \n        return max_total_value"
      c: "#include <stdlib.h>\n#include <string.h>\n\n// Comparison function for qsort\n\
        int compareEvents(const void *a, const void *b) {\n    const int *eventA = *(const\
        \ int **)a;\n    const int *eventB = *(const int **)b;\n    if (eventA[0] !=\
        \ eventB[0]) {\n        return eventA[0] - eventB[0];\n    }\n    return eventA[1]\
        \ - eventB[1]; // Secondary sort by end time (optional, but good for consistency)\n\
        }\n\n// Manual binary search (lower_bound equivalent)\n// Searches in the range\
        \ [low, high] inclusive\nint lower_bound_custom(int* arr, int low, int high,\
        \ int target) {\n    int ans = high + 1; // Default if no element found in range\n\
        \    while (low <= high) {\n        int mid = low + (high - low) / 2;\n    \
        \    if (arr[mid] >= target) {\n            ans = mid;\n            high = mid\
        \ - 1;\n        } else {\n            low = mid + 1;\n        }\n    }\n   \
        \ return ans;\n}\n\nint maxTwoEvents(int** events, int eventsSize, int* eventsColSize)\
        \ {\n    // Need to sort the array of pointers to events\n    qsort(events,\
        \ eventsSize, sizeof(int*), compareEvents);\n\n    int n = eventsSize;\n\n \
        \   int* suffixMaxValues = (int*)malloc(n * sizeof(int));\n    if (!suffixMaxValues)\
        \ return 0; // Handle allocation failure\n\n    suffixMaxValues[n - 1] = events[n\
        \ - 1][2];\n    for (int i = n - 2; i >= 0; --i) {\n        suffixMaxValues[i]\
        \ = (events[i][2] > suffixMaxValues[i + 1]) ? events[i][2] : suffixMaxValues[i\
        \ + 1];\n    }\n\n    int maxTotalValue = 0;\n\n    int* startTimes = (int*)malloc(n\
        \ * sizeof(int));\n    if (!startTimes) {\n        free(suffixMaxValues);\n\
        \        return 0; // Handle allocation failure\n    }\n    for (int i = 0;\
        \ i < n; ++i) {\n        startTimes[i] = events[i][0];\n    }\n\n    for (int\
        \ i = 0; i < n; ++i) {\n        int s_i = events[i][0];\n        int e_i = events[i][1];\n\
        \        int v_i = events[i][2];\n\n        maxTotalValue = (maxTotalValue >\
        \ v_i) ? maxTotalValue : v_i;\n\n        int targetStartTime = e_i + 1;\n\n\
        \        // Search in the range [i + 1, n - 1]\n        int idx = lower_bound_custom(startTimes,\
        \ i + 1, n - 1, targetStartTime);\n\n        if (idx < n) {\n            maxTotalValue\
        \ = (maxTotalValue > v_i + suffixMaxValues[idx]) ? maxTotalValue : v_i + suffixMaxValues[idx];\n\
        \        }\n    }\n\n    free(suffixMaxValues);\n    free(startTimes);\n\n \
        \   return maxTotalValue;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\nusing System.Linq;\n\
        \npublic class Solution {\n    public int MaxTwoEvents(int[][] events) {\n \
        \       // Sort events by start time\n        Array.Sort(events, (a, b) => a[0].CompareTo(b[0]));\n\
        \n        int n = events.Length;\n\n        // suffixMaxValues[i] stores the\
        \ maximum value of an event from events[i] to events[n-1]\n        int[] suffixMaxValues\
        \ = new int[n];\n        suffixMaxValues[n - 1] = events[n - 1][2];\n      \
        \  for (int i = n - 2; i >= 0; i--) {\n            suffixMaxValues[i] = Math.Max(events[i][2],\
        \ suffixMaxValues[i + 1]);\n        }\n\n        int maxTotalValue = 0;\n\n\
        \        // Extract start times for binary search\n        int[] startTimes\
        \ = new int[n];\n        for (int i = 0; i < n; i++) {\n            startTimes[i]\
        \ = events[i][0];\n        }\n\n        for (int i = 0; i < n; i++) {\n    \
        \        int s_i = events[i][0];\n            int e_i = events[i][1];\n    \
        \        int v_i = events[i][2];\n\n            // Case 1: Pick only event i\n\
        \            maxTotalValue = Math.Max(maxTotalValue, v_i);\n\n            //\
        \ Case 2: Pick event i and another non-overlapping event after it\n        \
        \    // Find the first event that starts at or after e_i + 1\n            int\
        \ targetStartTime = e_i + 1;\n\n            // Use Array.BinarySearch to find\
        \ the index of the first event whose start time is >= targetStartTime\n    \
        \        // Search only in events after the current one (i+1 to n-1)\n     \
        \       // Array.BinarySearch returns: index if found, or (-(insertion point)\
        \ - 1) if not found.\n            // The insertion point is the index of the\
        \ first element greater than the key, or n if all elements are less than the\
        \ key.\n            int idx = Array.BinarySearch(startTimes, i + 1, n - (i +\
        \ 1), targetStartTime);\n\n            if (idx < 0) { // Not found, convert\
        \ to insertion point\n                idx = ~idx; // Equivalent to -(idx + 1)\
        \ in C#\n            }\n\n            if (idx < n) {\n                // If\
        \ such an event exists, add its maximum possible value (from suffixMaxValues)\n\
        \                maxTotalValue = Math.Max(maxTotalValue, v_i + suffixMaxValues[idx]);\n\
        \            }\n        }\n\n        return maxTotalValue;\n    }\n}"
      javascript: "/**\n * @param {number[][]} events\n * @return {number}\n */\nvar\
        \ maxTwoEvents = function(events) {\n    // Sort events by start time\n    events.sort((a,\
        \ b) => a[0] - b[0]);\n\n    const n = events.length;\n\n    // suffixMaxValues[i]\
        \ stores the maximum value of an event from events[i] to events[n-1]\n    const\
        \ suffixMaxValues = new Array(n).fill(0);\n    suffixMaxValues[n - 1] = events[n\
        \ - 1][2];\n    for (let i = n - 2; i >= 0; i--) {\n        suffixMaxValues[i]\
        \ = Math.max(events[i][2], suffixMaxValues[i + 1]);\n    }\n\n    let maxTotalValue\
        \ = 0;\n\n    // Extract start times for binary search\n    const startTimes\
        \ = events.map(event => event[0]);\n\n    // Custom binary search for lower_bound\
        \ (finds the first index where element >= target)\n    const lowerBound = (arr,\
        \ target, low, high) => {\n        let ans = high + 1; // Default if no element\
        \ found in range [low, high]\n        while (low <= high) {\n            const\
        \ mid = Math.floor(low + (high - low) / 2);\n            if (arr[mid] >= target)\
        \ {\n                ans = mid;\n                high = mid - 1;\n         \
        \   } else {\n                low = mid + 1;\n            }\n        }\n   \
        \     return ans;\n    };\n\n    for (let i = 0; i < n; i++) {\n        const\
        \ [s_i, e_i, v_i] = events[i];\n\n        // Case 1: Pick only event i\n   \
        \     maxTotalValue = Math.max(maxTotalValue, v_i);\n\n        // Case 2: Pick\
        \ event i and another non-overlapping event after it\n        // Find the first\
        \ event that starts at or after e_i + 1\n        const targetStartTime = e_i\
        \ + 1;\n\n        // Search only in events after the current one (i+1 to n-1)\n\
        \        const idx = lowerBound(startTimes, targetStartTime, i + 1, n - 1);\n\
        \n        if (idx < n) { // If such an event exists\n            maxTotalValue\
        \ = Math.max(maxTotalValue, v_i + suffixMaxValues[idx]);\n        }\n    }\n\
        \n    return maxTotalValue;\n};"
      typescript: "function maxTwoEvents(events: number[][]): number {\n    // Sort\
        \ events by start time\n    events.sort((a, b) => a[0] - b[0]);\n\n    const\
        \ n = events.length;\n\n    // suffixMaxValues[i] stores the maximum value of\
        \ an event from events[i] to events[n-1]\n    const suffixMaxValues: number[]\
        \ = new Array(n).fill(0);\n    suffixMaxValues[n - 1] = events[n - 1][2];\n\
        \    for (let i = n - 2; i >= 0; i--) {\n        suffixMaxValues[i] = Math.max(events[i][2],\
        \ suffixMaxValues[i + 1]);\n    }\n\n    let maxTotalValue: number = 0;\n\n\
        \    // Extract start times for binary search\n    const startTimes: number[]\
        \ = events.map(event => event[0]);\n\n    // Custom binary search for lower_bound\
        \ (finds the first index where element >= target)\n    const lowerBound = (arr:\
        \ number[], target: number, low: number, high: number): number => {\n      \
        \  let ans: number = high + 1; // Default if no element found in range [low,\
        \ high]\n        while (low <= high) {\n            const mid = Math.floor(low\
        \ + (high - low) / 2);\n            if (arr[mid] >= target) {\n            \
        \    ans = mid;\n                high = mid - 1;\n            } else {\n   \
        \             low = mid + 1;\n            }\n        }\n        return ans;\n\
        \    };\n\n    for (let i = 0; i < n; i++) {\n        const [s_i, e_i, v_i]\
        \ = events[i];\n\n        // Case 1: Pick only event i\n        maxTotalValue\
        \ = Math.max(maxTotalValue, v_i);\n\n        // Case 2: Pick event i and another\
        \ non-overlapping event after it\n        // Find the first event that starts\
        \ at or after e_i + 1\n        const targetStartTime: number = e_i + 1;\n\n\
        \        // Search only in events after the current one (i+1 to n-1)\n     \
        \   const idx: number = lowerBound(startTimes, targetStartTime, i + 1, n - 1);\n\
        \n        if (idx < n) { // If such an event exists\n            maxTotalValue\
        \ = Math.max(maxTotalValue, v_i + suffixMaxValues[idx]);\n        }\n    }\n\
        \n    return maxTotalValue;\n};"
      php: "<?php\nclass Solution {\n\n    /**\n     * @param Integer[][] $events\n\
        \     * @return Integer\n     */\n    function maxTwoEvents($events) {\n   \
        \     // Sort events by start time\n        usort($events, function($a, $b)\
        \ {\n            return $a[0] - $b[0];\n        });\n\n        $n = count($events);\n\
        \n        // suffixMaxValues[i] stores the maximum value of an event from events[i]\
        \ to events[n-1]\n        $suffixMaxValues = array_fill(0, $n, 0);\n       \
        \ $suffixMaxValues[$n - 1] = $events[$n - 1][2];\n        for ($i = $n - 2;\
        \ $i >= 0; $i--) {\n            $suffixMaxValues[$i] = max($events[$i][2], $suffixMaxValues[$i\
        \ + 1]);\n        }\n\n        $maxTotalValue = 0;\n\n        // Extract start\
        \ times for binary search\n        $startTimes = array_map(function($event)\
        \ { return $event[0]; }, $events);\n\n        // Custom binary search for lower_bound\
        \ (finds the first index where element >= target)\n        $lowerBound = function($arr,\
        \ $target, $low, $high) use ($n) {\n            $ans = $high + 1; // Default\
        \ if no element found in range [low, high]\n            while ($low <= $high)\
        \ {\n                $mid = floor($low + ($high - $low) / 2);\n            \
        \    if ($arr[$mid] >= $target) {\n                    $ans = $mid;\n      \
        \              $high = $mid - 1;\n                } else {\n               \
        \     $low = $mid + 1;\n                }\n            }\n            return\
        \ $ans;\n        };\n\n        for ($i = 0; $i < $n; $i++) {\n            list($s_i,\
        \ $e_i, $v_i) = $events[$i];\n\n            // Case 1: Pick only event i\n \
        \           $maxTotalValue = max($maxTotalValue, $v_i);\n\n            // Case\
        \ 2: Pick event i and another non-overlapping event after it\n            //\
        \ Find the first event that starts at or after e_i + 1\n            $targetStartTime\
        \ = $e_i + 1;\n\n            // Search only in events after the current one\
        \ (i+1 to n-1)\n            $idx = $lowerBound($startTimes, $targetStartTime,\
        \ $i + 1, $n - 1);\n\n            if ($idx < $n) { // If such an event exists\n\
        \                $maxTotalValue = max($maxTotalValue, $v_i + $suffixMaxValues[$idx]);\n\
        \            }\n        }\n\n        return $maxTotalValue;\n    }\n}"
      swift: "import Foundation\n\nclass Solution {\n    func maxTwoEvents(_ events:\
        \ [[Int]]) -> Int {\n        // Sort events by start time\n        var sortedEvents\
        \ = events.sorted { $0[0] < $1[0] }\n\n        let n = sortedEvents.count\n\n\
        \        // suffixMaxValues[i] stores the maximum value of an event from events[i]\
        \ to events[n-1]\n        var suffixMaxValues = Array(repeating: 0, count: n)\n\
        \        suffixMaxValues[n - 1] = sortedEvents[n - 1][2]\n        for i in (0..<n\
        \ - 1).reversed() {\n            suffixMaxValues[i] = max(sortedEvents[i][2],\
        \ suffixMaxValues[i + 1])\n        }\n\n        var maxTotalValue = 0\n\n  \
        \      // Extract start times for binary search\n        let startTimes = sortedEvents.map\
        \ { $0[0] }\n\n        // Custom binary search for lower_bound (finds the first\
        \ index where element >= target)\n        func lowerBound(arr: [Int], target:\
        \ Int, low: Int, high: Int) -> Int {\n            var ans = high + 1 // Default\
        \ if no element found in range [low, high]\n            var l = low\n      \
        \      var h = high\n            while l <= h {\n                let mid = l\
        \ + (h - l) / 2\n                if arr[mid] >= target {\n                 \
        \   ans = mid\n                    h = mid - 1\n                } else {\n \
        \                   l = mid + 1\n                }\n            }\n        \
        \    return ans\n        }\n\n        for i in 0..<n {\n            let s_i\
        \ = sortedEvents[i][0]\n            let e_i = sortedEvents[i][1]\n         \
        \   let v_i = sortedEvents[i][2]\n\n            // Case 1: Pick only event i\n\
        \            maxTotalValue = max(maxTotalValue, v_i)\n\n            // Case\
        \ 2: Pick event i and another non-overlapping event after it\n            //\
        \ Find the first event that starts at or after e_i + 1\n            let targetStartTime\
        \ = e_i + 1\n\n            // Search only in events after the current one (i+1\
        \ to n-1)\n            let idx = lowerBound(arr: startTimes, target: targetStartTime,\
        \ low: i + 1, high: n - 1)\n\n            if idx < n { // If such an event exists\n\
        \                maxTotalValue = max(maxTotalValue, v_i + suffixMaxValues[idx])\n\
        \            }\n        }\n\n        return maxTotalValue\n    }\n}"
      kotlin: "import java.util.Arrays\n\nclass Solution {\n    fun maxTwoEvents(events:\
        \ Array<IntArray>): Int {\n        // Sort events by start time\n        events.sortBy\
        \ { it[0] }\n\n        val n = events.size\n\n        // suffixMaxValues[i]\
        \ stores the maximum value of an event from events[i] to events[n-1]\n     \
        \   val suffixMaxValues = IntArray(n)\n        suffixMaxValues[n - 1] = events[n\
        \ - 1][2]\n        for (i in n - 2 downTo 0) {\n            suffixMaxValues[i]\
        \ = Math.max(events[i][2], suffixMaxValues[i + 1])\n        }\n\n        var\
        \ maxTotalValue = 0\n\n        // Extract start times for binary search\n  \
        \      val startTimes = IntArray(n) { i -> events[i][0] }\n\n        for (i\
        \ in 0 until n) {\n            val s_i = events[i][0]\n            val e_i =\
        \ events[i][1]\n            val v_i = events[i][2]\n\n            // Case 1:\
        \ Pick only event i\n            maxTotalValue = Math.max(maxTotalValue, v_i)\n\
        \n            // Case 2: Pick event i and another non-overlapping event after\
        \ it\n            // Find the first event that starts at or after e_i + 1\n\
        \            val targetStartTime = e_i + 1\n\n            // Use binary search\
        \ to find the index of the first event whose start time is >= targetStartTime\n\
        \            // Search only in events after the current one (i+1 to n-1)\n \
        \           // Arrays.binarySearch returns: index if found, or (-(insertion\
        \ point) - 1) if not found.\n            // The insertion point is the index\
        \ of the first element greater than the key, or n if all elements are less than\
        \ the key.\n            var idx = startTimes.binarySearch(targetStartTime, i\
        \ + 1, n)\n\n            if (idx < 0) { // Not found, convert to insertion point\n\
        \                idx = -(idx + 1)\n            }\n\n            if (idx < n)\
        \ {\n                // If such an event exists, add its maximum possible value\
        \ (from suffixMaxValues)\n                maxTotalValue = Math.max(maxTotalValue,\
        \ v_i + suffixMaxValues[idx])\n            }\n        }\n\n        return maxTotalValue\n\
        \    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int maxTwoEvents(List<List<int>>\
        \ events) {\n    // Sort events by start time\n    events.sort((a, b) => a[0].compareTo(b[0]));\n\
        \n    final n = events.length;\n\n    // suffixMaxValues[i] stores the maximum\
        \ value of an event from events[i] to events[n-1]\n    final suffixMaxValues\
        \ = List<int>.filled(n, 0);\n    suffixMaxValues[n - 1] = events[n - 1][2];\n\
        \    for (int i = n - 2; i >= 0; i--) {\n      suffixMaxValues[i] = max(events[i][2],\
        \ suffixMaxValues[i + 1]);\n    }\n\n    int maxTotalValue = 0;\n\n    // Extract\
        \ start times for binary search\n    final startTimes = events.map((event) =>\
        \ event[0]).toList();\n\n    // Custom binary search for lower_bound (finds\
        \ the first index where element >= target)\n    int lowerBound(List<int> arr,\
        \ int target, int low, int high) {\n      int ans = high + 1; // Default if\
        \ no element found in range [low, high]\n      while (low <= high) {\n     \
        \   final mid = low + ((high - low) ~/ 2);\n        if (arr[mid] >= target)\
        \ {\n          ans = mid;\n          high = mid - 1;\n        } else {\n   \
        \       low = mid + 1;\n        }\n      }\n      return ans;\n    }\n\n   \
        \ for (int i = 0; i < n; i++) {\n      final s_i = events[i][0];\n      final\
        \ e_i = events[i][1];\n      final v_i = events[i][2];\n\n      // Case 1: Pick\
        \ only event i\n      maxTotalValue = max(maxTotalValue, v_i);\n\n      // Case\
        \ 2: Pick event i and another non-overlapping event after it\n      // Find\
        \ the first event that starts at or after e_i + 1\n      final targetStartTime\
        \ = e_i + 1;\n\n      // Search only in events after the current one (i+1 to\
        \ n-1)\n      final idx = lowerBound(startTimes, targetStartTime, i + 1, n -\
        \ 1);\n\n      if (idx < n) { // If such an event exists\n        maxTotalValue\
        \ = max(maxTotalValue, v_i + suffixMaxValues[idx]);\n      }\n    }\n\n    return\
        \ maxTotalValue;\n  }\n}"
      go: "package main\n\nimport (\n\t\"sort\"\n\t\"math\"\n)\n\nfunc maxTwoEvents(events\
        \ [][]int) int {\n    // Sort events by start time\n    sort.Slice(events, func(i,\
        \ j int) bool {\n        return events[i][0] < events[j][0]\n    })\n\n    n\
        \ := len(events)\n\n    // suffixMaxValues[i] stores the maximum value of an\
        \ event from events[i] to events[n-1]\n    suffixMaxValues := make([]int, n)\n\
        \    suffixMaxValues[n-1] = events[n-1][2]\n    for i := n - 2; i >= 0; i--\
        \ {\n        suffixMaxValues[i] = int(math.Max(float64(events[i][2]), float64(suffixMaxValues[i+1])))\n\
        \    }\n\n    maxTotalValue := 0\n\n    // Extract start times for binary search\n\
        \    startTimes := make([]int, n)\n    for i := 0; i < n; i++ {\n        startTimes[i]\
        \ = events[i][0]\n    }\n\n    for i := 0; i < n; i++ {\n        s_i, e_i, v_i\
        \ := events[i][0], events[i][1], events[i][2]\n\n        // Case 1: Pick only\
        \ event i\n        maxTotalValue = int(math.Max(float64(maxTotalValue), float64(v_i)))\n\
        \n        // Case 2: Pick event i and another non-overlapping event after it\n\
        \        // Find the first event that starts at or after e_i + 1\n        targetStartTime\
        \ := e_i + 1\n\n        // Use sort.SearchInts for lower_bound (finds the first\
        \ index where element >= target)\n        // Search only in events after the\
        \ current one (i+1 to n-1)\n        // sort.SearchInts returns the smallest\
        \ index i such that a[i] >= x.\n        // If no such index exists, it returns\
        \ len(a).\n        idx := sort.SearchInts(startTimes[i+1:n], targetStartTime)\n\
        \        idx += (i + 1) // Adjust index to be relative to the original startTimes\
        \ array\n\n        if idx < n { // If such an event exists\n            maxTotalValue\
        \ = int(math.Max(float64(maxTotalValue), float64(v_i + suffixMaxValues[idx])))\n\
        \        }\n    }\n\n    return maxTotalValue\n}"
      ruby: "class Solution\n    # @param {Integer[][]} events\n    # @return {Integer}\n\
        \    def max_two_events(events)\n        # Sort events by start time\n     \
        \   events.sort! { |a, b| a[0] - b[0] }\n\n        n = events.length\n\n   \
        \     # suffix_max_values[i] stores the maximum value of an event from events[i]\
        \ to events[n-1]\n        suffix_max_values = Array.new(n)\n        suffix_max_values[n\
        \ - 1] = events[n - 1][2]\n        (n - 2).downto(0) do |i|\n            suffix_max_values[i]\
        \ = [events[i][2], suffix_max_values[i + 1]].max\n        end\n\n        max_total_value\
        \ = 0\n\n        # Extract start times for binary search\n        start_times\
        \ = events.map { |event| event[0] }\n\n        # Custom binary search for lower_bound\
        \ (finds the first index where element >= target)\n        # Searches in the\
        \ range [low, high] inclusive\n        lower_bound = lambda do |arr, target,\
        \ low, high|\n            ans = high + 1 # Default if no element found in range\n\
        \            while low <= high\n                mid = low + (high - low) / 2\n\
        \                if arr[mid] >= target\n                    ans = mid\n    \
        \                high = mid - 1\n                else\n                    low\
        \ = mid + 1\n                end\n            end\n            ans\n       \
        \ end\n\n        for i in 0...n\n            s_i, e_i, v_i = events[i]\n\n \
        \           # Case 1: Pick only event i\n            max_total_value = [max_total_value,\
        \ v_i].max\n\n            # Case 2: Pick event i and another non-overlapping\
        \ event after it\n            # Find the first event that starts at or after\
        \ e_i + 1\n            target_start_time = e_i + 1\n\n            # Search only\
        \ in events after the current one (i+1 to n-1)\n            idx = lower_bound.call(start_times,\
        \ target_start_time, i + 1, n - 1)\n\n            if idx < n # If such an event\
        \ exists\n                max_total_value = [max_total_value, v_i + suffix_max_values[idx]].max\n\
        \            end\n        end\n\n        return max_total_value\n    end\nend"
      scala: "import scala.collection.mutable.ArrayBuffer\nimport scala.math.max\n\n\
        object Solution {\n    def maxTwoEvents(events: Array[Array[Int]]): Int = {\n\
        \        // Sort events by start time\n        val sortedEvents = events.sortBy(_(0))\n\
        \n        val n = sortedEvents.length\n\n        // suffixMaxValues[i] stores\
        \ the maximum value of an event from events[i] to events[n-1]\n        val suffixMaxValues\
        \ = Array.ofDim[Int](n)\n        suffixMaxValues(n - 1) = sortedEvents(n - 1)(2)\n\
        \        for (i <- n - 2 to 0 by -1) {\n            suffixMaxValues(i) = max(sortedEvents(i)(2),\
        \ suffixMaxValues(i + 1))\n        }\n\n        var maxTotalValue = 0\n\n  \
        \      // Extract start times for binary search\n        val startTimes = sortedEvents.map(_(0))\n\
        \n        // Custom binary search for lower_bound (finds the first index where\
        \ element >= target)\n        // Searches in the range [low, high] inclusive\n\
        \        def lowerBound(arr: Array[Int], target: Int, low: Int, high: Int):\
        \ Int = {\n            var ans = high + 1 // Default if no element found in\
        \ range\n            var l = low\n            var h = high\n            while\
        \ (l <= h) {\n                val mid = l + (h - l) / 2\n                if\
        \ (arr(mid) >= target) {\n                    ans = mid\n                  \
        \  h = mid - 1\n                } else {\n                    l = mid + 1\n\
        \                }\n            }\n            ans\n        }\n\n        for\
        \ (i <- 0 until n) {\n            val s_i = sortedEvents(i)(0)\n           \
        \ val e_i = sortedEvents(i)(1)\n            val v_i = sortedEvents(i)(2)\n\n\
        \            // Case 1: Pick only event i\n            maxTotalValue = max(maxTotalValue,\
        \ v_i)\n\n            // Case 2: Pick event i and another non-overlapping event\
        \ after it\n            // Find the first event that starts at or after e_i\
        \ + 1\n            val targetStartTime = e_i + 1\n\n            // Search only\
        \ in events after the current one (i+1 to n-1)\n            val idx = lowerBound(startTimes,\
        \ targetStartTime, i + 1, n - 1)\n\n            if (idx < n) { // If such an\
        \ event exists\n                maxTotalValue = max(maxTotalValue, v_i + suffixMaxValues(idx))\n\
        \            }\n        }\n\n        maxTotalValue\n    }\n}"
      rust: "impl Solution {\n    pub fn max_two_events(mut events: Vec<Vec<i32>>) ->\
        \ i32 {\n        // Sort events by start time\n        events.sort_unstable_by_key(|e|\
        \ e[0]);\n\n        let n = events.len();\n\n        // suffix_max_values[i]\
        \ stores the maximum value of an event from events[i] to events[n-1]\n     \
        \   let mut suffix_max_values = vec![0; n];\n        suffix_max_values[n - 1]\
        \ = events[n - 1][2];\n        for i in (0..n - 1).rev() {\n            suffix_max_values[i]\
        \ = events[i][2].max(suffix_max_values[i + 1]);\n        }\n\n        let mut\
        \ max_total_value = 0;\n\n        // Extract start times for binary search\n\
        \        let start_times: Vec<i32> = events.iter().map(|e| e[0]).collect();\n\
        \n        for i in 0..n {\n            let s_i = events[i][0];\n           \
        \ let e_i = events[i][1];\n            let v_i = events[i][2];\n\n         \
        \   // Case 1: Pick only event i\n            max_total_value = max_total_value.max(v_i);\n\
        \n            // Case 2: Pick event i and another non-overlapping event after\
        \ it\n            // Find the first event that starts at or after e_i + 1\n\
        \            let target_start_time = e_i + 1;\n\n            // Use binary_search_by_key\
        \ for lower_bound\n            // Search only in events after the current one\
        \ (i+1 to n-1)\n            let search_range = &start_times[i + 1..n];\n   \
        \         let idx_in_range = search_range.binary_search(&target_start_time).unwrap_or_else(|e|\
        \ e);\n            let idx = (i + 1) + idx_in_range; // Adjust index to be relative\
        \ to the original start_times array\n\n            if idx < n { // If such an\
        \ event exists\n                max_total_value = max_total_value.max(v_i +\
        \ suffix_max_values[idx]);\n            }\n        }\n\n        max_total_value\n\
        \    }\n}"
      racket: "#lang racket\n\n(provide (rename-out [max-two-events-solution maxTwoEvents]))\n\
        \n(define (max-two-events-solution events)\n  ;; Sort events by start time\n\
        \  (define sorted-events (sort events (lambda (a b) (< (car a) (car b)))))\n\
        \  (define n (length sorted-events))\n\n  (when (zero? n) (error \"Empty events\
        \ list is not allowed by constraints\"))\n\n  ;; suffix-max-values[i] stores\
        \ the maximum value of an event from events[i] to events[n-1]\n  (define suffix-max-values\
        \ (make-vector n 0))\n  (vector-set! suffix-max-values (- n 1) (list-ref (list-ref\
        \ sorted-events (- n 1)) 2))\n  (for ([i (in-range (- n 2) -1 -1)])\n    (vector-set!\
        \ suffix-max-values i\n                 (max (list-ref (list-ref sorted-events\
        \ i) 2)\n                      (vector-ref suffix-max-values (+ i 1)))))\n\n\
        \  (define max-total-value 0)\n\n  ;; Extract start times for binary search\n\
        \  (define start-times (map car sorted-events))\n\n  ;; Custom binary search\
        \ for lower_bound (finds the first index where element >= target)\n  (define\
        \ (lower-bound arr target low high)\n    (define ans (+ high 1)) ;; Default\
        \ if no element found in range [low, high]\n    (define l low)\n    (define\
        \ h high)\n    (let loop ((l l) (h h) (ans ans))\n      (if (<= l h)\n     \
        \     (let* ((mid (+ l (quotient (- h l) 2))))\n            (if (>= (list-ref\
        \ arr mid) target)\n                (loop l (- mid 1) mid)\n               \
        \ (loop (+ mid 1) h ans)))\n          ans)))\n\n  (for ([i (in-range n)])\n\
        \    (define event-i (list-ref sorted-events i))\n    (define s-i (list-ref\
        \ event-i 0))\n    (define e-i (list-ref event-i 1))\n    (define v-i (list-ref\
        \ event-i 2))\n\n    ;; Case 1: Pick only event i\n    (set! max-total-value\
        \ (max max-total-value v-i))\n\n    ;; Case 2: Pick event i and another non-overlapping\
        \ event after it\n    ;; Find the first event that starts at or after e_i +\
        \ 1\n    (define target-start-time (+ e-i 1))\n\n    ;; Search only in events\
        \ after the current one (i+1 to n-1)\n    (define idx (lower-bound start-times\
        \ target-start-time (+ i 1) (- n 1)))\n\n    (when (< idx n) ;; If such an event\
        \ exists\n      (set! max-total-value (max max-total-value (+ v-i (vector-ref\
        \ suffix-max-values idx))))))\n\n  max-total-value)"
      erlang: "-module(solution).\n-export([maxTwoEvents/1]).\n\n-spec maxTwoEvents(Events\
        \ :: [[integer()]]) -> integer().\nmaxTwoEvents(Events) ->\n    % Sort events\
        \ by start time\n    SortedEvents = lists:sort(fun(A, B) -> element(1, A) <\
        \ element(1, B) end, Events),\n    N = length(SortedEvents),\n\n    % suffixMaxValues[i]\
        \ stores the maximum value of an event from events[i] to events[n-1]\n    %\
        \ Using an array for suffixMaxValues for O(1) access.\n    SuffixMaxValues =\
        \ array:new(N),\n    SuffixMaxValues = array:set(N-1, element(3, lists:nth(N,\
        \ SortedEvents)), SuffixMaxValues),\n    SuffixMaxValues = lists:foldl(\n  \
        \      fun(I, AccArray) ->\n            EventValue = element(3, lists:nth(I+1,\
        \ SortedEvents)),\n            PrevMax = array:get(I+1, AccArray),\n       \
        \     array:set(I, max(EventValue, PrevMax), AccArray)\n        end,\n     \
        \   SuffixMaxValues,\n        lists:seq(N-2, 0, -1)\n    ),\n\n    MaxTotalValue\
        \ = 0,\n\n    % Extract start times for binary search\n    StartTimes = [element(1,\
        \ Event) || Event <- SortedEvents],\n\n    % Custom binary search for lower_bound\
        \ (finds the first index where element >= target)\n    LowerBound = fun\n  \
        \      (Arr, Target, Low, High) ->\n            Ans = High + 1,\n          \
        \  LowerBoundLoop = fun\n                (L_curr, H_curr, Ans_curr) when L_curr\
        \ =< H_curr ->\n                    Mid = L_curr + (H_curr - L_curr) div 2,\n\
        \                    Element = lists:nth(Mid + 1, Arr), % lists:nth is 1-indexed\n\
        \                    if\n                        Element >= Target -> LowerBoundLoop(L_curr,\
        \ Mid - 1, Mid);\n                        true -> LowerBoundLoop(Mid + 1, H_curr,\
        \ Ans_curr)\n                    end;\n                (L_curr, H_curr, Ans_curr)\
        \ -> Ans_curr\n            end,\n            LowerBoundLoop(Low, High, Ans)\n\
        \    end,\n\n    MaxTotalValueLoop = fun\n        (Idx, AccMax, []) -> AccMax;\n\
        \        (Idx, AccMax, [{S_i, E_i, V_i}|RestEvents]) ->\n            % Case\
        \ 1: Pick only event i\n            CurrentMax = max(AccMax, V_i),\n\n     \
        \       % Case 2: Pick event i and another non-overlapping event after it\n\
        \            TargetStartTime = E_i + 1,\n\n            % Search in the range\
        \ [Idx + 1, N - 1]\n            SearchLow = Idx + 1,\n            SearchHigh\
        \ = N - 1,\n\n            Idx2 = if SearchLow =< SearchHigh -> LowerBound(StartTimes,\
        \ TargetStartTime, SearchLow, SearchHigh); true -> N end,\n\n            NewMax\
        \ = if\n                Idx2 < N ->\n                    V_Idx2 = array:get(Idx2,\
        \ SuffixMaxValues),\n                    max(CurrentMax, V_i + V_Idx2);\n  \
        \              true -> CurrentMax\n            end,\n            MaxTotalValueLoop(Idx\
        \ + 1, NewMax, RestEvents)\n    end,\n    MaxTotalValueLoop(0, MaxTotalValue,\
        \ SortedEvents)."
      elixir: "defmodule Solution do\n  @spec max_two_events(events :: [[integer]])\
        \ :: integer\n  def max_two_events(events) do\n    # Sort events by start time\n\
        \    sorted_events = Enum.sort(events, fn [s1, _, _], [s2, _, _] -> s1 < s2\
        \ end)\n\n    n = length(sorted_events)\n\n    # suffix_max_values[i] stores\
        \ the maximum value of an event from events[i] to events[n-1]\n    # Using an\
        \ array (list) for suffixMaxValues. Build it reversed for efficiency, then reverse\
        \ back.\n    suffix_max_values_rev = \n      Enum.reduce(Enum.reverse(sorted_events),\
        \ [], fn [_, _, value], acc ->\n        case acc do\n          [] -> [value]\n\
        \          [h | _] -> [max(value, h) | acc]\n        end\n      end)\n    suffix_max_values\
        \ = Enum.reverse(suffix_max_values_rev)\n\n    max_total_value = 0\n\n    #\
        \ Extract start times for binary search\n    start_times = Enum.map(sorted_events,\
        \ fn [s, _, _] -> s end)\n\n    # Custom binary search for lower_bound (finds\
        \ the first index where element >= target)\n    lower_bound = fn arr, target,\
        \ low, high ->\n      ans = high + 1 # Default if no element found in range\
        \ [low, high]\n\n      do_lower_bound = fn\n        (l_curr, h_curr, ans_curr)\
        \ when l_curr <= h_curr ->\n          mid = l_curr + div(h_curr - l_curr, 2)\n\
        \          element = Enum.at(arr, mid)\n          if element >= target do\n\
        \            do_lower_bound.(l_curr, mid - 1, mid)\n          else\n       \
        \     do_lower_bound.(mid + 1, h_curr, ans_curr)\n          end\n        (_,\
        \ _, ans_curr) -> ans_curr\n      end\n\n      do_lower_bound.(low, high, ans)\n\
        \    end\n\n    Enum.reduce(0..(n - 1), max_total_value, fn i, acc_max_total_value\
        \ ->\n      [s_i, e_i, v_i] = Enum.at(sorted_events, i)\n\n      # Case 1: Pick\
        \ only event i\n      current_max = max(acc_max_total_value, v_i)\n\n      #\
        \ Case 2: Pick event i and another non-overlapping event after it\n      # Find\
        \ the first event that starts at or after e_i + 1\n      target_start_time =\
        \ e_i + 1\n\n      # Search only in events after the current one (i+1 to n-1)\n\
        \      idx = lower_bound.(start_times, target_start_time, i + 1, n - 1)\n\n\
        \      if idx < n do # If such an event exists\n        max(current_max, v_i\
        \ + Enum.at(suffix_max_values, idx))\n      else\n        current_max\n    \
        \  end\n    end)\n  end\nend"
    approach: 'The problem asks to find the maximum sum of values from at most two non-overlapping
      events. This can be broken down into two cases: choosing a single event, or choosing
      two non-overlapping events. To efficiently handle the non-overlapping condition
      and maximize the sum, we first sort all events by their start times. This allows
      us to process events in chronological order.


      After sorting, we iterate through each event `events[i]` and consider it as the
      first of a potential pair of non-overlapping events. For each `events[i] = [s_i,
      e_i, v_i]`, we want to find a second event `events[j] = [s_j, e_j, v_j]` such
      that `s_j >= e_i + 1` (non-overlapping condition) and `v_j` is maximized. To quickly
      find the maximum `v_j` among events starting after `e_i`, we precompute a `suffix_max_values`
      array. `suffix_max_values[k]` stores the maximum value of any event from `events[k]`
      to `events[N-1]`. With this, we can use binary search (specifically, `lower_bound`)
      to find the first event `events[k]` whose start time is `>= e_i + 1`. If such
      an event `events[k]` exists, `v_i + suffix_max_values[k]` is a candidate for the
      maximum sum. We also continuously update the overall maximum sum with `v_i` itself,
      to cover the case where only one event is chosen. The maximum of all these candidates
      (single event values and sums of two events) will be the final answer.'
    time_complexity: The time complexity is O(N log N). This is dominated by sorting
      the events, which takes O(N log N). Building the `suffix_max_values` array takes
      O(N). The main loop iterates N times, and inside the loop, a binary search (e.g.,
      `bisect_left` or `lower_bound`) is performed, which takes O(log N). Thus, the
      loop contributes O(N log N) to the total time. Overall, the complexity is O(N
      log N).
    space_complexity: The space complexity is O(N). This is primarily due to storing
      the `suffix_max_values` array and the `start_times` array (used for binary search),
      both of which require O(N) space. If the sorting algorithm uses auxiliary space,
      it might also contribute to O(N) space, but in-place sorts would not. The problem
      constraints allow for N up to 10^5, making O(N) space acceptable.
    elapsed_time: 169.05312252044678
    model: gemini-2.5-flash
    generated_at: '2025-12-23 01:10:30 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxTwoEvents(vector<vector<int>>& events)\
        \ {\n        sort(events.begin(), events.end(), [](vector<int>& a, vector<int>&\
        \ b) {\n            return a[1] < b[1];\n        });\n        int maxSum = 0;\n\
        \        int maxVal = 0;\n        for (auto& event : events) {\n           \
        \ int start = event[0], end = event[1], val = event[2];\n            if (start\
        \ > maxVal) {\n                maxSum = max(maxSum, val + maxVal);\n       \
        \     } else {\n                maxSum = max(maxSum, val);\n            }\n\
        \            maxVal = max(maxVal, val);\n        }\n        return maxSum;\n\
        \    }\n};"
      java: "class Solution {\n    public int maxTwoEvents(int[][] events) {\n     \
        \   Arrays.sort(events, (a, b) -> a[1] - b[1]);\n        int maxSum = 0;\n \
        \       int maxVal = 0;\n        for (int[] event : events) {\n            int\
        \ start = event[0], end = event[1], val = event[2];\n            if (start >\
        \ maxVal) {\n                maxSum = Math.max(maxSum, val + maxVal);\n    \
        \        } else {\n                maxSum = Math.max(maxSum, val);\n       \
        \     }\n            maxVal = Math.max(maxVal, val);\n        }\n        return\
        \ maxSum;\n    }\n}"
      python: "class Solution:\n    def maxTwoEvents(self, events: List[List[int]])\
        \ -> int:\n        events.sort(key=lambda x: x[1])\n        max_sum = 0\n  \
        \      max_val = 0\n        for start, end, val in events:\n            if start\
        \ > max_val:\n                max_sum = max(max_sum, val + max_val)\n      \
        \      else:\n                max_sum = max(max_sum, val)\n            max_val\
        \ = max(max_val, val)\n        return max_sum"
      python3: "class Solution:\n    def maxTwoEvents(self, events: List[List[int]])\
        \ -> int:\n        events.sort(key=lambda x: x[1])\n        max_sum = 0\n  \
        \      max_val = 0\n        for start, end, val in events:\n            if start\
        \ > max_val:\n                max_sum = max(max_sum, val + max_val)\n      \
        \      else:\n                max_sum = max(max_sum, val)\n            max_val\
        \ = max(max_val, val)\n        return max_sum"
      c: "typedef struct {\n    int start;\n    int end;\n    int val;\n} Event;\n\n\
        int compare(const void *a, const void *b) {\n    Event *e1 = (Event *)a;\n \
        \   Event *e2 = (Event *)b;\n    return e1->end - e2->end;\n}\n\nint maxTwoEvents(int\
        \ **events, int eventsSize, int *eventsColSize) {\n    qsort(events, eventsSize,\
        \ sizeof(int *), compare);\n    int maxSum = 0;\n    int maxVal = 0;\n    for\
        \ (int i = 0; i < eventsSize; i++) {\n        int start = events[i][0], end\
        \ = events[i][1], val = events[i][2];\n        if (start > maxVal) {\n     \
        \       maxSum = (maxSum > val + maxVal) ? maxSum : val + maxVal;\n        }\
        \ else {\n            maxSum = (maxSum > val) ? maxSum : val;\n        }\n \
        \       maxVal = (maxVal > val) ? maxVal : val;\n    }\n    return maxSum;\n\
        }"
      csharp: "public class Solution {\n    public int MaxTwoEvents(int[][] events)\
        \ {\n        Array.Sort(events, (a, b) => a[1].CompareTo(b[1]));\n        int\
        \ maxSum = 0;\n        int maxVal = 0;\n        foreach (int[] event in events)\
        \ {\n            int start = event[0], end = event[1], val = event[2];\n   \
        \         if (start > maxVal) {\n                maxSum = Math.Max(maxSum, val\
        \ + maxVal);\n            } else {\n                maxSum = Math.Max(maxSum,\
        \ val);\n            }\n            maxVal = Math.Max(maxVal, val);\n      \
        \  }\n        return maxSum;\n    }\n}"
      javascript: "var maxTwoEvents = function(events) {\n    events.sort((a, b) =>\
        \ a[1] - b[1]);\n    let maxSum = 0;\n    let maxVal = 0;\n    for (let event\
        \ of events) {\n        let start = event[0], end = event[1], val = event[2];\n\
        \        if (start > maxVal) {\n            maxSum = Math.max(maxSum, val +\
        \ maxVal);\n        } else {\n            maxSum = Math.max(maxSum, val);\n\
        \        }\n        maxVal = Math.max(maxVal, val);\n    }\n    return maxSum;\n\
        };"
      typescript: "function maxTwoEvents(events: number[][]): number {\n    events.sort((a,\
        \ b) => a[1] - b[1]);\n    let maxSum: number = 0;\n    let maxVal: number =\
        \ 0;\n    for (let event of events) {\n        let start: number = event[0],\
        \ end: number = event[1], val: number = event[2];\n        if (start > maxVal)\
        \ {\n            maxSum = Math.max(maxSum, val + maxVal);\n        } else {\n\
        \            maxSum = Math.max(maxSum, val);\n        }\n        maxVal = Math.max(maxVal,\
        \ val);\n    }\n    return maxSum;\n}"
      php: "class Solution {\n    function maxTwoEvents($events) {\n        usort($events,\
        \ function($a, $b) {\n            return $a[1] - $b[1];\n        });\n     \
        \   $maxSum = 0;\n        $maxVal = 0;\n        foreach ($events as $event)\
        \ {\n            $start = $event[0];\n            $end = $event[1];\n      \
        \      $val = $event[2];\n            if ($start > $maxVal) {\n            \
        \    $maxSum = max($maxSum, $val + $maxVal);\n            } else {\n       \
        \         $maxSum = max($maxSum, $val);\n            }\n            $maxVal\
        \ = max($maxVal, $val);\n        }\n        return $maxSum;\n    }\n}"
      swift: "class Solution {\n    func maxTwoEvents(_ events: [[Int]]) -> Int {\n\
        \        let sortedEvents = events.sorted { $0[1] < $1[1] }\n        var maxSum\
        \ = 0\n        var maxVal = 0\n        for event in sortedEvents {\n       \
        \     let start = event[0], end = event[1], val = event[2]\n            if start\
        \ > maxVal {\n                maxSum = max(maxSum, val + maxVal)\n         \
        \   } else {\n                maxSum = max(maxSum, val)\n            }\n   \
        \         maxVal = max(maxVal, val)\n        }\n        return maxSum\n    }\n\
        }"
      kotlin: "class Solution {\n    fun maxTwoEvents(events: Array<IntArray>): Int\
        \ {\n        events.sortBy { it[1] }\n        var maxSum = 0\n        var maxVal\
        \ = 0\n        for (event in events) {\n            val start = event[0]\n \
        \           val end = event[1]\n            val val_ = event[2]\n          \
        \  if (start > maxVal) {\n                maxSum = maxOf(maxSum, val_ + maxVal)\n\
        \            } else {\n                maxSum = maxOf(maxSum, val_)\n      \
        \      }\n            maxVal = maxOf(maxVal, val_)\n        }\n        return\
        \ maxSum\n    }\n}"
      dart: "class Solution {\n    int maxTwoEvents(List<List<int>> events) {\n    \
        \    events.sort((a, b) => a[1].compareTo(b[1]));\n        int maxSum = 0;\n\
        \        int maxVal = 0;\n        for (var event in events) {\n            int\
        \ start = event[0], end = event[1], val = event[2];\n            if (start >\
        \ maxVal) {\n                maxSum = max(maxSum, val + maxVal);\n         \
        \   } else {\n                maxSum = max(maxSum, val);\n            }\n  \
        \          maxVal = max(maxVal, val);\n        }\n        return maxSum;\n \
        \   }\n}"
      go: "func maxTwoEvents(events [][]int) int {\n    sort.Slice(events, func(i, j\
        \ int) bool {\n        return events[i][1] < events[j][1]\n    })\n    maxSum\
        \ := 0\n    maxVal := 0\n    for _, event := range events {\n        start,\
        \ end, val := event[0], event[1], event[2]\n        if start > maxVal {\n  \
        \          maxSum = max(maxSum, val+maxVal)\n        } else {\n            maxSum\
        \ = max(maxSum, val)\n        }\n        maxVal = max(maxVal, val)\n    }\n\
        \    return maxSum\n}\n\nfunc max(a, b int) int {\n    if a > b {\n        return\
        \ a\n    }\n    return b\n}"
      ruby: "class Solution\n    def max_two_events(events)\n        events.sort_by!\
        \ { |event| event[1] }\n        max_sum = 0\n        max_val = 0\n        events.each\
        \ do |event|\n            start, end_, val = event\n            if start > max_val\n\
        \                max_sum = [max_sum, val + max_val].max\n            else\n\
        \                max_sum = [max_sum, val].max\n            end\n           \
        \ max_val = [max_val, val].max\n        end\n        max_sum\n    end\nend"
      scala: "object Solution {\n    def maxTwoEvents(events: Array[Array[Int]]): Int\
        \ = {\n        val sortedEvents = events.sortBy(_.apply(1))\n        var maxSum\
        \ = 0\n        var maxVal = 0\n        for (event <- sortedEvents) {\n     \
        \       val start = event.apply(0)\n            val end = event.apply(1)\n \
        \           val val_ = event.apply(2)\n            if (start > maxVal) {\n \
        \               maxSum = Math.max(maxSum, val_ + maxVal)\n            } else\
        \ {\n                maxSum = Math.max(maxSum, val_)\n            }\n      \
        \      maxVal = Math.max(maxVal, val_)\n        }\n        maxSum\n    }\n}"
      rust: "impl Solution {\n    pub fn max_two_events(mut events: Vec<Vec<i32>>) ->\
        \ i32 {\n        events.sort_by_key(|event| event[1]);\n        let mut max_sum\
        \ = 0;\n        let mut max_val = 0;\n        for event in events {\n      \
        \      let start = event[0];\n            let end = event[1];\n            let\
        \ val = event[2];\n            if start > max_val {\n                max_sum\
        \ = max_sum.max(val + max_val)\n            } else {\n                max_sum\
        \ = max_sum.max(val)\n            }\n            max_val = max_val.max(val)\n\
        \        }\n        max_sum\n    }\n}"
      racket: "define (max-two-events events)\n    (let ((sorted-events (sort events\
        \ (lambda (x y) (< (cadr x) (cadr y))))))\n        (let loop ((events sorted-events)\
        \ (max-sum 0) (max-val 0))\n            (if (null? events)\n               \
        \ max-sum\n                (let ((start (car (car events))) (end (cadr (car\
        \ events))) (val (caddr (car events))))\n                    (if (> start max-val)\n\
        \                        (loop (cdr events) (max max-sum (+ val max-val)) (max\
        \ max-val val))\n                        (loop (cdr events) (max max-sum val)\
        \ (max max-val val))))))))"
      erlang: "max_two_events(Events) ->\n    lists:foldl(fun({Start, End, Val}, {MaxSum,\
        \ MaxVal}) ->\n        case Start > MaxVal of\n            true -> {max(MaxSum,\
        \ Val + MaxVal), max(MaxVal, Val)};\n            false -> {max(MaxSum, Val),\
        \ max(MaxVal, Val)}\n        end\n    end, {0, 0}, lists:sort(fun({_, End1,\
        \ _}, {_, End2, _}) -> End1 =< End2 end, Events))."
      elixir: "def max_two_events(events) do\n    events\n    |> Enum.sort_by(&Enum.at(&1,\
        \ 1))\n    |> Enum.reduce({0, 0}, fn [start, _, val], {max_sum, max_val} ->\n\
        \        if start > max_val do\n            {max(max_sum, val + max_val), max(max_val,\
        \ val)}\n        else\n            {max(max_sum, val), max(max_val, val)}\n\
        \        end\n    end)\n    |> elem(0)\nend"
    approach: "The problem can be solved by first sorting the events based on their\
      \ end times. Then, for each event, we find the maximum value of the events that\
      \ do not overlap with it. This can be done by maintaining a variable that stores\
      \ the maximum value of the non-overlapping events. We update this variable as\
      \ we iterate through the events. The maximum sum of two non-overlapping events\
      \ is then the maximum of the current event's value plus the maximum value of the\
      \ non-overlapping events. The key intuition here is that by sorting the events\
      \ based on their end times, we can efficiently find the non-overlapping events\
      \ for each event. \n  The algorithm iterates through the sorted events, maintaining\
      \ a variable to store the maximum value of the non-overlapping events. For each\
      \ event, it checks if the event's start time is greater than the end time of the\
      \ previous non-overlapping event. If it is, it updates the maximum value of the\
      \ non-overlapping events. Then, it calculates the maximum sum of two non-overlapping\
      \ events by adding the current event's value to the maximum value of the non-overlapping\
      \ events. The maximum sum is updated if the calculated sum is greater than the\
      \ current maximum sum."
    time_complexity: The time complexity of the algorithm is O(n log n) due to the sorting
      of the events. The subsequent for loop iterates through the events once, resulting
      in a linear time complexity of O(n). Therefore, the overall time complexity is
      O(n log n) + O(n) = O(n log n).
    space_complexity: The space complexity of the algorithm is O(n) for storing the
      events. The algorithm also uses a constant amount of space to store the maximum
      sum and the maximum value of the non-overlapping events. Therefore, the overall
      space complexity is O(n).
    elapsed_time: 7.101532697677612
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-23 01:10:37 '
---

## Problem #2054: Two Best Non-Overlapping Events

**Difficulty:** Medium

**Topics:** Array, Binary Search, Dynamic Programming, Sorting, Heap (Priority Queue)

## Problem Description

<p>You are given a <strong>0-indexed</strong> 2D integer array of <code>events</code> where <code>events[i] = [startTime<sub>i</sub>, endTime<sub>i</sub>, value<sub>i</sub>]</code>. The <code>i<sup>th</sup></code> event starts at <code>startTime<sub>i</sub></code><sub> </sub>and ends at <code>endTime<sub>i</sub></code>, and if you attend this event, you will receive a value of <code>value<sub>i</sub></code>. You can choose <strong>at most</strong> <strong>two</strong> <strong>non-overlapping</strong> events to attend such that the sum of their values is <strong>maximized</strong>.</p>

<p>Return <em>this <strong>maximum</strong> sum.</em></p>

<p>Note that the start time and end time is <strong>inclusive</strong>: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time <code>t</code>, the next event must start at or after <code>t + 1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/09/21/picture5.png" style="width: 400px; height: 75px;" />
<pre>
<strong>Input:</strong> events = [[1,3,2],[4,5,2],[2,4,3]]
<strong>Output:</strong> 4
<strong>Explanation: </strong>Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="Example 1 Diagram" src="https://assets.leetcode.com/uploads/2021/09/21/picture1.png" style="width: 400px; height: 77px;" />
<pre>
<strong>Input:</strong> events = [[1,3,2],[4,5,2],[1,5,5]]
<strong>Output:</strong> 5
<strong>Explanation: </strong>Choose event 2 for a sum of 5.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/09/21/picture3.png" style="width: 400px; height: 66px;" />
<pre>
<strong>Input:</strong> events = [[1,5,3],[1,5,1],[6,6,5]]
<strong>Output:</strong> 8
<strong>Explanation: </strong>Choose events 0 and 2 for a sum of 3 + 5 = 8.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= events.length &lt;= 10<sup>5</sup></code></li>
	<li><code>events[i].length == 3</code></li>
	<li><code>1 &lt;= startTime<sub>i</sub> &lt;= endTime<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= value<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
</ul>


## Hints

1. How can sorting the events on the basis of their start times help? How about end times?

2. How can we quickly get the maximum score of an interval not intersecting with the interval we chose?

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-23 01:10:30 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks to find the maximum sum of values from at most two non-overlapping events. This can be broken down into two cases: choosing a single event, or choosing two non-overlapping events. To efficiently handle the non-overlapping condition and maximize the sum, we first sort all events by their start times. This allows us to process events in chronological order.

After sorting, we iterate through each event `events[i]` and consider it as the first of a potential pair of non-overlapping events. For each `events[i] = [s_i, e_i, v_i]`, we want to find a second event `events[j] = [s_j, e_j, v_j]` such that `s_j >= e_i + 1` (non-overlapping condition) and `v_j` is maximized. To quickly find the maximum `v_j` among events starting after `e_i`, we precompute a `suffix_max_values` array. `suffix_max_values[k]` stores the maximum value of any event from `events[k]` to `events[N-1]`. With this, we can use binary search (specifically, `lower_bound`) to find the first event `events[k]` whose start time is `>= e_i + 1`. If such an event `events[k]` exists, `v_i + suffix_max_values[k]` is a candidate for the maximum sum. We also continuously update the overall maximum sum with `v_i` itself, to cover the case where only one event is chosen. The maximum of all these candidates (single event values and sums of two events) will be the final answer.

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
#include <vector>
#include <algorithm>

class Solution {
public:
    int maxTwoEvents(std::vector<std::vector<int>>& events) {
        // Sort events by start time
        std::sort(events.begin(), events.end());

        int n = events.size();

        // suffixMaxValues[i] stores the maximum value of an event from events[i] to events[n-1]
        std::vector<int> suffixMaxValues(n);
        suffixMaxValues[n - 1] = events[n - 1][2];
        for (int i = n - 2; i >= 0; --i) {
            suffixMaxValues[i] = std::max(events[i][2], suffixMaxValues[i + 1]);
        }

        int maxTotalValue = 0;

        // Extract start times for binary search
        std::vector<int> startTimes(n);
        for (int i = 0; i < n; ++i) {
            startTimes[i] = events[i][0];
        }

        for (int i = 0; i < n; ++i) {
            int s_i = events[i][0];
            int e_i = events[i][1];
            int v_i = events[i][2];

            // Case 1: Pick only event i
            maxTotalValue = std::max(maxTotalValue, v_i);

            // Case 2: Pick event i and another non-overlapping event after it
            // Find the first event that starts at or after e_i + 1
            int targetStartTime = e_i + 1;

            // Use std::lower_bound to find the iterator to the first element
            // in the range [startTimes.begin() + i + 1, startTimes.end())
            // that is not less than targetStartTime.
            auto it = std::lower_bound(startTimes.begin() + i + 1, startTimes.end(), targetStartTime);

            // Calculate the index
            int idx = std::distance(startTimes.begin(), it);

            if (idx < n) {
                // If such an event exists, add its maximum possible value (from suffixMaxValues)
                maxTotalValue = std::max(maxTotalValue, v_i + suffixMaxValues[idx]);
            }
        }

        return maxTotalValue;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

class Solution {
    public int maxTwoEvents(int[][] events) {
        // Sort events by start time
        Arrays.sort(events, Comparator.comparingInt(a -> a[0]));

        int n = events.length;

        // suffixMaxValues[i] stores the maximum value of an event from events[i] to events[n-1]
        int[] suffixMaxValues = new int[n];
        suffixMaxValues[n - 1] = events[n - 1][2];
        for (int i = n - 2; i >= 0; i--) {
            suffixMaxValues[i] = Math.max(events[i][2], suffixMaxValues[i + 1]);
        }

        int maxTotalValue = 0;

        // Extract start times for binary search
        int[] startTimes = new int[n];
        for (int i = 0; i < n; i++) {
            startTimes[i] = events[i][0];
        }

        for (int i = 0; i < n; i++) {
            int s_i = events[i][0];
            int e_i = events[i][1];
            int v_i = events[i][2];

            // Case 1: Pick only event i
            maxTotalValue = Math.max(maxTotalValue, v_i);

            // Case 2: Pick event i and another non-overlapping event after it
            // Find the first event that starts at or after e_i + 1
            int targetStartTime = e_i + 1;

            // Use binary search to find the index of the first event whose start time is >= targetStartTime
            // Search only in events after the current one (i+1 to n-1)
            // Arrays.binarySearch returns: index if found, or (-(insertion point) - 1) if not found.
            // The insertion point is the index of the first element greater than the key, or n if all elements are less than the key.
            int idx = Arrays.binarySearch(startTimes, i + 1, n, targetStartTime);

            if (idx < 0) { // Not found, convert to insertion point
                idx = -(idx + 1);
            }

            if (idx < n) {
                // If such an event exists, add its maximum possible value (from suffixMaxValues)
                maxTotalValue = Math.max(maxTotalValue, v_i + suffixMaxValues[idx]);
            }
        }

        return maxTotalValue;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import bisect

class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        events.sort() # Sort by start time
        n = len(events)

        # suffix_max_values[i] stores the maximum value of an event from events[i] to events[n-1]
        suffix_max_values = [0] * n
        suffix_max_values[n-1] = events[n-1][2]
        for i in range(n - 2, -1, -1):
            suffix_max_values[i] = max(events[i][2], suffix_max_values[i+1])

        max_total_value = 0

        # Extract start times for binary search
        start_times = [event[0] for event in events]

        for i in range(n):
            s_i, e_i, v_i = events[i]

            # Case 1: Pick only event i
            max_total_value = max(max_total_value, v_i)

            # Case 2: Pick event i and another non-overlapping event after it
            # Find the first event that starts at or after e_i + 1
            target_start_time = e_i + 1

            # Use bisect_left to find the index of the first event whose start time is >= target_start_time
            # Search only in events after the current one (i+1 to n-1)
            idx = bisect.bisect_left(start_times, target_start_time, lo=i+1)

            if idx < n:
                # If such an event exists, add its maximum possible value (from suffix_max_values)
                max_total_value = max(max_total_value, v_i + suffix_max_values[idx])

        return max_total_value
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import bisect

class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        events.sort() # Sort by start time
        n = len(events)

        # suffix_max_values[i] stores the maximum value of an event from events[i] to events[n-1]
        suffix_max_values = [0] * n
        suffix_max_values[n-1] = events[n-1][2]
        for i in range(n - 2, -1, -1):
            suffix_max_values[i] = max(events[i][2], suffix_max_values[i+1])

        max_total_value = 0

        # Extract start times for binary search
        start_times = [event[0] for event in events]

        for i in range(n):
            s_i, e_i, v_i = events[i]

            # Case 1: Pick only event i
            max_total_value = max(max_total_value, v_i)

            # Case 2: Pick event i and another non-overlapping event after it
            # Find the first event that starts at or after e_i + 1
            target_start_time = e_i + 1

            # Use bisect_left to find the index of the first event whose start time is >= target_start_time
            # Search only in events after the current one (i+1 to n-1)
            idx = bisect.bisect_left(start_times, target_start_time, lo=i+1)

            if idx < n:
                # If such an event exists, add its maximum possible value (from suffix_max_values)
                max_total_value = max(max_total_value, v_i + suffix_max_values[idx])

        return max_total_value
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

// Comparison function for qsort
int compareEvents(const void *a, const void *b) {
    const int *eventA = *(const int **)a;
    const int *eventB = *(const int **)b;
    if (eventA[0] != eventB[0]) {
        return eventA[0] - eventB[0];
    }
    return eventA[1] - eventB[1]; // Secondary sort by end time (optional, but good for consistency)
}

// Manual binary search (lower_bound equivalent)
// Searches in the range [low, high] inclusive
int lower_bound_custom(int* arr, int low, int high, int target) {
    int ans = high + 1; // Default if no element found in range
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] >= target) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return ans;
}

int maxTwoEvents(int** events, int eventsSize, int* eventsColSize) {
    // Need to sort the array of pointers to events
    qsort(events, eventsSize, sizeof(int*), compareEvents);

    int n = eventsSize;

    int* suffixMaxValues = (int*)malloc(n * sizeof(int));
    if (!suffixMaxValues) return 0; // Handle allocation failure

    suffixMaxValues[n - 1] = events[n - 1][2];
    for (int i = n - 2; i >= 0; --i) {
        suffixMaxValues[i] = (events[i][2] > suffixMaxValues[i + 1]) ? events[i][2] : suffixMaxValues[i + 1];
    }

    int maxTotalValue = 0;

    int* startTimes = (int*)malloc(n * sizeof(int));
    if (!startTimes) {
        free(suffixMaxValues);
        return 0; // Handle allocation failure
    }
    for (int i = 0; i < n; ++i) {
        startTimes[i] = events[i][0];
    }

    for (int i = 0; i < n; ++i) {
        int s_i = events[i][0];
        int e_i = events[i][1];
        int v_i = events[i][2];

        maxTotalValue = (maxTotalValue > v_i) ? maxTotalValue : v_i;

        int targetStartTime = e_i + 1;

        // Search in the range [i + 1, n - 1]
        int idx = lower_bound_custom(startTimes, i + 1, n - 1, targetStartTime);

        if (idx < n) {
            maxTotalValue = (maxTotalValue > v_i + suffixMaxValues[idx]) ? maxTotalValue : v_i + suffixMaxValues[idx];
        }
    }

    free(suffixMaxValues);
    free(startTimes);

    return maxTotalValue;
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
    public int MaxTwoEvents(int[][] events) {
        // Sort events by start time
        Array.Sort(events, (a, b) => a[0].CompareTo(b[0]));

        int n = events.Length;

        // suffixMaxValues[i] stores the maximum value of an event from events[i] to events[n-1]
        int[] suffixMaxValues = new int[n];
        suffixMaxValues[n - 1] = events[n - 1][2];
        for (int i = n - 2; i >= 0; i--) {
            suffixMaxValues[i] = Math.Max(events[i][2], suffixMaxValues[i + 1]);
        }

        int maxTotalValue = 0;

        // Extract start times for binary search
        int[] startTimes = new int[n];
        for (int i = 0; i < n; i++) {
            startTimes[i] = events[i][0];
        }

        for (int i = 0; i < n; i++) {
            int s_i = events[i][0];
            int e_i = events[i][1];
            int v_i = events[i][2];

            // Case 1: Pick only event i
            maxTotalValue = Math.Max(maxTotalValue, v_i);

            // Case 2: Pick event i and another non-overlapping event after it
            // Find the first event that starts at or after e_i + 1
            int targetStartTime = e_i + 1;

            // Use Array.BinarySearch to find the index of the first event whose start time is >= targetStartTime
            // Search only in events after the current one (i+1 to n-1)
            // Array.BinarySearch returns: index if found, or (-(insertion point) - 1) if not found.
            // The insertion point is the index of the first element greater than the key, or n if all elements are less than the key.
            int idx = Array.BinarySearch(startTimes, i + 1, n - (i + 1), targetStartTime);

            if (idx < 0) { // Not found, convert to insertion point
                idx = ~idx; // Equivalent to -(idx + 1) in C#
            }

            if (idx < n) {
                // If such an event exists, add its maximum possible value (from suffixMaxValues)
                maxTotalValue = Math.Max(maxTotalValue, v_i + suffixMaxValues[idx]);
            }
        }

        return maxTotalValue;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[][]} events
 * @return {number}
 */
var maxTwoEvents = function(events) {
    // Sort events by start time
    events.sort((a, b) => a[0] - b[0]);

    const n = events.length;

    // suffixMaxValues[i] stores the maximum value of an event from events[i] to events[n-1]
    const suffixMaxValues = new Array(n).fill(0);
    suffixMaxValues[n - 1] = events[n - 1][2];
    for (let i = n - 2; i >= 0; i--) {
        suffixMaxValues[i] = Math.max(events[i][2], suffixMaxValues[i + 1]);
    }

    let maxTotalValue = 0;

    // Extract start times for binary search
    const startTimes = events.map(event => event[0]);

    // Custom binary search for lower_bound (finds the first index where element >= target)
    const lowerBound = (arr, target, low, high) => {
        let ans = high + 1; // Default if no element found in range [low, high]
        while (low <= high) {
            const mid = Math.floor(low + (high - low) / 2);
            if (arr[mid] >= target) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    };

    for (let i = 0; i < n; i++) {
        const [s_i, e_i, v_i] = events[i];

        // Case 1: Pick only event i
        maxTotalValue = Math.max(maxTotalValue, v_i);

        // Case 2: Pick event i and another non-overlapping event after it
        // Find the first event that starts at or after e_i + 1
        const targetStartTime = e_i + 1;

        // Search only in events after the current one (i+1 to n-1)
        const idx = lowerBound(startTimes, targetStartTime, i + 1, n - 1);

        if (idx < n) { // If such an event exists
            maxTotalValue = Math.max(maxTotalValue, v_i + suffixMaxValues[idx]);
        }
    }

    return maxTotalValue;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxTwoEvents(events: number[][]): number {
    // Sort events by start time
    events.sort((a, b) => a[0] - b[0]);

    const n = events.length;

    // suffixMaxValues[i] stores the maximum value of an event from events[i] to events[n-1]
    const suffixMaxValues: number[] = new Array(n).fill(0);
    suffixMaxValues[n - 1] = events[n - 1][2];
    for (let i = n - 2; i >= 0; i--) {
        suffixMaxValues[i] = Math.max(events[i][2], suffixMaxValues[i + 1]);
    }

    let maxTotalValue: number = 0;

    // Extract start times for binary search
    const startTimes: number[] = events.map(event => event[0]);

    // Custom binary search for lower_bound (finds the first index where element >= target)
    const lowerBound = (arr: number[], target: number, low: number, high: number): number => {
        let ans: number = high + 1; // Default if no element found in range [low, high]
        while (low <= high) {
            const mid = Math.floor(low + (high - low) / 2);
            if (arr[mid] >= target) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    };

    for (let i = 0; i < n; i++) {
        const [s_i, e_i, v_i] = events[i];

        // Case 1: Pick only event i
        maxTotalValue = Math.max(maxTotalValue, v_i);

        // Case 2: Pick event i and another non-overlapping event after it
        // Find the first event that starts at or after e_i + 1
        const targetStartTime: number = e_i + 1;

        // Search only in events after the current one (i+1 to n-1)
        const idx: number = lowerBound(startTimes, targetStartTime, i + 1, n - 1);

        if (idx < n) { // If such an event exists
            maxTotalValue = Math.max(maxTotalValue, v_i + suffixMaxValues[idx]);
        }
    }

    return maxTotalValue;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php
class Solution {

    /**
     * @param Integer[][] $events
     * @return Integer
     */
    function maxTwoEvents($events) {
        // Sort events by start time
        usort($events, function($a, $b) {
            return $a[0] - $b[0];
        });

        $n = count($events);

        // suffixMaxValues[i] stores the maximum value of an event from events[i] to events[n-1]
        $suffixMaxValues = array_fill(0, $n, 0);
        $suffixMaxValues[$n - 1] = $events[$n - 1][2];
        for ($i = $n - 2; $i >= 0; $i--) {
            $suffixMaxValues[$i] = max($events[$i][2], $suffixMaxValues[$i + 1]);
        }

        $maxTotalValue = 0;

        // Extract start times for binary search
        $startTimes = array_map(function($event) { return $event[0]; }, $events);

        // Custom binary search for lower_bound (finds the first index where element >= target)
        $lowerBound = function($arr, $target, $low, $high) use ($n) {
            $ans = $high + 1; // Default if no element found in range [low, high]
            while ($low <= $high) {
                $mid = floor($low + ($high - $low) / 2);
                if ($arr[$mid] >= $target) {
                    $ans = $mid;
                    $high = $mid - 1;
                } else {
                    $low = $mid + 1;
                }
            }
            return $ans;
        };

        for ($i = 0; $i < $n; $i++) {
            list($s_i, $e_i, $v_i) = $events[$i];

            // Case 1: Pick only event i
            $maxTotalValue = max($maxTotalValue, $v_i);

            // Case 2: Pick event i and another non-overlapping event after it
            // Find the first event that starts at or after e_i + 1
            $targetStartTime = $e_i + 1;

            // Search only in events after the current one (i+1 to n-1)
            $idx = $lowerBound($startTimes, $targetStartTime, $i + 1, $n - 1);

            if ($idx < $n) { // If such an event exists
                $maxTotalValue = max($maxTotalValue, $v_i + $suffixMaxValues[$idx]);
            }
        }

        return $maxTotalValue;
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
    func maxTwoEvents(_ events: [[Int]]) -> Int {
        // Sort events by start time
        var sortedEvents = events.sorted { $0[0] < $1[0] }

        let n = sortedEvents.count

        // suffixMaxValues[i] stores the maximum value of an event from events[i] to events[n-1]
        var suffixMaxValues = Array(repeating: 0, count: n)
        suffixMaxValues[n - 1] = sortedEvents[n - 1][2]
        for i in (0..<n - 1).reversed() {
            suffixMaxValues[i] = max(sortedEvents[i][2], suffixMaxValues[i + 1])
        }

        var maxTotalValue = 0

        // Extract start times for binary search
        let startTimes = sortedEvents.map { $0[0] }

        // Custom binary search for lower_bound (finds the first index where element >= target)
        func lowerBound(arr: [Int], target: Int, low: Int, high: Int) -> Int {
            var ans = high + 1 // Default if no element found in range [low, high]
            var l = low
            var h = high
            while l <= h {
                let mid = l + (h - l) / 2
                if arr[mid] >= target {
                    ans = mid
                    h = mid - 1
                } else {
                    l = mid + 1
                }
            }
            return ans
        }

        for i in 0..<n {
            let s_i = sortedEvents[i][0]
            let e_i = sortedEvents[i][1]
            let v_i = sortedEvents[i][2]

            // Case 1: Pick only event i
            maxTotalValue = max(maxTotalValue, v_i)

            // Case 2: Pick event i and another non-overlapping event after it
            // Find the first event that starts at or after e_i + 1
            let targetStartTime = e_i + 1

            // Search only in events after the current one (i+1 to n-1)
            let idx = lowerBound(arr: startTimes, target: targetStartTime, low: i + 1, high: n - 1)

            if idx < n { // If such an event exists
                maxTotalValue = max(maxTotalValue, v_i + suffixMaxValues[idx])
            }
        }

        return maxTotalValue
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import java.util.Arrays

class Solution {
    fun maxTwoEvents(events: Array<IntArray>): Int {
        // Sort events by start time
        events.sortBy { it[0] }

        val n = events.size

        // suffixMaxValues[i] stores the maximum value of an event from events[i] to events[n-1]
        val suffixMaxValues = IntArray(n)
        suffixMaxValues[n - 1] = events[n - 1][2]
        for (i in n - 2 downTo 0) {
            suffixMaxValues[i] = Math.max(events[i][2], suffixMaxValues[i + 1])
        }

        var maxTotalValue = 0

        // Extract start times for binary search
        val startTimes = IntArray(n) { i -> events[i][0] }

        for (i in 0 until n) {
            val s_i = events[i][0]
            val e_i = events[i][1]
            val v_i = events[i][2]

            // Case 1: Pick only event i
            maxTotalValue = Math.max(maxTotalValue, v_i)

            // Case 2: Pick event i and another non-overlapping event after it
            // Find the first event that starts at or after e_i + 1
            val targetStartTime = e_i + 1

            // Use binary search to find the index of the first event whose start time is >= targetStartTime
            // Search only in events after the current one (i+1 to n-1)
            // Arrays.binarySearch returns: index if found, or (-(insertion point) - 1) if not found.
            // The insertion point is the index of the first element greater than the key, or n if all elements are less than the key.
            var idx = startTimes.binarySearch(targetStartTime, i + 1, n)

            if (idx < 0) { // Not found, convert to insertion point
                idx = -(idx + 1)
            }

            if (idx < n) {
                // If such an event exists, add its maximum possible value (from suffixMaxValues)
                maxTotalValue = Math.max(maxTotalValue, v_i + suffixMaxValues[idx])
            }
        }

        return maxTotalValue
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
  int maxTwoEvents(List<List<int>> events) {
    // Sort events by start time
    events.sort((a, b) => a[0].compareTo(b[0]));

    final n = events.length;

    // suffixMaxValues[i] stores the maximum value of an event from events[i] to events[n-1]
    final suffixMaxValues = List<int>.filled(n, 0);
    suffixMaxValues[n - 1] = events[n - 1][2];
    for (int i = n - 2; i >= 0; i--) {
      suffixMaxValues[i] = max(events[i][2], suffixMaxValues[i + 1]);
    }

    int maxTotalValue = 0;

    // Extract start times for binary search
    final startTimes = events.map((event) => event[0]).toList();

    // Custom binary search for lower_bound (finds the first index where element >= target)
    int lowerBound(List<int> arr, int target, int low, int high) {
      int ans = high + 1; // Default if no element found in range [low, high]
      while (low <= high) {
        final mid = low + ((high - low) ~/ 2);
        if (arr[mid] >= target) {
          ans = mid;
          high = mid - 1;
        } else {
          low = mid + 1;
        }
      }
      return ans;
    }

    for (int i = 0; i < n; i++) {
      final s_i = events[i][0];
      final e_i = events[i][1];
      final v_i = events[i][2];

      // Case 1: Pick only event i
      maxTotalValue = max(maxTotalValue, v_i);

      // Case 2: Pick event i and another non-overlapping event after it
      // Find the first event that starts at or after e_i + 1
      final targetStartTime = e_i + 1;

      // Search only in events after the current one (i+1 to n-1)
      final idx = lowerBound(startTimes, targetStartTime, i + 1, n - 1);

      if (idx < n) { // If such an event exists
        maxTotalValue = max(maxTotalValue, v_i + suffixMaxValues[idx]);
      }
    }

    return maxTotalValue;
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
	"sort"
	"math"
)

func maxTwoEvents(events [][]int) int {
    // Sort events by start time
    sort.Slice(events, func(i, j int) bool {
        return events[i][0] < events[j][0]
    })

    n := len(events)

    // suffixMaxValues[i] stores the maximum value of an event from events[i] to events[n-1]
    suffixMaxValues := make([]int, n)
    suffixMaxValues[n-1] = events[n-1][2]
    for i := n - 2; i >= 0; i-- {
        suffixMaxValues[i] = int(math.Max(float64(events[i][2]), float64(suffixMaxValues[i+1])))
    }

    maxTotalValue := 0

    // Extract start times for binary search
    startTimes := make([]int, n)
    for i := 0; i < n; i++ {
        startTimes[i] = events[i][0]
    }

    for i := 0; i < n; i++ {
        s_i, e_i, v_i := events[i][0], events[i][1], events[i][2]

        // Case 1: Pick only event i
        maxTotalValue = int(math.Max(float64(maxTotalValue), float64(v_i)))

        // Case 2: Pick event i and another non-overlapping event after it
        // Find the first event that starts at or after e_i + 1
        targetStartTime := e_i + 1

        // Use sort.SearchInts for lower_bound (finds the first index where element >= target)
        // Search only in events after the current one (i+1 to n-1)
        // sort.SearchInts returns the smallest index i such that a[i] >= x.
        // If no such index exists, it returns len(a).
        idx := sort.SearchInts(startTimes[i+1:n], targetStartTime)
        idx += (i + 1) // Adjust index to be relative to the original startTimes array

        if idx < n { // If such an event exists
            maxTotalValue = int(math.Max(float64(maxTotalValue), float64(v_i + suffixMaxValues[idx])))
        }
    }

    return maxTotalValue
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    # @param {Integer[][]} events
    # @return {Integer}
    def max_two_events(events)
        # Sort events by start time
        events.sort! { |a, b| a[0] - b[0] }

        n = events.length

        # suffix_max_values[i] stores the maximum value of an event from events[i] to events[n-1]
        suffix_max_values = Array.new(n)
        suffix_max_values[n - 1] = events[n - 1][2]
        (n - 2).downto(0) do |i|
            suffix_max_values[i] = [events[i][2], suffix_max_values[i + 1]].max
        end

        max_total_value = 0

        # Extract start times for binary search
        start_times = events.map { |event| event[0] }

        # Custom binary search for lower_bound (finds the first index where element >= target)
        # Searches in the range [low, high] inclusive
        lower_bound = lambda do |arr, target, low, high|
            ans = high + 1 # Default if no element found in range
            while low <= high
                mid = low + (high - low) / 2
                if arr[mid] >= target
                    ans = mid
                    high = mid - 1
                else
                    low = mid + 1
                end
            end
            ans
        end

        for i in 0...n
            s_i, e_i, v_i = events[i]

            # Case 1: Pick only event i
            max_total_value = [max_total_value, v_i].max

            # Case 2: Pick event i and another non-overlapping event after it
            # Find the first event that starts at or after e_i + 1
            target_start_time = e_i + 1

            # Search only in events after the current one (i+1 to n-1)
            idx = lower_bound.call(start_times, target_start_time, i + 1, n - 1)

            if idx < n # If such an event exists
                max_total_value = [max_total_value, v_i + suffix_max_values[idx]].max
            end
        end

        return max_total_value
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable.ArrayBuffer
import scala.math.max

object Solution {
    def maxTwoEvents(events: Array[Array[Int]]): Int = {
        // Sort events by start time
        val sortedEvents = events.sortBy(_(0))

        val n = sortedEvents.length

        // suffixMaxValues[i] stores the maximum value of an event from events[i] to events[n-1]
        val suffixMaxValues = Array.ofDim[Int](n)
        suffixMaxValues(n - 1) = sortedEvents(n - 1)(2)
        for (i <- n - 2 to 0 by -1) {
            suffixMaxValues(i) = max(sortedEvents(i)(2), suffixMaxValues(i + 1))
        }

        var maxTotalValue = 0

        // Extract start times for binary search
        val startTimes = sortedEvents.map(_(0))

        // Custom binary search for lower_bound (finds the first index where element >= target)
        // Searches in the range [low, high] inclusive
        def lowerBound(arr: Array[Int], target: Int, low: Int, high: Int): Int = {
            var ans = high + 1 // Default if no element found in range
            var l = low
            var h = high
            while (l <= h) {
                val mid = l + (h - l) / 2
                if (arr(mid) >= target) {
                    ans = mid
                    h = mid - 1
                } else {
                    l = mid + 1
                }
            }
            ans
        }

        for (i <- 0 until n) {
            val s_i = sortedEvents(i)(0)
            val e_i = sortedEvents(i)(1)
            val v_i = sortedEvents(i)(2)

            // Case 1: Pick only event i
            maxTotalValue = max(maxTotalValue, v_i)

            // Case 2: Pick event i and another non-overlapping event after it
            // Find the first event that starts at or after e_i + 1
            val targetStartTime = e_i + 1

            // Search only in events after the current one (i+1 to n-1)
            val idx = lowerBound(startTimes, targetStartTime, i + 1, n - 1)

            if (idx < n) { // If such an event exists
                maxTotalValue = max(maxTotalValue, v_i + suffixMaxValues(idx))
            }
        }

        maxTotalValue
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_two_events(mut events: Vec<Vec<i32>>) -> i32 {
        // Sort events by start time
        events.sort_unstable_by_key(|e| e[0]);

        let n = events.len();

        // suffix_max_values[i] stores the maximum value of an event from events[i] to events[n-1]
        let mut suffix_max_values = vec![0; n];
        suffix_max_values[n - 1] = events[n - 1][2];
        for i in (0..n - 1).rev() {
            suffix_max_values[i] = events[i][2].max(suffix_max_values[i + 1]);
        }

        let mut max_total_value = 0;

        // Extract start times for binary search
        let start_times: Vec<i32> = events.iter().map(|e| e[0]).collect();

        for i in 0..n {
            let s_i = events[i][0];
            let e_i = events[i][1];
            let v_i = events[i][2];

            // Case 1: Pick only event i
            max_total_value = max_total_value.max(v_i);

            // Case 2: Pick event i and another non-overlapping event after it
            // Find the first event that starts at or after e_i + 1
            let target_start_time = e_i + 1;

            // Use binary_search_by_key for lower_bound
            // Search only in events after the current one (i+1 to n-1)
            let search_range = &start_times[i + 1..n];
            let idx_in_range = search_range.binary_search(&target_start_time).unwrap_or_else(|e| e);
            let idx = (i + 1) + idx_in_range; // Adjust index to be relative to the original start_times array

            if idx < n { // If such an event exists
                max_total_value = max_total_value.max(v_i + suffix_max_values[idx]);
            }
        }

        max_total_value
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(provide (rename-out [max-two-events-solution maxTwoEvents]))

(define (max-two-events-solution events)
  ;; Sort events by start time
  (define sorted-events (sort events (lambda (a b) (< (car a) (car b)))))
  (define n (length sorted-events))

  (when (zero? n) (error "Empty events list is not allowed by constraints"))

  ;; suffix-max-values[i] stores the maximum value of an event from events[i] to events[n-1]
  (define suffix-max-values (make-vector n 0))
  (vector-set! suffix-max-values (- n 1) (list-ref (list-ref sorted-events (- n 1)) 2))
  (for ([i (in-range (- n 2) -1 -1)])
    (vector-set! suffix-max-values i
                 (max (list-ref (list-ref sorted-events i) 2)
                      (vector-ref suffix-max-values (+ i 1)))))

  (define max-total-value 0)

  ;; Extract start times for binary search
  (define start-times (map car sorted-events))

  ;; Custom binary search for lower_bound (finds the first index where element >= target)
  (define (lower-bound arr target low high)
    (define ans (+ high 1)) ;; Default if no element found in range [low, high]
    (define l low)
    (define h high)
    (let loop ((l l) (h h) (ans ans))
      (if (<= l h)
          (let* ((mid (+ l (quotient (- h l) 2))))
            (if (>= (list-ref arr mid) target)
                (loop l (- mid 1) mid)
                (loop (+ mid 1) h ans)))
          ans)))

  (for ([i (in-range n)])
    (define event-i (list-ref sorted-events i))
    (define s-i (list-ref event-i 0))
    (define e-i (list-ref event-i 1))
    (define v-i (list-ref event-i 2))

    ;; Case 1: Pick only event i
    (set! max-total-value (max max-total-value v-i))

    ;; Case 2: Pick event i and another non-overlapping event after it
    ;; Find the first event that starts at or after e_i + 1
    (define target-start-time (+ e-i 1))

    ;; Search only in events after the current one (i+1 to n-1)
    (define idx (lower-bound start-times target-start-time (+ i 1) (- n 1)))

    (when (< idx n) ;; If such an event exists
      (set! max-total-value (max max-total-value (+ v-i (vector-ref suffix-max-values idx))))))

  max-total-value)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([maxTwoEvents/1]).

-spec maxTwoEvents(Events :: [[integer()]]) -> integer().
maxTwoEvents(Events) ->
    % Sort events by start time
    SortedEvents = lists:sort(fun(A, B) -> element(1, A) < element(1, B) end, Events),
    N = length(SortedEvents),

    % suffixMaxValues[i] stores the maximum value of an event from events[i] to events[n-1]
    % Using an array for suffixMaxValues for O(1) access.
    SuffixMaxValues = array:new(N),
    SuffixMaxValues = array:set(N-1, element(3, lists:nth(N, SortedEvents)), SuffixMaxValues),
    SuffixMaxValues = lists:foldl(
        fun(I, AccArray) ->
            EventValue = element(3, lists:nth(I+1, SortedEvents)),
            PrevMax = array:get(I+1, AccArray),
            array:set(I, max(EventValue, PrevMax), AccArray)
        end,
        SuffixMaxValues,
        lists:seq(N-2, 0, -1)
    ),

    MaxTotalValue = 0,

    % Extract start times for binary search
    StartTimes = [element(1, Event) || Event <- SortedEvents],

    % Custom binary search for lower_bound (finds the first index where element >= target)
    LowerBound = fun
        (Arr, Target, Low, High) ->
            Ans = High + 1,
            LowerBoundLoop = fun
                (L_curr, H_curr, Ans_curr) when L_curr =< H_curr ->
                    Mid = L_curr + (H_curr - L_curr) div 2,
                    Element = lists:nth(Mid + 1, Arr), % lists:nth is 1-indexed
                    if
                        Element >= Target -> LowerBoundLoop(L_curr, Mid - 1, Mid);
                        true -> LowerBoundLoop(Mid + 1, H_curr, Ans_curr)
                    end;
                (L_curr, H_curr, Ans_curr) -> Ans_curr
            end,
            LowerBoundLoop(Low, High, Ans)
    end,

    MaxTotalValueLoop = fun
        (Idx, AccMax, []) -> AccMax;
        (Idx, AccMax, [{S_i, E_i, V_i}|RestEvents]) ->
            % Case 1: Pick only event i
            CurrentMax = max(AccMax, V_i),

            % Case 2: Pick event i and another non-overlapping event after it
            TargetStartTime = E_i + 1,

            % Search in the range [Idx + 1, N - 1]
            SearchLow = Idx + 1,
            SearchHigh = N - 1,

            Idx2 = if SearchLow =< SearchHigh -> LowerBound(StartTimes, TargetStartTime, SearchLow, SearchHigh); true -> N end,

            NewMax = if
                Idx2 < N ->
                    V_Idx2 = array:get(Idx2, SuffixMaxValues),
                    max(CurrentMax, V_i + V_Idx2);
                true -> CurrentMax
            end,
            MaxTotalValueLoop(Idx + 1, NewMax, RestEvents)
    end,
    MaxTotalValueLoop(0, MaxTotalValue, SortedEvents).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_two_events(events :: [[integer]]) :: integer
  def max_two_events(events) do
    # Sort events by start time
    sorted_events = Enum.sort(events, fn [s1, _, _], [s2, _, _] -> s1 < s2 end)

    n = length(sorted_events)

    # suffix_max_values[i] stores the maximum value of an event from events[i] to events[n-1]
    # Using an array (list) for suffixMaxValues. Build it reversed for efficiency, then reverse back.
    suffix_max_values_rev = 
      Enum.reduce(Enum.reverse(sorted_events), [], fn [_, _, value], acc ->
        case acc do
          [] -> [value]
          [h | _] -> [max(value, h) | acc]
        end
      end)
    suffix_max_values = Enum.reverse(suffix_max_values_rev)

    max_total_value = 0

    # Extract start times for binary search
    start_times = Enum.map(sorted_events, fn [s, _, _] -> s end)

    # Custom binary search for lower_bound (finds the first index where element >= target)
    lower_bound = fn arr, target, low, high ->
      ans = high + 1 # Default if no element found in range [low, high]

      do_lower_bound = fn
        (l_curr, h_curr, ans_curr) when l_curr <= h_curr ->
          mid = l_curr + div(h_curr - l_curr, 2)
          element = Enum.at(arr, mid)
          if element >= target do
            do_lower_bound.(l_curr, mid - 1, mid)
          else
            do_lower_bound.(mid + 1, h_curr, ans_curr)
          end
        (_, _, ans_curr) -> ans_curr
      end

      do_lower_bound.(low, high, ans)
    end

    Enum.reduce(0..(n - 1), max_total_value, fn i, acc_max_total_value ->
      [s_i, e_i, v_i] = Enum.at(sorted_events, i)

      # Case 1: Pick only event i
      current_max = max(acc_max_total_value, v_i)

      # Case 2: Pick event i and another non-overlapping event after it
      # Find the first event that starts at or after e_i + 1
      target_start_time = e_i + 1

      # Search only in events after the current one (i+1 to n-1)
      idx = lower_bound.(start_times, target_start_time, i + 1, n - 1)

      if idx < n do # If such an event exists
        max(current_max, v_i + Enum.at(suffix_max_values, idx))
      else
        current_max
      end
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N log N). This is dominated by sorting the events, which takes O(N log N). Building the `suffix_max_values` array takes O(N). The main loop iterates N times, and inside the loop, a binary search (e.g., `bisect_left` or `lower_bound`) is performed, which takes O(log N). Thus, the loop contributes O(N log N) to the total time. Overall, the complexity is O(N log N).

- **Space Complexity:** The space complexity is O(N). This is primarily due to storing the `suffix_max_values` array and the `start_times` array (used for binary search), both of which require O(N) space. If the sorting algorithm uses auxiliary space, it might also contribute to O(N) space, but in-place sorts would not. The problem constraints allow for N up to 10^5, making O(N) space acceptable.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-23 01:10:37 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by first sorting the events based on their end times. Then, for each event, we find the maximum value of the events that do not overlap with it. This can be done by maintaining a variable that stores the maximum value of the non-overlapping events. We update this variable as we iterate through the events. The maximum sum of two non-overlapping events is then the maximum of the current event's value plus the maximum value of the non-overlapping events. The key intuition here is that by sorting the events based on their end times, we can efficiently find the non-overlapping events for each event. 
  The algorithm iterates through the sorted events, maintaining a variable to store the maximum value of the non-overlapping events. For each event, it checks if the event's start time is greater than the end time of the previous non-overlapping event. If it is, it updates the maximum value of the non-overlapping events. Then, it calculates the maximum sum of two non-overlapping events by adding the current event's value to the maximum value of the non-overlapping events. The maximum sum is updated if the calculated sum is greater than the current maximum sum.

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
    int maxTwoEvents(vector<vector<int>>& events) {
        sort(events.begin(), events.end(), [](vector<int>& a, vector<int>& b) {
            return a[1] < b[1];
        });
        int maxSum = 0;
        int maxVal = 0;
        for (auto& event : events) {
            int start = event[0], end = event[1], val = event[2];
            if (start > maxVal) {
                maxSum = max(maxSum, val + maxVal);
            } else {
                maxSum = max(maxSum, val);
            }
            maxVal = max(maxVal, val);
        }
        return maxSum;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maxTwoEvents(int[][] events) {
        Arrays.sort(events, (a, b) -> a[1] - b[1]);
        int maxSum = 0;
        int maxVal = 0;
        for (int[] event : events) {
            int start = event[0], end = event[1], val = event[2];
            if (start > maxVal) {
                maxSum = Math.max(maxSum, val + maxVal);
            } else {
                maxSum = Math.max(maxSum, val);
            }
            maxVal = Math.max(maxVal, val);
        }
        return maxSum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[1])
        max_sum = 0
        max_val = 0
        for start, end, val in events:
            if start > max_val:
                max_sum = max(max_sum, val + max_val)
            else:
                max_sum = max(max_sum, val)
            max_val = max(max_val, val)
        return max_sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[1])
        max_sum = 0
        max_val = 0
        for start, end, val in events:
            if start > max_val:
                max_sum = max(max_sum, val + max_val)
            else:
                max_sum = max(max_sum, val)
            max_val = max(max_val, val)
        return max_sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
typedef struct {
    int start;
    int end;
    int val;
} Event;

int compare(const void *a, const void *b) {
    Event *e1 = (Event *)a;
    Event *e2 = (Event *)b;
    return e1->end - e2->end;
}

int maxTwoEvents(int **events, int eventsSize, int *eventsColSize) {
    qsort(events, eventsSize, sizeof(int *), compare);
    int maxSum = 0;
    int maxVal = 0;
    for (int i = 0; i < eventsSize; i++) {
        int start = events[i][0], end = events[i][1], val = events[i][2];
        if (start > maxVal) {
            maxSum = (maxSum > val + maxVal) ? maxSum : val + maxVal;
        } else {
            maxSum = (maxSum > val) ? maxSum : val;
        }
        maxVal = (maxVal > val) ? maxVal : val;
    }
    return maxSum;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaxTwoEvents(int[][] events) {
        Array.Sort(events, (a, b) => a[1].CompareTo(b[1]));
        int maxSum = 0;
        int maxVal = 0;
        foreach (int[] event in events) {
            int start = event[0], end = event[1], val = event[2];
            if (start > maxVal) {
                maxSum = Math.Max(maxSum, val + maxVal);
            } else {
                maxSum = Math.Max(maxSum, val);
            }
            maxVal = Math.Max(maxVal, val);
        }
        return maxSum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var maxTwoEvents = function(events) {
    events.sort((a, b) => a[1] - b[1]);
    let maxSum = 0;
    let maxVal = 0;
    for (let event of events) {
        let start = event[0], end = event[1], val = event[2];
        if (start > maxVal) {
            maxSum = Math.max(maxSum, val + maxVal);
        } else {
            maxSum = Math.max(maxSum, val);
        }
        maxVal = Math.max(maxVal, val);
    }
    return maxSum;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxTwoEvents(events: number[][]): number {
    events.sort((a, b) => a[1] - b[1]);
    let maxSum: number = 0;
    let maxVal: number = 0;
    for (let event of events) {
        let start: number = event[0], end: number = event[1], val: number = event[2];
        if (start > maxVal) {
            maxSum = Math.max(maxSum, val + maxVal);
        } else {
            maxSum = Math.max(maxSum, val);
        }
        maxVal = Math.max(maxVal, val);
    }
    return maxSum;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function maxTwoEvents($events) {
        usort($events, function($a, $b) {
            return $a[1] - $b[1];
        });
        $maxSum = 0;
        $maxVal = 0;
        foreach ($events as $event) {
            $start = $event[0];
            $end = $event[1];
            $val = $event[2];
            if ($start > $maxVal) {
                $maxSum = max($maxSum, $val + $maxVal);
            } else {
                $maxSum = max($maxSum, $val);
            }
            $maxVal = max($maxVal, $val);
        }
        return $maxSum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxTwoEvents(_ events: [[Int]]) -> Int {
        let sortedEvents = events.sorted { $0[1] < $1[1] }
        var maxSum = 0
        var maxVal = 0
        for event in sortedEvents {
            let start = event[0], end = event[1], val = event[2]
            if start > maxVal {
                maxSum = max(maxSum, val + maxVal)
            } else {
                maxSum = max(maxSum, val)
            }
            maxVal = max(maxVal, val)
        }
        return maxSum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxTwoEvents(events: Array<IntArray>): Int {
        events.sortBy { it[1] }
        var maxSum = 0
        var maxVal = 0
        for (event in events) {
            val start = event[0]
            val end = event[1]
            val val_ = event[2]
            if (start > maxVal) {
                maxSum = maxOf(maxSum, val_ + maxVal)
            } else {
                maxSum = maxOf(maxSum, val_)
            }
            maxVal = maxOf(maxVal, val_)
        }
        return maxSum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int maxTwoEvents(List<List<int>> events) {
        events.sort((a, b) => a[1].compareTo(b[1]));
        int maxSum = 0;
        int maxVal = 0;
        for (var event in events) {
            int start = event[0], end = event[1], val = event[2];
            if (start > maxVal) {
                maxSum = max(maxSum, val + maxVal);
            } else {
                maxSum = max(maxSum, val);
            }
            maxVal = max(maxVal, val);
        }
        return maxSum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxTwoEvents(events [][]int) int {
    sort.Slice(events, func(i, j int) bool {
        return events[i][1] < events[j][1]
    })
    maxSum := 0
    maxVal := 0
    for _, event := range events {
        start, end, val := event[0], event[1], event[2]
        if start > maxVal {
            maxSum = max(maxSum, val+maxVal)
        } else {
            maxSum = max(maxSum, val)
        }
        maxVal = max(maxVal, val)
    }
    return maxSum
}

func max(a, b int) int {
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
    def max_two_events(events)
        events.sort_by! { |event| event[1] }
        max_sum = 0
        max_val = 0
        events.each do |event|
            start, end_, val = event
            if start > max_val
                max_sum = [max_sum, val + max_val].max
            else
                max_sum = [max_sum, val].max
            end
            max_val = [max_val, val].max
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
    def maxTwoEvents(events: Array[Array[Int]]): Int = {
        val sortedEvents = events.sortBy(_.apply(1))
        var maxSum = 0
        var maxVal = 0
        for (event <- sortedEvents) {
            val start = event.apply(0)
            val end = event.apply(1)
            val val_ = event.apply(2)
            if (start > maxVal) {
                maxSum = Math.max(maxSum, val_ + maxVal)
            } else {
                maxSum = Math.max(maxSum, val_)
            }
            maxVal = Math.max(maxVal, val_)
        }
        maxSum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_two_events(mut events: Vec<Vec<i32>>) -> i32 {
        events.sort_by_key(|event| event[1]);
        let mut max_sum = 0;
        let mut max_val = 0;
        for event in events {
            let start = event[0];
            let end = event[1];
            let val = event[2];
            if start > max_val {
                max_sum = max_sum.max(val + max_val)
            } else {
                max_sum = max_sum.max(val)
            }
            max_val = max_val.max(val)
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
define (max-two-events events)
    (let ((sorted-events (sort events (lambda (x y) (< (cadr x) (cadr y))))))
        (let loop ((events sorted-events) (max-sum 0) (max-val 0))
            (if (null? events)
                max-sum
                (let ((start (car (car events))) (end (cadr (car events))) (val (caddr (car events))))
                    (if (> start max-val)
                        (loop (cdr events) (max max-sum (+ val max-val)) (max max-val val))
                        (loop (cdr events) (max max-sum val) (max max-val val))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
max_two_events(Events) ->
    lists:foldl(fun({Start, End, Val}, {MaxSum, MaxVal}) ->
        case Start > MaxVal of
            true -> {max(MaxSum, Val + MaxVal), max(MaxVal, Val)};
            false -> {max(MaxSum, Val), max(MaxVal, Val)}
        end
    end, {0, 0}, lists:sort(fun({_, End1, _}, {_, End2, _}) -> End1 =< End2 end, Events)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
def max_two_events(events) do
    events
    |> Enum.sort_by(&Enum.at(&1, 1))
    |> Enum.reduce({0, 0}, fn [start, _, val], {max_sum, max_val} ->
        if start > max_val do
            {max(max_sum, val + max_val), max(max_val, val)}
        else
            {max(max_sum, val), max(max_val, val)}
        end
    end)
    |> elem(0)
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of the algorithm is O(n log n) due to the sorting of the events. The subsequent for loop iterates through the events once, resulting in a linear time complexity of O(n). Therefore, the overall time complexity is O(n log n) + O(n) = O(n log n).

- **Space Complexity:** The space complexity of the algorithm is O(n) for storing the events. The algorithm also uses a constant amount of space to store the maximum sum and the maximum value of the non-overlapping events. Therefore, the overall space complexity is O(n).

</div>
</details>
