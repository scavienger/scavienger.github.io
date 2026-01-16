---
layout: post
title: "Maximum Square Area by Removing Fences From a Field"
date: 2026-01-16 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Enumeration"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int maximizeSquareArea(int m, int n, vector<int>&\
        \ hFences, vector<int>& vFences) {\n        vector<int> allHFences = hFences;\n\
        \        allHFences.push_back(1);\n        allHFences.push_back(m);\n      \
        \  sort(allHFences.begin(), allHFences.end());\n        allHFences.erase(unique(allHFences.begin(),\
        \ allHFences.end()), allHFences.end());\n\n        vector<int> allVFences =\
        \ vFences;\n        allVFences.push_back(1);\n        allVFences.push_back(n);\n\
        \        sort(allVFences.begin(), allVFences.end());\n        allVFences.erase(unique(allVFences.begin(),\
        \ allVFences.end()), allVFences.end());\n\n        unordered_set<long long>\
        \ hDiffs;\n        for (int i = 0; i < allHFences.size(); ++i) {\n         \
        \   for (int j = i + 1; j < allHFences.size(); ++j) {\n                hDiffs.insert(allHFences[j]\
        \ - allHFences[i]);\n            }\n        }\n\n        long long maxSide =\
        \ 0;\n        for (int i = 0; i < allVFences.size(); ++i) {\n            for\
        \ (int j = i + 1; j < allVFences.size(); ++j) {\n                long long diff\
        \ = allVFences[j] - allVFences[i];\n                if (hDiffs.count(diff))\
        \ {\n                    maxSide = max(maxSide, diff);\n                }\n\
        \            }\n        }\n\n        if (maxSide == 0) {\n            return\
        \ -1;\n        }\n\n        long long MOD = 1e9 + 7;\n        return (int)((maxSide\
        \ * maxSide) % MOD);\n    }\n};"
      java: "import java.util.Arrays;\nimport java.util.HashSet;\nimport java.util.Set;\n\
        import java.util.ArrayList;\nimport java.util.Collections;\n\nclass Solution\
        \ {\n    public int maximizeSquareArea(int m, int n, int[] hFences, int[] vFences)\
        \ {\n        ArrayList<Integer> allHFencesList = new ArrayList<>();\n      \
        \  for (int fence : hFences) {\n            allHFencesList.add(fence);\n   \
        \     }\n        allHFencesList.add(1);\n        allHFencesList.add(m);\n  \
        \      Collections.sort(allHFencesList);\n\n        // Remove duplicates (Java's\
        \ ArrayList doesn't have unique, so use a Set then convert back)\n        Set<Integer>\
        \ uniqueHFences = new HashSet<>(allHFencesList);\n        allHFencesList.clear();\n\
        \        allHFencesList.addAll(uniqueHFences);\n        Collections.sort(allHFencesList);\n\
        \n        ArrayList<Integer> allVFencesList = new ArrayList<>();\n        for\
        \ (int fence : vFences) {\n            allVFencesList.add(fence);\n        }\n\
        \        allVFencesList.add(1);\n        allVFencesList.add(n);\n        Collections.sort(allVFencesList);\n\
        \n        Set<Integer> uniqueVFences = new HashSet<>(allVFencesList);\n    \
        \    allVFencesList.clear();\n        allVFencesList.addAll(uniqueVFences);\n\
        \        Collections.sort(allVFencesList);\n\n        Set<Long> hDiffs = new\
        \ HashSet<>();\n        for (int i = 0; i < allHFencesList.size(); ++i) {\n\
        \            for (int j = i + 1; j < allHFencesList.size(); ++j) {\n       \
        \         hDiffs.add((long)allHFencesList.get(j) - allHFencesList.get(i));\n\
        \            }\n        }\n\n        long maxSide = 0;\n        for (int i =\
        \ 0; i < allVFencesList.size(); ++i) {\n            for (int j = i + 1; j <\
        \ allVFencesList.size(); ++j) {\n                long diff = (long)allVFencesList.get(j)\
        \ - allVFencesList.get(i);\n                if (hDiffs.contains(diff)) {\n \
        \                   maxSide = Math.max(maxSide, diff);\n                }\n\
        \            }\n        }\n\n        if (maxSide == 0) {\n            return\
        \ -1;\n        }\n\n        long MOD = 1_000_000_007L;\n        return (int)((maxSide\
        \ * maxSide) % MOD);\n    }\n}"
      python: "class Solution(object):\n    def maximizeSquareArea(self, m, n, hFences,\
        \ vFences):\n        \"\"\"\n        :type m: int\n        :type n: int\n  \
        \      :type hFences: List[int]\n        :type vFences: List[int]\n        :rtype:\
        \ int\n        \"\"\"\n        all_h_fences = sorted(list(set(hFences + [1,\
        \ m])))\n        all_v_fences = sorted(list(set(vFences + [1, n])))\n\n    \
        \    h_diffs = set()\n        for i in range(len(all_h_fences)):\n         \
        \   for j in range(i + 1, len(all_h_fences)):\n                h_diffs.add(all_h_fences[j]\
        \ - all_h_fences[i])\n\n        max_side = 0\n        for i in range(len(all_v_fences)):\n\
        \            for j in range(i + 1, len(all_v_fences)):\n                diff\
        \ = all_v_fences[j] - all_v_fences[i]\n                if diff in h_diffs:\n\
        \                    max_side = max(max_side, diff)\n\n        if max_side ==\
        \ 0:\n            return -1\n\n        MOD = 10**9 + 7\n        return (max_side\
        \ * max_side) % MOD"
      python3: "class Solution:\n    def maximizeSquareArea(self, m: int, n: int, hFences:\
        \ List[int], vFences: List[int]) -> int:\n        all_h_fences = sorted(list(set(hFences\
        \ + [1, m])))\n        all_v_fences = sorted(list(set(vFences + [1, n])))\n\n\
        \        h_diffs = set()\n        for i in range(len(all_h_fences)):\n     \
        \       for j in range(i + 1, len(all_h_fences)):\n                h_diffs.add(all_h_fences[j]\
        \ - all_h_fences[i])\n\n        max_side = 0\n        for i in range(len(all_v_fences)):\n\
        \            for j in range(i + 1, len(all_v_fences)):\n                diff\
        \ = all_v_fences[j] - all_v_fences[i]\n                if diff in h_diffs:\n\
        \                    max_side = max(max_side, diff)\n\n        if max_side ==\
        \ 0:\n            return -1\n\n        MOD = 10**9 + 7\n        return (max_side\
        \ * max_side) % MOD"
      c: "#include <stdlib.h>\n#include <stdio.h>\n#include <stdbool.h>\n\n// Custom\
        \ comparison function for qsort\nint compare(const void *a, const void *b) {\n\
        \    return (*(int*)a - *(int*)b);\n}\n\n// Function to remove duplicates from\
        \ a sorted array and return new size\nint removeDuplicates(int* arr, int size)\
        \ {\n    if (size == 0) return 0;\n    int j = 0;\n    for (int i = 1; i < size;\
        \ i++) {\n        if (arr[i] != arr[j]) {\n            j++;\n            arr[j]\
        \ = arr[i];\n        }\n    }\n    return j + 1;\n}\n\n// Function to check\
        \ if an element exists in a sorted array (binary search)\nbool contains(int*\
        \ arr, int size, int val) {\n    int low = 0, high = size - 1;\n    while (low\
        \ <= high) {\n        int mid = low + (high - low) / 2;\n        if (arr[mid]\
        \ == val) {\n            return true;\n        } else if (arr[mid] < val) {\n\
        \            low = mid + 1;\n        } else {\n            high = mid - 1;\n\
        \        }\n    }\n    return false;\n}\n\nint maximizeSquareArea(int m, int\
        \ n, int* hFences, int hFencesSize, int* vFences, int vFencesSize) {\n    //\
        \ Max possible fences: 600 + 2 = 602\n    int* allHFences = (int*)malloc(sizeof(int)\
        \ * (hFencesSize + 2));\n    for (int i = 0; i < hFencesSize; i++) {\n     \
        \   allHFences[i] = hFences[i];\n    }\n    allHFences[hFencesSize] = 1;\n \
        \   allHFences[hFencesSize + 1] = m;\n    int currentHFencesSize = hFencesSize\
        \ + 2;\n    qsort(allHFences, currentHFencesSize, sizeof(int), compare);\n \
        \   currentHFencesSize = removeDuplicates(allHFences, currentHFencesSize);\n\
        \n    int* allVFences = (int*)malloc(sizeof(int) * (vFencesSize + 2));\n   \
        \ for (int i = 0; i < vFencesSize; i++) {\n        allVFences[i] = vFences[i];\n\
        \    }\n    allVFences[vFencesSize] = 1;\n    allVFences[vFencesSize + 1] =\
        \ n;\n    int currentVFencesSize = vFencesSize + 2;\n    qsort(allVFences, currentVFencesSize,\
        \ sizeof(int), compare);\n    currentVFencesSize = removeDuplicates(allVFences,\
        \ currentVFencesSize);\n\n    // Max possible differences: (602 * 601) / 2 =\
        \ 180901\n    int* hDiffs = (int*)malloc(sizeof(int) * (currentHFencesSize *\
        \ (currentHFencesSize - 1) / 2));\n    int hDiffsCount = 0;\n    for (int i\
        \ = 0; i < currentHFencesSize; i++) {\n        for (int j = i + 1; j < currentHFencesSize;\
        \ j++) {\n            hDiffs[hDiffsCount++] = allHFences[j] - allHFences[i];\n\
        \        }\n    }\n    qsort(hDiffs, hDiffsCount, sizeof(int), compare);\n \
        \   hDiffsCount = removeDuplicates(hDiffs, hDiffsCount);\n\n    long long maxSide\
        \ = 0;\n    for (int i = 0; i < currentVFencesSize; i++) {\n        for (int\
        \ j = i + 1; j < currentVFencesSize; j++) {\n            int diff = allVFences[j]\
        \ - allVFences[i];\n            if (contains(hDiffs, hDiffsCount, diff)) {\n\
        \                if (diff > maxSide) {\n                    maxSide = diff;\n\
        \                }\n            }\n        }\n    }\n\n    free(allHFences);\n\
        \    free(allVFences);\n    free(hDiffs);\n\n    if (maxSide == 0) {\n     \
        \   return -1;\n    }\n\n    long long MOD = 1000000007LL;\n    return (int)((maxSide\
        \ * maxSide) % MOD);\n}"
      csharp: "using System;\nusing System.Collections.Generic;\nusing System.Linq;\n\
        \npublic class Solution {\n    public int MaximizeSquareArea(int m, int n, int[]\
        \ hFences, int[] vFences) {\n        List<int> allHFencesList = new List<int>(hFences);\n\
        \        allHFencesList.Add(1);\n        allHFencesList.Add(m);\n        allHFencesList\
        \ = allHFencesList.Distinct().OrderBy(x => x).ToList();\n\n        List<int>\
        \ allVFencesList = new List<int>(vFences);\n        allVFencesList.Add(1);\n\
        \        allVFencesList.Add(n);\n        allVFencesList = allVFencesList.Distinct().OrderBy(x\
        \ => x).ToList();\n\n        HashSet<long> hDiffs = new HashSet<long>();\n \
        \       for (int i = 0; i < allHFencesList.Count; i++) {\n            for (int\
        \ j = i + 1; j < allHFencesList.Count; j++) {\n                hDiffs.Add((long)allHFencesList[j]\
        \ - allHFencesList[i]);\n            }\n        }\n\n        long maxSide =\
        \ 0;\n        for (int i = 0; i < allVFencesList.Count; i++) {\n           \
        \ for (int j = i + 1; j < allVFencesList.Count; j++) {\n                long\
        \ diff = (long)allVFencesList[j] - allVFencesList[i];\n                if (hDiffs.Contains(diff))\
        \ {\n                    maxSide = Math.Max(maxSide, diff);\n              \
        \  }\n            }\n        }\n\n        if (maxSide == 0) {\n            return\
        \ -1;\n        }\n\n        long MOD = 1_000_000_007L;\n        return (int)((maxSide\
        \ * maxSide) % MOD);\n    }\n}"
      javascript: "/**\n * @param {number} m\n * @param {number} n\n * @param {number[]}\
        \ hFences\n * @param {number[]} vFences\n * @return {number}\n */\nvar maximizeSquareArea\
        \ = function(m, n, hFences, vFences) {\n    let allHFences = [...new Set([...hFences,\
        \ 1, m])].sort((a, b) => a - b);\n    let allVFences = [...new Set([...vFences,\
        \ 1, n])].sort((a, b) => a - b);\n\n    let hDiffs = new Set();\n    for (let\
        \ i = 0; i < allHFences.length; i++) {\n        for (let j = i + 1; j < allHFences.length;\
        \ j++) {\n            hDiffs.add(allHFences[j] - allHFences[i]);\n        }\n\
        \    }\n\n    let maxSide = 0;\n    for (let i = 0; i < allVFences.length; i++)\
        \ {\n        for (let j = i + 1; j < allVFences.length; j++) {\n           \
        \ let diff = allVFences[j] - allVFences[i];\n            if (hDiffs.has(diff))\
        \ {\n                maxSide = Math.max(maxSide, diff);\n            }\n   \
        \     }\n    }\n\n    if (maxSide === 0) {\n        return -1;\n    }\n\n  \
        \  const MOD = 10**9 + 7;\n    return (Number(maxSide) * Number(maxSide)) %\
        \ MOD;\n};"
      typescript: "function maximizeSquareArea(m: number, n: number, hFences: number[],\
        \ vFences: number[]): number {\n    let allHFences = [...new Set([...hFences,\
        \ 1, m])].sort((a, b) => a - b);\n    let allVFences = [...new Set([...vFences,\
        \ 1, n])].sort((a, b) => a - b);\n\n    let hDiffs: Set<number> = new Set();\n\
        \    for (let i = 0; i < allHFences.length; i++) {\n        for (let j = i +\
        \ 1; j < allHFences.length; j++) {\n            hDiffs.add(allHFences[j] - allHFences[i]);\n\
        \        }\n    }\n\n    let maxSide: number = 0;\n    for (let i = 0; i < allVFences.length;\
        \ i++) {\n        for (let j = i + 1; j < allVFences.length; j++) {\n      \
        \      let diff = allVFences[j] - allVFences[i];\n            if (hDiffs.has(diff))\
        \ {\n                maxSide = Math.max(maxSide, diff);\n            }\n   \
        \     }\n    }\n\n    if (maxSide === 0) {\n        return -1;\n    }\n\n  \
        \  const MOD = 10**9 + 7;\n    // Use BigInt for multiplication to prevent overflow\
        \ before modulo, then convert back to number\n    return Number((BigInt(maxSide)\
        \ * BigInt(maxSide)) % BigInt(MOD));\n};"
      php: "<?php\nclass Solution {\n\n    /**\n     * @param Integer $m\n     * @param\
        \ Integer $n\n     * @param Integer[] $hFences\n     * @param Integer[] $vFences\n\
        \     * @return Integer\n     */\n    function maximizeSquareArea($m, $n, $hFences,\
        \ $vFences) {\n        $allHFences = array_unique(array_merge($hFences, [1,\
        \ $m]));\n        sort($allHFences);\n\n        $allVFences = array_unique(array_merge($vFences,\
        \ [1, $n]));\n        sort($allVFences);\n\n        $hDiffs = [];\n        for\
        \ ($i = 0; $i < count($allHFences); $i++) {\n            for ($j = $i + 1; $j\
        \ < count($allHFences); $j++) {\n                $hDiffs[$allHFences[$j] - $allHFences[$i]]\
        \ = true; // Use as a hash set\n            }\n        }\n\n        $maxSide\
        \ = 0;\n        for ($i = 0; $i < count($allVFences); $i++) {\n            for\
        \ ($j = $i + 1; $j < count($allVFences); $j++) {\n                $diff = $allVFences[$j]\
        \ - $allVFences[$i];\n                if (isset($hDiffs[$diff])) {\n       \
        \             $maxSide = max($maxSide, $diff);\n                }\n        \
        \    }\n        }\n\n        if ($maxSide == 0) {\n            return -1;\n\
        \        }\n\n        $MOD = 10**9 + 7;\n        // PHP integers handle large\
        \ values automatically up to system limits, but explicit casting to int is needed\
        \ for return type.\n        // For modulo, ensure calculation is done with large\
        \ numbers if necessary.\n        return (int)(($maxSide * $maxSide) % $MOD);\n\
        \    }\n}\n?>"
      swift: "class Solution {\n    func maximizeSquareArea(_ m: Int, _ n: Int, _ hFences:\
        \ [Int], _ vFences: [Int]) -> Int {\n        var allHFences = Set(hFences +\
        \ [1, m]).sorted()\n        var allVFences = Set(vFences + [1, n]).sorted()\n\
        \n        var hDiffs = Set<Int>()\n        for i in 0..<allHFences.count {\n\
        \            for j in (i + 1)..<allHFences.count {\n                hDiffs.insert(allHFences[j]\
        \ - allHFences[i])\n            }\n        }\n\n        var maxSide: Int = 0\n\
        \        for i in 0..<allVFences.count {\n            for j in (i + 1)..<allVFences.count\
        \ {\n                let diff = allVFences[j] - allVFences[i]\n            \
        \    if hDiffs.contains(diff) {\n                    maxSide = max(maxSide,\
        \ diff)\n                }\n            }\n        }\n\n        if maxSide ==\
        \ 0 {\n            return -1\n        }\n\n        let MOD = 1_000_000_007\n\
        \        // Use Int64 for multiplication to prevent overflow before modulo\n\
        \        return Int((Int64(maxSide) * Int64(maxSide)) % Int64(MOD))\n    }\n\
        }"
      kotlin: "class Solution {\n    fun maximizeSquareArea(m: Int, n: Int, hFences:\
        \ IntArray, vFences: IntArray): Int {\n        val MOD = 1_000_000_007L\n\n\
        \        val allHFences = (hFences.toMutableList().apply { add(1); add(m) }).sorted()\n\
        \        val allVFences = (vFences.toMutableList().apply { add(1); add(n) }).sorted()\n\
        \n        val hLengths = mutableSetOf<Int>()\n        for (i in allHFences.indices)\
        \ {\n            for (j in i + 1 until allHFences.size) {\n                hLengths.add(allHFences[j]\
        \ - allHFences[i])\n            }\n        }\n\n        val vLengths = mutableSetOf<Int>()\n\
        \        for (i in allVFences.indices) {\n            for (j in i + 1 until\
        \ allVFences.size) {\n                vLengths.add(allVFences[j] - allVFences[i])\n\
        \            }\n        }\n\n        var maxSide = 0\n        for (length in\
        \ hLengths) {\n            if (vLengths.contains(length)) {\n              \
        \  maxSide = maxOf(maxSide, length)\n            }\n        }\n\n        return\
        \ if (maxSide == 0) {\n            -1\n        } else {\n            ((maxSide.toLong()\
        \ * maxSide.toLong()) % MOD).toInt()\n        }\n    }\n}"
      dart: "class Solution {\n  int maximizeSquareArea(int m, int n, List<int> hFences,\
        \ List<int> vFences) {\n    final int MOD = 1000000007;\n\n    List<int> allHFences\
        \ = List.from(hFences)..add(1)..add(m);\n    allHFences.sort();\n\n    List<int>\
        \ allVFences = List.from(vFences)..add(1)..add(n);\n    allVFences.sort();\n\
        \n    Set<int> hLengths = <int>{};\n    for (int i = 0; i < allHFences.length;\
        \ i++) {\n      for (int j = i + 1; j < allHFences.length; j++) {\n        hLengths.add(allHFences[j]\
        \ - allHFences[i]);\n      }\n    }\n\n    Set<int> vLengths = <int>{};\n  \
        \  for (int i = 0; i < allVFences.length; i++) {\n      for (int j = i + 1;\
        \ j < allVFences.length; j++) {\n        vLengths.add(allVFences[j] - allVFences[i]);\n\
        \      }\n    }\n\n    int maxSide = 0;\n    for (int length in hLengths) {\n\
        \      if (vLengths.contains(length)) {\n        if (length > maxSide) {\n \
        \         maxSide = length;\n        }\n      }\n    }\n\n    if (maxSide ==\
        \ 0) {\n      return -1;\n    } else {\n      return (maxSide * maxSide) % MOD;\n\
        \    }\n  }\n}"
      go: "func maximizeSquareArea(m int, n int, hFences []int, vFences []int) int {\n\
        \    const MOD int64 = 1_000_000_007\n\n    allHFences := make([]int, len(hFences)+2)\n\
        \    copy(allHFences, hFences)\n    allHFences[len(hFences)] = 1\n    allHFences[len(hFences)+1]\
        \ = m\n    sort.Ints(allHFences)\n\n    allVFences := make([]int, len(vFences)+2)\n\
        \    copy(allVFences, vFences)\n    allVFences[len(vFences)] = 1\n    allVFences[len(vFences)+1]\
        \ = n\n    sort.Ints(allVFences)\n\n    hLengths := make(map[int]bool)\n   \
        \ for i := 0; i < len(allHFences); i++ {\n        for j := i + 1; j < len(allHFences);\
        \ j++ {\n            hLengths[allHFences[j]-allHFences[i]] = true\n        }\n\
        \    }\n\n    vLengths := make(map[int]bool)\n    for i := 0; i < len(allVFences);\
        \ i++ {\n        for j := i + 1; j < len(allVFences); j++ {\n            vLengths[allVFences[j]-allVFences[i]]\
        \ = true\n        }\n    }\n\n    maxSide := 0\n    for length := range hLengths\
        \ {\n        if vLengths[length] {\n            if length > maxSide {\n    \
        \            maxSide = length\n            }\n        }\n    }\n\n    if maxSide\
        \ == 0 {\n        return -1\n    } else {\n        return int(((int64(maxSide)\
        \ * int64(maxSide)) % MOD))\n    }\n}"
      ruby: "require 'set'\n\ndef maximize_square_area(m, n, h_fences, v_fences)\n \
        \   mod = 1_000_000_007\n\n    all_h_fences = h_fences + [1, m]\n    all_h_fences.sort!\n\
        \n    all_v_fences = v_fences + [1, n]\n    all_v_fences.sort!\n\n    h_lengths\
        \ = Set.new\n    (0...all_h_fences.length).each do |i|\n        (i + 1...all_h_fences.length).each\
        \ do |j|\n            h_lengths.add(all_h_fences[j] - all_h_fences[i])\n   \
        \     end\n    end\n\n    v_lengths = Set.new\n    (0...all_v_fences.length).each\
        \ do |i|\n        (i + 1...all_v_fences.length).each do |j|\n            v_lengths.add(all_v_fences[j]\
        \ - all_v_fences[i])\n        end\n    end\n\n    max_side = 0\n    h_lengths.each\
        \ do |length|\n        if v_lengths.include?(length)\n            max_side =\
        \ [max_side, length].max\n        end\n    end\n\n    if max_side == 0\n   \
        \     return -1\n    else\n        return (max_side * max_side) % mod\n    end\n\
        end"
      scala: "object Solution {\n    def maximizeSquareArea(m: Int, n: Int, hFences:\
        \ Array[Int], vFences: Array[Int]): Int = {\n        val MOD = 1_000_000_007L\n\
        \n        val allHFences = (hFences.toSeq :+ 1 :+ m).sorted\n        val allVFences\
        \ = (vFences.toSeq :+ 1 :+ n).sorted\n\n        val hLengths = collection.mutable.Set[Int]()\n\
        \        for (i <- allHFences.indices) {\n            for (j <- i + 1 until\
        \ allHFences.length) {\n                hLengths.add(allHFences(j) - allHFences(i))\n\
        \            }\n        }\n\n        val vLengths = collection.mutable.Set[Int]()\n\
        \        for (i <- allVFences.indices) {\n            for (j <- i + 1 until\
        \ allVFences.length) {\n                vLengths.add(allVFences(j) - allVFences(i))\n\
        \            }\n        }\n\n        var maxSide = 0\n        for (length <-\
        \ hLengths) {\n            if (vLengths.contains(length)) {\n              \
        \  maxSide = math.max(maxSide, length)\n            }\n        }\n\n       \
        \ if (maxSide == 0) {\n            -1\n        } else {\n            ((maxSide.toLong\
        \ * maxSide.toLong) % MOD).toInt\n        }\n    }\n}"
      rust: "use std::collections::HashSet;\n\nimpl Solution {\n    pub fn maximize_square_area(m:\
        \ i32, n: i32, h_fences: Vec<i32>, v_fences: Vec<i32>) -> i32 {\n        let\
        \ mod_val: i64 = 1_000_000_007;\n\n        let mut all_h_fences = h_fences;\n\
        \        all_h_fences.push(1);\n        all_h_fences.push(m);\n        all_h_fences.sort_unstable();\n\
        \n        let mut all_v_fences = v_fences;\n        all_v_fences.push(1);\n\
        \        all_v_fences.push(n);\n        all_v_fences.sort_unstable();\n\n  \
        \      let mut h_lengths: HashSet<i32> = HashSet::new();\n        for i in 0..all_h_fences.len()\
        \ {\n            for j in (i + 1)..all_h_fences.len() {\n                h_lengths.insert(all_h_fences[j]\
        \ - all_h_fences[i]);\n            }\n        }\n\n        let mut v_lengths:\
        \ HashSet<i32> = HashSet::new();\n        for i in 0..all_v_fences.len() {\n\
        \            for j in (i + 1)..all_v_fences.len() {\n                v_lengths.insert(all_v_fences[j]\
        \ - all_v_fences[i]);\n            }\n        }\n\n        let mut max_side\
        \ = 0;\n        for &length in h_lengths.iter() {\n            if v_lengths.contains(&length)\
        \ {\n                max_side = max_side.max(length);\n            }\n     \
        \   }\n\n        if max_side == 0 {\n            -1\n        } else {\n    \
        \        let area = (max_side as i64 * max_side as i64) % mod_val;\n       \
        \     area as i32\n        }\n    }\n}"
      racket: "(define/contract (maximize-square-area m n hFences vFences)\n  (-> exact-integer?\
        \ exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)\n\
        \  (let* ((MOD 1000000007)\n         (allHFences (sort (append hFences (list\
        \ 1 m)) <))\n         (allVFences (sort (append vFences (list 1 n)) <))\n  \
        \       (hLengths (for/fold ((s (set))) ((i (in-range (length allHFences))))\n\
        \                       (for/fold ((s-inner s)) ((j (in-range (+ i 1) (length\
        \ allHFences))))\n                         (set-add s-inner (- (list-ref allHFences\
        \ j) (list-ref allHFences i))))))\n         (vLengths (for/fold ((s (set)))\
        \ ((i (in-range (length allVFences))))\n                       (for/fold ((s-inner\
        \ s)) ((j (in-range (+ i 1) (length allVFences))))\n                       \
        \  (set-add s-inner (- (list-ref allVFences j) (list-ref allVFences i))))))\n\
        \         (maxSide (for/fold ((current-max 0)) ((len (in-set hLengths)))\n \
        \                     (if (set-member? vLengths len)\n                     \
        \     (max current-max len)\n                          current-max))))\n   \
        \ (if (= maxSide 0)\n        -1\n        (modulo (* maxSide maxSide) MOD))))"
      erlang: "-spec maximize_square_area(M :: integer(), N :: integer(), HFences ::\
        \ [integer()], VFences :: [integer()]) -> integer().\nmaximize_square_area(M,\
        \ N, HFences, VFences) ->\n  MOD = 1000000007,\n\n  AllHFences = lists:sort(HFences\
        \ ++ [1, M]),\n  AllVFences = lists:sort(VFences ++ [1, N]),\n\n  HLens = lists:foldl(fun(I,\
        \ Acc) ->\n    lists:foldl(fun(J, AccInner) ->\n      sets:add_element(J - I,\
        \ AccInner)\n    end, Acc, lists:nthtail(lists:keyfind(I, 1, lists:zip(AllHFences,\
        \ lists:seq(1, length(AllHFences)))), AllHFences))\n  end, sets:new(), AllHFences),\n\
        \n  VLens = lists:foldl(fun(I, Acc) ->\n    lists:foldl(fun(J, AccInner) ->\n\
        \      sets:add_element(J - I, AccInner)\n    end, Acc, lists:nthtail(lists:keyfind(I,\
        \ 1, lists:zip(AllVFences, lists:seq(1, length(AllVFences)))), AllVFences))\n\
        \  end, sets:new(), AllVFences),\n\n  MaxSide = sets:fold(fun(Len, Acc) ->\n\
        \    if sets:is_element(Len, VLens) ->\n      max(Acc, Len);\n    true ->\n\
        \      Acc\n    end\n  end, 0, HLens),\n\n  if MaxSide == 0 ->\n    -1;\n  true\
        \ ->\n    (MaxSide * MaxSide) rem MOD\n  end."
      elixir: "defmodule Solution do\n  @spec maximize_square_area(m :: integer, n ::\
        \ integer, h_fences :: [integer], v_fences :: [integer]) :: integer\n  def maximize_square_area(m,\
        \ n, h_fences, v_fences) do\n    mod = 1_000_000_007\n\n    all_h_fences = (h_fences\
        \ ++ [1, m]) |> Enum.sort()\n    all_v_fences = (v_fences ++ [1, n]) |> Enum.sort()\n\
        \n    h_lengths = Enum.reduce(0..(length(all_h_fences) - 1), MapSet.new(), fn\
        \ i, acc ->\n      Enum.reduce((i + 1)..(length(all_h_fences) - 1), acc, fn\
        \ j, acc_inner ->\n        MapSet.put(acc_inner, Enum.at(all_h_fences, j) -\
        \ Enum.at(all_h_fences, i))\n      end)\n    end)\n\n    v_lengths = Enum.reduce(0..(length(all_v_fences)\
        \ - 1), MapSet.new(), fn i, acc ->\n      Enum.reduce((i + 1)..(length(all_v_fences)\
        \ - 1), acc, fn j, acc_inner ->\n        MapSet.put(acc_inner, Enum.at(all_v_fences,\
        \ j) - Enum.at(all_v_fences, i))\n      end)\n    end)\n\n    max_side = Enum.reduce(h_lengths,\
        \ 0, fn length, acc ->\n      if MapSet.member?(v_lengths, length) do\n    \
        \    max(acc, length)\n      else\n        acc\n      end\n    end)\n\n    if\
        \ max_side == 0 do\n      -1\n    else\n      rem(max_side * max_side, mod)\n\
        \    end\n  end\nend"
    approach: 'The problem asks for the maximum area of a square field that can be formed
      by selecting two horizontal fences and two vertical fences. The field is bounded
      by unremovable fences at y=1, y=m, x=1, and x=n. Other fences specified in `hFences`
      and `vFences` can be removed. This implies that any pair of available horizontal
      lines (including 1 and m) can define the top and bottom boundaries of a potential
      square, and similarly, any pair of available vertical lines (including 1 and n)
      can define the left and right boundaries.


      The strategy involves first collecting all possible horizontal fence positions
      (1, m, and all `hFences` values) and all possible vertical fence positions (1,
      n, and all `vFences` values). These lists are then sorted. Next, we compute all
      possible side lengths that can be formed horizontally by taking the absolute difference
      between any two distinct horizontal fence positions. These lengths are stored
      in a hash set for efficient lookup. The same process is repeated for vertical
      fence positions to generate all possible vertical side lengths, also stored in
      a hash set. Finally, we find the largest common length present in both the horizontal
      and vertical side length sets. If such a common length `S` exists, the maximum
      square area is `S * S`. If no common length is found, it''s impossible to form
      a square, and we return -1. The final area is returned modulo 10^9 + 7.'
    time_complexity: Let H be the length of `hFences` and V be the length of `vFences`.
      The effective number of horizontal and vertical fences will be H+2 and V+2 respectively.
      Sorting these lists takes O(H log H) and O(V log V). Generating all possible side
      lengths involves iterating through all pairs, which takes O((H+2)^2) for horizontal
      lengths and O((V+2)^2) for vertical lengths. Storing these in hash sets takes
      O((H+2)^2) and O((V+2)^2) on average. Finding the maximum common length involves
      iterating through one set (at most O((H+2)^2) elements) and performing average
      O(1) lookups in the other set. Given H, V <= 600, the dominant factor is O(max(H,
      V)^2).
    space_complexity: The space complexity is dominated by storing the sets of possible
      horizontal and vertical side lengths. Each set can contain up to O((H+2)^2) and
      O((V+2)^2) distinct lengths respectively. Therefore, the space complexity is O(max(H,
      V)^2). Given H, V <= 600, this is roughly O(600^2) which is about 360,000 integers,
      well within memory limits.
    elapsed_time: 99.56660890579224
    model: gemini-2.5-flash
    generated_at: '2026-01-16 01:11:34 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int maximizeSquareArea(int m, int n, vector<int>&\
        \ hFences, vector<int>& vFences) {\n        hFences.push_back(1);\n        hFences.push_back(m);\n\
        \        vFences.push_back(1);\n        vFences.push_back(n);\n        sort(hFences.begin(),\
        \ hFences.end());\n        sort(vFences.begin(), vFences.end());\n        set<int>\
        \ hSet;\n        set<int> vSet;\n        for (int i = 0; i < hFences.size()\
        \ - 1; i++) {\n            hSet.insert(hFences[i + 1] - hFences[i]);\n     \
        \   }\n        for (int i = 0; i < vFences.size() - 1; i++) {\n            vSet.insert(vFences[i\
        \ + 1] - vFences[i]);\n        }\n        int maxArea = -1;\n        for (auto\
        \ it = hSet.begin(); it != hSet.end(); it++) {\n            if (vSet.find(*it)\
        \ != vSet.end()) {\n                maxArea = max(maxArea, (*it) * (*it));\n\
        \            }\n        }\n        return maxArea;\n    }\n};"
      java: "class Solution {\n    public int maximizeSquareArea(int m, int n, int[]\
        \ hFences, int[] vFences) {\n        Arrays.sort(hFences);\n        Arrays.sort(vFences);\n\
        \        int[] hFencesNew = new int[hFences.length + 2];\n        int[] vFencesNew\
        \ = new int[vFences.length + 2];\n        hFencesNew[0] = 1;\n        hFencesNew[hFencesNew.length\
        \ - 1] = m;\n        vFencesNew[0] = 1;\n        vFencesNew[vFencesNew.length\
        \ - 1] = n;\n        System.arraycopy(hFences, 0, hFencesNew, 1, hFences.length);\n\
        \        System.arraycopy(vFences, 0, vFencesNew, 1, vFences.length);\n    \
        \    Set<Integer> hSet = new HashSet<>();\n        Set<Integer> vSet = new HashSet<>();\n\
        \        for (int i = 0; i < hFencesNew.length - 1; i++) {\n            hSet.add(hFencesNew[i\
        \ + 1] - hFencesNew[i]);\n        }\n        for (int i = 0; i < vFencesNew.length\
        \ - 1; i++) {\n            vSet.add(vFencesNew[i + 1] - vFencesNew[i]);\n  \
        \      }\n        int maxArea = -1;\n        for (Integer it : hSet) {\n   \
        \         if (vSet.contains(it)) {\n                maxArea = Math.max(maxArea,\
        \ it * it);\n            }\n        }\n        return maxArea;\n    }\n}"
      python: "class Solution:\n    def maximizeSquareArea(self, m, n, hFences, vFences):\n\
        \        hFences = [1] + sorted(hFences) + [m]\n        vFences = [1] + sorted(vFences)\
        \ + [n]\n        hSet = set()\n        vSet = set()\n        for i in range(len(hFences)\
        \ - 1):\n            hSet.add(hFences[i + 1] - hFences[i])\n        for i in\
        \ range(len(vFences) - 1):\n            vSet.add(vFences[i + 1] - vFences[i])\n\
        \        maxArea = -1\n        for it in hSet:\n            if it in vSet:\n\
        \                maxArea = max(maxArea, it * it)\n        return maxArea"
      python3: "class Solution:\n    def maximizeSquareArea(self, m: int, n: int, hFences:\
        \ List[int], vFences: List[int]) -> int:\n        hFences = [1] + sorted(hFences)\
        \ + [m]\n        vFences = [1] + sorted(vFences) + [n]\n        hSet = set()\n\
        \        vSet = set()\n        for i in range(len(hFences) - 1):\n         \
        \   hSet.add(hFences[i + 1] - hFences[i])\n        for i in range(len(vFences)\
        \ - 1):\n            vSet.add(vFences[i + 1] - vFences[i])\n        maxArea\
        \ = -1\n        for it in hSet:\n            if it in vSet:\n              \
        \  maxArea = max(maxArea, it * it)\n        return maxArea"
      c: "int maximizeSquareArea(int m, int n, int* hFences, int hFencesSize, int* vFences,\
        \ int vFencesSize) {\n    int* hFencesNew = (int*)malloc((hFencesSize + 2) *\
        \ sizeof(int));\n    int* vFencesNew = (int*)malloc((vFencesSize + 2) * sizeof(int));\n\
        \    hFencesNew[0] = 1;\n    hFencesNew[hFencesSize + 1] = m;\n    vFencesNew[0]\
        \ = 1;\n    vFencesNew[vFencesSize + 1] = n;\n    for (int i = 0; i < hFencesSize;\
        \ i++) {\n        hFencesNew[i + 1] = hFences[i];\n    }\n    for (int i = 0;\
        \ i < vFencesSize; i++) {\n        vFencesNew[i + 1] = vFences[i];\n    }\n\
        \    // sort hFencesNew and vFencesNew\n    for (int i = 0; i < hFencesSize\
        \ + 2; i++) {\n        for (int j = i + 1; j < hFencesSize + 2; j++) {\n   \
        \         if (hFencesNew[i] > hFencesNew[j]) {\n                int temp = hFencesNew[i];\n\
        \                hFencesNew[i] = hFencesNew[j];\n                hFencesNew[j]\
        \ = temp;\n            }\n        }\n    }\n    for (int i = 0; i < vFencesSize\
        \ + 2; i++) {\n        for (int j = i + 1; j < vFencesSize + 2; j++) {\n   \
        \         if (vFencesNew[i] > vFencesNew[j]) {\n                int temp = vFencesNew[i];\n\
        \                vFencesNew[i] = vFencesNew[j];\n                vFencesNew[j]\
        \ = temp;\n            }\n        }\n    }\n    int maxArea = -1;\n    for (int\
        \ i = 0; i < hFencesSize + 2; i++) {\n        for (int j = i + 1; j < hFencesSize\
        \ + 2; j++) {\n            int diff = hFencesNew[j] - hFencesNew[i];\n     \
        \       for (int k = 0; k < vFencesSize + 2; k++) {\n                for (int\
        \ l = k + 1; l < vFencesSize + 2; l++) {\n                    if (vFencesNew[l]\
        \ - vFencesNew[k] == diff) {\n                        maxArea = max(maxArea,\
        \ diff * diff);\n                    }\n                }\n            }\n \
        \       }\n    }\n    free(hFencesNew);\n    free(vFencesNew);\n    return maxArea;\n\
        }"
      csharp: "public class Solution {\n    public int MaximizeSquareArea(int m, int\
        \ n, int[] hFences, int[] vFences) {\n        Array.Sort(hFences);\n       \
        \ Array.Sort(vFences);\n        int[] hFencesNew = new int[hFences.Length +\
        \ 2];\n        int[] vFencesNew = new int[vFences.Length + 2];\n        hFencesNew[0]\
        \ = 1;\n        hFencesNew[hFencesNew.Length - 1] = m;\n        vFencesNew[0]\
        \ = 1;\n        vFencesNew[vFencesNew.Length - 1] = n;\n        Array.Copy(hFences,\
        \ 0, hFencesNew, 1, hFences.Length);\n        Array.Copy(vFences, 0, vFencesNew,\
        \ 1, vFences.Length);\n        HashSet<int> hSet = new HashSet<int>();\n   \
        \     HashSet<int> vSet = new HashSet<int>();\n        for (int i = 0; i < hFencesNew.Length\
        \ - 1; i++) {\n            hSet.Add(hFencesNew[i + 1] - hFencesNew[i]);\n  \
        \      }\n        for (int i = 0; i < vFencesNew.Length - 1; i++) {\n      \
        \      vSet.Add(vFencesNew[i + 1] - vFencesNew[i]);\n        }\n        int\
        \ maxArea = -1;\n        foreach (int it in hSet) {\n            if (vSet.Contains(it))\
        \ {\n                maxArea = Math.Max(maxArea, it * it);\n            }\n\
        \        }\n        return maxArea;\n    }\n}"
      javascript: "var maximizeSquareArea = function(m, n, hFences, vFences) {\n   \
        \ hFences = [1].concat(hFences).concat([m]);\n    vFences = [1].concat(vFences).concat([n]);\n\
        \    hFences.sort((a, b) => a - b);\n    vFences.sort((a, b) => a - b);\n  \
        \  let hSet = new Set();\n    let vSet = new Set();\n    for (let i = 0; i <\
        \ hFences.length - 1; i++) {\n        hSet.add(hFences[i + 1] - hFences[i]);\n\
        \    }\n    for (let i = 0; i < vFences.length - 1; i++) {\n        vSet.add(vFences[i\
        \ + 1] - vFences[i]);\n    }\n    let maxArea = -1;\n    for (let it of hSet)\
        \ {\n        if (vSet.has(it)) {\n            maxArea = Math.max(maxArea, it\
        \ * it);\n        }\n    }\n    return maxArea;\n};"
      typescript: "function maximizeSquareArea(m: number, n: number, hFences: number[],\
        \ vFences: number[]): number {\n    hFences = [1].concat(hFences).concat([m]);\n\
        \    vFences = [1].concat(vFences).concat([n]);\n    hFences.sort((a, b) =>\
        \ a - b);\n    vFences.sort((a, b) => a - b);\n    let hSet: Set<number> = new\
        \ Set();\n    let vSet: Set<number> = new Set();\n    for (let i = 0; i < hFences.length\
        \ - 1; i++) {\n        hSet.add(hFences[i + 1] - hFences[i]);\n    }\n    for\
        \ (let i = 0; i < vFences.length - 1; i++) {\n        vSet.add(vFences[i + 1]\
        \ - vFences[i]);\n    }\n    let maxArea: number = -1;\n    for (let it of hSet)\
        \ {\n        if (vSet.has(it)) {\n            maxArea = Math.max(maxArea, it\
        \ * it);\n        }\n    }\n    return maxArea;\n}"
      php: "class Solution {\n    function maximizeSquareArea($m, $n, $hFences, $vFences)\
        \ {\n        $hFences = array_merge([1], $hFences, [$m]);\n        $vFences\
        \ = array_merge([1], $vFences, [$n]);\n        sort($hFences);\n        sort($vFences);\n\
        \        $hSet = [];\n        $vSet = [];\n        for ($i = 0; $i < count($hFences)\
        \ - 1; $i++) {\n            $hSet[] = $hFences[$i + 1] - $hFences[$i];\n   \
        \     }\n        for ($i = 0; $i < count($vFences) - 1; $i++) {\n          \
        \  $vSet[] = $vFences[$i + 1] - $vFences[$i];\n        }\n        $maxArea =\
        \ -1;\n        foreach ($hSet as $it) {\n            if (in_array($it, $vSet))\
        \ {\n                $maxArea = max($maxArea, $it * $it);\n            }\n \
        \       }\n        return $maxArea;\n    }\n}"
      swift: "class Solution {\n    func maximizeSquareArea(_ m: Int, _ n: Int, _ hFences:\
        \ [Int], _ vFences: [Int]) -> Int {\n        var hFences = [1] + hFences + [m]\n\
        \        var vFences = [1] + vFences + [n]\n        hFences.sort()\n       \
        \ vFences.sort()\n        var hSet: Set<Int> = []\n        var vSet: Set<Int>\
        \ = []\n        for i in 0..<hFences.count - 1 {\n            hSet.insert(hFences[i\
        \ + 1] - hFences[i])\n        }\n        for i in 0..<vFences.count - 1 {\n\
        \            vSet.insert(vFences[i + 1] - vFences[i])\n        }\n        var\
        \ maxArea = -1\n        for it in hSet {\n            if vSet.contains(it) {\n\
        \                maxArea = max(maxArea, it * it)\n            }\n        }\n\
        \        return maxArea\n    }\n}"
      kotlin: "class Solution {\n    fun maximizeSquareArea(m: Int, n: Int, hFences:\
        \ IntArray, vFences: IntArray): Int {\n        val h = (listOf(1) + hFences.toList()\
        \ + listOf(m)).sorted()\n        val v = (listOf(1) + vFences.toList() + listOf(n)).sorted()\n\
        \        val hDiffs = h.zipWithNext { a, b -> b - a }\n        val vDiffs =\
        \ v.zipWithNext { a, b -> b - a }\n        val commonDiffs = hDiffs.intersect(vDiffs.toSet())\n\
        \        return if (commonDiffs.isEmpty()) -1 else (commonDiffs.max() * commonDiffs.max())\
        \ % (1000000007)\n    }\n}"
      dart: "class Solution {\n  int maximizeSquareArea(int m, int n, List<int> hFences,\
        \ List<int> vFences) {\n    var h = [1, ...hFences, m]..sort();\n    var v =\
        \ [1, ...vFences, n]..sort();\n    var hDiffs = [];\n    for (var i = 0; i <\
        \ h.length - 1; i++) {\n      hDiffs.add(h[i + 1] - h[i]);\n    }\n    var vDiffs\
        \ = [];\n    for (var i = 0; i < v.length - 1; i++) {\n      vDiffs.add(v[i\
        \ + 1] - v[i]);\n    }\n    var commonDiffs = hDiffs.toSet().intersection(vDiffs.toSet()).toList();\n\
        \    return commonDiffs.isEmpty ? -1 : (commonDiffs.reduce((a, b) => a > b ?\
        \ a : b) * commonDiffs.reduce((a, b) => a > b ? a : b)) % 1000000007;\n  }\n\
        }"
      go: "func maximizeSquareArea(m int, n int, hFences []int, vFences []int) int {\n\
        \    h := append([]int{1}, append(hFences, m)...) \n    v := append([]int{1},\
        \ append(vFences, n)...) \n    sort.Ints(h)\n    sort.Ints(v)\n    hDiffs :=\
        \ []int{}\n    vDiffs := []int{}\n    for i := 1; i < len(h); i++ {\n      \
        \  hDiffs = append(hDiffs, h[i] - h[i - 1])\n    }\n    for i := 1; i < len(v);\
        \ i++ {\n        vDiffs = append(vDiffs, v[i] - v[i - 1])\n    }\n    commonDiffs\
        \ := []int{}\n    for _, hd := range hDiffs {\n        for _, vd := range vDiffs\
        \ {\n            if hd == vd {\n                commonDiffs = append(commonDiffs,\
        \ hd)\n            }\n        }\n    }\n    if len(commonDiffs) == 0 {\n   \
        \     return -1\n    }\n    maxDiff := 0\n    for _, diff := range commonDiffs\
        \ {\n        if diff > maxDiff {\n            maxDiff = diff\n        }\n  \
        \  }\n    return (maxDiff * maxDiff) % 1000000007\n}"
      ruby: "# @param {Integer} m\n# @param {Integer} n\n# @param {Integer[]} h_fences\n\
        # @param {Integer[]} v_fences\n# @return {Integer}\ndef maximize_square_area(m,\
        \ n, h_fences, v_fences)\n    h = [1] + h_fences + [m]\n    h.sort!\n    v =\
        \ [1] + v_fences + [n]\n    v.sort!\n    h_diffs = []\n    (0...h.length - 1).each\
        \ do |i|\n        h_diffs << h[i + 1] - h[i]\n    end\n    v_diffs = []\n  \
        \  (0...v.length - 1).each do |i|\n        v_diffs << v[i + 1] - v[i]\n    end\n\
        \    common_diffs = h_diffs & v_diffs\n    if common_diffs.empty?\n        return\
        \ -1\n    end\n    max_diff = common_diffs.max\n    return (max_diff * max_diff)\
        \ % 1000000007\nend"
      scala: "object Solution {\n    def maximizeSquareArea(m: Int, n: Int, hFences:\
        \ Array[Int], vFences: Array[Int]): Int = {\n        val h = (1 +: hFences :+\
        \ m).sorted\n        val v = (1 +: vFences :+ n).sorted\n        val hDiffs\
        \ = h.zip(h.tail).map { case (a, b) => b - a }\n        val vDiffs = v.zip(v.tail).map\
        \ { case (a, b) => b - a }\n        val commonDiffs = hDiffs.toSet.intersect(vDiffs.toSet)\n\
        \        if (commonDiffs.isEmpty) -1 else (commonDiffs.max * commonDiffs.max)\
        \ % 1000000007\n    }\n}"
      rust: "impl Solution {\n    pub fn maximize_square_area(m: i32, n: i32, h_fences:\
        \ Vec<i32>, v_fences: Vec<i32>) -> i32 {\n        let mut h: Vec<i32> = vec![1];\n\
        \        h.extend(h_fences);\n        h.push(m);\n        h.sort_unstable();\n\
        \        let mut v: Vec<i32> = vec![1];\n        v.extend(v_fences);\n     \
        \   v.push(n);\n        v.sort_unstable();\n        let mut h_diffs: Vec<i32>\
        \ = Vec::new();\n        for i in 1..h.len() {\n            h_diffs.push(h[i]\
        \ - h[i - 1]);\n        }\n        let mut v_diffs: Vec<i32> = Vec::new();\n\
        \        for i in 1..v.len() {\n            v_diffs.push(v[i] - v[i - 1]);\n\
        \        }\n        let mut common_diffs: Vec<i32> = Vec::new();\n        for\
        \ &hd in &h_diffs {\n            for &vd in &v_diffs {\n                if hd\
        \ == vd {\n                    common_diffs.push(hd);\n                }\n \
        \           }\n        }\n        if common_diffs.is_empty() {\n           \
        \ return -1;\n        }\n        let max_diff = *common_diffs.iter().max().unwrap();\n\
        \        (max_diff * max_diff) % 1000000007\n    }\n}"
      racket: "(define/contract (maximize-square-area m n hFences vFences)\n  (-> exact-integer?\
        \ exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)\n\
        \  (let* (\n         (h (sort (cons 1 (append hFences (list m)))))\n       \
        \  (v (sort (cons 1 (append vFences (list n)))))\n         (h-diffs (for/list\
        \ (\n                         (i (range 1 (length h))))\n                  \
        \  (- (list-ref h i) (list-ref h (- i 1)))))\n         (v-diffs (for/list (\n\
        \                        (i (range 1 (length v))))\n                    (- (list-ref\
        \ v i) (list-ref v (- i 1)))))\n         (common-diffs (set->list (set-intersect\
        \ (list->set h-diffs) (list->set v-diffs)))))\n    (if (null? common-diffs)\n\
        \        -1\n        (let (\n              (max-diff (apply max common-diffs)))\n\
        \          (modulo (* max-diff max-diff) 1000000007)))))"
      erlang: "-spec maximize_square_area(M :: integer(), N :: integer(), HFences ::\
        \ [integer()], VFences :: [integer()]) -> integer().\nmaximize_square_area(M,\
        \ N, HFences, VFences) ->\n    H = [1 | HFences] ++ [M],\n    V = [1 | VFences]\
        \ ++ [N],\n    lists:sort(H),\n    lists:sort(V),\n    HDiffs = [H2 - H1 ||\
        \ {H1, H2} <- lists:zip(lists:sublist(H, 1, length(H) - 1), lists:sublist(H,\
        \ 2, length(H) - 1))],\n    VDiffs = [V2 - V1 || {V1, V2} <- lists:zip(lists:sublist(V,\
        \ 1, length(V) - 1), lists:sublist(V, 2, length(V) - 1))],\n    CommonDiffs\
        \ = [X || X <- HDiffs, lists:member(X, VDiffs)],\n    case CommonDiffs of\n\
        \        [] -> -1;\n        _ -> (lists:max(CommonDiffs) * lists:max(CommonDiffs))\
        \ rem 1000000007\n    end."
      elixir: "defmodule Solution do\n  @spec maximize_square_area(m :: integer, n ::\
        \ integer, h_fences :: [integer], v_fences :: [integer]) :: integer\n  def maximize_square_area(m,\
        \ n, h_fences, v_fences) do\n    h = [1 | h_fences] ++ [m] |> Enum.sort()\n\
        \    v = [1 | v_fences] ++ [n] |> Enum.sort()\n    h_diffs = Enum.zip(Enum.slice(h,\
        \ 1..-1), Enum.slice(h, 0..-2)) |> Enum.map(fn {a, b} -> a - b end)\n    v_diffs\
        \ = Enum.zip(Enum.slice(v, 1..-1), Enum.slice(v, 0..-2)) |> Enum.map(fn {a,\
        \ b} -> a - b end)\n    common_diffs = Enum.filter(h_diffs, &Enum.member?(v_diffs,\
        \ &1))\n    if Enum.empty?(common_diffs) do\n      -1\n    else\n      max_diff\
        \ = Enum.max(common_diffs)\n      rem(max_diff * max_diff, 1000000007)\n   \
        \ end\n  end\nend"
    approach: The problem can be solved by first adding the boundaries to the lists
      of horizontal and vertical fences. Then, we can generate all possible differences
      between the fences in both lists. The maximum common difference between the two
      lists will be the side length of the largest square that can be formed. If no
      common difference is found, it means that it is impossible to form a square and
      we return -1. The key intuition here is that the differences between the fences
      represent the possible side lengths of the square, and we need to find the maximum
      common side length between the horizontal and vertical fences.
    time_complexity: The time complexity of this solution is O(m log m + n log n) where
      m and n are the number of horizontal and vertical fences respectively. This is
      because we are sorting the lists of fences and then generating all possible differences
      between them. The sorting operation takes O(m log m) and O(n log n) time, and
      the generation of differences takes O(m^2) and O(n^2) time. However, since m and
      n are at most 600, the time complexity is dominated by the sorting operation.
    space_complexity: The space complexity of this solution is O(m + n) where m and
      n are the number of horizontal and vertical fences respectively. This is because
      we are storing the lists of fences and their differences in memory. The space
      required to store the lists of fences is O(m + n), and the space required to store
      the differences is also O(m + n). Therefore, the overall space complexity is O(m
      + n).
    elapsed_time: 12.514438152313232
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-16 01:11:51 '
---

## Problem #2975: Maximum Square Area by Removing Fences From a Field

**Difficulty:** Medium

**Topics:** Array, Hash Table, Enumeration

## Problem Description

<p>There is a large <code>(m - 1) x (n - 1)</code> rectangular field with corners at <code>(1, 1)</code> and <code>(m, n)</code> containing some horizontal and vertical fences given in arrays <code>hFences</code> and <code>vFences</code> respectively.</p>

<p>Horizontal fences are from the coordinates <code>(hFences[i], 1)</code> to <code>(hFences[i], n)</code> and vertical fences are from the coordinates <code>(1, vFences[i])</code> to <code>(m, vFences[i])</code>.</p>

<p>Return <em>the <strong>maximum</strong> area of a <strong>square</strong> field that can be formed by <strong>removing</strong> some fences (<strong>possibly none</strong>) or </em><code>-1</code> <em>if it is impossible to make a square field</em>.</p>

<p>Since the answer may be large, return it <strong>modulo</strong> <code>10<sup>9 </sup>+ 7</code>.</p>

<p><strong>Note: </strong>The field is surrounded by two horizontal fences from the coordinates <code>(1, 1)</code> to <code>(1, n)</code> and <code>(m, 1)</code> to <code>(m, n)</code> and two vertical fences from the coordinates <code>(1, 1)</code> to <code>(m, 1)</code> and <code>(1, n)</code> to <code>(m, n)</code>. These fences <strong>cannot</strong> be removed.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/11/05/screenshot-from-2023-11-05-22-40-25.png" /></p>

<pre>
<strong>Input:</strong> m = 4, n = 3, hFences = [2,3], vFences = [2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Removing the horizontal fence at 2 and the vertical fence at 2 will give a square field of area 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/11/22/maxsquareareaexample1.png" style="width: 285px; height: 242px;" /></p>

<pre>
<strong>Input:</strong> m = 6, n = 7, hFences = [2], vFences = [4]
<strong>Output:</strong> -1
<strong>Explanation:</strong> It can be proved that there is no way to create a square field by removing fences.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= m, n &lt;= 10<sup>9</sup></code></li>
	<li><code><font face="monospace">1 &lt;= hF</font>ences<font face="monospace">.length, vFences.length &lt;= 600</font></code></li>
	<li><code><font face="monospace">1 &lt; hFences[i] &lt; m</font></code></li>
	<li><code><font face="monospace">1 &lt; vFences[i] &lt; n</font></code></li>
	<li><code><font face="monospace">hFences</font></code><font face="monospace"> and </font><code><font face="monospace">vFences</font></code><font face="monospace"> are unique.</font></li>
</ul>


## Hints

1. Put `1` and `m` into `hFences`. The differences of any two values in the new `hFences` can be a horizontal edge of a rectangle.

2. Similarly put `1` and `n` into `vFences`. The differences of any two values in the new `vFences` can be a vertical edge of a rectangle.

3. Our goal is to find the maximum common value in both parts.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2026-01-16 01:11:34 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks for the maximum area of a square field that can be formed by selecting two horizontal fences and two vertical fences. The field is bounded by unremovable fences at y=1, y=m, x=1, and x=n. Other fences specified in `hFences` and `vFences` can be removed. This implies that any pair of available horizontal lines (including 1 and m) can define the top and bottom boundaries of a potential square, and similarly, any pair of available vertical lines (including 1 and n) can define the left and right boundaries.

The strategy involves first collecting all possible horizontal fence positions (1, m, and all `hFences` values) and all possible vertical fence positions (1, n, and all `vFences` values). These lists are then sorted. Next, we compute all possible side lengths that can be formed horizontally by taking the absolute difference between any two distinct horizontal fence positions. These lengths are stored in a hash set for efficient lookup. The same process is repeated for vertical fence positions to generate all possible vertical side lengths, also stored in a hash set. Finally, we find the largest common length present in both the horizontal and vertical side length sets. If such a common length `S` exists, the maximum square area is `S * S`. If no common length is found, it's impossible to form a square, and we return -1. The final area is returned modulo 10^9 + 7.

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
    int maximizeSquareArea(int m, int n, vector<int>& hFences, vector<int>& vFences) {
        vector<int> allHFences = hFences;
        allHFences.push_back(1);
        allHFences.push_back(m);
        sort(allHFences.begin(), allHFences.end());
        allHFences.erase(unique(allHFences.begin(), allHFences.end()), allHFences.end());

        vector<int> allVFences = vFences;
        allVFences.push_back(1);
        allVFences.push_back(n);
        sort(allVFences.begin(), allVFences.end());
        allVFences.erase(unique(allVFences.begin(), allVFences.end()), allVFences.end());

        unordered_set<long long> hDiffs;
        for (int i = 0; i < allHFences.size(); ++i) {
            for (int j = i + 1; j < allHFences.size(); ++j) {
                hDiffs.insert(allHFences[j] - allHFences[i]);
            }
        }

        long long maxSide = 0;
        for (int i = 0; i < allVFences.size(); ++i) {
            for (int j = i + 1; j < allVFences.size(); ++j) {
                long long diff = allVFences[j] - allVFences[i];
                if (hDiffs.count(diff)) {
                    maxSide = max(maxSide, diff);
                }
            }
        }

        if (maxSide == 0) {
            return -1;
        }

        long long MOD = 1e9 + 7;
        return (int)((maxSide * maxSide) % MOD);
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int maximizeSquareArea(int m, int n, int[] hFences, int[] vFences) {
        ArrayList<Integer> allHFencesList = new ArrayList<>();
        for (int fence : hFences) {
            allHFencesList.add(fence);
        }
        allHFencesList.add(1);
        allHFencesList.add(m);
        Collections.sort(allHFencesList);

        // Remove duplicates (Java's ArrayList doesn't have unique, so use a Set then convert back)
        Set<Integer> uniqueHFences = new HashSet<>(allHFencesList);
        allHFencesList.clear();
        allHFencesList.addAll(uniqueHFences);
        Collections.sort(allHFencesList);

        ArrayList<Integer> allVFencesList = new ArrayList<>();
        for (int fence : vFences) {
            allVFencesList.add(fence);
        }
        allVFencesList.add(1);
        allVFencesList.add(n);
        Collections.sort(allVFencesList);

        Set<Integer> uniqueVFences = new HashSet<>(allVFencesList);
        allVFencesList.clear();
        allVFencesList.addAll(uniqueVFences);
        Collections.sort(allVFencesList);

        Set<Long> hDiffs = new HashSet<>();
        for (int i = 0; i < allHFencesList.size(); ++i) {
            for (int j = i + 1; j < allHFencesList.size(); ++j) {
                hDiffs.add((long)allHFencesList.get(j) - allHFencesList.get(i));
            }
        }

        long maxSide = 0;
        for (int i = 0; i < allVFencesList.size(); ++i) {
            for (int j = i + 1; j < allVFencesList.size(); ++j) {
                long diff = (long)allVFencesList.get(j) - allVFencesList.get(i);
                if (hDiffs.contains(diff)) {
                    maxSide = Math.max(maxSide, diff);
                }
            }
        }

        if (maxSide == 0) {
            return -1;
        }

        long MOD = 1_000_000_007L;
        return (int)((maxSide * maxSide) % MOD);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        """
        :type m: int
        :type n: int
        :type hFences: List[int]
        :type vFences: List[int]
        :rtype: int
        """
        all_h_fences = sorted(list(set(hFences + [1, m])))
        all_v_fences = sorted(list(set(vFences + [1, n])))

        h_diffs = set()
        for i in range(len(all_h_fences)):
            for j in range(i + 1, len(all_h_fences)):
                h_diffs.add(all_h_fences[j] - all_h_fences[i])

        max_side = 0
        for i in range(len(all_v_fences)):
            for j in range(i + 1, len(all_v_fences)):
                diff = all_v_fences[j] - all_v_fences[i]
                if diff in h_diffs:
                    max_side = max(max_side, diff)

        if max_side == 0:
            return -1

        MOD = 10**9 + 7
        return (max_side * max_side) % MOD
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        all_h_fences = sorted(list(set(hFences + [1, m])))
        all_v_fences = sorted(list(set(vFences + [1, n])))

        h_diffs = set()
        for i in range(len(all_h_fences)):
            for j in range(i + 1, len(all_h_fences)):
                h_diffs.add(all_h_fences[j] - all_h_fences[i])

        max_side = 0
        for i in range(len(all_v_fences)):
            for j in range(i + 1, len(all_v_fences)):
                diff = all_v_fences[j] - all_v_fences[i]
                if diff in h_diffs:
                    max_side = max(max_side, diff)

        if max_side == 0:
            return -1

        MOD = 10**9 + 7
        return (max_side * max_side) % MOD
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

// Custom comparison function for qsort
int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

// Function to remove duplicates from a sorted array and return new size
int removeDuplicates(int* arr, int size) {
    if (size == 0) return 0;
    int j = 0;
    for (int i = 1; i < size; i++) {
        if (arr[i] != arr[j]) {
            j++;
            arr[j] = arr[i];
        }
    }
    return j + 1;
}

// Function to check if an element exists in a sorted array (binary search)
bool contains(int* arr, int size, int val) {
    int low = 0, high = size - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == val) {
            return true;
        } else if (arr[mid] < val) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return false;
}

int maximizeSquareArea(int m, int n, int* hFences, int hFencesSize, int* vFences, int vFencesSize) {
    // Max possible fences: 600 + 2 = 602
    int* allHFences = (int*)malloc(sizeof(int) * (hFencesSize + 2));
    for (int i = 0; i < hFencesSize; i++) {
        allHFences[i] = hFences[i];
    }
    allHFences[hFencesSize] = 1;
    allHFences[hFencesSize + 1] = m;
    int currentHFencesSize = hFencesSize + 2;
    qsort(allHFences, currentHFencesSize, sizeof(int), compare);
    currentHFencesSize = removeDuplicates(allHFences, currentHFencesSize);

    int* allVFences = (int*)malloc(sizeof(int) * (vFencesSize + 2));
    for (int i = 0; i < vFencesSize; i++) {
        allVFences[i] = vFences[i];
    }
    allVFences[vFencesSize] = 1;
    allVFences[vFencesSize + 1] = n;
    int currentVFencesSize = vFencesSize + 2;
    qsort(allVFences, currentVFencesSize, sizeof(int), compare);
    currentVFencesSize = removeDuplicates(allVFences, currentVFencesSize);

    // Max possible differences: (602 * 601) / 2 = 180901
    int* hDiffs = (int*)malloc(sizeof(int) * (currentHFencesSize * (currentHFencesSize - 1) / 2));
    int hDiffsCount = 0;
    for (int i = 0; i < currentHFencesSize; i++) {
        for (int j = i + 1; j < currentHFencesSize; j++) {
            hDiffs[hDiffsCount++] = allHFences[j] - allHFences[i];
        }
    }
    qsort(hDiffs, hDiffsCount, sizeof(int), compare);
    hDiffsCount = removeDuplicates(hDiffs, hDiffsCount);

    long long maxSide = 0;
    for (int i = 0; i < currentVFencesSize; i++) {
        for (int j = i + 1; j < currentVFencesSize; j++) {
            int diff = allVFences[j] - allVFences[i];
            if (contains(hDiffs, hDiffsCount, diff)) {
                if (diff > maxSide) {
                    maxSide = diff;
                }
            }
        }
    }

    free(allHFences);
    free(allVFences);
    free(hDiffs);

    if (maxSide == 0) {
        return -1;
    }

    long long MOD = 1000000007LL;
    return (int)((maxSide * maxSide) % MOD);
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
    public int MaximizeSquareArea(int m, int n, int[] hFences, int[] vFences) {
        List<int> allHFencesList = new List<int>(hFences);
        allHFencesList.Add(1);
        allHFencesList.Add(m);
        allHFencesList = allHFencesList.Distinct().OrderBy(x => x).ToList();

        List<int> allVFencesList = new List<int>(vFences);
        allVFencesList.Add(1);
        allVFencesList.Add(n);
        allVFencesList = allVFencesList.Distinct().OrderBy(x => x).ToList();

        HashSet<long> hDiffs = new HashSet<long>();
        for (int i = 0; i < allHFencesList.Count; i++) {
            for (int j = i + 1; j < allHFencesList.Count; j++) {
                hDiffs.Add((long)allHFencesList[j] - allHFencesList[i]);
            }
        }

        long maxSide = 0;
        for (int i = 0; i < allVFencesList.Count; i++) {
            for (int j = i + 1; j < allVFencesList.Count; j++) {
                long diff = (long)allVFencesList[j] - allVFencesList[i];
                if (hDiffs.Contains(diff)) {
                    maxSide = Math.Max(maxSide, diff);
                }
            }
        }

        if (maxSide == 0) {
            return -1;
        }

        long MOD = 1_000_000_007L;
        return (int)((maxSide * maxSide) % MOD);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} m
 * @param {number} n
 * @param {number[]} hFences
 * @param {number[]} vFences
 * @return {number}
 */
var maximizeSquareArea = function(m, n, hFences, vFences) {
    let allHFences = [...new Set([...hFences, 1, m])].sort((a, b) => a - b);
    let allVFences = [...new Set([...vFences, 1, n])].sort((a, b) => a - b);

    let hDiffs = new Set();
    for (let i = 0; i < allHFences.length; i++) {
        for (let j = i + 1; j < allHFences.length; j++) {
            hDiffs.add(allHFences[j] - allHFences[i]);
        }
    }

    let maxSide = 0;
    for (let i = 0; i < allVFences.length; i++) {
        for (let j = i + 1; j < allVFences.length; j++) {
            let diff = allVFences[j] - allVFences[i];
            if (hDiffs.has(diff)) {
                maxSide = Math.max(maxSide, diff);
            }
        }
    }

    if (maxSide === 0) {
        return -1;
    }

    const MOD = 10**9 + 7;
    return (Number(maxSide) * Number(maxSide)) % MOD;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maximizeSquareArea(m: number, n: number, hFences: number[], vFences: number[]): number {
    let allHFences = [...new Set([...hFences, 1, m])].sort((a, b) => a - b);
    let allVFences = [...new Set([...vFences, 1, n])].sort((a, b) => a - b);

    let hDiffs: Set<number> = new Set();
    for (let i = 0; i < allHFences.length; i++) {
        for (let j = i + 1; j < allHFences.length; j++) {
            hDiffs.add(allHFences[j] - allHFences[i]);
        }
    }

    let maxSide: number = 0;
    for (let i = 0; i < allVFences.length; i++) {
        for (let j = i + 1; j < allVFences.length; j++) {
            let diff = allVFences[j] - allVFences[i];
            if (hDiffs.has(diff)) {
                maxSide = Math.max(maxSide, diff);
            }
        }
    }

    if (maxSide === 0) {
        return -1;
    }

    const MOD = 10**9 + 7;
    // Use BigInt for multiplication to prevent overflow before modulo, then convert back to number
    return Number((BigInt(maxSide) * BigInt(maxSide)) % BigInt(MOD));
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
     * @param Integer $m
     * @param Integer $n
     * @param Integer[] $hFences
     * @param Integer[] $vFences
     * @return Integer
     */
    function maximizeSquareArea($m, $n, $hFences, $vFences) {
        $allHFences = array_unique(array_merge($hFences, [1, $m]));
        sort($allHFences);

        $allVFences = array_unique(array_merge($vFences, [1, $n]));
        sort($allVFences);

        $hDiffs = [];
        for ($i = 0; $i < count($allHFences); $i++) {
            for ($j = $i + 1; $j < count($allHFences); $j++) {
                $hDiffs[$allHFences[$j] - $allHFences[$i]] = true; // Use as a hash set
            }
        }

        $maxSide = 0;
        for ($i = 0; $i < count($allVFences); $i++) {
            for ($j = $i + 1; $j < count($allVFences); $j++) {
                $diff = $allVFences[$j] - $allVFences[$i];
                if (isset($hDiffs[$diff])) {
                    $maxSide = max($maxSide, $diff);
                }
            }
        }

        if ($maxSide == 0) {
            return -1;
        }

        $MOD = 10**9 + 7;
        // PHP integers handle large values automatically up to system limits, but explicit casting to int is needed for return type.
        // For modulo, ensure calculation is done with large numbers if necessary.
        return (int)(($maxSide * $maxSide) % $MOD);
    }
}
?>
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maximizeSquareArea(_ m: Int, _ n: Int, _ hFences: [Int], _ vFences: [Int]) -> Int {
        var allHFences = Set(hFences + [1, m]).sorted()
        var allVFences = Set(vFences + [1, n]).sorted()

        var hDiffs = Set<Int>()
        for i in 0..<allHFences.count {
            for j in (i + 1)..<allHFences.count {
                hDiffs.insert(allHFences[j] - allHFences[i])
            }
        }

        var maxSide: Int = 0
        for i in 0..<allVFences.count {
            for j in (i + 1)..<allVFences.count {
                let diff = allVFences[j] - allVFences[i]
                if hDiffs.contains(diff) {
                    maxSide = max(maxSide, diff)
                }
            }
        }

        if maxSide == 0 {
            return -1
        }

        let MOD = 1_000_000_007
        // Use Int64 for multiplication to prevent overflow before modulo
        return Int((Int64(maxSide) * Int64(maxSide)) % Int64(MOD))
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maximizeSquareArea(m: Int, n: Int, hFences: IntArray, vFences: IntArray): Int {
        val MOD = 1_000_000_007L

        val allHFences = (hFences.toMutableList().apply { add(1); add(m) }).sorted()
        val allVFences = (vFences.toMutableList().apply { add(1); add(n) }).sorted()

        val hLengths = mutableSetOf<Int>()
        for (i in allHFences.indices) {
            for (j in i + 1 until allHFences.size) {
                hLengths.add(allHFences[j] - allHFences[i])
            }
        }

        val vLengths = mutableSetOf<Int>()
        for (i in allVFences.indices) {
            for (j in i + 1 until allVFences.size) {
                vLengths.add(allVFences[j] - allVFences[i])
            }
        }

        var maxSide = 0
        for (length in hLengths) {
            if (vLengths.contains(length)) {
                maxSide = maxOf(maxSide, length)
            }
        }

        return if (maxSide == 0) {
            -1
        } else {
            ((maxSide.toLong() * maxSide.toLong()) % MOD).toInt()
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maximizeSquareArea(int m, int n, List<int> hFences, List<int> vFences) {
    final int MOD = 1000000007;

    List<int> allHFences = List.from(hFences)..add(1)..add(m);
    allHFences.sort();

    List<int> allVFences = List.from(vFences)..add(1)..add(n);
    allVFences.sort();

    Set<int> hLengths = <int>{};
    for (int i = 0; i < allHFences.length; i++) {
      for (int j = i + 1; j < allHFences.length; j++) {
        hLengths.add(allHFences[j] - allHFences[i]);
      }
    }

    Set<int> vLengths = <int>{};
    for (int i = 0; i < allVFences.length; i++) {
      for (int j = i + 1; j < allVFences.length; j++) {
        vLengths.add(allVFences[j] - allVFences[i]);
      }
    }

    int maxSide = 0;
    for (int length in hLengths) {
      if (vLengths.contains(length)) {
        if (length > maxSide) {
          maxSide = length;
        }
      }
    }

    if (maxSide == 0) {
      return -1;
    } else {
      return (maxSide * maxSide) % MOD;
    }
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maximizeSquareArea(m int, n int, hFences []int, vFences []int) int {
    const MOD int64 = 1_000_000_007

    allHFences := make([]int, len(hFences)+2)
    copy(allHFences, hFences)
    allHFences[len(hFences)] = 1
    allHFences[len(hFences)+1] = m
    sort.Ints(allHFences)

    allVFences := make([]int, len(vFences)+2)
    copy(allVFences, vFences)
    allVFences[len(vFences)] = 1
    allVFences[len(vFences)+1] = n
    sort.Ints(allVFences)

    hLengths := make(map[int]bool)
    for i := 0; i < len(allHFences); i++ {
        for j := i + 1; j < len(allHFences); j++ {
            hLengths[allHFences[j]-allHFences[i]] = true
        }
    }

    vLengths := make(map[int]bool)
    for i := 0; i < len(allVFences); i++ {
        for j := i + 1; j < len(allVFences); j++ {
            vLengths[allVFences[j]-allVFences[i]] = true
        }
    }

    maxSide := 0
    for length := range hLengths {
        if vLengths[length] {
            if length > maxSide {
                maxSide = length
            }
        }
    }

    if maxSide == 0 {
        return -1
    } else {
        return int(((int64(maxSide) * int64(maxSide)) % MOD))
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
require 'set'

def maximize_square_area(m, n, h_fences, v_fences)
    mod = 1_000_000_007

    all_h_fences = h_fences + [1, m]
    all_h_fences.sort!

    all_v_fences = v_fences + [1, n]
    all_v_fences.sort!

    h_lengths = Set.new
    (0...all_h_fences.length).each do |i|
        (i + 1...all_h_fences.length).each do |j|
            h_lengths.add(all_h_fences[j] - all_h_fences[i])
        end
    end

    v_lengths = Set.new
    (0...all_v_fences.length).each do |i|
        (i + 1...all_v_fences.length).each do |j|
            v_lengths.add(all_v_fences[j] - all_v_fences[i])
        end
    end

    max_side = 0
    h_lengths.each do |length|
        if v_lengths.include?(length)
            max_side = [max_side, length].max
        end
    end

    if max_side == 0
        return -1
    else
        return (max_side * max_side) % mod
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maximizeSquareArea(m: Int, n: Int, hFences: Array[Int], vFences: Array[Int]): Int = {
        val MOD = 1_000_000_007L

        val allHFences = (hFences.toSeq :+ 1 :+ m).sorted
        val allVFences = (vFences.toSeq :+ 1 :+ n).sorted

        val hLengths = collection.mutable.Set[Int]()
        for (i <- allHFences.indices) {
            for (j <- i + 1 until allHFences.length) {
                hLengths.add(allHFences(j) - allHFences(i))
            }
        }

        val vLengths = collection.mutable.Set[Int]()
        for (i <- allVFences.indices) {
            for (j <- i + 1 until allVFences.length) {
                vLengths.add(allVFences(j) - allVFences(i))
            }
        }

        var maxSide = 0
        for (length <- hLengths) {
            if (vLengths.contains(length)) {
                maxSide = math.max(maxSide, length)
            }
        }

        if (maxSide == 0) {
            -1
        } else {
            ((maxSide.toLong * maxSide.toLong) % MOD).toInt
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::HashSet;

impl Solution {
    pub fn maximize_square_area(m: i32, n: i32, h_fences: Vec<i32>, v_fences: Vec<i32>) -> i32 {
        let mod_val: i64 = 1_000_000_007;

        let mut all_h_fences = h_fences;
        all_h_fences.push(1);
        all_h_fences.push(m);
        all_h_fences.sort_unstable();

        let mut all_v_fences = v_fences;
        all_v_fences.push(1);
        all_v_fences.push(n);
        all_v_fences.sort_unstable();

        let mut h_lengths: HashSet<i32> = HashSet::new();
        for i in 0..all_h_fences.len() {
            for j in (i + 1)..all_h_fences.len() {
                h_lengths.insert(all_h_fences[j] - all_h_fences[i]);
            }
        }

        let mut v_lengths: HashSet<i32> = HashSet::new();
        for i in 0..all_v_fences.len() {
            for j in (i + 1)..all_v_fences.len() {
                v_lengths.insert(all_v_fences[j] - all_v_fences[i]);
            }
        }

        let mut max_side = 0;
        for &length in h_lengths.iter() {
            if v_lengths.contains(&length) {
                max_side = max_side.max(length);
            }
        }

        if max_side == 0 {
            -1
        } else {
            let area = (max_side as i64 * max_side as i64) % mod_val;
            area as i32
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (maximize-square-area m n hFences vFences)
  (-> exact-integer? exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* ((MOD 1000000007)
         (allHFences (sort (append hFences (list 1 m)) <))
         (allVFences (sort (append vFences (list 1 n)) <))
         (hLengths (for/fold ((s (set))) ((i (in-range (length allHFences))))
                       (for/fold ((s-inner s)) ((j (in-range (+ i 1) (length allHFences))))
                         (set-add s-inner (- (list-ref allHFences j) (list-ref allHFences i))))))
         (vLengths (for/fold ((s (set))) ((i (in-range (length allVFences))))
                       (for/fold ((s-inner s)) ((j (in-range (+ i 1) (length allVFences))))
                         (set-add s-inner (- (list-ref allVFences j) (list-ref allVFences i))))))
         (maxSide (for/fold ((current-max 0)) ((len (in-set hLengths)))
                      (if (set-member? vLengths len)
                          (max current-max len)
                          current-max))))
    (if (= maxSide 0)
        -1
        (modulo (* maxSide maxSide) MOD))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec maximize_square_area(M :: integer(), N :: integer(), HFences :: [integer()], VFences :: [integer()]) -> integer().
maximize_square_area(M, N, HFences, VFences) ->
  MOD = 1000000007,

  AllHFences = lists:sort(HFences ++ [1, M]),
  AllVFences = lists:sort(VFences ++ [1, N]),

  HLens = lists:foldl(fun(I, Acc) ->
    lists:foldl(fun(J, AccInner) ->
      sets:add_element(J - I, AccInner)
    end, Acc, lists:nthtail(lists:keyfind(I, 1, lists:zip(AllHFences, lists:seq(1, length(AllHFences)))), AllHFences))
  end, sets:new(), AllHFences),

  VLens = lists:foldl(fun(I, Acc) ->
    lists:foldl(fun(J, AccInner) ->
      sets:add_element(J - I, AccInner)
    end, Acc, lists:nthtail(lists:keyfind(I, 1, lists:zip(AllVFences, lists:seq(1, length(AllVFences)))), AllVFences))
  end, sets:new(), AllVFences),

  MaxSide = sets:fold(fun(Len, Acc) ->
    if sets:is_element(Len, VLens) ->
      max(Acc, Len);
    true ->
      Acc
    end
  end, 0, HLens),

  if MaxSide == 0 ->
    -1;
  true ->
    (MaxSide * MaxSide) rem MOD
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec maximize_square_area(m :: integer, n :: integer, h_fences :: [integer], v_fences :: [integer]) :: integer
  def maximize_square_area(m, n, h_fences, v_fences) do
    mod = 1_000_000_007

    all_h_fences = (h_fences ++ [1, m]) |> Enum.sort()
    all_v_fences = (v_fences ++ [1, n]) |> Enum.sort()

    h_lengths = Enum.reduce(0..(length(all_h_fences) - 1), MapSet.new(), fn i, acc ->
      Enum.reduce((i + 1)..(length(all_h_fences) - 1), acc, fn j, acc_inner ->
        MapSet.put(acc_inner, Enum.at(all_h_fences, j) - Enum.at(all_h_fences, i))
      end)
    end)

    v_lengths = Enum.reduce(0..(length(all_v_fences) - 1), MapSet.new(), fn i, acc ->
      Enum.reduce((i + 1)..(length(all_v_fences) - 1), acc, fn j, acc_inner ->
        MapSet.put(acc_inner, Enum.at(all_v_fences, j) - Enum.at(all_v_fences, i))
      end)
    end)

    max_side = Enum.reduce(h_lengths, 0, fn length, acc ->
      if MapSet.member?(v_lengths, length) do
        max(acc, length)
      else
        acc
      end
    end)

    if max_side == 0 do
      -1
    else
      rem(max_side * max_side, mod)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** Let H be the length of `hFences` and V be the length of `vFences`. The effective number of horizontal and vertical fences will be H+2 and V+2 respectively. Sorting these lists takes O(H log H) and O(V log V). Generating all possible side lengths involves iterating through all pairs, which takes O((H+2)^2) for horizontal lengths and O((V+2)^2) for vertical lengths. Storing these in hash sets takes O((H+2)^2) and O((V+2)^2) on average. Finding the maximum common length involves iterating through one set (at most O((H+2)^2) elements) and performing average O(1) lookups in the other set. Given H, V <= 600, the dominant factor is O(max(H, V)^2).

- **Space Complexity:** The space complexity is dominated by storing the sets of possible horizontal and vertical side lengths. Each set can contain up to O((H+2)^2) and O((V+2)^2) distinct lengths respectively. Therefore, the space complexity is O(max(H, V)^2). Given H, V <= 600, this is roughly O(600^2) which is about 360,000 integers, well within memory limits.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-16 01:11:51 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by first adding the boundaries to the lists of horizontal and vertical fences. Then, we can generate all possible differences between the fences in both lists. The maximum common difference between the two lists will be the side length of the largest square that can be formed. If no common difference is found, it means that it is impossible to form a square and we return -1. The key intuition here is that the differences between the fences represent the possible side lengths of the square, and we need to find the maximum common side length between the horizontal and vertical fences.

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
    int maximizeSquareArea(int m, int n, vector<int>& hFences, vector<int>& vFences) {
        hFences.push_back(1);
        hFences.push_back(m);
        vFences.push_back(1);
        vFences.push_back(n);
        sort(hFences.begin(), hFences.end());
        sort(vFences.begin(), vFences.end());
        set<int> hSet;
        set<int> vSet;
        for (int i = 0; i < hFences.size() - 1; i++) {
            hSet.insert(hFences[i + 1] - hFences[i]);
        }
        for (int i = 0; i < vFences.size() - 1; i++) {
            vSet.insert(vFences[i + 1] - vFences[i]);
        }
        int maxArea = -1;
        for (auto it = hSet.begin(); it != hSet.end(); it++) {
            if (vSet.find(*it) != vSet.end()) {
                maxArea = max(maxArea, (*it) * (*it));
            }
        }
        return maxArea;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maximizeSquareArea(int m, int n, int[] hFences, int[] vFences) {
        Arrays.sort(hFences);
        Arrays.sort(vFences);
        int[] hFencesNew = new int[hFences.length + 2];
        int[] vFencesNew = new int[vFences.length + 2];
        hFencesNew[0] = 1;
        hFencesNew[hFencesNew.length - 1] = m;
        vFencesNew[0] = 1;
        vFencesNew[vFencesNew.length - 1] = n;
        System.arraycopy(hFences, 0, hFencesNew, 1, hFences.length);
        System.arraycopy(vFences, 0, vFencesNew, 1, vFences.length);
        Set<Integer> hSet = new HashSet<>();
        Set<Integer> vSet = new HashSet<>();
        for (int i = 0; i < hFencesNew.length - 1; i++) {
            hSet.add(hFencesNew[i + 1] - hFencesNew[i]);
        }
        for (int i = 0; i < vFencesNew.length - 1; i++) {
            vSet.add(vFencesNew[i + 1] - vFencesNew[i]);
        }
        int maxArea = -1;
        for (Integer it : hSet) {
            if (vSet.contains(it)) {
                maxArea = Math.max(maxArea, it * it);
            }
        }
        return maxArea;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def maximizeSquareArea(self, m, n, hFences, vFences):
        hFences = [1] + sorted(hFences) + [m]
        vFences = [1] + sorted(vFences) + [n]
        hSet = set()
        vSet = set()
        for i in range(len(hFences) - 1):
            hSet.add(hFences[i + 1] - hFences[i])
        for i in range(len(vFences) - 1):
            vSet.add(vFences[i + 1] - vFences[i])
        maxArea = -1
        for it in hSet:
            if it in vSet:
                maxArea = max(maxArea, it * it)
        return maxArea
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences = [1] + sorted(hFences) + [m]
        vFences = [1] + sorted(vFences) + [n]
        hSet = set()
        vSet = set()
        for i in range(len(hFences) - 1):
            hSet.add(hFences[i + 1] - hFences[i])
        for i in range(len(vFences) - 1):
            vSet.add(vFences[i + 1] - vFences[i])
        maxArea = -1
        for it in hSet:
            if it in vSet:
                maxArea = max(maxArea, it * it)
        return maxArea
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int maximizeSquareArea(int m, int n, int* hFences, int hFencesSize, int* vFences, int vFencesSize) {
    int* hFencesNew = (int*)malloc((hFencesSize + 2) * sizeof(int));
    int* vFencesNew = (int*)malloc((vFencesSize + 2) * sizeof(int));
    hFencesNew[0] = 1;
    hFencesNew[hFencesSize + 1] = m;
    vFencesNew[0] = 1;
    vFencesNew[vFencesSize + 1] = n;
    for (int i = 0; i < hFencesSize; i++) {
        hFencesNew[i + 1] = hFences[i];
    }
    for (int i = 0; i < vFencesSize; i++) {
        vFencesNew[i + 1] = vFences[i];
    }
    // sort hFencesNew and vFencesNew
    for (int i = 0; i < hFencesSize + 2; i++) {
        for (int j = i + 1; j < hFencesSize + 2; j++) {
            if (hFencesNew[i] > hFencesNew[j]) {
                int temp = hFencesNew[i];
                hFencesNew[i] = hFencesNew[j];
                hFencesNew[j] = temp;
            }
        }
    }
    for (int i = 0; i < vFencesSize + 2; i++) {
        for (int j = i + 1; j < vFencesSize + 2; j++) {
            if (vFencesNew[i] > vFencesNew[j]) {
                int temp = vFencesNew[i];
                vFencesNew[i] = vFencesNew[j];
                vFencesNew[j] = temp;
            }
        }
    }
    int maxArea = -1;
    for (int i = 0; i < hFencesSize + 2; i++) {
        for (int j = i + 1; j < hFencesSize + 2; j++) {
            int diff = hFencesNew[j] - hFencesNew[i];
            for (int k = 0; k < vFencesSize + 2; k++) {
                for (int l = k + 1; l < vFencesSize + 2; l++) {
                    if (vFencesNew[l] - vFencesNew[k] == diff) {
                        maxArea = max(maxArea, diff * diff);
                    }
                }
            }
        }
    }
    free(hFencesNew);
    free(vFencesNew);
    return maxArea;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaximizeSquareArea(int m, int n, int[] hFences, int[] vFences) {
        Array.Sort(hFences);
        Array.Sort(vFences);
        int[] hFencesNew = new int[hFences.Length + 2];
        int[] vFencesNew = new int[vFences.Length + 2];
        hFencesNew[0] = 1;
        hFencesNew[hFencesNew.Length - 1] = m;
        vFencesNew[0] = 1;
        vFencesNew[vFencesNew.Length - 1] = n;
        Array.Copy(hFences, 0, hFencesNew, 1, hFences.Length);
        Array.Copy(vFences, 0, vFencesNew, 1, vFences.Length);
        HashSet<int> hSet = new HashSet<int>();
        HashSet<int> vSet = new HashSet<int>();
        for (int i = 0; i < hFencesNew.Length - 1; i++) {
            hSet.Add(hFencesNew[i + 1] - hFencesNew[i]);
        }
        for (int i = 0; i < vFencesNew.Length - 1; i++) {
            vSet.Add(vFencesNew[i + 1] - vFencesNew[i]);
        }
        int maxArea = -1;
        foreach (int it in hSet) {
            if (vSet.Contains(it)) {
                maxArea = Math.Max(maxArea, it * it);
            }
        }
        return maxArea;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var maximizeSquareArea = function(m, n, hFences, vFences) {
    hFences = [1].concat(hFences).concat([m]);
    vFences = [1].concat(vFences).concat([n]);
    hFences.sort((a, b) => a - b);
    vFences.sort((a, b) => a - b);
    let hSet = new Set();
    let vSet = new Set();
    for (let i = 0; i < hFences.length - 1; i++) {
        hSet.add(hFences[i + 1] - hFences[i]);
    }
    for (let i = 0; i < vFences.length - 1; i++) {
        vSet.add(vFences[i + 1] - vFences[i]);
    }
    let maxArea = -1;
    for (let it of hSet) {
        if (vSet.has(it)) {
            maxArea = Math.max(maxArea, it * it);
        }
    }
    return maxArea;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maximizeSquareArea(m: number, n: number, hFences: number[], vFences: number[]): number {
    hFences = [1].concat(hFences).concat([m]);
    vFences = [1].concat(vFences).concat([n]);
    hFences.sort((a, b) => a - b);
    vFences.sort((a, b) => a - b);
    let hSet: Set<number> = new Set();
    let vSet: Set<number> = new Set();
    for (let i = 0; i < hFences.length - 1; i++) {
        hSet.add(hFences[i + 1] - hFences[i]);
    }
    for (let i = 0; i < vFences.length - 1; i++) {
        vSet.add(vFences[i + 1] - vFences[i]);
    }
    let maxArea: number = -1;
    for (let it of hSet) {
        if (vSet.has(it)) {
            maxArea = Math.max(maxArea, it * it);
        }
    }
    return maxArea;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function maximizeSquareArea($m, $n, $hFences, $vFences) {
        $hFences = array_merge([1], $hFences, [$m]);
        $vFences = array_merge([1], $vFences, [$n]);
        sort($hFences);
        sort($vFences);
        $hSet = [];
        $vSet = [];
        for ($i = 0; $i < count($hFences) - 1; $i++) {
            $hSet[] = $hFences[$i + 1] - $hFences[$i];
        }
        for ($i = 0; $i < count($vFences) - 1; $i++) {
            $vSet[] = $vFences[$i + 1] - $vFences[$i];
        }
        $maxArea = -1;
        foreach ($hSet as $it) {
            if (in_array($it, $vSet)) {
                $maxArea = max($maxArea, $it * $it);
            }
        }
        return $maxArea;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maximizeSquareArea(_ m: Int, _ n: Int, _ hFences: [Int], _ vFences: [Int]) -> Int {
        var hFences = [1] + hFences + [m]
        var vFences = [1] + vFences + [n]
        hFences.sort()
        vFences.sort()
        var hSet: Set<Int> = []
        var vSet: Set<Int> = []
        for i in 0..<hFences.count - 1 {
            hSet.insert(hFences[i + 1] - hFences[i])
        }
        for i in 0..<vFences.count - 1 {
            vSet.insert(vFences[i + 1] - vFences[i])
        }
        var maxArea = -1
        for it in hSet {
            if vSet.contains(it) {
                maxArea = max(maxArea, it * it)
            }
        }
        return maxArea
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maximizeSquareArea(m: Int, n: Int, hFences: IntArray, vFences: IntArray): Int {
        val h = (listOf(1) + hFences.toList() + listOf(m)).sorted()
        val v = (listOf(1) + vFences.toList() + listOf(n)).sorted()
        val hDiffs = h.zipWithNext { a, b -> b - a }
        val vDiffs = v.zipWithNext { a, b -> b - a }
        val commonDiffs = hDiffs.intersect(vDiffs.toSet())
        return if (commonDiffs.isEmpty()) -1 else (commonDiffs.max() * commonDiffs.max()) % (1000000007)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maximizeSquareArea(int m, int n, List<int> hFences, List<int> vFences) {
    var h = [1, ...hFences, m]..sort();
    var v = [1, ...vFences, n]..sort();
    var hDiffs = [];
    for (var i = 0; i < h.length - 1; i++) {
      hDiffs.add(h[i + 1] - h[i]);
    }
    var vDiffs = [];
    for (var i = 0; i < v.length - 1; i++) {
      vDiffs.add(v[i + 1] - v[i]);
    }
    var commonDiffs = hDiffs.toSet().intersection(vDiffs.toSet()).toList();
    return commonDiffs.isEmpty ? -1 : (commonDiffs.reduce((a, b) => a > b ? a : b) * commonDiffs.reduce((a, b) => a > b ? a : b)) % 1000000007;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maximizeSquareArea(m int, n int, hFences []int, vFences []int) int {
    h := append([]int{1}, append(hFences, m)...) 
    v := append([]int{1}, append(vFences, n)...) 
    sort.Ints(h)
    sort.Ints(v)
    hDiffs := []int{}
    vDiffs := []int{}
    for i := 1; i < len(h); i++ {
        hDiffs = append(hDiffs, h[i] - h[i - 1])
    }
    for i := 1; i < len(v); i++ {
        vDiffs = append(vDiffs, v[i] - v[i - 1])
    }
    commonDiffs := []int{}
    for _, hd := range hDiffs {
        for _, vd := range vDiffs {
            if hd == vd {
                commonDiffs = append(commonDiffs, hd)
            }
        }
    }
    if len(commonDiffs) == 0 {
        return -1
    }
    maxDiff := 0
    for _, diff := range commonDiffs {
        if diff > maxDiff {
            maxDiff = diff
        }
    }
    return (maxDiff * maxDiff) % 1000000007
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} m
# @param {Integer} n
# @param {Integer[]} h_fences
# @param {Integer[]} v_fences
# @return {Integer}
def maximize_square_area(m, n, h_fences, v_fences)
    h = [1] + h_fences + [m]
    h.sort!
    v = [1] + v_fences + [n]
    v.sort!
    h_diffs = []
    (0...h.length - 1).each do |i|
        h_diffs << h[i + 1] - h[i]
    end
    v_diffs = []
    (0...v.length - 1).each do |i|
        v_diffs << v[i + 1] - v[i]
    end
    common_diffs = h_diffs & v_diffs
    if common_diffs.empty?
        return -1
    end
    max_diff = common_diffs.max
    return (max_diff * max_diff) % 1000000007
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maximizeSquareArea(m: Int, n: Int, hFences: Array[Int], vFences: Array[Int]): Int = {
        val h = (1 +: hFences :+ m).sorted
        val v = (1 +: vFences :+ n).sorted
        val hDiffs = h.zip(h.tail).map { case (a, b) => b - a }
        val vDiffs = v.zip(v.tail).map { case (a, b) => b - a }
        val commonDiffs = hDiffs.toSet.intersect(vDiffs.toSet)
        if (commonDiffs.isEmpty) -1 else (commonDiffs.max * commonDiffs.max) % 1000000007
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn maximize_square_area(m: i32, n: i32, h_fences: Vec<i32>, v_fences: Vec<i32>) -> i32 {
        let mut h: Vec<i32> = vec![1];
        h.extend(h_fences);
        h.push(m);
        h.sort_unstable();
        let mut v: Vec<i32> = vec![1];
        v.extend(v_fences);
        v.push(n);
        v.sort_unstable();
        let mut h_diffs: Vec<i32> = Vec::new();
        for i in 1..h.len() {
            h_diffs.push(h[i] - h[i - 1]);
        }
        let mut v_diffs: Vec<i32> = Vec::new();
        for i in 1..v.len() {
            v_diffs.push(v[i] - v[i - 1]);
        }
        let mut common_diffs: Vec<i32> = Vec::new();
        for &hd in &h_diffs {
            for &vd in &v_diffs {
                if hd == vd {
                    common_diffs.push(hd);
                }
            }
        }
        if common_diffs.is_empty() {
            return -1;
        }
        let max_diff = *common_diffs.iter().max().unwrap();
        (max_diff * max_diff) % 1000000007
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (maximize-square-area m n hFences vFences)
  (-> exact-integer? exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* (
         (h (sort (cons 1 (append hFences (list m)))))
         (v (sort (cons 1 (append vFences (list n)))))
         (h-diffs (for/list (
                         (i (range 1 (length h))))
                    (- (list-ref h i) (list-ref h (- i 1)))))
         (v-diffs (for/list (
                        (i (range 1 (length v))))
                    (- (list-ref v i) (list-ref v (- i 1)))))
         (common-diffs (set->list (set-intersect (list->set h-diffs) (list->set v-diffs)))))
    (if (null? common-diffs)
        -1
        (let (
              (max-diff (apply max common-diffs)))
          (modulo (* max-diff max-diff) 1000000007)))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec maximize_square_area(M :: integer(), N :: integer(), HFences :: [integer()], VFences :: [integer()]) -> integer().
maximize_square_area(M, N, HFences, VFences) ->
    H = [1 | HFences] ++ [M],
    V = [1 | VFences] ++ [N],
    lists:sort(H),
    lists:sort(V),
    HDiffs = [H2 - H1 || {H1, H2} <- lists:zip(lists:sublist(H, 1, length(H) - 1), lists:sublist(H, 2, length(H) - 1))],
    VDiffs = [V2 - V1 || {V1, V2} <- lists:zip(lists:sublist(V, 1, length(V) - 1), lists:sublist(V, 2, length(V) - 1))],
    CommonDiffs = [X || X <- HDiffs, lists:member(X, VDiffs)],
    case CommonDiffs of
        [] -> -1;
        _ -> (lists:max(CommonDiffs) * lists:max(CommonDiffs)) rem 1000000007
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec maximize_square_area(m :: integer, n :: integer, h_fences :: [integer], v_fences :: [integer]) :: integer
  def maximize_square_area(m, n, h_fences, v_fences) do
    h = [1 | h_fences] ++ [m] |> Enum.sort()
    v = [1 | v_fences] ++ [n] |> Enum.sort()
    h_diffs = Enum.zip(Enum.slice(h, 1..-1), Enum.slice(h, 0..-2)) |> Enum.map(fn {a, b} -> a - b end)
    v_diffs = Enum.zip(Enum.slice(v, 1..-1), Enum.slice(v, 0..-2)) |> Enum.map(fn {a, b} -> a - b end)
    common_diffs = Enum.filter(h_diffs, &Enum.member?(v_diffs, &1))
    if Enum.empty?(common_diffs) do
      -1
    else
      max_diff = Enum.max(common_diffs)
      rem(max_diff * max_diff, 1000000007)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this solution is O(m log m + n log n) where m and n are the number of horizontal and vertical fences respectively. This is because we are sorting the lists of fences and then generating all possible differences between them. The sorting operation takes O(m log m) and O(n log n) time, and the generation of differences takes O(m^2) and O(n^2) time. However, since m and n are at most 600, the time complexity is dominated by the sorting operation.

- **Space Complexity:** The space complexity of this solution is O(m + n) where m and n are the number of horizontal and vertical fences respectively. This is because we are storing the lists of fences and their differences in memory. The space required to store the lists of fences is O(m + n), and the space required to store the differences is also O(m + n). Therefore, the overall space complexity is O(m + n).

</div>
</details>
