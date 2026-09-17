---
layout: post
title: "Find Two Non-overlapping Sub-arrays Each With Target Sum"
date: 2026-09-17 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Binary Search", "Dynamic Programming", "Sliding Window"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minSumOfLengths(vector<int>& arr, int\
        \ target) {\n        int n = arr.size();\n        vector<int> best_so_far(n,\
        \ 1e9);\n        int left = 0, current_sum = 0, min_total_len = 1e9;\n\n   \
        \     for (int right = 0; right < n; ++right) {\n            current_sum +=\
        \ arr[right];\n            while (current_sum > target) {\n                current_sum\
        \ -= arr[left++];\n            }\n\n            if (current_sum == target) {\n\
        \                int current_len = right - left + 1;\n                if (left\
        \ > 0 && best_so_far[left - 1] != 1e9) {\n                    min_total_len\
        \ = min(min_total_len, current_len + best_so_far[left - 1]);\n             \
        \   }\n                best_so_far[right] = (right > 0) ? min(best_so_far[right\
        \ - 1], current_len) : current_len;\n            } else {\n                best_so_far[right]\
        \ = (right > 0) ? best_so_far[right - 1] : 1e9;\n            }\n        }\n\n\
        \        return (min_total_len >= 1e9) ? -1 : min_total_len;\n    }\n};"
      java: "class Solution {\n    public int minSumOfLengths(int[] arr, int target)\
        \ {\n        int n = arr.length;\n        int[] bestSoFar = new int[n];\n  \
        \      java.util.Arrays.fill(bestSoFar, Integer.MAX_VALUE / 2);\n        int\
        \ left = 0, currentSum = 0, minTotalLen = Integer.MAX_VALUE / 2;\n\n       \
        \ for (int right = 0; right < n; right++) {\n            currentSum += arr[right];\n\
        \            while (currentSum > target) {\n                currentSum -= arr[left++];\n\
        \            }\n\n            if (currentSum == target) {\n                int\
        \ currentLen = right - left + 1;\n                if (left > 0 && bestSoFar[left\
        \ - 1] != Integer.MAX_VALUE / 2) {\n                    minTotalLen = Math.min(minTotalLen,\
        \ currentLen + bestSoFar[left - 1]);\n                }\n                bestSoFar[right]\
        \ = (right > 0) ? Math.min(bestSoFar[right - 1], currentLen) : currentLen;\n\
        \            } else {\n                bestSoFar[right] = (right > 0) ? bestSoFar[right\
        \ - 1] : Integer.MAX_VALUE / 2;\n            }\n        }\n\n        return\
        \ (minTotalLen >= Integer.MAX_VALUE / 2) ? -1 : minTotalLen;\n    }\n}"
      python: "class Solution(object):\n    def minSumOfLengths(self, arr, target):\n\
        \        \"\"\"\n        :type arr: List[int]\n        :type target: int\n \
        \       :rtype: int\n        \"\"\"\n        n = len(arr)\n        best_so_far\
        \ = [float('inf')] * n\n        left = 0\n        current_sum = 0\n        min_total_len\
        \ = float('inf')\n\n        for right in range(n):\n            current_sum\
        \ += arr[right]\n            while current_sum > target:\n                current_sum\
        \ -= arr[left]\n                left += 1\n\n            if current_sum == target:\n\
        \                current_len = right - left + 1\n                if left > 0\
        \ and best_so_far[left - 1] != float('inf'):\n                    min_total_len\
        \ = min(min_total_len, current_len + best_so_far[left - 1])\n              \
        \  if right > 0:\n                    best_so_far[right] = min(best_so_far[right\
        \ - 1], current_len)\n                else:\n                    best_so_far[right]\
        \ = current_len\n            else:\n                if right > 0:\n        \
        \            best_so_far[right] = best_so_far[right - 1]\n\n        return min_total_len\
        \ if min_total_len != float('inf') else -1"
      python3: "class Solution:\n    def minSumOfLengths(self, arr: List[int], target:\
        \ int) -> int:\n        n = len(arr)\n        best_so_far = [float('inf')] *\
        \ n\n        left = 0\n        current_sum = 0\n        min_total_len = float('inf')\n\
        \n        for right in range(n):\n            current_sum += arr[right]\n  \
        \          while current_sum > target:\n                current_sum -= arr[left]\n\
        \                left += 1\n\n            if current_sum == target:\n      \
        \          current_len = right - left + 1\n                if left > 0 and best_so_far[left\
        \ - 1] != float('inf'):\n                    min_total_len = min(min_total_len,\
        \ current_len + best_so_far[left - 1])\n                best_so_far[right] =\
        \ min(best_so_far[right - 1], current_len) if right > 0 else current_len\n \
        \           else:\n                if right > 0:\n                    best_so_far[right]\
        \ = best_so_far[right - 1]\n\n        return min_total_len if min_total_len\
        \ != float('inf') else -1"
      c: "int minSumOfLengths(int* arr, int arrSize, int target) {\n    int* best_so_far\
        \ = (int*)malloc(sizeof(int) * arrSize);\n    int INF = 1000000;\n    for (int\
        \ i = 0; i < arrSize; i++) best_so_far[i] = INF;\n\n    int left = 0, current_sum\
        \ = 0, min_total_len = INF;\n\n    for (int right = 0; right < arrSize; right++)\
        \ {\n        current_sum += arr[right];\n        while (current_sum > target)\
        \ {\n            current_sum -= arr[left++];\n        }\n\n        if (current_sum\
        \ == target) {\n            int current_len = right - left + 1;\n          \
        \  if (left > 0 && best_so_far[left - 1] != INF) {\n                int total\
        \ = current_len + best_so_far[left - 1];\n                if (total < min_total_len)\
        \ min_total_len = total;\n            }\n            int prev_best = (right\
        \ > 0) ? best_so_far[right - 1] : INF;\n            best_so_far[right] = (current_len\
        \ < prev_best) ? current_len : prev_best;\n        } else {\n            best_so_far[right]\
        \ = (right > 0) ? best_so_far[right - 1] : INF;\n        }\n    }\n\n    free(best_so_far);\n\
        \    return (min_total_len >= INF) ? -1 : min_total_len;\n}"
      csharp: "public class Solution {\n    public int MinSumOfLengths(int[] arr, int\
        \ target) {\n        int n = arr.Length;\n        int inf = 200001;\n      \
        \  int[] minLen = new int[n];\n        for (int i = 0; i < n; i++) minLen[i]\
        \ = inf;\n        int left = 0, sum = 0, ans = inf;\n        for (int right\
        \ = 0; right < n; right++) {\n            sum += arr[right];\n            while\
        \ (sum > target) {\n                sum -= arr[left++];\n            }\n   \
        \         if (sum == target) {\n                int curLen = right - left +\
        \ 1;\n                if (left > 0 && minLen[left - 1] != inf) {\n         \
        \           ans = System.Math.Min(ans, minLen[left - 1] + curLen);\n       \
        \         }\n                minLen[right] = System.Math.Min((right > 0 ? minLen[right\
        \ - 1] : inf), curLen);\n            } else {\n                minLen[right]\
        \ = (right > 0 ? minLen[right - 1] : inf);\n            }\n        }\n     \
        \   return ans >= inf ? -1 : ans;\n    }\n}"
      javascript: "/**\n * @param {number[]} arr\n * @param {number} target\n * @return\
        \ {number}\n */\nvar minSumOfLengths = function(arr, target) {\n    let n =\
        \ arr.length;\n    let inf = 200001;\n    let minLen = new Array(n).fill(inf);\n\
        \    let left = 0, sum = 0, ans = inf;\n    for (let right = 0; right < n; right++)\
        \ {\n        sum += arr[right];\n        while (sum > target) {\n          \
        \  sum -= arr[left++];\n        }\n        if (sum === target) {\n         \
        \   let curLen = right - left + 1;\n            if (left > 0 && minLen[left\
        \ - 1] !== inf) {\n                ans = Math.min(ans, minLen[left - 1] + curLen);\n\
        \            }\n            minLen[right] = Math.min((right > 0 ? minLen[right\
        \ - 1] : inf), curLen);\n        } else {\n            minLen[right] = (right\
        \ > 0 ? minLen[right - 1] : inf);\n        }\n    }\n    return ans >= inf ?\
        \ -1 : ans;\n};"
      typescript: "function minSumOfLengths(arr: number[], target: number): number {\n\
        \    let n = arr.length;\n    let inf = 200001;\n    let minLen: number[] =\
        \ new Array(n).fill(inf);\n    let left = 0, sum = 0, ans = inf;\n    for (let\
        \ right = 0; right < n; right++) {\n        sum += arr[right];\n        while\
        \ (sum > target) {\n            sum -= arr[left++];\n        }\n        if (sum\
        \ === target) {\n            let curLen = right - left + 1;\n            if\
        \ (left > 0 && minLen[left - 1] !== inf) {\n                ans = Math.min(ans,\
        \ minLen[left - 1] + curLen);\n            }\n            minLen[right] = Math.min((right\
        \ > 0 ? minLen[right - 1] : inf), curLen);\n        } else {\n            minLen[right]\
        \ = (right > 0 ? minLen[right - 1] : inf);\n        }\n    }\n    return ans\
        \ >= inf ? -1 : ans;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $arr\n     * @param\
        \ Integer $target\n     * @return Integer\n     */\n    function minSumOfLengths($arr,\
        \ $target) {\n        $n = count($arr);\n        $inf = 200001;\n        $minLen\
        \ = array_fill(0, $n, $inf);\n        $left = 0;\n        $sum = 0;\n      \
        \  $ans = $inf;\n        for ($right = 0; $right < $n; $right++) {\n       \
        \     $sum += $arr[$right];\n            while ($sum > $target) {\n        \
        \        $sum -= $arr[$left++];\n            }\n            if ($sum == $target)\
        \ {\n                $curLen = $right - $left + 1;\n                if ($left\
        \ > 0 && $minLen[$left - 1] != $inf) {\n                    $ans = min($ans,\
        \ $minLen[$left - 1] + $curLen);\n                }\n                $minLen[$right]\
        \ = min(($right > 0 ? $minLen[$right - 1] : $inf), $curLen);\n            }\
        \ else {\n                $minLen[$right] = ($right > 0 ? $minLen[$right - 1]\
        \ : $inf);\n            }\n        }\n        return $ans >= $inf ? -1 : $ans;\n\
        \    }\n}"
      swift: "class Solution {\n    func minSumOfLengths(_ arr: [Int], _ target: Int)\
        \ -> Int {\n        let n = arr.count\n        let inf = 200001\n        var\
        \ minLen = [Int](repeating: inf, count: n)\n        var left = 0\n        var\
        \ sum = 0\n        var ans = inf\n        for right in 0..<n {\n           \
        \ sum += arr[right]\n            while sum > target {\n                sum -=\
        \ arr[left]\n                left += 1\n            }\n            if sum ==\
        \ target {\n                let curLen = right - left + 1\n                if\
        \ left > 0 && minLen[left - 1] != inf {\n                    ans = min(ans,\
        \ minLen[left - 1] + curLen)\n                }\n                minLen[right]\
        \ = min((right > 0 ? minLen[right - 1] : inf), curLen)\n            } else {\n\
        \                minLen[right] = (right > 0 ? minLen[right - 1] : inf)\n   \
        \         }\n        }\n        return ans >= inf ? -1 : ans\n    }\n}"
      kotlin: "class Solution {\n    fun minSumOfLengths(arr: IntArray, target: Int):\
        \ Int {\n        val n = arr.size\n        val minLeft = IntArray(n) { 100001\
        \ }\n        var ans = 200002\n        var left = 0\n        var currentSum\
        \ = 0\n        for (right in 0 until n) {\n            if (right > 0) {\n  \
        \              minLeft[right] = minLeft[right - 1]\n            }\n        \
        \    currentSum += arr[right]\n            while (currentSum > target && left\
        \ <= right) {\n                currentSum -= arr[left]\n                left++\n\
        \            }\n            if (currentSum == target) {\n                val\
        \ length = right - left + 1\n                if (left > 0 && minLeft[left -\
        \ 1] <= n) {\n                    if (minLeft[left - 1] + length < ans) {\n\
        \                        ans = minLeft[left - 1] + length\n                \
        \    }\n                }\n                if (length < minLeft[right]) {\n\
        \                    minLeft[right] = length\n                }\n          \
        \  }\n        }\n        return if (ans > n) -1 else ans\n    }\n}"
      dart: "class Solution {\n  int minSumOfLengths(List<int> arr, int target) {\n\
        \    int n = arr.length;\n    List<int> minLeft = List<int>.filled(n, 100001);\n\
        \    int ans = 200002;\n    int left = 0;\n    int currentSum = 0;\n    for\
        \ (int right = 0; right < n; right++) {\n      if (right > 0) {\n        minLeft[right]\
        \ = minLeft[right - 1];\n      }\n      currentSum += arr[right];\n      while\
        \ (currentSum > target && left <= right) {\n        currentSum -= arr[left];\n\
        \        left++;\n      }\n      if (currentSum == target) {\n        int length\
        \ = right - left + 1;\n        if (left > 0 && minLeft[left - 1] <= n) {\n \
        \         if (minLeft[left - 1] + length < ans) {\n            ans = minLeft[left\
        \ - 1] + length;\n          }\n        }\n        if (length < minLeft[right])\
        \ {\n          minLeft[right] = length;\n        }\n      }\n    }\n    return\
        \ (ans > n) ? -1 : ans;\n  }\n}"
      go: "func minSumOfLengths(arr []int, target int) int {\n    n := len(arr)\n  \
        \  minLeft := make([]int, n)\n    for i := range minLeft {\n        minLeft[i]\
        \ = 100001\n    }\n    ans := 200002\n    left := 0\n    currentSum := 0\n \
        \   for right := 0; right < n; right++ {\n        if right > 0 {\n         \
        \   minLeft[right] = minLeft[right-1]\n        }\n        currentSum += arr[right]\n\
        \        for currentSum > target && left <= right {\n            currentSum\
        \ -= arr[left]\n            left++\n        }\n        if currentSum == target\
        \ {\n            length := right - left + 1\n            if left > 0 && minLeft[left-1]\
        \ <= n {\n                if minLeft[left-1]+length < ans {\n              \
        \      ans = minLeft[left-1] + length\n                }\n            }\n  \
        \          if length < minLeft[right] {\n                minLeft[right] = length\n\
        \            }\n        }\n    }\n    if ans > n {\n        return -1\n    }\n\
        \    return ans\n}"
      ruby: "# @param {Integer[]} arr\n# @param {Integer} target\n# @return {Integer}\n\
        def min_sum_of_lengths(arr, target)\n    n = arr.length\n    min_left = Array.new(n,\
        \ 100001)\n    ans = 200002\n    left = 0\n    current_sum = 0\n    (0...n).each\
        \ do |right|\n        if right > 0\n            min_left[right] = min_left[right\
        \ - 1]\n        end\n        current_sum += arr[right]\n        while current_sum\
        \ > target && left <= right\n            current_sum -= arr[left]\n        \
        \    left += 1\n        end\n        if current_sum == target\n            length\
        \ = right - left + 1\n            if left > 0 && min_left[left - 1] <= n\n \
        \               sum_len = min_left[left - 1] + length\n                ans =\
        \ [ans, sum_len].min\n            end\n            min_left[right] = [min_left[right],\
        \ length].min\n        end\n    end\n    ans > n ? -1 : ans\nend"
      scala: "object Solution {\n    def minSumOfLengths(arr: Array[Int], target: Int):\
        \ Int = {\n        val n = arr.length\n        val minLeft = Array.fill(n)(100001)\n\
        \        var ans = 200002\n        var left = 0\n        var currentSum = 0\n\
        \        for (right <- 0 until n) {\n            if (right > 0) {\n        \
        \        minLeft(right) = minLeft(right - 1)\n            }\n            currentSum\
        \ += arr(right)\n            while (currentSum > target && left <= right) {\n\
        \                currentSum -= arr(left)\n                left += 1\n      \
        \      }\n            if (currentSum == target) {\n                val length\
        \ = right - left + 1\n                if (left > 0 && minLeft(left - 1) <= n)\
        \ {\n                    ans = math.min(ans, minLeft(left - 1) + length)\n \
        \               }\n                minLeft(right) = math.min(minLeft(right),\
        \ length)\n            }\n        }\n        if (ans > n) -1 else ans\n    }\n\
        }"
      rust: "impl Solution {\n    pub fn min_sum_of_lengths(arr: Vec<i32>, target: i32)\
        \ -> i32 {\n        let n = arr.len();\n        let mut min_len = vec![n as\
        \ i32 + 1; n];\n        let mut left = 0;\n        let mut sum = 0;\n      \
        \  let mut ans = n as i32 + 1;\n\n        for right in 0..n {\n            sum\
        \ += arr[right];\n            while sum > target {\n                sum -= arr[left];\n\
        \                left += 1;\n            }\n\n            let prev_min_val =\
        \ if right > 0 { min_len[right - 1] } else { n as i32 + 1 };\n\n           \
        \ if sum == target {\n                let curr_len = (right - left + 1) as i32;\n\
        \                if left > 0 {\n                    let prev_sub_min = min_len[left\
        \ - 1];\n                    if prev_sub_min <= n as i32 {\n               \
        \         ans = ans.min(prev_sub_min + curr_len);\n                    }\n \
        \               }\n                min_len[right] = prev_min_val.min(curr_len);\n\
        \            } else {\n                min_len[right] = prev_min_val;\n    \
        \        }\n        }\n\n        if ans > n as i32 { -1 } else { ans }\n   \
        \ }\n}"
      racket: "(define/contract (min-sum-of-lengths arr target)\n  (-> (listof exact-integer?)\
        \ exact-integer? exact-integer?)\n  (let* ([n (length arr)]\n         [arr-vec\
        \ (list->vector arr)]\n         [min-len (make-vector n (+ n 1))]\n        \
        \ [ans (+ n 1)])\n    (let loop ([left 0] [right 0] [curr-sum 0] [res ans])\n\
        \      (if (= right n)\n          (if (> res n) -1 res)\n          (let* ([s1\
        \ (+ curr-sum (vector-ref arr-vec right))])\n            (let-values ([(l s)\
        \ (let shrink-loop ([l-in left] [s-in s1])\n                               \
        \   (if (> s-in target)\n                                      (shrink-loop\
        \ (+ l-in 1) (- s-in (vector-ref arr-vec l-in)))\n                         \
        \             (values l-in s-in)))])\n              (let* ([curr-len (+ (- right\
        \ l) 1)]\n                     [prev-min-val (if (> right 0) (vector-ref min-len\
        \ (- right 1)) (+ n 1))]\n                     [new-res (if (and (= s target)\
        \ (> l 0))\n                                  (let ([prev-sub-min (vector-ref\
        \ min-len (- l 1))])\n                                    (if (<= prev-sub-min\
        \ n)\n                                        (min res (+ prev-sub-min curr-len))\n\
        \                                        res))\n                           \
        \       res)])\n                (if (= s target)\n                    (vector-set!\
        \ min-len right (min prev-min-val curr-len))\n                    (vector-set!\
        \ min-len right prev-min-val))\n                (loop l (+ right 1) s new-res))))))))"
      erlang: "-spec min_sum_of_lengths(Arr :: [integer()], Target :: integer()) ->\
        \ integer().\nmin_sum_of_lengths(Arr, Target) ->\n  N = length(Arr),\n  ArrVec\
        \ = list_to_tuple(Arr),\n  MinLen = array:new([{size, N}, {fixed, true}, {default,\
        \ N + 1}]),\n  Ans = solve(1, 1, 0, N, ArrVec, MinLen, N + 1, Target),\n  if\
        \ Ans > N -> -1; true -> Ans end.\n\nsolve(Right, Left, Sum, N, ArrVec, MinLen,\
        \ Ans, Target) when Right =< N ->\n  Sum1 = Sum + element(Right, ArrVec),\n\
        \  {NextLeft, FinalSum} = shrink(Left, Sum1, Target, ArrVec),\n  PrevMinVal\
        \ = if Right > 1 -> array:get(Right - 2, MinLen); true -> N + 1 end,\n  if\n\
        \    FinalSum == Target ->\n      CurrLen = Right - NextLeft + 1,\n      NewAns\
        \ = if\n        NextLeft > 1 ->\n          PrevSubMin = array:get(NextLeft -\
        \ 2, MinLen),\n          if PrevSubMin =< N -> erlang:min(Ans, PrevSubMin +\
        \ CurrLen);\n             true -> Ans\n          end;\n        true -> Ans\n\
        \      end,\n      NewMinLen = array:set(Right - 1, erlang:min(PrevMinVal, CurrLen),\
        \ MinLen),\n      solve(Right + 1, NextLeft, FinalSum, N, ArrVec, NewMinLen,\
        \ NewAns, Target);\n    true ->\n      NewMinLen = array:set(Right - 1, PrevMinVal,\
        \ MinLen),\n      solve(Right + 1, NextLeft, FinalSum, N, ArrVec, NewMinLen,\
        \ Ans, Target)\n  end;\nsolve(_, _, _, _, _, _, Ans, _) -> Ans.\n\nshrink(Left,\
        \ Sum, Target, ArrVec) when Sum > Target ->\n  shrink(Left + 1, Sum - element(Left,\
        \ ArrVec), Target, ArrVec);\nshrink(Left, Sum, _, _) ->\n  {Left, Sum}."
      elixir: "defmodule Solution do\n  @spec min_sum_of_lengths(arr :: [integer], target\
        \ :: integer) :: integer\n  def min_sum_of_lengths(arr, target) do\n    n =\
        \ length(arr)\n    arr_vec = List.to_tuple(arr)\n\n    {_, ans, _, _} = Enum.reduce(0..(n\
        \ - 1), {%{}, n + 1, 0, 0}, fn right, {min_len_map, ans, left, sum} ->\n   \
        \   sum = sum + elem(arr_vec, right)\n      {sum, left} = shrink(sum, left,\
        \ target, arr_vec)\n\n      prev_min_val = if right > 0, do: Map.get(min_len_map,\
        \ right - 1, n + 1), else: n + 1\n\n      if sum == target do\n        curr_len\
        \ = right - left + 1\n        new_ans = if left > 0 do\n          prev_sub_min\
        \ = Map.get(min_len_map, left - 1, n + 1)\n          if prev_sub_min <= n, do:\
        \ min(ans, prev_sub_min + curr_len), else: ans\n        else\n          ans\n\
        \        end\n        new_min_len_map = Map.put(min_len_map, right, min(prev_min_val,\
        \ curr_len))\n        {new_min_len_map, new_ans, left, sum}\n      else\n  \
        \      new_min_len_map = Map.put(min_len_map, right, prev_min_val)\n       \
        \ {new_min_len_map, ans, left, sum}\n      end\n    end)\n\n    if ans > n,\
        \ do: -1, else: ans\n  end\n\n  defp shrink(sum, left, target, arr_vec) when\
        \ sum > target do\n    shrink(sum - elem(arr_vec, left), left + 1, target, arr_vec)\n\
        \  end\n  defp shrink(sum, left, _target, _arr_vec), do: {sum, left}\nend"
    approach: 'The problem asks for two non-overlapping subarrays that sum to a specific
      target with the minimum combined length. Since all elements in the array are positive,
      we can efficiently find subarrays summing to the target using a sliding window
      (or prefix sums with a hash map). To ensure the two subarrays are non-overlapping,
      we maintain an auxiliary array ''best_so_far'', where best_so_far[i] stores the
      minimum length of a valid subarray found within the prefix arr[0...i].


      As we slide the window from left to right, whenever we find a window [left, right]
      that sums exactly to the target, we have a candidate for the second subarray.
      Its length is (right - left + 1). If there exists a valid subarray that ended
      before index ''left'' (i.e., best_so_far[left - 1] is valid), the sum of their
      lengths (best_so_far[left - 1] + length) is a potential candidate for the minimum
      total length. After checking this, we update best_so_far[right] to be the minimum
      of the length found at the current index and the best length found in previous
      steps. This dynamic programming approach ensures we only consider non-overlapping
      pairs while processing the array in a single pass.'
    time_complexity: O(N) where N is the length of the array. Each pointer in the sliding
      window (left and right) traverses the array at most once, and each update to the
      DP array is O(1).
    space_complexity: O(N) as we store an auxiliary array of size N to keep track of
      the minimum subarray length found up to each index.
    elapsed_time: 260.56128215789795
    model: gemini-3-flash-preview
    generated_at: '2026-09-17 02:48:29 '
---

## Problem #1477: Find Two Non-overlapping Sub-arrays Each With Target Sum

**Difficulty:** Medium

**Topics:** Array, Hash Table, Binary Search, Dynamic Programming, Sliding Window

## Problem Description

<p>You are given an array of integers <code>arr</code> and an integer <code>target</code>.</p>

<p>You have to find <strong>two non-overlapping sub-arrays</strong> of <code>arr</code> each with a sum equal <code>target</code>. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is <strong>minimum</strong>.</p>

<p>Return <em>the minimum sum of the lengths</em> of the two required sub-arrays, or return <code>-1</code> if you cannot find such two sub-arrays.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [3,2,2,4,3], target = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [7,3,4,7], target = 7
<strong>Output:</strong> 2
<strong>Explanation:</strong> Although we have three non-overlapping sub-arrays of sum = 7 ([7], [3,4] and [7]), but we will choose the first and third sub-arrays as the sum of their lengths is 2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [4,3,2,6,2,3,4], target = 6
<strong>Output:</strong> -1
<strong>Explanation:</strong> We have only one sub-array of sum = 6.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= arr[i] &lt;= 1000</code></li>
	<li><code>1 &lt;= target &lt;= 10<sup>8</sup></code></li>
</ul>


## Hints

1. Let's create two arrays prefix and suffix where prefix[i] is the minimum length of sub-array ends before i and has sum = k, suffix[i] is the minimum length of sub-array starting at or after i and has sum = k.

2. The answer we are searching for is min(prefix[i] + suffix[i]) for all values of i from 0 to n-1 where n == arr.length.

3. If you are still stuck with how to build prefix and suffix, you can store for each index i the length of the sub-array starts at i and has sum = k or infinity otherwise, and you can use it to build both prefix and suffix.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for two non-overlapping subarrays that sum to a specific target with the minimum combined length. Since all elements in the array are positive, we can efficiently find subarrays summing to the target using a sliding window (or prefix sums with a hash map). To ensure the two subarrays are non-overlapping, we maintain an auxiliary array 'best_so_far', where best_so_far[i] stores the minimum length of a valid subarray found within the prefix arr[0...i].

As we slide the window from left to right, whenever we find a window [left, right] that sums exactly to the target, we have a candidate for the second subarray. Its length is (right - left + 1). If there exists a valid subarray that ended before index 'left' (i.e., best_so_far[left - 1] is valid), the sum of their lengths (best_so_far[left - 1] + length) is a potential candidate for the minimum total length. After checking this, we update best_so_far[right] to be the minimum of the length found at the current index and the best length found in previous steps. This dynamic programming approach ensures we only consider non-overlapping pairs while processing the array in a single pass.

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang" id="lang-cpp" checked>
  <input type="radio" name="code-lang" id="lang-java">
  <input type="radio" name="code-lang" id="lang-python">
  <input type="radio" name="code-lang" id="lang-python3">
  <input type="radio" name="code-lang" id="lang-c">
  <input type="radio" name="code-lang" id="lang-csharp">
  <input type="radio" name="code-lang" id="lang-javascript">
  <input type="radio" name="code-lang" id="lang-typescript">
  <input type="radio" name="code-lang" id="lang-php">
  <input type="radio" name="code-lang" id="lang-swift">
  <input type="radio" name="code-lang" id="lang-kotlin">
  <input type="radio" name="code-lang" id="lang-dart">
  <input type="radio" name="code-lang" id="lang-go">
  <input type="radio" name="code-lang" id="lang-ruby">
  <input type="radio" name="code-lang" id="lang-scala">
  <input type="radio" name="code-lang" id="lang-rust">
  <input type="radio" name="code-lang" id="lang-racket">
  <input type="radio" name="code-lang" id="lang-erlang">
  <input type="radio" name="code-lang" id="lang-elixir">
  <div class="tab-labels">
    <label for="lang-cpp">C++</label>
    <label for="lang-java">Java</label>
    <label for="lang-python">Python</label>
    <label for="lang-python3">Python3</label>
    <label for="lang-c">C</label>
    <label for="lang-csharp">C#</label>
    <label for="lang-javascript">JavaScript</label>
    <label for="lang-typescript">TypeScript</label>
    <label for="lang-php">PHP</label>
    <label for="lang-swift">Swift</label>
    <label for="lang-kotlin">Kotlin</label>
    <label for="lang-dart">Dart</label>
    <label for="lang-go">Go</label>
    <label for="lang-ruby">Ruby</label>
    <label for="lang-scala">Scala</label>
    <label for="lang-rust">Rust</label>
    <label for="lang-racket">Racket</label>
    <label for="lang-erlang">Erlang</label>
    <label for="lang-elixir">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
class Solution {
public:
    int minSumOfLengths(vector<int>& arr, int target) {
        int n = arr.size();
        vector<int> best_so_far(n, 1e9);
        int left = 0, current_sum = 0, min_total_len = 1e9;

        for (int right = 0; right < n; ++right) {
            current_sum += arr[right];
            while (current_sum > target) {
                current_sum -= arr[left++];
            }

            if (current_sum == target) {
                int current_len = right - left + 1;
                if (left > 0 && best_so_far[left - 1] != 1e9) {
                    min_total_len = min(min_total_len, current_len + best_so_far[left - 1]);
                }
                best_so_far[right] = (right > 0) ? min(best_so_far[right - 1], current_len) : current_len;
            } else {
                best_so_far[right] = (right > 0) ? best_so_far[right - 1] : 1e9;
            }
        }

        return (min_total_len >= 1e9) ? -1 : min_total_len;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minSumOfLengths(int[] arr, int target) {
        int n = arr.length;
        int[] bestSoFar = new int[n];
        java.util.Arrays.fill(bestSoFar, Integer.MAX_VALUE / 2);
        int left = 0, currentSum = 0, minTotalLen = Integer.MAX_VALUE / 2;

        for (int right = 0; right < n; right++) {
            currentSum += arr[right];
            while (currentSum > target) {
                currentSum -= arr[left++];
            }

            if (currentSum == target) {
                int currentLen = right - left + 1;
                if (left > 0 && bestSoFar[left - 1] != Integer.MAX_VALUE / 2) {
                    minTotalLen = Math.min(minTotalLen, currentLen + bestSoFar[left - 1]);
                }
                bestSoFar[right] = (right > 0) ? Math.min(bestSoFar[right - 1], currentLen) : currentLen;
            } else {
                bestSoFar[right] = (right > 0) ? bestSoFar[right - 1] : Integer.MAX_VALUE / 2;
            }
        }

        return (minTotalLen >= Integer.MAX_VALUE / 2) ? -1 : minTotalLen;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)
        best_so_far = [float('inf')] * n
        left = 0
        current_sum = 0
        min_total_len = float('inf')

        for right in range(n):
            current_sum += arr[right]
            while current_sum > target:
                current_sum -= arr[left]
                left += 1

            if current_sum == target:
                current_len = right - left + 1
                if left > 0 and best_so_far[left - 1] != float('inf'):
                    min_total_len = min(min_total_len, current_len + best_so_far[left - 1])
                if right > 0:
                    best_so_far[right] = min(best_so_far[right - 1], current_len)
                else:
                    best_so_far[right] = current_len
            else:
                if right > 0:
                    best_so_far[right] = best_so_far[right - 1]

        return min_total_len if min_total_len != float('inf') else -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        best_so_far = [float('inf')] * n
        left = 0
        current_sum = 0
        min_total_len = float('inf')

        for right in range(n):
            current_sum += arr[right]
            while current_sum > target:
                current_sum -= arr[left]
                left += 1

            if current_sum == target:
                current_len = right - left + 1
                if left > 0 and best_so_far[left - 1] != float('inf'):
                    min_total_len = min(min_total_len, current_len + best_so_far[left - 1])
                best_so_far[right] = min(best_so_far[right - 1], current_len) if right > 0 else current_len
            else:
                if right > 0:
                    best_so_far[right] = best_so_far[right - 1]

        return min_total_len if min_total_len != float('inf') else -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int minSumOfLengths(int* arr, int arrSize, int target) {
    int* best_so_far = (int*)malloc(sizeof(int) * arrSize);
    int INF = 1000000;
    for (int i = 0; i < arrSize; i++) best_so_far[i] = INF;

    int left = 0, current_sum = 0, min_total_len = INF;

    for (int right = 0; right < arrSize; right++) {
        current_sum += arr[right];
        while (current_sum > target) {
            current_sum -= arr[left++];
        }

        if (current_sum == target) {
            int current_len = right - left + 1;
            if (left > 0 && best_so_far[left - 1] != INF) {
                int total = current_len + best_so_far[left - 1];
                if (total < min_total_len) min_total_len = total;
            }
            int prev_best = (right > 0) ? best_so_far[right - 1] : INF;
            best_so_far[right] = (current_len < prev_best) ? current_len : prev_best;
        } else {
            best_so_far[right] = (right > 0) ? best_so_far[right - 1] : INF;
        }
    }

    free(best_so_far);
    return (min_total_len >= INF) ? -1 : min_total_len;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinSumOfLengths(int[] arr, int target) {
        int n = arr.Length;
        int inf = 200001;
        int[] minLen = new int[n];
        for (int i = 0; i < n; i++) minLen[i] = inf;
        int left = 0, sum = 0, ans = inf;
        for (int right = 0; right < n; right++) {
            sum += arr[right];
            while (sum > target) {
                sum -= arr[left++];
            }
            if (sum == target) {
                int curLen = right - left + 1;
                if (left > 0 && minLen[left - 1] != inf) {
                    ans = System.Math.Min(ans, minLen[left - 1] + curLen);
                }
                minLen[right] = System.Math.Min((right > 0 ? minLen[right - 1] : inf), curLen);
            } else {
                minLen[right] = (right > 0 ? minLen[right - 1] : inf);
            }
        }
        return ans >= inf ? -1 : ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} arr
 * @param {number} target
 * @return {number}
 */
var minSumOfLengths = function(arr, target) {
    let n = arr.length;
    let inf = 200001;
    let minLen = new Array(n).fill(inf);
    let left = 0, sum = 0, ans = inf;
    for (let right = 0; right < n; right++) {
        sum += arr[right];
        while (sum > target) {
            sum -= arr[left++];
        }
        if (sum === target) {
            let curLen = right - left + 1;
            if (left > 0 && minLen[left - 1] !== inf) {
                ans = Math.min(ans, minLen[left - 1] + curLen);
            }
            minLen[right] = Math.min((right > 0 ? minLen[right - 1] : inf), curLen);
        } else {
            minLen[right] = (right > 0 ? minLen[right - 1] : inf);
        }
    }
    return ans >= inf ? -1 : ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minSumOfLengths(arr: number[], target: number): number {
    let n = arr.length;
    let inf = 200001;
    let minLen: number[] = new Array(n).fill(inf);
    let left = 0, sum = 0, ans = inf;
    for (let right = 0; right < n; right++) {
        sum += arr[right];
        while (sum > target) {
            sum -= arr[left++];
        }
        if (sum === target) {
            let curLen = right - left + 1;
            if (left > 0 && minLen[left - 1] !== inf) {
                ans = Math.min(ans, minLen[left - 1] + curLen);
            }
            minLen[right] = Math.min((right > 0 ? minLen[right - 1] : inf), curLen);
        } else {
            minLen[right] = (right > 0 ? minLen[right - 1] : inf);
        }
    }
    return ans >= inf ? -1 : ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $target
     * @return Integer
     */
    function minSumOfLengths($arr, $target) {
        $n = count($arr);
        $inf = 200001;
        $minLen = array_fill(0, $n, $inf);
        $left = 0;
        $sum = 0;
        $ans = $inf;
        for ($right = 0; $right < $n; $right++) {
            $sum += $arr[$right];
            while ($sum > $target) {
                $sum -= $arr[$left++];
            }
            if ($sum == $target) {
                $curLen = $right - $left + 1;
                if ($left > 0 && $minLen[$left - 1] != $inf) {
                    $ans = min($ans, $minLen[$left - 1] + $curLen);
                }
                $minLen[$right] = min(($right > 0 ? $minLen[$right - 1] : $inf), $curLen);
            } else {
                $minLen[$right] = ($right > 0 ? $minLen[$right - 1] : $inf);
            }
        }
        return $ans >= $inf ? -1 : $ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minSumOfLengths(_ arr: [Int], _ target: Int) -> Int {
        let n = arr.count
        let inf = 200001
        var minLen = [Int](repeating: inf, count: n)
        var left = 0
        var sum = 0
        var ans = inf
        for right in 0..<n {
            sum += arr[right]
            while sum > target {
                sum -= arr[left]
                left += 1
            }
            if sum == target {
                let curLen = right - left + 1
                if left > 0 && minLen[left - 1] != inf {
                    ans = min(ans, minLen[left - 1] + curLen)
                }
                minLen[right] = min((right > 0 ? minLen[right - 1] : inf), curLen)
            } else {
                minLen[right] = (right > 0 ? minLen[right - 1] : inf)
            }
        }
        return ans >= inf ? -1 : ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minSumOfLengths(arr: IntArray, target: Int): Int {
        val n = arr.size
        val minLeft = IntArray(n) { 100001 }
        var ans = 200002
        var left = 0
        var currentSum = 0
        for (right in 0 until n) {
            if (right > 0) {
                minLeft[right] = minLeft[right - 1]
            }
            currentSum += arr[right]
            while (currentSum > target && left <= right) {
                currentSum -= arr[left]
                left++
            }
            if (currentSum == target) {
                val length = right - left + 1
                if (left > 0 && minLeft[left - 1] <= n) {
                    if (minLeft[left - 1] + length < ans) {
                        ans = minLeft[left - 1] + length
                    }
                }
                if (length < minLeft[right]) {
                    minLeft[right] = length
                }
            }
        }
        return if (ans > n) -1 else ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minSumOfLengths(List<int> arr, int target) {
    int n = arr.length;
    List<int> minLeft = List<int>.filled(n, 100001);
    int ans = 200002;
    int left = 0;
    int currentSum = 0;
    for (int right = 0; right < n; right++) {
      if (right > 0) {
        minLeft[right] = minLeft[right - 1];
      }
      currentSum += arr[right];
      while (currentSum > target && left <= right) {
        currentSum -= arr[left];
        left++;
      }
      if (currentSum == target) {
        int length = right - left + 1;
        if (left > 0 && minLeft[left - 1] <= n) {
          if (minLeft[left - 1] + length < ans) {
            ans = minLeft[left - 1] + length;
          }
        }
        if (length < minLeft[right]) {
          minLeft[right] = length;
        }
      }
    }
    return (ans > n) ? -1 : ans;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minSumOfLengths(arr []int, target int) int {
    n := len(arr)
    minLeft := make([]int, n)
    for i := range minLeft {
        minLeft[i] = 100001
    }
    ans := 200002
    left := 0
    currentSum := 0
    for right := 0; right < n; right++ {
        if right > 0 {
            minLeft[right] = minLeft[right-1]
        }
        currentSum += arr[right]
        for currentSum > target && left <= right {
            currentSum -= arr[left]
            left++
        }
        if currentSum == target {
            length := right - left + 1
            if left > 0 && minLeft[left-1] <= n {
                if minLeft[left-1]+length < ans {
                    ans = minLeft[left-1] + length
                }
            }
            if length < minLeft[right] {
                minLeft[right] = length
            }
        }
    }
    if ans > n {
        return -1
    }
    return ans
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} arr
# @param {Integer} target
# @return {Integer}
def min_sum_of_lengths(arr, target)
    n = arr.length
    min_left = Array.new(n, 100001)
    ans = 200002
    left = 0
    current_sum = 0
    (0...n).each do |right|
        if right > 0
            min_left[right] = min_left[right - 1]
        end
        current_sum += arr[right]
        while current_sum > target && left <= right
            current_sum -= arr[left]
            left += 1
        end
        if current_sum == target
            length = right - left + 1
            if left > 0 && min_left[left - 1] <= n
                sum_len = min_left[left - 1] + length
                ans = [ans, sum_len].min
            end
            min_left[right] = [min_left[right], length].min
        end
    end
    ans > n ? -1 : ans
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minSumOfLengths(arr: Array[Int], target: Int): Int = {
        val n = arr.length
        val minLeft = Array.fill(n)(100001)
        var ans = 200002
        var left = 0
        var currentSum = 0
        for (right <- 0 until n) {
            if (right > 0) {
                minLeft(right) = minLeft(right - 1)
            }
            currentSum += arr(right)
            while (currentSum > target && left <= right) {
                currentSum -= arr(left)
                left += 1
            }
            if (currentSum == target) {
                val length = right - left + 1
                if (left > 0 && minLeft(left - 1) <= n) {
                    ans = math.min(ans, minLeft(left - 1) + length)
                }
                minLeft(right) = math.min(minLeft(right), length)
            }
        }
        if (ans > n) -1 else ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_sum_of_lengths(arr: Vec<i32>, target: i32) -> i32 {
        let n = arr.len();
        let mut min_len = vec![n as i32 + 1; n];
        let mut left = 0;
        let mut sum = 0;
        let mut ans = n as i32 + 1;

        for right in 0..n {
            sum += arr[right];
            while sum > target {
                sum -= arr[left];
                left += 1;
            }

            let prev_min_val = if right > 0 { min_len[right - 1] } else { n as i32 + 1 };

            if sum == target {
                let curr_len = (right - left + 1) as i32;
                if left > 0 {
                    let prev_sub_min = min_len[left - 1];
                    if prev_sub_min <= n as i32 {
                        ans = ans.min(prev_sub_min + curr_len);
                    }
                }
                min_len[right] = prev_min_val.min(curr_len);
            } else {
                min_len[right] = prev_min_val;
            }
        }

        if ans > n as i32 { -1 } else { ans }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-sum-of-lengths arr target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([n (length arr)]
         [arr-vec (list->vector arr)]
         [min-len (make-vector n (+ n 1))]
         [ans (+ n 1)])
    (let loop ([left 0] [right 0] [curr-sum 0] [res ans])
      (if (= right n)
          (if (> res n) -1 res)
          (let* ([s1 (+ curr-sum (vector-ref arr-vec right))])
            (let-values ([(l s) (let shrink-loop ([l-in left] [s-in s1])
                                  (if (> s-in target)
                                      (shrink-loop (+ l-in 1) (- s-in (vector-ref arr-vec l-in)))
                                      (values l-in s-in)))])
              (let* ([curr-len (+ (- right l) 1)]
                     [prev-min-val (if (> right 0) (vector-ref min-len (- right 1)) (+ n 1))]
                     [new-res (if (and (= s target) (> l 0))
                                  (let ([prev-sub-min (vector-ref min-len (- l 1))])
                                    (if (<= prev-sub-min n)
                                        (min res (+ prev-sub-min curr-len))
                                        res))
                                  res)])
                (if (= s target)
                    (vector-set! min-len right (min prev-min-val curr-len))
                    (vector-set! min-len right prev-min-val))
                (loop l (+ right 1) s new-res))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_sum_of_lengths(Arr :: [integer()], Target :: integer()) -> integer().
min_sum_of_lengths(Arr, Target) ->
  N = length(Arr),
  ArrVec = list_to_tuple(Arr),
  MinLen = array:new([{size, N}, {fixed, true}, {default, N + 1}]),
  Ans = solve(1, 1, 0, N, ArrVec, MinLen, N + 1, Target),
  if Ans > N -> -1; true -> Ans end.

solve(Right, Left, Sum, N, ArrVec, MinLen, Ans, Target) when Right =< N ->
  Sum1 = Sum + element(Right, ArrVec),
  {NextLeft, FinalSum} = shrink(Left, Sum1, Target, ArrVec),
  PrevMinVal = if Right > 1 -> array:get(Right - 2, MinLen); true -> N + 1 end,
  if
    FinalSum == Target ->
      CurrLen = Right - NextLeft + 1,
      NewAns = if
        NextLeft > 1 ->
          PrevSubMin = array:get(NextLeft - 2, MinLen),
          if PrevSubMin =< N -> erlang:min(Ans, PrevSubMin + CurrLen);
             true -> Ans
          end;
        true -> Ans
      end,
      NewMinLen = array:set(Right - 1, erlang:min(PrevMinVal, CurrLen), MinLen),
      solve(Right + 1, NextLeft, FinalSum, N, ArrVec, NewMinLen, NewAns, Target);
    true ->
      NewMinLen = array:set(Right - 1, PrevMinVal, MinLen),
      solve(Right + 1, NextLeft, FinalSum, N, ArrVec, NewMinLen, Ans, Target)
  end;
solve(_, _, _, _, _, _, Ans, _) -> Ans.

shrink(Left, Sum, Target, ArrVec) when Sum > Target ->
  shrink(Left + 1, Sum - element(Left, ArrVec), Target, ArrVec);
shrink(Left, Sum, _, _) ->
  {Left, Sum}.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_sum_of_lengths(arr :: [integer], target :: integer) :: integer
  def min_sum_of_lengths(arr, target) do
    n = length(arr)
    arr_vec = List.to_tuple(arr)

    {_, ans, _, _} = Enum.reduce(0..(n - 1), {%{}, n + 1, 0, 0}, fn right, {min_len_map, ans, left, sum} ->
      sum = sum + elem(arr_vec, right)
      {sum, left} = shrink(sum, left, target, arr_vec)

      prev_min_val = if right > 0, do: Map.get(min_len_map, right - 1, n + 1), else: n + 1

      if sum == target do
        curr_len = right - left + 1
        new_ans = if left > 0 do
          prev_sub_min = Map.get(min_len_map, left - 1, n + 1)
          if prev_sub_min <= n, do: min(ans, prev_sub_min + curr_len), else: ans
        else
          ans
        end
        new_min_len_map = Map.put(min_len_map, right, min(prev_min_val, curr_len))
        {new_min_len_map, new_ans, left, sum}
      else
        new_min_len_map = Map.put(min_len_map, right, prev_min_val)
        {new_min_len_map, ans, left, sum}
      end
    end)

    if ans > n, do: -1, else: ans
  end

  defp shrink(sum, left, target, arr_vec) when sum > target do
    shrink(sum - elem(arr_vec, left), left + 1, target, arr_vec)
  end
  defp shrink(sum, left, _target, _arr_vec), do: {sum, left}
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) where N is the length of the array. Each pointer in the sliding window (left and right) traverses the array at most once, and each update to the DP array is O(1).
- **Space Complexity:** O(N) as we store an auxiliary array of size N to keep track of the minimum subarray length found up to each index.
