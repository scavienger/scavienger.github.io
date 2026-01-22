---
layout: post
title: "Minimum Pair Removal to Sort Array I"
date: 2026-01-22 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Hash Table", "Linked List", "Heap (Priority Queue)", "Simulation", "Doubly-Linked List", "Ordered Set"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool isNonDecreasing(const std::vector<int>&\
        \ arr) {\n        for (size_t i = 0; i + 1 < arr.size(); ++i) {\n          \
        \  if (arr[i] > arr[i+1]) {\n                return false;\n            }\n\
        \        }\n        return true;\n    }\n\n    int minimumPairRemoval(std::vector<int>&\
        \ nums) {\n        int operations = 0;\n\n        while (!isNonDecreasing(nums))\
        \ {\n            int min_sum = std::numeric_limits<int>::max();\n          \
        \  int min_idx = -1;\n\n            for (size_t i = 0; i + 1 < nums.size();\
        \ ++i) {\n                int current_pair_sum = nums[i] + nums[i+1];\n    \
        \            if (current_pair_sum < min_sum) {\n                    min_sum\
        \ = current_pair_sum;\n                    min_idx = i;\n                }\n\
        \            }\n\n            nums[min_idx] = min_sum;\n            nums.erase(nums.begin()\
        \ + min_idx + 1);\n            operations++;\n        }\n\n        return operations;\n\
        \    }\n};"
      java: "import java.util.ArrayList;\nimport java.util.List;\n\nclass Solution {\n\
        \    private boolean isNonDecreasing(List<Integer> arr) {\n        for (int\
        \ i = 0; i < arr.size() - 1; i++) {\n            if (arr.get(i) > arr.get(i+1))\
        \ {\n                return false;\n            }\n        }\n        return\
        \ true;\n    }\n\n    public int minimumPairRemoval(int[] numsArray) {\n   \
        \     int operations = 0;\n\n        List<Integer> nums = new ArrayList<>();\n\
        \        for (int num : numsArray) {\n            nums.add(num);\n        }\n\
        \n        while (!isNonDecreasing(nums)) {\n            int minSum = Integer.MAX_VALUE;\n\
        \            int minIdx = -1;\n\n            for (int i = 0; i < nums.size()\
        \ - 1; i++) {\n                int currentPairSum = nums.get(i) + nums.get(i+1);\n\
        \                if (currentPairSum < minSum) {\n                    minSum\
        \ = currentPairSum;\n                    minIdx = i;\n                }\n  \
        \          }\n\n            nums.set(minIdx, minSum);\n            nums.remove(minIdx\
        \ + 1);\n            operations++;\n        }\n\n        return operations;\n\
        \    }\n}"
      python: "class Solution(object):\n    def minimumPairRemoval(self, nums):\n  \
        \      \"\"\"\n        :type nums: List[int]\n        :rtype: int\n        \"\
        \"\"\n        operations = 0\n\n        def is_non_decreasing(arr):\n      \
        \      for i in range(len(arr) - 1):\n                if arr[i] > arr[i+1]:\n\
        \                    return False\n            return True\n\n        current_nums\
        \ = list(nums)\n\n        while not is_non_decreasing(current_nums):\n     \
        \       min_sum = float('inf')\n            min_idx = -1\n\n            for\
        \ i in range(len(current_nums) - 1):\n                current_pair_sum = current_nums[i]\
        \ + current_nums[i+1]\n                if current_pair_sum < min_sum:\n    \
        \                min_sum = current_pair_sum\n                    min_idx = i\n\
        \n            current_nums[min_idx] = min_sum\n            current_nums.pop(min_idx\
        \ + 1)\n            operations += 1\n\n        return operations"
      python3: "class Solution:\n    def minimumPairRemoval(self, nums: List[int]) ->\
        \ int:\n        operations = 0\n\n        def is_non_decreasing(arr):\n    \
        \        for i in range(len(arr) - 1):\n                if arr[i] > arr[i+1]:\n\
        \                    return False\n            return True\n\n        current_nums\
        \ = list(nums)\n\n        while not is_non_decreasing(current_nums):\n     \
        \       min_sum = float('inf')\n            min_idx = -1\n\n            for\
        \ i in range(len(current_nums) - 1):\n                current_pair_sum = current_nums[i]\
        \ + current_nums[i+1]\n                if current_pair_sum < min_sum:\n    \
        \                min_sum = current_pair_sum\n                    min_idx = i\n\
        \n            current_nums[min_idx] = min_sum\n            current_nums.pop(min_idx\
        \ + 1)\n            operations += 1\n\n        return operations"
      c: "#include <stdbool.h>\n#include <limits.h> // For INT_MAX\n#include <string.h>\
        \ // For memcpy\n\nbool isNonDecreasing(int* arr, int size) {\n    if (size\
        \ <= 1) {\n        return true;\n    }\n    for (int i = 0; i < size - 1; i++)\
        \ {\n        if (arr[i] > arr[i+1]) {\n            return false;\n        }\n\
        \    }\n    return true;\n}\n\nint minimumPairRemoval(int* nums, int numsSize)\
        \ {\n    int operations = 0;\n\n    int current_nums[50];\n    memcpy(current_nums,\
        \ nums, numsSize * sizeof(int));\n    int current_size = numsSize;\n\n    while\
        \ (!isNonDecreasing(current_nums, current_size)) {\n        int min_sum = INT_MAX;\n\
        \        int min_idx = -1;\n\n        for (int i = 0; i < current_size - 1;\
        \ i++) {\n            int current_pair_sum = current_nums[i] + current_nums[i+1];\n\
        \            if (current_pair_sum < min_sum) {\n                min_sum = current_pair_sum;\n\
        \                min_idx = i;\n            }\n        }\n\n        current_nums[min_idx]\
        \ = min_sum;\n\n        for (int k = min_idx + 1; k < current_size - 1; k++)\
        \ {\n            current_nums[k] = current_nums[k+1];\n        }\n        current_size--;\n\
        \        operations++;\n    }\n\n    return operations;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\nusing System.Linq;\n\
        \npublic class Solution {\n    private bool IsNonDecreasing(List<int> arr) {\n\
        \        for (int i = 0; i < arr.Count - 1; i++) {\n            if (arr[i] >\
        \ arr[i+1]) {\n                return false;\n            }\n        }\n   \
        \     return true;\n    }\n\n    public int MinimumPairRemoval(int[] numsArray)\
        \ {\n        int operations = 0;\n\n        List<int> nums = new List<int>(numsArray);\n\
        \n        while (!IsNonDecreasing(nums)) {\n            int minSum = int.MaxValue;\n\
        \            int minIdx = -1;\n\n            for (int i = 0; i < nums.Count\
        \ - 1; i++) {\n                int currentPairSum = nums[i] + nums[i+1];\n \
        \               if (currentPairSum < minSum) {\n                    minSum =\
        \ currentPairSum;\n                    minIdx = i;\n                }\n    \
        \        }\n\n            nums[minIdx] = minSum;\n            nums.RemoveAt(minIdx\
        \ + 1);\n            operations++;\n        }\n\n        return operations;\n\
        \    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar minimumPairRemoval\
        \ = function(nums) {\n    let operations = 0;\n\n    const isNonDecreasing =\
        \ (arr) => {\n        for (let i = 0; i < arr.length - 1; i++) {\n         \
        \   if (arr[i] > arr[i+1]) {\n                return false;\n            }\n\
        \        }\n        return true;\n    };\n\n    let currentNums = [...nums];\
        \ \n\n    while (!isNonDecreasing(currentNums)) {\n        let minSum = Number.MAX_SAFE_INTEGER;\n\
        \        let minIdx = -1;\n\n        for (let i = 0; i < currentNums.length\
        \ - 1; i++) {\n            let currentPairSum = currentNums[i] + currentNums[i+1];\n\
        \            if (currentPairSum < minSum) {\n                minSum = currentPairSum;\n\
        \                minIdx = i;\n            }\n        }\n\n        currentNums.splice(minIdx,\
        \ 2, minSum); \n        operations++;\n    }\n\n    return operations;\n};"
      typescript: "function minimumPairRemoval(nums: number[]): number {\n    let operations:\
        \ number = 0;\n\n    const isNonDecreasing = (arr: number[]): boolean => {\n\
        \        for (let i = 0; i < arr.length - 1; i++) {\n            if (arr[i]\
        \ > arr[i+1]) {\n                return false;\n            }\n        }\n \
        \       return true;\n    };\n\n    let currentNums: number[] = [...nums]; \n\
        \n    while (!isNonDecreasing(currentNums)) {\n        let minSum: number =\
        \ Number.MAX_SAFE_INTEGER;\n        let minIdx: number = -1;\n\n        for\
        \ (let i = 0; i < currentNums.length - 1; i++) {\n            let currentPairSum:\
        \ number = currentNums[i] + currentNums[i+1];\n            if (currentPairSum\
        \ < minSum) {\n                minSum = currentPairSum;\n                minIdx\
        \ = i;\n            }\n        }\n\n        currentNums.splice(minIdx, 2, minSum);\
        \ \n        operations++;\n    }\n\n    return operations;\n};"
      php: "<?php\n\nclass Solution {\n\n    /**\n     * @param Integer[] $nums\n  \
        \   * @return Integer\n     */\n    function minimumPairRemoval($nums) {\n \
        \       $operations = 0;\n\n        $isNonDecreasing = function($arr) {\n  \
        \          for ($i = 0; $i < count($arr) - 1; $i++) {\n                if ($arr[$i]\
        \ > $arr[$i+1]) {\n                    return false;\n                }\n  \
        \          }\n            return true;\n        };\n\n        $currentNums =\
        \ $nums; \n\n        while (!$isNonDecreasing($currentNums)) {\n           \
        \ $minSum = PHP_INT_MAX;\n            $minIdx = -1;\n\n            for ($i =\
        \ 0; $i < count($currentNums) - 1; $i++) {\n                $currentPairSum\
        \ = $currentNums[$i] + $currentNums[$i+1];\n                if ($currentPairSum\
        \ < $minSum) {\n                    $minSum = $currentPairSum;\n           \
        \         $minIdx = $i;\n                }\n            }\n\n            array_splice($currentNums,\
        \ $minIdx, 2, [$minSum]); \n            $operations++;\n        }\n\n      \
        \  return $operations;\n    }\n}"
      swift: "class Solution {\n    func minimumPairRemoval(_ nums: [Int]) -> Int {\n\
        \        var operations = 0\n\n        func isNonDecreasing(_ arr: [Int]) ->\
        \ Bool {\n            for i in 0..<arr.count - 1 {\n                if arr[i]\
        \ > arr[i+1] {\n                    return false\n                }\n      \
        \      }\n            return true\n        }\n\n        var currentNums = nums\n\
        \n        while !isNonDecreasing(currentNums) {\n            var minSum = Int.max\n\
        \            var minIdx = -1\n\n            for i in 0..<currentNums.count -\
        \ 1 {\n                let currentPairSum = currentNums[i] + currentNums[i+1]\n\
        \                if currentPairSum < minSum {\n                    minSum =\
        \ currentPairSum\n                    minIdx = i\n                }\n      \
        \      }\n\n            currentNums[minIdx] = minSum\n            currentNums.remove(at:\
        \ minIdx + 1)\n            operations += 1\n        }\n\n        return operations\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun minimumPairRemoval(nums: IntArray): Int {\n\
        \        var currentNums = nums.toMutableList()\n        var operations = 0\n\
        \n        while (true) {\n            if (currentNums.size <= 1) {\n       \
        \         break\n            }\n            var nonDecreasing = true\n     \
        \       for (i in 0 until currentNums.size - 1) {\n                if (currentNums[i]\
        \ > currentNums[i+1]) {\n                    nonDecreasing = false\n       \
        \             break\n                }\n            }\n            if (nonDecreasing)\
        \ {\n                break\n            }\n\n            var minSum = Int.MAX_VALUE\n\
        \            var minIdx = -1\n\n            for (i in 0 until currentNums.size\
        \ - 1) {\n                val currentSum = currentNums[i] + currentNums[i+1]\n\
        \                if (currentSum < minSum) {\n                    minSum = currentSum\n\
        \                    minIdx = i\n                }\n            }\n\n      \
        \      val sumVal = currentNums[minIdx] + currentNums[minIdx+1]\n          \
        \  currentNums.removeAt(minIdx)\n            currentNums.removeAt(minIdx)\n\
        \            currentNums.add(minIdx, sumVal)\n\n            operations++\n \
        \       }\n\n        return operations\n    }\n}"
      dart: "class Solution {\n  int minimumPairRemoval(List<int> nums) {\n    List<int>\
        \ currentNums = List.from(nums);\n    int operations = 0;\n\n    while (true)\
        \ {\n      if (currentNums.length <= 1) {\n        break;\n      }\n      bool\
        \ nonDecreasing = true;\n      for (int i = 0; i < currentNums.length - 1; i++)\
        \ {\n        if (currentNums[i] > currentNums[i+1]) {\n          nonDecreasing\
        \ = false;\n          break;\n        }\n      }\n      if (nonDecreasing) {\n\
        \        break;\n      }\n\n      int minSum = 2147483647; // Max int value\n\
        \      int minIdx = -1;\n\n      for (int i = 0; i < currentNums.length - 1;\
        \ i++) {\n        int currentSum = currentNums[i] + currentNums[i+1];\n    \
        \    if (currentSum < minSum) {\n          minSum = currentSum;\n          minIdx\
        \ = i;\n        }\n      }\n\n      int sumVal = currentNums[minIdx] + currentNums[minIdx+1];\n\
        \      currentNums.removeAt(minIdx);\n      currentNums.removeAt(minIdx);\n\
        \      currentNums.insert(minIdx, sumVal);\n\n      operations++;\n    }\n\n\
        \    return operations;\n  }\n}"
      go: "func minimumPairRemoval(nums []int) int {\n    currentNums := make([]int,\
        \ len(nums))\n    copy(currentNums, nums)\n\n    operations := 0\n\n    for\
        \ {\n        if len(currentNums) <= 1 {\n            break\n        }\n    \
        \    nonDecreasing := true\n        for i := 0; i < len(currentNums)-1; i++\
        \ {\n            if currentNums[i] > currentNums[i+1] {\n                nonDecreasing\
        \ = false\n                break\n            }\n        }\n        if nonDecreasing\
        \ {\n            break\n        }\n\n        minSum := 2147483647 // Max int\
        \ value\n        minIdx := -1\n\n        for i := 0; i < len(currentNums)-1;\
        \ i++ {\n            currentSum := currentNums[i] + currentNums[i+1]\n     \
        \       if currentSum < minSum {\n                minSum = currentSum\n    \
        \            minIdx = i\n            }\n        }\n\n        sumVal := currentNums[minIdx]\
        \ + currentNums[minIdx+1]\n\n        newNums := make([]int, 0, len(currentNums)-1)\n\
        \        newNums = append(newNums, currentNums[:minIdx]...)\n        newNums\
        \ = append(newNums, sumVal)\n        newNums = append(newNums, currentNums[minIdx+2:]...)\n\
        \        currentNums = newNums\n\n        operations++\n    }\n\n    return\
        \ operations\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef minimum_pair_removal(nums)\n\
        \    current_nums = nums.dup\n    operations = 0\n\n    loop do\n        if\
        \ current_nums.length <= 1\n            break\n        end\n        non_decreasing\
        \ = true\n        (0...current_nums.length - 1).each do |i|\n            if\
        \ current_nums[i] > current_nums[i+1]\n                non_decreasing = false\n\
        \                break\n            end\n        end\n        if non_decreasing\n\
        \            break\n        end\n\n        min_sum = Float::INFINITY\n     \
        \   min_idx = -1\n\n        (0...current_nums.length - 1).each do |i|\n    \
        \        current_sum = current_nums[i] + current_nums[i+1]\n            if current_sum\
        \ < min_sum\n                min_sum = current_sum\n                min_idx\
        \ = i\n            end\n        end\n\n        sum_val = current_nums[min_idx]\
        \ + current_nums[min_idx+1]\n        current_nums.delete_at(min_idx)\n     \
        \   current_nums.delete_at(min_idx)\n        current_nums.insert(min_idx, sum_val)\n\
        \n        operations += 1\n    end\n\n    return operations\nend"
      scala: "object Solution {\n    def minimumPairRemoval(nums: Array[Int]): Int =\
        \ {\n        import scala.collection.mutable.ArrayBuffer\n        import scala.util.control.Breaks._\n\
        \n        var currentNums = ArrayBuffer.from(nums)\n        var operations =\
        \ 0\n\n        breakable {\n            while (true) {\n                if (currentNums.length\
        \ <= 1) {\n                    break\n                }\n                var\
        \ nonDecreasing = true\n                for (i <- 0 until currentNums.length\
        \ - 1) {\n                    if (currentNums(i) > currentNums(i+1)) {\n   \
        \                     nonDecreasing = false\n                        break\n\
        \                    }\n                }\n                if (nonDecreasing)\
        \ {\n                    break\n                }\n\n                var minSum\
        \ = Int.MaxValue\n                var minIdx = -1\n\n                for (i\
        \ <- 0 until currentNums.length - 1) {\n                    val currentSum =\
        \ currentNums(i) + currentNums(i+1)\n                    if (currentSum < minSum)\
        \ {\n                        minSum = currentSum\n                        minIdx\
        \ = i\n                    }\n                }\n\n                val sumVal\
        \ = currentNums(minIdx) + currentNums(minIdx+1)\n                currentNums.remove(minIdx)\n\
        \                currentNums.remove(minIdx)\n                currentNums.insert(minIdx,\
        \ sumVal)\n\n                operations += 1\n            }\n        }\n\n \
        \       operations\n    }\n}"
      rust: "impl Solution {\n    pub fn minimum_pair_removal(nums: Vec<i32>) -> i32\
        \ {\n        let mut current_nums: Vec<i32> = nums.to_vec();\n        let mut\
        \ operations = 0;\n\n        loop {\n            if current_nums.len() <= 1\
        \ {\n                break;\n            }\n            let mut non_decreasing\
        \ = true;\n            for i in 0..current_nums.len() - 1 {\n              \
        \  if current_nums[i] > current_nums[i+1] {\n                    non_decreasing\
        \ = false;\n                    break;\n                }\n            }\n \
        \           if non_decreasing {\n                break;\n            }\n\n \
        \           let mut min_sum = i32::MAX;\n            let mut min_idx = -1;\n\
        \n            for i in 0..current_nums.len() - 1 {\n                let current_sum\
        \ = current_nums[i] + current_nums[i+1];\n                if current_sum < min_sum\
        \ {\n                    min_sum = current_sum;\n                    min_idx\
        \ = i as i32;\n                }\n            }\n\n            let min_idx_usize\
        \ = min_idx as usize;\n            let sum_val = current_nums[min_idx_usize]\
        \ + current_nums[min_idx_usize+1];\n            current_nums.remove(min_idx_usize);\n\
        \            current_nums.remove(min_idx_usize);\n            current_nums.insert(min_idx_usize,\
        \ sum_val);\n\n            operations += 1;\n        }\n\n        operations\n\
        \    }\n}"
      racket: "(define/contract (minimum-pair-removal nums)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let loop ((current-nums nums) (operations 0))\n    (define\
        \ (is-non-decreasing lst)\n      (cond\n        ((<= (length lst) 1) #t)\n \
        \       (else\n         (for/and ((i (in-range (- (length lst) 1))))\n     \
        \      (<= (list-ref lst i) (list-ref lst (+ i 1)))))))\n\n    (if (is-non-decreasing\
        \ current-nums)\n        operations\n        (let* ((min-sum +inf.0)\n     \
        \          (min-idx -1)\n               (len (length current-nums)))\n     \
        \     (for ((i (in-range (- len 1))))\n            (let ((current-sum (+ (list-ref\
        \ current-nums i) (list-ref current-nums (+ i 1)))))              (when (< current-sum\
        \ min-sum)\n                (set! min-sum current-sum)\n                (set!\
        \ min-idx i))))\n\n          (let* ((sum-val (+ (list-ref current-nums min-idx)\
        \ (list-ref current-nums (+ min-idx 1))))\n                 (new-nums (append\
        \ (take current-nums min-idx)\n                                   (list sum-val)\n\
        \                                   (drop current-nums (+ min-idx 2)))))\n \
        \           (loop new-nums (+ operations 1)))))))"
      erlang: "-spec minimum_pair_removal(Nums :: [integer()]) -> integer().\nminimum_pair_removal(Nums)\
        \ ->\n    solve(Nums, 0).\n\nsolve(Nums, Operations) ->\n    case is_non_decreasing(Nums)\
        \ of\n        true -> Operations;\n        false ->\n            {MinSum, MinIdx}\
        \ = find_min_pair(Nums),\n            SumVal = lists:nth(MinIdx + 1, Nums) +\
        \ lists:nth(MinIdx + 2, Nums),\n            NewNums = remove_and_insert(Nums,\
        \ MinIdx, SumVal),\n            solve(NewNums, Operations + 1)\n    end.\n\n\
        is_non_decreasing(Nums) when length(Nums) =< 1 -> true;\nis_non_decreasing([H|T])\
        \ ->\n    is_non_decreasing_recursive(H, T).\n\nis_non_decreasing_recursive(_,\
        \ []) -> true;\nis_non_decreasing_recursive(Prev, [H|T]) ->\n    if\n      \
        \  Prev =< H -> is_non_decreasing_recursive(H, T);\n        true -> false\n\
        \    end.\n\nfind_min_pair(Nums) ->\n    Len = length(Nums),\n    find_min_pair_loop(Nums,\
        \ 0, Len - 2, 2147483647, -1).\n\nfind_min_pair_loop(_Nums, Idx, MaxIdx, MinSum,\
        \ MinIdx) when Idx > MaxIdx ->\n    {MinSum, MinIdx};\nfind_min_pair_loop(Nums,\
        \ Idx, MaxIdx, AccMinSum, AccMinIdx) ->\n    A = lists:nth(Idx + 1, Nums),\n\
        \    B = lists:nth(Idx + 2, Nums),\n    CurrentSum = A + B,\n    if\n      \
        \  CurrentSum < AccMinSum ->\n            find_min_pair_loop(Nums, Idx + 1,\
        \ MaxIdx, CurrentSum, Idx);\n        true ->\n            find_min_pair_loop(Nums,\
        \ Idx + 1, MaxIdx, AccMinSum, AccMinIdx)\n    end.\n\nremove_and_insert(List,\
        \ Idx, Val) ->\n    {Prefix, Rest} = lists:split(Idx, List),\n    {_RemovedPair,\
        \ Suffix} = lists:split(2, Rest),\n    Prefix ++ [Val] ++ Suffix."
      elixir: "defmodule Solution do\n  @spec minimum_pair_removal(nums :: [integer])\
        \ :: integer\n  def minimum_pair_removal(nums) do\n    solve(nums, 0)\n  end\n\
        \n  defp solve(nums, operations) do\n    if is_non_decreasing(nums) do\n   \
        \   operations\n    else\n      {min_sum, min_idx} = find_min_pair(nums)\n \
        \     sum_val = Enum.at(nums, min_idx) + Enum.at(nums, min_idx + 1)\n      new_nums\
        \ = remove_and_insert(nums, min_idx, sum_val)\n      solve(new_nums, operations\
        \ + 1)\n    end\n  end\n\n  defp is_non_decreasing(nums) do\n    if length(nums)\
        \ <= 1 do\n      true\n    else\n      is_non_decreasing_recursive(Enum.at(nums,\
        \ 0), Enum.drop(nums, 1))\n    end\n  end\n\n  defp is_non_decreasing_recursive(_prev,\
        \ []), do: true\n  defp is_non_decreasing_recursive(prev, [head | tail]) do\n\
        \    if prev <= head do\n      is_non_decreasing_recursive(head, tail)\n   \
        \ else\n      false\n    end\n  end\n\n  defp find_min_pair(nums) do\n    len\
        \ = length(nums)\n    find_min_pair_loop(nums, 0, len - 2, 2_147_483_647, -1)\n\
        \  end\n\n  defp find_min_pair_loop(_nums, idx, max_idx, min_sum, min_idx) when\
        \ idx > max_idx do\n    {min_sum, min_idx}\n  end\n  defp find_min_pair_loop(nums,\
        \ idx, max_idx, acc_min_sum, acc_min_idx) do\n    a = Enum.at(nums, idx)\n \
        \   b = Enum.at(nums, idx + 1)\n    current_sum = a + b\n    if current_sum\
        \ < acc_min_sum do\n      find_min_pair_loop(nums, idx + 1, max_idx, current_sum,\
        \ idx)\n    else\n      find_min_pair_loop(nums, idx + 1, max_idx, acc_min_sum,\
        \ acc_min_idx)\n    end\n  end\n\n  defp remove_and_insert(list, idx, val) do\n\
        \    {prefix, rest} = Enum.split(list, idx)\n    {_removed_pair, suffix} = Enum.split(rest,\
        \ 2)\n    prefix ++ [val] ++ suffix\n  end\nend"
    approach: 'The problem is solved by simulating the described operations until the
      array becomes non-decreasing. We initialize an operation counter to zero. In a
      loop, we first check if the current array is already non-decreasing. If it is,
      we break the loop and return the accumulated operations. If not, we iterate through
      all adjacent pairs in the array to find the one with the minimum sum, prioritizing
      the leftmost pair in case of ties.


      Once the minimum sum pair and its starting index are identified, we perform the
      operation: the first element of the pair is replaced by the sum, and the second
      element of the pair is removed from the array. The operation counter is then incremented.
      This process continues, reducing the array''s length by one in each step, until
      the non-decreasing condition is met.'
    time_complexity: The time complexity is O(N^3), where N is the initial length of
      the nums array. In the worst case, the array length decreases by one in each of
      N-1 operations. Each operation involves iterating through the current array to
      check if it's non-decreasing (O(L)), and then again to find the minimum sum pair
      (O(L)), where L is the current array length. Finally, modifying the array (e.g.,
      removing an element in the middle of a list or vector) can take O(L) time. Since
      L decreases from N down to 2, the total time complexity is approximately proportional
      to the sum of L for each step, multiplied by L for each step, resulting in O(N^3).
    space_complexity: The space complexity is O(N), where N is the initial length of
      the nums array. This is primarily for storing a mutable copy of the input array,
      which can grow up to the initial size N. In languages like C, where dynamic arrays
      are not built-in, a fixed-size array of maximum possible N elements is used. The
      helper function isNonDecreasing operates on the existing array and does not require
      significant additional space.
    elapsed_time: 84.97725987434387
    model: gemini-2.5-flash
    generated_at: '2026-01-22 01:12:38 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int minimumPairRemoval(vector<int>& nums)\
        \ {\n        int n = nums.size();\n        int operations = 0;\n        while\
        \ (!isNonDecreasing(nums)) {\n            int minSum = INT_MAX;\n          \
        \  int minIndex = -1;\n            for (int i = 0; i < n - 1; i++) {\n     \
        \           int sum = nums[i] + nums[i + 1];\n                if (sum < minSum)\
        \ {\n                    minSum = sum;\n                    minIndex = i;\n\
        \                }\n            }\n            nums.erase(nums.begin() + minIndex\
        \ + 1);\n            nums[minIndex] = minSum;\n            n--;\n          \
        \  operations++;\n        }\n        return operations;\n    }\n    bool isNonDecreasing(vector<int>&\
        \ nums) {\n        for (int i = 0; i < nums.size() - 1; i++) {\n           \
        \ if (nums[i] > nums[i + 1]) {\n                return false;\n            }\n\
        \        }\n        return true;\n    }\n};"
      java: "class Solution {\n    public int minimumPairRemoval(int[] nums) {\n   \
        \     int n = nums.length;\n        int operations = 0;\n        while (!isNonDecreasing(nums))\
        \ {\n            int minSum = Integer.MAX_VALUE;\n            int minIndex =\
        \ -1;\n            for (int i = 0; i < n - 1; i++) {\n                int sum\
        \ = nums[i] + nums[i + 1];\n                if (sum < minSum) {\n          \
        \          minSum = sum;\n                    minIndex = i;\n              \
        \  }\n            }\n            int[] newNums = new int[n - 1];\n         \
        \   System.arraycopy(nums, 0, newNums, 0, minIndex);\n            newNums[minIndex]\
        \ = minSum;\n            System.arraycopy(nums, minIndex + 2, newNums, minIndex\
        \ + 1, n - minIndex - 2);\n            nums = newNums;\n            n--;\n \
        \           operations++;\n        }\n        return operations;\n    }\n  \
        \  boolean isNonDecreasing(int[] nums) {\n        for (int i = 0; i < nums.length\
        \ - 1; i++) {\n            if (nums[i] > nums[i + 1]) {\n                return\
        \ false;\n            }\n        }\n        return true;\n    }\n}"
      python: "class Solution(object):\n    def minimumPairRemoval(self, nums):\n  \
        \      n = len(nums)\n        operations = 0\n        while not self.isNonDecreasing(nums):\n\
        \            minSum = float('inf')\n            minIndex = -1\n            for\
        \ i in range(n - 1):\n                sum = nums[i] + nums[i + 1]\n        \
        \        if sum < minSum:\n                    minSum = sum\n              \
        \      minIndex = i\n            nums.pop(minIndex + 1)\n            nums[minIndex]\
        \ = minSum\n            n -= 1\n            operations += 1\n        return\
        \ operations\n    def isNonDecreasing(self, nums):\n        for i in range(len(nums)\
        \ - 1):\n            if nums[i] > nums[i + 1]:\n                return False\n\
        \        return True"
      python3: "class Solution:\n    def minimumPairRemoval(self, nums: list[int]) ->\
        \ int:\n        n = len(nums)\n        operations = 0\n        while not self.isNonDecreasing(nums):\n\
        \            minSum = float('inf')\n            minIndex = -1\n            for\
        \ i in range(n - 1):\n                sum = nums[i] + nums[i + 1]\n        \
        \        if sum < minSum:\n                    minSum = sum\n              \
        \      minIndex = i\n            nums.pop(minIndex + 1)\n            nums[minIndex]\
        \ = minSum\n            n -= 1\n            operations += 1\n        return\
        \ operations\n    def isNonDecreasing(self, nums: list[int]) -> bool:\n    \
        \    for i in range(len(nums) - 1):\n            if nums[i] > nums[i + 1]:\n\
        \                return False\n        return True"
      c: "int minimumPairRemoval(int* nums, int numsSize) {\n    int operations = 0;\n\
        \    while (!isNonDecreasing(nums, numsSize)) {\n        int minSum = INT_MAX;\n\
        \        int minIndex = -1;\n        for (int i = 0; i < numsSize - 1; i++)\
        \ {\n            int sum = nums[i] + nums[i + 1];\n            if (sum < minSum)\
        \ {\n                minSum = sum;\n                minIndex = i;\n        \
        \    }\n        }\n        int* newNums = (int*)malloc((numsSize - 1) * sizeof(int));\n\
        \        for (int i = 0; i < minIndex; i++) {\n            newNums[i] = nums[i];\n\
        \        }\n        newNums[minIndex] = minSum;\n        for (int i = minIndex\
        \ + 1; i < numsSize - 1; i++) {\n            newNums[i] = nums[i + 1];\n   \
        \     }\n        free(nums);\n        nums = newNums;\n        numsSize--;\n\
        \        operations++;\n    }\n    return operations;\n}\nint isNonDecreasing(int*\
        \ nums, int numsSize) {\n    for (int i = 0; i < numsSize - 1; i++) {\n    \
        \    if (nums[i] > nums[i + 1]) {\n            return 0;\n        }\n    }\n\
        \    return 1;\n}"
      csharp: "public class Solution {\n    public int MinimumPairRemoval(int[] nums)\
        \ {\n        int n = nums.Length;\n        int operations = 0;\n        while\
        \ (!IsNonDecreasing(nums)) {\n            int minSum = int.MaxValue;\n     \
        \       int minIndex = -1;\n            for (int i = 0; i < n - 1; i++) {\n\
        \                int sum = nums[i] + nums[i + 1];\n                if (sum <\
        \ minSum) {\n                    minSum = sum;\n                    minIndex\
        \ = i;\n                }\n            }\n            int[] newNums = new int[n\
        \ - 1];\n            Array.Copy(nums, 0, newNums, 0, minIndex);\n          \
        \  newNums[minIndex] = minSum;\n            Array.Copy(nums, minIndex + 2, newNums,\
        \ minIndex + 1, n - minIndex - 2);\n            nums = newNums;\n          \
        \  n--;\n            operations++;\n        }\n        return operations;\n\
        \    }\n    bool IsNonDecreasing(int[] nums) {\n        for (int i = 0; i <\
        \ nums.Length - 1; i++) {\n            if (nums[i] > nums[i + 1]) {\n      \
        \          return false;\n            }\n        }\n        return true;\n \
        \   }\n}"
      javascript: "var minimumPairRemoval = function(nums) {\n    let n = nums.length;\n\
        \    let operations = 0;\n    while (!isNonDecreasing(nums)) {\n        let\
        \ minSum = Infinity;\n        let minIndex = -1;\n        for (let i = 0; i\
        \ < n - 1; i++) {\n            let sum = nums[i] + nums[i + 1];\n          \
        \  if (sum < minSum) {\n                minSum = sum;\n                minIndex\
        \ = i;\n            }\n        }\n        nums.splice(minIndex + 1, 1);\n  \
        \      nums[minIndex] = minSum;\n        n--;\n        operations++;\n    }\n\
        \    return operations;\n};\nfunction isNonDecreasing(nums) {\n    for (let\
        \ i = 0; i < nums.length - 1; i++) {\n        if (nums[i] > nums[i + 1]) {\n\
        \            return false;\n        }\n    }\n    return true;\n}"
      typescript: "function minimumPairRemoval(nums: number[]): number {\n    let n\
        \ = nums.length;\n    let operations = 0;\n    while (!isNonDecreasing(nums))\
        \ {\n        let minSum = Infinity;\n        let minIndex = -1;\n        for\
        \ (let i = 0; i < n - 1; i++) {\n            let sum = nums[i] + nums[i + 1];\n\
        \            if (sum < minSum) {\n                minSum = sum;\n          \
        \      minIndex = i;\n            }\n        }\n        nums.splice(minIndex\
        \ + 1, 1);\n        nums[minIndex] = minSum;\n        n--;\n        operations++;\n\
        \    }\n    return operations;\n}\nfunction isNonDecreasing(nums: number[]):\
        \ boolean {\n    for (let i = 0; i < nums.length - 1; i++) {\n        if (nums[i]\
        \ > nums[i + 1]) {\n            return false;\n        }\n    }\n    return\
        \ true;\n}"
      php: "class Solution {\n    function minimumPairRemoval($nums) {\n        $n =\
        \ count($nums);\n        $operations = 0;\n        while (!$this->isNonDecreasing($nums))\
        \ {\n            $minSum = PHP_INT_MAX;\n            $minIndex = -1;\n     \
        \       for ($i = 0; $i < $n - 1; $i++) {\n                $sum = $nums[$i]\
        \ + $nums[$i + 1];\n                if ($sum < $minSum) {\n                \
        \    $minSum = $sum;\n                    $minIndex = $i;\n                }\n\
        \            }\n            array_splice($nums, $minIndex + 1, 1);\n       \
        \     $nums[$minIndex] = $minSum;\n            $n--;\n            $operations++;\n\
        \        }\n        return $operations;\n    }\n    function isNonDecreasing($nums)\
        \ {\n        for ($i = 0; $i < count($nums) - 1; $i++) {\n            if ($nums[$i]\
        \ > $nums[$i + 1]) {\n                return false;\n            }\n       \
        \ }\n        return true;\n    }\n}"
      swift: "class Solution {\n    func minimumPairRemoval(_ nums: [Int]) -> Int {\n\
        \        var nums = nums\n        var n = nums.count\n        var operations\
        \ = 0\n        while !isNonDecreasing(nums) {\n            var minSum = Int.max\n\
        \            var minIndex = -1\n            for i in 0..<n - 1 {\n         \
        \       let sum = nums[i] + nums[i + 1]\n                if sum < minSum {\n\
        \                    minSum = sum\n                    minIndex = i\n      \
        \          }\n            }\n            nums.remove(at: minIndex + 1)\n   \
        \         nums[minIndex] = minSum\n            n -= 1\n            operations\
        \ += 1\n        }\n        return operations\n    }\n    func isNonDecreasing(_\
        \ nums: [Int]) -> Bool {\n        for i in 0..<nums.count - 1 {\n          \
        \  if nums[i] > nums[i + 1] {\n                return false\n            }\n\
        \        }\n        return true\n    }\n}"
      kotlin: "class Solution {\n    fun minimumPairRemoval(nums: IntArray): Int {\n\
        \        var operations = 0\n        var numsList = nums.toList()\n        while\
        \ (!isNonDecreasing(numsList)) {\n            var minSum = Int.MAX_VALUE\n \
        \           var minIndex = -1\n            for (i in 0 until numsList.size -\
        \ 1) {\n                val sum = numsList[i] + numsList[i + 1]\n          \
        \      if (sum < minSum) {\n                    minSum = sum\n             \
        \       minIndex = i\n                }\n            }\n            numsList\
        \ = numsList.subList(0, minIndex) + listOf(minSum) + numsList.subList(minIndex\
        \ + 2, numsList.size)\n            operations++\n        }\n        return operations\n\
        \    }\n\n    private fun isNonDecreasing(nums: List<Int>): Boolean {\n    \
        \    for (i in 0 until nums.size - 1) {\n            if (nums[i] > nums[i +\
        \ 1]) return false\n        }\n        return true\n    }\n}"
      dart: "class Solution {\n  int minimumPairRemoval(List<int> nums) {\n    int operations\
        \ = 0;\n    List<int> numsList = List.from(nums);\n    while (!isNonDecreasing(numsList))\
        \ {\n      int minSum = int.maxFinite;\n      int minIndex = -1;\n      for\
        \ (int i = 0; i < numsList.length - 1; i++) {\n        int sum = numsList[i]\
        \ + numsList[i + 1];\n        if (sum < minSum) {\n          minSum = sum;\n\
        \          minIndex = i;\n        }\n      }\n      numsList = [...numsList.sublist(0,\
        \ minIndex), minSum, ...numsList.sublist(minIndex + 2)];\n      operations++;\n\
        \    }\n    return operations;\n  }\n\n  bool isNonDecreasing(List<int> nums)\
        \ {\n    for (int i = 0; i < nums.length - 1; i++) {\n      if (nums[i] > nums[i\
        \ + 1]) return false;\n    }\n    return true;\n  }\n}"
      go: "func minimumPairRemoval(nums []int) int {\n    operations := 0\n    for !isNonDecreasing(nums)\
        \ {\n        minSum := 1000000\n        minIndex := -1\n        for i := 0;\
        \ i < len(nums)-1; i++ {\n            sum := nums[i] + nums[i+1]\n         \
        \   if sum < minSum {\n                minSum = sum\n                minIndex\
        \ = i\n            }\n        }\n        nums = append(append(nums[:minIndex],\
        \ []int{minSum}), nums[minIndex+2:]...)\n        operations++\n    }\n    return\
        \ operations\n}\n\nfunc isNonDecreasing(nums []int) bool {\n    for i := 0;\
        \ i < len(nums)-1; i++ {\n        if nums[i] > nums[i+1] {\n            return\
        \ false\n        }\n    }\n    return true\n}"
      ruby: "def minimum_pair_removal(nums)\n    operations = 0\n    while !is_non_decreasing(nums)\n\
        \        min_sum = 1000000\n        min_index = -1\n        (0...nums.size -\
        \ 1).each do |i|\n            sum = nums[i] + nums[i + 1]\n            if sum\
        \ < min_sum\n                min_sum = sum\n                min_index = i\n\
        \            end\n\n        end\n        nums = nums[0...min_index] + [min_sum]\
        \ + nums[min_index + 2..-1]\n        operations += 1\n    end\n    operations\n\
        end\n\nprivate\n\ndef is_non_decreasing(nums)\n    (0...nums.size - 1).each\
        \ do |i|\n        return false if nums[i] > nums[i + 1]\n    end\n    true\n\
        end"
      scala: "object Solution {\n    def minimumPairRemoval(nums: Array[Int]): Int =\
        \ {\n        var operations = 0\n        var numsList = nums.toList\n      \
        \  while (!isNonDecreasing(numsList)) {\n            var minSum = Int.MaxValue\n\
        \            var minIndex = -1\n            for (i <- 0 until numsList.size\
        \ - 1) {\n                val sum = numsList(i) + numsList(i + 1)\n        \
        \        if (sum < minSum) {\n                    minSum = sum\n           \
        \         minIndex = i\n                }\n            }\n            numsList\
        \ = numsList.take(minIndex) ::: List(minSum) ::: numsList.drop(minIndex + 2)\n\
        \            operations += 1\n        }\n        operations\n    }\n\n    private\
        \ def isNonDecreasing(nums: List[Int]): Boolean = {\n        for (i <- 0 until\
        \ nums.size - 1) {\n            if (nums(i) > nums(i + 1)) return false\n  \
        \      }\n        true\n    }\n}"
      rust: "impl Solution {\n    pub fn minimum_pair_removal(nums: Vec<i32>) -> i32\
        \ {\n        let mut operations = 0;\n        let mut nums_list = nums;\n  \
        \      while !is_non_decreasing(&nums_list) {\n            let mut min_sum =\
        \ i32::MAX;\n            let mut min_index = -1;\n            for i in 0..nums_list.len()\
        \ - 1 {\n                let sum = nums_list[i] + nums_list[i + 1];\n      \
        \          if sum < min_sum {\n                    min_sum = sum;\n        \
        \            min_index = i as i32;\n                }\n            }\n     \
        \       nums_list = nums_list[..min_index as usize].iter().cloned().chain(std::iter::once(min_sum)).chain(nums_list[(min_index\
        \ + 2) as usize..].iter().cloned()).collect::<Vec<i32>>();\n            operations\
        \ += 1;\n        }\n        operations\n    }\n}\n\nfn is_non_decreasing(nums:\
        \ &Vec<i32>) -> bool {\n    for i in 0..nums.len() - 1 {\n        if nums[i]\
        \ > nums[i + 1] {\n            return false;\n        }\n    }\n    true\n}"
      racket: "(define/contract (minimum-pair-removal nums)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let loop ((nums nums) (operations 0))\n    (if (is-non-decreasing?\
        \ nums)\n        operations\n        (let ((min-sum (apply min (map (lambda\
        \ (i) (+ (list-ref nums i) (list-ref nums (add1 i)))) (range 0 (sub1 (length\
        \ nums))))))\n              (min-index (let loop ((i 0))\n                 \
        \          (if (= (+ (list-ref nums i) (list-ref nums (add1 i))) min-sum)\n\
        \                               i\n                               (loop (add1\
        \ i))))))\n          (loop (append (take nums min-index) (list min-sum) (drop\
        \ nums (add1 (add1 min-index)))) (add1 operations))))))\n\n(define (is-non-decreasing?\
        \ nums)\n  (let loop ((nums nums))\n    (or (null? (cdr nums))\n        (and\
        \ (<= (car nums) (cadr nums))\n             (loop (cdr nums))))))"
      erlang: "minimum_pair_removal(Nums) ->\n    Operations =\n        lists:foldl(\n\
        \            fun(_, Acc) ->\n                case is_non_decreasing(Nums) of\n\
        \                    true -> Acc;\n                    false ->\n          \
        \              {MinSum, MinIndex} = find_min_sum(Nums),\n                  \
        \      NewNums = lists:sublist(Nums, 1, MinIndex) ++ [MinSum] ++ lists:sublist(Nums,\
        \ MinIndex + 2, length(Nums)),\n                        Acc + 1\n          \
        \      end\n            end,\n            0,\n            [Nums]).\n\nfind_min_sum(Nums)\
        \ ->\n    find_min_sum(Nums, 0, {1000000, -1}).\n\nfind_min_sum([H1, H2 | T],\
        \ Index, {MinSum, MinIndex}) ->\n    Sum = H1 + H2,\n    case Sum < MinSum of\n\
        \        true -> find_min_sum([H2 | T], Index + 1, {Sum, Index});\n        false\
        \ -> find_min_sum([H2 | T], Index + 1, {MinSum, MinIndex})\n    end;\nfind_min_sum(_,\
        \ _, Acc) -> Acc.\n\nis_non_decreasing([H1, H2 | T]) ->\n    case H1 =< H2 of\n\
        \        true -> is_non_decreasing([H2 | T]);\n        false -> false\n    end;\n\
        \nis_non_decreasing(_) -> true."
      elixir: "defmodule Solution do\n  @spec minimum_pair_removal(nums :: [integer])\
        \ :: integer\n  def minimum_pair_removal(nums) do\n    operations = 0\n    nums_list\
        \ = nums\n    while !is_non_decreasing(nums_list) do\n      {min_sum, min_index}\
        \ = find_min_sum(nums_list)\n      nums_list = Enum.take(nums_list, min_index)\
        \ ++ [min_sum] ++ Enum.drop(nums_list, min_index + 2)\n      operations = operations\
        \ + 1\n    end\n    operations\n  end\n\n  defp find_min_sum(nums) do\n    find_min_sum(nums,\
        \ 0, {1000000, -1})\n  end\n\n  defp find_min_sum([h1, h2 | t], index, {min_sum,\
        \ min_index}) do\n    sum = h1 + h2\n    if sum < min_sum do\n      find_min_sum([h2\
        \ | t], index + 1, {sum, index})\n    else\n      find_min_sum([h2 | t], index\
        \ + 1, {min_sum, min_index})\n    end\n  end\n\n  defp find_min_sum(_, _, acc),\
        \ do: acc\n\n  defp is_non_decreasing([h1, h2 | t]) do\n    if h1 <= h2 do\n\
        \      is_non_decreasing([h2 | t])\n    else\n      false\n    end\n  end\n\n\
        \  defp is_non_decreasing(_), do: true\nend"
    approach: 'The problem can be solved by simulating the operations. We start by finding
      the pair with the minimum sum in the array. If multiple such pairs exist, we choose
      the leftmost one. We then replace the pair with their sum and repeat the process
      until the array becomes non-decreasing. The key intuition here is to always choose
      the pair with the minimum sum, as this will minimize the number of operations
      needed to make the array non-decreasing.


      The algorithm works by maintaining a list of pairs and their sums. We iterate
      through the array to find the pair with the minimum sum, and then replace the
      pair with their sum. We repeat this process until the array becomes non-decreasing.
      The number of operations is incremented each time a pair is replaced. The algorithm
      terminates when the array becomes non-decreasing, at which point the number of
      operations is returned as the result.'
    time_complexity: O(n^2) where n is the length of the input array. This is because
      in the worst case, we need to iterate through the array for each operation, and
      there can be up to n operations.
    space_complexity: O(n) where n is the length of the input array. This is because
      we need to store the array and the pairs, which can take up to n space.
    elapsed_time: 11.04439115524292
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-22 01:12:54 '
---

## Problem #3507: Minimum Pair Removal to Sort Array I

**Difficulty:** Easy

**Topics:** Array, Hash Table, Linked List, Heap (Priority Queue), Simulation, Doubly-Linked List, Ordered Set

## Problem Description

<p>Given an array <code>nums</code>, you can perform the following operation any number of times:</p>

<ul>
	<li>Select the <strong>adjacent</strong> pair with the <strong>minimum</strong> sum in <code>nums</code>. If multiple such pairs exist, choose the leftmost one.</li>
	<li>Replace the pair with their sum.</li>
</ul>

<p>Return the <strong>minimum number of operations</strong> needed to make the array <strong>non-decreasing</strong>.</p>

<p>An array is said to be <strong>non-decreasing</strong> if each element is greater than or equal to its previous element (if it exists).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,2,3,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The pair <code>(3,1)</code> has the minimum sum of 4. After replacement, <code>nums = [5,2,4]</code>.</li>
	<li>The pair <code>(2,4)</code> has the minimum sum of 6. After replacement, <code>nums = [5,6]</code>.</li>
</ul>

<p>The array <code>nums</code> became non-decreasing in two operations.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>The array <code>nums</code> is already sorted.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50</code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


## Hints

1. Simulate the operations

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2026-01-22 01:12:38 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem is solved by simulating the described operations until the array becomes non-decreasing. We initialize an operation counter to zero. In a loop, we first check if the current array is already non-decreasing. If it is, we break the loop and return the accumulated operations. If not, we iterate through all adjacent pairs in the array to find the one with the minimum sum, prioritizing the leftmost pair in case of ties.

Once the minimum sum pair and its starting index are identified, we perform the operation: the first element of the pair is replaced by the sum, and the second element of the pair is removed from the array. The operation counter is then incremented. This process continues, reducing the array's length by one in each step, until the non-decreasing condition is met.

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
    bool isNonDecreasing(const std::vector<int>& arr) {
        for (size_t i = 0; i + 1 < arr.size(); ++i) {
            if (arr[i] > arr[i+1]) {
                return false;
            }
        }
        return true;
    }

    int minimumPairRemoval(std::vector<int>& nums) {
        int operations = 0;

        while (!isNonDecreasing(nums)) {
            int min_sum = std::numeric_limits<int>::max();
            int min_idx = -1;

            for (size_t i = 0; i + 1 < nums.size(); ++i) {
                int current_pair_sum = nums[i] + nums[i+1];
                if (current_pair_sum < min_sum) {
                    min_sum = current_pair_sum;
                    min_idx = i;
                }
            }

            nums[min_idx] = min_sum;
            nums.erase(nums.begin() + min_idx + 1);
            operations++;
        }

        return operations;
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
    private boolean isNonDecreasing(List<Integer> arr) {
        for (int i = 0; i < arr.size() - 1; i++) {
            if (arr.get(i) > arr.get(i+1)) {
                return false;
            }
        }
        return true;
    }

    public int minimumPairRemoval(int[] numsArray) {
        int operations = 0;

        List<Integer> nums = new ArrayList<>();
        for (int num : numsArray) {
            nums.add(num);
        }

        while (!isNonDecreasing(nums)) {
            int minSum = Integer.MAX_VALUE;
            int minIdx = -1;

            for (int i = 0; i < nums.size() - 1; i++) {
                int currentPairSum = nums.get(i) + nums.get(i+1);
                if (currentPairSum < minSum) {
                    minSum = currentPairSum;
                    minIdx = i;
                }
            }

            nums.set(minIdx, minSum);
            nums.remove(minIdx + 1);
            operations++;
        }

        return operations;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        operations = 0

        def is_non_decreasing(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i+1]:
                    return False
            return True

        current_nums = list(nums)

        while not is_non_decreasing(current_nums):
            min_sum = float('inf')
            min_idx = -1

            for i in range(len(current_nums) - 1):
                current_pair_sum = current_nums[i] + current_nums[i+1]
                if current_pair_sum < min_sum:
                    min_sum = current_pair_sum
                    min_idx = i

            current_nums[min_idx] = min_sum
            current_nums.pop(min_idx + 1)
            operations += 1

        return operations
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operations = 0

        def is_non_decreasing(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i+1]:
                    return False
            return True

        current_nums = list(nums)

        while not is_non_decreasing(current_nums):
            min_sum = float('inf')
            min_idx = -1

            for i in range(len(current_nums) - 1):
                current_pair_sum = current_nums[i] + current_nums[i+1]
                if current_pair_sum < min_sum:
                    min_sum = current_pair_sum
                    min_idx = i

            current_nums[min_idx] = min_sum
            current_nums.pop(min_idx + 1)
            operations += 1

        return operations
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdbool.h>
#include <limits.h> // For INT_MAX
#include <string.h> // For memcpy

bool isNonDecreasing(int* arr, int size) {
    if (size <= 1) {
        return true;
    }
    for (int i = 0; i < size - 1; i++) {
        if (arr[i] > arr[i+1]) {
            return false;
        }
    }
    return true;
}

int minimumPairRemoval(int* nums, int numsSize) {
    int operations = 0;

    int current_nums[50];
    memcpy(current_nums, nums, numsSize * sizeof(int));
    int current_size = numsSize;

    while (!isNonDecreasing(current_nums, current_size)) {
        int min_sum = INT_MAX;
        int min_idx = -1;

        for (int i = 0; i < current_size - 1; i++) {
            int current_pair_sum = current_nums[i] + current_nums[i+1];
            if (current_pair_sum < min_sum) {
                min_sum = current_pair_sum;
                min_idx = i;
            }
        }

        current_nums[min_idx] = min_sum;

        for (int k = min_idx + 1; k < current_size - 1; k++) {
            current_nums[k] = current_nums[k+1];
        }
        current_size--;
        operations++;
    }

    return operations;
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
    private bool IsNonDecreasing(List<int> arr) {
        for (int i = 0; i < arr.Count - 1; i++) {
            if (arr[i] > arr[i+1]) {
                return false;
            }
        }
        return true;
    }

    public int MinimumPairRemoval(int[] numsArray) {
        int operations = 0;

        List<int> nums = new List<int>(numsArray);

        while (!IsNonDecreasing(nums)) {
            int minSum = int.MaxValue;
            int minIdx = -1;

            for (int i = 0; i < nums.Count - 1; i++) {
                int currentPairSum = nums[i] + nums[i+1];
                if (currentPairSum < minSum) {
                    minSum = currentPairSum;
                    minIdx = i;
                }
            }

            nums[minIdx] = minSum;
            nums.RemoveAt(minIdx + 1);
            operations++;
        }

        return operations;
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
var minimumPairRemoval = function(nums) {
    let operations = 0;

    const isNonDecreasing = (arr) => {
        for (let i = 0; i < arr.length - 1; i++) {
            if (arr[i] > arr[i+1]) {
                return false;
            }
        }
        return true;
    };

    let currentNums = [...nums]; 

    while (!isNonDecreasing(currentNums)) {
        let minSum = Number.MAX_SAFE_INTEGER;
        let minIdx = -1;

        for (let i = 0; i < currentNums.length - 1; i++) {
            let currentPairSum = currentNums[i] + currentNums[i+1];
            if (currentPairSum < minSum) {
                minSum = currentPairSum;
                minIdx = i;
            }
        }

        currentNums.splice(minIdx, 2, minSum); 
        operations++;
    }

    return operations;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimumPairRemoval(nums: number[]): number {
    let operations: number = 0;

    const isNonDecreasing = (arr: number[]): boolean => {
        for (let i = 0; i < arr.length - 1; i++) {
            if (arr[i] > arr[i+1]) {
                return false;
            }
        }
        return true;
    };

    let currentNums: number[] = [...nums]; 

    while (!isNonDecreasing(currentNums)) {
        let minSum: number = Number.MAX_SAFE_INTEGER;
        let minIdx: number = -1;

        for (let i = 0; i < currentNums.length - 1; i++) {
            let currentPairSum: number = currentNums[i] + currentNums[i+1];
            if (currentPairSum < minSum) {
                minSum = currentPairSum;
                minIdx = i;
            }
        }

        currentNums.splice(minIdx, 2, minSum); 
        operations++;
    }

    return operations;
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
    function minimumPairRemoval($nums) {
        $operations = 0;

        $isNonDecreasing = function($arr) {
            for ($i = 0; $i < count($arr) - 1; $i++) {
                if ($arr[$i] > $arr[$i+1]) {
                    return false;
                }
            }
            return true;
        };

        $currentNums = $nums; 

        while (!$isNonDecreasing($currentNums)) {
            $minSum = PHP_INT_MAX;
            $minIdx = -1;

            for ($i = 0; $i < count($currentNums) - 1; $i++) {
                $currentPairSum = $currentNums[$i] + $currentNums[$i+1];
                if ($currentPairSum < $minSum) {
                    $minSum = $currentPairSum;
                    $minIdx = $i;
                }
            }

            array_splice($currentNums, $minIdx, 2, [$minSum]); 
            $operations++;
        }

        return $operations;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minimumPairRemoval(_ nums: [Int]) -> Int {
        var operations = 0

        func isNonDecreasing(_ arr: [Int]) -> Bool {
            for i in 0..<arr.count - 1 {
                if arr[i] > arr[i+1] {
                    return false
                }
            }
            return true
        }

        var currentNums = nums

        while !isNonDecreasing(currentNums) {
            var minSum = Int.max
            var minIdx = -1

            for i in 0..<currentNums.count - 1 {
                let currentPairSum = currentNums[i] + currentNums[i+1]
                if currentPairSum < minSum {
                    minSum = currentPairSum
                    minIdx = i
                }
            }

            currentNums[minIdx] = minSum
            currentNums.remove(at: minIdx + 1)
            operations += 1
        }

        return operations
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minimumPairRemoval(nums: IntArray): Int {
        var currentNums = nums.toMutableList()
        var operations = 0

        while (true) {
            if (currentNums.size <= 1) {
                break
            }
            var nonDecreasing = true
            for (i in 0 until currentNums.size - 1) {
                if (currentNums[i] > currentNums[i+1]) {
                    nonDecreasing = false
                    break
                }
            }
            if (nonDecreasing) {
                break
            }

            var minSum = Int.MAX_VALUE
            var minIdx = -1

            for (i in 0 until currentNums.size - 1) {
                val currentSum = currentNums[i] + currentNums[i+1]
                if (currentSum < minSum) {
                    minSum = currentSum
                    minIdx = i
                }
            }

            val sumVal = currentNums[minIdx] + currentNums[minIdx+1]
            currentNums.removeAt(minIdx)
            currentNums.removeAt(minIdx)
            currentNums.add(minIdx, sumVal)

            operations++
        }

        return operations
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minimumPairRemoval(List<int> nums) {
    List<int> currentNums = List.from(nums);
    int operations = 0;

    while (true) {
      if (currentNums.length <= 1) {
        break;
      }
      bool nonDecreasing = true;
      for (int i = 0; i < currentNums.length - 1; i++) {
        if (currentNums[i] > currentNums[i+1]) {
          nonDecreasing = false;
          break;
        }
      }
      if (nonDecreasing) {
        break;
      }

      int minSum = 2147483647; // Max int value
      int minIdx = -1;

      for (int i = 0; i < currentNums.length - 1; i++) {
        int currentSum = currentNums[i] + currentNums[i+1];
        if (currentSum < minSum) {
          minSum = currentSum;
          minIdx = i;
        }
      }

      int sumVal = currentNums[minIdx] + currentNums[minIdx+1];
      currentNums.removeAt(minIdx);
      currentNums.removeAt(minIdx);
      currentNums.insert(minIdx, sumVal);

      operations++;
    }

    return operations;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minimumPairRemoval(nums []int) int {
    currentNums := make([]int, len(nums))
    copy(currentNums, nums)

    operations := 0

    for {
        if len(currentNums) <= 1 {
            break
        }
        nonDecreasing := true
        for i := 0; i < len(currentNums)-1; i++ {
            if currentNums[i] > currentNums[i+1] {
                nonDecreasing = false
                break
            }
        }
        if nonDecreasing {
            break
        }

        minSum := 2147483647 // Max int value
        minIdx := -1

        for i := 0; i < len(currentNums)-1; i++ {
            currentSum := currentNums[i] + currentNums[i+1]
            if currentSum < minSum {
                minSum = currentSum
                minIdx = i
            }
        }

        sumVal := currentNums[minIdx] + currentNums[minIdx+1]

        newNums := make([]int, 0, len(currentNums)-1)
        newNums = append(newNums, currentNums[:minIdx]...)
        newNums = append(newNums, sumVal)
        newNums = append(newNums, currentNums[minIdx+2:]...)
        currentNums = newNums

        operations++
    }

    return operations
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def minimum_pair_removal(nums)
    current_nums = nums.dup
    operations = 0

    loop do
        if current_nums.length <= 1
            break
        end
        non_decreasing = true
        (0...current_nums.length - 1).each do |i|
            if current_nums[i] > current_nums[i+1]
                non_decreasing = false
                break
            end
        end
        if non_decreasing
            break
        end

        min_sum = Float::INFINITY
        min_idx = -1

        (0...current_nums.length - 1).each do |i|
            current_sum = current_nums[i] + current_nums[i+1]
            if current_sum < min_sum
                min_sum = current_sum
                min_idx = i
            end
        end

        sum_val = current_nums[min_idx] + current_nums[min_idx+1]
        current_nums.delete_at(min_idx)
        current_nums.delete_at(min_idx)
        current_nums.insert(min_idx, sum_val)

        operations += 1
    end

    return operations
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minimumPairRemoval(nums: Array[Int]): Int = {
        import scala.collection.mutable.ArrayBuffer
        import scala.util.control.Breaks._

        var currentNums = ArrayBuffer.from(nums)
        var operations = 0

        breakable {
            while (true) {
                if (currentNums.length <= 1) {
                    break
                }
                var nonDecreasing = true
                for (i <- 0 until currentNums.length - 1) {
                    if (currentNums(i) > currentNums(i+1)) {
                        nonDecreasing = false
                        break
                    }
                }
                if (nonDecreasing) {
                    break
                }

                var minSum = Int.MaxValue
                var minIdx = -1

                for (i <- 0 until currentNums.length - 1) {
                    val currentSum = currentNums(i) + currentNums(i+1)
                    if (currentSum < minSum) {
                        minSum = currentSum
                        minIdx = i
                    }
                }

                val sumVal = currentNums(minIdx) + currentNums(minIdx+1)
                currentNums.remove(minIdx)
                currentNums.remove(minIdx)
                currentNums.insert(minIdx, sumVal)

                operations += 1
            }
        }

        operations
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn minimum_pair_removal(nums: Vec<i32>) -> i32 {
        let mut current_nums: Vec<i32> = nums.to_vec();
        let mut operations = 0;

        loop {
            if current_nums.len() <= 1 {
                break;
            }
            let mut non_decreasing = true;
            for i in 0..current_nums.len() - 1 {
                if current_nums[i] > current_nums[i+1] {
                    non_decreasing = false;
                    break;
                }
            }
            if non_decreasing {
                break;
            }

            let mut min_sum = i32::MAX;
            let mut min_idx = -1;

            for i in 0..current_nums.len() - 1 {
                let current_sum = current_nums[i] + current_nums[i+1];
                if current_sum < min_sum {
                    min_sum = current_sum;
                    min_idx = i as i32;
                }
            }

            let min_idx_usize = min_idx as usize;
            let sum_val = current_nums[min_idx_usize] + current_nums[min_idx_usize+1];
            current_nums.remove(min_idx_usize);
            current_nums.remove(min_idx_usize);
            current_nums.insert(min_idx_usize, sum_val);

            operations += 1;
        }

        operations
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (minimum-pair-removal nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((current-nums nums) (operations 0))
    (define (is-non-decreasing lst)
      (cond
        ((<= (length lst) 1) #t)
        (else
         (for/and ((i (in-range (- (length lst) 1))))
           (<= (list-ref lst i) (list-ref lst (+ i 1)))))))

    (if (is-non-decreasing current-nums)
        operations
        (let* ((min-sum +inf.0)
               (min-idx -1)
               (len (length current-nums)))
          (for ((i (in-range (- len 1))))
            (let ((current-sum (+ (list-ref current-nums i) (list-ref current-nums (+ i 1)))))              (when (< current-sum min-sum)
                (set! min-sum current-sum)
                (set! min-idx i))))

          (let* ((sum-val (+ (list-ref current-nums min-idx) (list-ref current-nums (+ min-idx 1))))
                 (new-nums (append (take current-nums min-idx)
                                   (list sum-val)
                                   (drop current-nums (+ min-idx 2)))))
            (loop new-nums (+ operations 1)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec minimum_pair_removal(Nums :: [integer()]) -> integer().
minimum_pair_removal(Nums) ->
    solve(Nums, 0).

solve(Nums, Operations) ->
    case is_non_decreasing(Nums) of
        true -> Operations;
        false ->
            {MinSum, MinIdx} = find_min_pair(Nums),
            SumVal = lists:nth(MinIdx + 1, Nums) + lists:nth(MinIdx + 2, Nums),
            NewNums = remove_and_insert(Nums, MinIdx, SumVal),
            solve(NewNums, Operations + 1)
    end.

is_non_decreasing(Nums) when length(Nums) =< 1 -> true;
is_non_decreasing([H|T]) ->
    is_non_decreasing_recursive(H, T).

is_non_decreasing_recursive(_, []) -> true;
is_non_decreasing_recursive(Prev, [H|T]) ->
    if
        Prev =< H -> is_non_decreasing_recursive(H, T);
        true -> false
    end.

find_min_pair(Nums) ->
    Len = length(Nums),
    find_min_pair_loop(Nums, 0, Len - 2, 2147483647, -1).

find_min_pair_loop(_Nums, Idx, MaxIdx, MinSum, MinIdx) when Idx > MaxIdx ->
    {MinSum, MinIdx};
find_min_pair_loop(Nums, Idx, MaxIdx, AccMinSum, AccMinIdx) ->
    A = lists:nth(Idx + 1, Nums),
    B = lists:nth(Idx + 2, Nums),
    CurrentSum = A + B,
    if
        CurrentSum < AccMinSum ->
            find_min_pair_loop(Nums, Idx + 1, MaxIdx, CurrentSum, Idx);
        true ->
            find_min_pair_loop(Nums, Idx + 1, MaxIdx, AccMinSum, AccMinIdx)
    end.

remove_and_insert(List, Idx, Val) ->
    {Prefix, Rest} = lists:split(Idx, List),
    {_RemovedPair, Suffix} = lists:split(2, Rest),
    Prefix ++ [Val] ++ Suffix.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_pair_removal(nums :: [integer]) :: integer
  def minimum_pair_removal(nums) do
    solve(nums, 0)
  end

  defp solve(nums, operations) do
    if is_non_decreasing(nums) do
      operations
    else
      {min_sum, min_idx} = find_min_pair(nums)
      sum_val = Enum.at(nums, min_idx) + Enum.at(nums, min_idx + 1)
      new_nums = remove_and_insert(nums, min_idx, sum_val)
      solve(new_nums, operations + 1)
    end
  end

  defp is_non_decreasing(nums) do
    if length(nums) <= 1 do
      true
    else
      is_non_decreasing_recursive(Enum.at(nums, 0), Enum.drop(nums, 1))
    end
  end

  defp is_non_decreasing_recursive(_prev, []), do: true
  defp is_non_decreasing_recursive(prev, [head | tail]) do
    if prev <= head do
      is_non_decreasing_recursive(head, tail)
    else
      false
    end
  end

  defp find_min_pair(nums) do
    len = length(nums)
    find_min_pair_loop(nums, 0, len - 2, 2_147_483_647, -1)
  end

  defp find_min_pair_loop(_nums, idx, max_idx, min_sum, min_idx) when idx > max_idx do
    {min_sum, min_idx}
  end
  defp find_min_pair_loop(nums, idx, max_idx, acc_min_sum, acc_min_idx) do
    a = Enum.at(nums, idx)
    b = Enum.at(nums, idx + 1)
    current_sum = a + b
    if current_sum < acc_min_sum do
      find_min_pair_loop(nums, idx + 1, max_idx, current_sum, idx)
    else
      find_min_pair_loop(nums, idx + 1, max_idx, acc_min_sum, acc_min_idx)
    end
  end

  defp remove_and_insert(list, idx, val) do
    {prefix, rest} = Enum.split(list, idx)
    {_removed_pair, suffix} = Enum.split(rest, 2)
    prefix ++ [val] ++ suffix
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N^3), where N is the initial length of the nums array. In the worst case, the array length decreases by one in each of N-1 operations. Each operation involves iterating through the current array to check if it's non-decreasing (O(L)), and then again to find the minimum sum pair (O(L)), where L is the current array length. Finally, modifying the array (e.g., removing an element in the middle of a list or vector) can take O(L) time. Since L decreases from N down to 2, the total time complexity is approximately proportional to the sum of L for each step, multiplied by L for each step, resulting in O(N^3).

- **Space Complexity:** The space complexity is O(N), where N is the initial length of the nums array. This is primarily for storing a mutable copy of the input array, which can grow up to the initial size N. In languages like C, where dynamic arrays are not built-in, a fixed-size array of maximum possible N elements is used. The helper function isNonDecreasing operates on the existing array and does not require significant additional space.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-22 01:12:54 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by simulating the operations. We start by finding the pair with the minimum sum in the array. If multiple such pairs exist, we choose the leftmost one. We then replace the pair with their sum and repeat the process until the array becomes non-decreasing. The key intuition here is to always choose the pair with the minimum sum, as this will minimize the number of operations needed to make the array non-decreasing.

The algorithm works by maintaining a list of pairs and their sums. We iterate through the array to find the pair with the minimum sum, and then replace the pair with their sum. We repeat this process until the array becomes non-decreasing. The number of operations is incremented each time a pair is replaced. The algorithm terminates when the array becomes non-decreasing, at which point the number of operations is returned as the result.

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
    int minimumPairRemoval(vector<int>& nums) {
        int n = nums.size();
        int operations = 0;
        while (!isNonDecreasing(nums)) {
            int minSum = INT_MAX;
            int minIndex = -1;
            for (int i = 0; i < n - 1; i++) {
                int sum = nums[i] + nums[i + 1];
                if (sum < minSum) {
                    minSum = sum;
                    minIndex = i;
                }
            }
            nums.erase(nums.begin() + minIndex + 1);
            nums[minIndex] = minSum;
            n--;
            operations++;
        }
        return operations;
    }
    bool isNonDecreasing(vector<int>& nums) {
        for (int i = 0; i < nums.size() - 1; i++) {
            if (nums[i] > nums[i + 1]) {
                return false;
            }
        }
        return true;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minimumPairRemoval(int[] nums) {
        int n = nums.length;
        int operations = 0;
        while (!isNonDecreasing(nums)) {
            int minSum = Integer.MAX_VALUE;
            int minIndex = -1;
            for (int i = 0; i < n - 1; i++) {
                int sum = nums[i] + nums[i + 1];
                if (sum < minSum) {
                    minSum = sum;
                    minIndex = i;
                }
            }
            int[] newNums = new int[n - 1];
            System.arraycopy(nums, 0, newNums, 0, minIndex);
            newNums[minIndex] = minSum;
            System.arraycopy(nums, minIndex + 2, newNums, minIndex + 1, n - minIndex - 2);
            nums = newNums;
            n--;
            operations++;
        }
        return operations;
    }
    boolean isNonDecreasing(int[] nums) {
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] > nums[i + 1]) {
                return false;
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
class Solution(object):
    def minimumPairRemoval(self, nums):
        n = len(nums)
        operations = 0
        while not self.isNonDecreasing(nums):
            minSum = float('inf')
            minIndex = -1
            for i in range(n - 1):
                sum = nums[i] + nums[i + 1]
                if sum < minSum:
                    minSum = sum
                    minIndex = i
            nums.pop(minIndex + 1)
            nums[minIndex] = minSum
            n -= 1
            operations += 1
        return operations
    def isNonDecreasing(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        n = len(nums)
        operations = 0
        while not self.isNonDecreasing(nums):
            minSum = float('inf')
            minIndex = -1
            for i in range(n - 1):
                sum = nums[i] + nums[i + 1]
                if sum < minSum:
                    minSum = sum
                    minIndex = i
            nums.pop(minIndex + 1)
            nums[minIndex] = minSum
            n -= 1
            operations += 1
        return operations
    def isNonDecreasing(self, nums: list[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int minimumPairRemoval(int* nums, int numsSize) {
    int operations = 0;
    while (!isNonDecreasing(nums, numsSize)) {
        int minSum = INT_MAX;
        int minIndex = -1;
        for (int i = 0; i < numsSize - 1; i++) {
            int sum = nums[i] + nums[i + 1];
            if (sum < minSum) {
                minSum = sum;
                minIndex = i;
            }
        }
        int* newNums = (int*)malloc((numsSize - 1) * sizeof(int));
        for (int i = 0; i < minIndex; i++) {
            newNums[i] = nums[i];
        }
        newNums[minIndex] = minSum;
        for (int i = minIndex + 1; i < numsSize - 1; i++) {
            newNums[i] = nums[i + 1];
        }
        free(nums);
        nums = newNums;
        numsSize--;
        operations++;
    }
    return operations;
}
int isNonDecreasing(int* nums, int numsSize) {
    for (int i = 0; i < numsSize - 1; i++) {
        if (nums[i] > nums[i + 1]) {
            return 0;
        }
    }
    return 1;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinimumPairRemoval(int[] nums) {
        int n = nums.Length;
        int operations = 0;
        while (!IsNonDecreasing(nums)) {
            int minSum = int.MaxValue;
            int minIndex = -1;
            for (int i = 0; i < n - 1; i++) {
                int sum = nums[i] + nums[i + 1];
                if (sum < minSum) {
                    minSum = sum;
                    minIndex = i;
                }
            }
            int[] newNums = new int[n - 1];
            Array.Copy(nums, 0, newNums, 0, minIndex);
            newNums[minIndex] = minSum;
            Array.Copy(nums, minIndex + 2, newNums, minIndex + 1, n - minIndex - 2);
            nums = newNums;
            n--;
            operations++;
        }
        return operations;
    }
    bool IsNonDecreasing(int[] nums) {
        for (int i = 0; i < nums.Length - 1; i++) {
            if (nums[i] > nums[i + 1]) {
                return false;
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
var minimumPairRemoval = function(nums) {
    let n = nums.length;
    let operations = 0;
    while (!isNonDecreasing(nums)) {
        let minSum = Infinity;
        let minIndex = -1;
        for (let i = 0; i < n - 1; i++) {
            let sum = nums[i] + nums[i + 1];
            if (sum < minSum) {
                minSum = sum;
                minIndex = i;
            }
        }
        nums.splice(minIndex + 1, 1);
        nums[minIndex] = minSum;
        n--;
        operations++;
    }
    return operations;
};
function isNonDecreasing(nums) {
    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] > nums[i + 1]) {
            return false;
        }
    }
    return true;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimumPairRemoval(nums: number[]): number {
    let n = nums.length;
    let operations = 0;
    while (!isNonDecreasing(nums)) {
        let minSum = Infinity;
        let minIndex = -1;
        for (let i = 0; i < n - 1; i++) {
            let sum = nums[i] + nums[i + 1];
            if (sum < minSum) {
                minSum = sum;
                minIndex = i;
            }
        }
        nums.splice(minIndex + 1, 1);
        nums[minIndex] = minSum;
        n--;
        operations++;
    }
    return operations;
}
function isNonDecreasing(nums: number[]): boolean {
    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] > nums[i + 1]) {
            return false;
        }
    }
    return true;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function minimumPairRemoval($nums) {
        $n = count($nums);
        $operations = 0;
        while (!$this->isNonDecreasing($nums)) {
            $minSum = PHP_INT_MAX;
            $minIndex = -1;
            for ($i = 0; $i < $n - 1; $i++) {
                $sum = $nums[$i] + $nums[$i + 1];
                if ($sum < $minSum) {
                    $minSum = $sum;
                    $minIndex = $i;
                }
            }
            array_splice($nums, $minIndex + 1, 1);
            $nums[$minIndex] = $minSum;
            $n--;
            $operations++;
        }
        return $operations;
    }
    function isNonDecreasing($nums) {
        for ($i = 0; $i < count($nums) - 1; $i++) {
            if ($nums[$i] > $nums[$i + 1]) {
                return false;
            }
        }
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minimumPairRemoval(_ nums: [Int]) -> Int {
        var nums = nums
        var n = nums.count
        var operations = 0
        while !isNonDecreasing(nums) {
            var minSum = Int.max
            var minIndex = -1
            for i in 0..<n - 1 {
                let sum = nums[i] + nums[i + 1]
                if sum < minSum {
                    minSum = sum
                    minIndex = i
                }
            }
            nums.remove(at: minIndex + 1)
            nums[minIndex] = minSum
            n -= 1
            operations += 1
        }
        return operations
    }
    func isNonDecreasing(_ nums: [Int]) -> Bool {
        for i in 0..<nums.count - 1 {
            if nums[i] > nums[i + 1] {
                return false
            }
        }
        return true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minimumPairRemoval(nums: IntArray): Int {
        var operations = 0
        var numsList = nums.toList()
        while (!isNonDecreasing(numsList)) {
            var minSum = Int.MAX_VALUE
            var minIndex = -1
            for (i in 0 until numsList.size - 1) {
                val sum = numsList[i] + numsList[i + 1]
                if (sum < minSum) {
                    minSum = sum
                    minIndex = i
                }
            }
            numsList = numsList.subList(0, minIndex) + listOf(minSum) + numsList.subList(minIndex + 2, numsList.size)
            operations++
        }
        return operations
    }

    private fun isNonDecreasing(nums: List<Int>): Boolean {
        for (i in 0 until nums.size - 1) {
            if (nums[i] > nums[i + 1]) return false
        }
        return true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minimumPairRemoval(List<int> nums) {
    int operations = 0;
    List<int> numsList = List.from(nums);
    while (!isNonDecreasing(numsList)) {
      int minSum = int.maxFinite;
      int minIndex = -1;
      for (int i = 0; i < numsList.length - 1; i++) {
        int sum = numsList[i] + numsList[i + 1];
        if (sum < minSum) {
          minSum = sum;
          minIndex = i;
        }
      }
      numsList = [...numsList.sublist(0, minIndex), minSum, ...numsList.sublist(minIndex + 2)];
      operations++;
    }
    return operations;
  }

  bool isNonDecreasing(List<int> nums) {
    for (int i = 0; i < nums.length - 1; i++) {
      if (nums[i] > nums[i + 1]) return false;
    }
    return true;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minimumPairRemoval(nums []int) int {
    operations := 0
    for !isNonDecreasing(nums) {
        minSum := 1000000
        minIndex := -1
        for i := 0; i < len(nums)-1; i++ {
            sum := nums[i] + nums[i+1]
            if sum < minSum {
                minSum = sum
                minIndex = i
            }
        }
        nums = append(append(nums[:minIndex], []int{minSum}), nums[minIndex+2:]...)
        operations++
    }
    return operations
}

func isNonDecreasing(nums []int) bool {
    for i := 0; i < len(nums)-1; i++ {
        if nums[i] > nums[i+1] {
            return false
        }
    }
    return true
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def minimum_pair_removal(nums)
    operations = 0
    while !is_non_decreasing(nums)
        min_sum = 1000000
        min_index = -1
        (0...nums.size - 1).each do |i|
            sum = nums[i] + nums[i + 1]
            if sum < min_sum
                min_sum = sum
                min_index = i
            end

        end
        nums = nums[0...min_index] + [min_sum] + nums[min_index + 2..-1]
        operations += 1
    end
    operations
end

private

def is_non_decreasing(nums)
    (0...nums.size - 1).each do |i|
        return false if nums[i] > nums[i + 1]
    end
    true
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minimumPairRemoval(nums: Array[Int]): Int = {
        var operations = 0
        var numsList = nums.toList
        while (!isNonDecreasing(numsList)) {
            var minSum = Int.MaxValue
            var minIndex = -1
            for (i <- 0 until numsList.size - 1) {
                val sum = numsList(i) + numsList(i + 1)
                if (sum < minSum) {
                    minSum = sum
                    minIndex = i
                }
            }
            numsList = numsList.take(minIndex) ::: List(minSum) ::: numsList.drop(minIndex + 2)
            operations += 1
        }
        operations
    }

    private def isNonDecreasing(nums: List[Int]): Boolean = {
        for (i <- 0 until nums.size - 1) {
            if (nums(i) > nums(i + 1)) return false
        }
        true
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn minimum_pair_removal(nums: Vec<i32>) -> i32 {
        let mut operations = 0;
        let mut nums_list = nums;
        while !is_non_decreasing(&nums_list) {
            let mut min_sum = i32::MAX;
            let mut min_index = -1;
            for i in 0..nums_list.len() - 1 {
                let sum = nums_list[i] + nums_list[i + 1];
                if sum < min_sum {
                    min_sum = sum;
                    min_index = i as i32;
                }
            }
            nums_list = nums_list[..min_index as usize].iter().cloned().chain(std::iter::once(min_sum)).chain(nums_list[(min_index + 2) as usize..].iter().cloned()).collect::<Vec<i32>>();
            operations += 1;
        }
        operations
    }
}

fn is_non_decreasing(nums: &Vec<i32>) -> bool {
    for i in 0..nums.len() - 1 {
        if nums[i] > nums[i + 1] {
            return false;
        }
    }
    true
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (minimum-pair-removal nums)
  (-> (listof exact-integer?) exact-integer?)
  (let loop ((nums nums) (operations 0))
    (if (is-non-decreasing? nums)
        operations
        (let ((min-sum (apply min (map (lambda (i) (+ (list-ref nums i) (list-ref nums (add1 i)))) (range 0 (sub1 (length nums))))))
              (min-index (let loop ((i 0))
                           (if (= (+ (list-ref nums i) (list-ref nums (add1 i))) min-sum)
                               i
                               (loop (add1 i))))))
          (loop (append (take nums min-index) (list min-sum) (drop nums (add1 (add1 min-index)))) (add1 operations))))))

(define (is-non-decreasing? nums)
  (let loop ((nums nums))
    (or (null? (cdr nums))
        (and (<= (car nums) (cadr nums))
             (loop (cdr nums))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
minimum_pair_removal(Nums) ->
    Operations =
        lists:foldl(
            fun(_, Acc) ->
                case is_non_decreasing(Nums) of
                    true -> Acc;
                    false ->
                        {MinSum, MinIndex} = find_min_sum(Nums),
                        NewNums = lists:sublist(Nums, 1, MinIndex) ++ [MinSum] ++ lists:sublist(Nums, MinIndex + 2, length(Nums)),
                        Acc + 1
                end
            end,
            0,
            [Nums]).

find_min_sum(Nums) ->
    find_min_sum(Nums, 0, {1000000, -1}).

find_min_sum([H1, H2 | T], Index, {MinSum, MinIndex}) ->
    Sum = H1 + H2,
    case Sum < MinSum of
        true -> find_min_sum([H2 | T], Index + 1, {Sum, Index});
        false -> find_min_sum([H2 | T], Index + 1, {MinSum, MinIndex})
    end;
find_min_sum(_, _, Acc) -> Acc.

is_non_decreasing([H1, H2 | T]) ->
    case H1 =< H2 of
        true -> is_non_decreasing([H2 | T]);
        false -> false
    end;

is_non_decreasing(_) -> true.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec minimum_pair_removal(nums :: [integer]) :: integer
  def minimum_pair_removal(nums) do
    operations = 0
    nums_list = nums
    while !is_non_decreasing(nums_list) do
      {min_sum, min_index} = find_min_sum(nums_list)
      nums_list = Enum.take(nums_list, min_index) ++ [min_sum] ++ Enum.drop(nums_list, min_index + 2)
      operations = operations + 1
    end
    operations
  end

  defp find_min_sum(nums) do
    find_min_sum(nums, 0, {1000000, -1})
  end

  defp find_min_sum([h1, h2 | t], index, {min_sum, min_index}) do
    sum = h1 + h2
    if sum < min_sum do
      find_min_sum([h2 | t], index + 1, {sum, index})
    else
      find_min_sum([h2 | t], index + 1, {min_sum, min_index})
    end
  end

  defp find_min_sum(_, _, acc), do: acc

  defp is_non_decreasing([h1, h2 | t]) do
    if h1 <= h2 do
      is_non_decreasing([h2 | t])
    else
      false
    end
  end

  defp is_non_decreasing(_), do: true
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n^2) where n is the length of the input array. This is because in the worst case, we need to iterate through the array for each operation, and there can be up to n operations.

- **Space Complexity:** O(n) where n is the length of the input array. This is because we need to store the array and the pairs, which can take up to n space.

</div>
</details>
