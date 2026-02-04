---
layout: post
title: "Trionic Array II"
date: 2026-02-04 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Dynamic Programming"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/trionic-array-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    long long maxSumTrionic(vector<int>& nums)\
        \ {\n        int n = nums.size();\n        const long long NEG_INF = -2e17;\n\
        \        long long dp1 = NEG_INF, dp2 = NEG_INF, dp3 = NEG_INF;\n        long\
        \ long dp0 = nums[0];\n        long long ans = NEG_INF;\n\n        for (int\
        \ i = 1; i < n; ++i) {\n            long long n_dp1 = NEG_INF, n_dp2 = NEG_INF,\
        \ n_dp3 = NEG_INF;\n            if (nums[i] > nums[i - 1]) {\n             \
        \   if (dp1 > -1e17 || dp0 > -1e17) n_dp1 = max(dp1, dp0) + nums[i];\n     \
        \           if (dp3 > -1e17 || dp2 > -1e17) n_dp3 = max(dp3, dp2) + nums[i];\n\
        \            } else if (nums[i] < nums[i - 1]) {\n                if (dp2 >\
        \ -1e17 || dp1 > -1e17) n_dp2 = max(dp2, dp1) + nums[i];\n            }\n  \
        \          dp0 = nums[i];\n            dp1 = n_dp1;\n            dp2 = n_dp2;\n\
        \            dp3 = n_dp3;\n            if (dp3 > ans) ans = dp3;\n        }\n\
        \        return ans;\n    }\n};"
      java: "class Solution {\n    public long maxSumTrionic(int[] nums) {\n       \
        \ int n = nums.length;\n        long NEG_INF = -2_000_000_000_000_000_000L;\n\
        \        long dp1 = NEG_INF, dp2 = NEG_INF, dp3 = NEG_INF;\n        long dp0\
        \ = nums[0];\n        long ans = NEG_INF;\n\n        for (int i = 1; i < n;\
        \ i++) {\n            long n_dp1 = NEG_INF, n_dp2 = NEG_INF, n_dp3 = NEG_INF;\n\
        \            if (nums[i] > nums[i - 1]) {\n                if (dp1 > -1_000_000_000_000_000_000L\
        \ || dp0 > -1_000_000_000_000_000_000L)\n                    n_dp1 = Math.max(dp1,\
        \ dp0) + nums[i];\n                if (dp3 > -1_000_000_000_000_000_000L ||\
        \ dp2 > -1_000_000_000_000_000_000L)\n                    n_dp3 = Math.max(dp3,\
        \ dp2) + nums[i];\n            } else if (nums[i] < nums[i - 1]) {\n       \
        \         if (dp2 > -1_000_000_000_000_000_000L || dp1 > -1_000_000_000_000_000_000L)\n\
        \                    n_dp2 = Math.max(dp2, dp1) + nums[i];\n            }\n\
        \            dp0 = nums[i];\n            dp1 = n_dp1;\n            dp2 = n_dp2;\n\
        \            dp3 = n_dp3;\n            if (dp3 > ans) ans = dp3;\n        }\n\
        \        return ans;\n    }\n}"
      python: "class Solution(object):\n    def maxSumTrionic(self, nums):\n       \
        \ \"\"\"\n        :type nums: List[int]\n        :rtype: int\n        \"\"\"\
        \n        n = len(nums)\n        neg_inf = -float('inf')\n        dp1, dp2,\
        \ dp3 = neg_inf, neg_inf, neg_inf\n        dp0 = nums[0]\n        ans = neg_inf\n\
        \        for i in range(1, n):\n            n_dp1, n_dp2, n_dp3 = neg_inf, neg_inf,\
        \ neg_inf\n            if nums[i] > nums[i - 1]:\n                n_dp1 = max(dp1,\
        \ dp0) + nums[i]\n                n_dp3 = max(dp3, dp2) + nums[i]\n        \
        \    elif nums[i] < nums[i - 1]:\n                n_dp2 = max(dp2, dp1) + nums[i]\n\
        \            dp0, dp1, dp2, dp3 = nums[i], n_dp1, n_dp2, n_dp3\n           \
        \ if dp3 > ans: ans = dp3\n        return int(ans)"
      python3: "class Solution:\n    def maxSumTrionic(self, nums: List[int]) -> int:\n\
        \        n = len(nums)\n        neg_inf = -float('inf')\n        dp1, dp2, dp3\
        \ = neg_inf, neg_inf, neg_inf\n        dp0 = nums[0]\n        ans = neg_inf\n\
        \        for i in range(1, n):\n            n_dp1, n_dp2, n_dp3 = neg_inf, neg_inf,\
        \ neg_inf\n            if nums[i] > nums[i - 1]:\n                n_dp1 = max(dp1,\
        \ dp0) + nums[i]\n                n_dp3 = max(dp3, dp2) + nums[i]\n        \
        \    elif nums[i] < nums[i - 1]:\n                n_dp2 = max(dp2, dp1) + nums[i]\n\
        \            dp0, dp1, dp2, dp3 = nums[i], n_dp1, n_dp2, n_dp3\n           \
        \ if dp3 > ans: ans = dp3\n        return int(ans)"
      c: "long long maxSumTrionic(int* nums, int numsSize) {\n    long long neg_inf\
        \ = -2000000000000000000LL;\n    long long threshold = -1000000000000000000LL;\n\
        \    long long dp1 = neg_inf, dp2 = neg_inf, dp3 = neg_inf;\n    long long dp0\
        \ = nums[0];\n    long long ans = neg_inf;\n\n    for (int i = 1; i < numsSize;\
        \ i++) {\n        long long n_dp1 = neg_inf, n_dp2 = neg_inf, n_dp3 = neg_inf;\n\
        \        if (nums[i] > nums[i - 1]) {\n            if (dp1 > threshold || dp0\
        \ > threshold) n_dp1 = (dp1 > dp0 ? dp1 : dp0) + nums[i];\n            if (dp3\
        \ > threshold || dp2 > threshold) n_dp3 = (dp3 > dp2 ? dp3 : dp2) + nums[i];\n\
        \        } else if (nums[i] < nums[i - 1]) {\n            if (dp2 > threshold\
        \ || dp1 > threshold) n_dp2 = (dp2 > dp1 ? dp2 : dp1) + nums[i];\n        }\n\
        \        dp0 = nums[i];\n        dp1 = n_dp1;\n        dp2 = n_dp2;\n      \
        \  dp3 = n_dp3;\n        if (dp3 > ans) ans = dp3;\n    }\n    return ans;\n\
        }"
      csharp: "public class Solution {\n    public long MaxSumTrionic(int[] nums) {\n\
        \        int n = nums.Length;\n        long neg_inf = -2_000_000_000_000_000_000L;\n\
        \        long threshold = -1_000_000_000_000_000_000L;\n        long dp1 = neg_inf,\
        \ dp2 = neg_inf, dp3 = neg_inf;\n        long dp0 = nums[0];\n        long ans\
        \ = neg_inf;\n\n        for (int i = 1; i < n; i++) {\n            long n_dp1\
        \ = neg_inf, n_dp2 = neg_inf, n_dp3 = neg_inf;\n            if (nums[i] > nums[i\
        \ - 1]) {\n                if (dp1 > threshold || dp0 > threshold) n_dp1 = Math.Max(dp1,\
        \ dp0) + nums[i];\n                if (dp3 > threshold || dp2 > threshold) n_dp3\
        \ = Math.Max(dp3, dp2) + nums[i];\n            } else if (nums[i] < nums[i -\
        \ 1]) {\n                if (dp2 > threshold || dp1 > threshold) n_dp2 = Math.Max(dp2,\
        \ dp1) + nums[i];\n            }\n            dp0 = nums[i];\n            dp1\
        \ = n_dp1;\n            dp2 = n_dp2;\n            dp3 = n_dp3;\n           \
        \ if (dp3 > ans) ans = dp3;\n        }\n        return ans;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar maxSumTrionic\
        \ = function(nums) {\n    let n = nums.length;\n    let neg_inf = -Infinity;\n\
        \    let dp1 = neg_inf, dp2 = neg_inf, dp3 = neg_inf;\n    let dp0 = nums[0];\n\
        \    let ans = neg_inf;\n    for (let i = 1; i < n; i++) {\n        let n_dp1\
        \ = neg_inf, n_dp2 = neg_inf, n_dp3 = neg_inf;\n        if (nums[i] > nums[i\
        \ - 1]) {\n            n_dp1 = Math.max(dp1, dp0) + nums[i];\n            n_dp3\
        \ = Math.max(dp3, dp2) + nums[i];\n        } else if (nums[i] < nums[i - 1])\
        \ {\n            n_dp2 = Math.max(dp2, dp1) + nums[i];\n        }\n        dp0\
        \ = nums[i];\n        dp1 = n_dp1;\n        dp2 = n_dp2;\n        dp3 = n_dp3;\n\
        \        if (dp3 > ans) ans = dp3;\n    }\n    return ans;\n};"
      typescript: "function maxSumTrionic(nums: number[]): number {\n    const INF =\
        \ 1000000000000000;\n    let dp1 = -INF, dp2 = -INF, dp3 = -INF;\n    let maxTotal\
        \ = -INF;\n    const n = nums.length;\n    for (let i = 1; i < n; i++) {\n \
        \       const n_i = nums[i];\n        const n_prev = nums[i - 1];\n        if\
        \ (n_i > n_prev) {\n            dp3 = Math.max(dp3 + n_i, dp2 + n_i);\n    \
        \        dp1 = Math.max(dp1 + n_i, n_prev + n_i);\n            dp2 = -INF;\n\
        \        } else if (n_i < n_prev) {\n            dp2 = Math.max(dp2 + n_i, dp1\
        \ + n_i);\n            dp1 = -INF;\n            dp3 = -INF;\n        } else\
        \ {\n            dp1 = -INF;\n            dp2 = -INF;\n            dp3 = -INF;\n\
        \        }\n        if (dp3 > maxTotal) maxTotal = dp3;\n    }\n    return maxTotal;\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function maxSumTrionic($nums) {\n        $INF = 1000000000000000;\n\
        \        $dp1 = -$INF; $dp2 = -$INF; $dp3 = -$INF;\n        $maxTotal = -$INF;\n\
        \        $n = count($nums);\n        for ($i = 1; $i < $n; $i++) {\n       \
        \     $n_i = $nums[$i];\n            $n_prev = $nums[$i - 1];\n            if\
        \ ($n_i > $n_prev) {\n                $dp3 = max($dp3 + $n_i, $dp2 + $n_i);\n\
        \                $dp1 = max($dp1 + $n_i, $n_prev + $n_i);\n                $dp2\
        \ = -$INF;\n            } else if ($n_i < $n_prev) {\n                $dp2 =\
        \ max($dp2 + $n_i, $dp1 + $n_i);\n                $dp1 = -$INF;\n          \
        \      $dp3 = -$INF;\n            } else {\n                $dp1 = -$INF; $dp2\
        \ = -$INF; $dp3 = -$INF;\n            }\n            if ($dp3 > $maxTotal) $maxTotal\
        \ = $dp3;\n        }\n        return $maxTotal;\n    }\n}"
      swift: "class Solution {\n    func maxSumTrionic(_ nums: [Int]) -> Int {\n   \
        \     let INF = 1_000_000_000_000_000\n        var dp1 = -INF, dp2 = -INF, dp3\
        \ = -INF\n        var maxTotal = -INF\n        let n = nums.count\n        for\
        \ i in 1..<n {\n            let n_i = nums[i]\n            let n_prev = nums[i\
        \ - 1]\n            if n_i > n_prev {\n                dp3 = max(dp3 + n_i,\
        \ dp2 + n_i)\n                dp1 = max(dp1 + n_i, n_prev + n_i)\n         \
        \       dp2 = -INF\n            } else if n_i < n_prev {\n                dp2\
        \ = max(dp2 + n_i, dp1 + n_i)\n                dp1 = -INF\n                dp3\
        \ = -INF\n            } else {\n                dp1 = -INF\n               \
        \ dp2 = -INF\n                dp3 = -INF\n            }\n            if dp3\
        \ > maxTotal { maxTotal = dp3 }\n        }\n        return maxTotal\n    }\n\
        }"
      kotlin: "class Solution {\n    fun maxSumTrionic(nums: IntArray): Long {\n   \
        \     val INF = 1_000_000_000_000_000L\n        var dp1 = -INF\n        var\
        \ dp2 = -INF\n        var dp3 = -INF\n        var maxTotal = -INF\n        val\
        \ n = nums.size\n        for (i in 1 until n) {\n            val n_i = nums[i].toLong()\n\
        \            val n_prev = nums[i - 1].toLong()\n            if (n_i > n_prev)\
        \ {\n                dp3 = maxOf(dp3 + n_i, dp2 + n_i)\n                dp1\
        \ = maxOf(dp1 + n_i, n_prev + n_i)\n                dp2 = -INF\n           \
        \ } else if (n_i < n_prev) {\n                dp2 = maxOf(dp2 + n_i, dp1 + n_i)\n\
        \                dp1 = -INF\n                dp3 = -INF\n            } else\
        \ {\n                dp1 = -INF\n                dp2 = -INF\n              \
        \  dp3 = -INF\n            }\n            if (dp3 > maxTotal) maxTotal = dp3\n\
        \        }\n        return maxTotal\n    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int maxSumTrionic(List<int>\
        \ nums) {\n    int INF = 1000000000000000;\n    int dp1 = -INF, dp2 = -INF,\
        \ dp3 = -INF;\n    int maxTotal = -INF;\n    int n = nums.length;\n    for (int\
        \ i = 1; i < n; i++) {\n      int n_i = nums[i];\n      int n_prev = nums[i\
        \ - 1];\n      if (n_i > n_prev) {\n        dp3 = max(dp3 + n_i, dp2 + n_i);\n\
        \        dp1 = max(dp1 + n_i, n_prev + n_i);\n        dp2 = -INF;\n      } else\
        \ if (n_i < n_prev) {\n        dp2 = max(dp2 + n_i, dp1 + n_i);\n        dp1\
        \ = -INF;\n        dp3 = -INF;\n      } else {\n        dp1 = -INF;\n      \
        \  dp2 = -INF;\n        dp3 = -INF;\n      }\n      if (dp3 > maxTotal) maxTotal\
        \ = dp3;\n    }\n    return maxTotal;\n  }\n}"
      go: "func maxSumTrionic(nums []int) int64 {\n    const INF int64 = 1000000000000000\n\
        \    dp1, dp2, dp3 := -INF, -INF, -INF\n    maxTotal := -INF\n    n := len(nums)\n\
        \    for i := 1; i < n; i++ {\n        n_i := int64(nums[i])\n        n_prev\
        \ := int64(nums[i-1])\n        if n_i > n_prev {\n            v3_1 := dp3 +\
        \ n_i\n            v3_2 := dp2 + n_i\n            if v3_1 > v3_2 { dp3 = v3_1\
        \ } else { dp3 = v3_2 }\n            v1_1 := dp1 + n_i\n            v1_2 :=\
        \ n_prev + n_i\n            if v1_1 > v1_2 { dp1 = v1_1 } else { dp1 = v1_2\
        \ }\n            dp2 = -INF\n        } else if n_i < n_prev {\n            v2_1\
        \ := dp2 + n_i\n            v2_2 := dp1 + n_i\n            if v2_1 > v2_2 {\
        \ dp2 = v2_1 } else { dp2 = v2_2 }\n            dp1 = -INF\n            dp3\
        \ = -INF\n        } else {\n            dp1, dp2, dp3 = -INF, -INF, -INF\n \
        \       }\n        if dp3 > maxTotal {\n            maxTotal = dp3\n       \
        \ }\n    }\n    return maxTotal\n}"
      ruby: "def max_sum_trionic(nums)\n  n = nums.length\n  inf = 1_000_000_000_000_000_000\n\
        \  limit = 500_000_000_000_000_000\n  dp1 = -inf\n  dp2 = -inf\n  dp3 = -inf\n\
        \  max_total = -inf\n  (1...n).each do |i|\n    num = nums[i]\n    prev_num\
        \ = nums[i - 1]\n    if num > prev_num\n      next_dp1 = [dp1, prev_num].max\
        \ + num\n      next_dp3 = (dp3 > -limit || dp2 > -limit) ? [dp3, dp2].max +\
        \ num : -inf\n      dp1, dp2, dp3 = next_dp1, -inf, next_dp3\n    elsif num\
        \ < prev_num\n      next_dp2 = (dp2 > -limit || dp1 > -limit) ? [dp2, dp1].max\
        \ + num : -inf\n      dp1, dp2, dp3 = -inf, next_dp2, -inf\n    else\n     \
        \ dp1, dp2, dp3 = -inf, -inf, -inf\n    end\n    max_total = dp3 if dp3 > max_total\n\
        \  end\n  max_total\nend"
      scala: "object Solution {\n    def maxSumTrionic(nums: Array[Int]): Long = {\n\
        \        val n = nums.length\n        val INF = 1000000000000000000L\n     \
        \   val LIMIT = 500000000000000000L\n        var dp1 = -INF\n        var dp2\
        \ = -INF\n        var dp3 = -INF\n        var maxTotal = -INF\n        var i\
        \ = 1\n        while (i < n) {\n            val num = nums(i).toLong\n     \
        \       val prevNum = nums(i - 1).toLong\n            if (num > prevNum) {\n\
        \                val nextDp1 = Math.max(dp1, prevNum) + num\n              \
        \  val nextDp3 = if (dp3 > -LIMIT || dp2 > -LIMIT) Math.max(dp3, dp2) + num\
        \ else -INF\n                dp1 = nextDp1\n                dp2 = -INF\n   \
        \             dp3 = nextDp3\n            } else if (num < prevNum) {\n     \
        \           val nextDp2 = if (dp2 > -LIMIT || dp1 > -LIMIT) Math.max(dp2, dp1)\
        \ + num else -INF\n                dp1 = -INF\n                dp2 = nextDp2\n\
        \                dp3 = -INF\n            } else {\n                dp1 = -INF\n\
        \                dp2 = -INF\n                dp3 = -INF\n            }\n   \
        \         if (dp3 > maxTotal) maxTotal = dp3\n            i += 1\n        }\n\
        \        maxTotal\n    }\n}"
      rust: "impl Solution {\n    pub fn max_sum_trionic(nums: Vec<i32>) -> i64 {\n\
        \        let n = nums.len();\n        let inf: i64 = 1_000_000_000_000_000_000;\n\
        \        let limit: i64 = 500_000_000_000_000_000;\n        let mut dp1 = -inf;\n\
        \        let mut dp2 = -inf;\n        let mut dp3 = -inf;\n        let mut max_total\
        \ = -inf;\n        for i in 1..n {\n            let num = nums[i] as i64;\n\
        \            let prev_num = nums[i - 1] as i64;\n            let (next_dp1,\
        \ next_dp2, next_dp3) = if num > prev_num {\n                let d1 = dp1.max(prev_num)\
        \ + num;\n                let d3 = if dp3 > -limit || dp2 > -limit { dp3.max(dp2)\
        \ + num } else { -inf };\n                (d1, -inf, d3)\n            } else\
        \ if num < prev_num {\n                let d2 = if dp2 > -limit || dp1 > -limit\
        \ { dp2.max(dp1) + num } else { -inf };\n                (-inf, d2, -inf)\n\
        \            } else {\n                (-inf, -inf, -inf)\n            };\n\
        \            dp1 = next_dp1;\n            dp2 = next_dp2;\n            dp3 =\
        \ next_dp3;\n            if dp3 > max_total { max_total = dp3; }\n        }\n\
        \        max_total\n    }\n}"
      racket: "(define/contract (max-sum-trionic nums)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let* ([inf 1000000000000000000]\n         [limit 500000000000000000])\n\
        \    (let loop ([rem-nums (cdr nums)]\n               [prev (car nums)]\n  \
        \             [dp1 (- inf)]\n               [dp2 (- inf)]\n               [dp3\
        \ (- inf)]\n               [max-total (- inf)])\n      (if (null? rem-nums)\n\
        \          max-total\n          (let* ([num (car rem-nums)]\n              \
        \   [new-dp1 (if (> num prev) (+ (max dp1 prev) num) (- inf))]\n           \
        \      [new-dp2 (if (< num prev) (if (or (> dp2 (- limit)) (> dp1 (- limit)))\
        \ (+ (max dp2 dp1) num) (- inf)) (- inf))]\n                 [new-dp3 (if (>\
        \ num prev) (if (or (> dp3 (- limit)) (> dp2 (- limit))) (+ (max dp3 dp2) num)\
        \ (- inf)) (- inf))]\n                 [new-max (max max-total new-dp3)])\n\
        \            (loop (cdr rem-nums) num new-dp1 new-dp2 new-dp3 new-max))))))"
      erlang: "-spec max_sum_trionic(Nums :: [integer()]) -> integer().\nmax_sum_trionic(Nums)\
        \ ->\n  [First | Rest] = Nums,\n  INF = 1000000000000000000,\n  LIMIT = 500000000000000000,\n\
        \  solve(Rest, First, -INF, -INF, -INF, -INF, INF, LIMIT).\n\nsolve([], _Prev,\
        \ _DP1, _DP2, _DP3, MaxTotal, _INF, _LIMIT) ->\n  MaxTotal;\nsolve([Num | Rest],\
        \ Prev, DP1, DP2, DP3, MaxTotal, INF, LIMIT) ->\n  {NextDP1, NextDP2, NextDP3}\
        \ = if\n    Num > Prev ->\n      D1 = erlang:max(DP1, Prev) + Num,\n      D3\
        \ = if (DP3 > -LIMIT) orelse (DP2 > -LIMIT) -> erlang:max(DP3, DP2) + Num; true\
        \ -> -INF end,\n      {D1, -INF, D3};\n    Num < Prev ->\n      D2 = if (DP2\
        \ > -LIMIT) orelse (DP1 > -LIMIT) -> erlang:max(DP2, DP1) + Num; true -> -INF\
        \ end,\n      {-INF, D2, -INF};\n    true ->\n      {-INF, -INF, -INF}\n  end,\n\
        \  solve(Rest, Num, NextDP1, NextDP2, NextDP3, erlang:max(MaxTotal, NextDP3),\
        \ INF, LIMIT)."
      elixir: "defmodule Solution do\n  @spec max_sum_trionic(nums :: [integer]) ::\
        \ integer\n  def max_sum_trionic([first | rest]) do\n    inf = 1_000_000_000_000_000_000\n\
        \    limit = 500_000_000_000_000_000\n    solve(rest, first, -inf, -inf, -inf,\
        \ -inf, inf, limit)\n  end\n\n  defp solve([], _prev, _dp1, _dp2, _dp3, max_total,\
        \ _inf, _limit), do: max_total\n  defp solve([num | rest], prev, dp1, dp2, dp3,\
        \ max_total, inf, limit) do\n    {new_dp1, new_dp2, new_dp3} = cond do\n   \
        \   num > prev ->\n        next_dp1 = max(dp1, prev) + num\n        next_dp3\
        \ = if dp3 > -limit or dp2 > -limit, do: max(dp3, dp2) + num, else: -inf\n \
        \       {next_dp1, -inf, next_dp3}\n      num < prev ->\n        next_dp2 =\
        \ if dp2 > -limit or dp1 > -limit, do: max(dp2, dp1) + num, else: -inf\n   \
        \     {-inf, next_dp2, -inf}\n      true ->\n        {-inf, -inf, -inf}\n  \
        \  end\n    solve(rest, num, new_dp1, new_dp2, new_dp3, max(max_total, new_dp3),\
        \ inf, limit)\n  end\nend"
    approach: 'The problem asks for the maximum sum of a ''trionic subarray'', which
      consists of three consecutive phases: strictly increasing, strictly decreasing,
      and strictly increasing, where each phase contains at least two elements. We use
      dynamic programming to maintain three states: ''dp1'' for the maximum sum of a
      subarray ending at the current index that is in the first strictly increasing
      phase, ''dp2'' for the maximum sum of a subarray that has completed the first
      phase and is in the second strictly decreasing phase, and ''dp3'' for a subarray
      that has completed the first two phases and is in the final strictly increasing
      phase.'
    time_complexity: O(n), where n is the length of the input array. We iterate through
      the array once, and each state update takes constant time.
    space_complexity: O(1) auxiliary space (not counting the input array), as we only
      track the three DP states and a few variables for the current and previous states.
    elapsed_time: 375.88656306266785
    model: gemini-3-flash-preview
    generated_at: '2026-02-04 01:27:12 '
---

## Problem #3640: Trionic Array II

**Difficulty:** Hard

**Topics:** Array, Dynamic Programming

## Problem Description

<p data-end="191" data-start="0">You are given an integer array <code data-end="61" data-start="55">nums</code> of length <code data-end="75" data-start="72">n</code>.</p>

<p data-end="191" data-start="0">A <strong data-end="99" data-is-only-node="" data-start="79">trionic subarray</strong> is a contiguous subarray <code data-end="136" data-start="125">nums[l...r]</code> (with <code data-end="158" data-start="143">0 &lt;= l &lt; r &lt; n</code>) for which there exist indices <code>l &lt; p &lt; q &lt; r</code> such that:</p>

<ul>
	<li data-end="267" data-start="230"><code data-end="241" data-start="230">nums[l...p]</code> is <strong>strictly</strong> increasing,</li>
	<li data-end="307" data-start="270"><code data-end="281" data-start="270">nums[p...q]</code> is <strong>strictly</strong> decreasing,</li>
	<li data-end="347" data-start="310"><code data-end="321" data-start="310">nums[q...r]</code> is <strong>strictly</strong> increasing.</li>
</ul>

<p data-end="609" data-is-last-node="" data-is-only-node="" data-start="349">Return the <strong>maximum</strong> sum of any trionic subarray in <code data-end="417" data-start="411">nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [0,-2,-1,-3,0,2,-1]</span></p>

<p><strong>Output:</strong> <span class="example-io">-4</span></p>

<p><strong>Explanation:</strong></p>

<p data-end="129" data-start="72">Pick <code data-end="99" data-start="92">l = 1</code>, <code data-end="108" data-start="101">p = 2</code>, <code data-end="117" data-start="110">q = 3</code>, <code data-end="126" data-start="119">r = 5</code>:</p>

<ul>
	<li data-end="203" data-start="132"><code data-end="166" data-start="132">nums[l...p] = nums[1...2] = [-2, -1]</code> is strictly increasing (<code data-end="200" data-start="191">-2 &lt; -1</code>).</li>
	<li data-end="277" data-start="206"><code data-end="240" data-start="206">nums[p...q] = nums[2...3] = [-1, -3]</code> is strictly decreasing (<code data-end="274" data-start="265">-1 &gt; -3</code>)</li>
	<li data-end="396" data-start="280"><code data-end="316" data-start="280">nums[q...r] = nums[3...5] = [-3, 0, 2]</code> is strictly increasing (<code data-end="353" data-start="341">-3 &lt; 0 &lt; 2</code>).</li>
	<li data-end="396" data-start="280">Sum = <code>(-2) + (-1) + (-3) + 0 + 2 = -4</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,4,2,7]</span></p>

<p><strong>Output:</strong> <span class="example-io">14</span></p>

<p><strong>Explanation:</strong></p>

<p data-end="519" data-start="462">Pick <code data-end="489" data-start="482">l = 0</code>, <code data-end="498" data-start="491">p = 1</code>, <code data-end="507" data-start="500">q = 2</code>, <code data-end="516" data-start="509">r = 3</code>:</p>

<ul>
	<li data-end="589" data-start="522"><code data-end="554" data-start="522">nums[l...p] = nums[0...1] = [1, 4]</code> is strictly increasing (<code data-end="586" data-start="579">1 &lt; 4</code>).</li>
	<li data-end="659" data-start="592"><code data-end="624" data-start="592">nums[p...q] = nums[1...2] = [4, 2]</code> is strictly decreasing (<code data-end="656" data-start="649">4 &gt; 2</code>).</li>
	<li data-end="754" data-is-last-node="" data-start="662"><code data-end="694" data-start="662">nums[q...r] = nums[2...3] = [2, 7]</code> is strictly increasing (<code data-end="726" data-start="719">2 &lt; 7</code>).</li>
	<li data-end="754" data-is-last-node="" data-start="662">Sum = <code>1 + 4 + 2 + 7 = 14</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li data-end="883" data-start="851"><code data-end="881" data-start="851">4 &lt;= n = nums.length &lt;= 10<sup>5</sup></code></li>
	<li data-end="914" data-start="886"><code data-end="912" data-start="886">-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li data-end="978" data-is-last-node="" data-start="917">It is guaranteed that at least one trionic subarray exists.</li>
</ul>


## Hints

1. Use dynamic programming

2. Let four arrays `dp0...dp3` where `dpk[i]` is the max sum of a subarray ending at `i` after finishing `k` of the four phases (start -> inc -> dec -> inc)

3. Process each `i>0`

4. If `nums[i] > nums[i‑1]`, set `dp1[i]=max(dp1[i‑1]+nums[i], dp0[i‑1]+nums[i])`, `dp3[i]=max(dp3[i‑1]+nums[i], dp2[i‑1]+nums[i])`

5. If `nums[i] < nums[i‑1]`, set `dp2[i]=max(dp2[i‑1]+nums[i], dp1[i‑1]+nums[i])`

6. Always carry over `dp0[i]=dp0[i‑1]+nums[i]` when `nums[i]>nums[i‑1]`

7. Return the maximum value in `dp3`

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the maximum sum of a 'trionic subarray', which consists of three consecutive phases: strictly increasing, strictly decreasing, and strictly increasing, where each phase contains at least two elements. We use dynamic programming to maintain three states: 'dp1' for the maximum sum of a subarray ending at the current index that is in the first strictly increasing phase, 'dp2' for the maximum sum of a subarray that has completed the first phase and is in the second strictly decreasing phase, and 'dp3' for a subarray that has completed the first two phases and is in the final strictly increasing phase.

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
    long long maxSumTrionic(vector<int>& nums) {
        int n = nums.size();
        const long long NEG_INF = -2e17;
        long long dp1 = NEG_INF, dp2 = NEG_INF, dp3 = NEG_INF;
        long long dp0 = nums[0];
        long long ans = NEG_INF;

        for (int i = 1; i < n; ++i) {
            long long n_dp1 = NEG_INF, n_dp2 = NEG_INF, n_dp3 = NEG_INF;
            if (nums[i] > nums[i - 1]) {
                if (dp1 > -1e17 || dp0 > -1e17) n_dp1 = max(dp1, dp0) + nums[i];
                if (dp3 > -1e17 || dp2 > -1e17) n_dp3 = max(dp3, dp2) + nums[i];
            } else if (nums[i] < nums[i - 1]) {
                if (dp2 > -1e17 || dp1 > -1e17) n_dp2 = max(dp2, dp1) + nums[i];
            }
            dp0 = nums[i];
            dp1 = n_dp1;
            dp2 = n_dp2;
            dp3 = n_dp3;
            if (dp3 > ans) ans = dp3;
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
class Solution {
    public long maxSumTrionic(int[] nums) {
        int n = nums.length;
        long NEG_INF = -2_000_000_000_000_000_000L;
        long dp1 = NEG_INF, dp2 = NEG_INF, dp3 = NEG_INF;
        long dp0 = nums[0];
        long ans = NEG_INF;

        for (int i = 1; i < n; i++) {
            long n_dp1 = NEG_INF, n_dp2 = NEG_INF, n_dp3 = NEG_INF;
            if (nums[i] > nums[i - 1]) {
                if (dp1 > -1_000_000_000_000_000_000L || dp0 > -1_000_000_000_000_000_000L)
                    n_dp1 = Math.max(dp1, dp0) + nums[i];
                if (dp3 > -1_000_000_000_000_000_000L || dp2 > -1_000_000_000_000_000_000L)
                    n_dp3 = Math.max(dp3, dp2) + nums[i];
            } else if (nums[i] < nums[i - 1]) {
                if (dp2 > -1_000_000_000_000_000_000L || dp1 > -1_000_000_000_000_000_000L)
                    n_dp2 = Math.max(dp2, dp1) + nums[i];
            }
            dp0 = nums[i];
            dp1 = n_dp1;
            dp2 = n_dp2;
            dp3 = n_dp3;
            if (dp3 > ans) ans = dp3;
        }
        return ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maxSumTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        neg_inf = -float('inf')
        dp1, dp2, dp3 = neg_inf, neg_inf, neg_inf
        dp0 = nums[0]
        ans = neg_inf
        for i in range(1, n):
            n_dp1, n_dp2, n_dp3 = neg_inf, neg_inf, neg_inf
            if nums[i] > nums[i - 1]:
                n_dp1 = max(dp1, dp0) + nums[i]
                n_dp3 = max(dp3, dp2) + nums[i]
            elif nums[i] < nums[i - 1]:
                n_dp2 = max(dp2, dp1) + nums[i]
            dp0, dp1, dp2, dp3 = nums[i], n_dp1, n_dp2, n_dp3
            if dp3 > ans: ans = dp3
        return int(ans)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        neg_inf = -float('inf')
        dp1, dp2, dp3 = neg_inf, neg_inf, neg_inf
        dp0 = nums[0]
        ans = neg_inf
        for i in range(1, n):
            n_dp1, n_dp2, n_dp3 = neg_inf, neg_inf, neg_inf
            if nums[i] > nums[i - 1]:
                n_dp1 = max(dp1, dp0) + nums[i]
                n_dp3 = max(dp3, dp2) + nums[i]
            elif nums[i] < nums[i - 1]:
                n_dp2 = max(dp2, dp1) + nums[i]
            dp0, dp1, dp2, dp3 = nums[i], n_dp1, n_dp2, n_dp3
            if dp3 > ans: ans = dp3
        return int(ans)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
long long maxSumTrionic(int* nums, int numsSize) {
    long long neg_inf = -2000000000000000000LL;
    long long threshold = -1000000000000000000LL;
    long long dp1 = neg_inf, dp2 = neg_inf, dp3 = neg_inf;
    long long dp0 = nums[0];
    long long ans = neg_inf;

    for (int i = 1; i < numsSize; i++) {
        long long n_dp1 = neg_inf, n_dp2 = neg_inf, n_dp3 = neg_inf;
        if (nums[i] > nums[i - 1]) {
            if (dp1 > threshold || dp0 > threshold) n_dp1 = (dp1 > dp0 ? dp1 : dp0) + nums[i];
            if (dp3 > threshold || dp2 > threshold) n_dp3 = (dp3 > dp2 ? dp3 : dp2) + nums[i];
        } else if (nums[i] < nums[i - 1]) {
            if (dp2 > threshold || dp1 > threshold) n_dp2 = (dp2 > dp1 ? dp2 : dp1) + nums[i];
        }
        dp0 = nums[i];
        dp1 = n_dp1;
        dp2 = n_dp2;
        dp3 = n_dp3;
        if (dp3 > ans) ans = dp3;
    }
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public long MaxSumTrionic(int[] nums) {
        int n = nums.Length;
        long neg_inf = -2_000_000_000_000_000_000L;
        long threshold = -1_000_000_000_000_000_000L;
        long dp1 = neg_inf, dp2 = neg_inf, dp3 = neg_inf;
        long dp0 = nums[0];
        long ans = neg_inf;

        for (int i = 1; i < n; i++) {
            long n_dp1 = neg_inf, n_dp2 = neg_inf, n_dp3 = neg_inf;
            if (nums[i] > nums[i - 1]) {
                if (dp1 > threshold || dp0 > threshold) n_dp1 = Math.Max(dp1, dp0) + nums[i];
                if (dp3 > threshold || dp2 > threshold) n_dp3 = Math.Max(dp3, dp2) + nums[i];
            } else if (nums[i] < nums[i - 1]) {
                if (dp2 > threshold || dp1 > threshold) n_dp2 = Math.Max(dp2, dp1) + nums[i];
            }
            dp0 = nums[i];
            dp1 = n_dp1;
            dp2 = n_dp2;
            dp3 = n_dp3;
            if (dp3 > ans) ans = dp3;
        }
        return ans;
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
var maxSumTrionic = function(nums) {
    let n = nums.length;
    let neg_inf = -Infinity;
    let dp1 = neg_inf, dp2 = neg_inf, dp3 = neg_inf;
    let dp0 = nums[0];
    let ans = neg_inf;
    for (let i = 1; i < n; i++) {
        let n_dp1 = neg_inf, n_dp2 = neg_inf, n_dp3 = neg_inf;
        if (nums[i] > nums[i - 1]) {
            n_dp1 = Math.max(dp1, dp0) + nums[i];
            n_dp3 = Math.max(dp3, dp2) + nums[i];
        } else if (nums[i] < nums[i - 1]) {
            n_dp2 = Math.max(dp2, dp1) + nums[i];
        }
        dp0 = nums[i];
        dp1 = n_dp1;
        dp2 = n_dp2;
        dp3 = n_dp3;
        if (dp3 > ans) ans = dp3;
    }
    return ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxSumTrionic(nums: number[]): number {
    const INF = 1000000000000000;
    let dp1 = -INF, dp2 = -INF, dp3 = -INF;
    let maxTotal = -INF;
    const n = nums.length;
    for (let i = 1; i < n; i++) {
        const n_i = nums[i];
        const n_prev = nums[i - 1];
        if (n_i > n_prev) {
            dp3 = Math.max(dp3 + n_i, dp2 + n_i);
            dp1 = Math.max(dp1 + n_i, n_prev + n_i);
            dp2 = -INF;
        } else if (n_i < n_prev) {
            dp2 = Math.max(dp2 + n_i, dp1 + n_i);
            dp1 = -INF;
            dp3 = -INF;
        } else {
            dp1 = -INF;
            dp2 = -INF;
            dp3 = -INF;
        }
        if (dp3 > maxTotal) maxTotal = dp3;
    }
    return maxTotal;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxSumTrionic($nums) {
        $INF = 1000000000000000;
        $dp1 = -$INF; $dp2 = -$INF; $dp3 = -$INF;
        $maxTotal = -$INF;
        $n = count($nums);
        for ($i = 1; $i < $n; $i++) {
            $n_i = $nums[$i];
            $n_prev = $nums[$i - 1];
            if ($n_i > $n_prev) {
                $dp3 = max($dp3 + $n_i, $dp2 + $n_i);
                $dp1 = max($dp1 + $n_i, $n_prev + $n_i);
                $dp2 = -$INF;
            } else if ($n_i < $n_prev) {
                $dp2 = max($dp2 + $n_i, $dp1 + $n_i);
                $dp1 = -$INF;
                $dp3 = -$INF;
            } else {
                $dp1 = -$INF; $dp2 = -$INF; $dp3 = -$INF;
            }
            if ($dp3 > $maxTotal) $maxTotal = $dp3;
        }
        return $maxTotal;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxSumTrionic(_ nums: [Int]) -> Int {
        let INF = 1_000_000_000_000_000
        var dp1 = -INF, dp2 = -INF, dp3 = -INF
        var maxTotal = -INF
        let n = nums.count
        for i in 1..<n {
            let n_i = nums[i]
            let n_prev = nums[i - 1]
            if n_i > n_prev {
                dp3 = max(dp3 + n_i, dp2 + n_i)
                dp1 = max(dp1 + n_i, n_prev + n_i)
                dp2 = -INF
            } else if n_i < n_prev {
                dp2 = max(dp2 + n_i, dp1 + n_i)
                dp1 = -INF
                dp3 = -INF
            } else {
                dp1 = -INF
                dp2 = -INF
                dp3 = -INF
            }
            if dp3 > maxTotal { maxTotal = dp3 }
        }
        return maxTotal
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxSumTrionic(nums: IntArray): Long {
        val INF = 1_000_000_000_000_000L
        var dp1 = -INF
        var dp2 = -INF
        var dp3 = -INF
        var maxTotal = -INF
        val n = nums.size
        for (i in 1 until n) {
            val n_i = nums[i].toLong()
            val n_prev = nums[i - 1].toLong()
            if (n_i > n_prev) {
                dp3 = maxOf(dp3 + n_i, dp2 + n_i)
                dp1 = maxOf(dp1 + n_i, n_prev + n_i)
                dp2 = -INF
            } else if (n_i < n_prev) {
                dp2 = maxOf(dp2 + n_i, dp1 + n_i)
                dp1 = -INF
                dp3 = -INF
            } else {
                dp1 = -INF
                dp2 = -INF
                dp3 = -INF
            }
            if (dp3 > maxTotal) maxTotal = dp3
        }
        return maxTotal
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
  int maxSumTrionic(List<int> nums) {
    int INF = 1000000000000000;
    int dp1 = -INF, dp2 = -INF, dp3 = -INF;
    int maxTotal = -INF;
    int n = nums.length;
    for (int i = 1; i < n; i++) {
      int n_i = nums[i];
      int n_prev = nums[i - 1];
      if (n_i > n_prev) {
        dp3 = max(dp3 + n_i, dp2 + n_i);
        dp1 = max(dp1 + n_i, n_prev + n_i);
        dp2 = -INF;
      } else if (n_i < n_prev) {
        dp2 = max(dp2 + n_i, dp1 + n_i);
        dp1 = -INF;
        dp3 = -INF;
      } else {
        dp1 = -INF;
        dp2 = -INF;
        dp3 = -INF;
      }
      if (dp3 > maxTotal) maxTotal = dp3;
    }
    return maxTotal;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxSumTrionic(nums []int) int64 {
    const INF int64 = 1000000000000000
    dp1, dp2, dp3 := -INF, -INF, -INF
    maxTotal := -INF
    n := len(nums)
    for i := 1; i < n; i++ {
        n_i := int64(nums[i])
        n_prev := int64(nums[i-1])
        if n_i > n_prev {
            v3_1 := dp3 + n_i
            v3_2 := dp2 + n_i
            if v3_1 > v3_2 { dp3 = v3_1 } else { dp3 = v3_2 }
            v1_1 := dp1 + n_i
            v1_2 := n_prev + n_i
            if v1_1 > v1_2 { dp1 = v1_1 } else { dp1 = v1_2 }
            dp2 = -INF
        } else if n_i < n_prev {
            v2_1 := dp2 + n_i
            v2_2 := dp1 + n_i
            if v2_1 > v2_2 { dp2 = v2_1 } else { dp2 = v2_2 }
            dp1 = -INF
            dp3 = -INF
        } else {
            dp1, dp2, dp3 = -INF, -INF, -INF
        }
        if dp3 > maxTotal {
            maxTotal = dp3
        }
    }
    return maxTotal
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def max_sum_trionic(nums)
  n = nums.length
  inf = 1_000_000_000_000_000_000
  limit = 500_000_000_000_000_000
  dp1 = -inf
  dp2 = -inf
  dp3 = -inf
  max_total = -inf
  (1...n).each do |i|
    num = nums[i]
    prev_num = nums[i - 1]
    if num > prev_num
      next_dp1 = [dp1, prev_num].max + num
      next_dp3 = (dp3 > -limit || dp2 > -limit) ? [dp3, dp2].max + num : -inf
      dp1, dp2, dp3 = next_dp1, -inf, next_dp3
    elsif num < prev_num
      next_dp2 = (dp2 > -limit || dp1 > -limit) ? [dp2, dp1].max + num : -inf
      dp1, dp2, dp3 = -inf, next_dp2, -inf
    else
      dp1, dp2, dp3 = -inf, -inf, -inf
    end
    max_total = dp3 if dp3 > max_total
  end
  max_total
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxSumTrionic(nums: Array[Int]): Long = {
        val n = nums.length
        val INF = 1000000000000000000L
        val LIMIT = 500000000000000000L
        var dp1 = -INF
        var dp2 = -INF
        var dp3 = -INF
        var maxTotal = -INF
        var i = 1
        while (i < n) {
            val num = nums(i).toLong
            val prevNum = nums(i - 1).toLong
            if (num > prevNum) {
                val nextDp1 = Math.max(dp1, prevNum) + num
                val nextDp3 = if (dp3 > -LIMIT || dp2 > -LIMIT) Math.max(dp3, dp2) + num else -INF
                dp1 = nextDp1
                dp2 = -INF
                dp3 = nextDp3
            } else if (num < prevNum) {
                val nextDp2 = if (dp2 > -LIMIT || dp1 > -LIMIT) Math.max(dp2, dp1) + num else -INF
                dp1 = -INF
                dp2 = nextDp2
                dp3 = -INF
            } else {
                dp1 = -INF
                dp2 = -INF
                dp3 = -INF
            }
            if (dp3 > maxTotal) maxTotal = dp3
            i += 1
        }
        maxTotal
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn max_sum_trionic(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let inf: i64 = 1_000_000_000_000_000_000;
        let limit: i64 = 500_000_000_000_000_000;
        let mut dp1 = -inf;
        let mut dp2 = -inf;
        let mut dp3 = -inf;
        let mut max_total = -inf;
        for i in 1..n {
            let num = nums[i] as i64;
            let prev_num = nums[i - 1] as i64;
            let (next_dp1, next_dp2, next_dp3) = if num > prev_num {
                let d1 = dp1.max(prev_num) + num;
                let d3 = if dp3 > -limit || dp2 > -limit { dp3.max(dp2) + num } else { -inf };
                (d1, -inf, d3)
            } else if num < prev_num {
                let d2 = if dp2 > -limit || dp1 > -limit { dp2.max(dp1) + num } else { -inf };
                (-inf, d2, -inf)
            } else {
                (-inf, -inf, -inf)
            };
            dp1 = next_dp1;
            dp2 = next_dp2;
            dp3 = next_dp3;
            if dp3 > max_total { max_total = dp3; }
        }
        max_total
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (max-sum-trionic nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([inf 1000000000000000000]
         [limit 500000000000000000])
    (let loop ([rem-nums (cdr nums)]
               [prev (car nums)]
               [dp1 (- inf)]
               [dp2 (- inf)]
               [dp3 (- inf)]
               [max-total (- inf)])
      (if (null? rem-nums)
          max-total
          (let* ([num (car rem-nums)]
                 [new-dp1 (if (> num prev) (+ (max dp1 prev) num) (- inf))]
                 [new-dp2 (if (< num prev) (if (or (> dp2 (- limit)) (> dp1 (- limit))) (+ (max dp2 dp1) num) (- inf)) (- inf))]
                 [new-dp3 (if (> num prev) (if (or (> dp3 (- limit)) (> dp2 (- limit))) (+ (max dp3 dp2) num) (- inf)) (- inf))]
                 [new-max (max max-total new-dp3)])
            (loop (cdr rem-nums) num new-dp1 new-dp2 new-dp3 new-max))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_sum_trionic(Nums :: [integer()]) -> integer().
max_sum_trionic(Nums) ->
  [First | Rest] = Nums,
  INF = 1000000000000000000,
  LIMIT = 500000000000000000,
  solve(Rest, First, -INF, -INF, -INF, -INF, INF, LIMIT).

solve([], _Prev, _DP1, _DP2, _DP3, MaxTotal, _INF, _LIMIT) ->
  MaxTotal;
solve([Num | Rest], Prev, DP1, DP2, DP3, MaxTotal, INF, LIMIT) ->
  {NextDP1, NextDP2, NextDP3} = if
    Num > Prev ->
      D1 = erlang:max(DP1, Prev) + Num,
      D3 = if (DP3 > -LIMIT) orelse (DP2 > -LIMIT) -> erlang:max(DP3, DP2) + Num; true -> -INF end,
      {D1, -INF, D3};
    Num < Prev ->
      D2 = if (DP2 > -LIMIT) orelse (DP1 > -LIMIT) -> erlang:max(DP2, DP1) + Num; true -> -INF end,
      {-INF, D2, -INF};
    true ->
      {-INF, -INF, -INF}
  end,
  solve(Rest, Num, NextDP1, NextDP2, NextDP3, erlang:max(MaxTotal, NextDP3), INF, LIMIT).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_sum_trionic(nums :: [integer]) :: integer
  def max_sum_trionic([first | rest]) do
    inf = 1_000_000_000_000_000_000
    limit = 500_000_000_000_000_000
    solve(rest, first, -inf, -inf, -inf, -inf, inf, limit)
  end

  defp solve([], _prev, _dp1, _dp2, _dp3, max_total, _inf, _limit), do: max_total
  defp solve([num | rest], prev, dp1, dp2, dp3, max_total, inf, limit) do
    {new_dp1, new_dp2, new_dp3} = cond do
      num > prev ->
        next_dp1 = max(dp1, prev) + num
        next_dp3 = if dp3 > -limit or dp2 > -limit, do: max(dp3, dp2) + num, else: -inf
        {next_dp1, -inf, next_dp3}
      num < prev ->
        next_dp2 = if dp2 > -limit or dp1 > -limit, do: max(dp2, dp1) + num, else: -inf
        {-inf, next_dp2, -inf}
      true ->
        {-inf, -inf, -inf}
    end
    solve(rest, num, new_dp1, new_dp2, new_dp3, max(max_total, new_dp3), inf, limit)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n), where n is the length of the input array. We iterate through the array once, and each state update takes constant time.
- **Space Complexity:** O(1) auxiliary space (not counting the input array), as we only track the three DP states and a few variables for the current and previous states.
