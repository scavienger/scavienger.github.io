---
layout: post
title: "Number of Ways to Divide a Long Corridor"
date: 2025-12-14 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Math", "String", "Dynamic Programming"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int numberOfWays(std::string corridor) {\n\
        \        long long MOD = 1e9 + 7;\n\n        std::vector<int> seat_indices;\n\
        \        for (int i = 0; i < corridor.length(); ++i) {\n            if (corridor[i]\
        \ == 'S') {\n                seat_indices.push_back(i);\n            }\n   \
        \     }\n\n        int num_seats = seat_indices.size();\n\n        if (num_seats\
        \ == 0 || num_seats % 2 != 0) {\n            return 0;\n        }\n\n      \
        \  long long result = 1;\n        // We need to place dividers between (S_1,\
        \ S_2), (S_3, S_4), etc.\n        // These correspond to seat_indices[2k+1]\
        \ and seat_indices[2k+2]\n        // for k = 0, 1, ..., num_seats/2 - 2\n\n\
        \        for (int k = 0; k < num_seats / 2 - 1; ++k) {\n            // The divider\
        \ is placed between seat_indices[2k+1] and seat_indices[2k+2]\n            //\
        \ Number of ways to place this divider is the difference of their indices.\n\
        \            long long ways_for_this_divider = seat_indices[2 * k + 2] - seat_indices[2\
        \ * k + 1];\n            result = (result * ways_for_this_divider) % MOD;\n\
        \        }\n\n        return static_cast<int>(result);\n    }\n};"
      java: "import java.util.ArrayList;\nimport java.util.List;\n\nclass Solution {\n\
        \    public int numberOfWays(String corridor) {\n        long MOD = 1_000_000_007;\n\
        \n        List<Integer> seatIndices = new ArrayList<>();\n        for (int i\
        \ = 0; i < corridor.length(); ++i) {\n            if (corridor.charAt(i) ==\
        \ 'S') {\n                seatIndices.add(i);\n            }\n        }\n\n\
        \        int numSeats = seatIndices.size();\n\n        if (numSeats == 0 ||\
        \ numSeats % 2 != 0) {\n            return 0;\n        }\n\n        long result\
        \ = 1;\n        // We need to place dividers between (S_1, S_2), (S_3, S_4),\
        \ etc.\n        // These correspond to seatIndices[2k+1] and seatIndices[2k+2]\n\
        \        // for k = 0, 1, ..., numSeats/2 - 2\n\n        for (int k = 0; k <\
        \ numSeats / 2 - 1; ++k) {\n            // The divider is placed between seatIndices[2k+1]\
        \ and seatIndices[2k+2]\n            // Number of ways to place this divider\
        \ is the difference of their indices.\n            long waysForThisDivider =\
        \ seatIndices.get(2 * k + 2) - seatIndices.get(2 * k + 1);\n            result\
        \ = (result * waysForThisDivider) % MOD;\n        }\n\n        return (int)\
        \ result;\n    }\n}"
      python: "class Solution:\n    def numberOfWays(self, corridor: str) -> int:\n\
        \        MOD = 10**9 + 7\n\n        seat_indices = []\n        for i, char in\
        \ enumerate(corridor):\n            if char == 'S':\n                seat_indices.append(i)\n\
        \n        num_seats = len(seat_indices)\n\n        if num_seats == 0 or num_seats\
        \ % 2 != 0:\n            return 0\n\n        result = 1\n        # We need to\
        \ place dividers between (S_1, S_2), (S_3, S_4), etc.\n        # These correspond\
        \ to seat_indices[2k+1] and seat_indices[2k+2]\n        # for k = 0, 1, ...,\
        \ num_seats/2 - 2\n\n        for k in range(num_seats // 2 - 1):\n         \
        \   # The divider is placed between seat_indices[2k+1] and seat_indices[2k+2]\n\
        \            # Number of ways to place this divider is the difference of their\
        \ indices.\n            ways_for_this_divider = seat_indices[2 * k + 2] - seat_indices[2\
        \ * k + 1]\n            result = (result * ways_for_this_divider) % MOD\n\n\
        \        return result"
      python3: "class Solution:\n    def numberOfWays(self, corridor: str) -> int:\n\
        \        MOD = 10**9 + 7\n\n        seat_indices = []\n        for i, char in\
        \ enumerate(corridor):\n            if char == 'S':\n                seat_indices.append(i)\n\
        \n        num_seats = len(seat_indices)\n\n        if num_seats == 0 or num_seats\
        \ % 2 != 0:\n            return 0\n\n        result = 1\n        # We need to\
        \ place dividers between (S_1, S_2), (S_3, S_4), etc.\n        # These correspond\
        \ to seat_indices[2k+1] and seat_indices[2k+2]\n        # for k = 0, 1, ...,\
        \ num_seats/2 - 2\n\n        for k in range(num_seats // 2 - 1):\n         \
        \   # The divider is placed between seat_indices[2k+1] and seat_indices[2k+2]\n\
        \            # Number of ways to place this divider is the difference of their\
        \ indices.\n            ways_for_this_divider = seat_indices[2 * k + 2] - seat_indices[2\
        \ * k + 1]\n            result = (result * ways_for_this_divider) % MOD\n\n\
        \        return result"
      c: "#include <stdlib.h>\n#include <string.h>\n\n// Function to dynamically grow\
        \ an array (vector equivalent)\ntypedef struct {\n    int* data;\n    int size;\n\
        \    int capacity;\n} IntVector;\n\nvoid initIntVector(IntVector* vec, int initialCapacity)\
        \ {\n    vec->data = (int*)malloc(sizeof(int) * initialCapacity);\n    vec->size\
        \ = 0;\n    vec->capacity = initialCapacity;\n}\n\nvoid pushBackIntVector(IntVector*\
        \ vec, int value) {\n    if (vec->size == vec->capacity) {\n        vec->capacity\
        \ *= 2;\n        vec->data = (int*)realloc(vec->data, sizeof(int) * vec->capacity);\n\
        \    }\n    vec->data[vec->size++] = value;\n}\n\nvoid freeIntVector(IntVector*\
        \ vec) {\n    free(vec->data);\n    vec->data = NULL;\n    vec->size = 0;\n\
        \    vec->capacity = 0;\n}\n\nint numberOfWays(char* corridor) {\n    long long\
        \ MOD = 1e9 + 7;\n\n    IntVector seat_indices;\n    initIntVector(&seat_indices,\
        \ 10); // Initial capacity\n\n    int n = strlen(corridor);\n    for (int i\
        \ = 0; i < n; ++i) {\n        if (corridor[i] == 'S') {\n            pushBackIntVector(&seat_indices,\
        \ i);\n        }\n    }\n\n    int num_seats = seat_indices.size;\n\n    if\
        \ (num_seats == 0 || num_seats % 2 != 0) {\n        freeIntVector(&seat_indices);\n\
        \        return 0;\n    }\n\n    long long result = 1;\n    // We need to place\
        \ dividers between (S_1, S_2), (S_3, S_4), etc.\n    // These correspond to\
        \ seat_indices[2k+1] and seat_indices[2k+2]\n    // for k = 0, 1, ..., num_seats/2\
        \ - 2\n\n    for (int k = 0; k < num_seats / 2 - 1; ++k) {\n        // The divider\
        \ is placed between seat_indices[2k+1] and seat_indices[2k+2]\n        // Number\
        \ of ways to place this divider is the difference of their indices.\n      \
        \  long long ways_for_this_divider = seat_indices.data[2 * k + 2] - seat_indices.data[2\
        \ * k + 1];\n        result = (result * ways_for_this_divider) % MOD;\n    }\n\
        \n    freeIntVector(&seat_indices);\n    return (int)result;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int NumberOfWays(string corridor) {\n        long MOD = 1_000_000_007;\n\
        \n        List<int> seatIndices = new List<int>();\n        for (int i = 0;\
        \ i < corridor.Length; ++i) {\n            if (corridor[i] == 'S') {\n     \
        \           seatIndices.Add(i);\n            }\n        }\n\n        int numSeats\
        \ = seatIndices.Count;\n\n        if (numSeats == 0 || numSeats % 2 != 0) {\n\
        \            return 0;\n        }\n\n        long result = 1;\n        // We\
        \ need to place dividers between (S_1, S_2), (S_3, S_4), etc.\n        // These\
        \ correspond to seatIndices[2k+1] and seatIndices[2k+2]\n        // for k =\
        \ 0, 1, ..., numSeats/2 - 2\n\n        for (int k = 0; k < numSeats / 2 - 1;\
        \ ++k) {\n            // The divider is placed between seatIndices[2k+1] and\
        \ seatIndices[2k+2]\n            // Number of ways to place this divider is\
        \ the difference of their indices.\n            long waysForThisDivider = seatIndices[2\
        \ * k + 2] - seatIndices[2 * k + 1];\n            result = (result * waysForThisDivider)\
        \ % MOD;\n        }\n\n        return (int) result;\n    }\n}"
      javascript: "/**\n * @param {string} corridor\n * @return {number}\n */\nvar numberOfWays\
        \ = function(corridor) {\n    const MOD = 1_000_000_007;\n\n    const seatIndices\
        \ = [];\n    for (let i = 0; i < corridor.length; ++i) {\n        if (corridor[i]\
        \ === 'S') {\n            seatIndices.push(i);\n        }\n    }\n\n    const\
        \ numSeats = seatIndices.length;\n\n    if (numSeats === 0 || numSeats % 2 !==\
        \ 0) {\n        return 0;\n    }\n\n    let result = 1;\n    // We need to place\
        \ dividers between (S_1, S_2), (S_3, S_4), etc.\n    // These correspond to\
        \ seatIndices[2k+1] and seatIndices[2k+2]\n    // for k = 0, 1, ..., numSeats/2\
        \ - 2\n\n    for (let k = 0; k < numSeats / 2 - 1; ++k) {\n        // The divider\
        \ is placed between seatIndices[2k+1] and seatIndices[2k+2]\n        // Number\
        \ of ways to place this divider is the difference of their indices.\n      \
        \  const waysForThisDivider = seatIndices[2 * k + 2] - seatIndices[2 * k + 1];\n\
        \        result = (result * waysForThisDivider) % MOD;\n    }\n\n    return\
        \ result;\n};"
      typescript: "function numberOfWays(corridor: string): number {\n    const MOD\
        \ = 1_000_000_007;\n\n    const seatIndices: number[] = [];\n    for (let i\
        \ = 0; i < corridor.length; ++i) {\n        if (corridor[i] === 'S') {\n   \
        \         seatIndices.push(i);\n        }\n    }\n\n    const numSeats = seatIndices.length;\n\
        \n    if (numSeats === 0 || numSeats % 2 !== 0) {\n        return 0;\n    }\n\
        \n    let result = 1;\n    // We need to place dividers between (S_1, S_2),\
        \ (S_3, S_4), etc.\n    // These correspond to seatIndices[2k+1] and seatIndices[2k+2]\n\
        \    // for k = 0, 1, ..., numSeats/2 - 2\n\n    for (let k = 0; k < numSeats\
        \ / 2 - 1; ++k) {\n        // The divider is placed between seatIndices[2k+1]\
        \ and seatIndices[2k+2]\n        // Number of ways to place this divider is\
        \ the difference of their indices.\n        const waysForThisDivider = seatIndices[2\
        \ * k + 2] - seatIndices[2 * k + 1];\n        result = (result * waysForThisDivider)\
        \ % MOD;\n    }\n\n    return result;\n}"
      php: "<?php\n\nclass Solution {\n\n    /**\n     * @param String $corridor\n \
        \    * @return Integer\n     */\n    function numberOfWays($corridor) {\n  \
        \      $MOD = 1_000_000_007;\n\n        $seatIndices = [];\n        for ($i\
        \ = 0; $i < strlen($corridor); ++$i) {\n            if ($corridor[$i] === 'S')\
        \ {\n                $seatIndices[] = $i;\n            }\n        }\n\n    \
        \    $numSeats = count($seatIndices);\n\n        if ($numSeats === 0 || $numSeats\
        \ % 2 !== 0) {\n            return 0;\n        }\n\n        $result = 1;\n \
        \       // We need to place dividers between (S_1, S_2), (S_3, S_4), etc.\n\
        \        // These correspond to seatIndices[2k+1] and seatIndices[2k+2]\n  \
        \      // for k = 0, 1, ..., numSeats/2 - 2\n\n        for ($k = 0; $k < $numSeats\
        \ / 2 - 1; ++$k) {\n            // The divider is placed between seatIndices[2k+1]\
        \ and seatIndices[2k+2]\n            // Number of ways to place this divider\
        \ is the difference of their indices.\n            $waysForThisDivider = $seatIndices[2\
        \ * $k + 2] - $seatIndices[2 * $k + 1];\n            $result = ($result * $waysForThisDivider)\
        \ % $MOD;\n        }\n\n        return $result;\n    }\n}"
      swift: "class Solution {\n    func numberOfWays(_ corridor: String) -> Int {\n\
        \        let MOD = 1_000_000_007\n\n        var seatIndices: [Int] = []\n  \
        \      for (i, char) in corridor.enumerated() {\n            if char == \"S\"\
        \ {\n                seatIndices.append(i)\n            }\n        }\n\n   \
        \     let numSeats = seatIndices.count\n\n        if numSeats == 0 || numSeats\
        \ % 2 != 0 {\n            return 0\n        }\n\n        var result: Int = 1\n\
        \        // We need to place dividers between (S_1, S_2), (S_3, S_4), etc.\n\
        \        // These correspond to seatIndices[2k+1] and seatIndices[2k+2]\n  \
        \      // for k = 0, 1, ..., numSeats/2 - 2\n\n        for k in 0..<(numSeats\
        \ / 2 - 1) {\n            // The divider is placed between seatIndices[2k+1]\
        \ and seatIndices[2k+2]\n            // Number of ways to place this divider\
        \ is the difference of their indices.\n            let waysForThisDivider =\
        \ seatIndices[2 * k + 2] - seatIndices[2 * k + 1]\n            result = (result\
        \ * waysForThisDivider) % MOD\n        }\n\n        return result\n    }\n}"
      kotlin: "class Solution {\n    fun numberOfWays(corridor: String): Int {\n   \
        \     val MOD = 1_000_000_007L\n\n        val seatIndices = mutableListOf<Int>()\n\
        \        for (i in corridor.indices) {\n            if (corridor[i] == 'S')\
        \ {\n                seatIndices.add(i)\n            }\n        }\n\n      \
        \  val numSeats = seatIndices.size\n\n        if (numSeats == 0 || numSeats\
        \ % 2 != 0) {\n            return 0\n        }\n\n        var result: Long =\
        \ 1\n        // We need to place dividers between (S_1, S_2), (S_3, S_4), etc.\n\
        \        // These correspond to seatIndices[2k+1] and seatIndices[2k+2]\n  \
        \      // for k = 0, 1, ..., numSeats/2 - 2\n\n        for (k in 0 until (numSeats\
        \ / 2 - 1)) {\n            // The divider is placed between seatIndices[2k+1]\
        \ and seatIndices[2k+2]\n            // Number of ways to place this divider\
        \ is the difference of their indices.\n            val waysForThisDivider =\
        \ (seatIndices[2 * k + 2] - seatIndices[2 * k + 1]).toLong()\n            result\
        \ = (result * waysForThisDivider) % MOD\n        }\n\n        return result.toInt()\n\
        \    }\n}"
      dart: "class Solution {\n  int numberOfWays(String corridor) {\n    final int\
        \ MOD = 1000000007;\n\n    List<int> seatIndices = [];\n    for (int i = 0;\
        \ i < corridor.length; ++i) {\n      if (corridor[i] == 'S') {\n        seatIndices.add(i);\n\
        \      }\n    }\n\n    int numSeats = seatIndices.length;\n\n    if (numSeats\
        \ == 0 || numSeats % 2 != 0) {\n      return 0;\n    }\n\n    int result = 1;\n\
        \    // We need to place dividers between (S_1, S_2), (S_3, S_4), etc.\n   \
        \ // These correspond to seatIndices[2k+1] and seatIndices[2k+2]\n    // for\
        \ k = 0, 1, ..., numSeats/2 - 2\n\n    for (int k = 0; k < numSeats ~/ 2 - 1;\
        \ ++k) {\n      // The divider is placed between seatIndices[2k+1] and seatIndices[2k+2]\n\
        \      // Number of ways to place this divider is the difference of their indices.\n\
        \      int waysForThisDivider = seatIndices[2 * k + 2] - seatIndices[2 * k +\
        \ 1];\n      result = (result * waysForThisDivider) % MOD;\n    }\n\n    return\
        \ result;\n  }\n}"
      go: "package main\n\nimport \"strings\"\n\nfunc numberOfWays(corridor string)\
        \ int {\n    const MOD int = 1e9 + 7\n\n    var seatIndices []int\n    for i,\
        \ char := range corridor {\n        if char == 'S' {\n            seatIndices\
        \ = append(seatIndices, i)\n        }\n    }\n\n    numSeats := len(seatIndices)\n\
        \n    if numSeats == 0 || numSeats % 2 != 0 {\n        return 0\n    }\n\n \
        \   result := 1\n    // We need to place dividers between (S_1, S_2), (S_3,\
        \ S_4), etc.\n    // These correspond to seatIndices[2k+1] and seatIndices[2k+2]\n\
        \    // for k = 0, 1, ..., numSeats/2 - 2\n\n    for k := 0; k < numSeats /\
        \ 2 - 1; k++ {\n        // The divider is placed between seatIndices[2k+1] and\
        \ seatIndices[2k+2]\n        // Number of ways to place this divider is the\
        \ difference of their indices.\n        waysForThisDivider := seatIndices[2\
        \ * k + 2] - seatIndices[2 * k + 1]\n        result = (result * waysForThisDivider)\
        \ % MOD\n    }\n\n    return result\n}"
      ruby: "class Solution\n    def number_of_ways(corridor)\n        mod = 10**9 +\
        \ 7\n\n        seat_indices = []\n        corridor.each_char.with_index do |char,\
        \ i|\n            if char == 'S'\n                seat_indices << i\n      \
        \      end\n        end\n\n        num_seats = seat_indices.length\n\n     \
        \   if num_seats == 0 || num_seats % 2 != 0\n            return 0\n        end\n\
        \n        result = 1\n        # We need to place dividers between (S_1, S_2),\
        \ (S_3, S_4), etc.\n        # These correspond to seat_indices[2k+1] and seat_indices[2k+2]\n\
        \        # for k = 0, 1, ..., num_seats/2 - 2\n\n        (0...(num_seats / 2\
        \ - 1)).each do |k|\n            # The divider is placed between seat_indices[2k+1]\
        \ and seat_indices[2k+2]\n            # Number of ways to place this divider\
        \ is the difference of their indices.\n            ways_for_this_divider = seat_indices[2\
        \ * k + 2] - seat_indices[2 * k + 1]\n            result = (result * ways_for_this_divider)\
        \ % mod\n        end\n\n        result\n    end\nend"
      scala: "object Solution {\n    def numberOfWays(corridor: String): Int = {\n \
        \       val MOD: Long = 1_000_000_007L\n\n        val seatIndices = corridor.zipWithIndex.collect\
        \ {\n            case (char, i) if char == 'S' => i\n        }\n\n        val\
        \ numSeats = seatIndices.length\n\n        if (numSeats == 0 || numSeats % 2\
        \ != 0) {\n            return 0\n        }\n\n        var result: Long = 1\n\
        \        // We need to place dividers between (S_1, S_2), (S_3, S_4), etc.\n\
        \        // These correspond to seatIndices[2k+1] and seatIndices[2k+2]\n  \
        \      // for k = 0, 1, ..., numSeats/2 - 2\n\n        for (k <- 0 until (numSeats\
        \ / 2 - 1)) {\n            // The divider is placed between seatIndices[2k+1]\
        \ and seatIndices[2k+2]\n            // Number of ways to place this divider\
        \ is the difference of their indices.\n            val waysForThisDivider =\
        \ (seatIndices(2 * k + 2) - seatIndices(2 * k + 1)).toLong\n            result\
        \ = (result * waysForThisDivider) % MOD\n        }\n\n        result.toInt\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn number_of_ways(corridor: String) -> i32 {\n\
        \        let modular: i64 = 1_000_000_007;\n\n        let mut seat_indices:\
        \ Vec<usize> = Vec::new();\n        for (i, char) in corridor.chars().enumerate()\
        \ {\n            if char == 'S' {\n                seat_indices.push(i);\n \
        \           }\n        }\n\n        let num_seats = seat_indices.len();\n\n\
        \        if num_seats == 0 || num_seats % 2 != 0 {\n            return 0;\n\
        \        }\n\n        let mut result: i64 = 1;\n        // We need to place\
        \ dividers between (S_1, S_2), (S_3, S_4), etc.\n        // These correspond\
        \ to seat_indices[2k+1] and seat_indices[2k+2]\n        // for k = 0, 1, ...,\
        \ num_seats/2 - 2\n\n        for k in 0..(num_seats / 2 - 1) {\n           \
        \ // The divider is placed between seat_indices[2k+1] and seat_indices[2k+2]\n\
        \            // Number of ways to place this divider is the difference of their\
        \ indices.\n            let ways_for_this_divider = (seat_indices[2 * k + 2]\
        \ - seat_indices[2 * k + 1]) as i64;\n            result = (result * ways_for_this_divider)\
        \ % modular;\n        }\n\n        result as i32\n    }\n}"
      racket: "#lang racket\n\n(define (number-of-ways corridor)\n  (define MOD 1000000007)\n\
        \n  (define seat-indices\n    (for/list ([char (in-string corridor)]\n     \
        \          [i (in-naturals)]\n               #:when (char=? char #\\S))\n  \
        \    i))\n\n  (define num-seats (length seat-indices))\n\n  (cond\n    [(or\
        \ (= num-seats 0) (odd? num-seats)) 0]\n    [else\n     (define result (make-box\
        \ 1))\n     (for ([k (in-range (quotient num-seats 2) 1)]) ; k from 0 to num-seats/2\
        \ - 2\n       (define ways-for-this-divider\n         (- (list-ref seat-indices\
        \ (+ (* 2 k) 2))\n            (list-ref seat-indices (+ (* 2 k) 1))))\n    \
        \   (set-box! result (modulo (* (unbox result) ways-for-this-divider) MOD)))\n\
        \     (unbox result))])"
      erlang: "-module(solution).\n-export([number_of_ways/1]).\n\nnumber_of_ways(Corridor)\
        \ ->\n    MOD = 1000000007,\n\n    SeatIndices = get_seat_indices(Corridor,\
        \ 0, []),\n\n    NumSeats = length(SeatIndices),\n\n    if\n        NumSeats\
        \ == 0; NumSeats rem 2 /= 0 ->\n            0;\n        true ->\n          \
        \  calculate_ways(SeatIndices, NumSeats, 0, 1, MOD)\n    end.\n\nget_seat_indices(<<>>,\
        \ _Idx, Acc) ->\n    lists:reverse(Acc);\nget_seat_indices(<<C, Rest/binary>>,\
        \ Idx, Acc) ->\n    if\n        C == $S ->\n            get_seat_indices(Rest,\
        \ Idx + 1, [Idx | Acc]);\n        true ->\n            get_seat_indices(Rest,\
        \ Idx + 1, Acc)\n    end.\n\ncalculate_ways(SeatIndices, NumSeats, K, CurrentResult,\
        \ MOD) ->\n    if\n        K >= NumSeats div 2 - 1 ->\n            CurrentResult;\n\
        \        true ->\n            Idx1 = lists:nth(2 * K + 1 + 1, SeatIndices),\
        \ % Erlang lists are 1-indexed\n            Idx2 = lists:nth(2 * K + 2 + 1,\
        \ SeatIndices),\n            WaysForThisDivider = Idx2 - Idx1,\n           \
        \ NewResult = (CurrentResult * WaysForThisDivider) rem MOD,\n            calculate_ways(SeatIndices,\
        \ NumSeats, K + 1, NewResult, MOD)\n    end."
      elixir: "defmodule Solution do\n  @spec number_of_ways(corridor :: String.t) ::\
        \ integer\n  def number_of_ways(corridor) do\n    mod = 1_000_000_007\n\n  \
        \  seat_indices =\n      corridor\n      |> String.graphemes()\n      |> Enum.with_index()\n\
        \      |> Enum.filter(fn {char, _} -> char == \"S\" end)\n      |> Enum.map(fn\
        \ {_, index} -> index end)\n\n    num_seats = length(seat_indices)\n\n    cond\
        \ do\n      num_seats == 0 or rem(num_seats, 2) != 0 ->\n        0\n      true\
        \ ->\n        # We need to place dividers between (S_1, S_2), (S_3, S_4), etc.\n\
        \        # These correspond to seat_indices[2k+1] and seat_indices[2k+2]\n \
        \       # for k = 0, 1, ..., num_seats/2 - 2\n\n        Enum.reduce(0..(div(num_seats,\
        \ 2) - 2), 1, fn k, acc ->\n          # The divider is placed between seat_indices[2k+1]\
        \ and seat_indices[2k+2]\n          # Number of ways to place this divider is\
        \ the difference of their indices.\n          ways_for_this_divider = Enum.at(seat_indices,\
        \ 2 * k + 2) - Enum.at(seat_indices, 2 * k + 1)\n          rem(acc * ways_for_this_divider,\
        \ mod)\n        end)\n    end\n  end\nend"
    approach: 'The problem requires dividing a corridor into non-overlapping sections,
      each containing exactly two seats. The key insight is that if the total number
      of seats is odd or zero, it''s impossible to satisfy the condition, so we return
      0. If there''s an even and positive number of seats, say `k` seats, they must
      be grouped into `k/2` pairs. The first pair will be `(S_0, S_1)`, the second `(S_2,
      S_3)`, and so on, up to `(S_{k-2}, S_{k-1})`. The sections are implicitly defined
      by these pairs. A divider must be placed between the end of one pair and the beginning
      of the next. Specifically, a divider must be placed after `S_{2i+1}` and before
      `S_{2i+2}` for each `i` from `0` to `k/2 - 2`.


      To count the number of ways, we first collect all indices of ''S'' characters
      into a list. After checking the total seat count, we iterate through the required
      divider positions. For each divider needed between `S_{2i+1}` (at index `idx_1`)
      and `S_{2i+2}` (at index `idx_2`), the number of valid positions to place this
      divider is `idx_2 - idx_1`. This is because a divider can be placed at any integer
      index `p` such that `idx_1 < p <= idx_2`. The total number of ways is the product
      of the number of choices for each such required divider, calculated modulo `10^9
      + 7`. If there are exactly two seats, no additional dividers are needed, and the
      result is 1.'
    time_complexity: The time complexity is O(N), where N is the length of the corridor
      string. This is because we iterate through the corridor once to collect all seat
      indices, which takes O(N) time. Subsequently, we iterate through the collected
      seat indices to calculate the product of ways. In the worst case, all characters
      are 'S', so the seat_indices list has N elements, and this second loop runs O(N)
      times. Each multiplication and modulo operation takes constant time.
    space_complexity: The space complexity is O(N) in the worst case. This is due to
      storing the indices of all 'S' characters in a list. In the worst case, if all
      characters in the corridor are 'S', the list will contain N elements. If the number
      of seats is small, the space complexity will be O(number_of_seats), which is at
      most O(N). An O(1) space solution is possible by iterating through the corridor
      and maintaining counts and previous seat indices, but the O(N) space solution
      is simpler to implement and sufficient for the given constraints.
    elapsed_time: 86.45214939117432
    model: gemini-2.5-flash
    generated_at: '2025-12-14 01:13:23 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int numberOfWays(string corridor) {\n   \
        \     int n = corridor.size();\n        int mod = 1e9 + 7;\n        int count\
        \ = 0;\n        for (int i = 0; i < n; i++) {\n            if (corridor[i] ==\
        \ 'S') count++;\n        }\n        if (count % 2 == 1) return 0;\n        int\
        \ res = 1;\n        int last = -1;\n        for (int i = 0; i < n; i++) {\n\
        \            if (corridor[i] == 'S') {\n                if (last != -1) {\n\
        \                    int k = i - last - 1;\n                    res = (res *\
        \ (k + 1)) % mod;\n                }\n                last = i;\n          \
        \  }\n        }\n        return res;\n    }\n};"
      java: "class Solution {\n    public int numberOfWays(String corridor) {\n    \
        \    int n = corridor.length();\n        int mod = (int)1e9 + 7;\n        int\
        \ count = 0;\n        for (int i = 0; i < n; i++) {\n            if (corridor.charAt(i)\
        \ == 'S') count++;\n        }\n        if (count % 2 == 1) return 0;\n     \
        \   int res = 1;\n        int last = -1;\n        for (int i = 0; i < n; i++)\
        \ {\n            if (corridor.charAt(i) == 'S') {\n                if (last\
        \ != -1) {\n                    int k = i - last - 1;\n                    res\
        \ = (res * (k + 1)) % mod;\n                }\n                last = i;\n \
        \           }\n        }\n        return res;\n    }\n}"
      python: "class Solution:\n    def numberOfWays(self, corridor: str) -> int:\n\
        \        n = len(corridor)\n        mod = 10**9 + 7\n        count = 0\n   \
        \     for i in range(n):\n            if corridor[i] == 'S': count += 1\n  \
        \      if count % 2 == 1: return 0\n        res = 1\n        last = -1\n   \
        \     for i in range(n):\n            if corridor[i] == 'S':\n             \
        \   if last != -1:\n                    k = i - last - 1\n                 \
        \   res = (res * (k + 1)) % mod\n                last = i\n        return res"
      python3: "class Solution:\n    def numberOfWays(self, corridor: str) -> int:\n\
        \        n = len(corridor)\n        mod = 10**9 + 7\n        count = 0\n   \
        \     for i in range(n):\n            if corridor[i] == 'S': count += 1\n  \
        \      if count % 2 == 1: return 0\n        res = 1\n        last = -1\n   \
        \     for i in range(n):\n            if corridor[i] == 'S':\n             \
        \   if last != -1:\n                    k = i - last - 1\n                 \
        \   res = (res * (k + 1)) % mod\n                last = i\n        return res"
      c: "typedef struct {\n} Solution;\n\nint numberOfWays(char * corridor) {\n   \
        \ int n = strlen(corridor);\n    int mod = 1000000007;\n    int count = 0;\n\
        \    for (int i = 0; i < n; i++) {\n        if (corridor[i] == 'S') count++;\n\
        \    }\n    if (count % 2 == 1) return 0;\n    int res = 1;\n    int last =\
        \ -1;\n    for (int i = 0; i < n; i++) {\n        if (corridor[i] == 'S') {\n\
        \            if (last != -1) {\n                int k = i - last - 1;\n    \
        \            res = (res * (k + 1)) % mod;\n            }\n            last =\
        \ i;\n        }\n    }\n    return res;\n}"
      csharp: "public class Solution {\n    public int NumberOfWays(string corridor)\
        \ {\n        int n = corridor.Length;\n        int mod = (int)1e9 + 7;\n   \
        \     int count = 0;\n        for (int i = 0; i < n; i++) {\n            if\
        \ (corridor[i] == 'S') count++;\n        }\n        if (count % 2 == 1) return\
        \ 0;\n        int res = 1;\n        int last = -1;\n        for (int i = 0;\
        \ i < n; i++) {\n            if (corridor[i] == 'S') {\n                if (last\
        \ != -1) {\n                    int k = i - last - 1;\n                    res\
        \ = (res * (k + 1)) % mod;\n                }\n                last = i;\n \
        \           }\n        }\n        return res;\n    }\n}"
      javascript: "var numberOfWays = function(corridor) {\n    let n = corridor.length;\n\
        \    let mod = 1000000007;\n    let count = 0;\n    for (let i = 0; i < n; i++)\
        \ {\n        if (corridor[i] === 'S') count++;\n    }\n    if (count % 2 ===\
        \ 1) return 0;\n    let res = 1;\n    let last = -1;\n    for (let i = 0; i\
        \ < n; i++) {\n        if (corridor[i] === 'S') {\n            if (last !==\
        \ -1) {\n                let k = i - last - 1;\n                res = (res *\
        \ (k + 1)) % mod;\n            }\n            last = i;\n        }\n    }\n\
        \    return res;\n};"
      typescript: "function numberOfWays(corridor: string): number {\n    let n: number\
        \ = corridor.length;\n    let mod: number = 1000000007;\n    let count: number\
        \ = 0;\n    for (let i: number = 0; i < n; i++) {\n        if (corridor[i] ===\
        \ 'S') count++;\n    }\n    if (count % 2 === 1) return 0;\n    let res: number\
        \ = 1;\n    let last: number = -1;\n    for (let i: number = 0; i < n; i++)\
        \ {\n        if (corridor[i] === 'S') {\n            if (last !== -1) {\n  \
        \              let k: number = i - last - 1;\n                res = (res * (k\
        \ + 1)) % mod;\n            }\n            last = i;\n        }\n    }\n   \
        \ return res;\n}"
      php: "class Solution {\n    function numberOfWays($corridor) {\n        $n = strlen($corridor);\n\
        \        $mod = 1000000007;\n        $count = 0;\n        for ($i = 0; $i <\
        \ $n; $i++) {\n            if ($corridor[$i] == 'S') $count++;\n        }\n\
        \        if ($count % 2 == 1) return 0;\n        $res = 1;\n        $last =\
        \ -1;\n        for ($i = 0; $i < $n; $i++) {\n            if ($corridor[$i]\
        \ == 'S') {\n                if ($last != -1) {\n                    $k = $i\
        \ - $last - 1;\n                    $res = ($res * ($k + 1)) % $mod;\n     \
        \           }\n                $last = $i;\n            }\n        }\n     \
        \   return $res;\n    }\n}"
      swift: "class Solution {\n    func numberOfWays(_ corridor: String) -> Int {\n\
        \        let n = corridor.count\n        let mod: Int = 1000000007\n       \
        \ var count = 0\n        for i in 0..<n {\n            if corridor[i] == \"\
        S\" {\n                count += 1\n            }\n        }\n        if count\
        \ % 2 == 1 {\n            return 0\n        }\n        var res = 1\n       \
        \ var last = -1\n        for i in 0..<n {\n            if corridor[i] == \"\
        S\" {\n                if last != -1 {\n                    let k = i - last\
        \ - 1\n                    res = (res * (k + 1)) % mod\n                }\n\
        \                last = i\n            }\n        }\n        return res\n  \
        \  }\n}"
      kotlin: "class Solution {\n    fun numberOfWays(corridor: String): Int {\n   \
        \     val n = corridor.length\n        val mod = 1000000007\n        var count\
        \ = 0\n        for (i in 0 until n) {\n            if (corridor[i] == 'S') count++\n\
        \        }\n        if (count % 2 == 1) return 0\n        var res = 1\n    \
        \    var last = -1\n        for (i in 0 until n) {\n            if (corridor[i]\
        \ == 'S') {\n                if (last != -1) {\n                    val k =\
        \ i - last - 1\n                    res = (res * (k + 1)) % mod\n          \
        \      }\n                last = i\n            }\n        }\n        return\
        \ res\n    }\n}"
      dart: "class Solution {\n    int numberOfWays(String corridor) {\n        int\
        \ n = corridor.length;\n        int mod = 1000000007;\n        int count = 0;\n\
        \        for (int i = 0; i < n; i++) {\n            if (corridor[i] == 'S')\
        \ count++;\n        }\n        if (count % 2 == 1) return 0;\n        int res\
        \ = 1;\n        int last = -1;\n        for (int i = 0; i < n; i++) {\n    \
        \        if (corridor[i] == 'S') {\n                if (last != -1) {\n    \
        \                int k = i - last - 1;\n                    res = (res * (k\
        \ + 1)) % mod;\n                }\n                last = i;\n            }\n\
        \        }\n        return res;\n    }\n}"
      go: "func numberOfWays(corridor string) int {\n    n := len(corridor)\n    mod\
        \ := 1000000007\n    count := 0\n    for i := 0; i < n; i++ {\n        if corridor[i]\
        \ == 'S' {\n            count++\n        }\n    }\n    if count%2 == 1 {\n \
        \       return 0\n    }\n    res := 1\n    last := -1\n    for i := 0; i < n;\
        \ i++ {\n        if corridor[i] == 'S' {\n            if last != -1 {\n    \
        \            k := i - last - 1\n                res = (res * (k + 1)) % mod\n\
        \            }\n            last = i\n        }\n    }\n    return res\n}"
      ruby: "class Solution\n    def number_of_ways(corridor)\n        n = corridor.size\n\
        \        mod = 1000000007\n        count = 0\n        for i in 0...n\n     \
        \       if corridor[i] == 'S'\n                count += 1\n            end\n\
        \        end\n        if count % 2 == 1\n            return 0\n        end\n\
        \        res = 1\n        last = -1\n        for i in 0...n\n            if\
        \ corridor[i] == 'S'\n                if last != -1\n                    k =\
        \ i - last - 1\n                    res = (res * (k + 1)) % mod\n          \
        \      end\n                last = i\n            end\n        end\n       \
        \ res\n    end\nend"
      scala: "object Solution {\n    def numberOfWays(corridor: String): Int = {\n \
        \       val n = corridor.length\n        val mod = 1000000007\n        var count\
        \ = 0\n        for (i <- 0 until n) {\n            if (corridor(i) == 'S') count\
        \ += 1\n        }\n        if (count % 2 == 1) return 0\n        var res = 1\n\
        \        var last = -1\n        for (i <- 0 until n) {\n            if (corridor(i)\
        \ == 'S') {\n                if (last != -1) {\n                    val k =\
        \ i - last - 1\n                    res = (res * (k + 1)) % mod\n          \
        \      }\n                last = i\n            }\n        }\n        res\n\
        \    }\n}"
      rust: "struct Solution;\n\nimpl Solution {\n    pub fn number_of_ways(corridor:\
        \ String) -> i32 {\n        let n: usize = corridor.len();\n        let mod:\
        \ i32 = 1000000007;\n        let mut count = 0;\n        for i in 0..n {\n \
        \           if corridor.as_bytes()[i] as char == 'S' {\n                count\
        \ += 1;\n            }\n        }\n        if count % 2 == 1 {\n           \
        \ return 0;\n        }\n        let mut res = 1;\n        let mut last = -1;\n\
        \        for i in 0..n {\n            if corridor.as_bytes()[i] as char == 'S'\
        \ {\n                if last != -1 {\n                    let k = i as i32 -\
        \ last - 1;\n                    res = (res * (k + 1)) % mod;\n            \
        \    }\n                last = i as i32;\n            }\n        }\n       \
        \ res\n    }\n}"
      racket: "define (number-of-ways corridor)\n    (let* (\n        (n (string-length\
        \ corridor))\n        (mod 1000000007)\n        (count 0)\n        (res 1)\n\
        \        (last -1))\n        (do ((i 0 (+ i 1))) ((= i n))\n            (if\
        \ (eq? (string-ref corridor i) #\\S)\n                (set! count (+ count 1))))\n\
        \        (if (eq? (mod count 2) 1)\n            0\n            (do ((i 0 (+\
        \ i 1))) ((= i n))\n                (if (eq? (string-ref corridor i) #\\S)\n\
        \                    (if (not (eq? last -1))\n                        (set!\
        \ res (mod (* res (+ (- i last) 1)) mod)))\n                    (set! last i))))\n\
        \        res))"
      erlang: "number_of_ways(Corridor) ->\n    N = length(Corridor),\n    Mod = 1000000007,\n\
        \    Count = lists:foldl(fun(X, Sum) -> if X == $S -> Sum + 1; true -> Sum end\
        \ end, 0, Corridor),\n    if Count rem 2 == 1 -> 0;\n    true ->\n        Res\
        \ = lists:foldl(fun(X, {Last, Res}) ->\n            if X == $S ->\n        \
        \        if Last == -1 -> {I, Res};\n                true ->\n             \
        \       K = I - Last - 1,\n                    {(I, (Res * (K + 1)) rem Mod)}\n\
        \            end;\n            true -> {Last, Res}\n        end, {-1, 1}, Corridor),\n\
        \        element(2, Res)\n    end."
      elixir: "def number_of_ways(corridor) do\n    n = String.length(corridor)\n  \
        \  mod = 1000000007\n    count = Enum.reduce(0..n-1, 0, fn i, acc -> if String.at(corridor,\
        \ i) == \"S\", do: acc + 1, else: acc end)\n    if rem(count, 2) == 1, do: 0\n\
        \    res = Enum.reduce(0..n-1, {-1, 1}, fn i, {last, res} ->\n        if String.at(corridor,\
        \ i) == \"S\" do\n            if last != -1 do\n                k = i - last\
        \ - 1\n                {i, rem(res * (k + 1), mod)}\n            else\n    \
        \            {i, res}\n            end\n        else\n            {last, res}\n\
        \        end\n    end)\n    elem(res, 1)\nend"
    approach: The problem can be solved by dividing the corridor into segments, each
      containing two seats. We start by counting the number of seats in the corridor.
      If the number of seats is odd, it's impossible to divide the corridor into segments
      with exactly two seats each, so we return 0. Otherwise, we iterate over the corridor
      and find the positions of the seats. We then calculate the number of ways to divide
      the corridor by finding the product of the number of possible positions between
      each pair of adjacent seats. The key intuition here is that the number of ways
      to divide the corridor is the product of the number of ways to divide each segment,
      which is determined by the number of plants between the seats in that segment.
    time_complexity: The time complexity of this solution is O(n), where n is the length
      of the corridor. This is because we make a single pass over the corridor to count
      the number of seats and find their positions, and then we make another pass to
      calculate the number of ways to divide the corridor. The product calculation is
      also O(n) because we only need to consider the positions between each pair of
      adjacent seats.
    space_complexity: The space complexity of this solution is O(1), which means the
      space required does not grow with the size of the input, making it very efficient
      in terms of memory usage. This is because we only use a constant amount of space
      to store the count of seats, the positions of the seats, and the result.
    elapsed_time: 8.473752498626709
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-14 01:13:31 '
---

## Problem #2147: Number of Ways to Divide a Long Corridor

**Difficulty:** Hard

**Topics:** Math, String, Dynamic Programming

## Problem Description

<p>Along a long library corridor, there is a line of seats and decorative plants. You are given a <strong>0-indexed</strong> string <code>corridor</code> of length <code>n</code> consisting of letters <code>&#39;S&#39;</code> and <code>&#39;P&#39;</code> where each <code>&#39;S&#39;</code> represents a seat and each <code>&#39;P&#39;</code> represents a plant.</p>

<p>One room divider has <strong>already</strong> been installed to the left of index <code>0</code>, and <strong>another</strong> to the right of index <code>n - 1</code>. Additional room dividers can be installed. For each position between indices <code>i - 1</code> and <code>i</code> (<code>1 &lt;= i &lt;= n - 1</code>), at most one divider can be installed.</p>

<p>Divide the corridor into non-overlapping sections, where each section has <strong>exactly two seats</strong> with any number of plants. There may be multiple ways to perform the division. Two ways are <strong>different</strong> if there is a position with a room divider installed in the first way but not in the second way.</p>

<p>Return <em>the number of ways to divide the corridor</em>. Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>. If there is no way, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/04/1.png" style="width: 410px; height: 199px;" />
<pre>
<strong>Input:</strong> corridor = &quot;SSPPSPS&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are 3 different ways to divide the corridor.
The black bars in the above image indicate the two room dividers already installed.
Note that in each of the ways, <strong>each</strong> section has exactly <strong>two</strong> seats.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/04/2.png" style="width: 357px; height: 68px;" />
<pre>
<strong>Input:</strong> corridor = &quot;PPSPSP&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> There is only 1 way to divide the corridor, by not installing any additional dividers.
Installing any would create some section that does not have exactly two seats.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/12/3.png" style="width: 115px; height: 68px;" />
<pre>
<strong>Input:</strong> corridor = &quot;S&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> There is no way to divide the corridor because there will always be a section that does not have exactly two seats.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == corridor.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>corridor[i]</code> is either <code>&#39;S&#39;</code> or <code>&#39;P&#39;</code>.</li>
</ul>


## Hints

1. Divide the corridor into segments. Each segment has two seats, starts precisely with one seat, and ends precisely with the other seat.

2. How many dividers can you install between two adjacent segments? You must install precisely one. Otherwise, you would have created a section with not exactly two seats.

3. If there are k plants between two adjacent segments, there are k + 1 positions (ways) you could install the divider you must install.

4. The problem now becomes: Find the product of all possible positions between every two adjacent segments.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-14 01:13:23 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem requires dividing a corridor into non-overlapping sections, each containing exactly two seats. The key insight is that if the total number of seats is odd or zero, it's impossible to satisfy the condition, so we return 0. If there's an even and positive number of seats, say `k` seats, they must be grouped into `k/2` pairs. The first pair will be `(S_0, S_1)`, the second `(S_2, S_3)`, and so on, up to `(S_{k-2}, S_{k-1})`. The sections are implicitly defined by these pairs. A divider must be placed between the end of one pair and the beginning of the next. Specifically, a divider must be placed after `S_{2i+1}` and before `S_{2i+2}` for each `i` from `0` to `k/2 - 2`.

To count the number of ways, we first collect all indices of 'S' characters into a list. After checking the total seat count, we iterate through the required divider positions. For each divider needed between `S_{2i+1}` (at index `idx_1`) and `S_{2i+2}` (at index `idx_2`), the number of valid positions to place this divider is `idx_2 - idx_1`. This is because a divider can be placed at any integer index `p` such that `idx_1 < p <= idx_2`. The total number of ways is the product of the number of choices for each such required divider, calculated modulo `10^9 + 7`. If there are exactly two seats, no additional dividers are needed, and the result is 1.

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
    int numberOfWays(std::string corridor) {
        long long MOD = 1e9 + 7;

        std::vector<int> seat_indices;
        for (int i = 0; i < corridor.length(); ++i) {
            if (corridor[i] == 'S') {
                seat_indices.push_back(i);
            }
        }

        int num_seats = seat_indices.size();

        if (num_seats == 0 || num_seats % 2 != 0) {
            return 0;
        }

        long long result = 1;
        // We need to place dividers between (S_1, S_2), (S_3, S_4), etc.
        // These correspond to seat_indices[2k+1] and seat_indices[2k+2]
        // for k = 0, 1, ..., num_seats/2 - 2

        for (int k = 0; k < num_seats / 2 - 1; ++k) {
            // The divider is placed between seat_indices[2k+1] and seat_indices[2k+2]
            // Number of ways to place this divider is the difference of their indices.
            long long ways_for_this_divider = seat_indices[2 * k + 2] - seat_indices[2 * k + 1];
            result = (result * ways_for_this_divider) % MOD;
        }

        return static_cast<int>(result);
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.ArrayList;
import java.util.List;

class Solution {
    public int numberOfWays(String corridor) {
        long MOD = 1_000_000_007;

        List<Integer> seatIndices = new ArrayList<>();
        for (int i = 0; i < corridor.length(); ++i) {
            if (corridor.charAt(i) == 'S') {
                seatIndices.add(i);
            }
        }

        int numSeats = seatIndices.size();

        if (numSeats == 0 || numSeats % 2 != 0) {
            return 0;
        }

        long result = 1;
        // We need to place dividers between (S_1, S_2), (S_3, S_4), etc.
        // These correspond to seatIndices[2k+1] and seatIndices[2k+2]
        // for k = 0, 1, ..., numSeats/2 - 2

        for (int k = 0; k < numSeats / 2 - 1; ++k) {
            // The divider is placed between seatIndices[2k+1] and seatIndices[2k+2]
            // Number of ways to place this divider is the difference of their indices.
            long waysForThisDivider = seatIndices.get(2 * k + 2) - seatIndices.get(2 * k + 1);
            result = (result * waysForThisDivider) % MOD;
        }

        return (int) result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7

        seat_indices = []
        for i, char in enumerate(corridor):
            if char == 'S':
                seat_indices.append(i)

        num_seats = len(seat_indices)

        if num_seats == 0 or num_seats % 2 != 0:
            return 0

        result = 1
        # We need to place dividers between (S_1, S_2), (S_3, S_4), etc.
        # These correspond to seat_indices[2k+1] and seat_indices[2k+2]
        # for k = 0, 1, ..., num_seats/2 - 2

        for k in range(num_seats // 2 - 1):
            # The divider is placed between seat_indices[2k+1] and seat_indices[2k+2]
            # Number of ways to place this divider is the difference of their indices.
            ways_for_this_divider = seat_indices[2 * k + 2] - seat_indices[2 * k + 1]
            result = (result * ways_for_this_divider) % MOD

        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7

        seat_indices = []
        for i, char in enumerate(corridor):
            if char == 'S':
                seat_indices.append(i)

        num_seats = len(seat_indices)

        if num_seats == 0 or num_seats % 2 != 0:
            return 0

        result = 1
        # We need to place dividers between (S_1, S_2), (S_3, S_4), etc.
        # These correspond to seat_indices[2k+1] and seat_indices[2k+2]
        # for k = 0, 1, ..., num_seats/2 - 2

        for k in range(num_seats // 2 - 1):
            # The divider is placed between seat_indices[2k+1] and seat_indices[2k+2]
            # Number of ways to place this divider is the difference of their indices.
            ways_for_this_divider = seat_indices[2 * k + 2] - seat_indices[2 * k + 1]
            result = (result * ways_for_this_divider) % MOD

        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

// Function to dynamically grow an array (vector equivalent)
typedef struct {
    int* data;
    int size;
    int capacity;
} IntVector;

void initIntVector(IntVector* vec, int initialCapacity) {
    vec->data = (int*)malloc(sizeof(int) * initialCapacity);
    vec->size = 0;
    vec->capacity = initialCapacity;
}

void pushBackIntVector(IntVector* vec, int value) {
    if (vec->size == vec->capacity) {
        vec->capacity *= 2;
        vec->data = (int*)realloc(vec->data, sizeof(int) * vec->capacity);
    }
    vec->data[vec->size++] = value;
}

void freeIntVector(IntVector* vec) {
    free(vec->data);
    vec->data = NULL;
    vec->size = 0;
    vec->capacity = 0;
}

int numberOfWays(char* corridor) {
    long long MOD = 1e9 + 7;

    IntVector seat_indices;
    initIntVector(&seat_indices, 10); // Initial capacity

    int n = strlen(corridor);
    for (int i = 0; i < n; ++i) {
        if (corridor[i] == 'S') {
            pushBackIntVector(&seat_indices, i);
        }
    }

    int num_seats = seat_indices.size;

    if (num_seats == 0 || num_seats % 2 != 0) {
        freeIntVector(&seat_indices);
        return 0;
    }

    long long result = 1;
    // We need to place dividers between (S_1, S_2), (S_3, S_4), etc.
    // These correspond to seat_indices[2k+1] and seat_indices[2k+2]
    // for k = 0, 1, ..., num_seats/2 - 2

    for (int k = 0; k < num_seats / 2 - 1; ++k) {
        // The divider is placed between seat_indices[2k+1] and seat_indices[2k+2]
        // Number of ways to place this divider is the difference of their indices.
        long long ways_for_this_divider = seat_indices.data[2 * k + 2] - seat_indices.data[2 * k + 1];
        result = (result * ways_for_this_divider) % MOD;
    }

    freeIntVector(&seat_indices);
    return (int)result;
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
    public int NumberOfWays(string corridor) {
        long MOD = 1_000_000_007;

        List<int> seatIndices = new List<int>();
        for (int i = 0; i < corridor.Length; ++i) {
            if (corridor[i] == 'S') {
                seatIndices.Add(i);
            }
        }

        int numSeats = seatIndices.Count;

        if (numSeats == 0 || numSeats % 2 != 0) {
            return 0;
        }

        long result = 1;
        // We need to place dividers between (S_1, S_2), (S_3, S_4), etc.
        // These correspond to seatIndices[2k+1] and seatIndices[2k+2]
        // for k = 0, 1, ..., numSeats/2 - 2

        for (int k = 0; k < numSeats / 2 - 1; ++k) {
            // The divider is placed between seatIndices[2k+1] and seatIndices[2k+2]
            // Number of ways to place this divider is the difference of their indices.
            long waysForThisDivider = seatIndices[2 * k + 2] - seatIndices[2 * k + 1];
            result = (result * waysForThisDivider) % MOD;
        }

        return (int) result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} corridor
 * @return {number}
 */
var numberOfWays = function(corridor) {
    const MOD = 1_000_000_007;

    const seatIndices = [];
    for (let i = 0; i < corridor.length; ++i) {
        if (corridor[i] === 'S') {
            seatIndices.push(i);
        }
    }

    const numSeats = seatIndices.length;

    if (numSeats === 0 || numSeats % 2 !== 0) {
        return 0;
    }

    let result = 1;
    // We need to place dividers between (S_1, S_2), (S_3, S_4), etc.
    // These correspond to seatIndices[2k+1] and seatIndices[2k+2]
    // for k = 0, 1, ..., numSeats/2 - 2

    for (let k = 0; k < numSeats / 2 - 1; ++k) {
        // The divider is placed between seatIndices[2k+1] and seatIndices[2k+2]
        // Number of ways to place this divider is the difference of their indices.
        const waysForThisDivider = seatIndices[2 * k + 2] - seatIndices[2 * k + 1];
        result = (result * waysForThisDivider) % MOD;
    }

    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function numberOfWays(corridor: string): number {
    const MOD = 1_000_000_007;

    const seatIndices: number[] = [];
    for (let i = 0; i < corridor.length; ++i) {
        if (corridor[i] === 'S') {
            seatIndices.push(i);
        }
    }

    const numSeats = seatIndices.length;

    if (numSeats === 0 || numSeats % 2 !== 0) {
        return 0;
    }

    let result = 1;
    // We need to place dividers between (S_1, S_2), (S_3, S_4), etc.
    // These correspond to seatIndices[2k+1] and seatIndices[2k+2]
    // for k = 0, 1, ..., numSeats/2 - 2

    for (let k = 0; k < numSeats / 2 - 1; ++k) {
        // The divider is placed between seatIndices[2k+1] and seatIndices[2k+2]
        // Number of ways to place this divider is the difference of their indices.
        const waysForThisDivider = seatIndices[2 * k + 2] - seatIndices[2 * k + 1];
        result = (result * waysForThisDivider) % MOD;
    }

    return result;
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
     * @param String $corridor
     * @return Integer
     */
    function numberOfWays($corridor) {
        $MOD = 1_000_000_007;

        $seatIndices = [];
        for ($i = 0; $i < strlen($corridor); ++$i) {
            if ($corridor[$i] === 'S') {
                $seatIndices[] = $i;
            }
        }

        $numSeats = count($seatIndices);

        if ($numSeats === 0 || $numSeats % 2 !== 0) {
            return 0;
        }

        $result = 1;
        // We need to place dividers between (S_1, S_2), (S_3, S_4), etc.
        // These correspond to seatIndices[2k+1] and seatIndices[2k+2]
        // for k = 0, 1, ..., numSeats/2 - 2

        for ($k = 0; $k < $numSeats / 2 - 1; ++$k) {
            // The divider is placed between seatIndices[2k+1] and seatIndices[2k+2]
            // Number of ways to place this divider is the difference of their indices.
            $waysForThisDivider = $seatIndices[2 * $k + 2] - $seatIndices[2 * $k + 1];
            $result = ($result * $waysForThisDivider) % $MOD;
        }

        return $result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func numberOfWays(_ corridor: String) -> Int {
        let MOD = 1_000_000_007

        var seatIndices: [Int] = []
        for (i, char) in corridor.enumerated() {
            if char == "S" {
                seatIndices.append(i)
            }
        }

        let numSeats = seatIndices.count

        if numSeats == 0 || numSeats % 2 != 0 {
            return 0
        }

        var result: Int = 1
        // We need to place dividers between (S_1, S_2), (S_3, S_4), etc.
        // These correspond to seatIndices[2k+1] and seatIndices[2k+2]
        // for k = 0, 1, ..., numSeats/2 - 2

        for k in 0..<(numSeats / 2 - 1) {
            // The divider is placed between seatIndices[2k+1] and seatIndices[2k+2]
            // Number of ways to place this divider is the difference of their indices.
            let waysForThisDivider = seatIndices[2 * k + 2] - seatIndices[2 * k + 1]
            result = (result * waysForThisDivider) % MOD
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
    fun numberOfWays(corridor: String): Int {
        val MOD = 1_000_000_007L

        val seatIndices = mutableListOf<Int>()
        for (i in corridor.indices) {
            if (corridor[i] == 'S') {
                seatIndices.add(i)
            }
        }

        val numSeats = seatIndices.size

        if (numSeats == 0 || numSeats % 2 != 0) {
            return 0
        }

        var result: Long = 1
        // We need to place dividers between (S_1, S_2), (S_3, S_4), etc.
        // These correspond to seatIndices[2k+1] and seatIndices[2k+2]
        // for k = 0, 1, ..., numSeats/2 - 2

        for (k in 0 until (numSeats / 2 - 1)) {
            // The divider is placed between seatIndices[2k+1] and seatIndices[2k+2]
            // Number of ways to place this divider is the difference of their indices.
            val waysForThisDivider = (seatIndices[2 * k + 2] - seatIndices[2 * k + 1]).toLong()
            result = (result * waysForThisDivider) % MOD
        }

        return result.toInt()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int numberOfWays(String corridor) {
    final int MOD = 1000000007;

    List<int> seatIndices = [];
    for (int i = 0; i < corridor.length; ++i) {
      if (corridor[i] == 'S') {
        seatIndices.add(i);
      }
    }

    int numSeats = seatIndices.length;

    if (numSeats == 0 || numSeats % 2 != 0) {
      return 0;
    }

    int result = 1;
    // We need to place dividers between (S_1, S_2), (S_3, S_4), etc.
    // These correspond to seatIndices[2k+1] and seatIndices[2k+2]
    // for k = 0, 1, ..., numSeats/2 - 2

    for (int k = 0; k < numSeats ~/ 2 - 1; ++k) {
      // The divider is placed between seatIndices[2k+1] and seatIndices[2k+2]
      // Number of ways to place this divider is the difference of their indices.
      int waysForThisDivider = seatIndices[2 * k + 2] - seatIndices[2 * k + 1];
      result = (result * waysForThisDivider) % MOD;
    }

    return result;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

import "strings"

func numberOfWays(corridor string) int {
    const MOD int = 1e9 + 7

    var seatIndices []int
    for i, char := range corridor {
        if char == 'S' {
            seatIndices = append(seatIndices, i)
        }
    }

    numSeats := len(seatIndices)

    if numSeats == 0 || numSeats % 2 != 0 {
        return 0
    }

    result := 1
    // We need to place dividers between (S_1, S_2), (S_3, S_4), etc.
    // These correspond to seatIndices[2k+1] and seatIndices[2k+2]
    // for k = 0, 1, ..., numSeats/2 - 2

    for k := 0; k < numSeats / 2 - 1; k++ {
        // The divider is placed between seatIndices[2k+1] and seatIndices[2k+2]
        // Number of ways to place this divider is the difference of their indices.
        waysForThisDivider := seatIndices[2 * k + 2] - seatIndices[2 * k + 1]
        result = (result * waysForThisDivider) % MOD
    }

    return result
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    def number_of_ways(corridor)
        mod = 10**9 + 7

        seat_indices = []
        corridor.each_char.with_index do |char, i|
            if char == 'S'
                seat_indices << i
            end
        end

        num_seats = seat_indices.length

        if num_seats == 0 || num_seats % 2 != 0
            return 0
        end

        result = 1
        # We need to place dividers between (S_1, S_2), (S_3, S_4), etc.
        # These correspond to seat_indices[2k+1] and seat_indices[2k+2]
        # for k = 0, 1, ..., num_seats/2 - 2

        (0...(num_seats / 2 - 1)).each do |k|
            # The divider is placed between seat_indices[2k+1] and seat_indices[2k+2]
            # Number of ways to place this divider is the difference of their indices.
            ways_for_this_divider = seat_indices[2 * k + 2] - seat_indices[2 * k + 1]
            result = (result * ways_for_this_divider) % mod
        end

        result
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def numberOfWays(corridor: String): Int = {
        val MOD: Long = 1_000_000_007L

        val seatIndices = corridor.zipWithIndex.collect {
            case (char, i) if char == 'S' => i
        }

        val numSeats = seatIndices.length

        if (numSeats == 0 || numSeats % 2 != 0) {
            return 0
        }

        var result: Long = 1
        // We need to place dividers between (S_1, S_2), (S_3, S_4), etc.
        // These correspond to seatIndices[2k+1] and seatIndices[2k+2]
        // for k = 0, 1, ..., numSeats/2 - 2

        for (k <- 0 until (numSeats / 2 - 1)) {
            // The divider is placed between seatIndices[2k+1] and seatIndices[2k+2]
            // Number of ways to place this divider is the difference of their indices.
            val waysForThisDivider = (seatIndices(2 * k + 2) - seatIndices(2 * k + 1)).toLong
            result = (result * waysForThisDivider) % MOD
        }

        result.toInt
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn number_of_ways(corridor: String) -> i32 {
        let modular: i64 = 1_000_000_007;

        let mut seat_indices: Vec<usize> = Vec::new();
        for (i, char) in corridor.chars().enumerate() {
            if char == 'S' {
                seat_indices.push(i);
            }
        }

        let num_seats = seat_indices.len();

        if num_seats == 0 || num_seats % 2 != 0 {
            return 0;
        }

        let mut result: i64 = 1;
        // We need to place dividers between (S_1, S_2), (S_3, S_4), etc.
        // These correspond to seat_indices[2k+1] and seat_indices[2k+2]
        // for k = 0, 1, ..., num_seats/2 - 2

        for k in 0..(num_seats / 2 - 1) {
            // The divider is placed between seat_indices[2k+1] and seat_indices[2k+2]
            // Number of ways to place this divider is the difference of their indices.
            let ways_for_this_divider = (seat_indices[2 * k + 2] - seat_indices[2 * k + 1]) as i64;
            result = (result * ways_for_this_divider) % modular;
        }

        result as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (number-of-ways corridor)
  (define MOD 1000000007)

  (define seat-indices
    (for/list ([char (in-string corridor)]
               [i (in-naturals)]
               #:when (char=? char #\S))
      i))

  (define num-seats (length seat-indices))

  (cond
    [(or (= num-seats 0) (odd? num-seats)) 0]
    [else
     (define result (make-box 1))
     (for ([k (in-range (quotient num-seats 2) 1)]) ; k from 0 to num-seats/2 - 2
       (define ways-for-this-divider
         (- (list-ref seat-indices (+ (* 2 k) 2))
            (list-ref seat-indices (+ (* 2 k) 1))))
       (set-box! result (modulo (* (unbox result) ways-for-this-divider) MOD)))
     (unbox result))])
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([number_of_ways/1]).

number_of_ways(Corridor) ->
    MOD = 1000000007,

    SeatIndices = get_seat_indices(Corridor, 0, []),

    NumSeats = length(SeatIndices),

    if
        NumSeats == 0; NumSeats rem 2 /= 0 ->
            0;
        true ->
            calculate_ways(SeatIndices, NumSeats, 0, 1, MOD)
    end.

get_seat_indices(<<>>, _Idx, Acc) ->
    lists:reverse(Acc);
get_seat_indices(<<C, Rest/binary>>, Idx, Acc) ->
    if
        C == $S ->
            get_seat_indices(Rest, Idx + 1, [Idx | Acc]);
        true ->
            get_seat_indices(Rest, Idx + 1, Acc)
    end.

calculate_ways(SeatIndices, NumSeats, K, CurrentResult, MOD) ->
    if
        K >= NumSeats div 2 - 1 ->
            CurrentResult;
        true ->
            Idx1 = lists:nth(2 * K + 1 + 1, SeatIndices), % Erlang lists are 1-indexed
            Idx2 = lists:nth(2 * K + 2 + 1, SeatIndices),
            WaysForThisDivider = Idx2 - Idx1,
            NewResult = (CurrentResult * WaysForThisDivider) rem MOD,
            calculate_ways(SeatIndices, NumSeats, K + 1, NewResult, MOD)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec number_of_ways(corridor :: String.t) :: integer
  def number_of_ways(corridor) do
    mod = 1_000_000_007

    seat_indices =
      corridor
      |> String.graphemes()
      |> Enum.with_index()
      |> Enum.filter(fn {char, _} -> char == "S" end)
      |> Enum.map(fn {_, index} -> index end)

    num_seats = length(seat_indices)

    cond do
      num_seats == 0 or rem(num_seats, 2) != 0 ->
        0
      true ->
        # We need to place dividers between (S_1, S_2), (S_3, S_4), etc.
        # These correspond to seat_indices[2k+1] and seat_indices[2k+2]
        # for k = 0, 1, ..., num_seats/2 - 2

        Enum.reduce(0..(div(num_seats, 2) - 2), 1, fn k, acc ->
          # The divider is placed between seat_indices[2k+1] and seat_indices[2k+2]
          # Number of ways to place this divider is the difference of their indices.
          ways_for_this_divider = Enum.at(seat_indices, 2 * k + 2) - Enum.at(seat_indices, 2 * k + 1)
          rem(acc * ways_for_this_divider, mod)
        end)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N), where N is the length of the corridor string. This is because we iterate through the corridor once to collect all seat indices, which takes O(N) time. Subsequently, we iterate through the collected seat indices to calculate the product of ways. In the worst case, all characters are 'S', so the seat_indices list has N elements, and this second loop runs O(N) times. Each multiplication and modulo operation takes constant time.

- **Space Complexity:** The space complexity is O(N) in the worst case. This is due to storing the indices of all 'S' characters in a list. In the worst case, if all characters in the corridor are 'S', the list will contain N elements. If the number of seats is small, the space complexity will be O(number_of_seats), which is at most O(N). An O(1) space solution is possible by iterating through the corridor and maintaining counts and previous seat indices, but the O(N) space solution is simpler to implement and sufficient for the given constraints.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-14 01:13:31 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by dividing the corridor into segments, each containing two seats. We start by counting the number of seats in the corridor. If the number of seats is odd, it's impossible to divide the corridor into segments with exactly two seats each, so we return 0. Otherwise, we iterate over the corridor and find the positions of the seats. We then calculate the number of ways to divide the corridor by finding the product of the number of possible positions between each pair of adjacent seats. The key intuition here is that the number of ways to divide the corridor is the product of the number of ways to divide each segment, which is determined by the number of plants between the seats in that segment.

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
    int numberOfWays(string corridor) {
        int n = corridor.size();
        int mod = 1e9 + 7;
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (corridor[i] == 'S') count++;
        }
        if (count % 2 == 1) return 0;
        int res = 1;
        int last = -1;
        for (int i = 0; i < n; i++) {
            if (corridor[i] == 'S') {
                if (last != -1) {
                    int k = i - last - 1;
                    res = (res * (k + 1)) % mod;
                }
                last = i;
            }
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
    public int numberOfWays(String corridor) {
        int n = corridor.length();
        int mod = (int)1e9 + 7;
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (corridor.charAt(i) == 'S') count++;
        }
        if (count % 2 == 1) return 0;
        int res = 1;
        int last = -1;
        for (int i = 0; i < n; i++) {
            if (corridor.charAt(i) == 'S') {
                if (last != -1) {
                    int k = i - last - 1;
                    res = (res * (k + 1)) % mod;
                }
                last = i;
            }
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
    def numberOfWays(self, corridor: str) -> int:
        n = len(corridor)
        mod = 10**9 + 7
        count = 0
        for i in range(n):
            if corridor[i] == 'S': count += 1
        if count % 2 == 1: return 0
        res = 1
        last = -1
        for i in range(n):
            if corridor[i] == 'S':
                if last != -1:
                    k = i - last - 1
                    res = (res * (k + 1)) % mod
                last = i
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        n = len(corridor)
        mod = 10**9 + 7
        count = 0
        for i in range(n):
            if corridor[i] == 'S': count += 1
        if count % 2 == 1: return 0
        res = 1
        last = -1
        for i in range(n):
            if corridor[i] == 'S':
                if last != -1:
                    k = i - last - 1
                    res = (res * (k + 1)) % mod
                last = i
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
typedef struct {
} Solution;

int numberOfWays(char * corridor) {
    int n = strlen(corridor);
    int mod = 1000000007;
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (corridor[i] == 'S') count++;
    }
    if (count % 2 == 1) return 0;
    int res = 1;
    int last = -1;
    for (int i = 0; i < n; i++) {
        if (corridor[i] == 'S') {
            if (last != -1) {
                int k = i - last - 1;
                res = (res * (k + 1)) % mod;
            }
            last = i;
        }
    }
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int NumberOfWays(string corridor) {
        int n = corridor.Length;
        int mod = (int)1e9 + 7;
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (corridor[i] == 'S') count++;
        }
        if (count % 2 == 1) return 0;
        int res = 1;
        int last = -1;
        for (int i = 0; i < n; i++) {
            if (corridor[i] == 'S') {
                if (last != -1) {
                    int k = i - last - 1;
                    res = (res * (k + 1)) % mod;
                }
                last = i;
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
var numberOfWays = function(corridor) {
    let n = corridor.length;
    let mod = 1000000007;
    let count = 0;
    for (let i = 0; i < n; i++) {
        if (corridor[i] === 'S') count++;
    }
    if (count % 2 === 1) return 0;
    let res = 1;
    let last = -1;
    for (let i = 0; i < n; i++) {
        if (corridor[i] === 'S') {
            if (last !== -1) {
                let k = i - last - 1;
                res = (res * (k + 1)) % mod;
            }
            last = i;
        }
    }
    return res;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function numberOfWays(corridor: string): number {
    let n: number = corridor.length;
    let mod: number = 1000000007;
    let count: number = 0;
    for (let i: number = 0; i < n; i++) {
        if (corridor[i] === 'S') count++;
    }
    if (count % 2 === 1) return 0;
    let res: number = 1;
    let last: number = -1;
    for (let i: number = 0; i < n; i++) {
        if (corridor[i] === 'S') {
            if (last !== -1) {
                let k: number = i - last - 1;
                res = (res * (k + 1)) % mod;
            }
            last = i;
        }
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
    function numberOfWays($corridor) {
        $n = strlen($corridor);
        $mod = 1000000007;
        $count = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($corridor[$i] == 'S') $count++;
        }
        if ($count % 2 == 1) return 0;
        $res = 1;
        $last = -1;
        for ($i = 0; $i < $n; $i++) {
            if ($corridor[$i] == 'S') {
                if ($last != -1) {
                    $k = $i - $last - 1;
                    $res = ($res * ($k + 1)) % $mod;
                }
                $last = $i;
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
    func numberOfWays(_ corridor: String) -> Int {
        let n = corridor.count
        let mod: Int = 1000000007
        var count = 0
        for i in 0..<n {
            if corridor[i] == "S" {
                count += 1
            }
        }
        if count % 2 == 1 {
            return 0
        }
        var res = 1
        var last = -1
        for i in 0..<n {
            if corridor[i] == "S" {
                if last != -1 {
                    let k = i - last - 1
                    res = (res * (k + 1)) % mod
                }
                last = i
            }
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
    fun numberOfWays(corridor: String): Int {
        val n = corridor.length
        val mod = 1000000007
        var count = 0
        for (i in 0 until n) {
            if (corridor[i] == 'S') count++
        }
        if (count % 2 == 1) return 0
        var res = 1
        var last = -1
        for (i in 0 until n) {
            if (corridor[i] == 'S') {
                if (last != -1) {
                    val k = i - last - 1
                    res = (res * (k + 1)) % mod
                }
                last = i
            }
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
    int numberOfWays(String corridor) {
        int n = corridor.length;
        int mod = 1000000007;
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (corridor[i] == 'S') count++;
        }
        if (count % 2 == 1) return 0;
        int res = 1;
        int last = -1;
        for (int i = 0; i < n; i++) {
            if (corridor[i] == 'S') {
                if (last != -1) {
                    int k = i - last - 1;
                    res = (res * (k + 1)) % mod;
                }
                last = i;
            }
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
func numberOfWays(corridor string) int {
    n := len(corridor)
    mod := 1000000007
    count := 0
    for i := 0; i < n; i++ {
        if corridor[i] == 'S' {
            count++
        }
    }
    if count%2 == 1 {
        return 0
    }
    res := 1
    last := -1
    for i := 0; i < n; i++ {
        if corridor[i] == 'S' {
            if last != -1 {
                k := i - last - 1
                res = (res * (k + 1)) % mod
            }
            last = i
        }
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
    def number_of_ways(corridor)
        n = corridor.size
        mod = 1000000007
        count = 0
        for i in 0...n
            if corridor[i] == 'S'
                count += 1
            end
        end
        if count % 2 == 1
            return 0
        end
        res = 1
        last = -1
        for i in 0...n
            if corridor[i] == 'S'
                if last != -1
                    k = i - last - 1
                    res = (res * (k + 1)) % mod
                end
                last = i
            end
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
    def numberOfWays(corridor: String): Int = {
        val n = corridor.length
        val mod = 1000000007
        var count = 0
        for (i <- 0 until n) {
            if (corridor(i) == 'S') count += 1
        }
        if (count % 2 == 1) return 0
        var res = 1
        var last = -1
        for (i <- 0 until n) {
            if (corridor(i) == 'S') {
                if (last != -1) {
                    val k = i - last - 1
                    res = (res * (k + 1)) % mod
                }
                last = i
            }
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
    pub fn number_of_ways(corridor: String) -> i32 {
        let n: usize = corridor.len();
        let mod: i32 = 1000000007;
        let mut count = 0;
        for i in 0..n {
            if corridor.as_bytes()[i] as char == 'S' {
                count += 1;
            }
        }
        if count % 2 == 1 {
            return 0;
        }
        let mut res = 1;
        let mut last = -1;
        for i in 0..n {
            if corridor.as_bytes()[i] as char == 'S' {
                if last != -1 {
                    let k = i as i32 - last - 1;
                    res = (res * (k + 1)) % mod;
                }
                last = i as i32;
            }
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
define (number-of-ways corridor)
    (let* (
        (n (string-length corridor))
        (mod 1000000007)
        (count 0)
        (res 1)
        (last -1))
        (do ((i 0 (+ i 1))) ((= i n))
            (if (eq? (string-ref corridor i) #\S)
                (set! count (+ count 1))))
        (if (eq? (mod count 2) 1)
            0
            (do ((i 0 (+ i 1))) ((= i n))
                (if (eq? (string-ref corridor i) #\S)
                    (if (not (eq? last -1))
                        (set! res (mod (* res (+ (- i last) 1)) mod)))
                    (set! last i))))
        res))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
number_of_ways(Corridor) ->
    N = length(Corridor),
    Mod = 1000000007,
    Count = lists:foldl(fun(X, Sum) -> if X == $S -> Sum + 1; true -> Sum end end, 0, Corridor),
    if Count rem 2 == 1 -> 0;
    true ->
        Res = lists:foldl(fun(X, {Last, Res}) ->
            if X == $S ->
                if Last == -1 -> {I, Res};
                true ->
                    K = I - Last - 1,
                    {(I, (Res * (K + 1)) rem Mod)}
            end;
            true -> {Last, Res}
        end, {-1, 1}, Corridor),
        element(2, Res)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
def number_of_ways(corridor) do
    n = String.length(corridor)
    mod = 1000000007
    count = Enum.reduce(0..n-1, 0, fn i, acc -> if String.at(corridor, i) == "S", do: acc + 1, else: acc end)
    if rem(count, 2) == 1, do: 0
    res = Enum.reduce(0..n-1, {-1, 1}, fn i, {last, res} ->
        if String.at(corridor, i) == "S" do
            if last != -1 do
                k = i - last - 1
                {i, rem(res * (k + 1), mod)}
            else
                {i, res}
            end
        else
            {last, res}
        end
    end)
    elem(res, 1)
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this solution is O(n), where n is the length of the corridor. This is because we make a single pass over the corridor to count the number of seats and find their positions, and then we make another pass to calculate the number of ways to divide the corridor. The product calculation is also O(n) because we only need to consider the positions between each pair of adjacent seats.

- **Space Complexity:** The space complexity of this solution is O(1), which means the space required does not grow with the size of the input, making it very efficient in terms of memory usage. This is because we only use a constant amount of space to store the count of seats, the positions of the seats, and the result.

</div>
</details>
