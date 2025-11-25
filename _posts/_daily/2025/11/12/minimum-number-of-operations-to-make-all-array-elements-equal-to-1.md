---
layout: post
title: "Minimum Number of Operations to Make All Array Elements Equal to 1"
date: 2025-11-12 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Math", "Number Theory"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <numeric>\n#include <algorithm>\n\nclass Solution\
        \ {\npublic:\n    int minOperations(std::vector<int>& nums) {\n        int n\
        \ = nums.size();\n        int count_ones = 0;\n        for (int x : nums) {\n\
        \            if (x == 1) {\n                count_ones++;\n            }\n \
        \       }\n\n        if (count_ones > 0) {\n            return n - count_ones;\n\
        \        }\n\n        // No ones in the array, need to create one.\n       \
        \ // Find the shortest subarray whose GCD is 1.\n        int min_len_to_one\
        \ = n + 1; // Initialize with a value larger than any possible length\n\n  \
        \      for (int i = 0; i < n; ++i) {\n            int current_gcd = nums[i];\n\
        \            for (int j = i + 1; j < n; ++j) {\n                current_gcd\
        \ = std::gcd(current_gcd, nums[j]);\n                if (current_gcd == 1) {\n\
        \                    min_len_to_one = std::min(min_len_to_one, j - i + 1);\n\
        \                    break; // Found the shortest subarray starting at i with\
        \ GCD 1\n                }\n            }\n        }\n\n        if (min_len_to_one\
        \ == n + 1) {\n            return -1; // Impossible to make any element 1\n\
        \        }\n\n        // Operations to create one '1': min_len_to_one - 1\n\
        \        // Operations to convert remaining n-1 elements to '1': n - 1\n   \
        \     return (min_len_to_one - 1) + (n - 1);\n    }\n};"
      java: "import java.util.Arrays;\n\nclass Solution {\n    private int gcd(int a,\
        \ int b) {\n        while (b != 0) {\n            int temp = b;\n          \
        \  b = a % b;\n            a = temp;\n        }\n        return a;\n    }\n\n\
        \    public int minOperations(int[] nums) {\n        int n = nums.length;\n\
        \        int countOnes = 0;\n        for (int x : nums) {\n            if (x\
        \ == 1) {\n                countOnes++;\n            }\n        }\n\n      \
        \  if (countOnes > 0) {\n            return n - countOnes;\n        }\n\n  \
        \      // No ones in the array, need to create one.\n        // Find the shortest\
        \ subarray whose GCD is 1.\n        int minLenToOne = n + 1; // Initialize with\
        \ a value larger than any possible length\n\n        for (int i = 0; i < n;\
        \ ++i) {\n            int currentGcd = nums[i];\n            for (int j = i\
        \ + 1; j < n; ++j) {\n                currentGcd = gcd(currentGcd, nums[j]);\n\
        \                if (currentGcd == 1) {\n                    minLenToOne = Math.min(minLenToOne,\
        \ j - i + 1);\n                    break; // Found the shortest subarray starting\
        \ at i with GCD 1\n                }\n            }\n        }\n\n        if\
        \ (minLenToOne == n + 1) {\n            return -1; // Impossible to make any\
        \ element 1\n        }\n\n        // Operations to create one '1': minLenToOne\
        \ - 1\n        // Operations to convert remaining n-1 elements to '1': n - 1\n\
        \        return (minLenToOne - 1) + (n - 1);\n    }\n}"
      python: "import math\n\nclass Solution:\n    def minOperations(self, nums: list[int])\
        \ -> int:\n        n = len(nums)\n        count_ones = nums.count(1)\n\n   \
        \     if count_ones > 0:\n            return n - count_ones\n\n        # No\
        \ ones in the array, need to create one.\n        # Find the shortest subarray\
        \ whose GCD is 1.\n        min_len_to_one = n + 1 # Initialize with a value\
        \ larger than any possible length\n\n        for i in range(n):\n          \
        \  current_gcd = nums[i]\n            for j in range(i + 1, n):\n          \
        \      current_gcd = math.gcd(current_gcd, nums[j])\n                if current_gcd\
        \ == 1:\n                    min_len_to_one = min(min_len_to_one, j - i + 1)\n\
        \                    break # Found the shortest subarray starting at i with\
        \ GCD 1\n\n        if min_len_to_one == n + 1:\n            return -1 # Impossible\
        \ to make any element 1\n\n        # Operations to create one '1': min_len_to_one\
        \ - 1\n        # Operations to convert remaining n-1 elements to '1': n - 1\n\
        \        return (min_len_to_one - 1) + (n - 1)"
      python3: "import math\n\nclass Solution:\n    def minOperations(self, nums: list[int])\
        \ -> int:\n        n = len(nums)\n        count_ones = nums.count(1)\n\n   \
        \     if count_ones > 0:\n            return n - count_ones\n\n        # No\
        \ ones in the array, need to create one.\n        # Find the shortest subarray\
        \ whose GCD is 1.\n        min_len_to_one = n + 1 # Initialize with a value\
        \ larger than any possible length\n\n        for i in range(n):\n          \
        \  current_gcd = nums[i]\n            for j in range(i + 1, n):\n          \
        \      current_gcd = math.gcd(current_gcd, nums[j])\n                if current_gcd\
        \ == 1:\n                    min_len_to_one = min(min_len_to_one, j - i + 1)\n\
        \                    break # Found the shortest subarray starting at i with\
        \ GCD 1\n\n        if min_len_to_one == n + 1:\n            return -1 # Impossible\
        \ to make any element 1\n\n        # Operations to create one '1': min_len_to_one\
        \ - 1\n        # Operations to convert remaining n-1 elements to '1': n - 1\n\
        \        return (min_len_to_one - 1) + (n - 1)"
      c: "#include <stdio.h>\n#include <stdlib.h>\n#include <limits.h>\n\n// Function\
        \ to compute GCD\nint gcd(int a, int b) {\n    while (b != 0) {\n        int\
        \ temp = b;\n        b = a % b;\n        a = temp;\n    }\n    return a;\n}\n\
        \nint minOperations(int* nums, int numsSize) {\n    int n = numsSize;\n    int\
        \ count_ones = 0;\n    for (int i = 0; i < n; ++i) {\n        if (nums[i] ==\
        \ 1) {\n            count_ones++;\n        }\n    }\n\n    if (count_ones >\
        \ 0) {\n        return n - count_ones;\n    }\n\n    // No ones in the array,\
        \ need to create one.\n    // Find the shortest subarray whose GCD is 1.\n \
        \   int min_len_to_one = n + 1; // Initialize with a value larger than any possible\
        \ length\n\n    for (int i = 0; i < n; ++i) {\n        int current_gcd = nums[i];\n\
        \        for (int j = i + 1; j < n; ++j) {\n            current_gcd = gcd(current_gcd,\
        \ nums[j]);\n            if (current_gcd == 1) {\n                min_len_to_one\
        \ = (min_len_to_one < (j - i + 1)) ? min_len_to_one : (j - i + 1);\n       \
        \         break; // Found the shortest subarray starting at i with GCD 1\n \
        \           }\n        }\n    }\n\n    if (min_len_to_one == n + 1) {\n    \
        \    return -1; // Impossible to make any element 1\n    }\n\n    // Operations\
        \ to create one '1': min_len_to_one - 1\n    // Operations to convert remaining\
        \ n-1 elements to '1': n - 1\n    return (min_len_to_one - 1) + (n - 1);\n}"
      csharp: "using System;\nusing System.Linq;\n\npublic class Solution {\n    private\
        \ int Gcd(int a, int b) {\n        while (b != 0) {\n            int temp =\
        \ b;\n            b = a % b;\n            a = temp;\n        }\n        return\
        \ a;\n    }\n\n    public int MinOperations(int[] nums) {\n        int n = nums.Length;\n\
        \        int countOnes = 0;\n        foreach (int x in nums) {\n           \
        \ if (x == 1) {\n                countOnes++;\n            }\n        }\n\n\
        \        if (countOnes > 0) {\n            return n - countOnes;\n        }\n\
        \n        // No ones in the array, need to create one.\n        // Find the\
        \ shortest subarray whose GCD is 1.\n        int minLenToOne = n + 1; // Initialize\
        \ with a value larger than any possible length\n\n        for (int i = 0; i\
        \ < n; ++i) {\n            int currentGcd = nums[i];\n            for (int j\
        \ = i + 1; j < n; ++j) {\n                currentGcd = Gcd(currentGcd, nums[j]);\n\
        \                if (currentGcd == 1) {\n                    minLenToOne = Math.Min(minLenToOne,\
        \ j - i + 1);\n                    break; // Found the shortest subarray starting\
        \ at i with GCD 1\n                }\n            }\n        }\n\n        if\
        \ (minLenToOne == n + 1) {\n            return -1; // Impossible to make any\
        \ element 1\n        }\n\n        // Operations to create one '1': minLenToOne\
        \ - 1\n        // Operations to convert remaining n-1 elements to '1': n - 1\n\
        \        return (minLenToOne - 1) + (n - 1);\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar minOperations\
        \ = function(nums) {\n    const n = nums.length;\n    let countOnes = 0;\n \
        \   for (const x of nums) {\n        if (x === 1) {\n            countOnes++;\n\
        \        }\n    }\n\n    if (countOnes > 0) {\n        return n - countOnes;\n\
        \    }\n\n    // No ones in the array, need to create one.\n    // Find the\
        \ shortest subarray whose GCD is 1.\n    let minLenToOne = n + 1; // Initialize\
        \ with a value larger than any possible length\n\n    const gcd = (a, b) =>\
        \ {\n        while (b !== 0) {\n            let temp = b;\n            b = a\
        \ % b;\n            a = temp;\n        }\n        return a;\n    };\n\n    for\
        \ (let i = 0; i < n; ++i) {\n        let currentGcd = nums[i];\n        for\
        \ (let j = i + 1; j < n; ++j) {\n            currentGcd = gcd(currentGcd, nums[j]);\n\
        \            if (currentGcd === 1) {\n                minLenToOne = Math.min(minLenToOne,\
        \ j - i + 1);\n                break; // Found the shortest subarray starting\
        \ at i with GCD 1\n            }\n        }\n    }\n\n    if (minLenToOne ===\
        \ n + 1) {\n        return -1; // Impossible to make any element 1\n    }\n\n\
        \    // Operations to create one '1': minLenToOne - 1\n    // Operations to\
        \ convert remaining n-1 elements to '1': n - 1\n    return (minLenToOne - 1)\
        \ + (n - 1);\n};"
      typescript: "function minOperations(nums: number[]): number {\n    const n = nums.length;\n\
        \    let countOnes = 0;\n    for (const x of nums) {\n        if (x === 1) {\n\
        \            countOnes++;\n        }\n    }\n\n    if (countOnes > 0) {\n  \
        \      return n - countOnes;\n    }\n\n    // No ones in the array, need to\
        \ create one.\n    // Find the shortest subarray whose GCD is 1.\n    let minLenToOne\
        \ = n + 1; // Initialize with a value larger than any possible length\n\n  \
        \  const gcd = (a: number, b: number): number => {\n        while (b !== 0)\
        \ {\n            let temp = b;\n            b = a % b;\n            a = temp;\n\
        \        }\n        return a;\n    };\n\n    for (let i = 0; i < n; ++i) {\n\
        \        let currentGcd = nums[i];\n        for (let j = i + 1; j < n; ++j)\
        \ {\n            currentGcd = gcd(currentGcd, nums[j]);\n            if (currentGcd\
        \ === 1) {\n                minLenToOne = Math.min(minLenToOne, j - i + 1);\n\
        \                break; // Found the shortest subarray starting at i with GCD\
        \ 1\n            }\n        }\n    }\n\n    if (minLenToOne === n + 1) {\n \
        \       return -1; // Impossible to make any element 1\n    }\n\n    // Operations\
        \ to create one '1': minLenToOne - 1\n    // Operations to convert remaining\
        \ n-1 elements to '1': n - 1\n    return (minLenToOne - 1) + (n - 1);\n}"
      php: "<?php\nclass Solution {\n\n    private function gcd(int $a, int $b): int\
        \ {\n        while ($b !== 0) {\n            $temp = $b;\n            $b = $a\
        \ % $b;\n            $a = $temp;\n        }\n        return $a;\n    }\n\n \
        \   /**\n     * @param int[] $nums\n     * @return int\n     */\n    function\
        \ minOperations(array $nums): int {\n        $n = count($nums);\n        $countOnes\
        \ = 0;\n        foreach ($nums as $x) {\n            if ($x === 1) {\n     \
        \           $countOnes++;\n            }\n        }\n\n        if ($countOnes\
        \ > 0) {\n            return $n - $countOnes;\n        }\n\n        // No ones\
        \ in the array, need to create one.\n        // Find the shortest subarray whose\
        \ GCD is 1.\n        $minLenToOne = $n + 1; // Initialize with a value larger\
        \ than any possible length\n\n        for ($i = 0; $i < $n; ++$i) {\n      \
        \      $currentGcd = $nums[$i];\n            for ($j = $i + 1; $j < $n; ++$j)\
        \ {\n                $currentGcd = $this->gcd($currentGcd, $nums[$j]);\n   \
        \             if ($currentGcd === 1) {\n                    $minLenToOne = min($minLenToOne,\
        \ $j - $i + 1);\n                    break; // Found the shortest subarray starting\
        \ at i with GCD 1\n                }\n            }\n        }\n\n        if\
        \ ($minLenToOne === $n + 1) {\n            return -1; // Impossible to make\
        \ any element 1\n        }\n\n        // Operations to create one '1': minLenToOne\
        \ - 1\n        // Operations to convert remaining n-1 elements to '1': n - 1\n\
        \        return ($minLenToOne - 1) + ($n - 1);\n    }\n}"
      swift: "import Foundation\n\nclass Solution {\n    private func gcd(_ a: Int,\
        \ _ b: Int) -> Int {\n        var a = a\n        var b = b\n        while b\
        \ != 0 {\n            let temp = b\n            b = a % b\n            a = temp\n\
        \        }\n        return a\n    }\n\n    func minOperations(_ nums: [Int])\
        \ -> Int {\n        let n = nums.count\n        var countOnes = 0\n        for\
        \ x in nums {\n            if x == 1 {\n                countOnes += 1\n   \
        \         }\n        }\n\n        if countOnes > 0 {\n            return n -\
        \ countOnes\n        }\n\n        // No ones in the array, need to create one.\n\
        \        // Find the shortest subarray whose GCD is 1.\n        var minLenToOne\
        \ = n + 1 // Initialize with a value larger than any possible length\n\n   \
        \     for i in 0..<n {\n            var currentGcd = nums[i]\n            for\
        \ j in (i + 1)..<n {\n                currentGcd = gcd(currentGcd, nums[j])\n\
        \                if currentGcd == 1 {\n                    minLenToOne = min(minLenToOne,\
        \ j - i + 1)\n                    break // Found the shortest subarray starting\
        \ at i with GCD 1\n                }\n            }\n        }\n\n        if\
        \ minLenToOne == n + 1 {\n            return -1 // Impossible to make any element\
        \ 1\n        }\n\n        // Operations to create one '1': minLenToOne - 1\n\
        \        // Operations to convert remaining n-1 elements to '1': n - 1\n   \
        \     return (minLenToOne - 1) + (n - 1)\n    }\n}"
      kotlin: "import kotlin.math.min\n\nclass Solution {\n    private fun gcd(a: Int,\
        \ b: Int): Int {\n        var num1 = a\n        var num2 = b\n        while\
        \ (num2 != 0) {\n            val temp = num2\n            num2 = num1 % num2\n\
        \            num1 = temp\n        }\n        return num1\n    }\n\n    fun minOperations(nums:\
        \ IntArray): Int {\n        val n = nums.size\n        var countOnes = 0\n \
        \       for (x in nums) {\n            if (x == 1) {\n                countOnes++\n\
        \            }\n        }\n\n        if (countOnes > 0) {\n            return\
        \ n - countOnes\n        }\n\n        // No ones in the array, need to create\
        \ one.\n        // Find the shortest subarray whose GCD is 1.\n        var minLenToOne\
        \ = n + 1 // Initialize with a value larger than any possible length\n\n   \
        \     for (i in 0 until n) {\n            var currentGcd = nums[i]\n       \
        \     for (j in i + 1 until n) {\n                currentGcd = gcd(currentGcd,\
        \ nums[j])\n                if (currentGcd == 1) {\n                    minLenToOne\
        \ = min(minLenToOne, j - i + 1)\n                    break // Found the shortest\
        \ subarray starting at i with GCD 1\n                }\n            }\n    \
        \    }\n\n        if (minLenToOne == n + 1) {\n            return -1 // Impossible\
        \ to make any element 1\n        }\n\n        // Operations to create one '1':\
        \ minLenToOne - 1\n        // Operations to convert remaining n-1 elements to\
        \ '1': n - 1\n        return (minLenToOne - 1) + (n - 1)\n    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int _gcd(int a, int b) {\n \
        \   while (b != 0) {\n      int temp = b;\n      b = a % b;\n      a = temp;\n\
        \    }\n    return a;\n  }\n\n  int minOperations(List<int> nums) {\n    final\
        \ n = nums.length;\n    int countOnes = 0;\n    for (final x in nums) {\n  \
        \    if (x == 1) {\n        countOnes++;\n      }\n    }\n\n    if (countOnes\
        \ > 0) {\n      return n - countOnes;\n    }\n\n    // No ones in the array,\
        \ need to create one.\n    // Find the shortest subarray whose GCD is 1.\n \
        \   int minLenToOne = n + 1; // Initialize with a value larger than any possible\
        \ length\n\n    for (int i = 0; i < n; ++i) {\n      int currentGcd = nums[i];\n\
        \      for (int j = i + 1; j < n; ++j) {\n        currentGcd = _gcd(currentGcd,\
        \ nums[j]);\n        if (currentGcd == 1) {\n          minLenToOne = min(minLenToOne,\
        \ j - i + 1);\n          break; // Found the shortest subarray starting at i\
        \ with GCD 1\n        }\n      }\n    }\n\n    if (minLenToOne == n + 1) {\n\
        \      return -1; // Impossible to make any element 1\n    }\n\n    // Operations\
        \ to create one '1': minLenToOne - 1\n    // Operations to convert remaining\
        \ n-1 elements to '1': n - 1\n    return (minLenToOne - 1) + (n - 1);\n  }\n\
        }"
      go: "package main\n\nimport (\n\t\"math\"\n)\n\nfunc gcd(a, b int) int {\n\tfor\
        \ b != 0 {\n\t\ta, b = b, a%b\n\t}\n\treturn a\n}\n\nfunc minOperations(nums\
        \ []int) int {\n\tn := len(nums)\n\tcountOnes := 0\n\tfor _, x := range nums\
        \ {\n\t\tif x == 1 {\n\t\t\tcountOnes++\n\t\t}\n\t}\n\n\tif countOnes > 0 {\n\
        \t\treturn n - countOnes\n\t}\n\n\t// No ones in the array, need to create one.\n\
        \t// Find the shortest subarray whose GCD is 1.\n\tminLenToOne := n + 1 // Initialize\
        \ with a value larger than any possible length\n\n\tfor i := 0; i < n; i++ {\n\
        \t\tcurrentGcd := nums[i]\n\t\tfor j := i + 1; j < n; j++ {\n\t\t\tcurrentGcd\
        \ = gcd(currentGcd, nums[j])\n\t\t\tif currentGcd == 1 {\n\t\t\t\tminLenToOne\
        \ = int(math.Min(float64(minLenToOne), float64(j-i+1)))\n\t\t\t\tbreak // Found\
        \ the shortest subarray starting at i with GCD 1\n\t\t\t}\n\t\t}\n\t}\n\n\t\
        if minLenToOne == n + 1 {\n\t\treturn -1 // Impossible to make any element 1\n\
        \t}\n\n\t// Operations to create one '1': minLenToOne - 1\n\t// Operations to\
        \ convert remaining n-1 elements to '1': n - 1\n\treturn (minLenToOne - 1) +\
        \ (n - 1)\n}"
      ruby: "def gcd(a, b)\n  while b != 0\n    a, b = b, a % b\n  end\n  a\nend\n\n\
        # @param {Integer[]} nums\n# @return {Integer}\ndef min_operations(nums)\n \
        \ n = nums.length\n  count_ones = nums.count(1)\n\n  if count_ones > 0\n   \
        \ return n - count_ones\n  end\n\n  # No ones in the array, need to create one.\n\
        \  # Find the shortest subarray whose GCD is 1.\n  min_len_to_one = n + 1 #\
        \ Initialize with a value larger than any possible length\n\n  (0...n).each\
        \ do |i|\n    current_gcd = nums[i]\n    (i + 1...n).each do |j|\n      current_gcd\
        \ = gcd(current_gcd, nums[j])\n      if current_gcd == 1\n        min_len_to_one\
        \ = [min_len_to_one, j - i + 1].min\n        break # Found the shortest subarray\
        \ starting at i with GCD 1\n      end\n    end\n  end\n\n  if min_len_to_one\
        \ == n + 1\n    return -1 # Impossible to make any element 1\n  end\n\n  # Operations\
        \ to create one '1': min_len_to_one - 1\n  # Operations to convert remaining\
        \ n-1 elements to '1': n - 1\n  (min_len_to_one - 1) + (n - 1)\nend"
      scala: "import scala.annotation.tailrec\nimport scala.math.min\n\nobject Solution\
        \ {\n    @tailrec\n    private def gcd(a: Int, b: Int): Int = {\n        if\
        \ (b == 0) a\n        else gcd(b, a % b)\n    }\n\n    def minOperations(nums:\
        \ Array[Int]): Int = {\n        val n = nums.length\n        val countOnes =\
        \ nums.count(_ == 1)\n\n        if (countOnes > 0) {\n            return n -\
        \ countOnes\n        }\n\n        // No ones in the array, need to create one.\n\
        \        // Find the shortest subarray whose GCD is 1.\n        var minLenToOne\
        \ = n + 1 // Initialize with a value larger than any possible length\n\n   \
        \     for (i <- 0 until n) {\n            var currentGcd = nums(i)\n       \
        \     for (j <- i + 1 until n) {\n                currentGcd = gcd(currentGcd,\
        \ nums(j))\n                if (currentGcd == 1) {\n                    minLenToOne\
        \ = min(minLenToOne, j - i + 1)\n                    break // Found the shortest\
        \ subarray starting at i with GCD 1\n                }\n            }\n    \
        \    }\n\n        if (minLenToOne == n + 1) {\n            return -1 // Impossible\
        \ to make any element 1\n        }\n\n        // Operations to create one '1':\
        \ minLenToOne - 1\n        // Operations to convert remaining n-1 elements to\
        \ '1': n - 1\n        (minLenToOne - 1) + (n - 1)\n    }\n}"
      rust: "impl Solution {\n    fn gcd(mut a: i32, mut b: i32) -> i32 {\n        while\
        \ b != 0 {\n            let temp = b;\n            b = a % b;\n            a\
        \ = temp;\n        }\n        a\n    }\n\n    pub fn min_operations(nums: Vec<i32>)\
        \ -> i32 {\n        let n = nums.len() as i32;\n        let mut count_ones =\
        \ 0;\n        for &x in nums.iter() {\n            if x == 1 {\n           \
        \     count_ones += 1;\n            }\n        }\n\n        if count_ones >\
        \ 0 {\n            return n - count_ones;\n        }\n\n        // No ones in\
        \ the array, need to create one.\n        // Find the shortest subarray whose\
        \ GCD is 1.\n        let mut min_len_to_one = n + 1; // Initialize with a value\
        \ larger than any possible length\n\n        for i in 0..n as usize {\n    \
        \        let mut current_gcd = nums[i];\n            for j in (i + 1)..n as\
        \ usize {\n                current_gcd = Self::gcd(current_gcd, nums[j]);\n\
        \                if current_gcd == 1 {\n                    min_len_to_one =\
        \ min_len_to_one.min((j - i + 1) as i32);\n                    break; // Found\
        \ the shortest subarray starting at i with GCD 1\n                }\n      \
        \      }\n        }\n\n        if min_len_to_one == n + 1 {\n            return\
        \ -1; // Impossible to make any element 1\n        }\n\n        // Operations\
        \ to create one '1': min_len_to_one - 1\n        // Operations to convert remaining\
        \ n-1 elements to '1': n - 1\n        (min_len_to_one - 1) + (n - 1)\n    }\n\
        }"
      racket: "#lang racket\n\n(define (gcd a b)\n  (if (= b 0)\n      a\n      (gcd\
        \ b (modulo a b))))\n\n(define/public (min-operations nums)\n  (define n (vector-length\
        \ nums))\n  (define count-ones (for/sum ([x (in-vector nums)]) (if (= x 1) 1\
        \ 0)))\n\n  (when (> count-ones 0)\n    (return (- n count-ones)))\n\n  ;; No\
        \ ones in the array, need to create one.\n  ;; Find the shortest subarray whose\
        \ GCD is 1.\n  (define min-len-to-one (+ n 1)) ; Initialize with a value larger\
        \ than any possible length\n\n  (for ([i (in-range n)])\n    (define current-gcd\
        \ (vector-ref nums i))\n    (for ([j (in-range (+ i 1) n)])\n      (set! current-gcd\
        \ (gcd current-gcd (vector-ref nums j)))\n      (when (= current-gcd 1)\n  \
        \      (set! min-len-to-one (min min-len-to-one (+ (- j i) 1)))\n        (break)\
        \ ; Found the shortest subarray starting at i with GCD 1\n        )))\n\n  (if\
        \ (= min-len-to-one (+ n 1))\n      -1 ; Impossible to make any element 1\n\
        \      ;; Operations to create one '1': min-len-to-one - 1\n      ;; Operations\
        \ to convert remaining n-1 elements to '1': n - 1\n      (+ (- min-len-to-one\
        \ 1) (- n 1))))"
      erlang: "-module(solution).\n-export([min_operations/1]).\n\n%% Function to compute\
        \ GCD\ngcd(A, 0) -> A;\ngcd(A, B) -> gcd(B, A rem B).\n\n-spec min_operations(Nums\
        \ :: [integer()]) -> integer().\nmin_operations(Nums) ->\n    N = length(Nums),\n\
        \    CountOnes = lists:foldl(fun(X, Acc) -> if X == 1 -> Acc + 1; true -> Acc\
        \ end end, 0, Nums),\n\n    if CountOnes > 0 ->\n        N - CountOnes;\n  \
        \  true ->\n        %% No ones in the array, need to create one.\n        %%\
        \ Find the shortest subarray whose GCD is 1.\n        MinLenToOne = find_min_len_to_one(Nums,\
        \ N),\n\n        if MinLenToOne == N + 1 ->\n            -1; %% Impossible to\
        \ make any element 1\n        true ->\n            %% Operations to create one\
        \ '1': MinLenToOne - 1\n            %% Operations to convert remaining N-1 elements\
        \ to '1': N - 1\n            (MinLenToOne - 1) + (N - 1)\n        end\n    end.\n\
        \nfind_min_len_to_one(Nums, N) ->\n    lists:foldl(fun(I, AccMinLen) ->\n  \
        \      CurrentGcd = lists:nth(I + 1, Nums),\n        {NewMinLen, _} = lists:foldl(fun(J,\
        \ {CurrentMinLen, CurrentGcdAcc}) ->\n            NextGcd = gcd(CurrentGcdAcc,\
        \ lists:nth(J + 1, Nums)),\n            if NextGcd == 1 ->\n               \
        \ {min(CurrentMinLen, J - I + 1), NextGcd};\n            true ->\n         \
        \       {CurrentMinLen, NextGcd}\n            end\n        end, {AccMinLen,\
        \ CurrentGcd}, lists:seq(I + 1, N - 1)),\n        NewMinLen\n    end, N + 1,\
        \ lists:seq(0, N - 1))."
      elixir: "defmodule Solution do\n  @spec min_operations(nums :: [integer()]) ::\
        \ integer()\n  def min_operations(nums) do\n    n = length(nums)\n    count_ones\
        \ = Enum.count(nums, fn x -> x == 1 end)\n\n    if count_ones > 0 do\n     \
        \ n - count_ones\n    else\n      # No ones in the array, need to create one.\n\
        \      # Find the shortest subarray whose GCD is 1.\n      min_len_to_one =\
        \ find_min_len_to_one(nums, n)\n\n      if min_len_to_one == n + 1 do\n    \
        \    -1 # Impossible to make any element 1\n      else\n        # Operations\
        \ to create one '1': min_len_to_one - 1\n        # Operations to convert remaining\
        \ n-1 elements to '1': n - 1\n        (min_len_to_one - 1) + (n - 1)\n     \
        \ end\n    end\n  end\n\n  defp find_min_len_to_one(nums, n) do\n    0..(n -\
        \ 1)\n    |> Enum.reduce(n + 1, fn i, acc_min_len ->\n      current_gcd = Enum.at(nums,\
        \ i)\n      {new_min_len, _} = (i + 1)..(n - 1)\n      |> Enum.reduce({acc_min_len,\
        \ current_gcd}, fn j, {current_min_len, current_gcd_acc} ->\n        next_gcd\
        \ = gcd(current_gcd_acc, Enum.at(nums, j))\n        if next_gcd == 1 do\n  \
        \        {min(current_min_len, j - i + 1), next_gcd}\n        else\n       \
        \   {current_min_len, next_gcd}\n        end\n      end)\n      new_min_len\n\
        \    end)\n  end\n\n  defp gcd(a, 0), do: a\n  defp gcd(a, b), do: gcd(b, rem(a,\
        \ b))\nend"
    approach: The problem asks for the minimum number of operations to make all elements
      in an array equal to 1. An operation involves replacing an element with the GCD
      of itself and an adjacent element. The key insight is that if the array already
      contains at least one '1', then all other elements can be converted to '1' in
      a single operation each by taking their GCD with an adjacent '1'. For example,
      if `nums[k] = 1`, then `nums[k-1]` can become `gcd(nums[k-1], nums[k]) = gcd(nums[k-1],
      1) = 1` in one operation. Thus, if there are `count_ones` ones initially, we need
      `n - count_ones` operations to convert the remaining elements.
    time_complexity: The time complexity is O(N^2 * log(max_val)). In the worst case,
      we iterate through all possible subarrays (N^2 subarrays). For each subarray,
      we compute its GCD, which involves N GCD operations. Each GCD operation takes
      O(log(max_val)) time, where max_val is the maximum value in `nums`. Since N is
      small (up to 50), N^2 is 2500, and log(10^6) is about 20, this complexity is well
      within limits.
    space_complexity: The space complexity is O(1) as we only use a few variables to
      store counts, minimum length, and current GCD during the iteration. No auxiliary
      data structures that scale with input size are used.
    elapsed_time: 46.570815563201904
    model: gemini-2.5-flash
    generated_at: '2025-11-25 00:11:45 '
  - solutions:
      cpp: '// Generation failed for C++

        // Reason: HTTP Error 429'
      java: '// Generation failed for Java

        // Reason: HTTP Error 429'
      python: '// Generation failed for Python

        // Reason: HTTP Error 429'
      python3: '// Generation failed for Python3

        // Reason: HTTP Error 429'
      c: '// Generation failed for C

        // Reason: HTTP Error 429'
      csharp: '// Generation failed for C#

        // Reason: HTTP Error 429'
      javascript: '// Generation failed for JavaScript

        // Reason: HTTP Error 429'
      typescript: '// Generation failed for TypeScript

        // Reason: HTTP Error 429'
      php: '// Generation failed for PHP

        // Reason: HTTP Error 429'
      swift: '// Generation failed for Swift

        // Reason: HTTP Error 429'
      kotlin: '// Generation failed for Kotlin

        // Reason: HTTP Error 429'
      dart: '// Generation failed for Dart

        // Reason: HTTP Error 429'
      go: '// Generation failed for Go

        // Reason: HTTP Error 429'
      ruby: '// Generation failed for Ruby

        // Reason: HTTP Error 429'
      scala: '// Generation failed for Scala

        // Reason: HTTP Error 429'
      rust: '// Generation failed for Rust

        // Reason: HTTP Error 429'
      racket: '// Generation failed for Racket

        // Reason: HTTP Error 429'
      erlang: '// Generation failed for Erlang

        // Reason: HTTP Error 429'
      elixir: '// Generation failed for Elixir

        // Reason: HTTP Error 429'
    elapsed_time: 0.5985558032989502
    model: llama-3.3-70b-versatile
    generated_at: '2025-11-25 00:11:46 '
---

## Problem #2654: Minimum Number of Operations to Make All Array Elements Equal to 1

**Difficulty:** Medium

**Topics:** Array, Math, Number Theory

## Problem Description

<p>You are given a <strong>0-indexed</strong>&nbsp;array <code>nums</code> consisting of <strong>positive</strong> integers. You can do the following operation on the array <strong>any</strong> number of times:</p>

<ul>
	<li>Select an index <code>i</code> such that <code>0 &lt;= i &lt; n - 1</code> and replace either of&nbsp;<code>nums[i]</code> or <code>nums[i+1]</code> with their gcd value.</li>
</ul>

<p>Return <em>the <strong>minimum</strong> number of operations to make all elements of </em><code>nums</code><em> equal to </em><code>1</code>. If it is impossible, return <code>-1</code>.</p>

<p>The gcd of two integers is the greatest common divisor of the two integers.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,6,3,4]
<strong>Output:</strong> 4
<strong>Explanation:</strong> We can do the following operations:
- Choose index i = 2 and replace nums[2] with gcd(3,4) = 1. Now we have nums = [2,6,1,4].
- Choose index i = 1 and replace nums[1] with gcd(6,1) = 1. Now we have nums = [2,1,1,4].
- Choose index i = 0 and replace nums[0] with gcd(2,1) = 1. Now we have nums = [1,1,1,4].
- Choose index i = 2 and replace nums[3] with gcd(1,4) = 1. Now we have nums = [1,1,1,1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,10,6,14]
<strong>Output:</strong> -1
<strong>Explanation:</strong> It can be shown that it is impossible to make all the elements equal to 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## Hints

1. Note that if you have at least one occurrence of 1 in the array, then you can make all the other elements equal to 1 with one operation each.

2. Try finding the shortest subarray with a gcd equal to 1.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-11-25 00:11:45 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks for the minimum number of operations to make all elements in an array equal to 1. An operation involves replacing an element with the GCD of itself and an adjacent element. The key insight is that if the array already contains at least one '1', then all other elements can be converted to '1' in a single operation each by taking their GCD with an adjacent '1'. For example, if `nums[k] = 1`, then `nums[k-1]` can become `gcd(nums[k-1], nums[k]) = gcd(nums[k-1], 1) = 1` in one operation. Thus, if there are `count_ones` ones initially, we need `n - count_ones` operations to convert the remaining elements.

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
#include <numeric>
#include <algorithm>

class Solution {
public:
    int minOperations(std::vector<int>& nums) {
        int n = nums.size();
        int count_ones = 0;
        for (int x : nums) {
            if (x == 1) {
                count_ones++;
            }
        }

        if (count_ones > 0) {
            return n - count_ones;
        }

        // No ones in the array, need to create one.
        // Find the shortest subarray whose GCD is 1.
        int min_len_to_one = n + 1; // Initialize with a value larger than any possible length

        for (int i = 0; i < n; ++i) {
            int current_gcd = nums[i];
            for (int j = i + 1; j < n; ++j) {
                current_gcd = std::gcd(current_gcd, nums[j]);
                if (current_gcd == 1) {
                    min_len_to_one = std::min(min_len_to_one, j - i + 1);
                    break; // Found the shortest subarray starting at i with GCD 1
                }
            }
        }

        if (min_len_to_one == n + 1) {
            return -1; // Impossible to make any element 1
        }

        // Operations to create one '1': min_len_to_one - 1
        // Operations to convert remaining n-1 elements to '1': n - 1
        return (min_len_to_one - 1) + (n - 1);
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
    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public int minOperations(int[] nums) {
        int n = nums.length;
        int countOnes = 0;
        for (int x : nums) {
            if (x == 1) {
                countOnes++;
            }
        }

        if (countOnes > 0) {
            return n - countOnes;
        }

        // No ones in the array, need to create one.
        // Find the shortest subarray whose GCD is 1.
        int minLenToOne = n + 1; // Initialize with a value larger than any possible length

        for (int i = 0; i < n; ++i) {
            int currentGcd = nums[i];
            for (int j = i + 1; j < n; ++j) {
                currentGcd = gcd(currentGcd, nums[j]);
                if (currentGcd == 1) {
                    minLenToOne = Math.min(minLenToOne, j - i + 1);
                    break; // Found the shortest subarray starting at i with GCD 1
                }
            }
        }

        if (minLenToOne == n + 1) {
            return -1; // Impossible to make any element 1
        }

        // Operations to create one '1': minLenToOne - 1
        // Operations to convert remaining n-1 elements to '1': n - 1
        return (minLenToOne - 1) + (n - 1);
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
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        count_ones = nums.count(1)

        if count_ones > 0:
            return n - count_ones

        # No ones in the array, need to create one.
        # Find the shortest subarray whose GCD is 1.
        min_len_to_one = n + 1 # Initialize with a value larger than any possible length

        for i in range(n):
            current_gcd = nums[i]
            for j in range(i + 1, n):
                current_gcd = math.gcd(current_gcd, nums[j])
                if current_gcd == 1:
                    min_len_to_one = min(min_len_to_one, j - i + 1)
                    break # Found the shortest subarray starting at i with GCD 1

        if min_len_to_one == n + 1:
            return -1 # Impossible to make any element 1

        # Operations to create one '1': min_len_to_one - 1
        # Operations to convert remaining n-1 elements to '1': n - 1
        return (min_len_to_one - 1) + (n - 1)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import math

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        count_ones = nums.count(1)

        if count_ones > 0:
            return n - count_ones

        # No ones in the array, need to create one.
        # Find the shortest subarray whose GCD is 1.
        min_len_to_one = n + 1 # Initialize with a value larger than any possible length

        for i in range(n):
            current_gcd = nums[i]
            for j in range(i + 1, n):
                current_gcd = math.gcd(current_gcd, nums[j])
                if current_gcd == 1:
                    min_len_to_one = min(min_len_to_one, j - i + 1)
                    break # Found the shortest subarray starting at i with GCD 1

        if min_len_to_one == n + 1:
            return -1 # Impossible to make any element 1

        # Operations to create one '1': min_len_to_one - 1
        # Operations to convert remaining n-1 elements to '1': n - 1
        return (min_len_to_one - 1) + (n - 1)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

// Function to compute GCD
int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int minOperations(int* nums, int numsSize) {
    int n = numsSize;
    int count_ones = 0;
    for (int i = 0; i < n; ++i) {
        if (nums[i] == 1) {
            count_ones++;
        }
    }

    if (count_ones > 0) {
        return n - count_ones;
    }

    // No ones in the array, need to create one.
    // Find the shortest subarray whose GCD is 1.
    int min_len_to_one = n + 1; // Initialize with a value larger than any possible length

    for (int i = 0; i < n; ++i) {
        int current_gcd = nums[i];
        for (int j = i + 1; j < n; ++j) {
            current_gcd = gcd(current_gcd, nums[j]);
            if (current_gcd == 1) {
                min_len_to_one = (min_len_to_one < (j - i + 1)) ? min_len_to_one : (j - i + 1);
                break; // Found the shortest subarray starting at i with GCD 1
            }
        }
    }

    if (min_len_to_one == n + 1) {
        return -1; // Impossible to make any element 1
    }

    // Operations to create one '1': min_len_to_one - 1
    // Operations to convert remaining n-1 elements to '1': n - 1
    return (min_len_to_one - 1) + (n - 1);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Linq;

public class Solution {
    private int Gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public int MinOperations(int[] nums) {
        int n = nums.Length;
        int countOnes = 0;
        foreach (int x in nums) {
            if (x == 1) {
                countOnes++;
            }
        }

        if (countOnes > 0) {
            return n - countOnes;
        }

        // No ones in the array, need to create one.
        // Find the shortest subarray whose GCD is 1.
        int minLenToOne = n + 1; // Initialize with a value larger than any possible length

        for (int i = 0; i < n; ++i) {
            int currentGcd = nums[i];
            for (int j = i + 1; j < n; ++j) {
                currentGcd = Gcd(currentGcd, nums[j]);
                if (currentGcd == 1) {
                    minLenToOne = Math.Min(minLenToOne, j - i + 1);
                    break; // Found the shortest subarray starting at i with GCD 1
                }
            }
        }

        if (minLenToOne == n + 1) {
            return -1; // Impossible to make any element 1
        }

        // Operations to create one '1': minLenToOne - 1
        // Operations to convert remaining n-1 elements to '1': n - 1
        return (minLenToOne - 1) + (n - 1);
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
var minOperations = function(nums) {
    const n = nums.length;
    let countOnes = 0;
    for (const x of nums) {
        if (x === 1) {
            countOnes++;
        }
    }

    if (countOnes > 0) {
        return n - countOnes;
    }

    // No ones in the array, need to create one.
    // Find the shortest subarray whose GCD is 1.
    let minLenToOne = n + 1; // Initialize with a value larger than any possible length

    const gcd = (a, b) => {
        while (b !== 0) {
            let temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    };

    for (let i = 0; i < n; ++i) {
        let currentGcd = nums[i];
        for (let j = i + 1; j < n; ++j) {
            currentGcd = gcd(currentGcd, nums[j]);
            if (currentGcd === 1) {
                minLenToOne = Math.min(minLenToOne, j - i + 1);
                break; // Found the shortest subarray starting at i with GCD 1
            }
        }
    }

    if (minLenToOne === n + 1) {
        return -1; // Impossible to make any element 1
    }

    // Operations to create one '1': minLenToOne - 1
    // Operations to convert remaining n-1 elements to '1': n - 1
    return (minLenToOne - 1) + (n - 1);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minOperations(nums: number[]): number {
    const n = nums.length;
    let countOnes = 0;
    for (const x of nums) {
        if (x === 1) {
            countOnes++;
        }
    }

    if (countOnes > 0) {
        return n - countOnes;
    }

    // No ones in the array, need to create one.
    // Find the shortest subarray whose GCD is 1.
    let minLenToOne = n + 1; // Initialize with a value larger than any possible length

    const gcd = (a: number, b: number): number => {
        while (b !== 0) {
            let temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    };

    for (let i = 0; i < n; ++i) {
        let currentGcd = nums[i];
        for (let j = i + 1; j < n; ++j) {
            currentGcd = gcd(currentGcd, nums[j]);
            if (currentGcd === 1) {
                minLenToOne = Math.min(minLenToOne, j - i + 1);
                break; // Found the shortest subarray starting at i with GCD 1
            }
        }
    }

    if (minLenToOne === n + 1) {
        return -1; // Impossible to make any element 1
    }

    // Operations to create one '1': minLenToOne - 1
    // Operations to convert remaining n-1 elements to '1': n - 1
    return (minLenToOne - 1) + (n - 1);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php
class Solution {

    private function gcd(int $a, int $b): int {
        while ($b !== 0) {
            $temp = $b;
            $b = $a % $b;
            $a = $temp;
        }
        return $a;
    }

    /**
     * @param int[] $nums
     * @return int
     */
    function minOperations(array $nums): int {
        $n = count($nums);
        $countOnes = 0;
        foreach ($nums as $x) {
            if ($x === 1) {
                $countOnes++;
            }
        }

        if ($countOnes > 0) {
            return $n - $countOnes;
        }

        // No ones in the array, need to create one.
        // Find the shortest subarray whose GCD is 1.
        $minLenToOne = $n + 1; // Initialize with a value larger than any possible length

        for ($i = 0; $i < $n; ++$i) {
            $currentGcd = $nums[$i];
            for ($j = $i + 1; $j < $n; ++$j) {
                $currentGcd = $this->gcd($currentGcd, $nums[$j]);
                if ($currentGcd === 1) {
                    $minLenToOne = min($minLenToOne, $j - $i + 1);
                    break; // Found the shortest subarray starting at i with GCD 1
                }
            }
        }

        if ($minLenToOne === $n + 1) {
            return -1; // Impossible to make any element 1
        }

        // Operations to create one '1': minLenToOne - 1
        // Operations to convert remaining n-1 elements to '1': n - 1
        return ($minLenToOne - 1) + ($n - 1);
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
    private func gcd(_ a: Int, _ b: Int) -> Int {
        var a = a
        var b = b
        while b != 0 {
            let temp = b
            b = a % b
            a = temp
        }
        return a
    }

    func minOperations(_ nums: [Int]) -> Int {
        let n = nums.count
        var countOnes = 0
        for x in nums {
            if x == 1 {
                countOnes += 1
            }
        }

        if countOnes > 0 {
            return n - countOnes
        }

        // No ones in the array, need to create one.
        // Find the shortest subarray whose GCD is 1.
        var minLenToOne = n + 1 // Initialize with a value larger than any possible length

        for i in 0..<n {
            var currentGcd = nums[i]
            for j in (i + 1)..<n {
                currentGcd = gcd(currentGcd, nums[j])
                if currentGcd == 1 {
                    minLenToOne = min(minLenToOne, j - i + 1)
                    break // Found the shortest subarray starting at i with GCD 1
                }
            }
        }

        if minLenToOne == n + 1 {
            return -1 // Impossible to make any element 1
        }

        // Operations to create one '1': minLenToOne - 1
        // Operations to convert remaining n-1 elements to '1': n - 1
        return (minLenToOne - 1) + (n - 1)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import kotlin.math.min

class Solution {
    private fun gcd(a: Int, b: Int): Int {
        var num1 = a
        var num2 = b
        while (num2 != 0) {
            val temp = num2
            num2 = num1 % num2
            num1 = temp
        }
        return num1
    }

    fun minOperations(nums: IntArray): Int {
        val n = nums.size
        var countOnes = 0
        for (x in nums) {
            if (x == 1) {
                countOnes++
            }
        }

        if (countOnes > 0) {
            return n - countOnes
        }

        // No ones in the array, need to create one.
        // Find the shortest subarray whose GCD is 1.
        var minLenToOne = n + 1 // Initialize with a value larger than any possible length

        for (i in 0 until n) {
            var currentGcd = nums[i]
            for (j in i + 1 until n) {
                currentGcd = gcd(currentGcd, nums[j])
                if (currentGcd == 1) {
                    minLenToOne = min(minLenToOne, j - i + 1)
                    break // Found the shortest subarray starting at i with GCD 1
                }
            }
        }

        if (minLenToOne == n + 1) {
            return -1 // Impossible to make any element 1
        }

        // Operations to create one '1': minLenToOne - 1
        // Operations to convert remaining n-1 elements to '1': n - 1
        return (minLenToOne - 1) + (n - 1)
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
  int _gcd(int a, int b) {
    while (b != 0) {
      int temp = b;
      b = a % b;
      a = temp;
    }
    return a;
  }

  int minOperations(List<int> nums) {
    final n = nums.length;
    int countOnes = 0;
    for (final x in nums) {
      if (x == 1) {
        countOnes++;
      }
    }

    if (countOnes > 0) {
      return n - countOnes;
    }

    // No ones in the array, need to create one.
    // Find the shortest subarray whose GCD is 1.
    int minLenToOne = n + 1; // Initialize with a value larger than any possible length

    for (int i = 0; i < n; ++i) {
      int currentGcd = nums[i];
      for (int j = i + 1; j < n; ++j) {
        currentGcd = _gcd(currentGcd, nums[j]);
        if (currentGcd == 1) {
          minLenToOne = min(minLenToOne, j - i + 1);
          break; // Found the shortest subarray starting at i with GCD 1
        }
      }
    }

    if (minLenToOne == n + 1) {
      return -1; // Impossible to make any element 1
    }

    // Operations to create one '1': minLenToOne - 1
    // Operations to convert remaining n-1 elements to '1': n - 1
    return (minLenToOne - 1) + (n - 1);
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

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func minOperations(nums []int) int {
	n := len(nums)
	countOnes := 0
	for _, x := range nums {
		if x == 1 {
			countOnes++
		}
	}

	if countOnes > 0 {
		return n - countOnes
	}

	// No ones in the array, need to create one.
	// Find the shortest subarray whose GCD is 1.
	minLenToOne := n + 1 // Initialize with a value larger than any possible length

	for i := 0; i < n; i++ {
		currentGcd := nums[i]
		for j := i + 1; j < n; j++ {
			currentGcd = gcd(currentGcd, nums[j])
			if currentGcd == 1 {
				minLenToOne = int(math.Min(float64(minLenToOne), float64(j-i+1)))
				break // Found the shortest subarray starting at i with GCD 1
			}
		}
	}

	if minLenToOne == n + 1 {
		return -1 // Impossible to make any element 1
	}

	// Operations to create one '1': minLenToOne - 1
	// Operations to convert remaining n-1 elements to '1': n - 1
	return (minLenToOne - 1) + (n - 1)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def gcd(a, b)
  while b != 0
    a, b = b, a % b
  end
  a
end

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  n = nums.length
  count_ones = nums.count(1)

  if count_ones > 0
    return n - count_ones
  end

  # No ones in the array, need to create one.
  # Find the shortest subarray whose GCD is 1.
  min_len_to_one = n + 1 # Initialize with a value larger than any possible length

  (0...n).each do |i|
    current_gcd = nums[i]
    (i + 1...n).each do |j|
      current_gcd = gcd(current_gcd, nums[j])
      if current_gcd == 1
        min_len_to_one = [min_len_to_one, j - i + 1].min
        break # Found the shortest subarray starting at i with GCD 1
      end
    end
  end

  if min_len_to_one == n + 1
    return -1 # Impossible to make any element 1
  end

  # Operations to create one '1': min_len_to_one - 1
  # Operations to convert remaining n-1 elements to '1': n - 1
  (min_len_to_one - 1) + (n - 1)
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.annotation.tailrec
import scala.math.min

object Solution {
    @tailrec
    private def gcd(a: Int, b: Int): Int = {
        if (b == 0) a
        else gcd(b, a % b)
    }

    def minOperations(nums: Array[Int]): Int = {
        val n = nums.length
        val countOnes = nums.count(_ == 1)

        if (countOnes > 0) {
            return n - countOnes
        }

        // No ones in the array, need to create one.
        // Find the shortest subarray whose GCD is 1.
        var minLenToOne = n + 1 // Initialize with a value larger than any possible length

        for (i <- 0 until n) {
            var currentGcd = nums(i)
            for (j <- i + 1 until n) {
                currentGcd = gcd(currentGcd, nums(j))
                if (currentGcd == 1) {
                    minLenToOne = min(minLenToOne, j - i + 1)
                    break // Found the shortest subarray starting at i with GCD 1
                }
            }
        }

        if (minLenToOne == n + 1) {
            return -1 // Impossible to make any element 1
        }

        // Operations to create one '1': minLenToOne - 1
        // Operations to convert remaining n-1 elements to '1': n - 1
        (minLenToOne - 1) + (n - 1)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    fn gcd(mut a: i32, mut b: i32) -> i32 {
        while b != 0 {
            let temp = b;
            b = a % b;
            a = temp;
        }
        a
    }

    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let n = nums.len() as i32;
        let mut count_ones = 0;
        for &x in nums.iter() {
            if x == 1 {
                count_ones += 1;
            }
        }

        if count_ones > 0 {
            return n - count_ones;
        }

        // No ones in the array, need to create one.
        // Find the shortest subarray whose GCD is 1.
        let mut min_len_to_one = n + 1; // Initialize with a value larger than any possible length

        for i in 0..n as usize {
            let mut current_gcd = nums[i];
            for j in (i + 1)..n as usize {
                current_gcd = Self::gcd(current_gcd, nums[j]);
                if current_gcd == 1 {
                    min_len_to_one = min_len_to_one.min((j - i + 1) as i32);
                    break; // Found the shortest subarray starting at i with GCD 1
                }
            }
        }

        if min_len_to_one == n + 1 {
            return -1; // Impossible to make any element 1
        }

        // Operations to create one '1': min_len_to_one - 1
        // Operations to convert remaining n-1 elements to '1': n - 1
        (min_len_to_one - 1) + (n - 1)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (gcd a b)
  (if (= b 0)
      a
      (gcd b (modulo a b))))

(define/public (min-operations nums)
  (define n (vector-length nums))
  (define count-ones (for/sum ([x (in-vector nums)]) (if (= x 1) 1 0)))

  (when (> count-ones 0)
    (return (- n count-ones)))

  ;; No ones in the array, need to create one.
  ;; Find the shortest subarray whose GCD is 1.
  (define min-len-to-one (+ n 1)) ; Initialize with a value larger than any possible length

  (for ([i (in-range n)])
    (define current-gcd (vector-ref nums i))
    (for ([j (in-range (+ i 1) n)])
      (set! current-gcd (gcd current-gcd (vector-ref nums j)))
      (when (= current-gcd 1)
        (set! min-len-to-one (min min-len-to-one (+ (- j i) 1)))
        (break) ; Found the shortest subarray starting at i with GCD 1
        )))

  (if (= min-len-to-one (+ n 1))
      -1 ; Impossible to make any element 1
      ;; Operations to create one '1': min-len-to-one - 1
      ;; Operations to convert remaining n-1 elements to '1': n - 1
      (+ (- min-len-to-one 1) (- n 1))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([min_operations/1]).

%% Function to compute GCD
gcd(A, 0) -> A;
gcd(A, B) -> gcd(B, A rem B).

-spec min_operations(Nums :: [integer()]) -> integer().
min_operations(Nums) ->
    N = length(Nums),
    CountOnes = lists:foldl(fun(X, Acc) -> if X == 1 -> Acc + 1; true -> Acc end end, 0, Nums),

    if CountOnes > 0 ->
        N - CountOnes;
    true ->
        %% No ones in the array, need to create one.
        %% Find the shortest subarray whose GCD is 1.
        MinLenToOne = find_min_len_to_one(Nums, N),

        if MinLenToOne == N + 1 ->
            -1; %% Impossible to make any element 1
        true ->
            %% Operations to create one '1': MinLenToOne - 1
            %% Operations to convert remaining N-1 elements to '1': N - 1
            (MinLenToOne - 1) + (N - 1)
        end
    end.

find_min_len_to_one(Nums, N) ->
    lists:foldl(fun(I, AccMinLen) ->
        CurrentGcd = lists:nth(I + 1, Nums),
        {NewMinLen, _} = lists:foldl(fun(J, {CurrentMinLen, CurrentGcdAcc}) ->
            NextGcd = gcd(CurrentGcdAcc, lists:nth(J + 1, Nums)),
            if NextGcd == 1 ->
                {min(CurrentMinLen, J - I + 1), NextGcd};
            true ->
                {CurrentMinLen, NextGcd}
            end
        end, {AccMinLen, CurrentGcd}, lists:seq(I + 1, N - 1)),
        NewMinLen
    end, N + 1, lists:seq(0, N - 1)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_operations(nums :: [integer()]) :: integer()
  def min_operations(nums) do
    n = length(nums)
    count_ones = Enum.count(nums, fn x -> x == 1 end)

    if count_ones > 0 do
      n - count_ones
    else
      # No ones in the array, need to create one.
      # Find the shortest subarray whose GCD is 1.
      min_len_to_one = find_min_len_to_one(nums, n)

      if min_len_to_one == n + 1 do
        -1 # Impossible to make any element 1
      else
        # Operations to create one '1': min_len_to_one - 1
        # Operations to convert remaining n-1 elements to '1': n - 1
        (min_len_to_one - 1) + (n - 1)
      end
    end
  end

  defp find_min_len_to_one(nums, n) do
    0..(n - 1)
    |> Enum.reduce(n + 1, fn i, acc_min_len ->
      current_gcd = Enum.at(nums, i)
      {new_min_len, _} = (i + 1)..(n - 1)
      |> Enum.reduce({acc_min_len, current_gcd}, fn j, {current_min_len, current_gcd_acc} ->
        next_gcd = gcd(current_gcd_acc, Enum.at(nums, j))
        if next_gcd == 1 do
          {min(current_min_len, j - i + 1), next_gcd}
        else
          {current_min_len, next_gcd}
        end
      end)
      new_min_len
    end)
  end

  defp gcd(a, 0), do: a
  defp gcd(a, b), do: gcd(b, rem(a, b))
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N^2 * log(max_val)). In the worst case, we iterate through all possible subarrays (N^2 subarrays). For each subarray, we compute its GCD, which involves N GCD operations. Each GCD operation takes O(log(max_val)) time, where max_val is the maximum value in `nums`. Since N is small (up to 50), N^2 is 2500, and log(10^6) is about 20, this complexity is well within limits.

- **Space Complexity:** The space complexity is O(1) as we only use a few variables to store counts, minimum length, and current GCD during the iteration. No auxiliary data structures that scale with input size are used.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-11-25 00:11:46 )</small>
</summary>

<div class="ai-solution-content">

### Approach

No approach provided

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
// Generation failed for C++
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
// Generation failed for Java
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
// Generation failed for Python
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
// Generation failed for Python3
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
// Generation failed for C
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
// Generation failed for C#
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
// Generation failed for JavaScript
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
// Generation failed for TypeScript
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
// Generation failed for PHP
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
// Generation failed for Swift
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
// Generation failed for Kotlin
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
// Generation failed for Dart
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
// Generation failed for Go
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
// Generation failed for Ruby
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
// Generation failed for Scala
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
// Generation failed for Rust
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
// Generation failed for Racket
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
// Generation failed for Erlang
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
// Generation failed for Elixir
// Reason: HTTP Error 429
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** N/A

- **Space Complexity:** N/A

</div>
</details>
