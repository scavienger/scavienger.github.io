---
layout: post
title: "Four Divisors"
date: 2026-01-04 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Math"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/four-divisors/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int sumFourDivisors(std::vector<int>& nums)\
        \ {\n        int totalSumOfDivisors = 0;\n\n        for (int num : nums) {\n\
        \            int currentDivisorsCount = 0;\n            int currentDivisorsSum\
        \ = 0;\n\n            for (int i = 1; i * i <= num; ++i) {\n               \
        \ if (num % i == 0) {\n                    currentDivisorsCount++;\n       \
        \             currentDivisorsSum += i;\n\n                    if (i * i != num)\
        \ {\n                        currentDivisorsCount++;\n                     \
        \   currentDivisorsSum += num / i;\n                    }\n                }\n\
        \n                if (currentDivisorsCount > 4) {\n                    break;\n\
        \                }\n            }\n\n            if (currentDivisorsCount ==\
        \ 4) {\n                totalSumOfDivisors += currentDivisorsSum;\n        \
        \    }\n        }\n\n        return totalSumOfDivisors;\n    }\n};"
      java: "import java.util.List;\n\nclass Solution {\n    public int sumFourDivisors(List<Integer>\
        \ nums) {\n        int totalSumOfDivisors = 0;\n\n        for (int num : nums)\
        \ {\n            int currentDivisorsCount = 0;\n            int currentDivisorsSum\
        \ = 0;\n\n            for (int i = 1; i * i <= num; ++i) {\n               \
        \ if (num % i == 0) {\n                    currentDivisorsCount++;\n       \
        \             currentDivisorsSum += i;\n\n                    if (i * i != num)\
        \ {\n                        currentDivisorsCount++;\n                     \
        \   currentDivisorsSum += num / i;\n                    }\n                }\n\
        \n                if (currentDivisorsCount > 4) {\n                    break;\n\
        \                }\n            }\n\n            if (currentDivisorsCount ==\
        \ 4) {\n                totalSumOfDivisors += currentDivisorsSum;\n        \
        \    }\n        }\n\n        return totalSumOfDivisors;\n    }\n}"
      python: "import math\n\nclass Solution:\n    def sumFourDivisors(self, nums: List[int])\
        \ -> int:\n        total_sum_of_divisors = 0\n\n        for num in nums:\n \
        \           current_divisors_count = 0\n            current_divisors_sum = 0\n\
        \n            i = 1\n            while i * i <= num:\n                if num\
        \ % i == 0:\n                    current_divisors_count += 1\n             \
        \       current_divisors_sum += i\n\n                    if i * i != num:\n\
        \                        current_divisors_count += 1\n                     \
        \   current_divisors_sum += num // i\n\n                if current_divisors_count\
        \ > 4:\n                    break\n\n                i += 1\n\n            if\
        \ current_divisors_count == 4:\n                total_sum_of_divisors += current_divisors_sum\n\
        \n        return total_sum_of_divisors"
      python3: "import math\n\nclass Solution:\n    def sumFourDivisors(self, nums:\
        \ List[int]) -> int:\n        total_sum_of_divisors = 0\n\n        for num in\
        \ nums:\n            current_divisors_count = 0\n            current_divisors_sum\
        \ = 0\n\n            i = 1\n            while i * i <= num:\n              \
        \  if num % i == 0:\n                    current_divisors_count += 1\n     \
        \               current_divisors_sum += i\n\n                    if i * i !=\
        \ num:\n                        current_divisors_count += 1\n              \
        \          current_divisors_sum += num // i\n\n                if current_divisors_count\
        \ > 4:\n                    break\n\n                i += 1\n\n            if\
        \ current_divisors_count == 4:\n                total_sum_of_divisors += current_divisors_sum\n\
        \n        return total_sum_of_divisors"
      c: "int sumFourDivisors(int* nums, int numsSize) {\n    int totalSumOfDivisors\
        \ = 0;\n\n    for (int k = 0; k < numsSize; ++k) {\n        int num = nums[k];\n\
        \        int currentDivisorsCount = 0;\n        int currentDivisorsSum = 0;\n\
        \n        for (int i = 1; i * i <= num; ++i) {\n            if (num % i == 0)\
        \ {\n                currentDivisorsCount++;\n                currentDivisorsSum\
        \ += i;\n\n                if (i * i != num) {\n                    currentDivisorsCount++;\n\
        \                    currentDivisorsSum += num / i;\n                }\n   \
        \         }\n\n            if (currentDivisorsCount > 4) {\n               \
        \ break;\n            }\n        }\n\n        if (currentDivisorsCount == 4)\
        \ {\n            totalSumOfDivisors += currentDivisorsSum;\n        }\n    }\n\
        \n    return totalSumOfDivisors;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int SumFourDivisors(int[] nums) {\n        int totalSumOfDivisors\
        \ = 0;\n\n        foreach (int num in nums) {\n            int currentDivisorsCount\
        \ = 0;\n            int currentDivisorsSum = 0;\n\n            for (int i =\
        \ 1; i * i <= num; ++i) {\n                if (num % i == 0) {\n           \
        \         currentDivisorsCount++;\n                    currentDivisorsSum +=\
        \ i;\n\n                    if (i * i != num) {\n                        currentDivisorsCount++;\n\
        \                        currentDivisorsSum += num / i;\n                  \
        \  }\n                }\n\n                if (currentDivisorsCount > 4) {\n\
        \                    break;\n                }\n            }\n\n          \
        \  if (currentDivisorsCount == 4) {\n                totalSumOfDivisors += currentDivisorsSum;\n\
        \            }\n        }\n\n        return totalSumOfDivisors;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar sumFourDivisors\
        \ = function(nums) {\n    let totalSumOfDivisors = 0;\n\n    for (let num of\
        \ nums) {\n        let currentDivisorsCount = 0;\n        let currentDivisorsSum\
        \ = 0;\n\n        for (let i = 1; i * i <= num; ++i) {\n            if (num\
        \ % i === 0) {\n                currentDivisorsCount++;\n                currentDivisorsSum\
        \ += i;\n\n                if (i * i !== num) {\n                    currentDivisorsCount++;\n\
        \                    currentDivisorsSum += num / i;\n                }\n   \
        \         }\n\n            if (currentDivisorsCount > 4) {\n               \
        \ break;\n            }\n        }\n\n        if (currentDivisorsCount === 4)\
        \ {\n            totalSumOfDivisors += currentDivisorsSum;\n        }\n    }\n\
        \n    return totalSumOfDivisors;\n};"
      typescript: "function sumFourDivisors(nums: number[]): number {\n    let totalSumOfDivisors:\
        \ number = 0;\n\n    for (const num of nums) {\n        let currentDivisorsCount:\
        \ number = 0;\n        let currentDivisorsSum: number = 0;\n\n        for (let\
        \ i: number = 1; i * i <= num; ++i) {\n            if (num % i === 0) {\n  \
        \              currentDivisorsCount++;\n                currentDivisorsSum +=\
        \ i;\n\n                if (i * i !== num) {\n                    currentDivisorsCount++;\n\
        \                    currentDivisorsSum += num / i;\n                }\n   \
        \         }\n\n            if (currentDivisorsCount > 4) {\n               \
        \ break;\n            }\n        }\n\n        if (currentDivisorsCount === 4)\
        \ {\n            totalSumOfDivisors += currentDivisorsSum;\n        }\n    }\n\
        \n    return totalSumOfDivisors;\n};"
      php: "<?php\nclass Solution {\n\n    /**\n     * @param Integer[] $nums\n    \
        \ * @return Integer\n     */\n    function sumFourDivisors($nums) {\n      \
        \  $totalSumOfDivisors = 0;\n\n        foreach ($nums as $num) {\n         \
        \   $currentDivisorsCount = 0;\n            $currentDivisorsSum = 0;\n\n   \
        \         for ($i = 1; $i * $i <= $num; ++$i) {\n                if ($num %\
        \ $i === 0) {\n                    $currentDivisorsCount++;\n              \
        \      $currentDivisorsSum += $i;\n\n                    if ($i * $i !== $num)\
        \ {\n                        $currentDivisorsCount++;\n                    \
        \    $currentDivisorsSum += $num / $i;\n                    }\n            \
        \    }\n\n                if ($currentDivisorsCount > 4) {\n               \
        \     break;\n                }\n            }\n\n            if ($currentDivisorsCount\
        \ === 4) {\n                $totalSumOfDivisors += $currentDivisorsSum;\n  \
        \          }\n        }\n\n        return $totalSumOfDivisors;\n    }\n}\n?>"
      swift: "import Foundation\n\nclass Solution {\n    func sumFourDivisors(_ nums:\
        \ [Int]) -> Int {\n        var totalSumOfDivisors = 0\n\n        for num in\
        \ nums {\n            var currentDivisorsCount = 0\n            var currentDivisorsSum\
        \ = 0\n\n            var i = 1\n            while i * i <= num {\n         \
        \       if num % i == 0 {\n                    currentDivisorsCount += 1\n \
        \                   currentDivisorsSum += i\n\n                    if i * i\
        \ != num {\n                        currentDivisorsCount += 1\n            \
        \            currentDivisorsSum += num / i\n                    }\n        \
        \        }\n\n                if currentDivisorsCount > 4 {\n              \
        \      break\n                }\n\n                i += 1\n            }\n\n\
        \            if currentDivisorsCount == 4 {\n                totalSumOfDivisors\
        \ += currentDivisorsSum\n            }\n        }\n\n        return totalSumOfDivisors\n\
        \    }\n}"
      kotlin: "import kotlin.math.sqrt\n\nclass Solution {\n    fun sumFourDivisors(nums:\
        \ IntArray): Int {\n        var totalSumOfDivisors = 0\n\n        for (num in\
        \ nums) {\n            var currentDivisorsCount = 0\n            var currentDivisorsSum\
        \ = 0\n\n            var i = 1\n            while (i * i <= num) {\n       \
        \         if (num % i == 0) {\n                    currentDivisorsCount++\n\
        \                    currentDivisorsSum += i\n\n                    if (i *\
        \ i != num) {\n                        currentDivisorsCount++\n            \
        \            currentDivisorsSum += num / i\n                    }\n        \
        \        }\n\n                if (currentDivisorsCount > 4) {\n            \
        \        break\n                }\n\n                i++\n            }\n\n\
        \            if (currentDivisorsCount == 4) {\n                totalSumOfDivisors\
        \ += currentDivisorsSum\n            }\n        }\n\n        return totalSumOfDivisors\n\
        \    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int sumFourDivisors(List<int>\
        \ nums) {\n    int totalSumOfDivisors = 0;\n\n    for (int num in nums) {\n\
        \      int currentDivisorsCount = 0;\n      int currentDivisorsSum = 0;\n\n\
        \      for (int i = 1; i * i <= num; ++i) {\n        if (num % i == 0) {\n \
        \         currentDivisorsCount++;\n          currentDivisorsSum += i;\n\n  \
        \        if (i * i != num) {\n            currentDivisorsCount++;\n        \
        \    currentDivisorsSum += num ~/ i; // Integer division\n          }\n    \
        \    }\n\n        if (currentDivisorsCount > 4) {\n          break;\n      \
        \  }\n      }\n\n      if (currentDivisorsCount == 4) {\n        totalSumOfDivisors\
        \ += currentDivisorsSum;\n      }\n    }\n\n    return totalSumOfDivisors;\n\
        \  }\n}"
      go: "package main\n\nimport \"math\"\n\nfunc sumFourDivisors(nums []int) int {\n\
        \    totalSumOfDivisors := 0\n\n    for _, num := range nums {\n        currentDivisorsCount\
        \ := 0\n        currentDivisorsSum := 0\n\n        for i := 1; i * i <= num;\
        \ i++ {\n            if num % i == 0 {\n                currentDivisorsCount++\n\
        \                currentDivisorsSum += i\n\n                if i * i != num\
        \ {\n                    currentDivisorsCount++\n                    currentDivisorsSum\
        \ += num / i\n                }\n            }\n\n            if currentDivisorsCount\
        \ > 4 {\n                break\n            }\n        }\n\n        if currentDivisorsCount\
        \ == 4 {\n            totalSumOfDivisors += currentDivisorsSum\n        }\n\
        \    }\n\n    return totalSumOfDivisors\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef sum_four_divisors(nums)\n\
        \    total_sum_of_divisors = 0\n\n    nums.each do |num|\n        current_divisors_count\
        \ = 0\n        current_divisors_sum = 0\n\n        i = 1\n        while i *\
        \ i <= num\n            if num % i == 0\n                current_divisors_count\
        \ += 1\n                current_divisors_sum += i\n\n                if i *\
        \ i != num\n                    current_divisors_count += 1\n              \
        \      current_divisors_sum += num / i\n                end\n            end\n\
        \n            if current_divisors_count > 4\n                break\n       \
        \     end\n\n            i += 1\n        end\n\n        if current_divisors_count\
        \ == 4\n            total_sum_of_divisors += current_divisors_sum\n        end\n\
        \    end\n\n    total_sum_of_divisors\nend"
      scala: "object Solution {\n    def sumFourDivisors(nums: Array[Int]): Int = {\n\
        \        var totalSumOfDivisors = 0\n\n        for (num <- nums) {\n       \
        \     var currentDivisorsCount = 0\n            var currentDivisorsSum = 0\n\
        \            var i = 1\n            var continueLoop = true\n\n            while\
        \ (i * i <= num && continueLoop) {\n                if (num % i == 0) {\n  \
        \                  currentDivisorsCount += 1\n                    currentDivisorsSum\
        \ += i\n\n                    if (i * i != num) {\n                        currentDivisorsCount\
        \ += 1\n                        currentDivisorsSum += num / i\n            \
        \        }\n                }\n\n                if (currentDivisorsCount >\
        \ 4) {\n                    continueLoop = false\n                }\n\n    \
        \            i += 1\n            }\n\n            if (currentDivisorsCount ==\
        \ 4) {\n                totalSumOfDivisors += currentDivisorsSum\n         \
        \   }\n        }\n\n        totalSumOfDivisors\n    }\n}"
      rust: "impl Solution {\n    pub fn sum_four_divisors(nums: Vec<i32>) -> i32 {\n\
        \        let mut total_sum_of_divisors = 0;\n\n        for num in nums {\n \
        \           let mut current_divisors_count = 0;\n            let mut current_divisors_sum\
        \ = 0;\n\n            let mut i = 1;\n            while i * i <= num {\n   \
        \             if num % i == 0 {\n                    current_divisors_count\
        \ += 1;\n                    current_divisors_sum += i;\n\n                \
        \    if i * i != num {\n                        current_divisors_count += 1;\n\
        \                        current_divisors_sum += num / i;\n                \
        \    }\n                }\n\n                if current_divisors_count > 4 {\n\
        \                    break;\n                }\n\n                i += 1;\n\
        \            }\n\n            if current_divisors_count == 4 {\n           \
        \     total_sum_of_divisors += current_divisors_sum;\n            }\n      \
        \  }\n\n        total_sum_of_divisors\n    }\n}"
      racket: "#lang racket\n\n(define (sum-four-divisors nums)\n  (define total-sum-of-divisors\
        \ 0)\n\n  (for ([num (in-list nums)])\n    (define current-divisors-count 0)\n\
        \    (define current-divisors-sum 0)\n\n    (define i 1)\n    (define loop-continue\
        \ #t)\n\n    (while (and loop-continue (<= (* i i) num))\n      (when (= (remainder\
        \ num i) 0)\n        (set! current-divisors-count (+ current-divisors-count\
        \ 1))\n        (set! current-divisors-sum (+ current-divisors-sum i))\n\n  \
        \      (when (not (= (* i i) num))\n          (set! current-divisors-count (+\
        \ current-divisors-count 1))\n          (set! current-divisors-sum (+ current-divisors-sum\
        \ (quotient num i)))))\n\n      (when (> current-divisors-count 4)\n       \
        \ (set! loop-continue #f))\n\n      (set! i (+ i 1)))\n\n    (when (= current-divisors-count\
        \ 4)\n      (set! total-sum-of-divisors (+ total-sum-of-divisors current-divisors-sum))))\n\
        \n  total-sum-of-divisors)"
      erlang: "-module(solution).\n-export([sum_four_divisors/1]).\n\nsum_four_divisors(Nums)\
        \ ->\n    lists:foldl(fun(Num, Acc) ->\n        {Count, Sum} = find_divisors(Num,\
        \ 1, 0, 0),\n        case Count of\n            4 -> Acc + Sum;\n          \
        \  _ -> Acc\n        end\n    end, 0, Nums).\n\nfind_divisors(Num, I, CurrentCount,\
        \ CurrentSum) when I * I > Num ->\n    {CurrentCount, CurrentSum};\nfind_divisors(Num,\
        \ I, CurrentCount, CurrentSum) ->\n    case Num rem I of\n        0 ->\n   \
        \         NewCount1 = CurrentCount + 1,\n            NewSum1 = CurrentSum +\
        \ I,\n            case I * I == Num of\n                true ->\n          \
        \          if NewCount1 > 4 ->\n                        {NewCount1, NewSum1};\n\
        \                    true ->\n                        find_divisors(Num, I +\
        \ 1, NewCount1, NewSum1)\n                    end;\n                false ->\n\
        \                    NewCount2 = NewCount1 + 1,\n                    NewSum2\
        \ = NewSum1 + (Num div I),\n                    if NewCount2 > 4 ->\n      \
        \                  {NewCount2, NewSum2};\n                    true ->\n    \
        \                    find_divisors(Num, I + 1, NewCount2, NewSum2)\n       \
        \             end\n            end;\n        _ ->\n            find_divisors(Num,\
        \ I + 1, CurrentCount, CurrentSum)\n    end."
      elixir: "defmodule Solution do\n  @spec sum_four_divisors(nums :: [integer]) ::\
        \ integer\n  def sum_four_divisors(nums) do\n    Enum.reduce(nums, 0, fn num,\
        \ acc ->\n      {count, sum} = find_divisors(num, 1, 0, 0)\n      if count ==\
        \ 4, do: acc + sum, else: acc\n    end)\n  end\n\n  defp find_divisors(num,\
        \ i, current_count, current_sum) when i * i > num do\n    {current_count, current_sum}\n\
        \  end\n\n  defp find_divisors(num, i, current_count, current_sum) do\n    if\
        \ rem(num, i) == 0 do\n      new_count1 = current_count + 1\n      new_sum1\
        \ = current_sum + i\n\n      if i * i == num do\n        if new_count1 > 4 do\n\
        \          {new_count1, new_sum1}\n        else\n          find_divisors(num,\
        \ i + 1, new_count1, new_sum1)\n        end\n      else\n        new_count2\
        \ = new_count1 + 1\n        new_sum2 = new_sum1 + div(num, i)\n        if new_count2\
        \ > 4 do\n          {new_count2, new_sum2}\n        else\n          find_divisors(num,\
        \ i + 1, new_count2, new_sum2)\n        end\n      end\n    else\n      find_divisors(num,\
        \ i + 1, current_count, current_sum)\n    end\n  end\nend"
    approach: The problem requires us to find the sum of divisors for integers in a
      given array `nums` that have exactly four divisors. A number `n` has exactly four
      divisors if it is either the cube of a prime number (e.g., p^3, with divisors
      1, p, p^2, p^3) or the product of two distinct prime numbers (e.g., p*q, with
      divisors 1, p, q, p*q). Instead of attempting to factorize each number and check
      for these specific prime properties, a more straightforward approach is to directly
      count and sum all divisors for each number.
    time_complexity: The time complexity is dominated by iterating through each number
      in `nums` and, for each number, finding its divisors. For a number `N`, finding
      its divisors up to `sqrt(N)` takes `O(sqrt(N))` time. Given that `nums.length`
      is `L` and the maximum value in `nums` is `M`, the total time complexity will
      be `O(L * sqrt(M))`. With `L = 10^4` and `M = 10^5`, this is approximately `10^4
      * sqrt(10^5) = 10^4 * 316`, which is about `3.16 * 10^6` operations, well within
      typical time limits.
    space_complexity: The space complexity is `O(1)` because we only use a few constant-size
      variables to store the current count of divisors, their sum, and the total sum
      of divisors. We do not use any data structures that grow with the input size beyond
      these few variables.
    elapsed_time: 56.66019129753113
    model: gemini-2.5-flash
    generated_at: '2026-01-04 01:17:15 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int sumFourDivisors(vector<int>& nums) {\n\
        \        int sum = 0;\n        for (int num : nums) {\n            vector<int>\
        \ divisors;\n            for (int i = 1; i * i <= num; i++) {\n            \
        \    if (num % i == 0) {\n                    divisors.push_back(i);\n     \
        \               if (i * i != num) divisors.push_back(num / i);\n           \
        \     }\n            }\n            sort(divisors.begin(), divisors.end());\n\
        \            if (divisors.size() == 4) {\n                for (int d : divisors)\
        \ sum += d;\n            }\n        }\n        return sum;\n    }\n};"
      java: "class Solution {\n    public int sumFourDivisors(int[] nums) {\n      \
        \  int sum = 0;\n        for (int num : nums) {\n            List<Integer> divisors\
        \ = new ArrayList<>();\n            for (int i = 1; i * i <= num; i++) {\n \
        \               if (num % i == 0) {\n                    divisors.add(i);\n\
        \                    if (i * i != num) divisors.add(num / i);\n            \
        \    }\n            }\n            Collections.sort(divisors);\n           \
        \ if (divisors.size() == 4) {\n                for (int d : divisors) sum +=\
        \ d;\n            }\n        }\n        return sum;\n    }\n}"
      python: "class Solution:\n    def sumFourDivisors(self, nums: List[int]) -> int:\n\
        \        sum = 0\n        for num in nums:\n            divisors = []\n    \
        \        for i in range(1, int(num ** 0.5) + 1):\n                if num % i\
        \ == 0:\n                    divisors.append(i)\n                    if i *\
        \ i != num: divisors.append(num // i)\n            divisors.sort()\n       \
        \     if len(divisors) == 4:\n                sum += sum(divisors)\n       \
        \ return sum"
      python3: "class Solution:\n    def sumFourDivisors(self, nums: List[int]) -> int:\n\
        \        sum = 0\n        for num in nums:\n            divisors = []\n    \
        \        for i in range(1, int(num ** 0.5) + 1):\n                if num % i\
        \ == 0:\n                    divisors.append(i)\n                    if i *\
        \ i != num: divisors.append(num // i)\n            divisors.sort()\n       \
        \     if len(divisors) == 4:\n                sum += sum(divisors)\n       \
        \ return sum"
      c: "typedef struct {\n    int* data;\n    int size;\n} vector;\n\nint sumFourDivisors(int*\
        \ nums, int numsSize) {\n    int sum = 0;\n    for (int i = 0; i < numsSize;\
        \ i++) {\n        vector divisors;\n        divisors.data = malloc(100 * sizeof(int));\n\
        \        divisors.size = 0;\n        for (int j = 1; j * j <= nums[i]; j++)\
        \ {\n            if (nums[i] % j == 0) {\n                divisors.data[divisors.size++]\
        \ = j;\n                if (j * j != nums[i]) divisors.data[divisors.size++]\
        \ = nums[i] / j;\n            }\n        }\n        if (divisors.size == 4)\
        \ {\n            for (int j = 0; j < divisors.size; j++) sum += divisors.data[j];\n\
        \        }\n        free(divisors.data);\n    }\n    return sum;\n}"
      csharp: "public class Solution {\n    public int SumFourDivisors(int[] nums) {\n\
        \        int sum = 0;\n        foreach (int num in nums) {\n            List<int>\
        \ divisors = new List<int>();\n            for (int i = 1; i * i <= num; i++)\
        \ {\n                if (num % i == 0) {\n                    divisors.Add(i);\n\
        \                    if (i * i != num) divisors.Add(num / i);\n            \
        \    }\n            }\n            divisors.Sort();\n            if (divisors.Count\
        \ == 4) {\n                foreach (int d in divisors) sum += d;\n         \
        \   }\n        }\n        return sum;\n    }\n}"
      javascript: "var sumFourDivisors = function(nums) {\n    let sum = 0;\n    for\
        \ (let num of nums) {\n        let divisors = [];\n        for (let i = 1; i\
        \ * i <= num; i++) {\n            if (num % i == 0) {\n                divisors.push(i);\n\
        \                if (i * i != num) divisors.push(num / i);\n            }\n\
        \        }\n        divisors.sort((a, b) => a - b);\n        if (divisors.length\
        \ == 4) {\n            sum += divisors.reduce((a, b) => a + b, 0);\n       \
        \ }\n    }\n    return sum;\n};"
      typescript: "function sumFourDivisors(nums: number[]): number {\n    let sum:\
        \ number = 0;\n    for (let num of nums) {\n        let divisors: number[] =\
        \ [];\n        for (let i: number = 1; i * i <= num; i++) {\n            if\
        \ (num % i == 0) {\n                divisors.push(i);\n                if (i\
        \ * i != num) divisors.push(num / i);\n            }\n        }\n        divisors.sort((a,\
        \ b) => a - b);\n        if (divisors.length == 4) {\n            sum += divisors.reduce((a,\
        \ b) => a + b, 0);\n        }\n    }\n    return sum;\n}"
      php: "class Solution {\n    function sumFourDivisors($nums) {\n        $sum =\
        \ 0;\n        foreach ($nums as $num) {\n            $divisors = array();\n\
        \            for ($i = 1; $i * $i <= $num; $i++) {\n                if ($num\
        \ % $i == 0) {\n                    $divisors[] = $i;\n                    if\
        \ ($i * $i != $num) $divisors[] = $num / $i;\n                }\n          \
        \  }\n            sort($divisors);\n            if (count($divisors) == 4) {\n\
        \                $sum += array_sum($divisors);\n            }\n        }\n \
        \       return $sum;\n    }\n}"
      swift: "class Solution {\n    func sumFourDivisors(_ nums: [Int]) -> Int {\n \
        \       var sum = 0\n        for num in nums {\n            var divisors: [Int]\
        \ = []\n            for i in 1...Int(sqrt(Double(num))) {\n                if\
        \ num % i == 0 {\n                    divisors.append(i)\n                 \
        \   if i * i != num { divisors.append(num / i) }\n                }\n      \
        \      }\n            divisors.sort()\n            if divisors.count == 4 {\n\
        \                sum += divisors.reduce(0, +)\n            }\n        }\n  \
        \      return sum\n    }\n}"
      kotlin: "class Solution {\n    fun sumFourDivisors(nums: IntArray): Int {\n  \
        \      var sum = 0\n        for (num in nums) {\n            val divisors =\
        \ mutableListOf<Int>()\n            for (i in 1..kotlin.math.sqrt(num.toDouble()).toInt())\
        \ {\n                if (num % i == 0) {\n                    divisors.add(i)\n\
        \                    if (i * i != num) divisors.add(num / i)\n             \
        \   }\n            }\n            divisors.sort()\n            if (divisors.size\
        \ == 4) {\n                sum += divisors.sum()\n            }\n        }\n\
        \        return sum\n    }\n}"
      dart: "class Solution {\n    int sumFourDivisors(List<int> nums) {\n        int\
        \ sum = 0;\n        for (int num in nums) {\n            List<int> divisors\
        \ = [];\n            for (int i = 1; i * i <= num; i++) {\n                if\
        \ (num % i == 0) {\n                    divisors.add(i);\n                 \
        \   if (i * i != num) divisors.add(num ~/ i);\n                }\n         \
        \   }\n            divisors.sort();\n            if (divisors.length == 4) {\n\
        \                sum += divisors.reduce((a, b) => a + b);\n            }\n \
        \       }\n        return sum;\n    }\n}"
      go: "package main\n\nimport (\n    \"fmt\"\n    \"sort\"\n)\n\ntype Solution struct{}\n\
        \nfunc (s Solution) sumFourDivisors(nums []int) int {\n    sum := 0\n    for\
        \ _, num := range nums {\n        divisors := []int{}\n        for i := 1; i*i\
        \ <= num; i++ {\n            if num%i == 0 {\n                divisors = append(divisors,\
        \ i)\n                if i*i != num {\n                    divisors = append(divisors,\
        \ num/i)\n                }\n            }\n        }\n        sort.Ints(divisors)\n\
        \        if len(divisors) == 4 {\n            for _, d := range divisors {\n\
        \                sum += d\n            }\n        }\n    }\n    return sum\n\
        }"
      ruby: "class Solution\n    def sum_four_divisors(nums)\n        sum = 0\n    \
        \    nums.each do |num|\n            divisors = []\n            (1..Math.sqrt(num)).each\
        \ do |i|\n                if num % i == 0\n                    divisors << i\n\
        \                    divisors << num / i if i * i != num\n                end\n\
        \            end\n            divisors.sort!\n            if divisors.size ==\
        \ 4\n                sum += divisors.sum\n            end\n        end\n   \
        \     sum\n    end\nend"
      scala: "object Solution {\n    def sumFourDivisors(nums: Array[Int]): Int = {\n\
        \        var sum = 0\n        for (num <- nums) {\n            val divisors\
        \ = (1 to math.sqrt(num).toInt).filter(i => num % i == 0).flatMap(i => List(i,\
        \ num / i)).distinct.sorted\n            if (divisors.length == 4) sum += divisors.sum\n\
        \        }\n        sum\n    }\n}"
      rust: "struct Solution;\n\nimpl Solution {\n    pub fn sum_four_divisors(nums:\
        \ Vec<i32>) -> i32 {\n        let mut sum = 0;\n        for num in nums {\n\
        \            let mut divisors: Vec<i32> = Vec::new();\n            for i in\
        \ 1..=(num as f64).sqrt() as i32 {\n                if num % i == 0 {\n    \
        \                divisors.push(i);\n                    if i * i != num {\n\
        \                        divisors.push(num / i);\n                    }\n  \
        \              }\n            }\n            divisors.sort();\n            if\
        \ divisors.len() == 4 {\n                sum += divisors.iter().sum::<i32>();\n\
        \            }\n        }\n        sum\n    }\n}"
      racket: "(define (sum-four-divisors nums)\n    (let loop ((nums nums) (sum 0))\n\
        \        (if (null? nums)\n            sum\n            (let ((num (car nums))\n\
        \                  (divisors (filter (lambda (i) (zero? (remainder num i)))\n\
        \                                  (range 1 (add1 (sqrt num))))))\n        \
        \        (loop (cdr nums)\n                     (if (= (length divisors) 4)\n\
        \                         (+ sum (apply + divisors))\n                     \
        \    sum))))))"
      erlang: "sum_four_divisors(Nums) ->\n    sum_four_divisors(Nums, 0).\n\nsum_four_divisors([],\
        \ Sum) -> Sum;\nsum_four_divisors([Num | Nums], Sum) ->\n    Divisors = [I ||\
        \ I <- lists:seq(1, trunc(math:sqrt(Num))), Num rem I == 0],\n    case length(Divisors)\
        \ of\n        4 -> sum_four_divisors(Nums, Sum + lists:sum(Divisors));\n   \
        \     _ -> sum_four_divisors(Nums, Sum)\n    end."
      elixir: "def sum_four_divisors(nums) do\n    sum_four_divisors(nums, 0)\nend\n\
        \ndefp sum_four_divisors([], sum), do: sum\n\ndefp sum_four_divisors([num |\
        \ nums], sum) do\n    divisors = for i <- 1..:math.sqrt(num), rem(num, i) ==\
        \ 0, do: i\n    if length(divisors) == 4, do: sum_four_divisors(nums, sum +\
        \ Enum.sum(divisors)),\n    else: sum_four_divisors(nums, sum)\nend"
    approach: The problem requires finding the sum of divisors of integers in an array
      that have exactly four divisors. To solve this, we need to iterate over each number
      in the array and find its divisors. We can optimize this process by only looping
      up to the square root of each number, as any factor larger than the square root
      would have a corresponding factor smaller than the square root. For each number,
      we count its divisors and if the count is exactly four, we add the divisors to
      the total sum.
    time_complexity: The time complexity of this solution is O(n * sqrt(m)), where n
      is the number of elements in the array and m is the maximum value in the array.
      This is because for each number in the array, we are potentially looping up to
      its square root to find its divisors.
    space_complexity: The space complexity of this solution is O(1), as we are only
      using a constant amount of space to store the total sum and the count of divisors
      for each number. We are not using any data structures that scale with the input
      size.
    elapsed_time: 6.1825785636901855
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-04 01:17:21 '
---

## Problem #1390: Four Divisors

**Difficulty:** Medium

**Topics:** Array, Math

## Problem Description

<p>Given an integer array <code>nums</code>, return <em>the sum of divisors of the integers in that array that have exactly four divisors</em>. If there is no such integer in the array, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [21,4,7]
<strong>Output:</strong> 32
<strong>Explanation:</strong> 
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [21,21]
<strong>Output:</strong> 64
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. Find the divisors of each element in the array.

2. You only need to loop to the square root of a number to find its divisors.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2026-01-04 01:17:15 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem requires us to find the sum of divisors for integers in a given array `nums` that have exactly four divisors. A number `n` has exactly four divisors if it is either the cube of a prime number (e.g., p^3, with divisors 1, p, p^2, p^3) or the product of two distinct prime numbers (e.g., p*q, with divisors 1, p, q, p*q). Instead of attempting to factorize each number and check for these specific prime properties, a more straightforward approach is to directly count and sum all divisors for each number.

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
    int sumFourDivisors(std::vector<int>& nums) {
        int totalSumOfDivisors = 0;

        for (int num : nums) {
            int currentDivisorsCount = 0;
            int currentDivisorsSum = 0;

            for (int i = 1; i * i <= num; ++i) {
                if (num % i == 0) {
                    currentDivisorsCount++;
                    currentDivisorsSum += i;

                    if (i * i != num) {
                        currentDivisorsCount++;
                        currentDivisorsSum += num / i;
                    }
                }

                if (currentDivisorsCount > 4) {
                    break;
                }
            }

            if (currentDivisorsCount == 4) {
                totalSumOfDivisors += currentDivisorsSum;
            }
        }

        return totalSumOfDivisors;
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
    public int sumFourDivisors(List<Integer> nums) {
        int totalSumOfDivisors = 0;

        for (int num : nums) {
            int currentDivisorsCount = 0;
            int currentDivisorsSum = 0;

            for (int i = 1; i * i <= num; ++i) {
                if (num % i == 0) {
                    currentDivisorsCount++;
                    currentDivisorsSum += i;

                    if (i * i != num) {
                        currentDivisorsCount++;
                        currentDivisorsSum += num / i;
                    }
                }

                if (currentDivisorsCount > 4) {
                    break;
                }
            }

            if (currentDivisorsCount == 4) {
                totalSumOfDivisors += currentDivisorsSum;
            }
        }

        return totalSumOfDivisors;
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
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum_of_divisors = 0

        for num in nums:
            current_divisors_count = 0
            current_divisors_sum = 0

            i = 1
            while i * i <= num:
                if num % i == 0:
                    current_divisors_count += 1
                    current_divisors_sum += i

                    if i * i != num:
                        current_divisors_count += 1
                        current_divisors_sum += num // i

                if current_divisors_count > 4:
                    break

                i += 1

            if current_divisors_count == 4:
                total_sum_of_divisors += current_divisors_sum

        return total_sum_of_divisors
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import math

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum_of_divisors = 0

        for num in nums:
            current_divisors_count = 0
            current_divisors_sum = 0

            i = 1
            while i * i <= num:
                if num % i == 0:
                    current_divisors_count += 1
                    current_divisors_sum += i

                    if i * i != num:
                        current_divisors_count += 1
                        current_divisors_sum += num // i

                if current_divisors_count > 4:
                    break

                i += 1

            if current_divisors_count == 4:
                total_sum_of_divisors += current_divisors_sum

        return total_sum_of_divisors
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int sumFourDivisors(int* nums, int numsSize) {
    int totalSumOfDivisors = 0;

    for (int k = 0; k < numsSize; ++k) {
        int num = nums[k];
        int currentDivisorsCount = 0;
        int currentDivisorsSum = 0;

        for (int i = 1; i * i <= num; ++i) {
            if (num % i == 0) {
                currentDivisorsCount++;
                currentDivisorsSum += i;

                if (i * i != num) {
                    currentDivisorsCount++;
                    currentDivisorsSum += num / i;
                }
            }

            if (currentDivisorsCount > 4) {
                break;
            }
        }

        if (currentDivisorsCount == 4) {
            totalSumOfDivisors += currentDivisorsSum;
        }
    }

    return totalSumOfDivisors;
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
    public int SumFourDivisors(int[] nums) {
        int totalSumOfDivisors = 0;

        foreach (int num in nums) {
            int currentDivisorsCount = 0;
            int currentDivisorsSum = 0;

            for (int i = 1; i * i <= num; ++i) {
                if (num % i == 0) {
                    currentDivisorsCount++;
                    currentDivisorsSum += i;

                    if (i * i != num) {
                        currentDivisorsCount++;
                        currentDivisorsSum += num / i;
                    }
                }

                if (currentDivisorsCount > 4) {
                    break;
                }
            }

            if (currentDivisorsCount == 4) {
                totalSumOfDivisors += currentDivisorsSum;
            }
        }

        return totalSumOfDivisors;
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
var sumFourDivisors = function(nums) {
    let totalSumOfDivisors = 0;

    for (let num of nums) {
        let currentDivisorsCount = 0;
        let currentDivisorsSum = 0;

        for (let i = 1; i * i <= num; ++i) {
            if (num % i === 0) {
                currentDivisorsCount++;
                currentDivisorsSum += i;

                if (i * i !== num) {
                    currentDivisorsCount++;
                    currentDivisorsSum += num / i;
                }
            }

            if (currentDivisorsCount > 4) {
                break;
            }
        }

        if (currentDivisorsCount === 4) {
            totalSumOfDivisors += currentDivisorsSum;
        }
    }

    return totalSumOfDivisors;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function sumFourDivisors(nums: number[]): number {
    let totalSumOfDivisors: number = 0;

    for (const num of nums) {
        let currentDivisorsCount: number = 0;
        let currentDivisorsSum: number = 0;

        for (let i: number = 1; i * i <= num; ++i) {
            if (num % i === 0) {
                currentDivisorsCount++;
                currentDivisorsSum += i;

                if (i * i !== num) {
                    currentDivisorsCount++;
                    currentDivisorsSum += num / i;
                }
            }

            if (currentDivisorsCount > 4) {
                break;
            }
        }

        if (currentDivisorsCount === 4) {
            totalSumOfDivisors += currentDivisorsSum;
        }
    }

    return totalSumOfDivisors;
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
     * @param Integer[] $nums
     * @return Integer
     */
    function sumFourDivisors($nums) {
        $totalSumOfDivisors = 0;

        foreach ($nums as $num) {
            $currentDivisorsCount = 0;
            $currentDivisorsSum = 0;

            for ($i = 1; $i * $i <= $num; ++$i) {
                if ($num % $i === 0) {
                    $currentDivisorsCount++;
                    $currentDivisorsSum += $i;

                    if ($i * $i !== $num) {
                        $currentDivisorsCount++;
                        $currentDivisorsSum += $num / $i;
                    }
                }

                if ($currentDivisorsCount > 4) {
                    break;
                }
            }

            if ($currentDivisorsCount === 4) {
                $totalSumOfDivisors += $currentDivisorsSum;
            }
        }

        return $totalSumOfDivisors;
    }
}
?>
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
import Foundation

class Solution {
    func sumFourDivisors(_ nums: [Int]) -> Int {
        var totalSumOfDivisors = 0

        for num in nums {
            var currentDivisorsCount = 0
            var currentDivisorsSum = 0

            var i = 1
            while i * i <= num {
                if num % i == 0 {
                    currentDivisorsCount += 1
                    currentDivisorsSum += i

                    if i * i != num {
                        currentDivisorsCount += 1
                        currentDivisorsSum += num / i
                    }
                }

                if currentDivisorsCount > 4 {
                    break
                }

                i += 1
            }

            if currentDivisorsCount == 4 {
                totalSumOfDivisors += currentDivisorsSum
            }
        }

        return totalSumOfDivisors
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import kotlin.math.sqrt

class Solution {
    fun sumFourDivisors(nums: IntArray): Int {
        var totalSumOfDivisors = 0

        for (num in nums) {
            var currentDivisorsCount = 0
            var currentDivisorsSum = 0

            var i = 1
            while (i * i <= num) {
                if (num % i == 0) {
                    currentDivisorsCount++
                    currentDivisorsSum += i

                    if (i * i != num) {
                        currentDivisorsCount++
                        currentDivisorsSum += num / i
                    }
                }

                if (currentDivisorsCount > 4) {
                    break
                }

                i++
            }

            if (currentDivisorsCount == 4) {
                totalSumOfDivisors += currentDivisorsSum
            }
        }

        return totalSumOfDivisors
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
  int sumFourDivisors(List<int> nums) {
    int totalSumOfDivisors = 0;

    for (int num in nums) {
      int currentDivisorsCount = 0;
      int currentDivisorsSum = 0;

      for (int i = 1; i * i <= num; ++i) {
        if (num % i == 0) {
          currentDivisorsCount++;
          currentDivisorsSum += i;

          if (i * i != num) {
            currentDivisorsCount++;
            currentDivisorsSum += num ~/ i; // Integer division
          }
        }

        if (currentDivisorsCount > 4) {
          break;
        }
      }

      if (currentDivisorsCount == 4) {
        totalSumOfDivisors += currentDivisorsSum;
      }
    }

    return totalSumOfDivisors;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

import "math"

func sumFourDivisors(nums []int) int {
    totalSumOfDivisors := 0

    for _, num := range nums {
        currentDivisorsCount := 0
        currentDivisorsSum := 0

        for i := 1; i * i <= num; i++ {
            if num % i == 0 {
                currentDivisorsCount++
                currentDivisorsSum += i

                if i * i != num {
                    currentDivisorsCount++
                    currentDivisorsSum += num / i
                }
            }

            if currentDivisorsCount > 4 {
                break
            }
        }

        if currentDivisorsCount == 4 {
            totalSumOfDivisors += currentDivisorsSum
        }
    }

    return totalSumOfDivisors
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def sum_four_divisors(nums)
    total_sum_of_divisors = 0

    nums.each do |num|
        current_divisors_count = 0
        current_divisors_sum = 0

        i = 1
        while i * i <= num
            if num % i == 0
                current_divisors_count += 1
                current_divisors_sum += i

                if i * i != num
                    current_divisors_count += 1
                    current_divisors_sum += num / i
                end
            end

            if current_divisors_count > 4
                break
            end

            i += 1
        end

        if current_divisors_count == 4
            total_sum_of_divisors += current_divisors_sum
        end
    end

    total_sum_of_divisors
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def sumFourDivisors(nums: Array[Int]): Int = {
        var totalSumOfDivisors = 0

        for (num <- nums) {
            var currentDivisorsCount = 0
            var currentDivisorsSum = 0
            var i = 1
            var continueLoop = true

            while (i * i <= num && continueLoop) {
                if (num % i == 0) {
                    currentDivisorsCount += 1
                    currentDivisorsSum += i

                    if (i * i != num) {
                        currentDivisorsCount += 1
                        currentDivisorsSum += num / i
                    }
                }

                if (currentDivisorsCount > 4) {
                    continueLoop = false
                }

                i += 1
            }

            if (currentDivisorsCount == 4) {
                totalSumOfDivisors += currentDivisorsSum
            }
        }

        totalSumOfDivisors
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn sum_four_divisors(nums: Vec<i32>) -> i32 {
        let mut total_sum_of_divisors = 0;

        for num in nums {
            let mut current_divisors_count = 0;
            let mut current_divisors_sum = 0;

            let mut i = 1;
            while i * i <= num {
                if num % i == 0 {
                    current_divisors_count += 1;
                    current_divisors_sum += i;

                    if i * i != num {
                        current_divisors_count += 1;
                        current_divisors_sum += num / i;
                    }
                }

                if current_divisors_count > 4 {
                    break;
                }

                i += 1;
            }

            if current_divisors_count == 4 {
                total_sum_of_divisors += current_divisors_sum;
            }
        }

        total_sum_of_divisors
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (sum-four-divisors nums)
  (define total-sum-of-divisors 0)

  (for ([num (in-list nums)])
    (define current-divisors-count 0)
    (define current-divisors-sum 0)

    (define i 1)
    (define loop-continue #t)

    (while (and loop-continue (<= (* i i) num))
      (when (= (remainder num i) 0)
        (set! current-divisors-count (+ current-divisors-count 1))
        (set! current-divisors-sum (+ current-divisors-sum i))

        (when (not (= (* i i) num))
          (set! current-divisors-count (+ current-divisors-count 1))
          (set! current-divisors-sum (+ current-divisors-sum (quotient num i)))))

      (when (> current-divisors-count 4)
        (set! loop-continue #f))

      (set! i (+ i 1)))

    (when (= current-divisors-count 4)
      (set! total-sum-of-divisors (+ total-sum-of-divisors current-divisors-sum))))

  total-sum-of-divisors)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([sum_four_divisors/1]).

sum_four_divisors(Nums) ->
    lists:foldl(fun(Num, Acc) ->
        {Count, Sum} = find_divisors(Num, 1, 0, 0),
        case Count of
            4 -> Acc + Sum;
            _ -> Acc
        end
    end, 0, Nums).

find_divisors(Num, I, CurrentCount, CurrentSum) when I * I > Num ->
    {CurrentCount, CurrentSum};
find_divisors(Num, I, CurrentCount, CurrentSum) ->
    case Num rem I of
        0 ->
            NewCount1 = CurrentCount + 1,
            NewSum1 = CurrentSum + I,
            case I * I == Num of
                true ->
                    if NewCount1 > 4 ->
                        {NewCount1, NewSum1};
                    true ->
                        find_divisors(Num, I + 1, NewCount1, NewSum1)
                    end;
                false ->
                    NewCount2 = NewCount1 + 1,
                    NewSum2 = NewSum1 + (Num div I),
                    if NewCount2 > 4 ->
                        {NewCount2, NewSum2};
                    true ->
                        find_divisors(Num, I + 1, NewCount2, NewSum2)
                    end
            end;
        _ ->
            find_divisors(Num, I + 1, CurrentCount, CurrentSum)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec sum_four_divisors(nums :: [integer]) :: integer
  def sum_four_divisors(nums) do
    Enum.reduce(nums, 0, fn num, acc ->
      {count, sum} = find_divisors(num, 1, 0, 0)
      if count == 4, do: acc + sum, else: acc
    end)
  end

  defp find_divisors(num, i, current_count, current_sum) when i * i > num do
    {current_count, current_sum}
  end

  defp find_divisors(num, i, current_count, current_sum) do
    if rem(num, i) == 0 do
      new_count1 = current_count + 1
      new_sum1 = current_sum + i

      if i * i == num do
        if new_count1 > 4 do
          {new_count1, new_sum1}
        else
          find_divisors(num, i + 1, new_count1, new_sum1)
        end
      else
        new_count2 = new_count1 + 1
        new_sum2 = new_sum1 + div(num, i)
        if new_count2 > 4 do
          {new_count2, new_sum2}
        else
          find_divisors(num, i + 1, new_count2, new_sum2)
        end
      end
    else
      find_divisors(num, i + 1, current_count, current_sum)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is dominated by iterating through each number in `nums` and, for each number, finding its divisors. For a number `N`, finding its divisors up to `sqrt(N)` takes `O(sqrt(N))` time. Given that `nums.length` is `L` and the maximum value in `nums` is `M`, the total time complexity will be `O(L * sqrt(M))`. With `L = 10^4` and `M = 10^5`, this is approximately `10^4 * sqrt(10^5) = 10^4 * 316`, which is about `3.16 * 10^6` operations, well within typical time limits.

- **Space Complexity:** The space complexity is `O(1)` because we only use a few constant-size variables to store the current count of divisors, their sum, and the total sum of divisors. We do not use any data structures that grow with the input size beyond these few variables.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-04 01:17:21 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem requires finding the sum of divisors of integers in an array that have exactly four divisors. To solve this, we need to iterate over each number in the array and find its divisors. We can optimize this process by only looping up to the square root of each number, as any factor larger than the square root would have a corresponding factor smaller than the square root. For each number, we count its divisors and if the count is exactly four, we add the divisors to the total sum.

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
    int sumFourDivisors(vector<int>& nums) {
        int sum = 0;
        for (int num : nums) {
            vector<int> divisors;
            for (int i = 1; i * i <= num; i++) {
                if (num % i == 0) {
                    divisors.push_back(i);
                    if (i * i != num) divisors.push_back(num / i);
                }
            }
            sort(divisors.begin(), divisors.end());
            if (divisors.size() == 4) {
                for (int d : divisors) sum += d;
            }
        }
        return sum;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int sumFourDivisors(int[] nums) {
        int sum = 0;
        for (int num : nums) {
            List<Integer> divisors = new ArrayList<>();
            for (int i = 1; i * i <= num; i++) {
                if (num % i == 0) {
                    divisors.add(i);
                    if (i * i != num) divisors.add(num / i);
                }
            }
            Collections.sort(divisors);
            if (divisors.size() == 4) {
                for (int d : divisors) sum += d;
            }
        }
        return sum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        sum = 0
        for num in nums:
            divisors = []
            for i in range(1, int(num ** 0.5) + 1):
                if num % i == 0:
                    divisors.append(i)
                    if i * i != num: divisors.append(num // i)
            divisors.sort()
            if len(divisors) == 4:
                sum += sum(divisors)
        return sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        sum = 0
        for num in nums:
            divisors = []
            for i in range(1, int(num ** 0.5) + 1):
                if num % i == 0:
                    divisors.append(i)
                    if i * i != num: divisors.append(num // i)
            divisors.sort()
            if len(divisors) == 4:
                sum += sum(divisors)
        return sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
typedef struct {
    int* data;
    int size;
} vector;

int sumFourDivisors(int* nums, int numsSize) {
    int sum = 0;
    for (int i = 0; i < numsSize; i++) {
        vector divisors;
        divisors.data = malloc(100 * sizeof(int));
        divisors.size = 0;
        for (int j = 1; j * j <= nums[i]; j++) {
            if (nums[i] % j == 0) {
                divisors.data[divisors.size++] = j;
                if (j * j != nums[i]) divisors.data[divisors.size++] = nums[i] / j;
            }
        }
        if (divisors.size == 4) {
            for (int j = 0; j < divisors.size; j++) sum += divisors.data[j];
        }
        free(divisors.data);
    }
    return sum;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int SumFourDivisors(int[] nums) {
        int sum = 0;
        foreach (int num in nums) {
            List<int> divisors = new List<int>();
            for (int i = 1; i * i <= num; i++) {
                if (num % i == 0) {
                    divisors.Add(i);
                    if (i * i != num) divisors.Add(num / i);
                }
            }
            divisors.Sort();
            if (divisors.Count == 4) {
                foreach (int d in divisors) sum += d;
            }
        }
        return sum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var sumFourDivisors = function(nums) {
    let sum = 0;
    for (let num of nums) {
        let divisors = [];
        for (let i = 1; i * i <= num; i++) {
            if (num % i == 0) {
                divisors.push(i);
                if (i * i != num) divisors.push(num / i);
            }
        }
        divisors.sort((a, b) => a - b);
        if (divisors.length == 4) {
            sum += divisors.reduce((a, b) => a + b, 0);
        }
    }
    return sum;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function sumFourDivisors(nums: number[]): number {
    let sum: number = 0;
    for (let num of nums) {
        let divisors: number[] = [];
        for (let i: number = 1; i * i <= num; i++) {
            if (num % i == 0) {
                divisors.push(i);
                if (i * i != num) divisors.push(num / i);
            }
        }
        divisors.sort((a, b) => a - b);
        if (divisors.length == 4) {
            sum += divisors.reduce((a, b) => a + b, 0);
        }
    }
    return sum;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function sumFourDivisors($nums) {
        $sum = 0;
        foreach ($nums as $num) {
            $divisors = array();
            for ($i = 1; $i * $i <= $num; $i++) {
                if ($num % $i == 0) {
                    $divisors[] = $i;
                    if ($i * $i != $num) $divisors[] = $num / $i;
                }
            }
            sort($divisors);
            if (count($divisors) == 4) {
                $sum += array_sum($divisors);
            }
        }
        return $sum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func sumFourDivisors(_ nums: [Int]) -> Int {
        var sum = 0
        for num in nums {
            var divisors: [Int] = []
            for i in 1...Int(sqrt(Double(num))) {
                if num % i == 0 {
                    divisors.append(i)
                    if i * i != num { divisors.append(num / i) }
                }
            }
            divisors.sort()
            if divisors.count == 4 {
                sum += divisors.reduce(0, +)
            }
        }
        return sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun sumFourDivisors(nums: IntArray): Int {
        var sum = 0
        for (num in nums) {
            val divisors = mutableListOf<Int>()
            for (i in 1..kotlin.math.sqrt(num.toDouble()).toInt()) {
                if (num % i == 0) {
                    divisors.add(i)
                    if (i * i != num) divisors.add(num / i)
                }
            }
            divisors.sort()
            if (divisors.size == 4) {
                sum += divisors.sum()
            }
        }
        return sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int sumFourDivisors(List<int> nums) {
        int sum = 0;
        for (int num in nums) {
            List<int> divisors = [];
            for (int i = 1; i * i <= num; i++) {
                if (num % i == 0) {
                    divisors.add(i);
                    if (i * i != num) divisors.add(num ~/ i);
                }
            }
            divisors.sort();
            if (divisors.length == 4) {
                sum += divisors.reduce((a, b) => a + b);
            }
        }
        return sum;
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
    "sort"
)

type Solution struct{}

func (s Solution) sumFourDivisors(nums []int) int {
    sum := 0
    for _, num := range nums {
        divisors := []int{}
        for i := 1; i*i <= num; i++ {
            if num%i == 0 {
                divisors = append(divisors, i)
                if i*i != num {
                    divisors = append(divisors, num/i)
                }
            }
        }
        sort.Ints(divisors)
        if len(divisors) == 4 {
            for _, d := range divisors {
                sum += d
            }
        }
    }
    return sum
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    def sum_four_divisors(nums)
        sum = 0
        nums.each do |num|
            divisors = []
            (1..Math.sqrt(num)).each do |i|
                if num % i == 0
                    divisors << i
                    divisors << num / i if i * i != num
                end
            end
            divisors.sort!
            if divisors.size == 4
                sum += divisors.sum
            end
        end
        sum
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def sumFourDivisors(nums: Array[Int]): Int = {
        var sum = 0
        for (num <- nums) {
            val divisors = (1 to math.sqrt(num).toInt).filter(i => num % i == 0).flatMap(i => List(i, num / i)).distinct.sorted
            if (divisors.length == 4) sum += divisors.sum
        }
        sum
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
    pub fn sum_four_divisors(nums: Vec<i32>) -> i32 {
        let mut sum = 0;
        for num in nums {
            let mut divisors: Vec<i32> = Vec::new();
            for i in 1..=(num as f64).sqrt() as i32 {
                if num % i == 0 {
                    divisors.push(i);
                    if i * i != num {
                        divisors.push(num / i);
                    }
                }
            }
            divisors.sort();
            if divisors.len() == 4 {
                sum += divisors.iter().sum::<i32>();
            }
        }
        sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define (sum-four-divisors nums)
    (let loop ((nums nums) (sum 0))
        (if (null? nums)
            sum
            (let ((num (car nums))
                  (divisors (filter (lambda (i) (zero? (remainder num i)))
                                  (range 1 (add1 (sqrt num))))))
                (loop (cdr nums)
                     (if (= (length divisors) 4)
                         (+ sum (apply + divisors))
                         sum))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
sum_four_divisors(Nums) ->
    sum_four_divisors(Nums, 0).

sum_four_divisors([], Sum) -> Sum;
sum_four_divisors([Num | Nums], Sum) ->
    Divisors = [I || I <- lists:seq(1, trunc(math:sqrt(Num))), Num rem I == 0],
    case length(Divisors) of
        4 -> sum_four_divisors(Nums, Sum + lists:sum(Divisors));
        _ -> sum_four_divisors(Nums, Sum)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
def sum_four_divisors(nums) do
    sum_four_divisors(nums, 0)
end

defp sum_four_divisors([], sum), do: sum

defp sum_four_divisors([num | nums], sum) do
    divisors = for i <- 1..:math.sqrt(num), rem(num, i) == 0, do: i
    if length(divisors) == 4, do: sum_four_divisors(nums, sum + Enum.sum(divisors)),
    else: sum_four_divisors(nums, sum)
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this solution is O(n * sqrt(m)), where n is the number of elements in the array and m is the maximum value in the array. This is because for each number in the array, we are potentially looping up to its square root to find its divisors.

- **Space Complexity:** The space complexity of this solution is O(1), as we are only using a constant amount of space to store the total sum and the count of divisors for each number. We are not using any data structures that scale with the input size.

</div>
</details>
